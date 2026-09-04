"""The third engine at every rank: the fourth-order cluster cumulants as functions of N.

``workhouse.loopcalc`` needs no SU(3) table once the single-link spectra come
from the block characteristic polynomial (``link_spectrum``), so the same
cumulants the 2026-09-04 run computed at N = 3 can be computed at any rank.
The run record ``runs/rank_sweep_cumulants_2026-09-04`` holds them for
N = 3..70 in the kernel's (0,2) basis; the checks here recompute the cheap
ranks live and read the pinned certificate for the rest.

Two kinds of statement. First, the engine against what the corpus already
holds at every rank: the second-order hopping ``t_N`` and C-even hopping
``ell_N``, the leak = hop identity in both sectors, and the cube-completion
closed forms ``-160/(N(N^2-1)^3)`` and ``-106/(N(N^2-1)^3)``. Second, what
the corpus does not hold: rational functions of N for the two-hop weight and
the three dressing classes, reconstructed from the swept ranks and verified
on the ranks left out of the fit. A reconstructed form is exact if the true
function is rational of no higher degree than the fit -- which it is, being
a finite sum of products of Casimir differences and Weingarten values -- but
the degree bound is not proved here, so each form is recorded as verified at
every swept rank with the held-out count in its detail, and its symbolic
form is yielded for the catalogue.
"""

from __future__ import annotations

import json
from fractions import Fraction

from sympy import Rational, Symbol, cancel, factor

from .. import constants as K
from .. import loopcalc as LC
from ._core import ROOT, _suite

rank = _suite("the third engine at every rank (all-rank cumulants)")

_RUN = "runs/rank_sweep_cumulants_2026-09-04"
_CITE = "G14; C2; R2; MASTER_THEORY §4.1-4.2, §5; " + _RUN + "; ADR 0024"
_P = ((0, 1), (0, 0, 0))
_Q02 = ((0, 2), (0, 0, 0))
_N = Symbol("N")


def _certificate() -> dict:
    return json.loads((ROOT / _RUN / "certificate.json").read_text(encoding="utf-8"))


def _rat(x) -> Fraction:
    return Fraction(x.p, x.q)


def _at_rank(n, fn):
    """Run fn() with the engine switched to SU(n), restoring SU(3) afterwards."""
    LC.set_rank(n)
    try:
        return fn()
    finally:
        LC.set_rank(3)


_SECOND_ORDER = (
    "the third engine reproduces the all-rank second-order hopping t_N and C-even hopping ell_N, "
    "and leak = hop in both sectors, at N = 3..7 live and N = 3..70 pinned"
)


@rank.check(_SECOND_ORDER, _CITE + "; THM_FLUX Prop. 2; ADR 0023")
def _():
    # Live at N = 3..7: the coplanar shared-link hop is -t_N (the incidence -1
    # of S_sq), the perpendicular one +t_N, the C-even hop ell_N, and both raw
    # leakages equal ell_N - 1/C_F -- the identity ADR 0023 derived at N = 3,
    # here at every rank the engine reaches. The certificate extends the same
    # equalities to N = 40 against the registered all-rank formulas.
    def second(n):
        single = LC.Cluster([_P])
        pair = LC.Cluster([_P, ((0, 1), (1, 0, 0))])
        perp = LC.Cluster([_P, _Q02])
        h2s, _ = single.second_order()
        h2, _ = pair.second_order()
        h2p, _ = perp.second_order()
        return (
            LC.codd(h2, 0, 1),
            LC.codd(h2p, 0, 1),
            LC.ceven(h2, 0, 1),
            LC.codd(h2, 0, 0) - LC.codd(h2s, 0, 0),
            LC.ceven(h2, 0, 0) - LC.ceven(h2s, 0, 0),
        )

    live_ok = True
    for n in range(3, 8):
        hop, hop_p, hop_e, leak_o, leak_e = _at_rank(n, lambda n=n: second(n))
        t_n, ell_n, inv_cf = (
            _rat(K.hopping(n)),
            _rat(K.even_hopping(n)),
            1 / _rat(K.casimir_fundamental(n)),
        )
        live_ok = live_ok and hop == -t_n and hop_p == t_n and hop_e == ell_n
        live_ok = live_ok and leak_o == leak_e == ell_n - inv_cf
    cert = _certificate()["ranks"]
    pinned_ok = True
    for n_str, row in cert.items():
        n = int(n_str)
        t_n, ell_n, inv_cf = (
            _rat(K.hopping(n)),
            _rat(K.even_hopping(n)),
            1 / _rat(K.casimir_fundamental(n)),
        )
        pinned_ok = (
            pinned_ok and Fraction(row["hop_odd"]) == -t_n and Fraction(row["hop_perp_odd"]) == t_n
        )
        pinned_ok = pinned_ok and Fraction(row["hop_even"]) == ell_n
        pinned_ok = (
            pinned_ok
            and Fraction(row["leak_odd_raw"]) == Fraction(row["leak_even_raw"]) == ell_n - inv_cf
        )
    ok = live_ok and pinned_ok and len(cert) == 68 and set(map(int, cert)) == set(range(3, 71))
    return ok, (
        "live N = 3..7 and pinned N = 3..70: coplanar hop = -t_N = "
        "-2N(N^2-4)/((N^2-1)(2N^2-1)(4N^2-9)), perpendicular hop = +t_N, C-even hop = ell_N = "
        "-2N(3N^2-5)/(same), and the raw leakage in BOTH sectors = ell_N - 1/C_F at every rank "
        "(-481/612 at N = 3, the superseded t_+). The all-rank second order, from the third "
        "engine, with the leak = hop identity of ADR 0023 now at every rank"
    )


