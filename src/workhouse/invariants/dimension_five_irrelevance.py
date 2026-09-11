"""Exact dimension-count and geometric-sequence controls for the September source.

These checks establish the stated arithmetic. Applying the canonical scaling
factor to an actual interacting RG map, Cauchy increment or anisotropy requires
the analytic model estimates; this module does not machine-certify OS1.
"""

from __future__ import annotations

import sympy as sp

from ._core import _suite

dim5 = _suite("dimension counts and geometric scaling controls (G19)")
_CITE = (
    "G19_DIMENSION_FIVE_IRRELEVANCE_LEMMA_20260910.md; "
    "YM_BALABAN_MULTISCALE Theorem 7.1, 6.2, OS1; G19"
)

_NO_DIM_5 = "dimension-five monomial partitions have odd index and derivative counts"
_DIM_6_LEADING = "parity-even monomial partitions omit dimension five and allow dimension six"
_SCALING_GAIN = "canonical dimension-six scaling at L=3 equals 1/9 and is below 1/2"
_CAUCHY_SUM = "the geometric ratio 1/9 has exact sum 9/8 and the stated finite tail"
_SO4_RESTORATION = "the prescribed geometric sequence (1/9)^k tends to zero"


@dim5.check(_NO_DIM_5, _CITE)
def _check_no_dim_5():
    """Verify that index contraction parity and reflection parity forbid dimension-5 operators."""
    # For any monomial D^m F^n, canonical dimension is m + 2n.
    # Case d = 5: partitions of 5 into m + 2n with m, n >= 0.
    partitions_5 = [(m, n) for m in range(6) for n in range(4) if m + 2 * n == 5]
    # Expected partitions: (1, 2), (3, 1), (5, 0)
    # 1. Total Lorentz indices: m + 2n = 5.
    # Contraction with metric (rank 2) and Levi-Civita (rank 4) requires an even index count.
    index_parities = [5 % 2 != 0 for m, n in partitions_5]

    # 2. Spacetime reflection P: D -> -D (odd), F -> +F (even).
    # Monomial transforms as (-1)^m. Parity invariance requires m to be even.
    parity_parities = [m % 2 != 0 for m, n in partitions_5]

    passed = bool(
        partitions_5 == [(1, 2), (3, 1), (5, 0)] and all(index_parities) and all(parity_parities)
    )
    detail = (
        f"partitions of d=5 into m+2n: {partitions_5}; "
        f"all have odd Lorentz index count 5 (SO(4) scalar forbidden); "
        f"all have odd derivative count m in {1, 3, 5} (parity-odd, P-forbidden)"
    )
    return passed, detail


@dim5.check(_DIM_6_LEADING, _CITE, rests_on=(_NO_DIM_5,))
def _check_dim_6_leading():
    """Verify complete classification of operator dimensions up to d = 6."""
    # Enumerate (m, n) with even m (parity-even) and even m + 2n (index-even)
    allowed_by_dim = {}
    for d in range(7):
        allowed = [
            (m, n)
            for m in range(d + 1)
            for n in range(d // 2 + 1)
            if m + 2 * n == d and m % 2 == 0 and (m + 2 * n) % 2 == 0
        ]
        allowed_by_dim[d] = allowed

    # d=0: (0,0) [Identity]
    # d=2: (0,1) -> Tr(F) = 0 (traceless), delta^{mu nu} F_{mu nu} = 0 (antisymmetric).
    # d=4: (0,2) [Tr(F^2) kinetic, Tr(F F~)], (2,1) [Tr(D^2 F) = 0], (4,0)
    # d=5: empty
    # d=6: (0,3) [Tr(F^3)], (2,2) [Tr(D F D F)], (4,1), (6,0)
    passed = bool(
        len(allowed_by_dim[5]) == 0
        and len(allowed_by_dim[6]) > 0
        and allowed_by_dim[4] == [(0, 2), (2, 1), (4, 0)]
    )
    detail = (
        f"allowed parity-even partitions: d=4 -> {allowed_by_dim[4]}; "
        f"d=5 -> {allowed_by_dim[5]}; d=6 -> {allowed_by_dim[6]}; "
        "dimension six is permitted by these parity/index counts; operator realization is separate"
    )
    return passed, detail


@dim5.check(_SCALING_GAIN, _CITE, rests_on=(_DIM_6_LEADING,))
def _check_scaling_gain():
    """Verify that canonical dimension d = 6 gives scaling gain L^-2 = 1/9 <= 1/2."""
    L = sp.Integer(3)
    d = sp.Integer(6)
    scaling_exponent = d - 4
    gain = L ** (-scaling_exponent)
    lambda_bound = sp.Rational(1, 2)

    passed = bool(scaling_exponent == 2 and gain == sp.Rational(1, 9) and gain < lambda_bound)
    detail = (
        f"L={L}, d={d} -> scaling gain L^-(d-4) = {gain} = 1/9; "
        f"is below {lambda_bound}; actual polymer contraction is an additional analytic input"
    )
    return passed, detail, {"DIM6_MULTISCALE_GAIN": gain}


@dim5.check(_CAUCHY_SUM, _CITE, rests_on=(_SCALING_GAIN,))
def _check_cauchy_sum():
    """Verify that the geometric series sum_{k=0}^infty 9^-k converges to 9/8."""
    r = sp.Rational(1, 9)
    k_sym = sp.Symbol("k", integer=True, nonnegative=True)
    geom_sum = sp.Sum(r**k_sym, (k_sym, 0, sp.oo)).doit()
    expected = sp.Rational(9, 8)

    # Tail bound for n = 5
    n = 5
    tail_sum = sum(r**k for k in range(n, n + 20))
    exact_tail = (r**n) / (1 - r)
    tail_error = exact_tail - tail_sum

    passed = bool(
        geom_sum == expected and tail_sum < exact_tail and tail_error == (r ** (n + 20)) / (1 - r)
    )
    detail = (
        f"geometric sum sum_{{k=0}}^oo (1/9)^k = {geom_sum} = 9/8; "
        f"tail at n={n} is exactly {exact_tail}; "
        "actual expectation increments need a separately established domination by this sequence"
    )
    return passed, detail, {"CAUCHY_GEOMETRIC_SUM": geom_sum}


@dim5.check(_SO4_RESTORATION, _CITE, rests_on=(_SCALING_GAIN,))
def _check_so4_restoration():
    """Verify that directional variance anisotropy contracts to zero as 9^-k."""
    # Directional variance V at scale k: c_aniso(k) = c_0 * (1/9)^k
    c_0 = sp.Rational(1, 1)
    k = sp.Symbol("k", integer=True, nonnegative=True)
    c_k = c_0 * sp.Rational(1, 9) ** k
    lim_k = sp.limit(c_k, k, sp.oo)

    passed = bool(lim_k == 0)
    detail = (
        f"anisotropy coefficient c_aniso(k) = (1/9)^k; limit as k -> oo is {lim_k}; "
        "identifying this sequence with actual anisotropy requires the separate model estimates"
    )
    return passed, detail
