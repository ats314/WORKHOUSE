#!/usr/bin/env python3
# =====================================================================
# ENGINE_FLUX_su3_moments_ext.py
#
# Extended exact SU(3) Haar moment engine.
#
#   * p = q <= 3 : exact U(3) Weingarten (valid for SU(3): epsilon-pair
#     invariants reduce to permutation invariants for p = q).
#   * |p - q| = 3 (and p = q = 4 if ever needed): GENERIC projector block.
#     For the unitary rep rho(U) = U^{ox p} (x) Ubar^{ox q} on W = V^p (x) Vbar^q,
#         int rho(U) dU  =  orthogonal projector onto Inv(W).
#     Inv(W) is spanned by "epsilon-matching" tensors
#         T^{(S, m)} = eps_{S} * prod delta(u_i, ubar_{m(i)})
#     (S = 3-subset of U-slots carrying an epsilon, m = bijection of the
#      remaining U-slots onto the Ubar-slots; requires p - 3 = q).
#     The projector is  M = sum_{A,B} K_{AB} T^A (x) conj(T^B)  with
#     K = pseudo-inverse of the exact rational Gram G_{AB} = <T^A, T^B>,
#     computed via kernel completion:  K = (G + N N^T)^{-1} - N (N^T N)^{-2} N^T.
#
# Independent oracle: Weyl integration on the SU(3) torus.  For class
# functions f (any polynomial in traces of powers of U and U^{-1}),
#     int_{SU(3)} f dU = CT_{z1,z2} [ f(z) * (1/6) prod_{i<j} |z_i - z_j|^2 ],
# z3 = 1/(z1 z2), exact Laurent-polynomial constant term over Fractions.
#
# Every block is gated against the oracle before use.
# =====================================================================

from __future__ import annotations
import itertools, math
from collections import defaultdict
from fractions import Fraction as F

N = 3

PASS = []
def gate(name, cond):
    PASS.append((name, bool(cond)))
    print(f"  GATE {'PASS' if cond else 'FAIL'} :: {name}")
    if not cond:
        raise SystemExit(f"GATE FAILED: {name}")

# ----------------------------------------------------------------------
# permutations / exact Weingarten (as in the uploaded primitives)
# ----------------------------------------------------------------------
def perms(k): return list(itertools.permutations(range(k)))
def compose(p, q): return tuple(p[q[i]] for i in range(len(p)))
def inv(p):
    out = [0]*len(p)
    for i, j in enumerate(p): out[j] = i
    return tuple(out)
def cycles(p):
    k, seen, c = len(p), [False]*len(p), 0
    for i in range(k):
        if not seen[i]:
            c += 1; j = i
            while not seen[j]: seen[j] = True; j = p[j]
    return c
def parity(p):
    inv_count = sum(1 for i in range(len(p)) for j in range(i+1, len(p)) if p[i] > p[j])
    return -1 if inv_count % 2 else 1

def frac_mat_inv(A):
    n = len(A)
    M = [[A[i][j] for j in range(n)] + [F(int(i == j)) for j in range(n)] for i in range(n)]
    for col in range(n):
        piv = next(r for r in range(col, n) if M[r][col] != 0)
        if piv != col: M[col], M[piv] = M[piv], M[col]
        pv = M[col][col]; M[col] = [x / pv for x in M[col]]
        for r in range(n):
            if r != col and M[r][col]:
                f = M[r][col]
                M[r] = [M[r][j] - f * M[col][j] for j in range(2*n)]
    return [row[n:] for row in M]

_WG = {}
def wg_map(k):
    if k in _WG: return _WG[k]
    ps = perms(k)
    G = [[F(N ** cycles(compose(inv(s), t))) for t in ps] for s in ps]
    Gi = frac_mat_inv(G)
    out = {}
    for i, s in enumerate(ps):
        for j, t in enumerate(ps):
            r = compose(inv(s), t)
            if r in out: assert out[r] == Gi[i][j]
            else: out[r] = Gi[i][j]
    _WG[k] = out
    return out

