"""Exact cellular Hodge algebra and scoped tetrahedral flux diagnostics.

Physical Haar/Fierz histories and their retained projector remain unidentified.
The all-power master formula uses S = L_down - 4 I, never the total Laplacian.
"""

from __future__ import annotations

import itertools
from fractions import Fraction

import sympy as sp

from .. import cellular as CELL
from .. import kernel_orbits as KO
from . import hodge_feshbach as HF
from ._core import _suite

cellular_hodge = _suite("universal cellular Hodge and tetrahedral algebra")
CITE = "UNIVERSAL_CELLULAR_HODGE_TETRAHEDRAL"


def example_cells():
    """The tetrahedron and n-gonal prisms for n=3,...,8."""
    return [CELL.TETRAHEDRON, *(CELL.prism(n) for n in range(3, 9))]


def cellular_data(cell):
    """Construct exact unweighted incidence operators for a supplied cell."""
    boundary = sp.Matrix(cell.boundary_matrix())
    kernel = CELL.integer_kernel(cell)
    if len(kernel) != 1:
        raise ValueError(f"{cell.name}: expected a one-dimensional cycle space")
    psi = sp.Matrix(kernel[0])
    norm = (psi.T * psi)[0]
    up = psi * psi.T
    down = boundary.T * boundary
    projection = up / norm
    complement = sp.eye(len(cell.faces)) - projection
    return boundary, psi, down, up, projection, complement


def verify_cellular_spectrum(cells):
    """Finite controls of the analytic cellular sphere-boundary statements."""
    results = {}
    for cell in cells:
        boundary, psi, down, up, projection, complement = cellular_data(cell)
        count = len(cell.faces)
        norm = (psi.T * psi)[0]
        zero = sp.zeros(count)
        assert norm == count
        assert down * psi == sp.zeros(count, 1)
        assert down * up == zero
        assert up * psi == count * psi
        assert projection * projection == projection
        assert complement * complement == complement
        assert up * complement == zero
        assert complement * up == zero
        diagonal = [int((down + up)[i, i]) for i in range(count)]
        perimeters = [len(face) for face in cell.faces]
        assert diagonal == [p + 1 for p in perimeters]
        results[cell.name] = {
            "n_faces": count,
            "n_edges": boundary.rows,
            "lambda": int(norm),
            "equal_perimeters": len(set(perimeters)) == 1,
            "diag": diagonal,
            "up_harmonic": True,
        }
    return results


def verify_tetrahedral_commutant():
    """Solve the full S4 commutant constraints, rather than assume their form."""
    _, _, down, up, projection, complement = cellular_data(CELL.TETRAHEDRON)
    assert down == 4 * complement
    assert up == 4 * projection
    assert down + up == 4 * sp.eye(4)
    entries = sp.symbols("x:16")
    unknown = sp.Matrix(4, 4, entries)
    equations = []
    for permutation in itertools.permutations(range(4)):
        action = sp.zeros(4)
        for i, j in enumerate(permutation):
            action[i, j] = 1
        assert action * projection == projection * action
        assert action * complement == complement * action
        equations.extend(unknown * action - action * unknown)
    coefficients, _ = sp.linear_eq_to_matrix(equations, entries)
    dimension = len(entries) - coefficients.rank()
    assert dimension == 2
    a, b = sp.symbols("a b")
    operator = a * projection + b * complement
    compressed = complement * operator * complement
    assert compressed == b * complement
    assert complement * operator * projection == sp.zeros(4)
    assert sp.simplify(compressed - sp.trace(compressed) * complement / 3) == sp.zeros(4)
    return {"commutant_dimension": dimension, "permutations": 24}


def tetrahedral_flux_returns():
    """Count unweighted boundary-flux paths; do not interpret them as quantum states."""
    boundary, psi, _, _, _, complement = cellular_data(CELL.TETRAHEDRON)
    columns = [tuple(boundary[:, i]) for i in range(4)]
    zero_flux = (0,) * boundary.rows
    count = flagged = all_faces_flagged = 0
    for word in itertools.product(itertools.product(range(4), (-1, 1)), repeat=4):
        flux = columns[0]
        prefixes = []
        for face, sign in word:
            flux = tuple(a + sign * b for a, b in zip(flux, columns[face], strict=True))
            prefixes.append(flux)
        if flux != columns[1]:
            continue
        count += 1
        flagged += any(p in (columns[0], columns[1], zero_flux) for p in prefixes[:-1])
        all_faces_flagged += any(p in (*columns, zero_flux) for p in prefixes[:-1])
    face0 = sp.eye(4)[:, 0]
    return {
        "total_paths": count,
        "endpoint_or_zero_prefixes": flagged,
        "other_paths": count - flagged,
        "any_positive_face_or_zero_prefixes": all_faces_flagged,
        "Q_psi": complement * psi,
        "Q_face0": complement * face0,
        "Q_face0_norm_squared": (face0.T * complement * face0)[0],
    }


def geometric_polynomial(m, q):
    """Polynomial Pi_m, defined at q=0 without division."""
    if m < 0:
        raise ValueError("m must be nonnegative")
    return sp.expand(sum((-4) ** j * (q - 4) ** (m - 1 - j) for j in range(m)))


