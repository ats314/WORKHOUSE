"""Pin the G19 source review and replay its narrowly stated exact controls."""

from __future__ import annotations

import hashlib
import json
from datetime import UTC, datetime
from fractions import Fraction
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]


def triangular(n: int) -> Fraction:
    j = n.bit_length() - 1
    scale = 1 << j
    return Fraction(n - scale if j % 2 == 0 else 2 * scale - n, scale)


def main() -> None:
    inventory = json.loads(
        (ROOT / "docs/validation/wilson-g19-corpus-inventory.json").read_text("utf-8-sig")
    )
    for item in inventory:
        assert hashlib.sha256(Path(item["path"]).read_bytes()).hexdigest() == item["sha256"]
    for n in range(1, 8193):
        assert 0 <= triangular(n) <= 1
        assert abs(triangular(n + 1) - triangular(n)) <= Fraction(2, n)
    for j in range(20):
        assert triangular(1 << (2 * j)) == 0
        assert triangular(1 << (2 * j + 1)) == 1

    a11, a12, a22, b11, b12, b21, b22, c11, c12, c22 = sp.symbols(
        "a11 a12 a22 b11 b12 b21 b22 c11 c12 c22", real=True
    )
    a = sp.Matrix([[a11, a12], [a12, a22]])
    b = sp.Matrix([[b11, b12], [b21, b22]])
    c = sp.Matrix([[c11, c12], [c12, c22]])
    x = sp.Matrix(sp.symbols("x1 x2", real=True))
    y = sp.Matrix(sp.symbols("y1 y2", real=True))
    epsilon = sp.Symbol("epsilon", positive=True)
    potential = epsilon * (
        (a * x + b * y).dot(a * x + b * y) + (b.T * x + c * y).dot(b.T * x + c * y)
    )
    pressure = epsilon * sp.trace(c) - epsilon * (b.T * x + c * y).dot(b.T * x + c * y)
    assert (sp.hessian(potential + pressure, x) - 2 * epsilon * a * a).applyfunc(
        sp.expand
    ) == sp.zeros(2)
    assert (sp.hessian(pressure, x) + 2 * epsilon * b * b.T).applyfunc(sp.expand) == sp.zeros(2)

    constant, rate, speed, time = sp.symbols("C c v t", positive=True)
    integral = sp.integrate(constant**2 * sp.exp(-rate * speed * time), (time, 0, sp.oo))
    assert integral == constant**2 / (rate * speed)
    assert 4 * Fraction(3, 4) ** 8 == Fraction(6561, 16384) < Fraction(1, 2)

    names = [
        "scripts/validate_wilson_g19_review.py",
        "docs/validation/wilson-g19-corpus-inventory.json",
        "docs/validation/wilson-g19-corpus-review-manifest.json",
        "docs/validation/wilson-g19-corpus-reconciliation.md",
        "docs/validation/wilson-g19-gaussian-review.md",
        "docs/validation/wilson-g19-sources-review.md",
        "docs/validation/wilson-g19-fibers-review.md",
        "docs/validation/wilson-g19-cauchy-repair.md",
        "docs/validation/wilson-g19-martingale-repair.md",
        "docs/validation/wilson-sc17-late-ledger-audit.md",
        "docs/derivations/yangmills-continuum-balaban-multiscale-proof.md",
        "docs/derivations/yangmills-simon-flat-directions.md",
        "notes/imported/UPLOADS_2026-09-01/Continuum_Combined.lean",
    ]
    report = {
        "recorded_at": datetime.now(UTC).isoformat(),
        "files_hash_verified": len(inventory),
        "distinct_hashes": len({item["sha256"] for item in inventory}),
        "exact_controls": [
            "Bounded dyadic triangular sequence: 8192 increment checks "
            "and 20 exact separated subsequence pairs",
            "General symmetric 2+2 block Gaussian potential-pressure Hessian cancellation, "
            "all entries symbolic",
            "Exact integral of the squared flat-reference exponential semigroup envelope",
            "At kappa0=4, k=8, the proposed entropy weight is 6561/16384<1/2<log(2)",
        ],
        "scope": (
            "Hash verification and four finite/symbolic controls. The all-n counterexample, "
            "operator contour/Schur estimate and analytic corpus proofs are separately written "
            "arguments. No numerical or Lean replay of archived proof certificates is claimed. "
            "The imported Continuum_Combined.lean is not covered by the active Lean build."
        ),
        "artifacts_sha256": {
            name: hashlib.sha256((ROOT / name).read_bytes()).hexdigest() for name in names
        },
    }
    target = ROOT / "docs/validation/wilson-g19-review-2026-09-09.json"
    target.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    print(f"{len(inventory)} source hashes and four exact controls passed; {target}")


if __name__ == "__main__":
    main()
