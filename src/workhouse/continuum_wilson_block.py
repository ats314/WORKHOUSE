"""Exact finite controls for physical Wilson blocks and oscillator coefficients.

Analytic localization, eigenvalue remainders, OS intertwining and continuum
limits are not machine-certified by this module. Original product-logarithm
and balanced-coordinate computations are kept as separate derivation paths.
"""

from __future__ import annotations

from functools import lru_cache

import sympy as s


def inner(x: s.Matrix, y: s.Matrix) -> s.Expr:
    return s.simplify(-2 * s.trace(x * y))


def su_basis(n: int) -> list[s.Matrix]:
    if type(n) is not int or n < 2:
        raise ValueError("An SU(N) basis requires an integer rank N >= 2")
    result = []
    for i in range(n):
        for j in range(i + 1, n):
            a, b = (s.zeros(n), s.zeros(n))
            a[i, j] = a[j, i] = s.I / 2
            b[i, j], b[j, i] = (s.Rational(1, 2), -s.Rational(1, 2))
            result.extend((a, b))
    for k in range(1, n):
        a = s.zeros(n)
        for i in range(k):
            a[i, i] = s.I / s.sqrt(2 * k * (k + 1))
        a[k, k] = -k * s.I / s.sqrt(2 * k * (k + 1))
        result.append(a)
    return result


def zero_matrix(matrix: s.Matrix) -> bool:
    return all(s.simplify(x) == 0 for x in matrix)


def matrix_polynomial_product(a: list[s.Matrix], b: list[s.Matrix], degree: int) -> list[s.Matrix]:
    n = a[0].rows
    return [
        sum((a[j] * b[k - j] for j in range(k + 1) if j < len(a) and k - j < len(b)), s.zeros(n))
        for k in range(degree + 1)
    ]


def metric_jet_controls() -> dict:
    q0, q1, q2 = s.symbols("q0 q1 q2", real=True)
    a = s.Matrix([[0, -q2, q1], [q2, 0, -q0], [-q1, q0, 0]])
    identity, zero = (s.eye(3), s.zeros(3))
    cuu = [6 * identity, zero, -(a**2)]
    cuk = [3 * identity, -a, -(a**2) / 2]
    cku = [3 * identity, a, -(a**2) / 2]
    cuu_inverse = [identity / 6, zero, a**2 / 36]
    assert all(
        (
            zero_matrix(x - (identity if k == 0 else zero))
            for k, x in enumerate(matrix_polynomial_product(cuu, cuu_inverse, 2))
        )
    )
    cross = matrix_polynomial_product(matrix_polynomial_product(cku, cuu_inverse, 2), cuk, 2)
    schur = [4 * identity - cross[0], -cross[1], -cross[2]]
    assert zero_matrix(schur[0] - s.Rational(5, 2) * identity)
    assert zero_matrix(schur[1])
    assert zero_matrix(schur[2] - s.Rational(5, 12) * a**2)
    lift = matrix_polynomial_product(cku, cuu_inverse, 2)
    assert zero_matrix(lift[0] - identity / 2)
    assert zero_matrix(lift[1] - a / 6)
    assert zero_matrix(lift[2])
    assert s.Rational(1, 4) + s.Rational(1, 6) - s.Rational(1, 8) == s.Rational(7, 24)
    assert 2 * s.Rational(7, 24) == s.Rational(7, 12)
    dexp_inverse = [identity, -a / 2, a**2 / 12]
    dexp_inverse_t = [x.T for x in dexp_inverse]
    coarse = matrix_polynomial_product(
        matrix_polynomial_product(dexp_inverse, cuu, 2), dexp_inverse_t, 2
    )
    assert zero_matrix(coarse[0] - 6 * identity)
    assert zero_matrix(coarse[1])
    assert zero_matrix(coarse[2] + s.Rational(3, 2) * a**2)
    return {
        "vertical_kinetic_at_identity": "5/4",
        "schur_alpha_squared": "(5/12)(ad Q)^2",
        "balanced_velocity_alpha": "(7/12)[Q,E]",
        "coarse_form_g_squared_leading": "3/2",
        "coarse_form_order_one": "-(3/4)(ad Q)^2",
    }


