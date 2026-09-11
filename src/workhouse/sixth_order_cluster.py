"""The sixth-order effective Hamiltonian on a plaquette cluster, from the third engine.

Two independent evaluations of the same object, on the same cluster, with the
same primitives (``loopcalc``: loop words, Fierz ``H0``, Weingarten Haar):

* ``bloch_hermitian``: the general Bloch recursion with intermediate
  normalisation and the canonical Hermitian (des Cloizeaux) metric,

      K_n = P V chi_(n-1),   chi_n = D (V chi_(n-1) - sum_(j<n) chi_(n-j) K_j),
      M = P + chi^dagger chi,   H_eff = M^(1/2) (E0 + sum u^n K_n) M^(-1/2),

  which needs no ``P V P = 0`` and drops no odd order;
* ``folded_words``: the closed sixth-order word formula (F6) of
  ``G9_SIXTH_ORDER_COMBINED`` in ``A_m, B_m, C_2``, valid when ``P V P = 0``,
  evaluated by resolvent powers; together with ``H4 = A4 - {A2, B2}/2`` and
  ``H2 = A2``.

The two agree entry by entry through order six wherever both apply (the
tests, and every run record). Everything is exact: rationals at one rank, or
elements of Q(N) inside ``symbolic_rank.Symbolic``.

What a cluster's effective Hamiltonian is *not*: the band. The lattice
kernel is the sum of connected cluster cumulants. On a two-face cluster the
off-diagonal block P -> R is its own cumulant (no proper sub-cluster contains
both faces); the diagonal needs the single-face and vacuum subtractions,
which ``pair_cumulants`` performs. Larger supports are not evaluated here.
"""

from __future__ import annotations

from fractions import Fraction

from . import loopcalc as L


# ---------------------------------------------------------------- scalars and matrices
def _one():
    return L.F(1)


def _zero():
    return L.F(0)


def _binom(alpha: Fraction, k: int):
    """Generalised binomial coefficient alpha choose k, as the engine's scalar."""
    out = Fraction(1)
    for i in range(k):
        out *= (alpha - i) / (i + 1)
    return L.F(out)


def _mat_zero(m: int):
    return [[_zero() for _ in range(m)] for _ in range(m)]


def _mat_eye(m: int):
    return [[_one() if i == j else _zero() for j in range(m)] for i in range(m)]


def _mat_add(a, b, s=1):
    return [[x + s * y for x, y in zip(ra, rb, strict=True)] for ra, rb in zip(a, b, strict=True)]


def _mat_mul(a, b):
    m = len(a)
    return [
        [sum((a[i][k] * b[k][j] for k in range(m)), _zero()) for j in range(m)] for i in range(m)
    ]


def _mat_scale(a, s):
    return [[x * s for x in row] for row in a]


def _series_mul(a: list, b: list, order: int) -> list:
    m = len(a[0])
    return [
        _sum_mats([_mat_mul(a[j], b[n - j]) for j in range(n + 1)], m) for n in range(order + 1)
    ]


def _sum_mats(mats: list, m: int):
    out = _mat_zero(m)
    for x in mats:
        out = _mat_add(out, x)
    return out


def _series_power(metric: list, exponent: Fraction, order: int) -> list:
    """(I + X)^exponent as a matrix series, X = metric minus its order-zero identity."""
    m = len(metric[0])
    unit = [_mat_eye(m)] + [_mat_zero(m) for _ in range(order)]
    x = [_mat_zero(m)] + [metric[n] for n in range(1, order + 1)]
    total, power = unit, unit
    for k in range(1, order + 1):
        power = _series_mul(power, x, order)
        c = _binom(exponent, k)
        total = [_mat_add(t, p, c) for t, p in zip(total, power, strict=True)]
    return total


def _is_symmetric(a) -> bool:
    m = len(a)
    return all(a[i][j] == a[j][i] for i in range(m) for j in range(i + 1, m))


# ---------------------------------------------------------------- vectors
def vec_inner(bra: dict, ket: dict):
    """<bra|ket> for two formal vectors with real coefficients."""
    return sum((c * L.inner(w, ket) for w, c in bra.items()), _zero())


def vec_lin(vecs: list, coeffs: list) -> dict:
    out: dict = {}
    for v, c in zip(vecs, coeffs, strict=True):
        if c:
            out = L.vadd(out, v, c)
    return out


