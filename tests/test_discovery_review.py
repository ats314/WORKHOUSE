"""The review register records, chains and proposes; it never writes a ledger."""

from __future__ import annotations

import hashlib
import json
import shutil
import subprocess
from argparse import ArgumentParser, Namespace
from pathlib import Path

import pytest
import yaml

from workhouse import discovery_review as R

T1, T2, T3 = (
    "2026-09-11T10:00:00+00:00",
    "2026-09-11T11:00:00+00:00",
    "2026-09-11T12:00:00+00:00",
)
RECORDS = [
    {"id": "RESULT:A", "kind": "result", "statement": "closure estimate", "where": "x"},
    {"id": "DERIV:DOC:S1", "kind": "result", "statement": "s1", "where": "docs/derivations/x.md"},
    {"id": "DERIV:DOC:S2", "kind": "result", "statement": "s2", "where": "docs/derivations/x.md"},
    {"id": "CITE:DOC", "kind": "citation", "statement": "doc"},
    {"id": "CITE:OTHER", "kind": "citation", "statement": "other"},
    {"id": "G1", "kind": "gap", "statement": "gap"},
    {"id": "CHK:suite:check", "kind": "check", "statement": "check"},
    {"id": "LEAN:lemma", "kind": "theorem", "statement": "lemma"},
    {"id": "LIT:PAPER:G1", "kind": "literature", "statement": "paper"},
]


def _write(root: Path, relative: str, text: str) -> Path:
    path = root / relative
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8", newline="\n")
    return path


def _sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


@pytest.fixture
def checkout(tmp_path):
    root = tmp_path / "repo"
    _write(root, "index/claims.jsonl", "".join(json.dumps(row) + "\n" for row in RECORDS))
    _write(root, "index/graph.jsonl", "")
    _write(root, "index/symbols.jsonl", json.dumps({"id": "ell_n"}) + "\n")
    _write(
        root, "docs/derivations/x.md", "".join(f"line {n} closure estimate\n" for n in range(1, 31))
    )
    _write(root, "ledger/results.yaml", "schema: results/v1\nresults: []\n")
    _write(root, "ledger/gaps.yaml", "unifying_candidates:\n  - id: U1\n  - id: U7\n")
    return root


class _StubIndex:
    def metadata(self, check_current=True, **_):
        return {"fingerprint": "fp-one", "freshness": "matched"}


class _StubEngine:
    index = _StubIndex()
    closed = False

    def close(self):
        self.closed = True


def _factory():
    return _StubEngine()


def _compact_search(root: Path) -> dict:
    return {
        "schema": "workhouse-discovery/compact/v1",
        "query": "closure estimate",
        "queries": ["closure estimate"],
        "seeds": [],
        "hits": [
            {
                "rank": 1,
                "group": "direct",
                "id": "RESULT:A",
                "kind": "record",
                "score": 0.016393,
                "channels": {"lexical": 1},
                "claim_ids": ["RESULT:A"],
                "source": {"where": "ledger/results.yaml#RESULT:A"},
                "excerpt": "closure estimate",
                "excerpt_truncated": False,
                "matched_terms": ["closure", "estimate"],
                "record": {"kind": "result", "status": "proven", "tier": 3},
                "commands": {"why": "uv run --no-sync workhouse why RESULT:A"},
            },
            {
                "rank": 2,
                "group": "direct",
                "id": "PASSAGE:abc",
                "kind": "passage",
                "score": 0.016,
                "channels": {"lexical": 2},
                "claim_ids": ["DERIV:DOC:S1"],
                "source": {
                    "path": "docs/derivations/x.md",
                    "lines": [10, 14],
                    "passage_lines": [8, 20],
                    "sha256": _sha(root / "docs/derivations/x.md"),
                    "passage_id": "PASSAGE:abc",
                },
                "excerpt": "line 10 closure estimate\nline 11 closure estimate\n",
                "excerpt_truncated": True,
                "matched_terms": ["closure"],
            },
            {
                "rank": 3,
                "group": "direct",
                "id": "PASSAGE:zzz",
                "kind": "passage",
                "score": 0.01,
                "channels": {"lexical": 3},
                "claim_ids": [],
                "source": {"path": "docs/derivations/y.md", "lines": [1, 2], "sha256": "0" * 64},
                "excerpt": "unrelated",
                "excerpt_truncated": False,
                "matched_terms": [],
            },
        ],
        "related": [],
        "provenance": {"fingerprint": "fp-one", "freshness": "matched"},
        "meaning": "candidates",
        "execution": {"python_checks": 0},
    }


