#!/usr/bin/env python3
"""Standard-library verifier for the master paper's core claims.

No dependencies. Nine claim groups, matching the paper's Reproducibility
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
     exactly 2;
  6. the two-cube closure: the connected geometry rebuilt from oriented cell
     boundaries, its exact B = 6 and B = 4 spectra, and the six-channel
     census shown to BE the four Weingarten weights channel by channel;
  7. the charge-even Bloch cubic, decided at rational torus points, with
     p + q = 12 and the four high-symmetry spectra;
  8. the fourth-order checkpoint algebra: the extraction formulas invert the
     ansatz, X is blind to B, C and D, and e_2 vanishes identically on every
     axial cut -- the obstruction, as arithmetic. Nothing here decides
     C_shp, and no value of it is assumed;
  9. the coupling convention: 4 Delta(3u/2) reproduces the printed towers,
     and a 4**r rescaling misses them by exactly 16 and 64.

Every value is a Fraction. No float is constructed anywhere in this file, so
"agreement" here always means equality, never proximity.

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
# 6. The two-cube closure (runs/two_cube_codd_o2_2026-08-29)
# ---------------------------------------------------------------------------

#: The eleven oriented plaquettes of the open face-sharing (3,2,2) prism, in
#: the delivery's frozen order: base vertex and ordered plane axes.
TWO_CUBE_FACES = (
    ((0, 0, 0), (1, 2)),
    ((0, 0, 0), (1, 3)),
    ((0, 0, 0), (2, 3)),
    ((0, 0, 1), (1, 2)),
    ((0, 1, 0), (1, 3)),
    ((1, 0, 0), (1, 2)),
    ((1, 0, 0), (1, 3)),
    ((1, 0, 0), (2, 3)),
    ((1, 0, 1), (1, 2)),
    ((1, 1, 0), (1, 3)),
    ((2, 0, 0), (2, 3)),
)
#: left cube, right cube, shared face -- the index sets the Mobius fold uses.
I_L, I_R, I_F = (0, 1, 2, 3, 4, 7), (5, 6, 7, 8, 9, 10), (7,)


def two_cube_gram():
    """G = B B^T for the eleven faces, from oriented boundaries only.

    The delivery's own incidence array is not read: a face at base vertex x in
    plane (a, b) has oriented boundary +(x,a) +(x+e_a,b) -(x+e_b,a) -(x,b),
    the same convention the periodic complex uses above.
    """
    rows = []
    for x, (a, b) in TWO_CUBE_FACES:
        xa = tuple(v + (1 if k == a - 1 else 0) for k, v in enumerate(x))
        xb = tuple(v + (1 if k == b - 1 else 0) for k, v in enumerate(x))
        chain = {}
        for vertex, axis, sign in ((x, a, +1), (xa, b, +1), (xb, a, -1), (x, b, -1)):
            chain[(vertex, axis)] = chain.get((vertex, axis), 0) + sign
        rows.append(chain)
    links = sorted({k for r in rows for k in r})
    dense = [[r.get(k, 0) for k in links] for r in rows]
    return [[sum(p * q for p, q in zip(r, c, strict=True)) for c in dense] for r in dense]


def mobius_fold(g):
    """G_conn = G - J_L G_L J_L^T - J_R G_R J_R^T + J_F G_F J_F^T."""
    out = [row[:] for row in g]
    for idx, sign in ((I_L, -1), (I_R, -1), (I_F, +1)):
        for i in idx:
            for j in idx:
                out[i][j] += sign * g[i][j]
    return out


@check("two-cube connected geometry: four cross-cell pairs at -1, nothing else")
def _():
    conn = mobius_fold(two_cube_gram())
    off = {(i, j): conn[i][j] for i in range(11) for j in range(11) if i != j and conn[i][j]}
    want = {(0, 5), (5, 0), (1, 6), (6, 1), (3, 8), (8, 3), (4, 9), (9, 4)}
    return set(off) == want and set(off.values()) == {-1}


#: The six shared-link channel coefficients the delivery recovered, target-blind.
TWO_CUBE_CHANNELS = {
    "1": F(1, 12),
    "3": F(-1, 12),
    "bar3": F(-1, 12),
    "6": F(-1, 9),
    "bar6": F(-1, 9),
    "8": F(16, 51),
}


@check("two-cube six-channel census sums to t_3 = 5/612")
def _():
    return sum(TWO_CUBE_CHANNELS.values()) == F(5, 612) == b_sum(3) - a_sum(3)


@check("the census IS the Weingarten ledger: c_1 = -w_1, c_8 = -w_Adj, c_rho = w/2")
def _():
    # The sum is weak evidence -- six rationals reach 5/612 many ways. The
    # statement worth checking is channel by channel. The mixed family enters
    # negated because t_N = B_N - A_N; each like-family FUSION weight is split
    # evenly between the irrep and its conjugate, which is what distinguishes
    # the certificate's link-irrep labelling from the fusion-channel labelling
    # of Section 4. N = 3 only: the even split at every rank is a conjecture.
    predicted = {
        "1": -weight("singlet", 3),
        "8": -weight("adjoint", 3),
        "3": weight("antisym", 3) / 2,
        "bar3": weight("antisym", 3) / 2,
        "6": weight("sym", 3) / 2,
        "bar6": weight("sym", 3) / 2,
    }
    return predicted == TWO_CUBE_CHANNELS


@check("B = 4 and the published p+q<=1 cutoff are one truncation: -1/12, omitting 14/153")
def _():
    b4 = TWO_CUBE_CHANNELS["1"] + TWO_CUBE_CHANNELS["3"] + TWO_CUBE_CHANNELS["bar3"]
    omitted = TWO_CUBE_CHANNELS["6"] + TWO_CUBE_CHANNELS["bar6"] + TWO_CUBE_CHANNELS["8"]
    cutoff = weight("antisym", 3) - weight("singlet", 3)
    completion = weight("sym", 3) - weight("adjoint", 3)
    return (
        b4 == cutoff == F(-1, 12)
        and omitted == completion == F(14, 153)
        and b4 + omitted == F(5, 612)
    )


def two_cube_spectrum(coeff, diagonal):
    """Exact spectrum of coeff * G_conn + diag(diagonal).

    G_conn is four disjoint 2x2 blocks plus three isolated directions, so the
    eigenvalues are closed form: diag +- coeff*(-1) on each pair, and the
    diagonal itself on each isolated face. The block structure is asserted by
    the geometry check above, not assumed here.
    """
    conn = mobius_fold(two_cube_gram())
    pairs = ((0, 5), (1, 6), (3, 8), (4, 9))
    seen = {}
    for i, j in pairs:
        for ev in (diagonal[i] + coeff * conn[i][j], diagonal[i] - coeff * conn[i][j]):
            seen[ev] = seen.get(ev, 0) + 1
    for i in range(11):
        if not any(i in p for p in pairs):
            seen[diagonal[i]] = seen.get(diagonal[i], 0) + 1
    return seen


@check("B = 6 connected kernel has spectrum {0, (-15/4)^2, (-34/9)^4, (-129/34)^4}")
def _():
    d = [
        F(v, 612) for v in (-2317, -2317, -2295, -2317, -2317, -2317, -2317, 0, -2317, -2317, -2295)
    ]
    got = two_cube_spectrum(F(5, 612), d)
    return got == {F(0): 1, F(-15, 4): 2, F(-34, 9): 4, F(-129, 34): 4}


@check("B = 4 comparator on the same geometry: {0, (-15/4)^2, (-11/6)^4, (-5/3)^4}")
def _():
    # The sealed B = 4 result on the IDENTICAL geometry: K_conn = -(1/12)
    # G_conn + D_B4. Its ordering is the reverse of B = 6's -- the paired
    # (cross-cell) levels sit above the isolated ones there and below them
    # here -- because the coefficient changed sign. That reversal is the
    # whole content of the truncation finding, and it is exact.
    d = [F(-7, 4)] * 11
    d[2] = d[10] = F(-15, 4)
    d[7] = F(0)
    got = two_cube_spectrum(F(-1, 12), d)
    want = {F(0): 1, F(-15, 4): 2, F(-11, 6): 4, F(-5, 3): 4}
    if got != want:
        return False
    # and the sign of the pair splitting is opposite in the two truncations
    lo6 = min(two_cube_spectrum(F(5, 612), [F(0)] * 11))
    lo4 = min(two_cube_spectrum(F(-1, 12), [F(0)] * 11))
    return lo6 == F(-5, 612) and lo4 == F(-1, 12)


#: exact quadratic Casimirs of the SU(3) irreps the truncations can carry.
CASIMIR = {"1": F(0), "3": F(4, 3), "bar3": F(4, 3), "6": F(10, 3), "bar6": F(10, 3), "8": F(3)}


@check("Casimir budgets: B = 6 retains all six adjacent channels, B = 4 only three")
def _():
    budget = {r: CASIMIR[r] + 2 * CASIMIR["3"] for r in CASIMIR}
    in6 = {r for r, b in budget.items() if b <= 6}
    in4 = {r for r, b in budget.items() if b <= 4}
    return (
        in6 == set(CASIMIR)
        and in4 == {"1", "3", "bar3"}
        and budget["6"] == 6
        and budget["8"] == F(17, 3)
    )


# ---------------------------------------------------------------------------
# 7. The charge-even Bloch cubic
# ---------------------------------------------------------------------------


@check("C-even charpoly is mu^3 - 2p mu^2 + p^2 mu - 4 a1 a2 a3, at rational points")
def _():
    # The unsigned incidence drops the boundary SIGNS, so every entry of the
    # signed B becomes +(z + 1) rather than +-(z - 1):
    #
    #     N(k) = [[v2, v1, 0], [v3, 0, v1], [0, v3, v2]],  v_j = e^{i k_j} + 1.
    #
    # (Writing N with the signed sign pattern instead is the easy mistake: it
    # flips exactly one Gram entry and the determinant with it.) The three
    # coefficients of the characteristic polynomial of N N+ are decided here
    # at rational circle points, where every quantity is a Gaussian rational.
    ts = [F(1, 2), F(1, 3), F(2, 5), F(3, 7), F(5, 9)]
    zero = GQ(0)
    for t1, t2, t3 in product(ts, repeat=3):
        v = [circle_point(t) + GQ(1) for t in (t1, t2, t3)]
        nmat = [
            [v[1], v[0], zero],
            [v[2], zero, v[0]],
            [zero, v[2], v[1]],
        ]
        gram = []
        for r in range(3):
            row = []
            for c in range(3):
                acc = zero
                for m in range(3):
                    acc = acc + nmat[r][m] * nmat[c][m].conj()
                row.append(acc)
            gram.append(row)
        a = [(vj * vj.conj()).re for vj in v]
        p = a[0] + a[1] + a[2]
        tr = gram[0][0].re + gram[1][1].re + gram[2][2].re
        e2 = F(0)
        for i, j in ((0, 1), (0, 2), (1, 2)):
            e2 += (gram[i][i] * gram[j][j] - gram[i][j] * gram[j][i]).re
        det = (
            gram[0][0] * (gram[1][1] * gram[2][2] - gram[1][2] * gram[2][1])
            - gram[0][1] * (gram[1][0] * gram[2][2] - gram[1][2] * gram[2][0])
            + gram[0][2] * (gram[1][0] * gram[2][1] - gram[1][1] * gram[2][0])
        )
        if tr != 2 * p or e2 != p * p or det.re != 4 * a[0] * a[1] * a[2] or det.im != 0:
            return False
    return True


@check("p + q = 12 pointwise: one zone function runs both sectors")
def _():
    ts = [F(1, 2), F(1, 3), F(2, 5), F(3, 7), F(5, 9)]
    for t1, t2, t3 in product(ts, repeat=3):
        q = sum(
            ((circle_point(t) - GQ(1)) * (circle_point(t) - GQ(1)).conj()).re for t in (t1, t2, t3)
        )
        p = sum(
            ((circle_point(t) + GQ(1)) * (circle_point(t) + GQ(1)).conj()).re for t in (t1, t2, t3)
        )
        if p + q != 12:
            return False
    return True


@check("high-symmetry spectra: C-odd {0, q, q} and the C-even cubic's roots")
def _():
    # a_m = 2 + 2 cos k_m is 4 at k_m = 0 and 0 at k_m = pi, so both sectors
    # at Gamma, X, M and R are decided by integer arithmetic. Rather than
    # solving the cubic, the claimed roots are substituted into it and pinned
    # by Vieta: three roots summing to 2p with product 4 a1 a2 a3 are ALL of
    # them. lambda = mu - 4 throughout.
    points = {"Gamma": (0, 0, 0), "X": (1, 0, 0), "M": (1, 1, 0), "R": (1, 1, 1)}
    want_q = {"Gamma": 0, "X": 4, "M": 8, "R": 12}
    want_even = {
        "Gamma": [12, 0, 0],
        "X": [4, 4, -4],
        "M": [0, 0, -4],
        "R": [-4, -4, -4],
    }
    for name, pt in points.items():
        a = [0 if k else 4 for k in pt]
        p_zone, abc = sum(a), a[0] * a[1] * a[2]
        if 12 - p_zone != want_q[name]:
            return False
        mus = [lam + 4 for lam in want_even[name]]
        for mu in mus:
            if mu**3 - 2 * p_zone * mu**2 + p_zone**2 * mu - 4 * abc != 0:
                return False
        if sum(mus) != 2 * p_zone or mus[0] * mus[1] * mus[2] != 4 * abc:
            return False
    return True


@check("C-even Gamma splitting A1++ minus E++ is exactly 12 t_+, at both orders")
def _():
    # At Gamma the unsigned adjacency spectrum is {12, 0, 0}: TWO distinct
    # levels, where the signed one is {-4, -4, -4} and has only one. That is
    # why the charge-even rest frame separates the hopping from the leakage
    # exactly where no charge-odd Gamma datum can. Through the assembly
    # E_+(lambda, r) = tower + 12 leak + lambda t_+, the leakage and the tower
    # cancel in the difference and the splitting is (12 - 0) t_+.
    gamma_levels = sorted(set([12, 0, 0]))  # the C-even Gamma spectrum, deduplicated
    gap = max(gamma_levels) - min(gamma_levels)
    if gap != 12 or len(gamma_levels) != 2:
        return False
    for r, t_plus, want in ((2, F(-11, 306), F(-22, 51)), (3, T3_EVEN, F(-6335, 20808))):
        tower, leak = F(13, 20) if r == 2 else F(101, 200), t_plus
        top = tower + 12 * leak + max(gamma_levels) * t_plus
        bottom = tower + 12 * leak + min(gamma_levels) * t_plus
        if top - bottom != gap * t_plus or gap * t_plus != want:
            return False
    return True


# ---------------------------------------------------------------------------
# 8. The fourth-order checkpoint algebra and the obstruction
# ---------------------------------------------------------------------------


def checkpoint_deltas(a, b, c, d):
    """The paper's eq. for Delta at X, M, P, R in the shape basis."""
    return {
        "X": 4 * a,
        "M": 8 * a + 16 * b + 8 * c,
        "P": 6 * a + 8 * b + F(16, 3) * c,
        "R": 12 * a + 48 * b + 16 * c + F(16, 3) * d,
    }


