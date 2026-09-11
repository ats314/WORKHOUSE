"""Regression checks for cellular algebra and the repaired physical-history boundary."""

from fractions import Fraction
from types import SimpleNamespace

import sympy as sp

from workhouse import cellular as CELL
from workhouse.invariants import hodge_feshbach as HF
from workhouse.invariants import universal_cellular_hodge as H


def test_spectrum_across_prisms():
    results = H.verify_cellular_spectrum(H.example_cells())
    assert len(results) == 7
    assert [row["lambda"] for row in results.values()] == [4, 5, 6, 7, 8, 9, 10]
    assert results["4-gonal prism"]["diag"] == [5] * 6
    assert results["5-gonal prism"]["diag"] == [6, 6, 5, 5, 5, 5, 5]


def test_reoriented_face_preserves_spectrum_but_changes_carrier_signs():
    tetrahedron = CELL.TETRAHEDRON
    signs = sp.diag(-1, 1, 1, 1)
    reoriented = SimpleNamespace(
        name="one face reversed",
        faces=tetrahedron.faces,
        boundary_matrix=lambda: tetrahedron.boundary_matrix() * signs,
    )
    _, psi, _, _, _, complement = H.cellular_data(reoriented)
    assert len(set(psi)) == 2
    assert complement * psi == sp.zeros(4, 1)
    assert H.verify_cellular_spectrum([reoriented])[reoriented.name]["lambda"] == 4


def test_equal_perimeters_do_not_require_a_regular_polyhedron():
    bipyramid = CELL.Cell(
        "triangular bipyramid",
        ((0, 1, 2), (0, 2, 3), (0, 3, 1), (4, 2, 1), (4, 3, 2), (4, 1, 3)),
    )
    results = H.verify_cellular_spectrum([bipyramid])[bipyramid.name]
    assert results["n_faces"] == 6
    assert results["diag"] == [4] * 6
    assert results["equal_perimeters"]


def test_full_tetrahedral_commutant():
    assert H.verify_tetrahedral_commutant() == {"commutant_dimension": 2, "permutations": 24}


def test_flux_enumeration_does_not_annihilate_face_states():
    result = H.tetrahedral_flux_returns()
    assert result["total_paths"] == 96
    assert result["endpoint_or_zero_prefixes"] == 60
    assert result["other_paths"] == 36
    assert result["any_positive_face_or_zero_prefixes"] == 62
    assert result["Q_face0_norm_squared"] == sp.Rational(3, 4)
    assert result["Q_face0"] != result["Q_psi"]


def test_raw_retained_prefix_does_not_replace_the_projected_chain():
    # A finite algebra counterexample to the received generic inference;
    # this does not model physical tetrahedral Haar histories.
    projection = sp.diag(1, 0)
    complement = sp.eye(2) - projection
    v1 = sp.ones(2)
    v2 = sp.Matrix([[0, 1], [1, -1]])
    v3 = sp.Matrix([[0, 1], [1, 0]])
    raw_prefix = v2 * v1 * projection
    assert complement * raw_prefix == sp.zeros(2)
    projected_chain = projection * v3 * complement * v2 * complement * v1 * projection
    assert projected_chain == -projection


def test_master_instances_and_polynomial_extension_at_zero():
    assert all(H.verify_master_symbols().values())
    q = sp.Symbol("q")
    assert H.geometric_polynomial(4, q) == q**3 - 16 * q**2 + 96 * q - 256
    assert H.geometric_polynomial(0, q) == 0
    for m in range(1, 8):
        pi = H.geometric_polynomial(m, q)
        assert sp.expand(q * pi - (q - 4) ** m + (-4) ** m) == 0
        assert pi.subs(q, 0) == m * (-4) ** (m - 1)


def test_master_uses_shifted_operator_not_total_laplacian():
    identity, down, up, shifted, hopping = HF._ops()
    total = H.KO.combine((1, down), (1, up))
    generators = {"S": shifted, "T": total, "R": hopping}

    def at_pi(word):
        poly = HF._sigma(word, generators, identity, HF._psi())
        return sum(c * Fraction(-1) ** sum(e) for e, c in poly.items())

    assert at_pi("RSR") == -3072
    assert at_pi("RTR") == 9216
    assert at_pi("RSSSSR") == 196608
