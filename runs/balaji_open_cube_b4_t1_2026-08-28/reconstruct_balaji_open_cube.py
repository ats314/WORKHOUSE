#!/usr/bin/env python3
"""Reconstruct and test the Balaji et al. B=4 open-cube Hamiltonian.

This is an author-data-derived reconstruction, not a claim that the authors'
private global ED matrix was recovered.  It embeds the public ymcirc d=3,
B=4 plaquette master table on the six faces of one open cube, with absent
boundary control links fixed to the trivial SU(3) irrep.

The dimensionless Hamiltonian used here is

    K(u) = H/g^2 = (1/2) sum_links C2(R_l) - u sum_faces(Box+Box^dagger),
    u = g^-4,

with the extensive magnetic constant omitted, as in the paper's strong-
coupling discussion.
"""

from __future__ import annotations

import argparse
import ast
import gzip
import hashlib
import itertools
import json
from collections import defaultdict
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable

import numpy as np


ONE = (0, 0, 0)
THREE = (1, 0, 0)
THREE_BAR = (1, 1, 0)
IWEIGHTS = (ONE, THREE, THREE_BAR)
CONJ = (0, 2, 1)
FORDER = (1, 2, 3, -1, -2, -3)
FULL_SIGNATURE = ((1, 2, 3, -1, -2, -3),) * 4
EXPECTED_SOURCE_SHA256 = "4cad9538681c10e88270ef60045fb91b7f2de22b42f97621812667b492ba9a1a"
EXPECTED_SOURCE_BLOB = "1808849c74b36f8082e7030d074681be4bb8c0fd"
EXPECTED_DEVELOP_COMMIT = "e9e190bfda405608de9cab71c0df0161cfcb1a10"


@dataclass(frozen=True)
class Face:
    plane: tuple[int, int]  # zero-indexed coordinate axes
    fixed_axis: int
    fixed_value: int
    vertices: tuple[tuple[int, int, int], ...]
    active_edges: tuple[int, int, int, int]
    control_dirs: tuple[tuple[int, ...], ...]
    physical_control_positions: tuple[int, int, int, int]

    @property
    def author_plane(self) -> tuple[int, int]:
        return (self.plane[0] + 1, self.plane[1] + 1)

    @property
    def label(self) -> str:
        names = "xyz"
        return f"{names[self.plane[0]]}{names[self.plane[1]]}@{names[self.fixed_axis]}={self.fixed_value}"


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def canonical_edges() -> tuple[tuple[tuple[int, int, int], int], ...]:
    edges = []
    for axis in range(3):
        for vertex in itertools.product((0, 1), repeat=3):
            if vertex[axis] == 0:
                edges.append((tuple(vertex), axis))
    return tuple(edges)


EDGES = canonical_edges()
EDGE_INDEX = {edge: idx for idx, edge in enumerate(EDGES)}


def edge_index_from_half_link(vertex: tuple[int, int, int], signed_dir: int) -> int:
    axis = abs(signed_dir) - 1
    base = list(vertex)
    if signed_dir < 0:
        base[axis] -= 1
    key = (tuple(base), axis)
    if key not in EDGE_INDEX:
        raise KeyError(f"half-link {vertex}, {signed_dir} lies outside the open cube")
    return EDGE_INDEX[key]


def make_faces() -> tuple[Face, ...]:
    faces = []
    for a, b in ((0, 1), (0, 2), (1, 2)):
        c = ({0, 1, 2} - {a, b}).pop()
        for fixed in (0, 1):
            v1 = [0, 0, 0]
            v1[c] = fixed
            v2 = v1.copy()
            v2[a] = 1
            v3 = v2.copy()
            v3[b] = 1
            v4 = v1.copy()
            v4[b] = 1
            vertices = tuple(map(tuple, (v1, v2, v3, v4)))
            active = (
                edge_index_from_half_link(vertices[0], a + 1),
                edge_index_from_half_link(vertices[1], b + 1),
                edge_index_from_half_link(vertices[2], -(a + 1)),
                edge_index_from_half_link(vertices[3], -(b + 1)),
            )
            active_dirs = (
                {a + 1, b + 1},
                {-(a + 1), b + 1},
                {-(a + 1), -(b + 1)},
                {a + 1, -(b + 1)},
            )
            control_dirs = tuple(
                tuple(direction for direction in FORDER if direction not in active_at_vertex)
                for active_at_vertex in active_dirs
            )
            physical_direction = (c + 1) if fixed == 0 else -(c + 1)
            physical_positions = tuple(directions.index(physical_direction) for directions in control_dirs)
            faces.append(
                Face(
                    plane=(a, b),
                    fixed_axis=c,
                    fixed_value=fixed,
                    vertices=vertices,
                    active_edges=active,
                    control_dirs=control_dirs,
                    physical_control_positions=physical_positions,
                )
            )
    return tuple(faces)


