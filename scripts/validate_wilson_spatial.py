"""Verify pinned spatial inputs and replay the narrowly scoped exact controls.

Run with PYTHONPATH=src from this repository. --pin-inputs imports the listed
committed source texts once; the default mode never rewrites their manifest.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import subprocess
import xml.etree.ElementTree as ET
from datetime import UTC, datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
INPUTS = ROOT / "docs/derivations/wilson-spatial-inputs"
CHECKOUT = Path("C:/WORKHOUSE/WORKHOUSE-autonomous-20260905")
FLAT = Path("C:/WORKHOUSE/WORKHOUSE-flat-holonomy-20260907")
SOURCE_SPECS = (
    (
        CHECKOUT,
        "4bf812428e0af51d1ffcda299b0d97b38b644926",
        "G19_FORM_SCHUR_SCALE_COMPARISON_20260905.md",
    ),
    (
        CHECKOUT,
        "4bf812428e0af51d1ffcda299b0d97b38b644926",
        "G19_FULL_GAUSSIAN_FAST_GREEN_20260906.md",
    ),
    (
        CHECKOUT,
        "4bf812428e0af51d1ffcda299b0d97b38b644926",
        "G19_DYNAMIC_FIBER_COVARIANCE_AND_CUBIC_ENERGY_20260906.md",
    ),
    (CHECKOUT, "4bf812428e0af51d1ffcda299b0d97b38b644926", "G19_CUBIC_GROUND_TRANSFER_20260906.md"),
    (
        CHECKOUT,
        "4bf812428e0af51d1ffcda299b0d97b38b644926",
        "G19_WILSON_FINITE_CELL_GAP_AND_BOUNDARY_FORM_20260905.md",
    ),
    (
        CHECKOUT,
        "4bf812428e0af51d1ffcda299b0d97b38b644926",
        "G19_GAUSSIAN_PATH_ENDPOINT_BASELINE_20260906.md",
    ),
    (
        CHECKOUT,
        "4bf812428e0af51d1ffcda299b0d97b38b644926",
        "G19_WILSON_HARMONIC_CUBIC_OBSTRUCTION_20260906.md",
    ),
    (
        CHECKOUT,
        "4bf812428e0af51d1ffcda299b0d97b38b644926",
        "G19_LOCAL_COVARIANT_AVERAGED_PATH_SOURCES_20260905.md",
    ),
    (
        FLAT,
        "687e1a6c535b19dcd7ce8ca0a802d8270f069111",
        "G19_FLAT_HOLONOMY_SOURCES_AND_RANK_REPAIR_20260907.md",
    ),
)


def sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def committed(checkout: Path, revision: str, name: str) -> bytes:
    return subprocess.run(
        [
            "git",
            "-c",
            f"safe.directory={checkout.as_posix()}",
            "-C",
            str(checkout),
            "show",
            f"{revision}:paper/research_notes/{name}",
        ],
        check=True,
        capture_output=True,
    ).stdout


def pin_inputs() -> None:
    manifest = INPUTS / "manifest.json"
    if manifest.exists():
        raise FileExistsError("The spatial input manifest already exists; verify it instead")
    INPUTS.mkdir(parents=True, exist_ok=True)
    entries = []
    for checkout, revision, name in SOURCE_SPECS:
        payload = (checkout / "paper/research_notes" / name).read_bytes()
        blob = committed(checkout, revision, name)
        if payload.replace(b"\r\n", b"\n") != blob.replace(b"\r\n", b"\n"):
            raise ValueError(f"Working source differs from its recorded commit: {name}")
        target = INPUTS / name
        if target.exists():
            raise FileExistsError(target)
        target.write_bytes(payload)
        entries.append(
            {
                "name": name,
                "source_checkout": str(checkout),
                "source_commit": revision,
                "sha256": sha(payload),
            }
        )
    manifest.write_text(
        json.dumps(
            {
                "scope": "unchanged analytic spatial inputs; no promotion from provenance alone",
                "files": entries,
            },
            indent=2,
        )
        + "\n",
        encoding="utf-8",
    )


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--pin-inputs", action="store_true")
    args = parser.parse_args()
    if args.pin_inputs:
        pin_inputs()
    manifest = json.loads((INPUTS / "manifest.json").read_text(encoding="utf-8"))
    pins = []
    for entry in manifest["files"]:
        payload = (INPUTS / entry["name"]).read_bytes()
        if sha(payload) != entry["sha256"]:
            raise ValueError(f"Input digest mismatch: {entry['name']}")
        blob = committed(Path(entry["source_checkout"]), entry["source_commit"], entry["name"])
        if payload.replace(b"\r\n", b"\n") != blob.replace(b"\r\n", b"\n"):
            raise ValueError(f"Input differs from recorded commit: {entry['name']}")
        pins.append({**entry, "matches_commit_after_lf_normalization": True})

    from workhouse.invariants.wilson_spatial import spatial

    results = [vars(result) for result in spatial.run()]
    if not all(result["passed"] for result in results):
        raise ValueError(results)
    artifacts = (
        "docs/derivations/wilson-spatial-schur-excess.md",
        "src/workhouse/invariants/wilson_spatial.py",
        "scripts/validate_wilson_spatial.py",
        "lean/Workhouse/Basic.lean",
        "ledger/theorems.yaml",
        "ledger/gaps.yaml",
        "ledger/documents.yaml",
    )
    report = {
        "recorded_at": datetime.now(UTC).isoformat(),
        "analytic_scope": (
            "Exact Schur excess and conditional weighted remainder; complete local "
            "Wilson/source jets and conditional scale budgets"
        ),
        "not_established": (
            "Uniform interacting Wilson SP8/coarse matching, complete spatial trajectory "
            "and continuum measure"
        ),
        "input_pins": pins,
        "checks": results,
        "artifacts": {name: sha((ROOT / name).read_bytes()) for name in artifacts},
    }
    report["test_runs"] = []
    for filename in (
        "wilson-spatial-focused-2026-09-08.xml",
        "wilson-spatial-focused-retry-2026-09-08.xml",
        "wilson-spatial-graph-2026-09-08.xml",
    ):
        path = ROOT / "docs/validation" / filename
        if path.exists():
            suites = ET.parse(path).findall(".//testsuite")
            report["test_runs"].append(
                {
                    "file": filename,
                    "sha256": sha(path.read_bytes()),
                    **{
                        key: sum(int(suite.get(key, "0")) for suite in suites)
                        for key in ("tests", "failures", "errors", "skipped")
                    },
                }
            )
    report["retry_reason"] = (
        "The first collection failed on indentation in the new G19 ledger route. "
        "The repaired YAML was parsed directly, then the focused checks were rerun. "
        "The original error report is preserved; no full-regression pass is claimed."
    )
    report["lean_records"] = {
        path.name: sha(path.read_bytes())
        for path in (ROOT / "docs/validation").glob("wilson-spatial-*2026-09-08.txt")
    }
    output = ROOT / "docs/validation/wilson-spatial-2026-09-08.json"
    output.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    print(f"{len(results)}/{len(results)} exact controls; {len(pins)} pinned inputs; {output}")


if __name__ == "__main__":
    main()
