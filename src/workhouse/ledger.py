"""Loading and cross-validation of the YAML ledgers.

Three registers, and they are not peers:

* ``governing_register.yaml`` (R1-R23) is a verbatim transcription of the
  governing document's §14. **It is the authority.**
* ``contradictions.yaml`` (C1-C22) transcribes the older ``MASTER_THEORY.md``
  §8 register, which has its own numbering and is not governing. It is kept
  because checks were run against it and its entries carry the numbers.
* ``gaps.yaml`` (G1-G19) is the open-work register.

Validation here is structural: ids well-formed and complete, cross-references
resolving, vocabularies closed. It says nothing about physics.
"""

from __future__ import annotations

import re
from dataclasses import dataclass
from pathlib import Path
from typing import Any

import yaml

from .results import is_catalogue_id

LEDGER_DIR = Path(__file__).resolve().parents[2] / "ledger"

CONTRADICTION_STATUSES = frozenset(
    {"open", "resolved", "falsified", "superseded", "unresolved-in-corpus"}
)
TIERS = frozenset({0, 1, 2, 3})
#: Machine-readable gap lifecycle. The prose stays in `status`; this field is
#: what code reads, because FRONTIER once advertised discharged gaps as open
#: work — the exact "redo finished work" failure mode AGENTS.md warns about.
#: `partial` still counts as open work; only `discharged` leaves the queue.
GAP_STATES = frozenset({"open", "partial", "discharged"})
#: Machine-readable state of one plan step (a route) under a gap. The prose
#: stays in the step's `status`; this field is what `why` and the frontier
#: read. `dead` is the one that earns the field: a route closed by a run or a
#: finding must stop reading as open work, because G3's sealed sweep was
#: re-attempted by four sessions after it was known to emit only the Gamma
#: scalar. `untried` is a recorded proposal nobody has spent anything on yet.
ROUTE_STATES = frozenset({"untried", "live", "dead", "done"})
UNIFYING_STATUSES = frozenset({"conjectured", "supported", "promoted", "refuted"})


@dataclass
class Ledgers:
    contradictions: list[dict[str, Any]]
    gaps: list[dict[str, Any]]
    register: list[dict[str, Any]]
    dependency_spine: list[str]
    headline: str
    unifying_candidates: list[dict[str, Any]]

    @property
    def contradiction_ids(self) -> set[str]:
        return {c["id"] for c in self.contradictions}

    @property
    def gap_ids(self) -> set[str]:
        return {g["id"] for g in self.gaps}

    @property
    def register_ids(self) -> set[str]:
        return {r["id"] for r in self.register}

    def governing(self, contradiction_id: str) -> list[dict[str, Any]]:
        """The register items that state the same claim as a C-id, if any.

        Empty is the common and honest answer: most C-ids have no verbatim
        counterpart, and the crosswalk refuses to invent one.
        """
        return [r for r in self.register if contradiction_id in r["contradictions"]]

    @property
    def open_contradictions(self) -> list[dict[str, Any]]:
        return [c for c in self.contradictions if c["status"] == "open"]

    @property
    def load_bearing_gaps(self) -> list[dict[str, Any]]:
        return [g for g in self.gaps if g.get("load_bearing")]

    @property
    def open_gaps(self) -> list[dict[str, Any]]:
        """Gaps that still carry work: state open or partial, never discharged."""
        return [g for g in self.gaps if g.get("state", "open") != "discharged"]

    @property
    def open_gap_ids(self) -> set[str]:
        return {g["id"] for g in self.open_gaps}

    @property
    def discharged_gaps(self) -> list[dict[str, Any]]:
        return [g for g in self.gaps if g.get("state") == "discharged"]

    def gaps_by_tier(self, tier: int) -> list[dict[str, Any]]:
        return [g for g in self.gaps if g["tier"] == tier]


