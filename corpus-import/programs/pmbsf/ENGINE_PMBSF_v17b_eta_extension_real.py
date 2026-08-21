#!/usr/bin/env python3
"""
PMBSF v17b eta-extension: smoothing-bridge check at eta = 0.01, 0.005.

Purpose
-------
Measure connected cumulants of smoothed plaquette defect indicators

    X_{p,eta} = sigmoid((phi_p - t_q) / eta)

at the sparse stress threshold q_target, where t_q is chosen from the empirical
hard plaquette-score distribution so that P(phi_p >= t_q) ~= q_target.

This script is intentionally strict:
- It does NOT create dummy fields.
- It does NOT create random plaquette scores.
- It does NOT create dummy cumulants.
- It exits if it cannot find real data.

Accepted input formats
----------------------
Preferred:
  Precomputed plaquette score tensors phi with shape:
    [Ncfg, 6, L, L, L, L] or [Ncfg, 6, V] or [Ncfg, Nplaq]
  where phi = 1 - 1/2 ReTr(U_p).

Also supported:
  SU(2) link fields with shape:
    quaternion: [Ncfg, 4, L, L, L, L, 4] with quaternion order (a,b,c,d)
    matrix:     [Ncfg, 4, L, L, L, L, 2, 2] complex dtype
  The script computes the six plaquette orientations internally.

Examples
--------
python ENGINE_PMBSF_v17b_eta_extension_real.py \
  --input-root /content/thermalized_fields \
  --outdir /content/PMBSF_v17b_eta_ext \
  --L-list 12 16 24 \
  --beta-list 3.5 4.0 \
  --eta-list 0.01 0.005 \
  --q-target 0.003 \
  --jackknife-blocks 50 \
  --baseline-csv /content/v17b_locked_readout/cumulants.csv

Output
------
- cumulants_eta_extension.csv
- eta_bridge_summary.csv
- RUN_READOUT.md
"""

import argparse
import json
import math
import os
import re
import sys
import time
from pathlib import Path
from typing import Dict, Iterable, List, Optional, Sequence, Tuple

import numpy as np
import pandas as pd
import torch


ORIENTS: List[Tuple[int, int]] = [(0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3)]
ORIENT_TO_INDEX: Dict[Tuple[int, int], int] = {o: i for i, o in enumerate(ORIENTS)}


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser()
    p.add_argument("--input-root", type=str, required=True, help="Directory containing real phi or field tensors.")
    p.add_argument("--outdir", type=str, required=True)
    p.add_argument("--L-list", type=int, nargs="+", default=[12, 16, 24])
    p.add_argument("--beta-list", type=float, nargs="+", default=[3.5, 4.0])
    p.add_argument("--eta-list", type=float, nargs="+", default=[0.01, 0.005])
    p.add_argument("--q-target", type=float, default=0.003)
    p.add_argument("--device", type=str, default="cuda" if torch.cuda.is_available() else "cpu")
    p.add_argument("--jackknife-blocks", type=int, default=50)
    p.add_argument("--max-quantile-samples", type=int, default=5_000_000)
    p.add_argument("--exact-quantile", action="store_true", help="Use exact quantile over full phi tensor. Can be memory-heavy.")
    p.add_argument("--max-anchor-sites", type=int, default=0, help="0 means use all sites. Otherwise sample this many site anchors.")
    p.add_argument("--baseline-csv", type=str, default="", help="Optional locked v17b baseline CSV containing eta=0.025/0.05 rows.")
    p.add_argument("--seed", type=int, default=23060524)
    return p.parse_args()


def log(msg: str) -> None:
    print(msg, flush=True)


def safe_beta_string(beta: float) -> List[str]:
    raw = f"{beta:g}"
    return [raw, raw.replace(".", "p"), raw.replace(".", "_")]


