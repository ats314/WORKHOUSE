# HODGE v10a.24c — ROOTED FULL-T1 DUAL COLD ORACLE / GENERIC-ENDPOINT RETURN HOTFIX
# One self-contained Colab/A100 run.
import os
os.environ["PREFER_GPU"] = "1"
os.environ["GLUE_L"] = "5"
os.environ["V10A7_SUPPORT_POLS"] = "0,1,2"
os.environ["V10A7_RECHECK_Q1"] = "0"
os.environ["V10A7_UNBLIND"] = "0"
os.environ["V10A23_CLUSTER_POL"] = "2"

# v10a.2 A100 production configuration
import os
# v10a.12: keep tiny irregular Haar contractions from spawning nested BLAS pools.
os.environ.setdefault("OMP_NUM_THREADS","1")
os.environ.setdefault("OPENBLAS_NUM_THREADS","1")
os.environ.setdefault("MKL_NUM_THREADS","1")
os.environ.setdefault("NUMEXPR_NUM_THREADS","1")
os.environ.setdefault("PREFER_GPU","1")
os.environ.setdefault("GLUE_L","5")
os.environ.setdefault("V10A2_P_DEPTH","2")
os.environ.setdefault("V10A2_PROGRESS","1")
os.environ.setdefault("V5_PROGRESS","0")
os.environ.setdefault("V10A_PROGRESS","0")

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
import sys
import io
import faulthandler

# Colab/IPython replaces stderr with an ipykernel OutStream whose fileno()
# raises io.UnsupportedOperation.  Do NOT let the optional watchdog abort
# the production run.  Prefer the real process stderr when available; if
# that is unavailable, arm faulthandler on a plain temporary file.  The
# production heartbeat below remains the primary live-progress mechanism.
_V10A16_FH_ARMED = False
_V10A16_FH_FILE = None
try:
    _fh_stream = getattr(sys, "__stderr__", None)
    if _fh_stream is None:
        raise io.UnsupportedOperation("no sys.__stderr__")
    _fh_stream.fileno()
    faulthandler.enable(file=_fh_stream)
    faulthandler.dump_traceback_later(90, repeat=True, file=_fh_stream)
    _V10A16_FH_ARMED = True
except Exception:
    try:
        _V10A16_FH_FILE = open("/tmp/hodge_v10a16_faulthandler.log", "w", buffering=1)
        faulthandler.enable(file=_V10A16_FH_FILE)
        faulthandler.dump_traceback_later(
            90, repeat=True, file=_V10A16_FH_FILE
        )
        _V10A16_FH_ARMED = True
        print("[INFO] Colab stderr has no fileno(); watchdog redirected to "
              "/tmp/hodge_v10a16_faulthandler.log")
    except Exception as _fh_exc:
        print("[INFO] faulthandler watchdog disabled:", repr(_fh_exc))
        print("[INFO] timed production heartbeat remains enabled.")

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




import itertools
import numpy as np
from collections import defaultdict
from functools import lru_cache
from scipy.linalg import qr

def _v10a2_install_q2_haar(ns):
    # balanced k=3 Weingarten tensor
    ps,W=ns['lx_wg_fixed'](3)
    Ds=[]
    for sig in ps:
        D=np.zeros((3,)*6,dtype=np.float64)
        for r in np.ndindex((3,3,3)):
            br=[0,0,0]
            for i in range(3): br[sig[i]]=r[i]
            D[r[0],r[1],r[2],br[0],br[1],br[2]]=1.0
        Ds.append(D)
    T33=np.zeros((3,)*12,dtype=np.float64)
    for i,Di in enumerate(Ds):
        for j,Dj in enumerate(Ds):
            co=float(W[i][j])
            if co:
                T33 += co*np.einsum('abcABC,defDEF->adbecfADBECF',Di,Dj,optimize=True)
    # vectorized certified (4,1) pseudoinverse tensor
    EPS=ns['_FAST_EPS']; Inv41=[]
    for r in range(4):
        I=np.zeros((3,)*5,dtype=np.float64)
        for idx in np.ndindex((3,)*5):
            maj=idx[:4]; k=idx[4]
            if maj[r]==k:
                I[idx]=EPS[tuple(maj[j] for j in range(4) if j!=r)]
        Inv41.append(I)
    T41=np.zeros((3,)*10,dtype=np.float64)
    for r,I in enumerate(Inv41):
        for s,J in enumerate(Inv41):
            co=float(ns['_V9_C41'][r,s])
            if co:
                T41 += co*np.einsum('abcde,fghij->afbgchdiej',I,J,optimize=True)
    ns['_V9_T41']=T41
    # pure six-fundamental SU(3) singlet projector. Ten epsilon-pair invariants,
    # rank five; choose an independent basis and invert its Gram matrix.
    parts=[]
    for comb in itertools.combinations(range(1,6),2):
        A=(0,)+comb; B=tuple(i for i in range(6) if i not in A); parts.append((A,B))
    Inv60=[]
    for A,B in parts:
        I=np.zeros((3,)*6,dtype=np.float64)
        for idx in np.ndindex((3,)*6):
            I[idx]=EPS[tuple(idx[i] for i in A)]*EPS[tuple(idx[i] for i in B)]
        Inv60.append(I)
    G60=np.array([[np.tensordot(A,B,axes=6) for B in Inv60] for A in Inv60],dtype=np.float64)
    _,_,piv=qr(G60,pivoting=True)
    rank60=int(np.linalg.matrix_rank(G60,tol=1e-10)); keep=list(map(int,piv[:rank60]))
    I5=[Inv60[i] for i in keep]; C5=np.linalg.inv(G60[np.ix_(keep,keep)])
    T60=np.zeros((3,)*12,dtype=np.float64)
    for i,I in enumerate(I5):
        for j,J in enumerate(I5):
            co=float(C5[i,j])
            if co:
                T60 += co*np.einsum('abcdef,ghijkl->agbhcidjekfl',I,J,optimize=True)
    M60=np.transpose(T60,(0,2,4,6,8,10,1,3,5,7,9,11)).reshape(729,729)
    cert={
        'wg3_inverse_error': float(np.max(np.abs(np.array([[float(x) for x in row] for row in W]) @ np.array([[3**ns['lx_pcycles'](ns['lx_pcompose'](ns['lx_pinv'](a),b)) for b in ps] for a in ps],dtype=float) - np.eye(6)))),
        'rank60': rank60,
        'T60_trace': float(np.trace(M60)),
        'T60_symmetry_error': float(np.max(np.abs(M60-M60.T))),
        'T60_idempotence_error': float(np.max(np.abs(M60@M60-M60))),
    }
    supported={(1,1),(2,2),(3,3),(3,0),(0,3),(4,1),(1,4),(6,0),(0,6)}
    @lru_cache(maxsize=500000)
    def _canon(a,b):
        occ,part=ns['lx_combine_bra_ket'](a,b)
        by=defaultdict(lambda:{True:[],False:[]})
        for i,(l,t) in enumerate(occ): by[int(l)][bool(t)].append(i)
        args=[]
        for g in by.values():
            U,B=g[True],g[False]; pat=(len(U),len(B))
            if (pat[0]-pat[1])%3: return 0.0
            if pat==(1,1): pos=U+B; ten=ns['_FAST_T11']
            elif pat==(2,2): pos=U+B; ten=ns['_FAST_T22']
            elif pat==(3,3): pos=U+B; ten=T33
            elif pat in ((3,0),(0,3)): pos=U if len(U)==3 else B; ten=ns['_FAST_T30']
            elif pat in ((4,1),(1,4)): pos=(U+B) if len(U)==4 else (B+U); ten=T41
            elif pat in ((6,0),(0,6)): pos=U if len(U)==6 else B; ten=T60
            else: raise RuntimeError(f'Q2 Haar unsupported occurrence pattern {pat}')
            inds=[]
            for p0 in pos: inds.extend((int(part[2*p0]),int(part[2*p0+1])))
            args.extend((ten,inds))
        if not args: return float(ns['N']**len(set(part)))
        return float(ns['oe'].contract(*args,[],optimize='greedy'))
    def haar(a,b):
        aa,bb=ns['_joint_canon_states'](a,b)
        # symmetric cache key while preserving the joint link labels
        ka=(aa.occ,aa.part); kb=(bb.occ,bb.part)
        if kb < ka: aa,bb=bb,aa
        return _canon(aa,bb)
    return haar,supported,cert,_canon




# =============================================================================
# v10a.2 FULL-T1 / SATURATED-P Q2 FRONTIER CERTIFICATE
# =============================================================================
# This run does NOT extract m4_rest or C3_full^shp.  It removes two concrete
# misclassifications that would make a naive Q2 resolvent invalid:
#   (i) the retained degenerate E0=8/3 space must contain the full T1 plaquette
#       triplet, not one polarization;
#   (ii) the Q2 complement must be defined relative to the retained K=2 simple-
#        loop P graph, so deformed loops are not accidentally divided through as Q.
# The actual physical Q2 resolvent comes only after this frontier passes.

from scipy.sparse import hstack
from collections import Counter, defaultdict
from fractions import Fraction

V10A2_P_DEPTH=int(os.environ.get("V10A2_P_DEPTH","2"))
V10A2_PROGRESS=int(os.environ.get("V10A2_PROGRESS","1"))
V10A2_GRAM_TOL=float(os.environ.get("V10A2_GRAM_TOL",str(V10A_GRAM_TOL)))
V10A2_GATE_START=len(gates)


def _v10a2_full_t1_source_block(model):
    S=np.zeros((len(model['E_P']),3),dtype=np.float64)
    pols=((1,2),(0,2),(0,1))
    for a,pol in enumerate(pols):
        ff=[f for f,(_,i,j) in enumerate(faces) if (i,j)==pol]
        for f in ff:
            key,sgn,_=canonical_codd(B2[:,f])
            if key not in model['index']:
                raise RuntimeError(f"full-T1 source plaquette missing from P for {pol}")
            S[model['index'][key],a]+=float(sgn)/math.sqrt(len(ff))
    return S


def _v10a2_anchor_block(model):
    A=np.zeros((len(model['E_P']),3),dtype=np.float64)
    for a,pol in enumerate(((1,2),(0,2),(0,1))):
        f=next(f for f,(v,i,j) in enumerate(faces) if v==(0,0,0) and (i,j)==pol)
        key,sgn,_=canonical_codd(B2[:,f])
        A[model['index'][key],a]=float(sgn)
    return A


def _v10a2_source_facing_q(model,S,keep_vectors=True):
    """Expose only global-Q collision blocks touched by the full T1 source.

    Every raw record in a touched collision block is retained, not just source
    records, so the global Gram recoupling is unchanged.  The hard regression is
    ((B B^T-K_lambda) S)=0 for every Schur block.
    """
    groups=_v9_collision_groups(model['v9_collisions'])
    srcrows=set(np.flatnonzero(np.linalg.norm(S,axis=1)>1e-14).tolist())
    items=[(key,recs) for key,recs in groups.items() if any(int(r.parent) in srcrows for r in recs)]
    items.sort(key=lambda kv:(float(kv[0][1]),repr(kv[0][0])))
    nP=len(model['E_P'])
    Bblocks=[]; Eq=[]; qvecs=[]; metas=[]
    rawdim=phys=nullity=0; mineig=float('inf'); ortherr=0.0
    Kacc=defaultdict(lambda:csr_matrix((nP,nP),dtype=np.float64))
    t0=time.time()
    for ib,(key,recs) in enumerate(items):
        raw=[_v10_physical_raw_vec(model,r) for r in recs]
        n=len(raw); rawdim+=n
        G=np.zeros((n,n),dtype=np.float64)
        for i in range(n):
            for j in range(i,n):
                G[i,j]=G[j,i]=_vec_inner_fast(raw[i],raw[j])
        G=0.5*(G+G.T)
        ev,U=np.linalg.eigh(G)
        if len(ev): mineig=min(mineig,float(ev[0]))
        scale=max(1.0,float(np.max(ev)) if len(ev) else 1.0)
        mask=ev>V10A2_GRAM_TOL*scale
        r=int(np.count_nonzero(mask)); nullity+=n-r
        if not r: continue
        lv=ev[mask]; Ur=U[:,mask]
        X=Ur/np.sqrt(lv)[None,:]
        parents=sorted(set(int(x.parent) for x in recs)); pidx={p:i for i,p in enumerate(parents)}
        C=np.zeros((len(parents),n),dtype=np.float64)
        for i,rec in enumerate(recs): C[pidx[int(rec.parent)],i]+=1.0
        Bl=C@Ur@np.diag(np.sqrt(lv))
        rr=[];cc=[];vv=[]
        for il,p in enumerate(parents):
            for j,x in enumerate(Bl[il]):
                if abs(x)>1e-14: rr.append(p);cc.append(j);vv.append(float(x))
        Bg=coo_matrix((vv,(rr,cc)),shape=(nP,r),dtype=np.float64).tocsr()
        Bblocks.append(Bg); Kacc[float(key[1])]=Kacc[float(key[1])]+Bg@Bg.T
        qslice=(phys,phys+r); metas.append({'key':key,'X':X,'records':recs,'q_slice':qslice})
        if keep_vectors:
            for a in range(r):
                d=defaultdict(float)
                for ci,rv in zip(X[:,a],raw):
                    if abs(ci)>1e-15:
                        for st,x in rv.items(): d[st]+=float(ci)*float(x)
                v={st:x for st,x in d.items() if abs(x)>2e-13}
                qvecs.append(v)
                nrm=0.0
                for sa,ca in v.items():
                    for sb,cb in v.items(): nrm+=ca*cb*_vec_inner_fast({sa:1.0},{sb:1.0})
                ortherr=max(ortherr,abs(nrm-1.0))
        Eq.extend([float(key[1])]*r);phys+=r
        if V10A2_PROGRESS and len(items)>500 and (ib+1)%500==0:
            print(f"      source-Q quotient {ib+1:,}/{len(items):,}; physical={phys:,}; elapsed={time.time()-t0:.1f}s")
    B=hstack(Bblocks,format='csr') if Bblocks else csr_matrix((nP,0),dtype=np.float64)
    errs=[]
    for lam,vac,K in model['kernels']:
        D=np.asarray((Kacc[float(lam)]-K)@S)
        errs.append(float(np.max(np.abs(D))) if D.size else 0.0)
    return {'B_W':-B,'E_Q':np.asarray(Eq,dtype=np.float64),'qvecs':qvecs,
            'blocks':metas,'phys_dim':phys,'raw_dim':rawdim,'nullity':nullity,
            'groups':len(items),'src_kernel_error':max(errs,default=0.0),
            'gram_min_eig':mineig if mineig<float('inf') else 0.0,'orth_error':ortherr}


def _v10a2_flux_to_p(model,k):
    q=np.zeros(E,dtype=np.int8)
    for l,z in k: q[int(l)]=int(z)
    if not is_simple_single_loop(q): return None
    ck,_,_=canonical_codd(q)
    return model['index'].get(ck)


def _v10a2_q2_frontier_census(model,qquot,anchor,supported):
    Y=np.asarray(qquot['B_W'].T@anchor)
    bright=np.flatnonzero(np.linalg.norm(Y,axis=1)>1e-12)
    q1keys=set()
    for v in qquot['qvecs']:
        for st in v: q1keys.add(_v9_flux_key_state(st))
    classes=Counter(); retained_depth=Counter(); occurrence=Counter(); candidates={}; raw=0
    for j in bright:
        for st,c in qquot['qvecs'][int(j)].items():
            if abs(c)<1e-13: continue
            cand=set()
            for l,_ in st.occ: cand.update(link_faces[int(l)])
            for f in cand:
                for o in (-1,+1):
                    raw+=1
                    prod=lx_tensor_product(st,lx_trace_state(model['v9_fs_cached'](f,o)))
                    fk=_v9_flux_key_state(prod)
                    ip=_v10a2_flux_to_p(model,fk)
                    if ip is not None:
                        cls='P-retained-flux';retained_depth[int(model['depth'][model['keys'][ip]])]+=1
                    elif fk in q1keys: cls='Q1-key'
                    else: cls='new-Q2'
                    classes[cls]+=1
                    cc=_joint_canon_states(prod)[0]
                    candidates[(cc.occ,cc.part)]=cc
                    by=defaultdict(lambda:[0,0])
                    for l,t in prod.occ: by[int(l)][0 if t else 1]+=1
                    for x in by.values(): occurrence[tuple(x)]+=1
    byflux=defaultdict(list)
    for st in candidates.values(): byflux[_v9_flux_key_state(st)].append(st)
    pairpats=set(); pairs=0
    for ls in byflux.values():
        for i,a in enumerate(ls):
            for b in ls[i:]:
                pairs+=1; pairpats.update(_v10_endpoint_patterns(a,b))
    bad=set(pairpats)-set(supported)
    return {'bright_q1':len(bright),'raw_actions':raw,'classes':dict(classes),
            'retained_by_depth':dict(retained_depth),'unique_candidates':len(candidates),
            'flux_groups':len(byflux),'pair_tests':pairs,'pair_patterns':tuple(sorted(pairpats)),
            'unsupported_pair_patterns':tuple(sorted(bad)),'local_occurrence':dict(occurrence)}


# --- exact Q2 H0 resonance audit on the minimal full-T1 plaquette fiber -------
_V10A2_IMAP={1:(1,0),-1:(0,1),2:(2,0),-2:(0,2),8:(1,1)}
def _v10a2_energy_dyn(r):
    p,q=r; return Fraction(p*p+q*q+p*q+3*p+3*q,6)
def _v10a2_fuse(r,sg):
    p,q=r; out=[]
    if sg>0:
        out.append((p+1,q))
        if p>=1: out.append((p-1,q+1))
        if q>=1: out.append((p,q-1))
    else:
        out.append((p,q+1))
        if q>=1: out.append((p+1,q-1))
        if p>=1: out.append((p-1,q))
    return tuple(out)
def _v10a2_sig_dyn(sig): return tuple(sorted((int(l),)+_V10A2_IMAP[int(r)] for l,r in sig))
def _v10a2_sig_conj(sig): return tuple(sorted((l,q,p) for l,p,q in sig))
def _v10a2_sig_canon(sig):
    c=_v10a2_sig_conj(sig);return min(sig,c)
def _v10a2_sig_E(sig): return sum((_v10a2_energy_dyn((p,q)) for _,p,q in sig),Fraction(0))

def _v10a2_project_action(model,v,sig,face,orient):
    fs=model['v9_fs_cached'](face,orient);fd={int(l):int(s) for l,s in fs}
    cur={int(l):(int(p),int(q)) for l,p,q in _v10a2_sig_dyn(sig)}
    prod=defaultdict(Fraction)
    for st,c in v.items(): prod[lx_tensor_product(st,lx_trace_state(fs))]+=c
    chans=[(dict(prod),dict(cur))]
    for l,sg in fd.items():
        r=cur.get(l,(0,0));opts=_v10a2_fuse(r,sg);eigs=tuple(_v10a2_energy_dyn(x) for x in opts)
        if len(set(eigs))!=len(eigs): raise RuntimeError(f"degenerate local fusion {r},{sg},{opts}")
        nxt=[]
        for vec,smap in chans:
            for rr,ee in zip(opts,eigs):
                pv=vec if len(opts)==1 else _project_link(vec,l,ee,eigs)
                if not pv: continue
                sm=dict(smap)
                if rr==(0,0): sm.pop(l,None)
                else: sm[l]=rr
                nxt.append((pv,sm))
        chans=nxt
    return [(vec,tuple(sorted((l,p,q) for l,(p,q) in sm.items()))) for vec,sm in chans]


def _v10a2_vec_norm2(v,haar):
    groups=defaultdict(list)
    for st,c in v.items(): groups[_v9_flux_key_state(st)].append((st,float(c)))
    tot=0.0; pats=set()
    for ls in groups.values():
        for a,ca in ls:
            for b,cb in ls:
                pats.update(_v10_endpoint_patterns(a,b));tot+=ca*cb*haar(a,b)
    return float(tot),pats


def _v10a2_e0_resonance_audit(haar):
    # Rebuild only K=0 with all 81 plaquette states retained.  This is a cheap
    # exact degeneracy check independent of the large K=2 frontier model.
    mdl=build_global_glueball_model(0)
    q=build_physical_q_quotient(mdl,True,'full-T1 K0 resonance-Q1')
    groups=_v9_collision_groups(mdl['v9_collisions'])
    p=np.zeros(len(mdl['E_P']));p[0]=1.0;Ezero=E0_PLAQ
    y=np.asarray(q['B_W'].T@p).ravel(); z=np.zeros_like(y);mask=np.abs(y)>1e-12
    z[mask]=y[mask]/(Ezero-q['E_Q'][mask])
    rawitems=[]
    for meta in q['blocks']:
        a,b=meta['q_slice'];zl=z[a:b]
        if np.max(np.abs(zl),initial=0)<1e-14: continue
        d=meta['X']@zl; recs=groups[meta['key']]
        for di,rec in zip(d,recs):
            if abs(di)>1e-13: rawitems.append((float(di),rec))
    agg=defaultdict(lambda:defaultdict(float))
    for di,rec in rawitems:
        for conj,sgn in ((False,-1.0),(True,+1.0)):
            vv,_=mdl['v9_joint_vec'](rec,conj)
            isig=mdl['v9_rec_sig'](rec); isig=_rep_sig_conj(isig) if conj else isig
            cand=set()
            for st in vv:
                for l,_ in st.occ: cand.update(link_faces[int(l)])
            for f in cand:
                for o in (-1,+1):
                    for pv,osig in _v10a2_project_action(mdl,vv,isig,f,o):
                        if _v10a2_sig_E(osig)!=Fraction(8,3): continue
                        A=agg[_v10a2_sig_canon(osig)];fac=sgn*di/math.sqrt(2.0)
                        for st,c in pv.items(): A[st]+=fac*float(c)
    for k in list(agg):
        agg[k]={st:c for st,c in agg[k].items() if abs(c)>1e-12}
        if not agg[k]: del agg[k]
    psig={}
    pvec={}
    for i,qq in enumerate(mdl['states']):
        sig=tuple((int(l),1,0) if qq[l]>0 else (int(l),0,1) for l in np.flatnonzero(qq))
        psig[_v10a2_sig_canon(sig)]=i
        st=lx_trace_state(ordered_loop_steps(qq,links,shift));stc=lx_trace_state(ordered_loop_steps(-np.asarray(qq,dtype=np.int8),links,shift))
        pvec[i]={st:1/math.sqrt(2),stc:-1/math.sqrt(2)}
    pcoef=np.asarray(q['B_W']@z).ravel();missing=[cs for cs in agg if cs not in psig]
    residual={}
    for cs,A0 in agg.items():
        A=dict(A0);i=psig.get(cs)
        if i is not None:
            aa=float(pcoef[i])
            for st,c in pvec[i].items(): A[st]=A.get(st,0.0)-aa*c
        residual[cs]={st:c for st,c in A.items() if abs(c)>1e-11}
    norms=[];pats=set()
    for v in residual.values():
        if not v: continue
        n,pp=_v10a2_vec_norm2(v,haar); norms.append(n);pats.update(pp)
    return {'raw_source_coeffs':len(rawitems),'E0_groups':len(agg),'missing_from_P':len(missing),
            'nonzero_P_returns':int(np.count_nonzero(np.abs(pcoef)>1e-12)),
            'residual_norm2_sum':float(sum(norms)),'residual_norm2_max':float(max([abs(x) for x in norms] or [0.0])),
            'residual_patterns':tuple(sorted(pats))}




