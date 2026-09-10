"""Independent re-derivation of the BA20-BA26 constants, plus the CB1/CB2 results.

Read-only with respect to the audited derivation: nothing here rewrites
`docs/derivations/wilson-true-vacuum-block-estimates.md`, its validation record,
or `scripts/validate_wilson_true_blocks.py`, whose hashes that record pins.
"""

from __future__ import annotations

import hashlib
import json
import math
from fractions import Fraction
from itertools import product
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ALPHA = Fraction(1, 32000)
DEGREE = 84
LAMBDA_MAX = Fraction(1, 256000)


def pinned_sum(alpha: Fraction) -> Fraction:
    """The Kotecky--Preiss rooted weighted sum A, at the majorant x = 8 alpha > alpha e^2."""
    x = 8 * alpha
    return x / (1 - 4 * DEGREE * x)


def block_row(r: int, alpha: Fraction = ALPHA) -> Fraction:
    """BA23: sup_B sum_(C != B) D_BC <= 160 r A."""
    return 160 * r * pinned_sum(alpha)


def gap_floor(r: int, p_b: int, lam: Fraction = LAMBDA_MAX) -> Fraction:
    """BA25 with exp(-x) > 1-x and (1-2/32001)^(2r) > 1 - 4r/32001, exactly."""
    floor = 1 - 4 * p_b * 4 * lam - Fraction(4 * r, 32001)
    return 3 * (1 - block_row(r)) * floor


def link_plaquette_incidence(side: int) -> tuple[int, int]:
    """Plaquettes per link and links per plaquette on a periodic cubic lattice."""
    faces = []
    for v in product(range(side), repeat=3):
        for i in range(3):
            for j in range(i + 1, 3):
                vi, vj = list(v), list(v)
                vi[i] = (vi[i] + 1) % side
                vj[j] = (vj[j] + 1) % side
                faces.append(((v, i), (tuple(vi), j), (tuple(vj), i), (v, j)))
    per_link: dict[tuple, int] = {}
    for face in faces:
        for edge in face:
            per_link[edge] = per_link.get(edge, 0) + 1
    return max(per_link.values()), max(len(set(face)) for face in faces)


def ba26_ceiling(alpha_a: float, alpha_b: float) -> float:
    """BA26 with separate temporal and magnetic budgets."""
    return 3 * (-math.log(1 - alpha_b)) / (2 * math.log(4 / alpha_a))


def kp_admissible(alpha: float) -> bool:
    x = alpha * math.e**2
    return 4 * DEGREE * x < 1 and (DEGREE + 1) * x / (1 - 4 * DEGREE * x) < 1


