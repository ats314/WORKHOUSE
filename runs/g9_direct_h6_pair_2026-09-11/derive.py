"""The sixth-order effective Hamiltonian on the one-face and shared-link pair clusters, over Q(N).

Run from the repository root with the project environment:

    python runs/g9_direct_h6_pair_2026-09-11/derive.py [stage ...]

Stages (default: all), each writing its own JSON next to this file so that a
long run can be resumed and every number keeps its own provenance:

    validate   integer-rank (N = 11) agreement of the general Bloch recursion with the
               closed word formula (F6), with ``loopcalc.pair_element`` and
               ``Cluster.second_order``, and with the character-basis engine
    single     one face over Q(N): recursion, the seven pieces of (F6), the character
               engine, the vacuum, and their 1/N expansions
    pair_perpendicular, pair_coplanar
               the shared-link pairs over Q(N) by the word formula (F6): hop and on-site
               elements of H2, H4, H6 in both C sectors, the seven pieces, the vacuum
               (Bloch recursion), resolvent denominators, audit
    pair_perpendicular_h4, pair_coplanar_h4
               the same through order four (about a minute each): validation records
    expand     the 1/N expansions and leading powers of everything computed, and with
               both pair records the hops placed into the carrier symbol (``pair_symbol``)
    certificate assemble certificate.json from the stage files

Nothing here reads a kernel record or a run of either historical pipeline.
"""

from __future__ import annotations

import json
import sys
import time
from fractions import Fraction
from pathlib import Path

import sympy as sp

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
sys.path.insert(0, str(ROOT / "src"))

from workhouse import loopcalc as L  # noqa: E402
from workhouse import sixth_order_characters as CH  # noqa: E402
from workhouse import sixth_order_cluster as SC  # noqa: E402
from workhouse import symbolic_rank as SR  # noqa: E402

VALIDATION_RANK = 11
MIN_RANK = 9  # sixth-order words carry fluxes up to 8: the Q(N) forms specialise for N >= 9


def _dump(name: str, obj: dict) -> None:
    (HERE / f"{name}.json").write_text(
        json.dumps(obj, indent=1, sort_keys=True) + "\n", encoding="utf-8"
    )
    print(f"wrote {name}.json", flush=True)


def _load(name: str) -> dict:
    return json.loads((HERE / f"{name}.json").read_text(encoding="utf-8"))


def _s(x) -> str:
    return str(x.to_sympy()) if hasattr(x, "to_sympy") else str(x)


def integer_link_spectrum(N: int):
    """Casimir-table link spectra at one integer rank (no characteristic polynomial)."""

    def spectrum(word, link):
        a, b = L.content(word).get(link, [0, 0])
        weight = L.link_weight(link)
        out = set()
        for k in range(min(a, b) + 1):
            for lam in SR.partitions(a - k):
                for mu in SR.partitions(b - k):
                    aa, bb = sum(lam), sum(mu)
                    c2 = Fraction((aa + bb) * N + SR._content_sum(lam) + SR._content_sum(mu), 1)
                    c2 -= Fraction((aa - bb) ** 2, N)
                    out.add(weight * c2 / 4)
        return tuple(sorted(out))

    return spectrum


class IntegerRank:
    """``loopcalc`` at one integer rank >= 9 with the Casimir-table spectra."""

    def __init__(self, N: int):
        self.N = N

    def __enter__(self):
        self._saved = (L.N, L.CF, L.link_spectrum)
        L.set_rank(self.N)
        L.link_spectrum = integer_link_spectrum(self.N)
        return self

    def __exit__(self, *exc):
        L.N, L.CF, L.link_spectrum = self._saved
        return False


