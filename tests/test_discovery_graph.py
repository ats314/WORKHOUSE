"""Adversarial retrieval fixtures, independent of the scientific collector."""

from __future__ import annotations

from copy import deepcopy

import pytest

from workhouse.discovery_graph import GraphDiscovery, relationship_class


def nodes(*ids: str) -> list[dict]:
    return [{"id": id_, "kind": "result"} for id_ in ids]


def edge(src: str, dst: str, type_: str = "depends_on", **extra) -> dict:
    return {
        "src": src,
        "dst": dst,
        "type": type_,
        "how": "curated",
        "source": "ledger/example.yaml#fixture",
        **extra,
    }


def test_pagerank_matches_solved_three_node_chain_and_reports_tail_mass():
    graph = GraphDiscovery(nodes("A", "B", "C", "disconnected"), [edge("A", "B"), edge("B", "C")])
    result = graph.rank({"A": 1}, max_iterations=300)
    alpha = 0.85
    expected_b = alpha / (1 + alpha)
    assert result["converged"]
    assert result["scores"] == pytest.approx(
        {
            "A": 1 - alpha + alpha * expected_b / 2,
            "B": expected_b,
            "C": alpha * expected_b / 2,
        },
        abs=1e-8,
    )
    assert result["total_score_mass"] == pytest.approx(1)
    assert "disconnected" not in result["scores"]
    short = graph.rank({"A": 1}, limit=1)
    assert len(short["scores"]) == 1
    assert short["returned_score_mass"] < short["total_score_mass"]
    assert short["candidate_only"]


def test_dangling_mass_returns_to_personalization_and_unknown_seeds_are_explicit():
    graph = GraphDiscovery(nodes("A", "B"), [])
    result = graph.rank({"A": 3, "B": 1, "MISSING": 20})
    assert result["scores"] == {"A": 0.75, "B": 0.25}
    assert result["unknown_seeds"] == ["MISSING"]
    assert result["converged"]
    assert result["iterations"] == 1
    assert graph.rank({"MISSING": 1})["scores"] == {}
    assert graph.rank({})["iterations"] == 0
    assert graph.rank({"A": 1e308, "B": 1e308})["scores"] == {"A": 0.5, "B": 0.5}


def test_iteration_cap_is_honest_about_nonconvergence():
    graph = GraphDiscovery(nodes("A", "B"), [edge("A", "B")])
    result = graph.rank({"A": 1}, max_iterations=1)
    assert result["iterations"] == 1
    assert not result["converged"]
    assert result["residual"] > result["tolerance"]
    assert graph.rank({"A": 1}, alpha=0)["scores"] == {"A": 1.0}


@pytest.mark.parametrize(
    "kwargs",
    [
        {"alpha": 1},
        {"alpha": -0.1},
        {"alpha": float("nan")},
        {"max_iterations": 0},
        {"max_iterations": 1.5},
        {"tolerance": 0},
        {"tolerance": float("inf")},
        {"limit": -1},
        {"limit": True},
    ],
)
def test_rank_rejects_invalid_bounds(kwargs):
    with pytest.raises(ValueError):
        GraphDiscovery(nodes("A"), []).rank({"A": 1}, **kwargs)


@pytest.mark.parametrize("weight", [-1, float("nan"), float("inf")])
def test_rank_rejects_invalid_seed_weights(weight):
    with pytest.raises(ValueError):
        GraphDiscovery(nodes("A"), []).rank({"A": weight})


def test_archive_hub_cannot_manufacture_discovery_paths():
    graph = GraphDiscovery(
        nodes("ARCHIVE:all", "A", "B"),
        [
            edge("ARCHIVE:all", "A", "contains"),
            edge("ARCHIVE:all", "B", "contains"),
        ],
    )
    assert graph.rank({"A": 1})["scores"] == {"A": 1.0}
    assert graph.paths("A", "B")["paths"] == []
    assert graph.diagnostics["archive_membership_edges_excluded"] == 2
    # Excluding membership from discovery does not erase the registered edge.
    assert graph.connections("A", ["ARCHIVE:all"])[0]["has_registered_relation"]


