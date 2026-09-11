"""Evaluation harness semantics on a synthetic engine; never the real corpus."""

from __future__ import annotations

import argparse
import copy
import importlib.util
import json
import re
import sys
import types
from pathlib import Path

import pytest

from workhouse import discovery as D

SCRIPT = Path(__file__).resolve().parents[1] / "scripts/evaluate_discovery.py"
spec = importlib.util.spec_from_file_location("evaluate_discovery", SCRIPT)
assert spec and spec.loader
harness = importlib.util.module_from_spec(spec)
spec.loader.exec_module(harness)


def record(node, statement, where, **kwargs):
    return {"id": node, "kind": "result", "statement": statement, "where": where, **kwargs}


def edge(src, dst, type_="depends_on", how="curated"):
    return {"src": src, "dst": dst, "type": type_, "how": how, "source": "ledger/test.yaml"}


STATEMENTS = {
    "A": (
        "uniform score estimate for the conditional transport generator budget over rare "
        "coarse fibers of the synchronized radial flow"
    ),
    "B": (
        "canonical operator extension of the plaquette incidence matrix for the signed "
        "adjacency factorization in the retained sector"
    ),
    "C": (
        "a separate construction of matrix valued mass atoms from shrinking spectral islands "
        "after source normalization at separated times"
    ),
    "D": "short statement",
}
WHERE = {
    "A": "docs/derivations/a.md",
    "B": "theory/master.md",
    "C": "notes/imported/c.md",
    "D": "ledger/results.yaml",
}


class MemoryIndex:
    """A tiny lexical index: a hit per record sharing a long word with the query."""

    def __init__(self, root, cache_dir=None, **_):
        self.records = [record(node, STATEMENTS[node], WHERE[node]) for node in STATEMENTS]
        self.edges = [
            edge("B", "A"),
            edge("C", "B", "supported_by"),
            edge("A", "C", "bears_on"),
            edge("D", "A"),
            edge("B", "A", how="derived"),
            edge("B", "A", type_="cites"),
        ]
        self.symbols = []
        self.metadata_calls = []

    def build(self):
        return self.metadata()

    def metadata(self, check_current=True, *, recheck=True):
        self.metadata_calls.append(recheck)
        return {
            "fingerprint": "test-snapshot",
            "freshness": "matched",
            "freshness_observation": "rehashed" if recheck else "reused",
            "cache_reused": True,
        }

    def search(self, query, limit=100):
        tokens = {token for token in re.findall(r"[a-z]+", query.lower()) if len(token) > 3}
        hits = []
        for row in self.records:
            overlap = len(tokens & set(re.findall(r"[a-z]+", row["statement"].lower())))
            if overlap:
                hits.append(
                    {
                        "id": "chunk:" + row["id"],
                        "claim_ids": [row["id"]],
                        "kind": "record",
                        "path": row["where"],
                        "text": row["statement"],
                        "score": float(overlap),
                    }
                )
        if "unlinked" in tokens:
            hits.append(
                {
                    "id": "PASSAGE:1",
                    "claim_ids": [],
                    "kind": "passage",
                    "path": "literature/unlinked.md",
                    "start_line": 3,
                    "end_line": 5,
                    "text": "an unlinked literature passage",
                    "score": 0.5,
                }
            )
        hits.sort(key=lambda hit: (-hit["score"], hit["id"]))
        return hits[:limit]

    def close(self):
        pass


FIXTURE = {
    "schema": "workhouse-discovery-benchmark/v1",
    "queries": [
        {
            "id": "q_score",
            "group": "heldout_derivation",
            "query": "uniform score estimate",
            "expected_ids": ["A"],
        },
        {
            "id": "q_path",
            "group": "heldout_notes_literature",
            "query": "matrix valued mass atoms",
            "expected_paths": ["notes/imported/c.md"],
            "text_any": ["atom"],
            "terminology_note": "phrased in the note's own words",
        },
        {
            "id": "q_cross",
            "group": "heldout_historical",
            "query": "shrinking spectral islands",
            "expected_ids": ["C"],
        },
        {
            "id": "q_miss",
            "group": "heldout_derivation",
            "query": "nothing matches this",
            "expected_ids": ["ZZZ"],
        },
        {
            "id": "q_neg_empty",
            "group": "heldout_controls",
            "query": "zzzz absent token",
            "negative": True,
        },
        {
            "id": "q_neg_hit",
            "group": "heldout_controls",
            "query": "operator extension",
            "negative": True,
        },
    ],
}


