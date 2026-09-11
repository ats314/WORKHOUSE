"""The concept lexicon: cited variants only, deterministic expansion, editable plans."""

from __future__ import annotations

import copy
import json
import random
from argparse import ArgumentParser, Namespace
from pathlib import Path

import pytest
import yaml

from workhouse import discovery_lexicon as L

SOURCES = {
    "docs/derivations/w6.md": (
        "# W6 tail control\n"
        "The conditional score variance is bounded on rare fibers.\n"
        "A Hardy tail-resistance constant closes the argument.\n"
        "Selected inverse estimates hold uniform in volume.\n"
    ),
    "notes/imported/EX/ex-014.md": (
        "Brascamp-Lieb gives Var(f) <= E[grad f C^-1 grad f].\n"
        "The Fisher term is the extra covariance under Wilsonian blocking.\n"
        "A Combes-Thomas block inverse decays exponentially.\n"
    ),
    "corpus-import/programs/pmbsf/lemma_q.md": (
        "Lemma Q is a conditional rare-source factorization.\n"
        "The Källén–Lehmann spectral representation has a delta atom.\n"
    ),
    "literature/index.yaml": "  detail: the analytic Hardy inequality supplies the tail\n",
    "paper/research_notes/g19.md": "Conditional Poincare inequality on level sets of w.\n",
}


def _entry(concept, variants, related=(), **extra):
    return {
        "concept": concept,
        "meaning": f"The {concept} concept.",
        "variants": [
            {"text": text, "family": family, "source": source} for text, family, source in variants
        ],
        "related": list(related),
        "added_by": "test",
        "added_on": "2026-09-11",
        **extra,
    }


def _document(entries):
    return {"schema": L.SCHEMA, "version": 1, "updated_on": "2026-09-11", "entries": entries}


BASE_ENTRIES = [
    _entry(
        "conditional-score",
        [
            ("conditional score", "derivations", "docs/derivations/w6.md:2"),
            ("Fisher term", "notes", "notes/imported/EX/ex-014.md:2"),
            ("Brascamp-Lieb", "notes", "notes/imported/EX/ex-014.md:1"),
            ("Conditional Poincare inequality", "paper", "paper/research_notes/g19.md:1"),
        ],
        related=["rare-fiber"],
    ),
    _entry(
        "rare-fiber",
        [
            ("rare fibers", "derivations", "docs/derivations/w6.md:2"),
            (
                "rare-source factorization",
                "corpus-import",
                "corpus-import/programs/pmbsf/lemma_q.md:1",
            ),
            ("level sets", "paper", "paper/research_notes/g19.md:1"),
        ],
    ),
    _entry(
        "hardy-tail",
        [
            ("Hardy tail-resistance", "derivations", "docs/derivations/w6.md:3"),
            ("Hardy inequality", "literature", "literature/index.yaml:1"),
        ],
    ),
    _entry(
        "kallen-lehmann",
        [
            (
                "Källén–Lehmann spectral representation",
                "corpus-import",
                "corpus-import/programs/pmbsf/lemma_q.md:2",
            ),
            ("delta atom", "corpus-import", "corpus-import/programs/pmbsf/lemma_q.md:2"),
            ("uniform in volume", "derivations", "docs/derivations/w6.md:4"),
        ],
    ),
]


@pytest.fixture
def root(tmp_path):
    for relative, text in SOURCES.items():
        path = tmp_path / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text, encoding="utf-8", newline="\n")
    return tmp_path


def _write_lexicon(root, entries, name="lexicon.yaml"):
    path = root / "graph-tasks" / "discovery" / name
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        yaml.safe_dump(_document(entries), sort_keys=False, allow_unicode=True),
        encoding="utf-8",
        newline="\n",
    )
    return path


@pytest.fixture
def lexicon(root):
    return L.load(_write_lexicon(root, BASE_ENTRIES), root)


# ----------------------------------------------------------------------------- validation