def test_specific_dependency_beats_large_citation_hub():
    documents = [f"D{i:03}" for i in range(100)]
    graph = GraphDiscovery(
        nodes("S", "reusable", "HUB", *documents),
        [
            edge("S", "reusable"),
            edge("S", "HUB", "cites"),
            *(edge("HUB", document, "contains") for document in documents),
        ],
    )
    scores = graph.rank({"S": 1}, limit=200)["scores"]
    assert scores["reusable"] > 10 * scores["HUB"]
    assert scores["reusable"] > sum(scores[id_] for id_ in documents)


def test_repeated_sources_do_not_multiply_retrieval_weight():
    records = nodes("A", "B", "C")
    original = [edge("A", "B"), edge("A", "C")]
    copies = [edge("A", "B", source=f"copy-{i}.yaml") for i in range(50)]
    baseline = GraphDiscovery(records, original).rank({"A": 1})
    graph = GraphDiscovery(records, [*original, *copies, original[0]])
    assert graph.rank({"A": 1}) == baseline
    assert graph.diagnostics["duplicate_edges_ignored"] == 1
    assert len(graph.connections("A", ["B"])[0]["existing_relations"]) == 51
    assert graph.paths("A", "B")["paths"] == [
        [
            {
                "edge": copies[0],
                "direction": "forward",
                "from": "A",
                "to": "B",
                "relationship_class": "dependency",
            }
        ]
    ]


def test_dangling_and_malformed_edges_reported_without_invented_nodes():
    missing = edge("A", "absent")
    malformed = {"src": "A", "dst": "B", "type": "depends_on"}
    graph = GraphDiscovery(nodes("A", "B"), [missing, malformed, edge("A", "B")])
    assert graph.diagnostics["dangling_edges"] == [missing]
    assert graph.diagnostics["malformed_edges"] == [malformed]
    assert graph.diagnostics["registered_edges"] == 1
    assert "absent" not in graph.records
    assert graph.paths("A", "absent")["unknown_nodes"] == ["absent"]


def test_duplicate_record_ids_fail_instead_of_arbitrarily_choosing_source():
    with pytest.raises(ValueError, match="duplicate catalogue id"):
        GraphDiscovery(nodes("A", "A"), [])


def test_exploratory_path_retains_original_edge_and_reverse_direction():
    original = edge("A", "B", "supported_by", scope="only the closed-extension ingredient")
    graph = GraphDiscovery(nodes("A", "B"), [original])
    step = graph.paths("B", "A")["paths"][0][0]
    assert step["edge"] == original
    assert step["direction"] == "reverse"
    assert (step["from"], step["to"]) == ("B", "A")
    assert step["relationship_class"] == "scoped_support"
    assert graph.paths("B", "A")["candidate_only"]
    step["edge"]["scope"] = "modified by caller"
    assert graph.paths("B", "A")["paths"][0][0]["edge"] == original


def test_dependencies_keep_direction_and_exclude_support_and_mentions():
    graph = GraphDiscovery(
        nodes("A", "B", "C", "D", "E"),
        [
            edge("A", "B"),
            edge("B", "C", "rests_on"),
            edge("A", "D", "supported_by"),
            edge("D", "E", "mentions", how="derived"),
        ],
    )
    forward = graph.paths("A", "C", dependency_only=True)
    assert len(forward["paths"][0]) == 2
    assert all(step["direction"] == "forward" for step in forward["paths"][0])
    assert not forward["candidate_only"]
    assert graph.paths("C", "A", dependency_only=True)["paths"] == []
    assert graph.paths("A", "D", dependency_only=True)["paths"] == []
    assert graph.paths("A", "E", dependency_only=True)["paths"] == []
    assert len(graph.paths("C", "A")["paths"][0]) == 2


