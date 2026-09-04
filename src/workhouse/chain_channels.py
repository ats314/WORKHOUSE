"""The two-hop cumulant by channel: every contribution tagged by the irreps of its doubled links.

The two-hop weight ``u`` is the fourth-order cumulant ``W(P,Q,R) - W(P,R)`` of a
three-plaquette chain, and ADR 0019 made it the one dynamical input of the
Hodge form. In the third engine every resolvent is applied as a sum of exact
``H0`` eigencomponents, so every history's contribution can be tagged by the
energies of its three intermediate states. Above the rest energy ``E0`` those
energies are, in units of ``C_F/2``, an even number of extra fundamental links
plus, for each link the history has doubled, the excess of that link's irrep:
``0`` for the merged singlet, ``2(N-2)/(N-1)`` for ``Lambda^2 F``, ``2N^2/(N^2-1)``
for the adjoint, ``2(N+2)/(N+1)`` for ``Sym^2 F``. The labels are therefore
rank-independent, and each labelled channel is a rational function of ``N``
of low degree -- a product of the resolvent factors its irreps bring.

This module computes the tagged decomposition at one rank (``decompose``) and
labels it (``label_energy``); the closed forms and the chain comparison live
in the all-rank suite and its run record.
"""

from __future__ import annotations

import itertools
from collections import defaultdict
from fractions import Fraction as F

from . import loopcalc as L

COPLANAR = (((0, 1), (0, 0, 0)), ((0, 1), (1, 0, 0)), ((0, 1), (2, 0, 0)))
BENT = (((0, 1), (0, 0, 0)), ((0, 2), (0, 0, 0)), ((0, 1), (0, 0, 1)))


def excess_table(n: int) -> dict:
    """Energy excess of a doubled link's irrep over two fundamental links, in units of C_F/2."""
    return {
        "0": F(0),
        "lam": F(2 * (n - 2), n - 1),
        "adj": F(2 * n * n, n * n - 1),
        "sym": F(2 * (n + 2), n + 1),
    }


def label_energy(n: int, excess_units, position: str):
    """(extra fundamental links, sorted irrep excesses) for an energy above E0.

    ``position`` fixes what the state can be. After one insertion (``"outer"``:
    the first and third resolvents of the direct term, and both resolvents of
    the fold term) the state is the merged six-link loop, 2 extra links, with
    its one doubled link in any irrep -- or, when the insertion is the far
    face, two disjoint plaquettes, 4 extra links and nothing doubled. After
    two insertions (``"middle"``) it is 4 extra links with two doubled links in
    any irreps. Restricting the search to those shapes removes the accidental
    coincidences of small ranks (at N = 3, ``4 + 2 lam = 6`` and
    ``4 + sym = 2 + 2 adj``)."""
    ex = excess_table(n)
    names = ("lam", "adj", "sym")
    shapes = [(4, k) for k in (0, 1, 2)] if position == "middle" else [(2, 0), (2, 1), (4, 0)]
    for base, k in shapes:
        for combo in itertools.combinations_with_replacement(names, k):
            if base + sum(ex[c] for c in combo) == excess_units:
                return (base, combo)
    return None


def _resolvent_tagged(vec: dict, e0: F) -> dict:
    out = defaultdict(dict)
    for e, comp in L.eigen_components(vec):
        if e != e0:
            out[e] = L.vadd(out[e], comp, 1 / (e0 - e))
    return out


def _apply_V_flagged(cl, vec, flag, x_words):
    out = {False: {}, True: {}}
    for w in cl.words:
        f = flag or (w in x_words)
        out[f] = L.vadd(out[f], L.multiply(vec, w))
    return out