@check("the four extraction formulas invert the checkpoint ansatz")
def _():
    for a, b, c, d in (
        (F(5, 48), F(0), F(-1, 7), F(0)),
        (F(3), F(-2), F(5, 11), F(7, 3)),
        (F(-9, 4), F(13, 5), F(0), F(-1, 6)),
    ):
        dl = checkpoint_deltas(a, b, c, d)
        got = (
            dl["X"] / 4,
            (dl["X"] + 4 * dl["M"] - 6 * dl["P"]) / 16,
            3 * (2 * dl["P"] - dl["M"] - dl["X"]) / 8,
            3 * (dl["R"] - 6 * dl["M"] + 6 * dl["P"]) / 16,
        )
        if got != (a, b, c, d):
            return False
    return True


@check("X is blind to B, C and D: Delta_X = 4A alone")
def _():
    base = checkpoint_deltas(F(5, 48), F(0), F(0), F(0))["X"]
    moved = checkpoint_deltas(F(5, 48), F(9), F(-4), F(11))["X"]
    return base == moved == F(5, 12)


@check("e_2 is the zero polynomial on every axial cut; e_2(M) = 16, e_2(R) = 48")
def _():
    # a_i = 4 sin^2(k_i/2), so on a one-dimensional cut two of the three
    # vanish identically and e_2 = sum_{i<j} a_i a_j vanishes as a polynomial,
    # not merely numerically. The two fourth-order records differ by
    # 4 Delta_C e_2, so no axial or Gamma datum separates them at ANY
    # precision. This is the obstruction; it decides nothing about C_shp and
    # assumes no value for it.
    def e2(a):
        return a[0] * a[1] + a[0] * a[2] + a[1] * a[2]

    axial = all(e2([t, F(0), F(0)]) == 0 for t in (F(1, 3), F(2), F(7, 5), F(4)))
    return axial and e2([F(4), F(4), F(0)]) == 16 and e2([F(4), F(4), F(4)]) == 48


