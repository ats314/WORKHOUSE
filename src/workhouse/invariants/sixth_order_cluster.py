"""G9 direct sixth order on actual clusters: one face and the shared-link pairs, any rank.

The route asked for the direct sixth-order effective operator on the smallest
connected multi-plane support. This suite certifies the engine that computes
it and the one-face result it produces at every rank, and reads the retained
pair results of ``runs/g9_direct_h6_pair_2026-09-11`` where the computation
is too long for a check (hours over Q(N)).

What is certified here, and what is not: exact identities between three
independent evaluations (the general Bloch recursion with the Hermitian
metric, the closed word formula (F6), and the character-basis engine that
shares no primitive with the loop calculus), and exact 1/N expansions of
rational functions of N. Nothing here evaluates the SU(3) determinant
families a physical N = 3 sixth-order coefficient needs; the Q(N) forms
specialise to the per-rank engine for N >= 9 (sixth-order words carry fluxes
up to 8).
"""

from __future__ import annotations

import json
from fractions import Fraction

import sympy as sp

from .. import constants as K
from .. import kernel_orbits as KO
from .. import loopcalc as L
from .. import sixth_order_characters as CH
from .. import sixth_order_cluster as SC
from .. import symbolic_rank as SR
from ._core import ROOT, _suite

cluster = _suite("G9 direct sixth order on one face and the shared-link pairs, any rank")
_CITE = "G9; G16; ADR 0046 conjecture 4; runs/g9_direct_h6_pair_2026-09-11"
_RUN = ROOT / "runs" / "g9_direct_h6_pair_2026-09-11"
_N = sp.Symbol("N")
_X = sp.Symbol("x")
VALIDATION_RANK = 11


def _expand(expr, terms: int = 3) -> list[tuple[int, sp.Rational]]:
    """Leading terms of the 1/N expansion: [(power, coefficient), ...], power ascending."""
    e = sp.cancel(sp.sympify(expr, locals={"N": _N}) if isinstance(expr, str) else expr)
    if e == 0:
        return []
    s = sp.series(e.subs(_N, 1 / _X), _X, 0, 64).removeO()
    mons = sorted(sp.Poly(sp.expand(s), _X).as_dict().items())
    return [(int(k[0]), c) for k, c in mons[:terms]]


def _rf(x):
    return sp.cancel(x.to_sympy())


class _IntegerRank:
    """``loopcalc`` at an integer rank >= 9 with Casimir-table link spectra."""

    def __init__(self, N: int):
        self.N = N

    def __enter__(self):
        self._saved = (L.N, L.CF, L.link_spectrum)
        L.set_rank(self.N)
        N = self.N

        def spectrum(word, link):
            a, b = L.content(word).get(link, [0, 0])
            weight = L.link_weight(link)
            out = set()
            for k in range(min(a, b) + 1):
                for lam in SR.partitions(a - k):
                    for mu in SR.partitions(b - k):
                        aa, bb = sum(lam), sum(mu)
                        c2 = Fraction((aa + bb) * N + SR._content_sum(lam) + SR._content_sum(mu))
                        c2 -= Fraction((aa - bb) ** 2, N)
                        out.add(weight * c2 / 4)
            return tuple(sorted(out))

        L.link_spectrum = spectrum
        return self

    def __exit__(self, *exc):
        L.N, L.CF, L.link_spectrum = self._saved
        return False


