"""The external discovery scope: declared workstation roots, never followed links."""

from __future__ import annotations

import json
import os
import subprocess
import sys
from pathlib import Path
from types import SimpleNamespace

import pytest
import yaml

from workhouse import discovery_scope as S

REPO = Path(__file__).resolve().parents[1]
JUNCTIONS = [
    "01_PROOFS",
    "02_APPENDICES",
    "03_MANUSCRIPTS",
    "04_SIMULATIONS",
    "05_LEAN",
    "06_RESEARCH_DOCS",
    "08_REFERENCE_PAPERS",
    "10_ALREADY_REVIEWED",
    "11_FUNZONE",
    "SYNTH_COPY",
    "PAPERS",
    "FINAL PAPERS",
    "HODGE RUNS",
    "o4",
    "TWO CUBE B6",
    "SIMULATIONS",
    "organized_experiments",
    "WORKHOUSE-autonomous-20260905",
    "09_ARCHIVE/glacial_uploads",
    "09_ARCHIVE/pdftooltest",
    "09_ARCHIVE/session_logs",
    "worktrees/workspace-organization-20260910",
]


def minimal(**overrides) -> dict:
    data = {
        "schema": S.SCHEMA,
        "version": 1,
        "roots": [{"label": "notes", "path": "notes", "tier": 1}],
    }
    data.update(overrides)
    return data


def make_junction(link: Path, target: Path) -> bool:
    """Create an NTFS junction; False when the host cannot."""
    if sys.platform != "win32":
        return False
    result = subprocess.run(
        ["cmd", "/c", "mklink", "/J", str(link), str(target)], capture_output=True, text=True
    )
    return result.returncode == 0 and os.path.isjunction(link)


def make_symlink(link: Path, target: Path) -> bool:
    try:
        link.symlink_to(target, target_is_directory=target.is_dir())
    except (OSError, NotImplementedError):
        return False
    return link.is_symlink()


def test_glob_patterns_match_posix_relative_paths_and_prune_directories():
    matcher = S.Matcher(["GITHUB/**", "**/pytest-*/**", "*.log", "docs/?.md", "FINAL PAPERS/**"])
    assert matcher.match("GITHUB") == "GITHUB/**"
    assert matcher.match("GITHUB/deep/file.md") == "GITHUB/**"
    assert matcher.match("a/b/pytest-1") == "**/pytest-*/**"
    assert matcher.match("pytest-1/x.md") == "**/pytest-*/**"
    assert matcher.match("run.log") == "*.log"
    assert matcher.match("sub/run.log") is None
    assert matcher.match("docs/a.md") == "docs/?.md"
    assert matcher.match("docs/ab.md") is None
    assert matcher.match("final papers/x.tex") == "FINAL PAPERS/**"
    assert matcher.match("GITHUBX") is None
    assert not S.Matcher([])


def test_checked_in_scope_file_parses_validates_and_keeps_tier_three_off():
    path = REPO / S.SCOPE_PATH
    raw = path.read_bytes()
    header = raw.decode("utf-8").split("schema:")[0]
    assert "WORKSTATION paths" in header and "SKIPPED WITH AN EXPLICIT REPORT" in header
    scope = S.parse_scope(yaml.safe_load(raw), path=path)
    assert scope.schema == S.SCHEMA and scope.version >= 1
    labels = [root.label for root in scope.roots]
    assert len(labels) == len(set(labels))
    assert all(root.tier in S.TIERS for root in scope.roots)
    assert all(not root.enabled for root in scope.roots if root.tier == 3)
    assert any(root.enabled for root in scope.roots if root.tier == 1)
    assert any(root.enabled for root in scope.roots if root.tier == 2)
    assert all(not Path(root.path).is_absolute() and ".." not in root.path for root in scope.roots)
    for junction in JUNCTIONS:
        assert f"{junction}/**" in scope.exclude
    for checkout in ("REPO/**", "worktrees/**", "ALL THEORY/WORKHOUSE/**", "quarantine/**"):
        assert checkout in scope.exclude
    assert {".git", ".venv", "__pycache__", ".graph-state", "pytest-*"} <= set(scope.exclude_names)
    assert {"REPO/ledger", "REPO/index"} <= set(scope.protected)
    inbox = next(root for root in scope.roots if root.path == "INBOX")
    assert inbox.enabled and inbox.tier == 1


