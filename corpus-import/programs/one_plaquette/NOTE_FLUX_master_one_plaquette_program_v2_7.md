# MASTER DOCUMENT — Wilson One-Plaquette Spectral Program

**Consolidated record: paper claims, project-file verification map, corrected support derivations, and audit status**

Version 2.7 — June 11, 2026 (theory-paper draft)
Compiled against: manuscript *"Two-Sided Spectral Control of Wilson One-Plaquette Class Gaps and an Exactly Verified Strong-Coupling Bridge to the SU(3) Glueball Channels"* (draft of June 11, 2026); the nine project notebooks; the external support-derivations note ("Appendix C package"); and the June 11 in-project band-program certificates (§8): ENGINE_FLUX_glueball_band_certificate.py (29 gates), ENGINE_TROM_tromino_contract_independent_check.py (16), ENGINE_TROM_tromino_candidate_closed_form_check.py, ENGINE_FLUX_su3_moments_ext.py (27), ENGINE_FLUX_su3_domino_d3.py (251), RUN_TROM_d3_results.json, CERT_FLUX_d3_certificate_results.md. Version 2.1 additionally compiles against the June 11 store-audit pass (run logs: ENGINE_SUN_codd_local_gap_exact.py, c2_certificate.py, su3_exact_c2.py, gue_shell_calculus_verifier.py), the deposited certificate notebook SU3_d3_corrected_full_notebook.ipynb (kernel-executed copy), and the document-level regression ENGINE_FLUX_master_v2_regression_certificate.py (40 gates). Version 2.2 additionally compiles against the June 11 deposit-audit run logs (ENGINE_FLUX_glueball_band_certificate.py 29/29; ENGINE_TROM_tromino_contract_independent_check.py 19/19; ENGINE_TROM_tromino_candidate_closed_form_check.py; hash comparisons of all deposited copies), the two store editions of the manuscript PDF, and the delivered corrected band edition (ENGINE_FLUX_glueball_band_certificate_v2.py 36/36; NOTE_FLUX_glueball_band_results_v2.md). Version 2.3 additionally compiles against the N = 7 discrimination pass: the instrumented store-engine run (c2_certificate.py driver, exact q1 printouts) and the delivered independent certificate n7_c1_discrimination_certificate.py (18 gates). Version 2.4 additionally compiles against the §6.14 residual-rank pass: c2_residual_ranks_certificate.py (route B extended to third order, 16 gates) and c2_residual_ranks_routeC_storefix.py (the store cut–join engine under an exact rank filter, 13 gates). Version 2.5 additionally compiles against the delivered manuscript patch PAPER_FLUX_manuscript_section6_patch.tex/.pdf (seven paste-ready blocks; constants whitelist-verified against the certificate chain; assembly identities re-checked; compiles standalone). Version 2.6 additionally compiles against the audited CLS delivery: ENGINE_FLUX_cls_flat_band_certificate.py (uploaded, 13/13) and its post-audit v1.1 (14/14), RUN_FLUX_cls_flat_band_results.md v1.1, the exact L = 3 torus completeness computation, and the characteristic-polynomial reconciliation of the two Bloch conventions. Version 2.7 additionally compiles against the standalone theory-paper draft glueball_flat_band_paper_v0_1.tex/.pdf (10 pp.; constants whitelist-verified; fifteen assembly identities re-checked).

**Version 2.7 changes.** Standalone theory-paper draft delivered: "An exactly flat T₁⁺⁻ glueball band in strongly coupled SU(3) lattice gauge theory: Gauss-law protection, exact constants through third order, and a pre-registered fourth-order criterion" (glueball_flat_band_paper_v0_1.tex, compiled .pdf, 10 pp.). Contents: results (A)–(E) stated in the introduction; setting and the y = 2β/3 conventions; the within-plaquette towers and the bridge; the second-order leakage section with the channel-sum lemma, the vacuum-route lemma, the corrected two-sector theorem, and the domino adjudication as a remark; the band section with the incidence-factorization/Gauss-law theorem (proof included), the flat-band theorem, the CLS/completeness theorem carrying the exact L³+2 decomposition, the C-even band theorem, and the corrected immobility remark including the det N versus det B̃ ≡ 0 asymmetry; the third-order section (bare-link lemma, rigid flat band, C-even cubics, the leakₙᵉ = Tₙᵉ identity, the derived E⁺⁺ cubic 52163/260100 and curvature correction 6335/187272 flagged as following from the certified band form); the robustness theorem, sharpness theorem, pre-registered O(y⁴) criterion, and the all-orders conjecture stated without commitment; a numerical table (all decimals machine-checked); discussion covering the CLS condensed-matter connection, the quantum-number ordering 0⁺⁺ < 2⁺⁺ < 1⁺⁻ with explicit scope discipline (no continuum claim), and quantum-simulation benchmarks including the domino levels; outlook naming d-dimensional universality and two-flux interactions as open; a verification-chain appendix and a domino-benchmark appendix. Quality controls: every fraction extracted and checked against the certified whitelist (the only extras are the channel-split values and the historical 5/481, both intentional), all table decimals verified exactly, fifteen assembly identities re-checked, compiles standalone. Bibliography restricted to high-confidence classics with an explicit verify-before-submission note; author field is a placeholder. The companion-manuscript correction is stated transparently in the abstract and adjudicated in the text by the companion's own domino data. Nothing else is altered from Version 2.6.

**Version 2.6 changes.** A delivered CLS/Gauss-law certificate for the C-odd flat band was audited and integrated as new §8.6, with §6.12 re-cut around its O(y⁴) criterion. As uploaded it passed 13/13; the audit found and fixed (v1.1, 14/14): an operator-precedence slip in G10 that left the twelve-edge count ungated (substance verified externally, then gated), and an overclaim in the completeness statement — cube translates span the flat band at every k ≠ 0 but not the k = 0 fiber; the exact decomposition, now gated on the L = 3 torus (G09b), is L³+2 = (cube states, rank L³−1 with the single relation Σψ = 0) ⊕ (three rest states, Ñ(0) = −4I). That decomposition also corrects the attribution parenthetical of ENGINE_FLUX_glueball_band_certificate.py's multiplicity gate (count right, split wrong; §8.1 erratum), and a companion-note claim that the C-even sector lacks an analogous factorization was corrected (it has one, gated; the asymmetry is det N = −2v₁v₂v₃ vanishing only on zone faces versus det Ñ ≡ 0). Novelty split recorded honestly: the factorization, cube 2-chain, and L³+2 count were already gated in ENGINE_FLUX_glueball_band_certificate.py; the new theorem content is the Gauss-law reading (flat band = ker B†, zero net signed link amplitude), the exact completeness decomposition, and the robustness criterion — any link-mediated correction B M B† leaves the band exactly flat at every order, subsuming O(y²), structurally explaining O(y³), and reducing O(y⁴) flatness to the binary criterion u†H₄P_⊥ ≡ 0, with the minimal corner-sharing symbol provably failing it (geometry alone cannot protect the band once trominoes activate). The two files' Bloch conventions were verified characteristic-polynomial-equivalent. The manuscript patch's Theorem 6.3′ gains the decomposition sentence (recompiled). Nothing else is altered from Version 2.5.

**Version 2.5 changes.** §§6.9–6.10 move to DRAFTED: a paste-ready LaTeX patch for manuscript §6 is delivered (PAPER_FLUX_manuscript_section6_patch.tex, with compiled .pdf for proofreading), written against the manuscript's own notation and equation numbering as extracted from the store PDFs, using primed numbering (Lemma 6.1′, Theorem 6.3′, 6.3′′) to avoid cascading renumbers into §7's references. Seven blocks: (1) Lemma 6.1′, the vacuum-mediated route, with proof and the §7 adjudication; (2) corrected Theorem 6.2 — self-energy and channel split unchanged, hopping t₊ = −11/306 via the lemma, L(d) = 4(2d−3)(−11/153), eq. (22) → −217/1020; (3) Theorem 6.3′ — the exact O(y²) band structure solving Theorem 6.3's open signed-band problem (incidence factorizations, det Ñ ≡ 0, flat band 11/306, cube 2-chains with L³+2 multiplicity, corrected C-even band with curvature 22/459, bandwidth 88/153, E⁺⁺ = 223/1020, A₁⁺⁺ ⊕ E⁺⁺ / T₁⁺⁻ content); (4) Theorem 6.3′′ — the O(y³) extension (tromino vanishing, rigid flat band with d₃ = −109151/249696, m₊(0) cubic −54049/520200); (5) corrected Remark 6.4 (ratio 5/22, manifold-width 15/88, exact-flatness headline); (6) global relabeling and search-and-replace instructions including the abstract, with §7 explicitly untouched plus one adjudication sentence; (7) Appendix A certificate additions. Every constant in the patch was machine-checked against the certified whitelist and the twelve assembly identities re-verified before delivery. Closure of §§6.9–6.10 requires folding the patch into the manuscript source TeX, which is not in the store; nothing else is altered from Version 2.4.

**Version 2.4 changes.** §6.14 is closed: the residual c2 instances are decided in favor of the Theorem 2.2 closed forms by two independent exact routes — route B, the explicit-engine certificate extended to third-order Rayleigh–Schrödinger (loop-equation moment recursion reaching degree 18, cross-gated against the pairing engine and against the exact Pochhammer identity E[p2^k] = ∏(α+i) at degrees 16–18; C-odd pipeline added; 16 gates), and route C, the store's cut–join engine with one minimal retrofit (each monomial basis filtered to a maximal independent subset by an exact Schur test before any Gram is built; the full-rank driver re-runs unchanged; 13 gates). The decided values: c2+(4) = −55053/262144, c2+(5) = −60219/102400, c2−(4) = −72099/262144, c2−(5) = −261/320, c2−(6) = −3356317/1769472 — all equal to the closed forms, with routes B and C in exact agreement and every previously known value (N = 3 both sectors; even 6–12; odd 7–13) reproduced as anchors first. Theorem 2.2's c2 table is now certified at every fixed rank: even N = 3–12, odd N = 3–13. An auxiliary closed form was derived and gated en route: q_H2(N) = (N⁴−3N²+3)/(192N²) (= q1 − q_res). The §2 c2 row, the §2 summary, §6.14, and Appendix B are updated; nothing else is altered from Version 2.3.

**Version 2.3 changes.** §6.2 is closed: the N = 7 discrimination is decided, q1(7) = −13271/50176 exactly, by two independent exact routes — route A, the store's cut–join engine (c2_certificate.py, instrumented to print exact q1: q1(6, 7, 8) = −6953/36864, −13271/50176, −23081/65536), and route B, a delivered from-scratch certificate (n7_c1_discrimination_certificate.py: explicit-pairing projected-propagator Wick cross-gated against a trace-split full-GUE reduction, moments as exact Laurent polynomials in N, exact Gram–Schmidt shell basis with the rank-reduced cases handled, Parseval-closure completeness gates, the GR1 cell-12 ledger split reproduced at N = 3, 18 gates). The cubic-interpolation foil −13127/50176 is eliminated (separation 9/3136 in q units, ≈1.07×10⁻² in c1 units). Bonus beyond the ask: route B proves the Theorem 2.3 c1+ closed form **identically in N** at generic rank and exactly at every N = 3–12 — exceeding ff_gap_rational.py's claimed 3 ≤ N ≤ 10 certification, whose c1 burden is hereby discharged. The §2 c1+(N) rows, §6.1's residual-burden list, the §2 summary, and Appendix B are updated; nothing else is altered from Version 2.2.

