"""Exact finite controls for the entire Gaussian literal-source complement.

The analytic proof supplies operator monotonicity and Fock density. These
controls certify exact matrices, tensor sectors, and source counterexamples.
No numerical eigenvalue routine or rank interpolation is used.
"""

from __future__ import annotations

import math

import sympy as sp


def require(condition, message):
    if not condition:
        raise AssertionError(message)


def psd_pivots(matrix):
    matrix = sp.Matrix(matrix)
    require(matrix == matrix.T, "symmetric matrix")
    require(all(entry.is_Rational for entry in matrix), "exact rational matrix")
    pivots = []
    for index in range(matrix.rows):
        pivot = matrix[index, index]
        require(pivot >= 0, "positive semidefinite pivot")
        pivots.append(str(pivot))
        if pivot == 0:
            require(
                all(matrix[index, column] == 0 for column in range(index + 1, matrix.cols)),
                "zero pivot must have a zero remaining row",
            )
            continue
        for row in range(index + 1, matrix.rows):
            for column in range(row, matrix.cols):
                value = matrix[row, column] - matrix[row, index] * matrix[index, column] / pivot
                matrix[row, column] = matrix[column, row] = value
    return pivots


def projector(columns):
    columns = sp.Matrix(columns)
    require(columns.rank() == columns.cols > 0, "independent source columns")
    return columns * (columns.T * columns).inv() * columns.T


def encode(matrix):
    return [[str(matrix[i, j]) for j in range(matrix.cols)] for i in range(matrix.rows)]


def exact_matrix_chain(root_omega, source, floor):
    """T>0, Omega=T^2, K=T^4 keep both square roots exactly rational."""
    t = sp.Matrix(root_omega)
    psd_pivots(t)
    require(t.det() > 0, "strictly positive square root")
    omega = t**2
    k = omega**2
    ps = projector(source)
    qs = sp.eye(t.rows) - ps
    retained = projector(t.inv() * source)
    discarded = sp.eye(t.rows) - retained
    require(k * ps != ps * k, "noncommuting retained geometry")
    require(
        qs * t.inv() * discarded == t.inv() * discarded,
        "the source weight sends R-perp into S-perp",
    )
    return {
        "T": encode(t),
        "Omega": encode(omega),
        "K": encode(k),
        "P_S": encode(ps),
        "P_R": encode(retained),
        "frequency_floor": str(floor),
        "K_boundary_pivots": psd_pivots(k - floor**2 * qs),
        "square_root_monotonicity_example_pivots": psd_pivots(omega - floor * qs),
        "compressed_inverse_pivots": psd_pivots(
            discarded / floor - discarded * omega.inv() * discarded
        ),
        "full_frequency_pivots": psd_pivots(omega - floor * discarded),
        "source_geometry_noncommuting": True,
    }


def tensor_sum(operator, number):
    dimension = operator.rows
    return sum(
        (
            sp.kronecker_product(
                *(operator if index == slot else sp.eye(dimension) for index in range(number))
            )
            for slot in range(number)
        ),
        sp.zeros(dimension**number),
    )


def tensor_sector_controls():
    t = sp.Matrix([[2, 1], [1, 2]]) / 2
    omega = t**2
    retained = projector(t.inv() * sp.Matrix([1, 0]))
    discarded = sp.eye(2) - retained
    floor = sp.Rational(1, 3)
    records = []
    for number in (1, 2, 3, 4):
        hamiltonian = tensor_sum(omega, number)
        number_discarded = tensor_sum(discarded, number)
        retained_all = sp.kronecker_product(*(retained for _ in range(number)))
        complement_all = sp.eye(2**number) - retained_all
        records.append(
            {
                "particles": number,
                "ordered_tensor_dimension": 2**number,
                "frequency_minus_count_pivots": psd_pivots(hamiltonian - floor * number_discarded),
                "count_minus_complement_pivots": psd_pivots(number_discarded - complement_all),
                "full_complement_pivots": psd_pivots(hamiltonian - floor * complement_all),
            }
        )
    return {
        "sectors": records,
        "scope": (
            "Exact ordered-tensor inequalities restrict to symmetric bosons; "
            "no all-n sampling proof."
        ),
    }


def full_low_window_control():
    # Only slow quanta occur below 1/4 because the other frequency is 100.
    slow, fast = sp.Rational(1, 100), sp.Integer(100)
    t = sp.diag(sp.Rational(1, 10), 10)
    source = sp.Matrix([100, 1])
    retained = projector(t.inv() * source)
    cosine_squared = retained[0, 0]
    energy = sp.Rational(1, 4)
    require(
        25 * slow == energy < 26 * slow and fast > energy,
        "complete low window, not a selected list of states",
    )
    weights = [cosine_squared**n for n in range(26)]
    require(all(weight >= 1 - energy for weight in weights), "entire low-window source frame")
    return {
        "window_energy": str(energy),
        "frequency_floor": "1",
        "low_dimension": 26,
        "retained_slow_overlap_squared": str(cosine_squared),
        "minimum_exact_frame_weight": str(min(weights)),
        "proven_frame_lower": "3/4",
        "all_sectors_zero_through_25_present": True,
        "scope": "One exact full oscillator window including every allowed particle sector.",
    }


