#!/usr/bin/env python3
"""Reproduce G9 walk counts, exact folds and scoped carrier reduction.

The original 2026-09-10 script is preserved in runs/g9_sixth_combined_2026-09-11/source/.
Unit-edge walks are not plaquette histories. No physical RUR amplitude is inferred.
"""

from __future__ import annotations

import argparse
import itertools
import json
from pathlib import Path

from workhouse.sixth_order import (
    carrier_word,
    combination_report,
    folded_series,
    mixing_terms,
    single_plaquette_series,
)


def carrier_symbol_rur():
    import sympy as sp

    from workhouse.sixth_order import Q

    r, u, rur = (carrier_word(w) for w in ("R", "U", "RUR"))
    defect = sp.expand(Q**2 * rur - r * u * r)
    return {
        "sigma_r": str(r),
        "sigma_u": str(u),
        "sigma_rur": str(rur),
        "sigma_rr": str(carrier_word("RR")),
        "defect_rur": str(defect),
        "is_rur_carrier_projected": defect == 0,
        "contains_e3": "e3" in str(rur),
    }


def walk_census(length):
    steps = [(axis, sign) for axis in range(3) for sign in (-1, 1)]
    closed = retracing = planar = nonplanar = 0
    for path in itertools.product(steps, repeat=length):
        if any(sum(sign for a, sign in path if a == axis) for axis in range(3)):
            continue
        closed += 1
        if any(path[(i + 1) % length] == (axis, -sign) for i, (axis, sign) in enumerate(path)):
            retracing += 1
        elif len({a for a, _ in path}) < 3:
            planar += 1
        else:
            nonplanar += 1
    return {
        "length": length,
        "closed": closed,
        "retracing": retracing,
        "planar_nonretracing": planar,
        "nonplanar_nonretracing": nonplanar,
    }


def geometric_census_length_4_paths():
    return walk_census(4)


def geometric_census_length_6_cube_boundaries():
    """Historical API name: counts 3-axis walks, not six plaquette cube faces."""
    return walk_census(6)


def compute_sixth_order_b_shp_amplitude(*args, **kwargs):
    raise NotImplementedError(
        "Walk counts do not supply Haar weights, electric denominators or folds"
    )


def report():
    odd = single_plaquette_series()
    vacuum = single_plaquette_series(odd=False)
    folds = folded_series()["hermitian"][6]
    return {
        "scope": (
            "Exact formal folds, one-face SU(3) dynamics, and H4-induced carrier "
            "reduction; direct multi-face H6 remains open"
        ),
        "carrier": carrier_symbol_rur(),
        "walks": [walk_census(4), walk_census(6)],
        "hermitian_h6_shifted_electric_words": [
            {"word": "".join(w), "coefficient": str(c)} for w, c in sorted(folds.items())
        ],
        "h4_mixing_pairs": [
            {"left": a or "I", "right": b or "I", "q3_cleared": str(c)}
            for (a, b), c in mixing_terms().items()
        ],
        "combination": combination_report(),
        "one_face_odd": [str(c) for c in odd["energies"]],
        "one_face_vacuum": [str(c) for c in vacuum["energies"]],
        "one_face_rooted_gap": [
            str(a - b) for a, b in zip(odd["energies"], vacuum["energies"], strict=True)
        ],
        "one_face_odd_supports": odd["supports"],
        "one_face_vacuum_supports": vacuum["supports"],
    }


def run_checks():
    from workhouse.invariants.sixth_order import sixth

    results = sixth.run()
    for row in results:
        print(f"{'PASS' if row.passed else 'FAIL'}: {row.name}: {row.detail}")
    return all(row.passed for row in results)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--json", action="store_true")
    parser.add_argument("--out", type=Path)
    args = parser.parse_args()
    if args.json or args.out:
        text = json.dumps(report(), indent=2) + "\n"
        if args.out:
            args.out.parent.mkdir(parents=True, exist_ok=True)
            with args.out.open("x", encoding="utf-8") as stream:
                stream.write(text)
        else:
            print(text, end="")
    else:
        raise SystemExit(0 if run_checks() else 1)
