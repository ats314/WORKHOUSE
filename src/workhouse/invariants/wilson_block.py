"""The blocked Wilson transfer: the spectral block, the cluster margin, the source moments
(G18, G19; runs/discrete_time_wilson_2026-09-04, runs/excited_wilson_window_2026-09-04).

Two further packages from the parallel session of 2026-09-04 block the actual Wilson
transfer in physical time: one builds a scalar space-time polymer expansion for its vacuum
and full source correlations, the other asks what an operator-level isolation of the
plaquette window would take. Their analytic content is research-note proof, conditional on
the uniform kinetic window and on the abstract cluster theorem, and is not checked here.
What is checked is their exact arithmetic and their exact linear algebra: the block that
maximizes the guaranteed free separation and the margin it keeps after temporal rounding;
the support-count bound behind the volume-uniform first-derivative estimate; the
Kotecky-Preiss margin 11/56 that the explicit sufficient thresholds leave; and the
source-moment identities that separate motion inside the source span from leakage out of
it, with the dark-state control that shows why positive source weight is not completeness.
"""

from __future__ import annotations

from fractions import Fraction

from sympy import Matrix, Poly, Rational, Symbol, diff, exp, log, simplify, solve

from ._core import _suite

block = _suite("the blocked Wilson transfer: spectral block, cluster margin, source moments")

_RUN_DT = "runs/discrete_time_wilson_2026-09-04"
_RUN_EW = "runs/excited_wilson_window_2026-09-04"
_NOTE_DT = "paper/research_notes/G19_DISCRETE_TIME_VACUUM_AND_WINDOW_20260904.md"
_NOTE_EW = "paper/research_notes/G18_EXCITED_WINDOW_OPERATOR_BRIDGE_20260904.md"

_SPECTRAL_BLOCK = (
    "the spectrally optimal Wilson block: with the shell eigenvalue x^4 and the rest of the odd "
    "spectrum below x^5, x = exp(-gamma s), the guaranteed separation x^4 (1 - x) is maximal at "
    "x = 4/5 with value 256/3125; rounding the block to whole steps of at most s_sp/4 keeps at "
    "least 1024/15625; and the support count 4n x^max(n-4,0) is at most 16 for x <= 4/5, "
    "attained at n = 4 and 5"
)


@block.check(_SPECTRAL_BLOCK, "G18; " + _NOTE_EW + " sections 1 and 4; " + _RUN_EW)
def _():
    # Proposition 1 and Theorem 4 of the excited-window note. The physical free
    # window puts the odd plaquette shell at 4 gamma and everything else at or
    # above 5 gamma, so a block of duration s separates them by at least
    # e^{-4 gamma s} (1 - e^{-gamma s}); the maximizing block is explicit. The
    # factor 16 of the first-derivative bound is four links per plaquette times
    # four plaquettes per link, at the same x = 4/5.
    x = Symbol("x", positive=True)
    g = x**4 * (1 - x)
    x_star = [c for c in solve(diff(g, x), x) if c != 0]
    g_max = g.subs(x, Rational(4, 5))
    gamma = Symbol("gamma", positive=True)
    s_sp = log(Rational(5, 4)) / gamma
    # the worst rounded block, s = s_sp + s_sp/4: e^{-4 gamma s} = (4/5)^5 and
    # 1 - e^{-gamma s} >= 1/5
    at_worst = simplify(exp(-4 * gamma * (s_sp + s_sp / 4)) * (1 - exp(-gamma * s_sp)))
    supports = {n: 4 * n * Rational(4, 5) ** max(n - 4, 0) for n in range(1, 400)}
    peak = max(supports.values())
    ok = (
        x_star == [Rational(4, 5)]
        and g_max == Rational(256, 3125)
        and at_worst == Rational(1024, 15625)
        and peak == 16
        and [n for n, v in supports.items() if v == 16] == [4, 5]
    )
    return (
        ok,
        (
            f"d/dx [x^4 (1 - x)] = 0 at x = {x_star}; g(4/5) = {g_max}; the worst rounded block "
            f"(tau0 = s_sp/4) gives exactly {at_worst} = (4/5)^5 / 5; the support counts "
            f"4n (4/5)^max(n-4,0) peak at {peak} for n = 4 and 5 and fall afterwards, the ratio of "
            "consecutive terms being (n+1)/n * 4/5 < 1"
        ),
        {
            "WILSON_BLOCK_GAP_OPTIMAL": Rational(256, 3125),
            "WILSON_BLOCK_GAP_ROUNDED": Rational(1024, 15625),
        },
    )


