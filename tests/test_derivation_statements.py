"""Reject missing, changed, circular or falsely certified derivation records."""

from copy import deepcopy
from hashlib import sha256

import pytest
import yaml

from workhouse import derivation_statements as D


@pytest.fixture
def inventory(tmp_path):
    source = tmp_path / "docs/derivations/example.md"
    source.parent.mkdir(parents=True)
    source.write_text("# Exact source\n## Theorem A\nA follows from H.\n", encoding="utf-8")
    ledger = tmp_path / "ledger"
    ledger.mkdir()
    (ledger / "theorems.yaml").write_text(
        yaml.safe_dump({"theorems": [{"name": "ingredient"}]}), encoding="utf-8"
    )
    statement = dict(
        id="DERIV:EXAMPLE:A",
        statement="A under H",
        locator="Theorem A",
        anchor="A follows from H.",
        status="proven",
        evidence="analytic",
        hypotheses=["H"],
        depends_on=[],
        lean=[],
        lean_support=[dict(name="ingredient", scope="Only the finite identity.")],
        remaining="Construct the limiting operator.",
    )
    data = dict(
        schema="derivation-statements/v1",
        documents=[
            dict(
                id="CITE:EXAMPLE",
                path="docs/derivations/example.md",
                sha256=sha256(source.read_bytes()).hexdigest(),
                statements=[statement],
            )
        ],
    )
    return tmp_path, data


def test_support_never_manufactures_a_whole_statement_proof(inventory):
    root, data = inventory
    assert D.validate(data, root=root, theorem_names={"ingredient"}) == []
    (claim,) = D.claim_records(data, root=root)
    assert (claim["tier"], claim["status"], claim["evidence"]) == (3, "proven", "analytic")
    assert "Construct the limiting operator" in claim["detail"]
    edges = D.edge_records(data, root=root)
    assert any(e["dst"] == "LEAN:ingredient" and e["type"] == "supported_by" for e in edges)
    assert not any(e["type"] in {"formalizes", "promotes"} for e in edges)


def test_changed_source_and_wrong_anchor_cannot_keep_stale_provenance(inventory):
    root, data = inventory
    (root / data["documents"][0]["path"]).write_text("Different proof.", encoding="utf-8")
    errors = D.validate(data, root=root)
    assert any("SHA-256 mismatch" in e for e in errors)
    assert any("anchor is absent" in e for e in errors)
    with pytest.raises(ValueError, match="SHA-256"):
        D.claim_records(data, root=root)


def test_added_derivation_cannot_silently_escape_the_inventory(inventory):
    root, data = inventory
    (root / "docs/derivations/new.md").write_text("# New result", encoding="utf-8")
    assert any("inventory mismatch" in e for e in D.validate(data, root=root))


def test_missing_dependency_and_cycle_are_reported(inventory):
    root, data = inventory
    row = data["documents"][0]["statements"][0]
    row["depends_on"] = ["DERIV:EXAMPLE:MISSING"]
    assert any("unresolved" in e for e in D.validate(data, root=root))
    second = deepcopy(row)
    second["id"] = "DERIV:EXAMPLE:B"
    second["depends_on"] = [row["id"]]
    row["depends_on"] = [second["id"]]
    data["documents"][0]["statements"].append(second)
    assert any("circular" in e for e in D.validate(data, root=root))


def test_formal_support_must_name_a_registered_theorem_and_scope(inventory):
    root, data = inventory
    row = data["documents"][0]["statements"][0]
    row["lean_support"][0] = dict(name="unavailable", scope="")
    errors = D.validate(data, root=root, theorem_names={"ingredient"})
    assert any("exact scope" in e for e in errors)
    assert any("unregistered Lean" in e for e in errors)


def test_no_coverage_by_empty_fields_or_escaping_source_path(inventory):
    root, data = inventory
    row = data["documents"][0]["statements"][0]
    row["remaining"] = ""
    assert any("neither a full proof" in e for e in D.validate(data, root=root))
    data["documents"][0]["path"] = "../../outside.md"
    assert any("top-level derivation" in e for e in D.validate(data, root=root))


def test_live_inventory_has_complete_source_identity_and_registered_support():
    names = {
        x["name"]
        for x in yaml.safe_load((D.ROOT / "ledger/theorems.yaml").read_text(encoding="utf-8"))[
            "theorems"
        ]
    }
    assert D.validate(D.load(), theorem_names=names) == []


def test_generated_graph_retains_precise_source_and_kernel_dependencies():
    import json

    from workhouse import lean_dependencies as L

    kernel = L.load()
    actual = {
        (row["src"], row["dst"], row["type"], row["source"])
        for line in (D.ROOT / "index/graph.jsonl").read_text(encoding="utf-8").splitlines()
        if (row := json.loads(line))
    }
    for edge in D.edge_records() + L.edge_records(kernel):
        assert (edge["src"], edge["dst"], edge["type"], edge["source"]) in actual
    assert kernel["theorems"]["sc17_plaquette_interval"]["project_dependencies"] == [
        "spectral_interval_mass"
    ]
