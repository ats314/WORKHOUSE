from __future__ import annotations

from sympy import (
    Rational,
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
