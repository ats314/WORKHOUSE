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

from sympy import Rational, Symbol, cancel, factor, sympify

from .. import chain_channels as CC
from .. import constants as K
from .. import loopcalc as LC
from ._core import ROOT, _suite

rank = _suite("the third engine at every rank (all-rank cumulants)")

_RUN = "runs/rank_sweep_cumulants_2026-09-04"
_CITE = "G14; C2; R2; MASTER_THEORY §4.1-4.2, §5; " + _RUN + "; ADR 0024"
_P = ((0, 1), (0, 0, 0))
_Q02 = ((0, 2), (0, 0, 0))
_N = Symbol("N")


def sympify_form(text: str):
    return sympify(text, locals={"N": _N})


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


_CHANNEL_RUN = "runs/u_by_channel_2026-09-04"


def _channel_certificate() -> dict:
    return json.loads((ROOT / _CHANNEL_RUN / "certificate.json").read_text(encoding="utf-8"))


def _channel_forms() -> dict:
    return json.loads(
        (ROOT / _CHANNEL_RUN / "channel_closed_forms.json").read_text(encoding="utf-8")
    )


_U_CHANNELS = (
    "u is the sum of 74 irrep-labelled channels, each a product of resolvent factors in N, "
    "and the 74 closed forms sum to u(N) identically"
)


@rank.check(_U_CHANNELS, "G14; C2; " + _CHANNEL_RUN + "; ADR 0026; ADR 0019", rests_on=(_U_N,))
def _():
    # Every contribution to the two-hop cumulant is tagged by the irreps of
    # the links its intermediate states double -- singlet, Lambda^2, adjoint
    # or Sym^2 -- and the tag is rank-independent. The pinned run holds the
    # 58 direct and 16 fold channels at N = 3..30; the pinned reconstruction
    # holds each channel's closed form, a product of the resolvent factors
    # its irreps bring (Lambda^2: 2N-3 and 3N-4; Sym^2: 2N+3 and 3N+4; the
    # adjoint: 2N^2-1 and 3N^2-2; mixed pairs: 2N^2-3 and 4N^2 -+ N - 4).
    # Checked: every form at every pinned rank, one rank live, and the sum
    # of the 74 forms against the reconstructed u(N) symbolically.
    cert = _channel_certificate()
    forms = _channel_forms()
    n = _N
    exprs = {label: cancel(sympify_form(v["form"])) for label, v in forms.items()}
    pinned_ok = True
    for n_str, row in cert["ranks"].items():
        ch = row["coplanar"]["channels"]
        if set(ch) != set(exprs):
            pinned_ok = False
            break
        for label, val in ch.items():
            fv = Fraction(val)
            if exprs[label].subs(n, int(n_str)) != Rational(fv.numerator, fv.denominator):
                pinned_ok = False
    live = CC.decompose(CC.COPLANAR, 3)
    live_ok = {str(k) for k in live} == set(exprs) and all(
        exprs[str(k)].subs(n, 3) == Rational(v.numerator, v.denominator) for k, v in live.items()
    )
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
    u_odd = (
        n**3
        * (n**2 - 4) ** 2
        * _poly(n, [-54216, 313093, -771029, 1058410, -882908, 451352, -131616, 16896])
        / den
    )
    total = sum(exprs.values())
    sum_ok = cancel(total - u_odd) == 0
    direct = sum(1 for k in exprs if k.startswith("('direct'"))
    fold = len(exprs) - direct
    held = min(v["held_out"] for v in forms.values())
    ok = pinned_ok and live_ok and sum_ok and len(exprs) == 74 and direct == 58 and fold == 16
    return ok, (
        f"{len(exprs)} channels ({direct} direct, {fold} fold) at every pinned rank N = 3..30 and "
        f"live at N = 3; each closed form verified on at least {held} held-out ranks at "
        "reconstruction; the sum of the 74 forms minus the reconstructed u(N) is identically zero. "
        "The pure-fundamental chain channel is -4/(N(N^2-1)^3); every other channel carries the "
        "resolvent factors of its irreps"
    )


_CHAIN_TYPES = (
    "u is universal channel by channel: the coplanar, bent and in-plane L chains agree in every "
    "one of the 74 channels, up to the incidence sign, at N = 3..30"
)


