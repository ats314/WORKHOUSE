"""The library catalogue must stay machine-usable.

The catalogue is T3 metadata, not evidence — but the intake path leans on
its digests and identifiers, so a malformed row is a silently broken
acquisition, the same failure mode as an unpinnable citation.
"""

import csv
from pathlib import Path

import pytest

LIBRARY = Path(__file__).resolve().parents[1] / "literature" / "library"
VOLUMES = [("paper_manifest.csv", 99), ("volume2/paper_manifest.csv", 161)]
TIERS = {"core", "emerging", "frontier"}
HEX = set("0123456789abcdef")


def _rows(rel):
    with open(LIBRARY / rel, encoding="utf-8-sig") as fh:
        return list(csv.DictReader(fh))


@pytest.mark.parametrize(("rel", "expected"), VOLUMES)
def test_manifest_loads_with_expected_shape(rel, expected):
    rows = _rows(rel)
    assert len(rows) == expected
    for field in ("tier", "title", "sha256", "local_file", "year"):
        assert field in rows[0]


@pytest.mark.parametrize(("rel", "_expected"), VOLUMES)
def test_every_row_is_identifiable_and_pinnable(rel, _expected):
    """Each row needs a digest and at least one resolvable identifier."""
    for r in _rows(rel):
        assert r["tier"] in TIERS, r["title"]
        assert len(r["sha256"]) == 64 and set(r["sha256"]) <= HEX, r["title"]
        assert r["arxiv_id"] or r["doi"] or r["inspire_recid"], (
            f"unpinnable library row: {r['title']!r}"
        )


def test_digests_are_unique_across_all_volumes():
    """Volume 2's declared zero-overlap audit, held as a check forever."""
    digests = [r["sha256"] for rel, _n in VOLUMES for r in _rows(rel)]
    assert len(digests) == len(set(digests))
