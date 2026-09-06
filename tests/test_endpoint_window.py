"""Failure boundaries for exact endpoint counts and local tensor gradients."""

import copy
import importlib.util
import json
import shutil
import subprocess
import sys
from pathlib import Path

import pytest
import sympy as sp

ROOT = Path(__file__).resolve().parents[1]


@pytest.fixture(scope="module")
def selected():
    spec = importlib.util.spec_from_file_location(
        "selected_endpoint_runner", ROOT / "scripts/verify_endpoint_window.py"
    )
    runner = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(runner)
    old = {k: v for k, v in sys.modules.items() if k == "workhouse" or k.startswith("workhouse.")}
    native, invariants = runner.load_native()
    for name in list(sys.modules):
        if name == "workhouse" or name.startswith("workhouse."):
            del sys.modules[name]
    sys.modules.update(old)
    return runner, native, invariants


def endpoint_inputs():
    transfer = sp.diag(1, sp.Rational(1, 2), sp.Rational(1, 8))
    source = sp.Matrix([[1, 0], [0, sp.Rational(4, 5)], [0, sp.Rational(3, 5)]])
    return transfer, source, sp.Rational(1, 3), sp.Rational(3, 8)


def gradient_inputs():
    full = sp.diag(0, 4, 2, 2, 2)
    v, w = sp.Matrix([0, 1, 1, 0, 0]), sp.Matrix([0, 0, 0, 1, 1])
    return full, (v * v.T + w * w.T) / 10


def test_ten_checks_are_finite_and_complete(selected):
    _, native, invariants = selected
    checks = invariants.endpoint_window_suite.run()
    assert len(checks) == 10 and all(x.passed and x.tier == 1 for x in checks)
    payload = native.exact_endpoint_window_controls()
    assert set(payload) == {
        "endpoint",
        "localized_score",
        "local_gradient",
        "covariant_path",
        "fourier_alias",
    }
    assert [
        x["full_count"] for x in payload["endpoint"]["endpoint_and_two_lag"]["threshold_counts"]
    ] == [1, 2, 3]
    native.replay_endpoint_window_controls(payload)
    payload["endpoint"]["endpoint_and_two_lag"]["threshold_counts"][0]["full_count"] += 1
    with pytest.raises(ValueError, match="payload"):
        native.replay_endpoint_window_controls(payload)
    assert (
        native.exact_endpoint_window_controls()["endpoint"]["endpoint_and_two_lag"][
            "threshold_counts"
        ][0]["full_count"]
        == 1
    )


def test_full_endpoint_checks_the_complete_tail(selected):
    _, native, _ = selected
    inputs = endpoint_inputs()
    report = native.finite_endpoint_certificate(*inputs)
    assert report["full_count"] == report["exact_schur_count"] == 2
    assert report["two_lag"]["lower_count"] <= 2 <= report["two_lag"]["upper_count"]
    assert native.replay_finite_endpoint(*inputs, report) == report
    # The compressed moments alone cannot know whether the asserted d is valid.
    t, j, _, z = inputs
    moment_only = native.two_lag_count_certificate(j.T * t * j, j.T * t**2 * j, 0, z)
    assert moment_only["full_omitted_cap_is_external_hypothesis"]
    with pytest.raises(ValueError, match="entire omitted"):
        native.finite_endpoint_certificate(t, j, 0, z)


@pytest.mark.parametrize(
    "defect",
    ["missing_vacuum", "normalization", "float", "nonpositive", "above_one", "cap", "threshold"],
)
def test_full_endpoint_rejects_missing_hypotheses(selected, defect):
    _, native, _ = selected
    t, j, d, z = endpoint_inputs()
    if defect == "missing_vacuum":
        j = sp.eye(3)[:, [1, 2]]
    elif defect == "normalization":
        j[:, 1] *= 2
    elif defect == "float":
        t[1, 1] = 0.5
    elif defect == "nonpositive":
        t[2, 2] = -1
    elif defect == "above_one":
        t[2, 2] = 2
    elif defect == "cap":
        d = sp.Rational(1, 10)
    else:
        z = d
    with pytest.raises(ValueError):
        native.finite_endpoint_certificate(t, j, d, z)


