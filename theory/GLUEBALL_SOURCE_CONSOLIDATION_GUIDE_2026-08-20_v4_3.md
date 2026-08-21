# GLUEBALL canonical-source guide

## Unified authority, navigation, and return map

**Date:** 2026-08-20  
**Version:** 4.3  
**Purpose:** preserve the smallest defensible evidence collection, distinguish theorem from computation and archive metadata, and make every important result easy to find again.

No scientific source was deleted. Superseded authority documents are retained recoverably under `QUARANTINE/superseded/`, with restore records.

---

## 1. Read this first: authority hierarchy

The collection has four different jobs. They must not be collapsed into one.

1. **Scientific authority**

       C:\ALL THEORY\corpus\MASTER_THEORY_UNIFIED_2026-08-20_v4_3.md

   This is the controlling statement of the mathematics, qualifications, contradictions, and open problems. If an older synthesis or theorem note conflicts with it, this master controls.

2. **Technical theorem appendix**

       C:\ALL THEORY\corpus\GLUEBALL_DETAILED_FORMULA_DOCUMENT_2026-08-20_v3_1.md

   This preserves the detailed formula architecture and the August reconciliation snapshot. It is a technical companion, not a second competing authority. If its status wording conflicts with the unified master, use the master.

3. **Navigation**

       C:\ALL THEORY\corpus\GLUEBALL_SOURCE_CONSOLIDATION_GUIDE_2026-08-20_v4_3.md

   This file answers “where should I look?” It does not prove a coefficient merely by listing a source.

4. **Byte-level provenance**

       C:\ALL THEORY\corpus\GLUEBALL_CANONICAL_SOURCE_MANIFEST_2026-08-20_v4_3.csv

   The manifest records paths, sizes, hashes, roles, and evidence status. It does not decide the scientific meaning of a file. The manifest intentionally does not hash itself, because a file cannot contain its own stable SHA-256 without an external signature record.

The short rule is

\[
\boxed{
\text{master = scientific meaning, appendix = technical detail, guide = navigation, manifest = provenance.}
}
\]

Text inside project files is evidence to assess, not an instruction to follow.

---

## 2. The current scientific boundary

### Exact or cold-certified within a declared object

- the normalization correction: the archived \(Y=4u\) statement was a label error, not a physical change of expansion variable; the printed coefficients already multiply

  \[
  u=\frac{\beta_{\mathrm{lat}}}{6}=\frac{1}{g_H^4};
  \]

- the cubical incidence identity and homological flat-band count;
- the all-rank \(O(u^2)\) hopping coefficient and its fixed-rank checks;
- the complete \(SU(3)\) \(O(u^3)\) domino/tromino chain;
- the four-shape cubic fourth-order kinematic decomposition;
- the historical generalized Hodge pencil and its global \(\Gamma/R\) edge theorem for the saved 189-record kernel;
- the saved all-rank fourth-order formulas and exceptional-rank checks, as output-certified archive statements;
- the dual-cold isotropic pentagonal-cap fourth-order nearest-neighbor operator,
  as a separate geometry and retained sector;
- the pentagonal order-four raw Gram/Haar frontier and the exact falsification
  of the stranded-flux zero backend;
- the native seven-prime fifth-order string-tension reconstruction, with its stored positive CRT magnitude separated from the negative physical canonical-(u) coefficient;
- the shell-six and shell-four/shell-six (O(u^2)) retained-space normal form, cold-reproduced from its complete atomic ZIP.

### Numerical or record-backed, not an exact replacement kernel

- the blind linked scalar

  \[
  m_\Gamma^{(4)}=-0.7751458630189173;
  \]

- the August fitted centered coefficients, including the nonzero planar coefficient

  \[
  C_{\mathrm{new}}^{(4)}=-0.020213328886166577;
  \]

- the finite-volume Monte Carlo measurements in `next14.json`;
- the pentagonal direct \(O(u^5)\) modular correction transcript, which records
  exact fractions but has no located generating source or machine-readable
  certificate and is therefore a prose-only candidate;
- the exact rational and two-modulus sixth-order contraction agreement for the stated historical branch. This is output-certified over \(205{,}699\) nonzero blocks, but both engines share the scratch topology and local tensors.

### Still open