def lie_gaussian_controls() -> list[dict]:
    rows = []
    for n in (2, 3, 4):
        basis = su_basis(n)
        d = n * n - 1
        assert len(basis) == d
        assert all(
            (inner(t, v) == int(i == j) for i, t in enumerate(basis) for j, v in enumerate(basis))
        )
        q = sum((s.Rational(i % 5 - 2, i + 3) * t for i, t in enumerate(basis)), s.zeros(n))
        qnorm = inner(q, q)
        adq = s.Matrix([[inner(t, q * v - v * q) for v in basis] for t in basis])
        assert zero_matrix(adq + adq.T)
        assert s.simplify(s.trace(adq**2) + n * qnorm) == 0
        cf = s.Rational(n * n - 1, 2 * n)
        assert zero_matrix(sum((t * t for t in basis), s.zeros(n)) + cf * s.eye(n))
        mixed = sum((s.trace(q * q * t * t) for t in basis), s.S.Zero)
        assert s.simplify(mixed - cf * qnorm / 2) == 0
        a = 1 / s.sqrt(5)
        vertical_kinetic = s.Rational(5, 12) * a * s.trace(adq**2)
        vertical_potential = -mixed / (8 * a)
        vertical = s.simplify(vertical_kinetic + vertical_potential)
        assert s.simplify(vertical + s.sqrt(5) * (s.Rational(n, 12) + cf / 16) * qnorm) == 0
        bh = s.Rational(3, 2) * s.Rational(49, 360) / (2 * a) * n * qnorm
        assert s.simplify(bh - 49 * n * qnorm / (96 * s.sqrt(5))) == 0
        combined = s.simplify(vertical + bh)
        assert s.simplify(combined - s.sqrt(5) * (5 - 2 * n * n) * qnorm / (160 * n)) == 0
        rows.append(
            {
                "N": n,
                "dimension": d,
                "Q_norm_squared": str(qnorm),
                "combined_per_Q_norm_squared": str(s.simplify(combined / qnorm)),
            }
        )
    return rows


def polynomial_gauss_controls() -> dict:
    q = s.Matrix(s.symbols("q0:3", real=True))
    z = s.Matrix(s.symbols("z0:3", real=True))

    def gauss(f: s.Expr, coordinates: s.Matrix) -> s.Matrix:
        return coordinates.cross(s.Matrix([s.diff(f, x) for x in coordinates]))

    def first_coupling(f: s.Expr) -> s.Expr:
        gq = gauss(f, q)
        return s.expand(sum(s.diff(gq[b], z[b]) for b in range(3)))

    q2, z2, qz = (q.dot(q), z.dot(z), q.dot(z))
    physical = [q2, z2, qz, qz**2, q2 * z2, q2 * qz, qz**3 + q2 * z2**2]
    for f in physical:
        assert zero_matrix(gauss(f, q) + gauss(f, z))
        assert first_coupling(f) == 0
    f = s.Function("F")(*q, *z)
    gz = gauss(f, z)
    assert s.simplify(sum(s.diff(gz[b], z[b]) for b in range(3))) == 0
    negative = q[0] * z[1]
    assert first_coupling(negative) != 0
    return {
        "jointly_invariant_polynomials": len(physical),
        "arbitrary_function_divergence_identity": True,
        "noninvariant_negative_control": str(first_coupling(negative)),
        "scope": "Exact SU(2) polynomial checks; the general antisymmetry argument is analytic.",
    }


def scalar_controls() -> dict:
    n, g = s.symbols("N g", positive=True)
    d, cf = (n**2 - 1, (n**2 - 1) / (2 * n))
    vertical = -s.sqrt(5) * (n / 12 + cf / 16)
    bh = 49 * n / (96 * s.sqrt(5))
    assert s.simplify(vertical + bh - s.sqrt(5) * (5 - 2 * n**2) / (160 * n)) == 0
    haar_constant = s.Rational(3, 2) / g**2 * (-n * g**2 * d / 6) / 2
    assert s.simplify(haar_constant + n * d / 8) == 0
    variance = s.sqrt(5) / 2
    derivative_norm = (7 / (6 * s.sqrt(10))) ** 2 * variance
    assert s.simplify(derivative_norm - 49 / (144 * s.sqrt(5))) == 0
    return {
        "combined_shift": str(s.simplify(vertical + bh)),
        "haar_scalar": str(haar_constant),
        "ground_derivative_norm_coefficient": str(s.simplify(derivative_norm)),
    }


