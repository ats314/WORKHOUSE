"""
HODGE v10a.27 -- order-generic m5/m6/m7 frontier extension
=======================================================================

Run this file in the SAME Python/Colab namespace after the completed v10a.26
cell.  It deliberately contains no Hamer coefficients and performs no target
comparison.  Its jobs are:

  1. generalize the finite-cluster Krylov construction to arbitrary depth;
  2. certify factorized SU(3) Haar projectors through a requested local
     occurrence cap (nine for the Q3 frontier);
  3. generate an order-n support census from unrestricted, bidirectional
     magnetic histories, including paths that revisit P;
  4. regress that generic census against the completed O(u^4) support corpus;
  5. extract rooted linked coefficients with canonical Hermitian SW/BCH.

The default mode is PREFLIGHT.  Production requires V27_MODE=production.
There is no watchdog and every completed rooted shape is checkpointed.

Important: this is frontier code.  A production result is printed only after
all support, finite-volume, Haar, Hermiticity, and SW gates pass.  An unsupported
or ambiguous case raises before any coefficient is promoted.
"""

from __future__ import annotations

import hashlib
import itertools
import math
import os
import pickle
import time
from collections import Counter, defaultdict
from functools import lru_cache

import numpy as np
import sympy as sp


V27_SCHEMA = "hodge-v10a27-order-generic-rooted-krylov-haar9-v1"
V27_ORDER = int(os.environ.get("V27_ORDER", "5"))
V27_MODE = os.environ.get("V27_MODE", "preflight").strip().lower()
V27_HAAR_CAP = int(os.environ.get("V27_HAAR_CAP", "7" if V27_ORDER == 5 else "9"))
V27_PROGRESS = int(os.environ.get("V27_PROGRESS", "1"))
V27_HEARTBEAT = float(os.environ.get("V27_HEARTBEAT", "20"))
V27_RESUME = int(os.environ.get("V27_RESUME", "1"))
V27_CHECKPOINT = os.environ.get(
    "V27_CHECKPOINT", f"/content/hodge_v10a27_m{V27_ORDER}_shapes.pkl"
)
V27_GRAM_TOL = float(os.environ.get("V27_GRAM_TOL", "2e-10"))
V27_HERM_TOL = float(os.environ.get("V27_HERM_TOL", "2e-8"))
V27_SW_TOL = float(os.environ.get("V27_SW_TOL", "2e-10"))
V27_DUPLICATE_CHECKS = int(os.environ.get("V27_DUPLICATE_CHECKS", "4"))

if V27_ORDER not in (4, 5, 6, 7):
    raise ValueError("V27_ORDER must be 4, 5, 6, or 7")
if V27_MODE not in ("preflight", "production"):
    raise ValueError("V27_MODE must be 'preflight' or 'production'")

V27_KRYLOV_DEPTH = V27_ORDER // 2
V27_SUPPORT_HALF_DEPTH = (V27_ORDER + 1) // 2
V27_MARKED_SUPPORT_BOUND = V27_ORDER + 2


_REQUIRED_GLOBALS = (
    "L", "N", "faces", "verts", "T1_POLS", "anchor_faces", "V23C_ROOT",
    "V23C_POL", "_FAST_EPS", "oe", "LXState", "_V17_VAC",
    "_v17_apply_W_faces", "_v17_apply_W_labeled", "_v17_connected",
    "_v17_phys_index", "_v17_translate_support", "_v17_translate_face",
    "_v23c_split_h0", "_v23c_rooted_connected_subsets", "_v24c_shape_key",
    "_v24c_candidate_supports", "_v10a3_face_state", "_v10a3_h0_state_inner",
    "_joint_canon_states", "lx_combine_bra_ket", "_v26_sw_blocks",
    "_v23_sw_exact", "_v23_sp", "_v23_random", "_V23CF",
    "_v26_singlet_multiplicity", "_V17_NEIGH", "_v23c_fit_cluster",
)
_missing = [name for name in _REQUIRED_GLOBALS if name not in globals()]
if _missing:
    raise RuntimeError(
        "v10a.27 must run after the completed v10a.26 cell; missing symbols: "
        + ", ".join(_missing)
    )


V27_GATES = []


def v27_gate(name, ok, detail=""):
    ok = bool(ok)
    V27_GATES.append((str(name), ok, str(detail)))
    print(("[PASS] " if ok else "[FAIL] ") + str(name) + (f" :: {detail}" if detail != "" else ""))
    return ok


