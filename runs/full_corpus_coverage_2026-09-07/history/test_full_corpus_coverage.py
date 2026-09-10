"""Coverage and corruption controls; no mathematical truth inferred from intake."""

from __future__ import annotations

import copy
import importlib.util
import json
import subprocess
import sys
from pathlib import Path

import pytest

HERE = Path(__file__).resolve().parent
if (HERE / "coverage_run").is_dir():
    RUN = HERE / "coverage_run"
    MANIFEST = HERE / "WORKHOUSE_FULL_2026-09-07.jsonl"
    SCRIPT = HERE / "verify_full_corpus_coverage.py"
else:
    ROOT = HERE.parent
    RUN = ROOT / "runs/full_corpus_coverage_2026-09-07"
    MANIFEST = ROOT / "notes/WORKHOUSE_FULL_2026-09-07.jsonl"
    SCRIPT = ROOT / "scripts/verify_full_corpus_coverage.py"


@pytest.fixture(scope="module")
def fixture():
    spec = importlib.util.spec_from_file_location("full_corpus_coverage_control", SCRIPT)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    records = [
        json.loads(line) for line in MANIFEST.read_text(encoding="utf-8").splitlines() if line
    ]
    return module, records, module.load_inputs(RUN)


def test_inventory_covers_independently_reconstructed_source_union(fixture):
    module, records, inputs = fixture
    assert module.validate_records(records, inputs)["passed"]


def test_strict_subset_cannot_pass_by_its_own_count(fixture):
    module, records, inputs = fixture
    with pytest.raises(ValueError, match="Content coverage mismatch"):
        module.validate_records(records[:-1], inputs)


def test_recovered_object_list_must_cover_recursive_member_hashes(fixture):
    module, _, inputs = fixture
    removed = inputs["member_objects"][0]["sha256"]
    bad = {
        **inputs,
        "member_objects": inputs["member_objects"][1:],
        "member_classifications": [
            row for row in inputs["member_classifications"] if row["sha256"] != removed
        ],
    }
    with pytest.raises(ValueError, match="all member-only hashes"):
        module.expected_inventory(bad)


def test_missing_copy_locator_is_not_hidden_by_digest_coverage(fixture):
    module, records, inputs = fixture
    index = next(i for i, row in enumerate(records) if len(row["paths"]) > 1)
    bad = list(records)
    bad[index] = {**records[index], "paths": records[index]["paths"][1:]}
    with pytest.raises(ValueError, match="path coverage mismatch"):
        module.validate_records(bad, inputs)


def test_inventory_cannot_promote_a_proof(fixture):
    module, records, inputs = fixture
    bad = [{**records[0], "status": "proven"}, *records[1:]]
    with pytest.raises(ValueError, match="proof status"):
        module.validate_records(bad, inputs)


def test_array_metadata_does_not_claim_text_signature_scan(fixture):
    module, records, inputs = fixture
    index = next(
        i
        for i, row in enumerate(records)
        if row["extraction"]["extraction"] == "numeric-array-metadata-indexed"
    )
    bad = list(records)
    bad[index] = {**records[index], "scanned": True}
    with pytest.raises(ValueError, match="without extracted text"):
        module.validate_records(bad, inputs)


def test_quarantine_locator_cannot_escape_designated_root(fixture):
    module, _, inputs = fixture
    bad = {**inputs, "quarantine": copy.deepcopy(inputs["quarantine"])}
    bad["quarantine"]["moves"][0]["quarantine_path"] = "../escape"
    with pytest.raises(ValueError, match="Unbounded source locator"):
        module.expected_inventory(bad)


def test_changed_compressed_source_is_rejected_before_parsing(fixture, tmp_path):
    module, _, _ = fixture
    contract = json.loads((RUN / "COVERAGE_CONTRACT.json").read_text(encoding="utf-8"))
    (tmp_path / "COVERAGE_CONTRACT.json").write_text(json.dumps(contract), encoding="utf-8")
    first = tmp_path / contract["inputs"][0]["path"]
    first.parent.mkdir(parents=True)
    first.write_bytes(b"corrupted source")
    with pytest.raises(ValueError, match="Compressed input hash mismatch"):
        module.load_inputs(tmp_path)


def test_optimized_python_still_rejects_a_strict_subset(fixture, tmp_path):
    _, records, _ = fixture
    truncated = tmp_path / "subset.jsonl"
    truncated.write_text("\n".join(json.dumps(row) for row in records[:-1]), encoding="utf-8")
    result = subprocess.run(
        [sys.executable, "-O", str(SCRIPT), "--manifest", str(truncated), "--run", str(RUN)],
        capture_output=True,
        text=True,
        check=False,
    )
    assert result.returncode != 0
    assert "Content coverage mismatch" in result.stderr
