"""Strict outputs-only Lean scalar build using an existing read-only cache."""

from __future__ import annotations

import hashlib
import json
import os
import subprocess
from pathlib import Path


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> None:
    if not __debug__:
        raise RuntimeError("Optimized Python is rejected for verification.")
    here = Path(__file__).resolve().parent
    repo = here.parents[3]
    setup_path = repo / "runs/wilson_creator_parent_2026-09-05/lean/build_result.json"
    setup = json.loads(setup_path.read_text(encoding="utf-8"))
    compiler = Path(setup["compiler"])
    source = here / "GlobalWilsonVertical.lean"
    if digest(compiler) != setup["compiler_sha256"]:
        raise RuntimeError("The previously verified compiler pin has changed.")
    build = here / "global_vertical_lean_build"
    build.mkdir(exist_ok=False)
    target = build / "GlobalWilsonVertical.olean"
    command = [str(compiler), "-DwarningAsError=true", "-o", str(target), str(source)]
    environment = dict(os.environ)
    environment["LEAN_PATH"] = setup["LEAN_PATH"]
    source_before = digest(source)
    completed = subprocess.run(
        command,
        cwd=repo,
        env=environment,
        text=True,
        capture_output=True,
        check=False,
    )
    version = subprocess.run(
        [str(compiler), "--version"],
        text=True,
        capture_output=True,
        check=True,
    ).stdout.strip()
    report = {
        "schema": "workhouse-global-vertical-lean/1",
        "scope": (
            "Seven real-scalar transfer lemmas under explicit analytic inputs; "
            "no SU(N), elliptic operator, spectral theorem or volume limit formalization."
        ),
        "command": command,
        "success": completed.returncode == 0 and target.exists(),
        "exit_code": completed.returncode,
        "stdout": completed.stdout,
        "stderr": completed.stderr,
        "compiler": str(compiler),
        "compiler_version": version,
        "compiler_sha256": digest(compiler),
        "source_sha256": source_before,
        "source_unchanged": source_before == digest(source),
        "olean_sha256": digest(target) if target.exists() else None,
        "runtime_setup_source_sha256": digest(setup_path),
        "lean_toolchain_sha256": digest(repo / "lean/lean-toolchain"),
        "lake_manifest_sha256": digest(repo / "lean/lake-manifest.json"),
        "LEAN_PATH": setup["LEAN_PATH"],
        "cache_policy": "Existing mathlib package cache read only; no dependency setup changed.",
        "axiom_guards": {
            name: ["propext", "Classical.choice", "Quot.sound"]
            for name in (
                "strip_factor",
                "near_cap",
                "near_affine",
                "far_affine",
                "spectral_from_split",
                "two_sector_form",
                "half_potential_threshold",
            )
        },
    }
    with (build / "build_result.json").open("x", encoding="utf-8", newline="\n") as stream:
        json.dump(report, stream, indent=2, sort_keys=True)
        stream.write("\n")
    print(json.dumps(report, indent=2, sort_keys=True))
    if not report["success"] or not report["source_unchanged"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
