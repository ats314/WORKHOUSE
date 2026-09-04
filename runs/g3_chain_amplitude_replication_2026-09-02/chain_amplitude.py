"""The chain amplitude u, independently, on three-plaquette clusters.

An exact fourth-order degenerate perturbation theory on a small plaquette
cluster that uses the pinned exact engine ONLY for Wilson-word states, the
word product with unitarity simplification, the H0 (Fierz) action and Haar
inner products.  Everything else -- closure, resolvent, the Hermitian
fourth-order formula, the C-parity projection, the cluster cumulant -- is
here, and never reads either recorded kernel.

Two things make it fast where the staged version was not:

1. No Gram matrices.  H0 preserves the link occupation of a word, so each
   word's H0-closure is a finite block (2 to 8 words here), and on that
   block the electric operator has a rational spectrum.  The reduced
   resolvent Q (E0 - H0)^-1 Q is therefore an exact polynomial in H0:
   with r the squarefree part of the block's characteristic polynomial and
   g = r/(x - E0), the projector off the E0 eigenspace is 1 - g(H0)/g(E0)
   and the inverse of (E0 - x) modulo g is h/g(E0), h = (g(x)-g(E0))/(x-E0).
   The word basis is over-complete (for SU(3) the antisymmetric fusion of
   two same-direction fluxes is the conjugate plaquette), but any polynomial
   identity on the lifted matrix descends to the true operator, and the true
   minimal polynomial divides r because the true operator is diagonalisable.

2. Every matrix element is evaluated one-sided, <d_i | V G V G V G V d_j>,
   against a single-plaquette bra.  Then no Haar family above (2,2) is ever
   needed, and a per-link triality signature skips every inner product that
   link-charge conservation forces to zero before the engine is called.
"""

from __future__ import annotations

import json
import sys
import time
from collections import defaultdict
from fractions import Fraction as F
from pathlib import Path

import flint

HERE = Path(__file__).resolve().parent
ENGINE = HERE.parents[1] / "corpus-import" / "programs" / "hodge_o4_adjudication" / "src"
sys.path.insert(0, str(ENGINE))
import DATA_SU3_Exact_MarkedCluster_m4_Colab as M  # noqa: E402

X_QUANTUM = F(360421351, 40327601932800)
COLD_SCALE = 4.132743700859149  # runs/g3_kernel_record_dump_2026-08-28, float only

# ----------------------------------------------------------------------------
# lattice words
# ----------------------------------------------------------------------------
LINKS: dict[tuple[tuple[int, int, int], int], int] = {}


def link(site, d):
    key = (tuple(site), d)
    if key not in LINKS:
        LINKS[key] = len(LINKS)
    return LINKS[key]


def add(a, b):
    return tuple(x + y for x, y in zip(a, b))


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
        steps = [(l, -d) for l, d in reversed(steps)]
    return M.trace_state(steps)


def fq(x):
    return flint.fmpq(x.numerator, x.denominator)


def fr(x):
    return F(int(x.p), int(x.q))


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


def triality(word):
    sig = defaultdict(int)
    for l, is_u in word.occ:
        sig[l] += 1 if is_u else -1
    return tuple(sorted((l, n % 3) for l, n in sig.items() if n % 3))


def tri_add(a, b):
    """Per-link sum of two triality signatures, mod 3."""
    d = defaultdict(int, dict(a))
    for l, n in b:
        d[l] = (d[l] + n) % 3
    return tuple(sorted((l, n) for l, n in d.items() if n))


def reachable(targets, plaquette_words, remaining):
    """Signatures that reach one of `targets` with `remaining` more insertions."""
    sums = {()}
    for _ in range(remaining):
        sums = {tri_add(s, triality(w)) for s in sums for w in plaquette_words}
    neg = lambda s: tuple((l, (-n) % 3) for l, n in s)  # noqa: E731
    return {tri_add(t, neg(s)) for t in targets for s in sums}


