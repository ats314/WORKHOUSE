# F019 — Unit #10: 02_APPENDICES survey (blue/green/brown/red)

**Date:** 2026-06-12 · **Unit:** `E:\YANG\ORGANIZED\02_APPENDICES\` (~52 files). Method: delegated reconnaissance (per-file inventory + targeted convention greps), synthesized against F002/F016/F017 context. Deep reads split to #10b/#10c/#10d.

## 1. What the four colors are

- **brown_sections/** — the substantive layer: main-text section extracts (§1–§12, .txt, 600–1,600 lines each) + formatted appendices B/D/I/J + `NOTATION_AND_CONSTANTS.md` (476-line constants index) + `EXTERNAL_INPUTS.md` (every external result used-not-reproved, with a [CORE]/[OPTIONAL]/[CONDITIONAL] taxonomy — the most disciplined status practice seen outside the one-plaquette program).
- **blue/green_appendices/** — two successive editions of appendices A–H (.txt; only admin .md present); covers RP, OS axioms, boundary compression, Lyapunov drift, Green-kernel decay, Combes–Thomas, Davies decay.
- **red_propositions/** — 8 precision extracts: Davies-type decay for the massive Maxwell Green kernel (m²I + αd₁*d₁)⁻¹ with row-sum constants C₀/C_∂ replacing the global degree D_E.
- **Era hypothesis (recorded, not asserted):** structure matches F006's anatomy of the 23.5K-line Comprehensive manuscript (main sections + two appendix editions) — 02_APPENDICES is plausibly that manuscript disassembled; blue/green = its two appendix editions. Check in #10b/c.

## 2. Convention findings (the F002/F016 cross-check — major, and GOOD news)

1. **The brown layer parametrizes the metric instead of fixing it:** ⟨X,Y⟩_λ := λ(−Tr(XY)), λ > 0 explicit; representation constant λ_ρ; Maxwell stiffness **α := β/(nλ_ρ)**. This subsumes both corpus conventions (λ_ρ = 1 → trace, α = β/N; λ_ρ = 2 → Casimir, α = β/2N — the OP-12 runner's β/6 at N=3) and is immune to the factor-2 trap by construction. → deposited as a DOC_GOV_conventions.md row; `NOTATION_AND_CONSTANTS.md` is the brown-era source of truth.
2. **The Mode A/B reconciliation that proven/ lacks EXISTS here:** §3.1 Lemma 3.8 proves dvol_g = normalized Haar, and every Bakry–Émery statement in brown (§5.1, §6.1, §12.1) consistently uses dμ = Z⁻¹e^{−S}dvol_g — Mode A throughout, with the equivalence to the Haar description proven rather than assumed. The clean curvature statement is §5.1's hinge inequality: Ric_μ ⪰ c_H/2·I + (β/nλ_ρ)d₁*d₁ with c_H = κ_G (Einstein identity noted §10.1: Ric_G = κ_G g_G). **For master-paper purposes, the brown layer — not the two P04s — is the right citation target for the curvature mechanism**, subject to the #10b deep-read confirming the locality discipline (the hinge is stated at the vacuum linearization; whether the small-field restriction is carried honestly through §5.1's 1,605 lines is the open check — the strings "one-sided/Gribov/SAFE" are absent, which is *not* the same as the issue being absent).
3. Constants present: κ_G, c_H (= κ_G, semisimple), m² := c_H/2, α, λ_ρ, Lyapunov κ, R_W(r). **Absent: c_W, σ_A, (N²−1)/2N** — the proven/-era constants don't appear; the brown layer is its own regime.

## 3. red_propositions ↔ OP-1/OP-7 (live-bottleneck relevance)

The red extracts are Davies-decay statements for exactly the OP-1 comparator M = m²I + αd₁*d₁: Prop 9.X (Davies decay for the massive Maxwell Green kernel), 9.X′ (row-sum constant C₀ in place of D_E), 9.X″ (boundary constant C_∂), with the row-sum definitions. OP-12 Addendum 2 recorded that the OP-7 CT chain is ~10⁵–10⁶ loose in the q → 1 regime and "the analytic route needs … a sharper-than-HS argument" — **row-sum Davies decay is a candidate sharper toolkit, sitting unused in red_propositions/.** Deposited: OP-7 addendum line in OPEN_PROBLEMS + pointer for the OP-1 dossier. Cross-read vs the exact-kernel ledger (does Davies-with-C₀ close any of the 3×10⁵ kernel-estimate slack?) = **#10d, P1-priority**.

## 4. Splits queued

- **#10b** — brown core deep read: §3.1, §5.1, §10.1, §12.1 + NOTATION + EXTERNAL_INPUTS (~5K lines; carries the F002 locality check and the era identification).
- **#10c** — blue/green A–H .txt inventory + read (two editions; diff them).
- **#10d** — red Davies props vs `numerics/op12_theta` kchain ledger + OP-7 re-pointing (feeds the live campaign; do first).

## 5. Verdict (one line)

The appendices are the corpus's cleanest convention regime (λ-parametrized metric; dvol_g = Haar proven; hinge inequality Ric_μ ⪰ c_H/2 + α d₁*d₁) — the right curvature-mechanism citation target pending the #10b locality check; red_propositions holds an unused sharper-than-CT decay toolkit aimed at OP-7's known 10⁵–10⁶ slack (#10d, P1); blue/green = two appendix editions, likely the Comprehensive manuscript disassembled.