# ---------------------------------------------------------------- stages
def stage_validate() -> dict:
    t0 = time.time()
    out: dict = {"rank": VALIDATION_RANK}
    with IntegerRank(VALIDATION_RANK):
        single = SC.ModelSpace(SC.PAIRS["perpendicular"][:1], reduced=True)
        b = SC.bloch_hermitian(single, 6)
        f = SC.folded_words(single, 6)
        out["single_recursion_equals_word_formula"] = {
            str(n): b["H"][n] == f[f"H{n}"] for n in (2, 4, 6)
        }
        ch = CH.bloch_series(6, CH.PLAQUETTE, sign=1, casimir=CH.casimir_rank(VALIDATION_RANK))
        out["single_recursion_equals_characters"] = {
            "odd": [SC.odd_even(b["H"][n], 0, 0)[0] == ch["odd"][n] for n in range(7)],
            "even": [SC.odd_even(b["H"][n], 0, 0)[1] == ch["even"][n] for n in range(7)],
            "K_symmetric": ch["symmetric"],
        }
        vac = SC.ModelSpace(SC.PAIRS["perpendicular"][:1], reduced=True, vacuum=True)
        bv = SC.bloch_hermitian(vac, 6)
        chv = CH.bloch_series(6, CH.VACUUM, sign=1, casimir=CH.casimir_rank(VALIDATION_RANK))
        out["vacuum_recursion_equals_characters"] = [
            bv["H"][n][0][0] == chv["energies"][n] for n in range(7)
        ]
        out["single_H6_odd"] = str(SC.odd_even(b["H"][6], 0, 0)[0])
        out["single_H6_even"] = str(SC.odd_even(b["H"][6], 0, 0)[1])
        out["single_chi_sizes"] = [len(c[0]) for c in b["chi"]]
        pairs = {}
        for name, faces in SC.PAIRS.items():
            cl = L.Cluster(faces, True)
            h2, _ = cl.second_order()
            space = SC.ModelSpace(faces, reduced=True)
            bp = SC.bloch_hermitian(space, 4)
            pe = L.pair_element(faces)
            blk = {(a, c): bp["H"][4][a][c] for a in (0, 1) for c in (2, 3)}
            pairs[name] = {
                "H2_equals_second_order": bp["H"][2] == h2,
                "H4_block_equals_pair_element": blk == pe,
                "hop_odd_H2": str(SC.odd_even(bp["H"][2], 0, 1)[0]),
                "hop_odd_H4": str(SC.odd_even(bp["H"][4], 0, 1)[0]),
            }
        out["pairs_fourth_order"] = pairs
    out["seconds"] = time.time() - t0
    _dump("validate", out)
    return out


def stage_single() -> dict:
    t0 = time.time()
    out: dict = {"min_rank": MIN_RANK}
    with SR.Symbolic(min_rank=MIN_RANK) as S:
        single = SC.ModelSpace(SC.PAIRS["perpendicular"][:1], reduced=True)
        b = SC.bloch_hermitian(single, 6)
        out["recursion"] = {
            str(n): {
                "odd": _s(SC.odd_even(b["H"][n], 0, 0)[0]),
                "even": _s(SC.odd_even(b["H"][n], 0, 0)[1]),
            }
            for n in range(7)
        }
        f = SC.folded_words(single, 6)
        out["recursion_equals_word_formula"] = {str(n): b["H"][n] == f[f"H{n}"] for n in (2, 4, 6)}
        out["pieces"] = {
            name: {"odd": _s(SC.odd_even(mat, 0, 0)[0]), "even": _s(SC.odd_even(mat, 0, 0)[1])}
            for name, mat in f["pieces"].items()
        }
        vac = SC.ModelSpace(SC.PAIRS["perpendicular"][:1], reduced=True, vacuum=True)
        bv = SC.bloch_hermitian(vac, 6)
        out["vacuum"] = {str(n): _s(bv["H"][n][0][0]) for n in range(7)}
        out["audit"] = {
            "max_weingarten_n": S.stats["max_weingarten_n"],
            "max_charge": S.stats["max_charge"],
            "components_verified": S.stats["components_verified"],
            "resolvent_denominators": S.resolvent_denominators(),
        }
    ch = CH.bloch_series(6, CH.PLAQUETTE, sign=1)
    chv = CH.bloch_series(6, CH.VACUUM, sign=1)
    out["characters"] = {
        "odd": [_s(x) for x in ch["odd"]],
        "even": [_s(x) for x in ch["even"]],
        "vacuum": [_s(x) for x in chv["energies"]],
        "K_symmetric": ch["symmetric"],
    }
    out["recursion_equals_characters"] = {
        "odd": [out["recursion"][str(n)]["odd"] == out["characters"]["odd"][n] for n in range(7)],
        "even": [
            out["recursion"][str(n)]["even"] == out["characters"]["even"][n] for n in range(7)
        ],
        "vacuum": [out["vacuum"][str(n)] == out["characters"]["vacuum"][n] for n in range(7)],
    }
    out["seconds"] = time.time() - t0
    _dump("single", out)
    return out


