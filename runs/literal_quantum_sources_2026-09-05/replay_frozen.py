"""Read-only full replay of the frozen literal quantum source evidence."""

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
    if "sources" in saved:
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

    def rejects(function, *arguments):
        try:
            function(*arguments)
        except ValueError:
            return
        raise RuntimeError("A defective mathematical input or certificate was accepted")

    vacuum = sp.Matrix([sp.Rational(3, 5), sp.Rational(4, 5)])
    h = 7 * (sp.eye(2) - vacuum * vacuum.T) + 13 * sp.eye(2)
    cert = native.literal_projection_certificate(vacuum, sp.ones(2, 1), h, 13)
    cert["source_Gram"] = [["100"]]
    rejects(native.replay_literal_projection, vacuum, sp.ones(2, 1), h, 13, cert)
    rejects(native.literal_projection_certificate, vacuum, sp.ones(2, 1), h, 0)
    root = sp.Matrix([[2, 1], [1, 2]]) / 2
    # A compressed boundary inequality holds here, but the full premise fails.
    rejects(native.gaussian_source_certificate, root, sp.Matrix([1, 0]), 1)
    metric, fisher = sp.Matrix([[2, 1], [1, 2]]), sp.diag(1, 2)
    cert = native.fisher_cap_certificate(metric, fisher, 6)
    cert["slack_PSD_pivots"] = ["100", "100"]
    rejects(native.replay_fisher_cap, metric, fisher, 6, cert)
    pi0 = sp.diag(1, 0, 0, 0)
    vector = sp.Matrix([0, sp.Rational(3, 5), sp.Rational(4, 5), 0])
    h = sp.diag(0, 4, 7, 11)
    p = pi0 + vector * vector.T
    rejects(native.literal_full_domination_certificate, h, p, pi0, sp.Rational(127, 25))
    rejects(native.literal_full_domination_certificate, h, p - pi0, pi0, 1)
    cert = native.literal_full_domination_certificate(h, p, pi0, sp.Rational(175, 37))
    cert["reduced_inverse"][1][1] = "0"
    rejects(native.replay_literal_full_domination, h, p, pi0, sp.Rational(175, 37), cert)
    corrupt = copy.deepcopy(report)
    corrupt["controls"]["score"]["nonzero_connection_torus"]["exact_cross_form"] = "0"
    rejects(runner.replay_report, corrupt)
    return 8


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--manifest-only", action="store_true")
    args = parser.parse_args()
    count = check_manifest()
    if args.manifest_only:
        print(f"PASS: complete manifest, {count} files, no bytecode caches")
        return
    report = json.loads(contained("certificate.json").read_text(encoding="utf-8"))
    runner = load(
        "frozen_selected_literal_runner", "source/scripts/verify_literal_coarse_sources.py"
    )
    runner.replay_report(report)
    native = sys.modules["workhouse.literal_coarse_sources"]
    print(
        f"PASS: {len(report['sources'])} native source pins, "
        "seven check records and all six payloads",
        flush=True,
    )
    if replay_originals() != 6:
        raise RuntimeError("Six original control families are required")
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
