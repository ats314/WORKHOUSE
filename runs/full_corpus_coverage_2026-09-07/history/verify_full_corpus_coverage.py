"""Replay full-corpus inventory coverage from pinned source metadata, not counts.

This certifies capture/locator coverage and explicit exclusions only. Extraction,
numeric signatures and reference-library identification do not certify proofs.
"""

from __future__ import annotations

import argparse
import gzip
import hashlib
import json
from pathlib import Path, PurePosixPath


def _hash(data):
    return hashlib.sha256(data).hexdigest()


def _bounded(path):
    pure = PurePosixPath(path)
    if pure.is_absolute() or ".." in pure.parts or "\\" in path or ":" in path:
        raise ValueError(f"Unbounded source locator: {path}")
    return path


def load_inputs(run_dir):
    run_dir = Path(run_dir)
    contract = json.loads((run_dir / "COVERAGE_CONTRACT.json").read_text(encoding="utf-8"))
    if contract["schema"] != "workhouse-full-corpus-coverage/v1":
        raise ValueError("Unknown coverage contract")
    result = {}
    for item in contract["inputs"]:
        encoded = (run_dir / _bounded(item["path"])).read_bytes()
        if _hash(encoded) != item["gzip_sha256"]:
            raise ValueError(f"Compressed input hash mismatch: {item['role']}")
        raw = gzip.decompress(encoded)
        if _hash(raw) != item["source_sha256"]:
            raise ValueError(f"Source input hash mismatch: {item['role']}")
        text = raw.decode("utf-8")
        result[item["role"]] = (
            [json.loads(line) for line in text.splitlines() if line]
            if item["format"] == "jsonl"
            else json.loads(text)
        )
    return result


def expected_inventory(inputs):
    files = {row["path"]: row for row in inputs["loose_files"]}
    classes = {row["path"]: row for row in inputs["loose_classifications"]}
    if files.keys() != classes.keys():
        raise ValueError("Loose classification does not cover the full census")
    expected = {}
    for path, row in files.items():
        _bounded(path)
        classification = classes[path]
        if classification["sha256"] != row["sha256"]:
            raise ValueError("Loose classification hash mismatch")
        if classification["exclusion"] is None:
            record = expected.setdefault(
                row["sha256"], {"size": row["size"], "paths": set(), "current_loose": set()}
            )
            record["paths"].add(path)
            record["current_loose"].add(path)
    member_classes = {row["sha256"]: row for row in inputs["member_classifications"]}
    objects = {row["sha256"]: row for row in inputs["member_objects"]}
    all_loose_hashes = {row["sha256"] for row in files.values()}
    recovered_hashes = {
        row["sha256"]
        for row in inputs["members"]
        if row.get("kind") == "file" and row.get("sha256")
    } - all_loose_hashes
    if recovered_hashes != objects.keys():
        raise ValueError("Recovered objects do not cover all member-only hashes")
    if member_classes.keys() != objects.keys():
        raise ValueError("Member classification does not cover recovered objects")
    for sha, obj in objects.items():
        if member_classes[sha]["exclusion"] is None:
            expected.setdefault(sha, {"size": obj["size"], "paths": set(), "current_loose": set()})
    for member in inputs["members"]:
        if member.get("kind") != "file" or member.get("sha256") not in expected:
            continue
        locator = "!/".join(
            [member["containerpath"], *member.get("nestedancestor", []), member["memberpath"]]
        )
        # An unsafe archive name is an evidence locator, never a filesystem
        # extraction instruction. Original unsafe flags remain in provenance.
        expected[member["sha256"]]["paths"].add("ARCHIVE_MEMBER/" + locator)
    for move in inputs["quarantine"]["moves"]:
        for key in ["original_path", "retained_path", "quarantine_path"]:
            _bounded(move[key])
        if not move["quarantine_path"].startswith("quarantine/2026-09-07-exact-duplicates/"):
            raise ValueError("Quarantine locator outside designated root")
        for key in ["original_path", "retained_path"]:
            if files.get(move[key], {}).get("sha256") != move["sha256"]:
                raise ValueError(
                    "Quarantine duplicate does not match frozen original and retained bytes"
                )
        record = expected.get(move["sha256"])
        if classes[move["original_path"]]["exclusion"] is not None:
            # Two exact duplicated TeX auxiliaries remain captured in the
            # census/relocation audit but are explicitly excluded from notes.
            continue
        if record is None or move["original_path"] not in record["paths"]:
            raise ValueError("Quarantine move is outside eligible source coverage")
        record["paths"].update([move["retained_path"], move["quarantine_path"]])
        record["current_loose"].discard(move["original_path"])
        record["current_loose"].update([move["retained_path"], move["quarantine_path"]])
    return expected


def validate_records(records, inputs, workspace_root=None):
    expected = expected_inventory(inputs)
    actual = {r["digest"]: r for r in records}
    if len(actual) != len(records):
        raise ValueError("Duplicate manifest digest")
    if actual.keys() != expected.keys():
        missing = len(expected.keys() - actual.keys())
        extra = len(actual.keys() - expected.keys())
        raise ValueError(f"Content coverage mismatch: {missing} missing, {extra} extra")
    extraction = {
        r["sha256"]: r for r in [*inputs["loose_extraction"], *inputs["member_extraction"]]
    }
    for sha, row in actual.items():
        exp = expected[sha]
        if row["size"] != exp["size"] or set(row["paths"]) != exp["paths"]:
            raise ValueError(f"Size/path coverage mismatch: {sha}")
        if set(row["provenance"]["current_loose_paths"]) != exp["current_loose"]:
            raise ValueError(f"Current source locator mismatch: {sha}")
        if any(key in row for key in ["review", "status", "evidence", "tier"]):
            raise ValueError("Inventory cannot declare a proof status or review verdict")
        if row["extraction"]["extraction"] != extraction[sha]["extraction"]:
            raise ValueError("Extraction status differs from frozen extraction record")
        if row["scanned"] and not extraction[sha].get("text_file"):
            raise ValueError("Numeric signature scan claimed without extracted text")
        if row["extraction"]["extraction"] in {"error", "not-yet-extracted"}:
            raise ValueError("Incomplete extraction bookkeeping in final inventory")
    if workspace_root is not None:
        workspace_root = Path(workspace_root).resolve()
        for move in inputs["quarantine"]["moves"]:
            for key in ["retained_path", "quarantine_path"]:
                path = (workspace_root / _bounded(move[key])).resolve()
                if not path.is_relative_to(workspace_root):
                    raise ValueError("Resolved locator escapes workspace")
                if _hash(path.read_bytes()) != move["sha256"]:
                    raise ValueError("Current quarantine/retained byte mismatch")
    return {
        "passed": True,
        "distinct_contents": len(records),
        "quarantine_moves": len(inputs["quarantine"]["moves"]),
        "scope": (
            "Exact eligible census/member union, complete source locators and explicit "
            "extraction-only semantics; no mathematical proof acceptance."
        ),
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--manifest", type=Path, required=True)
    parser.add_argument("--run", type=Path, required=True)
    parser.add_argument("--workspace-root", type=Path)
    args = parser.parse_args()
    records = [
        json.loads(line) for line in args.manifest.read_text(encoding="utf-8").splitlines() if line
    ]
    print(
        json.dumps(validate_records(records, load_inputs(args.run), args.workspace_root), indent=2)
    )


if __name__ == "__main__":
    main()
