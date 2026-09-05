"""Read-only replay of pinned native and original continuum-block controls."""
import argparse
import ast
import hashlib
import importlib.util
import json
import math
import sys
import types
from dataclasses import asdict
from fractions import Fraction
from pathlib import Path

sys.dont_write_bytecode = True
if sys.flags.optimize:
    raise RuntimeError("Assertions must be enabled; do not use python -O")
ROOT = Path(__file__).resolve().parent


class RejectNumericalProposalImports:
    """The frozen acceptance path must work without undeclared numerical libraries."""

    def find_spec(self, fullname, path=None, target=None):
        if fullname.split(".", 1)[0] in {"numpy", "scipy"}:
            raise ImportError(
                f"Numerical proposal dependency forbidden during exact replay: {fullname}"
            )
        return None


sys.meta_path.insert(0, RejectNumericalProposalImports())


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
        path = contained(relative)
        if digest(path) != expected:
            raise RuntimeError(f"Manifest digest mismatch: {relative}")
        recorded[relative] = expected
    actual = {
        p.relative_to(ROOT).as_posix()
        for p in ROOT.rglob("*") if p.is_file() and p.name != "SHA256SUMS"
    }
    if any("__pycache__" in name or name.endswith((".pyc", ".pyo")) for name in actual):
        raise RuntimeError("Bytecode caches are not permitted in this frozen run")
    if actual != set(recorded):
        raise RuntimeError(f"Manifest file-set mismatch: {sorted(actual ^ set(recorded))}")
    return len(recorded)


def load(name, relative):
    path = contained(relative)
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"Cannot load pinned source: {relative}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


def payload(report, field):
    result = report
    for key in field.split("."):
        result = result[key]
    return result


def compare(value, filename):
    expected = json.loads(contained(filename).read_text(encoding="utf-8"))
    if value != expected:
        raise RuntimeError(f"Original exact-control payload changed: {filename}")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--manifest-only", action="store_true")
    args = parser.parse_args()
    count = check_manifest()
    if args.manifest_only:
        print(f"PASS: complete manifest, {count} files, no bytecode caches")
        return

    report = json.loads((ROOT / "certificate.json").read_text(encoding="utf-8"))
    config = json.loads((ROOT / "replay_config.json").read_text(encoding="utf-8"))
    for relative, expected in report["sources"].items():
        if digest(contained("source/" + relative)) != expected:
            raise RuntimeError(f"Runner-source digest mismatch: {relative}")

    # An empty package path prevents fallback to the installed workhouse package.
    package = types.ModuleType("workhouse")
    package.__path__ = []
    sys.modules["workhouse"] = package
    for entry in config["payloads"]:
        print(f"Replaying pinned {entry['module']} ...", flush=True)
        module = load(entry["module"], entry["source"])
        value = getattr(module, entry["function"])()
        if value != payload(report, entry["field"]):
            raise RuntimeError(f"Native payload mismatch: {entry['field']}")
    rotor = sys.modules["workhouse.continuum_wilson_rotor"]
    if rotor.rotor_certificates() != report["rotor_certificates"]:
        raise RuntimeError("Native embedded rotor certificates differ from the saved report")
    package = types.ModuleType("workhouse.invariants")
    package.__path__ = []
    sys.modules["workhouse.invariants"] = package
    load("workhouse.invariants._core", "source/src/workhouse/invariants/_core.py")
    invariants = load(
        "workhouse.invariants.continuum_wilson_block",
        "source/src/workhouse/invariants/continuum_wilson_block.py",
    )
    checks = json.loads(json.dumps([
        asdict(check) for check in invariants.continuum_block_suite.run()
    ]))
    if checks != report["checks"] or not all(check["passed"] for check in checks):
        raise RuntimeError("Pinned invariant-suite results differ from the saved report")
    print("PASS: native exact payloads and every runner source hash", flush=True)
    print(f"PASS: {len(checks)} pinned invariant checks and embedded rotor certificates",
          flush=True)

    # Recompute original independent controls through calculation functions;
    # do not invoke generation entry points that write JSON files.
    original = load("check_strip_born_oppenheimer_audit", "check_strip_born_oppenheimer_audit.py")
    compare({
        "scope": original.__doc__,
        "metric_jets": original.metric_jet_controls(),
        "lie_gaussian_contractions": original.lie_gaussian_controls(),
        "physical_gauss_cancellation": original.polynomial_gauss_controls(),
        "symbolic_scalar_constants": original.scalar_controls(),
    }, "strip_born_oppenheimer_audit_controls.json")
    original = load("check_multistrip_selfenergy", "check_multistrip_selfenergy.py")
    compare(original.exact_control(), "multistrip_selfenergy_controls.json")
    original = load("check_multistrip_first_shell", "check_multistrip_first_shell.py")
    compare(original.exact_control(), "multistrip_first_shell_controls.json")
    print("PASS: three original independent exact-control payloads", flush=True)

    # Preserve the original proposal script, but execute only its exact integer
    # recurrence. Its module-level NumPy/SciPy imports are irrelevant to acceptance.
    source = contained("check_su2_physical_rotor.py")
    functions = [node for node in ast.parse(source.read_text(encoding="utf-8")).body
                 if isinstance(node, ast.FunctionDef) and node.name == "sturm_count"]
    if len(functions) != 1 or functions[0].decorator_list:
        raise RuntimeError("Expected exactly one undecorated original Sturm recurrence")
    original_rotor = types.ModuleType("check_su2_physical_rotor")
    original_rotor.__file__ = str(source)
    original_rotor.__dict__.update({"F": Fraction, "math": math})
    sys.modules[original_rotor.__name__] = original_rotor
    exec(compile(ast.Module(body=functions, type_ignores=[]), str(source), "exec"),
         original_rotor.__dict__)
    original_replay = load("replay_su2_rotor_certificates", "replay_su2_rotor_certificates.py")
    original_replay.main()
    if any(name.split(".", 1)[0] in {"numpy", "scipy"} for name in sys.modules):
        raise RuntimeError("A numerical proposal dependency was imported")
    print("PASS: original integer recurrence and replay; NumPy/SciPy imports blocked", flush=True)
    final_count = check_manifest()
    print(f"PASS: final manifest unchanged, {final_count} files", flush=True)
    print("Scope: exact finite identities and saved rotor enclosures; "
          "analytic remainders and continuum claims are separate")


if __name__ == "__main__":
    main()
