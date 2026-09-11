"""End-to-end retrieval semantics on a small, adversarial scientific graph."""

import copy
import json

import pytest

from workhouse import discovery as D


def record(node, statement, where, **kwargs):
    return {"id": node, "kind": "result", "statement": statement, "where": where, **kwargs}


class MemoryIndex:
    def __init__(self, root, cache_dir=None):
        self.records = [
            record(
                "A", "uniform score estimate", "a.md", status="proven", evidence="analytic", tier=3
            ),
            record("B", "canonical operator extension", "b.md", status="conditional", tier=3),
            record("C", "a separate construction", "c.md", tier=0),
        ]
        self.edges = [
            {
                "src": "B",
                "dst": "A",
                "type": "depends_on",
                "how": "curated",
                "source": "ledger/test.yaml",
            },
            {
                "src": "C",
                "dst": "B",
                "type": "supported_by",
                "how": "curated",
                "source": "ledger/test.yaml",
            },
        ]
        self.symbols = []

    def build(self):
        return self.metadata()

    def metadata(self):
        return {"fingerprint": "test-snapshot"}

    def search(self, query, limit=100):
        if "score" not in query:
            return []
        return [
            {
                "id": "chunk:A",
                "claim_ids": ["A"],
                "kind": "record",
                "path": "a.md",
                "text": "uniform score estimate",
                "score": 1.0,
            }
        ]

    def close(self):
        pass


@pytest.fixture
def engine(monkeypatch, tmp_path):
    monkeypatch.setattr(D, "DiscoveryIndex", MemoryIndex)
    with D.DiscoveryEngine(tmp_path) as instance:
        yield instance


def test_graph_discovers_connected_statement_without_shared_query_words(engine):
    original_records = copy.deepcopy(engine.index.records)
    original_edges = copy.deepcopy(engine.index.edges)
    output = engine.search("score", limit=3)
    hit = next(hit for hit in output["related"] if hit["id"] == "B")
    assert "score" not in hit["text"]
    assert "graph" in hit["score_channels"]
    assert hit["graph_witness"]["paths"][0][0]["edge"] in original_edges
    assert hit["record"]["status"] == "conditional"
    assert engine.index.records == original_records
    assert engine.index.edges == original_edges
    assert output["execution"]["python_checks"] == 0


def test_lexical_ablation_and_no_hits_do_not_invent_candidates(engine):
    assert [hit["id"] for hit in engine.search("score", graph_weight=0)["hits"]] == ["A"]
    assert engine.search("zzzzunknown")["hits"] == []


def test_seed_search_preserves_all_three_evidence_axes(engine):
    output = engine.search("", seeds=["A"])
    hit = next(hit for hit in output["hits"] if hit["id"] == "A")
    assert (hit["record"]["status"], hit["record"]["evidence"], hit["record"]["tier"]) == (
        "proven",
        "analytic",
        3,
    )
    assert hit["discovery_only"] is True


def test_connections_exclude_existing_direct_relationships(engine):
    output = engine.connections("A", query="score")
    ids = {candidate["id"] for candidate in output["candidates"]}
    assert "A" not in ids and "B" not in ids
    assert "C" in ids
    assert all(candidate["candidate_only"] for candidate in output["candidates"])


@pytest.mark.parametrize(
    "kwargs",
    [{"limit": 0}, {"limit": 101}, {"pool": 0}, {"graph_weight": -1}, {"seeds": ["missing"]}],
)
def test_input_bounds(engine, kwargs):
    with pytest.raises(ValueError):
        engine.search("score", **kwargs)


def test_rrf_deduplicates_channels_and_explains_each_contribution():
    ranking = D.reciprocal_rank_fusion({"lexical": ["a", "a", "b"], "graph": ["b"]})
    assert list(ranking) == ["b", "a"]
    assert ranking["a"]["score"] == pytest.approx(1 / 61)
    assert ranking["b"]["channels"]["lexical"]["rank"] == 2


def test_context_budget_counts_json_escaping_and_reports_omissions(engine):
    result = engine.search("score")
    result["hits"][0]["record"] = dict(result["hits"][0]["record"], statement='λ"\\' * 5000)
    pack = D.context_pack(result, 2600)
    assert len(json.dumps(pack, ensure_ascii=True, sort_keys=True)) <= 2600
    # The top row is kept by shrinking its excerpt; escaping counts toward the budget.
    assert pack["hits"][0]["id"] == "A"
    assert pack["hits"][0]["excerpt_truncated"]
    assert pack["excerpt_chars"] < 700
    assert pack["omitted"] == len(pack["omitted_ids"])
    assert pack["provenance"]["fingerprint"] == "test-snapshot"


