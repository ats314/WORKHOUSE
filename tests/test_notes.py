"""The notes register must lose nothing and take nobody's word for anything.

Every rule exercised here exists for a recorded failure mode, and each test
names it. If one of these rules ever seems stupid, argue with the failure
mode it cites — and if it no longer earns its place, remove rule and test
together, visibly.
"""

import hashlib
import json

import pytest

from workhouse import notes


@pytest.fixture
def archive(tmp_path):
    root = tmp_path / "RESEARCH"
    (root / "drafts").mkdir(parents=True)
    (root / "hs_note.md").write_text(
        "Combes-Thomas bound with d_3 = -109151/249696 and b_3 = 1975/124848.\n"
    )
    (root / "drafts" / "hs_note_copy.md").write_text(
        "Combes-Thomas bound with d_3 = -109151/249696 and b_3 = 1975/124848.\n"
    )
    (root / "inert.txt").write_text("meeting notes, no numbers of interest\n")
    return root


@pytest.fixture
def registry(archive, tmp_path):
    """A declared archive, inventoried into a tmp notes dir."""
    reg = notes.Notes(
        archives=[{"id": "TEST_ARCHIVE", "description": "fixture archive", "source": "tmp_path"}],
        reviews=[],
    )
    notes.write_manifest(archive, "TEST_ARCHIVE", reg, notes_dir=tmp_path / "notes")
    manifest = tmp_path / "notes" / "TEST_ARCHIVE.jsonl"
    reg.manifests["TEST_ARCHIVE"] = [json.loads(line) for line in manifest.read_text().splitlines()]
    return reg


def _digest_of(registry, name):
    for row in registry.manifests["TEST_ARCHIVE"]:
        if any(name in p for p in row["paths"]):
            return row["digest"]
    raise KeyError(name)


def test_manifest_deduplicates_by_digest(registry):
    """3 files, 2 unique contents: the copy is the same row, not a second one."""
    rows = registry.manifests["TEST_ARCHIVE"]
    assert len(rows) == 2
    dup_row = next(r for r in rows if len(r["paths"]) == 2)
    assert dup_row["paths"] == ["drafts/hs_note_copy.md", "hs_note.md"]


def test_scan_refuses_an_undeclared_archive(archive, tmp_path):
    """A manifest nothing can review is an orphan; declaring comes first."""
    reg = notes.Notes(archives=[], reviews=[])
    with pytest.raises(KeyError):
        notes.write_manifest(archive, "NOT_DECLARED", reg, notes_dir=tmp_path / "notes")


def test_queue_ranks_coefficient_bearing_first_and_review_removes(registry):
    pending = notes.queue(registry)
    assert len(pending) == 2
    assert "hs_note" in pending[0][1]["paths"][0]  # carries d_3 and b_3

    registry.reviews.append(
        {
            "digest": _digest_of(registry, "hs_note"),
            "archive": "TEST_ARCHIVE",
            "verdict": "set-aside",
            "reason": "fixture",
        }
    )
    remaining = notes.queue(registry)
    assert len(remaining) == 1
    assert "inert" in remaining[0][1]["paths"][0]


def _review(registry, **overrides):
    entry = {
        "digest": _digest_of(registry, "hs_note"),
        "archive": "TEST_ARCHIVE",
        "verdict": "set-aside",
        "reason": "a recorded reason",
    }
    entry.update(overrides)
    registry.reviews.append(entry)
    return notes.validate(registry)


def test_a_sound_review_validates_clean(registry, tmp_path):
    assert _review(registry) == []


def test_an_unknown_verdict_is_rejected(registry):
    problems = _review(registry, verdict="looks-fine")
    assert any("unknown verdict" in p for p in problems)


def test_a_verdict_without_a_reason_is_decoration(registry):
    """Same failure mode as a unifying candidate without a falsifier."""
    problems = _review(registry, reason="  ")
    assert any("no reason" in p for p in problems)


def test_a_review_of_a_digest_not_in_the_manifest_is_caught(registry):
    problems = _review(registry, digest="ab" * 32)
    assert any("not in TEST_ARCHIVE's manifest" in p for p in problems)


def test_one_digest_gets_one_verdict(registry):
    _review(registry)
    problems = _review(registry, reason="second opinion")
    assert any("reviewed twice" in p for p in problems)


def test_an_import_must_hash_to_its_digest(registry, tmp_path):
    """ "Imported" is a claim; the bytes are the check."""
    (tmp_path / "landed.md").write_text("different bytes\n")
    _review(registry, verdict="import", imported_to="landed.md")
    problems = notes.validate(registry, root=tmp_path)
    assert any("does not hash to the digest" in p for p in problems)


def test_a_verbatim_import_validates(registry, tmp_path, archive):
    data = (archive / "hs_note.md").read_bytes()
    (tmp_path / "landed.md").write_bytes(data)
    assert hashlib.sha256(data).hexdigest() == _digest_of(registry, "hs_note")
    _review(registry, verdict="import", imported_to="landed.md")
    assert notes.validate(registry, root=tmp_path) == []


def test_an_extract_must_name_what_it_entered(registry):
    problems = _review(registry, verdict="extract")
    assert any("names no bears_on" in p for p in problems)


def test_bears_on_must_resolve(registry):
    """An edge to nothing is decoration — the literature layer's rule, reused."""
    problems = _review(registry, verdict="extract", bears_on=["G14", "NOT_A_CLAIM"])
    assert any("unknown target 'NOT_A_CLAIM'" in p for p in problems)
    assert not any("'G14'" in p for p in problems)


def test_superseded_needs_its_successor_in_a_manifest(registry):
    problems = _review(registry, verdict="superseded", superseded_by="cd" * 32)
    assert any("in no manifest" in p for p in problems)

    registry.reviews.clear()
    successor = _digest_of(registry, "inert")
    _review(registry, verdict="superseded", superseded_by=successor)
    assert notes.validate(registry) == []


def test_a_review_against_an_uninventoried_archive_is_premature(registry):
    registry.archives.append(
        {"id": "GHOST", "description": "declared, never scanned", "source": "nowhere"}
    )
    problems = _review(registry, archive="GHOST")
    assert any("has no manifest" in p for p in problems)


def test_the_checked_in_register_is_sound():
    """The real ledger/notes.yaml must always load and validate clean."""
    registry = notes.load()
    assert notes.validate(registry) == []
    assert "RESEARCH_2026-08" in registry.archive_ids
