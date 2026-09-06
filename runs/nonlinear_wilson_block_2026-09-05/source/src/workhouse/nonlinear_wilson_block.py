"""Exact controls for global fiber barriers and ground-bundle geometry.

The generic APIs validate explicit finite hypotheses. The analytic all-rank
operator theorem, conditional spectral premises and volume limits are not
machine-certified by this module.
"""

from __future__ import annotations

import copy
import itertools
from functools import lru_cache

import sympy as sp


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def zero(expression: sp.Expr | sp.MatrixBase, label: str) -> None:
    entries = list(expression) if isinstance(expression, sp.MatrixBase) else [expression]
    require(all(sp.simplify(entry) == 0 for entry in entries), label)


def frobenius2(matrix: sp.MatrixBase) -> sp.Expr:
    return sp.simplify(sp.trace(matrix.adjoint() * matrix))


def psd_minors(matrix: sp.MatrixBase) -> list[str]:
    zero(matrix - matrix.adjoint(), "Hermitian PSD input")
    values = []
    for size in range(1, matrix.rows + 1):
        for indices in itertools.combinations(range(matrix.rows), size):
            value = sp.simplify(matrix.extract(indices, indices).det())
            require(value.is_nonnegative is True, "nonnegative principal minor")
            values.append(str(value))
    return values


def nonnegative_coefficients(expression: sp.Expr, variables: tuple) -> dict:
    """Exact polynomial certificate on the stated nonnegative orthant."""
    numerator, denominator = sp.fraction(sp.cancel(expression))
    num = sp.Poly(numerator, *variables)
    den = sp.Poly(denominator, *variables)
    require(all(c >= 0 for c in num.coeffs()), "numerator coefficient")
    require(all(c >= 0 for c in den.coeffs()), "denominator coefficient")
    require(den.TC() > 0, "strict denominator on the closed orthant")
    return {
        "expression": str(sp.factor(expression)),
        "numerator": str(num.as_expr()),
        "denominator": str(den.as_expr()),
        "domain": "all variables nonnegative",
    }


def abstract_matrix_control() -> dict:
    coordinates = sp.symbols("a b c d e f g h", real=True)
    a, b, c, d, e, f, g, h = coordinates
    first = sp.Matrix([a + sp.I * b, c + sp.I * d])
    second = sp.Matrix([e + sp.I * f, g + sp.I * h])
    inner = (first.adjoint() * second)[0]
    wedge = first[0] * second[1] - first[1] * second[0]
    zero(
        frobenius2(first) * frobenius2(second)
        - sp.expand_complex(inner * sp.conjugate(inner))
        - sp.expand_complex(wedge * sp.conjugate(wedge)),
        "complex Lagrange identity",
    )
    zero(
        2 * (frobenius2(first) + frobenius2(second))
        - frobenius2(first - second)
        - frobenius2(first + second),
        "parallelogram and adjoint root-pair identity",
    )

    # B and Q need not commute; their explicit Gram factors certify positivity.
    left = sp.Matrix([[1, 0], [1, 2], [0, 1]]) / 10
    right = sp.Matrix([[1, 2], [0, 1], [2, -1]]) / 3
    bmat, qmat = left * left.T, right * right.T
    eta = sp.trace(bmat)
    amat = sp.eye(3) - bmat
    require(0 < eta < sp.Rational(1, 2), "near-neighborhood Gram trace")
    require(bmat * qmat != qmat * bmat, "noncommuting PSD example")
    value = sp.trace(amat * qmat) - (1 - eta) * sp.trace(qmat)
    wedge_sum = sum(
        (left[i, ell] * right[j, m] - left[j, ell] * right[i, m]) ** 2
        for ell in range(left.cols)
        for m in range(right.cols)
        for i in range(3)
        for j in range(i + 1, 3)
    )
    zero(value - wedge_sum, "Gram sum of exterior squares")
    require(value > 0, "strict noncommuting trace bound")
    wrong_q = sp.diag(0, -1)
    wrong_b = sp.diag(sp.Rational(1, 4), 0)
    negative = sp.trace(wrong_b) * sp.trace(wrong_q) - sp.trace(wrong_b * wrong_q)
    require(negative == -sp.Rational(1, 4), "missing-Q-positivity negative control")
    return {
        "symbolic_complex_identities": 2,
        "eta": str(eta),
        "noncommuting_trace_margin": str(value),
        "B_principal_minors": psd_minors(bmat),
        "Q_principal_minors": psd_minors(qmat),
        "A_minus_scalar_principal_minors": psd_minors(eta * sp.eye(3) - bmat),
        "missing_Q_positivity_margin": str(negative),
        "scope": "Arbitrary complex two-vector identities and one exact 3x3 PSD model.",
    }


