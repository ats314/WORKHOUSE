"""Make each discovery retrieval addition's benefit visible, in one process.

The harness builds one ``DiscoveryEngine`` and runs the same frozen queries
through several configurations (lexical only, with the graph channel, with
lexicon expansion, with agent-written query plans). A second evaluation hides
sampled registered edges from an in-memory graph copy and asks whether
``connections`` or plain retrieval recovers the hidden partner. Every number
is retrieval evidence about candidate ranking; none of it is proof, support or
scientific status, and the saved scientific graph is never written.

Run explicitly from a checkout. The unit tests exercise a synthetic engine.
"""

from __future__ import annotations

import argparse
import hashlib
import importlib
import importlib.util
import json
import math
import random
import re
import statistics
import subprocess
import sys
import time
import tracemalloc
from collections import defaultdict
from datetime import UTC, datetime
from pathlib import Path
from typing import Any

SCHEMA = "workhouse-discovery-evaluation/v1"
ROOT = Path(__file__).resolve().parents[1]
DEFAULT_FIXTURE = "tests/fixtures/discovery_heldout_queries.json"
DEVELOPMENT_FIXTURE = "tests/fixtures/discovery_queries.json"
LEXICON_PATH = "graph-tasks/discovery/lexicon.yaml"
LINK_EDGE_TYPES = ("depends_on", "bears_on", "supported_by")
MIN_STATEMENT_CHARS = 80
MIN_LEAK_CHARS = 4
LINK_LIMIT = 20
CONFIGURATIONS = (
    "lexical",
    "lexical+graph",
    "lexical+lexicon",
    "lexical+graph+lexicon",
    "plans",
)
# A query group names the vocabulary its questions were phrased in. A relevant
# hit outside these families is the cross-family case discovery exists for.
GROUP_FAMILIES = (
    ("historical", ("theory", "corpus-import")),
    ("theory", ("theory", "corpus-import")),
    ("derivation", ("docs",)),
    ("notes", ("notes", "literature", "research")),
    ("literature", ("notes", "literature", "research")),
    ("imported", ("notes", "literature", "research")),
)