FACES = make_faces()


def is_vertex_singlet(state: tuple[int, ...], vertex: tuple[int, int, int]) -> bool:
    half_reps = []
    for axis in range(3):
        signed_dir = axis + 1 if vertex[axis] == 0 else -(axis + 1)
        stored_rep = state[edge_index_from_half_link(vertex, signed_dir)]
        half_reps.append(stored_rep if signed_dir > 0 else CONJ[stored_rep])
    counts = tuple(sorted(half_reps))
    return counts in ((0, 0, 0), (0, 1, 2), (1, 1, 1), (2, 2, 2))


def enumerate_physical_states() -> tuple[tuple[int, ...], ...]:
    vertices = tuple(itertools.product((0, 1), repeat=3))
    return tuple(
        state
        for state in itertools.product(range(3), repeat=len(EDGES))
        if all(is_vertex_singlet(state, tuple(vertex)) for vertex in vertices)
    )


def padded_local_state(state: tuple[int, ...], face: Face) -> tuple:
    active = tuple(IWEIGHTS[state[idx]] for idx in face.active_edges)
    controls = []
    physical_direction = (face.fixed_axis + 1) if face.fixed_value == 0 else -(face.fixed_axis + 1)
    for vertex, directions, physical_position in zip(
        face.vertices, face.control_dirs, face.physical_control_positions
    ):
        values = [ONE] * 4
        control_edge = edge_index_from_half_link(vertex, physical_direction)
        values[physical_position] = IWEIGHTS[state[control_edge]]
        if directions[physical_position] != physical_direction:
            raise AssertionError("physical control direction was placed incorrectly")
        controls.append(tuple(values))
    return ((0, 0, 0, 0), active, tuple(controls))


def apply_local_final(
    state: tuple[int, ...], face: Face, local_initial: tuple, local_final: tuple
) -> tuple[int, ...]:
    if local_final[0] != (0, 0, 0, 0):
        raise AssertionError(f"unexpected nonzero vertex multiplicity: {local_final[0]}")
    if local_final[2] != local_initial[2]:
        raise AssertionError("a plaquette transition changed a control link")
    new_state = list(state)
    inverse = {iweight: label for label, iweight in enumerate(IWEIGHTS)}
    for edge, iweight in zip(face.active_edges, local_final[1]):
        if iweight not in inverse:
            raise AssertionError(f"B=4 open-cube transition escaped T1: {iweight}")
        new_state[edge] = inverse[iweight]
    return tuple(new_state)


def load_author_box_table(path: Path) -> tuple[dict, dict[tuple, list[tuple[tuple, dict]]]]:
    with gzip.open(path, "rt", encoding="utf-8") as handle:
        raw = json.load(handle)
    outgoing: dict[tuple, list[tuple[tuple, dict]]] = defaultdict(list)
    for encoded_pair, values in raw["data"].items():
        final_state, initial_state = ast.literal_eval(encoded_pair)
        outgoing[initial_state].append((final_state, values))
    return raw["metadata"], outgoing


def author_coefficient(values: dict, face: Face) -> float | None:
    plane_values = values.get(str(face.author_plane))
    if plane_values is None:
        return None
    value = plane_values.get(str(FULL_SIGNATURE))
    return None if value is None else float(value)


