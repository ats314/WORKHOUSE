"""Private-link paths as single links, and universality history by history (ADR 0030).

The first two steps of the plan for proving the channel-wise universality
behind the tier collapse (G14). Step 1: a face's private links enter every
history word only through their product along the face, so by Peter-Weyl a
path of k private links is one Haar link with k times the single-link H0;
``loopcalc.reduced_words`` collapses every cluster accordingly and the
reduced cluster computes the same cumulant channel by channel, five to ten
times faster. Step 2's first probes: on the reduced clusters the two-hop
weight agrees between the straight and the L-shaped chain for every
time-ordered insertion sequence separately, and integrand by integrand
within each; the single-contact dressing agrees history by history once the
two geometries are matched (time reversed, end roles swapped, one end face
conjugated). The record is ``runs/path_reduction_2026-09-04``.
"""

from __future__ import annotations

import json
from fractions import Fraction as F
from functools import cache

from .. import loopcalc as LC
from ._core import ROOT, _suite

reduction = _suite("private-link paths as single links; universality history by history")

_RUN = "runs/path_reduction_2026-09-04"
_CITE = "G14; " + _RUN + "; ADR 0030; ADR 0029; ADR 0026"
_P = ((0, 1), (0, 0, 0))
_Q_COP = ((0, 1), (1, 0, 0))


@cache
def _cert() -> dict:
    return json.loads((ROOT / _RUN / "certificate.json").read_text(encoding="utf-8"))


_REDUCED = (
    "a private-link path is one effective link with k times the single-link H0: every "
    "three-cluster cumulant of the beta_N assembly is the same, channel by channel in both "
    "sectors, on the reduced cluster as on the full one"
)


@reduction.check(
    _REDUCED,
    _CITE,
    rests_on=(
        "the 74 channels of u are identities in Q(N): every closed form of the pinned "
        "reconstruction is the symbolic channel exactly, and the finer per-link labelling adds "
        "only channels that vanish in the C-odd sector",
    ),
)
def _():
    # Live: the reduced coplanar pair's second-order hop and the reduced
    # two-hop chain at N = 3, against the registered constants. Pinned: eight
    # clusters over Q(N), every channel of both sectors equal between the
    # reduced and the full cluster, with the effective-link weights recorded.
    pair = LC.Cluster([_P, _Q_COP], reduced=True)
    h2, _v2 = pair.second_order()
    w = LC.cumulant([_P, _Q_COP, ((0, 1), (2, 0, 0))], 1, reduced=True)
    live = (
        LC.codd(h2, 0, 1) == F(-5, 612)
        and LC.ceven(h2, 0, 1) == F(-11, 306)
        and LC.block_odd(w) == F(360421351, 40327601932800)
        and LC.block_even(w) == F(948253471, 40327601932800)
    )
    rows = _cert()["reduced_vs_full"]
    pinned = all(
        r[s]["same_keys"]
        and r[s]["equal_channels"] == r[s]["channels_full"] == r[s]["channels_reduced"]
        and r[s]["totals_equal"]
        for r in rows.values()
        for s in ("odd", "even")
    )
    weights = {name: r["effective_link_weights"] for name, r in rows.items()}
    speed = min(r["seconds_full"] / max(r["seconds_reduced"], 0.1) for r in rows.values())
    ok = live and pinned and len(rows) == 8 and weights["u_coplanar"] == [3, 3]
    counts = ", ".join(
        f"{k}: {v['odd']['channels_full']}+{v['even']['channels_full']}" for k, v in rows.items()
    )
    return ok, (
        "live at N = 3: the reduced pair hops -5/612 and -11/306, the reduced chain gives "
        f"X_QUANTUM and u_even; pinned: {len(rows)} clusters over Q(N), every channel of both "
        f"sectors equal ({counts}); effective-link weights {weights}; at least {speed:.0f}x faster"
    )


_BY_HISTORY = (
    "universality of the two-hop weight holds history by history: the straight and the L-shaped "
    "chain agree in every (insertion sequence, channel) term of the direct term, and integrand "
    "by integrand within each term"
)


