"""Degenerate perturbation theory on a small plaquette cluster, exactly, block by block.

The pinned engine supplies Wilson-word states, exact Haar inner products and the
H0 (Fierz) action; the H0-closure of a word is an H0-invariant block, so the
resolvent is solved block by block and the Gram is only ever evaluated on the
word pairs an inner product actually needs.
"""
import sys, time
from collections import defaultdict, deque
from fractions import Fraction as F
sys.path.insert(0, "/home/user/WORKHOUSE/corpus-import/programs/hodge_o4_adjudication/src")
import flint
import DATA_SU3_Exact_MarkedCluster_m4_Colab as M

LINKS = {}
def link(site, d):
    key = (tuple(site), d)
    if key not in LINKS: LINKS[key] = len(LINKS)
    return LINKS[key]
def add(a, b): return tuple(x + y for x, y in zip(a, b))
def e(j): v = [0, 0, 0]; v[j] = 1; return tuple(v)
def plaquette(plane, base, conj=False):
    i, j = plane
    steps = [(link(base, i), 1), (link(add(base, e(i)), j), 1), (link(add(base, e(j)), i), -1), (link(base, j), -1)]
    if conj: steps = [(l, -d) for l, d in reversed(steps)]
    return M.trace_state(steps)

def fq(x): return flint.fmpq(x.numerator, x.denominator)
def fr(x): return F(int(x.p), int(x.q))
def vadd(a, b, s=F(1)):
    out = defaultdict(F, a)
    for k, v in b.items(): out[k] += s * v
    return {k: v for k, v in out.items() if v}
def word_mul(vec, word):
    out = defaultdict(F)
    for w, c in vec.items():
        factor, red = M.simplify_unitarity(M.tensor_product(w, word))
        out[red] += c * factor
    return {k: v for k, v in out.items() if v}

_BLOCK = {}      # word -> block id
_BLOCKS = {}     # block id -> Block
class Block:
    def __init__(self, seed):
        words, seen, queue = [], set(), deque([seed])
        seen.add(seed)
        self.h0 = {}
        while queue:
            w = queue.popleft(); words.append(w)
            act = M.h0_action(w); self.h0[w] = act
            for w2 in act:
                if w2 not in seen: seen.add(w2); queue.append(w2)
        self.words = words; self.index = {w: i for i, w in enumerate(words)}
        n = len(words); self.n = n
        G = flint.fmpq_mat(n, n)
        for i in range(n):
            for j in range(i, n):
                G[i, j] = fq(M.haar_inner(words[i], words[j])); G[j, i] = G[i, j]
        H = flint.fmpq_mat(n, n)
        for j, w in enumerate(words):
            for w2, c in self.h0[w].items(): H[self.index[w2], j] += fq(c)
        self.G, self.H = G, H
        self.GH = G * H
        # the model words (single plaquettes) inside this block, if any
    def solve(self, e0, rhs, model_words):
        """y with <w_i|(E0 - H0)|y> = <w_i|Q rhs>, y ⟂ model words, on the quotient."""
        n = self.n
        A = flint.fmpq_mat(n, n)
        for i in range(n):
            for j in range(n):
                A[i, j] = self.G[i, j] * fq(e0) - self.GH[i, j]
        b = flint.fmpq_mat(n, 1)
        rv = flint.fmpq_mat(n, 1)
        for w, c in rhs.items(): rv[self.index[w], 0] = fq(c)
        b = self.G * rv
        # project against EVERY model word through the Haar inner product: for
        # SU(3) the antisymmetric fusion of two same-direction fluxes IS the
        # conjugate plaquette, so a model state can live inside a block's span
        # without being one of its words
        mw = [w for w in model_words if any(M.haar_inner(w, w2) for w2 in self.words)]
        m = len(mw)
        GM = flint.fmpq_mat(n, m)
        for k, w in enumerate(mw):
            for i in range(n): GM[i, k] = fq(M.haar_inner(self.words[i], w))
            ov = sum((fq(M.haar_inner(w, w2)) * fq(c) for w2, c in rhs.items()), flint.fmpq(0))
            for i in range(n): b[i, 0] -= GM[i, k] * ov
        N = n + m
        aug = flint.fmpq_mat(N, N + 1)
        for i in range(n):
            for j in range(n): aug[i, j] = A[i, j]
            for k in range(m): aug[i, n + k] = GM[i, k]; aug[n + k, i] = GM[i, k]
            aug[i, N] = b[i, 0]
        R, rank = aug.rref()
        y = {}
        for i in range(rank):
            piv = next((j for j in range(N) if R[i, j] != 0), None)
            if piv is None:
                if R[i, N] != 0: raise RuntimeError("inconsistent")
                continue
            if piv < n and R[i, N] != 0: y[self.words[piv]] = fr(R[i, N])
        for i in range(rank, N):
            if R[i, N] != 0: raise RuntimeError("inconsistent tail")
        return y