def su2_group_control() -> dict:
    r = sp.Rational
    pauli = (sp.Matrix([[0, 1], [1, 0]]), sp.Matrix([[0, -sp.I], [sp.I, 0]]), sp.diag(1, -1))
    generators = tuple(-sp.I * item / 2 for item in pauli)
    for i, first in enumerate(generators):
        for j, second in enumerate(generators):
            zero(-2 * sp.trace(first * second) - int(i == j), "Lie metric normalization")
    casimir = -sum((item * item for item in generators), sp.zeros(2))
    zero(casimir - r(3, 4) * sp.eye(2), "fundamental Casimir")
    axis = (r(2, 3), r(1, 3), r(2, 3))
    axis_matrix = sum((axis[i] * pauli[i] for i in range(3)), sp.zeros(2))
    fmat = r(2, 3) * sp.eye(2) + sp.I * (pauli[0] / 3 + 2 * pauli[1] / 3)
    zero(fmat.adjoint() * fmat - sp.eye(2), "rational quaternion unitarity")
    zero(fmat.det() - 1, "rational quaternion special determinant")

    def adjoint(matrix):
        return sp.Matrix(
            3,
            3,
            lambda i, j: sp.simplify(
                -2 * sp.trace(generators[i] * matrix * generators[j] * matrix.adjoint())
            ),
        )

    cases = []
    for cosine, sine in (
        (sp.Integer(1), sp.Integer(0)),
        (r(3, 5), r(4, 5)),
        (sp.Integer(0), sp.Integer(1)),
    ):
        hmat = cosine * sp.eye(2) + sp.I * sine * axis_matrix
        umat, kmat = hmat * hmat, hmat * fmat
        ymat = fmat.adjoint() * hmat
        zero(hmat.adjoint() * hmat - sp.eye(2), "square-root unitarity")
        zero(hmat.det() - 1, "SU(2) square root")
        zero(kmat * ymat - umat, "actual coarse product")
        zero(
            sp.trace(kmat) + sp.trace(ymat) - 4 * cosine * r(2, 3),
            "exact two-character cancellation identity",
        )

        def v(matrix):
            return 2 - sp.re(sp.trace(matrix))

        triangle = 2 * (v(kmat) + v(ymat)) - v(umat)
        zero(
            triangle - frobenius2(sp.eye(2) - 2 * kmat + umat) / 2,
            "unitary product barrier exact remainder",
        )
        require(triangle >= 0, "product barrier positivity")
        rot = adjoint(umat)
        zero(rot.T * rot - sp.eye(3), "adjoint orthogonality")
        metric = 15 * (8 * sp.eye(3) - rot - rot.T).inv()
        dmat = (sp.eye(3) - rot) * (sp.eye(3) - rot.T)
        zero(metric / r(5, 2) - 6 * (6 * sp.eye(3) + dmat).inv(), "exact strip Schur metric ratio")
        ratio = 6 / (6 + 16 * cosine**2 * (1 - cosine**2))
        direction = sp.Matrix(axis)
        expected = r(5, 2) * (ratio * sp.eye(3) + (1 - ratio) * direction * direction.T)
        zero(metric - expected, "longitudinal and transverse metric eigenvalues")
        halfrot = adjoint(hmat)
        zero(halfrot * metric * halfrot.T - metric, "balanced metric translation")
        eigen_bound = psd_minors(4 * v(umat) * sp.eye(3) - dmat)
        cases.append(
            {
                "cos_half_angle": str(cosine),
                "sin_half_angle": str(sine),
                "coarse_v": str(v(umat)),
                "strip_transverse_ratio": str(ratio),
                "product_barrier_margin": str(triangle),
                "adjoint_root_bound_minors": eigen_bound,
                "metric_global_lower_minors": psd_minors(metric - r(3, 2) * sp.eye(3)),
                "metric_global_upper_minors": psd_minors(r(5, 2) * sp.eye(3) - metric),
            }
        )
        if cosine == 0:
            zero(umat + sp.eye(2), "central minus identity coarse value")
            zero(2 * (v(kmat) + v(ymat)) - 8, "fiber constant potential at -I")
            zero(metric - r(5, 2) * sp.eye(3), "central strip metric")
    return {
        "rational_group_cases": cases,
        "fundamental_Casimir": "3/4",
        "central_minus_I_potential_over_u": 8,
        "minus_I_conditional_gaps": {"bouquet": "3/4", "strip": "15/16"},
        "scope": (
            "Exact actual SU(2) group and metric normalization; "
            "Casimir input gives the -I obstruction."
        ),
    }


