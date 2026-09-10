"""Located derivation statements and their explicitly scoped formal support.

Source status and machine verification remain independent. A citation, a
dependency, or a supporting lemma never silently promotes a whole statement.
"""

from __future__ import annotations

import hashlib
import re
from pathlib import Path

import yaml

from .constants import EVIDENCE, STATUSES

ROOT = Path(__file__).resolve().parents[2]
SOURCE = "ledger/derivation_statements.yaml"
STATEMENT_ID = re.compile(r"DERIV:[A-Z0-9_:-]+\Z")


def _strings(value) -> bool:
    return isinstance(value, list) and all(isinstance(x, str) and x.strip() for x in value)


def load(*, root: Path | None = None) -> dict:
    return yaml.safe_load(((root or ROOT) / SOURCE).read_text(encoding="utf-8"))


def validate(
    data: dict,
    *,
    root: Path | None = None,
    theorem_names: set[str] | None = None,
    complete: bool = True,
) -> list[str]:
    root = root or ROOT
    errors = []
    if not isinstance(data, dict):
        return ["derivation statement inventory must be a mapping"]
    if data.get("schema") != "derivation-statements/v1":
        errors.append("unsupported derivation statement schema")
    documents = data.get("documents", [])
    if not isinstance(documents, list) or not documents:
        return [*errors, "documents must be a nonempty list"]
    # When the native citation register is present, an existing but unrelated
    # CITE id is not sufficient provenance for this source file.
    citation_paths = None
    citation_file = root / "ledger/documents.yaml"
    if citation_file.is_file():
        try:
            register = yaml.safe_load(citation_file.read_text(encoding="utf-8"))
            aliases = register.get("aliases") if isinstance(register, dict) else None
            if not isinstance(aliases, list) or not all(isinstance(x, dict) for x in aliases):
                errors.append("native citation register must contain alias mappings")
            else:
                citation_paths = {
                    f"CITE:{row['alias']}": row["path"]
                    for row in aliases
                    if isinstance(row.get("alias"), str) and isinstance(row.get("path"), str)
                }
        except (OSError, UnicodeError, yaml.YAMLError) as exc:
            errors.append(f"cannot read native citation register: {exc}")
    ids, sources, paths = set(), set(), set()
    statements = []
    for doc in documents:
        if not isinstance(doc, dict):
            errors.append("document inventory entries must be mappings")
            continue
        did, relative = doc.get("id", ""), doc.get("path", "")
        if not isinstance(did, str) or not did.startswith("CITE:") or did in sources:
            errors.append(f"{did}: missing or duplicate native citation id")
        if isinstance(did, str):
            sources.add(did)
        if not isinstance(relative, str) or not relative:
            errors.append(f"{did}: source must be a top-level derivation path")
            continue
        if (
            citation_paths is not None
            and isinstance(did, str)
            and citation_paths.get(did) != relative
        ):
            errors.append(f"{did}: native citation does not identify source {relative}")
        path = Path(relative)
        if (
            path.is_absolute()
            or ".." in path.parts
            or "\\" in relative
            or path.parent.as_posix() != "docs/derivations"
            or path.suffix != ".md"
            or not (root / path).resolve().is_relative_to(root.resolve())
        ):
            errors.append(f"{did}: source must be a top-level derivation path")
            continue
        if relative in paths:
            errors.append(f"{did}: duplicate source path {relative}")
        paths.add(relative)
        try:
            contents = (root / path).read_bytes()
            text = contents.decode("utf-8-sig")
        except (OSError, UnicodeError) as exc:
            errors.append(f"{did}: unreadable source: {exc}")
            continue
        if hashlib.sha256(contents).hexdigest() != doc.get("sha256"):
            errors.append(f"{did}: source SHA-256 mismatch; review the changed derivation")
        rows = doc.get("statements", [])
        if not isinstance(rows, list) or not rows:
            errors.append(f"{did}: statements must be a nonempty list")
            continue
        for row in rows:
            if not isinstance(row, dict):
                errors.append(f"{did}: statement entries must be mappings")
                continue
            sid = row.get("id", "")
            if not isinstance(sid, str) or not STATEMENT_ID.fullmatch(sid) or sid in ids:
                errors.append(f"{sid}: malformed or duplicate statement id")
            if isinstance(sid, str) and STATEMENT_ID.fullmatch(sid) and sid not in ids:
                ids.add(sid)
                statements.append(row)
            for field in ("statement", "locator", "anchor"):
                if not isinstance(row.get(field), str) or not row[field].strip():
                    errors.append(f"{sid}: missing {field}")
            if isinstance(row.get("anchor"), str) and row["anchor"] not in text:
                errors.append(f"{sid}: source anchor is absent")
            if not isinstance(row.get("status"), str) or row["status"] not in STATUSES:
                errors.append(f"{sid}: unknown mathematical status")
            evidence = row.get("evidence", "prose-only")
            if not isinstance(evidence, str) or evidence not in EVIDENCE:
                errors.append(f"{sid}: unknown evidence vocabulary")
            for field in ("hypotheses", "depends_on", "lean"):
                if not _strings(row.get(field)):
                    errors.append(f"{sid}: {field} must be a list of nonempty strings")
                elif len(row[field]) != len(set(row[field])):
                    errors.append(f"{sid}: duplicate {field}")
            if not isinstance(row.get("remaining"), str):
                errors.append(f"{sid}: remaining formalization must be explicit")
            if not row.get("lean") and not str(row.get("remaining", "")).strip():
                errors.append(f"{sid}: neither a full proof nor a remaining obligation is recorded")
            supports = row.get("lean_support", [])
            if not isinstance(supports, list):
                errors.append(f"{sid}: lean_support must be a list")
                supports = []
            names = list(row["lean"]) if _strings(row.get("lean")) else []
            for support in supports:
                if not isinstance(support, dict) or not all(
                    isinstance(support.get(field), str) and support[field].strip()
                    for field in ("name", "scope")
                ):
                    errors.append(f"{sid}: supporting Lean lemmas need a name and exact scope")
                if isinstance(support, dict) and isinstance(support.get("name"), str):
                    names.append(support["name"])
            if theorem_names is not None:
                for name in names:
                    if name not in theorem_names:
                        errors.append(f"{sid}: unregistered Lean declaration {name}")
    if complete:
        actual = {p.relative_to(root).as_posix() for p in (root / "docs/derivations").glob("*.md")}
        if actual != paths:
            errors.append(
                f"derivation inventory mismatch: missing={sorted(actual - paths)}, "
                f"extra={sorted(paths - actual)}"
            )
    dependencies = {
        row["id"]: row["depends_on"] if _strings(row.get("depends_on")) else []
        for row in statements
    }
    for sid, parents in dependencies.items():
        for parent in parents:
            if parent not in ids:
                errors.append(f"{sid}: unresolved statement dependency {parent}")
    visited, active = set(), set()

    def visit(sid):
        if sid in active:
            errors.append(f"{sid}: circular derivation dependency")
            return
        if sid in visited:
            return
        active.add(sid)
        for parent in dependencies.get(sid, []):
            visit(parent)
        active.remove(sid)
        visited.add(sid)

    for sid in dependencies:
        visit(sid)
    return errors


