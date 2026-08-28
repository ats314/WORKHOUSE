#!/usr/bin/env python3
"""Standard-library verifier for the master paper's core claims.

No dependencies. Five claim groups, matching the paper's Reproducibility
section:

  1. the rational coefficient ledger (channel weights, A_N, B_N, t_N, ell_N,
     the SU(3) third-order assembly, and the one-formula band assembly);
  2. the Weingarten derivation of the channel weights, by explicit summation
     over every index quadruple;
  3. the incidence identity B B+ = q I - w w+, DECIDED in exact
     Gaussian-rational arithmetic at rational torus points (each entry is a
     polynomial of degree <= 2 per variable; exact vanishing on a 5-point
     grid per variable decides the polynomial identity, not a residual);
  4. the chain condition d2 d3 = 0 over Z and the finite-torus ranks, with an
     EXPLICIT kernel basis (cube boundaries + three wrapping sheets) shown to
     be cycles of full kernel rank;
  5. the wrapping sheets are cycles but not harmonic: Rayleigh quotient
     exactly 2.

Rational-function identities in N are decided by exact evaluation at more
integer points than their degree bound: every identity below has numerator
and denominator degree <= 10, and is checked at N = 2..30.

Run:  python3 verify_core.py
"""

from __future__ import annotations

import sys
from fractions import Fraction as F
from itertools import product

CHECKS = []


def check(name):
    def register(fn):
        CHECKS.append((name, fn))
        return fn

    return register


# ---------------------------------------------------------------------------
# 1. The rational coefficient ledger
# ---------------------------------------------------------------------------

#: (dimension, quadratic Casimir) per shared-link fusion channel, as functions
#: of the rank N — the paper's eq. (12) table.
CHANNELS = {
    "singlet": (lambda n: F(1), lambda n: F(0)),
    "adjoint": (lambda n: F(n * n - 1), lambda n: F(n)),
    "antisym": (lambda n: F(n * (n - 1), 2), lambda n: F((n + 1) * (n - 2), n)),
    "sym": (lambda n: F(n * (n + 1), 2), lambda n: F((n - 1) * (n + 2), n)),
}


def c_fund(n):
    return F(n * n - 1, 2 * n)


def weight(rho, n):
    d, c = CHANNELS[rho]
    return -(d(n) / F(n * n)) / (c_fund(n) + c(n) / 2)


def a_sum(n):
    return weight("singlet", n) + weight("adjoint", n)


def b_sum(n):
    return weight("antisym", n) + weight("sym", n)


RANKS = range(2, 31)  # more points than any identity's degree bound


@check("channel weights match their closed forms (App. A), N = 2..30")
def _():
    closed = {
        "singlet": lambda n: F(-2, n * (n - 1) * (n + 1)),
        "adjoint": lambda n: F(-2 * (n - 1) * (n + 1), n * (2 * n * n - 1)),
        "antisym": lambda n: F(-(n - 1), (n + 1) * (2 * n - 3)),
        "sym": lambda n: F(-(n + 1), (n - 1) * (2 * n + 3)),
    }
    return all(weight(r, n) == closed[r](n) for r in CHANNELS for n in RANKS)


@check("A_N, B_N, t_N = B_N - A_N and ell_N = A_N + B_N + 1/C_F, N = 2..30")
def _():
    ok = True
    for n in RANKS:
        ok &= a_sum(n) == F(-2 * n**3, (n * n - 1) * (2 * n * n - 1))
        ok &= b_sum(n) == F(-4 * n * (n * n - 2), (n * n - 1) * (4 * n * n - 9))
        t = b_sum(n) - a_sum(n)
        ok &= t == F(2 * n * (n * n - 4), (n * n - 1) * (2 * n * n - 1) * (4 * n * n - 9))
        ell = a_sum(n) + b_sum(n) + 1 / c_fund(n)
        ok &= ell == F(-2 * n * (3 * n * n - 5), (n * n - 1) * (2 * n * n - 1) * (4 * n * n - 9))
    t3 = b_sum(3) - a_sum(3)
    ell3 = a_sum(3) + b_sum(3) + 1 / c_fund(3)
    return ok and b_sum(2) == a_sum(2) and t3 == F(5, 612) and ell3 == F(-11, 306)


