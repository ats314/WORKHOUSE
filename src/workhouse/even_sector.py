"""The charge-even band, built from the chain complex rather than scanned.

The C-odd sector is the one this program has verified to death: the signed
incidence factorization ``S(k) + 4I = B(k)B(k)^dagger`` with ``det B = 0``
gives the exactly flat carrier, and the spectrum ``{-4, q-4, q-4}`` is a
closed form that every downstream check leans on.

The C-even sector has no such object. What the corpus records for it is a
range and an expansion: ``lambda in [-4, 12]``, argued from positivity below
and from the 12-regularity of the plaquette graph above, and reported by a
41**3 dense numerical scan in ``ENGINE_FLUX_glueball_band_certificate_v2.py``;
plus ``lambda = 12 - (4/3)|k|**2`` near Gamma. On this repository's side the
only C-even geometry checked before now was two hand-written matrices at Gamma
and R -- so everything the band ledger does with the sector, the ``12 leak``
term, the bandwidth ``16|t_+|`` and the band edges at ``lambda = 12`` and
``lambda = -4``, rested on those two points and the manuscript's word.

This module supplies the missing closed form. Writing ``a_m = 2 + 2 cos k_m``
and ``p = a_1 + a_2 + a_3``, the unsigned Gram matrix ``N(k)N(k)^dagger`` has
characteristic polynomial

    mu**3 - 2 p mu**2 + p**2 mu - 4 a_1 a_2 a_3 ,     lambda = mu - 4,

exactly, at every k. Three consequences follow with no scan at all: the range
``[-4, 12]`` with each endpoint attained at exactly ONE momentum, Gamma and R,
which a scan cannot report;
the exact set on which the band touches its floor (the three zone-boundary
planes ``k_m = pi``, with multiplicity three only at the corner); and the
Gamma expansion ``lambda_{A1}(k) = 12 - (4/3)|k|**2 + O(k**4)`` that produces
the corpus's C-even curvature coefficients.

Two independent constructions are kept deliberately distinct, for the same
reason ``torus.py`` keeps its two rank routes apart. The Laurent-polynomial
route works in ``z_m = exp(i k_m)`` with ``conj(z) = 1/z``, so the cubic is a
rational-function identity checked by ``cancel`` rather than a trigonometric
one checked by ``simplify`` -- exact, and about a thousand times faster. The
finite-lattice route builds the plaquette adjacency on an ``L**3`` torus
straight from ``torus.py``'s boundary formula and compares integer
characteristic polynomials. Neither imports the other's answer, and the corpus
enters neither.
"""

from __future__ import annotations

from functools import lru_cache

import flint
from sympy import (
    Integer,
    Matrix,
    Poly,
    Rational,
    Symbol,
    cancel,
    cos,
    diff,
    expand,
    pi,
    symbols,
    zeros,
)

from . import torus as TOR

#: Face directions in the pair order ``torus.py`` uses: (1,2), (1,3), (2,3).
FACE_PAIRS = TOR.FACE_PAIRS

#: Bloch phases as free symbols. Hermitian conjugation is ``z -> 1/z`` and a
#: transpose, never `sympy.conjugate`: that keeps every intermediate a rational
#: function, so the identities below are decided by `cancel` on a polynomial
#: numerator instead of by trigonometric `simplify`.
Z = tuple(Symbol(f"z{m}", nonzero=True) for m in (1, 2, 3))

MU = Symbol("mu")
LAM = Symbol("lam")


def _phase(direction: int, inverse: bool):
    """``z_d`` or ``1/z_d``; ``direction = 0`` means the base site, phase 1."""
    if direction == 0:
        return Integer(1)
    z = Z[direction - 1]
    return 1 / z if inverse else z


def bloch_incidence(signed: bool, inverse: bool = False) -> Matrix:
    """The 3x3 Bloch incidence: rows face orbitals, columns link directions.

    Read straight off the boundary formula ``torus.py`` documents,

        d2 [x; i,j] = +[x+e_i; j] - [x; j] - [x+e_j; i] + [x; i],

    with the four links of the base face carrying their site offset as a
    phase. ``signed`` keeps the boundary signs (the C-odd sector); dropping
    them is the unsigned incidence (the C-even sector). Nothing else differs
    between the two sectors at this level, which is the whole point: the two
    bandwidths are two spectra of the same geometric object.
    """
    m = zeros(3, 3)
    for orbital, (i, j) in enumerate(FACE_PAIRS):
        for site, direction, sign in ((i, j, +1), (0, j, -1), (j, i, -1), (0, i, +1)):
            m[orbital, direction - 1] += (sign if signed else 1) * _phase(site, inverse)
    return expand(m)


