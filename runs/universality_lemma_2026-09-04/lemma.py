"""The universality lemma of the two-hop weight, proved by exhaustion on the fourth-order family.

    python lemma.py > console.log

Setting (ADR 0030, 0031). On the reduced clusters the straight and the L two-hop chain
share the end faces P = Tr(U1 W_P), Q = Tr(U2 W_Q) and differ in the middle face:
straight X_S = Tr(U1 A U2 B) with two private links of weight one, L X_L = Tr(U1 U2 C)
with one of weight two. In every surviving fourth-order history the middle face appears
once on each side of the amplitude, so its private letters are never projected; the Fierz
rewirings act only on the shared-link letters, and they do so identically in the two
geometries. Define phi on words: delete A and Ab, joining each one's predecessor to its
successor, and rename B, Bb to C, Cb. phi maps the straight word of every history to the L
word of the same history (part A). Universality is therefore the statement that the Haar
integral is phi-invariant on every word a history can produce.

The family a history can produce is exactly: a product of face words P^a P~^a Q^b Q~^b X X~,
followed by any permutation of the out-targets among the letters on one shared link (the
Fierz swaps generate every such permutation), followed by the Fierz cuts of unlike pairs
of shared-link letters (the wire into each continues to the other's successor, an emptied
cycle counted as a loop of N), never X's own letter with X~'s, which sit on opposite sides. Parts B and C check
``integrate(w) == integrate(phi(w))`` on that whole family for a, b <= 2, the multiplicities
fourth order reaches, at two ranks (a rational function of N of the degrees these
Weingarten sums have is determined by fewer points than that; the small cases are also
checked over Q(N)). Part D is the control: on arbitrary wirings of the same letters, phi
does NOT preserve the integral, so the lemma is a property of the family, not of the map.

Writes certificate.json.
"""

from __future__ import annotations

import json
import random
import sys
import time
from collections import Counter, defaultdict
from itertools import combinations, permutations
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
sys.path.insert(0, str(ROOT / "src"))

from workhouse import loopcalc as L  # noqa: E402
from workhouse import symbolic_rank as SR  # noqa: E402

T0 = time.time()
RANKS = (5, 7)
PARTS = __import__("os").environ.get("PARTS", "ABCD")

# ---------------------------------------------------------------- the abstract family
L1, L2, WP, WQ, LA, LB = 1, 2, 3, 4, 5, 6
# X_S = Tr(U1~ A U2 B): x1 -> A -> x2 -> B -> x1; X~_S = Bb -> xb2 -> Ab -> xb1 -> Bb.
# The L middle face is Tr(U1~ C U2~): C sits where A sits, B is absent, and the second
# shared link is traversed the other way (a relabelling the Haar integral does not see).
FIXED_PRIVATE = {"A": "x2", "B": "x1", "Bb": "xb2", "Ab": "xb1"}


def letters(a: int, b: int, s: int = 1) -> dict:
    let = {}
    for i in range(a):
        let[f"p{i}"], let[f"wP{i}"] = (L1, 1), (WP, 1)
        let[f"pb{i}"], let[f"wPb{i}"] = (L1, -1), (WP, -1)
    for j in range(b):
        let[f"q{j}"], let[f"wQ{j}"] = (L2, -s), (WQ, 1)
        let[f"qb{j}"], let[f"wQb{j}"] = (L2, s), (WQ, -1)
    let.update({"x1": (L1, -1), "x2": (L2, s), "A": (LA, 1), "B": (LB, 1)})
    let.update({"xb1": (L1, 1), "xb2": (L2, -s), "Ab": (LA, -1), "Bb": (LB, -1)})
    return let


def base_succ(a: int, b: int) -> dict:
    succ = {"x1": "A", "x2": "B", "Bb": "xb2", "xb2": "Ab", "Ab": "xb1", "xb1": "Bb"}
    succ.update(FIXED_PRIVATE)
    for i in range(a):
        succ[f"p{i}"], succ[f"wP{i}"] = f"wP{i}", f"p{i}"
        succ[f"pb{i}"], succ[f"wPb{i}"] = f"wPb{i}", f"pb{i}"
    for j in range(b):
        succ[f"q{j}"], succ[f"wQ{j}"] = f"wQ{j}", f"q{j}"
        succ[f"qb{j}"], succ[f"wQb{j}"] = f"wQb{j}", f"qb{j}"
    return succ


