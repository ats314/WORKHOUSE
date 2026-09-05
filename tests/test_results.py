"""Analytic results retain proof hypotheses and the scope of partial checks."""

from copy import deepcopy
from hashlib import sha256

import pytest
import yaml

from workhouse import atlas, derive, navigator
from workhouse import claims as C
from workhouse import graph as G
from workhouse import ledger as L
from workhouse import results as R
from workhouse.constants import STATUSES


@pytest.fixture
def register(tmp_path):
    (tmp_path / "ledger").mkdir()
    (tmp_path / "paper").mkdir()
    proof = tmp_path / "paper" / "proof.md"
    proof.write_bytes(b"# Theorem\nUnder H, conclusion follows.\n")
    (tmp_path / "paper" / "SHA256SUMS").write_text(
        f"{sha256(proof.read_bytes()).hexdigest()}  proof.md\n", encoding="utf-8"
    )
    aliases = [{"alias": "PROOF", "path": "paper/proof.md", "standing": "repo"}]
    (tmp_path / "ledger" / "documents.yaml").write_text(
        yaml.safe_dump({"schema": "documents/v1", "aliases": aliases}), encoding="utf-8"
    )
    row = {
        "id": "RESULT:example",
        "statement": "Under H, the analytic conclusion holds.",
        "status": "proven",
        "evidence": "analytic",
        "hypotheses": ["H holds."],
        "scope": "The analytic conclusion under H only.",
        "source": "CITE:PROOF",
        "source_section": "Theorem",
        "depends_on": ["RESULT:input"],
        "bears_on": ["G18"],
        "supported_by": [
            {"target": "CHK:suite:control", "scope": "Two-link algebra only."},
            {"target": "LEAN:scalar_bound", "scope": "The scalar inequality only."},
        ],
    }
    return tmp_path, row


def test_result_schema_and_pinned_source(register):
    root, row = register
    source = root / "ledger" / "results.yaml"
    source.write_text(yaml.safe_dump({"schema": "results/v1", "results": [row]}), encoding="utf-8")
    assert R.load(source, root=root) == [row]
    source.write_text(yaml.safe_dump({"schema": "results/v2", "results": [row]}), encoding="utf-8")
    with pytest.raises(ValueError, match="schema results/v1"):
        R.load(source, root=root)


@pytest.mark.parametrize("field", ["scope", "statement", "source_section", "hypotheses"])
def test_result_requires_exact_statement_hypotheses_and_scope(register, field):
    root, row = register
    del row[field]
    assert any(field in problem for problem in R.validate([row], root))


def test_finite_support_without_boundary_is_rejected(register):
    root, row = register
    del row["supported_by"][0]["scope"]
    assert any("supported_by scope" in problem for problem in R.validate([row], root))


@pytest.mark.parametrize("field", ["status", "evidence"])
def test_result_uses_existing_closed_vocabularies(register, field):
    root, row = register
    row[field] = "certified-by-metadata"
    assert any(f"unknown {field}" in problem for problem in R.validate([row], root))


def test_duplicate_result_ids_are_rejected(register):
    root, row = register
    assert any("duplicate id" in problem for problem in R.validate([row, deepcopy(row)], root))


@pytest.mark.parametrize("source", ["CITE:missing", "PROOF", "RUN:proof"])
def test_proof_source_must_resolve_to_a_document_alias(register, source):
    root, row = register
    row["source"] = source
    assert any("source" in problem for problem in R.validate([row], root))


def test_pin_is_checked_against_actual_proof_bytes(register):
    root, row = register
    (root / "paper" / "proof.md").write_bytes(b"A stronger unreviewed statement.\n")
    assert any("matching paper/SHA256SUMS pin" in p for p in R.validate([row], root))


def test_unpinned_or_nonpaper_source_cannot_support_result(register):
    root, row = register
    (root / "paper" / "SHA256SUMS").write_text("", encoding="utf-8")
    assert any("matching paper/SHA256SUMS pin" in p for p in R.validate([row], root))
    aliases = [{"alias": "PROOF", "path": "ledger/results.yaml"}]
    (root / "ledger" / "results.yaml").write_text("mutable prose", encoding="utf-8")
    (root / "ledger" / "documents.yaml").write_text(
        yaml.safe_dump({"aliases": aliases}), encoding="utf-8"
    )
    assert any("existing paper file" in p for p in R.validate([row], root))


@pytest.mark.parametrize("field", ["depends_on", "bears_on"])
def test_result_references_are_full_catalogue_ids(register, field):
    root, row = register
    row[field] = ["some plausible theorem"]
    assert any("full catalogue ids" in p for p in R.validate([row], root))


@pytest.mark.parametrize("status", sorted(STATUSES))
def test_partial_checks_do_not_change_status_or_promote_full_result(register, monkeypatch, status):
    _, row = register
    row["status"] = status
    monkeypatch.setattr(R, "load", lambda: [row])
    monkeypatch.setattr(
        C, "load_document_aliases", lambda: [{"alias": "PROOF", "path": "paper/proof.md"}]
    )
    claim = C.result_claims()[0]
    assert claim.kind == "result" and claim.tier == 3
    assert claim.status == status and claim.evidence == "analytic"
    assert row["scope"] in claim.detail
    assert row["hypotheses"][0] in claim.detail
    assert all(s["scope"] in claim.detail for s in row["supported_by"])
    assert claim.reproduce == ""  # finite or scalar checks cannot reproduce the full theorem