**Version 2.2 changes.** The §6.13 deposit landed and is verified: every deposited copy hash-matches its verified counterpart (sole exception: the standalone ENGINE_FLUX_su3_domino_d3.py differs from the notebook-embedded copy only in its JSON write path — the authoring absolute path /home/claude/review/; the notebook copy is canonical), and the band/tromino certificates run clean from the store — ENGINE_FLUX_glueball_band_certificate.py 29/29, ENGINE_TROM_tromino_contract_independent_check.py 19/19 (the deposited edition carries three more gates than the 16 recorded at v2.0), ENGINE_TROM_tromino_candidate_closed_form_check.py (symbolic identity + 40-point battery). Deposited §8 total: 326 gates. §6.11 is closed by a delivered corrected edition: ENGINE_FLUX_glueball_band_certificate_v2.py (36 gates: §8.2 hop throughout, as-written −9397/1020 retained as a provenance gate, six-field cross-check against RUN_TROM_d3_results.json) and NOTE_FLUX_glueball_band_results_v2.md. The §8.2 corrected-constants block gains two ratio lines: the per-bond ratio |t−|/|t+| = 5/22 supersedes Remark 6.4's 5/481 ≈ 1/96 (immobility survives via the exact flat band, not the ratio), and the manifold-width ratio becomes 15/88. §6.4 resolves at transcription level: b8 and b10 extract cleanly and identically from both store PDF editions, with magnitude and seam-claim consistency checks passing; analytic re-derivation of b7–b10 remains the residual. §§1.3, 6.4, 6.11, 6.13, 8 and the inventories are updated accordingly; nothing else is altered from Version 2.1.

