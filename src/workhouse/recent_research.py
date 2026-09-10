"""Source-pinned September research results in the native claim graph.

The registry preserves authored mathematical statements, their assumptions,
claim status and evidence level. Its T3 means that the whole statement is not
a registered machine check; it does not demote an analytic proof to prose-only.
Native invariant and Lean nodes can separately certify their precise scope.

Sources are byte-preserved inside this checkout. Original absolute paths are
provenance only, never inputs to loading or verification. No catalogue, CLI,
invariant collector or graph builder is imported here.
"""

from __future__ import annotations

import hashlib
import re
from dataclasses import dataclass
from fractions import Fraction
from pathlib import Path, PurePosixPath
from typing import Any

import yaml

from .constants import EVIDENCE, STATUSES

ROOT = Path(__file__).resolve().parents[2]
REGISTRY = "ledger/recent_research.yaml"
SOURCE_BASE = "runs/recent_research_integration_2026-09-09/sources/"
SOURCE_BASES = (
    SOURCE_BASE,
    "runs/w6_bg_budget_2026-09-10/sources/",
    "runs/m10_conditional_transport_2026-09-10/sources/",
)
SCHEMA = "recent-research/v1"
LINK_TYPES = frozenset(
    {"depends_on", "bears_on", "supported_by", "cannot_decide", "closed_by", "plans"}
)
NODE_ID = re.compile(r"^(?:RESULT|ROUTE):[A-Za-z0-9][A-Za-z0-9:_.-]*$")
SOURCE_ID = re.compile(r"^DOC:RECENT:[A-Za-z0-9][A-Za-z0-9:_.-]*$")
HASH = re.compile(r"^[0-9a-f]{64}$")


@dataclass
class Research:
    title: str
    source: str
    sources: list[dict[str, Any]]
    nodes: list[dict[str, Any]]


def load(path: Path | None = None, *, root: Path | None = None) -> Research:
    """Load the dedicated registry without importing or executing its sources."""
    root = root or ROOT
    path = path or root / REGISTRY
    data = yaml.safe_load(path.read_text(encoding="utf-8"))
    if not isinstance(data, dict) or data.get("schema") != SCHEMA:
        raise ValueError(f"{path}: expected schema {SCHEMA}")
    if not isinstance(data.get("title"), str) or not data["title"].strip():
        raise ValueError(f"{path}: title is required")
    for field in ("sources", "nodes"):
        if not isinstance(data.get(field), list):
            raise ValueError(f"{path}: {field} must be a list")
    try:
        source = path.resolve().relative_to(root.resolve()).as_posix()
    except ValueError:
        source = path.as_posix()
    return Research(data["title"], source, data["sources"], data["nodes"])


def _nonempty(value: Any) -> bool:
    return isinstance(value, str) and bool(value.strip())