def find_data_file(root: Path, L: int, beta: float) -> Path:
    beta_variants = safe_beta_string(beta)
    candidates: List[Path] = []

    exts = ["*.pt", "*.pth", "*.npy", "*.npz"]
    for ext in exts:
        for b in beta_variants:
            patterns = [
                f"*phi*L{L}*beta{b}*{ext[1:]}",
                f"*plaq*L{L}*beta{b}*{ext[1:]}",
                f"*field*L{L}*beta{b}*{ext[1:]}",
                f"*U*L{L}*beta{b}*{ext[1:]}",
                f"*L{L}*beta{b}*{ext[1:]}",
            ]
            for pat in patterns:
                candidates.extend(root.rglob(pat))

    candidates = sorted(set(candidates))
    if not candidates:
        raise FileNotFoundError(
            f"No real input tensor found for L={L}, beta={beta} under {root}. "
            "Expected a phi/plaq/field/U tensor file with L and beta in the filename."
        )

    # Prefer precomputed phi/plaquette-score files over raw fields.
    def score(path: Path) -> Tuple[int, int]:
        name = path.name.lower()
        phi_score = 0 if ("phi" in name or "plaq" in name or "score" in name) else 1
        size_score = path.stat().st_size
        return (phi_score, size_score)

    chosen = sorted(candidates, key=score)[0]
    log(f"[data] L={L} beta={beta}: using {chosen}")
    return chosen


def load_tensor(path: Path, device: str) -> torch.Tensor:
    suffix = path.suffix.lower()
    if suffix in [".pt", ".pth"]:
        obj = torch.load(path, map_location="cpu")
        if isinstance(obj, dict):
            # Prefer obvious keys.
            for key in ["phi", "phi_p", "plaquette_scores", "plaq_scores", "scores", "fields", "U", "links"]:
                if key in obj:
                    obj = obj[key]
                    break
            else:
                keys = list(obj.keys())
                raise ValueError(f"{path} is a dict but no recognized tensor key was found. Keys={keys}")
        if not torch.is_tensor(obj):
            obj = torch.as_tensor(obj)
        return obj.to(device)

    if suffix == ".npy":
        arr = np.load(path, allow_pickle=False)
        return torch.as_tensor(arr).to(device)

    if suffix == ".npz":
        npz = np.load(path, allow_pickle=False)
        keys = list(npz.keys())
        preferred = ["phi", "phi_p", "plaquette_scores", "plaq_scores", "scores", "fields", "U", "links"]
        for key in preferred:
            if key in npz:
                return torch.as_tensor(npz[key]).to(device)
        if len(keys) == 1:
            return torch.as_tensor(npz[keys[0]]).to(device)
        raise ValueError(f"{path} has multiple arrays but no recognized key. Keys={keys}")

    raise ValueError(f"Unsupported file extension: {path}")


def qmul(x: torch.Tensor, y: torch.Tensor) -> torch.Tensor:
    """Quaternion multiply, order (a,b,c,d), broadcast over leading dims."""
    a, b, c, d = x.unbind(-1)
    e, f, g, h = y.unbind(-1)
    return torch.stack(
        [
            a * e - b * f - c * g - d * h,
            a * f + b * e + c * h - d * g,
            a * g - b * h + c * e + d * f,
            a * h + b * g - c * f + d * e,
        ],
        dim=-1,
    )


def qconj(x: torch.Tensor) -> torch.Tensor:
    y = x.clone()
    y[..., 1:] = -y[..., 1:]
    return y


def matrix_dagger(x: torch.Tensor) -> torch.Tensor:
    return x.conj().transpose(-1, -2)


def roll_lattice(x: torch.Tensor, direction: int, shift: int = -1) -> torch.Tensor:
    # x has shape [Ncfg, L, L, L, L, ...]
    return torch.roll(x, shifts=shift, dims=1 + direction)


def compute_phi_from_quaternion_links(U: torch.Tensor) -> torch.Tensor:
    """
    U shape [Ncfg, 4, L, L, L, L, 4].
    Returns phi shape [Ncfg, 6, L, L, L, L].
    """
    if U.shape[1] != 4 or U.shape[-1] != 4:
        raise ValueError(f"Bad quaternion link shape: {tuple(U.shape)}")

    phis = []
    for mu, nu in ORIENTS:
        U_mu = U[:, mu]
        U_nu = U[:, nu]
        U_nu_x_plus_mu = roll_lattice(U_nu, mu, -1)
        U_mu_x_plus_nu = roll_lattice(U_mu, nu, -1)
        plaq = qmul(qmul(qmul(U_mu, U_nu_x_plus_mu), qconj(U_mu_x_plus_nu)), qconj(U_nu))
        scalar = plaq[..., 0].clamp(-1.0, 1.0)
        phi = 1.0 - scalar
        phis.append(phi)
    return torch.stack(phis, dim=1).contiguous()


