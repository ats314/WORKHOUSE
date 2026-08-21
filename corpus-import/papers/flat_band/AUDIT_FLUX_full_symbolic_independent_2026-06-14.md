# Independent audit: stable-rank SU(N>=7) fourth-order theorem

**Date:** June 14, 2026  
**Verdict:** **PASS**

## Closed result

For every integer \(N\ge 7\), the uploaded exact source chain certifies

\[
D_N(k)=A_N\sum_i X_i^2+B_N\sum_{i<j}X_iX_j,
\qquad X_i=1-\cos k_i,
\]

with

\[
q_N=-\frac{2}{3N}\frac{Q_{32}(N^2)}{D_{34}(N^2)},
\qquad
A_N=\frac{640}{N(N^2-1)^3},
\qquad
B_N=\frac{P_{402}(N)}{D_{409}(N)}.
\]

The exact sign certificates give

\[
q_N<0,\qquad A_N>0,\qquad B_N>0.
\]

Therefore \(\Gamma\) is the unique projected fourth-order minimum, \(R\) is the unique maximum, and

\[
\Delta c_{4,N}=A_N+B_N>0.
\]

No stable-rank Stage-3C or Stage-3G contraction remains open.

## Checks rerun

- All 20 files in the bundled SHA-256 manifest passed.
- Every separately uploaded source or ledger was byte-identical to its bundled counterpart.
- `ENGINE_Y4_sun_symbolic_qab_verify.py` ran unmodified and passed all gates.
- \(Q_{32}\) and \(D_{34}\) have exact degrees 32 and 34 in \(z=N^2\).
- The 33 positive Newton coefficients of \(Q_{32}\) were recomputed.
- The symbolic \(q_N\) formula matches every stored exact sample for \(N=7,\ldots,18\).
- The \(B_N\) ledger contains exactly 403 positive Newton coefficients followed by its certified zero tail, consistent with numerator degree 402 and denominator degree 409.
- The bundled exact \(N=7\) kernel artifact has 189 entries and passes Hermiticity, cubic covariance, scalar-\(\Gamma\), closed-form \(A_N\), and both independent \(B_N\) extraction gates.
- The \(N=7\) values of \(q_N\), \(A_N\), \(B_N\), and \(A_N+B_N\) independently match the symbolic formulas.

## Exact contraction census

| Object | Count |
|---|---:|
| Stable ordered words | 4,171 |
| Charge-conjugation orbits | 16,750 |
| Balanced signatures | 140 |
| Local joint paths | 330 |
| Trace topologies | 3,850 |
| Global fusion paths | 35,130 |
| \(q_N\)-contributing paths | 27,202 |
| \(A_N\)-contributing paths | 950 |
| \(B_N\)-contributing paths | 13,096 |

## Provenance

Canonical full-symbolic certificate SHA-256:

```text
50c3b0e945b87347416b1458b4346cee84b7d2e15385a152fa31a7adf1d500cd
```

The complete fixed-rank 35,130-path generator was not cold-rerun during this audit. Its bundled exact \(N=7\) output, symbolic expressions, coefficient ledgers, manifest, and verifier were independently checked. This limitation concerns runtime provenance, not any failed mathematical gate.
