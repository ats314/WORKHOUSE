#!/usr/bin/env python3
"""
Independent verification of  Hess V_Haar(0) = (N/12) * I  for SU(N).

V_Haar(X) = -log det( dexp_X ),   dexp_X = (1 - e^{-ad_X}) / ad_X

Basis:  T_a = (i/2) lambda_a,  orthonormal for <X,Y> = 2 tr(X^dag Y).

Two implementation notes that matter:
  * f(z) = (1-e^{-z})/z is evaluated by its ENTIRE power series
    f(A) = sum_k (-A)^k / (k+1)!  --  this avoids both the removable
    singularity at z=0 and the degenerate eigendecomposition of ad_X at X=0
    (all eigenvalues coincide there, so eigenvalue-based routines fail to
    converge and are not differentiable).
  * float64 throughout; the Hessian is taken with torch autograd.

Expected output: min eig = max eig = N/12 for every N (isotropy).

    SU(2) 0.166666667   SU(3) 0.250000000   SU(4) 0.333333333   SU(5) 0.416666667

Run:  python haar_hessian_check.py
Requires: torch, numpy
"""
import math

import numpy as np
import torch

torch.set_default_dtype(torch.float64)


def su_basis(N):
    """Orthonormal anti-Hermitian basis of su(N) for <X,Y> = 2 tr(X^dag Y)."""
    B = []
    for i in range(N):
        for j in range(i + 1, N):
            E = torch.zeros(N, N, dtype=torch.complex128)
            E[i, j] = 1
            E[j, i] = 1
            B.append(0.5j * E)
            E2 = torch.zeros(N, N, dtype=torch.complex128)
            E2[i, j] = -1j
            E2[j, i] = 1j
            B.append(0.5j * E2)
    for k in range(1, N):
        dg = torch.zeros(N, dtype=torch.complex128)
        for m in range(k):
            dg[m] = 1.0
        dg[k] = -k
        dg = dg * math.sqrt(2.0 / (k * (k + 1)))
        B.append(0.5j * torch.diag(dg))
    return B


def V_haar(x, B, K=16):
    """-log det f(ad_X) with f(A) = sum_k (-A)^k/(k+1)!, X = sum_a x_a T_a."""
    d = len(B)
    X = sum(x[a] * B[a] for a in range(d))
    cols = []
    for b in range(d):
        C = X @ B[b] - B[b] @ X                      # ad_X(T_b)
        cols.append(torch.stack([2 * torch.trace(B[a].conj().T @ C).real
                                 for a in range(d)]))
    A = torch.stack(cols, dim=1)                     # ad_X in the basis (real)

    F = torch.eye(d)
    P = torch.eye(d)
    for k in range(1, K):
        P = P @ (-A)
        F = F + P / float(math.factorial(k + 1))
    return -torch.linalg.slogdet(F).logabsdet


if __name__ == "__main__":
    for N in (2, 3, 4, 5):
        B = su_basis(N)
        d = len(B)
        gram = np.array([[complex(2 * torch.trace(B[a].conj().T @ B[b]))
                          for b in range(d)] for a in range(d)])
        x = torch.zeros(d, requires_grad=True)
        H = torch.autograd.functional.hessian(lambda v: V_haar(v, B), x).detach().numpy()
        H = (H + H.T) / 2
        ev = np.linalg.eigvalsh(H)
        print(f"SU({N}) dim={d:2d}  gram_err={np.abs(gram - np.eye(d)).max():.1e}  "
              f"Hess eig min={ev.min():.9f} max={ev.max():.9f}   N/12={N/12:.9f}")
