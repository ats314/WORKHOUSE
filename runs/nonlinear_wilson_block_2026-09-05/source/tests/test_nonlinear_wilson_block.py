"""Failure-boundary tests for exact nonlinear block acceptance."""

import subprocess
import sys
from pathlib import Path

import pytest
import sympy as sp

from workhouse.invariants.nonlinear_wilson_block import nonlinear_wilson_suite
from workhouse.nonlinear_wilson_block import (
    compression_leakage_certificate,
    exact_nonlinear_controls,
    replay_compression_certificate,
    replay_spectral_budget,
    replay_trace_certificate,
    trace_psd_certificate,
    vertical_spectral_budget,
)

ROOT = Path(__file__).resolve().parents[1]


def test_five_native_checks_preserve_their_finite_scopes():
    results = nonlinear_wilson_suite.run()
    assert len(results) == 5
    assert all(result.passed and result.tier == 1 for result in results)


def trace_inputs():
    return sp.Matrix([[1, 1], [1, 1]]) / 10, sp.diag(2, 1)


def test_trace_certificate_accepts_noncommuting_and_rank_deficient_inputs():
    bmat, qmat = trace_inputs()
    certificate = trace_psd_certificate(bmat, qmat)
    assert certificate["commuting"] is False
    assert certificate["margin"] == "3/10"
    assert replay_trace_certificate(bmat, qmat, certificate) == certificate


@pytest.mark.parametrize(
    "failure", ["Q_indefinite", "B_indefinite", "nonhermitian", "float", "shape"]
)
def test_trace_certificate_rejects_missing_hypotheses(failure):
    bmat, qmat = trace_inputs()
    if failure == "Q_indefinite":
        qmat = sp.Matrix([[1, 2], [2, 1]])
    elif failure == "B_indefinite":
        bmat = -bmat
    elif failure == "nonhermitian":
        qmat[0, 1] = 1
    elif failure == "float":
        bmat[0, 0] = 0.1
    else:
        qmat = sp.eye(3)
    with pytest.raises(ValueError):
        trace_psd_certificate(bmat, qmat)


@pytest.mark.parametrize("key,value", [("margin", "0"), ("commuting", True), ("loss_minors", [])])
def test_trace_replay_rejects_corrupted_margins_and_hypotheses(key, value):
    bmat, qmat = trace_inputs()
    certificate = trace_psd_certificate(bmat, qmat)
    certificate[key] = value
    with pytest.raises(ValueError, match="recomputation"):
        replay_trace_certificate(bmat, qmat, certificate)


@pytest.mark.parametrize("rank", [2, 4, 5, 20])
def test_scalar_budget_covers_both_cutoff_branches_without_claiming_rank_proof(rank):
    epsilon = min(sp.Integer(1), sp.Rational(4, rank))
    eta = epsilon / 8
    v = 7 * eta / 2
    near = vertical_spectral_budget(rank, 10, 3, v, eta)
    far = vertical_spectral_budget(rank, 10, 3, 2 * epsilon)
    assert near["branch"] == "near" and far["branch"] == "far"
    assert sp.Rational(near["cap_margin"]) >= 0
    assert sp.Rational(far["affine_margin"]) >= 0
    assert replay_spectral_budget(rank, 10, 3, v, eta, near) == near


def test_high_supplied_center_energy_does_not_silently_assert_a_fast_threshold():
    result = vertical_spectral_budget(2, 1, 100, sp.Rational(7, 20), sp.Rational(1, 10))
    assert result["nonnegative_Wilson_coefficient"] is False
    assert result["spectral_cap"] == "1"
    assert sp.Rational(result["cap_margin"]) > 0


