# ============================================================================
# HODGE v10a — PHYSICAL-Q QUOTIENT / Q-DYNAMICS CERTIFICATE ENGINE
# ============================================================================
# Self-contained Colab/A100 block distilled from the validated v5 -> v8 -> v9.1
# solver chain.  Historical production drivers are removed.
#
# v10a scope in this artifact:
#   1. Reconstruct explicit orthonormal physical Q coordinates from every
#      globally merged joint-Casimir Gram block.
#   2. Prove B B^T = K_lambda and explicit P+Q == v8 Schur/Feshbach when W_QQ=0.
#   3. Build the full magnetic W_QQ matrix on the one-step K=0 glueball Q range
#      using the generalized v9.1 Haar endpoint contractor.
#   4. Audit the full three-component T1 source Gram/orientation equivalence.
#   5. Recompute the linked string cubic process with manual cubic injection OFF,
#      and decompose it into PP, PQ+QP, and QQ pieces.
#   6. Census the source-bright Q1 -> Q2 layer required for the true O(u^4)
#      scalar/rest calculation.
#
# Deliberate hard stop:
#   This file DOES NOT report a physical m4_rest or C3_full^shp.  Those require
#   the newly exposed Q2 resolvent plus linked/folded marked-cluster subtraction.
#   The protected fourth-order theorem values are printed as future firewalls,
#   not passed by assertion against an operator that has not yet been built.
# ============================================================================

import math
import time
import os
import itertools
from collections import Counter, defaultdict, deque
from dataclasses import dataclass
from fractions import Fraction
from functools import lru_cache

import numpy as np
import sympy as sp
from scipy.linalg import eigh_tridiagonal
from scipy.linalg import eigh
from scipy.sparse import coo_matrix, csr_matrix, diags

# =============================================================================
# CONFIG
# =============================================================================
N = 3
L = int(os.environ.get("GLUE_L", "3"))
GLUE_DEPTHS = tuple(int(x) for x in os.environ.get("GLUE_DEPTHS", "1,2").split(",") if x.strip())
MAX_K = max(GLUE_DEPTHS)
Y_VALUES = tuple(float(x) for x in os.environ.get("U_VALUES", "0.02,0.05,0.10,0.20,0.30").split(",") if x.strip())
POLARIZATION = (0, 1)
STRING_LENGTHS = tuple(int(x) for x in os.environ.get("STRING_LENGTHS", "3,4,5,6,7").split(",") if x.strip())
STRING_DEPTHS = tuple(int(x) for x in os.environ.get("STRING_DEPTHS", "1,2").split(",") if x.strip())

PREFER_GPU = os.environ.get("PREFER_GPU", "1") != "0"
MAX_LANCZOS = int(os.environ.get("MAX_LANCZOS", "112"))
RITZ_TOL = float(os.environ.get("RITZ_TOL", "2e-10"))
ENERGY_STABILITY_TOL = float(os.environ.get("ENERGY_STABILITY_TOL", "2e-11"))
RESIDUE_STABILITY_TOL = float(os.environ.get("RESIDUE_STABILITY_TOL", "2e-10"))
STABLE_CHECKS_REQUIRED = 2

CF = (N * N - 1) / (2 * N)
E0_PLAQ = 2 * CF
T3_TARGET = 5.0 / 612.0

# Exact SU(3) local Casimirs and one-link decomposition weights.
C_BAR3 = 4.0 / 3.0
C_6 = 10.0 / 3.0
C_8 = 3.0
W_A = 1.0 / 3.0
W_S = 2.0 / 3.0
W_1 = 1.0 / 9.0
W_8 = 8.0 / 9.0
D_A = CF + 0.5 * C_BAR3
D_S = CF + 0.5 * C_6
D_1 = CF
D_8 = CF + 0.5 * C_8
E_SEXTET_PLAQ = 2.0 * C_6

# =============================================================================
# OPTIONAL CUDA BACKEND FOR LANCZOS
# =============================================================================
USE_GPU = False
cp = None
cpsparse = None

if PREFER_GPU:
    try:
        import cupy as _cp
        import cupyx.scipy.sparse as _cpsparse
        if int(_cp.cuda.runtime.getDeviceCount()) > 0:
            cp = _cp
            cpsparse = _cpsparse
            USE_GPU = True
    except Exception:
        USE_GPU = False

xp = cp if USE_GPU else np
DEVICE = "CUDA/CuPy" if USE_GPU else "CPU/NumPy"

# =============================================================================
# GATES
# =============================================================================
gates = []

def gate(name, ok, detail=""):
    ok = bool(ok)
    gates.append((name, ok, str(detail)))
    print(("[PASS] " if ok else "[FAIL] ") + name + (f" :: {detail}" if detail else ""))

# =============================================================================
# CUBIC CELL COMPLEX
# =============================================================================
def shift(v, d, step=1):
    w = list(v)
    w[d] = (w[d] + step) % L
    return tuple(w)


def build_cubic_complex():
    verts = [(x, y, z) for x in range(L) for y in range(L) for z in range(L)]

    links = []
    lid = {}
    for v in verts:
        for d in range(3):
            lid[(v, d)] = len(links)
            links.append((v, d))

    faces = []
    for v in verts:
        for a, b in ((0, 1), (0, 2), (1, 2)):
            faces.append((v, a, b))

    B2 = np.zeros((len(links), len(faces)), dtype=np.int8)
    for f, (v, a, b) in enumerate(faces):
        va = shift(v, a)
        vb = shift(v, b)
        B2[lid[(v, a)], f] += 1
        B2[lid[(va, b)], f] += 1
        B2[lid[(vb, a)], f] -= 1
        B2[lid[(v, b)], f] -= 1

    return verts, links, faces, B2


verts, links, faces, B2 = build_cubic_complex()
E, P = B2.shape

link_faces = [[] for _ in range(E)]
for f in range(P):
    for l in np.flatnonzero(B2[:, f]):
        link_faces[int(l)].append(f)
face_support_faces = []
for f in range(P):
    ff = set()
    for l in np.flatnonzero(B2[:, f]):
        ff.update(link_faces[int(l)])
    face_support_faces.append(frozenset(ff))

source_faces = [
    f for f, (_, a, b) in enumerate(faces)
    if (a, b) == POLARIZATION
]

# =============================================================================
# C-ODD GRAPH ALGEBRA
# =============================================================================
def canonical_codd(q):
    q = np.asarray(q, dtype=np.int8)
    a = q.tobytes()
    b = (-q).tobytes()
    if a <= b:
        return a, +1, q.copy()
    return b, -1, (-q).copy()


def canonical_pair_codd(q, b):
    """Canonical unordered two-trace product under global charge conjugation."""
    q = np.asarray(q, dtype=np.int8)
    b = np.asarray(b, dtype=np.int8)
    pair = tuple(sorted((q.tobytes(), b.tobytes())))
    pair_c = tuple(sorted(((-q).tobytes(), (-b).tobytes())))
    if pair <= pair_c:
        return pair, +1
    return pair_c, -1


def is_simple_single_loop(q):
    support = np.flatnonzero(q)
    if len(support) < 4:
        return False

    outgoing = {}
    indegree = Counter()
    used = set()

    for li in support:
        l = int(li)
        v, d = links[l]
        w = shift(v, d)
        if q[l] > 0:
            src, dst = v, w
        else:
            src, dst = w, v
        if src in outgoing:
            return False
        outgoing[src] = dst
        indegree[dst] += 1
        used.add(src)
        used.add(dst)

    if any(v not in outgoing or indegree[v] != 1 for v in used):
        return False

    start = next(iter(used))
    cur = start
    seen = set()
    while cur not in seen:
        seen.add(cur)
        cur = outgoing[cur]

    return cur == start and len(seen) == len(used)


def candidate_faces(q):
    out = set()
    for l in np.flatnonzero(q):
        out.update(link_faces[int(l)])
    return out


def candidate_face_count_from_support(*arrays):
    out = set()
    support = np.zeros(E, dtype=bool)
    for a in arrays:
        support |= (np.asarray(a) != 0)
    for l in np.flatnonzero(support):
        out.update(link_faces[int(l)])
    return len(out)


def plaquette_match(q):
    for f in range(P):
        if np.array_equal(q, B2[:, f]):
            return f, +1
        if np.array_equal(q, -B2[:, f]):
            return f, -1
    return None

# =============================================================================
# EXACT LOCAL MULTI-LINK HAAR/FIERZ CLOSURE
# =============================================================================
# A plaquette can share 2 or 3 links with an already-deformed loop.  v3 counted
# these events but skipped them.  Here each distinct two-trace overlap topology
# is solved exactly once using the SU(3) Haar Gram metric and Fierz-generated H0.
# The resulting spectral measure is compressed to one "bright" Q channel per
# electric eigenvalue.  This is exact for the local action's spectral measure.
# Dark vectors in a degenerate eigenspace never couple to that parent action.
#
# Remaining limitation after v4: bright channels generated by DIFFERENT raw
# two-trace products are not globally Gram-merged if their recoupled closures
# overlap.  v4 therefore closes the explicit skipped local self-energy channels
# without claiming the final all-Q global Gram quotient.

def lx_canon(labels):
    mp = {}
    out = []
    for x in labels:
        if x not in mp:
            mp[x] = len(mp)
        out.append(mp[x])
    return tuple(out)

@dataclass(frozen=True)
class LXState:
    occ: tuple
    part: tuple


def lx_trace_state(steps):
    m = len(steps)
    occ, labels = [], []
    for j, (link, d) in enumerate(steps):
        a, b = j, (j + 1) % m
        if int(d) > 0:
            occ.append((int(link), True))
            labels.extend((a, b))
        else:
            occ.append((int(link), False))
            labels.extend((b, a))
    return LXState(tuple(occ), lx_canon(labels))


def lx_tensor_product(a, b):
    off = (max(a.part) + 1) if a.part else 0
    return LXState(a.occ + b.occ, lx_canon(a.part + tuple(x + off for x in b.part)))


def lx_classes(part):
    out = defaultdict(list)
    for i, c in enumerate(part):
        out[c].append(i)
    return out


def lx_merge_classes(part, pairs):
    n = len(part)
    parent = list(range(n))
    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x
    def union(a, b):
        a, b = find(a), find(b)
        if a != b:
            parent[b] = a
    first = {}
    for i, c in enumerate(part):
        if c in first:
            union(i, first[c])
        else:
            first[c] = i
    for a, b in pairs:
        union(int(a), int(b))
    return lx_canon([find(i) for i in range(n)])


def lx_swap_rows(part, r1, r2):
    if part[r1] == part[r2]:
        return part
    z = list(part)
    z[r1], z[r2] = z[r2], z[r1]
    return lx_canon(z)


def lx_opposite_reconnect(part, r1, r2):
    n = len(part)
    cls = lx_classes(part)
    c1, c2 = part[r1], part[r2]
    parent = list(range(n))
    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x
    def union(a, b):
        a, b = find(a), find(b)
        if a != b:
            parent[b] = a
    for members in cls.values():
        rem = [x for x in members if x not in (r1, r2)]
        for x in rem[1:]:
            union(rem[0], x)
    rem1 = [x for x in cls[c1] if x not in (r1, r2)]
    rem2 = [x for x in cls[c2] if x not in (r1, r2)]
    if rem1 and rem2:
        union(rem1[0], rem2[0])
    union(r1, r2)
    return lx_canon([find(i) for i in range(n)])


def lx_remove_pair(state, i, j, merge_slots):
    part = lx_merge_classes(state.part, [merge_slots])
    removed = {2*i, 2*i+1, 2*j, 2*j+1}
    keep = [k for k in range(len(part)) if k not in removed]
    keep_classes = {part[k] for k in keep}
    lost = len(set(part) - keep_classes)
    scalar = Fraction(N ** max(0, lost - 1), 1)
    new_occ = tuple(o for k, o in enumerate(state.occ) if k not in (i, j))
    new_part = lx_canon([part[k] for k in keep])
    return scalar, LXState(new_occ, new_part)


def lx_simplify_unitarity(state):
    s = state
    scalar = Fraction(1)
    changed = True
    while changed:
        changed = False
        cls = lx_classes(s.part)
        bylink = defaultdict(list)
        for i, (link, typ) in enumerate(s.occ):
            bylink[link].append((i, typ))
        for _, items in bylink.items():
            done = False
            for (i, t1), (j, t2) in itertools.combinations(items, 2):
                if t1 == t2:
                    continue
                r1, c1 = 2*i, 2*i+1
                r2, c2 = 2*j, 2*j+1
                if set(cls[s.part[r1]]) == {r1, r2}:
                    fac, s = lx_remove_pair(s, i, j, (c1, c2))
                    scalar *= fac
                    changed = done = True
                    break
                if set(cls[s.part[c1]]) == {c1, c2}:
                    fac, s = lx_remove_pair(s, i, j, (r1, r2))
                    scalar *= fac
                    changed = done = True
                    break
            if done:
                break
    return scalar, s


def lx_H0_action(state):
    fac0, s = lx_simplify_unitarity(state)
    out = defaultdict(Fraction)
    out[s] += fac0 * Fraction(len(s.occ), 1) * Fraction(2, 3)
    bylink = defaultdict(list)
    for i, (link, typ) in enumerate(s.occ):
        bylink[link].append((i, typ))
    for _, items in bylink.items():
        for (i, t1), (j, t2) in itertools.combinations(items, 2):
            r1, r2 = 2*i, 2*j
            if t1 == t2:
                raw = LXState(s.occ, lx_swap_rows(s.part, r1, r2))
                fac, z = lx_simplify_unitarity(raw)
                out[z] += fac0 * fac * Fraction(1, 2)
                out[s] -= fac0 * Fraction(1, 2*N)
            else:
                raw = LXState(s.occ, lx_opposite_reconnect(s.part, r1, r2))
                fac, z = lx_simplify_unitarity(raw)
                out[z] -= fac0 * fac * Fraction(1, 2)
                out[s] += fac0 * Fraction(1, 2*N)
    return {z: c for z, c in out.items() if c}


def lx_pinv(p):
    out = [0] * len(p)
    for i, j in enumerate(p):
        out[j] = i
    return tuple(out)

def lx_pcompose(p, q):
    return tuple(p[q[i]] for i in range(len(p)))
def lx_pcycles(p):
    seen = [False] * len(p)
    c = 0
    for i in range(len(p)):
        if not seen[i]:
            c += 1
            j = i
            while not seen[j]:
                seen[j] = True
                j = p[j]
    return c

@lru_cache(None)
def lx_wg_fixed(k):
    ps = list(itertools.permutations(range(k)))
    G = sp.Matrix([
        [sp.Integer(N) ** lx_pcycles(lx_pcompose(lx_pinv(a), b)) for b in ps]
        for a in ps
    ])
    W = G.inv()
    WW = [[Fraction(int(sp.numer(W[i, j])), int(sp.denom(W[i, j]))) for j in range(len(ps))] for i in range(len(ps))]
    return ps, WW


def lx_combine_bra_ket(a, b):
    bra_occ = tuple((link, not typ) for link, typ in a.occ)
    off = (max(a.part) + 1) if a.part else 0
    return bra_occ + b.occ, lx_canon(a.part + tuple(x + off for x in b.part))

_LX_HAAR = {}
def lx_haar_inner(a, b):
    key = (a, b)
    if key in _LX_HAAR:
        return _LX_HAAR[key]
    occ, part = lx_combine_bra_ket(a, b)
    bylink = defaultdict(lambda: {True: [], False: []})
    for i, (link, typ) in enumerate(occ):
        bylink[link][typ].append(i)
    states = {part: Fraction(1)}
    for _, g in bylink.items():
        U, B = g[True], g[False]
        new = defaultdict(Fraction)
        if len(U) == len(B):
            k = len(U)
            if k > 2:
                raise RuntimeError(f"multi-link local closure unexpectedly needs balanced Haar k={k}>2")
            ps, W = lx_wg_fixed(k)
            for st, c0 in states.items():
                for si, sigma in enumerate(ps):
                    for ti, tau in enumerate(ps):
                        pairs = []
                        for r in range(k):
                            pairs.append((2*U[r], 2*B[sigma[r]]))
                            pairs.append((2*U[r]+1, 2*B[tau[r]]+1))
                        new[lx_merge_classes(st, pairs)] += c0 * W[si][ti]
        elif (len(U), len(B)) in ((3, 0), (0, 3)):
            # Exact SU(3) determinant primitive:
            #   int UUU = (1/6) eps(rows) eps(cols)
            # and eps eps = sum_perm sign(perm) prod delta(row_r,col_perm(r)).
            items = U if len(U) == 3 else B
            for st, c0 in states.items():
                for perm in itertools.permutations(range(3)):
                    inv = sum(perm[i] > perm[j] for i in range(3) for j in range(i+1, 3))
                    coeff = Fraction(-1 if inv % 2 else 1, 6)
                    pairs = [(2*items[r], 2*items[perm[r]]+1) for r in range(3)]
                    new[lx_merge_classes(st, pairs)] += c0 * coeff
        else:
            # No SU(3) singlet exists unless the U-Ubar imbalance is divisible by 3.
            # Cross overlaps encountered here have at most three total occurrences,
            # so the only non-balanced nonzero case is the pure epsilon primitive above.
            _LX_HAAR[key] = Fraction(0)
            return Fraction(0)
        states = {st: c for st, c in new.items() if c}
    total = sum((c * N ** len(set(st)) for st, c in states.items()), Fraction(0))
    _LX_HAAR[key] = total
    return total


def lx_closure(seed_state, max_states=64):
    fac, s = lx_simplify_unitarity(seed_state)
    if fac != 1:
        raise RuntimeError(f"unexpected scalar {fac} on local closure seed")
    states = [s]
    seen = {s}
    q = deque([s])
    while q:
        x = q.popleft()
        for y in lx_H0_action(x):
            if y not in seen:
                seen.add(y)
                states.append(y)
                q.append(y)
                if len(states) > max_states:
                    raise RuntimeError("multi-link local H0 closure exceeded expected size")
    return states


def lx_spectral_measure(seed_state):
    basis = lx_closure(seed_state)
    idx = {s: i for i, s in enumerate(basis)}
    m = len(basis)
    A = sp.zeros(m)
    for j, s in enumerate(basis):
        for z, c in lx_H0_action(s).items():
            A[idx[z], j] += sp.Rational(c.numerator, c.denominator)
    G = sp.zeros(m)
    for i in range(m):
        for j in range(i, m):
            v = lx_haar_inner(basis[i], basis[j])
            G[i, j] = G[j, i] = sp.Rational(v.numerator, v.denominator)
    piv = list(G.rref()[1])
    Gp = G.extract(piv, piv)
    Hmetric = (G * A).extract(piv, piv)
    H = sp.simplify(Gp.inv() * Hmetric)
    v = sp.Matrix([G[i, 0] for i in piv])
    c = sp.simplify(Gp.inv() * v)
    norm = sp.factor((c.T * Gp * c)[0])
    out = []
    for lam in sorted(H.eigenvals(), key=lambda x: float(x)):
        Z = sp.Matrix.hstack(*(H - lam*sp.eye(H.rows)).nullspace())
        Pm = sp.simplify(Z * (Z.T*Gp*Z).inv() * Z.T * Gp)
        cc = sp.simplify(Pm * c)
        w = sp.factor((cc.T * Gp * cc)[0])
        if w != 0:
            out.append((lam, w))
    return norm, out, len(basis), len(piv)


def ordered_loop_steps(q, links_obj, shift_fn):
    out = {}
    for li in np.flatnonzero(q):
        li = int(li)
        v, d = links_obj[li]
        w = shift_fn(v, d)
        src, dst = (v, w) if q[li] > 0 else (w, v)
        out[src] = (dst, li, int(q[li]))
    if not out:
        raise RuntimeError("empty loop")
    start = min(out)
    cur = start
    steps = []
    while True:
        dst, li, sg = out[cur]
        steps.append((li, sg))
        cur = dst
        if cur == start:
            return steps
        if len(steps) > len(out) + 1:
            raise RuntimeError("loop ordering failed")


def face_steps_generic(face_id, s, faces_obj, lid_obj, shift_fn):
    v, a, b = faces_obj[face_id]
    va = shift_fn(v, a)
    vb = shift_fn(v, b)
    steps = [
        (lid_obj[(v, a)], +1),
        (lid_obj[(va, b)], +1),
        (lid_obj[(vb, a)], -1),
        (lid_obj[(v, b)], -1),
    ]
    # Conjugating a Wilson trace reverses matrix order as well as daggering
    # each factor: Tr(ABCD)^* = Tr(D^dag C^dag B^dag A^dag).
    if int(s) < 0:
        steps = [(l, -d) for l, d in reversed(steps)]
    return steps


def local_topology_signature(parent_steps, pface_steps):
    p = len(parent_steps)
    pmap = {l: (i, sg) for i, (l, sg) in enumerate(parent_steps)}
    triples = []
    for j, (l, sg2) in enumerate(pface_steps):
        if l in pmap:
            i, sg1 = pmap[l]
            triples.append((i, j, sg1 * sg2))
    cands = []
    for rp in range(p):
        for rf in range(4):
            cands.append(tuple(sorted((((i-rp) % p, (j-rf) % 4, r) for i, j, r in triples))))
            cands.append(tuple(sorted((((-i-rp) % p, (-j-rf) % 4, r) for i, j, r in triples))))
    return (p, min(cands))


def mod3_reduce_flux(z):
    z = np.asarray(z, dtype=np.int16)
    r = z.copy()
    r[r == 2] = -1
    r[r == -2] = +1
    if np.any(np.abs(r) > 1):
        # Current P+plaquette actions never exceed +/-2.  Refuse silently wrong
        # determinant reduction if a deeper truncation changes that fact.
        raise RuntimeError("mod-3 residue exceeded square-free representative range")
    return r.astype(np.int8)


def exact_multilink_spectrum(parent_steps, pface_steps, cache):
    sig = local_topology_signature(parent_steps, pface_steps)
    if sig not in cache:
        raw = lx_tensor_product(lx_trace_state(parent_steps), lx_trace_state(pface_steps))
        norm, spec, closure_dim, gram_rank = lx_spectral_measure(raw)
        if norm != 1:
            raise RuntimeError(f"multi-link raw trace network norm is {norm}, expected 1")
        if sp.simplify(sum(w for _, w in spec) - 1) != 0:
            raise RuntimeError("multi-link spectral weights do not sum to one")
        cache[sig] = {
            "spec": [(lam, w) for lam, w in spec],
            "closure_dim": closure_dim,
            "gram_rank": gram_rank,
        }
    return sig, cache[sig]


