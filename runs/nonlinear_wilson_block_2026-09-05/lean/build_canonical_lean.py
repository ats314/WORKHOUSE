"""Strict local Lean build using the already pinned read-only toolchain cache."""

import hashlib
import json
import os
from pathlib import Path
import subprocess

ROOT = Path.cwd()
HERE = Path(__file__).resolve().parent
OUT = HERE / "canonical_lean_build"
OUT.mkdir(exist_ok=False)
previous = json.loads((ROOT / "runs/wilson_creator_parent_2026-09-05/lean/build_result.json").read_text(encoding="utf-8"))
compiler = Path(previous["compiler"])
digest = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
assert digest(compiler) == previous["compiler_sha256"]
env = os.environ.copy()
env["LEAN_PATH"] = previous["LEAN_PATH"]
modules = ["Workhouse/Basic", "Workhouse/VacuumChart", "Workhouse/VacuumCompression", "Workhouse/RootedScalarBounds", "Workhouse/CreatorParent", "Workhouse/GlobalWilsonVertical", "Workhouse"]
rows = []
with (OUT / "strict_build.log").open("x", encoding="utf-8", newline="\n") as log:
    for module in modules:
        source = ROOT / "lean" / (module + ".lean")
        target = ROOT / "lean/.lake/build/lib/lean" / (module + ".olean")
        target.parent.mkdir(parents=True, exist_ok=True)
        command = [str(compiler), "-DwarningAsError=true", "-o", str(target), str(source)]
        result = subprocess.run(command, cwd=ROOT / "lean", env=env, capture_output=True, text=True, encoding="utf-8")
        log.write("COMMAND: " + " ".join(command) + "\n" + result.stdout + result.stderr)
        log.flush()
        row = {"module": module, "command": command, "returncode": result.returncode, "source_sha256": digest(source), "stdout": result.stdout, "stderr": result.stderr}
        if result.returncode == 0:
            row["olean_sha256"] = digest(target)
        rows.append(row)
        print(module, result.returncode, flush=True)
        if result.returncode != 0:
            break
report = {"success": len(rows) == len(modules) and all(r["returncode"] == 0 for r in rows), "compiler": str(compiler), "compiler_sha256": digest(compiler), "compiler_version": previous["compiler_version"], "LEAN_PATH": env["LEAN_PATH"], "dependency_cache_policy": "existing original mathlib package cache, read only", "lean_toolchain_sha256": digest(ROOT / "lean/lean-toolchain"), "lake_manifest_sha256": digest(ROOT / "lean/lake-manifest.json"), "build_script_sha256": digest(Path(__file__)), "modules": rows}
(OUT / "build_result.json").write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8", newline="\n")
if not report["success"]:
    raise SystemExit(1)
