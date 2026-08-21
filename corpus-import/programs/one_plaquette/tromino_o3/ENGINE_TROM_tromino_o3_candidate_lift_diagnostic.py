#!/usr/bin/env python3
# =====================================================================
# ENGINE_TROM_tromino_o3_candidate_lift_diagnostic.py
#
# Diagnostic certificate for candidate O(y^3) tromino weights in the
# C-odd flat-band problem.
#
# IMPORTANT SCOPE:
#   This script does NOT compute the physical SU(3) third-order weights.
#   It consumes candidate weights for the three geometry classes that can
#   lift the O(y^2) flat band and computes the resulting first-order
#   perturbation of the flat C-odd branch.
#
# Default candidate is the primitive-weight hypothesis seen in Untitled221:
#     W(path+) = 2/9, W(path-) = 2/9, W(corner) = 2/27.
#   If those are later proven to be the true physical third-order weights,
#   this script gives the induced O(y^3) lifting diagnostic.
#
# Usage:
#   python ENGINE_TROM_tromino_o3_candidate_lift_diagnostic.py
#   python ENGINE_TROM_tromino_o3_candidate_lift_diagnostic.py --weights '{"path_bent_or_straight_prod+1":"2/9","path_bent_or_straight_prod-1":"2/9","triangle_corner_cyc-1":"2/27"}'
#   python ENGINE_TROM_tromino_o3_candidate_lift_diagnostic.py --emit-json tromino_o3_candidate_lift_diagnostic.json
# =====================================================================

import argparse
import itertools
import json
import math
from collections import Counter, defaultdict
from fractions import Fraction as F

import numpy as np

np.set_printoptions(precision=8, suppress=True)

PASS = []
def gate(name, cond):
    PASS.append((name, bool(cond)))
    print(f"  GATE {'PASS' if cond else 'FAIL'} :: {name}")
    if not cond:
        raise SystemExit(f"GATE FAILED: {name}")

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
NOTEBOOK_CANDIDATE = {
    "path_bent_or_straight_prod+1": F(2, 9),
    "path_bent_or_straight_prod-1": F(2, 9),
    "triangle_corner_cyc-1": F(2, 27),
}

# ---------------------------------------------------------------------
# Cubical complex
# ---------------------------------------------------------------------
def shift(x, d, L, n=1):
    z = list(x)
    z[d] = (z[d] + n) % L
    return tuple(z)


