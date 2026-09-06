"""Read-only full replay of the frozen endpoint and local source evidence."""

import argparse
import copy
import hashlib
import importlib.util
import json
import os
import sys
from pathlib import Path

sys.dont_write_bytecode = True
os.environ["PYTHONDONTWRITEBYTECODE"] = "1"
if sys.flags.optimize:
    raise RuntimeError("Assertions must be enabled; do not use python -O")
ROOT = Path(__file__).resolve().parent


class RejectNumericalImports:
    def find_spec(self, fullname, path=None, target=None):
        if fullname.split(".", 1)[0] in {"numpy", "scipy"}:
            raise ImportError("Undeclared numerical dependency forbidden: " + fullname)
        return None


sys.meta_path.insert(0, RejectNumericalImports())


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def contained(relative):
    path = (ROOT / relative).resolve()
    if path == ROOT or not path.is_relative_to(ROOT):
        raise RuntimeError("Invalid run-relative path: " + relative)
    return path


def check_manifest():
    recorded = {}
    for line in contained("SHA256SUMS").read_text(encoding="utf-8").splitlines():
        expected, relative = line.split("  ", 1)
        if relative in recorded:
            raise RuntimeError("Duplicate manifest entry: " + relative)
        if digest(contained(relative)) != expected:
            raise RuntimeError("Manifest digest mismatch: " + relative)
        recorded[relative] = expected
    actual = {
        p.relative_to(ROOT).as_posix()
        for p in ROOT.rglob("*")
        if p.is_file() and p.name != "SHA256SUMS"
    }
    if any("__pycache__" in p or p.endswith((".pyc", ".pyo")) for p in actual):
        raise RuntimeError("Bytecode caches are forbidden in a frozen run")
    if actual != set(recorded):
        raise RuntimeError("Manifest file-set mismatch: " + str(sorted(actual ^ set(recorded))))
    return len(recorded)


def load(name, relative):
    spec = importlib.util.spec_from_file_location(name, contained(relative))
    if spec is None or spec.loader is None:
        raise RuntimeError("Cannot load pinned source: " + relative)
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


def expected_payload(saved):
    if "controls" in saved:
        return saved["controls"]
    return {key: value for key, value in saved.items() if key != "source_sha256"}


def replay_originals():
    cases = json.loads(contained("provenance/original_cases.json").read_text(encoding="utf-8"))
    for row in cases:
        before = {name: digest(contained(name)) for name in row["source_pins"]}
        if before != row["source_pins"]:
            raise RuntimeError("Original declared source pin mismatch: " + row["family"])
        saved = json.loads(contained(row["report"]).read_text(encoding="utf-8"))
        module = load("original_literal_control_" + row["family"], row["source"])
        if module.controls() != expected_payload(saved):
            raise RuntimeError("Original complete exact payload differs: " + row["family"])
        if before != {name: digest(contained(name)) for name in before}:
            raise RuntimeError("Original source changed during replay")
    print(f"PASS: {len(cases)} original complete payloads and all declared source pins", flush=True)
    return len(cases)


def negative_controls(native, runner, report):
    import sympy as sp

    count = 0

    def rejects(function, *arguments):
        nonlocal count
        try:
            function(*arguments)
        except (ValueError, AssertionError):
            count += 1
            return
        raise RuntimeError("A defective mathematical input or certificate was accepted")

    t = sp.diag(1, sp.Rational(1, 2), sp.Rational(1, 8))
    j = sp.eye(3)[:, [0, 1]]
    d, z = sp.Rational(1, 8), sp.Rational(1, 2)
    cert = native.finite_endpoint_certificate(t, j, d, z)
    cert["full_count"] += 1
    rejects(native.replay_finite_endpoint, t, j, d, z, cert)
    rejects(native.finite_endpoint_certificate, t, sp.eye(3)[:, [1, 2]], d, z)
    rejects(native.finite_endpoint_certificate, t, j, sp.Rational(1, 16), z)
    rejects(native.two_lag_count_certificate, sp.eye(2) / 2, sp.eye(2) / 3, d, d)
    full, bad = sp.diag(0, 4, 2, 2, 2), sp.diag(1, 0, 0, 0, 0)
    rejects(native.local_gradient_certificate, full, bad, 2)
    positive = sp.Matrix([[2, 1], [1, 1]])
    rejects(native.covariant_source_floor_certificate, positive, sp.eye(2), sp.Matrix([1, 0]), 1)
    k, pc = sp.diag(0, 2, 3, 0), sp.diag(1, 1, 1, 0)
    b = sp.Matrix([[1, 0], [0, 1], [0, sp.I], [0, 0]])
    cert = native.covariant_source_floor_certificate(k, pc, b, 1)
    cert["source_Gram"][1][1] = "1"
    rejects(native.replay_covariant_source_floor, k, pc, b, 1, cert)
    corrupt = copy.deepcopy(report)
    corrupt["controls"]["endpoint"]["endpoint_and_two_lag"]["threshold_counts"][-1][
        "full_count"
    ] += 1
    rejects(runner.replay_report, corrupt)
    corrupt = copy.deepcopy(report)
    key = next(iter(corrupt["sources"]))
    corrupt["sources"][key] = "0" * 64
    rejects(runner.replay_report, corrupt)
    return count


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--manifest-only", action="store_true")
    args = parser.parse_args()
    count = check_manifest()
    if args.manifest_only:
        print(f"PASS: complete manifest, {count} files, no bytecode caches")
        return
    report = json.loads(contained("certificate.json").read_text(encoding="utf-8"))
    runner = load("frozen_selected_literal_runner", "source/scripts/verify_endpoint_window.py")
    runner.replay_report(report)
    native = sys.modules["workhouse.endpoint_window"]
    print(
        f"PASS: {len(report['sources'])} native source pins, "
        "ten check records and all five payloads",
        flush=True,
    )
    if replay_originals() != 5:
        raise RuntimeError("Five original control families are required")
    import runpy

    original = contained(
        "original_tree/outputs/wilson_complete_band_20260905/next_scale/next_nonlinear/next_full_window_comparison/replay_literal_endpoint_window.py"
    )
    old_argv = sys.argv
    try:
        sys.argv = [
            str(original),
            str(original.with_name("literal_endpoint_window_controls_frozen.json")),
        ]
        runpy.run_path(str(original), run_name="__main__")
    finally:
        sys.argv = old_argv
    print(
        f"PASS: {negative_controls(native, runner, report)} "
        "defective inputs or certificates rejected",
        flush=True,
    )
    if any(name.split(".", 1)[0] in {"numpy", "scipy"} for name in sys.modules):
        raise RuntimeError("An undeclared numerical dependency was imported")
    if check_manifest() != count:
        raise RuntimeError("Frozen file set changed during replay")
    print(f"PASS: {count} pinned files unchanged; NumPy/SciPy imports blocked", flush=True)
    print(
        "Scope: exact finite controls; full operator, Wilson localization, countable product, "
        "Fock and limiting score claims rely on the pinned analytic proofs."
    )


if __name__ == "__main__":
    main()
