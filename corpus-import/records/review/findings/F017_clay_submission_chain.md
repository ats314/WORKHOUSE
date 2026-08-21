# F017 — Unit #8: clay_submission chain (structure + concordance pass)

**Date:** 2026-06-12 · **Unit:** `E:\YANG\ORGANIZED\01_PROOFS\clay_submission\` (~64 files: 12 chain docs + recovered trio + reviews + submission_meta + CODE). Read: April deep-read (`CLAUDE_REVIEW/CLAY_SUBMISSION_PROOF_CHAIN_DEEP_READ.md`, 478 lines, in full); PROOF_09 + PROOF_11 in full (concordance samples); structure/hash survey of the rest. **PROOF_04 (1,256 lines), the reviews quartet, and CODE run-verification split to sub-unit #8b.**

## 1. Layout and provenance facts

Root files duplicate the organized subdirs byte-for-byte (sampled: PROOF_01/07/12 = DUP) **except CMI_PEER_REVIEW.md, which differs between root and reviews/** — two editions, undiffed (→ #8b). PROOF_13/14/15 sit at root only (June-12 recovery, F005/F006; NOT part of the reviewed 12-chain, adjudication with Alex). **Provenance note for any future reader: `CMI_PEER_REVIEW.md` (Dec 8, 2025, "Referee Status: ADVERSARIAL / HIGH RIGOR") is an internal simulated-referee artifact of the Dec review generation (F013's Math-Lead layer era), not actual Clay Mathematics Institute correspondence.** Its verdict — "STRONG CONDITIONAL PROOF… Existence implies Mass Gap, NOT a full resolution" — is the source of the "A−, Millennium-class reduction" language quoted across the corpus.

## 2. What the chain is (per the April deep-read, confirmed by samples)

A 12-document reduction: lattice layer (PROOF_01–04, curvature mechanism) → bridge (05–08, LSI lifting / polarity / UV log-forest / IR decoupling) → continuum (09–12, tightness / Mosco / flow stability / OS reconstruction), with the single declared assumption H1 = Tightness (PROOF_09). Deep-read Part 5: PROOF_01–12 = *reformulations of P01–P20*, more structured and more explicitly conditional. Consistent with everything in STATE.

## 3. Concordance samples — the grading gradient matters

**PROOF_09 and PROOF_11 are ~60-line outline documents** (each "proof" = 3–6 prose bullets) carrying **status "ESTABLISHED THEOREM."** The April deep-read transcribes their content *accurately* (its Lemma G1–G4 / M1–M3 summaries are nearly verbatim) but grades them "Fully rigorous" — at this granularity that grades the outline's coherence, not a line-by-line proof. Three structural observations, recorded without mathematical judgment:

1. **PROOF_11 Lemma G4 assumes the live bottleneck in one sentence:** "We derived that the 'Anomaly Source' ℛ is strictly positive due to the Haar measure dominance." Global anomaly positivity is precisely CONJ_B — open per live STATE. This concords with the deep-read's own Part 4 row ("PROOF_04: **Local only** (Gribov horizon open)") and **contradicts its Part 3 claim** "Conjecture B (Flow Containment): Proven in PROOF_11." The deep-read carries both statements; Part 3 reads as transcription of the submission's self-assessment, Part 4 as the reviewer's own grade. Anyone quoting Part 3 without Part 4 will overstate the chain. (F013's quoting-hazard genre, now located in the Clay layer too.)
2. **A dependency cycle is visible as written:** PROOF_09's Lemma M1 step 1 invokes "Uniform LSI: From Pillar I (Proof 05)", while PROOF_05 depends on Mosco (PROOF_10), which depends on weak convergence (PROOF_09). The deep-read's own Part 1 graph linearizes this (… → 09 → 10 → 11 → 05 → 12) and its Part 4 dependency column contains the cycle without naming it. The standing resolution in the corpus is that the cycle is broken by *assuming* H1 at PROOF_09 — which is what "single point of conditional assumption" means operationally.
3. **PROOF_09's M2 (uniqueness) leans on PROOF_11's flow uniqueness and "ergodicity implied by the Mass Gap ρ₀ > 0"** — i.e., uniqueness of the limit invokes the gap being proven downstream. Same genre as (2); fine as a conditional architecture, hazardous as quotable "ESTABLISHED THEOREM" headers.

**Concordance verdict:** the deep-read is reliable as *description*, charitable as *grading*, and internally tense (Part 3 vs Part 4). Combined with F016's rule: consume this layer through the deep-read's Part 4 table + 03_CRITICAL_GAPS, never through the docs' own status headers — and never through Part 3.

## 4. Cross-links

- **F006:** the Comprehensive manuscript's embedded Dependency Ledger flags 3 gaps and an explicitly conditional final theorem — matching this chain's honest reading (H1 + the local-only curvature + the polylog power p). The trio PROOF_13/14/15 (~200 lines) claims to close such gaps; both F005/F006 and this read keep them quarantined pending Alex.
- **Live campaigns:** OP-1/OP-12 attack the same content as PROOF_04's "local only" limitation + PROOF_07/08's uniformity claims, from the defect side; OP-4/OP-5 are the honest restatement of PROOF_09/12's assumed steps. The Clay chain's H1 ≡ OP-4 (tightness) under the live taxonomy.
- **EVIDENCE_01** (m_lat = 0.962·μ(β), R² = 0.998, β ∈ [5.7, 6.1]) is the curvature-mass fit also cited in the one-plaquette context (manuscript §8's β = 5.7 world) — finite-a evidence, no scaling claim; deep-read says the same.

## 5. Verdict (one line)

Chain = a 12-doc conditional reduction whose two thinnest links (PROOF_09/11, ~60-line outlines marked ESTABLISHED) carry the live bottleneck in single sentences; April deep-read accurate-as-description / charitable-as-grades with a Part 3-vs-Part 4 internal tension (quote only Part 4); CMI review = simulated referee (Dec generation), root/reviews editions differ; PROOF_04 + reviews + CODE → #8b.

---
**Correction (2026-06-12, F018):** §1's claim that CMI_PEER_REVIEW.md root and reviews/ editions differ was a shell-pipeline artifact (empty-variable comparison). They are byte-identical (md5 9fe5a463…). #8b re-scoped accordingly.
