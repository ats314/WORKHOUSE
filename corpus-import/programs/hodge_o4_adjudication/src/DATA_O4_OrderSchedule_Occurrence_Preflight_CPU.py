#!/usr/bin/env python3
"""Canonical CPU preflight for the SU(3) O(u^4) physical-Q schedule.

This is deliberately not a mass solver and not another oracle.  It certifies the
order boundary that the v25 finite-cluster tail violated:

    P -> Q1 -> Q2 -> Q1 -> P

The script:

* verifies the exact executed v10a2 notebook and its stored 17/17 evidence;
* enumerates the complete closed layer schedule through four W insertions;
* proves that W22 first appears at order five;
* checks that the accepted v10a2 occurrence census contains no seven-factor
  pattern;
* runs an exact Fraction one-face sensitivity regression in which deleting W22
  leaves coefficients through O(u^4) unchanged and changes O(u^5);
* exposes a reusable, provenance-first Hermitian O4 matrix assembler which never
  applies W to a Q2 source.

No Hamer value, historical target, Gelfand cluster calculation, scalar shift, or
Factor52 contractor is imported or evaluated here.
"""

from __future__ import annotations

import argparse
import ast
import contextlib
import hashlib
import io
import json
import os
import re
import sys
from collections import Counter, defaultdict
from dataclasses import asdict, dataclass
from fractions import Fraction
from pathlib import Path
from typing import Any, Callable, Iterable, Mapping, Sequence


SCHEMA = "hodge-o4-m3-preflight/v1"
ORDER = 4

P = 0
Q1 = 1
Q2 = 2
LAYER_NAMES = {P: "P", Q1: "Q1", Q2: "Q2"}

# Directed (target layer, source layer) blocks needed by some closed W word of
# length at most four.  W22 is intentionally absent.
O4_BLOCKS = frozenset({(P, P), (P, Q1), (Q1, P), (Q1, Q1), (Q1, Q2), (Q2, Q1)})
DIRECTLY_COMPUTED_BLOCKS = frozenset({(P, P), (Q1, P), (Q1, Q1), (Q2, Q1)})

APPROVED_CENTER_NEUTRAL_PATTERNS = frozenset(
    {(0, 3), (0, 6), (1, 1), (1, 4), (2, 2), (3, 0), (3, 3), (4, 1), (6, 0)}
)
FORBIDDEN_O4_PATTERNS = frozenset({(2, 5), (5, 2)})

V10A2_NOTEBOOK_SHA256 = "026DA360679CC7B7BCAC161A1DEAAA9A9E52B5D52C3892F624FF6B3DE6D82CE4"
V10A2_CODE_SHA256 = "AA55F3317A116A645FA5DF680F1EA700CA5712F7B61533CE17C582FD580578F2"
V25_REJECTED_SHA256 = "4E0F7970D659CF569BD99E7EBDDBF41F3590E1DFEC615A6CDD6F5498F9BFE61D"


class PreflightFailure(RuntimeError):
    """A fail-closed certificate or source-policy failure."""


class O4ScheduleViolation(PreflightFailure):
    """An operator request outside the canonical fourth-order schedule."""


class O4OccurrenceViolation(PreflightFailure):
    """A local Haar request outside the executed fourth-order corpus."""


@dataclass(frozen=True)
class Provenance:
    consumer: str
    requested_order: int
    source_layer: int
    target_layer: int
    source_index: int | None = None
    target_index: int | None = None
    source_name: str | None = None
    target_name: str | None = None
    h0_key: str | None = None
    link: int | str | None = None
    source_state: str | None = None
    target_state: str | None = None
    action: str = "W"


@dataclass(frozen=True)
class BasisRecord:
    state: Any
    key: Any
    layer: int
    name: str


@dataclass
class GateBook:
    passed: list[dict[str, Any]]

    def __init__(self) -> None:
        self.passed = []

    def require(self, name: str, condition: bool, detail: Any) -> None:
        if not bool(condition):
            raise PreflightFailure(f"{name}: {detail}")
        self.passed.append({"name": name, "detail": detail})


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest().upper()


def canonical_json(value: Any) -> str:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=True)


