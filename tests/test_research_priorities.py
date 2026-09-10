"""Research order must not invent proof dependencies or reopen established work."""

from copy import deepcopy
from types import SimpleNamespace

import pytest

from workhouse import claims, derivation_statements, graph, ledger, navigator, research_priorities

M10 = "DERIV:W6_CONDITIONAL_SCORE_TAIL_CONTROL:SCORE_DOMINATION_M10"
R10 = "DERIV:W6_GROUND_JETS_TRANSPORT_BUDGET:SOURCE_ENERGY_JETS_R10"
GRID = "DERIV:W6_GROUND_JETS_TRANSPORT_BUDGET:INTERACTING_GRID_COMPARISON"
SC17 = "DERIV:WILSON_SC17_SPATIAL_CLOSURE:ACTUAL_REFERENCE_DEFECT_BOUND"
TARGET = "DERIV:TEST:TARGET"
INPUT = "DERIV:TEST:INPUT"


def route(*, priority=1, target=TARGET, **fields):
    return {
        "step": f"derive target {priority}",
        "state": "untried",
        "status": "The actual model estimate remains open.",
        "frontier": {
            "priority": priority,
            "target": target,
            "scope": "Actual source form with its full energy domain.",
            "consequence": "Instantiates the separately proved conditional comparison.",
            "decisive_test": "Check the rare-source energy ratio.",
        },
        **fields,
    }


def ledgers(*steps, state="open"):
    return ledger.Ledgers(
        contradictions=[],
        gaps=[
            {
                "id": "G1",
                "title": "Actual comparison",
                "tier": 3,
                "state": state,
                "status": "The recorded scope explains this state.",
                "plan": list(steps),
            }
        ],
        register=[],
        dependency_spine=[],
        headline="",
        unifying_candidates=[],
    )


@pytest.mark.parametrize("lean", [None, []])
def test_proven_analytic_t3_input_is_ready_without_a_lean_proof(monkeypatch, lean):
    """Read the live truth status, including an unformalized analytic input."""
    source = {"id": INPUT, "status": "proven", "evidence": "analytic", "tier": 3}
    if lean is not None:
        source["lean"] = lean
    monkeypatch.setattr(research_priorities.results, "load", lambda: [])
    monkeypatch.setattr(
        research_priorities.recent_research, "load", lambda: SimpleNamespace(nodes=[])
    )
    monkeypatch.setattr(
        research_priorities.derivation_statements,
        "load",
        lambda: {"documents": [{"statements": [source, {"id": TARGET, "status": "open"}]}]},
    )
    selected = route(depends_on=[INPUT], blocked_by=[INPUT])
    before = deepcopy(selected)
    rows = research_priorities.collect(ledgers(selected))
    assert rows[0]["ready"] is True
    assert rows[0]["pending"] == []
    assert rows[0]["inputs"] == [INPUT]
    assert selected == before, "rendering readiness must not rewrite the source register"


@pytest.mark.parametrize("status", ["open", "conditional", "falsified", "superseded", None])
def test_only_established_explicit_completion_inputs_are_ready(status):
    statuses = {TARGET: "open"}
    if status is not None:
        statuses[INPUT] = status
    row = research_priorities.collect(ledgers(route(blocked_by=[INPUT])), statuses)[0]
    assert row["ready"] is False
    assert row["pending"] == [INPUT]
    assert row["pending_status"] == {INPUT: status or "unregistered"}


def test_available_conditional_implication_is_not_an_implicit_blocker():
    """An authored input is not an unproved application premise unless declared so."""
    row = research_priorities.collect(
        ledgers(route(depends_on=[INPUT])), {TARGET: "open", INPUT: "conditional"}
    )[0]
    assert row["ready"] is True
    assert row["inputs"] == [INPUT]
    assert row["pending"] == []


