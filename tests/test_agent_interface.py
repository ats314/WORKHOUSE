"""The machine-facing surface: JSON, colour policy, traversal, and the exports.

Every test here pins a property an agent depends on and a human would not
notice breaking. They exist because the interface was reported broken by an
agent rather than by a person: notes/imported/UPLOADS_2026-08-28i/
THEORY_GRAPH_AGENT_EXPERIENCE_NOTES_20260828.md.
"""

import io
import json
import subprocess
import sys

import pytest

from workhouse import branches, derive, graph, navigator, render, snapshot
from workhouse.cli import main

CHECKED = {"mode": "checked-index"}


def run(*argv):
    """Invoke the CLI in-process and capture what a pipe would receive."""
    buffer = io.StringIO()
    stdout, sys.stdout = sys.stdout, buffer
    try:
        code = main(list(argv))
    finally:
        sys.stdout = stdout
    return code, buffer.getvalue()


# -- colour policy --------------------------------------------------------


def test_no_ansi_reaches_a_pipe():
    """The reported failure: 41 escape sequences into a pipe that cannot see them.

    Asserted through a real subprocess, because the bug was in the *decision*
    (stdout.isatty()), and an in-process test that patches stdout would be
    testing the patch.
    """
    done = subprocess.run(
        [sys.executable, "-m", "workhouse.cli", "why", "C2", "--checked-index"],
        capture_output=True,
        text=True,
        check=False,
    )
    assert "\x1b[" not in done.stdout, "ANSI reached a pipe"
    assert "C2" in done.stdout, "stripping colour must not strip content"


def test_no_color_env_is_honoured(monkeypatch):
    monkeypatch.setenv("NO_COLOR", "")  # no-color.org: any value, including empty
    assert render.should_color(io.StringIO()) is False


def test_force_color_beats_a_pipe(monkeypatch):
    monkeypatch.delenv("NO_COLOR", raising=False)
    monkeypatch.setenv("FORCE_COLOR", "1")
    assert render.should_color(io.StringIO()) is True


def test_explicit_flag_beats_the_environment(monkeypatch):
    monkeypatch.setenv("NO_COLOR", "1")
    assert render.should_color(io.StringIO(), override=True) is True


def test_strip_ansi_leaves_text_alone():
    assert render.strip_ansi("\x1b[1mC2\x1b[0m — 5/48") == "C2 — 5/48"


# -- JSON surface ---------------------------------------------------------


@pytest.mark.parametrize(
    "argv",
    [
        ("why", "C2", "--checked-index", "--json"),
        ("search", "5/48", "--json"),
        ("status", "--json"),
        ("branches", "--checked-index", "--json"),
        ("drift", "--json"),
        ("derive", "C2", "--checked-index", "--json"),
        ("verify", "--only", "t_N = B_N - A_N", "--json"),
    ],
)
def test_json_mode_emits_one_parseable_document(argv):
    _code, text = run(*argv)
    payload = json.loads(text)
    assert payload["schema"] == render.SCHEMA
    assert payload["command"] == argv[0]


def test_json_is_never_painted():
    """SGR codes inside a JSON string value are a parsing trap, not decoration."""
    _code, text = run("why", "C2", "--checked-index", "--json", "--color")
    assert "\x1b[" not in text


def test_why_json_reports_a_miss_without_inventing_a_node():
    code, text = run("why", "NO-SUCH-ID", "--checked-index", "--json")
    payload = json.loads(text)
    assert code == 1 and payload["found"] is False and payload["id"] is None
    assert "hint" in payload


def test_verify_json_carries_a_rerun_command_per_check():
    _code, text = run("verify", "--only", "t_N = B_N - A_N", "--json")
    payload = json.loads(text)
    assert payload["total"] >= 1
    for check in payload["checks"]:
        assert check["reproduce"].startswith("workhouse verify --only ")


# -- traversal ------------------------------------------------------------


def test_depth_one_is_exactly_the_incident_edges():
    """The default view must not change shape now that --depth exists."""
    g = graph.load()
    edges, depth_of = navigator.traverse(g, "C2", depth=1)
    assert set(edges) == {e for e in g.edges if "C2" in (e.src, e.dst)}
    assert depth_of["C2"] == 0


def test_depth_is_monotone_and_terminates():
    g = graph.load()
    sizes = [len(navigator.traverse(g, "C2", depth=d)[0]) for d in (1, 2, 3)]
    assert sizes[0] < sizes[1] < sizes[2]
    # A depth past the graph's diameter must stop, not loop on a cycle.
    assert len(navigator.traverse(g, "C2", depth=99)[0]) <= len(g.edges)


def test_relations_filter_keeps_only_named_types():
    g = graph.load()
    edges, _ = navigator.traverse(g, "C2", depth=2, relations={"blocks", "resolves"})
    assert edges and {e.type for e in edges} <= {"blocks", "resolves"}


def test_traversal_is_deterministic():
    g = graph.load()
    first = navigator.traverse(g, "C2", depth=2)[0]
    second = navigator.traverse(g, "C2", depth=2)[0]
    assert first == second


