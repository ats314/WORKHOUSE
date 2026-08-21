#!/usr/bin/env python3
# =====================================================================
# ENGINE_TROM_tromino_weight_constraint_certificate.py
#
# Phase-2 geometry-weight certificate for the O(y^3) flat-band question.
#
# This is still NOT the full SU(3) third-order effective-Hamiltonian
# calculation. It is the exact geometry target that the SU(3) calculation
# must feed.
#
# Input/output meaning:
#   The O(y^2) C-odd flat band came from
#       S(k) + 4 I = Ntil(k) Ntil(k)^dag, det Ntil(k) == 0.
#   The next possible lifting at O(y^3) is controlled by two-hop/tromino
#   geometries p -> q -> r. The SU(3) resolvent/channel calculation will
#   assign a coefficient to each geometry class.
#
# This script computes the NECESSARY AND SUFFICIENT geometry condition for a
# weighted sum of tromino classes to preserve the flat C-odd band:
#
#       w_path+ = w_path- = w_corner_triangle.
#
# Backtrack and same-link-triangle weights are independently protected.
# The common lifter weight is also protected, because the equal-weight sum
# of the three lifting classes is the lifter part of S(k)^2.
#
# Therefore the next SU(3) ED/Weingarten certificate needs only this target:
#   compute the three physical lifting weights exactly and check whether
#       W(path_bent_or_straight_prod+1)
#     = W(path_bent_or_straight_prod-1)
#     = W(triangle_corner_cyc-1).
#
# If yes: the O(y^2) C-odd flat branch survives the length-2/tromino O(y^3)
# geometry sector. If no: the flat band is lifted at O(y^3).
#
# Optional usage:
#   python ENGINE_TROM_tromino_weight_constraint_certificate.py
#   python ENGINE_TROM_tromino_weight_constraint_certificate.py --weights '{"path_bent_or_straight_prod+1":1,"path_bent_or_straight_prod-1":2,"triangle_corner_cyc-1":1}'
# =====================================================================

import argparse
import itertools
import json
import math
import sys
from collections import Counter, defaultdict

import numpy as np
import sympy as sp

np.set_printoptions(precision=6, suppress=True)

PASS = []
def gate(name, cond):
    PASS.append((name, bool(cond)))
    print(f"  GATE {'PASS' if cond else 'FAIL'} :: {name}")
    if not cond:
        raise SystemExit(f"GATE FAILED: {name}")

# ---------------------------------------------------------------------
# 1. Cubical spatial plaquette complex
# ---------------------------------------------------------------------
ORIENT = [(0, 1), (0, 2), (1, 2)]  # xy, xz, yz
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
PROTECTED_CLASSES = [
    "backtrack_2plaquette",
    "triangle_same_link_cyc+1",
]


def shift(x, d, L, n=1):
    z = list(x)
    z[d] = (z[d] + n) % L
    return tuple(z)


