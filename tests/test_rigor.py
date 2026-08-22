"""The enclosure layer must be exact on entry and honest about overlap.

Each rule here names its failure mode: a value entering through a lossy
path is the exact/float boundary bug; a comparison that returns True on
overlapping balls is a certificate that certifies nothing.
"""

import pytest
from flint import arb
from sympy import Float, Rational

from workhouse import rigor


def test_doubles_enter_exactly():
    """A double is a dyadic rational; its ball must have zero radius."""
    b = rigor.ball(0.1)
    assert float(b.rad()) == 0.0


def test_rationals_are_enclosed():
    """The true rational must lie inside its ball's enclosure."""
    b = rigor.ball(Rational(1, 3))
    assert (b * 3 - 1).contains(0)
    assert float(b.rad()) > 0  # 1/3 is not dyadic; an exact claim would be a lie


def test_lossy_entry_paths_are_refused():
    """Strings and sympy Floats must be converted deliberately, never silently."""
    with pytest.raises(TypeError):
        rigor.ball("0.1")
    with pytest.raises(TypeError):
        rigor.ball(Float("0.1", 25))


def test_overlapping_balls_certify_nothing():
    """certified_lt must refuse the comparison when enclosures overlap."""
    a = arb("1.0", "1e-5")
    b = arb("1.000001", "1e-5")
    assert not rigor.certified_lt(a, b)
    assert not rigor.certified_lt(b, a)


def test_adjacent_doubles_are_separated_at_working_precision():
    """One ulp at double precision is a chasm at 128 bits — the FINDING's
    discrimination between two adjacent doubles must be provable, both ways."""
    import math

    x = 1.2345678901234567
    y = math.nextafter(x, 2.0)
    assert rigor.certified_lt(rigor.ball(x), rigor.ball(y))
    assert not rigor.certified_lt(rigor.ball(y), rigor.ball(x))


def test_certified_closer_discriminates_and_refuses():
    target = rigor.ball(Rational(1, 3))
    near = rigor.ball(1 / 3)  # nearest double
    import math

    far = rigor.ball(math.nextafter(1 / 3, 1.0))
    assert rigor.certified_closer(target, near, far)
    assert not rigor.certified_closer(target, far, near)
    # equidistant/self case: provable-only semantics refuse it
    assert not rigor.certified_closer(target, near, near)
