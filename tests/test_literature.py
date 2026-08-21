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


def test_the_hamer_edge_is_verified_and_stays_pinned():
    """The upgrade this test's predecessor demanded has happened — guard it.

    The old test forced the question: an upgrade to `verified` requires the
    Phys. Lett. B 224 table pinned and hashed and the five open questions
    answered. On 2026-08-21 a maintainer-supplied copy of the paper was read,
    Table 1 verified against the page image, the digest recorded, and all
    five questions answered from the text. What must not rot now: the digest
    must stay present (the publisher-copyright PDF itself is never stored),
    the answers must stay with the entry, and a downgrade back to
    transcription status would be silent evidence-loss.
    """
    lit = L.load()
    paper = next(p for p in lit.papers if p["id"] == "HAMER_1989")
    edges = lit.bearing_on("HAMER_A4_NUM")
    supplies = [e for _p, e in edges if e["relation"] == "supplies-value"]
    assert len(supplies) == 1
    assert supplies[0]["status"] == "verified"
    assert len(str(paper.get("source_sha256", ""))) == 64, "the pin must not disappear"
    assert paper.get("fulltext") is None, "publisher copyright: the PDF is never stored"
    assert len(paper.get("answered_questions", [])) == 5
    assert all(q.get("q") and q.get("a") for q in paper["answered_questions"])


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


# -- the citation web ---------------------------------------------------------


def test_every_cites_entry_resolves():
    """A citation pointing at nothing is the same failure as a dangling edge."""
    lit = L.load()
    for src, dst in lit.cites():
        assert dst in lit.node_ids, f"{src} cites unresolvable {dst}"
        assert dst != src


def test_an_unresolvable_cite_is_caught():
    import copy

    broken = copy.deepcopy(L.load())
    paper = next(p for p in broken.papers if p.get("cites"))
    paper["cites"].append("NO_SUCH_PAPER_1900")
    problems = L.validate(broken)
    assert any("cites unknown id" in p for p in problems), problems


def test_an_orphan_stub_is_rejected_as_decoration():
    """A stub earns its place by being cited; one nothing cites is a bibliography."""
    import copy

    broken = copy.deepcopy(L.load())
    broken.stubs.append(
        {
            "id": "ORPHAN_1999",
            "title": "x",
            "venue": "y",
            "year": 1999,
            "doi": "10.0/1",
            "note": "z",
        }
    )
    problems = L.validate(broken)
    assert any("no indexed paper cites" in p for p in problems), problems


def test_a_stub_cannot_carry_evidence():
    """bears_on on a stub would be an evidence edge dodging the evidence rules."""
    import copy

    broken = copy.deepcopy(L.load())
    stub = next(s for s in broken.stubs)
    stub["bears_on"] = [{"target": "C2", "relation": "corroborates", "status": "verified"}]
    problems = L.validate(broken)
    assert any("cannot bear on a claim" in p for p in problems), problems


def test_an_undated_inspire_count_is_rejected():
    """A count without its retrieval date reads as current forever."""
    import copy

    broken = copy.deepcopy(L.load())
    paper = next(p for p in broken.papers if p.get("inspire_citations"))
    paper["inspire_citations"].pop("as_of")
    problems = L.validate(broken)
    assert any("without as_of" in p for p in problems), problems


def test_in_degree_is_computed_and_covers_every_node():
    """The local weight is derived at call time; zeros are present, not absent."""
    lit = L.load()
    degree = lit.in_degree()
    assert set(degree) == lit.node_ids
    # The foundational Hamiltonian paper is the web's hub, and it is exactly
    # the kind of fact this layer exists to compute rather than remember.
    top = max(degree, key=lambda n: (degree[n], n))
    assert top == "KS_1975", sorted(degree.items(), key=lambda kv: -kv[1])[:3]


def test_the_acquisition_target_falls_out_of_the_data():
    """The most in-web-cited unpinned paper surfaces automatically."""
    targets = L.acquisition_targets()
    assert targets, "nothing to acquire would mean every source is pinned"
    assert targets[0]["id"] == "KS_1975"
    assert all(not t["obtained"] and t["in_web"] > 0 for t in targets)


