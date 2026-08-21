#!/usr/bin/env python3
"""
ENGINE_TROM_su3_moment_4_1.py  -- EXACT SU(3) Haar moments of type (4,1) and (1,4).

This is the "higher local Haar moment" keystone that the O(y^3/y^4) primitive
layer (ENGINE_FLUX_su3_haar_tromino_primitives.py) deliberately hard-fails on
(UnsupportedMoment for p=4,q=1).  It is required, in denominator-resolved form,
by the Stage-3G multi-path recoupling evaluator of the O(y^4) flat-band program.

METHOD (exact, rational):
  For U in SU(3), det U = 1, so the single Ubar is replaced by two U's via the
  verified cofactor identity
        Ubar_{cd} = (1/2) eps_{d m n} eps_{c p q} U_{p m} U_{q n}.
  This turns the (4,1) moment into a (6,0) moment of six fundamentals, and
        integral over SU(3) of U^{(x)6}  =  P_inv,
  the ORTHOGONAL PROJECTOR onto the SU(3)-invariant subspace of (C^3)^{(x)6}.
  That subspace is spanned by the epsilon-pair tensors eps(triple)*eps(triple);
  its projector is the exact rational matrix  P = A (A^T A)^{-1} A^T  for any
  full-rank choice A of 5 independent epsilon-pair tensors.  No floating point
  enters the exact value.

VERIFICATION: a hard gate compares the exact rationals against an independent
high-precision Haar Monte-Carlo on a panel of index tuples (asserts agreement).
"""
import itertools
from fractions import Fraction as Fr
import numpy as np

# ---- Levi-Civita ----
def _parity(p):
    inv = sum(1 for i in range(len(p)) for j in range(i+1,len(p)) if p[i] > p[j])
    return -1 if inv % 2 else 1
_EPS = {p: _parity(p) for p in itertools.permutations(range(3))}
def eps(i, j, k): return _EPS.get((i, j, k), 0)

# ---- exact (6,0) projector onto SU(3)-invariants in (C^3)^{(x)6} ----
_POS = list(range(6))
_PARTS = []
for _S in itertools.combinations(range(1, 6), 2):           # position 0 fixed in first triple
    _S = (0,) + _S
    _Sc = tuple(x for x in _POS if x not in _S)
    _PARTS.append((_S, _Sc))
_IDX = list(itertools.product(range(3), repeat=6))
_IDXMAP = {t: i for i, t in enumerate(_IDX)}
def _epair(part, t):
    S, Sc = part
    return eps(t[S[0]], t[S[1]], t[S[2]]) * eps(t[Sc[0]], t[Sc[1]], t[Sc[2]])
_Afull = np.zeros((729, 10), dtype=np.int64)
for _c, _part in enumerate(_PARTS):
    for _i, _t in enumerate(_IDX):
        _Afull[_i, _c] = _epair(_part, _t)
_cols = []
for _c in range(10):
    if np.linalg.matrix_rank(_Afull[:, _cols + [_c]]) == len(_cols) + 1:
        _cols.append(_c)
    if len(_cols) == 5: break
_A5 = _Afull[:, _cols]
def _inv_frac(M):
    n = len(M)
    X = [[Fr(M[i][j]) for j in range(n)] + [Fr(int(i == j)) for j in range(n)] for i in range(n)]
    for col in range(n):
        piv = next(r for r in range(col, n) if X[r][col] != 0)
        X[col], X[piv] = X[piv], X[col]
        pv = X[col][col]; X[col] = [x / pv for x in X[col]]
        for r in range(n):
            if r != col and X[r][col] != 0:
                f = X[r][col]; X[r] = [X[r][j] - f * X[col][j] for j in range(2*n)]
    return [row[n:] for row in X]
_G = [[int(np.dot(_A5[:, a], _A5[:, b])) for b in range(5)] for a in range(5)]
_Ginv = _inv_frac(_G)
_A5f = [[Fr(int(_A5[i, a])) for a in range(5)] for i in range(729)]
def _P(i, j):                       # exact rational projector entry
    row = [sum(_A5f[i][a] * _Ginv[a][b] for a in range(5)) for b in range(5)]
    return sum(row[b] * _A5f[j][b] for b in range(5))

def moment_6_0(rows, cols):
    """Exact rational integral over SU(3) of U_{rows[0],cols[0]} ... U_{rows[5],cols[5]}."""
    return _P(_IDXMAP[tuple(rows)], _IDXMAP[tuple(cols)])

