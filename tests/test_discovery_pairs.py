"""Pair dossiers compare two located texts without touching the graph."""

import argparse
import hashlib
import json
import sqlite3
import sys
import types
from argparse import Namespace
from pathlib import Path

import pytest

import workhouse
from workhouse import discovery as D
from workhouse import discovery_pairs as P
from workhouse.discovery_index import tokenize

A_LINES = [
    "# Conditional score on the finite lattice",
    "",
    "Assume K_g(w) is finite on the compact SU(2) square with coupling g and normalized ground.",
    "Then K_g(w) <= C_0 + C_1 g^{-2} E(V|w) holds, with c_shp = 5/48.",
    "The constant beta_n = 1/2 fixes the convention (factor 2pi).",
    "See notes/imported/x/#-note (2).md for the Brascamp-Lieb input.",
    "Extra line seven about nothing.",
]
NOTE_PATH = "notes/imported/x/#-note (2).md"
NOTE_LINES = [
    "## Brascamp-Lieb variance bound",
    "",
    "Provided the Witten Laplacian on 1-forms has a gap, K_g(w) <= C_0 + C_1 g^{-2} E(V|w) "
    "holds in the thermodynamic limit for SU(N).",
    "Here c_shp = 7/102 under the other normalization and beta_n = 1/2.",
    "The conditional score variance is uniform in L.",
]
FILES = {
    "docs/derivations/a.md": "\r\n".join(A_LINES) + "\r\n",
    NOTE_PATH: "\n".join(NOTE_LINES) + "\n",
    "literature/lit.md": (
        "Published bound: the conditional score K_g(w) obeys a Hardy inequality with "
        "constant C_1 on any lattice.\nNo coupling assumption is made.\n"
    ),
    "theory/d.md": (
        "Assume the compact square is SU(2) with coupling g.\n"
        "Provided K_g(w) <= C_0 + C_1 W_g(w) holds, the tail bound follows on the compact square.\n"
    ),
    "theory/e.md": (
        "The conditional score variance bound uses the Hardy inequality and the Poincare "
        "estimate.\n"
    ),
    "theory/f1.md": "We construct the operator K_g(w) from C_0, C_1 and W_g(w) on the square.\n",
    "theory/f2.md": (
        "Define K_g(w) via C_0, C_1 and W_g(w); this representation is the same object.\n"
    ),
    "ledger/results.yaml": "- id: RESULT:B\n  statement: catalogue wording lives here\n",
}
RECORDS = [
    {
        "id": "DERIV:A",
        "kind": "result",
        "status": "open",
        "evidence": "prose-only",
        "tier": 3,
        "statement": "Prove K_g(w) <= C_0 + C_1 g^{-2} E(V|w) on the compact square.",
        "detail": "Hypotheses: SU(2) compact square with coupling g.\nScope: finite lattice.",
        "where": "docs/derivations/a.md (### Section (lines 3-5))",
    },
    {
        "id": "RESULT:B",
        "kind": "result",
        "status": "proven",
        "evidence": "analytic",
        "tier": 3,
        "statement": "K_g(w) <= C_0 + C_1 g^{-2} E(V|w) on the compact square.",
        "detail": "Hypotheses: Assume SU(2) with coupling g.\nScope: compact square.",
        "where": "ledger/results.yaml#RESULT:B",
    },
    {
        "id": "LIT:C",
        "kind": "paper",
        "statement": "a published bound",
        "where": "literature/lit.md",
    },
    {
        "id": "CITE:DOC",
        "kind": "document",
        "statement": "source a",
        "where": "docs/derivations/a.md",
    },
]
EDGES = [
    {
        "src": "RESULT:B",
        "dst": "DERIV:A",
        "type": "depends_on",
        "how": "curated",
        "source": "ledger/results.yaml",
    },
    {
        "src": "DERIV:A",
        "dst": "CITE:DOC",
        "type": "cites",
        "how": "derived",
        "source": "ledger/derivation_statements.yaml",
    },
]


