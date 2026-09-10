"""Workspace inspection must preserve uncertainty and never overwrite evidence."""

from __future__ import annotations

import importlib.util
import json
import stat
import tempfile
import unittest
from pathlib import Path
from types import SimpleNamespace
from unittest.mock import patch

SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "workspace_status.py"
SPEC = importlib.util.spec_from_file_location("workspace_status_under_test", SCRIPT)
assert SPEC is not None and SPEC.loader is not None
workspace_status = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(workspace_status)


def git_result(stdout: str = "", error: str = "", exit_code: int = 0) -> dict:
    return {"stdout": stdout, "error": error, "exit_code": exit_code, "ok": exit_code == 0}


class InspectionTests(unittest.TestCase):
    def inspect(self, status: dict, head_after: str = "abc") -> dict:
        responses = [
            git_result("abc\n"),
            status,
            git_result(head_after + "\n"),
            git_result("/preserved/repository/.git\n"),
            git_result("refs/heads/main\n"),
        ]
        with patch.object(workspace_status, "git", side_effect=responses):
            return workspace_status.inspect(
                {"path": "/workspace/repository", "registered_head": "abc"},
                Path("/workspace/repository"),
            )

    def test_permission_warning_with_no_paths_does_not_establish_clean(self):
        warning = "warning: could not open directory 'private/': Permission denied"
        result = self.inspect(git_result(error=warning))
        self.assertFalse(result["inspection_complete"])
        self.assertFalse(result["status_complete"])
        self.assertIsNone(result["status"]["dirty"])
        self.assertEqual(result["warnings"], [{"operation": "status", "warning": warning}])

    def test_permission_warning_preserves_positive_partial_observations(self):
        result = self.inspect(git_result("M  staged\0?? new\0", "warning: unreadable directory"))
        self.assertTrue(result["status"]["dirty"])
        self.assertEqual(result["status"]["staged_paths"], 1)
        self.assertEqual(result["status"]["untracked_files"], 1)
        self.assertFalse(result["status"]["complete"])

    def test_failed_status_keeps_error_and_unknown_status(self):
        result = self.inspect(
            git_result(error="fatal: cannot access working directory", exit_code=128)
        )
        self.assertIsNone(result["status"])
        self.assertFalse(result["status_complete"])
        self.assertFalse(result["inspection_complete"])
        self.assertEqual(result["errors"][0]["exit_code"], 128)

    def test_head_change_makes_inspection_inconsistent(self):
        result = self.inspect(git_result(), head_after="def")
        self.assertTrue(result["concurrent_head_change"])
        self.assertFalse(result["inspection_consistent"])
        self.assertFalse(result["inspection_complete"])
        self.assertIsNone(result["status"]["dirty"])

    def test_clean_requires_complete_consistent_inspection(self):
        result = self.inspect(git_result())
        self.assertTrue(result["inspection_complete"])
        self.assertTrue(result["status_complete"])
        self.assertIs(result["status"]["dirty"], False)


class PorcelainTests(unittest.TestCase):
    def test_rename_source_is_not_counted_as_an_additional_path(self):
        counts = workspace_status.status_counts(
            "R  new name\0old name\0 M unstaged\0?? untracked\0UU conflict\0A  added\0"
        )
        self.assertEqual(counts["tracked_changed_paths"], 4)
        self.assertEqual(counts["staged_paths"], 2)
        self.assertEqual(counts["untracked_files"], 1)
        self.assertEqual(counts["unmerged_paths"], 1)

    def test_malformed_rename_cannot_be_accepted_as_complete(self):
        for raw in ("R  new name\0", "R  new name\0\0", "R  new name\0old name"):
            with self.subTest(raw=raw), self.assertRaises(ValueError):
                workspace_status.status_counts(raw)

    def test_worktree_names_with_spaces_and_newlines_are_preserved(self):
        worktrees = workspace_status.parse_worktrees(
            "worktree /workspace/name with\nnewline\0HEAD abc\0branch refs/heads/main\0\0"
            "worktree /workspace/second\0HEAD def\0detached\0\0"
        )
        self.assertEqual(worktrees[0]["path"], "/workspace/name with\nnewline")
        self.assertTrue(worktrees[1]["detached"])