print("=" * 148)
print(f"HODGE v10a.27 -- ROOTED ORDER-{V27_ORDER} FRONTIER")
print("=" * 148)
print("mode                         :", V27_MODE)
print("target coefficient           : NOT LOADED")
print("Krylov closure depth         :", V27_KRYLOV_DEPTH)
print("support half-history depth   :", V27_SUPPORT_HALF_DEPTH)
print("marked-support safe bound    :", V27_MARKED_SUPPORT_BOUND)
print("certified local Haar cap     :", V27_HAAR_CAP)
print("watchdog                     : NONE")


# ---------------------------------------------------------------------------
# 1. Exact invariant-basis Haar projectors through local occurrence cap nine
# ---------------------------------------------------------------------------


def _v27_triple_partitions(items):
    """Canonical partitions of distinct labels into unordered triples."""
    items = tuple(sorted(map(int, items)))
    if not items:
        yield ()
        return
    if len(items) % 3:
        return
    first = items[0]
    rest = items[1:]
    for pair in itertools.combinations(rest, 2):
        triple = (first,) + tuple(pair)
        remain = tuple(x for x in rest if x not in pair)
        for tail in _v27_triple_partitions(remain):
            yield (triple,) + tail


def _v27_invariant_specs(nmajor, nminor):
    """Delta/epsilon spanning family for Inv(3^nmajor x 3bar^nminor)."""
    nmajor, nminor = int(nmajor), int(nminor)
    if nmajor < nminor or (nmajor - nminor) % 3:
        return ()
    specs = []
    for targets in itertools.permutations(range(nmajor), nminor):
        used = set(targets)
        remainder = tuple(i for i in range(nmajor) if i not in used)
        for triples in _v27_triple_partitions(remainder):
            deltas = tuple((int(targets[j]), nmajor + j) for j in range(nminor))
            specs.append((deltas, tuple(tuple(map(int, t)) for t in triples)))
    return tuple(specs)


def _v27_greedy_gram_basis(G, expected_rank, tol=1e-9):
    """Deterministically select independent invariant tensors from their Gram matrix."""
    G = np.asarray(G, dtype=np.float64)
    keep = []
    for i in range(G.shape[0]):
        if not keep:
            residual = G[i, i]
        else:
            K = G[np.ix_(keep, keep)]
            g = G[np.ix_(keep, [i])][:, 0]
            residual = G[i, i] - float(g @ np.linalg.solve(K, g))
        if residual > tol:
            keep.append(i)
            if len(keep) == int(expected_rank):
                break
    return tuple(keep)


@lru_cache(maxsize=None)
def _v27_projector_data(nfund, nanti):
    """Return a certified factor I C I for a center-admissible SU(3) Haar integral."""
    nfund, nanti = int(nfund), int(nanti)
    if (nfund - nanti) % 3:
        raise ValueError("center-forbidden Haar pattern")
    nmajor, nminor = max(nfund, nanti), min(nfund, nanti)
    m = nmajor + nminor
    specs = _v27_invariant_specs(nmajor, nminor)
    expected = int(_v26_singlet_multiplicity(nmajor, nminor))
    if not specs or expected <= 0:
        raise RuntimeError(f"no invariant spanning family for {(nfund, nanti)}")

    grid = np.indices((3,) * m, dtype=np.int8)
    raw = []
    for deltas, triples in specs:
        arr = np.ones((3,) * m, dtype=np.int8)
        for a, b in deltas:
            arr = arr * (grid[a] == grid[b])
        for a, b, c in triples:
            arr = arr * _FAST_EPS[grid[a], grid[b], grid[c]]
        raw.append(arr.reshape(-1))
    R = np.stack(raw, axis=0)
    RF = np.asarray(R, dtype=np.float64)
    Graw = np.rint(RF @ RF.T).astype(np.int64)
    keep = _v27_greedy_gram_basis(Graw, expected)
    if len(keep) != expected:
        raise RuntimeError(
            f"invariant rank failure for {(nfund, nanti)}: selected {len(keep)}, expected {expected}"
        )
    G = Graw[np.ix_(keep, keep)]
    Gsp = sp.Matrix(G.tolist())
    if int(Gsp.rank()) != expected:
        raise RuntimeError(f"exact selected Gram rank failure for {(nfund, nanti)}")
    C = np.asarray(Gsp.inv().tolist(), dtype=np.float64)
    I = R[np.asarray(keep, dtype=int)].reshape((expected,) + (3,) * m).astype(np.float64)

    cross = Graw[:, np.asarray(keep, dtype=int)].astype(np.float64)
    span = cross @ C @ cross.T
    scale = max(1.0, float(np.max(np.abs(Graw))))
    cert = dict(
        pattern=(nfund, nanti),
        raw_count=len(specs),
        selected_rank=len(keep),
        representation_singlets=expected,
        gram_inverse_error=float(np.max(np.abs(C @ G - np.eye(expected)))),
        raw_span_error=float(np.max(np.abs(span - Graw)) / scale),
        coefficient_symmetry_error=float(np.max(np.abs(C - C.T))),
        selected_indices=keep,
    )
    if max(cert["gram_inverse_error"], cert["raw_span_error"], cert["coefficient_symmetry_error"]) > 2e-9:
        raise RuntimeError(f"Haar projector certificate failed for {(nfund, nanti)}: {cert}")
    return I, C, cert


