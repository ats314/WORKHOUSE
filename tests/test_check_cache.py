"""The per-check cache is keyed on every input and never serves `verify`."""

import errno
import json
import os
from contextvars import Context
from pathlib import Path

import pytest

from workhouse import check_cache as CC
from workhouse.invariants._core import Result, Suite


def test_walk_matches_legacy_file_selection_and_global_order(tmp_path, monkeypatch):
    monkeypatch.setattr(CC, "ROOT", tmp_path)
    for relative in (
        "tree/z.txt",
        "tree/alpha/first.txt",
        "tree/alpha-z.txt",
        "tree/a.txt",
        "tree/nested/leaf.txt",
        "tree/build.txt",
        "tree/.github/workflow.yml",
        "tree/.lake/deep/cache.olean",
        "tree/.git/config",
        "tree/build/generated.txt",
        "tree/nested/imported/source.py",
        "tree/notes/.venv/hidden.py",
        "tree/__pycache__/cached.pyc",
        "tree/files/imported",
    ):
        target = tmp_path / relative
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(relative, encoding="utf-8")

    def legacy_walk(relative):
        target = tmp_path / relative
        if target.is_file():
            return [target]
        if not target.is_dir():
            return []
        return [
            path
            for path in sorted(target.rglob("*"))
            if path.is_file() and not any(part in CC.SKIP_PARTS for part in path.parts)
        ]

    for relative in ("tree", "tree/.lake", "tree/files/imported", "missing"):
        assert list(CC._walk(relative)) == legacy_walk(relative)
    # Direct file inputs retain their historical exemption from tree exclusions.
    assert list(CC._walk("tree/files/imported")) == [tmp_path / "tree/files/imported"]


def test_walk_prunes_excluded_directories_before_descent(tmp_path, monkeypatch):
    monkeypatch.setattr(CC, "ROOT", tmp_path)
    for relative in (
        "tree/visible/leaf.txt",
        *(f"tree/{part}/deep/hidden.txt" for part in CC.SKIP_PARTS),
        "tree/visible/build/deep/hidden.txt",
    ):
        target = tmp_path / relative
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(relative, encoding="utf-8")
    original_walk = CC.os.walk
    visited = []

    def observed_walk(*args, **kwargs):
        for directory, directories, filenames in original_walk(*args, **kwargs):
            visited.append(Path(directory))
            yield directory, directories, filenames

    monkeypatch.setattr(CC.os, "walk", observed_walk)
    assert list(CC._walk("tree")) == [tmp_path / "tree/visible/leaf.txt"]
    assert visited == [tmp_path / "tree", tmp_path / "tree/visible"]


def test_walk_propagates_unexpected_scan_errors(tmp_path, monkeypatch):
    monkeypatch.setattr(CC, "ROOT", tmp_path)
    (tmp_path / "tree").mkdir()

    def fail_scandir(path):
        raise OSError(errno.EIO, "injected scan failure", str(path))

    monkeypatch.setattr(CC.os, "scandir", fail_scandir)
    with pytest.raises(OSError, match="injected scan failure") as failure:
        list(CC._walk("tree"))
    assert failure.value.errno == errno.EIO


def test_walk_preserves_permission_error_skips(tmp_path, monkeypatch):
    monkeypatch.setattr(CC, "ROOT", tmp_path)
    (tmp_path / "tree").mkdir()

    def fail_scandir(path):
        raise PermissionError(errno.EACCES, "injected permission failure", str(path))

    monkeypatch.setattr(CC.os, "scandir", fail_scandir)
    assert list(CC._walk("tree")) == []


def test_fingerprint_covers_the_input_trees_and_changes_when_one_does(tmp_path, monkeypatch):
    before = CC.fingerprint()
    # the fingerprint is over path, size and mtime; touching a ledger file moves it
    target = CC.ROOT / "ledger" / "documents.yaml"
    st = target.stat()
    try:
        import os

        os.utime(target, ns=(st.st_atime_ns, st.st_mtime_ns + 1_000_000))
        after = CC.fingerprint()
    finally:
        os.utime(target, ns=(st.st_atime_ns, st.st_mtime_ns))
    assert before != after
    assert CC.fingerprint() == before