@lru_cache(maxsize=4)
def gram(signed: bool) -> Matrix:
    """``N N^dagger`` (unsigned) or ``B B^dagger`` (signed), as Laurent polys.

    The adjacency is this minus ``4I``. Its diagonal is *not* 4: that is the
    FINITE face-face Gram ``|d2|^T|d2|``, whose diagonal counts a face's own
    four links. The Bloch diagonal at orbital ``(i,j)`` is ``a_i + a_j``
    (unsigned) and ``8 - a_i - a_j`` (signed), because the four in-plane
    same-orbital neighbours carry phases. The two objects are Fourier
    transforms of each other and confusing them is easy, so both are checked.
    """
    return expand(bloch_incidence(signed) * bloch_incidence(signed, inverse=True).T)


@lru_cache(maxsize=4)
def gram_charpoly(signed: bool):
    """Characteristic polynomial of the Gram matrix, in ``MU``."""
    return cancel(expand(gram(signed).charpoly(MU).as_expr()))


def a_symbols():
    """``a_m = 2 + 2 cos k_m = |1 + z_m|**2``, in Laurent form."""
    return tuple(z + 1 / z + 2 for z in Z)


def p_symbol():
    """``p = sum_m a_m``: the C-even sector's zone function."""
    return expand(sum(a_symbols()))


def q_symbol():
    """``q = 4 sum_m sin**2(k_m/2)``: the C-odd sector's zone function."""
    return expand(6 - sum(z + 1 / z for z in Z))


def even_cubic(mu, a, b, c):
    """``mu**3 - 2 p mu**2 + p**2 mu - 4abc`` with ``p = a + b + c``.

    The closed form. Its three roots are ``lambda + 4`` for the three C-even
    branches at that momentum.
    """
    p = a + b + c
    return mu**3 - 2 * p * mu**2 + p**2 * mu - 4 * a * b * c


def odd_cubic(mu, q):
    """``mu (mu - q)**2``: the C-odd sector's characteristic polynomial."""
    return mu * (mu - q) ** 2


def abc_at(k) -> tuple:
    """``(a_1, a_2, a_3)`` at a momentum triple, exactly."""
    return tuple(2 + 2 * cos(km) for km in k)


def lambdas_from_abc(a, b, c) -> list:
    """The three C-even adjacency eigenvalues, from the cubic's roots."""
    return sorted(Poly(even_cubic(LAM + 4, a, b, c), LAM).all_roots())


def even_lambdas(k) -> list:
    """The three C-even adjacency eigenvalues at one momentum, exactly."""
    return lambdas_from_abc(*abc_at(k))


def odd_lambdas(k) -> list:
    """The three C-odd adjacency eigenvalues at one momentum, exactly."""
    q = 4 * sum((1 - cos(km)) / 2 for km in k)
    return sorted([Integer(-4), q - 4, q - 4])


#: The four high-symmetry momenta of the simple cubic zone.
HIGH_SYMMETRY = {
    "Gamma": (Integer(0), Integer(0), Integer(0)),
    "X": (pi, Integer(0), Integer(0)),
    "M": (pi, pi, Integer(0)),
    "R": (pi, pi, pi),
}


# --------------------------------------------------------------------------
# The finite lattice, independently
# --------------------------------------------------------------------------
# `torus.py` builds d2 with signs, which gives the C-ODD adjacency as
# d2^T d2 - 4I. The C-even sector needs the entrywise absolute value of the
# same matrix, so it is built here from the same boundary formula rather than
# by taking |.| of a flint matrix -- one construction, one indexing, and the
# unsigned/signed switch in exactly one place.


def unsigned_incidence(ell: int) -> flint.fmpz_mat:
    """``|d2|``: rows edges, columns faces, a 1 wherever the link is on the face."""
    n = 3 * ell**3
    rows = [[0] * n for _ in range(n)]
    for x in TOR.sites(ell):
        for pair in FACE_PAIRS:
            i, j = pair
            col = TOR.face_index(x, pair, ell)
            for site, direction in (
                (TOR._shift(x, i, ell), j),
                (x, j),
                (TOR._shift(x, j, ell), i),
                (x, i),
            ):
                rows[TOR.edge_index(site, direction, ell)][col] += 1
    return flint.fmpz_mat(rows)