@cluster.check(
    "the sixth-order Bloch recursion, the closed word formula and the character engine "
    "agree on one face at N = 11 through order six, both C sectors and the vacuum",
    _CITE,
)
def one_face_three_engines():
    with _IntegerRank(VALIDATION_RANK):
        single = SC.ModelSpace(SC.PAIRS["perpendicular"][:1], reduced=True)
        b = SC.bloch_hermitian(single, 6)
        f = SC.folded_words(single, 6)
        words_ok = all(b["H"][n] == f[f"H{n}"] for n in (2, 4, 6))
        ch = CH.bloch_series(6, CH.PLAQUETTE, sign=1, casimir=CH.casimir_rank(VALIDATION_RANK))
        odd = [SC.odd_even(b["H"][n], 0, 0)[0] for n in range(7)]
        even = [SC.odd_even(b["H"][n], 0, 0)[1] for n in range(7)]
        chars_ok = odd == ch["odd"] and even == ch["even"] and ch["symmetric"]
        vac = SC.ModelSpace(SC.PAIRS["perpendicular"][:1], reduced=True, vacuum=True)
        bv = SC.bloch_hermitian(vac, 6)
        chv = CH.bloch_series(6, CH.VACUUM, sign=1, casimir=CH.casimir_rank(VALIDATION_RANK))
        vac_ok = [bv["H"][n][0][0] for n in range(7)] == chv["energies"]
        sizes = [len(c[0]) for c in b["chi"]]
    ok = words_ok and chars_ok and vac_ok
    return (
        ok,
        (
            f"N=11: H2,H4,H6 of the recursion equal the (F6) word formula entry by entry; the "
            f"C-odd and C-even energies and the vacuum equal the character-basis series at every "
            f"order 0..6; every K_n is a I + b sigma_x. H6 odd = {odd[6]}, even = {even[6]}, "
            f"vacuum = {chv['energies'][6]}; wave-operator supports {sizes}. Exact rationals."
        ),
        {
            "G9_ONE_FACE_SIXTH_ODD_N11": sp.Rational(odd[6]),
            "G9_ONE_FACE_SIXTH_VACUUM_N11": sp.Rational(chv["energies"][6]),
        },
    )


@cluster.check(
    "one face over Q(N): the vacuum-subtracted plaquette energy at order 2k is O(N^-(4k-1)) "
    "for k = 1, 2, 3, both C sectors, while every order's unsubtracted pieces are larger",
    _CITE,
)
def one_face_planar_law():
    ch = CH.bloch_series(6, CH.PLAQUETTE, sign=1)
    vac = CH.bloch_series(6, CH.VACUUM, sign=1)
    lead = {}
    ok = True
    for k in (1, 2, 3):
        n = 2 * k
        for sector in ("odd", "even"):
            terms = _expand(_rf(ch[sector][n]) - _rf(vac["energies"][n]), 2)
            lead[(sector, n)] = terms
            ok = ok and terms[0][0] == 4 * k - 1
        raw = _expand(_rf(ch["odd"][n]), 1)
        v = _expand(_rf(vac["energies"][n]), 1)
        lead[("vacuum", n)] = v
        ok = ok and raw[0][0] == 4 * k - 3 and v[0][0] == 4 * k - 3
    split = _expand(_rf(ch["odd"][6]) - _rf(ch["even"][6]), 1)
    ok = ok and split[0][0] == 11
    text = "; ".join(
        f"order {n} {s}: N^-{t[0][0]} x {t[0][1]}, next N^-{t[1][0]}"
        for (s, n), t in lead.items()
        if s != "vacuum"
    )
    return (
        ok,
        (
            f"{text}. The unsubtracted energy and the vacuum are both O(N^-(4k-3)) and cancel "
            f"one order; the C-odd/C-even splitting at order six is "
            f"N^-{split[0][0]} x {split[0][1]}. "
            "Exact rational functions of N (Pieri rules, valid for N >= 9); the k = 3 case is the "
            "ADR 0046 conjecture on the one-face cluster."
        ),
        {
            "G9_ONE_FACE_SIXTH_ODD_PLANAR": lead[("odd", 6)][0][1],
            "G9_ONE_FACE_SIXTH_EVEN_PLANAR": lead[("even", 6)][0][1],
            "G9_ONE_FACE_FOURTH_ODD_PLANAR": lead[("odd", 4)][0][1],
        },
    )


