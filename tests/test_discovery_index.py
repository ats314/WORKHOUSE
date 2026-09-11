"""Discovery retrieval preserves source identity without executing mathematics."""

import hashlib
import json
import os
from pathlib import Path

import pytest

from workhouse.discovery_index import DiscoveryIndex, tokenize


def _write(root, relative, text):
    path = root / relative
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8", newline="")
    return path


def _repo(tmp_path, records=None):
    root = tmp_path / "repo"
    root.mkdir()
    records = records or [{"id": "G1", "statement": "Ground state closure", "kind": "gap"}]
    for name, rows in (("claims", records), ("graph", []), ("symbols", [])):
        _write(root, f"index/{name}.jsonl", "".join(json.dumps(row) + "\n" for row in rows))
    return root


def test_exact_signed_values_and_mathematical_tokens():
    assert tokenize("-10/96 10/96 C_shp t_N α β") == [
        "-5/48",
        "5/48",
        "c_shp",
        "t_n",
        "alpha",
        "beta",
    ]


def test_signed_fraction_retrieval_does_not_conflate_values(tmp_path):
    root = _repo(tmp_path)
    _write(root, "theory/negative.md", "The coefficient is -5/48.\n")
    _write(root, "theory/positive.md", "The coefficient is 5/48.\n")
    with DiscoveryIndex(root) as index:
        hits = index.search("-10/96")
        assert [row["path"] for row in hits] == ["theory/negative.md"]
        assert [row["path"] for row in index.search("10/96")] == ["theory/positive.md"]


def test_quotes_and_match_operators_are_only_query_text(tmp_path):
    root = _repo(tmp_path)
    _write(root, "theory/source.md", "alpha source\n")
    with DiscoveryIndex(root) as index:
        assert index.search('alpha" OR * NEAR(foo,bar) NOT (')
        assert index.search('"*:()') == []


def test_passage_line_provenance_and_range_scoped_claim_links(tmp_path):
    records = [
        {"id": "CITE:TEST", "statement": "source", "where": "docs/derivations/test.md"},
        {
            "id": "DERIV:EARLY",
            "statement": "first",
            "where": "docs/derivations/test.md (lines 1-2)",
        },
        {
            "id": "DERIV:LATE",
            "statement": "last",
            "where": "docs/derivations/test.md (lines 35-36)",
        },
        {
            "id": "DERIV:UNSCOPED",
            "statement": "other",
            "where": "docs/derivations/test.md (## Other)",
        },
    ]
    root = _repo(tmp_path, records)
    text = "".join(f"paragraph{i} " + "geometry " * 40 + "\n" for i in range(1, 40))
    path = _write(root, "docs/derivations/test.md", text)
    with DiscoveryIndex(root) as index:
        hits = [h for h in index.search("paragraph1", 10) if h["kind"] == "passage"]
        assert hits
        row = hits[0]
        assert set(row["claim_ids"]) == {"CITE:TEST", "DERIV:EARLY"}
        assert row["claim_spans"]["DERIV:EARLY"] == {
            "start_line": 1,
            "end_line": 2,
            "scope": "registered_lines",
        }
        assert row["text"] == "".join(
            text.splitlines(keepends=True)[row["start_line"] - 1 : row["end_line"]]
        )
        assert row["source_sha256"] == hashlib.sha256(path.read_bytes()).hexdigest()


def test_record_hits_point_to_exact_saved_jsonl(tmp_path):
    root = _repo(tmp_path)
    with DiscoveryIndex(root) as index:
        row = index.search("Ground state closure")[0]
        assert row["kind"] == "record" and row["claim_ids"] == ["G1"]
        assert row["text"] == (root / row["path"]).read_text().splitlines()[row["start_line"] - 1]
        assert row["statement"] == "Ground state closure"