def _sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def _json(value) -> str:
    return json.dumps(value, sort_keys=True, ensure_ascii=True, separators=(",", ":"))


class MemoryIndex:
    """A built cache: chunks table with passages and records, optional FTS."""

    def __init__(self, root, cache_dir=None, **_options):
        self.root = Path(root)
        self.records = RECORDS
        self.edges = EDGES
        self.symbols = []
        self._connection = sqlite3.connect(":memory:")
        self._connection.execute(
            "CREATE TABLE chunks(rowid INTEGER PRIMARY KEY, id TEXT UNIQUE NOT NULL, "
            "data TEXT NOT NULL)"
        )
        try:
            self._connection.execute("CREATE VIRTUAL TABLE search USING fts5(terms, title_terms)")
            self.fts = True
        except sqlite3.OperationalError:
            self.fts = False
        for rowid, row in enumerate(self._chunks(), 1):
            self._connection.execute(
                "INSERT INTO chunks VALUES(?,?,?)", (rowid, row["id"], _json(row))
            )
            if self.fts:
                terms = " ".join("x" + t.encode().hex() for t in tokenize(row["text"]))
                self._connection.execute(
                    "INSERT INTO search(rowid,terms,title_terms) VALUES(?,?,?)", (rowid, terms, "")
                )
        self._connection.commit()

    def _chunks(self):
        def passage(id_, path, first, last, claim_spans):
            text = (self.root / path).read_bytes().decode("utf-8")
            return {
                "id": id_,
                "kind": "passage",
                "path": path,
                "start_line": first,
                "end_line": last,
                "text": text,
                "source_sha256": _sha(self.root / path),
                "claim_ids": sorted(claim_spans),
                "claim_spans": claim_spans,
            }

        yield passage(
            "PASSAGE:a1",
            "docs/derivations/a.md",
            1,
            7,
            {
                "CITE:DOC": {"start_line": 1, "end_line": 7, "scope": "source_document"},
                "DERIV:A": {"start_line": 3, "end_line": 5, "scope": "registered_lines"},
            },
        )
        yield passage("PASSAGE:notes1", NOTE_PATH, 1, 5, {})
        yield passage(
            "PASSAGE:lit1",
            "literature/lit.md",
            1,
            2,
            {"LIT:C": {"start_line": 1, "end_line": 2, "scope": "source_document"}},
        )
        yield {
            "id": "DERIV:A",
            "kind": "record",
            "path": "index/claims.jsonl",
            "start_line": 1,
            "end_line": 1,
            "text": _json(RECORDS[0]),
            "source_sha256": "0" * 64,
            "claim_ids": ["DERIV:A"],
        }

    def build(self):
        return self.metadata()

    def metadata(self, **_):
        return {"fingerprint": "test-snapshot", "freshness": "matched"}

    def search(self, query, limit=100):
        return []

    def close(self):
        self._connection.close()


@pytest.fixture
def root(tmp_path):
    base = tmp_path / "repo"
    for relative, text in FILES.items():
        path = base / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text, encoding="utf-8", newline="")
    return base


@pytest.fixture
def engine(monkeypatch, root):
    monkeypatch.setattr(D, "DiscoveryIndex", MemoryIndex)
    with D.DiscoveryEngine(root) as instance:
        yield instance


def _snapshot(root: Path) -> dict:
    return {p.relative_to(root).as_posix(): _sha(p) for p in root.rglob("*") if p.is_file()}


# --- endpoint resolution --------------------------------------------------


