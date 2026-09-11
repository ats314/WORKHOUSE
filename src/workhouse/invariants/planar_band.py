"""The planar limit of the fourth-order band: every cumulant, every channel, exactly.

Every fourth-order cumulant of the beta_N assembly is one rational function of
N (``runs/beta_n_symbolic_rank_2026-09-04``), and each is split into resolvent
channels that are themselves rational functions of N
(``runs/channels_symbolic_rank_2026-09-04``). This suite reads those forms and
derives their large-N laws by exact arithmetic (``runs/planar_band_2026-09-11``).

What comes out. Every cumulant, in both C-parity sectors, is O(N^-7) -- the
order of the six-face cube completions -- although its largest channels are
O(N^-3): the N^-3 and N^-5 totals of every cluster's channels vanish
identically, two cancelled orders in every one of the sixteen cluster/sector
pairs. The second-order hop shows the same structure one level down: A_N and
B_N are O(1/N) each and t_N = B_N - A_N is O(N^-3). So at order 2k (k = 1, 2)
the channel content is N^-(2k-1), k orders cancel, and the band coefficient is
N^-(4k-1); with u = beta/(2N) that is what makes the band, relative to the
plaquette energy 2C_F ~ N, a series in tau^2 = (beta/N^3)^2 with N-independent
limits. The planar limit of beta_N itself, 6170/9, decomposes exactly as
-16 u + 32 d - 16 corner + 848 with u -> 11/576, d -> 5/16, corner -> 6197/576:
the cube completion 848 carries 124% of it and the corner subtracts 25%; the
two-face two-hop and single-contact clusters together contribute under 2%.
"""

from __future__ import annotations

import json
from fractions import Fraction

import flint
from sympy import Poly, Symbol, cancel, diff, fraction, real_roots, sympify, together

from .. import constants as K
from .. import symbolic_rank as SR
from ._core import ROOT, _suite

planar = _suite("the planar limit of the fourth-order band (G16)")

_FORMS_RUN = "runs/beta_n_symbolic_rank_2026-09-04"
_CHANNEL_RUN = "runs/channels_symbolic_rank_2026-09-04"
_RUN = "runs/planar_band_2026-09-11"
_CITE = "G16; G14; G6; " + _RUN + "; " + _FORMS_RUN + "; " + _CHANNEL_RUN + "; ADR 0046; ADR 0029"
_N = Symbol("N")
_DERIVED_FORMS = (
    "every cumulant of the beta_N assembly is one rational function of N computed over Q(N): "
    "the closed forms are derived, not reconstructed, and specialise to the per-rank records at "
    "N = 3..70"
)


def _json(rel: str) -> dict:
    return json.loads((ROOT / rel).read_text(encoding="utf-8"))


def rf(text: str):
    return sympify(text, locals={"N": _N})


def _coeffs(poly_expr) -> list[Fraction]:
    return [Fraction(int(c.p), int(c.q)) for c in Poly(poly_expr, _N).all_coeffs()]


def inv_expansion(expr, terms: int = 6) -> tuple[int, list[Fraction]]:
    """Exact large-N expansion: expr = N**power * (c_0 + c_1/N + c_2/N^2 + ...).

    Reversed-polynomial power-series division over Q; every coefficient is exact.
    """
    num, den = fraction(cancel(together(expr)))
    a, b = _coeffs(num), _coeffs(den)
    power = (len(a) - 1) - (len(b) - 1)
    a = a + [Fraction(0)] * terms
    b = b + [Fraction(0)] * terms
    q: list[Fraction] = []
    for j in range(terms):
        q.append((a[j] - sum(q[i] * b[j - i] for i in range(j))) / b[0])
    return power, q


def leading(expr) -> tuple[int, Fraction]:
    power, q = inv_expansion(expr, 1)
    return power, q[0]


def _forms() -> dict:
    return {
        k: rf(v["factored"]) for k, v in _json(_FORMS_RUN + "/closed_forms.json")["forms"].items()
    }


def _real_roots_ge(poly_expr, lo: int) -> list:
    p = Poly(poly_expr, _N)
    return [] if p.degree() <= 0 else [r for r in real_roots(p) if r >= lo]


def _rf(entry: dict) -> SR.RF:
    """A pinned ``{"num": [...], "den": [...]}`` coefficient record as an element of Q(N)."""
    return SR.RF(flint.fmpq_poly(entry["num"]), flint.fmpq_poly(entry["den"]))


def _rf_from_sympy(expr) -> SR.RF:
    num, den = cancel(expr).as_numer_denom()

    def to(e):
        return flint.fmpq_poly(
            [flint.fmpq(int(c.p), int(c.q)) for c in Poly(e, _N).all_coeffs()[::-1]]
        )

    return SR.RF(to(num), to(den))


