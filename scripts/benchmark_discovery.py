"""Compare frozen retrieval queries using saved graph inputs; never collect checks.

Run explicitly from a checkout. The unit tests exercise scoring helpers only.
The benchmark compares systems with different source scopes, so its end-to-end
scores are not an isolated measure of the ranking algorithm.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import statistics
import sys
import time
from collections import defaultdict
from contextlib import contextmanager
from datetime import UTC, datetime
from pathlib import Path

SCHEMA = "workhouse-discovery-benchmark-result/v1"
FIXTURE_SCHEMA = "workhouse-discovery-benchmark/v1"
ROOT = Path(__file__).resolve().parents[1]
SAVED_INPUTS = ("index/claims.jsonl", "index/graph.jsonl", "index/symbols.jsonl")


def load_queries(path: Path) -> dict:
    payload = json.loads(path.read_text(encoding="utf-8"))
    if payload.get("schema") != FIXTURE_SCHEMA:
        raise ValueError("unsupported discovery query fixture schema")
    cases = payload.get("queries")
    if not isinstance(cases, list) or not cases:
        raise ValueError("query fixture must contain a nonempty queries list")
    seen = set()
    for case in cases:
        if not isinstance(case, dict) or not isinstance(case.get("id"), str):
            raise ValueError("each query needs a string id")
        if not case["id"] or case["id"] in seen:
            raise ValueError("query ids must be nonempty and unique")
        seen.add(case["id"])
        if not isinstance(case.get("query"), str) or not case["query"].strip():
            raise ValueError(f"query {case['id']} needs nonempty query text")
        if not case.get("expect_empty") and not (
            case.get("expected_claim_ids") or case.get("expected_paths")
        ):
            raise ValueError(f"query {case['id']} has no relevance target")
        for field in ("expected_claim_ids", "expected_paths", "text_any"):
            values = case.get(field, [])
            if not isinstance(values, list) or any(
                not isinstance(value, str) or not value for value in values
            ):
                raise ValueError(f"query {case['id']} has invalid {field}")
        if case.get("expect_empty") and (
            case.get("expected_claim_ids") or case.get("expected_paths")
        ):
            raise ValueError("negative controls cannot have positive targets")
    return payload


def _normal_path(value: str) -> str:
    value = value.replace("\\", "/").split(" (", 1)[0].split("#", 1)[0]
    value = re.sub(r":\d+(?:[-–]\d+)?$", "", value)
    return value.removeprefix("./")


def _path_matches(path: str, prefix: str) -> bool:
    path, prefix = _normal_path(path), _normal_path(prefix)
    return path == prefix or path.startswith(prefix.rstrip("/") + "/")


def is_relevant(hit: dict, case: dict) -> bool:
    """Accept listed IDs or source locators; never mine IDs from explanatory text."""
    if case.get("expect_empty"):
        return False
    ids = {hit.get("id", ""), hit.get("claim", "")}
    ids.update(hit.get("claim_ids") or [])
    if ids.intersection(case.get("expected_claim_ids", [])):
        return True
    paths = [hit.get("path", ""), hit.get("where", "")]
    passage = hit.get("matching_passage")
    if isinstance(passage, dict):
        paths.extend([passage.get("path", ""), passage.get("where", "")])
    if not any(
        _path_matches(path, prefix) for path in paths for prefix in case.get("expected_paths", [])
    ):
        return False
    markers = case.get("text_any", [])
    text = hit.get("text", "")
    if isinstance(passage, dict):
        text += " " + passage.get("text", "")
    return not markers or any(marker.casefold() in text.casefold() for marker in markers)


def score_query(hits: list[dict], case: dict, limit: int, error: str | None = None) -> dict:
    if limit <= 0:
        raise ValueError("limit must be positive")
    ranked = hits[:limit]
    first = next((i for i, hit in enumerate(ranked, 1) if is_relevant(hit, case)), None)
    negative = bool(case.get("expect_empty"))
    return {
        "query_id": case["id"],
        "group": case.get("group", "ungrouped"),
        "query": case["query"],
        "negative_control": negative,
        "first_relevant_rank": first if not error else None,
        "reciprocal_rank": 1.0 / first if first and not error else 0.0,
        "any_relevant_hit": bool(first) and not bool(error),
        "returned_hits": len(ranked),
        "empty_control_passed": not ranked and not error if negative else None,
        "error": error,
    }


def summarize(rows: list[dict], limit: int) -> dict:
    """Recall is query success (any relevant hit), not exhaustive document recall."""
    positive = [row for row in rows if not row["negative_control"]]
    negative = [row for row in rows if row["negative_control"]]
    timings = [row["warm_query_seconds"] for row in rows if "warm_query_seconds" in row]
    return {
        "limit": limit,
        "positive_queries": len(positive),
        "recall_at_k": (
            sum(row["any_relevant_hit"] for row in positive) / len(positive) if positive else None
        ),
        "mrr_at_k": (
            sum(row["reciprocal_rank"] for row in positive) / len(positive) if positive else None
        ),
        "successful_queries": sum(row["any_relevant_hit"] for row in positive),
        "negative_controls": len(negative),
        "negative_controls_passed": sum(bool(row["empty_control_passed"]) for row in negative),
        "error_queries": sum(bool(row["error"]) for row in rows),
        "mean_warm_query_seconds": statistics.mean(timings) if timings else None,
        "median_warm_query_seconds": statistics.median(timings) if timings else None,
    }


def _digest(path: Path) -> dict:
    raw = path.read_bytes()
    return {"sha256": hashlib.sha256(raw).hexdigest(), "bytes": len(raw)}


def _fingerprint(manifest: dict) -> str:
    return hashlib.sha256(json.dumps(manifest, sort_keys=True).encode()).hexdigest()


def _indexed_corpus_fingerprint(chunks) -> str:
    """Hash exactly the baseline's indexed content, including its token stream."""
    digest = hashlib.sha256()
    for chunk in chunks:
        row = [chunk.where, chunk.claim, chunk.text, chunk.tokens]
        digest.update(json.dumps(row, ensure_ascii=True, separators=(",", ":")).encode())
        digest.update(b"\n")
    return digest.hexdigest()


