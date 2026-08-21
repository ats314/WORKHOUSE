#!/usr/bin/env python3
# =====================================================================
# ENGINE_TROM_su3_o3_tromino_weight_extractor_v1.py
#
# Purpose
#   Extraction/validation harness for O(y^3) tromino weights in the
#   C-odd plaquette flat-band problem.
#
# What this script does
#   1. Builds the exact periodic cubical plaquette/link incidence geometry.
#   2. Classifies every ordered two-hop plaquette path into tromino classes.
#   3. Extracts class weights from one of four sources:
#        --mode primitive       : W_path+=2/9, W_path-=2/9, W_corner=2/27.
#        --mode equal           : equal protected lifter weights.
#        --mode custom          : JSON class->weight map.
#        --mode resolvent-json  : finite Rayleigh-Schroedinger kernel JSON.
#        --mode haar-moment     : exploratory SU(3) Haar cluster-moment audit.
#   4. Applies the resulting weights to the flat C-odd branch and reports
#      the O(y^3) Rayleigh correction alpha(k), bandwidth, and protection test.
#
# Critical scope
#   This is deliberately fail-closed.  It does NOT pretend that the primitive
#   weights are the physical SU(3) third-order weights.  The only mode that can
#   be treated as a physical extractor is --mode resolvent-json with a kernel
#   JSON whose matrix elements actually came from the SU(3) local/channel
#   calculation, including normalization and subtraction terms.
#
# Usage
#   python ENGINE_TROM_su3_o3_tromino_weight_extractor_v1.py --mode primitive
#   python ENGINE_TROM_su3_o3_tromino_weight_extractor_v1.py --mode equal --equal-weight 1
#   python ENGINE_TROM_su3_o3_tromino_weight_extractor_v1.py --mode custom \
#       --weights-json '{"path_bent_or_straight_prod+1":"2/9", "path_bent_or_straight_prod-1":"2/9", "triangle_corner_cyc-1":"2/27"}'
#   python ENGINE_TROM_su3_o3_tromino_weight_extractor_v1.py --make-kernel-template kernel_template.json
#   python ENGINE_TROM_su3_o3_tromino_weight_extractor_v1.py --mode resolvent-json --kernel-json kernel_template.json
#   python ENGINE_TROM_su3_o3_tromino_weight_extractor_v1.py --mode primitive --emit-json out.json
#
# Notes on resolvent-json mode
#   The finite-kernel schema is intentionally minimal.  For each tromino class c,
#   the weight is computed as
#
#       W_c = normalization_c * ( direct_00_c
#              + sum_n left_c[n] * right_c[n] / (E_source - E_n)
#              - sum_j subtraction_c[j] )
#
#   This mirrors the finite Rayleigh-Schroedinger structure: direct term plus
#   reduced-resolvent terms minus subtractions.  The JSON must provide the
#   state energies and class-specific matrix elements.  This script then does
#   the exact class-weight contraction and the flat-band lift diagnostic.
# =====================================================================

from __future__ import annotations

import argparse
import itertools
import json
import math
import os
from collections import Counter, defaultdict
from fractions import Fraction as F
from typing import Any, Dict, Iterable, List, Mapping, Optional, Sequence, Tuple

import numpy as np

np.set_printoptions(precision=10, suppress=True)

# ---------------------------------------------------------------------
# Constants and class inventory
# ---------------------------------------------------------------------

ORIENT = [(0, 1), (0, 2), (1, 2)]  # xy, xz, yz
ONAME = {0: "xy", 1: "xz", 2: "yz"}

CLASSES_ORDER = [
    "backtrack_2plaquette",
    "path_bent_or_straight_prod+1",
    "path_bent_or_straight_prod-1",
    "triangle_corner_cyc-1",
    "triangle_same_link_cyc+1",
]

LIFTER_CLASSES = [
    "path_bent_or_straight_prod+1",
    "path_bent_or_straight_prod-1",
    "triangle_corner_cyc-1",
]

PRIMITIVE_CANDIDATE = {
    "backtrack_2plaquette": F(0, 1),
    "path_bent_or_straight_prod+1": F(2, 9),
    "path_bent_or_straight_prod-1": F(2, 9),
    "triangle_corner_cyc-1": F(2, 27),
    "triangle_same_link_cyc+1": F(0, 1),
}

