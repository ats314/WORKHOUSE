"""Chain amplitude u, fast form: polynomial resolvent (no Gram), charge-pruned inner products, live log."""
import sys, time, pickle, os
from collections import defaultdict, deque, Counter
from fractions import Fraction as F
sys.path.insert(0, "/home/user/WORKHOUSE/corpus-import/programs/hodge_o4_adjudication/src")
import flint
import DATA_SU3_Exact_MarkedCluster_m4_Colab as M
from sympy import Rational, symbols, Poly, roots, interpolate

LOG = open(sys.argv[2] if len(sys.argv) > 2 else "chain.log", "a")
T0 = time.time()
def log(msg):
    line = f"[{time.time()-T0:7.0f}s] {msg}"
    print(line, flush=True); LOG.write(line + "\n"); LOG.flush()
CACHE = "haar_cache.pkl"
if os.path.exists(CACHE):
    with open(CACHE, "rb") as fh: M._HAAR_CACHE.update(pickle.load(fh))
    log(f"haar cache loaded: {len(M._HAAR_CACHE)}")
_last_save = [time.time()]
def save_cache(force=False):
    if force or time.time() - _last_save[0] > 120:
        with open(CACHE + ".tmp", "wb") as fh: pickle.dump(dict(M._HAAR_CACHE), fh)
        os.replace(CACHE + ".tmp", CACHE); _last_save[0] = time.time()

# ---- geometry
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

# ---- vectors
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
def charge(word):
    ch = Counter()
    for l, is_u in word.occ: ch[l] += 1 if is_u else -1
    return ch
_CHARGE = {}
def charge_of(w):
    if w not in _CHARGE: _CHARGE[w] = charge(w)
    return _CHARGE[w]
def compatible(w1, w2):
    """Haar integral <w1|w2> can be nonzero only if every link's charge difference is 0 mod 3."""
    c1, c2 = charge_of(w1), charge_of(w2)
    for l in set(c1) | set(c2):
        if (c1.get(l, 0) - c2.get(l, 0)) % 3: return False
    return True
STATS = Counter()
def inner(x, y):
    tot = F(0)
    for w1, c1 in x.items():
        for w2, c2 in y.items():
            STATS["pairs"] += 1
            if not compatible(w1, w2): STATS["pruned"] += 1; continue
            v = M.haar_inner(w1, w2); STATS["integrals"] += 1
            if v: tot += c1 * c2 * v
    save_cache()
    return tot

# ---- polynomial resolvent on H0-invariant blocks
_BLOCK = {}; _BLOCKS = {}
class Block:
    def __init__(self, seed, e0):
        words, seen, queue = [], {seed}, deque([seed]); self.h0 = {}
        while queue:
            w = queue.popleft(); words.append(w)
            act = M.h0_action(w); self.h0[w] = act
            for w2 in act:
                if w2 not in seen: seen.add(w2); queue.append(w2)
        self.words = words; self.index = {w: i for i, w in enumerate(words)}; n = len(words); self.n = n
        H = flint.fmpq_mat(n, n)
        for j, w in enumerate(words):
            for w2, c in self.h0[w].items(): H[self.index[w2], j] += flint.fmpq(c.numerator, c.denominator)
        self.H = H
        # rational roots of the characteristic polynomial: the H0 spectrum on the block (plus null-space extras)
        cp = H.charpoly()
        x = symbols("x")
        coeffs = [Rational(int(cp[k].p), int(cp[k].q)) for k in range(cp.degree(), -1, -1)]
        poly = Poly(coeffs, x)
        rts = [r for r in roots(poly, filter="Q")]
        self.spectrum = sorted(set(rts))
        # interpolation polynomial p with p(lam) = 1/(e0 - lam) for lam != e0, p(e0) = 0
        E0 = Rational(e0.numerator, e0.denominator)
        pts = [(lam, (0 if lam == E0 else 1 / (E0 - lam))) for lam in self.spectrum]
        if E0 not in self.spectrum: pts.append((E0, 0))
        p = Poly(interpolate(pts, x), x)
        self.pcoeffs = [F(int(c.p), int(c.q)) for c in p.all_coeffs()]  # highest degree first
    def apply(self, rhs):
        n = self.n
        v = flint.fmpq_mat(n, 1)
        for w, c in rhs.items(): v[self.index[w], 0] = flint.fmpq(c.numerator, c.denominator)
        acc = flint.fmpq_mat(n, 1)
        for c in self.pcoeffs:  # Horner: acc = acc*H + c*v
            acc = self.H * acc
            if c:
                cq = flint.fmpq(c.numerator, c.denominator)
                for i in range(n): acc[i, 0] += cq * v[i, 0]
        return {self.words[i]: F(int(acc[i, 0].p), int(acc[i, 0].q)) for i in range(n) if acc[i, 0] != 0}
