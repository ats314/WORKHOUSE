"""Exact original-link incidence and harmonic coarse-complement controls.

The matrix identities are finite exact controls. General-size coercivity,
quantization, and nonlinear/OS scope are proved or delimited in the companion
draft. No numerical eigensolver participates in acceptance.
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path

import sympy as s


def rectangle_complex(nx: int, ny: int):
    if nx < 1 or ny < 1:
        raise ValueError("Positive face dimensions are required")
    vertices = [(x, y) for y in range(ny + 1) for x in range(nx + 1)]
    edges = [((x, y), (x + 1, y)) for y in range(ny + 1) for x in range(nx)]
    edges += [((x, y), (x, y + 1)) for y in range(ny) for x in range(nx + 1)]
    vertex_index, edge_index = (
        {v: i for i, v in enumerate(vertices)},
        {e: i for i, e in enumerate(edges)},
    )
    faces = [(x, y) for y in range(ny) for x in range(nx)]
    gradient = s.zeros(len(edges), len(vertices))
    for i, (a, b) in enumerate(edges):
        gradient[i, vertex_index[a]], gradient[i, vertex_index[b]] = -1, 1
    curl = s.zeros(len(faces), len(edges))
    for i, (x, y) in enumerate(faces):
        for edge, sign in (
            (((x, y), (x + 1, y)), 1),
            (((x + 1, y), (x + 1, y + 1)), 1),
            (((x, y + 1), (x + 1, y + 1)), -1),
            (((x, y), (x, y + 1)), -1),
        ):
            curl[i, edge_index[edge]] = sign
    return vertices, edges, faces, gradient, curl


def face_dirichlet_matrix(nx: int, ny: int) -> s.Matrix:
    faces = [(x, y) for y in range(ny) for x in range(nx)]
    return s.Matrix(
        [
            [4 if a == b else -int(abs(a[0] - b[0]) + abs(a[1] - b[1]) == 1) for b in faces]
            for a in faces
        ]
    )


def incidence_controls() -> list[dict]:
    rows = []
    for nx, ny in ((1, 1), (2, 1), (4, 1), (2, 2), (3, 2), (4, 3)):
        vertices, edges, faces, gradient, curl = rectangle_complex(nx, ny)
        assert curl * gradient == s.zeros(len(faces), len(vertices))
        assert gradient.rank() == len(vertices) - 1
        assert curl.rank() == len(faces) == len(edges) - len(vertices) + 1
        k = curl * curl.T
        assert k == face_dirichlet_matrix(nx, ny)
        # Minimal Euclidean link lift has exactly the inverse face metric.
        lift = curl.T * k.inv()
        assert curl * lift == s.eye(len(faces))
        assert lift.T * lift == k.inv()
        if (nx, ny) == (2, 1):
            assert k.charpoly().as_expr() == s.Symbol("lambda") ** 2 - 8 * s.Symbol("lambda") + 15
        rows.append(
            {
                "faces": [nx, ny],
                "vertices": len(vertices),
                "edges": len(edges),
                "rank_curl": curl.rank(),
            }
        )
    return rows


def partition_matrices(nx: int, ny: int, side: int):
    if nx % side or ny % side:
        raise ValueError("The exact controls use equal square boxes")
    faces = [(x, y) for y in range(ny) for x in range(nx)]
    fi = {p: i for i, p in enumerate(faces)}
    boxes = [(x, y) for y in range(ny // side) for x in range(nx // side)]
    bi = {p: i for i, p in enumerate(boxes)}
    means = s.zeros(len(faces), len(boxes))
    neumann = s.zeros(len(faces))
    interface_vectors, boundary_vectors = [], []
    for face, i in fi.items():
        x, y = face
        box = (x // side, y // side)
        means[i, bi[box]] = s.Rational(1, side)
        for adjacent in ((x + 1, y), (x, y + 1)):
            if adjacent not in fi:
                continue
            vector = s.zeros(len(faces), 1)
            vector[i], vector[fi[adjacent]] = 1, -1
            if (adjacent[0] // side, adjacent[1] // side) == box:
                neumann += vector * vector.T
            else:
                interface_vectors.append(vector)
        missing = int(x == 0) + int(x == nx - 1) + int(y == 0) + int(y == ny - 1)
        for _ in range(missing):
            vector = s.zeros(len(faces), 1)
            vector[i] = 1
            boundary_vectors.append(vector)
    return means, neumann, interface_vectors, boundary_vectors


def gluing_controls() -> list[dict]:
    rows = []
    for nx, ny, side in ((4, 4, 2), (6, 4, 2), (6, 6, 3), (8, 4, 2)):
        means, neumann, interfaces, exterior = partition_matrices(nx, ny, side)
        k = face_dirichlet_matrix(nx, ny)
        assert means.T * means == s.eye(means.cols)
        assert neumann * means == s.zeros(k.rows, means.cols)
        assert k == neumann + sum((v * v.T for v in interfaces + exterior), s.zeros(k.rows))
        f = s.Rational(4, side * side)
        polynomial = k.charpoly().as_poly()
        assert polynomial.eval(f) != 0
        count = int(polynomial.count_roots(-s.oo, f))
        assert count <= means.cols
        rows.append(
            {
                "faces": [nx, ny],
                "box_side": side,
                "retained_dimension_bound": means.cols,
                "rational_fast_squared_frequency_floor": str(f),
                "exact_eigenvalue_count_below_floor": count,
                "retained_interface_squares": len(interfaces),
                "exterior_boundary_squares": len(exterior),
            }
        )
    return rows


def local_poincare_certificates() -> list[dict]:
    rows = []
    for side in (2, 3, 4):
        means, neumann, interfaces, exterior = partition_matrices(side, side, side)
        assert not interfaces
        q = s.eye(side * side) - means * means.T
        f = s.Rational(4, side * side)
        matrix = neumann - f * q
        lower, d = matrix.LDLdecomposition(hermitian=False)
        assert lower * d * lower.T == matrix
        assert all(value >= 0 for value in d.diagonal())
        assert matrix * means == s.zeros(side * side, 1)
        rows.append(
            {
                "box_side": side,
                "floor": str(f),
                "exact_LDL_diagonal": [str(x) for x in d.diagonal()],
            }
        )
    return rows


def low_mode_source_control() -> dict:
    k = face_dirichlet_matrix(4, 4)
    means, _, _, _ = partition_matrices(4, 4, 2)
    golden = (1 + s.sqrt(5)) / 2
    path_mode = s.Matrix([1, golden, golden, 1])
    mode = s.kronecker_product(path_mode, path_mode)
    eigenvalue = 3 - s.sqrt(5)
    assert (k * mode - eigenvalue * mode).applyfunc(s.simplify) == s.zeros(16, 1)
    ratio = s.simplify((mode.T * means * means.T * mode)[0] / mode.dot(mode))
    assert s.simplify(ratio - (9 + 4 * s.sqrt(5)) / 20) == 0
    exact_local_floor = s.Integer(2)
    lower = 1 - eigenvalue / exact_local_floor
    assert s.simplify(ratio - lower).is_positive is True
    # For a literal linear face coordinate the squared vacuum-source factor is sqrt(lambda)/2.
    face_source_frame = s.simplify(s.sqrt(eigenvalue) * ratio / 2)
    assert s.simplify(face_source_frame - s.sqrt(eigenvalue) * lower / 2).is_positive is True
    # Incorrect replacement by a Neumann outer boundary creates a zero mode.
    _, neumann_whole, _, _ = partition_matrices(4, 4, 4)
    assert neumann_whole * s.ones(16, 1) == s.zeros(16, 1)
    assert k * s.ones(16, 1) != s.zeros(16, 1)
    return {
        "lowest_squared_frequency": str(eigenvalue),
        "box_mean_frame_factor": str(ratio),
        "analytic_frame_lower": str(lower),
        "literal_face_source_frame_factor": str(face_source_frame),
        "wrong_outer_boundary_zero_mode_negative_control": True,
        "source_scope": (
            "Color-adjoint harmonic linear sources; "
            "physical singlets require centered quadratic pairs"
        ),
    }


def exact_controls() -> dict:
    return {
        "scope": __doc__,
        "original_link_incidence": incidence_controls(),
        "retained_boundary_gluing": gluing_controls(),
        "local_rational_Poincare_LDL": local_poincare_certificates(),
        "spectral_frame_and_source_coordinates": low_mode_source_control(),
        "source_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    }


if __name__ == "__main__":
    if not __debug__:
        raise RuntimeError("Exact controls require assertions enabled")
    result = exact_controls()
    with Path(__file__).with_suffix(".json").open("x", encoding="utf-8", newline="\n") as handle:
        json.dump(result, handle, indent=2)
        handle.write("\n")
    print(json.dumps(result, indent=2))