@pytest.fixture
def fixture_path(tmp_path):
    path = tmp_path / "heldout.json"
    path.write_text(json.dumps(FIXTURE), encoding="utf-8")
    return path


@pytest.fixture
def factory(monkeypatch, tmp_path):
    monkeypatch.setattr(D, "DiscoveryIndex", MemoryIndex)
    built = []

    def make():
        engine = D.DiscoveryEngine(tmp_path)
        built.append(engine)
        return engine

    make.built = built
    return make


# ----------------------------------------------------------------------------- fixtures


def test_fixture_normalization_accepts_heldout_spellings(fixture_path):
    fixture = harness.load_fixture(fixture_path)
    cases = {case["id"]: case for case in fixture["queries"]}
    assert cases["q_neg_empty"]["expect_empty"] is True
    assert cases["q_score"]["expected_claim_ids"] == ["A"]
    assert cases["q_path"]["terminology_note"]
    assert harness.fixture_kind(fixture) == "held-out"


def test_fixture_rejects_wrong_schema_and_keeps_benchmark_rules(tmp_path):
    bad = tmp_path / "bad.json"
    bad.write_text(json.dumps({"schema": "other", "queries": []}), encoding="utf-8")
    with pytest.raises(ValueError):
        harness.load_fixture(bad)
    no_target = tmp_path / "no_target.json"
    payload = {"schema": FIXTURE["schema"], "queries": [{"id": "x", "query": "text"}]}
    no_target.write_text(json.dumps(payload), encoding="utf-8")
    with pytest.raises(ValueError):
        harness.load_fixture(no_target)


def test_development_fixture_is_not_mistaken_for_held_out():
    fixture = {"queries": [{"group": "derivation_discovery"}, {"group": "exact_control"}]}
    assert harness.fixture_kind(fixture) == "development"


# ----------------------------------------------------------------------------- metrics


def test_configurations_score_recall_negatives_diversity_and_cross_family(factory, fixture_path):
    report = harness.evaluate(factory, fixture_path, link_samples=0, trace_memory=False)
    lexical = report["configurations"]["lexical"]["summary"]
    assert lexical["positive_queries"] == 4
    assert lexical["recall_at_k"] == pytest.approx(0.75)
    assert lexical["mrr_at_k"] == pytest.approx(0.75)
    assert lexical["negative_controls"] == 2
    assert lexical["negative_controls_passed"] == 1
    assert lexical["negative_controls_passed_below_median"] == 1
    assert lexical["mean_distinct_families_top_k"] >= 1
    rows = {row["query_id"]: row for row in report["configurations"]["lexical"]["rows"]}
    assert rows["q_score"]["relevant_family"] == "docs"
    assert rows["q_score"]["cross_family"] is False
    assert rows["q_cross"]["relevant_family"] == "notes"
    assert rows["q_cross"]["cross_family"] is True
    assert rows["q_miss"]["first_relevant_rank"] is None
    assert rows["q_miss"]["cross_family"] is None
    assert lexical["cross_family_assessed"] == 3
    assert lexical["cross_family_hits"] == 1
    table = {entry["query_id"]: entry for entry in report["per_query"]}
    assert table["q_score"]["ranks"]["lexical"] == 1
    assert table["q_miss"]["ranks"]["lexical"] is None
    assert table["q_neg_hit"]["ranks"]["lexical"] == "hits=1"
    assert report["evidence"].startswith("Held-out")
    assert report["execution"]["python_checks"] == 0


def test_graph_configuration_runs_with_default_search_and_lexicon_is_reported_absent(
    factory, fixture_path
):
    report = harness.evaluate(factory, fixture_path, link_samples=0, trace_memory=False)
    assert report["configurations"]["lexical+graph"]["status"] == "ran"
    unavailable = report["configurations"]["lexical+lexicon"]
    assert unavailable["status"] == "unavailable"
    assert "absent" in unavailable["reason"]
    assert report["configurations"]["plans"]["status"] == "unavailable"
    assert report["per_query"][0]["ranks"]["plans"] == "unavailable"
    assert report["inputs"]["lexicon"]["status"].endswith("absent")