#: SU(3) ledger (paper App. C) and the domino-engine diagonal/vacuum pieces.
B_3 = F(1975, 124848)
LEAK_3 = F(-12331, 249696)
D_3 = F(-109151, 249696)
D3_ODD_DOMINO = F(-24541, 62424)
D3_EVEN_DOMINO = F(-517313, 6242400)
VAC3_DOMINO = F(-9, 16)
T3_EVEN = F(-6335, 249696)


@check("SU(3) third-order assembly: d_3 = 7/32 + 12 leak_3 - 4 b_3")
def _():
    return F(7, 32) + 12 * LEAK_3 - 4 * B_3 == D_3


@check("leak_3 = domino diagonal - vacuum piece - tower, both sectors")
def _():
    odd = D3_ODD_DOMINO - VAC3_DOMINO - F(7, 32) == LEAK_3
    even = D3_EVEN_DOMINO - VAC3_DOMINO - F(101, 200) == T3_EVEN
    return odd and even


@check("one assembly formula gives all nine diagonal and band values")
def _():
    tower = {(2, "-"): F(1, 2), (3, "-"): F(7, 32), (2, "+"): F(13, 20), (3, "+"): F(101, 200)}
    leak = {(2, "-"): F(-11, 306), (2, "+"): F(-11, 306), (3, "-"): LEAK_3, (3, "+"): T3_EVEN}
    hop = {(2, "-"): F(5, 612), (2, "+"): F(-11, 306), (3, "-"): B_3, (3, "+"): T3_EVEN}

    def assemble(lam, r, s):
        return tower[(r, s)] + 12 * leak[(r, s)] + lam * hop[(r, s)]

    targets = [
        (assemble(0, 2, "-"), F(7, 102)),
        (assemble(-4, 2, "-"), F(11, 306)),
        (assemble(8, 2, "-"), F(41, 306)),
        (assemble(0, 2, "+"), F(223, 1020)),
        (assemble(12, 2, "+"), F(-217, 1020)),
        (assemble(-4, 2, "+"), F(1109, 3060)),
        (assemble(-4, 3, "-"), D_3),
        (assemble(8, 3, "-"), F(-61751, 249696)),
        (assemble(12, 3, "+"), F(-54049, 520200)),
    ]
    return all(got == want for got, want in targets)


@check("band spans: 12 t_3 = 5/51 (C-odd), 16 |ell_3| = 88/153 (C-even)")
def _():
    return 12 * F(5, 612) == F(5, 51) and 16 * F(11, 306) == F(88, 153)


# ---------------------------------------------------------------------------
# 2. The Weingarten derivation, by explicit summation
# ---------------------------------------------------------------------------


def wg_moments_explicit(n):
    """(M_direct, M_cross) summed over every index quadruple."""
    wg = {(0, 0): F(1, n * n - 1), (0, 1): F(-1, n * (n * n - 1))}
    wg[(1, 0)], wg[(1, 1)] = wg[(0, 1)], wg[(0, 0)]

    def moment(i1, j1, i2, j2, i1p, j1p, i2p, j2p):
        total = F(0)
        iis, jjs, iips, jjps = (i1, i2), (j1, j2), (i1p, i2p), (j1p, j2p)
        for s in (0, 1):
            for t in (0, 1):
                if all(iis[a] == iips[a ^ s] and jjs[a] == jjps[a ^ t] for a in (0, 1)):
                    total += wg[(s, t)]
        return total

    rng = range(n)
    direct = sum(moment(i, j, k, m, i, j, k, m) for i, j, k, m in product(rng, repeat=4))
    cross = sum(moment(i, j, k, m, i, m, k, j) for i, j, k, m in product(rng, repeat=4))
    return direct, cross


@check("Weingarten index sums: M_direct = N^2, M_cross = N, N = 2..6")
def _():
    return all(wg_moments_explicit(n) == (n * n, n) for n in range(2, 7))


