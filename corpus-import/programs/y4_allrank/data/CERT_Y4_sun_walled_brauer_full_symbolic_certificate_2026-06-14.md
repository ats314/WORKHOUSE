# Stable-rank SU(N) full symbolic fourth-order certificate

**Date:** June 14, 2026  
**Scope:** integer $N\ge7$.

## Final result

The balanced walled-Brauer contraction replacing the SU(3)-specific Stage-3C/3G carrier layer is complete for all three scalar outputs:

\[
\boxed{q_N=-\frac{2}{3N}\frac{Q_{32}(N^2)}{D_{34}(N^2)}},
\qquad
\boxed{A_N=\frac{640}{N(N^2-1)^3}},
\qquad
\boxed{B_N=\frac{P_{402}(N)}{D_{409}(N)}}.
\]

For every integer $N\ge7$,

\[
q_N<0,\qquad A_N>0,\qquad B_N>0.
\]

Therefore

\[
D_N(k)=A_N\sum_iX_i^2+B_N\sum_{i<j}X_iX_j,
\qquad X_i=1-\cos k_i,
\]

has the unique global minimum at $\Gamma$, the unique global maximum at $R$, and exact bandwidth

\[
\boxed{\Delta c_{4,N}=A_N+B_N>0}.
\]

The absolute fourth-order value is $c_{4,N}(\Gamma)=q_N$.

## Exact contraction census

| object | exact count |
|---|---:|
| stable ordered words | 4,171 |
| charge-conjugation orbits | 16,750 |
| balanced local signatures | 140 |
| local joint-Casimir path tensors | 330 |
| trace topologies | 3,850 |
| global fusion paths | 35,130 |
| $q_N$-contributing topologies | 2,290 |
| $q_N$-contributing paths | 27,202 |
| $A_N$-contributing topologies | 406 |
| $A_N$-contributing paths | 950 |
| $B_N$-contributing topologies | 2,328 |
| $B_N$-contributing paths | 13,096 |

The local pairing basis is $\{T_\pi:\pi\in S_k\}$ for $k\le3$, with Gram matrix

\[
G_{\pi\sigma}=N^{c(\pi^{-1}\sigma)}.
\]

Prefix Casimirs are represented exactly by the Fierz actions

\[
2T_a\!\cdot T_b=P_{ab}-\frac{1}{N}I,
\qquad
2T_a\!\cdot T_{\bar b}=-K_{a\bar b}+\frac{1}{N}I.
\]

Their joint eigenspaces reproduce all stable bipartition histories. The resulting trace networks are evaluated by exact partition/loop elimination, not by numerical color matrices.

## Exact formula for $q_N$

Set $z=N^2$. Then

\[
q_N=-\frac{2}{3N}\frac{Q_{32}(z)}{D_{34}(z)}.
\]

The denominator is

\[
D_{34}(z)=\left(z - 16\right) \left(z - 9\right)^{3} \left(z - 4\right) \left(z - 1\right)^{3} \left(2 z - 3\right) \left(2 z - 1\right)^{3} \left(3 z - 2\right) \left(3 z - 1\right) \left(4 z - 25\right) \left(4 z - 9\right)^{3} \left(4 z - 7\right) \left(4 z - 5\right) \left(4 z - 3\right) \left(4 z - 1\right) \left(9 z - 25\right) \left(9 z - 16\right) \left(16 z - 49\right) \left(16 z - 25\right) \left(16 z - 9\right) \left(16 z - 1\right) \left(4 z^{2} - 16 z + 9\right) \left(16 z^{2} - 44 z + 25\right) \left(16 z^{2} - 33 z + 16\right).
\]

All denominator factors are positive for $z=N^2\ge49$. The numerator is certified by its Newton expansion about $z=49$,

\[
Q_{32}(z)=\sum_{j=0}^{32}b_j\binom{z-49}{j},
\qquad b_j>0.
\]

Hence $Q_{32}(N^2)>0$ and $q_N<0$ for every integer $N\ge7$. The 33 exact integers $b_j$, the ordinary polynomial coefficients, and the complete compact formula are included in the machine-readable ledgers. Exact fixed-rank contractions at every rank $N=7,8,\ldots,18$ match this formula.

## Exact formula and sign of $A_N$

Direct symbolic contraction of 140 electric-history groups gives

\[
\boxed{A_N=\frac{640}{N(N-1)^3(N+1)^3}>0}.
\]

The symbolic residual is identically zero.

## Exact formula and sign of $B_N$

The $B_N$ contraction reduces to 743 electric-history groups and

\[
B_N=\frac{P_{402}(N)}{D_{409}(N)}.
\]

Every irreducible factor of $D_{409}$ is positive for $N\ge7$. The numerator has the exact Newton representation

\[
P_{402}(N)=\sum_{j=0}^{402}a_j\binom{N-7}{j},
\qquad a_j>0.
\]

Thus $B_N>0$ for every integer $N\ge7$. The complete 403-coefficient ledger and the compact 743-group rational expression are included with hashes.

## Verification gates

- Full exact fixed-rank kernels contain 189 real-space entries and satisfy Hermiticity and cubic covariance.
- $H_{4,N}(0)=q_NI$.
- The two independent extractions of $B_N$ agree exactly:
  \[
  2[c_{4,N}(M)-c_{4,N}(X)]=c_{4,N}(R)-c_{4,N}(X).
  \]
- $q_N$, $A_N$, and $B_N$ match exact fixed-rank contractions through the unused $N=18$ holdout.
- All symbolic denominator and Newton-positivity gates pass.

## Theorem status

\[
\boxed{\text{Stable-rank SU}(N\ge7)\text{ fourth-order band theorem: proved}}
\]

The remaining rank work is finite and exceptional: $SU(4)$, $SU(5)$, $SU(6)$, plus a separate pseudoreal $SU(2)$ treatment. No stable-rank Stage-3C/3G contraction remains open.
