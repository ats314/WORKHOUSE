#!/usr/bin/env python3
"""Haar Hessian scan for SU(3) (toy reproduction).

This script builds ad_X in an orthonormal su(3) basis under <X,Y> = -Tr(XY),
computes the Haar Jacobian term via singular values of ad_X,
and estimates the Hessian by central finite differences.

It is intentionally small and dependency-light (numpy only).
"""
import numpy as np, math
from numpy.linalg import svd, eigvalsh

lam = []
lam.append(np.array([[0,1,0],[1,0,0],[0,0,0]], dtype=complex))
lam.append(np.array([[0,-1j,0],[1j,0,0],[0,0,0]], dtype=complex))
lam.append(np.array([[1,0,0],[0,-1,0],[0,0,0]], dtype=complex))
lam.append(np.array([[0,0,1],[0,0,0],[1,0,0]], dtype=complex))
lam.append(np.array([[0,0,-1j],[0,0,0],[1j,0,0]], dtype=complex))
lam.append(np.array([[0,0,0],[0,0,1],[0,1,0]], dtype=complex))
lam.append(np.array([[0,0,0],[0,0,-1j],[0,1j,0]], dtype=complex))
lam.append((1/math.sqrt(3))*np.array([[1,0,0],[0,1,0],[0,0,-2]], dtype=complex))
lam = np.stack(lam, axis=0)

# Anti-Hermitian orthonormal basis under <X,Y> = -Tr(XY)
T = 1j * lam / math.sqrt(2)

def X_from_x(x):
    return np.tensordot(x, T, axes=(0,0))

def ad_matrix(x):
    X = X_from_x(x)
    comm = X[None,:,:] @ T - T @ X[None,:,:]   # [X, T_b]
    tr = np.einsum('aij,bji->ab', T, comm)     # Tr(T_a [X,T_b])
    return -np.real(tr)

def log_ratio(s):
    if s < 1e-6:
        s2 = s*s
        return s2/24 + 7*s2*s2/5760
    return math.log((s/2)/math.sin(s/2))

def V_haar(x):
    A = ad_matrix(x)
    s = svd(A, compute_uv=False)
    return sum(log_ratio(si) for si in s)

def hessian_fd(f, x, h=5e-4):
    x = np.array(x, dtype=float)
    n = x.size
    H = np.zeros((n,n), dtype=float)
    fx = f(x)
    for i in range(n):
        ei = np.zeros(n); ei[i]=1
        fp = f(x + h*ei); fm = f(x - h*ei)
        H[i,i] = (fp - 2*fx + fm)/(h*h)
    for i in range(n):
        ei = np.zeros(n); ei[i]=1
        for j in range(i+1,n):
            ej = np.zeros(n); ej[j]=1
            fpp = f(x + h*ei + h*ej)
            fpm = f(x + h*ei - h*ej)
            fmp = f(x - h*ei + h*ej)
            fmm = f(x - h*ei - h*ej)
            H[i,j] = (fpp - fpm - fmp + fmm)/(4*h*h)
            H[j,i] = H[i,j]
    return H

def min_eig_hess(x):
    H = hessian_fd(V_haar, x)
    return float(eigvalsh(H)[0])

def scan(radii=(0.0,0.01,0.02,0.03,0.04,0.05), ndir=12, seed=0):
    rng = np.random.default_rng(seed)
    out = []
    for r in radii:
        vals=[]
        for _ in range(ndir):
            u = rng.normal(size=8)
            u = u/np.linalg.norm(u)
            vals.append(min_eig_hess(r*u))
        out.append((r, float(min(vals)), float(np.mean(vals)), float(np.std(vals))))
    return out

if __name__ == "__main__":
    rows = scan()
    for r, mn, mu, sd in rows:
        print(f"r={r:.2f}  min={mn:.9f}  mean={mu:.9f}  std={sd:.3e}")
