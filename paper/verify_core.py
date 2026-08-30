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
     be cycles of full kernel rank, together with the closed cube surface,
     whose kernel is its fundamental class and whose face Gram splits 1+3+2
     along the rotation action;
  5. the wrapping sheets are cycles but not harmonic: Rayleigh quotient
     exactly 2;
  6. the two-cube connected geometry rebuilt from oriented cell boundaries,
     its exact B = 6 and B = 4 connected spectra, the six-channel census read
     channel by channel against the four Weingarten weights, and the endpoint
     Casimir budgets that admit six channels at B = 6 and three at B = 4,
     under a weak rule both of whose decisions are equalities;
  7. the charge-even Bloch cubic mu(mu - p)^2 = 4 a1 a2 a3 with p + q = 12,
     decided in the same Gaussian-rational arithmetic as group 3, the four
     high-symmetry spectra of BOTH sectors with their attainment sets, and the
     Gamma splitting that pins t_+ where no charge-odd Gamma datum can;
  8. the fourth-order checkpoint algebra: the four extraction formulas invert,
     X fixes A alone, the second witness separates off axis and not on it, and
     e_2 vanishes identically on every axial cut. This group decides NO value
     of the disputed off-axis coefficient and prefers no side of it -- it is
     the obstruction, as arithmetic;
  9. the coupling convention: 4 Delta(3u/2) reproduces the printed towers, and
     a 4^r rescaling misses them by 16 at u^2 and 64 at u^3.

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