def test_strict_threshold_does_not_count_equality(selected):
    _, native, _ = selected
    t = sp.diag(1, sp.Rational(1, 2), sp.Rational(1, 8))
    j = sp.eye(3)[:, [0, 1]]
    report = native.finite_endpoint_certificate(t, j, sp.Rational(1, 8), sp.Rational(1, 2))
    assert (
        report["full_count"]
        == report["two_lag"]["lower_count"]
        == report["two_lag"]["upper_count"]
        == 1
    )
    assert report["two_lag"]["lower_inertia"][2] == 1


@pytest.mark.parametrize(
    "defect",
    ["negative_variance", "impossible_contraction_moment", "nonsymmetric", "float", "wrong_shape"],
)
def test_moment_api_rejects_false_exact_moments(selected, defect):
    _, native, _ = selected
    a, a2 = sp.eye(2) / 2, sp.eye(2) / 3
    if defect == "negative_variance":
        a2 = sp.zeros(2)
    elif defect == "impossible_contraction_moment":
        a2 = sp.eye(2)
    elif defect == "nonsymmetric":
        a[0, 1] = 1
    elif defect == "float":
        a2[0, 0] = 0.333
    else:
        a2 = sp.eye(3)
    with pytest.raises(ValueError):
        native.two_lag_count_certificate(a, a2, sp.Rational(1, 4), sp.Rational(3, 4))


def test_two_lag_replay_rejects_changed_count(selected):
    _, native, _ = selected
    a, a2 = sp.eye(2) / 2, sp.eye(2) / 3
    d, z = sp.Rational(1, 4), sp.Rational(3, 4)
    report = native.two_lag_count_certificate(a, a2, d, z)
    native.replay_two_lag_count(a, a2, d, z, report)
    report["upper_count"] += 1
    with pytest.raises(ValueError, match="recomputation"):
        native.replay_two_lag_count(a, a2, d, z, report)


def test_tensor_gradient_uses_complete_nonorthonormal_profile_gram(selected):
    _, native, _ = selected
    full, bad = gradient_inputs()
    report = native.local_gradient_certificate(full, bad, 4)
    assert report["relative_cap"] == "1/20"
    assert len(report["profile_Gram"]) == 11
    assert report["profile_Gram"][-1][-1] == "3"
    assert sp.Matrix(report["complete_bad_form"]) == sp.diag(
        0, *([sp.Rational(1, 10)] * 4), *([sp.Rational(3, 5)] * 6)
    )
    assert native.replay_local_gradient(full, bad, 4, report) == report
    report["complete_bad_form"][1][2] = "1/10"
    with pytest.raises(ValueError, match="recomputation"):
        native.replay_local_gradient(full, bad, 4, report)


@pytest.mark.parametrize(
    "defect", ["uncentered", "negative", "overfull", "anisotropic_full", "copies", "float"]
)
def test_gradient_requires_local_domains_and_centering(selected, defect):
    _, native, _ = selected
    full, bad = gradient_inputs()
    copies = 2
    if defect == "uncentered":
        bad[0, 0] = 1
    elif defect == "negative":
        bad[1, 1] = -1
    elif defect == "overfull":
        bad *= 100
    elif defect == "anisotropic_full":
        full[3, 3] = 3
    elif defect == "copies":
        copies = True
    else:
        bad[1, 1] = 0.1
    with pytest.raises(ValueError):
        native.local_gradient_certificate(full, bad, copies)


def test_su2_leading_score_radial_and_pair_geometry(selected):
    _, native, _ = selected
    q1, q2 = [1, 0, 0], [0, 1, 0]
    assert native.su2_score_contraction(q1, q1)["centralizer_cancellation"]
    first = native.su2_score_contraction(q1, q2)
    second = native.su2_score_contraction(q2, q1)
    assert sp.Rational(first["angular_squared"]) + sp.Rational(second["angular_squared"]) == 2
    assert sp.Matrix(q1).cross(sp.Matrix(q2)) + sp.Matrix(q2).cross(sp.Matrix(q1)) == sp.zeros(3, 1)
    with pytest.raises(ValueError):
        native.su2_score_contraction([1.0, 0, 0], q2)


def complex_source_inputs():
    stiffness = sp.diag(0, 2, 3, 0)
    coulomb = sp.diag(1, 1, 1, 0)
    source = sp.Matrix([[1, 0], [0, 1], [0, sp.I], [0, 0]])
    return stiffness, coulomb, source, sp.Rational(1)


