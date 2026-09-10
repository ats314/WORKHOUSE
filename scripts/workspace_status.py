#!/usr/bin/env python3
"""Read current checkout identities without fetching, modifying Git, or reading source content.

Print JSON by default. --remote reads the live origin/main tip with ls-remote.
--out writes an exclusive new snapshot beneath navigation/checkpoints only.
"""

from __future__ import annotations

import argparse
import json
import os
import stat
import subprocess
import sys
from concurrent.futures import ThreadPoolExecutor
from datetime import UTC, datetime
from pathlib import Path, PureWindowsPath

ROOT = Path(__file__).absolute().parents[2]
ENV = {**os.environ, "GIT_OPTIONAL_LOCKS": "0", "GIT_TERMINAL_PROMPT": "0"}


def git(path: Path, *args: str) -> dict:
    try:
        result = subprocess.run(
            ["git", "-c", "core.quotepath=false", "-C", str(path), *args],
            env=ENV,
            capture_output=True,
            timeout=30,
            check=False,
        )
        return {
            "ok": result.returncode == 0,
            "stdout": result.stdout.decode("utf-8", errors="replace"),
            "error": result.stderr.decode("utf-8", errors="replace").strip()[:1200],
            "exit_code": result.returncode,
        }
    except (OSError, subprocess.TimeoutExpired) as exc:
        return {"ok": False, "stdout": "", "error": str(exc), "exit_code": None}


def value(result: dict) -> str | None:
    return result["stdout"].strip() if result["ok"] else None


def same_path(left: str | Path, right: str | Path) -> bool:
    return os.path.normcase(os.path.abspath(left)) == os.path.normcase(os.path.abspath(right))


def inside(path: Path, parent: Path) -> bool:
    return path == parent or parent in path.parents


def parse_worktrees(raw: str) -> list[dict]:
    entries, current = [], {}
    for field in raw.split("\0"):
        if not field:
            if current:
                entries.append(current)
                current = {}
            continue
        key, _, val = field.partition(" ")
        if key == "worktree":
            if current:
                entries.append(current)
            current = {"path": val}
        elif key == "HEAD":
            current["registered_head"] = val
        elif key == "branch":
            current["registered_branch"] = val
        elif key in {"detached", "bare", "locked", "prunable"}:
            current[key] = val or True
    if current:
        entries.append(current)
    return entries


def status_counts(raw: str) -> dict:
    tracked = untracked = conflicts = staged = 0
    if raw and not raw.endswith("\0"):
        raise ValueError("Truncated porcelain status output")
    entries = iter(raw.split("\0"))
    for entry in entries:
        if not entry:
            continue
        if len(entry) < 4 or entry[2] != " ":
            raise ValueError("Unexpected porcelain status record")
        code = entry[:2]
        if any(character not in " MADRCUT?!" for character in code):
            raise ValueError("Unexpected porcelain status code")
        if code == "??":
            untracked += 1
        elif code != "!!":
            tracked += 1
            unmerged = code in {"DD", "AU", "UD", "UA", "DU", "AA", "UU"}
            conflicts += unmerged
            staged += code[0] in "MADRCT" and not unmerged
        if ("R" in code or "C" in code) and not next(entries, None):
            raise ValueError("Truncated rename/copy status record")
    return {
        "tracked_changed_paths": tracked,
        "untracked_files": untracked,
        "unmerged_paths": conflicts,
        "staged_paths": staged,
        "dirty": bool(tracked or untracked),
    }


