#!/usr/bin/env python3
"""Exact, standard-library certificate for the finite-N SU(3) -> t_N B B^dagger bridge.

This program does not import any WORKHOUSE coefficient table.  It rebuilds the
SU(3) channel weights from dimensions, Casimirs, and the dimension-ratio matrix
element printed as Eq. (D1) of arXiv:2503.11888v5.  It also constructs the
oriented cubical boundary matrix directly and checks the proposed small-volume
spectral fingerprints over the rationals.
"""

import argparse
import json
from fractions import Fraction as F
from pathlib import Path


def check(name, condition, detail=""):
    if not condition:
        raise AssertionError(f"FAIL: {name}: {detail}")
    print(f"PASS: {name}" + (f" :: {detail}" if detail else ""))


def rank_q(matrix):
    """Exact row rank over Q."""
    a = [[F(x) for x in row] for row in matrix]
    if not a:
        return 0
    nrow, ncol = len(a), len(a[0])
    r = 0
    for c in range(ncol):
        pivot = next((i for i in range(r, nrow) if a[i][c]), None)
        if pivot is None:
            continue
        a[r], a[pivot] = a[pivot], a[r]
        p = a[r][c]
        a[r] = [x / p for x in a[r]]
        for i in range(r + 1, nrow):
            if a[i][c]:
                z = a[i][c]
                a[i] = [x - z * y for x, y in zip(a[i], a[r])]
        r += 1
        if r == nrow:
            break
    return r


def transpose(a):
    return [list(row) for row in zip(*a)]


def matmul(a, b):
    bt = transpose(b)
    return [[sum(x * y for x, y in zip(row, col)) for col in bt] for row in a]


def shifted(a, lam):
    return [
        [x - (lam if i == j else 0) for j, x in enumerate(row)]
        for i, row in enumerate(a)
    ]


def periodic_boundary_2(L):
    """Return the edge-by-face matrix of d_2 on the periodic L^3 cube complex."""
    points = [(x, y, z) for x in range(L) for y in range(L) for z in range(L)]
    edges = [(x, a) for x in points for a in range(3)]
    faces = [(x, a, b) for x in points for a in range(3) for b in range(a + 1, 3)]
    edge_id = {e: i for i, e in enumerate(edges)}
    d = [[0 for _ in faces] for _ in edges]

    def step(x, a):
        y = list(x)
        y[a] = (y[a] + 1) % L
        return tuple(y)

    for j, (x, a, b) in enumerate(faces):
        boundary = [
            ((x, a), +1),
            ((step(x, a), b), +1),
            ((step(x, b), a), -1),
            ((x, b), -1),
        ]
        for e, sign in boundary:
            d[edge_id[e]][j] += sign
    return d


