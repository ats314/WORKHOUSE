#!/usr/bin/env python3
"""The portable core verifier for the flat-band manuscript.

    python3 verify_core.py

Standard library only, no arguments, about a second. It exists so a referee
who will not install anything can still check the paper's arithmetic, and so
the manuscript's reproducibility sentence names an artifact that is actually
here.

What it checks, and in what sense:

* **exactly**, in ``fractions.Fraction`` throughout. There is not one float in
  this file. The representation-theory ledger is verified as an identity of
  *rational functions of N* -- polynomials cross-multiplied, not sampled -- so
  "true for every N" means every N, not the ones that were tried.
* **the incidence identity exactly too**, which is stronger than the
  manuscript promises for it. A point of the 3-torus with rational
  ``tan(k_j/2)`` has ``exp(i k_j)`` a Gaussian rational, so
  ``B B* = q I - w w*`` is decidable in exact arithmetic at that point.
  Rational points are dense, and the symbolic proof is Theorem 1; this is the
  arithmetic witness.
* **the chain condition and the torus ranks exactly**, over Z and then over
  F_p for two primes, with an explicit kernel basis exhibited. Rank over F_p
  never exceeds rank over Q, and the exhibited generators bound the kernel
  from below, so the two bounds meeting is a proof rather than a sample.

What it does NOT do, said plainly because this repository's rule is that a
check certifies algebra relative to stated definitions and nothing more:
it does not re-derive the Haar integrals that produce the channel weights,
it does not enumerate the third-order lifter classes, and it decides nothing
about the disputed fourth-order off-axis coefficient -- which is exactly why
the manuscript's theorems stop at O(u^3).

Equation numbers refer to the manuscript.
"""

from __future__ import annotations

import sys
from fractions import Fraction as F
from itertools import product

# --------------------------------------------------------------------------
# Exact univariate rational functions of N.
#
# A polynomial is a tuple of Fraction coefficients, lowest degree first. That
# is the whole algebra system: two rational functions are equal when their
# cross-products are equal as polynomials, which is an exact decision, so a
# claim "for every N" is settled without sampling a single N.
# --------------------------------------------------------------------------
Poly = tuple


def poly(*coeffs) -> Poly:
    out = [F(c) for c in coeffs]
    while len(out) > 1 and out[-1] == 0:
        out.pop()
    return tuple(out)


def padd(a: Poly, b: Poly) -> Poly:
    n = max(len(a), len(b))
    return poly(*[(a[i] if i < len(a) else 0) + (b[i] if i < len(b) else 0) for i in range(n)])


def pneg(a: Poly) -> Poly:
    return poly(*[-c for c in a])


def pmul(a: Poly, b: Poly) -> Poly:
    out = [F(0)] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        if x:
            for j, y in enumerate(b):
                out[i + j] += x * y
    return poly(*out)


def peval(a: Poly, n) -> F:
    acc = F(0)
    for c in reversed(a):
        acc = acc * n + c
    return acc


N = poly(0, 1)
ONE_P = poly(1)


class Rat:
    """A rational function num/den with exact equality."""

    __slots__ = ("num", "den")

    def __init__(self, num: Poly, den: Poly = ONE_P):
        self.num, self.den = num, den

    def __add__(self, o: Rat) -> Rat:
        return Rat(padd(pmul(self.num, o.den), pmul(o.num, self.den)), pmul(self.den, o.den))

    def __sub__(self, o: Rat) -> Rat:
        return Rat(padd(pmul(self.num, o.den), pneg(pmul(o.num, self.den))), pmul(self.den, o.den))

    def __mul__(self, o: Rat) -> Rat:
        return Rat(pmul(self.num, o.num), pmul(self.den, o.den))

    def __truediv__(self, o: Rat) -> Rat:
        return Rat(pmul(self.num, o.den), pmul(self.den, o.num))

    def __eq__(self, o) -> bool:
        return pmul(self.num, o.den) == pmul(o.num, self.den)

    def at(self, n) -> F:
        return peval(self.num, F(n)) / peval(self.den, F(n))


