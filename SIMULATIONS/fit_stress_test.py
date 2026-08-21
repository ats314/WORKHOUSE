#!/usr/bin/env python3
"""
fit_stress_test.py

Read a CSV with columns:
    beta, mu_eff, m, m_err (m_err optional)

and run several regression models:
    (1) linear through origin: m = a mu
    (2) affine: m = a mu + b
    (3) power law: m = c mu^p  (fit in log-space; requires mu,m>0)
    (4) sqrt: m = c sqrt(mu)  (through origin)

Outputs:
- a JSON summary with fitted parameters + basic uncertainty estimates (bootstrap).
- plots (residuals, fitted curves).

This is a stress-test scaffold: you supply the expanded dataset.
"""

from __future__ import annotations
import argparse
import json
import math
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, Tuple, Optional

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


@dataclass
class FitResult:
    name: str
    params: Dict[str, float]
    r2: float


def r2_score(y: np.ndarray, yhat: np.ndarray) -> float:
    ss_res = float(np.sum((y - yhat) ** 2))
    ss_tot = float(np.sum((y - float(np.mean(y))) ** 2))
    return 1.0 - ss_res / ss_tot if ss_tot > 0 else float("nan")


def fit_linear_origin(x: np.ndarray, y: np.ndarray) -> Tuple[float, np.ndarray]:
    a = float(np.sum(x * y) / np.sum(x ** 2))
    return a, a * x


def fit_affine(x: np.ndarray, y: np.ndarray) -> Tuple[float, float, np.ndarray]:
    # least squares for [a,b] minimizing ||a x + b - y||^2
    A = np.vstack([x, np.ones_like(x)]).T
    sol, *_ = np.linalg.lstsq(A, y, rcond=None)
    a, b = float(sol[0]), float(sol[1])
    return a, b, a * x + b


def fit_sqrt_origin(x: np.ndarray, y: np.ndarray) -> Tuple[float, np.ndarray]:
    sx = np.sqrt(x)
    c = float(np.sum(sx * y) / np.sum(sx ** 2))
    return c, c * sx


def fit_power(x: np.ndarray, y: np.ndarray) -> Tuple[float, float, np.ndarray]:
    # y = c x^p  => log y = log c + p log x
    if np.any(x <= 0) or np.any(y <= 0):
        raise ValueError("power-law fit requires x>0 and y>0")
    lx = np.log(x)
    ly = np.log(y)
    p, logc = np.polyfit(lx, ly, 1)
    c = float(np.exp(logc))
    yhat = c * (x ** p)
    return c, float(p), yhat


def bootstrap_params(
    x: np.ndarray,
    y: np.ndarray,
    fit_fn,
    B: int = 20000,
    seed: int = 0
) -> Dict[str, Tuple[float, float, float]]:
    """
    Return bootstrap median and 95% interval for each returned parameter.
    fit_fn must return (params_dict, yhat).
    """
    rng = np.random.default_rng(seed)
    params_list = []
    n = len(x)
    for _ in range(B):
        idx = rng.integers(0, n, size=n)
        xb = x[idx]
        yb = y[idx]
        params, _ = fit_fn(xb, yb)
        params_list.append(params)
    # aggregate
    keys = sorted(params_list[0].keys())
    out: Dict[str, Tuple[float,float,float]] = {}
    for k in keys:
        arr = np.array([p[k] for p in params_list], dtype=float)
        lo, med, hi = np.percentile(arr, [2.5, 50, 97.5])
        out[k] = (float(lo), float(med), float(hi))
    return out


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--csv", type=str, required=True)
    ap.add_argument("--outdir", type=str, default="fit_out")
    ap.add_argument("--bootstrap_B", type=int, default=20000)
    ap.add_argument("--seed", type=int, default=0)
    args = ap.parse_args()

    outdir = Path(args.outdir)
    outdir.mkdir(parents=True, exist_ok=True)

    df = pd.read_csv(args.csv)
    x = df["mu_eff"].to_numpy(dtype=float)
    y = df["m"].to_numpy(dtype=float)

    results = []

    # 1) linear through origin
    a, yhat = fit_linear_origin(x, y)
    results.append(FitResult("linear_origin", {"a": a}, r2_score(y, yhat)))

    # 2) affine
    a2, b2, yhat2 = fit_affine(x, y)
    results.append(FitResult("affine", {"a": a2, "b": b2}, r2_score(y, yhat2)))

    # 3) sqrt
    c, yhat3 = fit_sqrt_origin(x, y)
    results.append(FitResult("sqrt_origin", {"c": c}, r2_score(y, yhat3)))

    # 4) power law
    try:
        c4, p4, yhat4 = fit_power(x, y)
        results.append(FitResult("power", {"c": c4, "p": p4}, r2_score(y, yhat4)))
    except ValueError:
        pass

    # bootstrap for linear_origin and affine (as examples)
    def fit_fn_lin(xb, yb):
        a, _ = fit_linear_origin(xb, yb)
        return {"a": a}, None

    def fit_fn_aff(xb, yb):
        a, b, _ = fit_affine(xb, yb)
        return {"a": a, "b": b}, None

    boot = {
        "linear_origin": bootstrap_params(x, y, fit_fn_lin, B=args.bootstrap_B, seed=args.seed),
        "affine": bootstrap_params(x, y, fit_fn_aff, B=args.bootstrap_B, seed=args.seed),
    }

    summary = {
        "n": int(len(x)),
        "fits": [dict(name=r.name, params=r.params, r2=r.r2) for r in results],
        "bootstrap_95": boot,
    }

    (outdir / "fit_summary.json").write_text(json.dumps(summary, indent=2))

    # Plot: fits + residuals
    xx = np.linspace(float(np.min(x)), float(np.max(x)), 200)
    plt.figure()
    plt.scatter(x, y, label="data")
    for r in results:
        if r.name == "linear_origin":
            yy = r.params["a"] * xx
        elif r.name == "affine":
            yy = r.params["a"] * xx + r.params["b"]
        elif r.name == "sqrt_origin":
            yy = r.params["c"] * np.sqrt(xx)
        elif r.name == "power":
            yy = r.params["c"] * (xx ** r.params["p"])
        else:
            continue
        plt.plot(xx, yy, label=r.name)
    plt.xlabel("mu_eff")
    plt.ylabel("m")
    plt.legend()
    plt.savefig(outdir / "fit_curves.png", dpi=200, bbox_inches="tight")

    # Residual plot for the best R2 model
    best = max(results, key=lambda r: (r.r2 if not math.isnan(r.r2) else -1e9))
    if best.name == "linear_origin":
        ybest = best.params["a"] * x
    elif best.name == "affine":
        ybest = best.params["a"] * x + best.params["b"]
    elif best.name == "sqrt_origin":
        ybest = best.params["c"] * np.sqrt(x)
    elif best.name == "power":
        ybest = best.params["c"] * (x ** best.params["p"])
    else:
        ybest = np.full_like(y, np.nan)

    plt.figure()
    plt.scatter(x, y - ybest)
    plt.axhline(0.0)
    plt.xlabel("mu_eff")
    plt.ylabel("residual (m - m_fit)")
    plt.savefig(outdir / "residuals.png", dpi=200, bbox_inches="tight")

    print("Wrote:", outdir / "fit_summary.json")
    print("Wrote:", outdir / "fit_curves.png")
    print("Wrote:", outdir / "residuals.png")


if __name__ == "__main__":
    main()