@pytest.mark.parametrize("status", ["falsified", "superseded", "dead", None])
def test_retired_or_missing_mathematical_input_invalidates_readiness(status):
    statuses = {TARGET: "open"}
    if status is not None:
        statuses[INPUT] = status
    row = research_priorities.collect(ledgers(route(depends_on=[INPUT])), statuses)[0]
    assert row["ready"] is False
    assert row["invalid_inputs"] == [INPUT]
    assert row["pending"] == [INPUT]
    assert row["pending_status"][INPUT] == (status or "unregistered")


@pytest.mark.parametrize("reference", ["RESULT:MISSING", "ROUTE:MISSING", "DERIV:TEST:MISSING"])
def test_missing_authored_input_namespaces_fail_closed(reference):
    row = research_priorities.collect(ledgers(route(depends_on=[reference])), {TARGET: "open"})[0]
    assert row["ready"] is False
    assert row["invalid_inputs"] == [reference]


def test_unregistered_target_is_not_ready_without_an_explicit_blocker():
    row = research_priorities.collect(ledgers(route()), {})[0]
    assert row["ready"] is False
    assert row["pending"] == [TARGET]
    assert row["target_status"] == "unregistered"


@pytest.mark.parametrize("reference", ["LEAN:test_lemma", "CITE:TEST_SOURCE"])
def test_source_references_need_not_have_a_mathematical_completion_status(reference):
    row = research_priorities.collect(ledgers(route(depends_on=[reference])), {TARGET: "open"})[0]
    assert row["ready"] is True
    assert row["invalid_inputs"] == []


def test_priority_and_relevance_do_not_create_a_m10_to_r10_dependency():
    first = route(priority=1, target=M10, bears_on=[R10])
    second = route(priority=2, target=R10)
    rows = research_priorities.collect(ledgers(second, first), {M10: "open", R10: "open"})
    assert [r["target"] for r in rows] == [M10, R10]
    assert all(r["ready"] and r["pending"] == [] for r in rows)
    assert rows[1]["inputs"] == []


@pytest.mark.parametrize(
    "target_status", ["proven", "resolved", "discharged", "done", "falsified", "superseded", "dead"]
)
def test_established_and_retired_targets_leave_the_selected_queue(target_status):
    assert research_priorities.collect(ledgers(route()), {TARGET: target_status}) == []


@pytest.mark.parametrize("route_state", ["dead", "done"])
def test_closed_routes_leave_the_selected_queue(route_state):
    assert research_priorities.collect(ledgers(route(state=route_state)), {TARGET: "open"}) == []


def test_discharged_gap_is_excluded_but_partial_gap_remains():
    assert research_priorities.collect(ledgers(route(), state="discharged"), {}) == []
    assert len(research_priorities.collect(ledgers(route(), state="partial"), {})) == 1


@pytest.fixture
def isolated_ledger_validation(tmp_path, monkeypatch):
    """Validation reads only its tiny citation/theorem fixtures, not graph collectors."""
    directory = tmp_path / "ledger"
    directory.mkdir()
    (directory / "documents.yaml").write_text("aliases: []\n", encoding="utf-8")
    (directory / "theorems.yaml").write_text("theorems: []\n", encoding="utf-8")
    monkeypatch.setattr(ledger, "LEDGER_DIR", directory)


@pytest.mark.parametrize("priority", [0, -1, True, "1", 1.5, None])
def test_invalid_priority_is_rejected(isolated_ledger_validation, priority):
    errors = ledger.validate(ledgers(route(priority=priority)))
    assert any("frontier priority must be a positive integer" in error for error in errors)


def test_duplicate_priority_is_rejected_across_distinct_gaps(isolated_ledger_validation):
    led = ledgers(route())
    second = deepcopy(led.gaps[0])
    second["id"] = "G2"
    led.gaps.append(second)
    assert any("duplicate frontier priority 1" in e for e in ledger.validate(led))


@pytest.mark.parametrize("field", ["scope", "consequence", "decisive_test"])
def test_missing_priority_explanation_is_rejected(isolated_ledger_validation, field):
    selected = route()
    selected["frontier"][field] = " "
    assert any(
        f"frontier {field} must be nonempty text" in e for e in ledger.validate(ledgers(selected))
    )