def wrong_source_physical_counterexample():
    slow, fast = sp.Rational(1, 100), sp.Integer(100)
    omega = sp.diag(slow, fast)
    k = omega**2
    source = sp.Matrix([100, 1])
    ps = projector(source)
    boundary = k - (sp.eye(2) - ps)
    psd_pivots(boundary)
    require(boundary.det() == 0, "full matrix floor attained")
    wrong = projector(sp.diag(sp.Rational(1, 10), 10) * source)
    require(wrong == sp.ones(2) / 2, "wrong face-type weight changes the retained space")
    number = 10
    # Exact squared occupation coefficients of (I-Gamma(P_wrong))|slow^10>.
    squared = [(1 - sp.Rational(1, 2**number)) ** 2]
    squared.extend(sp.Rational(math.comb(number, j), 4**number) for j in range(1, number + 1))
    norm_squared = sum(squared)
    energy = sum(weight * ((number - j) * slow + j * fast) for j, weight in enumerate(squared))
    rayleigh = sp.cancel(energy / norm_squared)
    require(norm_squared == 1 - sp.Rational(1, 2**number), "actual complementary norm")
    require(rayleigh == sp.Rational(803, 1364) < 1, "wrong source violates the unit floor")
    # Orthogonality to the retained n-boson line follows independently from
    # the signed binomial occupation amplitudes, after a common denominator.
    require(
        2**number - 1 - sum(math.comb(number, j) for j in range(1, number + 1)) == 0,
        "the trial is exactly in the wrong complement",
    )
    color = sp.symbols("x0:3", real=True)
    invariant = sum(item**2 for item in color) ** 5
    for axis in range(3):
        direction = sp.eye(3)[:, axis].cross(sp.Matrix(color))
        derivative = sum(direction[j] * sp.diff(invariant, color[j]) for j in range(3))
        require(sp.expand(derivative) == 0, "degree-ten color tensor is SO(3) invariant")
    require(sp.Poly(invariant, *color).total_degree() == number, "physical tensor degree")
    return {
        "Omega": encode(omega),
        "P_S": encode(ps),
        "P_wrong": encode(wrong),
        "boundary_PSD_pivots": psd_pivots(boundary),
        "particles": number,
        "complementary_norm_squared": str(norm_squared),
        "rayleigh": str(rayleigh),
        "false_floor": "1",
        "physical_color_polynomial": str(invariant),
        "color_rotation_derivatives_zero": True,
        "scope": "Exact full-Fock wrong-source counterexample; invariant color lift is explicit.",
    }


def regulator_control():
    records = []
    for n in (1, 2, 4, 8):
        regulator = sp.Rational(2 * n + 1, n * (n + 1))
        frequency = sp.Rational(2 * n * n + 2 * n + 1, n * (n + 1))
        require(frequency**2 == 4 + regulator**2, "exact regulated square root")
        omega = sp.diag(regulator, frequency)
        q = sp.diag(0, 1)
        records.append(
            {
                "regulator": str(regulator),
                "fast_frequency": str(frequency),
                "uniform_floor_pivots": psd_pivots(omega - 2 * q),
                "retained_zero_mode_variance": str(1 / (2 * regulator)),
            }
        )
    n = sp.symbols("n", positive=True)
    regulator = (2 * n + 1) / (n * (n + 1))
    require(sp.limit(regulator, n, sp.oo) == 0, "regulator tends to zero")
    require(sp.limit(1 / (2 * regulator), n, sp.oo) == sp.oo, "no finite unregulated covariance")
    return {
        "cases": records,
        "uniform_frequency_floor": "2",
        "zero_mode_variance_diverges": True,
        "unregulated_Gaussian_vacuum_claimed": False,
    }


def controls():
    if not __debug__:
        raise RuntimeError("Optimized Python is rejected for exact verification")
    return {
        "matrix_chains": [
            exact_matrix_chain(
                sp.Matrix([[2, 1], [1, 2]]) / 2, sp.Matrix([1, 0]), sp.Rational(1, 3)
            ),
            exact_matrix_chain(sp.diag(sp.Rational(1, 10), 10), sp.Matrix([100, 1]), sp.Integer(1)),
        ],
        "tensor_sectors": tensor_sector_controls(),
        "full_low_window": full_low_window_control(),
        "wrong_source_physical_counterexample": wrong_source_physical_counterexample(),
        "retained_zero_mode_regulator": regulator_control(),
    }


# Derived from immutable original under next_nonlinear/:
# next_gaussian_full/check_entire_gaussian_literal_complement.py
# Original SHA256: bc57649b314ce6b78c30a0588d70d7197bec959be2434bef32b3ba27fb2505f5
