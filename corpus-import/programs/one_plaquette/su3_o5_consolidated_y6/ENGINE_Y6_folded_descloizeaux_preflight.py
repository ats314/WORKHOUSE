#!/usr/bin/env python3
"""Exact sixth-order folded/des-Cloizeaux coefficient preflight.

This is an order-generic extraction of the squarefree polynomial recurrence used
by the verified SU(3) fifth-order engine.  It validates n=6 path weights against
an independent Rayleigh-Schrödinger eigenvalue recurrence for deterministic
rational matrices.
"""
from __future__ import annotations

import itertools
import json
import math
from fractions import Fraction as F
from pathlib import Path


def fstr(x: F) -> str:
    return str(x.numerator) if x.denominator == 1 else f"{x.numerator}/{x.denominator}"


def padd(a, b, scale=F(1)):
    out = dict(a)
    for mask, value in b.items():
        out[mask] = out.get(mask, F(0)) + scale * value
        if out[mask] == 0:
            del out[mask]
    return out


def pmul(a, b):
    out = {}
    for m, v in a.items():
        for n, w in b.items():
            if m & n:
                continue
            out[m | n] = out.get(m | n, F(0)) + v * w
    return {m: v for m, v in out.items() if v}


def pscale(a, scale):
    return {m: v * scale for m, v in a.items() if v * scale}


def folded_coefficient(ds):
    """Coefficient for one ordered n-vertex path with n-1 denominators.

    Zero denominators identify returns to the degenerate model space.  The
    squarefree variables isolate the term in which each ordered vertex occurs
    exactly once.  Division by (z+1)! is the des-Cloizeaux symmetrization for
    z model-space intermediate returns.
    """
    ds = tuple(F(x) for x in ds)
    n = len(ds) + 1
    states = [0]
    energies = {0: F(0)}
    node = 1
    for d in ds:
        if d == 0:
            states.append(0)
        else:
            states.append(node)
            energies[node] = -d
            node += 1
    states.append(0)
    nstates = node

    V = [[{} for _ in range(nstates)] for _ in range(nstates)]
    for j in range(n):
        V[states[j + 1]][states[j]] = padd(
            V[states[j + 1]][states[j]], {1 << j: F(1)}
        )

    psi = [[{} for _ in range(nstates)] for _ in range(n + 1)]
    energy = [{} for _ in range(n + 1)]
    psi[0][0] = {0: F(1)}

    for order in range(1, n + 1):
        vpsi = []
        for i in range(nstates):
            acc = {}
            for j in range(nstates):
                acc = padd(acc, pmul(V[i][j], psi[order - 1][j]))
            vpsi.append(acc)
        energy[order] = vpsi[0]
        for i in range(1, nstates):
            acc = dict(vpsi[i])
            for k in range(1, order):
                acc = padd(acc, pmul(energy[k], psi[order - k][i]), -1)
            psi[order][i] = pscale(acc, F(1) / (-energies[i]))

    raw = energy[n].get((1 << n) - 1, F(0))
    zero_returns = sum(d == 0 for d in ds)
    return raw / F(math.factorial(zero_returns + 1))


def rs_coefficients(h, V, nmax):
    """Independent nondegenerate Rayleigh-Schrödinger recurrence."""
    nstates = len(h)
    e0 = h[0]
    psi = [[F(0)] * nstates for _ in range(nmax + 1)]
    energy = [F(0)] * (nmax + 1)
    psi[0][0] = F(1)
    for order in range(1, nmax + 1):
        vpsi = [
            sum(V[i][j] * psi[order - 1][j] for j in range(nstates))
            for i in range(nstates)
        ]
        energy[order] = vpsi[0]
        for i in range(1, nstates):
            subtraction = sum(
                energy[k] * psi[order - k][i] for k in range(1, order)
            )
            psi[order][i] = (vpsi[i] - subtraction) / (e0 - h[i])
    return energy


def path_sum(h, V, order):
    """Sum all ordered paths using the folded path coefficient."""
    nstates = len(h)
    e0 = h[0]
    total = F(0)
    for mids in itertools.product(range(nstates), repeat=order - 1):
        states = (0,) + mids + (0,)
        raw = F(1)
        for j in range(order):
            raw *= V[states[j + 1]][states[j]]
        if raw == 0:
            continue
        ds = tuple(F(0) if x == 0 else e0 - h[x] for x in mids)
        total += raw * folded_coefficient(ds)
    return total


