#!/usr/bin/env python3
"""
PMBSF SU(2) Lemma Q Block-Conditional Diagnostic — Stage B (block geometry)

Drop-in successor to Stage A. Same diagnostic, larger blocks:

  BLOCK_SIDE:        6  -> 10   (block volume 6^4=1296 -> 10^4=10000 sites)
  CORE_MARGIN:       2  -> 3    (core extent 2 -> 4 sites per dim)
  N_BLOCKS_PER_CFG:  4  -> 2    (cuts total blocks 128 -> 64 to bound wallclock)
  BLOCK_THERM:       128 -> 256 (larger interior needs more sweeps)
  BLOCK_BETWEEN:     8  -> 10   (slightly longer decorrelation)
  Core plaquettes:   24 -> 864  (per block, 36x more)

Plus one essential optimisation: pair-distance accumulation vectorised in numpy.
At 864 plaquettes per block, the original nested-Python loop (24^2=576 ops/block,
fine at Stage A) would be 864^2 ~ 7.5e5 ops/block; vectorising via masked
broadcast over a precomputed pairwise distance matrix is required.

What Stage B delivers that Stage A could not:

  1. Per-distance fits over d in {0, 1, 2, 3, 4, 5, 6, 7, 8} -- up to 9 reliable
     bins instead of Stage A's 3. This shrinks the bootstrap 95% CI on the decay
     rate m from factor-20 (Stage A: m in [0.10, 2.27]) to roughly factor-3.

  2. Depth analysis becomes possible: at margin=3, core sites have plaquette
     depth in {3, 4} (vs Stage A's single value 2).

  3. ~864 core plaquettes per block (vs 24): tighter within-block statistics
     on every metric.

Wallclock estimate: ~5-7 hours on an A100, comparable to Stage A's 5.4 hours.
The 36x more measurements per block is partly offset by 2x fewer blocks and
mostly by the fact that block sweeps -- not measurements -- dominate runtime,
and sweep cost scales as block_side^4 (7.7x) not as core_plaquettes (36x).

Outputs follow Stage A's schema (so existing analysis pipelines work):

  full_config_summary.csv
  single_source_depth.csv
  single_source_depth_summary.csv
  DATA_PMBSF_cavity_ratio_by_distance.csv          (NEW: was missing in Stage A upload)
  rooted_DATA_PMBSF_cavity_ratio_by_distance.csv
  pair_ratio_by_distance.csv
  cap_feature_scan.csv
  cap_feature_regression.csv
  boundary_block_summary.csv
  RUN_READOUT.md
"""

import os
import math
import time
import json
import random
from pathlib import Path
from typing import Dict, List, Tuple, Any

import numpy as np
import pandas as pd
import torch


# ======================================================================================
# CONFIG -- Stage B geometry change
# ======================================================================================

CONFIG = {
    "RUN_NAME": "PMBSF_SU2_LemmaQ_block_conditional_stageB_geometry",

    # Global ensemble -- unchanged from Stage A so the cached fullU.pt can be reused
    # IF you keep SEED the same.  We use a fresh seed for cleanliness; cost is +30 min
    # to regenerate the Wilson ensemble, which is small compared to the block runs.
    # To reuse Stage A's cache instead, set SEED = 23060524.
    "L_LIST": [16],
    "BETA_LIST": [3.5],
    "N_CFG": 32,
    "THERM_SWEEPS": 400,
    "BETWEEN_SWEEPS": 40,
    "START_MODE": "hot",
    "ETA": 0.005,
    "Q_TARGET": 0.003,
    "SAVE_FULL_LINKS": True,
    "REUSE_FULL_LINKS": True,

    # Block-conditional experiment -- STAGE B CHANGES HERE
    "BLOCK_SIDE": 10,           # was 6
    "CORE_MARGIN": 3,           # was 2
    "N_BLOCKS_PER_CFG": 2,      # was 4; halved because each block is now 36x heavier on measurement
    "BLOCK_THERM": 256,         # was 128; larger interior needs more equilibration
    "BLOCK_BETWEEN": 10,        # was 8
    "BLOCK_SAMPLES": 256,
    "UPDATE_MODE": "METROPOLIS",

    # Local source diagnostics
    "MEASURE_ALL_CORE_PLAQUETTES": True,
    "COMPUTE_PAIR_BY_DISTANCE": True,
    "COMPUTE_ROOTED_BAD": True,
    "H0_GRID": [3.0, 4.0, 5.0],
    "RHO0_GRID": [0.6, 0.7, 0.8],
    "H0_DEFAULT": 3.0,
    "RHO0_DEFAULT": 0.7,

    # Global Metropolis
    "INITIAL_PROPOSAL_SIGMA": 0.38,
    "TARGET_ACCEPT": 0.50,
    "ADAPT_DURING_THERM": True,

    # Block Metropolis
    "BLOCK_PROPOSAL_SIGMA": 0.38,
    "ADAPT_BLOCK_THERM": True,

    # Randomness/output
    "SEED": 23060529,           # fresh seed for Stage B (Stage A used 23060524)
    "DEVICE": "cuda" if torch.cuda.is_available() else "cpu",
    "DTYPE": "float32",
    "CACHE_ROOT": "/content/PMBSF_SU2_LemmaQ_cache",
    "OUT_ROOT": "/content/PMBSF_SU2_LemmaQ_block_output",

    # Safety / debug
    "PRINT_EVERY_BLOCK": 4,     # was 8; fewer blocks total so print more often
}


ORIENTS: List[Tuple[int, int]] = [(0,1), (0,2), (0,3), (1,2), (1,3), (2,3)]
ORIENT_TO_INDEX = {o: i for i, o in enumerate(ORIENTS)}


# ======================================================================================
# GENERAL UTILS  (identical to Stage A)
# ======================================================================================

def log(msg: str) -> None:
    print(msg, flush=True)

def now_id() -> str:
    return time.strftime("%Y%m%d_%H%M%S")

def ensure_dir(path: Path) -> None:
    path.mkdir(parents=True, exist_ok=True)

def beta_str(beta: float) -> str:
    return f"{beta:g}".replace(".", "p")

def dtype() -> torch.dtype:
    return torch.float32 if CONFIG["DTYPE"] == "float32" else torch.float64

def set_seed(seed: int) -> None:
    random.seed(seed)
    np.random.seed(seed)
    torch.manual_seed(seed)
    if torch.cuda.is_available():
        torch.cuda.manual_seed_all(seed)


# ======================================================================================
# SU(2) QUATERNION OPS  (identical to Stage A)
# ======================================================================================

def qmul(x: torch.Tensor, y: torch.Tensor) -> torch.Tensor:
    a,b,c,d = x.unbind(-1)
    e,f,g,h = y.unbind(-1)
    return torch.stack((
        a*e - b*f - c*g - d*h,
        a*f + b*e + c*h - d*g,
        a*g - b*h + c*e + d*f,
        a*h + b*g - c*f + d*e,
    ), dim=-1)