def stage_pair(which: str, order: int = 6) -> dict:
    """One shared-link pair over Q(N) through ``order`` by the word formula (F6),
    the vacuum by the Bloch recursion; ``order = 4`` is the fast (about a minute)
    record used to validate the expand/symbol pipeline and the suite's pair
    checks before the sixth-order stages finish."""
    t0 = time.time()
    out: dict = {
        "cluster": which,
        "faces": SC.PAIRS[which],
        "min_rank": MIN_RANK,
        "order": order,
    }
    with SR.Symbolic(min_rank=MIN_RANK) as S:
        space = SC.ModelSpace(SC.PAIRS[which], reduced=True)
        # the word formula (F6): ten times faster than the Bloch recursion on a pair
        # over Q(N) at order four (44 s against 446 s) and the only engine that
        # records the seven pieces; the two agree entry by entry at orders 2 and 4
        # on both pairs (validate.json) and at order 6 on one face (single.json)
        f = SC.folded_words(space, order)
        out["engine"] = "folded_words"
        out["elements"] = {}
        for n in range(2, order + 1, 2):
            hop = SC.odd_even(f[f"H{n}"], 0, 1)
            site = SC.odd_even(f[f"H{n}"], 0, 0)
            out["elements"][str(n)] = {
                "hop_odd": _s(hop[0]),
                "hop_even": _s(hop[1]),
                "site_odd": _s(site[0]),
                "site_even": _s(site[1]),
            }
        out["pieces"] = {
            name: {
                "hop_odd": _s(SC.odd_even(mat, 0, 1)[0]),
                "hop_even": _s(SC.odd_even(mat, 0, 1)[1]),
                "site_odd": _s(SC.odd_even(mat, 0, 0)[0]),
                "site_even": _s(SC.odd_even(mat, 0, 0)[1]),
            }
            for name, mat in f["pieces"].items()
        }
        vac = SC.ModelSpace(SC.PAIRS[which], reduced=True, vacuum=True)
        bv = SC.bloch_hermitian(vac, order)
        out["vacuum"] = {str(n): _s(bv["H"][n][0][0]) for n in range(order + 1)}
        out["audit"] = {
            "max_weingarten_n": S.stats["max_weingarten_n"],
            "max_charge": S.stats["max_charge"],
            "components_verified": S.stats["components_verified"],
            "resolvent_denominators": S.resolvent_denominators(),
        }
    out["seconds"] = time.time() - t0
    _dump(f"pair_{which}" if order == 6 else f"pair_{which}_h{order}", out)
    return out


N_ = sp.Symbol("N")


def expansion(expr: str, terms: int = 4) -> list:
    """Leading terms of the 1/N expansion of a rational function of N: [[power, coeff], ...]."""
    x = sp.Symbol("x")
    e = sp.cancel(sp.sympify(expr, locals={"N": N_}))
    if e == 0:
        return []
    s = sp.series(e.subs(N_, 1 / x), x, 0, 60).removeO()
    poly = sp.Poly(sp.expand(s), x)
    mons = sorted(poly.as_dict().items())
    return [[int(k[0]), str(c)] for k, c in mons[:terms]]


def leading_power(expr: str):
    ex = expansion(expr, 1)
    return ex[0][0] if ex else None


