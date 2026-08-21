#!/usr/bin/env python3
# =====================================================================
# ENGINE_FLUX_su3_domino_d3.py
#
# Exact O(y^3) degenerate perturbation theory on the ABSTRACT DOMINO:
# two independent SU(3) Haar matrices (g1, g2) = the two plaquette
# holonomies of a shared-link pair, gauge-reduced.  Conjugation-invariant
# wavefunctions are rational combinations of products of traces of words
# in (g1, g2).
#
#   H0 = 2*Cas(1) + 2*Cas(2) + cross(s),   cross(s) = -sum_a D_a^(1) D_a^(2)
#
# with D^(1) the right-translation derivative on g1 and D^(2) the
# right-translation derivative on g2 for shared-link sign s=+1, or the
# (minus) left-translation derivative for s=-1.  All derivations are
# implemented as exact Fierz surgery on trace words; SU(3) Cayley-
# Hamilton rewrites (g^2 = chi g - chibar + g^{-1}) keep every function
# in a canonical alternating-word basis of total letter degree <= 4.
#
#   V = -y W,  W = chi1 + chibar1 + chi2 + chibar2  (domino)
#                  chi1 + chibar1                   (single plaquette)
#
# des Cloizeaux to third order on the degenerate manifold:
#   H(1) = -PWP
#   H(2) = +P W R W P
#   H(3) = -P W R W R W P + (1/2){ P W R^2 W P , P W P }
# R = Q (E0 - H0)^{-1} Q implemented by exact rational linear solves on
# the H0-closure of each vector, with per-solve gates:
#   * coefficient-level residual == 0  (=> function identity),
#   * manifold overlaps of the solution == 0,
#   * every kernel vector of the stacked system is the ZERO FUNCTION
#     (Gram norm == 0), so R is well defined.
#
# Cross-validation: a fully independent single-plaquette spectral
# implementation (irrep basis via exact Schur characters on the Weyl
# torus, Jacobi-Trudi) must reproduce the strong-coupling Bridge towers
#   gap_2 = {13/20, 1/2},  gap_3 = {101/200, 7/32}
# and must agree entrywise with the word-calculus single plaquette.
#
# Output: exact rational d3 (third-order coefficient of the C-odd flat
# band), the O(y^3) extension of the C-even channel, and the corrected
# O(y^2) C-even hopping (vacuum-route term).
# =====================================================================

from __future__ import annotations
import json, itertools
from fractions import Fraction as F
from ENGINE_FLUX_su3_moments_ext import (link_terms, eval_term, v, perms, parity,
                             lp, lp_add, lp_mul, _WM, frac_mat_inv)

# ------------------------------------------------------------------
# gates
# ------------------------------------------------------------------
GATES = []
def gate(name, cond):
    GATES.append((name, bool(cond)))
    print(f"  GATE {'PASS' if cond else 'FAIL'} :: {name}")
    if not cond:
        raise SystemExit(f"GATE FAILED: {name}")

# ==================================================================
# SECTION A: canonical word / monomial / expression calculus
# ==================================================================
# letter = (gen, pow), gen in {1,2}, pow in {+1,-1}
# word   = tuple of letters (one trace, cyclic)
# monomial = sorted tuple of words (product of traces); () = constant 1
# expr   = dict {monomial: Fraction}

def _cyc_reduce(word):
    w = list(word)
    changed = True
    while changed and w:
        changed = False
        L = len(w)
        for i in range(L):
            j = (i + 1) % L
            if L >= 2 and w[i][0] == w[j][0] and w[i][1] == -w[j][1]:
                if j > i:
                    w = w[:i] + w[j+1:]
                else:  # wrap pair (last, first)
                    w = w[1:-1]
                changed = True
                break
    return tuple(w)

def _min_rotation(word):
    if not word: return word
    L = len(word)
    return min(tuple(word[i:] + word[:i]) for i in range(L))

def canon_word(word):
    """Canonicalize one trace word; returns expr {monomial: coeff}."""
    w = _cyc_reduce(word)
    if not w:
        return {(): F(3)}        # Tr(identity) = 3
    L = len(w)
    # find cyclically adjacent same-gen same-pow pair -> Cayley-Hamilton
    for i in range(L):
        j = (i + 1) % L
        if L >= 2 and w[i] == w[j]:
            gen, pw = w[i]
            # rotate so pair occupies the last two slots
            rot = w[(j+1) % L:] + w[:(j+1) % L] if j == (i+1) % L else None
            alpha = (w[j+1:] + w[:i]) if j > i else w[1:-1]
            out = {}
            if pw == +1:
                # Tr(alpha g g) = chi*Tr(alpha g) - chibar*Tr(alpha) + Tr(alpha g^-1)
                pieces = [ (F(1), ((gen, +1),), alpha + ((gen, +1),)),  # placeholder unused
                ]
                t1 = canon_word(alpha + ((gen, +1),))
                t2 = canon_word(alpha)
                t3 = canon_word(alpha + ((gen, -1),))
                chi    = ((gen, +1),)
                chibar = ((gen, -1),)
                for m, cf in t1.items():
                    mm = tuple(sorted(m + (chi,)))
                    out[mm] = out.get(mm, F(0)) + cf
                for m, cf in t2.items():
                    mm = tuple(sorted(m + (chibar,)))
                    out[mm] = out.get(mm, F(0)) - cf
                for m, cf in t3.items():
                    out[m] = out.get(m, F(0)) + cf
            else:
                # Tr(alpha g^-2) = chibar*Tr(alpha g^-1) - chi*Tr(alpha) + Tr(alpha g)
                t1 = canon_word(alpha + ((gen, -1),))
                t2 = canon_word(alpha)
                t3 = canon_word(alpha + ((gen, +1),))
                chi    = ((gen, +1),)
                chibar = ((gen, -1),)
                for m, cf in t1.items():
                    mm = tuple(sorted(m + (chibar,)))
                    out[mm] = out.get(mm, F(0)) + cf
                for m, cf in t2.items():
                    mm = tuple(sorted(m + (chi,)))
                    out[mm] = out.get(mm, F(0)) - cf
                for m, cf in t3.items():
                    out[m] = out.get(m, F(0)) + cf
            return {m: cf for m, cf in out.items() if cf != 0}
    return {(_min_rotation(w),): F(1)}