@rank.check(
    _CHAIN_TYPES,
    "G14; " + _CHANNEL_RUN + "; ADR 0026; ADR 0020; THM_FLUX Prop. 2",
    rests_on=(_U_CHANNELS,),
)
def _():
    # ADR 0020 found u = X_QUANTUM on three chain types and asked why -- "a
    # question about the Haar contraction rather than the kernel". Here it
    # is answered at the finest level the calculus offers: not only the sums
    # but every irrep-labelled channel agrees between the coplanar chain, the
    # bent chain (P and R on opposite cube faces through a side face) and the
    # in-plane L chain (the connector's two shared links ADJACENT, the
    # doubled-orbit geometry of ADR 0019). The straight and bent chains carry
    # the incidence signs +1 and -1 of THM_FLUX Prop. 2; the L chain's sign
    # is that of its own two incidences.
    cert = _channel_certificate()
    ok = True
    signs = {}
    for row in cert["ranks"].values():
        cop = {k: Fraction(v) for k, v in row["coplanar"]["channels"].items()}
        for name in ("bent", "L"):
            other = {k: Fraction(v) for k, v in row[name]["channels"].items()}
            if set(other) != set(cop):
                ok = False
                continue
            ratios = {k: other[k] / cop[k] for k in cop if cop[k]}
            if len(set(ratios.values())) != 1 or set(ratios.values()) - {Fraction(1), Fraction(-1)}:
                ok = False
            signs.setdefault(name, set()).update(ratios.values())
    ok = ok and signs.get("bent") == {Fraction(-1)} and len(signs.get("L", set())) == 1
    return ok, (
        f"at every pinned rank all 74 channels of the bent chain are "
        f"{', '.join(str(x) for x in sorted(signs.get('bent', [])))} times the coplanar chain's "
        f"and all 74 of the L chain are {', '.join(str(x) for x in sorted(signs.get('L', [])))} "
        "times it: the two-hop weight is one function of N per channel, whatever the planes. What "
        "ADR 0019 called the one dynamical input of the Hodge form is a property of the Haar "
        "contraction on the abstract three-plaquette cluster"
    )


_BETA_RUN = "runs/beta_n_from_assembly_2026-09-04"


def _beta_certificate() -> dict:
    return json.loads((ROOT / _BETA_RUN / "certificate.json").read_text(encoding="utf-8"))


_PAIR_CANCELS = (
    "the coplanar and perpendicular two-face clusters are one abstract graph up to conjugating Q, "
    "so their C-odd pair elements are exact negatives at every rank and the pair cluster drops "
    "out of C_shp"
)


@rank.check(
    _PAIR_CANCELS,
    "C2; C10; " + _BETA_RUN + "; ADR 0027",
    rests_on=(_SECOND_ORDER,),
)
def _():
    # The engine's value for a cluster depends only on its abstract graph: which link
    # matrices appear, in which direction, in which face -- the Haar measure, the link
    # energies and the Fierz rewiring are all per link and invariant under relabelling a
    # link or reversing it. Here a bijection of the seven links, with reversals, is found
    # that carries the coplanar cluster's words onto the perpendicular cluster's; it must
    # conjugate an odd number of faces (the shared link is traversed oppositely by the
    # coplanar pair and in the same direction by the perpendicular one, and a reversal
    # of the shared link preserves that), and the C-odd block is odd under conjugating a
    # face. The four entries of the two pair elements are then compared under Q <-> Q-bar
    # at N = 5, live.
    from itertools import permutations, product

    def canon(word):
        (cyc,) = word
        rots = [tuple(cyc[i:] + cyc[:i]) for i in range(len(cyc))]
        return min(rots)

    def relabel(word, sigma, flip):
        (cyc,) = word
        return canon(((tuple((sigma[link], d * flip[link]) for link, d in cyc)),))

    cop = LC.Cluster([_P, ((0, 1), (1, 0, 0))])
    perp = LC.Cluster([_P, _Q02])
    links_c = sorted({link for w in cop.words for link, _ in w[0]})
    links_p = sorted({link for w in perp.words for link, _ in w[0]})
    target = {canon(w): i for i, w in enumerate(perp.words)}
    parities = set()
    for perm in permutations(links_p, len(links_c)):
        sigma = dict(zip(links_c, perm, strict=True))
        for signs in product((1, -1), repeat=len(links_c)):
            flip = dict(zip(links_c, signs, strict=True))
            images = [target.get(relabel(w, sigma, flip)) for w in cop.words]
            if None in images or len(set(images)) != 4:
                continue
            # images[i] is where the i-th word (P, P-bar, Q, Q-bar) lands; landing on an
            # odd index (P-bar or Q-bar) is a conjugation, whether or not the faces swap roles
            conjugated = (images[0] in (1, 3)) + (images[2] in (1, 3))
            parities.add(conjugated % 2)
    isomorphic = parities == {1}

    def live():
        a = LC.pair_element([_P, ((0, 1), (1, 0, 0))])
        b = LC.pair_element([_P, _Q02])
        entries = all(a[(i, j)] == b[(i, 5 - j)] for i in (0, 1) for j in (2, 3))
        return entries, LC.block_odd(a), LC.block_odd(b), LC.block_even(a), LC.block_even(b)

    entries, odd_c, odd_p, even_c, even_p = _at_rank(5, live)
    ok = isomorphic and entries and odd_c + odd_p == 0 and even_c == even_p
    return ok, (
        f"every link bijection carrying the coplanar words onto the perpendicular words conjugates "
        f"an odd number of faces (parities found: {sorted(parities)}); at N = 5 the four entries "
        f"agree under Q <-> Q-bar, C-odd blocks {odd_c} and {odd_p}, C-even blocks equal ({even_c})"
    )