def test_paths_are_shortest_first_deterministic_and_cycle_safe():
    records = nodes("S", "A", "B", "C", "T")
    edges = [
        edge("S", "B"),
        edge("B", "T"),
        edge("S", "A"),
        edge("A", "T"),
        edge("A", "C"),
        edge("C", "S"),
        edge("C", "C"),
    ]
    graph = GraphDiscovery(records, edges)
    result = graph.paths("S", "T", limit=10)
    assert result == GraphDiscovery(records[::-1], edges[::-1]).paths("S", "T", limit=10)
    assert [len(path) for path in result["paths"]] == sorted(len(path) for path in result["paths"])
    assert [step["to"] for step in result["paths"][0]] == ["A", "T"]
    for path in result["paths"]:
        ids = ["S", *(step["to"] for step in path)]
        assert len(ids) == len(set(ids))
    assert graph.rank({"S": 1}) == GraphDiscovery(records[::-1], edges[::-1]).rank({"S": 1})


def test_path_bounds_report_actual_examined_entries():
    graph = GraphDiscovery(
        nodes("S", "A", "B", "T"), [edge("S", "A"), edge("A", "B"), edge("B", "T")]
    )
    limited = graph.paths("S", "T", max_visits=1)
    assert limited["visits"] == 1
    assert limited["paths"] == []
    assert limited["truncated"]
    assert limited["truncation_reasons"] == ["max_visits"]
    shallow = graph.paths("S", "T", max_depth=1)
    assert shallow["paths"] == []
    assert shallow["truncation_reasons"] == ["max_depth"]
    assert graph.paths("S", "T", max_visits=0)["visits"] == 0
    assert graph.paths("S", "T", limit=0)["truncation_reasons"] == ["limit"]
    assert graph.paths("S", "S")["paths"] == [[]]


@pytest.mark.parametrize(
    "kwargs",
    [
        {"max_depth": -1},
        {"max_visits": -1},
        {"limit": -1},
        {"max_visits": 0.5},
    ],
)
def test_path_bounds_are_validated(kwargs):
    with pytest.raises(ValueError):
        GraphDiscovery(nodes("A"), []).paths("A", "A", **kwargs)


def test_dependency_impact_distinguishes_downstream_from_exploratory_relevance():
    graph = GraphDiscovery(
        nodes("INPUT", "MID", "OUTPUT", "RELATED", "MENTION"),
        [
            edge("MID", "INPUT"),
            edge("OUTPUT", "MID", "rests_on"),
            edge("RELATED", "INPUT", "supported_by"),
            edge("MENTION", "INPUT", "mentions", how="derived"),
            edge("INPUT", "OUTPUT"),  # cycle must not repeat the seed
        ],
    )
    result = graph.dependency_impact("INPUT")
    assert [record["id"] for record in result["nodes"]] == ["MID", "OUTPUT"]
    assert all(
        step["direction"] == "reverse" for record in result["nodes"] for step in record["path"]
    )
    assert graph.dependency_impact("OUTPUT", direction="upstream")["nodes"][0]["id"] == "MID"
    assert graph.dependency_impact("INPUT", max_depth=1)["truncated"]
    assert graph.dependency_impact("INPUT", limit=1)["truncated"]
    assert graph.dependency_impact("INPUT", max_visits=1)["visits"] == 1
    assert graph.dependency_impact("unknown")["unknown_nodes"] == ["unknown"]
    with pytest.raises(ValueError):
        graph.dependency_impact("INPUT", direction="both")


def test_specific_shared_witness_is_more_informative_than_a_hub():
    extra = [f"D{i}" for i in range(30)]
    graph = GraphDiscovery(
        nodes("S", "X", "Y", "specific", "hub", *extra),
        [
            edge("S", "specific"),
            edge("X", "specific"),
            edge("S", "hub"),
            edge("Y", "hub"),
            *(edge(node, "hub") for node in extra),
        ],
    )
    results = graph.connections("S", ["Y", "X", "UNKNOWN", "X"])
    assert [item["id"] for item in results] == ["X", "Y"]
    assert results[0]["score"] > results[1]["score"]
    assert results[0]["shared_witnesses"][0]["id"] == "specific"
    assert results[0]["path_found"]
    assert len(results[0]["path"]) == 2
    assert results[0]["candidate_only"]
    assert not results[0]["has_registered_relation"]
    assert graph.connections("S", ["X"], limit=0) == []