# ---------------------------------------------------------------- model spaces
class ModelSpace:
    """A cluster with an explicit model space: its face words (the plaquette
    sector) or the empty word (the vacuum sector)."""

    def __init__(self, faces, reduced: bool = False, vacuum: bool = False):
        self.cluster = L.Cluster(faces, reduced)
        self.vacuum = vacuum
        if vacuum:
            self.words = [()]
            self.e0 = _zero()
        else:
            self.words = list(self.cluster.words)
            self.e0 = self.cluster.e0
        self.m = len(self.words)

    def V(self, vec: dict) -> dict:
        return self.cluster.V(vec)

    def R(self, vec: dict, power: int = 1) -> dict:
        return L.resolvent(vec, self.e0, power)

    def gram(self):
        return [[L.inner(a, {b: _one()}) for b in self.words] for a in self.words]

    def project(self, vec: dict):
        """Coefficients <w_i|vec> for the orthonormal model words."""
        return [L.inner(w, vec) for w in self.words]


# ---------------------------------------------------------------- the Bloch recursion
def bloch_hermitian(space: ModelSpace, order: int, check: bool = True) -> dict:
    """H_eff through ``order`` on the model space, Hermitian form, as matrices.

    Returns ``{"K": [K_0..K_n], "M": [M_0..M_n], "H": [H_0..H_n], "chi": ...}``
    with ``H_0 = E0 I``. When ``check`` is set the model Gram matrix is verified
    to be the identity (the projection below relies on it) and every ``H_n``
    is verified symmetric.
    """
    m = space.m
    if check and space.gram() != _mat_eye(m):
        raise AssertionError("model words are not orthonormal on this cluster")
    model = [{w: _one()} for w in space.words]
    chi = [model]
    K = [_mat_scale(_mat_eye(m), space.e0)]
    for n in range(1, order + 1):
        vchi = [space.V(chi[n - 1][j]) for j in range(m)]
        Kn = [[_zero()] * m for _ in range(m)]
        for j in range(m):
            col = space.project(vchi[j])
            for i in range(m):
                Kn[i][j] = col[i]
        K.append(Kn)
        chi_n = []
        for j in range(m):
            rhs = vchi[j]
            for lag in range(1, n):
                rhs = L.vadd(rhs, vec_lin(chi[n - lag], [K[lag][i][j] for i in range(m)]), -1)
            chi_n.append(space.R(rhs))
        chi.append(chi_n)
    # metric M_n = sum_(a+b=n, a,b>=1) chi_a^dagger chi_b
    M = [_mat_eye(m)] + [_mat_zero(m) for _ in range(order)]
    for n in range(2, order + 1):
        for a in range(1, n):
            b = n - a
            for i in range(m):
                for j in range(m):
                    M[n][i][j] += vec_inner(chi[a][i], chi[b][j])
    sqrt = _series_power(M, Fraction(1, 2), order)
    invsqrt = _series_power(M, Fraction(-1, 2), order)
    H = _series_mul(_series_mul(sqrt, K, order), invsqrt, order)
    if check:
        for n, h in enumerate(H):
            if not _is_symmetric(h):
                raise AssertionError(f"H_{n} is not symmetric")
    return {"K": K, "M": M, "H": H, "chi": chi}


# ---------------------------------------------------------------- the word formula
def _ket(space: ModelSpace, j: int, steps: int, powers: dict | None = None) -> dict:
    """(D^p_k V) ... (D^p_1 V) w_j, with p_s = powers.get(s, 1)."""
    v = {space.words[j]: _one()}
    for s in range(1, steps + 1):
        v = space.R(space.V(v), (powers or {}).get(s, 1))
    return v


def word_matrices(space: ModelSpace, order: int) -> dict:
    """A_m = P V (D V)^(m-1) P for m <= order, B_m (one D -> D^2), C_2 = P V D^3 V P."""
    m = space.m
    A, B = {}, {}
    for k in range(1, order + 1):
        kets = [space.V(_ket(space, j, k - 1)) for j in range(m)]
        A[k] = [[L.inner(space.words[i], kets[j]) for j in range(m)] for i in range(m)]
        if k >= 2:
            Bk = _mat_zero(m)
            for p in range(1, k):
                kets = [space.V(_ket(space, j, k - 1, {p: 2})) for j in range(m)]
                Bk = _mat_add(
                    Bk, [[L.inner(space.words[i], kets[j]) for j in range(m)] for i in range(m)]
                )
            B[k] = Bk
    kets = [space.V(_ket(space, j, 1, {1: 3})) for j in range(m)]
    C2 = [[L.inner(space.words[i], kets[j]) for j in range(m)] for i in range(m)]
    return {"A": A, "B": B, "C2": C2}