def centered_displacement(x, y, L):
    """Centered displacement y-x on a periodic L torus."""
    return tuple(((y[i] - x[i] + L // 2) % L) - L // 2 for i in range(3))


def boundary(x, o, L):
    """Oriented boundary of plaquette (x; mu<nu): [((site, direction), sign)]."""
    mu, nu = ORIENT[o]
    x = tuple(x)
    return [
        ((x, mu), +1),
        ((shift(x, mu, L), nu), +1),
        ((shift(x, nu, L), mu), -1),
        ((x, nu), -1),
    ]


def build_complex(L):
    plaqs = [(x, o) for x in itertools.product(range(L), repeat=3) for o in range(3)]
    pidx = {p: i for i, p in enumerate(plaqs)}
    link_inc = defaultdict(list)
    for p in plaqs:
        i = pidx[p]
        for ln, sg in boundary(p[0], p[1], L):
            link_inc[ln].append((i, sg))

    nbrs = {i: {} for i in range(len(plaqs))}
    for ln, inc in link_inc.items():
        for (i, si), (j, sj) in itertools.combinations(inc, 2):
            if j in nbrs[i] or i in nbrs[j]:
                raise RuntimeError("two plaquettes share more than one link")
            nbrs[i][j] = (si * sj, ln)
            nbrs[j][i] = (si * sj, ln)
    return plaqs, pidx, link_inc, nbrs


def common_links(bsets, indices):
    s = bsets[indices[0]].copy()
    for i in indices[1:]:
        s &= bsets[i]
    return s


def classify_path(i, q, r, nbrs, bsets):
    """Classify ordered two-hop path i -> q -> r by local tromino geometry."""
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
        # This class should not occur for the cubic plaquette shared-link graph,
        # but keeping the branch makes the classifier diagnostic complete.
        return f"path_common_link_prod{prod:+d}"
    return f"path_bent_or_straight_prod{prod:+d}"


# ---------------------------------------------------------------------
# 2. Bloch operators for class-resolved two-hop walks
# ---------------------------------------------------------------------
def build_class_terms(L=6):
    plaqs, pidx, link_inc, nbrs = build_complex(L)
    NP = len(plaqs)
    bsets = [set(ln for ln, _ in boundary(x, o, L)) for x, o in plaqs]

    class_terms = defaultdict(Counter)
    class_counts = Counter()
    root_counts = defaultdict(Counter)

    for i in range(NP):
        xi, oi = plaqs[i]
        for q, (s1, _) in nbrs[i].items():
            for r, (s2, _) in nbrs[q].items():
                cls = classify_path(i, q, r, nbrs, bsets)
                xr, orr = plaqs[r]
                d = centered_displacement(xi, xr, L)
                signprod = s1 * s2
                class_terms[cls][(oi, orr, d, signprod)] += 1
                class_counts[cls] += 1
                root_counts[oi][cls] += 1

    return plaqs, link_inc, nbrs, class_terms, class_counts, root_counts


def eval_counter(counter, k, L):
    """Evaluate reduced term counter into a 3x3 Bloch matrix."""
    M = np.zeros((3, 3), dtype=complex)
    for (o, oj, d, s), multiplicity in counter.items():
        phase = np.exp(1j * np.dot(np.asarray(k, dtype=float), np.asarray(d, dtype=float)))
        M[o, oj] += (multiplicity / (L ** 3)) * s * phase
    return M


def flat_vector(k):
    u = [1 - np.exp(1j * q) for q in k]
    return np.array([np.conjugate(u[2]), -np.conjugate(u[1]), np.conjugate(u[0])], dtype=complex)


def weighted_matrix(class_terms, weights, k, L):
    M = np.zeros((3, 3), dtype=complex)
    for cls, counter in class_terms.items():
        M += weights.get(cls, 0.0) * eval_counter(counter, k, L)
    return M


def flat_line_residual(class_terms, weights, ks, L):
    """Return max residual of M(k)w(k) being proportional to w(k), plus eval range."""
    max_resid = 0.0
    vals = []
    for k in ks:
        w = flat_vector(k)
        nrm = np.vdot(w, w).real
        if nrm < 1e-12:
            continue
        M = weighted_matrix(class_terms, weights, k, L)
        Mw = M @ w
        alpha = np.vdot(w, Mw) / nrm
        denom = np.linalg.norm(Mw) + 1e-12
        resid = np.linalg.norm(Mw - alpha * w) / denom
        max_resid = max(max_resid, float(resid))
        vals.append(alpha)
    vals = np.asarray(vals)
    if len(vals) == 0:
        return math.nan, math.nan, math.nan, math.nan
    return max_resid, float(vals.real.min()), float(vals.real.max()), float(np.max(np.abs(vals - vals[0])))


# ---------------------------------------------------------------------
# 3. Numeric linear algebra certificate for the protection subspace
# ---------------------------------------------------------------------
def build_constraint_matrix(class_terms, classes, ks, L):
    """Rows for equations sum_i w_i B_i(k) flat(k) - c flat(k)=0."""
    rows = []
    for k in ks:
        w = flat_vector(k)
        if np.linalg.norm(w) < 1e-12:
            continue
        cols = []
        for cls in classes:
            cols.append(eval_counter(class_terms[cls], k, L) @ w)
        cols.append(-w)  # coefficient of constant eigenvalue c
        C = np.column_stack(cols)  # 3 x (nclass+1)
        for a in range(3):
            rows.append(C[a].real)
            rows.append(C[a].imag)
    return np.vstack(rows)


def vector_from_weights(classes, weights, c):
    v = np.zeros(len(classes) + 1, dtype=float)
    for cls, val in weights.items():
        v[classes.index(cls)] = float(val)
    v[-1] = float(c)
    return v


def normalized_residual(A, v):
    return np.linalg.norm(A @ v) / max(np.linalg.norm(v), 1e-12)


def analytic_protection_condition(weights, tol=1e-10):
    """The derived exact condition: the three lifting weights are equal."""
    vals = [float(weights.get(cls, 0.0)) for cls in LIFTER_CLASSES]
    return max(vals) - min(vals) <= tol


def predicted_constant(weights):
    """Eigenvalue on the flat line if the analytic protection condition holds."""
    b = float(weights.get("backtrack_2plaquette", 0.0))
    t = float(weights.get("triangle_same_link_cyc+1", 0.0))
    l = float(weights.get("path_bent_or_straight_prod+1", 0.0))
    # Only valid if all lifter weights are equal to l.
    return 12.0 * b + 12.0 * l - 8.0 * t


# ---------------------------------------------------------------------
# 4. Main
# ---------------------------------------------------------------------
def main():
    parser = argparse.ArgumentParser(description="Tromino O(y^3) geometry-weight flat-band constraint certificate")
    parser.add_argument("--L", type=int, default=6, help="periodic lattice side length for geometry enumeration; default 6")
    parser.add_argument("--weights", type=str, default=None,
                        help="optional JSON dict of class weights to test")
    parser.add_argument("--samples", type=int, default=96, help="number of deterministic random k samples; default 96")
    args = parser.parse_args()

    L = args.L
    print("=" * 78)
    print("TROMINO GEOMETRY-WEIGHT CONSTRAINT CERTIFICATE")
    print("=" * 78)
    print(f"  lattice L={L}; k-samples={args.samples}")

    plaqs, link_inc, nbrs, class_terms, class_counts, root_counts = build_class_terms(L)
    NP = len(plaqs)

    print("=" * 78)
    print("STEP 1: base complex and class inventory")
    print("=" * 78)
    gate("every spatial link lies in 4 plaquettes with signs (+,+,-,-)",
         all(len(v) == 4 and sorted(s for _, s in v) == [-1, -1, 1, 1]
             for v in link_inc.values()))
    gate("every plaquette has 12 shared-link neighbors",
         all(len(nbrs[i]) == 12 for i in range(NP)))
    gate("each plaquette has 144 ordered two-hop paths",
         all(sum(root_counts[o].values()) == (NP // 3) * 144 for o in range(3)))
    gate("class counts are orbital-uniform",
         all(root_counts[0] == root_counts[o] for o in range(1, 3)))

    print("  ordered two-hop classes, count per source plaquette:")
    for cls in CLASSES_ORDER:
        per = class_counts[cls] // NP
        print(f"    {cls:32s} : {per:3d}")
    gate("observed class set matches expected five classes",
         set(class_terms.keys()) == set(CLASSES_ORDER))

    rng = np.random.default_rng(20260611)
    ks = rng.uniform(0.19, 2 * np.pi - 0.19, size=(args.samples, 3))

    print("=" * 78)
    print("STEP 2: individual class action on the flat-band line")
    print("=" * 78)
    status = {}
    for cls in CLASSES_ORDER:
        weights = {cls: 1.0}
        max_resid, emin, emax, spread = flat_line_residual(class_terms, weights, ks, L)
        protects = max_resid < 1e-9 and spread < 1e-9
        status[cls] = protects
        label = "PROTECTS" if protects else "LIFTS/MIXES"
        print(f"    {cls:32s} : {label:12s} resid={max_resid:.2e} spread={spread:.2e} eval=[{emin:+.3f},{emax:+.3f}]")

    gate("backtrack protects flat line", status["backtrack_2plaquette"])
    gate("same-link triangle protects flat line", status["triangle_same_link_cyc+1"])
    gate("all three lifter classes individually lift/mix",
         all(not status[cls] for cls in LIFTER_CLASSES))

    print("=" * 78)
    print("STEP 3: protection subspace solve")
    print("=" * 78)
    Aeq = build_constraint_matrix(class_terms, CLASSES_ORDER, ks, L)
    _, singular_values, vh = np.linalg.svd(Aeq, full_matrices=True)
    rank = int(np.sum(singular_values > 1e-9))
    null_dim = vh.shape[0] - rank
    print(f"  singular values: {np.array2string(singular_values, precision=3)}")
    print(f"  rank={rank}; null_dim={null_dim} among weights+constant")
    gate("protection nullspace has dimension 3", null_dim == 3)

    # Analytic basis vectors for the exact protection subspace:
    #   backtrack alone: c = 12
    #   same-link triangle alone: c = -8
    #   equal lifter combination: path+ = path- = corner = 1, c = 12
    basis = [
        ("backtrack basis", {"backtrack_2plaquette": 1.0}, 12.0),
        ("same-link triangle basis", {"triangle_same_link_cyc+1": 1.0}, -8.0),
        ("equal-lifter basis", {
            "path_bent_or_straight_prod+1": 1.0,
            "path_bent_or_straight_prod-1": 1.0,
            "triangle_corner_cyc-1": 1.0,
        }, 12.0),
    ]
    for name, weights, c in basis:
        v = vector_from_weights(CLASSES_ORDER, weights, c)
        res = normalized_residual(Aeq, v)
        gate(f"{name} lies in protection nullspace (resid {res:.2e})", res < 1e-10)

    all_one = {cls: 1.0 for cls in CLASSES_ORDER}
    gate("all five classes with equal weight reproduce S(k)^2 protection, c=16",
         normalized_residual(Aeq, vector_from_weights(CLASSES_ORDER, all_one, 16.0)) < 1e-10)

    # Anti-basis tests: differences among lifter weights must NOT protect.
    diff1 = {
        "path_bent_or_straight_prod+1": 1.0,
        "path_bent_or_straight_prod-1": -1.0,
    }
    diff2 = {
        "path_bent_or_straight_prod+1": 1.0,
        "triangle_corner_cyc-1": -1.0,
    }
    gate("lifter difference path+ - path- is outside protection subspace",
         normalized_residual(Aeq, vector_from_weights(CLASSES_ORDER, diff1, 0.0)) > 1e-3)
    gate("lifter difference path+ - corner is outside protection subspace",
         normalized_residual(Aeq, vector_from_weights(CLASSES_ORDER, diff2, 0.0)) > 1e-3)

    print("=" * 78)
    print("STEP 4: exact geometry conclusion")
    print("=" * 78)
    print("""
  NECESSARY AND SUFFICIENT GEOMETRY CONDITION:

      W(path_bent_or_straight_prod+1)
    = W(path_bent_or_straight_prod-1)
    = W(triangle_corner_cyc-1).

  Backtrack and same-link-triangle coefficients are independently protected.
  If the three lifting weights are equal, their equal-weight sum acts as a
  constant 12 on the C-odd flat line. If they are not equal, the flat line is
  mixed/dispersed by the tromino geometry sector.
""")

    if args.weights is not None:
        print("=" * 78)
        print("STEP 5: user-supplied physical weights test")
        print("=" * 78)
        try:
            supplied = json.loads(args.weights)
        except Exception as exc:
            raise SystemExit(f"Could not parse --weights as JSON: {exc}")
        weights = {cls: float(supplied.get(cls, 0.0)) for cls in CLASSES_ORDER}
        print("  supplied weights:")
        for cls in CLASSES_ORDER:
            print(f"    {cls:32s} : {weights[cls]:+.12g}")

        protected = analytic_protection_condition(weights, tol=1e-9)
        max_resid, emin, emax, spread = flat_line_residual(class_terms, weights, ks, L)
        print(f"  flat-line residual: {max_resid:.3e}")
        print(f"  sampled eigenvalue range on flat vector: [{emin:+.12g}, {emax:+.12g}], spread={spread:.3e}")
        if protected:
            c = predicted_constant(weights)
            print(f"  VERDICT: PROTECTED at geometry level; constant eigenvalue c = {c:+.12g}")
            gate("supplied weights satisfy equal-lifter condition", max_resid < 1e-8 and spread < 1e-8)
        else:
            print("  VERDICT: LIFTS/MIXES at geometry level unless additional non-tromino terms cancel it")
            gate("supplied weights violate equal-lifter condition and show nonzero residual", max_resid > 1e-6 or spread > 1e-6)

    print("=" * 78)
    print(f"ALL {len(PASS)} GATES PASSED")
    print("=" * 78)
    print("""
NEXT SU(3) CERTIFICATE TARGET:
  Compute the exact third-order/resolvent SU(3) coefficients for only these
  three lifting classes:
    1. path_bent_or_straight_prod+1
    2. path_bent_or_straight_prod-1
    3. triangle_corner_cyc-1

  Then run this script with --weights using those coefficients. Equality means
  the C-odd O(y^2) flat band survives this O(y^3) tromino sector; inequality
  means the flat band is genuinely lifted at O(y^3).
""")


if __name__ == "__main__":
    main()