@pytest.mark.parametrize(
    "arguments",
    [
        (True, 1, 0, 0, 0),
        (1, 1, 0, 0, 0),
        (2.0, 1, 0, 0, 0),
        (2, 0, 0, 0, 0),
        (2, 1.0, 0, 0, 0),
        (2, 1, -1, 0, 0),
        (2, 1, 1, -1, 0),
        (2, 1, 1, 0, None),
        (2, 1, 1, sp.Rational(1, 2), sp.Rational(1, 3)),
        (2, 1, 1, 2, sp.Rational(1, 10)),
    ],
)
def test_scalar_acceptance_rejects_invalid_domains(arguments):
    with pytest.raises(ValueError):
        vertical_spectral_budget(*arguments)


def test_scalar_replay_rejects_a_falsified_gap_margin():
    arguments = (2, 10, 3, sp.Rational(7, 20), sp.Rational(1, 10))
    certificate = vertical_spectral_budget(*arguments)
    certificate["cap_margin"] = "1000000"
    with pytest.raises(ValueError, match="recomputation"):
        replay_spectral_budget(*arguments, certificate)


def test_mutable_payloads_cannot_change_cached_acceptance():
    controls = exact_nonlinear_controls()
    controls["su2"]["minus_I_conditional_gaps"]["strip"] = "0"
    controls["ground_bundle"]["ad_X_linear_coefficients"][1] = "0"
    fresh = exact_nonlinear_controls()
    assert fresh["su2"]["minus_I_conditional_gaps"]["strip"] == "15/16"
    assert fresh["ground_bundle"]["ad_X_linear_coefficients"][1] == "7/24"


def compression_inputs():
    c, s = sp.Rational(3, 5), sp.Rational(4, 5)
    columns = sp.Matrix([[c, 0], [0, c], [s, 0], [0, s]])
    return sp.diag(11, 15, 18, 23), columns * columns.T, sp.diag(1, 1, 0, 0)


def test_complete_low_leakage_keeps_a_retained_projection_that_misses_the_vacuum():
    hamiltonian, retained, low = compression_inputs()
    certificate = compression_leakage_certificate(
        hamiltonian, retained, low, 11, 7, sp.Rational(16, 25)
    )
    assert certificate["compressed_floor"] == "63/25"
    assert certificate["low_leakage_nonzero"]
    assert (
        replay_compression_certificate(
            hamiltonian, retained, low, 11, 7, sp.Rational(16, 25), certificate
        )
        == certificate
    )


@pytest.mark.parametrize("failure", ["ground_only", "leakage", "vacuum", "nonprojector"])
def test_compression_rejects_incomplete_low_subspace_or_false_budget(failure):
    hamiltonian, retained, low = compression_inputs()
    energy, leak = 11, sp.Rational(16, 25)
    if failure == "ground_only":
        low = sp.diag(1, 0, 0, 0)
    elif failure == "leakage":
        leak = sp.Rational(1, 10)
    elif failure == "vacuum":
        energy = 10
    else:
        retained /= 2
    with pytest.raises(ValueError):
        compression_leakage_certificate(hamiltonian, retained, low, energy, 7, leak)


def test_compression_replay_rejects_an_invented_floor():
    arguments = (*compression_inputs(), 11, 7, sp.Rational(16, 25))
    certificate = compression_leakage_certificate(*arguments)
    certificate["compressed_floor"] = "7"
    with pytest.raises(ValueError, match="recomputation"):
        replay_compression_certificate(*arguments, certificate)


def test_runner_preserves_existing_output_and_rejects_optimized_python(tmp_path):
    script = ROOT / "scripts/verify_nonlinear_wilson_block.py"
    existing = tmp_path / "existing.json"
    existing.write_bytes(b"original evidence\n")
    refused = subprocess.run(
        [sys.executable, str(script), "--output", str(existing)],
        capture_output=True,
        text=True,
        check=False,
    )
    assert refused.returncode != 0 and "fresh output" in refused.stderr
    assert existing.read_bytes() == b"original evidence\n"
    fresh = tmp_path / "optimized.json"
    optimized = subprocess.run(
        [sys.executable, "-O", str(script), "--output", str(fresh)],
        capture_output=True,
        text=True,
        check=False,
    )
    assert optimized.returncode != 0 and "assertions enabled" in optimized.stderr
    assert not fresh.exists()
