"""Structural integrity of the contradiction and gap registers."""

from workhouse import ledger as L


def test_ledgers_load_and_validate():
    led = L.load()
    problems = L.validate(led)
    assert not problems, "ledger problems:\n" + "\n".join(f"  - {p}" for p in problems)


def test_registers_are_complete():
    """C1-C22 is closed (a verbatim transcription of the corpus's own
    register, which cannot grow); the gap register is the open-work list and
    grew deliberately on 2026-08-22 when G20-G23 scaffolded the analysis-side
    notes program (docs/referee/notes_review_core_theory_2026-08-22.md). The
    rule kept: gaps are contiguous from G1 with no holes, so a deleted or
    renumbered gap cannot pass silently."""
    led = L.load()
    assert led.contradiction_ids == {f"C{i}" for i in range(1, 23)}
    assert led.gap_ids == {f"G{i}" for i in range(1, len(led.gap_ids) + 1)}
    assert led.gap_ids >= {f"G{i}" for i in range(1, 24)}


def test_no_contradiction_remains_open_and_c2_closed_by_derivation():
    """C1 dissolved into an anchoring distinction; C2, the last real open item,
    was resolved by derivation on 2026-09-04 (ADR 0024). Both of its recorded
    sides stay listed, as C1's and C15's do."""
    led = L.load()
    assert {c["id"] for c in led.open_contradictions} == set()
    c2 = next(c for c in led.contradictions if c["id"] == "C2")
    assert c2["status"] == "resolved"
    assert "25/1024" in c2["resolution"]
    assert {s["label"] for s in c2["sides"]} >= {"historical", "v10a.26"}


def test_disputed_contradictions_carry_both_numbers():
    led = L.load()
    for c in led.open_contradictions:
        labels = [s["label"] for s in c["sides"]]
        assert len(labels) >= 2, f"{c['id']} records only one side: {labels}"


def test_c1_forbids_the_terminology_that_manufactured_it():
    """The false contradiction recurs whenever both are called "m_4"."""
    led = L.load()
    c1 = next(c for c in led.contradictions if c["id"] == "C1")
    assert c1["status"] == "resolved"
    term = c1["terminology"]
    assert set(term["correct"]) == {"q_band^(4)", "m_Gamma^(4)"}
    assert "m_4" in term["forbidden"]
    # Both quantities must stay on the record even though this is no longer a dispute.
    labels = " ".join(q["label"] for q in c1["quantities"])
    assert "band-kernel anchor" in labels and "vacuum-subtracted" in labels


def test_g3_no_longer_claims_to_resolve_c1():
    led = L.load()
    g3 = next(g for g in led.gaps if g["id"] == "G3")
    assert "C1" not in g3["resolves"], "C1 is dissolved, not pending adjudication"
    assert "C2" in g3["resolves"]


def test_load_bearing_gaps_are_the_bridge_and_the_free_energy_bound():
    led = L.load()
    assert {g["id"] for g in led.load_bearing_gaps} == {"G17", "G18"}


