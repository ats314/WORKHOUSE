"""Reconstruct exact source-current controls; default output is stdout only.

The finite polynomial controls do not certify the finite-g Wilson remainder,
unbounded-domain closure, physical reconstruction, or continuum passage.
"""

from __future__ import annotations

import hashlib
import json
from functools import cache, lru_cache
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
SCHEMA = "workhouse-source-current-bridges/v1"
SQUARE = "runs/recent_research_integration_2026-09-09/sources/w6_square_block_20260909"
SOURCES = (
    f"{SQUARE}/source.md",
    f"{SQUARE}/graph.md",
    f"{SQUARE}/residual_inverse.md",
    f"{SQUARE}/residual_all_energy.md",
    "paper/research_notes/G19_GROUND_MARGINAL_SCHUR_SCORE_20260905.md",
    "paper/research_notes/G19_TRUE_GROUND_LOCALIZED_WILSON_SCORE_20260905.md",
    "docs/derivations/source-currents-and-spectral-totality.md",
    "scripts/verify_source_current_bridges.py",
)


def cross_matrix(x):
    return sp.Matrix([[0, -x[2], x[1]], [x[2], 0, -x[0]], [-x[1], x[0], 0]])


def zero(value):
    if isinstance(value, sp.MatrixBase):
        return all(sp.simplify(entry) == 0 for entry in value)
    return sp.simplify(value) == 0


@lru_cache(maxsize=1)
def square_data():
    r2, r6 = sp.sqrt(2), sp.sqrt(6)
    vectors = [sp.Matrix(sp.symbols(f"{name}0:3", real=True)) for name in ("q", "u", "s", "v")]
    q, u, s, v = vectors
    y = sp.Matrix.vstack(*vectors)
    a = q.dot(q)
    triple = q.dot(u.cross(s))
    aa, bb, cc, dd = (2 * r2 - 1) / 7, (r2 - 4) / 14, (4 - r2) / 7, r2 / 4
    m0 = sp.diag(*([4] * 3 + [2] * 3 + [8] * 3 + [3] * 3))
    precision = sp.diag(*([r2 / 4] * 3 + [1] * 3 + [sp.Rational(1, 4)] * 3 + [r6 / 3] * 3))
    m1 = sp.zeros(12)
    for i, j, block in (
        (0, 1, aa * cross_matrix(s)),
        (1, 2, bb * cross_matrix(q)),
        (0, 2, cc * cross_matrix(q)),
        (0, 3, dd * cross_matrix(q)),
        (1, 3, -dd * cross_matrix(u)),
    ):
        m1[3 * i : 3 * i + 3, 3 * j : 3 * j + 3] = block
        m1[3 * j : 3 * j + 3, 3 * i : 3 * i + 3] = block.T
    polynomial = (
        aa
        * (
            2 * s.dot(s)
            - r2 / 4 * (a * s.dot(s) - q.dot(s) ** 2)
            - (u.dot(u) * s.dot(s) - u.dot(s) ** 2)
        )
        + bb * (2 * a - (a * u.dot(u) - q.dot(u) ** 2) - (a * s.dot(s) - q.dot(s) ** 2) / 4)
        + cc * (-2 * q.dot(u) + (q.dot(u) * s.dot(s) - q.dot(s) * u.dot(s)) / 4)
        + dd * r6 / 3 * (2 * q.dot(u) * v.dot(s) - q.dot(s) * v.dot(u) - u.dot(s) * v.dot(q))
    )
    return {
        "vectors": vectors,
        "y": y,
        "a": a,
        "T": triple,
        "A": aa,
        "B": bb,
        "C": cc,
        "D": dd,
        "M0": m0,
        "M1": m1,
        "precision": precision,
        "P": polynomial,
        "V": a * s.dot(s) - q.dot(s) ** 2 - triple**2,
    }


def gradient(expression, variables):
    return sp.Matrix([sp.diff(expression, variable) for variable in variables])


def transported_operator(expression):
    data = square_data()
    y = data["y"]
    flux = data["M1"] * gradient(expression, y)
    divergence = sum(sp.diff(flux[i], y[i]) for i in range(12))
    return sp.expand(-divergence / 2 + (data["precision"] * y).dot(flux))