def compute_phi_from_matrix_links(U: torch.Tensor) -> torch.Tensor:
    """
    U shape [Ncfg, 4, L, L, L, L, 2, 2].
    Returns phi shape [Ncfg, 6, L, L, L, L].
    """
    if U.shape[1] != 4 or U.shape[-2:] != (2, 2):
        raise ValueError(f"Bad matrix link shape: {tuple(U.shape)}")

    phis = []
    for mu, nu in ORIENTS:
        U_mu = U[:, mu]
        U_nu = U[:, nu]
        U_nu_x_plus_mu = roll_lattice(U_nu, mu, -1)
        U_mu_x_plus_nu = roll_lattice(U_mu, nu, -1)
        plaq = U_mu @ U_nu_x_plus_mu @ matrix_dagger(U_mu_x_plus_nu) @ matrix_dagger(U_nu)
        tr_re = torch.real(torch.diagonal(plaq, dim1=-2, dim2=-1).sum(-1))
        phi = 1.0 - 0.5 * tr_re
        phis.append(phi)
    return torch.stack(phis, dim=1).contiguous()


def normalize_phi_shape(x: torch.Tensor, L: int) -> torch.Tensor:
    """
    Return phi as float32 tensor [Ncfg, 6, L, L, L, L].
    Detect whether x is already phi or a link field.
    """
    x = x.detach()
    if not x.is_floating_point() and not torch.is_complex(x):
        x = x.float()

    shape = tuple(x.shape)

    # Already [Ncfg, 6, L,L,L,L].
    if x.ndim == 6 and x.shape[1] == 6 and all(s == L for s in x.shape[2:]):
        return x.float().contiguous()

    # [Ncfg, 6, V].
    if x.ndim == 3 and x.shape[1] == 6 and x.shape[2] == L**4:
        return x.reshape(x.shape[0], 6, L, L, L, L).float().contiguous()

    # [Ncfg, Nplaq] = [Ncfg, 6*L^4].
    if x.ndim == 2 and x.shape[1] == 6 * L**4:
        return x.reshape(x.shape[0], 6, L, L, L, L).float().contiguous()

    # Quaternion links [Ncfg,4,L,L,L,L,4].
    if x.ndim == 7 and x.shape[1] == 4 and all(s == L for s in x.shape[2:6]) and x.shape[-1] == 4:
        return compute_phi_from_quaternion_links(x.float())

    # Matrix links [Ncfg,4,L,L,L,L,2,2].
    if x.ndim == 8 and x.shape[1] == 4 and all(s == L for s in x.shape[2:6]) and x.shape[-2:] == (2, 2):
        return compute_phi_from_matrix_links(x)

    raise ValueError(
        f"Cannot interpret tensor shape {shape} for L={L}. "
        "Expected phi [N,6,L,L,L,L], phi [N,6,V], phi [N,6V], "
        "quaternion links [N,4,L,L,L,L,4], or matrix links [N,4,L,L,L,L,2,2]."
    )


def empirical_threshold(phi: torch.Tensor, q: float, max_samples: int, exact: bool, seed: int) -> float:
    flat = phi.reshape(-1)
    n = flat.numel()
    prob = 1.0 - q
    if exact or n <= max_samples:
        vals = flat.float().detach().cpu().numpy()
    else:
        gen = torch.Generator(device=flat.device)
        gen.manual_seed(seed)
        idx = torch.randint(0, n, (max_samples,), generator=gen, device=flat.device)
        vals = flat[idx].float().detach().cpu().numpy()
    return float(np.quantile(vals, prob))


def make_smoothed_indicator(phi: torch.Tensor, threshold: float, eta: float) -> torch.Tensor:
    z = (phi.float() - float(threshold)) / float(eta)
    # Clamp to avoid inf gradients/exp overflow; no gradient used, but this is numerically stable.
    return torch.sigmoid(torch.clamp(z, -80.0, 80.0)).contiguous()


def get_site_indices(L: int, max_anchor_sites: int, device: str, seed: int) -> Optional[torch.Tensor]:
    V = L**4
    if max_anchor_sites <= 0 or max_anchor_sites >= V:
        return None
    gen = torch.Generator(device=device)
    gen.manual_seed(seed + 17 * L)
    return torch.randperm(V, generator=gen, device=device)[:max_anchor_sites]


