"""Kernel-extracted Lean dependencies with source and axiom checks."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[2]
SOURCE = "ledger/lean_dependencies.json"
SOURCE_HASH_MODE = "utf8-lf"
STANDARD_AXIOMS = {"propext", "Classical.choice", "Quot.sound"}
DECLARATION_KINDS = {
    "theorem",
    "axiom",
    "definition",
    "opaque",
    "inductive",
    "constructor",
    "recursor",
    "quotient",
}


def _strings(value) -> bool:
    return isinstance(value, list) and all(isinstance(x, str) and x.strip() for x in value)


def _project_name(name: str) -> bool:
    return name.startswith(("Workhouse.", "_private.Workhouse."))


def _extracted_dependencies(full: str, declarations: dict, reverse: dict) -> set[str]:
    """Follow elaborated local helper constants, stopping at registered theorems."""
    found, visited = set(), {full}
    row = declarations[full]
    pending = [*row["type_dependencies"], *row["proof_dependencies"]]
    while pending:
        item = pending.pop()
        if item in visited:
            continue
        visited.add(item)
        if item in reverse:
            found.add(reverse[item])
        elif item in declarations:
            row = declarations[item]
            pending.extend(row["type_dependencies"])
            pending.extend(row["proof_dependencies"])
    return found


def source_hashes(root: Path) -> dict[str, str]:
    """Fingerprint strict UTF-8 text after only CRLF/CR-to-LF normalization.

    Git can normalize the same Lean input to LF on CI and CRLF on Windows.
    Keep all other characters, including a BOM and meaningful whitespace,
    unchanged. Derivation evidence uses a separate raw-byte hash policy.
    """
    paths = [
        root / "lean" / name
        for name in (
            "Workhouse.lean",
            "ProofDependencies.lean",
            "lean-toolchain",
            "lake-manifest.json",
            "lakefile.toml",
        )
    ]
    paths += sorted((root / "lean/Workhouse").rglob("*.lean"))
    fingerprints = {}
    for path in paths:
        if path.is_file():
            text = path.read_bytes().decode("utf-8").replace("\r\n", "\n").replace("\r", "\n")
            fingerprints[path.relative_to(root).as_posix()] = hashlib.sha256(
                text.encode("utf-8")
            ).hexdigest()
    return fingerprints


def validate(data: dict, root: Path) -> list[str]:
    if not isinstance(data, dict):
        return ["Lean dependency export must be a mapping"]
    errors = []
    if data.get("schema") != "lean-kernel-dependencies/v1":
        errors.append("unsupported Lean dependency schema")
    if data.get("source_hash_mode") != SOURCE_HASH_MODE:
        errors.append(f"Lean source hash mode must be {SOURCE_HASH_MODE}")
    try:
        if data.get("source_sha256") != source_hashes(root):
            errors.append(
                "Lean dependency export is stale; run scripts/export_lean_dependencies.py"
            )
    except (OSError, UnicodeError) as exc:
        errors.append(f"cannot fingerprint Lean UTF-8 sources: {exc}")
    try:
        registry = yaml.safe_load((root / "ledger/theorems.yaml").read_text(encoding="utf-8"))
        entries = registry.get("theorems") if isinstance(registry, dict) else None
        if not isinstance(entries, list) or not all(
            isinstance(row, dict) and isinstance(row.get("name"), str) and row["name"].strip()
            for row in entries
        ):
            return [*errors, "registered theorem inventory must contain named mappings"]
        registered = {row["name"] for row in entries}
        if len(registered) != len(entries):
            errors.append("registered theorem inventory contains duplicate names")
    except (OSError, UnicodeError, yaml.YAMLError) as exc:
        return [*errors, f"cannot read registered theorem inventory: {exc}"]
    theorems = data.get("theorems", {})
    if not isinstance(theorems, dict):
        return [*errors, "theorems must be a mapping"]
    if set(theorems) != registered:
        errors.append("Lean kernel export and registered theorem inventory differ")
    declarations = data.get("declarations", {})
    if not isinstance(declarations, dict):
        return [*errors, "declarations must be a mapping"]
    valid_declarations = {}
    for full, row in declarations.items():
        if not isinstance(full, str) or not _project_name(full) or not isinstance(row, dict):
            errors.append(f"{full}: malformed project declaration")
            continue
        if not isinstance(row.get("kind"), str) or row["kind"] not in DECLARATION_KINDS:
            errors.append(f"{full}: unknown declaration kind")
        valid = True
        for field in ("type_dependencies", "proof_dependencies", "axioms"):
            values = row.get(field)
            if not _strings(values):
                errors.append(f"{full}: {field} must be a list of nonempty strings")
                valid = False
            elif len(values) != len(set(values)):
                errors.append(f"{full}: duplicate {field}")
        if valid:
            valid_declarations[full] = row
    for full, row in valid_declarations.items():
        for dependency in [*row["type_dependencies"], *row["proof_dependencies"]]:
            if _project_name(dependency) and dependency not in valid_declarations:
                errors.append(f"{full}: local kernel dependency missing: {dependency}")
            if dependency in valid_declarations:
                inherited = set(valid_declarations[dependency]["axioms"])
                if not inherited <= set(row["axioms"]):
                    errors.append(f"{full}: transitive axiom record omits local dependency axioms")
    reverse = {}
    valid_theorems = {}
    for name, row in theorems.items():
        if not isinstance(name, str) or not isinstance(row, dict):
            errors.append(f"{name}: theorem record must be a named mapping")
            continue
        full = row.get("qualified_name")
        if not isinstance(full, str) or full.rsplit(".", 1)[-1] != name:
            errors.append(f"{name}: qualified theorem name does not match registered name")
            continue
        if full not in valid_declarations or valid_declarations[full]["kind"] != "theorem":
            errors.append(f"{name}: theorem missing from elaborated environment")
            continue
        axioms = set(valid_declarations[full]["axioms"])
        if axioms - STANDARD_AXIOMS:
            errors.append(f"{name}: nonstandard axioms {sorted(axioms - STANDARD_AXIOMS)}")
        dependencies = row.get("project_dependencies")
        if not _strings(dependencies):
            errors.append(f"{name}: project_dependencies must be a list of nonempty strings")
            continue
        if len(dependencies) != len(set(dependencies)):
            errors.append(f"{name}: duplicate project theorem dependencies")
        if not set(dependencies) <= registered - {name}:
            errors.append(f"{name}: unresolved or self-referential theorem dependency")
        reverse[full] = name
        valid_theorems[name] = row
    for name, row in valid_theorems.items():
        expected = _extracted_dependencies(row["qualified_name"], valid_declarations, reverse)
        if set(row["project_dependencies"]) != expected:
            errors.append(
                f"{name}: project dependencies disagree with elaborated constants: "
                f"expected {sorted(expected)}"
            )
    # A Lean theorem cannot recursively depend on itself through other theorems.
    # Recursive local definitions are legitimate and were handled by visited sets.
    visited, active = set(), set()

    def visit(name):
        if name in active:
            errors.append(f"{name}: circular registered theorem dependency")
            return
        if name in visited:
            return
        active.add(name)
        for dependency in valid_theorems.get(name, {}).get("project_dependencies", []):
            visit(dependency)
        active.remove(name)
        visited.add(name)

    for name in valid_theorems:
        visit(name)
    return errors


def load(*, root: Path | None = None) -> dict:
    root = root or ROOT
    data = json.loads((root / SOURCE).read_text(encoding="utf-8"))
    errors = validate(data, root)
    if errors:
        raise ValueError("\n".join(errors))
    return data


def edge_records(data: dict | None = None) -> list[dict]:
    data = data if data is not None else load()
    return [
        dict(
            src=f"LEAN:{name}",
            dst=f"LEAN:{dependency}",
            type="depends_on",
            how="derived",
            source=f"{SOURCE}#{row['qualified_name']}",
        )
        for name, row in sorted(data["theorems"].items())
        for dependency in row["project_dependencies"]
    ]


def detail(row: dict, data: dict) -> str:
    full = row["qualified_name"]
    axioms = data["declarations"][full]["axioms"]
    return (
        f"Lean declaration: {full}\nKernel dependency record: {SOURCE}#{full}\n"
        f"Project theorem dependencies: {', '.join(row['project_dependencies']) or 'none'}\n"
        f"Transitive axioms: {', '.join(axioms) or 'none'}"
    )