def test_content_hash_detects_same_size_same_mtime_edit(tmp_path):
    root = _repo(tmp_path)
    source = _write(root, "notes/imported/source.md", "alpha geometry\n")
    with DiscoveryIndex(root) as index:
        first = index.build()
        timestamp = source.stat()
        source.write_text("gamma geometry\n", encoding="utf-8", newline="")
        os.utime(source, ns=(timestamp.st_atime_ns, timestamp.st_mtime_ns))
        assert source.stat().st_size == timestamp.st_size
        assert index.metadata()["freshness"] == "stale"
        second = index.build()
        assert first["fingerprint"] != second["fingerprint"]
        assert index.search("alpha") == []
        assert index.search("gamma")


def test_content_addressed_cache_reuse_and_corruption_recovery(tmp_path):
    root = _repo(tmp_path)
    _write(root, "theory/source.md", "alpha geometry\n")
    with DiscoveryIndex(root) as index:
        first = index.build()
        assert not first["cache_reused"]
        second = index.build()
        assert second["cache_reused"] and second["fingerprint"] == first["fingerprint"]
    Path(first["cache_path"]).write_bytes(b"broken disposable cache")
    with DiscoveryIndex(root) as index:
        recovered = index.build()
        assert not recovered["cache_reused"]
        assert "cache_recovery" in recovered
        preserved = list(Path(first["cache_path"]).parent.glob("*.invalid-*.sqlite3"))
        assert len(preserved) == 1
        assert preserved[0].read_bytes() == b"broken disposable cache"
        assert index.search("alpha")


def test_missing_or_malformed_saved_index_never_collects(tmp_path, monkeypatch):
    from workhouse import claims

    def forbidden():
        pytest.fail("Discovery must never execute claims.collect")

    monkeypatch.setattr(claims, "collect", forbidden)
    root = tmp_path / "empty"
    root.mkdir()
    with DiscoveryIndex(root) as index, pytest.raises(FileNotFoundError):
        index.build()
    root = _repo(tmp_path)
    _write(root, "index/graph.jsonl", '{"src":"G1"}\n')
    with DiscoveryIndex(root) as index, pytest.raises(ValueError, match="Invalid saved record"):
        index.build()


def test_declared_source_scope_and_exclusions(tmp_path):
    root = _repo(tmp_path)
    for relative in (
        "theory/a.md",
        "docs/derivations/b.tex",
        "notes/imported/c.txt",
        "research/new/d.md",
    ):
        _write(root, relative, "specialneedle\n")
    for relative in ("research/runs/no.md", "literature/INBOX/no.md", "outside/no.md"):
        _write(root, relative, "specialneedle\n")
    _write(root, "theory/invalid.txt", "valid").write_bytes(b"\xff\xfe")
    with DiscoveryIndex(root) as index:
        meta = index.build()
        assert meta["source_count"] == 4
        assert len(index.search("specialneedle")) == 4
        assert {"path": "theory/invalid.txt", "reason": "non_utf8"} in meta["source_exclusions"]
        assert meta["execution"] == {"checks_executed": 0, "lean_compiled": False}


def test_symlink_source_escape_is_excluded(tmp_path):
    root = _repo(tmp_path)
    outside = _write(tmp_path, "outside.md", "secretexternal\n")
    link = root / "theory/escape.md"
    link.parent.mkdir()
    try:
        link.symlink_to(outside)
    except OSError:
        pytest.skip("Host does not permit creating symlinks")
    with DiscoveryIndex(root) as index:
        meta = index.build()
        assert index.search("secretexternal") == []
        assert {"path": "theory/escape.md", "reason": "unsafe_path"} in meta["source_exclusions"]


def test_oversized_single_line_is_bounded_and_exact(tmp_path):
    root = _repo(tmp_path)
    text = "longword " * 3000
    _write(root, "theory/long.md", text)
    with DiscoveryIndex(root) as index:
        hits = index.search("longword")
        assert len(hits) == 3
        for hit in hits:
            assert len(hit["text"]) <= 12000
            assert hit["start_line"] == hit["end_line"] == 1
            assert hit["text"] == text[hit["start_col"] - 1 : hit["end_col"]]


