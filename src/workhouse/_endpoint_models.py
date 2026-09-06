"""Preserved exact control functions.

Source: next_full_window_comparison/check_literal_endpoint_window.py.

Original SHA256: c003fbe9429de59150dc7f4f5d41fb608ebe6e88e787228a673915996a8b3ee8
Finite algebra only; analytic hypotheses and limits are not certified here.
"""

from __future__ import annotations

import math
import sys

import sympy as sp


def require(condition, label):
    if not condition:
        raise AssertionError(label)


def inertia(value):
    """Exact rational symmetric congruence, including zero diagonal pivots."""
    matrix = sp.Matrix(value)
    require(matrix == matrix.T, "symmetric matrix")
    require(all(entry.is_Rational for entry in matrix), "rational entries")
    signs = [0, 0, 0]  # positive, negative, zero
    while matrix.rows:
        pivot = next((i for i in range(matrix.rows) if matrix[i, i]), None)
        if pivot is None:
            pair = next(
                (
                    (i, j)
                    for i in range(matrix.rows)
                    for j in range(i + 1, matrix.cols)
                    if matrix[i, j]
                ),
                None,
            )
            if pair is None:
                signs[2] += matrix.rows
                break
            i, j = pair
            change = sp.eye(matrix.rows)
            change[j, i] = 1
            matrix = change.T * matrix * change
            pivot = i
        order = [pivot, *(i for i in range(matrix.rows) if i != pivot)]
        matrix = matrix.extract(order, order)
        diagonal = matrix[0, 0]
        signs[0 if diagonal > 0 else 1] += 1
        matrix = matrix[1:, 1:] - matrix[1:, :1] * matrix[:1, 1:] / diagonal
    return signs


def psd(matrix, label):
    signs = inertia(matrix)
    require(signs[1] == 0, label)
    return signs


def encode(matrix):
    return [[str(entry) for entry in row] for row in matrix.tolist()]


def endpoint_and_two_lag_controls():
    energies = (0, 1, 4, 9, 20)
    h = sp.diag(*energies)
    q = sp.Matrix([0, 48, 64, 1599, 0]) / 1601
    require((q.T * q)[0] == 1, "normalized missing direction")
    direction = sp.eye(5)[:, 3] - q
    rotation = sp.eye(5) - 2 * direction * direction.T / (direction.T * direction)[0]
    require(rotation.T * rotation == sp.eye(5), "rational source isometry")
    source = rotation[:, [0, 1, 2, 4]]
    p = source * source.T
    discarded = q * q.T
    require(p + discarded == sp.eye(5), "entire retained/omitted decomposition")
    require(source[:, 0] == sp.eye(5)[:, 0], "exact vacuum retained")
    low = sp.diag(1, 1, 1, 0, 0)
    loss = (q.T * low * q)[0]
    gamma = 1 - loss
    psd(low * p * low - gamma * low, "complete low source frame")
    inverse = sp.diag(0, 1, sp.Rational(1, 4), sp.Rational(1, 9), sp.Rational(1, 20))
    cap = (q.T * inverse * q)[0]
    floor = 1 / cap
    psd(h - floor * discarded, "full inverse-energy floor")
    require(floor > 4, "entire first cluster lies below the full fast coefficient")

    # tau=log(2), so all heat matrices are exactly rational.
    heat = sp.diag(*(sp.Rational(1, 2**energy) for energy in energies))
    a = source.T * heat * source
    a2 = source.T * heat**2 * source
    a3 = source.T * heat**3 * source
    v = a2 - a**2
    require(
        v == source.T * heat * discarded * heat * source, "established two-lag leakage identity"
    )
    psd(v, "equal-time memory is positive")
    require(v.rank() == 1 and v != sp.zeros(4), "nonzero irreducible leakage")
    require(a * a2 != a2 * a, "different endpoint transfers need not commute")
    require(
        a3 - a * a2 == source.T * heat * discarded * heat**2 * source, "unequal-lag exact memory"
    )
    psd(a2 - a**2, "pre-log dyadic order")

    high_heat = sp.Rational(1, 512)
    low_heat = sp.Rational(1, 2)
    d = gamma * high_heat + (1 - gamma) * low_heat
    actual_d = (q.T * heat * q)[0]
    require(actual_d <= d, "whole discarded transfer tail from complete frame")
    rows = []
    for threshold, expected in (
        (sp.Rational(3, 4), 1),
        (sp.Rational(1, 4), 2),
        (sp.Rational(1, 32), 3),
    ):
        require(threshold > d, "resolvent threshold exceeds entire discarded tail")
        lower = inertia(a - threshold * sp.eye(4))[0]
        upper_matrix = a - threshold * sp.eye(4) + v / (threshold - d)
        upper = inertia(upper_matrix)[0]
        exact = inertia(heat - threshold * sp.eye(5))[0]
        exact_schur = a - threshold * sp.eye(4) + v / (threshold - actual_d)
        require(
            lower == upper == exact == inertia(exact_schur)[0] == expected,
            "complete finite spectral count",
        )
        psd(upper_matrix - exact_schur, "matrix resolvent majorant")
        rows.append(
            {
                "threshold": str(threshold),
                "lower_count": lower,
                "upper_count": upper,
                "full_count": exact,
            }
        )
    require(
        inertia(a - sp.Rational(1, 2) * sp.eye(4))[0] == 1,
        "first source energy upper transfer bound",
    )
    require(inertia(a - gamma / 2 * sp.eye(4))[0] == 2, "first source energy lower transfer bound")
    require(
        inertia(a - sp.Rational(1, 16) * sp.eye(4))[0] == 2, "second source upper transfer bound"
    )
    require(inertia(a - gamma / 16 * sp.eye(4))[0] == 3, "second source lower transfer bound")
    # The fourth retained source is genuinely high; it was never omitted.
    require(a[3, 3] == sp.Rational(1, 2**20), "retained high source kept in all counts")
    return {
        "fine_energies": list(energies),
        "source_dimension": 4,
        "complete_low_rank": 3,
        "tau": "log(2)",
        "frame_lower": str(gamma),
        "full_fast_coefficient": str(floor),
        "A_tau": encode(a),
        "V_tau": encode(v),
        "actual_discarded_transfer": str(actual_d),
        "proven_discarded_transfer_bound": str(d),
        "threshold_counts": rows,
        "different_lags_noncommuting": True,
        "pre_log_dyadic_order": True,
        "scope": (
            "Exact five-state complete cluster, retained high state, full-form "
            "and two-lag matrix controls."
        ),
    }


