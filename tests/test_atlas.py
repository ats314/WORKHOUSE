"""The atlas is a faithful, self-contained view of the graph — never a new source."""

import re
from pathlib import Path

from workhouse import atlas
from workhouse import claims as C
from workhouse import graph as G

ROOT = Path(__file__).resolve().parents[1]
CATALOGUE = C.collect()
SYMBOLS = C.load_symbols()
GRAPH = G.build(CATALOGUE, SYMBOLS)
DATA = atlas.collect_data(CATALOGUE, SYMBOLS, GRAPH)
HTML = atlas.render(DATA)


def test_rendering_is_deterministic():
    assert atlas.render(DATA) == HTML


def test_the_view_matches_the_graph_exactly():
    """Every drawn node is a connected catalogue record; every edge is real."""
    connected = {e.src for e in GRAPH.edges} | {e.dst for e in GRAPH.edges}
    drawn = {n["id"] for n in DATA["nodes"]}
    assert drawn == connected
    assert len(DATA["edges"]) == len(GRAPH.edges)
    triples = {(e.src, e.dst, e.type) for e in GRAPH.edges}
    assert {(e["s"], e["d"], e["t"]) for e in DATA["edges"]} == triples


def test_the_dispute_stays_two_sided():
    """C2 renders both values and the never-promote marker, or not at all."""
    c2 = next(n for n in DATA["nodes"] if n["id"] == "C2")
    values = {s["value"] for s in c2["sides"]}
    assert "-211835444920651/4405310420659200" in values
    assert "-0.020213328886166577" in values
    assert "never promote" in HTML


def test_unifying_candidates_carry_their_falsifier():
    u3 = next(n for n in DATA["nodes"] if n["id"] == "U3")
    assert u3["falsifier"]


def test_self_contained_except_google_fonts():
    """The artifact CSP admits fonts.googleapis.com and nothing else external."""
    urls = set(re.findall(r"https?://[^\s\"'<>)]+", HTML))
    outside = {u for u in urls if not u.startswith("https://fonts.googleapis.com")}
    assert not outside, outside


def test_no_authored_prose_enters_the_page():
    """Node text is copied from records; the template carries no per-claim prose."""
    template = atlas.TEMPLATE.read_text()
    assert atlas.MARKER in template
    for needle in ("C_shp", "q_band", "tier collapse"):
        assert needle.lower() not in template.lower(), needle


def test_write_targets_a_path_outside_the_pinned_trees(tmp_path):
    out = atlas.write(tmp_path / "atlas.html", DATA)
    assert out.read_text() == HTML
    default = atlas.DEFAULT_OUT.resolve()
    for pinned in ("theory", "corpus-import", "settlement", "index"):
        assert (ROOT / pinned) not in default.parents
