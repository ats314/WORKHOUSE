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
    "GLUEBALL §18.3; the sharp form derived here",
    tier=2,
)
def _():
    # Jordan's inequality is tight where it is tight -- k = 0 and the zone
    # CORNER -- and the criterion applies it where it is loosest. What the
    # exclusion radius needs is min{ q(k) : |k| >= r, k in the zone }, and
    # that minimum sits on a coordinate AXIS, where Jordan is loose by
    # pi^2/4 = 2.467. The sharp minimum is elementary:
    #
    #   q(k) = sum_j h(k_j^2)  with  h(t) = 2(1 - cos sqrt t),
    #   h'(t) = sin(sqrt t)/sqrt t = sinc(sqrt t).
    #
    #   phi(s) := s cos s - sin s  has  phi' = -s sin s <= 0 on [0, pi] and
    #   phi(0) = 0, so phi <= 0, so sinc is non-increasing on (0, pi] and h is
    #   CONCAVE on [0, pi^2], with h(0) = 0. Concave through the origin makes
    #   h(t)/t non-increasing, and that finishes it in two cases: if some
    #   t_j >= r^2 then sum h >= h(t_j) >= h(r^2) because h is increasing; and
    #   if every t_j <= r^2 then h(t_j) >= (t_j / r^2) h(r^2), so
    #   sum h >= (sum t_j / r^2) h(r^2) >= h(r^2). Hence
    #
    #       min{ q(k) : |k| >= r } = h(r^2) = 4 sin^2(r/2),
    #
    # attained at t = (r^2, 0, 0) -- a coordinate AXIS, not the corner. The
    # second case is what covers |k|^2 > pi^2, where h(|k|^2) is not even
    # defined, so no case is being waved through.
    #
    # Substituting that for the Jordan bound in theta t_3 u^2 q >= W_4 u^4
    # gives r >= 2 arcsin((u/2) sqrt(W_4/(theta t_3))), whose leading constant
    # is sqrt(W_4/(theta t_3)) -- exactly 2/pi times the Jordan constant. The
    # Jordan statement stays TRUE; it is a valid, loose sufficient radius. The
    # paper may print either, but it should not print the loose one as if it
    # were the criterion.
    #
    # Declared T2, and that UNDERSTATES the verdict, which is exact: every
    # conjunct below is a symbolic identity or an exact rational/pi
    # comparison, and the ratio pi/2 holds for ANY W_4 because
    # crossover_constant rationalises its argument before dividing. The label
    # is T2 because the two printed constants are read off W4_NEW_NUM, which
    # the corpus records only as a float, and the tier guard matches `_NUM`
    # anywhere in the body. Loosening the guard to fit one check is the "make
    # the failing check pass" instinct this repository exists to resist, and
    # understating a tier cannot cause a false promotion -- which is the
    # failure the tier system is for. The sibling crossover checks carry T2
    # for the same reason, so this is also the consistent label.
    #
    # An earlier draft settled the minimum by SAMPLING the zone, which made a
    # float part of the verdict for real. That version would have passed on a
    # wrong minimum the sampler happened not to beat, so it was replaced by
    # the concavity argument rather than relabelled.
    s, t = symbols("s t", positive=True)
    phi = s * cos(s) - sin(s)
    # h(t) = 2(1 - cos sqrt t): its derivative IS sinc(sqrt t), and sinc is
    # non-increasing on (0, pi] exactly because phi <= 0 there.
    h = 2 * (1 - cos(sqrt(t)))
    derivative = simplify(diff(h, t) - sin(sqrt(t)) / sqrt(t)) == 0
    monotone_sinc = simplify(diff(phi, s) + s * sin(s)) == 0 and phi.subs(s, 0) == 0
    through_origin = h.subs(t, 0) == 0

    theta = Rational(1, 2)
    ratios = [
        simplify(G.crossover_constant(w4, theta) / G.exact_crossover_constant(w4, theta))
        for w4 in (K.W4_HISTORICAL_NUM, K.W4_NEW_NUM)
    ]
    sharper = all(r == pi / 2 for r in ratios)

    # Two exact witnesses for the gap, on the axis where the bound is used.
    # At r = pi the two agree (the corner, where Jordan is tight); at r = pi/2
    # the sharp minimum is 2 and Jordan gives 1, a factor of exactly 2.
    def sharp(r):
        return simplify(4 * sin(r / 2) ** 2)

    def jordan(r):
        return simplify(G.JORDAN * r**2)

    agree_at_corner = simplify(sharp(pi) - jordan(pi)) == 0 and sharp(pi) == 4
    loose_on_axis = sharp(pi / 2) == 2 and jordan(pi / 2) == 1

    exact = [
        float(G.exact_crossover_constant(w, theta)) for w in (K.W4_HISTORICAL_NUM, K.W4_NEW_NUM)
    ]
    loose = [float(G.crossover_constant(w, theta)) for w in (K.W4_HISTORICAL_NUM, K.W4_NEW_NUM)]
    ok = derivative and monotone_sinc and through_origin and sharper
    return ok and agree_at_corner and loose_on_axis, (
        "h(t) = 2(1 - cos sqrt t) has h'(t) = sinc(sqrt t), which is non-increasing on "
        "(0, pi] because (s cos s - sin s)' = -s sin s <= 0; h is therefore concave "
        "through the origin, h(t)/t is non-increasing, and the minimum of q over "
        "|k| >= r is 4 sin^2(r/2), on a coordinate axis. The exclusion radius is "
        "2 arcsin((u/2) sqrt(W_4/(theta t_3))), and the Jordan constant is exactly pi/2 "
        f"times the sharp one: {loose[0]:.2f} -> {exact[0]:.2f} and {loose[1]:.2f} -> "
        f"{exact[1]:.2f} at theta = 1/2. The two bounds agree exactly at r = pi (both 4, "
        "the corner) and differ by a factor of 2 at r = pi/2 (2 against 1), which is the "
        "axis the criterion actually uses -- Jordan is not wrong here, only loose"
    )