def test_first_query_rehashes_then_freshness_rechecks_stop(factory, fixture_path):
    report = harness.evaluate(factory, fixture_path, link_samples=0, trace_memory=False)
    engine = factory.built[0]
    assert engine.recheck_freshness is False
    calls = engine.index.metadata_calls
    assert calls[1] is True  # the warm-up search rehashed the sources
    assert all(recheck is False for recheck in calls[2:])
    assert "recheck_freshness" in report["discovery"]
    assert report["discovery"]["freshness_observation"] == "rehashed"


def test_hit_family_labels_external_records_and_passages():
    assert harness.hit_family({"external": True, "source_label": "outer"}) == "ext:outer"
    assert harness.hit_family({"path": "docs/derivations/a.md"}) == "docs"
    assert harness.hit_family({"where": "theory\\master.md:12"}) == "theory"
    assert harness.hit_family({"record": {"kind": "constant"}}) == "record:constant"
    assert harness.group_families("heldout_notes_literature") == (
        "notes",
        "literature",
        "research",
    )
    assert harness.group_families("exact_control") is None


# ----------------------------------------------------------------------------- plans


def test_plan_arguments_follow_engine_deduplication():
    plan = {"texts": ["primary", "other", "other"], "weights": [3.0, 2.0, 5.0]}
    arguments = harness._plan_arguments("primary", plan)
    assert arguments == {"queries": ["other"], "query_weights": [1.0, 2.0]}


def test_plans_directory_is_applied_and_reported(factory, fixture_path, tmp_path):
    plans = tmp_path / "plans"
    plans.mkdir()
    (plans / "q_score.json").write_text(
        json.dumps({"queries": [{"text": "conditional transport", "weight": 2.0}]}),
        encoding="utf-8",
    )
    (plans / "q_miss.json").write_text("{not json", encoding="utf-8")
    calls = []

    def spying_factory():
        engine = factory()
        original = engine.search

        def search(query, **kwargs):
            calls.append((query, kwargs))
            return original(query, **kwargs)

        engine.search = search
        return engine

    report = harness.evaluate(
        spying_factory,
        fixture_path,
        link_samples=0,
        trace_memory=False,
        plans_dir=plans,
        configurations=("plans",),
    )
    assert report["inputs"]["plans"]["query_ids_with_plans"] == ["q_score"]
    assert report["inputs"]["plans"]["problems"][0]["path"].endswith("q_miss.json")
    planned = [kwargs for query, kwargs in calls if query == "uniform score estimate"]
    assert {"queries": ["conditional transport"], "query_weights": [1.0, 2.0]}.items() <= (
        planned[-1].items()
    )
    rows = {row["query_id"]: row for row in report["configurations"]["plans"]["rows"]}
    assert rows["q_score"]["plan"] is True and rows["q_score"]["sub_queries"] == 1
    assert rows["q_path"]["plan"] is False


# ----------------------------------------------------------------------------- lexicon


def test_lexicon_configurations_run_when_module_and_file_exist(
    factory, fixture_path, tmp_path, monkeypatch
):
    lexicon = tmp_path / harness.LEXICON_PATH
    lexicon.parent.mkdir(parents=True)
    lexicon.write_text("terms: []\n", encoding="utf-8")
    fake = types.ModuleType("workhouse.discovery_lexicon")
    fake.DEFAULT_LEXICON_WEIGHT = 0.7
    fake.load = lambda path=None, root=None, **_: {"entries": [1, 2], "fingerprint": "lex"}
    fake.expand = lambda query, lexicon: {"sub_queries": ["spectral islands", ""]}
    monkeypatch.setitem(sys.modules, "workhouse.discovery_lexicon", fake)
    expander, status, facts = harness.lexicon_expander(tmp_path)
    assert status == "available"
    assert expander("x") == [{"text": "spectral islands", "weight": 0.7}]
    assert facts == {
        "fingerprint": "lex",
        "entries": 2,
        "sub_query_weight": 0.7,
        "api": "expand(query, lexicon)",
    }
    report = harness.evaluate(
        factory,
        fixture_path,
        link_samples=0,
        trace_memory=False,
        configurations=("lexical+lexicon", "lexical+graph+lexicon"),
    )
    for name in ("lexical+lexicon", "lexical+graph+lexicon"):
        data = report["configurations"][name]
        assert data["status"] == "ran"
        assert data["summary"]["queries_with_sub_queries"] == len(FIXTURE["queries"])
    # The expansion retrieves C for a query whose own words never match it.
    rows = {row["query_id"]: row for row in report["configurations"]["lexical+lexicon"]["rows"]}
    assert "C" in rows["q_miss"]["top_ids"]


