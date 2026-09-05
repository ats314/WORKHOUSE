"""The single-contact dressing obeys the same universality lemma as the two-hop weight.

    python lemma.py > console.log

Setting (ADR 0030, 0032). On the reduced clusters the coplanar (straight) and the
perpendicular (L) single-contact dressing each have one face carrying both shared links, the
hub: straight Q = Tr(U_e~ A U_x B) with two private links of weight one, L P = Tr(U_e U_x C)
with one of weight two. The other end face is the hub's neighbour across the link e, the
dressing X its neighbour across the link x. ADR 0030 found the two dressings agree history by
history once the correspondence reverses time, swaps the end roles and conjugates one end
face. The correspondence reverses time, so the straight cluster's histories are staged from
the other end here: one resolvent expansion written on the ket side and two on the bra side,
against the L cluster's two and one. With that staging every (sequence, channel) term's
integrands pair off one to one.

phi on straight words: delete A and A~, joining each one's predecessor to its successor;
rename B, B~ to C, C~; reverse the letters on the link e (a relabelling the Haar integral does
not see); conjugate the whole word (time reversal; the integrals are real). Part A checks
that phi maps the straight integrands of every term bijectively onto the L integrands with
the same Fierz coefficient, and that the Haar integral of every integrand equals that of its
image, over Q(N).

The abstract family is the one of runs/universality_lemma_2026-09-04 with the roles of the
two shared links exchanged: hub letters x_e -> A -> x_x -> B -> x_e, neighbours
E^a E~^a on the link e and X^c X~^c on the link x, every permutation of out-targets within a
shared link, then the Fierz cuts of unlike pairs a history can bring into one projected
state. Parts B and C check integrate(w) == integrate(phi(w)) on that family for a, c <= 2,
the multiplicities fourth order reaches; part D is the control on arbitrary wirings. The
mirror image (reverse every cycle, exchange the two links) carries this family onto the
two-hop family and phi onto that lemma's phi, so parts B to D are the two-hop lemma's mirror,
run here directly.

Writes certificate.json.
"""

from __future__ import annotations

import json
import os
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
PARTS = os.environ.get("PARTS", "ABCD")

# ---------------------------------------------------------------- the abstract family
LE, LX, WE, WX, LA, LB = 1, 2, 3, 4, 5, 6
# hub H = Tr(U_e~ A U_x B): xe -> A -> xx -> B -> xe; H~ = B~ -> xxb -> A~ -> xeb -> B~.
FIXED_PRIVATE = {"A": "xx", "B": "xe", "Bb": "xxb", "Ab": "xeb"}


def letters(a: int, c: int) -> dict:
    let = {}
    for i in range(a):
        let[f"e{i}"], let[f"wE{i}"] = (LE, 1), (WE, 1)
        let[f"eb{i}"], let[f"wEb{i}"] = (LE, -1), (WE, -1)
    for j in range(c):
        let[f"x{j}"], let[f"wX{j}"] = (LX, -1), (WX, 1)
        let[f"xb{j}"], let[f"wXb{j}"] = (LX, 1), (WX, -1)
    let.update({"xe": (LE, -1), "xx": (LX, 1), "A": (LA, 1), "B": (LB, 1)})
    let.update({"xeb": (LE, 1), "xxb": (LX, -1), "Ab": (LA, -1), "Bb": (LB, -1)})
    return let


