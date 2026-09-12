"""The single-face planar grading law over Q(N): orders two to ten, exactly.

ADR 0046 conjectured that the order-2k band coefficient is N^-(4k-1) while its
channels are N^-(2k-1), and verified it at k = 1, 2 on the fourth-order cluster
cumulants. The G9 suite of 2026-09-11 ("G9 direct sixth order on one face and
the shared-link pairs, any rank", runs/g9_direct_h6_pair_2026-09-11) then
established the one-face case at k = 3 exactly over Q(N), including the
N^-11 C-parity splitting at order six, and showed that the seven word-formula
pieces of (F6) are each O(N^-5). This run continues that line.

The object is the C-parity splitting of the one-plaquette diagonal,

    S_m(N) = odd_m - even_m = -2 K_m[0][1],

the off-diagonal Bloch matrix element between the two face words, computed by
the rank-generic character engine `workhouse.sixth_order_characters.bloch_series`
over the field Q(N).

What this run adds:

1. **Orders eight and ten (k = 4, 5)**, exactly: the exponent -(2m-1) and the
   planar coefficients c_8 = -123332/9 and c_10 = -49593808/135. Nothing in
   the corpus had gone past order six on this object.
2. **The planar coefficients of the splitting itself** at every even order
   through ten, and the tau-normalisation they imply: with u = N^2 tau/2 the
   order-m term is (c_m/2^m) N tau^m, so every even order carries the same
   single power of N and the single-face band per unit N is a function of tau
   alone, with b_2 = -1 and b_4 = -2 exactly.
3. **The irrep channel decomposition**, which is where the cancellation lives.
   Splitting S_m by the intermediate state of the perturbed vector gives four
   channels at every even m >= 4 -- the singlet ((), ()), the adjoint
   ((1,), (1,)), and the two two-box states ((2,), ()) and ((1,1), ()) -- each
   of order N^-(m-1), with leading coefficients (-4, +2, +1, +1) x 2^(m/2-2)
   summing to zero. This is a different decomposition from the word-formula
   pieces of (F6), and it is the one that explains ADR 0046's negative result:
   every channel has the SAME order, so no rule assigning an order per channel
   can reproduce the suppression.

An independent integer-N cross-check follows, using the one-plaquette character
engine of ADR 0047 (`odd_order.towers`, exact rationals at N <= 200) with
Richardson extrapolation in 1/N^2. It shares no primitive with the Q(N) engine.
"""

from __future__ import annotations

import json
import sys
import time
from fractions import Fraction
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "src"))

from workhouse import sixth_order_characters as CH  # noqa: E402
from workhouse.invariants import odd_order as OO  # noqa: E402

N = sp.Symbol("N")
ORDERS = (2, 4, 6, 8, 10)
CROSS_RANKS = list(range(60, 201, 20))


def rf(x):
    """A ``symbolic_rank`` rational function as a cancelled sympy expression."""
    return sp.cancel(x.to_sympy()) if hasattr(x, "to_sympy") else sp.cancel(x)


def _v(vec):
    """``V = chi_F + chi_F-bar`` on a character vector, as ``bloch_series`` applies it."""
    out = CH.multiply_fundamental(vec, False)
    for k, value in CH.multiply_fundamental(vec, True).items():
        out[k] = out.get(k, 0) + value
    return {k: value for k, value in out.items() if value}


def splitting_channels(series, m):
    """``S_m`` split by the intermediate state, exactly over Q(N).

    ``S_m = odd_m - even_m = -2 K_m[0][1]``, and ``K_m[0][1]`` is the coefficient
    of the first face word in ``V`` applied to the order-(m-1) perturbed vector
    of the second. The returned parts sum to ``S_m`` exactly; the caller asserts
    it.
    """
    model, chi = series["model"], series["chi"]
    out: dict = {}
    for state, coefficient in chi[m - 1][1].items():
        amplitude = _v({state: coefficient / coefficient}).get(model[0])
        if amplitude is None:
            continue
        out[state] = sp.cancel(-2 * rf(coefficient) * rf(amplitude))
    return {k: v for k, v in out.items() if v != 0}


