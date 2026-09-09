"""Cold exact replay and corruption controls for the flat-background proof inputs."""

import hashlib
import json
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RUN = ROOT / "runs" / "flat_holonomy_sources_2026-09-07"
PROOF = ROOT / "paper" / "research_notes" / "G19_FLAT_HOLONOMY_SOURCES_AND_RANK_REPAIR_20260907.md"


def replay(directory, *flags):
    return subprocess.run(
        [
            sys.executable,
            *flags,
            "-B",
            str(directory / "check_flat_holonomy.py"),
            "--replay",
            str(directory / "CONTROLS.json"),
        ],
        cwd=directory,
        capture_output=True,
        text=True,
        encoding="utf-8",
        timeout=90,
        check=False,
    )


def test_exact_controls_replay_after_cold_relocation(tmp_path):
    cold = tmp_path / "cold"
    shutil.copytree(RUN, cold)
    result = replay(cold)
    assert result.returncode == 0, result.stdout + result.stderr
    assert "32 complete exact Fourier blocks" in result.stdout


def test_repinned_false_mathematical_report_is_rejected(tmp_path):
    cold = tmp_path / "changed"
    shutil.copytree(RUN, cold)
    report_path = cold / "CONTROLS.json"
    report = json.loads(report_path.read_text(encoding="utf-8"))
    report["projection_jump"]["noncentral_rank"] = 51
    report_path.write_text(json.dumps(report), encoding="utf-8")
    lines = []
    for line in (cold / "SHA256SUMS").read_text(encoding="utf-8").splitlines():
        digest, name = line.split(maxsplit=1)
        if name == "CONTROLS.json":
            digest = hashlib.sha256(report_path.read_bytes()).hexdigest()
        lines.append(f"{digest}  {name}")
    (cold / "SHA256SUMS").write_text("\n".join(lines) + "\n", encoding="utf-8")
    result = replay(cold)
    assert result.returncode != 0
    assert "replayed mathematical report differs" in result.stderr


def test_optimized_execution_cannot_skip_proof_controls():
    result = replay(RUN, "-O")
    assert result.returncode != 0
    assert "optimized Python is not accepted" in result.stderr


def test_registered_proof_matches_frozen_proof():
    assert PROOF.read_bytes() == (RUN / "PROOF.md").read_bytes()
