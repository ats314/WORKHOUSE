#!/usr/bin/env python3
# =====================================================================
# ENGINE_TROM_tromino_o3_su3_weight_cards.py
#
# Stage-3 preparation for the SU(3) O(y^3) tromino calculation.
#
# This is NOT a substitute for the Haar/Fierz SU(3) weight engine. It is the
# exact geometry contract that that engine must consume. It isolates the three
# and only three geometry classes capable of lifting the O(y^2) C-odd flat
# band, gives canonical local representatives with oriented boundaries and
# shared-link signs, and provides the exact flat-band preservation test for any
# candidate SU(3) weights.
#
# The target equality for no O(y^3) tromino lifting is:
#
#   W(path_bent_or_straight_prod+1)
# = W(path_bent_or_straight_prod-1)
# = W(triangle_corner_cyc-1).
#
# Usage:
#   python ENGINE_TROM_tromino_o3_su3_weight_cards.py
#   python ENGINE_TROM_tromino_o3_su3_weight_cards.py --emit-json /tmp/tromino_cards.json
#   python ENGINE_TROM_tromino_o3_su3_weight_cards.py --weights '{"path_bent_or_straight_prod+1":1,"path_bent_or_straight_prod-1":1,"triangle_corner_cyc-1":1}'
#   python ENGINE_TROM_tromino_o3_su3_weight_cards.py --weights-file weights.json
# =====================================================================

import argparse
import itertools
import json
import math
from collections import Counter, defaultdict
from fractions import Fraction

import numpy as np

ORIENT = [(0, 1), (0, 2), (1, 2)]  # xy, xz, yz
ONAME = {0: "xy", 1: "xz", 2: "yz"}
L = 6

CLASSES_ORDER = [
    "backtrack_2plaquette",
    "path_bent_or_straight_prod+1",
    "path_bent_or_straight_prod-1",
    "triangle_corner_cyc-1",
    "triangle_same_link_cyc+1",
]
LIFTERS = [
    "path_bent_or_straight_prod+1",
    "path_bent_or_straight_prod-1",
    "triangle_corner_cyc-1",
]
PROTECTED = ["backtrack_2plaquette", "triangle_same_link_cyc+1"]

PASS = []
def gate(name, cond):
    PASS.append((name, bool(cond)))
    print(f"  GATE {'PASS' if cond else 'FAIL'} :: {name}")
    if not cond:
        raise SystemExit(f"GATE FAILED: {name}")


def shift(x, d, L=L, n=1):
    y = list(x)
    y[d] = (y[d] + n) % L
    return tuple(y)