def marginal_cutoff_counterexample():
    high = sp.Integer(4096)
    h = sp.diag(0, 1, high)
    source = sp.Matrix([0, sp.Rational(24, 25), sp.Rational(7, 25)])
    p = sp.diag(1, 0, 0) + source * source.T
    q = sp.eye(3) - p
    psd(h - 12 * q, "large full fast coefficient survives")
    marginal = (source.T * h * source)[0]
    require(marginal > 100, "fixed marginal-energy cutoff discards the fine energy-one source")
    overlap = source[1] ** 2
    heat_source = overlap / 2 + source[2] ** 2 / 2**high
    require(
        overlap / 2 < heat_source < sp.Rational(1, 2),
        "exact endpoint retains the fine low transition",
    )
    n = sp.symbols("n", positive=True)
    cosine, sine = (n**2 - 1) / (n**2 + 1), 2 * n / (n**2 + 1)
    require(sp.cancel(cosine**2 + sine**2 - 1) == 0, "normalized symbolic source family")
    energy = cosine**2 + n**6 * sine**2
    fast = 1 / (sine**2 + cosine**2 / n**6)
    require(sp.limit(cosine**2, n, sp.oo) == 1, "source frame tends to one")
    require(
        sp.limit(energy, n, sp.oo) == sp.oo and sp.limit(fast, n, sp.oo) == sp.oo,
        "marginal energy diverges despite growing full fast floor",
    )
    return {
        "fine_gap": "1",
        "high_energy": str(high),
        "verified_full_fast_floor": "12",
        "low_source_frame": str(overlap),
        "marginal_source_energy": str(marginal),
        "endpoint_transfer": "576/(625*2)+49/(625*2^4096)",
        "source_frame_limit": "1",
        "marginal_energy_limit": "infinity",
        "fast_coefficient_limit": "infinity",
        "scope": (
            "Finite self-adjoint source model; not asserted to be an actual Wilson or Markov model."
        ),
    }


