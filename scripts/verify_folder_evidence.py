"""Check the September three-folder source intake and its live graph connections.

This checks capture, reviewed disposition and retrieval, never mathematical truth.
The archived source bytes remain independent of later maintained source versions.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from collections import Counter
from pathlib import Path, PurePosixPath

import yaml

ROOT = Path(__file__).resolve().parents[1]
RUN = Path("runs/folder_evidence_integration_2026-09-10")


def bounded(value: str) -> str:
    path = PurePosixPath(value)
    if path.is_absolute() or ".." in path.parts or "\\" in value or ":" in value:
        raise ValueError(f"Unsafe evidence path: {value}")
    return value


def verify(root: Path = ROOT, *, inventory: dict | None = None) -> dict:
    root = Path(root)
    run = root / RUN
    if inventory is None:
        inventory = json.loads((run / "inventory.json").read_text(encoding="utf-8"))
    if inventory["schema"] != "folder-evidence-integration/v1":
        raise ValueError("Unknown folder evidence schema")
    rows = inventory["files"]
    by_path = {bounded(row["path"]): row for row in rows}
    if len(by_path) != len(rows):
        raise ValueError("Duplicate source row")
    census = json.loads((run / "source_inventory.json").read_text(encoding="utf-8"))["files"]
    captured = {entry["path"]: (entry["source_sha256"], entry["bytes"]) for entry in census}
    reviewed = {path: (row["source_sha256"], row["bytes"]) for path, row in by_path.items()}
    if len(captured) != len(census) or captured != reviewed:
        raise ValueError("Review inventory differs from independent source census")
    source_paths = {
        p.relative_to(run / "sources").as_posix()
        for p in (run / "sources").rglob("*")
        if p.is_file()
    }
    if source_paths != set(by_path):
        raise ValueError("Source tree and reviewed inventory differ")
    counts = Counter(path.split("/")[1] for path in by_path)
    if dict(counts) != inventory["folder_counts"]:
        raise ValueError("Folder coverage differs from captured scope")
    aliases = yaml.safe_load((root / "ledger/documents.yaml").read_text(encoding="utf-8"))
    aliases = {"CITE:" + a["alias"]: a for a in aliases["aliases"]}
    claims = {
        row["id"]: row
        for line in (root / "index/claims.jsonl").read_text(encoding="utf-8").splitlines()
        if (row := json.loads(line))
    }
    edges = {
        (e["src"], e["dst"], e["type"])
        for line in (root / "index/graph.jsonl").read_text(encoding="utf-8").splitlines()
        if (e := json.loads(line))
    }
    relationships = Counter()
    for path, row in by_path.items():
        raw = (run / "sources" / path).read_bytes()
        if hashlib.sha256(raw).hexdigest() != row["source_sha256"] or len(raw) != row["bytes"]:
            raise ValueError(f"Changed received source: {path}")
        relationship = row["baseline_relationship"]
        if relationship not in {"identical", "newline_only", "maintained_successor"}:
            raise ValueError(f"Unknown source relationship: {path}")
        relationships[relationship] += 1
        if relationship != "identical" and not row.get("difference_reason"):
            raise ValueError(f"Unexplained source version difference: {path}")
        selected = (root / path).read_bytes()
        if hashlib.sha256(selected).hexdigest() != row["baseline_sha256"]:
            raise ValueError(f"Reviewed source changed; record a fresh scoped successor: {path}")
        actual_relationship = (
            "identical"
            if raw == selected
            else "newline_only"
            if raw.replace(b"\r\n", b"\n") == selected.replace(b"\r\n", b"\n")
            else "maintained_successor"
        )
        if relationship != actual_relationship:
            raise ValueError(f"Incorrect source version relationship: {path}")
        review = row["review"]
        if not review.get("summary") or not review.get("scope"):
            raise ValueError(f"Missing scoped source review: {path}")
        cite_ids = row["citation_ids"]
        if not cite_ids:
            raise ValueError(f"Unrepresented source: {path}")
        for cid in cite_ids:
            alias = aliases.get(cid)
            if not alias or alias.get("path") != path or not (root / path).is_file():
                raise ValueError(f"Unresolved current citation: {path}: {cid}")
            if cid not in claims or claims[cid]["where"] != path or claims[cid]["tier"] != 3:
                raise ValueError(f"Missing or promoted source node: {cid}")
        primary = cite_ids[0]
        for target in review["claim_ids"]:
            if target in aliases and aliases[target].get("path") == path:
                raise ValueError(f"Self-reference is not reviewed claim coverage: {path}")
            if target not in claims or (primary, target, "bears_on") not in edges:
                raise ValueError(f"Missing reviewed claim connection: {primary} -> {target}")
        for target in review["citations"]:
            target = target if target.startswith("CITE:") else "CITE:" + target
            if target in aliases and aliases[target].get("path") == path:
                raise ValueError(f"Self-reference is not reviewed source coverage: {path}")
            if target not in claims or (primary, target, "cites") not in edges:
                raise ValueError(f"Missing reviewed source citation: {primary} -> {target}")
        if not review["claim_ids"] and not review["citations"]:
            raise ValueError(f"No reviewed retrieval connection: {path}")
    return {
        "source_files": len(rows),
        "folder_counts": dict(sorted(counts.items())),
        "baseline_relationships": dict(sorted(relationships.items())),
        "unrepresented_files": 0,
        "verification_scope": "source identity, scoped review coverage and graph retrieval",
        "fresh_mathematical_certification": False,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=ROOT)
    args = parser.parse_args()
    print(json.dumps(verify(args.root), indent=2))


if __name__ == "__main__":
    main()
