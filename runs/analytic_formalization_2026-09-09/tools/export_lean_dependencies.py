"""Strictly build Lean, then export dependencies from elaborated proof terms.

Run with the repository Python environment. Source changes, missing registered
theorems and nonstandard axioms fail before replacing the generated record.
"""

from __future__ import annotations

import json
import os
import re
import shutil
import subprocess
from pathlib import Path

import yaml

from workhouse import lean_dependencies as D

ROOT = Path(__file__).resolve().parents[1]


def main():
    lake = shutil.which("lake")
    if lake is None:
        raise SystemExit("Install the pinned Lean toolchain; lake is not on PATH.")
    before = D.source_hashes(ROOT)
    if os.name == "nt":
        # Concurrent Lean processes can fail to memory-map the same shared
        # mathlib cache files on Windows. Build project targets one at a time;
        # each still uses Lake's complete dependency and strict-warning checks.
        imports = (ROOT / "lean/Workhouse.lean").read_text(encoding="utf-8")
        for module in re.findall(r"^import (Workhouse\.\w+)\s*$", imports, re.MULTILINE):
            subprocess.run([lake, "build", module, "--wfail"], cwd=ROOT / "lean", check=True)
    subprocess.run([lake, "build", "--wfail"], cwd=ROOT / "lean", check=True)
    exported = subprocess.run(
        [lake, "env", "lean", "-DwarningAsError=true", "ProofDependencies.lean"],
        cwd=ROOT / "lean",
        check=True,
        capture_output=True,
        text=True,
        encoding="utf-8",
    )
    prefix = "WORKHOUSE_DEPENDENCY "
    rows = [
        json.loads(line[len(prefix) :])
        for line in exported.stdout.splitlines()
        if line.startswith(prefix)
    ]
    declarations = {row["name"]: {k: v for k, v in row.items() if k != "name"} for row in rows}
    registered = {
        row["name"]
        for row in yaml.safe_load((ROOT / "ledger/theorems.yaml").read_text(encoding="utf-8"))[
            "theorems"
        ]
    }
    names = {}
    for full, row in declarations.items():
        bare = full.rsplit(".", 1)[-1]
        if row["kind"] == "theorem" and bare in registered:
            if bare in names:
                raise ValueError(f"Ambiguous registered theorem: {bare}")
            names[bare] = full
    reverse = {full: bare for bare, full in names.items()}

    def dependencies(full):
        # Traverse local definitions/helpers until the next registered theorem;
        # that theorem's own outgoing edges retain subsequent dependencies.
        found, visited = set(), {full}
        pending = list(declarations[full]["type_dependencies"])
        pending += declarations[full]["proof_dependencies"]
        while pending:
            item = pending.pop()
            if item in visited:
                continue
            visited.add(item)
            if item in reverse:
                found.add(reverse[item])
            elif item in declarations:
                pending.extend(declarations[item]["type_dependencies"])
                pending.extend(declarations[item]["proof_dependencies"])
        return sorted(found)

    data = dict(
        schema="lean-kernel-dependencies/v1",
        source_hash_mode=D.SOURCE_HASH_MODE,
        source_sha256=before,
        extraction=(
            "Elaborated type/proof constants; local definitions traversed "
            "to the next registered theorem."
        ),
        theorems={
            bare: dict(qualified_name=full, project_dependencies=dependencies(full))
            for bare, full in sorted(names.items())
        },
        declarations=dict(sorted(declarations.items())),
    )
    problems = D.validate(data, ROOT)
    if problems:
        raise ValueError("\n".join(problems))
    output = ROOT / D.SOURCE
    output.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"Exported {len(names)} theorems, {len(declarations)} declarations: {output}")


if __name__ == "__main__":
    main()