def direct_by_energy(faces3, x_index: int) -> dict:
    """The C-odd direct term of the cumulant, tagged by (E1, E2, E3)."""
    cl3 = L.Cluster(faces3)
    ends = [f for k, f in enumerate(faces3) if k != x_index]
    cl2 = L.Cluster(ends)
    x_words = {cl3.words[2 * x_index], cl3.words[2 * x_index + 1]}
    e0 = cl3.e0
    kets = {}
    for a in (0, 1):
        stage = {}
        for f1, vec1 in _apply_V_flagged(cl3, {cl2.words[a]: F(1)}, False, x_words).items():
            if not vec1:
                continue
            for e1, c1 in _resolvent_tagged(vec1, e0).items():
                for f2, vec2 in _apply_V_flagged(cl3, c1, f1, x_words).items():
                    if not vec2:
                        continue
                    for e2, c2 in _resolvent_tagged(vec2, e0).items():
                        key = (e1, e2, f2)
                        stage[key] = L.vadd(stage.get(key, {}), c2)
        kets[a] = stage
    bras = {}
    for b in (2, 3):
        stage = {}
        for f1, vec1 in _apply_V_flagged(cl3, {cl2.words[b]: F(1)}, False, x_words).items():
            if not vec1:
                continue
            for e3, c3 in _resolvent_tagged(vec1, e0).items():
                for f2, vec2 in _apply_V_flagged(cl3, c3, f1, x_words).items():
                    if vec2:
                        key = (e3, f2)
                        stage[key] = L.vadd(stage.get(key, {}), vec2)
        bras[b] = stage
    out = defaultdict(F)
    for a in (0, 1):
        for b in (2, 3):
            sign = (1 if a == 0 else -1) * (1 if b == 2 else -1)
            for (e1, e2, fa), kv in kets[a].items():
                for (e3, fb), bv in bras[b].items():
                    if not (fa or fb):
                        continue
                    tot = F(0)
                    for w, c in bv.items():
                        tot += c * L.inner(w, kv)
                    out[(e1, e2, e3)] += sign * tot / 2
    return {k: v for k, v in out.items() if v}


def fold_by_energy(faces3, x_index: int) -> dict:
    """The C-odd fold difference -(1/2)({H2,V2}_3 - {H2,V2}_2), tagged by (E of H2, E of V2)."""
    cl3 = L.Cluster(faces3)
    ends = [f for k, f in enumerate(faces3) if k != x_index]
    cl2 = L.Cluster(ends)
    e0 = cl3.e0

    def moments(cl):
        m = len(cl.words)
        h2 = defaultdict(lambda: [[F(0)] * m for _ in range(m)])
        v2 = defaultdict(lambda: [[F(0)] * m for _ in range(m)])
        for j in range(m):
            v = cl.V({cl.words[j]: F(1)})
            for e, comp in L.eigen_components(v):
                if e == e0:
                    continue
                vc = cl.V(comp)
                for i in range(m):
                    val = L.inner(cl.words[i], vc)
                    h2[e][i][j] += val / (e0 - e)
                    v2[e][i][j] += val / (e0 - e) ** 2
        return h2, v2

    h3, v3 = moments(cl3)
    h2_, v2_ = moments(cl2)
    ids3 = [k for k in range(6) if k // 2 != x_index]
    out = defaultdict(F)
    for a in (0, 1):
        for b in (2, 3):
            sign = (1 if a == 0 else -1) * (1 if b == 2 else -1)
            for e, hm in h3.items():
                for ep, vm in v3.items():
                    val = (
                        sum(
                            hm[ids3[b]][k] * vm[k][ids3[a]] + vm[ids3[b]][k] * hm[k][ids3[a]]
                            for k in range(6)
                        )
                        / 2
                    )
                    out[("fold3", e, ep)] += -sign * val / 2
            for e, hm in h2_.items():
                for ep, vm in v2_.items():
                    val = sum(hm[b][k] * vm[k][a] + vm[b][k] * hm[k][a] for k in range(4)) / 2
                    out[("fold2", e, ep)] += sign * val / 2
    return {k: v for k, v in out.items() if v}


def decompose(chain, n: int) -> dict:
    """{label: C-odd contribution} at rank n, labels rank-independent; the values sum to u."""
    L.set_rank(n)
    try:
        cf2 = L.CF / 2
        e0 = 4 * cf2
        out = defaultdict(F)
        for (e1, e2, e3), v in direct_by_energy(list(chain), 1).items():
            lab = (
                label_energy(n, (e1 - e0) / cf2, "outer"),
                label_energy(n, (e2 - e0) / cf2, "middle"),
                label_energy(n, (e3 - e0) / cf2, "outer"),
            )
            if any(x is None for x in lab):
                raise ValueError(f"unlabelled energy at N = {n}: {(e1, e2, e3)}")
            out[("direct",) + lab] += v
        for (kind, e, ep), v in fold_by_energy(list(chain), 1).items():
            lab = (
                label_energy(n, (e - e0) / cf2, "outer"),
                label_energy(n, (ep - e0) / cf2, "outer"),
            )
            if any(x is None for x in lab):
                raise ValueError(f"unlabelled fold energy at N = {n}: {(e, ep)}")
            out[(kind,) + lab] += v
        return {k: v for k, v in out.items() if v}
    finally:
        L.set_rank(3)