@lru_cache(maxsize=4)
def shared_link_gram(ell: int) -> flint.fmpz_mat:
    """``|d2|^T |d2|``: how many links each pair of faces shares."""
    inc = unsigned_incidence(ell)
    return inc.transpose() * inc


@lru_cache(maxsize=4)
def plaquette_degrees(ell: int) -> tuple[set, set, set]:
    """``(diagonal values, off-diagonal values, degrees)`` of the shared-link Gram.

    The band assembly's ``12 leak`` term needs the plaquette graph to be
    12-regular and the shared-link count to be 0 or 1 -- otherwise "twelve
    neighbours, one leakage each" is a miscount, not a convention. Both are
    computed here rather than assumed.
    """
    gram_mat = shared_link_gram(ell)
    n = 3 * ell**3
    diag = {int(gram_mat[i, i]) for i in range(n)}
    off = {int(gram_mat[i, j]) for i in range(n) for j in range(n) if i != j}
    degrees = {sum(int(gram_mat[i, j]) for j in range(n) if j != i) for i in range(n)}
    return diag, off, degrees


@lru_cache(maxsize=4)
def finite_charpoly(ell: int) -> Poly:
    """Characteristic polynomial of the finite unsigned plaquette adjacency."""
    n = 3 * ell**3
    identity = flint.fmpz_mat(n, n, [4 if i == j else 0 for i in range(n) for j in range(n)])
    poly = (shared_link_gram(ell) - identity).charpoly()
    return Poly([int(poly[i]) for i in range(n, -1, -1)], LAM)


#: Extents whose Bloch momenta have rational cosines, so the Bloch product can
#: be formed in Q with no algebraic-number arithmetic: cos(2 pi m / L) is
#: rational only for L in {1, 2, 3, 4, 6}.
RATIONAL_EXTENTS = (3, 4, 6)


@lru_cache(maxsize=4)
def bloch_charpoly(ell: int) -> Poly:
    """The product of the C-even cubic over every allowed momentum."""
    if ell not in RATIONAL_EXTENTS:
        raise ValueError(f"L = {ell} has irrational Bloch cosines; use {RATIONAL_EXTENTS}")
    #: 2 + 2 cos(2 pi m / L), exactly, without going through a float cosine.
    two_cosines = {3: (2, -1, -1), 4: (2, 0, -2, 0), 6: (2, 1, -1, -2, -1, 1)}[ell]
    values = [2 + Rational(c) for c in two_cosines]
    product = Integer(1)
    for a in values:
        for b in values:
            for c in values:
                product *= even_cubic(LAM + 4, a, b, c)
    return Poly(expand(product), LAM)


def gamma_curvature_coefficients():
    """The three ``d lambda_{A1} / d(k_m**2)`` at Gamma, from the cubic.

    Derived, not asserted, and not assumed isotropic: substitute
    ``a_m = 4 - t_m`` with three independent ``t_m = k_m**2`` and
    ``mu = 16 + delta`` into the cubic, then read the implicit derivative
    ``d delta / d t_m = -(dF/dt_m)/(dF/ddelta)`` at the origin. All three come
    back ``-4/3``, so the A1++ branch disperses isotropically,

        lambda_{A1}(k) = 12 - (4/3)|k|**2 + O(k**4),

    and the corpus's C-even curvature coefficients are ``(4/3)|t_{r,+}|``.
    """
    delta = Symbol("delta")
    t = symbols("t1 t2 t3")
    f = expand(even_cubic(16 + delta, *(4 - tm for tm in t)))
    origin = {delta: 0, **dict.fromkeys(t, 0)}
    ddelta = diff(f, delta).subs(origin)
    return tuple(cancel(-diff(f, tm).subs(origin) / ddelta) for tm in t)


def matrix_norm_bound() -> tuple:
    """``(max row modulus sum, max column modulus sum)`` of the unsigned incidence.

    Each row of ``N`` has two nonzero entries of modulus ``|1 + z| <= 2`` and
    each column likewise, so ``||N||**2 <= 4 * 4 = 16`` and ``mu <= 16``.
    Returned as counts so a check can state the bound rather than assert it.
    """
    inc = bloch_incidence(False)
    rows = max(sum(1 for c in range(3) if inc[r, c] != 0) for r in range(3))
    cols = max(sum(1 for r in range(3) if inc[r, c] != 0) for c in range(3))
    return rows, cols