def expr_add(a, b, sb=F(1)):
    o = dict(a)
    for m, cf in b.items():
        o[m] = o.get(m, F(0)) + sb * cf
        if o[m] == 0: del o[m]
    return o

def expr_scale(a, s):
    if s == 0: return {}
    return {m: cf * s for m, cf in a.items()}

def mono_mul(m1, m2):
    return tuple(sorted(m1 + m2))

def expr_mul(a, b):
    o = {}
    for m1, c1 in a.items():
        for m2, c2 in b.items():
            mm = mono_mul(m1, m2)
            o[mm] = o.get(mm, F(0)) + c1 * c2
    return {m: cf for m, cf in o.items() if cf != 0}

def canon_monomial_expr(words, coeff=F(1)):
    """Product of (possibly non-canonical) words -> canonical expr."""
    out = {(): coeff}
    for w in words:
        out = expr_mul(out, canon_word(w))
    return out

def conj_expr(a):
    o = {}
    for m, cf in a.items():
        words = []
        for w in m:
            words.append(tuple((g, -p) for (g, p) in reversed(w)))
        ce = canon_monomial_expr(tuple(words), cf)
        o = expr_add(o, ce)
    return o

def mul_char(expr, gen, pw):
    o = {}
    w = ((gen, pw),)
    for m, cf in expr.items():
        mm = mono_mul(m, (w,))
        o[mm] = o.get(mm, F(0)) + cf
    return o

def apply_W(expr, chars):
    o = {}
    for (gen, pw) in chars:
        o = expr_add(o, mul_char(expr, gen, pw))
    return o

# ==================================================================
# SECTION B: exact Haar integration of canonical monomials
# ==================================================================
_INT_CACHE = {}
def integrate_monomial(m):
    if m in _INT_CACHE: return _INT_CACHE[m]
    nv = 0
    us = {1: [], 2: []}
    bs = {1: [], 2: []}
    for w in m:
        L = len(w)
        ids = list(range(nv, nv + L)); nv += L
        for t, (gen, pw) in enumerate(w):
            a, b = ids[t], ids[(t + 1) % L]
            if pw == +1: us[gen].append((a, b))
            else:        bs[gen].append((b, a))
    t1 = link_terms(us[1], bs[1])
    t2 = link_terms(us[2], bs[2])
    tot = F(0)
    for c1, k1 in t1:
        for c2, k2 in t2:
            tot += eval_term(c1 * c2, k1 + k2, nv)
    _INT_CACHE[m] = tot
    return tot

def integrate_expr(e):
    return sum((cf * integrate_monomial(m) for m, cf in e.items()), F(0))

def inner(a, b):
    """<a|b> = int conj(a) * b."""
    return integrate_expr(expr_mul(conj_expr(a), b))

# ==================================================================
# SECTION C: H0 as exact Fierz surgery
# ==================================================================
def _occurrences(m, gen):
    occ = []
    for wi, w in enumerate(m):
        for t, (g, p) in enumerate(w):
            if g == gen:
                occ.append((wi, t, p))
    return occ

def _ins_data(p, mode):
    """(cut_offset, suborder, eta) for an insertion on a letter of power p.
    mode 'R': standard right-derivative; mode 'L': left-derivative w/ minus
    (used for generator 2 when s = -1).  cut: 'after' -> cut at t+1, sub 0;
    'before' -> cut at t, sub 1."""
    if mode == 'R':
        return ('after', 0, +1) if p == +1 else ('before', 1, -1)
    else:  # 'L'
        return ('before', 1, -1) if p == +1 else ('after', 0, +1)

def _open_at(word, cut):
    """linear word starting at letter index `cut` (mod L) going around."""
    L = len(word)
    cut %= L
    return word[cut:] + word[:cut]