def test_unknown_relation_is_refused_not_silently_empty():
    """An empty result and a typo must not look the same to a caller."""
    code, text = run("why", "C2", "--checked-index", "--relations", "blocsk")
    assert code == 1 and "unknown relation" in text


# -- evidence and next actions --------------------------------------------


def test_evidence_carries_the_pin_and_the_observed_quote():
    rows = navigator.evidence_for("C2")
    assert len(rows) >= 2, "C2's two sides each have a pinned originating document"
    for row in rows:
        assert len(row["sha256"]) == 64
        assert row["quote"] and row["path"]


def test_next_actions_are_harvested_never_composed():
    """Every offered command must be some record's own `reproduce` field."""
    payload = navigator.payload("C2", **CHECKED)
    recorded = {
        c.reproduce
        for c in __import__("workhouse.claims", fromlist=["x"]).load_catalogue()
        if c.reproduce
    }
    assert payload["next_actions"]
    for action in payload["next_actions"]:
        assert action["command"] in recorded


# -- replay status --------------------------------------------------------


def test_replay_status_is_a_known_vocabulary():
    payload = navigator.payload("C2", **CHECKED)
    assert payload["replay"]["status"] in navigator.REPLAY


# -- checked-index mode ---------------------------------------------------


def test_checked_index_and_live_agree_on_a_current_tree():
    """If these disagree, one of them is lying to somebody."""
    live = navigator.payload("C2", mode="live")
    checked = navigator.payload("C2", mode="checked-index")
    assert {e["src"] + e["type"] + e["dst"] for e in live["edges"]} == {
        e["src"] + e["type"] + e["dst"] for e in checked["edges"]
    }


def test_checked_index_mode_says_so():
    _code, text = run("why", "C2", "--checked-index")
    assert "index/" in text and "live" in text


# -- branches -------------------------------------------------------------


def test_branches_prints_both_sides_and_promotes_neither():
    """Structural, not a word blacklist.

    The first version of this test scanned the rendered text for "average" and
    failed on the view's own banner -- "never average, never pick". A prose
    blacklist cannot tell a prohibition from a recommendation, so the property
    is asserted where it actually lives: both sides survive in the ledger's own
    order, neither carries a field marking it chosen, and both values are
    printed verbatim so a reader compares them rather than a summary.
    """
    from workhouse import ledger as ledger_mod

    data = branches.collect(**CHECKED)
    c2 = next(b for b in data["branches"] if b["id"] == "C2")
    recorded = next(c for c in ledger_mod.load().contradictions if c["id"] == "C2")

    assert [s["label"] for s in c2["sides"]] == [s["label"] for s in recorded["sides"]]
    for side in c2["sides"]:
        assert not (set(side) - set(recorded["sides"][0]) - {"originates_in", "decimal"}), (
            "a side gained a field the ledger never recorded"
        )
    text = render.strip_ansi(branches.render(data))
    for side in recorded["sides"]:
        assert str(side["value"]) in text
    assert str(recorded["delta"]) in text


def test_branches_names_the_gap_that_would_settle_it():
    data = branches.collect(**CHECKED)
    c2 = next(b for b in data["branches"] if b["id"] == "C2")
    assert [g["id"] for g in c2["settled_by"]] == ["G3"]


# -- derive ---------------------------------------------------------------


def test_derive_orders_support_by_distance_and_cites_its_source():
    data = derive.collect(["C2"], depth=2, **CHECKED)
    section = data["sections"][0]
    assert set(section["layers"]) == {"1", "2"}
    for rows in section["layers"].values():
        for row in rows:
            assert row["source"], "every row names the file its edge was read from"
            assert row["relation"] in derive.SUPPORTS


def test_derive_reports_an_unresolved_root_rather_than_dropping_it():
    code, text = run("derive", "NOT-AN-ID", "--checked-index")
    assert code == 1 and "NOT-AN-ID" in text


def test_derive_markdown_says_reachability_is_not_entailment():
    """The one sentence that keeps this export honest."""
    text = derive.render_markdown(derive.collect(["C2"], depth=1, **CHECKED))
    assert "not a proof" in text and "Reachability is not entailment" in text


def test_every_support_relation_is_a_real_graph_relation():
    assert set(derive.SUPPORTS) <= graph.TYPES


# -- drift ----------------------------------------------------------------


def test_drift_is_clean_on_a_current_tree():
    data = snapshot.compare()
    assert not data["stale"], f"index/ has drifted: {data['changed']}"


def test_generated_records_use_posix_paths():
    """Byte-determinism across platforms, for the generated files themselves.

    The agent memo found 47 provenance `source` fields differing between a
    Windows live build and the checked file purely by path separator. That has
    since been fixed at the source (`source_path` calls `as_posix`); this is
    what stops it coming back through some other generator.
    """
    offenders = [e.source for e in graph.load().edges if "\\" in e.source]
    assert not offenders, f"non-POSIX separators in generated edges: {offenders[:5]}"
