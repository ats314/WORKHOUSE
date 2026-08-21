# GLUEBALL canonical-source guide

## Unified authority, navigation, and return map

**Date:** 2026-08-20  
**Version:** 3  
**Purpose:** preserve the smallest defensible evidence collection, distinguish theorem from computation and archive metadata, and make every important result easy to find again.

No original project source was moved, renamed, edited, or deleted while preparing this guide.

---

## 1. Read this first: authority hierarchy

The collection has four different jobs. They must not be collapsed into one.

1. **Scientific authority**

       C:\Users\Alex\Downloads\MASTER_THEORY_UNIFIED_2026-08-20_v3.md

   This is the controlling statement of the mathematics, qualifications, contradictions, and open problems. If an older synthesis or theorem note conflicts with it, this master controls.

2. **Technical theorem appendix**

       C:\Users\Alex\Downloads\GLUEBALL_DETAILED_FORMULA_DOCUMENT_2026-08-20_v3_1.md

   This preserves the detailed formula architecture and the August reconciliation snapshot. It is a technical companion, not a second competing authority. If its status wording conflicts with the unified master, use the master.

3. **Navigation**

       C:\Users\Alex\Downloads\GLUEBALL_SOURCE_CONSOLIDATION_GUIDE_2026-08-20_v3.md

   This file answers “where should I look?” It does not prove a coefficient merely by listing a source.

4. **Byte-level provenance**

       C:\Users\Alex\Downloads\GLUEBALL_CANONICAL_SOURCE_MANIFEST_2026-08-20_v3.csv

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
- the pentagonal-cap fourth-order result, as a separate geometry and sector.

### Numerical or record-backed, not an exact replacement kernel

- the blind linked scalar

  \[
  m_\Gamma^{(4)}=-0.7751458630189173;
  \]

- the August fitted centered coefficients, including the nonzero planar coefficient

  \[
  C_{\mathrm{new}}^{(4)}=-0.020213328886166577;
  \]

- the finite-volume Monte Carlo measurements in `CERT_O4_next14.json`.

### Still open

- an exact, target-blind, unshifted physical cubic \(SU(3)\) fourth-order kernel;
- the exact physical planar coefficient \(C^{(4)}\) derived from that one kernel;
- a justified cross-kernel identification between the historical and August kernels;
- a one-shot upstream regeneration of the complete all-rank fourth-order chain;
- independent statistical reanalysis of the August Monte Carlo output from a raw ensemble/checkpoint;
- a continuum Yang–Mills mass-gap theorem.

Two firewalls are especially important:

1. A diagonal reanchor is exact **within one kernel** because adding \(\delta G\) to a generalized pencil shifts every eigenvalue by \(\delta\). It does not prove equality of two kernels’ off-axis parts.
2. At \(\Gamma\), the historical band has directional radial second derivatives. When \(\beta\ne2\alpha\), there is no ordinary Hessian or effective-mass tensor there. At \(R\), the Hessian is genuinely isotropic.

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
| `90_SUPERSEDED` | older syntheses, partial drafts, legacy audits | useful history; never override the master |
| `99_QUARANTINE` | transcripts, target-derived branches, non-evidence | do not cite as theorem evidence |

Every copied object should retain its original absolute path, byte count, SHA-256, role, status, and bundle membership. A shorter canonical filename is acceptable only when the manifest records the mapping.

---

## 4. Canonical bundle map

### A00–A02 — controlling documents

    C:\Users\Alex\Downloads\MASTER_THEORY_UNIFIED_2026-08-20_v3.md
    C:\Users\Alex\Downloads\GLUEBALL_SOURCE_CONSOLIDATION_GUIDE_2026-08-20_v3.md
    C:\Users\Alex\Downloads\GLUEBALL_DETAILED_FORMULA_DOCUMENT_2026-08-20_v3_1.md

Keep these together. The master decides status; the appendix carries dense formulas; this guide returns the reader to the evidence.

### A09 — normalization, atomic bundle

    F:\THEORY\papers\flat_band\AUDIT_FLUX_normalization_erratum_2026-06-14.md
    F:\THEORY\programs\one_plaquette\su3_o5_consolidated_y6\AUDIT_SU3_glueball_coupling_normalization_2026-06-14.md
    F:\THEORY\programs\one_plaquette\su3_o5_consolidated_y6\sources\AUDIT_SU3_glueball_string_normalization_2026-06-14.md
    F:\THEORY\ZIP ARCHIVES\GLUEBALL_STRING_NORMALIZATION_CORRECTION_V2.zip

Governing rule: never apply an extra factor \(4^r\) to the historical coefficients. The old \(Y=4u\) text was a label error.