def test_lexicon_import_failure_is_reported_not_raised(tmp_path, monkeypatch):
    lexicon = tmp_path / harness.LEXICON_PATH
    lexicon.parent.mkdir(parents=True)
    lexicon.write_text("terms: []\n", encoding="utf-8")
    monkeypatch.setitem(sys.modules, "workhouse.discovery_lexicon", None)
    expander, status, facts = harness.lexicon_expander(tmp_path)
    assert expander is None and status.startswith("import failed") and facts == {}
    broken = types.ModuleType("workhouse.discovery_lexicon")
    broken.expand = lambda query, lexicon: {"sub_queries": []}

    def load(path=None, root=None, **_):
        raise ValueError("lexicon invalid: missing citation")

    broken.load = load
    monkeypatch.setitem(sys.modules, "workhouse.discovery_lexicon", broken)
    expander, status, _facts = harness.lexicon_expander(tmp_path)
    assert expander is None and status.startswith("load failed: ValueError")


# ----------------------------------------------------------------------------- leakage


def test_leakage_check_flags_stems_and_ids_at_token_boundaries():
    cases = [
        {"id": "clean", "query": "transport budget", "expected_paths": ["docs/w6-budget.md"]},
        {"id": "stem", "query": "see w6-budget please", "expected_paths": ["docs/w6-budget.md"]},
        {"id": "id", "query": "what is DERIV:A about", "expected_claim_ids": ["DERIV:A"]},
        {"id": "prefix", "query": "t_23 value", "expected_claim_ids": ["t_2"]},
        {"id": "short", "query": "a value", "expected_paths": ["docs/a.md"]},
        {"id": "neg", "query": "w6-budget", "expect_empty": True},
        {"id": "exact", "query": "RESULT:X", "expected_claim_ids": ["RESULT:X"]},
        {
            "id": "exact_group",
            "group": "heldout_exact",
            "query": "what C15 says",
            "expected_claim_ids": ["C15"],
        },
    ]
    result = harness.leakage_check(cases)
    assert result["positive_queries"] == 7
    assert {row["query_id"] for row in result["rows"]} == {"stem", "id", "exact", "exact_group"}
    assert result["leaking_queries"] == 2
    assert result["exact_id_queries"] == 2
    kinds = {row["query_id"]: row["leaks"][0]["kind"] for row in result["rows"]}
    assert kinds == {
        "stem": "path_stem",
        "id": "claim_id",
        "exact": "exact_id_lookup",
        "exact_group": "exact_id_lookup",
    }


# ----------------------------------------------------------------------------- links


def test_eligible_edges_require_curated_types_and_long_statements(factory):
    engine = factory()
    edges = harness.eligible_edges(engine)
    assert [(e["src"], e["dst"], e["type"]) for e in edges] == [
        ("A", "C", "bears_on"),
        ("B", "A", "depends_on"),
        ("C", "B", "supported_by"),
    ]
    assert all(e["how"] == "curated" for e in edges)


def test_sampling_is_deterministic_and_type_stratified():
    edges = [edge("s", f"d{i}") for i in range(5)] + [edge("s", "x", "bears_on")]
    first = harness.sample_edges(edges, 2, seed=7)
    assert harness.sample_edges(edges, 2, seed=7) == first
    assert {e["type"] for e in first} == {"depends_on", "bears_on"}
    assert len(harness.sample_edges(edges, 40, seed=7)) == 6