def pair_fierz(m, ins_x, ins_y):
    """Sigma_a (T_a at ins_x)(T_a at ins_y) acting on monomial m.
    ins = (word_idx, cut, sub).  Returns expr (eta signs NOT included)."""
    (wx, cx, sx), (wy, cy, sy) = ins_x, ins_y
    words = list(m)
    if wx != wy:
        A, B = words[wx], words[wy]
        rest = tuple(w for i, w in enumerate(words) if i not in (wx, wy))
        alpha = _open_at(A, cx)
        beta  = _open_at(B, cy)
        # 1/2 [ Tr(alpha beta) - 1/3 TrA TrB ]
        e1 = canon_monomial_expr(rest + (alpha + beta,), F(1, 2))
        e2 = canon_monomial_expr(rest + (A, B), F(-1, 6))
        return expr_add(e1, e2)
    else:
        Wd = words[wx]
        rest = tuple(w for i, w in enumerate(words) if i != wx)
        L = len(Wd)
        cx_, cy_ = cx % L, cy % L
        # order the two insertions around the cycle: (cut, sub)
        if (cx_, sx) <= (cy_, sy):
            c1, c2 = cx_, cy_
        else:
            c1, c2 = cy_, cx_
        # arcs: beta = letters c1..c2-1, gamma = c2..c1-1 (cyclic)
        if c1 == c2:
            beta = tuple()
            gamma = _open_at(Wd, c1)
        else:
            beta  = tuple(Wd[i % L] for i in range(c1, c2 if c2 > c1 else c2 + L))
            gamma = tuple(Wd[i % L] for i in range(c2, c1 + L))
        # 1/2 [ Tr(beta) Tr(gamma) - 1/3 Tr(beta gamma) ]
        e1 = canon_monomial_expr(rest + (beta, gamma), F(1, 2))
        e2 = canon_monomial_expr(rest + (beta + gamma,), F(-1, 6))
        return expr_add(e1, e2)

def _cut_of(word_len, t, where):
    return (t + 1) % word_len if where == 'after' else t % word_len

def cas_monomial(m, gen):
    """Casimir derivation on monomial m for one generator (mode 'R')."""
    occ = _occurrences(m, gen)
    out = expr_scale({m: F(1)}, F(4, 3) * len(occ))
    for i in range(len(occ)):
        for j in range(i + 1, len(occ)):
            wi, ti, pi = occ[i]
            wj, tj, pj = occ[j]
            whi, subi, etai = _ins_data(pi, 'R')
            whj, subj, etaj = _ins_data(pj, 'R')
            Li, Lj = len(m[wi]), len(m[wj])
            ins_i = (wi, _cut_of(Li, ti, whi), subi)
            ins_j = (wj, _cut_of(Lj, tj, whj), subj)
            fz = pair_fierz(m, ins_i, ins_j)
            out = expr_add(out, expr_scale(fz, F(2) * etai * etaj))
    return out

def cross_monomial(m, s):
    """cross(s) = - sum_a D_a^(1) D_a^(2) on monomial m."""
    occ1 = _occurrences(m, 1)
    occ2 = _occurrences(m, 2)
    mode2 = 'R' if s == +1 else 'L'
    out = {}
    for (w1, t1, p1) in occ1:
        for (w2, t2, p2) in occ2:
            wh1, sub1, eta1 = _ins_data(p1, 'R')
            wh2, sub2, eta2 = _ins_data(p2, mode2)
            L1, L2 = len(m[w1]), len(m[w2])
            ins_1 = (w1, _cut_of(L1, t1, wh1), sub1)
            ins_2 = (w2, _cut_of(L2, t2, wh2), sub2)
            fz = pair_fierz(m, ins_1, ins_2)
            # Sigma_a d1 d2 = (i eta1)(i eta2) Fierz = -eta1 eta2 Fierz
            # cross = -Sigma  =>  +eta1 eta2 Fierz
            out = expr_add(out, expr_scale(fz, F(1) * eta1 * eta2))
    return out

def make_H0(model):
    """model: dict {gens: [..], s: +-1 or None}.  Returns expr->expr."""
    gens, s = model['gens'], model.get('s')
    cache = {}
    def H0_mono(m):
        if m in cache: return cache[m]
        out = {}
        for g in gens:
            out = expr_add(out, expr_scale(cas_monomial(m, g), F(2)))
        if s is not None:
            out = expr_add(out, cross_monomial(m, s))
        cache[m] = out
        return out
    def H0(e):
        out = {}
        for m, cf in e.items():
            out = expr_add(out, expr_scale(H0_mono(m), cf))
        return out
    H0.mono = H0_mono
    return H0

# ==================================================================
# SECTION D: exact rational linear algebra + resolvent
# ==================================================================
def solve_stacked(rows, rhs):
    """Exact Gaussian elimination on stacked system rows*y = rhs.
    Returns (particular_solution or None, kernel_basis)."""
    m = len(rows); n = len(rows[0]) if m else 0
    A = [list(rows[i]) + [rhs[i]] for i in range(m)]
    piv_cols, r = [], 0
    for col in range(n):
        piv = next((i for i in range(r, m) if A[i][col] != 0), None)
        if piv is None: continue
        A[r], A[piv] = A[piv], A[r]
        pv = A[r][col]
        A[r] = [x / pv for x in A[r]]
        for i in range(m):
            if i != r and A[i][col] != 0:
                f = A[i][col]
                A[i] = [A[i][j] - f * A[r][j] for j in range(n + 1)]
        piv_cols.append(col); r += 1
        if r == m: break
    for i in range(r, m):
        if A[i][n] != 0:
            return None, []
    sol = [F(0)] * n
    for i, col in enumerate(piv_cols):
        sol[col] = A[i][n]
    kernel = []
    free = [c for c in range(n) if c not in piv_cols]
    for fc in free:
        vec = [F(0)] * n; vec[fc] = F(1)
        for i, col in enumerate(piv_cols):
            vec[col] = -A[i][fc]
        kernel.append(vec)
    return sol, kernel

