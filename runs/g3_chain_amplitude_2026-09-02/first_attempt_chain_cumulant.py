"""The chain amplitude u: cumulant W({P,Q,R}) - W({P,R}) for the P -> R element.

Histories that never insert the connector Q are identical in both clusters and
cancel, so the direct term is computed on Q-touched histories only; the fold
term is second-order arithmetic on both clusters. Degree-3 Haar integrals then
occur only on shared links.
"""
import sys, time, pickle, atexit, os
from collections import defaultdict
from fractions import Fraction as F
import cluster_pt as P
M = P.M
CACHE = "haar_cache.pkl"
if os.path.exists(CACHE):
    with open(CACHE, "rb") as fh: M._HAAR_CACHE.update(pickle.load(fh))
    print("haar cache loaded:", len(M._HAAR_CACHE), flush=True)
def _save():
    with open(CACHE, "wb") as fh: pickle.dump(dict(M._HAAR_CACHE), fh)
atexit.register(_save)

def has_link(word, links): return any(l in links for l, _ in word.occ)

class Chain:
    def __init__(self, faces, connector_index):
        self.cl = P.Cluster(faces)
        self.q_words = {self.cl.words[2 * connector_index], self.cl.words[2 * connector_index + 1]}
        # links unique to Q identify Q-containing words: Q's links not in P or R
        q = self.cl.words[2 * connector_index]
        others = set()
        for i, w in enumerate(self.cl.words):
            if i // 2 != connector_index: others |= {l for l, _ in w.occ}
        self.q_only_links = {l for l, _ in q.occ} - others
        assert self.q_only_links, "connector must have a private link"
    def apply_V_split(self, vec_u, vec_t):
        """(untouched, touched) after one V insertion."""
        out_u, out_t = {}, dict()
        for w in self.cl.words:
            mu = P.word_mul(vec_u, w); mt = P.word_mul(vec_t, w)
            if w in self.q_words: out_t = P.vadd(out_t, mu)
            else: out_u = P.vadd(out_u, mu)
            out_t = P.vadd(out_t, mt)
        return out_u, out_t
    def touched_direct(self, i_from, i_to, verbose=True):
        """<r_to | V rvr_from> restricted to histories touching Q."""
        e0 = self.cl.e0; mw = self.cl.words; t0 = time.time()
        d = self.cl.model[i_from]
        v_u, v_t = self.apply_V_split(d, {})
        r_u, r_t = P.resolvent(v_u, e0, mw), P.resolvent(v_t, e0, mw)
        if verbose: print(f"    layer1 |r_u|={len(r_u)} |r_t|={len(r_t)} {time.time()-t0:.0f}s", flush=True)
        vr_u, vr_t = self.apply_V_split(r_u, r_t)
        rvr_u, rvr_t = P.resolvent(vr_u, e0, mw), P.resolvent(vr_t, e0, mw)
        if verbose: print(f"    layer2 |rvr_u|={len(rvr_u)} |rvr_t|={len(rvr_t)} {time.time()-t0:.0f}s", flush=True)
        w3_u, w3_t = self.apply_V_split(rvr_u, rvr_t)
        # bra: r_to = R V d_to, split by whether the bra word contains Q
        v_to = self.cl.apply_V(self.cl.model[i_to])
        r_to = P.resolvent(v_to, e0, mw)
        r_to_q = {w: c for w, c in r_to.items() if has_link(w, self.q_only_links)}
        val = P.inner(r_to, w3_t) + P.inner(r_to_q, w3_u)
        if verbose: print(f"    direct(touched) {i_from}->{i_to} = {val}  [{time.time()-t0:.0f}s]", flush=True)
        return val

def second_order_objects(cl):
    e0 = cl.e0; mw = cl.words; m = len(mw)
    vs = [cl.apply_V(d) for d in cl.model]
    r = [P.resolvent(v, e0, mw) for v in vs]
    rr = [P.resolvent(x, e0, mw) for x in r]
    H2 = [[P.inner(vs[i], r[j]) for j in range(m)] for i in range(m)]
    VR2V = [[P.inner(vs[i], rr[j]) for j in range(m)] for i in range(m)]
    return H2, VR2V

def fold(H2, VR2V, i, j, m):
    return sum(H2[i][k] * VR2V[k][j] + VR2V[i][k] * H2[k][j] for k in range(m)) / 2

def chain_amplitude(faces3, faces2, connector_index, label):
    """Both orientations of the endpoints, C-odd projected."""
    t0 = time.time()
    ch = Chain(faces3, connector_index)
    H2_3, V2_3 = second_order_objects(ch.cl)
    cl2 = P.Cluster(faces2)
    H2_2, V2_2 = second_order_objects(cl2)
    print(f"  {label}: second-order objects ready ({time.time()-t0:.0f}s)", flush=True)
    # indices: in faces3 the endpoints are faces 0 and 2 (P, R); in faces2 they are 0 and 1
    idx3 = {"P": 0, "Pb": 1, "R": 4, "Rb": 5}
    idx2 = {"P": 0, "Pb": 1, "R": 2, "Rb": 3}
    W = {}
    for a in ("P", "Pb"):
        for b in ("R", "Rb"):
            direct = ch.touched_direct(idx3[a], idx3[b])
            f3 = fold(H2_3, V2_3, idx3[b], idx3[a], 6)
            f2 = fold(H2_2, V2_2, idx2[b], idx2[a], 4)
            W[(a, b)] = direct - (f3 - f2)
            print(f"    W[{a}->{b}] = {W[(a, b)]}  (fold3-fold2 = {f3 - f2})", flush=True)
    codd = (W[("P", "R")] - W[("P", "Rb")] - W[("Pb", "R")] + W[("Pb", "Rb")]) / 2
    ceven = (W[("P", "R")] + W[("P", "Rb")] + W[("Pb", "R")] + W[("Pb", "Rb")]) / 2
    print(f"  {label}: C-odd chain amplitude = {codd} = {float(codd):.6e};  C-even = {ceven} = {float(ceven):.6e}   [{time.time()-t0:.0f}s]", flush=True)
    print(f"  {label}: X_QUANTUM = {F(360421351, 40327601932800)} = {360421351/40327601932800:.6e}; cold u = {4.132743700859149*360421351/40327601932800:.6e}", flush=True)
    return codd, ceven

if __name__ == "__main__":
    which = sys.argv[1] if len(sys.argv) > 1 else "coplanar"
    if which == "coplanar":
        faces3 = [((0, 1), (0, 0, 0)), ((0, 1), (1, 0, 0)), ((0, 1), (2, 0, 0))]
        faces2 = [((0, 1), (0, 0, 0)), ((0, 1), (2, 0, 0))]
    elif which == "bent":
        # P bottom (0,1) at origin, Q side face (0,2) at origin sharing the x-link, R = (0,1) at z=1 (opposite face, shares the top x-link of Q)
        faces3 = [((0, 1), (0, 0, 0)), ((0, 2), (0, 0, 0)), ((0, 1), (0, 0, 1))]
        faces2 = [((0, 1), (0, 0, 0)), ((0, 1), (0, 0, 1))]
    chain_amplitude(faces3, faces2, 1, which)