def block_of(word):
    if word not in _BLOCK:
        b = Block(word)
        bid = len(_BLOCKS); _BLOCKS[bid] = b
        for w in b.words: _BLOCK[w] = bid
    return _BLOCKS[_BLOCK[word]]

def resolvent(vec, e0, model_words):
    """R vec = Q (E0 - H0)^-1 Q vec, block by block."""
    groups = defaultdict(dict)
    for w, c in vec.items():
        b = block_of(w); groups[id(b)][w] = c
        groups[id(b)]["__block__"] = b
    out = {}
    for g in groups.values():
        b = g.pop("__block__")
        out = vadd(out, b.solve(e0, g, model_words))
    return out

def inner(x, y):
    tot = F(0)
    for w1, c1 in x.items():
        for w2, c2 in y.items():
            v = M.haar_inner(w1, w2)
            if v: tot += c1 * c2 * v
    return tot

class Cluster:
    def __init__(self, faces):
        self.faces = faces
        self.words = []
        for pl, b in faces:
            self.words.append(plaquette(pl, b)); self.words.append(plaquette(pl, b, conj=True))
        self.model = [{w: F(1)} for w in self.words]
        self.e0 = F(len(self.words[0].occ)) * M.CF / 2
    def apply_V(self, vec):
        out = {}
        for w in self.words: out = vadd(out, word_mul(vec, w))
        return out
    def effective(self, verbose=True):
        t0 = time.time(); e0 = self.e0; mw = self.words; m = len(mw)
        vs = [self.apply_V(d) for d in self.model]
        r = [resolvent(v, e0, mw) for v in vs]
        rr = [resolvent(x, e0, mw) for x in r]
        H2 = [[inner(vs[i], r[j]) for j in range(m)] for i in range(m)]
        VR2V = [[inner(vs[i], rr[j]) for j in range(m)] for i in range(m)]
        if verbose: print(f"  second order done, {len(_BLOCKS)} blocks, {time.time()-t0:.1f}s", flush=True)
        vr = [self.apply_V(x) for x in r]
        rvr = [resolvent(x, e0, mw) for x in vr]
        if verbose: print(f"  layer 2 done, {len(_BLOCKS)} blocks, {time.time()-t0:.1f}s", flush=True)
        vrvr = [self.apply_V(x) for x in rvr]
        H4a = [[inner(r[i], vrvr[j]) for j in range(m)] for i in range(m)]
        H4 = [[H4a[i][j] - sum(H2[i][k] * VR2V[k][j] + VR2V[i][k] * H2[k][j] for k in range(m)) / 2 for j in range(m)] for i in range(m)]
        if verbose: print(f"  fourth order done, {time.time()-t0:.1f}s", flush=True)
        return H2, VR2V, H4

def codd(Hm, i, j):
    a, b = 2 * i, 2 * j
    return (Hm[a][b] - Hm[a][b + 1] - Hm[a + 1][b] + Hm[a + 1][b + 1]) / 2
def ceven(Hm, i, j):
    a, b = 2 * i, 2 * j
    return (Hm[a][b] + Hm[a][b + 1] + Hm[a + 1][b] + Hm[a + 1][b + 1]) / 2

if __name__ == "__main__":
    single = Cluster([((0, 1), (0, 0, 0))])
    H2s, _, H4s = single.effective()
    print("single: C-odd diag 2nd", codd(H2s, 0, 0), " C-even diag 2nd", ceven(H2s, 0, 0), " 4th odd", codd(H4s, 0, 0), flush=True)
    pair = Cluster([((0, 1), (0, 0, 0)), ((0, 1), (1, 0, 0))])
    H2, VR2V, H4 = pair.effective()
    print("pair: C-odd hop 2nd", codd(H2, 0, 1), " C-even hop 2nd", ceven(H2, 0, 1), flush=True)
    print("pair: C-odd diag 2nd", codd(H2, 0, 0), " connected per-neighbour leakage:", codd(H2, 0, 0) - codd(H2s, 0, 0), flush=True)
    print("pair: 4th odd hop", codd(H4, 0, 1), " 4th odd diag", codd(H4, 0, 0), flush=True)
