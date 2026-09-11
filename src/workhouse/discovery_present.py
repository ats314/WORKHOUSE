"""Compact, agent-facing presentation of discovery results.

A search response carries every retrieved passage in full plus the complete
source manifest. Agents read a bounded fraction of that. This module renders
the same result as rank-ordered rows with an excerpt chosen around the query
terms, the exact source location and hash of that excerpt, the terms that
matched, and a summarized provenance block. It changes no score and adds no
retrieval channel; the full response remains available for auditing.
"""

from __future__ import annotations

import contextlib
import hashlib
import json
from pathlib import Path

from .discovery_index import protected_blocks, tokenize

SCHEMA = "workhouse-discovery/compact/v1"
CONTEXT_SCHEMA = "workhouse-discovery/context/v2"
EXCERPT_CHARS = 700
MIN_EXCERPT_CHARS = 120
RECORD_FIELDS = ("kind", "status", "evidence", "tier", "where")


def query_terms(query: str | list[str]) -> list[str]:
    """Deterministic query tokens, using the index tokenizer."""
    parts = [query] if isinstance(query, str) else list(query)
    return sorted({token for part in parts for token in tokenize(part)})


def matched_terms(terms: list[str], text: str) -> list[str]:
    present = set(tokenize(text))
    return [term for term in terms if term in present]


def excerpt(text: str, terms: list[str], max_chars: int = EXCERPT_CHARS) -> dict:
    """The whole-line window under ``max_chars`` with the most query-term hits.

    Ties prefer the earliest window. A window that would end inside a
    protected block (display math, equation environment, fenced code) grows
    to the block end when that fits the budget; otherwise the cut is reported
    in ``cuts_block``. Line offsets are zero-based relative to ``text``.
    """
    if max_chars < MIN_EXCERPT_CHARS:
        raise ValueError(f"excerpt budget must be at least {MIN_EXCERPT_CHARS} characters")
    lines = text.splitlines(keepends=True)
    if not lines:
        return {"text": "", "line_offset": [0, 0], "truncated": False, "cuts_block": False}
    if len(text) <= max_chars:
        return {
            "text": text,
            "line_offset": [0, len(lines) - 1],
            "truncated": False,
            "cuts_block": False,
        }
    wanted = set(terms)
    counts = [sum(1 for token in tokenize(line) if token in wanted) for line in lines]
    blocks = {}
    for span in protected_blocks(lines):
        for number in range(span[0], span[1] + 1):
            blocks[number] = span
    best = None
    for first in range(len(lines)):
        chars, hits, last = 0, 0, first - 1
        while last + 1 < len(lines) and chars + len(lines[last + 1]) <= max_chars:
            last += 1
            chars += len(lines[last])
            hits += counts[last]
        if last < first:
            # A single line longer than the budget: slice it.
            piece = lines[first][:max_chars]
            candidate = (counts[first] if wanted else 0, -first, first, first, piece)
        else:
            candidate = (hits, -first, first, last, "".join(lines[first : last + 1]))
        if best is None or candidate[:2] > best[:2]:
            best = candidate
        if not wanted:
            break
    assert best is not None
    _hits, _order, first, last, window = best
    block = blocks.get(last)
    cuts_block = block is not None and block[1] > last
    if cuts_block:
        extended = "".join(lines[first : block[1] + 1])
        if len(extended) <= max_chars:
            window, last, cuts_block = extended, block[1], False
    opening = blocks.get(first)
    if opening is not None and opening[0] < first:
        cuts_block = True
    return {
        "text": window,
        "line_offset": [first, last],
        "truncated": True,
        "cuts_block": cuts_block,
    }


def _witness_summary(witness: dict) -> dict:
    steps = []
    for path in witness.get("paths", [])[:1]:
        for step in path:
            edge = step.get("edge", {})
            arrow = "->" if step.get("direction") == "forward" else "<-"
            steps.append(f"{step.get('from')} {arrow}[{edge.get('type')}] {step.get('to')}")
    return {
        "seed": witness.get("seed"),
        "steps": steps,
        "truncated": witness.get("truncated", False),
        "semantics": "registered edges traversed for retrieval; not a dependency claim",
    }


