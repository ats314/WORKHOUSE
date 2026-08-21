#!/usr/bin/env python3
"""
PMBSF SU(2) Lemma Q — Exact Heat-Bath Block-Conditional Run

This script upgrades the side-8 Lemma Q frozen-exterior block experiment
from block Metropolis to exact SU(2) one-link heat-bath updates.

It tests:
  E[X_p | F_{C^c}] / q_eta,
  E[X_r X_p | F_{C^c}] / (q_eta E[X_r | F_{C^c}]),
  E[Y_r X_p | F_{C^c}] / (q_eta E[Y_r | F_{C^c}]),
where Y_r = X_r * 1_bad.

Exact heat bath:
  Conditional density pi(u) ∝ exp(beta * scalar(qmul(u, H))).
  Since scalar(qmul(u,H)) = dot(u, qconj(H)), this is vMF on S^3 with
      mean  = qconj(H)/||H||,
      kappa = beta ||H||.
  Sampling uses Wood's exact vMF rejection algorithm in dimension 4.
"""

import math
import time
import json
import random
from pathlib import Path
from typing import List, Tuple

import numpy as np
import pandas as pd
import torch

CONFIG = {
    "RUN_NAME": "PMBSF_SU2_LemmaQ_exact_heatbath_side8",
    "L_LIST": [16],
    "BETA_LIST": [3.5],
    "N_CFG_REQUEST": 16,
    "GLOBAL_UPDATE_MODE": "HEATBATH",      # used only if full-link cache is absent
    "THERM_SWEEPS": 400,
    "BETWEEN_SWEEPS": 40,
    "START_MODE": "hot",
    "SAVE_FULL_LINKS": True,
    "REUSE_FULL_LINKS": True,
    "ALLOW_LARGER_CACHE_REUSE": True,
    "KNOWN_CACHE_N_LIST": [32, 24, 16, 64],
    "ETA": 0.005,
    "Q_TARGET": 0.003,
    "BLOCK_UPDATE_MODE": "HEATBATH",
    "BLOCK_SIDE": 8,
    "CORE_MARGIN": 2,
    "N_BLOCKS_PER_CFG": 2,
    "BLOCK_THERM": 160,
    "BLOCK_BETWEEN": 6,
    "BLOCK_SAMPLES": 384,
    "ROOTS_PER_BLOCK": 128,
    "TARGETS_PER_ROOT_PER_DISTANCE": 4,
    "MAX_DISTANCE_L1": 10,
    "H0_DEFAULT": 3.0,
    "RHO0_DEFAULT": 0.7,
    "INITIAL_PROPOSAL_SIGMA": 0.38,
    "BLOCK_PROPOSAL_SIGMA": 0.38,
    "TARGET_ACCEPT": 0.50,
    "ADAPT_DURING_THERM": True,
    "ADAPT_BLOCK_THERM": True,
    "VMF_SMALL_KAPPA": 1e-7,
    "VMF_MAX_REJECTION_ROUNDS": 10000,
    "N_BOOTSTRAP": 400,
    "SEED": 23060524,
    "DEVICE": "cuda" if torch.cuda.is_available() else "cpu",
    "DTYPE": "float32",
    "CACHE_ROOT": "/content/PMBSF_SU2_LemmaQ_cache",
    "OUT_ROOT": "/content/PMBSF_SU2_LemmaQ_heatbath_output",
    "PRINT_EVERY_BLOCK": 4,
}

ORIENTS: List[Tuple[int, int]] = [(0,1), (0,2), (0,3), (1,2), (1,3), (2,3)]


def log(s: str) -> None:
    print(s, flush=True)

def now_id() -> str:
    return time.strftime("%Y%m%d_%H%M%S")

def beta_str(beta: float) -> str:
    return f"{beta:g}".replace(".", "p")

def dtype() -> torch.dtype:
    return torch.float32 if CONFIG["DTYPE"] == "float32" else torch.float64

def ensure_dir(p) -> None:
    Path(p).mkdir(parents=True, exist_ok=True)

def set_seed(seed: int) -> None:
    random.seed(seed)
    np.random.seed(seed)
    torch.manual_seed(seed)
    if torch.cuda.is_available():
        torch.cuda.manual_seed_all(seed)

def periodic_l1(a, b, L: int) -> int:
    a = np.asarray(a)
    b = np.asarray(b)
    d = np.abs(a - b) % L
    d = np.minimum(d, L - d)
    return int(d.sum())

def boot_se_ratio(nums, dens, nboot, seed):
    nums = np.asarray(nums, float)
    dens = np.asarray(dens, float)
    good = np.isfinite(nums) & np.isfinite(dens) & (dens > 0)
    nums, dens = nums[good], dens[good]
    if len(nums) <= 1:
        return np.nan
    rng = np.random.default_rng(seed)
    vals = []
    for _ in range(nboot):
        idx = rng.integers(0, len(nums), size=len(nums))
        vals.append(nums[idx].sum() / max(dens[idx].sum(), 1e-300))
    return float(np.std(vals, ddof=1))

def boot_se_mean(vals, nboot, seed):
    vals = np.asarray(vals, float)
    vals = vals[np.isfinite(vals)]
    if len(vals) <= 1:
        return np.nan
    rng = np.random.default_rng(seed)
    outs = []
    for _ in range(nboot):
        idx = rng.integers(0, len(vals), size=len(vals))
        outs.append(float(np.mean(vals[idx])))
    return float(np.std(outs, ddof=1))

# ======================================================================================
# SU(2) quaternion operations
# ======================================================================================


def qmul(x, y):
    a,b,c,d = x.unbind(-1)
    e,f,g,h = y.unbind(-1)
    return torch.stack((
        a*e - b*f - c*g - d*h,
        a*f + b*e + c*h - d*g,
        a*g - b*h + c*e + d*f,
        a*h + b*g - c*f + d*e,
    ), dim=-1)