def enumerate_closed_layer_walks(order: int) -> tuple[tuple[int, ...], ...]:
    """All nonnegative Motzkin walks of exactly ``order`` steps from P to P."""
    if order < 0:
        raise ValueError("order must be nonnegative")
    walks: list[tuple[int, ...]] = []

    def visit(path: tuple[int, ...]) -> None:
        used = len(path) - 1
        if used == order:
            if path[-1] == P:
                walks.append(path)
            return
        here = path[-1]
        for nxt in (here - 1, here, here + 1):
            if nxt < 0:
                continue
            # Returning to P needs at least ``nxt`` remaining downward steps.
            remaining_after = order - used - 1
            if nxt > remaining_after:
                continue
            visit(path + (nxt,))

    visit((P,))
    return tuple(sorted(walks))


def walk_blocks(walks: Iterable[Sequence[int]]) -> frozenset[tuple[int, int]]:
    # Matrix convention is (target, source), hence (b, a) for a -> b.
    return frozenset((int(b), int(a)) for w in walks for a, b in zip(w, w[1:]))


def first_closed_order_with_block(block: tuple[int, int], limit: int = 12) -> int | None:
    for order in range(limit + 1):
        if block in walk_blocks(enumerate_closed_layer_walks(order)):
            return order
    return None


def assert_o4_block(provenance: Provenance) -> None:
    block = (int(provenance.target_layer), int(provenance.source_layer))
    if block not in O4_BLOCKS:
        message = {
            "error": "forbidden O4 magnetic block",
            "requested_block": [LAYER_NAMES.get(block[0], str(block[0])), LAYER_NAMES.get(block[1], str(block[1]))],
            "first_closed_order": first_closed_order_with_block(block),
            "provenance": asdict(provenance),
            "note": "No Haar extension was attempted.",
        }
        raise O4ScheduleViolation(canonical_json(message))


class OccurrenceAuditor:
    def __init__(self) -> None:
        self.counts: Counter[tuple[int, int]] = Counter()

    def observe(self, n_u: int, n_ubar: int, provenance: Provenance) -> str:
        pattern = (int(n_u), int(n_ubar))
        self.counts[pattern] += 1
        if pattern in FORBIDDEN_O4_PATTERNS:
            payload = {
                "error": "forbidden seven-factor occurrence at O4",
                "pattern": list(pattern),
                "provenance": asdict(provenance),
                "note": "This is an upstream order-schedule failure. No Haar extension was attempted.",
            }
            raise O4OccurrenceViolation(canonical_json(payload))
        if sum(pattern) > 6:
            payload = {
                "error": "O4 local occurrence bound exceeded",
                "pattern": list(pattern),
                "provenance": asdict(provenance),
                "note": "No Haar extension was attempted.",
            }
            raise O4OccurrenceViolation(canonical_json(payload))
        if (pattern[0] - pattern[1]) % 3:
            return "center-zero"
        if pattern not in APPROVED_CENTER_NEUTRAL_PATTERNS:
            payload = {
                "error": "center-neutral occurrence absent from executed v10a2 corpus",
                "pattern": list(pattern),
                "provenance": asdict(provenance),
                "note": "No Haar extension was attempted.",
            }
            raise O4OccurrenceViolation(canonical_json(payload))
        return "contract"


def _normalize_pattern_record(record: Any) -> tuple[Any, int, int]:
    if isinstance(record, Mapping):
        return record.get("link"), int(record["n_u"]), int(record["n_ubar"])
    if len(record) != 3:
        raise ValueError("pattern records must be (link, n_u, n_ubar)")
    return record[0], int(record[1]), int(record[2])


