"""Closed forms in N for the pair clusters and the assembled beta, and the symbolic identity.

    python reconstruct_beta.py > reconstruct.log

From certificate.json: the lowest-degree rational function through the first
dp + dq + 1 ranks that reproduces every remaining rank, for the coplanar and
perpendicular pair clusters, the coplanar dressings, C_shp and beta. Then the
identity beta_assembled(N) == P17(N^2)/(N R20(N^2)) is checked symbolically
with sympy, using the corpus polynomials transcribed in workhouse.channel_ledger.
Writes closed_forms.json. Exact linear algebra in flint; no floating point.
"""

from __future__ import annotations

import json
import sys
from fractions import Fraction as F
from pathlib import Path

import flint
from sympy import Rational, Symbol, cancel, factor

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
sys.path.insert(0, str(ROOT / "src"))
from workhouse.channel_ledger import P17, R20, _z  # noqa: E402

cert = json.loads((HERE / "certificate.json").read_text(encoding="utf-8"))
N = Symbol("N")


def fq(x: F):
    return flint.fmpq(x.numerator, x.denominator)


def solve_rational(points, dp, dq):
    m = dp + dq + 1
    A = flint.fmpq_mat(m, m)
    b = flint.fmpq_mat(m, 1)
    for r, (n, v) in enumerate(points[:m]):
        nq = flint.fmpq(n)
        for i in range(dp + 1):
            A[r, i] = nq**i
        for j in range(dq):
            A[r, dp + 1 + j] = -fq(v) * nq**j
        b[r, 0] = fq(v) * nq**dq
    try:
        sol = A.solve(b)
    except Exception:
        return None
    pc = [F(int(sol[i, 0].p), int(sol[i, 0].q)) for i in range(dp + 1)]
    qc = [F(int(sol[dp + 1 + j, 0].p), int(sol[dp + 1 + j, 0].q)) for j in range(dq)] + [F(1)]
    return pc, qc


def evaluate(pc, qc, n):
    p = sum(c * F(n) ** i for i, c in enumerate(pc))
    q = sum(c * F(n) ** j for j, c in enumerate(qc))
    return p / q if q else None


def reconstruct(points, max_dp=30, max_diff=14, min_hold=6):
    for total in range(0, 2 * max_dp + max_diff):
        for d in range(0, max_diff):
            if (total - d) % 2:
                continue
            dp = (total - d) // 2
            dq = dp + d
            if dp < 0 or dp > max_dp:
                continue
            need = dp + dq + 1
            if len(points) - need < min_hold:
                continue
            sol = solve_rational(points, dp, dq)
            if sol is None:
                continue
            pc, qc = sol
            if all(evaluate(pc, qc, n) == v for n, v in points[need:]):
                P = sum(Rational(c.numerator, c.denominator) * N**i for i, c in enumerate(pc))
                Q = sum(Rational(c.numerator, c.denominator) * N**j for j, c in enumerate(qc))
                return dp, dq, cancel(P / Q), len(points) - need
    return None


def reconstruct_parity(points):
    """Try N^s g(N^2) for s in (-1, 0, 1) first (the corpus's beta_N is N^-1 P17(N^2)/R20(N^2),
    and every cumulant seen so far has a definite parity), then a general form in N."""
    for s_pow in (-1, 0, 1):
        pts_z = [(n * n, v / F(n) ** s_pow) for n, v in points]
        res = reconstruct(pts_z)
        if res is not None:
            dp, dq, g, held = res
            return dp, dq, cancel(N**s_pow * g.subs(N, N**2)), held, f"N^{s_pow} g(N^2)"
    res = reconstruct(points)
    if res is None:
        return None
    dp, dq, expr, held = res
    return dp, dq, expr, held, "g(N)"


# the reconstruction's domain: the ranks where the pair cluster was computed (N >= 5)
ranks = sorted(int(k) for k, row in cert["ranks"].items() if row["pair_coplanar"] is not None)
out = {}
KEYS = ("pair_coplanar", "pair_perpendicular", "single_coplanar", "fan_coplanar", "C_shp", "beta_assembled")
for key in KEYS:
    pts = [(n, F(cert["ranks"][str(n)][key])) for n in ranks]
    res = reconstruct_parity(pts)
    if res is None:
        print(f"{key}: NOT FOUND with {len(pts)} ranks", flush=True)
        continue
    dp, dq, expr, held, shape = res
    out[key] = {"form": str(expr), "degrees_in_z": [dp, dq], "shape": shape, "held_out": held}
    print(f"{key}: {shape} ({dp},{dq}) held-out {held}: {factor(expr)}", flush=True)

if "beta_assembled" in out:
    from sympy import sympify

    beta = sympify(out["beta_assembled"]["form"], locals={"N": N})
    corpus = P17.as_expr().subs(_z, N**2) / (N * R20.as_expr().subs(_z, N**2))
    diff = cancel(beta - corpus)
    out["identity"] = {"beta_assembled_minus_corpus": str(diff), "holds": diff == 0}
    print("beta_assembled(N) - P17(N^2)/(N R20(N^2)) =", diff, flush=True)
(HERE / "closed_forms.json").write_text(json.dumps(out, indent=1) + "\n", encoding="utf-8", newline="\n")
print("wrote closed_forms.json", flush=True)