def test_unknown_metadata_and_malformed_target_are_rejected(isolated_ledger_validation):
    selected = route(target="not a catalogue id")
    selected["frontier"]["automatic_proof_rank"] = 1
    errors = ledger.validate(ledgers(selected))
    assert any("frontier target must be a full catalogue id" in e for e in errors)
    assert any("unknown frontier fields" in e for e in errors)


@pytest.mark.parametrize("reference", ["LEAN:test_lemma", "CITE:TEST_SOURCE"])
@pytest.mark.parametrize("field", ["target", "blocked_by"])
def test_readiness_endpoints_require_authored_status_namespaces(
    isolated_ledger_validation, reference, field
):
    selected = route()
    if field == "target":
        selected["frontier"]["target"] = reference
    else:
        selected[field] = [reference]
    errors = ledger.validate(ledgers(selected))
    assert any(f"{field} must name an authored-status claim" in error for error in errors)


@pytest.mark.parametrize("field", ["depends_on", "blocked_by", "bears_on"])
def test_malformed_route_references_are_rejected(isolated_ledger_validation, field):
    selected = route(**{field: "DERIV:TEST:NOT_A_LIST"})
    assert any(
        f"{field} must be a list of full catalogue ids" in e
        for e in ledger.validate(ledgers(selected))
    )


@pytest.fixture
def route_graph(monkeypatch):
    """Exercise actual route-edge generation without unrelated corpus collections."""
    monkeypatch.setattr(graph, "SUITES", [])
    monkeypatch.setattr(graph, "_module_helpers", lambda: {})
    for name in (
        "load_document_aliases",
        "load_runs",
        "decisions",
        "load_theorems",
        "load_provenance",
    ):
        monkeypatch.setattr(claims, name, lambda: [])
    monkeypatch.setattr(graph.results_mod, "load", lambda: [])
    monkeypatch.setattr(graph.study_graph_mod, "load", lambda: [])
    monkeypatch.setattr(
        graph.literature_mod, "load", lambda: SimpleNamespace(papers=[], cites=lambda: [])
    )
    monkeypatch.setattr(
        graph.notes_mod, "load", lambda: SimpleNamespace(reviews=[], archives=[], manifests={})
    )
    for module in (
        graph.recent_research_mod,
        graph.derivation_statements_mod,
        graph.lean_dependencies_mod,
    ):
        monkeypatch.setattr(module, "edge_records", lambda: [])

    def build(led, known_ids):
        monkeypatch.setattr(graph.ledger_mod, "load", lambda: led)
        catalogue = [claims.Claim(id=ref, kind="result", statement=ref) for ref in known_ids]
        return graph.build(catalogue, [])

    return build


@pytest.mark.parametrize("field", ["target", "blocked_by", "bears_on", "depends_on"])
def test_unknown_route_reference_fails_graph_validation(route_graph, field):
    selected = route()
    unknown = "DERIV:TEST:UNKNOWN"
    if field == "target":
        selected["frontier"]["target"] = unknown
    else:
        selected[field] = [unknown]
    rid = claims.route_id("G1", selected["step"])
    built = route_graph(ledgers(selected), {"G1", rid, TARGET})
    assert any(f"unresolved id '{unknown}'" in e for e in graph.validate(built))


def test_route_target_blocker_and_relevance_are_distinct_graph_edges(route_graph):
    selected = route(blocked_by=[INPUT], bears_on=["DERIV:TEST:DOWNSTREAM"])
    rid = claims.route_id("G1", selected["step"])
    built = route_graph(ledgers(selected), {"G1", rid, TARGET, INPUT, "DERIV:TEST:DOWNSTREAM"})
    triples = {(e.src, e.dst, e.type) for e in built.edges}
    assert graph.validate(built) == []
    assert (rid, TARGET, "targets") in triples
    assert (rid, INPUT, "blocked_by") in triples
    assert (rid, "DERIV:TEST:DOWNSTREAM", "bears_on") in triples
    assert not any(e.type == "depends_on" for e in built.edges)