_CUBE_RANKS = (
    "the cube-completion closed forms hold with the full H0 dynamics at N = 4 and 5: "
    "-160/(N(N^2-1)^3) opposite, -106/(N(N^2-1)^3) adjacent"
)


@rank.check(
    _CUBE_RANKS,
    _CITE + "; runs/g3_corner_third_implementation_2026-09-04",
    rests_on=(
        "the adjacent-face cube completion is -106/(N(N^2-1)^3): the primitive -88 plus ten "
        "multi-loop histories at -18",
        "the cube completion from the third engine: -5/48 between opposite faces, -53/768 between "
        "adjacent ones",
    ),
)
def _():
    # The multi-loop model's selection rule (every doubly covered cube link is
    # forced into the singlet) is rank-independent; here the third engine,
    # which projects nothing by hand, returns the closed forms at two more ranks.
    others_perp = [
        ((0, 1), (0, 0, 1)),
        ((0, 2), (0, 1, 0)),
        ((1, 2), (0, 0, 0)),
        ((1, 2), (1, 0, 0)),
    ]
    others_norm = [
        ((0, 2), (0, 0, 0)),
        ((0, 2), (0, 1, 0)),
        ((1, 2), (0, 0, 0)),
        ((1, 2), (1, 0, 0)),
    ]
    got = {}
    for n in (4, 5):

        def both():
            adj = LC.cube_completion(_P, _Q02, others_perp)
            opp = LC.cube_completion(_P, ((0, 1), (0, 0, 1)), others_norm)
            return LC.block_odd(adj), LC.block_even(adj), LC.block_odd(opp), LC.block_even(opp)

        got[n] = _at_rank(n, both)
    ok = all(
        got[n][0] == got[n][1] == Fraction(-106, n * (n * n - 1) ** 3)
        and got[n][2] == got[n][3] == Fraction(-160, n * (n * n - 1) ** 3)
        for n in got
    )
    return ok, (
        f"N = 4: adjacent {got[4][0]} = -106/(4*15^3), opposite {got[4][2]} = -160/(4*15^3); "
        f"N = 5: adjacent {got[5][0]} = -106/(5*24^3), opposite {got[5][2]} = -160/(5*24^3); "
        "C-odd and C-even equal in the (0,2) basis at both ranks"
    )


@rank.check(
    "the rank sweep's N = 3 row is the registered SU(3) cumulants, sign and magnitude, in the "
    "kernel's basis",
    _CITE,
    rests_on=(
        "the corner cluster's cumulant from a third implementation, independent of the engine "
        "in every primitive",
    ),
)
def _():
    row = _certificate()["ranks"]["3"]
    ok = (
        Fraction(row["u_odd"]) == _rat(K.X_QUANTUM)
        and Fraction(row["u_even"]) == Fraction(948253471, 40327601932800)
        and Fraction(row["corner_odd"]) == Fraction(2580244782961, 398756546697600)
        and Fraction(row["corner_even"]) == Fraction(-56022878647, 4153714028100)
        and Fraction(row["single_odd"]) == Fraction(385, 1997568)
        and Fraction(row["fan_odd"]) == Fraction(-135671797, 105250609440)
    )
    return ok, (
        "u = X_QUANTUM, u_even, the corner, single-contact and fan dressings at N = 3 in the "
        "pinned sweep equal the registered values (the perpendicular-pair dressings with the "
        "(0,2) sign)"
    )