def scalar_budget_control() -> dict:
    h, k, u, a, e, s, w = sp.symbols("h k u a e s w", nonnegative=True)
    alpha = sp.Rational(8, 3)
    eta = h / (2 * (1 + h))
    epsilon = 1 / (1 + k)
    t = 1 / (1 + alpha * eta)
    zero(1 - t - alpha * eta * t, "exact kinetic loss")
    certificates = {
        "potential_coefficient_dominates_t": nonnegative_coefficients(1 - eta - t, (h,)),
        "metric_t_at_least_3_over_7": nonnegative_coefficients(t - sp.Rational(3, 7), (h,)),
        "cap_below": nonnegative_coefficients(
            t * (epsilon * u - a) + 4 * u * eta - (epsilon * u - a), (h, k, u, a)
        ),
        "cap_above": nonnegative_coefficients(
            t * (epsilon * u + a) + 4 * u * eta - epsilon * u, (h, k, u, a)
        ),
        "lower_v_at_least_3eta": nonnegative_coefficients(4 * eta - 2 * eta**2 - 3 * eta, (h,)),
        "kinetic_loss_at_most_3eta": nonnegative_coefficients(3 * eta - (1 - t), (h,)),
        "near_affine_loss_margin": nonnegative_coefficients(3 * eta / epsilon - (1 - t), (h, k)),
        "near_joint_scalar_margin": nonnegative_coefficients(
            4 * (e / epsilon + s) * eta - (1 - t) * e - s * (4 * eta - w), (h, k, e, s, w)
        ),
        "away_affine_margin": nonnegative_coefficients(e * (epsilon + w) / epsilon - e, (k, e, w)),
    }
    n = sp.symbols("N", positive=True)
    zero(n * (4 / n) - 4, "large-rank cutoff N epsilon = 4")
    # At N=2,3,4 the other branch is epsilon=1; its condition N<=4 is explicit.
    # m follows from the exact energy identity, not an integration surrogate.
    kinetic, center_e, rank = sp.symbols("kinetic center_e rank", nonnegative=True)
    msymbol = sp.symbols("m", real=True)
    zero(
        center_e
        - (kinetic + 4 * u * rank * (1 - msymbol))
        - (center_e - kinetic - 4 * u * rank + 4 * u * rank * msymbol),
        "central-ground energy identity",
    )
    coarse_v = sp.symbols("coarse_v", real=True)
    expected_at_u = 2 * u * ((rank - msymbol * rank) + (rank - msymbol * (rank - coarse_v)))
    expected_center = 4 * u * rank * (1 - msymbol)
    zero(
        expected_at_u - expected_center - 2 * u * msymbol * coarse_v,
        "unbalanced central-ground trial exact potential difference",
    )
    require(sp.Rational(4, 1) / alpha == sp.Rational(3, 2), "cap energy comparison")
    return {
        "alpha": "8/3",
        "epsilon_N": "min(1,4/N)",
        "parameterization": "eta=h/[2(1+h)], epsilon=1/(1+k); endpoints by continuity",
        "certificates": certificates,
        "large_rank_identity": "N*(4/N)=4; small branch N<=4",
        "principal_angle_margin_squared": "(2)^2-(sqrt(2))^2=2>0",
        "trial_potential_difference": "2*u*m*v(U)",
        "scope": (
            "Exact symbolic scalar identities under declared positivity domains; "
            "no spectral sampling."
        ),
    }