def test_unicode_minus_preserves_fraction_polarity(tmp_path):
    root = _repo(tmp_path)
    _write(root, "theory/negative.md", "The coefficient is −5/48.\n")
    _write(root, "theory/positive.md", "The coefficient is 5/48.\n")
    assert tokenize("−10/96") == tokenize("-5/48")
    with DiscoveryIndex(root) as index:
        for query in ("−10/96", "-10/96", "−5/48"):
            assert [row["path"] for row in index.search(query)] == ["theory/negative.md"]
        assert [row["path"] for row in index.search("5/48")] == ["theory/positive.md"]


def test_literal_hash_and_parentheses_in_source_names_keep_graph_joins(tmp_path):
    hashed = "corpus-import/#-Final-unified-theory.txt"
    numbered = "paper/STATUS_fourth_order_build (2).md"
    records = [
        {"id": "CORPUS:HASH", "statement": "source", "where": hashed},
        {"id": "CITE:NUMBERED", "statement": "source", "where": numbered},
        {"id": "DERIV:SCOPED", "statement": "lemma", "where": numbered + " (lines 2-3)"},
        {"id": "DERIV:COLON", "statement": "lemma", "where": hashed + ":2-3"},
        {
            "id": "DERIV:NOMATCH",
            "statement": "lemma",
            "where": "paper/STATUS_fourth_order_build (3).md",
        },
    ]
    root = _repo(tmp_path, records)
    _write(root, hashed, "hashneedle\nprecise identity\n")
    _write(root, numbered, "numberneedle\nprecise identity\n")
    with DiscoveryIndex(root) as index:
        hashed_hit = next(row for row in index.search("hashneedle") if row["kind"] == "passage")
        numbered_hit = next(row for row in index.search("numberneedle") if row["kind"] == "passage")
        assert hashed_hit["claim_ids"] == ["CORPUS:HASH", "DERIV:COLON"]
        assert numbered_hit["claim_ids"] == ["CITE:NUMBERED", "DERIV:SCOPED"]
        assert numbered_hit["claim_spans"]["DERIV:SCOPED"]["start_line"] == 2


@pytest.mark.parametrize("magnitude", ["1", "0.75", ".75", "2.5e-3"])
def test_integer_and_decimal_signs_survive_numeric_tokenization(tmp_path, magnitude):
    root = _repo(tmp_path)
    _write(root, "theory/negative.md", "The value is −" + magnitude + ".\n")
    _write(root, "theory/positive.md", "The value is " + magnitude + ".\n")
    assert tokenize("−" + magnitude) == tokenize("-" + magnitude) == ["-" + magnitude]
    assert tokenize("+" + magnitude) == tokenize(magnitude) == [magnitude]
    with DiscoveryIndex(root) as index:
        for query in ("-" + magnitude, "−" + magnitude):
            assert [row["path"] for row in index.search(query)] == ["theory/negative.md"]
        assert [row["path"] for row in index.search("+" + magnitude)] == ["theory/positive.md"]


def test_rational_plus_and_denominator_signs_are_canonical():
    assert tokenize("+10/96 10/+96 -10/-96") == ["5/48"] * 3
    assert tokenize("10/-96 −10/+96") == ["-5/48"] * 2
    assert tokenize("−5/5") == tokenize("-1") == ["-1"]


