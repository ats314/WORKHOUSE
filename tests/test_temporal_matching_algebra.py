"""Exact regressions for the temporal matching note; no lattice engine imported."""

import unittest
from fractions import Fraction

import sympy as s


class TemporalMatchingAlgebra(unittest.TestCase):
    def test_normalization_dictionary(self):
        N, eps, u = s.symbols("N eps u", positive=True)
        bt = 2 * N / eps
        bs = 2 * N * u * eps
        self.assertEqual(s.simplify(bs / (2 * N * eps)), u)
        self.assertEqual(s.simplify(bt * bs / (4 * N * N)), u)

    def test_anisotropic_prefactor(self):
        gs, gt, at, asp, N = s.symbols("gs gt at asp N", positive=True)
        xi = asp / at
        bt = 2 * N * xi / gt**2
        bs = 2 * N / (xi * gs**2)
        eps = 2 * N / bt
        self.assertEqual(s.simplify(bs / (2 * N * eps)), 1 / (gs**2 * gt**2))
        self.assertEqual(s.simplify(eps / at - (gt / gs) * (gs * gt) / asp), 0)

    def test_gaussian_covariance(self):
        N = s.symbols("N", positive=True)
        D = N * N - 1
        fundamental_fourth = D * (2 * N * N - 3) / (4 * N)
        covariance = 4 * fundamental_fourth / 12 - N * 2 * D / 24
        self.assertEqual(s.factor(covariance - D * (N * N - 3) / (12 * N)), 0)

    def test_clock_logarithm(self):
        e, C, N = s.symbols("e C N", positive=True)
        lam = 1 - C * e / 2 + (C * C / 8 - C * (N * N - 2) / (16 * N)) * e * e
        clock = s.series(-2 * s.log(lam) / C, e, 0, 3).removeO()
        self.assertEqual(s.simplify(clock - e - (N * N - 2) * e * e / (8 * N)), 0)

    def test_clock_cancels_every_fixed_casimir(self):
        e, C, N = s.symbols("e C N", positive=True)
        a = (N * N - 2) / (8 * N)
        loglam = -C * e / 2 - C * a * e * e / 2
        energy = s.series(-loglam / (e + a * e * e), e, 0, 2).removeO()
        self.assertEqual(s.simplify(energy - C / 2), 0)

    def test_single_plaquette_seed_energy(self):
        CF = s.Rational(4, 3)
        self.assertEqual(4 * CF / 2, s.Rational(8, 3))

    def test_symmetric_noncommuting_product_to_second_order(self):
        # Exact matrices deliberately do not commute.
        A = s.diag(0, 1, 3)
        B = s.Matrix([[0, 1, 0], [1, 0, 2], [0, 2, 0]])
        self.assertNotEqual(A * B, B * A)
        first = A + B
        second = A * A / 2 + B * B / 2 + (A * B + B * A) / 2
        self.assertEqual(second, first * first / 2)
        # This is the eps^2 cancellation in log(exp(eB/2)exp(eA)exp(eB/2)).
        self.assertEqual(second - first * first / 2, s.zeros(3))

    def test_relative_matching_margin(self):
        self.assertEqual(1 - 2 * Fraction(1, 4), Fraction(1, 2))
        self.assertEqual(Fraction(1, 4) / (1 - 2 * Fraction(1, 4)), Fraction(1, 2))

    def test_clock_only_without_retuning_changes_u(self):
        u, e, t = s.symbols("u e t", positive=True)
        magnetic_weight = u * e
        self.assertEqual(magnetic_weight / t, u * e / t)
        self.assertNotEqual(s.simplify(magnetic_weight / t), u)
        self.assertEqual(s.simplify((u * t) / t), u)


if __name__ == "__main__":
    unittest.main(verbosity=2)