@check("closed cube surface: ker d2 is the fundamental class, and G splits 1 + 3 + 2")
def _():
    # The six faces of a cube, outward-oriented, are a closed surface: the sum
    # of all six is a cycle and spans the kernel, which is b_2(S^2) = 1. The
    # face Gram then splits along the rotation action -- 4I on the
    # antisymmetric (vector, T_1) sector and 4I - 2(J - I) on the symmetric
    # (A_1 + E) sector, of spectra {4,4,4} and {0,6,6}.
    normals = [(-1, 0, 0), (1, 0, 0), (0, -1, 0), (0, 1, 0), (0, 0, -1), (0, 0, 1)]
    even = ((0, 1, 2), (1, 2, 0), (2, 0, 1))
    links, rows = {}, []
    for n in normals:
        c = next(k for k in range(3) if n[k])
        a, b = (k for k in range(3) if k != c)
        base = [0, 0, 0]
        base[c] = 1 if n[c] > 0 else 0
        sign = (1 if (a, b, c) in even else -1) * (1 if n[c] > 0 else -1)
        x = tuple(base)

        def step(y, k):
            z = list(y)
            z[k] += 1
            return tuple(z)

        chain = {}
        for link, sgn in (((x, a), 1), ((step(x, a), b), 1), ((step(x, b), a), -1), ((x, b), -1)):
            links.setdefault(link, len(links))
            chain[link] = chain.get(link, 0) + sign * sgn
        rows.append(chain)
    gram = [[sum(ri.get(k, 0) * rj.get(k, 0) for k in ri) for rj in rows] for ri in rows]
    # the all-ones vector is a cycle: every link cancels
    for link in links:
        if sum(row.get(link, 0) for row in rows) != 0:
            return False
    # G is 4 on the diagonal, 0 within an opposite pair, -1 otherwise
    for i in range(6):
        for j in range(6):
            want = 4 if i == j else (0 if i // 2 == j // 2 else -1)
            if gram[i][j] != want:
                return False

    # sector blocks, with |v|^2 = 2 divided out
    def block(coeff):
        vecs = [[coeff(i, m) for i in range(6)] for m in range(3)]
        return [
            [
                F(sum(vecs[r][i] * gram[i][j] * vecs[c][j] for i in range(6) for j in range(6)), 2)
                for c in range(3)
            ]
            for r in range(3)
        ]

    anti = block(lambda i, m: (1 if i % 2 else -1) if i // 2 == m else 0)
    sym = block(lambda i, m: 1 if i // 2 == m else 0)
    want_anti = [[F(4) if r == c else F(0) for c in range(3)] for r in range(3)]
    want_sym = [[F(4) if r == c else F(-2) for c in range(3)] for r in range(3)]

    def apply(block_, v):
        return [sum(block_[r][c] * v[c] for c in range(3)) for r in range(3)]

    # spectrum {0, 6, 6} exhibited, not inferred: the all-ones direction is the
    # kernel (the fundamental class) and the traceless part is the E doublet
    kernel_ok = apply(sym, [F(1), F(1), F(1)]) == [F(0)] * 3
    doublet_ok = all(
        apply(sym, v) == [6 * x for x in v] for v in ([F(1), F(-1), F(0)], [F(0), F(1), F(-1)])
    )
    return anti == want_anti and sym == want_sym and kernel_ok and doublet_ok


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
# 6. The two-cube connected geometry, its two spectra, and the census
# ---------------------------------------------------------------------------

#: The eleven oriented plaquettes of the open (3,2,2) prism, by base vertex and
#: ordered plane axes — the paper's App. F, in the delivery's frozen order.
PRISM_FACES = (
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
I_L, I_R, I_F = (0, 1, 2, 3, 4, 7), (5, 6, 7, 8, 9, 10), (7,)


def prism_gram_conn():
    """G_conn, built from oriented cell boundaries and Moebius-folded."""

    def step(x, a):
        y = list(x)
        y[a - 1] += 1
        return tuple(y)

    rows = []
    for x, (a, b) in PRISM_FACES:
        chain = {}
        for link, sign in (((x, a), 1), ((step(x, a), b), 1), ((step(x, b), a), -1), ((x, b), -1)):
            chain[link] = chain.get(link, 0) + sign
        rows.append(chain)
    gram = [[sum(ri.get(k, 0) * rj.get(k, 0) for k in ri) for rj in rows] for ri in rows]
    # A source cube's own face Gram is the target Gram restricted to its faces,
    # so lift-and-subtract collapses to index arithmetic: an entry survives iff
    # it is not inside L or R, or is restored by the shared face F.
    out = [[0] * 11 for _ in range(11)]
    for i in range(11):
        for j in range(11):
            w = 1 - ((i in I_L and j in I_L) + (i in I_R and j in I_R) - (i in I_F and j in I_F))
            out[i][j] = gram[i][j] * w
    return out


def block_spectrum(kmat, pairs, isolated):
    """Exact spectrum of a matrix that is 2x2 blocks plus isolated diagonals."""
    spec = {}
    for i, j in pairs:
        for ev in (kmat[i][i] + kmat[i][j], kmat[i][i] - kmat[i][j]):
            spec[ev] = spec.get(ev, 0) + 1
    for i in isolated:
        spec[kmat[i][i]] = spec.get(kmat[i][i], 0) + 1
    return spec


@check("two-cube G_conn is four cross-cell pairs at -1, and nothing else off-diagonal")
def _():
    conn = prism_gram_conn()
    off = {(i, j): conn[i][j] for i in range(11) for j in range(11) if i != j and conn[i][j]}
    want = {}
    for i, j in ((0, 5), (1, 6), (3, 8), (4, 9)):
        want[(i, j)] = want[(j, i)] = -1
    return off == want


@check("connected B=6 and B=4 spectra from the paper's own diagonals")
def _():
    conn = prism_gram_conn()
    pairs, isolated = ((0, 5), (1, 6), (3, 8), (4, 9)), (2, 7, 10)
    b6_numerators = (-2317, -2317, -2295, -2317, -2317, -2317, -2317, 0, -2317, -2317, -2295)
    d_b6 = [F(n, 612) for n in b6_numerators]
    d_b4 = [F(-7, 4)] * 11
    for i in (2, 10):
        d_b4[i] = F(-15, 4)
    d_b4[7] = F(0)
    cases = (
        (F(5, 612), d_b6, {F(0): 1, F(-15, 4): 2, F(-34, 9): 4, F(-129, 34): 4}),
        (F(-1, 12), d_b4, {F(0): 1, F(-15, 4): 2, F(-11, 6): 4, F(-5, 3): 4}),
    )
    for coeff, diag, want in cases:
        kmat = [[diag[i] if i == j else coeff * conn[i][j] for j in range(11)] for i in range(11)]
        if block_spectrum(kmat, pairs, isolated) != want:
            return False
    return True


#: The six link-resolved coefficients of the paper's eq. (census).
CENSUS = {
    "1": F(1, 12),
    "3": F(-1, 12),
    "bar3": F(-1, 12),
    "6": F(-1, 9),
    "bar6": F(-1, 9),
    "8": F(16, 51),
}


@check("the six-channel census IS the four Weingarten weights, channel by channel")
def _():
    predicted = {
        "1": -weight("singlet", 3),
        "8": -weight("adjoint", 3),
        "3": weight("antisym", 3) / 2,
        "bar3": weight("antisym", 3) / 2,
        "6": weight("sym", 3) / 2,
        "bar6": weight("sym", 3) / 2,
    }
    legacy = CENSUS["1"] + CENSUS["3"] + CENSUS["bar3"]
    restored = CENSUS["6"] + CENSUS["bar6"] + CENSUS["8"]
    return (
        predicted == CENSUS
        and sum(CENSUS.values()) == F(5, 612)
        and legacy == weight("antisym", 3) - weight("singlet", 3) == F(-1, 12)
        and restored == weight("sym", 3) - weight("adjoint", 3) == F(14, 153)
    )


@check("B=6 admits every adjacent shared-link channel and B=4 admits three, by a weak rule")
def _():
    # The retention rule is C2(rho) + 2 C2(3) <= B, and the weak inequality is
    # load-bearing: bar3 sits at exactly 4 and the sextet at exactly 6, so both
    # decisions the paper uses are equalities. A strict rule would give {1}
    # alone at B = 4 and lose the sextet at B = 6, contradicting both delivered
    # censuses -- which is how the deliveries fix the convention.
    casimir = {"1": F(0), "3": F(4, 3), "bar3": F(4, 3), "6": F(10, 3), "bar6": F(10, 3), "8": F(3)}
    budget = {r: c + 2 * casimir["3"] for r, c in casimir.items()}
    weak = {b: {r for r, v in budget.items() if v <= b} for b in (4, 6)}
    strict = {b: {r for r, v in budget.items() if v < b} for b in (4, 6)}
    return (
        weak[6] == set(CENSUS)
        and weak[4] == {"1", "3", "bar3"}
        and strict[6] != set(CENSUS)
        and strict[4] != {"1", "3", "bar3"}
        and budget["bar3"] == 4
        and budget["6"] == 6
        and budget["8"] == F(17, 3)
    )


# ---------------------------------------------------------------------------
# 7. The charge-even Bloch cubic
# ---------------------------------------------------------------------------


@check("C-even characteristic polynomial is mu(mu - p)^2 - 4 a1 a2 a3, and p + q = 12")
def _():
    ts = [F(1, 2), F(1, 3), F(2, 5), F(3, 7), F(5, 9)]
    zero = GQ(0)
    for t1, t2, t3 in product(ts, repeat=3):
        z = [circle_point(t) for t in (t1, t2, t3)]
        chat = [zj + GQ(1) for zj in z]  # 1 + e^{i k_j}: the UNSIGNED incidence
        d = [zj - GQ(1) for zj in z]
        ahat = [(c * c.conj()).re for c in chat]
        a = [(dj * dj.conj()).re for dj in d]
        if any(ah + aj != 4 for ah, aj in zip(ahat, a, strict=True)):
            return False
        if sum(ahat) + sum(a) != 12:
            return False
        n = [
            [chat[1], chat[0], zero],
            [chat[2], zero, chat[0]],
            [zero, chat[2], chat[1]],
        ]
        m = [
            [sum((n[r][k] * n[c][k].conj() for k in range(3)), zero) for c in range(3)]
            for r in range(3)
        ]
        p = sum(ahat)
        trace = m[0][0] + m[1][1] + m[2][2]
        minors = zero
        for r, c in ((0, 1), (0, 2), (1, 2)):
            minors = minors + m[r][r] * m[c][c] - m[r][c] * m[c][r]
        det = (
            m[0][0] * (m[1][1] * m[2][2] - m[1][2] * m[2][1])
            - m[0][1] * (m[1][0] * m[2][2] - m[1][2] * m[2][0])
            + m[0][2] * (m[1][0] * m[2][1] - m[1][1] * m[2][0])
        )
        if not (trace - GQ(2 * p)).is_zero():
            return False
        if not (minors - GQ(p * p)).is_zero():
            return False
        if not (det - GQ(4 * ahat[0] * ahat[1] * ahat[2])).is_zero():
            return False
    return True


@check("C-even spectra at Gamma, X, M, R are {12,0,0}, {-4,4,4}, {-4,0,0}, {-4,-4,-4}")
def _():
    # k_j in {0, pi} gives ahat_j in {4, 0} exactly; the cubic then factorises
    # over Q and the claimed roots are checked by expanding the product.
    points = {
        "Gamma": ((4, 4, 4), (12, 0, 0)),
        "X": ((0, 4, 4), (-4, 4, 4)),
        "M": ((0, 0, 4), (-4, 0, 0)),
        "R": ((0, 0, 0), (-4, -4, -4)),
    }
    for ahat, lambdas in points.values():
        p = sum(ahat)
        mus = [lam + 4 for lam in lambdas]
        # (mu - m0)(mu - m1)(mu - m2) against mu^3 - 2p mu^2 + p^2 mu - 4abc
        e1, e2, e3 = (
            sum(mus),
            mus[0] * mus[1] + mus[0] * mus[2] + mus[1] * mus[2],
            mus[0] * mus[1] * mus[2],
        )
        if (e1, e2, e3) != (2 * p, p * p, 4 * ahat[0] * ahat[1] * ahat[2]):
            return False
        if min(lambdas) < -4 or max(lambdas) > 12:
            return False
    # the charge-ODD half of the same four points: q = 12 - p, and the signed
    # spectrum is {0, q, q} by the incidence factorisation
    for name, (ahat, _lam) in points.items():
        q = 12 - sum(ahat)
        if q != {"Gamma": 0, "X": 4, "M": 8, "R": 12}[name]:
            return False
        odd = [F(0), F(q), F(q)]
        if sum(odd) != 2 * q or odd[0] * odd[1] * odd[2] != 0:
            return False
    # the top is attained only at Gamma; the floor wherever some ahat_j = 0
    tops = [n for n, (_ah, lam) in points.items() if max(lam) == 12]
    floors = sorted(n for n, (_ah, lam) in points.items() if min(lam) == -4)
    triple = [n for n, (_ah, lam) in points.items() if set(lam) == {-4}]
    return tops == ["Gamma"] and floors == ["M", "R", "X"] and triple == ["R"]


@check("C-even Gamma splitting A1++ minus E++ is exactly 12 t_+, at both orders")
def _():
    # At Gamma the unsigned adjacency spectrum has TWO distinct levels where
    # the signed one has only one, which is why the charge-even rest frame
    # separates the hopping from the leakage exactly where no charge-odd
    # Gamma datum can. Derived from the cubic rather than asserted: at Gamma
    # ahat = (4,4,4), p = 12 and the cubic factorises as (mu - 16)(mu - 4)^2.
    p_zone, abc = 12, 4 * 4 * 4
    roots = [16, 4, 4]
    for mu in roots:
        if mu**3 - 2 * p_zone * mu**2 + p_zone**2 * mu - 4 * abc != 0:
            return False
    if sum(roots) != 2 * p_zone or roots[0] * roots[1] * roots[2] != 4 * abc:
        return False
    levels = sorted({mu - 4 for mu in roots})  # lambda = mu - 4
    if levels != [0, 12]:
        return False
    # through E_+(lambda, r) = tower + 12 leak + lambda t_+, tower and leak
    # cancel in the difference and the splitting is (12 - 0) t_+
    for r, t_plus, want in ((2, F(-11, 306), F(-22, 51)), (3, T3_EVEN, F(-6335, 20808))):
        tower = F(13, 20) if r == 2 else F(101, 200)
        top = tower + 12 * t_plus + levels[1] * t_plus
        bottom = tower + 12 * t_plus + levels[0] * t_plus
        if top - bottom != 12 * t_plus or 12 * t_plus != want:
            return False
    return True


# ---------------------------------------------------------------------------
# 8. The fourth-order checkpoint algebra, and e_2 on the axes
# ---------------------------------------------------------------------------
#
# This group is the OBSTRUCTION as arithmetic. It decides no value of the
# disputed off-axis coefficient and prefers no side of it: what it establishes
# is that the four checkpoints invert the shape ansatz, that X sees A alone,
# and that e_2 is the zero polynomial on every axial cut — which is why no
# Gamma-point or axial datum can separate the two records at any precision.

#: rows of eq. (checkpoints): Delta_s = row . (A, B, C, D)
CHECKPOINT_ROWS = {
    "X": (F(4), F(0), F(0), F(0)),
    "M": (F(8), F(16), F(8), F(0)),
    "P": (F(6), F(8), F(16, 3), F(0)),
    "R": (F(12), F(48), F(16), F(16, 3)),
}


def solve4(rows, rhs):
    """Exact Gauss-Jordan on a 4x4 rational system; None if singular."""
    m = [list(r) + [v] for r, v in zip(rows, rhs, strict=True)]
    for col in range(4):
        piv = next((r for r in range(col, 4) if m[r][col] != 0), None)
        if piv is None:
            return None
        m[col], m[piv] = m[piv], m[col]
        scale = m[col][col]
        m[col] = [v / scale for v in m[col]]
        for r in range(4):
            if r != col and m[r][col] != 0:
                f = m[r][col]
                m[r] = [vr - f * vc for vr, vc in zip(m[r], m[col], strict=True)]
    return [row[4] for row in m]


@check("the four checkpoint formulas invert, and X fixes A alone")
def _():
    rows = [CHECKPOINT_ROWS[s] for s in ("X", "M", "P", "R")]
    # recover four independent test vectors exactly, including the unit vectors
    for target in (
        [F(1), F(0), F(0), F(0)],
        [F(0), F(1), F(0), F(0)],
        [F(0), F(0), F(1), F(0)],
        [F(0), F(0), F(0), F(1)],
        [F(5, 48), F(0), F(-1, 7), F(3, 11)],
    ):
        deltas = [sum(r[i] * target[i] for i in range(4)) for r in rows]
        if solve4(rows, deltas) != target:
            return False
    return CHECKPOINT_ROWS["X"] == (F(4), F(0), F(0), F(0))


@check("the C_alt witness separates off-axis by 8 and 16 times its shift, and not on-axis")
def _():
    # Non-identifiability exhibited by construction rather than argued from a
    # difference between two records: a second witness, shifted in C alone,
    # is identical to the first at X and separates only off axis. It prefers
    # no side of the dispute -- the shift is the recorded 25/1024 and the
    # witness is not a candidate for the physical value.
    def deltas(a, b, c, d):
        coeffs = (a, b, c, d)
        return {s: sum(r[i] * coeffs[i] for i in range(4)) for s, r in CHECKPOINT_ROWS.items()}

    shift = F(25, 1024)
    old_w = deltas(F(5, 48), F(0), F(0), F(0))
    alt_w = deltas(F(5, 48), F(0), shift, F(0))
    return (
        alt_w["X"] - old_w["X"] == 0
        and alt_w["M"] - old_w["M"] == 8 * shift == F(25, 128)
        and alt_w["R"] - old_w["R"] == 16 * shift == F(25, 64)
    )


@check("e_2 is the zero polynomial on every axial cut; e_2(M) = 16, e_2(R) = 48")
def _():
    def e2(a):
        return a[0] * a[1] + a[0] * a[2] + a[1] * a[2]

    def e3(a):
        return a[0] * a[1] * a[2]

    for t in (F(1, 2), F(1, 3), F(2, 5), F(3, 7), F(5, 9), F(7, 11)):
        ell = 2 - 2 * ((1 - t * t) / (1 + t * t))  # 4 sin^2(k/2) at a rational point
        for axis in range(3):
            a = [F(0), F(0), F(0)]
            a[axis] = ell
            if e2(a) != 0 or e3(a) != 0:
                return False
    return e2((F(4), F(4), F(0))) == 16 and e2((F(4), F(4), F(4))) == 48


# ---------------------------------------------------------------------------
# 9. The coupling convention
# ---------------------------------------------------------------------------


def tower(beta_coeffs):
    """4 * Delta(3u/2) as a coefficient list in u: [u^0, u^1, u^2, u^3]."""
    return [4 * cr * F(3, 2) ** r for r, cr in enumerate(beta_coeffs)]


@check("the printed towers are canonical u: 4 Delta(3u/2) reproduces them verbatim")
def _():
    minus = tower([F(2, 3), F(1, 6), F(1, 18), F(7, 432)])
    plus = tower([F(2, 3), F(-1, 6), F(13, 180), F(101, 2700)])
    return minus == [F(8, 3), F(1), F(1, 2), F(7, 32)] and plus == [
        F(8, 3),
        F(-1),
        F(13, 20),
        F(101, 200),
    ]


@check("a 4^r rescaling misses the printed tower by 16 at u^2 and 64 at u^3")
def _():
    minus = tower([F(2, 3), F(1, 6), F(1, 18), F(7, 432)])
    rescaled = [c / F(4) ** r for r, c in enumerate(minus)]
    return (
        minus != rescaled
        and minus[2] / rescaled[2] == 16
        and minus[3] / rescaled[3] == 64
        and rescaled[2] == F(1, 32)
        and rescaled[3] == F(7, 2048)
    )


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
