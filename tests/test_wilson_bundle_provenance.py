"""Preserved Wilson packages remain complete after their notes are relocated.

The integration manifest records the ZIP comparison made at import. Tests
do not require a maintainer's external ZIP: the immutable package checksum
file independently authenticates each imported destination, and the registry
test ensures that both received bundles name their native gap targets.
"""

import hashlib
import json
from pathlib import Path, PurePosixPath

import pytest

from workhouse import claims as C
from workhouse import ledger as L

ROOT = Path(__file__).resolve().parents[1]
RUN_IDS = ("discrete_time_wilson_2026-09-04", "excited_wilson_window_2026-09-04")


@pytest.mark.parametrize("run_id", RUN_IDS)
def test_every_original_package_member_has_one_unchanged_destination(run_id):
    run = ROOT / "runs" / run_id
    manifest = json.loads((run / "import_manifest.json").read_text(encoding="utf-8"))
    assert manifest["schema"] == "workhouse-zip-import/1"
    assert manifest["comparison"] == "every file member byte-identical"
    assert len(manifest["source_zip_sha256"]) == 64
    int(manifest["source_zip_sha256"], 16)
    members = manifest["members"]
    by_name = {m["package_path"]: m for m in members}
    assert len(by_name) == len(members), "duplicate ZIP-member mapping"
    assert len({m["repository_path"] for m in members}) == len(members)
    package_pins = {}
    for line in (run / "PACKAGE_SHA256SUMS").read_text(encoding="utf-8").splitlines():
        if line.strip() and not line.startswith("#"):
            digest, name = line.split(maxsplit=1)
            package_pins[name.strip()] = digest
    # The original checksum manifest is itself a preserved ZIP member.
    assert set(by_name) == set(package_pins) | {"SHA256SUMS"}
    for name, member in by_name.items():
        relative = PurePosixPath(member["repository_path"])
        assert not relative.is_absolute() and ".." not in relative.parts
        path = ROOT / relative
        data = path.read_bytes()
        digest = hashlib.sha256(data).hexdigest()
        assert len(data) == member["size"]
        assert digest == member["sha256"], member["repository_path"]
        if name in package_pins:
            assert digest == package_pins[name], f"relocated received member changed: {name}"


def test_both_packages_are_registered_against_existing_native_gaps():
    runs = C.load_runs()
    gap_ids = L.load().gap_ids
    for run_id in RUN_IDS:
        matches = [r for r in runs if r["id"] == run_id]
        assert len(matches) == 1
        assert set(matches[0]["bears_on"]) == {"G18", "G19"}
        assert set(matches[0]["bears_on"]) <= gap_ids
        assert (ROOT / matches[0]["dir"] / "import_manifest.json").is_file()