def richardson(pairs, depth):
    """Extrapolate y(N) = c + a/N^2 + ... to N = infinity, exactly, ``depth`` times."""
    x = [Fraction(1, n * n) for n, _ in pairs]
    y = [v for _, v in pairs]
    for _ in range(depth):
        y = [(y[i + 1] * x[i] - y[i] * x[i + 1]) / (x[i] - x[i + 1]) for i in range(len(y) - 1)]
        x = x[:-1]
    return y[0]


def main() -> None:
    cert = {
        "orders": list(ORDERS),
        "exponent_law": {str(m): -(2 * m - 1) for m in ORDERS},
        "planar_coefficients": {},
        "tau_coefficients": {},
        "channels": {},
        "integer_rank_cross_check": {},
        "timing_s": {},
    }

    t0 = time.time()
    series = CH.bloch_series(max(ORDERS), CH.PLAQUETTE, sign=1)
    cert["timing_s"]["bloch_series"] = round(time.time() - t0, 1)
    print(f"Q(N) Bloch series to order {max(ORDERS)} in {cert['timing_s']['bloch_series']} s")

    print("1. the exponent law and the planar coefficients, exactly over Q(N)", flush=True)
    for m in ORDERS:
        s = sp.cancel(rf(series["odd"][m]) - rf(series["even"][m]))
        c = sp.nsimplify(sp.limit(s * N ** (2 * m - 1), N, sp.oo))
        if c == 0 or not c.is_finite:
            raise ArithmeticError(f"order {m}: N^{2 * m - 1} S_m is not a finite nonzero limit")
        b = sp.nsimplify(c / 2**m)
        cert["planar_coefficients"][str(m)] = str(c)
        cert["tau_coefficients"][str(m)] = str(b)
        print(f"   m = {m}:  S_m = ({c}) N^-{2 * m - 1} (1 + O(N^-2));  b_{m} = {b}", flush=True)

    print("2. where the cancellation lives: the irrep channels, exactly", flush=True)
    for m in ORDERS:
        parts = splitting_channels(series, m)
        total = sp.cancel(sum(parts.values()))
        target = sp.cancel(rf(series["odd"][m]) - rf(series["even"][m]))
        if sp.simplify(total - target) != 0:
            raise ArithmeticError(f"order {m}: the channel split is not a decomposition")
        entry = {}
        for state, value in sorted(parts.items(), key=str):
            lead = sp.nsimplify(sp.limit(value * N ** (m - 1), N, sp.oo))
            entry[str(state)] = str(lead)
        leads = [sp.Rational(v) for v in entry.values()]
        entry["_sum"] = str(sum(leads))
        entry["_scale"] = str(sp.Rational(2) ** (m // 2 - 2))
        cert["channels"][str(m)] = entry
        shown = ", ".join(f"{k} {v}" for k, v in entry.items() if not k.startswith("_"))
        print(f"   m = {m}:  N^-{m - 1} x [{shown}];  sum {entry['_sum']}", flush=True)

    print("3. independent integer-rank cross-check (ADR 0047 engine, N <= 200)", flush=True)
    t0 = time.time()
    rows = {n: OO.towers(n, 8) for n in CROSS_RANKS}
    for m in (2, 4, 6, 8):
        pairs = [
            (n, (rows[n][f"tower{m}_odd"] - rows[n][f"tower{m}_even"]) * Fraction(n) ** (2 * m - 1))
            for n in CROSS_RANKS
        ]
        got = float(richardson(pairs, 5))
        want = float(sp.Rational(cert["planar_coefficients"][str(m)]))
        cert["integer_rank_cross_check"][str(m)] = {
            "extrapolated": got,
            "exact": cert["planar_coefficients"][str(m)],
            "relative_gap": abs(got / want - 1),
        }
        print(f"   m = {m}: {got:.9f} vs exact {want:.9f}  (rel {abs(got / want - 1):.2e})")
    cert["timing_s"]["cross_check"] = round(time.time() - t0, 1)

    out = Path(__file__).resolve().parent / "certificate.json"
    out.write_text(json.dumps(cert, indent=1, sort_keys=True) + "\n", encoding="utf-8")
    print(f"wrote {out.name}", flush=True)


if __name__ == "__main__":
    main()