def ground_bundle_geometry():
    if not __debug__:
        raise RuntimeError("Exact controls require assertions enabled")
    q = sp.Symbol("q", nonzero=True)
    c = 8 - q**2 - q**-2
    b = (4 - q**-2) / c
    schur = 4 - (4 - q**-2) * (4 - q**2) / c
    assert sp.cancel(schur - 15 / c) == 0
    root_derivative = 1 / (1 + q)
    bouquet = (sp.Rational(1, 2) - root_derivative) / q
    strip = (b - root_derivative) / q
    bouquet_factor = (q - 1) / (2 * q * (1 + q))
    strip_factor = (q - 1) * (q**2 + 5 * q + 1) / (q**2 * c * (1 + q))
    assert sp.cancel(bouquet - bouquet_factor) == 0
    assert sp.cancel(strip - strip_factor) == 0
    assert bouquet.subs(q, 1) == strip.subs(q, 1) == 0
    # q=exp(t/2), with t the spectral variable of ad(X).
    bouquet_linear = sp.diff(bouquet, q).subs(q, 1) / 2
    strip_linear = sp.diff(strip, q).subs(q, 1) / 2
    assert bouquet_linear == sp.Rational(1, 8)
    assert strip_linear == sp.Rational(7, 24)
    # Converting a coarse alpha E tangent and fiber alpha Z/2 chart
    # multiplies either coefficient by 2 alpha.
    assert 2 * strip_linear == sp.Rational(7, 12)
    assert 2 * bouquet_linear == sp.Rational(1, 4)
    t = sp.Symbol("t", real=True)
    shifted_s = (15 / c).subs(q, sp.exp(t / 2))
    assert sp.simplify(shifted_s.subs(t, -t) - shifted_s) == 0
    assert sp.simplify(sp.diff(shifted_s, t).subs(t, 0)) == 0
    assert sp.simplify(sp.diff(shifted_s, t, 2).subs(t, 0)) == sp.Rational(5, 6)

    # Spin-one matrices give a noncommuting anisotropic kinetic example.
    # D_a are Haar-skew representation generators; the Casimir is central.
    jx = sp.Matrix([[0, 1, 0], [1, 0, 1], [0, 1, 0]]) / sp.sqrt(2)
    jy = sp.Matrix([[0, -sp.I, 0], [sp.I, 0, -sp.I], [0, sp.I, 0]]) / sp.sqrt(2)
    jz = sp.diag(1, 0, -1)
    derivatives = [sp.I * j for j in (jx, jy, jz)]
    casimir = -sum((d * d for d in derivatives), sp.zeros(3))
    coefficients = sp.Matrix([[2, sp.Rational(1, 3), 0], [sp.Rational(1, 3), 3, 0], [0, 0, 4]])
    kinetic = (
        -sum(
            (
                coefficients[a, b] * derivatives[a] * derivatives[b]
                for a in range(3)
                for b in range(3)
            ),
            sp.zeros(3),
        )
        / 2
    )
    assert casimir == 2 * sp.eye(3)
    assert kinetic * casimir == casimir * kinetic
    second_sum = sum(
        ((a * b).adjoint() * (a * b) for a in derivatives for b in derivatives), sp.zeros(3)
    )
    assert second_sum == casimir**2
    # The coefficient floor S>=I makes T>=L/2. Check it exactly in
    # this noncommuting example, including the squared graph estimate.
    psd_minors(coefficients - sp.eye(3))
    psd_minors(kinetic**2 - casimir**2 / 4)
    return {
        "passed": True,
        "scope": (
            "Exact finite metric and lift controls for the near-I ground-bundle proof.\n\n"
            "These check the common rational functions of Ad(H), the first lift\n"
            "coefficients, and a finite SU(2) Casimir identity. They do not certify\n"
            "the uniform ground derivative, gap or projected-form theorem."
        ),
        "strip_schur_identity": "15/(8-q^2-q^-2)",
        "bouquet_residual_factor": str(sp.factor(bouquet)),
        "strip_residual_factor": str(sp.factor(strip)),
        "residual_at_identity": ["0", "0"],
        "ad_X_linear_coefficients": [str(bouquet_linear), str(strip_linear)],
        "strip_scaled_Z_coefficient": "7/12",
        "strip_S_second_derivative_at_identity": "5/6",
        "spin_one_casimir": "2 I",
        "exact_second_derivative_sum_equals_L_squared": True,
        "anisotropic_graph_estimate": True,
    }