def base_succ(a: int, c: int) -> dict:
    succ = {"xe": "A", "xx": "B", "Bb": "xxb", "xxb": "Ab", "Ab": "xeb", "xeb": "Bb"}
    succ.update(FIXED_PRIVATE)
    for i in range(a):
        succ[f"e{i}"], succ[f"wE{i}"] = f"wE{i}", f"e{i}"
        succ[f"eb{i}"], succ[f"wEb{i}"] = f"wEb{i}", f"eb{i}"
    for j in range(c):
        succ[f"x{j}"], succ[f"wX{j}"] = f"wX{j}", f"x{j}"
        succ[f"xb{j}"], succ[f"wXb{j}"] = f"wXb{j}", f"xb{j}"
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
    """The Fierz cut of an unlike pair on one link, as the engine performs it. Returns
    (succ, loops)."""
    s2 = dict(succ)
    ps = next(k for k, v in s2.items() if v == s)
    pt = next(k for k, v in s2.items() if v == t)
    ss, st = s2[s], s2[t]
    if ps == t and pt == s:
        del s2[s], s2[t]
        return s2, 1
    if ps == t:
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
    """Delete A and A~, joining predecessor to successor; B and B~ become the weight-two
    link C (a renaming). Returns (succ, letters, loops)."""
    s2, loops = delete(succ, ("A", "Ab"))
    let2 = {k: v for k, v in let.items() if k not in ("A", "Ab")}
    return s2, let2, loops


def both(succ, let, rank, loops=0):
    L.set_rank(rank)
    s2, let2, phi_loops = phi(succ, let)
    n = L.F(rank)
    return (
        L.integrate(word_of(succ, let)) * n**loops,
        L.integrate(word_of(s2, let2)) * n ** (loops + phi_loops),
    )


def phi_invariant(succ, let, ranks=RANKS, loops=0) -> bool:
    return all(v1 == v2 for v1, v2 in (both(succ, let, r, loops) for r in ranks))


def swap_family(a: int, c: int, reachable: bool = False):
    let = letters(a, c)
    base = base_succ(a, c)
    groups = []
    for link in (LE, LX):
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
    """Unlike pairs a Fierz cut can act on: never the hub's own letter with the hub
    conjugate's, which sit on opposite sides of the amplitude."""
    ups = [n for n, (lk, o) in let.items() if lk == link and o == 1]
    downs = [n for n, (lk, o) in let.items() if lk == link and o == -1]
    hub = {"xe", "xeb", "xx", "xxb"}
    return [(u, d) for u in ups for d in downs if not (u in hub and d in hub)]


def cut_sets(let: dict, link: int):
    pairs = cut_pairs(let, link)
    out = [()]
    for k in range(1, 3):
        for combo in combinations(pairs, k):
            used = [x for pr in combo for x in pr]
            if len(set(used)) == len(used):
                out.append(combo)
    return out


# ---------------------------------------------------------------- part A: phi on the histories
P = ((0, 1), (0, 0, 0))
Q_COP = ((0, 1), (1, 0, 0))
Q_PERP = ((0, 2), (0, 0, 0))
STRAIGHT = [P, ((0, 1), (2, 0, 0)), Q_COP]  # hub Q: the end face carrying both shared links
LSHAPE = [P, ((0, 1), (1, 0, 0)), Q_PERP]  # hub P
X_INDEX = 1
HUB = {"straight": 2, "L": 0}
SWAP = {"P": "Q", "P~": "Q~", "Q": "P", "Q~": "P~", "X": "X", "X~": "X~"}
CONJ_P = {"P": "P~", "P~": "P", "Q": "Q", "Q~": "Q~", "X": "X", "X~": "X~"}


def correspond(key):
    """ADR 0030's correspondence: reverse time, swap the end roles, conjugate P."""
    seq, l1, l2, l3 = key
    return (tuple(CONJ_P[SWAP[r]] for r in reversed(seq)), l3, l2, l1)


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


