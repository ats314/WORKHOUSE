"""The research bridge preserves mathematical scope and exact source identity."""

import json
from copy import deepcopy
from hashlib import sha256

import pytest
import yaml

from workhouse import recent_research as R


@pytest.fixture
def research(tmp_path):
    contents = b"# Located proof\nThe finite identity holds under H.\n"
    relative = R.SOURCE_BASE + "example/proof.md"
    path = tmp_path / relative
    path.parent.mkdir(parents=True)
    path.write_bytes(contents)
    source = {
        "id": "DOC:RECENT:EXAMPLE",
        "title": "Located proof",
        "path": relative,
        "original_path": "Z:/unavailable/original-proof.md",
        "sha256": sha256(contents).hexdigest(),
        "bytes": len(contents),
    }
    node = {
        "id": "RESULT:RECENT_EXAMPLE",
        "statement": "The finite identity holds under H.",
        "status": "proven",
        "evidence": "analytic",
        "scope": "A finite object satisfying H.",
        "detail": "The cited calculation proves precisely the displayed identity.",
        "verification": "An analytic proof, not a claimed full-statement Lean proof.",
        "value": "-10/96",
        "sources": [{"id": source["id"], "locator": "proof paragraph", "anchor": "under H"}],
        "links": [{"type": "bears_on", "target": "G19", "detail": "A scoped input only."}],
    }
    return R.Research("A preserved result", R.REGISTRY, [source], [node])


def test_registry_preserves_analytic_proof_status_without_manufacturing_machine_promotion(
    research, tmp_path
):
    assert R.validate(research, root=tmp_path, known_ids={"G19"}) == []
    source, result = R.claim_records(research, root=tmp_path)
    assert (result["status"], result["evidence"], result["tier"]) == ("proven", "analytic", 3)
    assert result["statement"] == research.nodes[0]["statement"]
    assert result["value"] == "-5/48"
    assert "Scope: A finite object satisfying H." in result["detail"]
    assert "Z:/unavailable" in source["detail"]
    assert source["where"].startswith(R.SOURCE_BASE)
    assert "reproduce" not in result  # No false command for an unreplayed full analytic theorem.


def test_hash_byte_count_and_exact_anchor_detect_changed_or_misattributed_source(
    research, tmp_path
):
    path = tmp_path / research.sources[0]["path"]
    path.write_text("# Different source\n", encoding="utf-8")
    problems = R.validate(research, root=tmp_path)
    assert any("SHA-256 mismatch" in p for p in problems)
    assert any("byte count mismatch" in p for p in problems)
    assert any("anchor absent" in p for p in problems)
    with pytest.raises(ValueError, match="SHA-256 mismatch"):
        R.claim_records(research, root=tmp_path)


def test_missing_copy_does_not_fall_back_to_external_original(research, tmp_path):
    original = tmp_path / "original.md"
    original.write_bytes((tmp_path / research.sources[0]["path"]).read_bytes())
    research.sources[0]["original_path"] = str(original)
    research.sources[0]["path"] = R.SOURCE_BASE + "missing.md"
    assert any("unavailable preserved source" in p for p in R.validate(research, root=tmp_path))


@pytest.mark.parametrize(
    "path", ["../outside.md", "C:/outside.md", R.SOURCE_BASE + "../outside.md"]
)
def test_source_paths_cannot_escape_the_pinned_bundle(research, tmp_path, path):
    research.sources[0]["path"] = path
    assert any(
        "inside the preserved source bundle" in p for p in R.validate(research, root=tmp_path)
    )


def test_curated_links_preserve_direction_and_require_resolving_endpoints(research, tmp_path):
    edge = R.edge_records(research)[-1]
    assert (edge["src"], edge["dst"], edge["type"]) == ("RESULT:RECENT_EXAMPLE", "G19", "bears_on")
    assert edge["how"] == "curated"
    assert "A scoped input only." in edge["source"]
    assert any(
        "unresolved native target" in p
        for p in R.validate(research, root=tmp_path, known_ids=set())
    )
    research.nodes[0]["links"][0]["target"] = "RESULT:RECENT_MISSING"
    assert any("unresolved research target" in p for p in R.validate(research, root=tmp_path))


def test_duplicate_nodes_and_edges_cannot_silently_collapse(research, tmp_path):
    research.nodes[0]["links"].append(deepcopy(research.nodes[0]["links"][0]))
    research.nodes.append(deepcopy(research.nodes[0]))
    problems = R.validate(research, root=tmp_path)
    assert any("duplicate research node" in p for p in problems)
    assert any("duplicate link" in p for p in problems)


@pytest.mark.parametrize(
    "field,value,problem",
    [
        ("tier", 0, "registry tier stays 3"),
        ("evidence", "published-proof", "existing evidence vocabulary"),
        ("status", "probably-true", "existing claim vocabulary"),
        ("value", 0.25, "exact rational string"),
        ("scope", "", "missing scope"),
        ("verification", "", "missing verification"),
    ],
)
def test_result_metadata_cannot_promote_or_erase_scope(research, tmp_path, field, value, problem):
    research.nodes[0][field] = value
    assert any(problem in p for p in R.validate(research, root=tmp_path))


def test_loader_checks_schema_and_keeps_authored_words(research, tmp_path):
    path = tmp_path / R.REGISTRY
    path.parent.mkdir(parents=True)
    data = {
        "schema": R.SCHEMA,
        "title": research.title,
        "sources": research.sources,
        "nodes": research.nodes,
    }
    path.write_text(yaml.safe_dump(data), encoding="utf-8")
    assert R.load(root=tmp_path).nodes == research.nodes
    data["schema"] = "unknown/v0"
    path.write_text(yaml.safe_dump(data), encoding="utf-8")
    with pytest.raises(ValueError, match="expected schema"):
        R.load(root=tmp_path)


def test_repository_registry_covers_scoped_results_and_preserves_the_remaining_obligation():
    research = R.load()
    native_ids = {
        json.loads(line)["id"]
        for line in (R.ROOT / "index/claims.jsonl").read_text(encoding="utf-8").splitlines()
        if line
    }
    assert R.validate(research, known_ids=native_ids) == []
    campaigns = {
        source["path"].removeprefix(R.SOURCE_BASE).split("/", 1)[0] for source in research.sources
    }
    assert len(campaigns) == 9
    nodes = {node["id"]: node for node in research.nodes}
    assert nodes["RESULT:W6_SQUARE_FINITE_G_FLOOR"]["status"] == "proven"
    assert "fixed" in nodes["RESULT:W6_SQUARE_FINITE_G_FLOOR"]["scope"].lower()
    assert nodes["RESULT:W6_ALL_STRIP_CANCELLATION"]["evidence"] == "analytic"
    assert nodes["ROUTE:RECENT_W6_UNIFORM_INTERACTING_TRANSFER"]["status"] == "open"
    assert nodes["ROUTE:RECENT_ANISOTROPY_DIRECT_SIXTH"]["status"] == "open"
    assert nodes["ROUTE:RECENT_W6_VERTICAL_GAP_SURROGATE"]["status"] == "falsified"
    assert nodes["ROUTE:RECENT_W6_UNWEIGHTED_RESIDUAL_SURROGATE"]["status"] == "falsified"
