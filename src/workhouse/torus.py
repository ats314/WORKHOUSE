"""The periodic cubical complex, built rather than asserted.

The repository has carried ``dim Z_2 = (L^3 - 1) + 3 = L^3 + 2`` as a checked
claim since the beginning, but both of its checks were arithmetic *on the
formula*: one simplifies ``(L**3 - 1) + 3 - (L**3 + 2)`` to zero, the other
evaluates the same formula at L = 3, 4, 5. Neither ever built a boundary map.
A formula that is re-arranged correctly is not a homology computation, and the
distinction matters here because the count is one of the four load-bearing
statements of the flat-band manuscript (Theorem 2).

This module builds the complex on ``(Z/LZ)^3`` from the two boundary formulas
the manuscript prints, over the integers, and settles the ranks exactly.

The rank argument is worth stating, because "computed the rank" hides a choice.
Gaussian elimination over Q on a 375x375 matrix of Fractions is slow and its
entries grow; elimination over ``F_p`` is fast but only gives
``rank_{F_p} <= rank_Q``, i.e. a LOWER bound on the kernel. So the two bounds
are taken from different directions and made to meet:

* ``rank_{F_p}(d2)`` bounds ``dim ker d2`` from **below** (for two primes);
* the explicitly exhibited cycles — every elementary cube boundary, plus the
  three wrapping sheets — bound it from **above**, because their span is
  contained in the kernel and its rank is computed the same way.

When ``rank[d3 | sheets] == 3L^3 - rank(d2)`` the two meet and the kernel
dimension is pinned, with a basis in hand rather than a dimension count. That
is also, exactly, the manuscript's own proof: ``ker d2 = im d3 (+) H_2``.

Nothing here uses sympy: integer and modular arithmetic is enough, and it
keeps the whole construction cheap enough to run inside a check.
"""

from __future__ import annotations

from functools import lru_cache
from itertools import product

#: Two primes, so a rank that is accidentally deficient modulo one of them is
#: caught rather than believed. Both are far larger than any entry that can
#: arise from a {0, +1, -1} incidence matrix at these sizes.
PRIMES = (2147483647, 2305843009213693951)

#: The three oriented face types, as (i, j) with i < j.
PAIRS = ((0, 1), (0, 2), (1, 2))


def faces(size: int) -> list[tuple[tuple[int, int, int], int, int]]:
    """The 3L^3 oriented faces ``(x, i, j)``."""
    return [(x, i, j) for x in product(range(size), repeat=3) for (i, j) in PAIRS]


def links(size: int) -> list[tuple[tuple[int, int, int], int]]:
    """The 3L^3 oriented links ``(x, i)``."""
    return [(x, i) for x in product(range(size), repeat=3) for i in range(3)]


def _shift(x: tuple[int, int, int], i: int, size: int) -> tuple[int, int, int]:
    y = list(x)
    y[i] = (y[i] + 1) % size
    return tuple(y)


@lru_cache(maxsize=8)
def boundaries(size: int) -> tuple[list[list[int]], list[list[int]]]:
    """``(d2, d3)`` as dense integer matrices, from the printed formulas.

    ``d2[x;i,j] = [x+e_i;j] - [x;j] - [x+e_j;i] + [x;i]``  (manuscript eq. 41)

    ``d3[x;1,2,3] = [x+e_1;2,3] - [x;2,3] - [x+e_2;1,3] + [x;1,3]
                    + [x+e_3;1,2] - [x;1,2]``              (manuscript eq. 42)

    ``d2`` is links-by-faces and ``d3`` is faces-by-cubes, so the composite
    ``d2 @ d3`` is links-by-cubes and must vanish identically.
    """
    fs, ls = faces(size), links(size)
    fi = {f: n for n, f in enumerate(fs)}
    li = {e: n for n, e in enumerate(ls)}
    cubes = list(product(range(size), repeat=3))

    d2 = [[0] * len(fs) for _ in ls]
    for col, (x, i, j) in enumerate(fs):
        d2[li[(_shift(x, i, size), j)]][col] += 1
        d2[li[(x, j)]][col] -= 1
        d2[li[(_shift(x, j, size), i)]][col] -= 1
        d2[li[(x, i)]][col] += 1

    d3 = [[0] * len(cubes) for _ in fs]
    for col, x in enumerate(cubes):
        d3[fi[(_shift(x, 0, size), 1, 2)]][col] += 1
        d3[fi[(x, 1, 2)]][col] -= 1
        d3[fi[(_shift(x, 1, size), 0, 2)]][col] -= 1
        d3[fi[(x, 0, 2)]][col] += 1
        d3[fi[(_shift(x, 2, size), 0, 1)]][col] += 1
        d3[fi[(x, 0, 1)]][col] -= 1
    return d2, d3


def sheets(size: int) -> list[list[int]]:
    """The three wrapping 2-cycles: all ``(i, j)`` faces in one slice.

    These are the harmonic generators of ``H_2(T^3)``. Each is a cycle because
    the slice is a closed torus: every link in it is shared by exactly two
    faces of the slice with opposite induced sign, so the boundary telescopes.
    That is checked, not assumed — see :func:`sheets_are_cycles`.
    """
    fi = {f: n for n, f in enumerate(faces(size))}
    out = []
    for i, j in PAIRS:
        k = ({0, 1, 2} - {i, j}).pop()
        v = [0] * (3 * size**3)
        for x in product(range(size), repeat=3):
            if x[k] == 0:
                v[fi[(x, i, j)]] = 1
        out.append(v)
    return out


