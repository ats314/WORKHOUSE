"""The prose corpus is evidence: it must be present and must not drift silently."""

import hashlib
from pathlib import Path

THEORY = Path(__file__).resolve().parents[1] / "theory"

# Recorded when the documents were loaded into the repository. A change here is
# not a failure of the theory, but it must be a deliberate, reviewed event.
#: The current stack. Superseded documents live in theory/superseded/ and are
#: pinned too, so drift in an archived document is still caught.
CURRENT = {
    "MASTER_THEORY_UNIFIED_2026-08-20_v3.md",
    "GLUEBALL_DETAILED_FORMULA_2026-08-20_v3.1.md",
    "GLUEBALL_SOURCE_CONSOLIDATION_GUIDE_2026-08-20_v3.md",
    "GLUEBALL_CANONICAL_SOURCE_MANIFEST_2026-08-20_v3.csv",
    "README.md",
}
SUPERSEDED = {
    "superseded/MASTER_THEORY.md",
    "superseded/MASTER_THEORY_UNIFIED_2026-08-20_v2.md",
}
EXPECTED = CURRENT | SUPERSEDED


def test_current_stack_present():
    names = {p.name for p in THEORY.glob("*.md")} | {p.name for p in THEORY.glob("*.csv")}
    assert names == CURRENT


def test_superseded_documents_are_quarantined_not_deleted():
    """Kept for the audit trail; never readable as current."""
    names = {f"superseded/{p.name}" for p in (THEORY / "superseded").glob("*.md")}
    assert names == SUPERSEDED


def test_the_truncated_unified_v2_is_not_in_the_current_stack():
    """v2 stops mid-structure at 2.5; v3 carries the governing register."""
    v2 = THEORY / "superseded" / "MASTER_THEORY_UNIFIED_2026-08-20_v2.md"
    v3 = THEORY / "MASTER_THEORY_UNIFIED_2026-08-20_v3.md"
    assert v2.exists() and v3.exists()
    assert len(v3.read_text().splitlines()) > 5 * len(v2.read_text().splitlines())
    assert "Governing contradiction and errata register" in v3.read_text()


def test_documents_are_non_trivial():
    for p in THEORY.glob("*.md"):
        if p.name == "README.md":
            continue
        assert p.stat().st_size > 5000, f"{p.name} looks truncated"


def test_manifest_matches_contents():
    """SHA-256 manifest, so provenance is checkable the way the corpus demands."""
    manifest = THEORY / "SHA256SUMS"
    assert manifest.exists(), "theory/SHA256SUMS is missing"
    recorded = {}
    for line in manifest.read_text().splitlines():
        if line.strip() and not line.startswith("#"):
            digest, name = line.split(maxsplit=1)
            recorded[name.strip()] = digest
    assert set(recorded) == EXPECTED
    for name, digest in recorded.items():
        actual = hashlib.sha256((THEORY / name).read_bytes()).hexdigest()
        assert actual == digest, f"{name} changed: {actual} != {digest}"