_BETA_EVERY_RANK = (
    "the cluster assembly reproduces the corpus's all-rank beta_N = P17(N^2)/(N R20(N^2)) exactly "
    "at every rank N = 4..70 (the pair cluster, which cancels, computed at N >= 5), and the "
    "link-disjoint pair is zero at every rank"
)


@rank.check(
    _BETA_EVERY_RANK,
    "C2; C10; G14; R2; GLUEBALL v3.1 ~1074, ~1080-1088, Appendix A ~1490-1508; "
    + _BETA_RUN
    + "; ADR 0027",
    rests_on=(
        _PAIR_CANCELS,
        _U_N,
        _CORNER_N,
        _FAN_N,
        _SINGLE_N,
        _CUBE_RANKS,
        "FINDING: C_shp from the assembled amplitudes in the kernel's basis is C_historical + "
        "25/1024, the registered continuation-shifted value",
    ),
)
def _():
    # The corpus states beta_N "for N >= 4", output-certified by its all-rank
    # program and never re-derived. Here it is assembled from cluster cumulants
    # by an engine that reads no kernel, no engine and no corpus formula:
    #   pi = pair_cop + 18 d_cop + 2 s_cop; rho = pair_perp + 14 d_perp + 2 s_perp
    #   + 2 corner + K_adj; C = -alpha_N/8 - u - (rho + pi)/2; beta = 8A + 16C,
    # all in the kernel's (0,2) basis, with the pair cluster in the PVP = 0 form
    # (exact for N >= 4: the first-order vertex is the (3,0) determinant family).
    # Every rank in the pinned run is checked against channel_ledger.beta_formula,
    # and N = 5 is recomputed live end to end.
    from ..channel_ledger import beta_formula

    cert = _beta_certificate()["ranks"]
    pinned = all(
        Fraction(row["beta_assembled"]) == beta_formula(int(n_str)) == Fraction(row["beta_corpus"])
        and row["equal"] is True
        for n_str, row in cert.items()
    )
    # the pair cluster is computed at N >= 5 (at N = 4 its (4,0)-family PVP = 0 form is
    # infeasible and, cancelling identically, not needed); where computed, the stacked
    # pair is zero and the two shared-link pairs are negatives
    with_pair = {n_str: row for n_str, row in cert.items() if row["pair_coplanar"] is not None}
    pairs_ok = set(map(int, with_pair)) == set(range(5, 71)) and all(
        Fraction(row["pair_normal"]) == 0
        and Fraction(row["pair_coplanar"]) + Fraction(row["pair_perpendicular"]) == 0
        for row in with_pair.values()
    )
    ranks_ok = set(map(int, cert)) == set(range(4, 71)) and pairs_ok

    def live():
        P = _P
        pair_cop = LC.block_odd(LC.pair_element([P, ((0, 1), (1, 0, 0))]))
        pair_perp = LC.block_odd(LC.pair_element([P, _Q02]))
        d_cop = LC.block_odd(LC.cumulant([P, ((0, 1), (2, 0, 0)), ((0, 1), (1, 0, 0))], 1))
        s_cop = LC.block_odd(LC.cumulant([P, ((1, 2), (1, 0, 0)), ((0, 1), (1, 0, 0))], 1))
        d_perp = LC.block_odd(LC.cumulant([P, ((0, 1), (1, 0, 0)), _Q02], 1))
        s_perp = LC.block_odd(LC.cumulant([P, ((0, 1), (0, -1, 0)), _Q02], 1))
        corner = LC.block_odd(LC.cumulant([P, ((1, 2), (1, 0, 0)), _Q02], 1))
        u = LC.block_odd(LC.cumulant([P, ((0, 1), (1, 0, 0)), ((0, 1), (2, 0, 0))], 1))
        return pair_cop, pair_perp, d_cop, s_cop, d_perp, s_perp, corner, u

    n = 5
    pair_cop, pair_perp, d_cop, s_cop, d_perp, s_perp, corner, u = _at_rank(n, live)
    den = n * (n * n - 1) ** 3
    pi = pair_cop + 18 * d_cop + 2 * s_cop
    rho = pair_perp + 14 * d_perp + 2 * s_perp + 2 * corner + Fraction(-106, den)
    c = Fraction(-80, den) - u - (rho + pi) / 2
    beta_live = 8 * Fraction(160, den) + 16 * c
    live_ok = beta_live == beta_formula(5) == Fraction(cert["5"]["beta_assembled"])
    cancel_ok = pair_cop + pair_perp == 0
    ok = pinned and ranks_ok and live_ok and cancel_ok
    return ok, (
        f"beta assembled = P17(N^2)/(N R20(N^2)) at every pinned rank N = 4..70 ({len(cert)} "
        f"ranks, exact rationals; the pair cluster computed at the {len(with_pair)} ranks N >= 5); "
        f"live at N = 5: pi = {pi}, rho = {rho}, C = {c}, "
        f"beta = {beta_live} = "
        f"beta_formula(5). The stacked pair is 0 at every rank, and the coplanar and perpendicular "
        f"pair clusters are exact negatives at every rank (live at N = 5: {pair_cop} and "
        f"{pair_perp}), so the pair cluster drops out of C_shp. The corpus's 'for N >= 4' formula, "
        "output-certified and never re-derived, is now assembled from cluster cumulants by an "
        "engine that reads none of it; with ADR 0024 it holds at N = 3 too"
    )