def test_seed_lexicon_loads_with_citations(lexicon):
    assert lexicon["schema"] == L.SCHEMA
    assert [entry["concept"] for entry in lexicon["entries"]][:2] == [
        "conditional-score",
        "rare-fiber",
    ]
    assert len(lexicon["fingerprint"]) == 64


def test_variant_with_nonexistent_citation_is_rejected(root):
    broken = copy.deepcopy(BASE_ENTRIES)
    broken[0]["variants"][0]["source"] = "docs/derivations/missing.md:1"
    with pytest.raises(ValueError, match="does not exist"):
        L.load(_write_lexicon(root, broken), root)


def test_variant_cited_beyond_file_end_is_rejected(root):
    broken = copy.deepcopy(BASE_ENTRIES)
    broken[0]["variants"][0]["source"] = "docs/derivations/w6.md:40"
    with pytest.raises(ValueError, match="exceed"):
        L.load(_write_lexicon(root, broken), root)


def test_variant_words_absent_from_cited_lines_are_rejected(root):
    invented = copy.deepcopy(BASE_ENTRIES)
    invented[0]["variants"][1]["text"] = "Fisher information matrix"
    with pytest.raises(ValueError, match=r"\['information', 'matrix'\]"):
        L.load(_write_lexicon(root, invented), root)


def test_accents_dashes_and_tex_escapes_fold_for_citation_checks(root):
    entries = copy.deepcopy(BASE_ENTRIES)
    entries[3]["variants"][0]["text"] = "Kallen--Lehmann spectral representation"
    (root / "corpus-import/programs/pmbsf/lemma_q.md").write_text(
        "Lemma Q is a conditional rare-source factorization.\n"
        "The K\\\"all\\'en-Lehmann spectral representation has a delta atom.\n",
        encoding="utf-8",
        newline="\n",
    )
    assert L.load(_write_lexicon(root, entries), root)["entries"][3]["concept"] == "kallen-lehmann"


@pytest.mark.parametrize(
    "mutate, message",
    [
        (lambda doc: doc.update(schema="workhouse-discovery-lexicon/v9"), "schema must be"),
        (lambda doc: doc.update(version=0), "version must be"),
        (lambda doc: doc["entries"].append(copy.deepcopy(doc["entries"][0])), "duplicate concept"),
        (lambda doc: doc["entries"][0].update(concept="Conditional Score"), "hyphenated slug"),
        (lambda doc: doc["entries"][0].update(status="proven"), "reserved keys"),
        (lambda doc: doc["entries"][0].update(evidence="analytic"), "reserved keys"),
        (lambda doc: doc["entries"][0]["variants"][0].update(tier=3), "reserved keys"),
        (lambda doc: doc["entries"][0].update(related=["nonexistent"]), "unknown"),
        (lambda doc: doc["entries"][0].update(related=["conditional-score"]), "relate to itself"),
        (lambda doc: doc["entries"][0]["variants"][0].update(family="blog"), "family 'blog'"),
        (
            lambda doc: doc["entries"][0]["variants"][0].update(source="docs/derivations/w6.md"),
            "path:line",
        ),
        (
            lambda doc: doc["entries"][0]["variants"][0].update(
                family="notes", source="docs/derivations/w6.md:2"
            ),
            "sources live under",
        ),
        (lambda doc: doc["entries"][0]["variants"][0].update(text="5/48"), "no word"),
        (lambda doc: doc["entries"][0]["variants"][0].update(text="DERIV:W6:M10"), "graph ID"),
        (
            lambda doc: doc["entries"][0].update(variants=doc["entries"][0]["variants"][:1]),
            "at least two",
        ),
        (lambda doc: doc["entries"][0].update(added_on="yesterday"), "ISO date"),
        (lambda doc: doc["entries"][0].pop("meaning"), "missing keys"),
    ],
)
def test_schema_problems_are_named(root, mutate, message):
    document = _document(copy.deepcopy(BASE_ENTRIES))
    mutate(document)
    problems = L.validate(document, root)
    assert any(message in problem for problem in problems), problems


