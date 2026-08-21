"""The prose corpus is evidence: it must be present and must not drift silently."""

import hashlib
import re
from pathlib import Path

THEORY = Path(__file__).resolve().parents[1] / "theory"

# Recorded when the documents were loaded into the repository. A change here is
# not a failure of the theory, but it must be a deliberate, reviewed event.
#: The current stack. Superseded documents live in theory/superseded/ and are
#: pinned too, so drift in an archived document is still caught.
CURRENT = {
    "MASTER_THEORY_UNIFIED_2026-08-20_v4_3.md",
    # Not superseded by v4.3: the coefficient appendix is still at v3.1.
    "GLUEBALL_DETAILED_FORMULA_2026-08-20_v3.1.md",
    "GLUEBALL_SOURCE_CONSOLIDATION_GUIDE_2026-08-20_v4_3.md",
    "GLUEBALL_CANONICAL_SOURCE_MANIFEST_2026-08-20_v4_3.csv",
    "README.md",
}
#: Upstream's own map of the tree this corpus was extracted from. It names
#: directories that do not exist here; it is kept so a cited path resolves.
GOVERNANCE = {
    "governance/INDEX.md",
    "governance/MAN_GOV_all_theory_local_path_index_v4_3.csv",
}
SUPERSEDED = {
    "superseded/MASTER_THEORY.md",
    "superseded/MASTER_THEORY_UNIFIED_2026-08-20_v2.md",
    "superseded/MASTER_THEORY_UNIFIED_2026-08-20_v3.md",
    "superseded/GLUEBALL_SOURCE_CONSOLIDATION_GUIDE_2026-08-20_v3.md",
    "superseded/GLUEBALL_CANONICAL_SOURCE_MANIFEST_2026-08-20_v3.csv",
}
EXPECTED = CURRENT | GOVERNANCE | SUPERSEDED

MASTER = THEORY / "MASTER_THEORY_UNIFIED_2026-08-20_v4_3.md"
MASTER_V3 = THEORY / "superseded" / "MASTER_THEORY_UNIFIED_2026-08-20_v3.md"


def _register(document: Path) -> list[str]:
    """The numbered items of §14, one string each, whitespace-normalized.

    Numbering is compared across versions, so the item text is returned without
    its leading number: v3's item 14 is v4.3's item 23 with identical text.
    """
    body = document.read_text()
    section = re.search(
        r"^## 14\. Governing contradiction and errata register\n(.*?)^---$",
        body,
        re.MULTILINE | re.DOTALL,
    )
    assert section, f"{document.name} has no §14 register"
    items = re.split(r"^\d+\. ", section.group(1), flags=re.MULTILINE)[1:]
    return [" ".join(item.split()) for item in items]


def test_current_stack_present():
    names = {p.name for p in THEORY.glob("*.md")} | {p.name for p in THEORY.glob("*.csv")}
    assert names == CURRENT


def test_superseded_documents_are_quarantined_not_deleted():
    """Kept for the audit trail; never readable as current."""
    directory = THEORY / "superseded"
    names = {f"superseded/{p.name}" for p in directory.iterdir() if p.is_file()}
    assert names == SUPERSEDED


def test_upstream_governance_is_present_and_separate():
    directory = THEORY / "governance"
    names = {f"governance/{p.name}" for p in directory.iterdir() if p.is_file()}
    assert names == GOVERNANCE


def test_v3_is_quarantined_because_upstream_says_so():
    """The promotion is not our judgement: upstream's path index records it."""
    index = (THEORY / "governance" / "MAN_GOV_all_theory_local_path_index_v4_3.csv").read_text()
    v3 = [ln for ln in index.splitlines() if "MASTER_THEORY_UNIFIED_2026-08-20_v3.md" in ln]
    assert v3, "upstream index does not mention v3 at all"
    assert all("quarantine_only" in ln for ln in v3), v3


def test_the_truncated_unified_v2_is_not_the_governing_document():
    """v2 stops mid-structure at §2.5; v4.3 carries the governing register."""
    v2 = THEORY / "superseded" / "MASTER_THEORY_UNIFIED_2026-08-20_v2.md"
    assert v2.exists() and MASTER.exists()
    assert len(MASTER.read_text().splitlines()) > 5 * len(v2.read_text().splitlines())
    assert "Governing contradiction and errata register" in MASTER.read_text()


def test_v4_3_register_extends_v3_without_retracting_anything():
    """FINDING-shaped check on the promotion itself.

    A version bump on an evidence document is only safe if the earlier register
    survives inside it. Items 1-13 must be text-identical, and v3's final item
    ("Scope") must still be present -- v4.3 renumbers it to 23 rather than
    dropping it. If a future version really does retract an item, this test
    fails and the retraction gets recorded instead of vanishing.
    """
    old, new = _register(MASTER_V3), _register(MASTER)
    assert len(old) == 14 and len(new) == 23, (len(old), len(new))
    assert old[:13] == new[:13]
    assert old[13] == new[22], "v3's Scope item is not v4.3's item 23"
    assert set(old) <= set(new)


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