def assemble_o4_hermitian_matrix(
    basis: Sequence[BasisRecord],
    apply_w: Callable[[Any], Any],
    split_h0: Callable[[Any], Mapping[Any, Any]],
    occurrence_patterns: Callable[[Any, Any], Iterable[Any]],
    inner: Callable[[Any, Any], float],
    *,
    consumer: str = "canonical-o4-assembler",
) -> tuple[list[list[float]], dict[str, Any]]:
    """Build PP/P1/11/12 once and obtain reverse blocks by Hermiticity.

    W is applied only to P and Q1 source columns.  A Q2 source is never sent to
    ``apply_w``.  Occurrences are inspected before ``inner`` can call Haar.
    """
    rows = [BasisRecord(x.state, x.key, int(x.layer), str(x.name)) for x in basis]
    if not rows:
        raise ValueError("basis is empty")
    if any(x.layer not in (P, Q1, Q2) for x in rows):
        raise O4ScheduleViolation("basis contains a layer outside P/Q1/Q2")

    by_layer_key: dict[tuple[int, Any], list[int]] = defaultdict(list)
    for index, row in enumerate(rows):
        by_layer_key[(row.layer, row.key)].append(index)

    n = len(rows)
    matrix = [[0.0 for _ in range(n)] for _ in range(n)]
    auditor = OccurrenceAuditor()
    applied_source_layers: list[int] = []
    computed: list[tuple[int, int]] = []

    for source_index, source in enumerate(rows):
        if source.layer == Q2:
            continue
        applied_source_layers.append(source.layer)
        generated = apply_w(source.state)
        target_layers = (P, Q1) if source.layer == P else (Q1, Q2)
        for key, block_state in split_h0(generated).items():
            for target_layer in target_layers:
                for target_index in by_layer_key.get((target_layer, key), ()):
                    target = rows[target_index]
                    # Same-layer elements are computed in one triangle only.
                    if target.layer == source.layer and target_index < source_index:
                        continue
                    provenance = Provenance(
                        consumer=consumer,
                        requested_order=ORDER,
                        source_layer=source.layer,
                        target_layer=target.layer,
                        source_index=source_index,
                        target_index=target_index,
                        source_name=source.name,
                        target_name=target.name,
                        h0_key=repr(key),
                        source_state=repr(source.state),
                        target_state=repr(target.state),
                    )
                    assert_o4_block(provenance)
                    for record in occurrence_patterns(target.state, block_state):
                        link, n_u, n_ubar = _normalize_pattern_record(record)
                        auditor.observe(n_u, n_ubar, Provenance(**{**asdict(provenance), "link": link}))
                    value = float(inner(target.state, block_state))
                    matrix[target_index][source_index] = value
                    matrix[source_index][target_index] = value
                    computed.append((target.layer, source.layer))

    if Q2 in applied_source_layers:
        raise O4ScheduleViolation("internal error: W was applied to a Q2 source")
    q2_indices = [i for i, x in enumerate(rows) if x.layer == Q2]
    if any(matrix[i][j] != 0.0 for i in q2_indices for j in q2_indices):
        raise O4ScheduleViolation("internal error: W22 is nonzero")
    return matrix, {
        "applied_source_layers": applied_source_layers,
        "computed_direct_blocks": sorted(set(computed)),
        "occurrence_counts": {f"{a},{b}": n for (a, b), n in sorted(auditor.counts.items())},
        "w22_exactly_zero": True,
    }


def _fraction_gelfand_scalar(
    h0: Sequence[Fraction], v: Sequence[Sequence[Fraction]], order: int
) -> tuple[Fraction, ...]:
    """Identity-normalized scalar-P recurrence, using exact rational arithmetic."""
    dim = len(h0)
    if dim < 2 or any(len(row) != dim for row in v):
        raise ValueError("invalid exact one-face model")
    psi = [[Fraction(0) for _ in range(dim)] for _ in range(order + 1)]
    heff = [Fraction(0) for _ in range(order + 1)]
    psi[0][0] = Fraction(1)
    heff[0] = h0[0]
    for k in range(1, order + 1):
        heff[k] = sum(v[0][j] * psi[k - 1][j] for j in range(dim))
        for i in range(1, dim):
            rhs = sum(v[i][j] * psi[k - 1][j] for j in range(dim))
            rhs -= sum(psi[j][i] * heff[k - j] for j in range(1, k))
            psi[k][i] = rhs / (h0[0] - h0[i])
    return tuple(heff)


def exact_one_face_w22_sensitivity() -> dict[str, Any]:
    f = Fraction
    h0 = (f(8, 3), f(20, 3), f(12), f(32, 3))
    layers = (P, Q1, Q2, Q2)
    full = (
        (f(1), -f(1), f(0), f(0)),
        (-f(1), f(0), -f(1), -f(1)),
        (f(0), -f(1), f(0), -f(1)),
        (f(0), -f(1), -f(1), f(1)),
    )
    pruned = tuple(
        tuple(f(0) if layers[i] == Q2 and layers[j] == Q2 else full[i][j] for j in range(4))
        for i in range(4)
    )
    efull = _fraction_gelfand_scalar(h0, full, 5)
    epruned = _fraction_gelfand_scalar(h0, pruned, 5)
    return {
        "full": efull,
        "pruned": epruned,
        "o4_equal": efull[:5] == epruned[:5],
        "o5_difference": efull[5] - epruned[5],
    }