def word_of(succ: dict, let: dict):
    seen, traces = set(), []
    for start in succ:
        if start in seen:
            continue
        tr, cur = [], start
        while cur not in seen:
            seen.add(cur)
            tr.append(let[cur])
            cur = succ[cur]
        traces.append(tuple(tr))
    return L.canon(traces)


def delete(succ: dict, names):
    """Remove letters, each one's predecessor taking over its successor; a letter whose
    removal closes an empty cycle is a closed index loop, worth N. Returns (succ, loops)."""
    s2 = dict(succ)
    loops = 0
    for x in names:
        if s2[x] == x:
            del s2[x]
            loops += 1
            continue
        pred = next(k for k, v in s2.items() if v == x)
        s2[pred] = s2[x]
        del s2[x]
    return s2, loops


def cut(succ: dict, s: str, t: str):
    """The Fierz cut of an unlike pair on one link, as the engine performs it: the wire into
    s continues to t's successor and the wire into t to s's successor, both letters removed,
    an emptied cycle counted as a loop. Returns (succ, loops)."""
    s2 = dict(succ)
    ps = next(k for k, v in s2.items() if v == s)
    pt = next(k for k, v in s2.items() if v == t)
    ss, st = s2[s], s2[t]
    if ps == t and pt == s:  # the pair is its own 2-cycle: an empty loop
        del s2[s], s2[t]
        return s2, 1
    if ps == t:  # ... -> t -> s -> ss becomes ... -> ss
        s2[pt] = ss
        del s2[s], s2[t]
        return s2, 0
    if pt == s:
        s2[ps] = st
        del s2[s], s2[t]
        return s2, 0
    s2[ps] = st
    s2[pt] = ss
    del s2[s], s2[t]
    return s2, 0


def phi(succ: dict, let: dict):
    """Delete B and Bb, joining predecessor to successor; A and Ab become the weight-two
    link C. Returns (succ, letters, loops)."""
    s2, loops = delete(succ, ("B", "Bb"))
    let2 = {k: v for k, v in let.items() if k not in ("B", "Bb")}
    return s2, let2, loops


def both(succ, let, rank, loops=0):
    """The two integrals, the word's own closed loops (from cuts) included on both sides."""
    L.set_rank(rank)
    s2, let2, phi_loops = phi(succ, let)
    n = L.F(rank)
    return (
        L.integrate(word_of(succ, let)) * n**loops,
        L.integrate(word_of(s2, let2)) * n ** (loops + phi_loops),
    )


def phi_invariant(succ, let, ranks=RANKS, loops=0) -> bool:
    return all(v1 == v2 for v1, v2 in (both(succ, let, r, loops) for r in ranks))


def swap_family(a: int, b: int, reachable: bool = False):
    """Every word reached from the face words by permuting out-targets within each shared
    link; with ``reachable`` only within letters of one orientation, which is what the Fierz
    swaps (like pairs) generate."""
    let = letters(a, b)
    base = base_succ(a, b)
    groups = []
    for link in (L1, L2):
        if reachable:
            groups.append([n for n, (lk, o) in let.items() if lk == link and o == 1])
            groups.append([n for n, (lk, o) in let.items() if lk == link and o == -1])
        else:
            groups.append([n for n, (lk, _o) in let.items() if lk == link])
    targets = [[base[n] for n in g] for g in groups]

    def rec(i, succ):
        if i == len(groups):
            yield dict(succ), let
            return
        for perm in permutations(targets[i]):
            succ.update(zip(groups[i], perm, strict=True))
            yield from rec(i + 1, succ)

    yield from rec(0, dict(base))


def cut_pairs(let: dict, link: int):
    """The unlike pairs a Fierz cut can act on: a U and a U~ of one shared link that can share
    a resolvent-projected state -- never X's own letter with X~'s, which sit on opposite sides."""
    ups = [n for n, (lk, o) in let.items() if lk == link and o == 1]
    downs = [n for n, (lk, o) in let.items() if lk == link and o == -1]
    xs = {"x1", "xb1", "x2", "xb2"}
    return [(u, d) for u in ups for d in downs if not (u in xs and d in xs)]


def cut_sets(let: dict, link: int):
    """Every set of up to two disjoint reachable cuts on one link, the empty set included."""
    pairs = cut_pairs(let, link)
    out = [()]
    for k in range(1, 3):
        for combo in combinations(pairs, k):
            used = [x for pr in combo for x in pr]
            if len(set(used)) == len(used):
                out.append(combo)
    return out