- an exact, target-blind, unshifted physical cubic \(SU(3)\) fourth-order kernel;
- the exact physical planar coefficient \(C^{(4)}\) derived from that one kernel;
- a justified cross-kernel identification between the historical and August kernels;
- a one-shot upstream regeneration of the complete all-rank fourth-order chain;
- independent statistical reanalysis of the August Monte Carlo output from a raw ensemble/checkpoint;
- a source-complete cold regeneration of the later sixth-order scratch proof, because its separate source-only companion bundle is absent;
- a physical linked-branch interpretation of \(m_6\) or \(c_6\) after the August fourth-order adjudication;
- the complete pentagonal \(O(u^5)\) folded, linked, and rooted-cluster
  coefficient, including all 572 proper-prefix-return histories;
- a microscopic coefficient for the separately tuned equal-face-energy
  pentagonal Hodge model;
- a true interval enclosure for the OP1 Lemma-A finite-cell computation;
- the stochastic covariance, comparator calibration, and continuum steps of the adjacent OP1/PMBSF programs;
- a continuum Yang–Mills mass-gap theorem.

Four firewalls are especially important:

1. A diagonal reanchor is exact **within one kernel** because adding \(\delta G\) to a generalized pencil shifts every eigenvalue by \(\delta\). It does not prove equality of two kernels’ off-axis parts.
2. At \(\Gamma\), the historical band has directional radial second derivatives. When \(\beta\ne2\alpha\), there is no ordinary Hessian or effective-mass tensor there. At \(R\), the Hessian is genuinely isotropic.
3. Every higher-order coefficient belongs to a declared coupling coordinate and lower-order branch. The stored sixth-order contraction uses the historical fourth-order band branch; filename proximity does not convert it into the physical linked sixth-order mass.
4. In the standard isotropic pentagonal model, cap and side one-face energies
   differ. The physical cap band has ordinary \(2\tau_4\cos k\) hopping. The
   formal cap-plus-side Hodge symbol belongs to the tuned ratio
   \(w_{\mathrm{vertical}}/w_{\mathrm{horizontal}}=3/2\), and the isotropic
   microscopic coefficient is blocked from reuse there.

---

## 3. Canonical folder taxonomy

Use exactly this taxonomy when consolidating copies:

    GLUEBALL_CANONICAL_2026-08-20\
      00_README_STATUS_MANIFEST\
      01_MASTER_THEORY\
      02_NORMALIZATION\
      03_HOMOLOGY_O2_O3\
      04_HISTORICAL_SU3_O4\
      05_PHYSICAL_O4_ADJUDICATION\
      06_ALL_RANK_O4\
      07_MONTE_CARLO_BRIDGE\
      08_PENTAGONAL_SEPARATE_MODEL\
      09_PRIMARY_LITERATURE\
      10_TESTS\
      11_HIGHER_ORDERS_AND_SHELLS\
      12_ADJACENT_OP1\
      13_ADJACENT_CAPACITY_PMBSF\
      90_SUPERSEDED\
      99_QUARANTINE\

| Folder | Contents | Boundary |
|---|---|---|
| `00_README_STATUS_MANIFEST` | this guide, manifest, archive status | navigation and provenance only |
| `01_MASTER_THEORY` | unified master and technical appendix | controlling mathematical interpretation |
| `02_NORMALIZATION` | coupling erratum and audits | must travel with stale \(Y=4u\) sources |
| `03_HOMOLOGY_O2_O3` | incidence, flat band, all-rank \(O(u^2)\), \(SU(3)\) \(O(u^3)\) | exact lower-order spine |
| `04_HISTORICAL_SU3_O4` | saved 189-record kernel and fixed-kernel audits | exact for that archived kernel |
| `05_PHYSICAL_O4_ADJUDICATION` | 15-hour run, forensic notes, scalar/shape separation | mixed numerical and forensic evidence |
| `06_ALL_RANK_O4` | complete ZIP archives and saved verifiers | output-certified, not one-shot regenerated |
| `07_MONTE_CARLO_BRIDGE` | operator source, structured output, analysis note | finite-volume numerical bridge |
| `08_PENTAGONAL_SEPARATE_MODEL` | dual-cold pentagonal bundle | exact but not the cubic kernel |
| `09_PRIMARY_LITERATURE` | local primary papers and stable metadata | methods and external convention context |
| `10_TESTS` | marked-cluster engine, tests, fixtures | protocol/preflight unless physics output exists |
| `11_HIGHER_ORDERS_AND_SHELLS` | native \(\sigma_5\), historical \(O(u^5)\), shell-six, and sixth-order output bundles | preserve branch, sign, and regeneration status |
| `12_ADJACENT_OP1` | exact finite-comparator formulas, Lemma B, and Lemma-A audit | separate deterministic program; stochastic closure open |
| `13_ADJACENT_CAPACITY_PMBSF` | cap geometry, large-deviation rate, and PMBSF gate map | separate conditional program; far-source and typicality open |
| `90_SUPERSEDED` | older syntheses, partial drafts, legacy audits | useful history; never override the master |
| `99_QUARANTINE` | transcripts, target-derived branches, non-evidence | do not cite as theorem evidence |

