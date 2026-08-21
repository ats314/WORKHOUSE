#!/usr/bin/env python3
"""
SU(4) exceptional local Haar/Casimir algebra certificate.

Consumes the output of y4_su4_exceptional_enumerator_v1.py and constructs,
in exact arithmetic, the finite-rank local library needed by the global O(y^4)
contraction.

For every oriented exceptional signature, this script:

  * builds an explicit invariant basis:
      (4,0)/(0,4): epsilon tensor;
      (5,1)/(1,5): five delta-epsilon tensors of rank four;
  * removes the unique five-index antisymmetry relation;
  * constructs the exact Gram matrix;
  * builds the three nested prefix Casimirs by Fierz identities;
  * verifies exact closure, G-self-adjointness, and mutual commutativity;
  * performs the exact joint eigenspace decomposition;
  * exports each channel as
        sum_ab K_ab T_a(row) T_b(col)
    together with its (C2_cut1,C2_cut2,C2_cut3) history;
  * proves the channel projectors are orthogonal, idempotent, and complete.

Input, preferred:
  SU4_EXCEPTIONAL_ENUMERATOR_V1_BUNDLE.zip

Fallback:
  y4_su4_local_signature_catalog.json

Outputs:
  SU4_LOCAL_ALGEBRA_V1/SU4_LOCAL_ALGEBRA_V1.json
  SU4_LOCAL_ALGEBRA_V1/SU4_LOCAL_ALGEBRA_V1.md
  SU4_LOCAL_ALGEBRA_V1/y4_su4_exceptional_local_library.json
  SU4_LOCAL_ALGEBRA_V1_BUNDLE.zip
"""
from __future__ import annotations

import hashlib
import itertools
import json
import os
import re
import sys
import time
import zipfile
from collections import Counter, defaultdict
from fractions import Fraction
from pathlib import Path
from typing import Any, Iterable

import sympy as sp

VERSION = "2026-06-14-su4-local-algebra-v1"
N = 4
CUTS = (1, 2, 3)
BASE = Path("/content") if Path("/content").exists() else Path("/mnt/data")
OUT = BASE / "SU4_LOCAL_ALGEBRA_V1"
EXTRACT = OUT / "extracted"
OUT.mkdir(parents=True, exist_ok=True)
EXTRACT.mkdir(parents=True, exist_ok=True)

ENUM_BUNDLE_GLOB = "SU4_EXCEPTIONAL_ENUMERATOR_V1_BUNDLE*.zip"
CATALOG_NAME = "y4_su4_local_signature_catalog.json"


def gate(name: str, cond: bool, detail: str = "") -> None:
    status = "PASS" if cond else "FAIL"
    print(f"{status:4s} {name:92s} {detail}")
    if not cond:
        raise AssertionError(f"{name}: {detail}")


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for block in iter(lambda: f.read(1 << 20), b""):
            h.update(block)
    return h.hexdigest()


def safe_extract(zpath: Path, dest: Path) -> list[Path]:
    dest.mkdir(parents=True, exist_ok=True)
    root = dest.resolve()
    with zipfile.ZipFile(zpath) as zf:
        for info in zf.infolist():
            target = (dest / info.filename).resolve()
            if target != root and not str(target).startswith(str(root) + os.sep):
                raise ValueError(f"unsafe ZIP member: {info.filename}")
        zf.extractall(dest)
        return [dest / x.filename for x in zf.infolist() if not x.is_dir()]


def recursive_extract(archives: Iterable[Path], max_depth: int = 3) -> list[dict[str, Any]]:
    queue = [(Path(p), 0) for p in archives]
    seen: set[str] = set()
    records: list[dict[str, Any]] = []
    while queue:
        zp, depth = queue.pop(0)
        if depth > max_depth or not zp.is_file():
            continue
        h = sha256(zp)
        if h in seen:
            continue
        seen.add(h)
        label = re.sub(r"[^A-Za-z0-9_.-]+", "_", zp.stem)[:90]
        dest = EXTRACT / f"d{depth}_{label}_{h[:10]}"
        try:
            files = safe_extract(zp, dest)
            records.append({
                "archive": str(zp), "sha256": h, "depth": depth,
                "destination": str(dest), "file_count": len(files), "status": "ok",
            })
            for p in files:
                if p.suffix.lower() == ".zip":
                    queue.append((p, depth + 1))
        except Exception as exc:
            records.append({
                "archive": str(zp), "sha256": h, "depth": depth,
                "status": "error", "error": repr(exc),
            })
    return records