def _evidence_file(root: Path, payload: dict, name: str = "search.json") -> Path:
    path = root.parent / name
    path.write_text(json.dumps(payload), encoding="utf-8")
    return path


def _register(root: Path) -> R.Register:
    return R.Register(root)


def _add(
    root,
    *,
    seed="RESULT:A",
    target="docs/derivations/x.md:10-14",
    kind="reusable-ingredient",
    evidence=None,
    timestamp=T1,
    note="the closure estimate feeds S1",
    slug=None,
):
    return _register(root).add(
        seed=seed,
        target=target,
        kind=kind,
        note=note,
        reviewer="test-agent",
        evidence=evidence or [],
        timestamp=timestamp,
        slug=slug,
        engine_factory=_factory,
    )


def _establish(root, review_id, at=T3):
    register = _register(root)
    register.mark(review_id, state="reviewing", reason="read both sources", timestamp=at)
    return register.mark(review_id, state="established", reason="hypotheses match", timestamp=at)


def _ns(**overrides) -> Namespace:
    base = {"json": True, "root": None, "register": None, "out": None}
    base.update(overrides)
    return Namespace(**base)


# -- recording --------------------------------------------------------------------------------


def test_add_records_pending_review_with_compact_evidence_and_hashes(checkout):
    evidence = _evidence_file(checkout, _compact_search(checkout))
    record = _add(checkout, evidence=[str(evidence)])
    path = checkout / "graph-tasks/discovery/reviews" / f"{record['id']}.yaml"
    assert path.is_file()
    assert R._ID.fullmatch(record["id"]) and record["id"].startswith("2026-09-11-")
    assert record["schema"] == R.SCHEMA and record["state"] == "pending"
    assert record["previous"] is None and len(record["sha256"]) == 64
    entry = record["evidence"][0]
    assert entry["command"] == "search"
    assert entry["argv"] == [
        "workhouse",
        "discover",
        "search",
        "closure estimate",
        "--limit",
        "3",
        "--json",
    ]
    assert entry["fingerprint"] == "fp-one" and entry["evidence_fingerprint"] == "fp-one"
    assert [row["id"] for row in entry["rows"]] == ["RESULT:A", "PASSAGE:abc"]
    assert all("commands" not in row for row in entry["rows"])
    assert entry["selection"].startswith("rows naming the seed or target")
    hashes = {(h["path"], tuple(h["lines"])): h for h in entry["source_hashes"]}
    assert hashes[("docs/derivations/x.md", (10, 14))]["sha256"] == _sha(
        checkout / "docs/derivations/x.md"
    )
    assert "stale_at_recording" not in hashes[("docs/derivations/x.md", (10, 14))]
    assert entry["excerpt_sha256"] == R._hash([row["excerpt"] for row in entry["rows"]])
    loaded = yaml.safe_load(path.read_text(encoding="utf-8"))
    assert loaded == record
    assert _register(checkout).validate()["problems"] == []


def test_full_search_output_is_compacted_before_it_is_copied(checkout):
    full = {
        "schema": "workhouse-discovery/v1",
        "query": "closure estimate",
        "queries": ["closure estimate"],
        "seeds": ["RESULT:A"],
        "hits": [
            {
                "id": "PASSAGE:abc",
                "kind": "passage",
                "path": "docs/derivations/x.md",
                "start_line": 8,
                "end_line": 20,
                "source_sha256": _sha(checkout / "docs/derivations/x.md"),
                "claim_ids": ["DERIV:DOC:S1"],
                "text": "".join(f"line {n} closure estimate\n" for n in range(8, 21)),
                "score": 0.5,
                "score_channels": {"lexical": {"rank": 1, "contribution": 0.01}},
            }
        ],
        "related": [],
        "provenance": {"fingerprint": "fp-one"},
    }
    record = _add(checkout, evidence=[str(_evidence_file(checkout, full))])
    entry = record["evidence"][0]
    row = entry["rows"][0]
    assert row["id"] == "PASSAGE:abc" and row["source"]["path"] == "docs/derivations/x.md"
    assert row["excerpt"].startswith("line 8") and "text" not in row
    assert entry["argv"][:5] == ["workhouse", "discover", "search", "closure estimate", "--seed"]


