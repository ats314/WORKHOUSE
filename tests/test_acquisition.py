"""The acquisition loop reports and fetches; it never curates.

Everything here runs offline: the network legs of the resolver are exercised
only through their pure planning functions, and intake runs on synthetic
files in a temp directory.
"""

import hashlib
import zlib

from workhouse import acquisition as A
from workhouse import literature as L

LIT = L.load()


# -- pure link construction ---------------------------------------------------


def test_pii_from_elsevier_doi():
    assert A.sciencedirect_pii("10.1016/0550-3213(86)90568-7") == "0550321386905687"
    assert A.sciencedirect_pii("10.1016/0370-2693(81)90369-5") == "0370269381903695"
    assert A.sciencedirect_pii("10.1103/PhysRevD.11.395") is None
    assert A.sciencedirect_pii(None) is None


def test_kek_scan_url_pattern():
    """Verified against scans actually retrieved: 80-10-101 is the KPS
    preprint, 82-08-005 is Smit's."""
    assert (
        A.kek_scan_url("80-10-101")
        == "https://lib-extopc.kek.jp/preprints/PDF/1980/8010/8010101.pdf"
    )
    assert (
        A.kek_scan_url("1976-10-104")
        == "https://lib-extopc.kek.jp/preprints/PDF/1976/7610/7610104.pdf"
    )
    assert A.kek_scan_url("2003-01-001") is None  # no known post-2000 pattern
    assert A.kek_scan_url("garbage") is None


def test_the_resolver_plan_never_touches_walled_publishers():
    """ScienceDirect and APS are browser links for a person, on purpose."""
    for record in LIT.papers + LIT.stubs:
        for source, url in A.resolve_plan(record):
            assert "sciencedirect" not in url
            assert "aps.org" not in url and "journals.aps" not in url
            assert source == "arxiv"


def test_browser_links_carry_the_walled_archive_for_a_human():
    hip = LIT.entry("HIP_1986")
    labels = dict(A.browser_links(hip))
    assert "sciencedirect" in labels
    assert labels["doi"].startswith("https://doi.org/10.1016/")


def test_walled_hosts_are_refused_wherever_the_url_comes_from():
    """OpenAlex sometimes lists the publisher's own copy as 'open'. The
    boundary is per-host, not per-code-path: walled hosts stay browser links
    even when a URL arrives dynamically."""
    assert not A.automation_welcome("https://www.sciencedirect.com/science/article/pii/x.pdf")
    assert not A.automation_welcome("https://linkinghub.elsevier.com/retrieve/pii/x")
    assert not A.automation_welcome("https://journals.aps.org/prd/pdf/10.1103/x")
    assert not A.automation_welcome("https://doi.org/10.1016/whatever")
    assert not A.automation_welcome("not a url")
    assert A.automation_welcome("https://arxiv.org/pdf/hep-lat/9901004")
    assert A.automation_welcome("https://lib-extopc.kek.jp/preprints/PDF/1980/8010/8010101.pdf")
    assert A.automation_welcome("https://ecommons.cornell.edu/bitstream/x.pdf")


def test_resolve_refuses_to_overwrite_an_inbox_copy(tmp_path):
    """A file already in the inbox may be a manually supplied scan awaiting
    intake; the resolver must stop before any network request, not clobber it."""
    body = b"%PDF-1.4 a working copy someone supplied"
    (tmp_path / "KS_1975.pdf").write_bytes(body)
    resolution = A.resolve("KS_1975", LIT, inbox=tmp_path)
    assert resolution.saved is None
    assert (tmp_path / "KS_1975.pdf").read_bytes() == body
    assert any("already present" in outcome for _s, _u, outcome in resolution.tried)
    assert all(source == "inbox" for source, _u, _o in resolution.tried)  # no fetch attempted


# -- the manifest -------------------------------------------------------------


def test_manifest_lists_exactly_the_unobtained_ranked():
    rows = A.manifest(LIT)
    ids = [r["id"] for r in rows]
    expected = {r["id"] for r in L.relevance(LIT) if not r["obtained"]}
    assert set(ids) == expected
    assert ids[0] == "KS_1975", "the computed top acquisition target leads the manifest"
    for row in rows:
        assert row["links"], row["id"]
        assert str(row["settles"]).strip(), row["id"]