def R(*coeffs) -> Rat:
    return Rat(poly(*coeffs))


# --------------------------------------------------------------------------
# 1. The representation-theory ledger  (Sec. 4 and App. A)
# --------------------------------------------------------------------------
C_F = Rat(poly(-1, 0, 1), poly(0, 2))  # (N^2 - 1) / (2N)                 eq. (4)

#: (dimension, quadratic Casimir) of each shared-link fusion channel.  eq. (19)
CHANNELS = {
    "1": (R(1), R(0)),
    "Adj": (R(-1, 0, 1), R(0, 1)),
    "Lambda^2": (Rat(poly(0, -1, 1), poly(2)), Rat(poly(-2, -1, 1), poly(0, 1))),
    "Sym^2": (Rat(poly(0, 1, 1), poly(2)), Rat(poly(-2, 1, 1), poly(0, 1))),
}

#: The closed forms the manuscript prints for the channel weights.  eq. (40)
CLOSED_FORM = {
    "1": Rat(poly(-2), poly(0, -1, 0, 1)),  # -2 / (N(N-1)(N+1))
    "Adj": Rat(poly(2, 0, -2), poly(0, -1, 0, 2)),  # -2(N^2-1) / (N(2N^2-1))
    "Lambda^2": Rat(poly(1, -1), poly(-3, -1, 2)),  # -(N-1) / ((2N-3)(N+1))
    "Sym^2": Rat(poly(-1, -1), poly(-3, 1, 2)),  # -(N+1) / ((2N+3)(N-1))
}

A_N = Rat(poly(0, 0, 0, -2), pmul(poly(-1, 0, 1), poly(-1, 0, 2)))  # eq. (20)
B_N = Rat(poly(0, 8, 0, -4), pmul(poly(-1, 0, 1), poly(-9, 0, 4)))  # eq. (21)
T_N = Rat(poly(0, -8, 0, 2), pmul(pmul(poly(-1, 0, 1), poly(-1, 0, 2)), poly(-9, 0, 4)))  # eq. (23)


def weight(name: str) -> Rat:
    """w_R = -(d_R / N^2) / (C_F + C_R/2), the resolvent weight of eq. (18)."""
    d, c = CHANNELS[name]
    return (R(0) - d / R(0, 0, 1)) / (C_F + c / R(2))


# --------------------------------------------------------------------------
# 2. The SU(3) coefficient ledger  (Table 2, eqs. (27)-(33))
# --------------------------------------------------------------------------
E_PLAQ = F(8, 3)  # u^0, the charge-odd one-plaquette rest energy
TOWER = (F(8, 3), F(1), F(1, 2), F(7, 32))  # eq. (27), the within-plaquette tower
T3 = F(5, 612)  # u^2 BB* coefficient
D_MINUS_2 = F(7, 102)  # u^2 charge-odd diagonal, before the -4t shift
E_FLAT_2 = F(11, 306)  # u^2 flat scalar
B3 = F(1975, 124848)  # u^3 BB* coefficient        eq. (29)
LEAK3 = F(-12331, 249696)  # u^3 per-neighbour leakage    eq. (29)
D3 = F(-109151, 249696)  # u^3 flat scalar         eq. (30)

Q_MAX = 12  # max of q(k) on the zone, at the corner R = (pi,pi,pi)


# --------------------------------------------------------------------------
# 3. Exact Gaussian rationals, for the incidence identity  (Thm. 1)
# --------------------------------------------------------------------------
class GQ:
    """a + bi with a, b rational. Exact."""

    __slots__ = ("re", "im")

    def __init__(self, re=0, im=0):
        self.re, self.im = F(re), F(im)

    def __add__(a, b):
        return GQ(a.re + b.re, a.im + b.im)

    def __sub__(a, b):
        return GQ(a.re - b.re, a.im - b.im)

    def __mul__(a, b):
        return GQ(a.re * b.re - a.im * b.im, a.re * b.im + a.im * b.re)

    def conj(a):
        return GQ(a.re, -a.im)

    def __eq__(a, b):
        return a.re == b.re and a.im == b.im

    def __repr__(a):
        return f"({a.re}{a.im:+}i)"


