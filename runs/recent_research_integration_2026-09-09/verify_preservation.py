"""Verify unchanged source imports; optionally pin the completed integration run."""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

RUN = Path(__file__).resolve().parent
ROOT = RUN.parents[1]


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load(name):
    return json.loads((RUN / name).read_text(encoding="utf-8-sig"))


def verify():
    checked = {"branch_run_files": 0, "campaign_sources": 0, "priority_docs": 0,
               "ported_lean_modules": 0}
    problems = []

    def check(path, expected):
        if not path.is_file() or digest(path).lower() != expected.lower():
            problems.append(str(path))

    imports = load("branch_run_imports.json")
    for item in imports:
        source = Path(item["source_directory"])
        destination = ROOT / "runs" / item["id"]
        names = {row["path"] for row in item["files"]}
        actual = {p.relative_to(destination).as_posix()
                  for p in destination.rglob("*") if p.is_file()}
        if names != actual:
            problems.append(f"{item['id']}: imported file inventory changed")
        for row in item["files"]:
            check(source / row["path"], row["sha256"])
            check(destination / row["path"], row["sha256"])
            checked["branch_run_files"] += 1
    for row in load("SOURCE_MANIFEST.json")["sources"]:
        check(ROOT / row["path"], row["sha256"])
        check(Path(row["original_path"]), row["sha256"])
        checked["campaign_sources"] += 1
    for row in load("docs_coverage.json")["records"]:
        check(ROOT / row["path"], row["sha256"])
        checked["priority_docs"] += 1
    lean = load("lean_integration_report.json")
    for row in lean["ported_modules"]:
        check(ROOT / row["destination"], row["sha256"])
        check(Path(row["source"]), row["sha256"])
        checked["ported_lean_modules"] += 1
    check(ROOT / "lean/Workhouse/Basic.lean", lean["basic_sha256_after"])
    return {"passed": not problems, "checked": checked, "problems": problems,
            "note": "Original provenance paths must be mounted for this optional source audit."}


def write_pins():
    files = sorted(p for p in RUN.rglob("*") if p.is_file() and p != RUN / "SHA256SUMS")
    lines = [f"{digest(p)}  {p.relative_to(RUN).as_posix()}\n" for p in files]
    (RUN / "SHA256SUMS").write_text("".join(lines), encoding="utf-8", newline="\n")
    return len(files)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--write-pins", action="store_true")
    args = parser.parse_args()
    report = verify()
    print(json.dumps(report, indent=2))
    if not report["passed"]:
        raise SystemExit(1)
    if args.write_pins:
        print(f"Pinned {write_pins()} files in the integration run.")
