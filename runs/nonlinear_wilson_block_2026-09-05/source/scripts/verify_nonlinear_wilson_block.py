"""Record scoped nonlinear single-block controls from the selected source tree."""

from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import platform
import sys
import types
from dataclasses import asdict
from datetime import UTC, datetime
from pathlib import Path

import sympy

ROOT = Path(__file__).resolve().parents[1]
SOURCES = (
    "src/workhouse/nonlinear_wilson_block.py",
    "src/workhouse/invariants/nonlinear_wilson_block.py",
    "src/workhouse/invariants/_core.py",
    "scripts/verify_nonlinear_wilson_block.py",
    "tests/test_nonlinear_wilson_block.py",
    "paper/research_notes/G19_WILSON_GLOBAL_VERTICAL_BARRIER_20260905.md",
    "paper/research_notes/G19_WILSON_GROUND_BUNDLE_RELATIVE_FORM_20260905.md",
    "paper/research_notes/G19_WILSON_ACTUAL_BLOCK_FAST_COMPLEMENT_20260905.md",
    "lean/Workhouse/GlobalWilsonVertical.lean",
)


def source_hashes():
    return {name: hashlib.sha256((ROOT / name).read_bytes()).hexdigest() for name in SOURCES}


def load_native():
    """Load the acceptance modules from this tree without installed fallbacks."""
    for name in ("workhouse", "workhouse.invariants"):
        package = types.ModuleType(name)
        package.__path__ = []
        sys.modules[name] = package
    modules = []
    for name, relative in (
        ("workhouse.nonlinear_wilson_block", SOURCES[0]),
        ("workhouse.invariants._core", SOURCES[2]),
        ("workhouse.invariants.nonlinear_wilson_block", SOURCES[1]),
    ):
        spec = importlib.util.spec_from_file_location(name, ROOT / relative)
        if spec is None or spec.loader is None:
            raise RuntimeError(f"Cannot load local source: {relative}")
        module = importlib.util.module_from_spec(spec)
        sys.modules[name] = module
        spec.loader.exec_module(module)
        modules.append(module)
    return modules[0], modules[2]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    if args.output.exists():
        raise FileExistsError("Choose a fresh output path; existing evidence is preserved")
    if sys.flags.optimize:
        raise RuntimeError("Exact controls require assertions enabled")
    sys.dont_write_bytecode = True
    sources = source_hashes()
    native, invariants = load_native()
    controls = native.exact_nonlinear_controls()
    checks = invariants.nonlinear_wilson_suite.run()
    if not all(check.passed for check in checks):
        raise AssertionError(checks)
    if source_hashes() != sources:
        raise RuntimeError("A source changed during verification")
    report = {
        "schema": "workhouse-nonlinear-wilson-block-controls/v1",
        "passed": True,
        "exact_check_count": len(checks),
        "checks": [asdict(check) for check in checks],
        "controls": controls,
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
            "Exact finite PSD/trace, SU(2) group/metric, symbolic scalar budget and "
            "ground-bundle geometry and complete-low-space compression controls. "
            "The pinned Lean source is provenance; "
            "its seven scalar lemmas require a separate strict build. No general "
            "elliptic, min-max, nonlinear spectral, ground-derivative, full-vacuum, "
            "volume-uniform or continuum theorem is machine-certified by this run."
        ),
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    with args.output.open("x", encoding="utf-8", newline="\n") as stream:
        json.dump(report, stream, indent=2, sort_keys=True)
        stream.write("\n")
    print(f"{len(checks)}/{len(checks)} exact controls passed; wrote {args.output}")


if __name__ == "__main__":
    main()