# =============================================================================
# HODGE v10a.3 — PHYSICAL-Q2 + DIRECT FOURTH-ORDER MOBILITY FIREWALL
# =============================================================================
# PURPOSE
# -------
# This run is the first post-v10a.2 calculation allowed to test the protected
# fourth-order mobility coefficients.  It has two independent but coupled tracks:
#
#   A. PHYSICAL-Q2 CERTIFICATE
#      Starting from the exact first-resolvent C- state of each of the three
#      anchored T1 plaquettes, apply a second magnetic insertion, resolve the
#      exact joint-link H0 irreps, and Gram-project against
#          retained K=2 simple-loop P  +  the COMPLETE relevant global Q1 block.
#      The positive residual is the physical source-adapted Q2 complement.
#
#   B. DIRECT FOURTH-ORDER FIREWALL
#      Independently propagate the full connected microscopic trace-network state
#          P0 W R W R W R W P0
#      with exact joint-link H0 projectors.  No fourth-order theorem coefficient
#      is supplied to this propagation.  Energy folds are deliberately omitted;
#      the project theorem proves that A^shp, B^shp, D^shp are fold-neutral.
#      The rest scalar and full C^shp remain BLINDED / UNCLAIMED.
#
# IMPORTANT
# ---------
# * Default L=5: this is the clean isolation volume.  The shape fit uses only
#   allowed L=5 Bloch momenta, so no continuous-momentum interpolation is hidden.
# * Connected magnetic insertions only.  Disconnected vacuum bubbles belong to
#   the linked/folded scalar sector and are not needed for the protected A/B/D
#   mobility firewall.
# * No W22 is built.  It first enters one order later.
# =============================================================================

from scipy.linalg import eigvalsh

V10A3_PROGRESS = int(os.environ.get("V10A3_PROGRESS", "1"))
V10A3_COEFF_TOL = float(os.environ.get("V10A3_COEFF_TOL", "2e-13"))
V10A3_NORM_TOL = float(os.environ.get("V10A3_NORM_TOL", "2e-10"))
V10A3_GRAM_TOL = float(os.environ.get("V10A3_GRAM_TOL", "2e-11"))
V10A3_SHAPE_TOL = float(os.environ.get("V10A3_SHAPE_TOL", "2e-7"))
V10A3_FIFTH_TOL = float(os.environ.get("V10A3_FIFTH_TOL", "5e-7"))
V10A3_P_DEPTH = int(os.environ.get("V10A3_P_DEPTH", "2"))
V10A3_GATE_START = len(gates)

T1_POLS = ((1,2),(0,2),(0,1))
A3_TARGET = 5.0/48.0
B3_TARGET = 0.0
D3_TARGET = 0.0
ALPHA3_TARGET = 5.0/12.0


def _v10a3_prune(v, tol=V10A3_COEFF_TOL):
    return {st: float(c) for st,c in v.items() if abs(float(c)) > tol}


def _v10a3_add_vec(dst, src, scale=1.0):
    for st,c in src.items():
        dst[st] += float(scale)*float(c)


def _v10a3_state_stats(state):
    return len(state), sum(len(v) for v in state.values())


def _v10a3_vec_inner(v, w, haar):
    """Physical inner product with exact center prefilter and extended SU(3) Haar."""
    if not v or not w:
        return 0.0
    ga=defaultdict(list); gb=defaultdict(list)
    for st,c in v.items(): ga[_v9_flux_key_state(st)].append((st,float(c)))
    for st,c in w.items(): gb[_v9_flux_key_state(st)].append((st,float(c)))
    ans=0.0
    for k,la in ga.items():
        lb=gb.get(k)
        if not lb: continue
        for a,ca in la:
            for b,cb in lb:
                ans += ca*cb*haar(a,b)
    return float(ans)


def _v10a3_vec_norm(v, haar):
    x=_v10a3_vec_inner(v,v,haar)
    if x < -V10A3_NORM_TOL:
        raise RuntimeError(f"physical vector has negative norm2 {x:.3e}")
    return max(0.0,float(x))


def _v10a3_sig_vec_add(state, sig, vec, scale=1.0):
    d=state.setdefault(sig,defaultdict(float))
    _v10a3_add_vec(d,vec,scale)


def _v10a3_compress_state(state):
    out={}
    for sig,v in state.items():
        z=_v10a3_prune(v)
        if z: out[sig]=z
    return out


def _v10a3_candidate_faces_vec(v):
    cand=set()
    for st in v:
        for l,_ in st.occ:
            cand.update(link_faces[int(l)])
    return cand


def _v10a3_project_action_dyn(model,v,sig,face,orient):
    """Recursive form of the v10a.2 local projector; input/output signatures are (link,p,q)."""
    fs=model['v9_fs_cached'](face,orient); fd={int(l):int(s) for l,s in fs}
    cur={int(l):(int(p),int(q)) for l,p,q in sig}
    prod=defaultdict(Fraction)
    for st,c in v.items(): prod[lx_tensor_product(st,lx_trace_state(fs))]+=c
    chans=[(dict(prod),dict(cur))]
    for l,sg in fd.items():
        r=cur.get(l,(0,0)); opts=_v10a2_fuse(r,sg); eigs=tuple(_v10a2_energy_dyn(x) for x in opts)
        if len(set(eigs))!=len(eigs): raise RuntimeError(f"degenerate local fusion {r},{sg},{opts}")
        nxt=[]
        for vec,smap in chans:
            for rr,ee in zip(opts,eigs):
                pv=vec if len(opts)==1 else _project_link(vec,l,ee,eigs)
                if not pv: continue
                sm=dict(smap)
                if rr==(0,0): sm.pop(l,None)
                else: sm[l]=rr
                nxt.append((pv,sm))
        chans=nxt
    return [(vec,tuple(sorted((l,p,q) for l,(p,q) in sm.items()))) for vec,sm in chans]