V27_ADMISSIBLE_PATTERNS = tuple(
    (a, b)
    for total in range(1, V27_HAAR_CAP + 1)
    for a in range(total + 1)
    for b in (total - a,)
    if (a - b) % 3 == 0
)


def _v27_certify_haar_cap():
    reports = []
    seen = set()
    for a, b in V27_ADMISSIBLE_PATTERNS:
        key = (max(a, b), min(a, b))
        if key in seen:
            continue
        seen.add(key)
        _, _, cert = _v27_projector_data(a, b)
        reports.append(cert)
        print(
            f"  Haar {a},{b}: raw={cert['raw_count']} rank={cert['selected_rank']} "
            f"span={cert['raw_span_error']:.2e} inv={cert['gram_inverse_error']:.2e}"
        )
    return reports


@lru_cache(maxsize=1_000_000)
def _v27_factor_haar_canon(a, b):
    occ, part = lx_combine_bra_ket(a, b)
    by = defaultdict(lambda: {True: [], False: []})
    for i, (link, typ) in enumerate(occ):
        by[int(link)][bool(typ)].append(i)
    args = []
    aux = (max(part) + 1) if part else 0
    for group in by.values():
        U, B = group[True], group[False]
        pat = (len(U), len(B))
        if (pat[0] - pat[1]) % 3:
            return 0.0
        if sum(pat) > V27_HAAR_CAP:
            raise RuntimeError(
                f"local Haar occurrence {pat} exceeds certified cap {V27_HAAR_CAP}; "
                "increase the cap only after a support census"
            )
        if pat not in V27_ADMISSIBLE_PATTERNS:
            raise RuntimeError(f"uncertified center-admissible Haar pattern {pat}")
        I, C, _ = _v27_projector_data(*pat)
        items = (U + B) if len(U) >= len(B) else (B + U)
        row = [int(part[2 * p]) for p in items]
        col = [int(part[2 * p + 1]) for p in items]
        ar, ac = aux, aux + 1
        aux += 2
        args.extend((I, [ar] + row, C, [ar, ac], I, [ac] + col))
    if not args:
        return float(N ** len(set(part)))
    return float(oe.contract(*args, [], optimize="greedy", memory_limit="max_input"))


def _v27_cluster_haar(a, b):
    aa, bb = _joint_canon_states(a, b)
    ka, kb = (aa.occ, aa.part), (bb.occ, bb.part)
    if kb < ka:
        aa, bb = bb, aa
    return _v27_factor_haar_canon(aa, bb)


print("\n[1] FACTORIZED SU(3) HAAR CERTIFICATE")
V27_HAAR_REPORTS = _v27_certify_haar_cap()
v27_gate(
    "every center-admissible local pattern through requested cap is certified",
    len(V27_ADMISSIBLE_PATTERNS) > 0
    and all(
        r["selected_rank"] == r["representation_singlets"]
        and r["gram_inverse_error"] < 2e-9
        and r["raw_span_error"] < 2e-9
        for r in V27_HAAR_REPORTS
    ),
    f"cap={V27_HAAR_CAP}, patterns={V27_ADMISSIBLE_PATTERNS}",
)


# ---------------------------------------------------------------------------
# 2. Order-generic physical Krylov basis
# ---------------------------------------------------------------------------


def _v27_state_copy(a):
    return {sig: dict(v) for sig, v in a.items()}