def expectation(polynomial: s.Expr, variables: list, variances: list) -> s.Expr:
    result = s.S.Zero
    for powers, coefficient in s.Poly(s.expand(polynomial), *variables).terms():
        moment = coefficient
        for power, variance in zip(powers, variances, strict=True):
            if power % 2:
                moment = s.S.Zero
                break
            if power:
                moment *= s.factorial2(power - 1) * variance ** (power // 2)
        result += moment
    return s.simplify(result)


def multistrip_control() -> dict:
    q1 = s.Matrix(s.symbols("q10:13", real=True))
    q2 = s.Matrix(s.symbols("q20:23", real=True))
    z1 = s.Matrix(s.symbols("z10:13", real=True))
    z2 = s.Matrix(s.symbols("z20:23", real=True))
    qs, zs = (list(q1) + list(q2), list(z1) + list(z2))
    variables = qs + zs
    variances = [s.sqrt(3) / 2] * 6 + [s.sqrt(5) / 2] * 6

    def angular(f: s.Expr, q: s.Matrix) -> s.Matrix:
        return q.cross(s.Matrix([s.diff(f, x) for x in q]))

    def oscillator_above_ground(f: s.Expr) -> s.Expr:
        result = sum(-s.Rational(3, 2) * s.diff(f, x, 2) + s.sqrt(3) * x * s.diff(f, x) for x in qs)
        result += sum(
            -s.Rational(5, 2) * s.diff(f, x, 2) + s.sqrt(5) * x * s.diff(f, x) for x in zs
        )
        return s.expand(result)

    psi = q1.dot(q2)
    l1, l2 = (angular(psi, q1), angular(psi, q2))
    assert l1 + l2 == s.zeros(3, 1)
    assert l1 != s.zeros(3, 1)
    coarse_energy = 2 * s.sqrt(3)
    assert s.simplify(oscillator_above_ground(psi) - coarse_energy * psi) == 0
    for component in list(l1) + list(l2):
        assert s.simplify(oscillator_above_ground(component) - coarse_energy * component) == 0
    coefficient = 7 / (2 * s.sqrt(10))
    image = s.expand(coefficient * (z1.dot(l1) + z2.dot(l2)))
    assert image != 0
    assert s.simplify(oscillator_above_ground(image) - (coarse_energy + s.sqrt(5)) * image) == 0
    total_gauss = sum((angular(image, q) for q in (q1, q2, z1, z2)), s.zeros(3, 1))
    assert all(s.simplify(x) == 0 for x in total_gauss)
    norm_psi = expectation(psi**2, variables, variances)
    norm_angular = expectation(l1.dot(l1) + l2.dot(l2), variables, variances)
    norm_image = expectation(image**2, variables, variances)
    assert norm_psi == s.Rational(9, 4)
    assert norm_angular == 9
    assert s.simplify(norm_image - 49 * s.sqrt(5) * norm_angular / 80) == 0
    schur = s.simplify(-norm_image / s.sqrt(5) / norm_psi)
    direct = s.Rational(3, 4) * norm_angular / norm_psi
    net = s.simplify(direct + schur)
    assert schur == -s.Rational(49, 20)
    assert direct == 3
    assert net == s.Rational(11, 20)
    n = s.symbols("N", integer=True, positive=True)
    assert s.simplify((s.Rational(3, 4) - s.Rational(49, 80)) * 2 * n) == 11 * n / 40
    shell_four = (q1.dot(q1) - 5 * s.sqrt(3) / 2) * psi
    shell_four = s.expand(
        (oscillator_above_ground(shell_four) - coarse_energy * shell_four) / (2 * s.sqrt(3))
    )
    assert shell_four != 0
    assert s.simplify(oscillator_above_ground(shell_four) - 4 * s.sqrt(3) * shell_four) == 0
    image_four = s.expand(
        coefficient * (z1.dot(angular(shell_four, q1)) + z2.dot(angular(shell_four, q2)))
    )
    assert image_four != 0
    fixed_energy_denominator_error = s.expand(
        oscillator_above_ground(image_four) - (coarse_energy + s.sqrt(5)) * image_four
    )
    assert fixed_energy_denominator_error != 0
    q, z = (q1, z1)
    sigma_q, sigma_z = (s.sqrt(3) / 2, s.sqrt(5) / 2)
    source_polynomials = [q.dot(q) - 3 * sigma_q, q.dot(z), z.dot(z) - 3 * sigma_z]
    source_gram = s.Matrix(
        [
            [expectation(f * h, variables, variances) for h in source_polynomials]
            for f in source_polynomials
        ]
    )
    assert source_gram == s.diag(s.Rational(9, 2), 3 * s.sqrt(15) / 4, s.Rational(15, 2))
    return {
        "scope": __doc__,
        "witness": "(Q1 dot Q2) times the product coarse Gaussian, SU(2)",
        "coarse_excitation": str(coarse_energy),
        "image_excitation": str(coarse_energy + s.sqrt(5)),
        "witness_norm_squared": str(norm_psi),
        "angular_norm_squared": str(norm_angular),
        "image_norm_squared": str(norm_image),
        "normalized_schur_coefficient": str(schur),
        "normalized_direct_metric_coefficient": str(direct),
        "normalized_net_angular_coefficient": str(net),
        "all_rank_normalized_net": "11*N/40",
        "mixed_shell_denominator_negative_control": True,
        "single_strip_centered_source_gram_SU2": str(source_gram),
        "single_strip_source_squared_norms_general": ["3*d/2", "d*sqrt(15)/4", "5*d/2"],
    }


def general_moments() -> dict:
    n = s.symbols("N", integer=True, positive=True)
    d = n**2 - 1
    variance = s.sqrt(3) / 2

    def radial_moment(k: int) -> s.Expr:
        return variance**k * s.prod(d + 2 * j for j in range(k))

    radial_norm = s.simplify(radial_moment(2) - radial_moment(1) ** 2)
    radial_delta = []
    degree_one_delta = []
    for k in (1, 2):
        excited = (
            radial_moment(k + 2)
            - 2 * radial_moment(1) * radial_moment(k + 1)
            + radial_moment(1) ** 2 * radial_moment(k)
        ) / radial_norm
        radial_delta.append(s.simplify(excited - radial_moment(k)))
        degree_one_delta.append(
            s.simplify(radial_moment(k + 1) / radial_moment(1) - radial_moment(k))
        )
    assert s.simplify(radial_delta[0] - 2 * s.sqrt(3)) == 0
    assert s.simplify(radial_delta[1] - 9 * (d + 2)) == 0
    assert s.simplify(2 * degree_one_delta[0] - radial_delta[0]) == 0
    assert s.simplify(2 * degree_one_delta[1] - 6 * (d + 2)) == 0
    quartic_average = (2 * n**2 - 3) / (4 * n * (d + 2))
    c = s.sqrt(5) * (5 - 2 * n**2) / (160 * n)
    local = s.simplify(c * radial_delta[0] - quartic_average * radial_delta[1] / 24)
    mixed = s.simplify(
        c * 2 * degree_one_delta[0] - quartic_average * 2 * degree_one_delta[1] / 24 + 11 * n / 40
    )
    split = s.simplify(mixed - local)
    assert s.simplify(split - (54 * n**2 - 15) / (160 * n)) == 0
    assert all(split.subs(n, rank) > 0 for rank in range(2, 21))
    return {
        "radial_delta_r2": str(radial_delta[0]),
        "radial_delta_r4": str(radial_delta[1]),
        "mixed_delta_sum_r2": str(2 * degree_one_delta[0]),
        "mixed_delta_sum_r4": str(s.simplify(2 * degree_one_delta[1])),
        "angular_average_TrQ4_per_r4": str(quartic_average),
        "local_unscaled_gap_correction": str(local),
        "mixed_unscaled_gap_correction": str(mixed),
        "mixed_minus_local": str(split),
    }


def matrix_trace_contractions() -> list[dict]:
    rows = []
    for n in (2, 3, 4):
        basis = su_basis(n)
        wick = s.simplify(
            sum(
                s.trace(a * a * b * b + a * b * a * b + a * b * b * a) for a in basis for b in basis
            )
        )
        expected = s.Rational((n * n - 1) * (2 * n * n - 3), 4 * n)
        assert wick == expected
        rows.append({"N": n, "unit_variance_TrQ4_Gaussian_moment": str(wick)})
    return rows


def explicit_su2_matrix() -> dict:
    q1, q2 = (s.Matrix(s.symbols("q10:13")), s.Matrix(s.symbols("q20:23")))
    variables = list(q1) + list(q2)
    variances = [s.sqrt(3) / 2] * 6
    r1, r2 = (q1.dot(q1), q2.dot(q2))
    states = [r1 - 3 * s.sqrt(3) / 2, r2 - 3 * s.sqrt(3) / 2, q1.dot(q2)]

    def angular(f: s.Expr, q: s.Matrix) -> s.Matrix:
        return q.cross(s.Matrix([s.diff(f, x) for x in q]))

    angulars = [(angular(f, q1), angular(f, q2)) for f in states]
    gram = s.Matrix([[expectation(f * h, variables, variances) for h in states] for f in states])
    assert gram == s.diag(s.Rational(9, 2), s.Rational(9, 2), s.Rational(9, 4))
    potential = -3 * s.sqrt(5) * (r1 + r2) / 320 - (r1**2 + r2**2) / 192
    vacuum_expectation = expectation(potential, variables, variances)
    effective = s.zeros(3)
    for i, f in enumerate(states):
        for j, h in enumerate(states):
            angular_form = sum((x.dot(y) for x, y in zip(angulars[i], angulars[j], strict=True)))
            effective[i, j] = expectation(
                s.Rational(11, 80) * angular_form + (potential - vacuum_expectation) * f * h,
                variables,
                variances,
            )
    normalized = (gram.inv() * effective).applyfunc(s.simplify)
    local = -3 * s.sqrt(15) / 160 - s.Rational(15, 64)
    mixed = -3 * s.sqrt(15) / 160 - s.Rational(5, 32) + s.Rational(11, 20)
    assert normalized == s.diag(local, local, mixed)
    assert s.simplify(mixed - local) == s.Rational(201, 320)
    bad_split = s.Rational(201, 320) - 3
    assert bad_split < 0
    return {
        "basis": ["centered |Q1|^2", "centered |Q2|^2", "Q1 dot Q2"],
        "gram": str(gram),
        "effective_matrix_relative_to_ground": str(normalized),
        "mixed_minus_local": "201/320",
        "omitted_metric_negative_control_split": str(bad_split),
    }


def conditional_gradient_control() -> dict:
    """Exact Gaussian covariance and the quotient metric, with a score witness."""
    coarse, kappa, c = s.symbols("C kappa c", positive=True)
    hessian = s.Matrix([[1 / coarse + kappa * c * c, -kappa * c], [-kappa * c, kappa]])
    covariance = s.Matrix([[coarse, c * coarse], [c * coarse, 1 / kappa + c * c * coarse]])
    assert zero_matrix(hessian * covariance - s.eye(2))
    theta = s.symbols("theta", nonnegative=True)
    t = c * c / (1 - theta)
    majorant = (1 + t) * s.eye(2) - s.Matrix([[1, c], [c, theta + c * c]])
    assert s.simplify(majorant.det() - t * (t - c * c)) == 0
    for m in (2, 4, 16):
        average = s.ones(1, m) / m
        assert (average * average.T)[0] == s.Rational(1, m)
        gradient = s.ones(m, 1) / m
        conditioned = (average * average.T).inv() * average * gradient
        assert conditioned[0] == 1
        assert (conditioned.T * (average * average.T) * conditioned)[0] == gradient.dot(gradient)
    a = su_basis(3)
    q, z = s.symbols("q z", real=True)
    diagonal = a[-2]
    mixed = -s.trace((q * diagonal) ** 2 * (z * diagonal) ** 2) / 4
    assert s.simplify(s.diff(mixed, q, z) + q * z / 8) == 0
    commutator = a[0] * a[1] - a[1] * a[0]
    assert inner(commutator, commutator) == 1
    center = (s.sqrt(5) - 1) / 4
    assert center.is_positive is True
    return {
        "sharp_gaussian_covariance": str(covariance),
        "majorant_determinant": str(s.factor(majorant.det())),
        "quotient_average_sizes": [2, 4, 16],
        "unweighted_average_negative_control_factor": 16,
        "mixed_quartic_hessian": str(s.diff(mixed, q, z)),
        "two_coarse_commutator_norm_squared": "1",
        "SU5_secondary_center_quadratic_coefficient": str(center),
        "scope": "Finite Gaussian and Lie identities; no global conditional-gap or RG theorem",
    }


def original_strip_control() -> dict:
    """Independent seven-link Rayleigh calculation in original face logarithms."""
    q, z = s.Matrix(s.symbols("q0:3")), s.Matrix(s.symbols("z0:3"))
    variables = list(q) + list(z)
    aq, az = 1 / s.sqrt(3), 1 / s.sqrt(5)
    variances = [1 / (2 * aq)] * 3 + [1 / (2 * az)] * 3
    x1, x2 = (q + z) / s.sqrt(2), (q - z) / s.sqrt(2)

    def ad(x):
        return s.Matrix([[0, -x[2], x[1]], [x[2], 0, -x[0]], [-x[1], x[0], 0]])

    def correction(p):
        dq = s.Matrix([s.diff(p, v) - aq * v * p for v in q])
        dz = s.Matrix([s.diff(p, v) - az * v * p for v in z])
        d1, d2 = (dq + dz) / s.sqrt(2), (dq - dz) / s.sqrt(2)
        a1, a2 = ad(x1), ad(x2)
        kinetic = -(d1.dot(a1 * a1 * d1) + d2.dot(a2 * a2 * d2)) / 6
        kinetic -= d1.dot(((a1 * a1 + a2 * a2) / 12 + a1 * a2 / 4) * d2)
        potential = -(x1.dot(x1) ** 2 + x2.dot(x2) ** 2) * p * p / 96
        norm = expectation(p * p, variables, variances)
        return {
            "kinetic": s.simplify(expectation(kinetic, variables, variances) / norm),
            "potential": s.simplify(expectation(potential, variables, variances) / norm),
            "haar": s.Integer(-1),
            "norm": norm,
        }

    ground = correction(s.Integer(1))
    radial = correction(q.dot(q) - 3 * s.sqrt(3) / 2)
    adjoint = correction(q[0])
    delta = s.simplify(sum(radial[k] - ground[k] for k in ("kinetic", "potential", "haar")))
    angular = q.cross(s.Matrix([1, 0, 0]))
    image = angular.dot(z) / s.sqrt(10)
    self_energy = s.simplify(
        expectation(image * image, variables, variances) / adjoint["norm"] / s.sqrt(5)
    )
    assert self_energy == s.Rational(1, 10)
    delta_adjoint = s.simplify(
        sum(adjoint[k] - ground[k] for k in ("kinetic", "potential", "haar")) - self_energy
    )
    assert s.simplify(delta + s.Rational(15, 64) + 3 * s.sqrt(15) / 160) == 0
    assert s.simplify(delta_adjoint - s.Rational(63, 320) + 3 * s.sqrt(15) / 320) == 0
    assert s.simplify(2 * delta_adjoint - delta) == s.Rational(201, 320)
    return {
        "ground": {k: str(v) for k, v in ground.items()},
        "radial": {k: str(v) for k, v in radial.items()},
        "adjoint": {k: str(v) for k, v in adjoint.items()},
        "radial_gap_correction": str(delta),
        "adjoint_gap_correction": str(delta_adjoint),
        "product_log_self_energy": str(self_energy),
        "mixed_minus_radial": str(s.simplify(2 * delta_adjoint - delta)),
        "balanced_comparison_difference": "0",
        "scope": "Exact SU(2) original-seven-link coefficients; no global remainder certification",
    }


@lru_cache(maxsize=1)
def exact_block_controls() -> dict:
    return {
        "conditional_gradient": conditional_gradient_control(),
        "metric_jets": metric_jet_controls(),
        "lie_gaussian_contractions": lie_gaussian_controls(),
        "physical_gauss": polynomial_gauss_controls(),
        "scalar_constants": scalar_controls(),
        "two_strip_selfenergy": multistrip_control(),
        "first_shell_general": general_moments(),
        "quartic_trace_contractions": matrix_trace_contractions(),
        "first_shell_SU2_matrix": explicit_su2_matrix(),
        "original_seven_link_SU2": original_strip_control(),
    }