def find_all(name: str, roots: Iterable[Path]) -> list[Path]:
    found: dict[str, Path] = {}
    for root in roots:
        if not root.exists():
            continue
        for p in root.rglob(name):
            if p.is_file():
                found[sha256(p)] = p
    return sorted(found.values(), key=lambda p: str(p))


def find_glob(pattern: str, roots: Iterable[Path]) -> list[Path]:
    found: dict[str, Path] = {}
    for root in roots:
        if not root.exists():
            continue
        for p in root.rglob(pattern):
            if p.is_file():
                found[sha256(p)] = p
    return sorted(found.values(), key=lambda p: str(p))


def upload_if_needed() -> list[Path]:
    if find_all(CATALOG_NAME, [BASE]) or find_glob(ENUM_BUNDLE_GLOB, [BASE]):
        return []
    if not Path("/content").exists():
        return []
    try:
        from google.colab import files as colab_files  # type: ignore
    except Exception:
        return []
    print("\nUPLOAD REQUIRED — select:")
    print("  SU4_EXCEPTIONAL_ENUMERATOR_V1_BUNDLE.zip")
    print("or:")
    print("  y4_su4_local_signature_catalog.json")
    uploaded = colab_files.upload()
    saved: list[Path] = []
    for name, data in uploaded.items():
        target = Path("/content") / Path(name).name
        target.write_bytes(data)
        saved.append(target)
        print(f"saved {len(data):,} bytes -> {target}")
    return saved


def parity(p: tuple[int, ...]) -> int:
    inversions = sum(
        p[i] > p[j]
        for i in range(len(p))
        for j in range(i + 1, len(p))
    )
    return -1 if inversions & 1 else 1


def flat_index(values: tuple[int, ...]) -> int:
    out = 0
    for value in values:
        out = N * out + value
    return out


def unflat_index(index: int, length: int) -> tuple[int, ...]:
    values = [0] * length
    for i in range(length - 1, -1, -1):
        values[i] = index % N
        index //= N
    return tuple(values)


Vector = dict[int, Fraction]


def clean(v: Vector) -> Vector:
    return {k: x for k, x in v.items() if x}


def add_scaled(out: Vector, v: Vector, coefficient: Fraction) -> None:
    if not coefficient:
        return
    for key, value in v.items():
        out[key] = out.get(key, Fraction(0)) + coefficient * value


def dot(a: Vector, b: Vector) -> Fraction:
    if len(a) > len(b):
        a, b = b, a
    return sum(value * b.get(key, 0) for key, value in a.items())


def epsilon_vector(length: int, positions: list[int]) -> Vector:
    out: Vector = {}
    for permutation in itertools.permutations(range(N)):
        values = [0] * length
        for position, color in zip(positions, permutation):
            values[position] = color
        out[flat_index(tuple(values))] = Fraction(parity(permutation))
    return out


def delta_epsilon_vector(
    tokens: tuple[int, ...],
    chosen_excess_position: int,
) -> Vector:
    plus = [i for i, token in enumerate(tokens) if token == 1]
    minus = [i for i, token in enumerate(tokens) if token == -1]
    if len(plus) == 5 and len(minus) == 1:
        excess = plus
        paired_position = minus[0]
    elif len(minus) == 5 and len(plus) == 1:
        excess = minus
        paired_position = plus[0]
    else:
        raise ValueError((tokens, chosen_excess_position))

    remaining = [i for i in excess if i != chosen_excess_position]
    out: Vector = {}
    for paired_color in range(N):
        for permutation in itertools.permutations(range(N)):
            values = [0] * len(tokens)
            values[chosen_excess_position] = paired_color
            values[paired_position] = paired_color
            for position, color in zip(remaining, permutation):
                values[position] = color
            key = flat_index(tuple(values))
            out[key] = out.get(key, Fraction(0)) + Fraction(parity(permutation))
    return clean(out)


