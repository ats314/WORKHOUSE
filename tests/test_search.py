"""Search is the retrieval this corpus actually needs: by value, not by concept."""

import json
import subprocess
import sys
from pathlib import Path

from workhouse import claims as C
from workhouse import search as S

ROOT = Path(__file__).resolve().parents[1]
CATALOGUE = C.collect()
SYMBOLS = C.symbol_records(CATALOGUE)


def _search(query):
    return S.search(query, CATALOGUE, SYMBOLS)


def test_exact_rationals_match_by_value_not_by_spelling():
    """-10/96 and -5/48 are the same claim. A string index would miss that."""
    hits, _ = _search("-10/96")
    assert any(h.claim.id == "CONST:CUBE_COMPLETION_4" for h in hits), [h.claim.id for h in hits]
    assert all(h.claim.value != "-10/96" for h in hits), "matched the spelling, not the value"


def test_a_decimal_prefix_finds_both_sides_of_c20():
    """The one real near-miss in the corpus, from eight digits.

    -0.8800987156226127 (exact gate) and -0.8800987156226097 (the printed
    float-reconstruction) differ by 31 ulps. Anyone typing the printed decimal
    should be shown both, plus the check that quantifies the gap.
    """
    hits, _ = _search("-0.88009871")
    ids = {h.claim.id for h in hits}
    assert "CONST:LINKED_VACUUM_4" in ids
    assert "CONST:LINKED_VACUUM_4_ARTIFACT" in ids
    assert any("c20" in i.lower() for i in ids)


def test_a_corpus_spelling_finds_the_repo_name():
    """C_shp appears nowhere in the corpus; C_shape appears 74 times."""
    hits, symbols = _search("C_shape")
    assert [s["canonical"] for s in symbols] == ["C_shp"]
    assert "C2" in {h.claim.id for h in hits}


def test_the_forbidden_name_is_matched_on_purpose():
    """`m_4` is what someone types when they have the wrong model.

    That query is the last moment the warning can help, so it must match even
    though `m_4` is not a legitimate alias of anything.
    """
    hits, symbols = _search("m_4")
    canon = {s["canonical"] for s in symbols}
    assert canon == {"q_band^(4)", "m_Gamma^(4)"}
    for symbol in symbols:
        assert symbol["forbidden"], symbol["canonical"]
    assert "C1" in {h.claim.id for h in hits}


def test_short_queries_need_a_token_boundary():
    """`m_4` must not match inside `LINKED_VACUUM_4`."""
    hits, _ = _search("m_4")
    text_hits = {h.claim.id for h in hits if h.how == "text"}
    assert "CONST:LINKED_VACUUM_4" not in text_hits
    assert "CONST:LINKED_VACUUM_4_ARTIFACT" not in text_hits


def test_a_coined_name_is_flagged_as_coined():
    """Phi_C is this repository's word. Not finding it is not absence."""
    _hits, symbols = _search("Phi_C")
    assert symbols and symbols[0]["coined_here"] is True
    rendered = S.format_results("Phi_C", *_search("Phi_C"))
    assert "Coined in this repository" in rendered
    assert "not absence" in rendered


def test_a_claim_id_pulls_in_what_it_routes_to():
    hits, _ = _search("C2")
    ids = {h.claim.id for h in hits}
    assert {"C2", "G3", "R5"} <= ids


def test_an_unmatched_query_says_how_to_ask_better():
    hits, symbols = _search("zzzz-no-such-thing")
    assert not hits and not symbols
    rendered = S.format_results("zzzz-no-such-thing", hits, symbols)
    assert "no claim matches" in rendered
    assert "exact rational" in rendered


def test_every_declared_corpus_spelling_is_still_findable():
    """The aliases are OBSERVED, not invented. Re-check them against the corpus.

    A spelling that has vanished is either a typo here or a document that moved,
    and both are worth a build failure. `coined_here` symbols are exempt --
    their whole point is that the corpus does not use the name.

    One grep pass over 928 files, not one per spelling: `-f` takes the whole
    pattern list and `-o` reports what matched. Containment rather than set
    membership on that output, because `-o` prints only the longest match at a
    position -- `Delta_C` never appears on its own when `\\Delta_C` is also in
    the list, though the text plainly contains it.
    """
    corpus = ROOT / "corpus-import"
    if not corpus.is_dir():
        return
    wanted = {
        spelling
        for symbol in SYMBOLS
        if not symbol.get("coined_here")
        for spelling in symbol["corpus_spellings"]
    }
    patterns = "\n".join(sorted(wanted)) + "\n"
    found = subprocess.run(
        ["grep", "-rIohF", "-f", "-", str(corpus), str(ROOT / "theory")],
        input=patterns,
        capture_output=True,
        text=True,
    )
    seen = found.stdout
    missing = sorted(spelling for spelling in wanted if spelling not in seen)
    assert not missing, "declared corpus spellings that no longer appear: " + "; ".join(missing)


def test_coined_names_really_are_absent_from_the_corpus():
    """The other direction: if a `coined_here` name turns up, the flag is wrong."""
    corpus = ROOT / "corpus-import"
    if not corpus.is_dir():
        return
    coined = [s["canonical"] for s in SYMBOLS if s.get("coined_here")]
    if not coined:
        return
    found = subprocess.run(
        ["grep", "-rIohF", "-f", "-", str(corpus)],
        input="\n".join(coined) + "\n",
        capture_output=True,
        text=True,
    )
    assert not found.stdout.strip(), (
        f"marked coined_here but present in the corpus: {set(found.stdout.split())}"
    )


def test_catalogue_files_are_current():
    claims_path, symbols_path = C.CLAIMS, C.SYMBOLS
    expected_claims = "".join(
        json.dumps(__import__("dataclasses").asdict(c), sort_keys=True) + "\n" for c in CATALOGUE
    )
    assert claims_path.read_text() == expected_claims, "stale; run `make catalogue`"
    expected_symbols = "".join(json.dumps(s, sort_keys=True) + "\n" for s in SYMBOLS)
    assert symbols_path.read_text() == expected_symbols, "stale; run `make catalogue`"


def test_no_generated_prose_fields():
    """Every field is copied from a curated source; none is written here.

    A generated one-line gloss would be the one place in this index an error
    could enter that no test could catch, and it would read like an index rather
    than like a guess.
    """
    fields = set(json.loads(C.CLAIMS.read_text().splitlines()[0]))
    assert "summary" not in fields and "topics" not in fields and "description" not in fields


def test_cli_search_runs_and_exits_nonzero_on_a_miss():
    hit = subprocess.run(
        [sys.executable, "-m", "workhouse.cli", "search", "--", "109151/249696"],
        capture_output=True,
        text=True,
        cwd=ROOT,
    )
    assert hit.returncode == 0 and "matching claims" in hit.stdout
    miss = subprocess.run(
        [sys.executable, "-m", "workhouse.cli", "search", "--", "zzzz-no-such-thing"],
        capture_output=True,
        text=True,
        cwd=ROOT,
    )
    assert miss.returncode == 1
