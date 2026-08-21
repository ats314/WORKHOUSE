#!/usr/bin/env python3
"""
SAFE eigenvalue scan (tracked, reproducible)

This script reproduces the SU(3) Haar exponential-chart potential

    V_Haar(x) := - log det(dexp_x)

where dexp_x is the left-trivialized derivative of exp at x, expressed in an
orthonormal basis of su(3) (with respect to the chosen inner product).

It then scans the minimum eigenvalue of the Hessian H(x)=∇^2 V_Haar(x)
over random directions on spheres of radius r.

Notes:
- Uses torch autograd to compute Hessians exactly (up to floating-point error).
- For small radii r <= 0.05, the series expansion for phi1 is extremely accurate.
- This script intentionally keeps the Haar piece isolated; to reproduce
  "physical" scans you must specify the *exact* Wilson/cluster/gauge reduction
  used to define H_phys.
"""

from __future__ import annotations
import argparse
import math
from dataclasses import dataclass
from pathlib import Path
from typing import List, Tuple

import numpy as np
import pandas as pd
import torch


DTYPE_R = torch.float64
DTYPE_C = torch.complex128


def gell_mann() -> List[torch.Tensor]:
    """Standard Gell-Mann matrices (Hermitian, Tr(λ_a λ_b)=2 δ_ab)."""
    lam = []
    lam.append(torch.tensor([[0,1,0],[1,0,0],[0,0,0]], dtype=DTYPE_C))                   # λ1
    lam.append(torch.tensor([[0,-1j,0],[1j,0,0],[0,0,0]], dtype=DTYPE_C))                # λ2
    lam.append(torch.tensor([[1,0,0],[0,-1,0],[0,0,0]], dtype=DTYPE_C))                  # λ3
    lam.append(torch.tensor([[0,0,1],[0,0,0],[1,0,0]], dtype=DTYPE_C))                   # λ4
    lam.append(torch.tensor([[0,0,-1j],[0,0,0],[1j,0,0]], dtype=DTYPE_C))                # λ5
    lam.append(torch.tensor([[0,0,0],[0,0,1],[0,1,0]], dtype=DTYPE_C))                   # λ6
    lam.append(torch.tensor([[0,0,0],[0,0,-1j],[0,1j,0]], dtype=DTYPE_C))                # λ7
    lam.append(torch.tensor([[1/math.sqrt(3),0,0],[0,1/math.sqrt(3),0],[0,0,-2/math.sqrt(3)]], dtype=DTYPE_C))  # λ8
    return lam


def build_su3_basis() -> List[torch.Tensor]:
    """
    Anti-Hermitian basis T_a = (i/2) λ_a.

    With inner product <A,B> := -2 Re Tr(A B), this basis is orthonormal.
    """
    lam = gell_mann()
    T = [0.5j * L for L in lam]
    return T


def inner(A: torch.Tensor, B: torch.Tensor) -> torch.Tensor:
    """<A,B> := -2 Re Tr(A B)"""
    return (-2.0 * torch.real(torch.trace(A @ B)))


@dataclass(frozen=True)
class SU3AdjointData:
    """Precomputed structure constants f[a,b,c] in an orthonormal basis."""
    f: torch.Tensor  # shape (8,8,8), real


def precompute_structure_constants() -> SU3AdjointData:
    T = build_su3_basis()
    f = torch.zeros((8,8,8), dtype=DTYPE_R)
    for a in range(8):
        for b in range(8):
            comm = T[a] @ T[b] - T[b] @ T[a]
            for c in range(8):
                f[a,b,c] = inner(comm, T[c]).to(DTYPE_R)
    return SU3AdjointData(f=f)


def ad_matrix(x: torch.Tensor, data: SU3AdjointData) -> torch.Tensor:
    """
    Build the adjoint matrix A(x) with entries A_{c b} such that
        [X, T_b] = sum_c A_{c b} T_c
    for X = sum_a x_a T_a.
    """
    return torch.einsum("a,abc->cb", x, data.f)