def test_connections_output_reconstructs_argv_and_matches_target(checkout):
    payload = {
        "schema": "workhouse-discovery/connections-compact/v1",
        "seed": {"id": "RESULT:A", "statement": "closure estimate"},
        "query": "closure estimate",
        "candidates": [
            {
                "rank": 1,
                "id": "DERIV:DOC:S2",
                "candidate_kind": "record",
                "excerpt": "s2",
                "path": ["RESULT:A <-[depends_on curated] DERIV:DOC:S2  (ledger)"],
                "record": {},
            },
            {"rank": 2, "id": "DERIV:DOC:S1", "candidate_kind": "record", "excerpt": "s1"},
        ],
        "provenance": {"fingerprint": "fp-one"},
    }
    record = _add(
        checkout, target="DERIV:DOC:S1", evidence=[str(_evidence_file(checkout, payload))]
    )
    entry = record["evidence"][0]
    assert entry["command"] == "connections"
    assert entry["argv"] == [
        "workhouse",
        "discover",
        "connections",
        "RESULT:A",
        "--limit",
        "2",
        "--json",
    ]
    assert [row["id"] for row in entry["rows"]] == ["DERIV:DOC:S1"]


def test_evidence_without_a_matching_row_keeps_top_rows_and_says_so(checkout):
    payload = _compact_search(checkout)
    payload["hits"] = payload["hits"][2:]
    record = _add(checkout, evidence=[str(_evidence_file(checkout, payload))])
    entry = record["evidence"][0]
    assert [row["id"] for row in entry["rows"]] == ["PASSAGE:zzz"]
    assert "no row named the seed or target" in entry["selection"]


def test_evidence_records_a_different_cache_than_the_one_observed(checkout):
    payload = _compact_search(checkout)
    payload["provenance"]["fingerprint"] = "fp-older"
    record = _add(checkout, evidence=[str(_evidence_file(checkout, payload))])
    assert record["evidence"][0]["fingerprint"] == "fp-one"
    assert "different discovery cache" in record["evidence"][0]["fingerprint_note"]


def test_reviewer_and_reasoning_are_mandatory(checkout, monkeypatch):
    monkeypatch.delenv(R.REVIEWER_ENV, raising=False)
    register = _register(checkout)
    with pytest.raises(R.ReviewError, match="reviewer"):
        register.add(seed="RESULT:A", target="G1", kind="documentary", note="n", reviewer=None)
    with pytest.raises(R.ReviewError, match="note"):
        register.add(seed="RESULT:A", target="G1", kind="documentary", note=" ", reviewer="x")
    monkeypatch.setenv(R.REVIEWER_ENV, "env-agent")
    record = register.add(seed="RESULT:A", target="G1", kind="documentary", note="n", reviewer=None)
    assert record["reviewer"] == "env-agent"


def test_seed_and_target_must_resolve(checkout):
    with pytest.raises(R.ReviewError, match="unknown record id"):
        _add(checkout, seed="RESULT:MISSING")
    with pytest.raises(R.ReviewError, match="lines must satisfy"):
        _add(checkout, target="docs/derivations/x.md:10-99")
    with pytest.raises(R.ReviewError, match="no such file"):
        _add(checkout, target="docs/derivations/nothing.md:1-2")
    with pytest.raises(R.ReviewError, match="must differ"):
        _add(checkout, seed="RESULT:A", target="RESULT:A")
    assert _add(checkout, target="SYM:ell_n")["target"] == "SYM:ell_n"


# -- closed vocabularies ------------------------------------------------------------------


@pytest.mark.parametrize("kind", sorted(R.RELATIONSHIP_KINDS))
def test_every_relationship_kind_is_accepted(checkout, kind):
    assert _add(checkout, kind=kind)["relationship_kind"] == kind


def test_relationship_kind_vocabulary_is_closed(checkout):
    assert {
        "shared-operator",
        "compatible-hypothesis",
        "reusable-ingredient",
        "equivalent-construction",
        "scope-restriction",
        "disagreement",
        "literature-bearing",
        "documentary",
        "unrelated",
    } == R.RELATIONSHIP_KINDS
    with pytest.raises(R.ReviewError, match="unknown relationship kind"):
        _add(checkout, kind="related")


