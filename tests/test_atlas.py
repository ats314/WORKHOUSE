"""The atlas is a faithful, self-contained view of the graph — never a new source."""

import json
import re
import shutil
import subprocess
from pathlib import Path

import pytest

from workhouse import atlas
from workhouse import claims as C
from workhouse import graph as G

ROOT = Path(__file__).resolve().parents[1]
if not C.CLAIMS.is_file():
    raise FileNotFoundError("Missing checked-in catalogue; run `make catalogue` before testing")
CATALOGUE = C.load_catalogue()
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
    assert all(e["p"] for e in DATA["edges"]), "the atlas must retain each edge source"


def test_the_dispute_stays_two_sided():
    """C2 renders both values and the never-promote marker, or not at all."""
    c2 = next(n for n in DATA["nodes"] if n["id"] == "C2")
    values = {s["value"] for s in c2["sides"]}
    assert "-211835444920651/4405310420659200" in values
    assert "-0.020213328886166577" in values
    assert "never promote" in HTML


def test_the_dispute_is_branchwise_and_keeps_originators():
    c2 = next(n for n in DATA["nodes"] if n["id"] == "C2")
    historical = next(s for s in c2["sides"] if s["label"] == "historical")
    current = next(s for s in c2["sides"] if s["label"] == "v10a.26")
    assert {m["id"] for m in historical["matches"]} >= {"CONST:C_shp (historical)"}
    assert {m["id"] for m in current["matches"]} >= {"CONST:C_SHP_NEW_NUM"}
    assert "DOC:kernel-historical-189" in historical["originators"]
    assert "DOC:nb-hodge-v10a26-alt2" in current["originators"]
    # Resolved 2026-09-04 (ADR 0024): the detail is now the resolution.
    assert "C_SHP_HISTORICAL + 25/1024" in c2["detail"]


def test_unifying_candidates_carry_their_falsifier():
    u3 = next(n for n in DATA["nodes"] if n["id"] == "U3")
    assert u3["falsifier"]


def test_self_contained_except_google_fonts():
    """The page depends only on Google Fonts; citation URLs are inert node data.

    Institutional sources can have URL identifiers instead of DOI/arXiv strings.
    Those identifiers must survive in the graph without being mistaken for a
    script, style, font, or other resource that the atlas fetches to render.
    The template contains all page code and resource references; the renderer
    only substitutes the separately tested graph data into its marker.
    """
    template = atlas.TEMPLATE.read_text(encoding="utf-8")
    urls = set(re.findall(r"https?://[^\s\"'<>)]+", template))
    outside = {u for u in urls if not u.startswith("https://fonts.googleapis.com")}
    assert not outside, outside


def test_no_authored_prose_enters_the_page():
    """Node text is copied from records; the template carries no per-claim prose."""
    template = atlas.TEMPLATE.read_text(encoding="utf-8")
    assert atlas.MARKER in template
    for needle in ("C_shp", "q_band", "tier collapse"):
        assert needle.lower() not in template.lower(), needle


def test_write_targets_a_path_outside_the_pinned_trees(tmp_path):
    out = atlas.write(tmp_path / "atlas.html", DATA)
    assert out.read_text(encoding="utf-8") == HTML
    default = atlas.DEFAULT_OUT.resolve()
    for pinned in ("theory", "corpus-import", "settlement", "index"):
        assert (ROOT / pinned) not in default.parents


def test_full_graph_layout_uses_spatial_hashing_and_notes_are_opt_in():
    template = atlas.TEMPLATE.read_text(encoding="utf-8")
    assert "Spatial hashing" in template
    assert "for (let j = i + 1" not in template
    assert '["note", "notes & archives", "--k-note", false]' in template


def test_study_notes_are_visible_with_theory_while_archive_notes_stay_opt_in():
    """Exercise the actual browser classifier; a T3 study must not vanish by default."""
    node = shutil.which("node")
    if node is None:
        pytest.skip("Node.js is unavailable for the atlas selector regression")
    template = atlas.TEMPLATE.read_text(encoding="utf-8")
    selector = template.split("const GROUP_OF = ", 1)[1].split("const nodes = ", 1)[0]
    script = (
        "const GROUP_OF = "
        + selector
        + """
const enabled = new Set(GROUPS.filter(row => row[3]).map(row => row[0]));
const cases = [['note', 'STUDY:YM:target'], ['note', 'NOTE:archive:old'],
               ['archive', 'ARCHIVE:old'], ['gap', 'G19']];
console.log(JSON.stringify(cases.map(([kind, id]) => {
  const group = GROUP_OF(kind, id); return [group, enabled.has(group)];
})));
"""
    )
    result = subprocess.run([node, "-e", script], capture_output=True, text=True, check=True)
    assert json.loads(result.stdout) == [
        ["theory", True],
        ["note", False],
        ["note", False],
        ["theory", True],
    ]
    assert "GROUP_OF(n.kind, n.id)" in template