def test_the_manifest_renders_and_says_the_inbox_rule():
    text = A.format_manifest(LIT)
    assert "KS_1975" in text
    assert "gitignored" in text
    assert "sciencedirect.com" in text  # the human's link to the open archive


# -- intake -------------------------------------------------------------------


def _flate_pdf(text: str) -> bytes:
    """A minimal text-layer PDF-alike: enough for the stdlib sniffer."""
    stream = zlib.compress(f"BT ({text}) Tj ET".encode("latin-1"))
    return b"%PDF-1.4\nstream\n" + stream + b"\nendstream\n%%EOF"


def test_intake_identifies_by_filename(tmp_path):
    (tmp_path / "KS_1975.pdf").write_bytes(b"%PDF-1.4 not really")
    reports = A.intake(tmp_path, LIT)
    assert len(reports) == 1
    assert reports[0].matched == "KS_1975"
    assert reports[0].how == "filename"
    assert any("source_sha256:" in line for line in reports[0].advice)
    assert any("never be committed" in line for line in reports[0].advice)


def test_intake_identifies_by_title_sniff(tmp_path):
    body = _flate_pdf("Hamiltonian formulation of Wilson's lattice gauge theories")
    (tmp_path / "mystery-download.pdf").write_bytes(body)
    reports = A.intake(tmp_path, LIT)
    assert reports[0].matched == "KS_1975", reports[0]
    assert reports[0].how.startswith("title tokens")


def test_intake_recognizes_an_already_pinned_copy(tmp_path):
    body = b"%PDF-1.4 the very bytes that were read"
    digest = hashlib.sha256(body).hexdigest()
    lit = L.Literature(
        papers=[{"id": "X_2000", "title": "Some paper", "source_sha256": digest}],
        stubs=[],
        wanted=[],
    )
    (tmp_path / "whatever.pdf").write_bytes(body)
    reports = A.intake(tmp_path, lit)
    assert reports[0].matched == "X_2000"
    assert "already the pinned copy" in reports[0].how
    assert any("nothing to do" in line for line in reports[0].advice)


def test_intake_flags_different_bytes_under_a_pinned_id(tmp_path):
    lit = L.Literature(
        papers=[{"id": "X_2000", "title": "Some paper", "source_sha256": "ab" * 32}],
        stubs=[],
        wanted=[],
    )
    (tmp_path / "X_2000.pdf").write_bytes(b"%PDF-1.4 other bytes")
    reports = A.intake(tmp_path, lit)
    assert any("DIFFERENT BYTES" in line for line in reports[0].advice)


def test_intake_tells_a_stub_to_be_promoted_first(tmp_path):
    # WEINGARTEN_1978 rather than a Munster id: the Munster stubs keep getting
    # promoted to full entries as their documents arrive, which is the system
    # working — this test just needs any node that is still a stub.
    (tmp_path / "WEINGARTEN_1978.pdf").write_bytes(b"%PDF-1.4 x")
    reports = A.intake(tmp_path, LIT)
    assert reports[0].matched == "WEINGARTEN_1978"
    assert any("promote it to a full entry" in line for line in reports[0].advice)


def test_intake_leaves_the_unidentifiable_unclaimed(tmp_path):
    (tmp_path / "scan0042.pdf").write_bytes(b"%PDF-1.4 image-only, no text layer")
    reports = A.intake(tmp_path, LIT)
    assert reports[0].matched is None
    assert "rename" in reports[0].how


def test_intake_never_edits_the_index(tmp_path):
    before = L.INDEX.read_bytes()
    (tmp_path / "KS_1975.pdf").write_bytes(b"%PDF-1.4 x")
    A.intake(tmp_path, LIT)
    A.format_intake(tmp_path, LIT)
    assert L.INDEX.read_bytes() == before


def test_intake_skips_the_inbox_readme(tmp_path):
    (tmp_path / "README.md").write_text("# rules")
    assert A.intake(tmp_path, LIT) == []


# -- the inbox stays out of the repository ------------------------------------


def test_the_inbox_is_gitignored_except_its_readme():
    gitignore = (A.ROOT / ".gitignore").read_text()
    assert "literature/inbox/*" in gitignore
    assert "!literature/inbox/README.md" in gitignore
    assert (A.INBOX / "README.md").is_file()
    assert "not the repository" in (A.INBOX / "README.md").read_text()
