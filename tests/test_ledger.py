"""Structural integrity of the contradiction and gap registers."""

from workhouse import ledger as L


def test_ledgers_load_and_validate():
    led = L.load()
    problems = L.validate(led)
    assert not problems, "ledger problems:\n" + "\n".join(f"  - {p}" for p in problems)


def test_registers_are_complete():
    led = L.load()
    assert led.contradiction_ids == {f"C{i}" for i in range(1, 23)}
    assert led.gap_ids == {f"G{i}" for i in range(1, 20)}


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


def test_g3_protocol_has_all_eleven_items():
    led = L.load()
    g3 = next(g for g in led.gaps if g["id"] == "G3")
    assert len(g3["protocol"]) == 11, "the adjudication protocol is an 11-item freeze"
    assert "inventory_trap" in g3, "the 3895-vs-3850 inventory warning must travel with G3"