def _load_benchmark():
    """Reuse the benchmark's relevance rules so two fixtures cannot drift apart."""
    path = Path(__file__).with_name("benchmark_discovery.py")
    spec = importlib.util.spec_from_file_location("benchmark_discovery", path)
    if spec is None or spec.loader is None:
        raise ImportError(f"cannot load {path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


benchmark = _load_benchmark()


# --------------------------------------------------------------------------- fixtures


def normalize_case(case: dict) -> dict:
    """Map held-out spellings onto the benchmark's fields without losing either.

    ``negative: true`` and ``expected_ids`` are the held-out fixture's names for
    ``expect_empty`` and ``expected_claim_ids``. Reading them as unknown keys
    would silently score every held-out negative as a positive with no target.
    """
    row = dict(case)
    if row.get("negative") and not row.get("expect_empty"):
        row["expect_empty"] = True
    ids = list(row.get("expected_claim_ids") or [])
    for value in row.get("expected_ids") or []:
        if value not in ids:
            ids.append(value)
    if ids:
        row["expected_claim_ids"] = ids
    return row


class _Text:
    """Duck-typed path so the benchmark validator reads normalized text."""

    def __init__(self, text: str):
        self.text = text

    def read_text(self, encoding: str = "utf-8") -> str:
        return self.text


def load_fixture(path: Path) -> dict:
    """Validate either fixture with the benchmark's rules after normalization."""
    payload = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(payload, dict):
        raise ValueError("query fixture must be a JSON object")
    payload["queries"] = [
        normalize_case(case) if isinstance(case, dict) else case
        for case in payload.get("queries") or []
    ]
    # The validator owns every acceptance rule; running it on the normalized
    # text keeps development and held-out fixtures under one contract.
    return benchmark.load_queries(_Text(json.dumps(payload)))


def fixture_kind(fixture: dict) -> str:
    groups = {case.get("group", "") for case in fixture["queries"]}
    return (
        "held-out" if any(str(group).startswith("heldout_") for group in groups) else "development"
    )


# --------------------------------------------------------------------------- families


def _first_segment(path: str) -> str:
    value = path.replace("\\", "/").strip()
    value = value.removeprefix("./")
    return value.split("/", 1)[0] if value else ""


def hit_family(hit: dict) -> str:
    """The source family of a hit; external roots are labelled, never merged."""
    if hit.get("external"):
        return f"ext:{hit.get('source_label') or 'unlabelled'}"
    path = hit.get("path") if isinstance(hit.get("path"), str) else ""
    segment = _first_segment(path or str(hit.get("where") or ""))
    if segment:
        return segment
    record = hit.get("record") if isinstance(hit.get("record"), dict) else {}
    return f"record:{record.get('kind') or hit.get('kind') or 'unknown'}"


def record_family(record: dict) -> str:
    segment = _first_segment(str(record.get("where") or ""))
    return segment or f"record:{record.get('kind') or 'unknown'}"


def group_families(group: str) -> tuple[str, ...] | None:
    name = str(group or "").casefold()
    for marker, families in GROUP_FAMILIES:
        if marker in name:
            return families
    return None


# --------------------------------------------------------------------------- inputs


def lexicon_expander(root: Path):
    """The lexicon channel, or the reason it is unavailable.

    The lexicon module and its YAML are written concurrently; a hard import
    would make the whole evaluation fail on the day one of them is absent.
    """
    lexicon_file = root / LEXICON_PATH
    if not lexicon_file.is_file():
        return None, f"{LEXICON_PATH} absent", {}
    try:
        # importlib honours sys.modules, so a test double or a replaced module
        # is seen; a package attribute bound at first import would not be.
        discovery_lexicon = importlib.import_module("workhouse.discovery_lexicon")
    except Exception as exc:  # Import problems are reported, never fatal.
        return None, f"import failed: {type(exc).__name__}: {exc}", {}
    expand = getattr(discovery_lexicon, "expand", None)
    if not callable(expand):
        return None, "discovery_lexicon.expand missing", {}
    load = getattr(discovery_lexicon, "load", None)
    lexicon = None
    if callable(load):
        try:
            lexicon = load(lexicon_file, root=root)
        except Exception as exc:  # An invalid lexicon is a reported input problem.
            return None, f"load failed: {type(exc).__name__}: {exc}", {}
    weight = getattr(discovery_lexicon, "DEFAULT_LEXICON_WEIGHT", 1.0)
    weight = float(weight) if isinstance(weight, int | float) and 0 < weight <= 10 else 1.0

    def expander(query: str) -> list[dict]:
        result = expand(query, lexicon) if lexicon is not None else expand(query)
        subs = result.get("sub_queries") if isinstance(result, dict) else None
        rows = []
        for item in subs if isinstance(subs, list) else []:
            text = item.get("text") if isinstance(item, dict) else item
            item_weight = item.get("weight", weight) if isinstance(item, dict) else weight
            if isinstance(text, str) and text.strip():
                rows.append({"text": text.strip(), "weight": float(item_weight)})
        return rows

    try:
        expander("probe")
    except Exception as exc:
        return None, f"expand failed: {type(exc).__name__}: {exc}", {}
    facts = {
        "fingerprint": (lexicon or {}).get("fingerprint"),
        "entries": len((lexicon or {}).get("entries") or []),
        "sub_query_weight": weight,
        "api": "expand(query, lexicon)" if lexicon is not None else "expand(query)",
    }
    return expander, "available", facts


def load_plans(directory: Path | None, case_ids: list[str]) -> tuple[dict, list[dict]]:
    """Agent-written query plans, ``<query id>.json`` with ``{queries: [{text, weight}]}``."""
    plans: dict[str, dict] = {}
    problems: list[dict] = []
    if directory is None:
        return plans, problems
    if not directory.is_dir():
        problems.append({"path": str(directory), "error": "plans directory absent"})
        return plans, problems
    for case_id in case_ids:
        path = directory / f"{case_id}.json"
        if not path.is_file():
            continue
        try:
            plan = json.loads(path.read_text(encoding="utf-8"))
            texts, weights = [], []
            for item in plan.get("queries", []):
                text = item["text"] if isinstance(item, dict) else str(item)
                weight = float(item.get("weight", 1.0)) if isinstance(item, dict) else 1.0
                if not isinstance(text, str) or not text.strip():
                    raise ValueError("plan query text must be a nonempty string")
                if not 0 < weight <= 10:
                    raise ValueError("plan weights must lie in (0, 10]")
                texts.append(text.strip())
                weights.append(weight)
            if not texts:
                raise ValueError("plan has no queries")
            plans[case_id] = {"path": str(path), "texts": texts, "weights": weights}
        except (OSError, ValueError, KeyError, TypeError) as exc:
            problems.append({"path": str(path), "error": f"{type(exc).__name__}: {exc}"})
    return plans, problems


def _plan_arguments(query: str, plan: dict) -> dict:
    """Weights must follow the engine's own deduplication or it rejects them."""
    weights: dict[str, float] = {}
    primary = query.strip()
    if primary:
        weights[primary] = 1.0
    for text, weight in zip(plan["texts"], plan["weights"], strict=True):
        weights.setdefault(text, weight)
    texts = [text for text in weights if text != primary]
    return {"queries": texts, "query_weights": [weights[text] for text in weights]}


# --------------------------------------------------------------------------- searches


def search_arguments(name: str, case: dict, limit: int, expander, plans: dict) -> dict | None:
    """Keyword arguments for one configuration, or ``None`` when it cannot run."""
    if name == "lexical":
        return {"limit": limit, "graph_weight": 0, "related_limit": 0}
    if name == "lexical+graph":
        return {"limit": limit}
    if name in ("lexical+lexicon", "lexical+graph+lexicon"):
        if expander is None:
            return None
        subs = expander(case["query"])
        plan = {"texts": [row["text"] for row in subs], "weights": [row["weight"] for row in subs]}
        arguments = {"limit": limit, **_plan_arguments(case["query"], plan)}
        if name == "lexical+lexicon":
            arguments.update(graph_weight=0, related_limit=0)
        return arguments
    if name == "plans":
        plan = plans.get(case["id"])
        if plan is None:
            return {"limit": limit}
        return {"limit": limit, **_plan_arguments(case["query"], plan)}
    raise ValueError(f"unknown configuration: {name}")


def score_row(
    case: dict, hits: list[dict], limit: int, error: str | None, related: list[dict] | None = None
) -> dict:
    """The benchmark's row plus the family, score and related-band facts.

    The graph channel never enters the primary band, so primary recall cannot
    show its effect; the related band is scored separately, never merged.
    """
    row = benchmark.score_query(hits, case, limit, error)
    ranked = hits[:limit]
    related_rank = None
    if related and not error and not case.get("expect_empty"):
        related_rank = next(
            (i for i, hit in enumerate(related, 1) if benchmark.is_relevant(hit, case)), None
        )
    row["related_first_relevant_rank"] = related_rank
    row["related_hits"] = len(related or [])
    row["relevant_only_in_related"] = bool(related_rank) and not row["any_relevant_hit"]
    families = [hit_family(hit) for hit in ranked]
    row["top_score"] = ranked[0].get("score") if ranked and not error else None
    # The pre-registered abstention rule: the top direct row covers fewer than
    # half of the query's content terms and no exact channel contributed.
    row["weak_match"], row["query_coverage"] = None, None
    if not error:
        try:
            from workhouse.discovery_present import present as compact_present

            hint = compact_present({"query": case["query"], "hits": ranked[:1], "related": []})[
                "abstention_hint"
            ]
            row["weak_match"] = bool(hint.get("weak_match"))
            row["query_coverage"] = hint.get("coverage")
        except Exception:  # A presentation failure must not fail the evaluation.
            pass
    row["families"] = families
    row["distinct_families"] = len(set(families))
    first = row["first_relevant_rank"]
    row["relevant_family"] = families[first - 1] if first else None
    expected = group_families(case.get("group", ""))
    row["group_families"] = list(expected) if expected else None
    row["cross_family"] = row["relevant_family"] not in expected if first and expected else None
    row["top_ids"] = [str(hit.get("id", "")) for hit in ranked]
    return row


def _timed_search(engine, query: str, arguments: dict, repeat: int) -> tuple[dict, float]:
    """Median wall time over ``repeat`` identical calls; the last result is kept."""
    seconds = []
    result: dict = {}
    for _ in range(max(1, repeat)):
        started = time.perf_counter()
        result = engine.search(query, **arguments)
        seconds.append(time.perf_counter() - started)
    return result, statistics.median(seconds)


def run_configuration(
    engine, name: str, cases: list[dict], limit: int, expander, plans: dict, repeat: int
) -> dict:
    rows = []
    for case in cases:
        arguments = search_arguments(name, case, limit, expander, plans)
        error, hits, related, seconds = None, [], [], None
        if arguments is None:
            error = "configuration unavailable"
        else:
            try:
                result, seconds = _timed_search(engine, case["query"], arguments, repeat)
                hits = result["hits"]
                related = result.get("related") or []
            except Exception as exc:  # A single failing query must not void the run.
                error = f"{type(exc).__name__}: {exc}"
        row = score_row(case, hits, limit, error, related)
        if seconds is not None:
            row["warm_query_seconds"] = seconds
        row["sub_queries"] = len(arguments.get("queries") or []) if arguments else 0
        row["plan"] = name == "plans" and case["id"] in plans
        rows.append(row)
    return {"rows": rows, "summary": summarize_rows(rows, limit)}


def summarize_rows(rows: list[dict], limit: int) -> dict:
    """Benchmark recall/MRR plus negative, diversity and cross-family views.

    Both negative-control criteria are reported: an empty result is the strict
    reading, and a top score below the positives' median top score is the
    reading an agent applying a score threshold would experience. Neither is a
    proof of absence.
    """
    summary = benchmark.summarize(rows, limit)
    positive = [row for row in rows if not row["negative_control"] and not row["error"]]
    negative = [row for row in rows if row["negative_control"] and not row["error"]]
    top_scores = [row["top_score"] for row in positive if row["top_score"] is not None]
    median_top = statistics.median(top_scores) if top_scores else None
    below = [
        row["top_score"] is None or (median_top is not None and row["top_score"] < median_top)
        for row in negative
    ]
    with_hits = [row for row in positive if row["returned_hits"]]
    assessed = [row for row in positive if row["cross_family"] is not None]
    scored = [row for row in rows if not row["negative_control"]]
    recovered_by_related = sum(bool(row.get("relevant_only_in_related")) for row in scored)
    summary.update(
        {
            "relevant_only_in_related": recovered_by_related,
            "recall_with_related": (
                (summary["successful_queries"] + recovered_by_related) / len(scored)
                if scored
                else None
            ),
            "median_positive_top_score": median_top,
            "negative_controls_passed_below_median": sum(below) if median_top is not None else None,
            "negative_controls_passed_weak_match": sum(
                bool(row.get("weak_match")) for row in negative
            ),
            "positives_flagged_weak_match": sum(bool(row.get("weak_match")) for row in positive),
            "mean_distinct_families_top_k": (
                statistics.mean(row["distinct_families"] for row in with_hits)
                if with_hits
                else None
            ),
            "cross_family_hits": sum(bool(row["cross_family"]) for row in assessed),
            "cross_family_assessed": len(assessed),
            "cross_family_fraction": (
                sum(bool(row["cross_family"]) for row in assessed) / len(assessed)
                if assessed
                else None
            ),
            "queries_with_sub_queries": sum(bool(row.get("sub_queries")) for row in rows),
        }
    )
    return summary


# --------------------------------------------------------------------------- leakage


def _contains_token(text: str, needle: str) -> bool:
    """Case-insensitive match at token boundaries; ``t_2`` must not match ``t_23``."""
    pattern = r"(?<![\w-])" + re.escape(needle) + r"(?![\w-])"
    return re.search(pattern, text, re.IGNORECASE) is not None


def leakage_check(cases: list[dict]) -> dict:
    """Flag expected file stems or ids quoted inside a query.

    A query that names its own answer measures string matching, not
    discovery; the held-out fixture promises zero such queries.
    """
    rows = []
    for case in cases:
        if case.get("expect_empty"):
            continue
        text = case["query"]
        exact_group = "exact" in str(case.get("group", "")).casefold()
        markers = []
        for path in case.get("expected_paths", []):
            stem = Path(path.replace("\\", "/")).stem
            # A one-letter stem such as "a.md" would flag every query.
            if len(stem) >= MIN_LEAK_CHARS and _contains_token(text, stem):
                markers.append({"kind": "path_stem", "value": stem})
        for value in case.get("expected_claim_ids", []):
            if _contains_token(text, value):
                # An exact-control query is the id itself; that is the control's
                # purpose, not a leak, and it is listed rather than hidden.
                intentional = exact_group or text.strip() == value
                markers.append(
                    {"kind": "exact_id_lookup" if intentional else "claim_id", "value": value}
                )
        rows.append({"query_id": case["id"], "leaks": markers})
    flagged = [row for row in rows if row["leaks"]]
    leaking = [
        row for row in flagged if any(leak["kind"] != "exact_id_lookup" for leak in row["leaks"])
    ]
    return {
        "positive_queries": len(rows),
        "leaking_queries": len(leaking),
        "exact_id_queries": len(flagged) - len(leaking),
        "rows": flagged,
        "meaning": (
            "Expected stems or ids inside a query would reward exact string matching; "
            "exact-control queries that consist of the id are listed, not counted."
        ),
    }


# --------------------------------------------------------------------------- link recovery


def eligible_edges(engine) -> list[dict]:
    """Curated edges of the recovery types between two substantive records.

    Short statements give retrieval nothing to work with, so their edges would
    measure the fixture, not the engine. One entry per (src, dst, type).
    """
    records = engine.records
    seen: set[tuple[str, str, str]] = set()
    edges = []
    for edge in engine.index.edges:
        if edge.get("type") not in LINK_EDGE_TYPES or edge.get("how") != "curated":
            continue
        src, dst = edge.get("src"), edge.get("dst")
        if not isinstance(src, str) or not isinstance(dst, str) or src == dst:
            continue
        source, target = records.get(src), records.get(dst)
        if source is None or target is None:
            continue
        if any(
            len(str(node.get("statement") or "")) < MIN_STATEMENT_CHARS for node in (source, target)
        ):
            continue
        key = (src, dst, edge["type"])
        if key in seen:
            continue
        seen.add(key)
        edges.append(edge)
    return sorted(edges, key=lambda edge: (edge["type"], edge["src"], edge["dst"]))


def sample_edges(edges: list[dict], count: int, seed: int) -> list[dict]:
    """Deterministic, type-stratified sample so rare types are represented."""
    by_type: dict[str, list[dict]] = defaultdict(list)
    for edge in edges:
        by_type[edge["type"]].append(edge)
    rng = random.Random(seed)
    pools = {type_: list(items) for type_, items in sorted(by_type.items())}
    for items in pools.values():
        rng.shuffle(items)
    chosen: list[dict] = []
    while len(chosen) < count and any(pools.values()):
        for type_ in sorted(pools):
            if pools[type_] and len(chosen) < count:
                chosen.append(pools[type_].pop())
    return chosen


def hidden_graph(engine, src: str, dst: str):
    """An in-memory graph without every edge joining ``src`` and ``dst``.

    Parallel edges between the same pair would keep the pair "already
    connected" and turn every such sample into a guaranteed miss for the
    wrong reason, so all of them are hidden and the count is recorded.
    """
    from workhouse.discovery_graph import GraphDiscovery

    pair = {src, dst}
    remaining = [edge for edge in engine.index.edges if {edge.get("src"), edge.get("dst")} != pair]
    hidden = len(engine.index.edges) - len(remaining)
    graph = GraphDiscovery(list(engine.records.values()), remaining)
    if dst in graph.neighbors(src):
        raise RuntimeError(f"hidden edge still present between {src} and {dst}")
    return graph, hidden


def _rank(target: str, ordered: list[str]) -> int | None:
    return next((position for position, node in enumerate(ordered, 1) if node == target), None)


def recover_one(engine, edge: dict, limit: int = LINK_LIMIT) -> dict:
    """Hide one edge, ask both variants for the partner, restore the graph."""
    src, dst = edge["src"], edge["dst"]
    graph, hidden = hidden_graph(engine, src, dst)
    row = {
        "src": src,
        "dst": dst,
        "type": edge["type"],
        "how": edge.get("how"),
        "source": edge.get("source"),
        "same_family": record_family(engine.records[src]) == record_family(engine.records[dst]),
        "src_family": record_family(engine.records[src]),
        "dst_family": record_family(engine.records[dst]),
        "edges_hidden": hidden,
        "connections_rank": None,
        "retrieval_rank": None,
        "connections_seconds": None,
        "retrieval_seconds": None,
        "error": None,
    }
    original = engine.graph
    engine.graph = graph
    try:
        started = time.perf_counter()
        result = engine.connections(src, limit=limit)
        row["connections_seconds"] = time.perf_counter() - started
        ordered = [str(candidate.get("id", "")) for candidate in result["candidates"]]
        row["connections_rank"] = _rank(dst, ordered)
        row["connections_candidates"] = len(ordered)
        statement = str(engine.records[src].get("statement") or "")
        started = time.perf_counter()
        search = engine.search(statement, limit=limit, related_limit=limit)
        row["retrieval_seconds"] = time.perf_counter() - started
        ids = list(
            dict.fromkeys(
                node
                for hit in search["hits"] + search["related"]
                for node in [hit.get("id"), *(hit.get("claim_ids") or [])]
                if isinstance(node, str) and node in engine.records
            )
        )
        row["retrieval_rank"] = _rank(dst, ids)
    except Exception as exc:  # Keep the sample; the failure is part of the result.
        row["error"] = f"{type(exc).__name__}: {exc}"
    finally:
        engine.graph = original
    return row


def _recovery_summary(rows: list[dict], key: str) -> dict:
    ranks = [row[key] for row in rows if not row["error"]]
    count = len(ranks)
    return {
        "samples": count,
        "recovered_at_5": sum(1 for rank in ranks if rank and rank <= 5) / count if count else None,
        "recovered_at_20": (
            sum(1 for rank in ranks if rank and rank <= LINK_LIMIT) / count if count else None
        ),
        "mrr": sum(1 / rank for rank in ranks if rank) / count if count else None,
        "misses": sum(1 for rank in ranks if not rank),
    }


def link_recovery(engine, count: int, seed: int, limit: int = LINK_LIMIT) -> dict:
    edges = eligible_edges(engine)
    samples = sample_edges(edges, count, seed)
    rows = [recover_one(engine, edge, limit) for edge in samples]
    variants = {"connections": "connections_rank", "retrieval_only": "retrieval_rank"}
    breakdown: dict[str, dict] = {}
    for variant, key in variants.items():
        by_type = {
            type_: _recovery_summary([row for row in rows if row["type"] == type_], key)
            for type_ in sorted({row["type"] for row in rows})
        }
        by_family = {
            "same_family": _recovery_summary([row for row in rows if row["same_family"]], key),
            "cross_family": _recovery_summary([row for row in rows if not row["same_family"]], key),
        }
        breakdown[variant] = {
            "overall": _recovery_summary(rows, key),
            "by_type": by_type,
            "by_family": by_family,
        }
    return {
        "eligible_edges": len(edges),
        "eligible_by_type": {
            type_: sum(1 for edge in edges if edge["type"] == type_) for type_ in LINK_EDGE_TYPES
        },
        "requested_samples": count,
        "samples": len(rows),
        "seed": seed,
        "limit": limit,
        "errors": sum(bool(row["error"]) for row in rows),
        "variants": breakdown,
        "rows": rows,
        "method": {
            "hidden": (
                "Every edge joining the sampled pair is removed from an in-memory graph copy; "
                "the engine's graph is swapped for the copy during the two calls and restored."
            ),
            "connections": (
                f"engine.connections(src, limit={limit}) with its default query and passage "
                "quota; rank of dst among the listed candidates."
            ),
            "retrieval_only": (
                f"engine.search(statement of src, limit={limit}, related_limit={limit}) with "
                "no seed; rank of dst among the hit and related ids in order."
            ),
            "sampling": "type-stratified round robin over a seeded shuffle",
            "meaning": (
                "Recovery of a registered edge is a retrieval property of the engine; it does "
                "not validate the edge or suggest new ones."
            ),
        },
    }


# --------------------------------------------------------------------------- environment


def memory_probe() -> dict:
    """Peak traced memory and, where the platform allows, the working set.

    Every probe is optional: an unavailable counter is reported as ``None``
    rather than ending an evaluation that already ran for minutes.
    """
    info: dict[str, Any] = {
        "tracemalloc_enabled": tracemalloc.is_tracing(),
        "tracemalloc_peak_bytes": None,
        "working_set_bytes": None,
        "peak_working_set_bytes": None,
        "working_set_source": None,
    }
    if tracemalloc.is_tracing():
        info["tracemalloc_peak_bytes"] = tracemalloc.get_traced_memory()[1]
    try:
        if sys.platform == "win32":
            import ctypes
            from ctypes import wintypes

            class Counters(ctypes.Structure):
                _fields_ = [
                    ("cb", wintypes.DWORD),
                    ("PageFaultCount", wintypes.DWORD),
                    ("PeakWorkingSetSize", ctypes.c_size_t),
                    ("WorkingSetSize", ctypes.c_size_t),
                    ("QuotaPeakPagedPoolUsage", ctypes.c_size_t),
                    ("QuotaPagedPoolUsage", ctypes.c_size_t),
                    ("QuotaPeakNonPagedPoolUsage", ctypes.c_size_t),
                    ("QuotaNonPagedPoolUsage", ctypes.c_size_t),
                    ("PagefileUsage", ctypes.c_size_t),
                    ("PeakPagefileUsage", ctypes.c_size_t),
                ]

            kernel32 = ctypes.WinDLL("kernel32", use_last_error=True)
            probe = kernel32.K32GetProcessMemoryInfo
            probe.argtypes = [wintypes.HANDLE, ctypes.POINTER(Counters), wintypes.DWORD]
            probe.restype = wintypes.BOOL
            kernel32.GetCurrentProcess.restype = wintypes.HANDLE
            counters = Counters()
            counters.cb = ctypes.sizeof(Counters)
            if not probe(kernel32.GetCurrentProcess(), ctypes.byref(counters), counters.cb):
                raise OSError(f"GetProcessMemoryInfo failed: {ctypes.get_last_error()}")
            info["working_set_bytes"] = int(counters.WorkingSetSize)
            info["peak_working_set_bytes"] = int(counters.PeakWorkingSetSize)
            info["working_set_source"] = "psapi GetProcessMemoryInfo"
        else:
            import resource

            usage = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
            scale = 1 if sys.platform == "darwin" else 1024
            info["peak_working_set_bytes"] = int(usage) * scale
            info["working_set_source"] = "getrusage ru_maxrss"
    except Exception as exc:  # The probe is diagnostic; it never fails the run.
        info["working_set_error"] = f"{type(exc).__name__}: {exc}"
    return info


def git_facts(root: Path) -> dict:
    """HEAD and the short status, tolerating a missing git or a non-repository."""
    facts: dict[str, Any] = {"head": None, "status_short": None, "error": None}
    for name, command in (
        ("head", ["git", "rev-parse", "HEAD"]),
        ("status_short", ["git", "status", "--short"]),
    ):
        try:
            completed = subprocess.run(
                command, cwd=root, capture_output=True, text=True, timeout=60, check=False
            )
            if completed.returncode != 0:
                raise OSError(completed.stderr.strip() or f"exit {completed.returncode}")
            output = completed.stdout.strip()
            facts[name] = output if name == "head" else output.splitlines()
        except (OSError, subprocess.SubprocessError, ValueError) as exc:
            facts["error"] = f"{type(exc).__name__}: {exc}"
    return facts


def _digest(path: Path) -> dict:
    raw = path.read_bytes()
    return {"sha256": hashlib.sha256(raw).hexdigest(), "bytes": len(raw)}


# --------------------------------------------------------------------------- evaluation


def evaluate(
    engine_factory,
    queries_path: Path,
    *,
    limit: int = 10,
    plans_dir: Path | None = None,
    link_samples: int = 40,
    seed: int = 20260911,
    repeat: int = 1,
    trace_memory: bool = False,
    configurations: tuple[str, ...] = CONFIGURATIONS,
) -> dict:
    """Run every configuration and the link-recovery study on one engine."""
    if not 1 <= limit <= 100:
        raise ValueError("limit must be between 1 and 100")
    if link_samples < 0:
        raise ValueError("link_samples must be nonnegative")
    unknown = sorted(set(configurations) - set(CONFIGURATIONS))
    if unknown:
        raise ValueError(f"unknown configurations: {', '.join(unknown)}")
    queries_path = queries_path.resolve()
    fixture = load_fixture(queries_path)
    cases = fixture["queries"]
    started_all = time.perf_counter()
    if trace_memory and not tracemalloc.is_tracing():
        tracemalloc.start()
    started = time.perf_counter()
    engine = engine_factory()
    build_seconds = time.perf_counter() - started
    report: dict[str, Any] = {
        "schema": SCHEMA,
        "created_at": datetime.now(UTC).isoformat(),
        "status": "ok",
        "errors": [],
    }
    try:
        root = Path(getattr(engine, "root", ROOT))
        report["root"] = str(root)
        report["git"] = git_facts(root)
        report["fixture"] = {
            "path": str(queries_path),
            **_digest(queries_path),
            "schema": fixture.get("schema"),
            "kind": fixture_kind(fixture),
            "source_commit": fixture.get("source_commit"),
            "queries": len(cases),
            "positive_queries": sum(not case.get("expect_empty") for case in cases),
            "negative_controls": sum(bool(case.get("expect_empty")) for case in cases),
            "groups": sorted({str(case.get("group", "ungrouped")) for case in cases}),
        }
        report["evidence"] = (
            "Held-out fixture: queries were authored before tuning; results are test evidence."
            if report["fixture"]["kind"] == "held-out"
            else "Development fixture: regression evidence only, not held-out evidence."
        )
        # The first search rehashes every source so an edit after the cache was
        # built is visible; later searches reuse that observation for speed.
        warm = engine.search(cases[0]["query"], limit=limit)
        provenance = warm.get("provenance", {})
        engine.recheck_freshness = False
        report["discovery"] = {
            "fingerprint": provenance.get("fingerprint"),
            "current_fingerprint": provenance.get("current_fingerprint"),
            "freshness": provenance.get("freshness"),
            "freshness_observation": provenance.get("freshness_observation"),
            "cache_reused": provenance.get("cache_reused"),
            "cache_path": provenance.get("cache_path"),
            "source_count": provenance.get("source_count"),
            "passage_count": provenance.get("passage_count"),
            "record_count": provenance.get("record_count"),
            "edge_count": provenance.get("edge_count"),
            "recheck_freshness": (
                "Sources were rehashed for the unscored warm-up query only; "
                "engine.recheck_freshness was then set to False for every scored query."
            ),
        }
        expander, lexicon_status, lexicon_facts = lexicon_expander(root)
        plans, plan_problems = load_plans(plans_dir, [case["id"] for case in cases])
        report["inputs"] = {
            "lexicon": {"path": LEXICON_PATH, "status": lexicon_status, **lexicon_facts},
            "plans": {
                "directory": str(plans_dir) if plans_dir else None,
                "query_ids_with_plans": sorted(plans),
                "problems": plan_problems,
            },
        }
        report["configurations"] = {}
        for name in configurations:
            unavailable = None
            if name in ("lexical+lexicon", "lexical+graph+lexicon") and expander is None:
                unavailable = f"lexicon {lexicon_status}"
            if name == "plans" and not plans:
                unavailable = "no query plans supplied" if plans_dir is None else "no plan matched"
            if unavailable:
                report["configurations"][name] = {
                    "status": "unavailable",
                    "reason": unavailable,
                    "description": describe(name),
                }
                continue
            data = run_configuration(engine, name, cases, limit, expander, plans, repeat)
            report["configurations"][name] = {
                "status": "ran",
                "description": describe(name),
                "summary": data["summary"],
                "rows": data["rows"],
            }
            for row in data["rows"]:
                if row["error"]:
                    report["errors"].append(
                        {"configuration": name, "query_id": row["query_id"], "error": row["error"]}
                    )
        report["per_query"] = per_query_table(report["configurations"], cases)
        report["leakage"] = leakage_check(cases)
        if link_samples:
            started = time.perf_counter()
            report["link_recovery"] = link_recovery(engine, link_samples, seed)
            report["link_recovery"]["seconds"] = time.perf_counter() - started
            for row in report["link_recovery"]["rows"]:
                if row["error"]:
                    report["errors"].append(
                        {"link_recovery": f"{row['src']} -> {row['dst']}", "error": row["error"]}
                    )
        else:
            report["link_recovery"] = {"skipped": True, "requested_samples": 0}
    finally:
        with_close = getattr(engine, "close", None)
        if callable(with_close):
            with_close()
    report["memory"] = memory_probe()
    if trace_memory and tracemalloc.is_tracing():
        tracemalloc.stop()
    report["timings"] = {
        "engine_build_seconds": build_seconds,
        "total_seconds": time.perf_counter() - started_all,
        "repeat": repeat,
        "note": (
            "Each scored query ran once per repeat in a reused process after one warm-up; "
            "medians over queries are reported per configuration."
            + (
                " tracemalloc was active; it inflated wall times four- to eight-fold on the "
                "2026-09-11 development run, so compare timings only with untraced runs."
                if trace_memory
                else " tracemalloc was off; peak memory comes from the process counters."
            )
        ),
    }
    report["measurement"] = {
        "recall_at_k": "Fraction of positive queries with a listed relevant hit in the top k.",
        "mrr_at_k": "Mean reciprocal first relevant rank; zero for misses and errors.",
        "negative_controls": (
            "Passed (empty): no primary hit. Passed (below median): top score below the "
            "median top score of positive queries in the same configuration."
        ),
        "source_diversity": "Mean distinct source families among the top-k primary hits.",
        "cross_family": (
            "Fraction of assessed positive queries whose first relevant hit lies outside the "
            "families implied by the query group."
        ),
        "scores": "Retrieval relevance only; never proof, support or scientific status.",
        "graph_writes": "None; the saved scientific graph and index are read only.",
    }
    report["execution"] = {"python_checks": 0, "lean": False, "scientific_index_written": False}
    if report["errors"]:
        report["status"] = "error"
    return report


def describe(name: str) -> str:
    return {
        "lexical": "engine.search(q, graph_weight=0, related_limit=0)",
        "lexical+graph": "engine.search(q) with default graph channel",
        "lexical+lexicon": "lexical with queries=discovery_lexicon.expand(q)['sub_queries']",
        "lexical+graph+lexicon": "default search with lexicon sub-queries",
        "plans": "default search with an agent plan's sub-queries and weights where present",
    }[name]


def per_query_table(configurations: dict, cases: list[dict]) -> list[dict]:
    """First relevant rank per query and configuration, one row per query."""
    table = []
    for case in cases:
        entry: dict[str, Any] = {
            "query_id": case["id"],
            "group": case.get("group", "ungrouped"),
            "negative_control": bool(case.get("expect_empty")),
            "ranks": {},
            "seconds": {},
        }
        for name, data in configurations.items():
            if data.get("status") != "ran":
                entry["ranks"][name] = "unavailable"
                continue
            row = next(row for row in data["rows"] if row["query_id"] == case["id"])
            entry["ranks"][name] = row["first_relevant_rank"] if not row["error"] else "error"
            entry["seconds"][name] = row.get("warm_query_seconds")
            if entry["negative_control"]:
                entry["ranks"][name] = f"hits={row['returned_hits']}"
        table.append(entry)
    return table


# --------------------------------------------------------------------------- rendering


def _pct(value: float | None) -> str:
    return "n/a" if value is None else f"{100 * value:.0f}%"


def _num(value: float | None, digits: int = 3) -> str:
    return "n/a" if value is None or not math.isfinite(value) else f"{value:.{digits}f}"


def render_markdown(report: dict) -> str:
    """A readable summary that repeats the report's own caveats."""
    fixture = report.get("fixture", {})
    git = report.get("git", {})
    discovery = report.get("discovery", {})
    lines = [
        "# Discovery evaluation",
        "",
        f"- Status: {report.get('status')}",
        f"- Evidence: {report.get('evidence')}",
        f"- Fixture: `{fixture.get('path')}` sha256 `{fixture.get('sha256')}` "
        f"({fixture.get('queries')} queries, {fixture.get('positive_queries')} positive, "
        f"{fixture.get('negative_controls')} negative)",
        f"- Git HEAD: `{git.get('head')}`; dirty paths: "
        f"{len(git.get('status_short') or [])}"
        + (f"; git error: {git.get('error')}" if git.get("error") else ""),
        f"- Discovery cache: `{discovery.get('fingerprint')}` freshness "
        f"{discovery.get('freshness')} ({discovery.get('freshness_observation')})",
        f"- {discovery.get('recheck_freshness')}",
        "",
        "## Configurations",
        "",
        "| configuration | status | recall@k | MRR@k | recall incl. related | neg. empty | "
        "neg. below median | neg. weak-match (positives flagged) | families/top-k | "
        "cross-family | median s |",
        "|---|---|---|---|---|---|---|---|---|---|---|",
    ]
    for name, data in report.get("configurations", {}).items():
        if data.get("status") != "ran":
            lines.append(f"| {name} | unavailable: {data.get('reason')} | | | | | | | | | |")
            continue
        s = data["summary"]
        negatives = s["negative_controls"]
        lines.append(
            f"| {name} | ran | {_pct(s['recall_at_k'])} | {_num(s['mrr_at_k'])} | "
            f"{_pct(s.get('recall_with_related'))} "
            f"(+{s.get('relevant_only_in_related', 0)}) | "
            f"{s['negative_controls_passed']}/{negatives} | "
            f"{s['negative_controls_passed_below_median']}/{negatives} | "
            f"{s.get('negative_controls_passed_weak_match', 0)}/{negatives} "
            f"({s.get('positives_flagged_weak_match', 0)}) | "
            f"{_num(s['mean_distinct_families_top_k'], 2)} | "
            f"{s['cross_family_hits']}/{s['cross_family_assessed']} | "
            f"{_num(s['median_warm_query_seconds'])} |"
        )
    names = [
        name
        for name, data in report.get("configurations", {}).items()
        if data.get("status") == "ran"
    ]
    lines.extend(["", "## First relevant rank per query", ""])
    lines.append("| query | group | " + " | ".join(names) + " |")
    lines.append("|---|---|" + "---|" * len(names))
    for entry in report.get("per_query", []):
        cells = [str(entry["ranks"].get(name, "")) for name in names]
        cells = ["miss" if cell == "None" else cell for cell in cells]
        lines.append(f"| {entry['query_id']} | {entry['group']} | " + " | ".join(cells) + " |")
    link = report.get("link_recovery", {})
    lines.extend(["", "## Link recovery (hidden registered edges)", ""])
    if link.get("skipped"):
        lines.append("Skipped.")
    else:
        lines.append(
            f"{link.get('samples')} of {link.get('eligible_edges')} eligible curated edges "
            f"(seed {link.get('seed')}, limit {link.get('limit')}, "
            f"{link.get('errors')} errors, {_num(link.get('seconds'), 1)} s)."
        )
        lines.extend(["", "| variant | slice | n | @5 | @20 | MRR |", "|---|---|---|---|---|---|"])
        for variant, data in link.get("variants", {}).items():
            slices = [("overall", data["overall"])]
            slices += list(data["by_type"].items())
            slices += list(data["by_family"].items())
            for label, s in slices:
                lines.append(
                    f"| {variant} | {label} | {s['samples']} | {_pct(s['recovered_at_5'])} | "
                    f"{_pct(s['recovered_at_20'])} | {_num(s['mrr'])} |"
                )
        method = link.get("method", {})
        lines.extend(["", f"Method: {method.get('hidden')} {method.get('meaning')}"])
    leakage = report.get("leakage", {})
    lines.extend(
        [
            "",
            "## Leakage check",
            "",
            f"{leakage.get('leaking_queries')} of {leakage.get('positive_queries')} positive "
            "queries contain an expected path stem or claim id; "
            f"{leakage.get('exact_id_queries', 0)} exact-control queries consist of their id "
            "(listed, not counted).",
        ]
    )
    for row in leakage.get("rows", []):
        leaks = ", ".join(f"{leak['kind']} {leak['value']}" for leak in row["leaks"])
        lines.append(f"- {row['query_id']}: {leaks}")
    memory = report.get("memory", {})
    timings = report.get("timings", {})

    def mb(value):
        return "n/a" if value is None else f"{value / 1e6:.0f} MB"

    lines.extend(
        [
            "",
            "## Resources",
            "",
            f"- Engine build: {_num(timings.get('engine_build_seconds'), 2)} s; "
            f"total: {_num(timings.get('total_seconds'), 1)} s; repeat {timings.get('repeat')}",
            f"- tracemalloc peak: {mb(memory.get('tracemalloc_peak_bytes'))}; "
            f"working set: {mb(memory.get('working_set_bytes'))}; "
            f"peak working set: {mb(memory.get('peak_working_set_bytes'))} "
            f"({memory.get('working_set_source') or memory.get('working_set_error') or 'n/a'})",
            f"- {timings.get('note')}",
            "",
            "## Meaning",
            "",
            f"- {report.get('measurement', {}).get('scores')}",
            f"- {report.get('measurement', {}).get('negative_controls')}",
            f"- {report.get('measurement', {}).get('cross_family')}",
            f"- {report.get('measurement', {}).get('graph_writes')}",
        ]
    )
    return "\n".join(lines) + "\n"


# --------------------------------------------------------------------------- command line


def add_arguments(parser: argparse.ArgumentParser) -> argparse.ArgumentParser:
    parser.add_argument(
        "--queries",
        type=Path,
        default=None,
        help=f"query fixture (default {DEFAULT_FIXTURE}; absent fixtures are skipped)",
    )
    parser.add_argument("--limit", type=int, default=10, help="primary hits scored per query")
    parser.add_argument("--out", type=Path, help="new JSON report path; never overwritten")
    parser.add_argument(
        "--markdown", type=Path, help="new Markdown summary path; never overwritten"
    )
    parser.add_argument("--plans", type=Path, help="directory of <query id>.json query plans")
    parser.add_argument("--link-samples", type=int, default=40, help="hidden edges to sample")
    parser.add_argument("--seed", type=int, default=20260911, help="edge sampling seed")
    parser.add_argument("--repeat", type=int, default=1, help="timed calls per query")
    parser.add_argument(
        "--tracemalloc",
        action="store_true",
        help="also trace Python allocations; inflates wall times several-fold",
    )
    parser.add_argument(
        "--configurations",
        default=",".join(CONFIGURATIONS),
        help="comma-separated subset of " + ", ".join(CONFIGURATIONS),
    )
    parser.add_argument(
        "--require-fixture", action="store_true", help="treat an absent fixture as an error"
    )
    return parser


def add_parser(subparsers):
    """Register ``evaluate`` under ``workhouse discover``."""
    parser = subparsers.add_parser(
        "evaluate",
        help="compare retrieval configurations and link recovery on a frozen query fixture",
    )
    return add_arguments(parser)


def run(args, engine_factory) -> int:
    """Evaluate with a caller-built engine; ``engine_factory()`` returns a DiscoveryEngine."""
    root = Path(getattr(args, "root", None) or ROOT)
    queries = Path(args.queries) if args.queries else root / DEFAULT_FIXTURE
    if not queries.is_file():
        message = {
            "status": "skipped",
            "reason": f"query fixture absent: {queries}",
            "hint": f"pass --queries {DEVELOPMENT_FIXTURE} for development-regression numbers",
        }
        print(json.dumps(message))
        return 2 if getattr(args, "require_fixture", False) else 0
    for path in (args.out, getattr(args, "markdown", None)):
        if path is not None and Path(path).exists():
            print(json.dumps({"status": "error", "error": f"output already exists: {path}"}))
            return 1
    if not 1 <= args.limit <= 100:
        print(json.dumps({"status": "error", "error": "--limit must be between 1 and 100"}))
        return 1
    configurations = tuple(
        name.strip() for name in str(args.configurations).split(",") if name.strip()
    )
    try:
        report = evaluate(
            engine_factory,
            queries,
            limit=args.limit,
            plans_dir=Path(args.plans) if getattr(args, "plans", None) else None,
            link_samples=args.link_samples,
            seed=args.seed,
            repeat=args.repeat,
            trace_memory=bool(getattr(args, "tracemalloc", False)),
            configurations=configurations,
        )
    except (OSError, ValueError) as exc:
        print(json.dumps({"status": "error", "error": f"{type(exc).__name__}: {exc}"}))
        return 1
    if args.out is not None:
        write_report(Path(args.out), report)
    if getattr(args, "markdown", None):
        path = Path(args.markdown)
        path.parent.mkdir(parents=True, exist_ok=True)
        with path.open("x", encoding="utf-8", newline="\n") as handle:
            handle.write(render_markdown(report))
    summary = {
        "status": report["status"],
        "evidence": report["evidence"],
        "out": str(args.out) if args.out else None,
        "configurations": {
            name: (
                {
                    key: data["summary"][key]
                    for key in ("recall_at_k", "mrr_at_k", "median_warm_query_seconds")
                }
                if data["status"] == "ran"
                else data["reason"]
            )
            for name, data in report["configurations"].items()
        },
        "link_recovery": {
            variant: data["overall"]
            for variant, data in report["link_recovery"].get("variants", {}).items()
        },
        "leaking_queries": report["leakage"]["leaking_queries"],
    }
    print(json.dumps(summary, indent=2))
    return 0 if report["status"] == "ok" else 1


def write_report(path: Path, report: dict) -> None:
    """Exclusive creation keeps every earlier evaluation artifact."""
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("x", encoding="utf-8", newline="\n") as handle:
        json.dump(report, handle, indent=2, ensure_ascii=False, sort_keys=True)
        handle.write("\n")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=ROOT, help="checkout to evaluate")
    add_arguments(parser)
    args = parser.parse_args(argv)
    root = args.root.resolve()
    sys.path.insert(0, str(root / "src"))
    from workhouse import discovery

    # Evaluating another checkout's engine against this checkout's fixture
    # would report numbers no commit here can reproduce.
    if not Path(discovery.__file__).resolve().is_relative_to(root):
        parser.error("workhouse imports must resolve inside the selected checkout")

    def engine_factory():
        return discovery.DiscoveryEngine(root)

    args.root = root
    return run(args, engine_factory)


if __name__ == "__main__":
    raise SystemExit(main())