@check("the C_alt witness separates off-axis by 8 and 16 times its shift, and not on-axis")
def _():
    # An explicit second witness recorded in the pinned edition. Its gap to
    # the historical value is exact; the induced band separations follow from
    # the checkpoint formulas alone. Exhibiting a second witness is how
    # non-identifiability is shown by construction rather than argued from a
    # difference -- and it prefers no side of C2.
    shift = F(25, 1024)
    a, b = F(5, 48), F(0)
    old = checkpoint_deltas(a, b, F(0), F(0))
    alt = checkpoint_deltas(a, b, shift, F(0))
    return (
        alt["X"] - old["X"] == 0
        and alt["M"] - old["M"] == 8 * shift == F(25, 128)
        and alt["R"] - old["R"] == 16 * shift == F(25, 64)
    )


# ---------------------------------------------------------------------------
# 9. The coupling convention
# ---------------------------------------------------------------------------


@check("4 Delta(3u/2) reproduces the printed towers, in canonical u")
def _():
    # Delta_s(y) = sum b_{r,s} y^r with the printed b's; the tower is
    # 4 Delta(3u/2). This is the whole content of the coupling erratum: the
    # printed coefficients are already in u = beta_N/(2N).
    b = {"-": (F(1, 18), F(7, 432)), "+": (F(13, 180), F(101, 2700))}
    got = {}
    for s, (b2, b3) in b.items():
        # coefficient of u^r in 4 * b_r * (3u/2)^r
        got[s] = (4 * b2 * F(9, 4), 4 * b3 * F(27, 8))
    return got["-"] == (F(1, 2), F(7, 32)) and got["+"] == (F(13, 20), F(101, 200))


