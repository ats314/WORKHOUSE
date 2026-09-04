"""Private-link paths as single links, and universality history by history, over Q(N).

    python reduce.py > console.log

Step 1 of the universality plan (G14). A face's private links -- those in no
other face of the cluster -- enter every history word only through their
product along the face, and D^r(U_a U_b U_c) = D^r(U_a) D^r(U_b) D^r(U_c), so a
path of k private links is one Haar link whose single-link H0 is k times the
usual one. ``loopcalc.reduced_words`` collapses every maximal private run to
such a link (``LINK_WEIGHT``). Part 1 recomputes every three-cluster cumulant
of the beta_N assembly on the reduced cluster, channel by channel, and
compares with the full cluster: same channels, same rational functions.

Step 2's first probe. Part 2 tags the direct term of the two-hop weight and
of the single-contact dressing by the time-ordered sequence of inserted faces
as well as by the channel labels, on the reduced clusters, and compares the
straight geometry with the L-shaped one term by term. For u the two chains
agree in every (sequence, channel) term; for the single contact they agree
in every term once the correspondence is the right one: the straight chain
dresses Q where the L chain dresses P, so time runs the other way (the
sequence and the labels reversed), the end roles swap, and one end face is
conjugated -- the incidence sign.

Part 3 goes one level finer still: for every (sequence, channel) term of the
two-hop weight, the final integrands -- the words whose Haar integrals the
term sums, each with its coefficient times its integral -- are compared as
multisets of values between the straight and the L chain. They coincide term
by term: the two geometries' history expansions are in value-preserving
bijection integrand by integrand, which is the level at which a proof of
universality has to work.

Writes certificate.json.
"""

from __future__ import annotations

import json
import sys
import time
from collections import Counter, defaultdict
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
sys.path.insert(0, str(ROOT / "src"))

from workhouse import loopcalc as L  # noqa: E402
from workhouse import symbolic_rank as SR  # noqa: E402

P = ((0, 1), (0, 0, 0))
Q_COP = ((0, 1), (1, 0, 0))
Q_PERP = ((0, 2), (0, 0, 0))
CLUSTERS = {
    "u_coplanar": ([P, Q_COP, ((0, 1), (2, 0, 0))], 1),
    "u_L": ([P, Q_COP, ((0, 1), (1, 1, 0))], 1),
    "u_bent": ([P, Q_PERP, ((0, 1), (0, 0, 1))], 1),
    "single_perp": ([P, ((0, 1), (1, 0, 0)), Q_PERP], 1),
    "single_cop": ([P, ((0, 1), (2, 0, 0)), Q_COP], 1),
    "fan_perp": ([P, ((0, 1), (0, -1, 0)), Q_PERP], 1),
    "fan_cop": ([P, ((1, 2), (1, 0, 0)), Q_COP], 1),
    "corner": ([P, ((1, 2), (1, 0, 0)), Q_PERP], 1),
}
T0 = time.time()
out = {"schema": "path_reduction/v1", "field": "Q(N)", "reduced_vs_full": {}, "by_history": {}}


def ratio_key(r: SR.RF) -> str:
    return str(r.at(0)) if r.num.degree() <= 0 and r.den.degree() <= 0 else str(r.to_sympy())


# ---------------------------------------------------------------- part 1
with SR.Symbolic():
    for name, (faces, x_index) in CLUSTERS.items():
        t = time.time()
        full = SR.channels(faces, x_index)
        t_full = time.time() - t
        t = time.time()
        reduced = SR.channels(faces, x_index, reduced=True)
        t_red = time.time() - t
        row = {}
        for sector, idx in (("odd", 0), ("even", 1)):
            f = {k: SR.blocks(v)[idx] for k, v in full.items()}
            r = {k: SR.blocks(v)[idx] for k, v in reduced.items()}
            f = {k: v for k, v in f.items() if v}
            r = {k: v for k, v in r.items() if v}
            row[sector] = {
                "channels_full": len(f),
                "channels_reduced": len(r),
                "same_keys": set(f) == set(r),
                "equal_channels": sum(1 for k in f if k in r and f[k] == r[k]),
                "totals_equal": sum(f.values(), SR.RF(0)) == sum(r.values(), SR.RF(0)),
            }
        words = L.Cluster(faces, reduced=True).words
        weights = sorted(
            L.link_weight(lk) for w in words[::2] for lk, _o in w[0] if L.link_weight(lk) > 1
        )
        row["effective_link_weights"] = weights
        row["seconds_full"] = round(t_full, 1)
        row["seconds_reduced"] = round(t_red, 1)
        out["reduced_vs_full"][name] = row
        print(
            f"[{time.time() - T0:6.1f}s] {name}: full {t_full:.1f}s, reduced {t_red:.1f}s; "
            f"C-odd {row['odd']['equal_channels']}/{row['odd']['channels_full']} equal, "
            f"C-even {row['even']['equal_channels']}/{row['even']['channels_full']} equal; "
            f"weights {weights}",
            flush=True,
        )


