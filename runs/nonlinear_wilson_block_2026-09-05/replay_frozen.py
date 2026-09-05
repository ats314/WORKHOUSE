"""Read-only exact replay of the frozen nonlinear Wilson block package."""

import argparse
import hashlib
import importlib.util
import json
import os
import sys
import types
from dataclasses import asdict
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
    actual = {p.relative_to(ROOT).as_posix() for p in ROOT.rglob("*")
              if p.is_file() and p.name != "SHA256SUMS"}
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


def normalize(value):
    return json.loads(json.dumps(value))


def negative_controls(native):
    import sympy as s

    b, q = s.Matrix([[1, 1], [1, 1]]) / 10, s.diag(2, 1)
    certificate = native.trace_psd_certificate(b, q)
    certificate["margin"] = "0"
    try:
        native.replay_trace_certificate(b, q, certificate)
    except ValueError:
        pass
    else:
        raise RuntimeError("Corrupt trace certificate accepted")
    arguments = (2, 10, 3, s.Rational(7, 20), s.Rational(1, 10))
    certificate = native.vertical_spectral_budget(*arguments)
    certificate["cap_margin"] = "1000000"
    try:
        native.replay_spectral_budget(*arguments, certificate)
    except ValueError:
        pass
    else:
        raise RuntimeError("Corrupt spectral budget accepted")
    columns = s.Matrix([[s.Rational(3, 5), 0], [0, s.Rational(3, 5)],
                         [s.Rational(4, 5), 0], [0, s.Rational(4, 5)]])
    hamiltonian, retained = s.diag(11, 15, 18, 23), columns * columns.T
    low = s.diag(1, 1, 0, 0)
    arguments = (hamiltonian, retained, low, 11, 7, s.Rational(16, 25))
    certificate = native.compression_leakage_certificate(*arguments)
    certificate["compressed_floor"] = "7"
    try:
        native.replay_compression_certificate(*arguments, certificate)
    except ValueError:
        pass
    else:
        raise RuntimeError("Corrupt compression floor accepted")
    try:
        native.compression_leakage_certificate(hamiltonian, retained,
                                               s.diag(1, 0, 0, 0), 11, 7,
                                               s.Rational(16, 25))
    except ValueError:
        pass
    else:
        raise RuntimeError("Incomplete low spectral space accepted")
    return 4


def check_lean_provenance():
    build = json.loads(contained("lean/canonical_build_result.json").read_text(encoding="utf-8"))
    original = json.loads(contained("lean/original_scalar_build_result.json").read_text(encoding="utf-8"))
    if not build["success"] or len(build["modules"]) != 7 or not original["success"]:
        raise RuntimeError("Strict Lean build evidence is incomplete")
    for row in build["modules"]:
        if row["returncode"] or "-DwarningAsError=true" not in row["command"]:
            raise RuntimeError("A canonical Lean module failed strict acceptance")
        if digest(contained("source/lean/" + row["module"] + ".lean")) != row["source_sha256"]:
            raise RuntimeError("Canonical strict Lean source pin mismatch")
    if digest(contained("source/lean/GlobalWilsonVertical.lean")) != original["source_sha256"]:
        raise RuntimeError("Original scalar Lean source pin mismatch")
    if original["source_sha256"] != digest(contained("source/lean/Workhouse/GlobalWilsonVertical.lean")):
        raise RuntimeError("Canonical and originally compiled scalar Lean differ")
    for name, key in (("lean-toolchain", "lean_toolchain_sha256"),
                      ("lake-manifest.json", "lake_manifest_sha256")):
        if digest(contained("source/lean/" + name)) != build[key] or build[key] != original[key]:
            raise RuntimeError("Lean dependency metadata pin mismatch")
    if build["compiler_sha256"] != original["compiler_sha256"]:
        raise RuntimeError("Strict builds used different compiler pins")
    print("PASS: seven strict canonical Lean module source pins and original seven scalar lemmas",
          flush=True)
    print("Lean scope: captured compiler evidence; this Python replay does not rerun Lean",
          flush=True)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--manifest-only", action="store_true")
    args = parser.parse_args()
    count = check_manifest()
    if args.manifest_only:
        print(f"PASS: complete manifest, {count} files, no bytecode caches")
        return
    certificate = json.loads(contained("certificate.json").read_text(encoding="utf-8"))
    if certificate["schema"] != "workhouse-nonlinear-wilson-block-controls/v1":
        raise RuntimeError("Unexpected native certificate schema")
    for name, expected in certificate["sources"].items():
        if digest(contained("source/" + name)) != expected:
            raise RuntimeError("Native source pin mismatch: " + name)
    for name in ("workhouse", "workhouse.invariants"):
        package = types.ModuleType(name)
        package.__path__ = []
        sys.modules[name] = package
    native = load("workhouse.nonlinear_wilson_block", "source/src/workhouse/nonlinear_wilson_block.py")
    load("workhouse.invariants._core", "source/src/workhouse/invariants/_core.py")
    invariants = load("workhouse.invariants.nonlinear_wilson_block",
                      "source/src/workhouse/invariants/nonlinear_wilson_block.py")
    if normalize(native.exact_nonlinear_controls()) != certificate["controls"]:
        raise RuntimeError("Native exact payload differs")
    checks = normalize([asdict(check) for check in invariants.nonlinear_wilson_suite.run()])
    if checks != certificate["checks"] or not all(check["passed"] for check in checks):
        raise RuntimeError("Native invariant records differ")
    if not certificate["passed"] or certificate["exact_check_count"] != len(checks) or len(checks) != 5:
        raise RuntimeError("Native count/status differs")
    print("PASS: all nine source pins, five native checks and their complete exact payloads", flush=True)

    # Keep the original outputs-relative layout intact, including all source
    # paths in the original certificate. No monkeypatch or source rewrite.
    original_base = "original_tree/outputs/wilson_complete_band_20260905/next_scale/next_nonlinear/"
    original_replay = load("original_global_vertical_replay",
                            original_base + "replay_global_wilson_vertical_barrier.py")
    original_replay.main()
    for stem in ("ground_bundle_geometry", "actual_complement_mechanism"):
        module = load("original_" + stem, "check_" + stem + ".py")
        expected = json.loads(contained("check_" + stem + ".json").read_text(encoding="utf-8"))
        if normalize(module.controls()) != expected:
            raise RuntimeError("Original exact payload differs: " + stem)
    print("PASS: all three unchanged original control programs and saved payloads", flush=True)
    print(f"PASS: {negative_controls(native)} corrupted or incomplete mathematical inputs rejected",
          flush=True)
    check_lean_provenance()
    if any(name.split(".", 1)[0] in {"numpy", "scipy"} for name in sys.modules):
        raise RuntimeError("An undeclared numerical dependency was imported")
    if check_manifest() != count:
        raise RuntimeError("Frozen file set changed during replay")
    print(f"PASS: all {count} pinned files unchanged; NumPy/SciPy imports blocked", flush=True)
    print("Scope: finite exact controls and captured scalar Lean build; general nonlinear "
          "operator proofs and open multiblock/continuum hypotheses remain distinct")


if __name__ == "__main__":
    main()
