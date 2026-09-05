"""Finite parent-gap certificates, independently replayed over exact rationals."""

import json
import subprocess
import sys
from copy import deepcopy
from fractions import Fraction
from pathlib import Path

import pytest
import sympy as sp

from workhouse import wilson_creator_parent as P


@pytest.fixture(scope="module")
def records():
    return [P.verify_model(*case) for case in P.control_cases()]


@pytest.mark.parametrize("index", range(6))
def test_parent_gap_and_unique_vacuum_have_independent_exact_certificates(records, index):
    record = records[index]
    assert record["commuting_idempotents"] and record["exact_similarity"]
    assert record["hamiltonian_psd"]["rank"] == record["hamiltonian_psd"]["dimension"] - 1
    assert sp.Rational(record["g_lower"]) >= sp.Rational(record["conservative_g_lower"]) > 0
    assert P.replay_model(record)["success"]


def test_rooted_ball_implies_the_stated_fixed_gap_in_a_multibody_overlap(records):
    record = records[0]
    assert record["name"] == "rooted_radius_overlapping_multibody"
    assert record["within_rooted_one_eighth_ball"]
    assert sp.Rational(record["rooted_weight2_upper"]) == sp.Rational(5, 64)
    assert sp.Rational(record["M1_upper"]) == sp.Rational(19, 512)
    assert sp.Rational(record["g_lower"]) == sp.Rational(256663, 262144)
    assert sp.Rational(record["g_lower"]) >= sp.Rational(247, 256)
    assert any(len(c["support"]) == 3 for c in record["creators"])


def test_quadratic_term_is_essential_to_positivity_and_the_vacuum(records):
    for record in records:
        negative = record["negative_control"]
        assert sp.Rational(negative["psi_T_H_linear_psi"]) < 0
        assert negative["vacuum_annihilation_fails"]


def test_vector_valued_ternary_overlap_is_checked_without_scalar_collapse(records):
    record = next(r for r in records if r["name"] == "ternary_vector_creators")
    assert record["link_dimensions"] == (3, 3, 3)
    assert record["binary_oracle"] is None
    assert any(len(c["entries"]) > 1 for c in record["creators"])
    assert record["overlap_commutator_controls"]
    assert len(record["idempotent_singular_controls"]) == 3


def test_exact_gap_equality_is_allowed_without_artificial_strict_rank():
    record = P.verify_model("free", (2, 2), [])
    assert record["g_lower"] == "1"
    assert record["hamiltonian_psd"]["rank"] == 3
    assert record["H_squared_minus_gH_psd"]["rank"] == 1
    assert P.replay_model(record)["success"]


def test_bounded_rooted_data_does_not_bound_the_global_similarity():
    record = P.disjoint_condition_number_control()
    assert record["a"] == "1/32" and record["rooted_weight2_norm"] == "1/16"
    assert record["parent_gap_for_every_n"] == "1025/1024"
    assert record["similarity_condition_number_lower_bound"] == "(1025/1024)^n"
    assert record["bound_at_n_8192_exceeds_1000_exactly"]


@pytest.mark.parametrize("matrix", [sp.diag(1, -1), sp.Matrix([[0, 1], [1, 0]])])
def test_positive_diagonal_is_not_mistaken_for_psd(matrix):
    with pytest.raises(AssertionError):
        P.exact_psd_certificate(matrix)


def test_altered_certificate_factorization_is_rejected(records):
    broken = deepcopy(records[0])
    diagonal = broken["hamiltonian_psd"]["diagonal"]
    diagonal[0] = str(sp.Rational(diagonal[0]) + 1)
    with pytest.raises(AssertionError):
        P.replay_model(broken)


def test_replay_recomputes_gap_instead_of_trusting_its_label(records):
    broken = deepcopy(records[0])
    broken["g_lower"] = "100"
    with pytest.raises(AssertionError):
        P.replay_model(broken)


def test_float_coefficients_are_not_silently_recast_as_exact_input():
    with pytest.raises(TypeError, match="exact"):
        P.verify_model("float", (2,), [((0,), {(1,): 0.1})])


def test_a_creator_cannot_carry_a_vacuum_component():
    with pytest.raises(AssertionError):
        P.verify_model("vacuum", (2,), [((0,), {(0,): Fraction(1, 100)})])


def test_runner_refuses_to_overwrite_existing_evidence(tmp_path):
    root = Path(__file__).resolve().parents[1]
    target = tmp_path / "evidence.json"
    original = b"existing evidence must remain byte-identical\n"
    target.write_bytes(original)
    process = subprocess.run(
        [
            sys.executable,
            str(root / "scripts/verify_wilson_creator_parent.py"),
            "--output",
            str(target),
        ],
        cwd=root,
        capture_output=True,
        text=True,
        check=False,
    )
    assert process.returncode != 0 and "fresh output" in process.stderr
    assert target.read_bytes() == original


def test_runner_refuses_disabled_assertions(tmp_path):
    root = Path(__file__).resolve().parents[1]
    target = tmp_path / "optimized.json"
    process = subprocess.run(
        [
            sys.executable,
            "-O",
            str(root / "scripts/verify_wilson_creator_parent.py"),
            "--output",
            str(target),
        ],
        cwd=root,
        capture_output=True,
        text=True,
        check=False,
    )
    assert process.returncode != 0 and "assertions enabled" in process.stderr
    assert not target.exists()


def test_runner_records_scoped_native_checks_and_independent_certificates(tmp_path):
    root = Path(__file__).resolve().parents[1]
    target = tmp_path / "parent.json"
    process = subprocess.run(
        [
            sys.executable,
            str(root / "scripts/verify_wilson_creator_parent.py"),
            "--output",
            str(target),
        ],
        cwd=root,
        capture_output=True,
        text=True,
        check=False,
    )
    assert process.returncode == 0, process.stderr
    report = json.loads(target.read_text(encoding="utf-8"))
    assert report["passed"] and report["exact_check_count"] == 5
    assert report["psd_certificate_count"] == 81
    assert len(report["models"]) == len(report["independent_replays"]) == 6
    assert all(check["passed"] and check["tier"] == 1 for check in report["checks"])
    assert report["runtime"]["assertions_enabled"]
    assert "does not machine-certify" in report["verification_scope"]
    assert "src/workhouse/wilson_creator_parent.py" in report["sources"]