@pytest.mark.parametrize(
    "broken, message",
    [
        (minimal(schema="other/v1"), "schema"),
        (minimal(version=0), "version"),
        (minimal(roots=[{"label": "a b", "path": "x", "tier": 1}]), "label"),
        (minimal(roots=[{"label": "a", "path": "C:/x", "tier": 1}]), "relative"),
        (minimal(roots=[{"label": "a", "path": "/x", "tier": 1}]), "relative"),
        (minimal(roots=[{"label": "a", "path": "../x", "tier": 1}]), "climb"),
        (minimal(roots=[{"label": "a", "path": "x", "tier": 4}]), "tier"),
        (minimal(roots=[{"label": "a", "path": "x", "tier": 1, "extra": 1}]), "unknown keys"),
        (minimal(roots=[{"label": "a", "path": "x", "tier": 1, "max_depth": -1}]), "max_depth"),
        (
            minimal(
                roots=[
                    {"label": "a", "path": "x", "tier": 1},
                    {"label": "a", "path": "y", "tier": 2},
                ]
            ),
            "duplicate",
        ),
        (minimal(exclude_names=["a/b"]), "directory names"),
        (minimal(exclude=["/abs/**"]), "relative"),
        (minimal(unexpected=True), "unknown keys"),
    ],
)
def test_malformed_scope_names_the_offending_key(broken, message):
    with pytest.raises(ValueError, match=message):
        S.parse_scope(broken)


def test_local_override_disables_enables_and_rejects_unknown_labels():
    scope = S.parse_scope(
        minimal(
            roots=[
                {"label": "a", "path": "x", "tier": 1},
                {"label": "b", "path": "y", "tier": 3, "enabled": False},
            ]
        )
    )
    S.apply_local(scope, {"schema": S.LOCAL_SCHEMA, "disable": ["a"], "enable": ["b"]})
    assert [root.enabled for root in scope.roots] == [False, True]
    assert scope.local_disabled == ("a",) and scope.local_enabled == ("b",)
    with pytest.raises(ValueError, match="unknown root labels"):
        S.apply_local(scope, {"schema": S.LOCAL_SCHEMA, "disable": ["nope"]})
    with pytest.raises(ValueError, match="both enables and disables"):
        S.apply_local(scope, {"schema": S.LOCAL_SCHEMA, "disable": ["a"], "enable": ["a"]})
    with pytest.raises(ValueError, match="schema"):
        S.apply_local(scope, {"schema": S.SCHEMA})


def _checkout(tmp_path: Path, *, workspace: bool = True) -> Path:
    base = tmp_path / "ws"
    checkout = base / "REPO"
    (checkout / "graph-tasks/discovery").mkdir(parents=True)
    if workspace:
        (base / S.WORKSPACE_MARKER).write_text(
            json.dumps({"canonical_repository": "REPO"}), encoding="utf-8"
        )
    return checkout


def _write_scope(checkout: Path, data: dict) -> None:
    (checkout / S.SCOPE_PATH).write_text(yaml.safe_dump(data), encoding="utf-8")


def test_base_resolution_prefers_environment_then_local_file_then_workspace_marker(
    tmp_path, monkeypatch
):
    checkout = _checkout(tmp_path)
    _write_scope(checkout, minimal())
    monkeypatch.delenv(S.BASE_ENV, raising=False)
    scope = S.load_scope(checkout)
    assert scope is not None
    assert scope.base == (tmp_path / "ws").resolve() and scope.base_source == "workspace_marker"
    assert scope.protected == ("REPO/ledger", "REPO/index")
    local = checkout / S.LOCAL_PATH
    local.parent.mkdir(parents=True)
    other = tmp_path / "other"
    other.mkdir()
    local.write_text(
        yaml.safe_dump({"schema": S.LOCAL_SCHEMA, "base": str(other), "disable": ["notes"]}),
        encoding="utf-8",
    )
    scope = S.load_scope(checkout)
    assert scope.base == other.resolve() and scope.base_source == "local_override"
    assert not scope.roots[0].enabled
    env_base = tmp_path / "env"
    env_base.mkdir()
    monkeypatch.setenv(S.BASE_ENV, str(env_base))
    scope = S.load_scope(checkout)
    assert scope.base == env_base.resolve() and scope.base_source == "environment"


