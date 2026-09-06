"""Preserved exact control functions.

Source: next_local_gradient_tensorization/check_local_gradient_tensorization.py.

Original SHA256: cf277f4574e4db6318efbd1782d217da511019de172a417c4ba790f3196f90ca
Finite algebra only; analytic hypotheses and limits are not certified here.
"""

from __future__ import annotations

import sys
from itertools import product

import sympy as sp


def require(condition, label):
    if not condition:
        raise AssertionError(label)


def psd_pivots(value):
    matrix = sp.Matrix(value)
    require(matrix == matrix.T, "symmetric matrix")
    pivots = []
    for index in range(matrix.rows):
        pivot = matrix[index, index]
        require(pivot >= 0, "nonnegative pivot")
        pivots.append(str(pivot))
        if pivot == 0:
            require(
                all(matrix[index, other] == 0 for other in range(index + 1, matrix.cols)),
                "zero pivot has zero remainder",
            )
            continue
        for row in range(index + 1, matrix.rows):
            for col in range(row, matrix.cols):
                new = matrix[row, col] - matrix[row, index] * matrix[index, col] / pivot
                matrix[row, col] = matrix[col, row] = new
    return pivots


def dot(left, right):
    return sum(coefficient * right.get(word, 0) for word, coefficient in left.items())


def form_entry(left, right, local):
    value = sp.Integer(0)
    for word, coefficient in left.items():
        for other, other_coefficient in right.items():
            for index in range(len(word)):
                if all(word[j] == other[j] for j in range(len(word)) if j != index):
                    value += coefficient * other_coefficient * local[word[index], other[index]]
    return value


def profiles(count):
    vacuum = (0,) * count
    basis = [{vacuum: sp.Integer(1)}]
    labels = ["vacuum"]
    for index in range(count):
        word = list(vacuum)
        word[index] = 1
        basis.append({tuple(word): sp.Integer(1)})
        labels.append(f"radial_{index}")
    for i in range(count):
        for j in range(i + 1, count):
            pair = {}
            for color in range(2, 5):
                word = list(vacuum)
                word[i] = word[j] = color
                pair[tuple(word)] = sp.Integer(1)
            basis.append(pair)
            labels.append(f"pair_{i}_{j}")
    return labels, basis


def matrix_on(basis, operation):
    return sp.Matrix([[operation(left, right) for right in basis] for left in basis])


def controls():
    if sys.flags.optimize:
        raise RuntimeError("Exact controls require assertions enabled")
    rational = sp.Rational
    local = sp.diag(0, 4, 2, 2, 2)
    v = sp.Matrix([0, 1, 1, 0, 0])
    w = sp.Matrix([0, 0, 0, 1, 1])
    bad = (v * v.T + w * w.T) / 10
    require(bad[1, 2] != 0 and bad[3, 4] != 0, "nontrivial local off-diagonal terms")
    require(local[:, 0] == bad[:, 0] == sp.zeros(5, 1), "forms kill constants exactly")
    epsilon = rational(1, 20)
    cases = []
    for count in (1, 2, 3, 5):
        labels, basis = profiles(count)
        gram = matrix_on(basis, dot)
        full_matrix = matrix_on(basis, lambda x, y: form_entry(x, y, local))
        bad_matrix = matrix_on(basis, lambda x, y: form_entry(x, y, bad))
        pairs = count * (count - 1) // 2
        expected_gram = sp.diag(1, *([1] * count), *([3] * pairs))
        expected_full = sp.diag(0, *([4] * count), *([12] * pairs))
        expected_bad = sp.diag(0, *([rational(1, 10)] * count), *([rational(3, 5)] * pairs))
        require(gram == expected_gram, "actual tensor profile Gram")
        require(full_matrix == expected_full, "complete tensor full form")
        require(bad_matrix == expected_bad, "all bad cross terms cancel")
        relative_slack = epsilon * full_matrix - bad_matrix
        pivots = psd_pivots(relative_slack)
        require(
            all(
                bad_matrix[i, j] == 0
                for i in range(len(basis))
                for j in range(len(basis))
                if i != j
            ),
            "radial/pair and overlapping-pair cancellation",
        )
        cases.append(
            {
                "copies": count,
                "full_profile_dimension": len(basis),
                "pair_singlets": pairs,
                "labels": labels,
                "profile_Gram_diagonal": [str(gram[i, i]) for i in range(len(basis))],
                "full_form_diagonal": [str(full_matrix[i, i]) for i in range(len(basis))],
                "bad_form_diagonal": [str(bad_matrix[i, i]) for i in range(len(basis))],
                "relative_slack_PSD_pivots": pivots,
                "offdiagonal_zero": True,
            }
        )
    # If an alleged excitation is not centered, the exact-support assertion fails.
    radial = {(1, 0): sp.Integer(1)}
    noncentered_pair = {word: sp.Integer(1) for word in product((0, 2), repeat=2)}
    noncentered_cross = form_entry(radial, noncentered_pair, bad)
    require(noncentered_cross == rational(1, 10), "missing-centering negative")
    any_bad = []
    p = rational(1, 4)
    for count in (1, 2, 3, 5, 10):
        # Derivative in coordinate zero is supported in its good region. Other
        # coordinates are independent vacuum draws; enumerate their bad events.
        exact = sp.Integer(0)
        for states in product((0, 1), repeat=count - 1):
            probability = sp.prod(p if item else 1 - p for item in states)
            if any(states):
                exact += probability
        require(exact == 1 - (1 - p) ** (count - 1), "global any-bad enumeration")
        any_bad.append(
            {
                "copies": count,
                "global_bad_gradient_ratio": str(exact),
                "sum_local_bad_gradient_ratio": "0",
            }
        )
    # Conditional score cross covariance, including nonscalar source derivatives.
    weights = [rational(2, 3), rational(-5, 7), rational(11, 4)]
    score_norm = (
        sum(
            sum(weight * state for weight, state in zip(weights, states, strict=True)) ** 2
            for states in product((-1, 1), repeat=3)
        )
        / 8
    )
    require(score_norm == sum(item**2 for item in weights), "centered independent score covariance")
    return {
        "passed": True,
        "local_full_form": [[str(item) for item in row] for row in local.tolist()],
        "local_bad_form": [[str(item) for item in row] for row in bad.tolist()],
        "local_bad_PSD_pivots": psd_pivots(bad),
        "local_domination_PSD_pivots": psd_pivots(local - bad),
        "local_radial_ratio": "1/40",
        "local_adjoint_trace_ratio": "1/20",
        "uniform_relative_bound": str(epsilon),
        "tensor_cases": cases,
        "noncentered_profile_negative_cross": str(noncentered_cross),
        "global_bad_event_counterexample": any_bad,
        "centered_product_score_squared_norm": str(score_norm),
        "scope": (
            "Exact finite tensor forms with nonzero local radial/adjoint "
            "and adjoint cross entries, "
            "full low-profile superpositions, missing-centering and any-bad negatives. "
            "No Wilson derivative rate, interacting product structure "
            "or countable proof is certified."
        ),
    }
