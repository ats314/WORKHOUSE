# Source File Review — Glueball Flat-Band Paper v0.7

**Date:** 2026-06-14  
**Audit scope:** uploaded source bundles, exact certificates, fixed-rank engine, SU(3) SOS package, target manifest, TeX/PDF, and A100 notebooks.

## Executive verdict

**Mathematical core: PASS.**  
**Archival/reproducibility completeness: CONDITIONAL PASS.**

The exact SU(3) fourth-order real-space sum-of-squares theorem reruns cleanly. The stable-rank fixed-
rank walled-Brauer engine also cold-runs and reproduces the bundled exact artifacts. I found no
contradiction in the stated values of \(q\), \(A\), \(B\), the high-symmetry coefficients, or the bandwidth.

The release is not yet fully self-regenerating from primitive inputs, however. The all-\(N\) symbolic
\(q_N\) and \(B_N\) expressions are frozen artifacts checked by a verifier; the release does not include
the script that regenerates those expressions from the 35,130-path contraction. In addition, the
published symbolic verifier contains a no-op loop where fixed-rank \(B_N\) sample equality should be
checked.

## Checks completed

### 1. Archive and file integrity

- Every uploaded ZIP passed archive testing.
- Every internal SHA-256 manifest checked passed.
- The two full-symbolic bundle uploads are byte-identical.
- The two v0.7 PDF uploads are byte-identical.
- The standalone TeX, source archive, ordered-word manifest, target manifest, and bundled copies are
  mutually consistent where duplicates exist.
- All 25 audited Python source files parse and compile.

### 2. SU(3) fourth-order theorem

The exact real-space SOS certificate reran successfully and verified:

- 189 kernel records;
- canonical semantic kernel SHA-256
  `48a422a517c7c1e70b84fd88a0773943f81ae3f9bfafadbe2304f8eb7d2e9b77`;
- exact Hermiticity;
- scalar \(H_4(0)=qI\);
- the 25-point contracted stencil;
- the exact SOS identity;
- finite-torus convolution regression;
- exact \(A\), \(B\), \(X/M/R\) anchors, and bandwidth.

The targeted Stage-3G reduction also reran and reproduced:

- 33 complete \(A\)-functional keys;
- 33 complete \(B\)-functional keys;
- 64 distinct union keys with 2 overlaps;
- \(A=5/12\);
- \(B=17607806155349/275331901291200\).

### 3. Stable-rank fixed-rank contraction

The complete exact fixed-rank engine was cold-run without editing.

- \(N=7\): 3,850 trace topologies, 35,130 global fusion paths, 189 kernel records; all gates passed.
- The regenerated \(N=7\) result is exactly equal to the bundled JSON artifact.
- \(N=8\): the same full contraction completed and all gates passed.
- At both \(N=7\) and \(N=8\), independently evaluated symbolic \(q_N\), \(A_N\), and \(B_N\)
  agree exactly with the fixed-rank contraction.

A longer \(N=18\) cold run was attempted but did not complete within the audit timeout. This is not a
failed mathematical gate; it limits the number of ranks independently rerun here.

### 4. Symbolic formula verifier

`ENGINE_Y4_sun_symbolic_qab_verify.py` reran successfully and verified:

- the compact rational \(q_N\) formula;
- denominator positivity;
- the 33 positive Newton coefficients of \(Q_{32}\);
- \(q_N\) agreement with stored samples for \(N=7,\ldots,18\);
- the closed \(A_N=640/[N(N^2-1)^3]\) formula;
- the degree-409 \(B_N\) denominator;
- the 403 positive Newton coefficients of the degree-402 \(B_N\) numerator;
- positivity of the frozen \(B_N\) expression for integer \(N\ge7\).

### 5. Paper build

- The v0.7 TeX source compiled in three passes.
- The final pass had no unresolved references or layout warnings.
- The result is 20 pages.
- Raster comparison of every compiled page against the supplied PDF found zero changed pages.

## Material findings

### Critical reproducibility gap 1 — no symbolic contraction generator

The release contains:

- the arbitrary fixed-rank exact engine;
- the frozen structured \(B_N\) expression;
- frozen \(q_N\) polynomial/formula ledgers;
- positivity/Newton ledgers;
- the formula verifier.

It does **not** contain a source program that starts from the 4,171 ordered words and local
walled-Brauer projectors and regenerates the full symbolic rational functions \(q_N\) and \(B_N\) over
\(\mathbb Q(N)\).

Therefore the release currently proves two separate things:

1. fixed-rank exact contractions can be regenerated; and
2. the supplied symbolic formulas have the stated algebraic and positivity properties.

It does not yet provide a cold, executable bridge from item 1 to item 2 for arbitrary symbolic \(N\).
That bridge should be included before calling the source release fully archival.

### Critical reproducibility gap 2 — the verifier does not compare stored \(B_N\) samples

The symbolic verifier contains:

```python
for row in cert['B'].get('samples', cert.get('samples', [])):
    pass
```