def inv_expansion_rf(x: SR.RF, terms: int = 6) -> tuple[int, list[Fraction]]:
    """``inv_expansion`` for an element of the flint field: no sympy in the loop."""
    a = [Fraction(int(c.p), int(c.q)) for c in x.num.coeffs()][::-1]
    b = [Fraction(int(c.p), int(c.q)) for c in x.den.coeffs()][::-1]
    power = (len(a) - 1) - (len(b) - 1)
    a = a + [Fraction(0)] * terms
    b = b + [Fraction(0)] * terms
    q: list[Fraction] = []
    for j in range(terms):
        q.append((a[j] - sum(q[i] * b[j - i] for i in range(j))) / b[0])
    return power, q


def channel_census(cluster: dict, sector: str) -> dict:
    """Leading powers of a cluster's channels; exact totals of its N^-3, N^-5, N^-7 coefficients."""
    total = _rf_from_sympy(rf(cluster[f"sum_{sector}"]))
    tp, tq = inv_expansion_rf(total, 1)
    chan_sum = SR.RF(0)
    entries = []
    for label, ch in cluster["channels"].items():
        raw = ch[sector]
        d = raw if isinstance(raw, dict) else eval(raw, {}, {})  # noqa: S307 - record bytes
        e = _rf(d)
        chan_sum = chan_sum + e
        if e:
            entries.append((label, *inv_expansion_rf(e, 6)))
    identity = chan_sum == total
    totals: dict[int, Fraction] = {}
    for _label, p, q in entries:
        for j, c in enumerate(q):
            if p - j >= -7:
                totals[p - j] = totals.get(p - j, Fraction(0)) + c
    return {
        "identity": identity,
        "cumulant_power": tp,
        "cumulant_leading": tq[0],
        "max_channel_power": max(p for _, p, _ in entries),
        "totals": {k: totals.get(k, Fraction(0)) for k in (-3, -5, -7)},
        "channels": len(entries),
    }


_CUMULANTS = (
    "every fourth-order cumulant of the beta_N assembly is O(N^-7) in both sectors, the order of "
    "the cube completions, and the planar limit of beta_N is 6170/9 = -16(11/576) + 32(5/16) "
    "- 16(6197/576) + 848"
)


@planar.check(_CUMULANTS, _CITE, rests_on=(_DERIVED_FORMS,))
def _():
    F = _forms()
    names = [
        k
        for k in F
        if k
        not in (
            "hop_odd",
            "hop_even",
            "hop_perp_odd",
            "C_shp",
            "beta_assembled",
            "rho",
            "pi",
            "rho_plus_pi",
        )
    ]
    powers = {k: leading(F[k])[0] for k in names}
    all_seven = all(p == -7 for p in powers.values())
    u, d, c = (leading(F[k])[1] for k in ("u_odd", "single_perp_odd", "corner_odd"))
    beta = leading(F["beta_assembled"])
    w4 = leading(K.alpha_pen(_N) + F["beta_assembled"])
    decomposed = -16 * u + 32 * d - 16 * c + 848
    next_beta = inv_expansion(F["beta_assembled"], 3)[1][2]
    ok = (
        all_seven
        and beta == (-7, Fraction(6170, 9))
        and decomposed == Fraction(6170, 9)
        and next_beta == Fraction(677903, 324)
        and w4 == (-7, Fraction(11930, 9))
        and (u, d, c) == (Fraction(11, 576), Fraction(5, 16), Fraction(6197, 576))
    )
    return ok, (
        f"{len(names)} cumulant forms all N^-7; beta_N ~ {beta[1]}/N^7 + {next_beta}/N^9 "
        f"(the corpus's 6170/9 and 677903/324, GLUEBALL v3.1); W_4 = alpha + beta ~ {w4[1]}/N^7; "
        f"planar shares: cube 848 -> {848 / beta[1]}, corner -> {-16 * c / beta[1]}, "
        f"single -> {32 * d / beta[1]}, two-hop -> {-16 * u / beta[1]}"
    )


_CHANNELS = (
    "two orders cancel in every cluster: the largest resolvent channels of every fourth-order "
    "cumulant are O(N^-3) and the N^-3 and N^-5 channel totals vanish identically, in all eight "
    "clusters and both sectors"
)