def test_context_pack_drops_lowest_ranks_first_and_names_them():
    from workhouse.discovery_present import context_pack

    hits = [
        {
            "id": f"PASSAGE:{i}",
            "kind": "passage",
            "path": f"theory/doc{i}.md",
            "start_line": 1,
            "end_line": 3,
            "source_sha256": "f" * 64,
            "claim_ids": [],
            "text": f"score estimate number {i} " * 40,
            "score": 1.0 / (i + 1),
            "score_channels": {"lexical": {"rank": i + 1, "contribution": 0.0}},
        }
        for i in range(12)
    ]
    result = {
        "query": "score estimate",
        "hits": hits,
        "related": [],
        "provenance": {"fingerprint": "abc", "freshness": "matched"},
        "meaning": "m",
        "retrieval": {"channels": ["lexical"]},
        "execution": {},
    }
    pack = context_pack(result, 3000)
    assert len(json.dumps(pack, ensure_ascii=True, sort_keys=True)) <= 3000
    kept = [row["rank"] for row in pack["hits"]]
    assert kept == list(range(1, len(kept) + 1))
    assert pack["omitted"] == 12 - len(kept) > 0
    assert [row["rank"] for row in pack["omitted_ids"]] == list(range(12, len(kept), -1))
    assert pack["hits"][0]["source"]["path"] == "theory/doc0.md"
    assert pack["hits"][0]["matched_terms"] == ["estimate", "score"]
    big = context_pack(result, 200000)
    assert big["omitted"] == 0 and big["excerpt_chars"] == 700


def test_source_diversity_keeps_other_sources_visible():
    rows = [{"id": str(i), "path": "same.md"} for i in range(10)]
    rows.append({"id": "other", "path": "other.md"})
    assert "other" in [row["id"] for row in D._select_diverse(rows, 3)]


def test_unlinked_lexical_passage_is_not_demoted_for_lacking_graph_channel(engine, monkeypatch):
    old_search = engine.index.search

    def passages(query, limit=100):
        return [
            {
                "id": "unlinked",
                "claim_ids": [],
                "kind": "passage",
                "path": "history.md",
                "start_line": 1,
                "text": "rare score mechanism",
                "score": 2.0,
            }
        ] + old_search(query, limit)

    monkeypatch.setattr(engine.index, "search", passages)
    output = engine.search("score", limit=1)
    assert output["hits"][0]["id"] == "unlinked"
    assert output["related"]


def test_source_diversity_normalizes_line_locators():
    rows = [
        {"id": "a", "where": "x.py:12"},
        {"id": "b", "where": "x.py:24"},
        {"id": "c", "where": "x.py:31"},
        {"id": "d", "where": "y.py:12"},
    ]
    assert [row["id"] for row in D._select_diverse(rows, 3)] == ["a", "b", "d"]


@pytest.mark.parametrize("source", ["corpus/#-Final-unified-theory.txt", "corpus/STATUS (2).md"])
def test_literal_filename_is_preserved_in_source_grouping(source):
    assert D._source_path(source) == source


def test_context_retains_detected_stale_inputs(engine):
    output = engine.search("score")
    output["provenance"].update(freshness="stale", current_fingerprint="new-inputs")
    pack = D.context_pack(output, 4000)
    assert pack["provenance"]["freshness"] == "stale"
    assert pack["provenance"]["current_fingerprint"] == "new-inputs"


def test_cli_context_budget_and_no_overwrite(engine, monkeypatch, capsys, tmp_path):
    from argparse import Namespace

    from workhouse.cli import _discover

    monkeypatch.setattr(D, "DiscoveryEngine", lambda: engine)
    output = tmp_path / "context.json"
    args = Namespace(
        discovery_command="search",
        query="score",
        limit=3,
        seed=None,
        graph_weight=0.8,
        semantic=None,
        context_chars=2000,
        out=str(output),
        json=False,
    )
    assert _discover(args) == 0
    rendered = capsys.readouterr().out.strip()
    assert len(rendered) <= 2000
    assert json.loads(rendered)["schema"] == "workhouse-discovery/context/v2"
    original = output.read_bytes()
    args.json = True
    assert _discover(args) == 1
    assert "error" in json.loads(capsys.readouterr().out)
    assert output.read_bytes() == original


def test_cli_unknown_path_target_is_structured_failure(engine, monkeypatch, capsys):
    from argparse import Namespace

    from workhouse.cli import _discover

    monkeypatch.setattr(D, "DiscoveryEngine", lambda: engine)
    args = Namespace(
        discovery_command="path",
        source="A",
        target="missing",
        depth=3,
        limit=3,
        dependency_only=True,
        out=None,
        json=True,
    )
    assert _discover(args) == 1
    assert "unknown path IDs" in json.loads(capsys.readouterr().out)["error"]
