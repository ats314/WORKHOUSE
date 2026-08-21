# F002 — scalar_cluster_recovery remainder (Pass 2)

**Date:** June 12, 2026 | **Unit:** ledger #2 | **Read:** final + first contradiction audits, latest critical-path report, COLAB status sweep (21/21) , FOUND_PAPERS index, PROJECT_HISTORY session log head, gap_auditor reporter JSON. **Skim-level only:** individual arXiv summaries (categorized: wilson_flow, bakry_emery — defer to unit #25 alongside gpt_masters), PATCH file contents.

## 1. The January audit-and-patch loop — and its two surviving CRITICALs

`HAAR/analysis_reports/` documents a Jan 18–19 automated audit cycle over `Synthesis_01_Haar_Geometry_Foundation` (~30 timestamped contradiction runs interleaved with 11 PATCH files). Severity trajectory: 3 CRITICAL / 4 MAJOR / 2 MINOR (v2 start) → **2 CRITICAL / 3 MAJOR / 0 MINOR (final run, Jan 19 01:35)**. The era patched but did not fully close. The surviving CRITICALs are precise and convention-level:

1. **One-sided vs two-sided Hessian bound (SAFE chapter).** Ch. 15.2 presents ‖∇²log J‖_op ≤ 0.049 as ∇²S_H ⪰ −0.049·I — but the op-norm bound is two-sided, and near 0 Ch. 3 gives a *positive* baseline (κ_G/3); the SAFE convexity statement as written misstates the mechanism.
2. **Mode A / Mode B reference-measure mixing in the Bakry–Émery tensor.** Ric_μ := Ric_g + ∇²S is hard-coded against the Riemannian volume (Mode A), but later chapters fold S_H into the action with Lebesgue reference (Mode B) while reusing the same Ric_μ — ambient-manifold/reference-measure choice inconsistent.

**⚠ Standing cross-check item (high value):** when ledger unit #7 reviews the *current* proven chain (P04 Haar curvature, Core Curvature Theorem) and unit #10 the appendices, verify explicitly that these two issues were resolved in the lineage — the chain descends from this material, and the April CLAUDE_REVIEW may or may not have addressed them in this exact form. Recorded here so no future pass forgets.

## 2. The January critical path = today's open problems (continuity check passes)

The latest critical-path report (Jan 18) lists 5 items that map one-to-one onto the live problem list: CP1 globalization of local BE + drift → uniform PI/LSI (= ★/OP-2 complex); **CP2 quantitative exceptional-set estimate uniform in volume (= the (S) sparsity lemma — OP-1's open half, already identified as the bottleneck five months ago)**; CP3 audited Wilson-Hessian Lipschitz with explicit constants (the deterministic-lemma demand that June's M1/M2 satisfied on the comparator side by exact computation); CP4 HS/Witten covariance packaged on the horizontal bundle; CP5 the OS bridge with matched hypotheses (= OP-5/CONJ_D territory). Nothing on today's list is missing from January's, and vice versa — the program's skeleton has been stable; what changed is the *quantitative* re-basing (June) and the formal review layer (April).

## 3. COLAB corpus status sweep (21 writeups)

All self-report "✅ VERIFIED" — meaning *numerical checks*, never proofs. Caveats carried by two: `su2_algorithm_portability` (⚠ polynomial fit), `trg_methodology_demo` (⚠ physics constants unverified). Three are phenomenological side-quests outside the chain (ckm_geometric_origin, cosmic_mass_budget, geometric_mass_spectrum — galaxy/cosmology era). Chain-relevant set beyond F001's three: `continuum_limit_verification`, `free_scalar_control`, `mass_gap_scaling_toy`, `su3_convexity_landscape`, `su3_vacuum_stability`, `lattice_cohomology_t3`, `u1_2d_trg_control` — adequate at summary level; deep-read only if a specific claim needs its methodology.

## 4. Mixed-quality automated literature search

`FOUND_PAPERS.md` (Jan 18): the arXiv auto-search returned blatant irrelevancies (a *Venus exploration strategy* document; a Besov-spaces paper by an author named Haar) for the query "Stratification strategy Codim HAAR" — the retrieval layer was keyword-naive. The `extracted/` summaries themselves are topic-categorized (wilson_flow, bakry_emery) and likely sound, but **provenance of "found via gap_targeted query" items should not be treated as relevance-vetted**. Note for unit #25.

## 5. Era infrastructure snapshots

PROJECT_HISTORY/03_SESSION_LOG records the Jan 14 quality correction ("superficial extraction… user pointed out") — the audit culture predates the current review pipeline. `reports/report_the_gap_auditor.json` (Jan 23): 129 claims / 41 certificates / only 7 claims with closed_by / 33 certs mapped — the ancestor of today's certificate culture, with era-internal numbers (do not quote as current).

## Actionables
- Add the two CRITICAL convention flags to units #7/#10 scope (done — noted in ledger rows).
- No STATE.md change: nothing here alters current status; the continuity check *supports* the live problem list's completeness.