def _notebook_code_and_output(path: Path) -> tuple[dict[str, Any], str, str]:
    raw = path.read_bytes()
    if sha256_bytes(raw) != V10A2_NOTEBOOK_SHA256:
        raise PreflightFailure(
            f"v10a2 notebook hash mismatch: {sha256_bytes(raw)} != {V10A2_NOTEBOOK_SHA256}"
        )
    notebook = json.loads(raw.decode("utf-8"))
    code_cells = [cell for cell in notebook.get("cells", []) if cell.get("cell_type") == "code"]
    if len(code_cells) != 1:
        raise PreflightFailure(f"expected one v10a2 code cell, found {len(code_cells)}")
    cell = code_cells[0]
    code = "".join(cell.get("source", []))
    if sha256_bytes(code.encode("utf-8")) != V10A2_CODE_SHA256:
        raise PreflightFailure("v10a2 code-cell hash mismatch")
    chunks: list[str] = []
    for output in cell.get("outputs", []):
        text = output.get("text")
        if isinstance(text, list):
            chunks.append("".join(text))
        elif isinstance(text, str):
            chunks.append(text)
        plain = output.get("data", {}).get("text/plain")
        if isinstance(plain, list):
            chunks.append("".join(plain))
        elif isinstance(plain, str):
            chunks.append(plain)
    return cell, code, "".join(chunks)


def _parse_tuple_after(label: str, output: str) -> tuple[tuple[int, int], ...]:
    match = re.search(rf"^{re.escape(label)}\s*:\s*(.+)$", output, re.MULTILINE)
    if not match:
        raise PreflightFailure(f"missing stored output field: {label}")
    value = ast.literal_eval(match.group(1).strip())
    return tuple(tuple(map(int, item)) for item in value)


def audit_executed_v10a2(path: Path, gates: GateBook) -> dict[str, Any]:
    cell, code, output = _notebook_code_and_output(path)
    gates.require("v10a2 stored execution count is one", cell.get("execution_count") == 1, cell.get("execution_count"))
    gates.require("v10a2 stored gate summary is 17/17", "PASSED 17/17 v10a.2 GATES" in output, "summary present")

    tree = ast.parse(code)
    called = {
        node.func.id
        for node in ast.walk(tree)
        if isinstance(node, ast.Call) and isinstance(node.func, ast.Name)
    }
    gates.require(
        "v10a2 frontier census is actually called",
        "_v10a2_q2_frontier_census" in called,
        "driver call found",
    )

    patterns = _parse_tuple_after("observed Q2 pair Haar patterns", output)
    gates.require(
        "stored v10a2 center-neutral pattern set is exact",
        frozenset(patterns) == APPROVED_CENTER_NEUTRAL_PATTERNS,
        patterns,
    )
    gates.require(
        "stored v10a2 pattern set excludes the forbidden pair",
        set(patterns).isdisjoint(FORBIDDEN_O4_PATTERNS),
        sorted(FORBIDDEN_O4_PATTERNS),
    )
    gates.require("stored v10a2 local words have at most six factors", max(sum(x) for x in patterns) <= 6, max(sum(x) for x in patterns))

    expected_fragments = {
        "raw_second_actions": "raw second magnetic actions        : 64,272",
        "new_q2": "'new-Q2': 52608",
        "unique_networks": "unique canonical frontier networks : 4,524",
        "pair_tests": "pair-overlap tests / flux groups   : 41,266 / 520",
    }
    for name, fragment in expected_fragments.items():
        gates.require(f"stored v10a2 {name} fixture matches", fragment in output, fragment)
    gates.require(
        "stored v10a2 occurrence support gate passed",
        "[PASS] v10a.2 every observed Q2 pair Haar signature is explicitly supported :: ()" in output,
        "unsupported=()",
    )
    return {
        "notebook": str(path.resolve()),
        "notebook_sha256": V10A2_NOTEBOOK_SHA256,
        "code_sha256": V10A2_CODE_SHA256,
        "patterns": [list(x) for x in patterns],
        "raw_second_actions": 64272,
        "new_q2": 52608,
        "unique_canonical_networks": 4524,
        "pair_tests": 41266,
        "flux_groups": 520,
    }


