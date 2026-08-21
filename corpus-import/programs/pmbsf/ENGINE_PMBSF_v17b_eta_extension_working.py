#!/usr/bin/env python3
"""
PMBSF v17b ETA EXTENSION — WORKING RUN SCRIPT

This is a real run script, not a scaffold.

It:
  1. Thermalizes SU(2) Wilson fields with quaternion Metropolis if no cache exists.
  2. Saves/reuses plaquette-score tensors phi_p = 1 - 1/2 ReTr(U_p).
  3. Sets the hard threshold t_q from the empirical q_target upper tail.
  4. Computes X_{p,eta} = sigmoid((phi_p - t_q)/eta).
  5. Measures connected cumulants for local support patterns.
  6. Performs block jackknife over configurations.
  7. Prints the readout and saves CSV/MD outputs.

Designed for Colab A100. Defaults are production-ish but editable at top.

Outputs:
  /content/PMBSF_v17b_eta_extension_output/<RUN_ID>/
    - cumulants_eta_extension.csv
    - eta_bridge_summary.csv
    - RUN_READOUT.md
    - cache/*.pt
"""

import os
import math
import time
import json
import random
from pathlib import Path
from typing import Dict, List, Tuple, Sequence, Optional

import numpy as np
import pandas as pd
import torch


# ======================================================================================
# USER CONFIG
# ======================================================================================

CONFIG = {
    "RUN_TAG": "PMBSF_v17b_eta_extension_REAL",

    # Full requested extension:
    "L_list": [12, 16, 24],
    "beta_list": [3.5, 4.0],
    "eta_list": [0.01, 0.005],
    "q_target": 0.003,

    # Metropolis sampling. Increase N_CFG for production if jackknife is noisy.
    # For a fast pilot, use L_list=[12], beta_list=[3.5], N_CFG=16, THERM_SWEEPS=80.
    "N_CFG": 64,
    "THERM_SWEEPS": 400,
    "BETWEEN_SWEEPS": 40,
    "START_MODE": "hot",          # "hot" or "cold"
    "INITIAL_PROPOSAL_SIGMA": 0.38,
    "ADAPT_DURING_THERM": True,
    "TARGET_ACCEPT": 0.50,

    # Measurement.
    "JACKKNIFE_BLOCKS": 32,
    "PATTERNS": ["pair_incident", "triple_star", "triple_L", "quad_local_mixed"],

    # Threshold quantile. Exact quantile over all plaquettes can be memory-heavy for L=24.
    "EXACT_QUANTILE": False,
    "MAX_QUANTILE_SAMPLES": 5_000_000,

    # Optional: sample anchor sites for cumulants. 0 means all L^4 sites.
    # Use e.g. 200_000 for a faster L=24 pass.
    "MAX_ANCHOR_SITES": 0,

    # Cache/reuse.
    "OUT_ROOT": "/content/PMBSF_v17b_eta_extension_output",
    "REUSE_PHI_CACHE": True,
    "REUSE_LAST_FIELD_CACHE": True,
    "SAVE_LAST_FIELD": True,

    # Optional locked old baseline CSV containing eta=0.025 rows with columns:
    # L,beta,eta,pattern,rooted_norm_qeta or enough columns to compute it.
    "BASELINE_CSV": "",

    "SEED": 23060524,
    "DEVICE": "cuda" if torch.cuda.is_available() else "cpu",
    "DTYPE": "float32",
}


# ======================================================================================
# BASIC UTILITIES
# ======================================================================================

ORIENTS: List[Tuple[int, int]] = [(0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3)]
ORIENT_TO_INDEX: Dict[Tuple[int, int], int] = {o: i for i, o in enumerate(ORIENTS)}


def now_id() -> str:
    return time.strftime("%Y%m%d_%H%M%S")


def beta_str(beta: float) -> str:
    return f"{beta:g}".replace(".", "p")


def log(s: str) -> None:
    print(s, flush=True)


def set_seeds(seed: int) -> None:
    random.seed(seed)
    np.random.seed(seed)
    torch.manual_seed(seed)
    if torch.cuda.is_available():
        torch.cuda.manual_seed_all(seed)


