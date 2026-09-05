r"""Compile every WORKHOUSE Lean module using the pinned, read-only mathlib cache.

Run from the repository root with:
    .venv\Scripts\python.exe -B outputs\lean_compression_20260905\verify_lean_compression.py

All compiled objects and reports are written into this isolated repository.
No lake setup, package download, or original-worktree write is performed.
"""

from __future__ import annotations

import hashlib
import json
import os
import subprocess
import sys
from pathlib import Path

OUTPUT = Path(__file__).resolve().parent
ROOT = OUTPUT.parents[1]
LEAN_ROOT = ROOT / "lean"
COMPILER = Path(
    r"C:\Users\Alex\.elan\toolchains\leanprover--lean4---v4.34.0-rc1\bin\lean.exe"
)
CACHE = Path(r"C:\WORKHOUSE\ALL THEORY\WORKHOUSE\lean\.lake\packages")
LIBRARY = LEAN_ROOT / ".lake" / "build" / "lib" / "lean"


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> int:
    prior_path = ROOT / "outputs" / "lean_chart_20260905" / "build_result.json"
    prior = json.loads(prior_path.read_text(encoding="utf-8"))
    sealed_chart = next(m for m in prior["modules"] if m["module"] == "Workhouse/VacuumChart")
    if digest(LEAN_ROOT / "Workhouse" / "VacuumChart.lean") != sealed_chart["source_sha256"]:
        raise RuntimeError("The previously sealed VacuumChart source has changed")
    (LIBRARY / "Workhouse").mkdir(parents=True, exist_ok=True)
    paths = [LIBRARY] + sorted(CACHE.glob("*/.lake/build/lib/lean"))
    environment = os.environ.copy()
    environment["LEAN_PATH"] = os.pathsep.join(map(str, paths))
    version = subprocess.run(
        [str(COMPILER), "--version"], capture_output=True, text=True, check=True
    ).stdout
    (OUTPUT / "compiler_version.txt").write_text(version, encoding="utf-8", newline="\n")
    modules = [
        "Workhouse/Basic", "Workhouse/VacuumChart",
        "Workhouse/VacuumCompression", "Workhouse",
    ]
    results = []
    log = []
    for module in modules:
        source = LEAN_ROOT / f"{module}.lean"
        target = LIBRARY / f"{module}.olean"
        command = [
            str(COMPILER),
            "-DwarningAsError=true",
            "-o",
            str(target.relative_to(LEAN_ROOT)),
            str(source.relative_to(LEAN_ROOT)),
        ]
        result = subprocess.run(
            command,
            cwd=LEAN_ROOT,
            env=environment,
            capture_output=True,
            text=True,
            encoding="utf-8",
            check=False,
        )
        results.append(
            {
                "module": module,
                "command": command,
                "source_sha256": digest(source),
                "exit_code": result.returncode,
                "stdout": result.stdout,
                "stderr": result.stderr,
                "olean_sha256": digest(target) if result.returncode == 0 else None,
            }
        )
        log.append(
            f"COMMAND: {subprocess.list2cmdline(command)}\n"
            f"EXIT: {result.returncode}\n"
            f"STDOUT:\n{result.stdout}\nSTDERR:\n{result.stderr}\n"
        )
        if result.returncode:
            break
    success = len(results) == len(modules) and all(r["exit_code"] == 0 for r in results)
    report = {
        "schema": "workhouse-lean-build/1",
        "success": success,
        "compiler": str(COMPILER),
        "compiler_sha256": digest(COMPILER),
        "compiler_version": version.strip(),
        "cwd": str(LEAN_ROOT),
        "LEAN_PATH": environment["LEAN_PATH"],
        "dependency_cache_policy": "existing original mathlib package cache, read only",
        "lean_toolchain_sha256": digest(LEAN_ROOT / "lean-toolchain"),
        "lake_manifest_sha256": digest(LEAN_ROOT / "lake-manifest.json"),
        "verification_script_sha256": digest(Path(__file__)),
        "previous_chart_report_sha256": digest(prior_path),
        "preserved_chart_source_sha256": sealed_chart["source_sha256"],
        "axiom_guards": {
            "Workhouse.VacuumCompression.corrected_eq_compression": [
                "propext", "Classical.choice", "Quot.sound"
            ],
            "Workhouse.VacuumCompression.vacuum_projection": [
                "propext", "Classical.choice", "Quot.sound"
            ],
            "Workhouse.VacuumChart.corrected_vacuum_legs": [
                "propext", "Classical.choice", "Quot.sound"
            ],
            "Workhouse.VacuumChart.scalar_vacuum_cancellation": [
                "propext", "Classical.choice", "Quot.sound"
            ],
            "Workhouse.VacuumChart.endpoint_disjoint_cancellation": [
                "propext", "Classical.choice", "Quot.sound"
            ],
        },
        "modules": results,
    }
    (OUTPUT / "strict_build.log").write_text("\n".join(log), encoding="utf-8", newline="\n")
    (OUTPUT / "build_result.json").write_text(
        json.dumps(report, indent=2) + "\n", encoding="utf-8", newline="\n"
    )
    print(f"Strict Lean build: {'PASS' if success else 'FAIL'} ({len(results)} modules)")
    print(version.strip())
    if not success:
        print(results[-1]["stdout"])
        print(results[-1]["stderr"], file=sys.stderr)
    return 0 if success else 1


if __name__ == "__main__":
    raise SystemExit(main())
