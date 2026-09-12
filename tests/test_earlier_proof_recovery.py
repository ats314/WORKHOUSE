"""Recovery must preserve every source identity without inflating proof status."""

import hashlib
import json
from pathlib import Path

import pytest

from workhouse import claims, graph, notes
from workhouse.invariants.earlier_proof_recovery import disjoint_staples

ROOT = Path(__file__).resolve().parents[1]
RUN = ROOT / "runs/earlier_proof_recovery_2026-09-11"
ARCHIVE = "EARLIER_PROOF_DISCOVERY_2026-09-11"
SUMMARY = json.loads((RUN / "coverage_summary.json").read_text(encoding="utf-8"))


def _coverage():
    return [
        json.loads(line)
        for line in (RUN / "keyword_coverage.jsonl").read_text(encoding="utf-8").splitlines()
    ]


def test_keyword_digest_set_has_no_dropped_or_unresolvable_source():
    rows = _coverage()
    digests = [r["sha256"] for r in rows]
    assert len(rows) == len(set(digests)) == SUMMARY["keyword_candidate_count"]
    encoded = ("\n".join(sorted(digests)) + "\n").encode()
    assert hashlib.sha256(encoded).hexdigest() == SUMMARY["keyword_digest_set_sha256"]
    registry = notes.load()
    identities = {
        claims.note_id(aid, row): row["digest"]
        for aid, entries in registry.manifests.items()
        for row in entries
    }
    catalogue = {c.id: c for c in claims.load_catalogue()}
    for row in rows:
        assert row["graph_ids"], row["primary_path"]
        for node in row["graph_ids"]:
            assert identities[node] == row["sha256"]
            assert catalogue[node].kind == "note"
            assert catalogue[node].tier == 3
        if row["sha256"] not in registry.reviewed_digests():
            assert all(catalogue[node].status == "pending" for node in row["graph_ids"])


def test_retained_originals_and_review_imports_match_exactly():
    sources = json.loads((RUN / "source_manifest.json").read_text(encoding="utf-8"))
    reviews = {r["digest"]: r for r in notes.load().reviews if r["archive"] == ARCHIVE}
    assert len(sources) == len(reviews) == SUMMARY["reviewed_source_import_count"]
    for source in sources:
        contents = (ROOT / source["retained_path"]).read_bytes()
        assert len(contents) == source["bytes"]
        digest = hashlib.sha256(contents).hexdigest()
        assert digest == source["original_sha256"]
        assert reviews[digest]["verdict"] == "import"
        assert reviews[digest]["imported_to"] == source["retained_path"]
        assert reviews[digest]["bears_on"]


def test_source_edges_keep_exact_native_identities_and_do_not_promote():
    catalogue = claims.load_catalogue()
    by_id = {c.id: c for c in catalogue}
    built = graph.build(catalogue, claims.load_symbols())
    triples = {(e.src, e.dst, e.type) for e in built.edges}
    registry = notes.load()
    by_digest = {row["digest"]: row for row in registry.manifests[ARCHIVE]}
    for review in registry.reviews:
        if review["archive"] != ARCHIVE:
            continue
        source_id = claims.note_id(ARCHIVE, by_digest[review["digest"]])
        for target in review["bears_on"]:
            assert (source_id, target, "bears_on") in triples
            assert (source_id, "CONST:" + target, "bears_on") not in triples
    for node in SUMMARY["result_ids"] + SUMMARY["derivation_ids"]:
        assert by_id[node].tier == 3
    for node in SUMMARY["check_ids"]:
        assert by_id[node].tier == 1
    assert by_id["RESULT:EARLIER_B6_RETAINED_KRYLOV_CAMPAIGN"].evidence == "numerical"
    assert by_id["DERIV:EARLIER_PROOF_RECOVERY:PHYSICAL_CARRIER_REALIZATION"].status == "open"
    assert by_id["DERIV:EARLIER_PROOF_RECOVERY:OMITTED_DETERMINANT_PARITY"].status == "falsified"
    assert not any(
        e.dst in SUMMARY["result_ids"] + SUMMARY["derivation_ids"] and e.type == "formalizes"
        for e in built.edges
    )


def _fixture_review(target):
    digest = "ab" * 32
    return notes.Notes(
        archives=[{"id": "TEST", "description": "Fixture", "source": "Fixture"}],
        manifests={"TEST": [{"digest": digest, "paths": ["proof.md"], "size": 1}]},
        reviews=[
            {
                "archive": "TEST",
                "digest": digest,
                "verdict": "extract",
                "reason": "Named scoped extraction.",
                "bears_on": [target],
            }
        ],
    )


@pytest.mark.parametrize(
    "target",
    [
        "RESULT:EARLIER_GRAM_NULL_OPERATOR_QUOTIENT",
        "DERIV:EARLIER_PROOF_RECOVERY:GRAM_NULL_OPERATOR_QUOTIENT",
        SUMMARY["check_ids"][0],
        "G19",
        "HAMER_A4_NUM",
    ],
)
def test_reviews_accept_live_registered_targets_without_collecting(monkeypatch, target):
    def forbidden(*args, **kwargs):
        raise AssertionError("Source validation must not collect or execute the graph")

    monkeypatch.setattr(claims, "collect", forbidden)
    assert notes.validate(_fixture_review(target)) == []


@pytest.mark.parametrize("target", ["RESULT:NOT_REGISTERED", "DERIV:NOT:REGISTERED", "CHK:bad:bad"])
def test_native_id_spelling_does_not_make_an_unregistered_target_valid(target):
    errors = notes.validate(_fixture_review(target))
    assert any("unknown target" in e for e in errors)


def test_staple_checker_refuses_degenerate_geometry():
    with pytest.raises(ValueError, match="L>=3"):
        disjoint_staples(2, 0)
    with pytest.raises(ValueError, match="mu"):
        disjoint_staples(3, 4)