def _closed_form_check(key: str, expr, live_rank: int, live_fn):
    """Every pinned rank against the closed form, one rank recomputed live."""
    cert = _certificate()["ranks"]
    pinned = all(
        Rational(Fraction(row[key]).numerator, Fraction(row[key]).denominator)
        == expr.subs(_N, int(n))
        for n, row in cert.items()
    )
    live = _at_rank(live_rank, live_fn)
    live_ok = Rational(live.numerator, live.denominator) == expr.subs(_N, live_rank)
    return pinned and live_ok, len(cert)


_SINGLE_N = (
    "the single-contact dressing at every rank: C-odd 2N^3(N^2-4)(10N^2-13)/((N^2-1)^3(4N^2-9)^2"
    "(2N^2-1)^2), C-even -ell_N^2/(2C_F)"
)


@rank.check(
    _SINGLE_N,
    _CITE,
    rests_on=(
        _SECOND_ORDER,
        "the rank sweep's N = 3 row is the registered SU(3) cumulants, sign and magnitude, in the "
        "kernel's basis",
    ),
)
def _():
    # Reconstructed from the ranks 3..24 as a rational function of degree
    # (7, 14) and verified on every remaining swept rank. The C-even form is
    # minus the C-even hop squared over the plaquette rest energy 2 C_F: the
    # dressing of a shared-link pair by a plaquette touching one of them is,
    # in the C-even sector, a second-order process of the second-order hop.
    n = _N
    den = (n**2 - 1) ** 3 * (4 * n**2 - 9) ** 2 * (2 * n**2 - 1) ** 2
    odd = 2 * n**3 * (n**2 - 4) * (10 * n**2 - 13) / den
    even = -4 * n**3 * (3 * n**2 - 5) ** 2 / den
    ell = -2 * n * (3 * n**2 - 5) / ((n**2 - 1) * (4 * n**2 - 9) * (2 * n**2 - 1))
    two_cf = (n**2 - 1) / n
    identity = cancel(even + ell**2 / two_cf) == 0

    def live():
        w = LC.cumulant([_P, ((0, 1), (1, 0, 0)), _Q02], 1)
        return LC.block_odd(w), LC.block_even(w)

    got = _at_rank(4, live)
    ok_odd, count = _closed_form_check("single_odd", odd, 4, lambda: got[0])
    ok_even, _c = _closed_form_check("single_even", even, 4, lambda: got[1])
    ok = ok_odd and ok_even and identity
    return (
        ok,
        (
            f"C-odd {factor(odd)} and C-even {factor(even)} hold at every pinned rank "
            f"({count} ranks, N = 3..{2 + count}) and live at N = 4 ({got[0]}, {got[1]}); the "
            "C-even form is "
            "-ell_N^2/(2 C_F) identically in N"
        ),
        {"SINGLE_CONTACT_DRESSING_ODD_N": odd, "SINGLE_CONTACT_DRESSING_EVEN_N": even},
    )


_FAN_N = (
    "the shared-link fan dressing at every rank: a (17, 24) rational function of N with "
    "denominator 3(N^2-1)^3(4N^2-9)^3(2N^2-1)^3(16N^2-9)(16N^2-49)(4N^2-7), verified on "
    "held-out ranks"
)


