"""Tests for the meaningful failure boundaries of physical-block controls."""

import copy
import subprocess
import sys
from fractions import Fraction
from pathlib import Path

import pytest
import sympy as s

from workhouse.continuum_wilson_block import exact_block_controls, expectation, su_basis
from workhouse.continuum_wilson_rotor import (
    replay_rotor_certificate,
    rotor_certificates,
    sturm_count,
)
from workhouse.invariants.continuum_wilson_block import continuum_block_suite

ROOT = Path(__file__).resolve().parents[1]


def test_native_suite_checks_all_six_scoped_controls():
    results = continuum_block_suite.run()
    assert len(results) == 6
    assert all(result.passed for result in results)


@pytest.mark.parametrize("failure", ["sturm", "tail", "normalization", "duplicate_index"])
def test_rotor_replay_rejects_corrupted_enclosure(failure):
    entry = rotor_certificates()[1]
    if failure == "sturm":
        # Still an ordered positive interval below the barrier; its count is false.
        entry["eigenvalues"][0]["ritz_interval"] = ["1", "2"]
    elif failure == "tail":
        entry["boundary_subtraction"] = "0"
    elif failure == "normalization":
        entry["gap_over_sqrt_u_interval"] = entry["gap_interval"]
    else:
        entry["eigenvalues"][1]["index"] = 0
    with pytest.raises(ValueError):
        replay_rotor_certificate(entry)


def test_rotor_replay_rejects_a_barrier_at_the_tail_floor():
    entry = rotor_certificates()[0]
    entry["barrier"] = entry["tail_kinetic_floor"]
    with pytest.raises(ValueError, match="barrier"):
        replay_rotor_certificate(entry)


def test_certificate_payloads_do_not_share_mutable_state():
    saved = rotor_certificates()
    changed = copy.deepcopy(saved)
    changed[0]["eigenvalues"][0]["lower"] = "0"
    assert rotor_certificates() == saved
    assert rotor_certificates() != changed


def test_sturm_internal_zero_principal_minor_uses_the_correct_sign_count():
    # Matrix [[2,-1],[-1,11/4]] has one eigenvalue below 2; the first minor is zero.
    assert sturm_count(Fraction(1, 4), 2, 2) == 1
    assert sturm_count(Fraction(1, 4), 2, 0) == 0
    assert sturm_count(Fraction(1, 4), 2, 4) == 2


@pytest.mark.parametrize("coupling,cutoff", [(0, 2), (-1, 2), (1, 1), (1, 2.0)])
def test_sturm_rejects_an_invalid_jacobi_domain(coupling, cutoff):
    with pytest.raises(ValueError):
        sturm_count(coupling, cutoff, 0)


def test_gaussian_moments_keep_mixed_and_odd_terms_distinct():
    x, y = s.symbols("x y")
    assert expectation(x**4 * y**2 + x * y**3, [x, y], [s.Rational(2), s.Rational(3)]) == 36
    with pytest.raises(ValueError):
        expectation(x**2, [x], [s.Rational(1), s.Rational(2)])


def test_invalid_rank_is_rejected():
    with pytest.raises(ValueError, match="rank"):
        su_basis(1)


def test_independent_original_link_and_effective_matrix_paths_agree():
    result = exact_block_controls()
    original = result["original_seven_link_SU2"]
    matrix = result["first_shell_SU2_matrix"]
    assert s.Rational(original["mixed_minus_radial"]) == s.Rational(matrix["mixed_minus_local"])
    assert s.Rational(matrix["omitted_metric_negative_control_split"]) < 0
    assert result["two_strip_selfenergy"]["mixed_shell_denominator_negative_control"]


def test_runner_preserves_existing_evidence(tmp_path):
    output = tmp_path / "retained.json"
    output.write_text("retained evidence", encoding="utf-8")
    run = subprocess.run(
        [
            sys.executable,
            str(ROOT / "scripts/verify_continuum_wilson_block.py"),
            "--output",
            str(output),
        ],
        cwd=ROOT,
        capture_output=True,
        text=True,
        check=False,
    )
    assert run.returncode != 0
    assert "fresh output" in run.stderr
    assert output.read_text(encoding="utf-8") == "retained evidence"


def test_runner_refuses_disabled_assertions(tmp_path):
    output = tmp_path / "never-written.json"
    run = subprocess.run(
        [
            sys.executable,
            "-O",
            str(ROOT / "scripts/verify_continuum_wilson_block.py"),
            "--output",
            str(output),
        ],
        cwd=ROOT,
        capture_output=True,
        text=True,
        check=False,
    )
    assert run.returncode != 0
    assert "assertions enabled" in run.stderr
    assert not output.exists()
