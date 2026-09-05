"""Verify the additive vacuum-compression identities and sharper constants."""

from __future__ import annotations

import argparse
import hashlib
import json
import sys
from dataclasses import asdict
from pathlib import Path

import sympy

from workhouse.invariants.wilson_compression import compression_suite

ROOT = Path(__file__).resolve().parents[1]


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    if args.output.exists():
        raise FileExistsError("Choose a new output path; existing evidence is preserved")
    results = list(compression_suite.run())
    if not all(result.passed for result in results):
        raise AssertionError(results)
    sources = [
        "scripts/verify_wilson_vacuum_compression.py",
        "src/workhouse/invariants/wilson_compression.py",
        "src/workhouse/wilson_vacuum_chart.py",
        "tests/test_wilson_vacuum_compression.py",
        "paper/research_notes/G18_VACUUM_COMPRESSION_BOUND_20260905.md",
        "lean/Workhouse/VacuumChart.lean",
        "lean/Workhouse/VacuumCompression.lean",
        "lean/Workhouse.lean",
    ]
    result = {
        "schema": "workhouse-wilson-vacuum-compression/v1",
        "passed": True,
        "checks": [asdict(item) for item in results],
        "exact_check_count": len(results),
        "scope": "exact symbolic complex three-state block, tensor transfer, rational bounds; "
        "arbitrary finite-matrix compression separately Lean checked; "
        "operator-norm conclusions proved analytically",
        "coefficient_convention": "[u^2] is half the second derivative",
        "sharpened_bounds": {
            "simple_compression_factor": "6032/5",
            "connected_factor": "3096/5",
            "disjoint_Js1_factor": "41472/125",
            "single_f_star_factor": "118872/125",
        },
        "sources": {
            name: hashlib.sha256((ROOT / name).read_bytes()).hexdigest() for name in sources
        },
        "runtime": {"python": sys.version.split()[0], "sympy": sympy.__version__},
        "not_claimed": ["convergent nonlinear chart", "thermodynamic actual-Wilson Riesz band"],
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(
        json.dumps(result, indent=2, sort_keys=True, default=str) + "\n",
        encoding="utf-8",
        newline="\n",
    )
    print(f"{len(results)}/{len(results)} exact checks passed; wrote {args.output}")


if __name__ == "__main__":
    main()
