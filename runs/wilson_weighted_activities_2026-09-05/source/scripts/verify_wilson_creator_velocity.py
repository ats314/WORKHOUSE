"""Record exact finite creator-velocity controls and rational majorant consequences."""

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

from workhouse.invariants.wilson_creator_velocity import creator_velocity_suite
from workhouse.wilson_contour_trees import exact_tree_control
from workhouse.wilson_creator_velocity import exact_controls

ROOT = Path(__file__).resolve().parents[1]
SOURCES = (
    "scripts/verify_wilson_creator_velocity.py",
    "src/workhouse/wilson_creator_velocity.py",
    "src/workhouse/invariants/wilson_creator_velocity.py",
    "tests/test_wilson_creator_velocity.py",
    "src/workhouse/wilson_contour_trees.py",
    "tests/test_wilson_contour_trees.py",
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
        raise RuntimeError("Exact controls require assertions enabled; do not use Python -O")
    sources = source_hashes()
    checks = list(creator_velocity_suite.run())
    if not all(check.passed for check in checks):
        raise AssertionError(checks)
    controls = exact_controls()
    if sources != source_hashes():
        raise RuntimeError("A source changed during verification; rerun after it is stable")
    result = {
        "schema": "workhouse-wilson-creator-velocity/v1",
        "passed": True,
        "exact_check_count": len(checks),
        "checks": [asdict(check) for check in checks],
        "finite_controls": controls,
        "finite_tree_control": exact_tree_control(),
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
            "Exact finite tensor creator inversion, vacuum-line phase, component factorization, "
            "finite Neumann contraction certificates, an ordered polynomial contour and rational "
            "majorant consequences under stated analytic premises. "
            "No uniform Wilson analytic theorem, "
            "infinite-dimensional bound, full analytic tree expansion or physical spectrum is "
            "certified by these finite checks."
        ),
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    with args.output.open("x", encoding="utf-8", newline="\n") as stream:
        stream.write(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(
        f"{len(checks)}/{len(checks)} exact creator-velocity controls passed; wrote {args.output}"
    )


if __name__ == "__main__":
    main()