def filt(vec, allowed):
    """Drop every word whose triality cannot reach the bra.  Exact: H0 keeps occupancy."""
    return {w: c for w, c in vec.items() if triality(w) in allowed}


HAAR_CALLS = {"engine": 0, "skipped": 0, "slow": 0}


def haar(w1, w2):
    """<w1|w2>, with the triality skip in front of the engine."""
    if triality(w1) != triality(w2):
        HAAR_CALLS["skipped"] += 1
        return F(0)
    HAAR_CALLS["engine"] += 1
    t0 = time.time()
    v = M.haar_inner(w1, w2)
    dt = time.time() - t0
    if dt > 0.5:
        HAAR_CALLS["slow"] += 1
        fam = family(w1, w2)
        print(f"      slow haar {dt:.1f}s family {fam} occ {len(w1.occ)}+{len(w2.occ)}", flush=True)
    return v


def family(w1, w2):
    """Per-link (U, Udag) counts of the combined bra-ket integrand, largest first."""
    cnt = defaultdict(lambda: [0, 0])
    for l, is_u in w1.occ:
        cnt[l][0 if not is_u else 1] += 1  # bra is conjugated
    for l, is_u in w2.occ:
        cnt[l][0 if is_u else 1] += 1
    return sorted((tuple(v) for v in cnt.values()), reverse=True)[:3]


def inner(x, y):
    tot = F(0)
    for w1, c1 in x.items():
        for w2, c2 in y.items():
            v = haar(w1, w2)
            if v:
                tot += c1 * c2 * v
    return tot


# ----------------------------------------------------------------------------
# the polynomial resolvent, by a Krylov minimal polynomial relative to the vector
# ----------------------------------------------------------------------------
_H0: dict = {}
KRYLOV_STATS = {"max_degree": 0, "calls": 0}
E0_SEEN = {"with_e0": 0, "without": 0}


def apply_H0(vec):
    out = defaultdict(F)
    for w, c in vec.items():
        act = _H0.get(w)
        if act is None:
            act = _H0[w] = M.h0_action(w)
        for w2, c2 in act.items():
            out[w2] += c * c2
    return {k: v for k, v in out.items() if v}