def moment_4_1(a, c, b, d):
    """Exact integral of  U_{a0 b0} U_{a1 b1} U_{a2 b2} U_{a3 b3} * conj(U_{c d}).
       a,b : length-4 row/col indices of the four U's; c,d : indices of the one Ubar."""
    tot = Fr(0)
    for m in range(3):
        for n in range(3):
            e1 = eps(d, m, n)
            if not e1: continue
            for p in range(3):
                for q in range(3):
                    e2 = eps(c, p, q)
                    if not e2: continue
                    tot += e1 * e2 * moment_6_0((a[0], a[1], a[2], a[3], p, q),
                                                (b[0], b[1], b[2], b[3], m, n))
    return tot / 2

def moment_1_4(a, b, c, d):
    """Exact integral of  U_{a b} * conj(U_{c0 d0}) ... conj(U_{c3 d3}).
       a,b : the single U; c,d : length-4 indices of the four Ubar.
       Real moment: equals moment_4_1 with U<->Ubar relabelled."""
    return moment_4_1(tuple(c), a, tuple(d), b)

# ---- a few exact reference values ----
REFERENCE = {
    "(6,0) [012|012]x[012|012]": moment_6_0((0,1,2,0,1,2), (0,1,2,0,1,2)),   # 1/18
    "(4,1) a=0120 c=0 b=0120 d=0": moment_4_1((0,1,2,0),0,(0,1,2,0),0),       # 1/12
    "(4,1) a=0012 c=0 b=1021 d=1": moment_4_1((0,0,1,2),0,(1,0,2,1),1),       # -1/24
}

def verify(n_samples=200000, tol=3e-3, seed=20260613):
    """Hard gate: exact rationals must match independent Haar Monte-Carlo."""
    rng = np.random.default_rng(seed)
    def haar():
        z = (rng.normal(size=(3,3)) + 1j*rng.normal(size=(3,3))) / np.sqrt(2)
        q, r = np.linalg.qr(z); ph = np.diag(r)/np.abs(np.diag(r)); q = q*ph.conj()
        return q / np.linalg.det(q)**(1/3)
    U = np.array([haar() for _ in range(n_samples)])
    npass = 0
    panel41 = [((0,1,2,0),0,(0,1,2,0),0), ((0,1,2,1),2,(0,1,2,1),2),
               ((0,0,1,2),0,(1,0,2,1),1), ((0,1,2,2),2,(0,1,2,0),1),
               ((1,2,0,1),0,(0,1,2,2),2), ((0,1,0,2),1,(2,0,1,0),1)]
    print("exact (4,1) vs Haar MC (N=%d):" % n_samples)
    for a,c,b,d in panel41:
        ex = moment_4_1(a,c,b,d)
        v = np.ones(n_samples, dtype=complex)
        for i in range(4): v *= U[:,a[i],b[i]]
        v *= np.conj(U[:,c,d]); mc = v.mean()
        ok = abs(float(ex)-mc.real) < tol and abs(mc.imag) < tol
        assert ok, f"GATE FAIL (4,1) a{a}c{c}b{b}d{d}: exact={ex} mc={mc}"
        npass += 1
        print(f"  GATE PASS  a{a}c{c} b{b}d{d}: exact={str(ex):>6}  MC={mc.real:+.4f}")
    # (1,4) panel (relabelled)
    panel14 = [(0,0,(0,1,2,0),(0,1,2,0)), (1,1,(0,0,1,2),(1,0,2,1))]
    print("exact (1,4) vs Haar MC:")
    for a,b,c,d in panel14:
        ex = moment_1_4(a,b,c,d)
        v = U[:,a,b].astype(complex).copy()
        for i in range(4): v *= np.conj(U[:,c[i],d[i]])
        mc = v.mean()
        ok = abs(float(ex)-mc.real) < tol and abs(mc.imag) < tol
        assert ok, f"GATE FAIL (1,4) a{a}b{b}c{c}d{d}: exact={ex} mc={mc}"
        npass += 1
        print(f"  GATE PASS  a{a}b{b} c{c}d{d}: exact={str(ex):>6}  MC={mc.real:+.4f}")
    print(f"\nALL {npass} EXACT-vs-MC GATES PASSED")

if __name__ == "__main__":
    print("Exact reference SU(3) Haar moments:")
    for k, v in REFERENCE.items():
        print(f"  {k} = {v}")
    print()
    verify()
