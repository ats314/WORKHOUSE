"""Briefings preserve saved evidence and make freshness/execution explicit.

All inputs are synthetic. Collectors and checkout observations are isolated so
these tests never rebuild the real catalogue or inspect another working tree.
"""

from __future__ import annotations

import json
import os
from copy import deepcopy
from dataclasses import asdict
from pathlib import Path

import pytest

from workhouse import briefing as B
from workhouse import check_cache as CC
from workhouse import claims as C
from workhouse import cli as CLI
from workhouse import graph as G
from workhouse import navigator as N
from workhouse.invariants._core import Result

CHECK_ID = C.check_id("brief fixture", "one computation")


def _forbidden(*args, **kwargs):
    pytest.fail("saved/startup mode attempted a live collector or fallback")


def _catalogue():
    return [
        C.Claim("G_TEST", "gap", "A physical hypothesis remains open.", status="open"),
        C.Claim(
            CHECK_ID,
            "check",
            "A finite calculation passed.",
            tier=1,
            status="passing",
            reproduce="workhouse verify --only 'one computation'",
        ),
        C.Claim(
            "ROUTE_TEST",
            "route",
            "The earlier route failed under its original hypotheses.",
            status="falsified",
            detail="Preserve the obstruction; finite checks do not close the physical gap.",
        ),
    ]


def _graph():
    return G.Graph(
        edges=[
            G.Edge(CHECK_ID, "G_TEST", "bears_on", "curated", "ledger/evidence.yaml"),
            G.Edge("ROUTE_TEST", "G_TEST", "bears_on", "curated", "ledger/evidence.yaml"),
        ],
        dangling=[],
    )


def _write_rows(path, rows):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        "".join(json.dumps(row, sort_keys=True) + "\n" for row in rows),
        encoding="utf-8",
        newline="\n",
    )


def _bytes_under(root):
    return {p.relative_to(root).as_posix(): p.read_bytes() for p in root.rglob("*") if p.is_file()}


def _record(root):
    return B.record_index_state(root, B.content_manifest(root))


def _mutate_preserving_metadata(path):
    before = path.stat()
    original = path.read_bytes()
    assert b"open" in original
    path.write_bytes(original.replace(b"open", b"shut", 1))
    os.utime(path, ns=(before.st_atime_ns, before.st_mtime_ns))
    after = path.stat()
    assert (after.st_size, after.st_mtime_ns) == (before.st_size, before.st_mtime_ns)


@pytest.fixture
def graph_root(tmp_path, monkeypatch):
    root = tmp_path / "checkout"
    (root / "docs").mkdir(parents=True)
    (root / B.PROTOCOL_PATH).write_text("# Synthetic graph protocol\n", encoding="utf-8")
    (root / "ledger").mkdir()
    (root / "ledger/evidence.yaml").write_text("obligation: open\n", encoding="utf-8")
    _write_rows(root / B.INDEX_PATHS[0], [asdict(c) for c in _catalogue()])
    _write_rows(root / B.INDEX_PATHS[1], [])
    _write_rows(root / B.INDEX_PATHS[2], [asdict(e) for e in _graph().edges])

    monkeypatch.setattr(C, "ROOT", root)
    monkeypatch.setattr(CC, "ROOT", root)
    monkeypatch.setattr(C, "collect", _forbidden)
    monkeypatch.setattr(C, "load_catalogue", _forbidden)
    monkeypatch.setattr(C, "load_symbols", _forbidden)
    monkeypatch.setattr(G, "build", _forbidden)
    monkeypatch.setattr(G, "load", _forbidden)
    monkeypatch.setattr(N, "priority_rows", _forbidden)
    monkeypatch.setattr(N, "neighborhood", _forbidden)
    monkeypatch.setattr(
        B,
        "_checkout",
        lambda root, manifest: {
            "root": str(root),
            "revision": "a" * 40,
            "git_available": True,
            "dirty": [],
        },
    )
    monkeypatch.setattr(B, "_runtime", lambda: {"python": "fixture", "packages": {}})
    monkeypatch.setenv("XDG_CACHE_HOME", str(tmp_path / "cache"))
    monkeypatch.delenv("WORKHOUSE_NO_CACHE", raising=False)
    return root


