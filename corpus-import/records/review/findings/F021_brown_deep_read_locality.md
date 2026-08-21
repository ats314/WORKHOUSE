# F021 — Unit #10b: brown deep read — the locality check passes; gaps are named, and they map onto the quarantined trio

**Date:** 2026-06-12 · **Unit:** `02_APPENDICES/brown_sections/` core. Coverage: §5.1-file (1,606 ln) read in full; §7 statement-level + §7.3.4 and closing assembly verbatim; §6.1 skeleton + hinge restatement; §3.1/§10.1/§12.1 targeted; NOTATION_AND_CONSTANTS + EXTERNAL_INPUTS in full. Era-ID delegated (mechanical string-probing). Carries the F002/F016 cross-check (one-sidedness; Mode A/B) and the F019 "pending locality check."

## 1. Era identification (settles F019's hypothesis)

**All 18 brown files, and all probed blue/green files, are verbatim-present in `03_MANUSCRIPTS/Comprehensive_Yang_Mills_Mass_Gap_Proof.tex` (23,528 ln).** 02_APPENDICES = the Comprehensive manuscript disassembled; blue/green = two appendix editions (green refines/expands blue per sample diffs). Consequence: **citing brown = citing the manuscript** — the manuscript's embedded Dependency Ledger (F006) and its conditional final theorem govern any brown quotation.

## 2. The locality check — PASSES (descriptive verdict)

The F016 pattern (global Hess(S_W) ≥ 0 boxed from near-minimum convexity) is **absent from brown**. What brown actually does:

1. **Vacuum identity** (§5.2, Prop 5.8): ∇²S_W(U⁽⁰⁾) = (β/nλ_ρ)d₁*d₁ — exact, at the vacuum only; kernel honestly = ker(d₁) incl. harmonic sector.
2. **Hessian stability** (§5.4, Lemma 5.19): ∇²S_W(U) ⪰ ∇²S_W(U⁽⁰⁾) − R_W(r)·I **only for U ∈ K_Λ(r)** (linkwise small-field region, Def 5.11, explicitly not gauge-invariant by design), R_W(r) = (β/n)(2νM₃(r_⋆))r.
3. **Localized hinge** (Prop 5.21/Cor 5.22): Ric_μ ⪰ (c_H−R_W(r))I + (β/nλ_ρ)d₁*d₁ **on K_Λ(r)**, with the quantitative radius condition (5.33): R_W(r) ≤ c_H/2 ⟺ **r ≤ c_H n/(4βνM₃)** — i.e. the validity radius shrinks like **O(1/β)** (stated in §6.1: "r … may be taken O(β⁻¹)").
4. **Local functional inequalities** (§5.5, §6.1): Poincaré/LSI on Ω_Λ(r) ⊂ K_Λ(r), Neumann-conditioned; HS/Brascamp–Lieb covariance bound via M_{m(r)} = m²(r)I + αd₁*d₁ — all explicitly local; Remark 5.31 records why the scalar bound is deliberately not used.
5. **Local→global** (§7): Foster–Lyapunov assembly that is **explicitly conditional**: "**Assumption 7.38 (coercive pairing inequality; open input)**" — 𝒫_Λ(U) ≥ c_pair𝒟_Λ(U) − C_pair, all Λ, all U — with the closing assembly stating "the only model-dependent obstruction being the coercive pairing inequality, Assumption 7.38," and the LSI route flagged separately: "the SPI ⇒ LSI conversion is treated as an external input unless proved explicitly (one of the 'referee-facing gaps')."

Also honest at the linear-algebra layer (§3.4): no volume-uniform positive lower bound for d₁*d₁ on im(d₁*) (smallest nonzero eigenvalue O(L⁻²)) — recorded as exactly why the Haar mass c_H is needed.