def test_explicit_blocked_by_route_cycle_is_invalid(route_graph):
    first = route(priority=1, target=TARGET)
    second = route(priority=2, target=INPUT)
    first_id = claims.route_id("G1", first["step"])
    second_id = claims.route_id("G1", second["step"])
    first["blocked_by"] = [second_id]
    second["blocked_by"] = [first_id]
    built = route_graph(ledgers(first, second), {"G1", first_id, second_id, TARGET, INPUT})
    assert any("route blocked_by cycle:" in error for error in graph.validate(built))


def test_route_cannot_require_its_own_target_as_completed(route_graph):
    selected = route(blocked_by=[TARGET])
    rid = claims.route_id("G1", selected["step"])
    built = route_graph(ledgers(selected), {"G1", rid, TARGET})
    assert any("route blocked_by its own target:" in error for error in graph.validate(built))


def test_alternative_target_producer_is_not_expanded_into_an_and_dependency(route_graph):
    """A -> required U, B -> required T, C -> T is viable through C then B then A."""
    first = route(priority=1, target=TARGET, blocked_by=[INPUT])
    second = route(priority=2, target=INPUT, blocked_by=[TARGET])
    independent = route(priority=3, target=TARGET)
    steps = [first, second, independent]
    known = {"G1", TARGET, INPUT}
    known.update(claims.route_id("G1", step["step"]) for step in steps)
    built = route_graph(ledgers(*steps), known)
    assert graph.validate(built) == []


def test_explicit_null_frontier_is_benign_in_readiness_validation_and_graph(
    isolated_ledger_validation, route_graph
):
    selected = route()
    selected["frontier"] = None
    led = ledgers(selected)
    assert ledger.validate(led) == []
    assert research_priorities.collect(led, {}) == []
    assert "Research priority:" not in research_priorities.detail(selected)
    rid = claims.route_id("G1", selected["step"])
    built = route_graph(led, {"G1", rid})
    assert graph.validate(built) == []
    assert not any(edge.type == "targets" for edge in built.edges)


@pytest.fixture
def live_registry():
    led = ledger.load()
    statuses = research_priorities.live_statuses(led)
    statements = {
        row["id"]: row
        for doc in derivation_statements.load()["documents"]
        for row in doc["statements"]
    }
    return led, statuses, statements


def test_real_g19_priorities_target_actual_open_derivations(live_registry):
    led, statuses, statements = live_registry
    rows = [r for r in research_priorities.collect(led, statuses) if r["gap"] == "G19"]
    assert [r["target"] for r in rows] == [
        M10,
        R10,
        GRID,
        SC17,
        "DERIV:YANGMILLS_CONTINUUM_BALABAN_MULTISCALE_PROOF:THEOREM_7_1",
    ]
    assert [r["priority"] for r in rows] == [1, 2, 3, 4, 5]
    for ref in (M10, R10, GRID, SC17):
        assert statements[ref]["status"] == "open"
    r10 = next(r for r in rows if r["target"] == R10)
    assert M10 not in r10["inputs"] + r10["pending"]
    assert M10 not in statements[R10]["depends_on"]


def test_proving_sc17_identity_does_not_hide_its_actual_model_target(live_registry):
    led, statuses, _ = live_registry
    statuses = {**statuses, "DERIV:WILSON_SC17_SPATIAL_CLOSURE:R12_R14": "proven"}
    rows = research_priorities.collect(led, statuses)
    assert any(row.get("target") == SC17 for row in rows)
    statuses[SC17] = "proven"
    assert not any(row.get("target") == SC17 for row in research_priorities.collect(led, statuses))