def select_oriented_site(X: torch.Tensor, orient_index: int, site_idx: Optional[torch.Tensor]) -> torch.Tensor:
    """
    X shape [Ncfg, 6, L,L,L,L].
    Returns [Ncfg, M_sites].
    """
    Y = X[:, orient_index].reshape(X.shape[0], -1)
    if site_idx is not None:
        Y = Y[:, site_idx]
    return Y


def pattern_variables(X: torch.Tensor, pattern: str, site_idx: Optional[torch.Tensor]) -> List[torch.Tensor]:
    """
    Pattern definitions must match the original v17b pattern library for strict comparability.
    These are canonical local support templates over plaquette orientations at the same anchor site.

    pair_incident:
        p01(x), p02(x) share the mu=0 link at x.
    triple_star:
        p01(x), p02(x), p03(x) share the mu=0 link at x.
    triple_L:
        p01(x), p02(x), p12(x) is a local L/triangle-like three-plaquette support.
    quad_local_mixed:
        p01(x), p02(x), p13(x), p23(x) is a four-plaquette local mixed support.
    """
    o01 = ORIENT_TO_INDEX[(0, 1)]
    o02 = ORIENT_TO_INDEX[(0, 2)]
    o03 = ORIENT_TO_INDEX[(0, 3)]
    o12 = ORIENT_TO_INDEX[(1, 2)]
    o13 = ORIENT_TO_INDEX[(1, 3)]
    o23 = ORIENT_TO_INDEX[(2, 3)]

    if pattern == "pair_incident":
        inds = [o01, o02]
    elif pattern == "triple_star":
        inds = [o01, o02, o03]
    elif pattern == "triple_L":
        inds = [o01, o02, o12]
    elif pattern == "quad_local_mixed":
        inds = [o01, o02, o13, o23]
    else:
        raise ValueError(f"Unknown pattern: {pattern}")

    return [select_oriented_site(X, i, site_idx) for i in inds]


def moment(vars_: Sequence[torch.Tensor], cfg_mask: Optional[torch.Tensor] = None) -> float:
    prod = None
    for v in vars_:
        vv = v if cfg_mask is None else v[cfg_mask]
        prod = vv if prod is None else prod * vv
    return float(prod.mean().detach().cpu())


def cumulant(vars_: Sequence[torch.Tensor], cfg_mask: Optional[torch.Tensor] = None) -> float:
    k = len(vars_)
    if k == 2:
        x, y = vars_
        return moment([x, y], cfg_mask) - moment([x], cfg_mask) * moment([y], cfg_mask)

    if k == 3:
        x, y, z = vars_
        e1, e2, e3 = moment([x], cfg_mask), moment([y], cfg_mask), moment([z], cfg_mask)
        e12, e13, e23 = moment([x, y], cfg_mask), moment([x, z], cfg_mask), moment([y, z], cfg_mask)
        e123 = moment([x, y, z], cfg_mask)
        return e123 - e12 * e3 - e13 * e2 - e23 * e1 + 2.0 * e1 * e2 * e3

    if k == 4:
        x1, x2, x3, x4 = vars_
        E = lambda inds: moment([vars_[i] for i in inds], cfg_mask)
        e1, e2, e3, e4 = E([0]), E([1]), E([2]), E([3])
        e12, e13, e14 = E([0, 1]), E([0, 2]), E([0, 3])
        e23, e24, e34 = E([1, 2]), E([1, 3]), E([2, 3])
        e123, e124, e134, e234 = E([0, 1, 2]), E([0, 1, 3]), E([0, 2, 3]), E([1, 2, 3])
        e1234 = E([0, 1, 2, 3])
        part2 = e1 * e234 + e2 * e134 + e3 * e124 + e4 * e123 + e12 * e34 + e13 * e24 + e14 * e23
        part3 = (
            e12 * e3 * e4 + e13 * e2 * e4 + e14 * e2 * e3
            + e23 * e1 * e4 + e24 * e1 * e3 + e34 * e1 * e2
        )
        return e1234 - part2 + 2.0 * part3 - 6.0 * e1 * e2 * e3 * e4

    raise ValueError(f"Cumulant order {k} not implemented")