@rank.check(_FAN_N, _CITE, rests_on=(_SECOND_ORDER, _SINGLE_N))
def _():
    # The three plaquettes on one link. Reconstructed from the ranks 3..44
    # (42 unknowns) and verified on every remaining swept rank at fit time;
    # here checked at every pinned rank and live at N = 4. The denominator
    # carries, beyond the single-contact dressing's factors, the linear ones
    # 4N +- 3 and 4N +- 7 -- resolvents of states where the shared link holds
    # three fluxes -- and 4N^2 - 7, the two-hop weight's own factor.
    n = _N
    den = (
        3
        * (n**2 - 1) ** 3
        * (4 * n**2 - 9) ** 3
        * (2 * n**2 - 1) ** 3
        * (16 * n**2 - 9)
        * (16 * n**2 - 49)
        * (4 * n**2 - 7)
    )
    odd_num = (
        -8
        * n**3
        * (n**2 - 4)
        * (
            363008 * n**12
            - 3144224 * n**10
            + 10850888 * n**8
            - 19034572 * n**6
            + 17764505 * n**4
            - 8272521 * n**2
            + 1496394
        )
    )
    even_num = (
        4
        * n**3
        * (
            2436096 * n**14
            - 28356544 * n**12
            + 136919408 * n**10
            - 353461224 * n**8
            + 522359998 * n**6
            - 437018150 * n**4
            + 189317052 * n**2
            - 32620563
        )
    )
    odd, even = odd_num / den, even_num / den

    def live():
        w = LC.cumulant([_P, ((0, 1), (0, -1, 0)), _Q02], 1)
        return LC.block_odd(w), LC.block_even(w)

    got = _at_rank(4, live)
    ok_odd, count = _closed_form_check("fan_odd", odd, 4, lambda: got[0])
    ok_even, _c = _closed_form_check("fan_even", even, 4, lambda: got[1])
    at3 = (odd.subs(n, 3), even.subs(n, 3))
    ok = (
        ok_odd
        and ok_even
        and at3 == (Rational(-135671797, 105250609440), Rational(2218032743, 421002437760))
    )
    return (
        ok,
        (
            f"C-odd and C-even fan forms hold at every pinned rank ({count} ranks) and live at "
            "N = 4 "
            f"({got[0]}, {got[1]}); at N = 3 they are the registered -135671797/105250609440 and "
            f"2218032743/421002437760. Numerators: C-odd -8N^3(N^2-4)(363008N^12 - ... + 1496394), "
            "C-even 4N^3(2436096N^14 - ... - 32620563)"
        ),
        {"FAN_DRESSING_ODD_N": cancel(odd), "FAN_DRESSING_EVEN_N": cancel(even)},
    )


def _poly(n, coeffs):
    """sum_k c_k n^(2k) from the constant term up: even polynomials in N."""
    return sum(c * n ** (2 * k) for k, c in enumerate(coeffs))


_U_N = (
    "the two-hop weight u at every rank: (21, 28) rational functions of N in both sectors, "
    "C-odd with the double zero (N^2-4)^2 at SU(2), verified on 16 held-out ranks"
)


@rank.check(_U_N, _CITE + "; ADR 0020", rests_on=(_SECOND_ORDER, _SINGLE_N))
def _():
    # The one dynamical input of the Hodge form (ADR 0019), the two-hop chain
    # cumulant, as a function of N: reconstructed from the ranks 3..52 (50
    # unknowns) and verified on 16 held-out ranks at fit time; checked here at
    # every pinned rank and live at N = 4. New denominator factors beyond the
    # dressings': 9N^2-16, 2N^2-3, 3N^2-2 and the pair 4N^2 -+ N - 4. The
    # C-odd numerator carries (N^2-4)^2: u vanishes doubly at the excluded
    # rank, where t_N vanishes once.
    n = _N
    den = (
        2
        * (n**2 - 1) ** 3
        * (4 * n**2 - 9) ** 3
        * (9 * n**2 - 16)
        * (2 * n**2 - 3)
        * (2 * n**2 - 1) ** 3
        * (3 * n**2 - 2)
        * (4 * n**2 - n - 4)
        * (4 * n**2 + n - 4)
    )
    odd = (
        n**3
        * (n**2 - 4) ** 2
        * _poly(n, [-54216, 313093, -771029, 1058410, -882908, 451352, -131616, 16896])
        / den
    )
    even = (
        n**3
        * _poly(
            n,
            [
                -1344384,
                9087856,
                -26524096,
                43647845,
                -44383661,
                28765162,
                -11840636,
                2995992,
                -433184,
                29184,
            ],
        )
        / den
    )

    def live():
        w = LC.cumulant([_P, ((0, 1), (1, 0, 0)), ((0, 1), (2, 0, 0))], 1)
        return LC.block_odd(w), LC.block_even(w)

    got = _at_rank(4, live)
    ok_odd, count = _closed_form_check("u_odd", odd, 4, lambda: got[0])
    ok_even, _c = _closed_form_check("u_even", even, 4, lambda: got[1])
    x = _rat(K.X_QUANTUM)
    ok = (
        ok_odd
        and ok_even
        and odd.subs(n, 3) == Rational(x.numerator, x.denominator)
        and even.subs(n, 3) == Rational(948253471, 40327601932800)
    )
    return (
        ok,
        (
            f"u_odd(N) and u_even(N) hold at every pinned rank ({count} ranks) and live at N = 4 "
            f"({got[0]}, {got[1]}); at N = 3 they are X_QUANTUM and u_even. Denominator "
            "2(N^2-1)^3(4N^2-9)^3(9N^2-16)(2N^2-3)(2N^2-1)^3(3N^2-2)(4N^2-N-4)(4N^2+N-4); C-odd "
            "numerator N^3(N^2-4)^2(16896N^14 - ... - 54216), C-even N^3(29184N^18 - ... - 1344384)"
        ),
        {"TWO_HOP_WEIGHT_ODD_N": cancel(odd), "TWO_HOP_WEIGHT_EVEN_N": cancel(even)},
    )


