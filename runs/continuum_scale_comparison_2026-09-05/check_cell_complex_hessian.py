"""Exact finite controls for the cell-complex Wilson gap derivation.

These controls check incidence, transverse reduction, square-block spectral
formulas and the discrete IMS identity. They do not certify the analytic
semiclassical theorem or any volume-uniform nonlinear estimate.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

import sympy as s

sys.dont_write_bytecode = True


def rectangle(nx: int, ny: int):
    vertices = [(x, y) for y in range(ny + 1) for x in range(nx + 1)]
    edges = [((x, y), (x + 1, y)) for y in range(ny + 1) for x in range(nx)]
    edges += [((x, y), (x, y + 1)) for y in range(ny) for x in range(nx + 1)]
    vi, ei = {v: i for i, v in enumerate(vertices)}, {e: i for i, e in enumerate(edges)}
    d0 = s.zeros(len(edges), len(vertices))
    for i, (tail, head) in enumerate(edges):
        d0[i, vi[head]], d0[i, vi[tail]] = 1, -1
    d1 = s.zeros(nx * ny, len(edges))
    for y in range(ny):
        for x in range(nx):
            f = y * nx + x
            for edge, sign in [
                (((x, y), (x + 1, y)), 1),
                (((x + 1, y), (x + 1, y + 1)), 1),
                (((x, y + 1), (x + 1, y + 1)), -1),
                (((x, y), (x, y + 1)), -1),
            ]:
                d1[f, ei[edge]] = sign
    return d0, d1


def controls():
    rows = []
    for nx, ny in [(1, 1), (2, 1), (2, 2), (3, 3)]:
        d0, d1 = rectangle(nx, ny)
        assert d1 * d0 == s.zeros(nx * ny, (nx + 1) * (ny + 1))
        assert d1.rank() == d1.rows == d1.cols - d0.rank()
        face = d1 * d1.T
        expected = s.zeros(nx * ny)
        for y in range(ny):
            for x in range(nx):
                f = y * nx + x
                expected[f, f] = 4
                for xx, yy in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]:
                    if 0 <= xx < nx and 0 <= yy < ny:
                        expected[f, yy * nx + xx] = -1
        assert face == expected
        lam = s.symbols("lam")
        spectrum = [
            4 - 2 * s.cos(s.pi * j / (nx + 1)) - 2 * s.cos(s.pi * k / (ny + 1))
            for j in range(1, nx + 1) for k in range(1, ny + 1)
        ]
        assert s.simplify(face.charpoly(lam).as_expr() - s.prod(lam - e for e in spectrum)) == 0
        minimum = s.simplify(spectrum[0])
        rows.append({"faces": [nx, ny], "transverse_dimension": d1.rows,
                     "minimum_curl_squared": str(minimum),
                     "SU_N_physical_gap_leading_coefficient": str(2 * s.sqrt(minimum))})

    d0, d1 = rectangle(2, 2)
    rooted_gradient = d0[:, 1:]
    projector = s.eye(d0.rows) - rooted_gradient * (
        rooted_gradient.T * rooted_gradient
    ).inv() * rooted_gradient.T
    assert projector == projector.T and projector * projector == projector
    assert d0.T * projector == s.zeros(d0.cols, d0.rows)
    assert d1 * projector == d1

    kinetic = d1.T * d1
    q = projector * s.Matrix([i * i + 1 for i in range(d1.cols)])
    eta0 = [s.Rational(3, 5) if i % 2 else s.Rational(4, 5) for i in range(d1.cols)]
    eta1 = [s.Rational(4, 5) if i % 2 else s.Rational(3, 5) for i in range(d1.cols)]
    etas = [eta0, eta1]
    assert all(sum(eta[i] ** 2 for eta in etas) == 1 for i in range(d1.cols))
    difference = sum(((s.diag(*eta) * q).T * kinetic * (s.diag(*eta) * q))[0]
                     for eta in etas) - (q.T * kinetic * q)[0]
    delta = s.Matrix(d1.cols, d1.cols, lambda i, j: sum(
        (eta[i] - eta[j]) ** 2 for eta in etas
    ))
    identity = -s.Rational(1, 2) * sum(
        kinetic[i, j] * q[i] * q[j] * delta[i, j]
        for i in range(d1.cols) for j in range(d1.cols)
    )
    assert difference == identity
    bound = max(sum(abs(kinetic[i, j]) * delta[i, j] for j in range(d1.cols))
                for i in range(d1.cols)) / 2
    assert abs(difference) <= bound * (q.T * q)[0]
    gradient = d0 * s.Matrix([i * i for i in range(d0.cols)])
    assert (gradient.T * kinetic * gradient)[0] == 0
    localized_gradient_energy = sum(
        ((s.diag(*eta) * gradient).T * kinetic * (s.diag(*eta) * gradient))[0]
        for eta in etas
    )
    assert localized_gradient_energy > 0
    return {
        "scope": __doc__, "rectangle_controls": rows,
        "transverse_projector_identities": True,
        "IMS_exact_difference": str(difference),
        "IMS_row_bound": str(bound),
        "localized_pure_gradient_negative_control": str(localized_gradient_energy),
        "first_physical_cluster_rank": "m*(m+1)/2 (analytic invariant-tensor proof)",
    }


if __name__ == "__main__":
    if sys.flags.optimize:
        raise RuntimeError("Assertions must be enabled")
    target = Path(__file__).with_suffix(".json")
    if target.exists():
        raise FileExistsError("Choose a fresh artifact; existing evidence is preserved")
    report = controls()
    target.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8", newline="\n")
    print(json.dumps(report, indent=2))