def matmul(a: list[list[int]], b: list[list[int]]) -> list[list[int]]:
    """Exact integer product, skipping the zeros an incidence matrix is made of."""
    out = [[0] * len(b[0]) for _ in a]
    for i, row in enumerate(a):
        acc = out[i]
        for t, coeff in enumerate(row):
            if coeff:
                for j, entry in enumerate(b[t]):
                    if entry:
                        acc[j] += coeff * entry
    return out


def rank_mod(matrix: list[list[int]], prime: int) -> int:
    """Rank over ``F_p``. Never exceeds the rank over Q — see the module docstring."""
    a = [[v % prime for v in row] for row in matrix]
    rows = len(a)
    cols = len(a[0]) if rows else 0
    rank = 0
    for col in range(cols):
        pivot = next((i for i in range(rank, rows) if a[i][col]), None)
        if pivot is None:
            continue
        a[rank], a[pivot] = a[pivot], a[rank]
        inv = pow(a[rank][col], prime - 2, prime)
        a[rank] = [(v * inv) % prime for v in a[rank]]
        for i in range(rows):
            if i != rank and a[i][col]:
                factor, row_i, row_r = a[i][col], a[i], a[rank]
                a[i] = [(row_i[j] - factor * row_r[j]) % prime for j in range(cols)]
        rank += 1
        if rank == rows:
            break
    return rank


def chain_condition(size: int) -> bool:
    """``d2 d3 = 0`` over the integers."""
    d2, d3 = boundaries(size)
    return not any(v for row in matmul(d2, d3) for v in row)


def sheets_are_cycles(size: int) -> bool:
    """Each wrapping sheet lies in ``ker d2``, over the integers."""
    d2, _ = boundaries(size)
    for sheet in sheets(size):
        support = [c for c, v in enumerate(sheet) if v]
        if any(sum(d2[r][c] * sheet[c] for c in support) for r in range(len(d2))):
            return False
    return True


def ranks(size: int) -> dict[str, int]:
    """Ranks and the kernel dimension, agreed by both primes.

    Returns ``rank_d2``, ``rank_d3``, ``dim_ker_d2`` and ``span_generators``
    — the last being the rank of ``[d3 | sheets]``, the explicit kernel basis.
    A disagreement between the two primes raises rather than picking one.
    """
    d2, d3 = boundaries(size)
    generators = [d3[f][:] + [s[f] for s in sheets(size)] for f in range(3 * size**3)]
    out = {}
    for label, matrix in (("rank_d2", d2), ("rank_d3", d3), ("span_generators", generators)):
        values = {rank_mod(matrix, p) for p in PRIMES}
        if len(values) != 1:
            raise ArithmeticError(f"{label} at L={size} disagrees between primes: {values}")
        out[label] = values.pop()
    out["dim_ker_d2"] = 3 * size**3 - out["rank_d2"]
    return out


def sheet_up_laplacian_ratio(size: int) -> tuple[int, int]:
    """``(<s, L_up s>, <s, s>)`` for a wrapping sheet — the harmonicity test.

    The manuscript's §6 says a term proportional to the up-Hodge Laplacian
    ``L_up = d3 d3*`` "disperses the cube-boundary component while leaving the
    three harmonic sheets pinned". The sheets Theorem 2 exhibits are cycles,
    but they are not in ``ker d3*``, so ``L_up`` moves them — and by exactly
    the same Rayleigh quotient at every size. Returning the two integers
    rather than their ratio keeps the check exact.
    """
    d2, d3 = boundaries(size)
    sheet = sheets(size)[0]
    # d3^T s, then d3 (d3^T s)
    adjoint = [
        sum(d3[f][c] * sheet[f] for f in range(len(sheet)) if sheet[f]) for c in range(size**3)
    ]
    up = [
        sum(d3[f][c] * adjoint[c] for c in range(size**3) if adjoint[c]) for f in range(len(sheet))
    ]
    return sum(sheet[f] * up[f] for f in range(len(sheet))), sum(v * v for v in sheet)


def bloch_nullities(size: int) -> dict[int, int]:
    """Nullity of ``d2(k)`` at each allowed momentum, as a multiset.

    The other route to the carrier. ``B(k) = d2(k)*`` is the manuscript's
    3x3 eq. (8); summing ``3 - rank B(k)`` over the ``L^3`` allowed momenta
    must give the same ``L^3 + 2`` the chain complex gives — and it does, but
    from different objects: the 3 is ``B(0) = 0``'s triple degeneracy, not
    ``b_2(T^3)``, and the ``L^3 - 1`` is the count of non-Gamma momenta, not a
    count of cubes. The manuscript states both decompositions and never
    remarks that they agree, which is the only machine link between its
    Theorem 1 and its Theorem 2.

    Exact: entries are cyclotomic, ranks are taken over the field they
    generate, never numerically.
    """
    from sympy import I, Matrix, exp, pi, simplify

    out: dict[int, int] = {}
    for n1 in range(size):
        for n2 in range(size):
            for n3 in range(size):
                d = [simplify(exp(2 * I * pi * n / size) - 1) for n in (n1, n2, n3)]
                b = Matrix([[d[1], -d[0], 0], [d[2], 0, -d[0]], [0, d[2], -d[1]]])
                nullity = 3 - b.H.rank()
                out[nullity] = out.get(nullity, 0) + 1
    return out
