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


def test_only_the_off_axis_coefficient_remains_open():
    """C1 dissolved into an anchoring distinction; C2 is the real open item."""
    led = L.load()
    assert {c["id"] for c in led.open_contradictions} == {"C2"}
    for c in led.open_contradictions:
        assert "G3" in c["blocks"], f"{c['id']} must route to the adjudication run"


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
        "sealed scalar sweep (demoted, optional)",
    ], "the rewritten route's steps: the executed pair, the live one, the demoted sweep"
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