def test_index_reading_checks_are_keyed_on_the_index_too():
    cache = CC.CheckCache()
    plain = cache.key("s", "n", "return True, ''")
    reads = cache.key("s", "n", "GRAPH.read_text()")
    assert plain != reads
    # and the key is stable for the same inputs
    assert cache.key("s", "n", "return True, ''") == plain


def test_round_trip_and_hit_counting(tmp_path, monkeypatch):
    monkeypatch.setenv("XDG_CACHE_HOME", str(tmp_path))
    monkeypatch.delenv("WORKHOUSE_NO_CACHE", raising=False)
    cache = CC.CheckCache()
    result = Result("n", True, "d", "sec", 1, 3, "src/x.py:3", {"A": "1/2"}, ("m",))
    key = cache.key("suite", "n", "src")
    assert cache.get(key) is None and cache.misses == 1
    cache.put(key, result)
    hit = cache.get(key)
    assert hit is not None and cache.hits == 1
    assert hit["passed"] is True and hit["yields"] == {"A": "1/2"}
    assert json.dumps(hit)  # plain types only


def test_a_suite_run_with_a_cache_skips_the_body_on_a_hit(tmp_path, monkeypatch):
    monkeypatch.setenv("XDG_CACHE_HOME", str(tmp_path))
    monkeypatch.delenv("WORKHOUSE_NO_CACHE", raising=False)
    suite = Suite("scratch cache")
    calls = []

    @suite.check("counts its calls")
    def _():
        calls.append(1)
        return True, "ran"

    cache = CC.CheckCache()
    first = suite.run(cache=cache)
    second = suite.run(cache=cache)
    assert len(calls) == 1
    assert first[0].detail == second[0].detail == "ran"
    # without a cache the body runs again: this is the `verify` path
    suite.run()
    assert len(calls) == 2


def test_no_cache_env_disables_it(tmp_path, monkeypatch):
    monkeypatch.setenv("XDG_CACHE_HOME", str(tmp_path))
    monkeypatch.setenv("WORKHOUSE_NO_CACHE", "1")
    cache = CC.CheckCache()
    assert not cache.on
    assert cache.get("anything") is None


def test_verify_never_passes_a_cache():
    """`workhouse verify` is the promise to re-derive; read the code, not a claim."""
    import inspect

    from workhouse import cli

    source = inspect.getsource(cli._verify)
    assert "cache" not in source


def test_standalone_bridge_implementation_change_invalidates_cached_check(tmp_path, monkeypatch):
    """The registered adapters execute these scripts outside the src tree."""
    monkeypatch.setattr(CC, "ROOT", tmp_path)
    for relative in (
        "scripts/verify_source_current_bridges.py",
        "scripts/verify_theory_geometry_bridges.py",
    ):
        target = tmp_path / relative
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text("# original computation\n", encoding="utf-8")
        before = CC.fingerprint()
        target.write_text("# changed mathematical computation\n", encoding="utf-8")
        assert CC.fingerprint() != before


def test_observed_collection_reuses_by_content_and_reports_check_identity(tmp_path, monkeypatch):
    monkeypatch.setattr(CC, "ROOT", tmp_path)
    monkeypatch.setenv("XDG_CACHE_HOME", str(tmp_path / "cache"))
    monkeypatch.delenv("WORKHOUSE_NO_CACHE", raising=False)
    suite = Suite("observed suite")
    calls = []

    @suite.check("observed check")
    def _():
        calls.append(1)
        return True, "executed"

    with CC.observe(content_key="inputs-one") as first:
        suite.run(cache=CC.CheckCache())
    with CC.observe(content_key="inputs-one") as reused:
        suite.run(cache=CC.CheckCache())
    with CC.observe(content_key="inputs-two") as changed:
        suite.run(cache=CC.CheckCache())
    assert len(calls) == 2
    assert first["reused"] == changed["reused"] == []
    assert reused["reused"] == [("observed suite", "observed check")]


