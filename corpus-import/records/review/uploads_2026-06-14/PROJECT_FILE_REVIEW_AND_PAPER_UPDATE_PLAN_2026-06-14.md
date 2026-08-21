# Project-file review and paper update plan

**Date:** June 14, 2026  
**Current manuscript:** `glueball_flat_band_paper_v0_7.tex/pdf`

## Verdict

The paper can and should be updated to v0.8. The core SU(3) theorem and the stable-rank symbolic sign theorem remain intact. The update should combine one necessary verification correction with two substantive additions: the Stage-3G implementation provenance and the newly extractable large-N asymptotics.

## Archives reviewed

- `GLUEBALL_FLAT_BAND_SOURCE_RELEASE_V0_7.zip`
- `Y4_SUN_WALLED_BRAUER_FULL_SYMBOLIC_BUNDLE_2026-06-14.zip`
- `SU_N_STAGE3G_WIRING_BUNDLE.zip`
- `Y4_SOS_TARGETED_STAGE3G_REDUCTION_BUNDLE.zip`
- `SU_N_WALLED_BRAUER_STAGE2A_BUNDLE.zip`
- corrected `SU_N_WALLED_BRAUER_STAGE2A_BUNDLE_R2.zip`
- `Y4_REAL_SPACE_SOS_PACKAGE.zip`
- corrected `Y4_REAL_SPACE_SOS_PACKAGE_V0_6.zip`
- `y4_extracted_sources.zip`
- standalone symbolic formulas, ledgers, verifier, fixed-rank engine, and ordered-word manifest

Every ZIP passed `unzip -t`. The duplicate `B_newton_coefficients` files are byte-identical.

## Rerun results

### Full symbolic verifier

`ENGINE_Y4_sun_symbolic_qab_verify.py` ran unmodified and passed:

- compact q formula and degrees 32/34 in z=N^2;
- 33 positive q numerator Newton coefficients;
- stored q fixed-rank matches N=7,...,18;
- exact A formula;
- B denominator degree 409 and 403 positive Newton coefficients;
- q<0, A>0, B>0 for all integer N>=7.

### Stage-3G wiring self-tests

The standalone trace-wiring contractor reran and passed all 147 gates:

- E|Tr U|^2=1, E|Tr U|^4=2, E|Tr U|^6=6;
- two-link connected and disconnected tests;
- 140/140 local signature/path interfaces;
- global charge-conjugation invariance;
- fourth-order folded-coefficient permutation symmetry.

This bundle is an intermediate implementation certificate. Its own status document correctly states that it predates recovery of the external physical normalization.

### Targeted Stage-3G reduction

The targeted SOS reduction reran and passed:

- 189-record semantic kernel hash;
- 33 A-functional keys and 33 B-functional keys;
- 64-key union with two overlaps;
- exact SU(3) regressions A_3=5/12 and B_3=17607806155349/275331901291200;
- cubic equality of all double-axis and face-diagonal coefficients.

This is a useful computational reduction and should be included as a methods remark or supplement.

## Necessary correction to v0.7

The manuscript and certificate state that q_N, A_N, and B_N match exact fixed-rank contractions for every N=7,...,18, including an N=18 holdout.

The bundled evidence supports a narrower statement:

- the certificate stores exact fixed-rank samples for q_N at N=7,...,18;
- the bundle includes one complete fixed-rank kernel artifact, at N=7, which matches q_7, A_7, and B_7;
- no N=8,...,18 full-kernel artifacts or A/B sample ledger are included;
- `ENGINE_Y4_sun_symbolic_qab_verify.py` contains no A/B fixed-rank equality assertion for those ranks; its legacy B-sample loop is a no-op.

Therefore replace the overbroad statement with:

> Stored exact fixed-rank values of q_N for N=7,...,18 match the compact formula. The bundled complete N=7 kernel independently matches q_7, A_7, and B_7 and passes both B extractions. The all-rank signs and formulas for A_N and B_N are certified by the exact symbolic residual, denominator factorizations, and positive Newton expansions.

The stronger N=7,...,18 claim may be restored only after including the corresponding full-kernel outputs or a machine-readable A/B sample ledger and active verifier assertions.

## Reproducibility qualification

The full symbolic bundle contains the final q and B expressions, ledgers, hashes, a verifier, and the fixed-rank contraction engine. It does not contain the symbolic-generation script that derives the structured B expression and q polynomial directly from the 35,130 path contraction. The paper should either:

1. include that generator in v0.8, or
2. describe the symbolic formulas as certified output artifacts whose internal algebra and N=7 fixed-rank anchor are independently verified, rather than calling the symbolic chain fully reproducible from scratch.

## New exact large-N corollary

The certified formulas imply

q_N = -227/N^5 - 1638943/(864 N^7) + O(N^-9),

A_N = 640/N^7 + 1920/N^9 + O(N^-11),

B_N = 6170/(9 N^7) + 677903/(324 N^9) + O(N^-11),

and hence

Delta c_{4,N} = A_N+B_N = 11930/(9 N^7) + O(N^-9).

Therefore

Delta c_{4,N}/|q_N| = 11930/(2043 N^2) + O(N^-4).

This shows a parametric large-N flattening: the fourth-order rest-energy shift scales as N^-5, while the mobility bandwidth is suppressed by an additional N^-2 and scales as N^-7.

## Recommended v0.8 edits

1. Correct the fixed-rank validation wording in the theorem proof and verification appendix.
2. Correct the symbolic certificate JSON/MD and verifier gate labels to distinguish q rank sweep from the N=7 full-kernel anchor.
3. Add a corollary giving the exact large-N asymptotics above.
4. Add a Stage-3G implementation remark describing exact partition/loop dynamic programming and its 147 self-tests.
5. Add the 64-key targeted extraction formulas:

   A_N = 4 [C^dagger H_{4,N} C]_{2e_0},
   B_N = 4 [C^dagger H_{4,N} C]_{e_0+e_1}.

6. Include `SU_N_STAGE3G_WIRING_BUNDLE.zip` and `Y4_SOS_TARGETED_STAGE3G_REDUCTION_BUNDLE.zip` in the release manifest.
7. Mark the original Stage-2A and SOS bundles, v0.2 TeX, and v0.3 PDF as superseded; retain only the R2/V0.6/v0.8 release chain.
8. Add the missing symbolic-generation script, or explicitly disclose its absence in the reproducibility statement.

## Final publication status

- **Mathematical core:** publishable after the verification wording is corrected.
- **Stable-rank sign theorem:** internally exact and strongly supported, with an N=7 full-kernel anchor.
- **From-scratch symbolic provenance:** not yet complete unless the formula-generation script is added.
- **Best next manuscript version:** v0.8, not a reissue of v0.7.
