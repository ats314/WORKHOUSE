"""The settlement package is received evidence, pinned like the corpus."""

import hashlib

from workhouse import settlement as S

#: Repository guidance, deliberately outside the pin -- the manifest is what
#: marks a file as received evidence (ADR 0006).
REPO_AUTHORED = {"SHA256SUMS", "CLAUDE.md"}

EXPECTED = {
    "SETTLEMENT.md",
    "README.md",
    "cold_rerun_pentagonal_frontier.txt",
    "cold_rerun_stranded_flux_audit.txt",
    "mce_adjudication_harness.py",
}


def test_all_artifacts_present():
    names = {p.name for p in S.SETTLEMENT_DIR.iterdir() if p.name not in REPO_AUTHORED}
    assert names == EXPECTED


def test_manifest_matches_contents():
    manifest = S.SETTLEMENT_DIR / "SHA256SUMS"
    assert manifest.exists(), "settlement/SHA256SUMS is missing"
    recorded = {}
    for line in manifest.read_text().splitlines():
        if line.strip() and not line.startswith("#"):
            digest, name = line.split(maxsplit=1)
            recorded[name.strip()] = digest
    assert set(recorded) == EXPECTED
    for name, digest in recorded.items():
        actual = hashlib.sha256((S.SETTLEMENT_DIR / name).read_bytes()).hexdigest()
        assert actual == digest, f"{name} changed: {actual} != {digest}"


def test_transcript_source_sha_is_not_the_artifact_sha():
    """SOURCE_SHA256 hashes the generating script, which is absent here.

    Conflating it with the artifact hash would invent provenance the repository
    does not have.
    """
    for run in S.read_cold_runs():
        artifact = S.SETTLEMENT_DIR / f"{run.name}.txt"
        artifact_sha = hashlib.sha256(artifact.read_bytes()).hexdigest()
        assert run.source_sha256
        assert run.source_sha256 != artifact_sha


def test_both_cold_runs_are_eight_of_eight():
    runs = S.read_cold_runs()
    assert len(runs) == 2
    assert all(r.passed == r.total == 8 for r in runs)


def test_stranded_flux_verdict_is_recorded():
    run = next(r for r in S.read_cold_runs() if "stranded_flux" in r.name)
    assert run.verdict == "ZERO_BACKEND_FALSIFIED"


def test_scan_gap_is_recorded_not_silenced():
    """The finding must stay visible; widening it away would be the wrong fix."""
    audit = S.audit_contamination_scan()
    assert audit.uncovered_scalar_determining == {"delta_gamma", "hamer_8a4"}
    # And the architecture claim the harness gets right, for contrast.
    assert "m_gamma_run15" in audit.covered


def test_hamer_form_is_not_covered_by_the_oracle_form():
    """The precise reason the scan misses it: different digit strings."""
    oracle, hamer = "7751458630189173", "7751458630184"
    assert hamer not in oracle
    assert oracle[:12] == hamer[:12]  # identical for twelve digits
    assert oracle[12] != hamer[12]  # then they part