class Resolvent:
    def __init__(self, H0, E0, manifold, tag):
        self.H0, self.E0, self.manifold, self.tag = H0, E0, manifold, tag
        self.n_solves = 0
    def Q(self, x):
        out = dict(x)
        for f in self.manifold:
            ov = inner(f, x)
            if ov != 0:
                out = expr_add(out, f, -ov)
        return out
    def apply(self, x):
        qx = self.Q(x)
        if not qx: return {}
        # H0-closure of qx's support
        basis = list(qx.keys())
        seen = set(basis)
        idx = 0
        while idx < len(basis):
            hm = self.H0.mono(basis[idx])
            for m in hm:
                if m not in seen:
                    seen.add(m); basis.append(m)
            idx += 1
        nb = len(basis)
        pos = {m: i for i, m in enumerate(basis)}
        # columns of H0
        Hcols = []
        for m in basis:
            col = [F(0)] * nb
            for mm, cf in self.H0.mono(m).items():
                col[pos[mm]] += cf
            Hcols.append(col)
        # rows of (E0 I - H0)
        rows = [[(self.E0 if i == j else F(0)) - Hcols[j][i] for j in range(nb)]
                for i in range(nb)]
        rhs = [qx.get(m, F(0)) for m in basis]
        # stack manifold-overlap constraints  <f_m | y> = 0
        for f in self.manifold:
            rows.append([inner(f, {m: F(1)}) for m in basis])
            rhs.append(F(0))
        sol, kernel = solve_stacked(rows, rhs)
        gate(f"[{self.tag}] resolvent solve consistent (n={nb})", sol is not None)
        # verify residual exactly at coefficient level
        res = [sum(rows[i][j] * sol[j] for j in range(nb)) - rhs[i]
               for i in range(len(rows))]
        gate(f"[{self.tag}] resolvent residual identically zero", all(r == 0 for r in res))
        # kernel vectors must be zero FUNCTIONS (Gram norm 0)
        for kv in kernel:
            vec_expr = {}
            for j, cf in enumerate(kv):
                if cf != 0:
                    vec_expr = expr_add(vec_expr, {basis[j]: cf})
            nrm = inner(vec_expr, vec_expr)
            gate(f"[{self.tag}] kernel vector is the zero function", nrm == 0)
        self.n_solves += 1
        y = {}
        for j, cf in enumerate(sol):
            if cf != 0:
                y = expr_add(y, {basis[j]: cf})
        return y

# ==================================================================
# SECTION E: des Cloizeaux engine (orders 1..3)
# ==================================================================
def run_pt(model, manifold, E0, chars, tag):
    """Returns dict with exact h1, h2, h3 matrices on the manifold."""
    H0 = make_H0(model)
    R = Resolvent(H0, E0, manifold, tag)
    n = len(manifold)
    # manifold orthonormality
    for a in range(n):
        for b in range(n):
            val = inner(manifold[a], manifold[b])
            gate(f"[{tag}] manifold Gram[{a}][{b}] == {int(a==b)}",
                 val == (F(1) if a == b else F(0)))
    Wf  = [apply_W(f, chars) for f in manifold]
    B   = [[inner(manifold[a], Wf[b]) for b in range(n)] for a in range(n)]
    h1  = [[-B[a][b] for b in range(n)] for a in range(n)]
    y1  = [R.apply(Wf[b]) for b in range(n)]
    h2  = [[inner(manifold[a], apply_W(y1[b], chars)) for b in range(n)]
           for a in range(n)]
    z   = [apply_W(y1[b], chars) for b in range(n)]
    y2  = [R.apply(z[b]) for b in range(n)]
    M3  = [[inner(manifold[a], apply_W(y2[b], chars)) for b in range(n)]
           for a in range(n)]
    r2  = [R.apply(y1[b]) for b in range(n)]      # R^2 Q W f_b
    A   = [[inner(manifold[a], apply_W(r2[b], chars)) for b in range(n)]
           for a in range(n)]
    def matmul(X, Y):
        return [[sum(X[i][k] * Y[k][j] for k in range(n)) for j in range(n)]
                for i in range(n)]
    AB, BA = matmul(A, B), matmul(B, A)
    h3 = [[-M3[a][b] + F(1, 2) * (AB[a][b] + BA[a][b]) for b in range(n)]
          for a in range(n)]
    for h, nm in ((h1, 'h1'), (h2, 'h2'), (h3, 'h3')):
        gate(f"[{tag}] {nm} Hermitian", all(h[a][b] == h[b][a]
             for a in range(n) for b in range(n)))
    return {'h1': h1, 'h2': h2, 'h3': h3, 'A': A, 'B': B}

def sandwich(h, u, w):
    n = len(h)
    num = sum(u[i] * h[i][j] * w[j] for i in range(n) for j in range(n))
    den_u = sum(x * x for x in u)
    den_w = sum(x * x for x in w)
    assert den_u == den_w
    return num / den_u

