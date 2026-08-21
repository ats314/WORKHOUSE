#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""analyze_ratio_beta_scan.py

Compact beta/tau scan for the ratio-based drift certificate.

This is intended to replace long “printer” reports with one decisive table:
  beta -> best tau0 -> (c_min_all, d_max_all, margin) and worst offenders.

Usage:
  python analyze_ratio_beta_scan.py --npz decomp_Lsweep_results.npz --beta0 6 --betas 4 6 8 10 12

It assumes the .npz is in the “flat” format with arrays:
  L, Bavg, lap, lap_se, gip, gip_se, LV, LV_se, kind, sigma
and that for each L-block, the first half are FIT and second half HOLDOUT.
"""

from __future__ import annotations

import argparse
import json
from typing import Dict, List, Tuple

import numpy as np


def load_npz(npz_path: str) -> Dict[str, np.ndarray]:
    d = dict(np.load(npz_path, allow_pickle=True))
    # Required
    for k in ["L", "Bavg", "lap", "gip"]:
        if k not in d:
            raise KeyError(f"Missing key {k} in {npz_path}")
    # Optional SE arrays
    for k in ["lap_se", "gip_se", "LV", "LV_se", "kind", "sigma"]:
        if k not in d:
            # tolerate missing; fill later
            d[k] = None
    return d


def per_L_fit_hold_indices(L: np.ndarray, Lval: int) -> Tuple[np.ndarray, np.ndarray]:
    idx = np.where(L == Lval)[0]
    n = idx.size
    if n < 4:
        return idx[:0], idx[:0]
    n_fit = n // 2
    return idx[:n_fit], idx[n_fit:]


def beta_rescale(
    lap: np.ndarray,
    gip: np.ndarray,
    lap_se: np.ndarray | None,
    gip_se: np.ndarray | None,
    beta0: float,
    beta: float,
) -> Tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
    s = float(beta) / float(beta0)
    gip_b = s * gip
    gip_se_b = s * gip_se if gip_se is not None else np.zeros_like(gip_b)
    LV_b = lap - gip_b
    if lap_se is None:
        LV_se_b = np.abs(gip_se_b)
    else:
        LV_se_b = np.sqrt(np.maximum(0.0, lap_se * lap_se + gip_se_b * gip_se_b))
    return gip_b, LV_b, gip_se_b, LV_se_b


def certificate_for_beta(
    *,
    L: np.ndarray,
    Bavg: np.ndarray,
    lap: np.ndarray,
    lap_se: np.ndarray | None,
    gip: np.ndarray,
    gip_se: np.ndarray | None,
    beta0: float,
    beta: float,
    nsigma: float,
    c_target: float,
    d_target: float,
    tau_quantiles: List[float],
) -> Dict[str, object]:
    Lvals = np.unique(L).astype(int)

    # Build tau grid from FIT quantiles per L, unioned
    taus = set()
    for Lv in Lvals:
        fit_idx, _ = per_L_fit_hold_indices(L, int(Lv))
        if fit_idx.size == 0:
            continue
        for q in tau_quantiles:
            taus.add(float(np.quantile(Bavg[fit_idx], q)))
    tau_grid = np.array(sorted({max(1e-12, t) for t in taus}), dtype=np.float64)
    if tau_grid.size == 0:
        return {"status": "EMPTY", "beta": float(beta), "curve": []}

    gip_b, LV_b, gip_se_b, LV_se_b = beta_rescale(lap, gip, lap_se, gip_se, beta0, beta)

    curve = []
    for tau in tau_grid:
        counts_by_L = {}
        cmins = []
        dmaxs = []
        worst_c = None
        worst_d = None

        for Lv in Lvals:
            _, hold_idx = per_L_fit_hold_indices(L, int(Lv))
            dom = hold_idx[Bavg[hold_idx] >= tau]
            counts_by_L[str(int(Lv))] = int(dom.size)
            if dom.size == 0:
                continue

            c_rat = (gip_b[dom] - nsigma * gip_se_b[dom]) / Bavg[dom]
            d_rat = (LV_b[dom] + nsigma * LV_se_b[dom]) / Bavg[dom]

            j_c = int(np.argmin(c_rat))
            j_d = int(np.argmax(d_rat))

            cmin = float(c_rat[j_c])
            dmax = float(d_rat[j_d])
            cmins.append(cmin)
            dmaxs.append(dmax)

            gidx_c = int(dom[j_c])
            gidx_d = int(dom[j_d])

            if worst_c is None or cmin < worst_c["cmin"]:
                worst_c = {"global_idx": gidx_c, "L": int(Lv), "tau": float(tau), "Bavg": float(Bavg[gidx_c]), "gip": float(gip_b[gidx_c]), "gip_se": float(gip_se_b[gidx_c]), "cmin": cmin}
            if worst_d is None or dmax > worst_d["dmax"]:
                worst_d = {"global_idx": gidx_d, "L": int(Lv), "tau": float(tau), "Bavg": float(Bavg[gidx_d]), "LV": float(LV_b[gidx_d]), "LV_se": float(LV_se_b[gidx_d]), "dmax": dmax}

        if len(cmins) == 0 or len(dmaxs) == 0:
            continue

        c_min_all = float(np.min(cmins))
        d_max_all = float(np.max(dmaxs))
        margin = min(c_min_all - c_target, (-d_target) - d_max_all)

        curve.append(
            {
                "tau": float(tau),
                "c_min_all": c_min_all,
                "d_max_all": d_max_all,
                "margin": margin,
                "counts_by_L": counts_by_L,
                "worst_c": worst_c,
                "worst_d": worst_d,
            }
        )

    if not curve:
        return {"status": "EMPTY", "beta": float(beta), "curve": []}

    best = max(curve, key=lambda r: r["margin"])
    status = "PASS" if (best["c_min_all"] >= c_target and best["d_max_all"] <= -d_target) else "FAIL"

    return {
        "status": status,
        "beta": float(beta),
        "tau0": best["tau"],
        "c_min_all": best["c_min_all"],
        "d_max_all": best["d_max_all"],
        "margin": best["margin"],
        "counts_by_L": best["counts_by_L"],
        "worst_c": best["worst_c"],
        "worst_d": best["worst_d"],
        "curve": curve,
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--npz", required=True)
    ap.add_argument("--beta0", type=float, default=6.0)
    ap.add_argument("--betas", nargs="+", type=float, default=[4, 6, 8, 10, 12])
    ap.add_argument("--nsigma", type=float, default=2.0)
    ap.add_argument("--c_target", type=float, default=20.0)
    ap.add_argument("--d_target", type=float, default=1.0)
    ap.add_argument("--tau_quantiles", nargs="+", type=float, default=[0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.67, 0.75, 0.8, 0.9, 0.95])
    ap.add_argument("--out_json", type=str, default="ratio_beta_scan_best.json")
    args = ap.parse_args()

    d = load_npz(args.npz)
    L = np.asarray(d["L"]).astype(np.int32).reshape(-1)
    Bavg = np.asarray(d["Bavg"]).astype(np.float64).reshape(-1)
    lap = np.asarray(d["lap"]).astype(np.float64).reshape(-1)
    gip = np.asarray(d["gip"]).astype(np.float64).reshape(-1)

    lap_se = np.asarray(d["lap_se"]).astype(np.float64).reshape(-1) if d["lap_se"] is not None else None
    gip_se = np.asarray(d["gip_se"]).astype(np.float64).reshape(-1) if d["gip_se"] is not None else None

    results = []
    for beta in args.betas:
        rep = certificate_for_beta(
            L=L,
            Bavg=Bavg,
            lap=lap,
            lap_se=lap_se,
            gip=gip,
            gip_se=gip_se,
            beta0=args.beta0,
            beta=float(beta),
            nsigma=float(args.nsigma),
            c_target=float(args.c_target),
            d_target=float(args.d_target),
            tau_quantiles=list(map(float, args.tau_quantiles)),
        )
        results.append(rep)

    # Choose best PASS by margin, else best FAIL by margin
    passes = [r for r in results if r.get("status") == "PASS"]
    best = max(passes, key=lambda r: r["margin"]) if passes else max(results, key=lambda r: r.get("margin", -1e9))

    # Print compact summary
    print("=== BETA SCAN (compact) ===")
    for r in results:
        if r.get("status") in ("PASS", "FAIL"):
            print(
                f"beta={r['beta']:6.2f} | {r['status']:4s} | tau0={r['tau0']:.6f} | "
                f"c_min_all={r['c_min_all']:.6f} | d_max_all={r['d_max_all']:.6f} | margin={r['margin']:.6f}"
            )
        else:
            print(f"beta={r.get('beta', float('nan')):6.2f} | EMPTY")

    print("\n=== BEST OVERALL ===")
    print(json.dumps({k: best[k] for k in best if k != 'curve'}, indent=2))

    with open(args.out_json, "w", encoding="utf-8") as f:
        json.dump(best, f, indent=2)
    print("[saved]", args.out_json)


if __name__ == "__main__":
    main()
