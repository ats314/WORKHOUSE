"""Exact creator inversion, independent tensor paths and their scope boundaries."""

import itertools
import json
import subprocess
import sys
from pathlib import Path

import pytest
import sympy as sp
from sympy.matrices.exceptions import NonInvertibleMatrixError

from workhouse import wilson_creator_velocity as V


@pytest.fixture(scope="module")
def controls():
    return V.exact_controls()


def test_exact_entangled_and_complex_paths_check_every_map_column(controls):
    models = controls["models"]
    assert [m["dimensions"] for m in models] == [[3, 3, 2], [3, 2]]
    assert [m["map_columns_checked"] for m in models] == [17, 5]
    assert all(m["independent_exponential_and_map"] for m in models)
    assert all(m["real_linear_inverse_residual_zero"] for m in models)
    assert all(m["normalized_vacuum_line_transport"] for m in models)
    assert models[0]["phase_rate"] == "0"
    assert sp.Rational(models[1]["phase_rate"]) != 0


def test_support_inverse_is_independent_of_tensor_matrix_construction(monkeypatch):
    def forbidden(*_):
        raise AssertionError("Support algebra must not call tensor matrices")

    monkeypatch.setattr(V.TensorSpace, "creator_matrix", forbidden)
    space = V.TensorSpace((2,))
    b, matrix = space.invert_velocity({(1,): sp.Rational(1, 10)}, {(1,): sp.I / 20})
    assert b == {(1,): 5 * sp.I / 99}
    assert matrix == sp.Matrix([[-sp.Rational(1, 100)]])


def test_tensor_exponential_is_independent_of_support_convolution(monkeypatch):
    def forbidden(*_):
        raise AssertionError("Tensor matrices must not call support convolution")

    monkeypatch.setattr(V.TensorSpace, "star", forbidden)
    space = V.TensorSpace((2, 2))
    exponential = space.matrix_exponential({(1, 0): 2, (0, 1): 3})
    assert exponential[:, 0] == sp.Matrix([1, 3, 2, 6])


def test_local_creator_keeps_excited_spectators_and_entanglement():
    space = V.TensorSpace((3, 3, 2))
    w = {(1, 1, 0): sp.Rational(1, 300), (2, 2, 0): -sp.Rational(1, 400)}
    matrix = space.creator_matrix(w)
    # The exact excited vector is rank two across its two qutrit factors.
    assert sp.diag(sp.Rational(1, 300), -sp.Rational(1, 400)).rank() == 2
    spectator = space.indices[(0, 0, 1)]
    assert matrix[space.indices[(1, 1, 1)], spectator] == sp.Rational(1, 300)
    assert matrix[space.indices[(2, 2, 1)], spectator] == -sp.Rational(1, 400)
    assert matrix**2 == sp.zeros(18)


def test_complex_linear_substitution_fails_the_true_conjugate_linear_equation():
    space = V.TensorSpace((2,))
    w = {(1,): sp.Rational(1, 10)}
    tangent = sp.Matrix([sp.I / 20])
    matrix = space.conjugate_matrix(w)
    naive = (sp.eye(1) - matrix).inv() * tangent
    assert naive - matrix * naive.conjugate() != tangent
    result = V.phase_control()
    assert result["normalized_vector_phase_rate"] == "1/198"


def test_global_inverse_respects_disjoint_component_factorization(controls):
    factor = controls["factorization"]
    assert factor["global_inverse_equals_embedded_local_inverses"]
    assert factor["cross_component_velocities_zero"]
    assert factor["generator_is_tensor_sum"]
    assert factor["creation_exponential_factorizes"]


def test_neumann_remainder_is_nonzero_and_rigorously_bounded(controls):
    assert [sp.Rational(m["finite_rooted_matrix_bound"]) for m in controls["models"]] == [
        sp.Rational(1321, 112500),
        sp.Rational(123, 5000),
    ]
    for model in controls["models"]:
        assert model["neumann_terms"] == 4
        assert (
            0
            < sp.Rational(model["neumann_remainder_norm"])
            <= sp.Rational(model["neumann_remainder_bound"])
        )
        assert sp.Rational(model["finite_rooted_matrix_bound"]) <= sp.Rational(
            model["rational_upper_envelope_of_analytic_bound"]
        )


