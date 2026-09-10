"""Read-only content census. A digest is inventory evidence, never a proof review."""

from __future__ import annotations

import argparse
import hashlib
import json
import os
from collections import Counter
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
from pathlib import Path

INFRASTRUCTURE = {
    ".git": "Git object database and checkout administration",
    ".venv": "Installed Python environment",
    "venv": "Installed Python environment",
    "node_modules": "Installed JavaScript dependencies",
    ".lake": "Downloaded Lean dependencies and compiled build tree",
    "__pycache__": "Generated Python bytecode",
    ".pytest_cache": "Generated pytest cache",
    ".ruff_cache": "Generated Ruff cache",
    ".mypy_cache": "Generated type-checker cache",
}


def dump(path, records):
    with path.open("x", encoding="utf-8", newline="\n") as out:
        for row in records:
            out.write(json.dumps(row, ensure_ascii=False, sort_keys=True) + "\n")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    root, output = args.root.resolve(), args.output.resolve()
    output.mkdir(parents=True, exist_ok=True)
    if (output / "files.jsonl").exists():
        raise FileExistsError("Use a fresh snapshot output directory")
    errors, excluded, dirs, paths = [], [], [], []

    def onerror(error):
        errors.append({"path": str(error.filename), "error": str(error)})

    for parent, subdirs, files in os.walk(root, followlinks=False, onerror=onerror):
        parent = Path(parent)
        kept = []
        for name in sorted(subdirs):
            child = parent / name
            rel = child.relative_to(root).as_posix()
            reason = INFRASTRUCTURE.get(name)
            if child.is_symlink() or child.is_junction():
                reason = "Filesystem link; not followed; target must be separately accounted"
            if child == output or child.name == "corpus_coverage_20260907":
                reason = "This audit's own generated outputs, excluded to avoid self-reference"
            if reason:
                excluded.append({"path": rel, "reason": reason})
            else:
                kept.append(name)
        subdirs[:] = kept
        dirs.append(parent.relative_to(root).as_posix())
        paths.extend(parent / name for name in sorted(files))
    print(json.dumps({"enumerated_files": len(paths), "excluded_subtrees": len(excluded)}), flush=True)

    def record(path):
        rel = path.relative_to(root).as_posix()
        item = {"path": rel, "top": rel.split("/")[0], "extension": path.suffix.lower()}
        try:
            if path.is_symlink():
                return {**item, "error": "Filesystem file link; not followed"}
            before = path.stat()
            digest = hashlib.sha256()
            with path.open("rb") as source:
                while chunk := source.read(2**20):
                    digest.update(chunk)
            after = path.stat()
            item.update(size=after.st_size, mtime_ns=after.st_mtime_ns, sha256=digest.hexdigest())
            if (before.st_size, before.st_mtime_ns) != (after.st_size, after.st_mtime_ns):
                item["error"] = "File changed during census; requires recheck"
        except OSError as error:
            item["error"] = str(error)
        return item

    records = []
    with ThreadPoolExecutor(max_workers=6) as pool:
        for index, item in enumerate(pool.map(record, paths), 1):
            records.append(item)
            if index % 10000 == 0:
                print(json.dumps({"hashed_or_error": index}), flush=True)
    records.sort(key=lambda row: row["path"])
    dump(output / "files.jsonl", records)
    dump(output / "excluded_subtrees.jsonl", excluded)
    dump(output / "directories.jsonl", [{"path": value} for value in dirs])
    errors.extend(row for row in records if "error" in row)
    dump(output / "errors.jsonl", errors)
    summary = {
        "root": str(root), "created_utc": datetime.now(timezone.utc).isoformat(),
        "files": len(records), "directories": len(dirs), "excluded_subtrees": len(excluded),
        "errors": len(errors), "bytes": sum(row.get("size", 0) for row in records),
        "distinct_sha256": len({row["sha256"] for row in records if "sha256" in row}),
        "by_top": dict(Counter(row["top"] for row in records)),
        "by_extension": dict(Counter(row["extension"] for row in records)),
        "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "scope": "All regular files outside explicitly listed infrastructure and audit-output subtrees. Archive members are a separate audit. Hashing is not semantic review.",
    }
    with (output / "summary.json").open("x", encoding="utf-8", newline="\n") as out:
        json.dump(summary, out, indent=2, ensure_ascii=False, sort_keys=True)
        out.write("\n")
    print(json.dumps(summary, ensure_ascii=False), flush=True)


if __name__ == "__main__":
    main()
