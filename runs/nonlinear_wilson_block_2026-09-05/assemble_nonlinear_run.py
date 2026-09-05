"""Fresh-only assembly and cold validation of nonlinear Wilson block evidence."""

import hashlib
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
from datetime import UTC, datetime
from pathlib import Path

sys.dont_write_bytecode = True
if sys.flags.optimize:
    raise RuntimeError("Assertions must be enabled")
HERE = Path(__file__).resolve().parent
BASE = HERE.parent
ROOT = next(p for p in HERE.parents if (p / "pyproject.toml").is_file())
RUN = ROOT / "runs/nonlinear_wilson_block_2026-09-05"
ENV = {k: v for k, v in os.environ.items() if k not in {"PYTHONPATH", "PYTHONHOME"}}
ENV["PYTHONDONTWRITEBYTECODE"] = "1"
BOOTSTRAP = r'''
import pathlib, runpy, sys
sys.dont_write_bytecode = True
class RejectNumericalImports:
    def find_spec(self, fullname, path=None, target=None):
        if fullname.split(".", 1)[0] in {"numpy", "scipy"}:
            raise ImportError("Undeclared numerical dependency forbidden: " + fullname)
        return None
sys.meta_path.insert(0, RejectNumericalImports())
target = sys.argv[1]
sys.argv = sys.argv[1:]
runpy.run_path(target, run_name="__main__")
'''
COLD_BOOTSTRAP = r'''
import os, pathlib, runpy, sys
sys.dont_write_bytecode = True
original = pathlib.Path(sys.argv[1]).resolve()
copy = pathlib.Path(sys.argv[2]).resolve()
def deny_checkout(event, args):
    if event == "open" and isinstance(args[0], (str, bytes, os.PathLike)):
        path = pathlib.Path(os.fsdecode(args[0])).resolve()
        if path.is_relative_to(original) and not path.is_relative_to(original / ".venv"):
            raise RuntimeError("Relocated replay accessed original checkout source: " + str(path))
sys.addaudithook(deny_checkout)
class RejectNumericalImports:
    def find_spec(self, fullname, path=None, target=None):
        if fullname.split(".", 1)[0] in {"numpy", "scipy"}:
            raise ImportError("Undeclared numerical dependency forbidden: " + fullname)
        return None
sys.meta_path.insert(0, RejectNumericalImports())
target = sys.argv[3]
sys.argv = sys.argv[3:]
runpy.run_path(target, run_name="__main__")
native = []
for name, module in sys.modules.items():
    if name.startswith("workhouse.") and getattr(module, "__file__", None):
        path = pathlib.Path(module.__file__).resolve()
        if not path.is_relative_to(copy):
            raise RuntimeError("An unpinned native module was imported: " + str(path))
        native.append(name)
if len(native) != 3:
    raise RuntimeError("Unexpected native module count: " + str(native))
print("PASS: three pinned native modules; no original checkout source access")
'''


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def write(path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("x", encoding="utf-8", newline="\n") as stream:
        stream.write(value)


def write_json(path, value):
    write(path, json.dumps(value, indent=2, sort_keys=True) + "\n")


def execute(command, cwd=ROOT):
    result = subprocess.run(command, cwd=cwd, env=ENV, capture_output=True,
                            text=True, check=False)
    if result.returncode:
        raise RuntimeError(f"Command failed ({result.returncode}): {command}\n"
                           + result.stdout + result.stderr)
    return result


def seal():
    paths = sorted(p for p in RUN.rglob("*") if p.is_file() and p.name != "SHA256SUMS")
    if any("__pycache__" in p.parts or p.suffix in {".pyc", ".pyo", ".olean"} for p in paths):
        raise RuntimeError("Compiled cache/binary artifacts are not part of this run")
    (RUN / "SHA256SUMS").write_text(
        "".join(f"{digest(p)}  {p.relative_to(RUN).as_posix()}\n" for p in paths),
        encoding="utf-8", newline="\n")
    return len(paths)


def cold_relocation(saved):
    before = {p.relative_to(RUN).as_posix(): digest(p) for p in RUN.rglob("*") if p.is_file()}
    with tempfile.TemporaryDirectory(prefix="workhouse-cold-nonlinear-") as directory:
        temporary = Path(directory)
        copy = temporary / "evidence"
        shutil.copytree(RUN, copy)
        replay = execute([sys.executable, "-I", "-B", "-c", COLD_BOOTSTRAP,
                          str(ROOT), str(copy), str(copy / "replay_frozen.py")], cwd=temporary)
        output = temporary / "fresh-native-certificate.json"
        native = execute([sys.executable, "-I", "-B", "-c", COLD_BOOTSTRAP,
                          str(ROOT), str(copy), str(copy / "source/scripts/verify_nonlinear_wilson_block.py"),
                          "--output", str(output)], cwd=temporary)
        fresh = json.loads(output.read_text(encoding="utf-8"))
        if any(value != fresh[key] for key, value in saved.items() if key != "runtime"):
            raise RuntimeError("Relocated fresh certificate differs outside runtime metadata")
        after = {p.relative_to(copy).as_posix(): digest(p) for p in copy.rglob("*") if p.is_file()}
        if after != before:
            raise RuntimeError("Relocated run changed during replay")
    return {"passed": True, "fresh_native_nonruntime_fields_match": True,
            "native_module_count": 3, "original_checkout_source_access_forbidden": True,
            "isolated_interpreter": True, "numpy_scipy_blocked": True,
            "frozen_relocated_file_count_including_manifest": len(before),
            "evidence_unchanged": True, "replay_stdout": replay.stdout,
            "native_stdout": native.stdout,
            "scope": "Relocation with declared existing interpreter dependencies; no fresh dependency install or Lean compilation is claimed."}


def main():
    if RUN.exists():
        raise FileExistsError("A run already exists; original evidence must not be overwritten")
    freeze_path = BASE / "CANONICAL_NONLINEAR_DOCS_FREEZE.json"
    handoff_path = BASE / "NATIVE_CANDIDATE_HANDOFF.json"
    freeze = json.loads(freeze_path.read_text(encoding="utf-8"))
    handoff = json.loads(handoff_path.read_text(encoding="utf-8"))
    frozen = dict(handoff["code_hashes"])
    frozen.update({row["path"]: row["sha256"] for row in freeze["proofs"]})
    before = {}
    for relative, expected in frozen.items():
        source = ROOT / relative
        if digest(source) != expected:
            raise RuntimeError("Frozen source changed: " + relative)
        before[str(source)] = expected
    build_path = BASE / "canonical_lean_build/build_result.json"
    build = json.loads(build_path.read_text(encoding="utf-8"))
    scalar_path = BASE / "global_vertical_lean_build/build_result.json"
    scalar = json.loads(scalar_path.read_text(encoding="utf-8"))
    if not build["success"] or len(build["modules"]) != 7 or not scalar["success"]:
        raise RuntimeError("Wait for the full strict canonical and scalar Lean builds")
    for row in build["modules"]:
        source = ROOT / "lean" / (row["module"] + ".lean")
        if row["returncode"] or digest(source) != row["source_sha256"]:
            raise RuntimeError("Canonical Lean build/source mismatch")
        if "-DwarningAsError=true" not in row["command"]:
            raise RuntimeError("Canonical Lean module was not built strictly")
    if digest(BASE / "build_canonical_lean.py") != build["build_script_sha256"]:
        raise RuntimeError("Strict build script provenance changed")
    compiler = Path(build["compiler"])
    if digest(compiler) != build["compiler_sha256"] or build["compiler_sha256"] != scalar["compiler_sha256"]:
        raise RuntimeError("Compiler pin mismatch")
    original_report = json.loads((BASE / "check_global_wilson_vertical_barrier.json").read_text(encoding="utf-8"))
    for relative, expected in original_report["sources"].items():
        if digest(ROOT / relative) != expected:
            raise RuntimeError("Original control source pin mismatch: " + relative)
    with tempfile.TemporaryDirectory(prefix="nonlinear-certificate-", dir=ROOT / "outputs") as directory:
        fresh = Path(directory) / "certificate.json"
        generated = execute([sys.executable, "-B", "-c", BOOTSTRAP,
                             str(ROOT / "scripts/verify_nonlinear_wilson_block.py"),
                             "--output", str(fresh)])
        report = json.loads(fresh.read_text(encoding="utf-8"))
        if not report["passed"] or report["exact_check_count"] != 5 or len(report["sources"]) != 9:
            raise RuntimeError("Native result count/status mismatch")
        RUN.mkdir()
        shutil.copyfile(fresh, RUN / "certificate.json")
    write(RUN / "native_runner.log", generated.stdout + generated.stderr)
    copies = []

    def copy(source, relative, role):
        target = RUN / relative
        if target.exists():
            if digest(target) != digest(source):
                raise RuntimeError("Duplicate evidence destination differs: " + relative)
            return
        target.parent.mkdir(parents=True, exist_ok=True)
        source_hash = digest(source)
        before.setdefault(str(source), source_hash)
        shutil.copyfile(source, target)
        if digest(target) != source_hash:
            raise RuntimeError("Evidence copy differs: " + relative)
        copies.append({"origin": str(source), "destination": relative,
                       "sha256": source_hash, "role": role})

    for relative, expected in report["sources"].items():
        if digest(ROOT / relative) != expected:
            raise RuntimeError("Runner input changed after native calculation")
        copy(ROOT / relative, "source/" + relative, "native runner input")
    originals = ["GLOBAL_WILSON_VERTICAL_BARRIER.md", "GLOBAL_WILSON_VERTICAL_BARRIER_SHARPENED.md",
                 "NEAR_IDENTITY_WILSON_GROUND_BUNDLE.md", "ACTUAL_TWO_SQUARE_FIBER_COMPLEMENT.md",
                 "GLOBAL_WILSON_VERTICAL_BARRIER_AUDIT.md", "WILSON_GROUND_BUNDLE_INDEPENDENT_AUDIT.md",
                 "ACTUAL_TWO_SQUARE_COMPLEMENT_AUDIT.md", "check_global_wilson_vertical_barrier.py",
                 "check_global_wilson_vertical_barrier.json", "replay_global_wilson_vertical_barrier.py",
                 "check_ground_bundle_geometry.py", "check_ground_bundle_geometry.json",
                 "check_actual_complement_mechanism.py", "check_actual_complement_mechanism.json"]
    for name in originals:
        copy(BASE / name, name, "unchanged original derivation, audit or exact evidence")
    # All original source-hash keys still resolve, even in a cold relocated run.
    for relative in original_report["sources"]:
        copy(ROOT / relative, "original_tree/" + relative, "original verifier source layout")
    original_relative = BASE.relative_to(ROOT).as_posix()
    for name in ("check_global_wilson_vertical_barrier.json", "replay_global_wilson_vertical_barrier.py"):
        copy(BASE / name, "original_tree/" + original_relative + "/" + name,
             "unchanged original certificate/replay in its source layout")
    for name in ("G19_WILSON_PHYSICAL_FIBER_FAST_GAP_20260905.md",
                 "G19_WILSON_STRIP_BO_AND_TWO_STRIP_SPLITTING_20260905.md",
                 "G19_WILSON_TWO_SQUARE_PHYSICAL_SHELLS_20260905.md",
                 "G19_FORM_SCHUR_SCALE_COMPARISON_20260905.md"):
        copy(ROOT / "paper/research_notes" / name, "source/paper/research_notes/" + name,
             "established analytic predecessor")
    for row in build["modules"]:
        relative = "lean/" + row["module"] + ".lean"
        copy(ROOT / relative, "source/" + relative, "strict canonical Lean module input")
    copy(BASE / "GlobalWilsonVertical.lean", "source/lean/GlobalWilsonVertical.lean",
         "original separately compiled scalar Lean source")
    for name in ("lean-toolchain", "lake-manifest.json", "lakefile.toml"):
        copy(ROOT / "lean" / name, "source/lean/" + name, "portable locked Lean project metadata")
    copy(build_path, "lean/canonical_build_result.json", "captured strict full canonical Lean build")
    copy(BASE / "canonical_lean_build/strict_build.log", "lean/canonical_strict_build.log",
         "captured strict compiler commands and output")
    copy(scalar_path, "lean/original_scalar_build_result.json", "original seven-lemma strict build")
    copy(BASE / "build_canonical_lean.py", "lean/build_canonical_lean.py", "original canonical build helper provenance")
    copy(BASE / "verify_global_wilson_vertical_lean.py", "lean/verify_global_wilson_vertical_lean.py",
         "original scalar build helper provenance")
    setup = ROOT / "runs/wilson_creator_parent_2026-09-05/lean/build_result.json"
    if digest(setup) != scalar["runtime_setup_source_sha256"]:
        raise RuntimeError("Original compiler setup provenance changed")
    copy(setup, "lean/original_compiler_setup.json", "original read-only compiler cache discovery record")
    copy(freeze_path, "provenance/CANONICAL_NONLINEAR_DOCS_FREEZE.json", "canonical documentation freeze")
    copy(handoff_path, "provenance/NATIVE_CANDIDATE_HANDOFF.json", "native code freeze and focused validation")
    for name in ("pyproject.toml", "uv.lock"):
        copy(ROOT / name, "environment/" + name, "locked declared Python environment")
    copy(HERE / "replay_frozen.py", "replay_frozen.py", "read-only acceptance replay")
    copy(Path(__file__), "assemble_nonlinear_run.py", "fresh-only assembly provenance")
    write_json(RUN / "copy_provenance.json", {"copies": copies})
    write(RUN / "README.md", '''# Nonlinear Wilson block evidence, 2026-09-05

This run preserves three canonical analytic proofs: the global vertical barrier,
the near-identity ground-bundle relative form, and the actual full-block fast
compression with its exact Schur realization. Their general operator arguments
remain analytic. The five native T1 checks certify specified finite PSD/trace,
SU(2), scalar-budget, geometry and compression identities. They do not certify
the complete analytic conclusions, volume-uniform estimates or a continuum limit.

The native report is `certificate.json`; all nine inputs are copied byte for
byte under `source/`. The original conservative and sharpened global derivations,
ground-bundle and full-complement drafts, all three independent audits, and all
three original exact-control programs/reports are preserved at the run root.
Historical pre-format/pre-locator certificates are left in the original outputs;
they are not advertised as replayable against a later source snapshot here.

From the repository's declared environment (`uv sync --all-extras --frozen`):

```powershell
.venv/Scripts/python.exe -B runs/nonlinear_wilson_block_2026-09-05/replay_frozen.py
```

This command loads only the pinned native files under empty package paths,
recomputes every native payload/check record and all original control payloads,
rejects four corrupt or incomplete mathematical inputs, and prohibits NumPy/SciPy
imports. It validates the complete manifest before and after without changing
evidence. Existing outputs and optimized Python are separately rejected.

The original global-barrier verifier records outputs-relative source paths.
`original_tree/` preserves that exact layout, both original proof versions and
all predecessor inputs, so its unchanged `source_hashes()` and original replay
work after relocation. The top-level source/report copies preserve canonical
documentation links; to run that original CLI directly, use its copy beneath
`original_tree/outputs/wilson_complete_band_20260905/next_scale/next_nonlinear/`.
The main `replay_frozen.py` invokes that correctly located original replay.

The seven new Lean lemmas formalize real-scalar inequalities under explicit
analytic inputs. They do not formalize SU(N), elliptic operators, spectral
min-max, a ground bundle, the full-block vacuum or a volume limit. The original
strict scalar build and complete strict canonical build are captured under
`lean/`; all seven canonical modules, the original scalar source and locked
Lean project metadata are under `source/lean/`. Both builds used the same pinned
Lean compiler and warning-as-error mode. No .olean binaries are required or
included. Python replay checks the recorded source/build pins; it does not
rerun the compiler or prove the reported compilation outcome anew.

For an independent compiler replay, use the copied `source/lean/` project with
its pinned toolchain and dependency manifest, obtain the declared Mathlib
dependencies, and run `lake build --wfail`. The captured helper scripts retain
their original absolute paths as provenance; those paths are not needed by
the exact Python replay. `canonical_build_result.json` and the strict log identify
the compiler, commands, source digests and output digests actually observed.

`source_integrity.json`, `copy_provenance.json` and `SHA256SUMS` record unchanged
inputs and the exact complete file set. `canonical_link_validation.json` checks
all planned run links and current local links in the maintained summaries and
three new notes. `negative_control_validation.json` records tamper, overwrite
and -O rejection. `cold_relocation_validation.json` records a copied-run replay
outside the checkout with -I, no PYTHONPATH and source-read auditing, plus a
fresh copied-runner certificate matching every non-runtime field. This uses
the existing declared interpreter environment rather than claiming a fresh
dependency installation. No previous sealed run is modified.
''')
    link_sources = [ROOT / row["path"] for row in freeze["proofs"]]
    link_sources += [ROOT / p for p in ("README.md", "docs/current_research.md",
                    "docs/research_goal.md", "paper/README.md")]
    actual_links = []
    for source in link_sources:
        prose = re.sub(r"```.*?```", "", source.read_text(encoding="utf-8"), flags=re.S)
        prose = re.sub(r"`[^`]*`", "", prose)
        for target in re.findall(r"\]\(([^)]+)\)", prose):
            clean = target.strip("<>").split("#", 1)[0]
            if not clean or "://" in clean or clean.startswith("mailto:"):
                continue
            if not (source.parent / clean).resolve().exists():
                raise RuntimeError(f"Broken current local link: {source}: {target}")
            actual_links.append({"from": source.relative_to(ROOT).as_posix(), "target": target})
    for row in freeze["planned_run_links"]:
        if not ((ROOT / row["from"]).parent / row["target"]).resolve().is_file():
            raise RuntimeError("A planned run link is missing")
    write_json(RUN / "canonical_link_validation.json", {"passed": True,
               "planned_run_link_count": len(freeze["planned_run_links"]),
               "planned_run_links": freeze["planned_run_links"],
               "current_local_link_count": len(actual_links), "current_local_links": actual_links})
    after = {path: digest(Path(path)) for path in before}
    if after != before:
        raise RuntimeError("A source changed during assembly")
    write_json(RUN / "source_integrity.json", {"passed": True, "before": before, "after": after})
    seal()
    replay = execute([sys.executable, "-B", str(RUN / "replay_frozen.py")])
    write(RUN / "replay_validation.log", replay.stdout + replay.stderr)
    seal()
    negative = {}
    optimized = subprocess.run([sys.executable, "-B", "-O", str(RUN / "replay_frozen.py")],
                               cwd=ROOT, env=ENV, capture_output=True, text=True, check=False)
    if optimized.returncode == 0 or "Assertions must be enabled" not in optimized.stderr:
        raise RuntimeError("Frozen replay did not reject optimized Python")
    negative["optimized_frozen_replay_rejected"] = True
    with tempfile.TemporaryDirectory(prefix="nonlinear-negative-") as directory:
        temporary = Path(directory)
        output = temporary / "evidence.json"
        runner = RUN / "source/scripts/verify_nonlinear_wilson_block.py"
        optimized = subprocess.run([sys.executable, "-B", "-O", "-c", BOOTSTRAP,
                                   str(runner), "--output", str(output)], cwd=temporary,
                                  env=ENV, capture_output=True, text=True, check=False)
        if optimized.returncode == 0 or output.exists() or "assertions enabled" not in optimized.stderr:
            raise RuntimeError("Native -O rejection failed")
        negative["optimized_native_runner_rejected_without_output"] = True
        output.write_text("retained evidence", encoding="utf-8")
        overwrite = subprocess.run([sys.executable, "-B", "-c", BOOTSTRAP,
                                   str(runner), "--output", str(output)], cwd=temporary,
                                  env=ENV, capture_output=True, text=True, check=False)
        if overwrite.returncode == 0 or "fresh output" not in overwrite.stderr or output.read_text(encoding="utf-8") != "retained evidence":
            raise RuntimeError("Existing evidence was not rejected and preserved")
        negative["existing_output_rejected_and_preserved"] = True
        corrupt = temporary / "corrupt-copy"
        shutil.copytree(RUN, corrupt)
        with (corrupt / "certificate.json").open("ab") as stream:
            stream.write(b"\ncorrupt\n")
        result = subprocess.run([sys.executable, "-B", str(corrupt / "replay_frozen.py"),
                                 "--manifest-only"], cwd=temporary, env=ENV,
                                capture_output=True, text=True, check=False)
        if result.returncode == 0 or "Manifest digest mismatch: certificate.json" not in result.stderr:
            raise RuntimeError("Manifest corruption rejection failed")
        negative["manifest_certificate_corruption_rejected"] = True
    negative.update({"mathematical_corruptions_rejected": 4, "passed": True})
    write_json(RUN / "negative_control_validation.json", negative)
    seal()
    cold = cold_relocation(report)
    write_json(RUN / "cold_relocation_validation.json", cold)
    count = seal()
    replay = execute([sys.executable, "-B", str(RUN / "replay_frozen.py")])
    (RUN / "replay_validation.log").write_text(replay.stdout + replay.stderr, encoding="utf-8", newline="\n")
    if seal() != count:
        raise RuntimeError("Final file count changed unexpectedly")
    final_cold = cold_relocation(report)
    final = execute([sys.executable, "-B", str(RUN / "replay_frozen.py"), "--manifest-only"])
    if {path: digest(Path(path)) for path in before} != before:
        raise RuntimeError("A source changed during final validation")
    result = {"passed": True, "run": str(RUN), "manifest_sha256": digest(RUN / "SHA256SUMS"),
              "manifest_file_count": count, "total_files_including_manifest": count + 1,
              "native_certificate_sha256": digest(RUN / "certificate.json"),
              "native_schema": report["schema"], "native_check_count": 5, "native_source_count": 9,
              "original_control_programs_replayed": 3, "original_source_pins_replayed": len(original_report["sources"]),
              "strict_lean_modules_passed": len(build["modules"]), "new_scalar_lean_theorems": 7,
              "planned_run_links_validated": len(freeze["planned_run_links"]),
              "current_local_links_validated": len(actual_links), "unchanged_source_count": len(before),
              "negative_controls": negative, "final_cold_relocation": final_cold,
              "final_manifest_validation": final.stdout, "completed_utc": datetime.now(UTC).isoformat()}
    write_json(HERE / "assembly_result.json", result)
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
