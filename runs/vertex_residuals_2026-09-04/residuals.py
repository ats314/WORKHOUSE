"""Where the universality identity lives: the shared-link words after every private path is integrated.

    python residuals.py > console.log

ADR 0030 found the two-hop weight universal history by history and integrand by
integrand between the straight and the L chain, on the reduced clusters. This
run asks at which point of the contraction the two geometries become literally
the same word. For every (insertion sequence, channel) term of the C-odd direct
term, every final integrand is taken with its coefficient, some of its links
are Haar-integrated with ``loopcalc.haar_link`` (every such link is a balanced
n = 1 family, so the integration is the cut delta delta / N), adjacent U U~
pairs of one link inside a trace are cancelled (unitarity; an emptied trace is
a factor N), and the residual words -- over the role alphabet l1, l2, wP, wQ --
are summed with their coefficients and compared between the geometries.

Two stages:

* ``xpriv``: integrate the middle face's private links only (two links of
  weight one in the straight chain, one of weight two in the L chain). The
  residual vectors, functions of the shared links and the two end paths, do
  NOT coincide: the L chain carries words in which the end paths are threaded
  through one trace with both shared links, the straight chain does not.
* ``xpriv,wP,wQ``: integrate the end paths as well. The residual vectors,
  formal words in the two shared links alone, coincide in every term,
  coefficient for coefficient, with no orientation flip.

The third stage takes no integral at all: for every term it compares, between
the geometries, the multiset of (Fierz coefficient, full Haar integral) pairs
over the final integrands, and the Haar family sizes the integrands present on
their links. They agree term by term: the integrands of the two geometries are
in bijection with the same coefficient AND the same Haar integral, although
the words differ. So the identity behind channel-wise universality is one of
Haar integrals of words that differ only in the middle face's private
structure, with everything else wired identically. Writes certificate.json.
"""

from __future__ import annotations

import json
import sys
import time
from collections import defaultdict
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
sys.path.insert(0, str(ROOT / "src"))

from workhouse import loopcalc as L  # noqa: E402
from workhouse import symbolic_rank as SR  # noqa: E402

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


def link_roles(cl3):
    """Every link of the reduced cluster by role: l1, l2 (shared), wP, wQ (end paths), xpriv."""
    words = cl3.words[::2]
    x_word = words[X_INDEX]
    ends = [w for k, w in enumerate(words) if k != X_INDEX]
    links_x = {lk for lk, _o in x_word[0]}
    links_p = {lk for lk, _o in ends[0][0]}
    links_q = {lk for lk, _o in ends[1][0]}
    roles = {}
    for lk in links_x & links_p:
        roles[lk] = "l1"
    for lk in links_x & links_q:
        roles[lk] = "l2"
    for lk in links_p - links_x:
        roles[lk] = "wP"
    for lk in links_q - links_x:
        roles[lk] = "wQ"
    for lk in links_x - links_p - links_q:
        roles[lk] = "xpriv"
    return roles


def simplify(word):
    """Cancel adjacent U U~ pairs of one link inside each trace, cyclically; an emptied trace
    is a closed loop, worth N."""
    loops = 0
    traces = []
    for tr in word:
        letters = list(tr)
        changed = True
        while changed and letters:
            changed = False
            n = len(letters)
            for i in range(n):
                j = (i + 1) % n
                if n >= 2 and letters[i][0] == letters[j][0] and letters[i][1] == -letters[j][1]:
                    for k in sorted((i, j), reverse=True):
                        del letters[k]
                    changed = True
                    break
        if letters:
            traces.append(tuple(letters))
        else:
            loops += 1
    return loops, L.canon(traces)


def relabel(word, roles):
    """The word over the role alphabet, canonical under rotation of traces and their order."""
    out = []
    for tr in word:
        t = tuple((roles[lk], o) for lk, o in tr)
        out.append(min(t[i:] + t[:i] for i in range(len(t))))
    return tuple(sorted(out))


def direct_terms(faces3):
    """{(sequence roles, l1, l2, l3): value} of the C-odd direct term, reduced cluster."""
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
                        res[((inv[s1], inv[s2], inv[s3], inv[s4]), l1, l2, l3)] += sign * tot / 2
    return {k: v for k, v in res.items() if v}


def residual(faces3, seq_roles, labels, integrate: set):
    """The C-odd term's integrands with the links of the given roles Haar-integrated and
    unitarity applied: {residual word over roles: coefficient}, and the term's value."""
    cl3 = L.Cluster(faces3, reduced=True)
    end_ids, idx = roles_of(cl3)
    roles = link_roles(cl3)
    to_integrate = [lk for lk, r in roles.items() if r in integrate]
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

    out: dict = defaultdict(SR.RF)
    total = SR.RF(0)
    for a in (0, 1):
        for b in (2, 3):
            sign = (1 if a == 0 else -1) * (1 if b == 2 else -1)
            ket = step(step({cl3.words[end_ids[a]]: SR.RF(1)}, s1, l1), s2, l2)
            bra = L.multiply(step({cl3.words[end_ids[b]]: SR.RF(1)}, s4, l3), cl3.words[s3])
            for w, c in bra.items():
                bc = L.conj(w)
                for w2, c2 in ket.items():
                    vec = {L.product(bc, w2): sign * c * c2 / 2}
                    for lk in to_integrate:
                        nxt: dict = defaultdict(SR.RF)
                        for ww, cc in vec.items():
                            if any(lk == l for t in ww for l, _o in t):
                                for w3, c3 in L.haar_link(ww, lk).items():
                                    nxt[w3] += cc * c3
                            else:
                                nxt[ww] += cc
                        vec = nxt
                    for ww, cc in vec.items():
                        if cc:
                            loops, red = simplify(ww)
                            out[relabel(red, roles)] += cc * SR.N_SYM**loops
                            total += cc * L.integrate(ww)
    return {k: v for k, v in out.items() if v}, total


