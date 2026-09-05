"""Compression and damping checks use the full operator, not only a source column."""

from sympy import Rational, SparseMatrix

from workhouse.wilson_vacuum_chart import chart, product_chart


def test_second_rotation_changes_only_the_vacuum_offdiagonal_blocks():
    model = chart(
        SparseMatrix.diag(1, Rational(3, 4)),
        [SparseMatrix([[0, Rational(2, 3)], [Rational(2, 3), Rational(1, 2)]])],
    )
    q = SparseMatrix.diag(0, 1)
    assert model.second_rotated[(2,)] == q * model.first_rotated[(2,)] * q
    assert not model.first_rotated[(2,)][:, 0].is_zero_matrix


def test_first_rotation_preserves_the_excited_compression_of_raw_transfer():
    for steps in (1, 2, 5):
        model = product_chart(2, ((0, 1),), steps=steps)
        q = SparseMatrix.diag(0, 1, 1, 1)
        assert model.first_rotated[(1,)] == q * model.raw[(1,)] * q


def test_perron_compression_factor_is_sharp_for_general_positive_families():
    # C(u)=diag(1+c u², delta-c u²) is positive with the first entry
    # its simple Perron eigenvalue near zero. Division by that eigenvalue
    # produces excited coefficient -(1+delta)c, not merely -c.
    delta, c = Rational(4, 5), Rational(3, 7)
    raw2 = SparseMatrix.diag(c, -c)
    base = SparseMatrix.diag(1, delta)
    q = SparseMatrix.diag(0, 1)
    corrected = q * raw2 * q - c * base * q
    assert corrected[1, 1] == -(1 + delta) * c
