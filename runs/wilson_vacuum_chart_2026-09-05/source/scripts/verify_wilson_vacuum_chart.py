"""Generate an exact finite-model certificate for the Wilson vacuum chart.

Run from the repository root. The certificate distinguishes live exact tensor
calculations, numerical exponential checks, and the separate analytic theorem.
It never overwrites the supplied September 4 research artifacts.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import sys
from pathlib import Path

import numpy as np
from scipy.linalg import expm
from sympy import Rational, SparseMatrix, cancel, symbols

from workhouse.wilson_chart_recursion import product_recursion
from workhouse.wilson_vacuum_chart import (
    chart,
    embed_local,
    product_chart,
    spectator_kinetic,
    support_majorants,
    two_level_negative_control,
)

ROOT = Path(__file__).resolve().parents[1]


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def finite_exponential_oracle() -> dict:
    """Different route: actual exponentials/eigenvectors, no coefficient engine."""
    ratio = Rational(3, 4)
    kinetic = SparseMatrix.diag(1, ratio)
    potential = SparseMatrix([[0, Rational(2, 3)], [Rational(2, 3), Rational(1, 2)]])
    model = chart(kinetic, [potential], 3)
    d, v = np.array(kinetic, dtype=float), np.array(potential, dtype=float)
    s1 = np.array(model.first_generators[0], dtype=float)
    s2 = np.array(model.second_generators[(2,)], dtype=float)
    a0 = np.array(model.second_rotated[(0,)], dtype=float)
    a1 = np.array(model.second_rotated[(1,)], dtype=float)
    a2 = np.array(model.second_rotated[(2,)], dtype=float)
    samples = []
    for u in (0.01, 0.005, 0.0025):
        e = expm(u * v / 2)
        block = np.linalg.matrix_power(e @ d @ e, 3)
        values, _ = np.linalg.eigh(block)
        unitary = expm(u * s1) @ expm(u**2 * s2)
        rotated = unitary.T @ block @ unitary / values[-1]
        remainder = float(np.linalg.norm(rotated - a0 - u * a1 - u**2 * a2, 2))
        vacuum_error = float(np.linalg.norm((rotated - a0)[:, 0]))
        samples.append(
            {
                "u": u,
                "operator_remainder": remainder,
                "vacuum_error": vacuum_error,
                "operator_remainder_over_u3": remainder / u**3,
            }
        )
    ratios = [
        samples[j]["operator_remainder"] / samples[j + 1]["operator_remainder"]
        for j in range(len(samples) - 1)
    ]
    if not all(6 < value < 10 for value in ratios):
        raise AssertionError(f"Independent cubic-remainder diagnostic failed: {ratios}")
    return {
        "method": "direct SciPy exponentials and NumPy Perron eigenvalue",
        "scope": "two-dimensional finite model, floating-point diagnostic",
        "steps": 3,
        "samples": samples,
        "halving_ratios": ratios,
        "passed": True,
    }


def verify() -> dict:
    checks = []

    def record(name: str, passed: bool, **details):
        if not passed:
            raise AssertionError(name)
        checks.append({"name": name, "passed": True, **details})

    control = two_level_negative_control()
    record(
        "first-order chart leaves quadratic creation; second-order chart cancels it",
        control["first_chart_residual"] == Rational(97, 96)
        and control["second_generator"] == Rational(97, 24)
        and control["final_vacuum_column"].is_zero_matrix,
        residual=str(control["first_chart_residual"]),
        second_generator=str(control["second_generator"]),
    )
    supports = ((0, 1, 2, 3), (3, 4, 5, 6))
    models = [product_chart(7, supports, steps=m) for m in (1, 2, 3)]
    for m, model in zip((1, 2, 3), models, strict=True):
        all_anchored = all(
            a[:, 0].is_zero_matrix and a[0, :].is_zero_matrix and a == a.H
            for k, a in model.second_rotated.items()
            if sum(k)
        )
        record(
            f"all nonconstant degree<=2 coefficients anchored for seven-site block m={m}",
            all_anchored,
            dimension=128,
            kinetic_ratio="4/5",
            supports=[list(s) for s in supports],
        )
    record(
        "local quadratic generator unchanged by powers one, two, three",
        models[0].second_generators == models[1].second_generators == models[2].second_generators,
    )
    mixed = models[0].second_generators[(1, 1)]
    record(
        "overlapping four-link faces require a nonzero connected second rotation",
        not mixed.is_zero_matrix,
        vacuum_column={str(i): str(mixed[i, 0]) for i in range(128) if mixed[i, 0]},
    )
    single = product_chart(2, ((0, 1),), steps=2)
    disjoint = product_chart(5, ((0, 1), (2, 3)), steps=2)
    first = single.first_rotated[(1,)]
    expected = (
        embed_local(first, (0, 1), 5)
        * embed_local(first, (2, 3), 5)
        * spectator_kinetic(5, (0, 1, 2, 3), Rational(4, 5) ** 2)
    )
    record(
        "disjoint coefficient equals product with the complete spectator kinetic factor",
        disjoint.second_rotated[(1, 1)] == expected
        and disjoint.second_generators[(1, 1)].is_zero_matrix,
    )
    local = product_chart(3, ((0, 1), (1, 2)), steps=2)
    spectator = product_chart(4, ((0, 1), (1, 2)), steps=2)
    d_out = spectator_kinetic(4, (0, 1, 2), Rational(4, 5) ** 2)
    record(
        "connected identities hold entrywise on excited spectator states",
        all(
            spectator.second_rotated[k] == embed_local(a, (0, 1, 2), 4) * d_out
            for k, a in local.second_rotated.items()
        ),
    )
    maxima = [max(support_majorants(n)[j] for n in range(1, 80)) for j in range(3)]
    record(
        "rational full-operator support-count bound",
        maxima == [16, 336, Rational(2592, 5)]
        and 11 * maxima[0] + 22 * maxima[1] + maxima[2] == Rational(40432, 5),
        exact_maxima=[str(x) for x in maxima],
        coefficient_constant="40432/5",
        tail_proof="ratios bounded respectively by 24/25,32/35,80/81 after maxima",
    )
    fourth = product_recursion(3, ((0, 1), (1, 2)), 4)
    third = product_recursion(4, ((0, 1), (1, 2), (2, 3)), 3)
    for label, model in (
        ("two overlapping supports through order four", fourth),
        ("three-support connected chain through order three", third),
    ):
        record(
            label,
            all(
                a[:, 0].is_zero_matrix and a[0, :].is_zero_matrix and a == a.H
                for k, a in model.rotated.items()
                if sum(k)
            ),
            dimension=next(iter(model.raw.values())).rows,
            nonconstant_coefficient_count=len(model.rotated) - 1,
        )
    record(
        "third and fourth generators are independent of block power",
        fourth.generators == product_recursion(3, ((0, 1), (1, 2)), 4, steps=2).generators,
    )
    single4 = product_recursion(2, ((0, 1),), 4)
    disconnected4 = product_recursion(5, ((0, 1), (2, 3)), 4)
    d_out4 = spectator_kinetic(5, (0, 1, 2, 3), Rational(4, 5))
    disconnected_keys = ((2, 1), (1, 2), (2, 2), (3, 1), (1, 3))
    record(
        "all disconnected cubic/quartic coefficients factor with spectator damping",
        all(
            disconnected4.rotated[k]
            == embed_local(single4.rotated[(k[0],)], (0, 1), 5)
            * embed_local(single4.rotated[(k[1],)], (2, 3), 5)
            * d_out4
            and disconnected4.generators[k].is_zero_matrix
            for k in disconnected_keys
        ),
    )
    d = Rational(4, 5) ** 2
    a = (1 + d) / (1 - d)
    record(
        "cubic generator matches exact arctangent diagonalization",
        single4.generators[(3,)][3, 0] == a / 12 - a**3 / 6,
        exact_generator=str(single4.generators[(3,)][3, 0]),
        method="Taylor expansion of atan((1+d)/(1-d)*sinh(u))/2",
    )
    x, y, tau = symbols("x y tau")
    r1, r2, r12 = tau / (x - 1), tau / (y - 1), tau / (x * y - 1)
    omitted = cancel(r12 * (r1 + r2) - r1 * r2)
    record(
        "endpoint denominator identity retains the mixed magnetic kick",
        cancel(r12 * (r1 + r2 + tau) - r1 * r2) == 0 and omitted != 0,
        omitted_kick_error=str(omitted),
        hypotheses="x != 1, y != 1, x*y != 1; exponential interpretation in analytic note",
    )
    sources = [
        "src/workhouse/wilson_vacuum_chart.py",
        "src/workhouse/wilson_chart_recursion.py",
        "tests/test_wilson_vacuum_chart.py",
        "tests/test_wilson_chart_recursion.py",
        "tests/test_wilson_chart_independent_oracle.py",
        "scripts/verify_wilson_vacuum_chart.py",
        "paper/research_notes/G18_SECOND_ORDER_WILSON_VACUUM_CHART_20260905.md",
        "paper/research_notes/G18_VACUUM_CHART_RECURSION_20260905.md",
        "paper/research_notes/G18_WILSON_ENDPOINT_GAUGE_AND_MAJORANT_20260905.md",
        "lean/Workhouse/VacuumChart.lean",
        "paper/research_notes/G19_TRANSFER_RESOLVENT_UNIFORM_BOUNDS_20260905.md",
        "paper/research_notes/G18_EXCITED_WINDOW_OPERATOR_BRIDGE_20260904.md",
    ]
    return {
        "schema": "workhouse-wilson-vacuum-chart/v1",
        "coefficient_convention": "ordinary multivariate Taylor coefficients, not derivatives",
        "exact_checks": checks,
        "exact_check_count": len(checks),
        "numeric_exponential_oracle": finite_exponential_oracle(),
        "analytic_result": {
            "statement": "local second-order chart of actual normalized Wilson block; "
            "full coefficient norm <= (40432/5) f_star^2",
            "evidence": "analytic proof in note; exact finite models check its identities",
            "uniformity": ["volume", "permitted temporal mesh", "local Hilbert dimension"],
            "extension": "connected chart and uniform full coefficient bound at every fixed order; "
            "block-independent generators and exact endpoint support inverse",
            "not_claimed": [
                "summed all-orders chart",
                "thermodynamic actual-Wilson band",
                "uniform finite-u remainder from the truncated chart",
                "spatial continuum",
            ],
        },
        "sources": {name: digest(ROOT / name) for name in sources},
        "runtime": {"python": sys.version.split()[0], "numpy": np.__version__},
        "passed": True,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    output = args.output.resolve()
    if output.exists():
        raise FileExistsError(f"Choose a new output path: {output}")
    result = verify()
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(
        json.dumps(
            {
                "exact_checks": result["exact_check_count"],
                "passed": result["passed"],
                "output": str(output),
            },
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