def integrand_pairs(faces3, seq_roles, labels):
    """(Fierz coefficient, full Haar integral, sorted family sizes) per final integrand."""
    cl3 = L.Cluster(faces3, reduced=True)
    end_ids, idx = roles_of(cl3)
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

    data = []
    for a in (0, 1):
        for b in (2, 3):
            sign = (1 if a == 0 else -1) * (1 if b == 2 else -1)
            ket = step(step({cl3.words[end_ids[a]]: SR.RF(1)}, s1, l1), s2, l2)
            bra = L.multiply(step({cl3.words[end_ids[b]]: SR.RF(1)}, s4, l3), cl3.words[s3])
            for w, c in bra.items():
                bc = L.conj(w)
                for w2, c2 in ket.items():
                    prod = L.product(bc, w2)
                    families = tuple(sorted(v[0] for v in L.content(prod).values()))
                    data.append((sign * c * c2 / 2, L.integrate(prod), families))
    return data


T0 = time.time()
out = {"schema": "vertex_residuals/v1", "field": "Q(N)", "stages": {}}
with SR.Symbolic():
    terms = sorted(direct_terms(STRAIGHT), key=str)
    print(f"[{time.time() - T0:.1f}s] {len(terms)} (sequence, channel) terms of the straight chain", flush=True)
    for name, integrate in (("xpriv", {"xpriv"}), ("xpriv,wP,wQ", {"xpriv", "wP", "wQ"})):
        t = time.time()
        equal_words = 0
        equal_totals = 0
        words_straight = set()
        words_l = set()
        example = None
        for key in terms:
            seq, lab = key[0], key[1:]
            rs, ts = residual(STRAIGHT, seq, lab, integrate)
            rl, tl = residual(LCHAIN, seq, lab, integrate)
            equal_totals += ts == tl
            equal_words += rs == rl
            words_straight |= set(rs)
            words_l |= set(rl)
            if rs != rl and example is None:
                example = {
                    "term": str(key),
                    "straight": {str(k): str(v.to_sympy()) for k, v in rs.items()},
                    "L": {str(k): str(v.to_sympy()) for k, v in rl.items()},
                }
        out["stages"][name] = {
            "integrated": sorted(integrate),
            "terms": len(terms),
            "residual_vectors_equal": equal_words,
            "totals_equal": equal_totals,
            "distinct_residual_words_straight": len(words_straight),
            "distinct_residual_words_L": len(words_l),
            "residual_words_straight": sorted(str(w) for w in words_straight),
            "residual_words_L": sorted(str(w) for w in words_l),
            "first_mismatch": example,
            "seconds": round(time.time() - t, 1),
        }
        print(
            f"[{time.time() - T0:.1f}s] integrate {name}: residual vectors equal in "
            f"{equal_words}/{len(terms)} terms, totals equal in {equal_totals}; "
            f"{len(words_straight)} distinct residual words (straight), {len(words_l)} (L)",
            flush=True,
        )
    t = time.time()
    pairs_equal = coeffs_equal = values_equal = 0
    families: dict = defaultdict(int)
    n_integrands = 0
    for key in terms:
        seq, lab = key[0], key[1:]
        ds = integrand_pairs(STRAIGHT, seq, lab)
        dl = integrand_pairs(LCHAIN, seq, lab)
        n_integrands += len(ds)
        key_c = lambda d: sorted(str(c.to_sympy()) for c, _v, _f in d)  # noqa: E731
        key_v = lambda d: sorted(str(v.to_sympy()) for _c, v, _f in d)  # noqa: E731
        key_p = lambda d: sorted((str(c.to_sympy()), str(v.to_sympy())) for c, v, _f in d)  # noqa: E731
        coeffs_equal += key_c(ds) == key_c(dl)
        values_equal += key_v(ds) == key_v(dl)
        pairs_equal += key_p(ds) == key_p(dl)
        for _c, _v, f in ds:
            families["straight " + str(f)] += 1
        for _c, _v, f in dl:
            families["L " + str(f)] += 1
    out["stages"]["pairs"] = {
        "terms": len(terms),
        "integrands_straight": n_integrands,
        "coefficient_multisets_equal": coeffs_equal,
        "haar_value_multisets_equal": values_equal,
        "coefficient_and_value_pair_multisets_equal": pairs_equal,
        "family_sizes": dict(sorted(families.items())),
        "seconds": round(time.time() - t, 1),
    }
    print(
        f"[{time.time() - T0:.1f}s] per-integrand pairs: coefficient multisets equal in "
        f"{coeffs_equal}/{len(terms)} terms, Haar-value multisets in {values_equal}, "
        f"(coefficient, value) pairs in {pairs_equal}; family sizes {dict(sorted(families.items()))}",
        flush=True,
    )
L.set_rank(3)
out["seconds"] = round(time.time() - T0, 1)
(HERE / "certificate.json").write_text(json.dumps(out, indent=1) + "\n", encoding="utf-8", newline="\n")
print("wrote certificate.json in", out["seconds"], "s")
