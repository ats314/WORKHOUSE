"""Independent rational certificate replay; imports no creator-parent engine."""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

import sympy as sp


def matrix_hash(matrix):
    rows = [[str(matrix[i, j]) for j in range(matrix.cols)] for i in range(matrix.rows)]
    return hashlib.sha256(json.dumps(rows, separators=(",", ":")).encode()).hexdigest()


def replay_psd(matrix, certificate):
    n = matrix.rows
    assert certificate["dimension"] == n
    assert certificate["matrix_sha256"] == matrix_hash(matrix)
    pivots = [sp.Rational(d) for d in certificate["diagonal"]]
    assert len(pivots) == n and all(d >= 0 for d in pivots)
    upper = sp.eye(n)
    positions = set()
    for i, j, value in certificate["unit_upper_off_diagonal"]:
        assert 0 <= i < j < n and (i, j) not in positions
        positions.add((i, j))
        upper[i, j] = sp.Rational(value)
    assert matrix == upper.T * sp.diag(*pivots) * upper
    rank = sum(d != 0 for d in pivots)
    assert certificate["rank"] == rank
    return rank


def rebuild(case):
    dims = case["link_dimensions"]
    size = int(sp.prod(dims))
    operators = []
    norms_squared = []
    for record in case["creators"]:
        support = record["support"]
        matrix = sp.zeros(size)
        norm2 = 0
        for excitations, value in record["entries"]:
            value = sp.Rational(value)
            norm2 += value**2
            factors = []
            for site, dim in enumerate(dims):
                if site in support:
                    factor = sp.zeros(dim)
                    excitation = excitations[support.index(site)]
                    assert 0 < excitation < dim
                    factor[excitation, 0] = value if site == support[0] else 1
                else:
                    factor = sp.eye(dim)
                factors.append(factor)
            matrix += sp.kronecker_product(*factors)
        operators.append(matrix)
        norms_squared.append(norm2)
    q = []
    for site in range(len(dims)):
        factors = [
            sp.diag(0, *([1] * (dim - 1))) if site == i else sp.eye(dim)
            for i, dim in enumerate(dims)
        ]
        q.append(sp.kronecker_product(*factors))
    anchors = [
        sum(
            (a for a, r in zip(operators, case["creators"], strict=True) if i in r["support"]),
            sp.zeros(size),
        )
        for i in range(len(dims))
    ]
    parents = [qi - ai for qi, ai in zip(q, anchors, strict=True)]
    h = sum((p.T * p for p in parents), sp.zeros(size))
    psi = sp.Matrix([sp.Rational(v) for v in case["state"]])
    assert psi[0] == 1
    for p in parents:
        assert p * p == p and p * psi == sp.zeros(size, 1)
        assert all(p * p2 == p2 * p for p2 in parents)
    norm2 = (psi.T * psi)[0]
    assert norm2 == sp.Rational(case["state_norm_squared"])
    projection = psi * psi.T / norm2
    mass = [
        sum(
            len(r["support"]) * sum(abs(sp.Rational(v)) for _, v in r["entries"])
            for r in case["creators"]
            if i in r["support"]
        )
        for i in range(len(dims))
    ]
    reduced_mass = [
        sum(
            (len(r["support"]) - 1) * sum(abs(sp.Rational(v)) for _, v in r["entries"])
            for r in case["creators"]
            if i in r["support"]
        )
        for i in range(len(dims))
    ]
    m, k = max(mass), max(reduced_mass)
    weighted = max(
        sum(
            2 ** len(r["support"]) * sum(abs(sp.Rational(v)) for _, v in r["entries"])
            for r in case["creators"]
            if i in r["support"]
        )
        for i in range(len(dims))
    )
    assert weighted == sp.Rational(case["rooted_weight2_upper"])
    assert bool(weighted <= sp.Rational(1, 8)) == case["within_rooted_one_eighth_ball"]
    assert m == sp.Rational(case["M1_upper"]) and k == sp.Rational(case["K1_upper"])
    g = 1 - k - m * m
    assert g == sp.Rational(case["g_lower"]) > 0
    if weighted <= sp.Rational(1, 8):
        assert m <= sp.Rational(1, 16) and k <= sp.Rational(1, 32)
        assert g >= sp.Rational(247, 256)
    assert replay_psd(h, case["hamiltonian_psd"]) == size - 1
    assert replay_psd(h * h - g * h, case["H_squared_minus_gH_psd"]) == size - 1
    assert (
        replay_psd(h - g * (sp.eye(size) - projection), case["H_minus_g_orthogonal_complement_psd"])
        == size - 1
    )
    for p, c in zip(parents, case["idempotent_singular_controls"], strict=True):
        replay_psd((p.T * p) ** 2 - p.T * p, c)
    for row in case["overlap_commutator_controls"]:
        x, y = row["creators"]
        c = operators[x] * operators[y].T - operators[y].T * operators[x]
        bound2 = norms_squared[x] * norms_squared[y]
        assert bound2 == sp.Rational(row["bound_squared"])
        replay_psd(bound2 * sp.eye(size) - c.T * c, row["certificate"])
    linear_only = sum((qi - ai - ai.T for qi, ai in zip(q, anchors, strict=True)), sp.zeros(size))
    witness = (psi.T * linear_only * psi)[0]
    assert witness == sp.Rational(case["negative_control"]["psi_T_H_linear_psi"]) < 0
    return {"name": case["name"], "dimension": size, "g": str(g), "success": True}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--certificate", type=Path, required=True)
    parser.add_argument("--source", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    if args.output.exists():
        raise FileExistsError(f"Refusing to overwrite {args.output}")
    data = json.loads(args.certificate.read_text(encoding="utf-8"))
    assert data["success"] is True
    assert data["schema"] == "workhouse-creator-parent-finite-controls/v1"
    assert data["source_sha256"] == hashlib.sha256(args.source.read_bytes()).hexdigest()
    records = [rebuild(case) for case in data["models"]]
    # Ensure altered gap evidence is detected, not accepted as trusted JSON.
    altered = dict(data["models"][0]["hamiltonian_psd"])
    altered["diagonal"] = [*altered["diagonal"]]
    altered["diagonal"][0] = str(sp.Rational(altered["diagonal"][0]) + 1)
    broken = json.loads(json.dumps(data["models"][0]))
    broken["hamiltonian_psd"] = altered
    try:
        rebuild(broken)
    except AssertionError:
        pass
    else:
        raise AssertionError("Altered PSD factorization was not rejected")
    output = {
        "schema": "workhouse-creator-parent-independent-replay/v1",
        "success": True,
        "certificate_sha256": hashlib.sha256(args.certificate.read_bytes()).hexdigest(),
        "replayer_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "models": records,
        "altered_factorization_rejected": True,
    }
    args.output.write_text(json.dumps(output, indent=2) + "\n", encoding="utf-8", newline="\n")
    print(
        f"PASS independent reconstruction of {len(records)} parent-gap certificates; "
        "tamper control rejected"
    )


if __name__ == "__main__":
    main()
