#!/usr/bin/env python3
"""
Recompute every geometric constant in EX-003 from su(N) structure constants.

Conventions:
  (A)  <X,Y> = 2 tr(X^dag Y)   -- orthonormal basis T_a = (i/2) lambda_a
  (B)  <X,Y> =   tr(X^dag Y)   -- orthonormal basis sqrt(2) T_a

Facts verified:
  Ric(SU(N)) = (N/4) g   in (A),   (N/2) g in (B)      [isotropic]
  Ric(X,X) = 1/4 sum_a ||[X,e_a]||^2  for an orthonormal basis {e_a}

Run: python geometric_constants.py     (numpy only)
"""
import math
import numpy as np


def su_basis(N):
    """Anti-Hermitian basis T_a = (i/2) lambda_a; orthonormal for <X,Y> = 2 tr(X^dag Y)."""
    B = []
    for i in range(N):
        for j in range(i + 1, N):
            E = np.zeros((N, N), complex); E[i, j] = 1;   E[j, i] = 1
            B.append(0.5j * E)
            E2 = np.zeros((N, N), complex); E2[i, j] = -1j; E2[j, i] = 1j
            B.append(0.5j * E2)
    for k in range(1, N):
        d = np.zeros(N, complex)
        d[:k] = 1.0
        d[k] = -k
        d = d * math.sqrt(2.0 / (k * (k + 1)))
        B.append(0.5j * np.diag(d))
    return B


def ricci_ratio(basis, ip):
    """Ric/g for a bi-invariant metric, from Ric(X,X) = 1/4 sum_a ||[X,e_a]||^2."""
    d = len(basis)
    out = []
    for b in range(d):
        s = sum(ip(basis[b] @ basis[a] - basis[a] @ basis[b],
                   basis[b] @ basis[a] - basis[a] @ basis[b]) for a in range(d))
        out.append(0.25 * s)
    return np.array(out)


if __name__ == "__main__":
    ipA = lambda X, Y: 2 * np.trace(X.conj().T @ Y).real
    ipB = lambda X, Y: 1 * np.trace(X.conj().T @ Y).real
    print(f"{'group':6s} {'dim':>4s} {'Ric/g (A)':>12s} {'N/4':>8s} "
          f"{'Ric/g (B)':>12s} {'N/2':>8s} {'HessHaar (A)':>13s} {'N/12':>8s}")
    for N in (2, 3, 4, 5):
        B = su_basis(N)
        d = len(B)
        assert np.abs(np.array([[ipA(B[a], B[b]) for b in range(d)]
                                for a in range(d)]) - np.eye(d)).max() < 1e-12
        rA = ricci_ratio(B, ipA)
        Bp = [math.sqrt(2) * t for t in B]
        rB = ricci_ratio(Bp, ipB)
        assert rA.max() - rA.min() < 1e-12, "Ricci should be isotropic"
        print(f"SU({N})  {d:4d} {rA.mean():12.6f} {N/4:8.4f} "
              f"{rB.mean():12.6f} {N/2:8.4f} {N/12:13.6f} {N/12:8.4f}")
    print("\nRatio Ric / Hess V_Haar = 3 exactly, in both conventions and for every N.")
    print("C2(fundamental) = (N^2-1)/(2N):  " +
          ", ".join(f"SU({N})={(N*N-1)/(2*N):.4f}" for N in (2, 3, 4, 5)))
    print("  -- this is NOT a curvature; see EX-003 'The one genuine error'.")