def test_missing_scope_file_means_no_external_roots_and_no_workspace_means_no_base(
    tmp_path, monkeypatch
):
    monkeypatch.delenv(S.BASE_ENV, raising=False)
    assert S.load_scope(_checkout(tmp_path)) is None
    checkout = _checkout(tmp_path / "second", workspace=False)
    _write_scope(checkout, minimal())
    # pytest's temporary directory may itself sit under a real workspace
    # (the repository's basetemp does); hide every ancestor marker.
    monkeypatch.setattr(S, "WORKSPACE_MARKER", "WORKSPACE.absent-for-this-test.json")
    scope = S.load_scope(checkout)
    assert scope.base is None and scope.base_source is None
    rows = S.resolve_roots(scope, checkout)
    assert rows[0]["skipped"] == "base_unavailable" and rows[0]["present"] is False


def test_resolve_roots_reports_absent_disabled_unsafe_and_present(tmp_path, monkeypatch):
    checkout = _checkout(tmp_path)
    base = tmp_path / "ws"
    (base / "present").mkdir()
    (base / "REPO/ledger").mkdir(parents=True)
    (base / "file.md").write_text("x", encoding="utf-8")
    _write_scope(
        checkout,
        minimal(
            roots=[
                {"label": "present", "path": "present", "tier": 1},
                {"label": "absent", "path": "missing", "tier": 1},
                {"label": "off", "path": "present", "tier": 3, "enabled": False},
                {"label": "self", "path": "REPO", "tier": 1},
                {"label": "ledger", "path": "REPO/ledger", "tier": 1},
                {"label": "file", "path": "file.md", "tier": 1},
                {"label": "base", "path": ".", "tier": 1, "max_depth": 0},
            ]
        ),
    )
    monkeypatch.delenv(S.BASE_ENV, raising=False)
    scope = S.load_scope(checkout)
    rows = {row["label"]: row for row in S.resolve_roots(scope, checkout)}
    assert rows["present"]["skipped"] is None and rows["present"]["present"]
    assert rows["absent"]["skipped"] == "absent" and not rows["absent"]["present"]
    assert rows["off"]["skipped"] == "disabled" and rows["off"]["present"]
    assert rows["self"]["skipped"] == "unsafe_path"
    assert rows["ledger"]["skipped"] == "unsafe_path"
    assert rows["file"]["skipped"] == "not_a_directory"
    assert rows["base"]["skipped"] is None and rows["base"]["absolute"] == str(base.resolve())


def test_safe_external_refuses_checkout_protected_and_missing_paths(tmp_path):
    checkout = tmp_path / "REPO"
    (checkout / "docs").mkdir(parents=True)
    protected = tmp_path / "REPO/ledger"
    protected.mkdir()
    outside = tmp_path / "outside"
    outside.mkdir()
    assert S.safe_external(outside, checkout, [protected])
    assert not S.safe_external(checkout, checkout, [])
    assert not S.safe_external(checkout / "docs", checkout, [])
    assert not S.safe_external(protected, checkout, [protected])
    assert not S.safe_external(tmp_path / "missing", checkout, [])


