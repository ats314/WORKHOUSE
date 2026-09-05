"""Record exact finite creator-parent controls and independently replay their certificates."""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import platform
import subprocess
import sys
from dataclasses import asdict
from datetime import UTC, datetime
from pathlib import Path

import sympy

from workhouse.invariants.wilson_creator_parent import (
    creator_parent_suite,
    finite_models,
    scalar_majorants,
)
from workhouse.wilson_creator_parent import disjoint_condition_number_control, replay_model

ROOT = Path(__file__).resolve().parents[1]
SOURCES = (
    "scripts/verify_wilson_creator_parent.py",
    "src/workhouse/wilson_creator_parent.py",
    "src/workhouse/rooted_creator.py",
    "src/workhouse/invariants/wilson_creator_parent.py",
    "src/workhouse/invariants/__init__.py",
    "tests/test_wilson_creator_parent.py",
    "paper/research_notes/G18_WILSON_CREATOR_PARENT_AND_SPECTRAL_FLOW_20260905.md",
)


def source_hashes():
    return {name: hashlib.sha256((ROOT / name).read_bytes()).hexdigest() for name in SOURCES}


def git_value(*arguments):
    process = subprocess.run(
        ["git", "-c", f"safe.directory={ROOT.as_posix()}", *arguments],
        cwd=ROOT,
        capture_output=True,
        text=True,
        encoding="utf-8",
        check=False,
    )
    return process.stdout.strip() if process.returncode == 0 else None


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    if args.output.exists():
        raise FileExistsError("Choose a fresh output path; existing evidence is preserved")
    if sys.flags.optimize:
        raise RuntimeError("Exact controls require assertions enabled; do not use Python -O")
    before = source_hashes()
    started = datetime.now(UTC).isoformat()
    checks = list(creator_parent_suite.run())
    if not checks or not all(result.passed for result in checks):
        raise AssertionError(checks)
    models = finite_models()
    replays = [replay_model(model) for model in models]
    if source_hashes() != before:
        raise RuntimeError("A source changed during verification; rerun after it is stable")
    report = {
        "schema": "workhouse-wilson-creator-parent/v1",
        "passed": True,
        "exact_check_count": len(checks),
        "checks": [asdict(result) for result in checks],
        "models": models,
        "independent_replays": replays,
        "psd_certificate_count": sum(
            3 + len(m["idempotent_singular_controls"]) + len(m["overlap_commutator_controls"])
            for m in models
        ),
        "scalar_majorants": scalar_majorants(),
        "global_similarity_negative_control": disjoint_condition_number_control(),
        "verification_scope": (
            "The passed field concerns five exact native controls, six fixed finite tensor "
            "models, rational sufficient-bound arithmetic and the explicit factorized "
            "negative-control family. It does not machine-certify the general Hilbert-space "
            "parent theorem, spectral flow, GNS identification, or a physical Wilson excited gap."
        ),
        "sources": before,
        "git": {
            "base_revision": git_value("rev-parse", "HEAD"),
            "branch": git_value("branch", "--show-current"),
        },
        "runtime": {
            "started_utc": started,
            "completed_utc": datetime.now(UTC).isoformat(),
            "python": sys.version,
            "implementation": platform.python_implementation(),
            "sympy": sympy.__version__,
            "assertions_enabled": True,
        },
        "machine": {
            "system": platform.system(),
            "release": platform.release(),
            "architecture": platform.machine(),
            "logical_cpu_count": os.cpu_count(),
        },
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    with args.output.open("x", encoding="utf-8", newline="\n") as stream:
        stream.write(json.dumps(report, indent=2, sort_keys=True, default=str) + "\n")
    print(
        f"{len(checks)}/{len(checks)} exact native controls and 81 PSD certificates passed; "
        f"wrote {args.output}"
    )


if __name__ == "__main__":
    main()