# ==================================================================
# SECTION F: independent single-plaquette spectral checker
# (irrep basis, exact Schur characters via Jacobi-Trudi on the torus)
# ==================================================================
def h_poly(k):
    out = lp()
    if k < 0: return out
    for a in range(k + 1):
        for b in range(k + 1 - a):
            ccount = k - a - b
            out[(a - ccount, b - ccount)] += F(1)
    return out

def schur(p, q):
    lam = (p + q, q, 0)
    H = [[h_poly(lam[i] - i + j) for j in range(3)] for i in range(3)]
    det = lp()
    for sg in perms(3):
        term = lp({(0, 0): F(parity(sg))})
        for i in range(3):
            term = lp_mul(term, H[i][sg[i]])
        det = lp_add(det, term)
    return det

def lp_conj(a):
    return lp({(-e1, -e2): cf for (e1, e2), cf in a.items()})

def torus_int(f):
    return lp_mul(f, _WM).get((0, 0), F(0))

def spectral_single():
    reps = [(p, q) for p in range(0, 7) for q in range(0, 7) if p + q <= 6]
    chars = {r: schur(*r) for r in reps}
    C2 = {r: F(r[0]**2 + r[1]**2 + r[0]*r[1], 3) + F(r[0] + r[1]) for r in reps}
    dims = {r: F((r[0]+1)*(r[1]+1)*(r[0]+r[1]+2), 2) for r in reps}
    for r in reps[:8]:
        sval = sum(chars[r].values())
        gate(f"[spec] dim({r}) check", sval == dims[r])
    for r in [(0,0),(1,0),(0,1),(2,0),(1,1),(3,0),(2,1)]:
        for r2 in [(0,0),(1,0),(0,1),(2,0),(1,1)]:
            val = torus_int(lp_mul(lp_conj(chars[r]), chars[r2]))
            gate(f"[spec] <chi_{r}|chi_{r2}> == {int(r==r2)}",
                 val == (F(1) if r == r2 else F(0)))
    fund = chars[(1, 0)]
    fundb = chars[(0, 1)]
    Wop = lp_add(fund, fundb)
    w = {}
    for r in reps:
        for r2 in reps:
            w[(r, r2)] = torus_int(lp_mul(lp_mul(lp_conj(chars[r]), Wop), chars[r2]))
    gate("[spec] W symmetric", all(w[(a, b)] == w[(b, a)] for a in reps for b in reps))
    E = {r: 2 * C2[r] for r in reps}

    def pt(manifold, E0):
        others = [r for r in reps if r not in manifold]
        n = len(manifold)
        B  = [[w[(a, b)] for b in manifold] for a in manifold]
        h1 = [[-B[i][j] for j in range(n)] for i in range(n)]
        h2 = [[sum(w[(a, m)] * w[(m, b)] / (E0 - E[m]) for m in others)
               for b in manifold] for a in manifold]
        M3 = [[sum(w[(a, m)] * w[(m, mm)] * w[(mm, b)] /
                   ((E0 - E[m]) * (E0 - E[mm]))
                   for m in others for mm in others)
               for b in manifold] for a in manifold]
        A  = [[sum(w[(a, m)] * w[(m, b)] / (E0 - E[m])**2 for m in others)
               for b in manifold] for a in manifold]
        AB = [[sum(A[i][k] * B[k][j] for k in range(n)) for j in range(n)]
              for i in range(n)]
        BA = [[sum(B[i][k] * A[k][j] for k in range(n)) for j in range(n)]
              for i in range(n)]
        h3 = [[-M3[i][j] + F(1, 2) * (AB[i][j] + BA[i][j]) for j in range(n)]
              for i in range(n)]
        h2 = [[F(x) for x in row] for row in h2]
        return h1, h2, h3
    # vacuum
    h1v, h2v, h3v = pt([(0, 0)], F(0))
    gate("[spec] vacuum e1 == 0", h1v[0][0] == 0)
    gate("[spec] vacuum e2 == -3/4", h2v[0][0] == F(-3, 4))
    gate("[spec] vacuum e3 == -9/32", h3v[0][0] == F(-9, 32))
    # excited manifold {3, 3bar}
    man = [(1, 0), (0, 1)]
    h1, h2, h3 = pt(man, F(8, 3))
    ev_e = lambda h: F(1, 2) * (h[0][0] + h[0][1] + h[1][0] + h[1][1])
    ev_o = lambda h: F(1, 2) * (h[0][0] - h[0][1] - h[1][0] + h[1][1])
    res = {
        'lvl1': (ev_e(h1), ev_o(h1)),
        'lvl2': (ev_e(h2), ev_o(h2)),
        'lvl3': (ev_e(h3), ev_o(h3)),
        'vac':  (F(0), h2v[0][0], h3v[0][0]),
    }
    gate("[spec] order-1 levels (even,odd) == (-1,+1)", res['lvl1'] == (F(-1), F(1)))
    gate("[spec] order-2 levels == (-1/10, -1/4)",
         res['lvl2'] == (F(-1, 10), F(-1, 4)))
    gate("[spec] order-2 gaps == (13/20, 1/2)  [BRIDGE TOWERS]",
         (res['lvl2'][0] - res['vac'][1], res['lvl2'][1] - res['vac'][1])
         == (F(13, 20), F(1, 2)))
    gate("[spec] order-3 gaps == (101/200, 7/32)  [BRIDGE TOWERS]",
         (res['lvl3'][0] - res['vac'][2], res['lvl3'][1] - res['vac'][2])
         == (F(101, 200), F(7, 32)))
    return res