def qconj(x):
    return torch.cat((x[..., :1], -x[..., 1:]), dim=-1)

def qnorm(x, eps=1e-12):
    return x / torch.linalg.norm(x, dim=-1, keepdim=True).clamp_min(eps)

def random_su2(shape, device, dt):
    return qnorm(torch.randn(*shape, 4, device=device, dtype=dt))

def random_near_identity(shape, sigma, device, dt):
    axis = torch.randn(*shape, 3, device=device, dtype=dt)
    axis = axis / torch.linalg.norm(axis, dim=-1, keepdim=True).clamp_min(1e-12)
    angle = sigma * torch.randn(*shape, device=device, dtype=dt)
    return torch.cat((torch.cos(angle)[..., None], torch.sin(angle)[..., None] * axis), dim=-1)

def roll_lat(x, direction, shift):
    return torch.roll(x, shifts=shift, dims=direction)

# ======================================================================================
# Exact vMF_4 / SU(2) heat-bath sampler
# ======================================================================================


@torch.no_grad()
def sample_uniform_s3(n: int, device: str, dt: torch.dtype) -> torch.Tensor:
    return qnorm(torch.randn(n, 4, device=device, dtype=dt))

@torch.no_grad()
def rotate_e0_to_mean(y: torch.Tensor, mean: torch.Tensor) -> torch.Tensor:
    e0 = torch.zeros_like(mean)
    e0[:, 0] = 1.0
    close = mean[:, 0] > (1.0 - 1e-7)
    u = e0 - mean
    denom = (u * u).sum(dim=-1, keepdim=True).clamp_min(1e-30)
    proj = (u * y).sum(dim=-1, keepdim=True)
    out = y - 2.0 * u * proj / denom
    out = torch.where(close[:, None], y, out)
    return qnorm(out)

@torch.no_grad()
def sample_vmf4(mean: torch.Tensor, kappa: torch.Tensor) -> torch.Tensor:
    """Exact vMF sampler on S^3 using Wood's rejection algorithm, p=4."""
    device = mean.device.type
    dt = mean.dtype
    n = mean.shape[0]
    out = torch.empty_like(mean)

    small = kappa <= CONFIG["VMF_SMALL_KAPPA"]
    if small.any():
        out[small] = sample_uniform_s3(int(small.sum().item()), device, dt)

    idx = torch.where(~small)[0]
    if idx.numel() == 0:
        return qnorm(out)

    kap = kappa[idx].to(dtype=dt)
    mu = mean[idx].to(dtype=dt)
    m = idx.numel()

    p = 4.0
    b = (-2.0 * kap + torch.sqrt(4.0 * kap * kap + (p - 1.0) ** 2)) / (p - 1.0)
    x0 = (1.0 - b) / (1.0 + b)
    c = kap * x0 + (p - 1.0) * torch.log(torch.clamp(1.0 - x0 * x0, min=1e-30))

    accepted_w = torch.empty(m, device=device, dtype=dt)
    remaining = torch.arange(m, device=device)
    beta_dist = torch.distributions.Beta(
        torch.tensor(1.5, device=device, dtype=dt),
        torch.tensor(1.5, device=device, dtype=dt),
    )

    rounds = 0
    while remaining.numel() > 0:
        rounds += 1
        if rounds > CONFIG["VMF_MAX_REJECTION_ROUNDS"]:
            raise RuntimeError("vMF rejection sampler exceeded VMF_MAX_REJECTION_ROUNDS")
        rr = remaining
        z = beta_dist.sample((rr.numel(),)).to(dtype=dt)
        b_r = b[rr]
        x0_r = x0[rr]
        kap_r = kap[rr]
        c_r = c[rr]
        w = (1.0 - (1.0 + b_r) * z) / torch.clamp(1.0 - (1.0 - b_r) * z, min=1e-30)
        log_accept = kap_r * w + (p - 1.0) * torch.log(torch.clamp(1.0 - x0_r * w, min=1e-30)) - c_r
        log_u = torch.log(torch.rand(rr.numel(), device=device, dtype=dt).clamp_min(1e-30))
        acc = log_u <= log_accept
        if acc.any():
            accepted_w[rr[acc]] = w[acc]
        remaining = rr[~acc]

    v = torch.randn(m, 3, device=device, dtype=dt)
    v = v / torch.linalg.norm(v, dim=-1, keepdim=True).clamp_min(1e-12)
    scale = torch.sqrt(torch.clamp(1.0 - accepted_w * accepted_w, min=0.0))
    y = torch.cat((accepted_w[:, None], scale[:, None] * v), dim=-1)
    x = rotate_e0_to_mean(y, mu)
    out[idx] = x
    return qnorm(out)

@torch.no_grad()
def sample_su2_heatbath_from_staple(H: torch.Tensor, beta: float) -> torch.Tensor:
    """
    H is the quaternion staple used in local score scalar(qmul(U,H)).
    scalar(qmul(U,H)) = dot(U, qconj(H)), so conditional law is vMF:
        mean  = qconj(H)/||H||
        kappa = beta ||H||.
    """
    Hc = qconj(H)
    hnorm = torch.linalg.norm(Hc, dim=-1)
    mean = Hc / hnorm[:, None].clamp_min(1e-12)
    kappa = float(beta) * hnorm
    return sample_vmf4(mean, kappa)

# ======================================================================================
# Full-lattice updates
# ======================================================================================


def make_parity_masks(L, device):
    coords = torch.meshgrid(*[torch.arange(L, device=device) for _ in range(4)], indexing="ij")
    parity = (coords[0] + coords[1] + coords[2] + coords[3]) & 1
    return parity == 0, parity == 1

