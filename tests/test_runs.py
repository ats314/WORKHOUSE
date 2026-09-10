"""In-repo run artifacts are evidence: pinned by digest, never edited.

Runs produced here preserve both generating code and output. Received runs
also preserve their original package manifests and any nested prior inputs.
Both kinds are pinned: a transcript that can drift silently stops being a
transcript.
"""

import hashlib
from pathlib import Path, PurePosixPath

import pytest

RUNS = Path(__file__).resolve().parents[1] / "runs"


def test_runs_directory_exists():
    assert RUNS.is_dir()
    assert any(p.is_dir() for p in RUNS.iterdir())


def _check_run_pins(run_dir):
    """A run can contain source subdirectories; every file still needs a pin."""
    manifest = run_dir / "SHA256SUMS"
    assert manifest.exists(), f"{run_dir.name}/SHA256SUMS is missing"
    recorded = {}
    for line in manifest.read_text(encoding="utf-8-sig").splitlines():
        if line.strip() and not line.startswith("#"):
            digest, name = line.split(maxsplit=1)
            name = name.strip()
            relative = PurePosixPath(name)
            assert (
                not relative.is_absolute()
                and ".." not in relative.parts
                and "\\" not in name
                and ":" not in name
            ), f"{run_dir.name}: unsafe manifest path {name!r}"
            assert name not in recorded, f"{run_dir.name}: duplicate pin {name}"
            recorded[name] = digest
    on_disk = {p.relative_to(run_dir).as_posix() for p in run_dir.rglob("*") if p.is_file()} - {
        "SHA256SUMS"
    }
    assert set(recorded) == on_disk, (
        f"{run_dir.name}: pinned {sorted(recorded)} != on disk {sorted(on_disk)}"
    )
    for name, digest in recorded.items():
        actual = hashlib.sha256((run_dir / name).read_bytes()).hexdigest()
        assert actual == digest, f"{run_dir.name}/{name} changed: {actual}"


def test_every_run_dir_is_fully_pinned():
    for run_dir in sorted(p for p in RUNS.iterdir() if p.is_dir()):
        _check_run_pins(run_dir)


def test_nested_run_pins_detect_changed_and_unregistered_files(tmp_path):
    source = tmp_path / "sources" / "proof.md"
    source.parent.mkdir()
    source.write_bytes(b"original proof")
    digest = hashlib.sha256(source.read_bytes()).hexdigest()
    (tmp_path / "SHA256SUMS").write_text(f"{digest}  sources/proof.md\n", encoding="utf-8")
    _check_run_pins(tmp_path)
    source.write_bytes(b"changed proof")
    with pytest.raises(AssertionError, match="changed"):
        _check_run_pins(tmp_path)
    source.write_bytes(b"original proof")
    (source.parent / "unregistered.md").write_bytes(b"not pinned")
    with pytest.raises(AssertionError, match="pinned"):
        _check_run_pins(tmp_path)


@pytest.mark.parametrize("name", ["../proof.md", "/proof.md", "C:/proof.md", "sources\\proof.md"])
def test_run_pins_reject_unsafe_paths(tmp_path, name):
    (tmp_path / "SHA256SUMS").write_text(f"{'0' * 64}  {name}\n", encoding="utf-8")
    with pytest.raises(AssertionError, match="unsafe manifest path"):
        _check_run_pins(tmp_path)


def test_run_pins_reject_duplicate_entries(tmp_path):
    line = f"{'0' * 64}  proof.md\n"
    (tmp_path / "SHA256SUMS").write_text(line + line, encoding="utf-8")
    with pytest.raises(AssertionError, match="duplicate pin"):
        _check_run_pins(tmp_path)