def build_box_matrix(
    states: tuple[tuple[int, ...], ...], outgoing: dict[tuple, list[tuple[tuple, dict]]]
) -> tuple[np.ndarray, np.ndarray, dict]:
    state_index = {state: idx for idx, state in enumerate(states)}
    box = np.zeros((len(states), len(states)), dtype=np.float64)
    diagnostics = {
        "face_transition_counts": {},
        "face_nonzero_counts": {},
        "missing_initial_local_states": 0,
        "escaped_physical_states": 0,
    }
    face_matrices = []
    for face in FACES:
        face_box = np.zeros_like(box)
        transition_count = 0
        nonzero_count = 0
        for column, state in enumerate(states):
            local_initial = padded_local_state(state, face)
            candidates = outgoing.get(local_initial)
            if candidates is None:
                diagnostics["missing_initial_local_states"] += 1
                continue
            for local_final, values in candidates:
                coefficient = author_coefficient(values, face)
                if coefficient is None:
                    continue
                transition_count += 1
                if coefficient == 0.0:
                    continue
                final_state = apply_local_final(state, face, local_initial, local_final)
                row = state_index.get(final_state)
                if row is None:
                    diagnostics["escaped_physical_states"] += 1
                    continue
                box[row, column] += coefficient
                face_box[row, column] += coefficient
                nonzero_count += 1
        diagnostics["face_transition_counts"][face.label] = transition_count
        diagnostics["face_nonzero_counts"][face.label] = nonzero_count
        face_matrices.append(face_box)
    return box, np.stack(face_matrices), diagnostics


def charge_matrix(states: tuple[tuple[int, ...], ...]) -> tuple[np.ndarray, np.ndarray]:
    state_index = {state: idx for idx, state in enumerate(states)}
    permutation = np.array(
        [state_index[tuple(CONJ[label] for label in state)] for state in states], dtype=np.int64
    )
    matrix = np.zeros((len(states), len(states)), dtype=np.float64)
    matrix[permutation, np.arange(len(states))] = 1.0
    return matrix, permutation


def odd_basis(permutation: np.ndarray) -> np.ndarray:
    columns = []
    visited = set()
    n = len(permutation)
    for idx in range(n):
        if idx in visited:
            continue
        partner = int(permutation[idx])
        visited.add(idx)
        visited.add(partner)
        if partner == idx:
            continue
        vector = np.zeros(n, dtype=np.float64)
        representative, conjugate = sorted((idx, partner))
        vector[representative] = 1.0 / np.sqrt(2.0)
        vector[conjugate] = -1.0 / np.sqrt(2.0)
        columns.append(vector)
    return np.column_stack(columns)


def single_face_odd_basis(
    states: tuple[tuple[int, ...], ...], box: np.ndarray, permutation: np.ndarray
) -> tuple[np.ndarray, list[dict]]:
    state_index = {state: idx for idx, state in enumerate(states)}
    vacuum_state = (0,) * len(EDGES)
    vacuum = state_index[vacuum_state]
    columns = []
    records = []
    for face in FACES:
        local_initial = padded_local_state(vacuum_state, face)
        # Use geometry rather than a matrix-column ambiguity: oriented Box on
        # vacuum is (3,3,bar3,bar3) on the CCW active links.
        oriented = list(vacuum_state)
        for edge, label in zip(face.active_edges, (1, 1, 2, 2)):
            oriented[edge] = label
        oriented = tuple(oriented)
        i = state_index[oriented]
        j = int(permutation[i])
        if abs(box[i, vacuum] - 1.0) > 1e-12 or abs(box.T[j, vacuum] - 1.0) > 1e-12:
            raise AssertionError(
                f"vacuum-to-loop normalization failed on {face.label}: "
                f"Box={box[i, vacuum]}, Boxdag={box.T[j, vacuum]}, local={local_initial}"
            )
        vector = np.zeros(len(states), dtype=np.float64)
        vector[i] = 1.0 / np.sqrt(2.0)
        vector[j] = -1.0 / np.sqrt(2.0)
        columns.append(vector)
        records.append(
            {
                "face": face.label,
                "oriented_state_index": i,
                "conjugate_state_index": j,
            }
        )
    return np.column_stack(columns), records


def group_eigenvalues(values: Iterable[float], tolerance: float = 2e-9) -> list[dict]:
    groups: list[list[float]] = []
    for value in sorted(float(x) for x in values):
        if not groups or abs(value - np.mean(groups[-1])) > tolerance:
            groups.append([value])
        else:
            groups[-1].append(value)
    return [
        {
            "value": float(np.mean(group)),
            "multiplicity": len(group),
            "spread": float(max(group) - min(group)),
        }
        for group in groups
    ]


def cubical_face_gram() -> np.ndarray:
    """Unsigned-invariant spectrum check from an oriented edge-face boundary."""
    boundary = np.zeros((len(EDGES), len(FACES)), dtype=np.int64)
    for face_idx, face in enumerate(FACES):
        # The active path is +a,+b,-a,-b.  The canonical stored edges for l3
        # and l4 point opposite to the path.
        for edge, sign in zip(face.active_edges, (1, 1, -1, -1)):
            boundary[edge, face_idx] = sign
    return boundary.T @ boundary