# ---------------------------------------------------------------- part 2
def apply_V_indexed(cl, vec):
    return {j: L.multiply(vec, w) for j, w in enumerate(cl.words)}


def resolvent_labelled(vec, e0):
    res: dict = defaultdict(dict)
    for e, per_link, comp in SR.labelled_components(vec):
        if e != e0:
            lab = SR.state_label(per_link)
            res[lab] = L.vadd(res[lab], comp, 1 / (e0 - e))
    return res


def direct_by_history(faces3, x_index):
    """The C-odd direct term keyed by (time-ordered roles of the four insertions, l1, l2, l3)."""
    cl3 = L.Cluster(faces3, reduced=True)
    end_ids = [k for k in range(6) if k // 2 != x_index]
    xs = {2 * x_index, 2 * x_index + 1}
    e0 = cl3.e0
    kets = {}
    for a in (0, 1):
        stage: dict = {}
        for s1, v1 in apply_V_indexed(cl3, {cl3.words[end_ids[a]]: SR.RF(1)}).items():
            if not v1:
                continue
            for l1, c1 in resolvent_labelled(v1, e0).items():
                for s2, v2 in apply_V_indexed(cl3, c1).items():
                    if not v2:
                        continue
                    for l2, c2 in resolvent_labelled(v2, e0).items():
                        key = (s1, s2, l1, l2)
                        stage[key] = L.vadd(stage.get(key, {}), c2)
        kets[a] = stage
    bras = {}
    for b in (2, 3):
        stage = {}
        for s4, v1 in apply_V_indexed(cl3, {cl3.words[end_ids[b]]: SR.RF(1)}).items():
            if not v1:
                continue
            for l3, c3 in resolvent_labelled(v1, e0).items():
                for s3, v2 in apply_V_indexed(cl3, c3).items():
                    if v2:
                        key = (s3, s4, l3)
                        stage[key] = L.vadd(stage.get(key, {}), v2)
        bras[b] = stage

    def role(j):
        face, conj = j // 2, j % 2
        if face == x_index:
            return "X~" if conj else "X"
        if face == end_ids[0] // 2:
            return "P~" if conj else "P"
        return "Q~" if conj else "Q"

    res: dict = defaultdict(SR.RF)
    for a in (0, 1):
        for b in (2, 3):
            sign = (1 if a == 0 else -1) * (1 if b == 2 else -1)
            for (s1, s2, l1, l2), kv in kets[a].items():
                for (s3, s4, l3), bv in bras[b].items():
                    if not any(s in xs for s in (s1, s2, s3, s4)):
                        continue
                    tot = SR.RF(0)
                    for w, c in bv.items():
                        tot += c * L.inner(w, kv)
                    if tot:
                        res[((role(s1), role(s2), role(s3), role(s4)), l1, l2, l3)] += sign * tot / 2
    return {k: v for k, v in res.items() if v}


SWAP = {"P": "Q", "P~": "Q~", "Q": "P", "Q~": "P~", "X": "X", "X~": "X~"}
CONJ_P = {"P": "P~", "P~": "P", "Q": "Q", "Q~": "Q~", "X": "X", "X~": "X~"}


def correspond(key, reverse=False, swap=False, conj_p=False):
    seq, l1, l2, l3 = key
    if reverse:
        seq, (l1, l2, l3) = tuple(reversed(seq)), (l3, l2, l1)
    if swap:
        seq = tuple(SWAP[r] for r in seq)
    if conj_p:
        seq = tuple(CONJ_P[r] for r in seq)
    return (seq, l1, l2, l3)


def compare(a: dict, b: dict, **mapping) -> dict:
    ratios: Counter = Counter()
    one_sided = 0
    for key, value in a.items():
        other = b.get(correspond(key, **mapping))
        if other is None:
            one_sided += 1
        else:
            ratios[ratio_key(other / value)] += 1
    return {"ratios": dict(ratios), "one_sided": one_sided, "terms": len(a)}


with SR.Symbolic():
    hist = {}
    for name in ("u_coplanar", "u_L", "single_perp", "single_cop"):
        t = time.time()
        hist[name] = direct_by_history(*CLUSTERS[name])
        print(
            f"[{time.time() - T0:6.1f}s] {name}: {len(hist[name])} (history, channel) terms over "
            f"{len({k[0] for k in hist[name]})} insertion sequences in {time.time() - t:.1f}s",
            flush=True,
        )
    out["by_history"]["u_L_vs_u_coplanar"] = {
        "identity": compare(hist["u_coplanar"], hist["u_L"]),
    }
    out["by_history"]["single_cop_vs_single_perp"] = {
        "identity": compare(hist["single_perp"], hist["single_cop"]),
        "reverse": compare(hist["single_perp"], hist["single_cop"], reverse=True),
        "reverse_swap_conjP": compare(
            hist["single_perp"], hist["single_cop"], reverse=True, swap=True, conj_p=True
        ),
    }
    out["by_history"]["sequences"] = {
        name: sorted(" ".join(s) for s in {k[0] for k in hist[name]}) for name in hist
    }
    for name, rows in out["by_history"].items():
        if name != "sequences":
            print(name, json.dumps(rows), flush=True)


# ---------------------------------------------------------------- part 3
def abstract(word):
    """Links relabelled by first appearance, each tagged with its weight."""
    order: dict = {}
    res = []
    for tr in word:
        t = []
        for lk, o in tr:
            if lk not in order:
                order[lk] = (len(order), L.link_weight(lk))
            t.append((order[lk], o))
        res.append(tuple(t))
    return tuple(res)


def integrand_values(faces3, x_index, seq_roles, labels):
    """For one (sequence, channel) term: {abstract integrand: coefficient x Haar integral}
    summed over the four C-odd entries with their signs."""
    cl3 = L.Cluster(faces3, reduced=True)
    end_ids = [k for k in range(6) if k // 2 != x_index]

    def role(j):
        face, conj = j // 2, j % 2
        if face == x_index:
            return "X~" if conj else "X"
        if face == end_ids[0] // 2:
            return "P~" if conj else "P"
        return "Q~" if conj else "Q"

    idx = {role(j): j for j in range(6)}
    s1, s2, s3, s4 = (idx[r] for r in seq_roles)
    l1, l2, l3 = labels
    e0 = cl3.e0

    def step(vec, s, lab):
        v = L.multiply(vec, cl3.words[s])
        res: dict = {}
        for e, per_link, comp in SR.labelled_components(v):
            if e != e0 and SR.state_label(per_link) == lab:
                res = L.vadd(res, comp, 1 / (e0 - e))
        return res

    values: dict = defaultdict(SR.RF)
    for a in (0, 1):
        for b in (2, 3):
            sign = (1 if a == 0 else -1) * (1 if b == 2 else -1)
            ket = step(step({cl3.words[end_ids[a]]: SR.RF(1)}, s1, l1), s2, l2)
            bra = L.multiply(step({cl3.words[end_ids[b]]: SR.RF(1)}, s4, l3), cl3.words[s3])
            for w, c in bra.items():
                bc = L.conj(w)
                for w2, c2 in ket.items():
                    prod = L.product(bc, w2)
                    val = c * c2 * L.integrate(prod)
                    if val:
                        values[abstract(prod)] += sign * val / 2
    return {k: v for k, v in values.items() if v}


with SR.Symbolic():
    faces_s, faces_l = CLUSTERS["u_coplanar"][0], CLUSTERS["u_L"][0]
    t = time.time()
    terms = sorted(hist["u_coplanar"], key=str)
    multiset_equal = 0
    words_equal = 0
    total_words = 0
    for key in terms:
        seq, lab = key[0], key[1:]
        vs = integrand_values(faces_s, 1, seq, lab)
        vl = integrand_values(faces_l, 1, seq, lab)
        ms = Counter(str(v.to_sympy()) for v in vs.values())
        ml = Counter(str(v.to_sympy()) for v in vl.values())
        multiset_equal += ms == ml
        words_equal += set(vs) == set(vl)
        total_words += len(vs)
    out["by_history"]["u_integrands"] = {
        "terms": len(terms),
        "value_multisets_equal": multiset_equal,
        "abstract_word_sets_equal": words_equal,
        "integrands_in_straight_chain": total_words,
        "seconds": round(time.time() - t, 1),
    }
    print("u integrands:", json.dumps(out["by_history"]["u_integrands"]), flush=True)
L.set_rank(3)
out["seconds"] = round(time.time() - T0, 1)
(HERE / "certificate.json").write_text(json.dumps(out, indent=1) + "\n", encoding="utf-8", newline="\n")
print("wrote certificate.json in", out["seconds"], "s")