def test_metadata_can_reuse_the_build_observation_only_when_asked(tmp_path):
    root = _repo(tmp_path)
    _write(root, "theory/note.md", "original content\n")
    index = DiscoveryIndex(root, cache_dir=tmp_path / "cache")
    first = index.build()
    (root / "theory" / "note.md").write_text("changed content\n", encoding="utf-8")
    reused = index.metadata(recheck=False)
    assert reused["freshness"] == "matched"
    assert reused["freshness_observation"] == "hashed at engine start in this process"
    assert reused["current_fingerprint"] == first["fingerprint"]
    rechecked = index.metadata()
    assert rechecked["freshness"] == "stale"
    assert rechecked["freshness_observation"] == "sources rehashed for this call"
    # A recheck refreshes the observation that later reuse reports.
    assert index.metadata(recheck=False)["freshness"] == "stale"
    index.close()


def test_plain_file_rejects_links_and_directories(tmp_path):
    target = tmp_path / "real.md"
    target.write_text("x\n", encoding="utf-8")
    assert DiscoveryIndex._plain_file(target)
    assert not DiscoveryIndex._plain_file(tmp_path)
    assert not DiscoveryIndex._plain_file(tmp_path / "missing.md")
    link = tmp_path / "link.md"
    try:
        link.symlink_to(target)
    except (OSError, NotImplementedError):
        pytest.skip("symlinks unavailable")
    assert not DiscoveryIndex._plain_file(link)


# --- external workstation roots ----------------------------------------------


def _external(tmp_path, monkeypatch, roots, records=None, **scope_extra):
    """A checkout plus a workstation base holding the declared external roots."""
    import yaml

    from workhouse import discovery_scope as S

    root = _repo(tmp_path, records)
    base = tmp_path / "ws"
    base.mkdir(exist_ok=True)
    monkeypatch.setenv(S.BASE_ENV, str(base))
    scope = {"schema": S.SCHEMA, "version": 1, "roots": roots, **scope_extra}
    _write(root, S.SCOPE_PATH, yaml.safe_dump(scope))
    return root, base


def _passages(index, query):
    return [row for row in index.search(query) if row["kind"] == "passage"]


def test_external_locator_prefix_and_row_provenance(tmp_path, monkeypatch):
    root, base = _external(tmp_path, monkeypatch, [{"label": "notes", "path": "notes", "tier": 1}])
    _write(base, "notes/deep/#odd (1).md", "externalneedle geometry\n")
    _write(root, "theory/inside.md", "internalneedle geometry\n")
    with DiscoveryIndex(root) as index:
        meta = index.build()
        hit = _passages(index, "externalneedle")[0]
        assert hit["path"] == "ext:notes/deep/#odd (1).md"
        assert hit["source_locator"] == "ext:notes/deep/#odd (1).md:1"
        assert hit["external"] is True and hit["source_label"] == "notes"
        assert hit["aliases"] == [] and hit["claim_ids"] == []
        internal = _passages(index, "internalneedle")[0]
        assert internal["external"] is False and internal["source_label"] == "checkout"
        assert meta["source_count"] == 2
        assert meta["internal_source_count"] == 1 and meta["external_source_count"] == 1
        assert meta["settings"]["external_roots"] == ["notes"]
        assert meta["external_base"] == str(base.resolve())
        assert meta["freshness_policy"] == {
            "internal": "content-hash every call",
            "external": "stat then content-hash on change",
        }
        (row,) = meta["external_roots"]
        assert row["label"] == "notes" and row["present"] and row["skipped"] is None
        assert (row["files"], row["sources"], row["aliases"], row["passages"]) == (1, 1, 0, 1)
        assert row["bytes"] == len("externalneedle geometry\n")


