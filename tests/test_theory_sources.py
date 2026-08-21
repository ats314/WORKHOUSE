"""The prose corpus is evidence: it must be present and must not drift silently."""

import hashlib
from pathlib import Path

THEORY = Path(__file__).resolve().parents[1] / "theory"

# Recorded when the documents were loaded into the repository. A change here is
# not a failure of the theory, but it must be a deliberate, reviewed event.
EXPECTED = {
    "MASTER_THEORY.md",
    "MASTER_THEORY_UNIFIED_2026-08-20_v2.md",
    "GLUEBALL_DETAILED_FORMULA_2026-08-20_v3.1.md",
}


def test_all_three_documents_present():
    assert {p.name for p in THEORY.glob("*.md")} == EXPECTED


def test_documents_are_non_trivial():
    for p in THEORY.glob("*.md"):
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
