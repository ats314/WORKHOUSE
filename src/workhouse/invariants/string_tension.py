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


# --------------------------------------------------------------------------
# What monotonicity in the coupling can and cannot reach (ADR 0022).
#
# A proposal recorded 2026-09-03: a Griffiths-type inequality -- true at every
# beta, abelian because the electric-flux sectors are Z_N-valued -- that makes
# the sector free energies monotone in beta and so carries the gap from
# strong to weak coupling, the way Griffiths' inequalities carry Ising order
# across phases. The Ising argument needs the quantity to be INCREASING in
# beta: order established at beta_0 then persists above it. The three checks
# below read the direction off the certified series and find it is the other
# one at every order, so a sector-wise monotonicity, if it holds at all,
# bounds the large-beta flux gap from ABOVE and can never establish it.
# --------------------------------------------------------------------------


@string_tension.check(
    "the leading electric-flux gap C_F L / (2 sqrt u) decreases in u for every N",
    "§11.2 / ADR 0022 (G19 route)",
)
def _():
    # The zeroth-order sector gap needs no census: one unit of Z_N electric
    # flux through a straight winding line of length L charges L links in the
    # fundamental, at (g^2 / 2) C_F per link, and g^2 = u^(-1/2) in the
    # canonical coordinate. Symbolic in N, u and L rather than at N = 3, so
    # the sign is a statement about every rank and every volume.
    n, coupling, length = symbols("N u L", positive=True)
    cf = (n**2 - 1) / (2 * n)
    gap = cf * length / (2 * sqrt(coupling))
    slope = simplify(gap.diff(coupling) + cf * length / (4 * coupling ** Rational(3, 2)))
    numerator = (cf * length).as_numer_denom()[0]
    # (N - 1)(N + 1) L: every factor positive for N > 1, so the slope
    # -(N^2 - 1) L / (8 N u^(3/2)) is negative wherever the series lives
    signs = all(
        f.subs(n, 2) > 0 and f.diff(n).subs(n, 2) >= 0 for f in numerator.as_ordered_factors()
    )
    # the SU(3) instance is sigma_0 u^(-1/2) L, i.e. the same constant the
    # fifth-order series starts from
    su3 = simplify(gap.subs(n, 3) - K.SIGMA_0 * length / sqrt(coupling))
    return (
        slope == 0 and signs and su3 == 0,
        (
            f"d/du [C_F L / (2 sqrt u)] = -(N^2 - 1) L / (8 N u^(3/2)) exactly; the numerator "
            f"factors as {numerator.factor()}, positive for N >= 2, so the leading flux gap is "
            "strictly "
            f"decreasing in u (hence in beta = 6u) at every rank and volume. At N = 3 it is "
            f"sigma_0 L / sqrt u with sigma_0 = {K.SIGMA_0}, so the slope coefficient is "
            f"-{K.SIGMA_0 / 2}: the direction is fixed before any correction enters"
        ),
        {"FLUX_GAP_SLOPE_0": -K.SIGMA_0 / 2},
    )


@string_tension.check(
    "every fifth-order slope coefficient is negative, so the flux gap falls as beta grows",
    "§11.2 / ADR 0022 (G19 route)",
    rests_on=(
        "sigma_n^phys = (-1)^n sigma_n^raw, and C5 is the n = 3 case",
        "the even coefficients are not sign-flipped",
    ),
)
def _():
    # Through fifth order the one-unit flux gap per unit length is
    # T a^2 = u^(-1/2) sigma(u) = sum_n sigma_n u^(n - 1/2), and its derivative
    # is sum_n (n - 1/2) sigma_n u^(n - 3/2). The question is only the signs
    # of the slope coefficients s_n = (n - 1/2) sigma_n: with sigma_0 > 0 at
    # n = 0 and every certified sigma_n < 0 at n >= 2, every term is negative
    # on ALL of u > 0 -- so the truncated gap is decreasing on the whole
    # half-line, not merely near u = 0. Corrections make it fall faster,
    # never slower. The rests_on checks are what fix the signs of sigma_3 and
    # sigma_5; a parity slip there would flip two of the five terms.
    terms = {0: K.SIGMA_0, 2: K.SIGMA_2, 3: K.SIGMA_3, 4: K.SIGMA_4, 5: K.SIGMA_5}
    slopes = {n: (n - Rational(1, 2)) * c for n, c in terms.items()}
    negative = all(s < 0 for s in slopes.values())
    # and once more symbolically, so the exponent bookkeeping is checked too
    coupling = symbols("u", positive=True)
    gap = sum(c * coupling ** (n - Rational(1, 2)) for n, c in terms.items())
    derivative = expand(gap.diff(coupling))
    rebuilt = expand(sum(s * coupling ** (n - Rational(3, 2)) for n, s in slopes.items()))
    # the KPS bridge writes the same function as (g^2 / 2) W(x), x = 2u: same
    # derivative, so the direction is not a convention of this coordinate
    kps = expand(
        (
            sum(
                c * (2 * coupling) ** n
                for n, c in (
                    (0, K.KPS_T0),
                    (2, K.KPS_T2),
                    (3, K.KPS_T3),
                    (4, K.KPS_T4),
                    (5, K.KPS_T5),
                )
            )
            / (2 * sqrt(coupling))
        ).diff(coupling)
    )
    return (
        negative and simplify(derivative - rebuilt) == 0 and simplify(kps - derivative) == 0,
        (
            f"slope coefficients (n - 1/2) sigma_n: {slopes} -- all five negative, so "
            "d/du [u^(-1/2) sigma(u)] < 0 for every u > 0 through fifth order, and identically in "
            "the KPS coordinate x = 2u. A sector-wise monotonicity in beta, if it holds, is "
            "therefore monotone DECREASING: it bounds the weak-coupling flux gap from above by its "
            "strong-coupling value and cannot bound it from below"
        ),
        {"SIGMA_SLOPE_2": slopes[2]},
    )


@string_tension.check(
    "a weight u^k, k >= 1, flips the small-u direction: the sign is the weight's, not evidence",
    "§11.2 / ADR 0022 (G19 route)",
)
def _():
    # The obvious repair -- multiply the gap by a power of the coupling so it
    # increases -- succeeds at small u for every k >= 1, because the leading
    # slope becomes (k - 1/2) sigma_0 > 0. That is exactly why it proves
    # nothing: the direction at small u is chosen by the weight, and whether
    # the weighted quantity keeps increasing at large u is the continuum
    # question itself (G19's necessary law sends the lattice gap to zero
    # faster than any power of u). Recorded so the repair is not re-proposed.
    coupling = symbols("u", positive=True)
    leading = K.SIGMA_0 * coupling ** Rational(-1, 2)
    small_u = {}
    for k in range(0, 4):
        weighted = expand((coupling**k * leading).diff(coupling))
        coefficient = simplify(weighted / coupling ** (k - Rational(3, 2)))
        small_u[k] = coefficient
    ok = (
        small_u[0] < 0
        and all(small_u[k] > 0 for k in (1, 2, 3))
        and all(small_u[k] == (k - Rational(1, 2)) * K.SIGMA_0 for k in small_u)
    )
    return ok, (
        f"leading slope of u^k * sigma_0 u^(-1/2) is (k - 1/2) sigma_0 = {small_u}: negative "
        "at k = 0, positive for every k >= 1. Any polynomial weight makes the small-u direction "
        "whatever one wants, so an increasing weighted gap at strong coupling carries no "
        "information about weak coupling"
    )