def test_state_vocabulary_is_closed(checkout):
    assert {"pending", "reviewing", "established", "rejected", "registered"} == R.STATES
    assert set(R.TRANSITIONS) == R.STATES
    record = _add(checkout)
    with pytest.raises(R.ReviewError, match="unknown state"):
        _register(checkout).mark(record["id"], state="done", reason="r")


# -- transitions ---------------------------------------------------------------------------


@pytest.mark.parametrize(
    "path, allowed",
    [
        (["reviewing"], True),
        (["established"], False),
        (["rejected"], False),
        (["registered"], False),
        (["reviewing", "pending"], False),
        (["reviewing", "established"], True),
        (["reviewing", "rejected"], True),
        (["reviewing", "registered"], False),
        (["reviewing", "established", "reviewing"], False),
        (["reviewing", "established", "rejected"], False),
        (["reviewing", "rejected", "reviewing"], False),
        (["reviewing", "rejected", "established"], False),
    ],
)
def test_transition_rules(checkout, path, allowed):
    record = _add(checkout)
    register = _register(checkout)
    for state in path[:-1]:
        register.mark(record["id"], state=state, reason="step", timestamp=T2)
    if allowed:
        marked = register.mark(record["id"], state=path[-1], reason="step", timestamp=T2)
        assert marked["state"] == path[-1]
        assert [entry["state"] for entry in marked["history"]] == ["pending", *path]
        assert register.validate()["problems"] == []
    else:
        with pytest.raises(R.ReviewError, match="cannot move"):
            register.mark(record["id"], state=path[-1], reason="step", timestamp=T2)


def test_registered_requires_a_human_supplied_change_and_ledger_id(checkout):
    record = _establish(checkout, _add(checkout)["id"])
    register = _register(checkout)
    for bad in (None, "", "PR #150", "RESULT:A.depends_on", "landed yesterday"):
        with pytest.raises(R.ReviewError, match="registered.as"):
            register.mark(
                record["id"], state="registered", reason="merged", registered_as=bad, timestamp=T3
            )
    done = register.mark(
        record["id"],
        state="registered",
        reason="merged",
        registered_as="PR #150 (a1b2c3d) ledger/results.yaml RESULT:A.depends_on",
        timestamp=T3,
    )
    assert done["state"] == "registered" and done["registered_as"].startswith("PR #150")
    assert done["history"][-1]["registered_as"] == done["registered_as"]
    assert register.validate()["problems"] == []
    with pytest.raises(R.ReviewError, match="cannot move"):
        register.mark(record["id"], state="rejected", reason="undo", timestamp=T3)


def test_every_mark_needs_a_reason_and_history_is_append_only(checkout):
    record = _add(checkout)
    register = _register(checkout)
    with pytest.raises(R.ReviewError, match="reason"):
        register.mark(record["id"], state="reviewing", reason="  ", timestamp=T2)
    register.mark(record["id"], state="reviewing", reason="reading", timestamp=T2)
    with pytest.raises(R.ReviewError, match="append-only"):
        register.mark(record["id"], state="established", reason="done", timestamp=T1)


# -- hash chain -----------------------------------------------------------------------------


def _rewrite(path: Path, mutate) -> None:
    data = yaml.safe_load(path.read_text(encoding="utf-8"))
    mutate(data)
    path.write_text(yaml.safe_dump(data, sort_keys=True), encoding="utf-8")


def test_hash_chain_links_records_and_detects_tampering(checkout):
    first = _add(checkout, timestamp=T1, slug="one")
    second = _add(checkout, timestamp=T2, slug="two", note="second")
    third = _add(checkout, timestamp=T3, slug="three", note="third")
    register = _register(checkout)
    assert second["previous"] == first["genesis"] and third["previous"] == second["genesis"]
    report = register.validate()
    assert report["problems"] == [] and report["chain"] == "intact" and report["records"] == 3
    reviews = checkout / "graph-tasks/discovery/reviews"
    path2 = reviews / f"{second['id']}.yaml"
    original = path2.read_bytes()

    # Re-laying out the YAML without changing a value is not tampering.
    _rewrite(path2, lambda d: None)
    assert register.validate()["problems"] == []

    _rewrite(path2, lambda d: d.__setitem__("reasoning", "rewritten"))
    problems = register.validate()["problems"]
    assert any("genesis mismatch" in p for p in problems)
    assert any("sha256 mismatch" in p for p in problems)
    path2.write_bytes(original)

    _rewrite(path2, lambda d: d.__setitem__("state", "established"))
    problems = register.validate()["problems"]
    assert any("sha256 mismatch" in p for p in problems)
    assert any("disagrees with the last history entry" in p for p in problems)
    path2.write_bytes(original)

    path2.unlink()
    problems = register.validate()["problems"]
    assert any("chain broken" in p and third["id"] in p for p in problems)
    assert register.validate()["chain"] == "broken"
    path2.write_bytes(original)
    assert register.validate()["problems"] == []

    # Reordering by backdating the third record is caught twice over.
    path3 = reviews / f"{third['id']}.yaml"
    _rewrite(path3, lambda d: d.__setitem__("created", "2026-09-11T09:00:00+00:00"))
    problems = register.validate()["problems"]
    assert any("genesis mismatch" in p for p in problems)
    assert any("chain broken" in p for p in problems)


