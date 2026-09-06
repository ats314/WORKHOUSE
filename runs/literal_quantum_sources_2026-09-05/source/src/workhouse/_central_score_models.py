"""Independent exact SU(2) central-score identity controls.

The positive trial uses its reconstructed potential, not the Wilson
potential. The actual Wilson obstruction additionally uses its analytic
positive ground equation and the established O(sqrt(u)) energy bound.
"""

from __future__ import annotations

import sys

import sympy as sp


def require(condition, label):
    if not condition:
        raise AssertionError(label)


def zero(expression, label):
    entries = list(expression) if isinstance(expression, sp.MatrixBase) else [expression]
    require(all(sp.simplify(entry) == 0 for entry in entries), label)


def controls():
    if sys.flags.optimize:
        raise RuntimeError("Exact controls require assertions enabled")
    r = sp.Rational
    a, u = sp.symbols("a u", positive=True)
    e, c, cot, aa, bb, ss, dd = sp.symbols("e c cot A B s d", real=True)
    aprime = 32 * u / a * (1 - c) - 8 * e / a - aa**2 - 2 * cot * aa
    bprime = -32 * u / a * (1 + c) + 8 * e / a + bb**2 - 2 * cot * bb
    dprime = aprime - bprime
    constant = 64 * u / a - 16 * e / a
    zero(
        dprime - (constant - aa**2 - bb**2 - 2 * cot * (aa - bb)),
        "actual Wilson Riccati difference",
    )
    divergence = sp.expand(dprime + (2 * cot + 2 * (aa - bb)) * (aa - bb))
    divergence = divergence.subs({aa: (ss + dd) / 2, bb: (ss - dd) / 2}, simultaneous=True)
    zero(divergence - (constant - ss**2 / 2 + 3 * dd**2 / 2), "Haar-weighted total derivative")
    d2 = sp.symbols("mean_d_squared", nonnegative=True)
    score_second = 2 * constant + 3 * d2
    weighted = sp.expand(2 * a * score_second / 12)
    zero(weighted - (r(64, 3) * u - r(16, 3) * e + a * d2 / 2), "axis Fisher and metric factors")

    theta = sp.symbols("theta", real=True)

    def laplacian_class(f):
        return sp.trigsimp((sp.diff(f, theta, 2) + 2 * sp.cot(theta) * sp.diff(f, theta)) / 4)

    zero(
        laplacian_class(2 * sp.cos(theta)) + r(3, 4) * 2 * sp.cos(theta),
        "normalized fundamental Casimir",
    )
    omega = 2 + sp.cos(theta)  # smooth positive on the whole SU(2) group
    A = -sp.sin(theta) / (2 + sp.cos(theta))
    B = -sp.sin(theta) / (2 - sp.cos(theta))
    d = sp.cancel(A - B)
    s = sp.cancel(A + B)
    p = sp.sin(theta) ** 2 * (4 - sp.cos(theta) ** 2) ** 2
    zero(
        sp.diff(p, theta) - p * (2 * sp.cot(theta) + 2 * d),
        "exact Haar conditional density derivative",
    )
    endpoint_limits = [sp.limit(p * d, theta, t) for t in (0, sp.pi)]
    require(endpoint_limits == [0, 0], "endpoint flux vanishes")
    norm = sp.integrate(sp.expand_trig(p), (theta, 0, sp.pi))

    def expectation(f):
        integrand = sp.trigsimp(sp.cancel(p * f))
        return sp.simplify(sp.integrate(sp.expand_trig(integrand), (theta, 0, sp.pi)) / norm)

    mean_s2, mean_d2 = expectation(s * s), expectation(d * d)
    haar_term = expectation(2 * sp.cot(theta) * d)
    mean_dprime = expectation(sp.diff(d, theta))
    require(mean_s2 == r(96, 113) and mean_d2 == r(4, 113), "exact positive trial moments")
    require(
        haar_term == r(28, 113) and mean_dprime == -r(36, 113), "Haar integration-by-parts factor"
    )
    zero(mean_dprime + haar_term + 2 * mean_d2, "integrated endpoint identity")
    require(mean_dprime != -2 * mean_d2, "omitting radial Haar drift is false")
    reconstructed = e + (a / 2) * laplacian_class(omega) / omega
    zero(
        -(a / 2) * laplacian_class(omega) + reconstructed * omega - e * omega,
        "reconstructed ground equation",
    )
    potential_pair = sp.simplify(reconstructed + reconstructed.subs(theta, sp.pi - theta) - 2 * e)
    mean_potential_pair = expectation(potential_pair)
    require(mean_potential_pair == 21 * a / 452, "exact reconstructed potential mean")
    zero(mean_s2 - (16 / a) * mean_potential_pair - 3 * mean_d2, "general-potential score identity")
    cc = sp.symbols("cosine", real=True)
    wilson_residual = sp.expand(r(3, 8) * a * cc + 4 * u * (1 - cc) * (2 + cc) - e * (2 + cc))
    require(
        sp.Poly(wilson_residual, cc).coeff_monomial(cc**2) == -4 * u,
        "positive trial is not falsely accepted as a Wilson ground",
    )

    pauli = (sp.Matrix([[0, 1], [1, 0]]), sp.Matrix([[0, -sp.I], [sp.I, 0]]), sp.diag(1, -1))
    generators = [sp.I * p / 2 for p in pauli]
    for i, ti in enumerate(generators):
        for j, tj in enumerate(generators):
            zero(-2 * sp.trace(ti * tj) - int(i == j), "unit Lie metric")
    axis = sp.Matrix([r(2, 3), r(1, 3), r(2, 3)])
    axis_matrix = sum((axis[i] * pauli[i] for i in range(3)), sp.zeros(2))
    geometry = []
    for cosine, sine in ((r(3, 5), r(4, 5)), (sp.Integer(0), sp.Integer(1)), (-r(3, 5), r(4, 5))):
        k = cosine * sp.eye(2) + sp.I * sine * axis_matrix
        umat = -sp.eye(2)
        y = k.adjoint() * umat
        zero(k.adjoint() * k - sp.eye(2), "exact quaternion unitarity")
        rot = sp.Matrix(
            3,
            3,
            lambda i, j, k=k: sp.simplify(
                -2 * sp.trace(generators[i] * k * generators[j] * k.adjoint())
            ),
        )
        zero(rot * rot.T - sp.eye(3), "adjoint orthogonality")
        jacobian = sp.BlockMatrix([[sp.eye(3), rot], [sp.eye(3), sp.zeros(3)]]).as_explicit()
        cometric = sp.simplify(a * jacobian * jacobian.T)
        expected = sp.BlockMatrix(
            [[2 * a * sp.eye(3), a * sp.eye(3)], [a * sp.eye(3), a * sp.eye(3)]]
        ).as_explicit()
        zero(cometric - expected, "actual product link cometric")
        cuu, cku, ckk = cometric[:3, :3], cometric[3:, :3], cometric[3:, 3:]
        zero(cku * cuu.inv() - sp.eye(3) / 2, "actual horizontal connection is one half")
        zero(ckk - cku * cuu.inv() * cku.T - a * sp.eye(3) / 2, "intrinsic vertical Schur metric")
        angle_derivatives = []
        for j, tangent in enumerate(generators):
            du = tangent * umat
            dk = tangent * k / 2
            dy = -k.adjoint() * dk * y + k.adjoint() * du
            theta1 = sp.simplify(-sp.trace(dk) / (2 * sine))
            theta2 = sp.simplify(-sp.trace(dy) / (2 * sine))
            zero(theta1 - axis[j] / 4, "first holonomy horizontal class angle")
            zero(theta2 - axis[j] / 4, "second holonomy horizontal class angle")
            zero(
                2 * (aa * theta1 + bb * theta2) - (aa + bb) * axis[j] / 2,
                "actual quantum density score",
            )
            angle_derivatives.append(str(theta1))
        geometry.append(
            {
                "cos_theta": str(cosine),
                "sin_theta": str(sine),
                "both_angle_derivatives": angle_derivatives,
            }
        )
    polar, azimuth = sp.symbols("polar azimuth", real=True)
    nvec = sp.Matrix(
        [sp.sin(polar) * sp.cos(azimuth), sp.sin(polar) * sp.sin(azimuth), sp.cos(polar)]
    )
    covariance = sp.Matrix(
        3,
        3,
        lambda i, j: (
            sp.integrate(
                sp.integrate(nvec[i] * nvec[j] * sp.sin(polar), (azimuth, 0, 2 * sp.pi)),
                (polar, 0, sp.pi),
            )
            / (4 * sp.pi)
        ),
    )
    zero(covariance - sp.eye(3) / 3, "uniform conjugacy-axis covariance")
    return {
        "passed": True,
        "wilson_scalar_identity": {
            "mean_s_squared": "128*u/a-32*e/a+3*mean_d_squared",
            "weighted_Fisher": str(weighted),
            "actual_bouquet_a": 4,
        },
        "positive_reconstructed_trial": {
            "omega": "2+cos(theta)",
            "radial_normalizer": str(norm),
            "mean_s_squared": str(mean_s2),
            "mean_d_squared": str(mean_d2),
            "mean_two_cot_d": str(haar_term),
            "mean_d_prime": str(mean_dprime),
            "mean_potential_pair_minus_two_e": str(mean_potential_pair),
            "endpoint_fluxes": list(map(str, endpoint_limits)),
            "omitted_Haar_drift_rejected": True,
            "not_a_Wilson_ground": True,
            "Wilson_residual_cosine_squared_coefficient": "-4*u",
        },
        "SU2_geometry": {
            "fundamental_Casimir": "3/4",
            "Cuu": "2*a*I",
            "b": "I/2",
            "S": "a*I/2",
            "cases": geometry,
            "axis_covariance": "I/3",
            "per_axis_Fisher": "E(s^2)/12",
        },
        "scope": (
            "Exact Riccati algebra, normalized Haar IBP in a reconstructed-potential trial, "
            "and finite exact SU(2) horizontal/metric controls. The trial is not a Wilson "
            "solution. The actual Wilson identity and large-u obstruction use the analytic "
            "positive ground equation and energy bound."
        ),
    }


# Original: next_quantum_score_center/check_central_score_identity_independent.py
# SHA256: 9a16953abb64750ec87039c44dfc868e70a0b1ff5e392b23a630084d885af0e3