def swap_operator(v: Vector, length: int, a: int, b: int) -> Vector:
    out: Vector = {}
    for key, value in v.items():
        values = list(unflat_index(key, length))
        values[a], values[b] = values[b], values[a]
        new_key = flat_index(tuple(values))
        out[new_key] = out.get(new_key, Fraction(0)) + value
    return clean(out)


def contraction_operator(v: Vector, length: int, a: int, b: int) -> Vector:
    """
    K on V tensor V*: K|i,j> = delta_ij sum_c |c,c>.
    """
    grouped: dict[tuple[int, ...], Fraction] = defaultdict(Fraction)
    for key, value in v.items():
        values = unflat_index(key, length)
        if values[a] == values[b]:
            remaining = tuple(
                values[i] for i in range(length) if i not in (a, b)
            )
            grouped[remaining] += value

    out: Vector = {}
    for remaining, coefficient in grouped.items():
        for color in range(N):
            values = []
            iterator = iter(remaining)
            for i in range(length):
                values.append(color if i in (a, b) else next(iterator))
            key = flat_index(tuple(values))
            out[key] = out.get(key, Fraction(0)) + coefficient
    return clean(out)


def casimir_apply(
    v: Vector,
    tokens: tuple[int, ...],
    event_positions: tuple[int, ...],
    cut: int,
) -> Vector:
    prefix = [
        local_position
        for local_position, event_position in enumerate(event_positions)
        if event_position <= cut
    ]
    out: Vector = {}
    c_f = Fraction(N * N - 1, 2 * N)
    add_scaled(out, v, len(prefix) * c_f)

    for offset, a in enumerate(prefix):
        for b in prefix[offset + 1:]:
            if tokens[a] == tokens[b]:
                # 2 T_a.T_b = P_ab - I/N.
                add_scaled(out, swap_operator(v, len(tokens), a, b), Fraction(1))
                add_scaled(out, v, Fraction(-1, N))
            else:
                # 2 T_a.T_bbar = -K_ab + I/N.
                add_scaled(out, contraction_operator(v, len(tokens), a, b), Fraction(-1))
                add_scaled(out, v, Fraction(1, N))
    return clean(out)


def to_sympy(value: Fraction) -> sp.Rational:
    return sp.Rational(value.numerator, value.denominator)


def matrix_to_strings(matrix: sp.Matrix) -> list[list[str]]:
    return [[str(sp.factor(matrix[i, j])) for j in range(matrix.cols)]
            for i in range(matrix.rows)]


def vector_linear_combination(
    basis: list[Vector],
    coefficients: list[Fraction],
) -> Vector:
    out: Vector = {}
    for vector, coefficient in zip(basis, coefficients):
        add_scaled(out, vector, coefficient)
    return clean(out)


def restricted_matrix(M: sp.Matrix, S: sp.Matrix) -> sp.Matrix:
    """Return X with M S = S X, using an exact invertible row minor."""
    rank = S.cols
    pivot_rows = list(S.T.rref()[1])
    minor = S.extract(pivot_rows, range(rank))
    gate("joint-decomposition subspace minor is nonsingular",
         minor.det() != 0, f"rank={rank}")
    rhs = (M * S).extract(pivot_rows, range(rank))
    X = sp.simplify(minor.inv() * rhs)
    gate("restricted Casimir preserves current joint subspace",
         M * S == S * X, "")
    return X


