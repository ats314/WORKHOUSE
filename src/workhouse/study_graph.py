"""Curated, source-located literature studies inside the native theory graph.

Each ``literature/*/theory_graph.yaml`` uses ``literature-study/v1``. Its
``nodes`` have an explicit ``STUDY:`` id, statement, existing claim status,
detail, and ``sources: [{paper, locator}]``. Optional ``links`` carry
``{type, target, detail}``, with native catalogue ids as targets. Source
membership and links are authored; no semantic relationship is inferred.

These are ordinary note nodes, always T3 and prose-only. A paper's theorem,
a problem requirement and a proposed bridge can all be recorded precisely
without manufacturing a machine check or a new truth vocabulary. This module
never collects the catalogue, so importing it cannot recurse through checks.
"""

from __future__ import annotations

import re
from dataclasses import dataclass
from pathlib import Path
from typing import Any

import yaml

from . import constants as K
from . import literature

ROOT = Path(__file__).resolve().parents[2]
SCHEMA = "literature-study/v1"
LINK_TYPES = frozenset({"depends_on", "bears_on", "supported_by", "cannot_decide"})
NODE_ID = re.compile(r"^STUDY:[A-Za-z0-9][A-Za-z0-9:_.-]*$")


@dataclass
class Study:
    title: str
    source: str
    nodes: list[dict[str, Any]]


def load(paths: list[Path] | None = None) -> list[Study]:
    """Read study files in stable order; an absent collection is empty."""
    paths = (
        paths if paths is not None else sorted((ROOT / "literature").glob("*/theory_graph.yaml"))
    )
    studies = []
    for path in sorted(paths):
        data = yaml.safe_load(path.read_text(encoding="utf-8"))
        if not isinstance(data, dict) or data.get("schema") != SCHEMA:
            raise ValueError(f"{path}: expected schema {SCHEMA}")
        if not isinstance(data.get("title"), str) or not data["title"].strip():
            raise ValueError(f"{path}: study has no title")
        if not isinstance(data.get("nodes"), list):
            raise ValueError(f"{path}: nodes must be a list")
        try:
            source = path.resolve().relative_to(ROOT.resolve()).as_posix()
        except ValueError:
            source = path.as_posix()
        studies.append(Study(data["title"], source, data["nodes"]))
    return studies


def validate(
    studies: list[Study] | None = None,
    *,
    paper_ids: set[str] | None = None,
    known_ids: set[str] | None = None,
) -> list[str]:
    """Validate curation, optionally resolving links against a supplied catalogue.

    The graph builder also checks every endpoint. Callers can supply ids from
    their existing catalogue; this function never rebuilds one to obtain them.
    """
    studies = studies if studies is not None else load()
    paper_ids = paper_ids if paper_ids is not None else literature.load().ids
    problems: list[str] = []
    seen: set[str] = set()
    for study in studies:
        for node in study.nodes:
            if not isinstance(node, dict):
                problems.append(f"{study.source}: study node must be a mapping")
                continue
            nid = node.get("id", "")
            label = f"{study.source}#{nid}"
            if not isinstance(nid, str) or not NODE_ID.fullmatch(nid):
                problems.append(f"{label}: node id must be a stable STUDY: identifier")
            elif nid in seen:
                problems.append(f"{label}: duplicate study node id")
            else:
                seen.add(nid)
            for field in ("statement", "detail"):
                if not isinstance(node.get(field), str) or not node[field].strip():
                    problems.append(f"{label}: missing {field}")
            if node.get("status") not in K.STATUSES:
                problems.append(f"{label}: status must use the existing claim vocabulary")
            for field, fixed in (("tier", 3), ("kind", "note"), ("evidence", "prose-only")):
                if field in node and node[field] != fixed:
                    problems.append(f"{label}: study {field} must remain {fixed!r}")
            sources = node.get("sources")
            if not isinstance(sources, list) or not sources:
                problems.append(f"{label}: sources must name at least one located paper")
                sources = []
            source_keys = set()
            for source in sources:
                if not isinstance(source, dict):
                    problems.append(f"{label}: source must be a paper/locator mapping")
                    continue
                paper, locator = source.get("paper"), source.get("locator")
                if not isinstance(paper, str) or paper not in paper_ids:
                    problems.append(f"{label}: source paper {paper!r} is not a full indexed paper")
                if not isinstance(locator, str) or not locator.strip():
                    problems.append(f"{label}: source has no page or section locator")
                key = (str(paper), str(locator))
                if key in source_keys:
                    problems.append(f"{label}: duplicate source locator {key}")
                source_keys.add(key)
            links = node.get("links", [])
            if not isinstance(links, list):
                problems.append(f"{label}: links must be a list")
                links = []
            link_keys = set()
            for link in links:
                if not isinstance(link, dict):
                    problems.append(f"{label}: link must be a type/target/detail mapping")
                    continue
                kind, target = link.get("type"), link.get("target")
                if kind not in LINK_TYPES:
                    problems.append(f"{label}: unsupported study link type {kind!r}")
                if not isinstance(target, str) or not target.strip():
                    problems.append(f"{label}: link has no target")
                elif known_ids is not None and target not in known_ids:
                    problems.append(f"{label}: link target {target!r} is unresolved")
                if target == nid:
                    problems.append(f"{label}: a study node cannot link to itself")
                if not isinstance(link.get("detail"), str) or not link["detail"].strip():
                    problems.append(f"{label}: link to {target!r} has no explanation")
                key = (str(kind), str(target))
                if key in link_keys:
                    problems.append(f"{label}: duplicate study link {key}")
                link_keys.add(key)
    return problems