def test_result_dependencies_must_be_acyclic_but_relevance_may_cycle():
    def edge(src, dst, kind):
        return G.Edge(src, dst, kind, "curated", "ledger/results.yaml")

    a, b = "RESULT:a", "RESULT:b"
    assert G.validate(G.Graph([edge(a, b, "bears_on"), edge(b, a, "bears_on")], [])) == []
    cycle = G.Graph([edge(a, b, "depends_on"), edge(b, a, "depends_on")], [])
    assert any("result depends_on cycle" in p for p in G.validate(cycle))
    assert any(
        "result depends_on cycle" in p for p in G.validate(G.Graph([edge(a, a, "depends_on")], []))
    )


def test_done_routes_can_name_the_proof_or_analytic_result():
    ledgers = L.load()
    route = next(g for g in ledgers.gaps if g["id"] == "G18")["plan"][0]
    route["state"] = "done"
    route["closed_by"] = ["RESULT:example", "CITE:PROOF"]
    assert not any("closed_by" in p for p in L.validate(ledgers))
    assert G._closer_id("RESULT:example", lambda _: "unreachable") == "RESULT:example"
    assert G._closer_id("CITE:PROOF", lambda _: "unreachable") == "CITE:PROOF"


def test_route_dependencies_use_full_ids_and_preserve_proof_status():
    ledgers = L.load()
    route = next(g for g in ledgers.gaps if g["id"] == "G18")["plan"][0]
    route["depends_on"] = ["RESULT:example", "CITE:PROOF", "ROUTE:G18:previous"]
    assert not any("depends_on" in p for p in L.validate(ledgers))
    route["depends_on"] = ["a possible future result"]
    assert any("depends_on must be a list of full catalogue ids" in p for p in L.validate(ledgers))


def test_result_scope_survives_terminal_markdown_json_and_atlas_exports():
    detail = "Hypotheses: " + "Explicit local hypothesis. " * 60 + "\nScope: finite controls only."
    claim = C.Claim(
        id="RESULT:example",
        kind="result",
        statement="Scoped analytic conclusion.",
        tier=3,
        status="proven",
        evidence="analytic",
        detail=detail,
    )
    source = C.Claim(id="CITE:PROOF", kind="citation", statement="Pinned proof.")
    graph = G.Graph([G.Edge(claim.id, source.id, "cites", "curated", "ledger/results.yaml")], [])
    catalogue = [claim, source]
    text, ok = navigator.explain(claim.id, catalogue, [], graph)
    assert ok and "Scope: finite controls only." in text
    data, ok = navigator.neighborhood(claim.id, catalogue, [], graph)
    assert ok and data["record"]["detail"] == detail
    text, ok = derive.render([claim.id], catalogue, [], graph)
    assert ok and detail in text
    data = atlas.collect_data(catalogue, [], graph)
    assert next(n for n in data["nodes"] if n["id"] == claim.id)["detail"] == detail


@pytest.fixture(scope="module")
def live_graph():
    catalogue = C.collect()
    return catalogue, G.build(catalogue, C.load_symbols())


def test_curated_result_edges_are_exact_and_all_endpoints_resolve(live_graph):
    catalogue, graph = live_graph
    rows = R.load()
    assert rows, "The analytic results must be registered, not confined to G18 prose."
    assert {row["id"] for row in rows} >= {
        f"RESULT:WILSON_{suffix}"
        for suffix in (
            "KINETIC_WINDOW",
            "SECOND_ORDER_CHART",
            "FIXED_ORDER_CHART",
            "VACUUM_COMPRESSION",
            "ENDPOINT_EQUATION",
            "TRANSFER_RESOLVENT",
            "ROOTED_CONTRACTION",
            "COEFFICIENT_LOCALITY",
            "CREATOR_LIMIT",
            "SAME_WEIGHT_OBSTRUCTION",
        )
    }
    by_id = {c.id: c for c in catalogue}
    expected = set()
    for row in rows:
        result = by_id[row["id"]]
        assert result.kind == "result" and result.tier == 3
        assert (result.status, result.evidence) == (row["status"], row["evidence"])
        expected.add((row["id"], row["source"], "cites"))
        for kind in ("depends_on", "bears_on"):
            expected.update((row["id"], target, kind) for target in row[kind])
        expected.update((row["id"], s["target"], "supported_by") for s in row["supported_by"])
    actual = {(e.src, e.dst, e.type) for e in graph.edges if e.source == "ledger/results.yaml"}
    assert actual == expected
    assert (
        "RESULT:WILSON_CREATOR_LIMIT",
        "RESULT:WILSON_ROOTED_CONTRACTION",
        "depends_on",
    ) in actual
    assert (
        "RESULT:WILSON_CREATOR_LIMIT",
        "RESULT:WILSON_COEFFICIENT_LOCALITY",
        "depends_on",
    ) in actual
    assert (
        "RESULT:WILSON_ROOTED_CONTRACTION",
        "RESULT:WILSON_ENDPOINT_EQUATION",
        "depends_on",
    ) in actual
    assert not any(e.type == "promotes" and e.dst.startswith("RESULT:") for e in graph.edges)
    assert all(e.how == "curated" for e in graph.edges if e.source == "ledger/results.yaml")
    assert G.validate(graph) == []


def test_unknown_result_reference_is_dangling_not_an_invented_node(live_graph, monkeypatch):
    catalogue, _ = live_graph
    rows = deepcopy(R.load())
    rows[0]["depends_on"].append("RESULT:does_not_exist")
    monkeypatch.setattr(R, "load", lambda: rows)
    graph = G.build(catalogue, C.load_symbols())
    assert any(ref == "RESULT:does_not_exist" for ref, _, _ in graph.dangling)
    assert any("unresolved id 'RESULT:does_not_exist'" in p for p in G.validate(graph))