def initialize_field(L, mode, device, dt):
    if mode == "cold":
        U = torch.zeros(4, L, L, L, L, 4, device=device, dtype=dt)
        U[..., 0] = 1.0
        return U
    if mode == "hot":
        return random_su2((4, L, L, L, L), device, dt)
    raise ValueError(mode)

def compute_staple_full(U, mu):
    H = torch.zeros_like(U[mu])
    U_mu = U[mu]
    for nu in range(4):
        if nu == mu:
            continue
        U_nu = U[nu]
        fwd = qmul(qmul(roll_lat(U_nu, mu, -1), qconj(roll_lat(U_mu, nu, -1))), qconj(U_nu))
        U_nu_m = roll_lat(U_nu, nu, +1)
        bwd = qmul(qmul(qconj(roll_lat(U_nu_m, mu, -1)), qconj(roll_lat(U_mu, nu, +1))), U_nu_m)
        H = H + fwd + bwd
    return H

@torch.no_grad()
def heatbath_sweep_full(U, beta, parity_masks):
    for mu in range(4):
        for mask in parity_masks:
            H = compute_staple_full(U, mu)
            new = sample_su2_heatbath_from_staple(H.reshape(-1, 4), beta).reshape_as(U[mu])
            U[mu] = torch.where(mask[..., None], new, U[mu])
    return U, 1.0

@torch.no_grad()
def metropolis_sweep_full(U, beta, sigma, parity_masks):
    dev = U.device.type
    dt = U.dtype
    acc = 0
    propn = 0
    for mu in range(4):
        for mask in parity_masks:
            H = compute_staple_full(U, mu)
            old = U[mu]
            old_s = qmul(old, H)[..., 0]
            prop = qnorm(qmul(random_near_identity(old.shape[:-1], sigma, dev, dt), old))
            new_s = qmul(prop, H)[..., 0]
            accept = (torch.log(torch.rand_like(old_s).clamp_min(1e-30)) < beta * (new_s - old_s)) & mask
            U[mu] = torch.where(accept[..., None], prop, old)
            acc += int(accept.sum().detach().cpu())
            propn += int(mask.sum().detach().cpu())
    return U, acc / max(propn, 1)