def inspect(entry: dict, canonical: Path) -> dict:
    path = Path(entry["path"])
    output = {**entry, "is_canonical": same_path(path, canonical), "errors": [], "warnings": []}
    before = git(path, "rev-parse", "--verify", "HEAD")
    status = git(path, "status", "--porcelain=v1", "-z", "--untracked-files=all")
    after = git(path, "rev-parse", "--verify", "HEAD")
    common = git(path, "rev-parse", "--path-format=absolute", "--git-common-dir")
    branch = git(path, "symbolic-ref", "--quiet", "HEAD")
    output.update(
        head_before=value(before),
        head_after=value(after),
        branch=value(branch),
        common_git_dir=value(common),
        status=None,
        concurrent_head_change=(value(before) != value(after))
        if before["ok"] and after["ok"]
        else None,
    )
    for label, result in (
        ("head_before", before),
        ("status", status),
        ("head_after", after),
        ("common_git_dir", common),
        ("branch", branch),
    ):
        if not result["ok"]:
            # symbolic-ref exit 1 with no stderr is normal for a detached HEAD.
            if label != "branch" or result["exit_code"] != 1 or result["error"]:
                output["errors"].append(
                    {"operation": label, "error": result["error"], "exit_code": result["exit_code"]}
                )
        elif result["error"]:
            output["warnings"].append({"operation": label, "warning": result["error"]})
    if status["ok"]:
        try:
            output["status"] = status_counts(status["stdout"])
        except ValueError as exc:
            output["errors"].append({"operation": "status_parse", "error": str(exc)})
    if before["ok"] and entry.get("registered_head"):
        output["head_changed_since_worktree_list"] = value(before) != entry["registered_head"]
    output["inspection_consistent"] = output["concurrent_head_change"] is False and not output.get(
        "head_changed_since_worktree_list", False
    )
    output["status_complete"] = (
        output["status"] is not None and not status["error"] and output["inspection_consistent"]
    )
    if output["status"] is not None:
        output["status"]["complete"] = output["status_complete"]
        # Positive observations remain useful; incomplete absence cannot establish clean.
        if not output["status_complete"] and not output["status"]["dirty"]:
            output["status"]["dirty"] = None
    output["inspection_complete"] = (
        output["status_complete"] and not output["errors"] and not output["warnings"]
    )
    return output


def collect(remote: bool) -> dict:
    config_path = ROOT / "WORKSPACE.json"
    has_config = config_path.is_file()
    config = (
        json.loads(config_path.read_text(encoding="utf-8-sig"))
        if has_config
        else {"canonical_repository": "."}
    )
    canonical = Path(os.path.abspath(ROOT / config["canonical_repository"]))
    listed = git(canonical, "worktree", "list", "--porcelain", "-z")
    entries = parse_worktrees(listed["stdout"]) if listed["ok"] else []
    if not any(same_path(entry["path"], canonical) for entry in entries):
        entries.append({"path": str(canonical), "registration": "not observed in worktree list"})
    with ThreadPoolExecutor(max_workers=4) as pool:
        observed = list(pool.map(lambda entry: inspect(entry, canonical), entries))
    canonical_state = next(item for item in observed if item["is_canonical"])
    common_dir = canonical_state["common_git_dir"]
    legacy_path = ROOT / config.get("legacy_primary_checkout", "ALL THEORY/WORKHOUSE")
    report = {
        "schema": "workhouse-workspace-status/v1",
        "mode": "configured_workspace" if has_config else "standalone_repository",
        "observed_at_utc": datetime.now(UTC).isoformat(),
        "workspace_root": str(ROOT),
        "canonical_repository": str(canonical),
        "scope": (
            "Git identities and working-tree status only; no source-content or mathematical review."
        ),
        "provenance": (
            "Live local commands; no fetch, checkout, reset, or source writes. "
            "Git optional locks disabled."
        ),
        "consistency": (
            "Per-worktree HEAD checked before and after status; "
            "this is not an atomic workspace snapshot. "
            "File edits without HEAD changes may occur during inspection."
        ),
        "common_git_dir": common_dir,
        "common_git_dir_under_legacy_checkout": inside(Path(common_dir), legacy_path)
        if has_config and common_dir
        else None,
        "worktree_list_error": None if listed["ok"] else listed["error"],
        "worktree_list_warnings": listed["error"] if listed["ok"] else None,
        "registered_worktrees_observed": len(parse_worktrees(listed["stdout"]))
        if listed["ok"]
        else None,
        "worktrees": observed,
        "local_origin_main": {
            "head": value(git(canonical, "rev-parse", "--verify", "refs/remotes/origin/main")),
            "provenance": "Local remote-tracking ref only; may be stale.",
        },
        "live_origin_main": {
            "requested": remote,
            "head": None,
            "provenance": "Not queried; pass --remote for read-only ls-remote.",
        },
    }
    historical = ROOT / "WORK_SINCE_LAST_SESSION"
    if (
        has_config
        and historical.exists()
        and not any(same_path(item["path"], historical) for item in observed)
    ):
        report["separate_historical_repository"] = inspect(
            {"path": str(historical), "role": "Separate preserved paper repository"}, canonical
        )
    if remote:
        live = git(canonical, "ls-remote", "--exit-code", "origin", "refs/heads/main")
        fields = live["stdout"].strip().split()
        valid = live["ok"] and len(fields) == 2 and fields[1] == "refs/heads/main"
        tip = fields[0] if valid else None
        detail = {
            "requested": True,
            "head": tip,
            "provenance": "Live git ls-remote origin refs/heads/main; no fetch; 30-second timeout.",
            "error": None if valid else live["error"] or "Unexpected or missing remote ref",
        }
        if tip:
            present = git(canonical, "cat-file", "-e", tip + "^{commit}")
            detail["tip_available_in_local_objects"] = present["ok"]
            if present["ok"] and canonical_state["head_after"]:
                comparison = git(
                    canonical,
                    "rev-list",
                    "--left-right",
                    "--count",
                    canonical_state["head_after"] + "..." + tip,
                )
                if comparison["ok"]:
                    ahead, behind = map(int, comparison["stdout"].split())
                    detail["canonical_ahead"] = ahead
                    detail["canonical_behind"] = behind
                else:
                    detail["comparison_error"] = comparison["error"]
        report["live_origin_main"] = detail
    report["local_inspection_complete"] = (
        not report["worktree_list_error"]
        and not report["worktree_list_warnings"]
        and all(
            item["inspection_complete"]
            for item in [
                *observed,
                *(
                    [report["separate_historical_repository"]]
                    if "separate_historical_repository" in report
                    else []
                ),
            ]
        )
    )
    report["inspection_complete"] = report["local_inspection_complete"] and (
        not remote or report["live_origin_main"]["head"] is not None
    )
    return report


