"""Exact product-vacuum mismatch and local-dressing controls.

Finite qubit controls illustrate an analytic obstruction to a raw fast
projection. They do not certify a nonlinear Wilson block projection.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

import sympy as s

sys.dont_write_bytecode = True


def tensor(items):
    result = s.Matrix([[1]])
    for item in items:
        result = s.kronecker_product(result, item)
    return result


def controls():
    c, sine = s.Rational(3, 5), s.Rational(4, 5)
    omega = s.Matrix([c, sine])
    rotation = s.Matrix([[c, -sine], [sine, c]])
    one_site = s.eye(2) - omega * omega.T
    rows = []
    for count in range(1, 5):
        dim = 2 ** count
        vacuum = tensor([omega] * count)
        unitary = tensor([rotation] * count)
        number = s.diag(*[j.bit_count() for j in range(dim)])
        actual = sum((tensor([one_site if j == site else s.eye(2)
                              for j in range(count)]) for site in range(count)), s.zeros(dim))
        assert unitary.T * unitary == s.eye(dim)
        assert unitary.T * actual * unitary == number
        assert actual * vacuum == s.zeros(dim, 1)
        raw = s.zeros(dim, 1)
        raw[0] = 1
        retained = raw * raw.T
        complement = s.eye(dim) - retained
        test = complement * vacuum
        norm = (test.T * test)[0]
        energy = (test.T * actual * test)[0]
        overlap_squared = c ** (2 * count)
        bound = count * sine ** 2 * overlap_squared / (1 - overlap_squared)
        assert norm == 1 - overlap_squared
        assert energy == count * sine ** 2 * overlap_squared
        assert s.cancel(energy / norm) == bound
        lift = -vacuum[1:, :] / c ** count
        fine = actual[1:, 1:]
        assert fine * lift == actual[1:, :1]
        assert 1 + (lift.T * lift)[0] == 1 / overlap_squared
        # The unrestricted gap-one lower form has an exact nonnegative
        # diagonal certificate after the independent product-unitary change.
        gap_one_form = actual - (s.eye(dim) - vacuum * vacuum.T)
        gap_one_diagonal = unitary.T * gap_one_form * unitary
        assert gap_one_diagonal == s.diag(*[0 if j == 0 else j.bit_count() - 1
                                           for j in range(dim)])
        assert all(gap_one_diagonal[j, j] >= 0 for j in range(dim))
        dressed_complement = s.eye(dim) - vacuum * vacuum.T
        dressed_gap_form = dressed_complement * actual * dressed_complement - dressed_complement
        assert dressed_gap_form == gap_one_form
        # Rank-one Cauchy certificate for the raw lower bound c^(2r).
        normalized_test = test / s.sqrt(norm)
        raw_rank_one = complement - test * test.T
        assert raw_rank_one * normalized_test == overlap_squared * normalized_test
        rows.append({"fast_qubits": count, "true_fast_gap": 1,
                     "raw_fast_lower_bound": str(overlap_squared),
                     "raw_fast_rayleigh_upper_bound": str(bound),
                     "raw_vacuum_mass_metric": str(1 / overlap_squared),
                     "dressed_fast_gap": 1})
    assert s.Rational(rows[-1]["raw_fast_rayleigh_upper_bound"]) < s.Rational(1, 20)
    return {"scope": __doc__, "c": str(c), "s": str(sine), "cases": rows,
            "raw_volume_uniform_gap_one_claim_refuted": True,
            "dressed_schur_lift_zero": True}


if __name__ == "__main__":
    if sys.flags.optimize:
        raise RuntimeError("Assertions must be enabled")
    target = Path(__file__).with_suffix(".json")
    if target.exists():
        raise FileExistsError("Existing evidence is preserved")
    result = controls()
    target.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8", newline="\n")
    print(json.dumps(result, indent=2))