def _v27_state_add(dst, src, scale=1.0):
    for sig, vec in src.items():
        d = dst.setdefault(sig, {})
        for st, x in vec.items():
            d[st] = d.get(st, 0.0) + float(scale) * float(x)


def _v27_state_scaled(a, scale):
    return {sig: {st: float(scale) * float(x) for st, x in v.items()} for sig, v in a.items()}


def _v27_inner(a, b):
    return float(_v10a3_h0_state_inner(a, b, _v27_cluster_haar)[0])


def _v27_norm2(a):
    x = _v27_inner(a, a)
    if x < -5e-9:
        raise RuntimeError(f"negative Haar norm in v10a.27 basis: {x:.3e}")
    return max(0.0, x)


def _v27_build_basis(C, vacuum=False, max_layer=None):
    C = frozenset(map(int, C))
    if not C:
        raise ValueError("empty finite cluster")
    if max_layer is None:
        max_layer = V27_KRYLOV_DEPTH
    max_layer = int(max_layer)
    t0, last = time.time(), time.time()
    pfaces = tuple(sorted(C)) if not vacuum else ()
    initial = [_v27_state_copy(_V17_VAC)] if vacuum else [
        _v27_state_copy(_v10a3_face_state(f)) for f in pfaces
    ]
    basis, bykey, p_indices = [], defaultdict(list), []

    def add_raw(raw, key, layer, name):
        v = _v27_state_copy(raw)
        for _ in range(2):
            for i in bykey.get(key, ()):
                ov = _v27_inner(basis[i]["state"], v)
                if abs(ov) > 1e-13:
                    _v27_state_add(v, basis[i]["state"], -ov)
        n2 = _v27_norm2(v)
        if n2 <= V27_GRAM_TOL:
            return None
        v = _v27_state_scaled(v, 1.0 / math.sqrt(n2))
        i = len(basis)
        basis.append(dict(state=v, key=key, layer=int(layer), name=str(name)))
        bykey[key].append(i)
        return i

    for j, state in enumerate(initial):
        blocks = _v23c_split_h0(state)
        if len(blocks) != 1:
            raise RuntimeError(f"P seed split into {len(blocks)} H0 blocks")
        key, block = next(iter(blocks.items()))
        i = add_raw(block, key, 0, "vac" if vacuum else f"Pface{pfaces[j]}")
        if i is None:
            raise RuntimeError("lost independent P seed")
        p_indices.append(i)
    nP = len(p_indices)
    layers = [list(range(nP))]

    for depth in range(1, max_layer + 1):
        new_layer = []
        parents = layers[depth - 1]
        for jj, j in enumerate(parents):
            w = _v17_apply_W_faces(basis[j]["state"], C)[0]
            for key, block in _v23c_split_h0(w).items():
                i = add_raw(block, key, depth, f"W(Q{depth-1}:{jj})")
                if i is not None:
                    new_layer.append(i)
            now = time.time()
            if V27_PROGRESS and (now - last >= V27_HEARTBEAT or jj + 1 == len(parents)):
                print(
                    f"      Q{depth} {jj+1:,}/{len(parents):,}; dim={len(basis):,}; "
                    f"Haar-cache={_v27_factor_haar_canon.cache_info()}; elapsed={now-t0:.1f}s",
                    flush=True,
                )
                last = now
        layers.append(new_layer)

    Eref = _V23CF(0, 1) if vacuum else _V23CF(8, 3)
    resonant = [
        i for i, item in enumerate(basis[nP:], start=nP) if item["key"][1] == Eref
    ]
    if resonant:
        raise RuntimeError(f"retained {len(resonant)} non-P resonances at E0={Eref}")

    nb = len(basis)
    H0 = np.asarray([float(item["key"][1]) for item in basis], dtype=np.float64)
    W = np.zeros((nb, nb), dtype=np.float64)
    for j, item in enumerate(basis):
        blocks = _v23c_split_h0(_v17_apply_W_faces(item["state"], C)[0])
        for key, block in blocks.items():
            for i in bykey.get(key, ()):
                W[i, j] = _v27_inner(basis[i]["state"], block)
        now = time.time()
        if V27_PROGRESS and (now - last >= V27_HEARTBEAT or j + 1 == nb):
            print(
                f"      W {j+1:,}/{nb:,}; Haar-cache={_v27_factor_haar_canon.cache_info()}; "
                f"elapsed={now-t0:.1f}s",
                flush=True,
            )
            last = now
    herm = float(np.max(np.abs(W - W.T))) if nb else 0.0
    if herm > V27_HERM_TOL:
        raise RuntimeError(f"finite-cluster W is not Hermitian: {herm:.3e}")
    W = 0.5 * (W + W.T)
    counts = tuple(len(x) for x in layers)
    return dict(
        C=C, vacuum=bool(vacuum), pfaces=pfaces, nP=nP, basis=basis,
        H0=H0, W=W, dim=nb, layer_counts=counts, herm=herm,
    )