def polynomial_product(first, second, degree):
    dimension = first[0].rows
    return [
        sum((first[i] * second[k - i] for i in range(k + 1)), sp.zeros(dimension))
        for k in range(degree + 1)
    ]


def markov_log_counterexample():
    laplace = sp.Matrix([[-1, 1, 0, 0], [1, -2, 1, 0], [0, 1, -2, 1], [0, 0, 1, -1]])
    require(laplace * sp.ones(4, 1) == sp.zeros(4, 1), "fine generator fixes constants")
    require(
        all(laplace[i, j] >= 0 for i in range(4) for j in range(4) if i != j), "fine Markov rates"
    )
    coarse = sp.Matrix([[1, 0, 0], [0, 1, 0], [0, 1, 0], [0, 0, 1]])
    marginal = sp.diag(sp.Rational(1, 4), sp.Rational(1, 2), sp.Rational(1, 4))
    compression = marginal.inv() * coarse.T / 4
    degree = 4
    series = [compression * laplace**k * coarse / math.factorial(k) for k in range(degree + 1)]
    require(series[0] == sp.eye(3), "normalized coarse source")
    for k, coefficient in enumerate(series):
        require(
            marginal * coefficient == coefficient.T * marginal,
            "exact detailed balance at each order",
        )
        require(
            coefficient * sp.ones(3, 1) == (sp.ones(3, 1) if k == 0 else sp.zeros(3, 1)),
            "coarse constants at each order",
        )
    base = list(series)
    base[0] = sp.zeros(3)
    power = [sp.eye(3), *(sp.zeros(3) for _ in range(degree))]
    logarithm = [sp.zeros(3) for _ in range(degree + 1)]
    for k in range(1, degree + 1):
        power = polynomial_product(power, base, degree)
        logarithm = [
            old + sp.Rational((-1) ** (k + 1), k) * new
            for old, new in zip(logarithm, power, strict=True)
        ]
    require(
        series[1][0, 2] == series[2][0, 2] == 0 and series[3][0, 2] == sp.Rational(1, 6),
        "three-edge endpoint distance",
    )
    require(
        logarithm[1][0, 2] == 0 and logarithm[2][0, 2] == -sp.Rational(1, 4),
        "negative logarithmic Markov rate",
    )
    return {
        "fine_generator": encode(laplace),
        "coarse_marginal": ["1/4", "1/2", "1/4"],
        "first_coarse_generator": encode(series[1]),
        "endpoint_13_first_order": "tau^3/6",
        "log_transition_13_first_order": "-tau^2/4",
        "negative_Markov_rate_for_small_positive_tau": True,
        "scope": (
            "Exact Taylor coefficients of a genuine finite reversible semigroup "
            "compression; the sign persists analytically for small positive tau."
        ),
    }


def conditional_clock_budget():
    rows = []
    product = sp.Integer(1)
    for j in range(1, 9):
        spacing = sp.Rational(1, 2**j)
        fast = 1 / spacing
        tau = spacing * (j + 1) ** 2
        loss = 1 / (tau * (fast - sp.Rational(1, 4)))
        require(loss <= sp.Rational(2, (j + 1) ** 2), "summable physical-time loss majorant")
        product /= 1 + loss
        rows.append({"j": j, "spacing": str(spacing), "physical_time": str(tau), "loss": str(loss)})
    x = sp.symbols("x", nonnegative=True)
    ratio = x / (2 * (1 + x))
    require(
        sp.cancel(2 - 1 / (1 - ratio) - 2 / (x + 2)) == 0,
        "arbitrary-symbol eventual factor-two bound",
    )
    return {
        "finite_steps": rows,
        "finite_gap_factor": str(product),
        "scope": (
            "Exact finite and scalar controls of a conditional hierarchy budget; "
            "no interacting hierarchy is constructed."
        ),
    }


def controls():
    if sys.flags.optimize:
        raise RuntimeError("Exact verification requires assertions enabled")
    require(inertia(sp.Matrix([[0, 1], [1, 0]])) == [1, 1, 0], "zero-diagonal inertia control")
    return {
        "endpoint_and_two_lag": endpoint_and_two_lag_controls(),
        "marginal_cutoff_counterexample": marginal_cutoff_counterexample(),
        "Markov_log_counterexample": markov_log_counterexample(),
        "conditional_clock_budget": conditional_clock_budget(),
    }