def exact_matrix(value, label="matrix"):
    """Accept a nonempty square matrix of exact, finite numeric entries."""
    matrix = sp.Matrix(value)
    if not matrix.rows or matrix.rows != matrix.cols:
        raise ValueError(f"{label} must be a nonempty square matrix")
    if any(
        entry.has(sp.Float) or not entry.is_number or entry.is_finite is not True
        for entry in matrix
    ):
        raise ValueError(f"{label} requires exact finite numeric entries")
    return matrix


def trace_psd_certificate(bmat, qmat):
    """Certify Tr(B)Tr(Q)-Tr(BQ)>=0 from exact positive matrix inputs."""
    bmat = exact_matrix(bmat, "B")
    qmat = exact_matrix(qmat, "Q")
    if bmat.shape != qmat.shape:
        raise ValueError("B and Q must have the same shape")
    try:
        bminors, qminors = psd_minors(bmat), psd_minors(qmat)
    except AssertionError as exc:
        raise ValueError("B and Q must be Hermitian positive semidefinite") from exc
    eta = sp.trace(bmat)
    margin = sp.simplify(eta * sp.trace(qmat) - sp.trace(bmat * qmat))
    loss_minors = psd_minors(eta * sp.eye(bmat.rows) - bmat)
    require(margin.is_nonnegative is True, "positive trace comparison")
    return {
        "dimension": bmat.rows,
        "eta": str(eta),
        "margin": str(margin),
        "B_minors": bminors,
        "Q_minors": qminors,
        "loss_minors": loss_minors,
        "commuting": bmat * qmat == qmat * bmat,
    }


def replay_trace_certificate(bmat, qmat, certificate):
    """Recompute every saved matrix margin/minor; reject altered evidence."""
    expected = trace_psd_certificate(bmat, qmat)
    if certificate != expected:
        raise ValueError("Trace certificate differs from exact recomputation")
    return expected


def _rational(value, label):
    if isinstance(value, bool):
        raise ValueError(f"{label} requires an exact rational")
    value = sp.sympify(value)
    if value.is_Rational is not True:
        raise ValueError(f"{label} requires an exact rational")
    return value


def vertical_spectral_budget(rank, u, center_energy, coarse_v, eta=None):
    """Replay scalar near/far inputs, without inventing a rotor eigenvalue.

    The center energy is supplied evidence. On the near branch eta must
    satisfy the proved geometry 3*eta<=v<=4*eta and 0<=eta<=1/2.
    """
    if isinstance(rank, bool) or not isinstance(rank, int) or rank < 2:
        raise ValueError("rank must be an integer at least two")
    u, energy, v = (
        _rational(item, label)
        for item, label in ((u, "u"), (center_energy, "center energy"), (coarse_v, "coarse v"))
    )
    if u <= 0 or energy < 0 or v < 0:
        raise ValueError("u must be positive and energies/coarse v nonnegative")
    epsilon = min(sp.Integer(1), sp.Rational(4, rank))
    if v <= epsilon:
        if eta is None:
            raise ValueError("The near branch requires eta")
        eta = _rational(eta, "eta")
        if not (0 <= eta <= sp.Rational(1, 2) and 3 * eta <= v <= 4 * eta):
            raise ValueError("eta and coarse v violate the near geometric hypotheses")
        t = 1 / (1 + sp.Rational(8, 3) * eta)
        comparison = t * energy + 4 * u * eta
        branch = "near"
    else:
        if eta is not None:
            raise ValueError("The far branch does not use a square-root parameter")
        comparison = u * v
        branch = "far"
    cap = min(energy, epsilon * u)
    affine = energy + (u - energy / epsilon) * v
    require(comparison >= cap and comparison >= affine, "exact scalar transfer")
    return {
        "rank": rank,
        "branch": branch,
        "epsilon": str(epsilon),
        "comparison": str(comparison),
        "spectral_cap": str(cap),
        "affine_lower": str(affine),
        "cap_margin": str(comparison - cap),
        "affine_margin": str(comparison - affine),
        "nonnegative_Wilson_coefficient": bool(u >= energy / epsilon),
    }