@pytest.mark.parametrize("missing", B.INDEX_PATHS)
def test_missing_saved_index_never_falls_back_to_live(graph_root, missing):
    (graph_root / missing).unlink()
    before = _bytes_under(graph_root)
    brief = B.build_brief(["G_TEST"], root=graph_root)
    assert brief["status"] == "unavailable"
    assert any(missing in error for error in brief["errors"])
    assert brief["verification"]["executed"] == 0
    assert brief["verification"]["cache_reused"] == 0
    assert _bytes_under(graph_root) == before


@pytest.mark.parametrize(
    "state", [None, "{broken", '{"schema": "unsupported/v9"}', "[]", "null", "42"]
)
def test_saved_verdicts_without_valid_provenance_have_unknown_freshness(graph_root, state):
    if state is not None:
        path = graph_root / B.STATE_PATH
        path.parent.mkdir(parents=True)
        path.write_text(state, encoding="utf-8")
    brief = B.build_brief(["G_TEST"], root=graph_root)
    assert brief["status"] == "ok"
    assert brief["snapshot"]["freshness"] == "unknown"
    assert brief["verification"]["recorded"] == 1
    assert brief["verification"]["executed"] == 0
    assert B.validate_brief(brief, root=graph_root)


def test_matching_saved_snapshot_is_read_only_and_preserves_failed_routes(graph_root):
    _record(graph_root)
    before = _bytes_under(graph_root)
    brief = B.build_brief(["G_TEST"], root=graph_root)
    assert brief["status"] == "ok"
    assert brief["snapshot"]["freshness"] == "matched"
    assert B.validate_brief(brief, root=graph_root) == []
    verification = brief["verification"]
    assert (verification["recorded"], verification["cache_reused"], verification["executed"]) == (
        1,
        0,
        0,
    )
    assert verification["lean"]["executed"] is False
    target = brief["targets"][0]
    assert target["record"]["status"] == "open"
    assert target["neighbors"]["ROUTE_TEST"]["status"] == "falsified"
    assert target["routes"][0]["record"]["detail"] == _catalogue()[2].detail
    assert _bytes_under(graph_root) == before


def test_content_hash_detects_same_size_same_mtime_input_mutation(graph_root):
    _record(graph_root)
    before = B.build_brief("G_TEST", root=graph_root)
    _mutate_preserving_metadata(graph_root / "ledger/evidence.yaml")
    after = B.build_brief("G_TEST", root=graph_root)
    assert after["status"] == "ok"
    assert after["snapshot"]["freshness"] == "stale"
    assert after["input_manifest"]["sha256"] != before["input_manifest"]["sha256"]
    assert any("input content differs" in e for e in B.validate_brief(before, root=graph_root))
    assert after["verification"]["executed"] == 0


def test_changed_saved_graph_bytes_are_stale_even_when_json_meaning_is_unchanged(graph_root):
    _record(graph_root)
    path = graph_root / B.INDEX_PATHS[2]
    path.write_bytes(path.read_bytes() + b"\n")
    brief = B.build_brief("G_TEST", root=graph_root)
    assert brief["status"] == "ok"
    assert brief["snapshot"]["freshness"] == "stale"


@pytest.mark.parametrize("ids", [[], [""], ["  "], [None], [123], ["NO_SUCH_ID"]])
def test_invalid_targets_produce_failure_envelopes_without_checks(graph_root, ids):
    brief = B.build_brief(ids, root=graph_root)
    assert brief["status"] == "invalid_target"
    assert brief["errors"]
    assert brief["verification"]["executed"] == 0


def test_mixed_valid_and_unknown_targets_do_not_silently_drop_the_unknown(graph_root):
    brief = B.build_brief(["G_TEST", "NO_SUCH_ID"], root=graph_root)
    assert brief["status"] == "invalid_target"
    assert len(brief["targets"]) == 2
    assert any(target.get("id") == "G_TEST" for target in brief["targets"])
    assert any("NO_SUCH_ID" in error for error in brief["errors"])


