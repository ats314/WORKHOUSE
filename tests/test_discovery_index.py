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
