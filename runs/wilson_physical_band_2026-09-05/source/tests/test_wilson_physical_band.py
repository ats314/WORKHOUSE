"""Focused tests of finite controls and their certification boundaries."""

import json
import subprocess
import sys
from pathlib import Path

import pytest
import sympy as sp

from workhouse import wilson_physical_band as controls


@pytest.fixture(scope="module")
def result():
    return controls.exact_controls()


def test_rotated_source_map_has_a_two_sided_inverse_and_exact_gram_certificates(result):
    band = result["rotated_band"]
    assert band["direct_rotation_and_two_sided_inverse_verified"]
    assert sp.Rational(band["coefficient_map_determinant"]) != 0
    assert all(
        sp.Rational(v) >= 0
        for key, values in band.items()
        if key.endswith("principal_minors")
        for v in values
    )


def test_psd_certificate_rejects_negative_and_nonsymmetric_matrices():
    with pytest.raises(AssertionError):
        controls.psd(sp.diag(1, -1))
    with pytest.raises(AssertionError):
        controls.psd(sp.Matrix([[1, 2], [0, 1]]))


def test_tagged_gram_has_real_overlap_and_zero_disjoint_cross_terms(result):
    source = result["source_gram"]
    gram = sp.Matrix([[sp.Rational(v) for v in row] for row in source["gram"]])
    assert gram[0, 1] == sp.Rational(19, 312500)
    assert gram[0, 2] == gram[1, 2] == 0
    assert sp.Rational(source["tagged_weight_two_norm"]) == sp.Rational(56, 125)
    assert sp.Rational(source["synthesis_norm_upper"]) == sp.Rational(7, 125)


def test_dropping_termwise_centering_breaks_the_gram_bound(result):
    negative = result["source_gram"]["uncentered_negative_control"]
    assert sp.Rational(negative["actual_gram_norm"]) == 2 * sp.Rational(
        negative["invalid_centered_bound"]
    )


def test_activity_exhaustion_has_nonzero_tails_and_a_surviving_disjoint_product(result):
    exhaustion = result["activity_exhaustion"]
    assert exhaustion["nonzero_activities"] == 6
    assert sp.Rational(exhaustion["overlap_commutator_frobenius_squared"]) > 0
    assert exhaustion["disjoint_families"] == 8
    assert exhaustion["activity_families_killed_by_local_vacuum"] == 1
    assert exhaustion["nonzero_two_activity_product"]
    tails = exhaustion["exhaustions"]
    assert [entry["tail_is_nonzero"] for entry in tails] == [True, True, False]
    assert sp.Rational(tails[-1]["local_operator_tail_bound"]) == 0
    assert all(
        sp.Rational(value) >= 0 for entry in tails for value in entry["tail_principal_minors"]
    )


def test_direct_family_enumeration_does_not_allow_overlapping_activities():
    supports = ((0, 1), (1, 2), (2, 3))
    families = set(controls._disjoint_families(supports))
    assert families == {(), ((0, 1),), ((1, 2),), ((2, 3),), ((0, 1), (2, 3))}


def test_frame_margins_and_completeness_counterexamples(result):
    margins = result["scalar_margins"]
    assert sp.Rational(margins["gram_lower"]) > sp.Rational(9, 16)
    assert sp.Rational(margins["inverse_bound"]) < sp.Rational(6, 5)
    assert result["negative_controls"]["source_kernel_vector"] == "(1,...,1)"
    assert result["negative_controls"]["synthesis_error_norm"] == "1"


def test_native_suite_registers_exactly_five_finitely_scoped_checks():
    from workhouse.invariants._core import SUITES
    from workhouse.invariants.wilson_physical_band import physical_band_suite

    assert physical_band_suite in SUITES
    checks = physical_band_suite.run()
    assert len(checks) == 5 and all(check.passed and check.tier == 1 for check in checks)


def test_runner_preserves_scope_and_refuses_overwrite(tmp_path):
    runner = Path(__file__).resolve().parents[1] / "scripts/verify_wilson_physical_band.py"
    output = tmp_path / "controls.json"
    command = [sys.executable, str(runner), "--output", str(output)]
    process = subprocess.run(command, capture_output=True, text=True, check=False)
    assert process.returncode == 0, process.stderr
    original = output.read_bytes()
    report = json.loads(original)
    assert report["passed"] and report["exact_check_count"] == 5
    assert "no infinite-volume Wilson theorem" in report["verification_scope"]
    repeat = subprocess.run(command, capture_output=True, text=True, check=False)
    assert repeat.returncode != 0 and "fresh output" in repeat.stderr
    assert output.read_bytes() == original


def test_runner_rejects_optimized_python(tmp_path):
    runner = Path(__file__).resolve().parents[1] / "scripts/verify_wilson_physical_band.py"
    output = tmp_path / "invalid.json"
    process = subprocess.run(
        [sys.executable, "-O", str(runner), "--output", str(output)],
        capture_output=True,
        text=True,
        check=False,
    )
    assert process.returncode != 0 and "assertions enabled" in process.stderr
    assert not output.exists()