def test_g3_rewrite_keeps_the_protocol_and_the_traps():
    """G3 was rewritten 2026-08-28 (maintainer's instruction): the sealed
    sweep cannot decide C_shp, so the route changed. The failure this test
    now prevents: the rewrite silently shedding the 11-item freeze (whose
    target-blindness discipline carries over to the new route) or the
    inventory warning. The protocol is retained as prose, so pin its
    load-bearing phrases rather than a list length."""
    led = L.load()
    g3 = next(g for g in led.gaps if g["id"] == "G3")
    superseded = g3["superseded_protocol"]
    for phrase in (
        "canonical u",
        "occurrence",
        "609",
        "Mobius",
        "linked subtraction",
        "sealed hashes",
        "no targets",
        "3895",
        "189-record",
        "lambda_R = 2*lambda_M",
        "q_band^(4) - E_0^(4)",
        "W_22",
        "from one run",
    ):
        assert phrase in superseded, f"superseded protocol lost: {phrase}"
    steps = [step["step"] for step in g3["plan"]]
    assert steps == [
        "block-structure comparison",
        "targeted kernel-bearing recomputation",
        "independent cross-amplitude computation",
        # Added 2026-08-30. The cross-amplitude step measured its own blocker
        # and found the register's 10-100x mis-attributed (3.9x, Amdahl-capped
        # at 5.3x); this step is the cheaper route that does not need the
        # engine at all, and it sits AFTER the measured one so the record
        # still reads in the order the work happened.
        "off-axis channel assembly through workhouse.cellular",
        "sealed scalar sweep (demoted, optional)",
        # Added 2026-09-01, from the graph, and run the same day: symmetry
        # fixes no orbit's sign and no plane-basis convention reaches the
        # flip, so the route closed `done` with a negative result. It stays
        # listed because a closed route is evidence the next reader needs.
        # Added 2026-09-01 from the Hodge form: the two-hop weight u is one
        # number the kernels disagree on by 4.13x; it cannot decide C2 but
        # decides which pipeline to trust, on a ten-link cluster.
        "chain amplitude u on the three-plaquette cluster",
        "covariance sign test of the two flipped orbits",
        # Added 2026-09-02 when the cross-amplitude route closed: the assembled
        # rho rests on the one cluster type no agreed record contains, so the
        # route that would settle C2's third side is that cluster from a third
        # implementation or from the historical pipeline's own ledger.
        "the corner cluster from a third implementation, or from the historical pipeline's "
        "own face-resolved ledger",
        # Added 2026-09-04 when the corner route closed both ways (ADR 0024):
        # the ledger closure the maintainer authorised the same night, and the
        # one follow-up that can sharpen but not overturn the result.
        "close C2 in the ledger on the recorded evidence -- the maintainer's call",
        "the pair cluster from the third engine, pure-six family included",
    ], (
        "G3's steps: the executed pair, the measured one, the cheaper route, the demoted "
        "sweep, the chain amplitude, the sign test, the corner cluster, the closure, the "
        "pair cluster"
    )
    sign_test = next(
        s for s in g3["plan"] if s["step"] == "covariance sign test of the two flipped orbits"
    )
    assert sign_test["state"] == "done", "the sign test was run on 2026-09-01; it is not open work"
    assert len(sign_test["closed_by"]) == 3 and all(
        ref.startswith("CHK:") for ref in sign_test["closed_by"]
    ), "a done route names the checks that closed it"
    assert "inventory_trap" in g3, "the 3895-vs-3850 inventory warning must travel with G3"


def test_governing_register_is_complete():
    led = L.load()
    assert led.register_ids == {f"R{i}" for i in range(1, 24)}


def test_the_register_transcription_is_verbatim():
    """The ledger must quote the governing document, not retell it.

    A paraphrase is how a register drifts: each retelling is defensible on its
    own and the sequence ends somewhere the corpus never said. Re-extract §14
    and compare, so drift is a build failure rather than a slow rewrite.
    """
    import sys
    from pathlib import Path

    sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
    from transcribe_register import DOCUMENT, items

    led = L.load()
    extracted = items(DOCUMENT)
    assert len(extracted) == len(led.register)
    for (title, text), entry in zip(extracted, led.register, strict=True):
        assert entry["title"] == title
        assert entry["text"].strip() == text, f"{entry['id']} is not verbatim"


def test_the_crosswalk_is_pinned():
    """Sameness is asserted by hand, so growing it must be a reviewed edit.

    No test can check that two prose items state the *same* claim rather than a
    related one. What a test can do is refuse to let the crosswalk grow
    silently: a new pair has to be added here as well, which is the point where
    someone has to defend it.
    """
    led = L.load()
    pairs = {(r["id"], c) for r in led.register for c in r["contradictions"]}
    assert pairs == {
        ("R1", "C4"),  # the Y label erratum
        ("R4", "C1"),  # anchoring, not a dispute
        ("R5", "C2"),  # the off-axis coefficient
        ("R6", "C22"),  # the target-derived August shift
        ("R8", "C12"),  # radial directional curvature
        ("R10", "C6"),  # the mobility promotion
        ("R12", "C21"),  # Monte Carlo language
        ("R13", "C9"),  # SU(4) flat-branch identity
        ("R14", "C5"),  # sigma sign convention
        ("R21", "C8"),  # the physical pentagonal manifold
        ("R23", "C3"),  # scope
    }
    # Eleven of twenty-two. The other eleven C-ids have no verbatim counterpart
    # in the governing register, and the crosswalk says so by staying empty.
    unmapped = led.contradiction_ids - {c for _, c in pairs}
    assert len(unmapped) == 11


