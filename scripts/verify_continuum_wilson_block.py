"""Record exact physical-block controls with their limited verification scope."""

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

from workhouse.continuum_wilson_block import exact_block_controls
from workhouse.continuum_wilson_rotor import exact_rotor_controls, rotor_certificates
from workhouse.invariants.continuum_wilson_block import continuum_block_suite

ROOT = Path(__file__).resolve().parents[1]
SOURCES = (
    "src/workhouse/continuum_wilson_block.py",
    "src/workhouse/continuum_wilson_rotor.py",
    "src/workhouse/invariants/continuum_wilson_block.py",
    "src/workhouse/invariants/_core.py",
    "scripts/verify_continuum_wilson_block.py",
    "tests/test_continuum_wilson_block.py",
    "paper/research_notes/G19_OS_BLOCKING_AND_REVERSE_MASS_MATCHING_20260905.md",
    "paper/research_notes/G19_CONDITIONAL_GRADIENT_REPAIR_20260905.md",
    "paper/research_notes/G19_WILSON_BLOCK_SCORE_AND_FIBER_OBSTRUCTION_20260905.md",
    "paper/research_notes/G19_WILSON_PHYSICAL_FIBER_FAST_GAP_20260905.md",
    "paper/research_notes/G19_WILSON_TWO_SQUARE_PHYSICAL_SHELLS_20260905.md",
    "paper/research_notes/G19_WILSON_STRIP_BO_AND_TWO_STRIP_SPLITTING_20260905.md",
    "paper/research_notes/G19_GLUEBALL_REVERSE_TARGET_DATA_20260905.md",
)


def source_hashes() -> dict[str, str]:
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
    checks = continuum_block_suite.run()
    if not all(check.passed for check in checks):
        raise AssertionError(checks)
    block, rotor = exact_block_controls(), exact_rotor_controls()
    if source_hashes() != sources:
        raise RuntimeError("A source changed during verification")
    report = {
        "schema": "workhouse-continuum-wilson-block-controls/v1",
        "passed": True,
        "exact_check_count": len(checks),
        "checks": [asdict(check) for check in checks],
        "block_controls": block,
        "rotor_controls": rotor,
        "rotor_certificates": rotor_certificates(),
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
            "Exact finite Gaussian, Lie, coordinate and oscillator controls, plus integer "
            "replay of fixed-u untruncated intrinsic SU(2) rotor enclosures under the analytic "
            "tail form identification. No analytic remainder, OS complement, multiscale "
            "or continuum theorem is machine-certified."
        ),
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    with args.output.open("x", encoding="utf-8", newline="\n") as stream:
        json.dump(report, stream, indent=2, sort_keys=True)
        stream.write("\n")
    print(f"{len(checks)}/{len(checks)} exact controls passed; wrote {args.output}")


if __name__ == "__main__":
    main()