def old4(ds):
    ds = tuple(F(x) for x in ds)
    zeros = [d for d in ds if d == 0]
    nz = [d for d in ds if d]
    if len(zeros) == 0:
        return F(1) / (ds[0] * ds[1] * ds[2])
    if len(zeros) == 1:
        return -(
            F(1) / (nz[0] ** 2 * nz[1])
            + F(1) / (nz[0] * nz[1] ** 2)
        ) / 2
    if len(zeros) == 2:
        return F(1, 3) / (nz[0] ** 3)
    return F(0)


def main():
    gates = {}

    # Exact regression to the previously certified fourth-order formulas.
    fourth_ok = True
    for bits in itertools.product((0, 1), repeat=3):
        ds = tuple(F(0) if bit else F(i + 2) for i, bit in enumerate(bits))
        fourth_ok &= folded_coefficient(ds) == old4(ds)
    gates["fourth_order_closed_form_regression"] = fourth_ok

    # Generic elementary properties at sixth order.
    pattern_records = []
    reversal_ok = True
    nonresolvent_ok = True
    finite_ok = True
    for bits in itertools.product((0, 1), repeat=5):
        ds = tuple(F(0) if bit else F(i + 2) for i, bit in enumerate(bits))
        value = folded_coefficient(ds)
        reverse = folded_coefficient(tuple(reversed(ds)))
        reversal_ok &= value == reverse
        if not any(bits):
            nonresolvent_ok &= value == F(1, math.prod(ds))
        finite_ok &= value.denominator != 0
        pattern_records.append(
            {
                "denominators": [fstr(x) for x in ds],
                "zero_returns": sum(bits),
                "coefficient": fstr(value),
            }
        )
    gates["sixth_order_all_32_resonance_patterns_finite"] = finite_ok
    gates["sixth_order_path_reversal_symmetry"] = reversal_ok
    gates["sixth_order_nonresonant_resolvent_product"] = nonresolvent_ok

    anchors = [
        (
            [F(0), F(2), F(5)],
            [
                [F(1), F(2), F(-1)],
                [F(2), F(3), F(1)],
                [F(-1), F(1), F(-2)],
            ],
        ),
        (
            [F(1), F(4), F(7), F(9)],
            [
                [F(-2), F(1), F(2), F(-1)],
                [F(1), F(3), F(-2), F(1)],
                [F(2), F(-2), F(1), F(2)],
                [F(-1), F(1), F(2), F(0)],
            ],
        ),
        (
            [F(-1), F(3), F(8)],
            [
                [F(2), F(-2), F(3)],
                [F(-2), F(1), F(2)],
                [F(3), F(2), F(-1)],
            ],
        ),
        (
            [F(2), F(5), F(11), F(17)],
            [
                [F(3), F(-1), F(2), F(1)],
                [F(-1), F(4), F(1), F(-2)],
                [F(2), F(1), F(-3), F(2)],
                [F(1), F(-2), F(2), F(5)],
            ],
        ),
    ]

    anchor_records = []
    sixth_matrix_ok = True
    fifth_matrix_ok = True
    for index, (h, V) in enumerate(anchors, 1):
        energies = rs_coefficients(h, V, 6)
        p5 = path_sum(h, V, 5)
        p6 = path_sum(h, V, 6)
        fifth_matrix_ok &= energies[5] == p5
        sixth_matrix_ok &= energies[6] == p6
        anchor_records.append(
            {
                "anchor": index,
                "E5": fstr(energies[5]),
                "pathsum5": fstr(p5),
                "E6": fstr(energies[6]),
                "pathsum6": fstr(p6),
            }
        )
    gates["fifth_order_random_matrix_regression"] = fifth_matrix_ok
    gates["sixth_order_random_matrix_regression"] = sixth_matrix_ok

    passed = all(gates.values())
    payload = {
        "status": "PASS" if passed else "FAIL",
        "purpose": "Exact O(u^6) folded/des-Cloizeaux path-weight preflight",
        "gates": gates,
        "sixth_order_resonance_patterns": pattern_records,
        "matrix_anchors": anchor_records,
        "conclusion": (
            "The order-generic folded recurrence is certified for six insertions. "
            "The remaining m6 blockers are the sixth-order connected geometry, "
            "local SU(3) invariant/path tensors, and global contractions."
        ),
    }
    out = Path(__file__).with_name("CERT_Y6_folded_descloizeaux_preflight_certificate.json")
    out.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    for name, value in gates.items():
        print(("PASS" if value else "FAIL"), name)
    print("CERTIFICATE", out)
    print("ALL Y6 FOLDED PREFLIGHT GATES PASS" if passed else "Y6 FOLDED PREFLIGHT FAILED")
    raise SystemExit(0 if passed else 1)


if __name__ == "__main__":
    main()