def history_integrands(faces3, reverse: bool):
    """{(sequence, l1, l2, l3): {word: coefficient}} of the C-odd direct term; ``reverse``
    writes two resolvent expansions on the bra side and one on the ket side."""
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

    def two_stage(end_word):
        stage: dict = {}
        for s1, w1 in enumerate(cl3.words):
            for l1, c1 in resolvent_labelled(L.multiply({end_word: SR.RF(1)}, w1)).items():
                for s2, w2 in enumerate(cl3.words):
                    v2 = L.multiply(c1, w2)
                    if v2:
                        for l2, c2 in resolvent_labelled(v2).items():
                            stage[(s1, s2, l1, l2)] = L.vadd(stage.get((s1, s2, l1, l2), {}), c2)
        return stage

    def one_stage(end_word):
        stage: dict = {}
        for s1, w1 in enumerate(cl3.words):
            for l1, c1 in resolvent_labelled(L.multiply({end_word: SR.RF(1)}, w1)).items():
                for s2, w2 in enumerate(cl3.words):
                    v2 = L.multiply(c1, w2)
                    if v2:
                        stage[(s1, s2, l1)] = L.vadd(stage.get((s1, s2, l1), {}), v2)
        return stage

    kets = {a: (one_stage if reverse else two_stage)(cl3.words[end_ids[a]]) for a in (0, 1)}
    bras = {b: (two_stage if reverse else one_stage)(cl3.words[end_ids[b]]) for b in (2, 3)}
    out: dict = {}
    for kk in {k for a in (0, 1) for k in kets[a]}:
        for bk in {k for b in (2, 3) for k in bras[b]}:
            if reverse:
                (s1, s2, l1), (s4, s3, l3, l2) = kk, bk
            else:
                (s1, s2, l1, l2), (s4, s3, l3) = kk, bk
            if not any(s in xs for s in (s1, s2, s3, s4)):
                continue
            words: dict = defaultdict(SR.RF)
            total = SR.RF(0)
            for a in (0, 1):
                for b in (2, 3):
                    kv, bv = kets[a].get(kk), bras[b].get(bk)
                    if not kv or not bv:
                        continue
                    sign = (1 if a == 0 else -1) * (1 if b == 2 else -1)
                    for w, coef in bv.items():
                        bc = L.conj(w)
                        for w2, c2 in kv.items():
                            prod = L.product(bc, w2)
                            val = L.integrate(prod)
                            if val:
                                words[prod] += sign * coef * c2 / 2
                                total += sign * coef * c2 / 2 * val
            words = {w: coef for w, coef in words.items() if coef}
            if words and total:
                out[((inv[s1], inv[s2], inv[s3], inv[s4]), l1, l2, l3)] = words
    return out


def roles_from_words(cl3, hub_face: int):
    """(hub-end link, hub-X link, end path, X path, hub privates in the hub's cyclic order
    after the hub-end letter, orientation of the hub's hub-end letter, of its hub-X letter,
    of the end face's shared letter)."""
    faces = [tuple(w[0]) for w in cl3.words[::2]]
    links = [{lk for lk, _o in f} for f in faces]
    other_end = next(i for i in range(3) if i not in (hub_face, X_INDEX))
    s_end = (links[hub_face] & links[other_end]).pop()
    s_x = (links[hub_face] & links[X_INDEX]).pop()

    def priv(i):
        return [lk for lk in links[i] if all(lk not in links[j] for j in range(3) if j != i)]

    hub = faces[hub_face]
    i_end = next(i for i, (lk, _o) in enumerate(hub) if lk == s_end)
    order = [hub[(i_end + k) % len(hub)][0] for k in range(len(hub))]
    hub_priv = [lk for lk in order if lk in priv(hub_face)]
    o_end = next(o for lk, o in hub if lk == s_end)
    o_x = next(o for lk, o in hub if lk == s_x)
    o_face = next(o for lk, o in faces[other_end] if lk == s_end)
    return s_end, s_x, priv(other_end)[0], priv(X_INDEX)[0], hub_priv, o_end, o_x, o_face