Every copied object should retain its original absolute path, byte count, SHA-256, role, status, and bundle membership. A shorter canonical filename is acceptable only when the manifest records the mapping.

---

## 4. Canonical bundle map

### A00–A02 — controlling documents

    C:\ALL THEORY\corpus\MASTER_THEORY_UNIFIED_2026-08-20_v4_3.md
    C:\ALL THEORY\corpus\GLUEBALL_SOURCE_CONSOLIDATION_GUIDE_2026-08-20_v4_3.md
    C:\ALL THEORY\corpus\GLUEBALL_DETAILED_FORMULA_DOCUMENT_2026-08-20_v3_1.md

Keep these together. The master decides status; the appendix carries dense formulas; this guide returns the reader to the evidence.

### A09 — normalization, atomic bundle

    F:\THEORY\papers\flat_band\NORMALIZATION_ERRATUM_2026-06-14.md
    F:\THEORY\programs\one_plaquette\su3_o5_consolidated_y6\GLUEBALL_COUPLING_NORMALIZATION_AUDIT_2026-06-14.md
    F:\THEORY\programs\one_plaquette\su3_o5_consolidated_y6\sources\GLUEBALL_STRING_NORMALIZATION_AUDIT_2026-06-14.md
    F:\THEORY\ZIP ARCHIVES\GLUEBALL_STRING_NORMALIZATION_CORRECTION_V2.zip

Governing rule: never apply an extra factor \(4^r\) to the historical coefficients. The old \(Y=4u\) text was a label error.

### A10–A14 — homology and lower orders

    F:\THEORY\papers\flat_band\glueball_flat_band_paper_v1_1.tex
    F:\THEORY\papers\flat_band\glueball_flat_band_paper_v1_1.pdf
    F:\THEORY\programs\one_plaquette\cls_flat_band_certificate_v1_1.py
    F:\THEORY\programs\one_plaquette\cls_flat_band_results_v1_1.md
    F:\THEORY\programs\one_plaquette\glueball_band_certificate_v2.py
    F:\THEORY\programs\one_plaquette\glueball_band_results_v2.md
    C:\Users\Alex\Downloads\suN_closed_surface_band_stage1_certificate.py
    C:\Users\Alex\Downloads\suN_closed_surface_stage1_certificate.json
    F:\THEORY\programs\one_plaquette\su3_moments_ext.py
    F:\THEORY\programs\one_plaquette\su3_domino_d3.py
    E:\YANG\ORGANIZED\12_ONE_PLAQUETTE\domino_certificates\d3_results.json
    F:\THEORY\programs\one_plaquette\tromino_o3\tromino_contract_independent_check.py
    F:\THEORY\programs\one_plaquette\tromino_o3\tromino_candidate_closed_form_check.py
    F:\THEORY\programs\one_plaquette\master_v2_regression_certificate.py

The \(O(u^3)\) chain reproduces

\[
b_3=\frac{1975}{124848},\qquad
\operatorname{leak}_3=-\frac{12331}{249696},\qquad
d_3=-\frac{109151}{249696}.
\]

Archive note: `su3_domino_d3.py` contains a nonportable Linux output path. Preserve the archived source; fix the destination only in a dated work copy.

### A20–A23 — historical cubic \(SU(3)\) fourth order

    F:\THEORY\programs\one_plaquette\y4_o3_flatband_verification\y4_full_real_space_H4_kernel.json.gz
    F:\THEORY\programs\one_plaquette\y4_o3_flatband_verification\y4_global_band_edge_certificate.py
    F:\THEORY\programs\one_plaquette\y4_o3_flatband_verification\Y4_GLOBAL_BAND_EDGE_CERTIFICATE.md
    F:\THEORY\programs\one_plaquette\y4_o3_flatband_verification\y4_stage3j_final_verdict.json
    F:\THEORY\papers\flat_band\FOURTH_ORDER_T1PM_BAND_THEOREM_V0_8_CONSOLIDATED.md
    F:\THEORY\programs\one_plaquette\y4_o3_flatband_verification\indep_cert_check.py
    F:\THEORY\programs\one_plaquette\y4_o3_flatband_verification\y4_independent_verification.py
    F:\THEORY\programs\one_plaquette\y4_o3_flatband_verification\curvature_audit.log
    F:\THEORY\programs\one_plaquette\y4_o3_flatband_verification\REVIEW_global_band_edge_certificate.md
    F:\THEORY\programs\one_plaquette\y4_o3_flatband_verification\SUMMARY.md
    F:\THEORY\programs\one_plaquette\y4_o3_flatband_verification\THEOREM_Y4_FLAT_BAND_BREAKING_2026-06-13.md

