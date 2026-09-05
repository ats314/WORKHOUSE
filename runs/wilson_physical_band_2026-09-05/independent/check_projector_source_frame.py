"""Exact finite controls for the close-projection/source-frame bridge."""

from __future__ import annotations

import hashlib
import itertools
import json
from pathlib import Path

import sympy as sp


def psd(matrix):
    """All principal minors, an exact finite PSD certificate."""
    assert matrix == matrix.T
    minors = []
    for size in range(1, matrix.rows + 1):
        for positions in itertools.combinations(range(matrix.rows), size):
            determinant = matrix.extract(positions, positions).det()
            assert determinant >= 0
            minors.append(str(determinant))
    return minors


def rotated_band():
    cosines = (sp.Rational(399, 401), sp.Rational(1599, 1601))
    sines = (sp.Rational(40, 401), sp.Rational(80, 1601))
    unitary = sp.zeros(4)
    for i, (c, s) in enumerate(zip(cosines, sines, strict=True)):
        assert c*c+s*s == 1
        unitary[i, i] = unitary[i+2, i+2] = c
        unitary[i+2, i] = s
        unitary[i, i+2] = -s
    identity = sp.eye(4)
    p0 = sp.diag(1, 1, 0, 0)
    p = unitary*p0*unitary.T
    assert unitary.T*unitary == identity
    c, d = sp.Rational(3, 4), sp.Rational(1, 4)
    free = c*p0+d*(identity-p0)
    dressed = unitary*free*unitary.T
    gap = c-d
    epsilon = gap*max(sines)
    delta = max(sines)
    assert epsilon <= gap/10
    assert delta <= epsilon/(gap-epsilon) <= sp.Rational(1, 9)
    error = dressed-free
    norm_certificate = psd(epsilon**2*identity-error**2)
    assert (epsilon**2*identity-error**2).det() == 0
    projection_certificate = psd(delta**2*identity-(p-p0)**2)
    assert (delta**2*identity-(p-p0)**2).det() == 0
    rotation = p*p0+(identity-p)*(identity-p0)
    square_root = sp.diag(*cosines, *cosines)
    assert rotation.T*rotation == identity-(p-p0)**2 == square_root**2
    assert rotation*square_root.inv() == unitary
    assert unitary*p0 == p*unitary
    assert unitary+unitary.T == 2*square_root
    j0 = identity[:, :2]
    perturbation = sp.Matrix([[1, 2], [2, -1], [2, 4], [4, -2]])/5
    assert perturbation.T*perturbation == sp.eye(2)
    eta = sp.Rational(1, 8)
    source = j0+eta*perturbation
    a0, a = p*j0, p*source
    inverse0 = j0.T*square_root.inv()*unitary.T
    assert inverse0*a0 == sp.eye(2)
    assert a0*inverse0*p == p
    coefficient_map = sp.eye(2)+inverse0*p*(source-j0)
    assert a == a0*coefficient_map
    assert coefficient_map.det() != 0
    inverse = coefficient_map.inv()*inverse0
    assert inverse*a == sp.eye(2)
    assert a*inverse*p == p
    lower = sp.Rational(559, 648)
    gram = source.T*p*source
    gram_lower = psd(gram-lower**2*sp.eye(2))
    gram_upper = psd((1+eta)**2*sp.eye(2)-gram)
    assert lower > sp.Rational(3, 4)
    assert 1/lower < sp.Rational(6, 5)
    return {
        "epsilon": str(epsilon), "gap": str(gap), "projection_norm": str(delta),
        "projection_bound": str(epsilon/(gap-epsilon)),
        "source_error": str(eta), "gram_lower": str(lower**2),
        "operator_norm_principal_minors": norm_certificate,
        "projection_norm_principal_minors": projection_certificate,
        "gram_lower_principal_minors": gram_lower,
        "gram_upper_principal_minors": gram_upper,
        "coefficient_map_determinant": str(coefficient_map.det()),
        "direct_rotation_and_two_sided_inverse_verified": True,
    }


def negative_controls():
    # Rectangular finite restriction of the infinite unilateral shift.
    shift = sp.zeros(6, 5)
    for i in range(5):
        shift[i+1, i] = 1
    assert shift.T*shift == sp.eye(5)
    assert shift*shift.T == sp.diag(0, 1, 1, 1, 1, 1)
    # Small columns do not control synthesis norm or completeness.
    count = 64
    defect = sp.ones(count)/count
    source = sp.eye(count)-defect
    assert defect**2 == defect
    assert source*sp.ones(count, 1) == sp.zeros(count, 1)
    assert all((defect[:, i].T*defect[:, i])[0] == sp.Rational(1, count) for i in range(count))
    # Finite checks of the strongly convergent cycle example on a common space.
    cycle_checks = []
    for length in (5, 9):
        cycle = sp.zeros(length+1)
        cycle[0, length] = 1
        for i in range(length):
            cycle[i+1, i] = 1
        assert cycle.T*cycle == sp.eye(length+1)
        for i in range(4):
            assert cycle[:, i] == sp.eye(length+1)[:, i+1]
        assert cycle.T[:, 0] == sp.eye(length+1)[:, length]
        cycle_checks.append(length)
    return {
        "rectangular_shift_gram_identity": True,
        "rectangular_shift_missing_vector": "e_0",
        "small_column_example_size": count,
        "column_error_norm": "1/8",
        "synthesis_error_norm": "1",
        "source_kernel_vector": "(1,...,1)",
        "unitary_cycle_lengths_checked": cycle_checks,
        "scope": "Finite witnesses; the infinite unilateral shift and strong-limit arguments are proved in the companion note",
    }


def main():
    if not __debug__:
        raise RuntimeError("Assertions must be enabled")
    root = Path(__file__).resolve().parent
    files = (Path(__file__), root / "PROJECTOR_SOURCE_FRAME_BRIDGE.md")
    result = {
        "scope": "Exact finite direct-rotation and source-frame algebra, not the actual Wilson source norm or thermodynamic operator limit",
        "rotated_band": rotated_band(),
        "negative_controls": negative_controls(),
        "sources": {path.name: hashlib.sha256(path.read_bytes()).hexdigest() for path in files},
    }
    destination = root / "projector_source_frame_control.json"
    with destination.open("x", encoding="utf-8") as stream:
        json.dump(result, stream, indent=2, sort_keys=True)
        stream.write("\n")
    print("Exact direct rotation, two-sided inverse, Gram bounds and negative controls passed")


if __name__ == "__main__":
    main()
