#!/usr/bin/env python3
"""
ENGINE_SHELL6_o2_symmetry_reduced_v2.py

Exact connected O(u^2) degenerate perturbation theory for the complete
44-state shell-six SU(3) Wilson-loop space.

This is a symmetry-reduced driver for ENGINE_SHELL6_o2_full_intermediate_v1.py.

Key reduction:
    the 44 oriented shell-six loops form three O_h orbits of sizes 12, 24, 8.
Only one exact trace-word-resolvent column is computed per orbit. All remaining
columns are reconstructed by exact covariance.

Hamiltonian convention:
    H = H0 - u W,  u = beta_lat/6 = 1/g^4.

The underlying full-intermediate engine keeps complete trace products through
the resolvent. It does not project first-hop states prematurely to simple
Wilson loops.

Outputs:
  * representative-column checkpoint;
  * reconstructed exact 44x44 H1 and connected H2 matrices;
  * O_h x C channel analysis;
  * exact covariance and stabilizer certificate.

Disconnected vacuum bubbles and common shell self-energy shifts are omitted.
They cannot affect channel ordering.
"""
from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import sys
import time
from fractions import Fraction as F
from pathlib import Path


HERE = Path(__file__).resolve().parent
ENGINE_PATH = HERE / "shell6_o2_full_intermediate_v2.py"

if not ENGINE_PATH.exists():
    raise FileNotFoundError(
        f"Required symmetry-cached full-intermediate engine is missing: {ENGINE_PATH}"
    )

spec = importlib.util.spec_from_file_location("shell6_full_v1", ENGINE_PATH)
engine = importlib.util.module_from_spec(spec)
assert spec.loader is not None
spec.loader.exec_module(engine)


VERSION = "2026-06-14-shell6-symmetry-reduced-v2"


def gate(name: str, condition: bool, detail: str = "") -> None:
    status = "PASS" if condition else "FAIL"
    print(f"{status:4s} {name} {detail}", flush=True)
    if not condition:
        raise RuntimeError(f"{name}: {detail}")


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1 << 20), b""):
            h.update(block)
    return h.hexdigest()


def fraction_vector_to_strings(vector):
    return [str(value) for value in vector]


def strings_to_fraction_vector(vector):
    return [F(value) for value in vector]


def shell_basis():
    shapes = engine.shapes6()
    gate("complete shell-six basis size", len(shapes) == 44, str(len(shapes)))

    words = []
    edge_index = {}
    for index, shape in enumerate(shapes):
        word, endpoint = engine.steps_to_word((0, 0, 0), shape)
        gate(f"shape {index} closes", endpoint == (0, 0, 0))
        words.append(word)

        key = engine.canonical_edges_translation(engine.word_to_edges(word))
        gate(f"shape {index} unique", key not in edge_index)
        edge_index[key] = index

    return shapes, words, edge_index


def group_permutations(shapes):
    group = engine.signed_permutation_group()
    index = {shape: i for i, shape in enumerate(shapes)}

    permutations = []
    for matrix in group:
        permutation = tuple(
            index[engine.transform_shape(shape, matrix)] for shape in shapes
        )
        gate(
            "O_h action is a permutation",
            sorted(permutation) == list(range(len(shapes))),
        )
        permutations.append(permutation)

    gate("O_h order", len(permutations) == 48, str(len(permutations)))
    return group, permutations


def orbit_data(shapes, permutations):
    remaining = set(range(len(shapes)))
    records = []

    while remaining:
        representative = min(remaining)
        target_maps = {}
        stabilizers = []

        for group_index, permutation in enumerate(permutations):
            target = permutation[representative]
            target_maps.setdefault(target, []).append(group_index)
            if target == representative:
                stabilizers.append(group_index)

        orbit = sorted(target_maps)
        remaining.difference_update(orbit)
        records.append(
            {
                "representative": representative,
                "representative_shape": list(shapes[representative]),
                "orbit": orbit,
                "orbit_size": len(orbit),
                "stabilizers": stabilizers,
                "target_maps": {
                    str(target): maps for target, maps in sorted(target_maps.items())
                },
            }
        )

    sizes = sorted(record["orbit_size"] for record in records)
    gate("three O_h shell-six orbits", len(records) == 3, str(sizes))
    gate("orbit sizes are 8,12,24", sizes == [8, 12, 24], str(sizes))
    gate(
        "orbits cover all states",
        sorted(i for record in records for i in record["orbit"])
        == list(range(len(shapes))),
    )
    return records