def make_phi_engine(cl_s, cl_l):
    """phi on engine words of the straight cluster, built from the roles: delete A (the hub
    private after the hub-end letter), rename B to C, map every link to the L link with the
    same role, reverse the links whose orientation differs between the geometries, conjugate."""
    s_end, s_x, w_end, w_x, priv_s, o_end_s, o_x_s, o_face_s = roles_from_words(cl_s, HUB["straight"])
    l_end, l_x, lw_end, lw_x, priv_l, o_end_l, o_x_l, o_face_l = roles_from_words(cl_l, HUB["L"])
    assert len(priv_s) == 2 and len(priv_l) == 1, (priv_s, priv_l)
    a_link, b_link = priv_s
    rename = {s_end: l_end, s_x: l_x, w_end: lw_end, w_x: lw_x, b_link: priv_l[0]}
    # the hub's letters fix the orientation of the shared links; the end face's shared letter
    # (relative to the hub's) fixes whether its private path is reversed as well
    # the conjugation flips every letter alike, so a shared link is reversed exactly when the
    # two hubs traverse it in different directions
    flips = set()
    if o_end_s != o_end_l:
        flips.add(s_end)
    if o_x_s != o_x_l:
        flips.add(s_x)
    if (o_face_s * o_end_s) != (o_face_l * o_end_l):
        flips.add(w_end)

    def phi_engine(word):
        traces = []
        for tr in word:
            t = [(rename[lk], -o if lk in flips else o) for lk, o in tr if lk != a_link]
            if t:
                traces.append(tuple((lk, -o) for lk, o in reversed(t)))
        return L.canon(traces)

    desc = {
        "delete": "A, the hub private after the hub-end letter",
        "rename_B_to_C": True,
        "reversed_links": sorted(
            {"hub-end link" if lk == s_end else "hub-X link" if lk == s_x else "end path" for lk in flips}
        ),
        "conjugate": True,
        "straight_faces": [[list(x) for x in f] for f in (tuple(w[0]) for w in cl_s.words[::2])],
        "L_faces": [[list(x) for x in f] for f in (tuple(w[0]) for w in cl_l.words[::2])],
    }
    return phi_engine, desc


out: dict = {"schema": "dressing_lemma/v1", "parts": {}}
with SR.Symbolic():
    if "A" in PARTS:
        cl_s, cl_l = L.Cluster(STRAIGHT, reduced=True), L.Cluster(LSHAPE, reduced=True)
        phi_engine, desc = make_phi_engine(cl_s, cl_l)
        hs = history_integrands(STRAIGHT, reverse=True)
        hl = history_integrands(LSHAPE, reverse=False)
        keys_equal = {correspond(k) for k in hl} == set(hs)
        bijection = coeff_equal = total_words = values_equal = 0
        first_failure = None
        for key, target in hl.items():
            words = hs.get(correspond(key), {})
            image = {phi_engine(w): coef for w, coef in words.items()}
            total_words += len(words)
            # the correspondence carries the incidence sign: L coefficient = - straight coefficient
            if set(image) == set(target):
                bijection += 1
                coeff_equal += all(image[w] == -target[w] for w in image)
            elif first_failure is None:
                first_failure = {
                    "key": str(key),
                    "image_not_in_L": len(set(image) - set(target)),
                    "L_not_in_image": len(set(target) - set(image)),
                }
            values_equal += sum(1 for w in words if L.integrate(w) == L.integrate(phi_engine(w)))
        # the naive staging, for the record: with two resolvents on the ket side of both clusters
        hs_naive = history_integrands(STRAIGHT, reverse=False)
        naive_equal = 0
        for key, target in hl.items():
            words = hs_naive.get(correspond(key), {})
            sig_l = Counter((str((-coef).to_sympy()), str(L.integrate(w).to_sympy())) for w, coef in target.items())
            sig_s = Counter((str(coef.to_sympy()), str(L.integrate(w).to_sympy())) for w, coef in words.items())
            naive_equal += sig_l == sig_s
        out["parts"]["A_phi_on_histories"] = {
            "phi": desc,
            "terms": len(hl),
            "keys_equal_under_the_correspondence": keys_equal,
            "integrands_straight": total_words,
            "terms_where_phi_is_a_bijection_onto_L": bijection,
            "terms_with_equal_coefficients_up_to_the_incidence_sign": coeff_equal,
            "integrands_with_equal_Haar_integral_over_QN": values_equal,
            "first_failure": first_failure,
            "naive_staging_terms_with_equal_coefficient_value_multisets": naive_equal,
        }
        print(f"[{time.time() - T0:.1f}s] A: {json.dumps(out['parts']['A_phi_on_histories'])}", flush=True)