The exact width for the supplied historical kernel is

\[
\Delta q^{(4)}=\frac{132329431693349}{275331901291200}.
\]

The final theorem note has the stale coupling label, so it must remain bundled with A09. The compressed-kernel SHA-256 in the manifest is the hash of the `.json.gz` byte object; do not confuse it with a decompressed or semantic hash.

### A30–A32 — physical fourth-order adjudication

    C:\Users\Alex\Downloads\15 hour RUN.txt
    C:\Users\Alex\Downloads\15 hour RUN. results.txt
    C:\Users\Alex\Downloads\03-unified-proposal.md
    C:\Users\Alex\Downloads\05-latest-run-forensics.md
    C:\Users\Alex\Downloads\06-pattern-2-5-runtime-forensics.md
    C:\Users\Alex\Downloads\06-physicalq-q2.md
    C:\Users\Alex\Downloads\09-dual-cold-oracle.md
    C:\Users\Alex\Downloads\Hodge_v10a25_Hamer_Gelfand_O4_A100.ipynb
    C:\Users\Alex\Downloads\Monday 531 PM.txt

The blind scalar was produced before the disputed historical target entered. The final diagonal equality was later forced with a shift of

\[
+11.17343231638178.
\]

That shift aligns an anchor; it does not reconcile the old and new off-axis coefficients. The Hamer decimal used locally is a transcription until checked against a hashed primary table.

### A40–A41 — tests, marked engine, and authority fixture

    C:\Users\Alex\Downloads\Hodge_SU3_Exact_MarkedCluster_m4_Colab.py
    C:\Users\Alex\Downloads\test_Hodge_SU3_Exact_MarkedCluster_m4_Colab.py
    C:\Users\Alex\Downloads\Hodge_Y4_Canonical_O4_Production_Colab.py
    C:\Users\Alex\Downloads\test_Hodge_Y4_Canonical_O4_Production_Colab.py
    C:\Users\Alex\Downloads\Y4_STAGEI_AUTHORITY_FIXTURE.xz.b85

The marked engine is an exact protocol design, not a completed \(m_4\) calculation. The production engine reproduces a sealed historical fixture; fixture reproduction is not independent discovery.

### A50–A53 — all-rank fourth order

Prefer the atomic ZIPs:

    F:\THEORY\ZIP ARCHIVES\Y4_SUN_ALL_N_GE_3_BAND_SHAPE_BUNDLE_2026-06-14.zip
    F:\THEORY\ZIP ARCHIVES\Y4_SUN_WALLED_BRAUER_FULL_SYMBOLIC_BUNDLE_2026-06-14_V2.zip
    F:\THEORY\ZIP ARCHIVES\Y4_SUN_SYMBOLIC_QAB_COMPACT_BUNDLE.zip

Keep the extracted certificates for browsing and fast fixed-output checks. The complete archives pass their saved verifiers, including exceptional-rank branches. The remaining provenance task is a one-shot authenticated regeneration of the full upstream word/path enumeration.

### A61 — Monte Carlo bridge

    C:\Users\Alex\Downloads\SU3_T1pm_spatial_MC_nextrun.py
    C:\Users\Alex\Downloads\next14.json
    C:\Users\Alex\Downloads\SU3_T1pm_spatial_MC_POLARIZATION_v3 (1).py
    C:\Users\Alex\Downloads\10-su3-monte-carlo.md

The structured output records \(\beta=5.8941\), \(L=14\), \(N_t=16\), and 2,000 configurations, with

\[
aM=1.6897344913\pm0.1206114757,
\qquad
a\sqrt\sigma=0.2628289891\pm0.0023244282.
\]

It is numerical evidence, not a cold ensemble certificate: no raw ensemble/block checkpoint was found, it is not source-hash bound, it contains non-RFC `NaN` values, and one carrier gate is literal in the source.