def get_dtype() -> torch.dtype:
    return torch.float32 if CONFIG["DTYPE"] == "float32" else torch.float64


def ensure_dir(p: Path) -> None:
    p.mkdir(parents=True, exist_ok=True)


# ======================================================================================
# SU(2) QUATERNION OPS
# Quaternion order: (a,b,c,d), corresponding to a I + i b sigma_1 + i c sigma_2 + i d sigma_3.
# ReTr(q) = 2a.
# ======================================================================================

def qmul(x: torch.Tensor, y: torch.Tensor) -> torch.Tensor:
    a, b, c, d = x.unbind(-1)
    e, f, g, h = y.unbind(-1)
    return torch.stack((
        a*e - b*f - c*g - d*h,
        a*f + b*e + c*h - d*g,
        a*g - b*h + c*e + d*f,
        a*h + b*g - c*f + d*e,
    ), dim=-1)


def qconj(x: torch.Tensor) -> torch.Tensor:
    return torch.cat((x[..., :1], -x[..., 1:]), dim=-1)


def qnormalize(x: torch.Tensor, eps: float = 1e-12) -> torch.Tensor:
    return x / torch.linalg.norm(x, dim=-1, keepdim=True).clamp_min(eps)


def random_su2(shape: Sequence[int], device: str, dtype: torch.dtype) -> torch.Tensor:
    x = torch.randn(*shape, 4, device=device, dtype=dtype)
    return qnormalize(x)


def random_near_identity(shape: Sequence[int], sigma: float, device: str, dtype: torch.dtype) -> torch.Tensor:
    axis = torch.randn(*shape, 3, device=device, dtype=dtype)
    axis = axis / torch.linalg.norm(axis, dim=-1, keepdim=True).clamp_min(1e-12)
    angle = sigma * torch.randn(*shape, device=device, dtype=dtype)
    c = torch.cos(angle)
    s = torch.sin(angle)
    return torch.cat((c[..., None], s[..., None] * axis), dim=-1)


def roll_lattice(x: torch.Tensor, direction: int, shift: int) -> torch.Tensor:
    # x shape [L,L,L,L,...]. direction in 0..3.
    return torch.roll(x, shifts=shift, dims=direction)


def make_parity_masks(L: int, device: str) -> Tuple[torch.Tensor, torch.Tensor]:
    coords = torch.meshgrid(
        torch.arange(L, device=device),
        torch.arange(L, device=device),
        torch.arange(L, device=device),
        torch.arange(L, device=device),
        indexing="ij",
    )
    parity = (coords[0] + coords[1] + coords[2] + coords[3]) & 1
    return (parity == 0), (parity == 1)


# ======================================================================================
# WILSON ACTION LOCAL STAPLES AND METROPOLIS
# ======================================================================================

def initialize_field(L: int, mode: str, device: str, dtype: torch.dtype) -> torch.Tensor:
    if mode == "cold":
        U = torch.zeros(4, L, L, L, L, 4, device=device, dtype=dtype)
        U[..., 0] = 1.0
        return U
    if mode == "hot":
        return random_su2((4, L, L, L, L), device, dtype)
    raise ValueError(f"Unknown START_MODE={mode}")


def compute_staple(U: torch.Tensor, mu: int) -> torch.Tensor:
    # U shape [4,L,L,L,L,4]. Returns staple for U_mu(x), shape [L,L,L,L,4].
    staple = torch.zeros_like(U[mu])
    U_mu = U[mu]

    for nu in range(4):
        if nu == mu:
            continue

        U_nu = U[nu]

        # Forward plaquette contribution:
        # U_nu(x+mu) U_mu^dagger(x+nu) U_nu^dagger(x)
        U_nu_x_plus_mu = roll_lattice(U_nu, mu, -1)
        U_mu_x_plus_nu = roll_lattice(U_mu, nu, -1)
        forward = qmul(qmul(U_nu_x_plus_mu, qconj(U_mu_x_plus_nu)), qconj(U_nu))

        # Backward plaquette contribution:
        # U_nu^dagger(x+mu-nu) U_mu^dagger(x-nu) U_nu(x-nu)
        U_nu_x_minus_nu = roll_lattice(U_nu, nu, +1)
        U_mu_x_minus_nu = roll_lattice(U_mu, nu, +1)
        U_nu_x_plus_mu_minus_nu = roll_lattice(U_nu_x_minus_nu, mu, -1)
        backward = qmul(qmul(qconj(U_nu_x_plus_mu_minus_nu), qconj(U_mu_x_minus_nu)), U_nu_x_minus_nu)

        staple = staple + forward + backward

    return staple