def self_policy_audit(gates: GateBook) -> dict[str, Any]:
    """Prove this runner has no alternate-oracle or unblinding machinery."""
    source = Path(__file__).read_text(encoding="utf-8")
    tree = ast.parse(source)
    symbols = {node.id for node in ast.walk(tree) if isinstance(node, ast.Name)}
    symbols.update(node.name for node in ast.walk(tree) if isinstance(node, (ast.FunctionDef, ast.ClassDef)))
    imported_roots: set[str] = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            imported_roots.update(alias.name.split(".", 1)[0] for alias in node.names)
        elif isinstance(node, ast.ImportFrom) and node.module:
            imported_roots.add(node.module.split(".", 1)[0])
    prohibited_symbols = {
        "M4_ORACLE",
        "local_shift",
        "_HAMER_X4",
        "_HAMER_U4",
        "_v25_gelfand_series",
        "_v23c_fit_cluster",
        "Factor52",
    }
    prohibited_imports = {"cupy", "opt_einsum", "scipy", "sympy"}
    gates.require(
        "preflight contains no alternate-oracle or unblind symbols",
        symbols.isdisjoint(prohibited_symbols),
        sorted(symbols & prohibited_symbols),
    )
    gates.require(
        "quick preflight uses only standard-library dependencies",
        imported_roots.isdisjoint(prohibited_imports),
        sorted(imported_roots),
    )
    return {
        "source_sha256": sha256_bytes(source.encode("utf-8")),
        "prohibited_symbols_present": sorted(symbols & prohibited_symbols),
        "prohibited_imports_present": sorted(imported_roots & prohibited_imports),
    }


def replay_v10a2(path: Path, gates: GateBook, verbose: bool = False) -> dict[str, Any]:
    """Execute the exact hashed v10a2 code cell and inspect live objects."""
    _, code, _ = _notebook_code_and_output(path)
    namespace: dict[str, Any] = {"__name__": "__main__"}
    transcript = io.StringIO()
    with contextlib.redirect_stdout(transcript):
        exec(compile(code, str(path) + "#code-cell", "exec"), namespace, namespace)
    text = transcript.getvalue()
    if verbose:
        print(text, end="")

    gate_start = int(namespace["V10A2_GATE_START"])
    live_gates = namespace["gates"][gate_start:]
    gates.require("fresh v10a2 replay is 17/17", len(live_gates) == 17 and all(ok for _, ok, _ in live_gates), f"{sum(ok for _, ok, _ in live_gates)}/{len(live_gates)}")
    front = namespace["front"]
    patterns = tuple(tuple(map(int, x)) for x in front["pair_patterns"])
    gates.require("fresh replay pattern set is exact", frozenset(patterns) == APPROVED_CENTER_NEUTRAL_PATTERNS, patterns)
    gates.require("fresh replay has no forbidden occurrence", set(patterns).isdisjoint(FORBIDDEN_O4_PATTERNS), patterns)
    gates.require("fresh replay new-Q2 count is exact", front["classes"].get("new-Q2") == 52608, front["classes"])
    gates.require("fresh replay canonical-network count is exact", front["unique_candidates"] == 4524, front["unique_candidates"])
    gates.require("fresh replay P-subtracted E0 residual passes", namespace["res"]["residual_norm2_max"] < 2e-12, namespace["res"]["residual_norm2_max"])
    return {
        "gate_count": len(live_gates),
        "patterns": [list(x) for x in patterns],
        "classes": dict(front["classes"]),
        "unique_canonical_networks": int(front["unique_candidates"]),
        "residual_norm2_max": float(namespace["res"]["residual_norm2_max"]),
        "transcript_sha256": sha256_bytes(text.encode("utf-8")),
    }


def poison_access_regression(gates: GateBook) -> dict[str, Any]:
    basis = (
        BasisRecord({"layer": P}, "E0", P, "P0"),
        BasisRecord({"layer": Q1}, "E1", Q1, "Q1"),
        BasisRecord({"layer": Q2}, "E2", Q2, "Q2"),
    )
    calls: list[int] = []

    def apply_w(state: Mapping[str, int]) -> dict[str, Any]:
        layer = int(state["layer"])
        calls.append(layer)
        if layer == Q2:
            raise AssertionError("poison W22 callback was reached")
        return {"source_layer": layer}

    def split_h0(generated: Mapping[str, int]) -> dict[str, Any]:
        return ({"E0": generated, "E1": generated} if generated["source_layer"] == P else {"E1": generated, "E2": generated})

    matrix, report = assemble_o4_hermitian_matrix(
        basis,
        apply_w,
        split_h0,
        lambda _a, _b: ((0, 1, 1),),
        lambda _a, _b: 1.0,
        consumer="poison-access-regression",
    )
    gates.require("O4 assembler never applies W to Q2", calls == [P, Q1], calls)
    gates.require(
        "O4 assembler computes only the canonical one-sided blocks",
        set(map(tuple, report["computed_direct_blocks"])) == DIRECTLY_COMPUTED_BLOCKS,
        report["computed_direct_blocks"],
    )
    gates.require("O4 assembler leaves W22 exactly zero", matrix[2][2] == 0.0 and report["w22_exactly_zero"], matrix)
    gates.require("O4 assembler reflects W21 to W12", matrix[2][1] == matrix[1][2] == 1.0, matrix)
    return report