def test_external_content_dedup_records_aliases_and_does_not_rechunk(tmp_path, monkeypatch):
    root, base = _external(
        tmp_path,
        monkeypatch,
        [
            {"label": "first", "path": "first", "tier": 1},
            {"label": "second", "path": "second", "tier": 2},
        ],
    )
    text = "sharedneedle appears in every copy\n"
    _write(root, "corpus-import/origin.md", text)
    _write(base, "first/copy_a.md", text)
    _write(base, "first/copy_b.md", text)
    _write(base, "second/copy_c.md", text)
    _write(base, "second/only_here.md", "secondneedle\n")
    _write(base, "first/unique.md", "uniqueneedle\n")
    _write(base, "second/unique_copy.md", "uniqueneedle\n")
    with DiscoveryIndex(root) as index:
        meta = index.build()
        hits = _passages(index, "sharedneedle")
        assert [hit["path"] for hit in hits] == ["corpus-import/origin.md"]
        assert hits[0]["aliases"] == [
            "ext:first/copy_a.md",
            "ext:first/copy_b.md",
            "ext:second/copy_c.md",
        ]
        unique = _passages(index, "uniqueneedle")
        assert [hit["path"] for hit in unique] == ["ext:first/unique.md"]
        assert unique[0]["aliases"] == ["ext:second/unique_copy.md"]
        sha = hits[0]["source_sha256"]
        assert meta["aliases"][sha] == hits[0]["aliases"]
        assert meta["alias_count"] == 4
        rows = {row["label"]: row for row in meta["external_roots"]}
        assert (rows["first"]["files"], rows["first"]["sources"], rows["first"]["aliases"]) == (
            3,
            1,
            2,
        )
        assert (
            rows["second"]["files"],
            rows["second"]["sources"],
            rows["second"]["aliases"],
        ) == (3, 1, 2)
        assert meta["source_count"] == 3


def test_external_disabled_and_absent_roots_are_reported_not_failures(tmp_path, monkeypatch):
    root, base = _external(
        tmp_path,
        monkeypatch,
        [
            {"label": "gone", "path": "does-not-exist", "tier": 1},
            {"label": "off", "path": "off", "tier": 3, "enabled": False},
            {"label": "here", "path": "here", "tier": 1},
        ],
    )
    _write(base, "off/secret.md", "disabledneedle\n")
    _write(base, "here/note.md", "presentneedle\n")
    with DiscoveryIndex(root) as index:
        meta = index.build()
        assert index.search("disabledneedle") == []
        assert _passages(index, "presentneedle")
        rows = {row["label"]: row for row in meta["external_roots"]}
        assert rows["gone"]["skipped"] == "absent" and rows["gone"]["present"] is False
        assert rows["off"]["skipped"] == "disabled" and rows["off"]["present"] is True
        assert rows["here"]["skipped"] is None
        assert meta["settings"]["external_roots"] == ["here"]


def test_external_exclusion_globs_names_depth_and_nested_checkouts(tmp_path, monkeypatch):
    root, base = _external(
        tmp_path,
        monkeypatch,
        [
            {"label": "arc", "path": "arc", "tier": 2, "exclude": ["mirror/**", "*.draft.md"]},
            {"label": "top", "path": ".", "tier": 1, "max_depth": 0},
        ],
        exclude_names=["cache-*"],
        exclude=["arc/global-skip/**", "junk/**"],
    )
    for relative in (
        "arc/keep/a.md",
        "arc/mirror/b.md",
        "arc/c.draft.md",
        "arc/global-skip/d.md",
        "arc/cache-1/e.md",
        "arc/__pycache__/f.md",
        "arc/nested/g.md",
        "top.md",
        "junk/h.md",
        "deeper/i.md",
    ):
        _write(base, relative, f"needle {relative}\n")
    (base / "arc/nested/.git").mkdir()
    with DiscoveryIndex(root) as index:
        meta = index.build()
        paths = sorted(hit["path"] for hit in _passages(index, "needle"))
        assert paths == ["ext:arc/keep/a.md", "ext:top/top.md"]
        reasons = {row["path"]: row["reason"] for row in meta["source_exclusions"]}
        assert reasons["ext:arc/mirror"] == "scope_exclusion"
        assert reasons["ext:arc/c.draft.md"] == "scope_exclusion"
        assert reasons["ext:arc/global-skip"] == "scope_exclusion"
        assert reasons["ext:arc/cache-1"] == "excluded_directory"
        assert reasons["ext:arc/__pycache__"] == "excluded_directory"
        assert reasons["ext:arc/nested"] == "git_checkout"
        assert reasons["ext:top/deeper"] == "depth_limit"
        assert reasons["ext:top/junk"] == "depth_limit"
        assert reasons["ext:top/arc"] == "depth_limit"


