#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""su2_drift_simulation.py

A cleaned, reproducible simulation + analysis harness extracted from the project notebooks.

Core features:
- Generates SU(2) lattice configurations (sigma-perturbed near-identity + Haar random)
- Estimates, per configuration:
    * Bavg  : mean plaquette defect (1 - (1/2)ReTr U_p)
    * Vbar  : 1 + Bavg
    * lap   : Monte Carlo estimate of group Laplacian ΔVbar
    * gip   : Monte Carlo estimate of <∇S_beta, ∇Vbar>
    * LV    : lap - gip  (generator applied to Vbar)
  with standard errors from MC directions.
- Saves a flat .npz suitable for downstream “ratio certificates” and beta scans.

This code is designed to be *practical*:
- Works on CPU or CUDA
- Chunks both configs and MC directions to control memory.

Notes:
- SU(2) elements are represented as unit quaternions q=(a,b,c,d).
- The exponential map uses v∈R^3 (su(2) coordinates) -> q∈S^3.

Example:
  python su2_drift_simulation.py --Ls 8 12 16 --K_total 512 --mc 128 --out decomp_Lsweep_results.npz

"""

from __future__ import annotations

import argparse
import json
import math
from dataclasses import dataclass
from typing import Dict, Iterable, List, Tuple

import numpy as np
import torch


# ---------------------------
# SU(2) quaternion ops
# ---------------------------

def su2_normalize(q: torch.Tensor, eps: float = 1e-12) -> torch.Tensor:
    return q / q.pow(2).sum(dim=-1, keepdim=True).clamp_min(eps).sqrt()


def su2_conj(q: torch.Tensor) -> torch.Tensor:
    a, b, c, d = q.unbind(-1)
    return torch.stack([a, -b, -c, -d], dim=-1)


def su2_mul(q1: torch.Tensor, q2: torch.Tensor) -> torch.Tensor:
    a1, b1, c1, d1 = q1.unbind(-1)
    a2, b2, c2, d2 = q2.unbind(-1)
    return torch.stack(
        [
            a1 * a2 - b1 * b2 - c1 * c2 - d1 * d2,
            a1 * b2 + b1 * a2 + c1 * d2 - d1 * c2,
            a1 * c2 - b1 * d2 + c1 * a2 + d1 * b2,
            a1 * d2 + b1 * c2 - c1 * b2 + d1 * a2,
        ],
        dim=-1,
    )


def su2_exp(v: torch.Tensor) -> torch.Tensor:
    """Exponential map su(2)≈R^3 -> SU(2)≈S^3 in quaternion coordinates.

    v: (..., 3)
    returns q: (..., 4) with unit norm (up to numerical error).
    """
    theta = torch.linalg.norm(v, dim=-1, keepdim=True)
    a = torch.cos(theta)

    # sinc(theta) = sin(theta)/theta, with stable small-angle expansion
    theta2 = theta * theta
    sinc = torch.where(
        theta > 1e-8,
        torch.sin(theta) / theta,
        1.0 - theta2 / 6.0,
    )
    vec = sinc * v
    return torch.cat([a, vec], dim=-1)


# ---------------------------
# Lattice plaquettes + observables
# ---------------------------

def plaquette(U: torch.Tensor, mu: int, nu: int) -> torch.Tensor:
    """P_{mu,nu}(x) = U_mu(x) U_nu(x+mu) U_mu(x+nu)^{-1} U_nu(x)^{-1}.

    U: (B, L,L,L,L, d=4, 4)
    returns: (B, L,L,L,L, 4)
    """
    U_mu = U[..., mu, :]  # (B, L,L,L,L, 4)
    U_nu = U[..., nu, :]

    U_nu_x_plus_mu = torch.roll(U_nu, shifts=-1, dims=1 + mu)
    U_mu_x_plus_nu = torch.roll(U_mu, shifts=-1, dims=1 + nu)

    return su2_mul(
        su2_mul(
            su2_mul(U_mu, U_nu_x_plus_mu),
            su2_conj(U_mu_x_plus_nu),
        ),
        su2_conj(U_nu),
    )


@torch.no_grad()
def wilson_action_Vbar_Bavg(U: torch.Tensor, beta: float) -> Tuple[torch.Tensor, torch.Tensor, torch.Tensor]:
    """Wilson action and the project’s Lyapunov observable.

    S = beta * sum_p (1 - a_p)
    Bavg = mean_p(1 - a_p)
    Vbar = 1 + Bavg

    where a_p is the real quaternion component (1/2 Re Tr U_p).
    """
    B = U.shape[0]
    d = U.shape[-2]
    defect_sum = torch.zeros((B,), device=U.device, dtype=U.dtype)
    defect_mean_sum = torch.zeros((B,), device=U.device, dtype=U.dtype)
    count = 0
    for mu in range(d):
        for nu in range(mu + 1, d):
            P = plaquette(U, mu, nu)
            defect = 1.0 - P[..., 0]
            defect_sum += defect.sum(dim=(1, 2, 3, 4))
            defect_mean_sum += defect.mean(dim=(1, 2, 3, 4))
            count += 1

    Bavg = defect_mean_sum / float(count)
    Vbar = 1.0 + Bavg
    S = beta * defect_sum
    return S, Vbar, Bavg


# ---------------------------
# Generator estimator via random su(2) directions
# ---------------------------

@dataclass
class LVEstimates:
    Vbar: torch.Tensor
    Bavg: torch.Tensor
    lap: torch.Tensor
    lap_se: torch.Tensor
    gip: torch.Tensor
    gip_se: torch.Tensor
    LV: torch.Tensor
    LV_se: torch.Tensor


@torch.no_grad()
def estimate_LV_moments_batch(
    U: torch.Tensor,
    *,
    beta: float,
    eps_fd: float,
    mc: int,
    mc_chunk: int,
    seed: int,
    xi_dtype: torch.dtype,
) -> LVEstimates:
    """Estimate lap, gip, LV with standard errors using symmetric finite differences.

    Uses random Xi ∈ R^3 per link (tangent directions) and perturbs U -> U exp(±eps Xi).
    """
    assert mc >= 2
    assert mc_chunk >= 1

    B, L = U.shape[0], U.shape[1]
    d = U.shape[-2]
    eps = float(eps_fd)

    _, V0, Bavg0 = wilson_action_Vbar_Bavg(U, beta=beta)
    V0 = V0.detach()

    def zeros():
        return torch.zeros((B,), device=U.device, dtype=U.dtype)

    sum_lv, sum_lv2 = zeros(), zeros()
    sum_lap, sum_lap2 = zeros(), zeros()
    sum_gip, sum_gip2 = zeros(), zeros()

    g = torch.Generator(device=U.device)
    g.manual_seed(int(seed))

    processed = 0
    U_base = U.unsqueeze(1)  # (B,1,L,L,L,L,d,4)

    while processed < mc:
        c = int(min(mc_chunk, mc - processed))

        # Xi in float32 is usually enough and saves a lot of memory
        Xi = torch.randn((B, c, L, L, L, L, d, 3), device=U.device, dtype=xi_dtype, generator=g)

        # exp(+eps Xi)
        exp_p = su2_exp(eps * Xi)
        U_p = su2_mul(U_base, exp_p)
        U_p_f = U_p.reshape(B * c, L, L, L, L, d, 4)
        S_p, V_p, _ = wilson_action_Vbar_Bavg(U_p_f, beta=beta)
        S_p = S_p.view(B, c)
        V_p = V_p.view(B, c)

        # exp(-eps Xi) = conj(exp(+eps Xi))
        exp_m = su2_conj(exp_p)
        U_m = su2_mul(U_base, exp_m)
        U_m_f = U_m.reshape(B * c, L, L, L, L, d, 4)
        S_m, V_m, _ = wilson_action_Vbar_Bavg(U_m_f, beta=beta)
        S_m = S_m.view(B, c)
        V_m = V_m.view(B, c)

        # Central differences
        V0c = V0.view(B, 1)
        lap = (V_p + V_m - 2.0 * V0c) / (eps * eps)
        dS = (S_p - S_m) / (2.0 * eps)
        dV = (V_p - V_m) / (2.0 * eps)
        gip = dS * dV
        lv = lap - gip

        # Accumulate sums / sumsquares over MC directions
        sum_lv += lv.sum(dim=1)
        sum_lv2 += (lv * lv).sum(dim=1)

        sum_lap += lap.sum(dim=1)
        sum_lap2 += (lap * lap).sum(dim=1)

        sum_gip += gip.sum(dim=1)
        sum_gip2 += (gip * gip).sum(dim=1)

        processed += c

        # free some memory early
        del Xi, exp_p, exp_m, U_p, U_m, U_p_f, U_m_f, S_p, S_m, V_p, V_m, lap, dS, dV, gip, lv

    def mean_se(sum_, sum2_):
        mean = sum_ / float(mc)
        var = (sum2_ - (sum_ * sum_) / float(mc)) / float(mc - 1)
        var = torch.clamp(var, min=0.0)
        se = torch.sqrt(var / float(mc))
        return mean, se

    LV_mean, LV_se = mean_se(sum_lv, sum_lv2)
    lap_mean, lap_se = mean_se(sum_lap, sum_lap2)
    gip_mean, gip_se = mean_se(sum_gip, sum_gip2)

    return LVEstimates(
        Vbar=V0,
        Bavg=Bavg0,
        lap=lap_mean,
        lap_se=lap_se,
        gip=gip_mean,
        gip_se=gip_se,
        LV=LV_mean,
        LV_se=LV_se,
    )


# ---------------------------
# Dataset streaming generator
# ---------------------------

def _make_labels(K_total: int, sigma_list: List[float], frac_haar: float, seed: int) -> Tuple[np.ndarray, np.ndarray]:
    K_total = int(K_total)
    assert 1 <= K_total
    K_haar = int(round(frac_haar * K_total))
    K_non = K_total - K_haar
    if K_non < 1:
        raise ValueError("Need at least one non-Haar sample (reduce frac_haar).")
    if len(sigma_list) < 1:
        raise ValueError("sigma_list must be non-empty.")

    counts = [K_non // len(sigma_list)] * len(sigma_list)
    for i in range(K_non - sum(counts)):
        counts[i] += 1

    sigmas = []
    kinds = []
    for sigma, k in zip(sigma_list, counts):
        sigmas.extend([float(sigma)] * int(k))
        kinds.extend([0] * int(k))

    sigmas.extend([float("nan")] * K_haar)
    kinds.extend([1] * K_haar)

    sigmas = np.asarray(sigmas, dtype=np.float64)
    kinds = np.asarray(kinds, dtype=np.int32)

    rng = np.random.default_rng(int(seed))
    perm = rng.permutation(K_total)
    return sigmas[perm], kinds[perm]


@torch.no_grad()
def iter_configs(
    *,
    L: int,
    sigmas: np.ndarray,
    kinds: np.ndarray,
    batch_configs: int,
    device: torch.device,
    dtype: torch.dtype,
    xi_dtype: torch.dtype,
    seed: int,
) -> Iterable[Tuple[torch.Tensor, np.ndarray, np.ndarray]]:
    """Yield batches of SU(2) gauge fields U plus metadata arrays."""
    assert sigmas.shape == kinds.shape
    K_total = int(sigmas.size)
    d = 4

    g = torch.Generator(device=device)
    g.manual_seed(int(seed))

    for start in range(0, K_total, batch_configs):
        end = min(K_total, start + batch_configs)
        sigma_b = sigmas[start:end]
        kind_b = kinds[start:end]
        B = end - start

        # Allocate U batch
        U = torch.empty((B, L, L, L, L, d, 4), device=device, dtype=dtype)

        mask_non = (kind_b == 0)
        mask_haar = (kind_b == 1)

        # Non-Haar: U = exp(sigma * Xi)
        if mask_non.any():
            idx = np.where(mask_non)[0]
            s = torch.tensor(sigma_b[idx], device=device, dtype=dtype).view(-1, 1, 1, 1, 1, 1, 1)
            Xi = torch.randn((idx.size, L, L, L, L, d, 3), device=device, dtype=xi_dtype, generator=g)
            U_non = su2_exp((s * Xi).to(dtype))
            U[idx] = U_non
            del Xi, s, U_non

        # Haar: random unit quaternions
        if mask_haar.any():
            idx = np.where(mask_haar)[0]
            q = torch.randn((idx.size, L, L, L, L, d, 4), device=device, dtype=dtype, generator=g)
            q = su2_normalize(q)
            U[idx] = q
            del q

        yield U, sigma_b, kind_b


# ---------------------------
# Run per-L sweep and save .npz
# ---------------------------

def run_L_sweep(
    *,
    Ls: List[int],
    K_total: int,
    beta: float,
    eps_fd: float,
    mc: int,
    mc_chunk: int,
    sigma_list: List[float],
    frac_haar: float,
    batch_configs: int,
    seed: int,
    dtype_str: str,
    xi_dtype_str: str,
    out_npz: str,
) -> Dict[str, object]:
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    dtype = torch.float64 if dtype_str.lower() == "float64" else torch.float32
    xi_dtype = torch.float32 if xi_dtype_str.lower() == "float32" else dtype

    meta = {
        "device": str(device),
        "dtype": dtype_str,
        "xi_dtype": xi_dtype_str,
        "beta": float(beta),
        "eps_fd": float(eps_fd),
        "mc": int(mc),
        "mc_chunk": int(mc_chunk),
        "K_total": int(K_total),
        "sigma_list": list(map(float, sigma_list)),
        "frac_haar": float(frac_haar),
        "batch_configs": int(batch_configs),
        "seed": int(seed),
        "Ls": list(map(int, Ls)),
    }

    out = {k: [] for k in ["L", "Bavg", "Vbar", "lap", "lap_se", "gip", "gip_se", "LV", "LV_se", "kind", "sigma"]}

    for L in Ls:
        sigmas, kinds = _make_labels(K_total=K_total, sigma_list=sigma_list, frac_haar=frac_haar, seed=seed + 10_000 * int(L))

        k_done = 0
        for U, sigma_b, kind_b in iter_configs(
            L=int(L),
            sigmas=sigmas,
            kinds=kinds,
            batch_configs=batch_configs,
            device=device,
            dtype=dtype,
            xi_dtype=xi_dtype,
            seed=seed + 1234 * int(L) + 17 * k_done,
        ):
            est = estimate_LV_moments_batch(
                U,
                beta=float(beta),
                eps_fd=float(eps_fd),
                mc=int(mc),
                mc_chunk=int(mc_chunk),
                seed=seed + 999 * int(L) + 31 * k_done,
                xi_dtype=xi_dtype,
            )

            B = U.shape[0]
            out["L"].append(np.full((B,), int(L), dtype=np.int32))
            out["kind"].append(kind_b.astype(np.int32))
            out["sigma"].append(sigma_b.astype(np.float64))

            for name, tensor in [
                ("Bavg", est.Bavg),
                ("Vbar", est.Vbar),
                ("lap", est.lap),
                ("lap_se", est.lap_se),
                ("gip", est.gip),
                ("gip_se", est.gip_se),
                ("LV", est.LV),
                ("LV_se", est.LV_se),
            ]:
                out[name].append(tensor.detach().cpu().numpy().astype(np.float64))

            k_done += B
            del U, est

        assert k_done == int(K_total), (L, k_done, K_total)

    # Concatenate
    out_np = {k: np.concatenate(v, axis=0) for k, v in out.items()}
    out_np["format"] = np.array("flat", dtype=object)
    out_np["meta"] = np.array(json.dumps(meta), dtype=object)

    np.savez(out_npz, **out_np)
    return meta


# ---------------------------
# Ratio certificates + beta scan (analysis utilities)
# ---------------------------

def beta_rescale_components(
    *,
    lap: np.ndarray,
    gip: np.ndarray,
    lap_se: np.ndarray | None,
    gip_se: np.ndarray | None,
    beta0: float,
    beta: float,
) -> Tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
    """Rescale to a new beta without re-simulating.

    Assumption:
      - V depends only on U, not on beta -> lap is beta-independent.
      - S_beta is linear in beta -> gip scales linearly in beta.

    Therefore:
      gip_beta = (beta/beta0) * gip
      LV_beta  = lap - gip_beta

    For standard errors:
      - gip_se scales linearly
      - LV_se is conservatively approximated as sqrt(lap_se^2 + gip_se_beta^2) if lap_se available.
    """
    s = float(beta) / float(beta0)
    gip_b = s * gip
    gip_se_b = s * gip_se if gip_se is not None else np.zeros_like(gip_b)
    LV_b = lap - gip_b

    if lap_se is None:
        LV_se_b = np.abs(gip_se_b)
    else:
        LV_se_b = np.sqrt(np.maximum(0.0, lap_se * lap_se + gip_se_b * gip_se_b))
    return gip_b, LV_b, gip_se_b, LV_se_b


def ratio_certificate_uniform_in_L(
    *,
    Bavg: np.ndarray,
    L: np.ndarray,
    gip: np.ndarray,
    LV: np.ndarray,
    gip_se: np.ndarray,
    LV_se: np.ndarray,
    nsigma: float,
    tau_grid: np.ndarray,
    holdout_mask: np.ndarray,
) -> Dict[str, object]:
    """Compute uniform-in-L ratio certificate over a tau grid on HOLDOUT points.

    Returns per-tau:
      c_min_all(tau) = min_{L} inf_{Bavg>=tau}(gip - nsigma*gip_se)/Bavg
      d_max_all(tau) = max_{L} sup_{Bavg>=tau}(LV + nsigma*LV_se)/Bavg
    """
    Lvals = np.unique(L)
    report_curve = []

    def per_L_indices(Lv: int) -> np.ndarray:
        return np.where((L == Lv) & holdout_mask)[0]

    for tau in tau_grid:
        tau = float(tau)
        counts_by_L = {}
        cmins = []
        dmaxs = []
        worst_c = None
        worst_d = None

        for Lv in Lvals:
            idx = per_L_indices(int(Lv))
            dom = idx[Bavg[idx] >= tau]
            counts_by_L[str(int(Lv))] = int(dom.size)
            if dom.size == 0:
                continue

            c_ratios = (gip[dom] - nsigma * gip_se[dom]) / Bavg[dom]
            d_ratios = (LV[dom] + nsigma * LV_se[dom]) / Bavg[dom]

            j_c = int(np.argmin(c_ratios))
            j_d = int(np.argmax(d_ratios))

            cmin = float(c_ratios[j_c])
            dmax = float(d_ratios[j_d])
            cmins.append(cmin)
            dmaxs.append(dmax)

            gidx_c = int(dom[j_c])
            gidx_d = int(dom[j_d])

            if worst_c is None or cmin < worst_c["cmin"]:
                worst_c = {"global_idx": gidx_c, "L": int(Lv), "Bavg": float(Bavg[gidx_c]), "gip": float(gip[gidx_c]), "gip_se": float(gip_se[gidx_c]), "LV": float(LV[gidx_c]), "LV_se": float(LV_se[gidx_c]), "cmin": cmin}

            if worst_d is None or dmax > worst_d["dmax"]:
                worst_d = {"global_idx": gidx_d, "L": int(Lv), "Bavg": float(Bavg[gidx_d]), "gip": float(gip[gidx_d]), "gip_se": float(gip_se[gidx_d]), "LV": float(LV[gidx_d]), "LV_se": float(LV_se[gidx_d]), "dmax": dmax}

        if len(cmins) == 0 or len(dmaxs) == 0:
            continue

        c_min_all = float(np.min(cmins))
        d_max_all = float(np.max(dmaxs))
        margin = min(c_min_all - 20.0, -1.0 - d_max_all)  # default project targets

        report_curve.append(
            {
                "tau": tau,
                "c_min_all": c_min_all,
                "d_max_all": d_max_all,
                "margin": margin,
                "counts_by_L": counts_by_L,
                "worst_c": worst_c,
                "worst_d": worst_d,
            }
        )

    # choose best by margin
    if not report_curve:
        return {"status": "EMPTY", "curve": []}
    best = max(report_curve, key=lambda r: r["margin"])
    return {"status": "OK", "best": best, "curve": report_curve}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--Ls", nargs="+", type=int, default=[8, 12, 16])
    ap.add_argument("--K_total", type=int, default=512)
    ap.add_argument("--beta", type=float, default=6.0)
    ap.add_argument("--eps_fd", type=float, default=5e-3)
    ap.add_argument("--mc", type=int, default=128)
    ap.add_argument("--mc_chunk", type=int, default=16)
    ap.add_argument("--sigma_list", nargs="+", type=float, default=[0.0, 0.1, 0.2, 0.4, 0.8, 1.6])
    ap.add_argument("--frac_haar", type=float, default=0.25)
    ap.add_argument("--batch_configs", type=int, default=8)
    ap.add_argument("--seed", type=int, default=0)
    ap.add_argument("--dtype", type=str, default="float64", choices=["float32", "float64"])
    ap.add_argument("--xi_dtype", type=str, default="float32", choices=["float32", "float64"])
    ap.add_argument("--out", type=str, default="decomp_Lsweep_results.npz")
    args = ap.parse_args()

    meta = run_L_sweep(
        Ls=args.Ls,
        K_total=args.K_total,
        beta=args.beta,
        eps_fd=args.eps_fd,
        mc=args.mc,
        mc_chunk=args.mc_chunk,
        sigma_list=args.sigma_list,
        frac_haar=args.frac_haar,
        batch_configs=args.batch_configs,
        seed=args.seed,
        dtype_str=args.dtype,
        xi_dtype_str=args.xi_dtype,
        out_npz=args.out,
    )

    print("[saved]", args.out)
    print("[meta]", json.dumps(meta, indent=2))


if __name__ == "__main__":
    main()