def _v27_cluster_coefficients(C, order=None):
    order = V27_ORDER if order is None else int(order)
    depth = order // 2
    one = _v27_build_basis(C, vacuum=False, max_layer=depth)
    vac = _v27_build_basis(C, vacuum=True, max_layer=depth)
    op, ooff = _v26_sw_blocks(one, order)
    vp, voff = _v26_sw_blocks(vac, order)
    root_i = one["pfaces"].index(V23C_ROOT)
    _, ra, rb = faces[V23C_ROOT]
    same = [
        i for i, f in enumerate(one["pfaces"])
        if tuple(faces[int(f)][1:]) == (ra, rb)
    ]
    coef = np.asarray(
        [float(np.sum(op[r][root_i, same]) - vp[r][0, 0]) for r in range(order + 1)],
        dtype=np.float64,
    )
    if abs(coef[0] - 8.0 / 3.0) > 2e-10:
        raise RuntimeError(f"incorrect u=0 cluster gap: {coef[0]}")
    return dict(
        coef=coef, order=order, depth=depth,
        one_dim=one["dim"], vac_dim=vac["dim"],
        one_layers=one["layer_counts"], vac_layers=vac["layer_counts"],
        sw_offdiag=max(float(ooff), float(voff)),
        one_herm=one["herm"], vac_herm=vac["herm"],
        method=f"canonical Hermitian SW/BCH through O(u^{order})",
    )


# ---------------------------------------------------------------------------
# 3. Exact-SW arbitrary-order regression
# ---------------------------------------------------------------------------


def _v27_sw_regression(order):
    errors = []
    for seed in (2711, 2712):
        rr = _v23_random.Random(seed)
        p, n = 2, 6
        H0 = _v23_sp.diag(0, 0, 2, 3, 5, 7)
        V = _v23_sp.zeros(n)
        a = _v23_sp.Integer(rr.randint(-2, 2))
        V[:p, :p] = a * _v23_sp.eye(p)
        for i in range(p, n):
            for j in range(p):
                x = _v23_sp.Integer(rr.randint(-2, 2))
                V[i, j] = V[j, i] = x
        for i in range(p, n):
            for j in range(i, n):
                x = _v23_sp.Integer(rr.randint(-2, 2))
                V[i, j] = V[j, i] = x
        exact = _v23_sw_exact(H0, V, p, order)
        model = dict(
            H0=np.asarray([float(H0[i, i]) for i in range(n)]),
            W=np.asarray(V.tolist(), dtype=np.float64), nP=p,
        )
        got, off = _v26_sw_blocks(model, order)
        err = max(
            max(
                float(np.max(np.abs(got[r] - np.asarray(exact[r].tolist(), dtype=float))))
                for r in range(order + 1)
            ),
            float(off),
        )
        errors.append(err)
    return max(errors)


print("\n[2] ORDER-GENERIC SW REGRESSION")
V27_SW_REGRESSION_ERROR = _v27_sw_regression(V27_ORDER)
v27_gate(
    f"NumPy SW recursion matches exact rational BCH through O(u^{V27_ORDER})",
    V27_SW_REGRESSION_ERROR < V27_SW_TOL,
    f"max error={V27_SW_REGRESSION_ERROR:.3e}",
)

print("\n[2b] ONE-FACE PHYSICAL PREFIX REGRESSION")
_v27_one_face = frozenset((V23C_ROOT,))
V27_ONE_FACE = _v27_cluster_coefficients(_v27_one_face, V27_ORDER)
_v27_one_face_old = _v23c_fit_cluster(_v27_one_face)
V27_ONE_FACE_PREFIX_ERROR = float(
    np.max(np.abs(V27_ONE_FACE["coef"][:5] - _v27_one_face_old["coef"][:5]))
)
v27_gate(
    "generic Haar/Krylov engine reproduces the certified v10a.26 one-face prefix",
    V27_ONE_FACE_PREFIX_ERROR < 3e-9,
    f"max O4-prefix error={V27_ONE_FACE_PREFIX_ERROR:.3e}; "
    f"new layers={V27_ONE_FACE['one_layers']}/{V27_ONE_FACE['vac_layers']}",
)