def test_reserved_vocabulary_cannot_enter_even_without_citation_checks():
    document = _document(copy.deepcopy(BASE_ENTRIES))
    document["entries"][1]["evidence"] = "numerical"
    problems = L.validate(document, root=None, check_citations=False)
    assert problems == [
        "entries[1] (rare-fiber): reserved keys ['evidence']; the lexicon carries "
        "terminology only, scientific standing stays in ledger records"
    ]


def test_citation_outside_checkout_is_rejected(root):
    escaping = copy.deepcopy(BASE_ENTRIES)
    escaping[0]["variants"][0]["source"] = "docs/derivations/../../w6.md:2"
    problems = L.validate(_document(escaping), root)
    assert any("checkout-relative" in problem for problem in problems)


# ------------------------------------------------------------------------------ expansion


def test_focused_expansion_is_deterministic_and_prefers_multi_token_variants(lexicon):
    query = "conditional score domination on rare fibers"
    first = L.expand(query, lexicon)
    second = L.expand(query, lexicon)
    assert first == second
    assert first["mode"] == "focused"
    assert first["concepts"] == ["conditional-score", "rare-fiber"]
    # Concepts take turns: notes alternative of the first, corpus alternative of the second.
    assert first["sub_queries"][:2] == ["Fisher term", "rare-source factorization"]
    assert first["weights"] == [L.DEFAULT_LEXICON_WEIGHT] * len(first["sub_queries"])
    assert all("lexicon" not in text for text in first["sub_queries"])
    assert len(first["explanations"]) == len(first["sub_queries"])
    assert "notes/imported/EX/ex-014.md:2" in first["explanations"][0]
    assert first["detail"][0]["mode"] == "focused"


def test_in_place_expansion_substitutes_the_matched_phrase(lexicon):
    query = "conditional score domination on rare fibers"
    result = L.expand(query, lexicon, mode="in-place")
    assert result["mode"] == "in-place"
    assert result["sub_queries"][0] == "Fisher term domination on rare fibers"
    assert result["sub_queries"][1] == "conditional score domination on rare-source factorization"
    assert result["detail"][0]["mode"] == "replaced"
    with pytest.raises(ValueError, match="mode"):
        L.expand(query, lexicon, mode="sideways")


@pytest.mark.parametrize("mode", ["focused", "in-place"])
def test_expansion_order_is_independent_of_entry_order(root, mode):
    query = "conditional score domination on rare fibers and Hardy tail-resistance"
    baseline = L.expand(query, L.load(_write_lexicon(root, BASE_ENTRIES), root), mode=mode)
    for seed in range(4):
        shuffled = copy.deepcopy(BASE_ENTRIES)
        random.Random(seed).shuffle(shuffled)
        shuffled_lexicon = L.load(_write_lexicon(root, shuffled, f"lex{seed}.yaml"), root)
        assert L.expand(query, shuffled_lexicon, mode=mode) == baseline


@pytest.mark.parametrize("mode", ["focused", "in-place"])
def test_expansion_never_drops_exact_rationals_or_ids(lexicon, mode):
    query = "conditional score bound -10/96 for DERIV:W6_TAIL:M10 and G19 at 2.5"
    result = L.expand(query, lexicon, mode=mode)
    assert result["protected"] == ["-10/96", "DERIV:W6_TAIL:M10", "G19", "2.5"]
    assert result["sub_queries"]
    for text in result["sub_queries"]:
        for token in ("-10/96", "DERIV:W6_TAIL:M10", "G19", "2.5"):
            assert token in text
    if mode == "focused":
        assert result["sub_queries"][0] == "Fisher term -10/96 DERIV:W6_TAIL:M10 G19 2.5"