@planar.check(_CHANNELS, _CITE, rests_on=(_DERIVED_FORMS,))
def _():
    # Every channel form of the channel record is re-expanded exactly here;
    # nothing is read from the planar record's own totals.
    clusters = _json(_CHANNEL_RUN + "/certificate.json")["clusters"]
    rows = {}
    for name, rec in clusters.items():
        for sector in ("odd", "even"):
            rows[(name, sector)] = channel_census(rec, sector)
    ok = all(
        r["identity"]
        and r["max_channel_power"] == -3
        and r["cumulant_power"] == -7
        and r["totals"][-3] == 0
        and r["totals"][-5] == 0
        and r["totals"][-7] == r["cumulant_leading"]
        for r in rows.values()
    )
    return ok, (
        f"{len(rows)} cluster/sector pairs, {sum(r['channels'] for r in rows.values())} nonzero "
        "channel forms re-expanded exactly: max channel power -3, cumulant power -7, N^-3 and "
        "N^-5 totals 0 in every pair; the N^-7 total is the cumulant's leading coefficient "
        f"(corner odd {rows[('corner', 'odd')]['cumulant_leading']}, "
        f"u odd {rows[('u_coplanar', 'odd')]['cumulant_leading']})"
    )


_SECOND = (
    "the second-order hop cancels one order: A_N and B_N are -1/N + O(N^-3) each and "
    "their difference t_N is 1/(4N^3) + O(N^-5)"
)


@planar.check(_SECOND, _CITE + "; MASTER_THEORY §4.3")
def _():
    a, b, t = (inv_expansion(f(_N), 4) for f in (K.antiparallel_sum, K.parallel_sum, K.hopping))
    ok = (
        a[0] == -1
        and b[0] == -1
        and a[1][0] == b[1][0] == -1
        and t[0] == -3
        and t[1][0] == Fraction(1, 4)
    )
    return ok, (
        f"A_N ~ {a[1][0]}/N, B_N ~ {b[1][0]}/N, t_N ~ {t[1][0]}/N^3: one cancelled order (N^-1); "
        "fourth order cancels two"
    )


_TAU = (
    "the band coefficients scale as N^-(4k-1) at order 2k (k = 1, 2), so W_4/W_2 = "
    "(11930/27) u^2/N^4 (1 + O(N^-2)); with u = beta/(2N) this is (5965/54) tau^2, tau = beta/N^3"
)


@planar.check(_TAU, _CITE + "; NOTE_O4 §11")
def _():
    F = _forms()
    w4 = K.alpha_pen(_N) + F["beta_assembled"]
    w2 = 12 * K.hopping(_N)
    ratio = cancel(w4 / w2)  # coefficient of u^2 in W_4 u^4 / (W_2 u^2)
    p, q = inv_expansion(ratio, 3)
    tau_coeff = q[0] / 4  # u^2 = beta^2/(4N^2): ratio * u^2 = (q0/4) beta^2/N^6
    ok = p == -4 and q[0] == Fraction(11930, 27) and tau_coeff == Fraction(5965, 54) and q[1] == 0
    return ok, (
        f"W_4/W_2 = {q[0]}/N^4 (1 + {q[2] / q[0]}/N^2 + ...), times u^2; t_N ~ N^-3 and "
        f"W_4 ~ N^-7 are N^-(4k-1) for k = 1, 2; tau^2 coefficient {tau_coeff} under u = beta/(2N)"
    )


_SIGN = (
    "N^7 beta_N, N^7 W_4 and N^7 corner_N are positive and decrease strictly to their planar "
    "limits for real N >= 3, and no closed form of the assembly has a pole or zero at real N >= 3"
)


@planar.check(_SIGN, _CITE)
def _():
    F = _forms()
    F["W4"] = K.alpha_pen(_N) + F["beta_assembled"]
    poles = {}
    for k, e in F.items():
        num, den = fraction(cancel(together(e)))
        poles[k] = (_real_roots_ge(num, 3), _real_roots_ge(den, 3))
    no_roots = all(not a and not b for a, b in poles.values())
    mono = {}
    for k in ("beta_assembled", "W4", "corner_odd"):
        scaled = cancel(_N**7 * F[k])
        dnum, _ = fraction(cancel(together(diff(scaled, _N))))
        lim = leading(F[k])[1]
        mono[k] = (scaled.subs(_N, 3) > lim > 0, _real_roots_ge(dnum, 3))
    ok = no_roots and all(above and not roots for above, roots in mono.values())
    at3 = cancel(_N**7 * F["beta_assembled"]).subs(_N, 3)
    return ok, (
        f"{len(F)} forms: no real zero or pole at N >= 3; N^7 beta_N falls from {float(at3):.4f} "
        "at N = 3 to 6170/9 = 685.56, N^7 W_4 to 11930/9, N^7 corner to 6197/576, each with no "
        "critical point at N >= 3"
    )