def perturbative_certificate(
    electric: np.ndarray,
    magnetic: np.ndarray,
    face_odd: np.ndarray,
    vacuum_index: int,
    face_gram: np.ndarray,
) -> dict:
    perturbation = -magnetic
    e0 = 8.0 / 3.0
    first_order = face_odd.T @ perturbation @ face_odd
    denominators = np.zeros_like(electric)
    mask = np.abs(electric - e0) > 1e-12
    denominators[mask] = 1.0 / (e0 - electric[mask])
    coupled = perturbation @ face_odd
    shell_second = coupled.T @ (denominators[:, None] * coupled)

    vacuum_coupled = perturbation[:, vacuum_index]
    vacuum_mask = np.abs(electric) > 1e-12
    vacuum_second = float(
        np.sum((vacuum_coupled[vacuum_mask] ** 2) / (0.0 - electric[vacuum_mask]))
    )
    gap_second = shell_second - vacuum_second * np.eye(face_odd.shape[1])
    eigenvalues = np.linalg.eigvalsh(gap_second)
    expected = np.array([31 / 12, 31 / 12, 11 / 4, 11 / 4, 11 / 4, 37 / 12])
    expected_matrix = (37.0 / 12.0) * np.eye(6) - face_gram / 12.0
    return {
        "first_order_matrix": first_order.tolist(),
        "first_order_identity_max_error": float(np.max(np.abs(first_order - np.eye(6)))),
        "vacuum_second_order": vacuum_second,
        "shell_raw_second_order_matrix": shell_second.tolist(),
        "gap_second_order_matrix": gap_second.tolist(),
        "gap_second_order_eigenvalues": eigenvalues.tolist(),
        "gap_second_order_groups": group_eigenvalues(eigenvalues),
        "predicted_matrix": expected_matrix.tolist(),
        "predicted_matrix_max_error": float(np.max(np.abs(gap_second - expected_matrix))),
        "expected_sorted": expected.tolist(),
        "expected_max_error": float(np.max(np.abs(eigenvalues - expected))),
    }


def finite_u_certificate(
    electric: np.ndarray,
    magnetic: np.ndarray,
    charge_odd: np.ndarray,
    face_odd: np.ndarray,
    u_values: tuple[float, ...],
) -> list[dict]:
    electric_odd = charge_odd.T @ (electric[:, None] * charge_odd)
    magnetic_odd = charge_odd.T @ magnetic @ charge_odd
    shell_in_odd = charge_odd.T @ face_odd
    records = []
    for u in u_values:
        full_hamiltonian = np.diag(electric) - u * magnetic
        ground = float(np.linalg.eigvalsh(full_hamiltonian)[0])
        odd_hamiltonian = electric_odd - u * magnetic_odd
        eigenvalues, eigenvectors = np.linalg.eigh(odd_hamiltonian)
        overlaps = np.sum((shell_in_odd.T @ eigenvectors) ** 2, axis=0)
        candidates = np.argsort(overlaps)[-6:]
        candidates = candidates[np.argsort(eigenvalues[candidates])]
        shell_energies = eigenvalues[candidates]
        shell_overlaps = overlaps[candidates]
        gap_coefficients = (shell_energies - ground - (8.0 / 3.0) - u) / (u * u)
        records.append(
            {
                "u": u,
                "g": u ** (-0.25),
                "ground_energy": ground,
                "shell_energies": shell_energies.tolist(),
                "shell_overlaps": shell_overlaps.tolist(),
                "gap_u2_coefficient_estimates": gap_coefficients.tolist(),
                "gap_u2_groups": group_eigenvalues(gap_coefficients, tolerance=max(2e-9, 5 * u)),
            }
        )
    return records