def verify_master_symbols(max_m=4):
    """Check the actual Laurent operators and finite instances of the power formula."""
    identity, down, up, shifted, hopping = HF._ops()
    generators = {"S": shifted, "U": up, "R": hopping}
    psi = HF._psi()
    q, e2, e3 = HF._elementary()
    total = KO.bloch_matrix(KO.combine((1, down), (1, up)))
    square_up = KO.bloch_matrix(KO.compose(up, up))
    up_matrix = KO.bloch_matrix(up)
    for i in KO.PLANES:
        for j in KO.PLANES:
            assert total[i][j] == (q if i == j else {})
            assert square_up[i][j] == KO._mul(q, up_matrix[i][j])
    assert shifted == KO.combine((1, down), (-4, identity))
    rr = HF._sigma("RR", generators, identity, psi)
    rur = HF._sigma("RUR", generators, identity, psi)
    assert rr == KO._add(KO._mul(q, e2), HF._scale(e3, Fraction(3)))
    assert rur == HF._scale(KO._mul(e2, e2), Fraction(4))
    q_minus_four = HF._sub(q, {(0, 0, 0): Fraction(4)})
    power = {(0, 0, 0): Fraction(1)}
    pi = {}
    results = {}
    for m in range(max_m + 1):
        actual = HF._sigma("R" + "S" * m + "R", generators, identity, psi)
        expected = HF._sub(KO._mul(power, rr), KO._mul(pi, rur))
        assert actual == expected, f"master symbol failed at m={m}"
        results[m] = True
        pi = HF._sub(power, HF._scale(pi, Fraction(4)))
        power = KO._mul(power, q_minus_four)
    return results


@cellular_hodge.check(
    "universal cellular Hodge spectrum: lambda = |F| and excursions are up-harmonic",
    f"{CITE} Theorems 1 and 2; U7; G14",
)
def check_universal_hodge_spectrum():
    results = verify_cellular_spectrum(example_cells())
    return True, (
        "Exact incidence controls for tetrahedron and prisms n=3..8: "
        + ", ".join(f"{name}: lambda={row['lambda']}" for name, row in results.items())
        + ". L_up Q=0 as an operator identity; the general cellular claim has an analytic proof."
    )


@cellular_hodge.check(
    "total Laplacian diagonal equals face perimeter plus one",
    f"{CITE} Theorem 3; U7",
)
def check_total_laplacian_diagonal():
    results = verify_cellular_spectrum(example_cells())
    return True, (
        f"Verified (L_down+L_up)_ff=p_f+1 on {len(results)} cells. "
        "Equal perimeters, including nonregular triangulations, give a scalar diagonal. "
        "Among n-gonal prisms only n=4 has equal cap and side perimeters."
    )


@cellular_hodge.check(
    "tetrahedral Hodge duality and S_4 commutant theorem",
    f"{CITE} Theorems 4 and 5; U3; U7",
)
def check_tetrahedral_s4_commutant():
    result = verify_tetrahedral_commutant()
    return True, (
        f"All {result['permutations']} permutation constraints on 16 matrix entries give "
        f"commutant dimension {result['commutant_dimension']}. "
        "L_down=4Q, L_up=4P; an invariant face operator is aP+bQ, so QMP=0 and QMQ=bQ. "
        "This does not identify a physical effective Hamiltonian or its momentum dependence."
    )


@cellular_hodge.check(
    "FINDING: tetrahedral flux return counts do not identify the carrier projector",
    f"{CITE} Theorem 6 and physical-history obligation; U3; U7; ADR 0008",
)
def check_tetrahedral_flux_projection_boundary():
    result = tetrahedral_flux_returns()
    expected_face = sp.Matrix([3, -1, -1, -1]) / 4
    passed = (
        result["total_paths"] == 96
        and result["endpoint_or_zero_prefixes"] == 60
        and result["other_paths"] == 36
        and result["any_positive_face_or_zero_prefixes"] == 62
        and result["Q_psi"] == sp.zeros(4, 1)
        and result["Q_face0"] == expected_face
        and result["Q_face0_norm_squared"] == sp.Rational(3, 4)
    )
    return passed, (
        "96 additive flux paths split 60/36 under the endpoint-or-zero predicate; "
        "including all positive face boundaries flags 62. Q psi=0, but "
        "Q e0=(3,-1,-1,-1)/4 has norm squared 3/4. These counts do not calculate "
        "physical Haar/Fierz histories or justify their individual Q-annihilation."
    )


@cellular_hodge.check(
    "R S^m R Carrier Symbol Master Theorem: exact closed polynomial for m=0..4",
    f"{CITE} Theorem 7; G9; G14",
)
def check_r_sm_r_master_theorem():
    result = verify_master_symbols()
    q = sp.Symbol("q")
    pi4 = geometric_polynomial(4, q)
    assert pi4 == q**3 - 16 * q**2 + 96 * q - 256
    return all(result.values()), (
        "For S=L_down-4I, verified the Laurent premises and sigma(R S^m R)="
        "(q-4)^m(q e2+3e3)-4 Pi_m(q)e2^2 for m=0..4. "
        "Pi4=q^3-16q^2+96q-256. The polynomial recurrence proves the general "
        "operator formula; no sixth-order dynamical word coefficient is determined."
    )
