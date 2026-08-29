from __future__ import annotations

from sympy import (
    Rational,
    expand,
    series,
    simplify,
    sqrt,
    symbols,
)

from .. import constants as K
from ._core import _suite

# ==========================================================================
string_tension = _suite("native string tension through fifth order (v4.3 §11.2)")


@string_tension.check("sigma_n^phys = (-1)^n sigma_n^raw, and C5 is the n = 3 case", "§11.2 / C5")
def _():
    # C5 recorded "-61/408 (the earlier +61/408 was an odd-order convention
    # error)" without saying which rule produced it. R14 states the rule; this
    # check is that C5's number is what the rule gives at n = 3.
    raw_3 = -K.SIGMA_3
    phys_3 = (-1) ** 3 * raw_3
    return (
        phys_3 == K.SIGMA_3
        and raw_3 == Rational(61, 408)
        and K.SIGMA_5_RAW == -K.SIGMA_5
        and K.SIGMA_5 < 0
    ), (
        f"sigma_3^raw = +{raw_3} -> sigma_3^phys = {phys_3}, exactly C5's "
        f"correction; sigma_5^raw = +{K.SIGMA_5_RAW} -> sigma_5^phys = {K.SIGMA_5}, "
        "so both odd physical coefficients are negative"
    )


@string_tension.check("the even coefficients are not sign-flipped", "§11.2")
def _():
    # A rule applied to the wrong parity is the classic way this erratum comes
    # back. (-1)^n is +1 at n = 2 and n = 4, so those printed signs are the raw
    # signs and must be left alone.
    return all((-1) ** n == 1 for n in (2, 4)) and K.SIGMA_2 < 0 and K.SIGMA_4 < 0, (
        f"sigma_2 = {K.SIGMA_2} and sigma_4 = {K.SIGMA_4} are negative in BOTH "
        "conventions; only odd n flips"
    )


@string_tension.check("sigma_4 shares the historical-branch denominator", "§11.2 / §6")
def _():
    # Same 7250590288602460800 as q_band^(4). Both are historical-branch fourth
    # order, so this is a provenance fingerprint, not a coincidence -- and it is
    # the reason sigma_4 inherits whatever the fourth-order kernel dispute
    # settles on.
    return K.SIGMA_4.q == K.Q_BAND_4.q, (
        f"sigma_4 and q_band^(4) both have denominator {K.SIGMA_4.q}; "
        f"q_band^(4)/sigma_4 = {K.Q_BAND_4 / K.SIGMA_4}"
    )


@string_tension.check("the seven-prime CRT reconstruction clears its uniqueness bound", "§11.2")
def _():
    numerator_bits = K.SIGMA_5_RAW.p.bit_length()
    denominator_bits = K.SIGMA_5_RAW.q.bit_length()
    bound = K.SIGMA_5_MODULUS_BITS // 2
    return (
        numerator_bits == 77
        and denominator_bits == 81
        and bound == K.SIGMA_5_UNIQUENESS_BITS
        and max(numerator_bits, denominator_bits) < bound
    ), (
        f"189-bit modulus gives a {bound}-bit rational-reconstruction bound; the "
        f"recovered numerator is {numerator_bits} bits and the denominator "
        f"{denominator_bits} bits, so the pair is the unique preimage"
    )


@string_tension.check("the ratio and sigma series reproduce E_flat exactly", "§11.2 vs §4.4")
def _():
    # The strongest thing in §11.2, and it is not stated there. Two independent
    # routes meet:
    #   §11.2 gives sigma(u) and m/sqrt(sigma) = sqrt(6)(4/3 + u/2 + 11/68 u^2
    #         - 7559/499392 u^3 + O(u^4));
    #   §4.4 gives E_flat(u) = 8/3 + u + 11/306 u^2 + D_3 u^3 from the C-even /
    #         C-odd hopping ledger, with D_3 = 7/32 + 12 leak_3 - 4 b_3.
    # Multiplying the first two recovers the third term by term, D_3 included.
    # Nothing was fitted: the ratio coefficients and sigma come from the string
    # sector, D_3 from the mass sector.
    coupling = symbols("u", positive=True)
    sigma = K.SIGMA_0 + sum(
        c * coupling**n for n, c in ((2, K.SIGMA_2), (3, K.SIGMA_3), (4, K.SIGMA_4), (5, K.SIGMA_5))
    )
    ratio = sqrt(6) * sum(c * coupling**n for n, c in enumerate(K.RATIO_UNDISPUTED))
    recovered = series(ratio * sqrt(sigma), coupling, 0, 4).removeO()
    expected = K.e_flat(coupling)
    residual = simplify(expand(recovered - expected))
    coefficients = [simplify(recovered.coeff(coupling, n)) for n in range(4)]
    return residual == 0, (
        f"sqrt(6) * ratio(u) * sqrt(sigma(u)) = {coefficients} through u^3, which "
        f"is E_flat term by term: 8/3, 1, 11/306, and D_3 = {K.D_3}. The u^3 "
        "coefficient is the discriminating one -- a normalization slip anywhere in "
        "either series would not land on it"
    )


@string_tension.check("m_{1+-}(0) = 8/3 follows from sigma(0) = 2/3 alone", "§11.2")
def _():
    # The constant term separately, because it is the one an eye can check:
    # sqrt(6) * (4/3) * sqrt(2/3) = 8/3, the free one-plaquette energy.
    leading = simplify(sqrt(6) * K.RATIO_UNDISPUTED[0] * sqrt(K.SIGMA_0))
    return leading == Rational(8, 3), (
        f"sqrt(6) * {K.RATIO_UNDISPUTED[0]} * sqrt({K.SIGMA_0}) = {leading}, the "
        "u -> 0 flat-band energy; the ratio's constant term is fixed by sigma(0), "
        "not free"
    )


@string_tension.check("the ratio series stops before the disputed order", "§11.2 / C2")
def _():
    # Four coefficients, ending at u^3. The u^4 term is withheld because it
    # inherits C2, not because it is unknown -- and the check above shows the
    # first four are tightly constrained, so the omission is load-bearing.
    return len(K.RATIO_UNDISPUTED) == 4, (
        f"the quoted ratio is sqrt(6) * {K.RATIO_UNDISPUTED} through u^3; C2 "
        "reaches every higher coefficient through the fourth-order mass kernel"
    )
