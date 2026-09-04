"""The certified index must stay current, and its reproduction commands must work."""

import shlex
import subprocess
import sys
from pathlib import Path

from workhouse import certified as C

ROOT = Path(__file__).resolve().parents[1]


def test_certified_md_is_current():
    assert C.render() == (ROOT / "CERTIFIED.md").read_text(encoding="utf-8"), (
        "CERTIFIED.md is stale; run `make certified`"
    )


def test_every_claim_is_ranked_by_tier_alone():
    """Not by importance, not by which document states it."""
    tiers = [c.tier for c in C.collect()]
    assert tiers == sorted(tiers)
    assert set(tiers) <= {0, 1, 2}


def test_every_claim_carries_a_reproduction_command():
    for claim in C.collect():
        assert claim.reproduce.strip(), claim.name
        assert claim.where.strip(), claim.name


def test_the_reproduction_commands_actually_reproduce():
    """The promise of this page is the third column. Test the promise.

    Every T1/T2 row claims a `workhouse verify --only ...` invocation
    re-establishes it. Run a sample of them for real, including one whose name
    contains the quoting hazards -- carets, plus signs, quotes.
    """
    checks = [c for c in C.collect() if c.tier in (1, 2)]
    assert len(checks) > 50
    sample = [
        checks[0],
        checks[len(checks) // 2],
        checks[-1],
        next(c for c in checks if "h_4^side = A_+" in c.name),
        next(c for c in checks if "sigma_n^phys" in c.name),
    ]
    for claim in sample:
        argv = shlex.split(claim.reproduce)
        assert argv[0] == "workhouse"
        proc = subprocess.run(
            [sys.executable, "-m", "workhouse.cli", *argv[1:]],
            capture_output=True,
            text=True,
            cwd=ROOT,
        )
        assert proc.returncode == 0, f"{claim.name}: {proc.stdout}{proc.stderr}"
        assert "checks passed" in proc.stdout, claim.name
        # A filtered run must print the numbers, not just a verdict.
        assert "PASS" in proc.stdout, claim.name


def test_an_unmatched_filter_fails_loudly():
    """Silently passing zero checks would read as a green certification."""
    proc = subprocess.run(
        [sys.executable, "-m", "workhouse.cli", "verify", "--only", "no such check"],
        capture_output=True,
        text=True,
        cwd=ROOT,
    )
    assert proc.returncode == 1
    assert "no check matches" in proc.stdout


def test_t0_claims_point_at_real_lean_lines():
    for claim in C.collect():
        if claim.tier != 0:
            continue
        path, _, line = claim.where.rpartition(":")
        body = (ROOT / path).read_text(encoding="utf-8").splitlines()
        assert claim.name in body[int(line) - 1], claim.where


def test_the_page_says_what_it_does_not_cover():
    """An index of certified work reads as a summary of the corpus unless it
    says otherwise, and that misreading is the expensive one."""
    text = C.render()
    assert "What is not here" in text
    assert "not mean it is wrong" in " ".join(text.split())