L.set_rank(3)

# ---------------------------------------------------------------- parts B, C
family: dict = {}
for a, c in (((1, 1), (2, 1), (1, 2), (2, 2)) if "B" in PARTS else ()):
    t = time.time()
    n = agree = 0
    exhaustive = (a, c) != (2, 2)
    rng = random.Random(1)
    for succ, let in swap_family(a, c):
        if not exhaustive and rng.random() > 0.01:
            continue
        n += 1
        agree += phi_invariant(succ, let, RANKS if exhaustive else (7,))
    family[f"swaps a={a} c={c}"] = {"words": n, "phi_invariant": agree, "exhaustive": exhaustive, "seconds": round(time.time() - t, 1)}
    print(f"[{time.time() - T0:.1f}s] B a={a} c={c}: {n} words, phi-invariant {agree}{'' if exhaustive else ' (1% sample)'}", flush=True)

for a, c in (((1, 1), (2, 1), (1, 2)) if "C" in PARTS else ()):
    t = time.time()
    let = letters(a, c)
    n = agree = 0
    c1s, c2s = cut_sets(let, LE), cut_sets(let, LX)
    exhaustive = (a, c) == (1, 1)
    rng = random.Random(3)
    for succ, _let in swap_family(a, c, reachable=True):
        if not exhaustive and rng.random() > 0.1:
            continue
        for k1 in c1s:
            for k2 in c2s:
                if not k1 and not k2:
                    continue
                s2, loops = dict(succ), 0
                for u, d in k1 + k2:
                    s2, extra = cut(s2, u, d)
                    loops += extra
                let2 = {k: v for k, v in let.items() if k in s2}
                n += 1
                agree += phi_invariant(s2, let2, RANKS if exhaustive else (7,), loops)
    family[f"reachable swaps then cuts a={a} c={c}"] = {
        "words": n,
        "phi_invariant": agree,
        "exhaustive": exhaustive,
        "seconds": round(time.time() - t, 1),
    }
    print(
        f"[{time.time() - T0:.1f}s] C a={a} c={c}: {n} reachable cut words, phi-invariant {agree}"
        f"{'' if exhaustive else ' (10% sample of swaps)'}",
        flush=True,
    )

t = time.time()
with SR.Symbolic():
    n = agree = 0
    for succ, let in (swap_family(1, 1) if "B" in PARTS else ()):
        n += 1
        s2, let2, _loops = phi(succ, let)
        agree += L.integrate(word_of(succ, let)) == L.integrate(word_of(s2, let2))
family["swaps a=c=1 over Q(N)"] = {"words": n, "phi_invariant": agree, "exhaustive": True, "seconds": round(time.time() - t, 1)}
print(f"[{time.time() - T0:.1f}s] B a=c=1 over Q(N): {n} words, phi-invariant {agree}", flush=True)
L.set_rank(3)
out["parts"]["B_C_family"] = family

# ---------------------------------------------------------------- part D: the control
t = time.time()
rng = random.Random(20260904)
control: dict = {}
for a, c in ((1, 1), (2, 2)):
    let = letters(a, c)
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
    control[f"random wirings a={a} c={c}"] = {"words": n, "phi_invariant": agree}
    print(f"[{time.time() - T0:.1f}s] D a={a} c={c}: {n} arbitrary wirings, phi-invariant {agree}", flush=True)
out["parts"]["D_control"] = control
out["seconds"] = round(time.time() - T0, 1)
(HERE / ("certificate" + os.environ.get("OUT_SUFFIX", "") + ".json")).write_text(
    json.dumps(out, indent=1) + "\n", encoding="utf-8", newline="\n"
)
print("wrote certificate.json in", out["seconds"], "s")