def _anti(x, y):
    return _mat_add(_mat_mul(x, y), _mat_mul(y, x))


def folded_words(space: ModelSpace, order: int = 6) -> dict:
    """H_2, H_4, H_6 from the closed word formulas (P V P = 0 assumed and checked),
    with the seven pieces of (F6) returned separately."""
    w = word_matrices(space, order)
    A, B, C2 = w["A"], w["B"], w["C2"]
    m = space.m
    if A[1] != _mat_zero(m):
        raise AssertionError("P V P != 0 on this cluster; the word formula does not apply")
    out = {"H2": A[2], "pieces": {}}
    if order >= 3:
        out["H3"] = A[3]
    if order >= 4:
        out["H4"] = _mat_add(A[4], _anti(A[2], B[2]), Fraction(-1, 2))
    if order >= 6:
        a2a2 = _mat_mul(A[2], A[2])
        b2b2 = _mat_mul(B[2], B[2])
        pieces = {
            "A6": A[6],
            "-{A4,B2}/2": _mat_scale(_anti(A[4], B[2]), Fraction(-1, 2)),
            "-{A3,B3}/2": _mat_scale(_anti(A[3], B[3]), Fraction(-1, 2)),
            "-{A2,B4}/2": _mat_scale(_anti(A[2], B[4]), Fraction(-1, 2)),
            "+{A2^2,C2}/2": _mat_scale(_anti(a2a2, C2), Fraction(1, 2)),
            "+3{A2,B2^2}/8": _mat_scale(_anti(A[2], b2b2), Fraction(3, 8)),
            "+B2A2B2/4": _mat_scale(_mat_mul(_mat_mul(B[2], A[2]), B[2]), Fraction(1, 4)),
        }
        out["pieces"] = pieces
        out["H6"] = _sum_mats(list(pieces.values()), m)
    out["matrices"] = w
    return out


# ---------------------------------------------------------------- blocks
def block(h, rows, cols):
    return {(a, b): h[a][b] for a in rows for b in cols}


def odd_even(h, face_a: int, face_b: int):
    """(C-odd, C-even) element between faces a and b of a cluster matrix."""
    w = {
        (0, 2): h[2 * face_a][2 * face_b],
        (0, 3): h[2 * face_a][2 * face_b + 1],
        (1, 2): h[2 * face_a + 1][2 * face_b],
        (1, 3): h[2 * face_a + 1][2 * face_b + 1],
    }
    return L.block_odd(w), L.block_even(w)


def pair_cumulants(faces2, order: int = 6, reduced: bool = True, method: str = "bloch") -> dict:
    """The sixth-order pair: hop cumulants (C-odd, C-even) and the on-site cumulant
    after single-face and vacuum subtraction, per order."""
    pair = ModelSpace(faces2, reduced)
    single = ModelSpace(faces2[:1], reduced)
    vac_pair = ModelSpace(faces2, reduced, vacuum=True)
    vac_single = ModelSpace(faces2[:1], reduced, vacuum=True)

    def run(space):
        if method == "bloch":
            return bloch_hermitian(space, order)["H"]
        f = folded_words(space, order)
        return {2: f["H2"], 4: f["H4"], 6: f.get("H6")}

    hp, hs, vp, vs = run(pair), run(single), run(vac_pair), run(vac_single)
    out = {}
    for n in (2, 4, 6):
        if n > order:
            break
        hop_odd, hop_even = odd_even(hp[n], 0, 1)
        site_odd_pair, site_even_pair = odd_even(hp[n], 0, 0)
        site_odd_single, site_even_single = odd_even(hs[n], 0, 0)
        vac = vp[n][0][0] - vs[n][0][0]
        out[n] = {
            "hop_odd": hop_odd,
            "hop_even": hop_even,
            "site_odd": site_odd_pair - site_odd_single - vac,
            "site_even": site_even_pair - site_even_single - vac,
            "vacuum_pair_minus_single": vac,
            "vacuum_single": vs[n][0][0],
            "single_odd": odd_even(hs[n], 0, 0)[0],
        }
    return out


PAIRS = {
    "perpendicular": [((0, 1), (0, 0, 0)), ((0, 2), (0, 0, 0))],
    "coplanar": [((0, 1), (0, 0, 0)), ((0, 1), (1, 0, 0))],
}