def _compact(hit: dict) -> dict:
    fields = ("id", "claim", "claim_ids", "path", "where", "text", "score", "score_channels")
    result = {key: hit[key] for key in fields if key in hit}
    if "text" in result:
        result["text"] = result["text"][:1200]
    passage = hit.get("matching_passage")
    if isinstance(passage, dict):
        result["matching_passage"] = {
            key: passage[key] for key in ("id", "path", "where", "text") if key in passage
        }
    return result


@contextmanager
def _finder_root(finder, root: Path):
    """Route baseline prose to the selected checkout without its on-disk cache."""
    names = {
        "ROOT": root,
        "CORPUS_DIR": root / "corpus-import",
        "PAPER_DIR": root / "paper",
        "DECISIONS_DIR": root / "docs/decisions",
    }
    previous = {name: getattr(finder, name) for name in names}
    try:
        for name, value in names.items():
            setattr(finder, name, value)
        yield
    finally:
        for name, value in previous.items():
            setattr(finder, name, value)


def _evaluate(cases: list[dict], search, limit: int) -> dict:
    rows = []
    for case in cases:
        started = time.perf_counter()
        error, hits, related = None, [], None
        try:
            response = search(case["query"], limit)
            if isinstance(response, dict):
                hits = response["hits"]
                related = response.get("related")
            else:
                hits = response
        except Exception as exc:  # Preserve individual query failures in the result artifact.
            error = f"{type(exc).__name__}: {exc}"
        elapsed = time.perf_counter() - started
        result = score_query(hits, case, limit, error)
        result["warm_query_seconds"] = elapsed
        result["hits"] = [_compact(hit) for hit in hits[:limit]]
        if related is not None:
            result["related"] = [_compact(hit) for hit in related]
            result["related_first_relevant_rank"] = next(
                (i for i, hit in enumerate(related, 1) if is_relevant(hit, case)), None
            )
            result["related_note"] = (
                "Graph suggestions are reported separately and do not affect primary hit metrics."
            )
        rows.append(result)
    groups: dict[str, list] = defaultdict(list)
    for row in rows:
        groups[row["group"]].append(row)
    return {
        "summary": summarize(rows, limit),
        "groups": {name: summarize(group, limit) for name, group in sorted(groups.items())},
        "queries": rows,
    }


