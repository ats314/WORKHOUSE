"""Fresh-only assembly of original dynamic/full-fast research evidence."""

from __future__ import annotations

import hashlib
import json
import platform
import shutil
import sys
from pathlib import Path


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def write_json(path, value):
    with path.open("x", encoding="utf-8", newline="\n") as stream:
        json.dump(value, stream, indent=2, sort_keys=True)
        stream.write("\n")


def seal(run):
    files = sorted(path for path in run.rglob("*") if path.is_file() and path.name != "SHA256SUMS")
    text = "".join(f"{sha(path)}  {path.relative_to(run).as_posix()}\n" for path in files)
    (run / "SHA256SUMS").write_text(text, encoding="utf-8", newline="\n")


def main():
    if sys.flags.optimize:
        raise RuntimeError("Assembly rejects optimized execution")
    base = Path(__file__).resolve().parent.parent
    repo = next(path for path in base.parents if (path / "pyproject.toml").is_file())
    run = repo / "runs/dynamic_fast_green_2026-09-06"
    if run.exists():
        raise FileExistsError("Run assembly requires a fresh directory")
    dynamic = base / "dynamic_fiber"
    witness = base / "full_fast"
    publication = base / "publication"
    mapping = {}
    for name in [
        "DYNAMIC_FIBER_COVARIANCE_AND_CUBIC_ENERGY.md",
        "check_dynamic_fiber.py",
        "DYNAMIC_FIBER_CONTROLS.json",
        "check_full_green_review.py",
        "FULL_GREEN_INDEPENDENT_POLYNOMIAL_CONTROLS.json",
        "INDEPENDENT_FULL_GREEN_REVIEW.md",
    ]:
        mapping[name] = dynamic / name
    mapping["DYNAMIC_FIBER_ORIGINAL_README.md"] = dynamic / "README.md"
    for name in [
        "FULL_GAUSSIAN_FAST_GREEN.md",
        "check_full_fast_green.py",
        "FULL_FAST_GREEN_CONTROLS.json",
    ]:
        mapping[name] = base / name
    inventory = json.loads(
        (witness / "LOCAL_PLAQUETTE_FAST_FREEZE.json").read_text(encoding="utf-8")
    )
    for name, digest in inventory["required_files"].items():
        if sha(witness / name) != digest:
            raise ValueError("Witness frozen input changed: " + name)
        mapping[name] = witness / name
    mapping["LOCAL_PLAQUETTE_FAST_FREEZE.json"] = witness / "LOCAL_PLAQUETTE_FAST_FREEZE.json"
    mapping["provenance/CANONICAL_COPY_AUDIT.json"] = publication / "CANONICAL_COPY_AUDIT.json"
    mapping["reviews/ROOT_MATHEMATICAL_AUDIT.md"] = publication / "ROOT_MATHEMATICAL_AUDIT.md"
    for name in [
        "replay_frozen.py",
        "assemble_dynamic_fast_run.py",
        "validate_dynamic_fast_run.py",
    ]:
        mapping[name] = publication / name
    records = json.loads((publication / "CANONICAL_COPY_AUDIT.json").read_text(encoding="utf-8"))
    canonical = {}
    for row in records:
        if (
            sha(repo / row["source"]) != row["source_sha256"]
            or sha(repo / row["target"]) != row["canonical_sha256"]
        ):
            raise ValueError("Canonical/original copy input changed")
        mapping["source/" + row["target"]] = repo / row["target"]
        canonical["source/" + row["target"]] = row["canonical_sha256"]
    if any(not path.is_file() for path in mapping.values()):
        raise FileNotFoundError("A required original input is not present")
    provenance = {
        name: {"source": path.relative_to(repo).as_posix(), "sha256": sha(path)}
        for name, path in mapping.items()
    }
    run.mkdir()
    for name, original in mapping.items():
        target = run / name
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(original, target)
    cases = []
    specifications = [
        (
            "check_dynamic_fiber.py",
            "DYNAMIC_FIBER_CONTROLS.json",
            "dynamic_named_functions",
            ["check_dynamic_fiber.py", "DYNAMIC_FIBER_COVARIANCE_AND_CUBIC_ENERGY.md"],
            ["controls", "dynamic_spectral_island", "frequencies", 0],
        ),
        (
            "check_full_fast_green.py",
            "FULL_FAST_GREEN_CONTROLS.json",
            "derive",
            [],
            ["families", 2, "probe_energy"],
        ),
        (
            "check_local_plaquette_fast_obstruction.py",
            "local_plaquette_fast_obstruction_controls_final.json",
            "witness_controls",
            [
                "check_local_plaquette_fast_obstruction.py",
                "LOCAL_PLAQUETTE_HARMONIC_FAST_OBSTRUCTION.md",
            ],
            ["controls", "physical_harmonic_fast_energy", "SU2_color_tensor_norm_squared"],
        ),
        (
            "check_full_green_review.py",
            "FULL_GREEN_INDEPENDENT_POLYNOMIAL_CONTROLS.json",
            "independent_polynomial_derive",
            [],
            ["full_compressed_polynomial_energy"],
        ),
    ]
    for checker, report, api, embedded, corruption in specifications:
        originals = set(embedded + [checker, report])
        if api == "derive":
            originals.add("FULL_GAUSSIAN_FAST_GREEN.md")
        cases.append(
            {
                "checker": checker,
                "report": report,
                "api": api,
                "embedded_pins": embedded,
                "corrupt_path": corruption,
                "original_pins": {name: sha(run / name) for name in sorted(originals)},
            }
        )
    write_json(
        run / "INPUTS.json",
        {
            "schema": "workhouse-dynamic-full-fast-originals/v1",
            "canonical_pins": canonical,
            "cases": cases,
            "original_report_boundary": (
                "Root Green report has external pins; "
                "embedded original report bytes remain unchanged."
            ),
        },
    )
    write_json(run / "PROVENANCE.json", provenance)
    write_json(
        run / "ENVIRONMENT.json",
        {
            "python": sys.version,
            "executable": sys.executable,
            "platform": platform.platform(),
            "required_libraries": ["sympy"],
            "scope": "Exact acceptance uses no NumPy/SciPy.",
        },
    )
    readme = """# Dynamic fiber covariance and actual full Gaussian fast Green

This run preserves three analytic proofs and four complete original control
families: dynamic conditional covariance/two-time SU2 Wick algebra;
nonreducing constrained full-fast inverses; the actual local Wilson
harmonic obstruction; and an independent 64-component colored polynomial
compression checking the ordered Lie-cubic factor.

Run `python replay_frozen.py --negative-controls` with SymPy installed.
Replay is read-only, rejects optimized Python, blocks NumPy/SciPy, checks
the complete manifest and original source pins, reconstructs the canonical
mathematical bodies, and compares every field of all four reports.

The original checkers also accept fresh output paths. Their original CLI
and embedded report pins are preserved; the root Green report predates its
final proof and is pinned externally in INPUTS and PROVENANCE. Acceptance
does not claim that this older report originally pinned a later proof.
The copied assembly and validation helpers are provenance; standalone
reproduction requires only replay_frozen.py and the files in this run.

The full inverse uses the n-leg energy prior, including mixed retained/fast
occupations. Conditional-fiber energy domination is a quadratic-form
statement, not entrywise absolute domination. The actual local magnetic
harmonic term obstructs an unrestricted regulator-uniform absolute rooted
bound, while its selected global spatial sum cancels. Bounded retained
means and local coefficient hypotheses remain explicit in the dynamic
bound. No interacting remainder or continuum mass-gap theorem is certified.

Finite exact controls support the analytic statements within their stated
boundaries. This run adds no native check or Lean theorem. The all-volume
Fourier estimates and all-n inverse identities remain analytically proved,
with their hypotheses, rather than machine-certified by finite examples.

`VALIDATION.json` records cold relocation, source-read and corruption guards.
`source/paper/research_notes/` contains the three canonical mirrors;
`provenance/CANONICAL_COPY_AUDIT.json` records original-to-canonical changes.
The historical pre-final local witness report is intentionally excluded.
"""
    (run / "README.md").write_text(readme, encoding="utf-8", newline="\n")
    seal(run)
    print(
        json.dumps(
            {
                "assembled": str(run),
                "copied_originals_and_sources": len(mapping),
                "families": len(cases),
                "canonical_proofs": len(canonical),
            }
        )
    )


if __name__ == "__main__":
    main()