def _v10a3_apply_W(model, state, progress_label="W"):
    """Connected magnetic action W=-M, immediately resolved into exact H0 irreps."""
    out={}; actions=channels=0
    items=list(state.items())
    t0=time.time()
    for ii,(sig,v) in enumerate(items):
        cand=_v10a3_candidate_faces_vec(v)
        for f in cand:
            for o in (-1,+1):
                actions += 1
                pcs=_v10a3_project_action_dyn(model,v,sig,f,o)
                for pv,osig in pcs:
                    channels += 1
                    _v10a3_sig_vec_add(out,osig,pv,-1.0)
        if V10A3_PROGRESS and len(items)>100 and (ii+1)%max(1,len(items)//5)==0:
            ns,nt=_v10a3_state_stats(out)
            print(f"      {progress_label} {ii+1:,}/{len(items):,} signature blocks; out={ns:,}/{nt:,}; elapsed={time.time()-t0:.1f}s")
    return _v10a3_compress_state(out), {'actions':actions,'channels':channels}


def _v10a3_face_state(face):
    q=np.asarray(B2[:,int(face)],dtype=np.int8)
    st=lx_trace_state(ordered_loop_steps(q,links,shift))
    stc=lx_trace_state(ordered_loop_steps(-q,links,shift))
    sig=_v10a2_sig_dyn(_rep_sig_from_flux(q))
    sigc=_v10a2_sig_dyn(_rep_sig_from_flux(-q))
    s=1.0/math.sqrt(2.0)
    return {sig:{st:s},sigc:{stc:-s}}


def _v10a3_face_pvec(face):
    q=np.asarray(B2[:,int(face)],dtype=np.int8)
    st=lx_trace_state(ordered_loop_steps(q,links,shift))
    stc=lx_trace_state(ordered_loop_steps(-q,links,shift))
    s=1.0/math.sqrt(2.0)
    return {st:s,stc:-s}


def _v10a3_physical_blocks(state):
    """Combine conjugate H0 signatures into physical C- blocks."""
    out=defaultdict(lambda:defaultdict(float))
    for sig,v in state.items():
        cs=_v10a2_sig_canon(sig); Esg=_v10a2_sig_E(sig)
        _v10a3_add_vec(out[(cs,Esg)],v,1.0)
    return {k:_v10a3_prune(v) for k,v in out.items() if _v10a3_prune(v)}


def _v10a3_residue_key_vec(v):
    ks=set()
    for st in v:
        k=_v9_flux_key_state(st)
        kc=tuple(sorted((int(l),-int(s)) for l,s in k))
        ks.add(min(k,kc))
    if len(ks)!=1:
        raise RuntimeError(f"physical block has {len(ks)} center-residue classes")
    return next(iter(ks))


def _v10a3_p0_catalog():
    faces0=[]; vecs=[]; keymap=defaultdict(list)
    for f in range(P):
        v,a,b=faces[f]
        q=np.asarray(B2[:,f],dtype=np.int8)
        sig=_v10a2_sig_dyn(_rep_sig_from_flux(q))
        cs=_v10a2_sig_canon(sig)
        key=(cs,_v10a2_sig_E(sig))
        faces0.append(f); vecs.append(_v10a3_face_pvec(f)); keymap[key].append(f)
    return faces0,vecs,keymap


P0_FACES,P0_VECS,P0_BY_SIG=_v10a3_p0_catalog()


def _v10a3_reduced_resolvent(state, haar, label="R"):
    """R=(E0-H0)^-1 on the complement of the full plaquette E0 band."""
    out={}; resonance_max=0.0; resonance_groups=0
    blocks=_v10a3_physical_blocks(state)
    # E0 physical residual must vanish after full plaquette subtraction.
    for (cs,Esg),v0 in blocks.items():
        if Esg != Fraction(8,3):
            continue
        resonance_groups += 1
        v=dict(v0)
        for f in P0_BY_SIG.get((cs,Esg),()):
            pv=P0_VECS[f]
            ov=_v10a3_vec_inner(pv,v,haar)
            if abs(ov)>V10A3_COEFF_TOL:
                for st,c in pv.items(): v[st]=v.get(st,0.0)-ov*c
        v=_v10a3_prune(v)
        n2=_v10a3_vec_norm(v,haar)
        resonance_max=max(resonance_max,n2)
    if resonance_max > V10A3_NORM_TOL:
        raise RuntimeError(f"{label}: unresolved physical E0 resonance norm2={resonance_max:.3e}")
    for sig,v in state.items():
        Esg=_v10a2_sig_E(sig)
        if Esg == Fraction(8,3):
            continue
        den=float(Fraction(8,3)-Esg)
        if abs(den)<1e-14: raise RuntimeError(f"{label}: zero denominator outside P0")
        out[sig]={st:float(c)/den for st,c in v.items()}
    return _v10a3_compress_state(out), {'E0_groups':resonance_groups,'E0_residual_norm2_max':resonance_max}


def _v10a3_project_P0(state, haar):
    """Return coefficients in the raw oriented plaquette C- basis."""
    blocks=_v10a3_physical_blocks(state)
    out=np.zeros(P,dtype=np.float64)
    for key,flist in P0_BY_SIG.items():
        v=blocks.get(key)
        if not v: continue
        for f in flist:
            out[f]=_v10a3_vec_inner(P0_VECS[f],v,haar)
    return out


def _v10a3_build_retained_p_catalog(model):
    by=defaultdict(list); split={}
    for i,q in enumerate(model['states']):
        q=np.asarray(q,dtype=np.int8)
        st=lx_trace_state(ordered_loop_steps(q,links,shift)); stc=lx_trace_state(ordered_loop_steps(-q,links,shift))
        sig=_v10a2_sig_dyn(_rep_sig_from_flux(q)); sigc=_v10a2_sig_dyn(_rep_sig_from_flux(-q))
        cs=_v10a2_sig_canon(sig); Esg=_v10a2_sig_E(sig)
        s=1/math.sqrt(2.0); pv={st:s,stc:-s}
        rk=_v10a3_residue_key_vec(pv)
        by[(rk,Esg)].append((i,pv))
        split[i]=((sig,{st:s}),(sigc,{stc:-s}))
    return by,split


def _v10a3_collision_groups_all(model):
    return _v9_collision_groups(model['v9_collisions'])


def _v10a3_q1_group_basis(model, residue_key, Esg, haar, cache):
    key=(residue_key,Fraction(Esg))
    if key in cache: return cache[key]
    recs=_v10a3_collision_groups_all(model).get(key,[])
    if not recs:
        z={'qvecs':[],'rank':0,'raw_dim':0,'min_eig':0.0,'orth_err':0.0}
        cache[key]=z; return z
    raw=[_v10_physical_raw_vec(model,r) for r in recs]
    n=len(raw); G=np.zeros((n,n),dtype=np.float64)
    for i in range(n):
        for j in range(i,n):
            G[i,j]=G[j,i]=_v10a3_vec_inner(raw[i],raw[j],haar)
    G=0.5*(G+G.T); ev,U=np.linalg.eigh(G)
    scale=max(1.0,float(np.max(ev)) if len(ev) else 1.0)
    if len(ev) and float(ev[0]) < -2e-8:
        raise RuntimeError(f"Q1 group {key}: non-PSD Gram min={ev[0]:.3e}")
    keep=ev>V10A3_GRAM_TOL*scale
    qvecs=[]; orth=0.0
    if np.any(keep):
        X=U[:,keep]/np.sqrt(ev[keep])[None,:]
        for a in range(X.shape[1]):
            d=defaultdict(float)
            for ci,rv in zip(X[:,a],raw): _v10a3_add_vec(d,rv,float(ci))
            v=_v10a3_prune(d); qvecs.append(v)
            orth=max(orth,abs(_v10a3_vec_norm(v,haar)-1.0))
    z={'qvecs':qvecs,'rank':len(qvecs),'raw_dim':n,
       'min_eig':float(ev[0]) if len(ev) else 0.0,'orth_err':orth}
    cache[key]=z; return z


def _v10a3_subtract_retained_P_physical(v, residue_key, Esg, pcat, haar):
    r=dict(v); coeff=[]
    for i,pv in pcat.get((residue_key,Esg),()):
        ov=_v10a3_vec_inner(pv,r,haar)
        coeff.append((i,ov))
        if abs(ov)>V10A3_COEFF_TOL:
            for st,c in pv.items(): r[st]=r.get(st,0.0)-ov*c
    return _v10a3_prune(r),coeff


def _v10a3_subtract_q1_physical(v, residue_key, Esg, model, haar, q1cache):
    qg=_v10a3_q1_group_basis(model,residue_key,Esg,haar,q1cache)
    r=dict(v); ovs=[]
    for qv in qg['qvecs']:
        ov=_v10a3_vec_inner(qv,r,haar); ovs.append(ov)
        if abs(ov)>V10A3_COEFF_TOL:
            for st,c in qv.items(): r[st]=r.get(st,0.0)-ov*c
    return _v10a3_prune(r),ovs,qg


def _v10a3_extract_first_q1(state_w1, model, pcat, psplit, haar):
    """Subtract saturated retained-P from the first magnetic layer; remainder is Q1."""
    state={sig:dict(v) for sig,v in state_w1.items()}
    blocks=_v10a3_physical_blocks(state)
    max_p_res=0.0
    for (cs,Esg),v in blocks.items():
        rk=_v10a3_residue_key_vec(v)
        # subtract matching retained P vectors directly from signature-separated state
        for i,pv in pcat.get((rk,Esg),()):
            ov=_v10a3_vec_inner(pv,v,haar)
            if abs(ov)>V10A3_COEFF_TOL:
                for sigi,part in psplit[i]:
                    d=state.setdefault(sigi,{})
                    for st,c in part.items(): d[st]=d.get(st,0.0)-ov*c
    state=_v10a3_compress_state(state)
    # The residue is the physical first Q layer; E0 must already be absent.
    return state, {'p_projection_residual':max_p_res}


def _v10a3_q1_completeness(q1_states, model, haar, q1cache):
    """Verify each anchored first-layer physical remainder lies in the complete global Q1 collision span.

    Because the Hamiltonian and Gram metric are translation covariant, certifying all three
    anchored T1 orientations certifies their translated source orbit as well.
    """
    max_res=0.0; blocks=0; ranks=[]
    for state in q1_states:
        for (cs,Esg),v0 in _v10a3_physical_blocks(state).items():
            rk=_v10a3_residue_key_vec(v0)
            r,ovs,qg=_v10a3_subtract_q1_physical(v0,rk,Esg,model,haar,q1cache)
            n2=_v10a3_vec_norm(r,haar); max_res=max(max_res,n2); blocks+=1; ranks.append(qg['rank'])
    return {'blocks':blocks,'max_residual_norm2':max_res,'max_group_rank':max(ranks,default=0)}


def _v10a3_q2_certificate(q2_states, model, pcat, haar, q1cache):
    """Gram-project three source-adapted second-step vectors against P + full relevant Q1."""
    bykey=defaultdict(lambda:[{}, {}, {}])
    for a,state in enumerate(q2_states):
        for (cs,Esg),v in _v10a3_physical_blocks(state).items():
            rk=_v10a3_residue_key_vec(v)
            key=(cs,Esg,rk)
            bykey[key][a]=v
    total_rank=raw_cols=0; min_eval=0.0; min_gap=float('inf'); max_orth=0.0
    rank_tol=[0,0,0]
    q2_blocks=[]; q1ranks=[]; p_removed=q1_removed=0
    for key,cols0 in bykey.items():
        cs,Esg,rk=key
        cols=[]
        for v0 in cols0:
            v,_pc=_v10a3_subtract_retained_P_physical(v0,rk,Esg,pcat,haar)
            p_removed += sum(abs(x)>V10A3_COEFF_TOL for _,x in _pc)
            v,ov,qg=_v10a3_subtract_q1_physical(v,rk,Esg,model,haar,q1cache)
            q1_removed += sum(abs(x)>V10A3_COEFF_TOL for x in ov)
            q1ranks.append(qg['rank'])
            cols.append(v)
        G=np.zeros((3,3),dtype=np.float64)
        for i in range(3):
            for j in range(i,3): G[i,j]=G[j,i]=_v10a3_vec_inner(cols[i],cols[j],haar)
        G=0.5*(G+G.T); ev,U=np.linalg.eigh(G)
        min_eval=min(min_eval,float(ev[0]))
        scale=max(1.0,float(ev[-1]))
        for it,fac in enumerate((0.1,1.0,10.0)): rank_tol[it]+=int(np.count_nonzero(ev>(fac*V10A3_GRAM_TOL*scale)))
        keep=ev>V10A3_GRAM_TOL*scale
        r=int(np.count_nonzero(keep)); raw_cols+=sum(bool(v) for v in cols)
        if not r: continue
        if Esg==Fraction(8,3):
            raise RuntimeError(f"physical Q2 retained an E0=8/3 block with rank {r}")
        min_gap=min(min_gap,abs(float(Esg)-E0_PLAQ)); total_rank+=r
        X=U[:,keep]/np.sqrt(ev[keep])[None,:]
        basis=[]
        for j in range(r):
            d=defaultdict(float)
            for a in range(3): _v10a3_add_vec(d,cols[a],X[a,j])
            qv=_v10a3_prune(d); basis.append(qv)
            max_orth=max(max_orth,abs(_v10a3_vec_norm(qv,haar)-1.0))
        # direct fourth-order sector on the three anchored sources
        q2_blocks.append({'key':key,'energy':float(Esg),'rank':r,'gram':G,'basis':basis,
                          'evals':ev[keep].copy()})
    return {'blocks':q2_blocks,'rank':total_rank,'raw_nonzero_columns':raw_cols,
            'min_gram_eig':min_eval,'min_energy_gap':min_gap if min_gap<float('inf') else 0.0,
            'orth_error':max_orth,'p_overlaps_removed':p_removed,'q1_overlaps_removed':q1_removed,
            'q1_group_rank_max':max(q1ranks,default=0),'rank_tol_0p1_1_10':tuple(rank_tol)}


def _v10a3_boundary_symbol(k):
    """3x3 Fourier symbol of B2 in T1_POLS order; right kernel is the flat line."""
    k=np.asarray(k,dtype=float); Nmat=np.zeros((3,3),dtype=np.complex128)
    lid_to_idx={i:x for i,x in enumerate(links)}
    for a,pol in enumerate(T1_POLS):
        f=next(f for f,(v,i,j) in enumerate(faces) if v==(0,0,0) and (i,j)==pol)
        for li in np.flatnonzero(B2[:,f]):
            v,d=lid_to_idx[int(li)]; coeff=float(B2[int(li),f])
            # coordinates are 0/1 for this origin face; periodic representation is exact
            phase=np.exp(-1j*np.dot(k,np.asarray(v,dtype=float)))
            Nmat[int(d),a]+=coeff*phase
    return Nmat


def _v10a3_flat_vector(k):
    Nmat=_v10a3_boundary_symbol(k)
    if np.max(np.abs(Nmat))<1e-13:
        return None
    u,s,vh=np.linalg.svd(Nmat)
    v=vh[-1].conj()
    v=v/np.linalg.norm(v)
    return v


def _v10a3_bloch_from_anchor(Kcols, k):
    """Fourier transform endpoint-face x 3 anchored columns to the 3x3 T1 symbol."""
    H=np.zeros((3,3),dtype=np.complex128); k=np.asarray(k,dtype=float)
    pol_to_i={p:i for i,p in enumerate(T1_POLS)}
    for f,(v,a,b) in enumerate(faces):
        bi=pol_to_i[(a,b)]
        phase=np.exp(-1j*np.dot(k,np.asarray(v,dtype=float)))
        H[bi,:]+=Kcols[f,:]*phase
    return H


def _v10a3_shape_row(k):
    aa=np.asarray([4.0*math.sin(float(x)/2.0)**2 for x in k])
    q=float(np.sum(aa)); e2=float(aa[0]*aa[1]+aa[0]*aa[2]+aa[1]*aa[2]); e3=float(np.prod(aa))
    return np.asarray([q,e2,4.0*e2/q,e3/q],dtype=float)



def _v10a3_translate_state(st, dv):
    """Periodic spatial translation of a trace-network state; color contractions are untouched."""
    dx,dy,dz=(int(dv[0])%L,int(dv[1])%L,int(dv[2])%L)
    occ=[]
    for li,typ in st.occ:
        v,d=links[int(li)]
        vv=((v[0]+dx)%L,(v[1]+dy)%L,(v[2]+dz)%L)
        occ.append((_V10A3_LID[(vv,d)],typ))
    return LXState(tuple(occ),st.part)


_V10A3_LID={(v,d):i for i,(v,d) in enumerate(links)}


def _v10a3_translate_sig(sig,dv):
    dx,dy,dz=(int(dv[0])%L,int(dv[1])%L,int(dv[2])%L)
    out=[]
    for li,p,q in sig:
        v,d=links[int(li)]
        vv=((v[0]+dx)%L,(v[1]+dy)%L,(v[2]+dz)%L)
        out.append((_V10A3_LID[(vv,d)],int(p),int(q)))
    return tuple(sorted(out))


def _v10a3_translate_h0_state(state,dv):
    out={}
    for sig,v in state.items():
        ts=_v10a3_translate_sig(sig,dv)
        d=out.setdefault(ts,defaultdict(float))
        for st,c in v.items():
            d[_v10a3_translate_state(st,dv)] += float(c)
    return _v10a3_compress_state(out)


def _v10a3_h0_state_inner(a,b,haar,bblocks=None):
    """Inner product using exact joint-H0 orthogonality before Haar contraction."""
    A=_v10a3_physical_blocks(a)
    B=bblocks if bblocks is not None else _v10a3_physical_blocks(b)
    ans=0.0; matched=0
    if len(A)>len(B):
        # Keep orientation semantics irrelevant: the physical inner product is symmetric/real here.
        A,B=B,A
    for k,va in A.items():
        vb=B.get(k)
        if vb:
            ans += _v10a3_vec_inner(va,vb,haar); matched += 1
    return float(ans),matched


def _v10a3_endpoint_kernels_bilinear(anchor_w1, anchor_r1, anchor_w2, anchor_r2, haar):
    """Build K2/K4 without W3/W4, exploiting both Hermiticity and exact H0 block orthogonality.

    K2(b,a)=<W b|R W a>,
    K4(b,a)=<W R W b|R W R W a>.
    Every endpoint bra is a translated copy of one of the three anchored T1 states.
    """
    r1blocks=[_v10a3_physical_blocks(x) for x in anchor_r1]
    r2blocks=[_v10a3_physical_blocks(x) for x in anchor_r2]
    pol_index={pol:i for i,pol in enumerate(T1_POLS)}
    K2=np.zeros((P,3),dtype=np.float64); K4=np.zeros((P,3),dtype=np.float64)
    matches2=matches4=0; t0=time.time()
    for f,(v,a,b) in enumerate(faces):
        bi=pol_index[(a,b)]
        tw1=_v10a3_translate_h0_state(anchor_w1[bi],v)
        tw2=_v10a3_translate_h0_state(anchor_w2[bi],v)
        for ai in range(3):
            K2[f,ai],m2=_v10a3_h0_state_inner(tw1,anchor_r1[ai],haar,r1blocks[ai])
            K4[f,ai],m4=_v10a3_h0_state_inner(tw2,anchor_r2[ai],haar,r2blocks[ai])
            matches2+=m2; matches4+=m4
        if V10A3_PROGRESS and P>100 and (f+1)%max(1,P//5)==0:
            print(f"      endpoint bilinear {f+1:,}/{P:,}; H0 matches={matches2:,}/{matches4:,}; elapsed={time.time()-t0:.1f}s")
    return K2,K4,{
        'w1_sig_blocks':tuple(len(x) for x in anchor_w1),'r1_sig_blocks':tuple(len(x) for x in anchor_r1),
        'w2_sig_blocks':tuple(len(x) for x in anchor_w2),'r2_sig_blocks':tuple(len(x) for x in anchor_r2),
        'matched_h0_blocks_K2':matches2,'matched_h0_blocks_K4':matches4,
    }


def _v10a3_extract_shape(K4):
    theta=2.0*math.pi/5.0
    fit_pts=[(theta,0,0),(theta,theta,0),(2*theta,theta,0),(theta,theta,theta)]
    test_pts=[(2*theta,theta,theta),(2*theta,2*theta,theta)]
    HG=_v10a3_bloch_from_anchor(K4,(0,0,0))
    gamma_herm=float(np.max(np.abs(HG-HG.conj().T)))
    gamma_spread=float(np.ptp(np.linalg.eigvalsh(0.5*(HG+HG.conj().T)).real))
    epsG=float(np.trace(HG).real/3.0)
    vals=[]; herm=[]
    for k in fit_pts+test_pts:
        H=_v10a3_bloch_from_anchor(K4,k); herm.append(float(np.max(np.abs(H-H.conj().T))))
        v=_v10a3_flat_vector(k)
        vals.append(float(np.real(np.vdot(v,H@v))))
    M=np.vstack([_v10a3_shape_row(k) for k in fit_pts])
    d=np.asarray(vals[:4])-epsG
    coef=np.linalg.solve(M,d)
    residuals=[]
    for k,obs in zip(test_pts,vals[4:]):
        pred=epsG+float(_v10a3_shape_row(k)@coef)
        residuals.append(obs-pred)
    return {'rest_direct':epsG,'A':coef[0],'B':coef[1],'C_direct':coef[2],'D':coef[3],
            'alpha':4.0*coef[0],'fit_cond':float(np.linalg.cond(M)),
            'fifth_residual_max':float(max(abs(x) for x in residuals)),
            'test_residuals':tuple(float(x) for x in residuals),
            'hermiticity_error':max([gamma_herm]+herm),'gamma_spread':gamma_spread,
            'fit_points':fit_pts,'test_points':test_pts,'fit_values':tuple(vals[:4]),'test_values':tuple(vals[4:])}


def _v10a3_second_order_t3_gate(K2, anchor_faces):
    errs=[]; n=0
    for a,f0 in enumerate(anchor_faces):
        for f in range(P):
            shared=np.flatnonzero((B2[:,f0]!=0)&(B2[:,f]!=0))
            if f==f0 or len(shared)!=1: continue
            l=int(shared[0]); target=float(B2[l,f0]*B2[l,f])*T3_TARGET
            errs.append(abs(float(K2[f,a])-target)); n+=1
    return n,max(errs,default=0.0)



# =============================================================================
# HODGE v10a.4 — COMPRESSED FESHBACH FOUR-MOMENT FOLD CERTIFICATE
# =============================================================================
# PURPOSE
# -------
# Compute the strict O(u^4) scalar Feshbach coefficient without materializing a
# global physical Q2 basis.  For H=H0+uV and R=Q(E0-H0)^-1 Q, define
#
#   w1 = Q V P,      r1 = R w1,
#   w2 = Q V r1,     r2 = R w2,
#   r12 = R r1.
#
# Then, in any scalar irreducible P block (the Gamma T1 triplet and vacuum),
#
#   D = <w2|r2>, C = Re<r1|r2>, N=<r1|r1>, J=<r1|R|r1>,
#
#   e4 = D - 2 e1 C - e2 N + e1^2 J.
#
# This run certifies that identity on the exact SU(3) compact vacuum character
# tower, then evaluates the corresponding connected Gamma-point axial moments.
# It DOES NOT call the axial result m4_rest: marked linked-cluster Mobius
# subtraction against the vacuum sector is deliberately a subsequent layer.
# =============================================================================

from fractions import Fraction as _F10

V10A4_PROGRESS = int(os.environ.get("V10A4_PROGRESS", "1"))
V10A4_VAC_ONLY = os.environ.get("V10A4_VAC_ONLY", "0") == "1"
V10A4_REQUIRE_L5 = os.environ.get("V10A4_REQUIRE_L5", "1") != "0"
V10A4_TOL = float(os.environ.get("V10A4_TOL", "2e-10"))
V10A4_CUBIC_TOL = float(os.environ.get("V10A4_CUBIC_TOL", "2e-8"))
V10A4_GATE_START = len(gates)


def _v10a4_frac(x, maxden=10**9):
    return _F10(float(x)).limit_denominator(int(maxden))


def _v10a4_compact_vacuum_moments(depth=4):
    """Exact character-basis Feshbach moments for the one-plaquette SU(3) vacuum."""
    reps,H0,M=vacuum_character_ops(int(depth))
    if reps[0] != (0,0):
        raise RuntimeError('vacuum character ordering changed')
    V=-np.asarray(M,dtype=np.float64)
    h=np.diag(np.asarray(H0,dtype=np.float64))
    E0=float(h[0])
    B=V[1:,0].copy()
    den=E0-h[1:]
    if np.min(np.abs(den)) < 1e-14:
        raise RuntimeError('compact vacuum Q denominator hit zero')
    R=np.diag(1.0/den)
    W=V[1:,1:]
    e1=float(V[0,0])
    r1=R@B
    w2=W@r1
    r2=R@w2
    r12=R@r1
    e2=float(B@r1)
    sigma3=float(r1@w2)
    N=float(r1@r1)
    C=float(np.real(r1@r2))
    J=float(r1@r12)
    D=float(w2@r2)
    e3=float(sigma3-e1*N)
    e4=float(D-2.0*e1*C-e2*N+e1*e1*J)
    return dict(depth=int(depth),dim=len(reps),e1=e1,e2=e2,sigma3=sigma3,e3=e3,
                D=D,C=C,N=N,J=J,e4=e4)


def _v10a4_fs_model():
    """Only the oriented plaquette-step cache required by the local W recursion."""
    lid={(v,d):i for i,(v,d) in enumerate(links)}
    cache={}
    def fs(face,orient):
        key=(int(face),int(orient))
        if key not in cache:
            cache[key]=tuple(face_steps_generic(int(face),int(orient),faces,lid,shift))
        return cache[key]
    return {'v9_fs_cached':fs}


def _v10a4_gamma_inner(left,right,haar,label=''):
    """Gamma-point bilinear sum using H0-block translation prefiltering.

    If |L_Gamma> and |R_Gamma> are volume-normalized translation sums, translation
    invariance reduces their inner product to sum_d <L_d|R_0>.  We scan only H0
    blocks whose translated joint-representation signature exists on the right;
    trace networks are translated only after this exact orthogonality prefilter.
    """
    LB=_v10a3_physical_blocks(left)
    RB=_v10a3_physical_blocks(right)
    ans=0.0; sig_tests=0; matched=0; haar_terms=0
    t0=time.time()
    items=list(LB.items())
    for ii,((cs,Esg),lv) in enumerate(items):
        for dv in verts:
            sig_tests += 1
            tcs=_v10a2_sig_canon(_v10a3_translate_sig(cs,dv))
            rv=RB.get((tcs,Esg))
            if rv is None:
                continue
            matched += 1
            tv={_v10a3_translate_state(st,dv):float(c) for st,c in lv.items()}
            ans += _v10a3_vec_inner(tv,rv,haar)
            haar_terms += len(tv)*len(rv)
        if V10A4_PROGRESS and len(items)>1000 and (ii+1)%max(1,len(items)//4)==0:
            print(f"      {label} blocks {ii+1:,}/{len(items):,}; H0 matches={matched:,}; elapsed={time.time()-t0:.1f}s")
    return float(ans),dict(left_blocks=len(LB),right_blocks=len(RB),signature_tests=sig_tests,
                           matched_h0_blocks=matched,raw_pair_upper_bound=haar_terms)


def _v10a4_diag_moment(lefts,rights,haar,name):
    vals=[]; stats=[]
    for a in range(3):
        x,st=_v10a4_gamma_inner(lefts[a],rights[a],haar,f'{name} pol{a}')
        vals.append(float(x)); stats.append(st)
        print(f"    {name}[{a}]={x:+.15g}  matches={st['matched_h0_blocks']:,}")
    spread=float(np.ptp(vals))
    return float(np.mean(vals)),spread,tuple(vals),stats


def _v10a4_first_order_local(s0s,w1s,haar):
    vals=[]
    for a in range(3):
        x,_=_v10a3_h0_state_inner(s0s[a],w1s[a],haar)
        vals.append(float(x))
    return float(np.mean(vals)),float(np.ptp(vals)),tuple(vals)


def _v10a4_t3_spot(anchor_faces,w1s,r1s,haar):
    """36 known shared-edge second-order hopping firewalls, without all-zone K2."""
    errs=[]; rows=[]
    rblocks=[_v10a3_physical_blocks(x) for x in r1s]
    for a,f0 in enumerate(anchor_faces):
        for f,(v,pa,pb) in enumerate(faces):
            if f==f0: continue
            shared=np.flatnonzero((B2[:,f0]!=0)&(B2[:,f]!=0))
            if len(shared)!=1: continue
            bi=T1_POLS.index((pa,pb))
            tw=_v10a3_translate_h0_state(w1s[bi],v)
            got,_=_v10a3_h0_state_inner(tw,r1s[a],haar,rblocks[a])
            l=int(shared[0]); target=float(B2[l,f0]*B2[l,f])*T3_TARGET
            errs.append(abs(got-target)); rows.append((a,f,got,target))
    return len(rows),max(errs,default=0.0)





# =============================================================================
# v10a.8 FAST GAMMA BLOCK-ORBIT CONTRACTION
# =============================================================================
# Replaces the raw per-pair Gamma Haar loop used by v10a.7.  The exact H0
# signature/translation prefilter is retained, but every matched pair of block
# vectors is jointly link-canonicalized ONCE.  Haar contractions are then done
# directly in those shared canonical link coordinates via _qcache, avoiding the
# repeated joint-canonicalization inside qhaar for every trace-network pair.
# Translation-equivalent whole block pairs are memoized, so repeated local
# topologies cost one block contraction rather than one contraction per lattice
# placement.

V10A8_HEARTBEAT = float(os.environ.get("V10A8_HEARTBEAT", "20"))
V10A8_BLOCK_CACHE_MAX = int(os.environ.get("V10A8_BLOCK_CACHE_MAX", "250000"))

def _v10a8_mem_gb():
    try:
        import psutil
        return psutil.Process(os.getpid()).memory_info().rss / (1024.0**3)
    except Exception:
        try:
            import resource
            r=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
            # Linux ru_maxrss is KiB.
            return float(r)/(1024.0**2)
        except Exception:
            return float('nan')

def _v10a8_block_key_and_inner(lv, rv, direct_haar, cache):
    """Exact physical inner product of two already H0-compatible blocks.

    All trace networks in both vectors are jointly link-canonicalized once.
    This preserves every relative shared-link topology while making translated
    copies byte-identical.  The resulting whole-block key is memoized.
    """
    if not lv or not rv:
        return 0.0, False, 0
    li=list(lv.items()); ri=list(rv.items())
    states=[st for st,_ in li] + [st for st,_ in ri]
    can=_joint_canon_states(*states)
    nl=len(li)
    lc=can[:nl]; rc=can[nl:]
    # Coefficients are generated by identical algebra under translation, hence
    # float.hex gives a stable exact key for topology-identical block copies.
    lk=tuple((st.occ,st.part,float(c).hex()) for st,(_,c) in zip(lc,li))
    rk=tuple((st.occ,st.part,float(c).hex()) for st,(_,c) in zip(rc,ri))
    # Hermitian symmetry halves cache duplication.
    if rk < lk:
        key=(rk,lk)
        A=[(st,float(c)) for st,(_,c) in zip(rc,ri)]
        B=[(st,float(c)) for st,(_,c) in zip(lc,li)]
    else:
        key=(lk,rk)
        A=[(st,float(c)) for st,(_,c) in zip(lc,li)]
        B=[(st,float(c)) for st,(_,c) in zip(rc,ri)]
    hit=key in cache
    if hit:
        return cache[key], True, 0

    # Center/N-ality prefilter exactly as in _v10a3_vec_inner, but because all
    # states already share one joint canonical link frame, direct_haar can be
    # _qcache: no per-pair joint relabeling remains in the hot loop.
    ga=defaultdict(list); gb=defaultdict(list)
    for st,c in A: ga[_v9_flux_key_state(st)].append((st,c))
    for st,c in B: gb[_v9_flux_key_state(st)].append((st,c))
    ans=0.0; npairs=0
    for fk,la in ga.items():
        lb=gb.get(fk)
        if not lb: continue
        for a,ca in la:
            for b,cb in lb:
                ans += ca*cb*direct_haar(a,b)
                npairs += 1
    ans=float(ans)
    if len(cache) < V10A8_BLOCK_CACHE_MAX:
        cache[key]=ans
    return ans, False, npairs



# =============================================================================
# v10a.10 UNIQUE-BLOCK MULTIPROCESS GAMMA ENGINE
# =============================================================================
# Phase 1 is cheap and deterministic: enumerate exact H0/translation matches,
# jointly canonicalize each WHOLE local block pair, and collapse identical
# translated topologies.  Phase 2 evaluates each unique local Haar block once,
# across CPU workers.  The A100 is not the right processor for these tiny
# irregular tensor networks; using all host cores and eliminating duplicate
# block work is the correct execution model.

V10A10_WORKERS = int(os.environ.get('V10A10_WORKERS', str(max(1,min(8,(os.cpu_count() or 2)-1)))))
V10A10_SCAN_HEARTBEAT = float(os.environ.get('V10A10_SCAN_HEARTBEAT','10'))
_V10A10_TASKS_GLOBAL=[]

def _v10a10_canon_block_pair(lv,rv):
    li=list(lv.items()); ri=list(rv.items())
    states=[st for st,_ in li]+[st for st,_ in ri]
    can=_joint_canon_states(*states); nl=len(li)
    lc=can[:nl]; rc=can[nl:]
    A=tuple((st,float(c)) for st,(_,c) in zip(lc,li))
    B=tuple((st,float(c)) for st,(_,c) in zip(rc,ri))
    ak=tuple((st.occ,st.part,float(c).hex()) for st,c in A)
    bk=tuple((st.occ,st.part,float(c).hex()) for st,c in B)
    if bk < ak:
        A,B=B,A; ak,bk=bk,ak
    return (ak,bk),A,B

def _v10a10_worker(idx):
    # Fork workers inherit the task table and certified Haar tensors without
    # serializing 80k trace-network terms through the multiprocessing queue.
    A,B,mult,cost=_V10A10_TASKS_GLOBAL[int(idx)]
    ga=defaultdict(list); gb=defaultdict(list)
    for st,c in A: ga[_v9_flux_key_state(st)].append((st,c))
    for st,c in B: gb[_v9_flux_key_state(st)].append((st,c))
    ans=0.0; npairs=0; t0=time.time()
    for fk,la in ga.items():
        lb=gb.get(fk)
        if not lb: continue
        for a,ca in la:
            for b,cb in lb:
                # A and B already share one canonical link frame, so bypass the
                # per-pair _joint_canon_states call in qhaar.
                ans += ca*cb*_qcache(a,b)
                npairs += 1
    return int(idx),float(ans),int(npairs),float(time.time()-t0)


def _v10a11_oneface_axial_character():
    """Exact C- one-plaquette character moments through the direct fourth order.

    This replaces the 54 (1-face,1-face) raw Haar block contractions, whose
    largest expanded partition block is 432x432.  It is the same physical
    one-face sector in the Haar-orthonormal SU(3) character basis.
    """
    # C- irreps reachable within two magnetic steps from 3-3bar:
    # (3-3b), (6-6b), (10-10b), ((2,1)-(1,2)).
    odd=((1,0),(2,0),(3,0),(2,1))
    # Build M in the normalized odd character basis by fusion, not by targets.
    # For each representative R, act with chi_3+chi_3bar on R-Rbar and collect
    # its coefficient on S-Sbar.
    M=np.zeros((4,4),dtype=np.float64)
    def conj(r): return (r[1],r[0])
    def fusions(r): return tuple(su3_fuse_fundamental(r))+tuple(su3_fuse_antifundamental(r))
    for j,r in enumerate(odd):
        coeff=Counter(fusions(r)); coeffb=Counter(fusions(conj(r)))
        for i,sr in enumerate(odd):
            # normalized odd states give the coefficient of chi_sr in
            # M(chi_r-chi_rbar); conjugation symmetry guarantees antisym pair.
            M[i,j]=float(coeff[sr]-coeffb[sr])
    H0=np.diag([2.0*su3_c2_pq(*r) for r in odd])
    V=-M; E0=H0[0,0]
    B=V[1:,0].copy(); W=V[1:,1:].copy(); den=E0-np.diag(H0)[1:]
    R=np.diag(1.0/den)
    r1=R@B; w2=W@r1; r2=R@w2; r12=R@r1
    return dict(e1=float(V[0,0]),e2=float(B@r1),sigma3=float(r1@w2),
                N=float(r1@r1),C=float(r1@r2),J=float(r1@r12),D=float(w2@r2))


# =============================================================================
# v10a.13 FACTORIZED SU(3) HAAR PROJECTORS
# =============================================================================
# The dense cold tensors remain the reference contractor.  Production Gamma
# pairs with expensive k=3/pure-six patterns use the mathematically identical
# low-rank projector factorizations below.  This removes the pathological
# 3^12 dense intermediates that stalled v10a.7-v10a.12.

def _v10a13_factor_data():
    if hasattr(_v10a13_factor_data,'data'):
        return _v10a13_factor_data.data
    data={}
    for k in (1,2,3):
        ps,W=lx_wg_fixed(k)
        D=np.zeros((len(ps),)+(3,)*(2*k),dtype=np.float64)
        for si,sig in enumerate(ps):
            for u in np.ndindex((3,)*k):
                bb=[0]*k
                for r in range(k): bb[sig[r]]=u[r]
                D[(si,)+u+tuple(bb)]=1.0
        data[('bal',k)]=(D,np.asarray([[float(x) for x in row] for row in W],dtype=np.float64))
    # Pure-six rank-five epsilon-pair factorization.
    EPS=_FAST_EPS
    parts=[]
    for comb in itertools.combinations(range(1,6),2):
        A=(0,)+comb; B=tuple(i for i in range(6) if i not in A); parts.append((A,B))
    inv=[]
    for A,B in parts:
        arr=np.zeros((3,)*6,dtype=np.float64)
        for idx in np.ndindex((3,)*6):
            arr[idx]=EPS[tuple(idx[i] for i in A)]*EPS[tuple(idx[i] for i in B)]
        inv.append(arr)
    G=np.array([[np.tensordot(x,y,axes=6) for y in inv] for x in inv],dtype=np.float64)
    _,_,piv=qr(G,pivoting=True)
    rank=int(np.linalg.matrix_rank(G,tol=1e-10))
    if rank!=5: raise RuntimeError(f'v10a.13 pure-six factor rank={rank}, expected 5')
    keep=list(map(int,piv[:rank]))
    data['six']=(np.stack([inv[i] for i in keep],axis=0),np.linalg.inv(G[np.ix_(keep,keep)]))
    _v10a13_factor_data.data=data
    return data

@lru_cache(maxsize=500000)
def _v10a13_haar_factor(a,b):
    """Haar inner product using low-rank row/column projector factors.

    Supported production patterns are exactly those surviving the v10a.12
    H0/center scan: (1,1),(2,2),(3,3),(3,0),(0,3),(6,0),(0,6).
    """
    occ,part=lx_combine_bra_ket(a,b)
    by=defaultdict(lambda:{True:[],False:[]})
    for i,(l,t) in enumerate(occ): by[int(l)][bool(t)].append(i)
    data=_v10a13_factor_data(); args=[]; pref=1.0
    aux=(max(part)+1) if part else 0
    for g in by.values():
        U,B=g[True],g[False]; pat=(len(U),len(B))
        if (pat[0]-pat[1])%3: return 0.0
        if pat in ((1,1),(2,2),(3,3)):
            k=len(U); D,W=data[('bal',k)]; ar=aux; ac=aux+1; aux+=2
            row=[int(part[2*p]) for p in U+B]
            col=[int(part[2*p+1]) for p in U+B]
            args.extend((D,[ar]+row,W,[ar,ac],D,[ac]+col))
        elif pat in ((3,0),(0,3)):
            items=U if len(U)==3 else B
            row=[int(part[2*p]) for p in items]
            col=[int(part[2*p+1]) for p in items]
            args.extend((_FAST_EPS,row,_FAST_EPS,col)); pref/=6.0
        elif pat in ((6,0),(0,6)):
            items=U if len(U)==6 else B
            I,C=data['six']; ar=aux; ac=aux+1; aux+=2
            row=[int(part[2*p]) for p in items]
            col=[int(part[2*p+1]) for p in items]
            args.extend((I,[ar]+row,C,[ar,ac],I,[ac]+col))
        else:
            # This should never fire after the production pair census.  Keep
            # the dense certified contractor as a safe explicit fallback.
            return float(_qcache(a,b))
    if not args: return float(N**len(set(part)))
    return float(pref*oe.contract(*args,[],optimize='greedy',memory_limit='max_input'))

def _v10a13_pair_score(a,b):
    # Cheap proxy for dense-projector cost.  Thresholded only for selecting the
    # faster equivalent representation; it never changes the mathematics.
    occ,_=lx_combine_bra_ket(a,b); by=defaultdict(lambda:[0,0])
    for _i,(_l,_t) in enumerate(occ): by[int(_l)][0 if _t else 1]+=1
    cm={(1,1):1,(2,2):4,(3,3):36,(3,0):6,(0,3):6,
        (4,1):96,(1,4):96,(6,0):900,(0,6):900}
    score=1
    for counts in by.values(): score*=cm.get(tuple(counts),1000)
    return int(score)
def _v10a10_gamma_support_inner(left_labeled,right_labeled,label=''):
    """v10a.12 exact Gamma inner product with PAIR-TOPOLOGY collapse.

    This is the replacement for the stalled v10a.7/v10a.10 hot loop.

    Phase 1: exact H0/signature/translation scan and whole-block orbit collapse.
    Phase 2: expand compatible center-flux pairs but canonicalize each individual
             Haar pair and sum its TOTAL coefficient before any tensor contraction.
    Phase 3: evaluate each unique canonical Haar topology exactly once with the
             certified extended Haar contractor, using shared-cache host threads.

    The one-face/one-face contribution is evaluated analytically in the exact
    C- SU(3) character basis, avoiding the worst 432x432 raw blocks entirely.
    """
    from concurrent.futures import ThreadPoolExecutor, as_completed

    threads=int(os.environ.get('V10A12_THREADS',str(max(1,min(8,os.cpu_count() or 1)))))
    batch=max(16,int(os.environ.get('V10A12_BATCH','512')))
    heartbeat=float(os.environ.get('V10A12_HEARTBEAT','15'))
    pair_tol=float(os.environ.get('V10A12_PAIR_TOL','2e-14'))

    RB=_v17_phys_index(right_labeled)
    Litems=[]
    for SL,st in left_labeled.items():
        for key,lv in _v10a3_physical_blocks(st).items():
            Litems.append((SL,key,lv))
    Litems.sort(key=lambda z:len(z[2]))

    # ------------------------------------------------------------------
    # PHASE 1 — cheap exact block/translation scan.
    # ------------------------------------------------------------------
    tasks={}; sig_tests=matches=raw_pair_upper=0; skipped11=0
    t0=time.time(); last=t0
    for ii,(SL,(cs,Esg),lv) in enumerate(Litems):
        for dv in verts:
            sig_tests += 1
            tcs=_v10a2_sig_canon(_v10a3_translate_sig(cs,dv))
            candidates=RB.get((tcs,Esg),())
            if not candidates: continue
            tv={_v10a3_translate_state(st,dv):float(c) for st,c in lv.items()}
            for SR,rv in candidates:
                matches += 1
                raw_pair_upper += len(tv)*len(rv)
                if len(SL)==1 and len(SR)==1:
                    skipped11 += 1
                    continue
                key,A,B=_v10a10_canon_block_pair(tv,rv)
                rec=tasks.get(key)
                if rec is None:
                    tasks[key]=[1,A,B,len(A)*len(B)]
                else:
                    rec[0]+=1
        now=time.time()
        if V10A7_PROGRESS and (now-last>=heartbeat or ii+1==len(Litems)):
            rate=(ii+1)/max(now-t0,1e-9)
            eta=(len(Litems)-ii-1)/rate if rate else 0.0
            print(f'      {label} scan {ii+1:,}/{len(Litems):,}; matches={matches:,}; '
                  f'unique-blocks={len(tasks):,}; raw-pairs<={raw_pair_upper:,}; '
                  f'RAM={_v10a8_mem_gb():.2f} GiB; elapsed={now-t0:.1f}s ETA~{eta:.1f}s',flush=True)
            last=now

    # Exact one-face C- character block, which replaces the largest raw blocks.
    _one=_v10a11_oneface_axial_character()
    d11=float(_one['D'])
    print(f'      {label} analytic one-face block: skipped matches={skipped11}; '
          f'D11={d11:+.15g} ~ {_v17_rational(d11)}',flush=True)
    gate('v10a.12 one-face axial e1=1',abs(_one['e1']-1.0)<V10A7_TOL,_one['e1'])
    gate('v10a.12 one-face axial e2=-1/4',abs(_one['e2']+0.25)<V10A7_TOL,_one['e2'])
    gate('v10a.12 one-face axial sigma3=C=0',
         abs(_one['sigma3'])<V10A7_TOL and abs(_one['C'])<V10A7_TOL,
         f"sigma3={_one['sigma3']}, C={_one['C']}")
    gate('v10a.12 one-face axial D=-13/896',abs(d11+13/896)<V10A7_TOL,d11)

    taskrecs=[(A,B,int(mult),int(cost)) for mult,A,B,cost in tasks.values()]
    whole_cost=sum(x[3] for x in taskrecs)
    maxcost=max([x[3] for x in taskrecs] or [0])
    print(f'      {label} block plan: unique-blocks={len(taskrecs):,}; '
          f'pair-upper(after one-face analytic)={whole_cost:,}; max-block={maxcost:,}',flush=True)

    # ------------------------------------------------------------------
    # PHASE 2 — collapse ALL individual canonical Haar pair topologies.
    # No Haar tensor contraction is performed here.
    # ------------------------------------------------------------------
    pairw=defaultdict(float); pair_occ=0
    tp=time.time(); last=tp
    for ti,(A,B,mult,cost) in enumerate(taskrecs):
        ga=defaultdict(list); gb=defaultdict(list)
        for st,c in A: ga[_v9_flux_key_state(st)].append((st,c))
        for st,c in B: gb[_v9_flux_key_state(st)].append((st,c))
        for fk,la in ga.items():
            lb=gb.get(fk)
            if not lb: continue
            for aa,ca in la:
                for bb,cb in lb:
                    # Joint canonicalization preserves the full relative link
                    # topology while collapsing every translated copy.
                    x,y=_joint_canon_states(aa,bb)
                    kx=(x.occ,x.part); ky=(y.occ,y.part)
                    if ky<kx: x,y=y,x
                    pairw[(x,y)] += float(mult)*float(ca)*float(cb)
                    pair_occ += 1
        now=time.time()
        if V10A7_PROGRESS and (now-last>=heartbeat or ti+1==len(taskrecs)):
            rate=(ti+1)/max(now-tp,1e-9)
            eta=(len(taskrecs)-ti-1)/rate if rate else 0.0
            print(f'      {label} collapse {ti+1:,}/{len(taskrecs):,}; '
                  f'pair-occ={pair_occ:,}; unique={len(pairw):,}; '
                  f'RAM={_v10a8_mem_gb():.2f} GiB; elapsed={now-tp:.1f}s ETA~{eta:.1f}s',flush=True)
            last=now

    pairw={k:w for k,w in pairw.items() if abs(w)>pair_tol}
    collapse_seconds=time.time()-tp
    compression=(pair_occ/max(len(pairw),1))
    print(f'      {label} PAIR-TOPOLOGY COLLAPSE: occurrences={pair_occ:,} -> '
          f'unique_nonzero={len(pairw):,} ({compression:.2f}x); '
          f'elapsed={collapse_seconds:.1f}s; RAM={_v10a8_mem_gb():.2f} GiB',flush=True)
    gate('v10a.12 pair-topology collapse is nonempty',len(pairw)>0,len(pairw))
    gate('v10a.12 pair-topology collapse reduces work',len(pairw)<pair_occ,
         f'{pair_occ:,}->{len(pairw):,}')

    # Cost proxy is used only to choose between two exactly equivalent Haar
    # representations.
    def _pair_complexity(item):
        (a,b),w=item
        return _v10a13_pair_score(a,b)

    items=list(pairw.items())
    items.sort(key=_pair_complexity,reverse=True)
    maxscore=_pair_complexity(items[0]) if items else 0
    print(f'      {label} Haar plan: unique={len(items):,}; execution=single-process-factorized; '
          f'batch={batch}; max-complexity-score={maxscore:,}',flush=True)

    # ------------------------------------------------------------------
    # PHASE 3 — one exact Haar evaluation per unique canonical topology.
    # Threads share the certified tensor cache; no giant objects are serialized.
    # ------------------------------------------------------------------
    # Cold equivalence gate: one representative of every endpoint-pattern
    # signature must match the original dense certified contractor before the
    # production sum starts.
    reps={}
    for (a,b),w in items:
        pats=tuple(sorted(_v10_endpoint_patterns(a,b)))
        reps.setdefault(pats,(a,b))
    ferr=[]
    print(f'      {label} factorized-Haar cold gate on {len(reps)} endpoint signatures',flush=True)
    for pats,(a,b) in reps.items():
        dense=float(_qcache(a,b)); fact=float(_v10a13_haar_factor(a,b))
        ferr.append(abs(dense-fact))
    gate('v10a.16 factorized Haar matches dense contractor on every production endpoint signature',
         max(ferr,default=0.0)<5e-12,f'maxerr={max(ferr,default=0.0):.3e}, signatures={len(reps)}')

    # Hybrid exact contractor.  Dense is faster for the small k<=2 networks;
    # factorized is dramatically faster for k=3/pure-six determinant networks.
    factor_threshold=int(os.environ.get('V10A16_FACTOR_THRESHOLD','0'))
    nfactor=sum(_pair_complexity(x)>=factor_threshold for x in items)
    print(f'      {label} production Haar: dense={len(items)-nfactor:,}; factorized={nfactor:,}; '
          f'threshold={factor_threshold:,}',flush=True)

    def _eval_item(kv):
        (a,b),w=kv
        if _v10a13_pair_score(a,b)>=factor_threshold:
            return float(w)*float(_v10a13_haar_factor.__wrapped__(a,b)),1
        return float(w)*float(_qcache(a,b)),0

    # Sequential execution is intentional.  The former thread/process versions
    # could block on one pathological dense contraction and made progress look
    # dead.  After factorization every individual topology is small; a heartbeat
    # is therefore guaranteed between short batches with no fork/CUDA hazards.
    ans=d11; done=0; nf_done=0; te=time.time(); last=te
    for kv in items:
        z,isf=_eval_item(kv); ans += z; nf_done += isf; done += 1
        now=time.time()
        if V10A7_PROGRESS and (now-last>=heartbeat or done%1000==0 or done==len(items)):
            rate=done/max(now-te,1e-9); eta=(len(items)-done)/rate if rate else 0.0
            ci=_qcache.cache_info() if hasattr(_qcache,'cache_info') else None
            fi='BYPASSED'
            print(f'      {label} Haar {done:,}/{len(items):,}; factorized={nf_done:,}; '
                  f'rate={rate:,.1f}/s; elapsed={now-te:.1f}s ETA~{eta:.1f}s; '
                  f'dense-cache={ci}; factor-cache={fi}; RAM={_v10a8_mem_gb():.2f} GiB',flush=True)
            last=now

    exec_seconds=time.time()-te
    print(f'      {label} COMPLETE D={ans:+.15g}; unique Haar={done:,}; '
          f'Haar time={exec_seconds:.1f}s; total={time.time()-t0:.1f}s',flush=True)
    return float(ans),dict(
        left_blocks=len(Litems),signature_tests=sig_tests,matched_h0_blocks=matches,
        raw_pair_upper_bound=raw_pair_upper,unique_block_pairs=len(taskrecs),
        pair_occurrences=pair_occ,unique_haar_pairs=len(items),
        pair_compression=compression,threads=1,scan_seconds=tp-t0,
        collapse_seconds=collapse_seconds,execute_seconds=exec_seconds,
        analytic_oneface_D=d11,analytic_oneface_matches=skipped11)


# =============================================================================
# v10a.17 FULL-T1 TRANSLATION-RESOLVED PAIR-COLLAPSED ENDPOINT KERNEL
# =============================================================================
# v10a.16 solved the scalar Gamma bottleneck by collapsing 1.8M center-compatible
# pair occurrences to ~1.2e5 canonical Haar topologies.  v10a.17 retains the
# lattice displacement attached to each occurrence, so the SAME collapsed Haar
# evaluation reconstructs the complete real-space 3x3 T1 fourth-order kernel.
#
# This is the direct operator needed to cold-extract the protected A/B/D/alpha
# coefficients and the previously unprotected C_direct from the same W2/R2
# corpus that produced D_A.  No historical fourth-order scalar or C target is
# loaded.

_V10A17_FACTOR_HAAR_CALLS = 0

def _v10a17_factor_haar_cached(a,b):
    """Use the shared factorized-Haar LRU across all 9 T1 endpoint columns."""
    global _V10A17_FACTOR_HAAR_CALLS
    _V10A17_FACTOR_HAAR_CALLS += 1
    return float(_v10a13_haar_factor(a,b))


def _v10a17_endpoint_vector(left_labeled, right_labeled, left_root, right_root, label=''):
    """Return the full translation-resolved bilinear vector.

    For every lattice translation dv of the left anchored half-history this
    computes

        < T_dv left | right >

    after exact H0/signature filtering, whole-block orbit collapse, individual
    Haar-pair topology collapse, and factorized SU(3) Haar contraction.

    The returned dictionary is keyed by dv in the cubic translation group.
    Haar values are cached globally across all polarization pairs, so the first
    column pays most of the tensor cost and the remaining 8 columns largely
    reuse the same canonical local topologies.
    """
    heartbeat=float(os.environ.get('V10A17_HEARTBEAT','15'))
    pair_tol=float(os.environ.get('V10A17_PAIR_TOL','2e-14'))

    RB=_v17_phys_index(right_labeled)
    Litems=[]
    for SL,st in left_labeled.items():
        for key,lv in _v10a3_physical_blocks(st).items():
            Litems.append((SL,key,lv))
    Litems.sort(key=lambda z:len(z[2]))

    # PHASE 1: H0/signature/translation scan, retaining displacement multiplicity.
    tasks={}
    matches=raw_pair_upper=skipped11=0
    skipped_dv=Counter()

    # v10a.24b correctness hotfix:
    # The analytic D11=-13/896 replacement is a SAME-POLARIZATION local
    # one-face result.  Cross-polarization 1x1 H0-signature matches are legal
    # and must fall through to the ordinary canonical-pair/Haar contractor.
    left_pol=tuple(faces[int(left_root)][1:])
    right_pol=tuple(faces[int(right_root)][1:])
    same_pol=(left_pol==right_pol)
    cross11_fallback=0
    cross11_dv=Counter()

    t0=time.time(); last=t0
    for ii,(SL,(cs,Esg),lv) in enumerate(Litems):
        for dv in verts:
            tcs=_v10a2_sig_canon(_v10a3_translate_sig(cs,dv))
            candidates=RB.get((tcs,Esg),())
            if not candidates:
                continue
            tv={_v10a3_translate_state(st,dv):float(c) for st,c in lv.items()}
            for SR,rv in candidates:
                matches += 1
                raw_pair_upper += len(tv)*len(rv)
                if len(SL)==1 and len(SR)==1:
                    if same_pol:
                        skipped11 += 1
                        skipped_dv[tuple(dv)] += 1
                        continue
                    # Cross-polarization 1x1 matches are NOT represented by the
                    # analytic same-polarization D11 block.  Keep them in the
                    # ordinary exact topology collapse / Haar path.
                    cross11_fallback += 1
                    cross11_dv[tuple(dv)] += 1
                key,A,B=_v10a10_canon_block_pair(tv,rv)
                rec=tasks.get(key)
                if rec is None:
                    rec=[A,B,Counter(),len(A)*len(B)]
                    tasks[key]=rec
                rec[2][tuple(dv)] += 1
        now=time.time()
        if V10A7_PROGRESS and (now-last>=heartbeat or ii+1==len(Litems)):
            rate=(ii+1)/max(now-t0,1e-9)
            eta=(len(Litems)-ii-1)/rate if rate else 0.0
            print(f'      {label} scan {ii+1:,}/{len(Litems):,}; matches={matches:,}; '
                  f'unique-blocks={len(tasks):,}; raw-pairs<={raw_pair_upper:,}; '
                  f'RAM={_v10a8_mem_gb():.2f} GiB; elapsed={now-t0:.1f}s ETA~{eta:.1f}s',flush=True)
            last=now

    out=defaultdict(float)

    # Firewall the shortcut itself.  For cross-polarization endpoint pairs the
    # skipped counter MUST remain zero; any 1x1 matches must have gone through
    # the general contractor above.
    gate(f'{label} analytic one-face shortcut confined to same polarization',
         same_pol or skipped11==0,
         f'left_pol={left_pol}, right_pol={right_pol}, '
         f'analytic_skips={skipped11}, crosspol_fallback={cross11_fallback}')

    if not same_pol and cross11_fallback:
        print(f'      {label} cross-polarization 1x1 fallback: '
              f'matches={cross11_fallback}; displacements={dict(cross11_dv)}',
              flush=True)

    # The analytically solved one-face C- block is strictly local and is used
    # ONLY for same-polarization endpoint pairs.  Center flux then forces the
    # translated bra plaquette to coincide with the ket plaquette.
    if skipped11:
        if not same_pol:
            raise RuntimeError(
                f'{label}: INTERNAL ERROR — cross-polarization one-face match '
                f'was incorrectly routed to analytic D11'
            )
        lp=faces[int(left_root)]
        rp=faces[int(right_root)]
        dv0=tuple((int(rp[0][i])-int(lp[0][i]))%L for i in range(3))
        if set(skipped_dv)-{dv0}:
            raise RuntimeError(f'{label}: one-face matches escaped the local displacement: {dict(skipped_dv)}')
        d11=float(_v10a11_oneface_axial_character()['D'])
        out[dv0] += d11
        gate(f'{label} one-face direct block=-13/896',
             abs(d11+13/896)<V10A7_TOL,d11)

    # PHASE 2: collapse individual canonical Haar pair topologies while keeping a
    # sparse displacement-weight ledger for each topology.
    pairw={}
    pair_occ=0
    tp=time.time(); last=tp
    taskrecs=list(tasks.values())
    for ti,(A,B,dv_mult,cost) in enumerate(taskrecs):
        ga=defaultdict(list); gb=defaultdict(list)
        for st,c in A: ga[_v9_flux_key_state(st)].append((st,c))
        for st,c in B: gb[_v9_flux_key_state(st)].append((st,c))
        for fk,la in ga.items():
            lb=gb.get(fk)
            if not lb:
                continue
            for aa,ca in la:
                for bb,cb in lb:
                    x,y=_joint_canon_states(aa,bb)
                    kx=(x.occ,x.part); ky=(y.occ,y.part)
                    if ky<kx:
                        x,y=y,x
                    pk=(x,y)
                    dw=pairw.get(pk)
                    if dw is None:
                        dw=defaultdict(float)
                        pairw[pk]=dw
                    base=float(ca)*float(cb)
                    for dv,mult in dv_mult.items():
                        dw[dv] += base*float(mult)
                    pair_occ += sum(dv_mult.values())
        now=time.time()
        if V10A7_PROGRESS and (now-last>=heartbeat or ti+1==len(taskrecs)):
            rate=(ti+1)/max(now-tp,1e-9)
            eta=(len(taskrecs)-ti-1)/rate if rate else 0.0
            print(f'      {label} collapse {ti+1:,}/{len(taskrecs):,}; '
                  f'pair-occ={pair_occ:,}; unique={len(pairw):,}; '
                  f'RAM={_v10a8_mem_gb():.2f} GiB; elapsed={now-tp:.1f}s ETA~{eta:.1f}s',flush=True)
            last=now

    # Drop topology/displacement weights that cancel before Haar.
    compact={}
    sparse_weights=0
    for k,d in pairw.items():
        z={dv:w for dv,w in d.items() if abs(w)>pair_tol}
        if z:
            compact[k]=z
            sparse_weights += len(z)
    pairw=compact
    print(f'      {label} PAIR-TOPOLOGY COLLAPSE: occurrences={pair_occ:,} -> '
          f'unique_nonzero={len(pairw):,}; sparse displacement weights={sparse_weights:,}; '
          f'RAM={_v10a8_mem_gb():.2f} GiB',flush=True)

    # Cold dense/factorized equivalence on every endpoint-pattern signature.
    reps={}
    for (a,b) in pairw:
        pats=tuple(sorted(_v10_endpoint_patterns(a,b)))
        reps.setdefault(pats,(a,b))
    ferr=[]
    for _pats,(a,b) in reps.items():
        dense=float(_qcache(a,b))
        fact=float(_v10a13_haar_factor(a,b))
        ferr.append(abs(dense-fact))
    gate(f'{label} factorized Haar matches dense endpoint signatures',
         max(ferr,default=0.0)<5e-12,
         f'maxerr={max(ferr,default=0.0):.3e}, signatures={len(reps)}')

    # PHASE 3: one Haar value per canonical topology; LRU is intentionally kept
    # live across polarization pairs.
    items=list(pairw.items())
    items.sort(key=lambda kv:_v10a13_pair_score(kv[0][0],kv[0][1]),reverse=True)
    te=time.time(); last=te
    c0=_v10a13_haar_factor.cache_info()
    for ii,((a,b),weights) in enumerate(items,1):
        h=_v10a17_factor_haar_cached(a,b)
        if h:
            for dv,w in weights.items():
                out[dv] += h*w
        now=time.time()
        if V10A7_PROGRESS and (now-last>=heartbeat or ii%2000==0 or ii==len(items)):
            ci=_v10a13_haar_factor.cache_info()
            rate=ii/max(now-te,1e-9); eta=(len(items)-ii)/rate if rate else 0.0
            print(f'      {label} Haar {ii:,}/{len(items):,}; '
                  f'cache hits/misses={ci.hits:,}/{ci.misses:,}; '
                  f'elapsed={now-te:.1f}s ETA~{eta:.1f}s; RAM={_v10a8_mem_gb():.2f} GiB',flush=True)
            last=now
    c1=_v10a13_haar_factor.cache_info()

    out={dv:float(x) for dv,x in out.items() if abs(x)>2e-13}
    total=float(sum(out.values()))
    print(f'      {label} COMPLETE gamma-sum={total:+.15g}; nonzero translations={len(out)}; '
          f'new Haar misses={c1.misses-c0.misses:,}; reused hits={c1.hits-c0.hits:,}; '
          f'total={time.time()-t0:.1f}s',flush=True)
    return out,dict(
        left_blocks=len(Litems),matched_blocks=matches,raw_pair_upper=raw_pair_upper,
        unique_block_pairs=len(tasks),pair_occurrences=pair_occ,
        unique_haar_pairs=len(pairw),sparse_displacement_weights=sparse_weights,
        oneface_matches=skipped11,
        crosspol_oneface_fallback_matches=cross11_fallback,
        crosspol_oneface_fallback_displacements=dict(cross11_dv),
        haar_new_misses=c1.misses-c0.misses,
        haar_reused_hits=c1.hits-c0.hits,
        total_seconds=time.time()-t0
    )


def _v10a17_build_K2(anchor_w1,anchor_r1):
    """Small exact-H0 second-order endpoint kernel; no fourth-order work here."""
    r1blocks=[_v10a3_physical_blocks(x) for x in anchor_r1]
    pol_index={pol:i for i,pol in enumerate(T1_POLS)}
    K2=np.zeros((P,3),dtype=np.float64)
    t0=time.time(); matches=0
    for f,(v,a,b) in enumerate(faces):
        bi=pol_index[(a,b)]
        tw1=_v10a3_translate_h0_state(anchor_w1[bi],v)
        for ai in range(3):
            K2[f,ai],m=_v10a3_h0_state_inner(tw1,anchor_r1[ai],qhaar,r1blocks[ai])
            matches += m
        if V10A7_PROGRESS and (f+1)%max(1,P//5)==0:
            print(f'      v10a17 K2 {f+1:,}/{P:,}; H0 matches={matches:,}; elapsed={time.time()-t0:.1f}s',flush=True)
    return K2


def _v10a8_gamma_support_inner(left_labeled,right_labeled,label='',skip_support_sizes=()):
    """Gamma bilinear directly from support-resolved halves.

    This avoids the 432-term aggregate H0 blocks created when 171 local supports
    are merged before the Haar contraction.  Exact H0 signatures and lattice
    translations still provide the first orthogonality filter; whole local block
    pairs are then jointly canonicalized and memoized.
    """
    RB=_v17_phys_index(right_labeled)
    Litems=[]
    for SL,st in left_labeled.items():
        if len(SL) in set(skip_support_sizes): continue
        for key,lv in _v10a3_physical_blocks(st).items():
            Litems.append((SL,key,lv))
    # Small blocks first: immediate progress and cache warm-up before determinant blocks.
    Litems.sort(key=lambda z: len(z[2]))
    ans=0.0; sig_tests=matched=0; raw_pair_upper=0
    block_cache={}; cache_hits=cache_misses=haar_pairs=0
    t0=time.time(); last=t0
    for ii,(SL,(cs,Esg),lv) in enumerate(Litems):
        for dv in verts:
            sig_tests += 1
            tcs=_v10a2_sig_canon(_v10a3_translate_sig(cs,dv))
            candidates=RB.get((tcs,Esg),())
            if not candidates: continue
            tv={_v10a3_translate_state(st,dv):float(c) for st,c in lv.items()}
            for SR,rv in candidates:
                if len(SR) in set(skip_support_sizes): continue
                matched += 1; raw_pair_upper += len(tv)*len(rv)
                x,hit,npairs=_v10a8_block_key_and_inner(tv,rv,_qcache,block_cache)
                ans += x
                if hit: cache_hits += 1
                else: cache_misses += 1; haar_pairs += npairs
        now=time.time()
        if V10A7_PROGRESS and (now-last >= V10A8_HEARTBEAT or ii+1==len(Litems)):
            rate=(ii+1)/max(now-t0,1e-9); eta=(len(Litems)-ii-1)/rate if rate>0 else float('inf')
            print(f"      {label} heartbeat local-blocks={ii+1:,}/{len(Litems):,} size={len(lv):,} "
                  f"matches={matched:,} cache={len(block_cache):,} hits={cache_hits:,} misses={cache_misses:,} "
                  f"haar-pairs={haar_pairs:,} RAM={_v10a8_mem_gb():.2f} GiB elapsed={now-t0:.1f}s ETA~{eta/60:.1f}m",flush=True)
            last=now
    return float(ans),dict(left_blocks=len(Litems),signature_tests=sig_tests,matched_h0_blocks=matched,
        raw_pair_upper_bound=raw_pair_upper,block_cache_entries=len(block_cache),block_cache_hits=cache_hits,
        block_cache_misses=cache_misses,unique_haar_pairs=haar_pairs,elapsed=time.time()-t0)

def _v10a8_gamma_inner(left,right,haar,label=''):
    """Fast exact Gamma-point bilinear for v10a.8.

    Mathematical value is identical to _v10a4_gamma_inner.  Optimization is
    representational only: exact H0/translation matching first, whole-block
    joint canonicalization second, memoized local Haar contraction third.
    """
    LB=_v10a3_physical_blocks(left)
    RB=_v10a3_physical_blocks(right)
    ans=0.0; sig_tests=matched=0; raw_pair_upper=0
    block_cache={}
    cache_hits=cache_misses=haar_pairs=0
    t0=time.time(); last=t0
    items=list(LB.items())
    _ls=sorted((len(v) for v in LB.values()), reverse=True); _rs=sorted((len(v) for v in RB.values()), reverse=True)
    print(f'      {label} census: LB={len(LB):,} RB={len(RB):,} max-terms L/R={(_ls[0] if _ls else 0):,}/{(_rs[0] if _rs else 0):,} topL={_ls[:8]} topR={_rs[:8]}', flush=True)
    # Exact right lookup is already O(1); the 125 signature tests are cheap and
    # are retained because they are a very strong orthogonality prefilter.
    for ii,((cs,Esg),lv) in enumerate(items):
        for dv in verts:
            sig_tests += 1
            tcs=_v10a2_sig_canon(_v10a3_translate_sig(cs,dv))
            rv=RB.get((tcs,Esg))
            if rv is None:
                continue
            matched += 1
            tv={_v10a3_translate_state(st,dv):float(c) for st,c in lv.items()}
            raw_pair_upper += len(tv)*len(rv)
            x,hit,npairs=_v10a8_block_key_and_inner(tv,rv,_qcache,block_cache)
            ans += x
            if hit: cache_hits += 1
            else:
                cache_misses += 1
                haar_pairs += npairs
        now=time.time()
        if V10A7_PROGRESS and (now-last >= V10A8_HEARTBEAT or ii+1==len(items)):
            rate=(ii+1)/max(now-t0,1e-9)
            eta=(len(items)-ii-1)/rate if rate>0 else float('inf')
            print(f"      {label} heartbeat blocks={ii+1:,}/{len(items):,} "
                  f"matches={matched:,} block-cache={len(block_cache):,} "
                  f"hits={cache_hits:,} misses={cache_misses:,} haar-pairs={haar_pairs:,} "
                  f"RAM={_v10a8_mem_gb():.2f} GiB elapsed={now-t0:.1f}s ETA~{eta/60:.1f}m")
            last=now
    return float(ans),dict(left_blocks=len(LB),right_blocks=len(RB),
        signature_tests=sig_tests,matched_h0_blocks=matched,
        raw_pair_upper_bound=raw_pair_upper,block_cache_entries=len(block_cache),
        block_cache_hits=cache_hits,block_cache_misses=cache_misses,
        unique_haar_pairs=haar_pairs,elapsed=time.time()-t0)

# =============================================================================
# HODGE v10a.7 — MARKED LINKED O(u^4) SCALAR LEDGER
# =============================================================================
# PURPOSE
# -------
# Close the remaining SU(3) Gamma-point fourth-order scalar problem without a
# global Q2 Gram build.  This layer combines the already-certified ingredients:
#
#   * full-complement four-moment Feshbach formula
#         e4 = D - 2 e1 C - e2 N + e1^2 J,
#   * exact source-sector identity Q1 W Q1 = 0, hence sigma3_A=C_A=0,
#   * extended SU(3) Haar endpoint tensors through (6,0)/(0,6),
#   * cold adjacent determinant certificate,
#   * protected O(u^4) Hodge mobility values as independent firewalls.
#
# New ingredient here: SUPPORT-RESOLVED marked histories.
# Instead of rerunning every finite cluster separately, each magnetic history is
# tagged by the exact plaquette support it uses through the two-insertion half
# histories.  The labels certify the complete rooted local corpus; the final
# Gamma Haar bilinear is then evaluated after H0-block merging for tractability.
#
# Vacuum O(u^4) is treated independently.  A hard Z3/cubical-cycle gate proves
# that a nonzero connected four-insertion vacuum support uses at most two
# distinct plaquettes.  We therefore evaluate the one-face and the two adjacent
# pair vacuum clusters exactly, subtract their proper subclusters, and count
# their embeddings attached to one marked plaquette.
#
# NO historical m4 value is supplied anywhere in the construction.
# The final m4_rest is printed only after all hard gates pass.
# =============================================================================

from fractions import Fraction as _Q17
from collections import defaultdict as _dd17, Counter as _Counter17, deque as _deque17
import itertools as _it17
import gc as _gc17

V10A7_GATE_START = len(gates)
V10A7_PROGRESS = int(os.environ.get('V10A7_PROGRESS','1'))
V10A7_TOL = float(os.environ.get('V10A7_TOL','3e-9'))
V10A7_SHAPE_TOL = float(os.environ.get('V10A7_SHAPE_TOL','5e-7'))
V10A7_RAT_DEN = int(os.environ.get('V10A7_RAT_DEN','1000000000'))
V10A7_DO_SHAPE = os.environ.get('V10A7_DO_SHAPE','1') != '0'
V10A7_SUPPORT_POLS = tuple(int(x) for x in os.environ.get('V10A7_SUPPORT_POLS','0,1,2').split(',') if x.strip())
if not V10A7_SUPPORT_POLS or any(x not in (0,1,2) for x in V10A7_SUPPORT_POLS):
    raise ValueError('V10A7_SUPPORT_POLS must be a nonempty subset of 0,1,2')
V10A7_UNBLIND = os.environ.get('V10A7_UNBLIND','1') != '0'
V10A7_RECHECK_Q1 = os.environ.get('V10A7_RECHECK_Q1','0') != '0'

if L != 5:
    raise RuntimeError(f'v10a.7 requires GLUE_L=5 for the cold shape firewall; got L={L}')

print('='*136)
print('HODGE v10a.23 — PREREQUISITE HODGE/HAAR CORPUS + DUAL COLD ORACLES')
print('='*136)
print(f'backend                         : {DEVICE}')
print(f'lattice                         : L={L}')
print('global K=2 P/Q Gram build       : REMOVED')
print('global physical Q2 basis        : NOT REQUIRED')
print('Gamma source fold identity      : C_A = sigma3_A = 0 (separate exact certificate)')
print('history organization            : exact rooted half-support census + merged H0/Haar Gamma bilinear')
print('vacuum linked subtraction       : one-face + adjacent-pair clusters after Z3 cycle completeness gate')
print('historical m4 target            : NOT LOADED')
print('support-resolved polarizations  :',V10A7_SUPPORT_POLS,'(cubic representatives; set 0,1,2 for full redundancy)')
print('recheck already-exact Q1 moments:',V10A7_RECHECK_Q1)

# -----------------------------------------------------------------------------
# 0. Geometry helpers
# -----------------------------------------------------------------------------

_V17_FID = {(tuple(v),int(a),int(b)):i for i,(v,a,b) in enumerate(faces)}
_V17_NEIGH = [frozenset(face_support_faces[f]) for f in range(P)]  # includes self


def _v17_translate_face(f,dv):
    v,a,b=faces[int(f)]
    vv=((v[0]+int(dv[0]))%L,(v[1]+int(dv[1]))%L,(v[2]+int(dv[2]))%L)
    return _V17_FID[(vv,int(a),int(b))]


def _v17_translate_support(S,dv):
    return frozenset(_v17_translate_face(f,dv) for f in S)


def _v17_faces_share_link(a,b):
    if int(a)==int(b): return True
    return int(b) in _V17_NEIGH[int(a)]


def _v17_connected(S):
    S=set(map(int,S))
    if not S: return True
    seen={next(iter(S))}; q=_deque17(seen)
    while q:
        a=q.popleft()
        for b in S-seen:
            if _v17_faces_share_link(a,b):
                seen.add(b); q.append(b)
    return len(seen)==len(S)


def _v17_face_normal(f):
    _,a,b=faces[int(f)]
    return ({0,1,2}-{int(a),int(b)}).pop()


def _v17_pair_class(a,b):
    if not _v17_faces_share_link(a,b) or int(a)==int(b):
        raise ValueError('pair class requires two distinct shared-link plaquettes')
    return 'coplanar' if _v17_face_normal(a)==_v17_face_normal(b) else 'perpendicular'


def _v17_rational(x,maxden=V10A7_RAT_DEN):
    return _Q17(float(x)).limit_denominator(int(maxden))

# -----------------------------------------------------------------------------
# 1. Vacuum support-completeness theorem gate at four insertions
# -----------------------------------------------------------------------------
# A vacuum Haar endpoint must have zero linkwise Z3 boundary.  On the cubic
# complex there is no nonzero local 2-cycle on <=4 faces (the elementary cube
# is the first one, at six faces).  We cold-check the <=4 statement on every
# rooted connected support and every nonzero Z3 coefficient assignment.


def _v17_rooted_connected_subsets(root,maxsize=4):
    root=int(root)
    levels={1:{frozenset((root,))}}
    allsets=set(levels[1])
    for k in range(2,int(maxsize)+1):
        nxt=set()
        for S in levels[k-1]:
            frontier=set()
            for f in S: frontier.update(_V17_NEIGH[f])
            for g in frontier-set(S):
                T=frozenset(set(S)|{int(g)})
                if len(T)==k and _v17_connected(T): nxt.add(T)
        levels[k]=nxt; allsets.update(nxt)
    return levels,allsets

_cycle_root=next(f for f,(v,a,b) in enumerate(faces) if v==(0,0,0) and (a,b)==(0,1))
_v17_levels,_v17_subsets=_v17_rooted_connected_subsets(_cycle_root,4)
_nonzero_small_cycles=[]
for S in _v17_subsets:
    fs=tuple(sorted(S))
    if len(fs)>4: continue
    A=np.asarray(B2[:,fs],dtype=np.int16)
    for coeff in _it17.product((1,2),repeat=len(fs)):
        z=(A@np.asarray(coeff,dtype=np.int16))%3
        if np.all(z==0):
            _nonzero_small_cycles.append((fs,coeff)); break

gate('v10a.7 no nonzero rooted Z3 cubical 2-cycle exists on <=4 faces',
     len(_nonzero_small_cycles)==0,
     f"counts={dict((k,len(v)) for k,v in _v17_levels.items())}, bad={len(_nonzero_small_cycles)}")

# If the four-insertion vacuum chain itself is Z3-trivial, enumerate its signed
# multiplicities.  Every occupied face must have net coefficient 0 mod 3.
_max_support=0; _good_mult=[]
for k in range(1,5):
    for labels in _it17.product(range(k),repeat=4):
        if set(labels)!=set(range(k)): continue
        for signs in _it17.product((-1,+1),repeat=4):
            net=[0]*k
            for a,s in zip(labels,signs): net[a]+=s
            if all(x%3==0 for x in net):
                _max_support=max(_max_support,k); _good_mult.append((labels,signs))
gate('v10a.7 four-insertion Z3-trivial vacuum multiplicities use <=2 distinct faces',
     _max_support<=2,f'max distinct support={_max_support}, valid patterns={len(_good_mult)}')

# -----------------------------------------------------------------------------
# 2. Install the already-certified extended SU(3) Haar contractor
# -----------------------------------------------------------------------------

qhaar,qsupported,qcert,_qcache=_v10a2_install_q2_haar(globals())
gate('v10a.7 k=3 Weingarten inverse',qcert['wg3_inverse_error']<5e-13,f"err={qcert['wg3_inverse_error']:.3e}")
gate('v10a.7 pure-six singlet rank=5',qcert['rank60']==5,f"rank={qcert['rank60']}")
gate('v10a.7 pure-six projector idempotent',qcert['T60_idempotence_error']<5e-13,f"err={qcert['T60_idempotence_error']:.3e}")

_fsmodel=_v10a4_fs_model()

# -----------------------------------------------------------------------------
# 3. Generic restricted-W and vacuum reduced resolvent
# -----------------------------------------------------------------------------


def _v17_apply_W_faces(state,allowed_faces):
    """W=-M restricted to an explicit finite set of magnetic plaquettes."""
    out={}; actions=channels=0
    F=tuple(sorted(map(int,allowed_faces)))
    for sig,v in state.items():
        for f in F:
            for o in (-1,+1):
                actions+=1
                for pv,osig in _v10a3_project_action_dyn(_fsmodel,v,sig,f,o):
                    channels+=1; _v10a3_sig_vec_add(out,osig,pv,-1.0)
    return _v10a3_compress_state(out),dict(actions=actions,channels=channels)


_V17_VAC_ST=LXState((),())
_V17_VAC_VEC={_V17_VAC_ST:1.0}
_V17_VAC={():dict(_V17_VAC_VEC)}


def _v17_vac_R(state,label='Rv'):
    """Q(0-H0)^-1Q with exact vacuum projection in the E=0 block."""
    blocks=_v10a3_physical_blocks(state)
    resmax=0.0; ng=0
    for (cs,Esg),v0 in blocks.items():
        if Esg!=0: continue
        ng+=1; v=dict(v0)
        ov=_v10a3_vec_inner(_V17_VAC_VEC,v,qhaar)
        if abs(ov)>V10A3_COEFF_TOL:
            for st,c in _V17_VAC_VEC.items(): v[st]=v.get(st,0.0)-ov*c
        v=_v10a3_prune(v)
        resmax=max(resmax,_v10a3_vec_norm(v,qhaar))
    if resmax>V10A3_NORM_TOL:
        raise RuntimeError(f'{label}: unresolved E=0 vacuum residual norm2={resmax:.3e}')
    out={}
    for sig,v in state.items():
        Esg=_v10a2_sig_E(sig)
        if Esg==0: continue
        den=-float(Esg)
        out[sig]={st:float(c)/den for st,c in v.items()}
    return _v10a3_compress_state(out),dict(E0_groups=ng,E0_residual_norm2_max=resmax)


def _v17_inner(a,b):
    return _v10a3_h0_state_inner(a,b,qhaar)[0]


def _v17_vac_cluster(C):
    C=frozenset(map(int,C))
    w1,_=_v17_apply_W_faces(_V17_VAC,C)
    r1,s1=_v17_vac_R(w1,'vac R1')
    w2,_=_v17_apply_W_faces(r1,C)
    r2,s2=_v17_vac_R(w2,'vac R2')
    e1=_v17_inner(_V17_VAC,w1)
    e2=_v17_inner(w1,r1)
    sig3=_v17_inner(r1,w2)
    Nn=_v17_inner(r1,r1)
    Dd=_v17_inner(w2,r2)
    e3=sig3 # e1=0
    e4=Dd-e2*Nn
    return dict(C=C,e1=e1,e2=e2,sigma3=sig3,e3=e3,N=Nn,D=Dd,e4=e4,
                pole=max(s1['E0_residual_norm2_max'],s2['E0_residual_norm2_max']))

# One-face vacuum is the exact compact character laboratory, now through the
# same Wilson/H0/Haar history engine used below.
_vac_seed=_cycle_root
_v1=_v17_vac_cluster({_vac_seed})
print('\n[3] COLD ONE-FACE VACUUM CLUSTER')
for k in ('e1','e2','sigma3','e3','N','D','e4'):
    print(f'  {k:7s} = {_v1[k]:+.15g}  rational~ {_v17_rational(_v1[k])}')
gate('v10a.7 one-face vacuum e1=0',abs(_v1['e1'])<V10A7_TOL,_v1['e1'])
gate('v10a.7 one-face vacuum e2=-3/4',abs(_v1['e2']+3/4)<V10A7_TOL,_v1['e2'])
gate('v10a.7 one-face vacuum e3=-9/32',abs(_v1['e3']+9/32)<V10A7_TOL,_v1['e3'])
gate('v10a.7 one-face vacuum N=9/32',abs(_v1['N']-9/32)<V10A7_TOL,_v1['N'])
gate('v10a.7 one-face vacuum D=-309/1280',abs(_v1['D']+309/1280)<V10A7_TOL,_v1['D'])
gate('v10a.7 one-face vacuum e4=-39/1280',abs(_v1['e4']+39/1280)<V10A7_TOL,_v1['e4'])

# Two adjacent vacuum cluster representatives.
_pair_rep={}
for q in sorted(_V17_NEIGH[_vac_seed]-{_vac_seed}):
    cls=_v17_pair_class(_vac_seed,q)
    _pair_rep.setdefault(cls,q)
if set(_pair_rep)!={'coplanar','perpendicular'}:
    raise RuntimeError(f'failed to find both vacuum adjacent pair classes: {_pair_rep}')

_vpair={}
print('\n[4] COLD TWO-FACE VACUUM CLUSTERS')
for cls,q in sorted(_pair_rep.items()):
    z=_v17_vac_cluster({_vac_seed,q})
    linked=z['e4']-2.0*_v1['e4']
    linked_e2=z['e2']-2.0*_v1['e2']
    linked_e3=z['e3']-2.0*_v1['e3']
    _vpair[cls]=dict(full=z,linked_e4=linked,linked_e2=linked_e2,linked_e3=linked_e3)
    print(f'  {cls:13s}: e4(C)={z["e4"]:+.15g} ~ {_v17_rational(z["e4"])}; '
          f'omega4={linked:+.15g} ~ {_v17_rational(linked)}')
    gate(f'v10a.7 vacuum {cls} pair has no linked O(u^2)',abs(linked_e2)<V10A7_TOL,linked_e2)
    gate(f'v10a.7 vacuum {cls} pair has no linked O(u^3)',abs(linked_e3)<V10A7_TOL,linked_e3)
    gate(f'v10a.7 vacuum {cls} pair full e4=-54321/837760',abs(z['e4']-float(_Q17(-54321,837760)))<V10A7_TOL,z['e4'])
    gate(f'v10a.7 vacuum {cls} pair omega4=-327/83776',abs(linked-float(_Q17(-327,83776)))<V10A7_TOL,linked)

gate('v10a.7 coplanar/perpendicular vacuum pair linked weights agree',abs(_vpair['coplanar']['linked_e4']-_vpair['perpendicular']['linked_e4'])<V10A7_TOL,_vpair['coplanar']['linked_e4']-_vpair['perpendicular']['linked_e4'])

# Exact disconnected-spectator check: a two-face vacuum cluster with no shared
# link must factorize, so its irreducible pair weight is identically zero.
_far=next(f for f in range(P) if f!=_vac_seed and f not in _V17_NEIGH[_vac_seed])
_vfar=_v17_vac_cluster({_vac_seed,_far})
_vfar_omega=_vfar['e4']-2.0*_v1['e4']
print(f'  disconnected pair spectator omega4={_vfar_omega:+.3e}')
gate('v10a.7 disconnected two-face vacuum spectator has zero linked O(u^4)',abs(_vfar_omega)<V10A7_TOL,_vfar_omega)

# Count vacuum linked-cluster embeddings attached to one marked plaquette.
_mark=_vac_seed
_single_emb=sorted(_V17_NEIGH[_mark])
_pairs=set()
for a in range(P):
    for b in _V17_NEIGH[a]:
        b=int(b)
        if b<=a: continue
        if not _v17_faces_share_link(a,b): continue
        if _v17_connected({_mark,a,b}): _pairs.add(frozenset((a,b)))
_pair_counts=_Counter17(_v17_pair_class(*tuple(S)) for S in _pairs)
print('\n[5] VACUUM EMBEDDINGS ATTACHED TO ONE MARKED PLAQUETTE')
print('  one-face embeddings:',len(_single_emb))
print('  adjacent-pair embeddings:',dict(_pair_counts),'total=',len(_pairs))
gate('v10a.7 one-face vacuum embedding count is 13',len(_single_emb)==13,len(_single_emb))

V4_LINKED_MARKED = len(_single_emb)*_v1['e4']
for cls,n in _pair_counts.items(): V4_LINKED_MARKED += int(n)*_vpair[cls]['linked_e4']
print(f'  linked vacuum O4 subtraction around mark = {V4_LINKED_MARKED:+.15g}  rational~ {_v17_rational(V4_LINKED_MARKED)}')
_V4_EX=_Q17(-1474623,1675520)
gate('v10a.7 linked vacuum O4 subtraction=-1474623/1675520',abs(V4_LINKED_MARKED-float(_V4_EX))<V10A7_TOL,V4_LINKED_MARKED)

# -----------------------------------------------------------------------------
# 4. Support-resolved connected axial recursion
# -----------------------------------------------------------------------------


def _v17_add_state(dst,src,scale=1.0):
    for sig,v in src.items(): _v10a3_sig_vec_add(dst,sig,v,scale)


def _v17_aggregate(LD):
    out={}
    for st in LD.values(): _v17_add_state(out,st,1.0)
    return _v10a3_compress_state(out)


def _v17_apply_W_labeled(LD,label='W'):
    out={}; actions=channels=0
    items=list(LD.items()); t0=time.time()
    for ii,(S,state) in enumerate(items):
        for sig,v in state.items():
            cand=_v10a3_candidate_faces_vec(v)
            for f in cand:
                for o in (-1,+1):
                    actions+=1
                    for pv,osig in _v10a3_project_action_dyn(_fsmodel,v,sig,int(f),int(o)):
                        channels+=1
                        T=frozenset(set(S)|{int(f)})
                        d=out.setdefault(T,{})
                        _v10a3_sig_vec_add(d,osig,pv,-1.0)
        if V10A7_PROGRESS and len(items)>20 and (ii+1)%max(1,len(items)//4)==0:
            print(f'      {label} supports {ii+1}/{len(items)}; out supports={len(out)}; elapsed={time.time()-t0:.1f}s')
    return {S:_v10a3_compress_state(st) for S,st in out.items() if _v10a3_compress_state(st)},dict(actions=actions,channels=channels)


def _v17_R_labeled(LD,label='R'):
    out={}; mx=0.0; ng=0
    for S,st in LD.items():
        rr,ss=_v10a3_reduced_resolvent(st,qhaar,label)
        mx=max(mx,float(ss['E0_residual_norm2_max'])); ng+=int(ss['E0_groups'])
        if rr: out[S]=rr
    return out,dict(E0_groups=ng,E0_residual_norm2_max=mx)


def _v17_phys_index(LD):
    idx=_dd17(list)
    for S,st in LD.items():
        for key,v in _v10a3_physical_blocks(st).items(): idx[key].append((S,v))
    return idx


def _v17_gamma_ledger(left,right,label='Gamma'):
    """Return exact-support ledger for <left_Gamma|right_Gamma>.

    Right source remains anchored.  Each translated left support is unioned with
    the right support before accumulation, so every contribution is assigned to
    its minimal marked plaquette support.
    """
    RB=_v17_phys_index(right)
    ledger=_dd17(float); tests=matches=haar_terms=0; t0=time.time()
    Litems=[]
    for SL,st in left.items():
        for key,lv in _v10a3_physical_blocks(st).items(): Litems.append((SL,key,lv))
    for ii,(SL,(cs,Esg),lv) in enumerate(Litems):
        for dv in verts:
            tests+=1
            tcs=_v10a2_sig_canon(_v10a3_translate_sig(cs,dv))
            candidates=RB.get((tcs,Esg),())
            if not candidates: continue
            matches+=len(candidates)
            tv={_v10a3_translate_state(st,dv):float(c) for st,c in lv.items()}
            tSL=_v17_translate_support(SL,dv)
            for SR,rv in candidates:
                x=_v10a3_vec_inner(tv,rv,qhaar)
                if abs(x)>1e-16:
                    ledger[frozenset(set(tSL)|set(SR))]+=float(x)
                haar_terms+=len(tv)*len(rv)
        if V10A7_PROGRESS and len(Litems)>200 and (ii+1)%max(1,len(Litems)//5)==0:
            print(f'      {label} blocks {ii+1}/{len(Litems)}; H0 matches={matches}; supports={len(ledger)}; elapsed={time.time()-t0:.1f}s')
    ledger={S:x for S,x in ledger.items() if abs(x)>2e-13}
    return ledger,dict(left_blocks=len(Litems),signature_tests=tests,matched_h0_blocks=matches,haar_upper=haar_terms)


def _v17_sum(L): return float(sum(L.values()))


def _v17_add_ledger(dst,src,scale=1.0):
    for S,x in src.items(): dst[S]+=float(scale)*float(x)


def _v17_union_convolution(A,B):
    out=_dd17(float)
    for SA,a in A.items():
        for SB,b in B.items(): out[frozenset(set(SA)|set(SB))]+=float(a)*float(b)
    return {S:x for S,x in out.items() if abs(x)>2e-13}


def _v17_size_summary(ledger):
    c=_Counter17(); w=_dd17(float)
    for S,x in ledger.items(): c[len(S)]+=1; w[len(S)]+=float(x)
    return dict(sorted(c.items())),dict(sorted(w.items()))

# Anchors are exactly the three origin T1 faces used by the endpoint/Bloch code.
anchor_faces=[next(f for f,(v,a,b) in enumerate(faces) if v==(0,0,0) and (a,b)==pol) for pol in T1_POLS]
print('\n[6] SUPPORT-RESOLVED AXIAL HALF-HISTORIES')
print('  anchor faces:',[(f,faces[f]) for f in anchor_faces])

S0s={}; W1Ls={}; R1Ls={}; W2Ls={}; R2Ls={}; R12Ls={}
W1s={};R1s={};W2s={};R2s={};R12s={}
resmax=0.0
for a in V10A7_SUPPORT_POLS:
    p0=anchor_faces[a]
    print(f'  polarization {a} {T1_POLS[a]}')
    S0={frozenset((p0,)):_v10a3_face_state(p0)}; S0s[a]=S0
    W1L,sw1=_v17_apply_W_labeled(S0,f'W1 pol{a}')
    R1L,sr1=_v17_R_labeled(W1L,f'R1 pol{a}')
    W2L,sw2=_v17_apply_W_labeled(R1L,f'W2 pol{a}')
    R2L,sr2=_v17_R_labeled(W2L,f'R2 pol{a}')
    R12L,sr12=_v17_R_labeled(R1L,f'R(R1) pol{a}')
    resmax=max(resmax,sr1['E0_residual_norm2_max'],sr2['E0_residual_norm2_max'],sr12['E0_residual_norm2_max'])
    W1Ls[a]=W1L;R1Ls[a]=R1L;W2Ls[a]=W2L;R2Ls[a]=R2L;R12Ls[a]=R12L
    W1s[a]=_v17_aggregate(W1L);R1s[a]=_v17_aggregate(R1L);W2s[a]=_v17_aggregate(W2L);R2s[a]=_v17_aggregate(R2L);R12s[a]=_v17_aggregate(R12L)
    print('    support counts W1/R1/W2/R2 =',len(W1L),len(R1L),len(W2L),len(R2L))
    print('    aggregate state stats W1/R1/W2/R2 =',_v10a3_state_stats(W1s[a]),_v10a3_state_stats(R1s[a]),_v10a3_state_stats(W2s[a]),_v10a3_state_stats(R2s[a]))

gate('v10a.7 all support-resolved reduced resolvents are free of E0 poles',resmax<V10A7_TOL,f'max residual norm2={resmax:.3e}')


# =============================================================================
# HODGE v10a.23 — DEGENERATE-FOLD FULL-T1 K4 OPERATOR
# =============================================================================
# This is the first layer in this solver that is allowed to form a fourth-order
# *operator* on the complete one-flux model space.  It does not use either
# disputed fourth-order scalar, nor the historical fourth-order C-shape target.
#
# Definitions (R = Q(E0-H0)^-1 Q):
#   K2 = B^T R B
#   N  = B^T R^2 B
#   J  = B^T R^3 B
#   D  = B^T R W R W R B
#   C1 = B^T R^2 W R B
# If PVP = a I on the full one-flux P space, the Hermitian canonical
# (des-Cloizeaux / SW) fourth-order block is
#
#   H4 = D - a(C1+C1^T) - 1/2 {K2,N} + a^2 J.
#
# The notebook first derives/regression-tests this operator identity on exact
# rational finite Hamiltonians with dim(P)=2.  It then proves/falsifies PVP=aP
# in the physical Wilson-network model before applying the formula.
# =============================================================================

import random as _v23_random
import sympy as _v23_sp
import hashlib as _v23_hashlib

V23_GATE_START=len(gates)
V23_TOL=float(os.environ.get('V10A23_TOL','3e-8'))
V23_RECORD_TOL=float(os.environ.get('V10A23_RECORD_TOL','2e-8'))
V23_HEART=float(os.environ.get('V10A23_HEARTBEAT','15'))

print('\n'+'='*148)
print('HODGE v10a.24c — DEGENERATE-FOLD FULL-T1 FOURTH-ORDER OPERATOR')
print('='*148)
print('disputed q/rest targets          : NOT LOADED')
print('historical C-shape target        : NOT LOADED')
print('PVP=aP                           : COMPUTED, NOT ASSUMED')
print('folded formula                   : EXACT dim(P)>1 SW REGRESSION FIRST')
print('full T1 polarizations            : 3')

# -----------------------------------------------------------------------------
# 1. Exact degenerate Schrieffer-Wolff regression of the operator formula
# -----------------------------------------------------------------------------

def _v23_smul(A,B):
    order=len(A)-1; n=A[0].rows
    out=[_v23_sp.zeros(n) for _ in range(order+1)]
    for k in range(order+1):
        z=_v23_sp.zeros(n)
        for i in range(k+1): z += A[i]*B[k-i]
        out[k]=z
    return out


def _v23_scomm(A,B):
    AB=_v23_smul(A,B); BA=_v23_smul(B,A)
    return [AB[i]-BA[i] for i in range(len(A))]


def _v23_bch(H,S,order):
    out=[x.copy() for x in H]; X=[x.copy() for x in H]; fac=1
    for k in range(1,order+1):
        X=_v23_scomm(X,S); fac*=k
        out=[out[i]+X[i]/_v23_sp.Integer(fac) for i in range(order+1)]
    return out


def _v23_sw_exact(H0,V,p,order=4):
    n=H0.rows
    H=[_v23_sp.zeros(n) for _ in range(order+1)]; H[0]=H0; H[1]=V
    S=[_v23_sp.zeros(n) for _ in range(order+1)]
    E0=H0[0,0]
    for r in range(1,order+1):
        base=_v23_bch(H,S,order)[r]
        Sr=_v23_sp.zeros(n)
        for q in range(p,n):
            den=H0[q,q]-E0
            for j in range(p):
                Sr[q,j]=-_v23_sp.cancel(base[q,j]/den)
                Sr[j,q]=-Sr[q,j]
        S[r]=Sr
    Hf=_v23_bch(H,S,order)
    return [_v23_sp.simplify(Hf[r][:p,:p]) for r in range(order+1)]


def _v23_fold_formula_exact(H0,V,p):
    E0=H0[0,0]; a=V[0,0]
    B=V[p:,:p]; W=V[p:,p:]
    R=_v23_sp.diag(*[_v23_sp.cancel(1/(E0-H0[i,i])) for i in range(p,H0.rows)])
    K2=_v23_sp.simplify(B.T*R*B)
    N =_v23_sp.simplify(B.T*(R**2)*B)
    J =_v23_sp.simplify(B.T*(R**3)*B)
    C1=_v23_sp.simplify(B.T*(R**2)*W*R*B)
    D =_v23_sp.simplify(B.T*R*W*R*W*R*B)
    K3=_v23_sp.simplify(B.T*R*W*R*B-a*N)
    H4=_v23_sp.simplify(D-a*(C1+C1.T)-_v23_sp.Rational(1,2)*(K2*N+N*K2)+a*a*J)
    return K2,K3,H4


def _v23_degenerate_fold_regression():
    rows=[]
    for seed in (2301,2302,2303,2304):
        rr=_v23_random.Random(seed); p=2; n=5
        H0=_v23_sp.diag(0,0,2,3,5)
        a=_v23_sp.Integer(rr.randint(-2,2))
        V=_v23_sp.zeros(n); V[:p,:p]=a*_v23_sp.eye(p)
        for i in range(p,n):
            for j in range(p):
                x=_v23_sp.Integer(rr.randint(-2,2)); V[i,j]=V[j,i]=x
        for i in range(p,n):
            for j in range(i,n):
                x=_v23_sp.Integer(rr.randint(-2,2)); V[i,j]=V[j,i]=x
        sw=_v23_sw_exact(H0,V,p,4)
        K2,K3,H4=_v23_fold_formula_exact(H0,V,p)
        B=V[p:,:p]; R=_v23_sp.diag(*[_v23_sp.cancel(1/(H0[0,0]-H0[i,i])) for i in range(p,n)])
        N=B.T*(R**2)*B
        noncomm=(_v23_sp.simplify(K2*N-N*K2)!=_v23_sp.zeros(p))
        e2=_v23_sp.simplify(sw[2]-K2)
        e3=_v23_sp.simplify(sw[3]-K3)
        e4=_v23_sp.simplify(sw[4]-H4)
        ok=(e2==_v23_sp.zeros(p) and e3==_v23_sp.zeros(p) and e4==_v23_sp.zeros(p))
        rows.append((seed,a,ok,noncomm))
    return rows

print('\n[10] EXACT DEGENERATE FOLD REGRESSION')
_v23_reg=_v23_degenerate_fold_regression()
gate('v10a.23 exact dim(P)=2 SW regressions prove folded operator formula',
     all(x[2] for x in _v23_reg),_v23_reg)
gate('v10a.23 toy regressions genuinely test noncommuting K2 and N',all(x[3] for x in _v23_reg),_v23_reg)

# -----------------------------------------------------------------------------
# 2. Physical PVP=aP gate — computed from the actual one-W trace-network action
# -----------------------------------------------------------------------------
print('\n[11] PHYSICAL PVP MODEL-SPACE GATE')
PVP_anchor=np.column_stack([_v10a3_project_P0(W1s[a],qhaar) for a in range(3)])
PVP_round=np.rint(PVP_anchor)
pvp_lift_err=float(np.max(np.abs(PVP_anchor-PVP_round)))
PVP_expected=np.zeros_like(PVP_round)
for a,f in enumerate(anchor_faces): PVP_expected[int(f),a]=1.0
pvp_struct_err=float(np.max(np.abs(PVP_round-PVP_expected)))
gate('v10a.23 physical PVP coefficients lift unambiguously to integers',pvp_lift_err<2e-10,pvp_lift_err)
gate('v10a.23 physical PVP is exactly +I under translation covariance',pvp_struct_err==0.0,
     f'lift_err={pvp_lift_err:.3e}, structural_err={pvp_struct_err:.1f}')
A_PVP=1.0

# -----------------------------------------------------------------------------
# 3. General translation-resolved pair-collapsed bilinear (no D-only shortcut)
# -----------------------------------------------------------------------------

def _v23_endpoint_general(left_labeled,right_labeled,left_root,right_root,label=''):
    heartbeat=V23_HEART
    pair_tol=float(os.environ.get('V10A23_PAIR_TOL','2e-14'))
    RB=_v17_phys_index(right_labeled)
    Litems=[]
    for SL,st in left_labeled.items():
        for key,lv in _v10a3_physical_blocks(st).items(): Litems.append((SL,key,lv))
    Litems.sort(key=lambda z:len(z[2]))

    tasks={}; matches=raw_pair_upper=0
    t0=time.time(); last=t0
    for ii,(SL,(cs,Esg),lv) in enumerate(Litems):
        for dv in verts:
            tcs=_v10a2_sig_canon(_v10a3_translate_sig(cs,dv))
            candidates=RB.get((tcs,Esg),())
            if not candidates: continue
            tv={_v10a3_translate_state(st,dv):float(c) for st,c in lv.items()}
            for SR,rv in candidates:
                matches+=1; raw_pair_upper+=len(tv)*len(rv)
                key,A,B=_v10a10_canon_block_pair(tv,rv)
                rec=tasks.get(key)
                if rec is None:
                    rec=[A,B,Counter()]; tasks[key]=rec
                rec[2][tuple(dv)]+=1
        now=time.time()
        if V10A7_PROGRESS and (now-last>=heartbeat or ii+1==len(Litems)):
            rate=(ii+1)/max(now-t0,1e-9); eta=(len(Litems)-ii-1)/rate if rate else 0.0
            print(f'      {label} scan {ii+1:,}/{len(Litems):,}; matches={matches:,}; '
                  f'blocks={len(tasks):,}; raw-pairs<={raw_pair_upper:,}; elapsed={now-t0:.1f}s ETA~{eta:.1f}s',flush=True)
            last=now

    pairw={}; pair_occ=0
    recs=list(tasks.values()); tp=time.time(); last=tp
    for ti,(A,B,dv_mult) in enumerate(recs):
        ga=defaultdict(list); gb=defaultdict(list)
        for st,c in A: ga[_v9_flux_key_state(st)].append((st,c))
        for st,c in B: gb[_v9_flux_key_state(st)].append((st,c))
        multsum=sum(dv_mult.values())
        for fk,la in ga.items():
            lb=gb.get(fk)
            if not lb: continue
            for aa,ca in la:
                for bb,cb in lb:
                    x,y=_joint_canon_states(aa,bb)
                    if (y.occ,y.part)<(x.occ,x.part): x,y=y,x
                    pk=(x,y); dw=pairw.get(pk)
                    if dw is None: dw=defaultdict(float); pairw[pk]=dw
                    base=float(ca)*float(cb)
                    for dv,mult in dv_mult.items(): dw[dv]+=base*float(mult)
                    pair_occ+=multsum
        now=time.time()
        if V10A7_PROGRESS and (now-last>=heartbeat or ti+1==len(recs)):
            print(f'      {label} collapse {ti+1:,}/{len(recs):,}; pair-occ={pair_occ:,}; unique={len(pairw):,}; elapsed={now-tp:.1f}s',flush=True)
            last=now

    pairw={k:{dv:w for dv,w in d.items() if abs(w)>pair_tol} for k,d in pairw.items()}
    pairw={k:d for k,d in pairw.items() if d}
    reps={}
    for a,b in pairw:
        pats=tuple(sorted(_v10_endpoint_patterns(a,b))); reps.setdefault(pats,(a,b))
    ferr=[]
    for a,b in reps.values(): ferr.append(abs(float(_qcache(a,b))-float(_v10a13_haar_factor(a,b))))
    gate(f'{label} factorized Haar matches dense endpoint signatures',max(ferr,default=0.0)<5e-12,
         f'maxerr={max(ferr,default=0.0):.3e}, signatures={len(reps)}')

    out=defaultdict(float); items=list(pairw.items())
    items.sort(key=lambda kv:_v10a13_pair_score(kv[0][0],kv[0][1]),reverse=True)
    te=time.time(); last=te
    for ii,((a,b),weights) in enumerate(items,1):
        h=_v10a17_factor_haar_cached(a,b)
        if h:
            for dv,w in weights.items(): out[dv]+=h*w
        now=time.time()
        if V10A7_PROGRESS and (now-last>=heartbeat or ii%2000==0 or ii==len(items)):
            rate=ii/max(now-te,1e-9); eta=(len(items)-ii)/rate if rate else 0.0
            print(f'      {label} Haar {ii:,}/{len(items):,}; elapsed={now-te:.1f}s ETA~{eta:.1f}s',flush=True); last=now
    out={dv:float(x) for dv,x in out.items() if abs(x)>2e-13}
    print(f'      {label} COMPLETE gamma-sum={sum(out.values()):+.15g}; translations={len(out)}; total={time.time()-t0:.1f}s',flush=True)
    return out,dict(
        left_blocks=len(Litems),
        matched_blocks=matches,
        raw_pair_upper=raw_pair_upper,
        unique_block_pairs=len(tasks),
        pair_occurrences=pair_occ,
        unique_haar_pairs=len(pairw),
        total_seconds=time.time()-t0
    )


def _v23_endpoint_cols(leftLD,rightLD,name,d_special=False):
    cols=np.zeros((P,3),dtype=np.float64); stats={}
    for ai in range(3):
        print(f'  {name}: ket polarization {ai} {T1_POLS[ai]}')
        for bi in range(3):
            lab=f'v10a23 {name} bra{bi}->ket{ai}'
            if d_special:
                vec,st=_v10a17_endpoint_vector(leftLD[bi],rightLD[ai],anchor_faces[bi],anchor_faces[ai],lab)
            else:
                vec,st=_v23_endpoint_general(leftLD[bi],rightLD[ai],anchor_faces[bi],anchor_faces[ai],lab)
            stats[(bi,ai)]=st
            for dv,x in vec.items():
                ff=next(iter(_v17_translate_support(frozenset((anchor_faces[bi],)),dv)))
                cols[int(ff),ai]+=float(x)
    return cols,stats


def _v23_cols_to_full(cols):
    pol_index={pol:i for i,pol in enumerate(T1_POLS)}
    M=np.zeros((P,P),dtype=np.float64)
    nz=[np.flatnonzero(np.abs(cols[:,a])>1e-14) for a in range(3)]
    for src,(v,a,b) in enumerate(faces):
        ai=pol_index[(a,b)]
        for f0 in nz[ai]:
            f=_v17_translate_face(int(f0),v)
            M[int(f),int(src)]=float(cols[int(f0),ai])
    return M


def _v23_full_to_cols(M):
    return np.column_stack([M[:,int(anchor_faces[a])] for a in range(3)])


def _v23_herm_gate(name,M,tol=V23_TOL):
    e=float(np.max(np.abs(M-M.T)))
    gate(f'v10a.23 {name} is Hermitian',e<tol,e)
    return 0.5*(M+M.T),e

# -----------------------------------------------------------------------------
# 4. Cold-build all operator moments and assemble the folded H4 matrix
# -----------------------------------------------------------------------------
print('\n[12] FULL-T1 OPERATOR MOMENTS')
K2_cols=_v10a17_build_K2([W1s[a] for a in range(3)],[R1s[a] for a in range(3)])
K2_full=_v23_cols_to_full(K2_cols); K2_full,_=_v23_herm_gate('K2',K2_full)
n2,e2err=_v10a3_second_order_t3_gate(K2_cols,anchor_faces)
gate('v10a.23 K2 retains all 36 exact t3 hoppings',n2==36 and e2err<5e-9,f'tests={n2}, maxerr={e2err:.3e}')

N_cols,N_stats=_v23_endpoint_cols(R1Ls,R1Ls,'N=<R1|R1>')
J_cols,J_stats=_v23_endpoint_cols(R1Ls,R12Ls,'J=<R1|R^2B>')
C1_cols,C1_stats=_v23_endpoint_cols(R1Ls,R2Ls,'C1=<R1|RWRB>')
D_cols,D_stats=_v23_endpoint_cols(W2Ls,R2Ls,'D=<WRB|RWRB>',d_special=True)

N_full,_=_v23_herm_gate('N',_v23_cols_to_full(N_cols))
J_full,_=_v23_herm_gate('J',_v23_cols_to_full(J_cols))
D_full,_=_v23_herm_gate('D',_v23_cols_to_full(D_cols))
C1_full=_v23_cols_to_full(C1_cols)
L_full=C1_full+C1_full.T

H4_ax_full=(D_full-A_PVP*L_full-0.5*(K2_full@N_full+N_full@K2_full)+(A_PVP*A_PVP)*J_full)
H4_ax_full,_=_v23_herm_gate('folded axial H4',H4_ax_full,5*V23_TOL)
H4_ax_cols=_v23_full_to_cols(H4_ax_full)

print('\n[13] FOLDED AXIAL BLOCH/HODGE SHAPE — STILL BLIND')
shape23=_v10a3_extract_shape(H4_ax_cols)
for k in ('rest_direct','A','B','C_direct','D','alpha','fifth_residual_max','hermiticity_error','gamma_spread'):
    print(f'  {k:22s} = {shape23[k]:+.15g}')

gate('v10a.23 folded axial Gamma block is cubic/scalar',shape23['gamma_spread']<5e-7,shape23['gamma_spread'])
gate('v10a.23 folded axial real-space kernel is Hermitian',shape23['hermiticity_error']<5e-7,shape23['hermiticity_error'])
gate('v10a.23 protected A3^shp=5/48',abs(shape23['A']-5/48)<5e-6,shape23['A'])
gate('v10a.23 protected B3^shp=0',abs(shape23['B'])<5e-6,shape23['B'])
gate('v10a.23 protected D3^shp=0',abs(shape23['D'])<5e-6,shape23['D'])
gate('v10a.23 protected alpha3=5/12',abs(shape23['alpha']-5/12)<2e-5,shape23['alpha'])
gate('v10a.23 folded full-shape residual closes',shape23['fifth_residual_max']<1e-5,shape23['fifth_residual_max'])

# Gamma scalar check against the independently exact one-polarization direct/fold
# moments.  This is a regression only; it is NOT called a physical mass.
D_gamma=float(np.trace(_v10a3_bloch_from_anchor(D_cols,(0,0,0))).real/3.0)
N_gamma=float(np.trace(_v10a3_bloch_from_anchor(N_cols,(0,0,0))).real/3.0)
J_gamma=float(np.trace(_v10a3_bloch_from_anchor(J_cols,(0,0,0))).real/3.0)
C_gamma=float(np.trace(_v10a3_bloch_from_anchor(C1_cols,(0,0,0))).real/3.0)
H4_gamma_formula=D_gamma-2*A_PVP*C_gamma-float(_Q17(-5945,612))*N_gamma+A_PVP*A_PVP*J_gamma
print('  Gamma moment audit:')
print('    D =',D_gamma,' C =',C_gamma,' N =',N_gamma,' J =',J_gamma)
print('    scalar folded formula =',H4_gamma_formula)
print('    matrix H4 Gamma       =',shape23['rest_direct'])
gate('v10a.23 matrix fold reduces to scalar Feshbach formula at Gamma',
     abs(H4_gamma_formula-shape23['rest_direct'])<2e-6,
     abs(H4_gamma_formula-shape23['rest_direct']))

# Persist blind outputs for the independent linked oracle below.
V23_AXIAL_H4_COLS=H4_ax_cols
V23_AXIAL_SHAPE=shape23
V23_AXIAL_RECORDS=int(np.count_nonzero(np.abs(H4_ax_cols)>V23_RECORD_TOL))
print('  blind folded axial nonzero anchored records =',V23_AXIAL_RECORDS)

# =============================================================================
# HODGE v10a.24c — INDEPENDENT ROOTED FINITE-CLUSTER LINKED-GAP ORACLE
# =============================================================================
# This second leg does NOT use any of the operator-moment ledgers above to obtain
# the physical rest coefficient.  The W1/W2 histories are used only as a SUPPORT
# census.  Each raw finite-cluster coefficient is recomputed by diagonalizing
# H_C(u)=H0+uV_C on that restricted cluster, constructing the Hermitian
# des-Cloizeaux one-particle block, subtracting an independently diagonalized
# vacuum level, and only then performing rooted incidence subtraction.
#
# The disputed fourth-order values remain absent until all lower-order and
# numerical-stability gates pass.
# =============================================================================

import itertools as _v23c_it
import math as _v23c_math
import time as _v23c_time
from collections import defaultdict as _v23c_dd, Counter as _v23c_Counter
from fractions import Fraction as _V23CF
from numpy.polynomial import Polynomial as _V23Poly
from scipy.linalg import eigh as _v23c_eigh

V23C_POL=int(os.environ.get('V10A23_CLUSTER_POL','2'))
V23C_ROOT=int(anchor_faces[V23C_POL])
V23C_GRAM_TOL=float(os.environ.get('V10A23_CLUSTER_GRAM_TOL','2e-10'))
V23C_HERM_TOL=float(os.environ.get('V10A23_CLUSTER_HERM_TOL','2e-8'))
V23C_FIT_UMAX=float(os.environ.get('V10A23_CLUSTER_FIT_UMAX','0.055'))
V23C_FIT_DEG=int(os.environ.get('V10A23_CLUSTER_FIT_DEG','6'))
V23C_FIT_N=int(os.environ.get('V10A23_CLUSTER_FIT_N','13'))
V23C_FIT_STAB_TOL=float(os.environ.get('V10A23_CLUSTER_FIT_STAB_TOL','5e-3'))
V23C_SYM_CHECKS=int(os.environ.get('V10A23_CLUSTER_SYM_CHECKS','4'))
V23C_PROGRESS=int(os.environ.get('V10A23_CLUSTER_PROGRESS','1'))

if V23C_FIT_N < V23C_FIT_DEG+3 or V23C_FIT_N%2==0:
    raise ValueError('V10A23_CLUSTER_FIT_N must be odd and at least FIT_DEG+3')

print('\n'+'='*148)
print('HODGE v10a.23 — INDEPENDENT FINITE-CLUSTER LINKED-GAP ORACLE')
print('='*148)
print('root/polarization                :',V23C_ROOT,faces[V23C_ROOT],V23C_POL)
print('raw cluster coefficients         : RECOMPUTED FROM RESTRICTED HAMILTONIANS')
print('operator H4 moment ledger        : NOT USED FOR REST COEFFICIENT')
print('disputed fourth-order values     : STILL NOT LOADED')
print('Krylov closure                   : P + Q1 + Q2')
print('fit                              : symmetric polynomial, umax=',V23C_FIT_UMAX,'deg=',V23C_FIT_DEG,'N=',V23C_FIT_N)

# ------------------------------- state algebra -------------------------------
def _v23c_state_copy(a):
    return {sig:{st:float(c) for st,c in v.items()} for sig,v in a.items()}

def _v23c_state_add(dst,src,scale=1.0):
    s=float(scale)
    for sig,v in src.items():
        d=dst.setdefault(sig,{})
        for st,c in v.items(): d[st]=d.get(st,0.0)+s*float(c)
    return _v10a3_compress_state(dst)

def _v23c_state_scaled(a,scale):
    z={}; return _v23c_state_add(z,a,scale)

def _v23c_inner(a,b): return float(_v10a3_h0_state_inner(a,b,qhaar)[0])

def _v23c_norm2(a):
    x=_v23c_inner(a,a)
    if x < -5e-9: raise RuntimeError(f'negative Haar norm2 in cluster oracle: {x:.3e}')
    return max(0.0,x)

def _v23c_split_h0(state):
    out={}
    for sig,v in state.items():
        key=(_v10a2_sig_canon(sig),_v10a2_sig_E(sig))
        d=out.setdefault(key,{})
        d[sig]={st:float(c) for st,c in v.items()}
    ans={}
    for k,v in out.items():
        z=_v10a3_compress_state(v)
        if z: ans[k]=z
    return ans

def _v23c_applyW(state,C): return _v17_apply_W_faces(state,C)[0]

# -------------------------- finite-cluster Krylov basis ----------------------
def _v23c_build_basis(C,vacuum=False):
    C=frozenset(map(int,C))
    if not C: raise ValueError('empty finite cluster')
    pfaces=tuple(sorted(C)) if not vacuum else ()
    initial=[_v23c_state_copy(_V17_VAC)] if vacuum else [_v23c_state_copy(_v10a3_face_state(f)) for f in pfaces]
    basis=[]; bykey=_v23c_dd(list); p_indices=[]

    def add_raw(raw,key,layer,name):
        v=_v23c_state_copy(raw)
        for _ in range(2):
            for i in bykey.get(key,()):
                ov=_v23c_inner(basis[i]['state'],v)
                if abs(ov)>1e-13: _v23c_state_add(v,basis[i]['state'],-ov)
        n2=_v23c_norm2(v)
        if n2<=V23C_GRAM_TOL: return None
        v=_v23c_state_scaled(v,1.0/_v23c_math.sqrt(n2))
        i=len(basis); basis.append({'state':v,'key':key,'layer':int(layer),'name':str(name)}); bykey[key].append(i)
        return i

    for j,s in enumerate(initial):
        blocks=_v23c_split_h0(s)
        if len(blocks)!=1: raise RuntimeError(f'P seed split into {len(blocks)} H0 blocks')
        key,blk=next(iter(blocks.items()))
        i=add_raw(blk,key,0,'vac' if vacuum else f'Pface{pfaces[j]}')
        if i is None: raise RuntimeError('lost independent P seed')
        p_indices.append(i)
    if p_indices!=list(range(len(p_indices))): raise RuntimeError('P ordering invariant failed')
    nP=len(p_indices)

    layer1=[]
    for j in range(nP):
        w=_v23c_applyW(basis[j]['state'],C)
        for key,blk in _v23c_split_h0(w).items():
            i=add_raw(blk,key,1,f'W(P{j})')
            if i is not None: layer1.append(i)
    layer2=[]
    for jj,j in enumerate(layer1):
        w=_v23c_applyW(basis[j]['state'],C)
        for key,blk in _v23c_split_h0(w).items():
            i=add_raw(blk,key,2,f'W(Q1{jj})')
            if i is not None: layer2.append(i)

    Eref=_V23CF(0,1) if vacuum else _V23CF(8,3)
    resonant=[i for i,b in enumerate(basis[nP:],start=nP) if b['key'][1]==Eref]
    if resonant: raise RuntimeError(f'finite cluster retained {len(resonant)} non-P resonances at E0={Eref}')

    nb=len(basis); H0=np.asarray([float(b['key'][1]) for b in basis],float); W=np.zeros((nb,nb),float)
    for j,b in enumerate(basis):
        wb=_v23c_applyW(b['state'],C); blocks=_v23c_split_h0(wb)
        for key,blk in blocks.items():
            for i in bykey.get(key,()): W[i,j]=_v23c_inner(basis[i]['state'],blk)
    herm=float(np.max(np.abs(W-W.T))) if nb else 0.0
    if herm>V23C_HERM_TOL: raise RuntimeError(f'finite-cluster W not Hermitian: {herm:.3e}, |C|={len(C)}, dim={nb}')
    W=0.5*(W+W.T)

    PG=np.zeros((nP,nP),float)
    for i in range(nP):
        for j in range(i,nP): PG[i,j]=PG[j,i]=_v23c_inner(basis[i]['state'],basis[j]['state'])
    perr=float(np.max(np.abs(PG-np.eye(nP))))
    if perr>2e-8: raise RuntimeError(f'finite-cluster P basis lost orthonormality: {perr:.3e}')
    return {'C':C,'vacuum':bool(vacuum),'pfaces':pfaces,'nP':nP,'basis':basis,'H0':H0,'W':W,'dim':nb,
            'layer1':len(layer1),'layer2':len(layer2),'herm':herm,'pgram_err':perr}

# -------------------------- des-Cloizeaux projection -------------------------
def _v23c_one_particle_heff(model,u):
    nP=int(model['nP']); H=np.diag(model['H0'])+float(u)*model['W']
    ew,U=_v23c_eigh(H,check_finite=False,overwrite_a=False)
    pweight=np.sum(U[:nP,:]**2,axis=0); sel=np.argsort(pweight)[-nP:]
    A=U[:nP,sel]; S=0.5*(A.T@A+(A.T@A).T); se,SV=np.linalg.eigh(S)
    if float(se[0])<0.20: raise RuntimeError(f'des-Cloizeaux P projection nearly singular: min={se[0]:.3e}, u={u}')
    Sinv=SV@np.diag(1.0/np.sqrt(se))@SV.T; Phi=A@Sinv
    orth=float(np.max(np.abs(Phi.T@Phi-np.eye(nP))))
    if orth>2e-8: raise RuntimeError(f'des-Cloizeaux projected vectors not orthonormal: {orth:.3e}')
    Heff=Phi@np.diag(ew[sel])@Phi.T; Heff=0.5*(Heff+Heff.T)
    return Heff,float(np.sum(pweight[sel])),float(se[0])

def _v23c_vac_energy(model,u):
    H=np.diag(model['H0'])+float(u)*model['W']; ew,U=_v23c_eigh(H,check_finite=False,overwrite_a=False)
    j=int(np.argmax(U[0,:]**2)); return float(ew[j]),float(U[0,j]**2)

def _v23c_cluster_gap_value(one,vac,u):
    Heff,pw,smin=_v23c_one_particle_heff(one,u); Ev,vw=_v23c_vac_energy(vac,u)
    root_i=one['pfaces'].index(V23C_ROOT); _,ra,rb=faces[V23C_ROOT]
    same=[i for i,f in enumerate(one['pfaces']) if tuple(faces[int(f)][1:])==(ra,rb)]
    return float(np.sum(Heff[root_i,same])-Ev),dict(pweight=pw,pSmin=smin,vweight=vw)

def _v23c_fit_cluster(C):
    one=_v23c_build_basis(C,False); vac=_v23c_build_basis(C,True)
    us=np.linspace(-V23C_FIT_UMAX,V23C_FIT_UMAX,V23C_FIT_N); ys=[]; qmin=1.0; vmin=1.0
    for u in us:
        y,st=_v23c_cluster_gap_value(one,vac,float(u)); ys.append(y); qmin=min(qmin,st['pSmin']); vmin=min(vmin,st['vweight'])
    ys=np.asarray(ys,float); p=_V23Poly.fit(us,ys,deg=V23C_FIT_DEG).convert()
    c=np.zeros(5,float); c[:min(5,len(p.coef))]=p.coef[:5]
    mask=np.abs(us)<=0.76*V23C_FIT_UMAX+1e-15; deg2=min(V23C_FIT_DEG,int(np.count_nonzero(mask))-2)
    p2=_V23Poly.fit(us[mask],ys[mask],deg=deg2).convert(); c2=np.zeros(5,float); c2[:min(5,len(p2.coef))]=p2.coef[:5]
    z0,_=_v23c_cluster_gap_value(one,vac,0.0)
    if abs(z0-8/3)>2e-9: raise RuntimeError(f'finite-cluster u=0 gap incorrect: {z0}')
    return {'coef':c,'coef_inner':c2,'fit_stability':float(abs(c[4]-c2[4])),'one_dim':one['dim'],'vac_dim':vac['dim'],
            'q1':one['layer1'],'q2':one['layer2'],'one_herm':one['herm'],'vac_herm':vac['herm'],'pSmin':qmin,'vweight':vmin}

# --------------------------- support candidate census ------------------------
def _v24c_candidate_supports(leftLD,rightLD,left_root,right_root,max_size=7):
    """Return concrete supports AND the translated left P endpoint.

    This is purely a support census: coefficients/Haar weights are ignored.
    Keeping the endpoint is essential for folded K2*N support composition,
    because the second two-W segment must be translated to the actual
    intermediate P plaquette rather than naively unioned at the original root.
    """
    RB=_v17_phys_index(rightLD)
    out=set()
    by_endpoint=_v23c_dd(set)
    tests=matches=0
    Litems=[]
    for SL,st in leftLD.items():
        for key,lv in _v10a3_physical_blocks(st).items():
            Litems.append((SL,key))
    t0=_v23c_time.time()
    for ii,(SL,(cs,Esg)) in enumerate(Litems):
        for dv in verts:
            tests+=1
            tcs=_v10a2_sig_canon(_v10a3_translate_sig(cs,dv))
            cand=RB.get((tcs,Esg),())
            if not cand:
                continue
            tSL=_v17_translate_support(SL,dv)
            endpoint=int(_v17_translate_face(int(left_root),tuple(dv)))
            # Endpoint must preserve the left-root plaquette orientation.
            if tuple(faces[endpoint][1:]) != tuple(faces[int(left_root)][1:]):
                raise RuntimeError("support census translation changed endpoint polarization")
            for SR,_ in cand:
                matches+=1
                C=frozenset(set(tSL)|set(SR))
                if int(right_root) not in C:
                    raise RuntimeError("support census lost the anchored ket root")
                if len(C)<=int(max_size) and _v17_connected(C):
                    out.add(C)
                    by_endpoint[endpoint].add(C)
        if V23C_PROGRESS and len(Litems)>200 and (ii+1)%max(1,len(Litems)//5)==0:
            print(f'  support scan {ii+1:,}/{len(Litems):,}; matches={matches:,}; '
                  f'supports={len(out):,}; endpoints={len(by_endpoint):,}; '
                  f'elapsed={_v23c_time.time()-t0:.1f}s')
    return out,{k:set(v) for k,v in by_endpoint.items()},dict(
        blocks=len(Litems),tests=tests,matches=matches,
        supports=len(out),endpoints=len(by_endpoint)
    )


def _v24c_face_translation(f_from,f_to):
    """Lattice translation sending f_from to f_to; orientations must agree."""
    a=faces[int(f_from)]
    b=faces[int(f_to)]
    if tuple(a[1:]) != tuple(b[1:]):
        raise RuntimeError(
            f"cannot translate between different plaquette orientations: {a} -> {b}"
        )
    return tuple((int(b[0][i])-int(a[0][i]))%int(L) for i in range(3))


def _v24c_compose_second_order_supports(seg_by_pair, root_pol):
    """Geometry of the folded {K2,N}/2 term on the diagonal T1 block.

    seg_by_pair[(bra_pol,ket_pol)] is an endpoint-resolved two-W support
    corpus anchored at ket_pol.  For each intermediate polarization b and
    concrete intermediate plaquette y:

        root(a) --two W--> y(b) --two W--> final(a)

    the second segment is translated so its ket anchor b coincides with y.
    This captures cross-polarization intermediate P states and allows the
    true maximal marked support size 7 (= initial + intermediate + final
    P faces + four action faces) instead of the old unsafe <=6 cap.
    """
    a0=int(root_pol)
    out=set()
    composed=0
    size_hist=_v23c_Counter()
    for b in range(3):
        first_map=seg_by_pair[(b,a0)][1]   # endpoint b, ket anchor a0
        second_all=seg_by_pair[(a0,b)][0] # bra a0, ket anchor b
        ket_b=int(anchor_faces[b])
        for y,first_supports in first_map.items():
            dv=_v24c_face_translation(ket_b,int(y))
            second_shifted=[
                _v17_translate_support(S,tuple(dv)) for S in second_all
            ]
            for A in first_supports:
                for Bt in second_shifted:
                    composed+=1
                    U=frozenset(set(A)|set(Bt))
                    if V23C_ROOT not in U:
                        raise RuntimeError("fold support composition lost marked root")
                    if len(U)<=7 and _v17_connected(U):
                        out.add(U)
                        size_hist[len(U)]+=1
    return out,dict(composed_pairs=composed,size_hist=dict(sorted(size_hist.items())))

def _v23c_rooted_connected_subsets(C):
    C=frozenset(map(int,C))
    if V23C_ROOT not in C: return ()
    rest=tuple(sorted(set(C)-{V23C_ROOT})); out=[]
    for mask in range(1<<len(rest)):
        S={V23C_ROOT}
        for i,f in enumerate(rest):
            if (mask>>i)&1: S.add(f)
        F=frozenset(S)
        if _v17_connected(F): out.append(F)
    return tuple(out)

# ------------------------- cubic rooted-shape cache --------------------------
def _v23c_centered_delta(x,x0):
    d=(int(x)-int(x0))%int(L)
    if d>int(L)//2: d-=int(L)//1
    return d

def _v23c_face_rep(f):
    v,a,b=faces[int(f)]; vr=faces[V23C_ROOT][0]
    base=tuple(_v23c_centered_delta(v[i],vr[i]) for i in range(3)); return (base,tuple(sorted((int(a),int(b)))))

def _v23c_face_vertices(rep):
    base,ab=rep; a,b=ab; e1=[0,0,0];e2=[0,0,0];e1[a]=1;e2[b]=1; out=[]
    for s,t in ((0,0),(1,0),(0,1),(1,1)): out.append(tuple(base[i]+s*e1[i]+t*e2[i] for i in range(3)))
    return out

def _v24c_perm_sign(perm):
    inv=sum(int(perm[i])>int(perm[j]) for i in range(3) for j in range(i+1,3))
    return -1 if inv%2 else +1

# Use only proper cubic rotations.  This is sufficient for symmetry reduction
# and avoids importing any parity/pseudovector convention into the cache key.
_V24C_TRANSFORMS=[]
for perm in _v23c_it.permutations(range(3)):
    ps=_v24c_perm_sign(perm)
    for signs in _v23c_it.product((-1,1),repeat=3):
        det=ps*int(signs[0])*int(signs[1])*int(signs[2])
        if det==+1:
            _V24C_TRANSFORMS.append((perm,signs))
if len(_V24C_TRANSFORMS)!=24:
    raise RuntimeError(f"expected 24 proper cubic rotations, got {len(_V24C_TRANSFORMS)}")

def _v23c_transform_vertex(x,T):
    perm,signs=T
    return tuple(int(signs[j])*int(x[perm[j]]) for j in range(3))

def _v23c_transform_face(rep,T):
    vv=[_v23c_transform_vertex(x,T) for x in _v23c_face_vertices(rep)]
    lo=tuple(min(x[i] for x in vv) for i in range(3))
    hi=tuple(max(x[i] for x in vv) for i in range(3))
    axes=tuple(i for i in range(3) if hi[i]-lo[i]==1)
    if len(axes)!=2 or any(hi[i]-lo[i] not in (0,1) for i in range(3)):
        raise RuntimeError('cubic face transform failed')
    return (lo,axes)

def _v23c_shift_rep(rep,d):
    b,ab=rep
    return (tuple(int(b[i])+int(d[i]) for i in range(3)),ab)

def _v24c_shape_key(C):
    """Canonical ROOTED cluster key.

    The old v10a.23 key stored only the transformed unmarked face set.
    If several faces share the root base vertex, it could identify two
    inequivalent choices of marked root.  Here the transformed root face is
    a separate field of the key, so root->root is mandatory.
    """
    C=frozenset(map(int,C))
    if V23C_ROOT not in C:
        raise RuntimeError("rooted shape key called on an unrooted cluster")
    rrep=_v23c_face_rep(V23C_ROOT)
    others=[_v23c_face_rep(f) for f in C if int(f)!=V23C_ROOT]
    keys=[]
    for T in _V24C_TRANSFORMS:
        rr=_v23c_transform_face(rrep,T)
        sh=tuple(-int(x) for x in rr[0])
        rooted=_v23c_shift_rep(rr,sh)
        zz=tuple(sorted(
            _v23c_shift_rep(_v23c_transform_face(r,T),sh)
            for r in others
        ))
        keys.append((rooted,zz))
    return min(keys)


def _v24c_old_unrooted_shape_key(C):
    """Diagnostic only: exact v10a.23 cache key, never used for physics."""
    reps=[_v23c_face_rep(f) for f in C]
    rrep=_v23c_face_rep(V23C_ROOT)
    keys=[]
    # use all 48 transforms to reproduce the old implementation exactly
    for perm in _v23c_it.permutations(range(3)):
        for signs in _v23c_it.product((-1,1),repeat=3):
            T=(perm,signs)
            rr=_v23c_transform_face(rrep,T)
            sh=tuple(-int(x) for x in rr[0])
            zz=tuple(sorted(
                _v23c_shift_rep(_v23c_transform_face(r,T),sh) for r in reps
            ))
            keys.append(zz)
    return min(keys)


def _v24c_root_cache_regression():
    """Geometry-only proof that the v10a.23 unrooted cache was unsafe.

    Enumerate every rooted connected cluster through size four.  Count old
    cache keys that contain more than one genuinely rooted proper-rotation key.
    This test is independent of all Haar/Feshbach numerics.
    """
    levels={1:{frozenset((V23C_ROOT,))}}
    for k in (2,3,4):
        nxt=set()
        for S in levels[k-1]:
            front=set()
            for f in S:
                front.update(_V17_NEIGH[int(f)])
            for g in front-set(S):
                T=frozenset(set(S)|{int(g)})
                if len(T)==k and _v17_connected(T):
                    nxt.add(T)
        levels[k]=nxt
    groups=_v23c_dd(set)
    for C in levels[4]:
        groups[_v24c_old_unrooted_shape_key(C)].add(_v24c_shape_key(C))
    unsafe=sum(len(v)>1 for v in groups.values())
    return unsafe,len(levels[4]),len(groups),len({_v24c_shape_key(C) for C in levels[4]})

# ------------------------------- production ---------------------------------
print('\n[14] INDEPENDENT FOUR-W SUPPORT CENSUS — ROOTED/FULL-T1 CORRECTED')

unsafe_old,n4,old4,new4=_v24c_root_cache_regression()
gate('v10a.24 geometry regression detects the old unrooted shape-cache collision',
     unsafe_old>0,
     f'unsafe old size-4 keys={unsafe_old}; concrete={n4}; old classes={old4}; rooted proper-rotation classes={new4}')

# Direct irreducible fourth-order paths on the marked diagonal polarization.
DMAX,DMAP,DSTATC=_v24c_candidate_supports(
    W2Ls[V23C_POL],W2Ls[V23C_POL],
    anchor_faces[V23C_POL],anchor_faces[V23C_POL],max_size=6
)
CLEFT,CLMAP,CLSTAT=_v24c_candidate_supports(
    W1Ls[V23C_POL],W2Ls[V23C_POL],
    anchor_faces[V23C_POL],anchor_faces[V23C_POL],max_size=6
)
CRIGHT,CRMAP,CRSTAT=_v24c_candidate_supports(
    W2Ls[V23C_POL],W1Ls[V23C_POL],
    anchor_faces[V23C_POL],anchor_faces[V23C_POL],max_size=6
)
CMAX=set(CLEFT)|set(CRIGHT)

# Every two-W model-space segment for all 3x3 T1 polarization pairs.
SEG={}
for b in range(3):
    for a in range(3):
        S,MP,ST=_v24c_candidate_supports(
            W1Ls[b],W1Ls[a],
            anchor_faces[b],anchor_faces[a],max_size=4
        )
        SEG[(b,a)]=(S,MP,ST)
        print(f'  two-W segment bra{b}<-ket{a}: supports={len(S):,}, endpoints={len(MP):,}')

# Same-polarization two-W supports cover J/lower-order geometry.
EMAX=set(SEG[(V23C_POL,V23C_POL)][0])

# Folded normalization support is an OPERATOR CONVOLUTION through every
# intermediate position and polarization, not a union of two root-anchored
# same-polarization sets.
FMAX,FSTAT=_v24c_compose_second_order_supports(SEG,V23C_POL)
print('  folded support composition:',FSTAT)
fold_max=max(map(len,FMAX),default=0)
gate('v10a.24 folded support census allows the full marked O4 support size through 7',
     fold_max<=7,
     f'folded maximal support={fold_max}, supports={len(FMAX):,}')

MAXC=set(DMAX)|set(CMAX)|set(EMAX)|set(FMAX)

# Explicitly include every rooted connected cluster through size 3 so the
# m1/m2/m3 gates do not depend on an O4 H0-match census.
small_levels={1:{frozenset((V23C_ROOT,))}}
for k in (2,3):
    nxt=set()
    for S in small_levels[k-1]:
        front=set()
        for f in S:
            front.update(_V17_NEIGH[int(f)])
        for g in front-set(S):
            T=frozenset(set(S)|{int(g)})
            if len(T)==k and _v17_connected(T):
                nxt.add(T)
    small_levels[k]=nxt
MAXC.update(small_levels[3])

CLUST=set()
for C in MAXC:
    CLUST.update(_v23c_rooted_connected_subsets(C))
CLUST=sorted(CLUST,key=lambda S:(len(S),tuple(sorted(S))))
CLSET=set(CLUST)

badclose=[]
for C in CLUST:
    for S in _v23c_rooted_connected_subsets(C):
        if S not in CLSET:
            badclose.append((C,S))
            break
    if badclose:
        break
gate('v10a.24 independent cluster poset is downward closed',
     not badclose,
     f'clusters={len(CLUST):,}, maximal={len(MAXC):,}')

sizecount=_v23c_Counter(map(len,CLUST))
shapekeys={_v24c_shape_key(C) for C in CLUST}
print('  concrete rooted clusters      =',len(CLUST),dict(sorted(sizecount.items())))
print('  ROOTED proper-rotation classes=',len(shapekeys))
print('  max direct/fold supports      =',
      max(map(len,DMAX),default=0),
      max(map(len,CMAX),default=0),
      max(map(len,FMAX),default=0))

print('\n[15] INDEPENDENT RESTRICTED-HAMILTONIAN COEFFICIENTS')
shape_cache={}; shape_rep={}; duplicate_checks=0; max_fit_stab=0.0; raw={}; t0=_v23c_time.time()
for ci,C in enumerate(CLUST,1):
    key=_v24c_shape_key(C)
    if key not in shape_cache:
        z=_v23c_fit_cluster(C); shape_cache[key]=z; shape_rep[key]=C; max_fit_stab=max(max_fit_stab,z['fit_stability'])
        if V23C_PROGRESS:
            cc=z['coef']; print(f'  shape {len(shape_cache):4d}/{len(shapekeys):4d} |C|={len(C)} dim={z["one_dim"]}/{z["vac_dim"]} '
                  f'q1/q2={z["q1"]}/{z["q2"]} c2={cc[2]:+.9g} c3={cc[3]:+.9g} c4={cc[4]:+.9g} '
                  f'fitΔ4={z["fit_stability"]:.2e} elapsed={_v23c_time.time()-t0:.1f}s',flush=True)
    elif duplicate_checks<V23C_SYM_CHECKS and C!=shape_rep[key]:
        z2=_v23c_fit_cluster(C); z1=shape_cache[key]; err=float(np.max(np.abs(z2['coef'][:5]-z1['coef'][:5])))
        gate(f'v10a.23 cubic-shape duplicate raw coefficients agree #{duplicate_checks+1}',err<2e-5,f'maxerr={err:.3e}'); duplicate_checks+=1
    raw[C]=shape_cache[key]['coef'].copy()
gate('v10a.23 finite-cluster u4 fit window is numerically stable',max_fit_stab<V23C_FIT_STAB_TOL,
     f'max |c4(full)-c4(inner)|={max_fit_stab:.3e}')

print('\n[16] ROOTED INCIDENCE TRANSFORM — INDEPENDENT RAW CLUSTERS')
omega={}; totals=np.zeros(5,float); bysize=_v23c_dd(lambda:np.zeros(5,float))
for C in CLUST:
    x=raw[C].copy()
    for S in _v23c_rooted_connected_subsets(C):
        if S!=C: x-=omega[S]
    omega[C]=x; totals+=x; bysize[len(C)]+=x
for k in sorted(bysize):
    x=bysize[k]; print(f'  size {k}: c1={x[1]:+.12g} c2={x[2]:+.12g} c3={x[3]:+.12g} c4={x[4]:+.12g}')
print('  TOTAL m1/m2/m3/m4 =',totals[1],totals[2],totals[3],totals[4])

gate('v10a.23 independent finite-cluster oracle recovers m1=1',abs(totals[1]-1.0)<2e-5,totals[1])
gate('v10a.23 independent finite-cluster oracle recovers m2=11/306',abs(totals[2]-float(_V23CF(11,306)))<2e-4,totals[2])
gate('v10a.23 independent finite-cluster oracle recovers m3=-109151/249696',abs(totals[3]-float(_V23CF(-109151,249696)))<8e-4,totals[3])

# Every gate from the new v10a.23 layers must pass before disputed values enter memory.
g23=gates[V23_GATE_START:]
if not all(ok for _,ok,_ in g23):
    print('\n'+'='*148); print('V10A.23 STOPPED BEFORE FOURTH-ORDER UNBLIND'); print('='*148)
    for i,(n,ok,d) in enumerate(g23,1): print(f'{i:02d}. {"PASS" if ok else "FAIL"} — {n}'+(f' :: {d}' if d else ''))
    raise AssertionError('v10a.23 pre-unblind gate failure; no fourth-order verdict permitted')

# =============================================================================
# 17. FINAL UNBLIND — disputed constants first appear here
# =============================================================================
print('\n[17] FINAL FOURTH-ORDER UNBLIND')
M4_ORACLE=float(totals[4])
M4_SHORTCUT=_V23CF(-160506019419340168451,14501180577204921600)
Q3_OLD=_V23CF(-20721577909065127111,7250590288602460800)
C3_OLD=_V23CF(-211835444920651,4405310420659200)

dnew=abs(M4_ORACLE-float(M4_SHORTCUT)); dold=abs(M4_ORACLE-float(Q3_OLD))
C_COLD=float(V23_AXIAL_SHAPE['C_direct']); dcold=abs(C_COLD-float(C3_OLD))
print('  independent linked m4         =',repr(M4_ORACLE))
print('  quarantined scalar shortcut   =',M4_SHORTCUT,'=',repr(float(M4_SHORTCUT)),' |Δ|=',dnew)
print('  historical 189-kernel q3      =',Q3_OLD,'=',repr(float(Q3_OLD)),' |Δ|=',dold)
print('  cold folded C_shape           =',repr(C_COLD))
print('  historical C_shape            =',C3_OLD,'=',repr(float(C3_OLD)),' |Δ|=',dcold)

# Convert the independently linked rest scalar into the physical mass kernel by
# a translation-local scalar shift.  Vacuum subtraction cannot change dispersion.
ax_rest=float(V23_AXIAL_SHAPE['rest_direct']); local_shift=M4_ORACLE-ax_rest
K4_mass_cols=V23_AXIAL_H4_COLS.copy()
for a,f in enumerate(anchor_faces): K4_mass_cols[int(f),a]+=local_shift
mass_shape=_v10a3_extract_shape(K4_mass_cols)
record_count=int(np.count_nonzero(np.abs(K4_mass_cols)>V23_RECORD_TOL))
print('  independently linked local shift=',repr(local_shift))
print('  final mass-kernel anchored records=',record_count)
print('  final mass-kernel shape:')
for k in ('rest_direct','A','B','C_direct','D','alpha','fifth_residual_max','hermiticity_error','gamma_spread'):
    print(f'    {k:22s} = {mass_shape[k]:+.15g}')

gate('v10a.23 final physical mass-kernel Gamma rest equals independent cluster oracle',abs(mass_shape['rest_direct']-M4_ORACLE)<2e-6,
     abs(mass_shape['rest_direct']-M4_ORACLE))
gate('v10a.23 final physical kernel has canonical 189 nonzero anchored records',record_count==189,record_count)

if dnew < dold/5.0: scalar_verdict='SCALAR ORACLE SUPPORTS v10a.20 SHORTCUT'
elif dold < dnew/5.0: scalar_verdict='SCALAR ORACLE SUPPORTS HISTORICAL q3'
else: scalar_verdict='SCALAR ORACLE RETURNS THIRD VALUE'
if dcold<2e-4: shape_verdict='FOLDED MATRIX SUPPORTS HISTORICAL C_shape'
else: shape_verdict='FOLDED MATRIX DOES NOT RECOVER HISTORICAL C_shape'

if scalar_verdict.endswith('HISTORICAL q3') and shape_verdict.startswith('FOLDED MATRIX SUPPORTS') and record_count==189:
    VERDICT='DUAL COLD ORACLES SUPPORT THE HISTORICAL 189-RECORD SU(3) O4 KERNEL'
elif scalar_verdict.endswith('v10a.20 SHORTCUT') and not shape_verdict.startswith('FOLDED MATRIX SUPPORTS'):
    VERDICT='DUAL COLD ORACLES SUPPORT THE MODERN SHORTCUT BRANCH'
else:
    VERDICT='MIXED/THIRD RESULT — DO NOT PROMOTE EITHER FOURTH-ORDER CLAIM'

print('\n  SCALAR VERDICT:',scalar_verdict)
print('  SHAPE VERDICT :',shape_verdict)
print('  FINAL VERDICT :',VERDICT)

print('\n'+'='*148)
print('FINAL v10a.23 GATE SUMMARY')
print('='*148)
g23=gates[V23_GATE_START:]
for i,(n,ok,d) in enumerate(g23,1): print(f'{i:02d}. {"PASS" if ok else "FAIL"} — {n}'+(f' :: {d}' if d else ''))
print('-'*148)
print(f'PASSED {sum(ok for _,ok,_ in g23)}/{len(g23)} v10a.23 GATES')
print('finite-cluster shape classes:',len(shape_cache),' concrete clusters:',len(CLUST))
print('independent linked m4       :',repr(M4_ORACLE))
print('folded C_shape              :',repr(C_COLD))
print('189-record count            :',record_count)
print('FINAL VERDICT               :',VERDICT)

if not all(ok for _,ok,_ in g23):
    raise AssertionError('v10a.23 post-unblind structural gate failure; verdict above is diagnostic only')