_KP_MARGIN = (
    "the explicit sufficient thresholds of the blocked-transfer polymer criterion leave the "
    "Kotecky-Preiss margin 11/56 < 1/4: with delta = e^(-(4+2xi))/16 and y = 1/256 the atom sum "
    "2 e^(4+2xi) delta + 8y/(1 - 144y) is exactly 1/8 + 1/14, and the coupling disc "
    "u_c = log(1 + e^(-(16+8xi)) / (256 (1+delta)^4)) / (J (s0 + tau0)) is where y reaches 1/256"
)


@block.check(_KP_MARGIN, "G19; " + _NOTE_DT + " section 4, eqs. (12)-(15); " + _RUN_DT)
def _():
    # Equations (12)-(15) of the discrete-time note: the temporal bonds contribute
    # 2 e^{4+2xi} delta, the magnetic atoms 8y/(1-144y) with 144^{r-1} connected
    # plaquette sets of size r through a fixed one; the two displayed choices
    # make the sum 11/56, strictly below the 1/4 the rooted-tree induction needs.
    xi = Symbol("xi", positive=True)
    delta = exp(-(4 + 2 * xi)) / 16
    y = Rational(1, 256)
    bonds = simplify(2 * exp(4 + 2 * xi) * delta)
    atoms = 8 * y / (1 - 144 * y)
    total = bonds + atoms
    # the disc: y = e^{16+8xi} (1+delta)^4 b(u) with b(u) = e^{J (s0+tau0) |u|} - 1, solved for |u|
    big_j, s0, tau0, u = (Symbol(n, positive=True) for n in ("J", "s0", "tau0", "u"))
    b_u = exp(big_j * (s0 + tau0) * u) - 1
    y_of_u = exp(16 + 8 * xi) * (1 + delta) ** 4 * b_u
    u_c = log(1 + exp(-(16 + 8 * xi)) / (256 * (1 + delta) ** 4)) / (big_j * (s0 + tau0))
    at_disc = simplify(y_of_u.subs(u, u_c))
    ok = bonds == Rational(1, 8) and atoms == Rational(1, 14) and total == Rational(11, 56)
    ok = ok and total < Rational(1, 4) and at_disc == Rational(1, 256)
    return (
        ok,
        (
            f"temporal bonds {bonds}, magnetic atoms {atoms}, sum {total} < 1/4; "
            f"y(u_c) = {at_disc}; "
            "144 = 12^2 bounds the rooted depth-first traversals of a connected plaquette set "
            "(twelve shared-link neighbours per plaquette, 2(r-1) steps)"
        ),
        {"WILSON_KP_MARGIN": Rational(11, 56)},
    )


def _model():
    """A finite exact model: a symmetric positive contraction D on Q^6 with three eigenvalues
    above 1/2 and three below, and three source vectors J; the blocks A = W* D W, R = Q D W of
    the excited-window note are read off P = J G^-1 J* and Q = 1 - P."""
    rows = [
        [F(7, 10), F(1, 20), 0, F(1, 50), 0, 0],
        [F(1, 20), F(3, 5), F(1, 25), 0, F(1, 100), 0],
        [0, F(1, 25), F(13, 20), 0, 0, F(1, 50)],
        [F(1, 50), 0, 0, F(1, 5), F(1, 40), 0],
        [0, F(1, 100), 0, F(1, 40), F(3, 20), F(1, 60)],
        [0, 0, F(1, 50), 0, F(1, 60), F(1, 10)],
    ]
    D = Matrix([[Rational(q.numerator, q.denominator) for q in r] for r in rows])
    J = Matrix(
        [
            [1, 0, 0],
            [0, 1, 0],
            [0, 0, 1],
            [Rational(1, 5), 0, 0],
            [0, Rational(1, 7), Rational(1, 9)],
            [0, 0, 0],
        ]
    )
    return D, J