def replay_spectral_budget(rank, u, center_energy, coarse_v, eta, certificate):
    expected = vertical_spectral_budget(rank, u, center_energy, coarse_v, eta)
    if certificate != expected:
        raise ValueError("Spectral budget differs from exact recomputation")
    return expected


def compression_leakage_certificate(hamiltonian, retained, low, ground_energy, fast_floor, leakage):
    """Check a finite complete-low-space compression bound with vacuum shift.

    The retained projector is allowed to miss the exact vacuum. The supplied
    low projector must cover every level below the declared spectral floor.
    """
    hamiltonian = exact_matrix(hamiltonian, "Hamiltonian")
    retained = exact_matrix(retained, "retained projector")
    low = exact_matrix(low, "low projector")
    if hamiltonian.shape != retained.shape or low.shape != retained.shape:
        raise ValueError("Hamiltonian and projections must have the same shape")
    energy = _rational(ground_energy, "ground energy")
    floor = _rational(fast_floor, "fast floor")
    leak = _rational(leakage, "leakage")
    if floor <= 0 or not 0 <= leak < 1:
        raise ValueError("A positive fast floor and leakage in [0,1) are required")
    try:
        zero(hamiltonian - hamiltonian.adjoint(), "self-adjoint Hamiltonian")
        for projection in (retained, low):
            zero(projection - projection.adjoint(), "orthogonal projection")
            zero(projection**2 - projection, "idempotent projection")
        zero(hamiltonian * low - low * hamiltonian, "reducing low spectral space")
        identity = sp.eye(hamiltonian.rows)
        shifted = hamiltonian - energy * identity
        psd_minors(shifted)
        if shifted.det() != 0:
            raise ValueError("The specified ground energy is not attained")
        psd_minors(shifted - floor * (identity - low))
        complement = identity - retained
        leakage_minors = psd_minors(leak * low - low * complement * low)
        compression_minors = psd_minors(
            complement * shifted * complement - floor * (1 - leak) * complement
        )
    except AssertionError as exc:
        raise ValueError("Invalid complete low-space, projection or leakage hypothesis") from exc
    return {
        "dimension": hamiltonian.rows,
        "low_rank": low.rank(),
        "retained_rank": retained.rank(),
        "ground_energy": str(energy),
        "fast_floor": str(floor),
        "leakage": str(leak),
        "compressed_floor": str(floor * (1 - leak)),
        "leakage_principal_minors": leakage_minors,
        "compression_principal_minors": compression_minors,
        "low_leakage_nonzero": low * complement * low != sp.zeros(low.rows),
    }


def replay_compression_certificate(
    hamiltonian, retained, low, ground_energy, fast_floor, leakage, certificate
):
    expected = compression_leakage_certificate(
        hamiltonian, retained, low, ground_energy, fast_floor, leakage
    )
    if expected != certificate:
        raise ValueError("Compression certificate differs from exact recomputation")
    return expected