def negative_provenance_regression(gates: GateBook) -> dict[str, Any]:
    provenance = Provenance(
        consumer="negative-control",
        requested_order=ORDER,
        source_layer=Q2,
        target_layer=Q2,
        source_index=7,
        target_index=9,
        source_name="Q2-source",
        target_name="Q2-target",
        h0_key="exact-test-key",
        link=12,
        source_state="source-LXState",
        target_state="target-LXState",
    )
    try:
        OccurrenceAuditor().observe(2, 5, provenance)
    except O4OccurrenceViolation as exc:
        message = str(exc)
    else:
        raise PreflightFailure("negative occurrence mutation did not fail")
    gates.require("forbidden occurrence fails with provenance", all(token in message for token in ("2,5", "source-LXState", "link", "No Haar extension")), message)

    try:
        assert_o4_block(provenance)
    except O4ScheduleViolation as exc:
        schedule_message = str(exc)
    else:
        raise PreflightFailure("negative W22 mutation did not fail")
    gates.require("forbidden W22 fails before Haar", all(token in schedule_message for token in ("Q2", "first_closed_order", "No Haar extension")), schedule_message)
    return {"occurrence_error": message, "schedule_error": schedule_message}


def audit_rejected_v25(path: Path, gates: GateBook) -> dict[str, Any]:
    raw = path.read_bytes()
    digest = sha256_bytes(raw)
    gates.require("rejected v25 identity is exact", digest == V25_REJECTED_SHA256, digest)
    notebook = json.loads(raw.decode("utf-8"))
    code = "".join(next(cell for cell in notebook["cells"] if cell.get("cell_type") == "code")["source"])
    tree = ast.parse(code)
    function = next(
        node for node in ast.walk(tree) if isinstance(node, ast.FunctionDef) and node.name == "_v23c_build_basis"
    )
    bad_loop = False
    for node in ast.walk(function):
        if not isinstance(node, ast.For) or not isinstance(node.iter, ast.Call):
            continue
        if isinstance(node.iter.func, ast.Name) and node.iter.func.id == "enumerate":
            if node.iter.args and isinstance(node.iter.args[0], ast.Name) and node.iter.args[0].id == "basis":
                calls = [
                    x for x in ast.walk(node) if isinstance(x, ast.Call) and isinstance(x.func, ast.Name) and x.func.id == "_v23c_applyW"
                ]
                if calls:
                    bad_loop = True
    gates.require("negative control detects v25 all-basis W loop", bad_loop, "W applied to enumerate(basis), including Q2")
    return {"path": str(path.resolve()), "sha256": digest, "all_basis_w_loop_detected": bad_loop}