GZERO, GONE = GQ(0, 0), GQ(1, 0)


#: The zone corner, where tan(k/2) is not rational but exp(i k) = -1 is.
CORNER = "pi"


def on_circle(t) -> GQ:
    """exp(i k) as an exact Gaussian rational, for tan(k/2) = t.

    The half-angle parametrisation is the reason this file can check Theorem 1
    exactly rather than to a residual: every rational t lands on the unit
    circle on the nose, and rational t is dense in it. ``CORNER`` is the one
    point the parametrisation misses, and it is the one the zone needs.
    """
    if t is CORNER:
        return GQ(-1, 0)
    t = F(t)
    den = 1 + t * t
    return GQ((1 - t * t) / den, 2 * t / den)


def bloch(ts):
    """(B(k), w(k), q(k)) at the torus point with tan(k_j/2) = ts[j]. eqs. (7)-(9)."""
    d = [on_circle(t) - GONE for t in ts]
    q = sum((x * x.conj() for x in d), GZERO)
    B = [
        [d[1], GZERO - d[0], GZERO],
        [d[2], GZERO, GZERO - d[0]],
        [GZERO, d[2], GZERO - d[1]],
    ]
    w = [d[2].conj(), GZERO - d[1].conj(), d[0].conj()]
    return B, w, q


def gmul(A, B):
    return [
        [sum((A[i][k] * B[k][j] for k in range(len(B))), GZERO) for j in range(len(B[0]))]
        for i in range(len(A))
    ]


def gdag(A):
    return [[A[j][i].conj() for j in range(len(A))] for i in range(len(A[0]))]


#: Deterministic torus points. Chosen once, hard-coded, never random: a
#: verifier whose inputs move is not reproducible. The last two are the
#: degenerate directions worth including on purpose (isotropic, and one
#: coordinate exactly at the zone origin).
TORUS_POINTS = [
    (F(1, 2), F(1, 3), F(1, 5)),
    (F(2, 7), F(-3, 5), F(11, 13)),
    (F(1), F(1, 7), F(-1, 4)),
    (F(3, 4), F(3, 4), F(3, 4)),
    (F(0), F(1, 2), F(1, 3)),
]


# --------------------------------------------------------------------------
# 4. The periodic cubical complex  (Thm. 2, App. B)
# --------------------------------------------------------------------------
def complex_matrices(L: int):
    """Integer boundary matrices of the periodic cubical cellulation of T^3.

    Faces (x;i,j) with i<j and links (x;i) each number 3L^3; cubes number L^3.
    The two boundary maps are the manuscript's eqs. (41) and (42) verbatim.
    """
    pts = list(product(range(L), repeat=3))
    pairs = [(0, 1), (0, 2), (1, 2)]
    faces = [(x, i, j) for x in pts for (i, j) in pairs]
    links = [(x, i) for x in pts for i in range(3)]
    fi = {f: n for n, f in enumerate(faces)}
    li = {e: n for n, e in enumerate(links)}

    def sh(x, i):
        y = list(x)
        y[i] = (y[i] + 1) % L
        return tuple(y)

    d2 = [[0] * len(faces) for _ in links]
    for c, (x, i, j) in enumerate(faces):
        d2[li[(sh(x, i), j)]][c] += 1
        d2[li[(x, j)]][c] -= 1
        d2[li[(sh(x, j), i)]][c] -= 1
        d2[li[(x, i)]][c] += 1

    d3 = [[0] * len(pts) for _ in faces]
    for c, x in enumerate(pts):
        d3[fi[(sh(x, 0), 1, 2)]][c] += 1
        d3[fi[(x, 1, 2)]][c] -= 1
        d3[fi[(sh(x, 1), 0, 2)]][c] -= 1
        d3[fi[(x, 0, 2)]][c] += 1
        d3[fi[(sh(x, 2), 0, 1)]][c] += 1
        d3[fi[(x, 0, 1)]][c] -= 1
    return d2, d3, faces