def test_record_endpoint_locates_registered_lines_and_hashes(engine, root):
    endpoint = P.resolve_endpoint(engine, "DERIV:A")
    assert endpoint["kind"] == "record" and endpoint["family"] == "derivations"
    source = endpoint["source"]
    assert source["path"] == "docs/derivations/a.md"
    assert source["lines"] == [3, 5]
    assert source["sha256"] == _sha(root / "docs/derivations/a.md")
    assert source["index_sha256_match"] is True
    assert endpoint["text_scope"] == "registered source lines"
    assert endpoint["_text"].splitlines() == A_LINES[2:5]
    assert endpoint["record"]["hypotheses"].startswith("SU(2)")
    assert endpoint["record"]["scope"] == "finite lattice."
    assert endpoint["record"]["status"] == "open" and endpoint["record"]["tier"] == 3


def test_catalogue_record_keeps_statement_text_not_the_ledger_file(engine):
    endpoint = P.resolve_endpoint(engine, "RESULT:B")
    assert endpoint["family"] == "catalogue"
    assert endpoint["source"]["available"] is True
    assert endpoint["source"]["lines"] is None
    assert "catalogue" in endpoint["text_scope"]
    assert "K_g(w)" in endpoint["_text"] and "Assume SU(2)" in endpoint["_text"]


def test_document_record_uses_the_whole_source(engine):
    endpoint = P.resolve_endpoint(engine, "CITE:DOC")
    assert endpoint["source"]["lines"] == [1, 7]
    assert endpoint["text_scope"].startswith("whole source document")
    assert endpoint["_text"].splitlines() == A_LINES


@pytest.mark.parametrize(
    "spec, path, first, last, external",
    [
        ("notes/imported/x/#-note (2).md:2-3", NOTE_PATH, 2, 3, None),
        ("docs/derivations/a.md:4", "docs/derivations/a.md", 4, 4, None),
        ("docs\\derivations\\a.md:4-6", "docs/derivations/a.md", 4, 6, None),
        ("ext:archive/dir/f.md:1-2", "dir/f.md", 1, 2, "archive"),
    ],
)
def test_locator_parsing(spec, path, first, last, external):
    assert P.parse_locator(spec) == {
        "path": path,
        "first": first,
        "last": last,
        "external": external,
    }


@pytest.mark.parametrize(
    "spec",
    [
        "C:/abs/x.md:1",
        "/x.md:1",
        "../x.md:1",
        "a/../x.md:1",
        "x.md:0",
        "x.md:5-2",
        "DERIV:NOPE",
        "ext:/x.md:1",
    ],
)
def test_locator_parsing_rejects(spec):
    with pytest.raises(ValueError):
        P.parse_locator(spec)


@pytest.mark.parametrize(
    "where, path, bounds",
    [
        (
            "docs/derivations/a.md (### M.4. The inequality (lines 473-495))",
            "docs/derivations/a.md",
            (473, 495),
        ),
        ("ledger/results.yaml#RESULT:X", "ledger/results.yaml", None),
        (
            "corpus-import/records/#-Final-unified-theory.txt",
            "corpus-import/records/#-Final-unified-theory.txt",
            None,
        ),
        ("corpus/STATUS (2).md", "corpus/STATUS (2).md", None),
        ("src/workhouse/x.py:22", "src/workhouse/x.py", (22, 22)),
        ("RESEARCH_2026-08/guide.md", "RESEARCH_2026-08/guide.md", None),
    ],
)
def test_parse_where(where, path, bounds):
    assert P.parse_where(where) == (path, bounds)


def test_locator_endpoint_reads_lines_and_maps_overlapping_claims(engine, root):
    endpoint = P.resolve_endpoint(engine, "docs/derivations/a.md:3-4")
    assert endpoint["kind"] == "passage" and endpoint["id"] is None
    assert endpoint["_text"].splitlines() == A_LINES[2:4]
    assert endpoint["source"]["sha256"] == _sha(root / "docs/derivations/a.md")
    assert endpoint["source"]["index_sha256_match"] is True
    assert endpoint["claim_ids"] == ["CITE:DOC", "DERIV:A"]
    outside = P.resolve_endpoint(engine, "docs/derivations/a.md:6-7")
    assert outside["claim_ids"] == ["CITE:DOC"]
    with pytest.raises(ValueError, match="exceeds"):
        P.resolve_endpoint(engine, "docs/derivations/a.md:6-40")


