# Fourth-order band-shape theorem for all non-pseudoreal SU(N)

**Status:** PASS  
**Scope:** integer SU(N), N>=3, in the verified fourth-order one-flux $T_1^{+-}$ effective Hamiltonian.

Let

\[
D_N(k)=\psi^\dagger[H_{4,N}(k)-q_NI]\psi,
\qquad X_i=1-\cos k_i.
\]

The established symmetry and displacement gates force

\[
D_N(k)=A_N\sum_iX_i^2+B_N\sum_{i<j}X_iX_j.
\]

## Coefficients

For SU(3),

\[
A_3=5/12,\qquad B_3=17607806155349/275331901291200.
\]

For every integer $N\ge4$,

\[
\boxed{A_N=\frac{640}{N(N^2-1)^3}},
\qquad
\boxed{B_N=\frac{P_{402}(N)}{D_{409}(N)}}.
\]

The exact structured expression for $B_N$ is frozen separately. For $N\ge7$, positivity follows from the 403 strictly positive Newton coefficients of $P_{402}$ about $N=7$ and positivity of every denominator factor. At $N=4,5,6$, positivity is checked exactly.

| N | $A_N$ | $B_N$ | $A_N+B_N$ |
|---:|---:|---:|---:|
| 3 | `5/12` | `17607806155349/275331901291200` | `132329431693349/275331901291200` |
| 4 | `32/675` | `3601925923737103752887/70481696720359496343750` | `2314426811641505637629/23493898906786498781250` |
| 5 | `1/108` | `126537112003083861011/12716894720031723060840` | `81428712396187592747/4238964906677241020280` |
| 6 | `64/25725` | `235401086266217267636986869176/88159201615617988827817767796875` | `454728157341029756849050509176/88159201615617988827817767796875` |

## Exceptional-rank reduction

- **SU(4):** the full scan adds 312 determinant-sector assignments, or 156 charge-conjugation orbits. Only 40 exceptional words enter the 64-key $A/B$ target. Their 48 topology amplitudes form nine exact classes. Every $A$-functional coefficient vanishes individually; in every $B$-amplitude class the $+8$ and $-8$ coefficients occur with equal multiplicity. Hence
  \[
  \Delta A_4=\Delta B_4=0.
  \]
- **SU(5):** no determinant-sector assignment occurs anywhere in the complete fourth-order geometry.
- **SU(6):** one determinant charge-conjugation orbit occurs globally, but it is absent from all 64 $A/B$ target entries. Hence it cannot modify $A_6$ or $B_6$.

The SU(4) contraction implementation independently reproduces the complete balanced $A_4$ and $B_4$ target before the determinant correction is added.

## Theorem

For every integer $N\ge3$,

\[
A_N>0,\qquad B_N>0.
\]

Therefore

\[
\boxed{\Gamma\text{ is the unique global minimum}},\qquad
\boxed{R\text{ is the unique global maximum}},
\]

and

\[
\boxed{\Delta c_{4,N}=A_N+B_N>0}.
\]

This closes the fourth-order projected band-shape theorem for every non-pseudoreal SU(N). SU(2) remains separate. The common offsets $q_4$ and $q_6$ still require their determinant-sector corrections; those offsets do not affect the extrema or bandwidth theorem.
