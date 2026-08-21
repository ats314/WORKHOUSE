"""Triage must find the signal and must never touch the archive."""

import hashlib

import pytest

from workhouse import triage


@pytest.fixture
def archive(tmp_path):
    """A miniature archive with one of each thing triage should notice."""
    root = tmp_path / "archive"
    (root / "drafts").mkdir(parents=True)
    repo = triage.Path(__file__).resolve().parents[1]

    pinned = (repo / "theory" / "MASTER_THEORY.md").read_bytes()
    (root / "MASTER_THEORY.md").write_bytes(pinned)  # pinned duplicate
    (root / "drafts" / "MT_backup.md").write_bytes(pinned)  # internal duplicate
    (root / "drafts" / "note_20260612.md").write_text(
        "Y = 2\\beta/3 = 4u, and d_3 = -109151/249696 with b_3 = 1975/124848.\n"
    )
    (root / "inert.txt").write_text("no numbers of interest\n")
    (root / "denominator_only.md").write_text("the value 249696 appears alone here\n")
    return root


def test_finds_files_already_pinned(archive):
    report = triage.scan(archive)
    dups = {str(f.path): f.duplicate_of for f in report.duplicates}
    assert dups["MASTER_THEORY.md"] == "theory/MASTER_THEORY.md"
    assert dups["drafts/MT_backup.md"] == "theory/MASTER_THEORY.md"


def test_finds_duplicates_within_the_archive(archive):
    groups = triage.scan(archive).internal_duplicate_groups()
    assert len(groups) == 1
    assert {str(f.path) for f in next(iter(groups.values()))} == {
        "MASTER_THEORY.md",
        "drafts/MT_backup.md",
    }


def test_short_signatures_require_co_occurrence(archive):
    """A lone denominator is noise; numerator plus denominator is the coefficient."""
    report = triage.scan(archive)
    by_name = {str(f.path): f for f in report.files}
    assert "d_3" not in by_name["denominator_only.md"].coefficients
    assert "d_3" in by_name["drafts/note_20260612.md"].coefficients
    assert "b_3" in by_name["drafts/note_20260612.md"].coefficients


def test_detects_the_coupling_erratum(archive):
    report = triage.scan(archive)
    carriers = {str(f.path) for f in report.erratum_carriers}
    assert "drafts/note_20260612.md" in carriers
    assert "inert.txt" not in carriers


def test_superseded_hint_survives_underscores():
    """Underscore is a word character, so a naive \\bold\\b never fires."""
    assert triage.SUPERSEDED_HINTS.search(triage._normalise_name("GLUE_old_copy.md"))
    assert triage.SUPERSEDED_HINTS.search(triage._normalise_name("MASTER_THEORY_backup.md"))
    assert not triage.SUPERSEDED_HINTS.search(triage._normalise_name("MASTER_THEORY.md"))


def test_extracts_date_hint(archive):
    report = triage.scan(archive)
    by_name = {str(f.path): f for f in report.files}
    assert by_name["drafts/note_20260612.md"].date_hint == "2026-06-12"


def test_scan_never_modifies_the_archive(archive):
    """Read-only is the contract; promoting anything is a human decision."""
    before = {
        p: hashlib.sha256(p.read_bytes()).hexdigest() for p in archive.rglob("*") if p.is_file()
    }
    triage.scan(archive)
    after = {
        p: hashlib.sha256(p.read_bytes()).hexdigest() for p in archive.rglob("*") if p.is_file()
    }
    assert before == after
    assert set(before) == set(after), "triage added or removed a file"


def test_every_signature_is_specific_enough():
    for label, alternatives in triage.SIGNATURES.items():
        for alt in alternatives:
            if len(alt) == 1:
                assert len(alt[0]) >= triage.MIN_SIGNATURE_DIGITS, (
                    f"{label}: lone signature {alt[0]} is too short to be safe"
                )


def test_report_formats_without_error(archive):
    text = triage.format_report(triage.scan(archive))
    assert "ALREADY PINNED" in text and "COEFFICIENT CENSUS" in text
