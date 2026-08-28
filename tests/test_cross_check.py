"""The flint rational-function engine, and the witnesses built on it."""

import pytest
from flint import fmpq, fmpq_poly

from workhouse import constants as K
from workhouse import cross_check as X


@pytest.fixture(scope="module")
def n():
    return X.Rat.of(X.GEN)


def test_the_normal_form_is_canonical(n):
    """Two spellings of one rational function must be the same object."""
    a = (n**2 - 1) / (n - 1)
    b = n + 1
    assert a == b
    assert a.num == b.num and a.den == b.den
    # ... and the denominator is monic, so scaling cannot produce two answers
    scaled = (2 * n**2 - 2) / (2 * n - 2)
    assert scaled == b


def test_arithmetic_is_exact(n):
    third = X.Rat.of(fmpq(1, 3))
    assert (third + third + third) == X.Rat.of(1)
    assert (n / (n + 1) + 1 / (n + 1)) == X.Rat.of(1)
    assert (n**3) ** 2 == n**6
    assert (n**-2) * n**2 == X.Rat.of(1)


def test_a_zero_denominator_raises_rather_than_agreeing_with_everything(n):
    with pytest.raises(ZeroDivisionError):
        X.Rat.make(fmpq_poly([1]), fmpq_poly([0]))
    with pytest.raises(ZeroDivisionError):
        (1 / (n - 3)).at(3)


def test_the_quotient_rule(n):
    assert (n**3).derivative() == 3 * n**2
    assert (1 / n).derivative() == -1 / n**2
    assert ((n + 1) / (n - 1)).derivative() == -2 / (n - 1) ** 2


def test_sympy_crosses_the_boundary_as_coefficients_only(n):
    """`together` is a common denominator, not a cancellation."""
    from sympy import together

    expr = K.hopping()
    assert X.from_sympy(expr, K.N) == X.from_sympy(together(expr), K.N)
    assert X.from_sympy(K.hopping(3)) == X.Rat.of(fmpq(5, 612))


def test_every_registered_witness_holds():
    held, failed = X.run()
    assert not failed, [w.name for w in failed]
    assert len(held) >= 25


def test_the_witness_can_fail(n):
    """A comparison that cannot fail says nothing about what it compares."""
    right = 2 * n * (n**2 - 4) / ((n**2 - 1) * (2 * n**2 - 1) * (4 * n**2 - 9))
    wrong = 2 * n * (n**2 - 4) / ((n**2 - 1) * (2 * n**2 - 1) * (4 * n**2 - 8))
    assert right != wrong
    assert X.Witness("planted", "test", X.from_sympy(K.hopping(), K.N), wrong).holds() is False
    assert X.Witness("planted", "test", X.from_sympy(K.hopping(), K.N), right).holds() is True


def test_a_structural_comparison_is_not_a_sample(n):
    """Point agreement is not identity; the engine compares normal forms."""
    right = n**2
    decoy = (n**7 - n**5 * 0) / n**5  # equals n**2 everywhere it is defined
    assert right == decoy
    near = (n**2 * (n - 5) + 0) / (n - 5)
    assert near == right  # the shared factor cancels exactly
    apart = n**2 + 1 / (n**10)
    assert apart != right
    assert all(apart.at(p) != right.at(p) for p in range(2, 6))


def test_witnesses_declare_whether_they_are_independent():
    rows = X.witnesses()
    assert sum(1 for w in rows if w.independent) >= 15
    for w in rows:
        assert w.name and w.section