ZERO_WEIGHTS = {cls: F(0, 1) for cls in CLASSES_ORDER}

# ---------------------------------------------------------------------
# Small gate/report helpers
# ---------------------------------------------------------------------

PASS: List[Tuple[str, bool]] = []


def gate(name: str, cond: bool, fatal: bool = True) -> None:
    PASS.append((name, bool(cond)))
    print(f"  GATE {'PASS' if cond else 'FAIL'} :: {name}")
    if fatal and not cond:
        raise SystemExit(f"GATE FAILED: {name}")


def warn(msg: str) -> None:
    print(f"  WARNING: {msg}")

# ---------------------------------------------------------------------
# Exact rational parsing
# ---------------------------------------------------------------------


def parse_fraction(x: Any) -> F:
    if isinstance(x, F):
        return x
    if isinstance(x, bool):
        raise ValueError(f"cannot parse boolean as fraction: {x!r}")
    if isinstance(x, int):
        return F(x, 1)
    if isinstance(x, float):
        return F(str(x)).limit_denominator(10**12)
    if isinstance(x, str):
        s = x.strip()
        if not s:
            raise ValueError("empty fraction string")
        return F(s)
    raise ValueError(f"cannot parse fraction from {x!r}")


def parse_weights_json(arg: Optional[str]) -> Dict[str, F]:
    weights = dict(ZERO_WEIGHTS)
    if arg is None:
        return weights
    obj = json.loads(arg)
    if not isinstance(obj, dict):
        raise ValueError("--weights-json must be a JSON object mapping class names to rational values")
    for k, v in obj.items():
        if k not in CLASSES_ORDER:
            raise ValueError(f"unknown class {k!r}; expected one of {CLASSES_ORDER}")
        weights[k] = parse_fraction(v)
    return weights


def format_frac(x: F) -> str:
    return str(x.numerator) if x.denominator == 1 else f"{x.numerator}/{x.denominator}"

# ---------------------------------------------------------------------
# Cubical complex
# ---------------------------------------------------------------------


def shift(x: Tuple[int, int, int], d: int, L: int, n: int = 1) -> Tuple[int, int, int]:
    z = list(x)
    z[d] = (z[d] + n) % L
    return tuple(z)  # type: ignore[return-value]


