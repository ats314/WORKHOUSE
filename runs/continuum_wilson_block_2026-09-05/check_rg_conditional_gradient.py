"""Exact controls for the conditional-gradient repair, not a Wilson RG proof."""

from fractions import Fraction as F
import json
import sympy as sp


def main() -> None:
    checks = {}
    m = 16
    checks["linear_average_rejects_claimed_intertwining"] = F(1) > F(1, m * m)
    checks["linear_average_requires_reciprocal_constant"] = F(m) * F(1, m) == 1
    checks["four_dimensional_standard_metric_factor"] = F(16, 2**2) == 4
    C, kappa, c = sp.symbols("C kappa c", positive=True)
    hessian = sp.Matrix([[1 / C + kappa * c**2, -kappa * c],
                         [-kappa * c, kappa]])
    covariance = sp.Matrix([[C, c * C], [c * C, 1 / kappa + c**2 * C]])
    checks["sharp_gaussian_covariance_identity"] = all(
        sp.simplify(x) == 0 for x in hessian * covariance - sp.eye(2)
    )
    theta = sp.symbols("theta", real=True)
    t = c**2 / (1 - theta)
    difference = (1 + t) * sp.eye(2) - sp.Matrix([[1, c], [c, theta + c**2]])
    checks["separated_fiber_determinant_identity"] = (
        sp.simplify(difference.det() - t * (t - c**2)) == 0
    )
    checks["separated_fiber_second_diagonal"] = (
        sp.simplify(difference[1, 1] - (1 - theta + theta * c**2 / (1 - theta))) == 0
    )
    for index, (theta_value, c_value) in enumerate([(F(0), F(1, 3)),
                                                  (F(1, 2), F(1, 5)),
                                                  (F(3, 4), F(2, 7))]):
        evaluated = difference.subs({theta: sp.Rational(theta_value.numerator, theta_value.denominator),
                                    c: sp.Rational(c_value.numerator, c_value.denominator)})
        checks[f"rational_psd_control_{index}"] = (
            evaluated[0, 0] >= 0 and evaluated[1, 1] >= 0 and evaluated.det() >= 0
        )
    assert all(checks.values()), checks
    print(json.dumps({"scope": "Exact derivative/metric/Gaussian and scalar PSD identities only.",
                      "checks": {k: bool(v) for k, v in checks.items()}}, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