def test_hash_in_filename_is_a_filename(engine, root):
    endpoint = P.resolve_endpoint(engine, NOTE_PATH + ":3-4")
    assert endpoint["family"] == "notes"
    assert endpoint["source"]["sha256"] == _sha(root / NOTE_PATH)
    assert endpoint["_text"].splitlines() == NOTE_LINES[2:4]


def test_passage_id_resolves_through_the_cache(engine):
    endpoint = P.resolve_endpoint(engine, "PASSAGE:notes1")
    assert endpoint["kind"] == "passage"
    assert endpoint["locator"] == NOTE_PATH + ":1-5"
    assert endpoint["source"]["on_disk_sha256_match"] is True
    assert endpoint["_text"].splitlines() == NOTE_LINES
    with pytest.raises(ValueError, match="PASSAGE"):
        P.resolve_endpoint(engine, "PASSAGE:missing")
    with pytest.raises(ValueError, match="PASSAGE"):
        P.resolve_endpoint(engine, "PASSAGE:a1x")


def test_external_locator_without_mounted_root_is_unavailable_not_an_error(engine):
    result = P.pair(engine, "DERIV:A", "ext:archive/dir/f.md:1-2")
    b = result["b"]
    assert b["family"] == "external:archive"
    assert b["source"]["available"] is False
    assert "archive" in b["source"]["reason"]
    assert b["excerpt"]["text"] == ""
    assert result["proposal"]["kind"] == "unrelated"


def test_external_locator_reads_a_mounted_root(engine, tmp_path):
    external = tmp_path / "archive"
    (external / "dir").mkdir(parents=True)
    target = external / "dir" / "f.md"
    target.write_text("K_g(w) bound in the external note under SU(2).\nsecond\n", encoding="utf-8")
    engine.index.external_roots = {"archive": external}
    endpoint = P.resolve_endpoint(engine, "ext:archive/dir/f.md:1-1")
    assert endpoint["source"]["available"] is True
    assert endpoint["source"]["sha256"] == _sha(target)
    assert endpoint["source"]["path"] == "ext:archive/dir/f.md"
    assert endpoint["_text"].startswith("K_g(w)")


def test_external_root_from_declared_scope(engine, tmp_path):
    base = tmp_path / "workstation"
    (base / "notes").mkdir(parents=True)
    (base / "notes" / "n.md").write_text("one\n", encoding="utf-8")
    root = types.SimpleNamespace(label="ws", path="notes", enabled=True)
    engine.index.scope = types.SimpleNamespace(base=base, enabled_roots=(root,))
    assert P._external_root(engine, "ws") == base / "notes"
    assert P._external_root(engine, "other") is None


def test_unknown_endpoint_is_an_error(engine):
    with pytest.raises(ValueError, match="not a record id"):
        P.resolve_endpoint(engine, "DERIV:MISSING")


# --- shared tokens, markers, conflicts -------------------------------------


@pytest.mark.parametrize(
    "text, token, values",
    [
        ("c_0 = 3/6 and later C_{0}=1/2", "c_0", {"1/2"}),
        ("\\beta_{n} = 3 while beta_n=3", "beta_n", {"3"}),
        ("0<g<g_* and g^2", "g", set()),
        ("g = 0.5 &= 7", "g", {"0.5"}),
        ("K_g(w) <= 4", "k_g", set()),
    ],
)
def test_stated_values(text, token, values):
    assert P.stated_values(P._normalized(text), token) == values


def test_clean_tokens_drops_latex_stubs():
    assert P.clean_tokens(tokenize("g^{-2} C_{0} K_g(w) alpha'")) == [
        "g",
        "-2",
        "c",
        "0",
        "k_g",
        "w",
        "alpha",
    ]


