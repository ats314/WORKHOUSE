"""Regression tests for the repaired M10 claims and actual mathematical witnesses."""

from __future__ import annotations

import json
import math
import subprocess
import sys
from pathlib import Path

import pytest
import sympy as sp

from workhouse.invariants import w6_synchronized_m10 as m10

ROOT = Path(__file__).resolve().parents[1]


def test_general_quadratic_jet_not_a_selected_matrix():
    assert m10.check_euler_cancellation()[0]


def test_synchronized_and_unsynchronized_profiles_are_distinguished():
    assert m10.check_synchronized_tangency()[0]
    assert m10.check_unsynchronized_failure()[0]


def test_actual_centered_integrand_includes_beta_and_normalization():
    assert m10.check_score_variance_denominator()[0]
    # A nonzero reference makes the omitted mean difference observable.
    psi, numerator, beta, hq = sp.Rational(1, 10), sp.Integer(2), sp.Integer(3), sp.Rational(1, 100)
    centered = (numerator / psi - beta) ** 2 * psi**2 / hq
    assert centered == 289
    assert centered != numerator**2 / hq


def test_spatial_remainder_witness_breaks_inverse_g_bound():
    g, gradient = m10.remainder_witness()
    for n in [1, 3, 20]:
        gn = (2 * sp.pi * n) ** (-sp.Rational(1, 6))
        assert sp.simplify((g * gradient).subs(g, gn) + 6 / gn**2) == 0
    assert m10.check_log_parameter_amplitude()[0]


def test_magnetic_hessian_cannot_be_used_as_action_hessian():
    assert m10.check_hessian_distinction()[0]


@pytest.mark.parametrize(
    "length", [sp.Rational(1, 100), sp.Rational(1, 2), sp.Integer(2), sp.Integer(20)]
)
def test_angular_moments_against_independent_quadrature(length):
    symbol, moments = m10.angular_moments()
    # Independent midpoint quadrature, used only as finite corroboration.
    size = 20000
    upper = float(length)
    dx = upper / size
    masses = [math.exp(-(i + 0.5) * dx) for i in range(size)]
    for order in [1, 2]:
        actual = sum(((i + 0.5) * dx) ** order * w for i, w in enumerate(masses)) / sum(masses)
        expected = float(moments[order].subs(symbol, length))
        assert actual == pytest.approx(expected, abs=2e-7)
        assert expected <= (1 if order == 1 else 2)


def test_angular_zero_and_large_parameter_limits():
    assert m10.check_angular_limits()[0]
    assert m10.check_normal_angular_budget()[0]


@pytest.mark.parametrize(
    "script",
    [
        "verify_m10_amplitude_and_complement.py",
        "verify_m10_tube_variance.py",
        "check_antipodal_score_bound.py",
    ],
)
def test_script_reports_only_scoped_controls(script, tmp_path):
    output = tmp_path / "result.json"
    run = subprocess.run(
        [sys.executable, str(ROOT / "scripts" / script), "--out", str(output)],
        cwd=ROOT,
        text=True,
        capture_output=True,
        check=False,
    )
    assert run.returncode == 0, run.stderr
    report = json.loads(output.read_text(encoding="utf-8"))
    assert report["checks"] and all(row["passed"] for row in report["checks"])
    assert report["actual_m10_status"] == "open"
    assert "Global domination bound holds" not in run.stdout


@pytest.mark.parametrize(
    "check",
    [
        m10.check_actual_jet_forcing,
        m10.check_weighted_jet_absorption,
        m10.check_control_action_and_slack,
    ],
)
def test_actual_complement_normalizations(check):
    assert check()[0]
