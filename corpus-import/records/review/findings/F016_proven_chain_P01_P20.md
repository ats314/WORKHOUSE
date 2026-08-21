# F016 — Unit #7: proven chain P01–P20 (+ F002/F014 convention cross-checks)

**Date:** 2026-06-12 · **Unit:** `E:\YANG\ORGANIZED\01_PROOFS\proven\` (21 P-docs + README/MANIFEST, 3,244 lines; source: infrared-glenn/CLEAN/01_PROVEN, copied 2026-03-29). Read: full — P02, both P04s, P07–P13 small set, P15–P20; structural (YAML + theorem skeleton) — P01, P03, P05, P06, P14. Cross-checked against `CLAUDE_REVIEW/01_MASTER_ASSESSMENT.md` + `03_CRITICAL_GAPS.md` (frozen April pass).

## 1. Layer profile

Nov 21–22, 2025 era; several docs authored "Manus AI". Status discipline is *mixed by document*: honest self-labels in P07 (CONDITIONAL, "Prong C heuristic"), P11 (SKETCH, "core difficulties of the Millennium Problem" named), P14 (CONDITIONAL), P15 (STATEMENT); but P12/P13/P16/P17 carry **status: PROVEN / "Rigorous Proof" headers over visibly qualitative or assumption-smuggling steps** (detail in §3).

## 2. The assigned F002 cross-check — ANSWERED

Both January Synthesis_01 CRITICALs have direct counterparts in this layer. Timeline correction: the P-docs (Nov 2025) **predate** the January audit — the right verb is *present at origin*, not "propagated into."

**(a) Mode A/B reference-measure mixing — CONFIRMED, structural.** The two P04 files realize the Haar contribution in two inequivalent bookkeepings: `P04_haar_geometry_supplement.md` works on the curved product manifold (dvol_g, Ric_g = κg > 0, mass = κ + βc_W on horizontals), while `P04_haar_mass_mechanism.md` + `P12` work on **flat ℝ^M with Lebesgue dA, Ric = 0**, recovering positivity entirely from the gauge-fixing penalty S_FP (σ_A = Ng₀²a²/6 = Hess of a chosen quadratic penalty; P12 §3.1 states "Ric = 0" explicitly). Both are status PROVEN; no reconciliation document exists in proven/. Whether κ-vs-σ_A double-counts or merely re-coordinatizes is **Alex's call** — but every downstream consumer (P07's σ decomposition, P10's c₀, P20's bridging proposition) cites these interchangeably.

**(b) One-sided/sign Hessian bound — CONFIRMED.** P04_mass §2.2 and P12 §3.3 assert Hess(S_W) ≥ 0 globally from near-minimum convexity of 1−cos, with the actual restriction acknowledged only parenthetically ("restricted to the first Gribov region (where the measure is concentrated)"). The boxed theorems drop the restriction. Same pattern the January audit flagged in Synthesis_01's SAFE bound.

**Attestation status:** both issues are now triple-attested — Nov origin (this read), Jan audit (F002), April review (01_MASTER_ASSESSMENT line 505 lists "P09 (unjustified formula), P13 (unjustified formula), P16 (a-uniformity), P20 (σ_A > 0)"; 06_DEEP_MATHEMATICS line 248: "Tightness argument is CIRCULAR") — and remain unrepaired in the originals. That's by design (archive read-only), but any future consumer of proven/ must route through CLAUDE_REVIEW's grades, not the docs' own headers.

## 3. Concordance check of the April review — PASSED (independent reproduction)

Reading blind-first, then comparing: my trouble list matches the April review's item-for-item. Highlights this read adds texture to:
- **P13** (status PROVEN, "Rigor A" first-pass, later DOWNGRADED to B/C in the same assessment): §3.3 contains a visible derivation-flailing loop — **five successive inequivalent formulas** for [X,Y]_V, with self-talk ("This is not quite right", "Let's use the simplest formulation", and finally *"This seems to be the consensus in the physics literature. Let's proceed with this, assuming it can be derived from first principles"*). The load-bearing step of H1 is assumed mid-proof. April's GAP-B/GAP-M record the Gribov-horizon unboundedness; the flailing loop itself is worth seeing raw.
- **P16** (PROVEN): Step 1 smuggles the open uniformity — "This holds uniformly for all a because ρ_a → const in the scaling limit" — which is precisely OP-4/CONJ_B territory; concords with April's GAP-L + circularity note. P16-as-PROVEN vs OP-4-as-open is a standing status conflict resolved in CLAUDE_REVIEW's favor by the live docs.
- **P17** (PROVEN, "H2"): Tr(𝒦_t) = 0 justified by a one-liner ("redistributes energy without changing the total trace... 𝒦 operator is traceless") — qualitative load-bearing step, F005 genre.
- **P09**: internal tension — Thm 3.1 claims M positive definite on physical modes, while its own §4.1 table shows toron zero modes of H_W lifted only by the Haar mass c₀ (= 4/3 at SU(3)). April: "unjustified formula." Consistent.

## 4. New observations (not found in the April layer)

1. **P07 vs P12 prong-taxonomy mismatch:** P07 defines Prong A = Haar positivity, B = asymptotic freedom, C = correction subdominance; P12 titles itself "Prong C" but its conclusion defines A = direct lattice calc, B = perturbative continuum, C = functional-inequality — two incompatible taxonomies for the same trilogy. Citation hazard when quoting "Prong C is proven."
2. **P04_supplement is an unlabeled conversational deliverable** — no YAML header, ends mid-dialogue ("If you want this written as a LaTeX lemma… I'll draft it next."). It sits in proven/ as if status-bearing; the April Pass-12 audit list names "P04" once (likely the mass-mechanism file). Hygiene flag.
3. **F014 factor-2 metric-trap check (assigned): the trap is live across layers.** P04_supplement pins ⟨·,·⟩ = −Tr (trace convention); P09/P10's c₀ = (N²−1)/2N = 4/3 at N=3 matches C₂(fund) in the **Casimir** convention; the one-plaquette program (master doc C.0) and the OP-12 θ-runner (α_W = β/6) use Casimir. No proven/ doc carries a C.0-style metric preamble. **Any cross-quotation of chain constants (κ, c₀, σ_A) against program constants must carry the factor 2** — recommend a one-page convention ledger in THEORY/theory/ if such cross-quotation starts happening (Alex's call).
4. **Possible lineage of the OP-12 comparator mass:** P04/P12's explicit value ρ = Ng₀²a²/6 = **0.5** at N=3, g₀=a=1 numerically coincides with the θ-scan's m₀² = 0.5. If intentional, worth one provenance line in `numerics/op12_theta/`; if coincidence, also worth knowing.
5. **P19's convexity condition is loose-but-conservative** (states m₀² − 2dκ ≥ ρ* although its own Hessian display has the hopping term entering positively); harmless, noted for the Lean shadow (P19 is the scalar prototype the Jan Lean repo formalizes).

## 5. Connections

P08 (C-sectors) is the clean foundation the flat-band program builds on (OP-14 context) — solid as written. P06's ODE content is what the Lean layer shadows (F008: "Riccati = root algebra"); P06 itself is honest about scope at the structural level read here. P18+P20 form the polarity/maximum-principle pair feeding CONJ_C. P03 (strong-coupling transfer-matrix gap) is the chain's anchor and pairs naturally with the one-plaquette program's exact strong-coupling spectroscopy.

## 6. Verdict (one line)

Layer read; both F002 CRITICALs confirmed present-at-origin (Mode A/B = the two P04s; one-sidedness = P04/P12's global Hess(S_W) ≥ 0) and now triple-attested-unrepaired; April review independently reproduced (concordance PASS — route all consumption through CLAUDE_REVIEW grades, not the docs' own PROVEN headers); new: prong-taxonomy mismatch, unlabeled P04 supplement, live factor-2 trap across layers, m₀² = 0.5 lineage question.