def test_external_paths_inside_checkout_or_protected_subtrees_are_refused(tmp_path, monkeypatch):
    root, base = _external(
        tmp_path,
        monkeypatch,
        [
            {"label": "self", "path": "repo", "tier": 1},
            {"label": "ledger", "path": "REPO/ledger", "tier": 1},
            {"label": "around", "path": "around", "tier": 1},
        ],
    )
    # With the base at tmp_path the checkout itself is "repo"; REPO/ledger is protected.
    _write(base, "REPO/ledger/results.md", "ledgerneedle\n")
    _write(base, "REPO/index/claims.md", "indexneedle\n")
    _write(base, "around/ok.md", "aroundneedle\n")
    monkeypatch.setenv("WORKHOUSE_DISCOVERY_BASE", str(tmp_path))
    with DiscoveryIndex(root) as index:
        meta = index.build()
        rows = {row["label"]: row for row in meta["external_roots"]}
        assert rows["self"]["skipped"] == "unsafe_path"
        assert index.search("ledgerneedle") == [] and index.search("indexneedle") == []
        assert rows["ledger"]["skipped"] in ("unsafe_path", "absent")
    monkeypatch.setenv("WORKHOUSE_DISCOVERY_BASE", str(base))
    with DiscoveryIndex(root) as index:
        meta = index.build()
        rows = {row["label"]: row for row in meta["external_roots"]}
        assert rows["ledger"]["skipped"] == "unsafe_path"
        assert index.search("ledgerneedle") == []
        assert _passages(index, "aroundneedle")


def test_external_junction_or_symlink_inside_root_is_refused(tmp_path, monkeypatch):
    from test_discovery_scope import make_junction, make_symlink

    root, base = _external(tmp_path, monkeypatch, [{"label": "ws", "path": "ws-root", "tier": 1}])
    target = tmp_path / "elsewhere"
    _write(target, "hidden.md", "linkedneedle\n")
    _write(base, "ws-root/plain.md", "plainneedle\n")
    link = base / "ws-root/link"
    if not (make_junction(link, target) or make_symlink(link, target)):
        pytest.skip("host cannot create junctions or symlinks")
    file_link = base / "ws-root/file-link.md"
    file_link_made = make_symlink(file_link, target / "hidden.md")
    with DiscoveryIndex(root) as index:
        meta = index.build()
        assert index.search("linkedneedle") == []
        assert _passages(index, "plainneedle")
        reasons = {row["path"]: row["reason"] for row in meta["source_exclusions"]}
        assert reasons["ext:ws/link"] == "reparse_point"
        if file_link_made:
            assert reasons["ext:ws/file-link.md"] == "reparse_point"


def test_external_freshness_is_stat_based_between_builds(tmp_path, monkeypatch):
    root, base = _external(tmp_path, monkeypatch, [{"label": "ws", "path": "ws-root", "tier": 1}])
    external = _write(base, "ws-root/note.md", "alpha external\n")
    with DiscoveryIndex(root) as index:
        first = index.build()
        stamp = external.stat()
        # A same-size, same-mtime edit is invisible to the stat policy until rebuild.
        external.write_text("gamma external\n", encoding="utf-8", newline="")
        os.utime(external, ns=(stamp.st_atime_ns, stamp.st_mtime_ns))
        rechecked = index.metadata()
        assert rechecked["freshness"] == "matched"
        assert rechecked["freshness_observation"].endswith("rehashed on change")
        # A changed stat rehashes that file and reports the edit.
        os.utime(external, ns=(stamp.st_atime_ns, stamp.st_mtime_ns + 1_000_000_000))
        stale = index.metadata()
        assert stale["freshness"] == "stale"
        second = index.build()
        assert second["fingerprint"] != first["fingerprint"]
        assert index.search("alpha") == [] and _passages(index, "gamma")
        # A new external file is seen without any prior stat record.
        _write(base, "ws-root/new.md", "delta external\n")
        assert index.metadata()["freshness"] == "stale"