def test_register_cannot_be_backdated_on_add(checkout):
    _add(checkout, timestamp=T2)
    with pytest.raises(R.ReviewError, match="cannot be backdated"):
        _add(checkout, timestamp=T1, note="earlier")
    with pytest.raises(R.ReviewError, match="ISO-8601"):
        _add(checkout, timestamp="yesterday", note="later")


def test_validate_reports_endpoints_that_stopped_resolving(checkout):
    _add(checkout)
    (checkout / "docs/derivations/x.md").unlink()
    problems = _register(checkout).validate()["problems"]
    assert any("target locator" in p and "no such file" in p for p in problems)


# -- proposals -----------------------------------------------------------------------------


def test_contradictions_surface_is_refused_with_an_explanation(checkout, capsys):
    record = _establish(checkout, _add(checkout, kind="disagreement")["id"])
    code = R.run(
        _ns(
            discovery_command="propose",
            id=record["id"],
            surface="contradictions",
            root=str(checkout),
        ),
        _factory,
    )
    assert code == 1
    error = json.loads(capsys.readouterr().out)["error"]
    assert "C1-C22" in error and "contradicts" in error
    assert "cannot_decide" in error and "refuted" in error
    assert list((checkout / "graph-tasks/discovery/proposals").glob("*.yaml")) == []


def test_proposal_needs_an_established_review(checkout):
    register = _register(checkout)
    pending = _add(checkout)
    with pytest.raises(R.ReviewError, match="'pending'"):
        register.propose(pending["id"], "results")
    register.mark(pending["id"], state="reviewing", reason="r", timestamp=T2)
    register.mark(pending["id"], state="rejected", reason="not the same object", timestamp=T2)
    with pytest.raises(R.ReviewError, match="'rejected'"):
        register.propose(pending["id"], "results")
    unrelated = _establish(checkout, _add(checkout, kind="unrelated", timestamp=T2)["id"])
    with pytest.raises(R.ReviewError, match="nothing to register"):
        register.propose(unrelated["id"], "results")
    with pytest.raises(R.ReviewError, match="unknown surface"):
        register.propose(unrelated["id"], "symbols")


def test_results_proposal_names_the_result_and_the_field_for_the_kind(checkout):
    record = _establish(checkout, _add(checkout, target="DERIV:DOC:S1")["id"])
    path, proposal = _register(checkout).propose(record["id"], "results")
    assert path == checkout / "graph-tasks/discovery/proposals" / f"{record['id']}-results.yaml"
    assert proposal["schema"] == R.PROPOSAL_SCHEMA
    assert proposal["ledger_file"] == "ledger/results.yaml"
    fragment = proposal["fragment"]
    assert "`- id: RESULT:A`" in fragment
    assert "    depends_on:\n      - DERIV:DOC:S1\n" in fragment
    assert proposal["meaning"].startswith("PROPOSAL")
    assert [item["item"] for item in proposal["checklist"]] == [key for key, _ in R.CHECKLIST]
    assert any("workhouse status" in step for step in proposal["apply"])
    assert "never writes under ledger/" in proposal["refused"]["writes"]
    loaded = yaml.safe_load(path.read_text(encoding="utf-8"))
    assert loaded["fragment"] == fragment
    control = _establish(checkout, _add(checkout, target="CHK:suite:check", timestamp=T2)["id"])
    _, supported = _register(checkout).propose(control["id"], "results")
    assert (
        "    supported_by:\n      - target: CHK:suite:check\n        scope: <FILL"
        in (supported["fragment"])
    )
    bearing = _establish(
        checkout, _add(checkout, kind="compatible-hypothesis", target="G1", timestamp=T3)["id"]
    )
    _, bears = _register(checkout).propose(bearing["id"], "results")
    assert "    bears_on:\n      - G1\n" in bears["fragment"]


