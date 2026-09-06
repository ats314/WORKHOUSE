"""Failure boundaries for finite literal-source acceptance and selected-tree replay."""

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
        "selected_literal_runner", ROOT / "scripts/verify_literal_coarse_sources.py"
    )
    runner = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(runner)
    # Restore an enclosing pytest process's previously loaded workhouse
    # package after selecting isolated modules; keep returned references.
    old = {
        name: value
        for name, value in sys.modules.items()
        if name == "workhouse" or name.startswith("workhouse.")
    }
    native, invariants = runner.load_native()
    for name in list(sys.modules):
        if name == "workhouse" or name.startswith("workhouse."):
            del sys.modules[name]
    sys.modules.update(old)
    return runner, native, invariants


def test_seven_native_checks_have_finite_scopes(selected):
    _, native, invariants = selected
    results = invariants.literal_coarse_suite.run()
    assert len(results) == 7 and all(item.passed and item.tier == 1 for item in results)
    payload = native.exact_literal_coarse_controls()
    assert set(payload) == {
        "literal",
        "common_gauss",
        "score",
        "gaussian",
        "central_score",
        "literal_inverse",
    }
    assert sp.Rational(
        payload["gaussian"]["wrong_source_physical_counterexample"]["rayleigh"]
    ) == sp.Rational(803, 1364)


def projection_inputs():
    vacuum = sp.Matrix([sp.Rational(3, 5), sp.Rational(4, 5)])
    return vacuum, sp.ones(2, 1), 7 * (sp.eye(2) - vacuum * vacuum.T) + 13 * sp.eye(2)


def test_exact_marginal_and_full_vacuum_subtraction(selected):
    _, native, _ = selected
    vacuum, coarse, hamiltonian = projection_inputs()
    certificate = native.literal_projection_certificate(vacuum, coarse, hamiltonian, 13)
    assert certificate["compressed_form"] == [["0"]]
    assert certificate["source_Gram"] == [["1"]]
    assert (
        native.replay_literal_projection(vacuum, coarse, hamiltonian, 13, certificate)
        == certificate
    )
    with pytest.raises(ValueError, match="subtraction"):
        native.literal_projection_certificate(vacuum, coarse, hamiltonian, 0)


@pytest.mark.parametrize(
    "defect", ["normalization", "sign", "missing_constant", "rank", "float", "negative_energy"]
)
def test_literal_source_hypotheses_are_required(selected, defect):
    _, native, _ = selected
    vacuum, coarse, hamiltonian = projection_inputs()
    if defect == "normalization":
        vacuum *= 2
    elif defect == "sign":
        vacuum[0] *= -1
    elif defect == "missing_constant":
        coarse = sp.Matrix([1, 0])
    elif defect == "rank":
        coarse = sp.ones(2, 2)
    elif defect == "float":
        hamiltonian[0, 0] = float(hamiltonian[0, 0])
    else:
        hamiltonian = 13 * sp.eye(2) - 7 * (sp.eye(2) - vacuum * vacuum.T)
    with pytest.raises(ValueError):
        native.literal_projection_certificate(vacuum, coarse, hamiltonian, 13)


def gaussian_inputs():
    return sp.Matrix([[2, 1], [1, 2]]) / 2, sp.Matrix([1, 0]), sp.Rational(1, 3)


def test_gaussian_certificate_uses_the_full_boundary_premise(selected):
    _, native, _ = selected
    root, source, floor = gaussian_inputs()
    certificate = native.gaussian_source_certificate(root, source, floor)
    assert not certificate["source_commutes_with_frequency"]
    assert native.replay_gaussian_source(root, source, floor, certificate) == certificate
    # Compression of K to S-perp is 41/16 >= 1. The full K-Q_S is
    # indefinite, so a compression-only verifier would accept this false input.
    assert (root**4)[1, 1] >= 1
    with pytest.raises(ValueError):
        native.gaussian_source_certificate(root, source, 1)


