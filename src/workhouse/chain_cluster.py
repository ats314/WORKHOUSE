"""Exact degenerate perturbation theory on a small plaquette cluster, and the chain amplitude u.

The G3 route "chain amplitude u on the three-plaquette cluster" (ADR 0019).
The pinned exact engine (corpus-import/programs/hodge_o4_adjudication) supplies
three primitives only -- Wilson-word states, exact Haar inner products and the
H0 (Fierz) action; everything else is here: the H0-closure of a word as an
invariant block, the resolvent as an exact polynomial in H0 on that block (H0
has rational spectrum, so no Gram matrix and no Haar integral is needed to
apply it), the projector off the model space (p(E0) = 0, which is exact because
the only states at the one-plaquette energy are plaquettes -- for SU(3) that
includes the antisymmetric fusion of two same-direction fluxes, which IS the
conjugate plaquette), and textbook Hermitian fourth-order theory with PVP = 0:

    H2 = P V R V P,    H4 = P V R V R V R V P - (1/2){P V R V P, P V R^2 V P}.

Haar integrals are attempted only where link-charge conservation allows a
nonzero value (charge difference 0 mod 3 on every link). The chain amplitude
is the cluster cumulant W({P,Q,R}) - W({P,R}) of the P -> R element: the
histories that never insert the connector Q are identical in both clusters and
cancel, so the direct term is taken on Q-touched histories only.

Everything is exact rational arithmetic; the whole computation runs in seconds.
"""

from __future__ import annotations

import sys
from collections import Counter, defaultdict, deque
from fractions import Fraction as F
from pathlib import Path

import flint
from sympy import Poly, Rational, interpolate, roots, symbols

ROOT = Path(__file__).resolve().parents[2]
ENGINE = ROOT / "corpus-import" / "programs" / "hodge_o4_adjudication" / "src"
if str(ENGINE) not in sys.path:
    sys.path.insert(0, str(ENGINE))
import DATA_SU3_Exact_MarkedCluster_m4_Colab as M  # noqa: E402

X_QUANTUM = F(360421351, 40327601932800)


# ---- geometry
LINKS = {}


def link(site, d):
    key = (tuple(site), d)
    if key not in LINKS:
        LINKS[key] = len(LINKS)
    return LINKS[key]


def add(a, b):
    return tuple(x + y for x, y in zip(a, b, strict=True))


def e(j):
    v = [0, 0, 0]
    v[j] = 1
    return tuple(v)


def plaquette(plane, base, conj=False):
    i, j = plane
    steps = [
        (link(base, i), 1),
        (link(add(base, e(i)), j), 1),
        (link(add(base, e(j)), i), -1),
        (link(base, j), -1),
    ]
    if conj:
        steps = [(lk, -d) for lk, d in reversed(steps)]
    return M.trace_state(steps)


# ---- vectors
def vadd(a, b, s=F(1)):
    out = defaultdict(F, a)
    for k, v in b.items():
        out[k] += s * v
    return {k: v for k, v in out.items() if v}


def word_mul(vec, word):
    out = defaultdict(F)
    for w, c in vec.items():
        factor, red = M.simplify_unitarity(M.tensor_product(w, word))
        out[red] += c * factor
    return {k: v for k, v in out.items() if v}


def charge(word):
    ch = Counter()
    for lk, is_u in word.occ:
        ch[lk] += 1 if is_u else -1
    return ch


_CHARGE = {}


def charge_of(w):
    if w not in _CHARGE:
        _CHARGE[w] = charge(w)
    return _CHARGE[w]


def compatible(w1, w2):
    """Haar integral <w1|w2> can be nonzero only if every link's charge difference is 0 mod 3."""
    c1, c2 = charge_of(w1), charge_of(w2)
    return all((c1.get(lk, 0) - c2.get(lk, 0)) % 3 == 0 for lk in set(c1) | set(c2))


STATS = Counter()


def inner(x, y):
    tot = F(0)
    for w1, c1 in x.items():
        for w2, c2 in y.items():
            STATS["pairs"] += 1
            if not compatible(w1, w2):
                STATS["pruned"] += 1
                continue
            v = M.haar_inner(w1, w2)
            STATS["integrals"] += 1
            if v:
                tot += c1 * c2 * v
    return tot


# ---- polynomial resolvent on H0-invariant blocks
_BLOCK = {}
_BLOCKS = {}


