#!/usr/bin/env python3
"""
Exact SU(N) C-odd local class-sector coefficient engine.

Computes the C-odd one-plaquette local class-sector expansion

    Delta_-^(N)(beta)
      = sqrt(9 beta/(2N)) + c0_-(N) + c1_-(N) beta^(-1/2) + O_N(beta^-1)

using exact rational finite Wick contractions for the traceless Hermitian
Weyl-Gaussian model with covariance

    E[X_ab X_cd] = 1/2 (delta_ad delta_bc - (1/N) delta_ab delta_cd).

The code avoids explicit pairings. It computes full-GUE trace moments by the
cut-join Gaussian integration-by-parts recursion, then obtains traceless moments
from X = Y - Tr(Y) I/N.

No numerical Monte Carlo is used.
"""
from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from functools import lru_cache
from itertools import product
from math import comb, sqrt
from typing import Dict, Iterable, List, Sequence, Tuple

Degs = Tuple[int, ...]
Monomial = Tuple[int, ...]


def fmt_frac(q: Fraction) -> str:
    return str(q.numerator) if q.denominator == 1 else f"{q.numerator}/{q.denominator}"


def monomial_degree(m: Monomial) -> int:
    return sum(m)


def sorted_degs(ds: Iterable[int]) -> Degs:
    return tuple(sorted((int(d) for d in ds if int(d) != 0), reverse=True))


@dataclass
class TracelessWick:
    N: int

    def __post_init__(self) -> None:
        if self.N < 2:
            raise ValueError("N must be >= 2")
        self._full = self._make_full_moment()
        self._tm_cache: Dict[Degs, Fraction] = {}

    def _make_full_moment(self):
        N = self.N

        @lru_cache(None)
        def wrap(degs: Degs) -> Fraction:
            z = sum(1 for d in degs if d == 0)
            non = sorted_degs(d for d in degs if d != 0)
            return Fraction(N) ** z * moment(non)

        @lru_cache(None)
        def moment(degs: Degs) -> Fraction:
            degs = sorted_degs(degs)
            if not degs:
                return Fraction(1)
            if sum(degs) % 2:
                return Fraction(0)

            # Cut-join recursion for full Hermitian Gaussian covariance
            # E[Y_ab Y_cd] = 1/2 delta_ad delta_bc.
            k = degs[0]
            rest = list(degs[1:])
            total = Fraction(0)

            # Cut one trace Tr(Y^k) into two traces.
            for ell in range(k - 1):
                total += wrap(tuple(rest + [ell, k - 2 - ell]))

            # Join Tr(Y^k) to another trace Tr(Y^d).
            for j, d in enumerate(rest):
                total += d * wrap(tuple(rest[:j] + rest[j + 1 :] + [k + d - 2]))

            return total / 2

        return wrap

    def _expanded_trace_terms(self, k: int) -> List[Tuple[Fraction, Degs]]:
        """Expansion of Tr((Y - Tr(Y)I/N)^k) into full-GUE traces."""
        N = self.N
        out: List[Tuple[Fraction, Degs]] = []
        for r in range(k + 1):
            coeff = Fraction(comb(k, r) * ((-1) ** (k - r)), N ** (k - r))
            degs: List[int] = [1] * (k - r)  # powers of Tr(Y)
            if r == 0:
                coeff *= N  # Tr(I)=N
            else:
                degs.append(r)
            out.append((coeff, tuple(degs)))
        return out

    def moment(self, degs: Sequence[int]) -> Fraction:
        """Traceless Hermitian Gaussian moment E[prod_j Tr X^{degs[j]}]."""
        key = tuple(sorted(int(d) for d in degs))
        if key in self._tm_cache:
            return self._tm_cache[key]

        terms: Dict[Degs, Fraction] = {(): Fraction(1)}
        for k in key:
            new_terms: Dict[Degs, Fraction] = {}
            for d0, c0 in terms.items():
                for c1, d1 in self._expanded_trace_terms(k):
                    kk = sorted_degs(d0 + d1)
                    new_terms[kk] = new_terms.get(kk, Fraction(0)) + c0 * c1
            terms = {d: c for d, c in new_terms.items() if c}

        val = sum(c * self._full(d) for d, c in terms.items())
        self._tm_cache[key] = val
        return val


