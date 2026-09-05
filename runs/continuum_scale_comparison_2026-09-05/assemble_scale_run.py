"""Fresh-only assembly of the frozen scale-comparison evidence package."""

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
ROOT = next(parent for parent in HERE.parents if (parent / "pyproject.toml").is_file())
BASE = ROOT / "outputs/wilson_complete_band_20260905/next_scale"
RUN = ROOT / "runs/continuum_scale_comparison_2026-09-05"
ARCHIVE = Path("C:/WORKHOUSE/09_ARCHIVE/sorted_second_pass/EXTRACT_02_Wilson_Hessian_Discrete_Curl.md")
ARCHIVE_SHA = "ab2c9981fecceba6d4c4ed88ac6e9df8936908d3a7bbf2317acfbe0a24a8983b"
ENV = dict(os.environ, PYTHONDONTWRITEBYTECODE="1")
BLOCKER = r'''
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
'''


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def write(path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("x", encoding="utf-8", newline="\n") as stream:
        stream.write(value)


def write_json(path, payload):
    write(path, json.dumps(payload, indent=2, sort_keys=True) + "\n")


def execute(arguments, cwd=ROOT, expected=0):
    result = subprocess.run(arguments, cwd=cwd, env=ENV, capture_output=True,
                            text=True, check=False)
    if result.returncode != expected:
        raise RuntimeError(f"Command failed ({result.returncode}): {arguments}\n"
                           + result.stdout + result.stderr)
    return result


def seal():
    files = sorted(p for p in RUN.rglob("*") if p.is_file() and p.name != "SHA256SUMS")
    if any("__pycache__" in p.parts or p.suffix in {".pyc", ".pyo"} for p in files):
        raise RuntimeError("Refusing to seal bytecode caches")
    (RUN / "SHA256SUMS").write_text(
        "".join(f"{digest(p)}  {p.relative_to(RUN).as_posix()}\n" for p in files),
        encoding="utf-8", newline="\n",
    )
    return len(files)


def main():
    if RUN.exists():
        raise FileExistsError("The target run already exists; do not overwrite evidence")
    docs_path = BASE / "integration/CANONICAL_DOCS_FREEZE.json"
    code_path = BASE / "integration/code/canonical_candidate_handoff.json"
    docs = json.loads(docs_path.read_text(encoding="utf-8"))
    code = json.loads(code_path.read_text(encoding="utf-8"))
    frozen = dict(code["canonical_code_hashes"])
    frozen.update({row["path"]: row["sha256"] for row in docs["proofs"]})
    for relative, expected in frozen.items():
        if digest(ROOT / relative) != expected:
            raise RuntimeError(f"A frozen canonical source changed: {relative}")
    if digest(ARCHIVE) != ARCHIVE_SHA:
        raise RuntimeError("Archived curl predecessor bytes differ from recorded provenance")
    originals = []
    for stem in ("cell_complex_hessian", "harmonic_incidence_comparison", "gaussian_memory",
                 "closed_form_schur", "periodic_3d_fast_bound", "vacuum_projection_mismatch"):
        originals.extend([f"check_{stem}.py", f"check_{stem}.json"])
    originals.extend(["check_gaussian_os_observability.py", "gaussian_os_observability_controls.json",
                      "VACUUM_ADAPTED_FAST_PROJECTION_ADDENDUM.md",
                      "QUANTUMREP_2019_INDEPENDENT_REVIEW.md", "QUANTUMREP_2019_RELEVANCE.md",
                      "quantumrep_exact_controls.txt", "quantumrep-01-00009.txt",
                      "quantumrep-first.png", "quantumrep-equations-6.png", "quantumrep-equations-7.png"])
    before = {str(BASE / name): digest(BASE / name) for name in originals}
    before.update({str(ROOT / relative): digest(ROOT / relative) for relative in frozen})
    before[str(ARCHIVE)] = digest(ARCHIVE)
    pdf = ROOT / "literature/fulltext/quantumrep-01-00009.pdf"
    before[str(pdf)] = digest(pdf)
    # Generate native evidence at an empty path. It records its own 11 source
    # hashes before and after and imports no installed workhouse fallback.
    with tempfile.TemporaryDirectory(prefix="scale-certificate-", dir=ROOT / "outputs") as directory:
        fresh = Path(directory) / "certificate.json"
        generated = execute([sys.executable, "-B", "-c", BLOCKER,
                             str(ROOT / "scripts/verify_continuum_scale_comparison.py"),
                             "--output", str(fresh)])
        report = json.loads(fresh.read_text(encoding="utf-8"))
        if report["exact_check_count"] != 7 or not report["passed"]:
            raise RuntimeError("Native certificate did not pass all seven checks")
        for relative, expected in report["sources"].items():
            if digest(ROOT / relative) != expected:
                raise RuntimeError("Native source changed after runner completed")
            before.setdefault(str(ROOT / relative), expected)
        RUN.mkdir()
        shutil.copyfile(fresh, RUN / "certificate.json")
    write(RUN / "native_runner.log", generated.stdout + generated.stderr)
    copies = []

    def copy(source, destination, reason):
        target = RUN / destination
        if target.exists():
            raise FileExistsError(f"Duplicate assembly destination: {destination}")
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(source, target)
        if digest(source) != digest(target):
            raise RuntimeError(f"Evidence copy differs: {destination}")
        copies.append({"origin": str(source), "destination": destination,
                       "sha256": digest(target), "role": reason})

    for relative in report["sources"]:
        copy(ROOT / relative, "source/" + relative, "native runner input")
    for row in docs["proofs"]:
        if row["path"] not in report["sources"]:
            copy(ROOT / row["path"], "source/" + row["path"], "method-comparison proof provenance")
    for name in originals:
        copy(BASE / name, name, "unchanged original independent evidence")
    for name in ("FINITE_CELL_WILSON_GAP_AND_BOUNDARY_FORM.md", "HARMONIC_BOUNDARY_COMPARISON.md",
                 "PERIODIC_3D_COULOMB_BOX_FAST_BOUND.md", "GAUSSIAN_OS_HISTORY_OBSERVABILITY.md",
                 "GAUSSIAN_MEMORY_AND_SPECTRAL_MATCHING.md", "CLOSED_FORM_SCHUR_GAP_AND_SCALE_BUDGET.md"):
        before[str(BASE / name)] = digest(BASE / name)
        copy(BASE / name, "original_drafts/" + name, "original derivation before canonical integration")
    copy(ARCHIVE, "provenance/EXTRACT_02_Wilson_Hessian_Discrete_Curl.md", "portable archived predecessor")
    copy(pdf, "provenance/quantumrep-01-00009.pdf", "user-supplied paper, method review only")
    copy(docs_path, "provenance/CANONICAL_DOCS_FREEZE.json", "documentation freeze handoff")
    copy(code_path, "provenance/canonical_candidate_handoff.json", "native code freeze handoff")
    copy(BASE / "integration/code/original_payload_comparison.json",
         "provenance/original_payload_comparison.json", "independent original/native payload audit")
    for name in ("pyproject.toml", "uv.lock"):
        copy(ROOT / name, "environment/" + name, "declared reproducible dependency environment")
    copy(HERE / "replay_frozen.py", "replay_frozen.py", "read-only acceptance replay")
    copy(Path(__file__), "assemble_scale_run.py", "fresh-only assembly provenance")
    write_json(RUN / "copy_provenance.json", {"copies": copies})
    link_rows = []
    for row in docs["pending_new_run_links"]:
        destination = ((ROOT / row["from"]).parent / row["target"]).resolve()
        if destination != RUN / "README.md" and not destination.is_file():
            raise RuntimeError(f"Missing canonical link: {row}")
        if not destination.is_relative_to(RUN):
            raise RuntimeError("Expected new-run link resolves outside the run")
        link_rows.append({**row, "run_relative": destination.relative_to(RUN).as_posix()})
    # Check all actual Markdown links to this run, not only the handoff list.
    actual_links = []
    for directory in (ROOT / "paper", ROOT / "docs", ROOT):
        candidates = directory.glob("*.md") if directory == ROOT else directory.rglob("*.md")
        for path in candidates:
            for target in re.findall(r"\]\(([^)]+)\)", path.read_text(encoding="utf-8")):
                clean = target.strip("<>").split("#", 1)[0]
                if "runs/continuum_scale_comparison_2026-09-05/" not in clean:
                    continue
                destination = (path.parent / clean).resolve()
                if destination != RUN / "README.md" and not destination.is_file():
                    raise RuntimeError(f"Broken new-run link in {path}: {target}")
                actual_links.append({"from": path.relative_to(ROOT).as_posix(), "target": target})
    write_json(RUN / "canonical_link_validation.json",
               {"passed": True, "handoff_links": link_rows, "actual_markdown_links": actual_links})
    after = {path: digest(Path(path)) for path in before}
    if after != before:
        raise RuntimeError("A source or original evidence changed during assembly")
    write_json(RUN / "source_integrity.json", {"passed": True, "before": before, "after": after})
    write(RUN / "README.md", '''# Continuum scale-comparison evidence, 2026-09-05

This run preserves six analytic research notes, their original derivations,
seven precisely scoped native checks, and seven original exact-control families.
The native certificate is `certificate.json`; every one of its eleven source
inputs is mirrored byte for byte under `source/`. The sixth note reviews a supplied
coupled-oscillator paper and is preserved as provenance, not an additional native
mathematical certificate. No new Lean theorem is claimed by this run.

The proved analytic results cover fixed-cell physical harmonic gaps, positive
interface comparison, the periodic three-dimensional Coulomb fast Hessian bound,
Gaussian history observability, and conditional closed-form Schur spectral/frame
comparison. They retain the torus zero modes, source-coordinate distinctions,
and the open nonlinear Wilson fast-form, history/locality and continuum hypotheses.
Finite controls certify the displayed algebra and examples; they do not substitute
for the general proofs. The raw-vacuum projection counterexample is additional
exact evidence and is deliberately not counted as an eighth native check.

From a repository environment installed using `uv sync --all-extras --frozen`:

```powershell
.venv/Scripts/python.exe -B runs/continuum_scale_comparison_2026-09-05/replay_frozen.py
```

The replay uses only pinned native modules under empty package paths, checks
both native payloads and every invariant record, and recomputes all seven original
control payloads. It prohibits NumPy/SciPy imports. The two original Gaussian
scripts write beside their source, so byte-identical copies run in fresh temporary
directories; the frozen original scripts and JSONs remain unchanged. The other
originals are called through their read-only calculation functions. Five corrupt
spectral/window inputs must be rejected. `python -O`, certificate overwrites and
manifest corruption are separately rejected in `negative_control_validation.json`.
`SHA256SUMS` covers the exact complete file set and forbids bytecode caches.

`copy_provenance.json` records every source and unchanged copy. The archived curl
predecessor is portable at `provenance/EXTRACT_02_Wilson_Hessian_Discrete_Curl.md`
(SHA256 `ab2c9981fecceba6d4c4ed88ac6e9df8936908d3a7bbf2317acfbe0a24a8983b`).
The user-supplied PDF is `provenance/quantumrep-01-00009.pdf`; its text, three selected
page images, exact method controls and independent review remain at the run root.
The paper is compared at its actual coupled-oscillator scope; it is not asserted
to prove a Yang-Mills result. Canonical proof links are checked in
`canonical_link_validation.json`. Frozen dependency metadata is under `environment/`.

`source_integrity.json` records equal hashes before and after assembly. The native
runner independently checks its own source hashes before and after calculation.
The final read-only replay also rechecks the complete manifest after all work.
The saved replay log was generated while assembling this new run; final sealing
and a further read-only replay are reported to the parent research task.
''')
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
    with tempfile.TemporaryDirectory(prefix="scale-negative-") as directory:
        temporary = Path(directory)
        output = temporary / "must-not-exist.json"
        runner = RUN / "source/scripts/verify_continuum_scale_comparison.py"
        optimized = subprocess.run([sys.executable, "-B", "-O", "-c", BLOCKER,
                                   str(runner), "--output", str(output)],
                                  cwd=temporary, env=ENV, capture_output=True, text=True, check=False)
        if optimized.returncode == 0 or output.exists() or "assertions enabled" not in optimized.stderr:
            raise RuntimeError("Frozen native runner did not reject optimization without output")
        negative["optimized_native_runner_rejected_without_output"] = True
        output.write_text("retained evidence", encoding="utf-8")
        overwrite = subprocess.run([sys.executable, "-B", "-c", BLOCKER, str(runner),
                                   "--output", str(output)], cwd=temporary, env=ENV,
                                  capture_output=True, text=True, check=False)
        if overwrite.returncode == 0 or "fresh output" not in overwrite.stderr:
            raise RuntimeError("Frozen native runner did not reject an existing output")
        if output.read_text(encoding="utf-8") != "retained evidence":
            raise RuntimeError("Negative overwrite test modified retained evidence")
        negative["existing_output_rejected_and_preserved"] = True
        corrupt = temporary / "corrupt-copy"
        shutil.copytree(RUN, corrupt)
        with (corrupt / "certificate.json").open("ab") as stream:
            stream.write(b"\ncorrupt\n")
        rejected = subprocess.run([sys.executable, "-B", str(corrupt / "replay_frozen.py"),
                                  "--manifest-only"], cwd=temporary, env=ENV,
                                 capture_output=True, text=True, check=False)
        if rejected.returncode == 0 or "Manifest digest mismatch: certificate.json" not in rejected.stderr:
            raise RuntimeError("Tampered certificate was not rejected by its manifest")
        negative["manifest_certificate_corruption_rejected"] = True
    negative["exact_spectral_and_window_corruptions_rejected"] = 5
    negative["passed"] = True
    write_json(RUN / "negative_control_validation.json", negative)
    count = seal()
    final = execute([sys.executable, "-B", str(RUN / "replay_frozen.py")])
    # The number of files is now final. Refresh only this generated assembly log,
    # reseal it, then perform a final read-only acceptance without changing the run.
    (RUN / "replay_validation.log").write_text(final.stdout + final.stderr,
                                               encoding="utf-8", newline="\n")
    if seal() != count:
        raise RuntimeError("Final evidence file count changed unexpectedly")
    final = execute([sys.executable, "-B", str(RUN / "replay_frozen.py")])
    if {path: digest(Path(path)) for path in before} != before:
        raise RuntimeError("A source or original changed during final replay")
    result = {"passed": True, "run": str(RUN), "manifest_sha256": digest(RUN / "SHA256SUMS"),
              "manifest_file_count": count, "total_files_including_manifest": count + 1,
              "native_source_count": len(report["sources"]),
              "native_schema": report["schema"], "native_exact_check_count": report["exact_check_count"],
              "native_certificate_sha256": digest(RUN / "certificate.json"),
              "original_control_families_replayed": 7, "canonical_handoff_links": len(link_rows),
              "actual_new_run_markdown_links": len(actual_links), "source_integrity_count": len(before),
              "completed_utc": datetime.now(UTC).isoformat(), "final_replay": final.stdout,
              "negative_controls": negative}
    write_json(HERE / "assembly_result.json", result)
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