def test_hidden_edge_is_absent_from_temporary_graph_and_restored(factory):
    engine = factory()
    original_graph = engine.graph
    original_edges = copy.deepcopy(engine.index.edges)
    assert "A" in engine.graph.neighbors("B")
    graph, hidden = harness.hidden_graph(engine, "B", "A")
    assert hidden == 3  # curated, derived and cites copies all join the pair
    assert "A" not in graph.neighbors("B")
    assert "C" in graph.neighbors("B")
    assert engine.graph is original_graph
    row = harness.recover_one(engine, edge("B", "A"))
    assert engine.graph is original_graph
    assert engine.index.edges == original_edges
    assert row["error"] is None
    assert row["edges_hidden"] == 3
    assert row["same_family"] is False
    assert row["connections_rank"] is None or row["connections_rank"] >= 1
    assert row["retrieval_rank"] is None or row["retrieval_rank"] >= 1
    assert row["connections_seconds"] >= 0 and row["retrieval_seconds"] >= 0


def test_graph_is_restored_when_connections_fail(factory, monkeypatch):
    engine = factory()
    original_graph = engine.graph

    def explode(*_args, **_kwargs):
        raise RuntimeError("boom")

    monkeypatch.setattr(engine, "connections", explode)
    row = harness.recover_one(engine, edge("B", "A"))
    assert row["error"] == "RuntimeError: boom"
    assert engine.graph is original_graph


def test_link_recovery_report_breaks_down_by_type_and_family(factory):
    engine = factory()
    report = harness.link_recovery(engine, count=40, seed=1)
    assert report["eligible_edges"] == 3 and report["samples"] == 3
    assert report["eligible_by_type"] == {"depends_on": 1, "bears_on": 1, "supported_by": 1}
    for variant in ("connections", "retrieval_only"):
        data = report["variants"][variant]
        assert set(data["by_type"]) == {"bears_on", "depends_on", "supported_by"}
        assert data["by_family"]["cross_family"]["samples"] == 3
        assert data["by_family"]["same_family"]["samples"] == 0
        assert data["by_family"]["same_family"]["recovered_at_5"] is None
        assert data["overall"]["samples"] == 3
    assert engine.graph.neighbors("B") >= {"A", "C"}


def test_recovery_summary_arithmetic():
    rows = [
        {"connections_rank": 1, "error": None},
        {"connections_rank": 7, "error": None},
        {"connections_rank": None, "error": None},
        {"connections_rank": 1, "error": "failed"},
    ]
    summary = harness._recovery_summary(rows, "connections_rank")
    assert summary["samples"] == 3
    assert summary["recovered_at_5"] == pytest.approx(1 / 3)
    assert summary["recovered_at_20"] == pytest.approx(2 / 3)
    assert summary["mrr"] == pytest.approx((1 + 1 / 7) / 3)
    assert summary["misses"] == 1


def test_related_band_is_scored_separately_and_never_inflates_primary_recall():
    case = {"id": "q", "group": "heldout_derivation", "query": "x", "expected_claim_ids": ["B"]}
    row = harness.score_row(case, [{"id": "A", "path": "docs/a.md"}], 10, None, [{"id": "B"}])
    assert row["any_relevant_hit"] is False and row["reciprocal_rank"] == 0
    assert row["related_first_relevant_rank"] == 1
    assert row["relevant_only_in_related"] is True
    summary = harness.summarize_rows([row], 10)
    assert summary["recall_at_k"] == 0
    assert summary["recall_with_related"] == 1.0
    assert summary["relevant_only_in_related"] == 1
    direct = harness.score_row(case, [{"id": "B", "path": "docs/b.md"}], 10, None, [{"id": "B"}])
    assert direct["relevant_only_in_related"] is False


def test_graph_channel_recovers_linked_record_in_related_band(factory, fixture_path):
    report = harness.evaluate(factory, fixture_path, link_samples=0, trace_memory=False)
    graph_rows = {r["query_id"]: r for r in report["configurations"]["lexical+graph"]["rows"]}
    lexical_rows = {r["query_id"]: r for r in report["configurations"]["lexical"]["rows"]}
    # The query for A never mentions B; only the registered B -> A edge reaches it.
    assert graph_rows["q_score"]["related_hits"] >= 1
    assert lexical_rows["q_score"]["related_hits"] == 0


# ----------------------------------------------------------------------------- report


def test_memory_probe_never_raises(monkeypatch):
    probe = harness.memory_probe()
    assert probe["tracemalloc_enabled"] is False
    assert probe["tracemalloc_peak_bytes"] is None
    assert "peak_working_set_bytes" in probe
    monkeypatch.setattr(sys, "platform", "unsupported-os")
    monkeypatch.setitem(sys.modules, "resource", None)
    fallback = harness.memory_probe()
    assert fallback["working_set_source"] is None
    assert "working_set_error" in fallback