# ==================================================================
# SECTION G: structural gates on the word calculus
# ==================================================================
def expr_of(words, coeff=F(1)):
    return canon_monomial_expr(tuple(words), coeff)

CHI1, CHIB1 = ((1, +1),), ((1, -1),)
CHI2, CHIB2 = ((2, +1),), ((2, -1),)

def expr_eq(a, b):
    return expr_add(a, b, F(-1)) == {}

def structural_gates():
    Hs = make_H0({'gens': [1], 's': None})
    e_chi  = expr_of([CHI1]);  e_chib = expr_of([CHIB1])
    gate("[word] H0 chi1 = 8/3 chi1",
         expr_eq(Hs(e_chi), expr_scale(e_chi, F(8, 3))))
    gate("[word] H0 chibar1 = 8/3 chibar1",
         expr_eq(Hs(e_chib), expr_scale(e_chib, F(8, 3))))
    e_chi2 = expr_of([CHI1, CHI1])
    tgt = expr_add(expr_scale(e_chi2, F(20, 3)), e_chib, F(-4))
    gate("[word] H0 chi1^2 = (20/3) chi1^2 - 4 chibar1  (3bar/6 split)",
         expr_eq(Hs(e_chi2), tgt))
    e_cc = expr_of([CHI1, CHIB1])
    tgt2 = expr_add(expr_scale(e_cc, F(6)), expr_of([()])[()] and {(): F(-6)} or {})
    tgt2 = expr_add(expr_scale(e_cc, F(6)), {(): F(-6)})
    gate("[word] H0 chi1 chibar1 = 6 chi1 chibar1 - 6  (singlet/octet split)",
         expr_eq(Hs(e_cc), tgt2))
    gate("[word] Tr(g^2) rewrite == chi^2 - 2 chibar",
         expr_eq(canon_word(((1, 1), (1, 1))),
                 expr_add(expr_of([CHI1, CHI1]), e_chib, F(-2))))
    gate("[word] det relation: Tr(g^3) == chi^3 - 3 chi chibar + 3",
         expr_eq(canon_word(((1, 1), (1, 1), (1, 1))),
                 expr_add(expr_add(expr_of([CHI1]*3),
                                   expr_of([CHI1, CHIB1]), F(-3)), {(): F(3)})))
    # channel blocks for both s
    for s in (+1, -1):
        Hd = make_H0({'gens': [1, 2], 's': s})
        for (wa, wb, label, like) in [
            ((CHI1, CHI2),  ((1, 1), (2, 1)),  'chi1chi2|m++', s == +1),
            ((CHI1, CHIB2), ((1, 1), (2, -1)), 'chi1chib2|m+-', s == -1),
        ]:
            ea = expr_of(list(wa))
            eb = expr_of([wb])
            Ha, Hb = Hd(ea), Hd(eb)
            # exact 2x2 in the (ea, eb) coordinates
            aa = Ha.get(tuple(sorted(tuple(sorted(w)) for w in [])), None)
            # read coefficients directly
            ma = tuple(sorted([w for w in wa]))
            mb = tuple(sorted([_min_rotation(wb)]))
            haa = Ha.get(ma, F(0)); hba = Ha.get(mb, F(0))
            hab = Hb.get(ma, F(0)); hbb = Hb.get(mb, F(0))
            gate(f"[word s={s:+d}] block {label} closed (no extra monomials)",
                 set(Ha) <= {ma, mb} and set(Hb) <= {ma, mb})
            tr2 = haa + hbb; det2 = haa * hbb - hab * hba
            want = (F(14, 3), F(17, 3)) if like else (F(4), F(11, 2))
            gate(f"[word s={s:+d}] {label} eigenvalues == {want}",
                 tr2 == want[0] + want[1] and det2 == want[0] * want[1])

def single_plaquette_word():
    model = {'gens': [1], 's': None}
    chars = [(1, +1), (1, -1)]
    man = [expr_of([CHI1]), expr_of([CHIB1])]
    vac = run_pt(model, [ {(): F(1)} ], F(0), chars, 'sp-vac')
    gate("[sp-word] vacuum e1 == 0", vac['h1'][0][0] == 0)
    gate("[sp-word] vacuum e2 == -3/4", vac['h2'][0][0] == F(-3, 4))
    gate("[sp-word] vacuum e3 == -9/32", vac['h3'][0][0] == F(-9, 32))
    exc = run_pt(model, man, F(8, 3), chars, 'sp-exc')
    u_e, u_o = [F(1), F(1)], [F(1), F(-1)]
    lv = {}
    for k, h in (('1', exc['h1']), ('2', exc['h2']), ('3', exc['h3'])):
        lv[k] = (sandwich(h, u_e, u_e), sandwich(h, u_o, u_o))
        gate(f"[sp-word] h{k} parity off-block zero",
             sandwich(h, u_e, u_o) == 0)
    gate("[sp-word] order-1 levels == (-1, +1)", lv['1'] == (F(-1), F(1)))
    gate("[sp-word] order-2 levels == (-1/10, -1/4)", lv['2'] == (F(-1, 10), F(-1, 4)))
    gate("[sp-word] order-2 gaps == (13/20, 1/2)",
         (lv['2'][0] + F(3, 4), lv['2'][1] + F(3, 4)) == (F(13, 20), F(1, 2)))
    gate("[sp-word] order-3 gaps == (101/200, 7/32)  [BRIDGE, word calculus]",
         (lv['3'][0] + F(9, 32), lv['3'][1] + F(9, 32)) == (F(101, 200), F(7, 32)))
    return {'lvl3': lv['3'], 'vac3': vac['h3'][0][0], 'vac2': vac['h2'][0][0]}