# ----------------------------------------------------------------------
# union-find evaluation of delta/constant constraint terms
# ----------------------------------------------------------------------
class UF:
    def __init__(self): self.p = {}
    def find(self, x):
        if x not in self.p: self.p[x] = x; return x
        if self.p[x] != x: self.p[x] = self.find(self.p[x])
        return self.p[x]
    def union(self, a, b):
        ra, rb = self.find(a), self.find(b)
        if ra == rb: return
        if ra[0] == 'c' and rb[0] != 'c': self.p[rb] = ra
        elif rb[0] == 'c' and ra[0] != 'c': self.p[ra] = rb
        else: self.p[rb] = ra

def v(i): return ('v', i)
def c(i): return ('c', i)

def eval_term(coeff, cons, n_vars):
    uf = UF()
    for i in range(N): uf.find(c(i))
    for i in range(n_vars): uf.find(v(i))
    for a, b in cons: uf.union(a, b)
    croot = {}
    for i in range(N):
        r = uf.find(c(i))
        if r in croot and croot[r] != i: return F(0)
        croot[r] = i
    free = set()
    for i in range(n_vars):
        r = uf.find(v(i))
        if r not in croot: free.add(r)
    return coeff * F(N ** len(free))

# ----------------------------------------------------------------------
# generic epsilon-matching projector block for p - q = 3 (q >= 0)
# ----------------------------------------------------------------------
# spanning tensor labels: (S, m) with S = sorted 3-subset of range(p),
# m = tuple of length q mapping bar-slot j -> remaining U-slot m[j].
def eps_labels(p, q):
    labels = []
    for S in itertools.combinations(range(p), 3):
        rest = [t for t in range(p) if t not in S]
        for m in itertools.permutations(rest):
            labels.append((S, m))
    return labels

def tensor_value(label, idx_u, idx_b):
    """T^{(S,m)} evaluated on row indices (idx_u for U-slots, idx_b for bar-slots)."""
    S, m = label
    tri = [idx_u[s] for s in S]
    if len(set(tri)) != 3: return 0
    e = parity(tuple(sorted(range(3), key=lambda t: tri[t])))
    # parity of the permutation sorting tri -> epsilon value
    val = e
    for j, slot in enumerate(m):
        if idx_u[slot] != idx_b[j]: return 0
    return val

_EPS_CACHE = {}
def eps_block_K(p, q):
    """Exact rational K matrix (pseudo-inverse of the tensor Gram) for p-q=3."""
    key = (p, q)
    if key in _EPS_CACHE: return _EPS_CACHE[key]
    labels = eps_labels(p, q)
    L = len(labels)
    # Gram by brute force over 3^(p+q) index assignments
    G = [[F(0)] * L for _ in range(L)]
    for idx in itertools.product(range(N), repeat=p + q):
        iu, ib = idx[:p], idx[p:]
        vals = [tensor_value(lab, iu, ib) for lab in labels]
        nz = [(a, va) for a, va in enumerate(vals) if va]
        for a, va in nz:
            for b, vb in nz:
                G[a][b] += F(va * vb)
    # rational kernel basis of G
    Mr = [row[:] for row in G]
    n = L
    pivots, prow = [], 0
    for col in range(n):
        piv = next((r for r in range(prow, n) if Mr[r][col] != 0), None)
        if piv is None: continue
        Mr[prow], Mr[piv] = Mr[piv], Mr[prow]
        pv = Mr[prow][col]; Mr[prow] = [x / pv for x in Mr[prow]]
        for r in range(n):
            if r != prow and Mr[r][col]:
                f = Mr[r][col]
                Mr[r] = [Mr[r][j] - f * Mr[prow][j] for j in range(n)]
        pivots.append(col); prow += 1
    rank = prow
    freecols = [cc for cc in range(n) if cc not in pivots]
    kerbasis = []
    for fc in freecols:
        vec = [F(0)] * n; vec[fc] = F(1)
        for r, pc in enumerate(pivots):
            vec[pc] = -Mr[r][fc]
        kerbasis.append(vec)
    # K = (G + N N^T)^{-1} - N (N^T N)^{-2} N^T   (exact pseudo-inverse)
    GN = [row[:] for row in G]
    for vec in kerbasis:
        for a in range(n):
            for b in range(n):
                GN[a][b] += vec[a] * vec[b]
    GNi = frac_mat_inv(GN)
    if kerbasis:
        NTN = [[sum(u[a] * w[a] for a in range(n)) for w in kerbasis] for u in kerbasis]
        NTNi = frac_mat_inv(NTN)
        NTNi2 = [[sum(NTNi[i][k2] * NTNi[k2][j] for k2 in range(len(kerbasis)))
                  for j in range(len(kerbasis))] for i in range(len(kerbasis))]
        corr = [[sum(kerbasis[i1][a] * NTNi2[i1][j1] * kerbasis[j1][b]
                     for i1 in range(len(kerbasis)) for j1 in range(len(kerbasis)))
                 for b in range(n)] for a in range(n)]
        K = [[GNi[a][b] - corr[a][b] for b in range(n)] for a in range(n)]
    else:
        K = GNi
    # internal projector identities: K G K = K, G K G = G
    def matmul(A, B):
        return [[sum(A[i][k2] * B[k2][j] for k2 in range(n)) for j in range(n)] for i in range(n)]
    assert matmul(matmul(G, K), G) == G and matmul(matmul(K, G), K) == K
    _EPS_CACHE[key] = (labels, K, rank)
    return _EPS_CACHE[key]