@pytest.mark.parametrize(
    ("relative", "payload"),
    [
        ("index/claims.jsonl", b"{bad json\n"),
        ("index/claims.jsonl", b'{"id":"incomplete"}\n'),
        ("index/symbols.jsonl", b"\xff\n"),
        ("index/graph.jsonl", b'{"src":"G_TEST"}\n'),
    ],
)
def test_malformed_saved_index_is_unavailable_not_a_live_rebuild(graph_root, relative, payload):
    (graph_root / relative).write_bytes(payload)
    brief = B.build_brief("G_TEST", root=graph_root)
    assert brief["status"] == "unavailable"
    assert brief["errors"]
    assert brief["verification"]["executed"] == 0


@pytest.mark.parametrize("duplicate", ["claim", "symbol", "claim_symbol_collision"])
def test_duplicate_saved_node_ids_are_unavailable(graph_root, duplicate):
    claims = [asdict(c) for c in _catalogue()]
    symbols = []
    if duplicate == "claim":
        claims.append({**claims[0], "statement": "A conflicting version of the same claim."})
    elif duplicate == "symbol":
        symbols = [{"id": "fixture_symbol"}, {"id": "fixture_symbol"}]
    else:
        claims.append(asdict(C.Claim("SYM:fixture_symbol", "gap", "A conflicting node.")))
        symbols = [{"id": "fixture_symbol"}]
    _write_rows(graph_root / B.INDEX_PATHS[0], claims)
    _write_rows(graph_root / B.INDEX_PATHS[1], symbols)
    brief = B.build_brief("G_TEST", root=graph_root)
    assert brief["status"] == "unavailable"
    assert any("duplicate" in error for error in brief["errors"])
    assert brief["verification"]["executed"] == 0


@pytest.mark.parametrize("endpoint", ["src", "dst"])
def test_saved_edges_cannot_silently_reference_absent_nodes(graph_root, endpoint):
    edge = {**asdict(_graph().edges[0]), endpoint: "MISSING_NODE"}
    _write_rows(graph_root / B.INDEX_PATHS[2], [edge])
    brief = B.build_brief("G_TEST", root=graph_root)
    assert brief["status"] == "unavailable"
    assert any("unresolved graph endpoint" in error for error in brief["errors"])
    assert brief["verification"]["executed"] == 0


def test_unreadable_input_directory_cannot_produce_a_partial_fresh_manifest(
    graph_root, monkeypatch
):
    walk = B.os.walk

    def unreadable_ledger(path, *args, onerror=None, **kwargs):
        if Path(path) == graph_root / "ledger":
            assert onerror is not None
            onerror(PermissionError("synthetic ledger directory is unreadable"))
        return walk(path, *args, onerror=onerror, **kwargs)

    monkeypatch.setattr(B.os, "walk", unreadable_ledger)
    brief = B.build_brief("G_TEST", root=graph_root)
    assert brief["status"] == "unavailable"
    assert any("cannot enumerate input" in error for error in brief["errors"])
    assert brief["verification"]["executed"] == 0


def test_changed_claim_text_invalidates_the_saved_brief_fingerprint(graph_root):
    _record(graph_root)
    brief = B.build_brief("G_TEST", root=graph_root)
    tampered = deepcopy(brief)
    tampered["targets"][0]["record"]["status"] = "proven"
    errors = B.validate_brief(tampered, root=graph_root, check_current=False)
    assert any("snapshot fingerprint mismatch" in error for error in errors)


@pytest.mark.parametrize("manifest_name", ["input_manifest", "snapshot"])
def test_resigning_outer_envelope_does_not_hide_a_broken_content_manifest(
    graph_root, manifest_name
):
    _record(graph_root)
    brief = B.build_brief("G_TEST", root=graph_root)
    row = next(iter(brief[manifest_name]["files"].values()))
    row["sha256"] = "0" * 64
    brief["snapshot_fingerprint"] = B.data_hash(
        {key: value for key, value in brief.items() if key != "snapshot_fingerprint"}
    )
    errors = B.validate_brief(brief, root=graph_root, check_current=False)
    assert any(f"{manifest_name} content manifest digest mismatch" in error for error in errors)


