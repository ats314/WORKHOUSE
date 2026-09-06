"""Read-only complete replay of the exact endpoint-window research control."""

from __future__ import annotations

import argparse
import copy
import hashlib
import importlib.abc
import importlib.util
import json
import sys
from pathlib import Path


class NoNumericalDependencies(importlib.abc.MetaPathFinder):
    def find_spec(self, fullname, path=None, target=None):
        if fullname.split(".")[0] in {"numpy", "scipy"}:
            raise ImportError("Forbidden numerical dependency: " + fullname)


def main():
    if sys.flags.optimize:
        raise RuntimeError("Exact replay requires assertions enabled")
    sys.dont_write_bytecode = True
    sys.meta_path.insert(0, NoNumericalDependencies())
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("certificate", type=Path)
    args = parser.parse_args()
    here = Path(__file__).resolve()
    repo = here.parents[5]
    checker = here.with_name("check_literal_endpoint_window.py")
    paths = (
        checker,
        here.with_name("LITERAL_ENDPOINT_COMPLETE_WINDOW.md"),
        repo / "paper/research_notes/G18_EXCITED_WINDOW_OPERATOR_BRIDGE_20260904.md",
        repo / "paper/research_notes/G19_WILSON_LITERAL_VACUUM_COARSE_SOURCES_20260905.md",
        repo / "paper/research_notes/G19_WILSON_COMMON_GAUSS_LITERAL_FAST_FLOOR_20260905.md",
        repo / "paper/research_notes/G19_TRUE_GROUND_CENTER_SCORE_OBSTRUCTION_20260905.md",
    )
    hashes = {
        path.relative_to(repo).as_posix(): hashlib.sha256(path.read_bytes()).hexdigest()
        for path in paths
    }
    report = json.loads(args.certificate.read_text(encoding="utf-8"))
    if report.get("passed") is not True or report.get("source_sha256") != hashes:
        raise ValueError("Certificate status or exact source pins differ")
    spec = importlib.util.spec_from_file_location("endpoint_control", checker)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    expected = module.controls()

    def accept(payload):
        if payload != expected:
            raise ValueError("Mathematical payload differs from exact recomputation")

    accept(report["controls"])
    corrupted = copy.deepcopy(expected)
    corrupted["endpoint_and_two_lag"]["threshold_counts"][-1]["full_count"] = 2
    try:
        accept(corrupted)
    except ValueError:
        pass
    else:
        raise AssertionError("A corrupted complete spectral count was accepted")
    if hashes != {
        path.relative_to(repo).as_posix(): hashlib.sha256(path.read_bytes()).hexdigest()
        for path in paths
    }:
        raise RuntimeError("Pinned source changed during replay")
    print("PASS: six source pins, all four payloads, corruption rejection, no NumPy/SciPy")


if __name__ == "__main__":
    main()
