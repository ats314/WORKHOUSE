"""Independent exact regressions for sixth-order dynamics and scope boundaries."""

from fractions import Fraction

import pytest
import sympy as sp

from workhouse.invariants.sixth_order import sixth
from workhouse.sixth_order import (
    E2,
    E3,
    Q,
    carrier_word,
    combination_report,
    evaluate_words,
    folded_series,
    h4_support,
    mixing_terms,
    reduce_support,
    single_plaquette_series,
)


@pytest.mark.parametrize("name,section,tier,fn", sixth.checks, ids=[x[0] for x in sixth.checks])
def test_exact_control(name, section, tier, fn):
    result = fn()
    assert result[0], result[1]


def test_word_shapes_must_be_combined_before_membership_test():
    # Each word has e2^2, but their sum does not. A positive individual word
    # expectation or a path count cannot certify a surviving shape.
    assert carrier_word("RUR") == 4 * E2**2
    assert reduce_support({"RUR": 1, "RRR": 2}) == -4 * Q * E3
    assert (
        sp.expand(carrier_word("RSR") - ((Q - 4) * carrier_word("RR") - carrier_word("RUR"))) == 0
    )


def test_unknown_direct_h6_is_not_silently_zero():
    missing = combination_report()
    zero = combination_report({})
    assert missing["combined_q3_cleared"] is None
    assert missing["direct_h6_supplied"] is False
    assert zero["direct_h6_supplied"] is True
    assert zero["combined_q3_cleared"] is not None
    with pytest.raises(ValueError):
        carrier_word("PVDVP")


def test_direct_h6_can_cancel_simple_pole_but_not_the_remaining_shapes():
    kappa = sp.Rational(h4_support()["R"]) ** 2 / sp.Rational(5, 612)
    direct = reduce_support({"R": -kappa / 2})
    numerator = sp.expand(Q**2 * direct + sum(mixing_terms().values()))
    assert numerator == kappa * (4 * E2**2 - 3 * Q * E3).expand()
    assert sp.rem(numerator, Q**2, Q) == numerator


def test_single_face_energies_against_independent_18_word_matrix_assembly():
    # Exact SU(3) fusion adjacency in an independently built finite character
    # matrix. Three interaction steps reach every intermediate irrep that a
    # closed six-step history can visit. No numerical diagonalization.
    def images(rep, odd):
        p, q = rep
        out = {}
        for dest in [
            (p + 1, q),
            (p - 1, q + 1),
            (p, q - 1),
            (p, q + 1),
            (p + 1, q - 1),
            (p - 1, q),
        ]:
            r, s = dest
            if r < 0 or s < 0 or (odd and r == s):
                continue
            sign = 1 if odd and r < s else -1
            key = (s, r) if odd and r < s else (r, s)
            out[key] = out.get(key, 0) + sign
        return out

    for odd in (False, True):
        target = (1, 0) if odd else (0, 0)
        reached = {target}
        for _ in range(3):
            reached |= {r for s in list(reached) for r, c in images(s, odd).items() if c}
        reps = [target] + sorted(reached - {target})
        v = sp.Matrix([[images(b, odd).get(a, 0) for b in reps] for a in reps])
        assert v == v.T
        energies = [sp.Rational(2 * (p * p + p * q + q * q + 3 * p + 3 * q), 3) for p, q in reps]
        e0 = energies[0]
        d = sp.diag(0, *[1 / (e0 - e) for e in energies[1:]])
        p = sp.diag(1, *([0] * (len(reps) - 1)))
        a = v[0, 0]
        v = v - a * sp.eye(len(reps))
        evaluated = evaluate_words(folded_series()["hermitian"][6], {"P": p, "D": d, "V": v})[0, 0]
        assert evaluated == single_plaquette_series(odd=odd)["energies"][6]
    assert single_plaquette_series()["energies"][6] == Fraction(407, 702464)


def test_arbitrary_h5_and_carrier_preserving_h3_do_not_enter_lambda6():
    # An independent coefficient recurrence for H_eff/u^2 through u^4.
    h0 = sp.diag(0, 7, 7)
    h = [
        h0,
        sp.diag(2, 11, 13),
        sp.Matrix([[3, 2, -5], [2, 4, 1], [-5, 1, 6]]),
        sp.Matrix([[17, 31, -19], [31, 23, 29], [-19, 29, -7]]),
        sp.Matrix([[41, -2, 5], [-2, 7, 11], [5, 11, -3]]),
    ]
    v = [sp.Matrix([1, 0, 0])]
    energy = [sp.S.Zero]
    for n in range(1, 5):
        rhs = sum((h[j] * v[n - j] for j in range(1, n + 1)), sp.zeros(3, 1))
        energy.append(rhs[0])
        rhs -= sum((energy[j] * v[n - j] for j in range(1, n + 1)), sp.zeros(3, 1))
        assert rhs[0] == 0
        v.append(sp.Matrix([0, -rhs[1] / 7, -rhs[2] / 7]))
    assert energy[4] == 41 - sp.Rational(2**2 + 5**2, 7)


def test_exact_reduction_refuses_float_weights():
    with pytest.raises(TypeError, match="floating-point"):
        reduce_support({"RUR": 0.1})
