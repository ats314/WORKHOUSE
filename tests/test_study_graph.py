"""Located reading notes join the graph without promoting external prose."""

from copy import deepcopy

import pytest
import yaml

from workhouse import claims as C
from workhouse import graph as G
from workhouse import literature as L
from workhouse import study_graph as S


@pytest.fixture
def study():
    return S.Study(
        "A located reading",
        "literature/example/theory_graph.yaml",
        [
            {
                "id": "STUDY:TEST:continuum",
                "statement": "A continuum construction must satisfy the stated axioms.",
                "status": "open",
                "detail": "This is a problem requirement, not a proof of its solution.",
                "sources": [{"paper": "KS_1975", "locator": "section 1"}],
                "links": [
                    {
                        "type": "bears_on",
                        "target": "G19",
                        "detail": "The continuum gap records this construction obligation.",
                    }
                ],
            }
        ],
    )


def test_an_absent_study_collection_is_empty(tmp_path, monkeypatch):
    monkeypatch.setattr(S, "ROOT", tmp_path)
    assert S.load() == []


def test_study_files_require_the_schema_and_preserve_authored_words(tmp_path, study):
    path = tmp_path / "theory_graph.yaml"
    data = {"schema": S.SCHEMA, "title": study.title, "nodes": study.nodes}
    path.write_text(yaml.safe_dump(data), encoding="utf-8")
    loaded = S.load([path])
    assert loaded[0].nodes == study.nodes
    assert S.validate(loaded, paper_ids={"KS_1975"}, known_ids={"G19"}) == []
    data["schema"] = "unknown/v1"
    path.write_text(yaml.safe_dump(data), encoding="utf-8")
    with pytest.raises(ValueError, match="expected schema"):
        S.load([path])


def test_a_source_statement_stays_t3_even_if_its_claim_status_is_proven(study):
    study.nodes[0]["status"] = "proven"
    records = C.collect_study_claims([study], paper_ids={"KS_1975"})
    record = records[0]
    assert (record.kind, record.tier, record.evidence) == ("note", 3, "prose-only")
    assert record.status == "proven"
    assert record.statement == study.nodes[0]["statement"]
    assert "KS_1975 (section 1)" in record.cites
    assert "G19" in record.related
    assert study.nodes[0]["links"][0]["detail"] in record.detail
    assert record.where == f"{study.source}#STUDY:TEST:continuum"


@pytest.mark.parametrize("field,value", [("tier", 0), ("kind", "check"), ("evidence", "analytic")])
def test_study_metadata_cannot_promote_a_reading(study, field, value):
    study.nodes[0][field] = value
    assert any("must remain" in p for p in S.validate([study], paper_ids={"KS_1975"}))
    with pytest.raises(ValueError, match="must remain"):
        C.collect_study_claims([study], paper_ids={"KS_1975"})


def test_missing_source_locator_and_unindexed_paper_are_rejected(study):
    study.nodes[0]["sources"] = [{"paper": "NOT_INDEXED"}]
    problems = S.validate([study], paper_ids={"KS_1975"})
    assert any("not a full indexed paper" in p for p in problems)
    assert any("no page or section locator" in p for p in problems)


def test_links_need_an_explanation_a_supported_type_and_a_resolving_target(study):
    link = study.nodes[0]["links"][0]
    link["type"], link["target"], link["detail"] = "proves", "G999", ""
    problems = S.validate([study], paper_ids={"KS_1975"}, known_ids={"G19"})
    assert any("unsupported study link type" in p for p in problems)
    assert any("unresolved" in p for p in problems)
    assert any("no explanation" in p for p in problems)


def test_duplicate_nodes_and_links_do_not_silently_collapse(study):
    study.nodes[0]["links"].append(deepcopy(study.nodes[0]["links"][0]))
    study.nodes.append(deepcopy(study.nodes[0]))
    problems = S.validate([study], paper_ids={"KS_1975"})
    assert any("duplicate study node id" in p for p in problems)
    assert any("duplicate study link" in p for p in problems)


def test_study_relationships_enter_the_native_graph_with_their_locators(study, monkeypatch):
    monkeypatch.setattr(S, "load", lambda: [study])
    # The stored catalogue supplies the existing endpoints; the fixture supplies
    # this study's nodes. Structural graph tests separately rebuild all checks.
    catalogue = C.load_catalogue() + C.collect_study_claims([study])
    graph = G.build(catalogue)
    assert not [d for d in graph.dangling if "STUDY:TEST:" in d[0]]
    edges = [e for e in graph.edges if "STUDY:TEST:continuum" in (e.src, e.dst)]
    triples = {(e.src, e.dst, e.type) for e in edges}
    assert triples == {
        ("LIT:KS_1975", "STUDY:TEST:continuum", "contains"),
        ("STUDY:TEST:continuum", "LIT:KS_1975", "supported_by"),
        ("STUDY:TEST:continuum", "G19", "bears_on"),
    }
    assert all(study.source in e.source for e in edges)
    assert any("section 1" in e.source for e in edges)
    assert all(e.how == "curated" for e in edges)


def test_all_study_files_have_resolvable_located_sources():
    studies = S.load()
    literature = L.load()
    catalogue = C.collect_study_claims(studies, paper_ids=literature.ids)
    known = {c.id for c in C.load_catalogue()} | {c.id for c in catalogue}
    known |= {f"LIT:{pid}" for pid in literature.node_ids}
    assert S.validate(studies, known_ids=known) == []
    nodes = {node["id"] for study in studies for node in study.nodes}
    records = {c.id: c for c in catalogue if c.id in nodes}
    assert nodes == set(records)
    assert all((c.kind, c.tier, c.evidence) == ("note", 3, "prose-only") for c in records.values())