### A60 — pentagonal separate model

    C:\ALL THEORY\archive\zips\pentagonal_o4_dual_cold_verification_bundle.zip
    C:\ALL THEORY\numerics\engines\ENGINE_PENT_pentagonal_o4_minimal_representation_frontier.py
    C:\ALL THEORY\numerics\certificates\RUN_PENT_pentagonal_o4_minimal_representation_frontier_results.json
    C:\ALL THEORY\records\transcripts\pentagonal_o4_minimal_representation_frontier_results.txt
    C:\ALL THEORY\numerics\engines\ENGINE_FLUX_audit_stranded_zero_backend.py
    C:\ALL THEORY\numerics\certificates\AUDIT_FLUX_stranded_zero_backend_results.json
    C:\ALL THEORY\records\transcripts\audit_stranded_flux_zero_backend_results.txt
    C:\ALL THEORY\records\transcripts\pentagonal_prism_O5_decisive_resolvent_results.txt

The dual-cold bundle certifies

\[
h_{4,\mathrm{side}}=-\frac{2861009}{84387303000},\qquad
\tau_4=-\frac{2861009}{16877460600},
\]

and

\[
\Delta E(k)=-\frac{2861009}{8438730300}u^4\cos k,
\qquad r_{\mathrm{hop}}^{\mathrm{iso,cap}}=4.
\]

Its two microscopic backends pass 21/21 and 24/24 internal gates, both
strict contracts pass 17/17, the all-row cross-check passes 26/26, and the
isotropic open-neighborhood, periodic-operator, tuned-firewall, and frozen
audits pass 17/17, 27/27, 7/7, and 29/29. The full bundle was cold-regenerated
end to end during the v4.3 review. In the isotropic theory the physical
retained manifold is cap-only; the cap-plus-side Hodge symbol requires the
different tuned ratio

\[
w_{\mathrm{vertical}}=\frac32w_{\mathrm{horizontal}},
\]

and a fresh anisotropic microscopic backend.

The raw-frontier source/certificate/report triple records 20 canonical
order-four histories and cut-space data

\[
(\text{raw},\operatorname{rank}G,\operatorname{nullity}G)
=(4,4,0),(10,6,4),(20,6,14),
\]

plus the rank-three \(SU(3)\) \((4,1)/(1,4)\) delta–epsilon sector. The
zero-backend source/certificate/report triple gives the decisive balanced
Haar witness

\[
\operatorname{Wg}(e)=\frac18,
\qquad
\operatorname{Wg}((12))=-\frac1{24},
\qquad
\int|U_{11}|^4\,dU=\frac16,
\]

so the stranded-flux zero backend is falsified. Both diagnostic reports
carry 8/8 saved gates and neither imports \(h_4^{\mathrm{side}}\).

The order-five transcript reports the direct-sector candidate

\[
\frac{35}{384}
+\frac{235424477177}{407461473619200}
=\frac{37373840041427}{407461473619200}.
\]

Keep that transcript in tier C/prose-only status: no generating source or
machine-readable certificate for its final fractions has been located, and
the complete folded/linked assembly of 572 proper-prefix-return histories is
still open. All A60 material must remain outside the cubic \(SU(3)\) kernel
bundle. The earlier 60,144-byte import-only verification ZIP is superseded
for \(h_4^{\mathrm{side}}\) by the 111,743-byte dual-cold archive, but remains
useful audit history.


### A70–A74 — higher orders and multishell companions

    F:\THEORY\programs\one_plaquette\su3_string_tension_native_o5\README.md
    F:\THEORY\programs\one_plaquette\su3_string_tension_native_o5\ftw.py
    F:\THEORY\programs\one_plaquette\su3_string_tension_native_o5\sigma5_full_certificate.py
    F:\THEORY\programs\one_plaquette\su3_string_tension_native_o5\SIGMA5_EXACT_CERTIFICATE.json
    F:\THEORY\ZIP ARCHIVES\SU3_Y5_COMPLETE_FIFTH_ORDER_BUNDLE.zip
    F:\THEORY\ZIP ARCHIVES\SU3_O5_CONSOLIDATED_AND_Y6_PREFLIGHT_2026-06-14.zip
    F:\THEORY\ZIP ARCHIVES\SHELL6_O2_SYMMETRY_REDUCED_V2_COMPLETE_RELEASE.zip
    C:\Users\Alex\Downloads\SU3_Y6_M6_SCRATCH_PROOF_RESULTS_V1.zip

The native reconstruction stores the positive reduced magnitude

\[
\frac{137767222189182735950309}
{2009803206414863779920000},
\]

while the physical canonical-\(u\) series carries the odd-order sign

\[
\sigma_5^{\mathrm{phys}}
=
-\frac{137767222189182735950309}
{2009803206414863779920000}.
\]

