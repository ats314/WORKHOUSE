# SU(4) fourth-order determinant-sector completion

**Status:** PASS  
**Scope:** complete projected one-flux $T_1^{+-}$ coefficient through $O(y^4)$.

## Exceptional finite-rank census

The spatial corpus remains 4,171 ordered words. The SU(4) selection rule adds 312 sign assignments,
forming 156 charge-conjugation orbits across 76 words. Of these, 128 are final-only corrections
and 28 contain an exceptional determinant channel at the third resolvent cut. The exceptional
contraction reduces to 96 trace topologies and 1,806 exact fusion paths.

The 42 exceptional local token signatures consist of 30 rank-one epsilon sectors and
12 four-dimensional $(5,1)/(1,5)$ invariant sectors. Nested partial Casimirs resolve every path.

## Determinant correction

The generic stable-rank expression for $q_N$ is singular at $N=4$, so the exact-balance
sector was recomputed directly at fixed rank with the folded resonant prescription before
adding the determinant sector.

The complete epsilon-sector kernel has 39 entries, but its projection onto the cube-boundary
branch is exactly momentum-independent:

\[
\Delta q_4=-304746539168/160249753125,\qquad \Delta A_4=\Delta B_4=0.
\]

## Final exact SU(4) coefficients

\[
q_4=-162485785670299274695454289332603/121294607143027203361265133093750,
\]
\[
A_4=32/675,\qquad B_4=3601925923737103752887/70481696720359496343750,
\]
\[
\Delta c_{4,4}=A_4+B_4=2314426811641505637629/23493898906786498781250>0.
\]

For $X_i=1-\cos k_i$ the exact projected numerator is

\[
D_4(k)=A_4\sum_iX_i^2+B_4\sum_{i<j}X_iX_j,
\]

and

\[
c_{4,4}(k)=q_4+\frac{D_4(k)}{2\sum_iX_i}.
\]

Because $A_4>0$ and $B_4>0$, $\Gamma$ is the unique global minimum and
$R=(\pi,\pi,\pi)$ is the unique global maximum.

Full-kernel semantic SHA-256: `e8bc5badc026d9874af56cd9ded47c4f0b0833597cb13ae5fd5e618a113dfeb9`.

Certificate SHA-256: `c7134744af13ae171787bd9fe510591e95a6375f3b0442e4c1619b8924ed2b5b`.