_BETA_CLOSED_FORM = (
    "the assembled beta's closed form in N, reconstructed from 38 ranks and confirmed on the "
    "other 28, is the corpus's P17(N^2)/(N R20(N^2)) as a rational function; the pair "
    "clusters' closed forms are exact negatives with a double pole at N = 3"
)


@rank.check(
    _BETA_CLOSED_FORM,
    "GLUEBALL v3.1 Appendix A ~1490-1508 (P17, R20); C10; G14; "
    + _BETA_RUN
    + "/closed_forms.json; ADR 0027",
    rests_on=(_BETA_EVERY_RANK,),
)
def _():
    # reconstruct_beta.py finds, for each certified quantity, the lowest-degree N^s g(N^2)
    # through the first dp + dq + 1 ranks that reproduces every remaining rank. Here every
    # form is re-evaluated at every certified rank N >= 5 (the reconstruction's domain: at
    # N = 4 the (4,0) determinant family enters the pair cluster's Haar integrals and is
    # not part of the continuation), the beta form is compared with the corpus's formula
    # as a rational function, and the two pair forms are added. What this does not prove:
    # that the assembled beta is a rational function of bounded degree in N -- with that
    # bound the rank-by-rank equality would already imply the symbolic identity.
    from sympy import Rational, Symbol, cancel, limit, sympify

    from ..channel_ledger import P17, R20, _z

    N = Symbol("N")
    forms = json.loads((ROOT / _BETA_RUN / "closed_forms.json").read_text(encoding="utf-8"))
    cert = _beta_certificate()["ranks"]
    keys = (
        "pair_coplanar",
        "pair_perpendicular",
        "single_coplanar",
        "fan_coplanar",
        "C_shp",
        "beta_assembled",
    )
    expr = {k: sympify(forms[k]["form"], locals={"N": N}) for k in keys}
    every_rank = all(
        expr[k].subs(N, n) == Rational(row[k])
        for n_str, row in cert.items()
        if (n := int(n_str)) >= 5
        for k in keys
    )
    held = {k: forms[k]["held_out"] for k in keys}
    corpus = P17.as_expr().subs(_z, N**2) / (N * R20.as_expr().subs(_z, N**2))
    identity = cancel(expr["beta_assembled"] - corpus) == 0
    pair_sum = cancel(expr["pair_coplanar"] + expr["pair_perpendicular"]) == 0
    residue = limit(expr["pair_coplanar"] * (N - 3) ** 2, N, 3)
    pole = residue == Rational(5, 1088)
    ok = every_rank and identity and pair_sum and pole and forms["identity"]["holds"] is True
    return ok, (
        f"every closed form reproduces every certified rank N >= 5 (held-out ranks {held}); "
        f"beta_assembled(N) - P17(N^2)/(N R20(N^2)) = 0 as a rational function; "
        f"pair_coplanar(N) + pair_perpendicular(N) = 0 identically; the pair cluster's "
        f"continuation has a double pole at N = 3 with (N-3)^2-coefficient {residue}, which the "
        "sum pi + rho never sees. The identity is symbolic given a degree bound on the assembled "
        "beta; the rank-by-rank equality at 4..70 stands on its own"
    )