def centered_displacement(x: Tuple[int, int, int], y: Tuple[int, int, int], L: int) -> Tuple[int, int, int]:
    return tuple(((y[i] - x[i] + L // 2) % L) - L // 2 for i in range(3))  # type: ignore[return-value]


def boundary(x: Tuple[int, int, int], o: int, L: int) -> List[Tuple[Tuple[Tuple[int, int, int], int], int]]:
    mu, nu = ORIENT[o]
    x = tuple(x)
    return [
        ((x, mu), +1),
        ((shift(x, mu, L), nu), +1),
        ((shift(x, nu, L), mu), -1),
        ((x, nu), -1),
    ]


def build_complex(L: int):
    if L < 5:
        raise ValueError("Use L>=5. Smaller periodic boxes can alias some tromino displacements.")
    plaqs = [(x, o) for x in itertools.product(range(L), repeat=3) for o in range(3)]
    pidx = {p: i for i, p in enumerate(plaqs)}
    link_inc: Dict[Tuple[Tuple[int, int, int], int], List[Tuple[int, int]]] = defaultdict(list)
    for p in plaqs:
        i = pidx[p]
        for ln, sg in boundary(p[0], p[1], L):
            link_inc[ln].append((i, sg))

    nbrs: Dict[int, Dict[int, Tuple[int, Tuple[Tuple[int, int, int], int]]]] = {i: {} for i in range(len(plaqs))}
    for ln, inc in link_inc.items():
        for (i, si), (j, sj) in itertools.combinations(inc, 2):
            if j in nbrs[i] or i in nbrs[j]:
                raise RuntimeError("two plaquettes share more than one link; geometry convention broken")
            nbrs[i][j] = (si * sj, ln)
            nbrs[j][i] = (si * sj, ln)
    return plaqs, pidx, link_inc, nbrs


def common_links(bsets: Sequence[set], indices: Sequence[int]) -> set:
    s = bsets[indices[0]].copy()
    for i in indices[1:]:
        s &= bsets[i]
    return s


def classify_path(i: int, q: int, r: int, nbrs: Mapping[int, Mapping[int, Tuple[int, Any]]], bsets: Sequence[set]) -> str:
    if r == i:
        return "backtrack_2plaquette"
    s1 = nbrs[i][q][0]
    s2 = nbrs[q][r][0]
    prod = s1 * s2
    adj_ir = r in nbrs[i]
    com3 = common_links(bsets, [i, q, r])
    if adj_ir:
        cyc = s1 * s2 * nbrs[r][i][0]
        if len(com3) == 1:
            return f"triangle_same_link_cyc{cyc:+d}"
        return f"triangle_corner_cyc{cyc:+d}"
    if len(com3) == 1:
        # This class is absent in the expected five-class inventory for the
        # oriented plaquette complex used here, but keep the label explicit if
        # a convention change ever produces it.
        return f"path_common_link_prod{prod:+d}"
    return f"path_bent_or_straight_prod{prod:+d}"


def build_terms(L: int):
    plaqs, pidx, link_inc, nbrs = build_complex(L)
    NP = len(plaqs)
    bsets = [set(ln for ln, _ in boundary(x, o, L)) for x, o in plaqs]

    # Single-hop signed adjacency counter S(k).
    single = Counter()
    for i in range(NP):
        xi, oi = plaqs[i]
        for j, (s, _) in nbrs[i].items():
            xj, oj = plaqs[j]
            d = centered_displacement(xi, xj, L)
            single[(oi, oj, d, s)] += 1

    # Ordered two-hop class counters.
    class_terms: Dict[str, Counter] = defaultdict(Counter)
    class_counts = Counter()
    root_counts: Dict[int, Counter] = defaultdict(Counter)
    representatives: Dict[str, Tuple[int, int, int]] = {}

    for i in range(NP):
        xi, oi = plaqs[i]
        for q, (s1, _) in nbrs[i].items():
            for r, (s2, _) in nbrs[q].items():
                cls = classify_path(i, q, r, nbrs, bsets)
                representatives.setdefault(cls, (i, q, r))
                xr, orr = plaqs[r]
                d = centered_displacement(xi, xr, L)
                signprod = s1 * s2
                class_terms[cls][(oi, orr, d, signprod)] += 1
                class_counts[cls] += 1
                root_counts[oi][cls] += 1

    return plaqs, link_inc, nbrs, single, class_terms, class_counts, root_counts, representatives

# ---------------------------------------------------------------------
# Fourier-space flat-band diagnostic
# ---------------------------------------------------------------------


def eval_counter(counter: Counter, k: np.ndarray, L: int) -> np.ndarray:
    M = np.zeros((3, 3), dtype=complex)
    for (o, oj, d, s), multiplicity in counter.items():
        phase = np.exp(1j * np.dot(np.asarray(k), np.asarray(d)))
        M[o, oj] += (multiplicity / (L ** 3)) * s * phase
    return M


def flat_vector(k: np.ndarray) -> np.ndarray:
    u = [1 - np.exp(1j * q) for q in k]
    return np.array([np.conjugate(u[2]), -np.conjugate(u[1]), np.conjugate(u[0])], dtype=complex)


def weighted_matrix(class_terms: Mapping[str, Counter], weights: Mapping[str, F], k: np.ndarray, L: int) -> np.ndarray:
    M = np.zeros((3, 3), dtype=complex)
    for cls, val in weights.items():
        if cls not in class_terms:
            continue
        if val != 0:
            M += float(val) * eval_counter(class_terms[cls], k, L)
    return M


def rayleigh_on_flat(class_terms: Mapping[str, Counter], weights: Mapping[str, F], k: np.ndarray, L: int):
    w = flat_vector(k)
    nrm = np.vdot(w, w).real
    if nrm < 1e-12:
        return None
    M = weighted_matrix(class_terms, weights, k, L)
    Mw = M @ w
    alpha = np.vdot(w, Mw) / nrm
    resid = np.linalg.norm(Mw - alpha * w) / (np.linalg.norm(Mw) + 1e-15)
    return float(alpha.real), float(abs(alpha.imag)), float(resid)


def equal_lifter_condition(weights: Mapping[str, F]) -> bool:
    vals = [weights[c] for c in LIFTER_CLASSES]
    return vals[0] == vals[1] == vals[2]


def finite_epsilon_check(single_counter: Counter, class_terms: Mapping[str, Counter], weights: Mapping[str, F], ks: np.ndarray, L: int, eps: float = 1e-7):
    worst = 0.0
    used = 0
    for k in ks:
        w = flat_vector(k)
        if np.linalg.norm(w) < 1e-9:
            continue
        S = eval_counter(single_counter, k, L)
        evS = np.linalg.eigvalsh(S)
        gap = np.partition(np.abs(evS + 4.0), 1)[1]
        if gap < 0.25:
            continue
        out = rayleigh_on_flat(class_terms, weights, k, L)
        if out is None:
            continue
        alpha, _, _ = out
        M = weighted_matrix(class_terms, weights, k, L)
        ev = np.linalg.eigvalsh(S + eps * M)
        nearest = ev[np.argmin(np.abs(ev + 4.0))]
        err = abs((nearest + 4.0) / eps - alpha)
        worst = max(worst, float(err))
        used += 1
    return used, worst

# ---------------------------------------------------------------------
# Finite Rayleigh-Schroedinger kernel extraction
# ---------------------------------------------------------------------


def make_kernel_template(path: str) -> None:
    template = {
        "description": "Template for finite SU(3) O(y^3) C-odd tromino kernel. Fill matrix elements from the physical local/channel calculation.",
        "physical_su3_o3_kernel": False,
        "normalization_convention": "W_c = normalization*(direct_00 + sum_n left[n]*right[n]/(E_source-E_n) - sum(subtractions))",
        "source_state": "Codd_source_p3",
        "states": [
            {"name": "Codd_source_p3", "energy": "3"},
            {"name": "intermediate_1", "energy": "5"},
            {"name": "intermediate_2", "energy": "7"},
        ],
        "classes": {
            cls: {
                "direct_00": "0",
                "left": {"intermediate_1": "0", "intermediate_2": "0"},
                "right": {"intermediate_1": "0", "intermediate_2": "0"},
                "subtractions": ["0"],
                "normalization": "1",
            }
            for cls in CLASSES_ORDER
        },
    }
    # Put the primitive numbers in comments cannot be done in JSON, so add a hint key.
    template["primitive_candidate_hint"] = {
        "path_bent_or_straight_prod+1": "2/9",
        "path_bent_or_straight_prod-1": "2/9",
        "triangle_corner_cyc-1": "2/27",
    }
    with open(path, "w", encoding="utf-8") as f:
        json.dump(template, f, indent=2, sort_keys=True)
    print(f"wrote kernel template: {path}")


def extract_weights_from_resolvent_json(path: str) -> Tuple[Dict[str, F], Dict[str, Any]]:
    with open(path, "r", encoding="utf-8") as f:
        obj = json.load(f)
    if not isinstance(obj, dict):
        raise ValueError("kernel JSON must be an object")

    source = obj.get("source_state")
    if not source:
        raise ValueError("kernel JSON missing source_state")
    states = obj.get("states")
    if not isinstance(states, list):
        raise ValueError("kernel JSON missing states list")

    energies: Dict[str, F] = {}
    for st in states:
        if not isinstance(st, dict) or "name" not in st or "energy" not in st:
            raise ValueError("each state must have name and energy")
        energies[str(st["name"])] = parse_fraction(st["energy"])
    if source not in energies:
        raise ValueError(f"source_state {source!r} not present in states")
    E0 = energies[source]

    classes = obj.get("classes")
    if not isinstance(classes, dict):
        raise ValueError("kernel JSON missing classes object")

    weights = dict(ZERO_WEIGHTS)
    details: Dict[str, Any] = {
        "physical_su3_o3_kernel": bool(obj.get("physical_su3_o3_kernel", False)),
        "source_state": source,
        "class_contributions": {},
    }

    for cls in CLASSES_ORDER:
        cobj = classes.get(cls, {})
        if not isinstance(cobj, dict):
            raise ValueError(f"class {cls} entry must be an object")
        direct = parse_fraction(cobj.get("direct_00", "0"))
        norm = parse_fraction(cobj.get("normalization", "1"))
        subtractions = [parse_fraction(x) for x in cobj.get("subtractions", [])]
        left = {str(k): parse_fraction(v) for k, v in cobj.get("left", {}).items()}
        right = {str(k): parse_fraction(v) for k, v in cobj.get("right", {}).items()}
        keys = sorted(set(left) | set(right))
        resolvent = F(0, 1)
        terms = []
        for st in keys:
            if st == source:
                continue
            if st not in energies:
                raise ValueError(f"class {cls} references unknown state {st!r}")
            denom = E0 - energies[st]
            if denom == 0:
                raise ZeroDivisionError(f"class {cls}, state {st}: reduced-resolvent denominator is zero")
            lv = left.get(st, F(0, 1))
            rv = right.get(st, F(0, 1))
            contrib = lv * rv / denom
            resolvent += contrib
            terms.append({"state": st, "left": format_frac(lv), "right": format_frac(rv), "denominator": format_frac(denom), "contribution": format_frac(contrib)})
        subtraction_total = sum(subtractions, F(0, 1))
        total = norm * (direct + resolvent - subtraction_total)
        weights[cls] = total
        details["class_contributions"][cls] = {
            "direct_00": format_frac(direct),
            "resolvent": format_frac(resolvent),
            "subtraction_total": format_frac(subtraction_total),
            "normalization": format_frac(norm),
            "weight": format_frac(total),
            "terms": terms,
        }
    return weights, details

# ---------------------------------------------------------------------
# Exploratory SU(3) Haar cluster moment audit
# ---------------------------------------------------------------------


def haar_su3(rng: np.random.Generator) -> np.ndarray:
    z = (rng.normal(size=(3, 3)) + 1j * rng.normal(size=(3, 3))) / math.sqrt(2.0)
    q, r = np.linalg.qr(z)
    d = np.diag(r)
    ph = d / np.abs(d)
    q = q * ph.conjugate()
    det = np.linalg.det(q)
    q = q / (det ** (1.0 / 3.0))
    return q


def plaquette_matrix(plaq: Tuple[Tuple[int, int, int], int], U: Mapping[Tuple[Tuple[int, int, int], int], np.ndarray], L: int) -> np.ndarray:
    M = np.eye(3, dtype=complex)
    for ln, sg in boundary(plaq[0], plaq[1], L):
        A = U[ln]
        if sg < 0:
            A = A.conjugate().T
        M = M @ A
    return M


def haar_cluster_moment_weights(plaqs: Sequence[Tuple[Tuple[int, int, int], int]], representatives: Mapping[str, Tuple[int, int, int]], L: int, nsamples: int, seed: int) -> Tuple[Dict[str, F], Dict[str, Any]]:
    """Exploratory local moment: E[ImTr(P_i) ReTr(P_q) ImTr(P_r)].

    This is not the final physical resolvent weight.  It is included to test
    whether a naive local Haar cluster moment already distinguishes the three
    lifter geometries.  The output weights are rationalized floating estimates;
    use only as a diagnostic.
    """
    rng = np.random.default_rng(seed)
    weights = dict(ZERO_WEIGHTS)
    details: Dict[str, Any] = {"scope": "exploratory Haar moment only; not final physical SU(3) O(y^3) weight", "moments": {}}

    # Reference variance for a single plaquette ImTr, estimated on independent Haar.
    ref_vals = []
    for _ in range(max(1000, min(nsamples, 5000))):
        U = haar_su3(rng)
        ref_vals.append(float(np.trace(U).imag ** 2))
    ref_var = float(np.mean(ref_vals))
    if ref_var <= 1e-14:
        raise RuntimeError("bad Haar variance estimate")

    for cls in CLASSES_ORDER:
        if cls not in representatives:
            continue
        triple = representatives[cls]
        links = sorted({ln for idx in triple for ln, _ in boundary(plaqs[idx][0], plaqs[idx][1], L)})
        vals = []
        for _ in range(nsamples):
            U = {ln: haar_su3(rng) for ln in links}
            mats = [plaquette_matrix(plaqs[idx], U, L) for idx in triple]
            val = float(np.trace(mats[0]).imag * np.trace(mats[1]).real * np.trace(mats[2]).imag)
            vals.append(val)
        mean = float(np.mean(vals))
        stderr = float(np.std(vals, ddof=1) / math.sqrt(max(1, nsamples)))
        normalized = mean / ref_var
        # Rationalization is for display only.  Keep denominator bounded.
        weights[cls] = F(normalized).limit_denominator(10**6)
        details["moments"][cls] = {
            "representative_indices": list(triple),
            "representative_plaquettes": [str(plaqs[idx]) for idx in triple],
            "links": len(links),
            "mean": mean,
            "stderr": stderr,
            "imtr_variance_reference": ref_var,
            "normalized_mean": normalized,
            "rationalized_weight": format_frac(weights[cls]),
        }
    return weights, details

# ---------------------------------------------------------------------
# Main diagnostic runner
# ---------------------------------------------------------------------


def run_flat_diagnostic(weights: Mapping[str, F], args: argparse.Namespace, extraction_details: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
    print("=" * 78)
    print("SU(3) O(y^3) TROMINO WEIGHT EXTRACTOR / FLAT-BRANCH DIAGNOSTIC")
    print("=" * 78)
    print(f"  mode={args.mode}; L={args.L}; samples={args.samples}; grid={args.grid}^3")
    print("  extracted/applied weights:")
    for cls in CLASSES_ORDER:
        print(f"    {cls:32s} : {format_frac(weights.get(cls, F(0, 1))):>16s} = {float(weights.get(cls, F(0, 1))):+.12g}")

    if args.mode == "primitive":
        warn("primitive mode reproduces the candidate hypothesis; it is not a physical SU(3) resolvent certificate")
    if args.mode == "haar-moment":
        warn("haar-moment mode is exploratory; it is not the physical reduced-resolvent extractor")
    if args.mode == "resolvent-json" and extraction_details and not extraction_details.get("physical_su3_o3_kernel", False):
        warn("kernel JSON is not marked physical_su3_o3_kernel=true; treat output as algebraic plumbing, not a physical certificate")

    plaqs, link_inc, nbrs, single, class_terms, class_counts, root_counts, representatives = build_terms(args.L)
    NP = len(plaqs)

    print("=" * 78)
    print("STEP 1: geometry gates")
    print("=" * 78)
    gate("every link lies in 4 plaquettes with signs (+,+,-,-)",
         all(len(v) == 4 and sorted(s for _, s in v) == [-1, -1, 1, 1] for v in link_inc.values()))
    gate("every plaquette has exactly 12 shared-link neighbors",
         all(len(nbrs[i]) == 12 for i in range(NP)))
    gate("observed two-hop class set is the expected five-class tromino inventory",
         set(class_terms.keys()) == set(CLASSES_ORDER))
    gate("two-hop class counts are orbital-uniform",
         all(root_counts[0] == root_counts[o] for o in range(1, 3)))

    print("  count per source plaquette:")
    for cls in CLASSES_ORDER:
        print(f"    {cls:32s} : {class_counts[cls] // NP:3d}")

    print("  representatives:")
    for cls in CLASSES_ORDER:
        tri = representatives.get(cls)
        if tri is None:
            continue
        rep = [f"{ONAME[plaqs[idx][1]]}@{plaqs[idx][0]}" for idx in tri]
        print(f"    {cls:32s} : {rep}")

    rng = np.random.default_rng(args.seed)
    ks = rng.uniform(0.31, 2 * np.pi - 0.31, size=(args.samples, 3))

    print("=" * 78)
    print("STEP 2: O(y^2) flat-band base gate")
    print("=" * 78)
    max_s_resid = 0.0
    for k in ks[: min(96, args.samples)]:
        w = flat_vector(k)
        S = eval_counter(single, k, args.L)
        max_s_resid = max(max_s_resid, np.linalg.norm(S @ w + 4.0 * w) / (np.linalg.norm(w) + 1e-15))
    gate(f"signed adjacency has exact flat vector numerically (max residual {max_s_resid:.2e})", max_s_resid < 1e-11)

    print("=" * 78)
    print("STEP 3: equal-lifter protection test")
    print("=" * 78)
    protected = equal_lifter_condition(weights)
    print(f"  equal-lifter condition W_path+ = W_path- = W_corner: {protected}")
    print(f"    W_path+  = {format_frac(weights['path_bent_or_straight_prod+1'])}")
    print(f"    W_path-  = {format_frac(weights['path_bent_or_straight_prod-1'])}")
    print(f"    W_corner = {format_frac(weights['triangle_corner_cyc-1'])}")

    equal_test = dict(ZERO_WEIGHTS)
    for c in LIFTER_CLASSES:
        equal_test[c] = F(1, 1)
    spreads_equal = []
    resids_equal = []
    for k in ks[: min(96, args.samples)]:
        out = rayleigh_on_flat(class_terms, equal_test, k, args.L)
        if out is not None:
            a, _, r = out
            spreads_equal.append(a)
            resids_equal.append(r)
    gate("equal lifter weights give constant flat-line correction", max(spreads_equal) - min(spreads_equal) < 1e-10)
    gate("equal lifter weights preserve the flat line", max(resids_equal) < 1e-10)

    print("=" * 78)
    print("STEP 4: O(y^3) flat-branch first-order correction")
    print("=" * 78)
    alphas: List[float] = []
    imags: List[float] = []
    resids: List[float] = []
    for k in ks:
        out = rayleigh_on_flat(class_terms, weights, k, args.L)
        if out is not None:
            a, im, r = out
            alphas.append(a)
            imags.append(im)
            resids.append(r)
    if not alphas:
        raise RuntimeError("no valid flat-branch samples")
    amin, amax = min(alphas), max(alphas)
    spread = amax - amin
    print(f"  sampled alpha(k): min={amin:+.12g}, max={amax:+.12g}, spread={spread:.12g}")
    print(f"  max imaginary leakage in alpha(k): {max(imags):.3e}")
    print(f"  max flat-line residual ||Mw-alpha w||/||Mw||: {max(resids):.3e}")
    gate("Rayleigh corrections are real to numerical precision", max(imags) < 1e-10)
    if protected:
        gate("protected weights have zero sampled bandwidth", spread < 1e-9)
    else:
        gate("nonprotected weights show sampled bandwidth", spread > 1e-6, fatal=False)

    high_sym = {
        "X(pi,0,0)": (math.pi, 0.0, 0.0),
        "M(pi,pi,0)": (math.pi, math.pi, 0.0),
        "R(pi,pi,pi)": (math.pi, math.pi, math.pi),
        "generic(pi/2,pi/3,pi/5)": (math.pi / 2, math.pi / 3, math.pi / 5),
    }
    print("  high-symmetry/reference alpha(k):")
    high_out = {}
    for name, kval in high_sym.items():
        out = rayleigh_on_flat(class_terms, weights, np.asarray(kval), args.L)
        if out is None:
            continue
        a, im, r = out
        high_out[name] = {"alpha": a, "imag": im, "residual": r}
        print(f"    {name:24s}: alpha={a:+.12g}, residual={r:.3e}")

    print("=" * 78)
    print("STEP 5: finite-epsilon branch-tracking sanity")
    print("=" * 78)
    used, worst = finite_epsilon_check(single, class_terms, weights, ks, args.L, eps=args.eps)
    print(f"  generic samples used={used}; worst |finite-difference shift - Rayleigh|={worst:.3e}")
    gate("enough nondegenerate generic samples for branch check", used >= min(20, max(1, args.samples // 4)))
    gate("finite-epsilon eigenvalue shift matches Rayleigh prediction", worst < 1e-5)

    print("=" * 78)
    print("STEP 6: rough Brillouin-zone grid extrema")
    print("=" * 78)
    grid = np.linspace(0, 2 * math.pi, args.grid, endpoint=False)
    vals = []
    for k1 in grid:
        for k2 in grid:
            for k3 in grid:
                out = rayleigh_on_flat(class_terms, weights, np.asarray((k1, k2, k3)), args.L)
                if out is not None:
                    vals.append(out[0])
    gmin, gmax = min(vals), max(vals)
    print(f"  grid alpha(k): min={gmin:+.12g}, max={gmax:+.12g}, width={gmax - gmin:.12g}")
    if protected:
        gate("grid confirms protected zero bandwidth", gmax - gmin < 1e-9)
    else:
        gate("grid detects nonzero candidate bandwidth", gmax - gmin > 1e-6, fatal=False)

    result = {
        "mode": args.mode,
        "scope": "physical only if mode=resolvent-json and supplied kernel is a real SU(3) O(y^3) reduced-resolvent/channel kernel",
        "weights": {cls: format_frac(weights.get(cls, F(0, 1))) for cls in CLASSES_ORDER},
        "equal_lifter_condition": protected,
        "sample_alpha_min": amin,
        "sample_alpha_max": amax,
        "sample_alpha_spread": spread,
        "sample_max_flat_line_residual": max(resids),
        "grid_alpha_min": gmin,
        "grid_alpha_max": gmax,
        "grid_alpha_width": gmax - gmin,
        "high_symmetry": high_out,
        "finite_epsilon_samples_used": used,
        "finite_epsilon_worst_error": worst,
        "passes": sum(1 for _, ok in PASS if ok),
        "gates_total": len(PASS),
        "extraction_details": extraction_details or {},
    }

    if args.emit_json:
        with open(args.emit_json, "w", encoding="utf-8") as f:
            json.dump(result, f, indent=2, sort_keys=True)
        print(f"  wrote JSON: {args.emit_json}")

    print("=" * 78)
    print(f"GATES PASSED: {result['passes']} / {result['gates_total']}")
    print("=" * 78)
    if args.mode == "resolvent-json" and extraction_details and extraction_details.get("physical_su3_o3_kernel", False):
        print("INTERPRETATION: supplied kernel is marked physical. If the kernel entries are correct, the reported weights are the physical O(y^3) tromino weights.")
    else:
        print("INTERPRETATION: this run validates the extraction/flat-band plumbing. It is not a final physical SU(3) O(y^3) certificate unless a correct physical resolvent kernel was supplied.")
    if protected:
        print("RESULT: equal-lifter protection holds for the supplied weights; no O(y^3) bandwidth is detected.")
    else:
        print("RESULT: equal-lifter protection fails for the supplied weights; the supplied O(y^3) kernel lifts the flat branch.")
    return result


def main() -> None:
    ap = argparse.ArgumentParser(description="SU(3) O(y^3) tromino weight extractor and C-odd flat-band diagnostic")
    ap.add_argument("--mode", choices=["primitive", "equal", "zero", "custom", "resolvent-json", "haar-moment"], default="primitive")
    ap.add_argument("--L", type=int, default=6, help="periodic lattice size for geometry enumeration; use L>=5")
    ap.add_argument("--samples", type=int, default=256, help="deterministic random k samples")
    ap.add_argument("--grid", type=int, default=24, help="grid per dimension for rough BZ extrema")
    ap.add_argument("--seed", type=int, default=20260611)
    ap.add_argument("--eps", type=float, default=1e-7, help="finite-epsilon branch-tracking step")
    ap.add_argument("--weights-json", type=str, default=None, help="custom JSON class->rational weight map")
    ap.add_argument("--kernel-json", type=str, default=None, help="finite Rayleigh-Schroedinger kernel JSON for --mode resolvent-json")
    ap.add_argument("--equal-weight", type=str, default="1", help="equal lifter weight for --mode equal")
    ap.add_argument("--haar-samples", type=int, default=20000, help="samples for --mode haar-moment")
    ap.add_argument("--emit-json", type=str, default=None, help="optional output JSON path")
    ap.add_argument("--make-kernel-template", type=str, default=None, help="write a resolvent kernel JSON template and exit")
    args = ap.parse_args()

    if args.make_kernel_template:
        make_kernel_template(args.make_kernel_template)
        return

    extraction_details: Optional[Dict[str, Any]] = None
    if args.mode == "primitive":
        weights = dict(PRIMITIVE_CANDIDATE)
        extraction_details = {"source": "primitive candidate", "physical_su3_o3_kernel": False}
    elif args.mode == "equal":
        weights = dict(ZERO_WEIGHTS)
        ew = parse_fraction(args.equal_weight)
        for c in LIFTER_CLASSES:
            weights[c] = ew
        extraction_details = {"source": "equal protected toy kernel", "physical_su3_o3_kernel": False}
    elif args.mode == "zero":
        weights = dict(ZERO_WEIGHTS)
        extraction_details = {"source": "zero kernel", "physical_su3_o3_kernel": False}
    elif args.mode == "custom":
        weights = parse_weights_json(args.weights_json)
        extraction_details = {"source": "custom class weights", "physical_su3_o3_kernel": False}
    elif args.mode == "resolvent-json":
        if not args.kernel_json:
            raise SystemExit("--mode resolvent-json requires --kernel-json PATH")
        weights, extraction_details = extract_weights_from_resolvent_json(args.kernel_json)
    elif args.mode == "haar-moment":
        plaqs, _, _, _, _, _, _, representatives = build_terms(args.L)
        weights, extraction_details = haar_cluster_moment_weights(plaqs, representatives, args.L, args.haar_samples, args.seed)
    else:
        raise AssertionError(args.mode)

    run_flat_diagnostic(weights, args, extraction_details)


if __name__ == "__main__":
    main()