def test_junction_root_is_refused_not_followed(tmp_path, monkeypatch):
    target = tmp_path / "ws/real"
    target.mkdir(parents=True)
    (target / "note.md").write_text("junction target\n", encoding="utf-8")
    link = tmp_path / "ws/link"
    if not make_junction(link, target):
        pytest.skip("host cannot create NTFS junctions")
    assert S.is_reparse_point(link) and not link.is_symlink()
    checkout = _checkout(tmp_path)
    _write_scope(checkout, minimal(roots=[{"label": "link", "path": "link", "tier": 1}]))
    monkeypatch.delenv(S.BASE_ENV, raising=False)
    rows = S.resolve_roots(S.load_scope(checkout), checkout)
    assert rows[0]["skipped"] == "reparse_point"


def test_symlink_root_is_refused_not_followed(tmp_path, monkeypatch):
    target = tmp_path / "ws/real"
    target.mkdir(parents=True)
    link = tmp_path / "ws/link"
    if not make_symlink(link, target):
        pytest.skip("host cannot create symlinks")
    assert S.is_reparse_point(link)
    checkout = _checkout(tmp_path)
    _write_scope(checkout, minimal(roots=[{"label": "link", "path": "link", "tier": 1}]))
    monkeypatch.delenv(S.BASE_ENV, raising=False)
    rows = S.resolve_roots(S.load_scope(checkout), checkout)
    assert rows[0]["skipped"] == "reparse_point"


def test_locators_carry_the_ext_prefix_and_round_trip():
    text = S.locator("all-theory", "records/transcripts/# HODGE v10a.26 \ufffd Comp.txt")
    assert text.startswith("ext:all-theory/")
    assert S.split_locator(text) == (
        "all-theory",
        "records/transcripts/# HODGE v10a.26 \ufffd Comp.txt",
    )
    assert S.split_locator("theory/MASTER.md") is None


def test_cli_scope_report_does_not_build_unless_asked(tmp_path, monkeypatch, capsys):
    checkout = _checkout(tmp_path)
    (tmp_path / "ws/notes").mkdir()
    _write_scope(checkout, minimal())
    monkeypatch.delenv(S.BASE_ENV, raising=False)
    monkeypatch.setattr(S, "checkout_root", lambda: checkout)

    def forbidden():
        pytest.fail("scope without --build must not construct an engine")

    args = SimpleNamespace(build=False, json=True, out=None)
    assert S.run(args, forbidden) == 0
    report = json.loads(capsys.readouterr().out)
    assert report["schema"] == S.REPORT_SCHEMA
    assert report["roots"][0]["label"] == "notes" and report["roots"][0]["present"]
    assert report["scope"]["base_source"] == "workspace_marker"

    class Engine:
        class index:  # noqa: N801 - mimics DiscoveryEngine.index
            @staticmethod
            def metadata(recheck=True):
                return {
                    "fingerprint": "abc",
                    "alias_count": 2,
                    "freshness_policy": {"internal": "x", "external": "y"},
                    "external_roots": [
                        {
                            "label": "notes",
                            "files": 3,
                            "sources": 2,
                            "aliases": 1,
                            "bytes": 10,
                            "passages": 4,
                        }
                    ],
                }

        def __enter__(self):
            return self

        def __exit__(self, *_):
            return False

    out = tmp_path / "report.json"
    args = SimpleNamespace(build=True, json=False, out=str(out))
    assert S.run(args, Engine) == 0
    text = capsys.readouterr().out
    assert "2 src 1 alias 4 passages" in text and "absent root is skipped" in text
    saved = json.loads(out.read_text(encoding="utf-8"))
    assert saved["fingerprint"] == "abc" and saved["roots"][0]["passages"] == 4
    with pytest.raises(FileExistsError):
        S.run(args, Engine)


def test_cli_scope_report_surfaces_a_malformed_file_as_an_error(tmp_path, monkeypatch, capsys):
    checkout = _checkout(tmp_path)
    (checkout / S.SCOPE_PATH).write_text("schema: wrong\n", encoding="utf-8")
    monkeypatch.setattr(S, "checkout_root", lambda: checkout)
    args = SimpleNamespace(build=True, json=True, out=None)
    assert S.run(args, lambda: pytest.fail("no engine for a broken scope")) == 1
    assert "schema" in json.loads(capsys.readouterr().out)["error"]
