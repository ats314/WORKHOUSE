"""`workhouse ask` finds candidates and promotes nothing."""

from workhouse import finder as F


def test_tokenizer_keeps_rationals_whole_and_drops_stop_words():
    toks = F.tokenize("the coefficient 5/48 and -11/192 of C_shp is t_N")
    assert "5/48" in toks and "-11/192" in toks
    assert "the" not in toks and "and" not in toks
    assert "c_shp" in toks and "t_n" in toks


def test_a_question_in_words_finds_the_check_that_answers_it():
    index = F.load_cached()
    rows, text = F.ask(
        "plaquette graph twelve neighbours two faces share at most one link", 5, index
    )
    assert rows
    assert any("12-regular" in r["text"] for r in rows[:3]), [r["where"] for r in rows]
    assert "T3" in text
    assert all(r["why"].startswith("workhouse why") for r in rows if r["claim"])


def test_corpus_prose_is_in_the_index_with_line_numbers():
    index = F.load_cached()
    prose = [c for c in index.chunks if c.where.startswith("corpus-import/") and not c.claim]
    assert len(prose) > 1000
    assert all(":" in c.where and c.where.rsplit(":", 1)[1].isdigit() for c in prose[:50])


def test_a_query_with_no_shared_term_is_empty_not_invented():
    index = F.load_cached()
    rows, text = F.ask("zzzqqq xyzzy", 5, index)
    assert rows == [] and "no chunk" in text
