from __future__ import annotations

from sympy import (
    Rational,
    cos,
    diff,
    nsimplify,
    pi,
    simplify,
    sin,
    sqrt,
    symbols,
)

from .. import constants as K
from .. import near_gamma as G
from ._core import _suite

# ==========================================================================
near_gamma = _suite("near-Gamma uniformity (G11)")


@near_gamma.check("Jordan bound q(k) >= (4/pi^2)|k|^2 holds on the whole zone", "GLUEBALL §18.3")
def _():
    xs = symbols("xs", real=True)
    diff_expr = 4 * sin(xs / 2) ** 2 - G.JORDAN * xs**2
    # sin'' = -sin <= 0 on [0,pi] so sin is concave and lies above its chord.
    concave = simplify(diff(sin(xs), xs, 2) + sin(xs)) == 0
    samples = [diff_expr.subs(xs, pi * Rational(i, 200)) for i in range(201)]
    never_negative = all(v >= 0 for v in samples)
    tight = simplify(diff_expr.subs(xs, pi)) == 0
    return concave and never_negative and tight, (
        "sin is concave on [0,pi] so it exceeds its chord 2x/pi; substituting "
        "x -> x/2 and squaring gives the bound, with equality at k=0 and at the "
        "zone corner — so the bound is tight, not slack"
    )


@near_gamma.check("t(u) >= t_3 u^2 for u > 0, so the gap bound is safe", "MASTER_THEORY §4.4")
def _():
    # b_3 > 0, so dropping the cubic term can only understate the gap.
    return K.B_3 > 0, f"b_3 = {K.B_3} > 0; t(u) - t_3 u^2 = b_3 u^3 >= 0"


@near_gamma.check("crossover constant K = (pi/2) sqrt(W_4 / (theta t_3))", "GLUEBALL §18.3", tier=2)
def _():
    theta = Rational(1, 2)
    got = G.crossover_constant(K.W4_HISTORICAL_NUM, theta)
    want = (pi / 2) * sqrt(nsimplify(K.W4_HISTORICAL_NUM, rational=True) / (theta * K.T_MINUS_2))
    return simplify(got - want) == 0, f"K_historical(theta=1/2) = {float(got):.4f}"


@near_gamma.check(
    "the criterion survives C2: K depends on the kernel only through sqrt(W_4)",
    "MASTER_THEORY §5.5 / C2",
    tier=2,
)
def _():
    theta = Rational(1, 2)
    k_hist = float(G.crossover_constant(K.W4_HISTORICAL_NUM, theta))
    k_new = float(G.crossover_constant(K.W4_NEW_NUM, theta))
    ratio = k_new / k_hist
    expected = (K.W4_NEW_NUM / K.W4_HISTORICAL_NUM) ** 0.5
    conservative = float(G.conservative_constant(theta))
    return abs(ratio - expected) < 1e-12 and conservative >= max(k_hist, k_new), (
        f"K_hist = {k_hist:.4f}, K_new = {k_new:.4f}, ratio {ratio:.6f} = "
        f"sqrt(W4_new/W4_old); the larger constant {conservative:.4f} bounds both, so "
        "the exclusion radius can be stated now without adjudicating C2"
    )


@near_gamma.check(
    "the statement is non-vacuous only below an explicit coupling",
    "GLUEBALL §18.3",
    tier=2,
)
def _():
    theta = Rational(1, 2)
    u_max = float(G.max_coupling(theta))
    # At u_max the excluded ball exactly fills the inscribed sphere of the zone.
    at_max = G.excluded_zone_fraction(u_max * 1.01, theta)
    return 0 < u_max < 1 and at_max == 1.0, (
        f"K*u < pi requires u < {u_max:.6f} at theta=1/2 "
        f"(u < {float(G.max_coupling(1)):.6f} at theta=1). Above that the excluded "
        "ball covers the zone and the near-Gamma claim says nothing."
    )


@near_gamma.check("excluded zone fraction grows as u^3", "GLUEBALL §18.3", tier=2)
def _():
    f1 = G.excluded_zone_fraction(0.02)
    f2 = G.excluded_zone_fraction(0.04)
    return abs(f2 / f1 - 8) < 1e-9, (
        f"u=0.02 excludes {100 * f1:.2f}%, u=0.04 excludes {100 * f2:.2f}% "
        "— a factor of 8, as a ball volume must"
    )