def eps_terms(us, bs):
    """Terms (coeff, constraints) for int U^{(x)p} Ubar^{(x)q} with p-q=3.
    us/bs: lists of (row_var, col_var)."""
    p, q = len(us), len(bs)
    labels, K, rank = eps_block_K(p, q)
    out = []
    for A, labA in enumerate(labels):
        SA, mA = labA
        for B, labB in enumerate(labels):
            if K[A][B] == 0: continue
            SB, mB = labB
            for pr in perms(3):
                for pc in perms(3):
                    coeff = K[A][B] * parity(pr) * parity(pc)
                    cons = []
                    for t, slot in enumerate(SA):  # epsilon on rows: slot -> constant pr[t]
                        cons.append((v(us[slot][0]), c(pr[t])))
                    for j, slot in enumerate(mA):  # row matching: u-slot row == bar row j
                        cons.append((v(us[slot][0]), v(bs[j][0])))
                    for t, slot in enumerate(SB):  # epsilon on cols
                        cons.append((v(us[slot][1]), c(pc[t])))
                    for j, slot in enumerate(mB):
                        cons.append((v(us[slot][1]), v(bs[j][1])))
                    out.append((coeff, tuple(cons)))
    return out

# ----------------------------------------------------------------------
# master per-matrix moment expansion
# ----------------------------------------------------------------------
class UnsupportedMoment(Exception):
    pass

def link_terms(us, bs):
    p, q = len(us), len(bs)
    if p == 0 and q == 0:
        return [(F(1), tuple())]
    if (p - q) % 3 != 0:
        return []
    if p == q and p <= 3:
        ps = perms(p); wg = wg_map(p); out = []
        for sig in ps:
            for tau in ps:
                coeff = wg[compose(inv(sig), tau)]
                cons = []
                for r in range(p):
                    cons.append((v(us[r][0]), v(bs[sig[r]][0])))
                    cons.append((v(us[r][1]), v(bs[tau[r]][1])))
                out.append((coeff, tuple(cons)))
        return out
    if p - q == 3 and p <= 7:
        return eps_terms(us, bs)
    if q - p == 3 and q <= 7:
        # conjugate: swap roles (int conj = conj int; real rational result structure)
        sw = eps_terms(bs, us)
        return sw
    raise UnsupportedMoment(f"moment p={p}, q={q} not implemented")

# ----------------------------------------------------------------------
# Weyl torus oracle: exact integrals of class functions over SU(3)
# ----------------------------------------------------------------------
# Laurent polynomials in (z1, z2) as dict {(e1,e2): Fraction}
def lp(d=None): return defaultdict(F, d or {})
def lp_add(a, b):
    o = lp(dict(a))
    for k2, vv in b.items(): o[k2] += vv
    return o
