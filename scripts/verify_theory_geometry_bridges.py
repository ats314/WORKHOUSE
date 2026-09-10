#!/usr/bin/env python3
"""Exact algebra controls for theory-geometry-and-riccati-bridges.md.

The public ``check_*`` functions return (passed, evidence). They do not write
files, register claims, or infer physical uniformity from finite algebra.
"""

from __future__ import annotations

import json

import sympy as sp


def anisotropy_variance(coordinates):
    """The pair-sum definition, also usable for the dimension counterexample."""
    return sp.expand(
        sum(x * y * (x - y) ** 2 for i, x in enumerate(coordinates) for y in coordinates[i + 1 :])
    )


def check_anisotropy_maximum() -> tuple[bool, str]:
    """Check the complete candidate algebra in the stationary-point proof."""
    a, s = sp.symbols("a s", real=True)
    f = anisotropy_variance([a, a, 1 - 2 * a])
    quadratic = 24 * a**2 - 13 * a + 1
    minus, plus = [(13 + sign * sp.sqrt(73)) / 48 for sign in (-1, 1)]
    maximum = (827 + 73 * sp.sqrt(73)) / 18432
    minimum = (827 - 73 * sp.sqrt(73)) / 18432
    boundary = s * (1 - 4 * s)
    counterexample = anisotropy_variance([sp.Rational(4, 5), *([sp.Rational(1, 15)] * 3)])
    comparisons = [
        sp.diff(f, a) + 2 * (3 * a - 1) * quadratic,
        sp.rem(f - (37 - 73 * a) / 384, quadratic, a),
        sp.simplify(f.subs(a, minus) - maximum),
        sp.simplify(f.subs(a, plus) - minimum),
        f.subs(a, 0),
        f.subs(a, sp.Rational(1, 2)),
        f.subs(a, sp.Rational(1, 3)),
        sp.expand(sp.Rational(1, 16) - boundary - 4 * (s - sp.Rational(1, 8)) ** 2),
        counterexample - sp.Rational(484, 5625),
    ]
    # Exact signs, with positive quantities squared; no floating extrema search.
    upper_rhs = sp.Rational(18432 * 2, 25) - 827
    sign_checks = [
        8**2 < 73 < 9**2,  # both radical stationary points are in (0,1/2)
        827 + 73 * 8 > 18432 // 16,
        sp.Rational(827, 18432) < sp.Rational(1, 16),
        upper_rhs > 0,
        upper_rhs**2 > 73**3,
        counterexample > sp.Rational(2, 25),
    ]
    return all(sp.expand(v) == 0 for v in comparisons) and all(sign_checks), (
        "stationary derivative, both radical values, endpoint and boundary maxima exact; "
        "K3=(827+73*sqrt(73))/18432<2/25; four-coordinate value=484/5625>2/25. "
        "The three-coordinate Lagrange reduction is the accompanying analytic proof."
    )


def check_hodge_secular_and_moments() -> tuple[bool, str]:
    """Expand the actual diagonal-plus-rank-one determinant, not a defined symbol."""
    r1, r2, r3, b, c, xi = sp.symbols("r1 r2 r3 b c xi", real=True)
    vector = sp.Matrix([r1, r2, r3])
    coordinates = [r1**2, r2**2, r3**2]
    q = sum(coordinates)
    e2 = sum(x * y for i, x in enumerate(coordinates) for y in coordinates[i + 1 :])
    e3 = sp.prod(coordinates)
    up = vector * vector.T
    cross = sp.diag(*coordinates) - up
    matrix = b * up + c * cross
    target = xi**3 - b * q * xi**2 + c * (2 * b - c) * e2 * xi - c**2 * (3 * b - 2 * c) * e3
    determinant = (xi * sp.eye(3) - matrix).det()
    residual = sp.expand(determinant - target)
    # A corrupted constant term is a negative control, not another fitted value.
    wrong_target = target + c**2 * e3
    x, y = sp.symbols("x y", real=True)
    angular = [x, y, 1 - x - y]
    mean = sum(z**2 for z in angular)
    second = sum(z**3 for z in angular)
    third = sum(z**4 for z in angular)
    variance = anisotropy_variance(angular)
    central2 = sum(z * (z - mean) ** 2 for z in angular)
    central3 = sum(z * (z - mean) ** 3 for z in angular)
    moments = [
        sp.expand(central2 - variance),
        sp.expand(central3 - (third - 3 * mean * second + 2 * mean**3)),
    ]
    zero_extension = target.subs({r1: 0, r2: 0, r3: 0}) == xi**3
    return (
        residual == 0
        and sp.expand(determinant - wrong_target) != 0
        and moments == [0, 0]
        and zero_extension
    ), (
        "generic six-variable 3x3 determinant residual=0; wrong constant rejected; "
        "second and third centered angular moments exact; q=0 determinant=xi^3. "
        "Physical higher-order coefficients and normalized q=0 carrier are not asserted."
    )


def _zero_matrix(matrix) -> bool:
    return all(sp.cancel(entry) == 0 for entry in matrix)