def joint_eigenspaces(matrices: list[sp.Matrix]) -> list[dict[str, Any]]:
    dimension = matrices[0].rows
    spaces = [{"basis": sp.eye(dimension), "eigenvalues": []}]
    for M in matrices:
        refined = []
        for record in spaces:
            S = record["basis"]
            X = restricted_matrix(M, S)
            for eigenvalue, multiplicity, eigenvectors in X.eigenvects():
                V = sp.Matrix.hstack(*eigenvectors)
                gate("eigenspace dimension matches algebraic multiplicity",
                     V.cols == multiplicity,
                     f"lambda={eigenvalue} cols={V.cols} multiplicity={multiplicity}")
                refined.append({
                    "basis": sp.simplify(S * V),
                    "eigenvalues": record["eigenvalues"] + [sp.factor(eigenvalue)],
                })
        spaces = refined
    return spaces


def candidate_basis(signature: tuple[int, ...]) -> tuple[
    tuple[int, ...], tuple[int, ...], list[dict[str, Any]], list[Vector]
]:
    event_positions = tuple(i for i, token in enumerate(signature) if token)
    tokens = tuple(signature[i] for i in event_positions)
    plus = tokens.count(1)
    minus = tokens.count(-1)

    descriptors: list[dict[str, Any]] = []
    vectors: list[Vector] = []

    if (plus, minus) in {(4, 0), (0, 4)}:
        descriptors.append({
            "type": "epsilon",
            "event_positions": list(event_positions),
            "orientation": "fundamental" if plus == 4 else "antifundamental",
        })
        vectors.append(epsilon_vector(len(tokens), list(range(len(tokens)))))
    elif (plus, minus) in {(5, 1), (1, 5)}:
        excess_token = 1 if plus == 5 else -1
        excess_positions = [
            i for i, token in enumerate(tokens) if token == excess_token
        ]
        paired_position = next(
            i for i, token in enumerate(tokens) if token == -excess_token
        )
        for chosen in excess_positions:
            descriptors.append({
                "type": "delta_epsilon",
                "chosen_excess_local_position": chosen,
                "chosen_excess_event": event_positions[chosen],
                "paired_local_position": paired_position,
                "paired_event": event_positions[paired_position],
                "epsilon_events": [
                    event_positions[i] for i in excess_positions if i != chosen
                ],
                "excess_orientation": (
                    "fundamental" if excess_token == 1 else "antifundamental"
                ),
            })
            vectors.append(delta_epsilon_vector(tokens, chosen))
    else:
        raise ValueError((signature, plus, minus))

    return event_positions, tokens, descriptors, vectors