def qconj(x: torch.Tensor) -> torch.Tensor:
    return torch.cat((x[..., :1], -x[..., 1:]), dim=-1)

def qnorm(x: torch.Tensor, eps: float = 1e-12) -> torch.Tensor:
    return x / torch.linalg.norm(x, dim=-1, keepdim=True).clamp_min(eps)

def random_su2(shape, device: str, dt: torch.dtype) -> torch.Tensor:
    return qnorm(torch.randn(*shape, 4, device=device, dtype=dt))

def random_near_identity(shape, sigma: float, device: str, dt: torch.dtype) -> torch.Tensor:
    axis = torch.randn(*shape, 3, device=device, dtype=dt)
    axis = axis / torch.linalg.norm(axis, dim=-1, keepdim=True).clamp_min(1e-12)
    angle = sigma * torch.randn(*shape, device=device, dtype=dt)
    return torch.cat((torch.cos(angle)[..., None], torch.sin(angle)[..., None] * axis), dim=-1)

def roll_lat(x: torch.Tensor, direction: int, shift: int) -> torch.Tensor:
    return torch.roll(x, shifts=shift, dims=direction)


# ======================================================================================
# FULL-LATTICE METROPOLIS  (identical to Stage A)
# ======================================================================================

def make_parity_masks(L: int, device: str):
    coords = torch.meshgrid(
        torch.arange(L, device=device),
        torch.arange(L, device=device),
        torch.arange(L, device=device),
        torch.arange(L, device=device),
        indexing="ij",
    )
    parity = (coords[0] + coords[1] + coords[2] + coords[3]) & 1
    return parity == 0, parity == 1

def initialize_field(L: int, mode: str, device: str, dt: torch.dtype) -> torch.Tensor:
    if mode == "cold":
        U = torch.zeros(4, L, L, L, L, 4, device=device, dtype=dt)
        U[..., 0] = 1.0
        return U
    if mode == "hot":
        return random_su2((4, L, L, L, L), device, dt)
    raise ValueError(f"Unknown START_MODE={mode}")

def compute_staple_full(U: torch.Tensor, mu: int) -> torch.Tensor:
    H = torch.zeros_like(U[mu])
    U_mu = U[mu]
    for nu in range(4):
        if nu == mu:
            continue
        U_nu = U[nu]

        U_nu_x_plus_mu = roll_lat(U_nu, mu, -1)
        U_mu_x_plus_nu = roll_lat(U_mu, nu, -1)
        forward = qmul(qmul(U_nu_x_plus_mu, qconj(U_mu_x_plus_nu)), qconj(U_nu))

        U_nu_x_minus_nu = roll_lat(U_nu, nu, +1)
        U_mu_x_minus_nu = roll_lat(U_mu, nu, +1)
        U_nu_x_plus_mu_minus_nu = roll_lat(U_nu_x_minus_nu, mu, -1)
        backward = qmul(qmul(qconj(U_nu_x_plus_mu_minus_nu), qconj(U_mu_x_minus_nu)), U_nu_x_minus_nu)

        H = H + forward + backward
    return H

@torch.no_grad()
def metropolis_sweep_full(U: torch.Tensor, beta: float, sigma: float, parity_masks) -> Tuple[torch.Tensor, float]:
    device = U.device.type
    dt = U.dtype
    acc_count = 0
    prop_count = 0
    for mu in range(4):
        for mask in parity_masks:
            H = compute_staple_full(U, mu)
            old = U[mu]
            old_score = qmul(old, H)[..., 0]
            R = random_near_identity(old.shape[:-1], sigma, device, dt)
            prop = qnorm(qmul(R, old))
            new_score = qmul(prop, H)[..., 0]
            log_alpha = beta * (new_score - old_score)
            log_u = torch.log(torch.rand_like(log_alpha).clamp_min(1e-30))
            accept = (log_u < log_alpha) & mask
            U[mu] = torch.where(accept[..., None], prop, old)
            acc_count += int(accept.sum().detach().cpu())
            prop_count += int(mask.sum().detach().cpu())
    return U, acc_count / max(prop_count, 1)