def test_every_open_contradiction_is_visible_in_the_governing_register():
    """An open C-id with no governing counterpart would be unaccounted for."""
    led = L.load()
    for c in led.open_contradictions:
        assert led.governing(c["id"]), f"{c['id']} is open but the register does not carry it"


def test_the_nine_items_v4_3_added_are_present():
    """v3 ended at 14; v4.3 has 23. The additions are the reason to promote it."""
    led = L.load()
    added = {r["title"] for r in led.register if int(r["id"][1:]) in range(14, 23)}
    assert added == {
        "String signs",
        "Sixth-order scope",
        "Registry lag",
        "Cap geometry",
        "Atomic shell-six source",
        "OP1 enclosure",
        "Pentagonal provenance",
        "Pentagonal Hamiltonian firewall",
        "Pentagonal fifth-order scope",
    }


def test_no_ledger_file_has_a_duplicate_mapping_key():
    """yaml.safe_load keeps the LAST of two identical keys, and says nothing.

    Written after exactly that: an insertion landed between a step's ``status``
    and its ``what``, leaving one step with two ``what`` keys and the step above
    it with none. Every test still passed, ``workhouse verify`` still passed,
    and the register silently carried the wrong prose under the right heading —
    which is the failure mode this whole repository exists to make impossible.
    A loader that raises on duplicates costs nothing and closes it.
    """
    import yaml

    class StrictLoader(yaml.SafeLoader):
        pass

    def no_duplicates(loader, node, deep=False):
        seen = set()
        for key_node, _value in node.value:
            key = loader.construct_object(key_node, deep=deep)
            assert key not in seen, f"duplicate key {key!r} at {key_node.start_mark}"
            seen.add(key)
        return yaml.SafeLoader.construct_mapping(loader, node, deep)

    StrictLoader.add_constructor(yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, no_duplicates)
    from pathlib import Path

    ledger_dir = Path(__file__).resolve().parents[1] / "ledger"
    for path in sorted(ledger_dir.glob("*.yaml")):
        yaml.load(path.read_text(encoding="utf-8"), Loader=StrictLoader)


def test_plan_steps_carry_a_closed_route_state():
    """Every plan step is a route with a state from the closed vocabulary.

    The failure this prevents: a route a run has closed reading as open work.
    G3's sealed sweep was re-attempted by four sessions after it was known to
    emit only the Gamma scalar; it is now `dead`, with the finding that killed
    it as its closer, and a validator rejects a step without a state.
    """
    led = L.load()
    steps = [(g["id"], st) for g in led.gaps for st in g.get("plan", []) or []]
    assert steps
    for gid, st in steps:
        assert st.get("state") in L.ROUTE_STATES, (gid, st.get("step"))
    g3 = next(g for g in led.gaps if g["id"] == "G3")
    by_step = {st["step"]: st for st in g3["plan"]}
    assert by_step["sealed scalar sweep (demoted, optional)"]["state"] == "dead"
    assert by_step["sealed scalar sweep (demoted, optional)"]["cannot_decide"] == ["C2"]
    assert by_step["off-axis channel assembly through workhouse.cellular"]["state"] == "dead"
    assert by_step["independent cross-amplitude computation"]["state"] == "done"
    # a step with an unknown state is a validation failure, not a silent open route
    import copy

    broken = copy.deepcopy(led)
    next(g for g in broken.gaps if g["id"] == "G3")["plan"][0]["state"] = "pending"
    assert any("state must be one of" in p for p in L.validate(broken))
