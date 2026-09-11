from __future__ import annotations

import sys
from pathlib import Path

SCRIPTS_DIR = Path(__file__).resolve().parents[1] / "scripts"
if str(SCRIPTS_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPTS_DIR))

import ci_scope  # noqa: E402


def test_manual_full_flag(tmp_path: Path) -> None:
    out = tmp_path / "github_output.txt"
    ret = ci_scope.main(["--full", "--github-output", str(out)])
    assert ret == 0
    lines = out.read_text(encoding="utf-8").strip().splitlines()
    assert "full=true" in lines
    assert "lean=true" in lines


def test_doc_files_classify_as_fast_path(tmp_path: Path) -> None:
    out = tmp_path / "github_output.txt"
    files = ["README.md", "docs/README.md", "CLAUDE.md", "CONTRIBUTING.md"]
    ret = ci_scope.main(["--github-output", str(out)] + files)
    assert ret == 0
    lines = out.read_text(encoding="utf-8").strip().splitlines()
    assert "full=false" in lines
    assert "lean=false" in lines


def test_code_and_lean_classify_as_full_path(tmp_path: Path) -> None:
    candidates = [
        ("src/workhouse/invariants/something.py", False),
        ("lean/Workhouse/Something.lean", True),
        ("ledger/results.yaml", False),
        (".github/workflows/ci.yml", False),
        ("Makefile", True),
        ("scripts/bootstrap-lean.sh", True),
    ]
    for idx, (code_file, lean_expected) in enumerate(candidates):
        out = tmp_path / f"github_output_{idx}.txt"
        ret = ci_scope.main(["--github-output", str(out), code_file])
        assert ret == 0
        lines = out.read_text(encoding="utf-8").strip().splitlines()
        assert "full=true" in lines
        assert f"lean={'true' if lean_expected else 'false'}" in lines


def test_unclassified_file_forces_full_path(tmp_path: Path) -> None:
    out = tmp_path / "github_output.txt"
    ret = ci_scope.main(["--github-output", str(out), "random_untracked_script.sh"])
    assert ret == 0
    lines = out.read_text(encoding="utf-8").strip().splitlines()
    assert "full=true" in lines
    assert "lean=false" in lines


def test_missing_base_sha_falls_back_to_full_path(tmp_path: Path) -> None:
    out = tmp_path / "github_output.txt"
    ret = ci_scope.main(["--base", "", "--github-output", str(out)])
    assert ret == 0
    lines = out.read_text(encoding="utf-8").strip().splitlines()
    assert "full=true" in lines
    assert "lean=true" in lines
