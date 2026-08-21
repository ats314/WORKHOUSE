# F005 — PROOF_13/14/15 structural review (#3) — for Alex's judgment

**Date:** June 12, 2026. All three read in full. **Structural findings only — no judgment of mathematical validity.**

## Headline: they are sections of the Comprehensive manuscript, not chain extensions

`Comprehensive_Yang_Mills_Mass_Gap_Proof.tex` (23,528 lines, same YANG_ANTI snapshot) contains PROOF_13's and PROOF_15's text **verbatim** (lines 3342, 3466; the manuscript is organized in `\part{}`s — "Core Proofs and Derivations" / "Unified Proof Architecture" / "Appendices"). The trio are standalone exports of that manuscript's gap-closure sections. **Consequence: their review status is inseparable from the Comprehensive manuscript's review status (unreviewed), and the real adjudication object is the manuscript** — a 23.5K-line document whose closing architecture claims the full result. Ledger #4 (manuscript structural map) is now the gating review unit.

## Reference-existence checks

| Reference in trio | Exists in 12-doc chain? | Exists in Comprehensive? |
|---|---|---|
| "Dependency Ledger (Gap 1, Part 7.3 / Part 12)" | **No** (term absent from all 12 reviewed docs) | **Referenced but not present** (only the 2 citing sentences themselves) — *a cited document that exists nowhere in any store* |
| "Part 7.3 / 8.3 / 10 / 11 / 12" numbering | No — chain uses PROOF_01–12 architecture | Yes — `\part{}` structure (55 Part-references) |
| K_Λ(ε/r), badness functional B_Λ | Not in PROOF_09/11 (0 hits) | Yes (manuscript-internal vocabulary; also CMI_PEER_REVIEW/PHYSICS_REFEREE_REPORT mention the family) |
| PBH / Higgs-Bundle flow | Nominal presence (PROOF_09: 1 hit, PROOF_11: 2) | Yes (4 hits) |
| "Proof 09" (CT conjugation), "Proof 13/14" cross-cites | Chain's PROOF_09 is *Tightness and Existence* — **different content** than the CT-conjugation doc PROOF_15 cites | internal numbering presumably consistent within manuscript (not fully verified) |

## Document-level structural observations (per doc)

**PROOF_13 (pairing-term coercivity via "Parabolic Higgs-Bundle Flow").** The load-bearing steps of Prop 13.1's proof are qualitative at exactly the critical points: "can be reorganized into a discrete spatial Laplacian", "overwhelmingly absorbs the remnant" — no constants, no conditions on β₀, no statement of where the PBH flow's claimed properties are established. The mechanism is introduced in this document with no construction cited.

**PROOF_14 (SPI→LSI via "Aida–Shigekawa mechanism").** Explicitly depends on PROOF_13 ("Because we proved that the PBH Flow exhibits stringent coercivity (Proof 13)…"). Theorem 14.1 carries a "Proof Analysis" rather than a proof; key steps assert applicability ("the Aida–Shigekawa truncation identity strictly applies") without verifying that mechanism's hypotheses. Corollary 14.2 (Herbst) is the standard shape. Encoding artifacts ("Poincar", "Bakry-mery") indicate machine generation/export.

**PROOF_15 (RP permanence under block-spinning).** Theorem 15.1's proof asserts "P_b is explicitly constructed out of independent Gaussian integrations / block-averaging" — no construction given or cited; commutativity with Θ is assumed in the construction it doesn't exhibit. **Its closing paragraph claims completion: "…successfully proving that spec(H)\{0} ⊂ [m_gap, ∞)… resolving the complete architecture requirement." This directly contradicts the project's own recorded status** (conditional on CONJ_B; continuum chain open; "No continuum Yang–Mills mass gap is claimed" — STATE.md). Either the trio + Comprehensive manuscript represent a claimed closure that the review pipeline never validated, or rhetorical overreach in a generated draft. **That adjudication is the single most consequential open review item in the corpus** — it determines whether the Comprehensive manuscript is (a) a major unvalidated advance or (b) a polished overclaim to be archived as such.

## Recommendation to Alex (organizational)

Review order: (1) locate or reconstruct the "Dependency Ledger" (if it never existed, the trio's gap-numbering has no anchor); (2) judge PROOF_13 first — 14 and 15 both lean on it; (3) treat the Comprehensive manuscript as the unit of judgment (ledger #4 will produce its structural map next). Until then: trio stays quarantined in `under_review/`, PROOF_MAP/DB untouched, and **nothing in the trio's language should enter status documents** — especially PROOF_15's completion claim.