@pytest.mark.parametrize("changed", ["input", "saved_index"])
def test_bytes_changing_between_graph_read_and_return_are_reported(
    graph_root, monkeypatch, changed
):
    _record(graph_root)
    neighborhoods = B._neighborhoods

    def change_after_read(*args, **kwargs):
        value = neighborhoods(*args, **kwargs)
        if changed == "input":
            _mutate_preserving_metadata(graph_root / "ledger/evidence.yaml")
        else:
            path = graph_root / B.INDEX_PATHS[0]
            path.write_bytes(path.read_bytes() + b"\n")
        return value

    monkeypatch.setattr(B, "_neighborhoods", change_after_read)
    brief = B.build_brief("G_TEST", root=graph_root)
    assert brief["status"] == "changed_during_read"
    assert brief["snapshot"]["freshness"] == "changed_during_read"
    assert B.validate_brief(brief, root=graph_root, check_current=False)


def test_checkout_change_during_read_is_not_reported_as_a_consistent_brief(graph_root, monkeypatch):
    observe = B._checkout
    calls = []

    def changing_checkout(root, manifest):
        checkout = observe(root, manifest)
        calls.append(1)
        checkout["revision"] = ("a" if len(calls) == 1 else "b") * 40
        return checkout

    monkeypatch.setattr(B, "_checkout", changing_checkout)
    brief = B.build_brief("G_TEST", root=graph_root)
    assert brief["status"] == "changed_during_read"
    assert brief["snapshot"]["freshness"] == "changed_during_read"


def test_current_validation_detects_checkout_change_after_brief(graph_root, monkeypatch):
    _record(graph_root)
    brief = B.build_brief("G_TEST", root=graph_root)
    observe = B._checkout

    def different_checkout(root, manifest):
        return {**observe(root, manifest), "revision": "b" * 40}

    monkeypatch.setattr(B, "_checkout", different_checkout)
    assert any("checkout revision differs" in e for e in B.validate_brief(brief, root=graph_root))


def test_index_provenance_is_not_written_after_inputs_change(graph_root):
    inputs = B.content_manifest(graph_root)
    _mutate_preserving_metadata(graph_root / "ledger/evidence.yaml")
    with pytest.raises(B.BriefingError) as failure:
        B.record_index_state(graph_root, inputs)
    assert failure.value.status == "changed_during_read"
    assert not (graph_root / B.STATE_PATH).exists()


def test_startup_is_a_notice_without_freshness_scan_or_checks(graph_root, monkeypatch):
    (graph_root / B.INDEX_PATHS[0]).unlink()
    before = _bytes_under(graph_root)
    monkeypatch.setattr(B, "content_manifest", _forbidden)
    monkeypatch.setattr(B, "_checkout", _forbidden)
    text = B.startup_text(root=graph_root)
    assert B.PROTOCOL_VERSION in text
    assert B.INDEX_PATHS[0] in text
    assert "unavailable" in text
    assert "workhouse brief" in text
    assert _bytes_under(graph_root) == before


