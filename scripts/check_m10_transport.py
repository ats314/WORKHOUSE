"""Check finite identities used by the conditional-transport derivation.

These exact SymPy controls do not prove the actual conditional concentration
theorem, its external WKB input, or the uniform M10 score estimate.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path

import sympy as sp

SCOPE = (
    "Exact finite symbolic identities only. This run does not certify the external "
    "one-well theorem, actual conditional concentration, compact elliptic estimates, "
    "the finite-flow limiting argument, or the complete all-fiber M10 estimate."
)


def equal(left: sp.Expr | sp.MatrixBase, right: sp.Expr | sp.MatrixBase) -> bool:
    difference = left - right
    if isinstance(difference, sp.MatrixBase):
        return all(sp.simplify(entry) == 0 for entry in difference)
    return sp.simplify(difference) == 0


def gaussian_mean(polynomial: sp.Expr, variable: sp.Symbol, variance: sp.Expr) -> sp.Expr:
    """Exact centered Gaussian polynomial expectation, using Wick moments."""
    result = sp.S.Zero
    for (degree,), coefficient in sp.Poly(polynomial, variable).terms():
        if degree % 2 == 0:
            moment = sp.S.One if degree == 0 else sp.factorial2(degree - 1)
            result += coefficient * moment * variance ** (degree // 2)
    return sp.simplify(result)


def build_checks() -> list[dict[str, object]]:
    checks: list[dict[str, object]] = []

    def record(name: str, passed: bool, statement: str, exact_value: object) -> None:
        checks.append(
            {
                "name": name,
                "passed": bool(passed),
                "statement": statement,
                "exact_value": str(exact_value),
            }
        )

    r, theta = sp.symbols("r theta", real=True)
    z = sp.Function("z")
    radial_divergence = sp.diff(sp.sin(r) ** 2 * z(r), r) / sp.sin(r) ** 2
    record(
        "haar_radial_divergence",
        equal(radial_divergence, sp.diff(z(r), r) + 2 * sp.cot(r) * z(r)),
        "SU(2) radial Haar divergence is z'(r)+2 cot(r) z(r).",
        sp.simplify(radial_divergence),
    )
    euler_divergence_at_zero = sp.limit(1 + 2 * r * sp.cot(r), r, 0)
    record(
        "haar_euler_origin",
        equal(euler_divergence_at_zero, sp.Integer(3)),
        "The three-dimensional Euler field has Haar divergence tending to 3.",
        euler_divergence_at_zero,
    )

    potential_minimum = 16 * (1 - sp.cos(theta / 4))
    a0, a1, a2, a3 = theta / 4, theta / 4, theta / 2, theta / 2
    minimum_path_potential = 4 * (4 - sp.cos(a0) - sp.cos(a1) - sp.cos(a2 - a0) - sp.cos(a3 - a1))
    record(
        "constrained_minimum_path_value",
        equal(minimum_path_potential, potential_minimum),
        "The stated constrained path has V=16[1-cos(theta/4)].",
        sp.simplify(minimum_path_potential),
    )
    record(
        "constrained_antipode",
        equal(potential_minimum.subs(theta, sp.pi), 16 - 8 * sp.sqrt(2)),
        "The antipodal constrained value is 16-8 sqrt(2).",
        sp.simplify(potential_minimum.subs(theta, sp.pi)),
    )
    potential_quadratic = sp.limit(potential_minimum / theta**2, theta, 0)
    record(
        "potential_small_angle",
        equal(potential_quadratic, sp.Rational(1, 2)),
        "v_min(theta)=theta^2/2+O(theta^4).",
        potential_quadratic,
    )

    action = 32 * sp.sqrt(2) * (1 - sp.cos(theta / 8))
    record(
        "agmon_phase_eikonal",
        equal(sp.diff(action, theta) ** 2, potential_minimum)
        and equal(action.subs(theta, 0), sp.S.Zero),
        "I(0)=0 and I'(theta)^2=v_min(theta).",
        action,
    )
    action_quadratic = sp.limit(action / theta**2, theta, 0)
    record(
        "agmon_small_angle",
        equal(action_quadratic, sp.sqrt(2) / 4),
        "I(theta)=sqrt(2) theta^2/4+O(theta^4).",
        action_quadratic,
    )
    trace_cometric = 2 * (1 - sp.cos(theta) ** 2) / sp.diff(sp.cos(theta), theta) ** 2
    record(
        "trace_cometric_factor",
        equal(trace_cometric, sp.Integer(2)),
        "Gamma(w,w)=2(1-w^2) implies Gamma(theta,theta)=2 on regular fibers.",
        sp.simplify(trace_cometric),
    )

    electric = sp.Matrix([[4, -1, 3, -1], [-1, 4, -1, 3], [3, -1, 6, -2], [-1, 3, -2, 6]])
    magnetic = sp.Matrix([[2, 0, -1, 0], [0, 2, 0, -1], [-1, 0, 1, 0], [0, -1, 0, 1]])
    outer = sp.Matrix([0, 0, 1, 1])
    longitudinal_cometric = electric / 4
    gradient = longitudinal_cometric * outer
    velocity = sp.Matrix(
        [sp.Rational(1, 4), sp.Rational(1, 4), sp.Rational(1, 2), sp.Rational(1, 2)]
    )
    speed_squared = (velocity.T * longitudinal_cometric.inv() * velocity)[0]
    record(
        "horizontal_lift_and_metric_speed",
        equal(gradient, 2 * velocity)
        and equal((outer.T * gradient)[0], sp.Integer(2))
        and equal(speed_squared, sp.Rational(1, 2)),
        "The constrained path is half the theta gradient and has G-speed squared 1/2.",
        {"gradient": str(gradient), "speed_squared": str(speed_squared)},
    )

    orthogonal = sp.Matrix([[1, 0, 1, 0], [1, 0, -1, 0], [0, 1, 0, 1], [0, 1, 0, -1]]) / sp.sqrt(2)
    precision_plus = sp.Matrix(
        [[1, -sp.Rational(1, 2)], [-sp.Rational(1, 2), (1 + sp.sqrt(2)) / 4]]
    )
    precision_minus = sp.Matrix(
        [[sp.sqrt(6) / 3, -sp.sqrt(6) / 6], [-sp.sqrt(6) / 6, (sp.sqrt(6) + 3) / 12]]
    )
    precision = sp.simplify(orthogonal * sp.diag(precision_plus, precision_minus) * orthogonal.T)
    record(
        "actual_gaussian_riccati",
        equal(precision * electric * precision, magnetic),
        "The stated actual-square precision satisfies A C A=M.",
        precision,
    )

    # theta=(y0,y1,y2,q-y2), separately in each of the three colors.
    product_map = sp.Matrix([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, -1, 1]])
    product_precision = sp.simplify(product_map.T * precision * product_map)
    fast_hessian = product_precision[:3, :3]
    mixed_column = product_precision[:3, 3]
    mean_per_q = sp.Matrix([sp.Rational(1, 4), sp.Rational(1, 4), sp.Rational(1, 2)])
    record(
        "conditional_gaussian_mean",
        equal(fast_hessian * mean_per_q + mixed_column, sp.zeros(3, 1)),
        "At fixed q, the Gaussian minimum is (q/4,q/4,q/2).",
        mean_per_q,
    )
    principal_minors = [sp.simplify(fast_hessian[:k, :k].det()) for k in range(1, 4)]
    record(
        "conditional_hessian_positive",
        all(value.is_positive is True for value in principal_minors),
        "All three leading principal minors of the one-color fast Hessian are positive.",
        principal_minors,
    )
    aa, bb, cc = sp.symbols("a b c", real=True)
    deviation = sp.Matrix([aa, bb, cc])
    square_form = (aa + bb) ** 2 / 4 + cc**2 / 4 + sp.sqrt(6) * (aa - bb - cc) ** 2 / 12
    record(
        "conditional_quadratic_form_S7",
        equal((deviation.T * fast_hessian * deviation)[0] / 2, square_form),
        "S7 equals one half the conditional Hessian quadratic form, per color.",
        square_form,
    )
    normal_gradient_per_q = -fast_hessian * mean_per_q
    drift_coefficient = sp.simplify((mean_per_q.T * fast_hessian * mean_per_q)[0] / 2)
    covariance_coefficient = sp.simplify(
        (normal_gradient_per_q.T * fast_hessian.inv() * normal_gradient_per_q)[0] / 2
    )
    record(
        "normal_drift_gaussian_coefficient",
        equal(drift_coefficient, (6 + sp.sqrt(6)) / 48)
        and equal(drift_coefficient, covariance_coefficient),
        "Both Gaussian variance formulas give (6+sqrt(6))|q|^2/48 for the stopped-Q drift.",
        drift_coefficient,
    )
    full_mean_per_q = product_map * mean_per_q.col_join(sp.ones(1, 1))
    retained_phase = sp.simplify((full_mean_per_q.T * precision * full_mean_per_q)[0] / 2)
    record(
        "gaussian_retained_phase",
        equal(retained_phase, action_quadratic / 4),
        "The retained Gaussian phase matches I(|q|/2) at quadratic order.",
        retained_phase,
    )

    cutoff = sp.Function("chi")
    radial_speeds = [r * cutoff(4 * r), r * cutoff(4 * r), r * cutoff(2 * r), r * cutoff(r)]
    minimum_angles = [theta / 4, theta / 4, theta / 2, theta]
    synchronized = [
        speed.subs(r, angle) for speed, angle in zip(radial_speeds, minimum_angles, strict=True)
    ]
    record(
        "synchronized_cutoff_velocities",
        all(
            equal(speed, angle * cutoff(theta))
            for speed, angle in zip(synchronized, minimum_angles, strict=True)
        ),
        "The four synchronized profiles preserve the complete minimum curve exactly.",
        synchronized,
    )

    g, stiffness = sp.symbols("g stiffness", positive=True)
    x, center, centered_x = sp.symbols("x center centered_x", real=True)
    log_ground = sp.log(stiffness / (sp.pi * g**2)) / 4 - stiffness * (x - center) ** 2 / (2 * g**2)
    shifted_score = sp.simplify(
        sp.diff(log_ground, g) + (x * sp.diff(log_ground, x) + sp.Rational(1, 2)) / g
    )
    record(
        "shifted_gaussian_skew_score",
        equal(shifted_score, -stiffness * center * (x - center) / g**3),
        "Euler dilation with its skew half-density term gives sigma=-a m(x-m)/g^3.",
        shifted_score,
    )
    shifted_polynomial = shifted_score.subs(x, centered_x + center)
    scalar_variance = g**2 / (2 * stiffness)
    score_mean = gaussian_mean(shifted_polynomial, centered_x, scalar_variance)
    score_variance = (
        gaussian_mean(shifted_polynomial**2, centered_x, scalar_variance) - score_mean**2
    )
    record(
        "shifted_gaussian_score_variance",
        equal(score_mean, sp.S.Zero) and equal(score_variance, stiffness * center**2 / (2 * g**4)),
        "The normalized squared-ground density gives Var(sigma)=a m^2/(2g^4).",
        sp.simplify(score_variance),
    )

    q, y = sp.symbols("q y", real=True)
    density = sp.Function("p")(g, y, q)
    marginal = sp.Function("h")(g, q)
    fiber_speed = sp.Function("b")(y)
    coarse_speed = sp.Function("zq")(q)
    log_joint_density = sp.log(marginal) + sp.log(density)
    twice_score = (
        sp.diff(log_joint_density, g)
        + (
            fiber_speed * sp.diff(log_joint_density, y)
            + coarse_speed * sp.diff(log_joint_density, q)
        )
        / g
        + (sp.diff(fiber_speed, y) + sp.diff(coarse_speed, q)) / g
    )
    coarse_scalar = (
        sp.diff(sp.log(marginal), g)
        + coarse_speed * sp.diff(sp.log(marginal), q) / g
        + sp.diff(coarse_speed, q) / g
    )
    residual = (
        sp.diff(density, g)
        + coarse_speed * sp.diff(density, q) / g
        + sp.diff(density * fiber_speed, y) / g
    )
    record(
        "conditional_score_continuity_residual",
        equal(twice_score - coarse_scalar, residual / density),
        "Twice the score minus its coarse scalar is r/p; conditional normalization centers it.",
        "2 sigma - coarse_scalar = r/p",
    )
    hessian, quadratic_coefficient = sp.symbols("H G", positive=True)
    quadratic_score = quadratic_coefficient * centered_x**2 / 2
    quadratic_mean = gaussian_mean(quadratic_score, centered_x, 1 / (2 * hessian))
    quadratic_variance = (
        gaussian_mean(quadratic_score**2, centered_x, 1 / (2 * hessian)) - quadratic_mean**2
    )
    record(
        "quadratic_laplace_variance_factor",
        equal(quadratic_variance, quadratic_coefficient**2 / (8 * hessian**2)),
        "For Cov(z)=(2H)^-1, Var(G z^2/2)=G^2/(8H^2).",
        sp.simplify(quadratic_variance),
    )
    return checks


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, help="Write the exact check report as JSON.")
    args = parser.parse_args()
    checks = build_checks()
    passed = sum(check["passed"] is True for check in checks)
    report = {
        "schema": "workhouse.m10-transport-exact-checks.v1",
        "scope": SCOPE,
        "source": "docs/derivations/w6-conditional-transport-obstruction.md",
        "passed": passed,
        "total": len(checks),
        "checks": checks,
    }
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    print(f"{passed}/{len(checks)} exact conditional-transport controls passed.")
    for check in checks:
        if check["passed"] is not True:
            print(f"FAILED: {check['name']}")
    print(SCOPE)
    if args.output:
        print(f"JSON: {args.output.resolve()}")
    return 0 if passed == len(checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
