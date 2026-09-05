"""Failure-boundary tests for the exact scale-comparison acceptance APIs."""

import subprocess
import sys
from pathlib import Path

import pytest
import sympy as s

from workhouse.continuum_scale_comparison import (
    exact_scale_controls,
    gaussian_certificates,
    gaussian_schur_blocks,
    graph_source_control,
    inverse_fast_budget,
    partition_matrices,
    rational_interval_replay,
    rectangle_complex,
    replay_gaussian_enclosures,
    require_psd,
)
from workhouse.continuum_scale_periodic import (
    complex_matrices,
    exact_periodic_controls,
    periodic_green,
)
from workhouse.invariants.continuum_scale_comparison import continuum_scale_suite

ROOT = Path(__file__).resolve().parents[1]
F = s.Matrix([[7, 2], [2, 5]])
D = s.Matrix([[2, -1], [1, 3]])
K0 = s.Matrix([[2, 1], [1, 4]])


def test_native_suite_runs_seven_precisely_scoped_checks():
    result = continuum_scale_suite.run()
    assert len(result) == 7
    assert all(row.passed and row.tier == 1 for row in result)


@pytest.mark.parametrize("failure", ["interval", "index", "margin", "missing"])
def test_schur_certificate_rejects_corruption(failure):
    certificates = gaussian_certificates()
    if failure == "interval":
        certificates[0]["lambda_interval"] = ["1/10", "1/5"]
    elif failure == "index":
        certificates[1]["j"] = 1
    elif failure == "margin":
        certificates[0]["strict_lower_control"] = "0"
    else:
        certificates.pop()
    with pytest.raises(ValueError):
        replay_gaussian_enclosures(F, D, K0, 3, certificates)


def test_root_replay_distinguishes_branch_multiplicity_and_endpoint_roots():
    x = s.Symbol("x")
    polynomial = (x**2 - 2) * (x**2 - 3)
    assert rational_interval_replay(polynomial, ["7/5", "3/2"], 2) == (
        s.Rational(7, 5),
        s.Rational(3, 2),
    )
    with pytest.raises(ValueError, match="root index"):
        rational_interval_replay(polynomial, ["7/5", "3/2"], 0)
    with pytest.raises(ValueError, match="simple"):
        rational_interval_replay((x**2 - 2) ** 2, ["7/5", "3/2"], 1)
    with pytest.raises(ValueError, match="endpoint"):
        rational_interval_replay(x - 1, ["1", "2"], 0)


@pytest.mark.parametrize("failure", ["floor", "float", "nonsymmetric", "static", "shape"])
def test_schur_construction_rejects_invalid_hypotheses(failure):
    fast, coupling, static, floor = F.copy(), D.copy(), K0.copy(), 3
    if failure == "floor":
        floor = 6
    elif failure == "float":
        fast[0, 0] = 7.0
    elif failure == "nonsymmetric":
        fast[0, 1] = 1
    elif failure == "static":
        static = s.zeros(2)
    else:
        coupling = s.zeros(2, 3)
    with pytest.raises(ValueError):
        gaussian_schur_blocks(fast, coupling, static, floor)


def test_psd_acceptance_keeps_off_diagonal_principal_minors():
    # Positive diagonal alone would wrongly accept this indefinite matrix.
    with pytest.raises(ValueError, match="positive semidefinite"):
        require_psd(s.Matrix([[1, 2], [2, 1]]))
    require_psd(s.Matrix([[1, 1], [1, 1]]))


@pytest.mark.parametrize("nx,ny,side", [(0, 2, 1), (2, 2, 0), (2, 2, 3), (2.0, 2, 1), (True, 2, 1)])
def test_invalid_original_link_or_box_geometry_is_rejected(nx, ny, side):
    with pytest.raises(ValueError):
        partition_matrices(nx, ny, side)


def test_original_link_curl_keeps_shared_edge_orientation():
    _, _, _, gradient, curl = rectangle_complex(2, 1)
    assert curl * gradient == s.zeros(2, 6)
    assert curl * curl.T == s.Matrix([[4, -1], [-1, 4]])
    # Making only one shared-edge orientation agree violates the chain law.
    altered = curl.copy()
    shared = next(j for j in range(curl.cols) if curl[0, j] and curl[1, j])
    altered[1, shared] *= -1
    assert altered * gradient != s.zeros(2, 6)