def _commands(node: str | None) -> dict:
    if not node:
        return {}
    return {
        "why": f"uv run --no-sync workhouse why {node}",
        "brief": (
            f"uv run --no-sync workhouse brief {node} --json --out .graph-state/TASK/brief.json"
        ),
        "connections": f"uv run --no-sync workhouse discover connections {node} --json",
    }


def compact_hit(
    hit: dict, terms: list[str], *, rank: int, group: str, max_chars: int = EXCERPT_CHARS
) -> dict:
    """One rank-ordered row: where it is, what matched, and how to follow up."""
    row = {
        "rank": rank,
        "group": group,
        "id": hit["id"],
        "kind": hit.get("kind"),
        "score": round(float(hit.get("score", 0.0)), 6),
        "channels": {
            name: info.get("rank") for name, info in hit.get("score_channels", {}).items()
        },
    }
    passage = hit if hit.get("kind") == "passage" else hit.get("matching_passage")
    from_passage = bool(passage and passage.get("kind") == "passage")
    if from_passage:
        window = excerpt(passage["text"], terms, max_chars)
        first, last = window["line_offset"]
        base = int(passage.get("start_line", 1))
        row["source"] = {
            "path": passage["path"],
            "lines": [base + first, base + last],
            "passage_lines": [base, int(passage.get("end_line", base))],
            "sha256": passage.get("source_sha256"),
            "passage_id": passage.get("id"),
        }
        row["excerpt"] = window["text"]
        row["excerpt_truncated"] = window["truncated"]
        if window["cuts_block"]:
            row["excerpt_cuts_block"] = True
        row["matched_terms"] = matched_terms(terms, passage["text"])
        row["claim_ids"] = list(passage.get("claim_ids", []))
    else:
        record = hit.get("record", {}) or {}
        statement = str(record.get("statement") or hit.get("text") or "")
        row["source"] = {"where": record.get("where") or hit.get("where", "")}
        row["excerpt"] = statement[:max_chars]
        row["excerpt_truncated"] = len(statement) > max_chars
        row["matched_terms"] = matched_terms(
            terms, "\n".join(str(record.get(key) or "") for key in ("statement", "detail"))
        )
        row["claim_ids"] = list(hit.get("claim_ids", []))
    record = hit.get("record")
    if isinstance(record, dict) and hit.get("kind") == "record":
        row["record"] = {key: record.get(key) for key in RECORD_FIELDS if record.get(key)}
        if from_passage:
            # The excerpt is source text; the statement is the catalogue wording.
            row["statement"] = str(record.get("statement", ""))[: min(400, max_chars)]
        row["commands"] = _commands(hit["id"])
    if hit.get("query_ranks"):
        row["query_ranks"] = dict(hit["query_ranks"])
    if hit.get("graph_witness"):
        row["graph_witness"] = _witness_summary(hit["graph_witness"])
    return row


def provenance_summary(meta: dict, root: Path | None = None) -> dict:
    """Identity and freshness without the per-file manifest."""
    cache_path = meta.get("cache_path")
    if cache_path and root is not None:
        with contextlib.suppress(ValueError):
            cache_path = Path(cache_path).resolve().relative_to(Path(root).resolve()).as_posix()
    summary = {
        "schema": meta.get("schema"),
        "fingerprint": meta.get("fingerprint"),
        "current_fingerprint": meta.get("current_fingerprint"),
        "freshness": meta.get("freshness"),
        "freshness_observation": meta.get("freshness_observation"),
        "freshness_error": meta.get("freshness_error"),
        "implementation_sha256": meta.get("implementation_sha256"),
        "index_manifest": meta.get("index_manifest"),
        "source_count": meta.get("source_count"),
        "passage_count": meta.get("passage_count"),
        "record_count": meta.get("record_count"),
        "edge_count": meta.get("edge_count"),
        "exclusion_count": meta.get("exclusion_count"),
        "inaccessible_count": meta.get("inaccessible_count"),
        "roots": (meta.get("settings") or {}).get("roots"),
        "external_roots": (meta.get("settings") or {}).get("external_roots"),
        "cache_path": cache_path,
        "execution": meta.get("execution"),
        "full_manifest": "workhouse discover info --json",
    }
    return {key: value for key, value in summary.items() if value is not None}


