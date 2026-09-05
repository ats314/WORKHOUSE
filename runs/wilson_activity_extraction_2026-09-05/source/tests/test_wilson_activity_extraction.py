"""Exact extraction under noncommuting overlap and its factorization boundary."""

import json
import subprocess
import sys
from fractions import Fraction
from pathlib import Path

import pytest
import sympy as sp

from workhouse import wilson_activity_extraction as E


@pytest.fixture(scope="module")
def controls():
    return E.exact_controls()


def test_two_noncommuting_positive_models_reconstruct_all_induced_transfers(controls):
    models = controls["models"]
    assert sum(m["reconstruction_count"] for m in models) == 32
    assert all(m["closed_formula_equals_root_block_recursion"] for m in models)
    assert all(
        sp.Rational(p["det_B"]) > 0 and sp.Rational(p["smallest_D_entry"]) > 0
        for model in models
        for p in model["positivity_congruences"]
    )
    assert sp.Rational(models[0]["overlap_commutator_frobenius_squared"]) == sp.Rational(
        390963, 51200000000
    )
    assert models[0]["full_activity_nonzero"]


def test_all_activities_are_hermitian_and_annihilate_both_local_vacuum_legs(controls):
    count = 0
    for model in controls["models"]:
        for activity in model["activities"]:
            matrix = sp.Matrix([[sp.Rational(v) for v in row] for row in activity["matrix"]])
            assert matrix == matrix.T
            assert matrix[:, 0] == sp.zeros(matrix.rows, 1)
            assert matrix[0, :] == sp.zeros(1, matrix.cols)
            if len(activity["sites"]) == 1:
                assert matrix == sp.zeros(2)
            count += 1
    assert count == 30


def test_component_factorization_cancels_disconnected_activities(controls):
    assert [len(m["disconnected_cancellations"]) for m in controls["models"]] == [5, 9]
    assert not controls["models"][1]["full_activity_nonzero"]


def test_root_block_recursion_does_not_reuse_partition_enumeration(monkeypatch):
    family, _ = E.ordered_transfer_family((0, 1, 2), ((0, 1), (1, 2)))
    expected = E.mobius_cumulants(family)

    def forbidden(_):
        raise AssertionError("The independent recurrence must not enumerate partitions")

    monkeypatch.setattr(E, "partitions", forbidden)
    assert E.rooted_cumulants(family) == expected


def test_noncontiguous_tensor_embedding_preserves_operator_order():
    left = sp.Matrix(4, 4, range(1, 17))
    right = sp.Matrix([[2, 11], [13, 17]])
    arguments = (((0, 2), (1,)), (left, right), (0, 1, 2))
    direct = E.tensor_entries(*arguments)
    assert direct == E.tensor_permuted(*arguments)
    assert direct[1, 6] == 77
    assert direct != direct.T


def test_partition_enumeration_has_no_duplicate_or_missing_partitions():
    for size, bell in enumerate((1, 1, 2, 5, 15, 52)):
        result = list(E.partitions(tuple(range(size))))
        assert len(result) == len(set(result)) == bell


def test_vacuum_fixing_does_not_supply_the_missing_factorization_premise(controls):
    negative = controls["missing_factorization"]
    assert negative["positive_and_vacuum_fixing"]
    assert negative["component_factorization_fails"]
    assert sp.Rational(negative["disconnected_activity_11_entry"]) == sp.Rational(1, 12)


def test_zero_interaction_recovers_only_the_free_singleton_cumulants():
    family, _ = E.ordered_transfer_family((0, 1, 2), ((0, 1), (1, 2)), u=0, d=Fraction(1, 4))
    cumulants = E.mobius_cumulants(family)
    for sites, cumulant in cumulants.items():
        assert cumulant == (
            sp.diag(1, sp.Rational(1, 4)) if len(sites) == 1 else sp.zeros(2 ** len(sites))
        )


def test_inexact_parameters_and_invalid_positive_factor_domain_are_rejected():
    with pytest.raises(TypeError, match="exact rational"):
        E.ordered_transfer_family((0, 1), ((0, 1),), u=0.1)
    with pytest.raises(ValueError, match="positive contraction"):
        E.ordered_transfer_family((0, 1), ((0, 1),), u=1)
    with pytest.raises(ValueError, match="partition"):
        E.tensor_entries(((0,), (0,)), (sp.eye(2), sp.eye(2)), (0, 1))


def test_runner_retains_exact_scope_and_refuses_to_overwrite(tmp_path):
    root = Path(__file__).resolve().parents[1]
    output = tmp_path / "extraction.json"
    command = [
        sys.executable,
        str(root / "scripts/verify_wilson_activity_extraction.py"),
        "--output",
        str(output),
    ]
    process = subprocess.run(command, cwd=root, capture_output=True, text=True, check=False)
    assert process.returncode == 0, process.stderr
    original = output.read_bytes()
    report = json.loads(original)
    assert report["passed"] and report["exact_check_count"] == 2
    assert len(report["finite_controls"]["models"]) == 2
    assert "No analytic Wilson activity majorant" in report["verification_scope"]
    assert all(check["tier"] == 1 and check["passed"] for check in report["checks"])
    repeat = subprocess.run(command, cwd=root, capture_output=True, text=True, check=False)
    assert repeat.returncode != 0 and "fresh output" in repeat.stderr
    assert output.read_bytes() == original


def test_runner_cannot_certify_with_assertions_disabled(tmp_path):
    root = Path(__file__).resolve().parents[1]
    output = tmp_path / "optimized.json"
    command = [
        sys.executable,
        "-O",
        str(root / "scripts/verify_wilson_activity_extraction.py"),
        "--output",
        str(output),
    ]
    process = subprocess.run(command, cwd=root, capture_output=True, text=True, check=False)
    assert process.returncode != 0 and "assertions enabled" in process.stderr
    assert not output.exists()