@torch.no_grad()
def metropolis_sweep(U: torch.Tensor, beta: float, sigma: float, parity_masks: Tuple[torch.Tensor, torch.Tensor]) -> Tuple[torch.Tensor, float]:
    device = U.device.type
    dtype = U.dtype
    acc_count = 0
    prop_count = 0

    for mu in range(4):
        for parity_mask in parity_masks:
            staple = compute_staple(U, mu)
            old_link = U[mu]
            old_score = qmul(old_link, staple)[..., 0]  # scalar part; log weight beta*score

            R = random_near_identity(old_link.shape[:-1], sigma, device, dtype)
            proposal = qnormalize(qmul(R, old_link))
            new_score = qmul(proposal, staple)[..., 0]

            log_alpha = beta * (new_score - old_score)
            log_u = torch.log(torch.rand_like(log_alpha).clamp_min(1e-30))
            accept = (log_u < log_alpha) & parity_mask

            U[mu] = torch.where(accept[..., None], proposal, old_link)

            acc_count += int(accept.sum().detach().cpu())
            prop_count += int(parity_mask.sum().detach().cpu())

    return U, acc_count / max(prop_count, 1)


@torch.no_grad()
def run_sweeps(U: torch.Tensor, beta: float, n_sweeps: int, sigma: float, parity_masks: Tuple[torch.Tensor, torch.Tensor],
               adapt: bool = False, label: str = "") -> Tuple[torch.Tensor, float, List[float]]:
    acc_hist = []
    for s in range(1, n_sweeps + 1):
        U, acc = metropolis_sweep(U, beta, sigma, parity_masks)
        acc_hist.append(acc)

        if adapt and s % 10 == 0:
            recent = float(np.mean(acc_hist[-10:]))
            # Conservative multiplicative adaptation.
            if recent < CONFIG["TARGET_ACCEPT"] - 0.07:
                sigma *= 0.92
            elif recent > CONFIG["TARGET_ACCEPT"] + 0.07:
                sigma *= 1.08
            sigma = float(np.clip(sigma, 0.03, 1.50))

        if label and (s == 1 or s == n_sweeps or s % max(1, n_sweeps // 5) == 0):
            recent = float(np.mean(acc_hist[-min(len(acc_hist), 10):]))
            log(f"    [{label}] sweep={s:5d}/{n_sweeps:<5d} acc_recent={recent:.4f} sigma={sigma:.5f}")

    return U, sigma, acc_hist


# ======================================================================================
# PLAQUETTE SCORES
# ======================================================================================

@torch.no_grad()
def plaquette_scores_phi(U: torch.Tensor) -> torch.Tensor:
    # Returns phi shape [6,L,L,L,L].
    phis = []
    for mu, nu in ORIENTS:
        U_mu = U[mu]
        U_nu = U[nu]
        U_nu_x_plus_mu = roll_lattice(U_nu, mu, -1)
        U_mu_x_plus_nu = roll_lattice(U_mu, nu, -1)

        P = qmul(qmul(qmul(U_mu, U_nu_x_plus_mu), qconj(U_mu_x_plus_nu)), qconj(U_nu))
        scalar = P[..., 0].clamp(-1.0, 1.0)
        phi = 1.0 - scalar
        phis.append(phi)

    return torch.stack(phis, dim=0).contiguous()


def cache_paths(run_dir: Path, L: int, beta: float) -> Tuple[Path, Path]:
    cache = run_dir / "cache"
    ensure_dir(cache)
    b = beta_str(beta)
    phi_name = (
        f"phi_L{L}_beta{b}_N{CONFIG['N_CFG']}_therm{CONFIG['THERM_SWEEPS']}"
        f"_between{CONFIG['BETWEEN_SWEEPS']}_seed{CONFIG['SEED']}.pt"
    )
    U_name = f"Ulast_L{L}_beta{b}_seed{CONFIG['SEED']}.pt"
    return cache / phi_name, cache / U_name


@torch.no_grad()
def generate_or_load_phi(L: int, beta: float, run_dir: Path) -> torch.Tensor:
    device = CONFIG["DEVICE"]
    dtype = get_dtype()
    phi_path, U_path = cache_paths(run_dir, L, beta)

    if CONFIG["REUSE_PHI_CACHE"] and phi_path.exists():
        log(f"[cache] loading phi: {phi_path}")
        return torch.load(phi_path, map_location=device).to(device)

    parity_masks = make_parity_masks(L, device)
    sigma = float(CONFIG["INITIAL_PROPOSAL_SIGMA"])

    if CONFIG["REUSE_LAST_FIELD_CACHE"] and U_path.exists():
        log(f"[cache] loading last field: {U_path}")
        U = torch.load(U_path, map_location=device).to(device)
        thermal_sweeps = 0
    else:
        log(f"[init] {CONFIG['START_MODE']} field L={L} beta={beta}")
        U = initialize_field(L, CONFIG["START_MODE"], device, dtype)
        thermal_sweeps = int(CONFIG["THERM_SWEEPS"])

    if thermal_sweeps > 0:
        U, sigma, _ = run_sweeps(
            U, beta, thermal_sweeps, sigma, parity_masks,
            adapt=bool(CONFIG["ADAPT_DURING_THERM"]),
            label="therm"
        )

    phis = []
    acc_all = []
    log(f"[collect] L={L} beta={beta} N_CFG={CONFIG['N_CFG']} BETWEEN={CONFIG['BETWEEN_SWEEPS']}")
    for i in range(1, int(CONFIG["N_CFG"]) + 1):
        U, sigma, acc_hist = run_sweeps(
            U, beta, int(CONFIG["BETWEEN_SWEEPS"]), sigma, parity_masks,
            adapt=False,
            label=""
        )
        acc_all.extend(acc_hist)
        phi = plaquette_scores_phi(U).detach().cpu()
        phis.append(phi)

        if i == 1 or i == CONFIG["N_CFG"] or i % max(1, CONFIG["N_CFG"] // 8) == 0:
            log(f"    [cfg] {i:4d}/{CONFIG['N_CFG']} acc_mean_recent={np.mean(acc_hist):.4f} sigma={sigma:.5f}")

    phi_all = torch.stack(phis, dim=0).contiguous()  # [Ncfg,6,L,L,L,L], CPU
    torch.save(phi_all, phi_path)
    log(f"[saved] phi cache: {phi_path}")

    if CONFIG["SAVE_LAST_FIELD"]:
        torch.save(U.detach().cpu(), U_path)
        log(f"[saved] last field: {U_path}")

    del U
    if device == "cuda":
        torch.cuda.empty_cache()

    log(f"[acceptance] mean={np.mean(acc_all):.6f} std={np.std(acc_all):.6f}")
    return phi_all.to(device)


# ======================================================================================
# THRESHOLD, INDICATORS, PATTERNS, CUMULANTS
# ======================================================================================

def empirical_threshold(phi: torch.Tensor, q: float, L: int, beta: float) -> float:
    flat = phi.reshape(-1)
    n = flat.numel()
    seed = int(CONFIG["SEED"] + 1000 * L + 100 * beta)

    if CONFIG["EXACT_QUANTILE"] or n <= CONFIG["MAX_QUANTILE_SAMPLES"]:
        vals = flat.float().detach().cpu().numpy()
    else:
        gen = torch.Generator(device=flat.device)
        gen.manual_seed(seed)
        idx = torch.randint(0, n, (CONFIG["MAX_QUANTILE_SAMPLES"],), generator=gen, device=flat.device)
        vals = flat[idx].float().detach().cpu().numpy()

    return float(np.quantile(vals, 1.0 - q))


def smoothed_indicator(phi: torch.Tensor, threshold: float, eta: float) -> torch.Tensor:
    z = (phi.float() - float(threshold)) / float(eta)
    return torch.sigmoid(torch.clamp(z, -80.0, 80.0)).contiguous()


def get_site_indices(L: int, device: str) -> Optional[torch.Tensor]:
    max_sites = int(CONFIG["MAX_ANCHOR_SITES"])
    V = L ** 4
    if max_sites <= 0 or max_sites >= V:
        return None
    g = torch.Generator(device=device)
    g.manual_seed(CONFIG["SEED"] + 777 * L)
    return torch.randperm(V, generator=g, device=device)[:max_sites]


def select_orient_sites(X: torch.Tensor, orient_idx: int, site_idx: Optional[torch.Tensor]) -> torch.Tensor:
    # X shape [Ncfg,6,L,L,L,L]. Return [Ncfg,M].
    Y = X[:, orient_idx].reshape(X.shape[0], -1)
    if site_idx is not None:
        Y = Y[:, site_idx]
    return Y


def pattern_variables(X: torch.Tensor, pattern: str, site_idx: Optional[torch.Tensor]) -> List[torch.Tensor]:
    # Local same-anchor templates. Keep this synchronized with original v17b if you have that exact library.
    o01 = ORIENT_TO_INDEX[(0, 1)]
    o02 = ORIENT_TO_INDEX[(0, 2)]
    o03 = ORIENT_TO_INDEX[(0, 3)]
    o12 = ORIENT_TO_INDEX[(1, 2)]
    o13 = ORIENT_TO_INDEX[(1, 3)]
    o23 = ORIENT_TO_INDEX[(2, 3)]

    if pattern == "pair_incident":
        idxs = [o01, o02]
    elif pattern == "triple_star":
        idxs = [o01, o02, o03]
    elif pattern == "triple_L":
        idxs = [o01, o02, o12]
    elif pattern == "quad_local_mixed":
        idxs = [o01, o02, o13, o23]
    else:
        raise ValueError(f"Unknown pattern {pattern}")

    return [select_orient_sites(X, idx, site_idx) for idx in idxs]


def mean_product(vars_: Sequence[torch.Tensor], cfg_mask: Optional[torch.Tensor] = None) -> float:
    prod = None
    for v in vars_:
        vv = v if cfg_mask is None else v[cfg_mask]
        prod = vv if prod is None else prod * vv
    return float(prod.mean().detach().cpu())


def connected_cumulant(vars_: Sequence[torch.Tensor], cfg_mask: Optional[torch.Tensor] = None) -> float:
    k = len(vars_)

    if k == 1:
        return mean_product(vars_, cfg_mask)

    if k == 2:
        x, y = vars_
        return mean_product([x, y], cfg_mask) - mean_product([x], cfg_mask) * mean_product([y], cfg_mask)

    if k == 3:
        x, y, z = vars_
        e1 = mean_product([x], cfg_mask)
        e2 = mean_product([y], cfg_mask)
        e3 = mean_product([z], cfg_mask)
        e12 = mean_product([x, y], cfg_mask)
        e13 = mean_product([x, z], cfg_mask)
        e23 = mean_product([y, z], cfg_mask)
        e123 = mean_product([x, y, z], cfg_mask)
        return e123 - e12*e3 - e13*e2 - e23*e1 + 2.0*e1*e2*e3

    if k == 4:
        E = lambda inds: mean_product([vars_[i] for i in inds], cfg_mask)

        e1, e2, e3, e4 = E([0]), E([1]), E([2]), E([3])
        e12, e13, e14 = E([0,1]), E([0,2]), E([0,3])
        e23, e24, e34 = E([1,2]), E([1,3]), E([2,3])
        e123, e124, e134, e234 = E([0,1,2]), E([0,1,3]), E([0,2,3]), E([1,2,3])
        e1234 = E([0,1,2,3])

        # kappa_4 partition formula.
        part_1_3 = e1*e234 + e2*e134 + e3*e124 + e4*e123
        part_2_2 = e12*e34 + e13*e24 + e14*e23
        part_2_1_1 = (
            e12*e3*e4 + e13*e2*e4 + e14*e2*e3 +
            e23*e1*e4 + e24*e1*e3 + e34*e1*e2
        )
        return e1234 - part_1_3 - part_2_2 + 2.0*part_2_1_1 - 6.0*e1*e2*e3*e4

    raise ValueError(f"Unsupported cumulant order {k}")


def jackknife_cumulant(vars_: Sequence[torch.Tensor], n_blocks: int) -> Tuple[float, float, int]:
    ncfg = int(vars_[0].shape[0])
    b = min(int(n_blocks), ncfg)

    theta = connected_cumulant(vars_, None)

    if b < 2:
        return theta, float("nan"), b

    estimates = []
    blocks = np.array_split(np.arange(ncfg), b)

    for block in blocks:
        mask = torch.ones(ncfg, dtype=torch.bool, device=vars_[0].device)
        mask[torch.as_tensor(block, device=vars_[0].device)] = False
        estimates.append(connected_cumulant(vars_, mask))

    est = np.asarray(estimates, dtype=np.float64)
    jk_mean = float(est.mean())
    jk_se = math.sqrt((b - 1.0) / b * float(np.sum((est - jk_mean) ** 2)))
    return theta, jk_se, b


# ======================================================================================
# SUMMARY / READOUT
# ======================================================================================

def summarize_eta_bridge(df: pd.DataFrame) -> pd.DataFrame:
    rows = []

    for (L, beta, pattern), g in df.groupby(["L", "beta", "pattern"]):
        by_eta = g.groupby("eta")["rooted_norm_qeta"].max().to_dict()
        relmax = g["rel_jk_se"].replace([np.inf, -np.inf], np.nan).max()

        r_005_001 = np.nan
        if 0.005 in by_eta and 0.01 in by_eta and by_eta[0.01] != 0:
            r_005_001 = by_eta[0.005] / by_eta[0.01]

        verdict = "PASS" if (np.isfinite(relmax) and relmax <= 0.5 and (not np.isfinite(r_005_001) or r_005_001 <= 3.0)) else "CHECK"

        rows.append({
            "L": L,
            "beta": beta,
            "pattern": pattern,
            "max_rooted_eta_0p01": by_eta.get(0.01, np.nan),
            "max_rooted_eta_0p005": by_eta.get(0.005, np.nan),
            "ratio_0p005_over_0p01": r_005_001,
            "max_rel_jk_se": relmax,
            "verdict_internal": verdict,
        })

    summary = pd.DataFrame(rows)

    baseline = str(CONFIG.get("BASELINE_CSV", "")).strip()
    if baseline:
        bpath = Path(baseline)
        if not bpath.exists():
            raise FileNotFoundError(f"BASELINE_CSV does not exist: {bpath}")

        base = pd.read_csv(bpath)
        if "pattern_kind" in base.columns and "pattern" not in base.columns:
            base = base.rename(columns={"pattern_kind": "pattern"})
        if "rooted_norm_qeta" not in base.columns:
            if "rooted_norm" in base.columns:
                base["rooted_norm_qeta"] = base["rooted_norm"]
            elif {"kappa", "q_eta_mean", "order"}.issubset(base.columns):
                base["rooted_norm_qeta"] = base["kappa"].abs() / (base["q_eta_mean"] ** (base["order"] - 1))
            else:
                raise ValueError("Baseline CSV needs rooted_norm_qeta, rooted_norm, or kappa/q_eta_mean/order.")

        base025 = base[np.isclose(base["eta"].astype(float), 0.025)]
        base_max = base025.groupby(["L", "beta", "pattern"])["rooted_norm_qeta"].max().reset_index()
        base_max = base_max.rename(columns={"rooted_norm_qeta": "max_rooted_eta_0p025"})

        summary = summary.merge(base_max, on=["L", "beta", "pattern"], how="left")
        summary["ratio_0p005_over_0p025"] = summary["max_rooted_eta_0p005"] / summary["max_rooted_eta_0p025"]
        summary["verdict_vs_0p025"] = np.where(
            (summary["ratio_0p005_over_0p025"].isna()) | (summary["ratio_0p005_over_0p025"] <= 5.0),
            "PASS",
            "CHECK",
        )

    return summary


def write_readout(run_dir: Path, df: pd.DataFrame, summary: pd.DataFrame, elapsed: float) -> None:
    lines = []
    lines.append("# PMBSF v17b eta-extension readout")
    lines.append("")
    lines.append("## Run identity")
    lines.append("")
    lines.append(f"- Run tag: `{CONFIG['RUN_TAG']}`")
    lines.append(f"- Elapsed minutes: `{elapsed/60:.3f}`")
    lines.append(f"- Device: `{CONFIG['DEVICE']}`")
    lines.append("")
    lines.append("## Config")
    lines.append("")
    lines.append("```json")
    lines.append(json.dumps(CONFIG, indent=2, sort_keys=True))
    lines.append("```")
    lines.append("")
    lines.append("## Output files")
    lines.append("")
    lines.append("- `cumulants_eta_extension.csv`")
    lines.append("- `eta_bridge_summary.csv`")
    lines.append("- `RUN_READOUT.md`")
    lines.append("")
    lines.append("## Decision rules")
    lines.append("")
    lines.append("- Clean row: `rel_jk_se <= 0.3`.")
    lines.append("- Usable row: `rel_jk_se <= 0.5`.")
    lines.append("- Internal eta bridge pass: eta=0.005 rooted norm no more than 3x eta=0.01, with max rel-JK-SE <= 0.5.")
    lines.append("- If baseline eta=0.025 is supplied: eta=0.005 rooted norm no more than 5x eta=0.025.")
    lines.append("")
    lines.append("## Summary")
    lines.append("")
    if len(summary):
        lines.append(summary.to_markdown(index=False))
    else:
        lines.append("No summary rows.")
    lines.append("")
    lines.append("## Worst cumulant rows by rooted_norm_qeta")
    lines.append("")
    if len(df):
        show_cols = [
            "L", "beta", "eta", "pattern", "order", "q_hard_emp", "q_eta_mean",
            "kappa", "jk_se", "rel_jk_se", "rooted_norm_qeta", "clean_rel_jk_le_0p3"
        ]
        worst = df.sort_values("rooted_norm_qeta", ascending=False).head(30)
        lines.append(worst[show_cols].to_markdown(index=False))
    else:
        lines.append("No rows.")
    lines.append("")
    lines.append("## Status")
    lines.append("")
    lines.append(
        "This run tests smoothing-bridge boundedness for smoothed Wilson plaquette-score indicators. "
        "It is finite-volume numerical evidence only. It is not a proof of the Wilson stochastic theorem."
    )
    lines.append("")

    (run_dir / "RUN_READOUT.md").write_text("\n".join(lines), encoding="utf-8")


# ======================================================================================
# MAIN
# ======================================================================================

def run() -> pd.DataFrame:
    set_seeds(int(CONFIG["SEED"]))

    run_id = f"{CONFIG['RUN_TAG']}_{now_id()}"
    run_dir = Path(CONFIG["OUT_ROOT"]) / run_id
    ensure_dir(run_dir)

    log("=" * 100)
    log(f"[run] {run_id}")
    log(f"[device] {CONFIG['DEVICE']}")
    if CONFIG["DEVICE"] == "cuda":
        log(f"[gpu] {torch.cuda.get_device_name(0)}")
    log(f"[outdir] {run_dir}")
    log("=" * 100)

    all_rows = []
    start = time.time()

    for L in CONFIG["L_list"]:
        for beta in CONFIG["beta_list"]:
            log("=" * 100)
            log(f"[combo] L={L}, beta={beta}")
            log("=" * 100)

            phi = generate_or_load_phi(int(L), float(beta), run_dir)
            phi = phi.to(CONFIG["DEVICE"], non_blocking=True)

            threshold = empirical_threshold(phi, float(CONFIG["q_target"]), int(L), float(beta))
            q_hard_emp = float((phi >= threshold).float().mean().detach().cpu())

            log(f"[threshold] t_q={threshold:.10g} q_target={CONFIG['q_target']} q_hard_emp={q_hard_emp:.8g}")

            site_idx = get_site_indices(int(L), CONFIG["DEVICE"])
            n_sites = int(L**4 if site_idx is None else site_idx.numel())

            for eta in CONFIG["eta_list"]:
                log("-" * 100)
                log(f"[eta] L={L} beta={beta} eta={eta}")
                X = smoothed_indicator(phi, threshold, float(eta))
                q_eta_mean = float(X.mean().detach().cpu())
                log(f"[eta] q_eta_mean={q_eta_mean:.8g}, anchor_sites={n_sites}")

                for pattern in CONFIG["PATTERNS"]:
                    vars_ = pattern_variables(X, pattern, site_idx)
                    order = len(vars_)

                    kappa, jk_se, jk_blocks = jackknife_cumulant(vars_, int(CONFIG["JACKKNIFE_BLOCKS"]))
                    rel = float(abs(jk_se) / abs(kappa)) if kappa != 0 and math.isfinite(jk_se) else float("inf")

                    rooted_qeta = float(abs(kappa) / max(q_eta_mean, 1e-300) ** (order - 1))
                    rooted_qtarget = float(abs(kappa) / float(CONFIG["q_target"]) ** (order - 1))

                    clean = bool(rel <= 0.3)
                    usable = bool(rel <= 0.5)

                    row = {
                        "L": int(L),
                        "beta": float(beta),
                        "eta": float(eta),
                        "q_target": float(CONFIG["q_target"]),
                        "threshold_t": threshold,
                        "q_hard_emp": q_hard_emp,
                        "q_eta_mean": q_eta_mean,
                        "pattern": pattern,
                        "order": int(order),
                        "n_cfg": int(phi.shape[0]),
                        "n_anchor_sites": int(n_sites),
                        "n_observations": int(phi.shape[0] * n_sites),
                        "kappa": float(kappa),
                        "jk_se": float(jk_se),
                        "rel_jk_se": float(rel),
                        "jackknife_blocks_used": int(jk_blocks),
                        "rooted_norm_qeta": rooted_qeta,
                        "rooted_norm_qtarget": rooted_qtarget,
                        "clean_rel_jk_le_0p3": clean,
                        "usable_rel_jk_le_0p5": usable,
                    }
                    all_rows.append(row)

                    log(
                        f"  {pattern:17s} k={order} "
                        f"kappa={kappa:+.6e} jk={jk_se:.3e} rel={rel:.3f} "
                        f"root_qeta={rooted_qeta:.6e} clean={clean}"
                    )

                del X
                if CONFIG["DEVICE"] == "cuda":
                    torch.cuda.empty_cache()

            del phi
            if CONFIG["DEVICE"] == "cuda":
                torch.cuda.empty_cache()

    elapsed = time.time() - start
    df = pd.DataFrame(all_rows)
    df_path = run_dir / "cumulants_eta_extension.csv"
    df.to_csv(df_path, index=False)

    summary = summarize_eta_bridge(df)
    summary_path = run_dir / "eta_bridge_summary.csv"
    summary.to_csv(summary_path, index=False)

    write_readout(run_dir, df, summary, elapsed)

    log("=" * 100)
    log(f"[done] elapsed={elapsed/60:.2f} minutes")
    log(f"[saved] {df_path}")
    log(f"[saved] {summary_path}")
    log(f"[saved] {run_dir / 'RUN_READOUT.md'}")
    log("=" * 100)

    log("[summary verdict counts]")
    if len(summary):
        log(str(summary["verdict_internal"].value_counts(dropna=False)))
    else:
        log("No summary rows.")

    return df


if __name__ == "__main__":
    run()