@cluster.check(
    "one face over Q(N): the seven pieces of (F6) are each O(N^-5) and their sum is the "
    "character-engine H6, so three orders cancel between channel content and cumulant",
    _CITE,
    rests_on=(
        "one face over Q(N): the vacuum-subtracted plaquette energy at order 2k is O(N^-(4k-1)) "
        "for k = 1, 2, 3, both C sectors, while every order's unsubtracted pieces are larger",
    ),
)
def one_face_pieces():
    record = json.loads((_RUN / "single.json").read_text(encoding="utf-8"))
    pieces = record["pieces"]
    ch = CH.bloch_series(6, CH.PLAQUETTE, sign=1)
    ok = len(pieces) == 7
    orders = {}
    total = {"odd": sp.Integer(0), "even": sp.Integer(0)}
    for name, forms in pieces.items():
        for sector in ("odd", "even"):
            e = sp.cancel(sp.sympify(forms[sector], locals={"N": _N}))
            total[sector] += e
            lead = _expand(e, 1)
            orders[(name, sector)] = lead[0][0] if lead else None
    for sector in ("odd", "even"):
        ok = ok and sp.cancel(total[sector] - _rf(ch[sector][6])) == 0
    nonzero = [p for p in orders.values() if p is not None]
    ok = ok and all(p == 5 for p in nonzero) and orders[("-{A3,B3}/2", "odd")] is None
    h6 = _expand(_rf(ch["odd"][6]), 1)[0]
    return (
        ok,
        (
            f"Pieces read from the run record: leading powers {sorted(set(nonzero))} on every "
            f"nonzero piece ({len(nonzero)} of 14 sector entries; the odd-history fold {{A3,B3}} "
            f"vanishes at generic rank by charge); their exact sum over Q(N) equals the "
            f"independent character-engine H6 in both sectors, which is N^-{h6[0]} x {h6[1]}; "
            "with the vacuum the cumulant is N^-11. Three cancelled orders: N^-5, N^-7, N^-9."
        ),
    )


def _pair_record(which: str) -> dict | None:
    path = _RUN / f"pair_{which}.json"
    if not path.exists():
        return None
    return json.loads(path.read_text(encoding="utf-8"))


_PAIR_SUFFIX = ""  # "_h4" selects the fast fourth-order validation records


def _pair_records() -> dict[str, dict] | None:
    out = {}
    for which in ("coplanar", "perpendicular"):
        path = _RUN / f"pair_{which}{_PAIR_SUFFIX}.json"
        if not path.exists():
            return None
        out[which] = json.loads(path.read_text(encoding="utf-8"))
    return out


def _form(expr: str):
    return sp.cancel(sp.sympify(expr, locals={"N": _N}))


_PAIR_LAW = (
    "the shared-link pairs over Q(N): the C-odd hop at order 2k is O(N^-(4k-1)) for k = 1, 2, 3 "
    "on both pairs, the order-2 hops are -t_N (coplanar) and +t_N (perpendicular), and the "
    "order-4 hops specialise at N = 11 to the pair_element value"
)
_PAIR_MIRROR = (
    "the coplanar and perpendicular pair hops are exact negatives in the C-odd sector and equal "
    "in the C-even sector at every even order through six, over Q(N)"
)
_PAIR_PIECES = (
    "on both shared-link pairs over Q(N), every nonzero (F6) piece of the sixth-order hop is "
    "O(N^-5) in both C sectors while their exact sum, the hop, is O(N^-11)"
)
_PAIR_SYMBOL = (
    "placed in the carrier symbol with the orbit closed forms, the pair hops give "
    "T_2k = 4 pi_2k e1 - 2 (pi_2k + rho_2k) e2 with pi = coplanar hop and rho = perpendicular "
    "hop, and the e2 coefficient vanishes at every order: the pair enters the symbol as "
    "4 pi_2k q alone"
)


