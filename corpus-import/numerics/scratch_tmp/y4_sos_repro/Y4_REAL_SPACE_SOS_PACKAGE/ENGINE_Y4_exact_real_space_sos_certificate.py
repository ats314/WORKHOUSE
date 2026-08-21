#!/usr/bin/env python3
"""
Y4 exact real-space sum-of-squares certificate
================================================

Proves, in exact rational Laurent arithmetic, that the complete SU(3)
fourth-order 189-record plaquette kernel satisfies

    C^† (H4 - q I) C
      = (A/4) sum_i L_i^2 + (B/4) sum_{i<j} L_i L_j,

where C is the oriented cube-boundary map, L_i=(T_i-I)^†(T_i-I),
A=5/12, and B=17607806155349/275331901291200.

The output is a local 25-point scalar stencil and a manifestly positive
sum-of-squares quadratic form.  No floating-point arithmetic is used in the
proof gates.
"""
from __future__ import annotations

import argparse
import gzip
import hashlib
import json
from collections import defaultdict
from fractions import Fraction as F
from pathlib import Path
from typing import Dict, Iterable, Tuple

Exp = Tuple[int, int, int]
Poly = Dict[Exp, F]
ZERO: Exp = (0, 0, 0)
PLANES = ((0, 1), (0, 2), (1, 2))
A = F(5, 12)
B = F(17607806155349, 275331901291200)
Q0 = F(-20721577909065127111, 7250590288602460800)
EXPECTED_KERNEL_RECORDS = 189
EXPECTED_SEMANTIC_KERNEL_SHA256 = (
    "48a422a517c7c1e70b84fd88a0773943f81ae3f9bfafadbe2304f8eb7d2e9b77"
)


def gate(name: str, condition: bool, detail: str = "") -> None:
    print(f"{'PASS' if condition else 'FAIL':4s} {name:62s} {detail}")
    if not condition:
        raise AssertionError(f"{name}: {detail}")


def recursive_find(filename: str) -> Path | None:
    preferred = [
        Path("/content") / filename,
        Path("/content/Y4_STAGE3J") / filename,
        Path.cwd() / filename,
        Path.cwd() / "Y4_STAGE3J" / filename,
        Path("/mnt/data") / filename,
        Path("/mnt/data/_sos_pipeline/Y4_STAGE3J") / filename,
    ]
    for path in preferred:
        if path.exists():
            return path
    for root in (Path("/content"), Path.cwd(), Path("/mnt/data")):
        if root.exists():
            for path in root.rglob(filename):
                return path
    return None


def load_kernel(path: Path) -> dict:
    opener = gzip.open if path.suffix == ".gz" else open
    with opener(path, "rt", encoding="utf-8") as handle:
        return json.load(handle)


def canonical_kernel_sha(records: list[dict]) -> str:
    payload = json.dumps(records, sort_keys=True, separators=(",", ":")).encode()
    return hashlib.sha256(payload).hexdigest()


def clean(poly: Dict[Exp, F]) -> Poly:
    return {e: c for e, c in poly.items() if c}


def add(*polys: Poly) -> Poly:
    out: Dict[Exp, F] = defaultdict(F)
    for poly in polys:
        for e, c in poly.items():
            out[e] += c
    return clean(out)


def scale(poly: Poly, scalar: F) -> Poly:
    return clean({e: scalar * c for e, c in poly.items()})


def mul(left: Poly, right: Poly) -> Poly:
    out: Dict[Exp, F] = defaultdict(F)
    for e, c in left.items():
        for f, d in right.items():
            out[tuple(e[i] + f[i] for i in range(3))] += c * d
    return clean(out)


def shift(poly: Poly, displacement: Exp, scalar: F = F(1)) -> Poly:
    return clean({
        tuple(e[i] + displacement[i] for i in range(3)): scalar * c
        for e, c in poly.items()
    })


def adjoint(poly: Poly) -> Poly:
    return {tuple(-x for x in e): c for e, c in poly.items()}


def monomial(exp: Exp, coefficient: F = F(1)) -> Poly:
    return {exp: coefficient}


def direction_exp(axis: int, amount: int = 1) -> Exp:
    e = [0, 0, 0]
    e[axis] = amount
    return tuple(e)  # type: ignore[return-value]