# ==================================================================
# SECTION H: the domino, both s, orders 1..3
# ==================================================================
def domino(s):
    model = {'gens': [1, 2], 's': s}
    chars = [(1, +1), (1, -1), (2, +1), (2, -1)]
    man = [expr_of([CHI1]), expr_of([CHIB1]), expr_of([CHI2]), expr_of([CHIB2])]
    tag = f"dom(s={s:+d})"
    vac = run_pt(model, [ {(): F(1)} ], F(0), chars, tag + '-vac')
    gate(f"[{tag}] vacuum e2 == -3/2", vac['h2'][0][0] == F(-3, 2))
    gate(f"[{tag}] vacuum e3 == -9/16 (= 2 x single: no connected 3rd-order vac)",
         vac['h3'][0][0] == F(-9, 16))
    exc = run_pt(model, man, F(8, 3), chars, tag)
    # parity/swap-adapted vectors over basis [chi1, chib1, chi2, chib2]
    e1v, o1v = [F(1), F(1), F(0), F(0)], [F(1), F(-1), F(0), F(0)]
    e2v, o2v = [F(0), F(0), F(1), F(1)], [F(0), F(0), F(1), F(-1)]
    out = {'vac2': vac['h2'][0][0], 'vac3': vac['h3'][0][0]}
    for k, h in (('1', exc['h1']), ('2', exc['h2']), ('3', exc['h3'])):
        De = sandwich(h, e1v, e1v); Te = sandwich(h, e1v, e2v)
        Do = sandwich(h, o1v, o1v); To = sandwich(h, o1v, o2v)
        gate(f"[{tag}] h{k} C-parity block diagonal",
             sandwich(h, e1v, o1v) == 0 and sandwich(h, e1v, o2v) == 0
             and sandwich(h, e2v, o1v) == 0 and sandwich(h, e2v, o2v) == 0)
        gate(f"[{tag}] h{k} swap symmetric",
             sandwich(h, e1v, e1v) == sandwich(h, e2v, e2v)
             and sandwich(h, o1v, o1v) == sandwich(h, o2v, o2v))
        out[f'De{k}'], out[f'Te{k}'] = De, Te
        out[f'Do{k}'], out[f'To{k}'] = Do, To
    return out