@check("channel weights are d_rho/N^2 from the two moments, N = 2..30")
def _():
    ok = True
    for n in RANKS:
        m_direct, m_cross = F(n * n), F(n)  # decided above by explicit summation
        ok &= (m_direct + m_cross) / (2 * m_direct) == CHANNELS["sym"][0](n) / (n * n)
        ok &= (m_direct - m_cross) / (2 * m_direct) == CHANNELS["antisym"][0](n) / (n * n)
        ok &= 1 / m_direct == CHANNELS["singlet"][0](n) / (n * n)
        ok &= 1 - 1 / m_direct == CHANNELS["adjoint"][0](n) / (n * n)
    return ok


# ---------------------------------------------------------------------------
# 3. The incidence identity, in exact Gaussian-rational arithmetic
# ---------------------------------------------------------------------------


class GQ:
    """A Gaussian rational a + b i with exact Fraction parts."""

    __slots__ = ("re", "im")

    def __init__(self, re, im=0):
        self.re, self.im = F(re), F(im)

    def __add__(self, o):
        return GQ(self.re + o.re, self.im + o.im)

    def __sub__(self, o):
        return GQ(self.re - o.re, self.im - o.im)

    def __mul__(self, o):
        return GQ(self.re * o.re - self.im * o.im, self.re * o.im + self.im * o.re)

    def conj(self):
        return GQ(self.re, -self.im)

    def is_zero(self):
        return self.re == 0 and self.im == 0


def circle_point(t):
    """The rational unit-circle point ((1 - t^2) + 2 t i)/(1 + t^2)."""
    den = 1 + t * t
    return GQ((1 - t * t) / den, 2 * t / den)


@check("B B+ = q I - w w+ decided at rational torus points (5^3 grid)")
def _():
    ts = [F(1, 2), F(1, 3), F(2, 5), F(3, 7), F(5, 9)]
    zero = GQ(0)
    for t1, t2, t3 in product(ts, repeat=3):
        d = [circle_point(t) - GQ(1) for t in (t1, t2, t3)]
        b = [
            [d[1], zero - d[0], zero],
            [d[2], zero, zero - d[0]],
            [zero, d[2], zero - d[1]],
        ]
        w = [d[2].conj(), zero - d[1].conj(), d[0].conj()]
        q = zero
        for dj in d:
            q = q + dj * dj.conj()
        for r in range(3):
            for c in range(3):
                bbd = zero
                for m in range(3):
                    bbd = bbd + b[r][m] * b[c][m].conj()
                rhs = (q if r == c else zero) - w[r] * w[c].conj()
                if not (bbd - rhs).is_zero():
                    return False
        # B+ w = 0 and |w|^2 = q, the carrier statements
        for c in range(3):
            acc = zero
            for r in range(3):
                acc = acc + b[r][c].conj() * w[r]
            if not acc.is_zero():
                return False
        norm = zero
        for wr in w:
            norm = norm + wr * wr.conj()
        if not (norm - q).is_zero():
            return False
    return True


# ---------------------------------------------------------------------------
# 4. The chain complex over Z, with an explicit kernel basis
# ---------------------------------------------------------------------------

PAIRS = ((1, 2), (1, 3), (2, 3))


def _site(x, ell):
    return x[0] + ell * (x[1] + ell * x[2])


def _shift(x, i, ell):
    y = list(x)
    y[i - 1] = (y[i - 1] + 1) % ell
    return tuple(y)


def d2_matrix(ell):
    n = 3 * ell**3
    rows = [[0] * n for _ in range(n)]
    for x in product(range(ell), repeat=3):
        for pi, (i, j) in enumerate(PAIRS):
            col = 3 * _site(x, ell) + pi
            rows[3 * _site(_shift(x, i, ell), ell) + (j - 1)][col] += 1
            rows[3 * _site(x, ell) + (j - 1)][col] -= 1
            rows[3 * _site(_shift(x, j, ell), ell) + (i - 1)][col] -= 1
            rows[3 * _site(x, ell) + (i - 1)][col] += 1
    return rows