def snapshot_path(raw: str) -> Path:
    if not (ROOT / "WORKSPACE.json").is_file():
        raise ValueError(
            "Standalone repository mode prints to stdout; --out requires a configured workspace"
        )
    windows_path = PureWindowsPath(raw)
    if windows_path.drive and not windows_path.root:
        raise ValueError("Snapshot path must not use drive-relative Windows syntax")
    components = windows_path.parts[1:] if windows_path.anchor else windows_path.parts
    if any(":" in component for component in components):
        raise ValueError("Snapshot path must not use Windows alternate data stream syntax")
    candidate = Path(raw)
    if ".." in candidate.parts:
        raise ValueError("Snapshot path must not contain '..'")
    candidate = Path(os.path.abspath(candidate if candidate.is_absolute() else ROOT / candidate))
    allowed = ROOT / "navigation" / "checkpoints"
    if candidate == allowed or not inside(candidate, allowed):
        raise ValueError("--out must name a new file beneath navigation/checkpoints")
    for part in [*reversed(candidate.parents), candidate]:
        try:
            info = part.lstat()
        except FileNotFoundError:
            continue
        if stat.S_ISLNK(info.st_mode) or getattr(info, "st_file_attributes", 0) & 0x400:
            raise ValueError(
                f"Snapshot path traverses a symlink, junction, or reparse point: {part}"
            )
    if os.path.lexists(candidate):
        raise ValueError(f"Refusing to overwrite existing path: {candidate}")
    return candidate


def locate_root(explicit: str | None) -> Path:
    if explicit:
        chosen = Path(os.path.abspath(explicit))
        if not chosen.is_dir():
            raise ValueError(f"Workspace/repository directory does not exist: {chosen}")
        return chosen
    script_dir = Path(__file__).absolute().parent
    for start in (script_dir, Path.cwd()):
        for candidate in (start, *start.parents):
            if (candidate / "WORKSPACE.json").is_file():
                return candidate
    for start in (script_dir, Path.cwd()):
        top = value(git(start, "rev-parse", "--show-toplevel"))
        if top:
            return Path(top)
    raise ValueError("No WORKSPACE.json or Git repository found; pass --workspace-root DIRECTORY")


def main() -> int:
    global ROOT
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--workspace-root", help="Workspace with WORKSPACE.json, or a standalone Git checkout"
    )
    parser.add_argument(
        "--remote", action="store_true", help="Read live origin/main without fetching"
    )
    parser.add_argument("--out", help="Exclusive new JSON file beneath navigation/checkpoints")
    args = parser.parse_args()
    try:
        ROOT = locate_root(args.workspace_root)
        destination = snapshot_path(args.out) if args.out else None
        report = collect(args.remote)
        rendered = json.dumps(report, indent=2, ensure_ascii=True) + "\n"
        if destination:
            # Recheck after Git commands; exclusive creation never overwrites a snapshot.
            destination = snapshot_path(str(destination))
            destination.parent.mkdir(parents=True, exist_ok=True)
            snapshot_path(str(destination))
            with destination.open("x", encoding="utf-8", newline="\n") as stream:
                stream.write(rendered)
        print(rendered, end="")
        return 0 if report["inspection_complete"] else 1
    except (OSError, ValueError, KeyError) as exc:
        print(f"workspace_status: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
