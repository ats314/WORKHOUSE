"""Unit tests for the Universal Cellular Hodge-Feshbach Theorem & Tetrahedral Resolution.

Tests the findings of U3, U7, G14 and resolves the ADR 0008 / ADR 0045 challenge.
"""

from __future__ import annotations

import sys
from pathlib import Path

import sympy as sp
from sympy import Matrix, eye, ones, zeros

from workhouse import cellular as CELL

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import verify_universal_hodge_tetrahedral as vh


def test_universal_hodge_spectrum_and_annihilation():
    """Verify that lambda = |F| and L_up Q = 0 hold across multiple polyhedral families."""
    cells = [
        CELL.TETRAHEDRON,
        CELL.TRIANGULAR_PRISM,
        CELL.CUBE,
        CELL.PENTAGONAL_PRISM,
        CELL.prism(6),
    ]
    results = vh.verify_universal_hodge_spectrum(cells)
    assert len(results) == len(cells)
    for name, r in results.items():
        assert r["lambda"] == r["n_faces"]
        assert r["up_harmonic"] is True
        # Cube (4-prism) and tetrahedron are regular with scalar diagonals; other prisms are irregular
        if name in ("tetrahedron", "4-gonal prism"):
            assert r["is_regular"] is True
        else:
            assert r["is_regular"] is False


def test_tetrahedral_s4_commutant_and_schur_lemma():
    """Verify tetrahedral S_4 representation commutant coincides with Hodge algebra."""
    res = vh.verify_tetrahedral_s4_commutant()
    assert res["hodge_proportionality"] is True
    assert res["s4_commutation"] is True
    assert res["commutant_is_hodge"] is True
    assert res["traceless_compression_vanishes"] is True
    assert res["off_carrier_vanishes"] is True


def test_tetrahedral_proper_returns_q_annihilation():
    """Verify that all proper returns on tetrahedron vanish after intermediate Q-projection."""
    res = vh.verify_tetrahedral_proper_returns()
    assert res["second_order_scalar_rest"] is True
    assert res["all_returns_annihilated_by_Q"] is True
    assert res["proper_returns_count"] == 60
    assert res["direct_transports_count"] == 36


def test_tetrahedral_algebraic_isomorphisms():
    """Verify exact matrix identities for tetrahedral Hodge generators."""
    tet = CELL.TETRAHEDRON
    B = Matrix(tet.boundary_matrix())
    L_down = B.T * B
    psi = Matrix(CELL.integer_kernel(tet)[0])
    L_up = psi * psi.T
    P = (psi * psi.T) / 4
    Q = eye(4) - P

    # Exact relations
    assert L_down == 4 * Q
    assert L_up == 4 * P
    assert L_down + L_up == 4 * eye(4)
    assert L_down * L_up == zeros(4, 4)
    assert L_up * Q == zeros(4, 4)
    assert L_down * P == zeros(4, 4)

    # Commutant test for arbitrary symmetric matrix
    M = Matrix([[10, 2, 2, 2], [2, 10, 2, 2], [2, 2, 10, 2], [2, 2, 2, 10]])
    assert M * P == P * M
    assert M * Q == Q * M
    # Compression is pure scalar:
    assert Q * M * Q == 8 * Q
    assert Q * M * P == zeros(4, 4)
    assert P * M * Q == zeros(4, 4)
    # Traceless part:
    assert Q * M * Q - (sp.trace(Q * M * Q) / 3) * Q == zeros(4, 4)


def test_r_sm_r_carrier_symbol_master_theorem():
    """Verify that the closed-form carrier symbol master theorem holds for m=0..4."""
    res = vh.verify_r_sm_r_master_theorem(max_m=4)
    assert len(res) == 5
    for m in range(5):
        assert res[m] is True