def block_of(word, e0):
    if word not in _BLOCK:
        b = Block(word, e0); bid = len(_BLOCKS); _BLOCKS[bid] = b
        for w in b.words: _BLOCK[w] = bid
    return _BLOCKS[_BLOCK[word]]
def resolvent(vec, e0):
    groups = defaultdict(dict)
    for w, c in vec.items(): groups[id(block_of(w, e0))][w] = c
    out = {}
    for w in list(vec):
        pass
    done = set()
    for w, c in vec.items():
        b = block_of(w, e0)
        if id(b) in done: continue
        done.add(id(b))
        out = vadd(out, b.apply(groups[id(b)]))
    return out

class Cluster:
    def __init__(self, faces):
        self.faces = faces; self.words = []
        for pl, b in faces:
            self.words.append(plaquette(pl, b)); self.words.append(plaquette(pl, b, conj=True))
        self.model = [{w: F(1)} for w in self.words]
        self.e0 = F(len(self.words[0].occ)) * M.CF / 2
    def apply_V(self, vec):
        out = {}
        for w in self.words: out = vadd(out, word_mul(vec, w))
        return out
def codd(Hm, i, j):
    a, b = 2 * i, 2 * j
    return (Hm[a][b] - Hm[a][b + 1] - Hm[a + 1][b] + Hm[a + 1][b + 1]) / 2
def ceven(Hm, i, j):
    a, b = 2 * i, 2 * j
    return (Hm[a][b] + Hm[a][b + 1] + Hm[a + 1][b] + Hm[a + 1][b + 1]) / 2

def second_order(cl):
    e0 = cl.e0; m = len(cl.words)
    vs = [cl.apply_V(d) for d in cl.model]
    r = [resolvent(v, e0) for v in vs]
    rr = [resolvent(x, e0) for x in r]
    H2 = [[inner(vs[i], r[j]) for j in range(m)] for i in range(m)]
    VR2V = [[inner(vs[i], rr[j]) for j in range(m)] for i in range(m)]
    return H2, VR2V, vs, r

def validate():
    single = Cluster([((0, 1), (0, 0, 0))]); H2s, _, _, _ = second_order(single)
    pair = Cluster([((0, 1), (0, 0, 0)), ((0, 1), (1, 0, 0))]); H2, _, _, _ = second_order(pair)
    perp = Cluster([((0, 1), (0, 0, 0)), ((0, 2), (0, 0, 0))]); H2p, _, _, _ = second_order(perp)
    hop, hopp, ceven_hop = codd(H2, 0, 1), codd(H2p, 0, 1), ceven(H2, 0, 1)
    leak = codd(H2, 0, 0) - codd(H2s, 0, 0) + F(3, 4)
    ok = hop == F(-5, 612) and hopp == F(5, 612) and ceven_hop == F(-11, 306) and leak == F(-11, 306)
    log(f"validation: coplanar hop {hop}, perpendicular hop {hopp}, C-even hop {ceven_hop}, leakage {leak} -> {'OK' if ok else 'MISMATCH'}")
    if not ok: raise SystemExit("second-order validation failed")