def project_exact_column(word, edge_index, verbose):
    h1_edges, h2_edges = engine.exact_column(
        word,
        shell_len=6,
        E0=F(4),
        verbose=verbose,
    )

    dimension = len(edge_index)
    h1 = [F(0) for _ in range(dimension)]
    h2 = [F(0) for _ in range(dimension)]
    outside_h1 = F(0)
    outside_h2 = F(0)

    for edges, amplitude in h1_edges.items():
        key = engine.canonical_edges_translation(edges)
        if key in edge_index:
            h1[edge_index[key]] += amplitude
        else:
            outside_h1 += amplitude

    for edges, amplitude in h2_edges.items():
        key = engine.canonical_edges_translation(edges)
        if key in edge_index:
            h2[edge_index[key]] += amplitude
        else:
            outside_h2 += amplitude

    # Projection outside the shell is expected to be absent after the second hop.
    gate("H1 projection closes on shell six", outside_h1 == 0, str(outside_h1))
    gate("H2 projection closes on shell six", outside_h2 == 0, str(outside_h2))
    return h1, h2


def apply_permutation_to_vector(vector, permutation):
    output = [F(0) for _ in vector]
    for source, target in enumerate(permutation):
        output[target] = vector[source]
    return output


def save_representative_checkpoint(
    path: Path,
    shapes,
    orbit_records,
    representative_columns,
    calibration,
):
    payload = {
        "meta": {
            "version": VERSION,
            "basis_dimension": len(shapes),
            "completed_representatives": sorted(
                int(index) for index in representative_columns
            ),
            "variable": "u=beta_lat/6=1/g^4",
            "common_scalar_omitted": True,
        },
        "shell_shapes": [list(shape) for shape in shapes],
        "orbits": orbit_records,
        "representative_columns": {
            str(index): {
                "H1": fraction_vector_to_strings(columns["H1"]),
                "H2_connected": fraction_vector_to_strings(
                    columns["H2_connected"]
                ),
            }
            for index, columns in sorted(representative_columns.items())
        },
        "shell4_calibration": calibration,
    }
    temporary = path.with_suffix(path.suffix + ".tmp")
    temporary.write_text(
        json.dumps(payload, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    temporary.replace(path)


def load_representative_checkpoint(path: Path, shapes, orbit_records):
    if not path.exists():
        return {}, None

    payload = json.loads(path.read_text(encoding="utf-8"))
    gate("checkpoint version", payload["meta"]["version"] == VERSION)
    gate(
        "checkpoint basis",
        payload["shell_shapes"] == [list(shape) for shape in shapes],
    )

    stored_orbits = [
        {
            key: value
            for key, value in record.items()
            if key != "target_maps"
        }
        for record in payload["orbits"]
    ]
    current_orbits = [
        {
            key: value
            for key, value in record.items()
            if key != "target_maps"
        }
        for record in orbit_records
    ]
    gate("checkpoint orbit decomposition", stored_orbits == current_orbits)

    columns = {}
    for index, item in payload["representative_columns"].items():
        columns[int(index)] = {
            "H1": strings_to_fraction_vector(item["H1"]),
            "H2_connected": strings_to_fraction_vector(
                item["H2_connected"]
            ),
        }
    return columns, payload.get("shell4_calibration")


def representative_stabilizer_gates(
    representative,
    h1,
    h2,
    orbit_record,
    permutations,
):
    for group_index in orbit_record["stabilizers"]:
        permutation = permutations[group_index]
        gate(
            f"H1 stabilizer covariance rep={representative} g={group_index}",
            apply_permutation_to_vector(h1, permutation) == h1,
        )
        gate(
            f"H2 stabilizer covariance rep={representative} g={group_index}",
            apply_permutation_to_vector(h2, permutation) == h2,
        )

    # Multiple group maps to the same target must reconstruct the same column.
    for target_text, maps in orbit_record["target_maps"].items():
        target = int(target_text)
        reference_h1 = None
        reference_h2 = None
        for group_index in maps:
            permutation = permutations[group_index]
            candidate_h1 = apply_permutation_to_vector(h1, permutation)
            candidate_h2 = apply_permutation_to_vector(h2, permutation)
            if reference_h1 is None:
                reference_h1 = candidate_h1
                reference_h2 = candidate_h2
            else:
                gate(
                    f"H1 map consistency rep={representative} target={target}",
                    candidate_h1 == reference_h1,
                )
                gate(
                    f"H2 map consistency rep={representative} target={target}",
                    candidate_h2 == reference_h2,
                )


def reconstruct_full_matrices(
    dimension,
    orbit_records,
    representative_columns,
    permutations,
):
    h1 = [[F(0) for _ in range(dimension)] for _ in range(dimension)]
    h2 = [[F(0) for _ in range(dimension)] for _ in range(dimension)]
    assigned = set()

    for orbit_record in orbit_records:
        representative = orbit_record["representative"]
        columns = representative_columns[representative]
        rep_h1 = columns["H1"]
        rep_h2 = columns["H2_connected"]

        representative_stabilizer_gates(
            representative,
            rep_h1,
            rep_h2,
            orbit_record,
            permutations,
        )

        for target_text, maps in orbit_record["target_maps"].items():
            target = int(target_text)
            permutation = permutations[maps[0]]
            target_h1 = apply_permutation_to_vector(rep_h1, permutation)
            target_h2 = apply_permutation_to_vector(rep_h2, permutation)
            for row in range(dimension):
                h1[row][target] = target_h1[row]
                h2[row][target] = target_h2[row]
            assigned.add(target)

    gate(
        "all matrix columns reconstructed",
        assigned == set(range(dimension)),
        str(len(assigned)),
    )
    return h1, h2


def exact_matrix_gates(h1, h2, permutations, shapes):
    transpose_h1 = [list(row) for row in zip(*h1)]
    transpose_h2 = [list(row) for row in zip(*h2)]
    gate("H1 exact symmetry", h1 == transpose_h1)
    gate("H2 exact symmetry", h2 == transpose_h2)

    dimension = len(shapes)

    def commute(matrix, permutation):
        # H P = P H, exact.
        for row in range(dimension):
            for column in range(dimension):
                left = matrix[row][permutation[column]]
                right = matrix[
                    permutations_inverse(permutation)[row]
                ][column]
                if left != right:
                    return False
        return True

    # Faster exact relation: H[p(r),p(c)] = H[r,c].
    for group_index, permutation in enumerate(permutations):
        condition_h1 = all(
            h1[permutation[row]][permutation[column]] == h1[row][column]
            for row in range(dimension)
            for column in range(dimension)
        )
        condition_h2 = all(
            h2[permutation[row]][permutation[column]] == h2[row][column]
            for row in range(dimension)
            for column in range(dimension)
        )
        gate(f"H1 exact O_h covariance g={group_index}", condition_h1)
        gate(f"H2 exact O_h covariance g={group_index}", condition_h2)

    shape_index = {shape: i for i, shape in enumerate(shapes)}
    reversal = [
        shape_index[engine.reverse_shape(shape)] for shape in shapes
    ]
    gate(
        "H1 exact C covariance",
        all(
            h1[reversal[row]][reversal[column]] == h1[row][column]
            for row in range(dimension)
            for column in range(dimension)
        ),
    )
    gate(
        "H2 exact C covariance",
        all(
            h2[reversal[row]][reversal[column]] == h2[row][column]
            for row in range(dimension)
            for column in range(dimension)
        ),
    )

    nonzero_h1 = [
        value for row in h1 for value in row if value != 0
    ]
    gate("H1 has 96 nonzero entries", len(nonzero_h1) == 96, str(len(nonzero_h1)))
    gate(
        "all H1 entries are -1/3",
        set(nonzero_h1) == {F(-1, 3)},
        str(sorted(set(nonzero_h1))),
    )


def permutations_inverse(permutation):
    inverse = [0 for _ in permutation]
    for source, target in enumerate(permutation):
        inverse[target] = source
    return inverse


def save_full_matrix(
    path,
    shapes,
    orbit_records,
    h1,
    h2,
    calibration,
    representative_checkpoint,
):
    payload = {
        "meta": {
            "version": VERSION,
            "scope": (
                "Exact connected shell-six H1/H2 reconstructed from three "
                "O_h representative columns. Common scalar omitted."
            ),
            "variable": "u=beta_lat/6=1/g^4",
            "basis_dimension": len(shapes),
            "orbit_sizes": [
                record["orbit_size"] for record in orbit_records
            ],
            "representative_indices": [
                record["representative"] for record in orbit_records
            ],
        },
        "shell_shapes": [list(shape) for shape in shapes],
        "orbits": orbit_records,
        "H1": [
            [str(value) for value in row] for row in h1
        ],
        "H2_connected": [
            [str(value) for value in row] for row in h2
        ],
        "shell4_calibration": calibration,
        "gates": {
            "three_orbits": True,
            "stabilizer_consistency": True,
            "exact_symmetry": True,
            "exact_Oh_covariance": True,
            "exact_C_covariance": True,
        },
    }
    path.write_text(
        json.dumps(payload, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )


def convert_to_v1_matrix_format(source, destination):
    payload = json.loads(source.read_text(encoding="utf-8"))
    converted = {
        "meta": {
            "version": payload["meta"]["version"],
            "scope": payload["meta"]["scope"],
            "completed_columns": payload["meta"]["basis_dimension"],
            "matrix_dimension": payload["meta"]["basis_dimension"],
            "term_topology_cache_size": 0,
        },
        "shell_shapes": payload["shell_shapes"],
        "H1": payload["H1"],
        "H2_connected": payload["H2_connected"],
        "shell4_calibration": payload["shell4_calibration"],
    }
    destination.write_text(
        json.dumps(converted, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )


def compute(args):
    engine.configure_term_cache(args.term_cache.resolve())

    shapes, words, edge_index = shell_basis()
    _group, permutations = group_permutations(shapes)
    orbits = orbit_data(shapes, permutations)

    print("O_h ORBIT DECOMPOSITION")
    for record in orbits:
        print(
            f"  representative {record['representative']:2d}: "
            f"size={record['orbit_size']:2d}, "
            f"shape={tuple(record['representative_shape'])}, "
            f"stabilizer={len(record['stabilizers'])}",
            flush=True,
        )

    calibration = engine.shell4_codd_calibration(
        verbose=not args.quiet
    )

    representative_columns = {}
    old_calibration = None
    if args.resume:
        representative_columns, old_calibration = (
            load_representative_checkpoint(
                args.representatives.resolve(),
                shapes,
                orbits,
            )
        )
        if old_calibration is not None:
            gate(
                "checkpoint calibration",
                old_calibration == calibration,
            )

    completed_this_run = 0
    for record in orbits:
        representative = record["representative"]
        if representative in representative_columns:
            print(
                f"SKIP representative {representative}: already checkpointed",
                flush=True,
            )
            continue
        if (
            args.max_representatives is not None
            and completed_this_run >= args.max_representatives
        ):
            break

        start = time.time()
        print(
            f"\nREPRESENTATIVE {representative}: "
            f"orbit size {record['orbit_size']}",
            flush=True,
        )
        h1, h2 = project_exact_column(
            words[representative],
            edge_index,
            verbose=not args.quiet,
        )
        representative_stabilizer_gates(
            representative,
            h1,
            h2,
            record,
            permutations,
        )
        representative_columns[representative] = {
            "H1": h1,
            "H2_connected": h2,
        }
        save_representative_checkpoint(
            args.representatives.resolve(),
            shapes,
            orbits,
            representative_columns,
            calibration,
        )
        completed_this_run += 1
        print(
            f"  representative {representative} completed in "
            f"{time.time() - start:.1f} s; "
            f"H1 nnz={sum(value != 0 for value in h1)}, "
            f"H2 nnz={sum(value != 0 for value in h2)}, "
            f"cache={engine.term_cache_size()}",
            flush=True,
        )

    # Rewrite the representative checkpoint in canonical metadata form even
    # when all representatives were loaded from an older checkpoint.
    save_representative_checkpoint(
        args.representatives.resolve(),
        shapes,
        orbits,
        representative_columns,
        calibration,
    )

    required = {record["representative"] for record in orbits}
    available = set(representative_columns)
    if available != required:
        print(
            "PARTIAL REPRESENTATIVE CHECKPOINT: "
            f"{len(available)}/{len(required)} complete",
            flush=True,
        )
        return None

    h1, h2 = reconstruct_full_matrices(
        len(shapes),
        orbits,
        representative_columns,
        permutations,
    )
    exact_matrix_gates(h1, h2, permutations, shapes)

    save_full_matrix(
        args.matrix.resolve(),
        shapes,
        orbits,
        h1,
        h2,
        calibration,
        args.representatives.resolve(),
    )

    compatible = args.matrix.resolve().with_name(
        args.matrix.stem + "_v1_compatible.json"
    )
    convert_to_v1_matrix_format(args.matrix.resolve(), compatible)

    engine.analyze_shell6_matrix(
        compatible,
        args.analysis.resolve(),
    )

    print("ALL SYMMETRY-REDUCED SHELL-SIX GATES PASS", flush=True)
    print(f"MATRIX {args.matrix.resolve()}", flush=True)
    print(f"ANALYSIS {args.analysis.resolve()}", flush=True)
    return args.matrix.resolve()


def analyze_only(args):
    compatible = args.matrix.resolve().with_name(
        args.matrix.stem + "_v1_compatible.json"
    )
    convert_to_v1_matrix_format(args.matrix.resolve(), compatible)
    engine.analyze_shell6_matrix(
        compatible,
        args.analysis.resolve(),
    )


def parse_args():
    parser = argparse.ArgumentParser(
        description=(
            "Three-orbit exact shell-six O(u^2) SU(3) computation."
        )
    )
    parser.add_argument(
        "--mode",
        choices=("orbits", "compute", "analyze", "all"),
        default="all",
    )
    parser.add_argument(
        "--representatives",
        type=Path,
        default=Path("CERT_SHELL6_o2_representatives_v2.json"),
    )
    parser.add_argument(
        "--matrix",
        type=Path,
        default=Path("CERT_SHELL6_o2_matrix_v2.json"),
    )
    parser.add_argument(
        "--analysis",
        type=Path,
        default=Path("shell6_o2_analysis_v2.json"),
    )
    parser.add_argument(
        "--term-cache",
        type=Path,
        default=Path("shell6_o2_full_intermediate_term_cache.pkl"),
    )
    parser.add_argument(
        "--max-representatives",
        type=int,
        default=None,
    )
    parser.add_argument(
        "--no-resume",
        dest="resume",
        action="store_false",
    )
    parser.add_argument("--quiet", action="store_true")
    parser.set_defaults(resume=True)
    return parser.parse_args()


def main():
    args = parse_args()

    if args.mode == "orbits":
        shapes, _words, _edge_index = shell_basis()
        _group, permutations = group_permutations(shapes)
        records = orbit_data(shapes, permutations)
        print(json.dumps(records, indent=2, sort_keys=True))
        return

    if args.mode in ("compute", "all"):
        compute(args)
        return

    if args.mode == "analyze":
        analyze_only(args)


if __name__ == "__main__":
    main()