def source_congruence_residuals() -> dict[str, bool]:
    """Generic symmetric 3x3 blocks, retained dimension two, arbitrary skew K."""
    a11, a12, a22, b1, b2 = sp.symbols("a11 a12 a22 b1 b2", real=True)
    f = sp.symbols("f", nonzero=True)
    k12, k13, k23 = sp.symbols("k12 k13 k23", real=True)
    h = sp.Matrix([[a11, a12, b1], [a12, a22, b2], [b1, b2, f]])
    k = sp.Matrix([[0, k12, k13], [-k12, 0, k23], [-k13, -k23, 0]])
    graph = sp.Matrix([[1, 0], [0, 1], [-b1 / f, -b2 / f]])
    schur = graph.T * h * graph
    first = h * k - k * h
    second = (first * k - k * first) / 2
    force = (first * graph)[2:3, :]
    kg = k * graph
    retained = kg[:2, :]
    cross = k[2:3, :2]
    gamma = kg[2:3, :] + sp.Matrix([[b1 / f, b2 / f]]) * retained
    retained_dot = cross.T * force / f
    d2 = (retained * retained + retained_dot) / 2
    actual2 = graph.T * second * graph - force.T * force / f
    target2 = retained.T * schur * retained + schur * d2 + d2.T * schur
    return {
        "force_ward": _zero_matrix(force - (f * gamma - cross * schur)),
        "first_congruence": _zero_matrix(
            graph.T * first * graph - schur * retained - retained.T * schur
        ),
        "complete_second_congruence": _zero_matrix(actual2 - target2),
        "omitted_exchange_rejected": not _zero_matrix(graph.T * second * graph - target2),
        "frozen_graph_rejected": not _zero_matrix(first[2:3, :2] - force),
    }


def check_source_congruence() -> tuple[bool, str]:
    checks = source_congruence_residuals()
    # Independent exact finite source change, retaining a nonzero graph dressing.
    h = (
        sp.Matrix(
            [
                [4, 1, sp.Rational(1, 2)],
                [1, 3, sp.Rational(1, 3)],
                [sp.Rational(1, 2), sp.Rational(1, 3), 5],
            ]
        )
        - sp.eye(3) / 7
    )
    unitary = sp.Matrix(
        [
            [sp.Rational(3, 5), 0, sp.Rational(-4, 5)],
            [0, 1, 0],
            [sp.Rational(4, 5), 0, sp.Rational(3, 5)],
        ]
    )
    graph = sp.Matrix([[1, 0], [0, 1], [-h[2, 0] / h[2, 2], -h[2, 1] / h[2, 2]]])
    schur = graph.T * h * graph
    changed = unitary.T * h * unitary
    changed_schur = changed[:2, :2] - changed[:2, 2:3] * changed[2:3, :2] / changed[2, 2]
    overlap = graph.T * unitary[:, :2]
    fast_overlap = unitary[2:3, :2]
    inverse_target = overlap.T * schur.inv() * overlap + fast_overlap.T * fast_overlap / h[2, 2]
    checks["finite_resolvent"] = _zero_matrix(changed_schur.inv() - inverse_target)
    return all(checks.values()), (
        "generic noncommuting 2+1 block force and first/second congruence residuals=0; "
        "omitted exchange and frozen graph rejected; independent rational finite source "
        "resolvent identity exact. Unbounded transport and metric norm estimates are separate."
    )


def check_scalar_source_parity() -> tuple[bool, str]:
    """An exact block parity control, with mixed-parity retained negative control."""
    g = sp.symbols("g", real=True)
    parity = sp.diag(1, -1, 1)
    first = sp.Matrix([[0, 2, 0], [2, 0, 3], [0, 3, 0]])
    second = sp.Matrix([[1, 0, 2], [0, 3, 0], [2, 0, 4]])
    h = sp.diag(3, 5, 7) + g * first + g**2 * second + g**3 * first
    scalar_schur = h[0, 0] - (h[:1, 1:] * h[1:, 1:].inv() * h[1:, :1])[0, 0]
    mixed_schur = h[:2, :2] - h[:2, 2:3] * h[2:3, :2] / h[2, 2]
    checks = [
        _zero_matrix(parity * h * parity - h.subs(g, -g)),
        sp.cancel(scalar_schur - scalar_schur.subs(g, -g)) == 0,
        not _zero_matrix(mixed_schur - mixed_schur.subs(g, -g)),
        first != sp.zeros(3),
    ]
    return all(checks), (
        "exact scalar even-source Schur function is even despite nonzero odd full jet; "
        "mixed-parity retained counterexample is not even. Actual scalar-square source "
        "covariance is proved in TG7; this algebra check supplies no g=0 remainder regularity."
    )


def check_riccati_default() -> tuple[bool, str]:
    endpoint_coefficient = sp.Rational(96228, 625000)
    endpoint_bound = sp.Rational(27, 100)
    endpoint_strict = 3 * endpoint_coefficient**2 < endpoint_bound**2
    root_margin = 1 - endpoint_bound - sp.Rational(17, 20) ** 2
    return bool(endpoint_strict and root_margin > 0), (
        "default endpoint 96228*sqrt(3)/625000<27/100 by exact positive-square comparison; "
        "1-27/100-(17/20)^2=3/400>0, hence contraction<3/20 and amplification<20/17. "
        "The generic residual theorem requires both ball memberships and a fixed point."
    )


CHECKERS = {
    "anisotropy_maximum": check_anisotropy_maximum,
    "hodge_secular_and_moments": check_hodge_secular_and_moments,
    "source_congruence": check_source_congruence,
    "scalar_source_parity": check_scalar_source_parity,
    "riccati_default": check_riccati_default,
}


def run_checks() -> dict[str, dict[str, bool | str]]:
    output = {}
    for name, checker in CHECKERS.items():
        passed, evidence = checker()
        output[name] = {"passed": bool(passed), "evidence": evidence}
    return output


if __name__ == "__main__":
    report = run_checks()
    print(json.dumps(report, indent=2))
    raise SystemExit(0 if all(item["passed"] for item in report.values()) else 1)