### A10–A14 — homology and lower orders

    F:\THEORY\papers\flat_band\PAPER_FLUX_glueball_flat_band_v1_1.tex
    F:\THEORY\papers\flat_band\PAPER_FLUX_glueball_flat_band_v1_1.pdf
    F:\THEORY\programs\one_plaquette\ENGINE_FLUX_cls_flat_band_certificate_v1_1.py
    F:\THEORY\programs\one_plaquette\NOTE_FLUX_cls_flat_band_results_v1_1.md
    F:\THEORY\programs\one_plaquette\ENGINE_FLUX_glueball_band_certificate_v2.py
    F:\THEORY\programs\one_plaquette\NOTE_FLUX_glueball_band_results_v2.md
    C:\Users\Alex\Downloads\ENGINE_SUN_closed_surface_band_stage1_certificate.py
    C:\Users\Alex\Downloads\CERT_SUN_closed_surface_stage1_certificate.json
    F:\THEORY\programs\one_plaquette\ENGINE_FLUX_su3_moments_ext.py
    F:\THEORY\programs\one_plaquette\ENGINE_FLUX_su3_domino_d3.py
    E:\YANG\ORGANIZED\12_ONE_PLAQUETTE\domino_certificates\RUN_TROM_d3_results.json
    F:\THEORY\programs\one_plaquette\tromino_o3\ENGINE_TROM_tromino_contract_independent_check.py
    F:\THEORY\programs\one_plaquette\tromino_o3\ENGINE_TROM_tromino_candidate_closed_form_check.py
    F:\THEORY\programs\one_plaquette\ENGINE_FLUX_master_v2_regression_certificate.py

The \(O(u^3)\) chain reproduces

\[
b_3=\frac{1975}{124848},\qquad
\operatorname{leak}_3=-\frac{12331}{249696},\qquad
d_3=-\frac{109151}{249696}.
\]

Archive note: `ENGINE_FLUX_su3_domino_d3.py` contains a nonportable Linux output path. Preserve the archived source; fix the destination only in a dated work copy.

### A20–A23 — historical cubic \(SU(3)\) fourth order

    F:\THEORY\programs\one_plaquette\y4_o3_flatband_verification\DATA_Y4_full_real_space_h4_kernel.json.gz
    F:\THEORY\programs\one_plaquette\y4_o3_flatband_verification\ENGINE_Y4_global_band_edge_certificate.py
    F:\THEORY\programs\one_plaquette\y4_o3_flatband_verification\CERT_Y4_global_band_edge_certificate.md
    F:\THEORY\programs\one_plaquette\y4_o3_flatband_verification\CERT_Y4_stage3j_verdict.json
    F:\THEORY\papers\flat_band\THM_Y5_fourth_order_t1pm_band_theorem_v0_8.md
    F:\THEORY\programs\one_plaquette\y4_o3_flatband_verification\ENGINE_Y4_indep_cert_check.py
    F:\THEORY\programs\one_plaquette\y4_o3_flatband_verification\ENGINE_Y4_independent_verification.py
    F:\THEORY\programs\one_plaquette\y4_o3_flatband_verification\AUDIT_Y4_curvature.log
    F:\THEORY\programs\one_plaquette\y4_o3_flatband_verification\AUDIT_Y4_review_global_band_edge_certificate.md
    F:\THEORY\programs\one_plaquette\y4_o3_flatband_verification\NOTE_Y4_summary.md
    F:\THEORY\programs\one_plaquette\y4_o3_flatband_verification\THM_Y4_theorem_flat_band_breaking_2026-06-13.md

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
    C:\Users\Alex\Downloads\NB_O4_hodge_v10a25_hamer_gelfand_a100.ipynb
    C:\Users\Alex\Downloads\Monday 531 PM.txt

The blind scalar was produced before the disputed historical target entered. The final diagonal equality was later forced with a shift of

\[
+11.17343231638178.
\]

That shift aligns an anchor; it does not reconcile the old and new off-axis coefficients. The Hamer decimal used locally is a transcription until checked against a hashed primary table.

### A40–A41 — tests, marked engine, and authority fixture

    C:\Users\Alex\Downloads\DATA_SU3_Exact_MarkedCluster_m4_Colab.py
    C:\Users\Alex\Downloads\ENGINE_O4_test_hodge_su3_exact_markedcluster_m4_colab.py
    C:\Users\Alex\Downloads\ENGINE_Y4_hodge_canonical_o4_production_colab.py
    C:\Users\Alex\Downloads\test_ENGINE_Y4_hodge_canonical_o4_production_colab.py
    C:\Users\Alex\Downloads\DATA_Y4_stagei_authority_fixture.xz.b85

The marked engine is an exact protocol design, not a completed \(m_4\) calculation. The production engine reproduces a sealed historical fixture; fixture reproduction is not independent discovery.

### A50–A53 — all-rank fourth order

Prefer the atomic ZIPs:

    F:\THEORY\ZIP ARCHIVES\Y4_SUN_ALL_N_GE_3_BAND_SHAPE_BUNDLE_2026-06-14.zip
    F:\THEORY\ZIP ARCHIVES\Y4_SUN_WALLED_BRAUER_FULL_SYMBOLIC_BUNDLE_2026-06-14.zip
    F:\THEORY\ZIP ARCHIVES\Y4_SUN_SYMBOLIC_QAB_COMPACT_BUNDLE.zip