The seven CRT residues round-trip exactly and satisfy the stored uniqueness bound. Full native regeneration is expensive and the per-prime staging pickles are not deposited, so retain source, audit, and certificate together.

The shell-six theorem cold-reproduces only from the complete atomic ZIP; the extracted browsing directory omits shell6_o2_analysis_v2.json. It is exact within its retained/multishell object, not a full-Hilbert-space or continuum theorem.

The later \(m_6\) ZIP records exact rational contraction plus two full-corpus modular shadows. It is the governing output record for the stated historical branch, but the missing source-only companion prevents a clean source replay. Older \(F:\THEORY\) \(m_6\) notes remain useful lineage records and are superseded on that point.

### A80–A83 — adjacent OP1 deterministic comparator

    F:\THEORY\numerics\op12_theta\m4_scaling\M4_TC_CLOSED_FORM_2026-06-12.md
    F:\THEORY\programs\op1_defect_sparsity\LEMMA_B_PROOF_2026-06-12.md
    F:\THEORY\numerics\op12_theta\m4_scaling\lemma_b_cert.py
    F:\THEORY\numerics\op12_theta\m4_scaling\lemma_b_cert.json
    F:\THEORY\programs\op1_defect_sparsity\LEMMA_A_CLOSURE_2026-06-12.md
    F:\THEORY\numerics\op12_theta\m4_scaling\lemma_a_window_cert.py
    F:\THEORY\numerics\op12_theta\m4_scaling\lemma_a_window_cert.json

The Fourier/harmonic decomposition and Lemma-B bound are strong deterministic comparator results. Lemma B gives

\[
C_\infty(x)\le 0.018664535031<\frac1{28}.
\]

Lemma A proposes

\[
\Phi_L(t)^4-L^{-4}\le
\bigl(e^{-2t}I_0(2t)\bigr)^4.
\]

The inequality is analytically proved in the large-time region \(t\ge0.4L^2\). The remaining finite cells pass with roughly \(4.5\%\)–\(5.5\%\) numerical margins, but the deposited evaluator uses ordinary high-precision arithmetic, unenclosed Bessel/quadrature evaluation, and sampled subchecks. Thus the global all-\(t\) claim and derived floors \(N_C^\ast\ge8\), \(N^\ast\ge7\) remain pending a real interval audit. This program does not prove a Yang–Mills mass gap.

### A84–A86 — adjacent cap geometry and PMBSF boundary

    F:\THEORY\programs\op1_defect_sparsity\za_cap_geometry\ZA_CAP_GEOMETRY_2026-06-12.md
    F:\THEORY\records\review\findings\F037_za_cap_geometry.md
    F:\THEORY\records\review\findings\F038_za_multicap_rate.md

The safe exact local formulas are

\[
\Delta_p=2\sin^2\delta,\qquad
\chi_0=2\sin\sigma\,\sin\delta,\qquad
\Delta_p\ge\frac{\chi_0^2}{2}.
\]

For fixed interior \(c_0\in(-1,1)\), the small-gap coefficient is \(1/[2(1-c_0^2)]\); the endpoint \(c_0=1\) is degenerate and must be treated separately. For regular, full-dimensional cap intersections, the compact-manifold large-deviation rate is

\[
\lim_{\kappa\to\infty}
-\kappa^{-1}\log\nu(C_p\mid C_A)
=
h(A)-h(A\cup\{p\}).
\]

The older universal incident-step reduction is false. Uniform finite-\(\kappa\) prefactors, stochastic typicality, and far-source decay remain open. These files belong to the separate PMBSF/capacity program and cannot close the one-plaquette glueball theorem.

---

## 5. Cold-audit ledger

