"""Record finite exact physical-band controls without certifying the infinite theorem."""

from __future__ import annotations

import argparse
import hashlib
import json
import platform
import sys
from dataclasses import asdict
from datetime import UTC, datetime
from pathlib import Path

import sympy

from workhouse.invariants.wilson_physical_band import physical_band_suite
from workhouse.wilson_physical_band import exact_controls

ROOT = Path(__file__).resolve().parents[1]
SOURCES = (
    "src/workhouse/wilson_physical_band.py",
    "src/workhouse/invariants/wilson_physical_band.py",
    "scripts/verify_wilson_physical_band.py",
    "tests/test_wilson_physical_band.py",
    "src/workhouse/wilson_activity_extraction.py",
    "paper/research_notes/G18_WILSON_INFINITE_VOLUME_PHYSICAL_BAND_20260905.md",
    "paper/research_notes/G18_WILSON_CARDINALITY_UNITARY_CHART_20260905.md",
    "paper/research_notes/G18_WILSON_WEIGHTED_ACTIVITY_BOUND_20260905.md",
)


def source_hashes():
    return {name: hashlib.sha256((ROOT / name).read_bytes()).hexdigest() for name in SOURCES}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    if args.output.exists():
        raise FileExistsError("Choose a fresh output path; existing evidence is preserved")
    if sys.flags.optimize:
        raise RuntimeError("Exact controls require assertions enabled")
    sources = source_hashes()
    checks = physical_band_suite.run()
    if not all(check.passed for check in checks):
        raise AssertionError(checks)
    controls = exact_controls()
    if source_hashes() != sources:
        raise RuntimeError("A source changed during verification")
    report = {
        "schema": "workhouse-physical-band-finite-controls/v1",
        "passed": True,
        "exact_check_count": len(checks),
        "checks": [asdict(check) for check in checks],
        "finite_controls": controls,
        "sources": sources,
        "runtime": {
            "python": sys.version,
            "sympy": sympy.__version__,
            "system": platform.system(),
            "architecture": platform.machine(),
            "completed_utc": datetime.now(UTC).isoformat(),
            "assertions_enabled": True,
        },
        "verification_scope": (
            "Finite exact source Gram, projection, activity exhaustion and rational controls only; "
            "no infinite-volume Wilson theorem is machine-certified"
        ),
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    with args.output.open("x", encoding="utf-8") as stream:
        json.dump(report, stream, indent=2, sort_keys=True)
        stream.write("\n")
    print(f"{len(checks)}/{len(checks)} finite exact controls passed; wrote {args.output}")


if __name__ == "__main__":
    main()
