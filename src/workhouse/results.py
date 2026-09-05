"""Curated analytic results and their explicitly bounded verification support.

This register records mathematical status separately from verification tier.
A pinned proof and a finite control do not turn the full analytic statement
into a symbolic or Lean theorem. Catalogue generation keeps every result T3.
"""

from __future__ import annotations

import hashlib
import re
from pathlib import Path
from typing import Any

import yaml

from .constants import EVIDENCE, STATUSES

ROOT = Path(__file__).resolve().parents[2]
SOURCE = ROOT / "ledger" / "results.yaml"
_RESULT_ID = re.compile(r"RESULT:[A-Za-z0-9][A-Za-z0-9_.-]*\Z")
_PREFIXES = frozenset(
    {
        "RESULT",
        "CHK",
        "LEAN",
        "RUN",
        "CITE",
        "CONST",
        "DOC",
        "CORPUS",
        "ARCHIVE",
        "NOTE",
        "LIT",
        "ADR",
        "ROUTE",
    }
)


def _nonempty(value: Any) -> bool:
    return isinstance(value, str) and bool(value.strip())


def is_catalogue_id(value: Any) -> bool:
    """Recognize full id spelling; actual endpoints resolve in graph.validate."""
    if not _nonempty(value) or "\n" in value or "\r" in value:
        return False
    if re.fullmatch(r"[CGRU]\d+", value):
        return True
    prefix, separator, suffix = value.partition(":")
    return bool(separator and prefix in _PREFIXES and suffix.strip())


def validate(rows: list[dict[str, Any]], root: Path | None = None) -> list[str]:
    """Structural validation, including proof bytes; never a truth adjudication."""
    base = root or ROOT
    aliases_doc = yaml.safe_load((base / "ledger" / "documents.yaml").read_text(encoding="utf-8"))
    aliases = aliases_doc["aliases"]
    paper = (base / "paper").resolve()
    pins: dict[str, list[str]] = {}
    for line in (paper / "SHA256SUMS").read_text(encoding="utf-8").splitlines():
        if not line.strip() or line.startswith("#"):
            continue
        digest, relative = line.split(maxsplit=1)
        pins.setdefault(relative.strip(), []).append(digest)

    problems: list[str] = []
    seen: set[str] = set()
    for row in rows:
        if not isinstance(row, dict):
            problems.append("result entry must be a mapping")
            continue
        rid = row.get("id")
        label = str(rid)
        if not isinstance(rid, str) or not _RESULT_ID.fullmatch(rid):
            problems.append(f"{label}: malformed RESULT id")
        elif rid in seen:
            problems.append(f"{label}: duplicate id")
        else:
            seen.add(rid)
        for field in ("statement", "scope", "source_section"):
            if not _nonempty(row.get(field)):
                problems.append(f"{label}: {field} must be a nonempty string")
        for field, vocabulary in (("status", STATUSES), ("evidence", EVIDENCE)):
            if not isinstance(row.get(field), str) or row[field] not in vocabulary:
                problems.append(f"{label}: unknown {field} {row.get(field)!r}")
        hypotheses = row.get("hypotheses")
        if (
            not isinstance(hypotheses, list)
            or not hypotheses
            or not all(map(_nonempty, hypotheses))
        ):
            problems.append(f"{label}: hypotheses must be a nonempty list of nonempty strings")
        for field in ("depends_on", "bears_on"):
            refs = row.get(field)
            if not isinstance(refs, list) or not all(map(is_catalogue_id, refs)):
                problems.append(f"{label}: {field} must be a list of full catalogue ids")
        support = row.get("supported_by")
        if not isinstance(support, list):
            problems.append(f"{label}: supported_by must be a list")
        else:
            for item in support:
                if not isinstance(item, dict):
                    problems.append(f"{label}: supported_by entry must be a mapping")
                    continue
                target = item.get("target")
                if not is_catalogue_id(target) or not target.startswith(("CHK:", "LEAN:", "RUN:")):
                    problems.append(
                        f"{label}: supported_by target must be a full CHK, LEAN or RUN id"
                    )
                if not _nonempty(item.get("scope")):
                    problems.append(f"{label}: supported_by scope must be a nonempty string")

        source = row.get("source")
        matches = [a for a in aliases if source == f"CITE:{a['alias']}"]
        if len(matches) != 1 or matches[0].get("unresolved") or not matches[0].get("path"):
            problems.append(f"{label}: source {source!r} must resolve to one document alias")
            continue
        path = (base / matches[0]["path"]).resolve()
        if not path.is_relative_to(paper) or not path.is_file():
            problems.append(f"{label}: source must be an existing paper file")
            continue
        relative = path.relative_to(paper).as_posix()
        digests = pins.get(relative, [])
        if len(digests) != 1 or digests[0] != hashlib.sha256(path.read_bytes()).hexdigest():
            problems.append(
                f"{label}: source {relative} has no unique matching paper/SHA256SUMS pin"
            )
    return problems


def load(path: Path | None = None, *, root: Path | None = None) -> list[dict[str, Any]]:
    """Read results/v1, rejecting malformed records before catalogue generation."""
    target = path or SOURCE
    document = yaml.safe_load(target.read_text(encoding="utf-8"))
    if not isinstance(document, dict) or document.get("schema") != "results/v1":
        raise ValueError("result register must use schema results/v1")
    rows = document.get("results")
    if not isinstance(rows, list):
        raise ValueError("result register results must be a list")
    if problems := validate(rows, root=root):
        raise ValueError("invalid result register:\n" + "\n".join(problems))
    return rows


def detail(row: dict[str, Any]) -> str:
    """Preserve every hypothesis and verification boundary in the catalogue."""
    parts = [f"Hypotheses: {'; '.join(row['hypotheses'])}", f"Scope: {row['scope']}"]
    parts.extend(f"Support {s['target']}: {s['scope']}" for s in row["supported_by"])
    return "\n".join(parts)