def test_the_two_relevance_weights_stay_separate():
    """Global fame must not outrank local load-bearing: MP_1999 has two orders
    of magnitude more INSPIRE citations than KS_1975 has in-web ones, and the
    ranking still puts KS_1975 first."""
    rows = L.relevance()
    ids = [r["id"] for r in rows]
    assert ids.index("KS_1975") < ids.index("MP_1999")


def test_holes_are_leads_with_a_checking_recipe():
    """Every hole says what checking it would take, and none is promoted."""
    for hole in L.holes():
        assert hole.kind in ("disconnected-pair", "missed-source")
        assert "Check:" in hole.lead, hole
        assert hole.target
        assert len(hole.pair) == 2


def test_a_confusable_edge_never_opens_a_hole():
    """HSB_2000 is attached to HAMER_A4_NUM to say it is NOT a source; its
    citation disconnection from HAMER_1989 is the expected state, not a lead."""
    for hole in L.holes():
        assert "HSB_2000" not in hole.pair, hole


def test_the_hamer_kss_disentanglement_holds():
    """Hamer's [7] is the three-author 1976 series paper, not KS_1975.

    The conflation shipped once, in this file's own note. The contradiction
    edges must stay on KSS_1976, KS_1975 must carry none, and the web must
    record Hamer citing both -- the published-comparisons suite asserts the
    same thing at verify time.
    """
    lit = L.load()
    kss = next(p for p in lit.papers if p["id"] == "KSS_1976")
    ks = next(p for p in lit.papers if p["id"] == "KS_1975")
    hamer = next(p for p in lit.papers if p["id"] == "HAMER_1989")
    assert len(kss["authors"]) == 3 and len(ks["authors"]) == 2
    assert {e["relation"] for e in kss["bears_on"]} == {"contradicts"}
    # The exact target pair, which the invariant check leaves unnamed to keep
    # its T1 declaration clean of *_NUM spellings.
    assert {e["target"] for e in kss["bears_on"]} == {"D_3", "M_GAMMA_4_NUM"}
    assert all(e["relation"] != "contradicts" for e in ks["bears_on"])
    assert {"KS_1975", "KSS_1976"} <= set(hamer["cites"])


def test_the_kps_table_is_pinned_and_its_edges_verified():
    """The KEK scan of the 1980 KPS preprint carries the exact Table 2 that
    validates the certified sigma series rational for rational; the pin, the
    two verified edges, and the superseded-PRL trap stub must not rot. The
    exact equalities themselves are asserted by the published-comparisons
    suite at verify time."""
    lit = L.load()
    kps = next(p for p in lit.papers if p["id"] == "KPS_1981")
    assert len(str(kps.get("source_sha256", ""))) == 64
    assert kps.get("fulltext") is None, "publisher copyright: the scan is pinned, never stored"
    assert {e["target"]: e["status"] for e in kps["bears_on"]} == {
        "G7": "verified",
        "R14": "verified",
    }
    assert "KPS_PRL_1979" in kps["cites"]
    trap = next(s for s in lit.stubs if s["id"] == "KPS_PRL_1979")
    assert "supersede" in trap["note"], "the wrong-x^5 warning must stay recorded"


def test_read_citers_are_pinned_and_their_negatives_recorded():
    """The three indexed citers of Hamer 1989 were read and digest-pinned; the
    two checked for coefficient tables record the negative in their notes so
    nobody re-reads them hunting for one."""
    lit = L.load()
    for pid in ("SZH_1997", "LLL_2006", "CM_2003"):
        paper = next(p for p in lit.papers if p["id"] == pid)
        assert len(str(paper.get("source_sha256", ""))) == 64, f"{pid} lost its pin"
        assert paper.get("fulltext") is None, f"{pid}: no licence permits storage"
    assert "NONE" in next(p for p in lit.papers if p["id"] == "SZH_1997")["note"]
    assert "NEGATIVE" in next(p for p in lit.papers if p["id"] == "CM_2003")["note"]