def test_shared_tokens_separate_symbols_single_letters_and_ranked_terms(engine):
    result = P.pair(engine, "DERIV:A", NOTE_PATH + ":1-5")
    shared = result["shared"]
    assert {"k_g", "c_0", "c_1", "c_shp", "beta_n"} <= set(shared["symbols"])
    assert "1/2" in shared["rationals"] and "5/48" not in shared["rationals"]
    assert "g" in shared["single_letters"] and "g" not in shared["symbols"]
    assert shared["term_ranking"].endswith("frequency, ascending")
    assert all(term in shared["term_counts"] for term in shared["terms"])
    lexicon = shared["lexicon"]
    assert lexicon["available"] is False and "not present" in lexicon["reason"]


def test_markers_regime_rank_coupling_cues_and_normalization(engine):
    result = P.pair(engine, "DERIV:A", NOTE_PATH + ":1-5")
    a, b = result["markers"]["a"], result["markers"]["b"]
    assert a["regime"] == ["finite lattice"] and a["rank"] == ["SU(2)"]
    assert b["regime"] == ["infinite volume/thermodynamic limit"] and b["rank"] == ["SU(N)"]
    assert "g" in a["coupling"] and "g" in b["coupling"] and "L=" not in b["coupling"]
    assert {"convention", "factor", "1/2", "2pi", "normalized"} <= set(a["normalization"])
    assert [c["line"] for c in a["hypothesis_cues"] if c.get("line")] == [3]
    assert a["hypothesis_cues"][0]["symbols"] == ["k_g"]
    assert b["hypothesis_cues"][0]["symbols"] == ["c_0", "c_1", "k_g"]
    assert [(c["line"], c["cue"]) for c in b["hypothesis_cues"]] == [
        (3, "provided"),
        (4, "under"),
        (5, "uniform in"),
    ]
    assert result["a"]["excerpt"]["lines"] == [3, 5]
    assert result["b"]["excerpt"]["lines"] == [1, 5]


def test_excerpt_window_is_chosen_by_the_other_endpoints_terms(engine):
    result = P.pair(engine, "DERIV:A", NOTE_PATH + ":1-5", excerpt_chars=150)
    window = result["b"]["excerpt"]
    assert window["truncated"] is True
    assert 1 <= window["lines"][0] <= window["lines"][1] <= 5
    assert "K_g(w)" in window["text"] or "c_shp" in window["text"]
    with pytest.raises(ValueError):
        P.pair(engine, "DERIV:A", NOTE_PATH + ":1-5", excerpt_chars=10)


# --- kind rules -------------------------------------------------------------


def test_rule_disagreement_from_stated_values(engine):
    result = P.pair(engine, "DERIV:A", NOTE_PATH + ":1-5")
    proposal = result["proposal"]
    assert proposal["kind"] == "disagreement" and proposal["rule"] == 3
    assert proposal["confidence"] == "medium"
    conflict = result["value_conflicts"][0]
    assert (conflict["carrier"], conflict["a"], conflict["b"]) == ("c_shp", ["5/48"], ["7/102"])
    assert "c_shp" in proposal["check_next"][0]
    assert "no new C-ids" in proposal["check_next"][-1]
    assert "never a new C-id" in proposal["registrable_as"]


def test_rule_documentary_from_a_citation(engine):
    result = P.pair(engine, "docs/derivations/a.md:6-7", NOTE_PATH + ":1-2")
    assert result["citations"] == [{"in": "a", "cites": "#-note (2).md"}]
    assert result["proposal"]["kind"] == "documentary" and result["proposal"]["rule"] == 2


def test_rule_documentary_from_registered_citation_edge(engine):
    result = P.pair(engine, "DERIV:A", "CITE:DOC")
    assert [e["type"] for e in result["graph"]["existing_relations"]] == ["cites"]
    assert result["proposal"]["kind"] == "documentary"


