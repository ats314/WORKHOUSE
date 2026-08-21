#!/usr/bin/env python3
"""
SU(3) Haar Jacobian Hessian scan in exponential coordinates.

Goal: numerically lower-bound the smallest eigenvalue of the Hessian of
    V_Haar(x) = - log J(x),
where J(x) is the Jacobian determinant of the exponential map exp: su(3) -> SU(3)
in an orthonormal basis.

We implement:
  - A concrete orthonormal anti-Hermitian basis using Gell-Mann matrices.
  - The adjoint representation matrix ad_X in that basis.
  - The Jacobian via eigenvalues of ad_X:
        det(d exp_X) = det( (1 - e^{-ad_X}) / ad_X )
    For skew-symmetric ad_X with eigenvalues ± i θ, the determinant is
        ∏_{eigs} (2 sin(θ/2) / θ),
    and V_Haar = -log(det).

We then compute the full 8x8 Hessian by finite differences and record
  - lambda_min(Hess V_Haar(x))
for random directions at radii r in [0, R0].

Notes:
  - The overall constant depends on basis normalization; we also provide
    a scaling x = s y to match a chosen normalization (e.g. kappa*=0.25).
"""

import math
import numpy as np
import pandas as pd

def gell_mann():
    i = 1j
    lam = []
    lam.append(np.array([[0,1,0],[1,0,0],[0,0,0]],dtype=complex))      # λ1
    lam.append(np.array([[0,-i,0],[i,0,0],[0,0,0]],dtype=complex))     # λ2
    lam.append(np.array([[1,0,0],[0,-1,0],[0,0,0]],dtype=complex))     # λ3
    lam.append(np.array([[0,0,1],[0,0,0],[1,0,0]],dtype=complex))      # λ4
    lam.append(np.array([[0,0,-i],[0,0,0],[i,0,0]],dtype=complex))     # λ5
    lam.append(np.array([[0,0,0],[0,0,1],[0,1,0]],dtype=complex))      # λ6
    lam.append(np.array([[0,0,0],[0,0,-i],[0,i,0]],dtype=complex))     # λ7
    lam.append(np.array([[1/math.sqrt(3),0,0],[0,1/math.sqrt(3),0],[0,0,-2/math.sqrt(3)]],dtype=complex)) # λ8
    return lam

LAM = gell_mann()

# Orthonormal anti-Hermitian basis E_a = i λ_a / sqrt(2) with inner product <A,B> = -Re Tr(A B)
E = [1j * L / math.sqrt(2) for L in LAM]

def inner(A, B):
    return float(np.real(-np.trace(A @ B)))

# sanity: check orthonormality
_G = np.array([[inner(E[a], E[b]) for b in range(8)] for a in range(8)])
if np.max(np.abs(_G - np.eye(8))) > 5e-12:
    raise RuntimeError("Basis not orthonormal; check normalization.")

def su3_from_coords(x):
    X = np.zeros((3,3), dtype=complex)
    for a in range(8):
        X += float(x[a]) * E[a]
    return X

def ad_matrix(x):
    X = su3_from_coords(x)
    A = np.zeros((8,8), dtype=float)
    for b in range(8):
        comm = X @ E[b] - E[b] @ X
        for a in range(8):
            A[a,b] = inner(E[a], comm)
    return A

def logJ_from_ad(A, eps=1e-12):
    # A is real skew-symmetric => eigenvalues ± i θ
    eigs = np.linalg.eigvals(A)
    logJ = 0.0
    for lam in eigs:
        theta = abs(lam.imag)
        if theta < eps:
            continue
        r = 2.0 * math.sin(theta/2.0) / theta
        logJ += math.log(abs(r))
    return logJ

def V_haar(x):
    return -logJ_from_ad(ad_matrix(x))

def hessian_fd(f, x, h=5e-5):
    x = np.array(x, dtype=float)
    n = len(x)
    H = np.zeros((n,n), dtype=float)
    fx = f(x)
    for i in range(n):
        e = np.zeros(n); e[i]=1.0
        fp = f(x + h*e)
        fm = f(x - h*e)
        H[i,i] = (fp - 2*fx + fm) / (h*h)
    for i in range(n):
        for j in range(i+1,n):
            ei = np.zeros(n); ei[i]=1.0
            ej = np.zeros(n); ej[j]=1.0
            fpp = f(x + h*ei + h*ej)
            fpm = f(x + h*ei - h*ej)
            fmp = f(x - h*ei + h*ej)
            fmm = f(x - h*ei - h*ej)
            Hij = (fpp - fpm - fmp + fmm) / (4*h*h)
            H[i,j] = H[j,i] = Hij
    return H

def random_unit_vec(n, rng):
    v = rng.normal(size=n)
    v /= np.linalg.norm(v)
    return v

def scan(R0=0.05, radii=None, Ndir=20, seed=0, h=5e-5, target_kappa=0.25):
    """
    If target_kappa is not None, we apply a coordinate scaling x = s y so that
    Hess(V)(0) has eigenvalue target_kappa at the origin.

    For this basis, Hess(V)(0) ≈ 0.5 I, so s = sqrt(target_kappa / 0.5).
    """
    if radii is None:
        radii = [0.0, 0.01, 0.02, 0.03, 0.04, 0.05]
    rng = np.random.default_rng(seed)

    # origin Hessian to set scale
    H0 = hessian_fd(V_haar, np.zeros(8), h=h)
    lam0 = float(np.linalg.eigvalsh(H0)[0])

    if target_kappa is None:
        s = 1.0
    else:
        s = math.sqrt(target_kappa / lam0)

    def V_scaled(y):
        return V_haar(s*np.array(y))

    rows = []
    for r in radii:
        mins=[]
        maxs=[]
        for k in range(Ndir):
            if r == 0.0:
                y = np.zeros(8)
            else:
                y = r * random_unit_vec(8, rng)
            H = hessian_fd(V_scaled, y, h=h)
            ev = np.linalg.eigvalsh(H)
            mins.append(float(ev[0]))
            maxs.append(float(ev[-1]))
        rows.append({
            "r": r,
            "min_over_dirs": min(mins),
            "mean_min": float(np.mean(mins)),
            "max_over_dirs": max(maxs),
            "Ndir": Ndir,
            "h": h,
            "scale_s": s,
            "origin_min_eig_unscaled": lam0,
            "target_kappa": target_kappa,
        })
    return pd.DataFrame(rows)

if __name__ == "__main__":
    df = scan()
    print(df.to_string(index=False))