def test_fresh_observation_bypasses_cache_reads_and_writes(tmp_path, monkeypatch):
    monkeypatch.setattr(CC, "ROOT", tmp_path)
    monkeypatch.setenv("XDG_CACHE_HOME", str(tmp_path / "cache"))
    monkeypatch.delenv("WORKHOUSE_NO_CACHE", raising=False)
    suite = Suite("fresh suite")
    calls = []

    @suite.check("fresh check")
    def _():
        calls.append(1)
        return True, f"execution {len(calls)}"

    with CC.observe(content_key="same-inputs"):
        suite.run(cache=CC.CheckCache())
    cached_bytes = {path: path.read_bytes() for path in CC._cache_dir().glob("*")}
    with CC.observe(content_key="same-inputs", fresh=True) as fresh:
        cache = CC.CheckCache()
        assert not cache.on
        assert suite.run(cache=cache)[0].detail == "execution 2"
        assert cache.get("any-key") is None
        cache.put("another-key", Result("n", True, "d", "s", 1, 0, "src.py"))
    assert fresh["reused"] == []
    assert {path: path.read_bytes() for path in CC._cache_dir().glob("*")} == cached_bytes
    assert "WORKHOUSE_NO_CACHE" not in os.environ
    with CC.observe(content_key="same-inputs") as reused:
        assert suite.run(cache=CC.CheckCache())[0].detail == "execution 1"
    assert len(calls) == 2
    assert reused["reused"] == [("fresh suite", "fresh check")]


def test_observations_restore_nested_and_exceptional_contexts():
    assert CC._OBSERVATION.get() is None
    with CC.observe(content_key="outer") as outer:
        assert Context().run(CC._OBSERVATION.get) is None
        with (
            pytest.raises(RuntimeError, match="inner failure"),
            CC.observe(content_key="inner", fresh=True) as inner,
        ):
            assert CC._OBSERVATION.get() is inner
            raise RuntimeError("inner failure")
        assert CC._OBSERVATION.get() is outer
        assert outer == {"content_key": "outer", "fresh": False, "reused": []}
    assert CC._OBSERVATION.get() is None


def test_observed_index_key_uses_bytes_even_when_size_and_mtime_match(tmp_path, monkeypatch):
    monkeypatch.setattr(CC, "ROOT", tmp_path)
    monkeypatch.delenv("WORKHOUSE_NO_CACHE", raising=False)
    index = tmp_path / "index" / "graph.jsonl"
    index.parent.mkdir()
    index.write_bytes(b"old")
    original_stat = index.stat()
    with CC.observe(content_key="stable-inputs"):
        before = CC.CheckCache()
        before_index = before.key("suite", "check", "GRAPH.read_text()")
        before_plain = before.key("suite", "check", "return True, ''")
        index.write_bytes(b"new")
        os.utime(index, ns=(original_stat.st_atime_ns, original_stat.st_mtime_ns))
        after = CC.CheckCache()
        assert after.key("suite", "check", "GRAPH.read_text()") != before_index
        assert after.key("suite", "check", "return True, ''") == before_plain


@pytest.mark.parametrize("failure_kind", ["scan", "read"])
def test_observed_index_fails_on_unreadable_data(tmp_path, monkeypatch, failure_kind):
    monkeypatch.setattr(CC, "ROOT", tmp_path)
    monkeypatch.delenv("WORKHOUSE_NO_CACHE", raising=False)
    index = tmp_path / "index"
    index.mkdir()
    graph = index / "graph.jsonl"
    graph.write_text("{}\n", encoding="utf-8")
    if failure_kind == "scan":
        original = CC.os.scandir

        def fail_scan(path):
            if Path(path) == index:
                raise PermissionError(errno.EACCES, "unreadable index directory", str(path))
            return original(path)

        monkeypatch.setattr(CC.os, "scandir", fail_scan)
    else:
        original = Path.read_bytes

        def fail_read(path):
            if path == graph:
                raise PermissionError(errno.EACCES, "unreadable index file", str(path))
            return original(path)

        monkeypatch.setattr(Path, "read_bytes", fail_read)
    with (
        CC.observe(content_key="same-inputs"),
        pytest.raises(PermissionError, match="unreadable index"),
    ):
        CC.CheckCache()
