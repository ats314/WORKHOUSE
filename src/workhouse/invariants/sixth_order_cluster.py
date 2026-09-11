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

from .. import loopcalc as L
from .. import sixth_order_characters as CH
from .. import sixth_order_cluster as SC
from .. import symbolic_rank as SR
from ._core import ROOT, _suite

cluster = _suite("G9 direct sixth order on one face and the shared-link pairs, any rank")
_CITE = "G9; G16; runs/g9_direct_h6_pair_2026-09-11 (the N^-(4k-1) conjecture of runs/planar_band_2026-09-11, branch claude/planar-band-20260911)"  # noqa: E501
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
