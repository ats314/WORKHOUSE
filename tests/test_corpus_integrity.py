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

#: Written by this repository, deliberately outside the pin. Manifest membership
#: is what makes a file corpus evidence, so these are not it — which is exactly
#: why CLAUDE.md may live here while no *pinned* file may bear that name.
REPO_AUTHORED = {"SHA256SUMS", "CLAUDE.md"}


def _entries():
    for line in MANIFEST.read_text(encoding="utf-8").splitlines():
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
    cfg = (CORPUS.parent / "pyproject.toml").read_text(encoding="utf-8")
    assert "corpus-import" in cfg and "settlement" in cfg, (
        "ruff's extend-exclude must keep covering both evidence trees"
    )


def test_nothing_in_the_corpus_escapes_the_manifest():
    """A file present but unpinned is outside the guarantee.

    The hash check only sees names the manifest already lists, so an added file
    is invisible to it — which is how a stale `SHA256SUMS.tmp` from a failed
    generator run sat in the tree unnoticed. Walk the directory instead.
    """
    pinned = {name for _, name in _entries()} | REPO_AUTHORED
    present = {p.relative_to(CORPUS).as_posix() for p in CORPUS.rglob("*") if p.is_file()}
    unpinned = sorted(present - pinned)
    assert not unpinned, (
        f"{len(unpinned)} files in corpus-import/ are not in the manifest: "
        f"{unpinned[:5]}. Either pin them with `make corpus-manifest` or remove them."
    )


def test_the_corpus_carries_no_file_that_would_load_as_instructions():
    """Corpus prose must never arrive as an agent instruction file.

    `corpus-import/CLAUDE.md` did exactly that: a document written upstream, by
    an AI, naming as authority the very version this repository has since
    quarantined. Any agent reading a file in that directory would have picked it
    up automatically. It is kept byte-identical under a name that does not load
    (see ADR 0006); this test stops the class of problem from returning.
    """
    hazards = {"CLAUDE.md", "AGENTS.md", ".cursorrules", "copilot-instructions.md"}
    found = sorted(name for _, name in _entries() if pathlib.PurePath(name).name in hazards)
    assert not found, (
        f"corpus files that auto-load as instructions: {found}. Rename them "
        "(bytes unchanged) and re-point the manifest line."
    )
