"""A received file cannot disappear or acquire a stronger tier through intake."""

import copy
import importlib.util
import json
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "verify_folder_evidence", ROOT / "scripts/verify_folder_evidence.py"
)
audit = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(audit)


def inventory():
    return json.loads((ROOT / audit.RUN / "inventory.json").read_text(encoding="utf-8"))


def test_received_folder_evidence_has_scoped_graph_coverage():
    report = audit.verify()
    assert report["unrepresented_files"] == 0
    assert report["fresh_mathematical_certification"] is False


@pytest.mark.parametrize(
    "defect",
    ["omitted", "duplicate", "digest", "citation", "claim", "scope", "self", "version", "selected"],
)
def test_intake_rejects_lost_sources_and_broken_provenance(defect):
    data = copy.deepcopy(inventory())
    row = data["files"][0]
    if defect == "omitted":
        data["files"].pop()
    elif defect == "duplicate":
        data["files"].append(copy.deepcopy(row))
    elif defect == "digest":
        row["source_sha256"] = "0" * 64
    elif defect == "citation":
        row["citation_ids"] = ["CITE:DOES_NOT_EXIST"]
    elif defect == "claim":
        row["review"]["claim_ids"] = ["RESULT:DOES_NOT_EXIST"]
    elif defect == "scope":
        row["review"]["scope"] = ""
    elif defect == "self":
        row["review"]["claim_ids"] = row["citation_ids"]
        row["review"]["citations"] = []
    elif defect == "version":
        row["baseline_relationship"] = (
            "maintained_successor" if row["baseline_relationship"] == "identical" else "identical"
        )
        row["difference_reason"] = "An unsupported description cannot replace byte comparison."
    elif defect == "selected":
        row["baseline_sha256"] = "0" * 64
    with pytest.raises(ValueError):
        audit.verify(inventory=data)
