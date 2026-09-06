"""Fresh-only assembly of the literal quantum source package after final freeze."""

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
RUN = ROOT / "runs/literal_quantum_sources_2026-09-05"
RUNNER = "scripts/verify_literal_coarse_sources.py"
ENV = {k: v for k, v in os.environ.items() if k not in {"PYTHONPATH", "PYTHONHOME"}}
ENV["PYTHONDONTWRITEBYTECODE"] = "1"
CASES = (
    (
        "literal",
        "next_literal/check_literal_vacuum_projection.py",
        "next_literal/check_literal_vacuum_projection.json",
    ),
    (
        "common",
        "next_literal_common/check_common_gauss_literal_projection.py",
        "next_literal_common/check_common_gauss_literal_projection.json",
    ),
    (
        "score",
        "next_literal/score_controls/check_ground_marginal_score.py",
        "next_literal/score_controls/ground_marginal_score_controls_final.json",
    ),
    (
        "gaussian",
        "next_gaussian_full/check_entire_gaussian_literal_complement.py",
        "next_gaussian_full/check_entire_gaussian_literal_complement.json",
    ),
    (
        "center",
        "next_quantum_score_center/check_central_score_identity_independent.py",
        "next_quantum_score_center/central_score_identity_independent.json",
    ),
    (
        "inverse",
        "next_literal_inverse/check_literal_inverse_energy.py",
        "next_literal_inverse/literal_inverse_energy_controls.json",
    ),
)
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
            if not (source.parent / clean).resolve().exists():
                raise RuntimeError(f"Broken current local link: {source}: {target}")
            actual.append({"from": source.relative_to(ROOT).as_posix(), "target": target})
    planned = freeze.get("planned_run_links", [])
    link_audit = PUBLICATION / "LITERAL_DOC_LINK_AUDIT.json"
    if not planned and link_audit.is_file():
        earlier = json.loads(link_audit.read_text(encoding="utf-8"))
        planned = [
            {"from": source.replace("\\", "/"), "target": target}
            for source, target in earlier.get("pending_run", [])
        ]
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
    inventory_module = load(
        PUBLICATION / "run_plan/inventory_originals.py", "literal_original_inventory"
    )
    runner = load(ROOT / RUNNER, "literal_assembly_selected_runner")
    source_pins = runner.source_hashes()
    proof_paths = [path for path in source_pins if path.startswith("paper/research_notes/")]
    if len(proof_paths) != 5 or len(runner.MODEL_NAMES) != 6:
        raise RuntimeError("Five final proofs and six original private models are required")
    # Handoffs are provenance plus independently checked canonical byte inventories.
    proof_rows = freeze.get("proofs", freeze.get("files", []))
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
    code_pins = handoff.get("code_hashes", handoff.get("source_hashes", {}))
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
    for family, source_name, report_name in CASES:
        source, report_path = BASE / source_name, BASE / report_name
        report = json.loads(report_path.read_text(encoding="utf-8"))
        if "sources" in report:
            pins = {ROOT / name: sha for name, sha in report["sources"].items()}
        elif isinstance(report["source_sha256"], dict):
            pins = {source.parent / name: sha for name, sha in report["source_sha256"].items()}
        else:
            pins = {source: report["source_sha256"]}
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
            or report["exact_check_count"] != 7
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
    for relative, kind in inventory_module.INPUTS.items():
        source = BASE / relative
        copy(source, source.name, "unchanged original " + kind)
        copy(
            source,
            "original_tree/" + source.relative_to(ROOT).as_posix(),
            "portable unchanged original " + kind,
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
        for name in set(re.findall(r"\]\((G19_[^)#]+\.md)(?:#[^)]*)?\)", prose)):
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
    for name in (
        "CANONICAL_LITERAL_COPY_AUDIT.json",
        "copy_literal_proof_notes.py",
        "LITERAL_DOC_LINK_AUDIT.json",
    ):
        path = PUBLICATION / name
        if path.is_file():
            copy(path, "provenance/" + name, "original-to-canonical mathematical prose mapping")
    for name in (
        "CURRENT_ORIGINAL_INPUTS.json",
        "original_six_family_replay.json",
        "inventory_originals.py",
        "replay_originals.py",
        "ASSEMBLY_PLAN.md",
    ):
        copy(
            PUBLICATION / "run_plan" / name,
            "provenance/" + name,
            "preassembly original evidence inventory/replay",
        )
    copy(HERE / "replay_frozen.py", "replay_frozen.py", "read-only complete exact replay")
    copy(Path(__file__), "assemble_literal_run.py", "fresh-only assembly provenance")
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
    negative.update({"mathematical_defects_rejected": 8, "passed": True})
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
        "native_check_count": 7,
        "native_source_count": len(source_pins),
        "original_control_families": 6,
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


README = """# Literal quantum sources: exact evidence, 2026-09-05

This run preserves five canonical analytic notes and the separately provenanced
inverse-energy addendum. The actual additive Wilson results use the true vacuum,
literal coarse sources and complete low spectral spaces. They give full form
domination and entire low-window onto frames for the specified independent or
common-Gauss copies. A generic intrinsic-score criterion remains valid; the
exact central SU(2) identity disproves the proposed global sublinear Fisher bound
and retains a conditional energy-localized replacement. The Gaussian theorem
uses the precise weighted coordinate range and explicit zero-mode regulator.
These statements do not add ambient interactions or establish a continuum limit.

`certificate.json` records seven native finite exact checks with all source pins
under `source/`. The six original control families and every saved mathematical
payload are preserved unchanged at the run root and in `original_tree/`, together
with their original proofs and audits. The inverse addendum strengthens existing
results; its finite four-state example distinguishes the full coefficient
175/37 from the sharper restricted-compression coefficient 127/25. The positive
trial in the central-score check uses a reconstructed potential and is explicitly
not an exact Wilson ground-state formula.

From the repository's declared environment (`uv sync --all-extras --frozen`):

```powershell
.venv/Scripts/python.exe -B runs/literal_quantum_sources_2026-09-05/replay_frozen.py
```

The read-only replay validates every manifest file before and after, loads the
complete pinned native model list through empty package namespaces, compares all
native check records and six payloads, replays every original complete payload
and declared source hash, and rejects eight defective mathematical inputs or
certificates. NumPy/SciPy imports and bytecode writes are disabled. `-O`, existing
output files and deliberately corrupted evidence are rejected separately.

The literal and Gaussian original controls resolve repository-relative source
pins using their original directory depth. Execute those original CLIs beneath
`original_tree/outputs/wilson_complete_band_20260905/next_scale/next_nonlinear/`,
not from their documentary top-level copies. The frozen replay uses this exact
layout automatically. Their complete historical predecessor inputs are copied
under the same miniature tree. No original program was patched for relocation.

`source_integrity.json`, `copy_provenance.json` and `SHA256SUMS` establish source
preservation and the complete file set. `canonical_link_validation.json` checks
current documentation links. `cold_relocation_validation.json` records replay
outside the checkout with an isolated interpreter and an audit that forbids
original-checkout source reads, followed by a fresh selected-runner certificate
matching every non-runtime field. This uses the existing declared Python
dependencies; it does not claim a new dependency installation.

The native checks certify their specified finite examples and exact identities.
Wilson localization, the limiting quantum-ground score conclusion, closed-form
operator statements, countable tensorization, Fock density and all-size harmonic
consequences are the pinned analytic arguments. No new Lean theorem is included
or inferred from an earlier compiler report. Neither a finite number cutoff nor
a positive-regulator result certifies an unregulated torus vacuum. The actual
interacting-volume, complete OS-history and continuum obligations remain open.

The prior generic score proposal and older drafts are preserved with provenance;
the new canonical score note explicitly links its resolved global candidate to
the central obstruction. The outdated unsuffixed score draft certificate is not
used as current evidence. Assembly/inventory scripts copied as provenance retain
their original repository layout; `replay_frozen.py` is the portable entry point.
No previous sealed run was modified.
"""


if __name__ == "__main__":
    main()