def cube_boundary_symbol() -> tuple[Poly, Poly, Poly]:
    # Cell/origin gauge, basis planes (01,02,12):
    # psi=(z_2-1, -(z_1-1), z_0-1)^T.
    return (
        add(monomial(direction_exp(2)), monomial(ZERO, F(-1))),
        add(monomial(ZERO), monomial(direction_exp(1), F(-1))),
        add(monomial(direction_exp(0)), monomial(ZERO, F(-1))),
    )


def laplacian_symbol(axis: int) -> Poly:
    # L_i=(T_i-I)^†(T_i-I)=2-T_i-T_i^{-1}.
    return {
        ZERO: F(2),
        direction_exp(axis, +1): F(-1),
        direction_exp(axis, -1): F(-1),
    }


def exact_contracted_kernel(payload: dict) -> tuple[Poly, F]:
    records = payload["kernel"]
    planes = tuple(tuple(p) for p in payload["meta"]["basis_planes"])
    plane_index = {plane: index for index, plane in enumerate(planes)}
    psi = cube_boundary_symbol()

    # Derive q from H4(0) rather than trusting a copied constant.
    h0 = [[F(0) for _ in range(3)] for _ in range(3)]
    for record in records:
        a = plane_index[tuple(record["input_plane"])]
        b = plane_index[tuple(record["output_plane"])]
        h0[b][a] += F(record["weight"])
    q = h0[0][0]

    out: Dict[Exp, F] = defaultdict(F)
    for record in records:
        a = plane_index[tuple(record["input_plane"])]
        b = plane_index[tuple(record["output_plane"])]
        displacement = tuple(int(x) for x in record["displacement"])
        weight = F(record["weight"])
        factor = mul(adjoint(psi[b]), psi[a])
        for e, c in shift(factor, displacement, weight).items():
            out[e] += c

    for a in range(3):
        for e, c in mul(adjoint(psi[a]), psi[a]).items():
            out[e] -= q * c
    return clean(out), q


def sos_polynomial() -> Poly:
    laps = [laplacian_symbol(i) for i in range(3)]
    terms = []
    for i in range(3):
        terms.append(scale(mul(laps[i], laps[i]), A / 4))
    for i in range(3):
        for j in range(i + 1, 3):
            terms.append(scale(mul(laps[i], laps[j]), B / 4))
    return add(*terms)


def expected_stencil() -> Poly:
    w0 = F(9, 2) * A + 3 * B
    w1 = -(A + B)
    w2 = A / 4
    wd = B / 4
    out: Dict[Exp, F] = defaultdict(F)
    out[ZERO] = w0
    for i in range(3):
        out[direction_exp(i, +1)] += w1
        out[direction_exp(i, -1)] += w1
        out[direction_exp(i, +2)] += w2
        out[direction_exp(i, -2)] += w2
    for i in range(3):
        for j in range(i + 1, 3):
            for si in (-1, +1):
                for sj in (-1, +1):
                    e = [0, 0, 0]
                    e[i] = si
                    e[j] = sj
                    out[tuple(e)] += wd
    return clean(out)


def periodic_convolution(field: dict[Exp, F], stencil: Poly, L: int) -> dict[Exp, F]:
    out: Dict[Exp, F] = defaultdict(F)
    for x, value in field.items():
        for r, weight in stencil.items():
            y = tuple((x[i] - r[i]) % L for i in range(3))
            out[y] += weight * value
    return clean(out)


def finite_torus_gate(left: Poly, right: Poly, L: int = 7) -> bool:
    # Deterministic integer test field; L=7 avoids aliasing of offsets <=2.
    field = {
        (x, y, z): F((3 * x + 5 * y + 7 * z + 11 * x * y + 13 * z * z) % 17 - 8)
        for x in range(L)
        for y in range(L)
        for z in range(L)
    }
    return periodic_convolution(field, left, L) == periodic_convolution(field, right, L)