@near_gamma.check(
    "the exact zone minimum of q on |k| >= r is 4 sin^2(r/2), and Jordan overstates it by pi/2",
    "MASTER edition §9.7 (near-Gamma statement that does not adjudicate)",
)
def _():
    # The exclusion radius was quoted from Jordan's inequality, which is
    # tight at the ZONE CORNER and nowhere the criterion actually uses. The
    # sharp statement is a concavity argument: writing q = sum_m h(k_m^2)
    # with h(t) = 2(1 - cos sqrt t), the identity (s cos s - sin s)' =
    # -s sin s <= 0 makes h concave and increasing on [0, pi^2], so the
    # minimum of q over the simplex |k|^2 >= r^2 sits at a vertex and equals
    # 4 sin^2(r/2) -- attained on a coordinate axis, which is exactly where
    # the fourth-order shape terms are compared. The Jordan constant is
    # therefore pi/2 times too large, and this check records the factor
    # rather than leaving the printed constants unexplained.
    s, tt = symbols("s tt", positive=True)
    # Everything below is decided symbolically. An earlier draft sampled the
    # vertex minimum in floats and declared itself T1, which the repository's
    # own tier guard rejected -- correctly: a bound argued from float
    # comparisons is T2 whatever its inputs look like. The concavity argument
    # settles it exactly and needs no sampling.
    #
    # h(t) = 2(1 - cos sqrt t) is the per-axis contribution, q = sum_m h(k_m^2).
    #   h'(t) = sin(sqrt t) / sqrt t >= 0 on [0, pi^2], since sin >= 0 on
    #     [0, pi]: h is increasing, so the minimum over |k| >= r sits on the
    #     sphere |k| = r.
    #   h''(t) has the sign of (s cos s - sin s) at s = sqrt t, whose
    #     derivative is -s sin s <= 0 on [0, pi]; that expression vanishes at
    #     s = 0, so it is <= 0 throughout and h is CONCAVE there.
    #   A concave function summed over the simplex {x >= 0, sum x = r^2}
    #     attains its MINIMUM at an extreme point, i.e. all the length on one
    #     axis -- and there q = h(r^2) = 4 sin^2(r/2).
    concavity = simplify(diff(s * cos(s) - sin(s), s) + s * sin(s)) == 0
    vanishes_at_zero = simplify((s * cos(s) - sin(s)).subs(s, 0)) == 0
    h = 2 * (1 - cos(sqrt(tt)))
    increasing = simplify(diff(h, tt) - sin(sqrt(tt)) / sqrt(tt)) == 0
    # and the vertex value is the claimed one, exactly
    r = symbols("r", positive=True)
    vertex = simplify(h.subs(tt, r**2) - 4 * sin(r / 2) ** 2) == 0
    vertex = bool(vertex) and concavity and vanishes_at_zero and increasing
    # The relation between the two constants is exact and free of any
    # bandwidth: for ANY W_4, the registered crossover constant is pi/2 times
    # the sharp one, because Jordan's bound understates q on the axis by
    # exactly pi^2/4 and K enters through sqrt(q). Verified with W_4 a free
    # symbol, so no float and no float-valued constant is touched here -- the
    # two recorded numeric constants belong to the T2 check above, which is
    # where the reader should look for values.
    theta, w4 = Rational(1, 2), symbols("W4", positive=True)
    sharp = sqrt(w4 / (theta * K.T_MINUS_2))
    jordan = G.crossover_constant(w4, theta)
    factor = simplify(jordan - (pi / 2) * sharp) == 0
    return concavity and increasing and vertex and factor, (
        "h(t) = 2(1 - cos sqrt t) has h'(t) = sin(sqrt t)/sqrt t >= 0 and is concave on "
        "[0, pi^2] by the identity (s cos s - sin s)' = -s sin s <= 0 with the expression "
        "vanishing at s = 0; a concave sum over the simplex is minimised at a vertex, so "
        "min_{|k| >= r} q(k) = h(r^2) = 4 sin^2(r/2), attained on a coordinate axis. Jordan's "
        "(4/pi^2)|k|^2 is tight only at the zone corner; on the axis it is loose by pi^2/4, so "
        "the sharp crossover constant is sqrt(W_4/(theta t_3)) and the registered Jordan "
        "constant is exactly pi/2 times it -- verified with W_4 a free symbol, so it holds for "
        "either recorded kernel and for any third one. Numerically that turns 17.04 and 23.66 "
        "into 10.85 and 15.06; those values are floats and live in the T2 crossover check, not "
        "here"
    )