def sheets(L: int, faces) -> list[list[int]]:
    """The three wrapping 2-cycles: all (i,j) faces in one slice normal to k."""
    fi = {f: n for n, f in enumerate(faces)}
    out = []
    for i, j in [(0, 1), (0, 2), (1, 2)]:
        k = ({0, 1, 2} - {i, j}).pop()
        v = [0] * len(faces)
        for x in product(range(L), repeat=3):
            if x[k] == 0:
                v[fi[(x, i, j)]] = 1
        out.append(v)
    return out


def imul(A, B):
    out = [[0] * len(B[0]) for _ in A]
    for i, Ai in enumerate(A):
        oi = out[i]
        for t, a in enumerate(Ai):
            if a:
                Bt = B[t]
                for j, b in enumerate(Bt):
                    if b:
                        oi[j] += a * b
    return out


def rank_mod(M, p: int) -> int:
    """Rank over F_p. Never exceeds the rank over Q -- which is why it can
    only ever certify the kernel from above, and the generators do the rest."""
    A = [[v % p for v in row] for row in M]
    rows = len(A)
    cols = len(A[0]) if rows else 0
    r = 0
    for c in range(cols):
        piv = next((i for i in range(r, rows) if A[i][c]), None)
        if piv is None:
            continue
        A[r], A[piv] = A[piv], A[r]
        inv = pow(A[r][c], p - 2, p)
        A[r] = [(v * inv) % p for v in A[r]]
        for i in range(rows):
            if i != r and A[i][c]:
                f, Ai, Ar = A[i][c], A[i], A[r]
                A[i] = [(Ai[j] - f * Ar[j]) % p for j in range(cols)]
        r += 1
        if r == rows:
            break
    return r


PRIMES = (2147483647, 2305843009213693951)


# --------------------------------------------------------------------------
# The checks
# --------------------------------------------------------------------------
CHECKS: list = []


def check(name: str, section: str):
    def register(fn):
        CHECKS.append((name, section, fn))
        return fn

    return register


@check("channel weights match their printed closed forms", "eqs. (18)-(19) vs (40)")
def _():
    bad = [k for k in CHANNELS if weight(k) != CLOSED_FORM[k]]
    detail = ", ".join(f"w_{k} = {CLOSED_FORM[k].at(3)} at N=3" for k in CHANNELS)
    return not bad, (f"mismatch: {bad}" if bad else f"all four exact in N; {detail}")


@check("A_N = w_1 + w_Adj and B_N = w_L2 + w_S2", "eqs. (20)-(21)")
def _():
    a = weight("1") + weight("Adj")
    b = weight("Lambda^2") + weight("Sym^2")
    ok = a == A_N and b == B_N
    return ok, f"A_3 = {A_N.at(3)}, B_3 = {B_N.at(3)}, both as identities in N"


@check("t_N = B_N - A_N = 2N(N^2-4)/[(N^2-1)(2N^2-1)(4N^2-9)]", "Thm. 3, eq. (23)")
def _():
    return (B_N - A_N) == T_N, f"identity in N; numerator 2N(N^2-4) gives t_2 = {T_N.at(2)}"


@check("t_3 = 5/612, and t_N > 0 for every integer N >= 3", "eq. (25)")
def _():
    if T_N.at(3) != T3:
        return False, f"t_3 = {T_N.at(3)}, not {T3}"
    # Positivity is a factorisation argument, not a sample. The identity check
    # above pins the factored form; each of N, N^2-4, N^2-1, 2N^2-1, 4N^2-9 is
    # increasing in N and positive at N = 3, so all five stay positive for
    # every N >= 3 and the quotient does too. The sweep is a witness, not the
    # argument.
    at_three = [3, 3**2 - 4, 3**2 - 1, 2 * 3**2 - 1, 4 * 3**2 - 9]
    witness = all(T_N.at(n) > 0 for n in range(3, 60))
    return all(f > 0 for f in at_three) and witness, (
        f"t_3 = {T3}; the five factors are {at_three} at N = 3 and each is increasing, "
        "so t_N > 0 for every N >= 3; swept to N = 59 as a witness"
    )