def validate(
    research: Research | None = None,
    *,
    root: Path | None = None,
    known_ids: set[str] | None = None,
    verify_sources: bool = True,
) -> list[str]:
    """Validate curation and preserved bytes, never the truth of a source proof.

    ``known_ids`` optionally resolves native graph targets against a caller's
    existing catalogue. All internal targets are resolved unconditionally.
    """
    root = root or ROOT
    research = research if research is not None else load(root=root)
    problems: list[str] = []
    sources: dict[str, dict] = {}
    texts: dict[str, str] = {}
    for item in research.sources:
        if not isinstance(item, dict):
            problems.append("source must be a mapping")
            continue
        sid = item.get("id")
        if not isinstance(sid, str) or not SOURCE_ID.fullmatch(sid):
            problems.append(f"source {sid!r}: invalid stable source id")
            continue
        if sid in sources:
            problems.append(f"{sid}: duplicate source id")
        sources[sid] = item
        for field in ("path", "original_path", "title"):
            if not _nonempty(item.get(field)):
                problems.append(f"{sid}: missing {field}")
        digest = item.get("sha256", "")
        if not isinstance(digest, str) or not HASH.fullmatch(digest):
            problems.append(f"{sid}: invalid sha256")
        path = item.get("path", "")
        if not isinstance(path, str):
            continue
        relative = PurePosixPath(path)
        if (
            not path.startswith(SOURCE_BASES)
            or relative.is_absolute()
            or ".." in relative.parts
            or "\\" in path
        ):
            problems.append(f"{sid}: source path must stay inside the preserved source bundle")
            continue
        target = root / path
        if not target.resolve().is_relative_to(root.resolve()):
            problems.append(f"{sid}: source resolves outside the checkout")
            continue
        if verify_sources:
            try:
                contents = target.read_bytes()
            except OSError as error:
                problems.append(f"{sid}: unavailable preserved source: {error}")
                continue
            if hashlib.sha256(contents).hexdigest() != digest:
                problems.append(f"{sid}: source SHA-256 mismatch")
            if len(contents) != item.get("bytes"):
                problems.append(f"{sid}: source byte count mismatch")
            texts[sid] = contents.decode("utf-8-sig", errors="replace")

    internal: set[str] = set(sources)
    seen: set[str] = set()
    for node in research.nodes:
        if isinstance(node, dict) and isinstance(node.get("id"), str):
            internal.add(node["id"])
    for node in research.nodes:
        if not isinstance(node, dict):
            problems.append("research node must be a mapping")
            continue
        nid = node.get("id")
        if not isinstance(nid, str) or not NODE_ID.fullmatch(nid):
            problems.append(f"{nid!r}: invalid stable result or route id")
            continue
        if nid in seen:
            problems.append(f"{nid}: duplicate research node id")
        seen.add(nid)
        for field in ("statement", "scope", "detail", "verification"):
            if not _nonempty(node.get(field)):
                problems.append(f"{nid}: missing {field}")
        if node.get("status") not in STATUSES:
            problems.append(f"{nid}: status must use the existing claim vocabulary")
        if node.get("evidence") not in EVIDENCE:
            problems.append(f"{nid}: evidence must use the existing evidence vocabulary")
        if node.get("tier", 3) != 3:
            problems.append(f"{nid}: attach a native check to certify scope; registry tier stays 3")
        if "value" in node:
            try:
                if not isinstance(node["value"], str):
                    raise ValueError("exact values must be strings")
                Fraction(node["value"])
            except (TypeError, ValueError, ZeroDivisionError):
                problems.append(f"{nid}: value must be an exact rational string")
        references = node.get("sources")
        if not isinstance(references, list) or not references:
            problems.append(f"{nid}: at least one located source is required")
            references = []
        reference_keys = set()
        for reference in references:
            if not isinstance(reference, dict):
                problems.append(f"{nid}: source reference must be a mapping")
                continue
            sid = reference.get("id")
            if not isinstance(sid, str) or sid not in sources:
                problems.append(f"{nid}: unresolved source {sid!r}")
            for field in ("locator", "anchor"):
                if not _nonempty(reference.get(field)):
                    problems.append(f"{nid}: source reference has no {field}")
            key = (str(sid), str(reference.get("locator")))
            if key in reference_keys:
                problems.append(f"{nid}: duplicate source locator {key}")
            reference_keys.add(key)
            anchor = reference.get("anchor")
            if sid in texts and _nonempty(anchor) and anchor not in texts[sid]:
                problems.append(f"{nid}: source anchor absent from {sid}")
        links = node.get("links", [])
        if not isinstance(links, list):
            problems.append(f"{nid}: links must be a list")
            links = []
        link_keys = set()
        for link in links:
            if not isinstance(link, dict):
                problems.append(f"{nid}: link must be a mapping")
                continue
            target, kind = link.get("target"), link.get("type")
            if kind not in LINK_TYPES:
                problems.append(f"{nid}: unsupported relationship {kind!r}")
            if not _nonempty(target):
                problems.append(f"{nid}: link target is required")
            elif target == nid:
                problems.append(f"{nid}: self-dependency is not allowed")
            elif target not in internal and known_ids is not None and target not in known_ids:
                problems.append(f"{nid}: unresolved native target {target!r}")
            elif (
                target.startswith(("RESULT:W6_", "RESULT:RECENT_", "ROUTE:RECENT_"))
                and target not in internal
            ):
                problems.append(f"{nid}: unresolved research target {target!r}")
            if not _nonempty(link.get("detail")):
                problems.append(f"{nid}: link explanation is required")
            key = (str(kind), str(target))
            if key in link_keys:
                problems.append(f"{nid}: duplicate link {key}")
            link_keys.add(key)
    return problems


def claim_records(research: Research | None = None, *, root: Path | None = None) -> list[dict]:
    """Return keyword dictionaries for claims.Claim with no circular imports."""
    root = root or ROOT
    research = research if research is not None else load(root=root)
    problems = validate(research, root=root)
    if problems:
        raise ValueError("recent research problems:\n" + "\n".join(problems))
    sources = {source["id"]: source for source in research.sources}
    records = []
    for source in research.sources:
        records.append(
            dict(
                id=source["id"],
                kind="document",
                statement=source["title"],
                tier=3,
                where=source["path"],
                cites=research.source,
                evidence="record-backed",
                detail=(
                    f"Original: {source['original_path']}\n"
                    f"Preserved SHA-256: {source['sha256']}; bytes: {source['bytes']}. "
                    "Byte identity establishes provenance, not a theorem or a fresh control run."
                ),
            )
        )
    for node in research.nodes:
        refs = node["sources"]
        links = node.get("links", [])
        record = dict(
            id=node["id"],
            kind="route" if node["id"].startswith("ROUTE:") else "result",
            statement=node["statement"],
            tier=3,
            where=f"{research.source}#{node['id']}",
            cites="; ".join(f"{sources[r['id']]['path']} ({r['locator']})" for r in refs),
            status=node["status"],
            evidence=node["evidence"],
            detail="\n".join(
                [node["detail"], "Scope: " + node["scope"], "Verification: " + node["verification"]]
                + [f"{x['type']} {x['target']}: {x['detail']}" for x in links]
            ),
            related=sorted({r["id"] for r in refs} | {x["target"] for x in links}),
        )
        if "value" in node:
            value = Fraction(node["value"])
            record.update(value=str(value), decimal=float(value))
        records.append(record)
    return records


def edge_records(research: Research | None = None, *, root: Path | None = None) -> list[dict]:
    """Return keyword dictionaries for graph.Edge; preserve authored directions."""
    research = research if research is not None else load(root=root)
    records = []
    for node in research.nodes:
        origin = f"{research.source}#{node['id']}"
        for reference in node["sources"]:
            records.append(
                dict(
                    src=node["id"],
                    dst=reference["id"],
                    type="supported_by",
                    how="curated",
                    source=f"{origin}.sources ({reference['locator']})",
                )
            )
        for i, link in enumerate(node.get("links", [])):
            records.append(
                dict(
                    src=node["id"],
                    dst=link["target"],
                    type=link["type"],
                    how="curated",
                    source=f"{origin}.links[{i}]: {link['detail']}",
                )
            )
    return records
