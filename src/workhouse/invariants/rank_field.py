"""The third engine over Q(N): the closed forms derived, the degree bound proved (ADR 0029).

ADR 0025 and ADR 0027 reconstructed the fourth-order cumulants and the
assembled shape coefficient as rational functions of N from a rank sweep and
verified them on held-out ranks; the identity ``beta_N = P17(N^2)/(N R20(N^2))``
was stated as rational functions "conditional on a degree bound". Here the
engine is run over the field Q(N) itself (``workhouse.symbolic_rank``): every
cumulant comes out as one rational function of N, computed, and the degree
bound is what it is because the function is in hand. The run records are
``runs/beta_n_symbolic_rank_2026-09-04`` (the cumulants, the assembly, the
audit behind the specialisation argument) and
``runs/channels_symbolic_rank_2026-09-04`` (the same cumulants channel by
channel, for G14).

What the derivation establishes and what it does not: the closed forms are
the values the per-rank engine computes at every N >= 5, by the argument in
``symbolic_rank``'s docstring, whose premises the record certifies; at N = 3
and N = 4 the forms agree with the per-rank engine as a checked fact (a
resolvent denominator vanishes at N = 4 and the argument does not reach). The
polynomial identity itself is proved in Lean (``betaN_from_three_cumulants``).

The pinned forms are read as integer coefficient lists into ``symbolic_rank.RF``
(flint), so every comparison, ratio and sum below is exact field arithmetic in
Q(N); sympy touches only the handful of literal forms and the factoring.
"""

from __future__ import annotations

import ast
import json
from fractions import Fraction
from functools import cache
from math import gcd, lcm

import flint
from sympy import Poly, Rational, Symbol, cancel, expand, factor, sympify

from .. import loopcalc as LC
from .. import symbolic_rank as SR
from ..channel_ledger import P17, R20, _z
from ._core import ROOT, _suite

field = _suite("the third engine over Q(N): closed forms derived, the degree bound")

_BETA_RUN = "runs/beta_n_symbolic_rank_2026-09-04"
_CHANNEL_RUN = "runs/channels_symbolic_rank_2026-09-04"
_SWEEP = "runs/rank_sweep_cumulants_2026-09-04"
_ASSEMBLY = "runs/beta_n_from_assembly_2026-09-04"
_CITE = "G14; C10; R2; " + _BETA_RUN + "; ADR 0029; ADR 0027; ADR 0025"
_N = Symbol("N")
_P = ((0, 1), (0, 0, 0))
_Q02 = ((0, 2), (0, 0, 0))


@cache
def _json(rel: str) -> dict:
    return json.loads((ROOT / rel).read_text(encoding="utf-8"))


def _rf(entry: dict) -> SR.RF:
    """A pinned ``{"num": [...], "den": [...]}`` coefficient record as an element of Q(N)."""
    return SR.RF(flint.fmpq_poly(entry["num"]), flint.fmpq_poly(entry["den"]))


def _poly_of(expr) -> flint.fmpq_poly:
    return flint.fmpq_poly(
        [flint.fmpq(int(c.p), int(c.q)) for c in Poly(expr, _N).all_coeffs()[::-1]]
    )


def _rf_from_sympy(expr) -> SR.RF:
    num, den = cancel(expr).as_numer_denom()
    return SR.RF(_poly_of(num), _poly_of(den))


