# Independent audit: stable-rank SU(N) Stage 1

**Date:** June 14, 2026  
**Scope:** the uploaded `NB_Y4_from_scratch_alt.ipynb`, stable-rank executable, extracted source archive, ordered-word manifest, and certificate.

## Verdict

\[
\boxed{\text{All executable stable-rank Stage-1 gates reproduce successfully.}}
\]

The previously missing complete-source dependency is now supplied. The stable-rank executable ran unmodified against an independently regenerated Stage-0 support manifest and exited successfully.

## Reproduced gates

- connected supports: **182,440**
- candidate support/output pairs: **895,524**
- stable support/output classes: **439**
- canonical ordered words: **4,171**
- exact-balance sign assignments: **33,500**
- charge-conjugation orbits: **16,750**
- balanced token signatures: **140**
- symbolic energy signatures: **37,500**
- resonant signatures: **17,073**
- nonresonant signatures: **20,427**
- distinct denominator polynomials: **94**
- accidental integer roots for integer N >= 7: **0**
- balanced SU(3) channel regression: **140/140**, zero mismatches

## Source provenance

All nine extracted source files are byte-identical to the corresponding sources embedded in the complete-from-scratch notebook:

`stage0.py`, `stage1.py`, `stage2.py`, `stage3b.py`, `stage3c.py`, `stage3e.py`, `stage3g.py`, `stage3i.py`, and `stage3j.py`.

This includes the Stage-3I folded des-Cloizeaux generator.

## Manifest comparison

The rerun produces exactly the same 4,171 ordered-word records. The only semantic metadata difference is the filesystem path of the independently regenerated Stage-0 support file. The normalized summary is exact. The compressed-file SHA-256 differs because the gzip artifact contains run-dependent metadata and the support-path string; this is not a mathematical discrepancy.

## Non-mathematical defect

The executable's Markdown template is a raw f-string but writes doubled LaTeX backslashes. A fresh rerun therefore emits commands such as `\\frac` and `\\ge` instead of `\frac` and `\ge`. The uploaded certificate has normalized single backslashes. This is a presentation bug only; it does not affect the JSON, word manifest, enumeration, denominator analysis, or regression gates. The repair is to use single backslashes inside the raw template.

## Logical boundary

This audit verifies the stable-rank geometry, exact-balance reduction, symbolic bipartition channel enumeration, denominator classification, and SU(3) balanced-channel regression. It does **not** produce the open symbolic Stage-3C/3G walled-Brauer contraction or the rational functions q_N, A_N, and B_N.

## Status

\[
\boxed{\text{SU(3) fourth-order source provenance: closed}}
\]

\[
\boxed{\text{SU}(N\ge7)\text{ Stage-1 geometry and denominator theorem: independently reproduced}}
\]

\[
\boxed{\text{Symbolic balanced contraction for }q_N,A_N,B_N: \text{open}}
\]
