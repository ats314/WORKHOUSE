"""The graph is generated, resolvable, and never asserts what no source records."""

import json
import subprocess
import sys
from dataclasses import asdict
from fractions import Fraction
from pathlib import Path

from workhouse import certified, navigator
from workhouse import claims as C
from workhouse import graph as G

ROOT = Path(__file__).resolve().parents[1]
CATALOGUE = C.collect()
SYMBOLS = C.load_symbols()
GRAPH = G.build(CATALOGUE, SYMBOLS)
TRIPLES = {(e.src, e.dst, e.type) for e in GRAPH.edges}


def test_graph_file_is_current():
    expected = "".join(json.dumps(asdict(e), sort_keys=True) + "\n" for e in GRAPH.edges)
    assert G.GRAPH.read_text() == expected, "stale; run `make catalogue`"


def test_every_endpoint_resolves_and_nothing_dangles():
    nodes = {c.id for c in CATALOGUE} | {f"SYM:{s['id']}" for s in SYMBOLS}
    for edge in GRAPH.edges:
        assert edge.src in nodes, edge
        assert edge.dst in nodes, edge
    assert not GRAPH.dangling, GRAPH.dangling
    assert G.validate(GRAPH) == []


def test_building_twice_is_byte_identical():
    again = G.build(CATALOGUE, SYMBOLS)
    assert G.render(again) == G.render(GRAPH)


def test_edge_types_are_the_closed_set():
    assert {e.type for e in GRAPH.edges} <= G.TYPES
    assert {e.how for e in GRAPH.edges} <= {"curated", "derived"}


def test_the_ledger_edges_survive_the_round_trip():
    """One pinned edge per curated source, so a silent format change is loud."""
    assert ("G3", "C2", "resolves") in TRIPLES
    assert ("C2", "G3", "blocks") in TRIPLES
    assert ("R5", "C2", "contradictions") in TRIPLES
    assert ("R5", "G3", "gaps") in TRIPLES
    assert ("SYM:c_shp", "C2", "claims") in TRIPLES
    assert ("SYM:q_band_4", "CONST:Q_BAND_4", "code_names") in TRIPLES
    assert ("LIT:CS_2006:C7", "C7", "bears_on") in TRIPLES
    assert ("LIT:HAMER_1989:HAMER_A4_NUM", "CONST:HAMER_A4_NUM", "bears_on") in TRIPLES
    assert ("U3", "G14", "supported_by") in TRIPLES
    assert ("U3", "ADR:0005", "supported_by") in TRIPLES


def test_the_citation_web_is_in_the_graph():
    """Curated cites edges run between paper-level LIT nodes, one per curated
    entry, and the conflation this layer untangled stays untangled: Hamer 1989
    cites BOTH Kogut-Susskind 1975 and Kogut-Sinclair-Susskind 1976."""
    assert ("LIT:HAMER_1989", "LIT:KS_1975", "cites") in TRIPLES
    assert ("LIT:HAMER_1989", "LIT:KSS_1976", "cites") in TRIPLES
    assert ("LIT:HAMER_1989", "LIT:HIP_1986", "cites") in TRIPLES
    assert ("LIT:CS_2006", "LIT:WEINGARTEN_1978", "cites") in TRIPLES
    assert ("LIT:LLL_2006", "LIT:HAMER_1989", "cites") in TRIPLES
    curated_cites = [e for e in GRAPH.edges if e.type == "cites" and e.how == "curated"]
    assert all(e.src.startswith("LIT:") and e.dst.startswith("LIT:") for e in curated_cites)
    from workhouse import literature

    assert len(curated_cites) == len(set(literature.load().cites()))


def test_paper_level_nodes_exist_beside_the_edge_records():
    """LIT:<id> is the paper; LIT:<id>:<target> is one bearing claim of it."""
    ids = {c.id for c in CATALOGUE}
    assert "LIT:HAMER_1989" in ids
    assert "LIT:HAMER_1989:C1" in ids
    assert "LIT:WEINGARTEN_1978" in ids  # stubs are nodes too
    stub = next(c for c in CATALOGUE if c.id == "LIT:WEINGARTEN_1978")
    assert "stub" in stub.status


def test_checks_cite_the_ids_buried_in_their_free_text():
    """The load-bearing derived join: section strings, check names, suite names."""
    tier_collapse_cites = {
        s for (s, d, t) in TRIPLES if d == "G14" and t == "cites" and s.startswith("CHK:")
    }
    assert len(tier_collapse_cites) >= 6, tier_collapse_cites
    assert any(d == "C7" and t == "cites" for (_s, d, t) in TRIPLES)
    assert any(d == "ADR:0005" and t == "cites" for (_s, d, t) in TRIPLES)


def test_the_adr_lifecycle_is_structural():
    assert ("ADR:0002", "ADR:0001", "amends") in TRIPLES
    assert ("ADR:0005", "ADR:0004", "retracts") in TRIPLES
    # An "ADR NNNN" in a decision's body is a mention, same as a ledger id.
    assert ("ADR:0007", "ADR:0004", "mentions") in TRIPLES