def _register_pair_checks() -> None:
    """The pair checks read retained run records (hours over Q(N)); they register
    only when both records are present, so a checkout without them certifies the
    one-face results alone rather than failing on absent evidence."""
    if _pair_records() is None:
        return

    @cluster.check(_PAIR_LAW, _CITE)
    def pair_hops_law():
        recs = _pair_records()
        validate = json.loads((_RUN / "validate.json").read_text(encoding="utf-8"))
        order = min(r.get("order", 6) for r in recs.values())
        lead, ok = {}, order == 6
        t_n = K.hopping(_N)
        for which, rec in recs.items():
            for n in range(2, order + 1, 2):
                for sector in ("odd", "even"):
                    e = _form(rec["elements"][str(n)][f"hop_{sector}"])
                    terms = _expand(e, 2)
                    lead[(which, n, sector)] = terms
                    if sector == "odd":
                        ok = ok and terms[0][0] == 2 * n - 1
            h2 = _form(rec["elements"]["2"]["hop_odd"])
            ok = ok and sp.cancel(h2 - (-t_n if which == "coplanar" else t_n)) == 0
            h4 = _form(rec["elements"]["4"]["hop_odd"]).subs(_N, VALIDATION_RANK)
            ok = ok and h4 == sp.Rational(validate["pairs_fourth_order"][which]["hop_odd_H4"])
        text = "; ".join(
            f"{w} order {n} {s}: N^-{t[0][0]} x {t[0][1]}"
            + (f", next N^-{t[1][0]}" if len(t) > 1 else "")
            for (w, n, s), t in lead.items()
            if s == "odd"
        )
        even = "; ".join(
            f"{w} order {n} even: N^-{t[0][0]} x {t[0][1]}"
            for (w, n, s), t in lead.items()
            if s == "even" and t
        )
        values = {}
        if ("coplanar", 6, "odd") in lead:
            cop, perp = lead[("coplanar", 6, "odd")], lead[("perpendicular", 6, "odd")]
            values["G9_PAIR_SIXTH_HOP_COPLANAR_PLANAR"] = cop[0][1]
            values["G9_PAIR_SIXTH_HOP_PERPENDICULAR_PLANAR"] = perp[0][1]
        return (
            ok,
            (
                f"{text}. C-even: {even}. Order 2 is -t_N and +t_N exactly (K.hopping); order 4 "
                f"at N = 11 equals the pair_element block of validate.json. Exact rational "
                f"functions of N from the word formula (F6) (valid for N >= 9); the "
                f"k = 3 case is ADR 0046 conjecture 4 on the two-face clusters."
            ),
            values,
        )

    @cluster.check(_PAIR_MIRROR, _CITE)
    def pair_hops_mirror():
        recs = _pair_records()
        order = min(r.get("order", 6) for r in recs.values())
        ok = order == 6
        rows = []
        for n in range(2, order + 1, 2):
            c, p = recs["coplanar"]["elements"][str(n)], recs["perpendicular"]["elements"][str(n)]
            odd_sum = sp.cancel(_form(c["hop_odd"]) + _form(p["hop_odd"]))
            even_diff = sp.cancel(_form(c["hop_even"]) - _form(p["hop_even"]))
            ok = ok and odd_sum == 0 and even_diff == 0
            rows.append(f"order {n}: odd sum {odd_sum}, even difference {even_diff}")
        return ok, (
            "; ".join(rows) + ". The link bijection carrying the coplanar words onto the "
            "perpendicular words conjugates an odd number of faces (the fourth-order identity of "
            "the all-rank suite), and the identity persists at order six over Q(N), so the pair "
            "cluster contributes to pi and rho with opposite signs at every order"
        )

    @cluster.check(_PAIR_SYMBOL, _CITE, rests_on=(_PAIR_LAW, _PAIR_MIRROR))
    def pair_symbol():
        recs = _pair_records()
        order = min(r.get("order", 6) for r in recs.values())
        down = KO.down_laplacian()
        sign_ok = down[((0, 1), (0, 1), (1, 0, 0))] == -1 and down[((0, 1), (0, 2), (0, 0, 0))] == 1
        pi_form = KO.symmetric(**KO.CLOSED_FORMS["pi"])
        rho_form = KO.symmetric(**KO.CLOSED_FORMS["rho"])
        e1, e2 = KO.E1, KO.E2
        pi_expected = KO._add(KO._add({}, e1, 4), e2, -2)
        forms_ok = pi_form == pi_expected and rho_form == KO._add({}, e2, -2)
        ok = order == 6 and sign_ok and forms_ok
        rows, values = [], {}
        for n in range(2, order + 1, 2):
            pi = _form(recs["coplanar"]["elements"][str(n)]["hop_odd"])
            rho = _form(recs["perpendicular"]["elements"][str(n)]["hop_odd"])
            c1, c2 = sp.cancel(4 * pi), sp.cancel(-2 * (pi + rho))
            ok = ok and c2 == 0
            lead = _expand(c1, 2)
            rows.append(
                f"order {n}: e1 coefficient N^-{lead[0][0]} x {lead[0][1]} "
                f"+ N^-{lead[1][0]} x {lead[1][1]}, e2 coefficient {c2}"
            )
            if n == 2:
                ok = ok and sp.cancel(c1 + 4 * K.hopping(_N)) == 0
            if n == 6:
                values["G9_PAIR_SIXTH_SYMBOL_E1_PLANAR"] = lead[0][1]
        return (
            ok,
            (
                "; ".join(rows) + ". Sign: the order-2 kernel is t_N L_down off the diagonal, "
                "whose entries are -1 on coplanar and +1 on perpendicular neighbours "
                "(kernel_orbits.down_laplacian), matching the recursion's -t_N and +t_N, so "
                "pi_n and rho_n are the hops themselves in the kernel's (0,2) basis; at order 2 "
                "the e1 coefficient is -4 t_N. Orbit closed forms pi -> 4 e1 - 2 e2, rho -> -2 e2 "
                "(kernel_orbits.CLOSED_FORMS). The pair's contribution to C_shp, -(pi + rho)/2, "
                "is zero at every order; only the two-face part of pi and rho is placed here, "
                "the three-face and larger sixth-order clusters are not computed"
            ),
            values,
        )

    @cluster.check(_PAIR_PIECES, _CITE, rests_on=(_PAIR_LAW,))
    def pair_pieces():
        recs = _pair_records()
        order = min(r.get("order", 6) for r in recs.values())
        ok = order == 6 and all("pieces" in r for r in recs.values())
        rows, powers = [], set()
        for which, rec in recs.items():
            if "pieces" not in rec:
                continue
            for sector in ("odd", "even"):
                total = sp.Integer(0)
                for name, forms in rec["pieces"].items():
                    e = _form(forms[f"hop_{sector}"])
                    total += e
                    lead = _expand(e, 1)
                    if lead:
                        powers.add(lead[0][0])
                        ok = ok and lead[0][0] == order - 1
                    rows.append(
                        f"{which} {sector} {name}: N^-{lead[0][0]}"
                        if lead
                        else f"{which} {sector} {name}: 0"
                    )
                hop = _form(rec["elements"][str(order)][f"hop_{sector}"])
                ok = ok and sp.cancel(total - hop) == 0
        return ok, (
            f"leading powers of the nonzero (F6) hop pieces: {sorted(powers)}; "
            + "; ".join(rows)
            + f". Their exact sum is the order-{order} hop in both sectors on both pairs, "
            "so the pair hop cancels three orders, N^-5, N^-7, N^-9, between its channel "
            "content and its cumulant: the ADR 0046 mechanism at k = 3 on a two-face cluster"
        )


_register_pair_checks()