@lru_cache(maxsize=1)
def cometric_and_operator_control():
    data = square_data()
    r2 = sp.sqrt(2)
    original = sp.Matrix([[4, -1, 3, -1], [-1, 4, -1, 3], [3, -1, 6, -2], [-1, 3, -2, 6]])
    transform = sp.Matrix(
        [
            [0, 0, 1 / r2, 1 / r2],
            [1 / r2, 1 / r2, -1 / (2 * r2), -1 / (2 * r2)],
            [0, 0, 1 / r2, -1 / r2],
            [1 / r2, -1 / r2, -1 / (2 * r2), 1 / (2 * r2)],
        ]
    )
    metric_defect = transform * original * transform.T - sp.diag(4, 2, 8, 3)
    divergences = [
        sum(sp.diff(data["M1"][i, j], data["y"][i]) for i in range(12)) for j in range(12)
    ]
    first_defect = sp.expand(transported_operator(data["T"]) - data["P"])
    second_defect = sp.expand(
        transported_operator(data["T"] * data["a"])
        - data["P"] * data["a"]
        - 2 * data["A"] * data["V"]
    )
    radial_gradient = gradient(data["a"], data["y"])
    second_radial_symbol = sp.expand(radial_gradient.dot(data["M1"] * radial_gradient))
    return {
        "passed": zero(metric_defect)
        and zero(data["M1"] - data["M1"].T)
        and all(zero(item) for item in divergences)
        and zero(first_defect)
        and zero(second_defect)
        and zero(second_radial_symbol),
        "scope": "Actual-square cometric and complete physical Q12 radial differential action",
        "mode_cometric": [4, 2, 8, 3],
        "operator_defects": [str(first_defect), str(second_defect)],
        "second_radial_symbol": str(second_radial_symbol),
        "column_divergences": list(map(str, divergences)),
    }