@torch.no_grad()
def run_full_sweeps(U, beta, n_sweeps, sigma, parity_masks, adapt=False, label=""):
    acc_hist = []
    for s in range(1, n_sweeps + 1):
        U, acc = metropolis_sweep_full(U, beta, sigma, parity_masks)
        acc_hist.append(acc)
        if adapt and s % 10 == 0:
            recent = float(np.mean(acc_hist[-10:]))
            if recent < CONFIG["TARGET_ACCEPT"] - 0.07:
                sigma *= 0.92
            elif recent > CONFIG["TARGET_ACCEPT"] + 0.07:
                sigma *= 1.08
            sigma = float(np.clip(sigma, 0.03, 1.50))
        if label and (s == 1 or s == n_sweeps or s % max(1, n_sweeps // 5) == 0):
            log(f"    [{label}] sweep={s:5d}/{n_sweeps:<5d} acc_recent={np.mean(acc_hist[-min(10,len(acc_hist)):]):.4f} sigma={sigma:.5f}")
    return U, sigma, acc_hist


# ======================================================================================
# LINK GATHER/SET AND LOCAL STAPLES FOR BLOCK UPDATES  (identical to Stage A)
# ======================================================================================

def shift_coords(coords: torch.Tensor, direction: int, shift: int, L: int) -> torch.Tensor:
    out = coords.clone()
    out[:, direction] = (out[:, direction] + int(shift)) % L
    return out

def gather_links(U: torch.Tensor, mu: int, coords: torch.Tensor) -> torch.Tensor:
    idx = tuple(coords[:, d].long() for d in range(4))
    return U[mu][idx]

def set_links_(U: torch.Tensor, mu: int, coords: torch.Tensor, vals: torch.Tensor) -> None:
    idx = tuple(coords[:, d].long() for d in range(4))
    U[mu][idx] = vals

def compute_staple_at_coords(U: torch.Tensor, mu: int, coords: torch.Tensor) -> torch.Tensor:
    L = U.shape[1]
    H = torch.zeros((coords.shape[0], 4), device=U.device, dtype=U.dtype)
    for nu in range(4):
        if nu == mu:
            continue
        coords_plus_mu = shift_coords(coords, mu, +1, L)
        coords_plus_nu = shift_coords(coords, nu, +1, L)
        coords_minus_nu = shift_coords(coords, nu, -1, L)
        coords_plus_mu_minus_nu = shift_coords(coords_minus_nu, mu, +1, L)
        U_nu_x_plus_mu = gather_links(U, nu, coords_plus_mu)
        U_mu_x_plus_nu = gather_links(U, mu, coords_plus_nu)
        U_nu_x = gather_links(U, nu, coords)
        forward = qmul(qmul(U_nu_x_plus_mu, qconj(U_mu_x_plus_nu)), qconj(U_nu_x))
        U_nu_x_minus_nu = gather_links(U, nu, coords_minus_nu)
        U_mu_x_minus_nu = gather_links(U, mu, coords_minus_nu)
        U_nu_x_plus_mu_minus_nu = gather_links(U, nu, coords_plus_mu_minus_nu)
        backward = qmul(qmul(qconj(U_nu_x_plus_mu_minus_nu), qconj(U_mu_x_minus_nu)), U_nu_x_minus_nu)
        H = H + forward + backward
    return H

@torch.no_grad()
def metropolis_sweep_block_local(U: torch.Tensor, beta: float, sigma: float, active_coords_by_mu_parity: Dict[Tuple[int,int], torch.Tensor]) -> Tuple[torch.Tensor, float]:
    device = U.device.type
    dt = U.dtype
    acc_count = 0
    prop_count = 0
    for mu in range(4):
        for parity in (0, 1):
            coords = active_coords_by_mu_parity.get((mu, parity))
            if coords is None or coords.numel() == 0:
                continue
            H = compute_staple_at_coords(U, mu, coords)
            old = gather_links(U, mu, coords)
            old_score = qmul(old, H)[..., 0]
            R = random_near_identity(old.shape[:-1], sigma, device, dt)
            prop = qnorm(qmul(R, old))
            new_score = qmul(prop, H)[..., 0]
            log_alpha = beta * (new_score - old_score)
            log_u = torch.log(torch.rand_like(log_alpha).clamp_min(1e-30))
            accept = log_u < log_alpha
            new_vals = torch.where(accept[..., None], prop, old)
            set_links_(U, mu, coords, new_vals)
            acc_count += int(accept.sum().detach().cpu())
            prop_count += int(coords.shape[0])
    return U, acc_count / max(prop_count, 1)

@torch.no_grad()
def run_block_sweeps(U, beta, n_sweeps, sigma, active_coords_by_mu_parity, adapt=False):
    acc_hist = []
    for s in range(1, n_sweeps + 1):
        U, acc = metropolis_sweep_block_local(U, beta, sigma, active_coords_by_mu_parity)
        acc_hist.append(acc)
        if adapt and s % 10 == 0:
            recent = float(np.mean(acc_hist[-10:]))
            if recent < CONFIG["TARGET_ACCEPT"] - 0.08:
                sigma *= 0.92
            elif recent > CONFIG["TARGET_ACCEPT"] + 0.08:
                sigma *= 1.08
            sigma = float(np.clip(sigma, 0.03, 1.50))
    return U, sigma, acc_hist


# ======================================================================================
# PLAQUETTES, FEATURES, THRESHOLD  (identical to Stage A)
# ======================================================================================

def plaquette_phi_at_coords(U: torch.Tensor, mu: int, nu: int, coords: torch.Tensor) -> torch.Tensor:
    L = U.shape[1]
    x = coords
    x_plus_mu = shift_coords(x, mu, +1, L)
    x_plus_nu = shift_coords(x, nu, +1, L)
    U_mu_x = gather_links(U, mu, x)
    U_nu_x_plus_mu = gather_links(U, nu, x_plus_mu)
    U_mu_x_plus_nu = gather_links(U, mu, x_plus_nu)
    U_nu_x = gather_links(U, nu, x)
    P = qmul(qmul(qmul(U_mu_x, U_nu_x_plus_mu), qconj(U_mu_x_plus_nu)), qconj(U_nu_x))
    return 1.0 - P[..., 0].clamp(-1.0, 1.0)

def forward_staple_component_at_coords(U: torch.Tensor, mu: int, nu: int, coords: torch.Tensor) -> torch.Tensor:
    L = U.shape[1]
    x_plus_mu = shift_coords(coords, mu, +1, L)
    x_plus_nu = shift_coords(coords, nu, +1, L)
    U_nu_x_plus_mu = gather_links(U, nu, x_plus_mu)
    U_mu_x_plus_nu = gather_links(U, mu, x_plus_nu)
    U_nu_x = gather_links(U, nu, coords)
    c0 = qmul(qmul(U_nu_x_plus_mu, qconj(U_mu_x_plus_nu)), qconj(U_nu_x))
    return qnorm(c0)

def smooth_indicator(phi: torch.Tensor, threshold: float, eta: float) -> torch.Tensor:
    z = (phi.float() - float(threshold)) / float(eta)
    return torch.sigmoid(torch.clamp(z, -80.0, 80.0))

def compute_phi_all_orientations(U: torch.Tensor) -> torch.Tensor:
    parts = []
    L = U.shape[1]
    coords = torch.stack(torch.meshgrid(
        torch.arange(L, device=U.device),
        torch.arange(L, device=U.device),
        torch.arange(L, device=U.device),
        torch.arange(L, device=U.device),
        indexing="ij"
    ), dim=-1).reshape(-1, 4)
    for mu,nu in ORIENTS:
        phi = plaquette_phi_at_coords(U, mu, nu, coords).reshape(L, L, L, L)
        parts.append(phi)
    return torch.stack(parts, dim=0)

def find_threshold_for_smooth(phi_values_np: np.ndarray, q_target: float, eta: float) -> Tuple[float, float, float]:
    lo = float(np.min(phi_values_np) - 10.0 * eta - 1e-6)
    hi = float(np.max(phi_values_np) + 10.0 * eta + 1e-6)
    vals = phi_values_np.astype(np.float64)
    for _ in range(80):
        mid = 0.5 * (lo + hi)
        q_mid = float(np.mean(1.0 / (1.0 + np.exp(-np.clip((vals - mid) / eta, -80.0, 80.0)))))
        if q_mid > q_target:
            lo = mid
        else:
            hi = mid
    t = 0.5 * (lo + hi)
    q_eta = float(np.mean(1.0 / (1.0 + np.exp(-np.clip((vals - t) / eta, -80.0, 80.0)))))
    q_hard = float(np.mean(vals >= t))
    return t, q_eta, q_hard

def cap_F(rho: torch.Tensor, a: float) -> torch.Tensor:
    a_clamped = max(-1.0, min(1.0, float(a)))
    rho_c = torch.clamp(rho, -1.0, 1.0)
    return rho_c * a_clamped + torch.sqrt(torch.clamp(1.0 - rho_c*rho_c, min=0.0)) * math.sqrt(max(0.0, 1.0 - a_clamped*a_clamped))


# ======================================================================================
# BLOCK GEOMETRY  (identical to Stage A; works for any BLOCK_SIDE / CORE_MARGIN)
# ======================================================================================

def make_range(anchor: int, side: int) -> List[int]:
    return list(range(anchor, anchor + side))

def make_block_spec(L: int, anchor: Tuple[int,int,int,int], block_side: int, core_margin: int, device: str) -> Dict[str, Any]:
    block_ranges = [make_range(anchor[d], block_side) for d in range(4)]
    core_lo = [anchor[d] + core_margin for d in range(4)]
    core_hi_excl = [anchor[d] + block_side - core_margin for d in range(4)]
    if any(core_hi_excl[d] <= core_lo[d] for d in range(4)):
        raise ValueError("CORE_MARGIN too large for BLOCK_SIDE")

    active_coords_by_mu_parity: Dict[Tuple[int,int], torch.Tensor] = {}
    for mu in range(4):
        coords_list = []
        for x0 in block_ranges[0]:
            for x1 in block_ranges[1]:
                for x2 in block_ranges[2]:
                    for x3 in block_ranges[3]:
                        x = [x0, x1, x2, x3]
                        if x[mu] + 1 <= anchor[mu] + block_side - 1:
                            coords_list.append(x)
        arr = np.array(coords_list, dtype=np.int64)
        if arr.size == 0:
            for parity in (0,1):
                active_coords_by_mu_parity[(mu, parity)] = torch.empty((0,4), device=device, dtype=torch.long)
            continue
        parity_arr = arr.sum(axis=1) & 1
        for parity in (0,1):
            sub = arr[parity_arr == parity]
            active_coords_by_mu_parity[(mu, parity)] = torch.as_tensor(sub, device=device, dtype=torch.long)

    core_entries = []
    core_by_ori: Dict[int, Dict[str, Any]] = {}
    eye = np.eye(4, dtype=np.int64)
    for oi, (mu,nu) in enumerate(ORIENTS):
        coords_list = []
        depths = []
        for x0 in range(core_lo[0], core_hi_excl[0]):
            for x1 in range(core_lo[1], core_hi_excl[1]):
                for x2 in range(core_lo[2], core_hi_excl[2]):
                    for x3 in range(core_lo[3], core_hi_excl[3]):
                        x = np.array([x0,x1,x2,x3], dtype=np.int64)
                        corners = [x, x + eye[mu], x + eye[nu], x + eye[mu] + eye[nu]]
                        ok = True
                        for c in corners:
                            for d in range(4):
                                if not (core_lo[d] <= c[d] < core_hi_excl[d]):
                                    ok = False
                                    break
                            if not ok:
                                break
                        if not ok:
                            continue

                        dep = 999
                        for c in corners:
                            for d in range(4):
                                dep = min(dep, int(c[d] - anchor[d]))
                                dep = min(dep, int(anchor[d] + block_side - 1 - c[d]))
                        coords_list.append(x.tolist())
                        depths.append(dep)
                        core_entries.append({
                            "ori_index": oi,
                            "mu": mu,
                            "nu": nu,
                            "coord": tuple(int(v) for v in x.tolist()),
                            "depth": int(dep),
                        })

        coords_tensor = torch.as_tensor(np.array(coords_list, dtype=np.int64), device=device, dtype=torch.long) if coords_list else torch.empty((0,4), device=device, dtype=torch.long)
        core_by_ori[oi] = {"mu": mu, "nu": nu, "coords": coords_tensor, "depths": depths}

    return {
        "anchor": tuple(int(x) for x in anchor),
        "block_side": block_side,
        "core_margin": core_margin,
        "active_coords_by_mu_parity": active_coords_by_mu_parity,
        "core_entries": core_entries,
        "core_by_ori": core_by_ori,
        "n_core_plaquettes": len(core_entries),
        "core_lo": tuple(core_lo),
        "core_hi_excl": tuple(core_hi_excl),
    }

def random_anchor(L: int, block_side: int, rng: np.random.Generator) -> Tuple[int,int,int,int]:
    max_anchor = L - block_side
    if max_anchor < 0:
        raise ValueError("BLOCK_SIDE > L")
    return tuple(int(x) for x in rng.integers(0, max_anchor + 1, size=4))


# ======================================================================================
# CORE MEASUREMENT  (identical to Stage A; vectorised over plaquettes already)
# ======================================================================================

@torch.no_grad()
def measure_core(U: torch.Tensor, block_spec: Dict[str, Any], beta: float, threshold: float, eta: float) -> Dict[str, np.ndarray]:
    n = block_spec["n_core_plaquettes"]
    X = np.zeros(n, dtype=np.float64)
    k_arr = np.zeros(n, dtype=np.float64)
    rho_arr = np.zeros(n, dtype=np.float64)
    g_arr = np.zeros(n, dtype=np.float64)
    phi_arr = np.zeros(n, dtype=np.float64)

    ptr_by_ori = {}
    for idx, ent in enumerate(block_spec["core_entries"]):
        ptr_by_ori.setdefault(ent["ori_index"], []).append(idx)

    a_t_eta = 1.0 - (float(threshold) - float(eta))

    for oi, group in block_spec["core_by_ori"].items():
        coords = group["coords"]
        if coords.numel() == 0:
            continue
        mu = group["mu"]
        nu = group["nu"]
        flat_indices = ptr_by_ori.get(oi, [])
        phi = plaquette_phi_at_coords(U, mu, nu, coords)
        x = smooth_indicator(phi, threshold, eta)
        H = compute_staple_at_coords(U, mu, coords)
        k = torch.linalg.norm(H, dim=-1)
        Hhat = H / k[..., None].clamp_min(1e-12)
        c0 = forward_staple_component_at_coords(U, mu, nu, coords)
        rho = (Hhat * c0).sum(dim=-1).clamp(-1.0, 1.0)
        F = cap_F(rho, a_t_eta)
        g = beta * k * torch.clamp(1.0 - F, min=0.0)
        idx_np = np.array(flat_indices, dtype=np.int64)
        X[idx_np] = x.detach().cpu().numpy()
        phi_arr[idx_np] = phi.detach().cpu().numpy()
        k_arr[idx_np] = k.detach().cpu().numpy()
        rho_arr[idx_np] = rho.detach().cpu().numpy()
        g_arr[idx_np] = g.detach().cpu().numpy()

    bad_default = ((k_arr < CONFIG["H0_DEFAULT"]) | (rho_arr < CONFIG["RHO0_DEFAULT"])).astype(np.float64)
    Y_default = X * bad_default

    return {
        "X": X,
        "Y_default": Y_default,
        "bad_default": bad_default,
        "phi": phi_arr,
        "k": k_arr,
        "rho": rho_arr,
        "g": g_arr,
    }


# ======================================================================================
# FULL CONFIG CACHE / GLOBAL THRESHOLD  (identical to Stage A)
# ======================================================================================

def full_config_cache_path(L: int, beta: float) -> Path:
    cache = Path(CONFIG["CACHE_ROOT"])
    ensure_dir(cache)
    stem = (
        f"fullU_L{L}_beta{beta_str(beta)}_N{CONFIG['N_CFG']}"
        f"_therm{CONFIG['THERM_SWEEPS']}_between{CONFIG['BETWEEN_SWEEPS']}"
        f"_seed{CONFIG['SEED']}.pt"
    )
    return cache / stem

@torch.no_grad()
def generate_or_load_full_configs(L: int, beta: float) -> Tuple[torch.Tensor, Dict[str, float]]:
    path = full_config_cache_path(L, beta)
    if CONFIG["REUSE_FULL_LINKS"] and path.exists():
        log(f"[cache] loading full links: {path}")
        U_all = torch.load(path, map_location="cpu")
        return U_all, {"acceptance_mean": np.nan, "acceptance_std": np.nan, "from_cache": True}

    device = CONFIG["DEVICE"]
    dt = dtype()
    parity_masks = make_parity_masks(L, device)
    sigma = float(CONFIG["INITIAL_PROPOSAL_SIGMA"])
    log(f"[init-global] {CONFIG['START_MODE']} L={L} beta={beta}")
    U = initialize_field(L, CONFIG["START_MODE"], device, dt)
    U, sigma, acc_therm = run_full_sweeps(
        U, beta, CONFIG["THERM_SWEEPS"], sigma, parity_masks,
        adapt=bool(CONFIG["ADAPT_DURING_THERM"]), label="therm")
    configs = []
    acc_all = []
    log(f"[collect-global] N_CFG={CONFIG['N_CFG']} BETWEEN={CONFIG['BETWEEN_SWEEPS']}")
    for i in range(1, CONFIG["N_CFG"] + 1):
        U, sigma, acc_hist = run_full_sweeps(U, beta, CONFIG["BETWEEN_SWEEPS"], sigma, parity_masks, adapt=False, label="")
        acc_all.extend(acc_hist)
        configs.append(U.detach().cpu().clone())
        if i == 1 or i == CONFIG["N_CFG"] or i % max(1, CONFIG["N_CFG"] // 8) == 0:
            log(f"    [global-cfg] {i:4d}/{CONFIG['N_CFG']} acc={np.mean(acc_hist):.4f} sigma={sigma:.5f}")
    U_all = torch.stack(configs, dim=0).contiguous()
    if CONFIG["SAVE_FULL_LINKS"]:
        torch.save(U_all, path)
        log(f"[saved] {path}")
    if device == "cuda":
        torch.cuda.empty_cache()
    return U_all, {
        "acceptance_mean": float(np.mean(acc_all)),
        "acceptance_std": float(np.std(acc_all)),
        "from_cache": False,
    }

@torch.no_grad()
def estimate_global_threshold(U_all_cpu: torch.Tensor, L: int, beta: float) -> Dict[str, float]:
    device = CONFIG["DEVICE"]
    phi_chunks = []
    log("[threshold] computing global plaquette phi values for all orientations")
    for i in range(U_all_cpu.shape[0]):
        U = U_all_cpu[i].to(device)
        phi_all = compute_phi_all_orientations(U).detach().cpu().reshape(-1).numpy()
        phi_chunks.append(phi_all)
        if device == "cuda":
            del U
            torch.cuda.empty_cache()
    vals = np.concatenate(phi_chunks, axis=0)
    t, q_eta, q_hard = find_threshold_for_smooth(vals, CONFIG["Q_TARGET"], CONFIG["ETA"])
    return {
        "threshold_t": float(t),
        "q_eta": float(q_eta),
        "q_hard_emp": float(q_hard),
        "phi_mean": float(np.mean(vals)),
        "phi_std": float(np.std(vals)),
        "phi_q99": float(np.quantile(vals, 0.99)),
        "phi_q999": float(np.quantile(vals, 0.999)),
    }


# ======================================================================================
# STATISTICS AGGREGATION  (identical to Stage A)
# ======================================================================================

def finalize_distance_ratios(block_dist_rows: List[Dict[str, Any]], q_eta: float):
    df = pd.DataFrame(block_dist_rows)
    if df.empty:
        return pd.DataFrame(), pd.DataFrame(), pd.DataFrame()
    out = []
    for d, sub in df.groupby("distance_l1"):
        pair_num = sub["pair_xx_sum"].sum()
        pair_count = sub["pair_count"].sum()
        lambda_num = sub["lambda_num"].sum()
        lambda_den = sub["lambda_den"].sum()
        root_num = sub["root_num"].sum()
        root_den = sub["root_den"].sum()
        pair_ratio = pair_num / max(q_eta*q_eta*pair_count, 1e-300)
        lambda_ratio = lambda_num / max(lambda_den, 1e-300)
        root_ratio = root_num / max(root_den, 1e-300)
        sub2 = sub.copy()
        sub2["pair_ratio_block"] = sub2["pair_xx_sum"] / np.maximum(q_eta*q_eta*sub2["pair_count"], 1e-300)
        sub2["lambda_ratio_block"] = sub2["lambda_num"] / np.maximum(sub2["lambda_den"], 1e-300)
        sub2["root_ratio_block"] = sub2["root_num"] / np.maximum(sub2["root_den"], 1e-300)
        def se(col):
            x = sub2[col].replace([np.inf, -np.inf], np.nan).dropna().to_numpy()
            if len(x) <= 1:
                return np.nan
            return float(np.std(x, ddof=1) / math.sqrt(len(x)))
        out.append({
            "distance_l1": int(d),
            "n_block_distance_rows": int(len(sub)),
            "pair_count": int(pair_count),
            "pair_ratio_R2": float(pair_ratio),
            "pair_ratio_R2_se_block": se("pair_ratio_block"),
            "cavity_Lambda": float(lambda_ratio),
            "cavity_Lambda_se_block": se("lambda_ratio_block"),
            "rooted_Lambda": float(root_ratio),
            "rooted_Lambda_se_block": se("root_ratio_block"),
            "lambda_den": float(lambda_den),
            "root_den": float(root_den),
        })
    agg = pd.DataFrame(out).sort_values("distance_l1")
    pair_df = agg[["distance_l1", "pair_count", "pair_ratio_R2", "pair_ratio_R2_se_block"]].copy()
    cavity_df = agg[["distance_l1", "pair_count", "cavity_Lambda", "cavity_Lambda_se_block", "lambda_den"]].copy()
    rooted_df = agg[["distance_l1", "pair_count", "rooted_Lambda", "rooted_Lambda_se_block", "root_den"]].copy()
    return pair_df, cavity_df, rooted_df

def regression_cap_feature(single_df: pd.DataFrame) -> pd.DataFrame:
    rows = []
    if single_df.empty:
        return pd.DataFrame()
    eps = 1e-300
    df = single_df[np.isfinite(single_df["g_mean"]) & (single_df["q_cond"] > 0)].copy()
    if len(df) >= 3:
        x = df["g_mean"].to_numpy(dtype=float)
        y = np.log(df["q_cond"].to_numpy(dtype=float) + eps)
        Xmat = np.vstack([np.ones_like(x), x]).T
        coef, _, _, _ = np.linalg.lstsq(Xmat, y, rcond=None)
        yhat = Xmat @ coef
        ss_res = float(np.sum((y-yhat)**2))
        ss_tot = float(np.sum((y-np.mean(y))**2))
        r2 = 1.0 - ss_res / max(ss_tot, 1e-300)
        rows.append({
            "predictor": "g_mean", "n": int(len(df)),
            "intercept": float(coef[0]), "slope": float(coef[1]), "r2": float(r2),
            "interpretation": "negative slope supports heat-bath cap predictor" if coef[1] < 0 else "nonnegative slope does not support cap predictor",
        })
    if len(df) >= 3:
        x = df["rho_mean"].to_numpy(dtype=float)
        y = np.log(df["q_cond"].to_numpy(dtype=float) + eps)
        Xmat = np.vstack([np.ones_like(x), x]).T
        coef, _, _, _ = np.linalg.lstsq(Xmat, y, rcond=None)
        yhat = Xmat @ coef
        ss_res = float(np.sum((y-yhat)**2))
        ss_tot = float(np.sum((y-np.mean(y))**2))
        r2 = 1.0 - ss_res / max(ss_tot, 1e-300)
        rows.append({
            "predictor": "rho_mean", "n": int(len(df)),
            "intercept": float(coef[0]), "slope": float(coef[1]), "r2": float(r2),
            "interpretation": "negative slope means higher alignment lowers source rate" if coef[1] < 0 else "unexpected sign or weak relation",
        })
    return pd.DataFrame(rows)

def summarize_single_source(single_df: pd.DataFrame) -> pd.DataFrame:
    if single_df.empty:
        return pd.DataFrame()
    rows = []
    for depth, sub in single_df.groupby("depth"):
        x = sub["ratio_qcond_over_q"].to_numpy(dtype=float)
        rows.append({
            "depth": int(depth), "n": int(len(x)),
            "mean_ratio": float(np.mean(x)), "median_ratio": float(np.median(x)),
            "q90_ratio": float(np.quantile(x, 0.90)), "q95_ratio": float(np.quantile(x, 0.95)),
            "max_ratio": float(np.max(x)),
            "se_mean_naive": float(np.std(x, ddof=1) / math.sqrt(len(x))) if len(x) > 1 else np.nan,
        })
    return pd.DataFrame(rows).sort_values("depth")


# ======================================================================================
# BLOCK-CONDITIONAL RUN  (Stage B: vectorised pair-distance accumulation)
# ======================================================================================

@torch.no_grad()
def run_block_conditional_for_combo(U_all_cpu: torch.Tensor, L: int, beta: float, threshold_info: Dict[str, float], outdir: Path):
    device = CONFIG["DEVICE"]
    q_eta = float(threshold_info["q_eta"])
    threshold = float(threshold_info["threshold_t"])

    rng = np.random.default_rng(CONFIG["SEED"] + int(1000*beta) + L)

    single_rows = []
    block_summary_rows = []
    block_dist_rows = []

    n_cfg = U_all_cpu.shape[0]
    total_blocks = n_cfg * CONFIG["N_BLOCKS_PER_CFG"]
    block_counter = 0

    for cfg_idx in range(n_cfg):
        U_base_cpu = U_all_cpu[cfg_idx]

        for bidx in range(CONFIG["N_BLOCKS_PER_CFG"]):
            block_counter += 1
            anchor = random_anchor(L, CONFIG["BLOCK_SIDE"], rng)
            block_spec = make_block_spec(
                L=L, anchor=anchor,
                block_side=CONFIG["BLOCK_SIDE"], core_margin=CONFIG["CORE_MARGIN"],
                device=device)
            ncore = block_spec["n_core_plaquettes"]
            if ncore == 0:
                continue

            U = U_base_cpu.to(device).clone()
            sigma = float(CONFIG["BLOCK_PROPOSAL_SIGMA"])

            U, sigma, acc_therm = run_block_sweeps(
                U, beta, CONFIG["BLOCK_THERM"], sigma,
                block_spec["active_coords_by_mu_parity"],
                adapt=bool(CONFIG["ADAPT_BLOCK_THERM"]))

            sum_X = np.zeros(ncore, dtype=np.float64)
            sum_Y = np.zeros(ncore, dtype=np.float64)
            sum_bad = np.zeros(ncore, dtype=np.float64)
            sum_phi = np.zeros(ncore, dtype=np.float64)
            sum_k = np.zeros(ncore, dtype=np.float64)
            sum_rho = np.zeros(ncore, dtype=np.float64)
            sum_g = np.zeros(ncore, dtype=np.float64)
            sum_XX = np.zeros((ncore, ncore), dtype=np.float64)
            sum_YX = np.zeros((ncore, ncore), dtype=np.float64)

            acc_sample_all = []

            for s in range(CONFIG["BLOCK_SAMPLES"]):
                U, sigma, acc_between = run_block_sweeps(
                    U, beta, CONFIG["BLOCK_BETWEEN"], sigma,
                    block_spec["active_coords_by_mu_parity"], adapt=False)
                acc_sample_all.extend(acc_between)
                meas = measure_core(U, block_spec, beta, threshold, CONFIG["ETA"])
                X = meas["X"]; Y = meas["Y_default"]
                sum_X += X
                sum_Y += Y
                sum_bad += meas["bad_default"]
                sum_phi += meas["phi"]
                sum_k += meas["k"]
                sum_rho += meas["rho"]
                sum_g += meas["g"]
                sum_XX += np.outer(X, X)
                sum_YX += np.outer(Y, X)

            denom = float(CONFIG["BLOCK_SAMPLES"])
            bar_X = sum_X / denom
            bar_Y = sum_Y / denom
            bar_bad = sum_bad / denom
            bar_phi = sum_phi / denom
            bar_k = sum_k / denom
            bar_rho = sum_rho / denom
            bar_g = sum_g / denom
            mean_XX = sum_XX / denom
            mean_YX = sum_YX / denom

            # per-row single-source rows
            for i, ent in enumerate(block_spec["core_entries"]):
                single_rows.append({
                    "L": L, "beta": beta,
                    "cfg_idx": cfg_idx, "block_idx": block_counter,
                    "anchor": str(anchor),
                    "plaquette_local_idx": i,
                    "ori_index": ent["ori_index"], "mu": ent["mu"], "nu": ent["nu"],
                    "coord": str(ent["coord"]), "depth": ent["depth"],
                    "threshold_t": threshold, "q_eta": q_eta,
                    "q_cond": float(bar_X[i]),
                    "ratio_qcond_over_q": float(bar_X[i] / max(q_eta, 1e-300)),
                    "root_bad_cond": float(bar_Y[i]),
                    "root_bad_ratio_over_q": float(bar_Y[i] / max(q_eta, 1e-300)),
                    "bad_prob_cond": float(bar_bad[i]),
                    "phi_mean": float(bar_phi[i]),
                    "k_mean": float(bar_k[i]),
                    "rho_mean": float(bar_rho[i]),
                    "g_mean": float(bar_g[i]),
                })

            # =============================================================
            # VECTORISED PAIR-DISTANCE ACCUMULATION  (Stage B change)
            # =============================================================
            # Build full L1 pairwise distance matrix in one shot, then group by
            # distance.  At ncore=864 this is O(ncore^2) memory (6 MB) and
            # O(ncore^2) work in numpy (vs O(ncore^2) Python loop at 1300x cost).
            coords_arr = np.array([ent["coord"] for ent in block_spec["core_entries"]],
                                  dtype=np.int64)  # (ncore, 4)
            diff = (coords_arr[:, None, :] - coords_arr[None, :, :]) % L  # (ncore, ncore, 4)
            diff_min = np.minimum(diff, L - diff)
            D = diff_min.sum(axis=-1)  # (ncore, ncore) periodic L1 distances

            diag_mask = np.eye(ncore, dtype=bool)
            # bar_X broadcast across columns: entry (i,j) carries bar_X[i]
            bar_X_col = np.broadcast_to(bar_X[:, None], (ncore, ncore))
            bar_Y_col = np.broadcast_to(bar_Y[:, None], (ncore, ncore))

            unique_d = np.unique(D[~diag_mask])
            for d_val in unique_d:
                mask = (D == d_val) & (~diag_mask)
                if not mask.any():
                    continue
                pair_xx_sum = float(mean_XX[mask].sum())
                pair_count = float(mask.sum())
                lambda_den = float(q_eta * bar_X_col[mask].sum())
                root_num = float(mean_YX[mask].sum())
                root_den = float(q_eta * bar_Y_col[mask].sum())
                block_dist_rows.append({
                    "L": L, "beta": beta,
                    "cfg_idx": cfg_idx, "block_idx": block_counter,
                    "anchor": str(anchor),
                    "distance_l1": int(d_val),
                    "pair_xx_sum": pair_xx_sum,
                    "pair_count": pair_count,
                    "lambda_num": pair_xx_sum,   # same as pair_xx_sum by construction
                    "lambda_den": lambda_den,
                    "root_num": root_num,
                    "root_den": root_den,
                })

            block_summary_rows.append({
                "L": L, "beta": beta,
                "cfg_idx": cfg_idx, "block_idx": block_counter,
                "anchor": str(anchor),
                "n_core_plaquettes": int(ncore),
                "block_accept_therm_mean": float(np.mean(acc_therm)),
                "block_accept_sample_mean": float(np.mean(acc_sample_all)),
                "block_accept_sample_std": float(np.std(acc_sample_all)),
                "q_cond_mean_over_core": float(np.mean(bar_X)),
                "q_cond_median_over_core": float(np.median(bar_X)),
                "ratio_qcond_mean_over_q": float(np.mean(bar_X) / max(q_eta, 1e-300)),
                "ratio_qcond_median_over_q": float(np.median(bar_X) / max(q_eta, 1e-300)),
                "bad_prob_mean_over_core": float(np.mean(bar_bad)),
                "root_bad_mean_over_core": float(np.mean(bar_Y)),
            })

            if block_counter == 1 or block_counter == total_blocks or block_counter % max(1, CONFIG["PRINT_EVERY_BLOCK"]) == 0:
                log(
                    f"    [block] {block_counter:4d}/{total_blocks} cfg={cfg_idx} anchor={anchor} "
                    f"ncore={ncore} qcond/q={np.mean(bar_X)/max(q_eta,1e-300):.3f} "
                    f"acc={np.mean(acc_sample_all):.4f}"
                )

            if device == "cuda":
                del U
                torch.cuda.empty_cache()

    single_df = pd.DataFrame(single_rows)
    block_summary_df = pd.DataFrame(block_summary_rows)
    pair_df, cavity_df, rooted_df = finalize_distance_ratios(block_dist_rows, q_eta)
    cap_reg_df = regression_cap_feature(single_df)
    single_summary_df = summarize_single_source(single_df)

    return {
        "single_source_depth": single_df,
        "single_source_depth_summary": single_summary_df,
        "boundary_block_summary": block_summary_df,
        "pair_ratio_by_distance": pair_df,
        "cavity_ratio_by_distance": cavity_df,
        "rooted_cavity_ratio_by_distance": rooted_df,
        "cap_feature_scan": single_df.copy(),
        "cap_feature_regression": cap_reg_df,
    }


# ======================================================================================
# MAIN  (identical to Stage A)
# ======================================================================================

def run():
    set_seed(CONFIG["SEED"])
    run_id = f"{CONFIG['RUN_NAME']}_{now_id()}"
    outdir = Path(CONFIG["OUT_ROOT"]) / run_id
    ensure_dir(outdir)

    log("="*100)
    log(f"[run] {run_id}")
    log(f"[device] {CONFIG['DEVICE']}")
    if CONFIG["DEVICE"] == "cuda":
        log(f"[gpu] {torch.cuda.get_device_name(0)}")
    log(f"[outdir] {outdir}")
    log(f"[geometry] BLOCK_SIDE={CONFIG['BLOCK_SIDE']}, CORE_MARGIN={CONFIG['CORE_MARGIN']}, "
        f"N_BLOCKS_PER_CFG={CONFIG['N_BLOCKS_PER_CFG']}")
    log("="*100)

    all_full_summary = []
    all_outputs = {
        "single_source_depth": [],
        "single_source_depth_summary": [],
        "boundary_block_summary": [],
        "pair_ratio_by_distance": [],
        "cavity_ratio_by_distance": [],
        "rooted_cavity_ratio_by_distance": [],
        "cap_feature_scan": [],
        "cap_feature_regression": [],
    }

    start = time.time()

    for L in CONFIG["L_LIST"]:
        for beta in CONFIG["BETA_LIST"]:
            combo_start = time.time()
            log("="*100)
            log(f"[combo] L={L} beta={beta}")
            log("="*100)

            U_all_cpu, gen_info = generate_or_load_full_configs(L, beta)
            threshold_info = estimate_global_threshold(U_all_cpu, L, beta)

            log("[threshold summary]")
            for k, v in threshold_info.items():
                log(f"  {k}: {v}")

            outputs = run_block_conditional_for_combo(U_all_cpu, L, beta, threshold_info, outdir)

            for key, df in outputs.items():
                if not df.empty:
                    all_outputs[key].append(df)

            full_summary = {
                "L": L, "beta": beta,
                **gen_info, **threshold_info,
                "combo_elapsed_min": (time.time() - combo_start) / 60.0,
            }

            ss = outputs["single_source_depth_summary"]
            if not ss.empty:
                full_summary["max_depth_median_ratio"] = float(ss["median_ratio"].max())
                full_summary["max_depth_q95_ratio"] = float(ss["q95_ratio"].max())
                full_summary["max_depth_max_ratio"] = float(ss["max_ratio"].max())
                full_summary["depth_bins_present"] = sorted(ss["depth"].unique().tolist())

            cav = outputs["cavity_ratio_by_distance"]
            if not cav.empty:
                full_summary["max_cavity_Lambda"] = float(cav["cavity_Lambda"].replace([np.inf, -np.inf], np.nan).max())
                full_summary["median_cavity_Lambda"] = float(cav["cavity_Lambda"].replace([np.inf, -np.inf], np.nan).median())
                full_summary["max_distance_bin"] = int(cav["distance_l1"].max())

            root = outputs["rooted_cavity_ratio_by_distance"]
            if not root.empty:
                full_summary["max_rooted_Lambda"] = float(root["rooted_Lambda"].replace([np.inf, -np.inf], np.nan).max())
                full_summary["median_rooted_Lambda"] = float(root["rooted_Lambda"].replace([np.inf, -np.inf], np.nan).median())

            reg = outputs["cap_feature_regression"]
            if not reg.empty:
                grow = reg[reg["predictor"] == "g_mean"]
                if len(grow):
                    full_summary["cap_g_slope"] = float(grow.iloc[0]["slope"])
                    full_summary["cap_g_r2"] = float(grow.iloc[0]["r2"])
                rrow = reg[reg["predictor"] == "rho_mean"]
                if len(rrow):
                    full_summary["cap_rho_slope"] = float(rrow.iloc[0]["slope"])
                    full_summary["cap_rho_r2"] = float(rrow.iloc[0]["r2"])

            all_full_summary.append(full_summary)

            log("[combo summary]")
            for k, v in full_summary.items():
                if isinstance(v, float):
                    log(f"  {k}: {v:.8g}")
                else:
                    log(f"  {k}: {v}")

    elapsed = time.time() - start

    full_summary_df = pd.DataFrame(all_full_summary)
    full_summary_path = outdir / "full_config_summary.csv"
    full_summary_df.to_csv(full_summary_path, index=False)

    written_paths = {"full_config_summary": full_summary_path}
    merged_outputs = {}
    for key, dfs in all_outputs.items():
        merged = pd.concat(dfs, ignore_index=True) if dfs else pd.DataFrame()
        merged_outputs[key] = merged
        path = outdir / f"{key}.csv"
        merged.to_csv(path, index=False)
        written_paths[key] = path

    readout = []
    readout.append("# PMBSF SU(2) Lemma Q Block-Conditional Diagnostic — Stage B Readout")
    readout.append("")
    readout.append("## Status")
    readout.append("")
    readout.append("Block-geometry follow-up to Stage A: `BLOCK_SIDE=10`, `CORE_MARGIN=3`, "
                   "`N_BLOCKS_PER_CFG=2`, `BLOCK_THERM=256`. ~864 core plaquettes per block "
                   "(vs 24 in Stage A). Distance fits now extend to d ~ 8 (vs Stage A's 4).")
    readout.append("")
    readout.append("This is still NOT a proof of Lemma Q.")
    readout.append("")
    readout.append("## Config")
    readout.append("")
    readout.append("```json")
    readout.append(json.dumps(CONFIG, indent=2, sort_keys=True))
    readout.append("```")
    readout.append("")
    readout.append(f"Elapsed minutes: `{elapsed/60:.3f}`")
    readout.append("")
    readout.append("## Full/global summary")
    readout.append("")
    readout.append(full_summary_df.to_markdown(index=False))
    readout.append("")

    ss_sum = merged_outputs["single_source_depth_summary"]
    if not ss_sum.empty:
        readout.append("## Table A. Single-source conditional control (depth-resolved)")
        readout.append("")
        readout.append(ss_sum.to_markdown(index=False))
        readout.append("")
        readout.append("Stage A had a single depth bin (depth=2) by geometric construction. "
                       "Stage B should show depth-resolved variation here.")
        readout.append("")

    cav = merged_outputs["cavity_ratio_by_distance"]
    root = merged_outputs["rooted_cavity_ratio_by_distance"]
    pair = merged_outputs["pair_ratio_by_distance"]
    if not cav.empty or not root.empty or not pair.empty:
        readout.append("## Table B. Cavity / rooted cavity / pair ratios by distance")
        readout.append("")
        readout.append("Stage A had only d in {0,1,2,3,4} with d=4 being unreliably sparse "
                       "(6 pairs per block). Stage B should support fits over d in {1..6+}.")
        readout.append("")
        if not pair.empty:
            readout.append("### Pair ratio R_2(d)")
            readout.append(pair.to_markdown(index=False))
            readout.append("")
        if not cav.empty:
            readout.append("### Cavity ratio Lambda(d)")
            readout.append(cav.to_markdown(index=False))
            readout.append("")
        if not root.empty:
            readout.append("### Rooted cavity ratio Lambda_root(d)")
            readout.append(root.to_markdown(index=False))
            readout.append("")

    reg = merged_outputs["cap_feature_regression"]
    if not reg.empty:
        readout.append("## Table C. Feature discrimination (univariate)")
        readout.append("")
        readout.append(reg.to_markdown(index=False))
        readout.append("")
        readout.append("Note: pass-17 follow-up showed Stage A's univariate R^2 ~ 0.03 and "
                       "the multivariate ceiling at R^2 ~ 0.04 on positive rows. The "
                       "Stage B per-row CSV `cap_feature_scan.csv` supports the same "
                       "multivariate analysis -- see `extended_regression.py` from pass 17.")
        readout.append("")

    readout.append("## Interpretation thresholds (same as Stage A)")
    readout.append("")
    readout.append("- Single-source: median `q_cond/q_eta` less than about 1.5, q95 less than about 3.")
    readout.append("- Cavity: `cavity_Lambda(d)` remains O(1) and ideally approaches 1 with distance.")
    readout.append("- Rooted: `rooted_Lambda(d)` remains O(1); direct test of rooted bad-staple absorption.")
    readout.append("- Cap mechanism: regression slope of `log(q_cond)` versus `g_mean` is negative.")
    readout.append("- New in Stage B: depth-resolved median ratio should be flat or decrease with depth; "
                   "pair/rooted decay rates should now have CI width comparable to the point estimate.")
    readout.append("")

    readout_path = outdir / "RUN_READOUT.md"
    readout_path.write_text("\n".join(readout), encoding="utf-8")
    written_paths["RUN_READOUT"] = readout_path

    log("="*100)
    log(f"[done] elapsed={elapsed/60:.2f} min")
    for key, path in written_paths.items():
        log(f"[saved] {key}: {path}")
    log("="*100)
    log("[final summary]")
    log(full_summary_df.to_string(index=False))

    return merged_outputs, full_summary_df


if __name__ == "__main__":
    run()