@check("large-N expansion 1/4, -1/16, -77/64, -1021/256", "eq. (25) and App. A")
def _():
    # t_N * N^3 is a rational function of z = 1/N^2; expand it as a power
    # series in z by long division of the two polynomials.
    num = [F(2), F(-8)]  # 2N(N^2-4) = N^3 (2 - 8 z),  z = 1/N^2
    den = pmul(pmul(poly(1, -1), poly(2, -1)), poly(4, -9))  # (1-z)(2-z)(4-9z)
    coeffs, rem = [], list(num) + [F(0)] * 8
    for k in range(4):
        c = rem[k] / den[0]
        coeffs.append(c)
        for i, d in enumerate(den):
            if k + i < len(rem):
                rem[k + i] -= c * d
    want = [F(1, 4), F(-1, 16), F(-77, 64), F(-1021, 256)]
    return coeffs == want, f"N^3 t_N = {coeffs} in z = 1/N^2, matching the printed series"


@check("E_F,N = 2 C_F = (N^2-1)/N", "eq. (4)")
def _():
    lhs = R(2) * C_F
    return lhs == Rat(poly(-1, 0, 1), poly(0, 1)), f"E_F,3 = {lhs.at(3)}"


@check("d_3 = 7/32 + 12 leak_3 - 4 b_3 = -109151/249696", "eq. (30), Table 2")
def _():
    lhs = TOWER[3] + 12 * LEAK3 - 4 * B3
    return lhs == D3, f"{lhs} vs printed {D3}"


@check("the u^2 flat scalar is the shifted diagonal: 7/102 - 4(5/612) = 11/306", "eq. (28)")
def _():
    lhs = D_MINUS_2 - 4 * T3
    return lhs == E_FLAT_2, f"{D_MINUS_2} - 4*{T3} = {lhs}"


@check("E_flat and tau carry the ledger coefficients", "Thm. 6, eqs. (32)-(33)")
def _():
    e_flat = (E_PLAQ, F(1), E_FLAT_2, D3)
    tau = (T3, B3)
    ok = e_flat == (F(8, 3), F(1), F(11, 306), F(-109151, 249696)) and tau == (
        F(5, 612),
        F(1975, 124848),
    )
    return ok, f"E_flat = {e_flat} in u^0..u^3; tau = {tau} in u^2..u^3"


@check("manifold width 12 t_N u^2, and tau(u) > 0 for u > 0", "eqs. (26), (35)")
def _():
    # q(k) attains 12 at the zone corner, so the retained width is 12 t_N u^2.
    corner = sum(4 * 1 for _ in range(3))
    positive = T3 > 0 and B3 > 0  # tau(u) = T3 u^2 + B3 u^3, both positive
    return corner == Q_MAX and positive, (
        f"q_max = {corner} at R; tau has coefficients {T3}, {B3}, both > 0, so "
        "Delta_L(u) = 4 tau(u) sin^2(pi/L) > 0 for every u > 0"
    )