# ==================================================================
def main():
    print("=" * 78)
    print("SECTION A-F gates: independent spectral single plaquette")
    print("=" * 78)
    spec = spectral_single()

    print("=" * 78)
    print("Structural gates: word calculus / H0 derivation")
    print("=" * 78)
    structural_gates()

    print("=" * 78)
    print("Single plaquette via word calculus (cross-validates des Cloizeaux)")
    print("=" * 78)
    sp = single_plaquette_word()

    print("=" * 78)
    print("Domino, s = +1 and s = -1")
    print("=" * 78)
    dp = domino(+1)
    dm = domino(-1)

    print("=" * 78)
    print("Order-by-order physics gates")
    print("=" * 78)
    # order 1
    gate("order-1: De1 == -1, Do1 == +1 (both s)",
         dp['De1'] == F(-1) and dp['Do1'] == F(1)
         and dm['De1'] == F(-1) and dm['Do1'] == F(1))
    gate("order-1: no first-order hopping", dp['Te1'] == 0 and dp['To1'] == 0
         and dm['Te1'] == 0 and dm['To1'] == 0)
    # order 2: the gold ladder
    gate("order-2: C-odd hopping T2(s) == s * 5/612",
         dp['To2'] == F(5, 612) and dm['To2'] == F(-5, 612))
    gate("order-2: C-even hopping s-independent", dp['Te2'] == dm['Te2'])
    gate("order-2: C-even hopping == -11/306  ( = -481/612 + 3/4 vacuum route )",
         dp['Te2'] == F(-11, 306))
    gate("order-2: diagonals s-independent",
         dp['Do2'] == dm['Do2'] and dp['De2'] == dm['De2'])
    gate("order-2: C-odd diag-gap == 284/612",
         dp['Do2'] - dp['vac2'] == F(284, 612))
    lv_odd = sorted([dp['Do2'] - dp['vac2'] + dp['To2'],
                     dp['Do2'] - dp['vac2'] - dp['To2']])
    gate("order-2: C-odd domino gap levels == {31/68, 17/36}  [paper SS7]",
         lv_odd == [F(31, 68), F(17, 36)])
    lv_even = sorted([dp['De2'] - dp['vac2'] + dp['Te2'],
                      dp['De2'] - dp['vac2'] - dp['Te2']])
    gate("order-2: C-even domino gap levels == {1769/3060, 13/20}  [paper SS7]",
         lv_even == [F(1769, 3060), F(13, 20)])
    leak2 = (dp['Do2'] - dp['vac2']) - F(1, 2)
    gate("order-2: per-neighbor diagonal leakage == -11/306",
         leak2 == F(-11, 306))
    m2_flat = F(1, 2) + 12 * leak2 + (-4) * (dp['To2'] / 1)  # b2 = T2(+1)
    gate("order-2 assembly reproduces flat-band 11/306",
         m2_flat == F(11, 306))

    # order 3: structure gates
    gate("order-3: C-odd hopping odd in s: T3(+1) == -T3(-1)  [sigma-covariance]",
         dp['To3'] == -dm['To3'])
    gate("order-3: C-even hopping s-independent", dp['Te3'] == dm['Te3'])
    gate("order-3: diagonals s-independent",
         dp['Do3'] == dm['Do3'] and dp['De3'] == dm['De3'])
    gate("order-3: domino C-odd single-gap consistency "
         "(vac3 matches single x2 used in leakage)",
         dp['vac3'] == F(-9, 16))
    # exact structural identity (echoes order 2): C-even leakage == C-even hop
    gate("identity: leak2_even == T2_even == -11/306",
         (dp['De2'] - dp['vac2']) - F(13, 20) == dp['Te2'] == F(-11, 306))
    gate("identity: leak3_even == T3_even  (vacuum-route mechanism, order 3)",
         (dp['De3'] - dp['vac3']) - F(101, 200) == dp['Te3'])
    # certificate locks (regression pins for the computed exact constants)
    gate("lock: b3 == 1975/124848", dp['To3'] == F(1975, 124848))
    gate("lock: T3_even == -6335/249696", dp['Te3'] == F(-6335, 249696))
    gate("lock: D3_odd == -24541/62424", dp['Do3'] == F(-24541, 62424))
    gate("lock: D3_even == -517313/6242400", dp['De3'] == F(-517313, 6242400))

    print("=" * 78)
    print("ASSEMBLY: exact O(y^3) constants")
    print("=" * 78)
    b3 = dp['To3']                       # T3(s)/s at s=+1
    gap3_single_odd  = F(7, 32)
    gap3_single_even = F(101, 200)
    leak3_o = (dp['Do3'] - dp['vac3']) - gap3_single_odd
    leak3_e = (dp['De3'] - dp['vac3']) - gap3_single_even
    d3      = gap3_single_odd + 12 * leak3_o + (-4) * b3
    d3_top  = gap3_single_odd + 12 * leak3_o + 8 * b3
    t3e     = dp['Te3']
    m3_even_k0   = gap3_single_even + 12 * leak3_e + 12 * t3e
    m3_even_min  = gap3_single_even + 12 * leak3_e + (-4) * t3e
    # corrected O(y^2) C-even numbers (vacuum-route hopping)
    t2e = dp['Te2']
    leak2e = (dp['De2'] - dp['vac2']) - F(13, 20)
    m2_even_k0  = F(13, 20) + 12 * leak2e + 12 * t2e
    m2_even_min = F(13, 20) + 12 * leak2e + (-4) * t2e
    gate("lock: d3 == -109151/249696", d3 == F(-109151, 249696))
    gate("lock: d3_top == -61751/249696", d3_top == F(-61751, 249696))
    gate("lock: m3_even_k0 == -54049/520200", m3_even_k0 == F(-54049, 520200))
    gate("lock: corrected m2_even_k0 == -217/1020", m2_even_k0 == F(-217, 1020))

    results = {
        'order2': {
            'T2_odd(s=+1)': str(dp['To2']), 'T2_even': str(t2e),
            'leak2_odd': str(leak2), 'leak2_even': str(leak2e),
            'm2_even_k0_A1++_corrected': str(m2_even_k0),
            'm2_even_bandmin_corrected': str(m2_even_min),
            'm2_odd_flat': str(m2_flat),
            'corrected_Ceven_curvature_coeff': str(-t2e * F(4, 3)),
            'corrected_Ceven_bandwidth_16|t|': str(16 * abs(t2e)),
            'E++_k0_unchanged': str(F(13, 20) + 12 * leak2e),
        },
        'order3': {
            'b3 = T3_odd(s=+1)': str(b3),
            'T3_even': str(t3e),
            'D3_odd': str(dp['Do3']), 'D3_even': str(dp['De3']),
            'e_vac3_domino': str(dp['vac3']),
            'leak3_odd': str(leak3_o), 'leak3_even': str(leak3_e),
            'd3 (C-odd flat band, all k)': str(d3),
            'd3_top (C-odd dispersive top, mu=8)': str(d3_top),
            'm3_even_k0 (A1++ at k=0)': str(m3_even_k0),
            'm3_even_bandmin (lambda=-4)': str(m3_even_min),
        },
    }
    print(json.dumps(results, indent=2))
    with open('/home/claude/review/RUN_TROM_d3_results.json', 'w') as fh:
        json.dump(results, fh, indent=2)

    print("=" * 78)
    print(f"ALL {len(GATES)} GATES PASSED")
    print(f"  m-(k) = 8/3 + y + (11/306) y^2 + ({d3}) y^3   for ALL k")
    print("=" * 78)

if __name__ == "__main__":
    main()