@reduction.check(_BY_HISTORY, _CITE + "; ADR 0019", rests_on=(_REDUCED,))
def _():
    # ADR 0029 found u universal channel by channel; here the C-odd direct
    # term is split further by the time-ordered sequence of the four inserted
    # faces. Every term agrees with ratio 1, and inside each term the final
    # integrands -- coefficient times Haar integral -- form the same multiset
    # of values in both geometries, although the words themselves differ
    # (the middle face's private links are two links in one chain and one
    # doubled link in the other). That is the level a proof must work at.
    h = _cert()["by_history"]
    u = h["u_L_vs_u_coplanar"]["identity"]
    integ = h["u_integrands"]
    ok = (
        u["ratios"] == {"1": u["terms"]}
        and u["one_sided"] == 0
        and u["terms"] == 124
        and integ["value_multisets_equal"] == integ["terms"] == 124
        and integ["abstract_word_sets_equal"] == 0
    )
    return ok, (
        f"{u['terms']} (sequence, channel) terms over {len(h['sequences']['u_coplanar'])} "
        "insertion sequences, every ratio L/straight = 1, none one-sided; the value multisets "
        f"of the final integrands agree in all {integ['terms']} terms while the abstract words "
        f"agree in {integ['abstract_word_sets_equal']}: a value-preserving bijection of "
        "integrands, not a coincidence of sums"
    )


_SINGLE_BY_HISTORY = (
    "the single-contact dressing agrees history by history between its two geometries once "
    "time is reversed, the end roles are swapped and one end face is conjugated: every "
    "(sequence, channel) term has ratio -1"
)


@reduction.check(_SINGLE_BY_HISTORY, _CITE, rests_on=(_REDUCED,))
def _():
    # The straight chain dresses Q, the L-shaped chain dresses P. Read with
    # the roles as they stand no term matches; reversing the sequence and
    # the labels alone matches none either; reversing, swapping P and Q and
    # conjugating P matches every term with the incidence sign -1. This is
    # the history-level form of ADR 0029's corrected channel comparison.
    s = _cert()["by_history"]["single_cop_vs_single_perp"]
    ok = (
        s["identity"]["one_sided"] == s["identity"]["terms"] == 128
        and s["reverse"]["one_sided"] == 128
        and s["reverse_swap_conjP"]["ratios"] == {"-1": 128}
        and s["reverse_swap_conjP"]["one_sided"] == 0
    )
    return ok, (
        f"{s['identity']['terms']} terms: naive pairing matches none, reversal alone matches "
        f"none, reversal with the end roles swapped and P conjugated matches all with ratio -1"
    )


_RESIDUALS_RUN = "runs/vertex_residuals_2026-09-04"

_RESIDUALS = (
    "where the identity lives: after every private path is integrated, the straight and the "
    "L chain leave the same formal word in the two shared links, coefficient for coefficient, in "
    "every (sequence, channel) term; after the middle face's private links alone they do not"
)


@reduction.check(_RESIDUALS, _CITE + "; " + _RESIDUALS_RUN + "; ADR 0031", rests_on=(_BY_HISTORY,))
def _():
    # Each final integrand is Haar-integrated over some of its links (balanced
    # n = 1 families, so each integration is the cut delta delta / N), adjacent
    # U U~ pairs are cancelled, and the residual words over the role alphabet
    # are summed. Integrating the middle face's private links only leaves
    # different functions of the shared links and the end paths in the two
    # geometries -- the L chain threads the end paths through one trace with
    # both shared links, the straight chain does not; integrating the end
    # paths too leaves literally the same word. The lemma behind universality
    # is therefore about the fully contracted two-link word.
    cert = json.loads((ROOT / _RESIDUALS_RUN / "certificate.json").read_text(encoding="utf-8"))
    partial = cert["stages"]["xpriv"]
    full = cert["stages"]["xpriv,wP,wQ"]
    pairs = cert["stages"]["pairs"]
    ok = (
        full["residual_vectors_equal"] == full["terms"] == 124
        and full["totals_equal"] == 124
        and partial["totals_equal"] == 124
        and partial["residual_vectors_equal"] < partial["terms"]
        and set(full["residual_words_straight"]) == set(full["residual_words_L"]) == {"()"}
        and pairs["coefficient_and_value_pair_multisets_equal"] == 124
        and max(
            int(k.split("(")[1].split(")")[0].split(",")[-1] or 0) for k in pairs["family_sizes"]
        )
        <= 3
    )
    return ok, (
        f"integrating the middle face's private links only: residual vectors equal in "
        f"{partial['residual_vectors_equal']} of {partial['terms']} terms (totals equal in all); "
        f"integrating the end paths as well: equal in {full['residual_vectors_equal']} of "
        f"{full['terms']}, every term reducing to the empty word; per integrand, the (Fierz "
        f"coefficient, Haar integral) pairs agree as multisets in "
        f"{pairs['coefficient_and_value_pair_multisets_equal']} of {pairs['terms']} terms over "
        f"{pairs['integrands_straight']} integrands, with Haar families of size at most three"
    )