def analyze_signature(row: dict[str, Any]) -> dict[str, Any]:
    signature = tuple(int(x) for x in row["signature"])
    event_positions, tokens, descriptors, candidates = candidate_basis(signature)
    family = (tokens.count(1), tokens.count(-1))
    expected_rank = 1 if family in {(4, 0), (0, 4)} else 4

    candidate_gram = sp.Matrix([
        [to_sympy(dot(a, b)) for b in candidates]
        for a in candidates
    ])
    rank = candidate_gram.rank()
    gate("exceptional invariant-space rank",
         rank == expected_rank,
         f"signature={signature} family={family} rank={rank}")

    pivots = list(candidate_gram.rref()[1])
    gate("independent invariant basis has expected size",
         len(pivots) == expected_rank,
         f"signature={signature} pivots={pivots}")

    basis = [candidates[i] for i in pivots]
    basis_descriptors = [descriptors[i] for i in pivots]
    G = candidate_gram.extract(pivots, pivots)
    gate("independent invariant Gram matrix is positive definite",
         all(x > 0 for x in G.cholesky().diagonal()),
         f"signature={signature}")

    cut_matrices: list[sp.Matrix] = []
    cut_eigenvalue_histograms: list[dict[str, int]] = []

    for cut in CUTS:
        operated = [
            casimir_apply(vector, tokens, event_positions, cut)
            for vector in basis
        ]
        H = sp.Matrix([
            [to_sympy(dot(left, right)) for right in operated]
            for left in basis
        ])
        M = sp.simplify(G.inv() * H)

        # Exact closure in the invariant basis.
        for column, operated_vector in enumerate(operated):
            coefficients = [
                Fraction(int(sp.numer(M[i, column])), int(sp.denom(M[i, column])))
                for i in range(M.rows)
            ]
            reconstructed = vector_linear_combination(basis, coefficients)
            gate("prefix Casimir closes on invariant basis",
                 reconstructed == operated_vector,
                 f"signature={signature} cut={cut} column={column}")

        gate("prefix Casimir is self-adjoint in the invariant Gram metric",
             G * M == M.T * G,
             f"signature={signature} cut={cut}")
        eigenvalues = M.eigenvals()
        gate("prefix Casimir spectrum is rational and nonnegative",
             all(value.is_Rational and value >= 0 for value in eigenvalues),
             f"signature={signature} cut={cut} eigenvalues={eigenvalues}")

        cut_matrices.append(M)
        cut_eigenvalue_histograms.append({
            str(sp.factor(value)): int(multiplicity)
            for value, multiplicity in sorted(
                eigenvalues.items(), key=lambda item: sp.default_sort_key(item[0])
            )
        })

    for i in range(len(cut_matrices)):
        for j in range(i + 1, len(cut_matrices)):
            gate("nested prefix Casimirs commute exactly",
                 cut_matrices[i] * cut_matrices[j]
                 == cut_matrices[j] * cut_matrices[i],
                 f"signature={signature} cuts={CUTS[i]},{CUTS[j]}")

    spaces = joint_eigenspaces(cut_matrices)
    gate("joint Casimir eigenspaces span invariant space",
         sum(record["basis"].cols for record in spaces) == expected_rank,
         f"signature={signature}")

    channels = []
    kernels = []
    for channel_index, space in enumerate(spaces, start=1):
        S = space["basis"]
        Gs = sp.simplify(S.T * G * S)
        K = sp.simplify(S * Gs.inv() * S.T)
        multiplicity = S.cols

        gate("joint channel projector is idempotent",
             sp.simplify(K * G * K - K) == sp.zeros(K.rows),
             f"signature={signature} channel={channel_index}")
        gate("joint channel trace equals multiplicity",
             sp.simplify(sp.trace(K * G)) == multiplicity,
             f"signature={signature} channel={channel_index}")

        kernels.append(K)
        channels.append({
            "channel_id": f"C{channel_index:02d}",
            "casimir_history": [str(sp.factor(x)) for x in space["eigenvalues"]],
            "multiplicity": multiplicity,
            "basis_coefficient_subspace": matrix_to_strings(S),
            "kernel_in_independent_invariant_basis": matrix_to_strings(K),
            "kernel_nonzero_entries": sum(
                K[i, j] != 0 for i in range(K.rows) for j in range(K.cols)
            ),
        })

    for i in range(len(kernels)):
        for j in range(i + 1, len(kernels)):
            gate("distinct joint channel projectors are Gram-orthogonal",
                 sp.simplify(kernels[i] * G * kernels[j])
                 == sp.zeros(expected_rank),
                 f"signature={signature} channels={i+1},{j+1}")

    total_kernel = sum(kernels, sp.zeros(expected_rank))
    gate("joint channel projectors resolve the full Haar projector",
         sp.simplify(total_kernel - G.inv()) == sp.zeros(expected_rank),
         f"signature={signature}")
    gate("full Haar projector has trace equal to invariant dimension",
         sp.simplify(sp.trace(G.inv() * G)) == expected_rank,
         f"signature={signature}")

    audit_det_cuts = tuple(int(x) for x in row.get("determinant_cuts", []))
    zero_cut3_channels = sum(
        channel["multiplicity"]
        for channel in channels
        if channel["casimir_history"][2] == "0"
    )
    if 3 in audit_det_cuts:
        gate("enumerator determinant-cut flag has a C2=0 cut-3 channel",
             zero_cut3_channels >= 1,
             f"signature={signature} zero_mult={zero_cut3_channels}")
    else:
        gate("no unflagged C2=0 cut-3 determinant channel",
             zero_cut3_channels == 0,
             f"signature={signature} zero_mult={zero_cut3_channels}")

    # For a pure four-strand final invariant the prefix channel is exterior power.
    if family in {(4, 0), (0, 4)}:
        expected = []
        for cut in CUTS:
            p = sum(event <= cut for event in event_positions)
            expected.append(Fraction(p * (N - p) * (N + 1), 2 * N))
        actual = tuple(
            Fraction(int(sp.numer(cut_matrices[i][0, 0])),
                     int(sp.denom(cut_matrices[i][0, 0])))
            for i in range(3)
        )
        gate("pure determinant signature follows exterior-power Casimirs",
             actual == tuple(expected),
             f"signature={signature} actual={actual} expected={tuple(expected)}")

    return {
        "signature": list(signature),
        "canonical_under_C": row.get("canonical_under_C"),
        "occurrences": int(row.get("occurrences", 0)),
        "family": list(family),
        "final_charge": family[0] - family[1],
        "event_positions": list(event_positions),
        "active_tokens": list(tokens),
        "audit_cut_charges": row.get("cut_charges", []),
        "audit_determinant_cuts": list(audit_det_cuts),
        "candidate_basis_size": len(candidates),
        "invariant_dimension": expected_rank,
        "candidate_gram": matrix_to_strings(candidate_gram),
        "independent_candidate_indices": pivots,
        "independent_basis_descriptors": basis_descriptors,
        "independent_gram": matrix_to_strings(G),
        "cut_casimir_matrices": {
            str(cut): matrix_to_strings(matrix)
            for cut, matrix in zip(CUTS, cut_matrices)
        },
        "cut_spectra": {
            str(cut): spectrum
            for cut, spectrum in zip(CUTS, cut_eigenvalue_histograms)
        },
        "channels": channels,
        "cut3_determinant_channel_multiplicity": zero_cut3_channels,
    }