def simple_low_window():
    hamiltonian = s.Matrix(
        [
            [s.Rational(1, 2), 0, s.Rational(1, 2)],
            [0, s.Rational(1, 4), 0],
            [s.Rational(1, 2), 0, s.Rational(1, 2)],
        ]
    )
    window = s.Matrix(
        [
            [s.Rational(1, 2), 0, -s.Rational(1, 2)],
            [0, 1, 0],
            [-s.Rational(1, 2), 0, s.Rational(1, 2)],
        ]
    )
    return hamiltonian, window


def test_graph_sources_cover_a_whole_low_window_with_a_dressed_vacuum():
    hamiltonian, window = simple_low_window()
    result = graph_source_control(hamiltonian, 2, window, s.Rational(1, 4), s.Rational(1, 2))
    assert result["rank"] == 2
    assert result["frame_lower"] == "3/4"


@pytest.mark.parametrize("failure", ["nonprojector", "nonreducing", "highenergy", "floor"])
def test_graph_source_acceptance_rejects_invalid_window_or_fast_floor(failure):
    hamiltonian, window = simple_low_window()
    floor = s.Rational(1, 2)
    if failure == "nonprojector":
        window *= 2
    elif failure == "nonreducing":
        window = s.diag(1, 0, 0)
    elif failure == "highenergy":
        window = s.eye(3) - window
    else:
        floor = s.Rational(1, 4)
    with pytest.raises(ValueError):
        graph_source_control(hamiltonian, 2, window, s.Rational(1, 4), floor)


def test_inverse_budget_is_in_energy_units_and_requires_positive_bounds():
    gaps = inverse_fast_budget(s.Rational(1, 7), [3 * 2**j for j in range(8)])
    expected = 7 + s.Rational(2, 3) * (1 - s.Rational(1, 2) ** 8)
    assert gaps[-1] == 1 / expected
    assert all(a > b > 0 for a, b in zip(gaps, gaps[1:], strict=False))
    with pytest.raises(ValueError, match="Positive rational"):
        inverse_fast_budget(1, [2, 0])
    with pytest.raises(ValueError, match="Positive rational"):
        inverse_fast_budget(1.0, [2])


def test_returned_controls_and_certificates_do_not_mutate_cached_acceptance():
    controls = exact_scale_controls()
    controls["gaussian_memory"]["certificates"][0]["j"] = -1
    certificates = gaussian_certificates()
    certificates[0]["j"] = -1
    assert exact_scale_controls()["gaussian_memory"]["certificates"][0]["j"] == 1
    assert gaussian_certificates()[0]["j"] == 1


@pytest.mark.parametrize("period", [1, 2, 3.0, True])
def test_periodic_geometry_rejects_short_or_noninteger_conventions(period):
    with pytest.raises(ValueError):
        complex_matrices(period)


def test_periodic_green_requires_a_complete_site_set():
    sites, _, _, _, _, laplace = complex_matrices(3)
    with pytest.raises(ValueError, match="complete periodic cube"):
        periodic_green(3, sites[:-1])
    green = periodic_green(3, sites)
    assert laplace * green == s.eye(27) - s.ones(27) / 27


def test_periodic_harmonic_directions_and_nonlocal_witness_survive_replay():
    result = exact_periodic_controls()
    assert [row["harmonic_cochain_directions_retained"] for row in result["periodic_controls"]] == [
        3,
        3,
    ]
    assert result["periodic_controls"][1]["projected_box_tail_nonzero_entries"] == 88
    result["periodic_controls"][1]["projected_box_tail_nonzero_entries"] = 0
    assert (
        exact_periodic_controls()["periodic_controls"][1]["projected_box_tail_nonzero_entries"]
        == 88
    )


@pytest.mark.parametrize("optimized", [False, True])
def test_runner_rejects_overwrite_and_disabled_assertions(tmp_path, optimized):
    output = tmp_path / "evidence.json"
    if not optimized:
        output.write_text("retained evidence", encoding="utf-8")
    args = [sys.executable, *(["-O"] if optimized else [])]
    args.extend(
        [str(ROOT / "scripts/verify_continuum_scale_comparison.py"), "--output", str(output)]
    )
    result = subprocess.run(args, cwd=ROOT, capture_output=True, text=True, check=False)
    assert result.returncode != 0
    assert ("assertions enabled" if optimized else "fresh output") in result.stderr
    if optimized:
        assert not output.exists()
    else:
        assert output.read_text(encoding="utf-8") == "retained evidence"