@check("a 4**r rescaling misses the printed towers by exactly 16 and 64")
def _():
    # The archived Y = 2 beta/3 = 4u line is a definition-label erratum.
    # Reading it as a coordinate would demand coefficient_r / 4^r, and the
    # printed table differs from that by exactly 4^r -- which is why the
    # rescaling must never be applied.
    #
    # The first draft of this check was `F(1,2)/(F(1,2)/16) == 16`, which is
    # x/(x/16) = 16 for every nonzero x: a tautology that would pass whatever
    # the towers were. It is now anchored to the towers this file actually
    # builds from the printed b-coefficients, so a wrong tower fails it.
    b = {"-": (F(1, 18), F(7, 432)), "+": (F(13, 180), F(101, 2700))}
    ok = True
    for b2, b3 in b.values():
        printed = (4 * b2 * F(9, 4), 4 * b3 * F(27, 8))
        rescaled = (printed[0] / 4**2, printed[1] / 4**3)
        ok &= printed[0] == 16 * rescaled[0] and printed[1] == 64 * rescaled[1]
        ok &= printed[0] != rescaled[0] and printed[1] != rescaled[1]
    # and the charge-odd tower is the one the paper prints
    return ok and (4 * F(1, 18) * F(9, 4), 4 * F(7, 432) * F(27, 8)) == (F(1, 2), F(7, 32))


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