def published_curve_certificate(
    figure_pdf: Path,
    electric: np.ndarray,
    magnetic: np.ndarray,
) -> dict:
    """Compare against the vector path labeled ``exact`` in the paper figure.

    The source Matplotlib PDF retains the 61-point black curve as vector data.
    Axis tick positions determine the affine PDF-coordinate-to-data map, so no
    raster digitization or hand-entered energy values are involved.
    """
    try:
        import pdfplumber
    except ImportError as exc:  # pragma: no cover - depends on local artifact runtime
        return {"status": "SKIP", "reason": f"pdfplumber unavailable: {exc}"}

    if not figure_pdf.is_file():
        return {"status": "SKIP", "reason": f"figure PDF not found: {figure_pdf}"}
    with pdfplumber.open(figure_pdf) as document:
        if len(document.pages) != 1:
            raise AssertionError(f"expected a one-page figure PDF, found {len(document.pages)}")
        page = document.pages[0]
        exact_candidates = [
            curve
            for curve in page.curves
            if curve.get("stroking_color") in (0, 0.0)
            and curve.get("dash") is None
            and abs(float(curve.get("linewidth", 0.0)) - 1.5) < 1e-12
            and float(curve.get("width", 0.0)) > 300
            and len(curve.get("pts", ())) > 20
        ]
        if len(exact_candidates) != 1:
            raise AssertionError(f"could not uniquely identify the exact vector curve: {len(exact_candidates)}")
        points = exact_candidates[0]["pts"]

        x_ticks = sorted(
            float(line["x0"])
            for line in page.lines
            if abs(float(line["x0"]) - float(line["x1"])) < 1e-12
            and 3.4 < abs(float(line["bottom"]) - float(line["top"])) < 3.6
        )
        y_ticks = sorted(
            float(line["top"])
            for line in page.lines
            if abs(float(line["top"]) - float(line["bottom"])) < 1e-12
            and 3.4 < abs(float(line["x1"]) - float(line["x0"])) < 3.6
        )
        if len(x_ticks) != 7 or len(y_ticks) != 8:
            raise AssertionError(f"unexpected tick census: x={len(x_ticks)}, y={len(y_ticks)}")

    # Figure 8 uses x ticks 0.8,...,2.0 and y ticks 0,-1,...,-7.
    x0, x1 = x_ticks[0], x_ticks[-1]
    y_top, y_bottom = y_ticks[0], y_ticks[-1]
    g_values = np.array([0.8 + (float(x) - x0) * (2.0 - 0.8) / (x1 - x0) for x, _ in points])
    published_energies = np.array(
        [(y_top - float(y)) * 7.0 / (y_bottom - y_top) for _, y in points]
    )
    reconstructed_energies = np.array(
        [
            float(np.linalg.eigvalsh(np.diag(electric) - magnetic / (g**4))[0] * g * g)
            for g in g_values
        ]
    )
    residuals = reconstructed_energies - published_energies
    max_abs = float(np.max(np.abs(residuals)))
    result = {
        "status": "PASS" if max_abs < 2e-6 else "FAIL",
        "source_pdf": str(figure_pdf.resolve()),
        "source_pdf_sha256": sha256_file(figure_pdf.resolve()),
        "method": "direct extraction of the 61-point black exact vector path and vector axis ticks",
        "point_count": len(points),
        "g_min": float(np.min(g_values)),
        "g_max": float(np.max(g_values)),
        "max_absolute_energy_error": max_abs,
        "rms_energy_error": float(np.sqrt(np.mean(residuals**2))),
        "samples": [
            {
                "g": float(g_values[index]),
                "published_vector_energy": float(published_energies[index]),
                "reconstructed_energy": float(reconstructed_energies[index]),
                "residual": float(residuals[index]),
            }
            for index in range(0, len(points), 10)
        ],
    }
    if result["status"] != "PASS":
        raise AssertionError(f"published exact-curve validation failed: {result}")
    return result


