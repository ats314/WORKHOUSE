"""Fresh-only assembly of the endpoint and local source package after final freeze."""

import argparse
import hashlib
import importlib.util
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
PUBLICATION = HERE.parent
BASE = PUBLICATION.parent
ROOT = next(p for p in HERE.parents if (p / "pyproject.toml").is_file())
RUN = ROOT / "runs/wilson_endpoint_local_score_2026-09-05"
RUNNER = "scripts/verify_endpoint_window.py"
ENV = {k: v for k, v in os.environ.items() if k not in {"PYTHONPATH", "PYTHONHOME"}}
ENV["PYTHONDONTWRITEBYTECODE"] = "1"
BOOTSTRAP = r"""
import runpy, sys
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
"""
COLD_BOOTSTRAP = r"""
import os, pathlib, runpy, sys
sys.dont_write_bytecode = True
original = pathlib.Path(sys.argv[1]).resolve()
copy = pathlib.Path(sys.argv[2]).resolve()
expected_count = int(sys.argv[3])
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
target = sys.argv[4]
sys.argv = sys.argv[4:]
runpy.run_path(target, run_name="__main__")
native = []
for name, module in sys.modules.items():
    if name.startswith("workhouse.") and getattr(module, "__file__", None):
        path = pathlib.Path(module.__file__).resolve()
        if not path.is_relative_to(copy):
            raise RuntimeError("An unpinned native module was imported: " + str(path))
        native.append(name)
if len(native) != expected_count:
    raise RuntimeError("Unexpected native module count: " + str(native))
print(f"PASS: {len(native)} pinned native modules; no original checkout source access")
"""


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def write(path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("x", encoding="utf-8", newline="\n") as stream:
        stream.write(value)


def write_json(path, value):
    write(path, json.dumps(value, indent=2, sort_keys=True) + "\n")


def execute(command, cwd=ROOT):
    result = subprocess.run(command, cwd=cwd, env=ENV, capture_output=True, text=True, check=False)
    if result.returncode:
        raise RuntimeError(
            f"Command failed ({result.returncode}): {command}\n" + result.stdout + result.stderr
        )
    return result


def load(path, name):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


def seal():
    paths = sorted(p for p in RUN.rglob("*") if p.is_file() and p.name != "SHA256SUMS")
    if any("__pycache__" in p.parts or p.suffix in {".pyc", ".pyo", ".olean"} for p in paths):
        raise RuntimeError("Compiled caches/binaries are not part of this run")
    (RUN / "SHA256SUMS").write_text(
        "".join(f"{digest(p)}  {p.relative_to(RUN).as_posix()}\n" for p in paths),
        encoding="utf-8",
        newline="\n",
    )
    return len(paths)


def cold_relocation(saved, module_count):
    before = {p.relative_to(RUN).as_posix(): digest(p) for p in RUN.rglob("*") if p.is_file()}
    with tempfile.TemporaryDirectory(prefix="workhouse-cold-literal-") as directory:
        temporary = Path(directory)
        copied = temporary / "evidence"
        shutil.copytree(RUN, copied)
        prefix = [
            sys.executable,
            "-I",
            "-B",
            "-c",
            COLD_BOOTSTRAP,
            str(ROOT),
            str(copied),
            str(module_count),
        ]
        replay = execute([*prefix, str(copied / "replay_frozen.py")], cwd=temporary)
        output = temporary / "fresh-native-certificate.json"
        native = execute(
            [*prefix, str(copied / "source" / RUNNER), "--output", str(output)], cwd=temporary
        )
        fresh = json.loads(output.read_text(encoding="utf-8"))
        if {k: v for k, v in saved.items() if k != "runtime"} != {
            k: v for k, v in fresh.items() if k != "runtime"
        }:
            raise RuntimeError("Relocated native certificate differs outside runtime metadata")
        after = {
            p.relative_to(copied).as_posix(): digest(p) for p in copied.rglob("*") if p.is_file()
        }
        if after != before:
            raise RuntimeError("Relocated run changed during replay")
    return {
        "passed": True,
        "fresh_native_nonruntime_fields_match": True,
        "native_module_count": module_count,
        "original_checkout_source_access_forbidden": True,
        "isolated_interpreter": True,
        "numpy_scipy_blocked": True,
        "frozen_relocated_file_count_including_manifest": len(before),
        "evidence_unchanged": True,
        "replay_stdout": replay.stdout,
        "native_stdout": native.stdout,
        "scope": (
            "Relocation with the existing declared interpreter dependencies; "
            "no fresh dependency install or Lean compilation is claimed."
        ),
    }


def validate_links(proof_paths, freeze):
    sources = [ROOT / path for path in proof_paths]
    sources += [
        ROOT / path
        for path in (
            "README.md",
            "docs/current_research.md",
            "docs/research_goal.md",
            "paper/README.md",
        )
    ]
    actual = []
    for source in sources:
        prose = re.sub(r"```.*?```", "", source.read_text(encoding="utf-8"), flags=re.S)
        prose = re.sub(r"`[^`]*`", "", prose)
        for target in re.findall(r"\]\(([^)]+)\)", prose):
            clean = target.strip("<>").split("#", 1)[0]
            if not clean or "://" in clean or clean.startswith("mailto:"):
                continue
            if "/" not in clean and "." not in clean:
                continue
            if not (source.parent / clean).resolve().exists():
                raise RuntimeError(f"Broken current local link: {source}: {target}")
            actual.append({"from": source.relative_to(ROOT).as_posix(), "target": target})
    applied = json.loads((PUBLICATION / "CANONICAL_DOCS_APPLIED.json").read_text(encoding="utf-8"))
    planned = [{"from": row[0], "target": row[1]} for row in applied["pending_new_run_links"]]
    for row in planned:
        if not ((ROOT / row["from"]).parent / row["target"]).resolve().is_file():
            raise RuntimeError("A frozen planned run link is missing")
    return {
        "passed": True,
        "planned_run_link_count": len(planned),
        "planned_run_links": planned,
        "current_local_link_count": len(actual),
        "current_local_links": actual,
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--docs-freeze", type=Path, required=True)
    parser.add_argument("--native-handoff", type=Path, required=True)
    args = parser.parse_args()
    if RUN.exists():
        raise FileExistsError("A run already exists; original evidence must not be overwritten")
    freeze = json.loads(args.docs_freeze.read_text(encoding="utf-8"))
    handoff = json.loads(args.native_handoff.read_text(encoding="utf-8"))
    inventory = json.loads(
        (PUBLICATION / "run_plan/ORIGINAL_INPUT_INVENTORY.json").read_text(encoding="utf-8")
    )
    runner = load(ROOT / RUNNER, "literal_assembly_selected_runner")
    source_pins = runner.source_hashes()
    proof_paths = [path for path in source_pins if path.startswith("paper/research_notes/")]
    if len(proof_paths) != 4 or len(runner.MODEL_NAMES) != 5:
        raise RuntimeError("Four final proofs and five original private models are required")
    # Handoffs are provenance plus independently checked canonical byte inventories.
    proof_rows = freeze["proof_copies"]
    frozen_proofs = {}
    for row in proof_rows:
        name = row.get("path", row.get("canonical"))
        if name:
            path = Path(name)
            if path.is_absolute():
                name = path.relative_to(ROOT).as_posix()
            frozen_proofs[name] = row.get("sha256", row.get("canonical_sha256"))
    if {path: source_pins[path] for path in proof_paths} != frozen_proofs:
        raise RuntimeError("Final documentation freeze differs from the native proof source set")
    code_pins = handoff["sources"]
    if not code_pins or any(
        source_pins.get(name) != expected for name, expected in code_pins.items()
    ):
        raise RuntimeError("Final native handoff pins need inspection or differ")
    before = {str(ROOT / name): expected for name, expected in source_pins.items()}
    for path, expected in before.items():
        if digest(Path(path)) != expected:
            raise RuntimeError("Frozen source mismatch")
    case_records = []
    extra_original_pins = {}
    for entry in inventory["families"]:
        family = entry["family"]
        source = ROOT / entry["script"]["source"]
        report_path = ROOT / entry["report"]["source"]
        pins = {ROOT / row["source"]: row["sha256"] for row in entry["verified_declared_pins"]}
        if (
            digest(source) != entry["script"]["sha256"]
            or digest(report_path) != entry["report"]["sha256"]
        ):
            raise RuntimeError("Original family bytes changed")
        if any(digest(path) != sha for path, sha in pins.items()):
            raise RuntimeError("Original source pins differ: " + family)
        extra_original_pins.update(pins)
        case_records.append(
            {
                "family": family,
                "source": "original_tree/" + source.relative_to(ROOT).as_posix(),
                "report": "original_tree/" + report_path.relative_to(ROOT).as_posix(),
                "source_pins": {
                    "original_tree/" + path.relative_to(ROOT).as_posix(): sha
                    for path, sha in pins.items()
                },
            }
        )
    with tempfile.TemporaryDirectory(
        prefix="literal-certificate-", dir=ROOT / "outputs"
    ) as directory:
        fresh = Path(directory) / "certificate.json"
        generated = execute(
            [sys.executable, "-B", "-c", BOOTSTRAP, str(ROOT / RUNNER), "--output", str(fresh)]
        )
        report = json.loads(fresh.read_text(encoding="utf-8"))
        if (
            not report["passed"]
            or report["exact_check_count"] != 10
            or report["sources"] != source_pins
        ):
            raise RuntimeError("Final native count, pins or status differs")
        RUN.mkdir()
        shutil.copyfile(fresh, RUN / "certificate.json")
    write(RUN / "native_runner.log", generated.stdout + generated.stderr)
    copies = []

    def copy(source, relative, role):
        source = Path(source)
        target = RUN / relative
        if target.exists():
            if digest(target) != digest(source):
                raise RuntimeError("Duplicate evidence destination differs: " + relative)
            return
        target.parent.mkdir(parents=True, exist_ok=True)
        sha = digest(source)
        before.setdefault(str(source), sha)
        shutil.copyfile(source, target)
        if digest(target) != sha:
            raise RuntimeError("Evidence copy differs: " + relative)
        copies.append({"origin": str(source), "destination": relative, "sha256": sha, "role": role})

    for name in source_pins:
        copy(ROOT / name, "source/" + name, "native runner source input")
    original_rows = list(inventory["extra_evidence"])
    for entry in inventory["families"]:
        original_rows.extend([entry["script"], entry["report"]])
    for row in original_rows:
        source = ROOT / row["source"]
        if digest(source) != row["sha256"]:
            raise RuntimeError("Inventoried original changed: " + row["source"])
        copy(source, source.name, "unchanged original proof/control/audit")
        copy(
            source,
            "original_tree/" + source.relative_to(ROOT).as_posix(),
            "portable unchanged original",
        )
    for source in extra_original_pins:
        copy(
            source,
            "original_tree/" + source.relative_to(ROOT).as_posix(),
            "original declared source snapshot",
        )
        if source.relative_to(ROOT).as_posix().startswith("paper/research_notes/"):
            copy(
                source,
                "source/" + source.relative_to(ROOT).as_posix(),
                "analytic predecessor provenance",
            )
    for relative in proof_paths:
        prose = (ROOT / relative).read_text(encoding="utf-8")
        for name in set(re.findall(r"\]\((G(?:18|19)_[^)#]+\.md)(?:#[^)]*)?\)", prose)):
            path = ROOT / "paper/research_notes" / name
            if not path.is_file():
                raise RuntimeError("A direct analytic predecessor is missing: " + name)
            copy(
                path,
                "source/paper/research_notes/" + name,
                "direct analytic predecessor provenance",
            )
    copy(
        args.docs_freeze,
        "provenance/" + args.docs_freeze.name,
        "final canonical documentation freeze",
    )
    copy(args.native_handoff, "provenance/" + args.native_handoff.name, "final native code freeze")
    for name in ("pyproject.toml", "uv.lock"):
        copy(ROOT / name, "environment/" + name, "locked declared Python dependencies")
    for relative in (
        "CANONICAL_DOCS_APPLIED.json",
        "CANONICAL_NATIVE_CODE_FREEZE.json",
        "INDEPENDENT_NATIVE_API_REVIEW.md",
        "FINAL_ENDPOINT_DOCS_REVIEW.md",
        "staged_docs/CANDIDATE_COPY_AUDIT.json",
        "staged_docs/build_candidate.py",
        "staged_docs/apply_candidate.py",
        "run_plan/ORIGINAL_INPUT_INVENTORY.json",
        "run_plan/RESULT_SUPPORT_MAPPING.json",
        "run_plan/prepare_run_plan.py",
        "run_plan/ASSEMBLY_PLAN.md",
    ):
        source = PUBLICATION / relative
        if source.is_file():
            copy(source, "provenance/" + source.name, "source/copy/scope audit provenance")
    copy(HERE / "replay_frozen.py", "replay_frozen.py", "read-only complete exact replay")
    copy(Path(__file__), "assemble_endpoint_run.py", "fresh-only assembly provenance")
    write_json(RUN / "provenance/original_cases.json", case_records)
    write_json(RUN / "copy_provenance.json", {"copies": copies})
    write(RUN / "README.md", README)
    links = validate_links(proof_paths, freeze)
    write_json(RUN / "canonical_link_validation.json", links)
    after = {path: digest(Path(path)) for path in before}
    if after != before:
        raise RuntimeError("A source changed during assembly")
    write_json(RUN / "source_integrity.json", {"passed": True, "before": before, "after": after})
    seal()
    replay = execute([sys.executable, "-B", str(RUN / "replay_frozen.py")])
    write(RUN / "replay_validation.log", replay.stdout + replay.stderr)
    seal()
    negative = {}
    optimized = subprocess.run(
        [sys.executable, "-B", "-O", str(RUN / "replay_frozen.py")],
        cwd=ROOT,
        env=ENV,
        capture_output=True,
        text=True,
        check=False,
    )
    if optimized.returncode == 0 or "Assertions must be enabled" not in optimized.stderr:
        raise RuntimeError("Frozen replay did not reject optimized Python")
    negative["optimized_frozen_replay_rejected"] = True
    with tempfile.TemporaryDirectory(prefix="literal-negative-") as directory:
        temporary = Path(directory)
        output = temporary / "evidence.json"
        selected_runner = RUN / "source" / RUNNER
        optimized = subprocess.run(
            [
                sys.executable,
                "-B",
                "-O",
                "-c",
                BOOTSTRAP,
                str(selected_runner),
                "--output",
                str(output),
            ],
            cwd=temporary,
            env=ENV,
            capture_output=True,
            text=True,
            check=False,
        )
        if (
            optimized.returncode == 0
            or output.exists()
            or "assertions enabled" not in optimized.stderr
        ):
            raise RuntimeError("Native -O rejection failed")
        negative["optimized_native_runner_rejected_without_output"] = True
        output.write_text("retained evidence", encoding="utf-8")
        overwrite = subprocess.run(
            [sys.executable, "-B", "-c", BOOTSTRAP, str(selected_runner), "--output", str(output)],
            cwd=temporary,
            env=ENV,
            capture_output=True,
            text=True,
            check=False,
        )
        if (
            overwrite.returncode == 0
            or "fresh output" not in overwrite.stderr
            or output.read_text(encoding="utf-8") != "retained evidence"
        ):
            raise RuntimeError("Existing evidence was not rejected and preserved")
        negative["existing_output_rejected_and_preserved"] = True
        corrupted = temporary / "corrupt-copy"
        shutil.copytree(RUN, corrupted)
        with (corrupted / "certificate.json").open("ab") as stream:
            stream.write(b"\ncorrupt\n")
        result = subprocess.run(
            [sys.executable, "-B", str(corrupted / "replay_frozen.py"), "--manifest-only"],
            cwd=temporary,
            env=ENV,
            capture_output=True,
            text=True,
            check=False,
        )
        if (
            result.returncode == 0
            or "Manifest digest mismatch: certificate.json" not in result.stderr
        ):
            raise RuntimeError("Manifest corruption rejection failed")
        negative["manifest_certificate_corruption_rejected"] = True
    negative.update({"mathematical_defects_rejected": 9, "passed": True})
    write_json(RUN / "negative_control_validation.json", negative)
    seal()
    module_count = len(runner.MODEL_NAMES) + 3
    write_json(RUN / "cold_relocation_validation.json", cold_relocation(report, module_count))
    count = seal()
    replay = execute([sys.executable, "-B", str(RUN / "replay_frozen.py")])
    (RUN / "replay_validation.log").write_text(
        replay.stdout + replay.stderr, encoding="utf-8", newline="\n"
    )
    if seal() != count:
        raise RuntimeError("Final file count changed unexpectedly")
    final_cold = cold_relocation(report, module_count)
    final = execute([sys.executable, "-B", str(RUN / "replay_frozen.py"), "--manifest-only"])
    if {path: digest(Path(path)) for path in before} != before:
        raise RuntimeError("A source changed during final validation")
    result = {
        "passed": True,
        "run": str(RUN),
        "manifest_sha256": digest(RUN / "SHA256SUMS"),
        "manifest_file_count": count,
        "total_files_including_manifest": count + 1,
        "native_certificate_sha256": digest(RUN / "certificate.json"),
        "native_schema": report["schema"],
        "native_check_count": 10,
        "native_source_count": len(source_pins),
        "original_control_families": 5,
        "original_declared_source_pins": sum(len(row["source_pins"]) for row in case_records),
        "canonical_note_count": len(proof_paths),
        "new_lean_theorems": 0,
        "planned_run_links_validated": links["planned_run_link_count"],
        "current_local_links_validated": links["current_local_link_count"],
        "unchanged_source_count": len(before),
        "negative_controls": negative,
        "final_cold_relocation": final_cold,
        "final_manifest_validation": final.stdout,
        "completed_utc": datetime.now(UTC).isoformat(),
    }
    write_json(HERE / "assembly_result.json", result)
    print(json.dumps(result, indent=2))


README = """# Complete endpoints, localized score and covariant sources

This sealed run preserves four canonical analytic proofs, five original
finite control families and ten native exact checks. The endpoint theorem
controls the entire retained spectrum and the complete additive Wilson
cluster. The actual localized score theorem gives a selected static-source
Schur estimate, with exact gradient-support tensorization. Local covariant
matrix path observations have a uniform transverse harmonic floor and a
regulated full Gaussian consequence. These are distinct established scopes;
the nonlinear interacting ground/source, compatible history/scale hierarchy
and continuum construction remain open.

From the declared repository environment (`uv sync --all-extras --frozen`):

```powershell
.venv/Scripts/python.exe -B runs/wilson_endpoint_local_score_2026-09-05/replay_frozen.py
```

The replay verifies the exact manifest before and after, loads eight pinned
native modules through empty package namespaces, and compares all fifteen
source pins, ten check records and five complete mathematical payloads.
It recomputes every original payload and all twelve original declared source
pins, runs the unchanged original endpoint replay, and rejects nine corrupt
mathematical inputs or certificates. NumPy/SciPy and bytecode writes are
blocked. Optimized mode, existing output and manifest corruption are checked
separately on disposable evidence copies.

Original sources and reports are preserved unchanged at the run root and
under `original_tree/` at their required repository-relative depth. Invoke
the original endpoint CLI from that preserved tree; its top-level copy is
documentary because it locates prior proofs through parents[5]. No original
program is patched for relocation. Use the final suffixed reports linked
in the canonical proofs; earlier intermediate snapshots are not current
acceptance evidence.

`certificate.json` and `source/` contain the selected canonical replay inputs.
`copy_provenance.json`, `source_integrity.json` and `SHA256SUMS` record exact
source preservation. `canonical_link_validation.json` resolves the current
proof and research-page references. `cold_relocation_validation.json`
records an isolated copied-run replay and a fresh native certificate with
matching non-runtime fields, while an audit hook forbids original-checkout
source reads. Declared existing interpreter libraries remain available;
this is not a claim to have reinstalled dependencies or compiled new Lean.

The finite controls check exact matrices, strict spectral counts, genuine
Markov and separate static-energy negatives, leading SU(2) algebra, complete
finite tensor forms, actual path/cell identities and full complex-rational
Fourier blocks. The all-size, arbitrary fixed-rank, closed-domain, actual
Wilson derivative and countable/full-Fock conclusions are the analytic
proofs. The moment-only API retains its externally certified whole-tail
premise. A compression-only bound is not promoted to a full form. The
positive regulator does not construct an unregulated flat-mode vacuum.
No previous sealed run was modified.
"""

if __name__ == "__main__":
    main()