_CORNER_N = (
    "the corner dressing at every rank: (23, 30) rational functions of N in both sectors, "
    "verified on 12 held-out ranks"
)


@rank.check(_CORNER_N, _CITE, rests_on=(_SECOND_ORDER, _SINGLE_N, _FAN_N))
def _():
    # The cluster that decided C2 (ADR 0024), at every rank. Reconstructed
    # from the ranks 3..56 (54 unknowns), verified on 12 held-out ranks at
    # fit time; checked here at every pinned rank and live at N = 4. Its
    # denominator adds 4N^2-1, 9N^2-25, 3N^2-1, 4N^2-5 and the pair
    # 4N^2 -+ 2N - 5 to the dressings' common factors.
    n = _N
    den = (
        (n**2 - 1) ** 3
        * (4 * n**2 - 9) ** 3
        * (4 * n**2 - 1)
        * (9 * n**2 - 25)
        * (2 * n**2 - 1) ** 3
        * (3 * n**2 - 1)
        * (4 * n**2 - 5)
        * (4 * n**2 - 2 * n - 5)
        * (4 * n**2 + 2 * n - 5)
    )
    odd = (
        16
        * n**3
        * (n**2 - 4)
        * _poly(
            n,
            [
                -7465875,
                69464470,
                -275614672,
                611821212,
                -837251963,
                732994774,
                -411323454,
                143075272,
                -28088736,
                2379648,
            ],
        )
        / den
    )
    even = (
        -4
        * n**3
        * _poly(
            n,
            [
                119693925,
                -1145987952,
                4725387671,
                -11055425976,
                16270850000,
                -15779823732,
                10254591256,
                -4433035640,
                1227530272,
                -197840512,
                14175744,
            ],
        )
        / den
    )

    def live():
        w = LC.cumulant([_P, ((1, 2), (1, 0, 0)), _Q02], 1)
        return LC.block_odd(w), LC.block_even(w)

    got = _at_rank(4, live)
    ok_odd, count = _closed_form_check("corner_odd", odd, 4, lambda: got[0])
    ok_even, _c = _closed_form_check("corner_even", even, 4, lambda: got[1])
    ok = (
        ok_odd
        and ok_even
        and odd.subs(n, 3) == Rational(2580244782961, 398756546697600)
        and even.subs(n, 3) == Rational(-56022878647, 4153714028100)
    )
    return (
        ok,
        (
            f"corner forms hold at every pinned rank ({count} ranks) and live at N = 4 ({got[0]}, "
            f"{got[1]}); at N = 3 they are the registered +2580244782961/398756546697600 and "
            "-56022878647/4153714028100 (the (0,2) basis). Denominator "
            "(N^2-1)^3(4N^2-9)^3(4N^2-1)(9N^2-25)(2N^2-1)^3(3N^2-1)(4N^2-5)(4N^2-2N-5)(4N^2+2N-5)"
        ),
        {"CORNER_DRESSING_ODD_N": cancel(odd), "CORNER_DRESSING_EVEN_N": cancel(even)},
    )