def test_gaps_proposal_carries_a_falsifier_placeholder_and_next_id(checkout):
    record = _establish(
        checkout, _add(checkout, kind="equivalent-construction", target="DERIV:DOC:S1")["id"]
    )
    _, proposal = _register(checkout).propose(record["id"], "gaps")
    fragment = proposal["fragment"]
    assert "  - id: U8\n" in fragment
    assert "    falsifier: |\n      <FILL BEFORE APPLYING" in fragment
    assert "    status: conjectured\n" in fragment
    assert "      - RESULT:A\n      - DERIV:DOC:S1\n" in fragment
    refuted = _establish(
        checkout, _add(checkout, kind="disagreement", target="DERIV:DOC:S2", timestamp=T2)["id"]
    )
    _, disagreement = _register(checkout).propose(refuted["id"], "gaps")
    assert "    status: refuted\n    refuted_2026_09_11: |" in disagreement["fragment"]


def test_derivation_documents_and_literature_fragments(checkout):
    register = _register(checkout)
    deriv = _establish(checkout, _add(checkout, seed="DERIV:DOC:S1", target="DERIV:DOC:S2")["id"])
    _, proposal = register.propose(deriv["id"], "derivation")
    assert "`id: DERIV:DOC:S1`" in proposal["fragment"]
    assert "    depends_on:\n    - DERIV:DOC:S2" in proposal["fragment"]
    lean = _establish(
        checkout, _add(checkout, seed="DERIV:DOC:S1", target="LEAN:lemma", timestamp=T2)["id"]
    )
    _, support = register.propose(lean["id"], "derivation")
    assert "    lean_support:\n    - name: lemma\n      scope: <FILL" in support["fragment"]
    docs = _establish(
        checkout,
        _add(checkout, seed="CITE:DOC", target="CITE:OTHER", kind="documentary", timestamp=T3)[
            "id"
        ],
    )
    _, cites = register.propose(docs["id"], "documents")
    assert (
        "`alias: DOC`" in cites["fragment"] and "    cites:\n      - OTHER\n" in cites["fragment"]
    )
    bearing = _establish(
        checkout,
        _add(checkout, seed="CITE:DOC", target="G1", kind="documentary", timestamp=T3)["id"],
    )
    _, bears = register.propose(bearing["id"], "documents")
    assert "    bears_on:\n      - G1" in bears["fragment"]
    lit = _establish(
        checkout,
        _add(checkout, seed="LIT:PAPER:G1", target="G1", kind="disagreement", timestamp=T3)["id"],
    )
    _, literature = register.propose(lit["id"], "literature")
    assert "`id: PAPER`" in literature["fragment"]
    assert "        relation: contradicts\n" in literature["fragment"]
    assert "status: transcription-unverified" in literature["fragment"]
    passage = _establish(
        checkout, _add(checkout, seed="CITE:DOC", kind="documentary", timestamp=T3)["id"]
    )
    _, located = register.propose(passage["id"], "documents")
    assert "<FILL: catalogue id carrying passage docs/derivations/x.md:10-14" in located["fragment"]


def test_proposal_checklist_reports_source_hash_state(checkout):
    evidence = _evidence_file(checkout, _compact_search(checkout))
    record = _establish(checkout, _add(checkout, evidence=[str(evidence)])["id"])
    register = _register(checkout)
    _, fresh = register.propose(record["id"], "results")
    hashes = next(i for i in fresh["checklist"] if i["item"] == "source_hashes_matched")
    assert hashes["done"] is True and fresh["evidence"] == record["evidence"]
    (checkout / "docs/derivations/x.md").write_text("changed\n" * 30, encoding="utf-8")
    _, stale = register.propose(record["id"], "results", out=str(checkout.parent / "stale.yaml"))
    hashes = next(i for i in stale["checklist"] if i["item"] == "source_hashes_matched")
    assert hashes["done"] is False and "changed" in hashes["observation"]


