"""The library catalogue must stay machine-usable.

The catalogue is T3 metadata, not evidence — but the intake path leans on
its digests and identifiers, so a malformed row is a silently broken
acquisition, the same failure mode as an unpinnable citation.
"""

import csv
from pathlib import Path

LIBRARY = Path(__file__).resolve().parents[1] / "literature" / "library"
TIERS = {"core", "emerging", "frontier"}
HEX = set("0123456789abcdef")


def _rows():
    with open(LIBRARY / "paper_manifest.csv", encoding="utf-8-sig") as fh:
        return list(csv.DictReader(fh))


def test_manifest_loads_with_expected_shape():
    rows = _rows()
    assert len(rows) == 99
    for field in ("tier", "title", "sha256", "local_file", "year"):
        assert field in rows[0]


def test_every_row_is_identifiable_and_pinnable():
    """Each row needs a digest and at least one resolvable identifier."""
    for r in _rows():
        assert r["tier"] in TIERS, r["title"]
        assert len(r["sha256"]) == 64 and set(r["sha256"]) <= HEX, r["title"]
        assert r["arxiv_id"] or r["doi"] or r["inspire_recid"], (
            f"unpinnable library row: {r['title']!r}"
        )


def test_digests_are_unique():
    digests = [r["sha256"] for r in _rows()]
    assert len(digests) == len(set(digests))