def test_source_families_identify_locator_overlap_without_claiming_independence():
    records = [
        {"id": "A", "where": "research/origin.tex:12"},
        {"id": "B", "where": "research/origin.tex:99"},
        {"id": "C", "where": "research/other.tex#section"},
        {"id": "D"},
    ]
    graph = GraphDiscovery(records, [])
    results = {item["id"]: item for item in graph.connections("A", ["B", "C", "D"])}
    assert results["B"]["source_family"]["comparison"] == "overlap"
    assert results["B"]["source_family"]["shared"] == ["path:research/origin.tex"]
    assert results["C"]["source_family"]["comparison"] == "no_recorded_overlap"
    assert results["D"]["source_family"]["comparison"] == "unknown"
    assert "not independent evidence" in results["C"]["source_family"]["semantics"]
    assert not results["C"]["path_found"]


def test_citation_overlap_is_reported_with_original_locators():
    records = [
        {"id": "A", "where": "a.tex"},
        {"id": "B", "where": "b.tex"},
        {"id": "CITE:source", "where": "corpus-import/origin.tex:14"},
    ]
    graph = GraphDiscovery(
        records, [edge("A", "CITE:source", "cites"), edge("B", "CITE:source", "cites")]
    )
    result = graph.connections("A", ["B"])[0]
    assert result["source_family"]["shared"] == [
        "path:corpus-import/origin.tex",
        "source:CITE:source",
    ]
    assert result["shared_witnesses"][0]["source_step"]["edge"]["type"] == "cites"


def test_queries_never_mutate_inputs_or_promote_scientific_status():
    records = [
        {"id": "A", "status": "proven", "tier": 3, "evidence": "analytic"},
        {"id": "B", "status": "conditional", "tier": 0},
    ]
    edges = [edge("A", "B", "supported_by")]
    before = deepcopy((records, edges))
    graph = GraphDiscovery(records, edges)
    graph.rank({"A": 1})
    graph.paths("A", "B")
    result = graph.connections("A", ["B"])[0]
    assert (records, edges) == before
    assert graph.records["A"]["tier"] == 3
    result["existing_relations"][0]["type"] = "formalizes"
    assert graph.connections("A", ["B"])[0]["existing_relations"][0]["type"] == "supported_by"
    assert relationship_class("formalizes") != relationship_class("supported_by")
    assert relationship_class("new_unknown_type") == "unknown"


def test_unknown_provenance_cannot_enter_dependency_traversal():
    guessed = edge("A", "B", how="inferred")
    graph = GraphDiscovery(nodes("A", "B"), [guessed])
    assert graph.diagnostics["malformed_edges"] == [guessed]
    assert graph.paths("A", "B", dependency_only=True)["paths"] == []


def test_source_families_strip_derivation_locators_but_preserve_literal_filenames():
    records = [
        {"id": "A", "where": "docs/derivations/shared.md (## First (lines 1-10))"},
        {"id": "B", "where": "docs/derivations/shared.md (## Second (lines 11-20))"},
        {"id": "C", "where": "docs/derivations/shared.md (Lemma third; lines 21-25)"},
        {"id": "D", "where": "docs/derivations/shared.md (lines 26-30)"},
        {"id": "HASH", "where": "corpus-import/transcripts/#-Final-unified-theory.txt"},
        {"id": "PARENS", "where": "corpus-import/STATUS_fourth_order_build (2).md"},
    ]
    graph = GraphDiscovery(records, [])
    results = {item["id"]: item for item in graph.connections("A", [r["id"] for r in records])}
    for node in ("B", "C", "D"):
        assert results[node]["source_family"]["shared"] == ["path:docs/derivations/shared.md"]
    assert results["HASH"]["source_family"]["target"] == [
        "path:corpus-import/transcripts/#-Final-unified-theory.txt"
    ]
    assert results["PARENS"]["source_family"]["target"] == [
        "path:corpus-import/STATUS_fourth_order_build (2).md"
    ]