F = Fraction

_SOURCE_MOMENTS = (
    "the source-moment identities of the excited-window note hold exactly: with G = J*J and "
    "P = J G^-1 J*, Q = 1 - P, the moments C_j = J* D^j J satisfy J*(D Q D)J = C_2 - C_1 G^-1 C_1 "
    "(the leakage R*R in the source frame) and J*(D - c)^2 J = J*(D - c)P(D - c)J + "
    "J*(D - c)Q(D - c)J "
    "for every scalar c (the split into (A - c)^2 and R*R); a dark state orthogonal to the sources "
    "leaves every C_j unchanged while enlarging the window, so positive source weight is not "
    "completeness"
)


@block.check(_SOURCE_MOMENTS, "G18; " + _NOTE_EW + " sections 6-7, eqs. (19)-(20); " + _RUN_EW)
def _():
    # Section 7 of the excited-window note, checked on an exact rational model
    # rather than believed: the variance around a scalar c splits into the
    # motion inside the source span, (A - c)^2, and the leakage R*R, and the
    # latter is what the three moments determine. Passing to the source frame
    # W = J G^{-1/2} is a congruence by G^{-1/2}, which changes neither
    # equality. The dark-state control is Section 10's finite counterexample.
    D, J = _model()
    n = D.shape[0]
    G = J.T * J
    Ginv = G.inv()
    P = J * Ginv * J.T
    Q = Matrix.eye(n) - P
    C = [J.T * D**j * J for j in range(3)]
    leakage_ok = C[2] - C[1] * Ginv * C[1] == J.T * D * Q * D * J
    c = Symbol("c")
    Dc = D - c * Matrix.eye(n)
    lhs = (J.T * Dc**2 * J).applyfunc(simplify)
    rhs = (J.T * Dc * P * Dc * J + J.T * Dc * Q * Dc * J).applyfunc(simplify)
    split_ok = lhs == rhs
    # the dark state: a seventh basis vector orthogonal to the sources, with its own
    # eigenvalue 2/3 inside the window; the three moments do not move, the window grows
    D7 = Matrix.zeros(n + 1, n + 1)
    D7[:n, :n] = D
    D7[n, n] = Rational(2, 3)
    J7 = Matrix.zeros(n + 1, 3)
    J7[:n, :] = J
    dark_invisible = all(J7.T * D7**j * J7 == C[j] for j in range(3))
    lam = Symbol("lam")
    high = Poly(D.charpoly(lam).as_expr(), lam).count_roots(Rational(1, 2), 1)
    high7 = Poly(D7.charpoly(lam).as_expr(), lam).count_roots(Rational(1, 2), 1)
    positive = all(D[:k, :k].det() > 0 for k in range(1, n + 1))
    contraction = Poly(D.charpoly(lam).as_expr(), lam).count_roots(1, 2) == 0
    ok = leakage_ok and split_ok and dark_invisible and high == 3 and high7 == 4
    ok = ok and positive and contraction
    return ok, (
        f"leakage J*(D Q D)J = C_2 - C_1 G^-1 C_1: {leakage_ok}; the P + Q split of J*(D - c)^2 J "
        f"holds identically in c: {split_ok}; D is positive definite ({positive}) with every "
        f"eigenvalue below 1 ({contraction}) and {high} eigenvalues in [1/2, 1]; the dark state at "
        f"2/3 leaves C_0, C_1, C_2 unchanged ({dark_invisible}) and raises that count to {high7}"
    )