Keep the extracted certificates for browsing and fast fixed-output checks. The complete archives pass their saved verifiers, including exceptional-rank branches. The remaining provenance task is a one-shot authenticated regeneration of the full upstream word/path enumeration.

### A61 — Monte Carlo bridge

    C:\Users\Alex\Downloads\ENGINE_MC_su3_t1pm_spatial_nextrun.py
    C:\Users\Alex\Downloads\CERT_O4_next14.json
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

    C:\Users\Alex\Downloads\pentagonal_o4_dual_cold_verification_bundle.zip

The dual-cold bundle certifies

\[
h_{4,\mathrm{side}}=-\frac{2861009}{84387303000},\qquad
\tau_4=-\frac{2861009}{16877460600},
\]

and

\[
\Delta E(k)=-\frac{2861009}{8438730300}u^4\cos k,
\qquad r_{\mathrm{hop}}=4.
\]

This result must remain outside the cubic \(SU(3)\) kernel bundle.

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

The failing companion assertion expects `PHASE1_BLOCKED_NOT_M4`; the engine now reports the more accurate `PHASE3_TRIALITY_CANDIDATE_SWEEP_READY_NOT_YET_EVALUATED`. Update the assertion only in a work copy, then rerun before the expensive sweep.

---

## 6. Superseded and quarantine policy

### `90_SUPERSEDED`

Place older syntheses, partial unified drafts, and legacy status notes here. They remain useful for derivations and history, but their scientific status language cannot override the unified master. In particular, preserve:

- `MASTER_THEORY.md` as the broad legacy synthesis;
- `MASTER_THEORY_UNIFIED_2026-08-20_v2.md` as the partial predecessor, if retained;
- the v2 consolidation guide and v2 manifest as provenance snapshots;
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
- continuum gap manuscripts whose transfer, spectral, or regularity step is still conditional;
- any future \(M_5\)–\(M_7\) output that does not declare its coupling coordinate.

---

## 7. Exact duplicate groups

These pairs are byte-identical. Record both paths; do not delete originals merely because a duplicate exists.

| Pair | Bytes | SHA-256 |
|---|---:|---|
| `hhc_circuit_bridge_audit.txt` / `(1)` | 1,670 | `8E2740C4CA74449E19B2E093EEAE34434836431A6949C4F38DE006AAB6DD7261` |
| `NB_O4_hodge_v10a26_factor52complete_exactsw_rootedoracle_a100.ipynb` / `(1)` | 398,480 | `96E3263BCA6534E6E598FEC07F2310EAF88EB48266C0B7EAE17CBEC26D0DC9CA` |
| `NB_O4_hodge_v10a24c_section15_reduced_gpu_benchmark_fresh.ipynb` / `(1)` | 364,825 | `C779D4BDC9CB561912DACB0AE03DABD8F7D6CD81ABF8841767BDAE8CD961F435` |
| `NB_O4_hodge_v10a7_marked_linked_scalar_colab.ipynb` / `(1)` | 87,033 | `D0784F048667EE3170996B787DC911F6DCB4ED7E462096EA7659A0BEAA59EE75` |

The Downloads and E-drive copies of `RUN_TROM_d3_results.json` are also byte-identical. The E-drive copy is the archived provenance object; the Downloads copy is a cold-run convenience object.

---

## 8. Return map

| Question | First place to look |
|---|---|
| What is the strongest current statement? | unified master v3 |
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
| Is the pentagonal result part of the cubic theorem? | no; A60 is a separate exact model |
| Does Lean verify the physical fourth-order theorem? | no |
| Is there a continuum mass-gap proof? | no |

---

## 9. Safe consolidation procedure

1. Create the folder tree without changing any original.
2. Copy the guide, manifest, unified master, and technical appendix first.
3. Copy the normalization bundle before any source carrying the stale \(Y=4u\) label.
4. Copy each certificate family as an atomic bundle: source, input, output, verifier, and status note.
5. Recompute every SHA-256 and compare it with the v3 manifest.
6. Put `STATUS.md` beside any engine that has only preflight output.
7. Put `SCOPE.md` beside the pentagonal and Monte Carlo bundles.
8. Keep the complete all-rank ZIPs even when extracted browsing copies are present.
9. Record exact duplicates; postpone deletion until the frozen archive has been checked independently.
10. Freeze the completed canonical folder read-only. Perform new work in a dated workbench and promote only audited outputs.

---

## 10. Archive-level conclusion

The collection is mature enough to consolidate without erasing its scientific boundary:

\[
\boxed{
\begin{gathered}
\text{the homological and lower-order spine is exact;}\\
\text{the historical generalized Hodge pencil is exact for its saved kernel;}\\
\text{the August linked \(\Gamma\) scalar is strong numerical evidence;}\\
\text{the physical cubic planar \(O(u^4)\) coefficient remains open.}
\end{gathered}
}
\]

That hierarchy is the archive’s central protection: it preserves the strongest results without turning a fit, a reanchor, a fixture, or a separate geometry into a theorem about the physical cubic kernel.