def test_rooted_column_anchor_bound_handles_changed_roots_and_complex_inputs():
    space = V.TensorSpace((2, 2))
    matrix = sp.Matrix([[0, 2, sp.I], [sp.I, 0, 3], [1 + sp.I, -2, 0]])
    bound = space.rooted_matrix_bound(matrix)
    for entries in itertools.product((0, 1, -1, sp.I), repeat=3):
        vector = sp.Matrix(entries)
        before = space.family(sp.Matrix([0]).col_join(vector))
        after = space.family(sp.Matrix([0]).col_join(matrix * vector.conjugate()))
        assert space.rooted_norm(after) <= bound * space.rooted_norm(before)


@pytest.mark.parametrize("dimensions", [(), (1,), (2.5,)])
def test_invalid_local_dimensions_are_rejected(dimensions):
    with pytest.raises(ValueError, match="dimensions at least two"):
        V.TensorSpace(dimensions)


def test_empty_support_inexact_coefficients_and_invalid_basis_are_rejected():
    space = V.TensorSpace((2,))
    with pytest.raises(ValueError, match="empty-support"):
        space.exponential({(0,): 1})
    with pytest.raises(TypeError, match="exact rational"):
        space.exponential({(1,): 0.1})
    with pytest.raises(ValueError, match="outside"):
        space.exponential({(2,): 1})
    with pytest.raises(ValueError, match="shape"):
        space.family(sp.zeros(3, 1))


def test_large_creator_can_make_the_real_linear_inverse_singular():
    space = V.TensorSpace((2,))
    with pytest.raises(NonInvertibleMatrixError):
        space.invert_velocity({(1,): 1}, {(1,): sp.I})


def test_noncommuting_contour_keeps_order_and_connected_partition_subtraction(controls):
    contour = controls["ordered_contour"]
    assert contour["connected_words_equal_partition_cumulants"]
    assert contour["connected_words_per_order"] == [0, 0, 6, 24]
    assert sp.Rational(contour["overlap_commutator_frobenius_squared"]) == sp.Rational(3, 4)


def test_scalar_bounds_retain_the_analytic_premises(controls):
    bounds = controls["scalar_bounds"]
    assert sp.Rational(bounds["primitive_upper"]) == sp.Rational(71, 181250) < sp.Rational(1, 2500)
    assert (
        sp.Rational(bounds["full_operator_upper"]) == sp.Rational(1, 998) < sp.Rational(512, 78125)
    )
    assert sp.Rational(bounds["chart_velocity_upper"]) == sp.Rational(1, 6)
    assert "log(5/4) >= 1/5" in bounds["transcendental_premises"]


def test_runner_records_finite_scope_and_refuses_overwrite(tmp_path):
    root = Path(__file__).resolve().parents[1]
    output = tmp_path / "velocity.json"
    command = [
        sys.executable,
        str(root / "scripts/verify_wilson_creator_velocity.py"),
        "--output",
        str(output),
    ]
    process = subprocess.run(command, cwd=root, capture_output=True, text=True, check=False)
    assert process.returncode == 0, process.stderr
    original = output.read_bytes()
    report = json.loads(original)
    assert report["passed"]
    assert all(check["tier"] == 1 and check["passed"] for check in report["checks"])
    assert len(report["finite_controls"]["models"]) == 2
    assert "No uniform Wilson analytic theorem" in report["verification_scope"]
    repeat = subprocess.run(command, cwd=root, capture_output=True, text=True, check=False)
    assert repeat.returncode != 0 and "fresh output" in repeat.stderr
    assert output.read_bytes() == original


def test_runner_cannot_certify_with_assertions_disabled(tmp_path):
    root = Path(__file__).resolve().parents[1]
    output = tmp_path / "optimized.json"
    command = [
        sys.executable,
        "-O",
        str(root / "scripts/verify_wilson_creator_velocity.py"),
        "--output",
        str(output),
    ]
    process = subprocess.run(command, cwd=root, capture_output=True, text=True, check=False)
    assert process.returncode != 0 and "assertions enabled" in process.stderr
    assert not output.exists()