def stage_expand() -> dict:
    out: dict = {}
    single = _load("single")
    out["single"] = {}
    for n in (2, 4, 6):
        vac = single["vacuum"][str(n)]
        rec = single["recursion"][str(n)]
        out["single"][str(n)] = {
            "odd_minus_vacuum": expansion(f"({rec['odd']})-({vac})"),
            "even_minus_vacuum": expansion(f"({rec['even']})-({vac})"),
            "odd_minus_even": expansion(f"({rec['odd']})-({rec['even']})"),
            "vacuum": expansion(vac),
        }
    out["single"]["pieces"] = {
        name: {"odd": expansion(v["odd"], 2), "even": expansion(v["even"], 2)}
        for name, v in single["pieces"].items()
    }
    pairs = {}
    for which in SC.PAIRS:
        path = HERE / f"pair_{which}.json"
        if not path.exists():
            continue
        pair = pairs[which] = _load(f"pair_{which}")
        out[which] = {}
        for n in range(2, pair.get("order", 6) + 1, 2):
            el = pair["elements"][str(n)]
            site_single = single["recursion"][str(n)]
            vac_pair, vac_single = pair["vacuum"][str(n)], single["vacuum"][str(n)]
            out[which][str(n)] = {
                "hop_odd": expansion(el["hop_odd"]),
                "hop_even": expansion(el["hop_even"]),
                "site_odd_cumulant": expansion(
                    f"({el['site_odd']})-({site_single['odd']})-(({vac_pair})-({vac_single}))"
                ),
                "site_even_cumulant": expansion(
                    f"({el['site_even']})-({site_single['even']})-(({vac_pair})-({vac_single}))"
                ),
                "vacuum_pair_minus_single": expansion(f"({vac_pair})-({vac_single})"),
            }
    if len(pairs) == 2:
        out["symbol"] = pair_symbol(pairs["coplanar"], pairs["perpendicular"])
    _dump("expand", out)
    return out


def pair_symbol(coplanar: dict, perpendicular: dict) -> dict:
    """The two pair hops placed into the carrier symbol, order by order.

    In the kernel's (0,2) basis the in-plane orbit amplitude is the coplanar
    shared-link hop and the rotation orbit amplitude the perpendicular one:
    pi_n = hop_odd(coplanar), rho_n = hop_odd(perpendicular). The sign is the
    second-order kernel's: it is t_N times the down Laplacian off the diagonal,
    whose entries are -1 on coplanar and +1 on perpendicular neighbours
    (``kernel_orbits.down_laplacian``), and the recursion's order-2 hops are
    -t_N and +t_N. With ``kernel_orbits.CLOSED_FORMS`` (pi -> 4 e1 - 2 e2,
    rho -> -2 e2) the pair's symbol is T_n = 4 pi_n e1 - 2 (pi_n + rho_n) e2.
    """
    out = {}
    order = min(coplanar.get("order", 6), perpendicular.get("order", 6))
    for n in range(2, order + 1, 2):
        pi = coplanar["elements"][str(n)]["hop_odd"]
        rho = perpendicular["elements"][str(n)]["hop_odd"]
        e1 = sp.cancel(4 * sp.sympify(pi, locals={"N": N_}))
        e2 = sp.cancel(-2 * (sp.sympify(pi, locals={"N": N_}) + sp.sympify(rho, locals={"N": N_})))
        out[str(n)] = {
            "pi": pi,
            "rho": rho,
            "pi_plus_rho": str(sp.cancel(e2 / -2)),
            "e1_coefficient": str(e1),
            "e2_coefficient": str(e2),
            "e1_expansion": expansion(str(e1)),
            "e2_expansion": expansion(str(e2)),
        }
    return out


def stage_certificate() -> dict:
    cert: dict = {
        "schema": "g9-direct-h6-pair/v1",
        "validation_rank": VALIDATION_RANK,
        "min_rank": MIN_RANK,
    }
    for name in ("validate", "single", "expand"):
        cert[name] = _load(name)
    for which in SC.PAIRS:
        if (HERE / f"pair_{which}.json").exists():
            cert[f"pair_{which}"] = _load(f"pair_{which}")
    _dump("certificate", cert)
    return cert


STAGES = {
    "validate": stage_validate,
    "single": stage_single,
    "pair_perpendicular": lambda: stage_pair("perpendicular"),
    "pair_coplanar": lambda: stage_pair("coplanar"),
    "pair_perpendicular_h4": lambda: stage_pair("perpendicular", 4),
    "pair_coplanar_h4": lambda: stage_pair("coplanar", 4),
    "expand": stage_expand,
    "certificate": stage_certificate,
}


if __name__ == "__main__":
    names = sys.argv[1:] or list(STAGES)
    for name in names:
        print(f"== {name}", flush=True)
        STAGES[name]()