def jackknife_cumulant(vars_: Sequence[torch.Tensor], n_blocks: int) -> Tuple[float, float, int]:
    """
    Jackknife over configuration axis. Each leave-one-block estimate uses all anchor sites.
    """
    ncfg = vars_[0].shape[0]
    b = min(n_blocks, ncfg)
    if b < 2:
        theta = cumulant(vars_)
        return theta, float("nan"), 1

    blocks = np.array_split(np.arange(ncfg), b)
    estimates = []
    all_idx = torch.arange(ncfg, device=vars_[0].device)

    for block in blocks:
        mask = torch.ones(ncfg, dtype=torch.bool, device=vars_[0].device)
        mask[torch.as_tensor(block, device=vars_[0].device)] = False
        estimates.append(cumulant(vars_, cfg_mask=mask))

    estimates_np = np.asarray(estimates, dtype=np.float64)
    theta_full = cumulant(vars_)
    jk_mean = estimates_np.mean()
    jk_se = math.sqrt((b - 1) / b * float(np.sum((estimates_np - jk_mean) ** 2)))
    return theta_full, jk_se, b


def summarize_eta_bridge(df: pd.DataFrame, baseline_csv: str, outdir: Path) -> pd.DataFrame:
    frames = [df.copy()]
    if baseline_csv:
        base_path = Path(baseline_csv)
        if not base_path.exists():
            raise FileNotFoundError(f"baseline-csv does not exist: {base_path}")
        base = pd.read_csv(base_path)

        # Try to normalize common column names.
        rename = {}
        if "pattern_kind" in base.columns and "pattern" not in base.columns:
            rename["pattern_kind"] = "pattern"
        if "rel_JK_SE" in base.columns and "rel_jk_se" not in base.columns:
            rename["rel_JK_SE"] = "rel_jk_se"
        base = base.rename(columns=rename)

        needed = {"L", "beta", "eta", "pattern"}
        if not needed.issubset(set(base.columns)):
            raise ValueError(f"baseline-csv missing required columns {needed}. Found {set(base.columns)}")

        if "rooted_norm_qeta" not in base.columns:
            # Best-effort fallback from kappa and q/q_eta.
            if "kappa" in base.columns and "q_eta_mean" in base.columns and "order" in base.columns:
                base["rooted_norm_qeta"] = base["kappa"].abs() / (base["q_eta_mean"] ** (base["order"] - 1))
            elif "rooted_norm" in base.columns:
                base["rooted_norm_qeta"] = base["rooted_norm"]
            else:
                raise ValueError("baseline-csv needs rooted_norm_qeta or enough columns to compute it.")

        frames.append(base[df.columns.intersection(base.columns).tolist()].copy())

    all_df = pd.concat(frames, ignore_index=True, sort=False)

    group_cols = ["L", "beta", "pattern"]
    rows = []
    for key, g in all_df.groupby(group_cols):
        L, beta, pattern = key
        gg = g.copy()
        gg["abs_root"] = gg["rooted_norm_qeta"].abs()
        by_eta = gg.groupby("eta")["abs_root"].max().to_dict()

        ratio_0005_to_001 = (
            by_eta.get(0.005, np.nan) / by_eta.get(0.01, np.nan)
            if by_eta.get(0.01, np.nan) not in [0, np.nan] else np.nan
        )
        ratio_001_to_0025 = (
            by_eta.get(0.01, np.nan) / by_eta.get(0.025, np.nan)
            if by_eta.get(0.025, np.nan) not in [0, np.nan] else np.nan
        )
        ratio_0005_to_0025 = (
            by_eta.get(0.005, np.nan) / by_eta.get(0.025, np.nan)
            if by_eta.get(0.025, np.nan) not in [0, np.nan] else np.nan
        )
        max_rel_jk = float(gg["rel_jk_se"].replace([np.inf, -np.inf], np.nan).max()) if "rel_jk_se" in gg else np.nan

        # Conservative pass/fail flags.
        clean_enough = bool(np.isfinite(max_rel_jk) and max_rel_jk <= 0.5)
        bounded_internal = bool((not np.isfinite(ratio_0005_to_001)) or ratio_0005_to_001 <= 3.0)
        bounded_vs_baseline = bool((not np.isfinite(ratio_0005_to_0025)) or ratio_0005_to_0025 <= 5.0)

        rows.append({
            "L": L,
            "beta": beta,
            "pattern": pattern,
            "max_root_eta_0p025": by_eta.get(0.025, np.nan),
            "max_root_eta_0p01": by_eta.get(0.01, np.nan),
            "max_root_eta_0p005": by_eta.get(0.005, np.nan),
            "ratio_0p005_over_0p01": ratio_0005_to_001,
            "ratio_0p01_over_0p025": ratio_001_to_0025,
            "ratio_0p005_over_0p025": ratio_0005_to_0025,
            "max_rel_jk_se": max_rel_jk,
            "clean_enough_rel_jk_le_0p5": clean_enough,
            "bounded_internal_ratio_le_3": bounded_internal,
            "bounded_vs_baseline_ratio_le_5": bounded_vs_baseline,
            "verdict": "PASS" if clean_enough and bounded_internal and bounded_vs_baseline else "CHECK",
        })

    summary = pd.DataFrame(rows)
    summary.to_csv(outdir / "eta_bridge_summary.csv", index=False)
    return summary