class Chain:
    def __init__(self, faces3, faces2, ci):
        self.cl = Cluster(faces3); self.cl2 = Cluster(faces2)
        self.q_words = {self.cl.words[2 * ci], self.cl.words[2 * ci + 1]}
        q = self.cl.words[2 * ci]; others = set()
        for i, w in enumerate(self.cl.words):
            if i // 2 != ci: others |= {l for l, _ in w.occ}
        self.q_links = {l for l, _ in q.occ} - others
    def apply_V_split(self, vu, vt):
        ou, ot = {}, {}
        for w in self.cl.words:
            mu, mt = word_mul(vu, w), word_mul(vt, w)
            if w in self.q_words: ot = vadd(ot, mu)
            else: ou = vadd(ou, mu)
            ot = vadd(ot, mt)
        return ou, ot
    def run(self, label):
        e0 = self.cl.e0
        H2_3, V2_3, vs3, r3 = second_order(self.cl)
        H2_2, V2_2, _, _ = second_order(self.cl2)
        log(f"{label}: second-order objects ready; integrals so far {STATS['integrals']} (pruned {STATS['pruned']} of {STATS['pairs']})")
        idx3 = {"P": 0, "Pb": 1, "R": 4, "Rb": 5}; idx2 = {"P": 0, "Pb": 1, "R": 2, "Rb": 3}
        # ket side for P and Pb: r split, then rvr split
        ket = {}
        for a in ("P", "Pb"):
            vu, vt = self.apply_V_split(self.cl.model[idx3[a]], {})
            ru, rt = resolvent(vu, e0), resolvent(vt, e0)
            vru, vrt = self.apply_V_split(ru, rt)
            ket[a] = (resolvent(vru, e0), resolvent(vrt, e0))
            log(f"{label}: ket {a}: |rvr_u|={len(ket[a][0])} |rvr_t|={len(ket[a][1])}")
        # bra side for R and Rb: V r_R, split by Q-content
        bra = {}
        for b in ("R", "Rb"):
            vr = self.cl.apply_V(r3[idx3[b]])
            vr_q = {w: c for w, c in vr.items() if any(l in self.q_links for l, _ in w.occ)}
            bra[b] = (vr, vr_q)
            log(f"{label}: bra {b}: |V r|={len(vr)} of which Q-words {len(vr_q)}")
        W = {}
        for a in ("P", "Pb"):
            for b in ("R", "Rb"):
                t1 = time.time()
                direct = inner(bra[b][0], ket[a][1]) + inner(bra[b][1], ket[a][0])
                m3, m2 = 6, 4
                f3 = sum(H2_3[idx3[b]][k] * V2_3[k][idx3[a]] + V2_3[idx3[b]][k] * H2_3[k][idx3[a]] for k in range(m3)) / 2
                f2 = sum(H2_2[idx2[b]][k] * V2_2[k][idx2[a]] + V2_2[idx2[b]][k] * H2_2[k][idx2[a]] for k in range(m2)) / 2
                W[(a, b)] = direct - (f3 - f2)
                log(f"{label}: W[{a}->{b}] = {W[(a, b)]} (direct {direct}, fold diff {f3 - f2}) in {time.time()-t1:.0f}s; integrals {STATS['integrals']}, pruned {STATS['pruned']}/{STATS['pairs']}")
        u_odd = (W[("P", "R")] - W[("P", "Rb")] - W[("Pb", "R")] + W[("Pb", "Rb")]) / 2
        u_even = (W[("P", "R")] + W[("P", "Rb")] + W[("Pb", "R")] + W[("Pb", "Rb")]) / 2
        xq = F(360421351, 40327601932800)
        log(f"{label}: RESULT C-odd chain amplitude = {u_odd} = {float(u_odd):.9e}; C-even = {u_even} = {float(u_even):.9e}")
        log(f"{label}: X_QUANTUM = {float(xq):.9e}; ratio to X_QUANTUM = {float(u_odd / xq):.9f}; cold ratio would be 4.132743701")
        save_cache(force=True)
        return u_odd

if __name__ == "__main__":
    which = sys.argv[1] if len(sys.argv) > 1 else "coplanar"
    validate()
    if which == "coplanar":
        f3 = [((0, 1), (0, 0, 0)), ((0, 1), (1, 0, 0)), ((0, 1), (2, 0, 0))]; f2 = [f3[0], f3[2]]
    else:
        f3 = [((0, 1), (0, 0, 0)), ((0, 2), (0, 0, 0)), ((0, 1), (0, 0, 1))]; f2 = [f3[0], f3[2]]
    Chain(f3, f2, 1).run(which)
    log("done")
