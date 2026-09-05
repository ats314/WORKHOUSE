"""Live exact finite-model checks for the local Wilson vacuum chart (G18).

These checks reconstruct transfer coefficients using the current oracle. They
check finite matrix identities and the rational support bound; the analytic
arbitrary-order induction and its untruncated scope remain research-note results.
"""

from __future__ import annotations

from sympy import Rational, Symbol, simplify

from ..wilson_vacuum_chart import (
    embed_local,
    product_chart,
    spectator_kinetic,
    support_majorants,
    two_level_negative_control,
)
from ._core import _suite

chart_suite = _suite("the local Wilson vacuum chart: exact quadratic repair and support bound")
_NOTE = "paper/research_notes/G18_SECOND_ORDER_WILSON_VACUUM_CHART_20260905.md"


@chart_suite.check(
    "the local vacuum chart repairs a genuine quadratic creation term: the two-level "
    "symmetric transfer leaves 97/96 after the first rotation, and the exact second "
    "generator 97/24 cancels it on both vacuum legs",
    "G18; " + _NOTE + " sections 4 and 8; finite exact two-level model",
)
def _():
    data = two_level_negative_control()
    coefficient = data["model"].second_rotated[(2,)]
    ok = (
        data["first_chart_residual"] == Rational(97, 96)
        and data["second_generator"] == data["predicted_generator"] == Rational(97, 24)
        and coefficient == coefficient.H
        and coefficient[:, 0].is_zero_matrix
        and coefficient[0, :].is_zero_matrix
    )
    return ok, (
        f"live symmetric-transfer expansion: first-chart quadratic vacuum creation "
        f"{data['first_chart_residual']}; independently stated local generator formula "
        f"{data['predicted_generator']}; final two vacuum legs vanish exactly. "
        "This is a finite-model algebra check, not convergence of the nonlinear chart."
    )


@chart_suite.check(
    "local quadratic chart coefficients retain overlapping and disjoint support structure: "
    "connected generators are block-power invariant, disjoint coefficients factor, and "
    "free spectator entries remain present",
    "G18; " + _NOTE + " sections 5 and 7; exact finite product-transfer models",
)
def _():
    ratio = Rational(4, 5)
    supports = ((0, 1), (1, 2))
    one = product_chart(3, supports, ratio, steps=1)
    two = product_chart(3, supports, ratio, steps=2)
    outside = product_chart(4, supports, ratio, steps=2)
    anchored = all(
        coefficient == coefficient.H
        and coefficient[:, 0].is_zero_matrix
        and coefficient[0, :].is_zero_matrix
        for degree, coefficient in two.second_rotated.items()
        if sum(degree)
    )
    local = (
        one.first_generators == two.first_generators
        and one.second_generators == two.second_generators
        and not two.first_rotated[(1, 1)][:, 0].is_zero_matrix
        and all(
            outside.second_rotated[degree]
            == embed_local(coefficient, (0, 1, 2), 4) * spectator_kinetic(4, (0, 1, 2), ratio**2)
            for degree, coefficient in two.second_rotated.items()
        )
    )
    disjoint = product_chart(4, ((0, 1), (2, 3)), ratio, steps=2)
    single = product_chart(2, ((0, 1),), ratio, steps=2)
    first = single.first_rotated[(1,)]
    factor = (
        disjoint.second_rotated[(1, 1)]
        == embed_local(first, (0, 1), 4) * embed_local(first, (2, 3), 4)
        and disjoint.second_generators[(1, 1)].is_zero_matrix
        and disjoint.eigenvalue_second[(1, 1)] == 0
    )
    return anchored and local and factor, (
        f"exact two-/three-/four-site models: both vacuum legs anchored={anchored}; "
        f"same generators at blocks m=1,2 and every spectator entry retained={local}; "
        f"disjoint coefficient equals the product of the local first coefficients={factor}. "
        "Local and global expansions share the coefficient engine; these are structural controls."
    )


@chart_suite.check(
    "the complete quadratic support majorant is 40432/5: repeated, overlapping and "
    "disjoint activity counts have exact maxima 16, 336 and 2592/5 for delta <= 4/5",
    "G18; " + _NOTE + " section 6; rational arithmetic and decreasing-tail induction",
)
def _():
    # These finite ranges include every possible peak. The exact ratios below
    # prove that each remaining tail decreases; a finite scan alone would not.
    samples = [support_majorants(n) for n in range(1, 11)]
    maxima = tuple(max(row[j] for row in samples) for j in range(3))
    tail_ratios = (
        Rational(6, 5) * Rational(4, 5),
        Rational(8, 7) * Rational(4, 5),
        Rational(10, 9) ** 2 * Rational(4, 5),
    )
    coefficient = 11 * maxima[0] + 22 * maxima[1] + maxima[2]
    ok = (
        maxima == (16, 336, Rational(2592, 5))
        and all(r < 1 for r in tail_ratios)
        and coefficient == Rational(40432, 5)
    )
    return (
        ok,
        f"maxima={maxima}; subsequent-term ratio bounds={tail_ratios}, all below one; "
        f"11*16 + 22*336 + 2592/5 = {coefficient}. This is the coefficient multiplying "
        "f_*^2 in the analytic operator bound, not a physical hopping coefficient.",
        {"WILSON_CHART_QUADRATIC_SUPPORT_FACTOR": coefficient},
    )


@chart_suite.check(
    "the endpoint-gauge mixed-kick identity is exact: r_tau(E1+E2) times "
    "(r_tau(E1)+r_tau(E2)+tau) equals r_tau(E1)r_tau(E2); omitting the mixed "
    "exponential kick leaves the nonzero residual -tau^2/(xy-1)",
    "G18; paper/research_notes/G18_WILSON_ENDPOINT_GAUGE_AND_MAJORANT_20260905.md "
    "section 4, equation (11); rational algebra after x=exp(tau E1), y=exp(tau E2)",
)
def _():
    # The physical substitution has x,y>1 and tau>0. Rational simplification
    # is performed on the common nonzero-denominator domain, without an
    # approximation to either exponential or a spectral norm assertion.
    x, y, tau = (Symbol(name, positive=True) for name in ("x", "y", "tau"))
    r1, r2, r12 = tau / (x - 1), tau / (y - 1), tau / (x * y - 1)
    complete = simplify(r12 * (r1 + r2 + tau) - r1 * r2)
    omitted = simplify(r12 * (r1 + r2) - r1 * r2)
    expected = -(tau**2) / (x * y - 1)
    witness = omitted.subs({x: 2, y: 3, tau: Rational(1, 5)})
    ok = complete == 0 and simplify(omitted - expected) == 0 and witness == -Rational(1, 125)
    return ok, (
        f"complete rational residual={complete}; omitted mixed kick gives {omitted}; "
        f"at x=2,y=3,tau=1/5 the exact negative-control residual is {witness}. "
        "This checks the endpoint identity only. The resolvent-composed rooted contraction "
        "is proved analytically in G18_ROOTED_WILSON_CONTRACTION_20260905.md; "
        "the unrestricted undamped same-weight proposal fails for disjoint active families."
    )