def invert_matrix(A: List[List[Fraction]]) -> List[List[Fraction]]:
    n = len(A)
    aug = [list(A[i]) + [Fraction(int(i == j)) for j in range(n)] for i in range(n)]
    for col in range(n):
        pivot = None
        for r in range(col, n):
            if aug[r][col] != 0:
                pivot = r
                break
        if pivot is None:
            raise ArithmeticError("singular Gram matrix")
        if pivot != col:
            aug[col], aug[pivot] = aug[pivot], aug[col]
        pv = aug[col][col]
        aug[col] = [x / pv for x in aug[col]]
        for r in range(n):
            if r == col:
                continue
            fac = aug[r][col]
            if fac:
                aug[r] = [aug[r][j] - fac * aug[col][j] for j in range(2 * n)]
    return [row[n:] for row in aug]


def projection_norm(source: Monomial, basis: List[Monomial], W: TracelessWick) -> Fraction:
    if not basis:
        return Fraction(0)
    G = [[W.moment(basis[i] + basis[j]) for j in range(len(basis))] for i in range(len(basis))]
    v = [W.moment(basis[i] + source) for i in range(len(basis))]
    Gi = invert_matrix(G)
    n = len(basis)
    return sum(v[i] * Gi[i][j] * v[j] for i in range(n) for j in range(n))


def generate_odd_class_monomials(max_degree: int) -> List[Monomial]:
    """Generate odd monomials in power sums P_2,...,P_max_degree with total degree <= max_degree."""
    gens = list(range(2, max_degree + 1))
    out: List[Monomial] = []

    def rec(start: int, remaining: int, cur: List[int]) -> None:
        deg = sum(cur)
        if deg > 0 and deg % 2 == 1:
            out.append(tuple(sorted(cur)))
        for k in range(start, max_degree + 1):
            if deg + k <= max_degree:
                cur.append(k)
                rec(k, remaining - k, cur)
                cur.pop()

    rec(2, max_degree, [])
    # Sort by total degree and then lexicographically, preferring primitive-looking terms first.
    out = sorted(set(out), key=lambda m: (sum(m), len(m), m))
    return out


def independent_basis(candidates: List[Monomial], W: TracelessWick) -> List[Monomial]:
    """Greedily select a Gram-independent subbasis."""
    basis: List[Monomial] = []
    for m in candidates:
        trial = basis + [m]
        G = [[W.moment(trial[i] + trial[j]) for j in range(len(trial))] for i in range(len(trial))]
        try:
            invert_matrix(G)
            basis.append(m)
        except ArithmeticError:
            pass
    return basis


@dataclass
class OddResult:
    N: int
    c0: Fraction
    q_h2: Fraction
    q_res: Fraction
    q_total: Fraction
    R: Fraction
    Q3: Fraction
    Q5: Fraction
    Q7: Fraction

    @property
    def c1_float(self) -> float:
        return float(self.q_total) * sqrt(2 * self.N)