def _prim(coeffs) -> tuple:
    """Coefficients, constant term first, scaled to primitive integers with a positive lead."""
    fr = [Fraction(int(c.p), int(c.q)) for c in coeffs]
    m = 1
    for c in fr:
        m = lcm(m, c.denominator)
    ints = [int(c * m) for c in fr]
    while ints and ints[-1] == 0:
        ints.pop()
    g = 0
    for v in ints:
        g = gcd(g, abs(v))
    ints = [v // g for v in ints] if g else ints
    if ints and ints[-1] < 0:
        ints = [-v for v in ints]
    return tuple(ints)


def _ptuple(expr) -> tuple:
    return _prim(Poly(expr, _N).all_coeffs()[::-1])


def _pstr(t: tuple) -> str:
    return str(sum(c * _N**k for k, c in enumerate(t)))


def _den_factors(rf: SR.RF) -> set:
    """The irreducible factors of a denominator, as primitive coefficient tuples."""
    _content, facs = rf.den.factor()
    return {_prim(f.coeffs()) for f, _m in facs}


def _rat(x: Fraction) -> Rational:
    return Rational(x.numerator, x.denominator)


def _poly(n, coeffs):
    """sum_k c_k n^(2k) from the constant term up: even polynomials in N."""
    return sum(c * n ** (2 * k) for k, c in enumerate(coeffs))


# The three cumulants and the cube completion that beta_N is made of, as the
# all-rank suite records them (ADR 0025) -- restated here so that the identity
# check below is pure algebra on literal forms, which is what the Lean theorems
# prove, and so that the derivation check can compare them with the engine's
# own Q(N) output independently.
def two_hop_odd(n):
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
    return (
        n**3
        * (n**2 - 4) ** 2
        * _poly(n, [-54216, 313093, -771029, 1058410, -882908, 451352, -131616, 16896])
        / den
    )


def single_contact_odd(n):
    return (
        2
        * n**3
        * (n**2 - 4)
        * (10 * n**2 - 13)
        / ((n**2 - 1) ** 3 * (4 * n**2 - 9) ** 2 * (2 * n**2 - 1) ** 2)
    )


def corner_odd(n):
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
    return (
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


def cube_adjacent(n):
    return -106 / (n * (n**2 - 1) ** 3)


def corpus_beta(n):
    return P17.as_expr().subs(_z, n**2) / (n * R20.as_expr().subs(_z, n**2))


_DERIVED = (
    "every cumulant of the beta_N assembly is one rational function of N computed over Q(N): "
    "the closed forms are derived, not reconstructed, and specialise to the per-rank records at "
    "N = 3..70"
)


@field.check(
    _DERIVED,
    _CITE,
    rests_on=(
        "the single-contact dressing at every rank: C-odd 2N^3(N^2-4)(10N^2-13)/((N^2-1)^3"
        "(4N^2-9)^2(2N^2-1)^2), C-even -ell_N^2/(2C_F)",
        "the two-hop weight u at every rank: (21, 28) rational functions of N in both sectors, "
        "C-odd with the double zero (N^2-4)^2 at SU(2), verified on 16 held-out ranks",
        "the corner dressing at every rank: (23, 30) rational functions of N in both sectors, "
        "verified on 12 held-out ranks",
    ),
)
def _():
    # Live: the single-contact dressing of the perpendicular pair, computed
    # over Q(N) end to end (about ten seconds), against the pinned form and the
    # all-rank suite's literal form. Pinned: every form of the record, in both
    # sectors, evaluated at every rank of the two per-rank records by this
    # check rather than by the record's own claim. Two rational functions of
    # degree at most (23, 30) that agree at 68 ranks are identical, so this is
    # also the identity of the record's forms with the all-rank suite's.
    forms = _json(_BETA_RUN + "/closed_forms.json")["forms"]
    with SR.Symbolic() as S:
        w = LC.cumulant([_P, ((0, 1), (1, 0, 0)), _Q02], 1)
        live_odd, live_even = LC.block_odd(w), LC.block_even(w)
    live_ok = (
        live_odd == _rf(forms["single_perp_odd"])
        and live_even == _rf(forms["single_perp_even"])
        and live_odd == _rf_from_sympy(single_contact_odd(_N))
        and S.stats["components_verified"] > 0
    )
    sweep = _json(_SWEEP + "/certificate.json")["ranks"]
    assembly = _json(_ASSEMBLY + "/certificate.json")["ranks"]
    keys = {
        "hop_odd": (sweep, "hop_odd"),
        "hop_even": (sweep, "hop_even"),
        "u_odd": (sweep, "u_odd"),
        "u_even": (sweep, "u_even"),
        "single_perp_odd": (sweep, "single_odd"),
        "single_perp_even": (sweep, "single_even"),
        "fan_perp_odd": (sweep, "fan_odd"),
        "fan_perp_even": (sweep, "fan_even"),
        "corner_odd": (sweep, "corner_odd"),
        "corner_even": (sweep, "corner_even"),
        "single_cop_odd": (assembly, "single_coplanar"),
        "fan_cop_odd": (assembly, "fan_coplanar"),
        "beta_assembled": (assembly, "beta_assembled"),
    }
    pinned_ok, ranks = True, 0
    for name, (rows, key) in keys.items():
        rf = _rf(forms[name])
        for n_str, row in rows.items():
            if row.get(key) is None:
                continue
            ranks += 1
            if rf.at(int(n_str)) != Fraction(row[key]):
                pinned_ok = False
    degrees = {k: tuple(v["degrees_in_N"]) for k, v in forms.items()}
    ok = live_ok and pinned_ok and degrees["beta_assembled"] == (34, 41)
    return ok, (
        "live over Q(N): the perpendicular single-contact dressing is "
        f"{factor(live_odd.to_sympy())} "
        f"(C-odd) with {S.stats['components_verified']} eigencomponents verified; pinned: 13 forms "
        f"agree with the per-rank records at {ranks} rank evaluations. Degrees in N: "
        f"u {degrees['u_odd']}, "
        f"single {degrees['single_perp_odd']}, fan {degrees['fan_perp_odd']}, corner "
        f"{degrees['corner_odd']}, beta {degrees['beta_assembled']} -- the degree bound of "
        "ADR 0027 "
        "is the computed degree"
    )


_AUDIT = (
    "the specialisation argument's certificate: every eigencomponent an exact H0 eigenvector over "
    "Q(N), every Haar family balanced with n <= 3, every flux audited, and the one resolvent "
    "denominator vanishing at an integer rank >= 4 is at N = 4"
)


@field.check(_AUDIT, _CITE + "; ADR 0024", rests_on=(_DERIVED,))
def _():
    # The record's audit is the certificate that the Q(N) computation and the
    # per-rank engine perform the same computation for N >= 5: no word with
    # every nonzero flux >= 5 (so the charge filters agree), balanced families
    # only with n <= 3 <= N (so the Weingarten function is the inverse), and
    # the spectral decompositions verified. The integer roots >= 4 of the
    # resolvent denominators say where the argument stops: at N = 4 an
    # intermediate state becomes degenerate with the plaquette, which is the
    # per-rank engine's N = 4 path; the forms still agree there, as a fact.
    audit = _json(_BETA_RUN + "/certificate.json")["audit"]
    roots = audit["integer_roots_at_least_4"]
    states_at_4 = sorted(set(roots.get("4", [])))
    ok = (
        audit["max_weingarten_n"] == 3
        and audit["max_charge"] == 6
        and audit["components_verified"] > 20000
        and set(roots) == {"4"}
        and all(v["roots"] for v in audit["denominators"].values()) is not None
    )
    return ok, (
        f"{audit['components_verified']} eigencomponents verified over Q(N); largest "
        "Weingarten "
        f"family n = {audit['max_weingarten_n']}; largest link flux {audit['max_charge']} "
        "with every "
        "such word carrying another flux of magnitude <= 4; "
        f"{audit['distinct_intermediate_energies']} "
        f"distinct intermediate energies; link irreps met {audit['link_irreps_met']}; "
        "integer roots "
        f">= 4 of E0 - E: {sorted(roots)}, at N = 4 the states {states_at_4}. So the derivation is "
        "the per-rank value at every N >= 5; N = 3 and N = 4 are checked agreements"
    )


_NEGATIVES = (
    "the coplanar dressings are the exact negatives of the perpendicular ones in Q(N), single "
    "contact and fan alike, so the eleven-cumulant assembly is three cumulants and the cube: "
    "beta_N = -16u + 32d - 16 corner + 848/(N(N^2-1)^3)"
)


@field.check(_NEGATIVES, _CITE, rests_on=(_DERIVED,))
def _():
    # pi = 18 d_cop + 2 s_cop and rho = 14 d_perp + 2 s_perp + 2 corner + K
    # (the pair cancelling, ADR 0027); with d_cop = -d_perp and s_cop = -s_perp
    # the fans drop out entirely -- which is why R20 carries none of the fan's
    # factors 4N -+ 3, 4N -+ 7, 4N^2 - 7 -- and beta = -16u - 8(rho + pi)
    # collapses to three cumulants and the cube, alpha_N cancelling.
    forms = _json(_BETA_RUN + "/closed_forms.json")
    f = {k: _rf(v) for k, v in forms["forms"].items()}
    negatives = (
        f["single_cop_odd"] + f["single_perp_odd"] == 0
        and f["fan_cop_odd"] + f["fan_perp_odd"] == 0
        and f["single_cop_even"] == f["single_perp_even"]
        and f["fan_cop_even"] == f["fan_perp_even"]
    )
    three = (
        -16 * f["u_odd"]
        + 32 * f["single_perp_odd"]
        - 16 * f["corner_odd"]
        - 8 * f["cube_adjacent_odd"]
    )
    collapsed = f["beta_assembled"] == three
    assembly = _json(_ASSEMBLY + "/certificate.json")["ranks"]
    sweep = _json(_SWEEP + "/certificate.json")["ranks"]
    rank_ok = all(
        Fraction(assembly[n]["single_coplanar"]) + Fraction(sweep[n]["single_odd"]) == 0
        and Fraction(assembly[n]["fan_coplanar"]) + Fraction(sweep[n]["fan_odd"]) == 0
        for n in assembly
    )
    fan_factors = {
        _ptuple(e) for e in (4 * _N - 3, 4 * _N + 3, 4 * _N - 7, 4 * _N + 7, 4 * _N**2 - 7)
    }
    r20_factors = {
        _ptuple(fct) for fct, _m in Poly(R20.as_expr().subs(_z, _N**2), _N).factor_list()[1]
    }
    fans_absent = not (fan_factors & r20_factors)
    ok = negatives and collapsed and rank_ok and fans_absent
    return ok, (
        "d_cop + d_perp = 0 and s_cop + s_perp = 0 in the C-odd sector, and equal in the C-even, "
        "as "
        "rational functions and at every rank N = 4..70 of the assembly record; beta = "
        "-16u + 32d - 16 corner - 8K identically, alpha_N cancelling; the fan's factors "
        "(4N -+ 3)(4N -+ 7)(4N^2 - 7) are absent from R20 because the fans cancel"
    )


_IDENTITY = (
    "the final polynomial identity: -16 u + 32 d - 16 corner - 8 K_adj = P17(N^2)/(N R20(N^2)) as "
    "rational functions, for the closed forms of the two-hop weight, the single-contact dressing, "
    "the corner dressing and the adjacent-face cube completion"
)


@field.check(_IDENTITY, _CITE + "; GLUEBALL v3.1 Appendix A", rests_on=(_DERIVED, _NEGATIVES))
def _():
    # Pure algebra on the literal forms, which is what lean/Workhouse/Basic.lean
    # proves (betaN_assembled_numerator, betaN_from_three_cumulants): every
    # denominator divides N R20(N^2), and over that common denominator the
    # weighted numerators sum to P17(N^2) exactly. The forms are the engine's
    # Q(N) output by the derivation check above.
    n = _N
    three = (
        -16 * two_hop_odd(n)
        + 32 * single_contact_odd(n)
        - 16 * corner_odd(n)
        - 8 * cube_adjacent(n)
    )
    as_functions = cancel(three - corpus_beta(n)) == 0
    common = n * R20.as_expr().subs(_z, n**2)
    numerator = expand(cancel(three * common))
    cleared = expand(numerator - P17.as_expr().subs(_z, n**2)) == 0
    forms = _json(_BETA_RUN + "/closed_forms.json")["forms"]
    same_forms = all(
        _rf(forms[k]) == _rf_from_sympy(g(n))
        for k, g in (
            ("u_odd", two_hop_odd),
            ("single_perp_odd", single_contact_odd),
            ("corner_odd", corner_odd),
            ("cube_adjacent_odd", cube_adjacent),
        )
    )
    ok = as_functions and cleared and same_forms and Poly(numerator, n).degree() == 34
    return (
        ok,
        (
            "cancel(-16u + 32d - 16 corner - 8K - P17(N^2)/(N R20(N^2))) = 0; with denominators "
            "cleared over N R20(N^2) the numerator is P17(N^2), degree 34 in N; the four forms are "
            "the record's. Proved in Lean as betaN_from_three_cumulants"
        ),
        {"BETA_N_THREE_CUMULANT_FORM": cancel(three)},
    )


# --------------------------------------------------------------------------
# G14: the same decomposition for the corner and fan dressings, over Q(N)
# (runs/channels_symbolic_rank_2026-09-04).

_CHANNEL_CITE = "G14; C2; " + _CHANNEL_RUN + "; ADR 0029; ADR 0026; ADR 0019"


@cache
def _channels(cluster: str, sector: str) -> dict:
    """{channel key: nonzero element of Q(N)} of one cluster of the pinned record."""
    rows = _json(_CHANNEL_RUN + "/certificate.json")["clusters"][cluster]["channels"]
    out = {}
    for row in rows.values():
        rf = _rf(row[sector])
        if rf:
            out[ast.literal_eval(row["key"])] = rf
    return out


def _ratio_key(rf: SR.RF):
    """A constant ratio as a Fraction, anything else as its printed form."""
    if rf.num.degree() <= 0 and rf.den.degree() <= 0:
        return rf.at(0)
    return str(rf.to_sympy())


def _ratios(a: str, b: str, sector: str):
    """Per-channel ratios b/a over the union of nonzero channels, and the one-sided ones."""
    fa, fb = _channels(a, sector), _channels(b, sector)
    ratios: dict = {}
    one_sided = []
    for key in set(fa) | set(fb):
        if key in fa and key in fb:
            ratios.setdefault(_ratio_key(fb[key] / fa[key]), []).append(key)
        else:
            one_sided.append(key)
    return ratios, one_sided


def _counts(ratios: dict) -> dict:
    return {r: len(keys) for r, keys in ratios.items()}


_U_CHANNELS_QN = (
    "the 74 channels of u are identities in Q(N): every closed form of the pinned reconstruction "
    "is the symbolic channel exactly, and the finer per-link labelling adds only channels that "
    "vanish in the C-odd sector"
)


@field.check(
    _U_CHANNELS_QN,
    _CHANNEL_CITE,
    rests_on=(
        "u is the sum of 74 irrep-labelled channels, each a product of resolvent factors in N, "
        "and the 74 closed forms sum to u(N) identically",
    ),
)
def _():
    # ADR 0026 tagged every history by the total energies of its intermediate
    # states and reconstructed each channel from a rank sweep. Here the tag is
    # read off the per-link energies of each verified eigencomponent and the
    # channel is computed in Q(N). The two labellings differ only in the
    # order of the irrep names; every pinned form is recovered exactly.
    pinned = _json("runs/u_by_channel_2026-09-04/channel_closed_forms.json")
    mine = _channels("u_coplanar", "odd")

    def norm(key):
        return (key[0],) + tuple((e, tuple(sorted(names))) for e, names in key[1:])

    pin = {
        norm(ast.literal_eval(label)): _rf_from_sympy(sympify(v["form"], locals={"N": _N}))
        for label, v in pinned.items()
    }
    ours = {norm(k): v for k, v in mine.items()}
    agree = sum(1 for k in pin if k in ours and ours[k] == pin[k])
    even = _channels("u_coplanar", "even")
    total = sum(mine.values(), SR.RF(0)) == _rf_from_sympy(two_hop_odd(_N))
    ok = agree == len(pin) == 74 and set(ours) == set(pin) and total and len(even) == 122
    return ok, (
        f"{agree} of {len(pin)} pinned channel forms recovered as identities in Q(N); the C-odd "
        f"sector has exactly those 74 nonzero channels of the 122 the per-link labelling "
        f"distinguishes (all 122 nonzero in the C-even sector); the 74 sum to u(N)"
    )


_UNIVERSALITY_QN = (
    "u is universal channel by channel as an identity in Q(N): bent = -coplanar and L = coplanar "
    "in every C-odd channel and both equal it in every C-even channel, so u2 = 2u and the tier "
    "collapse D = -6u + 3u2 = 0 hold at every rank"
)


@field.check(
    _UNIVERSALITY_QN,
    _CHANNEL_CITE + "; THM_FLUX Prop. 2",
    rests_on=(
        _U_CHANNELS_QN,
        "u is universal channel by channel: the coplanar, bent and in-plane L chains agree in "
        "every "
        "one of the 74 channels, up to the incidence sign, at N = 3..30",
        "the tier collapse is one identity: D = -6u + 3*u2 with u2 = 2u",
        "B = 0 is unpopulated, not cancelled",
    ),
)
def _():
    # ADR 0026 established this at N = 3..30 by computation; over Q(N) it is
    # one identity per channel. With the orbit structure of the kernel
    # (B unpopulated, D = -6u + 3u2 and u2 the two coplanar L paths at weight
    # u), B = D = 0 at every rank follows -- the corpus's "dynamical selection
    # rule" is the Hodge form plus this universality.
    results = {}
    for other in ("u_bent", "u_L"):
        for sector in ("odd", "even"):
            ratios, one_sided = _ratios("u_coplanar", other, sector)
            results[(other, sector)] = (_counts(ratios), len(one_sided))
    ok = (
        results[("u_bent", "odd")] == ({Fraction(-1): 74}, 0)
        and results[("u_bent", "even")] == ({Fraction(1): 122}, 0)
        and results[("u_L", "odd")] == ({Fraction(1): 74}, 0)
        and results[("u_L", "even")] == ({Fraction(1): 122}, 0)
    )
    return ok, (
        "bent/coplanar = -1 in all 74 C-odd channels and +1 in all 122 C-even ones; L/coplanar = "
        "+1 "
        "in all 74 and all 122; no channel present in one chain only. One function of N per "
        "channel whatever the planes, as an identity"
    )


_FAN_CHANNELS = (
    "the shared-link fan dressing is universal channel by channel in Q(N): the coplanar fan is "
    "minus the perpendicular fan in every C-odd channel and equal in every C-even one, and its "
    "channels are the only ones that carry three-box irreps"
)


@field.check(_FAN_CHANNELS, _CHANNEL_CITE, rests_on=(_U_CHANNELS_QN,))
def _():
    # The coplanar fan (P and Q coplanar, X perpendicular, all three on one
    # link) and the perpendicular fan (P and X coplanar, Q perpendicular) are
    # one abstract cluster: three faces around a link, two of them coplanar.
    # Channel by channel the agreement is exact. The states after two
    # insertions can triple the shared link, which is where the fan's own
    # resolvent factors 4N -+ 3, 4N -+ 7 and 4N^2 - 7 come from.
    odd, one_odd = _ratios("fan_perp", "fan_cop", "odd")
    even, one_even = _ratios("fan_perp", "fan_cop", "even")
    names = set()
    for key in _channels("fan_perp", "odd"):
        for _extra, irreps in key[1:]:
            names.update(irreps)
    three_box = {n for n in names if n in ("3|", "21|", "111|", "2|1", "11|1")}
    corner_names = {
        n for key in _channels("corner", "odd") for _e, irreps in key[1:] for n in irreps
    }
    u_names = {
        n for key in _channels("u_coplanar", "odd") for _e, irreps in key[1:] for n in irreps
    }
    fan_factors = set()
    for rf in _channels("fan_perp", "odd").values():
        fan_factors |= _den_factors(rf)
    own = {_ptuple(e) for e in (4 * _N - 3, 4 * _N + 3, 4 * _N - 7, 4 * _N + 7, 4 * _N**2 - 7)}
    ok = (
        _counts(odd) == {Fraction(-1): 84}
        and not one_odd
        and _counts(even) == {Fraction(1): 138}
        and not one_even
        and three_box == {"3|", "21|", "111|", "2|1", "11|1"}
        and not (corner_names | u_names) & three_box
        and own <= fan_factors
    )
    return ok, (
        "coplanar/perpendicular fan = -1 in all 84 C-odd channels and +1 in all 138 C-even ones; "
        f"the fan's labels carry the three-box irreps {sorted(three_box)} (F^3 and F^2 x Fbar on "
        "the "
        "tripled link), which no channel of u or of the corner does, and its channels carry the "
        "factors 4N -+ 3, 4N -+ 7 and 4N^2 - 7"
    )


_SINGLE_CHANNELS = (
    "the single-contact dressing is universal channel by channel too, once the two geometries "
    "are matched: the straight chain dresses Q where the L-shaped chain dresses P, so the direct "
    "term's intermediate states correspond in reverse time order, and then all 92 C-odd channels "
    "have ratio -1 and all 164 C-even channels ratio +1"
)


@field.check(_SINGLE_CHANNELS, _CHANNEL_CITE, rests_on=(_NEGATIVES, _U_CHANNELS_QN))
def _():
    # The coplanar single contact is the straight chain P-Q-X with the dressing
    # on Q; the perpendicular one is the chain X-P-Q with X on P, the two
    # shared links of P adjacent. A channel label lists the intermediate
    # states in time order from the ket end, so the two geometries' direct
    # terms correspond with the labels reversed (the dressed end is the ket in
    # one and the bra in the other); the fold labels, one per factor of
    # {H2, V2}, correspond as they stand. Under that correspondence the
    # agreement is exact in every channel of both sectors. Read with the
    # labels paired naively, 24 channels look exceptional and cancel only in
    # sum; that reading was recorded for a few hours on 2026-09-04 and is
    # wrong -- the artifact, not the dressing, was the exception. Where the
    # geometries attach the dressing to the same end (u's chains, the fans)
    # the naive pairing is the right one, which is why it worked there.
    def paired(key):
        if key[0] == "direct":
            return ("direct", key[3], key[2], key[1])
        return key

    results = {}
    for sector in ("odd", "even"):
        perp, cop = _channels("single_perp", sector), _channels("single_cop", sector)
        ratios: dict = {}
        one_sided = 0
        for key, value in perp.items():
            other = cop.get(paired(key))
            if other is None:
                one_sided += 1
            else:
                ratios.setdefault(_ratio_key(other / value), []).append(key)
        results[sector] = (_counts(ratios), one_sided, len(perp), len(cop))
    naive, naive_one = _ratios("single_perp", "single_cop", "odd")
    ok = (
        results["odd"] == ({Fraction(-1): 92}, 0, 92, 92)
        and results["even"] == ({Fraction(1): 164}, 0, 164, 164)
        and _counts(naive) == {Fraction(-1): 76, Fraction(1): 8}
        and len(naive_one) == 16
    )
    return ok, (
        "with the direct-term labels reversed between the geometries and the fold labels as they "
        "stand: L/straight = -1 in all 92 C-odd channels and +1 in all 164 C-even ones, none "
        "one-sided. Paired naively the same channels read as 76 agreeing, 8 with the wrong sign "
        "and 16 one-sided, the 24 cancelling only in sum -- an artifact of the time-ordered "
        "labels, retracted the day it was recorded"
    )


_CORNER_CHANNELS = (
    "the corner dressing by channel: 87 C-odd channels, at most three doubled links in any "
    "direct-term state, every resolvent factor the corner adds to R20 the energy of an "
    "identified intermediate state, and the Weingarten poles at N = -+3 of single channels "
    "cancelling in the sum"
)


@field.check(_CORNER_CHANNELS, _CHANNEL_CITE + "; ADR 0025", rests_on=(_U_CHANNELS_QN,))
def _():
    # The corner's three faces pairwise share three different links, so after
    # two insertions three links can be doubled at once. The middle-state
    # label predicts the resolvent: E - E0 in units of C_F/2 is
    # 2 + sum of excesses, excess 2N^2/(N^2-1) (adj), 2(N-2)/(N-1) (lam),
    # 2(N+2)/(N+1) (sym), and the numerator of E0 - E is the factor.
    n = _N
    excess = {
        "adj": 2 * n**2 / (n**2 - 1),
        "lam": 2 * (n - 2) / (n - 1),
        "sym": 2 * (n + 2) / (n + 1),
    }
    corner = _channels("corner", "odd")
    predicted = {}
    for key in corner:
        if key[0] != "direct":
            continue
        extra, irreps = key[2]
        energy = cancel(extra + sum(excess[i] for i in irreps))
        num = Poly(energy.as_numer_denom()[0], n)
        predicted[key] = {_ptuple(f) for f, _m in num.factor_list()[1]}
    new_factors = {
        _ptuple(e)
        for e in (
            3 * n**2 - 1,
            2 * n - 1,
            2 * n + 1,
            4 * n**2 - 2 * n - 5,
            4 * n**2 + 2 * n - 5,
            4 * n**2 - 5,
            3 * n - 5,
            3 * n + 5,
        )
    }
    explained = True
    for key, rf in corner.items():
        for f in _den_factors(rf) & new_factors:
            if key[0] != "direct" or f not in predicted[key]:
                explained = False
    kinds = {k: sum(1 for key in corner if key[0] == k) for k in ("direct", "fold2", "fold3")}
    max_doubled = max(len(irreps) for key in corner if key[0] == "direct" for _e, irreps in key[1:])
    fold_max = max(len(irreps) for key in corner if key[0] != "direct" for _e, irreps in key[1:])
    all_factors = set()
    for rf in corner.values():
        all_factors |= _den_factors(rf)
    total = sum(corner.values(), SR.RF(0))
    poles = {_ptuple(n - 3), _ptuple(n + 3)}
    poles_cancel = poles <= all_factors and not (poles & _den_factors(total))
    ok = (
        len(corner) == 87
        and kinds == {"direct": 31, "fold2": 24, "fold3": 32}
        and max_doubled == 3
        and fold_max == 4
        and explained
        and total == _rf_from_sympy(corner_odd(n))
        and poles_cancel
    )
    return ok, (
        f"{len(corner)} nonzero C-odd channels ({kinds}), at most {max_doubled} doubled links in a "
        f"direct-term state and {fold_max} in the fold's face-times-conjugate states; "
        "3N^2-1 from the middle state (2, adj adj), 2N -+ 1 from (2, adj adj adj), "
        "4N^2 -+ 2N - 5 from (2, adj lam lam) and (2, adj sym sym), 4N^2 - 5 from "
        "(2, adj lam sym), "
        "3N -+ 5 from (2, lam lam) and (2, sym sym) -- each factor appears only in channels whose "
        "middle state has that energy; the n = 3 Weingarten poles N = -+3 of single channels are "
        "absent from the sum, which is the recorded corner form"
    )


_BETA_BY_CHANNEL = (
    "beta_N is a sum of resolvent products: -16 u + 32 d - 16 corner + 848/(N(N^2-1)^3) over "
    "254 channel terms, each a rational function of N whose denominator is a product of "
    "resolvent factors, equals P17(N^2)/(N R20(N^2))"
)


@field.check(
    _BETA_BY_CHANNEL,
    _CHANNEL_CITE + "; " + _BETA_RUN,
    rests_on=(_IDENTITY, _U_CHANNELS_QN, _CORNER_CHANNELS, _SINGLE_CHANNELS),
)
def _():
    # The question the G14 route asked: whether the corpus's all-rank formula
    # is itself a sum of resolvent products. It is: three cumulants by channel
    # and the cube completion, with the integer weights of the assembly. And
    # every one of the three is universal channel by channel across the
    # geometries it occurs in.
    n = _N
    u, d, c = (
        _channels("u_coplanar", "odd"),
        _channels("single_perp", "odd"),
        _channels("corner", "odd"),
    )
    cube = SR.RF(848, SR.N_SYM * (SR.N_SYM**2 - 1) ** 3)
    total = (
        -16 * sum(u.values(), SR.RF(0))
        + 32 * sum(d.values(), SR.RF(0))
        - 16 * sum(c.values(), SR.RF(0))
        + cube
    )
    identity = total == _rf_from_sympy(corpus_beta(n))
    allowed = {
        _ptuple(e)
        for e in (
            n,
            n - 1,
            n + 1,
            n - 3,
            n + 3,
            2 * n - 3,
            2 * n + 3,
            3 * n - 4,
            3 * n + 4,
            2 * n - 1,
            2 * n + 1,
            3 * n - 5,
            3 * n + 5,
            2 * n**2 - 1,
            2 * n**2 - 3,
            3 * n**2 - 2,
            3 * n**2 - 1,
            4 * n**2 - 5,
            4 * n**2 - n - 4,
            4 * n**2 + n - 4,
            4 * n**2 - 2 * n - 5,
            4 * n**2 + 2 * n - 5,
        )
    }
    factors = set()
    degrees = set()
    for fs in (u, d, c):
        for rf in fs.values():
            factors |= _den_factors(rf)
            degrees.add(rf.degrees())
    terms = len(u) + len(d) + len(c) + 1
    ok = (
        identity
        and terms == 254
        and factors <= allowed
        and max(dn for _dg, dn in degrees) <= 7
        and max(dg for dg, _dn in degrees) <= 4
    )
    return ok, (
        f"{terms} terms ({len(u)} of u, {len(d)} of the single contact, {len(c)} of the corner, "
        "one "
        "cube completion) sum to P17(N^2)/(N R20(N^2)) identically; every channel denominator is a "
        f"product of {sorted(_pstr(f) for f in factors)} with degree at most 7 in N, and every "
        "numerator has degree at most 4"
    )
