"""Closed forms in N for every channel of u, reconstructed from certificate.json.

    python reconstruct_channels.py > reconstruct.log

For each labelled channel of the coplanar chain, the lowest-degree rational
function P/Q (Q monic) through the first dp + dq + 1 ranks that reproduces
every remaining rank exactly. Writes channel_closed_forms.json: label ->
{"form": sympy string, "degrees": [dp, dq], "held_out": k}. Exact linear
algebra in flint; no floating point anywhere.
"""

from __future__ import annotations

import json
import sys
from fractions import Fraction as F
from pathlib import Path

import flint
from sympy import Rational, Symbol, cancel

HERE = Path(__file__).resolve().parent
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


def reconstruct(points, max_dp=14, max_diff=12, min_hold=4):
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


ranks = sorted(int(k) for k in cert["ranks"])
labels = set()
for n in ranks:
    labels |= set(cert["ranks"][str(n)]["coplanar"]["channels"])
out = {}
for label in sorted(labels):
    pts = [(n, F(cert["ranks"][str(n)]["coplanar"]["channels"].get(label, "0"))) for n in ranks]
    res = reconstruct(pts)
    if res is None:
        print("NOT FOUND:", label, flush=True)
        continue
    dp, dq, expr, held = res
    out[label] = {"form": str(expr), "degrees": [dp, dq], "held_out": held}
    print(f"{label}: ({dp},{dq}) held-out {held}: {expr}", flush=True)
(HERE / "channel_closed_forms.json").write_text(json.dumps(out, indent=1) + "\n", encoding="utf-8", newline="\n")
print("wrote", len(out), "closed forms of", len(labels), "labels")
