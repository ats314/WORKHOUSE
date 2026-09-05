"""Read-only exact replay of the frozen continuum scale-comparison package."""

import argparse
import hashlib
import importlib.util
import json
import os
import shutil
import subprocess
import sys
import tempfile
import types
from dataclasses import asdict
from pathlib import Path

sys.dont_write_bytecode = True
if sys.flags.optimize:
    raise RuntimeError("Assertions must be enabled; do not use python -O")
ROOT = Path(__file__).resolve().parent


class RejectNumericalImports:
    def find_spec(self, fullname, path=None, target=None):
        if fullname.split(".", 1)[0] in {"numpy", "scipy"}:
            raise ImportError(f"Undeclared numerical dependency forbidden: {fullname}")
        return None


sys.meta_path.insert(0, RejectNumericalImports())


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def contained(relative):
    path = (ROOT / relative).resolve()
    if not path.is_relative_to(ROOT) or path == ROOT:
        raise RuntimeError(f"Invalid run-relative path: {relative}")
    return path


def check_manifest():
    recorded = {}
    for line in (ROOT / "SHA256SUMS").read_text(encoding="utf-8").splitlines():
        expected, relative = line.split("  ", 1)
        if relative in recorded:
            raise RuntimeError(f"Duplicate manifest entry: {relative}")
        if digest(contained(relative)) != expected:
            raise RuntimeError(f"Manifest digest mismatch: {relative}")
        recorded[relative] = expected
    actual = {p.relative_to(ROOT).as_posix() for p in ROOT.rglob("*")
              if p.is_file() and p.name != "SHA256SUMS"}
    if any("__pycache__" in p or p.endswith((".pyc", ".pyo")) for p in actual):
        raise RuntimeError("Bytecode caches are forbidden in the frozen run")
    if actual != set(recorded):
        raise RuntimeError(f"Manifest file-set mismatch: {sorted(actual ^ set(recorded))}")
    return len(actual)


