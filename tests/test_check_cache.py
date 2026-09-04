"""The per-check cache is keyed on every input and never serves `verify`."""

import json

from workhouse import check_cache as CC
from workhouse.invariants._core import Result, Suite


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