def run_benchmark(root: Path, queries_path: Path, limit: int = 10) -> dict:
    """Build each system once, warm its process, and run identical frozen queries."""
    if not 1 <= limit <= 100:
        raise ValueError("limit must be between 1 and 100")
    root, queries_path = root.resolve(), queries_path.resolve()
    fixture = load_queries(queries_path)
    before = {name: _digest(root / name) for name in SAVED_INPUTS}
    # Do not call load_catalogue(): it can collect checks when its input is missing.
    from workhouse import finder
    from workhouse.claims import Claim

    if not Path(finder.__file__).resolve().is_relative_to(root):
        raise ValueError("workhouse imports must resolve inside the selected checkout")
    catalogue = [
        Claim(**json.loads(line))
        for line in (root / SAVED_INPUTS[0]).read_text(encoding="utf-8").splitlines()
        if line.strip()
    ]
    report = {
        "schema": SCHEMA,
        "created_at": datetime.now(UTC).isoformat(),
        "root": str(root),
        "queries": {
            "path": str(queries_path),
            **_digest(queries_path),
            "source_commit": fixture.get("source_commit"),
            "selection": fixture.get("selection"),
        },
        "saved_inputs": before,
        "reviewed_source_manifest": {
            path: (_digest(root / path) if (root / path).is_file() else {"unavailable": True})
            for path in sorted(
                {
                    case["source_review"]["path"]
                    for case in fixture["queries"]
                    # Negative controls record "none": nothing to hash.
                    if case.get("source_review", {}).get("path") not in (None, "", "none")
                }
            )
        },
        "implementation_manifest": {
            path: _digest(root / path)
            for path in (
                "scripts/benchmark_discovery.py",
                "src/workhouse/finder.py",
                "src/workhouse/discovery.py",
                "src/workhouse/discovery_index.py",
                "src/workhouse/discovery_graph.py",
            )
            if (root / path).is_file()
        },
        "saved_graph_fingerprint": _fingerprint(before),
        "execution": {"python_checks": 0, "lean": False, "scientific_index_written": False},
        "measurement": {
            "recall_at_k": "Fraction of positive queries with at least one listed relevant hit.",
            "mrr_at_k": "Mean reciprocal first relevant rank, zero for misses and errors.",
            "timing": (
                "One unscored warm-up, then each query once in a reused process. Setup may "
                "reuse a discovery cache; inspect provenance. This is not a repeated "
                "latency distribution."
            ),
            "scope": (
                "Finder and discovery have different prose scopes. An end-to-end gain "
                "may come from expanded corpus coverage, chunking, tokenization, diversity, "
                "or ranking. Exact controls are reported separately."
            ),
            "limitations": (
                "Purposive small fixture; targets chosen by source reading. Relevant "
                "sources are not exhaustively annotated. Scores measure retrieval, "
                "not mathematical correctness, novelty or proof status."
            ),
        },
        "systems": {},
        "errors": [],
    }
    cases = fixture["queries"]
    with _finder_root(finder, root):
        try:
            started = time.perf_counter()
            baseline = finder.build(catalogue=catalogue)
            build_seconds = time.perf_counter() - started
            finder.ask(cases[0]["query"], limit=limit, index=baseline)
            data = _evaluate(cases, lambda q, k: finder.ask(q, limit=k, index=baseline)[0], limit)
            data["build_seconds"] = build_seconds
            data["provenance"] = {
                "cache_reused": False,
                "chunk_count": len(baseline.chunks),
                "indexed_corpus_fingerprint": _indexed_corpus_fingerprint(baseline.chunks),
                "fingerprint_scope": "Ordered locator, claim ID, visible text, and token stream.",
                "prose_roots": ["corpus-import", "paper", "docs/decisions"],
                "catalogue_records": len(catalogue),
            }
            report["systems"]["finder"] = data
        except Exception as exc:
            report["errors"].append({"system": "finder", "error": f"{type(exc).__name__}: {exc}"})
    engine = None
    try:
        # Lazy import lets metric tests and baseline setup run without model dependencies.
        from workhouse.discovery import DiscoveryEngine

        started = time.perf_counter()
        engine = DiscoveryEngine(root)
        build_seconds = time.perf_counter() - started
        engine.search(cases[0]["query"], limit=limit)
        data = _evaluate(cases, lambda q, k: engine.search(q, limit=k), limit)
        data["build_seconds"] = build_seconds
        data["provenance"] = engine.index.metadata()
        report["systems"]["discovery"] = data
        lexical = _evaluate(cases, lambda q, k: engine.index.search(q, limit=k), limit)
        lexical["build_seconds"] = 0.0
        lexical["provenance"] = data["provenance"]
        lexical["interpretation"] = (
            "Same expanded index, lexical ranking only. Comparison with discovery also "
            "changes exact-match fusion and source diversity. Related graph suggestions "
            "are separate from the primary hit metrics. "
            "Build is reused; zero means no additional index construction."
        )
        report["systems"]["discovery_lexical"] = lexical
    except Exception as exc:
        report["errors"].append({"system": "discovery", "error": f"{type(exc).__name__}: {exc}"})
    finally:
        if engine is not None:
            engine.close()
    after = {name: _digest(root / name) for name in SAVED_INPUTS}
    report["saved_inputs_unchanged"] = before == after
    if before != after:
        report["errors"].append(
            {"system": "inputs", "error": "Saved graph changed during benchmark."}
        )
    report["status"] = (
        "error"
        if report["errors"]
        or any(data["summary"]["error_queries"] for data in report["systems"].values())
        else "ok"
    )
    return report


def write_report(path: Path, report: dict) -> None:
    """Exclusive creation preserves every earlier benchmark artifact."""
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("x", encoding="utf-8", newline="\n") as handle:
        json.dump(report, handle, indent=2, ensure_ascii=False, sort_keys=True)
        handle.write("\n")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=ROOT)
    parser.add_argument(
        "--queries", type=Path, default=ROOT / "tests/fixtures/discovery_queries.json"
    )
    parser.add_argument("--limit", type=int, default=10)
    parser.add_argument("--out", type=Path, required=True, help="New JSON path; never overwritten.")
    args = parser.parse_args(argv)
    if args.out.exists():
        parser.error(f"output already exists: {args.out}")
    if not 1 <= args.limit <= 100:
        parser.error("--limit must be between 1 and 100")
    sys.path.insert(0, str(args.root.resolve() / "src"))
    report = run_benchmark(args.root, args.queries, args.limit)
    write_report(args.out, report)
    print(
        json.dumps(
            {
                "status": report["status"],
                "out": str(args.out),
                "systems": {name: value["summary"] for name, value in report["systems"].items()},
            },
            indent=2,
        )
    )
    return 0 if report["status"] == "ok" else 1


if __name__ == "__main__":
    raise SystemExit(main())