def _checked(data=None, *, root=None):
    root = root or ROOT
    data = data if data is not None else load(root=root)
    theorems = yaml.safe_load((root / "ledger/theorems.yaml").read_text(encoding="utf-8"))[
        "theorems"
    ]
    problems = validate(data, root=root, theorem_names={row["name"] for row in theorems})
    if problems:
        raise ValueError("derivation statement problems:\n" + "\n".join(problems))
    return data


def claim_records(data=None, *, root=None) -> list[dict]:
    data = _checked(data, root=root)
    records = []
    for doc in data["documents"]:
        for row in doc["statements"]:
            full = row.get("lean", [])
            supports = row.get("lean_support", [])
            detail = [
                "Hypotheses: " + "; ".join(row["hypotheses"]),
                "Whole-statement Lean declarations: " + (", ".join(full) or "none"),
                "Remaining formalization: " + (row["remaining"] or "none recorded"),
            ]
            detail += [f"Lean support {s['name']}: {s['scope']}" for s in supports]
            records.append(
                dict(
                    id=row["id"],
                    kind="result",
                    tier=3,
                    statement=row["statement"],
                    where=f"{doc['path']} ({row['locator']})",
                    cites=doc["id"],
                    status=row["status"],
                    evidence=row.get("evidence", "prose-only"),
                    detail="\n".join(detail),
                    related=sorted(
                        {
                            doc["id"],
                            *row["depends_on"],
                            *(f"LEAN:{name}" for name in full),
                            *(f"LEAN:{s['name']}" for s in supports),
                        }
                    ),
                )
            )
    return records


def edge_records(data=None, *, root=None) -> list[dict]:
    data = _checked(data, root=root)
    edges = []

    def add(src, dst, kind, location):
        edges.append(dict(src=src, dst=dst, type=kind, how="curated", source=location))

    for doc in data["documents"]:
        for row in doc["statements"]:
            sid = row["id"]
            location = f"{SOURCE}#{sid} ({row['locator']})"
            add(doc["id"], sid, "contains", location)
            add(sid, doc["id"], "cites", location)
            for parent in row["depends_on"]:
                add(sid, parent, "depends_on", location)
            for name in row["lean"]:
                add(f"LEAN:{name}", sid, "formalizes", location)
            for support in row.get("lean_support", []):
                add(
                    sid,
                    f"LEAN:{support['name']}",
                    "supported_by",
                    f"{location}: {support['scope']}",
                )
    return edges