def load(directory: Path | None = None) -> Ledgers:
    d = directory or LEDGER_DIR
    contradictions = yaml.safe_load((d / "contradictions.yaml").read_text(encoding="utf-8"))
    gaps = yaml.safe_load((d / "gaps.yaml").read_text(encoding="utf-8"))
    register = yaml.safe_load((d / "governing_register.yaml").read_text(encoding="utf-8"))
    return Ledgers(
        contradictions=contradictions["contradictions"],
        gaps=gaps["gaps"],
        register=register["items"],
        dependency_spine=gaps.get("dependency_spine", []),
        headline=gaps.get("headline", "").strip(),
        unifying_candidates=gaps.get("unifying_candidates", []),
    )


#: Path-valued leaf keys inside ledger entries, at any nesting depth. These are
#: exactly what `workhouse why` hands an agent as the next file to open, so a
#: moved artifact must be a validation failure, not a silent dead end.
PATH_KEYS = frozenset({"artifact", "recorded_in", "leads"})


def _walk_paths(value: Any) -> list[str]:
    """Every string under a PATH_KEYS key, recursively."""
    found: list[str] = []
    if isinstance(value, dict):
        for key, sub in value.items():
            if key in PATH_KEYS:
                items = sub if isinstance(sub, list) else [sub]
                found.extend(str(s) for s in items if isinstance(s, str))
            else:
                found.extend(_walk_paths(sub))
    elif isinstance(value, list):
        for sub in value:
            found.extend(_walk_paths(sub))
    return found


