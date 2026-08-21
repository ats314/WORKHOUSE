# F018 — Unit #9: cmi_review_package

**Date:** 2026-06-12 · **Unit:** `E:\YANG\ORGANIZED\01_PROOFS\cmi_review_package\` (67 files). Method: hash-comparison against clay_submission for the shared corpus; full read of the unique layer (README_REVIEWERS, 00_CORE_HYPOTHESES, theorem-skeletons of 01/02/03/04 sections, 434 lines).

## 1. Composition

- **Shared with clay_submission, byte-identical (sampled + spot-set):** PROOF_01–12, the three PROOF_REVIEWs, PHYSICS_REFEREE pair, EVIDENCE_01, MANUSCRIPT tex, all three CODE/VERIFY scripts. The package is clay_submission **plus a five-document reviewer-facing reduction layer** (`cmi_review_sections/`: 00_CORE_HYPOTHESES, 01_MEASURE_EXISTENCE, 02_MOSCO_STABILITY, 03_GEOMETRIC_FLOW, 04_MASS_GAP_THEOREM + README_REVIEWERS; Dec 8, 2025).
- **Correction to F017:** my claim that clay_submission's root and reviews/ editions of CMI_PEER_REVIEW.md differ was a shell-pipeline artifact — **they are byte-identical** (9fe5a463…). F017 annotated; ledger #8 row and CHAIN_STATUS_MAP fixed; #8b re-scoped (drop the diff item).

## 2. The substantive delta: TWO different "single axioms" named H1

| Package | "The single assumption H1" | Live-language location |
|---|---|---|
| clay_submission (per Apr deep-read Part 3/8) | **Tightness / mGH convergence** of μ_a | OP-4 |
| cmi_review_package (00_CORE_HYPOTHESES) | **Uniform lattice LSI**: Ent_{μ_a}(f²) ≤ 2ρ₀⁻¹ℰ_a(f,f) uniformly in a and volume | OP-2's level (uniform coercivity); strictly **stronger** than tightness — 01_MEASURE_EXISTENCE *derives* tightness from it via Herbst |

**Citation hazard (deposited to CHAIN_STATUS_MAP):** "the proof rests on a single assumption" appears in both packages with different referents. Any master-paper sentence quoting "H1" must name which one. The LSI form also carries heavier physical claims in 00_CORE_HYPOTHESES ("absence of Gribov horizon in the support; absence of vacuum SSB") — stated as *physical meaning*, not proven.

## 3. Status structure of the unique layer (described, not judged)

- 00_CORE_HYPOTHESES: "**ONE (1)** Core Hypothesis remaining"; uniqueness + gauge-independence claimed derived from LSI structure (Holley-Stroock / Gross cited).
- 01/02/04: conditional derivations from H1 — E1 tightness, E2 uniqueness (ergodicity via LSI), E3 closability; Mosco lemmas A/B/C/D1/D2/D5; OS1 reflection positivity **restricted to the physical subspace** (their stated answer to the gauge-fixing-breaks-RP problem: reconstruct only on Wilson-loop algebra), OS2 reconstruction, gap = ρ₀. April master assessment graded 01_MEASURE_EXISTENCE "A — rigorous construction" *as a conditional*.
- 03_GEOMETRIC_FLOW: claims to **derive H1** ("While Proofs 01–02 assume H1 as an axiom, this section derives H1 from the geometry of the action") via the PBH flow — Lemma G4 "If ℛ(0) > 0 (Haar/Wilson Dominated) then ℛ(t) > 0 for all t" is the same one-sentence global-positivity step as PROOF_11's G4 (F017 §3.1), i.e. CONJ_B-shaped. README_REVIEWERS is honest about this: the flow argument is "*suggesting* H1 holds… for the strictest mathematical standard, H1 can be viewed as the Single Remaining Axiom."
- README_REVIEWERS' three reviewer instructions (verify uniqueness derivation; verify exact locality in PROOF_08; assess the reduction to H1) are a fair map of where the weight sits.

## 4. Cross-links

The H1(LSI) formulation is the direct ancestor of OP-2 (★, the master inequality) in the live taxonomy; the clay H1(tightness) maps to OP-4. The dependency OP-2 ⇒ OP-4 recorded in OPEN_PROBLEMS matches the package's internal logic (LSI ⇒ Herbst ⇒ tightness). G4's "Haar/Wilson dominated" persistence is another instance of the CONJ_B single-sentence pattern (third sighting: P07 Prong B/C, PROOF_11 G4, 03_GEOMETRIC_FLOW G4). RP-on-physical-subspace (04 §1) is the same move OP-5 confronts honestly in the live list.

## 5. Verdict (one line)

cmi_review_package = clay_submission + a cleaner reviewer-facing reduction whose axiom is uniform LSI (≠ clay's tightness — two H1s, citation hazard now in CHAIN_STATUS_MAP); its H1-derivation section reproduces the familiar one-sentence CONJ_B step; README_REVIEWERS is the honest framing; F017's CMI-editions claim corrected (identical, shell artifact).