def write_readout(outdir: Path, config: dict, cumulants: pd.DataFrame, summary: pd.DataFrame, elapsed: float) -> None:
    lines = []
    lines.append("# PMBSF v17b eta-extension readout")
    lines.append("")
    lines.append("## Run configuration")
    lines.append("")
    lines.append("```json")
    lines.append(json.dumps(config, indent=2, sort_keys=True))
    lines.append("```")
    lines.append("")
    lines.append(f"Elapsed seconds: `{elapsed:.3f}`")
    lines.append("")
    lines.append("## Files")
    lines.append("")
    lines.append("- `cumulants_eta_extension.csv`")
    lines.append("- `eta_bridge_summary.csv`")
    lines.append("")
    lines.append("## Decision rules")
    lines.append("")
    lines.append("- Clean enough: `rel_jk_se <= 0.5` for summary grouping.")
    lines.append("- Internal boundedness: max rooted norm at eta=0.005 no more than 3x eta=0.01.")
    lines.append("- Baseline boundedness, if baseline CSV supplied: eta=0.005 no more than 5x eta=0.025.")
    lines.append("")
    lines.append("## Summary verdict counts")
    lines.append("")
    if not summary.empty:
        lines.append(summary["verdict"].value_counts(dropna=False).to_markdown())
    else:
        lines.append("No summary rows.")
    lines.append("")
    lines.append("## Worst extension rows by rooted_norm_qeta")
    lines.append("")
    if not cumulants.empty:
        cols = ["L", "beta", "eta", "pattern", "order", "q_hard_emp", "q_eta_mean", "kappa", "jk_se", "rel_jk_se", "rooted_norm_qeta"]
        worst = cumulants.sort_values("rooted_norm_qeta", ascending=False).head(20)
        lines.append(worst[cols].to_markdown(index=False))
    else:
        lines.append("No cumulant rows.")
    lines.append("")
    lines.append("## Interpretation")
    lines.append("")
    lines.append(
        "This readout is evidence for or against smoothing-bridge boundedness only if the input tensors "
        "are real thermalized Wilson data or real precomputed plaquette scores. It is not a Wilson stochastic theorem."
    )
    lines.append("")
    (outdir / "RUN_READOUT.md").write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    args = parse_args()
    torch.manual_seed(args.seed)
    np.random.seed(args.seed)

    outdir = Path(args.outdir)
    outdir.mkdir(parents=True, exist_ok=True)
    root = Path(args.input_root)

    if not root.exists():
        raise FileNotFoundError(f"input-root does not exist: {root}")

    patterns = ["pair_incident", "triple_star", "triple_L", "quad_local_mixed"]
    rows = []
    start = time.time()

    log("=" * 100)
    log("[run] PMBSF_v17b_eta_extension_real")
    log(f"[device] {args.device}")
    log(f"[input-root] {root}")
    log(f"[outdir] {outdir}")
    log("=" * 100)

    for L in args.L_list:
        for beta in args.beta_list:
            data_file = find_data_file(root, L, beta)
            raw = load_tensor(data_file, args.device)
            phi = normalize_phi_shape(raw, L)
            del raw
            torch.cuda.empty_cache() if args.device.startswith("cuda") else None

            ncfg = int(phi.shape[0])
            threshold = empirical_threshold(
                phi=phi,
                q=args.q_target,
                max_samples=args.max_quantile_samples,
                exact=args.exact_quantile,
                seed=args.seed + 1000 * L + int(100 * beta),
            )
            q_hard_emp = float((phi >= threshold).float().mean().detach().cpu())

            log("-" * 100)
            log(f"[combo] L={L} beta={beta} ncfg={ncfg} threshold_t={threshold:.10g} q_hard_emp={q_hard_emp:.8g}")

            site_idx = get_site_indices(L, args.max_anchor_sites, args.device, args.seed)
            n_sites_used = L**4 if site_idx is None else int(site_idx.numel())

            for eta in args.eta_list:
                X = make_smoothed_indicator(phi, threshold, eta)
                q_eta_mean = float(X.mean().detach().cpu())
                log(f"  [eta] eta={eta:g} q_eta_mean={q_eta_mean:.8g} anchor_sites={n_sites_used}")

                for pattern in patterns:
                    vars_ = pattern_variables(X, pattern, site_idx)
                    order = len(vars_)
                    kappa, jk_se, jk_blocks_used = jackknife_cumulant(vars_, args.jackknife_blocks)
                    rel_jk_se = float(abs(jk_se) / abs(kappa)) if kappa != 0 and math.isfinite(jk_se) else float("inf")

                    rooted_qeta = float(abs(kappa) / max(q_eta_mean, 1e-300) ** (order - 1))
                    rooted_qtarget = float(abs(kappa) / args.q_target ** (order - 1))

                    clean = bool(rel_jk_se <= 0.3)
                    usable = bool(rel_jk_se <= 0.5)

                    log(
                        f"    {pattern:17s} k={order} "
                        f"kappa={kappa:+.6e} jk={jk_se:.3e} rel={rel_jk_se:.3f} "
                        f"root_qeta={rooted_qeta:.6e}"
                    )

                    rows.append({
                        "L": L,
                        "beta": beta,
                        "q_target": args.q_target,
                        "eta": eta,
                        "pattern": pattern,
                        "order": order,
                        "source_file": str(data_file),
                        "n_configs": ncfg,
                        "n_anchor_sites": n_sites_used,
                        "n_observations": int(ncfg * n_sites_used),
                        "threshold_t": threshold,
                        "q_hard_emp": q_hard_emp,
                        "q_eta_mean": q_eta_mean,
                        "kappa": kappa,
                        "jk_se": jk_se,
                        "rel_jk_se": rel_jk_se,
                        "jackknife_blocks_used": jk_blocks_used,
                        "rooted_norm_qeta": rooted_qeta,
                        "rooted_norm_qtarget": rooted_qtarget,
                        "clean_rel_jk_le_0p3": clean,
                        "usable_rel_jk_le_0p5": usable,
                    })

                del X
                torch.cuda.empty_cache() if args.device.startswith("cuda") else None

            del phi
            torch.cuda.empty_cache() if args.device.startswith("cuda") else None

    df = pd.DataFrame(rows)
    cumulant_path = outdir / "cumulants_eta_extension.csv"
    df.to_csv(cumulant_path, index=False)

    summary = summarize_eta_bridge(df, args.baseline_csv, outdir)
    elapsed = time.time() - start

    config = {
        "input_root": str(root),
        "outdir": str(outdir),
        "L_list": args.L_list,
        "beta_list": args.beta_list,
        "eta_list": args.eta_list,
        "q_target": args.q_target,
        "device": args.device,
        "jackknife_blocks": args.jackknife_blocks,
        "max_quantile_samples": args.max_quantile_samples,
        "exact_quantile": args.exact_quantile,
        "max_anchor_sites": args.max_anchor_sites,
        "baseline_csv": args.baseline_csv,
        "seed": args.seed,
    }
    write_readout(outdir, config, df, summary, elapsed)

    log("=" * 100)
    log(f"[done] elapsed={elapsed/60:.2f} min")
    log(f"[saved] {cumulant_path}")
    log(f"[saved] {outdir / 'eta_bridge_summary.csv'}")
    log(f"[saved] {outdir / 'RUN_READOUT.md'}")
    log("=" * 100)

    if not summary.empty:
        log("[summary verdict counts]")
        log(str(summary["verdict"].value_counts(dropna=False)))


if __name__ == "__main__":
    main()