def run(args: argparse.Namespace) -> dict[str, Any]:
    gates = GateBook()

    policy_result = self_policy_audit(gates)

    o4_walks = enumerate_closed_layer_walks(ORDER)
    o5_walks = enumerate_closed_layer_walks(5)
    gates.require("exactly nine closed four-step layer walks", len(o4_walks) == 9, len(o4_walks))
    gates.require("O4 layer walks reach no deeper than Q2", max(max(w) for w in o4_walks) == Q2, o4_walks)
    gates.require("O4 walk-derived block schedule is exact", walk_blocks(o4_walks) == O4_BLOCKS, sorted(walk_blocks(o4_walks)))
    gates.require("no O4 closed walk contains W22", all((Q2, Q2) not in tuple(zip(w, w[1:])) for w in o4_walks), o4_walks)
    gates.require("W22 first enters a closed walk at order five", first_closed_order_with_block((Q2, Q2)) == 5, first_closed_order_with_block((Q2, Q2)))
    gates.require("order-five sensitivity walk exists", (P, Q1, Q2, Q2, Q1, P) in o5_walks, (P, Q1, Q2, Q2, Q1, P))

    exact = exact_one_face_w22_sensitivity()
    gates.require("exact one-face coefficients agree with and without W22 through O4", exact["o4_equal"], [str(x) for x in exact["full"][:5]])
    gates.require("exact one-face O4 coefficient is -13/896", exact["full"][4] == Fraction(-13, 896), str(exact["full"][4]))
    gates.require("exact one-face W22 sensitivity first appears at O5", exact["o5_difference"] == Fraction(-5, 7168), str(exact["o5_difference"]))

    notebook_result = audit_executed_v10a2(args.v10a2_notebook, gates)
    poison_result = poison_access_regression(gates)
    negative_result = negative_provenance_regression(gates)
    replay_result = replay_v10a2(args.v10a2_notebook, gates, args.verbose_replay) if args.replay_baseline else None
    rejected_result = audit_rejected_v25(args.audit_rejected_v25, gates) if args.audit_rejected_v25 else None

    payload: dict[str, Any] = {
        "schema": SCHEMA,
        "status": "PASS",
        "scope": "M3 O4 order schedule and occurrence preflight only; no m4 or publication claim",
        "order": ORDER,
        "closed_o4_walks": [list(w) for w in o4_walks],
        "allowed_blocks": [[a, b] for a, b in sorted(O4_BLOCKS)],
        "forbidden_blocks": [[P, Q2], [Q2, P], [Q2, Q2]],
        "w22_first_closed_order": 5,
        "approved_patterns": [list(x) for x in sorted(APPROVED_CENTER_NEUTRAL_PATTERNS)],
        "forbidden_patterns": [list(x) for x in sorted(FORBIDDEN_O4_PATTERNS)],
        "exact_one_face": {
            "full": [str(x) for x in exact["full"]],
            "w22_pruned": [str(x) for x in exact["pruned"]],
            "o5_difference": str(exact["o5_difference"]),
        },
        "executed_v10a2": notebook_result,
        "fresh_replay": replay_result,
        "poison_access": poison_result,
        "negative_controls": negative_result,
        "source_policy": policy_result,
        "rejected_v25_audit": rejected_result,
        "gates": gates.passed,
        "claims_not_made": [
            "physical m4",
            "complete 3895-topology corpus",
            "189-record production kernel",
            "historical agreement",
            "publication readiness",
        ],
    }
    payload["certificate_id"] = sha256_bytes(canonical_json(payload).encode("utf-8"))
    return payload


def default_v10a2_path() -> Path:
    return Path(__file__).resolve().parent / "sources" / "NB_O4_hodge_v10a2_fullt1_k2_q2_frontier_a100.ipynb"


def parse_args(argv: Sequence[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--v10a2-notebook", type=Path, default=default_v10a2_path())
    parser.add_argument("--replay-baseline", action="store_true", help="freshly execute the exact hashed v10a2 code cell (about 90 seconds on this CPU)")
    parser.add_argument("--verbose-replay", action="store_true", help="print the full v10a2 transcript during a fresh replay")
    parser.add_argument("--audit-rejected-v25", type=Path, help="optional negative-control audit of the known rejected v25 notebook")
    parser.add_argument("--json-out", type=Path, help="write the deterministic JSON certificate atomically")
    return parser.parse_args(argv)


def main(argv: Sequence[str] | None = None) -> int:
    args = parse_args(argv)
    try:
        payload = run(args)
        text = json.dumps(payload, indent=2, sort_keys=True, ensure_ascii=True)
        if args.json_out:
            destination = args.json_out.resolve()
            destination.parent.mkdir(parents=True, exist_ok=True)
            temporary = destination.with_suffix(destination.suffix + ".tmp")
            temporary.write_text(text + "\n", encoding="utf-8")
            os.replace(temporary, destination)
        print(text)
        print(f"\nM3 PREFLIGHT PASS: {len(payload['gates'])}/{len(payload['gates'])} required gates")
        print("GPU AUTHORIZATION: BLOCKED (this certificate closes schedule/occurrence preflight only)")
        return 0
    except Exception as exc:
        print("M3 PREFLIGHT FAILED", file=sys.stderr)
        print(f"{type(exc).__name__}: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
