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
    for paper in lit.papers:
        if paper.get("fulltext"):
            assert str(paper["licence"]).lower() in L.REDISTRIBUTABLE, paper["id"]
    assert "arxiv-assumed-1991-2003" not in L.REDISTRIBUTABLE


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
    edges = L.load().bearing_on("HAMER_A4")
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