def present(result: dict, *, max_chars: int = EXCERPT_CHARS, root: Path | None = None) -> dict:
    """Render a search result as compact rows; scores and order are unchanged."""
    terms = query_terms(result.get("queries") or result.get("query", ""))
    rows = [
        compact_hit(hit, terms, rank=rank, group="direct", max_chars=max_chars)
        for rank, hit in enumerate(result.get("hits", []), 1)
    ]
    related = [
        compact_hit(hit, terms, rank=rank, group="related", max_chars=max_chars)
        for rank, hit in enumerate(result.get("related", []), 1)
    ]
    return {
        "schema": SCHEMA,
        "query": result.get("query", ""),
        "queries": result.get("queries"),
        "seeds": result.get("seeds", []),
        "hits": rows,
        "related": related,
        "retrieval": result.get("retrieval"),
        "provenance": provenance_summary(result.get("provenance", {}), root),
        "meaning": result.get("meaning"),
        "execution": result.get("execution"),
        "full_response": "workhouse discover search ... --json --full",
    }


def context_pack(result: dict, max_chars: int = 16000, *, root: Path | None = None) -> dict:
    """A hard-bounded handoff that keeps rank order and names what it omits.

    Rows enter in rank order (direct matches before related suggestions).
    When the budget is exceeded, every retained excerpt shrinks in steps
    before the lowest-ranked row is dropped, so the top result is only ever
    lost when the metadata alone exceeds the budget.
    """
    if max_chars < 2000:
        raise ValueError("context budget must be at least 2000 characters")
    compact = present(result, root=root)
    ordered = compact["hits"] + compact["related"]
    pack = {
        "schema": CONTEXT_SCHEMA,
        "query": compact["query"],
        "queries": compact.get("queries"),
        "seeds": compact["seeds"],
        "meaning": compact["meaning"],
        "provenance": compact["provenance"],
        "scientific_graph_freshness": "not assessed; use a retained workhouse brief",
        "execution": compact.get("execution", {}),
        "retrieval": {
            key: value
            for key, value in (compact.get("retrieval") or {}).items()
            if key in {"channels", "fusion", "graph_method", "graph_residual", "candidate_pool"}
        },
        "hits": [],
        "omitted": 0,
        "omitted_ids": [],
        "excerpt_chars": EXCERPT_CHARS,
        "budget": {"max_chars": max_chars, "unit": "serialized JSON characters, not tokens"},
    }

    def encoded() -> str:
        return json.dumps(pack, ensure_ascii=True, sort_keys=True)

    if len(encoded()) + 100 > max_chars:
        raise ValueError("query metadata exceeds context budget")
    terms = query_terms(result.get("queries") or result.get("query", ""))
    budgets = [EXCERPT_CHARS, 400, 250, MIN_EXCERPT_CHARS]
    full_rows = [(hit, "direct") for hit in result.get("hits", [])]
    full_rows += [(hit, "related") for hit in result.get("related", [])]
    kept = list(ordered)
    while kept:
        fits = False
        for budget in budgets:
            pack["hits"] = [
                compact_hit(hit, terms, rank=row["rank"], group=group, max_chars=budget)
                for row, (hit, group) in zip(kept, full_rows[: len(kept)], strict=True)
            ]
            pack["excerpt_chars"] = budget
            if len(encoded()) + 100 <= max_chars:
                fits = True
                break
        if fits:
            break
        dropped = kept.pop()
        pack["omitted"] += 1
        pack["omitted_ids"].append(
            {"rank": dropped["rank"], "group": dropped["group"], "id": dropped["id"]}
        )
    if not kept:
        pack["hits"] = []
    pack["fingerprint"] = hashlib.sha256(encoded().encode()).hexdigest()
    return pack


