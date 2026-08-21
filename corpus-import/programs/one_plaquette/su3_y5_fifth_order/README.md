# SU(3) one-flux C-odd band — fifth order (Y5) — campaign intake (2026-06-14)

**What this is.** The exact fifth-order (\(O(y^5)\), \(y=\beta_{\rm lat}/6=1/g_H^4\)) des-Cloizeaux
contraction for the SU(3) one-flux \(T_1^{+-}\) band — the order-5 extension of the flat-band /
band-shape program. Deposited from the 2026-06-14 ZIP-ARCHIVES drop after independent cold verification.

## The result

\[
q_5=-\frac{866236750503342026253096691057}{1169668083793811403447133488000}\approx-0.740583386437,
\quad A_5=\frac{313}{240},\quad
B_5=\frac{1881863087742908605903793}{1652932248975967181040000}.
\]

With \(S=\sum X_i,\;Q=\sum X_i^2,\;R=\sum_{i<j}X_iX_j\) (\(X_i=1-\cos k_i\)),
\[
c_5(k)=q_5+\frac{A_5 Q + B_5 R}{2S},
\]
an exact 25-term Laurent-polynomial identity from the complete 189-record real-space kernel.
\(A_5>0,\;B_5>0\); exact bandwidth \(=4037562229115732471176793/1652932248975967181040000\).

## Verification done this session (grounds: T1 machine-gated)

`ENGINE_Y5_verify_su3.py` cold (Python 3.10, sympy 1.14.0), no cache:

```
ALL SU3 O(y^5) GATES PASS   (exit 0)
```

Gates include: 29366 words / 22071 blocks / 524823 global paths / 189 kernel entries; q₅ summary
match; fourth-order des-Cloizeaux regression; exact Hermiticity; **H₅(Γ) = q₅·I** (exact); exact
Laurent factorization D = A₅Q + B₅R (25 terms); A₅,B₅ positive; bandwidth exact; Stage2/Stage3G span.
Kernel semantic SHA256 `123dbf137adfbda22c2fea36c45631ea0a93ef1cd126aed90da5fee04df0a5ed`. Cold-run gate
log: `RUN_Y5_verify_su3_bundle.log`.

**Scope honesty.** T1 (machine-gated, cold-reproduced). Not T2/T3; not promoted to "established."

## Provenance

- Source: `C:\ALL THEORY\ZIP ARCHIVES\SU3_Y5_COMPLETE_FIFTH_ORDER_BUNDLE.zip` — md5 `33343b4b95533143cf2b9884b8ccce47` (19.7 MB).
- Distilled here: theorem, certificate, the two verifier scripts, the stage summaries, cold-run log.
  The bulk \(O(y^5)\) data (`y5_*.json.gz` kernels/words/topology, the `y5_stage0_*.cpp` enumerators,
  `*_INPUTS.zip`, COLAB notebook) stays in the source bundle. Per-file MD5 in `MAN_SUN_md5sums.txt`.
- Y6 is only a partial historical (KPS/Hamer) transcription (`SU3_Y5_Y6_HISTORICAL_RECOVERY*`), not a computation.

## Open / next
- O(y⁶) band coefficients beyond the KPS denominators (would extend the series).
- T2 review of the des-Cloizeaux contraction would raise the tier.
