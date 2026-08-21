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

LEDGER_DIR = Path(__file__).resolve().parents[2] / "ledger"

CONTRADICTION_STATUSES = frozenset(
    {"open", "resolved", "falsified", "superseded", "unresolved-in-corpus"}
)
TIERS = frozenset({0, 1, 2, 3})


@dataclass
class Ledgers:
    contradictions: list[dict[str, Any]]
    gaps: list[dict[str, Any]]
    register: list[dict[str, Any]]
    dependency_spine: list[str]
    headline: str

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

    def gaps_by_tier(self, tier: int) -> list[dict[str, Any]]:
        return [g for g in self.gaps if g["tier"] == tier]


def load(directory: Path | None = None) -> Ledgers:
    d = directory or LEDGER_DIR
    contradictions = yaml.safe_load((d / "contradictions.yaml").read_text())
    gaps = yaml.safe_load((d / "gaps.yaml").read_text())
    register = yaml.safe_load((d / "governing_register.yaml").read_text())
    return Ledgers(
        contradictions=contradictions["contradictions"],
        gaps=gaps["gaps"],
        register=register["items"],
        dependency_spine=gaps.get("dependency_spine", []),
        headline=gaps.get("headline", "").strip(),
    )


def validate(ledgers: Ledgers) -> list[str]:
    """Return a list of structural problems. Empty means the ledgers are sound."""
    problems: list[str] = []

    def seq_complete(ids: set[str], prefix: str, label: str) -> None:
        nums = sorted(int(i[1:]) for i in ids if re.fullmatch(rf"{prefix}\d+", i))
        if len(nums) != len(ids):
            problems.append(f"{label}: malformed ids present")
        expected = list(range(1, len(nums) + 1))
        if nums != expected:
            missing = sorted(set(expected) - set(nums))
            problems.append(f"{label}: id sequence has gaps at {missing}")

    seq_complete(ledgers.contradiction_ids, "C", "contradictions")
    seq_complete(ledgers.gap_ids, "G", "gaps")
    seq_complete(ledgers.register_ids, "R", "governing register")

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
        for ref in g.get("resolves", []):
            if ref not in ledgers.contradiction_ids:
                problems.append(f"{g['id']} resolves unknown contradiction {ref}")
        for ref in g.get("depends_on", []) + g.get("unblocks", []):
            if ref not in ledgers.gap_ids:
                problems.append(f"{g['id']} references unknown gap {ref}")

    # Every open contradiction must be reachable from some gap's `resolves`.
    claimed = {r for g in ledgers.gaps for r in g.get("resolves", [])}
    for c in ledgers.open_contradictions:
        if c["id"] not in claimed:
            problems.append(f"{c['id']} is open but no gap claims to resolve it")

    return problems