def compute_odd_coefficients(N: int) -> OddResult:
    W = TracelessWick(N)
    P3 = (3,)
    source = (3, 4)  # P4 P3

    norm3 = W.moment((3, 3))
    if norm3 == 0:
        raise ValueError(f"P3 has zero norm at N={N}; C-odd sector not available.")

    # First-order coefficient from H1=-P4/48.
    c0 = -Fraction(1, 48) * (W.moment((3, 4, 3)) / norm3 - W.moment((4,)))

    # H2 contribution. H2=sqrt(N/2) P6/1440, so q_H2=c_H2/sqrt(2N)=Delta<P6>/2880.
    q_h2 = (W.moment((3, 6, 3)) / norm3 - W.moment((6,))) / 2880

    # Cumulative odd bases through shells 3,5,7.
    basis3 = independent_basis(generate_odd_class_monomials(3), W)
    basis5 = independent_basis(generate_odd_class_monomials(5), W)
    basis7 = independent_basis(generate_odd_class_monomials(7), W)

    C3 = projection_norm(source, basis3, W) / norm3
    C5 = projection_norm(source, basis5, W) / norm3
    C7 = projection_norm(source, basis7, W) / norm3
    Q3, Q5, Q7 = C3, C5 - C3, C7 - C5

    # Vacuum even-sector P4 shell projections from the proven even appendix.
    Q0_2 = Fraction((N * N - 1) * (2 * N * N - 3) ** 2, 2 * N * N)
    Q0_4 = Fraction((N * N - 1) * (N ** 4 - 6 * N * N + 18), 4 * N * N)

    # Resolvent contraction for gap between shell 3 and shell 0.
    R = -Q5 / 2 - Q7 / 4 + Q0_2 / 2 + Q0_4 / 4
    q_res = R / (48 * 48)
    q_total = q_h2 + q_res

    return OddResult(N=N, c0=c0, q_h2=q_h2, q_res=q_res, q_total=q_total, R=R, Q3=Q3, Q5=Q5, Q7=Q7)


def formula_c0(N: int) -> Fraction:
    return -Fraction(3 * (N * N - 3), 16 * N)


def formula_q_h2(N: int) -> Fraction:
    return Fraction(6 * N ** 4 - 31 * N * N + 53, 768 * N * N)


def formula_q_res(N: int) -> Fraction:
    return -Fraction(26 * N ** 4 - 159 * N * N + 396, 1536 * N * N)


def formula_q_total(N: int) -> Fraction:
    return -Fraction(14 * N ** 4 - 97 * N * N + 290, 1536 * N * N)


def main() -> None:
    print("=" * 96)
    print("Exact SU(N) C-odd local class-sector coefficient engine")
    print("=" * 96)
    print("Computes c0_-, q_H2_-, q_res_-, q_-=c1_-/sqrt(2N) by exact Wick recursion.")
    print()

    Ns = list(range(3, 13))
    for N in Ns:
        r = compute_odd_coefficients(N)
        print(f"N={N}")
        print(f"  c0_-        = {fmt_frac(r.c0)}")
        print(f"  q_H2_-      = {fmt_frac(r.q_h2)}")
        print(f"  q_res_-     = {fmt_frac(r.q_res)}")
        print(f"  q_total_-   = {fmt_frac(r.q_total)}  (c1_-/sqrt(2N))")
        print(f"  c1_- approx = {r.c1_float:.15g}")
        print(f"  shell norms = Q3 {fmt_frac(r.Q3)}, Q5 {fmt_frac(r.Q5)}, Q7 {fmt_frac(r.Q7)}")
        assert r.c0 == formula_c0(N), (N, r.c0, formula_c0(N))
        assert r.q_h2 == formula_q_h2(N), (N, r.q_h2, formula_q_h2(N))
        assert r.q_res == formula_q_res(N), (N, r.q_res, formula_q_res(N))
        assert r.q_total == formula_q_total(N), (N, r.q_total, formula_q_total(N))
        print("  formula check: PASS")
        print()

    print("Closed forms verified for N=3,...,12:")
    print("  c0_-(N)  = -3(N^2-3)/(16N)")
    print("  q_H2_-(N)=  (6N^4 - 31N^2 + 53)/(768 N^2)")
    print("  q_res_-(N)=-(26N^4 -159N^2 +396)/(1536 N^2)")
    print("  q_-(N)   =-(14N^4 - 97N^2 +290)/(1536 N^2)")
    print()
    print("Therefore")
    print("  c1_-(N) = sqrt(2N) q_-(N)")
    print("          = -sqrt(2)*(14N^4 - 97N^2 + 290)/(1536 N^(3/2)).")
    print()
    print("Local C-odd expansion:")
    print("  Delta_-^(N)(beta) = sqrt(9 beta/(2N))")
    print("      - 3(N^2-3)/(16N)")
    print("      - sqrt(2)*(14N^4 - 97N^2 + 290)/(1536 N^(3/2)) beta^(-1/2)")
    print("      + O_N(beta^(-1)).")


if __name__ == "__main__":
    main()