def test_rule_literature_bearing(engine):
    result = P.pair(engine, "LIT:C", "DERIV:A")
    assert result["a"]["family"] == "literature"
    assert result["proposal"]["kind"] == "literature-bearing" and result["proposal"]["rule"] == 4
    assert "literature/index.yaml" in result["proposal"]["registrable_as"]


def test_rule_scope_restriction(engine):
    result = P.pair(engine, "docs/derivations/a.md:3-4", NOTE_PATH + ":3-3")
    proposal = result["proposal"]
    assert proposal["kind"] == "scope-restriction" and proposal["rule"] == 5
    assert "SU(2)" in proposal["check_next"][0] and "SU(N)" in proposal["check_next"][0]
    assert "thermodynamic limit" in proposal["check_next"][0]


def test_rule_compatible_hypothesis(engine):
    result = P.pair(engine, "docs/derivations/a.md:3-4", "theory/d.md:1-2")
    proposal = result["proposal"]
    assert proposal["kind"] == "compatible-hypothesis" and proposal["rule"] == 7
    assert "k_g" in proposal["reasons"][-1]
    assert "A line 3 and B line 2" in proposal["check_next"][0]


def test_rule_shared_operator(engine):
    result = P.pair(engine, "docs/derivations/a.md:4-4", "theory/d.md:2-2")
    proposal = result["proposal"]
    assert proposal["kind"] == "shared-operator" and proposal["rule"] == 8
    assert proposal["confidence"] == "low"
    assert "normalization of" in proposal["check_next"][0]


def test_rule_reusable_ingredient(engine):
    result = P.pair(engine, "theory/e.md:1-1", NOTE_PATH + ":5-5")
    assert result["shared"]["symbols"] == []
    assert result["proposal"]["kind"] == "reusable-ingredient" and result["proposal"]["rule"] == 9


def test_rule_unrelated(engine):
    result = P.pair(engine, "theory/e.md:1-1", "docs/derivations/a.md:7-7")
    proposal = result["proposal"]
    assert proposal["kind"] == "unrelated" and proposal["rule"] == 1
    assert proposal["confidence"] == "low"
    assert proposal["check_next"][-1] == "Do not register anything from this pair."


def test_rule_equivalent_construction(engine):
    result = P.pair(engine, "theory/f1.md:1-1", "theory/f2.md:1-1")
    proposal = result["proposal"]
    assert proposal["kind"] == "equivalent-construction" and proposal["rule"] == 6
    assert result["shared"]["symbol_jaccard"] == 1.0
    assert "falsifier" in proposal["check_next"][1]


def test_record_pair_reports_registered_edge_and_dependency_path(engine):
    result = P.pair(engine, "RESULT:B", "DERIV:A")
    graph = result["graph"]
    assert graph["mode"] == "record-record"
    assert [e["type"] for e in graph["existing_relations"]] == ["depends_on"]
    assert graph["dependency_path"]["a_to_b"]["found"] is True
    assert graph["dependency_path"]["b_to_a"]["found"] is False
    assert graph["exploratory_path"]["found"] is True
    assert graph["exploratory_path"]["steps"][0].startswith("RESULT:B ->[depends_on curated]")
    proposal = result["proposal"]
    assert proposal["kind"] == "shared-operator"
    assert proposal["confidence"] == "medium"
    assert proposal["reasons"][0] == "registered relation(s): depends_on"
    assert "path" in result["commands"] and "why_b" in result["commands"]


def test_passage_maps_to_record_is_reported(engine):
    result = P.pair(engine, "DERIV:A", "docs/derivations/a.md:3-5")
    assert result["graph"]["mode"] == "record-passage"
    assert result["graph"]["passage_maps_to_record"] == "b maps to a"
    assert result["graph"]["shared_claim_ids"] == ["DERIV:A"]