def test_run_writes_report_and_markdown_then_refuses_overwrite(
    factory, fixture_path, tmp_path, capsys
):
    out = tmp_path / "reports/eval.json"
    markdown = tmp_path / "reports/eval.md"
    args = argparse.Namespace(
        queries=fixture_path,
        limit=10,
        out=out,
        markdown=markdown,
        plans=None,
        link_samples=2,
        seed=3,
        repeat=2,
        tracemalloc=True,
        configurations="lexical,lexical+graph,plans",
        require_fixture=False,
        root=tmp_path,
    )
    assert harness.run(args, factory) == 0
    report = json.loads(out.read_text(encoding="utf-8"))
    assert report["schema"] == harness.SCHEMA
    assert report["fixture"]["sha256"] and report["fixture"]["kind"] == "held-out"
    assert report["git"].keys() == {"head", "status_short", "error"}
    assert report["memory"]["tracemalloc_enabled"] is True
    assert report["memory"]["tracemalloc_peak_bytes"] > 0
    assert report["timings"]["repeat"] == 2
    assert report["link_recovery"]["samples"] == 2
    assert report["leakage"]["leaking_queries"] == 0
    assert set(report["configurations"]) == {"lexical", "lexical+graph", "plans"}
    text = markdown.read_text(encoding="utf-8")
    assert "## Configurations" in text and "| lexical | ran |" in text
    assert "## Link recovery" in text and "retrieval_only" in text
    assert "never proof" in text
    printed = json.loads(capsys.readouterr().out)
    assert printed["status"] == "ok"
    assert harness.run(args, factory) == 1
    assert "already exists" in capsys.readouterr().out


def test_render_markdown_handles_skipped_links_and_unavailable_configurations():
    report = {
        "status": "ok",
        "evidence": "Development fixture: regression evidence only.",
        "fixture": {"path": "f.json", "sha256": "abc", "queries": 1},
        "git": {"head": "deadbeef", "status_short": ["M x"], "error": None},
        "discovery": {"fingerprint": "fp", "freshness": "matched"},
        "configurations": {
            "lexical": {
                "status": "ran",
                "summary": {
                    "recall_at_k": 1.0,
                    "mrr_at_k": 1.0,
                    "negative_controls": 0,
                    "negative_controls_passed": 0,
                    "negative_controls_passed_below_median": None,
                    "mean_distinct_families_top_k": 1.0,
                    "cross_family_hits": 0,
                    "cross_family_assessed": 0,
                    "median_warm_query_seconds": 0.01,
                },
            },
            "plans": {"status": "unavailable", "reason": "no query plans supplied"},
        },
        "per_query": [{"query_id": "q", "group": "g", "ranks": {"lexical": None}}],
        "link_recovery": {"skipped": True},
        "leakage": {"leaking_queries": 0, "positive_queries": 1, "rows": []},
        "memory": {},
        "timings": {},
        "measurement": {"scores": "Retrieval relevance only; never proof."},
    }
    text = harness.render_markdown(report)
    assert "| q | g | miss |" in text
    assert "unavailable: no query plans supplied" in text
    assert "Skipped." in text


def test_absent_fixture_is_skipped_with_a_message(factory, tmp_path, capsys):
    args = argparse.Namespace(
        queries=tmp_path / "missing.json",
        limit=10,
        out=None,
        markdown=None,
        plans=None,
        link_samples=0,
        seed=0,
        repeat=1,
        tracemalloc=False,
        configurations="lexical",
        require_fixture=False,
        root=tmp_path,
    )
    assert harness.run(args, factory) == 0
    assert json.loads(capsys.readouterr().out)["status"] == "skipped"
    args.require_fixture = True
    assert harness.run(args, factory) == 2
    assert factory.built == []


def test_add_parser_registers_evaluate_subcommand():
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(dest="discovery_command")
    harness.add_parser(subparsers)
    args = parser.parse_args(["evaluate", "--link-samples", "5", "--tracemalloc"])
    assert args.discovery_command == "evaluate"
    assert args.link_samples == 5 and args.tracemalloc is True
    assert parser.parse_args(["evaluate"]).tracemalloc is False
    assert args.queries is None and args.out is None