def parse_args() -> argparse.Namespace:
    default_source = Path(
        ".scratch/literature/ymcirc-feature-obc/ymcirc-feature-OBC-mixed-BC/"
        "ymcirc/_ymcirc_data/magnetic-hamiltonian-box-term-matrix-elements/"
        "B4_dim(3)_PBC_magnetic_hamiltonian.json.gz"
    )
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source", type=Path, default=default_source)
    parser.add_argument(
        "--matrix-output", type=Path, default=Path("balaji_open_cube_B4_T1_hamiltonian.npz")
    )
    parser.add_argument(
        "--certificate-output", type=Path, default=Path("balaji_open_cube_B4_T1_certificate.json")
    )
    parser.add_argument(
        "--figure-pdf",
        type=Path,
        default=Path(".scratch/literature/2509.25865v3/images/cube_VQE_Energies.pdf"),
        help="paper's vector Figure 8 PDF; validation is skipped if absent",
    )
    parser.add_argument(
        "--u-values", default="0.02,0.01,0.005,0.0025", help="comma-separated positive u values"
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    source = args.source.resolve()
    if not source.is_file():
        raise FileNotFoundError(source)
    source_sha = sha256_file(source)
    if source_sha != EXPECTED_SOURCE_SHA256:
        raise RuntimeError(
            f"source SHA-256 mismatch: expected {EXPECTED_SOURCE_SHA256}, observed {source_sha}"
        )

    metadata, outgoing = load_author_box_table(source)
    expected_metadata = {
        "dim": "d=3",
        "truncation_mode": "B",
        "cutoff": 4,
        "PBCs": [True, True, True],
        "f_order": [1, 2, 3, -1, -2, -3],
    }
    for key, expected_value in expected_metadata.items():
        if metadata.get(key) != expected_value:
            raise RuntimeError(
                f"source metadata mismatch for {key}: expected {expected_value}, got {metadata.get(key)}"
            )

    states = enumerate_physical_states()
    if len(states) != 243:
        raise AssertionError(f"expected 243 gauge-invariant T1 cube states, found {len(states)}")
    state_index = {state: idx for idx, state in enumerate(states)}
    vacuum_index = state_index[(0,) * len(EDGES)]

    box, face_boxes, build_diagnostics = build_box_matrix(states, outgoing)
    if build_diagnostics["missing_initial_local_states"] != 0:
        raise AssertionError(build_diagnostics)
    if build_diagnostics["escaped_physical_states"] != 0:
        raise AssertionError(build_diagnostics)
    magnetic = box + box.T
    electric = np.array(
        [(2.0 / 3.0) * sum(label != 0 for label in state) for state in states], dtype=np.float64
    )

    charge, charge_permutation = charge_matrix(states)
    charge_commutator = float(np.max(np.abs(charge @ magnetic - magnetic @ charge)))
    if charge_commutator > 2e-12:
        raise AssertionError(f"naive charge conjugation does not commute: {charge_commutator}")
    charge_odd = odd_basis(charge_permutation)
    if charge_odd.shape != (243, 121):
        raise AssertionError(f"unexpected C- block dimension: {charge_odd.shape}")

    face_odd, face_records = single_face_odd_basis(states, box, charge_permutation)
    if np.max(np.abs(face_odd.T @ face_odd - np.eye(6))) > 2e-12:
        raise AssertionError("single-face odd states are not orthonormal")
    if np.max(np.abs(charge @ face_odd + face_odd)) > 2e-12:
        raise AssertionError("single-face states are not charge odd")

    gram = cubical_face_gram()
    gram_eigenvalues = np.linalg.eigvalsh(gram.astype(float))
    perturbative = perturbative_certificate(electric, magnetic, face_odd, vacuum_index, gram)
    if perturbative["first_order_identity_max_error"] > 2e-12:
        raise AssertionError("the C- shell does not have the expected common +u term")
    if perturbative["expected_max_error"] > 2e-10:
        raise AssertionError(
            "author-data second-order spectrum disagrees with the predicted T1 shell: "
            f"{perturbative['gap_second_order_eigenvalues']}"
        )
    if perturbative["predicted_matrix_max_error"] > 2e-10:
        raise AssertionError(
            "the full author-data Schur complement is not 37/12 I - G/12: "
            f"max error {perturbative['predicted_matrix_max_error']}"
        )

    u_values = tuple(float(value) for value in args.u_values.split(","))
    if not u_values or any(value <= 0 for value in u_values):
        raise ValueError("all u values must be positive")
    finite_u = finite_u_certificate(electric, magnetic, charge_odd, face_odd, u_values)
    curve_validation = published_curve_certificate(args.figure_pdf.resolve(), electric, magnetic)

    args.matrix_output.parent.mkdir(parents=True, exist_ok=True)
    np.savez_compressed(
        args.matrix_output,
        basis=np.asarray(states, dtype=np.int8),
        edges=np.asarray([[*vertex, axis] for vertex, axis in EDGES], dtype=np.int8),
        faces=np.asarray(
            [[*face.plane, face.fixed_axis, face.fixed_value] for face in FACES], dtype=np.int8
        ),
        electric_diagonal=electric,
        oriented_box_by_face=face_boxes,
        oriented_box=box,
        magnetic_box_plus_dagger=magnetic,
        charge_conjugation=charge,
        charge_permutation=charge_permutation,
        charge_odd_basis=charge_odd,
        single_face_charge_odd_basis=face_odd,
        second_order_gap_matrix=np.asarray(perturbative["gap_second_order_matrix"]),
        cubical_face_gram=gram,
    )
    matrix_sha = sha256_file(args.matrix_output.resolve())

    certificate = {
        "schema": "balaji-open-cube-b4-t1-author-data-reconstruction-v1",
        "status": "PASS",
        "provenance_boundary": (
            "The local plaquette coefficients are the authors' public ymcirc data. "
            "The 243-state open-cube assembly and spectral projection are an independent reconstruction; "
            "the authors' original global ED matrix was not published or recovered."
        ),
        "source": {
            "repository": "https://github.com/hepqis-uiuc/ymcirc",
            "develop_commit_observed": EXPECTED_DEVELOP_COMMIT,
            "git_blob": EXPECTED_SOURCE_BLOB,
            "path": str(source),
            "sha256": source_sha,
            "metadata": metadata,
            "raw_oriented_box_entries": sum(len(values) for values in outgoing.values()),
        },
        "convention": {
            "hamiltonian": "K(u)=H/g^2=(1/2)sum_l C2(R_l)-u sum_p(Box_p+Box_p^dagger)",
            "u": "g^-4",
            "magnetic_constant": "omitted",
            "single_face_electric_energy": 8.0 / 3.0,
        },
        "cube": {
            "vertices": 8,
            "edges": len(EDGES),
            "faces": len(FACES),
            "physical_basis_dimension": len(states),
            "charge_odd_dimension": charge_odd.shape[1],
            "face_labels": [face.label for face in FACES],
            "single_face_records": face_records,
            "box_nnz": int(np.count_nonzero(box)),
            "magnetic_nnz": int(np.count_nonzero(magnetic)),
            "charge_commutator_max_abs": charge_commutator,
            "build_diagnostics": build_diagnostics,
        },
        "independent_topology_check": {
            "face_gram_matrix": gram.tolist(),
            "face_gram_eigenvalues": gram_eigenvalues.tolist(),
            "face_gram_groups": group_eigenvalues(gram_eigenvalues),
        },
        "perturbative_result": perturbative,
        "finite_u_diagonalization": finite_u,
        "published_exact_curve_validation": curve_validation,
        "matrix_artifact": {
            "path": str(args.matrix_output.resolve()),
            "sha256": matrix_sha,
            "format": "NumPy NPZ; K(u)=diag(electric_diagonal)-u*magnetic_box_plus_dagger",
        },
        "acceptance_statement": (
            "The author-data-derived B=4=T1 open-cube Hamiltonian has a six-state C- shell "
            "whose second-order gap coefficients are 37/12 (1), 11/4 (3), and 31/12 (2). "
            "Relative to the G=0 signed-boundary singlet this is 0 (1), -1/3 (3), -1/2 (2), "
            "confirming the predicted 1+3+2 multiplicities and the T1 reversed kinetic ordering."
        ),
    }
    args.certificate_output.parent.mkdir(parents=True, exist_ok=True)
    args.certificate_output.write_text(json.dumps(certificate, indent=2) + "\n", encoding="utf-8")
    certificate_sha = sha256_file(args.certificate_output.resolve())

    print("PASS: author-data-derived Balaji B=4=T1 open-cube reconstruction")
    print(f"physical basis: {len(states)}; C- block: {charge_odd.shape[1]}")
    print(f"Box nnz: {np.count_nonzero(box)}; Box+Box^dagger nnz: {np.count_nonzero(magnetic)}")
    print("C- gap O(u^2) groups:")
    for group in perturbative["gap_second_order_groups"]:
        print(f"  {group['value']:.15g}  multiplicity {group['multiplicity']}")
    if curve_validation["status"] == "PASS":
        print(
            "published 61-point exact curve: PASS; "
            f"max |delta E|={curve_validation['max_absolute_energy_error']:.3e}"
        )
    else:
        print(f"published exact curve: {curve_validation['status']} ({curve_validation['reason']})")
    print(f"matrix: {args.matrix_output.resolve()}  sha256={matrix_sha}")
    print(f"certificate: {args.certificate_output.resolve()}  sha256={certificate_sha}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