def test_push_rank_matches_power_iteration_within_its_reported_residual():
    documents = [f"D{i:03}" for i in range(40)]
    graph = GraphDiscovery(
        nodes("S", "T", "U", "HUB", *documents),
        [
            edge("S", "T"),
            edge("T", "U", "supported_by"),
            edge("S", "HUB", "cites"),
            edge("U", "S", "bears_on"),
            *(edge("HUB", document, "contains") for document in documents),
        ],
    )
    exact = graph.rank({"S": 1, "T": 0.5}, limit=200, max_iterations=500, tolerance=1e-12)
    approx = graph.rank({"S": 1, "T": 0.5}, limit=200, method="push", push_epsilon=1e-9)
    assert approx["method"] == "push"
    assert approx["converged"]
    assert approx["residual_meaning"].startswith("exact L1 distance")
    distance = sum(
        abs(exact["scores"].get(node, 0.0) - approx["scores"].get(node, 0.0))
        for node in exact["scores"].keys() | approx["scores"].keys()
    )
    # The residual mass bounds the L1 error exactly; the power iteration
    # itself stopped at a 1e-12 change, so allow that slack too.
    assert distance <= approx["residual"] + 1e-9
    assert list(exact["scores"])[:5] == list(approx["scores"])[:5]
    assert approx["total_score_mass"] + approx["residual"] == pytest.approx(1.0, abs=1e-9)


def test_push_rank_restarts_dangling_mass_and_reports_push_cap():
    graph = GraphDiscovery(nodes("A", "B"), [edge("A", "B")])
    result = graph.rank({"A": 1}, method="push", push_epsilon=1e-12)
    exact = graph.rank({"A": 1}, max_iterations=400, tolerance=1e-13)
    assert result["scores"] == pytest.approx(exact["scores"], abs=1e-9)
    capped = graph.rank({"A": 1}, method="push", push_epsilon=1e-12, max_pushes=1)
    assert capped["iterations"] == 1
    assert not capped["converged"]
    assert capped["residual"] > 0
    with pytest.raises(ValueError):
        graph.rank({"A": 1}, method="jump")
    with pytest.raises(ValueError):
        graph.rank({"A": 1}, method="push", push_epsilon=0)
    with pytest.raises(ValueError):
        graph.rank({"A": 1}, method="push", max_pushes=0)


def test_neighbors_and_paths_limit_are_explicit_about_unexplored_rows():
    graph = GraphDiscovery(
        nodes("S", "W", "A", "B", "C"),
        [edge("S", "W"), edge("A", "W"), edge("B", "W"), edge("C", "W"), edge("S", "C", "cites")],
    )
    assert graph.neighbors("S") == {"W", "C"}
    assert graph.neighbors("A") == {"W"}
    assert graph.neighbors("missing") == set()
    rows = graph.connections("S", ["A", "B"], limit=2, paths_limit=1)
    assert [row["id"] for row in rows] == ["A", "B"]
    assert rows[0]["path_found"] is True
    assert rows[1]["path_found"] is None
    assert rows[1]["path_truncation_reasons"] == ["paths_limit"]
    explained = graph.explain_path("S", "B")
    assert explained["path_found"] is True
    assert [step["to"] for step in explained["path"]] == ["W", "B"]
    with pytest.raises(ValueError):
        graph.connections("S", ["A"], paths_limit=-1)


def test_paths_copy_edges_only_for_returned_paths():
    graph = GraphDiscovery(nodes("A", "B", "C"), [edge("A", "B"), edge("B", "C")])
    found = graph.paths("A", "C", max_depth=3)
    assert len(found["paths"]) == 1
    steps = found["paths"][0]
    steps[0]["edge"]["type"] = "mutated"
    assert graph.edges[0]["type"] == "depends_on"
