"""Fresh-only assembly of the three reviewed original control families."""

import hashlib
import json
import re
import shutil
import subprocess
import sys
from pathlib import Path

sys.dont_write_bytecode = True
REPO = Path.cwd().resolve()
HERE = Path(__file__).resolve().parent
BASE = HERE.parent
RUN = REPO / "runs/gaussian_path_nonlinear_input_2026-09-06"


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def write_json(path, data):
    with path.open("x", encoding="utf-8", newline="\n") as stream:
        json.dump(data, stream, indent=2, sort_keys=True)
        stream.write("\n")


def seal():
    lines = [
        sha(p) + "  " + p.relative_to(RUN).as_posix()
        for p in sorted(RUN.rglob("*"))
        if p.is_file() and p.name != "SHA256SUMS"
    ]
    (RUN / "SHA256SUMS").write_text("\n".join(lines) + "\n", encoding="utf-8", newline="\n")


def run(command, cwd=REPO):
    result = subprocess.run(command, cwd=cwd, capture_output=True, text=True, check=False)
    return {"returncode": result.returncode, "stdout": result.stdout, "stderr": result.stderr}


def main():
    if sys.flags.optimize:
        raise RuntimeError("Assertions required")
    if RUN.exists():
        raise FileExistsError(RUN)
    cases = [
        (
            "next_gaussian_endpoint_baseline",
            "EXACT_GAUSSIAN_PATH_ENDPOINT_BASELINE.md",
            "check_gaussian_endpoint_baseline.py",
            "gaussian_endpoint_baseline_controls_frozen.json",
            "checks",
            "source_sha256",
            "G19_GAUSSIAN_PATH_ENDPOINT_BASELINE_20260906.md",
        ),
        (
            "next_gaussian_fast_covariance",
            "CONDITIONAL_QUANTUM_PATH_COVARIANCE.md",
            "check_conditional_quantum_covariance.py",
            "conditional_quantum_covariance_controls_frozen.json",
            "controls",
            "source_sha256",
            "G19_CONDITIONAL_QUANTUM_PATH_COVARIANCE_20260906.md",
        ),
        (
            "next_cubic_ground_transfer",
            "CUBIC_GROUND_TRANSFER.md",
            "check_cubic_ground_transfer.py",
            "cubic_ground_controls_frozen.json",
            "controls",
            "sources",
            "G19_CUBIC_GROUND_TRANSFER_20260906.md",
        ),
    ]
    extras = {
        "next_gaussian_endpoint_baseline": [
            "INDEPENDENT_GAUSSIAN_ENDPOINT_REVIEW.md",
            "GAUSSIAN_ENDPOINT_VALIDATION.json",
        ],
        "next_gaussian_fast_covariance": [
            "INDEPENDENT_CONDITIONAL_COVARIANCE_REVIEW.md",
            "CONDITIONAL_COVARIANCE_FREEZE.json",
            "CONDITIONAL_COVARIANCE_VALIDATION.json",
            "INDEPENDENT_COVARIANCE_REPLAY_VALIDATION.json",
        ],
        "next_cubic_ground_transfer": [
            "INDEPENDENT_CUBIC_GROUND_REVIEW.md",
            "CUBIC_INDEPENDENT_REPLAY_VALIDATION.json",
            "validate_cubic_independently.py",
        ],
    }
    copies = {}
    inputs = {
        "schema": "workhouse-gaussian-path-original-inputs/v1",
        "cases": [],
        "canonical_pins": {},
    }
    for folder, proof, checker, report, payload_key, pin_key, canonical in cases:
        saved = json.loads((BASE / folder / report).read_text(encoding="utf-8"))
        for name, digest in saved[pin_key].items():
            if sha(BASE / folder / name) != digest:
                raise ValueError("Original report source mismatch: " + name)
        for name in [proof, checker, report, *extras[folder]]:
            copies[name] = BASE / folder / name
        relative = "source/paper/research_notes/" + canonical
        source = REPO / "paper/research_notes" / canonical
        inputs["canonical_pins"][relative] = sha(source)
        copies[relative] = source
        inputs["cases"].append(
            {
                "checker": checker,
                "report": report,
                "proof": proof,
                "payload_key": payload_key,
                "pin_key": pin_key,
                "original_pins": sorted(saved[pin_key]),
            }
        )
    copies["replay_frozen.py"] = HERE / "replay_frozen.py"
    copies["assemble_run.py"] = Path(__file__).resolve()
    copies["provenance/CANDIDATE_COPY_AUDIT.json"] = (
        BASE / "next_publication_continuation/staged_docs/CANDIDATE_COPY_AUDIT.json"
    )
    copies["provenance/CANONICAL_DOCS_APPLIED.json"] = (
        BASE / "next_publication_continuation/staged_docs/CANONICAL_DOCS_APPLIED.json"
    )
    copies["continuation/CONNECTED_CUBIC_FAST_ENERGY_DRAFT.md"] = (
        BASE / "next_connected_cubic_fast_energy/CONNECTED_CUBIC_FAST_ENERGY_DRAFT.md"
    )
    before = {str(source): sha(source) for source in copies.values()}
    RUN.mkdir(parents=True)
    for relative, source in copies.items():
        destination = RUN / relative
        destination.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(source, destination)
    write_json(RUN / "INPUTS.json", inputs)
    (RUN / "continuation/UNVERIFIED.md").write_text(
        "# Unverified continuation preserved without promotion\n\n"
        "CONNECTED_CUBIC_FAST_ENERGY_DRAFT.md is an unfinished continuation copied "
        "verbatim at the user's request to preserve work before stopping research. "
        "It has not completed independent proof review or exact controls. Its file "
        "hash establishes byte preservation only. It supplies no RESULT, native CHK, "
        "Lean theorem or evidence support in this run.\n",
        encoding="utf-8",
        newline="\n",
    )
    write_json(
        RUN / "PROVENANCE.json",
        {
            relative: {"source": source.relative_to(REPO).as_posix(), "sha256": sha(source)}
            for relative, source in copies.items()
        },
    )
    (RUN / "README.md").write_text(
        "# Gaussian path and first nonlinear input evidence\n\n"
        "Three analytically proved results are accompanied by their original exact controls "
        "and independent reviews. This run adds no native CHK or Lean theorem. The controls "
        "verify finite algebra; the all-size and fixed-complex mathematical scopes are in "
        "the proofs. Original evidence bytes are preserved at the run root; canonical proof "
        "mirrors are under source/. PROVENANCE.json identifies each copy.\n\n"
        "From a checkout with the locked WORKHOUSE dependencies installed, run:\n\n"
        "```text\npython -B runs/gaussian_path_nonlinear_input_2026-09-06/replay_frozen.py "
        "--negative-controls\n```\n\n"
        "Replay is read-only and loads only the three pinned original modules and declared "
        "SymPy dependencies. NumPy/SciPy and optimized execution are rejected. Every manifest "
        "file, original source pin, full mathematical payload and canonical mirror is checked "
        "before/after replay. VALIDATION.json records cold relocation and rejection checks.\n\n"
        "The Gaussian estimates retain a positive regulator or explicitly omit flat modes. "
        "Covariance summability is uniform in volume at fixed block scale; no uniform-in-L "
        "derivative bound is claimed. The cubic theorem concerns fixed finite complexes "
        "and the stated local source chart, preserving its distinction from the full "
        "matrix-observation sigma algebra. Interacting scale iteration remains open.\n",
        encoding="utf-8",
        newline="\n",
    )
    seal()
    positive = run([sys.executable, "-B", str(RUN / "replay_frozen.py"), "--negative-controls"])
    if positive["returncode"]:
        raise ValueError(positive)
    optimized = run([sys.executable, "-B", "-O", str(RUN / "replay_frozen.py")])
    if optimized["returncode"] == 0:
        raise ValueError("Optimized replay accepted")
    negative_root = HERE / "cold_validation"
    if negative_root.exists():
        raise FileExistsError(negative_root)
    negative_root.mkdir()
    cold = negative_root / "cold_run"
    shutil.copytree(RUN, cold)
    cold_before = {p.relative_to(cold).as_posix(): sha(p) for p in cold.rglob("*") if p.is_file()}
    cold_result = run(
        [sys.executable, "-B", str(cold / "replay_frozen.py"), "--negative-controls"], cold
    )
    if cold_result["returncode"]:
        raise ValueError(cold_result)
    if cold_before != {
        p.relative_to(cold).as_posix(): sha(p) for p in cold.rglob("*") if p.is_file()
    }:
        raise ValueError("Cold replay wrote evidence")
    # This is a newly created disposable validation copy, never the sealed run.
    corrupted = cold / "EXACT_GAUSSIAN_PATH_ENDPOINT_BASELINE.md"
    corrupted.write_bytes(corrupted.read_bytes() + b"\ncorruption negative\n")
    corruption = run([sys.executable, "-B", str(cold / "replay_frozen.py")], cold)
    if corruption["returncode"] == 0:
        raise ValueError("Manifest corruption accepted")
    overwrite = run(
        [sys.executable, "-B", str(RUN / cases[0][2]), "--output", str(RUN / cases[0][3])]
    )
    if overwrite["returncode"] == 0:
        raise ValueError("Original output overwrite accepted")
    after = {str(source): sha(source) for source in copies.values()}
    if before != after:
        raise ValueError("Original source changed")
    linked_files = [
        REPO / "README.md",
        REPO / "docs/current_research.md",
        REPO / "docs/research_goal.md",
        REPO / "paper/README.md",
        *[REPO / "paper/research_notes" / case[6] for case in cases],
    ]
    links = []
    for document in linked_files:
        for target in re.findall(r"\]\(([^)]+)\)", document.read_text(encoding="utf-8")):
            if RUN.name not in target:
                continue
            resolved = (document.parent / target.split("#", 1)[0]).resolve()
            if not resolved.is_file():
                raise ValueError("Missing published run link: " + str(resolved))
            links.append({"document": document.relative_to(REPO).as_posix(), "target": target})
    write_json(
        RUN / "VALIDATION.json",
        {
            "passed": True,
            "full_replay": positive,
            "cold_relocation": cold_result,
            "optimized_rejection": optimized["returncode"],
            "manifest_corruption_rejection": corruption["returncode"],
            "overwrite_rejection": overwrite["returncode"],
            "original_input_bytes_unchanged": True,
            "resolved_run_links": links,
            "snapshot_note": (
                "Cold copy predates this additive validation record; "
                "final full replay checks the final seal."
            ),
        },
    )
    seal()
    final = run([sys.executable, "-B", str(RUN / "replay_frozen.py"), "--negative-controls"])
    if final["returncode"]:
        raise ValueError(final)
    summary = {
        "passed": True,
        "manifest_sha256": sha(RUN / "SHA256SUMS"),
        "manifest_entries": len((RUN / "SHA256SUMS").read_text().splitlines()),
        "file_count": sum(p.is_file() for p in RUN.rglob("*")),
        "canonical_pins": inputs["canonical_pins"],
        "resolved_run_link_occurrences": len(links),
        "final_replay": final,
    }
    write_json(HERE / "ASSEMBLY_RESULT.json", summary)
    print(json.dumps(summary, sort_keys=True))


if __name__ == "__main__":
    main()
