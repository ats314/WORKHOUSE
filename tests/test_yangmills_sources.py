"""The seed bibliography is complete and its acquired versions remain identifiable."""

import hashlib
import json
from pathlib import Path

from workhouse import literature, study_graph

ROOT = Path(__file__).resolve().parents[1]
DIRECTORY = ROOT / "literature/yangmills"


def references():
    return sum(
        [
            json.loads((DIRECTORY / name).read_text(encoding="utf-8"))
            for name in ("sources_01_25.json", "sources_26_50.json")
        ],
        [],
    )


def test_every_seed_reference_and_bundled_work_is_represented():
    refs = references()
    assert sorted(r["number"] for r in refs) == list(range(1, 51))
    works = [w for r in refs for w in r["works"]]
    assert len(works) == len({w["id"] for w in works}) == 61
    assert all(r["raw_citation"] and r["works"] for r in refs)
    mapping = json.loads((DIRECTORY / "reference_map.json").read_text())
    seed_map = [m for m in mapping if m["reference"] is not None]
    assert {m["source_id"] for m in seed_map} == {w["id"] for w in works}
    lit = literature.load()
    assert {m["paper_id"] for m in seed_map} == set(lit.entry("JW_2006")["cites"])
    assert all(m["paper_id"] in lit.ids for m in mapping)


def test_acquisition_is_not_silently_equated_with_a_complete_reading():
    works = [w for r in references() for w in r["works"]]
    for work in works:
        assert work["metadata_status"] and work["access_status"]
        assert work["scope_note"] and work["evidence_locators"]
        assert work["verified_urls"]
        if not work.get("local_path"):
            assert work["access_limitation"]
        if "preview" in work["access_status"]:
            assert literature.load().entry(work["id"]).get("source_sha256") is None


def test_local_reading_copies_match_their_recorded_versions_when_present():
    works = [w for r in references() for w in r["works"]]
    works.extend(json.loads((DIRECTORY / "sources_related.json").read_text()))
    for work in works:
        if not work.get("local_path"):
            continue
        path = ROOT / work["local_path"]
        # Copyrighted reading copies are deliberately absent from clean clones.
        if path.exists():
            assert path.read_bytes().startswith(b"%PDF"), work["id"]
            assert hashlib.sha256(path.read_bytes()).hexdigest() == work["sha256"]


def test_methodological_nodes_keep_the_physical_operator_and_limit_obligations():
    nodes = {n["id"]: n for s in study_graph.load() for n in s.nodes}
    required = [
        "physical-gap",
        "operator-identification",
        "sector-completeness",
        "uniform-curvature",
        "volume-control",
        "uv-control",
        "matrix-commutator-model",
    ]
    assert all("STUDY:YM:" + suffix in nodes for suffix in required)
    matrix = nodes["STUDY:YM:matrix-commutator-model"]
    assert matrix["sources"][0]["paper"] == "SIMON_1983_DISCRETE"
    assert any(
        link["type"] == "cannot_decide" and link["target"] == "G19" for link in matrix["links"]
    )
    assert study_graph.validate() == []


def test_page_extraction_accounts_for_every_source_and_page_without_inventing_fulltext():
    directory = DIRECTORY / "extraction"
    sources = json.loads((directory / "sources.json").read_text(encoding="utf-8"))
    pages = [
        json.loads(line)
        for line in (directory / "pages.jsonl").read_text(encoding="utf-8").splitlines()
    ]
    assert len(sources) == len({s["source_id"] for s in sources}) == 65
    for source in sources:
        found = [p for p in pages if p["source_id"] == source["source_id"]]
        assert [p["pdf_page"] for p in found] == list(range(1, source["pages"] + 1))
        if not source["pages"]:
            assert source["extraction_status"] == "no local full text"
            continue
        assert all(p["source_sha256"] == source["source_sha256"] for p in found)
        assert all(p["paper_id"] == source["paper_id"] for p in found)
        assert all("locator candidates only" in p["status"] for p in found)
        pdf = ROOT / source["source_pdf"]
        if pdf.exists():
            assert hashlib.sha256(pdf.read_bytes()).hexdigest() == source["source_sha256"]
    summary = json.loads((directory / "summary.json").read_text(encoding="utf-8"))
    assert len(pages) == summary["pages"]
    assert sum(s["pages"] for s in sources) == len(pages)
    assert sum(p["text_characters"] < 80 for p in pages) == summary["low_text_pages"]