@pytest.mark.parametrize(
    "defect",
    ["zero_floor", "negative_floor", "singular", "nonpositive", "float", "rank", "dimension"],
)
def test_gaussian_certificate_rejects_missing_domains(selected, defect):
    _, native, _ = selected
    root, source, floor = gaussian_inputs()
    if defect == "zero_floor":
        floor = 0
    elif defect == "negative_floor":
        floor = -1
    elif defect == "singular":
        root = sp.diag(0, 2)
    elif defect == "nonpositive":
        root = -root
    elif defect == "float":
        floor = 0.3
    elif defect == "rank":
        source = sp.ones(2, 2)
    else:
        source = sp.ones(3, 1)
    with pytest.raises(ValueError):
        native.gaussian_source_certificate(root, source, floor)


def test_commuting_and_fully_retained_gaussian_cases_are_valid(selected):
    _, native, _ = selected
    assert native.gaussian_source_certificate(sp.diag(1, 2), sp.Matrix([1, 0]), 4)[
        "source_commutes_with_frequency"
    ]
    assert native.gaussian_source_certificate(sp.diag(1, 2), sp.eye(2), 100)[
        "full_boundary_PSD_pivots"
    ] == ["1", "16"]


def test_noncommuting_fisher_cap_and_missing_positivity(selected):
    _, native, _ = selected
    metric, fisher = sp.Matrix([[2, 1], [1, 2]]), sp.diag(1, 2)
    certificate = native.fisher_cap_certificate(metric, fisher, 6)
    assert not certificate["commuting"]
    assert native.replay_fisher_cap(metric, fisher, 6, certificate) == certificate
    with pytest.raises(ValueError):
        native.fisher_cap_certificate(metric, fisher, 3)
    with pytest.raises(ValueError):
        native.fisher_cap_certificate(metric, sp.diag(-1, 2), 6)


@pytest.mark.parametrize("kind", ["literal", "gaussian", "fisher"])
def test_generic_replay_rejects_corrupted_certificate(selected, kind):
    _, native, _ = selected
    if kind == "literal":
        arguments = (*projection_inputs(), 13)
        certificate = native.literal_projection_certificate(*arguments)
        certificate["source_Gram"] = [["100"]]
        replay = native.replay_literal_projection
    elif kind == "gaussian":
        arguments = gaussian_inputs()
        certificate = native.gaussian_source_certificate(*arguments)
        certificate["P_R"][0][0] = "0"
        replay = native.replay_gaussian_source
    else:
        arguments = (sp.eye(2), sp.eye(2), 1)
        certificate = native.fisher_cap_certificate(*arguments)
        certificate["slack_PSD_pivots"] = ["1", "1"]
        replay = native.replay_fisher_cap
    with pytest.raises(ValueError, match="recomputation"):
        replay(*arguments, certificate)


def test_full_payload_replay_and_cached_mutation_isolation(selected):
    _, native, _ = selected
    payload = native.exact_literal_coarse_controls()
    native.replay_literal_coarse_controls(payload)
    payload["score"]["nonzero_connection_torus"]["exact_cross_form"] = "0"
    with pytest.raises(ValueError, match="recomputation"):
        native.replay_literal_coarse_controls(payload)
    assert (
        native.exact_literal_coarse_controls()["score"]["nonzero_connection_torus"][
            "exact_cross_form"
        ]
        == "-1/8"
    )


def full_domination_inputs():
    vacuum = sp.diag(1, 0, 0, 0)
    vector = sp.Matrix([0, sp.Rational(3, 5), sp.Rational(4, 5), 0])
    return sp.diag(0, 4, 7, 11), vacuum + vector * vector.T, vacuum


