"""
HODGE v10a.28 -- order-aware Krylov/Gram optimization firewall
=======================================================================

Run this file in the SAME Python/Colab namespace after the completed v10a.26
cell.  It deliberately contains no coefficient at the requested new order and
performs no comparison to that target.  Certified lower-order values are used
only as regression locks.  Its jobs are:

  1. preserve the certified v10a.26/v10a.27 mathematics while eliminating
     redundant finite-W reconstruction;
  2. certify factorized SU(3) Haar projectors through a requested local
     occurrence cap (nine for the Q3 frontier);
  3. reuse Gram--Schmidt projections as exact Krylov-band W entries and build
     only the deepest self-block when the requested odd order needs it;
  4. cache contraction paths separately from Haar values and pre-index the
     physical/flux blocks of every retained basis vector;
  5. optionally generate an order-n support census from unrestricted, bidirectional
     magnetic histories, including paths that revisit P;
  6. extract rooted linked coefficients with canonical Hermitian SW/BCH.

The default mode is FIREWALL at order four.  It computes only the one-face
regression unless V28_RUN_CENSUS=1 is requested.  Production requires both
V28_MODE=production and an explicit order-matched confirmation string.  Even
then the default is one newly computed shape per invocation.  There is no
watchdog; every completed rooted shape is checkpointed atomically.

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

try:
    import cupy as cp
    _v28_gpu_count = int(cp.cuda.runtime.getDeviceCount())
except Exception:
    cp = None
    _v28_gpu_count = 0


V28_SCHEMA = "hodge-v10a28-order-aware-krylov-gram-haar9-v1"
V28_ORDER = int(os.environ.get("V28_ORDER", "4"))
V28_MODE = os.environ.get("V28_MODE", "firewall").strip().lower()
V28_HAAR_CAP = int(os.environ.get("V28_HAAR_CAP", "7" if V28_ORDER <= 5 else "9"))
V28_PROGRESS = int(os.environ.get("V28_PROGRESS", "1"))
V28_HEARTBEAT = float(os.environ.get("V28_HEARTBEAT", "20"))
V28_RESUME = int(os.environ.get("V28_RESUME", "1"))
V28_CHECKPOINT = os.environ.get(
    "V28_CHECKPOINT", f"/content/hodge_v10a28_m{V28_ORDER}_shapes.pkl"
)
V28_CENSUS_CHECKPOINT = os.environ.get(
    "V28_CENSUS_CHECKPOINT", f"/content/hodge_v10a28_m{V28_ORDER}_census.pkl"
)
V28_GRAM_TOL = float(os.environ.get("V28_GRAM_TOL", "2e-10"))
V28_HERM_TOL = float(os.environ.get("V28_HERM_TOL", "2e-8"))
V28_SW_TOL = float(os.environ.get("V28_SW_TOL", "2e-10"))
V28_DUPLICATE_CHECKS = int(os.environ.get("V28_DUPLICATE_CHECKS", "0"))
V28_HAAR_CACHE_SIZE = int(os.environ.get("V28_HAAR_CACHE_SIZE", "2000000"))
V28_PATH_CACHE_SIZE = int(os.environ.get("V28_PATH_CACHE_SIZE", "250000"))
V28_PATH_OPTIMIZER = os.environ.get("V28_PATH_OPTIMIZER", "greedy").strip().lower()
V28_HERMITICITY_AUDIT_PAIRS = int(os.environ.get("V28_HERMITICITY_AUDIT_PAIRS", "12"))
V28_TIME_BUDGET_MINUTES = float(os.environ.get("V28_TIME_BUDGET_MINUTES", "30"))
V28_MAX_NEW_SHAPES = int(os.environ.get("V28_MAX_NEW_SHAPES", "1"))
V28_RUN_CENSUS = int(os.environ.get("V28_RUN_CENSUS", "1" if V28_MODE == "production" else "0"))
V28_ALLOW_REFERENCE_REBUILD = int(os.environ.get("V28_ALLOW_REFERENCE_REBUILD", "0"))
V28_PRODUCTION_CONFIRM = os.environ.get("V28_PRODUCTION_CONFIRM", "").strip()
V28_GPU = os.environ.get("V28_GPU", "auto").strip().lower()
if V28_GPU not in ("auto", "0", "1", "off", "on", "false", "true"):
    raise ValueError("V28_GPU must be auto/on/off or 1/0")
V28_GPU_ENABLED = _v28_gpu_count > 0 and V28_GPU not in ("0", "off", "false")
if V28_GPU in ("1", "on", "true") and not V28_GPU_ENABLED:
    raise RuntimeError("V28_GPU requested but no usable CuPy CUDA device was found")
V28_GPU_SW_MIN_DIM = int(os.environ.get("V28_GPU_SW_MIN_DIM", "96"))

if V28_ORDER not in (4, 5, 6, 7):
    raise ValueError("V28_ORDER must be 4, 5, 6, or 7")
if V28_MODE not in ("firewall", "production"):
    raise ValueError("V28_MODE must be 'firewall' or 'production'")
if V28_PATH_OPTIMIZER not in ("greedy", "auto", "auto-hq", "dp", "branch-2"):
    raise ValueError("unsupported V28_PATH_OPTIMIZER")
if V28_MAX_NEW_SHAPES < 0:
    raise ValueError("V28_MAX_NEW_SHAPES must be nonnegative (0 means unlimited)")
if V28_TIME_BUDGET_MINUTES < 0:
    raise ValueError("V28_TIME_BUDGET_MINUTES must be nonnegative")
if V28_HERMITICITY_AUDIT_PAIRS < 1:
    raise ValueError("V28_HERMITICITY_AUDIT_PAIRS must be at least one")
_v28_required_haar_cap = 7 if V28_ORDER <= 5 else 9
if V28_HAAR_CAP < _v28_required_haar_cap:
    raise ValueError(
        f"order {V28_ORDER} requires V28_HAAR_CAP>={_v28_required_haar_cap}"
    )
if V28_HAAR_CAP > 9:
    raise ValueError("v10a.28 is certified only through local Haar cap nine")
if V28_MODE == "production":
    expected_confirmation = f"YES_ORDER_{V28_ORDER}"
    if V28_PRODUCTION_CONFIRM != expected_confirmation:
        raise RuntimeError(
            "production is intentionally locked; set "
            f"V28_PRODUCTION_CONFIRM={expected_confirmation} after the firewall passes"
        )
    if not V28_RUN_CENSUS:
        raise RuntimeError("production requires V28_RUN_CENSUS=1")

V28_KRYLOV_DEPTH = V28_ORDER // 2
V28_SUPPORT_HALF_DEPTH = (V28_ORDER + 1) // 2
V28_MARKED_SUPPORT_BOUND = V28_ORDER + 2


_REQUIRED_GLOBALS = (
    "L", "N", "faces", "verts", "T1_POLS", "anchor_faces", "V23C_ROOT",
    "V23C_POL", "_FAST_EPS", "oe", "LXState", "_V17_VAC",
    "_v17_apply_W_faces", "_v17_apply_W_labeled", "_v17_connected",
    "_v17_phys_index", "_v17_translate_support", "_v17_translate_face",
    "_v23c_split_h0", "_v23c_rooted_connected_subsets", "_v24c_shape_key",
    "_v24c_candidate_supports", "_v10a3_face_state", "_v10a3_h0_state_inner",
    "_v10a3_physical_blocks", "_v10a3_compress_state", "_v9_flux_key_state",
    "_joint_canon_states", "lx_combine_bra_ket", "_v26_sw_blocks",
    "_v23_sw_exact", "_v23_sp", "_v23_random", "_V23CF",
    "_v26_singlet_multiplicity", "_V17_NEIGH", "_v23c_fit_cluster",
)
_missing = [name for name in _REQUIRED_GLOBALS if name not in globals()]
if _missing:
    raise RuntimeError(
        "v10a.28 must run after the completed v10a.26 cell; missing symbols: "
        + ", ".join(_missing)
    )


V28_GATES = []


def v28_gate(name, ok, detail=""):
    ok = bool(ok)
    V28_GATES.append((str(name), ok, str(detail)))
    print(("[PASS] " if ok else "[FAIL] ") + str(name) + (f" :: {detail}" if detail != "" else ""))
    return ok


print("=" * 148)
print(f"HODGE v10a.28 -- ORDER-{V28_ORDER} OPTIMIZATION FIREWALL")
print("=" * 148)
print("mode                         :", V28_MODE)
print("target coefficient           : NOT LOADED")
print("Krylov closure depth         :", V28_KRYLOV_DEPTH)
print("support half-history depth   :", V28_SUPPORT_HALF_DEPTH)
print("marked-support safe bound    :", V28_MARKED_SUPPORT_BOUND)
print("certified local Haar cap     :", V28_HAAR_CAP)
print("factorized Haar cache entries:", f"{V28_HAAR_CACHE_SIZE:,}")
print("contraction-path cache       :", f"{V28_PATH_CACHE_SIZE:,} ({V28_PATH_OPTIMIZER})")
print("support census enabled       :", bool(V28_RUN_CENSUS))
print("support census checkpoint    :", V28_CENSUS_CHECKPOINT)
print("production budget            :", f"{V28_TIME_BUDGET_MINUTES:g} min between shapes")
print("new shapes per invocation    :", "unlimited" if V28_MAX_NEW_SHAPES == 0 else V28_MAX_NEW_SHAPES)
print("hybrid GPU backend           :", "CuPy/CUDA" if V28_GPU_ENABLED else "CPU fallback")
print("watchdog                     : NONE")


# ---------------------------------------------------------------------------
# 1. Exact invariant-basis Haar projectors through local occurrence cap nine
# ---------------------------------------------------------------------------


def _v28_triple_partitions(items):
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
        for tail in _v28_triple_partitions(remain):
            yield (triple,) + tail


def _v28_invariant_specs(nmajor, nminor):
    """Delta/epsilon spanning family for Inv(3^nmajor x 3bar^nminor)."""
    nmajor, nminor = int(nmajor), int(nminor)
    if nmajor < nminor or (nmajor - nminor) % 3:
        return ()
    specs = []
    for targets in itertools.permutations(range(nmajor), nminor):
        used = set(targets)
        remainder = tuple(i for i in range(nmajor) if i not in used)
        for triples in _v28_triple_partitions(remainder):
            deltas = tuple((int(targets[j]), nmajor + j) for j in range(nminor))
            specs.append((deltas, tuple(tuple(map(int, t)) for t in triples)))
    return tuple(specs)


def _v28_greedy_gram_basis(G, expected_rank, tol=1e-9):
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
def _v28_projector_data(nfund, nanti):
    """Return a certified factor I C I for a center-admissible SU(3) Haar integral."""
    nfund, nanti = int(nfund), int(nanti)
    if (nfund - nanti) % 3:
        raise ValueError("center-forbidden Haar pattern")
    nmajor, nminor = max(nfund, nanti), min(nfund, nanti)
    m = nmajor + nminor
    specs = _v28_invariant_specs(nmajor, nminor)
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
    if V28_GPU_ENABLED and RF.size >= 100_000:
        dRF = cp.asarray(RF)
        Graw = cp.asnumpy(cp.rint(dRF @ dRF.T)).astype(np.int64)
        del dRF
    else:
        Graw = np.rint(RF @ RF.T).astype(np.int64)
    keep = _v28_greedy_gram_basis(Graw, expected)
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


V28_ADMISSIBLE_PATTERNS = tuple(
    (a, b)
    for total in range(1, V28_HAAR_CAP + 1)
    for a in range(total + 1)
    for b in (total - a,)
    if (a - b) % 3 == 0
)


def _v28_certify_haar_cap():
    reports = []
    seen = set()
    for a, b in V28_ADMISSIBLE_PATTERNS:
        key = (max(a, b), min(a, b))
        if key in seen:
            continue
        seen.add(key)
        _, _, cert = _v28_projector_data(a, b)
        reports.append(cert)
        print(
            f"  Haar {a},{b}: raw={cert['raw_count']} rank={cert['selected_rank']} "
            f"span={cert['raw_span_error']:.2e} inv={cert['gram_inverse_error']:.2e}"
        )
    return reports


@lru_cache(maxsize=V28_HAAR_CACHE_SIZE)
def _v28_factor_haar_canon(a, b):
    occ, part = lx_combine_bra_ket(a, b)
    by = defaultdict(lambda: {True: [], False: []})
    for i, (link, typ) in enumerate(occ):
        by[int(link)][bool(typ)].append(i)
    args, topology = [], []
    aux = (max(part) + 1) if part else 0
    for group in by.values():
        U, B = group[True], group[False]
        pat = (len(U), len(B))
        if (pat[0] - pat[1]) % 3:
            return 0.0
        if sum(pat) > V28_HAAR_CAP:
            raise RuntimeError(
                f"local Haar occurrence {pat} exceeds certified cap {V28_HAAR_CAP}; "
                "increase the cap only after a support census"
            )
        if pat not in V28_ADMISSIBLE_PATTERNS:
            raise RuntimeError(f"uncertified center-admissible Haar pattern {pat}")
        I, C, _ = _v28_projector_data(*pat)
        items = (U + B) if len(U) >= len(B) else (B + U)
        row = [int(part[2 * p]) for p in items]
        col = [int(part[2 * p + 1]) for p in items]
        ar, ac = aux, aux + 1
        aux += 2
        args.extend((I, [ar] + row, C, [ar, ac], I, [ac] + col))
        topology.append((pat, tuple(row), tuple(col), int(ar), int(ac)))
    if not args:
        return float(N ** len(set(part)))
    path = _v28_contraction_path(tuple(topology))
    return float(oe.contract(*args, [], optimize=path))


@lru_cache(maxsize=V28_PATH_CACHE_SIZE)
def _v28_contraction_path(topology):
    """Cache the optimizer result by integer wiring, independently of values."""
    args = []
    for pat, row, col, ar, ac in topology:
        I, C, _ = _v28_projector_data(*pat)
        args.extend((I, [ar] + list(row), C, [ar, ac], I, [ac] + list(col)))
    path, _ = oe.contract_path(*args, [], optimize=V28_PATH_OPTIMIZER)
    return tuple(path)


def _v28_cluster_haar(a, b):
    aa, bb = _joint_canon_states(a, b)
    ka, kb = (aa.occ, aa.part), (bb.occ, bb.part)
    if kb < ka:
        aa, bb = bb, aa
    return _v28_factor_haar_canon(aa, bb)


print("\n[1] FACTORIZED SU(3) HAAR CERTIFICATE")
V28_HAAR_REPORTS = _v28_certify_haar_cap()
v28_gate(
    "every center-admissible local pattern through requested cap is certified",
    len(V28_ADMISSIBLE_PATTERNS) > 0
    and all(
        r["selected_rank"] == r["representation_singlets"]
        and r["gram_inverse_error"] < 2e-9
        and r["raw_span_error"] < 2e-9
        for r in V28_HAAR_REPORTS
    ),
    f"cap={V28_HAAR_CAP}, patterns={V28_ADMISSIBLE_PATTERNS}",
)


# ---------------------------------------------------------------------------
# 2. Order-generic physical Krylov basis
# ---------------------------------------------------------------------------


def _v28_state_copy(a):
    return {sig: dict(v) for sig, v in a.items()}


def _v28_state_add(dst, src, scale=1.0):
    for sig, vec in src.items():
        d = dst.setdefault(sig, {})
        for st, x in vec.items():
            d[st] = d.get(st, 0.0) + float(scale) * float(x)
    return dst


def _v28_state_scaled(a, scale):
    return _v10a3_compress_state({
        sig: {st: float(scale) * float(x) for st, x in v.items()}
        for sig, v in a.items()
    })


def _v28_index_state(state):
    """Pre-index a physical state by H0 block and center-flux residue."""
    indexed = {}
    for h0key, vec in _v10a3_physical_blocks(state).items():
        groups = defaultdict(list)
        for st, coeff in vec.items():
            groups[_v9_flux_key_state(st)].append((st, float(coeff)))
        indexed[h0key] = {key: tuple(items) for key, items in groups.items()}
    return indexed


def _v28_inner_indexed(A, B, stats=None):
    """Exact H0/center-prefiltered Haar inner product on prepared indexes."""
    if stats is not None:
        stats["indexed_inner_calls"] += 1
    if len(A) > len(B):
        A, B = B, A
    ans = 0.0
    for h0key, ga in A.items():
        gb = B.get(h0key)
        if not gb:
            continue
        if len(ga) > len(gb):
            ga, gb = gb, ga
        for fluxkey, left in ga.items():
            right = gb.get(fluxkey)
            if not right:
                continue
            if stats is not None:
                stats["trace_pair_requests"] += len(left) * len(right)
            for a, ca in left:
                for b, cb in right:
                    ans += ca * cb * _v28_cluster_haar(a, b)
    return float(ans)


def _v28_inner(a, b):
    return _v28_inner_indexed(_v28_index_state(a), _v28_index_state(b))


def _v28_norm2(a):
    x = _v28_inner(a, a)
    if x < -5e-9:
        raise RuntimeError(f"negative Haar norm in v10a.28 basis: {x:.3e}")
    return max(0.0, x)


def _v28_build_basis(C, vacuum=False, max_layer=None, order=None):
    """Build a Krylov basis and its required W entries in the same traversal.

    For order n and d=floor(n/2), columns through layer d-1 are produced while
    constructing Q_d.  Hermiticity supplies their transpose.  The Q_d W Q_d
    block is required only for odd n; at even n it cannot occur in a closed
    length-n P-to-P history and is therefore left exactly zero.
    """
    C = frozenset(map(int, C))
    if not C:
        raise ValueError("empty finite cluster")
    order = V28_ORDER if order is None else int(order)
    if max_layer is None:
        max_layer = order // 2
    max_layer = int(max_layer)
    if max_layer != order // 2:
        raise ValueError("order-aware builder requires max_layer=floor(order/2)")
    t0, last = time.time(), time.time()
    pfaces = tuple(sorted(C)) if not vacuum else ()
    initial = [_v28_state_copy(_V17_VAC)] if vacuum else [
        _v28_state_copy(_v10a3_face_state(f)) for f in pfaces
    ]
    basis, bykey, p_indices = [], defaultdict(list), []
    w_entries, w_sources = {}, {}
    stats = Counter(
        magnetic_actions=0, indexed_inner_calls=0, trace_pair_requests=0,
        projection_reuses=0, direct_projection_evals=0,
        deep_self_evals=0, hermiticity_audit_evals=0,
    )
    second_pass_max = 0.0
    haar_start = _v28_factor_haar_canon.cache_info()
    path_start = _v28_contraction_path.cache_info()

    def put_w(i, j, value, source):
        i, j, value = int(i), int(j), float(value)
        if abs(basis[i]["layer"] - basis[j]["layer"]) > 1:
            if abs(value) > V28_HERM_TOL:
                raise RuntimeError(
                    f"Krylov band violation W[{i},{j}]={value:+.3e} "
                    f"at layers {basis[i]['layer']}/{basis[j]['layer']}"
                )
            return
        pair = (min(i, j), max(i, j))
        if pair in w_entries:
            old = w_entries[pair]
            err = abs(old - value)
            if err > V28_HERM_TOL * max(1.0, abs(old), abs(value)):
                raise RuntimeError(
                    f"inconsistent Hermitian Gram ledger {pair}: "
                    f"{old:+.12g} versus {value:+.12g}"
                )
            w_entries[pair] = 0.5 * (old + value)
            w_sources[pair] = w_sources[pair] + "+" + str(source)
        else:
            w_entries[pair] = value
            w_sources[pair] = str(source)

    def add_raw(raw, key, layer, name, parent=None):
        nonlocal second_pass_max
        v = _v28_state_copy(raw)
        first_projection = {}
        for gs_pass in range(2):
            vidx = _v28_index_state(v)
            corrections = []
            for i in bykey.get(key, ()):
                pair = None if parent is None else (min(i, parent), max(i, parent))
                if gs_pass == 0 and pair is not None and pair in w_entries:
                    ov = w_entries[pair]
                    stats["projection_reuses"] += 1
                else:
                    ov = _v28_inner_indexed(basis[i]["index"], vidx, stats)
                    if gs_pass == 0:
                        stats["direct_projection_evals"] += 1
                if gs_pass == 0:
                    first_projection[i] = float(ov)
                else:
                    second_pass_max = max(second_pass_max, abs(float(ov)))
                if abs(ov) > 1e-13:
                    corrections.append((i, float(ov)))
            for i, ov in corrections:
                _v28_state_add(v, basis[i]["state"], -ov)
            v = _v10a3_compress_state(v)
        vidx = _v28_index_state(v)
        n2 = _v28_inner_indexed(vidx, vidx, stats)
        if n2 < -5e-9:
            raise RuntimeError(f"negative Haar norm in v10a.28 basis: {n2:.3e}")
        n2 = max(0.0, float(n2))
        if parent is not None:
            for i, ov in first_projection.items():
                put_w(i, parent, ov, "GS")
        if n2 <= V28_GRAM_TOL:
            return None
        v = _v28_state_scaled(v, 1.0 / math.sqrt(n2))
        i = len(basis)
        basis.append(dict(
            state=v, index=_v28_index_state(v), key=key,
            layer=int(layer), name=str(name),
        ))
        bykey[key].append(i)
        if parent is not None:
            put_w(i, parent, math.sqrt(n2), "residual-norm")
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
            stats["magnetic_actions"] += 1
            for key, block in _v23c_split_h0(w).items():
                i = add_raw(
                    block, key, depth, f"W(Q{depth-1}:{jj})", parent=j,
                )
                if i is not None:
                    new_layer.append(i)
            now = time.time()
            if V28_PROGRESS and (now - last >= V28_HEARTBEAT or jj + 1 == len(parents)):
                print(
                    f"      Q{depth} {jj+1:,}/{len(parents):,}; dim={len(basis):,}; "
                    f"ledger={len(w_entries):,}; reuse={stats['projection_reuses']:,}; "
                    f"Haar-cache={_v28_factor_haar_canon.cache_info()}; elapsed={now-t0:.1f}s",
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

    deepest_self_required = bool(order % 2)
    deep_t0 = time.time()
    if deepest_self_required:
        deepest = set(layers[-1])
        for jj, j in enumerate(layers[-1]):
            wstate = _v17_apply_W_faces(basis[j]["state"], C)[0]
            stats["magnetic_actions"] += 1
            for key, block in _v23c_split_h0(wstate).items():
                bidx = _v28_index_state(block)
                for i in bykey.get(key, ()):
                    if i not in deepest or i > j:
                        continue
                    x = _v28_inner_indexed(basis[i]["index"], bidx, stats)
                    stats["deep_self_evals"] += 1
                    put_w(i, j, x, "odd-deep-self")
            now = time.time()
            if V28_PROGRESS and (now - last >= V28_HEARTBEAT or jj + 1 == len(deepest)):
                print(
                    f"      Q{max_layer}WQ{max_layer} {jj+1:,}/{len(deepest):,}; "
                    f"ledger={len(w_entries):,}; elapsed={now-t0:.1f}s",
                    flush=True,
                )
                last = now
    deep_seconds = time.time() - deep_t0

    nb = len(basis)
    H0 = np.asarray([float(item["key"][1]) for item in basis], dtype=np.float64)
    W = np.zeros((nb, nb), dtype=np.float64)
    for (i, j), value in w_entries.items():
        W[i, j] = W[j, i] = float(value)

    # Independent reverse-direction checks: W is filled symmetrically, so the
    # numerical identity W-W.T would not itself audit the Gram ledger.
    candidate_pairs = sorted(w_entries)
    if len(candidate_pairs) > V28_HERMITICITY_AUDIT_PAIRS > 0:
        pick = np.linspace(
            0, len(candidate_pairs) - 1,
            num=V28_HERMITICITY_AUDIT_PAIRS, dtype=int,
        )
        audit_pairs = [candidate_pairs[int(k)] for k in pick]
    else:
        audit_pairs = candidate_pairs
    reverse_cache = {}
    herm = 0.0
    for i, j in audit_pairs:
        if j not in reverse_cache:
            reverse_cache[j] = _v23c_split_h0(
                _v17_apply_W_faces(basis[j]["state"], C)[0]
            )
            stats["magnetic_actions"] += 1
        block = reverse_cache[j].get(basis[i]["key"])
        reverse = 0.0 if block is None else _v28_inner_indexed(
            basis[i]["index"], _v28_index_state(block), stats,
        )
        stats["hermiticity_audit_evals"] += 1
        herm = max(herm, abs(float(reverse) - float(W[i, j])))
    if herm > V28_HERM_TOL:
        raise RuntimeError(f"finite-cluster W Hermiticity audit failed: {herm:.3e}")
    counts = tuple(len(x) for x in layers)
    haar_end = _v28_factor_haar_canon.cache_info()
    path_end = _v28_contraction_path.cache_info()
    return dict(
        C=C, vacuum=bool(vacuum), pfaces=pfaces, nP=nP, basis=basis,
        H0=H0, W=W, dim=nb, layer_counts=counts, herm=herm,
        order=order, deepest_self_required=deepest_self_required,
        deepest_self_skipped=not deepest_self_required,
        gram_second_pass_max=second_pass_max,
        w_ledger_entries=len(w_entries), w_sources=w_sources,
        w_inner_evals=int(stats["indexed_inner_calls"]),
        trace_pair_requests=int(stats["trace_pair_requests"]),
        projection_reuses=int(stats["projection_reuses"]),
        direct_projection_evals=int(stats["direct_projection_evals"]),
        deep_self_evals=int(stats["deep_self_evals"]),
        magnetic_actions=int(stats["magnetic_actions"]),
        hermiticity_audit_pairs=len(audit_pairs),
        haar_hits=haar_end.hits-haar_start.hits,
        haar_misses=haar_end.misses-haar_start.misses,
        path_hits=path_end.hits-path_start.hits,
        path_misses=path_end.misses-path_start.misses,
        deep_self_seconds=deep_seconds,
        build_seconds=time.time()-t0,
    )


def _v28_poly_mul_backend(A, B, xp):
    order = len(A) - 1
    out = [xp.zeros_like(A[0]) for _ in range(order + 1)]
    for k in range(order + 1):
        for i in range(k + 1):
            out[k] += A[i] @ B[k - i]
    return out


def _v28_poly_comm_backend(A, B, xp):
    AB = _v28_poly_mul_backend(A, B, xp)
    BA = _v28_poly_mul_backend(B, A, xp)
    return [AB[i] - BA[i] for i in range(len(A))]


def _v28_bch_backend(H, S, order, xp):
    out = [x.copy() for x in H]
    X = [x.copy() for x in H]
    fac = 1.0
    for k in range(1, order + 1):
        X = _v28_poly_comm_backend(X, S, xp)
        fac *= float(k)
        for r in range(order + 1):
            out[r] += X[r] / fac
    return out


def _v28_sw_blocks(model, order, force_backend=None):
    """Canonical SW/BCH using CuPy for sufficiently large dense matrices."""
    n = int(np.asarray(model["W"]).shape[0])
    if force_backend == "gpu":
        use_gpu = V28_GPU_ENABLED
    elif force_backend == "cpu":
        use_gpu = False
    else:
        use_gpu = V28_GPU_ENABLED and n >= V28_GPU_SW_MIN_DIM
    xp = cp if use_gpu else np
    H0v = xp.asarray(model["H0"], dtype=xp.float64)
    V = xp.asarray(model["W"], dtype=xp.float64)
    p = int(model["nP"])
    Z = lambda: xp.zeros((n, n), dtype=xp.float64)
    H = [Z() for _ in range(order + 1)]
    H[0] = xp.diag(H0v)
    H[1] = V.copy()
    S = [Z() for _ in range(order + 1)]
    E0 = H0v[0]
    degerr = xp.max(xp.abs(H0v[:p] - E0))
    degerr = float(degerr.get()) if use_gpu else float(degerr)
    if degerr > 1e-12:
        raise RuntimeError("v10a.28 SW P block is not H0-degenerate")
    for r in range(1, order + 1):
        base = _v28_bch_backend(H, S, order, xp)[r]
        Sr = Z()
        if p < n:
            den = H0v[p:] - E0
            mind = xp.min(xp.abs(den))
            mind = float(mind.get()) if use_gpu else float(mind)
            if mind < 1e-13:
                raise RuntimeError("v10a.28 SW found a retained non-P E0 resonance")
            Sr[p:, :p] = -base[p:, :p] / den[:, None]
            Sr[:p, p:] = -Sr[p:, :p].T
        S[r] = Sr
    Hf = _v28_bch_backend(H, S, order, xp)
    off = 0.0
    if p < n:
        for r in range(1, order + 1):
            val = xp.max(xp.abs(Hf[r][:p, p:]))
            off = max(off, float(val.get()) if use_gpu else float(val))
    P = []
    for r in range(order + 1):
        z = 0.5 * (Hf[r][:p, :p] + Hf[r][:p, :p].T)
        P.append(cp.asnumpy(z) if use_gpu else np.asarray(z))
    return P, off, ("gpu" if use_gpu else "cpu")


def _v28_cluster_coefficients(C, order=None):
    order = V28_ORDER if order is None else int(order)
    depth = order // 2
    one = _v28_build_basis(C, vacuum=False, max_layer=depth, order=order)
    vac = _v28_build_basis(C, vacuum=True, max_layer=depth, order=order)
    op, ooff, obackend = _v28_sw_blocks(one, order)
    vp, voff, vbackend = _v28_sw_blocks(vac, order)
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
        w_inner_evals=one["w_inner_evals"] + vac["w_inner_evals"],
        trace_pair_requests=one["trace_pair_requests"] + vac["trace_pair_requests"],
        projection_reuses=one["projection_reuses"] + vac["projection_reuses"],
        direct_projection_evals=(
            one["direct_projection_evals"] + vac["direct_projection_evals"]
        ),
        deep_self_evals=one["deep_self_evals"] + vac["deep_self_evals"],
        deepest_self_required=bool(order % 2),
        deepest_self_skipped=not bool(order % 2),
        magnetic_actions=one["magnetic_actions"] + vac["magnetic_actions"],
        haar_hits=one["haar_hits"] + vac["haar_hits"],
        haar_misses=one["haar_misses"] + vac["haar_misses"],
        path_hits=one["path_hits"] + vac["path_hits"],
        path_misses=one["path_misses"] + vac["path_misses"],
        build_seconds=one["build_seconds"] + vac["build_seconds"],
        sw_backend=(obackend, vbackend),
        method=(
            f"order-aware Krylov Gram ledger plus canonical Hermitian "
            f"SW/BCH through O(u^{order})"
        ),
    )


# ---------------------------------------------------------------------------
# 3. Exact-SW arbitrary-order regression
# ---------------------------------------------------------------------------


def _v28_sw_regression(order):
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
        got, off, _ = _v28_sw_blocks(model, order, force_backend="cpu")
        err = max(
            max(
                float(np.max(np.abs(got[r] - np.asarray(exact[r].tolist(), dtype=float))))
                for r in range(order + 1)
            ),
            float(off),
        )
        errors.append(err)
    return max(errors)


def _v28_gpu_sw_regression(order):
    if not V28_GPU_ENABLED:
        return 0.0
    rr = np.random.default_rng(271927)
    p, n = 3, max(128, V28_GPU_SW_MIN_DIM)
    h0 = np.concatenate((np.zeros(p), np.linspace(1.0, 7.0, n - p)))
    V = rr.normal(size=(n, n))
    V = 0.5 * (V + V.T)
    V[:p, :p] = np.eye(p) * 0.125
    model = dict(H0=h0, W=V, nP=p)
    cpu, coff, _ = _v28_sw_blocks(model, order, force_backend="cpu")
    gpu, goff, _ = _v28_sw_blocks(model, order, force_backend="gpu")
    return max(
        max(float(np.max(np.abs(cpu[r] - gpu[r]))) for r in range(order + 1)),
        abs(float(coff) - float(goff)),
    )


def _v28_order_band_regression():
    """Check the even/odd deepest-block rule on generic Krylov-band models."""
    rng = np.random.default_rng(280427)
    errors, odd_sensitivity = {}, {}
    for order in (4, 5, 6, 7):
        depth = order // 2
        layer_sizes = [2] + [3] * (depth + 1)
        offsets = np.cumsum([0] + layer_sizes)
        n = int(offsets[-1])
        H0 = np.zeros(n, dtype=np.float64)
        for layer in range(1, len(layer_sizes)):
            sl = slice(offsets[layer], offsets[layer + 1])
            H0[sl] = layer + np.linspace(0.2, 0.8, layer_sizes[layer])
        W = np.zeros((n, n), dtype=np.float64)
        for layer in range(len(layer_sizes)):
            sl = slice(offsets[layer], offsets[layer + 1])
            z = rng.normal(size=(layer_sizes[layer], layer_sizes[layer]))
            W[sl, sl] = 0.5 * (z + z.T)
            if layer + 1 < len(layer_sizes):
                sr = slice(offsets[layer + 1], offsets[layer + 2])
                z = rng.normal(size=(layer_sizes[layer], layer_sizes[layer + 1]))
                W[sl, sr] = z
                W[sr, sl] = z.T

        full, _, _ = _v28_sw_blocks(
            dict(H0=H0, W=W, nP=layer_sizes[0]), order, force_backend="cpu",
        )
        cut = int(offsets[depth + 1])
        Wcut = W[:cut, :cut].copy()
        if order % 2 == 0:
            deep = slice(offsets[depth], offsets[depth + 1])
            Wcut[deep, deep] = 0.0
        reduced, _, _ = _v28_sw_blocks(
            dict(H0=H0[:cut], W=Wcut, nP=layer_sizes[0]),
            order, force_backend="cpu",
        )
        errors[order] = max(
            float(np.max(np.abs(full[r] - reduced[r])))
            for r in range(order + 1)
        )
        if order % 2:
            wrong = W[:cut, :cut].copy()
            deep = slice(offsets[depth], offsets[depth + 1])
            wrong[deep, deep] = 0.0
            missing, _, _ = _v28_sw_blocks(
                dict(H0=H0[:cut], W=wrong, nP=layer_sizes[0]),
                order, force_backend="cpu",
            )
            odd_sensitivity[order] = float(
                np.max(np.abs(full[order] - missing[order]))
            )
    return errors, odd_sensitivity


print("\n[2] ORDER-GENERIC SW REGRESSION")
V28_SW_REGRESSION_ERROR = _v28_sw_regression(V28_ORDER)
v28_gate(
    f"NumPy SW recursion matches exact rational BCH through O(u^{V28_ORDER})",
    V28_SW_REGRESSION_ERROR < V28_SW_TOL,
    f"max error={V28_SW_REGRESSION_ERROR:.3e}",
)
V28_GPU_SW_REGRESSION_ERROR = _v28_gpu_sw_regression(V28_ORDER)
v28_gate(
    "GPU and CPU SW/BCH backends agree",
    V28_GPU_SW_REGRESSION_ERROR < 2e-9,
    (f"max error={V28_GPU_SW_REGRESSION_ERROR:.3e}" if V28_GPU_ENABLED else "GPU unavailable; CPU fallback"),
)
V28_ORDER_BAND_ERRORS, V28_ODD_DEEP_SENSITIVITY = _v28_order_band_regression()
v28_gate(
    "order-aware Krylov truncation matches the full band model through O4--O7",
    max(V28_ORDER_BAND_ERRORS.values()) < V28_SW_TOL,
    ", ".join(f"O{k}={v:.2e}" for k, v in V28_ORDER_BAND_ERRORS.items()),
)
v28_gate(
    "odd-order regression detects removal of the required deepest self-block",
    min(V28_ODD_DEEP_SENSITIVITY.values()) > 1e-8,
    ", ".join(
        f"O{k} response={v:.2e}" for k, v in V28_ODD_DEEP_SENSITIVITY.items()
    ),
)

print("\n[2b] ONE-FACE PHYSICAL PREFIX REGRESSION")
_v28_one_face = frozenset((V23C_ROOT,))
V28_ONE_FACE = _v28_cluster_coefficients(_v28_one_face, V28_ORDER)
print(
    "  order-aware work: "
    f"inner={V28_ONE_FACE['w_inner_evals']:,}, "
    f"projection-reuse={V28_ONE_FACE['projection_reuses']:,}, "
    f"deep-self={V28_ONE_FACE['deep_self_evals']:,}, "
    f"Haar hit/miss={V28_ONE_FACE['haar_hits']:,}/"
    f"{V28_ONE_FACE['haar_misses']:,}, "
    f"build={V28_ONE_FACE['build_seconds']:.1f}s"
)
print(
    "  deepest Krylov self-block: "
    + ("COMPUTED (odd-order requirement)" if V28_ONE_FACE["deepest_self_required"]
       else "SKIPPED (even-order theorem)")
)
_v28_one_face_key = _v24c_shape_key(_v28_one_face)
if (
    "shape_cache" in globals()
    and _v28_one_face_key in shape_cache
    and len(shape_cache[_v28_one_face_key].get("coef", ())) >= 5
):
    _v28_one_face_old = shape_cache[_v28_one_face_key]
    print("  reused completed v10a.26 one-face coefficient cache")
else:
    if not V28_ALLOW_REFERENCE_REBUILD:
        raise RuntimeError(
            "completed v10a.26 one-face comparator is unavailable.  v10a.28 "
            "will not silently start its multi-minute rebuild; restore shape_cache "
            "or explicitly set V28_ALLOW_REFERENCE_REBUILD=1"
        )
    print("  WARNING: explicitly authorized v10a.26 one-face comparator rebuild")
    _v28_one_face_old = _v23c_fit_cluster(_v28_one_face)
V28_ONE_FACE_PREFIX_ERROR = float(
    np.max(np.abs(V28_ONE_FACE["coef"][:5] - _v28_one_face_old["coef"][:5]))
)
v28_gate(
    "generic Haar/Krylov engine reproduces the certified v10a.26 one-face prefix",
    V28_ONE_FACE_PREFIX_ERROR < 3e-9,
    f"max O4-prefix error={V28_ONE_FACE_PREFIX_ERROR:.3e}; "
    f"new layers={V28_ONE_FACE['one_layers']}/{V28_ONE_FACE['vac_layers']}",
)


# ---------------------------------------------------------------------------
# 4. Generic bidirectional support history census
# ---------------------------------------------------------------------------


def _v28_history_levels(max_depth, pol=None):
    pol = V23C_POL if pol is None else int(pol)
    root = int(anchor_faces[pol])
    levels = [{frozenset((root,)): _v10a3_face_state(root)}]
    for depth in range(1, int(max_depth) + 1):
        nxt, stats = _v17_apply_W_labeled(levels[-1], f"v28 unrestricted W{depth}")
        levels.append(nxt)
        print(
            f"  history depth {depth}: supports={len(nxt):,} "
            f"actions={stats['actions']:,} channels={stats['channels']:,}"
        )
    return levels


def _v28_support_census(order, pol=None, history_levels=None):
    order = int(order)
    pol = V23C_POL if pol is None else int(pol)
    root = int(anchor_faces[pol])
    left_depth = order // 2
    right_depth = order - left_depth
    if history_levels is None or len(history_levels) <= right_depth:
        history_levels = _v28_history_levels(right_depth, pol)
    supports, endpoints, stats = _v24c_candidate_supports(
        history_levels[left_depth], history_levels[right_depth],
        root, root, max_size=order + 2,
    )
    return supports, endpoints, stats, history_levels


def _v28_rooted_extent(C):
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


def _v28_census_signature():
    payload = (
        V28_SCHEMA, "support-census-v1", int(L), int(V23C_POL),
        int(V28_ORDER), int(V28_MARKED_SUPPORT_BOUND),
    )
    return hashlib.sha256(repr(payload).encode()).hexdigest()


def _v28_load_census():
    if not (
        V28_RESUME and V28_CENSUS_CHECKPOINT
        and os.path.exists(V28_CENSUS_CHECKPOINT)
    ):
        return None
    try:
        with open(V28_CENSUS_CHECKPOINT, "rb") as fh:
            payload = pickle.load(fh)
    except Exception as exc:
        print(f"  unreadable census checkpoint ignored: {exc}")
        return None
    if (
        payload.get("schema") != V28_SCHEMA
        or payload.get("signature") != _v28_census_signature()
    ):
        print("  incompatible census checkpoint ignored")
        return None
    return payload


def _v28_save_census(o4_supports, o4_stats, maxc, support_stats):
    if not V28_CENSUS_CHECKPOINT:
        return
    path = os.path.abspath(os.path.expanduser(V28_CENSUS_CHECKPOINT))
    parent = os.path.dirname(path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    tmp = path + ".tmp"
    payload = dict(
        schema=V28_SCHEMA, signature=_v28_census_signature(),
        o4_supports=set(o4_supports), o4_stats=o4_stats,
        maxc=set(maxc), support_stats=support_stats, saved_at=time.time(),
    )
    with open(tmp, "wb") as fh:
        pickle.dump(payload, fh, protocol=pickle.HIGHEST_PROTOCOL)
        fh.flush()
        os.fsync(fh.fileno())
    os.replace(tmp, path)


if V28_RUN_CENSUS:
    _v28_census_cache = _v28_load_census()
    _v28_prior_census = (
        _v28_census_cache is None
        and globals().get("V27_ORDER") == V28_ORDER
        and bool(globals().get("V27_MAXC"))
        and "V27_O4_SUPPORTS" in globals()
    )
    if _v28_prior_census:
        _v28_census_cache = dict(
            o4_supports=set(V27_O4_SUPPORTS),
            o4_stats=globals().get("V27_O4_STATS", {}),
            maxc=set(V27_MAXC),
            support_stats=globals().get("V27_SUPPORT_STATS", {}),
        )
        _v28_save_census(
            _v28_census_cache["o4_supports"],
            _v28_census_cache["o4_stats"],
            _v28_census_cache["maxc"],
            _v28_census_cache["support_stats"],
        )
        print(
            "\n  imported the completed in-memory v10a.27 support census "
            "and checkpointed it for v10a.28"
        )
    print("\n[3] GENERIC SUPPORT-CENSUS REGRESSION AT ORDER FOUR")
    if _v28_census_cache is None:
        _v28_histories = _v28_history_levels(
            max(2, V28_SUPPORT_HALF_DEPTH), V23C_POL,
        )
        V28_O4_SUPPORTS, _, V28_O4_STATS, _ = _v28_support_census(
            4, V23C_POL, _v28_histories
        )
    else:
        V28_O4_SUPPORTS = set(_v28_census_cache["o4_supports"])
        V28_O4_STATS = _v28_census_cache["o4_stats"]
        print(
            f"  loaded {len(V28_O4_SUPPORTS):,} O4 supports from "
            f"{V28_CENSUS_CHECKPOINT}"
        )
    if "MAXC" in globals():
        _v28_missing_o4 = set(MAXC) - set(V28_O4_SUPPORTS)
        v28_gate(
            "unrestricted bidirectional histories cover the certified O4 support corpus",
            not _v28_missing_o4,
            f"generic={len(V28_O4_SUPPORTS)}, certified={len(MAXC)}, "
            f"missing={len(_v28_missing_o4)}",
        )
    else:
        v28_gate(
            "completed O4 support corpus is available for regression",
            False, "MAXC missing",
        )

    print(f"\n[4] ORDER-{V28_ORDER} SUPPORT CENSUS")
    if _v28_census_cache is None:
        V28_MAXC, V28_ENDPOINT_SUPPORTS, V28_SUPPORT_STATS, _v28_histories = (
            _v28_support_census(V28_ORDER, V23C_POL, _v28_histories)
        )
        _v28_save_census(
            V28_O4_SUPPORTS, V28_O4_STATS, V28_MAXC, V28_SUPPORT_STATS,
        )
        print(f"  atomically saved support census to {V28_CENSUS_CHECKPOINT}")
    else:
        V28_MAXC = set(_v28_census_cache["maxc"])
        V28_ENDPOINT_SUPPORTS = set()
        V28_SUPPORT_STATS = _v28_census_cache["support_stats"]
        print(
            f"  loaded {len(V28_MAXC):,} order-{V28_ORDER} supports from "
            f"{V28_CENSUS_CHECKPOINT}"
        )
    v28_gate(
        "order-n support census is nonempty", bool(V28_MAXC), V28_SUPPORT_STATS,
    )

    _extent_rows = [(C,) + _v28_rooted_extent(C) for C in V28_MAXC]
    _boundary = [row for row in _extent_rows if row[2]]
    V28_MAX_EXTENT = max((row[1] for row in _extent_rows), default=0)
    v28_gate(
        "periodic geometry is free of half-box support aliases",
        not _boundary,
        f"L={L}, max centered extent={V28_MAX_EXTENT}, "
        f"boundary supports={len(_boundary)}",
    )

    V28_CLUSTERS = set()
    for C in V28_MAXC:
        V28_CLUSTERS.update(_v23c_rooted_connected_subsets(C))

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
    V28_CLUSTERS.update(_small)

    _downward_missing = []
    for C in V28_CLUSTERS:
        for S in _v23c_rooted_connected_subsets(C):
            if S not in V28_CLUSTERS:
                _downward_missing.append((C, S))
                break
    v28_gate(
        "order-n rooted cluster poset is downward closed",
        not _downward_missing,
        f"clusters={len(V28_CLUSTERS)}, maximal={len(V28_MAXC)}, "
        f"missing={len(_downward_missing)}",
    )
    V28_SHAPE_KEYS = {_v24c_shape_key(C) for C in V28_CLUSTERS}
    print("  concrete rooted clusters       :", len(V28_CLUSTERS))
    print("  rooted proper-rotation classes :", len(V28_SHAPE_KEYS))
    print(
        "  size histogram                 :",
        dict(sorted(Counter(map(len, V28_CLUSTERS)).items())),
    )
else:
    print("\n[3--4] SUPPORT CENSUS SKIPPED BY FIREWALL CONFIGURATION")
    print("  Set V28_RUN_CENSUS=1 explicitly to enumerate unrestricted histories.")
    V28_O4_SUPPORTS, V28_MAXC, V28_ENDPOINT_SUPPORTS = set(), set(), set()
    V28_O4_STATS, V28_SUPPORT_STATS = {}, {}
    V28_MAX_EXTENT, V28_CLUSTERS, V28_SHAPE_KEYS = 0, set(), set()
    v28_gate(
        "support census is disabled in the short firewall",
        V28_MODE == "firewall",
        "production remains locked until V28_RUN_CENSUS=1",
    )


# ---------------------------------------------------------------------------
# 5. Checkpointed production and rooted incidence transform
# ---------------------------------------------------------------------------


def _v28_signature():
    payload = (
        V28_SCHEMA, int(L), int(V23C_POL), int(V28_ORDER), int(V28_HAAR_CAP),
        tuple(sorted(map(repr, V28_SHAPE_KEYS))),
    )
    return hashlib.sha256(repr(payload).encode()).hexdigest()


V28_RUN_SIGNATURE = _v28_signature()


def _v28_save(cache):
    if not V28_CHECKPOINT:
        return
    path = os.path.abspath(os.path.expanduser(V28_CHECKPOINT))
    parent = os.path.dirname(path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    tmp = path + ".tmp"
    payload = dict(
        schema=V28_SCHEMA, signature=V28_RUN_SIGNATURE, order=V28_ORDER,
        haar_cap=V28_HAAR_CAP, shape_cache=cache, saved_at=time.time(),
    )
    with open(tmp, "wb") as fh:
        pickle.dump(payload, fh, protocol=pickle.HIGHEST_PROTOCOL)
        fh.flush()
        os.fsync(fh.fileno())
    os.replace(tmp, path)


def _v28_load():
    if not (V28_RESUME and V28_CHECKPOINT and os.path.exists(V28_CHECKPOINT)):
        return {}
    with open(V28_CHECKPOINT, "rb") as fh:
        payload = pickle.load(fh)
    if payload.get("schema") != V28_SCHEMA or payload.get("signature") != V28_RUN_SIGNATURE:
        print("  incompatible checkpoint ignored")
        return {}
    cache = {
        k: v for k, v in dict(payload.get("shape_cache", {})).items()
        if k in V28_SHAPE_KEYS
    }
    print(f"  resumed {len(cache)}/{len(V28_SHAPE_KEYS)} shapes from {V28_CHECKPOINT}")
    return cache


def _v28_lower_targets():
    return {
        0: 8.0 / 3.0,
        1: 1.0,
        2: 11.0 / 306.0,
        3: -109151.0 / 249696.0,
        4: -0.7751458630189173,
    }


def _v28_production():
    if not all(ok for _, ok, _ in V28_GATES):
        raise RuntimeError("v10a.28 preflight gate failure; production is blocked")
    cache = _v28_load()
    representatives = {}
    raw = {}
    duplicate_checks = 0
    max_offdiag = 0.0
    t0 = time.time()
    new_shapes = 0
    ordered = sorted(V28_CLUSTERS, key=lambda C: (len(C), _v24c_shape_key(C), tuple(sorted(C))))

    def budget_stop(reason):
        _v28_save(cache)
        print(
            f"\n[BUDGET STOP] {reason}; saved "
            f"{len(cache)}/{len(V28_SHAPE_KEYS)} shapes. "
            "Rerun the identical production command to resume.",
            flush=True,
        )
        return dict(
            complete=False, schema=V28_SCHEMA,
            signature=V28_RUN_SIGNATURE, order=V28_ORDER,
            completed_shapes=len(cache), total_shapes=len(V28_SHAPE_KEYS),
            newly_computed_shapes=new_shapes,
            checkpoint=V28_CHECKPOINT, target_loaded=False,
        )

    try:
        for C in ordered:
            key = _v24c_shape_key(C)
            representatives.setdefault(key, C)
            if key not in cache:
                elapsed = time.time() - t0
                if V28_MAX_NEW_SHAPES > 0 and new_shapes >= V28_MAX_NEW_SHAPES:
                    return budget_stop(
                        f"per-invocation limit of {V28_MAX_NEW_SHAPES} new shape(s) reached"
                    )
                if (
                    V28_TIME_BUDGET_MINUTES > 0
                    and new_shapes > 0
                    and elapsed >= 60.0 * V28_TIME_BUDGET_MINUTES
                ):
                    return budget_stop(
                        f"{V28_TIME_BUDGET_MINUTES:g}-minute between-shape budget reached"
                    )
                print(
                    f"  shape START {len(cache)+1}/{len(V28_SHAPE_KEYS)} |C|={len(C)}; "
                    f"this shape runs to its atomic checkpoint",
                    flush=True,
                )
                item = _v28_cluster_coefficients(C, V28_ORDER)
                cache[key] = item
                new_shapes += 1
                _v28_save(cache)
                dt = time.time() - t0
                done, remaining = len(cache), len(V28_SHAPE_KEYS) - len(cache)
                eta = (dt / max(new_shapes, 1)) * remaining
                print(
                    f"  shape DONE  {done}/{len(V28_SHAPE_KEYS)} |C|={len(C)} "
                    f"dim={item['one_dim']}/{item['vac_dim']} "
                    f"layers={item['one_layers']}/{item['vac_layers']} "
                    f"inner={item['w_inner_evals']:,} reuse={item['projection_reuses']:,} "
                    f"deep={item['deep_self_evals']:,} Haar={item['haar_hits']:,}/"
                    f"{item['haar_misses']:,} SW={item['sw_backend']} "
                    f"c{V28_ORDER}={item['coef'][V28_ORDER]:+.12g} "
                    f"SWoff={item['sw_offdiag']:.2e} elapsed={dt:.1f}s ETA~{eta:.1f}s",
                    flush=True,
                )
            item = cache[key]
            max_offdiag = max(max_offdiag, float(item["sw_offdiag"]))
            if duplicate_checks < V28_DUPLICATE_CHECKS and C != representatives[key]:
                other = _v28_cluster_coefficients(C, V28_ORDER)
                err = float(np.max(np.abs(other["coef"] - item["coef"])))
                v28_gate(
                    f"rooted proper-rotation duplicate #{duplicate_checks+1}",
                    err < 3e-9, f"max coefficient error={err:.3e}",
                )
                duplicate_checks += 1
            raw[C] = np.asarray(item["coef"], dtype=np.float64).copy()
    except KeyboardInterrupt:
        _v28_save(cache)
        print(f"\n[SAFE INTERRUPT] saved {len(cache)}/{len(V28_SHAPE_KEYS)} shapes")
        raise

    v28_gate(
        f"exact SW block diagonalization closes through O(u^{V28_ORDER})",
        max_offdiag < V28_SW_TOL, f"max P-Q residual={max_offdiag:.3e}",
    )
    v28_gate(
        "every rooted shape has a coefficient",
        len(cache) == len(V28_SHAPE_KEYS), f"{len(cache)}/{len(V28_SHAPE_KEYS)}",
    )

    omega = {}
    totals = np.zeros(V28_ORDER + 1, dtype=np.float64)
    by_size = defaultdict(lambda: np.zeros(V28_ORDER + 1, dtype=np.float64))
    for C in sorted(V28_CLUSTERS, key=lambda x: (len(x), tuple(sorted(x)))):
        z = raw[C].copy()
        for S in _v23c_rooted_connected_subsets(C):
            if S != C:
                z -= omega[S]
        omega[C] = z
        totals += z
        by_size[len(C)] += z

    print("\nROOTED INCIDENCE TRANSFORM")
    for size in sorted(by_size):
        row = " ".join(f"m{k}={by_size[size][k]:+.12g}" for k in range(1, V28_ORDER + 1))
        print(f"  size {size}: {row}")
    print("  TOTAL:", " ".join(f"m{k}={totals[k]:+.15g}" for k in range(V28_ORDER + 1)))

    for k, target in _v28_lower_targets().items():
        if k >= V28_ORDER:
            continue
        tol = 2e-8 if k <= 2 else (2e-7 if k == 3 else 2e-6)
        v28_gate(
            f"rooted oracle reproduces protected lower coefficient m{k}",
            abs(totals[k] - target) < tol,
            f"got={totals[k]:+.15g}, error={totals[k]-target:+.3e}",
        )

    if not all(ok for _, ok, _ in V28_GATES):
        raise RuntimeError("v10a.28 production completed but a hard gate failed; do not unblind")
    result = dict(
        schema=V28_SCHEMA, signature=V28_RUN_SIGNATURE, order=V28_ORDER,
        coefficients=totals, by_size=dict(by_size), omega=omega,
        concrete_clusters=len(V28_CLUSTERS), shapes=len(V28_SHAPE_KEYS),
        haar_cap=V28_HAAR_CAP, krylov_depth=V28_KRYLOV_DEPTH,
        target_loaded=False,
    )
    print("\nBLIND PRODUCTION RESULT")
    print(f"  m{V28_ORDER} = {totals[V28_ORDER]!r}")
    print("  external target was not loaded; compare only in a separate verifier")
    return result


print("\n[5] PREFLIGHT SUMMARY")
for i, (name, ok, detail) in enumerate(V28_GATES, 1):
    print(f"{i:02d}. {'PASS' if ok else 'FAIL'} -- {name}" + (f" :: {detail}" if detail else ""))
print(f"PASSED {sum(int(ok) for _, ok, _ in V28_GATES)}/{len(V28_GATES)} PREFLIGHT GATES")

V28_RESULT = None
if V28_MODE == "production":
    V28_RESULT = _v28_production()
else:
    print(
        "\nFIREWALL ONLY.  No support census or production shapes were started.\n"
        "For production, rerun this source in the post-v10a.26 namespace "
        "(a completed in-memory v10a.27 census may remain loaded) with "
        "V28_RUN_CENSUS=1, V28_MODE=production, and the exact "
        f"confirmation V28_PRODUCTION_CONFIRM=YES_ORDER_{V28_ORDER}.\n"
        "The requested-order external target remains absent; lower-order "
        "regression locks are present."
    )