def deletion_sets(let: dict, link: int):
    """Every set of disjoint (U, U~) pairs of the letters on one shared link."""
    ups = [n for n, (lk, o) in let.items() if lk == link and o == 1]
    downs = [n for n, (lk, o) in let.items() if lk == link and o == -1]
    out = [()]
    for k in range(1, min(len(ups), len(downs)) + 1):
        for us in combinations(ups, k):
            for ds in permutations(downs, k):
                out.append(tuple(zip(us, ds, strict=True)))
    return out


# ---------------------------------------------------------------- part A: phi on the histories
P = ((0, 1), (0, 0, 0))
Q_COP = ((0, 1), (1, 0, 0))
STRAIGHT = [P, Q_COP, ((0, 1), (2, 0, 0))]
LCHAIN = [P, Q_COP, ((0, 1), (1, 1, 0))]
X_INDEX = 1


def roles_of(cl3):
    end_ids = [k for k in range(6) if k // 2 != X_INDEX]

    def role(j):
        face, conj = j // 2, j % 2
        if face == X_INDEX:
            return "X~" if conj else "X"
        if face == end_ids[0] // 2:
            return "P~" if conj else "P"
        return "Q~" if conj else "Q"

    return end_ids, {role(j): j for j in range(6)}


def history_integrands(faces3):
    """{(sequence, l1, l2, l3, a, b): {word: coefficient}} of the C-odd direct term."""
    cl3 = L.Cluster(faces3, reduced=True)
    end_ids, idx = roles_of(cl3)
    inv = {j: r for r, j in idx.items()}
    xs = {2 * X_INDEX, 2 * X_INDEX + 1}
    e0 = cl3.e0

    def resolvent_labelled(vec):
        res: dict = defaultdict(dict)
        for e, per_link, comp in SR.labelled_components(vec):
            if e != e0:
                lab = SR.state_label(per_link)
                res[lab] = L.vadd(res[lab], comp, 1 / (e0 - e))
        return res

    kets, bras = {}, {}
    for a in (0, 1):
        stage: dict = {}
        for s1, w1 in enumerate(cl3.words):
            for l1, c1 in resolvent_labelled(
                L.multiply({cl3.words[end_ids[a]]: SR.RF(1)}, w1)
            ).items():
                for s2, w2 in enumerate(cl3.words):
                    v2 = L.multiply(c1, w2)
                    if v2:
                        for l2, c2 in resolvent_labelled(v2).items():
                            stage[(s1, s2, l1, l2)] = L.vadd(stage.get((s1, s2, l1, l2), {}), c2)
        kets[a] = stage
    for b in (2, 3):
        stage = {}
        for s4, w4 in enumerate(cl3.words):
            for l3, c3 in resolvent_labelled(
                L.multiply({cl3.words[end_ids[b]]: SR.RF(1)}, w4)
            ).items():
                for s3, w3 in enumerate(cl3.words):
                    v2 = L.multiply(c3, w3)
                    if v2:
                        stage[(s3, s4, l3)] = L.vadd(stage.get((s3, s4, l3), {}), v2)
        bras[b] = stage
    # the C-odd integrands of every history whose C-odd value is nonzero: the four (a, b)
    # entries summed with their signs, integrands with a zero Haar integral dropped (they
    # are the histories with the middle face on one side only, whose private links are
    # unbalanced)
    out: dict = {}
    for (s1, s2, l1, l2) in {k for a in (0, 1) for k in kets[a]}:
        for (s3, s4, l3) in {k for b in (2, 3) for k in bras[b]}:
            if not any(s in xs for s in (s1, s2, s3, s4)):
                continue
            words: dict = defaultdict(SR.RF)
            total = SR.RF(0)
            for a in (0, 1):
                for b in (2, 3):
                    kv = kets[a].get((s1, s2, l1, l2))
                    bv = bras[b].get((s3, s4, l3))
                    if not kv or not bv:
                        continue
                    sign = (1 if a == 0 else -1) * (1 if b == 2 else -1)
                    for w, c in bv.items():
                        bc = L.conj(w)
                        for w2, c2 in kv.items():
                            prod = L.product(bc, w2)
                            val = L.integrate(prod)
                            if val:
                                words[prod] += sign * c * c2 / 2
                                total += sign * c * c2 / 2 * val
            words = {w: c for w, c in words.items() if c}
            if words and total:
                out[((inv[s1], inv[s2], inv[s3], inv[s4]), l1, l2, l3)] = words
    return out


def phi_engine_word(word, cl_s, cl_l):
    """phi on an engine word of the straight cluster: delete A and Ab, rename B to C, and map
    every other link to the L cluster's link with the same role."""
    words_s, words_l = cl_s.words[::2], cl_l.words[::2]
    xs, xl = words_s[X_INDEX][0], words_l[X_INDEX][0]
    ends_s = [w for k, w in enumerate(words_s) if k != X_INDEX]
    ends_l = [w for k, w in enumerate(words_l) if k != X_INDEX]
    shared_s = {lk for lk, _o in xs} & ({lk for lk, _o in ends_s[0][0]} | {lk for lk, _o in ends_s[1][0]})
    shared_l = {lk for lk, _o in xl} & ({lk for lk, _o in ends_l[0][0]} | {lk for lk, _o in ends_l[1][0]})
    priv_s = [lk for lk, _o in xs if lk not in shared_s]  # two weight-one links, in X's order
    priv_l = [lk for lk, _o in xl if lk not in shared_l]  # one weight-two link
    assert len(priv_s) == 2 and len(priv_l) == 1, (priv_s, priv_l)
    # X_S = l1 A l2 B (cyclic): A, the private letter that follows the l1-shared letter, is
    # the one the L chain keeps as its weight-two link; B, after the l2 letter, is deleted
    order = [lk for lk, _o in xs]
    i1 = next(i for i, lk in enumerate(order) if lk in shared_s and lk in {l for l, _ in ends_s[0][0]})
    a_link = order[(i1 + 1) % 4] if order[(i1 + 1) % 4] in priv_s else order[(i1 - 1) % 4]
    b_link = next(lk for lk in priv_s if lk != a_link)
    link_map = {a_link: priv_l[0]}
    l2_s = next(lk for lk in shared_s if lk in {l for l, _ in ends_s[1][0]})
    l2_l = next(lk for lk in shared_l if lk in {l for l, _ in ends_l[1][0]})
    o_s = next(o for lk, o in xs if lk == l2_s)
    o_l = next(o for lk, o in xl if lk == l2_l)
    flip = {l2_l} if o_s != o_l else set()
    # shared links and end paths: match by role (which end face they belong to)
    for k in range(2):
        s_links = {lk for lk, _o in ends_s[k][0]}
        l_links = {lk for lk, _o in ends_l[k][0]}
        s_shared = next(lk for lk in s_links if lk in shared_s)
        l_shared = next(lk for lk in l_links if lk in shared_l)
        link_map[s_shared] = l_shared
        link_map[next(lk for lk in s_links if lk != s_shared)] = next(lk for lk in l_links if lk != l_shared)
    traces = []
    for tr in word:
        t = [(link_map[lk], -o if link_map[lk] in flip else o) for lk, o in tr if lk != b_link]
        if t:
            traces.append(tuple(t))
    return L.canon(traces)


out: dict = {"schema": "universality_lemma/v1", "parts": {}}
with SR.Symbolic():
  if "A" in PARTS:
    hs = history_integrands(STRAIGHT)
    hl = history_integrands(LCHAIN)
    cl_s, cl_l = L.Cluster(STRAIGHT, reduced=True), L.Cluster(LCHAIN, reduced=True)
    keys_equal = set(hs) == set(hl)
    bijection = coeff_equal = total_words = 0
    orient_note = None
    for key, words in hs.items():
        target = hl.get(key, {})
        image = {phi_engine_word(w, cl_s, cl_l): c for w, c in words.items()}
        total_words += len(words)
        if set(image) == set(target):
            bijection += 1
            coeff_equal += all(image[w] == target[w] for w in image)
        elif orient_note is None:
            orient_note = {"key": str(key), "image_not_in_L": len(set(image) - set(target)), "L_not_in_image": len(set(target) - set(image))}
    out["parts"]["A_phi_on_histories"] = {
        "terms": len(hs),
        "keys_equal": keys_equal,
        "integrands_straight": total_words,
        "terms_where_phi_is_a_bijection_onto_L": bijection,
        "terms_with_equal_coefficients": coeff_equal,
        "first_failure": orient_note,
    }
    print(f"[{time.time() - T0:.1f}s] A: {json.dumps(out['parts']['A_phi_on_histories'])}", flush=True)
L.set_rank(3)

# ---------------------------------------------------------------- parts B, C
family: dict = {}
for a, b in (((1, 1), (2, 1), (1, 2), (2, 2)) if "B" in PARTS else ()):
    t = time.time()
    n = agree = 0
    exhaustive = (a, b) != (2, 2)
    rng = random.Random(1)
    for succ, let in swap_family(a, b):
        if not exhaustive and rng.random() > 0.01:
            continue
        n += 1
        agree += phi_invariant(succ, let, RANKS if exhaustive else (7,))
    family[f"swaps a={a} b={b}"] = {"words": n, "phi_invariant": agree, "exhaustive": exhaustive, "seconds": round(time.time() - t, 1)}
    print(f"[{time.time() - T0:.1f}s] B a={a} b={b}: {n} words, phi-invariant {agree}{'' if exhaustive else ' (1% sample)'}", flush=True)

for a, b in ((1, 1), (2, 1), (1, 2)):
    t = time.time()
    let = letters(a, b)
    n = agree = 0
    c1s, c2s = cut_sets(let, L1), cut_sets(let, L2)
    exhaustive = (a, b) == (1, 1)
    rng = random.Random(3)
    for succ, _let in swap_family(a, b, reachable=True):
        if not exhaustive and rng.random() > 0.1:
            continue
        for c1 in c1s:
            for c2 in c2s:
                if not c1 and not c2:
                    continue
                s2, loops = dict(succ), 0
                for u, d in c1 + c2:
                    s2, extra = cut(s2, u, d)
                    loops += extra
                let2 = {k: v for k, v in let.items() if k in s2}
                n += 1
                agree += phi_invariant(s2, let2, RANKS if exhaustive else (7,), loops)
    family[f"reachable swaps then cuts a={a} b={b}"] = {
        "words": n,
        "phi_invariant": agree,
        "exhaustive": exhaustive,
        "seconds": round(time.time() - t, 1),
    }
    print(
        f"[{time.time() - T0:.1f}s] C a={a} b={b}: {n} reachable cut words, phi-invariant {agree}"
        f"{'' if exhaustive else ' (10% sample of swaps)'}",
        flush=True,
    )

# the smallest case over Q(N) as well
t = time.time()
with SR.Symbolic():
    n = agree = 0
    for succ, let in (swap_family(1, 1) if "B" in PARTS else ()):
        n += 1
        s2, let2, _loops = phi(succ, let)
        agree += L.integrate(word_of(succ, let)) == L.integrate(word_of(s2, let2))
family["swaps a=b=1 over Q(N)"] = {"words": n, "phi_invariant": agree, "exhaustive": True, "seconds": round(time.time() - t, 1)}
print(f"[{time.time() - T0:.1f}s] B a=b=1 over Q(N): {n} words, phi-invariant {agree}", flush=True)
L.set_rank(3)
out["parts"]["B_C_family"] = family

# ---------------------------------------------------------------- part D: the control
t = time.time()
rng = random.Random(20260904)
control: dict = {}
for a, b in ((1, 1), (2, 2)):
    let = letters(a, b)
    names = list(let)
    free_out = [x for x in names if x not in FIXED_PRIVATE]
    free_in = [x for x in names if x not in set(FIXED_PRIVATE.values())]
    agree = n = 0
    for _ in range(300 if "D" in PARTS else 0):
        rng.shuffle(free_in)
        succ = dict(FIXED_PRIVATE)
        succ.update(zip(free_out, free_in, strict=True))
        n += 1
        agree += phi_invariant(succ, let, (7,))
    control[f"random wirings a={a} b={b}"] = {"words": n, "phi_invariant": agree}
    print(f"[{time.time() - T0:.1f}s] D a={a} b={b}: {n} arbitrary wirings, phi-invariant {agree}", flush=True)
out["parts"]["D_control"] = control
out["seconds"] = round(time.time() - T0, 1)
(HERE / ("certificate" + __import__("os").environ.get("OUT_SUFFIX", "") + ".json")).write_text(json.dumps(out, indent=1) + "\n", encoding="utf-8", newline="\n")
print("wrote certificate.json in", out["seconds"], "s")
