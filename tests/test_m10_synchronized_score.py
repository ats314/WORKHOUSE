"""Test suite for W6/G19 M10 conditional score domination under synchronized transport.

Guards:
1. Tangency cancellation of the linear phase drift along the conditional minimizer.
2. Non-zero drift of the failed unsynchronized counterexample field.
3. Euler dilation cancellation at q = 0.
4. Reduction of tube variance to quadratic potential floor.
5. Exact antipodal Hessian spectrum and normal spectral gap.
6. Monotone global potential quadratic floor.
7. Gauge invariance of the ground state score on the antipodal minimizing sphere.
8. Semiclassical amplitude gradient scaling |nabla_eta a_g| <= c_a / g.
9. Cancellation of Psi_g denominator in the score variance integrand.
10. Global full-fiber domination bound.
"""

from __future__ import annotations

import importlib.util
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]


@pytest.fixture(scope="module")
def tube_script():
    script_path = ROOT / "scripts" / "verify_m10_tube_variance.py"
    spec = importlib.util.spec_from_file_location("verify_m10_tube_variance", script_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


@pytest.fixture(scope="module")
def antipodal_script():
    script_path = ROOT / "scripts" / "check_antipodal_score_bound.py"
    spec = importlib.util.spec_from_file_location("check_antipodal_score_bound", script_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


@pytest.fixture(scope="module")
def amp_script():
    script_path = ROOT / "scripts" / "verify_m10_amplitude_and_complement.py"
    spec = importlib.util.spec_from_file_location("verify_m10_amplitude_and_complement", script_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def test_synchronized_tangency_cancels_drift(tube_script):
    res = tube_script.check_tangency_cancellation()
    assert res["is_tangent"] is True
    assert res["drift_difference"] == ["0", "0", "0"]


def test_failed_unsynchronized_field_has_nonzero_drift(tube_script):
    res = tube_script.check_tangency_cancellation()
    assert res["failed_is_nonzero"] is True
    assert any("chi" in term for term in res["failed_drift"])


def test_euler_cancellation_at_zero(tube_script):
    res = tube_script.check_euler_cancellation()
    assert res["F_identically_zero"] is True
    assert res["hessian_identically_zero"] is True


def test_tube_variance_quadratic_bound(tube_script):
    res = tube_script.check_tube_variance_bound()
    assert res["ratio_floor_holds"] is True
    assert res["small_angle_ratio"] == 0.5
    assert res["antipodal_ratio"] > res["lower_bound_constant"]
    assert res["lower_bound_constant"] > 0.20


def test_antipodal_spectrum_and_gap(antipodal_script):
    res = antipodal_script.check_antipodal_spectrum()
    assert res["has_two_zeros"] is True
    assert res["has_seven_normal"] is True
    assert res["bound_holds"] is True
    assert res["min_normal_eigenvalue"] > 1.656


def test_potential_floor_and_domination(antipodal_script):
    res = antipodal_script.check_potential_floor()
    assert res["v_pi_exact"] is True
    assert res["v_pi_float"] > 4.68
    assert res["floor_holds"] is True
    assert res["monotone_decreasing"] is True


def test_antipodal_gauge_score_invariance(antipodal_script):
    res = antipodal_script.check_gauge_score_invariance()
    assert res["orbit_is_homogeneous"] is True
    assert res["differential_vanishes"] is True
    assert res["angular_first_order_variance"] == 0.0


def test_amplitude_gradient_scaling(amp_script):
    assert amp_script.verify_amplitude_scaling() is True


def test_score_integrand_denominator_cancellation(amp_script):
    assert amp_script.verify_integrand_denominator_cancellation() is True


def test_agmon_gap_and_global_domination(amp_script):
    assert amp_script.verify_agmon_gap() is True
    assert amp_script.verify_global_domination_bound() is True
