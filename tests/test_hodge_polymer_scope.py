"""Abstract and syntactic support must not promote physical model checks."""

import json
from hashlib import sha256

import yaml

from workhouse import derivation_statements as D


def test_received_hodge_polymer_sources_remain_recoverable():
    run = D.ROOT / "runs/hodge_polymer_scope_2026-09-10"
    manifest = json.loads((run / "source_manifest.json").read_text(encoding="utf-8"))
    assert manifest["files"]
    for row in manifest["files"]:
        source = (run / row["snapshot_path"]).resolve()
        assert source.is_relative_to(run.resolve())
        assert sha256(source.read_bytes()).hexdigest() == row["sha256"]


def test_abstract_hodge_and_scalar_polymer_proofs_do_not_promote_physical_checks():
    groups = [
        s
        for doc in D.load()["documents"]
        for s in doc["statements"]
        if s["id"].startswith("DERIV:HODGE_POLYMER_SUPPORTED:")
    ]
    assert groups and all(row["lean"] for row in groups)
    names = {name for group in groups for name in group["lean"]}
    rows = yaml.safe_load((D.ROOT / "ledger/theorems.yaml").read_text(encoding="utf-8"))["theorems"]
    # Changing this boundary requires the actual incidence or polymer construction,
    # not a renamed Boolean predicate, prescribed polynomial, or geometric sum.
    for row in rows:
        if row["name"] in names:
            assert row["formalizes"] == [] and row["promotes"] == []
            assert row["proof_sources"]
    assert "rank_one_rur_cleared_defect_zero" in names
    assert "rur_two_r_no_u_false" in names
    assert "geometric_majorant_le_iff" in names


def test_physical_hodge_result_links_are_explicitly_scoped_support():
    results = yaml.safe_load((D.ROOT / "ledger/results.yaml").read_text(encoding="utf-8"))
    hodge = next(
        row for row in results["results"] if row["id"] == "RESULT:HODGE_FESHBACH_SPLITTING"
    )
    support = {row["target"]: row["scope"] for row in hodge["supported_by"]}
    assert "supplied abstract Hodge relations" in support["LEAN:hodge_decomposition"]
    assert "real inner-product space" in support["LEAN:r_excitation_up_harmonic"]
    assert hodge["status"] == "proven"
