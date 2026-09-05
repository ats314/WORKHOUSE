"""Exact finite Schur, vacuum, gap and entire-window graph-frame controls.

These are matrix controls of the analytic closed-form theorem, not a
verification of an actual Wilson coarse/fine factorization.
"""
from __future__ import annotations

import itertools
import json
import sys
from pathlib import Path

import sympy as s

sys.dont_write_bytecode = True


def positive_semidefinite(matrix):
    assert matrix == matrix.T
    return all(matrix.extract(indices, indices).det() >= 0
               for k in range(1, matrix.rows + 1)
               for indices in itertools.combinations(range(matrix.rows), k))


def controls():
    # Large cross term: static K0 without the graph norm gives a false gap.
    eigenvalue = 3 - 2 * s.sqrt(2)
    assert eigenvalue >= s.Rational(1, 6)
    assert eigenvalue <= s.Rational(1, 5)
    assert eigenvalue < s.Rational(1, 2)

    fine = s.diag(2, 5)
    lift = s.Matrix([[1, s.Rational(1, 2)], [-s.Rational(2, 3), s.Rational(3, 4)]])
    static = s.Matrix([[1, -1], [-1, 1]])
    mass = s.eye(2) + lift.T * lift
    assert mass * static != static * mass
    hamiltonian = (static + lift.T * fine * lift).row_join(lift.T * fine)
    hamiltonian = hamiltonian.col_join((fine * lift).row_join(fine))
    triangular = s.eye(4)
    triangular[2:, :2] = -lift
    assert triangular.T * hamiltonian * triangular == s.diag(static, fine)
    null = s.Matrix([1, 1]).col_join(-lift * s.Matrix([1, 1]))
    assert hamiltonian * null == s.zeros(4, 1)
    assert hamiltonian.rank() == 3

    shift_rows = []
    for z in [s.Rational(1, 3), s.Rational(1), s.Rational(3, 2)]:
        resolvent = (fine - z * s.eye(2)).inv()
        lifted = lift + z * resolvent * lift
        remainder = lift.T * resolvent * lift
        schur = static - z * mass - z * z * remainder
        transform = s.eye(4)
        transform[2:, :2] = -lifted
        assert transform.T * (hamiltonian - z * s.eye(4)) * transform == s.diag(
            schur, fine - z * s.eye(2)
        )
        assert positive_semidefinite((mass - s.eye(2)) / (2 - z) - remainder)
        assert positive_semidefinite(schur - (static - 2 * z / (2 - z) * mass))
        variable = s.symbols("t")
        full_negative = hamiltonian.charpoly(variable).as_poly().count_roots(-s.oo, z)
        schur_negative = schur.charpoly(variable).as_poly().count_roots(-s.oo, 0)
        assert full_negative == schur_negative
        shift_rows.append({"z": str(z), "negative_index": int(full_negative)})

    mu = s.trace(mass.inv() * static)
    lower = 2 * mu / (2 + mu)
    variable = s.symbols("t")
    nonzero_polynomial = s.Poly(s.cancel(hamiltonian.charpoly(variable).as_expr() / variable),
                               variable)
    assert nonzero_polynomial.count_roots(0, lower) == 0
    assert nonzero_polynomial.count_roots(0, mu) >= 1

    # Rational actual low-window projector, independent of any eigenvector fit.
    rotation13 = s.Matrix([[s.Rational(4, 5), 0, s.Rational(3, 5)],
                           [0, 1, 0],
                           [-s.Rational(3, 5), 0, s.Rational(4, 5)]])
    rotation23 = s.Matrix([[1, 0, 0],
                           [0, s.Rational(12, 13), s.Rational(5, 13)],
                           [0, -s.Rational(5, 13), s.Rational(12, 13)]])
    rotation = rotation13 * rotation23
    assert rotation.T * rotation == s.eye(3)
    energy = s.Rational(1, 4)
    full = rotation * s.diag(0, energy, 5) * rotation.T
    window = rotation * s.diag(1, 1, 0) * rotation.T
    floor = full[2, 2]
    u = full[2:, :2] / floor
    graph = s.eye(2).col_join(-u)
    metric = s.eye(2) + u.T * u
    graph_projection = graph * metric.inv() * graph.T
    frame_lower = 1 - (energy / floor) ** 2
    assert energy < floor
    assert graph_projection * graph_projection == graph_projection
    assert positive_semidefinite(window * graph_projection * window - frame_lower * window)
    assert (window * graph).rank() == window.rank() == 2
    assert (full * window)[2:, :] == floor * (window[2:, :] + u * window[:2, :])

    inverse_gap = s.Rational(7)
    for j in range(8):
        fast = 3 * 2 ** j
        next_gap = fast / (1 + fast * inverse_gap)
        inverse_gap = s.cancel(1 / next_gap)
    expected_inverse = 7 + s.Rational(2, 3) * (1 - s.Rational(1, 2) ** 8)
    assert inverse_gap == expected_inverse

    return {
        "scope": __doc__,
        "large_cross_term": {"actual_low_energy": str(eigenvalue),
                             "mu": "1/5", "lower_bound": "1/6",
                             "omitted_mass_false_bound": "1/2"},
        "noncommuting_shift_controls": shift_rows,
        "vacuum_graph_dimension": 1,
        "noncommuting_coarse_positive_energy": str(mu),
        "noncommuting_full_gap_bracket": [str(lower), str(mu)],
        "whole_window": {"rank": 2, "energy": str(energy), "fast_floor": str(floor),
                         "frame_lower": str(frame_lower), "onto_rank": 2},
        "eight_step_inverse_gap_budget": str(inverse_gap),
    }


if __name__ == "__main__":
    if sys.flags.optimize:
        raise RuntimeError("Assertions must be enabled")
    target = Path(__file__).with_suffix(".json")
    if target.exists():
        raise FileExistsError("Existing evidence is preserved; select a fresh output")
    result = controls()
    target.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8", newline="\n")
    print(json.dumps(result, indent=2))
