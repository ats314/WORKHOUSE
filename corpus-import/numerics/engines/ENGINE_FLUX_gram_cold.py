"""
Independent regeneration of the odd Gram determinants (closes gap F1).

Reimplements the traceless-Hermitian Gaussian trace-moment calculus from
scratch -- no import of the project's colab engine -- and rebuilds the
degree<=5 and degree<=7 odd Gram matrices and their determinants.

Method.  For X traceless Hermitian Gaussian, write X = Y - (Tr Y/N) I with Y
full Hermitian Gaussian, covariance E[Y_ab Y_cd] = (1/2) delta_ad delta_bc.
Then
    Tr X^k = sum_{r=0}^{k} C(k,r) (-Tr Y / N)^{k-r} Tr Y^r ,   Tr Y^0 = N,
and full-GUE mixed trace moments obey the standard Wick recursion
    E[Tr Y^k * R] = (1/2) [ sum_{l=0}^{k-2} E[Tr Y^l Tr Y^{k-2-l} * R]
                          + sum_j d_j E[Tr Y^{k+d_j-2} * R_without_j] ].

Working at fixed integer N with exact Fractions avoids polynomial swell, and
agreement at enough ranks proves the closed form outright:  both sides are
rational functions of bounded degree, so a difference vanishing at more points
than the degree bound is identically zero.
"""

from fractions import Fraction as F
from functools import lru_cache
from math import comb


class Wick:
    """Traceless-Hermitian Gaussian trace moments at a fixed integer rank."""

    def __init__(self, N):
        self.N = N

    @lru_cache(maxsize=None)
    def _gue(self, degs):
        """E[ prod_i Tr Y^{d_i} ] for full Hermitian Gaussian Y."""
        degs = tuple(sorted((d for d in degs if d != 0), reverse=True))
        if not degs:
            return F(1)
        if sum(degs) % 2:
            return F(0)
        k, rest = degs[0], list(degs[1:])
        tot = F(0)
        for l in range(k - 1):
            tot += self._wrap(tuple(rest + [l, k - 2 - l]))
        for j, d in enumerate(rest):
            tot += d * self._wrap(tuple(rest[:j] + rest[j + 1:] + [k + d - 2]))
        return tot / 2

    @lru_cache(maxsize=None)
    def _wrap(self, degs):
        """Same, but Tr Y^0 = N contributes a factor of N per zero entry."""
        z = sum(1 for d in degs if d == 0)
        return F(self.N) ** z * self._gue(tuple(d for d in degs if d != 0))

    @lru_cache(maxsize=None)
    def _traceless_terms(self, k):
        """Tr X^k expanded over products of Tr Y^j, as (coeff, degs) pairs."""
        out = []
        for r in range(k + 1):
            c = F(comb(k, r) * (-1) ** (k - r), self.N ** (k - r))
            degs = [1] * (k - r)
            if r == 0:
                c *= self.N          # Tr Y^0 = N
            else:
                degs.append(r)
            out.append((c, tuple(degs)))
        return out

    @lru_cache(maxsize=None)
    def moment(self, degs):
        """E[ prod_i Tr X^{d_i} ] for traceless Hermitian Gaussian X."""
        terms = {(): F(1)}
        for k in sorted(degs):
            nxt = {}
            for d0, c0 in terms.items():
                for c1, d1 in self._traceless_terms(k):
                    key = tuple(sorted(d0 + d1, reverse=True))
                    nxt[key] = nxt.get(key, F(0)) + c0 * c1
            terms = {d: c for d, c in nxt.items() if c != 0}
        return sum((c * self._wrap(d) for d, c in terms.items()), F(0))


def odd_monomials(max_degree):
    """Partitions into parts >= 2 with odd total <= max_degree."""
    out = set()

    def rec(start, cur):
        tot = sum(cur)
        if tot and tot % 2:
            out.add(tuple(sorted(cur)))
        for k in range(start, max_degree + 1):
            if tot + k <= max_degree:
                cur.append(k)
                rec(k, cur)
                cur.pop()

    rec(2, [])
    return sorted(out, key=lambda m: (sum(m), len(m), m))


def det_exact(M):
    M = [row[:] for row in M]
    n = len(M)
    det = F(1)
    for i in range(n):
        p = next((r for r in range(i, n) if M[r][i] != 0), None)
        if p is None:
            return F(0)
        if p != i:
            M[i], M[p] = M[p], M[i]
            det = -det
        det *= M[i][i]
        inv = F(1) / M[i][i]
        for r in range(i + 1, n):
            f = M[r][i] * inv
            if f:
                for c in range(i, n):
                    M[r][c] -= f * M[i][c]
    return det


def gram_det(N, max_degree):
    W = Wick(N)
    b = odd_monomials(max_degree)
    G = [[W.moment(tuple(sorted(b[i] + b[j]))) for j in range(len(b))]
         for i in range(len(b))]
    return det_exact(G), len(b)


# closed forms under test
def closed5(N):
    return (F(45, 4096) * (N*N - 1)**3 * (N*N - 4)**3 * (N*N - 9) * (N*N - 16)
            / F(N**3))


def closed7(N):
    return (F(14175, 2**34) * (N*N - 1)**8 * (N*N - 4)**7 * (N*N - 9)**4
            * (N*N - 16)**3 * (N*N - 25) * (N*N - 36) / F(N**7))


def verify(max_rank=64, verbose=True):
    """Regenerate both determinants and compare to the closed forms."""
    # degree bounds: deg5 -> num 16 / den 3 ; deg7 -> num 48 / den 7
    need5, need7 = 16 + 3 + 2, 48 + 7 + 2
    ok5 = ok7 = True
    n5 = n7 = 0
    for N in range(2, max_rank + 1):
        d5, sz5 = gram_det(N, 5)
        if d5 != closed5(N):
            ok5 = False
            if verbose:
                print(f"    deg5 MISMATCH at N={N}")
            break
        n5 += 1
        if n5 >= need5 and n7 >= need7:
            break
        d7, sz7 = gram_det(N, 7)
        if d7 != closed7(N):
            ok7 = False
            if verbose:
                print(f"    deg7 MISMATCH at N={N}")
            break
        n7 += 1
    if verbose:
        print(f"    basis sizes: deg<=5 -> {sz5}, deg<=7 -> {sz7}")
        print(f"    deg<=5 matched at {n5} ranks (need {need5} to prove)")
        print(f"    deg<=7 matched at {n7} ranks (need {need7} to prove)")
    return ok5 and ok7, n5, n7, need5, need7


if __name__ == "__main__":
    import time
    t0 = time.time()
    print("Regenerating odd Gram determinants from an independent Wick engine")
    ok, n5, n7, need5, need7 = verify()
    print(f"  proved deg<=5: {ok and n5 >= need5}")
    print(f"  proved deg<=7: {ok and n7 >= need7}")
    print(f"  elapsed {time.time()-t0:.1f}s")