_LEMMA_RUN = "runs/universality_lemma_2026-09-04"

_LEMMA = (
    "the universality lemma, by exhaustion on the fourth-order family: phi (delete the second "
    "private letter of the straight middle face, keep the first as the weight-two link) maps every "
    "history's straight integrand onto its L integrand with the same coefficient, and preserves "
    "the Haar integral on every word the Fierz swaps and cuts can generate from the face words"
)


@reduction.check(
    _LEMMA, _CITE + "; " + _LEMMA_RUN + "; ADR 0032", rests_on=(_RESIDUALS, _BY_HISTORY)
)
def _():
    # The record enumerates the family a fourth-order history can produce -- a
    # product of face words, then any permutation of out-targets within each
    # shared link's letters (every permutation, a superset of the like-pair
    # swaps), then the Fierz cuts of unlike pairs with their closed loops
    # counted, never X's own letter with X~'s -- and checks integrate(w) ==
    # integrate(phi(w)) on all of it for the multiplicities fourth order
    # reaches, exhaustively where the count allows. The control shows the
    # identity is a property of the family: on arbitrary wirings of the same
    # letters phi does not preserve the integral, and cutting a pair no history
    # can cut breaks it too.
    cert = json.loads((ROOT / _LEMMA_RUN / "certificate.json").read_text(encoding="utf-8"))
    a = cert["parts"]["A_phi_on_histories"]
    fam = cert["parts"]["B_C_family"]
    ctrl = cert["parts"]["D_control"]
    exhaustive = [k for k, v in fam.items() if v["exhaustive"]]
    ok = (
        a["terms"]
        == a["terms_where_phi_is_a_bijection_onto_L"]
        == a["terms_with_equal_coefficients"]
        == 124
        and a["integrands_straight"] == 536
        and all(v["phi_invariant"] == v["words"] for v in fam.values())
        and fam["swaps a=1 b=1"]["words"] == 576
        and fam["swaps a=2 b=1"]["words"] == fam["swaps a=1 b=2"]["words"] == 17280
        and fam["swaps a=b=1 over Q(N)"]["words"] == 576
        and fam["reachable swaps then cuts a=1 b=1"]["words"] == 384
        and len(exhaustive) >= 5
        and all(v["phi_invariant"] < v["words"] for v in ctrl.values())
    )
    total = sum(v["words"] for v in fam.values())
    families = ", ".join(
        f"{k}: {v['words']}" + ("" if v["exhaustive"] else " sampled") for k, v in fam.items()
    )
    controls = ", ".join(f"{k}: {v['phi_invariant']}/{v['words']}" for k, v in ctrl.items())
    return ok, (
        "phi is a coefficient-preserving bijection of integrands in "
        f"{a['terms_where_phi_is_a_bijection_onto_L']} of {a['terms']} history terms "
        f"({a['integrands_straight']} integrands); the Haar integral is phi-invariant on all "
        f"{total} words of the swap and cut families checked ({families}); on arbitrary wirings "
        f"it is not ({controls})"
    )
