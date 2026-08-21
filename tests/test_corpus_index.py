"""The code/data index must cover what the prose index cannot see."""

from fractions import Fraction

import pytest

from workhouse import corpus_index as X

pytestmark = pytest.mark.skipif(not X.CORPUS_DIR.is_dir(), reason="corpus-import/ not present")


@pytest.fixture(scope="module")
def tables():
    return X.scan(), X.scan(exts=X.PROSE_EXTS)


def test_code_files_outnumber_prose(tables):
    """The prose engine sees 322 of 854; this one exists for the other 532."""
    cov = X.coverage()
    assert cov["code_files"] > cov["prose_files"]


def test_sealed_core_is_visible_here(tables):
    """5/48 and friends have no entry in the prose index (MIN_MAG = 1000)."""
    code, prose = tables
    locs = X.sealed_core_locations(code, prose)
    assert locs["A_shp = 5/48"]["code_files"] > 10
    assert locs["alpha_pen = 5/12"]["code_files"] > 10
    assert locs["t_3 = 5/612"]["code_files"] > 10


def test_short_rationals_need_a_denominator_floor():
    """Guard against indexing array subscripts as constants."""
    assert X.MIN_DENOMINATOR >= 8
    assert Fraction(5, 48).denominator >= X.MIN_DENOMINATOR


def test_finds_undocumented_convention_factors(tables):
    """The classifier's hazard class, extended past prose.

    A code constant that is a simple rational multiple of a vouched one is
    either a convention that belongs in the classifier or a transcription that
    does not. Either way nothing currently records it.
    """
    code, prose = tables
    findings = X.rational_multiples(code, prose)
    assert findings, "expected at least the beta/8 and sigma_4 multiples"
    ratios = {abs(f.ratio) for f in findings}
    assert Fraction(1, 8) in ratios, "beta_old/8 lives in code with no prose backing"


def test_classifier_is_prose_only(tables):
    """Every pair it documents is absent from our code-side findings."""
    code, prose = tables
    known = X.classifier_entries()
    assert known, "the corpus classifier should be readable"
    found = {
        f"{f.code_value.numerator}/{f.code_value.denominator}"
        for f in X.rational_multiples(code, prose)
    }
    documented = {k.split(" ~ ")[0].strip() for k in known}
    assert not (found & documented), "a finding should not duplicate the classifier"


def test_scan_is_read_only(tmp_path):
    (tmp_path / "a.py").write_text("x = 5/48\n")
    before = (tmp_path / "a.py").read_bytes()
    X.scan(root=tmp_path)
    assert (tmp_path / "a.py").read_bytes() == before