def d3_matrix(ell):
    rows = [[0] * ell**3 for _ in range(3 * ell**3)]
    for x in product(range(ell), repeat=3):
        col = _site(x, ell)
        for sign, i, pair in ((1, 1, (2, 3)), (-1, 2, (1, 3)), (1, 3, (1, 2))):
            pi = PAIRS.index(pair)
            rows[3 * _site(_shift(x, i, ell), ell) + pi][col] += sign
            rows[3 * _site(x, ell) + pi][col] -= sign
    return rows


def sheets(ell):
    out = []
    for pi, (i, j) in enumerate(PAIRS):
        (m,) = set((1, 2, 3)) - {i, j}
        v = [0] * (3 * ell**3)
        for x in product(range(ell), repeat=3):
            if x[m - 1] == 0:
                v[3 * _site(x, ell) + pi] = 1
        out.append(v)
    return out


def matmul(a, b):
    return [
        [sum(a[r][k] * b[k][c] for k in range(len(b))) for c in range(len(b[0]))]
        for r in range(len(a))
    ]


def rank(mat):
    """Exact rank by Fraction Gaussian elimination."""
    m = [[F(v) for v in row] for row in mat]
    nrows, ncols = len(m), len(m[0])
    r = 0
    for c in range(ncols):
        piv = next((i for i in range(r, nrows) if m[i][c] != 0), None)
        if piv is None:
            continue
        m[r], m[piv] = m[piv], m[r]
        inv = 1 / m[r][c]
        m[r] = [v * inv for v in m[r]]
        for i in range(nrows):
            if i != r and m[i][c] != 0:
                f = m[i][c]
                m[i] = [a - f * b for a, b in zip(m[i], m[r], strict=True)]
        r += 1
        if r == nrows:
            break
    return r


@check("d2 d3 = 0 over Z and rank d3 = L^3 - 1, L = 1..3")
def _():
    for ell in (1, 2, 3):
        d2, d3 = d2_matrix(ell), d3_matrix(ell)
        if any(v != 0 for row in matmul(d2, d3) for v in row):
            return False
        if rank(d3) != ell**3 - 1:
            return False
    return True


@check("dim ker d2 = L^3 + 2 with an explicit spanning cycle basis, L = 1..3")
def _():
    for ell in (1, 2, 3):
        d2, d3 = d2_matrix(ell), d3_matrix(ell)
        nullity = 3 * ell**3 - rank(d2)
        if nullity != ell**3 + 2:
            return False
        # explicit basis: the L^3 cube boundaries plus the three sheets
        n_faces = 3 * ell**3
        cols = [[d3[r][c] for r in range(n_faces)] for c in range(ell**3)] + sheets(ell)
        # every column is a cycle over Z
        for col in cols:
            if any(sum(d2[r][k] * col[k] for k in range(n_faces)) != 0 for r in range(n_faces)):
                return False
        # and together they have full kernel rank
        if rank([[col[r] for col in cols] for r in range(n_faces)]) != nullity:
            return False
    return True


# ---------------------------------------------------------------------------
# 5. The wrapping sheets are cycles but not harmonic
# ---------------------------------------------------------------------------


@check("sheet Rayleigh quotient <s, d3 d3^T s>/|s|^2 = 2 exactly, L = 2..4")
def _():
    for ell in (2, 3, 4):
        d3 = d3_matrix(ell)
        for s in sheets(ell):
            up = [sum(d3[r][c] * s[r] for r in range(len(s))) for c in range(ell**3)]
            num = sum(v * v for v in up)
            den = sum(v * v for v in s)
            if num != 2 * den or num == 0:
                return False
    return True


# ---------------------------------------------------------------------------


def main():
    failures = 0
    for name, fn in CHECKS:
        ok = fn()
        print(("PASS  " if ok else "FAIL  ") + name)
        failures += not ok
    print(f"\n{len(CHECKS) - failures}/{len(CHECKS)} core checks passed")
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