def test_live_reuse_fresh_bypass_and_byte_change_have_distinct_execution_counts(
    graph_root, monkeypatch
):
    executions = []

    def collect_fixture():
        cache = CC.CheckCache()
        key = cache.key("brief fixture", "one computation", "synthetic computation")
        if cache.get(key) is None:
            executions.append(1)
            cache.put(key, Result("one computation", True, "computed under fixture inputs"))
        return _catalogue()

    monkeypatch.setattr(C, "collect", collect_fixture)
    monkeypatch.setattr(C, "symbol_records", lambda catalogue: [])
    monkeypatch.setattr(G, "build", lambda catalogue, symbols: _graph())
    saved_before = {rel: (graph_root / rel).read_bytes() for rel in B.INDEX_PATHS}

    first = B.build_brief("G_TEST", root=graph_root, live=True)
    reused = B.build_brief("G_TEST", root=graph_root, live=True)
    assert first["status"] == reused["status"] == "ok"
    assert first["verification"]["executed"] == 1
    assert reused["verification"]["cache_reused"] == 1
    assert reused["verification"]["executed"] == 0
    assert len(executions) == 1

    cache_dir = Path(os.environ["XDG_CACHE_HOME"])
    cache_before = _bytes_under(cache_dir)
    fresh = B.build_brief("G_TEST", root=graph_root, fresh=True)
    assert fresh["status"] == "ok"
    assert fresh["verification"]["mode"] == "fresh"
    assert fresh["verification"]["cache_reused"] == 0
    assert fresh["verification"]["executed"] == 1
    assert len(executions) == 2
    assert _bytes_under(cache_dir) == cache_before
    assert "WORKHOUSE_NO_CACHE" not in os.environ

    _mutate_preserving_metadata(graph_root / "ledger/evidence.yaml")
    changed = B.build_brief("G_TEST", root=graph_root, live=True)
    assert changed["status"] == "ok"
    assert changed["verification"]["cache_reused"] == 0
    assert changed["verification"]["executed"] == 1
    assert len(executions) == 3
    assert {rel: (graph_root / rel).read_bytes() for rel in B.INDEX_PATHS} == saved_before


def test_graph_build_failure_retains_completed_fresh_check_counts(graph_root, monkeypatch):
    completed = []

    def collect_fixture():
        completed.append(CHECK_ID)
        return _catalogue()

    def failed_graph(catalogue, symbols):
        raise ValueError("synthetic graph construction failed after Python checks")

    monkeypatch.setattr(C, "collect", collect_fixture)
    monkeypatch.setattr(C, "symbol_records", lambda catalogue: [])
    monkeypatch.setattr(G, "build", failed_graph)
    brief = B.build_brief("G_TEST", root=graph_root, fresh=True)
    assert completed == [CHECK_ID]
    assert brief["status"] == "unavailable"
    assert any("graph construction failed" in error for error in brief["errors"])
    assert brief["verification"]["mode"] == "fresh"
    assert brief["verification"]["executed"] == 1
    assert brief["verification"]["cache_reused"] == 0
    assert brief["verification"]["checks"][0]["id"] == CHECK_ID
    assert brief["verification"]["execution_state"] == "complete"


def test_interrupted_fresh_collection_reports_unknown_counts(graph_root, monkeypatch):
    def failed_collection():
        raise ValueError("synthetic interruption before catalogue completion")

    monkeypatch.setattr(C, "collect", failed_collection)
    brief = B.build_brief("G_TEST", root=graph_root, fresh=True)
    assert brief["status"] == "unavailable"
    assert any("interruption before catalogue completion" in error for error in brief["errors"])
    assert brief["verification"]["mode"] == "fresh"
    assert brief["verification"]["execution_state"] == "incomplete"
    assert brief["verification"]["executed"] is None
    assert brief["verification"]["cache_reused"] is None
    assert brief["verification"]["failed"] is None