**Version 2.1 changes.** The audit universe is split into three tiers — *store* (the persistent project file store), *delivered* (produced and verified June 11, awaiting deposit), and *session-only* — and §0/§2 statuses now name the tier. Five verification-map rows upgrade against store certificates run-verified during this pass: the entire charge-odd weak sector through c1 (ENGINE_SUN_codd_local_gap_exact.py, exact Wick, closed forms verified N = 3–12; §6.5 closed); c2±(N) (c2_certificate.py: even N = 6–12, odd N = 7–13; su3_exact_c2.py: both SU(3) instances; §6.3 closed as a requirement); c0+(N) together with Proposition 3.1's α_N and γ_N (gue_shell_calculus_verifier.py, exact N = 3–12, SU(3) anchor ρ₃ = 0.5501615335… reconciling GR1/GR2's recorded ρ values). The §8 core is packaged and store-ready: SU3_d3_corrected_full_notebook.ipynb writes and runs ENGINE_FLUX_su3_moments_ext.py + ENGINE_FLUX_su3_domino_d3.py (27 + 251 gates; kernel-executed end-to-end; RUN_TROM_d3_results.json byte-reproducible, sha256 d2d653b4…); the band-flatness and tromino certificates remain session-only (§6.13). §3 gains 3.14 (c3+(N) specializes at N = 3 to Theorem 2.1's c3) and 3.15 (first-principles derivation of the C-even curvature factor 4/3, hence 22/459). §6 is re-cut: 6.3/6.5 closed, 6.13–6.14 added, 6.2 gains a unit clarification, 6.8 adopts the 40-gate document regression. Nothing in §§1, 4, 5, 7 is altered.

**Version 2.0 changes.** New §8 records the strong-coupling band program completed *inside* the project on June 11: (i) the exact O(y²) C-odd flat-band theorem; (ii) a machine-certified **correction to manuscript Theorem 6.2** — the C-even hopping omits a vacuum-mediated route, so t₊ = −11/306, not −481/612, adjudicated by the manuscript's own §7 domino data; (iii) the O(y³) tromino-vanishing theorem; (iv) the exact third-order flat-band constant d₃ = −109151/249696 and the C-even O(y³) extension. §§1.5–1.6, 2, 3.3–3.4, C.4 and 6 carry correction flags and status upgrades; nothing else is altered from Version 1.0.

---

## 0. Purpose and document inventory

This document is the single point of reference for the one-plaquette program. It records (i) every quantitative claim of the manuscript, (ii) exactly which claims are independently supported — by the notebook corpus, the project file store, or delivered artifacts — and at what level (exact / numeric / preview / external / absent), (iii) the internal consistency checks performed during compilation, (iv) a corrected, self-contained version of the proposed support appendix, (v) the status of the logically separate defect (PMBSF) program, and (vi) the open items required to complete the audit chain. Nothing here weakens or extends the manuscript's claims; the manuscript's own scope discipline (strong coupling only; no continuum or Yang–Mills mass-gap claim) is adopted throughout. Version 2.1 distinguishes the *project file store* (the persistent corpus accompanying this document) from *session artifacts*; every status names its tier, and presence in the store confers status only when paired with a June 11 run log.

**Artifact inventory.**

| Artifact | Contents | Status in this project |
|---|---|---|
| Manuscript (PDF) | Theorems 2.1–6.3, domino verification (§7), Monte Carlo context (§8), Appendices A–B | **In store** (two editions, 11- and 12-page; Appendix B b-block extracts cleanly from both — §6.4) |
| GOODRESULTS1–4.ipynb | SU(3) weak-coupling c0/c1 program (symbolic + numeric), SU(2) hard-edge diagnostics | Present |
| GOODRESULTS5.ipynb | SU(4)/SU(N) Peter–Weyl gap scans; PMBSF Green-kernel and capacity-envelope diagnostics | Present |
| Untitled206.ipynb | Weyl-triangle solvers, character-basis confirmations, exact rational c1(N) engine, symbolic general-N machinery | Present |
| Untitled185, Untitled193, v16_MATRIX_PASS.ipynb | PMBSF defect program (firewall tests, spike/trace audits, Wilson-vs-random transfer) | Present |
| Appendix A certificate scripts (ff_gap_rational.py, sun_gap_free_fermion_certificate_c3.py, su3_c4_exact_certificate.py, gue_shell_calculus_verifier.py, r_moment_ratio_measurement.py, domino_ed_certificate.py, glueball_v4_reanalysis_fixedvec.py, glueball_v4_robustness.py) | The manuscript's verification chain for §§2–8 | Seven of eight **absent from store**; gue_shell_calculus_verifier.py **in store, run-verified June 11** (see §6.1, Appendix B) |
| Support-derivations note | Proposed "Appendix C" geometry package citing Appendix D/K/L, Core-3/Core-10, Synthesis 01/08 | Reviewed in §7; cited corpus **not in project** |
| ENGINE_FLUX_glueball_band_certificate.py + glueball_band_results.md | O(y²) lattice band theorem: exact flat C-odd band, C-even band structure, quantum numbers (29 gates) | **In store, run-verified June 11** (29/29). C-even A₁⁺⁺ numbers as-written, superseded by §8.2; corrected edition delivered: ENGINE_FLUX_glueball_band_certificate_v2.py + NOTE_FLUX_glueball_band_results_v2.md (36/36; §6.11) |
| ENGINE_TROM_tromino_contract_independent_check.py | Independent verification of the O(y³) tromino contract (19 gates in the deposited edition; 16 at v2.0 writing) | **In store, run-verified June 11** (19/19); needs ENGINE_FLUX_su3_haar_tromino_primitives.py/.json colocated and reads CERT_TROM_tromino_o3_su3_weight_cards.json from the authoring path /home/claude/review/ (path fix recommended) |
| ENGINE_TROM_tromino_candidate_closed_form_check.py | Closed-form lift diagnostic for candidate tromino weights; default weights (0,0,0) | **In store, run-verified June 11** (symbolic identity gate + 40-point battery; α extrema 8/3 on BZ axes, 8/27 at R) |
| ENGINE_FLUX_su3_moments_ext.py | Extended exact SU(3) Haar moment engine: U(3) Weingarten p = q ≤ 3, generic charge-±3 ε-projector blocks, independent Weyl-torus oracle (27 gates) | **In store** (notebook-embedded and standalone copies, hash-identical); kernel-executed June 11, 27/27 |
| ENGINE_FLUX_su3_domino_d3.py + RUN_TROM_d3_results.json + CERT_FLUX_d3_certificate_results.md | Abstract-domino word calculus, des Cloizeaux to O(y³): d₃ extraction, Theorem 6.2 correction, C-even O(y³) (251 gates) | **In store** (notebook-embedded copy canonical; the standalone deposit differs only in its JSON write path, the authoring /home/claude/review/); RUN_TROM_d3_results.json **in store** (two identical copies; sha256 d2d653b4…); CERT_FLUX_d3_certificate_results.md **in store** |
| SU3_d3_corrected_full_notebook.ipynb (+ _EXECUTED copy) | Self-contained packaging of ENGINE_FLUX_su3_moments_ext.py + ENGINE_FLUX_su3_domino_d3.py; writes RUN_TROM_d3_results.json locally | **In store** (both copies hash-match the verified deliverables); 278 gates embedded |
| ENGINE_FLUX_master_v2_regression_certificate.py | 40-gate document-level regression: §3 arithmetic incl. 3.14–3.15, §§6–8 constant web | **In store** (hash-matches the delivered copy); 40/40 |
| Store certificate corpus (charge-odd, c2, GUE) | ENGINE_SUN_codd_local_gap_exact.py, su3_odd_gap.py, SU_N_C_odd_appendix.tex, C-odd Finite-Wick docx, c2_certificate.py, su3_exact_c2.py, gue_shell_calculus_verifier.py (+ module tex/pdf) | **In store**; run-verified June 11 where noted (Appendix B) |

The notebooks divide into two logically independent programs, mirroring the manuscript's own firewall (manuscript §10):

* **Program A — one-plaquette spectral program** (the manuscript's subject): GOODRESULTS1–4, GOODRESULTS5 cells 5–7, Untitled206.
* **Program B — PMBSF / Wilson-defect geometry** (deferred to a separate manuscript): Untitled185, Untitled193, v16_MATRIX_PASS, GOODRESULTS5 cells 0–4.

---

## 1. Claims inventory of the manuscript

All constants below are transcribed from the manuscript and are the audit targets for §2.

### 1.1 Weak coupling (manuscript §2)

**Theorem 2.1 (SU(3), six exact coefficients).** Charge-even:

    Δ+(β) = √(2β/3) − 5/16 − (311√6/9216) β^{−1/2} − (5665/110592) β^{−1}
            − (8470769√6/509607936) β^{−3/2} − (56673445/1528823808) β^{−2} + O(β^{−5/2})

Charge-odd:

    Δ−(β) = √(3β/2) − 3/8 − (551√6/13824) β^{−1/2} − (53/864) β^{−1} + O(β^{−3/2}),
    c4− = −290599777/6115295232.

**Theorem 2.2 (general N).** Parity–rationality (even-j coefficients in Q, odd-j in √(2N)·Q) and closed forms:

    c0+(N) = −(2N² − 3)/(16N)
    c2+(N) = −(60N⁶ − 401N⁴ + 1522N² − 2297)/(49152 N²)
    c2−(N) = −(95N⁶ − 981N⁴ + 5853N² − 15335)/(49152 N²)
    c3+(N) = −√(2N)(2970N⁸ − 27878N⁶ + 166512N⁴ − 546024N² + 734405)/(2²¹·3²·N³)

**Theorem 2.3 (fixed-rank three-term laws).**

    Δ+(β) = √(2β/N) − (2N²−3)/(16N) − √2(6N⁴−24N²+41)/(1024 N^{3/2}) β^{−1/2} + O(β^{−1})
    Δ−(β) = √(9β/2N) − 3(N²−3)/(16N) − √2(14N⁴−97N²+290)/(1536 N^{3/2}) β^{−1/2} + O(β^{−1})

**Remark 2.4.** Fixed-rank only: the hierarchy is ordered for β ≫ N³; no large-N reading.

**Remark 2.5.** The irreducibly angular (rank-two) contribution √6/576 at order β^{−1/2}, missed by any radial reduction; confirmed numerically at ≈ 8000× the fit residual.

### 1.2 GUE structure and the moment-ratio observable (manuscript §3)

**Proposition 3.1.** Traceless-GUE identification: radial weight u^{αN} e^{−u} with αN = (N²−3)/2; universal first perturbation H1 = −p4/48; projection constant γN = (2N²−3)/(N(N²+1)).

**Theorem 3.2.** R = ⟨p3²⟩/⟨p2³⟩ with

    R0(N) = 3(N²−4)/(N(N²+1)(N²+3)),   r1/R0 = N²(N²−9)/(8(N²+1)),
    R_SU(3)(β) = (1/24)(1 − (7/80)β^{−2} + O(β^{−3})),   SU(4) slope r1/R0 = 14/17.

Monte Carlo confirmation of R_SU(3) = 1/24 at the half-percent level (β = 5.8–160).

### 1.3 Strong coupling (manuscript §4)

**Theorem 4.1 (towers).**

    Δ+ = 2/3 − β/6 + (13/180)β² + (101/2700)β³ + (1657/567000)β⁴ − (32657/7620480)β⁵
         − (2167017157/800150400000)β⁶ + …   (extended through β¹⁰; b7–b10 in App. B)
    Δ− = 2/3 + β/6 + (1/18)β² + (7/432)β³ + (143/181440)β⁴ − (34877/15240960)β⁵
         − (2055143/1600300800)β⁶ + …

Appendix B values transcribed cleanly from the PDF text layer: b7 = −367979177879/1344252672000000 and b9 = +1207377346074065219/3794018741452800000000. v2.2: from the store PDFs (both editions, identical) the previously garbled entries now transcribe cleanly: b8 = +38764675528307/83642388480000000 and b10 = +3830311511546635473989/92555087197741056000000000. Magnitudes continue the tower smoothly (|b7|…|b10| ≈ 2.74×10⁻⁴, 4.63×10⁻⁴, 3.18×10⁻⁴, 4.14×10⁻⁵), and the order-10 evaluation respects the seam claim (+1.3×10⁻² relative at β = 1.5, i.e. <2%); the two-sided-control table's "strong tower" column is the order-6 series, whose quoted residuals (−7×10⁻⁴ at β = 1, −2.0×10⁻² at β = 1.5) were reproduced independently of b7–b10. Analytic re-derivation of b7–b10 remains the residual check (§6.4).

Seam structure: strong tower accurate to <2% for β ≤ 1.5; weak law <0.7% for β ≥ 2.5; level-repulsion minimum near β ≈ 0.8. Negative results: best pole-free two-point Padé in x = √β is 6.1×10⁻²; cubic algebraic approximants develop a branch defect near β ≈ 4.7.

**Theorem 4.2 (global closure).** Δ+ = √(1/2 + (2/3)β·g(β)) with g a pole-free two-point [13/13] Padé in x = √β matched to the proven towers; max relative error 9.5×10⁻⁴ on β ∈ [0.25, 50].

### 1.4 Bridge Theorem (manuscript §5)

**Theorem 5.1.** Restricting the Kogut–Susskind magnetic term to a single plaquette: h_loop = 4H_β − β at β = 3y/2, hence m±(y) = 4Δ±_SU(3)(3y/2). O(y) check: m± = 8/3 ∓ y.

### 1.5 O(y²) leakage (manuscript §6)

**Lemma 6.1.** Fused-channel norms N_R = d_R/9: {1: 1/9, 8: 8/9} and {3̄: 1/3, 6: 2/3}; channel energies above E0 = 8/3: 1 → 4, 8 → 11/2, 3̄ → 14/3, 6 → 17/3.

**Theorem 6.2 (C-even).** Per shared-link neighbor: self-energy = hopping = −481/612 (channel split 1: −1/12, 8: −16/51, 3̄: −1/6, 6: −2/9), orientation-independent; vacuum subtraction +3/4 per neighbor; assembly L(d) = 4(2d−3)(−503/612); at d = 3:

    m+(y) = 8/3 − y − (9397/1020) y² + O(y³).

**[CORRECTED — see §8.2.]** The hopping entry omits the vacuum-mediated route ⟨e_r|W|0⟩⟨0|W|e_i⟩/(8/3) = +3/4 present for every C-even pair. Corrected per-neighbor hopping t₊ = −481/612 + 3/4 = −11/306; corrected assembly L(d) = 4(2d−3)·(−11/153); corrected coefficient at k = 0: −217/1020. The self-energy −481/612, its channel split, the diagonal vacuum subtraction +3/4, and the neighbor count 12 are all unaffected.

**Theorem 6.3 (C-odd).** Within-plaquette second order −1/4 (consistency 9c2− = 1/2); cross-component networks vanish by link balance so the C-odd neighbor self-energy equals −481/612; hopping families N_mixed = −27/68 (channels 1, 8) and N_like = −7/18 (channels 3̄, 6) with sum −481/612; signed hopping t−(s) = 5s/612; diagonal leakage 12(−481/612 + 3/4) = −22/51, diagonal y² coefficient 1/2 − 22/51 = 7/102; band bound ±5/51, coefficient confined to [−3/102, 17/102]. |t−|/|t+| = 5/481 ≈ 1/96 (Remark 6.4: nearly immobile C-odd excitation). Assumption 6.5: infinite-volume linked-cluster step invoked, not re-proved.

### 1.6 Domino verification (manuscript §7)

Exact diagonalization of the Kogut–Susskind Hamiltonian on two plaquettes sharing one link: 19 gauge-invariant functions; exact rational Haar tensor-network engine (Weingarten k ≤ 2, ε-tensor third moments); Fierz-insertion electric operator; gates include the full y = 0 spectrum {0, (8/3)×4, 4×2, (14/3)×2, (17/3)×2, (11/2)×2, 6×2, (20/3)×4} and E_vac → −(3/2)y². Predicted vs exact level coefficients:

| Level | Prediction | ED | Difference |
|---|---|---|---|
| C-even symmetric | 1769/3060 = 0.5781046 | 0.5781130 | 8.4×10⁻⁶ |
| C-even antisymmetric | 13/20 = 0.6500000 | 0.6500011 | 1.1×10⁻⁶ |
| C-odd symmetric | 31/68 = 0.4558824 | 0.4558835 | 1.2×10⁻⁶ |
| C-odd antisymmetric | 17/36 = 0.4722222 | 0.4722236 | 1.4×10⁻⁶ |

The C-odd values were blind targets (produced by the diagonalization before the C-odd assembly).

All four coefficients are now also derived in-project as exact rationals by the abstract-domino perturbation theory of §8.4 ({1769/3060, 13/20} and {31/68, 17/36} reproduced exactly as gates), upgrading §7 to EXACT-in-project — and the C-even pair is precisely what adjudicates the Theorem 6.2 correction (§8.2).

### 1.7 Numerical context at β = 5.7 (manuscript §8)

LO Euclidean SCE ratio m/√σ = 4√(−ln u): 3.815 at β = 5.7, 3.713 at β = 6.0 (only the ratio is meaningful). Monte Carlo: Wilson action, 10³×16, 8 chains × 540 measurements, 12 smeared A1++ operators, C(0)-metric fixed-vector GEVP with synthetic self-test: a·m(0++) = 1.146 ± 0.246, consistent at 0.65σ with 0.987(9) at β = 5.6924; m/√σ = 2.82 ± 0.61 (the Wilson-action scalar dip). Stated caveats: τ_int = 7–32 measurements; single coarse coupling; no continuum statement.

### 1.8 Appendix A (verification chain)

Eight named single-file certificate scripts with hard gates (inventoried in §0 above), plus two methodological lemmas: (i) Casimir cross-term signs (+T⊗T for like slot pairs, −T⊗T^T for mixed (U, Ū) pairs, detectable via ∫Δf = 0); (ii) C(0)-metric whitening for noisy variational bases (whitening at t0 ≥ 1 amplifies noise; per-timeslice max eigenvalues ride the random-matrix noise edge and bias low).

---

## 2. Verification map: manuscript claim → project evidence

Status legend — **EXACT**: proven/closed in exact arithmetic inside the project files; **NUM**: independent numerical confirmation inside the project files; **PREVIEW**: numerical value in the files consistent with the manuscript's exact constant, but no exact derivation recorded; **EXT**: manuscript attributes verification to Appendix A scripts not present in the project; **ABSENT**: no trace in the project files. Tier tags (v2.1): **store** = in the project file store with a June 11 run log; **delivered** = produced and verified June 11, awaiting deposit; **session-only** = exists only in working-session records. The v2.0 label EXACT (in-project) is superseded by EXACT (store via notebook) where applicable.

| Claim | Status | Evidence (notebook · cell) | Notes |
|---|---|---|---|
| Leading √(2β/N) | EXACT (harmonic) + NUM | 206·12 (ladder, gap/√β → √(2/3) to 10⁻⁸ via GR3 fit); GR5·6 (SU(4) √(β/2)) | GR5·5's early c4 ≈ 7/16 was a truncation artifact, superseded by corrected M-scaling in GR5·6 |
| c0 = −5/16; q4 = −1/576 | EXACT | GR1·0/3/5, GR3 (symbolic), GR4 | 180·q4 = −5/16; numeric fits −0.31249996 (GR3), −0.3125000 (206·12) |
| q6 = 19/1244160 | EXACT | GR1·0 | Input to the sextic first-order piece |
| c1 = −311√6/9216 (Thm 2.1) | EXACT ×3 + NUM ×3 | GR1·12 (invariant ledger: Δ_res = −205√6/3072, Δ_H2 = 19√6/576, residual 0); GR2·0 (fixed-branch resolvent); 206·16 (exact rational engine q = −311/9216); 206·12 fit −0.0826591; GR3 fit −0.08265957; GR1·2 Richardson −0.0826544 | Strongest-verified constant in the program |
| Rank-two term √6/576 (Rmk 2.5) | EXACT + NUM | GR1·12 (structural: radial reduction drops p3²); 206·12 (radial foil −0.0869122 rejected at ≈8500× fit residual) | The manuscript's "≈8000×" traces to exactly this output: 0.0042526 / 5×10⁻⁷ |
| c0(N) = −(2N²−3)/16N | NUM (N=4) + used (N=7) + **EXACT (store, N=3–12)** | GR5·6 (−29/64 confirmed); 206·13–15 (c0(7) = −95/112 as input); gue_shell_calculus_verifier.py (run June 11: exact per-N table, e.g. −95/112 at N=7, −95/64 at N=12) | Closed form now store-certified over N = 3–12 |
| c1+(N) closed form (Thm 2.3) | EXACT (N = 3, 4, 6) | 206·16–17: q(3) = −311/9216, q(4) = −1193/16384, q(6) = −6953/36864, each matching −√2(6N⁴−24N²+41)/(1024N^{3/2}); v2.3: c2_certificate.py (q1 column, N = 6–12) and n7_c1_discrimination_certificate.py (delivered: symbolic identity in N at generic rank; exact at every N = 3–12 incl. rank-reduced N = 3, 4, 5) | A competing "cubic interpolation" candidate coincides with this formula through N = 6 and separates only at N = 7 (decided in the next row) |
| c1+(N) at N = 7 (discrimination) | **DECIDED — EXACT (two independent routes, v2.3)** | Route A: c2_certificate.py (store, cut–join engine; instrumented driver prints exact q1(7) = −13271/50176). Route B: n7_c1_discrimination_certificate.py (delivered; independent explicit-pairing engine, 18 gates incl. Parseval closure and the N = 3 ledger split q_res = −205/3072, q_H2 = 19/576) | q1(7) = −13271/50176; cubic foil −13127/50176 eliminated (separation 9/3136 in q units; √14·144/50176 ≈ 1.07×10⁻² in c1 units). Legacy 206·13–15/206·20 attempts superseded; ff_gap_rational's 3 ≤ N ≤ 10 claim exceeded (3–12 plus the identity) |
| c1−(3) = −551√6/13824; entire charge-odd weak sector through c1 | **EXACT (store, N=3–12)** | ENGINE_SUN_codd_local_gap_exact.py (run June 11: exact Wick recursion; c0−(3) = −3/8, q−(3) = −551/13824; closed forms c0−(N), c1−(N) verified N = 3–12); su3_exact_c2.py (independent N=3 route); su3_odd_gap.py; SU_N_C_odd_appendix.tex; C-odd Finite-Wick docx | The notebook corpus remains silent on the odd sector (GR2·0 rejected branch; 206·12's 1.5ω ladder entry); the store carries the derivation. §6.5 closed |
| H1 = −p4/48 (Prop 3.1) | Used as convention | 206·16 (engine conventions H1 = −P4/48, H2 = √(N/2)P6/1440); consistent with GR1·12's H1 = −p2²/96 via p4 = p2²/2 at rank two | Universality proof remains EXT: the store's gue_shell_calculus_verifier.py (run June 11) certifies the companion Prop 3.1 data (α_N, γ_N, c0(N), radial leakage entries, Perron quartic; N = 3–12) but does not gate H1-universality itself |
| αN = (N²−3)/2 | Implicit (N=3) + **EXACT (store, N=3–12)** | GR1 Laguerre basis with α = 3 = α_3; gue_shell_calculus_verifier.py (run June 11: α table 3, 13/2, 11, …, 141/2) | — |
| γN; Theorem 3.2 (R0, 1/24, 7/80, 14/17, MC) | γN: **EXACT (store, N=3–12)**; R0/slopes/MC: ABSENT / EXT | gue_shell_calculus_verifier.py (run June 11: γ table 1/2, 29/68, …, 19/116) | r_moment_ratio_measurement.py not in store; the R-observable and MC rows are unchanged |
| c2(3) = −5665/110592 = −0.0512244 | PREVIEW | GR3 fit −0.0512314; 206·12 fits −0.0507612 (deg 3), −0.0512553 (deg 4) | Fits consistent at the 10⁻⁵–10⁻⁴ level with the exact value, now **EXACT (store)**: su3_exact_c2.py (run June 11: c2+ = −5665/110592, c2− = −53/864, both c1 q's gated) |
| c2(N), c2−(N) closed forms; parity–rationality (j ≤ 2) | **EXACT — complete (store + delivered: even N = 3–12; odd N = 3–13; v2.4)** | c2_certificate.py (run June 11: exact third-order RS; even table matches −(60N⁶−401N⁴+1522N²−2297)/(49152N²) for N = 6–12, odd closed form for N = 7–13, with c0/q1/qres gated en route); su3_exact_c2.py (N = 3, both sectors); 206·22–25 cut–join attempt recorded (H3 shift −(N−1)⁷/(256N⁷)) | v2.4: no uncertified instances remain — even N = 3–12 and odd N = 3–13 complete (residual ranks decided by two routes, §6.14). Parity–rationality exhibited structurally at j ≤ 2 across the full range. Cut–join completion remains optional cross-validation (§6.3) |
| c3(N) closed form; c3(3), c4±(3) exact | EXT | — | Manuscript: independent character-basis extractions agree to 1.05×10⁻⁴ and 9.1×10⁻⁶; §3.14 (v2.1) anchors c3+(N) at N = 3 exactly against Theorem 2.1 |
| §4 strong towers, b7–b10, seam, Padé negative results, Thm 4.2 (9.5×10⁻⁴) | ABSENT | — | No strong-coupling or Padé code in any notebook |
| §5 Bridge Theorem | ABSENT (paper self-contained) | — | Proof is short and contained in the manuscript; re-derived independently in §3.9 and §4 (C.5) below |
| §6 leakage constants (d_R/9, −481/612, 5s/612, 7/102) | **EXACT (store via notebook)** | SU3_d3_corrected_full_notebook.ipynb → ENGINE_FLUX_su3_domino_d3.py (251 gates; kernel-executed June 11) | Lemma 6.1 energies and norms, t−(s) = 5s/612, and diagonal leakage −11/306 re-derived exactly; **Theorem 6.2's 9397/1020 corrected to −217/1020** (§8.2) |
| §7 domino ED | **EXACT (store via notebook)** | SU3_d3_corrected_full_notebook.ipynb → ENGINE_FLUX_su3_domino_d3.py | All four level coefficients reproduced as exact rationals (abstract-domino PT, both shared-link signs s = ±1) |
| §8 SCE table and MC at β = 5.7 | ABSENT / EXT | — | glueball_v4_* scripts not in project |
| §10 deferred-program characterization | NUM | v16 (Wilson ≈ random plaquette-incidence: PASS), 193 (Bernoulli comparator fails) | Detailed in §5 below |

**Summary.** The notebook corpus independently establishes the leading term, c0, and c1 of the charge-even weak-coupling law — c1 in exact arithmetic by three distinct routes — plus the c1(N) closed form at N = 3, 4, 6 and the rank-two structural mechanism of Remark 2.5. As of Version 2.1 the store additionally certifies, with June 11 run logs: the entire charge-odd weak sector through c1 (N = 3–12); c2± complete (even N = 3–12; odd N = 3–13; residual ranks decided v2.4); c0+(N), α_N, γ_N (N = 3–12); and — via the deposited certificate notebook — the strong-coupling leakage/domino sector: Lemma 6.1, the §7 levels, the corrected Theorem 6.2 (§8.2), and the O(y³) constants (§8.4), 278 gates in all. As of v2.2 the full §8 chain is in the store and run-verified (326 gates; §6.13 closed), with the corrected band edition delivered (§6.11). As of v2.3 the c1+(N) closed form is certified identically in N (generic rank) and exactly at every N = 3–12, with the N = 7 foil eliminated by two independent routes. Still resting on absent Appendix A scripts: c3 and c4± beyond the §3.14 anchor, H1-universality, Theorem 3.2's R-observable and Monte Carlo, and §§4, 8 of the manuscript.

---

## 3. Internal consistency checks performed for this document

The following re-derivations were carried out independently during compilation (exact arithmetic unless noted). All pass. They are recorded so that future edits to the manuscript can be regression-tested against them.

**3.1 N = 3 specializations of Theorems 2.2–2.3 reproduce Theorem 2.1.**
c1+(3) = −√2·311/(1024·3√3) = −311√6/9216; c1−(3) = −√2·551/(1536·3√3) = −551√6/13824; c0−(3) = −3·6/48 = −3/8; c2+(3) = −(43740 − 32481 + 13698 − 2297)/442368 = −22660/442368 = −5665/110592; c2−(3) = −(69255 − 79461 + 52677 − 15335)/442368 = −27136/442368 = −53/864. All four match Theorem 2.1 exactly.

**3.2 Theorem 3.2 / Proposition 3.1 internal closure.**
R0(3) = 3·5/(3·10·12) = 1/24; the slope numerator N²(N²−9) vanishes identically at N = 3, consistent with the SU(3) expansion starting at β^{−2}; at N = 4 the slope is 16·7/(8·17) = 14/17. γ3 = (2·9−3)/(3·10) = 1/2; α3 = (9−3)/2 = 3, which is precisely the Laguerre parameter α = 3 hard-coded throughout GOODRESULTS1 — an implicit in-project confirmation of αN at N = 3.

**3.3 Leakage channel arithmetic (Theorems 6.2–6.3).**
Channel split sums to the self-energy: −1/12 − 16/51 − 1/6 − 2/9 = (−51 − 192 − 102 − 136)/612 = −481/612. Family decomposition: N_mixed + N_like = −27/68 − 7/18 = (−243 − 238)/612 = −481/612, and the difference gives |t−| = |−243 + 238|/612 = 5/612. Diagonal C-odd leakage 12(−481/612 + 459/612) = −22/51; coefficient 1/2 − 22/51 = 7/102; band 12·(5/612) = 5/51 = 10/102, hence the interval [−3/102, 17/102]. Per-neighbor C-even total −481/612 + 459/612 − 481/612 = −503/612. *(Arithmetic of the manuscript as written; §8.2 corrects the third summand to the vacuum-route-inclusive hopping −11/306 = −22/612, giving per-neighbor total −44/612 = −11/153.)*

**3.4 The 9397/1020 assembly.**
4Δ+(3y/2) = 8/3 − y + (13/20)y² + O(y³) from the strong tower (4·(13/180)·(9/4) = 13/20); adding L(3)y² = 12·(−503/612)y² = −(503/51)y² gives 13/20 − 503/51 = (663 − 10060)/1020 = −9397/1020, matching Theorem 6.2. Note the restricted within-plaquette value 13/20 equals the domino C-even antisymmetric level coefficient — exactly the manuscript's structural statement that all neighbor leakage cancels in that level. *(This check confirms the manuscript's internal arithmetic only; §8.2 corrects the input hopping, and the corrected assembly reads 13/20 + 12(−11/306) + 12(−11/306) = −217/1020.)*

**3.5 C-odd within-plaquette consistency.**
4·c2−·(3/2)² = 4·(1/18)·(9/4) = 1/2 = 9c2−, matching Theorem 6.3(i).

**3.6 H2 convention equivalence (links GR1 to the 206 engine).**
At rank two (traceless, e1 = 0) the Newton identities give p4 = p2²/2, p5 = (5/6)p2p3, p6 = p2³/4 + p3²/3. Hence the 206 engine's H2 = √(N/2)·P6/1440 at N = 3 equals √(3/2)(p2³/4 + p3²/3)/1440 = √6·p2³/11520 + √6·p3²/8640 — identically GR1 cell 12's H2. The two independently written engines share one convention.

**3.7 H1 convention equivalence.**
p4 = p2²/2 at rank two implies −p4/48 = −p2²/96, so the universal H1 of Proposition 3.1 (used in 206·16) and GR1's radial H1 coincide for SU(3).

**3.8 The "≈8000×" of Remark 2.5.**
206·12: foil separation √6/576 = 0.0042526; fit deviation |−0.0826591 − (−0.0826596)| ≈ 5×10⁻⁷; ratio ≈ 8.5×10³.

**3.9 Bridge consistency at first order.**
Matching −y(χ+χ̄) to 4·(−β/6)(χ+χ̄) gives y = 2β/3, i.e. β = 3y/2; four links at ½C2 quadruple the Casimir weight. Then m± = 4Δ±(3y/2) = 4(2/3 ∓ (1/6)(3y/2)) + O(y²) = 8/3 ∓ y, agreeing with the degenerate-PT check in the manuscript's proof of Theorem 5.1.

**3.10 SU(4) two-way check.**
The 206·16 exact rational q(4) = −1193/16384 gives c1(4) = √8·q(4) = −√2·1193/8192 = −0.20596, identical to the closed form −√2(6·256 − 384 + 41)/(1024·8). Predicted weak-law residual at β = 1000: −0.20596/√1000 = −6.5×10⁻³; GOODRESULTS5 cell 6 measured −6.73×10⁻³ — agreement, with the small remainder of the expected sign and size for the c2(4) term. The closed form was thereby anchored numerically in a notebook that never printed it.

**3.11 SU(6) closed-form match.**
√12·(−6953/36864) = −6953√3/18432 = −√2(6·1296 − 864 + 41)/(1024·6√6). Exact.

**3.12 Both leading terms from one harmonic computation.**
With the physics Casimir metric (C.0 below), the per-quantum frequency is ω0 = √(β/2N); the first Weyl-invariant excitations are p2 (degree 2, C-even) and p3 (degree 3, C-odd), giving Δ+_lead = 2ω0 = √(2β/N) and Δ−_lead = 3ω0 = √(9β/2N) — the leading terms of both sectors in Theorem 2.3 from a single normalization. Numerical anchor: 206·12's spectrum ladder at β = 400 shows (E_n − E0)/ω = 0.981, 1.477, 1.953, 2.445, 2.918 at degrees 2, 3, 4, 5, 6 against the harmonic values 1, 1.5, 2, 2.5, 3 (ω ≡ √(2β/3)) — the p3 entry at 1.5ω is the C-odd leading gap, visible in the project data even though no odd-sector law was derived there.

**3.13 c2 previews.**
Exact −5665/110592 = −0.0512244 vs GR3 fit −0.0512314 and 206·12 degree-4 fit −0.0512553: consistent at the level expected from the neglected β^{−3/2} term.

**3.14 c3+(N) specializes to Theorem 2.1 (extends 3.1; new in v2.1).**
2970·3⁸ − 27878·3⁶ + 166512·3⁴ − 546024·3² + 734405 = 19486170 − 20323062 + 13487472 − 4914216 + 734405 = 8470769 exactly, and 2²¹·3²·3³ = 509607936, so c3+(3) = −8470769√6/509607936 — Theorem 2.1's c3 on the nose. (Gate A7 of the document regression.)

**3.15 First-principles curvature factor 4/3 (new in v2.1; independent of ENGINE_FLUX_glueball_band_certificate.py).**
The 3×3 orientation Bloch matrix S(k) — diagonal 2cos k_a + 2cos k_b for orientation (ab), off-diagonal 4cos(k_t1/2)cos(k_t2/2) with (t1, t2) the transverse pair — has spectrum {12, 0, 0} at k = 0 and the triple {−4} at (π, π, π), confirming λ_S ∈ [−4, 12] with the A₁/E split of §8.1. S is even in k, so the O(|k|²) shift of the simple A₁ eigenvalue is exactly ⟨A₁|S⁽²⁾|A₁⟩ = (1/3)·(entry sum of S⁽²⁾) = −(4/3)|k|², verified symbolically along three independent directions: λ_S(k) = 12 − (4/3)|k|² + O(k⁴). The curvature line of §8.2/§6.11 is therefore derived, not only certified: (11/306)(4/3) = 22/459 corrected; (481/612)(4/3) = 481/459 as-written. (Gates D3*/D3b.)

---

## 4. Support Appendix C — corrected, self-contained package

This section supersedes the external support-derivations note. It is written to be pasted into the manuscript (or a companion note) without citing any document outside the manuscript itself. Changes from the note are recorded in §7.

### C.0 Conventions and metric normalization (required preamble)

Two bi-invariant inner products on su(n) appear in the literature:

    ⟨Y, Z⟩_tr   = −Re Tr( ρF(Y) ρF(Z) )            (defining-trace convention)
    ⟨Y, Z⟩      = −2 Re Tr( ρF(Y) ρF(Z) )           (physics/Casimir convention)

The manuscript and all project numerics use the second: orthonormal generators satisfy Tr(TaTb) = δab/2, the quadratic Casimir is built in this metric, and C2(fund) = 4/3 for SU(3). The Wilson plaquette potential Φβ(g) = β(1 − (1/n)Re Tr g) has Hessian at the identity

    ∇²Φβ(1)[Y, Y] = (β/n)·⟨Y, Y⟩_tr = (β/2n)·⟨Y, Y⟩,

so α_W = β/n in the trace convention but α_W = β/2n in the Casimir convention. With H = ½C2 + ½α_W r² + … in the Casimir metric, the per-quantum harmonic frequency is

    ω0 = 2√(a·b),  a = 1/2,  b = β/(4N)   ⇒   ω0 = √(β/2N).

The Weyl-invariant grading (first invariants p2 at degree 2, p3 at degree 3) then yields the leading gaps of both charge sectors at once: Δ+ = 2ω0 = √(2β/N) and Δ− = 3ω0 = √(9β/2N), as in Theorem 2.3.

**Warning (the factor-2 trap).** Pairing the trace-convention Hessian α_W = β/N with the Casimir-normalized ½C2 yields ω0 = √(β/N) and a spurious leading gap √(4β/N), off by √2. Any appendix stating the Hessian must pin the metric explicitly. Numerical anchor for the correct convention: the character-basis spectrum ladder (Untitled206, cell 12) at β = 400 reproduces level spacings of ω0 = √(β/6) per polynomial degree to 2% accuracy.

### C.1 Plaquette holonomy linearizes to the lattice curl d1

Let X ∈ C¹(Λ; g) be a Lie-algebra-valued 1-cochain and Ub(t) = exp(tXb) the vacuum geodesic. For p = (x; μ, ν),

    Up(t) = U_{x,μ}(t) · U_{x+êμ,ν}(t) · U_{x+êν,μ}(t)^{−1} · U_{x,ν}(t)^{−1}.

Every factor equals 1 at t = 0, so the derivative is the sum of first variations, inverse factors entering with a minus sign:

    (d/dt)|₀ Up(t) = X_{x,μ} + X_{x+êμ,ν} − X_{x+êν,μ} − X_{x,ν} = (d1 X)_p,

with d1 the oriented plaquette coboundary (incidence coefficients σ_{p,b} ∈ {−1, 0, +1}). Hence (d Hol_p)|_vac = d1: the single-plaquette flux coordinate quantized by Hβ is exactly one component of the lattice curl.

### C.2 Wilson plaquette Hessian at the identity

For g(t) = exp(tY), A = ρF(Y) anti-Hermitian, Re Tr exp(tA) = n + (t²/2)Re Tr(A²) + O(t⁴) — the O(t) and O(t³) terms vanish because Tr(A) and Tr(A³) are purely imaginary. Therefore

    Φβ(exp tY) = −(β/2n) Re Tr(A²) t² + O(t⁴) = ½ α_W |Y|² t² + O(t⁴),

with α_W as fixed by the chosen metric in C.0. The gradient vanishes at the identity; the Riemannian Hessian is α_W·⟨·,·⟩.

### C.3 Wilson vacuum Hessian equals the discrete Maxwell operator

Combining C.1 and C.2 along the geodesic family U(t): Up(t) = 1 + t(d1X)_p + O(t²), and since ∇Φβ(1) = 0 the second-order term of Up contributes nothing (the would-be cross term multiplies the vanishing gradient). Summing over plaquettes,

    ∇²S_{Λ,β}(vac)(X, X) = α_W Σ_p |(d1X)_p|² = α_W ⟨X, d1*d1 X⟩,

i.e. ∇²S(vac) = α_W d1*d1. The one-plaquette class Hamiltonian is the compact, all-orders-in-the-group completion of a single such local curvature mode; the manuscript solves that local atom exactly.

### C.4 Incidence counts (two different counts, kept apart)

*Euclidean (4D action geometry).* A link (x, μ) lies in the boundary of the plaquettes (x; μ, ν) and (x − êν; μ, ν) for each ν ≠ μ, hence in νP = 2(d − 1) plaquettes; νP = 6 in d = 4. Each plaquette contributes 3 other links, so the link-adjacency degree obeys D_E ≤ 3νP = 18 in d = 4.

*Hamiltonian (spatial leakage counting, manuscript §6).* In d_s spatial dimensions a spatial link lies in 2(d_s − 1) spatial plaquettes, i.e. 2d_s − 3 plaquettes other than a given one. A plaquette has four boundary links, so the shared-link neighbor count is 4(2d_s − 3) = 12 at d_s = 3 — the assembly factor of Theorem 6.2. *(Per §8.2 the corrected per-neighbor constant at k = 0 is −11/153 = (−481 + 459 − 22)/612: self-energy + vacuum subtraction + vacuum-route-inclusive hopping; the count 12 is unaffected.)*

These are distinct counts answering distinct questions; stating both prevents the apparent 6-versus-3 tension.

### C.5 Bridge restatement (optional)

The factor-4 / β = 3y/2 matching is re-derived in §3.9 above and is identical to the manuscript's own proof of Theorem 5.1; including it as an appendix item is redundant. If retained for self-containedness, mark it as a restatement.

### C.6 Scope and Euclidean compatibility

The Wilson weight factorizes over plaquettes with w_β(g) = exp((β/n)Re Tr g), whose character expansion has non-negative coefficients; the resulting sum-of-squares kernel w_β(g⁻¹h) = Σα f̄α(g)fα(h) is the standard mechanism behind finite-volume Osterwalder–Schrader reflection positivity for the Wilson measure (Osterwalder–Seiler, the manuscript's reference [3]). One sentence citing [3] suffices; a full RP appendix would invite precisely the continuum-directed reading that manuscript §§1.1 and 9 foreclose. Dependency statement: lattice geometry (C.1–C.4) supports the *interpretation* of the local object; the manuscript supplies the *exact* one-plaquette and first-neighbor strong-coupling spectral data; neither implies any statement about the continuum Yang–Mills mass gap.

### C.7 Sourcing policy

Appendix C must be self-contained. In particular it must not cite the deferred Wilson-defect (PMBSF) manuscript or its appendices: the paper declares that program logically independent (§10), and routing "support" through it would blur a firewall the paper deliberately built. Derivations C.1–C.4 are elementary and need no external source.

---

## 5. Program B record (PMBSF / Wilson-defect geometry)

Logically independent of every theorem in the manuscript; summarized here because (a) four of the nine notebooks belong to it, and (b) one sentence of manuscript §10 rests on it.

| Notebook | Test | Headline result |
|---|---|---|
| Untitled185 (v3b) | Danger-corner firewall θ_phys = sup⟨f, V(U)f⟩/⟨f, Mf⟩, M = m²I + α d1*d1, Hodge-projected; L = 8–24, 50 cfgs, hot/cold, 3 weightings (β = 4, m² = 0.5) | All SAFE; θ_phys p99 = 0.8541, p999 = 0.8779 < 1 |
| Untitled185 cell 7 (v4) | Mosco / projected-Maxwell continuum-bridge verifier | Projector divergence/idempotence sanity PASS; θ_phys < 1 and hard-bound assertions hold on all rows |
| Untitled193 cell 0 (A′ audit) | Global spike-residual budget against the Bernoulli random-plaquette capacity bound | Allowed M̄_max ≈ 2.4–3.3×10⁻⁴ at L = 24 — unrealistically tiny; the A′ route does **not** close; pivot to trace-weighted finite-rank route |
| Untitled193 cell 1 | Trace-weighted finite-rank closure audit | Verdict WEAK across δ (needs a sharper lemma or smaller observed W̄) |
| Untitled193 cells 2–3 (v13/v14) | Heat-bath coefficient geometry / global absorption (Matrix-Stein η diagnostics) | η thresholds recorded per subset; decision rules logged |
| v16_MATRIX_PASS | Matrix-Laplace / trace-MGF transfer: Wilson top-p plaquette masks vs uniform random masks of equal count, A_p = P·1_{∂p}·P | PASS (max Δ_ML ≤ 0.05) at p = 0.001 (0.0050) and p = 0.003 (0.0199 at L = 12; 0.0180 at L = 24, A100 run); FAIL at p = 0.01, θ = 64 (0.1256). Eigen/moment-root Wilson-to-random ratios 1.008–1.035 |
| GOODRESULTS5 cells 0–4 | Massive Green-kernel decay G ~ C r^{−(d−1)/2}e^{−ηr} for the Hodge comparator; deterministic defect capacity envelope | Fitters corrected for the dimensional prefactor; envelope diagnostics recorded |

**What this licenses in the manuscript.** Exactly the §10 sentence: Wilson defect masks behave like *random plaquette-incidence* geometry (v16 PASS at the operative selection fractions) rather than like *independent Bernoulli edge* masks (the Bernoulli comparator consumes the budget in the 193 audit). Nothing else in the manuscript may cite Program B, per C.7.

---

## 6. Open items and required artifacts

**6.1 Add the remaining Appendix A certificates to the store.** One of the eight is present and run-verified (gue_shell_calculus_verifier.py, June 11); seven remain absent: ff_gap_rational.py, sun_gap_free_fermion_certificate_c3.py, su3_c4_exact_certificate.py, r_moment_ratio_measurement.py, domino_ed_certificate.py, glueball_v4_reanalysis_fixedvec.py, glueball_v4_robustness.py. The store's c2 pair (c2_certificate.py, su3_exact_c2.py) discharges the c2 portion of the su3_c4 lineage. The audit weight still resting on the seven absent scripts: exact c3 and c4 (both sectors) beyond the §3.14 anchor; H1-universality and Theorem 3.2's R-observable with its Monte Carlo; §§4, 8 of the manuscript. (ff_gap_rational's c1 burden — the N = 7 discrimination and the 3 ≤ N ≤ 10 certification — is discharged as of v2.3, §6.2.)

**6.2 [CLOSED — v2.3] N = 7 discrimination decided.** q1(7) = −13271/50176 exactly, by two independent exact routes: route A, the store's cut–join engine (c2_certificate.py, instrumented driver; q1(6, 7, 8) printed exactly, all matching the quartic closed form), and route B, the delivered n7_c1_discrimination_certificate.py — a from-scratch engine (explicit-pairing projected-propagator Wick cross-gated against a trace-split full-GUE reduction; exact Laurent-in-N moments; exact Gram–Schmidt with rank-reduced cases at N = 3, 4, 5 handled, graded invariant dimensions 5/7/7 against 8 at N ≥ 6; Parseval-closure completeness gates; the GR1 cell-12 ledger split reproduced at N = 3; 18 gates, all passing). The cubic-interpolation foil −13127/50176 is eliminated. Route B additionally proves the Theorem 2.3 c1+ closed form identically in N at generic rank and exactly at every N = 3–12. The mod-p route (206·20) is moot. Unit note retained: the 1.07×10⁻² separation is in c1 units, √14·144/50176; in q units it is 144/50176 = 9/3136 ≈ 2.87×10⁻³.

**6.3 [CLOSED as a requirement — v2.1] Symbolic c2(N) completion demoted to optional cross-validation.** c2_certificate.py (store, run June 11) certifies the c2+(N) closed form for N = 6–12 and c2−(N) for N = 7–13 by exact third-order Rayleigh–Schrödinger; su3_exact_c2.py covers both SU(3) instances. Completing 206·25's cut–join engine would add an independent symbolic-in-N route — worthwhile, no longer load-bearing. Preserve the recorded intermediate (direct H3 shift = −(N−1)⁷/(256N⁷)) as a gate if pursued. The residual certification gap moves to §6.14.

**6.4 [RESOLVED at transcription level — v2.2] Appendix B b8 and b10.** Both now transcribe cleanly and identically from the two store PDF editions (values in §1.3), with tower-magnitude and seam-claim consistency checks passing. Residual: an analytic re-derivation of b7–b10 — the §4 tower has no in-store code (§6.1's absent-script list).

**6.5 [CLOSED — v2.1] Charge-odd weak-sector artifact exists in the store.** ENGINE_SUN_codd_local_gap_exact.py (run June 11) derives c0−(N) and c1−(N) by exact Wick recursion and verifies the closed forms for N = 3–12; su3_exact_c2.py independently reproduces the N = 3 instance; SU_N_C_odd_appendix.tex and the C-odd Finite-Wick docx document the derivation. The notebook-corpus observation stands (GR2·0 rejected branch; 206·12's 1.5ω ladder entry) but no longer marks a gap.

**6.6 If Appendix C is adopted, apply the §4 corrections:** the C.0 metric line (the factor-2 trap), the C.4 two-counts distinction, OS demoted to one sentence citing [3], C.5 marked optional, C.7 sourcing policy enforced.

**6.7 Documentation hygiene (optional, in the spirit of manuscript App. A's lemma log).** Record (i) the cubic-foil candidate and its planned elimination at N = 7; (ii) GR5·5's truncation artifact (apparent c4 ≈ 7/16) and its correction by M-scaling in GR5·6; (iii) the early Weyl-triangle CPU pathology (c1_fit = 263.8 from unconverged Davidson) and its GPU fix — each is a reusable failure mode.

**6.8 Adopt §3 as a regression gate list.** The thirteen checks of §3 are cheap, exact, and span §§2–7 of the manuscript; any future edit should re-run them. The §8 certificates add 323 machine gates (29 + 16 + 27 + 251); the strong-coupling regression command is `python3 ENGINE_FLUX_su3_moments_ext.py && python3 ENGINE_FLUX_su3_domino_d3.py`, now reproducible from the deposited notebook. v2.1 adds the document-level regression ENGINE_FLUX_master_v2_regression_certificate.py — 40 hard gates spanning §§1–3 arithmetic (including 3.14–3.15) and the §§6–8 constant web, all passing June 11; command: `python3 ENGINE_FLUX_master_v2_regression_certificate.py`.

**6.9 [DRAFTED — v2.5] Theorem 6.2 correction: paste-ready patch delivered.** PAPER_FLUX_manuscript_section6_patch.tex, Patches 1–2 and 5–6: Lemma 6.1′ (the vacuum-mediated route, with proof, the distant-pair cancellation, and the §7 adjudication forcing |t₊| = 11/306), the corrected Theorem 6.2 (hopping t₊ = −481/612 + 3/4 = −11/306; L(d) = 4(2d−3)(−11/153); eq. (22) → −217/1020; the operator identity reinterpreted as equating channel sums), the corrected Remark 6.4 (per-bond ratio 5/22; manifold-width 15/88; exact-flatness headline), and the global replace list including the abstract's −481/612 hopping line. The §7 table is explicitly untouched (it adjudicates), gaining one closing sentence. Closure requires folding into the manuscript source TeX (not in the store).

**6.10 [DRAFTED — v2.5] Theorems 6.3′ and 6.3′′: paste-ready patch delivered.** PAPER_FLUX_manuscript_section6_patch.tex, Patches 3–4: Theorem 6.3′ states the exact O(y²) band structure — incidence factorizations A+4I = NN†, S+4I = ÑÑ† with det Ñ ≡ 0, the exactly flat C-odd band m₋(k) = 8/3 + y + (11/306)y² for all k (replacing Theorem 6.3's interval), cube-2-chain kernel with L³+2 multiplicity, the corrected C-even band E₊(k) with curvature 22/459 and bandwidth 88/153, and the rest-frame content A₁⁺⁺ ⊕ E⁺⁺ (E⁺⁺ = 223/1020) and T₁⁺⁻. Theorem 6.3′′ states the third order: tromino vanishing, the rigid flat band m₋(k) = 8/3 + y + (11/306)y² − (109151/249696)y³ for all k, m₊(0) through O(y³) (−54049/520200), the band-top cubic 471353/1560600, and the leakₙᵉ = Tₙᵉ identity. Closure requires folding into the manuscript source TeX.

**6.11 [CLOSED — v2.2] glueball_band_results regenerated.** ENGINE_FLUX_glueball_band_certificate_v2.py (36 gates, all passing; delivered) applies t₊ = −11/306 throughout, retains the as-written −9397/1020 as a provenance gate, gates the corrected set {−217/1020, 1109/3060, 22/459, 88/153, 5/22} plus E⁺⁺ t-independence, and cross-checks six fields of RUN_TROM_d3_results.json's order-2 block. NOTE_FLUX_glueball_band_results_v2.md (delivered) is the corrected edition: C-even block regenerated, per-bond and manifold-width ratios updated (5/22; 15/88), effective mass m* = 459/(44y²), and the O(y³) caveat superseded by the certified third-order flatness. The C-odd block, the flatness theorem, the quantum-number identifications, and E⁺⁺(k=0) = 223/1020 stand as written.

**6.12 Next frontier: O(y⁴) — re-cut as a binary, pre-registered question (v2.6).** Trominoes first activate there (§8.3); the §8.4 pipeline extends with a fourth-order des Cloizeaux term, a revisited per-matrix moment-degree budget (the (5,2) block is already implemented and gated), and tromino geometry re-entering the assembly. §8.6's robustness theorem reduces the flatness question to a single criterion: flat at O(y⁴) ⟺ u(k)†H₄(k)P_⊥(k) ≡ 0, equivalently [H₄, P_flat] = 0, equivalently in real space the fourth-order hopping annihilates cube-boundary states up to a constant. Link-mediated (B M B†) contributions cannot break flatness at any order; the minimal corner-sharing symbol provably fails the criterion (gate G12), so once the O(y⁴) weight cards exist, flatness holds iff the weights satisfy a finite system of exact rational linear conditions Σ_g w_g·[u†T_g P_⊥] = 0 — either an exact lattice Gauss-law protection (suggesting all-orders flatness) or the first nonzero T₁⁺⁻ bandwidth, computable from the same scalars. Pre-registered outcome, decided by the weight computation.

**6.13 [CLOSED — v2.2] Residual §8 certificates deposited and run-verified.** ENGINE_FLUX_glueball_band_certificate.py (29/29), ENGINE_TROM_tromino_contract_independent_check.py (19/19 in the deposited edition — three gates beyond the 16 recorded at v2.0; requires ENGINE_FLUX_su3_haar_tromino_primitives.py/.json colocated and CERT_TROM_tromino_o3_su3_weight_cards.json at the authoring path /home/claude/review/), ENGINE_TROM_tromino_candidate_closed_form_check.py (symbolic identity + 40-point battery), glueball_band_results.md (as-written edition; corrected edition per §6.11), and CERT_FLUX_d3_certificate_results.md are all in the store. The O(y²) all-k flatness theorem and the O(y³) tromino-vanishing theorem are now store-supported. Path-portability note: the contract check's weight-cards read and the standalone ENGINE_FLUX_su3_domino_d3.py's JSON write both use authoring absolute paths — a one-line cwd fix in each (mirroring the notebook's domino fix) is recommended at next touch.

**6.14 [CLOSED — v2.4] Residual c2 ranks certified, two independent routes.** Route B: c2_residual_ranks_certificate.py (delivered) — the explicit engine of §6.2 extended to third-order Rayleigh–Schrödinger and to the C-odd sector, with a loop-equation full-GUE moment recursion (split/join Wick on the first insertion) reaching the degree-18 moments the odd pipeline needs, cross-gated against the explicit-pairing engine through degree 12 and against the exact Pochhammer identity E[p2^k] at degrees 16 and 18; odd rank structure 3/4/6/6 at N = 3/4/5/6 against 7 at N ≥ 7; 16 gates. Route C: c2_residual_ranks_routeC_storefix.py (delivered) — the store cut–join engine with one retrofit, an exact Schur-complement rank filter on each monomial basis; the full-rank store driver re-runs unchanged underneath, and the rank-fixed pipeline reproduces both N = 3 anchors before deciding; 13 gates. Decisions (routes agree exactly, all equal to the closed forms): c2+(4) = −55053/262144, c2+(5) = −60219/102400, c2−(4) = −72099/262144, c2−(5) = −261/320, c2−(6) = −3356317/1769472. Theorem 2.2's c2 table is thereby certified at every fixed rank (even N = 3–12, odd N = 3–13). Auxiliary closed form derived and gated en route: q_H2(N) = (N⁴−3N²+3)/(192N²).

---

## 7. Review record of the external support-derivations note

**Verified correct:** derivations 1 (holonomy = d1), 3 (Hessian = α_W d1*d1), 4 (incidence counts, including the quoted L(d) = 4(2d−3)(−503/612)), 5 (bridge matching), and the OS/transfer background (6–7). Derivations 8–10 are framing; 10's scope statement matches the manuscript.

**Corrected:** derivation 2 is internally consistent but uses the defining-trace metric (α_W = β/n). Set beside the manuscript's Casimir-normalized ½C2 it produces a spurious factor √2 in the leading gap. Fixed in C.0; once fixed, the Hessian plus the invariant grading derives *both* leading terms (a strengthening, not just a repair).

**Demoted:** OS/reflection positivity from a proposed appendix to one sentence citing [3] (scope protection); derivation 5 marked redundant with the manuscript's own Theorem 5.1 proof.

**Provenance flag:** the note cites "Appendix D/K/L, Core-3, Core-10, Synthesis 01/08" and a tensor-network synthesis — a corpus not present in this project and therefore unaudited here. The project notebooks contain the *computational embodiment* of the same geometry (d0/d1, the Maxwell comparator, Hodge projection, Wilson plaquette potential with α_W = β/n in the SU(2) trace convention) inside Program B — which is exactly why C.7 requires Appendix C to be written self-contained rather than cited through that corpus.

---

## 8. The strong-coupling band program (in-project, June 11 sessions)

Four work sessions completed, inside this project and in exact rational arithmetic throughout, the lattice band program that the manuscript's §6 opens: the O(y²) band theorem, an audit of the O(y³) tromino suite, the tromino-vanishing theorem, and the extraction of the third-order constant d₃ — in the course of which a constant of manuscript Theorem 6.2 was found to be incorrect and was machine-corrected. Total: 323 hard gates across four certificate scripts, all passing. Packaging (v2.1): the two core scripts are deposited via SU3_d3_corrected_full_notebook.ipynb, kernel-executed end-to-end on June 11 — 27 + 251 gates embedded, RUN_TROM_d3_results.json byte-identical between the notebook and standalone runs (sha256 d2d653b4…). v2.2: the band and tromino certificates are now also in the store and run-verified (§6.13); deposited §8 total 326 gates.

### 8.1 O(y²) band theorem (ENGINE_FLUX_glueball_band_certificate.py, 29 gates)

**C-odd sector (T₁⁺⁻).** The signed-adjacency hopping matrix possesses an *exactly* flat band: det Ñ ≡ 0 identically in k, so the band eigenvalue μ ≡ −4 and

    m₋(k) = 8/3 + y + (11/306) y²   for ALL k.

The dispersive partner band spans μ ∈ [−4, 8], i.e. coefficients [11/306, 41/306], touching the flat band at its bottom edge. This sharpens Theorem 6.3's interval bound [−3/102, 17/102] to exact band edges.

**C-even sector (A₁⁺⁺ ⊕ E⁺⁺).** Band-structure eigenvalue λ_S(k) ∈ [−4, 12] with λ_S(0) = 12 (A₁) and 0 (E, doubly). E⁺⁺ at k = 0 has coefficient 223/1020. The certificate's A₁⁺⁺ values were computed with the manuscript's t₊ = −481/612 and are superseded by §8.2; everything else in the certificate stands. v2.2: ENGINE_FLUX_glueball_band_certificate_v2.py applies the correction (36 gates; §6.11). v2.6 (attribution erratum): the multiplicity gate's parenthetical "L³ cube states + 2 dispersive branches touching" miscounts the decomposition; the exact split, gated in §8.6, is L³−1 independent cube states plus the three k = 0 rest states.

### 8.2 Correction to Theorem 6.2 (ENGINE_FLUX_su3_domino_d3.py)

**The vacuum-route lemma.** For C-even single-flux states, the second-order effective Hamiltonian contains the |0⟩-mediated route

    ⟨e_r| W R W |e_i⟩ ⊃ ⟨e_r|W|0⟩⟨0|W|e_i⟩ / (8/3 − 0) = (√2)(√2)(3/8) = +3/4

for every pair (i, r), adjacent or distant; it is absent for C-odd states since ⟨o|W|0⟩ = 0 (Theorem 6.3 untouched). For distant pairs it exactly cancels the free two-flux channel sum 2/(8/3 − 16/3) = −3/4, recovering the known vanishing of distant hops; for shared-link neighbors the cancellation is partial:

    t₊ = −481/612 + 3/4 = **−11/306**.

The manuscript's −481/612 is correct *as a channel sum* but incomplete as the hop. The manuscript's own §7 domino data adjudicate decisively: the C-even domino gap levels are diag-gap ± |t₊| with diag-gap 1879/3060, and {1769/3060, 13/20} forces |t₊| = 110/3060 = 11/306, not 481/612. The pipeline reproduces both §7 level sets exactly as gates.

**Corrected constants** (sign of t₊ unchanged ⇒ band minimum stays at k = 0):

    m₊(k) = 8/3 − y + [ 13/20 − (11/306)(12 + λ_S(k)) ] y² + O(y³)
    A₁⁺⁺ at k = 0:        −217/1020      (replaces −9397/1020)
    band top (λ_S = −4):   1109/3060
    curvature near k = 0:  +(22/459)|k|²  (replaces 481/459)
    bandwidth 16|t₊|:       88/153        (replaces 1924/153)
    E⁺⁺ at k = 0:           223/1020      (UNCHANGED)
    per-bond ratio |t−|/|t+|:  (5/612)/(11/306) = 5/22   [v2.2; replaces Remark 6.4's
        5/481 ≈ 1/96 — the immobility statement survives via the exact flat band
        (§8.1, and through O(y³) by §8.3), not via the ratio]
    manifold-width ratio (C-odd : C-even): (5/51)/(88/153) = 15/88   [v2.2; replaces 15/1924]

Untouched by the correction: Lemma 6.1; the channel split of −481/612; the diagonal vacuum subtraction +3/4 (a distinct, legitimate +3/4 from vacuum-energy bookkeeping — the likely source of the omission); the neighbor count 12; Theorem 6.3 and all C-odd results; the §7 table.

### 8.3 O(y³) tromino theorem

The externally supplied tromino-contract suite was audited: the contract is correct and was re-verified independently (ENGINE_TROM_tromino_contract_independent_check.py, 16 gates); cells 7–9 of the accompanying candidate-weight notebook were found wrong and discarded; the closed-form lift diagnostic for candidate weights was certified separately (ENGINE_TROM_tromino_candidate_closed_form_check.py), with advised default weights (0, 0, 0).

**Theorem (bare-link lemma).** Every O(y³) tromino weight vanishes; trominoes first activate at O(y⁴). Consequence: the third-order lattice effective Hamiltonian retains the second-order signed-adjacency structure — σ-covariance verified by the gate T₃(s) = −T₃(−s) — so the C-odd flat band at μ ≡ −4 remains exactly flat at third order, with uniform coefficient

    d₃ = 7/32 + 12·leak₃ − 4·b₃.

### 8.4 Exact d₃ and the C-even O(y³) extension (ENGINE_FLUX_su3_moments_ext.py 27 gates; ENGINE_FLUX_su3_domino_d3.py 251 gates)

The abstract domino — two independent Haar matrices (g₁, g₂) with H₀ = 2Cas⁽¹⁾ + 2Cas⁽²⁾ + cross(s), cross(s) = −Σ_a D_a⁽¹⁾D_a⁽²⁾ carrying the shared-link sign — is solved by exact des Cloizeaux perturbation theory to third order in a canonical word calculus (Cayley–Hamilton rewrites g² = χg − χ̄ + g⁻¹ keep all functions in an alternating-word basis of non-increasing degree; H₀ acts by exact Fierz surgery). Haar integrals come from the Layer-1 moment engine (Weingarten p = q ≤ 3 plus generic charge-±3 ε-projector blocks with exact pseudo-inverse Grams), itself gated against an independent Weyl-torus oracle. Resolvents are exact stacked rational solves with per-solve gates (consistency; coefficient-level residual ≡ 0; every kernel vector is the zero function). The des Cloizeaux formula H⁽³⁾ = −PWRWRWP + ½{PWR²WP, PWP} is validated by two *independent* single-plaquette implementations (word calculus and an irrep-basis spectral build with Jacobi–Trudi Schur characters), both reproducing the Bridge towers {13/20, 1/2} and {101/200, 7/32}, the vacuum series (−3/4, −9/32), and the level shifts (−1/10, −1/4).

Machine-exact domino constants (s-covariance and s-independence gated where required):

    b₃ = T₃ᵒ(s=+1) = 1975/124848        T₃ᵉ = −6335/249696
    D₃ᵒ = −24541/62424                   D₃ᵉ = −517313/6242400
    e₃ᵛᵃᶜ(domino) = −9/16  (= 2·(−9/32); no connected third-order vacuum diagram)
    leak₃ᵒ = (D₃ᵒ − e₃ᵛᵃᶜ) − 7/32 = −12331/249696
    leak₃ᵉ = (D₃ᵉ − e₃ᵛᵃᶜ) − 101/200 = −6335/249696

**Headline (Theorem 6.3′ material):**

    m₋(k) = 8/3 + y + (11/306) y² − (109151/249696) y³   for ALL k
    (d₃ ≈ −0.437135;  C-odd dispersive top: d₃ᵗᵒᵖ = −61751/249696)

**Exact identity (gated):** leakₙᵉ = Tₙᵉ at n = 2 and n = 3 — the diagonal's +3/4 (vacuum-energy bookkeeping) and the hop's +3/4 (the |0⟩ route) are distinct mechanisms with equal value, making the A₁⁺⁺ correction at k = 0 equal to within-tower + 24·Tₙᵉ per order.

**C-even at O(y³):** m₊(k=0) = 8/3 − y − (217/1020) y² − (54049/520200) y³; at λ_S = −4 the cubic coefficient is 471353/1560600.

The d₃ assembly contraction is validated by a gate showing the identical second-order contraction reproduces the known flat-band constant: 1/2 + 12(−11/306) − 4(5/612) = 11/306.

### 8.5 Gate ledger

ENGINE_FLUX_su3_moments_ext.py: 27 (oracle batteries; Weingarten sector; ε-blocks (3,0), (4,1) incl. ∫(trU)⁴trŪ = 3 with Inv(V⁴⊗V̄) rank 3, (1,4), (5,2); (6,0) intentionally unsupported with hard-fail guard — a degree census shows per-closure Grams cap at (4,1)/(3,3)). ENGINE_FLUX_su3_domino_d3.py: 251 (spectral checker incl. both Bridge towers; word-calculus structure incl. the four shared-link channel 2×2 blocks at both s reproducing Lemma 6.1; per-solve resolvent gates; vacuum predictions −3/2 and −9/16; full §7 reproduction; order-3 σ-covariance and s-independence; certificate locks on every exact constant). ENGINE_FLUX_glueball_band_certificate.py: 29. ENGINE_TROM_tromino_contract_independent_check.py: 19 in the deposited edition (16 at v2.0 writing). **Deposited total (v2.2): 326** (27 + 251 + 29 + 19), all run-verified June 11, plus ENGINE_TROM_tromino_candidate_closed_form_check.py (symbolic identity + 40-point battery). Corrected band edition (delivered): ENGINE_FLUX_glueball_band_certificate_v2.py, 36 gates. Document-level regression (in store): ENGINE_FLUX_master_v2_regression_certificate.py, 40 gates.

---

### 8.6 Gauss-law structure of the C-odd flat band; the O(y⁴) criterion (v2.6)

A delivered, independently constructed certificate (ENGINE_FLUX_cls_flat_band_certificate.py, uploaded 13/13; audited and sharpened to v1.1, 14/14) reframes the flat-band theorem from first principles — oriented plaquette boundaries only. (i) Ñ(k) + 4I = B(k)B(k)† with B the plaquette→link boundary symbol, so Ñ ⪰ −4 and the flat band is exactly ker B†: states with zero net signed amplitude into every link — a lattice Gauss law. (ii) The Levi-Civita-oriented boundary of one elementary cube is an exact zero-leakage real-space eigenvector at −4 (Bloch symbol u(k) = (−sin k₂/2, −sin k₀/2, sin k₁/2) in its convention), and flatness is ∂₂∂₃ = 0, gated on all twelve cube edges. (iii) Exact completeness (v1.1, gate G09b): on the L³ torus, dim ker(Ñ+4I) = L³+2 = (cube states, rank L³−1, single relation Σψ = 0) ⊕ (three k = 0 rest states, Ñ(0) = −4I) — correcting the band certificate's attribution parenthetical (§8.1 erratum). (iv) Robustness theorem (the new content): any correction whose symbol factors through the link channel, B M B†, annihilates the flat subspace for arbitrary M — exact flatness with unshifted hopping energy at every link-mediated order, subsuming O(y²) and structurally explaining why tromino vanishing preserved O(y³); the sharp O(y⁴) criterion is u†H₄P_⊥ ≡ 0, and the minimal corner-sharing symbol provably fails it (gate G12), so geometry alone cannot protect the band once trominoes activate (§6.12 re-cut). (v) tr(Ñ+4I) = 8Σ_a sin²(k_a/2), re-deriving the band edges [11/306, 41/306]. Audit record: novelty split as in the v2.6 changes; the two Bloch conventions (this certificate vs ENGINE_FLUX_glueball_band_certificate.py) verified characteristic-polynomial-equivalent; both sectors factorize, with det N = −2v₁v₂v₃ (C-even, kernel only on zone faces) versus det Ñ ≡ 0 (C-odd) as the qualitative dispersing/non-dispersing asymmetry. Companion: RUN_FLUX_cls_flat_band_results.md v1.1.

---

## Appendix A: notebook-by-notebook inventory

| Notebook | Program | Contents and key recorded outputs |
|---|---|---|
| GOODRESULTS1 (14 cells) | A | SU(3) c1 in depth: q4 = −1/576, q6 = 19/1244160; Richardson c1 ≈ −0.0826544; Weyl-invariant operator derivation (H1 = −p2²/96; H2 = √6(p2³/11520 + p3²/8640)); exact resolvent; shell-8 suite (ρ(T) = 0.5502) locking c0, c1; **cell 12**: exact invariant ledger Δ_res = −205√6/3072, Δ_H2 = 19√6/576, c1 = −311√6/9216, residual 0, with the radial-misses-p3² structural conclusion |
| GOODRESULTS2 (8 cells) | A (+ side thread) | Fixed-branch exact c1 (ground → p2 shell, not p3); exact radial Casimir diagnostic (Δ_rad χ(p,q) = −C2(p,q)χ — no missing metric); cells 4–7: finite-channel polymer-resolvent thresholds (weak-coupling multi-plaquette locality diagnostic using H1 amplitudes 5/24, √10/48, 7√10/48, √5/16; ρ_chan = 0.550162) — a third thread, in neither the manuscript nor Program B |
| GOODRESULTS3 (1 cell) | A (+ SU(2)) | Symbolic q4 = −1/576; SU(2) hard-edge boundary-strip constants √2/(2√π), √2/(3√π) (outside manuscript scope); Peter–Weyl scan to β = 10⁶: fits 0.816496580887 / −0.312499956 / −0.082659570 / c2 ≈ −0.0512314 |
| GOODRESULTS4 (1 cell) | A (+ SU(2)) | Earlier version of GR3 without the residual fits |
| GOODRESULTS5 (8 cells) | B (0–4) + A (5–7) | Green-kernel decay fitter and Hodge capacity envelope (B); SU(3) sanity and SU(4) scans (A): corrected M-scaling confirms √(β/2) − 29/64, residual −6.73×10⁻³ at β = 1000; cell 5's c4 ≈ 7/16 superseded |
| Untitled206 (26 cells) | A | Weyl-triangle solvers (CPU pathology then converged GPU runs, c1_eff → −0.0843 at β = 1024); **cell 12** character-basis confirmation (K-gate at β = 3200, fits c0/c1/c2, radial foil rejected at ≈8500×, harmonic ladder); cells 13–15 SU(7) K-sweeps (foil separation 1.07×10⁻², truncation-limited); **cells 16–17** exact rational c1(N) engine (q(3) = −311/9216, q(4) = −1193/16384, q(6) = −6953/36864, conventions H1 = −P4/48, H2 = √(N/2)P6/1440); cell 20 mod-p N = 7 test (interrupted); cells 22–25 symbolic cut–join engine toward c2(N) (truncated) |
| Untitled185 (8 cells) | B | PMBSF v3b firewall: all SAFE, θ_phys p99 = 0.8541; v4 Mosco verifier, sanity PASS |
| Untitled193 (4 cells) | B | A′ spike audit (route does not close; Bernoulli comparator consumes budget); trace-weighted audit (WEAK); v13/v14 Matrix-Stein η audits |
| v16_MATRIX_PASS (3 cells) | B | Wilson-vs-random matrix-Laplace transfer: PASS p ≤ 0.003 through L = 24 (max Δ_ML = 0.0180), FAIL p = 0.01 at θ = 64; ratio diagnostics 1.008–1.035 |

## Appendix B: store and delivered certificate corpus (v2.1)

Run status refers to the June 11 audit pass; presence without a run log confers no status, and store files not listed here were not audited in this pass.

| Artifact | Tier | Covers | June 11 run status |
|---|---|---|---|
| ENGINE_SUN_codd_local_gap_exact.py | store | Exact Wick C-odd engine: c0−(N), c1−(N) closed forms | PASS, N = 3–12 (c0−(3) = −3/8, q−(3) = −551/13824) |
| su3_odd_gap.py | store | Numerical C-odd consistency at N = 3 (header: verified N = 3–12) | present; not re-run |
| SU_N_C_odd_appendix.tex; Finite_Wick_Certificate_for_the_SU_N__C-odd_Local_Gap.docx | store | Odd-sector derivation write-ups (carry the c1− closed form) | documentation |
| c2_certificate.py | store | Exact third-order RS: c2+(N) even N = 6–12, c2−(N) N = 7–13; c0/q1/qres gated en route | PASS (all rows True, both sectors); instrumented driver (v2.3) prints exact q1(6, 7, 8) = −6953/36864, −13271/50176, −23081/65536 |
| n7_c1_discrimination_certificate.py | delivered (v2.3) | Independent route-B engine for §6.2: dual moment engines cross-gated, exact G–S shell basis, second-order RS; decides q1(7) and proves the c1+ closed form identically in N and at every N = 3–12 | 18/18 |
| c2_residual_ranks_certificate.py | delivered (v2.4) | Route B at third order, both sectors: loop-equation moment recursion (degree 18), Pochhammer gates, rank-reduced G–S; decides c2± at the residual ranks and re-derives the full c2 table N = 3–12 | 16/16 |
| c2_residual_ranks_routeC_storefix.py | delivered (v2.4) | Route C: store cut–join engine under an exact Schur rank filter (in-memory patch; store file untouched); residual-rank decisions cross-pinned to route B | 13/13 |
| PAPER_FLUX_manuscript_section6_patch.tex (+ compiled .pdf) | delivered (v2.5; refined v2.6) | Seven paste-ready §6 blocks: Lemma 6.1′, corrected Theorem 6.2 and Remark 6.4, Theorems 6.3′/6.3′′ (v2.6: L³+2 decomposition sentence added), global relabeling list, Appendix A additions; constant provenance table included | constants whitelist-verified; 12 assembly identities re-checked; compiles standalone (4 pp.) |
| ENGINE_FLUX_cls_flat_band_certificate.py (uploaded) | delivered (v2.6) | CLS/Gauss-law certificate v1.0: factorization, cube CLS, robustness criterion, corner-sharing sharpness | 13/13 as uploaded; two audit findings (G10 precedence; k = 0 span overclaim) |
| ENGINE_FLUX_cls_flat_band_certificate_v1_1.py; NOTE_FLUX_cls_flat_band_results_v1_1.md | delivered (v2.6) | Post-audit edition: G10 count gated, G09b exact torus completeness (29 = 26 + 3 at L = 3), G11 reworded, novelty split and C-even-factorization correction in the note | 14/14 |
| glueball_flat_band_paper_v0_1.tex (+ compiled .pdf) | delivered (v2.7) | Standalone theory paper, 10 pp.: corrected leakage with adjudication, Gauss-law/flat-band/CLS/C-even band theorems with the L³+2 decomposition, third-order rigidity, robustness + pre-registered O(y⁴) criterion + all-orders conjecture, numerical table, verification and domino appendices | constants whitelist-verified; 15 assembly identities re-checked; compiles standalone |
| su3_exact_c2.py | store | SU(3): c2+ = −5665/110592, c2− = −53/864, both c1 q's | PASS (4/4) |
| gue_shell_calculus_verifier.py (+ gue_shell_calculus_module.tex/.pdf) | store | α_N, γ_N, c0+(N) exact N = 3–12; SU(3) anchor ρ₃ = 0.5501615335…, T entries {5/24, √10/48, 7√10/48, √5/16}, Perron quartic λ⁴ − (215/768)λ² − (175/13824)λ + 25/294912; large-N ρ_rad asymptotic | PASS ("ALL REQUESTED CHECKS PASSED"); ρ₃ reconciles GR1 shell-8 ρ(T) = 0.5502 and GR2 ρ_chan = 0.550162 |
| SU3_d3_corrected_full_notebook.ipynb (+ _EXECUTED copy) | store (v2.2; hash-matched) | §8 core: writes/runs ENGINE_FLUX_su3_moments_ext.py (27) + ENGINE_FLUX_su3_domino_d3.py (251); emits RUN_TROM_d3_results.json | kernel-executed; 278/278 |
| ENGINE_FLUX_su3_moments_ext.py; ENGINE_FLUX_su3_domino_d3.py (standalone deposits) | store | Standalone copies of the notebook-embedded scripts | moments hash-identical; domino differs only in the authoring JSON write path /home/claude/review/ (notebook copy canonical) |
| RUN_TROM_d3_results.json | store (two identical copies) | 21 exact constants, orders 2–3, corrected C-even block included | byte-identical across notebook and standalone runs; sha256 d2d653b4… |
| CERT_FLUX_d3_certificate_results.md | store | §8.4 results note (d₃, Theorem 6.2 correction) | documentation |
| ENGINE_FLUX_master_v2_regression_certificate.py | store (v2.2; hash-matched) | 40-gate document regression: §3 arithmetic 3.1–3.15, §§6–8 web, Bloch curvature | 40/40 |
| ENGINE_FLUX_glueball_band_certificate.py; glueball_band_results.md | store | O(y²) band theorem, as-written C-even pins | 29/29 (June 11 deposit audit) |
| ENGINE_FLUX_glueball_band_certificate_v2.py; NOTE_FLUX_glueball_band_results_v2.md | delivered (v2.2) | Corrected band edition: §8.2 hop throughout; provenance gate for −9397/1020; six-field RUN_TROM_d3_results.json cross-check; corrected results note | 36/36 |
| ENGINE_TROM_tromino_contract_independent_check.py | store | O(y³) tromino-contract verification | 19/19 (deposited edition; deps: primitives colocated, weight cards at /home/claude/review/) |
| ENGINE_TROM_tromino_candidate_closed_form_check.py | store | Closed-form lift diagnostic; α(k) identity, extrema 8/3 (axes) and 8/27 (R) | PASS (symbolic gate + 40-point battery) |
| ENGINE_FLUX_su3_haar_tromino_primitives.py/.json; ENGINE_TROM_tromino_o3_su3_weight_cards.py/.json | store | Moment primitives and weight-card data consumed by the contract check | dependency/data; loaded successfully in the contract run |
| ENGINE_TROM_su3_o3_tromino_weight_extractor_v1.py / _v1_1_colab_fixed.py; ENGINE_TROM_tromino_o3_candidate_lift_diagnostic.py; ENGINE_TROM_tromino_weight_constraint_certificate.py | store | §8.3 provenance suite (the externally supplied extractor whose cells 7–9 were discarded; auxiliary diagnostics) | present; not load-bearing, not re-run this pass |
| PAPER_PMBSF_master_one_plaquette_bridge.pdf; …_1.pdf | store | Manuscript, two editions (11- and 12-page) | Appendix B b-block extracts cleanly and identically from both (§6.4) |
| two_sided_gap_and_glueball_estimate.md | store | Working note (June 11) | present; not audited this pass |
| MASTER_one_plaquette_program.md (v1.0); …__1_.md (v2.0) | store | Prior editions of this document | superseded by v2.2 (v2.1 delivered) |

*End of master document.*
