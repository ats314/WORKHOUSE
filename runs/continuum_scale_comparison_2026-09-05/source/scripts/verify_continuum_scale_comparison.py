"""Record precisely scoped exact scale-comparison controls from a source tree."""

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
    "src/workhouse/continuum_scale_comparison.py",
    "src/workhouse/invariants/continuum_scale_comparison.py",
    "src/workhouse/invariants/_core.py",
    "src/workhouse/continuum_scale_periodic.py",
    "scripts/verify_continuum_scale_comparison.py",
    "tests/test_continuum_scale_comparison.py",
    "paper/research_notes/G19_WILSON_FINITE_CELL_GAP_AND_BOUNDARY_FORM_20260905.md",
    "paper/research_notes/G19_WILSON_HARMONIC_BOUNDARY_COMPARISON_20260905.md",
    "paper/research_notes/G19_GAUSSIAN_OS_HISTORY_OBSERVABILITY_20260905.md",
    "paper/research_notes/G19_FORM_SCHUR_SCALE_COMPARISON_20260905.md",
    "paper/research_notes/G19_WILSON_THREE_DIMENSIONAL_HARMONIC_BOUNDARY_20260905.md",
)


def source_hashes():
    return {name: hashlib.sha256((ROOT / name).read_bytes()).hexdigest() for name in SOURCES}


def load_native():
    """Load only this tree's acceptance modules, never an installed fallback."""
    for name in ("workhouse", "workhouse.invariants"):
        package = types.ModuleType(name)
        package.__path__ = []
        sys.modules[name] = package
    modules = []
    for name, relative in (
        ("workhouse.continuum_scale_comparison", SOURCES[0]),
        ("workhouse.continuum_scale_periodic", "src/workhouse/continuum_scale_periodic.py"),
        ("workhouse.invariants._core", SOURCES[2]),
        ("workhouse.invariants.continuum_scale_comparison", SOURCES[1]),
    ):
        path = ROOT / relative
        spec = importlib.util.spec_from_file_location(name, path)
        if spec is None or spec.loader is None:
            raise RuntimeError(f"Cannot load local source: {relative}")
        module = importlib.util.module_from_spec(spec)
        sys.modules[name] = module
        spec.loader.exec_module(module)
        modules.append(module)
    return modules[0], modules[3], modules[1]


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
    native, invariants, periodic = load_native()
    controls = native.exact_scale_controls()
    periodic_controls = periodic.exact_periodic_controls()
    checks = invariants.continuum_scale_suite.run()
    if not all(check.passed for check in checks):
        raise AssertionError(checks)
    if source_hashes() != sources:
        raise RuntimeError("A source changed during verification")
    report = {
        "schema": "workhouse-continuum-scale-comparison-controls/v1",
        "passed": True,
        "exact_check_count": len(checks),
        "checks": [asdict(check) for check in checks],
        "controls": controls,
        "periodic_controls": periodic_controls,
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
            "Exact finite link-incidence, boundary, Gaussian memory, Sturm enclosure, "
            "OS covariance, invariant-polynomial, closed-form matrix and graph-frame controls. "
            "No all-size coercivity, analytic remainder, infinite-dimensional spectral or "
            "Fock theorem, nonlinear Wilson scale factorization or continuum claim is "
            "machine-certified by this run."
        ),
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    with args.output.open("x", encoding="utf-8", newline="\n") as stream:
        json.dump(report, stream, indent=2, sort_keys=True)
        stream.write("\n")
    print(f"{len(checks)}/{len(checks)} exact controls passed; wrote {args.output}")


if __name__ == "__main__":
    main()