# ---------------------------------------------------------------------------
# 4. Generic bidirectional support history census
# ---------------------------------------------------------------------------


def _v27_history_levels(max_depth, pol=None):
    pol = V23C_POL if pol is None else int(pol)
    root = int(anchor_faces[pol])
    levels = [{frozenset((root,)): _v10a3_face_state(root)}]
    for depth in range(1, int(max_depth) + 1):
        nxt, stats = _v17_apply_W_labeled(levels[-1], f"v27 unrestricted W{depth}")
        levels.append(nxt)
        print(
            f"  history depth {depth}: supports={len(nxt):,} "
            f"actions={stats['actions']:,} channels={stats['channels']:,}"
        )
    return levels


def _v27_support_census(order, pol=None, history_levels=None):
    order = int(order)
    pol = V23C_POL if pol is None else int(pol)
    root = int(anchor_faces[pol])
    left_depth = order // 2
    right_depth = order - left_depth
    if history_levels is None or len(history_levels) <= right_depth:
        history_levels = _v27_history_levels(right_depth, pol)
    supports, endpoints, stats = _v24c_candidate_supports(
        history_levels[left_depth], history_levels[right_depth],
        root, root, max_size=order + 2,
    )
    return supports, endpoints, stats, history_levels


def _v27_rooted_extent(C):
    """Maximum centered coordinate displacement from the marked root."""
    root_vertex = faces[V23C_ROOT][0]
    extent = 0
    boundary = False
    for f in C:
        v = faces[int(f)][0]
        for i in range(3):
            raw = (int(v[i]) - int(root_vertex[i])) % int(L)
            d = raw if raw <= int(L) // 2 else raw - int(L)
            extent = max(extent, abs(int(d)))
            if int(L) % 2 == 1 and abs(int(d)) == int(L) // 2:
                boundary = True
    return extent, boundary


print("\n[3] GENERIC SUPPORT-CENSUS REGRESSION AT ORDER FOUR")
_v27_histories = _v27_history_levels(max(2, V27_SUPPORT_HALF_DEPTH), V23C_POL)
V27_O4_SUPPORTS, _, V27_O4_STATS, _ = _v27_support_census(
    4, V23C_POL, _v27_histories
)
if "MAXC" in globals():
    _v27_missing_o4 = set(MAXC) - set(V27_O4_SUPPORTS)
    v27_gate(
        "unrestricted bidirectional histories cover the certified O4 support corpus",
        not _v27_missing_o4,
        f"generic={len(V27_O4_SUPPORTS)}, certified={len(MAXC)}, missing={len(_v27_missing_o4)}",
    )
else:
    v27_gate("completed O4 support corpus is available for regression", False, "MAXC missing")


print(f"\n[4] ORDER-{V27_ORDER} SUPPORT CENSUS")
V27_MAXC, V27_ENDPOINT_SUPPORTS, V27_SUPPORT_STATS, _v27_histories = _v27_support_census(
    V27_ORDER, V23C_POL, _v27_histories
)
if not V27_MAXC:
    v27_gate("order-n support census is nonempty", False, V27_SUPPORT_STATS)
else:
    v27_gate("order-n support census is nonempty", True, V27_SUPPORT_STATS)

_extent_rows = [(C,) + _v27_rooted_extent(C) for C in V27_MAXC]
_boundary = [row for row in _extent_rows if row[2]]
V27_MAX_EXTENT = max((row[1] for row in _extent_rows), default=0)
v27_gate(
    "periodic geometry is free of half-box support aliases",
    not _boundary,
    f"L={L}, max centered extent={V27_MAX_EXTENT}, boundary supports={len(_boundary)}",
)

V27_CLUSTERS = set()
for C in V27_MAXC:
    V27_CLUSTERS.update(_v23c_rooted_connected_subsets(C))

# Preserve unconditional lower-order regression coverage.
_small = {frozenset((V23C_ROOT,))}
for _ in range(2):
    nxt = set()
    for S in _small:
        frontier = set()
        for f in S:
            frontier.update(_V17_NEIGH[int(f)])
        for g in frontier - set(S):
            T = frozenset(set(S) | {int(g)})
            if len(T) <= 3 and _v17_connected(T):
                nxt.add(T)
    _small.update(nxt)