def fstr(value: F) -> str:
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--kernel", type=Path, default=None)
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=(
            Path("/content/Y4_REAL_SPACE_SOS")
            if Path("/content").exists()
            else Path("/mnt/data/Y4_REAL_SPACE_SOS")
        ),
    )
    args, _unknown = parser.parse_known_args()

    kernel_path = args.kernel or recursive_find("DATA_Y4_full_real_space_h4_kernel.json.gz")
    if kernel_path is None:
        kernel_path = recursive_find("CERT_Y4_full_real_space_h4_kernel.json")
    assert kernel_path is not None, "Missing CERT_Y4_full_real_space_h4_kernel.json[.gz]"

    args.output_dir.mkdir(parents=True, exist_ok=True)
    payload = load_kernel(kernel_path)
    records = payload["kernel"]

    print("=" * 104)
    print("SU(3) O(y^4) EXACT REAL-SPACE SUM-OF-SQUARES CERTIFICATE")
    print("=" * 104)
    print("kernel :", kernel_path)
    print("output :", args.output_dir)
    print("mode   : exact fractions; CPU only")
    print()

    gate("kernel record count", len(records) == EXPECTED_KERNEL_RECORDS, str(len(records)))
    gate(
        "basis planes",
        tuple(tuple(p) for p in payload["meta"]["basis_planes"]) == PLANES,
        str(payload["meta"]["basis_planes"]),
    )
    semantic_sha = canonical_kernel_sha(records)
    gate(
        "semantic kernel SHA-256",
        semantic_sha == EXPECTED_SEMANTIC_KERNEL_SHA256,
        semantic_sha,
    )

    # Exact real-space Hermiticity.
    record_map = {
        (
            tuple(r["input_plane"]),
            tuple(r["output_plane"]),
            tuple(r["displacement"]),
        ): F(r["weight"])
        for r in records
    }
    hermitian = all(
        record_map.get((b, a, tuple(-x for x in d)), F(0)) == w
        for (a, b, d), w in record_map.items()
    )
    gate("exact real-space Hermiticity", hermitian)

    contracted, q = exact_contracted_kernel(payload)
    sos = sos_polynomial()
    stencil = expected_stencil()

    gate("H4(0) scalar q", q == Q0, fstr(q))
    gate("contracted Laurent support", len(contracted) == 25, str(len(contracted)))
    gate("exact SOS Laurent identity", contracted == sos)
    gate("exact 25-point stencil identity", contracted == stencil)
    gate("finite L=7 real-space convolution regression", finite_torus_gate(contracted, stencil))

    w0 = stencil[ZERO]
    w1 = stencil[(1, 0, 0)]
    w2 = stencil[(2, 0, 0)]
    wd = stencil[(1, 1, 0)]
    row_sum = sum(stencil.values(), F(0))
    gate("stencil center weight", w0 == F(189690244462349, 91777300430400), fstr(w0))
    gate("stencil nearest-axis weight", w1 == F(-132329431693349, 275331901291200), fstr(w1))
    gate("stencil double-axis weight", w2 == F(5, 48), fstr(w2))
    gate("stencil face-diagonal weight", wd == F(17607806155349, 1101327605164800), fstr(wd))
    gate("stencil annihilates constants", row_sum == 0, fstr(row_sum))
    gate("manifest SOS positivity", A > 0 and B > 0, f"A={fstr(A)}, B={fstr(B)}")

    # High-symmetry generalized eigenvalues lambda=D/G.
    # X=(2,0,0), M=(2,2,0), R=(2,2,2).
    lam_X = A
    lam_M = A + B / 2
    lam_R = A + B
    gate("X lift", lam_X == F(5, 12), fstr(lam_X))
    gate(
        "M/R consistency",
        2 * (lam_M - lam_X) == lam_R - lam_X == B,
        f"M={fstr(lam_M)}, R={fstr(lam_R)}",
    )
    gate(
        "exact bandwidth",
        lam_R == F(132329431693349, 275331901291200),
        fstr(lam_R),
    )

    stencil_records = [
        {"offset": list(e), "weight": fstr(c)}
        for e, c in sorted(stencil.items())
    ]
    result = {
        "title": "SU(3) fourth-order real-space SOS theorem",
        "status": "PASS",
        "kernel": {
            "path": str(kernel_path),
            "records": len(records),
            "semantic_sha256": semantic_sha,
            "stage3i_sha256": payload["meta"].get("stage3i_sha256"),
        },
        "constants": {
            "q": fstr(q),
            "A": fstr(A),
            "B": fstr(B),
            "bandwidth": fstr(A + B),
        },
        "operator_identity": (
            "C^dagger(H4-qI)C=(A/4)sum_i L_i^2+(B/4)sum_{i<j}L_iL_j, "
            "L_i=(T_i-I)^dagger(T_i-I)"
        ),
        "stencil": {
            "records": stencil_records,
            "center": fstr(w0),
            "nearest_axis": fstr(w1),
            "double_axis": fstr(w2),
            "face_diagonal": fstr(wd),
            "row_sum": fstr(row_sum),
        },
        "generalized_eigenproblem": {
            "metric": "G=C^dagger C=sum_i L_i",
            "equation": "Q phi=lambda G phi",
            "lambda_symbol": "[A sum_i X_i^2+B sum_{i<j}X_iX_j]/[2 sum_i X_i]",
        },
    }

    json_path = args.output_dir / "CERT_Y4_real_space_sos_certificate.json"
    json_path.write_text(json.dumps(result, indent=2, sort_keys=True), encoding="utf-8")
    stencil_path = args.output_dir / "CERT_Y4_real_space_sos_stencil.json"
    stencil_path.write_text(json.dumps({"stencil": stencil_records}, indent=2), encoding="utf-8")

    md = fr"""# Exact real-space sum-of-squares theorem for the SU(3) fourth-order lift

**Status:** PASS  
**Kernel records:** {len(records)}  
**Semantic kernel SHA-256:** `{semantic_sha}`

Let \(C=\partial_3\) be the cell/origin-gauge cube-boundary map with symbol

\[
\psi(k)=\bigl(e^{{ik_2}}-1,-(e^{{ik_1}}-1),e^{{ik_0}}-1\bigr)^T.
\]

For the complete fourth-order plaquette kernel \(H_4\),

\[
q={fstr(q)},\qquad A={fstr(A)},\qquad B={fstr(B)},
\]

and exact rational Laurent arithmetic proves

\[
\boxed{{
C^\dagger(H_4-qI)C
=\frac{{A}}4\sum_i L_i^2
+\frac{{B}}4\sum_{{i<j}}L_iL_j
}},
\qquad
L_i=(T_i-I)^\dagger(T_i-I).
\]

Equivalently,

\[
C^\dagger(H_4-qI)C
=\frac{{5}}{{48}}\sum_i L_i^2
+\frac{{17607806155349}}{{1101327605164800}}
\sum_{{i<j}}(\nabla_i\nabla_j)^\dagger(\nabla_i\nabla_j).
\]

This is a manifest local sum of squares.  In real space it is the 25-point stencil

\[
(Q\phi)_x=w_0\phi_x+w_1\sum_i(\phi_{{x+e_i}}+\phi_{{x-e_i}})
+w_2\sum_i(\phi_{{x+2e_i}}+\phi_{{x-2e_i}})
+w_d\sum_{{i<j}}\sum_{{\sigma,\tau=\pm1}}
\phi_{{x+\sigma e_i+\tau e_j}},
\]

with

\[
w_0={fstr(w0)},\quad
w_1={fstr(w1)},\quad
w_2={fstr(w2)},\quad
w_d={fstr(wd)},
\]

and \(w_0+6w_1+6w_2+12w_d=0\).

The cube-boundary states are not orthonormal. Their Gram operator is

\[
G=C^\dagger C=\sum_iL_i,
\]

so the physical fourth-order lift is the generalized eigenproblem

\[
Q\phi=\lambda G\phi,
\qquad
\lambda(k)=
\frac{{A\sum_iX_i^2+B\sum_{{i<j}}X_iX_j}}
{{2\sum_iX_i}},
\quad X_i=1-\cos k_i.
\]

The exact high-symmetry lifts are

\[
\lambda_X=A={fstr(lam_X)},\qquad
\lambda_M=A+\frac B2={fstr(lam_M)},\qquad
\lambda_R=A+B={fstr(lam_R)}.
\]
"""
    md_path = args.output_dir / "THM_Y4_real_space_sos_theorem.md"
    md_path.write_text(md, encoding="utf-8")

    print()
    print("ALL REAL-SPACE SOS GATES PASS")
    print("JSON   :", json_path)
    print("STENCIL:", stencil_path)
    print("MD     :", md_path)


if __name__ == "__main__":
    main()