def test_Qi_floor_retains_harmonics_and_actual_complex_source_gram(selected):
    _, native, _ = selected
    inputs = complex_source_inputs()
    report = native.covariant_source_floor_certificate(*inputs)
    assert report["source_Gram"] == [["1", "0"], ["0", "2"]]
    assert report["physical_zero_modes_retained"]
    assert not report["unregulated_vacuum_asserted"]
    assert report["source_projection"][1][2] == "-I/2"
    assert native.replay_covariant_source_floor(*inputs, report) == report
    report["floor"] = "100"
    with pytest.raises(ValueError, match="recomputation"):
        native.replay_covariant_source_floor(*inputs, report)


def test_source_floor_rejects_compression_only_bound(selected):
    _, native, _ = selected
    stiffness = sp.Matrix([[1, 2], [2, sp.Rational(9, 2)]])
    assert stiffness.det() > 0 and stiffness[1, 1] >= 1
    assert (stiffness - sp.diag(0, 1)).det() < 0
    with pytest.raises(ValueError, match="negative exact pivot"):
        native.covariant_source_floor_certificate(stiffness, sp.eye(2), sp.Matrix([1, 0]), 1)


@pytest.mark.parametrize(
    "defect",
    [
        "missing_harmonic",
        "not_transverse",
        "false_floor",
        "not_projection",
        "nonhermitian",
        "not_Qi",
        "dependent",
    ],
)
def test_source_floor_requires_full_geometry(selected, defect):
    _, native, _ = selected
    stiffness, coulomb, source, floor = complex_source_inputs()
    if defect == "missing_harmonic":
        source = source[:, [1]]
    elif defect == "not_transverse":
        source[3, 1] = 1
    elif defect == "false_floor":
        floor = 100
    elif defect == "not_projection":
        coulomb[0, 0] = 2
    elif defect == "nonhermitian":
        stiffness[1, 2] = sp.I
    elif defect == "not_Qi":
        source[1, 1] = sp.sqrt(2)
    else:
        source[:, 1] = source[:, 0]
    with pytest.raises(ValueError):
        native.covariant_source_floor_certificate(stiffness, coulomb, source, floor)


def test_selected_runner_cold_replay_overwrite_and_optimization(selected, tmp_path):
    runner, _, _ = selected
    cold = tmp_path / "cold"
    for name in runner.SOURCES:
        dest = cold / name
        dest.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(ROOT / name, dest)
    certificate = tmp_path / "certificate.json"
    verify = cold / "scripts/verify_endpoint_window.py"
    replay = cold / "scripts/replay_endpoint_window.py"
    command = [sys.executable, "-B", str(verify), "--output", str(certificate)]
    generated = subprocess.run(command, capture_output=True, text=True, cwd=tmp_path)
    assert generated.returncode == 0, generated.stderr
    before = certificate.read_bytes()
    repeated = subprocess.run(command, capture_output=True, text=True, cwd=tmp_path)
    assert repeated.returncode != 0 and "fresh output" in repeated.stderr
    checked = subprocess.run(
        [sys.executable, "-B", str(replay), str(certificate)],
        capture_output=True,
        text=True,
        cwd=tmp_path,
    )
    assert checked.returncode == 0, checked.stderr
    assert certificate.read_bytes() == before
    fresh = tmp_path / "forbidden.json"
    for cmd in (
        [sys.executable, "-O", str(verify), "--output", str(fresh)],
        [sys.executable, "-O", str(replay), str(certificate)],
    ):
        rejected = subprocess.run(cmd, capture_output=True, text=True, cwd=tmp_path)
        assert rejected.returncode != 0 and "assertions" in rejected.stderr
    assert not fresh.exists()
    report = json.loads(before)
    changed = copy.deepcopy(report)
    changed["controls"]["localized_score"]["fisher"]["radial_contraction"] = 1
    corrupt = tmp_path / "corrupt.json"
    corrupt.write_text(json.dumps(changed), encoding="utf-8")
    rejected = subprocess.run(
        [sys.executable, "-B", str(replay), str(corrupt)],
        capture_output=True,
        text=True,
        cwd=tmp_path,
    )
    assert rejected.returncode != 0 and "recomputation" in rejected.stderr
    (cold / runner.SOURCES[0]).write_bytes((cold / runner.SOURCES[0]).read_bytes() + b"\n")
    rejected = subprocess.run(
        [sys.executable, "-B", str(replay), str(certificate)],
        capture_output=True,
        text=True,
        cwd=tmp_path,
    )
    assert rejected.returncode != 0 and "source pins" in rejected.stderr
