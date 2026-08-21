"""Sweeps that need arithmetic, not comprehension.

The corpus is ~12M tokens, about 61x a context window. Nothing here reads it;
every check below compares numbers.
"""

from fractions import Fraction

import pytest

from workhouse import corpus_index as X
from workhouse import corpus_registry as R

pytestmark = pytest.mark.skipif(not X.CORPUS_DIR.is_dir(), reason="corpus-import/ not present")


@pytest.fixture(scope="module")
def table():
    return R.combined_table()


def test_the_corpus_has_no_undetected_transcription_slips(table):
    """A negative result worth pinning.

    Every adjacent pair of the 225 substantial rationals is compared. Exactly
    one pair agrees numerically without being equal, and it is the documented
    C20 artifact: the exact gate value against its float reconstruction.
    A second hit appearing here means a new slip entered the corpus.
    """
    pairs = R.near_miss_pairs(table)
    assert len(pairs) == 1, f"expected only the known C20 pair, got {pairs}"
    known = {Fraction(-1474623, 1675520), Fraction(-521965902, 593076541)}
    assert {pairs[0].a, pairs[0].b} == known
    assert pairs[0].relative < 1e-14


def test_attribution_survives_chained_equalities():
    """`x = y + z = value` binds the value to `x`, not to the nearest symbol.

    Getting this wrong reported the flat-band paper's `B_5` as carrying two
    values. It does not: the second is `Delta c_5 = A_5 + B_5`, and the two
    differ by exactly `A_5 = 313/240`.
    """
    line = r"\Delta c_5=A_5+B_5=\frac{4037562229115732471176793}{1652932248975967181040000}"
    assert R._attribute(line) == r"\Delta c_5"
    simple = r"B_5=\frac{1881863087742908605903793}{1652932248975967181040000}"
    assert R._attribute(simple) == "B_5"


def test_the_b5_difference_is_exactly_A5():
    """The arithmetic that proved the false positive."""
    a = Fraction(1881863087742908605903793, 1652932248975967181040000)
    b = Fraction(4037562229115732471176793, 1652932248975967181040000)
    assert b - a == Fraction(313, 240)


def test_pentagonal_ratio_chain_is_only_half_documented():
    """FINDING: the classifier records tau_4 -> dispersion, not h_4_side -> tau_4."""
    h = Fraction(2861009, 84387303000)  # h_4^side
    tau = Fraction(2861009, 16877460600)  # tau_4
    disp = Fraction(2861009, 8438730300)  # cap dispersion coefficient
    assert tau / h == 5
    assert disp / tau == 2
    assert disp / h == 10
    documented = " ".join(X.classifier_entries())
    assert "2861009/16877460600 ~ 2861009/8438730300" in documented
    assert "2861009/84387303000" not in documented, (
        "the 5x link from h_4^side to tau_4 is now documented — retire this check"
    )


def test_coverage_makes_the_unexamined_remainder_visible(table):
    cov = R.coverage(table)
    assert cov["text_files"] > 800
    assert cov["files_carrying_a_rational"] > 300
    # Files with nothing checkable stay T3. Saying so is the point.
    assert cov["prose_only_files"] > 400
    assert cov["distinct_rationals"] > 1000