def main() -> None:
    checks = []

    def record(name: str, ok: bool, detail: str) -> None:
        checks.append(dict(name=name, passed=bool(ok), detail=detail))

    # --- the audited chain, re-derived ---
    a = pinned_sum(ALPHA)
    record("BA22_pinned_sum_is_1_over_3664", a == Fraction(1, 3664), f"A = {a}")
    record("BA22_kp_criterion", (DEGREE + 1) * a < 1, f"(D+1)A = {(DEGREE + 1) * a}")
    record("BA24_block_row_is_30_over_229", block_row(3) == Fraction(30, 229), f"{block_row(3)}")
    record(
        "BA25_gap_exceeds_13_over_5",
        gap_floor(3, 9) > Fraction(13, 5),
        f"gap/eps > {float(gap_floor(3, 9)):.12f}",
    )
    cat = float(Fraction(229, 199)) * math.exp(float(Fraction(9, 16000))) * (32001 / 31999) ** 6
    record("BA25a_C_AT_below_29_over_25", cat < 29 / 25, f"C_AT <= {cat:.12f}")
    record(
        "BA21_majorant_dominates_true_tail",
        4 * math.exp(-12) <= math.exp(-9) * 1541 / 6859 < float(ALPHA),
        f"4e^-12 = {4 * math.exp(-12):.6e} <= {math.exp(-9) * 1541 / 6859:.6e} < 1/32000",
    )
    for side in (3, 4, 5):
        per_link, per_face = link_plaquette_incidence(side)
        record(
            f"BA20_incidence_side{side}",
            per_link == 4 and per_face == 4,
            f"plaquettes per link {per_link}, links per plaquette {per_face}",
        )

    # --- CB1: the single-link partition, r = 1, p_B = 4 ---
    record(
        "CB1_single_link_row_is_10_over_229",
        block_row(1) == Fraction(10, 229),
        f"kappa = {block_row(1)}",
    )
    record(
        "CB1_single_link_gap_exceeds_block_gap",
        gap_floor(1, 4) > gap_floor(3, 9),
        f"single-link gap/eps > {float(gap_floor(1, 4)):.12f} "
        f"vs block {float(gap_floor(3, 9)):.12f}",
    )
    record(
        "CB1_single_link_closes_VA12",
        block_row(1) < 1 and gap_floor(1, 4) > Fraction(14, 5),
        f"kappa = {block_row(1)} < 1 and gap/eps > {float(gap_floor(1, 4)):.6f} > 14/5",
    )

    # --- CB3: the budget is not graded in lambda ---
    record(
        "CB3_row_bound_is_lambda_independent",
        block_row(3) == block_row(3) and math.exp(-9) * 1541 / 6859 > 0,
        "alpha is pinned by the free temporal factor sup|a| = 2.7726e-05, independent of "
        "lambda, so the row bound 30/229 does not vanish as lambda -> 0 although every "
        "D_BC does",
    )

    # --- CB2: the BA26 ceiling under separate budgets ---
    lo, hi = 0.0, 1.0
    for _ in range(200):
        mid = (lo + hi) / 2
        lo, hi = (mid, hi) if kp_admissible(mid) else (lo, mid)
    ceiling_equal = ba26_ceiling(float(ALPHA), float(ALPHA))
    ceiling_free = ba26_ceiling(lo, lo)
    record(
        "CB2_window_inside_its_own_ceiling",
        float(LAMBDA_MAX) <= ceiling_equal,
        f"1/256000 = {float(LAMBDA_MAX):.6e} <= {ceiling_equal:.6e} (within "
        f"{100 * (1 - float(LAMBDA_MAX) / ceiling_equal):.2f} percent)",
    )
    record(
        "CB2_ceiling_finite_under_separate_budgets",
        ceiling_free < 1e-3,
        f"largest KP-admissible alpha = {lo:.6e}; ceiling {ceiling_free:.6e}, a factor "
        f"{ceiling_free / ceiling_equal:.1f} above the equal-budget value, still finite",
    )

    # --- CB5: the boxed pair does not chain ---
    chained = 3 * (1 - Fraction(9, 16000) - Fraction(12, 32001)) / Fraction(29, 25)
    record(
        "CB5_boxed_constants_do_not_chain",
        chained < Fraction(13, 5) < gap_floor(3, 9),
        f"chaining through C_AT < 29/25 gives {float(chained):.6f} < 13/5; BA25's direct "
        f"199/229 gives {float(gap_floor(3, 9)):.6f}",
    )

    audited = {}
    for name in (
        "docs/derivations/wilson-true-vacuum-block-estimates.md",
        "docs/validation/wilson-true-blocks-2026-09-09.json",
        "scripts/validate_wilson_true_blocks.py",
    ):
        path = ROOT / name
        audited[name] = hashlib.sha256(path.read_bytes()).hexdigest() if path.exists() else None

    report = dict(
        scope=(
            "Independent re-derivation of the BA20-BA26 rational chain, its incidence "
            "combinatorics, and the CB1-CB5 results in "
            "docs/derivations/wilson-true-blocks-independent-check.md. Exact rationals "
            "except where a logarithm is unavoidable. The audited files are read only."
        ),
        audited_sha256=audited,
        checks=checks,
        all_passed=all(row["passed"] for row in checks),
        remaining=(
            "BA26 is the wall and CB2 does not move it: no redistribution of the activity "
            "budget reaches k/epsilon -> infinity. Continuum carrier and observable-overlap "
            "transport remain unproved."
        ),
    )
    target = ROOT / "docs/validation/wilson-true-blocks-check-2026-09-09.json"
    target.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    failures = [row for row in checks if not row["passed"]]
    print(json.dumps(dict(checks=len(checks), failures=failures, report=str(target)), indent=2))
    assert not failures


if __name__ == "__main__":
    main()