def resolvent(vec, e0, model_words=None):
    """G vec = Q (E0 - H0)^-1 Q vec, exactly, with no Gram and no charpoly.

    Krylov: v, H0 v, H0^2 v, ... until the first exact linear dependence gives
    the minimal polynomial m of H0 relative to v on the lifted word space.  Its
    degree is the number of distinct energies v touches (a handful), never the
    block size.  With r the squarefree part of m and g = r/(x - E0):
        (1 - P_E0) = 1 - g(H0)/g(E0),   Q(E0 - H0)^-1 Q = s(H0)(1 - P_E0),
        s = h/g(E0),  h = (g(x) - g(E0))/(x - E0),
    and every polynomial in H0 applied to v is reduced modulo m, so G v is a
    combination of the Krylov vectors already in hand.  Everything descends
    from the over-complete word basis to the true state space because the true
    minimal polynomial relative to v divides m and is squarefree.

    Q drops the E0 eigencomponent, which is the model space and nothing else,
    by Casimir counting: an occupied link costs at least C_F/2 = 2/3, energies
    are half-Casimirs of SU(3) irreps, and the only gauge-invariant way to
    total 8/3 is four fundamental links closing into a 4-cycle -- a plaquette
    of the cluster, in one of its two orientations, whose colour contraction
    is unique.  The over-complete basis makes such a state appear inside
    bigger words (P.P antisymmetrised is Pbar; a Q Qbar bubble contains the
    vacuum), which is exactly what the projector removes.
    """
    if not vec:
        return {}
    KRYLOV_STATS["calls"] += 1
    K = [dict(vec)]
    index: dict = {}
    while True:
        nxt = apply_H0(K[-1])
        for w in nxt:
            index.setdefault(w, len(index))
        for kv in K:
            for w in kv:
                index.setdefault(w, len(index))
        k = len(K)
        n = len(index)
        aug = flint.fmpq_mat(n, k + 1)
        for i, kv in enumerate(K):
            for w, c in kv.items():
                aug[index[w], i] = fq(c)
        for w, c in nxt.items():
            aug[index[w], k] = fq(c)
        R, rank = aug.rref()
        pivots = []
        for i in range(rank):
            piv = next(j for j in range(k + 1) if R[i, j] != 0)
            pivots.append(piv)
        if k in pivots:
            K.append(nxt)  # independent: keep going
            continue
        # dependent: nxt = sum c_i K_i, with rank == k and pivots 0..k-1
        assert rank == k and pivots == list(range(k)), (rank, pivots)
        coeffs = [fr(R[i, k]) for i in range(k)]
        break
    KRYLOV_STATS["max_degree"] = max(KRYLOV_STATS["max_degree"], k)
    x = flint.fmpq_poly([0, 1])
    m = x**k - flint.fmpq_poly([fq(c) for c in coeffs])
    _, factors = m.factor()
    r = flint.fmpq_poly([1])
    for f, _mult in factors:
        r *= f
    E0 = fq(e0)
    lin = x - E0
    if r % lin == 0:
        g = r // lin
        E0_SEEN["with_e0"] += 1
    else:
        g = r
        E0_SEEN["without"] += 1
    gE0 = g(E0)
    assert gE0 != 0
    h = (g - gE0) // lin
    assert (g - gE0) % lin == 0
    one = flint.fmpq_poly([1])
    q = ((h / gE0) * (one - g / gE0)) % m
    qc = [fr(c) for c in q.coeffs()]
    out = defaultdict(F)
    for i, c in enumerate(qc):
        if c:
            for w, v in K[i].items():
                out[w] += c * v
    return {w: v for w, v in out.items() if v}


def haar_vec(word, vec):
    return sum((c * haar(word, w) for w, c in vec.items()), F(0))