V27_CLUSTERS.update(_small)

_downward_missing = []
for C in V27_CLUSTERS:
    for S in _v23c_rooted_connected_subsets(C):
        if S not in V27_CLUSTERS:
            _downward_missing.append((C, S))
            break
v27_gate(
    "order-n rooted cluster poset is downward closed",
    not _downward_missing,
    f"clusters={len(V27_CLUSTERS)}, maximal={len(V27_MAXC)}, missing={len(_downward_missing)}",
)

V27_SHAPE_KEYS = {_v24c_shape_key(C) for C in V27_CLUSTERS}
print("  concrete rooted clusters       :", len(V27_CLUSTERS))
print("  rooted proper-rotation classes :", len(V27_SHAPE_KEYS))
print("  size histogram                 :", dict(sorted(Counter(map(len, V27_CLUSTERS)).items())))


# ---------------------------------------------------------------------------
# 5. Checkpointed production and rooted incidence transform
# ---------------------------------------------------------------------------


def _v27_signature():
    payload = (
        V27_SCHEMA, int(L), int(V23C_POL), int(V27_ORDER), int(V27_HAAR_CAP),
        tuple(sorted(map(repr, V27_SHAPE_KEYS))),
    )
    return hashlib.sha256(repr(payload).encode()).hexdigest()


V27_RUN_SIGNATURE = _v27_signature()


