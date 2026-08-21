# Stable-rank SU(N) fourth-order Stage-1 certificate

**Scope:** integer \(N\ge7\).

## Stable-rank reduction

The verified fourth-order geometry has maximum local tensor degree six.  An
\(SU(N)\) invariant with \(n_f\) fundamental and \(n_{\bar f}\)
antifundamental indices requires

\[
n_f-n_{\bar f}\equiv0\pmod N.
\]

For \(N\ge7\), \(|n_f-n_{\bar f}|\le6\), hence the condition is equivalent
to \(n_f=n_{\bar f}\).  Therefore no determinant/epsilon sectors occur.
Only the balanced families \((1,1),(2,2),(3,3)\) survive.

## Exact geometry counts

- connected supports: **182,440**
- candidate support/output pairs: **895,524**
- stable support/output classes: **439**
- canonical ordered words: **4,171**
- exact-balance sign assignments: **33,500**
- charge-conjugation orbits: **16,750**

The sign masks were recomputed after rotating each ordered transition into its
canonical frame.

## Local Haar data

- unique balanced token signatures: **140**
- \((1,1)\) occurrences: **173,520**
- \((2,2)\) occurrences: **13,140**
- \((3,3)\) occurrences: **400**

The balanced Weingarten coefficients are

\[
\mathrm{Wg}_1(e)=\frac1N,
\]

\[
\mathrm{Wg}_2(e)=\frac1{N^2-1},\qquad
\mathrm{Wg}_2((12))=-\frac1{N(N^2-1)},
\]

and

\[
\mathrm{Wg}_3(e)=
\frac{N^2-2}{N(N^2-1)(N^2-4)},
\]

\[
\mathrm{Wg}_3((12))=
-\frac1{(N^2-1)(N^2-4)},
\qquad
\mathrm{Wg}_3((123))=
\frac2{N(N^2-1)(N^2-4)}.
\]

## Symbolic representation channels

Stable-rank irreducible channels are represented by bipartitions
\((\lambda,\mu)\), with exact Casimir

\[
C_2(\lambda,\mu)=
\frac{
N^2(|\lambda|+|\mu|)
+N[\kappa(\lambda)+\kappa(\mu)]
-(|\lambda|-|\mu|)^2
}{2N}.
\]

Exact counts:

- energy signatures: **37,500**
- resonant: **17,073**
- nonresonant: **20,427**
- all-resonant orbits: **7,452**
- mixed orbits: **2,673**
- nonresonant-only orbits: **6,625**
- maximum energy signatures per orbit: **105**
- maximum global channel-path multiplicity: **1296**
- distinct denominator polynomials: **94**
- accidental integer denominator roots for \(N\ge7\): **none**

The bipartition engine was evaluated at \(N=3\) and compared with the existing
SU(3) \((p,q)\) engine on all **140** balanced
token signatures: **zero mismatches**.

## Verdict

The geometry and denominator layers of the fourth-order calculation now have
an exact stable-rank \(SU(N\ge7)\) formulation.  The next load-bearing step is
the symbolic balanced contraction layer replacing the SU(3)-specific
Stage-3C/3G carrier matrices by walled-Brauer diagram tensors.