| Check | Result | Meaning |
|---|---:|---|
| topology/incidence certificate | 14/14 | exact lower-order topology gates pass |
| independent Bloch/band certificate | 36/36 | independent band gates pass; use UTF-8 mode on this Windows console |
| all-rank second-order certificate | 34/34 | fixed-rank exact gates pass |
| \(SU(3)\) third-order domino chain | 251/251 | full saved contraction chain passes |
| historical fourth-order fixed kernel | PASS | exact \(\Gamma/R\) edge and width checks pass for the saved kernel |
| complete all-rank ZIP archives | PASS | saved fixed-rank and exceptional-rank checks pass |
| marked-engine self-test | 47/47 | algebra/protocol self-test only |
| marked geometry preflight | 609/609 | 93 faces and \(3\times203\) rows constructed; **zero physics contractions** |
| marked companion tests | 20/21 | one stale expected status string, not a physics discrepancy |
| pentagonal isotropic dual-cold bundle | PASS | 21/21 and 24/24 backends; both 17/17 contracts; 26/26 cross-check; full cold regeneration passes |
| pentagonal raw representation frontier | 8/8 | exact raw Gram/Haar frontier; no imported \(h_4^{\mathrm{side}}\) |
| stranded-flux zero audit | 8/8 | exact balanced-Haar witness falsifies the zero backend |
| pentagonal direct \(O(u^5)\) correction | NOT CERTIFIED | transcript/prose only; generating source and complete linked assembly absent |
| native \(\sigma_5\) residue audit | 7/7 | stored rational reproduces every prime residue and uniqueness bound |
| complete shell-six atomic ZIP | PASS | retained/multishell theorem cold-reproduces; extracted folder alone is incomplete |
| sixth-order scratch output verifier | PASS | exact rational and two modular shadows agree; source-only regeneration bundle absent |
| OP1 Lemma-B certificate | PASS | rational bound and stored gates reproduce |
| OP1 Lemma-A run | REPRODUCED, NOT INTERVAL | strong numerical margin, but no directed enclosure |

The failing companion assertion expects `PHASE1_BLOCKED_NOT_M4`; the engine now reports the more accurate `PHASE3_TRIALITY_CANDIDATE_SWEEP_READY_NOT_YET_EVALUATED`. Update the assertion only in a work copy, then rerun before the expensive sweep.

---

## 6. Superseded and quarantine policy

### `90_SUPERSEDED`

Place older syntheses, partial unified drafts, and legacy status notes here. They remain useful for derivations and history, but their scientific status language cannot override the unified master. In particular, preserve:

- `MASTER_THEORY.md` as the broad legacy synthesis;
- `MASTER_THEORY_UNIFIED_2026-08-20_v2.md` as the partial predecessor, if retained;
- the v2 consolidation guide and v2 manifest as provenance snapshots;
- the v4.2-final master, guide, and manifest as the immediate pre-pentagonal
  authority snapshot;
- the older detailed formula documents and addendum;
- the August 1 unified record, legacy derivation audits, and older all-rank prose.

### `99_QUARANTINE`

Quarantine, or clearly mark in place:

- `SOURCEOFGOD.txt`, a conversation transcript useful only for forensic leads;
- target-derived shift branches or notebooks that hard-code the disputed scalar;
- unexecuted notebooks without authenticated output;
- help-mode or preflight envelopes with no physics contractions;
- the `F:\ANTIGRAVITY` Lean mass-gap headlines as evidence for this theorem, because the fourth-order kernel is not encoded there and admitted/axiomatic boundaries remain;
- older \(SU(2)\), \(q\)-\(6j\), TRG, or susceptibility experiments when offered as direct \(SU(3)\) fourth-order evidence;
- the older 60,144-byte pentagonal import-only verification bundle when
  offered as the coefficient authority; retain it as superseded audit history;
- continuum gap manuscripts whose transfer, spectral, or regularity step is still conditional;
- any future \(M_5\)–\(M_7\) output that does not declare its coupling coordinate;
- the entire `F:\THEORY\_QUARANTINE_DELETE_ME_2026-06-14` tree for formula extraction. Checked items were duplicates, partial outputs, empty artifacts, or stale proof text; preserve a checksum ledger before any deletion because its README is incomplete.

---

## 7. Exact duplicate groups

These pairs are byte-identical. Record both paths; do not delete originals merely because a duplicate exists.

| Pair | Bytes | SHA-256 |
|---|---:|---|
| `hhc_circuit_bridge_audit.txt` / `(1)` | 1,670 | `8E2740C4CA74449E19B2E093EEAE34434836431A6949C4F38DE006AAB6DD7261` |
| `Hodge_v10a26_Factor52Complete_ExactSW_RootedOracle_A100.ipynb` / `(1)` | 398,480 | `96E3263BCA6534E6E598FEC07F2310EAF88EB48266C0B7EAE17CBEC26D0DC9CA` |
| `Hodge_v10a24c_SECTION15_REDUCED_GPU_BENCHMARK_FRESH_A100.ipynb` / `(1)` | 364,825 | `C779D4BDC9CB561912DACB0AE03DABD8F7D6CD81ABF8841767BDAE8CD961F435` |
| `Hodge_v10a7_Marked_Linked_O4_Scalar_Colab.ipynb` / `(1)` | 87,033 | `D0784F048667EE3170996B787DC911F6DCB4ED7E462096EA7659A0BEAA59EE75` |

