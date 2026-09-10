"""Independent source-current reconstruction and its necessary qualifications."""

import importlib.util
from pathlib import Path

import pytest
import sympy as sp

ROOT = Path(__file__).resolve().parents[1]


@pytest.fixture(scope="module")
def bridge():
    spec = importlib.util.spec_from_file_location(
        "source_current_bridge_checks", ROOT / "scripts/verify_source_current_bridges.py"
    )
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def test_actual_cometric_and_complete_operator_action(bridge):
    result = bridge.cometric_and_operator_control()
    assert result["passed"]
    assert result["mode_cometric"] == [4, 2, 8, 3]
    assert result["operator_defects"] == ["0", "0"]
    assert result["second_radial_symbol"] == "0"


def test_exact_current_moments_require_the_fast_v_current(bridge):
    assert bridge.current_moment_control()["passed"]
    omitted = bridge.current_moment_control(include_v=False)
    assert not omitted["passed"]
    assert omitted["defects"][0] != "0"


def test_joint_radial_budget_is_certified_in_rationals(bridge):
    result = bridge.radial_budget_control()
    assert result["passed"]
    for low, high in result["positive_rational_enclosures"].values():
        assert sp.Rational(low) > 0
        assert sp.Rational(high) >= sp.Rational(low)


def test_projection_and_coefficient_motion_are_retained(bridge):
    result = bridge.residual_and_centering_control()
    assert result["passed"]
    assert result["omitted_product_term"] != "0"


def test_variational_ingredient_allows_a_kernel_without_asserting_an_inverse(bridge):
    result = bridge.variational_completion_control()
    assert result["passed"]
    assert result["degenerate_form_determinant"] == "0"


def test_a_small_exponential_family_can_miss_a_low_state(bridge):
    result = bridge.source_totality_negative_control()
    assert result["passed"]
    assert sp.Rational(result["unobserved_energy"]) < sp.Rational(result["observed_energy"])
    assert result["source_span_dimension"] < result["vacuum_complement_dimension"]


def test_normalized_source_requires_second_cumulant_difference(bridge):
    assert bridge.normalized_source_control()["passed"]
