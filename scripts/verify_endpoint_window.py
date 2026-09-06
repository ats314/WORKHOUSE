"""Write fresh exact endpoint/local-source evidence from an isolated selected tree."""

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
SCHEMA = "workhouse-endpoint-local-source-controls/v1"
MODEL_NAMES = (
    "_endpoint_models",
    "_localized_score_models",
    "_local_gradient_models",
    "_covariant_path_models",
    "_fourier_alias_models",
)
SOURCES = (
    *(f"src/workhouse/{name}.py" for name in MODEL_NAMES),
    "src/workhouse/endpoint_window.py",
    "src/workhouse/invariants/_core.py",
    "src/workhouse/invariants/endpoint_window.py",
    "scripts/verify_endpoint_window.py",
    "scripts/replay_endpoint_window.py",
    "tests/test_endpoint_window.py",
    "paper/research_notes/G19_LITERAL_ENDPOINT_COMPLETE_WINDOW_20260905.md",
    "paper/research_notes/G19_TRUE_GROUND_LOCALIZED_WILSON_SCORE_20260905.md",
    "paper/research_notes/G19_LOCAL_GRADIENT_EXCITATION_SUPPORT_20260905.md",
    "paper/research_notes/G19_LOCAL_COVARIANT_AVERAGED_PATH_SOURCES_20260905.md",
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
        ("workhouse.endpoint_window", "src/workhouse/endpoint_window.py"),
        ("workhouse.invariants._core", "src/workhouse/invariants/_core.py"),
        (
            "workhouse.invariants.endpoint_window",
            "src/workhouse/invariants/endpoint_window.py",
        ),
    ):
        spec = importlib.util.spec_from_file_location(name, ROOT / relative)
        if spec is None or spec.loader is None:
            raise RuntimeError(f"Cannot load selected source {relative}")
        module = importlib.util.module_from_spec(spec)
        sys.modules[name] = module
        spec.loader.exec_module(module)
        loaded[name] = module
    return loaded["workhouse.endpoint_window"], loaded["workhouse.invariants.endpoint_window"]


def compute():
    native, invariants = load_native()
    payload = native.exact_endpoint_window_controls()
    checks = invariants.endpoint_window_suite.run()
    if len(checks) != 10 or not all(check.passed for check in checks):
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
        or report.get("exact_check_count") != 10
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
            "Exact finite endpoint/source/moment matrices, Markov Taylor and marginal "
            "counterexamples, conditional scalar budget, SU2 leading Lie/Gaussian algebra "
            "complete finite centered tensor-gradient forms, gauge-covariant path/cochain "
            "matrices, and full Q(i) Fourier source bounds. This does not certify "
            "Wilson ground remainders, infinite spectra, all-copy or interacting limits."
        ),
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    with args.output.open("x", encoding="utf-8", newline="\n") as stream:
        json.dump(report, stream, indent=2, sort_keys=True)
        stream.write("\n")
    print(f"10/10 exact checks passed; wrote {args.output}")


if __name__ == "__main__":
    main()