# ----------------------------------------------------------------------------
# the cluster and its effective Hamiltonian
# ----------------------------------------------------------------------------
class Cluster:
    def __init__(self, faces):
        self.faces = faces
        self.words = []
        for pl, b in faces:
            self.words.append(plaquette(pl, b))
            self.words.append(plaquette(pl, b, conj=True))
        self.model = [{w: F(1)} for w in self.words]
        self.e0 = F(len(self.words[0].occ)) * M.CF / 2
        self.norm = [haar(w, w) for w in self.words]

    def V(self, vec):
        out = {}
        for w in self.words:
            out = vadd(out, word_mul(vec, w))
        return out

    def G(self, vec):
        return resolvent(vec, self.e0, self.words)

    def element(self, i, vec):
        """<d_i|vec> / sqrt(<d_i|d_i><d_j|d_j>) -- all norms are 1 for SU(3)."""
        return haar_vec(self.words[i], vec)

    def effective(self, ends, log=print):
        """The Hermitian H4 between two faces, on the model basis {P, Pbar, R, Rbar}.

        The assembly is the pinned engine's own (build_exact_endpoint_fourth_order_ledgers):
            H4 = D - A C1 - C1^T A - (K2 N + N K2)/2 + A A J
        with A = PVP (the SU(3) baryonic vertex, +-1 per C-sector), K2 = PVGVP,
        N = PVG^2VP, J = PVG^3VP, C1 = PVG^2VGVP, D = PVGVGVGVP.

        The two-insertion moments A, K2, N, J are taken on the whole model
        basis (their Haar families never exceed (2,2)).  C1 and D are taken only
        between the two endpoint faces: their diagonals would need the MIXED
        (4,1) and BALANCED (3,3) families, which the engine evaluates at
        seconds to minutes each, and no product in H4 between distinct faces
        ever reads a diagonal of C1 or D.
        """
        t0 = time.time()
        m = len(self.words)
        rng = range(m)
        fa, fb = ends
        ia, ib = (2 * fa, 2 * fa + 1), (2 * fb, 2 * fb + 1)
        vd = [self.V(d) for d in self.model]
        gv = [self.G(v) for v in vd]
        ggv = [self.G(x) for x in gv]
        gggv = [self.G(x) for x in ggv]
        A = [[self.element(i, vd[j]) for j in rng] for i in rng]
        K2 = [[self.element(i, self.V(gv[j])) for j in rng] for i in rng]
        N = [[self.element(i, self.V(ggv[j])) for j in rng] for i in rng]
        J = [[self.element(i, self.V(gggv[j])) for j in rng] for i in rng]
        log(f"    two-insertion moments: {time.time() - t0:.1f}s; krylov {KRYLOV_STATS}")
        for name, X in (("A", A), ("K2", K2), ("N", N), ("J", J)):
            assert all(X[i][j] == X[j][i] for i in rng for j in rng), f"{name} not symmetric"
        assert all(A[i][j] == (1 if (i // 2 == j // 2 and i != j) else 0) for i in rng for j in rng), (
            "PVP is not the baryonic vertex P <-> Pbar at unit weight"
        )
        if fa == fb:
            # a diagonal D needs the (3,3) family; only the second order is wanted here
            self.moments = {"A": A, "K2": K2, "N": N, "J": J}
            return K2, N, {}
        pairs = [(i, j) for i in ia for j in ib] + [(i, j) for i in ib for j in ia]
        C1 = defaultdict(F)
        D = defaultdict(F)
        for bras, kets in ((ia, ib), (ib, ia)):
            targets = {triality(self.words[i]) for i in bras}
            allow = [reachable(targets, self.words, k) for k in range(4)]
            for j in kets:
                s1 = filt(self.V(self.model[j]), allow[3])
                s2 = filt(self.V(self.G(s1)), allow[2])
                r2 = self.G(s2)
                vgr2 = filt(self.V(self.G(r2)), allow[0])
                s3 = filt(self.V(r2), allow[1])
                z = filt(self.V(self.G(s3)), allow[0])
                log(
                    f"      ket {j} -> bras {bras}: |s1|={len(s1)} |s2|={len(s2)} |r2|={len(r2)} "
                    f"|s3|={len(s3)} |z|={len(z)} krylov={KRYLOV_STATS} {time.time() - t0:.1f}s"
                )
                for i in bras:
                    C1[(i, j)] = self.element(i, vgr2)
                    D[(i, j)] = self.element(i, z)
        log(f"    endpoint moments: {time.time() - t0:.1f}s; haar {HAAR_CALLS}; E0 {E0_SEEN}")
        assert all(D[(i, j)] == D[(j, i)] for i, j in pairs), "D not symmetric"

        def conj(i):
            return i ^ 1

        H4 = {}
        for i, j in pairs:
            fold = sum(K2[i][k] * N[k][j] + N[i][k] * K2[k][j] for k in rng) / 2
            H4[(i, j)] = D[(i, j)] - C1[(conj(i), j)] - C1[(conj(j), i)] - fold + J[i][j]
        assert all(H4[(i, j)] == H4[(j, i)] for i, j in pairs), "H4 not symmetric"
        log(f"    fourth order between faces {fa} and {fb}: {time.time() - t0:.1f}s")
        self.moments = {"A": A, "K2": K2, "N": N, "J": J, "C1": dict(C1), "D": dict(D)}
        return K2, N, H4


def codd(Hm, i, j):
    a, b = 2 * i, 2 * j
    return (Hm[a][b] - Hm[a][b + 1] - Hm[a + 1][b] + Hm[a + 1][b + 1]) / 2


def ceven(Hm, i, j):
    a, b = 2 * i, 2 * j
    return (Hm[a][b] + Hm[a][b + 1] + Hm[a + 1][b] + Hm[a + 1][b + 1]) / 2


def two_insertion_moments(cl):
    """A, K2, N, J on the whole model basis of a cluster; families never exceed (2,2)."""
    m = len(cl.words)
    rng = range(m)
    vd = [cl.V(d) for d in cl.model]
    gv = [cl.G(v) for v in vd]
    ggv = [cl.G(x) for x in gv]
    gggv = [cl.G(x) for x in ggv]
    A = [[cl.element(i, vd[j]) for j in rng] for i in rng]
    K2 = [[cl.element(i, cl.V(gv[j])) for j in rng] for i in rng]
    N = [[cl.element(i, cl.V(ggv[j])) for j in rng] for i in rng]
    J = [[cl.element(i, cl.V(gggv[j])) for j in rng] for i in rng]
    for name, X in (("A", A), ("K2", K2), ("N", N), ("J", J)):
        assert all(X[i][j] == X[j][i] for i in rng for j in rng), f"{name} not symmetric"
    assert all(A[i][j] == (1 if (i // 2 == j // 2 and i != j) else 0) for i in rng for j in rng), (
        "PVP is not the baryonic vertex P <-> Pbar at unit weight"
    )
    return A, K2, N, J


def traversal(word):
    """link -> +1/-1: the direction a plaquette word traverses each of its links."""
    return {l: (1 if is_u else -1) for l, is_u in word.occ}


def incidence_sign(faces3, connector):
    """The product of the two signed shared-link incidences P~Q and Q~R.

    THM_FLUX Prop. 2's S_sq carries -1 on a shared link the two plaquettes
    traverse in opposite directions (coplanar neighbours) and +1 when they
    traverse it the same way; (S_sq^2)_{PR} through Q is the product.
    """
    words = [plaquette(pl, b) for pl, b in faces3]
    q = traversal(words[connector])
    sign = 1
    for k, w in enumerate(words):
        if k == connector:
            continue
        t = traversal(w)
        (shared,) = set(t) & set(q)
        sign *= t[shared] * q[shared]
    return sign


def chain_cumulant(faces3, connector, log=print):
    """W(P,Q,R) - W(P,R) on the P -> R block of the Hermitian H4, exactly.

    Every history that never inserts the connector Q is the same word, the
    same H0 evolution and the same Haar projection on both clusters, so it
    cancels in the cumulant.  Of the engine's assembly
        H4 = D - A C1 - C1^T A - (K2 N + N K2)/2 + A A J
    the A-terms and J between two link-disjoint faces need three or two
    insertions with net charge P Rbar, which no Q-touched history can supply,
    so they cancel too.  What survives is
        W3 - W2 = D_touched - (fold3 - fold2),
    D_touched the direct term over histories that insert Q at least once
    (the orderings of {Rbar, P, Q, Qbar} on |R>, whose Haar families never
    exceed (2,2)) and the folds from the two-insertion moments on each
    cluster, which are cheap on the whole model basis.
    """
    t0 = time.time()
    cl3 = Cluster(faces3)
    supports = [frozenset(l for l, _ in cl3.words[2 * k].occ) for k in range(len(faces3))]
    ends_k = [k for k in range(len(faces3)) if k != connector]
    assert all(len(supports[k] & supports[connector]) == 1 for k in ends_k), "Q must share exactly one link with each endpoint"
    assert not (supports[ends_k[0]] & supports[ends_k[1]]), "the endpoints must be link-disjoint"
    log(f"    links: {len(set().union(*supports))}, shared with Q: {[sorted(supports[k] & supports[connector]) for k in ends_k]}")
    faces2 = [f for k, f in enumerate(faces3) if k != connector]
    cl2 = Cluster(faces2)
    m3, m2 = len(cl3.words), len(cl2.words)
    _, K2_3, N_3, _ = two_insertion_moments(cl3)
    _, K2_2, N_2, _ = two_insertion_moments(cl2)
    log(f"    two-insertion moments on both clusters: {time.time() - t0:.1f}s; krylov {KRYLOV_STATS}")
    # face index maps: endpoints are faces 0 and 2 of the chain, 0 and 1 of the pair
    ends3 = [k for k in range(len(faces3)) if k != connector]
    w3 = {}  # (face, orientation) -> word index in cl3
    w2 = {}
    for slot, face in enumerate(ends3):
        for o in (0, 1):
            w3[(slot, o)] = 2 * face + o
            w2[(slot, o)] = 2 * slot + o
    # map cl2 word index -> cl3 word index (same word objects: same links)
    assert all(cl2.words[w2[k]] == cl3.words[w3[k]] for k in w3), "endpoint words differ between clusters"
    q_words = {cl3.words[2 * connector], cl3.words[2 * connector + 1]}

    def V_split(u, t):
        out_u, out_t = {}, {}
        for w in cl3.words:
            mu = word_mul(u, w)
            mt = word_mul(t, w)
            if w in q_words:
                out_t = vadd(out_t, mu)
            else:
                out_u = vadd(out_u, mu)
            out_t = vadd(out_t, mt)
        return out_u, out_t

    D_t = {}
    for bra_slot, ket_slot in ((0, 1), (1, 0)):
        bras = [w3[(bra_slot, o)] for o in (0, 1)]
        kets = [w3[(ket_slot, o)] for o in (0, 1)]
        targets = {triality(cl3.words[i]) for i in bras}
        allow = [reachable(targets, cl3.words, k) for k in range(4)]
        for j in kets:
            u, t = V_split(cl3.model[j], {})
            u, t = filt(u, allow[3]), filt(t, allow[3])
            u, t = cl3.G(u), cl3.G(t)
            u, t = V_split(u, t)
            u, t = filt(u, allow[2]), filt(t, allow[2])
            u, t = cl3.G(u), cl3.G(t)
            u, t = V_split(u, t)
            u, t = filt(u, allow[1]), filt(t, allow[1])
            u, t = cl3.G(u), cl3.G(t)
            _, t = V_split(u, t)
            t = filt(t, allow[0])
            log(
                f"      ket {j} -> bras {bras}: |z_touched|={len(t)} krylov={KRYLOV_STATS} "
                f"{time.time() - t0:.1f}s"
            )
            for i in bras:
                D_t[(i, j)] = cl3.element(i, t)
            log(f"      haar {HAAR_CALLS} {time.time() - t0:.1f}s")
    assert all(D_t[(i, j)] == D_t[(j, i)] for (i, j) in D_t), "D_touched not symmetric"

    def fold(K2, N, i, j, m):
        return sum(K2[i][k] * N[k][j] + N[i][k] * K2[k][j] for k in range(m)) / 2

    W = {}
    for oa in (0, 1):
        for ob in (0, 1):
            i3, j3 = w3[(0, oa)], w3[(1, ob)]
            i2, j2 = w2[(0, oa)], w2[(1, ob)]
            f3 = fold(K2_3, N_3, i3, j3, m3)
            f2 = fold(K2_2, N_2, i2, j2, m2)
            W[(oa, ob)] = D_t[(i3, j3)] - (f3 - f2)
            log(f"      W[{oa}{ob}] = {W[(oa, ob)]}   (D_touched {D_t[(i3, j3)]}, fold3-fold2 {f3 - f2})")
    u_odd = (W[(0, 0)] - W[(0, 1)] - W[(1, 0)] + W[(1, 1)]) / 2
    u_even = (W[(0, 0)] + W[(0, 1)] + W[(1, 0)] + W[(1, 1)]) / 2
    log(f"    chain cumulant done in {time.time() - t0:.1f}s")
    return u_odd, u_even, W


# ----------------------------------------------------------------------------
# clusters
# ----------------------------------------------------------------------------
XY = (0, 1)
XZ = (0, 2)
CLUSTERS = {
    "single": [(XY, (0, 0, 0))],
    "coplanar_pair": [(XY, (0, 0, 0)), (XY, (1, 0, 0))],
    "perpendicular_pair": [(XY, (0, 0, 0)), (XZ, (0, 0, 0))],
    "disjoint_pair": [(XY, (0, 0, 0)), (XY, (2, 0, 0))],
    # P, Q, R in one plane, Q sharing one link with each endpoint
    "coplanar_chain": [(XY, (0, 0, 0)), (XY, (1, 0, 0)), (XY, (2, 0, 0))],
    # P and Q coplanar (share the x-link at x=1), R perpendicular to Q,
    # sharing Q's far vertical link.  P and R are link-disjoint.
    "bent_chain": [(XY, (0, 0, 0)), (XY, (1, 0, 0)), ((1, 2), (2, 0, 0))],
    "bent_pair": [(XY, (0, 0, 0)), ((1, 2), (2, 0, 0))],
    # P and R both perpendicular to Q, on opposite links of Q, opposite sides
    # P and R both perpendicular to Q, on opposite links of Q, and to each
    # other: P is the xz-face on Q's x-link at the origin, R the yz-face
    # hanging below Q's far y-link, so that P and R share no link.
    "zigzag_chain": [(XZ, (0, 0, 0)), (XY, (0, 0, 0)), ((1, 2), (1, 0, -1))],
}


def check_links(name):
    words = Cluster(CLUSTERS[name]).words
    supports = [frozenset(l for l, _ in w.occ) for w in words[::2]]
    return supports


ENDS = {"single": (0, 0), "coplanar_pair": (0, 0), "perpendicular_pair": (0, 0), "disjoint_pair": (0, 0)}


def run(names, log=print):
    results = {}
    for name in names:
        t0 = time.time()
        log(f"== {name}")
        cl = Cluster(CLUSTERS[name])
        ends = ENDS.get(name, (0, len(CLUSTERS[name]) - 1))
        H2, VR2V, H4 = cl.effective(ends, log)
        results[name] = (cl, H2, VR2V, H4)
        log(f"   done in {time.time() - t0:.1f}s")
    return results


def main(argv):
    which = argv[1] if len(argv) > 1 else "all"
    log = print
    t_all = time.time()
    # --- second order, the register's own numbers ---
    res = run(["single", "coplanar_pair", "perpendicular_pair", "disjoint_pair"], log)
    _, H2s, _, _ = res["single"]
    _, H2c, _, _ = res["coplanar_pair"]
    _, H2p, _, _ = res["perpendicular_pair"]
    _, H2d, _, _ = res["disjoint_pair"]
    log("")
    log("second order (register: t_3 = 5/612, T_PLUS_2 = -11/306, LEAK_2 = -11/306, bubble -3/4)")
    log(f"  single-plaquette C-odd diagonal           = {codd(H2s, 0, 0)}")
    log(f"  single-plaquette C-even diagonal          = {ceven(H2s, 0, 0)}")
    log(f"  coplanar shared-link C-odd hop            = {codd(H2c, 0, 1)}")
    log(f"  perpendicular shared-link C-odd hop       = {codd(H2p, 0, 1)}")
    log(f"  shared-link C-even hop (coplanar)         = {ceven(H2c, 0, 1)}")
    log(f"  shared-link C-even hop (perpendicular)    = {ceven(H2p, 0, 1)}")
    log(f"  C-odd leakage per shared-link neighbour   = {codd(H2c, 0, 0) - codd(H2s, 0, 0)}")
    log(f"  C-odd leakage per disjoint neighbour      = {codd(H2d, 0, 0) - codd(H2s, 0, 0)}")
    log(f"  disjoint-pair C-odd hop                   = {codd(H2d, 0, 1)}")
    log(f"  disjoint-pair C-even hop                  = {ceven(H2d, 0, 1)}")
    if which == "second":
        return
    # --- fourth order: the chain cumulant ---
    log("")
    log("fourth order: chain cumulant W(P,Q,R) - W(P,R) on the P -> R element")
    chains = ["coplanar_chain", "bent_chain", "zigzag_chain"]
    if which != "all":
        chains = [c for c in chains if c == which]
    out = {}
    for chain in chains:
        log(f"== {chain}: faces {CLUSTERS[chain]}")
        u_odd, u_even, W = chain_cumulant(CLUSTERS[chain], 1, log)
        sign = incidence_sign(CLUSTERS[chain], 1)
        out[chain] = (u_odd, u_even, sign)
        log(f"  {chain}: (S_sq^2)_PR incidence sign through Q = {sign:+d}")
        log(f"  {chain}: C-odd chain amplitude          = {u_odd} = {float(u_odd):.9e}")
        log(f"  {chain}: C-odd amplitude / incidence sign  u = {u_odd * sign}")
        log(f"  {chain}: C-even chain amplitude         = {u_even} = {float(u_even):.9e}")
        log(f"  {chain}: u / X_QUANTUM = {u_odd * sign / X_QUANTUM}")
    cert = {
        "schema": "workhouse/chain-amplitude/v1",
        "engine": "corpus-import/programs/hodge_o4_adjudication/src/DATA_SU3_Exact_MarkedCluster_m4_Colab.py",
        "engine_used_for": ["trace_state", "tensor_product", "simplify_unitarity", "h0_action", "haar_inner", "CF"],
        "second_order": {
            "single_codd_diagonal": str(codd(H2s, 0, 0)),
            "single_ceven_diagonal": str(ceven(H2s, 0, 0)),
            "coplanar_shared_link_codd_hop": str(codd(H2c, 0, 1)),
            "perpendicular_shared_link_codd_hop": str(codd(H2p, 0, 1)),
            "shared_link_ceven_hop_coplanar": str(ceven(H2c, 0, 1)),
            "shared_link_ceven_hop_perpendicular": str(ceven(H2p, 0, 1)),
            "codd_leakage_per_shared_link_neighbour": str(codd(H2c, 0, 0) - codd(H2s, 0, 0)),
            "codd_leakage_per_disjoint_neighbour": str(codd(H2d, 0, 0) - codd(H2s, 0, 0)),
            "disjoint_pair_codd_hop": str(codd(H2d, 0, 1)),
        },
        "chains": {
            name: {
                "faces": [[list(pl), list(b)] for pl, b in CLUSTERS[name]],
                "connector": 1,
                "incidence_sign": s,
                "codd_chain_amplitude": str(uo),
                "u": str(uo * s),
                "ceven_chain_amplitude": str(ue),
            }
            for name, (uo, ue, s) in out.items()
        },
        "haar_calls": dict(HAAR_CALLS),
        "krylov": dict(KRYLOV_STATS),
        "seconds": round(time.time() - t_all, 1),
    }
    with open(HERE / "chain_amplitude_certificate.json", "w", encoding="utf-8") as fh:
        json.dump(cert, fh, indent=2)
        fh.write("\n")
    log("certificate written: chain_amplitude_certificate.json")
    log("")
    log(f"X_QUANTUM (historical exact kernel) = {X_QUANTUM} = {float(X_QUANTUM):.9e}")
    log(f"cold v10a.26 value                  = {COLD_SCALE} * X_QUANTUM = {COLD_SCALE * float(X_QUANTUM):.9e}")
    log(f"haar calls: {HAAR_CALLS}; krylov {KRYLOV_STATS}; E0 {E0_SEEN}; total {time.time() - t_all:.1f}s")
    return out


if __name__ == "__main__":
    main(sys.argv)