This loop performs no assertion. The later loop checks only that the frozen \(B_N\) expression is
positive at ranks listed in the \(q_N\) sample table. It does not compare symbolic \(B_N\) against an
independently stored fixed-rank \(B_N\) value.

The independently rerun \(N=7\) and \(N=8\) contractions do agree with the symbolic expression, so
this is a verifier coverage defect, not evidence that the formula is wrong.

**Required repair:** store exact \(B_N\) samples for at least \(N=7,\ldots,18\), including the declared
holdout, and assert exact equality in the verifier.

### Major release-completeness gap — lower-order certificate sources are absent

The paper's Appendix A names several lower-order independent scripts, but they are not present in the
v0.7 source release or the uploaded source bundles:

- `ENGINE_FLUX_su3_moments_ext.py`
- `ENGINE_FLUX_su3_domino_d3.py`
- `ENGINE_FLUX_glueball_band_certificate_v2.py`
- `ENGINE_FLUX_cls_flat_band_certificate_v1_1.py`
- `ENGINE_SUN_closed_surface_band_stage1_certificate.py`
- `ENGINE_Y4_exact_analytic_factorization_certificate.py`

The fourth-order real-space SOS certificate is present. The release is therefore substantially
self-contained for the newest fourth-order work, but not for every lower-order theorem and numerical
constant retained in the paper.

### Major package-hygiene issue — stale Stage-3G status bundle

The older standalone Stage-3G wiring bundle still says physical normalization and final \(A_N,B_N\)
outputs are unresolved. The newer full-symbolic bundle and fixed-rank engine supersede that status.

The older bundle should be labeled `ARCHIVAL_INTERMEDIATE_DO_NOT_USE_FOR_FINAL_STATUS`, or removed
from the publication release, to prevent a reviewer from concluding that the paper contradicts its
own source package.

### Moderate engineering issues

1. **Ambiguous file discovery.** The fixed-rank scripts recursively select the first matching filename
   from `/content`, the current directory, or `/mnt/data`. A stale duplicate can be selected silently.
   Publication scripts should use explicit command-line paths or bundle-relative paths and verify
   expected hashes before execution.

2. **Assertions used as proof gates.** Many hard gates use Python `assert`; `python -O` disables them.
   Replace with explicit checks that raise exceptions.

3. **Hardcoded path count.** The fixed-rank output writes `global_fusion_paths: 35130` as a literal
   rather than the computed `path_total`. The computed run did produce 35,130, but the payload should
   serialize the computed value and assert the expected count.

4. **No locked environment.** Add `NOTE_MISC_requirements.txt` or a Conda lock, Python/SymPy version constraints,
   and a one-command cold-run entry point.

5. **No explicit license.** Add a source and data license before public release.

### Stage-2 serialized verifier

The packaged serialized Stage-2 verifier was started twice but did not complete within the audit
runtime limits. Its archives and checksums are intact, and the newer fixed-rank engine independently
recomputed the local 140-signature layer while completing the \(N=7\) and \(N=8\) global runs. This
is an uncompleted audit item, not a failed result.

## A100 notebook assessment

The GPU notebooks divide into two categories:

- **Useful regression:** the SOS A100/CPU check agrees with the exact theorem at floating-point
  precision and is a valid independent implementation test.
- **Exploratory spectroscopy:** the Monte Carlo/GEVP/string-tension notebooks do not yet contain enough
  statistically independent configurations for physical mass or string-tension claims. Stored outputs
  include very small effective sample counts, unstable uncertainties, and failed/undefined mass fits.

The paper correctly treats the GPU work as a regression rather than part of the exact proof and
correctly states that a same-normalization string-tension series is still needed for continuum mass
comparison.

## Recommended release gate

Before submission or public archival release, require these five changes:

1. Add the symbolic \(\mathbb Q(N)\) contraction generator for \(q_N\) and \(B_N\).
2. Repair the no-op \(B_N\) sample loop and include exact fixed-rank samples/holdout values.
3. Add the six missing lower-order certificate scripts and their frozen input artifacts.
4. Replace recursive filename discovery with explicit hashed inputs and replace `assert` proof gates.
5. Remove or clearly quarantine superseded intermediate bundles and add a locked environment plus
   one-command reproduction script.

## Final assessment

- **SU(3) fourth-order SOS theorem:** reproducible and internally consistent.
- **Stable-rank fixed-rank contraction:** reproducible at audited ranks and consistent with the frozen
  formulas.
- **All-\(N\) positivity theorem for the supplied formulas:** algebraically verified.
- **All-\(N\) symbolic derivation from primitive source:** not yet fully regenerable from this release.
- **Paper PDF/TeX consistency:** pass.
- **Continuum glueball-mass prediction:** not supplied by these source files, consistent with the
  manuscript's stated scope.

**Publication readiness:** mathematically strong, but source release should be revised once more before
being described as fully self-contained or archival-grade.
