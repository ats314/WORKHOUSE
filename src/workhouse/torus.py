"""The periodic cubical chain complex over Z, built rather than asserted.

The corpus's carrier count dim Z_2 = L^3 + 2 entered this repository as
arithmetic on a formula: (L^3 - 1) + 3 simplifies to L^3 + 2, and evaluates
correctly at L = 3, 4, 5. Neither step ever constructed a boundary map, so
neither could have noticed a wrong sign in d_2, a misindexed torus wrap, or a
formula that happened to match a miscounted kernel. This module carries out
the manuscript's own proof: build d_2 and d_3 from the printed boundary
formulas, and settle every rank by elimination.

Conventions (MASTER paper App. E; UNIFIED §0.1):

- sites x in (Z/L)^3, linear index x1 + L*(x2 + L*x3);
- edges [x; i], i in {1,2,3};
- faces [x; i,j], i < j, pair order (1,2), (1,3), (2,3);
- cubes [x; 1,2,3];
- d2 [x;i,j] = [x+ei; j] - [x; j] - [x+ej; i] + [x; i];
- d3 [x;1,2,3] = [x+e1;2,3] - [x;2,3] - [x+e2;1,3] + [x;1,3]
                 + [x+e3;1,2] - [x;1,2].

Matrices act on coefficient columns: D2(L) has one column per face and one
row per edge, D3(L) one column per cube and one row per face.

Two rank routes are kept deliberately distinct. `flint.fmpz_mat.rank` decides
the rank over Q exactly. The mod-p route bounds it from one side only —
rank drops under reduction, never rises — so nullity mod p bounds the kernel
from ABOVE, while an exhibited family of integer cycles of full rank bounds
it from BELOW. The two meet, which is the theorem.
"""

from __future__ import annotations

from itertools import product

import flint

#: Face directions in pair order (1,2), (1,3), (2,3).
FACE_PAIRS = ((1, 2), (1, 3), (2, 3))

#: A deliberately unremarkable prime for the one-sided mod-p bound.
DEFAULT_PRIME = 1_000_003


def _site(x, ell):
    return x[0] + ell * (x[1] + ell * x[2])


def _shift(x, i, ell):
    """x + e_i on the torus, i in {1,2,3}."""
    y = list(x)
    y[i - 1] = (y[i - 1] + 1) % ell
    return tuple(y)


def edge_index(x, i, ell):
    return 3 * _site(x, ell) + (i - 1)


def face_index(x, pair, ell):
    return 3 * _site(x, ell) + FACE_PAIRS.index(pair)


def sites(ell):
    return list(product(range(ell), repeat=3))


def d2_matrix(ell):
    """Face-to-edge boundary: rows edges, columns faces, entries in Z."""
    n = 3 * ell**3
    rows = [[0] * n for _ in range(n)]
    for x in sites(ell):
        for pair in FACE_PAIRS:
            i, j = pair
            col = face_index(x, pair, ell)
            rows[edge_index(_shift(x, i, ell), j, ell)][col] += 1
            rows[edge_index(x, j, ell)][col] -= 1
            rows[edge_index(_shift(x, j, ell), i, ell)][col] -= 1
            rows[edge_index(x, i, ell)][col] += 1
    return flint.fmpz_mat(rows)


def d3_matrix(ell):
    """Cube-to-face boundary: rows faces, columns cubes, entries in Z."""
    n_faces, n_cubes = 3 * ell**3, ell**3
    rows = [[0] * n_cubes for _ in range(n_faces)]
    for x in sites(ell):
        col = _site(x, ell)
        for sign, i, pair in (
            (+1, 1, (2, 3)),
            (-1, 2, (1, 3)),
            (+1, 3, (1, 2)),
        ):
            rows[face_index(_shift(x, i, ell), pair, ell)][col] += sign
            rows[face_index(x, pair, ell)][col] -= sign
    return flint.fmpz_mat(rows)


def wrapping_sheet(ell, pair):
    """The integer face chain s_(ij) = sum_{x: x_m = 0} [x; i, j].

    m is the direction complementary to the pair. The sheet is a cycle —
    every edge appears once with + and once with - as the sum wraps — but it
    is NOT harmonic: d3^T moves it (see `sheet_rayleigh_num_den`).
    """
    i, j = pair
    (m,) = set((1, 2, 3)) - {i, j}
    vec = [0] * (3 * ell**3)
    for x in sites(ell):
        if x[m - 1] == 0:
            vec[face_index(x, pair, ell)] = 1
    return vec


def cycle_matrix(ell):
    """Columns: all L^3 cube boundaries, then the three wrapping sheets."""
    d3 = d3_matrix(ell)
    n_faces, n_cubes = d3.nrows(), d3.ncols()
    cols = [[int(d3[r, c]) for r in range(n_faces)] for c in range(n_cubes)]
    cols += [wrapping_sheet(ell, pair) for pair in FACE_PAIRS]
    return flint.fmpz_mat([[col[r] for col in cols] for r in range(n_faces)])


def _mod_rank(mat, prime):
    rows = [[int(mat[r, c]) % prime for c in range(mat.ncols())] for r in range(mat.nrows())]
    return flint.nmod_mat(rows, prime).rank()


def kernel_dim_exact(ell):
    """dim ker d_2 over Q, by exact integer elimination."""
    d2 = d2_matrix(ell)
    return d2.ncols() - d2.rank()


def kernel_dim_bounds(ell, prime=DEFAULT_PRIME):
    """(lower, upper) bounds on dim ker d_2 over Q, from one prime.

    lower: the mod-p rank of the exhibited cycle family is a lower bound on
    its Q-rank, and every column is verified to be an exact integer cycle, so
    the kernel is at least that large.
    upper: rank mod p <= rank over Q, so nullity mod p >= nullity over Q.
    """
    d2 = d2_matrix(ell)
    cyc = cycle_matrix(ell)
    if not (d2 * cyc).is_zero():  # each exhibited column must be a cycle over Z
        raise AssertionError(f"L={ell}: an exhibited 'cycle' is not in ker d_2")
    lower = _mod_rank(cyc, prime)
    upper = d2.ncols() - _mod_rank(d2, prime)
    return lower, upper


def sheet_rayleigh_num_den(ell, pair=(1, 2)):
    """(<s, d3 d3^T s>, <s, s>) for a wrapping sheet, as exact integers."""
    d3 = d3_matrix(ell)
    s = wrapping_sheet(ell, pair)
    up = [
        sum(int(d3[r, c]) * s[r] for r in range(d3.nrows()))  # (d3^T s)_c
        for c in range(d3.ncols())
    ]
    return sum(v * v for v in up), sum(v * v for v in s)
