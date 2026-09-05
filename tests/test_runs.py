"""In-repo run artifacts are evidence: pinned by digest, never edited.

Runs produced here preserve both generating code and output. Received runs
also preserve their original package manifests and any nested prior inputs.
Both kinds are pinned: a transcript that can drift silently stops being a
transcript.
"""

import hashlib
from pathlib import Path, PurePosixPath

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
        # Received runs may preserve nested prior/ inputs. Every file must be
        # pinned, including those below a directory; directories have no hash.
        on_disk = {p.relative_to(run_dir).as_posix() for p in run_dir.rglob("*") if p.is_file()} - {
            "SHA256SUMS"
        }
        assert set(recorded) == on_disk, (
            f"{run_dir.name}: pinned {sorted(recorded)} != on disk {sorted(on_disk)}"
        )
        for name, digest in recorded.items():
            relative = PurePosixPath(name)
            assert not relative.is_absolute() and ".." not in relative.parts, (
                f"{run_dir.name}: unsafe manifest path {name!r}"
            )
            actual = hashlib.sha256((run_dir / name).read_bytes()).hexdigest()
            assert actual == digest, f"{run_dir.name}/{name} changed: {actual}"
