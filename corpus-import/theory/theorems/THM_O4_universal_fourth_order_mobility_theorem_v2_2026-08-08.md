# Universal Fourth-Order Mobility Theorem — corrected case-complete form

**Date:** 2026-08-08  
**Status:** exact case-complete theorem relative to the accepted finite-rank and stable-rank certificates. Not yet a unified cold microscopic reproduction bundle.

## Theorem U4M

For the three-dimensional \(SU(N)\) Wilson one-plaquette \(C\)-odd branch, let \(\alpha_N\) denote the old-pencil axial fourth-order mobility coefficient. Then for every integer \(N\ge3\),

\[
\boxed{
\alpha_N=
\frac{640}{N(N^2-1)^3}.
}
\]

In four-shape notation,

\[
\boxed{
A_N^{\rm shp}
=
\frac{\alpha_N}{4}
=
\frac{160}{N(N^2-1)^3}.
}
\]

## Proof

Partition the ranks:

\[
\{N\in\mathbb Z:N\ge3\}
=
\{3,4,5,6\}\sqcup\{N\ge7\}.
\]

The exact finite-rank registry gives

\[
\alpha_3=\frac5{12},
\qquad
\alpha_4=\frac{32}{675},
\qquad
\alpha_5=\frac1{108},
\qquad
\alpha_6=\frac{64}{25725}.
\]

Direct substitution gives

\[
\frac{640}{3(3^2-1)^3}=\frac5{12},
\]

\[
\frac{640}{4(4^2-1)^3}=\frac{32}{675},
\]

\[
\frac{640}{5(5^2-1)^3}=\frac1{108},
\]

\[
\frac{640}{6(6^2-1)^3}=\frac{64}{25725}.
\]

The accepted exact stable-rank theorem gives the same rational function for every \(N\ge7\). These cases exhaust all integers \(N\ge3\). Therefore

\[
\boxed{
\alpha_N=
\frac{640}{N(N^2-1)^3}
\quad\forall N\ge3.
}
\]

\(\square\)

## Exceptional-rank structural facts

These facts are useful explanations but are **not needed logically** for the case-exhaustion proof above.

### SU(4)

The complete exceptional certificate proves

\[
H^{\rm exc}_{4,4}(k)\psi(k)
=
\Delta q_4\psi(k)
\]

identically, with

\[
\Delta q_4=
-\frac{304746539168}{160249753125},
\qquad
\Delta\alpha_4=\Delta\beta_4=0.
\]

The full exceptional matrix is not scalar.

The Laurent–Koszul cage-annihilator theorem now further implies

\[
H^{\rm exc}_{4,4}-\Delta q_4I
=
C_4S
=
-C_4\widetilde N^T
\]

for some Laurent-polynomial \(C_4\).

### SU(5)

At exactly six terminal fundamental/antifundamental factors, an \(SU(5)\) determinant family would require

\[
p+q=6,\qquad |p-q|=5.
\]

The sum and difference have incompatible parity, so no integer solution exists. This is consistent with the recovered empty exceptional scan.

### SU(6)

The exact finite-rank registry gives

\[
\alpha_6=\frac{64}{25725}.
\]

The independent resolvent arithmetic gives

\[
C_2(\Lambda^kV)
=
\left(\frac{14}{3},\frac{21}{4},\frac{14}{3}\right),
\]

\[
\Delta E
=
\left(-\frac72,-\frac{14}{3},-\frac72\right),
\]

and

\[
F_{\det}=-\frac6{343},
\qquad
\Delta q_6=\frac6{343}.
\]

The current build also records a same-plaquette exceptional word. However, in this corrected theorem we **do not promote that fact alone** to the stronger full-matrix claim

\[
H^{\rm exc}_{4,6}=\Delta q_6 I_3
\]

without the complete microscopic SU(6) exceptional kernel/certificate in the active reproducibility bundle.

## Provenance boundary

The universal mobility formula is case-complete relative to accepted exact records, but publication-grade cold reproduction still calls for one bundle regenerating:

1. the SU(3) microscopic fourth-order kernel;
2. the SU(4) exceptional kernel and Laurent residual;
3. the SU(5) microscopic finite-rank certificate;
4. the SU(6) microscopic finite-rank certificate;
5. the stable-rank \(N\ge7\) contraction certificate;
6. the degree-seven Gram matrix construction.

## Stronger conceptual target

The exact SU(4) result motivates the quotient-scalar question

\[
P_{\rm cage}(k)
H^{\det}_{4,N}(k)
P_{\rm cage}(k)
=
\delta q_N P_{\rm cage}(k),
\]

with \(\delta q_N\) independent of momentum.

For SU(4), this property is certified. The Laurent–Koszul theorem shows that, for finite-range Laurent residuals in the SU(4) convention, quotient scalarity is equivalent to membership in the one-sided cage-annihilator module.

The remaining microscopic theorem is therefore not an abstract factorization problem; it is to prove that determinant contractions land in that module before the final cancellation is evaluated.