def test_full_inverse_domination_differs_from_the_compressed_floor(selected):
    _, native, _ = selected
    arguments = (*full_domination_inputs(), sp.Rational(175, 37))
    certificate = native.literal_full_domination_certificate(*arguments)
    assert native.replay_literal_full_domination(*arguments, certificate) == certificate
    with pytest.raises(ValueError):
        native.literal_full_domination_certificate(*full_domination_inputs(), sp.Rational(127, 25))
    certificate["reduced_inverse"][1][1] = "0"
    with pytest.raises(ValueError, match="recomputation"):
        native.replay_literal_full_domination(*arguments, certificate)


@pytest.mark.parametrize(
    "defect", ["missing_vacuum", "incomplete_kernel", "wrong_shift", "nonprojection"]
)
def test_full_inverse_floor_requires_the_exact_entire_vacuum(selected, defect):
    _, native, _ = selected
    hamiltonian, retained, vacuum = full_domination_inputs()
    if defect == "missing_vacuum":
        retained -= vacuum
    elif defect == "incomplete_kernel":
        hamiltonian[3, 3] = 0
    elif defect == "wrong_shift":
        hamiltonian += sp.eye(4)
    else:
        retained[0, 0] = 2
    with pytest.raises(ValueError):
        native.literal_full_domination_certificate(hamiltonian, retained, vacuum, 1)


@pytest.fixture(scope="module")
def relocated_tree(selected, tmp_path_factory):
    runner, _, _ = selected
    root = tmp_path_factory.mktemp("literal-selected-tree")
    for relative in runner.SOURCES:
        destination = root / relative
        destination.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(ROOT / relative, destination)
    return root


def run_script(tree, basename, *arguments, optimize=False):
    command = [
        sys.executable,
        *(["-O"] if optimize else []),
        str(tree / "scripts" / basename),
        *map(str, arguments),
    ]
    return subprocess.run(command, cwd=tree, capture_output=True, text=True, timeout=90)


def test_fresh_runner_read_only_replay_and_corruptions(relocated_tree):
    root = relocated_tree
    output = root / "certificate.json"
    result = run_script(root, "verify_literal_coarse_sources.py", "--output", output)
    assert result.returncode == 0, result.stderr
    before = {
        path.relative_to(root): path.read_bytes() for path in root.rglob("*") if path.is_file()
    }
    replay = run_script(root, "replay_literal_coarse_sources.py", output)
    assert replay.returncode == 0, replay.stderr
    assert before == {
        path.relative_to(root): path.read_bytes() for path in root.rglob("*") if path.is_file()
    }
    assert b"\r\n" not in output.read_bytes()
    overwrite = run_script(root, "verify_literal_coarse_sources.py", "--output", output)
    assert overwrite.returncode != 0 and "fresh output" in overwrite.stderr
    assert output.read_bytes() == before[Path("certificate.json")]
    report = json.loads(output.read_text(encoding="utf-8"))
    for name in ("controls", "sources", "checks"):
        corrupt = copy.deepcopy(report)
        if name == "controls":
            corrupt[name]["gaussian"]["full_low_window"]["low_dimension"] = 25
        elif name == "sources":
            corrupt[name][next(iter(corrupt[name]))] = "0" * 64
        else:
            corrupt[name][0]["detail"] = "The full analytic theorem is machine proved"
        path = root / (name + "-corrupt.json")
        path.write_text(json.dumps(corrupt), encoding="utf-8")
        assert run_script(root, "replay_literal_coarse_sources.py", path).returncode != 0


def test_optimized_verification_and_replay_are_rejected(relocated_tree):
    root = relocated_tree
    output = root / "optimized.json"
    verify = run_script(root, "verify_literal_coarse_sources.py", "--output", output, optimize=True)
    replay = run_script(
        root, "replay_literal_coarse_sources.py", "does-not-exist.json", optimize=True
    )
    assert verify.returncode != 0 and "assertions enabled" in verify.stderr
    assert replay.returncode != 0 and "assertions enabled" in replay.stderr
    assert not output.exists()