def test_in_place_replacement_tolerates_stop_words_plurals_and_dashes(lexicon):
    replaced = L.expand("estimates uniform in volume for the rare fiber", lexicon, mode="in-place")
    assert (
        "estimates Källén–Lehmann spectral representation for the rare fiber"
        in (replaced["sub_queries"])
    )
    assert (
        "estimates uniform in volume for the rare-source factorization" in (replaced["sub_queries"])
    )
    assert L.expand("a rare coarse fiber", lexicon, mode="in-place")["sub_queries"] == [
        "a rare coarse fiber rare-source factorization",
        "a rare coarse fiber level sets",
    ]


def test_nested_alternatives_are_not_stacked(root):
    entries = copy.deepcopy(BASE_ENTRIES)
    entries[0]["variants"].append(
        {
            "text": "Brascamp-Lieb gives",
            "family": "notes",
            "source": "notes/imported/EX/ex-014.md:1",
        }
    )
    lexicon = L.load(_write_lexicon(root, entries), root)
    result = L.expand("conditional score", lexicon)
    # 'Brascamp-Lieb gives' nests 'Brascamp-Lieb'; only the first is used, so the
    # same notes passage is not voted for twice under near-identical sub-queries.
    assert result["sub_queries"] == [
        "Fisher term",
        "Brascamp-Lieb",
        "Conditional Poincare inequality",
    ]


def test_expansion_budget_and_round_robin(lexicon):
    query = "conditional score on rare fibers with Hardy tail-resistance"
    limited = L.expand(query, lexicon, max_sub_queries=3)
    assert len(limited["sub_queries"]) == 3
    # Three-token 'Hardy tail-resistance' is the most specific match, then slug order;
    # each matched concept gets one turn before any concept gets a second.
    concepts = [row["concept"] for row in limited["detail"]]
    assert concepts == ["hardy-tail", "conditional-score", "rare-fiber"]
    assert L.expand(query, lexicon, max_sub_queries=0)["sub_queries"] == []
    with pytest.raises(ValueError):
        L.expand(query, lexicon, max_sub_queries=L.MAX_SUB_QUERIES + 1)
    with pytest.raises(ValueError):
        L.expand(query, lexicon, weight=0)


def test_no_match_yields_no_sub_queries(lexicon):
    result = L.expand("plaquette entropy beats logarithmic growth", lexicon)
    assert result == {
        "query": "plaquette entropy beats logarithmic growth",
        "mode": "focused",
        "sub_queries": [],
        "weights": [],
        "concepts": [],
        "explanations": [],
        "matches": [],
        "detail": [],
        "protected": [],
    }


# ----------------------------------------------------------------------------------- plan


def test_plan_shape(lexicon):
    result = L.plan("conditional score on rare fibers", lexicon)
    assert result["schema"] == L.PLAN_SCHEMA
    assert result["question"] == "conditional score on rare fibers"
    assert result["seeds"] == []
    assert result["queries"][0] == {
        "text": "conditional score on rare fibers",
        "weight": 1.0,
        "origin": "user",
    }
    assert len(result["queries"]) > 1
    for row in result["queries"][1:]:
        assert row["origin"].startswith("lexicon:")
        assert row["weight"] == L.DEFAULT_LEXICON_WEIGHT
        assert row["cites"]
    assert result["mode"] == "focused"
    in_place = L.plan("conditional score on rare fibers", lexicon, mode="in-place")
    assert in_place["mode"] == "in-place"
    assert in_place["queries"][1]["text"] == "Fisher term on rare fibers"
    assert "2-4 reformulations" in result["instructions"]
    assert "verbatim" in result["instructions"]
    assert "do not add IDs" in result["instructions"]
    assert result["lexicon"]["fingerprint"] == lexicon["fingerprint"]
    assert "not" in result["meaning"] and "evidence" in result["meaning"]
    json.dumps(result)
    with pytest.raises(ValueError):
        L.plan("   ", lexicon)
    with pytest.raises(ValueError):
        L.plan("x", lexicon, lexicon_weight=0)


