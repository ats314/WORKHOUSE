"""In-repo run artifacts are evidence: pinned by digest, never edited.

Unlike ``settlement/`` (received) these were produced in this repository by
pinned code, so the generating script and the artifact are BOTH present —
but the artifacts still pin, because a transcript that can drift silently
stops being a transcript.
"""

import hashlib
from pathlib import Path

RUNS = Path(__file__).resolve().parents[1] / "runs"


def test_runs_directory_exists():
    assert RUNS.is_dir()
    assert any(p.is_dir() for p in RUNS.iterdir())


def test_every_run_dir_is_fully_pinned():
    for run_dir in sorted(p for p in RUNS.iterdir() if p.is_dir()):
        manifest = run_dir / "SHA256SUMS"
        assert manifest.exists(), f"{run_dir.name}/SHA256SUMS is missing"
        recorded = {}
        for line in manifest.read_text().splitlines():
            if line.strip() and not line.startswith("#"):
                digest, name = line.split(maxsplit=1)
                recorded[name.strip()] = digest
        on_disk = {p.name for p in run_dir.iterdir()} - {"SHA256SUMS"}
        assert set(recorded) == on_disk, (
            f"{run_dir.name}: pinned {sorted(recorded)} != on disk {sorted(on_disk)}"
        )
        for name, digest in recorded.items():
            actual = hashlib.sha256((run_dir / name).read_bytes()).hexdigest()
            assert actual == digest, f"{run_dir.name}/{name} changed: {actual}"


def test_every_pinned_run_file_is_tracked_by_git():
    """A file pinned by SHA256SUMS but absent from git fails only in CI.

    This is a real defect that has happened here: ``.gitignore`` excludes
    ``*.log``, run transcripts ARE ``.log`` files, and ``git add`` drops them
    silently. The manifest still pins them, so the suite above passes locally
    against the working tree and fails in a fresh clone where the files do not
    exist. ``git add -f`` is the fix; this test is the alarm.
    """
    import subprocess

    for run_dir in sorted(p for p in RUNS.iterdir() if p.is_dir()):
        manifest = run_dir / "SHA256SUMS"
        names = [
            line.split(maxsplit=1)[1].strip()
            for line in manifest.read_text().splitlines()
            if line.strip() and not line.startswith("#")
        ]
        for name in names:
            rel = (run_dir / name).relative_to(RUNS.parent)
            proc = subprocess.run(
                ["git", "ls-files", "--error-unmatch", str(rel)],
                cwd=RUNS.parent,
                capture_output=True,
            )
            assert proc.returncode == 0, (
                f"{rel} is pinned by {run_dir.name}/SHA256SUMS but is NOT tracked by git "
                "— it will be missing in CI. Add it with `git add -f`."
            )