@pytest.mark.parametrize("outcome", ["success", "invalid_graph", "nonconverged", "changed_inputs"])
def test_cli_index_records_provenance_only_after_valid_stable_convergence(
    graph_root, monkeypatch, capsys, outcome
):
    claims_path, symbols_path, graph_path = [graph_root / rel for rel in B.INDEX_PATHS]
    monkeypatch.setattr(C, "CLAIMS", claims_path)
    monkeypatch.setattr(C, "SYMBOLS", symbols_path)
    monkeypatch.setattr(G, "GRAPH", graph_path)
    events = []

    def write_claims():
        events.append("claims")
        if outcome == "nonconverged":
            claims_path.write_bytes(claims_path.read_bytes() + b"\n")
        elif outcome == "changed_inputs":
            _mutate_preserving_metadata(graph_root / "ledger/evidence.yaml")
        return claims_path, symbols_path

    def write_graph():
        events.append("graph")
        return graph_path

    def validate_graph():
        events.append("validate")
        return ["synthetic dangling endpoint"] if outcome == "invalid_graph" else []

    record = B.record_index_state

    def record_after_validation(root, inputs):
        assert events[-1] == "validate"
        events.append("record")
        return record(root, inputs)

    monkeypatch.setattr(C, "write", write_claims)
    monkeypatch.setattr(G, "write", write_graph)
    monkeypatch.setattr(G, "validate", validate_graph)
    monkeypatch.setattr(B, "record_index_state", record_after_validation)
    rc = CLI.main(["index", "--write"])
    assert rc == (0 if outcome == "success" else 1)
    assert (graph_root / B.STATE_PATH).exists() is (outcome == "success")
    if outcome == "success":
        assert events == ["claims", "graph", "validate", "record"]
        assert B.build_brief("G_TEST", root=graph_root)["snapshot"]["freshness"] == "matched"
    elif outcome == "nonconverged":
        assert events.count("claims") == 4
        assert "validate" not in events
        assert "record" not in events
    elif outcome == "invalid_graph":
        assert "record" not in events
    else:
        assert "record" in events
        assert "changed_during_read" in capsys.readouterr().err


def _route_cli_to_fixture(monkeypatch, root):
    build = B.build_brief

    def fixture_brief(ids, **kwargs):
        kwargs["root"] = root
        return build(ids, **kwargs)

    monkeypatch.setattr(B, "build_brief", fixture_brief)


def test_cli_exclusive_output_saves_a_valid_brief_without_stdout(graph_root, monkeypatch, capsys):
    _record(graph_root)
    _route_cli_to_fixture(monkeypatch, graph_root)
    destination = graph_root / "handoff.json"
    rc = CLI.main(["brief", "G_TEST", "--json", "--out", str(destination)])
    assert rc == 0
    saved = json.loads(destination.read_text(encoding="utf-8"))
    assert capsys.readouterr().out == ""
    assert B.validate_brief(saved, root=graph_root) == []


def test_cli_json_without_output_path_prints_a_valid_brief(graph_root, monkeypatch, capsys):
    _record(graph_root)
    _route_cli_to_fixture(monkeypatch, graph_root)
    before = _bytes_under(graph_root)
    assert CLI.main(["brief", "G_TEST", "--json"]) == 0
    brief = json.loads(capsys.readouterr().out)
    assert B.validate_brief(brief, root=graph_root) == []
    assert _bytes_under(graph_root) == before


def test_cli_out_refuses_to_overwrite_an_existing_receipt(graph_root, monkeypatch, capsys):
    _record(graph_root)
    _route_cli_to_fixture(monkeypatch, graph_root)
    destination = graph_root / "handoff.json"
    original = b"previous task receipt\n"
    destination.write_bytes(original)
    rc = CLI.main(["brief", "G_TEST", "--json", "--out", str(destination)])
    assert rc != 0
    assert destination.read_bytes() == original
    capsys.readouterr()


def test_cli_startup_requires_no_target_and_never_builds_a_brief(graph_root, monkeypatch, capsys):
    startup = B.startup_text
    monkeypatch.setattr(B, "startup_text", lambda *args, **kwargs: startup(root=graph_root))
    monkeypatch.setattr(B, "build_brief", _forbidden)
    monkeypatch.setattr(B, "content_manifest", _forbidden)
    assert CLI.main(["brief", "--startup"]) == 0
    assert B.PROTOCOL_VERSION in capsys.readouterr().out


@pytest.mark.parametrize(
    "extra", [["G_TEST"], ["--json"], ["--live"], ["--fresh"], ["--out", "unused.json"]]
)
def test_cli_startup_rejects_incompatible_flags_before_work(graph_root, monkeypatch, extra):
    monkeypatch.setattr(B, "startup_text", _forbidden)
    monkeypatch.setattr(B, "build_brief", _forbidden)
    with pytest.raises(SystemExit) as failure:
        CLI.main(["brief", "--startup", *extra])
    assert failure.value.code == 2