def test_plan_file_feeds_the_cli_queries_file_reader(lexicon, tmp_path):
    from workhouse.cli import _sub_queries

    result = L.plan("conditional score on rare fibers", lexicon)
    path = tmp_path / "plan.json"
    path.write_text(json.dumps(result), encoding="utf-8")
    texts = _sub_queries(Namespace(queries=None, queries_file=str(path)))
    assert texts == [row["text"] for row in result["queries"]]


# ------------------------------------------------------------------------------ maintenance


def test_lexicon_add_appends_bumps_version_and_rejects_uncited(root):
    path = _write_lexicon(root, BASE_ENTRIES)
    original = path.read_bytes()
    entry = _entry(
        "combes-thomas",
        [
            ("Combes-Thomas block inverse", "notes", "notes/imported/EX/ex-014.md:3"),
            ("Selected inverse", "derivations", "docs/derivations/w6.md:4"),
        ],
        related=["conditional-score"],
    )
    updated = L.lexicon_add(path, entry, root)
    assert updated["version"] == 2
    assert [row["concept"] for row in L.lexicon_list(updated)][:2] == [
        "combes-thomas",
        "conditional-score",
    ]
    assert L.lexicon_show(updated, "combes-thomas")["variants"][0]["family"] == "notes"
    after_add = path.read_bytes()
    assert after_add.startswith(original.split(b"version: 1")[0])
    with pytest.raises(ValueError, match="duplicate concept"):
        L.lexicon_add(path, entry, root)
    invented = _entry(
        "invented",
        [
            ("cavity method", "corpus-import", "corpus-import/programs/pmbsf/lemma_q.md:1"),
            ("Fisher term", "notes", "notes/imported/EX/ex-014.md:2"),
        ],
    )
    with pytest.raises(ValueError, match="cavity"):
        L.lexicon_add(path, invented, root)
    assert path.read_bytes() == after_add


def test_lexicon_add_aligns_with_hand_indented_lists_and_keeps_comments(root):
    path = root / "graph-tasks" / "discovery" / "hand.yaml"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        "# hand-written header comment\n"
        "schema: workhouse-discovery-lexicon/v1\n"
        "version: 3\n"
        "entries:\n"
        "  - concept: hardy-tail\n"
        "    meaning: Hardy.\n"
        "    variants:\n"
        "      - text: Hardy tail-resistance\n"
        "        family: derivations\n"
        "        source: docs/derivations/w6.md:3\n"
        "      - text: Hardy inequality\n"
        "        family: literature\n"
        "        source: literature/index.yaml:1\n"
        "    related: []\n"
        "    added_by: test\n"
        "    added_on: 2026-09-11\n",
        encoding="utf-8",
        newline="\n",
    )
    entry = _entry(
        "rare-fiber",
        [
            ("rare fibers", "derivations", "docs/derivations/w6.md:2"),
            ("level sets", "paper", "paper/research_notes/g19.md:1"),
        ],
    )
    updated = L.lexicon_add(path, entry)  # root inferred from graph-tasks/discovery
    assert updated["version"] == 4
    text = path.read_text(encoding="utf-8")
    assert text.startswith("# hand-written header comment\n")
    assert "\n  - concept: rare-fiber\n" in text
    empty = root / "graph-tasks" / "discovery" / "empty.yaml"
    empty.write_text(
        "schema: workhouse-discovery-lexicon/v1\nversion: 1\nentries: []\n",
        encoding="utf-8",
        newline="\n",
    )
    assert [row["concept"] for row in L.lexicon_list(L.lexicon_add(empty, entry))] == ["rare-fiber"]


# -------------------------------------------------------------------------------------- CLI


def _parser():
    parser = ArgumentParser()
    subparsers = parser.add_subparsers(dest="discovery_command", required=True)
    L.add_parser(subparsers)
    return parser