class Block:
    def __init__(self, seed, e0):
        words, seen, queue = [], {seed}, deque([seed])
        self.h0 = {}
        while queue:
            w = queue.popleft()
            words.append(w)
            act = M.h0_action(w)
            self.h0[w] = act
            for w2 in act:
                if w2 not in seen:
                    seen.add(w2)
                    queue.append(w2)
        self.words = words
        self.index = {w: i for i, w in enumerate(words)}
        n = len(words)
        self.n = n
        H = flint.fmpq_mat(n, n)
        for j, w in enumerate(words):
            for w2, c in self.h0[w].items():
                H[self.index[w2], j] += flint.fmpq(c.numerator, c.denominator)
        self.H = H
        # rational roots of the characteristic polynomial: the H0 spectrum on the
        # block, plus harmless extras from the null space of dependent words
        cp = H.charpoly()
        x = symbols("x")
        coeffs = [Rational(int(cp[k].p), int(cp[k].q)) for k in range(cp.degree(), -1, -1)]
        poly = Poly(coeffs, x)
        rts = [r for r in roots(poly, filter="Q")]
        self.spectrum = sorted(set(rts))
        # interpolation polynomial p with p(lam) = 1/(e0 - lam) for lam != e0, p(e0) = 0
        E0 = Rational(e0.numerator, e0.denominator)
        pts = [(lam, (0 if lam == E0 else 1 / (E0 - lam))) for lam in self.spectrum]
        if E0 not in self.spectrum:
            pts.append((E0, 0))
        p = Poly(interpolate(pts, x), x)
        self.pcoeffs = [F(int(c.p), int(c.q)) for c in p.all_coeffs()]  # highest degree first

    def apply(self, rhs):
        n = self.n
        v = flint.fmpq_mat(n, 1)
        for w, c in rhs.items():
            v[self.index[w], 0] = flint.fmpq(c.numerator, c.denominator)
        acc = flint.fmpq_mat(n, 1)
        for c in self.pcoeffs:  # Horner: acc = acc*H + c*v
            acc = self.H * acc
            if c:
                cq = flint.fmpq(c.numerator, c.denominator)
                for i in range(n):
                    acc[i, 0] += cq * v[i, 0]
        return {
            self.words[i]: F(int(acc[i, 0].p), int(acc[i, 0].q)) for i in range(n) if acc[i, 0] != 0
        }


def block_of(word, e0):
    if word not in _BLOCK:
        b = Block(word, e0)
        bid = len(_BLOCKS)
        _BLOCKS[bid] = b
        for w in b.words:
            _BLOCK[w] = bid
    return _BLOCKS[_BLOCK[word]]


def resolvent(vec, e0):
    groups = defaultdict(dict)
    for w, c in vec.items():
        groups[id(block_of(w, e0))][w] = c
    out = {}
    done = set()
    for w in vec:
        b = block_of(w, e0)
        if id(b) in done:
            continue
        done.add(id(b))
        out = vadd(out, b.apply(groups[id(b)]))
    return out


class Cluster:
    def __init__(self, faces):
        self.faces = faces
        self.words = []
        for pl, b in faces:
            self.words.append(plaquette(pl, b))
            self.words.append(plaquette(pl, b, conj=True))
        self.model = [{w: F(1)} for w in self.words]
        self.e0 = F(len(self.words[0].occ)) * M.CF / 2

    def apply_V(self, vec):
        out = {}
        for w in self.words:
            out = vadd(out, word_mul(vec, w))
        return out


def codd(Hm, i, j):
    a, b = 2 * i, 2 * j
    return (Hm[a][b] - Hm[a][b + 1] - Hm[a + 1][b] + Hm[a + 1][b + 1]) / 2


def ceven(Hm, i, j):
    a, b = 2 * i, 2 * j
    return (Hm[a][b] + Hm[a][b + 1] + Hm[a + 1][b] + Hm[a + 1][b + 1]) / 2


def second_order(cl):
    e0 = cl.e0
    m = len(cl.words)
    vs = [cl.apply_V(d) for d in cl.model]
    r = [resolvent(v, e0) for v in vs]
    rr = [resolvent(x, e0) for x in r]
    H2 = [[inner(vs[i], r[j]) for j in range(m)] for i in range(m)]
    VR2V = [[inner(vs[i], rr[j]) for j in range(m)] for i in range(m)]
    return H2, VR2V, vs, r


