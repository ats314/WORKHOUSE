"""Replay full-corpus inventory coverage from pinned source metadata, not counts.

This certifies capture/locator coverage and explicit exclusions only. Extraction,
numeric signatures and reference-library identification do not certify proofs.
"""

from __future__ import annotations

import argparse
import gzip
import hashlib
import json
from collections import Counter, defaultdict
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
    source_paths = {}
    for item in contract["inputs"]:
        if item["role"] in result:
            raise ValueError(f"Duplicate coverage input role: {item['role']}")
        source_paths[item["role"]] = _bounded(item["source_path"])
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
    required = {
        "loose_files",
        "loose_classifications",
        "loose_extraction",
        "members",
        "member_objects",
        "member_classifications",
        "member_extraction",
        "quarantine",
        "prior_reviews",
    }
    if not required <= result.keys():
        raise ValueError("Coverage contract is missing required source inputs")
    result["_source_paths"] = source_paths
    return result


def _unique(rows, field, label):
    result = {row[field]: row for row in rows}
    if len(result) != len(rows):
        raise ValueError(f"Duplicate {label} key")
    return result


def _multiset(rows):
    return Counter(json.dumps(row, sort_keys=True, ensure_ascii=False) for row in rows)


def expected_metadata(inputs):
    """Derive metadata from pinned source records, never from candidate rows."""
    extraction = {}
    for role in ["loose_extraction", "member_extraction"]:
        root = PurePosixPath(inputs["_source_paths"][role]).parent
        for source in inputs[role]:
            sha = source["sha256"]
            if sha in extraction:
                raise ValueError("Duplicate extraction source digest")
            normalized = {
                key: value
                for key, value in source.items()
                if key not in {"paths", "representative", "sha256", "size", "review"}
            }
            if normalized.get("text_file"):
                normalized["text_file"] = str(root / _bounded(normalized["text_file"]))
            extraction[sha] = normalized
    members = defaultdict(list)
    fields = [
        "containerpath",
        "container_sha256",
        "nestedancestor",
        "ancestor_sha256",
        "memberpath",
        "member_index",
        "unsafe_extraction_path",
    ]
    for member in inputs["members"]:
        if member.get("kind") == "file" and member.get("sha256"):
            members[member["sha256"]].append({k: member[k] for k in fields if k in member})
    reviews = defaultdict(list)
    archives = defaultdict(set)
    for prior in inputs["prior_reviews"]:
        archives[prior["digest"]].add(prior["archive"])
        for review in prior["reviews"]:
            if review["digest"] != prior["digest"] or review["archive"] != prior["archive"]:
                raise ValueError("Prior review source identity mismatch")
            reviews[prior["digest"]].append({"archive": prior["archive"], **review})
    return extraction, members, reviews, archives


def expected_inventory(inputs):
    files = _unique(inputs["loose_files"], "path", "loose file")
    classes = _unique(inputs["loose_classifications"], "path", "loose classification")
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
    member_classes = _unique(inputs["member_classifications"], "sha256", "member classification")
    objects = _unique(inputs["member_objects"], "sha256", "member object")
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
    extraction, member_provenance, prior_reviews, prior_archives = expected_metadata(inputs)
    if extraction.keys() != expected.keys():
        raise ValueError("Extraction records do not cover exactly the eligible content union")
    for sha, row in actual.items():
        exp = expected[sha]
        if row["size"] != exp["size"] or set(row["paths"]) != exp["paths"]:
            raise ValueError(f"Size/path coverage mismatch: {sha}")
        if set(row["provenance"]["current_loose_paths"]) != exp["current_loose"]:
            raise ValueError(f"Current source locator mismatch: {sha}")
        if any(key in row for key in ["review", "status", "evidence", "tier"]):
            raise ValueError("Inventory cannot declare a proof status or review verdict")
        if row["extraction"] != extraction[sha]:
            raise ValueError(f"Normalized extraction metadata differs from frozen source: {sha}")
        if _multiset(row["provenance"]["archive_members"]) != _multiset(member_provenance[sha]):
            raise ValueError(f"Structured archive chain provenance mismatch: {sha}")
        if _multiset(row["provenance"]["prior_review_refs"]) != _multiset(prior_reviews[sha]):
            raise ValueError(f"Prior review provenance mismatch: {sha}")
        if row["provenance"]["prior_inventory_archives"] != sorted(prior_archives[sha]):
            raise ValueError(f"Prior inventory archive provenance mismatch: {sha}")
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
            "normalized extraction and archive/review provenance; no mathematical proof acceptance."
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