def centered_displacement(x, y, L=L):
    return tuple(((y[i] - x[i] + L // 2) % L) - L // 2 for i in range(3))


def local_coord(x, root):
    return centered_displacement(root, x, L)


def boundary(x, o, L=L):
    """Oriented boundary of plaquette (site x, orientation o)."""
    mu, nu = ORIENT[o]
    return [
        ((tuple(x), mu), +1),
        ((shift(x, mu, L), nu), +1),
        ((shift(x, nu, L), mu), -1),
        ((tuple(x), nu), -1),
    ]


def build_complex(L=L):
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
            nbrs[i][j] = (si * sj, ln, si, sj)
            nbrs[j][i] = (si * sj, ln, sj, si)
    return plaqs, pidx, link_inc, nbrs


def common_links(boundary_sets, indices):
    out = set(boundary_sets[indices[0]])
    for i in indices[1:]:
        out &= boundary_sets[i]
    return out


def classify_path(i, q, r, nbrs, boundary_sets):
    if r == i:
        return "backtrack_2plaquette"
    s1 = nbrs[i][q][0]
    s2 = nbrs[q][r][0]
    prod = s1 * s2
    adj_ir = r in nbrs[i]
    common3 = common_links(boundary_sets, [i, q, r])
    if adj_ir:
        cyc = s1 * s2 * nbrs[r][i][0]
        if len(common3) == 1:
            return f"triangle_same_link_cyc{cyc:+d}"
        return f"triangle_corner_cyc{cyc:+d}"
    if len(common3) == 1:
        return f"path_common_link_prod{prod:+d}"
    return f"path_bent_or_straight_prod{prod:+d}"


def canonical_key(plaqs, triple):
    """Translation-normalized key for selecting simple representatives."""
    root = plaqs[triple[0]][0]
    cards = []
    for idx in triple:
        x, o = plaqs[idx]
        cards.append((local_coord(x, root), o))
    # Small coordinates preferred, then orbital lexicographic.
    score = sum(sum(abs(c) for c in loc) for loc, _ in cards)
    return (score, cards)


def link_to_local(link, root):
    x, d = link
    return {"site": list(local_coord(x, root)), "dir": int(d)}


def plaquette_card(plaqs, idx, root):
    x, o = plaqs[idx]
    bdy = []
    for ln, sg in boundary(x, o, L):
        bdy.append({"link": link_to_local(ln, root), "sign": int(sg)})
    return {
        "site": list(local_coord(x, root)),
        "orientation_index": int(o),
        "orientation": ONAME[o],
        "boundary": bdy,
    }


def path_card(cls, plaqs, triple, nbrs, boundary_sets):
    i, q, r = triple
    root = plaqs[i][0]
    s1, link1, sigma_i_1, sigma_q_1 = nbrs[i][q]
    s2, link2, sigma_q_2, sigma_r_2 = nbrs[q][r]
    data = {
        "class": cls,
        "role_order": ["initial", "middle", "final"],
        "plaquettes": {
            "initial": plaquette_card(plaqs, i, root),
            "middle": plaquette_card(plaqs, q, root),
            "final": plaquette_card(plaqs, r, root),
        },
        "hops": [
            {
                "from": "initial", "to": "middle",
                "shared_link": link_to_local(link1, root),
                "sigma_from": int(sigma_i_1),
                "sigma_to": int(sigma_q_1),
                "relative_sign": int(s1),
            },
            {
                "from": "middle", "to": "final",
                "shared_link": link_to_local(link2, root),
                "sigma_from": int(sigma_q_2),
                "sigma_to": int(sigma_r_2),
                "relative_sign": int(s2),
            },
        ],
        "two_hop_sign_product": int(s1 * s2),
        "initial_final_adjacent": bool(r in nbrs[i]),
        "common_links_all_three": [link_to_local(ln, root) for ln in sorted(common_links(boundary_sets, [i, q, r]))],
    }
    if r in nbrs[i]:
        s3, link3, sigma_r_3, sigma_i_3 = nbrs[r][i]
        data["closing_hop"] = {
            "from": "final", "to": "initial",
            "shared_link": link_to_local(link3, root),
            "sigma_from": int(sigma_r_3),
            "sigma_to": int(sigma_i_3),
            "relative_sign": int(s3),
        }
        data["cycle_sign"] = int(s1 * s2 * s3)
    return data


def build_inventory(L=L):
    plaqs, pidx, link_inc, nbrs = build_complex(L)
    boundary_sets = [set(ln for ln, _ in boundary(x, o, L)) for x, o in plaqs]
    class_counts = Counter()
    root_counts = defaultdict(Counter)
    reps = {}
    rep_keys = {}
    all_triples = defaultdict(list)

    for i in range(len(plaqs)):
        oi = plaqs[i][1]
        for q in nbrs[i]:
            for r in nbrs[q]:
                cls = classify_path(i, q, r, nbrs, boundary_sets)
                triple = (i, q, r)
                class_counts[cls] += 1
                root_counts[oi][cls] += 1
                all_triples[cls].append(triple)
                key = canonical_key(plaqs, triple)
                if cls not in reps or key < rep_keys[cls]:
                    reps[cls] = triple
                    rep_keys[cls] = key
    return plaqs, link_inc, nbrs, boundary_sets, class_counts, root_counts, reps, all_triples


def flat_band_weight_status(weights, tol=1e-12):
    vals = [float(weights.get(k, 0.0)) for k in LIFTERS]
    maxdiff = max(abs(vals[a] - vals[b]) for a in range(3) for b in range(a+1, 3))
    protected = maxdiff <= tol
    return protected, vals, maxdiff


def weight_report(weights):
    protected, vals, maxdiff = flat_band_weight_status(weights)
    print("\nWEIGHT TEST")
    for cls in LIFTERS:
        print(f"  {cls:36s} = {weights.get(cls, 0)}")
    print(f"  max pairwise lifter-weight difference = {maxdiff:.6g}")
    if protected:
        print("  VERDICT: protected by the tromino geometry constraint")
    else:
        print("  VERDICT: LIFTS/MIXES the flat-band line unless SU(3) non-geometry terms cancel it")
    return protected


def parse_weights(args):
    if args.weights_file:
        with open(args.weights_file, "r", encoding="utf-8") as f:
            return json.load(f)
    if args.weights:
        return json.loads(args.weights)
    return None


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--emit-json", default=None, help="write canonical geometry cards to this JSON path")
    ap.add_argument("--weights", default=None, help="JSON dictionary of physical SU(3) weights to test")
    ap.add_argument("--weights-file", default=None, help="JSON file containing physical SU(3) weights to test")
    args = ap.parse_args()

    print("=" * 78)
    print("STAGE-3 SU(3) TROMINO WEIGHT CARDS / FLAT-BAND CONTRACT")
    print("=" * 78)
    plaqs, link_inc, nbrs, boundary_sets, class_counts, root_counts, reps, all_triples = build_inventory(L)
    NP = len(plaqs)

    gate("every link has four incident spatial plaquettes", all(len(v) == 4 for v in link_inc.values()))
    gate("every plaquette has twelve shared-link neighbors", all(len(nbrs[i]) == 12 for i in nbrs))
    gate("each plaquette has 144 ordered two-hop paths", sum(class_counts.values()) == 144 * NP)
    gate("observed class set is exactly the five expected classes", set(class_counts) == set(CLASSES_ORDER))
    gate("class counts are orbital-uniform", all(root_counts[0] == root_counts[o] for o in range(3)))

    print("\nOrdered two-hop classes, per source plaquette:")
    expected_per_source = {
        "backtrack_2plaquette": 12,
        "path_bent_or_straight_prod+1": 52,
        "path_bent_or_straight_prod-1": 40,
        "triangle_corner_cyc-1": 16,
        "triangle_same_link_cyc+1": 24,
    }
    for cls in CLASSES_ORDER:
        per_source = class_counts[cls] // NP
        print(f"  {cls:36s}: {per_source:3d}")
        gate(f"count for {cls} is {expected_per_source[cls]} per source", per_source == expected_per_source[cls])

    cards = []
    print("\nCanonical representative cards for the three lifter classes:")
    for cls in LIFTERS:
        card = path_card(cls, plaqs, reps[cls], nbrs, boundary_sets)
        cards.append(card)
        print(f"\n  {cls}")
        for role in ["initial", "middle", "final"]:
            p = card["plaquettes"][role]
            print(f"    {role:7s}: site={p['site']} orient={p['orientation']}")
        print(f"    hop signs: {[h['relative_sign'] for h in card['hops']]}, product={card['two_hop_sign_product']}")
        if "cycle_sign" in card:
            print(f"    closing cycle sign: {card['cycle_sign']}")
        print(f"    common links all three: {card['common_links_all_three']}")

    gate("all three lifter classes have representative cards", len(cards) == 3)
    gate("path+ representative has two-hop sign +1", cards[0]["two_hop_sign_product"] == +1)
    gate("path- representative has two-hop sign -1", cards[1]["two_hop_sign_product"] == -1)
    gate("corner triangle representative has cycle sign -1", cards[2].get("cycle_sign") == -1)
    gate("corner triangle has no single common link among all three plaquettes", len(cards[2]["common_links_all_three"]) == 0)

    contract = {
        "stage": "O(y^3) tromino SU(3) weight contract",
        "flat_band_no_lift_condition": {
            "required_equal_weights": LIFTERS,
            "equation": "W(path_bent_or_straight_prod+1) = W(path_bent_or_straight_prod-1) = W(triangle_corner_cyc-1)",
            "protected_without_constraint": PROTECTED,
        },
        "class_counts_per_source_plaquette": expected_per_source,
        "lifter_cards": cards,
    }

    if args.emit_json:
        with open(args.emit_json, "w", encoding="utf-8") as f:
            json.dump(contract, f, indent=2, sort_keys=True)
        print(f"\nWrote geometry contract JSON: {args.emit_json}")

    # Built-in sanity tests for candidate weights.
    print("\nBuilt-in weight sanity tests:")
    equal = {cls: 1 for cls in LIFTERS}
    unequal = {LIFTERS[0]: 1, LIFTERS[1]: 2, LIFTERS[2]: 1}
    gate("equal lifter weights preserve flat-band line", flat_band_weight_status(equal)[0])
    gate("unequal lifter weights are detected as lifting/mixing", not flat_band_weight_status(unequal)[0])

    weights = parse_weights(args)
    if weights is not None:
        protected = weight_report(weights)
        gate("provided weights satisfy the exact no-lift condition", protected)
    else:
        print("\nNo physical SU(3) weights supplied. Next computation must provide:")
        for cls in LIFTERS:
            print(f"  W({cls})")
        print("and then rerun this script with --weights or --weights-file.")

    print("=" * 78)
    print(f"ALL {len(PASS)} GATES PASSED")
    print("=" * 78)


if __name__ == "__main__":
    main()
