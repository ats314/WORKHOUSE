"""Assemble the new continuum-block evidence run after dependencies freeze.

This owns only the named new run. It never regenerates repository views,
registers a run, overwrites original evidence, or edits a canonical source.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import shutil
import subprocess
import sys
from pathlib import Path

sys.dont_write_bytecode = True

EVIDENCE = [
    "check_rg_conditional_gradient.py",
    "check_wilson_block_score.py",
    "wilson_block_score_controls.json",
    "check_strip_born_oppenheimer_audit.py",
    "strip_born_oppenheimer_audit_controls.json",
    "check_multistrip_selfenergy.py",
    "multistrip_selfenergy_controls.json",
    "check_multistrip_first_shell.py",
    "multistrip_first_shell_controls.json",
    "check_original_strip_su2.py",
    "check_original_strip_su2.json",
    "check_su2_physical_rotor.py",
    "su2_physical_rotor_control.json",
    "extend_su2_rotor_certificate.py",
    "su2_rotor_1000000_certificate.json",
    "replay_su2_rotor_certificates.py",
    "check_su2_oscillator_correction.py",
    "SU2_PHYSICAL_ROTOR_CONTROL.md",
    "STRIP_BORN_OPPENHEIMER_INDEPENDENT_AUDIT.md",
]

DRAFTS = [
    "RG_CONDITIONAL_GRADIENT_REPAIR.md",
    "REVERSE_MASS_MATCHING.md",
    "WILSON_BLOCK_CONDITIONAL_SCORE.md",
    "PHYSICAL_WILSON_FIBER_FAST_GAP.md",
    "FULL_PHYSICAL_TWO_SQUARE_GAP.md",
    "GLUEBALL_REVERSE_TARGET_DATA.md",
    "WILSON_STRIP_BORN_OPPENHEIMER_FIRST_TERM.md",
]

REPLAY = r'''"""Read-only replay of pinned native and original continuum-block controls."""
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
'''


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def contained(root: Path, relative: str) -> Path:
    result = (root / relative).resolve()
    if not result.is_relative_to(root) or result == root:
        raise RuntimeError(f"Path escapes the intended root: {relative}")
    return result


def write_manifest(run: Path) -> None:
    files = sorted(p for p in run.rglob("*") if p.is_file() and p.name != "SHA256SUMS")
    if any("__pycache__" in p.parts or p.suffix in {".pyc", ".pyo"} for p in files):
        raise RuntimeError("Refusing to freeze bytecode artifacts")
    (run / "SHA256SUMS").write_text(
        "".join(f"{digest(path)}  {path.relative_to(run).as_posix()}\n" for path in files),
        encoding="utf-8", newline="\n",
    )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--certificate", type=Path, required=True)
    parser.add_argument("--block-field", required=True)
    parser.add_argument("--rotor-field", required=True)
    args = parser.parse_args()
    if sys.flags.optimize:
        raise RuntimeError("Assertions must remain enabled")
    evidence_root = Path(__file__).resolve().parent
    repo = evidence_root.parents[1]
    run = contained(repo, "runs/continuum_wilson_block_2026-09-05")
    if run.exists():
        raise RuntimeError("The new run already exists; inspect it instead of overwriting")
    certificate = args.certificate.resolve()
    if not certificate.is_relative_to(repo / "outputs"):
        raise RuntimeError("The new runner certificate must be an outputs artifact")
    report = json.loads(certificate.read_text(encoding="utf-8"))
    sources = report["sources"]
    for name, expected in sources.items():
        path = contained(repo, name)
        if digest(path) != expected:
            raise RuntimeError(f"Canonical dependency changed after certificate generation: {name}")
    for name in [*EVIDENCE, *DRAFTS]:
        if not contained(evidence_root, name).is_file():
            raise RuntimeError(f"Missing required original evidence: {name}")

    run.mkdir(parents=False)
    shutil.copyfile(certificate, run / "certificate.json")
    source_provenance = {}
    for name, expected in sources.items():
        destination = contained(run, "source/" + name)
        destination.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(contained(repo, name), destination)
        source_provenance[name] = expected
    # Also retain the declared dependency environment for cold reproduction.
    for name in ["pyproject.toml", "uv.lock"]:
        destination = contained(run, "source/" + name)
        if not destination.exists():
            shutil.copyfile(repo / name, destination)

    originals = {}
    for name in EVIDENCE:
        shutil.copyfile(evidence_root / name, run / name)
        originals[name] = digest(evidence_root / name)
    for name in DRAFTS:
        destination = run / "original_drafts" / name
        destination.parent.mkdir(exist_ok=True)
        shutil.copyfile(evidence_root / name, destination)
        originals["original_drafts/" + name] = digest(evidence_root / name)
    shutil.copyfile(Path(__file__), run / "assemble_run.py")

    config = {"payloads": [
        {"module": "workhouse.continuum_wilson_block", "function": "exact_block_controls",
         "source": "source/src/workhouse/continuum_wilson_block.py", "field": args.block_field},
        {"module": "workhouse.continuum_wilson_rotor", "function": "exact_rotor_controls",
         "source": "source/src/workhouse/continuum_wilson_rotor.py", "field": args.rotor_field},
    ]}
    (run / "replay_config.json").write_text(json.dumps(config, indent=2) + "\n", encoding="utf-8")
    (run / "proof_provenance.json").write_text(json.dumps({
        "runner_sources": source_provenance,
        "original_evidence_copied_byte_for_byte": originals,
        "scope": "Original output drafts are preserved separately from the canonical runner-pinned proof sources.",
    }, indent=2) + "\n", encoding="utf-8")
    (run / "replay_frozen.py").write_text(REPLAY, encoding="utf-8", newline="\n")
    (run / "README.md").write_text(
        "# Continuum Wilson block evidence, 5 September 2026\n\n"
        "This run records the native exact finite controls, original independent algebra, "
        "and four saved untruncated SU(2) rotor enclosures. The complete analytic block, "
        "oscillator-remainder, OS-intertwining and conditional scale statements are the "
        "separately pinned proof sources. This is not a continuum Yang-Mills certificate.\n\n"
        "Run from the repository environment:\n\n"
        "```text\npython -B runs/continuum_wilson_block_2026-09-05/replay_frozen.py\n```\n\n"
        "The replay rejects optimization, verifies the entire manifest before and after, "
        "loads the copied native modules through an empty fake package rather than the "
        "installed workhouse package, compares their exact payloads to certificate.json, "
        "reruns all six pinned invariant checks and matches the embedded rotor certificates, "
        "recomputes three original independent control payloads without rewriting them, "
        "and replays the four saved rotor enclosures by integer signs. The original "
        "Sturm recurrence is AST-loaded with only Fraction and math globals; the original "
        "replay main retains its source hashes and corrupted-interval check. NumPy and "
        "SciPy imports are deliberately blocked, and the eigensolver proposal path is "
        "disabled. The original numerical-generation scripts remain unchanged. No "
        "bytecode caches are written.\n\n"
        "Every runner SOURCES path is mirrored under source/. Original scripts and JSON "
        "records remain byte-for-byte copies at the top level; original research drafts "
        "are under original_drafts/. proof_provenance.json distinguishes those drafts "
        "from the canonical proof bytes. Source changes require a new run rather than "
        "editing this record. The original generation scripts may refuse existing JSON "
        "or write reports; use replay_frozen.py for a read-only replay.\n",
        encoding="utf-8", newline="\n",
    )
    write_manifest(run)
    env = os.environ.copy()
    env["PYTHONDONTWRITEBYTECODE"] = "1"
    replay = subprocess.run(
        [sys.executable, "-B", str(run / "replay_frozen.py")],
        cwd=repo, env=env, check=False, capture_output=True, text=True,
    )
    if replay.returncode:
        print(replay.stdout)
        print(replay.stderr, file=sys.stderr)
        raise RuntimeError("Frozen replay failed; the unregistered new run requires inspection")
    (run / "frozen_replay.txt").write_text(replay.stdout, encoding="utf-8", newline="\n")
    if replay.stderr:
        (run / "frozen_replay_stderr.txt").write_text(replay.stderr, encoding="utf-8", newline="\n")
    optimized = subprocess.run(
        [sys.executable, "-B", "-O", str(run / "replay_frozen.py"), "--manifest-only"],
        cwd=repo, env=env, check=False, capture_output=True, text=True,
    )
    if optimized.returncode == 0 or "Assertions must be enabled" not in optimized.stderr:
        raise RuntimeError("The replay did not reject disabled assertions")
    (run / "optimization_rejection.txt").write_text(
        optimized.stderr, encoding="utf-8", newline="\n",
    )
    write_manifest(run)
    subprocess.run(
        [sys.executable, "-B", str(run / "replay_frozen.py"), "--manifest-only"],
        cwd=repo, env=env, check=True,
    )
    for name, expected in sources.items():
        if digest(contained(repo, name)) != expected:
            raise RuntimeError(f"Canonical dependency changed during assembly: {name}")
    for name in [*EVIDENCE, *DRAFTS]:
        key = name if name in EVIDENCE else "original_drafts/" + name
        if digest(evidence_root / name) != originals[key]:
            raise RuntimeError(f"Original evidence changed during assembly: {name}")
    print(replay.stdout)
    print("FROZEN", run)
    print("MANIFEST_SHA256", digest(run / "SHA256SUMS"))


if __name__ == "__main__":
    main()
