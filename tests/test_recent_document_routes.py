"""Keep the September derivation and validation sources reachable in the graph."""

import json
from pathlib import Path

from workhouse import claims, graph


def test_september_document_coverage_has_native_nodes():
    root = Path(claims.ROOT)
    coverage = json.loads(
        (root / "runs/recent_research_integration_2026-09-09/docs_coverage.json").read_text()
    )["records"]
    catalogue = {item.id: item for item in claims.collect()}
    assert coverage
    for row in coverage:
        assert catalogue[row["node"]].where == row["path"]
        assert (root / row["path"]).is_file()


def test_review_and_formal_source_links_are_curated_without_tier_promotion():
    catalogue = claims.collect()
    by_id = {item.id: item for item in catalogue}
    built = graph.build(catalogue)
    triples = {(edge.src, edge.dst, edge.type) for edge in built.edges}
    formal = "CITE:SEPT_DOC_YANGMILLS_FORMAL_BRIDGES"
    proposal = "CITE:SEPT_DOC_YANGMILLS_RESOLVENT_LOCALIZATION_AND_DIRICHLET_GAP"
    assert (formal, "G23", "bears_on") in triples
    assert (proposal, "CITE:YM_GPU_AUDIT", "superseded_by") in triples
    assert by_id[formal].tier == by_id[proposal].tier == 3
    assert by_id[proposal].status == "quarantined"
    assert not built.dangling
