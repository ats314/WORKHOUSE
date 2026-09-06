"""Write fresh exact literal-source evidence from an isolated selected tree."""

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
SCHEMA = "workhouse-literal-coarse-source-controls/v1"
MODEL_NAMES = (
    "_literal_inverse_models",
    "_central_score_models",
    "_literal_vacuum_models",
    "_common_gauss_models",
    "_ground_score_models",
    "_gaussian_literal_models",
)
SOURCES = (
    *(f"src/workhouse/{name}.py" for name in MODEL_NAMES),
    "src/workhouse/literal_coarse_sources.py",
    "src/workhouse/invariants/_core.py",
    "src/workhouse/invariants/literal_coarse_sources.py",
    "scripts/verify_literal_coarse_sources.py",
    "scripts/replay_literal_coarse_sources.py",
    "tests/test_literal_coarse_sources.py",
    "paper/research_notes/G19_WILSON_LITERAL_VACUUM_COARSE_SOURCES_20260905.md",
    "paper/research_notes/G19_WILSON_COMMON_GAUSS_LITERAL_FAST_FLOOR_20260905.md",
    "paper/research_notes/G19_GROUND_MARGINAL_SCHUR_SCORE_20260905.md",
    "paper/research_notes/G19_GAUSSIAN_QUANTUM_FAST_SOURCES_20260905.md",
    "paper/research_notes/G19_TRUE_GROUND_CENTER_SCORE_OBSTRUCTION_20260905.md",
)


def source_hashes():
    return {name: hashlib.sha256((ROOT / name).read_bytes()).hexdigest() for name in SOURCES}


def load_native():
    """Load only the selected tree, including private model dependencies."""
    if sys.flags.optimize:
        raise RuntimeError("Exact controls require assertions enabled")
    sys.dont_write_bytecode = True
    for name in ("workhouse", "workhouse.invariants"):
        package = types.ModuleType(name)
        package.__path__ = []
        sys.modules[name] = package
    loaded = {}
    for name, relative in (
        *((f"workhouse.{name}", f"src/workhouse/{name}.py") for name in MODEL_NAMES),
        ("workhouse.literal_coarse_sources", "src/workhouse/literal_coarse_sources.py"),
        ("workhouse.invariants._core", "src/workhouse/invariants/_core.py"),
        (
            "workhouse.invariants.literal_coarse_sources",
            "src/workhouse/invariants/literal_coarse_sources.py",
        ),
    ):
        spec = importlib.util.spec_from_file_location(name, ROOT / relative)
        if spec is None or spec.loader is None:
            raise RuntimeError(f"Cannot load selected source {relative}")
        module = importlib.util.module_from_spec(spec)
        sys.modules[name] = module
        spec.loader.exec_module(module)
        loaded[name] = module
    return loaded["workhouse.literal_coarse_sources"], loaded[
        "workhouse.invariants.literal_coarse_sources"
    ]


def compute():
    native, invariants = load_native()
    payload = native.exact_literal_coarse_controls()
    checks = invariants.literal_coarse_suite.run()
    if len(checks) != 7 or not all(check.passed for check in checks):
        raise AssertionError(checks)
    return payload, [asdict(check) for check in checks]


def replay_report(report):
    """Read-only complete mathematical replay, with exact selected-source pins."""
    if sys.flags.optimize:
        raise RuntimeError("Exact controls require assertions enabled")
    if report.get("schema") != SCHEMA or report.get("passed") is not True:
        raise ValueError("Invalid certificate schema or status")
    before = source_hashes()
    if report.get("sources") != before:
        raise ValueError("Certificate source pins do not match the selected tree")
    payload, checks = compute()
    # Normalize tuples in dataclasses exactly as the JSON writer does.
    checks = json.loads(json.dumps(checks))
    if (
        report.get("controls") != payload
        or report.get("checks") != checks
        or report.get("exact_check_count") != 7
    ):
        raise ValueError("Certificate differs from full exact recomputation")
    if before != source_hashes():
        raise RuntimeError("A selected source changed during replay")
    return True


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    if args.output.exists():
        raise FileExistsError("Choose a fresh output path; existing evidence is preserved")
    if sys.flags.optimize:
        raise RuntimeError("Exact controls require assertions enabled")
    before = source_hashes()
    payload, checks = compute()
    if before != source_hashes():
        raise RuntimeError("A selected source changed during verification")
    report = {
        "schema": SCHEMA,
        "passed": True,
        "exact_check_count": len(checks),
        "checks": checks,
        "controls": payload,
        "sources": before,
        "runtime": {
            "python": sys.version,
            "sympy": sympy.__version__,
            "system": platform.system(),
            "architecture": platform.machine(),
            "completed_utc": datetime.now(UTC).isoformat(),
            "assertions_enabled": True,
        },
        "verification_scope": (
            "Exact finite weighted-vacuum, tensor and SO(3) projection, intrinsic-score, "
            "noncommuting Gaussian source, complete finite-window, inverse-energy and "
            "central Riccati/Haar controls. Full "
            "Wilson localization, countable tensorization, Fock density, operator "
            "monotonicity and all-sector results are analytic, not machine-certified. "
            "The actual Wilson central obstruction uses its analytic ground equation "
            "and energy bound. No interacting-volume, OS-history, unregulated-vacuum "
            "or continuum claim."
        ),
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    with args.output.open("x", encoding="utf-8", newline="\n") as stream:
        json.dump(report, stream, indent=2, sort_keys=True)
        stream.write("\n")
    print(f"7/7 exact checks passed; wrote {args.output}")


if __name__ == "__main__":
    main()