def phi1(A: torch.Tensor, order: int = 12) -> torch.Tensor:
    """
    phi1(A) = (exp(A)-I) A^{-1} = sum_{k>=0} A^k / (k+1)!.
    Here we compute the truncated series; for ||A|| small this is extremely accurate.
    """
    n = A.shape[0]
    I = torch.eye(n, dtype=A.dtype, device=A.device)
    term = I.clone()
    out = term / 1.0  # k=0 term: I / 1!
    factorial = 1.0
    for k in range(1, order + 1):
        term = term @ A  # A^k
        factorial *= (k + 1)  # (k+1)!
        out = out + term / factorial
    return out


def haar_potential(x: torch.Tensor, data: SU3AdjointData, series_order: int = 12) -> torch.Tensor:
    """
    V_Haar(x) := -log det(dexp_x), where dexp_x = (I - exp(-ad_x)) ad_x^{-1} = phi1(-ad_x).
    """
    A = ad_matrix(x, data)
    dexp = phi1(-A, order=series_order)
    sign, logabsdet = torch.linalg.slogdet(dexp)
    # In the small SAFE region, sign should be +1.
    return -logabsdet


def hessian_of_scalar(fn, x: torch.Tensor) -> torch.Tensor:
    """Return Hessian of a scalar fn at x using torch autograd."""
    from torch.autograd.functional import hessian
    x = x.clone().detach().requires_grad_(True)
    H = hessian(lambda z: fn(z), x)
    return H.detach()


def min_eigval(H: torch.Tensor) -> float:
    return float(torch.min(torch.linalg.eigvalsh(H)))


def random_unit(d: int, rng: torch.Generator) -> torch.Tensor:
    v = torch.randn(d, dtype=DTYPE_R, generator=rng)
    return v / torch.linalg.norm(v)


def scan(
    radii: List[float],
    n_dir: int,
    seed: int,
    series_order: int,
    out_csv: Path,
    metric_scale: float = 1.0,
) -> pd.DataFrame:
    data = precompute_structure_constants()
    rng = torch.Generator().manual_seed(seed)

    rows = []
    global_min = float("inf")
    global_arg = None

    for r in radii:
        min_r = float("inf")
        for _ in range(n_dir):
            n = random_unit(8, rng)
            x = (r * n).to(DTYPE_R)
            H = hessian_of_scalar(lambda z: haar_potential(metric_scale * z, data, series_order), x)
            lam = min_eigval(H)
            min_r = min(min_r, lam)
            if lam < global_min:
                global_min = lam
                global_arg = (r, x.detach().cpu().numpy().copy())
        rows.append({"r": r, "lambda_min_Haar": min_r})

    df = pd.DataFrame(rows)
    df.to_csv(out_csv, index=False)

    print("GLOBAL MIN eigenvalue:", global_min)
    if global_arg is not None:
        r0, x0 = global_arg
        print("  attained at radius r =", r0)
        print("  direction x =", x0)

    return df


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--radii", type=float, nargs="+", default=[0,0.01,0.02,0.03,0.04,0.05])
    ap.add_argument("--n_dir", type=int, default=64)
    ap.add_argument("--seed", type=int, default=42)
    ap.add_argument("--metric_scale", type=float, default=1.0,
                    help="Scale factor multiplying x before building ad_x (normalization knob)")
    ap.add_argument("--series_order", type=int, default=20)
    ap.add_argument("--outdir", type=str, default=".")
    args = ap.parse_args()

    outdir = Path(args.outdir)
    outdir.mkdir(parents=True, exist_ok=True)

    out_csv = outdir / "safe_scan_results.csv"
    df = scan(
        radii=list(args.radii),
        n_dir=args.n_dir,
        seed=args.seed,
        series_order=args.series_order,
        out_csv=out_csv,
        metric_scale=args.metric_scale,
    )
    print(df)

if __name__ == "__main__":
    main()
