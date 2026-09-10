"""Replay antipodal exact controls and independent original-potential derivatives."""

from __future__ import annotations

import argparse
import json
import math
import random
from dataclasses import asdict
from pathlib import Path

from workhouse.invariants.w6_antipodal import antipodal


def directional_check():
    """Sixty seeded five-point second differences; numerical corroboration only."""
    rng = random.Random(20260910)

    def dot(a, b):
        return sum(x * y for x, y in zip(a, b, strict=True))

    def cross(a, b):
        return [a[1] * b[2] - a[2] * b[1], a[2] * b[0] - a[0] * b[2], a[0] * b[1] - a[1] * b[0]]

    def mul(q, r):
        v, w = q[1:], r[1:]
        vector = cross(v, w)
        return [q[0] * r[0] - dot(v, w), *[q[0] * w[j] + r[0] * v[j] + vector[j] for j in range(3)]]

    def inv(q):
        return [q[0], *[-entry for entry in q[1:]]]

    def exponential(v):
        length = math.sqrt(dot(v, v))
        sinc = math.sin(length) / length if length else 1.0
        return [math.cos(length), *[sinc * entry for entry in v]]

    errors, h, tolerance = [], 1e-3, 2e-7
    for trial in range(60):
        alpha = (0.0, math.pi / 4)[trial] if trial < 2 else rng.uniform(0, math.pi / 4)
        n = [rng.gauss(0, 1) for _ in range(3)]
        norm = math.sqrt(dot(n, n))
        n = [entry / norm for entry in n]
        direction = [rng.gauss(0, 1) for _ in range(9)]
        norm = math.sqrt(dot(direction, direction))
        direction = [entry / norm for entry in direction]
        a, b, c = direction[:3], direction[3:6], direction[6:]
        aa = [math.cos(alpha), *[math.sin(alpha) * entry for entry in n]]
        bb = mul(aa, aa)

        def potential(t, a=a, b=b, c=c, aa=aa, bb=bb):
            ea, eb, ec = (exponential([t * entry for entry in v]) for v in (a, b, c))
            u0, u1 = mul(aa, ea), mul(mul(inv(aa), eb), bb)
            u2, u3 = mul(bb, ec), mul(inv(ec), bb)
            return 16 - 4 * (u0[0] + u1[0] + mul(u2, inv(u0))[0] + mul(u3, inv(u1))[0])

        second = (
            -potential(2 * h)
            + 16 * potential(h)
            - 30 * potential(0)
            + 16 * potential(-h)
            - potential(-2 * h)
        ) / (12 * h**2)
        ca = [c[j] - a[j] for j in range(3)]
        cb = [c[j] + b[j] for j in range(3)]
        ab = [a[j] - b[j] for j in range(3)]
        expected = 4 * math.cos(alpha) * (dot(a, a) + dot(ca, ca) + dot(b, b) + dot(cb, cb))
        expected -= 8 * math.sin(alpha) * dot(n, cross(c, ab))
        errors.append(abs(second - expected))
    return {
        "name": "original_potential_second_directional_derivatives",
        "tier": 2,
        "passed": max(errors) <= tolerance,
        "samples": len(errors),
        "seed": 20260910,
        "step": h,
        "method": "five-point central second difference of original four face words",
        "maximum_absolute_error": max(errors),
        "absolute_tolerance": tolerance,
        "scope": "Finite corroboration, including theta=0 and theta=pi; not proof.",
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--out", type=Path)
    args = parser.parse_args()
    exact = [asdict(result) for result in antipodal.run()]
    numerical = directional_check()
    passed = all(result["passed"] for result in exact) and numerical["passed"]
    payload = {
        "schema": "w6-antipodal-controls/v1",
        "passed": passed,
        "exact_checks": exact,
        "numerical_control": numerical,
        "scope": "Exact magnetic algebra and finite numerical corroboration. Bundle, "
        "metric-order and score-invariance arguments are reviewed in the source "
        "note. No full-statement Lean formalization or true-ground M10 estimate.",
    }
    text = json.dumps(payload, indent=2) + "\n"
    if args.out:
        args.out.parent.mkdir(parents=True, exist_ok=True)
        with args.out.open("x", encoding="utf-8", newline="\n") as stream:
            stream.write(text)
    print(text, end="")
    return 0 if passed else 1


if __name__ == "__main__":
    raise SystemExit(main())