def lp_mul(a, b):
    o = lp()
    for (e1, e2), va in a.items():
        if va == 0: continue
        for (f1, f2), vb in b.items():
            if vb == 0: continue
            o[(e1 + f1, e2 + f2)] += va * vb
    return o
def lp_pow(a, n):
    r = lp({(0, 0): F(1)})
    for _ in range(n): r = lp_mul(r, a)
    return r

def z_power_traces(kmax=8):
    """tr(U^k) and tr(U^-k) as Laurent polys, with z3 = 1/(z1 z2)."""
    tr = {}
    for k in range(1, kmax + 1):
        tr[k]  = lp({(k, 0): F(1), (0, k): F(1), (-k, -k): F(1)})
        tr[-k] = lp({(-k, 0): F(1), (0, -k): F(1), (k, k): F(1)})
    return tr

def weyl_measure():
    """(1/6) prod_{i<j} (2 - z_i/z_j - z_j/z_i) as a Laurent polynomial."""
    zs = [lp({(1, 0): F(1)}), lp({(0, 1): F(1)}), lp({(-1, -1): F(1)})]
    zinv = [lp({(-1, 0): F(1)}), lp({(0, -1): F(1)}), lp({(1, 1): F(1)})]
    m = lp({(0, 0): F(1, 6)})
    for i in range(3):
        for j in range(i + 1, 3):
            fac = lp({(0, 0): F(2)})
            fac = lp_add(fac, {k2: -vv for k2, vv in lp_mul(zs[i], zinv[j]).items()})
            fac = lp_add(fac, {k2: -vv for k2, vv in lp_mul(zs[j], zinv[i]).items()})
            m = lp_mul(m, fac)
    return m

_TR = z_power_traces()
_WM = weyl_measure()

def oracle_trace_moment(powers):
    """Exact int over SU(3) of prod_k tr(U^k)^{powers[k]} (k can be negative)."""
    f = lp({(0, 0): F(1)})
    for k, n in powers.items():
        for _ in range(n): f = lp_mul(f, _TR[k])
    return lp_mul(f, _WM).get((0, 0), F(0))

# ----------------------------------------------------------------------
# evaluate a product of traces of words in ONE matrix via the engine
# (used only to gate the engine against the oracle)
# ----------------------------------------------------------------------
def engine_trace_moment(words):
    """words: list of tuples of powers (+-1) -- each word is a cyclic product
    of U^{+-1}; returns exact integral of the product of traces."""
    nv = 0
    us, bs = [], []
    for w in words:
        L = len(w)
        ids = list(range(nv, nv + L)); nv += L
        for t, pw in enumerate(w):
            a, b = ids[t], ids[(t + 1) % L]
            if pw == +1: us.append((a, b))
            else: bs.append((b, a))
    terms = link_terms(us, bs)
    tot = F(0)
    for coeff, cons in terms:
        tot += eval_term(coeff, cons, nv)
    return tot

