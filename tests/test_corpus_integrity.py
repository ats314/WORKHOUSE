"""The corpus is evidence. Nothing may rewrite it silently.

This exists because something did. A first `ruff format .` reached into
`corpus-import/` and modified 296 files before the tool config excluded it, and
nothing caught it — `theory/` and `settlement/` carry hash manifests, the
928-file corpus did not.
"""

import hashlib
import pathlib

import pytest

CORPUS = pathlib.Path(__file__).resolve().parents[1] / "corpus-import"
MANIFEST = CORPUS / "SHA256SUMS"

pytestmark = pytest.mark.skipif(not CORPUS.is_dir(), reason="corpus-import/ not present")


def _entries():
    for line in MANIFEST.read_text().splitlines():
        if line.strip():
            digest, name = line.split("  ", 1)
            yield digest, name


def test_manifest_exists_and_is_substantial():
    assert MANIFEST.exists(), "corpus-import/SHA256SUMS is missing"
    assert sum(1 for _ in _entries()) > 900


def test_every_corpus_file_matches_its_hash():
    mismatched, missing = [], []
    for digest, name in _entries():
        path = CORPUS / name
        if not path.is_file():
            missing.append(name)
        elif hashlib.sha256(path.read_bytes()).hexdigest() != digest:
            mismatched.append(name)
    assert not missing, f"{len(missing)} corpus files vanished: {missing[:5]}"
    assert not mismatched, (
        f"{len(mismatched)} corpus files changed without a manifest update: "
        f"{mismatched[:5]}. If the change was deliberate, regenerate with "
        "`make corpus-manifest` and say why in the PR."
    )


def test_formatters_are_excluded_from_evidence():
    """The config fix that stopped the 296-file rewrite must stay in place."""
    cfg = (CORPUS.parent / "pyproject.toml").read_text()
    assert "corpus-import" in cfg and "settlement" in cfg, (
        "ruff's extend-exclude must keep covering both evidence trees"
    )