@cache
def gaussian_monomial(exponent, variance):
    if exponent % 2:
        return sp.Integer(0)
    return sp.factorial2(exponent - 1) * variance ** (exponent // 2) if exponent else sp.Integer(1)


def gaussian_integral(polynomial, variables, variances):
    result = sp.Integer(0)
    for exponents, coefficient in sp.Poly(sp.expand(polynomial), variables).terms():
        result += coefficient * sp.prod(
            gaussian_monomial(exponent, variance)
            for exponent, variance in zip(exponents, variances, strict=True)
        )
    return sp.expand(result)


@lru_cache(maxsize=2)
def current_moment_control(include_v=True):
    """Wick-reconstruct the current; include_v=False is a deliberate negative control."""
    data = square_data()
    q, u, s, v = data["vectors"]
    radial, psi, derivative = sp.symbols("r psi derivative", real=True)
    a = sp.Symbol("a", positive=True)
    grad = gradient(data["T"], data["y"]) * psi
    grad[:3, 0] += 2 * q * data["T"] * derivative
    flux = data["M1"] * grad
    count = 12 if include_v else 9
    squared = sum(flux[i] ** 2 / (2 * data["M0"][i, i]) for i in range(count))
    # Simultaneous rotational invariance permits this orientation after the
    # full operator/current have been constructed in all twelve coordinates.
    squared = squared.subs({q[0]: radial, q[1]: 0, q[2]: 0})
    variables = list(u) + list(s) + list(v)
    variances = [sp.Rational(1, 2)] * 3 + [sp.Integer(2)] * 3 + [sp.sqrt(6) / 4] * 3
    moment = gaussian_integral(squared, variables, variances)
    moment = sp.Poly(moment, radial)
    if any(exponent[0] % 2 for exponent, _ in moment.terms()):
        raise AssertionError("Rotational scalar current unexpectedly has an odd radial term")
    moment = sp.expand(
        sum(coefficient * a ** (exponent[0] // 2) for exponent, coefficient in moment.terms())
    )
    pp = sp.simplify(moment.coeff(psi, 2))
    pt = sp.simplify(moment.coeff(psi, 1).coeff(derivative, 1))
    tt = sp.simplify(moment.coeff(derivative, 2))
    density_derivative = 1 / (2 * a) - 1 / (2 * sp.sqrt(2))
    integrated = sp.simplify(pp - (sp.diff(pt, a) + pt * density_derivative) / 2)
    ca, cd = (9 - 4 * sp.sqrt(2)) / 49, (159 + 11 * sp.sqrt(2)) / 196
    defects = [sp.simplify(integrated - ca * a**2 / 4 - cd * a), sp.simplify(tt - 16 * ca * a**2)]
    return {
        "passed": all(zero(item) for item in defects),
        "scope": "Exact first-current Gaussian moments and radial integration by parts",
        "includes_v_current": include_v,
        "before_radial_ibp": list(map(str, (pp, pt, tt))),
        "after_radial_ibp": list(map(str, (integrated, tt))),
        "defects": list(map(str, defects)),
    }


def quadratic_radical_interval(expression):
    """An exact rational enclosure in Q(sqrt(2)), without a float sign test."""
    radical = sp.sqrt(2)
    expression = sp.expand(sp.radsimp(expression))
    coefficient = expression.coeff(radical)
    constant = sp.simplify(expression - coefficient * radical)
    if not coefficient.is_Rational or not constant.is_Rational:
        raise ValueError("Expected a rational affine expression in sqrt(2)")
    lo, hi = sp.Rational(1414213, 1000000), sp.Rational(1414214, 1000000)
    if not lo**2 < 2 < hi**2:
        raise AssertionError("Invalid radical enclosure")
    left, right = (lo, hi) if coefficient >= 0 else (hi, lo)
    return sp.factor(constant + coefficient * left), sp.factor(constant + coefficient * right)


@lru_cache(maxsize=1)
def radial_budget_control():
    r = sp.sqrt(2)
    ca, cd, delta, m = (9 - 4 * r) / 49, (159 + 11 * r) / 196, (2 - 4 * r) / 7, 4 + r
    theta = sp.Rational(1, 12)
    astar, dstar = cd + 15 * r * ca / 11, 58 * ca / 11
    # I <= (5sqrt(2) N + (8/theta) G)/(1-theta).
    coefficient_n = cd + ca * 5 * r / (4 * (1 - theta))
    coefficient_g = 16 * ca + ca * 2 / (theta * (1 - theta))
    kstar = sp.simplify(delta**2 * astar / (8 * m**2))
    c0 = sp.simplify(delta**2 / (4 * m))
    sign_expressions = {
        "cA": ca,
        "cD": cd,
        "Astar": astar,
        "dstar": dstar,
        "spectral_monotonicity_margin": 2 * astar - dstar * m,
        "rational_bound_margin": sp.Rational(1, 840) - kstar,
    }
    enclosures = {
        name: quadratic_radical_interval(value) for name, value in sign_expressions.items()
    }
    x = sp.Symbol("x", nonnegative=True)
    spectral_derivative = sp.diff((astar + dstar * x) / (m + x) ** 2, x)
    derivative_defect = sp.simplify(
        spectral_derivative - (dstar * m - 2 * astar - dstar * x) / (m + x) ** 3
    )
    return {
        "passed": zero(coefficient_n - astar)
        and zero(coefficient_g - 8 * dstar)
        and zero(derivative_defect)
        and all(bounds[0] > 0 for bounds in enclosures.values())
        and zero(c0 - (44 - 25 * r) / 686),
        "scope": "Scalar radial Young and joint spectral budget for the complete first current",
        "Kstar": str(sp.radsimp(kstar)),
        "Kstar_decimal": str(sp.N(kstar, 25)),
        "C0": str(sp.radsimp(c0)),
        "positive_rational_enclosures": {
            name: list(map(str, bounds)) for name, bounds in enclosures.items()
        },
    }


def residual_and_centering_control():
    g = sp.Symbol("g", real=True)
    a0 = sp.diag(2, 3)
    ag = sp.Matrix([[2 + g, g], [g, 3 + g]])
    t = sp.Matrix([1, 2])
    u0, wg = a0.inv() * t, ag.inv() * t
    residual = ag * u0 - t
    s0, sg = t.dot(u0), t.dot(wg)
    testing_defect = sp.simplify(residual.dot(wg) - (s0 - sg))
    # Differentiate P r=0 for an actual rotating rank-one projection.
    c, s = sp.cos(g), sp.sin(g)
    vacuum, fast = sp.Matrix([c, s]), sp.Matrix([-s, c])
    projection = vacuum * vacuum.T
    dp = projection.diff(g)
    connection = dp * projection - projection * dp
    derivative_defect = sp.simplify(projection * (fast.diff(g) - connection * fast))
    # Gaussian D*=x-d/dx: the coefficient derivative is indispensable.
    x = sp.Symbol("x", real=True)
    coefficient, current = x**2 + 1, x + 2
    adjoint_current = x * current - sp.diff(current, x)
    product_defect = sp.expand(
        coefficient * adjoint_current
        - (x * coefficient * current - sp.diff(coefficient * current, x))
        - current * sp.diff(coefficient, x)
    )
    z, y, e = sp.symbols("z y e", nonnegative=True)
    # If z^2-y^2<=ez and z>y+e, this identity gives a contradiction.
    square_defect = sp.expand((z**2 - y**2 - e * z) - ((z - y - e) * (z + y) + e * y))
    return {
        "passed": zero(testing_defect)
        and zero(derivative_defect)
        and zero(product_defect)
        and zero(square_defect)
        and not zero(current * sp.diff(coefficient, x)),
        "scope": "Finite inverse testing and exact projection/product centering algebra",
        "inverse_testing_defect": str(testing_defect),
        "omitted_product_term": str(current * sp.diff(coefficient, x)),
        "projection_motion_defect": list(map(str, derivative_defect)),
    }


def variational_completion_control():
    coupling, current, image = sp.symbols("g j y", real=True)
    kappa = sp.Symbol("kappa", positive=True)
    defect = sp.expand(
        coupling**2 * current**2 / kappa
        - (2 * coupling * current * image - kappa * image**2)
        - (coupling * current - kappa * image) ** 2 / kappa
    )
    # A genuine kernel is permitted in the variational ingredient. This
    # matrix has no inverse; the later inverse-dependent composition is separate.
    derivative_map = sp.Matrix([[1, 0]])
    degenerate_form = 2 * derivative_map.T * derivative_map
    return {
        "passed": zero(defect) and degenerate_form.det() == 0 and degenerate_form.rank() == 1,
        "scope": "Inverse-free square completion with an explicit degenerate energy example",
        "square_completion_defect": str(defect),
        "degenerate_form_determinant": str(degenerate_form.det()),
    }


def source_totality_negative_control():
    vacuum = sp.ones(4, 1) / 2
    observed = sp.Matrix([-1, -1, 1, 1]) / 2
    dark = sp.Matrix([-1, 1, 0, 0]) / sp.sqrt(2)
    hamiltonian = 3 * (sp.eye(4) - vacuum * vacuum.T) - sp.Rational(11, 4) * dark * dark.T
    alpha = sp.Symbol("alpha", real=True)
    source = sp.Matrix([sp.exp(-alpha), sp.exp(-alpha), sp.exp(alpha), sp.exp(alpha)]) / 2
    source -= sp.cosh(alpha) * vacuum
    tangent_defect = sp.simplify(source.diff(alpha).subs(alpha, 0) - observed)
    return {
        "passed": zero(hamiltonian * vacuum)
        and zero(hamiltonian * observed - 3 * observed)
        and zero(hamiltonian * dark - dark / 4)
        and zero(dark.dot(source))
        and zero(tangent_defect),
        "scope": "Finite counterexample to spectral completeness of one exponential source family",
        "observed_energy": "3",
        "unobserved_energy": "1/4",
        "source_span_dimension": 1,
        "vacuum_complement_dimension": 3,
    }


def normalized_source_control():
    z1, z2 = sp.symbols("Z1 Z2", positive=True)
    variance = z2 / z1**2 - 1
    normalized_defect = sp.simplify(variance - (z2 - z1**2) / z1**2)
    t, u, v, alpha = sp.symbols("t u v alpha", real=True)
    coefficients = sp.symbols("k1:7", real=True)
    cumulant = sum(coefficient * t ** (i + 1) for i, coefficient in enumerate(coefficients))
    second_derivative = sp.diff(cumulant, t, 2).subs(t, alpha * (u + v))
    integrated = alpha**2 * sp.integrate(second_derivative, (u, 0, 1), (v, 0, 1))
    cumulant_defect = sp.expand(
        cumulant.subs(t, 2 * alpha) - 2 * cumulant.subs(t, alpha) - integrated
    )
    return {
        "passed": zero(normalized_defect) and zero(cumulant_defect),
        "scope": "Normalized variance algebra and polynomial double-integral identity",
        "variance_defect": str(normalized_defect),
        "cumulant_defect": str(cumulant_defect),
    }


def exact_controls():
    return {
        "cometric_and_operator": cometric_and_operator_control(),
        "current_moments": current_moment_control(),
        "radial_budget": radial_budget_control(),
        "variational_completion": variational_completion_control(),
        "residual_and_centering": residual_and_centering_control(),
        "source_totality_negative": source_totality_negative_control(),
        "normalized_sources": normalized_source_control(),
    }


def main():
    controls = exact_controls()
    payload = {
        "schema": SCHEMA,
        "passed": all(control["passed"] for control in controls.values()),
        "scope": "Exact finite coefficients/algebra; finite-g and continuum hypotheses remain open",
        "controls": controls,
        "source_sha256": {
            name: hashlib.sha256((ROOT / name).read_bytes()).hexdigest() for name in SOURCES
        },
    }
    print(json.dumps(payload, indent=2))
    return 0 if payload["passed"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
