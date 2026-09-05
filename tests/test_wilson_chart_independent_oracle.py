"""Closed two-level spectral formulas independent of the coefficient engine.

The Perron coefficients follow from trace and determinant of the exact
symmetric transfer. The local generator follows the direct eigenvector
expansion. Two noncommuting potentials test mixed coefficients and scaling.
"""

import pytest
from sympy import Rational, SparseMatrix

from workhouse.wilson_vacuum_chart import chart


@pytest.mark.parametrize("steps", [1, 4])
def test_noncommuting_two_level_trace_determinant_and_eigenvector_oracle(steps):
    delta, tau = Rational(3, 5), Rational(2, 3)
    v1, h1 = Rational(2, 7), Rational(3, 8)
    v2, h2 = -Rational(1, 5), Rational(4, 9)
    first = SparseMatrix([[0, v1], [v1, h1]])
    second = SparseMatrix([[0, v2], [v2, h2]])
    assert first * second != second * first
    actual = chart(SparseMatrix.diag(1, delta), [first, second], steps, tau)

    # det(T)=delta*exp(tau*(h1*z1+h2*z2)), while tr(T)=tr(D*exp(tau*V)).
    # Expanding lambda^2-tr(T)*lambda+det(T)=0 at lambda(0)=1 gives b2.
    # Since b1=0, the Perron coefficient of T^m is m times that of T.
    common = steps * tau**2 * (1 + delta) / (1 - delta)
    perron = {
        (2, 0): common * v1**2 / 2,
        (1, 1): common * v1 * v2,
        (0, 2): common * v2**2 / 2,
    }
    eigenvector_factor = tau**2 * (1 + 6 * delta + delta**2) / (8 * (1 - delta) ** 2)
    generator = {
        (2, 0): eigenvector_factor * h1 * v1,
        (1, 1): eigenvector_factor * (h1 * v2 + h2 * v1),
        (0, 2): eigenvector_factor * h2 * v2,
    }
    for degree in perron:
        assert actual.eigenvalue_second[degree] == perron[degree]
        assert actual.second_generators[degree][1, 0] == generator[degree]
        assert actual.second_rotated[degree][:, 0].is_zero_matrix

    assert generator == {
        (2, 0): Rational(31, 168),
        (1, 1): Rational(4061, 45360),
        (0, 2): -Rational(62, 405),
    }