def test_real_g19_routes_emit_exact_targets_and_available_input_edges(live_registry, route_graph):
    led, statuses, _ = live_registry
    g19 = deepcopy(next(g for g in led.gaps if g["id"] == "G19"))
    selected = [s for s in g19["plan"] if s.get("frontier")]
    # Keep the actual selected route metadata and omit unrelated historical gap edges.
    reduced = ledgers()
    reduced.gaps = [{"id": "G19", "plan": selected}]
    known = {"G19"}
    for step in selected:
        known.add(claims.route_id("G19", step["step"]))
        refs = [step["frontier"]["target"]]
        refs += step.get("depends_on", []) + step.get("blocked_by", []) + step.get("bears_on", [])
        known.update(ref for ref in refs if ref in statuses)
    built = route_graph(reduced, known)
    assert graph.validate(built) == []
    triples = {(e.src, e.dst, e.type) for e in built.edges}
    for step in selected:
        rid = claims.route_id("G19", step["step"])
        assert (rid, step["frontier"]["target"], "targets") in triples
        for relation in ("depends_on", "blocked_by", "bears_on"):
            for ref in step.get(relation, []):
                assert (rid, ref, relation) in triples
    r10 = next(s for s in selected if s["frontier"]["target"] == R10)
    r10_route = claims.route_id("G19", r10["step"])
    assert (r10_route, M10, "depends_on") not in triples
    assert (r10_route, M10, "blocked_by") not in triples


def test_route_detail_keeps_target_scope_and_decisive_test():
    selected = route(depends_on=[INPUT], blocked_by=[INPUT], bears_on=["G1"])
    text = research_priorities.detail(selected)
    for value in (
        TARGET,
        selected["frontier"]["scope"],
        selected["frontier"]["consequence"],
        selected["frontier"]["decisive_test"],
        INPUT,
    ):
        assert value in text
    assert "curated order, not a proof dependency" in text


@pytest.fixture
def navigator_snapshot(monkeypatch):
    """The catalogue owns lifecycle; live ledgers contribute only authored metadata."""
    conditional = "DERIV:TEST:CONDITIONAL_IMPLICATION"
    downstream = "DERIV:TEST:DOWNSTREAM"
    selected = route(depends_on=[INPUT, conditional], blocked_by=[INPUT], bears_on=[downstream])
    newer = route(priority=2, target="DERIV:TEST:NEW_LIVE_TARGET")
    newer["step"] = "new route absent from the supplied snapshot"
    led = ledgers(selected, newer)
    rid = claims.route_id("G1", selected["step"])
    catalogue = [
        claims.Claim(id="G1", kind="gap", statement="Snapshot gap", status="cost 3 · partial"),
        claims.Claim(id=rid, kind="route", statement=selected["step"], status="live", tier=3),
        claims.Claim(id=TARGET, kind="result", statement="Actual target", status="open", tier=3),
        claims.Claim(
            id=INPUT,
            kind="result",
            statement="Actual analytic input",
            status="proven",
            tier=3,
            evidence="analytic",
        ),
        claims.Claim(
            id=conditional,
            kind="result",
            statement="Available conditional theorem",
            status="conditional",
            tier=3,
            evidence="analytic",
        ),
        claims.Claim(id=downstream, kind="result", statement="Later consequence", status="open"),
        claims.Claim(
            id=newer["frontier"]["target"], kind="result", statement="New target", status="open"
        ),
    ]
    monkeypatch.setattr(ledger, "load", lambda: led)

    def forbidden_collection(*args, **kwargs):
        pytest.fail(
            "snapshot navigation must not collect live statuses, claims, symbols or a graph"
        )

    monkeypatch.setattr(research_priorities, "live_statuses", forbidden_collection)
    monkeypatch.setattr(claims, "collect", forbidden_collection)
    monkeypatch.setattr(claims, "load_symbols", forbidden_collection)
    monkeypatch.setattr(graph, "build", forbidden_collection)
    return SimpleNamespace(
        led=led,
        catalogue=catalogue,
        route_id=rid,
        selected=selected,
        newer=newer,
        graph=graph.Graph(edges=[], dangling=[]),
    )


def test_snapshot_navigation_excludes_new_live_route_without_collecting(navigator_snapshot):
    case = navigator_snapshot
    rows = navigator.priority_rows("G1", case.catalogue)
    assert [row["id"] for row in rows] == [case.route_id]
    assert rows[0]["state"] == "live", "the ledger's untried state must not replace the snapshot"
    assert rows[0]["ready"] is True
    data, found = navigator.neighborhood("G1", case.catalogue, [], case.graph)
    text, text_found = navigator.explain("G1", case.catalogue, [], case.graph)
    assert found and text_found
    assert data["priorities"] == rows
    assert case.newer["step"] not in text
    assert case.newer["frontier"]["target"] not in text