def test_confidence_never_high(engine):
    for pair in [("DERIV:A", NOTE_PATH + ":1-5"), ("RESULT:B", "DERIV:A"), ("LIT:C", "DERIV:A")]:
        assert P.pair(engine, *pair)["proposal"]["confidence"] in P.CONFIDENCE
    assert "high" not in P.CONFIDENCE


# --- lexicon (optional, foreign module) -------------------------------------


def _lexicon_file(root):
    path = root / P.LEXICON_PATH
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("concepts: []\n", encoding="utf-8")


def test_lexicon_module_absent_is_reported_not_guessed(engine, root, monkeypatch):
    _lexicon_file(root)
    monkeypatch.setitem(sys.modules, "workhouse.discovery_lexicon", None)
    monkeypatch.delattr(workhouse, "discovery_lexicon", raising=False)
    lexicon = P.pair(engine, "DERIV:A", NOTE_PATH + ":1-5")["shared"]["lexicon"]
    assert lexicon == {
        "available": False,
        "reason": "discovery_lexicon not importable",
        "concepts": [],
    }


def test_lexicon_concepts_matched_in_both_texts(engine, root, monkeypatch):
    _lexicon_file(root)
    fake = types.SimpleNamespace(
        load_lexicon=lambda path: [
            {"id": "conditional-score", "variants": ["conditional score", "K_g"]},
            {"id": "brascamp-lieb", "variants": ["Brascamp-Lieb"]},
            {"id": "absent", "variants": ["zzz"]},
        ]
    )
    monkeypatch.setitem(sys.modules, "workhouse.discovery_lexicon", fake)
    monkeypatch.setattr(workhouse, "discovery_lexicon", fake, raising=False)
    lexicon = P.pair(engine, "DERIV:A", NOTE_PATH + ":1-5")["shared"]["lexicon"]
    assert lexicon["available"] is True
    assert [c["concept"] for c in lexicon["concepts"]] == ["conditional-score"]
    assert lexicon["concepts"][0]["a"] == ["K_g"]


# --- rendering, CLI and safety --------------------------------------------


def test_render_shows_both_excerpts_markers_and_checks(engine):
    result = P.pair(engine, "DERIV:A", NOTE_PATH + ":1-5")
    text = P.render_pair(result)
    assert "A excerpt lines 3-5" in text and "B excerpt lines 1-5" in text
    assert " | " in text  # side by side
    assert "proposal: disagreement" in text
    assert "check next:" in text and "review_add:" in text
    assert "--seed 'DERIV:A' --target" in text
    assert "finite lattice" in text and "SU(N)" in text
    assert result["meaning"] == P.MEANING and text.splitlines()[1] == P.MEANING


def test_cli_run_writes_once_and_prints_json_or_text(engine, tmp_path, capsys):
    out = tmp_path / "pair.json"
    args = Namespace(
        a="DERIV:A", b=NOTE_PATH + ":1-5", json=False, out=str(out), excerpt_chars=None
    )
    assert P.run(args, lambda: engine) == 0
    printed = capsys.readouterr().out
    assert "pair dossier" in printed
    saved = json.loads(out.read_text(encoding="utf-8"))
    assert saved["schema"] == P.SCHEMA and saved["proposal"]["kind"] == "disagreement"
    assert saved["execution"] == {
        "python_checks": 0,
        "lean": False,
        "scientific_index_written": False,
    }
    original = out.read_bytes()
    args.json = True
    assert P.run(args, lambda: engine) == 1
    assert "error" in json.loads(capsys.readouterr().out)
    assert out.read_bytes() == original
    args.out = None
    assert P.run(args, lambda: engine) == 0
    assert json.loads(capsys.readouterr().out)["schema"] == P.SCHEMA


def test_cli_unknown_endpoint_is_a_structured_failure(engine, capsys):
    args = Namespace(a="DERIV:A", b="nothing-here", json=True, out=None, excerpt_chars=300)
    assert P.run(args, lambda: engine) == 1
    assert "not a record id" in json.loads(capsys.readouterr().out)["error"]