def load(name, relative):
    spec = importlib.util.spec_from_file_location(name, contained(relative))
    if spec is None or spec.loader is None:
        raise RuntimeError(f"Cannot load pinned source: {relative}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


def normalize(value):
    return json.loads(json.dumps(value))


def compare_original(value, relative):
    expected = json.loads(contained(relative).read_text(encoding="utf-8"))
    if normalize(value) != expected:
        raise RuntimeError(f"Original exact-control payload mismatch: {relative}")


ISOLATED_BOOTSTRAP = r'''
import runpy, sys
sys.dont_write_bytecode = True
if sys.flags.optimize:
    raise RuntimeError("Assertions must be enabled")
class RejectNumericalImports:
    def find_spec(self, fullname, path=None, target=None):
        if fullname.split(".", 1)[0] in {"numpy", "scipy"}:
            raise ImportError("Undeclared numerical dependency forbidden: " + fullname)
        return None
sys.meta_path.insert(0, RejectNumericalImports())
runpy.run_path(sys.argv[1], run_name="__main__")
if any(n.split(".", 1)[0] in {"numpy", "scipy"} for n in sys.modules):
    raise RuntimeError("Numerical dependency imported")
'''


def isolated_original(script, result):
    # Both scripts write relative to __file__; preserve the originals by executing
    # a byte-identical source in a fresh, temporary directory outside the run.
    with tempfile.TemporaryDirectory(prefix="workhouse-scale-original-") as directory:
        temporary = Path(directory)
        copy = temporary / script
        shutil.copyfile(contained(script), copy)
        if digest(copy) != digest(contained(script)):
            raise RuntimeError("Isolated source copy differs")
        env = dict(os.environ, PYTHONDONTWRITEBYTECODE="1")
        process = subprocess.run(
            [sys.executable, "-B", "-c", ISOLATED_BOOTSTRAP, str(copy)],
            cwd=temporary, env=env, capture_output=True, text=True, check=False,
        )
        if process.returncode:
            raise RuntimeError(f"Isolated {script} failed:\n{process.stderr}")
        compare_original(json.loads((temporary / result).read_text(encoding="utf-8")), result)
        if digest(copy) != digest(contained(script)):
            raise RuntimeError("An isolated original source changed during replay")


def negative_controls(native):
    import sympy as s

    fast = s.Matrix([[7, 2], [2, 5]])
    cross = s.Matrix([[2, -1], [1, 3]])
    static = s.Matrix([[2, 1], [1, 4]])
    for failure in ("interval", "index", "margin", "missing"):
        certificates = native.gaussian_certificates()
        if failure == "interval":
            certificates[0]["lambda_interval"] = ["1/10", "1/5"]
        elif failure == "index":
            certificates[1]["j"] = 1
        elif failure == "margin":
            certificates[0]["strict_lower_control"] = "0"
        else:
            certificates.pop()
        try:
            native.replay_gaussian_enclosures(fast, cross, static, 3, certificates)
        except ValueError:
            pass
        else:
            raise RuntimeError(f"Corrupt spectral certificate accepted: {failure}")
    hamiltonian = s.Matrix([[s.Rational(1, 2), 0, s.Rational(1, 2)],
                            [0, s.Rational(1, 4), 0],
                            [s.Rational(1, 2), 0, s.Rational(1, 2)]])
    bad_window = s.diag(1, 0, 0)
    try:
        native.graph_source_control(hamiltonian, 2, bad_window,
                                    s.Rational(1, 4), s.Rational(1, 2))
    except ValueError:
        pass
    else:
        raise RuntimeError("Nonreducing graph-source window accepted")
    return 5


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--manifest-only", action="store_true")
    args = parser.parse_args()
    count = check_manifest()
    if args.manifest_only:
        print(f"PASS: complete manifest, {count} files, no bytecode caches")
        return
    report = json.loads(contained("certificate.json").read_text(encoding="utf-8"))
    if report["schema"] != "workhouse-continuum-scale-comparison-controls/v1":
        raise RuntimeError("Unexpected native certificate schema")
    for relative, expected in report["sources"].items():
        if digest(contained("source/" + relative)) != expected:
            raise RuntimeError(f"Runner-source hash mismatch: {relative}")
    for name in ("workhouse", "workhouse.invariants"):
        package = types.ModuleType(name)
        package.__path__ = []
        sys.modules[name] = package
    native = load("workhouse.continuum_scale_comparison",
                  "source/src/workhouse/continuum_scale_comparison.py")
    periodic = load("workhouse.continuum_scale_periodic",
                    "source/src/workhouse/continuum_scale_periodic.py")
    load("workhouse.invariants._core", "source/src/workhouse/invariants/_core.py")
    invariants = load("workhouse.invariants.continuum_scale_comparison",
                      "source/src/workhouse/invariants/continuum_scale_comparison.py")
    if normalize(native.exact_scale_controls()) != report["controls"]:
        raise RuntimeError("Native scale payload differs from saved certificate")
    if normalize(periodic.exact_periodic_controls()) != report["periodic_controls"]:
        raise RuntimeError("Native periodic payload differs from saved certificate")
    checks = normalize([asdict(check) for check in invariants.continuum_scale_suite.run()])
    if checks != report["checks"] or not all(check["passed"] for check in checks):
        raise RuntimeError("Native invariant records differ from saved certificate")
    if not report["passed"] or report["exact_check_count"] != len(checks) or len(checks) != 7:
        raise RuntimeError("Native acceptance count/status mismatch")
    print(f"PASS: all {len(report['sources'])} source hashes and seven native checks/payloads",
          flush=True)
    for script, function, result in (
        ("check_cell_complex_hessian.py", "controls", "check_cell_complex_hessian.json"),
        ("check_harmonic_incidence_comparison.py", "exact_controls",
         "check_harmonic_incidence_comparison.json"),
        ("check_closed_form_schur.py", "controls", "check_closed_form_schur.json"),
        ("check_periodic_3d_fast_bound.py", "controls", "check_periodic_3d_fast_bound.json"),
        ("check_vacuum_projection_mismatch.py", "controls",
         "check_vacuum_projection_mismatch.json"),
    ):
        original = load("original_" + Path(script).stem, script)
        compare_original(getattr(original, function)(), result)
        print(f"PASS: original {script} exact payload", flush=True)
    isolated_original("check_gaussian_memory.py", "check_gaussian_memory.json")
    isolated_original("check_gaussian_os_observability.py",
                      "gaussian_os_observability_controls.json")
    print("PASS: both writing Gaussian originals replayed in fresh isolated directories",
          flush=True)
    print(f"PASS: {negative_controls(native)} corrupt certificate/window controls rejected",
          flush=True)
    if any(n.split(".", 1)[0] in {"numpy", "scipy"} for n in sys.modules):
        raise RuntimeError("An undeclared numerical dependency was imported")
    if check_manifest() != count:
        raise RuntimeError("Frozen file set changed during replay")
    print(f"PASS: all {count} pinned files unchanged; NumPy/SciPy imports blocked", flush=True)
    print("Scope: exact finite controls; all-size analytic proofs and open nonlinear "
          "Wilson/continuum hypotheses are distinguished in the pinned notes")


if __name__ == "__main__":
    main()