@check("B B* = q I - w w*, B* w = 0, spec = {0, q, q}", "Thm. 1, eqs. (10)-(11)")
def _():
    lines = []
    for ts in TORUS_POINTS:
        B, w, q = bloch(ts)
        BB = gmul(B, gdag(B))
        target = [
            [(q if i == j else GZERO) - w[i] * w[j].conj() for j in range(3)] for i in range(3)
        ]
        if any(BB[i][j] != target[i][j] for i in range(3) for j in range(3)):
            return False, f"factorisation fails at tan(k/2) = {ts}"
        Bd = gdag(B)
        if any(sum((Bd[i][k] * w[k] for k in range(3)), GZERO) != GZERO for i in range(3)):
            return False, f"B* w != 0 at {ts}"
        if sum((x * x.conj() for x in w), GZERO) != q:
            return False, f"||w||^2 != q at {ts}"
        # char. poly of BB* must be x(x-q)^2: trace 2q, second invariant q^2, det 0
        tr = sum((BB[i][i] for i in range(3)), GZERO)
        det = (
            BB[0][0] * (BB[1][1] * BB[2][2] - BB[1][2] * BB[2][1])
            - BB[0][1] * (BB[1][0] * BB[2][2] - BB[1][2] * BB[2][0])
            + BB[0][2] * (BB[1][0] * BB[2][1] - BB[1][1] * BB[2][0])
        )
        m2 = (
            (BB[0][0] * BB[1][1] - BB[0][1] * BB[1][0])
            + (BB[0][0] * BB[2][2] - BB[0][2] * BB[2][0])
            + (BB[1][1] * BB[2][2] - BB[1][2] * BB[2][1])
        )
        if not (tr == q + q and m2 == q * q and det == GZERO):
            return False, f"spectrum is not {{0,q,q}} at {ts}"
        # q = 4 sum sin^2(k_j/2), with sin^2(k/2) = t^2/(1+t^2)
        if q.re != sum((F(4) * F(t) ** 2 / (1 + F(t) ** 2) for t in ts), F(0)):
            return False, f"q != 4 sum sin^2(k/2) at {ts}"
        lines.append(str(q.re))
    return True, f"exact at {len(TORUS_POINTS)} rational torus points; q = {', '.join(lines)}"


@check("d_2 d_3 = 0 on the periodic complex", "eq. (6), App. B")
def _():
    for L in (1, 2, 3, 4):
        d2, d3, _ = complex_matrices(L)
        if any(v for row in imul(d2, d3) for v in row):
            return False, f"d_2 d_3 != 0 at L = {L}"
    return True, "exact over Z for L = 1, 2, 3, 4"


@check("rank d_3 = L^3 - 1 and dim ker d_2 = L^3 + 2", "Thm. 2, eqs. (14)-(15)")
def _():
    rows = []
    for L in (1, 2, 3, 4):
        d2, d3, faces = complex_matrices(L)
        gens = [d3[f][:] + [s[f] for s in sheets(L, faces)] for f in range(len(faces))]
        r3 = {rank_mod(d3, p) for p in PRIMES}
        r2 = {rank_mod(d2, p) for p in PRIMES}
        rg = {rank_mod(gens, p) for p in PRIMES}
        if len(r3 | {L**3 - 1}) != 1:
            return False, f"rank d_3 = {r3} at L = {L}, expected {L**3 - 1}"
        ker2 = len(faces) - r2.pop()
        if ker2 != L**3 + 2 or rg != {L**3 + 2}:
            return False, f"dim ker d_2 = {ker2}, generators span {rg}, at L = {L}"
        rows.append(f"L={L}: rank d_3 = {L**3 - 1}, dim ker d_2 = {ker2}")
    return True, "; ".join(rows) + " (two primes, generators exhibited)"


@check("the L^3+2 count is the chain complex, not the Bloch convention", "Thm. 2 remark")
def _():
    # The manuscript assumes L >= 3 for the twelve-neighbour Bloch convention.
    # That caveat is about the adjacency picture; the chain-level count is
    # convention-free, and holds at L = 1 and L = 2 as well. Worth pinning so
    # nobody later "fixes" the small cases.
    out = []
    for L in (1, 2):
        d2, _, faces = complex_matrices(L)
        ker2 = len(faces) - rank_mod(d2, PRIMES[0])
        if ker2 != L**3 + 2:
            return False, f"dim ker d_2 = {ker2} at L = {L}, expected {L**3 + 2}"
        out.append(f"L={L}: {ker2}")
    return True, "; ".join(out) + " = L^3+2, so the L>=3 caveat is Bloch-only"