def test_external_scope_changes_and_labels_enter_the_fingerprint(tmp_path, monkeypatch):
    import yaml

    from workhouse import discovery_scope as S

    root, base = _external(
        tmp_path,
        monkeypatch,
        [
            {"label": "a", "path": "a", "tier": 1},
            {"label": "b", "path": "b", "tier": 2},
        ],
    )
    _write(base, "a/x.md", "needle a\n")
    _write(base, "b/y.md", "needle b\n")
    with DiscoveryIndex(root) as index:
        first = index.build()
        assert first["settings"]["external_roots"] == ["a", "b"]
        declared = first["settings"]["external_scope"]
        assert [row["label"] for row in declared["roots"]] == ["a", "b"]
        assert index.metadata()["freshness"] == "matched"
        local = root / S.LOCAL_PATH
        local.parent.mkdir(parents=True, exist_ok=True)
        local.write_text(
            yaml.safe_dump({"schema": S.LOCAL_SCHEMA, "disable": ["b"]}), encoding="utf-8"
        )
        assert index.metadata()["freshness"] == "stale"
        second = index.build()
        assert second["fingerprint"] != first["fingerprint"]
        assert second["settings"]["external_roots"] == ["a"]
        assert index.search("needle b") == [] or all(
            hit["path"] != "ext:b/y.md" for hit in index.search("needle b")
        )
        assert second["external_scope"]["local_disabled"] == ["b"]


def test_malformed_scope_file_is_an_explicit_error(tmp_path, monkeypatch):
    root, _base = _external(tmp_path, monkeypatch, [{"label": "a", "path": "a", "tier": 1}])
    _write(root, "graph-tasks/discovery/scope.yaml", "schema: workhouse-discovery-scope/v1\n")
    with DiscoveryIndex(root) as index, pytest.raises(ValueError, match="version"):
        index.build()


def test_external_non_utf8_and_oversized_files_are_excluded(tmp_path, monkeypatch):
    from workhouse import discovery_index as module

    root, base = _external(tmp_path, monkeypatch, [{"label": "ws", "path": "ws-root", "tier": 1}])
    _write(base, "ws-root/bad.md", "x").write_bytes(b"\xff\xfe\x00")
    _write(base, "ws-root/big.md", "x" * 32)
    _write(base, "ws-root/ok.md", "okneedle\n")
    monkeypatch.setattr(module, "MAX_SOURCE_BYTES", 16)
    with DiscoveryIndex(root) as index:
        meta = index.build()
        reasons = {row["path"]: row["reason"] for row in meta["source_exclusions"]}
        assert reasons["ext:ws/bad.md"] == "non_utf8"
        assert reasons["ext:ws/big.md"] == "size_limit"
        assert _passages(index, "okneedle")


def test_lost_math_opener_does_not_protect_the_rest_of_the_document():
    from workhouse.discovery_index import MAX_PROTECTED_LINES, protected_blocks

    lines = ["prose\n"] * 5 + ["\\end{cases}$$\n"] + ["more prose\n"] * 300
    assert protected_blocks(lines) == []
    unclosed = ["$$\n"] + ["x\n"] * 400
    assert protected_blocks(unclosed) == []
    long_closed = ["$$\n"] + ["x\n"] * (MAX_PROTECTED_LINES + 5) + ["$$\n"]
    assert protected_blocks(long_closed) == []
    short_closed = ["$$\n"] + ["x\n"] * 10 + ["$$\n"]
    assert protected_blocks(short_closed) == [(0, 11)]