def open_cube_boundary_2():
    """Return d_2 for the six coordinate faces of one open unit cube."""
    edges = []
    for a in range(3):
        for x0 in (0, 1):
            for x1 in (0, 1):
                x = [0, 0, 0]
                others = [i for i in range(3) if i != a]
                x[others[0]], x[others[1]] = x0, x1
                edges.append((tuple(x), a))
    edge_id = {e: i for i, e in enumerate(edges)}
    faces = []
    for a in range(3):
        for b in range(a + 1, 3):
            c = next(i for i in range(3) if i not in (a, b))
            for side in (0, 1):
                x = [0, 0, 0]
                x[c] = side
                faces.append((tuple(x), a, b))
    d = [[0 for _ in faces] for _ in edges]

    def step(x, a):
        y = list(x)
        y[a] += 1
        return tuple(y)

    for j, (x, a, b) in enumerate(faces):
        boundary = [
            ((x, a), +1),
            ((step(x, a), b), +1),
            ((step(x, b), a), -1),
            ((x, b), -1),
        ]
        for e, sign in boundary:
            d[edge_id[e]][j] += sign
    return d


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, help="write a machine-readable JSON certificate")
    args = parser.parse_args()

    # SU(3) representation data, independently transcribed from Appendix C.
    N = 3
    c_f = F(N * N - 1, 2 * N)
    data = {
        "1": (1, F(0)),
        "8": (N * N - 1, F(N)),
        "bar3": (N * (N - 1) // 2, F((N + 1) * (N - 2), N)),
        "6": (N * (N + 1) // 2, F((N - 1) * (N + 2), N)),
    }
    weights = {}
    for rho, (dim, casimir) in data.items():
        matrix_element_sq = F(dim, N * N)  # Eq. (D1) squared.
        gap = c_f + casimir / 2
        weights[rho] = -matrix_element_sq / gap

    expected = {"1": -F(1, 12), "8": -F(16, 51), "bar3": -F(1, 6), "6": -F(2, 9)}
    check("four SU(3) channel weights", weights == expected, str(weights))
    a3 = weights["1"] + weights["8"]
    b3 = weights["bar3"] + weights["6"]
    t3 = b3 - a3
    check("A_3", a3 == -F(27, 68), str(a3))
    check("B_3", b3 == -F(7, 18), str(b3))
    check("t_3", t3 == F(5, 612), str(t3))
    closed_t3 = F(2 * N * (N * N - 4), (N * N - 1) * (2 * N * N - 1) * (4 * N * N - 9))
    check("all-rank closed law at N=3", t3 == closed_t3, str(closed_t3))
    cutoff_t3 = weights["bar3"] - weights["1"]
    check("p+q<=1 projected hopping has opposite sign", cutoff_t3 == -F(1, 12), str(cutoff_t3))
    omitted_completion = weights["6"] - weights["8"]
    check("omitted 6 and 8 channels exactly complete T1", cutoff_t3 + omitted_completion == t3, str(omitted_completion))

    # One open cube: exact rational nullities determine the full spectrum.
    d_open = open_cube_boundary_2()
    l_open = matmul(transpose(d_open), d_open)
    open_mult = {lam: 6 - rank_q(shifted(l_open, lam)) for lam in (0, 4, 6)}
    check("one-cube spectrum", open_mult == {0: 1, 4: 3, 6: 2}, str(open_mult))
    open_t_spectrum = {lam * t3: mult for lam, mult in open_mult.items()}
    check(
        "one-cube t_3 spectrum",
        open_t_spectrum == {F(0): 1, F(5, 153): 3, F(5, 102): 2},
        str(open_t_spectrum),
    )
    open_t1_spectrum = {lam * cutoff_t3: mult for lam, mult in open_mult.items()}
    check(
        "one-cube T1 spectrum has reversed sign",
        open_t1_spectrum == {F(0): 1, -F(1, 3): 3, -F(1, 2): 2},
        str(open_t1_spectrum),
    )
    check("full and T1 cube orderings are opposite", min(open_t_spectrum) == 0 and min(open_t1_spectrum) == -F(1, 2))

    # Absolute vacuum-subtracted O(u^2) blocks on the open cube.  T1 has a
    # 3/4 same-face term; restoring the omitted local sextet route (-1/4)
    # gives the full 1/2.  The vacuum route contributes +3/4 to each
    # neighboring-face leakage in this C-odd gap convention.
    t1_self, full_self = F(3, 4), F(1, 2)
    t1_leak = weights["1"] + weights["bar3"] + F(3, 4)
    full_leak = sum(weights.values(), F(0)) + F(3, 4)
    check("open-cube T1 leakage", t1_leak == F(1, 2), str(t1_leak))
    check("open-cube full leakage", full_leak == -F(11, 306), str(full_leak))
    t1_g_scalar = t1_self + 4 * t1_leak - 4 * cutoff_t3
    full_g_scalar = full_self + 4 * full_leak - 4 * t3
    counterterm_scalar = full_g_scalar - t1_g_scalar
    check(
        "open-cube complete scalar counterterm",
        (t1_g_scalar, full_g_scalar, counterterm_scalar) == (F(37, 12), F(11, 34), -F(563, 204)),
        str((t1_g_scalar, full_g_scalar, counterterm_scalar)),
    )
    open_t1_absolute = {t1_g_scalar + lam * cutoff_t3: mult for lam, mult in open_mult.items()}
    open_full_absolute = {full_g_scalar + lam * t3: mult for lam, mult in open_mult.items()}
    check(
        "open-cube absolute O(u^2) coefficient spectra",
        open_t1_absolute == {F(37, 12): 1, F(11, 4): 3, F(31, 12): 2}
        and open_full_absolute == {F(11, 34): 1, F(109, 306): 3, F(19, 51): 2},
        str((open_t1_absolute, open_full_absolute)),
    )

    # Periodic L=3: all 81 face modes are accounted for exactly.
    d3 = periodic_boundary_2(3)
    l3 = matmul(transpose(d3), d3)
    mult3 = {lam: 81 - rank_q(shifted(l3, lam)) for lam in (0, 3, 6, 9)}
    check("periodic L=3 spectrum", mult3 == {0: 29, 3: 12, 6: 24, 9: 16}, str(mult3))
    check("periodic L=3 multiplicities exhaust face space", sum(mult3.values()) == 81)
    t_spectrum3 = {lam * t3: mult for lam, mult in mult3.items()}
    check(
        "periodic L=3 t_3 spectrum",
        t_spectrum3
        == {F(0): 29, F(5, 204): 12, F(5, 102): 24, F(5, 68): 16},
        str(t_spectrum3),
    )
    print("PASS: 18/18 exact bridge gates")

    def q(value):
        return str(value)

    certificate = {
        "schema": "finite-n-su3-bbdagger-bridge/v1",
        "status": "PASS",
        "exact_gate_count": 18,
        "canonical_hamiltonian": "H_dimensionless = (1/2) sum E^2 - u sum(Box+Box^dagger)",
        "published_coupling_dictionaries": {
            "Ciavarella-Burbano-Bauer_arXiv_2503.11888v5": "u=1/(2*g^4) after H/g^2",
            "Balaji_et_al_arXiv_2509.25865v3": "u=1/g^4 after dropping the constant and dividing H by g^2",
        },
        "su3_channels": {
            rho: {
                "dimension": dim,
                "casimir": q(casimir),
                "matrix_element_squared": q(F(dim, N * N)),
                "resolvent_weight": q(weights[rho]),
            }
            for rho, (dim, casimir) in data.items()
        },
        "coefficients": {
            "A3": q(a3),
            "B3": q(b3),
            "t3_T1": q(cutoff_t3),
            "omitted_6_minus_8_completion": q(omitted_completion),
            "t3_channel_complete": q(t3),
        },
        "open_cube": {
            "BBdagger_eigenvalue_multiplicities": {str(k): v for k, v in open_mult.items()},
            "T1_relative_u2_spectrum": {q(k): v for k, v in open_t1_spectrum.items()},
            "complete_relative_u2_spectrum": {q(k): v for k, v in open_t_spectrum.items()},
            "T1_absolute_u2_coefficients": {q(k): v for k, v in open_t1_absolute.items()},
            "complete_absolute_u2_coefficients": {q(k): v for k, v in open_full_absolute.items()},
            "counterterm": {
                "identity_coefficient": q(counterterm_scalar),
                "BBdagger_coefficient": q(omitted_completion),
            },
        },
        "periodic_L3": {
            "face_dimension": 81,
            "BBdagger_eigenvalue_multiplicities": {str(k): v for k, v in mult3.items()},
            "complete_relative_u2_spectrum": {q(k): v for k, v in t_spectrum3.items()},
        },
        "claim_boundary": "Exact through second order in the charge-odd one-plaquette sector; not a full finite-coupling T2 cube diagonalization.",
    }
    if args.output:
        args.output.write_text(json.dumps(certificate, indent=2) + "\n", encoding="utf-8")
        print(f"WROTE: {args.output}")


if __name__ == "__main__":
    main()