@pytest.mark.parametrize(
    "out",
    [
        "ledger/new.yaml",
        "index/new.yaml",
        "docs/derivations/new.yaml",
        "paper/x.yaml",
        "FRONTIER.md",
    ],
)
def test_out_under_a_scientific_tree_is_refused(checkout, out):
    record = _establish(checkout, _add(checkout)["id"])
    with pytest.raises(R.ReviewError, match="refused --out"):
        _register(checkout).propose(record["id"], "results", out=out)
    assert not (checkout / out).exists()


def test_out_elsewhere_works_once_and_never_overwrites(checkout, capsys):
    record = _establish(checkout, _add(checkout)["id"])
    out = checkout / ".graph-state/task/proposal.yaml"
    args = _ns(
        discovery_command="propose",
        id=record["id"],
        surface="results",
        out=str(out),
        root=str(checkout),
    )
    assert R.run(args, _factory) == 0
    written = out.read_bytes()
    assert json.loads(capsys.readouterr().out)["path"] == out.as_posix()
    assert R.run(args, _factory) == 1
    assert "error" in json.loads(capsys.readouterr().out)
    assert out.read_bytes() == written


# -- the whole cycle never touches the ledgers -----------------------------------------------


@pytest.mark.skipif(shutil.which("git") is None, reason="git is needed to observe the trees")
def test_full_cycle_leaves_ledger_and_index_unchanged(checkout, capsys):
    def git(*args):
        return subprocess.run(
            ["git", *args], cwd=checkout, capture_output=True, text=True, check=True
        ).stdout

    git("init", "-q")
    git("config", "user.email", "test@example.invalid")
    git("config", "user.name", "test")
    git("add", "-A")
    git("commit", "-q", "-m", "fixture")
    evidence = _evidence_file(checkout, _compact_search(checkout))
    common = {"root": str(checkout)}
    assert (
        R.run(
            _ns(
                discovery_command="review",
                review_command="add",
                seed="RESULT:A",
                target="docs/derivations/x.md:10-14",
                kind="reusable-ingredient",
                note="the estimate is the input",
                reviewer="test-agent",
                evidence=[str(evidence)],
                timestamp=T1,
                slug="cycle",
                **common,
            ),
            _factory,
        )
        == 0
    )
    review_id = json.loads(capsys.readouterr().out)["id"]
    for state, at in (("reviewing", T2), ("established", T3)):
        assert (
            R.run(
                _ns(
                    discovery_command="review",
                    review_command="mark",
                    id=review_id,
                    state=state,
                    reason="read",
                    registered_as=None,
                    reviewer=None,
                    timestamp=at,
                    **common,
                ),
                _factory,
            )
            == 0
        )
        capsys.readouterr()
    assert (
        R.run(_ns(discovery_command="propose", id=review_id, surface="results", **common), _factory)
        == 0
    )
    capsys.readouterr()
    assert (
        R.run(_ns(discovery_command="review", review_command="validate", **common), _factory) == 0
    )
    assert json.loads(capsys.readouterr().out)["problems"] == []
    assert git("status", "--short", "ledger", "index") == ""
    changed = {line[3:].split("/")[0] for line in git("status", "--short").splitlines()}
    assert changed == {"graph-tasks"}
    assert (
        R.run(
            _ns(discovery_command="review", review_command="list", state=None, **common), _factory
        )
        == 0
    )
    rows = json.loads(capsys.readouterr().out)
    assert [row["state"] for row in rows] == ["established"]


# -- replay --------------------------------------------------------------------------------


def test_replay_compares_fingerprints_sources_and_excerpts(checkout, monkeypatch, capsys):
    payload = _compact_search(checkout)
    record = _add(checkout, evidence=[str(_evidence_file(checkout, payload))])
    calls = []

    def fake_run(argv, root):
        calls.append((argv, root))
        return json.dumps(payload)

    monkeypatch.setattr(R, "_run_argv", fake_run)
    args = _ns(
        discovery_command="review", review_command="replay", id=record["id"], root=str(checkout)
    )
    assert R.run(args, _factory) == 0
    result = json.loads(capsys.readouterr().out)
    assert result["verdict"] == "matched"
    entry = result["entries"][0]
    assert entry["fingerprint"] == "matched" and entry["excerpt_sha256"] == "matched"
    assert all(source["sha256"] == "matched" for source in entry["sources"])
    assert calls[0][0][-1] == "--json" and calls[0][1] == checkout.resolve()

    payload["provenance"]["fingerprint"] = "fp-two"
    assert R.run(args, _factory) == 2
    assert json.loads(capsys.readouterr().out)["entries"][0]["fingerprint"] == "changed"

    payload["provenance"]["fingerprint"] = "fp-one"
    payload["hits"][1]["excerpt"] = "different words"
    (checkout / "docs/derivations/x.md").write_text("edited\n" * 30, encoding="utf-8")
    assert R.run(args, _factory) == 2
    entry = json.loads(capsys.readouterr().out)["entries"][0]
    assert entry["excerpt_sha256"] == "changed"
    assert {source["sha256"] for source in entry["sources"]} == {"changed"}

    monkeypatch.setattr(R, "_run_argv", lambda argv, root: json.dumps({"error": "unavailable"}))
    assert R.run(args, _factory) == 1
    assert json.loads(capsys.readouterr().out)["verdict"] == "error"


