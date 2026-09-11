"""Small synthetic relevance tests; never build or search the real corpus."""

from __future__ import annotations

import importlib.util
import json
from pathlib import Path

import pytest

SCRIPT = Path(__file__).resolve().parents[1] / "scripts/benchmark_discovery.py"
spec = importlib.util.spec_from_file_location("benchmark_discovery", SCRIPT)
assert spec and spec.loader
benchmark = importlib.util.module_from_spec(spec)
spec.loader.exec_module(benchmark)


def case(**kwargs):
    return {"id": "q", "query": "find this", "expected_claim_ids": ["DERIV:A"], **kwargs}


def test_metrics_use_first_relevant_rank_and_count_misses():
    found = benchmark.score_query([{"id": "x"}, {"claim_ids": ["DERIV:A"]}], case(), 3)
    missed = benchmark.score_query([{"id": "x"}], case(id="missing"), 3)
    assert found["first_relevant_rank"] == 2
    summary = benchmark.summarize([found, missed], 3)
    assert summary["recall_at_k"] == 0.5
    assert summary["mrr_at_k"] == 0.25


def test_relevant_hit_beyond_k_is_a_miss_and_duplicates_do_not_boost_score():
    hits = [{"id": "x"}, {"id": "DERIV:A"}, {"id": "DERIV:A"}]
    assert benchmark.score_query(hits, case(), 1)["reciprocal_rank"] == 0
    assert benchmark.score_query(hits, case(), 3)["reciprocal_rank"] == 0.5


def test_path_relevance_normalizes_locations_and_requires_text_marker():
    query = case(
        expected_claim_ids=[],
        expected_paths=["docs/derivations/a.md"],
        text_any=["conditional score"],
    )
    assert benchmark.is_relevant(
        {"where": "docs\\derivations\\a.md:21-29", "text": "Conditional score bound"}, query
    )
    assert not benchmark.is_relevant(
        {"path": "docs/derivations/a.md.other", "text": "conditional score"}, query
    )
    assert not benchmark.is_relevant(
        {"path": "docs/derivations/a.md", "text": "unrelated chapter"}, query
    )


def test_claim_ids_in_prose_are_not_counted_as_returned_claims():
    assert not benchmark.is_relevant({"id": "other", "text": "see DERIV:A"}, case())
    assert benchmark.is_relevant({"claim": "DERIV:A"}, case())


def test_matching_passage_can_supply_actual_source_and_marker():
    query = case(expected_claim_ids=[], expected_paths=["docs/source.md"], text_any=["score"])
    assert benchmark.is_relevant(
        {
            "id": "other",
            "matching_passage": {"where": "docs/source.md (lines 5-9)", "text": "score theorem"},
        },
        query,
    )


def test_negative_controls_and_errors_are_not_silent_successes():
    negative = case(id="empty", expected_claim_ids=[], expect_empty=True)
    passed = benchmark.score_query([], negative, 10)
    failed = benchmark.score_query([{"id": "unexpected"}], negative, 10)
    errored = benchmark.score_query([], case(), 10, "RuntimeError: failed")
    summary = benchmark.summarize([passed, failed, errored], 10)
    assert summary["positive_queries"] == 1
    assert summary["negative_controls_passed"] == 1
    assert summary["error_queries"] == 1
    assert summary["recall_at_k"] == 0
    assert summary["mrr_at_k"] == 0


def test_empty_positive_population_is_unavailable_not_perfect():
    assert benchmark.summarize([], 10)["recall_at_k"] is None
    assert benchmark.summarize([], 10)["mrr_at_k"] is None


def test_frozen_fixture_is_well_formed_and_keeps_both_controls():
    fixture = benchmark.load_queries(SCRIPT.parents[1] / "tests/fixtures/discovery_queries.json")
    groups = {query["group"] for query in fixture["queries"]}
    assert {
        "derivation_discovery",
        "imported_discovery",
        "theory_discovery",
        "exact_control",
        "negative_control",
    } <= groups
    assert all("source_review" in query for query in fixture["queries"])


def test_fixture_rejects_duplicate_ids(tmp_path):
    path = tmp_path / "queries.json"
    path.write_text(
        json.dumps({"schema": benchmark.FIXTURE_SCHEMA, "queries": [case(), case()]}),
        encoding="utf-8",
    )
    with pytest.raises(ValueError, match="unique"):
        benchmark.load_queries(path)


def test_report_refuses_to_overwrite(tmp_path):
    path = tmp_path / "report.json"
    benchmark.write_report(path, {"original": True})
    before = path.read_bytes()
    with pytest.raises(FileExistsError):
        benchmark.write_report(path, {"replacement": True})
    assert path.read_bytes() == before


def test_missing_saved_input_stops_before_importing_or_collecting(tmp_path):
    fixture = SCRIPT.parents[1] / "tests/fixtures/discovery_queries.json"
    with pytest.raises(FileNotFoundError):
        benchmark.run_benchmark(tmp_path, fixture)


def test_related_graph_suggestions_do_not_inflate_primary_hit_metrics():
    data = benchmark._evaluate(
        [case()],
        lambda query, limit: {
            "hits": [{"id": "unrelated"}],
            "related": [{"id": "DERIV:A"}],
        },
        10,
    )
    assert data["summary"]["recall_at_k"] == 0
    assert data["summary"]["mrr_at_k"] == 0
    assert data["queries"][0]["related_first_relevant_rank"] == 1
    assert data["queries"][0]["related"][0]["id"] == "DERIV:A"
