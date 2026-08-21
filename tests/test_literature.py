"""The literature index is an evidence map: every edge must resolve and be honest."""

from workhouse import literature as L


def test_index_loads_and_validates():
    problems = L.validate()
    assert not problems, "literature problems:\n" + "\n".join(f"  - {p}" for p in problems)


def test_every_paper_bears_on_something_that_exists():
    """A citation attached to no claim is decoration."""
    lit = L.load()
    known = L._known_targets()
    for paper in lit.papers:
        assert paper["bears_on"], paper["id"]
        for edge in paper["bears_on"]:
            assert edge["target"] in known, f"{paper['id']} -> {edge['target']}"


def test_no_fulltext_is_stored_without_a_redistributable_licence():
    """Storing a paper is republishing it.

    Most of the load-bearing literature here predates 2004 and carries arXiv's
    assumed-1991-2003 licence, which grants arXiv distribution rights and grants
    this repository none. The gate is enforced rather than remembered.
    """
    lit = L.load()
    allowed = L.REDISTRIBUTABLE | L.VERBATIM_ONLY
    for paper in lit.papers:
        if paper.get("fulltext"):
            assert str(paper["licence"]).lower() in allowed, paper["id"]
    # The licence covering most of this literature grants arXiv distribution
    # rights and grants this repository none. It must stay out of both sets.
    assert "arxiv-assumed-1991-2003" not in allowed
    assert "publisher-copyright" not in allowed


def test_every_paper_is_pinnable():
    """A DOI or an arXiv id, so the citation can be resolved rather than trusted."""
    for paper in L.load().papers:
        assert paper.get("doi") or paper.get("arxiv"), paper["id"]


def test_the_hamer_edge_stays_marked_as_a_transcription():
    """The program's strongest external agreement rests on an unpinned table.

    5.2e-13 against Hamer's a_4 is the best independent evidence here, and the
    corpus itself says the primary table has never been hashed. If someone
    upgrades this edge to `verified`, they must have actually obtained the
    paper — this test is the place that forces the question.
    """
    edges = L.load().bearing_on("HAMER_A4_NUM")
    supplies = [e for _p, e in edges if e["relation"] == "supplies-value"]
    assert len(supplies) == 1
    assert supplies[0]["status"] == "transcription-unverified", (
        "if this was upgraded, Phys. Lett. B 224 must be pinned and hashed and "
        "the five open_questions in the index answered"
    )


def test_the_confusable_paper_is_recorded_as_such():
    """The 2000 GFMC paper shares its first author and subject with the 1989 one.

    The corpus's own recovery engine rejects it by scanning page text. That
    rejection should survive outside one script.
    """
    lit = L.load()
    hsb = next(p for p in lit.papers if p["id"] == "HSB_2000")
    relations = {e["relation"] for e in hsb["bears_on"]}
    assert relations == {"confusable"}


def test_wanted_entries_say_what_they_would_settle():
    for want in L.load().wanted:
        assert str(want["would_settle"]).strip(), want["what"]


def test_a_target_query_finds_the_weingarten_edge():
    rows = L.load().bearing_on("C7")
    assert [p["id"] for p, _e in rows] == ["CS_2006"]
    assert rows[0][1]["status"] == "verified"


def test_a_scope_firewall_forbids_supplying_values():
    """Cross-regime numbers are what corpus §12 exists to stop.

    A paper from another dimension or field content can be compared against and
    borrowed from methodologically. Its coefficients may not enter. The rule is
    enforced in validate(), so an entry cannot declare a firewall and then quietly
    breach it.
    """
    lit = L.load()
    walled = [p for p in lit.papers if str(p.get("scope_firewall", "")).strip()]
    assert walled, "no firewalled entry left to exercise the rule"
    for paper in walled:
        for edge in paper["bears_on"]:
            assert edge["relation"] != "supplies-value", f"{paper['id']} -> {edge['target']}"


def test_the_firewall_rule_actually_fires():
    """Mutate an entry to breach its own firewall and confirm validate() catches it."""
    import copy

    lit = L.load()
    broken = copy.deepcopy(lit)
    walled = next(p for p in broken.papers if str(p.get("scope_firewall", "")).strip())
    walled["bears_on"][0]["relation"] = "supplies-value"
    problems = L.validate(broken)
    assert any("scope firewall" in p for p in problems), problems


def test_stored_fulltext_is_byte_identical_to_what_was_read():
    """NoDerivatives means the stored bytes must be the original ones."""
    import hashlib

    lit = L.load()
    stored = [p for p in lit.papers if p.get("fulltext")]
    assert stored, "no stored paper left to exercise the verbatim rule"
    for paper in stored:
        path = L.LITERATURE_DIR / paper["fulltext"]
        assert path.is_file(), paper["id"]
        assert hashlib.sha256(path.read_bytes()).hexdigest() == paper["source_sha256"]
        assert str(paper["licence"]).lower() in (L.REDISTRIBUTABLE | L.VERBATIM_ONLY)


def test_a_verbatim_only_licence_needs_a_digest():
    """Without one there is nothing proving the file was not reformatted."""
    import copy

    broken = copy.deepcopy(L.load())
    paper = next(
        p
        for p in broken.papers
        if str(p["licence"]).lower() in L.VERBATIM_ONLY and p.get("fulltext")
    )
    paper.pop("source_sha256")
    problems = L.validate(broken)
    assert any("source_sha256 is required" in p for p in problems), problems


def test_publisher_copyright_still_blocks_storage():
    """The gate that keeps seven of eight papers out must not have loosened."""
    import copy

    broken = copy.deepcopy(L.load())
    paper = next(p for p in broken.papers if p["licence"] == "publisher-copyright")
    paper["fulltext"] = "fulltext/whatever.pdf"
    problems = L.validate(broken)
    assert any("does not permit redistribution" in p for p in problems), problems
    assert "publisher-copyright" not in (L.REDISTRIBUTABLE | L.VERBATIM_ONLY)