@pytest.mark.parametrize("input_status", ["proven", "open"])
def test_gap_and_direct_route_share_snapshot_readiness_and_text_json_metadata(
    navigator_snapshot, input_status
):
    case = navigator_snapshot
    next(claim for claim in case.catalogue if claim.id == INPUT).status = input_status
    gap_rows = navigator.priority_rows("G1", case.catalogue)
    direct_rows = navigator.priority_rows(case.route_id, case.catalogue)
    assert direct_rows == gap_rows
    row = direct_rows[0]
    assert row["ready"] is (input_status == "proven")
    assert row["input_status"]["DERIV:TEST:CONDITIONAL_IMPLICATION"] == "conditional"
    assert row["pending"] == ([] if input_status == "proven" else [INPUT])
    for node in ("G1", case.route_id):
        data, found = navigator.neighborhood(node, case.catalogue, [], case.graph)
        text, text_found = navigator.explain(node, case.catalogue, [], case.graph)
        assert found and text_found
        assert data["priorities"] == direct_rows
        for field in ("id", "step", "target", "scope", "consequence", "decisive_test"):
            assert row[field] in text
        assert "conditional implication; actual model hypotheses remain separate" in text
        if row["ready"]:
            assert "readiness: no recorded completion blocker" in text
        else:
            assert f"completion awaits: {INPUT} (open)" in text


@pytest.mark.parametrize("target_status", ["proven", "falsified", "superseded"])
def test_snapshot_target_status_suppresses_live_open_route(navigator_snapshot, target_status):
    case = navigator_snapshot
    assert case.led.gaps[0]["state"] == "open"
    assert case.selected["state"] == "untried"
    next(claim for claim in case.catalogue if claim.id == TARGET).status = target_status
    assert navigator.priority_rows("G1", case.catalogue) == []
    assert navigator.priority_rows(case.route_id, case.catalogue) == []
    data, found = navigator.neighborhood("G1", case.catalogue, [], case.graph)
    text, text_found = navigator.explain("G1", case.catalogue, [], case.graph)
    assert found and text_found
    assert data["priorities"] == []
    assert "Current derivation priorities" not in text


@pytest.mark.parametrize(
    "kind,status", [("route", "done"), ("route", "dead"), ("gap", "cost 3 · discharged")]
)
def test_snapshot_route_and_gap_lifecycle_controls_priority_queue(navigator_snapshot, kind, status):
    case = navigator_snapshot
    next(claim for claim in case.catalogue if claim.kind == kind).status = status
    assert navigator.priority_rows("G1", case.catalogue) == []
    assert navigator.priority_rows(case.route_id, case.catalogue) == []
    data, found = navigator.neighborhood(case.route_id, case.catalogue, [], case.graph)
    assert found and data["priorities"] == []


def test_snapshot_route_requires_its_owning_gap_and_correct_node_kind(navigator_snapshot):
    case = navigator_snapshot
    no_gap = [claim for claim in case.catalogue if claim.id != "G1"]
    assert navigator.priority_rows(case.route_id, no_gap) == []
    assert navigator.priority_rows(INPUT, case.catalogue) == []
    assert navigator.priority_rows("ROUTE:ABSENT", case.catalogue) == []
    next(claim for claim in case.catalogue if claim.id == case.route_id).kind = "result"
    assert navigator.priority_rows("G1", case.catalogue) == []


def test_gap_standing_text_agrees_with_snapshot_lifecycle(navigator_snapshot):
    case = navigator_snapshot
    next(claim for claim in case.catalogue if claim.id == "G1").status = "cost 3 · discharged"
    text, found = navigator.explain("G1", case.catalogue, [], case.graph)
    assert found
    assert "Gap standing\033[0m  discharged" in text
    assert "Gap standing\033[0m  open" not in text