**For master papers:** cite brown for the *mechanism* (vacuum Hessian identity; localized hinge; matrix-not-scalar HS argument) with the locality hypotheses attached (U ∈ K_Λ(r), r = O(1/β), R_W(r) ≤ c_H/2). Never quote a brown global statement unconditionally: global Poincaré is conditional on Assumption 7.38; global LSI additionally on SPI→LSI.

## 3. Bonus result — the quarantined trio maps 1:1 onto brown's named open inputs

| Quarantined (theory/under_review, F005/F006) | Brown-layer named gap | Exact target |
|---|---|---|
| PROOF_13 Pairing-Term Coercivity | **Assumption 7.38** (coercive pairing inequality; open input) | inequality (7.60) |
| PROOF_14 SPI→LSI Localization | **EI-SPI-LSI** ([OPTIONAL/FLAGGED] external conversion, Part 8.3) | profile-matched SPI⇒LSI theorem |
| PROOF_15 Reflection-Equivariant RG | **EI-RG-RP** ([CONDITIONAL] continuum architecture, §12.1 (C1)–(C3)) | RP permanence along a_n ↓ 0 |

This sharpens Alex's adjudication packet (STATE item 2): each trio doc claims exactly one named brown assumption; the assumptions' verbatim statements are now located. (EXTERNAL_INPUTS' closing line routes remaining gaps to the manuscript's DEPENDENCY_LEDGER [GAP] entries — consistent with F006.) **Verified at content level on both ends (verification pass):** PROOF_13 §13.1 opens "Resolving the Part 7.3 Coercivity Gap… Dependency Ledger (Gap 1, Part 7.3)" with 𝒫_Λ = ½⟨∇S_W, ∇V_Λ⟩ — identically brown's (7.58) since ∇V_Λ = Σ_p z̃_p∇z̃_p; PROOF_14 names "the [GAP] listed in Part 8.3… SPI → Uniform LSI conversion"; PROOF_15 names "the final remaining logically flagged assumption from the Dependency Ledger (Part 12)" with reflection-equivariant block-spinning along a_n ↓ 0. The Ledger's three gaps ≡ {A7.38, EI-SPI-LSI, EI-RG-RP} — F006's "3 gaps" now have brown-layer names.

## 4. Convention/constants notes

NOTATION_AND_CONSTANTS fixes: λ_ρ; c_H ("scalar mass… ultimately determines **m² = c_H/2**"); α := β/(nλ_ρ); M = m²I + αd₁*d₁, ‖M⁻¹‖ ≤ 1/m²; and a CT block (§G) whose decay rate η = (1/R)log(1 + a₀/2B) **already uses the off-diagonal row-sum constant B** — the kchain ledger's q_CT convention is exactly this block (lineage confirmed); the red extracts' incremental content relative to brown is the Davies (arcosh) rate only, not the row-sum idea (refines F020 §1 framing; F020's computations unaffected). Lineage candidate for F016's open question: OP-12's m₀² = 0.5 ↔ brown's m² = c_H/2 under a c_H = 1 normalization — recorded, not asserted. Era note: §10.1 contains second-person chat-voice remnants ("you even get…") amid formal statements; Einstein identity Ric_G = κ_G g_G stated there for compact simple G, metric ∝ −Killing. §12.1 contains no reference-measure statements at grep level (no Mode-B leak found; RP permanence is architecture-conditional via EI-RG-RP).

## 5. Residuals → #10c

Blue/green edition ordering + content diff (subagent sampled 3 pairs; full diff pending); §8.1/§9.1/§11.1 unread at depth (statement-level only via EXTERNAL_INPUTS' internal-proof list).

## 6. Deposits

DOC_GOV_conventions.md hinge row resolved (locality confirmed + exact hypotheses); CHAIN_STATUS_MAP §2c updated (brown rules firm; trio mapping added to §2 item 4); theory/under_review/README.md gains the 1:1 mapping; STATE (header, Under-review, items 2/3); ledger #10b → DONE; SESSION_LOG.