def _path_line(step: dict) -> str:
    edge = step.get("edge", {})
    arrow = "->" if step.get("direction") == "forward" else "<-"
    return (
        f"{step.get('from')} {arrow}[{edge.get('type')} {edge.get('how')}] {step.get('to')}"
        f"  ({edge.get('source')})"
    )


def present_connections(result: dict, *, max_chars: int = EXCERPT_CHARS, root=None) -> dict:
    """Compact connection candidates: witnesses, path, excerpt and what to check."""
    seed = result.get("seed", {})
    terms = query_terms(result.get("query", ""))
    rows = []
    for rank, candidate in enumerate(result.get("candidates", []), 1):
        record = candidate.get("record", {}) or {}
        row = {
            "rank": rank,
            "id": candidate["id"],
            "connection_rank": round(float(candidate.get("connection_rank", 0.0)), 6),
            "record": {key: record.get(key) for key in RECORD_FIELDS if record.get(key)},
            "statement": str(record.get("statement", ""))[:400],
            "retrieval_channels": {
                name: info.get("rank") for name, info in candidate.get("retrieval", {}).items()
            },
            "shared_witness_count": candidate.get("shared_witness_count", 0),
            "shared_witnesses": [
                {
                    "id": witness["id"],
                    "degree": witness.get("degree"),
                    "via": [
                        witness.get("source_step", {}).get("edge", {}).get("type"),
                        witness.get("target_step", {}).get("edge", {}).get("type"),
                    ],
                }
                for witness in candidate.get("shared_witnesses", [])[:3]
            ],
            "path": [_path_line(step) for step in candidate.get("path", [])],
            "path_found": candidate.get("path_found"),
            "existing_relations": len(candidate.get("existing_relations", [])),
            "source_family": (candidate.get("source_family") or {}).get("comparison"),
            "commands": _commands(candidate["id"]),
        }
        passage = candidate.get("matching_passage")
        if passage and passage.get("kind") == "passage":
            window = excerpt(passage["text"], terms, max_chars)
            first, last = window["line_offset"]
            base = int(passage.get("start_line", 1))
            row["source"] = {
                "path": passage["path"],
                "lines": [base + first, base + last],
                "sha256": passage.get("source_sha256"),
            }
            row["excerpt"] = window["text"]
            row["excerpt_truncated"] = window["truncated"]
            row["matched_terms"] = matched_terms(terms, passage["text"])
        rows.append(row)
    return {
        "schema": "workhouse-discovery/connections-compact/v1",
        "seed": {
            "id": seed.get("id"),
            "statement": str(seed.get("statement", ""))[:600],
            "where": seed.get("where"),
            **{key: seed.get(key) for key in RECORD_FIELDS if seed.get(key)},
        },
        "query": result.get("query", ""),
        "candidates": rows,
        "already_connected_excluded": result.get("already_connected_excluded"),
        "review_required": [
            "Compare the exact objects, hypotheses, regime and normalizations.",
            "Read each cited argument; copied prose is not an independent origin.",
            "Register a relationship only through a reviewed proposal file.",
        ],
        "provenance": provenance_summary(result.get("provenance", {}), root),
        "meaning": result.get("meaning"),
        "execution": result.get("execution"),
        "full_response": "workhouse discover connections ID --json --full",
    }