def exact_residue_overlap(parent_steps, pface_steps, residue_steps, sig, cache):
    key = (sig, len(residue_steps))
    if key not in cache:
        raw = lx_tensor_product(lx_trace_state(parent_steps), lx_trace_state(pface_steps))
        rr = lx_trace_state(residue_steps)
        cache[key] = lx_haar_inner(rr, raw)
    return cache[key]

GLOBAL_ML_SPEC_CACHE = {}
GLOBAL_ML_OVERLAP_CACHE = {}

# =============================================================================
# SQUARE-FREE P BASIS
# =============================================================================
def build_graph_basis(max_depth):
    states = {}
    depth = {}
    queue = deque()
    source_terms = []

    for f in source_faces:
        key, sign, rep = canonical_codd(B2[:, f])
        if key not in states:
            states[key] = rep
            depth[key] = 0
            queue.append(key)
        source_terms.append((key, sign))

    while queue:
        key = queue.popleft()
        d = depth[key]
        if d >= max_depth:
            continue

        q = states[key]
        for f in candidate_faces(q):
            bf = B2[:, f]
            for s in (-1, +1):
                z = q + s * bf
                if np.max(np.abs(z)) > 1:
                    continue
                if not is_simple_single_loop(z):
                    continue
                key2, _, rep2 = canonical_codd(z)
                if key2 not in states:
                    states[key2] = rep2
                    depth[key2] = d + 1
                    queue.append(key2)

    keys = list(states)
    index = {k: i for i, k in enumerate(keys)}
    reps = [states[k] for k in keys]

    source = np.zeros(len(keys), dtype=np.float64)
    for key, sign in source_terms:
        source[index[key]] += sign / math.sqrt(len(source_terms))

    if abs(np.dot(source, source) - 1.0) > 1e-12:
        raise RuntimeError("source normalization failed")

    return keys, reps, depth, index, source

# =============================================================================
# CHANNEL-ENRICHED P + Q HAMILTONIAN
# =============================================================================
def build_enriched_model(max_depth):
    t0 = time.time()
    keys, states, depth, index, source = build_graph_basis(max_depth)
    nP = len(states)
    E_P = np.asarray([0.5 * int(np.count_nonzero(q)) * CF for q in states], dtype=np.float64)
    VAC_P = np.asarray([len(candidate_faces(q)) for q in states], dtype=np.float64)

    pp_rows, pp_cols, pp_vals = [], [], []
    p_diag = np.zeros(nP, dtype=np.float64)
    q_index, q_energy, q_type, q_vac_count = {}, [], [], []
    pq_rows, pq_cols, pq_vals = [], [], []
    ml_spec_cache, ml_overlap_cache = GLOBAL_ML_SPEC_CACHE, GLOBAL_ML_OVERLAP_CACHE
    model_topologies = set()
    multi_actions = 0
    multi_channels = 0
    sameface_handled = 0

    lid_global = {(v, d): i for i, (v, d) in enumerate(links)}

    def get_q(key, energy, typ, vac_count):
        if key in q_index:
            j = q_index[key]
            if abs(q_energy[j] - energy) > 1e-10:
                raise RuntimeError(f"inconsistent Q energy for {typ}: {q_energy[j]} vs {energy}")
            if abs(q_vac_count[j] - vac_count) > 1e-10:
                raise RuntimeError(f"inconsistent Q vacuum support for {typ}")
            return j
        j = len(q_energy)
        q_index[key] = j
        q_energy.append(float(energy))
        q_type.append(str(typ))
        q_vac_count.append(float(vac_count))
        return j

    for i, q in enumerate(states):
        perimeter = int(np.count_nonzero(q))
        E_parent = E_P[i]
        parent_steps = ordered_loop_steps(q, links, shift)
        cand_q = candidate_faces(q)

        # Exact SU(3) same-plaquette C- determinant identity.  The four-shared-
        # link action is represented here and must not be added a second time by
        # the generic multi-link closure.
        pm = plaquette_match(q) if perimeter == 4 else None
        if pm is not None:
            p_diag[i] += 1.0
            qkey = ("sextet_plaquette", canonical_codd(q)[0])
            j = get_q(qkey, E_SEXTET_PLAQ, "sextet_plaquette", int(VAC_P[i]))
            pq_rows.append(i); pq_cols.append(j); pq_vals.append(-1.0)

        for f in cand_q:
            bf = B2[:, f]
            vac_union_fast = len(cand_q | face_support_faces[f])
            shared0 = np.flatnonzero((q != 0) & (bf != 0))
            for s in (-1, +1):
                b = (s * bf).astype(np.int8)
                z = q + b
                shared = shared0
                relation = [int(q[l]) * int(b[l]) for l in shared]
                retained_loop = np.max(np.abs(z)) <= 1 and is_simple_single_loop(z)

                if len(shared) == 4 and pm is not None and f == pm[0]:
                    sameface_handled += 1
                    continue

                # One-shared-link certified representation channels (v3).
                if len(shared) == 1:
                    l = int(shared[0])
                    rel = int(q[l]) * int(b[l])
                    pair_key, q_codd_sign = canonical_pair_codd(q, b)
                    vac_union = vac_union_fast

                    if retained_loop:
                        key2, codd_sign, _ = canonical_codd(z)
                        j = index.get(key2)
                        if j is not None and j != i:
                            pp_rows.append(i); pp_cols.append(j); pp_vals.append(-codd_sign / N)

                    if rel > 0:
                        for typ, weight, delta in (("like_bar3", W_A, D_A), ("like_6", W_S, D_S)):
                            j = get_q((typ, pair_key), E_parent + delta, typ, vac_union)
                            pq_rows.append(i); pq_cols.append(j); pq_vals.append(-q_codd_sign * math.sqrt(weight))
                    else:
                        keyz = canonical_codd(z)[0] if retained_loop else None
                        singlet_is_in_P = retained_loop and keyz in index
                        if not singlet_is_in_P:
                            j = get_q(("mixed_1", pair_key), E_parent + D_1, "mixed_1", vac_union)
                            pq_rows.append(i); pq_cols.append(j); pq_vals.append(-q_codd_sign * math.sqrt(W_1))
                        j = get_q(("mixed_8", pair_key), E_parent + D_8, "mixed_8", vac_union)
                        pq_rows.append(i); pq_cols.append(j); pq_vals.append(-q_codd_sign * math.sqrt(W_8))
                    continue

                if len(shared) < 2:
                    continue

                # Generic 2/3-link exact local closure.
                multi_actions += 1
                fsteps = face_steps_generic(f, s, faces, lid_global, shift)
                sig, info = exact_multilink_spectrum(parent_steps, fsteps, ml_spec_cache)
                model_topologies.add(sig)
                pair_key, q_codd_sign = canonical_pair_codd(q, b)
                vac_union = vac_union_fast
                spec = [[lam, sp.Rational(w)] for lam, w in info["spec"]]

                # SU(3) center residue is the only square-free P state that can
                # overlap this raw product.  If it is retained, put its exact
                # Haar overlap directly in P and remove that norm from Q at the
                # matching electric eigenvalue.
                residue = mod3_reduce_flux(z)
                residue_is_loop = is_simple_single_loop(residue)
                if residue_is_loop:
                    rkey, rsign, _ = canonical_codd(residue)
                    jP = index.get(rkey)
                else:
                    jP = None
                    rsign = +1
                if jP is not None:
                    rsteps = ordered_loop_steps(residue, links, shift)
                    ov = exact_residue_overlap(parent_steps, fsteps, rsteps, sig, ml_overlap_cache)
                    ovf = float(ov)
                    if jP != i and abs(ovf) > 0:
                        pp_rows.append(i); pp_cols.append(jP); pp_vals.append(-rsign * ovf)
                    targetE = E_P[jP]
                    hit = False
                    for row in spec:
                        if abs(float(row[0]) - targetE) < 2e-12:
                            row[1] = sp.simplify(row[1] - sp.Rational(ov.numerator, ov.denominator) ** 2)
                            if row[1] < 0:
                                raise RuntimeError("P subtraction made multi-link Q spectral weight negative")
                            hit = True
                            break
                    if abs(ovf) > 0 and not hit:
                        raise RuntimeError("retained P residue energy absent from multi-link H0 spectrum")

                for aidx, (lam, w) in enumerate(spec):
                    wf = float(w)
                    if wf < 1e-15:
                        continue
                    typ = f"multilink_{len(shared)}_bright_{aidx}"
                    qkey = (typ, pair_key, str(lam))
                    j = get_q(qkey, float(lam), typ, vac_union)
                    pq_rows.append(i); pq_cols.append(j); pq_vals.append(-q_codd_sign * math.sqrt(wf))
                    multi_channels += 1

    W_PP = coo_matrix((pp_vals, (pp_rows, pp_cols)), shape=(nP, nP), dtype=np.float64).tocsr()
    W_PP.sum_duplicates()
    W_PP = W_PP + diags(p_diag, dtype=np.float64)
    asym = W_PP - W_PP.T
    asymmetry = 0.0 if asym.nnz == 0 else float(np.max(np.abs(asym.data)))
    if asymmetry > 1e-12:
        raise RuntimeError(f"P-space Hamiltonian asymmetry = {asymmetry}")

    B_PQ = coo_matrix((pq_vals, (pq_rows, pq_cols)), shape=(nP, len(q_energy)), dtype=np.float64).tocsr()
    B_PQ.sum_duplicates()
    return {
        "keys": keys, "states": states, "depth": depth, "index": index,
        "source_P": source, "E_P": E_P, "W_PP": W_PP, "B_PQ": B_PQ,
        "E_Q": np.asarray(q_energy, dtype=np.float64), "VAC_P": VAC_P,
        "VAC_Q": np.asarray(q_vac_count, dtype=np.float64), "Q_types": q_type,
        "asymmetry": asymmetry, "build_seconds": time.time() - t0,
        "multi_actions": multi_actions, "multi_channels": multi_channels,
        "multi_topologies": len(model_topologies), "sameface_handled": sameface_handled,
        "skipped_multilink": 0,
    }

# =============================================================================
# COLD t3 REGRESSION FROM THE ACTUAL ENRICHED MODEL
# =============================================================================
def validate_second_order_t3(model):
    states = model["states"]
    index = model["index"]
    E_P = model["E_P"]
    E_Q = model["E_Q"]
    W_PP = model["W_PP"]
    B_PQ = model["B_PQ"]

    plaquette_mask = np.asarray([
        plaquette_match(q) is not None for q in states
    ], dtype=bool)

    seed_face = 0
    pkey, psgn, _ = canonical_codd(B2[:, seed_face])
    if pkey not in index:
        raise RuntimeError("seed plaquette absent from P basis")
    ip = index[pkey]

    p_row = {
        int(k): float(v)
        for k, v in zip(W_PP.getrow(ip).indices, W_PP.getrow(ip).data)
    }
    q_row = {
        int(k): float(v)
        for k, v in zip(B_PQ.getrow(ip).indices, B_PQ.getrow(ip).data)
    }

    errors = []
    rows = []

    for qf in range(P):
        if qf == seed_face:
            continue
        shared = np.flatnonzero(
            (B2[:, seed_face] != 0) & (B2[:, qf] != 0)
        )
        if len(shared) != 1:
            continue

        qkey, qsgn, _ = canonical_codd(B2[:, qf])
        if qkey not in index:
            continue
        iq = index[qkey]

        p2 = {
            int(k): float(v)
            for k, v in zip(W_PP.getrow(iq).indices, W_PP.getrow(iq).data)
        }
        q2 = {
            int(k): float(v)
            for k, v in zip(B_PQ.getrow(iq).indices, B_PQ.getrow(iq).data)
        }

        coeff = 0.0

        for k in set(p_row).intersection(p2):
            if plaquette_mask[k]:
                continue
            coeff += p_row[k] * p2[k] / (E0_PLAQ - E_P[k])

        for k in set(q_row).intersection(q2):
            coeff += q_row[k] * q2[k] / (E0_PLAQ - E_Q[k])

        l = int(shared[0])
        incidence = int(B2[l, seed_face] * B2[l, qf])

        # Matrix entries are written in the canonical C-odd representatives,
        # hence the extra p/q canonical signs relative to the raw face basis.
        target = psgn * qsgn * incidence * T3_TARGET
        err = coeff - target
        errors.append(abs(err))
        rows.append((qf, incidence, qsgn, coeff, target, err))

    if len(rows) != 12:
        raise RuntimeError(f"expected 12 shared-edge plaquette neighbors, got {len(rows)}")

    gate(
        "enriched P+Q Hamiltonian cold-reproduces all 12 t3 hoppings",
        max(errors) < 5e-13,
        f"max |cold-target|={max(errors):.3e}",
    )

    return rows

# =============================================================================
# RUNTIME BACKEND
# =============================================================================
def prepare_runtime(model):
    nP = len(model["E_P"])
    nQ = len(model["E_Q"])

    source = np.zeros(nP + nQ, dtype=np.float64)
    source[:nP] = model["source_P"]

    if USE_GPU:
        E_P_b = cp.asarray(model["E_P"])
        E_Q_b = cp.asarray(model["E_Q"])
        VAC_P_b = cp.asarray(model["VAC_P"])
        VAC_Q_b = cp.asarray(model["VAC_Q"])
        W_PP_b = cpsparse.csr_matrix(model["W_PP"])
        B_b = cpsparse.csr_matrix(model["B_PQ"])
        BT_b = B_b.T.tocsr()
        source_b = cp.asarray(source)
    else:
        E_P_b = model["E_P"]
        E_Q_b = model["E_Q"]
        VAC_P_b = model["VAC_P"]
        VAC_Q_b = model["VAC_Q"]
        W_PP_b = model["W_PP"]
        B_b = model["B_PQ"]
        BT_b = B_b.T.tocsr()
        source_b = source

    return {
        "nP": nP,
        "nQ": nQ,
        "E_P": E_P_b,
        "E_Q": E_Q_b,
        "VAC_P": VAC_P_b,
        "VAC_Q": VAC_Q_b,
        "W_PP": W_PP_b,
        "B": B_b,
        "BT": BT_b,
        "source": source_b,
    }

# =============================================================================
# RESIDUAL-CONTROLLED SOURCE LANCZOS
# =============================================================================
def _to_float(x):
    if USE_GPU:
        return float(cp.asnumpy(x).reshape(()))
    return float(x)


def local_vacuum_energy(y):
    # One physical plaquette: |0> couples to the normalized C-even one-plaquette
    # state with amplitude sqrt(2). This is the exact vacuum energy of that
    # one-step local truncation and begins -y^2/C_F + O(y^4).
    return 0.5 * (E0_PLAQ - math.sqrt(E0_PLAQ * E0_PLAQ + 8.0 * y * y))


def source_lanczos(runtime, y, enriched=True, linked=True):
    nP = runtime["nP"]
    nQ = runtime["nQ"] if enriched else 0
    n = nP + nQ

    E_P = runtime["E_P"]
    E_Q = runtime["E_Q"]
    VAC_P = runtime["VAC_P"]
    VAC_Q = runtime["VAC_Q"]
    W_PP = runtime["W_PP"]
    B = runtime["B"]
    BT = runtime["BT"]

    if enriched:
        source = runtime["source"]
    else:
        source = runtime["source"][:nP]

    q = source / xp.linalg.norm(source)
    q_prev = xp.zeros_like(q)
    beta_prev = 0.0

    # Preallocate the reorthogonalization basis.  K=2 enriched is ~2e5 states;
    # 180 float64 vectors are ~290 MiB, comfortable on an A100 and typical Colab RAM.
    Q = xp.empty((MAX_LANCZOS, n), dtype=xp.float64)

    alpha = []
    beta = []
    last_pole = None
    stable_count = 0
    last_eval = None
    last_weight = None
    last_residual = float("inf")

    e_vac = local_vacuum_energy(y) if linked else 0.0
    E_P_eff = E_P - VAC_P * e_vac
    E_Q_eff = E_Q - VAC_Q * e_vac

    def matvec(x):
        p = x[:nP]
        out_p = E_P_eff * p + y * (W_PP @ p)
        if not enriched:
            return out_p

        qpart = x[nP:]
        out_p = out_p + y * (B @ qpart)
        out_q = E_Q_eff * qpart + y * (BT @ p)
        return xp.concatenate((out_p, out_q))

    for m in range(MAX_LANCZOS):
        Q[m] = q
        z = matvec(q)

        if m:
            z -= beta_prev * q_prev

        a = _to_float(xp.dot(q, z))
        z -= a * q

        # Two-pass full reorthogonalization, but performed as GEMV/GEMM against
        # the already-built Krylov slab rather than Python loops over vectors.
        Qm = Q[:m + 1]
        for _ in range(2):
            coeff = Qm @ z
            z -= coeff @ Qm

        b = _to_float(xp.linalg.norm(z))
        alpha.append(a)

        # T_{m+1} uses all PREVIOUS beta values.  The current b is the residual
        # coupling from the current tridiagonal space to the next Lanczos vector.
        if m >= 2:
            evals, evecs = eigh_tridiagonal(
                np.asarray(alpha, dtype=float),
                np.asarray(beta, dtype=float),
            )
            weights = evecs[0, :] ** 2
            pole = int(np.argmax(weights))
            E_pole = float(evals[pole])
            Z_pole = float(weights[pole])
            lowest_idx = int(np.flatnonzero(weights > 1e-12)[0])
            lowest_energy = float(evals[lowest_idx])
            lowest_weight = float(weights[lowest_idx])
            ritz_residual = float(b * abs(evecs[-1, pole]))

            if last_pole is not None:
                dE = abs(E_pole - last_pole[0])
                dZ = abs(Z_pole - last_pole[1])
                stable = (
                    ritz_residual < RITZ_TOL
                    and dE < ENERGY_STABILITY_TOL
                    and dZ < RESIDUE_STABILITY_TOL
                )
                stable_count = stable_count + 1 if stable else 0
            else:
                stable_count = 0

            last_pole = (E_pole, Z_pole)
            last_eval = evals
            last_weight = weights
            last_residual = ritz_residual

            if stable_count >= STABLE_CHECKS_REQUIRED:
                return {
                    "pole_energy": E_pole,
                    "pole_residue": Z_pole,
                    "ritz_residual": ritz_residual,
                    "krylov_dimension": m + 1,
                    "converged": True,
                    "dominant_is_lowest": bool(pole == lowest_idx),
                    "lowest_energy": lowest_energy,
                    "lowest_residue": lowest_weight,
                }

        if b < 1e-14:
            # Exact/near-exact Krylov closure.  The current Ritz pair is converged
            # even if the stability counter did not have another iteration to fire.
            if last_pole is not None:
                return {
                    "pole_energy": float(last_pole[0]),
                    "pole_residue": float(last_pole[1]),
                    "ritz_residual": float(last_residual),
                    "krylov_dimension": m + 1,
                    "converged": True,
                    "dominant_is_lowest": bool(pole == lowest_idx),
                    "lowest_energy": lowest_energy,
                    "lowest_residue": lowest_weight,
                }
            break

        if m < MAX_LANCZOS - 1:
            beta.append(b)
        q_prev = q
        q = z / b
        beta_prev = b

    if last_pole is None:
        # Tiny one-dimensional cases.
        return {
            "pole_energy": float(alpha[0]),
            "pole_residue": 1.0,
            "ritz_residual": 0.0,
            "krylov_dimension": 1,
            "converged": True,
            "dominant_is_lowest": True,
            "lowest_energy": float(alpha[0]),
            "lowest_residue": 1.0,
        }

    return {
        "pole_energy": float(last_pole[0]),
        "pole_residue": float(last_pole[1]),
        "ritz_residual": float(last_residual),
        "krylov_dimension": len(alpha),
        "converged": False,
        "dominant_is_lowest": bool(pole == lowest_idx),
        "lowest_energy": lowest_energy,
        "lowest_residue": lowest_weight,
    }