def test_replay_without_evidence_reports_nothing_to_compare(checkout):
    record = _add(checkout)
    result = _register(checkout).replay(record["id"])
    assert result["verdict"] == "no-evidence" and result["entries"] == []


# -- CLI surface -------------------------------------------------------------------------------


def test_add_parser_registers_review_and_propose_under_discover():
    parser = ArgumentParser()
    sub = parser.add_subparsers(dest="command")
    ds = sub.add_parser("discover")
    ds_sub = ds.add_subparsers(dest="discovery_command", required=True)
    R.add_parser(ds_sub)
    args = parser.parse_args(
        [
            "discover",
            "review",
            "add",
            "--seed",
            "A",
            "--target",
            "B",
            "--kind",
            "disagreement",
            "--note",
            "why",
            "--evidence",
            "e.json",
            "--timestamp",
            T1,
            "--json",
        ]
    )
    assert (args.discovery_command, args.review_command) == ("review", "add")
    assert args.evidence == ["e.json"] and args.json and args.root is None
    args = parser.parse_args(["discover", "propose", "ID", "--surface", "gaps", "--out", "p.yaml"])
    assert (args.discovery_command, args.id, args.surface, args.out) == (
        "propose",
        "ID",
        "gaps",
        "p.yaml",
    )
    args = parser.parse_args(
        ["discover", "review", "mark", "ID", "--state", "rejected", "--reason", "no"]
    )
    assert args.review_command == "mark" and args.state == "rejected"
    for command in ("list", "validate"):
        assert parser.parse_args(["discover", "review", command]).review_command == command
    assert parser.parse_args(["discover", "review", "replay", "ID"]).review_command == "replay"
    assert parser.parse_args(["discover", "review", "show", "ID"]).review_command == "show"
    with pytest.raises(SystemExit):
        parser.parse_args(
            [
                "discover",
                "review",
                "add",
                "--seed",
                "A",
                "--target",
                "B",
                "--kind",
                "related",
                "--note",
                "n",
            ]
        )


def test_list_show_and_validate_render_text_and_json(checkout, capsys):
    record = _add(checkout)
    common = {"root": str(checkout), "json": False}
    assert (
        R.run(
            _ns(discovery_command="review", review_command="list", state=None, **common), _factory
        )
        == 0
    )
    assert record["id"] in capsys.readouterr().out
    assert (
        R.run(
            _ns(discovery_command="review", review_command="list", state="rejected", **common),
            _factory,
        )
        == 0
    )
    assert capsys.readouterr().out.strip() == "no reviews recorded"
    assert (
        R.run(
            _ns(discovery_command="review", review_command="show", id=record["id"], **common),
            _factory,
        )
        == 0
    )
    shown = capsys.readouterr().out
    assert f"id: {record['id']}" in shown and "state: pending" in shown
    assert (
        R.run(_ns(discovery_command="review", review_command="show", id="nope", **common), _factory)
        == 1
    )
    assert "Review refused" in capsys.readouterr().out
    assert (
        R.run(_ns(discovery_command="review", review_command="validate", **common), _factory) == 0
    )
    assert "register valid" in capsys.readouterr().out


def test_register_directory_can_be_relocated_outside_the_checkout(checkout, tmp_path):
    elsewhere = tmp_path / "scratch-register"
    register = R.Register(checkout, elsewhere)
    record = register.add(
        seed="RESULT:A", target="G1", kind="documentary", note="n", reviewer="x", timestamp=T1
    )
    assert (elsewhere / "reviews" / f"{record['id']}.yaml").is_file()
    assert not (checkout / "graph-tasks").exists()
