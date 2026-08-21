# PMBSF — Projected Maxwell Birman–Schwinger Firewall (working set)

**Definition of done:** the SU(2) conditional-firewall manuscript (`../../papers/pmbsf_su2/`) is referee-ready — the LCI ⇒ TOS+J ⇒ Lemma Q reduction written in full, every assumption tagged honestly as `[open input]`, no claim beyond *conditional*, and the open analytic core (Lemma Q / source-weighted Bałaban expansion) stated explicitly as the remaining input rather than buried.

**Intake June 12, 2026 from C:\Downloads (Alex's recent-chats exports, May 22–30, 2026).** Full deposit (279 files, MD5 manifest): `E:\YANG\ORGANIZED\13_PMBSF\`. This working set: the pass-19 master, latest paper lines, and the Lemma Q complex.

## What this program is

The PMBSF program is the *analytic* attack on defect sparsity — the same factorization the June OP-1 campaign reached from the numerical side. Its own status line (pass 19, May 26): **"Conditional. NOT a Yang–Mills mass-gap proof."** Theorem stack:

    Lemma Q + source-weighted Bałaban expansion + boundary-band gate ⇒ SU(2) projected-capacity firewall closure.

**Lemma Q** = conditional rare-source factorization: every additional marked plaquette in a shaved Bałaban block core costs one factor of the global source intensity q_η, uniformly under exterior conditioning. **This is the (S) lemma of `programs/op1_defect_sparsity/PLAN_OP1_unif_closure.md` (M3), in its precise SU(2) form.** Pass 19 sharpens the attack: LCI (local cap-intersection stability for heat-bath caps) + Bałaban far-source stability ⇒ TOS+J ⇒ positive source-radius bound Z_A(ρ/q_η) ≤ e^{K|A|} ⇒ Lemma Q. Lemma Q remains open analytically.

## Key files here

| File | Role |
|---|---|
| NOTE_PMBSF_master_pass19_lci_exacthb_2026_05_26.md | Master document, pass 19 (supersedes the v2.7 one-plaquette master's Program B inventory, which stops at v16) |
| MAN_PMBSF_pass19_publication_bundle_manifest_2026_05_26.md | What the May publication bundle contains |
| PMBSF_SU2_conditional_firewall_paper_v3_4_merged / manuscript_v3_3_unified_core | Latest SU(2) paper line |
| NOTE_PMBSF_su3_su_n_wilson_merged_draft_2026-05-30.md | Latest SU(3)/SU(N) paper line (May 30 — newest dated doc) |
| Sections 4/5/6, 13/14 | Lemma Q statement; source-radius extraction; TOS+J; referee-risk ledger; remaining analytic tasks |
| NOTE_PMBSF_lci_tosj_reduction_lemmaq_2026_05_26.md | The reduction that replaced "prove Lemma Q" with the LCI route |
| Theorem FNG …Projected Capacity Firewall.md | The headline conditional theorem statement |
| NOTE_PMBSF_l64_projected_capacity_threshold_law.md | Threshold law at L=64 |
| Expanded_Derivations_PMBSF_LemmaQ_SU3 / Literature map | SU(3) derivations; literature positioning for Lemma Q |
| LemmaQ scripts ×3 + ENGINE_FLUX_lci_typicality_diagnostic.py + v17/v17b scripts + cavity CSVs | Stage-B exact heat-bath geometry diagnostics, v17 BS cumulants, η-extension |
| Mprime_to_HPM_bridge(.md/_v17b_PATCH) + extraction protocol | M′→HPM bridge line |
| PAPER_PMBSF_master_one_plaquette_bridge.pdf | The bridge document between PMBSF and the one-plaquette program |
| PLAN_PMBSF_stageb.md | Stage B plan |

## Open cross-links (recorded June 12, 2026)

1. **M3 ≡ Lemma Q** (SU(2) form): the OP-1 dossier's M3 row now points here. The June M2 exact-kernel certificates are the comparator-side counterpart of this program's "deterministic projective-capacity spine."
2. The one-plaquette master doc v2.7's Program B inventory is **stale relative to pass 19** — supersession noted, not edited into the archive doc.
3. Alex must adjudicate: is the (S) lemma to be closed in the PMBSF/Lemma-Q formulation (SU(2), heat-bath caps, Bałaban blocks) or the OP-1 comparator formulation (SU(3) Wilson, ρ-weighted kernel sums)? The two need a translation note either way.

## F037 correction to `NOTE_PMBSF_lci_tosj_reduction_lemmaq_2026_05_26.md` §§8–9 (June 12, 2026)

First agent attack on Z.A's deterministic cap-geometry core (`programs/op1_defect_sparsity/za_cap_geometry/`, finding F037). Two results bear directly on this program's files:

1. **The bare-cap curvature step (9.5) is now PROVED with an explicit constant** (c_curv = 1/2; sharp 1/(2(1−c₀²))) — but only for A=∅.
2. **The incident-subset form of (9.5) is FALSE** (sampling-verified counterexample: k=3 caps, χ₀=0.19 but true height-drop Δ_p=0.002). The §9 good event `G_LCI` (9.7), defined via `χ₀(A) = u_A·n_p − a`, does **not** control the cap ratio (8.4) for incident subsets. **Fix: redefine the good event by the true height-drop, `G_LCI' = {min_A Δ_p(A) ≥ Δ*}`, Δ_p(A) = h(A) − h(A∪{p}).**

**Actionable for `ENGINE_FLUX_lci_typicality_diagnostic.py`:** it currently reports `min_chi0 = min_A (u_A·n_p − a)`. It already computes `h(A)` (and can compute `h(A∪{p})`) in `solve_cap_intersection_max`, so it should report `min_A Δ_p(A) = h(A) − h(A∪{p})` as the LCI margin instead. The χ₀ observable overstates the good event. (The Bałaban far-source / Z.B side is unaffected by this correction.)

**F038 update (June 12, 2026): the deterministic LCI core is now COMPLETE.** The cap-ratio rate is `Δ_p(A)` for **every** incident `A≠∅` — proved (Varadhan/Laplace) and exact-quadrature-certified, prefactor bounded `M∈[−½,0]` (`za_cap_geometry/ENGINE_OP1_za_multicap_v2.py`, G-ZB1/G-ZB2). So every finite-dim step of §§6–11 is proved-or-certified, and **Z.A reduces to the single typicality statement** `G_LCI' = {min_A Δ_p(A) ≥ Δ_q + O(logκ/κ)}` P-typically. The diagnostic re-point above is now the direct route to evidence on the *entire* remaining content of Z.A — measure `min_A Δ_p(A)` on the Stage-B ensemble and test G_LCI'. Finding F038.

**F039 update (June 12, 2026): the re-point is EXECUTED and measured.** `min_A Δ_p(A)` computed on a real exact-heat-bath config (β=3.5, L=4) via `za_cap_geometry/ENGINE_OP1_za_dp_v3.py` (gates pass). **Both observables agree on whether the good event holds** (12.5%; exact, since Δ_p(A)>0 ⟺ χ₀(A)>0) **but Δ_p shows the margin is much smaller** (never >0.05 vs χ₀ >0.10; half of χ₀-good cases are Δ_p-marginal). At L=4/κ≈18 the strict G_LCI' good event is essentially empty ⟹ everything rooted ⟹ **Z.A typicality is a larger-L + rooted (Z.B) phenomenon, not L=4 pointwise; Z.B is load-bearing**. The natural next run is this same measurement at L=16 (the engine here, not the archived diagnostic, is the one to extend — it uses the hardened solver and computes Δ_p directly). Finding F039.