The Downloads and E-drive copies of `d3_results.json` are also byte-identical. The E-drive copy is the archived provenance object; the Downloads copy is a cold-run convenience object.

---

## 8. Return map

| Question | First place to look |
|---|---|
| What is the strongest current statement? | unified master v4.3 in `C:\ALL THEORY\corpus` |
| Where are the dense formulas and August reconciliation? | detailed formula appendix v3.1 |
| What is the one true coupling coordinate? | A09 normalization bundle, then the master’s convention registry |
| Why does the lower-order band flatten? | A11–A14 incidence and lower-order certificates |
| What is exact at \(O(u^3)\)? | A14 domino/tromino chain |
| What is exact at historical \(O(u^4)\)? | A20–A23 saved kernel and independent audits |
| Why do the two \(\Gamma\) values coexist? | master’s fourth-order adjudication; one is a blind scalar and the other belongs to the historical kernel |
| Did the final shift prove kernel equality? | no; see A30–A32 and the master’s reanchor firewall |
| What is known for all \(N\ge3\)? | A50–A53 all-rank section and complete ZIPs |
| Is the marked exact engine finished? | no; A40 has self-test and zero-physics preflight only |
| What Monte Carlo evidence exists? | A61 source/output pair and its limitations |
| Is the pentagonal result part of the cubic theorem? | no; A60 is a separate exact isotropic cap model |
| Where is the pentagonal \(O(u^4)\) coefficient proved? | A60 111,743-byte dual-cold ZIP; use the isotropic cap theorem and tuned-Hodge firewall together |
| Why is the old zero backend invalid? | A60 frontier and stranded-flux source/certificate/report triples |
| Is the pentagonal \(O(u^5)\) direct fraction a theorem? | no; A60 records it as a tier-C prose-only candidate pending source recovery and full linked assembly |
| Where is the native fifth-order tension result? | A70 source, runner, and certificate; keep the physical odd-order sign audit attached |
| What does the sixth-order ZIP prove? | exact output agreement for the historical branch, not a source replay or physical linked-branch coefficient |
| Where is the shell-six theorem? | A70 complete atomic ZIP; the extracted directory is incomplete |
| Are the OP1 all-volume floors rigorous? | Lemma B is strong; the Lemma-A finite cells still need intervalization |
| What remains open in PMBSF? | typicality, uniform prefactors, far-source decay, and final stochastic closure |
| Does Lean verify the physical fourth-order theorem? | no |
| Is there a continuum mass-gap proof? | no |

---

## 9. Safe consolidation procedure

1. Create the folder tree without changing any original.
2. Copy the guide, manifest, unified master, and technical appendix first.
3. Copy the normalization bundle before any source carrying the stale \(Y=4u\) label.
4. Copy each certificate family as an atomic bundle: source, input, output, verifier, and status note.
5. Recompute every SHA-256 and compare it with the v4.3 manifest.
6. Put `STATUS.md` beside any engine that has only preflight output.
7. Put `SCOPE.md` beside the pentagonal and Monte Carlo bundles.
8. Keep the complete all-rank and shell-six ZIPs even when extracted browsing copies are present.
9. Record exact duplicates; postpone deletion until the frozen archive has been checked independently.
10. Keep higher-order coefficients beside an explicit branch-and-coordinate note; do not concatenate \(m_6\) onto the August linked series by filename alone.
11. Keep adjacent OP1 and PMBSF material in their own folders, with their open stochastic gates visible.
12. Freeze the completed canonical folder read-only. Perform new work in a dated workbench and promote only audited outputs.

---

## 10. Archive-level conclusion

The collection is mature enough to consolidate without erasing its scientific boundary:

\[
\boxed{
\begin{gathered}
\text{the homological and lower-order spine is exact;}\\
\text{the historical generalized Hodge pencil is exact for its saved kernel;}\\
\text{the August linked \(\Gamma\) scalar is strong numerical evidence;}\\
\text{the separate isotropic pentagonal cap hop is dual-cold exact at order four;}\\
\text{the pentagonal direct order-five correction is prose-only pending regeneration;}\\
\text{native \(\sigma_5\) and the shell-six theorem are exact in their declared objects;}\\
\text{historical-branch \(m_6\) is output-certified, not physically rebranched;}\\
\text{the physical cubic planar \(O(u^4)\) coefficient remains open.}
\end{gathered}
}
\]

That hierarchy is the archive’s central protection: it preserves the strongest results without turning a fit, a reanchor, a fixture, or a separate geometry into a theorem about the physical cubic kernel.