def validate():
    single = Cluster([((0, 1), (0, 0, 0))])
    H2s, _, _, _ = second_order(single)
    pair = Cluster([((0, 1), (0, 0, 0)), ((0, 1), (1, 0, 0))])
    H2, _, _, _ = second_order(pair)
    perp = Cluster([((0, 1), (0, 0, 0)), ((0, 2), (0, 0, 0))])
    H2p, _, _, _ = second_order(perp)
    hop, hopp, ceven_hop = codd(H2, 0, 1), codd(H2p, 0, 1), ceven(H2, 0, 1)
    leak = codd(H2, 0, 0) - codd(H2s, 0, 0) + F(3, 4)
    ok = (
        hop == F(-5, 612) and hopp == F(5, 612) and ceven_hop == F(-11, 306) and leak == F(-11, 306)
    )
    return {
        "coplanar_hop": hop,
        "perpendicular_hop": hopp,
        "c_even_hop": ceven_hop,
        "leakage": leak,
        "ok": ok,
    }


class Chain:
    def __init__(self, faces3, faces2, ci):
        self.cl = Cluster(faces3)
        self.cl2 = Cluster(faces2)
        self.q_words = {self.cl.words[2 * ci], self.cl.words[2 * ci + 1]}
        q = self.cl.words[2 * ci]
        others = set()
        for i, w in enumerate(self.cl.words):
            if i // 2 != ci:
                others |= {lk for lk, _ in w.occ}
        self.q_links = {lk for lk, _ in q.occ} - others

    def apply_V_split(self, vu, vt):
        ou, ot = {}, {}
        for w in self.cl.words:
            mu, mt = word_mul(vu, w), word_mul(vt, w)
            if w in self.q_words:
                ot = vadd(ot, mu)
            else:
                ou = vadd(ou, mu)
            ot = vadd(ot, mt)
        return ou, ot

    def run(self, label):
        e0 = self.cl.e0
        H2_3, V2_3, vs3, r3 = second_order(self.cl)
        H2_2, V2_2, _, _ = second_order(self.cl2)
        idx3 = {"P": 0, "Pb": 1, "R": 4, "Rb": 5}
        idx2 = {"P": 0, "Pb": 1, "R": 2, "Rb": 3}
        # ket side for P and Pb: r split, then rvr split
        ket = {}
        for a in ("P", "Pb"):
            vu, vt = self.apply_V_split(self.cl.model[idx3[a]], {})
            ru, rt = resolvent(vu, e0), resolvent(vt, e0)
            vru, vrt = self.apply_V_split(ru, rt)
            ket[a] = (resolvent(vru, e0), resolvent(vrt, e0))
        # bra side for R and Rb: V r_R, split by Q-content
        bra = {}
        for b in ("R", "Rb"):
            vr = self.cl.apply_V(r3[idx3[b]])
            vr_q = {w: c for w, c in vr.items() if any(lk in self.q_links for lk, _ in w.occ)}
            bra[b] = (vr, vr_q)
        W = {}
        for a in ("P", "Pb"):
            for b in ("R", "Rb"):
                direct = inner(bra[b][0], ket[a][1]) + inner(bra[b][1], ket[a][0])
                m3, m2 = 6, 4
                f3 = (
                    sum(
                        H2_3[idx3[b]][k] * V2_3[k][idx3[a]] + V2_3[idx3[b]][k] * H2_3[k][idx3[a]]
                        for k in range(m3)
                    )
                    / 2
                )
                f2 = (
                    sum(
                        H2_2[idx2[b]][k] * V2_2[k][idx2[a]] + V2_2[idx2[b]][k] * H2_2[k][idx2[a]]
                        for k in range(m2)
                    )
                    / 2
                )
                W[(a, b)] = direct - (f3 - f2)
        u_odd = (W[("P", "R")] - W[("P", "Rb")] - W[("Pb", "R")] + W[("Pb", "Rb")]) / 2
        u_even = (W[("P", "R")] + W[("P", "Rb")] + W[("Pb", "R")] + W[("Pb", "Rb")]) / 2
        return u_odd, u_even


CHAINS = {
    # P at the origin in plane (0,1); Q the connector; R the far endpoint
    "coplanar": ([((0, 1), (0, 0, 0)), ((0, 1), (1, 0, 0)), ((0, 1), (2, 0, 0))]),
    # P bottom face, Q a side face sharing P's x-link, R the top face: two perpendicular junctions
    "bent": ([((0, 1), (0, 0, 0)), ((0, 2), (0, 0, 0)), ((0, 1), (0, 0, 1))]),
}


def chain_amplitude(which: str) -> tuple[F, F]:
    """(C-odd, C-even) chain amplitude for the named chain, exactly."""
    faces3 = CHAINS[which]
    return Chain(faces3, [faces3[0], faces3[2]], 1).run(which)