def test_add_parser_registers_pair():
    parser = argparse.ArgumentParser()
    sub = parser.add_subparsers(dest="discovery_command")
    P.add_parser(sub)
    args = parser.parse_args(
        ["pair", "X", "y.md:1-2", "--json", "--excerpt-chars", "300", "--out", "o.json"]
    )
    assert (args.a, args.b, args.json, args.excerpt_chars, args.out) == (
        "X",
        "y.md:1-2",
        True,
        300,
        "o.json",
    )
    assert parser.parse_args(["pair", "X", "Y"]).excerpt_chars == P.PAIR_EXCERPT_CHARS


def test_dossier_writes_nothing_and_leaves_records_untouched(engine, root):
    before = _snapshot(root)
    records = json.dumps(engine.index.records, sort_keys=True)
    for pair in [("DERIV:A", NOTE_PATH + ":1-5"), ("RESULT:B", "DERIV:A"), ("LIT:C", "CITE:DOC")]:
        result = P.pair(engine, *pair)
        assert result["proposal"]["kind"] in P.KINDS
        assert result["a"]["record"].get("status") == RECORDS_BY_ID[pair[0]].get("status")
    assert _snapshot(root) == before
    assert json.dumps(engine.index.records, sort_keys=True) == records


RECORDS_BY_ID = {row["id"]: row for row in RECORDS}


def test_terms_rank_by_corpus_rarity_when_fts_is_available(engine):
    if not engine.index.fts:
        pytest.skip("sqlite without fts5")
    shared = P.pair(engine, "theory/e.md:1-1", NOTE_PATH + ":5-5")["shared"]
    assert shared["term_ranking"] == "corpus chunk frequency, ascending"
    assert shared["terms"][0] == "variance"
    assert shared["term_counts"]["variance"]["corpus"] == 1


def test_lexicon_real_contract_load_root_and_matches(engine, root, monkeypatch):
    _lexicon_file(root)
    calls = {}

    def load(path, root=None, *, check_citations=True):
        calls["root"] = root
        return {
            "entries": [
                {"concept": "conditional-score", "variants": [{"text": "K_g", "family": "notes"}]},
                {"concept": "absent", "variants": [{"text": "zzz", "family": "notes"}]},
            ],
            "fingerprint": "abc",
        }

    def matches(query, lexicon):
        present = set(tokenize(query))
        return [
            {"concept": entry["concept"], "text": variant["text"], "family": variant["family"]}
            for entry in lexicon["entries"]
            for variant in entry["variants"]
            if set(tokenize(variant["text"])) <= present
        ]

    fake = types.SimpleNamespace(load=load, matches=matches)
    monkeypatch.setitem(sys.modules, "workhouse.discovery_lexicon", fake)
    monkeypatch.setattr(workhouse, "discovery_lexicon", fake, raising=False)
    lexicon = P.pair(engine, "DERIV:A", NOTE_PATH + ":1-5")["shared"]["lexicon"]
    assert calls["root"] == engine.root
    assert lexicon["available"] is True and lexicon["fingerprint"] == "abc"
    assert lexicon["concepts"] == [{"concept": "conditional-score", "a": ["K_g"], "b": ["K_g"]}]
    assert lexicon["method"].startswith("discovery_lexicon.matches")


def test_lexicon_load_failure_is_reported_not_raised(engine, root, monkeypatch):
    _lexicon_file(root)

    def load(path, root=None, **_):
        raise ValueError("lexicon invalid: bad citation")

    fake = types.SimpleNamespace(load=load)
    monkeypatch.setitem(sys.modules, "workhouse.discovery_lexicon", fake)
    monkeypatch.setattr(workhouse, "discovery_lexicon", fake, raising=False)
    lexicon = P.pair(engine, "DERIV:A", NOTE_PATH + ":1-5")["shared"]["lexicon"]
    assert lexicon["available"] is False and "bad citation" in lexicon["reason"]