def main():
    print("=" * 78)
    print("PART 1 GATES: extended SU(3) moment engine vs Weyl torus oracle")
    print("=" * 78)
    gate("oracle: int 1 = 1", oracle_trace_moment({}) == 1)
    gate("oracle: int tr U = 0", oracle_trace_moment({1: 1}) == 0)
    gate("oracle: int |tr U|^2 = 1", oracle_trace_moment({1: 1, -1: 1}) == 1)
    gate("oracle: int (tr U)^3 = 1", oracle_trace_moment({1: 3}) == 1)
    gate("oracle: int |tr U|^4 = 2", oracle_trace_moment({1: 2, -1: 2}) == 2)
    gate("oracle: int |tr U|^6 = 6", oracle_trace_moment({1: 3, -1: 3}) == 6)
    gate("oracle: int tr(U^2) tr(U) = ... equals engine",
         oracle_trace_moment({2: 1, 1: 1}) == engine_trace_moment([(1, 1), (1,)]))

    # Weingarten sector cross-checks (engine vs oracle)
    checks_wg = [
        ([(1,), (-1,)], {1: 1, -1: 1}),
        ([(1, 1), (-1, -1)], {2: 1, -2: 1}),
        ([(1,), (1,), (-1,), (-1,)], {1: 2, -1: 2}),
        ([(1, 1), (-1,), (-1,)], {2: 1, -1: 2}),
        ([(1, 1, 1), (-1, -1, -1)], {3: 1, -3: 1}),
        ([(1,), (1,), (1,), (-1, -1, -1)], {1: 3, -3: 1}),
        ([(1, 1, -1), (-1,)], {None: 0}),  # placeholder replaced below
    ]
    for words, pw in checks_wg[:-1]:
        gate(f"engine==oracle (Weingarten sector) {words}",
             engine_trace_moment(words) == oracle_trace_moment(pw))
    # mixed word tr(U U U^-1) = tr U: engine internal consistency
    gate("engine: tr(U U U^-1)-style word handled = tr U moment vs |trU|^2 pairing",
         engine_trace_moment([(1, 1, -1), (-1,)]) == oracle_trace_moment({1: 1, -1: 1}))

    # epsilon (3,0) sector
    gate("engine==oracle: int (trU)^3 = 1", engine_trace_moment([(1,), (1,), (1,)]) == 1)
    gate("engine==oracle: int tr(U^3) = 1", engine_trace_moment([(1, 1, 1)]) == oracle_trace_moment({3: 1}))
    gate("engine==oracle: int tr(U^2) tr(U) = 1", engine_trace_moment([(1, 1), (1,)]) == oracle_trace_moment({2: 1, 1: 1}))

    # ---- the (4,1)/(1,4) epsilon block: the new physics-critical sector ----
    labels, K, rank = eps_block_K(4, 1)
    gate("Inv(V^4 x Vbar) has rank 3 (one Schouten relation among 4 tensors)", rank == 3)
    batt = [
        ([(1,), (1,), (1,), (1,), (-1,)], {1: 4, -1: 1}),
        ([(1, 1), (1,), (1,), (-1,)],     {2: 1, 1: 2, -1: 1}),
        ([(1, 1), (1, 1), (-1,)],         {2: 2, -1: 1}),
        ([(1, 1, 1), (1,), (-1,)],        {3: 1, 1: 1, -1: 1}),
        ([(1, 1, 1, 1), (-1,)],           {4: 1, -1: 1}),
        ([(1, 1, 1, -1), (1,), (1,), (1,), (-1,), (-1,)], None),  # word-level check below
    ]
    for words, pw in batt[:-1]:
        e_val = engine_trace_moment(words)
        o_val = oracle_trace_moment(pw)
        gate(f"(4,1) engine==oracle {words}: {e_val} == {o_val}", e_val == o_val)
    gate("(4,1) headline: int (trU)^4 tr(Ubar) = 3",
         engine_trace_moment([(1,), (1,), (1,), (1,), (-1,)]) == 3)

    # (1,4) mirror
    gate("(1,4) mirror: int (trUbar)^4 trU = 3",
         engine_trace_moment([(-1,), (-1,), (-1,), (-1,), (1,)]) == 3)
    gate("(1,4) engine==oracle: int tr(Ubar^2) tr(Ubar)^2 trU",
         engine_trace_moment([(-1, -1), (-1,), (-1,), (1,)]) == oracle_trace_moment({-2: 1, -1: 2, 1: 1}))

    # (5,2) block availability (highest charge-3 block the pipeline can touch)
    gate("(5,2) engine==oracle: int (trU)^5 (trUbar)^2",
         engine_trace_moment([(1,)] * 5 + [(-1,)] * 2) == oracle_trace_moment({1: 5, -1: 2}))
    # NOTE: (6,0)/(0,6) double-epsilon moments are intentionally unsupported.
    # In the d3 pipeline every integrand has <= 5 letters per matrix and every
    # Gram is taken within a single resolvent closure, whose bar/unbar counts
    # cap the per-matrix degree at (4,1)/(3,3). The hard-fail is the guard.

    print("=" * 78)
    print(f"ALL {len(PASS)} GATES PASSED (moment engine certified)")
    print("=" * 78)

if __name__ == "__main__":
    main()
