"""Classify changed repository inputs for CI verification routing.

Selects either the fast documentation/help path (full=false) or full repository
verification (full=true: Lean proofs, catalogue check, full test suite).
"""

from __future__ import annotations

import argparse
import ast
import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PERMITTED_HELP_PYTHON_FILES = {"src/workhouse/cli.py"}
ALLOWLIST_ROOT_FILES = {
    "README.md",
    "INDEX.md",
    "AGENTS.md",
    "CLAUDE.md",
    "CONTRIBUTING.md",
    "LICENSE",
    "NOTICE",
    "docs/documentation_manifest.json",
}

LEAN_PATHS = {"Makefile", "scripts/bootstrap-lean.sh"}


def has_lean_changes(files: list[str]) -> bool:
    for f in files:
        posix = Path(f).as_posix()
        if posix.startswith("lean/") or posix in LEAN_PATHS:
            return True
    return False


def load_maintained_docs(root: Path = ROOT) -> set[str]:
    manifest_path = root / "docs" / "documentation_manifest.json"
    maintained = set(ALLOWLIST_ROOT_FILES)
    if manifest_path.is_file():
        try:
            data = json.loads(manifest_path.read_text(encoding="utf-8"))
            for p in data.get("maintained", []):
                maintained.add(Path(p).as_posix())
        except Exception:
            pass
    return maintained


def is_doc_path(path: str, maintained: set[str]) -> bool:
    posix = Path(path).as_posix()
    if posix in maintained:
        return True
    return bool(
        (posix.startswith("docs/") or posix.startswith("graph-tasks/")) and posix.endswith(".md")
    )


def strip_help_ast(tree: ast.AST) -> ast.AST:
    """Normalize AST by replacing docstrings and help/description kwarg strings with constants."""

    class StripTransformer(ast.NodeTransformer):
        def visit_Expr(self, node: ast.Expr) -> ast.AST:
            if isinstance(node.value, ast.Constant) and isinstance(node.value.value, str):
                node.value.value = "__STRIPPED_DOCSTRING__"
            return self.generic_visit(node)

        def visit_Call(self, node: ast.Call) -> ast.AST:
            for kw in node.keywords:
                if (
                    kw.arg in ("help", "description", "epilog")
                    and isinstance(kw.value, ast.Constant)
                    and isinstance(kw.value.value, str)
                ):
                    kw.value.value = "__STRIPPED_HELP__"
            return self.generic_visit(node)

    return StripTransformer().visit(tree)


def is_permitted_help_edit(path: str, base_sha: str | None, root: Path = ROOT) -> bool:
    posix = Path(path).as_posix()
    if posix not in PERMITTED_HELP_PYTHON_FILES:
        return False
    current_file = root / posix
    if not current_file.is_file():
        return False
    try:
        current_ast = ast.parse(current_file.read_text(encoding="utf-8"))
        current_norm = ast.dump(strip_help_ast(current_ast), include_attributes=False)
    except Exception:
        return False

    if not base_sha:
        return False

    try:
        res = subprocess.run(
            ["git", "show", f"{base_sha}:{posix}"],
            cwd=root,
            capture_output=True,
            check=False,
            text=True,
            encoding="utf-8",
        )
        if res.returncode != 0:
            return False
        base_ast = ast.parse(res.stdout)
        base_norm = ast.dump(strip_help_ast(base_ast), include_attributes=False)
        return current_norm == base_norm
    except Exception:
        return False


def get_changed_files(
    base_sha: str | None, head_sha: str | None, root: Path = ROOT
) -> list[str] | None:
    if not base_sha or base_sha.strip("0") == "":
        return None
    head = head_sha or "HEAD"
    try:
        cmd = ["git", "diff", "--name-only", f"{base_sha}...{head}"]
        res = subprocess.run(
            cmd, cwd=root, capture_output=True, check=False, text=True, encoding="utf-8"
        )
        if res.returncode != 0:
            cmd = ["git", "diff", "--name-only", base_sha, head]
            res = subprocess.run(
                cmd, cwd=root, capture_output=True, check=False, text=True, encoding="utf-8"
            )
            if res.returncode != 0:
                return None
        return [line.strip().replace("\\", "/") for line in res.stdout.splitlines() if line.strip()]
    except Exception:
        return None


def classify_changes(
    files: list[str], base_sha: str | None = None, root: Path = ROOT
) -> tuple[bool, str]:
    if not files:
        return False, "No changed files detected"
    maintained = load_maintained_docs(root)
    for f in files:
        if is_doc_path(f, maintained):
            continue
        if is_permitted_help_edit(f, base_sha, root=root):
            continue
        return True, f"{f} requires full verification"
    return False, "All changes are documentation or permitted help edits"


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Classify changed files for CI scope selection.")
    parser.add_argument("--base", default=None, help="Base commit SHA or ref")
    parser.add_argument("--head", default=None, help="Head commit SHA or ref")
    parser.add_argument("--full", action="store_true", help="Force full verification")
    parser.add_argument("--github-output", default=None, help="Path to $GITHUB_OUTPUT file")
    parser.add_argument("files", nargs="*", help="Explicit changed files (optional)")

    args = parser.parse_args(argv)

    if args.full:
        full = True
        lean = True
        reason = "Manual full run requested (--full)"
    elif args.files:
        full, reason = classify_changes(args.files, base_sha=args.base)
        lean = has_lean_changes(args.files)
    else:
        changed = get_changed_files(args.base, args.head)
        if changed is None:
            full = True
            lean = True
            reason = "Could not determine changed files; falling back to full verification"
        else:
            full, reason = classify_changes(changed, base_sha=args.base)
            lean = has_lean_changes(changed)

    if args.github_output:
        out_path = Path(args.github_output)
        out_path.parent.mkdir(parents=True, exist_ok=True)
        flag = "true" if full else "false"
        lean_flag = "true" if lean else "false"
        with out_path.open("a", encoding="utf-8", newline="\n") as f:
            f.write(f"full={flag}\n")
            f.write(f"lean={lean_flag}\n")

    flag = "true" if full else "false"
    lean_flag = "true" if lean else "false"
    print(f"CI Scope: full={flag} lean={lean_flag} ({reason})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
