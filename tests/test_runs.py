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