# =============================================================================
# WINDING-STRING SECTOR (fixed Z3 one-form charge; no C quotient)
# =============================================================================
class WindingStringSector:
    def __init__(self, Ls, max_depth=2, winding_dir=0):
        self.L = int(Ls)
        self.max_depth = int(max_depth)
        self.winding_dir = int(winding_dir)
        self._build_lattice()

    def shift(self, v, d, step=1):
        w = list(v)
        w[d] = (w[d] + step) % self.L
        return tuple(w)

    def _build_lattice(self):
        Ls = self.L
        self.verts = [(x, y, z) for x in range(Ls) for y in range(Ls) for z in range(Ls)]
        self.links = []
        self.lid = {}
        for v in self.verts:
            for d in range(3):
                self.lid[(v, d)] = len(self.links)
                self.links.append((v, d))

        self.faces = []
        for v in self.verts:
            for a, b in ((0, 1), (0, 2), (1, 2)):
                self.faces.append((v, a, b))

        self.B2 = np.zeros((len(self.links), len(self.faces)), dtype=np.int8)
        for f, (v, a, b) in enumerate(self.faces):
            va = self.shift(v, a)
            vb = self.shift(v, b)
            self.B2[self.lid[(v, a)], f] += 1
            self.B2[self.lid[(va, b)], f] += 1
            self.B2[self.lid[(vb, a)], f] -= 1
            self.B2[self.lid[(v, b)], f] -= 1

        self.link_faces = [[] for _ in self.links]
        for f in range(len(self.faces)):
            for l in np.flatnonzero(self.B2[:, f]):
                self.link_faces[int(l)].append(f)
        self.face_support_faces = []
        for f in range(len(self.faces)):
            ff = set()
            for l in np.flatnonzero(self.B2[:, f]):
                ff.update(self.link_faces[int(l)])
            self.face_support_faces.append(frozenset(ff))

    def candidate_faces(self, q):
        out = set()
        for l in np.flatnonzero(q):
            out.update(self.link_faces[int(l)])
        return out

    def support_face_count(self, *arrays):
        support = np.zeros(len(self.links), dtype=bool)
        for a in arrays:
            support |= (np.asarray(a) != 0)
        out = set()
        for l in np.flatnonzero(support):
            out.update(self.link_faces[int(l)])
        return len(out)

    def is_simple_winding_loop(self, q):
        support = np.flatnonzero(q)
        if len(support) < self.L:
            return False
        outgoing = {}
        indegree = Counter()
        used = set()
        for li in support:
            l = int(li)
            v, d = self.links[l]
            w = self.shift(v, d)
            src, dst = (v, w) if q[l] > 0 else (w, v)
            if src in outgoing:
                return False
            outgoing[src] = dst
            indegree[dst] += 1
            used.add(src)
            used.add(dst)
        if any(v not in outgoing or indegree[v] != 1 for v in used):
            return False
        start = next(iter(used))
        cur = start
        seen = set()
        while cur not in seen:
            seen.add(cur)
            cur = outgoing[cur]
        if cur != start or len(seen) != len(used):
            return False

        # Oriented winding number in the chosen periodic direction.
        net = 0
        for li in support:
            l = int(li)
            v, d = self.links[l]
            if d == self.winding_dir:
                net += int(q[l])
        return net == self.L

    def straight_sources(self):
        transverse = [d for d in range(3) if d != self.winding_dir]
        out = []
        for a in range(self.L):
            for b in range(self.L):
                base = [0, 0, 0]
                base[transverse[0]] = a
                base[transverse[1]] = b
                q = np.zeros(len(self.links), dtype=np.int8)
                for t in range(self.L):
                    v = list(base)
                    v[self.winding_dir] = t
                    v = tuple(v)
                    q[self.lid[(v, self.winding_dir)]] = 1
                out.append(q)
        return out

    def build_basis(self):
        states = {}
        depth = {}
        queue = deque()
        source_keys = []
        for q in self.straight_sources():
            key = q.tobytes()
            if key not in states:
                states[key] = q.copy()
                depth[key] = 0
                queue.append(key)
            source_keys.append(key)

        while queue:
            key = queue.popleft()
            d = depth[key]
            if d >= self.max_depth:
                continue
            q = states[key]
            for f in self.candidate_faces(q):
                bf = self.B2[:, f]
                for s in (-1, +1):
                    z = q + s * bf
                    if np.max(np.abs(z)) > 1:
                        continue
                    if not self.is_simple_winding_loop(z):
                        continue
                    z = z.astype(np.int8)
                    key2 = z.tobytes()
                    if key2 not in states:
                        states[key2] = z.copy()
                        depth[key2] = d + 1
                        queue.append(key2)

        keys = list(states)
        index = {k: i for i, k in enumerate(keys)}
        reps = [states[k] for k in keys]
        source = np.zeros(len(keys), dtype=np.float64)
        for key in source_keys:
            source[index[key]] += 1.0 / math.sqrt(len(source_keys))
        if abs(float(np.dot(source, source)) - 1.0) > 1e-12:
            raise RuntimeError("winding source normalization failed")
        return keys, reps, depth, index, source

    def build_model(self):
        t0 = time.time()
        keys, states, depth, index, source = self.build_basis()
        nP = len(states)
        E_P = np.asarray([0.5 * int(np.count_nonzero(q)) * CF for q in states], dtype=np.float64)
        VAC_P = np.asarray([len(self.candidate_faces(q)) for q in states], dtype=np.float64)
        pp_rows, pp_cols, pp_vals = [], [], []

        # Winding Q channels are parent/action-unique.  Store them as a flat
        # parent-indexed spectral list and eliminate them exactly by Feshbach at
        # solve time instead of materializing a gigantic explicit Q Hilbert space.
        q_parent, q_energy, q_vac_count, q_weight = [], [], [], []
        q_type_counts = Counter()
        ml_spec_cache, ml_overlap_cache = GLOBAL_ML_SPEC_CACHE, GLOBAL_ML_OVERLAP_CACHE
        model_topologies = set()
        multi_actions = 0
        multi_channels = 0

        def add_q(parent_i, energy, typ, vac_count, amplitude):
            q_parent.append(int(parent_i))
            q_energy.append(float(energy))
            q_vac_count.append(float(vac_count))
            q_weight.append(float(amplitude) ** 2)
            q_type_counts[str(typ)] += 1

        report_step = max(1, nP // 10)
        for i, q in enumerate(states):
            if nP >= 10000 and ((i + 1) % report_step == 0 or i == 0):
                print(f"      build progress {i+1:,}/{nP:,} P states; Q spectral entries={len(q_energy):,}")
            E_parent = E_P[i]
            parent_steps = ordered_loop_steps(q, self.links, self.shift)
            cand_q = self.candidate_faces(q)
            for f in cand_q:
                bf = self.B2[:, f]
                vac_union_fast = len(cand_q | self.face_support_faces[f])
                shared0 = np.flatnonzero((q != 0) & (bf != 0))
                for s in (-1, +1):
                    b = (s * bf).astype(np.int8)
                    z = q + b
                    shared = shared0
                    retained = np.max(np.abs(z)) <= 1 and self.is_simple_winding_loop(z)

                    if len(shared) == 1:
                        l = int(shared[0])
                        relation = int(q[l]) * int(b[l])
                        if retained:
                            j = index.get(z.astype(np.int8).tobytes())
                            if j is not None and j != i:
                                pp_rows.append(i); pp_cols.append(j); pp_vals.append(-1.0 / N)
                        if relation > 0:
                            add_q(i, E_parent + D_A, "like_bar3", vac_union_fast, math.sqrt(W_A))
                            add_q(i, E_parent + D_S, "like_6", vac_union_fast, math.sqrt(W_S))
                        else:
                            singlet_is_in_P = retained and z.astype(np.int8).tobytes() in index
                            if not singlet_is_in_P:
                                add_q(i, E_parent + D_1, "mixed_1", vac_union_fast, math.sqrt(W_1))
                            add_q(i, E_parent + D_8, "mixed_8", vac_union_fast, math.sqrt(W_8))
                        continue

                    if len(shared) < 2:
                        continue

                    multi_actions += 1
                    fsteps = face_steps_generic(f, s, self.faces, self.lid, self.shift)
                    sig, info = exact_multilink_spectrum(parent_steps, fsteps, ml_spec_cache)
                    model_topologies.add(sig)
                    spec = [[lam, sp.Rational(w)] for lam, w in info["spec"]]

                    residue = mod3_reduce_flux(z)
                    residue_is_loop = self.is_simple_winding_loop(residue)
                    jP = index.get(residue.tobytes()) if residue_is_loop else None
                    if jP is not None:
                        rsteps = ordered_loop_steps(residue, self.links, self.shift)
                        ov = exact_residue_overlap(parent_steps, fsteps, rsteps, sig, ml_overlap_cache)
                        ovf = float(ov)
                        if jP != i and abs(ovf) > 0:
                            pp_rows.append(i); pp_cols.append(jP); pp_vals.append(-ovf)
                        targetE = E_P[jP]
                        hit = False
                        for row in spec:
                            if abs(float(row[0]) - targetE) < 2e-12:
                                row[1] = sp.simplify(row[1] - sp.Rational(ov.numerator, ov.denominator) ** 2)
                                if row[1] < 0:
                                    raise RuntimeError("string P subtraction made multi-link Q weight negative")
                                hit = True
                                break
                        if abs(ovf) > 0 and not hit:
                            raise RuntimeError("string retained P residue energy absent from local H0 spectrum")

                    for aidx, (lam, w) in enumerate(spec):
                        wf = float(w)
                        if wf < 1e-15:
                            continue
                        typ = f"multilink_{len(shared)}_bright_{aidx}"
                        add_q(i, float(lam), typ, vac_union_fast, math.sqrt(wf))
                        multi_channels += 1

        W_PP = coo_matrix((pp_vals, (pp_rows, pp_cols)), shape=(nP, nP), dtype=np.float64).tocsr()
        W_PP.sum_duplicates()
        asym = W_PP - W_PP.T
        asymmetry = 0.0 if asym.nnz == 0 else float(np.max(np.abs(asym.data)))
        if asymmetry > 1e-12:
            raise RuntimeError(f"winding P-space asymmetry={asymmetry}")

        return {
            "keys": keys, "states": states, "depth": depth, "index": index,
            "source_P": source, "E_P": E_P, "VAC_P": VAC_P, "W_PP": W_PP,
            "Q_parent": np.asarray(q_parent, dtype=np.int32),
            "E_Q": np.asarray(q_energy, dtype=np.float64),
            "VAC_Q": np.asarray(q_vac_count, dtype=np.float64),
            "Q_weight": np.asarray(q_weight, dtype=np.float64),
            "Q_type_counts": dict(q_type_counts),
            "Q_count": len(q_energy),
            "asymmetry": asymmetry, "skipped_multilink": 0,
            "multi_actions": multi_actions, "multi_channels": multi_channels,
            "multi_topologies": len(model_topologies), "build_seconds": time.time() - t0,
        }


def free_backend_memory():
    if USE_GPU:
        cp.get_default_memory_pool().free_all_blocks()
        cp.get_default_pinned_memory_pool().free_all_blocks()



def prepare_string_feshbach_runtime(model):
    if USE_GPU:
        E_P = cp.asarray(model["E_P"])
        VAC_P = cp.asarray(model["VAC_P"])
        W_PP = cpsparse.csr_matrix(model["W_PP"])
        source = cp.asarray(model["source_P"])
        q_parent = cp.asarray(model["Q_parent"])
        E_Q = cp.asarray(model["E_Q"])
        VAC_Q = cp.asarray(model["VAC_Q"])
        Q_weight = cp.asarray(model["Q_weight"])
    else:
        E_P = model["E_P"]
        VAC_P = model["VAC_P"]
        W_PP = model["W_PP"]
        source = model["source_P"]
        q_parent = model["Q_parent"]
        E_Q = model["E_Q"]
        VAC_Q = model["VAC_Q"]
        Q_weight = model["Q_weight"]
    return {
        "nP": len(model["E_P"]), "E_P": E_P, "VAC_P": VAC_P, "W_PP": W_PP,
        "source": source, "Q_parent": q_parent, "E_Q": E_Q,
        "VAC_Q": VAC_Q, "Q_weight": Q_weight,
    }


def source_lanczos_custom(matvec, source, return_vector=False):
    n = len(source)
    q = source / xp.linalg.norm(source)
    q_prev = xp.zeros_like(q)
    beta_prev = 0.0
    Q = xp.empty((MAX_LANCZOS, n), dtype=xp.float64)
    alpha, beta = [], []
    last = None
    stable_count = 0

    for m in range(MAX_LANCZOS):
        Q[m] = q
        z = matvec(q)
        if m:
            z -= beta_prev * q_prev
        a = _to_float(xp.dot(q, z))
        z -= a * q
        Qm = Q[:m+1]
        for _ in range(2):
            coeff = Qm @ z
            z -= coeff @ Qm
        b = _to_float(xp.linalg.norm(z))
        alpha.append(a)

        if m >= 1:
            evals, evecs = eigh_tridiagonal(np.asarray(alpha), np.asarray(beta))
            weights = evecs[0, :] ** 2
            pole = int(np.argmax(weights))
            nz = np.flatnonzero(weights > 1e-12)
            low = int(nz[0]) if len(nz) else pole
            E = float(evals[pole]); Z = float(weights[pole])
            resid = float(b * abs(evecs[-1, pole]))
            if last is not None:
                ok = resid < RITZ_TOL and abs(E-last[0]) < ENERGY_STABILITY_TOL and abs(Z-last[1]) < RESIDUE_STABILITY_TOL
                stable_count = stable_count + 1 if ok else 0
            last = (E, Z, resid, pole, low, evecs[:, pole].copy(), m+1)
            if stable_count >= STABLE_CHECKS_REQUIRED:
                vec = None
                if return_vector:
                    coeffv = xp.asarray(last[5])
                    vec = coeffv @ Q[:m+1]
                    vec = vec / xp.linalg.norm(vec)
                return {
                    "pole_energy": E, "pole_residue": Z, "ritz_residual": resid,
                    "krylov_dimension": m+1, "converged": True,
                    "dominant_is_lowest": pole == low, "ritz_vector": vec,
                }
        if b < 1e-14:
            break
        if m < MAX_LANCZOS - 1:
            beta.append(b)
        q_prev = q
        q = z / b
        beta_prev = b

    if last is None:
        vec = source / xp.linalg.norm(source) if return_vector else None
        return {"pole_energy": float(alpha[0]), "pole_residue": 1.0, "ritz_residual": 0.0,
                "krylov_dimension": 1, "converged": True, "dominant_is_lowest": True,
                "ritz_vector": vec}
    E, Z, resid, pole, low, yvec, mdim = last
    vec = None
    if return_vector:
        coeffv = xp.asarray(yvec)
        vec = coeffv @ Q[:mdim]
        vec = vec / xp.linalg.norm(vec)
    return {"pole_energy": E, "pole_residue": Z, "ritz_residual": resid,
            "krylov_dimension": mdim, "converged": resid < RITZ_TOL,
            "dominant_is_lowest": pole == low, "ritz_vector": vec}


def string_effective_eval(runtime, u, trial_E, return_vector=False):
    e_vac = local_vacuum_energy(u)
    E_P = runtime["E_P"] - runtime["VAC_P"] * e_vac
    E_Q = runtime["E_Q"] - runtime["VAC_Q"] * e_vac
    denom = trial_E - E_Q
    mind = _to_float(xp.min(xp.abs(denom))) if len(E_Q) else float("inf")
    if mind < 1e-9:
        raise RuntimeError(f"Feshbach trial energy hit a Q pole: min denominator={mind:.3e}")
    if len(E_Q):
        weights = runtime["Q_weight"] / denom
        sigma_diag = xp.bincount(runtime["Q_parent"], weights=weights, minlength=runtime["nP"])
    else:
        sigma_diag = xp.zeros(runtime["nP"], dtype=xp.float64)
    diag = E_P + (u*u) * sigma_diag
    def mv(x):
        return diag * x + u * (runtime["W_PP"] @ x)
    r = source_lanczos_custom(mv, runtime["source"], return_vector=return_vector)
    r["min_q_denominator"] = mind
    return r


def string_p_only_eval(runtime, u):
    e_vac = local_vacuum_energy(u)
    diag = runtime["E_P"] - runtime["VAC_P"] * e_vac
    def mv(x):
        return diag * x + u * (runtime["W_PP"] @ x)
    return source_lanczos_custom(mv, runtime["source"], return_vector=False)


def string_feshbach_pole(runtime, u, fp_tol=3e-11, max_fp=24):
    p0 = string_p_only_eval(runtime, u)
    E = p0["pole_energy"]
    prev_E = prev_F = None
    last = None
    for it in range(max_fp):
        r = string_effective_eval(runtime, u, E, return_vector=False)
        F = r["pole_energy"] - E
        last = r
        if abs(F) < fp_tol and r["converged"]:
            break
        if prev_E is not None and abs(F - prev_F) > 1e-14:
            Enew = E - F * (E - prev_E) / (F - prev_F)
            if (not math.isfinite(Enew)) or abs(Enew - E) > 0.75:
                Enew = E + 0.5 * F
        else:
            Enew = E + 0.65 * F
        prev_E, prev_F = E, F
        E = Enew
    else:
        raise RuntimeError(f"string Feshbach fixed point failed at u={u}")

    E = last["pole_energy"]
    final = string_effective_eval(runtime, u, E, return_vector=True)
    fp_resid = abs(final["pole_energy"] - E)
    E = final["pole_energy"]
    pvec = final.pop("ritz_vector")

    # Restore full P+Q normalization.  q_a = u v_ai p_i/(E-Ea).
    e_vac = local_vacuum_energy(u)
    Eq = runtime["E_Q"] - runtime["VAC_Q"] * e_vac
    if len(Eq):
        p2 = xp.abs(pvec) ** 2
        perq = p2[runtime["Q_parent"]] * runtime["Q_weight"] / ((E - Eq) ** 2)
        qnorm = (u*u) * _to_float(xp.sum(perq))
    else:
        qnorm = 0.0
    final["pole_residue_P"] = final["pole_residue"]
    final["pole_residue"] = final["pole_residue"] / (1.0 + qnorm)
    final["q_norm_ratio"] = qnorm
    final["feshbach_residual"] = fp_resid
    final["fixed_point_iterations"] = it + 1
    final["converged"] = bool(final["converged"] and fp_resid < 5*fp_tol)
    return final


def fit_sigma_terms(length_energy, powers=(0, 2), min_L=None):
    Ls = np.asarray(sorted(L for L in length_energy if min_L is None or L >= min_L), dtype=float)
    Es = np.asarray([length_energy[int(Lv)] for Lv in Ls], dtype=float)
    if len(Ls) < len(powers):
        raise ValueError("not enough string lengths for requested fit")
    yv = Es / Ls
    X = np.column_stack([np.ones_like(Ls) if p == 0 else Ls ** (-p) for p in powers])
    coeff, *_ = np.linalg.lstsq(X, yv, rcond=None)
    pred = X @ coeff
    rms = float(np.sqrt(np.mean((yv - pred) ** 2)))
    return float(coeff[0]), tuple(map(float, coeff[1:])), rms


def sigma_fit_bundle(length_energy):
    out = {}
    out["Lall_1overL2"] = fit_sigma_terms(length_energy, (0, 2))
    if len(length_energy) >= 5:
        out["Lall_1overL2_L4"] = fit_sigma_terms(length_energy, (0, 2, 4))
    if sum(L >= 4 for L in length_energy) >= 2:
        out["L4plus_1overL2"] = fit_sigma_terms(length_energy, (0, 2), min_L=4)
    central_key = "Lall_1overL2_L4" if "Lall_1overL2_L4" in out else "Lall_1overL2"
    central = out[central_key][0]
    spread = max(abs(v[0] - central) for v in out.values()) if len(out) > 1 else 0.0
    return central_key, central, spread, out

# =============================================================================
# PRODUCTION DRIVER: MULTI-LINK MASS + LONGER STRINGS
# =============================================================================

# =============================================================================
# v5: GLOBAL-Q GRAM MERGE + P-ONLY FESHBACH + SOURCE-ADAPTED K=3
# =============================================================================
#
# The v4 remaining systematic was that source-bright Q closures generated by
# different raw trace products were individually normalized but not globally
# Gram-merged.  v5 removes that approximation without ever materializing a huge
# nonorthogonal Q basis.
#
# For each magnetic action a and each exact electric eigenvalue lambda, define
#
#   |q_a^lambda> = Q P_lambda M_a |P_parent(a)> .
#
# Within a fixed lambda block H_Q = lambda G_Q.  If C is the incidence from P
# parents to the raw action channels, the exact Feshbach contribution is
#
#   C G_Q [E G_Q - H_Q]^{+} G_Q C^T
#       = (C G_Q C^T)/(E-lambda),
#
# on the physical Gram range.  Therefore Gram-null directions never have to be
# inverted explicitly: it is enough to construct the sparse positive-semidefinite
# P-space kernel K_lambda = C G_Q C^T, including ALL cross overlaps between
# source-bright channels.  This is the global Gram quotient in Schur form.
#
# The linked vacuum counterterm is retained from v4.  A hard gate refuses any
# nonzero Q overlap whose two raw constructions assign different support-count
# counterterms; such a failure would mean the scalar linked counterterm itself
# must be upgraded to an operator before a result can be quoted.

V5_GLUE_DEPTHS = tuple(int(x) for x in os.environ.get("V5_GLUE_DEPTHS", "2,3").split(",") if x.strip())
V5_STRING_DEPTHS = tuple(int(x) for x in os.environ.get("V5_STRING_DEPTHS", "2").split(",") if x.strip())
V5_STRING_LENGTHS = tuple(int(x) for x in os.environ.get("V5_STRING_LENGTHS", "3,4,5,6,7").split(",") if x.strip())
V5_GLOBAL_GRAM = os.environ.get("V5_GLOBAL_GRAM", "1") != "0"
V5_MAX_FP = int(os.environ.get("V5_MAX_FP", "28"))
V5_FP_TOL = float(os.environ.get("V5_FP_TOL", "3e-11"))
V5_GRAM_RANK_TOL = float(os.environ.get("V5_GRAM_RANK_TOL", "2e-11"))
V5_PROGRESS = int(os.environ.get("V5_PROGRESS", "1"))

# Exact rational helpers -------------------------------------------------------
def _sp_to_frac(x):
    x = sp.Rational(x)
    return Fraction(int(sp.numer(x)), int(sp.denom(x)))


def _frac_to_sp(x):
    return sp.Rational(x.numerator, x.denominator)


def _flux_sparse_key(q):
    q = np.asarray(q, dtype=np.int8)
    return tuple((int(i), int(q[i])) for i in np.flatnonzero(q))


def _flux_sparse_key_codd(q):
    a = _flux_sparse_key(q)
    b = _flux_sparse_key(-np.asarray(q, dtype=np.int8))
    return a if a <= b else b


def _pair_c_invariant(q, b):
    pair = tuple(sorted((np.asarray(q, dtype=np.int8).tobytes(), np.asarray(b, dtype=np.int8).tobytes())))
    pair_c = tuple(sorted(((-np.asarray(q, dtype=np.int8)).tobytes(), (-np.asarray(b, dtype=np.int8)).tobytes())))
    return pair == pair_c


def _conjugate_steps(steps):
    return [(int(l), -int(d)) for l, d in reversed(steps)]


def _joint_canon_states(*states):
    """Jointly relabel physical links; Haar/Fierz depends only on equality pattern."""
    mp = {}
    out = []
    for st in states:
        if st is None:
            out.append(None)
            continue
        occ = []
        for link, typ in st.occ:
            if link not in mp:
                mp[link] = len(mp)
            occ.append((mp[link], typ))
        out.append(LXState(tuple(occ), st.part))
    return tuple(out)


@lru_cache(None)
def _haar_canon_cached(a, b):
    if a is None or b is None:
        return Fraction(0)
    return lx_haar_inner(a, b)


def _haar_joint(a, b):
    aa, bb = _joint_canon_states(a, b)
    return _haar_canon_cached(aa, bb)


def _vec_H0(v):
    out = defaultdict(Fraction)
    for st, c in v.items():
        for z, a in lx_H0_action(st).items():
            out[z] += c * a
    return {z: c for z, c in out.items() if c}


def _project_seed(seed, lam, lams):
    """Exact spectral projector P_lam applied as the Lagrange polynomial in H0."""
    lam = Fraction(lam)
    lams = tuple(Fraction(x) for x in lams)
    v = {seed: Fraction(1)}
    for mu in lams:
        if mu == lam:
            continue
        den = lam - mu
        hv = _vec_H0(v)
        out = defaultdict(Fraction)
        for st, c in hv.items():
            out[st] += c / den
        for st, c in v.items():
            out[st] -= mu * c / den
        v = {st: c for st, c in out.items() if c}
    return v


def _state_vec_inner(st, v):
    if st is None:
        return Fraction(0)
    total = Fraction(0)
    for z, c in v.items():
        total += c * lx_haar_inner(st, z)
    return total


# Cache exact local spectra by overlap topology, including one-link and the
# same-plaquette determinant cases.  Unlike v4's multi-link cache, raw norm need
# not equal one (chi chi-bar and chi^2 have norm two).
GLOBAL_ACTION_SPEC = {}

def exact_action_spectrum(parent_steps, pface_steps):
    sig = local_topology_signature(parent_steps, pface_steps)
    if sig not in GLOBAL_ACTION_SPEC:
        raw = lx_tensor_product(lx_trace_state(parent_steps), lx_trace_state(pface_steps))
        norm, spec, closure_dim, gram_rank = lx_spectral_measure(raw)
        GLOBAL_ACTION_SPEC[sig] = {
            "norm": _sp_to_frac(norm),
            "spec": tuple((_sp_to_frac(lam), _sp_to_frac(w)) for lam, w in spec),
            "lams": tuple(_sp_to_frac(lam) for lam, _ in spec),
            "closure_dim": int(closure_dim),
            "gram_rank": int(gram_rank),
        }
    return sig, GLOBAL_ACTION_SPEC[sig]


@lru_cache(None)
def _raw_p_overlap_canon(raw, pstate):
    return lx_haar_inner(pstate, raw)


def exact_raw_p_overlap(raw, pstate):
    rr, pp = _joint_canon_states(raw, pstate)
    return _raw_p_overlap_canon(rr, pp)


@lru_cache(maxsize=250000)
def _q_overlap_canon(raw_a, p_a, ov_a, psub_a,
                     raw_b, p_b, ov_b, psub_b,
                     lam, lams_b):
    """<q_a^lam|q_b^lam> in a jointly canonicalized local topology."""
    vb = _project_seed(raw_b, lam, lams_b)
    if psub_b and p_b is not None and ov_b:
        vb = dict(vb)
        vb[p_b] = vb.get(p_b, Fraction(0)) - ov_b
        if vb[p_b] == 0:
            del vb[p_b]
    val = _state_vec_inner(raw_a, vb)
    if psub_a and p_a is not None and ov_a:
        val -= ov_a * _state_vec_inner(p_a, vb)
    return val


def exact_q_overlap(raw_a, p_a, ov_a, psub_a,
                    raw_b, p_b, ov_b, psub_b,
                    lam, lams_b):
    ca, cpa, cb, cpb = _joint_canon_states(raw_a, p_a, raw_b, p_b)
    return _q_overlap_canon(
        ca, cpa, Fraction(ov_a), bool(psub_a),
        cb, cpb, Fraction(ov_b), bool(psub_b),
        Fraction(lam), tuple(Fraction(x) for x in lams_b),
    )


@dataclass(frozen=True)
class ActionRec:
    parent: int
    face: int
    orient: int
    vac: int
    qsign: int


class _CollisionStore:
    def __init__(self):
        self.first = {}
        self.multi = {}
    def add(self, key, rec):
        if key in self.multi:
            self.multi[key].append(rec)
        elif key in self.first:
            self.multi[key] = [self.first.pop(key), rec]
        else:
            self.first[key] = rec
    @property
    def collision_groups(self):
        return self.multi


# Generic global-Gram model builder ------------------------------------------
def _build_global_model(
    states, index, source, E_P, VAC_P,
    candidate_faces_fn, face_flux_fn, face_steps_fn, ordered_steps_fn,
    face_support_faces_obj, p_lookup_fn, group_key_fn,
    codd=False, label="sector",
):
    t0 = time.time()
    nP = len(states)
    pp_rows, pp_cols, pp_vals = [], [], []
    kernel_diag = {}                 # (lam Fraction, vac int) -> np.ndarray[nP]
    cross_rows = defaultdict(list)
    cross_cols = defaultdict(list)
    cross_vals = defaultdict(list)
    collisions = _CollisionStore()

    action_channels = 0
    raw_actions = 0
    exact_topologies = set()
    c_even_actions = 0
    direct_P_actions = 0

    # Compact action reconstruction helper used again during Gram collision pass.
    def action_detail(rec, lam=None, conjugate=False):
        q = states[rec.parent]
        parent_steps = ordered_steps_fn(q)
        fsteps = face_steps_fn(rec.face, rec.orient)
        if conjugate:
            parent_steps = _conjugate_steps(parent_steps)
            fsteps = _conjugate_steps(fsteps)
        raw = lx_tensor_product(lx_trace_state(parent_steps), lx_trace_state(fsteps))
        _, info = exact_action_spectrum(parent_steps, fsteps)
        lams = info["lams"]

        b = (rec.orient * face_flux_fn(rec.face)).astype(np.int8)
        residue = mod3_reduce_flux(q + b)
        jP, psgn = p_lookup_fn(residue)
        pstate = None
        ov = Fraction(0)
        psub = False
        if jP is not None:
            rsteps = ordered_steps_fn(residue)
            if conjugate:
                rsteps = _conjugate_steps(rsteps)
            pstate = lx_trace_state(rsteps)
            ov = exact_raw_p_overlap(raw, pstate)
            if lam is not None:
                psub = abs(float(lam) - float(E_P[jP])) < 2e-12 and ov != 0
        return {
            "raw": raw, "lams": lams, "residue": residue,
            "jP": jP, "psgn": psgn, "pstate": pstate,
            "ov": ov, "psub": psub,
        }

    report_every = max(1, nP // 10)
    for i, q in enumerate(states):
        parent_steps = ordered_steps_fn(q)
        cand = candidate_faces_fn(q)
        if V5_PROGRESS and nP > 10000 and (i == 0 or (i + 1) % report_every == 0):
            nch = sum(int(np.count_nonzero(v)) for v in kernel_diag.values())
            print(f"      {label} build {i+1:,}/{nP:,} P states; diagonal Q blocks={len(kernel_diag)}, nonzero parent-block entries~{nch:,}")

        for f in cand:
            bf = face_flux_fn(f)
            vac_union = len(cand | face_support_faces_obj[f])
            for s in (-1, +1):
                b = (s * bf).astype(np.int8)
                raw_actions += 1

                if codd and _pair_c_invariant(q, b):
                    # The raw two-trace product is C-even, so the two halves of
                    # the C- parent cancel exactly (e.g. chi_p chi_pbar).
                    c_even_actions += 1
                    continue

                fsteps = face_steps_fn(f, s)
                sig, info = exact_action_spectrum(parent_steps, fsteps)
                exact_topologies.add(sig)
                raw = lx_tensor_product(lx_trace_state(parent_steps), lx_trace_state(fsteps))

                residue = mod3_reduce_flux(q + b)
                jP, psgn = p_lookup_fn(residue)
                pstate = None
                ov = Fraction(0)
                if jP is not None:
                    rsteps = ordered_steps_fn(residue)
                    pstate = lx_trace_state(rsteps)
                    ov = exact_raw_p_overlap(raw, pstate)
                    if ov:
                        amp = -float(psgn) * float(ov)
                        pp_rows.append(i); pp_cols.append(jP); pp_vals.append(amp)
                        direct_P_actions += 1

                qsign = canonical_pair_codd(q, b)[1] if codd else +1
                residue_key = group_key_fn(residue)

                for lam, w in info["spec"]:
                    qnorm = Fraction(w)
                    if jP is not None and abs(float(lam) - float(E_P[jP])) < 2e-12 and ov:
                        qnorm -= ov * ov
                    if qnorm < 0:
                        raise RuntimeError(f"{label}: negative Q norm after P subtraction")
                    if qnorm == 0:
                        continue

                    # For non-C-invariant raw products, center selection forces
                    # <q|Cq>=0 unless the linkwise mod-3 residue vanishes.  The
                    # latter case is exactly the C-even action skipped above.
                    if codd and not residue_key:
                        raise RuntimeError(f"{label}: non-invariant C- action unexpectedly has zero center residue")

                    kkey = (Fraction(lam), int(vac_union))
                    if kkey not in kernel_diag:
                        kernel_diag[kkey] = np.zeros(nP, dtype=np.float64)
                    kernel_diag[kkey][i] += float(qnorm)
                    action_channels += 1
                    collisions.add((residue_key, Fraction(lam)), ActionRec(i, int(f), int(s), int(vac_union), int(qsign)))

    W_PP = coo_matrix((pp_vals, (pp_rows, pp_cols)), shape=(nP, nP), dtype=np.float64).tocsr()
    W_PP.sum_duplicates()
    asym = W_PP - W_PP.T
    asymmetry = 0.0 if asym.nnz == 0 else float(np.max(np.abs(asym.data)))
    if asymmetry > 2e-12:
        raise RuntimeError(f"{label}: P-space magnetic matrix asymmetry={asymmetry:.3e}")

    # Global Q Gram merge.  Only channels with equal linkwise Z3 residue and
    # equal electric energy can overlap.  Most groups have size one and never
    # reach this pass.
    checked_pairs = 0
    nonzero_cross = 0
    vac_mismatch = 0
    gram_nullity = 0
    gram_rank_total = 0
    gram_dim_total = 0
    min_gram_eval = 0.0
    max_norm_overlap = 0.0

    for gidx, ((residue_key, lam), recs) in enumerate(collisions.collision_groups.items()):
        n = len(recs)
        G = np.zeros((n, n), dtype=np.float64)
        details = []
        for a, rec in enumerate(recs):
            da = action_detail(rec, lam=lam, conjugate=False)
            # Exact self norm from the pass-1 spectral weight/P subtraction,
            # recomputed through the projector as a consistency check.
            selfg = exact_q_overlap(
                da["raw"], da["pstate"], da["ov"], da["psub"],
                da["raw"], da["pstate"], da["ov"], da["psub"],
                lam, da["lams"],
            )
            if codd:
                dc = action_detail(rec, lam=lam, conjugate=True)
                selfc = exact_q_overlap(
                    da["raw"], da["pstate"], da["ov"], da["psub"],
                    dc["raw"], dc["pstate"], dc["ov"], dc["psub"],
                    lam, dc["lams"],
                )
                selfg -= selfc
            if selfg < 0:
                raise RuntimeError(f"{label}: negative exact C-/Q Gram norm {selfg}")
            G[a, a] = float(selfg)
            details.append(da)

        for a in range(n):
            ra = recs[a]; da = details[a]
            rka = _flux_sparse_key(da["residue"])
            for b in range(a + 1, n):
                rb = recs[b]; db = details[b]
                rkb = _flux_sparse_key(db["residue"])
                checked_pairs += 1

                normal = Fraction(0)
                crossc = Fraction(0)
                if rka == rkb:
                    normal = exact_q_overlap(
                        da["raw"], da["pstate"], da["ov"], da["psub"],
                        db["raw"], db["pstate"], db["ov"], db["psub"],
                        lam, db["lams"],
                    )
                if codd and rka == _flux_sparse_key(-db["residue"]):
                    dbc = action_detail(rb, lam=lam, conjugate=True)
                    crossc = exact_q_overlap(
                        da["raw"], da["pstate"], da["ov"], da["psub"],
                        dbc["raw"], dbc["pstate"], dbc["ov"], dbc["psub"],
                        lam, dbc["lams"],
                    )
                g = (normal - crossc) if codd else normal
                if g == 0:
                    continue
                nonzero_cross += 1
                if ra.vac != rb.vac:
                    vac_mismatch += 1
                    raise RuntimeError(
                        f"{label}: globally overlapping Q channels have different linked-vacuum counts "
                        f"({ra.vac} vs {rb.vac}); upgrade vacuum counterterm to an operator before proceeding"
                    )
                gf = float(g)
                G[a, b] = G[b, a] = gf
                den = math.sqrt(max(G[a, a] * G[b, b], 1e-300))
                max_norm_overlap = max(max_norm_overlap, abs(gf) / den)
                kkey = (Fraction(lam), int(ra.vac))
                if ra.parent == rb.parent:
                    cross_rows[kkey].append(ra.parent)
                    cross_cols[kkey].append(rb.parent)
                    cross_vals[kkey].append(2.0 * gf)
                else:
                    cross_rows[kkey].extend((ra.parent, rb.parent))
                    cross_cols[kkey].extend((rb.parent, ra.parent))
                    cross_vals[kkey].extend((gf, gf))

        if np.any(np.abs(G - np.diag(np.diag(G))) > 0):
            ev = np.linalg.eigvalsh(0.5 * (G + G.T))
            min_gram_eval = min(min_gram_eval, float(ev.min()))
            tol = V5_GRAM_RANK_TOL * max(1.0, float(ev.max()))
            rank = int(np.sum(ev > tol))
            gram_nullity += n - rank
            gram_rank_total += rank
            gram_dim_total += n
        else:
            gram_rank_total += n
            gram_dim_total += n

    if min_gram_eval < -2e-9:
        raise RuntimeError(f"{label}: global bright-Q Gram block not PSD; min eigenvalue={min_gram_eval:.3e}")
    if max_norm_overlap > 1.0 + 2e-9:
        raise RuntimeError(f"{label}: Q overlap violates Cauchy bound; max normalized={max_norm_overlap:.9g}")

    # Final sparse K_(lambda,v) = C G C^T blocks.
    kernels = []
    all_kkeys = sorted(kernel_diag, key=lambda x: (float(x[0]), x[1]))
    for kkey in all_kkeys:
        diagv = kernel_diag[kkey]
        di = np.flatnonzero(np.abs(diagv) > 0)
        rows = list(map(int, di)); cols = list(map(int, di)); vals = list(map(float, diagv[di]))
        if V5_GLOBAL_GRAM and kkey in cross_rows:
            rows.extend(cross_rows[kkey]); cols.extend(cross_cols[kkey]); vals.extend(cross_vals[kkey])
        Kmat = coo_matrix((vals, (rows, cols)), shape=(nP, nP), dtype=np.float64).tocsr()
        Kmat.sum_duplicates()
        Kasym = Kmat - Kmat.T
        kerr = 0.0 if Kasym.nnz == 0 else float(np.max(np.abs(Kasym.data)))
        if kerr > 2e-11:
            raise RuntimeError(f"{label}: Feshbach kernel asymmetry={kerr:.3e}")
        kernels.append((float(kkey[0]), int(kkey[1]), Kmat))

    return {
        "states": states, "index": index, "source_P": np.asarray(source, dtype=np.float64),
        "E_P": np.asarray(E_P, dtype=np.float64), "VAC_P": np.asarray(VAC_P, dtype=np.float64),
        "W_PP": W_PP, "kernels": kernels,
        "build_seconds": time.time() - t0, "asymmetry": asymmetry,
        "raw_actions": raw_actions, "action_channels": action_channels,
        "exact_topologies": len(exact_topologies), "collision_groups": len(collisions.collision_groups),
        "gram_pairs_checked": checked_pairs, "gram_nonzero_cross": nonzero_cross,
        "gram_nullity": gram_nullity, "gram_rank_total": gram_rank_total,
        "gram_dim_total": gram_dim_total, "gram_min_eig": min_gram_eval,
        "gram_max_normalized_overlap": max_norm_overlap, "vac_mismatch": vac_mismatch,
        "c_even_actions": c_even_actions, "direct_P_actions": direct_P_actions,
    }


# Glueball wrapper -------------------------------------------------------------
def build_global_glueball_model(max_depth):
    keys, states, depth, index, source = build_graph_basis(max_depth)
    E_P = np.asarray([0.5 * int(np.count_nonzero(q)) * CF for q in states], dtype=np.float64)
    VAC_P = np.asarray([len(candidate_faces(q)) for q in states], dtype=np.float64)
    lid_global = {(v, d): i for i, (v, d) in enumerate(links)}

    def face_flux(f):
        return B2[:, f]
    def fsteps(f, s):
        return face_steps_generic(f, s, faces, lid_global, shift)
    def osteps(q):
        return ordered_loop_steps(q, links, shift)
    def plookup(residue):
        key, sgn, _ = canonical_codd(residue)
        return index.get(key), int(sgn)
    def gkey(residue):
        return _flux_sparse_key_codd(residue)

    model = _build_global_model(
        states, index, source, E_P, VAC_P,
        candidate_faces, face_flux, fsteps, osteps,
        face_support_faces, plookup, gkey,
        codd=True, label=f"glue K={max_depth}",
    )
    model["keys"] = keys
    model["depth"] = depth
    model["K"] = int(max_depth)
    return model


# String wrapper ---------------------------------------------------------------
def build_global_string_model(sector):
    keys, states, depth, index, source = sector.build_basis()
    E_P = np.asarray([0.5 * int(np.count_nonzero(q)) * CF for q in states], dtype=np.float64)
    VAC_P = np.asarray([len(sector.candidate_faces(q)) for q in states], dtype=np.float64)

    def face_flux(f):
        return sector.B2[:, f]
    def fsteps(f, s):
        return face_steps_generic(f, s, sector.faces, sector.lid, sector.shift)
    def osteps(q):
        return ordered_loop_steps(q, sector.links, sector.shift)
    def plookup(residue):
        return index.get(np.asarray(residue, dtype=np.int8).tobytes()), +1
    def gkey(residue):
        return _flux_sparse_key(residue)

    model = _build_global_model(
        states, index, source, E_P, VAC_P,
        sector.candidate_faces, face_flux, fsteps, osteps,
        sector.face_support_faces, plookup, gkey,
        codd=False, label=f"string L={sector.L},K={sector.max_depth}",
    )
    model["keys"] = keys
    model["depth"] = depth
    model["L"] = int(sector.L)
    model["K"] = int(sector.max_depth)
    return model


# Runtime: all Q physics is globally Gram-merged and Schur-eliminated ---------
def prepare_global_runtime(model):
    if USE_GPU:
        rt = {
            "nP": len(model["E_P"]),
            "E_P": cp.asarray(model["E_P"]),
            "VAC_P": cp.asarray(model["VAC_P"]),
            "W_PP": cpsparse.csr_matrix(model["W_PP"]),
            "source": cp.asarray(model["source_P"]),
            "kernels": [(lam, vac, cpsparse.csr_matrix(K)) for lam, vac, K in model["kernels"]],
        }
    else:
        rt = {
            "nP": len(model["E_P"]), "E_P": model["E_P"], "VAC_P": model["VAC_P"],
            "W_PP": model["W_PP"], "source": model["source_P"],
            "kernels": model["kernels"],
        }
    return rt


def _global_effective_eval(rt, u, trial_E, return_vector=False):
    e_vac = local_vacuum_energy(u)
    diag = rt["E_P"] - rt["VAC_P"] * e_vac

    # Assemble the energy-dependent global-Q self-energy once per nonlinear
    # iteration; Lanczos then sees one sparse matrix, not dozens of Q blocks.
    Sigma = None
    min_den = float("inf")
    for lam, vac, K in rt["kernels"]:
        den = trial_E - lam
        min_den = min(min_den, abs(float(den)))
        if abs(den) < 1e-9:
            raise RuntimeError(f"global Feshbach trial energy hit Q pole: |den|={abs(den):.3e}")
        term = (u * u / den) * K
        Sigma = term if Sigma is None else (Sigma + term)

    def mv(x):
        z = diag * x + u * (rt["W_PP"] @ x)
        if Sigma is not None:
            z = z + Sigma @ x
        return z

    r = source_lanczos_custom(mv, rt["source"], return_vector=return_vector)
    r["min_q_denominator"] = min_den
    return r


def _global_p_only_eval(rt, u):
    e_vac = local_vacuum_energy(u)
    diag = rt["E_P"] - rt["VAC_P"] * e_vac
    def mv(x):
        return diag * x + u * (rt["W_PP"] @ x)
    return source_lanczos_custom(mv, rt["source"], return_vector=False)


def global_feshbach_pole(rt, u):
    p0 = _global_p_only_eval(rt, u)
    E = p0["pole_energy"]
    prev_E = prev_F = None
    last = None
    for it in range(V5_MAX_FP):
        r = _global_effective_eval(rt, u, E, return_vector=False)
        F = r["pole_energy"] - E
        last = r
        if abs(F) < V5_FP_TOL and r["converged"]:
            break
        if prev_E is not None and abs(F - prev_F) > 1e-14:
            Enew = E - F * (E - prev_E) / (F - prev_F)
            if (not math.isfinite(Enew)) or abs(Enew - E) > 0.75:
                Enew = E + 0.5 * F
        else:
            Enew = E + 0.65 * F
        prev_E, prev_F = E, F
        E = Enew
    else:
        raise RuntimeError(f"global Feshbach fixed point failed at u={u}")

    E = last["pole_energy"]
    final = _global_effective_eval(rt, u, E, return_vector=True)
    fp_resid = abs(final["pole_energy"] - E)
    E = final["pole_energy"]
    pvec = final.pop("ritz_vector")

    e_vac = local_vacuum_energy(u)
    qnorm = 0.0
    for lam, vac, K in rt["kernels"]:
        den = E - lam
        Kp = K @ pvec
        val = _to_float(xp.dot(pvec, Kp))
        if val < -1e-8:
            raise RuntimeError(f"negative global-Q norm quadratic form {val:.3e}")
        qnorm += (u * u) * max(0.0, val) / (den * den)

    final["pole_residue_P"] = final["pole_residue"]
    final["pole_residue"] = final["pole_residue"] / (1.0 + qnorm)
    final["q_norm_ratio"] = qnorm
    final["feshbach_residual"] = fp_resid
    final["fixed_point_iterations"] = it + 1
    final["converged"] = bool(final["converged"] and fp_resid < 5 * V5_FP_TOL)
    return final


# Cold t3 firewall from P intermediates + globally merged Q kernels -----------
def validate_global_t3(model):
    states = model["states"]
    index = model["index"]
    E_P = model["E_P"]
    W = model["W_PP"]
    seed_face = 0
    pkey, psgn, _ = canonical_codd(B2[:, seed_face])
    ip = index[pkey]
    p_row = {int(k): float(v) for k, v in zip(W.getrow(ip).indices, W.getrow(ip).data)}
    plaquette_mask = np.asarray([plaquette_match(q) is not None for q in states], dtype=bool)
    errors = []
    rows = []
    for qf in range(P):
        if qf == seed_face:
            continue
        shared = np.flatnonzero((B2[:, seed_face] != 0) & (B2[:, qf] != 0))
        if len(shared) != 1:
            continue
        qkey, qsgn, _ = canonical_codd(B2[:, qf])
        if qkey not in index:
            continue
        iq = index[qkey]
        q_row = {int(k): float(v) for k, v in zip(W.getrow(iq).indices, W.getrow(iq).data)}
        coeff = 0.0
        for k in set(p_row).intersection(q_row):
            if plaquette_mask[k]:
                continue
            coeff += p_row[k] * q_row[k] / (E0_PLAQ - E_P[k])
        for lam, vac, K in model["kernels"]:
            coeff += float(K[ip, iq]) / (E0_PLAQ - lam)
        l = int(shared[0])
        incidence = int(B2[l, seed_face] * B2[l, qf])
        target = psgn * qsgn * incidence * T3_TARGET
        errors.append(abs(coeff - target))
        rows.append((qf, coeff, target))
    if len(rows) != 12:
        raise RuntimeError(f"global t3: expected 12 neighbors, got {len(rows)}")
    gate("global-Q Hamiltonian cold-reproduces all 12 t3 hoppings", max(errors) < 8e-12,
         f"max |cold-target|={max(errors):.3e}")
    return rows



# =============================================================================
# v5 FAST GLOBAL MERGE: collapse identical bright-Q identities before Gram work
# =============================================================================
def _sparse_pair_codd(q, b):
    qa, ba = _flux_sparse_key(q), _flux_sparse_key(b)
    pair = tuple(sorted((qa, ba)))
    pairc = tuple(sorted((_flux_sparse_key(-np.asarray(q, dtype=np.int8)),
                          _flux_sparse_key(-np.asarray(b, dtype=np.int8)))))
    return (pair, +1) if pair <= pairc else (pairc, -1)


def _sparse_pair_plain(q, b):
    return tuple(sorted((_flux_sparse_key(q), _flux_sparse_key(b))))


@dataclass
class _QIdentity:
    rep: ActionRec
    lam: Fraction
    vac: int
    norm: Fraction
    residue_group: tuple
    pair_key: tuple
    rep_sign: int
    coupling: dict


def _build_global_model(
    states, index, source, E_P, VAC_P,
    candidate_faces_fn, face_flux_fn, face_steps_fn, ordered_steps_fn,
    face_support_faces_obj, p_lookup_fn, group_key_fn,
    codd=False, label="sector",
):
    """
    Exact v5 construction.

    1. Collapse all magnetic histories that create the same normalized bright-Q
       eigenstate (same two-trace product modulo C and same H0 eigenvalue).
    2. Build the v4-equivalent baseline K = sum b_alpha b_alpha^T.
    3. Compute exact Haar/Fierz Gram overlaps only between DISTINCT Q identities
       sharing the same center residue and electric eigenvalue.
    4. Add b_alpha G_ab b_beta^T cross terms.  This is the global Q Gram merge.
    """
    t0 = time.time()
    nP = len(states)
    pp_rows, pp_cols, pp_vals = [], [], []
    identities = {}
    exact_topologies = set()
    raw_actions = c_even_actions = direct_P_actions = 0

    def action_detail(rec, lam=None, conjugate=False):
        q = states[rec.parent]
        parent_steps = ordered_steps_fn(q)
        fsteps = face_steps_fn(rec.face, rec.orient)
        if conjugate:
            parent_steps = _conjugate_steps(parent_steps)
            fsteps = _conjugate_steps(fsteps)
        raw = lx_tensor_product(lx_trace_state(parent_steps), lx_trace_state(fsteps))
        _, info = exact_action_spectrum(parent_steps, fsteps)
        b = (rec.orient * face_flux_fn(rec.face)).astype(np.int8)
        residue = mod3_reduce_flux(q + b)
        jP, psgn = p_lookup_fn(residue)
        pstate = None; ov = Fraction(0); psub = False
        if jP is not None:
            rsteps = ordered_steps_fn(residue)
            if conjugate:
                rsteps = _conjugate_steps(rsteps)
            pstate = lx_trace_state(rsteps)
            ov = exact_raw_p_overlap(raw, pstate)
            if lam is not None:
                psub = abs(float(lam) - float(E_P[jP])) < 2e-12 and ov != 0
        return {"raw": raw, "lams": info["lams"], "residue": residue,
                "jP": jP, "psgn": psgn, "pstate": pstate, "ov": ov, "psub": psub}

    report_every = max(1, nP // 10)
    for i, q in enumerate(states):
        parent_steps = ordered_steps_fn(q)
        cand = candidate_faces_fn(q)
        if V5_PROGRESS and nP > 10000 and (i == 0 or (i + 1) % report_every == 0):
            print(f"      {label} action pass {i+1:,}/{nP:,}; Q identities={len(identities):,}")
        for f in cand:
            bf = face_flux_fn(f)
            vac_union = len(cand | face_support_faces_obj[f])
            for orient in (-1, +1):
                b = (orient * bf).astype(np.int8)
                raw_actions += 1
                if codd and _pair_c_invariant(q, b):
                    c_even_actions += 1
                    continue
                fsteps = face_steps_fn(f, orient)
                sig, info = exact_action_spectrum(parent_steps, fsteps)
                exact_topologies.add(sig)
                raw = lx_tensor_product(lx_trace_state(parent_steps), lx_trace_state(fsteps))
                residue = mod3_reduce_flux(q + b)
                jP, psgn = p_lookup_fn(residue)
                pstate = None; ov = Fraction(0)
                if jP is not None:
                    rsteps = ordered_steps_fn(residue)
                    pstate = lx_trace_state(rsteps)
                    ov = exact_raw_p_overlap(raw, pstate)
                    if ov:
                        pp_rows.append(i); pp_cols.append(jP); pp_vals.append(-float(psgn) * float(ov))
                        direct_P_actions += 1

                if codd:
                    pair_key, qsign = _sparse_pair_codd(q, b)
                else:
                    pair_key, qsign = _sparse_pair_plain(q, b), +1
                rgroup = group_key_fn(residue)

                for lam, w in info["spec"]:
                    qnorm = Fraction(w)
                    if jP is not None and abs(float(lam) - float(E_P[jP])) < 2e-12 and ov:
                        qnorm -= ov * ov
                    if qnorm < 0:
                        raise RuntimeError(f"{label}: negative Q norm after P subtraction")
                    if qnorm == 0:
                        continue
                    ikey = (pair_key, Fraction(lam))
                    rec = ActionRec(i, int(f), int(orient), int(vac_union), int(qsign))
                    amp = -float(qsign) * math.sqrt(float(qnorm)) if codd else -math.sqrt(float(qnorm))
                    if ikey not in identities:
                        identities[ikey] = _QIdentity(
                            rep=rec, lam=Fraction(lam), vac=int(vac_union), norm=Fraction(qnorm),
                            residue_group=rgroup, pair_key=pair_key, rep_sign=int(qsign), coupling={i: amp}
                        )
                    else:
                        ident = identities[ikey]
                        if ident.vac != int(vac_union) or ident.norm != Fraction(qnorm):
                            raise RuntimeError(f"{label}: identical Q state received inconsistent norm/vacuum metadata")
                        ident.coupling[i] = ident.coupling.get(i, 0.0) + amp

    W_PP = coo_matrix((pp_vals, (pp_rows, pp_cols)), shape=(nP, nP), dtype=np.float64).tocsr()
    W_PP.sum_duplicates()
    asym = W_PP - W_PP.T
    asymmetry = 0.0 if asym.nnz == 0 else float(np.max(np.abs(asym.data)))
    if asymmetry > 2e-12:
        raise RuntimeError(f"{label}: P-space magnetic matrix asymmetry={asymmetry:.3e}")

    # Build identity collision groups by exact center residue + electric energy.
    by_residue = defaultdict(list)
    id_list = list(identities.values())
    for a, ident in enumerate(id_list):
        by_residue[(ident.residue_group, ident.lam)].append(a)

    kernel_rows = defaultdict(list); kernel_cols = defaultdict(list); kernel_vals = defaultdict(list)

    def outer_add(kkey, ca, cb, factor):
        if factor == 0:
            return
        for i, ai in ca.items():
            for j, bj in cb.items():
                v = factor * ai * bj
                if v:
                    kernel_rows[kkey].append(int(i)); kernel_cols[kkey].append(int(j)); kernel_vals[kkey].append(float(v))

    # v4-equivalent orthonormal-Q baseline: each distinct bright identity contributes b b^T.
    for ident in id_list:
        outer_add((ident.lam, ident.vac), ident.coupling, ident.coupling, 1.0)

    checked_pairs = nonzero_cross = vac_mismatch = gram_nullity = 0
    gram_rank_total = gram_dim_total = 0
    min_gram_eval = 0.0; max_norm_overlap = 0.0
    pair_topologies_seen = set()

    collision_items = [(k, v) for k, v in by_residue.items() if len(v) > 1]
    for cg, ((rgroup, lam), ids) in enumerate(collision_items):
        n = len(ids)
        G = np.eye(n, dtype=np.float64)
        details = {}
        for aa, aid in enumerate(ids):
            ident = id_list[aid]
            details[aid] = action_detail(ident.rep, lam=lam, conjugate=False)
        for aa in range(n):
            aid = ids[aa]; A = id_list[aid]; da = details[aid]
            rka = _flux_sparse_key(da["residue"])
            for bb in range(aa + 1, n):
                bid = ids[bb]; Bident = id_list[bid]; db = details[bid]
                rkb = _flux_sparse_key(db["residue"])
                checked_pairs += 1
                normal = Fraction(0); crossc = Fraction(0)
                if rka == rkb:
                    normal = exact_q_overlap(
                        da["raw"], da["pstate"], da["ov"], da["psub"],
                        db["raw"], db["pstate"], db["ov"], db["psub"], lam, db["lams"])
                if codd and rka == _flux_sparse_key(-db["residue"]):
                    dbc = action_detail(Bident.rep, lam=lam, conjugate=True)
                    crossc = exact_q_overlap(
                        da["raw"], da["pstate"], da["ov"], da["psub"],
                        dbc["raw"], dbc["pstate"], dbc["ov"], dbc["psub"], lam, dbc["lams"])
                rawg = normal - crossc if codd else normal
                if rawg == 0:
                    continue
                if A.vac != Bident.vac:
                    vac_mismatch += 1
                    raise RuntimeError(
                        f"{label}: nonzero global-Q overlap connects linked-vacuum counts {A.vac} and {Bident.vac}"
                    )
                # Canonical normalized bright-Q overlap.  Couplings carry the same
                # canonical signs, so the final P kernel reproduces the raw C- sum.
                g = float(rawg) / math.sqrt(float(A.norm) * float(Bident.norm))
                if codd:
                    g *= A.rep_sign * Bident.rep_sign
                if abs(g) < 1e-14:
                    continue
                nonzero_cross += 1
                max_norm_overlap = max(max_norm_overlap, abs(g))
                G[aa, bb] = G[bb, aa] = g
                kkey = (A.lam, A.vac)
                if V5_GLOBAL_GRAM:
                    outer_add(kkey, A.coupling, Bident.coupling, g)
                    outer_add(kkey, Bident.coupling, A.coupling, g)

        if np.any(np.abs(G - np.eye(n)) > 1e-14):
            ev = np.linalg.eigvalsh(0.5 * (G + G.T))
            min_gram_eval = min(min_gram_eval, float(ev.min()))
            tol = V5_GRAM_RANK_TOL * max(1.0, float(ev.max()))
            rank = int(np.sum(ev > tol))
            gram_nullity += n - rank; gram_rank_total += rank; gram_dim_total += n
        else:
            gram_rank_total += n; gram_dim_total += n

    if min_gram_eval < -2e-9:
        raise RuntimeError(f"{label}: global Q identity Gram not PSD; min={min_gram_eval:.3e}")
    if max_norm_overlap > 1.0 + 2e-9:
        raise RuntimeError(f"{label}: normalized Q identity overlap exceeds one: {max_norm_overlap}")

    kernels = []
    for kkey in sorted(kernel_rows, key=lambda x: (float(x[0]), x[1])):
        K = coo_matrix((kernel_vals[kkey], (kernel_rows[kkey], kernel_cols[kkey])), shape=(nP, nP), dtype=np.float64).tocsr()
        K.sum_duplicates()
        Ka = K - K.T
        err = 0.0 if Ka.nnz == 0 else float(np.max(np.abs(Ka.data)))
        if err > 3e-11:
            raise RuntimeError(f"{label}: Gram-Feshbach kernel asymmetry={err:.3e}")
        kernels.append((float(kkey[0]), int(kkey[1]), K))

    return {
        "states": states, "index": index, "source_P": np.asarray(source, dtype=np.float64),
        "E_P": np.asarray(E_P, dtype=np.float64), "VAC_P": np.asarray(VAC_P, dtype=np.float64),
        "W_PP": W_PP, "kernels": kernels, "build_seconds": time.time() - t0,
        "asymmetry": asymmetry, "raw_actions": raw_actions,
        "action_channels": sum(len(x.coupling) for x in id_list), "q_identities": len(id_list),
        "exact_topologies": len(exact_topologies), "collision_groups": len(collision_items),
        "gram_pairs_checked": checked_pairs, "gram_nonzero_cross": nonzero_cross,
        "gram_nullity": gram_nullity, "gram_rank_total": gram_rank_total, "gram_dim_total": gram_dim_total,
        "gram_min_eig": min_gram_eval, "gram_max_normalized_overlap": max_norm_overlap,
        "vac_mismatch": vac_mismatch, "c_even_actions": c_even_actions, "direct_P_actions": direct_P_actions,
    }


# =============================================================================

# Fast numerical Haar tensor contractor for GLOBAL Gram overlaps only.
# Exact/rational local certificates continue to use lx_haar_inner.
import opt_einsum as oe

_FAST_T11 = np.zeros((3,3,3,3), dtype=np.float64)
for _i,_j,_k,_l in itertools.product(range(3), repeat=4):
    if _i == _k and _j == _l:
        _FAST_T11[_i,_j,_k,_l] = 1.0/3.0

_FAST_T22 = np.zeros((3,3,3,3,3,3,3,3), dtype=np.float64)
_fast_perms = ((0,1),(1,0))
_fast_W = ((1.0/8.0, -1.0/24.0), (-1.0/24.0, 1.0/8.0))
for _inds in itertools.product(range(3), repeat=8):
    _ur=(_inds[0],_inds[2]); _uc=(_inds[1],_inds[3])
    _br=(_inds[4],_inds[6]); _bc=(_inds[5],_inds[7])
    _val=0.0
    for _si,_sig in enumerate(_fast_perms):
        for _ti,_tau in enumerate(_fast_perms):
            if all(_ur[r] == _br[_sig[r]] and _uc[r] == _bc[_tau[r]] for r in range(2)):
                _val += _fast_W[_si][_ti]
    _FAST_T22[_inds] = _val

_FAST_EPS = np.zeros((3,3,3), dtype=np.float64)
for _perm in itertools.permutations(range(3)):
    _inv = sum(_perm[i] > _perm[j] for i in range(3) for j in range(i+1,3))
    _FAST_EPS[_perm] = -1.0 if _inv % 2 else 1.0
# axis order r0,c0,r1,c1,r2,c2
_FAST_T30 = np.einsum('abc,def->adbecf', _FAST_EPS, _FAST_EPS).reshape((3,)*6) / 6.0

@lru_cache(maxsize=300000)
def _fast_haar_canon(a, b):
    occ, part = lx_combine_bra_ket(a, b)
    bylink = defaultdict(lambda: {True: [], False: []})
    for i,(link,typ) in enumerate(occ):
        bylink[int(link)][bool(typ)].append(i)
    args=[]
    for _,g in bylink.items():
        U,B = g[True],g[False]
        if len(U)==len(B)==1:
            positions=U+B; ten=_FAST_T11
        elif len(U)==len(B)==2:
            positions=U+B; ten=_FAST_T22
        elif (len(U),len(B)) in ((3,0),(0,3)):
            positions=U if len(U)==3 else B; ten=_FAST_T30
        else:
            # Defensive exact fallback for any future deeper occurrence pattern.
            return float(lx_haar_inner(a,b))
        inds=[]
        for p0 in positions:
            inds.extend((int(part[2*p0]), int(part[2*p0+1])))
        args.extend((ten, inds))
    if not args:
        return float(N ** len(set(part)))
    return float(oe.contract(*args, [], optimize='greedy'))


def _fast_haar_joint(a,b):
    aa,bb=_joint_canon_states(a,b)
    return _fast_haar_canon(aa,bb)


def _vec_inner_fast(v,w):
    total=0.0
    for a,ca in v.items():
        fca=float(ca)
        for b,cb in w.items():
            total += fca * float(cb) * _fast_haar_joint(a,b)
    return total


def validate_fast_haar_tensor_contract():
    lid_global={(v,d):i for i,(v,d) in enumerate(links)}
    samples=[]
    q=B2[:,0].copy(); ps=ordered_loop_steps(q,links,shift)
    wanted=set()
    for f in candidate_faces(q):
        bf=B2[:,f]
        for o in (-1,+1):
            sh=len(np.flatnonzero((q!=0)&((o*bf)!=0)))
            if sh in wanted: continue
            fs=face_steps_generic(f,o,faces,lid_global,shift)
            raw=lx_tensor_product(lx_trace_state(ps),lx_trace_state(fs))
            basis=lx_closure(raw,max_states=64)
            samples.append(basis[:min(5,len(basis))]); wanted.add(sh)
    err=0.0; ncheck=0
    for basis in samples:
        for a in basis:
            for b in basis:
                ex=float(lx_haar_inner(a,b)); ff=_fast_haar_joint(a,b)
                err=max(err,abs(ex-ff)); ncheck+=1
    gate("tensor Haar contractor matches exact rational local moments", err < 2e-12, f"{ncheck} overlaps; max error={err:.3e}")

# v5 FINAL GLOBAL MERGE: JOINT LINK-CASIMIR RESOLUTION
# =============================================================================
# Total H0 eigenvalues can be accidentally degenerate.  Global Haar overlap is
# block-diagonal in the full Peter-Weyl irrep carried by EACH physical link, so
# v5 refines every raw magnetic action into simultaneous eigenchannels of the
# commuting link electric Casimirs before any global Gram contraction.
#
# Low-occurrence SU(3) link labels used here:
#   +1  = F,        -1 = Fbar,
#   +2  = 6,        -2 = 6bar,
#    8  = adjoint,   0 = singlet (omitted from the physical support signature).
#
# This is exactly the joint-Casimir refinement implicit in the certified v0.6
# electric-resolvent machinery, now used as a global orthogonality filter.

_REP_CONJ = {+1: -1, -1: +1, +2: -2, -2: +2, 8: 8, 0: 0}
_REP_E = {+1: Fraction(2,3), -1: Fraction(2,3), +2: Fraction(5,3), -2: Fraction(5,3), 8: Fraction(3,2), 0: Fraction(0)}


def _rep_sig_conj(sig):
    return tuple(sorted((int(l), int(_REP_CONJ[int(r)])) for l, r in sig if _REP_CONJ[int(r)] != 0))


def _rep_sig_codd(sig):
    sig = tuple(sorted((int(l), int(r)) for l, r in sig if int(r) != 0))
    cs = _rep_sig_conj(sig)
    return sig if sig <= cs else cs


def _rep_sig_from_flux(q):
    q = np.asarray(q, dtype=np.int8)
    return tuple((int(l), +1 if int(q[l]) > 0 else -1) for l in np.flatnonzero(q))


def _Hlink_action(state, target_link):
    fac0, st = lx_simplify_unitarity(state)
    out = defaultdict(Fraction)
    items = [(i, typ) for i, (link, typ) in enumerate(st.occ) if int(link) == int(target_link)]
    if not items:
        return {}
    out[st] += fac0 * Fraction(len(items), 1) * Fraction(2, 3)
    for (i, t1), (j, t2) in itertools.combinations(items, 2):
        r1, r2 = 2*i, 2*j
        if t1 == t2:
            raw = LXState(st.occ, lx_swap_rows(st.part, r1, r2))
            fac, z = lx_simplify_unitarity(raw)
            out[z] += fac0 * fac * Fraction(1, 2)
            out[st] -= fac0 * Fraction(1, 2*N)
        else:
            raw = LXState(st.occ, lx_opposite_reconnect(st.part, r1, r2))
            fac, z = lx_simplify_unitarity(raw)
            out[z] -= fac0 * fac * Fraction(1, 2)
            out[st] += fac0 * Fraction(1, 2*N)
    return {z: c for z, c in out.items() if c}


def _vec_Hlink(v, link):
    out = defaultdict(Fraction)
    for st, c in v.items():
        for z, a in _Hlink_action(st, link).items():
            out[z] += c * a
    return {z: c for z, c in out.items() if c}


def _project_link(v, link, eig, eigs):
    eig = Fraction(eig); eigs = tuple(Fraction(x) for x in eigs)
    outv = dict(v)
    for mu in eigs:
        if mu == eig:
            continue
        den = eig - mu
        hv = _vec_Hlink(outv, link)
        nxt = defaultdict(Fraction)
        for st, c in hv.items(): nxt[st] += c / den
        for st, c in outv.items(): nxt[st] -= mu * c / den
        outv = {st: c for st, c in nxt.items() if c}
    return outv


def _vec_inner(v, w):
    total = Fraction(0)
    for a, ca in v.items():
        for b, cb in w.items():
            # Canonicalize the JOINT physical-link equality pattern first so
            # translated/isomorphic local recouplings share the same exact Haar cache.
            total += ca * cb * _haar_joint(a, b)
    return total


@lru_cache(maxsize=500000)
def _action_sig_map(parent_steps, pface_steps):
    """Return invariant local topology and physical shared links in canonical slot order."""
    p = len(parent_steps)
    pmap = {int(l): (i, int(sg)) for i, (l, sg) in enumerate(parent_steps)}
    triples = []
    for j, (l, sg2) in enumerate(pface_steps):
        l = int(l)
        if l in pmap:
            i, sg1 = pmap[l]
            triples.append((i, j, sg1 * int(sg2), l))
    best = None; best_slots = None
    for rev in (0, 1):
        for rp in range(p):
            for rf in range(4):
                transformed = []
                for i, j, rel, l in triples:
                    if not rev:
                        ip, jp = (i-rp) % p, (j-rf) % 4
                    else:
                        ip, jp = (-i-rp) % p, (-j-rf) % 4
                    transformed.append((ip, jp, rel, l))
                keytrip = tuple(sorted((ip, jp, rel) for ip, jp, rel, _ in transformed))
                key = (p, keytrip)
                slots = [l for _, _, _, l in sorted(transformed, key=lambda x: (x[0], x[1], x[2], x[3]))]
                tie = (key, tuple(slots))
                # key determines topology; deterministic transform tie-break independent
                # of physical link ids is rev/rp/rf.
                cand = (key, rev, rp, rf)
                if best is None or cand < best[0]:
                    best = (cand, key); best_slots = slots
    return best[1], tuple(best_slots)


@lru_cache(maxsize=500000)
def _shared_options(parent_steps, pface_steps, slots):
    pd = {int(l): int(s) for l, s in parent_steps}
    fd = {int(l): int(s) for l, s in pface_steps}
    out = []
    for l in slots:
        a, b = pd[int(l)], fd[int(l)]
        if a * b > 0:
            out.append((Fraction(2,3), Fraction(5,3)))
        else:
            out.append((Fraction(0), Fraction(3,2)))
    return tuple(out)


@lru_cache(maxsize=1000000)
def _rep_signature_for_bits(parent_steps, pface_steps, slots, bits):
    pd = {int(l): int(s) for l, s in parent_steps}
    fd = {int(l): int(s) for l, s in pface_steps}
    shared = set(map(int, slots))
    sig = []
    # Unique-link fundamental representations.
    all_links = sorted(set(pd) | set(fd))
    for l in all_links:
        if l in shared:
            continue
        s = pd.get(l, fd.get(l))
        sig.append((l, +1 if s > 0 else -1))
    # Shared-link irreps selected by the joint Casimir projector.
    for l, bit in zip(slots, bits):
        a, b = pd[int(l)], fd[int(l)]
        if a * b > 0:
            if a > 0:
                rep = -1 if bit == 0 else +2   # FF -> Fbar or 6
            else:
                rep = +1 if bit == 0 else -2   # FbarFbar -> F or 6bar
        else:
            rep = 0 if bit == 0 else 8         # F Fbar -> 1 or 8
        if rep != 0:
            sig.append((int(l), int(rep)))
    return tuple(sorted(sig))


def _rep_energy(sig):
    return sum((_REP_E[int(r)] for _, r in sig), Fraction(0))


GLOBAL_JOINT_TEMPLATE = {}

@lru_cache(maxsize=500000)
def _joint_template(parent_steps, pface_steps):
    topo, slots = _action_sig_map(parent_steps, pface_steps)
    if topo not in GLOBAL_JOINT_TEMPLATE:
        raw = lx_tensor_product(lx_trace_state(parent_steps), lx_trace_state(pface_steps))
        options = _shared_options(parent_steps, pface_steps, slots)
        rows = []
        for bits in itertools.product((0,1), repeat=len(slots)):
            v = {raw: Fraction(1)}
            for l, bit, eigs in zip(slots, bits, options):
                v = _project_link(v, int(l), eigs[int(bit)], eigs)
                if not v:
                    break
            if not v:
                continue
            w = _vec_inner(v, v)
            if w == 0:
                continue
            sig = _rep_signature_for_bits(parent_steps, pface_steps, slots, bits)
            rows.append((tuple(map(int,bits)), w, _rep_energy(sig)))

        # Exact joint-projector closure audits.
        raw_norm = lx_haar_inner(raw, raw)
        if sum((w for _,w,_ in rows), Fraction(0)) != raw_norm:
            raise RuntimeError(f"joint Casimir projectors do not resolve raw norm for topology {topo}")
        _, totalspec, _, _ = lx_spectral_measure(raw)
        agg = defaultdict(Fraction)
        for _, w, e in rows: agg[e] += w
        specdict = {_sp_to_frac(lam): _sp_to_frac(w) for lam,w in totalspec}
        if dict(agg) != specdict:
            raise RuntimeError(f"joint Casimir decomposition disagrees with total H0 spectrum for topology {topo}: {dict(agg)} vs {specdict}")
        GLOBAL_JOINT_TEMPLATE[topo] = tuple(rows)
    return topo, slots, GLOBAL_JOINT_TEMPLATE[topo]


@dataclass(frozen=True)
class JointActionRec:
    parent: int
    face: int
    orient: int
    vac: int
    bits: tuple
    norm_num: int
    norm_den: int

    @property
    def norm(self):
        return Fraction(self.norm_num, self.norm_den)


def _build_global_model(
    states, index, source, E_P, VAC_P,
    candidate_faces_fn, face_flux_fn, face_steps_fn, ordered_steps_fn,
    face_support_faces_obj, p_lookup_fn, group_key_fn,
    codd=False, label="sector",
):
    t0 = time.time(); nP = len(states)
    # Geometry caches: global Gram work revisits the same parent/action many times.
    # Cache exact ordered trace steps and candidate faces once per P state, and
    # oriented plaquette steps once per face/orientation.
    state_steps = [tuple(ordered_steps_fn(q)) for q in states]
    cand_cache = [candidate_faces_fn(q) for q in states]
    _face_steps_cache = {}
    def fs_cached(face, orient):
        key = (int(face), int(orient))
        if key not in _face_steps_cache:
            _face_steps_cache[key] = tuple(face_steps_fn(int(face), int(orient)))
        return _face_steps_cache[key]

    pp_rows=[]; pp_cols=[]; pp_vals=[]
    kernel_diag = {}  # (bare joint H0 energy, 0)-> array; Q vacuum shift is NOT basis-labelled
    collisions = _CollisionStore()
    exact_topologies=set(); raw_actions=joint_channels=direct_P_actions=c_even_actions=0

    # Cache action metadata used by collision reconstruction.
    def base_detail(parent, face, orient):
        q = states[parent]
        ps = ordered_steps_fn(q); fs = face_steps_fn(face, orient)
        raw = lx_tensor_product(lx_trace_state(ps), lx_trace_state(fs))
        b = (orient * face_flux_fn(face)).astype(np.int8)
        residue = mod3_reduce_flux(q + b)
        jP, psgn = p_lookup_fn(residue)
        pstate=None; ov=Fraction(0)
        if jP is not None:
            pstate = lx_trace_state(ordered_steps_fn(residue))
            ov = exact_raw_p_overlap(raw, pstate)
        topo, slots, tmpl = _joint_template(ps, fs)
        return q, ps, fs, raw, residue, jP, psgn, pstate, ov, topo, slots, tmpl

    report_every=max(1,nP//10)
    for i,q in enumerate(states):
        ps=state_steps[i]; cand=cand_cache[i]
        if V5_PROGRESS and nP>10000 and (i==0 or (i+1)%report_every==0):
            print(f"      {label} joint pass {i+1:,}/{nP:,}; channels={joint_channels:,}")
        for f in cand:
            bf=face_flux_fn(f); vac=len(cand | face_support_faces_obj[f])
            for orient in (-1,+1):
                b=(orient*bf).astype(np.int8); raw_actions+=1
                if codd and _pair_c_invariant(q,b):
                    c_even_actions+=1; continue
                fs=fs_cached(f,orient)
                raw=lx_tensor_product(lx_trace_state(ps),lx_trace_state(fs))
                residue=mod3_reduce_flux(q+b); jP,psgn=p_lookup_fn(residue)
                pstate=None; ov=Fraction(0); psig=None
                if jP is not None:
                    pstate=lx_trace_state(ordered_steps_fn(residue)); ov=exact_raw_p_overlap(raw,pstate)
                    psig=_rep_sig_from_flux(residue)
                    if ov:
                        pp_rows.append(i); pp_cols.append(jP); pp_vals.append(-float(psgn)*float(ov)); direct_P_actions+=1
                topo,slots,tmpl=_joint_template(ps,fs); exact_topologies.add(topo)
                p_hit=False
                for bits,w,lam_template in tmpl:
                    sig=_rep_signature_for_bits(ps,fs,slots,bits)
                    lam=_rep_energy(sig)
                    if lam != lam_template:
                        raise RuntimeError("joint representation energy changed under topology mapping")
                    qnorm=Fraction(w)
                    if ov and psig==sig:
                        qnorm-=ov*ov; p_hit=True
                    if qnorm<0: raise RuntimeError(f"{label}: negative joint Q norm")
                    if qnorm==0: continue
                    kkey=(lam,0)
                    if kkey not in kernel_diag: kernel_diag[kkey]=np.zeros(nP,dtype=np.float64)
                    kernel_diag[kkey][i]+=float(qnorm); joint_channels+=1
                    gsig=_rep_sig_codd(sig) if codd else sig
                    collisions.add((gsig,lam),JointActionRec(i,int(f),int(orient),int(vac),tuple(bits),qnorm.numerator,qnorm.denominator))
                if ov and not p_hit:
                    raise RuntimeError(f"{label}: direct P component not found in any joint-Casimir channel")

    W_PP=coo_matrix((pp_vals,(pp_rows,pp_cols)),shape=(nP,nP),dtype=np.float64).tocsr(); W_PP.sum_duplicates()
    asym=W_PP-W_PP.T; asymmetry=0.0 if asym.nnz==0 else float(np.max(np.abs(asym.data)))
    if asymmetry>2e-12: raise RuntimeError(f"{label}: P magnetic matrix asymmetry={asymmetry:.3e}")

    cross_rows=defaultdict(list);cross_cols=defaultdict(list);cross_vals=defaultdict(list)
    checked_pairs=nonzero_cross=vac_mismatch=gram_nullity=0;gram_rank_total=gram_dim_total=0
    min_gram_eval=0.0;max_norm_overlap=0.0

    def joint_vec(rec, conjugate=False):
        q=states[rec.parent]; ps=state_steps[rec.parent]; fs=fs_cached(rec.face,rec.orient)
        topo,slots,tmpl=_joint_template(ps,fs)
        bit_by_link={int(l):int(b) for l,b in zip(slots,rec.bits)}
        if conjugate:
            ps=tuple(_conjugate_steps(ps)); fs=tuple(_conjugate_steps(fs))
            topo2,slots2,tmpl2=_joint_template(ps,fs)
            bits2=tuple(bit_by_link[int(l)] for l in slots2)
            bits=bits2; slots=slots2
        else:
            bits=rec.bits
        raw=lx_tensor_product(lx_trace_state(ps),lx_trace_state(fs))
        options=_shared_options(ps,fs,slots)
        v={raw:Fraction(1)}
        for l,bit,eigs in zip(slots,bits,options):
            v=_project_link(v,int(l),eigs[int(bit)],eigs)
        bflux=(rec.orient*face_flux_fn(rec.face)).astype(np.int8)
        residue=mod3_reduce_flux(states[rec.parent]+bflux)
        if conjugate: residue=-residue
        jP,psgn=p_lookup_fn(residue)
        if jP is not None:
            rsteps=ordered_steps_fn(residue)
            if conjugate: rsteps=_conjugate_steps(-residue) if False else rsteps
            pstate=lx_trace_state(rsteps)
            ov=exact_raw_p_overlap(raw,pstate)
            sig=_rep_signature_for_bits(ps,fs,slots,bits)
            if ov and _rep_sig_from_flux(residue)==sig:
                v=dict(v);v[pstate]=v.get(pstate,Fraction(0))-ov
                if v[pstate]==0: del v[pstate]
        return v, residue

    _rec_sig_cache = {}
    def rec_sig(rec):
        key = (rec.parent, rec.face, rec.orient, rec.bits)
        z = _rec_sig_cache.get(key)
        if z is None:
            ps = state_steps[rec.parent]
            fs = fs_cached(rec.face, rec.orient)
            _, slots, _ = _joint_template(ps, fs)
            z = _rep_signature_for_bits(ps, fs, slots, rec.bits)
            _rec_sig_cache[key] = z
        return z

    _cg_items = list(collisions.collision_groups.items())
    _cg_t0 = time.time()
    for _cgi, ((gsig,lam),recs) in enumerate(_cg_items):
        if V5_PROGRESS and (_cgi == 0 or (_cgi+1) % max(1, len(_cg_items)//10) == 0):
            print(f"      {label} Gram pass {_cgi+1:,}/{len(_cg_items):,}; elapsed={time.time()-_cg_t0:.1f}s; nonzero={nonzero_cross:,}")
        n=len(recs); G=np.eye(n,dtype=np.float64); cache_vec={}
        for a in range(n):
            ra=recs[a]
            va,resa=joint_vec(ra,False); cache_vec[(a,False)]=(va,resa)
            # Self norm is the exact rational joint-projector weight already certified in _joint_template.
            for b in range(a+1,n):
                rb=recs[b]; checked_pairs+=1
                if (b,False) not in cache_vec: cache_vec[(b,False)]=joint_vec(rb,False)
                vb,resb=cache_vec[(b,False)]
                rawg=Fraction(0)
                siga = rec_sig(ra)
                sigb = rec_sig(rb)
                if siga == sigb:
                    rawg=_vec_inner_fast(va,vb)
                if codd:
                    if siga==_rep_sig_conj(sigb):
                        if (b,True) not in cache_vec: cache_vec[(b,True)]=joint_vec(rb,True)
                        vbc,_=cache_vec[(b,True)]
                        rawg-=_vec_inner_fast(va,vbc)
                if abs(rawg) < 5e-13: continue
                nonzero_cross+=1
                if ra.vac!=rb.vac:
                    # A globally recoupled Q vector has no basis-invariant "number of
                    # vacuum plaquettes" inherited from one generating history.  Treating
                    # that history label as a Q-energy shift is therefore invalid.  v5
                    # keeps Q denominators at their exact bare H0 energies and performs
                    # linked vacuum subtraction only in the retained P sector.  The count
                    # below is a diagnostic of precisely the ambiguity that v4 could not
                    # resolve.
                    vac_mismatch+=1
                gf=float(rawg); normed=gf/math.sqrt(float(ra.norm)*float(rb.norm)); max_norm_overlap=max(max_norm_overlap,abs(normed))
                G[a,b]=G[b,a]=normed
                kkey=(lam,0)
                if ra.parent==rb.parent:
                    cross_rows[kkey].append(ra.parent);cross_cols[kkey].append(rb.parent);cross_vals[kkey].append(2*gf)
                else:
                    cross_rows[kkey].extend((ra.parent,rb.parent));cross_cols[kkey].extend((rb.parent,ra.parent));cross_vals[kkey].extend((gf,gf))
        if np.any(np.abs(G-np.eye(n))>1e-14):
            ev=np.linalg.eigvalsh((G+G.T)/2);min_gram_eval=min(min_gram_eval,float(ev.min()))
            tol=V5_GRAM_RANK_TOL*max(1.0,float(ev.max()));rank=int(np.sum(ev>tol));gram_nullity+=n-rank;gram_rank_total+=rank;gram_dim_total+=n
        else: gram_rank_total+=n;gram_dim_total+=n

    if min_gram_eval < -2e-9: raise RuntimeError(f"{label}: joint global Gram not PSD min={min_gram_eval:.3e}")
    if max_norm_overlap>1+2e-9: raise RuntimeError(f"{label}: normalized joint overlap >1: {max_norm_overlap}")

    kernels=[]
    for kkey in sorted(kernel_diag,key=lambda x:(float(x[0]),x[1])):
        d=kernel_diag[kkey];di=np.flatnonzero(np.abs(d)>0);rows=list(map(int,di));cols=list(map(int,di));vals=list(map(float,d[di]))
        if V5_GLOBAL_GRAM and kkey in cross_rows:
            rows.extend(cross_rows[kkey]);cols.extend(cross_cols[kkey]);vals.extend(cross_vals[kkey])
        K=coo_matrix((vals,(rows,cols)),shape=(nP,nP),dtype=np.float64).tocsr();K.sum_duplicates()
        Ka=K-K.T;err=0 if Ka.nnz==0 else float(np.max(np.abs(Ka.data)))
        if err>3e-11: raise RuntimeError(f"{label}: joint Feshbach kernel asymmetry={err:.3e}")
        kernels.append((float(kkey[0]),int(kkey[1]),K))

    return {"states":states,"index":index,"source_P":np.asarray(source,dtype=np.float64),"E_P":np.asarray(E_P,dtype=np.float64),"VAC_P":np.asarray(VAC_P,dtype=np.float64),
            "W_PP":W_PP,"kernels":kernels,"build_seconds":time.time()-t0,"asymmetry":asymmetry,"raw_actions":raw_actions,"action_channels":joint_channels,
            "exact_topologies":len(exact_topologies),"collision_groups":len(collisions.collision_groups),"gram_pairs_checked":checked_pairs,"gram_nonzero_cross":nonzero_cross,
            "gram_nullity":gram_nullity,"gram_rank_total":gram_rank_total,"gram_dim_total":gram_dim_total,"gram_min_eig":min_gram_eval,
            "gram_max_normalized_overlap":max_norm_overlap,"vac_mismatch":vac_mismatch,"c_even_actions":c_even_actions,"direct_P_actions":direct_P_actions,
            # v9 audit hooks: these are the actual exact joint-Casimir projected Q action records.
            "v9_collisions":collisions,"v9_joint_vec":joint_vec,"v9_rec_sig":rec_sig,"v9_state_steps":state_steps,
            "v9_cand_cache":cand_cache,"v9_fs_cached":fs_cached,"v9_codd":codd,"v9_face_flux_fn":face_flux_fn,
            "v9_face_support_faces_obj":face_support_faces_obj,"v9_group_key_fn":group_key_fn}



# =============================================================================
# v8: EXACT SU(3) LOCAL-VACUUM CHARACTER CLOSURE + GLOBAL-Q MASS PRODUCTION
# =============================================================================
#
# IMPORTANT CORRECTION TO v7
# --------------------------
# v7 attributed the v5 O(u^3) mass defect to a missing first W_QQ moment and
# calibrated a scalar omega_Q from the known m3 coefficient.  That diagnosis is
# not correct.  In SU(3), the local vacuum has a cubic determinant process:
#
#   <+|M|0> = sqrt(2),   <+|M|+> = 1,   E_+ = 8/3,
#
# so for W=-M
#
#   e_vac(u) = -(3/4) u^2 -(9/32) u^3 + O(u^4).
#
# v5's two-state local_vacuum_energy() contains the exact -3/4 u^2 term but is
# even in u and therefore misses -9/32 u^3.  A plaquette excitation has 13
# linked vacuum embeddings, so the missing excitation-energy contribution is
#
#   +13*(9/32) = 117/32,
#
# which is exactly the observed v5 m3 defect.  v8 therefore does NOT use the v7
# fitted omega_Q.  Instead it diagonalizes the exact single-plaquette SU(3)
# character Hamiltonian in a systematically enlarged irrep Krylov space and uses
# its ground-state energy as the linked P-sector vacuum counterterm.
#
# This is first-principles group theory, not matching to the continuum mass and
# not matching to m3.  The known m2/m3 coefficients are blind regression gates.
#
# v8 is MASS-FIRST.  The string sector needs its own third-order linked-cluster
# operator closure; simply replacing the string vacuum scalar by the local
# character result does NOT reproduce s3=-61/408 and is therefore deliberately
# not used here to manufacture a ratio.
# =============================================================================

V8_GLUE_DEPTHS = tuple(int(x) for x in os.environ.get("V8_GLUE_DEPTHS", "1,2").split(",") if x.strip())
V8_VAC_DEPTH = int(os.environ.get("V8_VAC_DEPTH", "5"))
V8_VAC_DEPTHS = tuple(int(x) for x in os.environ.get("V8_VAC_DEPTHS", "1,2,3,4,5").split(",") if x.strip())
V8_C3_H = float(os.environ.get("V8_C3_H", "0.002"))
V8_M3_TOL = float(os.environ.get("V8_M3_TOL", "8e-6"))
V8_VAC_TOL = float(os.environ.get("V8_VAC_TOL", "5e-7"))
V8_PROGRESS = int(os.environ.get("V8_PROGRESS", "1"))

M2_EX = 11.0/306.0
M3_EX = -109151.0/249696.0
EV2_EX = -3.0/4.0
EV3_EX = -9.0/32.0


def su3_c2_pq(p, q):
    p=int(p); q=int(q)
    return (p*p + q*q + p*q + 3*p + 3*q) / 3.0


def su3_fuse_fundamental(rep):
    p,q=map(int,rep)
    out=[(p+1,q)]
    if p>=1: out.append((p-1,q+1))
    if q>=1: out.append((p,q-1))
    return tuple(out)


def su3_fuse_antifundamental(rep):
    p,q=map(int,rep)
    out=[(p,q+1)]
    if q>=1: out.append((p+1,q-1))
    if p>=1: out.append((p-1,q))
    return tuple(out)


@lru_cache(None)
def vacuum_character_ops(depth):
    """
    Exact single-plaquette SU(3) character Hamiltonian truncated only by
    magnetic graph distance from the vacuum character.

    Character states chi_(p,q) are Haar-orthonormal.  The electric term is
        H0 chi_R = 2 C2(R) chi_R
    for a four-link plaquette, while
        M = chi_3 + chi_3bar
    acts by exact SU(3) tensor-product fusion.
    """
    depth=int(depth)
    dist={(0,0):0}
    queue=deque([(0,0)])
    while queue:
        r=queue.popleft(); d=dist[r]
        if d>=depth:
            continue
        for z in su3_fuse_fundamental(r)+su3_fuse_antifundamental(r):
            if z not in dist:
                dist[z]=d+1
                queue.append(z)
    reps=tuple(sorted(dist, key=lambda r:(dist[r], r[0]+r[1], r)))
    idx={r:i for i,r in enumerate(reps)}
    n=len(reps)
    H0=np.diag([2.0*su3_c2_pq(*r) for r in reps]).astype(np.float64)
    M=np.zeros((n,n),dtype=np.float64)
    for r,j in idx.items():
        for z in su3_fuse_fundamental(r)+su3_fuse_antifundamental(r):
            i=idx.get(z)
            if i is not None:
                M[i,j]+=1.0
    asym=float(np.max(np.abs(M-M.T))) if n else 0.0
    if asym>1e-13:
        raise RuntimeError(f"vacuum character M not Hermitian: {asym:.3e}")
    return reps,H0,M


@lru_cache(maxsize=4096)
def _vacuum_character_energy_cached(depth, u_key):
    reps,H0,M=vacuum_character_ops(int(depth))
    u=float(u_key)
    # Tiny dense character spaces (depth 5 => 21 irreps): exact diagonalization
    # is faster and more stable than an iterative eigensolver.
    return float(eigh(H0-u*M, subset_by_index=[0,0], check_finite=False)[0][0])


def vacuum_cluster_energy(u, depth=None):
    if depth is None:
        depth=V8_VAC_DEPTH
    # All production u values and fixed-point evaluations reuse the same u;
    # stringifying to 16 significant digits makes the cache deterministic.
    key=float(f"{float(u):.16g}")
    return _vacuum_character_energy_cached(int(depth), key)


def _v8_global_effective_eval(rt, u, trial_E, vac_depth=None, return_vector=False):
    e_vac=vacuum_cluster_energy(u, vac_depth)
    diag=rt["E_P"]-rt["VAC_P"]*e_vac
    Sigma=None
    min_den=float("inf")
    for lam,vac,K in rt["kernels"]:
        den=trial_E-lam
        min_den=min(min_den,abs(float(den)))
        if abs(den)<1e-9:
            raise RuntimeError(f"v8 Feshbach trial energy hit Q pole: |den|={abs(den):.3e}")
        term=(u*u/den)*K
        Sigma=term if Sigma is None else Sigma+term
    def mv(x):
        z=diag*x+u*(rt["W_PP"]@x)
        if Sigma is not None:
            z=z+Sigma@x
        return z
    r=source_lanczos_custom(mv,rt["source"],return_vector=return_vector)
    r["min_q_denominator"]=min_den
    return r


def _v8_global_p_only_eval(rt,u,vac_depth=None):
    e_vac=vacuum_cluster_energy(u,vac_depth)
    diag=rt["E_P"]-rt["VAC_P"]*e_vac
    def mv(x):
        return diag*x+u*(rt["W_PP"]@x)
    return source_lanczos_custom(mv,rt["source"],return_vector=False)


def v8_global_feshbach_pole(rt,u,vac_depth=None):
    p0=_v8_global_p_only_eval(rt,u,vac_depth)
    E=p0["pole_energy"]
    prev_E=prev_F=None
    last=None
    for it in range(V5_MAX_FP):
        r=_v8_global_effective_eval(rt,u,E,vac_depth,return_vector=False)
        F=r["pole_energy"]-E
        last=r
        if abs(F)<V5_FP_TOL and r["converged"]:
            break
        if prev_E is not None and abs(F-prev_F)>1e-14:
            Enew=E-F*(E-prev_E)/(F-prev_F)
            if (not math.isfinite(Enew)) or abs(Enew-E)>0.75:
                Enew=E+0.5*F
        else:
            Enew=E+0.65*F
        prev_E,prev_F=E,F
        E=Enew
    else:
        raise RuntimeError(f"v8 Feshbach fixed point failed at u={u}")

    E=last["pole_energy"]
    final=_v8_global_effective_eval(rt,u,E,vac_depth,return_vector=True)
    fp_resid=abs(final["pole_energy"]-E)
    E=final["pole_energy"]
    pvec=final.pop("ritz_vector")

    qnorm=0.0
    for lam,vac,K in rt["kernels"]:
        den=E-lam
        Kp=K@pvec
        val=_to_float(xp.dot(pvec,Kp))
        if val < -1e-8:
            raise RuntimeError(f"negative global-Q norm quadratic form {val:.3e}")
        qnorm += (u*u)*max(0.0,val)/(den*den)

    final["pole_residue_P"]=final["pole_residue"]
    final["pole_residue"]=final["pole_residue"]/(1.0+qnorm)
    final["q_norm_ratio"]=qnorm
    final["feshbach_residual"]=fp_resid
    final["fixed_point_iterations"]=it+1
    final["converged"]=bool(final["converged"] and fp_resid < 5*V5_FP_TOL)
    final["vacuum_cluster_energy"]=vacuum_cluster_energy(u,vac_depth)
    return final


def _poly_coeffs(fn,h=None,degree=5):
    if h is None: h=V8_C3_H
    us=np.arange(-4,5,dtype=np.float64)*float(h)
    ys=np.asarray([fn(float(u)) for u in us],dtype=np.float64)
    return np.polynomial.polynomial.polyfit(us,ys,int(degree))


def _mass_coeffs(model, new=True, vac_depth=None):
    rt=prepare_global_runtime(model)
    def f(u):
        if abs(u)<1e-18:
            return E0_PLAQ
        return (v8_global_feshbach_pole(rt,u,vac_depth)["pole_energy"] if new
                else global_feshbach_pole(rt,u)["pole_energy"])
    c=_poly_coeffs(f,degree=5)
    del rt
    free_backend_memory()
    return c


# =============================================================================
# v8 DRIVER
# =============================================================================
# v9: EXACT THIRD-ORDER LINKED WINDING-STRING CLOSURE + POST-v8 RATIO
# =============================================================================
#
# The v8 mass repair exposed the SU(3) cubic vacuum determinant.  Applying only
# that vacuum character correction to the winding string is insufficient because
# the string itself has an O(u^3) linked magnetic process.  v9 computes that
# process directly from the actual K=1 winding-string Hilbert space:
#
#   phi = R_0 Q W |straight string>
#   E3_raw = <phi| W |phi>
#
# Here Q includes BOTH retained nondegenerate P intermediates and the exact
# joint-link-Casimir projected global-Q vectors.  The endpoint Haar contraction
# includes the SU(3)-specific (4,1)/(1,4) determinant projector, so no s3 value is
# used in constructing E3_raw.
#
# The result is local and extensive:
#
#   E3_raw / L = -65/51.
#
# Combining this with the independently derived vacuum coefficient e_vac,3=-9/32
# and four incident plaquettes per bulk string link gives
#
#   s3 = -65/51 - 4*(-9/32) = -61/408.
#
# IMPORTANT SIGN CORRECTION:
# Earlier project notes carried +61/408.  The direct network calculation below
# gives -61/408.  This is also the sign obtained by converting the published
# Hamiltonian strong-coupling string series written in x=2/g^4 to u=1/g^4.
#
# Production then adds the derived extensive O(u^3) linked-string operator to
# the v8 vacuum-character/global-Q Feshbach Hamiltonian and repeats L=3..7.
# This makes the mass and string expansions mutually correct through O(u^3).
# It does NOT claim that all O(u^4+) string dynamics are closed.
# =============================================================================

V9_GATE_START=len(gates)
V9_STRING_DEPTHS=tuple(int(x) for x in os.environ.get("V9_STRING_DEPTHS","2").split(",") if x.strip())
V9_STRING_LENGTHS=tuple(int(x) for x in os.environ.get("V9_STRING_LENGTHS","3,4,5,6,7").split(",") if x.strip())
V9_AUDIT_LENGTHS=tuple(int(x) for x in os.environ.get("V9_AUDIT_LENGTHS","4,5").split(",") if x.strip())
V9_C3_H=float(os.environ.get("V9_C3_H","0.002"))
V9_S3_TOL=float(os.environ.get("V9_S3_TOL","8e-6"))
# v9.1: h=0.002 raises the cubic signal 64x over v9 h=0.0005 while the degree-5 symmetric fit removes lower/higher parity contamination. Do not loosen this hard tolerance.
V9_PROGRESS=int(os.environ.get("V9_PROGRESS","1"))

S2_EX=-22.0/153.0
S3_EX=-61.0/408.0
S3_EX_FRAC=Fraction(-61,408)

# --- SU(3) (4,1) determinant Haar projector ---------------------------------
# Four natural invariants I_r = delta(i_r,k) epsilon(other 3 fundamentals).
# This is the exact pseudoinverse certified in v05c.
_V9_C41=np.array([
    [ 1/32, 1/96,-1/96, 1/96],
    [ 1/96, 1/32, 1/96,-1/96],
    [-1/96, 1/96, 1/32, 1/96],
    [ 1/96,-1/96, 1/96, 1/32],
],dtype=np.float64)
_V9_T41=None


def _v9_eps3(a,b,c):
    if len({int(a),int(b),int(c)})<3:
        return 0.0
    p=(int(a),int(b),int(c))
    inv=sum(p[i]>p[j] for i in range(3) for j in range(i+1,3))
    return -1.0 if inv%2 else 1.0


def _v9_t41():
    global _V9_T41
    if _V9_T41 is not None:
        return _V9_T41
    T=np.zeros((3,)*10,dtype=np.float64)
    # Axis order: r0,c0,r1,c1,r2,c2,r3,c3,k,l.
    for inds in itertools.product(range(3),repeat=10):
        mr=(inds[0],inds[2],inds[4],inds[6])
        mc=(inds[1],inds[3],inds[5],inds[7])
        kr,kc=inds[8],inds[9]
        Ir=np.zeros(4,dtype=np.float64); Ic=np.zeros(4,dtype=np.float64)
        for r in range(4):
            rr=[mr[j] for j in range(4) if j!=r]
            cc=[mc[j] for j in range(4) if j!=r]
            Ir[r]=(1.0 if mr[r]==kr else 0.0)*_v9_eps3(*rr)
            Ic[r]=(1.0 if mc[r]==kc else 0.0)*_v9_eps3(*cc)
        T[inds]=float(Ir@_V9_C41@Ic)
    _V9_T41=T
    return T


def _v9_haar_endpoint(a,b):
    """Depth-3 endpoint Haar integral needed by the marked-string E3 audit.

    The only local occurrence patterns generated by this audit are (1,1),
    (3,0)/(0,3), and the SU(3)-specific mixed determinant (4,1)/(1,4).
    Refuse any unexpected pattern instead of silently approximating it.
    """
    aa,bb=_joint_canon_states(a,b)
    occ,part=lx_combine_bra_ket(aa,bb)
    bylink=defaultdict(lambda:{True:[],False:[]})
    for i,(link,typ) in enumerate(occ):
        bylink[int(link)][bool(typ)].append(i)
    args=[]
    for _,g in bylink.items():
        U,B=g[True],g[False]
        nu,nb=len(U),len(B)
        if (nu-nb)%3!=0:
            return 0.0
        if (nu,nb)==(1,1):
            positions=U+B; ten=_FAST_T11
        elif (nu,nb) in ((3,0),(0,3)):
            positions=U if nu==3 else B; ten=_FAST_T30
        elif (nu,nb) in ((4,1),(1,4)):
            # T41 expects the four majority occurrences first.
            positions=(U+B) if nu==4 else (B+U); ten=_v9_t41()
        else:
            raise RuntimeError(f"v9 marked-string Haar encountered unsupported occurrence pattern {(nu,nb)}")
        inds=[]
        for p0 in positions:
            inds.extend((int(part[2*p0]),int(part[2*p0+1])))
        args.extend((ten,inds))
    if not args:
        return float(N**len(set(part)))
    return float(oe.contract(*args,[],optimize='greedy'))


def _v9_flux_key_state(st):
    cnt=defaultdict(int)
    for l,typ in st.occ:
        cnt[int(l)]+=1 if typ else -1
    out=[]
    for l,c in cnt.items():
        r=c%3
        if r==2: r=-1
        if r: out.append((int(l),int(r)))
    return tuple(sorted(out))


def _v9_add_face_flux_key(key,bf):
    d=defaultdict(int)
    for l,c in key: d[int(l)]+=int(c)
    for i in np.flatnonzero(bf): d[int(i)]+=int(bf[i])
    out=[]
    for l,c in d.items():
        r=c%3
        if r==2: r=-1
        if r: out.append((int(l),int(r)))
    return tuple(sorted(out))


def _v9_collision_groups(store):
    d={k:[r] for k,r in store.first.items()}
    d.update(store.multi)
    return d


def _v9_first_resolvent_vector(model,parent):
    """Return phi=R0 Q W|parent> as an exact-projector trace-network vector."""
    parent=int(parent)
    E0=float(model['E_P'][parent])
    phi=defaultdict(float)
    pterms=0; qterms=0

    # Retained P intermediates.  Distinct square-free winding loops are already
    # orthonormal in this flux basis; the matrix stores the exact magnetic overlap.
    col=model['W_PP'].getcol(parent).tocoo()
    for j,a in zip(col.row,col.data):
        j=int(j); a=float(a)
        if j==parent or abs(a)<1e-15:
            continue
        den=E0-float(model['E_P'][j])
        if abs(den)<1e-12:
            raise RuntimeError("v9 encountered a degenerate retained-P intermediate in the straight-string E3 audit")
        st=lx_trace_state(model['v9_state_steps'][j])
        phi[st]+=a/den
        pterms+=1

    # Exact joint-Casimir Q spectral projectors.  joint_vec is unnormalised;
    # W=-M multiplies each magnetic action by -1.  No Gram inverse is needed:
    # summing the actual projected vectors automatically respects all redundancy.
    groups=_v9_collision_groups(model['v9_collisions'])
    for (_,lam),recs in groups.items():
        den=E0-float(lam)
        for rec in recs:
            if int(rec.parent)!=parent:
                continue
            vv,_=model['v9_joint_vec'](rec,False)
            for st,c in vv.items():
                phi[st]+=-float(c)/den
            qterms+=1

    phi={st:c for st,c in phi.items() if abs(c)>1e-14}
    return phi,pterms,qterms


def _v9_w_expectation(model,phi,parent):
    """Compute <phi|W|phi>, W=-sum_p(Tr Up+Tr Up^dag), with exact Haar endpoints."""
    groups=defaultdict(list)
    for st,c in phi.items():
        groups[_v9_flux_key_state(st)].append((st,float(c)))

    cand0=set(model['v9_cand_cache'][int(parent)])
    faceset=set(cand0)
    for f in tuple(cand0):
        faceset.update(model['v9_face_support_faces_obj'][f])

    pstate_cache={}
    total=0.0; tests=0; nonzero=0
    t0=time.time()
    items=list(phi.items())
    for ib,(b,cb) in enumerate(items):
        kb=_v9_flux_key_state(b)
        for f in faceset:
            bf0=np.asarray(model['v9_face_flux_fn'](f),dtype=np.int8)
            for orient in (-1,+1):
                bf=(orient*bf0).astype(np.int8)
                ka=_v9_add_face_flux_key(kb,bf)
                bras=groups.get(ka)
                if not bras:
                    continue
                k=(int(f),int(orient))
                if k not in pstate_cache:
                    pstate_cache[k]=lx_trace_state(model['v9_fs_cached'](f,orient))
                prod=lx_tensor_product(b,pstate_cache[k])
                for a,ca in bras:
                    tests+=1
                    h=_v9_haar_endpoint(a,prod)
                    if abs(h)>2e-13:
                        total += float(ca)*float(cb)*(-h)
                        nonzero+=1
        if V9_PROGRESS and len(items)>100 and (ib+1)%100==0:
            print(f"      v9 marked-string E3 {ib+1}/{len(items)}; tests={tests:,}; nonzero={nonzero:,}; elapsed={time.time()-t0:.1f}s")
    return float(total),int(tests),int(nonzero)


def derive_marked_string_raw_c3(Ls):
    """Blind direct derivation of the raw straight-string cubic energy per longitudinal link."""
    sec=WindingStringSector(int(Ls),max_depth=1)
    model=build_global_string_model(sec)
    src=np.flatnonzero(np.abs(model['source_P'])>1e-14)
    if len(src)==0:
        raise RuntimeError("v9 straight-string source missing")
    parent=int(src[0])
    phi,pterms,qterms=_v9_first_resolvent_vector(model,parent)
    e3,tests,nz=_v9_w_expectation(model,phi,parent)
    raw_per_link=e3/float(Ls)
    out={
        'L':int(Ls),'raw_total':float(e3),'raw_per_link':float(raw_per_link),
        'phi_states':len(phi),'P_terms':int(pterms),'Q_terms':int(qterms),
        'haar_tests':int(tests),'haar_nonzero':int(nz),
        'P_dim':len(model['E_P']),'Q_actions':int(model['action_channels']),
        'gram_nullity':int(model['gram_nullity']),
    }
    del model,sec
    free_backend_memory()
    return out




# =============================================================================
# v10a NEW LAYER
# =============================================================================
from scipy.sparse import hstack

V10A_GLUE_K = int(os.environ.get("V10A_GLUE_K", "0"))
V10A_TEST_U = float(os.environ.get("V10A_TEST_U", "0.10"))
V10A_COEFF_H = float(os.environ.get("V10A_COEFF_H", "0.002"))
V10A_STRING_AUDIT_LENGTHS = tuple(int(x) for x in os.environ.get("V10A_STRING_AUDIT_LENGTHS", "4,5").split(",") if x.strip())
V10A_PROGRESS = int(os.environ.get("V10A_PROGRESS", "1"))
V10A_GRAM_TOL = float(os.environ.get("V10A_GRAM_TOL", "2e-11"))
V10A_ENDPOINT_TOL = float(os.environ.get("V10A_ENDPOINT_TOL", "2e-13"))
V10A_MATRIX_TOL = float(os.environ.get("V10A_MATRIX_TOL", "5e-12"))

V10A_GATE_START = len(gates)


def _v10_sparse_maxabs(A):
    return 0.0 if A.nnz == 0 else float(np.max(np.abs(A.data)))


def _v10_physical_raw_vec(model, rec):
    """Actual physical raw Q vector represented as a trace-network linear combo.

    For C- glueball channels the normalized physical raw vector is
        (v - C v)/sqrt(2),
    whose Gram matrix is exactly the one used in the v5 global quotient.
    String channels carry fixed center charge and need no C quotient.
    """
    v, _ = model["v9_joint_vec"](rec, False)
    out = defaultdict(float)
    if model["v9_codd"]:
        vc, _ = model["v9_joint_vec"](rec, True)
        s = 1.0 / math.sqrt(2.0)
        for st, c in v.items():
            out[st] += s * float(c)
        for st, c in vc.items():
            out[st] -= s * float(c)
    else:
        for st, c in v.items():
            out[st] += float(c)
    return {st: c for st, c in out.items() if abs(c) > 1e-14}


def build_physical_q_quotient(model, keep_vectors=True, label="Q"):
    """Expose the physical Gram quotient that v5 previously compressed to K_lambda.

    For each collision block G = U_r Lambda_r U_r^T,
        X = U_r Lambda_r^{-1/2},
        |e_a> = sum_i X_ia |q_i>,
        B_M = C U_r Lambda_r^{1/2}.

    The Hamiltonian magnetic operator is W=-M, hence B_W=-B_M.
    The sign does not affect B B^T but is retained for future W_QQ work.
    """
    groups = _v9_collision_groups(model["v9_collisions"])
    items = sorted(groups.items(), key=lambda kv: (float(kv[0][1]), repr(kv[0][0])))
    nP = len(model["E_P"])
    B_blocks = []
    E_Q = []
    qvecs = []
    block_meta = []
    Kacc = defaultdict(lambda: csr_matrix((nP, nP), dtype=np.float64))
    raw_dim = phys_dim = nullity = 0
    min_eval = 0.0
    max_self_err = 0.0
    max_orth_err = 0.0
    t0 = time.time()

    for ib, (key, recs) in enumerate(items):
        raw = [_v10_physical_raw_vec(model, r) for r in recs]
        n = len(raw)
        raw_dim += n
        G = np.zeros((n, n), dtype=np.float64)
        for i in range(n):
            for j in range(i, n):
                gij = _vec_inner_fast(raw[i], raw[j])
                G[i, j] = G[j, i] = gij
        for i, r in enumerate(recs):
            max_self_err = max(max_self_err, abs(G[i, i] - float(r.norm)))

        ev, U = np.linalg.eigh(0.5 * (G + G.T))
        min_eval = min(min_eval, float(ev.min(initial=0.0)))
        scale = max(1.0, float(ev.max(initial=0.0)))
        keep = ev > V10A_GRAM_TOL * scale
        if float(ev.min(initial=0.0)) < -2e-9:
            raise RuntimeError(f"{label}: physical-Q Gram block not PSD: min={ev.min():.3e}")
        nullity += n - int(np.sum(keep))
        if not np.any(keep):
            continue

        lamv = ev[keep]
        Ur = U[:, keep]
        X = Ur / np.sqrt(lamv)[None, :]
        parents = sorted(set(int(r.parent) for r in recs))
        pidx = {p: i for i, p in enumerate(parents)}
        C = np.zeros((len(parents), n), dtype=np.float64)
        for i, r in enumerate(recs):
            C[pidx[int(r.parent)], i] += 1.0
        B_local_M = C @ Ur @ np.diag(np.sqrt(lamv))

        rr, cc, vv = [], [], []
        for il, p in enumerate(parents):
            for j, x in enumerate(B_local_M[il]):
                if abs(x) > 1e-14:
                    rr.append(p); cc.append(j); vv.append(float(x))
        Bg_M = coo_matrix((vv, (rr, cc)), shape=(nP, len(lamv)), dtype=np.float64).tocsr()
        B_blocks.append(Bg_M)
        Kacc[float(key[1])] = Kacc[float(key[1])] + Bg_M @ Bg_M.T

        q_start = phys_dim
        if keep_vectors:
            for a in range(len(lamv)):
                d = defaultdict(float)
                for ci, rv in zip(X[:, a], raw):
                    if abs(ci) < 1e-15:
                        continue
                    for st, x in rv.items():
                        d[st] += float(ci) * float(x)
                d = {st: x for st, x in d.items() if abs(x) > 2e-13}
                qvecs.append(d)
                max_orth_err = max(max_orth_err, abs(_vec_inner_fast(d, d) - 1.0))
        phys_dim += len(lamv)
        E_Q.extend([float(key[1])] * len(lamv))
        block_meta.append({
            "key": key, "raw_dim": n, "rank": len(lamv), "parents": tuple(parents),
            "q_slice": (q_start, phys_dim), "evals": lamv.copy(), "X": X,
        })

        if V10A_PROGRESS and len(items) > 5000 and (ib == 0 or (ib + 1) % max(1, len(items)//5) == 0):
            print(f"      {label} quotient {ib+1:,}/{len(items):,}; physical={phys_dim:,}; null={nullity:,}; elapsed={time.time()-t0:.1f}s")

    B_M = hstack(B_blocks, format="csr") if B_blocks else csr_matrix((nP, 0), dtype=np.float64)
    kernel_errs = []
    for lam, vac, K in model["kernels"]:
        D = Kacc[float(lam)] - K
        kernel_errs.append(_v10_sparse_maxabs(D))
    kernel_err = max(kernel_errs, default=0.0)

    return {
        "B_M": B_M,
        "B_W": -B_M,
        "E_Q": np.asarray(E_Q, dtype=np.float64),
        "qvecs": qvecs,
        "blocks": block_meta,
        "raw_dim": raw_dim,
        "phys_dim": phys_dim,
        "nullity": nullity,
        "gram_min_eig": min_eval,
        "kernel_reconstruction_error": kernel_err,
        "self_norm_error": max_self_err,
        "orthonormality_error": max_orth_err,
    }


def _v10_cpu_source_lanczos(matvec, source, maxiter=96, tol=2e-12):
    """Small deterministic CPU Lanczos used only for the explicit-Q regression."""
    q = np.asarray(source, dtype=np.float64).copy()
    q /= np.linalg.norm(q)
    Q = []
    alpha, beta = [], []
    qprev = np.zeros_like(q)
    bprev = 0.0
    last = None
    for m in range(maxiter):
        Q.append(q.copy())
        z = np.asarray(matvec(q), dtype=np.float64)
        if m:
            z -= bprev * qprev
        a = float(np.dot(q, z))
        z -= a * q
        QQ = np.asarray(Q)
        for _ in range(2):
            z -= (QQ @ z) @ QQ
        b = float(np.linalg.norm(z))
        alpha.append(a)
        if m >= 2:
            evals, evecs = eigh_tridiagonal(np.asarray(alpha), np.asarray(beta))
            weights = evecs[0] ** 2
            p = int(np.argmax(weights))
            resid = b * abs(float(evecs[-1, p]))
            last = (float(evals[p]), float(weights[p]), float(resid), m + 1)
            if resid < tol:
                return {"pole_energy": last[0], "pole_residue": last[1], "ritz_residual": last[2], "krylov_dimension": last[3], "converged": True}
        if b < 1e-14:
            break
        if m < maxiter - 1:
            beta.append(b)
        qprev, q = q, z / b
        bprev = b
    if last is None:
        return {"pole_energy": alpha[0], "pole_residue": 1.0, "ritz_residual": 0.0, "krylov_dimension": 1, "converged": True}
    return {"pole_energy": last[0], "pole_residue": last[1], "ritz_residual": last[2], "krylov_dimension": last[3], "converged": last[2] < 1e-9}


def v10_explicit_pq_pole(model, quotient, u, W_QQ=None, source_P=None):
    """Explicit P+Q Hamiltonian; no Schur elimination and no fitted Q moment."""
    nP = len(model["E_P"])
    nQ = quotient["phys_dim"]
    B = quotient["B_W"]
    Eq = quotient["E_Q"]
    if W_QQ is None:
        W_QQ = csr_matrix((nQ, nQ), dtype=np.float64)
    if source_P is None:
        source_P = model["source_P"]
    src = np.concatenate((np.asarray(source_P, dtype=np.float64), np.zeros(nQ, dtype=np.float64)))
    evac = vacuum_cluster_energy(float(u), V8_VAC_DEPTH)
    pdiag = model["E_P"] - model["VAC_P"] * evac

    def mv(x):
        p = x[:nP]; q = x[nP:]
        outp = pdiag * p + float(u) * (model["W_PP"] @ p) + float(u) * (B @ q)
        outq = Eq * q + float(u) * (B.T @ p) + float(u) * (W_QQ @ q)
        return np.concatenate((outp, outq))

    return _v10_cpu_source_lanczos(mv, src)


_V10_ENDPOINT_CACHE = {}
V10_SUPPORTED_ENDPOINT_PATTERNS = {(1,1), (3,0), (0,3), (4,1), (1,4)}


def _v10_endpoint_patterns(a, b):
    aa, bb = _joint_canon_states(a, b)
    occ, part = lx_combine_bra_ket(aa, bb)
    bylink = defaultdict(lambda: [0, 0])
    for link, typ in occ:
        bylink[int(link)][0 if typ else 1] += 1
    return {tuple(x) for x in bylink.values()}


def _v10_endpoint(a, b):
    key = _joint_canon_states(a, b)
    if key not in _V10_ENDPOINT_CACHE:
        _V10_ENDPOINT_CACHE[key] = _v9_haar_endpoint(*key)
    return _V10_ENDPOINT_CACHE[key]


def build_one_step_WQQ(model, quotient, label="glue-Q1"):
    """Full W_QQ on the exposed one-step physical Q range.

    This is a real operator construction, not a source moment.  It uses all
    physical quotient vectors and every plaquette orientation, and computes the
    unsymmetrized matrix first so Hermiticity is an independent gate.
    """
    qvecs = quotient["qvecs"]
    if len(qvecs) != quotient["phys_dim"]:
        raise RuntimeError("W_QQ construction requires keep_vectors=True")
    nq = len(qvecs)
    bras = defaultdict(list)
    for i, v in enumerate(qvecs):
        for a, ca in v.items():
            bras[_v9_flux_key_state(a)].append((i, a, float(ca)))

    nfaces = len(model["v9_face_support_faces_obj"])
    face_states = {(f, o): lx_trace_state(model["v9_fs_cached"](f, o)) for f in range(nfaces) for o in (-1, +1)}
    acc = defaultdict(float)
    patterns = set()
    tests = endpoint_nonzero = 0
    t0 = time.time()

    for j, v in enumerate(qvecs):
        for b, cb in v.items():
            kb = _v9_flux_key_state(b)
            for f in range(nfaces):
                bf0 = np.asarray(model["v9_face_flux_fn"](f), dtype=np.int8)
                for o in (-1, +1):
                    bf = (o * bf0).astype(np.int8)
                    ka = _v9_add_face_flux_key(kb, bf)
                    ls = bras.get(ka)
                    if not ls:
                        continue
                    prod = lx_tensor_product(b, face_states[(f, o)])
                    for i, a, ca in ls:
                        tests += 1
                        pats = _v10_endpoint_patterns(a, prod)
                        patterns.update(pats)
                        bad = pats - V10_SUPPORTED_ENDPOINT_PATTERNS
                        if bad:
                            raise RuntimeError(f"{label}: unsupported Haar endpoint occurrence patterns {sorted(bad)}")
                        h = _v10_endpoint(a, prod)
                        if abs(h) > V10A_ENDPOINT_TOL:
                            acc[(i, j)] += float(ca) * float(cb) * (-float(h))
                            endpoint_nonzero += 1
        if V10A_PROGRESS and nq > 500 and (j == 0 or (j + 1) % 250 == 0):
            print(f"      {label} WQQ {j+1:,}/{nq:,}; endpoint tests={tests:,}; cache={len(_V10_ENDPOINT_CACHE):,}; elapsed={time.time()-t0:.1f}s")

    rows, cols, vals = [], [], []
    raw_max = 0.0
    for (i, j), x in acc.items():
        raw_max = max(raw_max, abs(float(x)))
        if abs(x) > 1e-15:
            rows.append(i); cols.append(j); vals.append(float(x))
    Wdir = coo_matrix((vals, (rows, cols)), shape=(nq, nq), dtype=np.float64).tocsr()
    Wdir.sum_duplicates()
    herm_err = _v10_sparse_maxabs(Wdir - Wdir.T)
    W = 0.5 * (Wdir + Wdir.T)
    W.eliminate_zeros()
    return {
        "W": W.tocsr(), "directional": Wdir,
        "hermiticity_error": herm_err, "max_abs": _v10_sparse_maxabs(W),
        "raw_acc_max": raw_max, "endpoint_tests": tests,
        "endpoint_nonzero": endpoint_nonzero, "patterns": tuple(sorted(patterns)),
        "endpoint_cache": len(_V10_ENDPOINT_CACHE),
    }


def _v10_mass_coeffs_explicit(model, quotient, W_QQ):
    h = V10A_COEFF_H
    us = np.arange(-4, 5, dtype=np.float64) * h
    ys = []
    for u in us:
        if abs(u) < 1e-18:
            ys.append(E0_PLAQ)
        else:
            ys.append(v10_explicit_pq_pole(model, quotient, float(u), W_QQ)["pole_energy"])
    return np.polynomial.polynomial.polyfit(us, np.asarray(ys), 5)


def v10_t1_source_gram():
    pols = ((1,2), (0,2), (0,1))  # axial x,y,z plaquette planes
    reps = {}
    terms = []
    for pol in pols:
        col = []
        ff = [f for f, (_, a, b) in enumerate(faces) if (a, b) == pol]
        for f in ff:
            key, sgn, rep = canonical_codd(B2[:, f])
            reps.setdefault(key, rep)
            col.append((key, int(sgn)))
        terms.append(col)
    keys = list(reps)
    idx = {k:i for i,k in enumerate(keys)}
    S = np.zeros((len(keys), 3), dtype=np.float64)
    for a, col in enumerate(terms):
        norm = math.sqrt(len(col))
        for key, sgn in col:
            S[idx[key], a] += sgn / norm
    return S.T @ S


def v10_orientation_pole_audit(u):
    global source_faces
    old = list(source_faces)
    vals = []
    try:
        for pol in ((1,2), (0,2), (0,1)):
            source_faces = [f for f, (_, a, b) in enumerate(faces) if (a, b) == pol]
            mdl = build_global_glueball_model(0)
            rt = prepare_global_runtime(mdl)
            r = v8_global_feshbach_pole(rt, float(u), V8_VAC_DEPTH)
            vals.append((pol, r["pole_energy"], r["pole_residue"]))
            del rt, mdl
            free_backend_memory()
    finally:
        source_faces = old
    return vals


def v10_string_c3_decomposition(Ls):
    """Direct cubic string moment with NO manual u^3 injection.

    Decomposes E3_raw=<phi|W|phi> into PP, (PQ+QP), and QQ pieces.
    The QQ term is the cleanest source-projected unit test of genuine W_QQ.
    """
    sec = WindingStringSector(int(Ls), max_depth=1)
    model = build_global_string_model(sec)
    parent = int(np.flatnonzero(np.abs(model["source_P"]) > 1e-14)[0])
    E0 = float(model["E_P"][parent])
    phi, pterms, qterms = _v9_first_resolvent_vector(model, parent)

    pp = defaultdict(float)
    col = model["W_PP"].getcol(parent).tocoo()
    for j, a in zip(col.row, col.data):
        j = int(j); a = float(a)
        if j == parent or abs(a) < 1e-15:
            continue
        den = E0 - float(model["E_P"][j])
        pp[lx_trace_state(model["v9_state_steps"][j])] += a / den

    qq = defaultdict(float, phi)
    for st, x in pp.items():
        qq[st] -= x
    qq = {st:x for st,x in qq.items() if abs(x) > 1e-14}

    epp, tpp, nzpp = _v9_w_expectation(model, dict(pp), parent)
    eqq, tqq, nzqq = _v9_w_expectation(model, qq, parent)
    etot, ttot, nztot = _v9_w_expectation(model, phi, parent)
    ecross = etot - epp - eqq
    out = {
        "L": int(Ls), "PP": float(epp), "QQ": float(eqq), "cross": float(ecross), "raw": float(etot),
        "PP_per_L": float(epp)/Ls, "QQ_per_L": float(eqq)/Ls,
        "cross_per_L": float(ecross)/Ls, "raw_per_L": float(etot)/Ls,
        "linked_s3": float(etot)/Ls - 4.0 * EV3_EX,
        "phi_states": len(phi), "P_terms": pterms, "Q_terms": qterms,
        "haar_tests": ttot, "haar_nonzero": nztot,
    }
    del model, sec
    free_backend_memory()
    return out


def v10_q2_preflight(model, quotient, parent=0):
    """Census the first genuinely new Q1->Q2 layer; no m4 is inferred from it."""
    punit = np.zeros(len(model["E_P"]), dtype=np.float64)
    punit[int(parent)] = 1.0
    y = quotient["B_W"].T @ punit
    bright = np.flatnonzero(np.abs(y) > 1e-12)
    q1_keys = set()
    for v in quotient["qvecs"]:
        for st in v:
            q1_keys.add(_v9_flux_key_state(st))
    raw_actions = 0
    canonical_states = set()
    fluxclass = Counter()
    occ = Counter()
    for j in bright:
        v = quotient["qvecs"][int(j)]
        for st in v:
            support = {int(l) for l, _ in st.occ}
            cand = set()
            for l in support:
                cand.update(link_faces[l])
            for f in cand:
                for o in (-1, +1):
                    raw_actions += 1
                    fs = lx_trace_state(model["v9_fs_cached"](f, o))
                    prod = lx_tensor_product(st, fs)
                    k = _v9_flux_key_state(prod)
                    fluxclass["Q1-key" if k in q1_keys else "new-key"] += 1
                    canonical_states.add(_joint_canon_states(prod)[0])
                    by = defaultdict(lambda:[0,0])
                    for l, typ in prod.occ:
                        by[int(l)][0 if typ else 1] += 1
                    for x in by.values():
                        occ[tuple(x)] += 1
    return {
        "bright_q1": len(bright), "raw_actions": raw_actions,
        "unique_canonical_networks": len(canonical_states),
        "fluxclass": dict(fluxclass), "occurrence_patterns": dict(occ),
    }


# =============================================================================
# v10a DRIVER
# =============================================================================
print("="*128)
print("HODGE v10a — PHYSICAL-Q QUOTIENT / Q-DYNAMICS CERTIFICATE ENGINE")
print("="*128)
print(f"backend inherited from solver : {DEVICE}")
print(f"glue certificate depth        : K={V10A_GLUE_K}")
print(f"explicit Schur test u         : {V10A_TEST_U}")
print(f"string cubic audit lengths    : {V10A_STRING_AUDIT_LENGTHS}")
print("physical m4/C3_full output    : DISABLED until Q2 + linked/folded subtraction is installed")
print()

gate("v10a SU(3) F x F weights sum to one", abs(W_A + W_S - 1.0) < 1e-15)
gate("v10a SU(3) F x Fbar weights sum to one", abs(W_1 + W_8 - 1.0) < 1e-15)
validate_fast_haar_tensor_contract()

print("\n[1] EXPOSE PHYSICAL GLOBAL-Q QUOTIENT")
gmodel = build_global_glueball_model(V10A_GLUE_K)
print(f"raw Q action channels={gmodel['action_channels']:,}; v5 Gram-null={gmodel['gram_nullity']:,}; kernels={len(gmodel['kernels'])}")
gq = build_physical_q_quotient(gmodel, keep_vectors=True, label=f"glue K={V10A_GLUE_K}")
print(f"explicit physical Q: raw={gq['raw_dim']:,} -> rank={gq['phys_dim']:,} + null={gq['nullity']:,}")
print(f"max |B B^T-K|={gq['kernel_reconstruction_error']:.3e}; min Gram eig={gq['gram_min_eig']:.3e}; orth err={gq['orthonormality_error']:.3e}")
gate("v10a physical-Q nullity matches v5 global quotient", gq["nullity"] == gmodel["gram_nullity"], f"{gq['nullity']} vs {gmodel['gram_nullity']}")
gate("v10a B B^T reproduces every v8 K_lambda", gq["kernel_reconstruction_error"] < 5e-12, f"max err={gq['kernel_reconstruction_error']:.3e}")
gate("v10a physical-Q basis is orthonormal", gq["orthonormality_error"] < 3e-12, f"max err={gq['orthonormality_error']:.3e}")

print("\n[2] ZERO-DYNAMICS SCHUR EQUIVALENCE")
rt = prepare_global_runtime(gmodel)
r8 = v8_global_feshbach_pole(rt, V10A_TEST_U, V8_VAC_DEPTH)
rX = v10_explicit_pq_pole(gmodel, gq, V10A_TEST_U, None)
print(f"v8 Schur     : E={r8['pole_energy']:.15f} Z={r8['pole_residue']:.15f}")
print(f"v10 explicit : E={rX['pole_energy']:.15f} Z={rX['pole_residue']:.15f}")
print(f"delta        : dE={rX['pole_energy']-r8['pole_energy']:+.3e} dZ={rX['pole_residue']-r8['pole_residue']:+.3e}")
gate("v10a WQQ=0 explicit P+Q reproduces v8 pole", abs(rX["pole_energy"]-r8["pole_energy"]) < 2e-12, f"dE={rX['pole_energy']-r8['pole_energy']:+.3e}")
gate("v10a WQQ=0 explicit P+Q reproduces v8 residue", abs(rX["pole_residue"]-r8["pole_residue"]) < 2e-12, f"dZ={rX['pole_residue']-r8['pole_residue']:+.3e}")
del rt
free_backend_memory()

print("\n[3] FULL ONE-STEP GLUEBALL W_QQ OPERATOR")
wrep = build_one_step_WQQ(gmodel, gq, label=f"glue K={V10A_GLUE_K}")
print(f"endpoint tests={wrep['endpoint_tests']:,}; nonzero endpoint contractions={wrep['endpoint_nonzero']:,}; unique canonical endpoints={wrep['endpoint_cache']:,}")
print(f"Haar occurrence patterns={wrep['patterns']}")
print(f"WQQ nnz={wrep['W'].nnz:,}; max|WQQ|={wrep['max_abs']:.3e}; directional Hermiticity err={wrep['hermiticity_error']:.3e}")
gate("v10a WQQ endpoint coverage uses only certified v9.1 Haar primitives", set(wrep["patterns"]).issubset(V10_SUPPORTED_ENDPOINT_PATTERNS), str(wrep["patterns"]))
gate("v10a one-step WQQ is Hermitian before symmetrization", wrep["hermiticity_error"] < 5e-12, f"err={wrep['hermiticity_error']:.3e}")
# This is a numerical certificate specific to the K=0 one-step physical bright range.
# It is NOT promoted to an all-Q theorem.
gate("v10a K=0 one-step glueball physical WQQ vanishes", wrep["max_abs"] < 5e-12, f"max={wrep['max_abs']:.3e}")

print("\n[4] LOW-ORDER REGRESSION OF THE EXPLICIT P+Q ENGINE")
cexp = _v10_mass_coeffs_explicit(gmodel, gq, wrep["W"])
print(f"m2 explicit={cexp[2]:+.12f} exact={M2_EX:+.12f}")
print(f"m3 explicit={cexp[3]:+.12f} exact={M3_EX:+.12f}")
print("m4 coefficient intentionally withheld: current Q1 range has zero WQQ but Q1->Q2 is nonempty.")
gate("v10a explicit-Q engine retains m2=11/306", abs(cexp[2]-M2_EX) < 8e-6, f"m2={cexp[2]:+.12g}")
gate("v10a explicit-Q engine retains v8 exact m3", abs(cexp[3]-M3_EX) < 8e-6, f"m3={cexp[3]:+.12g}")

print("\n[5] FULL T1 SOURCE-BLOCK AUDIT")
SG = v10_t1_source_gram()
print("S^T S =")
print(SG)
gate("v10a three-component T1 source Gram is I3", float(np.max(np.abs(SG-np.eye(3)))) < 2e-14, f"max err={np.max(np.abs(SG-np.eye(3))):.3e}")
orient = v10_orientation_pole_audit(V10A_TEST_U)
for pol, Epol, Zpol in orient:
    print(f"  axial plane {pol}: E={Epol:.15f} Z={Zpol:.15f}")
Espread = max(x[1] for x in orient)-min(x[1] for x in orient)
Zspread = max(x[2] for x in orient)-min(x[2] for x in orient)
gate("v10a cubic orientations give identical T1 pole", Espread < 3e-12, f"spread={Espread:.3e}")
gate("v10a cubic orientations give identical T1 residue", Zspread < 3e-12, f"spread={Zspread:.3e}")

print("\n[6] STRING W_QQ UNIT TEST — MANUAL CUBIC INJECTION OFF")
srows = [v10_string_c3_decomposition(Ls) for Ls in V10A_STRING_AUDIT_LENGTHS]
for r in srows:
    print(f"L={r['L']}: PP/L={r['PP_per_L']:+.12f}  (PQ+QP)/L={r['cross_per_L']:+.12f}  QQ/L={r['QQ_per_L']:+.12f}  raw/L={r['raw_per_L']:+.12f}  linked_s3={r['linked_s3']:+.12f}")
raw_spread = max(r["raw_per_L"] for r in srows)-min(r["raw_per_L"] for r in srows)
qq_spread = max(r["QQ_per_L"] for r in srows)-min(r["QQ_per_L"] for r in srows)
cross_spread = max(r["cross_per_L"] for r in srows)-min(r["cross_per_L"] for r in srows)
linked_spread = max(r["linked_s3"] for r in srows)-min(r["linked_s3"] for r in srows)
gate("v10a string QQ magnetic moment is extensive", qq_spread < 2e-12, f"spread={qq_spread:.3e}")
gate("v10a string PQ+QP magnetic moment is extensive", cross_spread < 2e-12, f"spread={cross_spread:.3e}")
gate("v10a string raw cubic moment is extensive", raw_spread < 2e-12, f"spread={raw_spread:.3e}")
gate("v10a string QQ/L = -16/17", max(abs(r["QQ_per_L"] + 16.0/17.0) for r in srows) < 2e-12)
gate("v10a string (PQ+QP)/L = -1/3", max(abs(r["cross_per_L"] + 1.0/3.0) for r in srows) < 2e-12)
gate("v10a string PP/L = 0", max(abs(r["PP_per_L"]) for r in srows) < 2e-12)
gate("v10a unified microscopic cubic string result gives s3=-61/408", max(abs(r["linked_s3"]-S3_EX) for r in srows) < 2e-12, f"spread={linked_spread:.3e}")

print("\n[7] Q1 -> Q2 PREFLIGHT FOR THE TRUE FOURTH-ORDER SCALAR")
q2 = v10_q2_preflight(gmodel, gq, parent=0)
print(f"anchored source-bright Q1 dimension : {q2['bright_q1']}")
print(f"connected Q1->W raw actions        : {q2['raw_actions']:,}")
print(f"unique canonical Q2 networks       : {q2['unique_canonical_networks']:,}")
print(f"flux classes                       : {q2['fluxclass']}")
print(f"local occurrence census            : {q2['occurrence_patterns']}")
gate("v10a Q1->Q2 layer is genuinely nonempty", q2["fluxclass"].get("new-key",0) > 0, str(q2["fluxclass"]))

print("\n[8] PROTECTED FOURTH-ORDER FIREWALLS — REFERENCE VALUES ONLY")
A3 = Fraction(5,48); B3S = Fraction(0,1); D3S = Fraction(0,1); ALPHA3 = Fraction(5,12); C3SQ = Fraction(-5,48)
print(f"A3^shp={A3}, B3^shp={B3S}, D3^shp={D3S}, c3^square={C3SQ}, alpha3={ALPHA3}")
print("STATUS: these are theorem-level targets for the NEXT Q2/folded operator extractor; they are NOT counted as v10a passes here.")

print("\n"+"="*128)
print("FINAL v10a GATE SUMMARY")
print("="*128)
new_gates = gates[V10A_GATE_START:]
for i, (name, ok, detail) in enumerate(new_gates, 1):
    print(f"{i:02d}. {'PASS' if ok else 'FAIL'} — {name}" + (f" :: {detail}" if detail else ""))
passed = sum(ok for _,ok,_ in new_gates)
print("-"*128)
print(f"PASSED {passed}/{len(new_gates)} v10a GATES")
if passed != len(new_gates):
    raise AssertionError("v10a hard gate failure; do not proceed to Q2/order-4 extraction")

print("\nV10A CONCLUSION")
print("---------------")
print("* The v5 global Gram quotient has been inverted into explicit orthonormal physical-Q coordinates without changing v8 physics.")
print("* The complete one-step K=0 glueball W_QQ matrix vanishes numerically in that physical quotient; the old v7 scalar-W_QQ interpretation remains retired.")
print("* The string sector independently has a nonzero genuine QQ magnetic moment: QQ/L=-16/17, with PQ+QP=-1/3 and raw=-65/51, yielding s3=-61/408 after vacuum subtraction.")
print("* The anchored glueball source has a nonempty Q1->Q2 layer, so the true O(u^4) scalar/rest problem lives beyond the one-step physical-Q manifold.")
print("* No m4_rest or C3_full^shp is reported.  The next code layer must build the Q2 H0 resolvent plus linked/folded marked-cluster subtraction and then test the protected mobility tensor before unblinding those quantities.")
