# Independent cold rerun: stable-rank \(SU(N\ge7)\) fourth-order theorem

**Date:** June 14, 2026  
**Verdict:** **PASS**

## What was rerun

1. The bundled symbolic verifier was executed unmodified.
2. The complete 35,130-path fixed-rank contraction was cold-rerun independently
   for every integer rank \(N=7,8,\ldots,18\).
3. Every rerun was compared exactly against the stored \(q_N\) samples, the
   symbolic \(q_N,A_N,B_N\) formulas, and all high-symmetry reconstruction identities.
4. The duplicate bundles, source-release nested bundle, ordered-word archive,
   source archive, certificate, and verifier were compared byte-for-byte.

## Exact result

\[
q_N=-\frac{2}{3N}\frac{Q_{32}(N^2)}{D_{34}(N^2)}<0,
\]

\[
A_N=\frac{640}{N(N^2-1)^3}>0,
\qquad
B_N>0
\]

for every integer \(N\ge7\).

The projected band is

\[
D_N(k)=A_N\sum_iX_i^2+B_N\sum_{i<j}X_iX_j,
\qquad X_i=1-\cos k_i.
\]

Hence \(\Gamma\) is the unique global minimum, \(R\) is the unique global
maximum, and

\[
\Delta c_{4,N}=A_N+B_N>0.
\]

## Fixed-rank cold-rerun table

| \(N\) | Runtime (s) | \(q_N\) | \(A_N\) | \(B_N\) | Bandwidth | Gates |
|---:|---:|---:|---:|---:|---:|:---:|
| 7 | 27.72 | -0.01630173231 | 0.0008267195767 | 0.0008867478516 | 0.001713467428 | PASS |
| 8 | 30.00 | -0.007962231415 | 0.0003199398513 | 0.0003430456158 | 0.0006629854671 | PASS |
| 9 | 31.00 | -0.004282649062 | 0.0001388888889 | 0.0001488849651 | 0.0002877738539 | PASS |
| 10 | 31.00 | -0.002475088607 | 6.595904974e-05 | 7.069522497e-05 | 0.0001366542747 | PASS |
| 11 | 32.00 | -0.00151313937 | 3.367003367e-05 | 3.608371838e-05 | 6.975375205e-05 | PASS |
| 12 | 32.00 | -0.0009680113247 | 1.823856291e-05 | 1.954443154e-05 | 3.778299445e-05 | PASS |
| 13 | 31.00 | -0.0006429488269 | 1.038266344e-05 | 1.112536876e-05 | 2.15080322e-05 | PASS |
| 14 | 32.00 | -0.0004407445925 | 6.165213266e-06 | 6.605913906e-06 | 1.277112717e-05 | PASS |
| 15 | 31.00 | -0.0003103926583 | 3.796161322e-06 | 4.067362945e-06 | 7.863524267e-06 | PASS |
| 16 | 29.00 | -0.0002237503828 | 2.412345176e-06 | 2.584606079e-06 | 4.996951255e-06 | PASS |
| 17 | 28.00 | -0.0001646129335 | 1.575990478e-06 | 1.688486342e-06 | 3.26447682e-06 | PASS |
| 18 | 28.00 | -0.0001232999452 | 1.055115254e-06 | 1.130406831e-06 | 2.185522085e-06 | PASS |

Every rank reproduced 4,171 ordered words, 16,750 charge-conjugation orbits,
140 balanced signatures, 3,850 trace topologies, 35,130 global fusion paths,
189 real-space kernel entries, and 63 root entries.

For every rank,

\[
X=q_N+A_N,\qquad
M=q_N+A_N+\frac12B_N,\qquad
R=q_N+A_N+B_N,
\]

with

\[
R-2M+X=0
\]

exactly.

## Provenance

- The two uploaded full-symbolic ZIPs are byte-identical.
- The source-release nested full-symbolic ZIP is byte-identical to them.
- The separately uploaded ordered-word and source archives are byte-identical
  to their bundled counterparts.
- The source-release certificate and verifier are byte-identical to the bundled files.
- The cold-rerun \(N=7\) result matches the packaged \(N=7\) result semantically.

Canonical certificate SHA-256:

```text
50c3b0e945b87347416b1458b4346cee84b7d2e15385a152fa31a7adf1d500cd
```

Canonical full-symbolic bundle SHA-256:

```text
8feec874aa16c823bb837efa8df626d5cf735db5ecaa6c90b8806ddf456b51a5
```

## Final status

\[
\boxed{\text{Stable-rank }SU(N\ge7)\text{ fourth-order band theorem: independently reproduced}}
\]

No stable-rank Stage-3C or Stage-3G contraction remains open. The remaining
rank work is finite and exceptional: \(SU(4)\), \(SU(5)\), and \(SU(6)\), with
\(SU(2)\) requiring a separate pseudoreal treatment.