def _v27_save(cache):
    if not V27_CHECKPOINT:
        return
    path = os.path.abspath(os.path.expanduser(V27_CHECKPOINT))
    parent = os.path.dirname(path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    tmp = path + ".tmp"
    payload = dict(
        schema=V27_SCHEMA, signature=V27_RUN_SIGNATURE, order=V27_ORDER,
        haar_cap=V27_HAAR_CAP, shape_cache=cache, saved_at=time.time(),
    )
    with open(tmp, "wb") as fh:
        pickle.dump(payload, fh, protocol=pickle.HIGHEST_PROTOCOL)
        fh.flush()
        os.fsync(fh.fileno())
    os.replace(tmp, path)


def _v27_load():
    if not (V27_RESUME and V27_CHECKPOINT and os.path.exists(V27_CHECKPOINT)):
        return {}
    with open(V27_CHECKPOINT, "rb") as fh:
        payload = pickle.load(fh)
    if payload.get("schema") != V27_SCHEMA or payload.get("signature") != V27_RUN_SIGNATURE:
        print("  incompatible checkpoint ignored")
        return {}
    cache = {
        k: v for k, v in dict(payload.get("shape_cache", {})).items()
        if k in V27_SHAPE_KEYS
    }
    print(f"  resumed {len(cache)}/{len(V27_SHAPE_KEYS)} shapes from {V27_CHECKPOINT}")
    return cache


def _v27_lower_targets():
    return {
        0: 8.0 / 3.0,
        1: 1.0,
        2: 11.0 / 306.0,
        3: -109151.0 / 249696.0,
        4: -0.7751458630189173,
    }


def _v27_production():
    if not all(ok for _, ok, _ in V27_GATES):
        raise RuntimeError("v10a.27 preflight gate failure; production is blocked")
    cache = _v27_load()
    representatives = {}
    raw = {}
    duplicate_checks = 0
    max_offdiag = 0.0
    t0 = time.time()
    ordered = sorted(V27_CLUSTERS, key=lambda C: (len(C), _v24c_shape_key(C), tuple(sorted(C))))
    try:
        for C in ordered:
            key = _v24c_shape_key(C)
            representatives.setdefault(key, C)
            if key not in cache:
                print(
                    f"  shape START {len(cache)+1}/{len(V27_SHAPE_KEYS)} |C|={len(C)}",
                    flush=True,
                )
                item = _v27_cluster_coefficients(C, V27_ORDER)
                cache[key] = item
                _v27_save(cache)
                dt = time.time() - t0
                done = len(cache)
                eta = dt * (len(V27_SHAPE_KEYS) - done) / max(done, 1)
                print(
                    f"  shape DONE  {done}/{len(V27_SHAPE_KEYS)} |C|={len(C)} "
                    f"dim={item['one_dim']}/{item['vac_dim']} "
                    f"layers={item['one_layers']}/{item['vac_layers']} "
                    f"c{V27_ORDER}={item['coef'][V27_ORDER]:+.12g} "
                    f"SWoff={item['sw_offdiag']:.2e} elapsed={dt:.1f}s ETA~{eta:.1f}s",
                    flush=True,
                )
            item = cache[key]
            max_offdiag = max(max_offdiag, float(item["sw_offdiag"]))
            if duplicate_checks < V27_DUPLICATE_CHECKS and C != representatives[key]:
                other = _v27_cluster_coefficients(C, V27_ORDER)
                err = float(np.max(np.abs(other["coef"] - item["coef"])))
                v27_gate(
                    f"rooted proper-rotation duplicate #{duplicate_checks+1}",
                    err < 3e-9, f"max coefficient error={err:.3e}",
                )
                duplicate_checks += 1
            raw[C] = np.asarray(item["coef"], dtype=np.float64).copy()
    except KeyboardInterrupt:
        _v27_save(cache)
        print(f"\n[SAFE INTERRUPT] saved {len(cache)}/{len(V27_SHAPE_KEYS)} shapes")
        raise

    v27_gate(
        f"exact SW block diagonalization closes through O(u^{V27_ORDER})",
        max_offdiag < V27_SW_TOL, f"max P-Q residual={max_offdiag:.3e}",
    )
    v27_gate(
        "every rooted shape has a coefficient",
        len(cache) == len(V27_SHAPE_KEYS), f"{len(cache)}/{len(V27_SHAPE_KEYS)}",
    )

    omega = {}
    totals = np.zeros(V27_ORDER + 1, dtype=np.float64)
    by_size = defaultdict(lambda: np.zeros(V27_ORDER + 1, dtype=np.float64))
    for C in sorted(V27_CLUSTERS, key=lambda x: (len(x), tuple(sorted(x)))):
        z = raw[C].copy()
        for S in _v23c_rooted_connected_subsets(C):
            if S != C:
                z -= omega[S]
        omega[C] = z
        totals += z
        by_size[len(C)] += z

    print("\nROOTED INCIDENCE TRANSFORM")
    for size in sorted(by_size):
        row = " ".join(f"m{k}={by_size[size][k]:+.12g}" for k in range(1, V27_ORDER + 1))
        print(f"  size {size}: {row}")
    print("  TOTAL:", " ".join(f"m{k}={totals[k]:+.15g}" for k in range(V27_ORDER + 1)))

    for k, target in _v27_lower_targets().items():
        if k > V27_ORDER:
            continue
        tol = 2e-8 if k <= 2 else (2e-7 if k == 3 else 2e-6)
        v27_gate(
            f"rooted oracle reproduces protected lower coefficient m{k}",
            abs(totals[k] - target) < tol,
            f"got={totals[k]:+.15g}, error={totals[k]-target:+.3e}",
        )

    if not all(ok for _, ok, _ in V27_GATES):
        raise RuntimeError("v10a.27 production completed but a hard gate failed; do not unblind")
    result = dict(
        schema=V27_SCHEMA, signature=V27_RUN_SIGNATURE, order=V27_ORDER,
        coefficients=totals, by_size=dict(by_size), omega=omega,
        concrete_clusters=len(V27_CLUSTERS), shapes=len(V27_SHAPE_KEYS),
        haar_cap=V27_HAAR_CAP, krylov_depth=V27_KRYLOV_DEPTH,
        target_loaded=False,
    )
    print("\nBLIND PRODUCTION RESULT")
    print(f"  m{V27_ORDER} = {totals[V27_ORDER]!r}")
    print("  external target was not loaded; compare only in a separate verifier")
    return result


print("\n[5] PREFLIGHT SUMMARY")
for i, (name, ok, detail) in enumerate(V27_GATES, 1):
    print(f"{i:02d}. {'PASS' if ok else 'FAIL'} -- {name}" + (f" :: {detail}" if detail else ""))
print(f"PASSED {sum(int(ok) for _, ok, _ in V27_GATES)}/{len(V27_GATES)} PREFLIGHT GATES")

V27_RESULT = None
if V27_MODE == "production":
    V27_RESULT = _v27_production()
else:
    print(
        "\nPREFLIGHT ONLY.  If every gate passed, launch with:\n"
        f"  V27_ORDER={V27_ORDER} V27_HAAR_CAP={V27_HAAR_CAP} V27_MODE=production\n"
        "The Hamer coefficients remain absent from this file."
    )
