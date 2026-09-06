"""Preserved exact control functions.

Source: next_energy_local_score/check_localized_true_ground_score.py.

Original SHA256: be023e2359afbdce45f0bb5c6b42513561dbbd39071557ac3d165583667a9de5
Finite algebra only; analytic hypotheses and limits are not certified here.
"""

from __future__ import annotations

import sympy as s


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ValueError(message)


def cross_matrix(v: s.Matrix) -> s.Matrix:
    return s.Matrix([[0, -v[2], v[1]], [v[2], 0, -v[0]], [-v[1], v[0], 0]])


def controls() -> dict:
    x = s.symbols("x", real=True)
    q = s.Matrix(s.symbols("q1:4", real=True))
    z = s.Matrix(s.symbols("z1:4", real=True))
    a = cross_matrix(q)
    identity = s.eye(3)

    # Order-two Taylor algebra. No nonlinear operator is replaced by it.
    ad_u = identity + x * a + x**2 * a**2 / 2
    ad_u_inverse = identity - x * a + x**2 * a**2 / 2
    c_uu = 8 * identity - ad_u - ad_u_inverse
    require(s.simplify(c_uu - (6 * identity - x**2 * a**2)) == s.zeros(3), "coarse metric")
    c_inverse = identity / 6 + x**2 * a**2 / 36
    b = ((4 * identity - ad_u_inverse) * c_inverse).applyfunc(
        lambda v: s.series(v, x, 0, 3).removeO()
    )
    root_inverse = identity / 2 - x * a / 8
    residual = ((identity - x * a / 2) * (b - root_inverse)).applyfunc(
        lambda v: s.expand(v).coeff(x, 1)
    )
    require(residual == s.Rational(7, 24) * a, "balanced residual coefficient")
    require(a * q == s.zeros(3, 1), "centralizer kernel")

    basis = [identity[:, j] for j in range(3)]
    gaussian_forcing = s.expand(sum(q[j] * q.cross(basis[j]).dot(z) for j in range(3)))
    require(gaussian_forcing == 0, "first scaled forcing does not kill vacuum")
    require(s.simplify(a.T * a - ((q.dot(q)) * identity - q * q.T)) == s.zeros(3), "adjoint Gram")

    horizontal_coefficient = -s.Rational(7, 12) / s.sqrt(5)
    covariance = s.sqrt(5) / 2
    fisher_coefficient = s.simplify(4 * horizontal_coefficient**2 * covariance)
    require(fisher_coefficient == s.Rational(49, 72) / s.sqrt(5), "Fisher normalization")
    weighted_coefficient = s.simplify(6 * fisher_coefficient)
    require(weighted_coefficient == s.Rational(49, 12) / s.sqrt(5), "weighted Fisher normalization")
    require(s.simplify((q.T * (a.T * a) * q)[0]) == 0, "class radial contraction")

    # A noninvariant leading Gaussian does not satisfy the crucial cancellation.
    anisotropic_gradient = s.diag(1, 2, 3) * q
    anisotropic_forcing = s.expand(
        sum(anisotropic_gradient[j] * q.cross(basis[j]).dot(z) for j in range(3))
    )
    values = dict(zip(list(q) + list(z), [1, 1, 0, 0, 0, 1], strict=True))
    witness = anisotropic_forcing.subs(values)
    require(witness != 0, "noninvariant Gaussian negative must be nonzero")

    # The common Gauss sum vanishes, but the two independent fiber variances add.
    q1, q2 = s.Matrix([1, 0, 0]), s.Matrix([0, 1, 0])
    first, second = q1.cross(q2), q2.cross(q1)
    require(first + second == s.zeros(3, 1), "pair profile must obey common Gauss")
    independent_score_variance = first.dot(first) + second.dot(second)
    require(independent_score_variance == 2, "independent scores must not cancel")

    g, coefficient, fast = s.symbols("g coefficient fast", positive=True)
    general_loss = s.simplify((coefficient / 2) / (fast / g**2))
    class_loss = s.simplify((coefficient * g**2 / 2) / (fast / g**2))
    require(general_loss == coefficient * g**2 / (2 * fast), "general Schur exponent")
    require(class_loss == coefficient * g**4 / (2 * fast), "class Schur exponent")

    return {
        "scope": (
            "Exact finite metric/Gaussian/Schur algebra only; "
            "no Wilson ground or analytic remainder certification."
        ),
        "metric": {
            "coarse_constant": 6,
            "balanced_residual_linear_coefficient": "7/24",
            "centralizer_annihilated": True,
        },
        "ground_forcing": {
            "invariant_gaussian_order_g_forcing": 0,
            "noninvariant_gaussian_negative": str(witness),
        },
        "fisher": {
            "conditional_coefficient": str(fisher_coefficient),
            "coarse_metric_weighted_coefficient": str(weighted_coefficient),
            "radial_contraction": 0,
        },
        "common_gauss": {
            "pair_total_gauss": [0, 0, 0],
            "independent_score_variance": int(independent_score_variance),
        },
        "schur": {
            "general_relative_power_g": 2,
            "local_class_relative_power_g": 4,
        },
    }