def validate(ledgers: Ledgers) -> list[str]:
    """Return a list of structural problems. Empty means the ledgers are sound."""
    problems: list[str] = []
    root = LEDGER_DIR.parent

    def seq_complete(entries: list[dict[str, Any]], prefix: str, label: str) -> None:
        raw = [e["id"] for e in entries]
        ids = set(raw)
        # Duplicate ids collapse silently in the set views, and every consumer
        # doing `next(g for g in ...)` would then pick one copy at random.
        if len(raw) != len(ids):
            duplicated = sorted({i for i in raw if raw.count(i) > 1})
            problems.append(f"{label}: duplicate ids {duplicated}")
        nums = sorted(int(i[1:]) for i in ids if re.fullmatch(rf"{prefix}\d+", i))
        if len(nums) != len(ids):
            problems.append(f"{label}: malformed ids present")
        expected = list(range(1, len(nums) + 1))
        if nums != expected:
            missing = sorted(set(expected) - set(nums))
            problems.append(f"{label}: id sequence has gaps at {missing}")

    seq_complete(ledgers.contradictions, "C", "contradictions")
    seq_complete(ledgers.gaps, "G", "gaps")
    seq_complete(ledgers.register, "R", "governing register")

    for r in ledgers.register:
        if not r.get("text", "").strip():
            problems.append(f"{r['id']}: empty transcription")
        for ref in r["contradictions"]:
            if ref not in ledgers.contradiction_ids:
                problems.append(f"{r['id']} crosswalks to unknown contradiction {ref}")
        for ref in r["gaps"]:
            if ref not in ledgers.gap_ids:
                problems.append(f"{r['id']} crosswalks to unknown gap {ref}")

    for c in ledgers.contradictions:
        if c["status"] not in CONTRADICTION_STATUSES:
            problems.append(f"{c['id']}: unknown status {c['status']!r}")
        for ref in c.get("blocks", []):
            if ref not in ledgers.gap_ids:
                problems.append(f"{c['id']} blocks unknown gap {ref}")
        # An open contradiction with nobody working on it is how a register rots.
        if c["status"] == "open" and not c.get("blocks"):
            problems.append(f"{c['id']} is open but names no gap that would resolve it")

    for g in ledgers.gaps:
        if g["tier"] not in TIERS:
            problems.append(f"{g['id']}: unknown tier {g['tier']!r}")
        if g.get("state") not in GAP_STATES:
            problems.append(
                f"{g['id']}: state must be one of {sorted(GAP_STATES)}, got {g.get('state')!r}"
            )
        # A discharged verdict needs its evidence in prose; bare enum rots.
        if g.get("state") in ("partial", "discharged") and not str(g.get("status", "")).strip():
            problems.append(f"{g['id']}: state {g['state']} but no status prose recording why")
        for ref in g.get("resolves", []):
            if ref not in ledgers.contradiction_ids:
                problems.append(f"{g['id']} resolves unknown contradiction {ref}")
        for ref in g.get("depends_on", []) + g.get("unblocks", []):
            if ref not in ledgers.gap_ids:
                problems.append(f"{g['id']} references unknown gap {ref}")
        seen_steps: set[str] = set()
        for step in g.get("plan", []) or []:
            label = f"{g['id']} plan step {step.get('step')!r}"
            if not str(step.get("step", "")).strip():
                problems.append(f"{g['id']}: a plan step has no name")
                continue
            if step["step"] in seen_steps:
                problems.append(f"{label}: duplicate step name")
            seen_steps.add(step["step"])
            if step.get("state") not in ROUTE_STATES:
                problems.append(
                    f"{label}: state must be one of {sorted(ROUTE_STATES)}, got "
                    f"{step.get('state')!r}"
                )
            # A closed route names what closed it, or its status prose does;
            # a bare 'dead' is an assertion nobody can audit.
            if step.get("state") in ("dead", "done") and not (
                step.get("closed_by") or str(step.get("status", "")).strip()
            ):
                problems.append(f"{label}: {step['state']} but neither closed_by nor status")
            for ref in step.get("closed_by", []) or []:
                ref = str(ref)
                if re.fullmatch(r"[CG]\d+", ref) and ref not in (
                    ledgers.contradiction_ids | ledgers.gap_ids
                ):
                    problems.append(f"{label}: closed_by unknown {ref}")
                if not (
                    re.fullmatch(r"[CGRU]\d+", ref)
                    or ref.startswith(("RUN:", "CHK:", "RESULT:", "CITE:"))
                    or re.fullmatch(r"ADR[:\s]*\d{4}", ref)
                ):
                    problems.append(
                        f"{label}: closed_by {ref!r} is not a ledger, run, check, "
                        "result, citation or ADR id"
                    )
            dependencies = step.get("depends_on", [])
            if not isinstance(dependencies, list) or not all(map(is_catalogue_id, dependencies)):
                problems.append(f"{label}: depends_on must be a list of full catalogue ids")
            for ref in step.get("cannot_decide", []) or []:
                if ref not in (ledgers.contradiction_ids | ledgers.gap_ids):
                    problems.append(f"{label}: cannot_decide unknown {ref}")

    # Path-valued fields, wherever they nest. Contradictions carry them too.
    for entry in ledgers.gaps + ledgers.contradictions:
        for rel in _walk_paths(entry):
            if not (root / rel).exists():
                problems.append(f"{entry['id']}: path {rel!r} does not exist")

    # The dependency spine renders verbatim into FRONTIER §6; its ids must
    # resolve or a renumbering reads as current forever.
    for line in ledgers.dependency_spine:
        for ref in re.findall(r"\b[CG]\d+\b", str(line)):
            if ref not in (ledgers.contradiction_ids | ledgers.gap_ids):
                problems.append(f"dependency_spine cites unknown {ref}: {line!r}")

    seen_unifying: set[str] = set()
    for uc in ledgers.unifying_candidates:
        if uc["status"] not in UNIFYING_STATUSES:
            problems.append(f"{uc['id']}: unknown status {uc['status']!r}")
        # No falsifier means it is an analogy, and analogies are not candidates.
        if not str(uc.get("falsifier", "")).strip():
            problems.append(f"{uc['id']}: no falsifier — state what would refute it")
        if uc["id"] in seen_unifying:
            problems.append(f"{uc['id']}: duplicate id")
        seen_unifying.add(uc["id"])
        for ref in uc.get("supported_by", []):
            if re.fullmatch(r"[CG]\d+", ref) and ref not in (
                ledgers.contradiction_ids | ledgers.gap_ids
            ):
                problems.append(f"{uc['id']} cites unknown {ref}")

    # Every open contradiction must be reachable from some gap's `resolves`.
    claimed = {r for g in ledgers.gaps for r in g.get("resolves", [])}
    for c in ledgers.open_contradictions:
        if c["id"] not in claimed:
            problems.append(f"{c['id']} is open but no gap claims to resolve it")

    return problems