def render_paths(result: dict) -> str:
    lines = [
        f"{result.get('source')} -> {result.get('target')}: "
        f"{len(result.get('paths', []))} path(s), mode {result.get('mode')}",
        result.get("semantics", ""),
    ]
    for number, path in enumerate(result.get("paths", []), 1):
        lines.append(f"path {number} ({len(path)} steps)")
        lines.extend("  " + _path_line(step) for step in path)
    if result.get("truncated"):
        lines.append(f"truncated: {', '.join(result.get('truncation_reasons', []))}")
    return "\n".join(line for line in lines if line is not None)


def render_impact(result: dict) -> str:
    lines = [
        f"{result.get('direction')} of {result.get('source')}: "
        f"{len(result.get('nodes', []))} recorded node(s)",
        result.get("semantics", ""),
    ]
    for node in result.get("nodes", []):
        last = node["path"][-1] if node.get("path") else {}
        edge = last.get("edge", {})
        lines.append(
            f"  depth {node['depth']}: {node['id']}  via {edge.get('type')} ({edge.get('source')})"
        )
    if result.get("truncated"):
        lines.append(f"truncated: {', '.join(result.get('truncation_reasons', []))}")
    return "\n".join(lines)


def render_info(meta: dict) -> str:
    summary = provenance_summary(meta)
    lines = [
        f"discovery cache {str(summary.get('fingerprint', ''))[:12]}  "
        f"freshness {summary.get('freshness')}",
        f"sources {summary.get('source_count')}  passages {summary.get('passage_count')}  "
        f"records {summary.get('record_count')}  edges {summary.get('edge_count')}",
        f"roots: {', '.join(summary.get('roots') or [])}",
    ]
    if summary.get("external_roots"):
        lines.append(f"external roots: {', '.join(summary['external_roots'])}")
    lines.append(
        f"exclusions {summary.get('exclusion_count')}  inaccessible "
        f"{summary.get('inaccessible_count')}  cache {summary.get('cache_path')}"
    )
    return "\n".join(lines)


def render_compact(result: dict) -> str:
    """Readable text for a compact search result."""
    lines = [result.get("meaning") or "", ""]
    for row in result.get("hits", []) + result.get("related", []):
        if row["group"] == "related" and row["rank"] == 1:
            lines.extend(["", "Related graph candidates (separate from direct matches)"])
        source = row.get("source", {})
        first, last = (source.get("lines") or ["?", "?"])[:2]
        where = source.get("where", "")
        if source.get("path"):
            where = f"{source['path']}:{first}-{last}"
        lines.append(f"{row['rank']:>2}. {row['id']}  [{', '.join(row.get('matched_terms', []))}]")
        lines.append(f"    {where}")
        for text_line in row.get("excerpt", "").strip().splitlines()[:6]:
            lines.append("    | " + text_line.rstrip()[:160])
    return "\n".join(lines)


def render_connections(result: dict) -> str:
    """Readable text for compact (or full) connection candidates."""
    seed = result.get("seed", {})
    lines = [
        f"seed {seed.get('id')}: {str(seed.get('statement', ''))[:200]}",
        result.get("meaning") or "",
        "",
    ]
    for row in result.get("candidates", []):
        record = row.get("record", {}) or {}
        statement = row.get("statement") or str(record.get("statement", ""))[:200]
        rank = row.get("rank", "")
        lines.append(f"{rank:>2}. {row['id']}  witnesses {row.get('shared_witness_count', 0)}")
        lines.append(f"    {statement[:200]}")
        location = row.get("source", {}) if isinstance(row.get("source"), dict) else {}
        if location.get("path"):
            first, last = (location.get("lines") or ["?", "?"])[:2]
            lines.append(f"    {location['path']}:{first}-{last}")
        else:
            lines.append(f"    {record.get('where', '')}")
        path = row.get("path") or []
        if path and isinstance(path[0], str):
            lines.append("    path: " + " | ".join(path[:3]))
        elif path:
            lines.append(f"    path: {len(path)} step(s)")
        else:
            lines.append("    path: not found within bounds")
    return "\n".join(lines)