def actual_complement_mechanism():
    if not __debug__:
        raise RuntimeError("Exact controls require assertions enabled")
    rows = []
    for g in (sp.Rational(1, 2), sp.Rational(1, 4), sp.Rational(1, 8)):
        t = g**2
        c, r = ((1 - t**2) / (1 + t**2), 2 * t / (1 + t**2))
        retained = sp.Matrix([[c, 0], [0, c], [r, 0], [0, r]])
        complement = sp.Matrix([[-r, 0], [0, -r], [c, 0], [0, c]])
        assert retained.T * retained == complement.T * complement == sp.eye(2)
        assert retained.T * complement == sp.zeros(2)
        p, q = (retained * retained.T, complement * complement.T)
        low = sp.diag(1, 1, 0, 0)
        h = sp.diag(11, 15, 18, 23) / g**2
        vacuum = sp.eye(4)[:, 0]
        mixed = sp.eye(4)[:, 2]
        assert (q * vacuum).dot(q * vacuum) == r**2 > 0
        assert low * q * low == r**2 * low
        floor = 7 * c**2 / g**2
        fast = complement.T * (h - 11 * sp.eye(4) / g**2) * complement
        assert fast[0, 0] == floor
        assert fast[1, 1] >= floor and fast[0, 1] == fast[1, 0] == 0
        assert floor == (18 - 11) * (1 - r**2) / g**2
        projected = p * mixed
        projected_norm2 = projected.dot(projected)
        projected_energy = (projected.T * h * projected)[0]
        assert projected_norm2 == r**2
        assert projected_energy == r**2 * (11 * c**2 + 18 * r**2) / g**2
        assert projected_norm2 <= 4 * g**4
        assert projected_energy <= 72 * g**2
        constrained = q * mixed
        rayleigh = (constrained.T * (h - 11 * sp.eye(4) / g**2) * constrained)[0] / constrained.dot(
            constrained
        )
        assert rayleigh == floor
        rows.append(
            {
                "g": str(g),
                "vacuum_Q_norm_squared": str(r**2),
                "actual_compressed_floor": str(floor),
                "complete_low_leakage_bound_attained": True,
                "projected_trial_norm_squared": str(projected_norm2),
                "projected_trial_energy": str(projected_energy),
                "projection_energy_over_g_squared": str(projected_energy / g**2),
            }
        )
    g = sp.Symbol("g", positive=True)
    c, r = ((1 - g**4) / (1 + g**4), 2 * g**2 / (1 + g**4))
    assert sp.limit(r**2 * (11 * c**2 + 18 * r**2) / g**4, g, 0) == 44
    assert sp.limit(7 * c**2, g, 0) == 7
    qv = sp.symbols("q0:3")
    zv = sp.symbols("z0:3")
    mixed = sum((a * b for a, b in zip(qv, zv, strict=True)))

    def excitation(poly):
        return sp.expand(
            sum(
                -sp.Rational(3, 2) * sp.diff(poly, a, 2) + sp.sqrt(3) * a * sp.diff(poly, a)
                for a in qv
            )
            + sum(
                -sp.Rational(5, 2) * sp.diff(poly, b, 2) + sp.sqrt(5) * b * sp.diff(poly, b)
                for b in zv
            )
        )

    assert sp.expand(excitation(mixed) - (sp.sqrt(3) + sp.sqrt(5)) * mixed) == 0
    for axis in range(3):
        e = sp.eye(3)[:, axis]
        dq, dz = (e.cross(sp.Matrix(qv)), e.cross(sp.Matrix(zv)))
        derivative = sum(
            dq[i] * sp.diff(mixed, qv[i]) + dz[i] * sp.diff(mixed, zv[i]) for i in range(3)
        )
        assert sp.expand(derivative) == 0
    assert mixed.subs(dict(zip(zv, [-x for x in zv], strict=True)), simultaneous=True) == -mixed
    assert sp.sqrt(3) + sp.sqrt(5) > 2 * sp.sqrt(3)
    assert sp.sqrt(3) + sp.sqrt(5) < 2 * sp.sqrt(5)
    return {
        "passed": True,
        "scope": (
            "Exact finite controls for the actual-complement proof mechanism.\n\n"
            "A rational four-state family checks full-vacuum subtraction, complete low\n"
            "projection leakage, and the small projected-trial energy cost. An invariant\n"
            "harmonic polynomial checks the mixed-shell energy. These are controls of\n"
            "the proof's finite algebra, not a finite replacement for the actual Wilson\n"
            "projection-convergence or infinite-dimensional compression theorem."
        ),
        "rational_cases": rows,
        "normalized_projection_energy_limit": "44",
        "scaled_compressed_floor_limit": "7",
        "physical_mixed_harmonic_excitation": "sqrt(3)+sqrt(5)",
        "mixed_polynomial_Gauss_invariant": True,
        "mixed_fiber_inversion_odd": True,
        "no_inference_that_P_contains_true_vacuum": True,
    }


@lru_cache(maxsize=1)
def _cached_controls():
    if not __debug__:
        raise RuntimeError("Optimized Python is rejected for exact verification")
    return {
        "matrix": abstract_matrix_control(),
        "su2": su2_group_control(),
        "scalar": scalar_budget_control(),
        "ground_bundle": ground_bundle_geometry(),
        "actual_complement": actual_complement_mechanism(),
    }


def exact_nonlinear_controls():
    """Return independent copies so callers cannot mutate cached acceptance."""
    if not __debug__:
        raise RuntimeError("Optimized Python is rejected for exact verification")
    return copy.deepcopy(_cached_controls())