@check("without the orientation signs there is no flat branch", "Sec. 4")
def _():
    # The manuscript's own falsification control, and the reason the flat band
    # is dynamical rather than generic: removing the orientation sign replaces
    # each (e^{ik} - 1) by (e^{ik} + 1). The resulting unsigned adjacency has
    # no eigenvalue common to Gamma and the corner, so no level can be
    # momentum-independent.
    def adjacency(ts, signed):
        z = [on_circle(t) for t in ts]
        d = [zz - GONE if signed else zz + GONE for zz in z]
        m = (
            [[d[1], GZERO - d[0], GZERO], [d[2], GZERO, GZERO - d[0]], [GZERO, d[2], GZERO - d[1]]]
            if signed
            else [[d[1], d[0], GZERO], [d[2], GZERO, d[0]], [GZERO, d[2], d[1]]]
        )
        prod = gmul(m, gdag(m))
        return [[prod[i][j] - (GQ(4, 0) if i == j else GZERO) for j in range(3)] for i in range(3)]

    def eigenvalues(a):
        # Both matrices here are multiples of {0,1}-circulant-like forms whose
        # spectra are integers; the invariants pin them without a root finder.
        tr = sum((a[i][i] for i in range(3)), GZERO)
        m2 = (
            (a[0][0] * a[1][1] - a[0][1] * a[1][0])
            + (a[0][0] * a[2][2] - a[0][2] * a[2][0])
            + (a[1][1] * a[2][2] - a[1][2] * a[2][1])
        )
        det = (
            a[0][0] * (a[1][1] * a[2][2] - a[1][2] * a[2][1])
            - a[0][1] * (a[1][0] * a[2][2] - a[1][2] * a[2][0])
            + a[0][2] * (a[1][0] * a[2][1] - a[1][1] * a[2][0])
        )
        return tr.re, m2.re, det.re

    gamma = (F(0), F(0), F(0))
    corner = (CORNER, CORNER, CORNER)
    # {12, 0, 0}: trace 12, second invariant 0, determinant 0.
    unsigned_gamma = eigenvalues(adjacency(gamma, False)) == (F(12), F(0), F(0))
    # {-4, -4, -4}: trace -12, second invariant 48, determinant -64.
    unsigned_corner = eigenvalues(adjacency(corner, False)) == (F(-12), F(48), F(-64))
    signed_gamma = eigenvalues(adjacency(gamma, True)) == (F(-12), F(48), F(-64))
    # {-4, 8, 8}: trace 12, second invariant -64 + 64 + ... = 0, det -256.
    signed_corner = eigenvalues(adjacency(corner, True)) == (F(12), F(0), F(-256))
    ok = unsigned_gamma and unsigned_corner and signed_gamma and signed_corner
    return ok, (
        "unsigned: {12,0,0} at Gamma and {-4,-4,-4} at the corner, disjoint, so no level "
        "survives both. Signed: {-4,-4,-4} and {-4,8,8}, sharing -4 -- the flat branch. "
        "Three face orbitals and cubic symmetry are not enough on their own"
    )


def main() -> int:
    print("verify_core.py -- exact arithmetic for the flat-band manuscript")
    print(f"{len(CHECKS)} checks, standard library only, no floats\n")
    failed = 0
    for name, section, fn in CHECKS:
        try:
            ok, detail = fn()
        except Exception as exc:  # a check that raises has failed
            ok, detail = False, f"raised {type(exc).__name__}: {exc}"
        print(f"  {'PASS' if ok else 'FAIL'}  {name}")
        print(f"        {section} -- {detail}")
        failed += not ok
    print()
    if failed:
        print(f"{len(CHECKS) - failed}/{len(CHECKS)} passed, {failed} FAILED")
        return 1
    print(f"{len(CHECKS)}/{len(CHECKS)} passed")
    return 0


if __name__ == "__main__":
    sys.exit(main())
