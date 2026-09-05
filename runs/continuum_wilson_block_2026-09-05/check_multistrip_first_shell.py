"""Exact first-shell effective matrix controls for two edge-disjoint strips.

These finite Gaussian computations verify the stated second-order effective
matrix, not the analytic eigenvalue remainder or a multi-block RG theorem.
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path

import sympy as s
from check_multistrip_selfenergy import expectation
from check_strip_born_oppenheimer_audit import su_basis


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
    q1, q2 = s.Matrix(s.symbols("q10:13")), s.Matrix(s.symbols("q20:23"))
    variables = list(q1) + list(q2)
    variances = [s.sqrt(3) / 2] * 6
    r1, r2 = q1.dot(q1), q2.dot(q2)
    states = [r1 - 3 * s.sqrt(3) / 2, r2 - 3 * s.sqrt(3) / 2, q1.dot(q2)]

    def angular(f: s.Expr, q: s.Matrix) -> s.Matrix:
        return q.cross(s.Matrix([s.diff(f, x) for x in q]))

    angulars = [(angular(f, q1), angular(f, q2)) for f in states]
    gram = s.Matrix([[expectation(f * h, variables, variances) for h in states] for f in states])
    assert gram == s.diag(s.Rational(9, 2), s.Rational(9, 2), s.Rational(9, 4))
    # The Q-independent fiber and Haar constants cancel in gaps.
    potential = -3 * s.sqrt(5) * (r1 + r2) / 320 - (r1**2 + r2**2) / 192
    vacuum_expectation = expectation(potential, variables, variances)
    effective = s.zeros(3)
    for i, f in enumerate(states):
        for j, h in enumerate(states):
            angular_form = sum(x.dot(y) for x, y in zip(angulars[i], angulars[j], strict=True))
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
    # Dropping the direct metric term reverses the sign of this splitting.
    bad_split = s.Rational(201, 320) - 3
    assert bad_split < 0
    return {
        "basis": ["centered |Q1|^2", "centered |Q2|^2", "Q1 dot Q2"],
        "gram": str(gram),
        "effective_matrix_relative_to_ground": str(normalized),
        "mixed_minus_local": "201/320",
        "omitted_metric_negative_control_split": str(bad_split),
    }


def exact_control() -> dict:
    return {
        "scope": __doc__,
        "general_moments": general_moments(),
        "direct_matrix_trace_Wick_contractions": matrix_trace_contractions(),
        "explicit_SU2_first_shell_matrix": explicit_su2_matrix(),
        "source_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    }


if __name__ == "__main__":
    result = exact_control()
    with (
        Path(__file__)
        .with_name("multistrip_first_shell_controls.json")
        .open("x", encoding="utf-8") as handle
    ):
        json.dump(result, handle, indent=2)
        handle.write("\n")
    print(json.dumps(result, indent=2))