def test_cli_plan_json_out_and_no_overwrite(root, capsys, tmp_path):
    path = _write_lexicon(root, BASE_ENTRIES)
    out = tmp_path / "plan.json"
    args = _parser().parse_args(
        ["plan", "conditional score on rare fibers", "--lexicon", str(path), "--out", str(out)]
    )
    args.json = True
    assert L.run(args, engine_factory=lambda: pytest.fail("plans need no engine")) == 0
    printed = json.loads(capsys.readouterr().out)
    assert printed["schema"] == L.PLAN_SCHEMA
    assert json.loads(out.read_text(encoding="utf-8"))["question"] == printed["question"]
    assert L.run(args, None) == 1
    assert "error" in json.loads(capsys.readouterr().out)
    args = _parser().parse_args(["plan", "conditional score", "--lexicon", str(path)])
    assert L.run(args, None) == 0
    text = capsys.readouterr().out
    assert "q1  w=1.0" in text and "lexicon:conditional-score" in text


def test_cli_lexicon_list_show_validate_add(root, capsys, tmp_path):
    path = _write_lexicon(root, BASE_ENTRIES)
    parser = _parser()
    assert L.run(parser.parse_args(["lexicon", "validate", "--lexicon", str(path), "--json"])) == 0
    report = json.loads(capsys.readouterr().out)
    assert report["valid"] and report["concepts"] == 4
    assert L.run(parser.parse_args(["lexicon", "list", "--lexicon", str(path)])) == 0
    assert "hardy-tail" in capsys.readouterr().out
    assert L.run(parser.parse_args(["lexicon", "show", "rare-fiber", "--lexicon", str(path)])) == 0
    assert "corpus-import/programs/pmbsf/lemma_q.md:1" in capsys.readouterr().out
    assert L.run(parser.parse_args(["lexicon", "show", "nope", "--lexicon", str(path)])) == 1
    assert "unknown concept" in capsys.readouterr().out
    entry_file = tmp_path / "entry.json"
    entry_file.write_text(
        json.dumps(
            _entry(
                "combes-thomas",
                [
                    ("Combes-Thomas block inverse", "notes", "notes/imported/EX/ex-014.md:3"),
                    ("Selected inverse", "derivations", "docs/derivations/w6.md:4"),
                ],
            )
        ),
        encoding="utf-8",
    )
    args = parser.parse_args(
        ["lexicon", "add", "--entry", str(entry_file), "--lexicon", str(path), "--json"]
    )
    assert L.run(args) == 0
    assert json.loads(capsys.readouterr().out)["concept"] == "combes-thomas"
    assert L.load(path, root)["version"] == 2


def test_cli_validate_reports_broken_lexicon(root, capsys):
    broken = copy.deepcopy(BASE_ENTRIES)
    broken[0]["variants"][0]["source"] = "docs/derivations/w6.md:99"
    path = _write_lexicon(root, broken)
    args = _parser().parse_args(["lexicon", "validate", "--lexicon", str(path), "--json"])
    assert L.run(args) == 1
    assert "exceed" in json.loads(capsys.readouterr().out)["error"]


# ----------------------------------------------------------------------- shipped lexicon


@pytest.mark.skipif(
    not (L.ROOT / L.DEFAULT_PATH).is_file() or not (L.ROOT / "docs/derivations").is_dir(),
    reason="shipped lexicon and its cited sources are only present in a full checkout",
)
def test_shipped_lexicon_citations_are_present_in_the_checkout():
    """Citation rot is a validation failure, as for ledger/symbols.yaml spellings."""
    lexicon = L.load()
    assert len(lexicon["entries"]) >= 40
    for entry in lexicon["entries"]:
        assert len({variant["family"] for variant in entry["variants"]}) >= 2, entry["concept"]
    assert Path(lexicon["path"]).name == "lexicon.yaml"