def centered_displacement(x, y, L):
    return tuple(((y[i] - x[i] + L // 2) % L) - L // 2 for i in range(3))


def boundary(x, o, L):
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
        return f"path_common_link_prod{prod:+d}"
    return f"path_bent_or_straight_prod{prod:+d}"


def build_terms(L=6):
    plaqs, pidx, link_inc, nbrs = build_complex(L)
    NP = len(plaqs)
    bsets = [set(ln for ln, _ in boundary(x, o, L)) for x, o in plaqs]

    # Single-hop signed adjacency counter S(k)
    single = Counter()
    for i in range(NP):
        xi, oi = plaqs[i]
        for j, (s, _) in nbrs[i].items():
            xj, oj = plaqs[j]
            d = centered_displacement(xi, xj, L)
            single[(oi, oj, d, s)] += 1

    # Ordered two-hop class counters.
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

    return plaqs, link_inc, nbrs, single, class_terms, class_counts, root_counts


def eval_counter(counter, k, L):
    M = np.zeros((3, 3), dtype=complex)
    for (o, oj, d, s), multiplicity in counter.items():
        phase = np.exp(1j * np.dot(np.asarray(k), np.asarray(d)))
        M[o, oj] += (multiplicity / (L ** 3)) * s * phase
    return M


def flat_vector(k):
    u = [1 - np.exp(1j * q) for q in k]
    return np.array([np.conjugate(u[2]), -np.conjugate(u[1]), np.conjugate(u[0])], dtype=complex)


def weighted_matrix(class_terms, weights, k, L):
    M = np.zeros((3, 3), dtype=complex)
    for cls, val in weights.items():
        if abs(float(val)) > 0:
            M += float(val) * eval_counter(class_terms[cls], k, L)
    return M


def rayleigh_on_flat(class_terms, weights, k, L):
    w = flat_vector(k)
    nrm = np.vdot(w, w).real
    if nrm < 1e-12:
        return None
    M = weighted_matrix(class_terms, weights, k, L)
    Mw = M @ w
    alpha = np.vdot(w, Mw) / nrm
    resid = np.linalg.norm(Mw - alpha * w) / (np.linalg.norm(Mw) + 1e-15)
    return float(alpha.real), float(abs(alpha.imag)), float(resid)


def parse_fraction(s):
    if isinstance(s, (int, float)):
        return F(s).limit_denominator(10**9)
    if isinstance(s, str):
        return F(s.strip())
    raise ValueError(f"cannot parse fraction from {s!r}")


def parse_weights(arg):
    weights = {cls: F(0, 1) for cls in CLASSES_ORDER}
    if arg is None:
        weights.update(NOTEBOOK_CANDIDATE)
        return weights
    obj = json.loads(arg)
    for k, v in obj.items():
        if k not in CLASSES_ORDER:
            raise ValueError(f"unknown class {k!r}; expected one of {CLASSES_ORDER}")
        weights[k] = parse_fraction(v)
    return weights


def equal_lifter_condition(weights):
    vals = [weights[c] for c in LIFTER_CLASSES]
    return vals[0] == vals[1] == vals[2]


def finite_epsilon_check(single_counter, class_terms, weights, ks, L, eps=1e-7):
    """For generic k, compare exact first-order Rayleigh shift with eigenvalue of S+epsM near -4."""
    worst = 0.0
    used = 0
    for k in ks:
        w = flat_vector(k)
        if np.linalg.norm(w) < 1e-9:
            continue
        S = eval_counter(single_counter, k, L)
        evS = np.linalg.eigvalsh(S)
        # Avoid near-degenerate points where branch tracking is ambiguous.
        gap = np.partition(np.abs(evS + 4.0), 1)[1]
        if gap < 0.25:
            continue
        out = rayleigh_on_flat(class_terms, weights, k, L)
        if out is None:
            continue
        alpha, imag, resid = out
        M = weighted_matrix(class_terms, weights, k, L)
        ev = np.linalg.eigvalsh(S + eps * M)
        nearest = ev[np.argmin(np.abs(ev + 4.0))]
        err = abs((nearest + 4.0) / eps - alpha)
        worst = max(worst, float(err))
        used += 1
    return used, worst


def main():
    ap = argparse.ArgumentParser(description="C-odd O(y^3) candidate tromino lifting diagnostic")
    ap.add_argument("--L", type=int, default=6, help="periodic lattice size for geometry enumeration")
    ap.add_argument("--samples", type=int, default=256, help="deterministic random k samples")
    ap.add_argument("--grid", type=int, default=24, help="grid per dimension for rough BZ extrema")
    ap.add_argument("--weights", type=str, default=None,
                    help="JSON class->weight map. Values may be strings like '2/9'. Default is notebook candidate.")
    ap.add_argument("--emit-json", type=str, default=None, help="optional output JSON path")
    args = ap.parse_args()

    weights = parse_weights(args.weights)
    print("=" * 78)
    print("TROMINO O(y^3) CANDIDATE LIFT DIAGNOSTIC")
    print("=" * 78)
    print("  SCOPE: consumes candidate geometry weights; does not compute physical SU(3) resolvent weights.")
    print(f"  L={args.L}; samples={args.samples}; grid={args.grid}^3")
    print("  weights:")
    for cls in CLASSES_ORDER:
        print(f"    {cls:32s} : {weights[cls]} = {float(weights[cls]):+.12g}")

    plaqs, link_inc, nbrs, single, class_terms, class_counts, root_counts = build_terms(args.L)
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

    rng = np.random.default_rng(20260611)
    ks = rng.uniform(0.31, 2 * np.pi - 0.31, size=(args.samples, 3))

    print("=" * 78)
    print("STEP 2: O(y^2) flat-band base gate")
    print("=" * 78)
    max_s_resid = 0.0
    for k in ks[:64]:
        w = flat_vector(k)
        S = eval_counter(single, k, args.L)
        max_s_resid = max(max_s_resid, np.linalg.norm(S @ w + 4.0 * w) / (np.linalg.norm(w) + 1e-15))
    gate(f"signed adjacency has exact flat vector numerically (max residual {max_s_resid:.2e})", max_s_resid < 1e-11)

    print("=" * 78)
    print("STEP 3: exact protection condition")
    print("=" * 78)
    protected = equal_lifter_condition(weights)
    print(f"  equal-lifter condition: {protected}")
    if weights == {cls: F(0, 1) for cls in CLASSES_ORDER}:
        gate("zero weights are trivially protected", protected)
    elif args.weights is None:
        gate("default notebook candidate violates equal-lifter condition", not protected)

    # Verify equal lifter toy protects; current weights if non-equal lift/mix.
    equal_test = {cls: F(0, 1) for cls in CLASSES_ORDER}
    equal_test["path_bent_or_straight_prod+1"] = F(1, 1)
    equal_test["path_bent_or_straight_prod-1"] = F(1, 1)
    equal_test["triangle_corner_cyc-1"] = F(1, 1)
    spreads_equal = []
    resids_equal = []
    for k in ks[:96]:
        a, im, r = rayleigh_on_flat(class_terms, equal_test, k, args.L)
        spreads_equal.append(a)
        resids_equal.append(r)
    gate("equal lifter weights give constant flat-line correction", max(spreads_equal)-min(spreads_equal) < 1e-10)
    gate("equal lifter weights preserve the flat line", max(resids_equal) < 1e-10)

    print("=" * 78)
    print("STEP 4: candidate flat-branch first-order correction")
    print("=" * 78)
    alphas = []
    imags = []
    resids = []
    for k in ks:
        out = rayleigh_on_flat(class_terms, weights, k, args.L)
        if out is not None:
            a, im, r = out
            alphas.append(a); imags.append(im); resids.append(r)
    amin, amax = min(alphas), max(alphas)
    spread = amax - amin
    print(f"  sampled Rayleigh correction alpha(k): min={amin:+.12g}, max={amax:+.12g}, spread={spread:.12g}")
    print(f"  max imaginary leakage in alpha(k): {max(imags):.3e}")
    print(f"  max flat-line residual ||Mw-alpha w||/||Mw||: {max(resids):.3e}")
    gate("Rayleigh corrections are real to numerical precision", max(imags) < 1e-11)
    if protected:
        gate("protected weights have zero sampled spread", spread < 1e-9)
    else:
        gate("nonprotected weights show sampled energy spread", spread > 1e-4)

    # High-symmetry path values: skip Gamma because the generic flat eigenvector vanishes there.
    high_sym = {
        "X(pi,0,0)": (math.pi, 0.0, 0.0),
        "M(pi,pi,0)": (math.pi, math.pi, 0.0),
        "R(pi,pi,pi)": (math.pi, math.pi, math.pi),
        "generic(pi/2,pi/3,pi/5)": (math.pi/2, math.pi/3, math.pi/5),
    }
    print("  high-symmetry / reference alpha(k):")
    high_out = {}
    for name, k in high_sym.items():
        a, im, r = rayleigh_on_flat(class_terms, weights, np.asarray(k), args.L)
        high_out[name] = {"alpha": a, "residual": r}
        print(f"    {name:24s}: alpha={a:+.12g}, residual={r:.3e}")

    print("=" * 78)
    print("STEP 5: finite-epsilon branch-tracking sanity")
    print("=" * 78)
    used, worst = finite_epsilon_check(single, class_terms, weights, ks, args.L, eps=1e-7)
    print(f"  generic samples used={used}; worst |finite-difference shift - Rayleigh|={worst:.3e}")
    gate("enough nondegenerate generic samples for branch check", used >= 20)
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
    print(f"  grid alpha(k): min={gmin:+.12g}, max={gmax:+.12g}, width={gmax-gmin:.12g}")
    if not protected:
        gate("grid detects nonzero candidate bandwidth", gmax - gmin > 1e-4)

    result = {
        "scope": "candidate diagnostic only; not physical SU(3) O(y^3) certificate",
        "weights": {cls: str(weights[cls]) for cls in CLASSES_ORDER},
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
        "passes": len(PASS),
    }
    if args.emit_json:
        with open(args.emit_json, "w") as f:
            json.dump(result, f, indent=2, sort_keys=True)
        print(f"  wrote JSON: {args.emit_json}")

    print("=" * 78)
    print(f"ALL {len(PASS)} GATES PASSED")
    print("=" * 78)
    print("""
INTERPRETATION:
  The exact O(y^2) flat band is still proven. This diagnostic says what a
  candidate O(y^3) tromino-weight set would do to that flat branch.

  For the default notebook candidate, W_path+=W_path-=2/9 and W_corner=2/27,
  the equal-lifter condition fails and alpha(k) has nonzero momentum spread.
  Therefore, IF those primitive weights become the fully normalized physical
  third-order SU(3) weights, the C-odd flat band lifts at O(y^3).

  This script is not the final weight extractor. The remaining hard problem is
  still the full SU(3) resolvent/channel calculation of W_path+, W_path-, and
  W_corner, including all normalization and subtraction terms.
""")

if __name__ == "__main__":
    main()
