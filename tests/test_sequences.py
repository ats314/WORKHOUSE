"""The sequence register, its builders, and the OEIS evidence gate."""

import copy
import re

import pytest
import yaml

from workhouse import claims as claims_mod
from workhouse import graph as graph_mod
from workhouse import oeis as oeis_mod


@pytest.fixture(scope="module")
def sequences():
    return oeis_mod.load()


def test_the_register_validates(sequences):
    assert oeis_mod.validate(sequences) == []


def test_every_builder_is_registered_and_returns_integers(sequences):
    for s in sequences:
        assert s.builder in oeis_mod.BUILDERS, s.id
        terms = s.terms
        assert len(terms) >= oeis_mod.MIN_TERMS, s.id
        assert all(isinstance(t, int) for t in terms), s.id


def test_recorded_terms_match_what_the_builders_return(sequences):
    """Terms are computed, never transcribed; the register only mirrors them."""
    for s in sequences:
        recorded = s.scan.get("terms")
        assert recorded is not None, f"{s.id} has no recorded scan"
        assert list(recorded) == s.terms, s.id


def test_every_sequence_says_what_a_hit_would_mean(sequences):
    for s in sequences:
        assert len(s.what_a_hit_would_mean.split()) >= 20, s.id
        assert s.generated_by in oeis_mod.GENERATED_BY, s.id


def test_recorded_verdicts_are_what_the_gate_returns(sequences):
    for s in sequences:
        got, _reason = oeis_mod.verdict(
            s, list(s.scan.get("hits", ())), s.scan["expected_by_chance"]
        )
        assert got == s.scan["verdict"], s.id


def test_a_closed_form_family_can_never_be_promoted_by_a_hit(sequences):
    """The gate's most important refusal, exercised on a fabricated hit."""
    closed = next(s for s in sequences if s.generated_by == "closed-form-in-N")
    got, reason = oeis_mod.verdict(closed, ["A000001"], 0.0)
    assert got == "not-evidence"
    assert "normalisation" in reason


def test_a_census_hit_needs_the_corrected_chance_count(sequences):
    census = next(s for s in sequences if s.generated_by == "census-output")
    # just inside the gate once the correlation correction is applied
    ok, _ = oeis_mod.verdict(
        census, ["A000001"], oeis_mod.MAX_EXPECTED / oeis_mod.CORRELATION_FACTOR / 10
    )
    assert ok == "hit"
    # ... and just outside it
    bad, _ = oeis_mod.verdict(
        census, ["A000001"], oeis_mod.MAX_EXPECTED / oeis_mod.CORRELATION_FACTOR * 10
    )
    assert bad == "not-evidence"


def test_absence_is_reported_before_the_evidence_gate(sequences):
    """No hit is no hit, whatever the sequence's length or provenance."""
    for s in sequences:
        got, reason = oeis_mod.verdict(s, [], 1.0)
        assert got == "no-hit"
        assert "no OEIS sequence contains" in reason


def test_the_snapshot_pin_is_a_digest_and_a_date():
    doc = yaml.safe_load(oeis_mod.REGISTRY.read_text(encoding="utf-8"))
    snap = doc["snapshot"]
    assert re.fullmatch(r"[0-9a-f]{64}", snap["sha256"])
    assert snap["source"] == oeis_mod.SNAPSHOT_URL
    assert snap["last_modified"] and snap["scanned"]
    assert snap["sequences_in_snapshot"] > 100_000
    assert snap["term_slots"] > 1_000_000


def test_the_correction_factor_covers_every_measured_control():
    doc = yaml.safe_load(oeis_mod.REGISTRY.read_text(encoding="utf-8"))
    controls = doc["null_model_controls"]
    assert {c["name"] for c in controls} == set(oeis_mod.CONTROLS)
    ratios = [c["ratio"] for c in controls if c["ratio"]]
    assert ratios and max(ratios) <= oeis_mod.CORRELATION_FACTOR
    for c in controls:
        if c["observed"] == 0:
            assert c["ratio"] is None


def test_validate_catches_a_broken_entry(tmp_path, sequences):
    """Mutate a deep copy and assert the validator notices."""
    doc = yaml.safe_load(oeis_mod.REGISTRY.read_text(encoding="utf-8"))
    for mutate, needle in (
        (lambda d: d["sequences"][0].update(builder="no_such_builder"), "unknown builder"),
        (lambda d: d["sequences"][0].update(generated_by="vibes"), "generated_by"),
        (lambda d: d["sequences"][0].update(what_a_hit_would_mean="  "), "what a hit"),
        (lambda d: d["sequences"].append(copy.deepcopy(d["sequences"][0])), "duplicate id"),
    ):
        broken = copy.deepcopy(doc)
        mutate(broken)
        path = tmp_path / "sequences.yaml"
        path.write_text(yaml.safe_dump(broken), encoding="utf-8")
        problems = oeis_mod.validate(oeis_mod.load(path))
        assert any(needle in p for p in problems), (needle, problems)


def test_the_needle_is_the_oeis_contiguous_run_form():
    """Signs are stripped on both sides: that is what the site's `seq:` does."""
    assert oeis_mod.needle([1, 2, 3]) == ",1,2,3,"
    assert oeis_mod.needle([-5, 7, -9]) == ",5,7,9,"


def test_the_match_ignores_signs_the_way_the_site_does():
    """`seq:` matches "possibly by ignoring signs"; `signed:` is the strict one.

    Sign-exact matching disagreed with the live site on 17 of 50 queries,
    always by finding fewer -- and the two registered families that are mostly
    negative are exactly where that would have hidden a hit.
    """
    signed = [("A000001", ",1,-2,3,-4,"), ("A000002", ",1,2,3,4,")]
    stripped = [(a, d.replace("-", "")) for a, d in signed]
    assert oeis_mod.matches(stripped, [1, 2, 3]) == ["A000001", "A000002"]
    assert oeis_mod.matches(stripped, [1, -2, 3]) == ["A000001", "A000002"]


def test_every_sequence_reaches_the_graph(sequences):
    catalogue = claims_mod.load_catalogue()
    ids = {c.id for c in catalogue}
    for s in sequences:
        assert f"SEQ:{s.id}" in ids, s.id
    g = graph_mod.build()
    assert not g.dangling
    edges = {(e.src, e.dst) for e in g.edges if e.source == graph_mod.SEQ_SOURCE}
    expected = {(f"SEQ:{s.id}", graph_mod.resolve_target(t)) for s in sequences for t in s.bears_on}
    assert edges >= expected


def test_an_oeis_node_exists_for_every_match_and_only_those(sequences):
    """A miss must not strand a node; a match must not be hidden by its verdict."""
    hits = {a for s in sequences for a in s.scan.get("hits", ())}
    catalogue = claims_mod.load_catalogue()
    nodes = {c.id for c in catalogue if c.id.startswith("OEIS:")}
    assert nodes == {f"OEIS:{a}" for a in hits}
    # The live case is a `not-evidence` match, so the node must exist anyway
    assert hits, "the calibration sequence should be matching something"
    assert any(c.status == "not-evidence" for c in catalogue if c.id.startswith("OEIS:"))


def test_one_oeis_node_per_a_number_however_many_sequences_match_it(sequences):
    """Two families matching one entry are one node with two edges, not a clash."""
    ids = [c.id for c in claims_mod.load_catalogue()]
    assert len(ids) == len(set(ids))
    g = graph_mod.build()
    for edge in (e for e in g.edges if e.type == "matches"):
        assert edge.src.startswith("OEIS:") and edge.dst.startswith("SEQ:")