@torch.no_grad()
def run_full_sweeps(U, beta, n, sigma, parity_masks, adapt=False, label=""):
    hist = []
    for s in range(1, n + 1):
        if CONFIG["GLOBAL_UPDATE_MODE"].upper() == "HEATBATH":
            U, a = heatbath_sweep_full(U, beta, parity_masks)
        else:
            U, a = metropolis_sweep_full(U, beta, sigma, parity_masks)
            if adapt and s % 10 == 0:
                r = float(np.mean(hist[-10:])) if hist else a
                if r < CONFIG["TARGET_ACCEPT"] - 0.07:
                    sigma *= 0.92
                elif r > CONFIG["TARGET_ACCEPT"] + 0.07:
                    sigma *= 1.08
                sigma = float(np.clip(sigma, 0.03, 1.50))
        hist.append(a)
        if label and (s == 1 or s == n or s % max(1, n // 5) == 0):
            log(f"    [{label}] sweep={s:5d}/{n:<5d} stat_recent={np.mean(hist[-min(10,len(hist)):]):.4f} sigma={sigma:.5f}")
    return U, sigma, hist

# ======================================================================================
# Cache
# ======================================================================================


def full_cache_path(L, beta, ncfg):
    cache = Path(CONFIG["CACHE_ROOT"])
    ensure_dir(cache)
    stem = f"fullU_L{L}_beta{beta_str(beta)}_N{ncfg}_therm{CONFIG['THERM_SWEEPS']}_between{CONFIG['BETWEEN_SWEEPS']}_seed{CONFIG['SEED']}.pt"
    return cache / stem

@torch.no_grad()
def load_or_generate_full_configs(L, beta):
    nreq = int(CONFIG["N_CFG_REQUEST"])
    p = full_cache_path(L, beta, nreq)
    if CONFIG["REUSE_FULL_LINKS"] and p.exists():
        log(f"[cache] loading requested full links: {p}")
        return torch.load(p, map_location="cpu")[:nreq].contiguous(), {"from_cache": True, "cache_used": str(p), "acceptance_mean": np.nan, "acceptance_std": np.nan}
    if CONFIG["REUSE_FULL_LINKS"] and CONFIG["ALLOW_LARGER_CACHE_REUSE"]:
        for ntry in CONFIG["KNOWN_CACHE_N_LIST"]:
            pp = full_cache_path(L, beta, int(ntry))
            if pp.exists() and int(ntry) >= nreq:
                log(f"[cache] loading larger cache and slicing: {pp}")
                return torch.load(pp, map_location="cpu")[:nreq].contiguous(), {"from_cache": True, "cache_used": str(pp), "acceptance_mean": np.nan, "acceptance_std": np.nan}

    device = CONFIG["DEVICE"]
    dt = dtype()
    parity_masks = make_parity_masks(L, device)
    sigma = float(CONFIG["INITIAL_PROPOSAL_SIGMA"])
    U = initialize_field(L, CONFIG["START_MODE"], device, dt)
    log(f"[init-global] {CONFIG['START_MODE']} L={L} beta={beta} update={CONFIG['GLOBAL_UPDATE_MODE']}")
    U, sigma, _ = run_full_sweeps(U, beta, CONFIG["THERM_SWEEPS"], sigma, parity_masks, adapt=CONFIG["ADAPT_DURING_THERM"], label="therm")

    cfgs = []
    stats = []
    log(f"[collect-global] N_CFG_REQUEST={nreq} BETWEEN={CONFIG['BETWEEN_SWEEPS']}")
    for i in range(1, nreq + 1):
        U, sigma, h = run_full_sweeps(U, beta, CONFIG["BETWEEN_SWEEPS"], sigma, parity_masks, adapt=False)
        stats.extend(h)
        cfgs.append(U.detach().cpu().clone())
        if i == 1 or i == nreq or i % max(1, nreq // 8) == 0:
            log(f"    [global-cfg] {i:4d}/{nreq} stat={np.mean(h):.4f} sigma={sigma:.5f}")
    Uall = torch.stack(cfgs, dim=0).contiguous()
    if CONFIG["SAVE_FULL_LINKS"]:
        torch.save(Uall, p)
        log(f"[saved] {p}")
    if device == "cuda":
        torch.cuda.empty_cache()
    return Uall, {"from_cache": False, "cache_used": str(p), "acceptance_mean": float(np.mean(stats)), "acceptance_std": float(np.std(stats))}

# ======================================================================================
# Local gather / block heat bath
# ======================================================================================


def shift_coords(coords, direction, shift, L):
    out = coords.clone()
    out[:, direction] = (out[:, direction] + int(shift)) % L
    return out

def gather_links(U, mu, coords):
    idx = tuple(coords[:, d].long() for d in range(4))
    return U[mu][idx]

def set_links_(U, mu, coords, vals):
    idx = tuple(coords[:, d].long() for d in range(4))
    U[mu][idx] = vals

def compute_staple_at_coords(U, mu, coords):
    L = U.shape[1]
    H = torch.zeros((coords.shape[0], 4), device=U.device, dtype=U.dtype)
    for nu in range(4):
        if nu == mu:
            continue
        cp_mu = shift_coords(coords, mu, +1, L)
        cp_nu = shift_coords(coords, nu, +1, L)
        cm_nu = shift_coords(coords, nu, -1, L)
        cp_mu_m_nu = shift_coords(cm_nu, mu, +1, L)
        fwd = qmul(qmul(gather_links(U, nu, cp_mu), qconj(gather_links(U, mu, cp_nu))), qconj(gather_links(U, nu, coords)))
        bwd = qmul(qmul(qconj(gather_links(U, nu, cp_mu_m_nu)), qconj(gather_links(U, mu, cm_nu))), gather_links(U, nu, cm_nu))
        H = H + fwd + bwd
    return H

@torch.no_grad()
def heatbath_sweep_block(U, beta, active):
    for mu in range(4):
        for parity in (0, 1):
            coords = active.get((mu, parity))
            if coords is None or coords.numel() == 0:
                continue
            H = compute_staple_at_coords(U, mu, coords)
            new_vals = sample_su2_heatbath_from_staple(H, beta)
            set_links_(U, mu, coords, new_vals)
    return U, 1.0

@torch.no_grad()
def metropolis_sweep_block(U, beta, sigma, active):
    dev = U.device.type
    dt = U.dtype
    acc = 0
    propn = 0
    for mu in range(4):
        for parity in (0, 1):
            coords = active.get((mu, parity))
            if coords is None or coords.numel() == 0:
                continue
            H = compute_staple_at_coords(U, mu, coords)
            old = gather_links(U, mu, coords)
            old_s = qmul(old, H)[..., 0]
            prop = qnorm(qmul(random_near_identity(old.shape[:-1], sigma, dev, dt), old))
            new_s = qmul(prop, H)[..., 0]
            accept = torch.log(torch.rand_like(old_s).clamp_min(1e-30)) < beta * (new_s - old_s)
            set_links_(U, mu, coords, torch.where(accept[..., None], prop, old))
            acc += int(accept.sum().detach().cpu())
            propn += int(coords.shape[0])
    return U, acc / max(propn, 1)

@torch.no_grad()
def run_block_sweeps(U, beta, n, sigma, active, adapt=False):
    hist = []
    for s in range(1, n + 1):
        if CONFIG["BLOCK_UPDATE_MODE"].upper() == "HEATBATH":
            U, a = heatbath_sweep_block(U, beta, active)
        else:
            U, a = metropolis_sweep_block(U, beta, sigma, active)
            if adapt and s % 10 == 0:
                r = float(np.mean(hist[-10:])) if hist else a
                if r < CONFIG["TARGET_ACCEPT"] - 0.08:
                    sigma *= 0.92
                elif r > CONFIG["TARGET_ACCEPT"] + 0.08:
                    sigma *= 1.08
                sigma = float(np.clip(sigma, 0.03, 1.50))
        hist.append(a)
    return U, sigma, hist

# ======================================================================================
# Plaquettes and features
# ======================================================================================


def plaquette_phi_at_coords(U, mu, nu, coords):
    L = U.shape[1]
    cp_mu = shift_coords(coords, mu, +1, L)
    cp_nu = shift_coords(coords, nu, +1, L)
    P = qmul(qmul(qmul(gather_links(U, mu, coords), gather_links(U, nu, cp_mu)), qconj(gather_links(U, mu, cp_nu))), qconj(gather_links(U, nu, coords)))
    return 1.0 - P[..., 0].clamp(-1.0, 1.0)

def forward_staple_component_at_coords(U, mu, nu, coords):
    L = U.shape[1]
    cp_mu = shift_coords(coords, mu, +1, L)
    cp_nu = shift_coords(coords, nu, +1, L)
    return qnorm(qmul(qmul(gather_links(U, nu, cp_mu), qconj(gather_links(U, mu, cp_nu))), qconj(gather_links(U, nu, coords))))

def smooth_indicator(phi, t, eta):
    return torch.sigmoid(torch.clamp((phi.float() - float(t)) / float(eta), -80.0, 80.0))

def compute_phi_all_orientations(U):
    L = U.shape[1]
    coords = torch.stack(torch.meshgrid(*[torch.arange(L, device=U.device) for _ in range(4)], indexing="ij"), dim=-1).reshape(-1, 4)
    return torch.stack([plaquette_phi_at_coords(U, mu, nu, coords).reshape(L, L, L, L) for mu, nu in ORIENTS], dim=0)

def find_threshold(vals, qtarget, eta):
    vals = vals.astype(np.float64)
    lo = float(vals.min() - 10 * eta - 1e-6)
    hi = float(vals.max() + 10 * eta + 1e-6)
    for _ in range(80):
        mid = 0.5 * (lo + hi)
        q = float(np.mean(1.0 / (1.0 + np.exp(-np.clip((vals - mid) / eta, -80, 80)))))
        if q > qtarget:
            lo = mid
        else:
            hi = mid
    t = 0.5 * (lo + hi)
    q = float(np.mean(1.0 / (1.0 + np.exp(-np.clip((vals - t) / eta, -80, 80)))))
    qh = float(np.mean(vals >= t))
    return t, q, qh

def cap_F(rho, a):
    a = max(-1.0, min(1.0, float(a)))
    rho = torch.clamp(rho, -1.0, 1.0)
    return rho * a + torch.sqrt(torch.clamp(1.0 - rho * rho, min=0.0)) * math.sqrt(max(0.0, 1.0 - a * a))

@torch.no_grad()
def estimate_threshold(Uall, L, beta):
    dev = CONFIG["DEVICE"]
    chunks = []
    log("[threshold] computing global phi over all orientations")
    for i in range(Uall.shape[0]):
        U = Uall[i].to(dev)
        chunks.append(compute_phi_all_orientations(U).detach().cpu().reshape(-1).numpy())
        if dev == "cuda":
            del U
            torch.cuda.empty_cache()
    vals = np.concatenate(chunks)
    t, q, qh = find_threshold(vals, CONFIG["Q_TARGET"], CONFIG["ETA"])
    return {"threshold_t": float(t), "q_eta": float(q), "q_hard_emp": float(qh), "phi_mean": float(vals.mean()), "phi_std": float(vals.std()), "phi_q99": float(np.quantile(vals, .99)), "phi_q999": float(np.quantile(vals, .999))}

# ======================================================================================
# Block geometry / pair sampling
# ======================================================================================


def random_anchor(L, side, rng):
    return tuple(int(x) for x in rng.integers(0, L - side + 1, size=4))

def make_block_spec(L, anchor, side, margin, device):
    ranges = [range(anchor[d], anchor[d] + side) for d in range(4)]
    core_lo = [anchor[d] + margin for d in range(4)]
    core_hi = [anchor[d] + side - margin for d in range(4)]
    active = {}
    for mu in range(4):
        coords = []
        for x0 in ranges[0]:
            for x1 in ranges[1]:
                for x2 in ranges[2]:
                    for x3 in ranges[3]:
                        x = [x0, x1, x2, x3]
                        if x[mu] + 1 <= anchor[mu] + side - 1:
                            coords.append(x)
        arr = np.array(coords, dtype=np.int64)
        parity = arr.sum(axis=1) & 1
        for p in (0, 1):
            active[(mu, p)] = torch.as_tensor(arr[parity == p], device=device, dtype=torch.long)
    eye = np.eye(4, dtype=np.int64)
    entries = []
    byori = {}
    for oi, (mu, nu) in enumerate(ORIENTS):
        coords = []
        for x0 in range(core_lo[0], core_hi[0]):
            for x1 in range(core_lo[1], core_hi[1]):
                for x2 in range(core_lo[2], core_hi[2]):
                    for x3 in range(core_lo[3], core_hi[3]):
                        x = np.array([x0, x1, x2, x3], dtype=np.int64)
                        corners = [x, x + eye[mu], x + eye[nu], x + eye[mu] + eye[nu]]
                        if all(core_lo[d] <= c[d] < core_hi[d] for c in corners for d in range(4)):
                            dep = min(min(int(c[d] - anchor[d]), int(anchor[d] + side - 1 - c[d])) for c in corners for d in range(4))
                            coords.append(x.tolist())
                            entries.append({"ori_index": oi, "mu": mu, "nu": nu, "coord": tuple(int(v) for v in x), "depth": int(dep)})
        byori[oi] = {"mu": mu, "nu": nu, "coords": torch.as_tensor(np.array(coords, dtype=np.int64), device=device, dtype=torch.long)}
    return {"anchor": tuple(anchor), "active": active, "entries": entries, "byori": byori, "ncore": len(entries)}

def sample_pairs(spec, L, rng):
    n = spec["ncore"]
    coords = np.array([e["coord"] for e in spec["entries"]], dtype=np.int64)
    roots = rng.choice(n, size=min(CONFIG["ROOTS_PER_BLOCK"], n), replace=False)
    pairs_by_d = {}
    meta = []
    for i in roots:
        ds = np.array([periodic_l1(coords[i], coords[j], L) for j in range(n)], dtype=np.int64)
        for d in range(1, CONFIG["MAX_DISTANCE_L1"] + 1):
            cand = np.where(ds == d)[0]
            cand = cand[cand != i]
            if cand.size == 0:
                continue
            k = min(CONFIG["TARGETS_PER_ROOT_PER_DISTANCE"], int(cand.size))
            for j in rng.choice(cand, size=k, replace=False):
                pairs_by_d.setdefault(d, []).append((int(i), int(j)))
                meta.append({"root_idx": int(i), "target_idx": int(j), "distance_l1": int(d)})
    return pairs_by_d, pd.DataFrame(meta)

@torch.no_grad()
def measure_core(U, spec, beta, t, eta):
    n = spec["ncore"]
    X = np.zeros(n)
    phi_a = np.zeros(n)
    k_a = np.zeros(n)
    rho_a = np.zeros(n)
    g_a = np.zeros(n)
    ptr = {}
    for idx, e in enumerate(spec["entries"]):
        ptr.setdefault(e["ori_index"], []).append(idx)
    a = 1.0 - (float(t) - float(eta))
    for oi, gp in spec["byori"].items():
        coords = gp["coords"]
        if coords.numel() == 0:
            continue
        mu, nu = gp["mu"], gp["nu"]
        idx = np.array(ptr[oi], dtype=np.int64)
        phi = plaquette_phi_at_coords(U, mu, nu, coords)
        x = smooth_indicator(phi, t, eta)
        H = compute_staple_at_coords(U, mu, coords)
        k = torch.linalg.norm(H, dim=-1)
        Hhat = H / k[..., None].clamp_min(1e-12)
        c0 = forward_staple_component_at_coords(U, mu, nu, coords)
        rho = (Hhat * c0).sum(dim=-1).clamp(-1, 1)
        F = cap_F(rho, a)
        gg = beta * k * torch.clamp(1.0 - F, min=0.0)
        X[idx] = x.detach().cpu().numpy()
        phi_a[idx] = phi.detach().cpu().numpy()
        k_a[idx] = k.detach().cpu().numpy()
        rho_a[idx] = rho.detach().cpu().numpy()
        g_a[idx] = gg.detach().cpu().numpy()
    bad = ((k_a < CONFIG["H0_DEFAULT"]) | (rho_a < CONFIG["RHO0_DEFAULT"])).astype(float)
    Y = X * bad
    return X, Y, bad, phi_a, k_a, rho_a, g_a

# ======================================================================================
# Aggregation
# ======================================================================================


def summarize_single(df):
    out = []
    for depth, sub in df.groupby("depth"):
        x = sub["ratio_qcond_over_q"].to_numpy(float)
        out.append({"depth": int(depth), "n": len(x), "mean_ratio": float(np.mean(x)), "mean_boot_se": boot_se_mean(x, CONFIG["N_BOOTSTRAP"], CONFIG["SEED"] + depth), "median_ratio": float(np.median(x)), "q90_ratio": float(np.quantile(x, .90)), "q95_ratio": float(np.quantile(x, .95)), "q99_ratio": float(np.quantile(x, .99)), "max_ratio": float(np.max(x))})
    return pd.DataFrame(out).sort_values("depth")

def finalize_dist(rows, q):
    df = pd.DataFrame(rows)
    if df.empty:
        return pd.DataFrame(), pd.DataFrame(), pd.DataFrame()
    out = []
    for d, sub in df.groupby("distance_l1"):
        pair_num = sub["pair_xx_sum"].to_numpy(float)
        pair_den = (q * q * sub["pair_count"]).to_numpy(float)
        cav_num = sub["lambda_num"].to_numpy(float)
        cav_den = sub["lambda_den"].to_numpy(float)
        root_num = sub["root_num"].to_numpy(float)
        root_den = sub["root_den"].to_numpy(float)
        out.append({"distance_l1": int(d), "n_block_rows": len(sub), "pair_count": int(sub["pair_count"].sum()), "pair_ratio_R2": float(pair_num.sum() / max(pair_den.sum(), 1e-300)), "pair_ratio_R2_boot_se": boot_se_ratio(pair_num, pair_den, CONFIG["N_BOOTSTRAP"], CONFIG["SEED"] + 10*d), "cavity_Lambda": float(cav_num.sum() / max(cav_den.sum(), 1e-300)), "cavity_Lambda_boot_se": boot_se_ratio(cav_num, cav_den, CONFIG["N_BOOTSTRAP"], CONFIG["SEED"] + 20*d), "rooted_Lambda": float(root_num.sum() / max(root_den.sum(), 1e-300)), "rooted_Lambda_boot_se": boot_se_ratio(root_num, root_den, CONFIG["N_BOOTSTRAP"], CONFIG["SEED"] + 30*d), "lambda_den": float(cav_den.sum()), "root_den": float(root_den.sum())})
    agg = pd.DataFrame(out).sort_values("distance_l1")
    return agg[["distance_l1", "pair_count", "pair_ratio_R2", "pair_ratio_R2_boot_se"]], agg[["distance_l1", "pair_count", "cavity_Lambda", "cavity_Lambda_boot_se", "lambda_den"]], agg[["distance_l1", "pair_count", "rooted_Lambda", "rooted_Lambda_boot_se", "root_den"]]

def cap_regression(df):
    out = []
    eps = 1e-300
    d = df[np.isfinite(df["g_mean"]) & (df["q_cond"] > 0)].copy()
    for pred in ["g_mean", "rho_mean", "k_mean"]:
        if len(d) < 3:
            continue
        x = d[pred].to_numpy(float)
        y = np.log(d["q_cond"].to_numpy(float) + eps)
        Xmat = np.vstack([np.ones_like(x), x]).T
        coef, _, _, _ = np.linalg.lstsq(Xmat, y, rcond=None)
        yhat = Xmat @ coef
        r2 = 1 - float(np.sum((y - yhat)**2)) / max(float(np.sum((y - y.mean())**2)), 1e-300)
        out.append({"predictor": pred, "n": len(d), "intercept": float(coef[0]), "slope": float(coef[1]), "r2": float(r2)})
    return pd.DataFrame(out)

# ======================================================================================
# Block experiment
# ======================================================================================

@torch.no_grad()
def run_combo(Uall, L, beta, thr):
    dev = CONFIG["DEVICE"]
    q = float(thr["q_eta"])
    t = float(thr["threshold_t"])
    rng = np.random.default_rng(CONFIG["SEED"] + int(1000 * beta) + L + 9000)
    single, bsum, distrows, metas = [], [], [], []
    block_counter = 0
    total = Uall.shape[0] * CONFIG["N_BLOCKS_PER_CFG"]
    for ci in range(Uall.shape[0]):
        for _ in range(CONFIG["N_BLOCKS_PER_CFG"]):
            block_counter += 1
            anchor = random_anchor(L, CONFIG["BLOCK_SIDE"], rng)
            spec = make_block_spec(L, anchor, CONFIG["BLOCK_SIDE"], CONFIG["CORE_MARGIN"], dev)
            n = spec["ncore"]
            pairs_by_d, meta = sample_pairs(spec, L, rng)
            if len(meta):
                meta["cfg_idx"] = ci
                meta["block_idx"] = block_counter
                meta["anchor"] = str(anchor)
                metas.append(meta)
            U = Uall[ci].to(dev).clone()
            sigma = float(CONFIG["BLOCK_PROPOSAL_SIGMA"])
            U, sigma, therm_stats = run_block_sweeps(U, beta, CONFIG["BLOCK_THERM"], sigma, spec["active"], adapt=CONFIG["ADAPT_BLOCK_THERM"])
            sumX = np.zeros(n); sumY = np.zeros(n); sumbad = np.zeros(n)
            sumphi = np.zeros(n); sumk = np.zeros(n); sumrho = np.zeros(n); sumg = np.zeros(n)
            sample_stats = []
            dacc = {d: {"pair_xx_sum": 0.0, "pair_count": float(len(pairs)), "lambda_num": 0.0, "sumXroot": 0.0, "root_num": 0.0, "sumYroot": 0.0} for d, pairs in pairs_by_d.items()}
            for _s in range(CONFIG["BLOCK_SAMPLES"]):
                U, sigma, h = run_block_sweeps(U, beta, CONFIG["BLOCK_BETWEEN"], sigma, spec["active"], adapt=False)
                sample_stats.extend(h)
                X, Y, bad, phi, k, rho, g = measure_core(U, spec, beta, t, CONFIG["ETA"])
                sumX += X; sumY += Y; sumbad += bad; sumphi += phi; sumk += k; sumrho += rho; sumg += g
                for d, pairs in pairs_by_d.items():
                    if not pairs:
                        continue
                    ii = np.fromiter((p[0] for p in pairs), dtype=np.int64)
                    jj = np.fromiter((p[1] for p in pairs), dtype=np.int64)
                    dacc[d]["pair_xx_sum"] += float(np.sum(X[ii] * X[jj]))
                    dacc[d]["lambda_num"] += float(np.sum(X[ii] * X[jj]))
                    dacc[d]["sumXroot"] += float(np.sum(X[ii]))
                    dacc[d]["root_num"] += float(np.sum(Y[ii] * X[jj]))
                    dacc[d]["sumYroot"] += float(np.sum(Y[ii]))
            den = float(CONFIG["BLOCK_SAMPLES"])
            bx = sumX / den; by = sumY / den; bbad = sumbad / den
            bphi = sumphi / den; bk = sumk / den; brho = sumrho / den; bg = sumg / den
            for i, e in enumerate(spec["entries"]):
                single.append({"L": L, "beta": beta, "cfg_idx": ci, "block_idx": block_counter, "anchor": str(anchor), "plaquette_local_idx": i, "ori_index": e["ori_index"], "mu": e["mu"], "nu": e["nu"], "coord": str(e["coord"]), "depth": e["depth"], "threshold_t": t, "q_eta": q, "q_cond": float(bx[i]), "ratio_qcond_over_q": float(bx[i] / max(q, 1e-300)), "root_bad_cond": float(by[i]), "root_bad_ratio_over_q": float(by[i] / max(q, 1e-300)), "bad_prob_cond": float(bbad[i]), "phi_mean": float(bphi[i]), "k_mean": float(bk[i]), "rho_mean": float(brho[i]), "g_mean": float(bg[i])})
            for d, r in dacc.items():
                distrows.append({"L": L, "beta": beta, "cfg_idx": ci, "block_idx": block_counter, "anchor": str(anchor), "distance_l1": int(d), "pair_xx_sum": r["pair_xx_sum"] / den, "pair_count": r["pair_count"], "lambda_num": r["lambda_num"] / den, "lambda_den": q * (r["sumXroot"] / den), "root_num": r["root_num"] / den, "root_den": q * (r["sumYroot"] / den)})
            bsum.append({"L": L, "beta": beta, "cfg_idx": ci, "block_idx": block_counter, "anchor": str(anchor), "n_core_plaquettes": int(n), "n_sampled_pairs": int(sum(len(v) for v in pairs_by_d.values())), "block_update_mode": CONFIG["BLOCK_UPDATE_MODE"], "block_therm_stat_mean": float(np.mean(therm_stats)), "block_sample_stat_mean": float(np.mean(sample_stats)), "block_sample_stat_std": float(np.std(sample_stats)), "q_cond_mean_over_core": float(np.mean(bx)), "q_cond_median_over_core": float(np.median(bx)), "ratio_qcond_mean_over_q": float(np.mean(bx) / max(q, 1e-300)), "ratio_qcond_median_over_q": float(np.median(bx) / max(q, 1e-300)), "bad_prob_mean_over_core": float(np.mean(bbad)), "root_bad_mean_over_core": float(np.mean(by))})
            if block_counter == 1 or block_counter == total or block_counter % max(1, CONFIG["PRINT_EVERY_BLOCK"]) == 0:
                log(f"    [block] {block_counter:4d}/{total} cfg={ci} anchor={anchor} ncore={n} pairs={sum(len(v) for v in pairs_by_d.values())} qcond/q={np.mean(bx)/max(q,1e-300):.3f} update_stat={np.mean(sample_stats):.4f}")
            if dev == "cuda":
                del U
                torch.cuda.empty_cache()
    single_df = pd.DataFrame(single)
    pair, cav, root = finalize_dist(distrows, q)
    return {"single_source_depth": single_df, "single_source_depth_summary": summarize_single(single_df), "boundary_block_summary": pd.DataFrame(bsum), "pair_ratio_by_distance": pair, "cavity_ratio_by_distance": cav, "rooted_cavity_ratio_by_distance": root, "cap_feature_scan": single_df.copy(), "cap_feature_regression": cap_regression(single_df), "sampled_pair_metadata": pd.concat(metas, ignore_index=True) if metas else pd.DataFrame()}

# ======================================================================================
# Driver
# ======================================================================================

def run():
    set_seed(CONFIG["SEED"])
    run_id = f"{CONFIG['RUN_NAME']}_{now_id()}"
    outdir = Path(CONFIG["OUT_ROOT"]) / run_id
    ensure_dir(outdir)
    log("=" * 100)
    log(f"[run] {run_id}")
    log(f"[device] {CONFIG['DEVICE']}")
    if CONFIG["DEVICE"] == "cuda":
        log(f"[gpu] {torch.cuda.get_device_name(0)}")
    log(f"[outdir] {outdir}")
    log("=" * 100)
    start = time.time()
    summaries = []
    outputs = {k: [] for k in ["single_source_depth", "single_source_depth_summary", "boundary_block_summary", "pair_ratio_by_distance", "cavity_ratio_by_distance", "rooted_cavity_ratio_by_distance", "cap_feature_scan", "cap_feature_regression", "sampled_pair_metadata"]}
    for L in CONFIG["L_LIST"]:
        for beta in CONFIG["BETA_LIST"]:
            combo_start = time.time()
            log("=" * 100)
            log(f"[combo] L={L} beta={beta}")
            log("=" * 100)
            Uall, gen = load_or_generate_full_configs(L, beta)
            thr = estimate_threshold(Uall, L, beta)
            log("[threshold summary]")
            for k, v in thr.items():
                log(f"  {k}: {v}")
            out = run_combo(Uall, L, beta, thr)
            for k, df in out.items():
                if not df.empty:
                    outputs[k].append(df)
            summ = {"L": L, "beta": beta, **gen, **thr, "combo_elapsed_min": (time.time() - combo_start) / 60.0}
            ss = out["single_source_depth_summary"]
            if not ss.empty:
                summ["max_depth_median_ratio"] = float(ss["median_ratio"].max())
                summ["max_depth_q95_ratio"] = float(ss["q95_ratio"].max())
                summ["max_depth_q99_ratio"] = float(ss["q99_ratio"].max())
                summ["max_depth_max_ratio"] = float(ss["max_ratio"].max())
            cav = out["cavity_ratio_by_distance"]
            root = out["rooted_cavity_ratio_by_distance"]
            if not cav.empty:
                summ["max_cavity_Lambda"] = float(cav["cavity_Lambda"].replace([np.inf, -np.inf], np.nan).max())
                summ["median_cavity_Lambda"] = float(cav["cavity_Lambda"].replace([np.inf, -np.inf], np.nan).median())
            if not root.empty:
                summ["max_rooted_Lambda"] = float(root["rooted_Lambda"].replace([np.inf, -np.inf], np.nan).max())
                summ["median_rooted_Lambda"] = float(root["rooted_Lambda"].replace([np.inf, -np.inf], np.nan).median())
            reg = out["cap_feature_regression"]
            if not reg.empty and len(reg[reg["predictor"] == "g_mean"]):
                grow = reg[reg["predictor"] == "g_mean"].iloc[0]
                summ["cap_g_slope"] = float(grow["slope"])
                summ["cap_g_r2"] = float(grow["r2"])
            summaries.append(summ)
            log("[combo summary]")
            for k, v in summ.items():
                log(f"  {k}: {v:.8g}" if isinstance(v, float) else f"  {k}: {v}")
    elapsed = (time.time() - start) / 60.0
    fs = pd.DataFrame(summaries)
    fs.to_csv(outdir / "full_config_summary.csv", index=False)
    merged = {}
    for k, dfs in outputs.items():
        df = pd.concat(dfs, ignore_index=True) if dfs else pd.DataFrame()
        merged[k] = df
        df.to_csv(outdir / f"{k}.csv", index=False)
    read = []
    read += ["# PMBSF SU(2) Lemma Q Exact Heat-Bath Side-8 Readout", "", "Finite-volume frozen-exterior block-conditional diagnostic. Not a proof of Lemma Q.", "", "## Config", "", "```json", json.dumps(CONFIG, indent=2, sort_keys=True), "```", "", f"Elapsed minutes: `{elapsed:.3f}`", "", "## Full/global summary", "", fs.to_markdown(index=False), ""]
    for title, k in [("Table A. Single-source conditional control", "single_source_depth_summary"), ("Pair ratio by distance", "pair_ratio_by_distance"), ("Cavity ratio by distance", "cavity_ratio_by_distance"), ("Rooted cavity ratio by distance", "rooted_cavity_ratio_by_distance"), ("Feature discrimination", "cap_feature_regression")]:
        if not merged[k].empty:
            read += [f"## {title}", "", merged[k].to_markdown(index=False), ""]
    read += ["## Decision rules", "", "- Strong pass: median q_cond/q <= 1.5, q95 <= 3, cavity/rooted medians <= 1.5, cavity/rooted maxima <= 4.", "- Useful but noisy pass: medians controlled, q95 <= 4, maxima explained by sparse denominators.", "- Fail: median q_cond/q > 2 or cavity/rooted ratios grow badly with distance.", ""]
    (outdir / "RUN_READOUT.md").write_text("\n".join(read), encoding="utf-8")
    log("=" * 100)
    log(f"[done] elapsed={elapsed:.2f} min")
    for p in ["full_config_summary.csv", "single_source_depth.csv", "single_source_depth_summary.csv", "boundary_block_summary.csv", "pair_ratio_by_distance.csv", "DATA_PMBSF_cavity_ratio_by_distance.csv", "rooted_DATA_PMBSF_cavity_ratio_by_distance.csv", "cap_feature_scan.csv", "cap_feature_regression.csv", "sampled_pair_metadata.csv", "RUN_READOUT.md"]:
        log(f"[saved] {outdir / p}")
    log("=" * 100)
    log("[final summary]")
    log(fs.to_string(index=False))

if __name__ == "__main__":
    run()