def test_the_retracted_dependency_is_never_materialized():
    """ADR 0005 removed the G14 -> G9 dependency ADR 0004 proposed.

    The ADR nodes may mention both ids; nothing may connect the gaps
    themselves. If this fails, a generator has resurrected a retracted claim.
    """
    between = {(s, d, t) for (s, d, t) in TRIPLES if {s, d} == {"G14", "G9"}}
    assert not between, between


def test_theorem_map_is_complete_and_sound():
    """Every Lean theorem has a curated entry, and every entry checks out.

    A `promotes` entry must match exactly ONE registered check: a duplicate
    check name would silently fan a curated T0-promotion edge out to a suite
    no YAML author ever pointed at.
    """
    lean_names = {c.name for c in certified.lean_claims()}
    entries = C.load_theorems()
    assert {t["name"] for t in entries} == lean_names
    nodes = {c.id for c in CATALOGUE} | {f"SYM:{s['id']}" for s in SYMBOLS}
    check_ids: dict[str, list[str]] = {}
    for suite in G.SUITES:
        for name, _sec, _tier, _fn in suite.checks:
            check_ids.setdefault(name, []).append(C.check_id(suite.name, name))
    for entry in entries:
        for target in entry.get("formalizes", []):
            assert target in nodes, f"{entry['name']}: unknown target {target!r}"
        for check in entry.get("promotes", []):
            assert len(check_ids.get(check, [])) == 1, (
                f"{entry['name']}: {check!r} must match exactly one registered check"
            )
        if "value" in entry:
            Fraction(entry["value"])  # must parse exactly


def test_catalogue_ids_are_unique():
    """_slug truncates to 40 chars; a collision would silently merge two claims."""
    ids = [c.id for c in CATALOGUE]
    duplicates = {i for i in ids if ids.count(i) > 1}
    assert not duplicates, duplicates


def test_the_t0_layer_is_in_the_catalogue():
    theorems = [c for c in CATALOGUE if c.kind == "theorem"]
    assert len(theorems) == len(certified.lean_claims())
    assert all(c.tier == 0 and c.reproduce == "make lean" for c in theorems)
    decisions = [c for c in CATALOGUE if c.kind == "decision"]
    assert len(decisions) == len(list((ROOT / "docs" / "decisions").glob("*.md")))


def test_why_shows_both_sides_of_the_dispute():
    text, found = navigator.explain("C2", CATALOGUE, SYMBOLS, GRAPH)
    assert found
    assert "-211835444920651/4405310420659200" in text
    assert "-0.020213328886166577" in text
    assert "neither promoted" in text


def test_why_carries_the_retraction_with_the_gap():
    text, found = navigator.explain("G14", CATALOGUE, SYMBOLS, GRAPH)
    assert found
    assert "RETRACTED" in text
    assert "ADR:0005" in text


def test_why_resolves_forgiving_spellings():
    queries = (
        "adr 5",
        "ADR:0005",
        "c2",
        "newton_three",
        "q_band_4",
        "sym:c_shp",
        "lean:newton_three",
    )
    for query in queries:
        _text, found = navigator.explain(query, CATALOGUE, SYMBOLS, GRAPH)
        assert found, query


def test_why_points_a_miss_at_search():
    text, found = navigator.explain("zzzz-no-such-id", CATALOGUE, SYMBOLS, GRAPH)
    assert not found
    assert "workhouse search" in text


def test_cli_why_runs_and_exits_nonzero_on_a_miss():
    hit = subprocess.run(
        [sys.executable, "-m", "workhouse.cli", "why", "C2"],
        capture_output=True,
        text=True,
        cwd=ROOT,
    )
    assert hit.returncode == 0 and "neither promoted" in hit.stdout
    miss = subprocess.run(
        [sys.executable, "-m", "workhouse.cli", "why", "zzzz"],
        capture_output=True,
        text=True,
        cwd=ROOT,
    )
    assert miss.returncode == 1


def test_run_register_matches_runs_directory():
    """Every pinned run directory has a register entry and vice versa.

    The failure this prevents: a run record cited by checks only as a
    file-path string, invisible to `workhouse why` — or a register entry
    whose directory (or SHA256SUMS pin) quietly disappeared.
    """
    from workhouse import claims

    root = Path(claims.ROOT)
    registered = {run["id"]: run for run in claims.load_runs()}
    on_disk = {
        p.name
        for p in (root / "runs").iterdir()
        if p.is_dir()
    }
    assert set(registered) == on_disk, (
        f"register vs runs/: only in register {sorted(set(registered) - on_disk)}, "
        f"only on disk {sorted(on_disk - set(registered))}"
    )
    for rid, run in registered.items():
        rdir = root / run["dir"]
        assert rdir.is_dir(), f"{rid}: {run['dir']} is not a directory"
        assert (rdir / "SHA256SUMS").is_file(), f"{rid}: no SHA256SUMS pin"
        assert run.get("bears_on"), f"{rid}: a run with no bears_on is invisible"