class SnapshotBoundaryTests(unittest.TestCase):
    def setUp(self):
        temporary = tempfile.TemporaryDirectory()
        self.addCleanup(temporary.cleanup)
        self.root = Path(temporary.name)
        (self.root / "WORKSPACE.json").write_text(json.dumps({"canonical_repository": "REPO"}))
        root_patch = patch.object(workspace_status, "ROOT", self.root)
        root_patch.start()
        self.addCleanup(root_patch.stop)

    def test_outside_and_traversal_paths_are_rejected(self):
        candidates = (
            "REPO/report.json",
            "navigation/checkpoints/../escape.json",
            str(self.root.parent / "outside.json"),
        )
        for candidate in candidates:
            with self.subTest(candidate=candidate), self.assertRaises(ValueError):
                workspace_status.snapshot_path(candidate)

    def test_existing_evidence_is_never_overwritten(self):
        existing = self.root / "navigation" / "checkpoints" / "status.json"
        existing.parent.mkdir(parents=True)
        existing.write_bytes(b"preserved evidence")
        with self.assertRaisesRegex(ValueError, "overwrite"):
            workspace_status.snapshot_path(str(existing))
        self.assertEqual(existing.read_bytes(), b"preserved evidence")

    def test_windows_alternate_stream_targets_are_rejected_without_opening_them(self):
        existing = self.root / "navigation" / "checkpoints" / "status.json"
        existing.parent.mkdir(parents=True)
        existing.write_bytes(b"preserved evidence")
        candidates = (
            str(existing) + ":probe",
            "navigation/checkpoints/new.json:probe",
            "navigation/checkpoints/status.json::$DATA",
        )
        for candidate in candidates:
            with (
                self.subTest(candidate=candidate),
                self.assertRaisesRegex(ValueError, "alternate data stream"),
            ):
                workspace_status.snapshot_path(candidate)
        self.assertEqual(existing.read_bytes(), b"preserved evidence")

    def test_windows_drive_relative_output_paths_are_rejected(self):
        for candidate in ("C:", "C:navigation/checkpoints/status.json"):
            with (
                self.subTest(candidate=candidate),
                self.assertRaisesRegex(ValueError, "drive-relative"),
            ):
                workspace_status.snapshot_path(candidate)
        ordinary = self.root / "navigation" / "checkpoints" / "new-status.json"
        self.assertEqual(workspace_status.snapshot_path(str(ordinary)), ordinary)

    def test_reparse_point_in_output_ancestry_is_rejected(self):
        blocked = self.root / "navigation"
        original_lstat = Path.lstat

        def lstat(path: Path):
            if path == blocked:
                return SimpleNamespace(st_mode=stat.S_IFDIR, st_file_attributes=0x400)
            return original_lstat(path)

        with patch.object(Path, "lstat", lstat), self.assertRaisesRegex(ValueError, "reparse"):
            workspace_status.snapshot_path("navigation/checkpoints/status.json")

    def test_standalone_checkout_is_discovered_without_workspace_configuration(self):
        standalone = self.root / "fresh-clone"
        standalone.mkdir()
        # Hide the workspace fixture while discovering a genuinely separate clone.
        original_is_file = Path.is_file

        def is_file(path: Path):
            return False if path.name == "WORKSPACE.json" else original_is_file(path)

        with (
            patch.object(workspace_status, "__file__", str(standalone / "scripts" / "status.py")),
            patch.object(Path, "cwd", return_value=standalone),
            patch.object(Path, "is_file", is_file),
            patch.object(workspace_status, "git", return_value=git_result(str(standalone))),
        ):
            self.assertEqual(workspace_status.locate_root(None), standalone)
            with self.assertRaisesRegex(ValueError, "Standalone repository"):
                workspace_status.snapshot_path("navigation/checkpoints/status.json")


if __name__ == "__main__":
    unittest.main()