def main() -> None:
    started = time.time()
    print("=" * 116)
    print("SU(4) EXCEPTIONAL LOCAL HAAR + JOINT CASIMIR ALGEBRA")
    print("=" * 116)
    print("version :", VERSION)
    print("output  :", OUT)
    print("hardware: CPU exact sparse tensors and rational linear algebra")

    uploaded = upload_if_needed()
    archives = find_glob(ENUM_BUNDLE_GLOB, [BASE])
    archives += [p for p in uploaded if p.suffix.lower() == ".zip"]
    extraction = recursive_extract(archives)
    roots = [BASE, EXTRACT]

    catalog_paths = find_all(CATALOG_NAME, roots)
    gate("SU(4) local-signature catalog located", bool(catalog_paths), str(catalog_paths[:3]))
    catalog_path = catalog_paths[0]
    catalog = json.loads(catalog_path.read_text(encoding="utf-8"))
    rows = catalog["signatures"]

    gate("catalog contains exceptional signatures", bool(rows), str(len(rows)))
    gate("catalog families are exactly the SU(4) exceptional families",
         {
             tuple(int(x) for x in row["family"])
             for row in rows
         }.issubset({(4, 0), (0, 4), (5, 1), (1, 5)}),
         "")

    library_records = []
    family_signature_hist = Counter()
    family_occurrence_hist = Counter()
    invariant_dimension_hist = Counter()
    channel_history_hist = Counter()
    total_channel_kernel_terms = 0
    determinant_cut3_signature_count = 0

    for index, row in enumerate(rows, start=1):
        record = analyze_signature(row)
        record["local_library_id"] = f"S4L-{index:04d}"
        library_records.append(record)

        family = tuple(record["family"])
        family_signature_hist[family] += 1
        family_occurrence_hist[family] += record["occurrences"]
        invariant_dimension_hist[record["invariant_dimension"]] += 1
        if record["cut3_determinant_channel_multiplicity"]:
            determinant_cut3_signature_count += 1
        for channel in record["channels"]:
            history = tuple(channel["casimir_history"])
            channel_history_hist[history] += record["occurrences"] * channel["multiplicity"]
            total_channel_kernel_terms += channel["kernel_nonzero_entries"]

        if index % 10 == 0 or index == len(rows):
            print(
                f"[local algebra] signatures={index}/{len(rows)} "
                f"channels={sum(len(r['channels']) for r in library_records)}",
                flush=True,
            )

    # Charge-conjugation consistency.
    record_by_signature = {
        tuple(record["signature"]): record for record in library_records
    }
    for signature, record in record_by_signature.items():
        conjugate = tuple(-x for x in signature)
        if conjugate not in record_by_signature:
            continue
        other = record_by_signature[conjugate]
        gate("charge-conjugate signatures have equal invariant dimension",
             record["invariant_dimension"] == other["invariant_dimension"],
             f"{signature}")
        gate("charge-conjugate signatures have equal cut spectra",
             record["cut_spectra"] == other["cut_spectra"],
             f"{signature}")
        histories = sorted(
            (tuple(c["casimir_history"]), c["multiplicity"])
            for c in record["channels"]
        )
        other_histories = sorted(
            (tuple(c["casimir_history"]), c["multiplicity"])
            for c in other["channels"]
        )
        gate("charge-conjugate signatures have equal joint Casimir histories",
             histories == other_histories,
             f"{signature}")

    output_library = {
        "meta": {
            "version": VERSION,
            "rank": N,
            "normalization": "Tr(T^A T^B)=1/2 delta^{AB}",
            "local_tensor_formula": (
                "For each channel: P_channel(row,col)="
                "sum_ab K_ab T_a(row)T_b(col), using independent_basis_descriptors."
            ),
            "source_catalog": str(catalog_path),
            "source_catalog_sha256": sha256(catalog_path),
        },
        "counts": {
            "oriented_signatures": len(library_records),
            "families": {
                f"({a},{b})": count
                for (a, b), count in sorted(family_signature_hist.items())
            },
            "family_occurrences": {
                f"({a},{b})": count
                for (a, b), count in sorted(family_occurrence_hist.items())
            },
            "invariant_dimension_histogram": {
                str(k): v for k, v in sorted(invariant_dimension_hist.items())
            },
            "joint_channels": sum(len(record["channels"]) for record in library_records),
            "distinct_joint_casimir_histories": len(channel_history_hist),
            "signatures_with_cut3_determinant_channel": determinant_cut3_signature_count,
            "serialized_channel_kernel_nonzero_entries": total_channel_kernel_terms,
        },
        "joint_casimir_history_occurrence_histogram": {
            ",".join(history): count
            for history, count in sorted(channel_history_hist.items())
        },
        "signatures": library_records,
    }

    library_path = OUT / "y4_su4_exceptional_local_library.json"
    library_path.write_text(
        json.dumps(output_library, indent=2, sort_keys=True),
        encoding="utf-8",
    )
    library_sha = sha256(library_path)

    summary = {
        "version": VERSION,
        "status": "PASS",
        "inputs": {
            "catalog": str(catalog_path),
            "catalog_sha256": sha256(catalog_path),
            "extraction": extraction,
        },
        "counts": output_library["counts"],
        "family_signature_histogram": {
            f"({a},{b})": count
            for (a, b), count in sorted(family_signature_hist.items())
        },
        "family_occurrence_histogram": {
            f"({a},{b})": count
            for (a, b), count in sorted(family_occurrence_hist.items())
        },
        "gates": {
            "exact_gram_rank": True,
            "prefix_casimir_closure": True,
            "prefix_casimir_self_adjoint": True,
            "nested_casimirs_commute": True,
            "joint_projectors_idempotent": True,
            "joint_projectors_orthogonal": True,
            "joint_projectors_complete": True,
            "charge_conjugation_consistent": True,
            "passed": True,
        },
        "output": {
            "local_library": str(library_path),
            "local_library_sha256": library_sha,
        },
        "next_stage": (
            "Use this library only on the 312 exceptional assignments. Keep every balanced "
            "local node in the existing walled-Brauer library. Build the 76-word hybrid corpus, "
            "sum local channel Casimirs at cuts 1,2,3, apply the unchanged fourth-order folded "
            "coefficient, contract the exact delta-epsilon tensor networks, and add the resulting "
            "kernel delta to the balanced N=4 evaluation."
        ),
        "elapsed_seconds": time.time() - started,
    }

    json_path = OUT / "SU4_LOCAL_ALGEBRA_V1.json"
    json_path.write_text(json.dumps(summary, indent=2, sort_keys=True), encoding="utf-8")
    json_sha = sha256(json_path)

    md = fr"""# SU(4) exceptional local Haar and Casimir algebra

**Status:** PASS  
**Version:** `{VERSION}`

## Exact local invariant spaces

The exceptional signatures contain only:

- `(4,0)` and `(0,4)`: one-dimensional epsilon invariant;
- `(5,1)` and `(1,5)`: four-dimensional delta-epsilon invariant space.

The five natural delta-epsilon tensors have one exact linear dependency, the
five-index antisymmetry identity in four dimensions.

## Exact channel algebra

For every oriented signature, the certificate verifies:

- exact Gram rank;
- closure of all three prefix Casimirs;
- self-adjointness in the invariant Gram metric;
- mutual commutativity of the nested Casimirs;
- exact joint eigenspace decomposition;
- projector idempotence and orthogonality;
- completeness of the channel projectors;
- charge-conjugation consistency.

Counts:

```text
oriented signatures: {len(library_records)}
joint channels: {output_library['counts']['joint_channels']}
distinct Casimir histories: {output_library['counts']['distinct_joint_casimir_histories']}
signatures with a cut-3 determinant channel:
    {determinant_cut3_signature_count}
```

The local channel tensor exported for the next stage is

\[
P_{{\alpha}}(r,c)=\sum_{{a,b}}K^{{(\alpha)}}_{{ab}}T_a(r)T_b(c),
\]

where the basis tensors `T_a` are explicit epsilon or delta-epsilon tensors and
each channel carries its exact three-cut Casimir history.

## Next stage

Keep the verified balanced local library unchanged. Apply the exported finite
`SU(4)` library only to the 312 exceptional assignments in the 76 mixed words,
contract their exact tensor networks, and add the resulting kernel correction
to the balanced `N=4` evaluation.
"""
    md_path = OUT / "SU4_LOCAL_ALGEBRA_V1.md"
    md_path.write_text(md, encoding="utf-8")
    md_sha = sha256(md_path)

    bundle = BASE / "SU4_LOCAL_ALGEBRA_V1_BUNDLE.zip"
    with zipfile.ZipFile(bundle, "w", compression=zipfile.ZIP_DEFLATED) as zf:
        for p in (json_path, md_path, library_path):
            zf.write(p, arcname=p.name)
        source_path = Path(globals().get("__file__", ""))
        if source_path.is_file():
            zf.write(source_path, arcname=source_path.name)

    print("\n" + "=" * 116)
    print("SU(4) LOCAL ALGEBRA STATUS: PASS")
    print("=" * 116)
    print("oriented signatures                    :", len(library_records))
    print("family signature histogram             :", dict(sorted(family_signature_hist.items())))
    print("invariant dimension histogram          :", dict(sorted(invariant_dimension_hist.items())))
    print("joint channels                         :", output_library["counts"]["joint_channels"])
    print("distinct joint Casimir histories       :", len(channel_history_hist))
    print("signatures with cut-3 determinant      :", determinant_cut3_signature_count)
    print("serialized channel-kernel nonzero terms:", total_channel_kernel_terms)
    print("JSON:", json_path, json_sha)
    print("MD:  ", md_path, md_sha)
    print("LIB: ", library_path, library_sha)
    print("ZIP: ", bundle, sha256(bundle))
    print("=" * 116)


if __name__ == "__main__":
    main()
