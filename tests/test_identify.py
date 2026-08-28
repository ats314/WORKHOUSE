"""The identification machinery, and the guards that stop it finding things."""

import math
from fractions import Fraction

import pytest

from workhouse import identify as ident


def test_simplest_between_is_the_least_denominator():
    """The classic cases, plus one the float version gets wrong.

    The interval is CLOSED, so [1/3, 1/2] answers 1/2 rather than the 2/5 the
    open interval would give -- an endpoint is admissible, which is what the
    caller wants when the endpoints are a measurement's error bars.
    """
    assert ident.simplest_between(Fraction(1, 3), Fraction(1, 2)) == Fraction(1, 2)
    assert ident.simplest_between(Fraction(3, 10), Fraction(2, 5)) == Fraction(1, 3)
    assert ident.simplest_between(Fraction(3), Fraction(4)) == Fraction(3)
    assert ident.simplest_between(Fraction(-1, 2), Fraction(1, 2)) == Fraction(0)
    # An interval far below double precision: the float recursion diverges here.
    lo = Fraction(1, 3) - Fraction(1, 10**30)
    hi = Fraction(1, 3) + Fraction(1, 10**30)
    assert ident.simplest_between(lo, hi) == Fraction(1, 3)


@pytest.mark.parametrize(
    ("value", "half", "qmax"),
    [(0.1234567, 1e-4, 600), (-0.42857, 1e-3, 300), (3.14159, 1e-5, 900)],
)
def test_enumeration_matches_trial_division(value, half, qmax):
    w = ident.Window(value, half, "test")
    found, truncated = ident.admissible_rationals(w, qmax)
    assert not truncated
    assert len(found) == ident.brute_force_count(w, qmax)
    lo, hi = w.interval()
    assert all(lo <= f <= hi and f.denominator <= qmax for f in found)
    assert len(set(found)) == len(found)


def test_farey_estimate_tracks_the_exact_count():
    """The closed form is asymptotic; it must still be right to a few percent."""
    w = ident.Window(0.020213328886166577, 7.6e-16, "test")
    found, _ = ident.admissible_rationals(w, 10**9)
    assert 0.9 < len(found) / ident.farey_count(w, 10**9) < 1.1


def test_saturation_is_where_every_denominator_matches():
    w = ident.Window(0.123456789, 1e-9, "test")
    lo, hi = w.interval()
    sat = ident.saturation_denominator(w)
    for q in (sat, sat + 1, 3 * sat):
        assert math.ceil(lo * q) <= math.floor(hi * q)


def test_a_window_needs_a_positive_halfwidth():
    with pytest.raises(ValueError):
        ident.Window(1.0, 0.0, "an exact value needs no window")


def test_an_all_rational_basis_is_refused():
    """The trap: 4*(5/48) - 5/12 = 0 is a relation among the basis, not a find."""
    w = ident.Window(-0.020213328886166577, 4.6e-15, "test")
    with pytest.raises(ValueError, match="Q-linearly dependent"):
        ident.sweep(w, {"a": Fraction(5, 48), "b": Fraction(5, 12)})


def test_the_relation_search_finds_a_planted_relation():
    values = [math.pi, math.sqrt(2), 3 * math.pi - 5 * math.sqrt(2)]
    coefficients, residual = ident.lll_relations(values, 14, limit=1)[0]
    assert abs(float(residual)) < 1e-10
    assert coefficients in ((3, -5, -1), (-3, 5, 1))
    assert ident.pslq_relation(values, 12)["relation"] is not None


def test_pslq_reports_an_exclusion_rather_than_a_silence():
    """A None must say which None it is: no relation, or out of steps."""
    result = ident.pslq_relation([ident.targets()["C_shp"].value, math.pi, math.e], 16, 10**5)
    assert result["relation"] is None
    assert not result["exhausted"]
    assert result["norm_bound"] and result["norm_bound"] > 1000


def test_a_genuine_relation_is_a_candidate_under_the_calibrated_budget():
    """The false negative the uncalibrated margin produced, pinned.

    ``x = 5/48 - pi/1000`` really does satisfy ``6000x - 625 + 6*pi = 0``.
    Charging the search by significant digits scored that at margin +1.8 and
    discarded it; the counting budget scores it +4.0.
    """
    planted = 5 / 48 - math.pi / 1000
    w = ident.Window(planted, 1e-15, "planted control")
    found = [r for r in ident.sweep(w, {"1": 1.0, "pi": math.pi}) if r.height == 6000]
    assert found, "the planted relation was not returned"
    assert found[0].window_consistent
    assert found[0].verdict == "candidate"


def test_a_relation_that_misses_the_window_is_not_scored_on_a_budget():
    w = ident.Window(0.1234567890123, 1e-16, "a very tight window")
    off = [r for r in ident.sweep(w, ident.bases()["circle"], digits=9) if not r.window_consistent]
    assert off, "expected an under-resolved relation to miss the window"
    assert all(r.verdict == "off-window" for r in off)


def test_the_lattice_scale_follows_the_absolute_window():
    assert ident.scale_digits(ident.Window(0.02, 1e-15, "x")) == 15
    assert ident.scale_digits(ident.Window(0.02, 1e-13, "x")) == 13


def test_a_float_basis_is_refused_past_the_dyadic_threshold():
    """Past ~22 digits LLL returns the basis's own dyadic dependency."""
    w = ident.Window(0.02021332888616, 1e-30, "impossibly tight")
    with pytest.raises(ValueError, match="dyadic dependency"):
        ident.sweep(w, ident.bases()["circle"])


def test_the_c2_float_yields_nothing_that_clears_its_budget():
    """The finding, as a test: no relation over any basis is a candidate."""
    w = ident.targets()["C_shp"]
    for basis in ident.bases().values():
        assert all(r.verdict != "candidate" for r in ident.sweep(w, basis))
    assert ident.admissible_rationals(w, 10**6) == ([], False)


def test_the_registered_c20_artifact_is_refused():
    """limit_denominator always answers, and the corpus has the scar to prove it.

    LINKED_VACUUM_4_ARTIFACT is exactly what limit_denominator(1e9) returned for
    a float whose true exact value is -1474623/1675520, 31 ulps away. The
    identifier must not reproduce that mistake: at the value's own precision the
    nine-digit denominator is far past the ceiling, so it is not a candidate.
    """
    from workhouse import constants as K

    artifact = Fraction(int(K.LINKED_VACUUM_4_ARTIFACT.p), int(K.LINKED_VACUUM_4_ARTIFACT.q))
    truth = Fraction(int(K.LINKED_VACUUM_4.p), int(K.LINKED_VACUUM_4.q))
    assert artifact == Fraction(float(truth)).limit_denominator(10**9) or artifact != truth
    w = ident.Window(float(truth), 1e-13, "the gate value's own printed precision")
    assert ident.identification_ceiling(w) < artifact.denominator
    found, _ = ident.admissible_rationals(w, 10**7)
    assert truth in found
    assert artifact not in found


def test_targets_declare_a_provenance_for_their_window():
    for name, w in ident.targets().items():
        assert w.halfwidth > 0, name
        assert len(w.provenance) > 20, name
        assert 8 < w.digits <= ident.DOUBLE_DIGITS, name
