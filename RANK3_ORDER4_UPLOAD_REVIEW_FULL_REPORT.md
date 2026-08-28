# Rank-3 / order-4 upload review — full working report

**Session date:** 2026-08-23 → 2026-08-24.  
**Repository:** `ats314/WORKHOUSE` @ `main` (`bcddd4a`), branch `claude/files-theory-graph-review-2mei2d`.  
**Request:** *review these files against the theory graph.*  
**Mode:** read-only audit. No repository value, tier, tolerance, ledger entry, invariant or `theory/` file was changed. The only write is one new document, `docs/referee/rank3_order4_upload_review_2026-08-23.md`.

This is the complete working record: every task, every finding that survived
adversarial verification, every candidate finding that was refuted and why,
every claim checked and confirmed, and every claim that cannot be checked from
this repository. The condensed conclusions are in the committed referee report;
this document is the evidence behind them.

---

## Contents

- [1. Executive summary](#1-executive-summary)
- [2. The artifacts under review](#2-the-artifacts-under-review)
- [3. Method](#3-method)
- [4. Task register — the ten investigation lanes](#4-task-register--the-ten-investigation-lanes)
- [5. Findings that survived verification (60)](#5-findings-that-survived-verification-60)
- [6. Candidate findings refuted at verification (68)](#6-candidate-findings-refuted-at-verification-68)
- [7. Claims checked and confirmed correct (185)](#7-claims-checked-and-confirmed-correct-185)
- [8. Claims not verifiable from this repository (79)](#8-claims-not-verifiable-from-this-repository-79)
- [9. Lane notes](#9-lane-notes)
- [10. Deliverables and state](#10-deliverables-and-state)
- [11. Recommended next actions](#11-recommended-next-actions)

---

## 1. Executive summary

The upload's **arithmetic spine is sound** and several of its numbers are more
accurate than the repository's own constants. Its **central mechanism is refuted**.
Its **localization conclusion survives**, but on a premise no document states. And
the **one-face agreement it presents as new** is a pre-existing, presently-executable
corpus certificate the documents never cite.

### 1.1 The five load-bearing conclusions

**(a) The named suspect is not the mechanism.** `A §3`/`§4`, `B §5(2)` and `D:91`
attribute the blind per-size cluster table to a finite-`u` degree-6 fit on 13 points
in engine v10a.24c, and make a `W22`-off recomputation ("Knob B") the discriminator
"between *fit artifact* and *real physics*". Both halves fail. Every blind value the
documents cite comes from `corpus-import/records/transcripts/15 hour RUN.txt`, which is
the **v10a.26** run; its production coefficients come from `_v26_sw_blocks(one,4)` at
`:7232`, an order-truncated Hermitian SW/BCH recursion, and the run prints
`production coefficient method: canonical Hermitian SW/BCH; no polynomial fit/window`
at `:10617` — the line immediately above the table they quote. The 13-point fit
survives only as `_v26_legacy_fit_models`, docstring *"Audit only"*. The v10a.24c
production run died on `KeyboardInterrupt` and emitted no `[16]` block at all.
Separately, zeroing `W22` leaves the effective P-block **exactly** unchanged at orders
0–4 (verified two ways: 9 closed four-step Motzkin walks, none containing a `(2,2)`
step; and an exact-rational transcription of the SW/BCH recursion over random layered
models), so Knob B returns the same number identically. Even counterfactually the fit
could not carry the gap: the run's own preflight measures exact-SW against the retired
fit at `2.267e-07` (`:9190`) against a branch gap of `10.293…` — a factor of 4.5·10⁷.

**(b) The localization is right, for an unstated reason.** The F07 total is
`D_EXACT + FOLD − V_link`. `A`, `B` and `D` decompose `D` and `V_link` by face count and
never give `FOLD` a value or a face profile — only `C:224` prints it, as
`5315003/140454 = +37.8415922650832`, **3.68× the entire gap being localized**. The
conclusion survives only because the one-face fold vanishes exactly: from the corpus's
own gated isolated one-face model the reduced-resolvent moments are `e2 = -1/4`,
`N = 1/16`, `J = -1/64`, `C = 0`, so `-2C - e2·N + J = 1/64 - 1/64 = 0`. No document
states, cites or checks this, and `J = -1/64` occurs nowhere in the repository.

**(c) The one-face agreement is not new.** It is `EXPECTED_GAP` at
`ENGINE_O4_hodge_rootonly_firewall_v1.py:43` — one line below the two lines the
documents do cite — with `one_face_certificate()` at `:218-230` recomputing all three
series in exact `Fraction` from SU(3) characters and raising on mismatch. Executed here:
it passes. The *localization inference* does appear to belong to the session; the
premise does not.

**(d) The dispute is mis-routed.** `A:78`/`B:220` file it as "a sub-entry of C2 / G3".
The G3 half is right; the C2 half is a category error. C2's registered scope is the
off-axis coefficient only (`contradictions.yaml:63-74`), `symbols.yaml:72,98` bind
`C_shp`/`Delta_C` to C2 and `Delta_Gamma` to `[C1, R6]`, and `invariants.py:436-447`
machine-checks that `Φ_C(0) = 0`, so a `k = 0` quantity cannot move `Δ_C` in either
direction. The repository already holds the value inside **C1** at
`contradictions.yaml:36-40`.

**(e) The certificate is arithmetically clean and provenance-broken.** 20/20 hashes
verify; the full 69,800-record replay reproduces `D_EXACT` and `-11.068479463778765`
bit-identically once repaired; the target-leakage scan is clean. But
`ledger_generator.py` is not shipped, so 5 of 7 modules raise `ModuleNotFoundError` and
the package cannot unpickle its own entry point; no upstream hash is bound anywhere;
both advertised QBOUND "exactness gates" are unfailable; shipped independent coverage
is ≤ 84 of 69,800 records (≤ 0.120%) against a report claim of all 69,800; and
`rank3_order4_exact_haar_summary.json` carries a five-line LF island in an otherwise-CRLF
file plus a `sort_keys` violation, both exactly at the QBOUND gate block.

### 1.2 Findings by class

| Class | Count |
|---|---:|
| `overstated` | 22 |
| `artifact-wrong` | 15 |
| `provenance-gap` | 11 |
| `repo-wrong-or-stale` | 5 |
| `graph-conflict` | 5 |
| `other` | 2 |
| **total surviving** | **60** |
| candidates refuted at verification | 68 |
| claims checked and confirmed correct | 185 |
| claims unverifiable from this repository | 79 |

Severity split of survivors: 19 high, 34 medium, 7 low. Several verifiers recommended
downgrades from the originating auditor's severity; those recommendations are preserved
verbatim in the corrected statements in §5 and were applied when writing the referee report.

### 1.3 One correction to the orchestrator's own working hypothesis

Mid-session I flagged a possible circularity: the blind per-size table appeared to sum
bit-for-bit to `8 × HAMER_A4_NUM`, which would have made the corpus's strongest external
validation self-referential. **This was refuted.** The coincidence is an artifact of the
upload's own rendering — `B:60-61` prints sizes 4 and 5 as "`~ 0 (numerical zero)`" where
the transcript prints `-1.3933298959e-14` and `-2.85049761573e-14`. The four-row subset
does land bit-exactly on `8·a_4`; the six actual rows sum to `-0.7751458630184425`, 382
ulps away, and **no permutation of the six reaches it** (all 720 orderings give one of
three doubles). The whole coincidence sits inside the 12-significant-figure print
truncation floor: the `size 6` row alone, `-0.208333333333` as the truncation of `-5/24`,
carries a `+3.33e-13` print error, 64% of the entire `5.17e-13` gap it was being used to
adjudicate. A new finding replaced the hypothesis: the documents' silent substitution of
zeros for those two rows, and `A:62`'s untiered 13-digit precision claim.

---

## 2. The artifacts under review

| # | Artifact | Kind | Delivered |
|---|---|---|---|
| A | `RANK3_ORDER4_MASTER_RECORD.md` | front-door index + synthesis, self-labelled T3 | yes |
| B | `F07_VS_BLIND_TWOFACE_ADJUDICATION.md` | two-face localization + provenance guard | yes |
| C | `WORKHOUSE_RANK3_ORDER4_W2_R2_ORACLE_LINEAGE_TRACE_20260823.md` | dataflow forensics | yes |
| D | `WORKHOUSE_RANK3_ORDER4_F07_VS_BLIND_ORACLE_STRUCTURAL_TRACE_20260823.md` | structural fork | yes |
| E | `WORKHOUSE_RANK3_ORDER4_MODULAR_HAAR_CERTIFICATE_20260823.zip` | 22 files, 20 manifested | yes |

**Four of the seven documents `A §0` declares were not delivered**, including both it
names as entry points (*"If you read one thing: F (the coordination note) for the
argument; the check for the machine-verified spine"*):

- `DENOMINATOR_LOCALIZATION_INVESTIGATION` (`A:21`, A's internal "A")
- `ORACLE_COUNTERFACTUAL_AUDIT` (`A:23`, internal "C")
- `F07_VS_BLIND_COORDINATION_NOTE` (`A:26`, internal "F")
- `f07_twoface_adjudication_check.py` (`A:27`) — the "machine-verified spine"

Consequently `A`'s declared reading order cannot be followed at all, `A §2` rows 7–8 and
the `§2` capstone cannot be audited, and the screen `A:163` instructs the reader to run
does not exist. `A` also references its own `§11.2`, `§11.3`, `§12`, `§5.5` and `§6` —
sections of the undelivered document "A", not of the master record. `D`'s five line-anchors
into `WORKHOUSE_RANK3_ORDER4_EXACT_HAAR_FINAL_AUDIT_20260823.md` are likewise unresolvable,
though `E` corroborates the substance behind two of them.

### 2.1 Path mapping used throughout

| Cited prefix | Resolves to | Verifiable here |
|---|---|---|
| `work/WORKHOUSE-readonly/…` | `/home/user/WORKHOUSE/…` | **yes** |
| `work/rank3_order4_cubic_ledger/` | external | no |
| `work/rank3_order4_exact_haar_run/` | external | no |
| `work/rank3_order4_exact_haar_package_verify/` | external | no |
| `work/fold_linked_exact/` | external | no |

Everything in §8 is unverifiable **because of this mapping**, not because it was found
wrong. The documents were produced in a working tree that is not this repository.

---

## 3. Method

### 3.1 Orchestrator pass (before fan-out)

Read `CLAUDE.md`, `AGENTS.md`, `FRONTIER.md`, `ledger/contradictions.yaml`, the G3 entry
of `ledger/gaps.yaml`, and the relevant blocks of `src/workhouse/constants.py`. Extracted
the certificate zip and verified `sha256sum -c SHA256SUMS.txt` (20/20 OK). Recomputed the
core identities in `fractions.Fraction`/`sympy`. This produced four seed observations
handed to the fan-out — one of which (the Hamer bit-exactness) was later refuted by the
lane assigned to test it, which is the intended behaviour.

### 3.2 Fan-out

| | |
|---|---:|
| investigation lanes | 10 |
| candidate findings produced | 128 |
| adversarial verifiers (one per candidate, effort `high`) | 128 |
| total agents | 138 |
| tool calls | 3,084 |
| subagent tokens | 10,964,467 |
| wall clock | ~7h05m |

Every lane was given the same standing instructions: read-only; do not read
`corpus-import/` recursively; quantify ("close" is not a finding, `3.0e-15 = 31 ulps`
is); classify each result as *artifact wrong* / *repo wrong or stale* / *unverifiable
here* / *correct*; never widen a tolerance, promote a disputed value, or edit `theory/`;
cite `file:line` for everything.

### 3.3 Verification pass

Every candidate finding was handed to an independent verifier told to **default to
refuting it**, to re-open the cited files itself rather than trust the evidence line, and
to recompute all arithmetic independently. A finding was allowed to stand only if the
verifier personally reproduced the discrepancy. **68 of 128 candidates (53%) were refuted**,
including several the originating lane had marked high-severity. Many that survived did
so in materially narrowed form; the verifiers' corrections to their own auditors are
preserved in §5 and are often more informative than the finding itself.

### 3.4 Post-verification orchestrator spot-checks

Four load-bearing results were re-checked by hand before being written up:
the v10a.26 exact-SW provenance (`15 hour RUN.txt:3, 6799-6800, 10614, 10617, 10619-10626,
7220-7246`); `EXPECTED_GAP` at `ENGINE_O4_hodge_rootonly_firewall_v1.py:43` with
`one_face_certificate()` at `:218-230`; the `workhouse search --corpus` suppression,
reproduced live; and the `summary.json` line-ending/sort-order anomaly, reproduced
byte-wise. The report's reproduction block was executed and passes.

---

## 4. Task register — the ten investigation lanes

Per-lane outcome counts, then the brief each lane was given.

| Lane | Brief | Survived | Refuted | Confirmed | Unverifiable |
|---|---|---:|---:|---:|---:|
| `citations-AB` | Citation audit — documents A and B | 10 | 3 | 26 | 8 |
| `citations-CD` | Citation audit — documents C and D | 4 | 8 | 27 | 12 |
| `arithmetic` | Exhaustive exact re-derivation | 8 | 6 | 46 | 11 |
| `certificate` | Certificate package audit | 10 | 4 | 11 | 9 |
| `ledger-graph` | Ledger-graph consistency | 3 | 12 | 10 | 5 |
| `invariants-tests` | Invariant and test coverage | 3 | 10 | 13 | 6 |
| `hamer-circularity` | Hamer circularity investigation | 4 | 5 | 9 | 5 |
| `localization-argument` | Attack on the central structural argument | 6 | 7 | 17 | 6 |
| `rules-compliance` | Rules and ADR compliance | 6 | 6 | 12 | 9 |
| `corpus-value-search` | Search-by-value over the corpus | 6 | 7 | 14 | 8 |
| | **total** | **60** | **68** | **185** | **79** |

### 4.1 `citations-AB` — Citation audit — documents A and B

**Brief.** Extract every file:line pointer in A and B; open each in the repo; check the file exists, the line says what is claimed, and the quotation is verbatim rather than paraphrased. Special attention: the five v10a.21r retraction quotes, the blind per-size table, the one-face vectors, the W22 preflight gates, the two-face vacuum block.

**Findings that survived (10):**

- `B-83776-factorization` — *high / artifact-wrong* — The factorization is wrong. 83776 = 2^6·7·11·17. The printed product 2^7·7·11·17^2 equals 2848384, which is 34x too large. The likely source of the slip is the neighbouring denominator on the line above: 837760 = 2^7·5·7·11·17 (it does carry 2^7). The 17^2 is invented outright; nothing in the chain 
- `B-fit-provenance-stale` — *high / repo-wrong-or-stale* — The cited line ranges are real and do contain the 13-point degree-6 fit — but in the OLDER engine. The run that produced the number B is targeting (size 2 c4 = -0.403971702978 at 15 hour RUN.txt:10621) retired that fit. In that run the production coefficients come from an order-4 Schrieffer-Wolff/BC
- `A-W22-null-only-at-one-face` — *high / artifact-wrong* — Contradicted by the very file A cites two lines earlier in its own reproduction list. DATA_O4_OrderSchedule_Occurrence_Preflight_CPU.py:609-610 gates "no O4 closed walk contains W22" and "W22 first enters a closed walk at order five" — and these are face-independent. `enumerate_closed_layer_walks` (
- `B-axrest-provenance` — *medium / provenance-gap* — The value -11.9485781794014 appears in neither named file, nor anywhere else in the repository. Every corpus print of this quantity is -11.9485781794007 (or the run's derived variants ...400714 / ...400696), and constants.py records -11.9485781794007. B's number is the correct one (it is float(D_EXA
- `B-3897-misquote` — *medium / artifact-wrong* — The quoted string is verbatim at line 2925 only. Line 3897 does not contain those words; it says "the supposed independent incidence adjudicator was effectively constructed to recover the v10a.20 ledger" — the same proposition in different words. Presenting one quotation under two line numbers makes
- `retraction-attributed-to-maintainer` — *medium / overstated* — All five quoted lines are in the assistant's voice in the transcript, not the maintainer's. The maintainer's turn is line 1977 ("review all runs and give me a consistent fucking path forward. im sick of this fucking run around."); "Stop. Do not run v10a.21r." at 1978 opens the reply, which continues
- `twoface-vacuum-called-exact` — *medium / overstated* — The cited corpus evidence is float, not exact. v10a.7 computes e4(C) and omega4 in floating point and gates them against the rationals at a tolerance (default 3e-9); the transcript's own output writes the rationals with a tilde — "e4(C)=-0.0648407658517953 ~ -54321/837760" — which is the corpus's no
- `T2-rows-carry-no-tolerance` — *medium / overstated* — Stated as T2 with no tolerance, which CLAUDE.md's tier table requires ("float agreement within a stated tolerance … tolerance in the detail line"). The actual agreement is far looser than the quoted digits imply, because the per-size rows are printed to 12 significant figures. Summing the six printe
- `check-script-8-vs-6` — *medium / graph-conflict* — A and B give different contents for the same named script, and the script does not exist anywhere reachable — not in /home/user/WORKHOUSE, not in the extracted certificate zip, not in the upload directory (a filesystem-wide find for the name returns nothing). So the count cannot be adjudicated, and 
- `v10a21r-size1-never-run` — *medium / provenance-gap* — No output from v10a.21 or v10a.21r exists anywhere in the corpus, so the statement about what the engine yields is unverifiable here. Both notebooks are unexecuted: execution_count is None and there are zero stored outputs in each; a grep for the engine's own size-table print strings ("exact linked 

**Candidates refuted (3):** `oneface-agreement-not-new`, `B-forbidden-name-m4`, `A-609-cluster-unsupported`

### 4.2 `citations-CD` — Citation audit — documents C and D

**Brief.** Same, for C and D; and separate in-repo citations from the external work/rank3_order4_* tree. Recompute C's asserted SHA-256 for the v10a.7 engine. Check whether theory/SHA256SUMS or corpus-import/SHA256SUMS pin any cited file.

**Findings that survived (4):**

- `d-wrong-engine-version` — *high / artifact-wrong* — The statement about v10a24c's source is true, but every blind number D quotes comes from a DIFFERENT engine, v10a.26, which explicitly retired the polynomial fit and replaced it with order-truncated Hermitian SW/BCH. D's central section-2 objection therefore does not apply to the numbers it is level
- `d-one-face-exact-overstated` — *medium / overstated* — The F07/preflight side is an exact rational; the blind side is a 12-significant-figure printout, so the agreement is established to roughly 6e-14 absolute, not exactly. "Exact" and "proven equal" are the wrong words for a float comparison. (The analytic side of D's claim is correct and I confirmed i
- `c-invariant-line-range-wrong` — *medium / artifact-wrong* — The cited range points mostly at a DIFFERENT invariant. invariants.py:414-418 is the tail of the C20 linked-vacuum float-reconstruction check; :419-420 are blank; :421-422 are only the decorator and `def _():` of the applied-shift check. The sentence C paraphrases lives at :428, outside the cited ra
- `d-one-face-constants-sourced-externally` — *low / provenance-gap* — Both constants are sourced only to external, unverifiable files, when both are gated and PASSED inside this repository. D's strongest section rests on citations a reader here cannot check, while the in-repo evidence that would make it a T1 result went uncited. This is a missed corroboration, not an 

**Candidates refuted (8):** `d-w22-regression-already-exists`, `c-hash-chain-mismatch-vs-shipped-cert`, `c-v10a7-lineage-is-float-and-fold-not-derived`, `repo-raw-folded-381-ulps-unchecked`, `d-audit06-is-about-v25`, `d-relabel-ignores-threshold-fragility-and-existing-check`, `c-design-coupling-quantifiable`, `c-predates-is-version-string-only`

### 4.3 `arithmetic` — Exhaustive exact re-derivation

**Brief.** Recompute every number in A, B, C, D independently in fractions.Fraction/sympy — rationals, decimals, factorizations, differences, counts — and state agree/disagree/not-checkable with the discrepancy in absolute terms and ulps. Includes the referee report's weighted Haar sum, D_EXACT, QBOUND divisibility and integer lift.

**Findings that survived (8):**

- `b3-83776-factorization` — *high / artifact-wrong* — The prime factorization is simply false. sympy.factorint(83776) = {2:6, 7:1, 11:1, 17:1}, i.e. 83776 = 2^6·7·11·17. The product the document prints, 2^7·7·11·17^2, equals 2848384 — a different number, 34x larger. No reading rescues it: 837760 = 2^7·5·7·11·17 and 1675520 = 2^8·5·7·11·17, so neither n
- `degree6-fit-misattribution` — *high / repo-wrong-or-stale* — The blind numbers all four documents cite (m4 = -0.7751458630189173 and the per-size c4 table at 15 hour RUN.txt:10620-10626) were produced by HODGE **v10a.26**, not v10a.24c, and v10a.26 explicitly retired the polynomial fit. The run's own source comment reads "no u-grid or polynomial fit enters th
- `oneface-agree-exactly` — *medium / overstated* — Only one side is exact. The F07 side is the exact rational 143/8960 (T1). The blind side exists only as a 12-significant-digit float print, `c4=+0.0159598214286`. The strongest supportable statement is agreement to 2.86e-14 absolute / 1.79e-12 relative — a T2 bound set by the print precision, not an
- `blind-table-sum-precision` — *medium / artifact-wrong* — The printed rows do not sum to the printed total at the precision A asserts. All six printed rows sum to −0.7751458630184424382751163; with sizes 4 and 5 taken as zero (B §2's own rendering) they sum to exactly −0.7751458630184. The oracle total is −0.7751458630189173. Gap 4.7486e-13 (six rows) or 5
- `d-exact-decimal-last-digit` — *low / artifact-wrong* — Not the correctly rounded decimal of the exact rational. -361008126292641364183/7250590288602460800 = -49.7901704444846074944676901…, whose correctly rounded 15-dp form is -49.790170444484607. The printed …609 is the *double*'s decimal expansion (the nearest double is -49.790170444484608935908909188
- `twoface-vacuum-tier` — *low / overstated* — The identity ω4 = e4(C) − 2·V1 = −327/83776, given the rationals, is genuinely T1 (I re-derived it exactly). But the corpus does not establish e4(C) = −54321/837760 exactly: v10a.7 computes a float and gates it against the rational with `abs(...) < V10A7_TOL` where V10A7_TOL defaults to 3e-9, and th
- `b4-quote-attribution` — *low / provenance-gap* — The quoted wording appears only at Monday 531 PM.txt:2925. Line 3897 is a differently worded passage ("the supposed independent incidence adjudicator was effectively constructed to recover the v10a.20 ledger") — the same substance but not the same sentence, presented inside quotation marks as if it 
- `cert-no-history-binding` — *medium / provenance-gap* — The summary actually shipped in artifact E binds no such thing. Its complete key set is D11, D_EXACT, D_EXACT_decimal, D_EXACT_QBOUND_numerator, D_EXACT_denominator_divides_QBOUND, D_EXACT_integer_over_QBOUND_equality, QBOUND, crt_prime_count_histogram, elapsed_seconds, fully_unordered_nonzero_topol

**Candidates refuted (6):** `b2-zeroed-rows`, `cert-census-divergence`, `ax-rest-reverification`, `c1-invariants-line-slip`, `check-count-conflict`, `a1-hamer-validated-unqualified`

### 4.4 `certificate` — Certificate package audit

**Brief.** Audit artifact E on its own terms: read all three reports, run every shipped validator, determine whether the chain primitives -> W2/R2 -> pickle is present, cross-check C section 3's hash table against what is actually in the package, scan every .py for target leakage, and establish where FOLD and V_link enter.

**Findings that survived (10):**

- `cert-not-replayable-as-shipped` — *high / provenance-gap* — False as a statement about the shipped bundle. 3 of the 4 shipped validators, plus the primary generator itself, fail at import. The package cannot be replayed from its own entry point without files that are not in it. Three separate defects: (a) `rank3_order4_cubic_ledger/ledger_generator.py` is no
- `all-record-independent-replay-has-no-shipped-artifact` — *high / overstated* — No artifact in the package backs this. The only all-record artifact shipped is `rank3_order4_exact_haar_validation.json`, produced by validate_modular_haar_ledger.py — and that script recomputes ZERO of the 69,800 Haar numerators. It reads `scaled_haar_numerator` from the ledger and only checks |n| 
- `package-starts-at-the-pickle-no-upstream-binding` — *high / provenance-gap* — The package begins at `root_exact_pair_topologies.pkl.gz`, which already contains the finished 69,800 (topology, weight) pairs. Everything upstream — the primitive JSON, the W2/R2 generator, the freeze file, the W2/R2 history ledger, the aggregation from 117,161 orientation-sensitive keys to 69,800 
- `document-C-describes-a-different-artifact-than-E` — *medium / graph-conflict* — Zero of C's eight tabulated hashes appear anywhere in package E, and E's summary binds neither a history hash nor a contractor hash. C is describing the `exact_haar_sum.py` route under `work/rank3_order4_cubic_ledger/` / `work/rank3_order4_exact_haar_run/`; E is the `modular_haar_contractor.py` rout
- `summary-json-was-edited-after-generation` — *medium / provenance-gap* — The shipped summary is demonstrably NOT the byte output of the shipped contractor. modular_haar_contractor.py:544-546 writes it with `json.dumps(summary, indent=2, sort_keys=True)` and LF newlines. The shipped file is CRLF throughout EXCEPT for exactly five consecutive lines, and those five lines ar
- `qbound-lift-gate-is-a-tautology` — *medium / overstated* — This is an identity, not a check. Given `d | Q`, the lift is defined as `n * (Q // d)` and `Fraction(n*(Q//d), Q)` is `n/d` by construction — it cannot fail once the divisibility assertion on the previous line has passed. One of the two headline "exactness gates" therefore carries no information. Th
- `headline-scalar-is-the-repo-quarantined-value-undisclosed` — *medium / overstated* — That exact rational is what WORKHOUSE already records as QUARANTINED_SCALAR, annotated "Rejected by both sides; recorded so it is never silently resurrected", with claim status `falsified` and register status `rejected-by-both`. Neither E report mentions this. E's scope caveats are about physical co
- `180-of-180-synthetic-tests-unsupported` — *medium / overstated* — No code and no artifact in the package performs a 180-case three-way synthetic comparison. Grep of every .py for `180`, `synthetic`, `three-way`, `three_way` returns nothing. The claim is also arithmetically distinct from the three checks that ARE shipped (9,100 pure-six entries; 40 non-pure topolog
- `independence-of-local-tensors-partially-overstated` — *low / overstated* — The two implementations share their mathematical inputs verbatim: PURE_SIX_BASIS is the identical five (2,2,2) tableaux in the identical order in both files, and both build the balanced Gram from the same Weingarten definition 3^cycles(sigma^-1 tau) and invert it by Gauss-Jordan over Fractions. So t
- `packaging-hygiene` — *low / other* — Three cosmetic-but-real packaging defects: (1) AUDIT_REPORT.md and WORKHOUSE_RANK3_ORDER4_MODULAR_HAAR_INDEPENDENT_AUDIT_20260823.md are the same bytes under two names, which invites double-counting them as two documents; (2) four run outputs (1.5 MB) are duplicated between the package root and modu

**Candidates refuted (4):** `fold-and-linked-vacuum-are-supplied-not-derived`, `sha256sums-coverage-is-narrower-than-20-of-20-suggests`, `zero-haar-stratum-essentially-unchecked-by-shipped-certificates`, `int64-safety-envelope-names-the-wrong-dimension`

### 4.5 `ledger-graph` — Ledger-graph consistency

**Brief.** Check the documents' claims and proposed writes against contradictions.yaml, gaps.yaml, symbols.yaml, theorems.yaml, index/claims.jsonl, index/graph.jsonl, FRONTIER.md and CERTIFIED.md. Does the proposed new contradiction duplicate, conflict with, or extend the register? Does the relabel introduce a fourth vocabulary? Is the m_4 framing forbidden? Is Knob B the same as G3 protocol item 10?

**Findings that survived (3):**

- `sub-entry-of-c2-is-a-category-error` — *high / graph-conflict* — C2 is not a container for a Gamma-point scalar dispute; by C2's own argument it structurally cannot be. C2 is exactly the off-axis coefficient C_shp, and its notes prove a Gamma-point scalar places NO constraint on Delta_C. Filing a Gamma-point branch conflict under C2 is orthogonal to C2's content 
- `g3-oneliner-half-restates-half-is-new` — *medium / overstated* — Split verdict. The first clause is genuinely new to the verification layer; the second restates protocol item 10 plus audit_findings bullet 3, narrowed and stripped of the recorded blocker. "Decisive" is also wrong for G3 as scoped — by G3's own detail a Gamma-point recomputation cannot settle what 
- `b-section-3-factorization-wrong` — *medium / artifact-wrong* — The factorization is wrong. 2^7*7*11*17^2 = 2848384, not 83776. This string would be transcribed verbatim into any ledger entry recording the two-face vacuum, so it matters in the ledger lane and not only in numerics.

**Candidates refuted (12):** `no-slot-c-register-is-closed`, `pair-already-registered-in-c1`, `existing-slot-is-graph-invisible`, `routing-to-g3-reverses-adr-0002`, `three-new-fields-are-a-fourth-vocabulary`, `which-axis-actually-moves`, `validate-is-not-the-gate`, `m4-spelling-is-forbidden-for-m-gamma-4`, `same-physical-quantity-is-asserted-not-shown`, `knob-b-is-a-strict-subset-of-protocol-item-10`, `relabel-scope-misses-downstream-sites`, `recommendations-omit-the-one-wrong-value`

### 4.6 `invariants-tests` — Invariant and test coverage

**Brief.** Map the proposed checks onto what the repository already checks. Enumerate the 13-check anchoring suite. Run make verify. Run workhouse why / search on every key value. Determine which of the proposed 8 checks would duplicate an existing one.

**Findings that survived (3):**

- `raw-folded-axial-is-stale-and-unchecked` — *high / repo-wrong-or-stale* — src/workhouse/constants.py:428 records RAW_FOLDED_AXIAL_GAMMA_NUM = -11.9485781794007, which is 6.768e-13 away from the exact D_EXACT+FOLD. No invariant in any suite reads that constant — it appears only in the float-naming guard tests/test_constants.py:68 — so nothing in the 140 checks would ever c
- `search-corpus-suppresses-occurrences` — *high / repo-wrong-or-stale* — `workhouse search --corpus <value>` prints exactly that confident false negative whenever the claim catalogue has no hit. format_results returns early inside `if not hits:` — before the block that renders `occurrences` — so the corpus scan runs, finds the value, and its result is discarded. The user
- `oracle-free-row-is-untiered-and-contested` — *medium / overstated* — Internal contradiction: the header promises every row is T1 or T2, and row 8's tier is literally '—'. Worse, it sits in a table titled 'The certified spine (what is machine-verified)'. Substantively, this repository already certifies two blind spots in the corpus's own blindness machinery, so 'zero 

**Candidates refuted (10):** `blind-table-check-duplicates-hamer`, `blind-total-is-not-the-row-sum`, `w22-decisive-test-already-an-open-item`, `f07-value-already-registered`, `anchoring-invariance-duplicates-existing-t1`, `eight-checks-vs-six`, `twoface-vacuum-has-no-current-theory-anchor`, `gap-10293-is-a-subtraction-of-two-registered-constants`, `dispute-suite-cites-a-superseded-section`, `search-cli-rejects-negative-rationals`

### 4.7 `hamer-circularity` — Hamer circularity investigation

**Brief.** Chase the orchestrator's lead that the blind per-size table sums bit-exactly to 8*HAMER_A4_NUM: trace where HAMER_A4_NUM came from, quantify the coincidence, check whether m_1..m_3 agreements are equally tight, and return a verdict of genuine / circular / undetermined.

**Findings that survived (4):**

- `premise-bit-exact-sum-is-false` — *high / other* — Not true as stated. Summing ALL SIX printed c4 rows in printed order gives -0.7751458630184425 (hex bfe8cdfeb26967ae), which is 382 ulps from 8*a_4 = -0.7751458630184 (hex bfe8cdfeb2696630). The bit-exact identity appears only for the hand-selected 4-row subset {size 1, 2, 3, 6} — i.e. after droppin
- `two-live-checks-contradict-on-provenance` — *medium / repo-wrong-or-stale* — This is stale and directly contradicts the other live check on the same constant, which states at invariants.py:1285-1292 that "the caveat is retired" because the primary was obtained and pinned on 2026-08-21. Both checks are in `make verify` and both PASS, so a reader of the verify output is told t
- `hamer-tolerance-is-fitted-not-derived` — *medium / overstated* — The bound is set 2.5% above the observed gap rather than derived from an error budget, and it silently absorbs a real fact: the agreement EXCEEDS the paper's own printed precision. a_4's 12th significant figure sits at 1e-13, so its printed half-ulp is 5e-14; times the bridge factor 8 that is 4.0e-1
- `artifact-blind-table-sums-to-oracle-overstated` — *medium / artifact-wrong* — Stated as an unqualified equality to 13 printed digits, it is false. The six printed per-size c4 values sum to -0.7751458630184425; the oracle TOTAL at :10626 is -0.7751458630189173. Gap 4.748e-13 = 4277 ulps; the two differ in the 12th significant figure. The claim is defensible only with a toleran

**Candidates refuted (5):** `hamer-a4-not-circular`, `a2-a3-corroborations-carry-no-information`, `primary-source-pin-is-unverifiable`, `a4-last-digit-is-the-discriminator`, `m2-m3-recovery-gates-are-loose`

### 4.8 `localization-argument` — Attack on the central structural argument

**Brief.** Attack the one-face-agreement-implies-multi-face-localization argument on four axes: the undecomposed fold, the tier of the agreement, the logical step itself, and whether the 10.293 gap is informative at all given that it equals local_shift + V_link identically. Plus verify the W22 O4-nullity claim.

**Findings that survived (6):**

- `fold-never-decomposed` — *high / overstated* — The F07 total is D_EXACT + FOLD - V_link. FOLD is not an opaque global scalar: it is the Rayleigh-Schrodinger renormalisation term FOLD_A = -2*C_A - E2_A*N_A + J_A (C_A = 0), a BILINEAR in two Gamma-point 13-face sums. A product of face-sums does not decompose into a sum over faces without a convent
- `blind-o4-is-not-a-fit` — *high / artifact-wrong* — The per-size table all three documents use (15 hour RUN.txt:10620-10626) was NOT produced by the fit and NOT by v10a24c. It was produced by the v10a.26 run, in which the production cluster coefficients come from an order-truncated canonical Hermitian Schrieffer-Wolff/BCH recursion and the 13-point d
- `agree-exactly-overstated` — *medium / overstated* — The blind side of the comparison is a 12-significant-digit printout, not an exact object, so "exactly" is not established at any tier above T2 and A's own §2 table correctly says T2 - the prose and the table disagree. The printed +0.0159598214286 differs from 143/8960 = 0.015959821428571427 by 2.857
- `twoface-vacuum-tier` — *medium / overstated* — The corpus evidence for these two-face vacuum numbers is float gating at V10A7_TOL = 3e-9, not exact arithmetic. For omega4 = -327/83776 = 0.0039033 an absolute tolerance of 3e-9 is 7.7e-7 relative - four orders of magnitude looser than the one-face agreement the same table calls T2. The coplanar/pe
- `w22-only-structural-difference` — *medium / graph-conflict* — Contradicted by document D, which enumerates several other structural differences: the representations themselves (exact trace-history state space vs cluster-local Gram/Krylov basis, D §2), the inventories (117,161/69,800 Haar classes vs 203/33 rooted clusters vs 609 marked vs 3,895 Stage-3H, D §4 -
- `83776-factorization` — *medium / artifact-wrong* — 83776 = 2^6 * 7 * 11 * 17. The printed product 2^7*7*11*17^2 equals 2,848,384, which is 34x too large. The error sits in the section B offers as "a clean input that IS available" and it carries a divisibility claim ("| QBOUND") whose stated prime support is wrong by one factor of 2 and one factor of

**Candidates refuted (7):** `v10a21r-size1-claim-false`, `w22-o4-nullity-understated`, `no-crosswalk-vs-termwise-comparison`, `blind-table-does-not-close`, `rivals-claim-unsupported`, `ax-rest-provenance`, `143-8960-already-in-corpus`

### 4.9 `rules-compliance` — Rules and ADR compliance

**Brief.** Judge the documents and A section 6's what-to-land list against CLAUDE.md, AGENTS.md, README.md, CONTRIBUTING.md and all twelve ADRs. Audit A section 2's eight tier assignments for honesty. Determine what evidence tier an out-of-tree run can reach and what would have to be shipped. List every document A references that was not delivered.

**Findings that survived (6):**

- `gamma-scalar-mis-routed-to-C2` — *high / artifact-wrong* — C2 is the off-axis coefficient C_shp. ADR 0002 proves a Γ-point scalar cannot be a sub-entry of it: Φ_C(0)=0, so "a Gamma-point scalar therefore fixes Delta_Gamma and constrains Delta_C not at all." G3's scope was then deliberately NARROWED to C_shp on exactly that ground. Landing item 3 on G3 re-wi
- `oneface-explanation-is-cited-not-derived` — *medium / overstated* — Two problems. (i) Tier: what is offered is a citation of `gates.require(...)` declarations in a corpus program. Reading a gate is not running it, and corpus-import/ is T3 by CLAUDE.md's own table ("a document says so and nothing checks it"). Nothing in src/workhouse/invariants.py checks this, so it 
- `four-sevenths-of-the-set-missing` — *high / provenance-gap* — Neither of the two things A tells the reader to read was delivered. Four of the seven items in A's own §0 document set are absent: DENOMINATOR_LOCALIZATION_INVESTIGATION (internal "A"), ORACLE_COUNTERFACTUAL_AUDIT (internal "C"), F07_VS_BLIND_COORDINATION_NOTE (internal "F"), and f07_twoface_adjudic
- `tiers-asserted-not-computed` — *medium / overstated* — CLAUDE.md: "a claim's status is **computed, not asserted**", and the tier table's "Where it lives" column is part of the definition — T1/T2 live in src/workhouse/invariants.py. None of A §2's eight rows is registered there, and the script that allegedly computes them was not delivered, so every row 
- `cert-zip-cannot-land-as-a-run` — *medium / provenance-gap* — All 20 listed digests verify, but the directory fails ADR 0012's pinning rule and tests/test_runs.py on three counts: (i) the manifest is named SHA256SUMS.txt, not SHA256SUMS; (ii) two on-disk files are unlisted — SHA256SUMS.txt itself and WORKHOUSE_RANK3_ORDER4_MODULAR_HAAR_INDEPENDENT_AUDIT_202608
- `unremarked-census-divergence` — *medium / graph-conflict* — The shipped run's own summary reports two further census numbers that do NOT match the historical v10a.20b values the document quotes, and neither document remarks on it. Document C §4 records the notebook as gating 3,597 whole-block orbits and 1,829,147 pair occurrences; the delivered root_exact_pa

**Candidates refuted (6):** `blind-table-does-not-close`, `vlink-decomposition-is-an-lcm`, `master-record-rounds-away-the-live-finding`, `proposed-adr-duplicates-three-rules`, `what-to-land-omits-the-one-real-upgrade`, `derivative-language-for-a-grep`

### 4.10 `corpus-value-search` — Search-by-value over the corpus

**Brief.** For each of ~30 key rationals and counts, report how many DISTINCT originating computations mention it, where, and under what name. Determine which of the documents' new facts already exist verbatim, whether a per-size F07 decomposition exists outside the retired v10a.21r, and whether any coinage collides with corpus vocabulary.

**Findings that survived (6):**

- `blind-table-is-v10a26-exact-SW-not-a-degree-6-fit` — *high / artifact-wrong* — The per-size table all four documents quote was NOT produced by v10a.24c's degree-6 fit. `15 hour RUN.txt` is a v10a.26 run (header line 3), and in v10a.26 `_v23c_fit_cluster` is REDEFINED to extract coefficients from an order-graded canonical Hermitian SW/BCH recursion (`_v26_sw_blocks(model,4)`), 
- `oneface-143-8960-already-a-corpus-certificate` — *high / overstated* — 143/8960 is already a named, exactly-gated corpus constant, and it sits one line below the very line document B cites for its inputs. `ENGINE_O4_hodge_rootonly_firewall_v1.py` declares EXPECTED_VACUUM at :41, EXPECTED_AXIAL at :42 (both cited by B §2), and EXPECTED_GAP = (8/3, 1, 1/2, 7/32, 143/8960
- `83776-factorization-wrong` — *medium / artifact-wrong* — 83776 = 2^6·7·11·17 = 64·1309. The printed product 2^7·7·11·17^2 equals 2848384, which is 34x too large. The corpus itself has the right factorization of the parent denominator: chat.txt derives 83776 = 2^6·1309 and 837760 = 2^7·5·7·11·17. The 17^2 appears to be imported from the fold denominator 14
- `vlink-face-decomposition-already-exact-with-counts` — *medium / overstated* — The corpus already has the full decomposition WITH the integer embedding counts, and gates it exactly; the documents' check reduces it to a denominator-factorization fact, which is strictly weaker and carries no information about the decomposition. v10a.21r constructs V_MIN from the concrete embeddi
- `twoface-vacuum-tier-and-route-count` — *medium / overstated* — Two problems. (i) Tier: the corpus evidence for both values is a FLOAT gate at V10A7_TOL = 3e-9, i.e. T2, not T1. The only exact statement available is the rearrangement ω4 = e4(C) − 2·V1, which is a definitional identity once the two inputs are literals, not independent evidence for the value. (ii)
- `document-C-invariants-line-cite-off` — *low / provenance-gap* — The cited range straddles two different checks. Lines 402-418 are the C20 check ("exact gate value vs printed float-reconstruction"), which is about the V_link float artifact, not about target-derivation. The check C describes is at :421-429, "run's applied shift is not Delta_Gamma" ("Gate 85's equa

**Candidates refuted (7):** `blind-per-size-table-does-not-sum-to-printed-total`, `F07-label-collides-with-corpus-feature-id`, `m4-is-a-forbidden-name`, `W22-O4-nullity-is-size-independent-in-the-corpus`, `knob-B-and-the-five-requirements-are-existing-protocol-items`, `branch-gap-10.293-is-printed-in-the-corpus`, `C20-artifact-on-V_link-never-mentioned`

---

## 5. Findings that survived verification (60)

Ordered by severity, then lane. Each entry gives the originating auditor's claim and the
**verifier's corrected statement**, which supersedes it wherever the two differ. Where a
finding was independently produced by more than one lane, all instances are kept — the
cross-lane index below shows which.

**Editor's note on one scope conflict between verifiers.** Two verifiers reach opposite
conclusions about `QBOUND`, and both are right within their own scope. The verifier of
`b3-83776-factorization` (§5.1) states that `QBOUND` is *not* a stored literal anywhere in
**this repository** — it is accumulated at runtime in the v10a.21 notebook
(`NB_O4_hodge_v10a21_exact_rooted_cluster_adjudicator_a100.ipynb` cell 1, source lines
6398-6425) from data that is absent — and therefore marks the `| QBOUND` divisibility
claim UNVERIFIABLE HERE. The verifiers of `83776-factorization` and
`qbound-lift-gate-is-a-tautology` cite `QBOUND =
62895057857493885215590055852113920000000` as a literal in the **delivered certificate**
(`cert/modular_haar_contractor.py:47`, `cert/independent_replay_modular_crt.py:24`,
`cert/validate_modular_haar_ledger.py:14`) and confirm divisibility against it. Both hold:
the value is not in the repo, it is in artifact E, and `83776 | QBOUND` under E's value.
The committed referee report uses E's value and says so. Note the consequence the §5.1
verifier draws and the others do not: the `| QBOUND` gate is non-discriminating here —
both the true `83776` and the erroneous `2848384` divide it.

**Cross-lane corroboration.** These findings were reached independently by more than one lane:

| Finding | Reached independently by |
|---|---|
| 83776 factorization (B:99) | `citations-AB`/`B-83776-factorization`, `arithmetic`/`b3-83776-factorization`, `localization-argument`/`83776-factorization`, `corpus-value-search`/`83776-factorization-wrong` |
| W22 / degree-6 fit attribution | `citations-AB`/`B-fit-provenance-stale`, `citations-AB`/`A-W22-null-only-at-one-face`, `citations-CD`/`d-wrong-engine-version`, `arithmetic`/`degree6-fit-misattribution`, `localization-argument`/`blind-o4-is-not-a-fit`, `localization-argument`/`w22-only-structural-difference`, `corpus-value-search`/`blind-table-is-v10a26-exact-SW-not-a-degree-6-fit` |
| one-face agreement tier / novelty | `arithmetic`/`oneface-agree-exactly`, `localization-argument`/`agree-exactly-overstated`, `rules-compliance`/`oneface-explanation-is-cited-not-derived`, `corpus-value-search`/`oneface-143-8960-already-a-corpus-certificate` |
| routing to C2 | `ledger-graph`/`sub-entry-of-c2-is-a-category-error`, `rules-compliance`/`gamma-scalar-mis-routed-to-C2` |
| two-face vacuum tier (T1 vs T2) | `arithmetic`/`twoface-vacuum-tier`, `localization-argument`/`twoface-vacuum-tier`, `corpus-value-search`/`twoface-vacuum-tier-and-route-count` |

### 5.1 `b3-83776-factorization`

| | |
|---|---|
| **severity** | high |
| **class** | `artifact-wrong` |
| **lane** | `arithmetic` |
| **verifier confidence** | high |
| **where** | artifact B §3 (line 99); value corroborated at /home/user/WORKHOUSE/corpus-import/programs/hodge_o4_adjudication/src/ENGINE_O4_hodge_v10a21r_adjudicator_only_same_kernel.py:359 (VPAIR=_XQ(-327,83776)) |

**Claim as stated.** "83776 = 2⁷·7·11·17²    (in-scope, | QBOUND)"

**What is wrong (originating auditor).** The prime factorization is simply false. sympy.factorint(83776) = {2:6, 7:1, 11:1, 17:1}, i.e. 83776 = 2^6·7·11·17. The product the document prints, 2^7·7·11·17^2, equals 2848384 — a different number, 34x larger. No reading rescues it: 837760 = 2^7·5·7·11·17 and 1675520 = 2^8·5·7·11·17, so neither neighbouring denominator carries a 17^2 either. (The divisibility half of the sentence is true: 83776 | QBOUND, since QBOUND = 2^36·3^20·5^7·7·11·13·17^3·19·23·29·31·37·47.) The same 83776 is quoted correctly as a value everywhere else in A/B, so this is an isolated printed-factorization error, but it is stated as exact fact and an in-scope/QBOUND inference is hung off it.

**Evidence (originating auditor).** 83776 = 2^6·7·11·17 (verified sympy.factorint); 2^7·7·11·17^2 = 2848384 ≠ 83776; 837760 = 2^7·5·7·11·17; 1675520 = 2^8·5·7·11·17; 1309 = 7·11·17; 83776·10 = 837760, 83776·20 = 1675520 (all True). QBOUND % 83776 == 0.

**Verifier's corrected statement — authoritative.**

> Artifact B line 99 (/root/.claude/uploads/384fab32-8991-52ce-b2bf-4999d379e3f5/6a2b59cb-F07_VS_BLIND_TWOFACE_ADJUDICATION.md:99) prints `83776 = 2⁷·7·11·17²    (in-scope, | QBOUND)`. The factorization is false. sympy.factorint(83776) = {2:6, 7:1, 11:1, 17:1}, i.e. 83776 = 2^6·7·11·17 (64·7·11·17 = 83776). The printed product 2^7·7·11·17^2 = 2848384, which is 34x larger (2848384/83776 = 34 = 2·17 exactly, so the error is exactly one surplus factor of 2 and one surplus factor of 17). No neighbouring denominator in the same code block rescues the reading: 837760 = 2^7·5·7·11·17 (B:97, e4(C) = -54321/837760) and 1675520 = 2^8·5·7·11·17 (B:112, V_link = -1474623/1675520); neither carries 17^2, and both carry a 5 the printed product lacks. The "2⁷" is however the correct 2-exponent of the neighbouring 837760, the likely provenance of the slip.
> 
> The value 83776 itself is correct and used correctly everywhere else: VPAIR=_XQ(-327,83776) at /home/user/WORKHOUSE/corpus-import/programs/hodge_o4_adjudication/src/ENGINE_O4_hodge_v10a21r_adjudicator_only_same_kernel.py:359 (with V1=_XQ(-39,1280) at :358), and I confirmed in exact Fraction arithmetic that e4(C) - 2·V1 = -54321/837760 + 78/1280 = -327/83776. Also confirmed exactly: 1309 = 7·11·17, 1280·1309 = 1675520, 83776·20 = 1675520, 83776·10 = 837760. So B:112 and A:61 ("1675520 = 1280·1309 = 83776·20") are correct; only B:99 is wrong, and a grep over all four .md artifacts shows B:99 is the only place any factorization of 83776 is printed.
> 
> Two qualifications, both narrowing the finding as filed:
> 
> (1) The two parentheticals on the same line do NOT both fall with the factorization. "in-scope" means all prime factors lie in S4_PRIMES = {2,3,5,7,11,13,17,19,23,29,31,37,47} (/home/user/WORKHOUSE/corpus-import/programs/hodge_o4_adjudication/notebooks/NB_O4_hodge_v10a21_exact_rooted_cluster_adjudicator_a100.ipynb, cell 1 source line 6194; enforced by _factor_localized at source lines 6399-6408). {2,7,11,17} ⊆ S4_PRIMES, so "in-scope" is TRUE for 83776. "| QBOUND" is UNVERIFIABLE HERE, not "true" as the candidate's evidence line asserts: QBOUND is not a stored literal anywhere in the repo — it is accumulated at runtime as the prime-exponent LCM over `pairw` (same notebook, source lines 6398-6425), `pairw` is absent, and no printed QBOUND value exists in the repo (grep for "QBOUND =" over .py/.ipynb/.md/.txt/.log yields no output line). The QBOUND factorization quoted in the candidate's evidence (2^36·3^20·5^7·7·11·13·17^3·19·23·29·31·37·47) has no source in this repository and must not be repeated as established.
> 
> (2) Severity "high" is overstated; medium/low is right. Nothing downstream consumes the factorization — no repo code or artifact arithmetic reads it, the value -327/83776 is correct at every use site, and the only inference hung off it ("in-scope") is independently true. It is an isolated printed-factorization error in a prose document, stated as exact fact, correctly recorded as artifact-wrong under the T3 default.

**Why it holds.** Reproduced from primary sources rather than trusting the evidence line. Recomputed with sympy/Fraction: factorint(83776)={2:6,7:1,11:1,17:1}; 2^7·7·11·17^2 = 2848384 != 83776 (ratio exactly 34 = 2·17); 837760 = 2^7·5·7·11·17; 1675520 = 2^8·5·7·11·17; 1309 = 7·11·17. Re-read B:99 with cat -A to confirm the exact superscript characters (U+2077 on the 2, U+00B2 on the 17) — the document really does print 2^7 and 17^2, so this is not a rendering artifact. Confirmed the corroborating value at ENGINE_O4_hodge_v10a21r_adjudicator_only_same_kernel.py:359 and derived -327/83776 = e4(C) - 2·V1 exactly from e4(C) = -54321/837760 and V1 = -39/1280. Grepped all four uploaded .md artifacts: B:99 is the only printed factorization of 83776, so the error is isolated, not systematic. Two corrections to the filed finding: "in-scope" is independently TRUE (S4_PRIMES at notebook cell 1 line 6194 contains 2, 7, 11, 17), and "QBOUND % 83776 == 0" is UNVERIFIABLE here — QBOUND is runtime-computed from data absent from this repo and never stored or printed, so the evidence line's QBOUND factorization is itself unsourced and should be struck. The core claim survives adversarial checking; only the severity and the QBOUND half need correction.

---

### 5.2 `degree6-fit-misattribution`

| | |
|---|---|
| **severity** | high |
| **class** | `repo-wrong-or-stale` |
| **lane** | `arithmetic` |
| **verifier confidence** | high |
| **where** | artifacts A §3, A §4 (Knob B / outcome table), B §0, B §5 item 2, D §2 (line 91); /home/user/WORKHOUSE/corpus-import/records/transcripts/15 hour RUN.txt:7121-7124,7230-7246,10617; /home/user/WORKHOUSE/corpus-import/programs/hodge_o4_adjudication/src/ENGINE_O4_hodge_v10a24c_rootedfullt1_dualcoldoracle_a100.py:6792-6794 |

**Claim as stated.** B §5.2: "the blind v10a.24c basis admits Q2↔Q2 and extracts coefficients by a degree-6 fit on 13 points"; A §3: "the blind branch admits W22 and extracts O4 by a finite-`u` degree-6 fit"; A §4 Knob B and the whole "W22 fit contamination" discriminator; D §2: "The v10a24c implementation, however, diagonalizes at finite `u` and extracts coefficients using a degree-six fit on 13 points"

**What is wrong (originating auditor).** The blind numbers all four documents cite (m4 = -0.7751458630189173 and the per-size c4 table at 15 hour RUN.txt:10620-10626) were produced by HODGE **v10a.26**, not v10a.24c, and v10a.26 explicitly retired the polynomial fit. The run's own source comment reads "no u-grid or polynomial fit enters the production coefficient", it prints "production coefficient method: canonical Hermitian SW/BCH; no polynomial fit/window" immediately above the table the documents quote, and its `_v23c_fit_cluster` now calls `_v26_sw_blocks` and returns `'fit_stability': 0.0, 'method':'canonical Hermitian SW/BCH through O(u^4)'`. The legacy fit survives only as a one-face audit cross-check. The degree-6 / 13-point constants are real but belong to the *other* engine (V23C_FIT_DEG='6', V23C_FIT_N='13'). This matters because A §4 makes "fit contamination" the discriminator between artifact and real physics, and D §2 uses the fit as the only escape from its own admission that "exact perturbative power counting places the first W22 contribution at fifth order". With an exact order-by-order SW/BCH recursion through O(u^4) that escape hatch is gone. NOTE: the *structural* half of the claim survives — v10a.26 builds W with no layer mask exactly as v10a.24c does, so W22 is present in the cluster matrix in both.

**Evidence (originating auditor).** 15 hour RUN.txt:3 and :6447 — "HODGE v10a.26"; :7121-7124 — "no u-grid or polynomial fit / enters the production coefficient"; :10617 — "production coefficient method: canonical Hermitian SW/BCH; no polynomial fit/window"; :7230-7246 — `_v23c_fit_cluster` returns fit_stability 0.0 and method 'canonical Hermitian SW/BCH through O(u^4)'; :7613 — legacy fit only via audit_legacy=True; :7621 gate "v10a.26 exact SW agrees with the retired symmetric fit on the one-face audit". Fit constants at ENGINE_O4_hodge_v10a24c...py:6792-6794 (UMAX 0.055, DEG 6, N 13). W22 present in both: v10a24c:6894-6898 == 15 hour RUN.txt:7094-7098.

**Verifier's corrected statement — authoritative.**

> CONFIRMED, with two corrections to the finding's own framing.
> 
> WHAT I REPRODUCED (every line opened directly):
> 
> 1. PROVENANCE. The blind numbers A, B and D adjudicate — m4 = -0.7751458630189173 and the per-size c4 table — are printed at /home/user/WORKHOUSE/corpus-import/records/transcripts/15 hour RUN.txt:10620-10626, and that transcript is HODGE v10a.26: header at :1-3 "# HODGE v10a.26 — FACTOR-(5,2) COMPLETE + EXACT-SW ROOTED ORACLE", banner print at :6447; 49 occurrences of "v10a.26" vs 2 of "v10a.24c". The value -0.7751458630189173 occurs in no other transcript except "15 hour RUN. results.txt" and "## Assessment.txt"; it does not appear in "# HODGE v10a.24c — production runti.txt", which terminates in a KeyboardInterrupt traceback.
> 
> 2. METHOD. v10a.26 retired the polynomial fit as the production path:
>  - 15 hour RUN.txt:7121-7124 (source comment): "...block-diagonalizes H0+uW order-by-order and returns the canonical Hermitian P block directly; no u-grid or polynomial fit enters the production coefficient."
>  - :6799-6800 (banner source): "production coefficients : canonical Hermitian SW/BCH through O(u^4)" / "retired fit (one-face audit only) : symmetric polynomial, umax= ... deg= ... N= ...", rendered in the output at :9144 as "umax= 0.055 deg= 6 N= 13".
>  - :10617, the line immediately above the quoted table: "production coefficient method: canonical Hermitian SW/BCH; no polynomial fit/window".
>  - :7230-7246 `_v23c_fit_cluster(C, audit_legacy=False)` calls `_v26_sw_blocks(one,4)`/`_v26_sw_blocks(vac,4)` (:7232) and returns `'fit_stability':0.0` (:7242) and `'method':'canonical Hermitian SW/BCH through O(u^4)'` (:7245). `_v26_sw_blocks` (:7149-7169) is an order-by-order BCH/SW recursion on the Taylor coefficient list H[0..4] — no u-grid — validated against the exact rational oracle `_v23_sw_exact` to 5e-12 (:7188-7196).
>  - The 13-point degree-6 fit survives only as `_v26_legacy_fit_models` (:7220-7228), reachable solely via `audit_legacy=True` at the one-face preflight (:7613).
>  By contrast the v10a.24c engine genuinely uses the fit in production: /home/user/WORKHOUSE/corpus-import/programs/hodge_o4_adjudication/src/ENGINE_O4_hodge_v10a24c_rootedfullt1_dualcoldoracle_a100.py:6934-6946 (`_V23Poly.fit(us, ys, deg=6)` on `np.linspace(-0.055, 0.055, 13)`), called in the production shape loop at :7271. So the artifacts' description is true of the SOURCE FILE they cite and false of the RUN whose numbers they quote.
> 
> 3. QUANTIFICATION the finding omitted. The run measures exactly how far the retired fit sits from exact SW: gate "v10a.26 exact SW agrees with the retired symmetric fit on the one-face audit :: max coefficient difference=2.267e-07" (15 hour RUN.txt:9190, repeated as gate 75 at :10733). Even the discarded fit is within 2.267e-07 across all five coefficients — about eight orders of magnitude below the 10.293333600759848 branch gap that A §1 / B §1 are trying to explain.
> 
> 4. ADDITIONAL SUB-ERROR the finding did not name. A §5 states the corpus "has a multi-face fit-stability guard". That guard is the gate "v10a.23 finite-cluster u4 fit window is numerically stable", max |c4(full)-c4(inner)|, and it exists ONLY in the v10a24c engine (...v10a24c....py:7280-7281, fed by `max_fit_stab` at :7267 and :7271). It does not exist in 15 hour RUN.txt at all — grep for `max_fit_stab` returns nothing there, and the run hardcodes `fit_stability: 0.0` (:7242). So A's stated fallback guard is likewise absent from the run that produced its numbers.
> 
> CORRECTION 1 — the finding's `kind: repo-wrong-or-stale` is misclassified. The repository is RIGHT and self-consistent; the uploaded artifacts are wrong. /home/user/WORKHOUSE/ledger/provenance.yaml:120-136 records the v10a.26 notebook as "the originating computation"; /home/user/WORKHOUSE/src/workhouse/constants.py:9 attributes the floats to "the v10a.26 folded run"; /home/user/WORKHOUSE/corpus-import/records/transcripts/README.md:5,7 names the pair correctly; and /home/user/WORKHOUSE/corpus-import/records/audits/09-dual-cold-oracle.md — the static audit of the v10a24c family that itself describes the deg-6/13-point fit at :35 and :57 — states at :6 that every v10a.24c artifact has "`execution_count: null`, and zero stored outputs ... no preserved pass/fail result closes either gate". A source with zero stored outputs cannot have produced the quoted table. File this as artifact-wrong (A, B, D), not repo-wrong.
> 
> CORRECTION 2 — the naming half is softer than the finding states. 15 hour RUN.txt:6750 carries the internal section header "# HODGE v10a.24c — INDEPENDENT ROOTED FINITE-CLUSTER LINKED-GAP ORACLE" and :6792 prints "HODGE v10a.23 — INDEPENDENT FINITE-CLUSTER LINKED-GAP ORACLE", so B §0's "v10a.23/24c rooted incidence transform" is defensible lineage naming for that leg. Likewise the constants V23C_FIT_UMAX/DEG/N = 0.055/6/13 are present in the v10a.26 run too (15 hour RUN.txt:6775-6777) — they do not belong exclusively to "the other engine"; in v10a.26 they parameterize only the retired audit. What is indefensible, and is the entire finding, is the METHOD attribution: B §5 item 2 (B:167-170) "extracts coefficients by a degree-6 fit on 13 points", A §3 (A:90) "extracts O4 by a finite-`u` degree-6 fit", and D §2 (D:91) "diagonalizes at finite `u` and extracts coefficients using a degree-six fit on 13 points" are each contradicted by the run's own printed method line at :10617 and its source comment at :7121-7124.
> 
> CONSEQUENCE (argument, not a machine check). D §2 concedes "exact perturbative power counting places the first `W22` contribution at fifth order" and uses the finite-u fit as the sole reason the block could still contaminate O(u^4); A §4 Knob B and its outcome row "divergence is W22 fit contamination" rest on the same premise. Under an exact order-by-order SW recursion that premise is void: the O(u^4) P block contains at most four factors of V, while any path touching V_{Q2Q2} needs P→Q1→Q2→Q2→Q1→P = five, so W22 cannot enter c4. I verified the recursion is order-by-order and rational-oracle-validated, but no gate in the run STATES multi-face W22-O4-nullity, so this consequence is an argument from the code's structure, not a repo check. The structural half of A/B/D survives intact: v10a.26 builds W with no layer mask exactly as v10a.24c does — 15 hour RUN.txt:7094-7098 is line-for-line the same loop as ...v10a24c....py:6894-6898 (modulo an added progress print) — so W22 is present in the cluster matrix in both.

**Why it holds.** I opened every cited line rather than trusting the evidence field. The transcript producing m4 = -0.7751458630189173 and the per-size table (15 hour RUN.txt:10620-10626) is HODGE v10a.26 (:1-3, :6447), and that run's own banner (:6799-6800), source comment (:7121-7124), production print (:10617) and code (`_v23c_fit_cluster` -> `_v26_sw_blocks`, fit_stability 0.0, :7230-7246; `_v26_sw_blocks` :7149-7169 validated to 5e-12 against an exact rational SW oracle at :7188-7196) all state the production coefficients come from an exact order-by-order Hermitian SW/BCH recursion with no polynomial fit. The deg-6/13-point fit is reachable only via audit_legacy=True at the one-face preflight (:7613, :7220-7228). The fit IS production in the v10a24c engine (...v10a24c....py:6934-6946, called at :7271), so A, B and D describe the wrong engine's method for the numbers they quote. Corroborating: the value appears in no v10a.24c transcript, and the repo's own audit records that every v10a.24c artifact has zero stored outputs (audits/09-dual-cold-oracle.md:6). I added the run's own fit-vs-exact measurement (2.267e-07 at :9190/:10733), eight orders below the 10.2933336 gap the fit is blamed for, and a fourth sub-error the finding missed (A §5's "multi-face fit-stability guard" exists only at ...v10a24c....py:7280-7281 and is absent from the run). I downgraded the finding's kind from repo-wrong-or-stale to artifact-wrong, since provenance.yaml:120-136, constants.py:9 and transcripts/README.md:5 attribute the numbers to v10a.26 correctly, and softened the naming half, since the run's own internal section header at :6750 does read "HODGE v10a.24c" and the fit constants do exist in the v10a.26 source at :6775-6777.

---

### 5.3 `all-record-independent-replay-has-no-shipped-artifact`

| | |
|---|---|
| **severity** | high |
| **class** | `overstated` |
| **lane** | `certificate` |
| **verifier confidence** | high |
| **where** | cert/AUDIT_REPORT.md:40,57; cert/INDEPENDENT_REFEREE_REPORT.md:48; /tmp/claude-0/-home-user-WORKHOUSE/384fab32-8991-52ce-b2bf-4999d379e3f5/scratchpad/cert/validate_modular_haar_ledger.py:59-62 |

**Claim as stated.** "an independent all-record replay of the final 69,800-entry ledger" (AUDIT_REPORT.md:57) and "The full 69,800-record primary ledger was then replayed record by record. The verifier independently checked ... lifted numerators, reduced Haar values ..." (INDEPENDENT_REFEREE_REPORT.md:48)

**What is wrong (originating auditor).** No artifact in the package backs this. The only all-record artifact shipped is `rank3_order4_exact_haar_validation.json`, produced by validate_modular_haar_ledger.py — and that script recomputes ZERO of the 69,800 Haar numerators. It reads `scaled_haar_numerator` from the ledger and only checks |n| <= bound (line 60) and haar == n/q (lines 61-62). The numerator, which is the entire scientific content, is taken as given. The script that does recompute all 69,800 numerators is independent_replay_modular_crt.py, and its outputs (`independent_modular_crt_exact_haar_numerators.json.gz`, `independent_modular_crt_exact_haar_status.json`) are absent from the zip and from SHA256SUMS.txt. Shipped independent recomputation therefore covers 44 of 69,800 topologies = 0.063% (stratified certificate), plus 40 more in the reference crosscheck.

**Evidence (originating auditor).** validate_modular_haar_ledger.py lines 59-62: `numerator = int(row["scaled_haar_numerator"]); assert abs(numerator) <= expected_bound; haar = Fraction(numerator, expected_q)`. Its Q_PATTERN/TRIANGLE tables (lines 15-16) are copies of the generator's own tables (modular_haar_contractor.py:36-44, 209-219), so "q products recomputed" and "signed bounds recomputed" are recomputations against the generator's own constants. I closed the gap myself: reconstructed the environment and ran independent_replay_modular_crt.py to completion over all 69,800 classes (~62 min). It agrees with the primary ledger on every record — 0 unmatched keys, 0 numerator mismatches, 0 Haar mismatches, 0 weight mismatches — and returns D_exact = -361008126292641364183/7250590288602460800, total_integer_numerator_over_qbound = -3131555650840341423974721085483725619200000, zero_haar_values = 9184. So the claim is TRUE and reproducible; it is simply not evidenced by anything in the package.

**Verifier's corrected statement — authoritative.**

> OVERSTATED CLAIM, PACKAGE SHIPS NO ARTIFACT FOR IT — holds, with two citations narrowed and one piece of the original evidence withdrawn.
> 
> WHAT IS TRUE (all re-verified from primary sources by me):
> 
> 1. The only all-record artifact in the package is `modular_haar_run/rank3_order4_exact_haar_validation.json` (`"records": 69800`), produced by `cert/validate_modular_haar_ledger.py`. That script recomputes ZERO of the 69,800 Haar numerators. Lines 59-62 verbatim: `numerator = int(row["scaled_haar_numerator"])` / `assert abs(numerator) <= expected_bound` / `haar = Fraction(numerator, expected_q)` / `assert frac(row["haar"]) == haar`. The numerator — the entire scientific content of each record — is read from the generator's own ledger. The certificate it writes is honest about this: its flags are `record_q_products_recomputed`, `record_signed_bounds_recomputed`, `record_crt_modulus_exceeds_twice_bound`, `record_haar_equal_scaled_numerator_over_q`, `record_weighted_contributions_recomputed` — no numerator flag exists.
> 
> 2. NEW QUANTIFICATION (mine): the only per-record gate touching the numerator is `abs(n) <= signed_uniqueness_bound` (line 60). Over all 69,800 records that interval admits a MINIMUM of 13,123 integers, MEDIAN 3.7280698815493e13, MAXIMUM 3.4704941442785281e16. The gate therefore excludes essentially nothing: it cannot distinguish the correct numerator from ~1e13 wrong ones.
> 
> 3. `validate_modular_haar_ledger.py:15-16` `Q_PATTERN`/`TRIANGLE` are literal copies of the generator's own constants — `modular_haar_contractor.py:36-44` (`Q_PATTERN`, identical map) and the values `LOCAL_TRIANGLE_BOUND` at `modular_haar_contractor.py:209-223` computes from `BALANCED_INVERSE`/`PURE_SIX_INVERSE`, echoed in `rank3_order4_exact_haar_summary.json` `local_triangle_bound` = {0,3:1; 0,6:66; 1,1:1; 2,2:8; 3,0:1; 3,3:120; 6,0:66}. So "q products recomputed" and "signed bounds recomputed" are recomputations against the generator's own tables, not independent ones. (Correction: the dict spans 209-223, not the 209-219 originally cited.)
> 
> 4. The script that DOES recompute all 69,800 numerators is `cert/independent_replay_modular_crt.py` (line 106, `modular.exact_haar_numerator(left, right, stats)`, inside the loop over all pair items). Neither of its outputs — `independent_modular_crt_exact_haar_numerators.json.gz` (line 197) or `independent_modular_crt_exact_haar_status.json` (line 210) — appears in the extracted package or in any of the 20 lines of `SHA256SUMS.txt`.
> 
> 5. NEW (mine): the package does not even let a reader regenerate that output. `python3 cert/independent_replay_modular_crt.py` fails immediately: `ModuleNotFoundError: No module named 'ledger_generator'` at line 19 — it sys.path-inserts `WORK/"rank3_order4_cubic_ledger"` (line 18), which is external and absent. Line 21 imports `modular_su3_projector` while the shipped module is named `independent_modular_su3_projector.py`, and line 65 expects `root_exact_pair_topologies.pkl.gz` in the PARENT directory while the zip places it in the package root.
> 
> 6. Shipped independent recomputation therefore covers 44/69,800 = 0.0630% (`stratified_actual_topology_modular_audit.json`: `audited_topologies: 44`, `endpoint_signature_strata: 22`), plus 40 in `rank3_order4_modular_reference_crosscheck.json` (`actual_frozen_topologies_checked: 40`, 20 signatures). Union <= 84 = <= 0.120%. Note the 40 crosscheck records carry no topology identifier (keys: `crt_primes`, `patterns`, `signed_bound`, `value`), so disjointness from the 44 cannot be verified from the artifacts; only `AUDIT_REPORT.md:55`'s own word "additional" supports it.
> 
> WHERE THE OVERSTATEMENT ACTUALLY SITS (narrowed):
> - `cert/INDEPENDENT_REFEREE_REPORT.md:48` is the sharp one: "The full 69,800-record primary ledger was then replayed record by record. The verifier independently checked topology uniqueness and order, local `q` products, signed CRT bounds, LIFTED NUMERATORS, reduced Haar values, ...". The lifted numerators are not checked in any sense that constrains them; per item 2 the only gate admits >=13,123 values per record. Every other item in that sentence IS done by the shipped validator.
> - `cert/AUDIT_REPORT.md:57` ("an independent all-record replay of the final 69,800-entry ledger") is overstated only in the word "independent", and only by placement: it sits in a bulleted "Independent checks" list whose other four bullets are genuine independent recomputations, so it reads as one of them.
> 
> WITHDRAWN FROM THE ORIGINAL FINDING:
> - `cert/AUDIT_REPORT.md:40` is NOT overstated and must be dropped from the charge. It reads "A separate replay recomputed every record's `q` product, bound, CRT sufficiency, Haar rational, weighted contribution, total sum, and `D_EXACT`" — an exact and complete description of `validate_modular_haar_ledger.py`, conspicuously omitting the Haar numerator.
> - The originating auditor's evidence line ("I ran independent_replay_modular_crt.py to completion ... 0 unmatched keys, 0 numerator mismatches, 0 Haar mismatches, 0 weight mismatches") is UNVERIFIABLE HERE and partly inaccurate as a description of the script: `independent_replay_modular_crt.py` never opens the primary ledger (it loads only `root_exact_pair_topologies.pkl.gz`, lines 65-67) and emits no per-record comparison of any kind. Its aggregate figures do match the shipped `rank3_order4_exact_haar_summary.json`/`validation.json` (D_exact = -361008126292641364183/7250590288602460800; lift = -3131555650840341423974721085483725619200000; zero_haar = 9184), but that agreement should not be entered as reproduced evidence.
> 
> NET: this is an evidence-packaging defect, not an arithmetic one. Nothing here shows the numerators are wrong; it shows that the package's own artifacts pin only 84 of 69,800 of them independently (<= 0.120%), while `INDEPENDENT_REFEREE_REPORT.md:48` asserts all 69,800 lifted numerators were independently checked. Under CLAUDE.md's "no document is authority, only a machine check is", the correct status of the 69,716 unchecked numerators in this package is T3, not certified. Nothing in WORKHOUSE currently records this (grep for `69800`/`modular_haar`/`exact_haar` outside `.venv/` returns nothing relevant).

**Why it holds.** I opened every cited file at every cited line and reproduced the arithmetic. validate_modular_haar_ledger.py:59-62 is verbatim as claimed and demonstrably reads rather than recomputes the numerator; its own certificate flags never claim otherwise. The generator-table copying is confirmed against modular_haar_contractor.py:36-44 and 209-223. The independent_replay_modular_crt.py outputs are genuinely absent from both the extracted tree and all 20 lines of SHA256SUMS.txt, and I additionally established the script cannot be run from the package at all (ModuleNotFoundError: ledger_generator, plus a module-name and a path mismatch). I quantified the one numerator gate that does exist: it admits a minimum of 13,123 and a median of 3.73e13 integers per record, so it constrains nothing. Coverage counts 44 and 40 are read directly out of the two certificate JSONs. I refuted two sub-parts of the original finding: AUDIT_REPORT.md:40 is an accurate description of the validator and should not be charged, and the auditor's own full-replay reproduction is unverifiable here and misdescribes the script's outputs. The core claim — the package ships no artifact backing an independent all-record recomputation, while INDEPENDENT_REFEREE_REPORT.md:48 asserts one — survives intact.

---

### 5.4 `cert-not-replayable-as-shipped`

| | |
|---|---|
| **severity** | high |
| **class** | `provenance-gap` |
| **lane** | `certificate` |
| **verifier confidence** | high |
| **where** | cert/AUDIT_REPORT.md:70 (and the byte-identical WORKHOUSE_..._AUDIT_20260823.md:70); scripts at /tmp/claude-0/-home-user-WORKHOUSE/384fab32-8991-52ce-b2bf-4999d379e3f5/scratchpad/cert/{modular_haar_contractor.py:31-32, independent_replay_modular_crt.py:16-21, independent_cross_check_actual_topologies.py:16-21, crosscheck_modular_haar_reference.py:13-23} |

**Claim as stated.** "The accompanying ZIP contains the frozen source archive, exact ledger, summaries and validations, both independent cross-check certificates, referee report, and all contractor/replay sources needed to audit the route."

**What is wrong (originating auditor).** False as a statement about the shipped bundle. 3 of the 4 shipped validators, plus the primary generator itself, fail at import. The package cannot be replayed from its own entry point without files that are not in it. Three separate defects: (a) `rank3_order4_cubic_ledger/ledger_generator.py` is not shipped, yet it is imported by modular_haar_contractor.py:32, independent_replay_modular_crt.py:19 and independent_cross_check_actual_topologies.py:21, and it is required to unpickle the entry-point file at all (the pickle's STACK_GLOBAL is `ledger_generator.LXState`, attrs `occ`,`part`); (b) the two reference modules were renamed on packaging — every importer asks for `exact_su3_projector` / `modular_su3_projector`, the zip contains `independent_exact_su3_projector.py` / `independent_modular_su3_projector.py`; (c) independent_replay_modular_crt.py:17 and independent_cross_check_actual_topologies.py:17 set `WORK = HERE.parent` and look for the pickle and `modular_haar_run/` there, but the package is flat, so those paths resolve outside the package. numpy is also an undeclared dependency with no requirements file.

**Evidence (originating auditor).** Ran all four from the package root. validate_modular_haar_ledger.py EXIT=0 (3.9 s, PASS). crosscheck_modular_haar_reference.py EXIT=1 `ModuleNotFoundError: No module named 'numpy'` (line 13); with numpy present it next fails on `ledger_generator`. independent_replay_modular_crt.py EXIT=1 `ModuleNotFoundError: No module named 'ledger_generator'` (line 19). independent_cross_check_actual_topologies.py EXIT=1 same error (line 21). After I installed numpy 2.4.6, wrote a 20-line `ledger_generator.LXState` stub, restored the two module names and rebuilt the directory layout, all four run to completion and pass.

**Verifier's corrected statement — authoritative.**

> CONFIRMED, with three corrections to the auditor's wording and a downgrade of severity to medium.
> 
> QUOTE VERIFIED. cert/AUDIT_REPORT.md:70 reads verbatim: "The accompanying ZIP contains the frozen source archive, exact ledger, summaries and validations, both independent cross-check certificates, referee report, and all contractor/replay sources needed to audit the route." The second copy, WORKHOUSE_RANK3_ORDER4_MODULAR_HAAR_INDEPENDENT_AUDIT_20260823.md, is byte-identical (both md5 1579a6f4a632bb3f9bda2b780466c29f), same line 70.
> 
> PACKAGE STATE. I re-extracted the original upload dc08a31e-...CERTIFICATE_20260823.zip into a fresh directory; the shipped cert/ tree is byte-identical to it (diff -r clean), so I tested pristine bytes. 22 files; SHA256SUMS.txt lists 20 and all 20 verify on a fresh extract. No README, no requirements.txt, no run instructions anywhere in the bundle.
> 
> IMPORT BREAKAGE (stronger than stated). Running each shipped .py under /usr/bin/python3 (numpy 2.4.6 present) from the package root, 5 of the 7 shipped modules raise ModuleNotFoundError, not "3 of 4 validators plus the generator":
>   - crosscheck_modular_haar_reference.py:21, independent_replay_modular_crt.py:19, independent_cross_check_actual_topologies.py:19, modular_haar_contractor.py:32 -> No module named 'ledger_generator'
>   - independent_modular_su3_projector.py:21 -> No module named 'exact_su3_projector'
> Only validate_modular_haar_ledger.py (EXIT=0, PASS) and independent_exact_su3_projector.py import cleanly.
> 
> CORRECTION 1 (line cite). The third ledger_generator importer is independent_cross_check_actual_topologies.py:19, NOT :21 as the finding states; :21 in that file is `import modular_su3_projector`. The finding also omits a fourth importer, crosscheck_modular_haar_reference.py:21.
> 
> PICKLE DEPENDENCY VERIFIED FROM THE BYTES. root_exact_pair_topologies.pkl.gz decompresses to 12,458,390 bytes containing exactly two STACK_GLOBAL opcodes: ('ledger_generator','LXState') at offset 1595 and ('fractions','Fraction') at 1724, followed by NEWOBJ + BUILD with state-dict keys 'occ' and 'part'. No ledger_generator.py exists in the zip, in SHA256SUMS.txt, or anywhere in /home/user/WORKHOUSE.
> 
> CORRECTION 2 ("the package is flat" is wrong; defects (b) and (c) are one root cause). The zip is NOT flat: it ships modular_haar_run/ as a real subdirectory of 4 files plus duplicate flat copies. The actual defect is a one-level path offset with the same origin as the rename: the packager flattened the working tree's `independent_haar_audit/` subdirectory into the zip root and prefixed its two library modules with `independent_`. Residual evidence in the shipped code: crosscheck_modular_haar_reference.py:16-20 still puts ROOT/"independent_haar_audit" on sys.path; independent_replay_modular_crt.py:17 and independent_cross_check_actual_topologies.py:17 still set WORK = HERE.parent and read WORK/root_exact_pair_topologies.pkl.gz (:65 and :62) and WORK/modular_haar_run/... (:63-64), while modular_haar_contractor.py:553-554 uses HERE. I reconstructed the implied tree — work/{pkl.gz, modular_haar_run/, modular_haar_contractor.py, validate_*, crosscheck_*} plus work/independent_haar_audit/{exact_su3_projector.py, modular_su3_projector.py, independent_replay_*, independent_cross_check_*} plus work/rank3_order4_cubic_ledger/ledger_generator.py — and every script resolved with no other change (stratified audit PASS 44/44, 1.92 s).
> 
> CORRECTION 3 (numpy is the weakest leg and partly an artifact of this box). Here `python3` resolves to /home/user/WORKHOUSE/.venv/bin/python3, which has no numpy; /usr/bin/python3 already ships numpy 2.4.6. So the `ModuleNotFoundError: numpy` at crosscheck_modular_haar_reference.py:13 is environment-dependent, not a property of the package; with numpy present that script fails at :21 on ledger_generator instead. The failure count is unchanged either way. What IS a package property is the absence of any requirements.txt or README.
> 
> REPAIR REPRODUCED END-TO-END. With (i) numpy, (ii) a 3-line `ledger_generator.LXState` stub, (iii) the two module names restored, (iv) the one-level layout fix: validate_modular_haar_ledger.py EXIT=0; crosscheck_modular_haar_reference.py EXIT=0, passed:true, elapsed 165.7 s, 9,100 pure-six projector entries on the full 90x90 support, 488 delta terms; independent_cross_check_actual_topologies.py EXIT=0, PASS 44/44 across all 22 signatures, 1.71 s; independent_replay_modular_crt.py EXIT=0, 69,800/69,800 records in 4013.7 s, status "complete", reproducing D_exact = -361008126292641364183/7250590288602460800 and m4_rest = -160506019419340168451/14501180577204921600, bit-identical to INDEPENDENT_REFEREE_REPORT.md and to the orchestrator's established D_EXACT+FOLD-V_link. One detail the auditor's stub description would get wrong: LXState must have a normal __dict__ — a __slots__ version dies with `AttributeError: 'LXState' object has no attribute '__dict__'` at crosscheck_modular_haar_reference.py:73, because the pickle rebuilds via NEWOBJ+BUILD.
> 
> SEVERITY: medium, not high. The import breakage is packaging hygiene, repairable in minutes, and withholds no mathematics — a 3-line stub suffices precisely because ledger_generator is imported only for pickle class identity, as modular_haar_contractor.py:32 says in its own comment. The substantive residue, and the only part worth a ledger entry, is narrower: the ZIP omits work/rank3_order4_cubic_ledger/ledger_generator.py entirely (external to this repo; document C cites it up to :1653-1675, so roughly 1,700 lines), so the frozen census the whole certificate rests on — 69,800 unordered contraction classes from 117,161 orientation-sensitive keys, 5,400 matched sectors, raw pair upper bound 9,814,138, 54 skipped one-face matches, all re-emitted verbatim as `source_counts` by the replay — cannot be regenerated or checked from the bundle. AUDIT_REPORT.md:59 partially self-discloses this ("This does not independently prove that the primitive generator is a complete physical perturbation expansion; that is a distinct provenance/modeling obligation"), but :70 as written is still false.
> 
> NOT PREVIOUSLY RECORDED: grep for modular_haar / ledger_generator / root_exact_pair_topologies / rank3_order4_exact_haar across /home/user/WORKHOUSE (*.md, *.py, *.yaml, *.json) returns nothing. Repo untouched: git status clean, numpy installed only into the system python, not the repo venv.

**Why it holds.** I re-extracted the original zip and confirmed the shipped cert/ directory is byte-identical, so I tested pristine bytes rather than the prior auditor's working copy. Every cited line resolved as claimed except one: independent_cross_check_actual_topologies.py imports ledger_generator at line 19, not 21, and the finding misses a fourth importer at crosscheck_modular_haar_reference.py:21. I reproduced all four exit codes from the package root (1 PASS, 3 ModuleNotFoundError), confirmed the ledger_generator.LXState dependency directly from the pickle opcode stream (STACK_GLOBAL at offset 1595, NEWOBJ+BUILD, state keys 'occ'/'part'), and confirmed that ledger_generator.py, exact_su3_projector.py and modular_su3_projector.py exist neither in the zip, nor in its manifest, nor in the repo. I then repaired the package stepwise to isolate each defect in order: with numpy alone all three still die on ledger_generator; with the stub added they die on the renamed modules; with the names restored they die on WORK=HERE.parent resolving outside the package; with the layout fixed all four run and pass, the full 69,800-record replay reproducing D_exact and m4_rest bit-identically in 4013.7 s. Two supporting statements in the finding are wrong and I corrected them — the package is not flat (it ships modular_haar_run/ as a subdirectory), and the numpy failure is an artifact of this box's default python3 being the repo venv rather than a package property — but neither correction touches the load-bearing claim, which is that the sentence at AUDIT_REPORT.md:70 is false about the shipped bundle. I downgraded severity because a 3-line stub restores full arithmetic auditability, so nothing mathematical is withheld; the real gap is the absent generator source, which makes the frozen 69,800-class census unauditable from the bundle, and AUDIT_REPORT.md:59 already partly concedes that.

---

### 5.5 `package-starts-at-the-pickle-no-upstream-binding`

| | |
|---|---|
| **severity** | high |
| **class** | `provenance-gap` |
| **lane** | `certificate` |
| **verifier confidence** | high |
| **where** | cert/AUDIT_REPORT.md:59,63; cert/INDEPENDENT_REFEREE_REPORT.md:52; entry point /tmp/claude-0/-home-user-WORKHOUSE/384fab32-8991-52ce-b2bf-4999d379e3f5/scratchpad/cert/root_exact_pair_topologies.pkl.gz |

**Claim as stated.** "The arithmetic certificate is therefore closed for the frozen generator lineage." (AUDIT_REPORT.md:59) — with hashes listing only "Frozen source topology archive: 5337734a..." (line 63)

**What is wrong (originating auditor).** The package begins at `root_exact_pair_topologies.pkl.gz`, which already contains the finished 69,800 (topology, weight) pairs. Everything upstream — the primitive JSON, the W2/R2 generator, the freeze file, the W2/R2 history ledger, the aggregation from 117,161 orientation-sensitive keys to 69,800 unordered classes — is neither shipped nor hash-bound from inside the package. Worse, the pickle's own key literally named `source_history_sha256` does NOT contain a SHA-256: it holds a dict of counts {'left_physical_blocks': 3439, 'matched_h0_blocks': 5400, 'raw_pair_upper_bound': 9814138, 'skipped_one_face_matches': 54, 'compatible_state_pairs': 2468250, 'observed_haar_patterns': [...], 'unsupported_haar_patterns': [], 'max_bra_ket_occurrences': 24}. So the entry point carries zero cryptographic binding to anything that produced it. The census integers the referee report cites (5,400 matches; 9,814,138 raw pair upper bound; 54 skipped one-face matches; 117,161 historical keys) are bare integer fields inside that pickle — nothing in the package recomputes or witnesses any of them, and no code in the package performs the 117,161 -> 69,800 quotient.

**Evidence (originating auditor).** Unpickled the entry point with a restricted Unpickler (only `ledger_generator.LXState` and `fractions.Fraction` allowed). Top-level keys: ['counts','pair_weights','pattern_histogram','schema','signature_histogram','source_history_sha256']; len(pair_weights)=69800. Grepped all package .py for 117161/117_161/'collapse'/'aggregate' — no aggregation code. Missing hashes, taken from document C §3: primitive JSON 3685369c951036765f940612114419e76e27dd4f9efe79112053a48abd1faa33, canonical parsed primitive 2eda6c8940280d269e27983800d8f51d9cc51dc27735ef71823dfff37b1362ab, W2/R2 generator a72a2c412bfa3a7da3847ac4fe04c48fb5e1d1db7f95ae4e391c1ea31ca306ce, freeze e68d515899f03d1a84a028645b2f42e176bb0bb54c3b21be8be030da41f1dc26, history ledger 543869b10f5137ea74fbd5f27d25027dea66f936ce9844b77a029453b8bf8c97 — none present in the package.

**Verifier's corrected statement — authoritative.**

> HOLDS, with one overreach trimmed and one strengthening added. Reproduced from primary sources.
> 
> WHAT I VERIFIED MYSELF
> 
> 1. The misnamed key is real. Unpickling cert/root_exact_pair_topologies.pkl.gz with a restricted Unpickler (fractions.Fraction real; ledger_generator.LXState stubbed) gives a dict with keys exactly ['counts','pair_weights','pattern_histogram','schema','signature_histogram','source_history_sha256'], schema 'workhouse-exact-pair-topology-ledger-pickle-v1', len(pair_weights)=69800. `source_history_sha256` holds {'left_physical_blocks':3439,'matched_h0_blocks':5400,'raw_pair_upper_bound':9814138,'skipped_one_face_matches':54,'compatible_state_pairs':2468250,'observed_haar_patterns':[[0,3],[0,6],[1,1],[2,2],[3,0],[3,3],[6,0]],'unsupported_haar_patterns':[],'max_bra_ket_occurrences':24} — a counts dict, no digest. Sharper than the auditor stated: a regex over the full 12,458,390-byte decompressed pickle stream finds ZERO 64-hex substrings anywhere, and the only `sha`-shaped token in the entire stream is the key name `source_history_sha256` itself.
> 
> 2. No upstream hash is present. Grepping the whole package for the five document-C §3 chain hashes (be0baa19-...LINEAGE_TRACE...md:122-126: primitive JSON 3685369c..., canonical parsed primitive 2eda6c89..., W2/R2 generator a72a2c41..., freeze e68d5158..., history ledger 543869b1...) returns no file for any of the five. The 46 distinct 64-hex strings that do occur in the package's JSONs are the ledger/entry-point digests plus 44 per-topology digests in stratified_actual_topology_modular_audit.json — none bind upstream.
> 
> 3. No aggregation code. `117161` appears in zero of the 7 package .py files. It survives only as passthrough: modular_haar_contractor.py:525 copies payload["counts"]["historical_orientation_sensitive_topologies"] straight into the summary, and independent_replay_modular_crt.py:175 copies payload["counts"] wholesale as "source_counts". Grep for 5400 / 9814138 / 54 / skipped_one_face across all package .py: zero hits. Nothing recomputes or witnesses any census integer; the 117,161 -> 69,800 quotient is performed nowhere in the package.
> 
> 4. NEW — stronger than the auditor claimed. All four executable entry points import a module that is not shipped: modular_haar_contractor.py:31-32, independent_replay_modular_crt.py:18-19, independent_cross_check_actual_topologies.py:18-19 and crosscheck_modular_haar_reference.py:19-21 each sys.path.insert a `rank3_order4_cubic_ledger` directory and then `import ledger_generator`. That directory does not exist in the package (only ./ and ./modular_haar_run); the import raises ModuleNotFoundError: No module named 'ledger_generator'. Since the pickle's keys are ledger_generator.LXState instances, the package cannot even unpickle its own entry point as shipped. This directly falsifies AUDIT_REPORT.md:70, which asserts the ZIP contains "all contractor/replay sources needed to audit the route."
> 
> TRIMMED OVERREACH (the finding must not be written into the ledger as broader than this)
> The package DOES cryptographically bind its own entry point: SHA256SUMS.txt has 20 entries and all 20 verify OK, pinning root_exact_pair_topologies.pkl.gz = 5337734a57bd2e1fe690c636f19bc0f65c48bac86cc029a7e4dfe87251e8ff59, the same digest AUDIT_REPORT.md:63 lists and that rank3_order4_exact_haar_summary.json records as source_topology_ledger_sha256. The gap is strictly UPSTREAM of the pickle. "Zero cryptographic binding to anything that produced it" is correct as written; "the package has no hashes" would not be.
> 
> WHY THIS IS NOT A RESTATEMENT OF THE REPORTS' OWN CAVEAT
> AUDIT_REPORT.md:59 and INDEPENDENT_REFEREE_REPORT.md:62 both disclaim only that the frozen primitive generator is "a complete physical perturbation expansion" — a modeling/completeness caveat. The gap here is orthogonal: it is that the "frozen generator lineage" over which arithmetic closure IS asserted is itself not shipped, not hash-bound, and not recomputed from inside the package. Document C corroborates rather than contradicts: C:181-186 concedes that even in the external production route, 117,161 is "carried as the historical orientation-sensitive reference rather than recomputed", and that the only code path able to recompute it is the *unused* older collapse function.
> 
> CLASSIFICATION: (iii)+(i) mixed — the upstream artifacts are EXTERNAL to this repo (work/rank3_order4_cubic_ledger/, per the path mapping) and therefore unverifiable here, which is exactly the point: the package's self-contained closure claim at AUDIT_REPORT.md:59 and its completeness claim at :70 cannot be checked from the package, and :70 is demonstrably false as shipped. Nothing in /home/user/WORKHOUSE records this package or these hashes, so it is not already known.

**Why it holds.** Every element re-derived from primary sources, not taken on trust. Cited lines opened directly: AUDIT_REPORT.md:59 ("The arithmetic certificate is therefore closed for the frozen generator lineage.") and :63 (frozen source topology archive 5337734a...) read exactly as quoted; INDEPENDENT_REFEREE_REPORT.md:52 carries the 117,161/69,800/5,400/9,814,138/54 census as bare prose. Independently unpickled the entry point with a restricted Unpickler and got the six top-level keys and len(pair_weights)=69800 as claimed, and confirmed the misnamed field by a stronger test than the auditor ran: zero 64-hex substrings exist anywhere in the 12,458,390-byte decompressed stream, so the pickle contains no digest of any kind. Grepped all five document-C §3 upstream hashes across the package: none present. Grepped 117161/5400/9814138/54 across all 7 package .py files: zero hits, and located the two passthrough sites (modular_haar_contractor.py:525, independent_replay_modular_crt.py:175) proving the census integers are copied, never recomputed. I additionally found a defect the auditor missed that strengthens the finding: all four executable scripts import ledger_generator from a rank3_order4_cubic_ledger/ directory absent from the package (ModuleNotFoundError confirmed by execution), which falsifies AUDIT_REPORT.md:70's "all contractor/replay sources needed to audit the route". I attempted to refute on three grounds and each failed: the reports' disclaimers (AUDIT_REPORT.md:59 sentence 2, REFEREE:62) are scoped to physical completeness of the generator, not to lineage binding, so they do not cover this; document C:181-186 corroborates rather than rebuts, conceding 117,161 is carried not recomputed even externally; and nothing in /home/user/WORKHOUSE mentions this package, so it is not already recorded. The one genuine overreach — the implication of no binding at all — I trimmed: SHA256SUMS.txt's 20 entries all verify OK and do pin the entry point, so the gap is strictly upstream of the pickle.

---

### 5.6 `A-W22-null-only-at-one-face`

| | |
|---|---|
| **severity** | high |
| **class** | `artifact-wrong` |
| **lane** | `citations-AB` |
| **verifier confidence** | high |
| **where** | artifact A §3 (A:88-92) and §2 row 3 (A:59). Repo: corpus-import/programs/hodge_o4_adjudication/src/DATA_O4_OrderSchedule_Occurrence_Preflight_CPU.py:2-19, 46-48, 124-147, 609-610, 317-338 |

**Claim as stated.** "The corpus proves W22 is O4-null **only at one face**; multi-face W22-O4-safety is fit-argued, not exactly gated" (A §3), and "W22 (the branches' only structural difference) is exactly O4-null at one face" (A §2 row 3)

**What is wrong (originating auditor).** Contradicted by the very file A cites two lines earlier in its own reproduction list. DATA_O4_OrderSchedule_Occurrence_Preflight_CPU.py:609-610 gates "no O4 closed walk contains W22" and "W22 first enters a closed walk at order five" — and these are face-independent. `enumerate_closed_layer_walks` (:124-147) enumerates Motzkin walks on the Krylov layer index P/Q1/Q2 with no face data whatsoever; the pruning at :142 is what makes a Q2→Q2 step unreturnable in four steps. The file's own docstring, line 13, states the conclusion as "proves that W22 first appears at order five", unqualified by face count. What IS one-face-specific is only the 4-state exact-Fraction regression at :317-338 (h0=(8/3,20/3,12,32/3), layers (P,Q1,Q2,Q2)) that produces o4_equal and o5_difference=-5/7168. So A inverts the evidence: the general statement is the exactly gated one, and the one-face statement is the narrow numerical illustration. This weakens A §3's "named suspect" and the whole §4 framing, which rests on multi-face W22-O4-safety being unproven.

**Evidence (originating auditor).** DATA_O4_OrderSchedule_Occurrence_Preflight_CPU.py:609 `gates.require("no O4 closed walk contains W22", all((Q2, Q2) not in tuple(zip(w, w[1:])) for w in o4_walks), o4_walks)`; :610 `gates.require("W22 first enters a closed walk at order five", first_closed_order_with_block((Q2, Q2)) == 5, ...)`; :124-147 `def enumerate_closed_layer_walks(order)` — "All nonnegative Motzkin walks of exactly ``order`` steps from P to P", operating on integers P=0,Q1=1,Q2=2 (:46-48) with no face argument; :2-19 module docstring line 13 "proves that W22 first appears at order five". Second independent statement of the same fact: ENGINE_O4_hodge_rootonly_firewall_v1.py:10-12 "A layer-distance proof that a Q2-W-Q2 block first contributes at fifth order".

**Verifier's corrected statement — authoritative.**

> Artifact A misattributes the limit on W22-O4-nullity to face count. A:88-92 asserts "The corpus proves W22 is O4-null **only at one face**; multi-face W22-O4-safety is fit-argued, not exactly gated", and A:166 files DATA_O4_OrderSchedule_Occurrence_Preflight_CPU.py:610 under "W22 one-face exact facts". Line 610 is face-independent: it gates `first_closed_order_with_block((Q2,Q2)) == 5`, and :609 gates `all((Q2,Q2) not in tuple(zip(w,w[1:])) for w in o4_walks)`, both evaluated on `enumerate_closed_layer_walks` (:124-147) — nonnegative-integer Motzkin walks from P to P on the Krylov layer index (P=0,Q1=1,Q2=2, :46-48) with no face data anywhere in the function or its callers. I re-ran the extracted functions: order 4 yields exactly 9 closed walks ((0,0,0,0,0),(0,0,0,1,0),(0,0,1,0,0),(0,0,1,1,0),(0,1,0,0,0),(0,1,0,1,0),(0,1,1,0,0),(0,1,1,1,0),(0,1,2,1,0)), none containing a (2,2) step; walk counts by order are 1,1,2,4,9,21,51,127 with (2,2) first appearing at order 5. The file's own docstring line 13 states the conclusion unqualified: "proves that W22 first appears at order five". What is genuinely one-face-only is the exact-Fraction regression at :317-338 (h0=(8/3,20/3,12,32/3), layers (P,Q1,Q2,Q2)), gated at :614/:615/:616, which I reproduced: o4_equal=True, full[4] = -13/896, o5_difference = -5/7168 exactly. So the exactly-gated statement is the face-independent one and the one-face statement is the concrete numerical demonstration; A has them inverted.
> 
> Three corrections to the finding as originally worded, all verified: (1) "the pruning at :142 is what makes a Q2->Q2 step unreturnable in four steps" is FALSE — I re-ran the enumerator with `if nxt > remaining_after: continue` deleted and got the identical 9 walks at order 4 and 21 at order 5; the prune is pure early termination and the closure filter `path[-1] == P` is what excludes (2,2). (2) ENGINE_O4_hodge_rootonly_firewall_v1.py:10-11 ("A layer-distance proof that a Q2-W-Q2 block first contributes at fifth order") is corroboration, not an independent origin — same program directory, same LAYERS/LAYER_DEPTH construct (:45-46, :232-234), and its LAYERS tuple is capped at depth 2 where the DATA enumerator is uncapped; per AGENTS.md "repetition is not independence" it should not be cited as a second independent statement. (3) The finding's closing claim that this "weakens ... the whole §4 framing" is an overreach: A's own companion document D (e22209c0-...STRUCTURAL_TRACE...md:91) already gives the correct and still-standing reason for the decisive test — "exact perturbative power counting places the first `W22` contribution at fifth order, so the mere presence of the block does not prove that it changed the true fourth-order Taylor coefficient", the residual risk being that v10a24c diagonalizes at finite u and extracts coefficients by a degree-six fit on 13 points. A §4 Knob B (W22-off, order-truncated) remains motivated by that fit-vs-order-truncation gap, which is a property of the extraction method, not of face count.
> 
> A partial defense of A exists and should be recorded alongside: the :609/:610 gates are theorems about walks whose physical premise (W is layer-tridiagonal in the Krylov index, and the O(u^4) effective coefficient equals the sum over 4-step closed P->P walks) is machine-checked nowhere in this repo at ANY face count, while :614/:616 is a premise-free exact demonstration in an explicit 4-state Hamiltonian and is one-face-only. That is a real asymmetry — but it is an asymmetry of premise-freeness, not of face count, and it does not license the sentence A wrote.
> 
> Not already recorded here: the only W22 entry in the verification layer is settlement protocol item 10 (ledger/gaps.yaml:127; src/workhouse/invariants.py:670-679), a different subject. External blind-branch directories (work/rank3_order4_exact_haar_run/ etc.) are absent, so the blind branch's actual multi-face O4 extraction remains UNVERIFIABLE here.

**Why it holds.** I opened the cited file myself and re-executed the cited functions rather than trusting the evidence line. The gates at :609-610 operate on `enumerate_closed_layer_walks`, which takes only an integer order and enumerates nonnegative Motzkin walks — there is no face parameter in the function, its callers, or the module's O4_BLOCKS/DIRECTLY_COMPUTED_BLOCKS constants (:52-54); the only occurrences of "face" in the entire 695-line file are on lines 16, 303, 317, 613-616 and 635, all attached to the 4-state exact-Fraction regression. So A:88-92's "only at one face" and A:166's classification of :610 as a "one-face exact fact" are demonstrably wrong about what the repo gates. I reproduced every number (9 walks, first (2,2) at order 5, -13/896, -5/7168) and also falsified one of the auditor's own supporting claims (the :142 prune) by re-running the enumerator without it, and downgraded the finding's severity because A's companion document D:91 states the correct reason for the same decisive test, so A §4 does not collapse.

---

### 5.7 `B-83776-factorization`

| | |
|---|---|
| **severity** | high |
| **class** | `artifact-wrong` |
| **lane** | `citations-AB` |
| **verifier confidence** | high |
| **where** | artifact B §3, line 99 (B:99). Repo cross-refs: corpus-import/programs/hodge_o4_adjudication/src/ENGINE_O4_hodge_v10a21r_adjudicator_only_same_kernel.py:359 (VPAIR=_XQ(-327,83776)); corpus-import/records/audits/07-denominator-lift.md:38 |

**Claim as stated.** "83776 = 2⁷·7·11·17²    (in-scope, | QBOUND)"

**What is wrong (originating auditor).** The factorization is wrong. 83776 = 2^6·7·11·17. The printed product 2^7·7·11·17^2 equals 2848384, which is 34x too large. The likely source of the slip is the neighbouring denominator on the line above: 837760 = 2^7·5·7·11·17 (it does carry 2^7). The 17^2 is invented outright; nothing in the chain has 17^2 except den(D_EXACT), which has 17^3. The divisibility half of the parenthetical survives: 83776 divides den(D_EXACT)=7250590288602460800 and den(M4_EXACT)=14501180577204921600, so "| QBOUND" holds given D_EXACT=TOTAL_NUM/QBOUND (corpus-import/records/audits/07-denominator-lift.md:38).

**Evidence (originating auditor).** sympy.factorint(83776) = {2:6, 7:1, 11:1, 17:1}; 2**7*7*11*17**2 = 2848384; sympy.factorint(837760) = {2:7,5:1,7:1,11:1,17:1}; sympy.factorint(7250590288602460800) = {2:7,3:6,5:2,7:1,11:1,13:1,17:3,19:1,29:1,31:1,37:1}. Cross-check that the value itself is right: e4(C)-2*V1 = Fraction(-54321,837760) - 2*Fraction(-39,1280) == Fraction(-327,83776) exactly.

**Verifier's corrected statement — authoritative.**

> Artifact B line 99 prints "83776 = 2⁷·7·11·17²    (in-scope, | QBOUND)". The factorization is arithmetically wrong: 83776 = 2⁶·7·11·17 (= 64·1309, 1309 = 7·11·17; sympy.factorint(83776) = {2:6, 7:1, 11:1, 17:1}). The printed product 2⁷·7·11·17² = 2848384 = 34·83776. Both exponents are wrong (2⁶ not 2⁷; 17¹ not 17²). Confirmed on the raw bytes of B:99 (U+2077 and U+00B2 superscripts), so this is not a rendering artifact.
> 
> SCOPE — annotation only, no propagation. The value it annotates is correct: Fraction(-54321,837760) - 2*Fraction(-39,1280) == Fraction(-327,83776) exactly, matching the repo's own gates at corpus-import/programs/hodge_o4_adjudication/src/ENGINE_O4_hodge_v10a21r_adjudicator_only_same_kernel.py:359 (VPAIR=_XQ(-327,83776)) and .../ENGINE_O4_hodge_v10a7_marked_linked_scalar.py:5433-5434. The divisibility half also survives: 7250590288602460800 % 83776 == 0 (quotient 86547343972050); that is den(D_EXACT) as printed at corpus-import/records/audits/08-rooted-adjudication.md:53, in lowest terms (gcd(361008126292641364183, 7250590288602460800) = 1), and D_EXACT = TOTAL_NUM/QBOUND (corpus-import/records/audits/07-denominator-lift.md:38), so 83776 | QBOUND. "in-scope" is unaffected: {2,7,11,17} lies in QBOUND's prime set {2,3,5,7,11,13,17,19,29,31,37} under either factorization. B's neighbouring factorizations are correct (B:70 8960 = 2⁸·5·7; B:112 1675520 = 1280·1309 = 83776·20), so the slip is isolated. Severity should be downgraded from high to low/medium: it is a one-line erratum in a decorative annotation, not a defect in any computed quantity.
> 
> CORRECTION TO THE ORIGINATING AUDITOR'S RATIONALE: its evidence line claims "nothing in the chain has 17² except den(D_EXACT), which has 17³". That is false — factorint(140454) = {2:1, 3:5, 17:2} (denominator of FOLD_EX = 5315003/140454, cited on the same audit line 07-denominator-lift.md:38) and factorint(249696) = {2:5, 3:3, 17:2} each carry exactly 17², so a 17² is available elsewhere in the chain. The proposed provenance (2⁷ borrowed from the neighbouring 837760 = 2⁷·5·7·11·17 on B:97) is plausible but unproven and should not be stated as fact in any ledger entry.
> 
> Not previously recorded: grep for "83776" over ledger/ and index/ returns nothing.

**Why it holds.** I reproduced the discrepancy from primary sources rather than the evidence line: od -c on B:99 confirms the literal text, sympy.factorint gives 83776 = 2^6·7·11·17 against the printed 2^7·7·11·17^2 = 2848384 (34x), and exact Fraction arithmetic confirms the annotated value -327/83776 and the "| QBOUND" divisibility both stand. The error is real, checkable, and unrecorded in the repo, so the finding holds — but it is a non-propagating annotation error, not high severity, and the originating auditor's supporting claim that nothing else in the chain carries 17^2 is itself wrong (den(FOLD_EX) = 140454 = 2·3^5·17^2), which I corrected rather than passing through.

---

### 5.8 `B-fit-provenance-stale`

| | |
|---|---|
| **severity** | high |
| **class** | `repo-wrong-or-stale` |
| **lane** | `citations-AB` |
| **verifier confidence** | high |
| **where** | artifact B §5 item 2 (B:167-170); artifact A §3 (A:88-92) and §4 Knob B (A:105, A:108-113). Repo: corpus-import/records/transcripts/15 hour RUN.txt:7220-7246, 6799-6800, 7670, 9143-9144, 9190, 10617 |

**Claim as stated.** "the blind v10a.24c basis admits `Q2↔Q2` and extracts coefficients by a degree-6 fit on 13 points — an order-truncated `W22`-off comparison is required before its size-2 is promotable — `ENGINE…v10a24c…py:6894-6899, 6928-6946`"

**What is wrong (originating auditor).** The cited line ranges are real and do contain the 13-point degree-6 fit — but in the OLDER engine. The run that produced the number B is targeting (size 2 c4 = -0.403971702978 at 15 hour RUN.txt:10621) retired that fit. In that run the production coefficients come from an order-4 Schrieffer-Wolff/BCH block diagonalization (`_v26_sw_blocks(one,4)`), and the 13-point fit survives only as a one-face audit. So the premise of B §5(2) and of A §4 "Knob B" (recompute blind two-face O4 W22-off, order-truncated, to test for "W22 fit contamination") describes a method the cited run does not use: the run's production coefficients are already order-truncated at O(u^4) by construction. The discriminator A §4 calls "the discriminator between fit artifact and real physics" is, for these numbers, aimed at a fit that was not used.

**Evidence (originating auditor).** 15 hour RUN.txt:7230-7246 — `def _v23c_fit_cluster(C,audit_legacy=False)` computes `c=[sum(op[r][root_i,same])-vp[r][0,0] for r in range(5)]` from `_v26_sw_blocks(one,4)`, returns `'method':'canonical Hermitian SW/BCH through O(u^4)'`, and only runs `_v26_legacy_fit_models` (docstring: "Audit only: reproduce the retired 13-point fit", :7220-7227) when audit_legacy=True. 15 hour RUN.txt:6799-6800 and :9143-9144 print "production coefficients : canonical Hermitian SW/BCH through O(u^4)" / "retired fit (one-face audit only) : symmetric polynomial, umax= 0.055 deg= 6 N= 13". :7670 and :10617 print "production coefficient method: canonical Hermitian SW/BCH; no polynomial fit/window". :9190 [PASS] "exact SW agrees with the retired symmetric fit on the one-face audit :: max coefficient difference=2.267e-07". The [16] table at :7672-7681 sums `raw[C]=shape_cache[key]['coef']`, i.e. the SW coefficients. The fit constants B describes do exist at ENGINE_O4_hodge_v10a24c_rootedfullt1_dualcoldoracle_a100.py:6793-6794 (DEG default '6', N default '13').

**Verifier's corrected statement — authoritative.**

> ARTIFACT-WRONG (not repo-wrong-or-stale): artifacts B and A misattribute the extraction method behind the number they target.
> 
> WHAT IS WRONG. B §5 item 2 (/root/.claude/uploads/384fab32-8991-52ce-b2bf-4999d379e3f5/6a2b59cb-F07_VS_BLIND_TWOFACE_ADJUDICATION.md:168-170) asserts "the blind v10a.24c basis admits Q2<->Q2 and extracts coefficients by a degree-6 fit on 13 points", citing ENGINE...v10a24c...py:6894-6899, 6928-6946, as the ground for requiring an "order-truncated W22-off comparison" before the blind size-2 is promotable. A repeats it: A:90 "the blind branch admits W22 and extracts O4 by a finite-u degree-6 fit"; A:91-92 and A:131-133 "multi-face W22-O4-safety is fit-argued, not exactly gated"; A:108/112 name the discriminator "W22 fit contamination". The second clause is FALSE for the number both documents target.
> 
> PROVENANCE OF THE TARGET NUMBER (single origin). "size 2 ... c4=-0.403971702978" occurs at exactly two places in the corpus: /home/user/WORKHOUSE/corpus-import/records/transcripts/15 hour RUN.txt:10621 and its copy 15 hour RUN. results.txt:2862 (grep -rn "403971" over transcripts; zero hits in src/, ledger/, index/, docs/, theory/). B:161 and A:103 cite 15 hour RUN.txt:10621 explicitly, so this is unambiguously their source.
> 
> THAT NUMBER IS SW/BCH, NOT A FIT. In that run: the [16] table (15 hour RUN.txt:7672-7683) sums raw[C] (:7675); raw[C]=shape_cache[key]['coef'].copy() (:7658); shape_cache filled by z=_v23c_fit_cluster(C) with the default audit_legacy=False (:7642). _v23c_fit_cluster (:7230-7246) computes op,ooff=_v26_sw_blocks(one,4); vp,voff=_v26_sw_blocks(vac,4) (:7232) and c=np.asarray([float(np.sum(op[r][root_i,same])-vp[r][0,0]) for r in range(5)]) (:7235), returning 'method':'canonical Hermitian SW/BCH through O(u^4)' (:7246). _v26_sw_blocks (:7149-7171) is an order-by-order BCH/SW polynomial recursion truncated at order=4 (_v26_poly_mul/_v26_poly_comm/_v26_bch, :7126-7147); its header comment states "no u-grid or polynomial fit enters the production coefficient" (:7124). The 13-point deg-6 fit survives only as _v26_legacy_fit_models, docstring "Audit only: reproduce the retired 13-point fit" (:7220-7221), invoked once on the one-face preflight cluster via audit_legacy=True (:7613) and gated at :7621. The run prints this in three places: "production coefficients : canonical Hermitian SW/BCH through O(u^4)" / "retired fit (one-face audit only) : symmetric polynomial, umax= 0.055 deg= 6 N= 13" (source :6799-6800, output :9143-9144); "production coefficient method: canonical Hermitian SW/BCH; no polynomial fit/window" (source :7670, output :10617); and [PASS] "v10a.26 exact SW agrees with the retired symmetric fit on the one-face audit :: max coefficient difference=2.267e-07" (:9190).
> 
> INDEPENDENT NUMERIC CORROBORATION (recomputed here in Fraction). The same [16] table's size-1 entry, c4=+0.0159598214286 (15 hour RUN.txt:10620), against the exact 143/8960 = -13/896 + 39/1280 = 0.015959821428571427: |diff| = 2.857e-14, which is the .12g print-precision floor, i.e. 7.935e6 times tighter than the 2.267e-07 fit-vs-SW discrepancy the run itself records on that very cluster. A deg-6 fit on 13 points over |u|<=0.055 carrying 2.267e-07 error cannot yield that agreement.
> 
> B'S FILE CITATION IS ACCURATE, ITS ATTRIBUTION IS NOT. In ENGINE_O4_hodge_v10a24c_rootedfullt1_dualcoldoracle_a100.py the cited lines are real: :6934-6946 is the production _v23c_fit_cluster returning 'coef' from _V23Poly.fit(us, ys, deg=V23C_FIT_DEG) with V23C_FIT_DEG=6, V23C_FIT_N=13 (:6793-6794); :6894-6899 is the full-basis W build. But that engine's own production transcript ("# HODGE v10a.24c - production runti.txt") aborted with KeyboardInterrupt inside [15] (:8771, :8776) and never printed [16] (its [16] source is at :7269) - so v10a.24c is the source of no per-size c4 anywhere in the corpus. The [16] banner in the 15-hour run still reads "HODGE v10a.23" (:9136), which is the plausible cause of B's misattribution.
> 
> SCOPE LIMIT - the auditor's conclusion overreaches on one point. B's first clause ("the basis admits Q2<->Q2") remains TRUE of the v10a.26 run: 15 hour RUN.txt:7094-7098 builds W over the full basis including layer2, structurally identical to ENGINE...v10a24c...py:6894-6899, and _v23c_fit_cluster reports q2=one['layer2']>0 (:7244; e.g. q1/q2=60/564 at :10607). So A's Knob B (W22-off recomputation, A:104) is not itself refuted - only its stated motivation is. What is refuted is the claim that the blind size-2 c4 is fit-derived and therefore suspect for finite-u truncation leakage; it is already order-truncated at O(u^4) by construction, so "fit artifact" (A:108, A:112) is not a live explanation for the -0.403971702978 value, and A:131-133's "multi-face W22-O4-safety is fit-argued rather than exactly proven" rests on a method the run does not use. Whether W22 can enter the O(u^4) P-block of a full-basis SW recursion is a separate question that neither this check nor the auditor settles; do not record it as settled.
> 
> KIND CORRECTION. The finding's kind field ("repo-wrong-or-stale") is wrong. The repository is not stale here: it carries no copy of -0.403971702978, and ledger/provenance.yaml:120-121 already names the run family NB_O4_hodge_v10a26_factor52complete_exactsw_rootedoracle_a100_alt2.ipynb ("exactsw"). Nothing in the repo asserts the fit provenance; only artifacts A and B do.

**Why it holds.** I reproduced the finding independently from primary sources rather than trusting its evidence line. Every cited line number checked out on inspection (15 hour RUN.txt:6799-6800, 7124, 7126-7171, 7220-7227, 7230-7246, 7613, 7621, 7642, 7658, 7670, 7672-7683, 9143-9144, 9190, 10617, 10620-10621; ENGINE...v10a24c...py:6793-6794, 6894-6899, 6934-6946). Three independent confirmations: (1) the code path from the printed table back to _v26_sw_blocks(.,4) is unbroken and carries no fit; (2) the run prints "no polynomial fit/window" three times and labels the 13-point fit "retired"/"one-face audit only"; (3) numerically, the same table's size-1 c4 matches the exact 143/8960 to 2.857e-14, 7.9e6x tighter than the run's own 2.267e-07 fit-vs-SW gap, which the fit could not achieve. I also closed the obvious escape route for the artifacts - that some v10a.24c run produced the same value - by grepping the whole corpus (only the 15-hour run and its results copy) and confirming the 24c production transcript died on KeyboardInterrupt before [16]. I narrowed two overreaches in the finding as written: B's Q2<->Q2 clause is still true of the run (15 hour RUN.txt:7094-7098), so the W22-off knob is not refuted, only its "fit contamination" motivation; and the kind is artifact-wrong, not repo-wrong-or-stale, since the repo holds no copy of the number and already labels the run family exactsw.

---

### 5.9 `d-wrong-engine-version`

| | |
|---|---|
| **severity** | high |
| **class** | `artifact-wrong` |
| **lane** | `citations-CD` |
| **verifier confidence** | high |
| **where** | artifact D §2 (lines 79-91), §1 (line 27), §9 (line 221); repo corpus-import/programs/hodge_o4_adjudication/src/ENGINE_O4_hodge_v10a24c_rootedfullt1_dualcoldoracle_a100.py:6792-6794; corpus-import/records/transcripts/15 hour RUN.txt:3,6800,7123,7149-7170,10614,10617,10620 |

**Claim as stated.** D §2: "The v10a24c implementation, however, diagonalizes at finite `u` and extracts coefficients using a degree-six fit on 13 points (`ENGINE...v10a24c...py:6928-6946`). An exact order-truncated `W22`-off comparison is therefore required before the blind fourth-order scalar can be promoted." D §2 also introduces v10a24c as "the blind branch" that produced m_{4,blind}.

**What is wrong (originating auditor).** The statement about v10a24c's source is true, but every blind number D quotes comes from a DIFFERENT engine, v10a.26, which explicitly retired the polynomial fit and replaced it with order-truncated Hermitian SW/BCH. D's central section-2 objection therefore does not apply to the numbers it is levelled against. The W22 block is genuinely still present in v10a.26, but the leakage channel D names (finite-u diagonalization + degree-6 fit) is exactly what v10a.26 removed, and in an order-truncated BCH the first W22 path P->Q1->Q2->Q2->Q1->P needs five V-factors and cannot reach order 4.

**Evidence (originating auditor).** v10a24c defaults confirmed: V23C_FIT_DEG='6' at ENGINE_O4_hodge_v10a24c...py:6793, V23C_FIT_N='13' at :6794, V23C_FIT_UMAX='0.055' at :6792 — so D's "degree-six fit on 13 points" is exact for that FILE. But the producing run is v10a.26: banner "# HODGE v10a.26 — FACTOR-(5,2) COMPLETE + EXACT-SW ROOTED ORACLE" at '15 hour RUN.txt':3; "retired fit (one-face audit only)" at :6800; "# returns the canonical Hermitian P block directly; no u-grid or polynomial fit" at :7123; order-truncated BCH `_v26_sw_blocks(model,order=4)` at :7149-7170; executed output four lines above the rows D cites: "production coefficient method: canonical Hermitian SW/BCH; no polynomial fit/window" at :10617 and "[PASS] v10a.26 exact SW block diagonalization closes through O(u^4) :: max P-Q residual=5.551e-16" at :10614. No executed v10a24c run in this repo produces these numbers: `grep -rn '^  size 1: c1=' corpus-import/records/transcripts/` returns only '15 hour RUN.txt':10620 and '15 hour RUN. results.txt':2861, both v10a.26; the v10a24c transcript ('# HODGE v10a.24c — production runti.txt', 9099 lines) contains only source print statements at :7278/:7302, no [16]/[17] output.

**Verifier's corrected statement — authoritative.**

> CONFIRMED (artifact-wrong), with one narrowing and one attribution correction.
> 
> WHAT I REPRODUCED
> 
> 1. D's premise is true of the FILE. /home/user/WORKHOUSE/corpus-import/programs/hodge_o4_adjudication/src/ENGINE_O4_hodge_v10a24c_rootedfullt1_dualcoldoracle_a100.py (7370 lines) defaults V23C_FIT_UMAX='0.055' (:6792), V23C_FIT_DEG='6' (:6793), V23C_FIT_N='13' (:6794); `_v23c_fit_cluster` at :6934 builds `us=np.linspace(-UMAX,UMAX,13)` (:6936), evaluates a finite-u des-Cloizeaux gap, and fits `_V23Poly.fit(us,ys,deg=6)` (:6939). That file contains no `_v26_sw_blocks`, no string "v10a.26", no "retired fit" (grep: zero hits).
> 
> 2. But the numbers D quotes are not from that file's method. Every blind value D cites is at corpus-import/records/transcripts/15 hour RUN.txt, whose banner is "# HODGE v10a.26 — FACTOR-(5,2) COMPLETE + EXACT-SW ROOTED ORACLE" (:3). In that program `_v23c_fit_cluster` is REDEFINED at :7230 as `def _v23c_fit_cluster(C,audit_legacy=False)` and its production coefficients come from `op,ooff=_v26_sw_blocks(one,4); vp,voff=_v26_sw_blocks(vac,4)` (:7232) — an order-truncated Hermitian SW/BCH recursion defined at :7149-7176 under the comment "no u-grid or polynomial fit enters the production coefficient" (:7123). It returns `'method':'canonical Hermitian SW/BCH through O(u^4)'` (:7246). The legacy polynomial fit survives only behind `audit_legacy=True`, called once for the one-face preflight at :7613; the run's own banner prints "production coefficients : canonical Hermitian SW/BCH through O(u^4)" (:6799) and "retired fit (one-face audit only)" (:6800).
> 
> 3. The cited rows are downstream of that. `raw[C]=shape_cache[key]['coef'].copy()` (:7658), shape_cache filled at :7642 from the redefined `_v23c_fit_cluster`; the [16] rooted-incidence loop is :7673-7681. Executed output: :10614 "[PASS] v10a.26 exact SW block diagonalization closes through O(u^4) :: max P-Q residual=5.551e-16"; :10617 "production coefficient method: canonical Hermitian SW/BCH; no polynomial fit/window"; :10619 "[16]"; :10620 size 1 c4=+0.0159598214286; :10621 size 2 c4=-0.403971702978; :10626 TOTAL m4 = -0.7751458630189173. D cites exactly these at its lines 24/27, 54, 218/221.
> 
> 4. No executed v10a24c run produces them. `grep -rn '^  size 1: c1=' corpus-import/records/transcripts/` returns only "15 hour RUN.txt":10620 and "15 hour RUN. results.txt":2861 — both v10a.26 (results.txt carries the same v10a.26 PASS lines at :1386-1389). The v10a24c transcript ("# HODGE v10a.24c — production runti.txt", 9099 lines) has the [16]/[17] `print(...)` calls only as SOURCE at :7269 and :7294 (the size-row print is :7277, TOTAL at :7278) and terminates in a bare `KeyboardInterrupt` — consistent with "the exact hot path that was manually interrupted in v10a.24c" (15 hour RUN.txt:6804).
> 
> 5. The fit could not have produced these digits. results.txt:1431: "[PASS] v10a.26 exact SW agrees with the retired symmetric fit on the one-face audit :: max coefficient difference=2.267e-07". The retired fit is accurate to ~2.3e-7 — 4.4e5 times larger than the 5.1725e-13 gap the repo tracks between 8*HAMER_A4_NUM = -0.7751458630184 and M_GAMMA_4_NUM = -0.7751458630189173 (src/workhouse/invariants.py:390). The printed size-1 c4 also matches 143/8960 = 0.015959821428571427 to 2.86e-14 (print-width limited), impossible from a 2e-7-accurate fit.
> 
> 6. D's remaining demand is moot, and I verified this exactly, not by assertion. In an order-truncated SW/BCH over a layered Krylov basis (P/Q1/Q2, W nonzero only between adjacent layers — which holds because Q2 vectors are Gram-Schmidted against all earlier same-H0-key vectors including layer 1, forcing <Q2|W|P>=0 up to the 1e-13 ortho threshold), zeroing the Q2-Q2 block leaves the effective P block bit-identical through order 4. My exact-rational reimplementation of `_v26_sw_blocks` over 40 random layered models (Fraction arithmetic, order-6 truncation) gives max |W22-on minus W22-off| = 0 exactly at orders 0,1,2,3,4 and first nonzero at order 5 (81/8) and 6 (1130245/15552). So the "exact order-truncated W22-off comparison" D says is "required" is (a) already order-truncated in the producing run, and (b) provably a null comparison at order 4.
> 
> NARROWING (why this is not simply "wrong engine version")
> 
> D's naming is partly defensible: the v10a.26 program's own section header for this leg literally reads "# HODGE v10a.24c — INDEPENDENT ROOTED FINITE-CLUSTER LINKED-GAP ORACLE" (15 hour RUN.txt:6750) and its gates print "v10a.23" labels (:10627-10629). The defect is not the version label but the mechanism: D asserts the blind fourth-order coefficients were extracted by finite-u diagonalization + degree-6/13-point fit, and they were not. D also frames W22-freedom at order four as a property of a not-yet-built "current canonical architecture" (line 91) when the executed run already has it. D nowhere mentions v10a.26 (grep 'v10a' over D: lines 79, 91, 101, 103, 108, 207 — all "v10a24c").
> 
> WHAT SURVIVES IN D
> 
> D's structural observation is correct and unchanged in v10a.26: `_v23c_build_basis` still builds the dense W over every retained basis vector with no layer mask (15 hour RUN.txt:7094-7098, identical to v10a24c.py:6894-6899), so the Q2-Q2 block is materially present. Only the leakage channel D names is gone.
> 
> PROVENANCE OF D'S ERROR (repo-side note, not a repo defect per se)
> 
> D's sentence tracks corpus-import/records/audits/02-duplication-report.md:46 — "F09's cluster result is a fitted numeric coefficient (`v10a24c.py:6934-6946`)" — the same line range D cites. That audit statement is true of the source file but would be false if applied to the numbers in "15 hour RUN.txt". Relatedly, corpus-import/records/audits/05-latest-run-forensics.md:26 lists the v10a.26 notebook as "unique source candidate; no run evidence" while "15 hour RUN.txt" is an executed v10a.26 log identified as such at theory/superseded/MASTER_THEORY.md:44 ("v10a.26 A100 run log/results"). Nothing currently checked in the repo records that M_GAMMA_4_NUM (src/workhouse/constants.py:207) came from exact-SW rather than a fit; src/workhouse/constants.py:202-206 says only "from the blind finite-cluster/rooted oracle (float only)".
> 
> SEVERITY: I would set medium-high rather than high. D's literal sentence about the file is true; the error is in the "therefore", and its practical cost is (i) an unwarranted implication that the blind m4 is fit-contaminated and (ii) an unnecessary requirement #2 ("make W22 unschedulable at order four") in D's line 221-226 work plan.

**Why it holds.** I opened all cited lines myself. The v10a24c .py file does default to a degree-6 / 13-point fit (:6792-6794, :6934-6942) and contains no v10a.26 code, so D's premise about the FILE is true. But the producing run, "15 hour RUN.txt", is v10a.26 (banner :3) and redefines _v23c_fit_cluster at :7230 to take its production coefficients from the order-truncated SW/BCH _v26_sw_blocks (:7149, :7232), with the polynomial fit demoted to an audit_legacy one-face path (:6800, :7613); the executed output says so directly at :10617 and passes an exact-SW closure gate at :10614, three lines above the [16] rows D cites (:10620-10626). grep shows the only two files containing these rows are the v10a.26 log and its results file; the v10a24c transcript holds those prints as source only and ends in KeyboardInterrupt. Quantitatively the fit cannot be the source: results.txt:1431 records the retired fit disagreeing with exact SW by 2.267e-07, 4.4e5x the 5.1725e-13 residual the repo tracks against 8*HAMER_A4_NUM, and the size-1 row matches 143/8960 to 2.86e-14. Finally I reimplemented the SW/BCH recursion in exact Fractions and confirmed over 40 random layered models that removing the Q2-Q2 block changes the effective P block by exactly 0 at orders 0-4 and first at order 5 (81/8) — so D's demanded W22-off comparison is a null test at order four. The finding is real; I narrowed it (the run's own section header does say "v10a.24c", so the defect is the fit-extraction attribution, not the version label alone) and traced its origin to corpus-import/records/audits/02-duplication-report.md:46.

---

### 5.10 `blind-table-is-v10a26-exact-SW-not-a-degree-6-fit`

| | |
|---|---|
| **severity** | high |
| **class** | `artifact-wrong` |
| **lane** | `corpus-value-search` |
| **verifier confidence** | high |
| **where** | A §3 "The named suspect", A §4 "Knob B"; B §0, §5 item 2, §6; D §2 "Blind finite-cluster branch" — vs corpus-import/records/transcripts/15 hour RUN.txt:3,10614,10617 and corpus-import/programs/hodge_o4_adjudication/notebooks/NB_O4_hodge_v10a26_factor52complete_exactsw_rootedoracle_a100.ipynb:7171,7242,7252-7268 |

**Claim as stated.** "the blind v10a.24c basis admits Q2↔Q2 and extracts coefficients by a degree-6 fit on 13 points — an order-truncated W22-off comparison is required before its size-2 is promotable" (B §5.2); "The blind linked-cluster oracle (v10a.23/24c rooted incidence transform) measures m₄,blind = −0.7751458630189173" (B §0); "the blind branch admits W22 and extracts O4 by a finite-u degree-6 fit" (A §3); "Knob B — blind two-face O4 recomputed W22-off (order-truncated)" (A §4); "The v10a24c implementation, however, diagonalizes at finite u and extracts coefficients using a degree-six fit on 13 points" (D §2)

**What is wrong (originating auditor).** The per-size table all four documents quote was NOT produced by v10a.24c's degree-6 fit. `15 hour RUN.txt` is a v10a.26 run (header line 3), and in v10a.26 `_v23c_fit_cluster` is REDEFINED to extract coefficients from an order-graded canonical Hermitian SW/BCH recursion (`_v26_sw_blocks(model,4)`), returning `fit_stability: 0.0` and `method: 'canonical Hermitian SW/BCH through O(u^4)'`. The 13-point degree-6 fit survives only as `_v26_legacy_fit_models`, whose own docstring says "Audit only: reproduce the retired 13-point fit". The run prints "production coefficient method: canonical Hermitian SW/BCH; no polynomial fit/window" three lines above the table the documents cite, and gates "v10a.26 exact SW block diagonalization closes through O(u^4) :: max P-Q residual=5.551e-16" and "v10a.26 NumPy SW recursion matches the exact rational BCH oracle through O(u^4)" (<5e-12). Because the extraction is order-graded, W22 cannot enter the order-4 P block at all (the corpus's own Motzkin-walk gate: "no O4 closed walk contains W22"). The documents' central named suspect — "W22 fit contamination" — and their Knob B discriminator are therefore aimed at a retired code path, not at the number they are comparing against.

**Evidence (originating auditor).** corpus-import/records/transcripts/15 hour RUN.txt:3 ("# HODGE v10a.26 — FACTOR-(5,2) COMPLETE + EXACT-SW ROOTED ORACLE"); :10614 "[PASS] v10a.26 exact SW block diagonalization closes through O(u^4) :: max P-Q residual=5.551e-16"; :10617 "production coefficient method: canonical Hermitian SW/BCH; no polynomial fit/window"; :10619-10626 the quoted table. NB_O4_hodge_v10a26_factor52complete_exactsw_rootedoracle_a100.ipynb:7171 `def _v26_sw_blocks(model,order=4)` (order-by-order H[0],H[1]=V, S[r], BCH); :7242-7243 `def _v26_legacy_fit_models` / "Audit only: reproduce the retired 13-point fit"; :7252-7268 the redefined `_v23c_fit_cluster` returning 'fit_stability':0.0 and 'method':'canonical Hermitian SW/BCH through O(u^4)'. The degree-6 fit the documents cite is the OLD v10a.24c body at ENGINE_O4_hodge_v10a24c_rootedfullt1_dualcoldoracle_a100.py:6939-6946 (`_V23Poly.fit(us,ys,deg=V23C_FIT_DEG)`). Order-4 W22 exclusion gated at DATA_O4_OrderSchedule_Occurrence_Preflight_CPU.py:609-610.

**Verifier's corrected statement — authoritative.**

> HOLDS (artifact-wrong), with one calibration to D.
> 
> WHAT I REPRODUCED FROM PRIMARY SOURCES
> 
> 1. Provenance of the quoted table. `/home/user/WORKHOUSE/corpus-import/records/transcripts/15 hour RUN.txt:3` = "# HODGE v10a.26 — FACTOR-(5,2) COMPLETE + EXACT-SW ROOTED ORACLE". The per-size table the documents cite is at :10620-10626 (`size 2 ... c4=-0.403971702978`; `TOTAL m1/m2/m3/m4 = ... -0.7751458630189173`), i.e. exactly where B:232 says it is. Searching the whole repo for `403971702978` returns exactly three hits, all v10a.26 outputs: `15 hour RUN.txt:10621`, `15 hour RUN. results.txt:2862`, `NB_O4_hodge_v10a26_..._alt2.ipynb:2898`. No v10a.24c output of that table exists here: the v10a.24c production transcript (`corpus-import/records/transcripts/# HODGE v10a.24c — production runti.txt`) terminates in `KeyboardInterrupt` at :9099 and never reaches its own section [16] (source print at :7278). So the number is a v10a.26 product and nothing else.
> 
> 2. The extraction method in that run is order-graded SW/BCH, not a fit. In the transcript's own embedded source: `_v23c_fit_cluster` (:7230-7246) calls `_v26_sw_blocks(one,4)` / `_v26_sw_blocks(vac,4)` (:7149-7170, order-by-order H[0]=diag(H0), H[1]=V, S[r], BCH), takes `c[r] = Σ op[r][root,same] - vp[r][0,0]` for r=0..4, and returns `'fit_stability':0.0` and `'method':'canonical Hermitian SW/BCH through O(u^4)'`. The 13-point degree-6 fit survives only as `_v26_legacy_fit_models` (:7220, docstring :7221 "Audit only: reproduce the retired 13-point fit"), invoked exactly once with `audit_legacy=True` on the one-face preflight (:7613). The run states this itself at :6799-6800 ("production coefficients : canonical Hermitian SW/BCH through O(u^4)" / "retired fit (one-face audit only)") and again at :10617, two lines above the [16] header and three above the first table row: "production coefficient method: canonical Hermitian SW/BCH; no polynomial fit/window". Identical code in `corpus-import/programs/hodge_o4_adjudication/notebooks/NB_O4_hodge_v10a26_factor52complete_exactsw_rootedoracle_a100.ipynb:7171` (`_v26_sw_blocks`), :7242-7243 (legacy docstring), :7252-7268 (redefined `_v23c_fit_cluster`). All notebook line numbers in the finding are correct.
> 
>    Gates in that run: SW-vs-exact-rational-BCH regression `2.6645352591003757e-15` (tol 5e-12) at :9148; `max P-Q residual=5.551e-16` (tol 2e-10) at :10614; and the one-face legacy-fit comparison `max coefficient difference=2.267e-07` (tol V23C_FIT_STAB_TOL=5e-3) at :9190 — the two methods are 2.267e-07 apart even at one face, five orders of magnitude above the 5.17e-13 discrepancy under discussion, which is itself evidence the fit is not the source of the quoted digits.
> 
> 3. The degree-6 fit is v10a.24c's, and only v10a.24c's. `corpus-import/programs/hodge_o4_adjudication/src/ENGINE_O4_hodge_v10a24c_rootedfullt1_dualcoldoracle_a100.py:6934-6946` is `_v23c_fit_cluster` with `us=np.linspace(-0.055,0.055,13)`, `_V23Poly.fit(us,ys,deg=6)`, plus a 0.76-window inner refit and `fit_stability=|c4(full)-c4(inner)|`. That file contains no `_v26_sw_blocks` and no SW/BCH path (grep: zero hits).
> 
> 4. W22 cannot enter an order-graded O4 P block. I re-implemented the Motzkin enumeration of `DATA_O4_OrderSchedule_Occurrence_Preflight_CPU.py:124-146` from scratch: exactly 9 closed 4-step P→P walks, max depth Q2, none containing a (Q2,Q2) step, first appearance of (Q2,Q2) at order 5 — matching gates at :607-610 verbatim. The exact one-face sensitivity gates at :614-616 give O4 coefficients equal with and without W22, O4 = -13/896, first O5 bite = -5/7168. The argument is layer-generic, not one-face-specific; it needs only ⟨P|W|Q2⟩=0, which holds by construction in `_v23c_build_basis` (layer2 is orthogonalized within each H0 key against layer1, and W|P⟩ is exhausted into layer1).
> 
> WHERE EACH DOCUMENT FAILS
> 
> - A §3 (`52ebdfa7-...MASTER_RECORD.md:90`): "the blind branch admits W22 and extracts O4 by a finite-`u` degree-6 fit" — flatly false of the run that produced the number. A:91-92 "multi-face W22-O4-safety is fit-argued, not exactly gated" inherits the error.
> - A §4 Knob B (`:104`, `:108`, `:112`): "blind two-face O4 recomputed W22-off (order-truncated)" is a provable no-op. Because the blind extraction is already order-truncated at r=4, zeroing W22 changes the O4 coefficient only by float roundoff, so Knob B carries zero discriminating information between "W22 fit contamination" and "genuine multi-face physics". The stated discriminator does not discriminate.
> - A §5 (`:131`): "has a multi-face fit-stability guard" is also false for this run — `fit_stability` is hardcoded 0.0 (`15 hour RUN.txt:7242`); the `max_fit_stab` gate exists only in v10a.24c (`ENGINE...v10a24c...py:7280`), which never reached it.
> - B §0 (`6a2b59cb-...md:19-20`): calling the source "v10a.23/24c rooted incidence transform" is a half-defensible lineage label (the v26 run's own banner at :6792 and gates at :10627-10629 are printed as "v10a.23"), but the method attribution behind it is wrong.
> - B §5 item 2 (`:167-170`): "the blind v10a.24c basis admits Q2↔Q2 and extracts coefficients by a degree-6 fit on 13 points — an order-truncated W22-off comparison is required before its size-2 is promotable". The basis clause is true (v10a.26 also feeds the full W, W22 included, into `_v26_sw_blocks`); the extraction clause is false for the cited number, and the "required comparison" is already discharged, exactly, by the order-grading plus the repo's own gates at DATA_O4...:609-610.
> - D §2 (`e22209c0-...md:91`) — CALIBRATION: read literally, D's sentence "The v10a24c implementation, however, diagonalizes at finite u and extracts coefficients using a degree-six fit on 13 points (`ENGINE...v10a24c...py:6928-6946`)" is an accurate description of v10a.24c. D's error is the inference in the next sentence — "An exact order-truncated W22-off comparison is therefore required before the blind fourth-order scalar can be promoted" — which silently identifies the blind fourth-order scalar with the v10a.24c code path. It is not: it is a v10a.26 output, and D:95 even names "canonical Hermitian SW/BCH" as the prescription that "avoids the ambiguity", not noticing that the blind run already printed that exact phrase as its production method.
> 
> NOT ALREADY RECORDED HERE. The repo consistently attributes the 15-hour run and m_Γ^(4) to v10a.26 (`src/workhouse/constants.py:9,163`; `theory/superseded/MASTER_THEORY.md:44-45,565`; `ledger/provenance.yaml:120-125`), and nowhere states that the blind oracle used a polynomial fit. So the documents' claim contradicts the repo's own provenance as well as the transcript.
> 
> NET EFFECT. The one axis all four documents nominate as the structural difference between the F07 and blind branches — W22 entering the blind O4 through a finite-u degree-6 fit — is aimed at a code path (`_v23c_fit_cluster` as of v10a.24c) that produced none of the numbers under adjudication. The 10.293333600759848 gap is not explained by fit contamination, and Knob B must be withdrawn as a discriminator. The one-face agreement at 143/8960 and the size-2 target -0.403971702978 are unaffected; the multi-face question stays open on the other grounds the documents give (rooted Möbius, polarization restriction to index 2, Stage-3H crosswalk).

**Why it holds.** Every cited line reproduced from primary sources. `15 hour RUN.txt:3` is a v10a.26 header; :10617 prints "production coefficient method: canonical Hermitian SW/BCH; no polynomial fit/window" three lines above the cited table; the run's own embedded source at :7230-7246 shows `_v23c_fit_cluster` calling `_v26_sw_blocks(...,4)` and returning `fit_stability:0.0`, with the 13-point degree-6 fit demoted to `_v26_legacy_fit_models` ("Audit only", :7221) and run once on the one-face preflight only (legacy-vs-SW difference 2.267e-07 at :9190). The degree-6 fit the documents describe is v10a.24c's `_v23c_fit_cluster` at ENGINE...v10a24c...py:6934-6946, and that engine's production transcript died in KeyboardInterrupt at :9099 before section [16]; the value -0.403971702978 occurs in exactly three places in the repo, all v10a.26 outputs. I independently re-enumerated the Motzkin walks (9 closed 4-step P→P walks, max depth Q2, no (Q2,Q2) step, first at order 5), matching DATA_O4_OrderSchedule_Occurrence_Preflight_CPU.py:607-610 — so an order-graded O4 extraction is W22-free by construction and A §4's Knob B is a provable no-op. Calibration applied: D §2's description of v10a.24c's code is itself accurate; D's error is attributing the quoted blind scalar to that path. Not previously recorded in the repo, which independently attributes the run to v10a.26.

---

### 5.11 `oneface-143-8960-already-a-corpus-certificate`

| | |
|---|---|
| **severity** | high |
| **class** | `overstated` |
| **lane** | `corpus-value-search` |
| **verifier confidence** | high |
| **where** | B §0, §2, §6 check 1-2; A §2 rows 1-2, §3; D executive verdict and §1 — vs corpus-import/programs/hodge_o4_adjudication/src/ENGINE_O4_hodge_rootonly_firewall_v1.py:43,218-229 |

**Claim as stated.** "The decisive new fact is that the two branches agree exactly at one face (143/8960)" (B §0); "The most useful new localization is exact: the one-face contribution agrees between the branches" (D, executive verdict); A §2 lists "one-face gap | T1 | −13/896 + 39/1280 = 143/8960" as this session's certified spine and A §3 as "this session's contribution".

**What is wrong (originating auditor).** 143/8960 is already a named, exactly-gated corpus constant, and it sits one line below the very line document B cites for its inputs. `ENGINE_O4_hodge_rootonly_firewall_v1.py` declares EXPECTED_VACUUM at :41, EXPECTED_AXIAL at :42 (both cited by B §2), and EXPECTED_GAP = (8/3, 1, 1/2, 7/32, 143/8960) at :43 — which B does not mention. `one_face_certificate()` at :218-229 recomputes vacuum and axial series in exact Fractions, forms gap = axial − vacuum, and raises GateFailure unless gap == EXPECTED_GAP. Two further corpus sites already assert the same vector as the size-one ROOTED coefficient row (i.e. the branch identification the documents claim as new): v10a.29b installs "the already-completed size-one rooted coefficient row through order four as a frozen comparator (8/3, 1, 1/2, 7/32, 143/8960)" as `V26_ONE_FACE_PREFIX_EXACT`, and the v10a.24c section-15 benchmark regression-tests the generic reduced-Haar one-face fit against `exact=_v23g_np.array([8/3,1.0,0.5,7/32,143/8960],float)` with a hard AssertionError. The agreement therefore holds at ALL orders 0-4 (8/3, 1, 1/2, 7/32=0.21875, 143/8960), not only at c4, and it is a pre-existing regression gate, not a new localization.

**Evidence (originating auditor).** corpus-import/programs/hodge_o4_adjudication/src/ENGINE_O4_hodge_rootonly_firewall_v1.py:43 `EXPECTED_GAP = (Q(8, 3), Q(1), Q(1, 2), Q(7, 32), Q(143, 8960))`; :218-229 `one_face_certificate()` with `if gap != EXPECTED_GAP: raise GateFailure`. corpus-import/programs/hodge_o4_adjudication/notebooks/NB_O4_hodge_v10a29b_m5_first_no_m4_rerun.ipynb:13 (prose), :66 `V26_ONE_FACE_PREFIX_EXACT = ("8/3","1","1/2","7/32","143/8960")`, :415 assert. NB_O4_hodge_v10a24c_section15_reduced_gpu_benchmark_fresh.ipynb (BENCHMARK 1, `[15A] ONE-FACE GENERIC REDUCED-HAAR BENCHMARK`). corpus-import/records/transcripts/Monday 531 PM.txt:9702 "[8/3, 1, 1/2, 7/32, 143/8960]". Blind row: 15 hour RUN.txt:10620 "c1=+1 c2=+0.5 c3=+0.21875 c4=+0.0159598214286" — matches all four printed entries. Note the corpus_index misses :43 because it writes `Q(143, 8960)`, not `Fraction(...)`.

**Verifier's corrected statement — authoritative.**

> OVERSTATED-NOVELTY (severity: medium, not high). The exact one-face agreement the artifacts present as new is pre-existing corpus material, at three sites the artifacts do not cite.
> 
> What the artifacts claim as new:
> - B §0:21-22 "The decisive new fact is that the two branches **agree exactly at one face** (`143/8960`)"
> - D:29 "The most useful new localization is exact: the one-face contribution agrees between the branches."
> - A:9-13 / A §3:80 "Localization (this session's contribution)", premise 1 = "the branches agree exactly at one face (§2)".
> 
> What the corpus already holds (all re-opened and re-run by me):
> 
> 1. /home/user/WORKHOUSE/corpus-import/programs/hodge_o4_adjudication/src/ENGINE_O4_hodge_rootonly_firewall_v1.py:43 `EXPECTED_GAP = (Q(8, 3), Q(1), Q(1, 2), Q(7, 32), Q(143, 8960))` — literally one line below the :41-42 that B §2:78 and A:165 cite for their inputs, and neither A nor B nor D mentions :43 or EXPECTED_GAP. :218-229 `one_face_certificate()` recomputes the vacuum and axial series in exact `fractions.Fraction` from SU(3) characters, forms `gap = axial - vacuum`, and raises `GateFailure` on any mismatch (:223, :225, :227). I copied the file to scratchpad and executed it: it returns vacuum=(0,0,-3/4,-9/32,-39/1280), axial=(8/3,1,-1/4,-1/16,-13/896), gap=(8/3,1,1/2,7/32,143/8960), `gap == EXPECTED_GAP` True. So B's certified-spine row 1 (`-13/896 + 39/1280 = 143/8960`) is a strictly weaker restatement of a presently-executable corpus certificate that derives all five entries.
> 
> 2. corpus-import/programs/hodge_o4_adjudication/notebooks/NB_O4_hodge_v10a29b_m5_first_no_m4_rerun.ipynb:17 (prose) "installs the already-completed **size-one rooted coefficient row** through order four as a frozen comparator", :20 `(8/3, 1, 1/2, 7/32, 143/8960)`, :66 `V26_ONE_FACE_PREFIX_EXACT`, cell-7 lines 119-129 writing that vector into `shape_cache[_one_face_key]` tagged "frozen completed v10a.26 size-one rooted row", guarded at 139-144 by `max error >= 3e-9 -> RuntimeError`, asserted at :415. This is the cross-branch identification itself — the *rooted* (blind-side) size-one row asserted equal to the exact analytic gap vector.
> 
> 3. NB_O4_hodge_v10a24c_section15_reduced_gpu_benchmark_fresh.ipynb, cell 1, `[15A] ONE-FACE GENERIC REDUCED-HAAR BENCHMARK` (cell-relative lines 7664-7678): comment at 7665 states "generic reduced engine, NOT the analytic character bypass"; 7669 `exact=_v23g_np.array([8/3,1.0,0.5,7/32,143/8960],float)`; 7674 raises `AssertionError('V23G one-face exact regression FAILED; two-face benchmark forbidden')` unless err[1]<2e-5, err[2]<3e-5, err[3]<8e-5, err[4]<V23G_ONEFACE_TOL (=3e-4, defined at 7296); the u=0 leg is gated separately at 7657 (`abs(z0-8/3)>2e-9 -> RuntimeError`). Also corpus-import/records/transcripts/Monday 531 PM.txt:9702 "Runs only the exact one-face Gelfand regression against [8/3, 1, 1/2, 7/32, 143/8960]."
> 
> Extent: the agreement is a 5-vector, not a single c4. Executed evidence covers orders 1-4: 15 hour RUN.txt:10620 prints the blind rooted size-1 row `c1=+1 c2=+0.5 c3=+0.21875 c4=+0.0159598214286`, and 1, 1/2, 7/32=0.21875, 143/8960=0.015959821428571427 match every printed digit. Order 0 (8/3) is not printed in that table; it comes from the comparator/gate sites in 2-3.
> 
> Three qualifications that trim the original finding:
> (a) A §2 does not assert novelty — its header is "The certified spine (what is machine-verified)" and its lead-in is "Every row is T1 (exact) or T2 (numerical)". Only B §0, D:29, and A §3's premise 1 carry the novelty claim.
> (b) The *inference* A §3 credits to the session — that the whole 10.293 gap therefore lives in size >= 2 — I could not find in the corpus: `grep -rn "size *[>≥] *2|size-2|multi-face|multiface" corpus-import/records/transcripts/*.txt` returns nothing. So the premise is pre-existing; the localization step is not shown to be. Calling the session's whole contribution pre-existing would itself be an overreach.
> (c) Sites 2 and 3 are written but UNEXECUTED in the corpus (both notebooks: every cell `execution_count: null`, zero outputs; no transcript contains `[15A]` or `V23G` output), so they are declared gates rather than recorded passes. Site 1 is the one that executes and passes today.
> 
> Mitigation (why the artifacts plausibly missed :43, and a real repo-side gap): `workhouse.corpus_index` cannot see this file at all. `PATTERNS` matches only bare `a/b`, `Fraction(a, b)`, and `\frac{}{}`; the engine writes `Q(143, 8960)` via the alias `Q = Fraction` at :37. I ran `ci._extract(path.read_text(), path)` over ENGINE_O4_hodge_rootonly_firewall_v1.py and it yields 0 rationals — the entire EXPECTED_VACUUM/AXIAL/GAP block is invisible to value-search, so `workhouse search 143/8960` cannot surface :43.
> 
> Recommended handling: do not land A §6 item 3's ledger one-liner in a form that credits the one-face agreement to this session. State it as "the F07-vs-blind split is localized to size >= 2, resting on the pre-existing one-face certificate ENGINE_O4_hodge_rootonly_firewall_v1.py:43,218-229". Note also that 143/8960 appears nowhere in the WORKHOUSE verification layer (grep across everything outside corpus-import/ returns zero hits), so promoting `one_face_certificate()` to a registered T1 invariant is a genuine, unclaimed T3->T1 move.

**Why it holds.** I re-opened every cited primary source rather than trusting the evidence line, and re-ran the arithmetic and the corpus certificate myself. ENGINE_O4_hodge_rootonly_firewall_v1.py:43 does declare EXPECTED_GAP = (8/3, 1, 1/2, 7/32, 143/8960), one line below the :41-42 that B §2:78 cites, and B/A/D never mention it; I copied the engine to scratchpad and executed one_face_certificate(), which recomputes both series in exact Fractions and returns exactly that gap vector. The cross-branch identification B calls "the decisive new fact" is stated verbatim in NB_O4_hodge_v10a29b:17,20,66 ("already-completed size-one rooted coefficient row") and hard-gated in NB_O4_hodge_v10a24c_section15 cell 1 lines 7669-7675 against a generic reduced-Haar engine the comment explicitly flags as "NOT the analytic character bypass". The blind row at 15 hour RUN.txt:10620 matches 1, 0.5, 0.21875, 0.0159598214286 to every printed digit (143/8960 = 0.015959821428571427). So the novelty claim in B §0 and D:29 does not survive. I trimmed three overreaches in the original finding: A §2 makes no novelty claim (its header is "what is machine-verified"); the size>=2 localization inference itself is absent from the corpus transcripts, so only its premise is pre-existing; and both notebook gates are unexecuted (execution_count null, no outputs, no transcript), making them declared gates rather than recorded passes. I also confirmed the corpus_index blind spot by running ci._extract on the file — it returns 0 rationals because PATTERNS does not match the Q(...) alias — which explains the miss and is itself a repo-side gap. Severity is medium rather than high: no mathematical statement in the artifacts is false; the harm is confined to novelty attribution if A §6 item 3 lands as written.

---

### 5.12 `premise-bit-exact-sum-is-false`

| | |
|---|---|
| **severity** | high |
| **class** | `other` |
| **lane** | `hamer-circularity` |
| **verifier confidence** | high |
| **where** | corpus-import/records/transcripts/15 hour RUN.txt:10620-10625 (printed rows), :10626 (TOTAL); src/workhouse/constants.py:239 |

**Claim as stated.** "the blind per-size table sums (in printed order) to -0.77514586301840004978, which equals 8*HAMER_A4_NUM = 8*(-0.0968932328773) to the last float bit" (orchestrator's seed fact for this lane)

**What is wrong (originating auditor).** Not true as stated. Summing ALL SIX printed c4 rows in printed order gives -0.7751458630184425 (hex bfe8cdfeb26967ae), which is 382 ulps from 8*a_4 = -0.7751458630184 (hex bfe8cdfeb2696630). The bit-exact identity appears only for the hand-selected 4-row subset {size 1, 2, 3, 6} — i.e. after dropping the two numerical-zero rows (size 4 = -1.3933298959e-14, size 5 = -2.85049761573e-14), which together are exactly -4.2438e-14. Dropping them is defensible (they are exact zeros polluted by float noise), but it is a choice, not what the transcript prints, and the coincidence must be priced with that choice made.

**Evidence (originating auditor).** six-row sum = -0.7751458630184425, hex bfe8cdfeb26967ae; 8*a_4 = -0.7751458630184, hex bfe8cdfeb2696630; ulps(six-row, 8a_4) = 382; ulps(six-row, oracle -0.7751458630189173) = 4277. Four-row sum {1,2,3,6} = -0.7751458630184, hex bfe8cdfeb2696630, == 8*a_4 bit-for-bit (0 ulps). size4+size5 = -4.2438275116e-14 accounts for the whole difference.

**Verifier's corrected statement — authoritative.**

> The seed premise is false as stated, and the underlying observation carries no evidential weight in ANY subset form.
> 
> (1) SIX-ROW SUM (what the transcript actually prints). /home/user/WORKHOUSE/corpus-import/records/transcripts/15 hour RUN.txt:10620-10625 prints six rows, all six carrying a numeric c4 — sizes 4 and 5 are printed as -1.3933298959e-14 and -2.85049761573e-14, NOT elided. Summed as floats in printed order: -0.7751458630184425 (hex bfe8cdfeb26967ae). 8*HAMER_A4_NUM (/home/user/WORKHOUSE/src/workhouse/constants.py:239, HAMER_A4_NUM = -0.0968932328773) = -0.7751458630184 (hex bfe8cdfeb2696630). Gap = -4.241051954068098e-14 = 382 ulps. NOT bit-exact. No permutation of the six rows reaches 8*a_4: all 720 orderings give one of {-0.7751458630184426, -0.7751458630184425, -0.7751458630184423}.
> 
> (2) THE MATCH IS THE 4-ROW SUBSET. Dropping sizes 4 and 5 and summing {1,2,3,6} in printed order gives -0.7751458630184, hex bfe8cdfeb2696630, identical to 8*a_4 to the bit (0 ulps). This is stronger than "bit-exact float": as exact rationals the four printed decimals sum to -968932328773/1250000000000, which IS 8 x the printed Hamer decimal exactly. size4+size5 = -4.24382751163e-14 exactly, accounting for the whole 6-row/4-row difference.
> 
> (3) THE SEED'S OWN NUMBERS BETRAY THE SUBSET. The seed's quoted value -0.77514586301840004978 is the leading decimal expansion of float bfe8cdfeb2696630, i.e. the 4-row sum, not the 6-row sum. And the seed's "5.173e-13 from M_GAMMA_4_NUM" is the 4-row-vs-oracle gap (5.172529071728604e-13, 4659 ulps); the 6-row-vs-oracle gap is 4.748423876321795e-13 (4277 ulps).
> 
> (4) STRENGTHENING — the coincidence sits inside the print-truncation noise floor, so it is not evidence either way. The rows are printed to 12 significant digits, so each carries up to ~5e-13 of print rounding. Concretely, size 6 = -0.208333333333 is the truncation of -5/24; its print error alone is +3.3333333333e-13, which is 64% of the entire 5.172529071728604e-13 Hamer-vs-oracle gap the sum is being used to adjudicate. Summing printed rows therefore cannot distinguish 8*a_4 from the oracle at all, and "lands bit-exactly on 8*a_4" is a rounding artifact, not a linked-cluster fact.
> 
> (5) COLLATERAL — the same defect infects a proposed invariant in the artifacts. Document A line 62 ("blind table closes | T2 | Sigma per-size c4 = oracle -0.7751458630189 (:10626)") and document B line 195 (proposed invariant #5 "blind_table_sums_to_oracle") both propose registering the row sum as a T2 check. The printed rows do not sum to the oracle at the printed precision: they sum to -0.7751458630184425, 4.748e-13 / 4277 ulps from M_GAMMA_4_NUM = -0.7751458630189173 (/home/user/WORKHOUSE/src/workhouse/constants.py:207). The transcript TOTAL at :10626 is computed from full-precision internals, not from the printed rows. Document B lines 57-64 reprints sizes 4 and 5 as "~ 0 (numerical zero)", silently making the substitution this finding identifies.
> 
> (6) NOT ALREADY RECORDED. The repo checks only 8*HAMER_A4_NUM against M_GAMMA_4_NUM (/home/user/WORKHOUSE/src/workhouse/invariants.py:390 and :1299, gap 5.17e-13 under HAMER_TOLERANCE). Nothing in the repo asserts anything about the per-size row sum, so this is new.

**Why it holds.** I opened both cited primary sources myself rather than trusting the evidence line. sed -n '10600,10640p' on "/home/user/WORKHOUSE/corpus-import/records/transcripts/15 hour RUN.txt" shows section [16] ROOTED INCIDENCE TRANSFORM with six printed rows at :10620-10625 and the TOTAL at :10626 — sizes 4 and 5 do carry printed numerical-zero c4 values, so "the table" unambiguously means six rows. sed -n '225,255p' on src/workhouse/constants.py confirms HAMER_A4_NUM = -0.0968932328773 at line 239. I recomputed independently in python3: the float sum in printed order over all six rows = -0.7751458630184425 (hex bfe8cdfeb26967ae) versus 8*a_4 = -0.7751458630184 (hex bfe8cdfeb2696630), 382 ulps by symmetric-ordinal count — the finding's headline numbers reproduce exactly.

I attacked the finding on three routes and all three failed. (a) Does the transcript actually elide sizes 4/5, making "the table" four rows and the finding a strawman? No — both rows are printed with explicit values. (b) Is the 382-ulp gap an artifact of the auditor's chosen summation order? No — I brute-forced all 720 orderings of the six rows and none equals 8*a_4. (c) Is this already known and recorded? No — invariants.py:390 and :1299 compare 8*a_4 to M_GAMMA_4_NUM only and say nothing about the row sum.

Two independent tells confirm the seed was computed on the 4-row subset while describing the whole table: the seed's own quoted decimal -0.77514586301840004978 is the expansion of the 4-row float, and the seed's 5.173e-13 oracle gap is the 4-row gap while the 6-row gap is 4.748e-13. With fractions.Fraction over the printed decimals the 4-row identity is exact as rationals, which is sharper than the finding's "bit-exact float" phrasing, so I upgraded that clause.

The one place I go beyond the finding is severity direction. The finding calls dropping the two zero rows "defensible"; I quantified the print granularity and found that size 6 alone — the 12-digit truncation of -5/24 — carries +3.333e-13 of print error against the 5.173e-13 gap being adjudicated, so neither the 4-row nor the 6-row agreement is evidence of anything. That also invalidates the T2 invariant documents A:62 and B:195 propose registering, which is why I rate this worth writing down rather than too weak to state.

---

### 5.13 `raw-folded-axial-is-stale-and-unchecked`

| | |
|---|---|
| **severity** | high |
| **class** | `repo-wrong-or-stale` |
| **lane** | `invariants-tests` |
| **verifier confidence** | high |
| **where** | repo src/workhouse/constants.py:427-435, tests/test_constants.py:68; artifact B §1 (correct), artifact A §1 (hides it) |

**Claim as stated.** B §1: "`ax_rest` (raw folded rest) | `−11.9485781794014` | `D_EXACT + FOLD`, pre-linked-vacuum" — B is closer to correct than the repo constant

**What is wrong (originating auditor).** src/workhouse/constants.py:428 records RAW_FOLDED_AXIAL_GAMMA_NUM = -11.9485781794007, which is 6.768e-13 away from the exact D_EXACT+FOLD. No invariant in any suite reads that constant — it appears only in the float-naming guard tests/test_constants.py:68 — so nothing in the 140 checks would ever catch the drift. The exact value is recoverable from two constants already in the registry: QUARANTINED_SCALAR + LINKED_VACUUM_4 = -86634244910174898583/7250590288602460800 = -11.948578179401377, an unchecked free T1 promotion. (Caveat: the repo float faithfully transcribes what RUN15 printed, and RUN15_APPLIED_SHIFT_NUM = 11.17343231638178 is consistent with it — M_GAMMA_4_NUM - (-11.9485781794007) = 11.173432316381783 — so the imprecision originates in the corpus's own printout, not in the repo transcription. That is exactly why an invariant is needed.)

**Evidence (originating auditor).** grep: RAW_FOLDED_AXIAL_GAMMA_NUM occurs only at src/workhouse/constants.py:428 and tests/test_constants.py:68 — zero uses in src/workhouse/invariants.py. Exact: Fraction(-160506019419340168451,14501180577204921600) + Fraction(-1474623,1675520) = -86634244910174898583/7250590288602460800, float = -11.948578179401377. Gap to repo value = 6.7679e-13 = 381 ulps by math.ulp (ulp 1.7764e-15); = 255 ulps under the 2^-52*|x| convention; = 510 ulps under the 2^-53*|x| convention the repo's own C20 check uses at invariants.py:408. B's printed -11.9485781794014 is 2.309e-14 = 13 ulps from the correctly rounded double; A's -11.9486 is 2.18e-5 away.

**Verifier's corrected statement — authoritative.**

> `RAW_FOLDED_AXIAL_GAMMA_NUM` is an unchecked T3 float that sits 381 ulps from an exact value already derivable from two rationals in the same file — a free T1 promotion the repo has the pattern for but never applied. The finding is NOT "repo-wrong-or-stale": the transcription is faithful and the imprecision originates upstream.
> 
> EXACT VALUE (recomputed with fractions.Fraction, verified twice):
>   src/workhouse/constants.py:427  QUARANTINED_SCALAR = -160506019419340168451/14501180577204921600
>   src/workhouse/constants.py:430  LINKED_VACUUM_4    = -1474623/1675520
>   sum = -86634244910174898583/7250590288602460800, nearest double -11.948578179401377
> The corpus states the defining relation itself: theory/superseded/MASTER_THEORY.md:416 — "the raw folded axial Gamma-block before linked vacuum subtraction was -11.9485781794007; the linked vacuum O(u^4) subtraction ... is -1474623/1675520", and artifact B:37 writes it as `M4_SHORTCUT = ax_rest - V_link = QUARANTINED_SCALAR`. So ax_rest = QUARANTINED_SCALAR + LINKED_VACUUM_4 exactly. Independently corroborated outside the repo by certificate E: /tmp/.../cert/AUDIT_REPORT.md:8-33 gives D_EXACT = -361008126292641364183/7250590288602460800, F = 5315003/140454, V = -1474623/1675520, and I confirmed D_EXACT + F - V == QUARANTINED_SCALAR exactly (Fraction equality, True).
> 
> THE GAP (src/workhouse/constants.py:428, RAW_FOLDED_AXIAL_GAMMA_NUM = -11.9485781794007):
>   exact gap  = 6.7740e-13   (exact-rational: ax_rest - Fraction(repo_float); the candidate's 6.768e-13 is the float-subtraction value and is wrong in the 3rd digit)
>   = 381 ulps by math.ulp (ulp = 1.7764e-15)
>   = 255 ulps under the 2^-52*|x| convention
>   = 511 ulps under the 2^-53*|x| convention the repo's own C20 check uses at src/workhouse/invariants.py:408 (candidate said 510; 510.65, rounds to 511)
> 
> NOTHING READS IT. Repo-wide grep (excluding .git) for RAW_FOLDED yields exactly three hits: src/workhouse/constants.py:428 (definition), tests/test_constants.py:68 (the float-naming allowlist only — it asserts the name ends in _NUM, never the value), and index/claims.jsonl:229 (generated catalogue: tier 3, "module-level, not in REGISTRY"). Zero occurrences in src/workhouse/invariants.py, which carries 140 `.check(` registrations. No suite would catch drift in this constant.
> 
> THE REPO ALREADY HAS THE RIGHT PATTERN AND DID NOT APPLY IT HERE. constants.py:211-215 records DELTA_GAMMA_NUM = 2.0827701250956417 alongside DELTA_GAMMA_AS_PRINTED_NUM = 2.0827701250956414, with a comment explaining the corpus printout is one ulp low, and invariants.py:327-334 asserts that one-ulp discrepancy as a certified check. RAW_FOLDED_AXIAL_GAMMA_NUM has no exact sibling, no `_AS_PRINTED_` marker, and no docstring comment of its own (line 428 sits under the comment belonging to QUARANTINED_SCALAR), so its name reads as the value rather than as a printout — while its error is 381 ulps, not 1.
> 
> ORIGIN OF THE IMPRECISION (upstream, not the repo). The candidate's caveat is right and I located the cause. corpus-import/records/transcripts/"15 hour RUN. results.txt" prints three independent float paths for the same scalar: :1353 rest_direct = -11.9485781794007 (381 ulps low-magnitude), :1371 scalar folded formula = -11.948578179400714 (373 ulps), :1372 matrix H4 Gamma = -11.948578179400696 (383 ulps). They agree with each other to ~2e-14 and all miss the exact by ~6.7e-13 because the run's float Haar sum is itself off: the same file prints gamma-sum = -49.7901704444838 (:1346) and D = -49.79017044448387 (:1369) against the certificate's exact D_EXACT = -49.79017044448461, i.e. 7.375e-13 high, which propagates straight into ax_rest = D + FOLD. So the repo transcribes RUN15 correctly; RUN15's own float pipeline is what is 7e-13 off. RUN15_APPLIED_SHIFT_NUM = 11.17343231638178 (constants.py:437) is internally consistent with the imprecise value, which is why no cross-check inside the repo trips.
> 
> ARTIFACTS: B:36 prints -11.9485781794014 — the correctly rounded 15-significant-figure decimal of the exact value, 2.248e-14 = 12.7 ulps from the nearest double, i.e. ~30x closer than the repo constant. B is right. A:38 prints -11.9486, 2.18e-5 away, which hides the question entirely.
> 
> PROVENANCE NOTE: the digits -11.9485781794007 appear in theory/ only in theory/superseded/MASTER_THEORY.md:416, a superseded document; the current theory/MASTER_THEORY_UNIFIED_2026-08-20_v4_3.md:1061 refers to "a raw folded rest value" without printing a number. Nothing in README.md, ledger/*.yaml, FRONTIER.md, CERTIFIED.md or invariants.py records this discrepancy — the only ledger mention of ax_rest is ledger/contradictions.yaml:59, which is the by-construction caveat about local_shift, a different point.

**Why it holds.** I reproduced every element from primary sources rather than the evidence line. (1) Read constants.py:427-437 and tests/test_constants.py:60-80 directly; confirmed line 428 is a bare float with no comment of its own and that the test is a naming allowlist, not a value check. (2) Repo-wide grep confirms only three occurrences and zero in invariants.py (140 checks). (3) Recomputed the exact sum QUARANTINED_SCALAR + LINKED_VACUUM_4 = -86634244910174898583/7250590288602460800 in Fraction and independently verified the certificate chain D_EXACT + F - V == QUARANTINED_SCALAR exactly from /tmp/.../cert/AUDIT_REPORT.md and rank3_order4_exact_haar_summary.json, so the identity does not rest on the orchestrator's say-so. (4) Corrected two numbers in the candidate: the exact gap is 6.7740e-13, not 6.768e-13 (that is float(exact)-repo, not the exact-rational difference), and the 2^-53 convention gives 511 ulps, not 510. (5) Corrected the kind: the repo faithfully transcribes theory/superseded/MASTER_THEORY.md:416, and I traced the imprecision to RUN15's own float Haar sum (D = -49.79017044448387 vs exact -49.79017044448461, 7.375e-13) at "15 hour RUN. results.txt":1346,1353,1369-1372, so this is a missing-invariant / free-T1-promotion finding, not repo error. (6) Searched README.md, all ledger/*.yaml, FRONTIER.md, CERTIFIED.md and invariants.py for any prior record of the discrepancy: none exists, so it is not already known. (7) The comparison to the repo's own DELTA_GAMMA_NUM / DELTA_GAMMA_AS_PRINTED_NUM treatment (constants.py:211-215, invariants.py:327-334) shows the repo checks a one-ulp printout discrepancy elsewhere while leaving a 381-ulp one unchecked here, which is what makes the finding worth stating rather than too weak.

---

### 5.14 `search-corpus-suppresses-occurrences`

| | |
|---|---|
| **severity** | high |
| **class** | `repo-wrong-or-stale` |
| **lane** | `invariants-tests` |
| **verifier confidence** | high |
| **where** | repo src/workhouse/search.py:219-225 vs :248-262; docstring at src/workhouse/search.py:162-169 |

**Claim as stated.** CLAUDE.md:108-112: "`workhouse search` is the front door to both… It matches by *value* rather than spelling"; src/workhouse/search.py:165-169: "a front-door 'no corpus occurrence' for a value sitting in six .md files is a confident false negative — the exact failure mode this repository's culture warns against"

**What is wrong (originating auditor).** `workhouse search --corpus <value>` prints exactly that confident false negative whenever the claim catalogue has no hit. format_results returns early inside `if not hits:` — before the block that renders `occurrences` — so the corpus scan runs, finds the value, and its result is discarded. The user sees 'no claim matches …  For the corpus itself, add --corpus, or grep it directly' even though --corpus was passed and the scan succeeded. Exit code is 0, which makes the failure silent. This hits precisely the values these five artifacts are about.

**Evidence (originating auditor).** src/workhouse/search.py:219-225 (`if not hits:` … `return "\n".join(out)`) precedes the occurrences block at src/workhouse/search.py:248-262. Demonstrated: `workhouse search --corpus -- "-327/83776"` prints 'no claim matches' and exits 0, while `corpus_occurrences("-327/83776")` returns total_occurrences = 61 across 5 files. Same for 143/8960 (6 occurrences), -54321/837760 (63), -5/7168 (2), -13/896 (79), -39/1280 (43), verified directly against workhouse.corpus_index.scan_cached().

**Verifier's corrected statement — authoritative.**

> REPO DEFECT, reproduced. `format_results` in /home/user/WORKHOUSE/src/workhouse/search.py returns early at :219-225 (`if not hits:` … `return "\n".join(out)`) before the corpus-occurrences renderer at :246-259, so when a query matches no claim and no symbol, a successful `--corpus` scan is computed and then discarded. Reproduced: `python3 -m workhouse.cli search --corpus -- "-327/83776"` prints only `no claim matches '-327/83776'.` followed by the boilerplate whose last line is "For the corpus itself, add --corpus, or grep it directly." — printed even though --corpus was passed and succeeded. Independently recounted via `workhouse.corpus_index.scan_cached()`: -327/83776 = 61 occurrences across 25 distinct files (the auditor's "5 files" is wrong; format_results would have shown 10, its `limit` default); -13/896 = 79/26; -54321/837760 = 63/23; -39/1280 = 43/26; 143/8960 = 6/3; -5/7168 = 2/2. All six have 0 claim hits and 0 symbol hits and so take the early return. Positive control: 109151/249696 has 8 claim hits and renders the "In the corpus" block normally (83 occurrences), confirming the fault is the empty-hits branch and not the scan. Decisive evidence this is a bug, not intent, is an inconsistency inside one function: src/workhouse/cli.py:160-163 sets `found_in_corpus = occurrences is not None and occurrences.total_occurrences > 0` and returns exit 0 on that basis, so the CLI records the value as found while the renderer it invoked at :161 suppresses it — output and exit code disagree. This contradicts the front-door role asserted at CLAUDE.md:108-112 and the stated design intent in the `corpus_occurrences` docstring at src/workhouse/search.py:163-166 ("a front-door 'no corpus occurrence' for a value sitting in six .md files is a confident false negative"). Two corrections to the finding as filed: (i) the program never prints the words "no corpus occurrence" — the message "no claim matches" is literally true, and the false negative is by omission plus the misleading closing advice, so "prints exactly that confident false negative" overstates it; (ii) exit 0 is not itself a defect, it is `found_in_corpus` behaving correctly — it is the symptom of the output/exit-code divergence. Not previously recorded: no FINDING check, no README or ledger note, and no test exercises the occurrences argument at all — tests/test_search.py:74 and :88 both call format_results with three arguments, and :88 is exactly the no-hits case. Undetected because the documented example README.md:87 (`workhouse search 5/48 --corpus`) has 18 claim hits and never reaches the branch. Fix is one line: move or duplicate the occurrences rendering above the :225 return. Scope: tool-usability defect in the search front door; it changes no corpus value, tier, or claim status, so "high" severity is defensible only on the front-door-trust argument, not on any effect on recorded results.

**Why it holds.** I opened src/workhouse/search.py at the cited lines myself and confirmed the early return at :219-225 precedes the occurrences block at :246-259; ran the CLI and saw the suppressed output with exit 0; recomputed occurrence counts directly from corpus_index.scan_cached() rather than trusting the evidence line (and found one of its numbers, "5 files", to be wrong — it is 25); established a positive control (109151/249696) proving the scan works and only the empty-hits path drops it; found the corroborating internal inconsistency at cli.py:160-163; and confirmed via grep of tests/ and the docs that nothing in the repo tests or records this. The finding's substance is correct; only two characterizations (the wording of the printed false negative, and the role of exit 0) needed tightening.

---

### 5.15 `sub-entry-of-c2-is-a-category-error`

| | |
|---|---|
| **severity** | high |
| **class** | `graph-conflict` |
| **lane** | `ledger-graph` |
| **verifier confidence** | medium |
| **where** | artifact A §3 line 78, B §7 line 220; repo ledger/contradictions.yaml:88-113, FRONTIER.md:58, AGENTS.md:186 |

**Claim as stated.** A §3: "This is a sub-entry of C2 / G3."  B §7: "the open item is the F07-vs-blind multi-face split (a sub-entry of C2/G3)"

**What is wrong (originating auditor).** C2 is not a container for a Gamma-point scalar dispute; by C2's own argument it structurally cannot be. C2 is exactly the off-axis coefficient C_shp, and its notes prove a Gamma-point scalar places NO constraint on Delta_C. Filing a Gamma-point branch conflict under C2 is orthogonal to C2's content and would falsify C2's title, FRONTIER §3, and AGENTS.md.

**Evidence (originating auditor).** ledger/contradictions.yaml:96-113 (C2 notes): "Since e_2 = O(|k|^4) and Q = O(|k|^2), Phi_C = O(|k|^2) and Phi_C(0) = 0. So Hamer's Gamma-point scalar pins Delta_Gamma and places NO constraint on Delta_C." C2's title (line 89) is "the one genuinely open item"; FRONTIER.md:58 repeats it; AGENTS.md:186 "one contradiction genuinely open: C2". The encoding check is src/workhouse/invariants.py:436-440 (Phi_C vanishes at Gamma along every direction). The disputed gap 10.293333600759848 is a pure k=0 quantity, so Phi_C(0)=0 makes it inert for Delta_C.

**Verifier's corrected statement — authoritative.**

> HOLDS IN NARROWED FORM (severity: medium, not high — the "C2" half is misfiled, the "G3" half is correct).
> 
> WHAT I REPRODUCED
> 
> 1. The artifacts' words. A §3 line 78 (`/root/.claude/uploads/384fab32-8991-52ce-b2bf-4999d379e3f5/52ebdfa7-RANK3_ORDER4_MASTER_RECORD.md:78`): "This is a sub-entry of C2 / G3." B §7 lines 219-221 (`.../6a2b59cb-F07_VS_BLIND_TWOFACE_ADJUDICATION.md:219-221`): "the open item is the F07-vs-blind multi-face split (a sub-entry of C2/G3)". B places this under the heading "## 7. Ledger status — flagged, not changed" (B:203), i.e. in a context where ledger IDs are the payload, not loose prose.
> 
> 2. The disputed pair is a Gamma-point rest scalar, by the artifacts' own framing. A's title line 1 is "Rank-3 / order-4 Γ-scalar: master record"; A §1 (lines 36-47) is "The three scalars (never conflate)": ax_rest -11.9486, M4_SHORTCUT = F07 branch = -11.0685, M4_ORACLE = blind = -0.7751, with "|M4_ORACLE − M4_SHORTCUT| = 10.293333600759848 — the real, open branch conflict." Recomputed exactly: float(Fraction(-160506019419340168451, 14501180577204921600)) = -11.068479463778765, minus -0.7751458630189173 = -10.293333600759848. Exact match. A grep of A and B for shape|shp|off-axis|dispersion|band returns ZERO hits — neither document raises any off-axis or k-dependent quantity at all.
> 
> 3. C2 is exactly and only the off-axis coefficient. `/home/user/WORKHOUSE/ledger/contradictions.yaml:63-89`: title (64) "Fourth-order off-axis coefficient C_shp — the one genuinely open item"; its two `sides` (67-74) are -211835444920651/4405310420659200 = -0.04808638318135875 and -0.020213328886166577, `delta: 0.027873054295192174` (all three verified exactly in Python). Its machine check is `src/workhouse/invariants.py:361-366`, which compares only `C_SHP_NEW_NUM - float(C_SHP_HISTORICAL)`. The F07/blind values -11.068479463778765 and -0.7751458630189173 appear nowhere in C2.
> 
> 4. The two disputed values are C1's quantities, not C2's. `contradictions.yaml:32-35` records m_Gamma^(4) = -0.7751458630189173; `contradictions.yaml:36-40` records the "quarantined shortcut" -160506019419340168451/14501180577204921600 = -11.068479463778765, `status: rejected-by-both`. Grep across the whole ledger shows the quarantined shortcut occurs at exactly one ledger line, 36 — inside C1, never under C2. In code it is `QUARANTINED_SCALAR` (`src/workhouse/constants.py:426-435`) and is registered "falsified"/"record-backed" (`constants.py:649-655`); its check is `invariants.py:397-400`.
> 
> 5. The structural reason the filing cannot work is machine-checked. C2's own notes (`contradictions.yaml:79-84`) state Phi_C(k) = 4*e_2(k)/Q(k) = O(|k|^2), Phi_C(0) = 0, "So Hamer's Gamma-point scalar pins Delta_Gamma and places NO constraint on Delta_C." That is a T1/T2 check, not just prose: `invariants.py:436-447`, "Phi_C vanishes at Gamma along every direction", whose detail line ends "A Gamma-point scalar therefore constrains Delta_Gamma but places no constraint whatsoever on Delta_C." Since the F07-vs-blind gap of 10.293333600759848 is entirely a k=0 quantity, adjudicating it cannot move Delta_C in either direction, so it cannot be a sub-entry of C2.
> 
> 6. The G3 half of "C2/G3" is CORRECT and must not be condemned with it. `ledger/gaps.yaml:40-70`: G3 `resolves: [C2, C3, C22]` (line 51), and its protocol explicitly includes "independent scalar ledger testing q_band^(4) - E_0^(4) =? m_Gamma^(4)" (line 68) and "both m_Gamma^(4) and C^(4) from the same run" (line 70). A Gamma-scalar branch conflict is squarely inside G3's scope.
> 
> CORRECT ROUTING: the F07-vs-blind split belongs to C1 (`contradictions.yaml:8-61`, status resolved, and note its own `by_construction_caveat` at 55-61) and C22 (`contradictions.yaml:272-277`, resolved), under G3. This matters beyond bookkeeping: B:213-219 uses the "sub-entry of C2/G3" label while simultaneously asserting that C1/C22 are not being reopened. Filing the dispute under C2 is precisely what lets that sentence stand; naming C1 would make visible that the document is proposing to reopen a resolved entry.
> 
> WHAT I REFUTE IN THE ORIGINAL FINDING
> 
> - "would falsify C2's title, FRONTIER §3, and AGENTS.md:186" — false. `FRONTIER.md:58` and `AGENTS.md:186` ("one contradiction genuinely open: C2") are statements about the COUNT of open contradictions. A sub-entry filed inside C2 leaves that count at one, so nothing there is falsified. The defect is a scope mismatch, not a falsification.
> - Severity "high" is overstated. The repo itself uses "C1/C2" as a coarse bucket in C3's resolution (`contradictions.yaml:96-98`: "The §5.2 values are sealed; everything else is C1/C2"), and C1, C2 and C3 all carry `section: "§5.5"` — so "C2/G3" is partly defensible as workstream shorthand (C2 blocks G3, `contradictions.yaml:89`; `FRONTIER.md:123`). Combined with the G3 half being right, this is a medium-severity mislabel: the fix is to write "C1/C22, under G3".

**Why it holds.** Independently reproduced from primary sources. C2 (ledger/contradictions.yaml:63-89) has exactly two sides, -0.04808638318135875 and -0.020213328886166577, delta 0.027873054295192174 (verified exactly), and its only machine check (invariants.py:361-366) touches C_SHP alone. The F07-vs-blind pair (-11.068479463778765 vs -0.7751458630189173, gap 10.293333600759848, recomputed exactly) are C1 quantities (contradictions.yaml:32-40); the quarantined shortcut occurs at exactly one ledger line, 36, inside C1. Both artifacts frame the dispute as a Gamma-scalar one (A's own title and §1) and mention no off-axis quantity at all (zero grep hits), while Phi_C(0)=0 — machine-checked at invariants.py:436-447 — makes a Gamma-point scalar structurally incapable of constraining Delta_C. So "sub-entry of C2" is a genuine misfiling. But two parts of the original finding fail: the G3 half of "C2/G3" is correct (gaps.yaml:51 resolves C2/C3/C22; protocol lines 68 and 70 name the Gamma-scalar ledger explicitly), and the claim that the mislabel "would falsify C2's title, FRONTIER §3, AGENTS.md:186" is wrong, since those lines count open contradictions and a sub-entry would not change that count. Confidence is medium rather than high because the number-level disjointness is certain but the "category error" reading competes with a defensible workstream-shorthand reading, which the repo's own bucket usage at contradictions.yaml:96-98 supports.

---

### 5.16 `blind-o4-is-not-a-fit`

| | |
|---|---|
| **severity** | high |
| **class** | `artifact-wrong` |
| **lane** | `localization-argument` |
| **verifier confidence** | high |
| **where** | A §3 line 91, §4 lines 96-113; B §5 lines 168-171; D §2 line 91. Repo: /home/user/WORKHOUSE/corpus-import/records/transcripts/15 hour RUN.txt:9143-9144,10613-10617,10620-10626; /home/user/WORKHOUSE/corpus-import/programs/hodge_o4_adjudication/notebooks/NB_O4_hodge_v10a26_factor52complete_exactsw_rootedoracle_a100.ipynb (concatenated source 7157-7178, 7228-7254, 7650, 7666, 7678) |

**Claim as stated.** A §3 line 91: "the blind branch admits W22 and extracts O4 by a finite-u degree-6 fit." A §4: "Knob B - blind two-face O4 recomputed W22-off (order-truncated)"; "The W22-mask knob is the discriminator between fit artifact and real physics." B §5.2 and D §2 line 91 the same, citing ENGINE...v10a24c...py:6928-6946.

**What is wrong (originating auditor).** The per-size table all three documents use (15 hour RUN.txt:10620-10626) was NOT produced by the fit and NOT by v10a24c. It was produced by the v10a.26 run, in which the production cluster coefficients come from an order-truncated canonical Hermitian Schrieffer-Wolff/BCH recursion and the 13-point degree-6 fit is explicitly retired to an audit-only role. Since the O(u^4) effective P-block of an order-truncated SW is a sum over closed 4-step layer walks, and the corpus's own gate proves no such walk contains W22, W22 cannot contaminate the c4 the documents are using. The documents' central proposed experiment (Knob B: recompute the blind O4 "W22-off, order-truncated") is therefore a null experiment on this data - the knob is already turned, and its answer is forced to zero by DATA_O4...:609-610. The "fit contamination vs real physics" discriminator that A §4 calls "a distinction none of the five documents could draw alone" is void.

**Evidence (originating auditor).** 15 hour RUN.txt:9143-9144 (run output): "production coefficients : canonical Hermitian SW/BCH through O(u^4)" / "retired fit (one-face audit only) : symmetric polynomial, umax= 0.055 deg= 6 N= 13"; :10617 (immediately above the table): "production coefficient method: canonical Hermitian SW/BCH; no polynomial fit/window"; :10613-10614 "[PASS] v10a.26 exact SW block diagonalization closes through O(u^4) :: max P-Q residual=5.551e-16". Source: NB_O4_hodge_v10a26_...ipynb redefines _v23c_fit_cluster to call _v26_sw_blocks(one,4)/_v26_sw_blocks(vac,4) and return 'fit_stability':0.0, 'method':'canonical Hermitian SW/BCH through O(u^4)' (concatenated-source lines 7238-7254); _v26_legacy_fit_models docstring "Audit only: reproduce the retired 13-point fit" (:7228-7235); SW recursion _v26_sw_blocks at :7157-7178, gated against an exact rational BCH oracle to <5e-12 at :7201-7203. The file the documents cite (v10a24c) contains no v10a.26 code (grep count 0) and does still use the fit at :7271,7279 - but it is not the engine that produced the cited transcript.

**Verifier's corrected statement — authoritative.**

> ARTIFACT-WRONG (documents A and B; document D partially). Documents A and B attribute the blind per-size cluster table to a finite-u degree-6 polynomial fit and (B) to engine v10a.24c. Both attributions are false for the numbers actually cited, and the experiment A builds on them is a null experiment.
> 
> 1. PROVENANCE OF THE CITED TABLE. A:168 and B:232 both name `corpus-import/records/transcripts/15 hour RUN.txt:10620-10626` as "blind per-size table"; A:103 compares Knob A against "blind `size 2 c4 = -0.403971702978` (`:10621`)"; B:159-161 cites the same value at `15 hour RUN.txt:10621`. That file is the **v10a.26** run: its header is `# HODGE v10a.26 - FACTOR-(5,2) COMPLETE + EXACT-SW ROOTED ORACLE` (line 3), and the file is source+output concatenated (the `print` for section [16] is at :7672, its output at :10619). The line immediately above the table, :10617, reads `production coefficient method: canonical Hermitian SW/BCH; no polynomial fit/window`; the run banner at :9143-9144 reads `production coefficients : canonical Hermitian SW/BCH through O(u^4)` / `retired fit (one-face audit only) : symmetric polynomial, umax= 0.055 deg= 6 N= 13`. The engine source in that same file confirms it: `_v23c_fit_cluster` at :7230-7246 calls `_v26_sw_blocks(one,4)`/`_v26_sw_blocks(vac,4)` (:7232), returns `'fit_stability':0.0` and `'method':'canonical Hermitian SW/BCH through O(u^4)'`, and the 13-point fit survives only as `_v26_legacy_fit_models` (:7220-7228), docstring "Audit only: reproduce the retired 13-point fit". The SW/BCH recursion is at :7149-7178 and is gated against an exact rational BCH oracle at :7180-7203 (`[PASS] ... :: 2.6645352591003757e-15`, :9148); block closure is gated at :10614 (`max P-Q residual=5.551e-16`). Verified independently in the notebook `corpus-import/programs/hodge_o4_adjudication/notebooks/NB_O4_hodge_v10a26_factor52complete_exactsw_rootedoracle_a100.ipynb` (concatenated code source: `_v26_sw_blocks` def at line 7147, audit-only docstring at 7219, `_v23c_fit_cluster` at 7228 — the finding's 7157/7228-7235 offsets are off by 2-10 lines, immaterial).
> 
> 2. v10a.24c NEVER PRODUCED THE TABLE. `ENGINE_O4_hodge_v10a24c_rootedfullt1_dualcoldoracle_a100.py` does use the degree-6 13-point fit (`_v23c_fit_cluster` at :6934-6946) on a dense W with no layer mask (:6894-6899) — B's and D's description of that *source* is accurate — and contains zero v10a.26 code (`grep -c 'v10a\.26\|_v26_'` = 0). But the v10a.24c production run itself died with `KeyboardInterrupt` inside section [15] (`# HODGE v10a.24c - production runti.txt`:8771 is the last section header, :9099 is the traceback); it emitted no `[16] ROOTED INCIDENCE TRANSFORM` block (grep count 0). The value -0.403971702978 occurs nowhere in the repository except `15 hour RUN.txt:10621` and its results twin `15 hour RUN. results.txt:2862`.
> 
> 3. KNOB B IS A NULL EXPERIMENT. Reproduced exactly, twice. (a) Closed layer walks: there are exactly 9 closed four-step Motzkin walks from P to P; none contains a (Q2,Q2) step; the unique five-step one that does is (P,Q1,Q2,Q2,Q1,P). This is already gated in-repo at `corpus-import/programs/hodge_o4_adjudication/src/DATA_O4_OrderSchedule_Occurrence_Preflight_CPU.py:606,609,610,611`. (b) Bridging that abstract gate to the actual production recursion (which the repo does not currently do): I transcribed `_v26_poly_mul`/`_v26_poly_comm`/`_v26_bch`/`_v26_sw_blocks` from `15 hour RUN.txt:7125-7178` into sympy exact rationals and ran 12 random Hermitian models with layer-tridiagonal V (P-Q2 block zero, all other blocks incl. W11 and W22 nonzero) over P/Q1/Q2 dimensions 1-3 each. In all 12, the effective P-blocks at orders 0,1,2,3,4 are **exactly equal as rational matrices** with W22 present and with W22 zeroed, and differ at order 5 in all 12. The premise (W[P,Q2]=0) holds in the v10a.26 basis by construction: `_v23c_build_basis` (`15 hour RUN.txt:7040-7118`) seeds P, sets Q1=W(P), Q2=W(Q1) with orthogonalisation, and the resonance guard forbids any non-P vector at E0, so W·P lies in span(P,Q1). Therefore recomputing the blind two-face O4 "W22-off, order-truncated" returns the *same* -0.403971702978 (identically in exact arithmetic; below float64 rounding, ~1e-16, in the run's implementation — far below the 4.7e-13 by which the printed table already disagrees with its own printed TOTAL). A's discriminator table at :106-113 therefore cannot select its first row for any reason relating to fit contamination, and the claim at :112-113 that "the W22-mask knob is the discriminator between fit artifact and real physics" is void.
> 
> 4. A:90-91 IS SEPARATELY REFUTED. "The corpus proves W22 is O4-null **only at one face**; multi-face W22-O4-safety is fit-argued, not exactly gated" is false on both halves: the walk gate at DATA_O4...:609-610 is a statement about the layer graph and carries no face count, and the multi-face coefficients were not fit at all.
> 
> 5. QUANTIFIED COUNTERFACTUAL. Even if the retired fit *had* been used, it cannot carry the divergence the documents are trying to explain. The v10a.26 run's own preflight compares exact SW against the retired 13-point fit on the same finite matrices: `[PASS] v10a.26 exact SW agrees with the retired symmetric fit on the one-face audit :: max coefficient difference=2.267e-07` (`15 hour RUN.txt:9190`). The branch gap under adjudication is |Delta| = 10.293333600759848 (`:10633`) — a factor of 4.5e7 larger. (Caveat: 2.267e-07 was measured at one face only; the fit was never run multi-face.)
> 
> SCOPE CORRECTION vs the candidate finding: document D is materially more careful than A and B and should not be graded identically. D:91 already states "exact perturbative power counting places the first `W22` contribution at fifth order, so the mere presence of the block does **not** prove that it changed the true fourth-order Taylor coefficient", and adds "The current canonical architecture avoids the ambiguity by making `W22` impossible at order four". D's premises about the v10a.24c source are correct; D's error is only the conclusion in the same sentence — "An exact order-truncated `W22`-off comparison is therefore required before the blind fourth-order scalar can be promoted" — where the "blind fourth-order scalar" is (D:27) the v10a.26 table it already exempted. None of the five documents mentions v10a.26 or names the production method (grep for `v10a.26|v10a26|SW/BCH|Schrieffer` across all five returns SW/BCH only as the *prescribed, not-yet-run* canonical branch: C:349, D:95, D:167).
> 
> NOT ALREADY RECORDED, but adjacent: `ledger/gaps.yaml:126-129` and `src/workhouse/invariants.py:664-679` carry "protocol item 10 (W22 order-schedule toggle) is hardcoded OPEN". That is a different engine lineage — `settlement/mce_adjudication_harness.py:43,335`, the sealed marked-cluster m4 certificate protocol — and must not be conflated with the v10a.26 cluster oracle when this is written into the ledger.

**Why it holds.** Every citation checked at source and every arithmetic claim reproduced independently. Verified verbatim: A:88-92 and A:96-113 (the fit attribution and the two-knob table), B:159-161 and B:167-170 (v10a.24c + degree-6 fit as the origin of the size-2 value), D:91. Verified from the transcript that `15 hour RUN.txt` is the v10a.26 run and that its section-[16] table is preceded at :10617 by "no polynomial fit/window", with the engine source at :7230-7246 calling `_v26_sw_blocks` and retiring the fit to audit-only. Verified that v10a.24c contains no v10a.26 code and that its own run died in section [15] without ever emitting section [16], and that -0.403971702978 appears nowhere else in the repo. Independently reproduced the 9 closed four-step Motzkin walks and their W22-freeness, and — the step the repo had not written down — transcribed the run's own SW/BCH recursion into exact sympy rationals and confirmed on 12 random layer-tridiagonal Hermitian models that orders 0-4 of the effective P-block are exactly W22-independent while order 5 is not. That makes Knob B informationless on this data and voids the "fit artifact vs real physics" discriminator. Two corrections to the candidate: document D is materially more careful than A and B and its premises are right (only its conclusion is wrong), and the finding's notebook line offsets are off by 2-10 lines. The existing ledger entry on a "W22 toggle OPEN" belongs to a different engine lineage and does not already record this.

---

### 5.17 `fold-never-decomposed`

| | |
|---|---|
| **severity** | high |
| **class** | `overstated` |
| **lane** | `localization-argument` |
| **verifier confidence** | high |
| **where** | A §2 line 57, §3 lines 80-86; B §0 lines 22-24, §2 lines 66-87, §5 lines 159-176; D §1 lines 45-63, §9 lines 213-227. Repo: /home/user/WORKHOUSE/corpus-import/programs/hodge_o4_adjudication/src/ENGINE_O4_hodge_v10a6_gamma_q1_zero_scalar_ledger.py:668-670,798,802; .../ENGINE_O4_hodge_v10a21r_adjudicator_only_same_kernel.py:122-127,331-339 |

**Claim as stated.** A §3: "the entire 10.293 gap lives in the multi-face (size >= 2) sector, because 1. the branches agree exactly at one face ... so the gap is neither anchoring nor one-face; it is purely multi-face accounting." B §2: "The F07 branch's one-face contribution is exactly D11 - e4_vac(1) = -13/896 + 39/1280 = 143/8960."

**What is wrong (originating auditor).** The F07 total is D_EXACT + FOLD - V_link. FOLD is not an opaque global scalar: it is the Rayleigh-Schrodinger renormalisation term FOLD_A = -2*C_A - E2_A*N_A + J_A (C_A = 0), a BILINEAR in two Gamma-point 13-face sums. A product of face-sums does not decompose into a sum over faces without a convention for cross terms, and the corpus's only such convention is a union convolution that puts a fold term on EVERY support, including the singleton. All three documents state the F07 one-face contribution as D11 - V1 with no fold term, and none of A/B/D ever gives FOLD a value, a face profile, or a place in the five-point specification of the proposed two-face test (A §4 knob A, B §5, D §9). Quantitatively the omitted object dwarfs the thing being localised: FOLD = +37.8416 = 3.68x the entire 10.293 gap, and its singleton part is 0, so 100% of it sits in the size>=2 sector the documents claim to have isolated. (The one-face conclusion itself survives - see confirmed_correct - but by an exact cancellation the documents neither state nor cite.)

**Evidence (originating auditor).** FOLD_A=-2*C_A-E2_A*N_A+J_A at v10a6:798; gate FOLD_A==Fraction(5315003,140454) at :802; E2_A=codd_R[SEED]+sum_inc*R1_off, N_A, J_A at :668-670 with sum_inc=-4 over 12 shared-edge neighbours (:665). Recomputed exactly: -E2_A*N_A+J_A = -(-5945/612)(511051/124848)+(-48945521/25468992) = 5315003/140454 = +37.84159226508323; D_EXACT+FOLD-V_link = -160506019419340168451/14501180577204921600 exactly. FOLD/|M4_ORACLE-M4_SHORTCUT| = 37.8416/10.2933 = 3.676. Face profile under the corpus's own union convolution, using the exactly-verified isolated one-face moments (e2=-1/4, N=1/16, J=-1/64): FOLD[size1] = 0 exactly; FOLD[size2] = -0.30692 - S; FOLD[size3] = +38.14851 + S, where S = sum_f E2[{R,f}]*N[{R,f}] is the only unresolved piece. With S=0, FOLD[size3]=+38.15; with the uniform-neighbour estimate S=-3.179, FOLD[size2]=+2.872 (7.1x the blind size-2 target -0.403971702978) and FOLD[size3]=+34.97 (196x the blind size-3 value -0.178800648136). Either way the fold's multi-face content is 3.4-3.7x the entire gap.

**Verifier's corrected statement — authoritative.**

> HOLDS, with three corrections and a downgrade of severity to medium-high (the localization conclusion survives; this is a derivation gap in a load-bearing step, not a refutation).
> 
> REPRODUCED FROM PRIMARY SOURCES:
> 
> (1) FOLD is a bilinear, not an opaque scalar. /home/user/WORKHOUSE/corpus-import/programs/hodge_o4_adjudication/src/ENGINE_O4_hodge_v10a6_gamma_q1_zero_scalar_ledger.py:798 `FOLD_A=-2*C_A-E2_A*N_A+J_A`, with C_A=Fraction(0) at :787 and E2_A/N_A/J_A at :668-670 (each = seed-face moment + sum_inc*off-diagonal, sum_inc=-4 over the 12 shared-edge neighbours, computed :659 and gated :660 — the finding cites :665, wrong by ~5 lines). Recomputed exactly: -(-5945/612)(511051/124848)+(-48945521/25468992) = 5315003/140454 = +37.84159226508323, matching the gate at :802. FOLD/|M4_ORACLE-M4_SHORTCUT| = 37.84159226508323/10.293333600759848 = 3.676320396561303.
> 
> (2) The corpus's only face-resolution convention for that bilinear is a set-union convolution: ENGINE_O4_hodge_v10a21r_adjudicator_only_same_kernel.py:122-127 (`_v21_union_convolution`, key = frozenset(SA)|frozenset(SB)), applied at :331-333 (`E2N_MIN=_v21_union_convolution(E2_MIN,N_MIN)`) and folded into EA_MIN at :335-340. Because {ROOT} u {ROOT} = {ROOT}, it does assign a fold term to the singleton support, exactly as the finding says. V_MIN likewise puts V1=-39/1280 on {ROOT} (:358, :361-363, since _V17_NEIGH includes self — ENGINE_O4_hodge_v10a7_marked_linked_scalar.py:5224,5448), and D_MIN[{ROOT}] is the injected analytic_11=-13/896 (:312-313, :296-297).
> 
> (3) A, B and D all compute the F07 one-face contribution as D11 - V1 with no fold term (A:57; B:66-71; D:45-52), and none of the three ever gives FOLD a value or a face profile. Only document C does (`FOLD_EXACT = 5315003 / 140454`, C:224). Nothing in the repo's verification layer records it either: repo-wide grep for `5315003`, `140454`, `143/8960` over src/, ledger/, docs/, theory/, adr/ returns zero hits, so this is not already-known-and-recorded.
> 
> (4) The omitted singleton fold really is exactly zero, and the finding is right that no document states or cites why. I derived it from the corpus's own gated isolated one-face model at DATA_O4_OrderSchedule_Occurrence_Preflight_CPU.py:317-338 (h0=(8/3,20/3,12,32/3), V at :321-326, gated "exact one-face O4 coefficient is -13/896" at :615). Its reduced-resolvent moments are e2 = -1/4, N = 1/16, J = -1/64, C = 0 exactly, so -2C - e2*N + J = 1/64 - 1/64 = 0 exactly. That is why -13/896 can serve simultaneously as the FULL one-face e4 (EXPECTED_AXIAL[4], ENGINE_O4_hodge_rootonly_firewall_v1.py:42) and as v10a21r's DIRECT D[{ROOT}] (:313) without contradiction — an identity the corpus relies on and no document names.
> 
> CORRECTION A — the finding overstates its own evidence. It calls e2=-1/4, N=1/16, J=-1/64 "exactly-verified isolated one-face moments". e2, and N via e3=-1/16 with N=-e3, are in EXPECTED_AXIAL at rootonly_firewall_v1.py:42, but J = -1/64 occurs NOWHERE in the repository (repo-wide grep for `-1/64` / `(-1,64)` across .py/.md/.txt/.json/.yaml: 0 hits). It is derivable — I derived it — but it was not verified when asserted.
> 
> CORRECTION B — "all three documents" is too broad. D is hedged: D:63 says the first disagreement must occur among size>=2 clusters "or in their P-return/fold/incidence accounting", and D:221 tells the reader to trace a size-2 difference through "direct Q2 return, P-return/fold, and vacuum terms". The unqualified claim is A:80-86 ("the entire 10.293 gap lives in the multi-face sector ... it is purely multi-face accounting") and B:22-24 ("so the entire gap lives in the multi-face (size >= 2) sector").
> 
> CORRECTION C — the size-2/size-3 profile is more model-dependent than stated. I reproduce the finding's numbers exactly (FOLD[2] = -0.30691941008108997 - S, FOLD[3] = +38.14851167516432 + S, summing with FOLD[1]=0 to 37.84159226508323), but only under an ADDITIONAL unstated assumption the finding does not flag: that all of J's non-singleton weight sits at size 2 (J_rest = J_A + 1/64 = -1.90614...). S is genuinely unresolved; the "uniform-neighbour estimate S=-3.179" and the derived "7.1x" and "196x" multipliers are unverifiable here and should be dropped.
> 
> STRONGEST DEFENSIBLE FORM: the F07 total is D_EXACT + FOLD - V_link, and its implementation produces no per-face decomposition at all; FOLD = 5315003/140454 = +37.84159226508323 is 3.676x the 10.293333600759848 branch gap and, under the corpus's only face convention (v10a21r:122-127,333), carries exactly 0 at the singleton and +37.84159226508323 at size >= 2. A:80-86 and B:22-24 therefore state a localization that is arithmetically correct but rests on an exact cancellation (-2C - e2*N + J = 1/64 - 1/64 = 0 in the one-face model at DATA_O4_OrderSchedule_Occurrence_Preflight_CPU.py:319-326) that no document states, cites, or checks. The sharp operational consequence is forward-looking: the five-point specification for a valid two-face F07 weight (A:98-104 knob A, B:159-176, D:213-227) fixes a vacuum convention but no fold convention, so any comparison of an F07 size-2 weight against blind `size 2 c4 = -0.403971702978` is undefined until the assignment of the +37.84159226508323 of size>=2 fold weight is fixed.

**Why it holds.** I re-derived every number independently in exact rationals rather than trusting the evidence line. Confirmed at the cited lines: FOLD_A is the bilinear -2*C_A-E2_A*N_A+J_A (v10a6:798, gate :802, inputs :668-670, C_A=0 :787), value 5315003/140454 = +37.84159226508323 = 3.6763x the 10.2933336 gap; the corpus's sole face convention is the set-union convolution (v10a21r:122-127 used at :333), which does place a term on the singleton {ROOT}; A:57, B:66-71 and D:45-52 all write the F07 one-face contribution as D11 - V1 with no fold term, and only document C (:224) ever gives FOLD a value. I also killed my own best counter-argument: B:126-128 ("its size-1 weight is 143/8960") is not a citation of a computed v10a21r size table — no transcript in corpus-import/records/transcripts contains that table — it is B re-deriving the same number from analytic_11 (:313) and V1 (:358), i.e. omitting the fold again. Finally I verified the cancellation the documents rely on: from the corpus's own gated one-face model (DATA_O4_OrderSchedule...:319-326, gate :615) I computed e2=-1/4, N=1/16, J=-1/64, C=0, giving fold[one face] = 0 exactly — so the conclusion survives but its justification is absent from the record, and J=-1/64 has zero occurrences repo-wide, contradicting the finding's "exactly-verified" wording. Nothing in ledger/, src/, docs/ or theory/ records 5315003/140454 or 143/8960, so this is not already known. I downgraded severity because the localization conclusion is correct and the missing step is a two-line exact computation, and corrected "all three documents" because D:63 and D:221 explicitly hedge on "P-return/fold".

---

### 5.18 `four-sevenths-of-the-set-missing`

| | |
|---|---|
| **severity** | high |
| **class** | `provenance-gap` |
| **lane** | `rules-compliance` |
| **verifier confidence** | high |
| **where** | artifact A §0 (lines 21-30), §2 (lines 63-70), §5 (lines 125-136), §6 (line 153); artifact D lines 17, 39, 45, 112, 125, 157, 176 |

**Claim as stated.** "**If you read one thing:** F (the coordination note) for the argument; the check for the machine-verified spine." and status line "Every *check* it points to is machine-verified"

**What is wrong (originating auditor).** Neither of the two things A tells the reader to read was delivered. Four of the seven items in A's own §0 document set are absent: DENOMINATOR_LOCALIZATION_INVESTIGATION (internal "A"), ORACLE_COUNTERFACTUAL_AUDIT (internal "C"), F07_VS_BLIND_COORDINATION_NOTE (internal "F"), and f07_twoface_adjudication_check.py. A §2 rows 7-8 rest on audit C §3/§4; §2's capstone on internal A §11.2; §5 bullets 1 and 3 on internal A §11.3/§12 and F C3; §6 item 5 on internal A §5.5/§6. Separately, document D line-cites WORKHOUSE_RANK3_ORDER4_EXACT_HAAR_FINAL_AUDIT_20260823.md at :9-40, :42-55, :57-91, :93-160, :124-126 and :158-160 — that file is not in the certificate zip, and the zip's AUDIT_REPORT.md is a different 70-line document, so every one of those line citations is uncheckable. In the other direction, the certificate zip that WAS delivered appears nowhere in A §0.

**Evidence (originating auditor).** Delivered set: A(master record), B(twoface), C(lineage trace), D(structural trace), E(zip). Zip contents listed in SHA256SUMS.txt: 20 files, none named *FINAL_AUDIT*; `grep -rl FINAL_AUDIT` over the extracted zip returns nothing; wc -l AUDIT_REPORT.md = 70 < the 160 lines D cites.

**Verifier's corrected statement — authoritative.**

> Provenance gap, reproduced in full: the delivered set does not contain most of the document set artifact A declares, including both items A tells the reader to read first.
> 
> (1) A §0 (lines 19-27) enumerates seven items. Only three were delivered: §0 "B" = `W2_R2_ORACLE_LINEAGE_TRACE` (upload C), §0 "D" = `F07_VS_BLIND_ORACLE_STRUCTURAL_TRACE` (upload D), §0 "E" = `F07_VS_BLIND_TWOFACE_ADJUDICATION` (upload B). Four are absent: `DENOMINATOR_LOCALIZATION_INVESTIGATION` (A:21, internal "A"), `ORACLE_COUNTERFACTUAL_AUDIT` (A:23, internal "C"), `F07_VS_BLIND_COORDINATION_NOTE` (A:26, internal "F"), and `f07_twoface_adjudication_check.py` (A:27). Verified: `find`/`grep -rl` for DENOMINATOR_LOCALIZATION, ORACLE_COUNTERFACTUAL, COORDINATION_NOTE, f07_twoface, adjudication_check over /home/user/WORKHOUSE (excluding .git) and over the extracted certificate zip return zero hits; the three prose names occur exactly once each in the entire delivered corpus, in A's own §0 table. A:29-30 ("If you read one thing: F (the coordination note) for the argument; the check for the machine-verified spine") names two of the four absentees, so neither recommended entry point exists. Note also that A itself (the master record) is an eighth document absent from its own §0 table.
> 
> (2) The undelivered documents are load-bearing for A's headline status line "Every *check* it points to is machine-verified" (A:4-5). A §2 rows 7-8 cite audit C: A:63 "F07 anchoring-invariant | T1 | ... (audit C §4)" and A:64 "F07 oracle-free | — | two independent scanners, zero leakage (B §2, C §3)" — 2 of the 8 spine rows. The §2 capstone rests on A:66 "Capstone (A §11.2)"; §5 bullet 1 on A:125 "Correction, document A §11.3/§12"; §5 bullet 3 on A:134 "Meta-pattern (F C3)"; §6 item 5 on A:153 "Optional Lean — ... (A §5.5, §6)". The 8-check screen A:163 says to run (`python3 f07_twoface_adjudication_check.py  # 8 checks, exit 0`) is not in the delivered set.
> 
> (3) Conversely, the one certificate bundle that WAS delivered (artifact E, `WORKHOUSE_RANK3_ORDER4_MODULAR_HAAR_CERTIFICATE_20260823.zip`, 20 files per SHA256SUMS.txt) is named nowhere in A: `grep -i "certificate|modular|zip"` over A returns only generic phrases at A:21, A:22 ("the exact-Haar package"), A:68 ("the certificate stack").
> 
> (4) Document D line-cites `work/rank3_order4_exact_haar_package_verify/WORKHOUSE_RANK3_ORDER4_EXACT_HAAR_FINAL_AUDIT_20260823.md` at five places — D:17 (`:9-40` and `:42-55,57-91,93-126`), D:39 (`:124-126`), D:125 (`:42-55,65-75`), D:157 (`:9-40,42-55,57-91,93-160`), D:176 (`:158-160`). That file is in an external directory not present here, and it is also absent from the delivered zip: `grep -rl FINAL_AUDIT` over the extracted zip returns nothing, and the zip's `AUDIT_REPORT.md` is 70 lines (byte-identical to `WORKHOUSE_RANK3_ORDER4_MODULAR_HAAR_INDEPENDENT_AUDIT_20260823.md`), so a `:158-160` anchor cannot resolve in it. Every FINAL_AUDIT line anchor in D is therefore unresolvable from the delivered set.
> 
> CORRECTIONS to the candidate as filed, both narrowing it:
>  (a) The "where" list mis-attributes D:45 and D:112 as FINAL_AUDIT cites. D:45 cites `work/fold_linked_exact/README.md:21-27`; D:112 cites `work/rank3_order4_cubic_ledger/exact_haar_sum.py:276-368`. Both are external and unverifiable here, but neither is a FINAL_AUDIT citation. The FINAL_AUDIT cites are at D:17, 39, 125, 157, 176 only.
>  (b) "every one of those line citations is uncheckable" is true of the line ANCHORS but overstates the evidential damage: the substance behind two of the five is corroborated by the delivered zip. D:17 cites `FINAL_AUDIT:9-40` for the exact result and components; the zip's `AUDIT_REPORT.md:31-33` states m_{4,rest} = D_EXACT + F - V_linked = -160506019419340168451/14501180577204921600 ~= -11.068479463778765, which I reproduced exactly (`float(Fraction(-160506019419340168451, 14501180577204921600))` == -11.068479463778765) and which matches the orchestrator's independently established value. D:176 cites `:158-160` for the package's scope boundary; that sentence appears in substance at `AUDIT_REPORT.md:59` ("This does not independently prove that the primitive generator is a complete physical perturbation expansion; that is a distinct provenance/modeling obligation"). D:39 (`:124-126`, one-face vacuum coefficient confirmed by the independent verifier) has no counterpart in the zip. So the defensible statement is that the FINAL_AUDIT document is missing and its line anchors cannot be resolved, not that the claims it anchors are unsupported.
> 
> SEVERITY: I would file this medium, not high. It is a delivery/provenance gap in an uploaded T3 bundle, not a defect in the repo or the corpus; nothing here is a wrong number, and the arithmetic spine rows A:57, A:60, A:61 have been independently confirmed exact by the orchestrator. What it does establish precisely is that A:4-5's "Every *check* it points to is machine-verified" is not auditable from the delivered set for A §2 rows 7-8 and the §2 capstone, and that A's declared reading order cannot be followed at all.

**Why it holds.** Reproduced independently from primary sources. Enumerated A §0 lines 19-27 myself and matched each item against the five delivered artifacts: three of seven present (§0 B, D, E), four absent. Confirmed absence with find and grep -rl over /home/user/WORKHOUSE (excluding .git) and over the extracted zip — zero hits for all four names; the three prose names appear exactly once each, in A's own §0. Confirmed A:29-30 points at two absentees. Confirmed the dependency lines A:63, 64, 66, 125, 134, 153 read as claimed. Confirmed the zip is unnamed in A by grep. Confirmed D's FINAL_AUDIT cites by grep -n (lines 17, 39, 125, 157, 176), confirmed the zip has 20 files in SHA256SUMS.txt with no FINAL_AUDIT, confirmed wc -l AUDIT_REPORT.md = 70 < the 160 lines D cites, and confirmed AUDIT_REPORT.md is byte-identical to the INDEPENDENT_AUDIT file. Two corrections found by reading rather than listing: D:45/D:112 are not FINAL_AUDIT cites, and the substance behind D:17 and D:176 is corroborated by the delivered zip (I recomputed the rational to float and matched AUDIT_REPORT.md:31-33 exactly), so "uncheckable" applies to the anchors, not the claims. Nothing in the repo records this already — grep for these names returns nothing anywhere in WORKHOUSE.

---

### 5.19 `gamma-scalar-mis-routed-to-C2`

| | |
|---|---|
| **severity** | high |
| **class** | `artifact-wrong` |
| **lane** | `rules-compliance` |
| **verifier confidence** | high |
| **where** | artifact A §3 (line 78) and §6 item 3 (lines 149-150); artifact D §8 (lines 193-199) |

**Claim as stated.** "This is a sub-entry of C2 / G3." and A §6 item 3: "`ledger/gaps.yaml` one-liner on G3: 'the F07-vs-blind split is localized to size ≥ 2; the decisive test is the exact W22-off two-face recomputation.'"

**What is wrong (originating auditor).** C2 is the off-axis coefficient C_shp. ADR 0002 proves a Γ-point scalar cannot be a sub-entry of it: Φ_C(0)=0, so "a Gamma-point scalar therefore fixes Delta_Gamma and constrains Delta_C not at all." G3's scope was then deliberately NARROWED to C_shp on exactly that ground. Landing item 3 on G3 re-widens a scope ADR 0002 narrowed, and routing the F07-vs-blind Γ-scalar to C2 recreates the category error ADR 0002 exists to prevent. Document D §8 gets this right and recommends "a separate open contradiction or sub-entry"; A overrides it without argument. Compliant form: open C23 (next free id) with both values recorded side by side and neither promoted, and add to G3 at most a pointer that protocol item 10 restricted to two faces is a cheap partial discharge. The W22 knob is also not new: it is already G3 protocol item 10, and the repo already holds a FINDING that the harness hardcodes it OPEN.

**Evidence (originating auditor).** docs/decisions/0002-anchoring-is-not-a-dispute.md §3 (Phi_C(0)=0 argument); ledger/gaps.yaml:44-50 ("Scope narrowed once C1 was dissolved... what G3 must now settle is the off-axis coefficient C_shp"); ledger/gaps.yaml:69 ("W_22 order-schedule toggle across all 33 rooted classes"); src/workhouse/invariants.py:666 ("FINDING: the harness can never report COMPLETE" — item 10 hardcoded OPEN); max contradiction id in ledger/contradictions.yaml is C22

**Verifier's corrected statement — authoritative.**

> Artifact A mis-routes a Γ-point rest-scalar branch conflict to contradiction C2, whose registered scope is the off-axis coefficient C_shp only. A:78 ("This is a sub-entry of C2 / G3"), repeated at B:220, files the F07-vs-blind dispute — `M4_SHORTCUT` = -160506019419340168451/14501180577204921600 = -11.068479463778765 vs `M4_ORACLE` = -0.7751458630189173, gap 10.293333600759848 (A:38-42, recomputed exactly) — under C2. But C2's subject is a different quantity: its two sides are -211835444920651/4405310420659200 = -0.04808638318135875 and -0.020213328886166577, delta 0.027873054295192174 (contradictions.yaml:63-73), i.e. a gap 369x smaller in a quantity that is not a Γ-point scalar. The binding is explicit in the symbol register: C2 carries exactly `C_shp` (symbols.yaml:72) and `Delta_C` (symbols.yaml:98), while `Delta_Gamma` — the family the -11.0685/-0.7751 gap belongs to — is bound to [C1, R6] (symbols.yaml:81). symbols.yaml:89-91 states the reason in the register itself: "Gamma-point data cannot constrain it, because the kernel it multiplies vanishes at Gamma." ADR 0002 §3 is the proof (`Phi_C(k) = 4*e_2(k)/Q(k)`, `Phi_C(0) = 0`, "A Gamma-point scalar therefore fixes `Delta_Gamma` and constrains `Delta_C` not at all"). The repo already registers the disputed value in the correct place: contradictions.yaml:36-40 holds it as a C1 quantity, "quarantined shortcut", status rejected-by-both, and constants.py:426-427 / :649-655 as QUARANTINED_SCALAR, status falsified. Secondary defect, weaker but real: A §6 item 3 (A:149-150) instructs a gaps.yaml one-liner on G3 reading "the F07-vs-blind split is localized to size >= 2; the decisive test is the exact W22-off two-face recomputation." G3's detail was deliberately narrowed on the same ADR 0002 ground — gaps.yaml:45-50, "Scope narrowed once C1 was dissolved... what G3 must now settle is the off-axis coefficient C_shp, since the Gamma-point scalar is externally validated against Hamer and Phi_C(0) = 0 makes Gamma-point data structurally incapable of constraining Delta_C", with ADR 0002's Consequences saying G3 "no longer needs to adjudicate a scalar." Landing that one-liner re-inserts a scalar adjudication into G3's settlement scope. (G3's protocol does retain scalar items 9 and 11, so the protocol is not scalar-free; the narrowing is about what G3 must settle, and that is what the one-liner would widen.) Third, the W22 axis is not new: it is G3 protocol item 10, "W_22 order-schedule toggle across all 33 rooted classes" (gaps.yaml:69), and invariants.py:665-676 already holds the FINDING "the harness can never report COMPLETE" because item 10 is hardcoded OPEN — though A's Knob B (a blind two-face O4 recomputation with W22 off, A:104) is a genuinely cheaper new instance on that known axis, not a restatement of it. Compliant landing: record the branch conflict where the repo already keeps the quantity — amend the C1 "quarantined shortcut" entry at contradictions.yaml:36-40, or open a new contradiction (next free id is C23; max is C22 at contradictions.yaml:272) — with both values side by side and neither promoted, and add to G3 at most a pointer that a two-face W22-off recomputation is a cheap partial exercise of protocol item 10. Two caveats on the finding as originally stated: artifact D never mentions C2 at all and files its recommendation under a "C1:" heading (D:180, D:193), so it did not reject a C2 routing so much as never propose one, and A does not engage D:193 rather than overriding it; and A:5-7 states the session was read-only, so this is a defective proposed write, not a defect already in the ledger.

**Why it holds.** Reproduced the core mis-routing from primary sources, three independent times over. (1) Artifact A is titled "Rank-3 / order-4 Γ-scalar: master record" (A:1) and A:38-42 names the two disputed quantities as `M4_SHORTCUT` = -11.068479463778765 and `M4_ORACLE` = -0.7751458630189173, gap 10.293333600759848 (I recomputed: Fraction(-160506019419340168451, 14501180577204921600) = -11.068479463778765; -11.068479463778765 - (-0.7751458630189173) = -10.293333600759848, matching A:42 exactly). A:78 then files that dispute as "a sub-entry of C2 / G3", and B:220 repeats it verbatim. (2) C2's scope is bound to C_shp in four independent repo locations, none of which admits a Γ-point scalar: contradictions.yaml:63-64 title "Fourth-order off-axis coefficient C_shp"; its two sides at :67-73 are -0.04808638318135875 and -0.020213328886166577 (delta 0.027873054295192174, which I recomputed exactly and which matches the printed value bit-for-bit); provenance.yaml:104,125 identify both sides as C_shp originating computations; and symbols.yaml binds exactly two symbols to C2 — `C_shp` (:72) and `Delta_C` (:98) — while `Delta_Gamma`, the scalar family the F07/blind gap belongs to, is bound to [C1, R6] at symbols.yaml:81, NOT C2. symbols.yaml:89-91 states the reason in the register itself: "Gamma-point data cannot constrain it, because the kernel it multiplies vanishes at Gamma." (3) ADR 0002 §3 is as cited: `Phi_C(k) = 4*e_2(k)/Q(k)`, `Phi_C(0) = 0`, "A Gamma-point scalar therefore fixes `Delta_Gamma` and constrains `Delta_C` not at all"; its Consequences section says "G3's scope narrows: it no longer needs to adjudicate a scalar." gaps.yaml:45-50 carries that narrowing verbatim. (4) The repo already has a home for -11.0685: contradictions.yaml:36-40 records it as a C1 quantity, "quarantined shortcut", status rejected-by-both, and constants.py:426-427 / :649-655 as QUARANTINED_SCALAR, status falsified. So the correct neighbourhood is C1/Delta_Gamma, not C2. (5) Corroborating checks on the finding's supporting claims: max contradiction id is C22 (contradictions.yaml:272), so C23 is next free; W22 is already G3 protocol item 10 at gaps.yaml:69; and invariants.py:665-676 holds the FINDING "the harness can never report COMPLETE" because item 10 is hardcoded OPEN. Adversarial checks that did NOT refute it: I checked whether "C2" in A might mean coordination-note connection C2 rather than the ledger contradiction — it cannot, because A:78 writes "C2 / G3" pairing it with an unambiguous ledger gap id, and A:156 writes "Nothing in 1-5 promotes either side of C2", which is non-negotiable #2's language. I also checked whether the multi-face (size >= 2) localization could be an off-axis statement — it is not; cluster support size is not momentum direction, and A:100-113 frames both knobs as scalar recomputations against blind `size 2 c4`. Three corrections to the finding's framing, none fatal: (a) artifact D never mentions C2 at all (zero grep hits) and files its recommendation under the heading "C1: split the resolved naming issue from the newly genuine branch conflict" (D:180), so "D gets this right" is true only in the weak sense that D avoids C2; "A overrides it without argument" overstates — A:24 lists D only for the structural fork and never engages D:193. (b) "Compliant form: open C23" is the auditor's prescription, not a verified defect; amending the existing C1 quantity at contradictions.yaml:36-40, as D:186-199 recommends, is at least as compliant and avoids a duplicate register entry. (c) "The W22 knob is not new" is fair as to the axis (gaps.yaml:69) but A's Knob B — blind two-face O4 recomputed W22-off (A:104) — is a narrower, cheaper instance than item 10's "toggle across all 33 rooted classes", so it is a new experiment on a known axis, not a restatement. Finally, note the defect is a proposed write, not an executed one: A:5-7 states the session was read-only and nothing landed.

---

### 5.20 `blind-table-sum-precision`

| | |
|---|---|
| **severity** | medium |
| **class** | `artifact-wrong` |
| **lane** | `arithmetic` |
| **verifier confidence** | medium |
| **where** | artifacts A §2 (row "blind table closes"), B §2, B §6 (row 5); /home/user/WORKHOUSE/corpus-import/records/transcripts/15 hour RUN.txt:10620-10626 |

**Claim as stated.** A §2 table row: "blind table closes | T2 | Σ per-size `c4` = oracle `−0.7751458630189` (`:10626`)"; B §2 code block prints the six size rows and then "TOTAL m4  = -0.7751458630189173     (= M4_ORACLE)" as if it were their sum

**What is wrong (originating auditor).** The printed rows do not sum to the printed total at the precision A asserts. All six printed rows sum to −0.7751458630184424382751163; with sizes 4 and 5 taken as zero (B §2's own rendering) they sum to exactly −0.7751458630184. The oracle total is −0.7751458630189173. Gap 4.7486e-13 (six rows) or 5.173e-13 (four rows) — 4277 / 4657 ulps, relative 6.13e-13. A quotes the equality to 13 significant digits (…0189) where the sum only reaches …0184; the two agree to 11 significant digits, not 13. The check named `blind_table_sums_to_oracle` (B §6 row 5) is honest as a T2 claim **only at tolerance ≥ 5.2e-13**, and the printed data support no tighter statement than the worst-case propagated envelope of ±1.55e-12 (rows quoted to 1e-12, one to 1e-13; RSS envelope 8.7e-13). Any tolerance tighter than ~5e-13 makes the check fail. B §6 states it with an ellipsis ("−0.775145863…"), which is honest; A §2's 13-digit form is not.

**Evidence (originating auditor).** Decimal sum of ['+0.0159598214286','-0.403971702978','-0.178800648136','-1.3933298959e-14','-2.85049761573e-14','-0.208333333333'] = -0.7751458630184424382751163. Four-row variant = -0.7751458630184 exactly. Oracle -0.7751458630189173. |Δ| = 4.748617248837E-13 / 5.173E-13. ulp(0.775) = 1.1102e-16 → 4277 / 4658 ulps. Worst-case envelope Σ(half-ulp of print) = 1.55000000000055E-12. Repo already records the same 5.2e-13 figure at ledger/contradictions.yaml:51-52 and docs/decisions/0002-anchoring-is-not-a-dispute.md:53.

**Verifier's corrected statement — authoritative.**

> SURVIVES, but downgraded to severity LOW and restated: this is a stated-tolerance defect in A, not a wrong number, and the numerical gap is fully explained by print truncation.
> 
> Reproduced from primary source. `/home/user/WORKHOUSE/corpus-import/records/transcripts/15 hour RUN.txt:10620-10625` prints the six per-size `c4` values at 12 significant figures; `:10626` prints `TOTAL m1/m2/m3/m4 = 1.0 0.03594771241824929 -0.4371355568371267 -0.7751458630189173`.
> 
> Exact arithmetic (Decimal prec 60 and IEEE double, agreeing):
> - six printed rows sum to -0.7751458630184424382751163 (left-to-right float: -0.7751458630184425); exact gap to the oracle = 4.748424e-13 = 4277 ulps of 0.775 (ulp = 1.1102230246251565e-16), relative 6.126e-13;
> - with sizes 4 and 5 taken as zero (artifact B's own rendering, B:60-61) the four rows sum to exactly -0.7751458630184; gap = 5.172529e-13 = 4659 ulps, relative 6.673e-13. (The finding's "4657 / 4658 ulps" is off by one to two; the correct counts are 4277 and 4659.)
> - half-ulp-of-print envelope Sigma = 1.55000000000055e-12, confirmed. Both observed gaps lie INSIDE that envelope, so the disagreement is entirely accounted for by 12-significant-figure decimal printing and is NOT evidence of any numerical defect in the run. It must not be recorded as a corpus discrepancy.
> 
> CORRECTION 1 to the finding: A:62's string `-0.7751458630189` is a correct 13-sf truncation of the oracle value printed at the line A cites (`:10626`). No number in A is wrong. The defect is narrower: A:62 presents the row `blind table closes | T2 | Sigma per-size c4 = oracle -0.7751458630189 (:10626)` with NO tolerance at 13-digit precision, while the only data it cites (`:10620-10625`) close on the total to 4.7e-13, i.e. 12 significant digits by truncation / 11 by rounding-to-N-sf. CLAUDE.md requires a T2 tolerance in the detail line. B:195 states the same check as `blind_table_sums_to_oracle | T2 | Sigma size-c4 = -0.775145863...`, whose ellipsis at 9 digits is honest — so A:62 is tighter than its own companion document's rendering of the same check.
> 
> CORRECTION 2 / new corroboration the original auditor missed: the four-row printed sum is BIT-IDENTICAL to 8 * HAMER_A4_NUM (`/home/user/WORKHOUSE/src/workhouse/constants.py:239`), both being the double -0.7751458630184 = -436368327480931/562949953421312. Hence the 5.1725e-13 half of this finding is numerically the same quantity the repo already records at `/home/user/WORKHOUSE/ledger/contradictions.yaml:51-52` ("8 * a_4 = -0.7751458630184, agreeing to 5.2e-13") and `/home/user/WORKHOUSE/docs/decisions/0002-anchoring-is-not-a-dispute.md:53`, and already machine-checks at `/home/user/WORKHOUSE/src/workhouse/invariants.py:388` against `HAMER_TOLERANCE = 5.3e-13` (`constants.py:264`). That half of the finding is therefore not new.
> 
> RESIDUAL ACTIONABLE CONTENT (why it still holds at all): A:147-149 proposes landing `f07_twoface_adjudication_check.py` as an `invariants.py` suite. If `blind_table_sums_to_oracle` is landed, its tolerance must be >= 5.2e-13 for the six-row form and >= 5.3e-13 to match the existing `HAMER_TOLERANCE` precedent; a tolerance inferred from A:62's 13-digit rendering (~1e-13) makes the check fail on the corpus's own printed data. The check script itself is external to this repo and was not in the uploaded certificate zip, so its actual tolerance is UNVERIFIABLE here.

**Why it holds.** I reopened `15 hour RUN.txt:10619-10626`, artifact A line 62 and artifact B lines 56-64 and 195 myself, and recomputed every number in exact Decimal and in IEEE double. The core arithmetic reproduces: the printed rows genuinely do not sum to the printed total (4.748424e-13 / 4277 ulps for six rows; 5.172529e-13 / 4659 ulps for the four-row rendering), and A:62 does quote the closure to 13 significant digits with no tolerance while B:195 quotes the identical check with a 9-digit ellipsis. That internal inconsistency is real and is not my reading imposed on the text. But two of the finding's framings do not survive: (i) A's 13-digit string is a correct transcription of the oracle at the line A cites, so nothing in A is numerically false — the defect is an unstated/over-tight T2 tolerance, not a wrong value; (ii) both gaps fall inside the +/-1.55e-12 half-ulp-of-print envelope the finding itself computes, so the gap is pure decimal-print truncation with no residual anomaly, and recording it as a corpus discrepancy would be wrong. I also found that the four-row sum is bit-identical to 8*HAMER_A4_NUM, making the 5.1725e-13 figure the same number the repo already records in contradictions.yaml, ADR 0002, and invariants.py:388 (HAMER_TOLERANCE = 5.3e-13) — so that half is already known. What is left is a low-severity presentation/tolerance guard that matters only because A proposes landing the check into invariants.py. Confidence medium rather than high because the arithmetic is certain but the charge rests on an interpretive reading of a one-line table cell, and the check script that would settle the tolerance is external and absent.

---

### 5.21 `cert-no-history-binding`

| | |
|---|---|
| **severity** | medium |
| **class** | `provenance-gap` |
| **lane** | `arithmetic` |
| **verifier confidence** | high |
| **where** | artifact C §3 (lines 118-137); /tmp/claude-0/-home-user-WORKHOUSE/384fab32-8991-52ce-b2bf-4999d379e3f5/scratchpad/cert/rank3_order4_exact_haar_summary.json, cert/SHA256SUMS.txt |

**Claim as stated.** C §3: "The exact-Haar summary binds the same history hash and the contractor hash in `work/rank3_order4_exact_haar_run/rank3_order4_exact_haar_summary.json:1`" plus a nine-row hash-chain table

**What is wrong (originating auditor).** The summary actually shipped in artifact E binds no such thing. Its complete key set is D11, D_EXACT, D_EXACT_decimal, D_EXACT_QBOUND_numerator, D_EXACT_denominator_divides_QBOUND, D_EXACT_integer_over_QBOUND_equality, QBOUND, crt_prime_count_histogram, elapsed_seconds, fully_unordered_nonzero_topologies, haar_ledger(+sha256), historical_orientation_sensitive_topologies, local_q_pattern, local_triangle_bound, peak_modular_factor_elements, schema, source_schema, source_topology_ledger(+sha256), weighted_haar_sum, zero_haar_topologies. There is no history hash, no generator hash, no freeze hash, no contractor hash. Its sha256 is 2b845725…, not the d3d2cb89… that C's table names as "final exact summary", and its source_topology_ledger_sha256 is 5337734a…, not the 48abeca4… C names as "exact topology ledger, gzip" — so the shipped artifact is a different (modular) run from the one C tabulates. Consequence: within artifact E the `weight` column of the 69,800-row ledger is an *unexplained input*. I replayed the arithmetic exactly and it is flawless, but nothing in E ties those weights to any frozen W2/R2 history. C's own verdict ("Exactness of D relative to the frozen W2/R2 construction: established") is therefore not exhibited by the certificate that accompanies it.

**Evidence (originating auditor).** cert/rank3_order4_exact_haar_summary.json key list (above); sha256(cert/rank3_order4_exact_haar_summary.json) = 2b845725b88120f0dc84f91d1ca6aa2f77e82a857098f0d9d7ea0bd4d2f801c6 per cert/SHA256SUMS.txt, vs C §3 row "final exact summary d3d2cb899966eef88e87f8bdc5216772a26a9620d6d77fce0b6341b67c87d9c7"; source_topology_ledger_sha256 = 5337734a57bd2e1fe690c636f19bc0f65c48bac86cc029a7e4dfe87251e8ff59 (verified against the actual file) vs C §3 row "exact topology ledger, gzip 48abeca47d51993b05a9b297b20656af3dfed3aaf4d857eac1f466d073c2a662".

**Verifier's corrected statement — authoritative.**

> PROVENANCE GAP (medium): artifact C's hash chain is not exhibited by the certificate E that accompanies it.
> 
> C:136-137 asserts "The exact-Haar summary binds the same history hash and the contractor hash in work/rank3_order4_exact_haar_run/rank3_order4_exact_haar_summary.json:1". That path is EXTERNAL to this repo and unverifiable here; the finding is not that C is false, but that the summary actually shipped in E binds no such thing.
> 
> Reproduced from primary sources:
> (1) Shipped summary key set (I enumerated it, 22 keys): D11, D_EXACT, D_EXACT_decimal, D_EXACT_QBOUND_numerator, D_EXACT_denominator_divides_QBOUND, D_EXACT_integer_over_QBOUND_equality, QBOUND, crt_prime_count_histogram, elapsed_seconds, fully_unordered_nonzero_topologies, haar_ledger, haar_ledger_sha256, historical_orientation_sensitive_topologies, local_q_pattern, local_triangle_bound, peak_modular_factor_elements, schema, source_schema, source_topology_ledger, source_topology_ledger_sha256, weighted_haar_sum, zero_haar_topologies. No history hash, no generator hash, no freeze hash, no contractor hash.
> (2) sha256(cert/rank3_order4_exact_haar_summary.json) = 2b845725b88120f0dc84f91d1ca6aa2f77e82a857098f0d9d7ea0bd4d2f801c6 (recomputed; matches cert/SHA256SUMS.txt:14), NOT the d3d2cb899966eef88e87f8bdc5216772a26a9620d6d77fce0b6341b67c87d9c7 that C:131 names "final exact summary".
> (3) sha256(cert/root_exact_pair_topologies.pkl.gz) = 5337734a57bd2e1fe690c636f19bc0f65c48bac86cc029a7e4dfe87251e8ff59 (recomputed; equals both SHA256SUMS.txt and the summary's source_topology_ledger_sha256), NOT the 48abeca47d51993b05a9b297b20656af3dfed3aaf4d857eac1f466d073c2a662 of C:129. I also gunzipped it: uncompressed sha256 = 9593bf47afe1253bbd18276e968f8d8b71067f6269f6c5ff2ce57b6f00e38b95, NOT C:130's a7f13ca19eb675ec4340f1664ec04a49979a5cb9e8e95dbb59272b69fa2bb2dd — so the mismatch is not a gzip-header/mtime artifact.
> (4) STRONGER than the original evidence line: I grepped the entire cert tree for all NINE hashes in C:122-131 (3685369c, 2eda6c89, a72a2c41, e68d5158, 543869b1, f944bfef, 48abeca4, a7f13ca1, d3d2cb89). Zero occurrences of any of them; grep for 'freeze', 'history_sha', 'contractor_sha', 'W2', 'R2' across cert *.json/*.md also returns nothing.
> (5) The shipped run is the modular one: cert/rank3_order4_exact_haar_{summary,validation}.json are byte-identical (md5 8d706670…, b85a2c07…) to their copies under cert/modular_haar_run/, and the summary carries crt_prime_count_histogram and elapsed_seconds 264.954.
> 
> CORRECTION to the original finding's wording: the ledger's `weight` column is NOT an "unexplained input". modular_haar_contractor.py:458 reads weight from payload["pair_weights"] of root_exact_pair_topologies.pkl.gz, and :454/:523 pin that file's sha256 — which I verified matches the shipped bytes. The weights are digest-pinned and internally replayable. The gap is one level upstream: the pickle's own top-level keys are only schema / counts / pair_weights (no provenance hashes), and its producer `ledger_generator` — imported at modular_haar_contractor.py:32 "required only for frozen pickle identity" — is not shipped in E. So the correct statement is that the weights are an UNATTRIBUTED input: pinned by digest, but with no shipped producer and no binding to any frozen W2/R2 history.
> 
> Consequence, as narrowly as the evidence supports: C:327-328's verdict "Exactness of D relative to the frozen W2/R2 construction: established by the package's exact arithmetic and immutable ledgers" is not exhibited by E. E's own INDEPENDENT_REFEREE_REPORT.md lists only two artifact hashes (ledger 1b9ed180…, source topology ledger 5337734a…) and asserts it "certifies the arithmetic over the frozen generator lineage" without exhibiting that lineage. The arithmetic within E is intact: I independently confirmed D11 = -13/896 exactly and D11 + weighted_haar_sum/2 == D_EXACT = -361008126292641364183/7250590288602460800 exactly in Fraction, over a 69,800-row ledger (matching validation.json records=69800).
> 
> Not already recorded in the repo: grep of /home/user/WORKHOUSE for d3d2cb89, 5337734a, 48abeca4, 2b845725, exact_haar_summary, modular_haar_contractor, rank3_order4_exact_haar returns no hits.
> 
> Where: C lines 118-137 (table 120-131, binding sentence 136-137) and 327-328; /tmp/claude-0/-home-user-WORKHOUSE/384fab32-8991-52ce-b2bf-4999d379e3f5/scratchpad/cert/rank3_order4_exact_haar_summary.json; cert/SHA256SUMS.txt:14; cert/modular_haar_contractor.py:32,454,458,523; cert/INDEPENDENT_REFEREE_REPORT.md (Artifacts section).

**Why it holds.** I re-opened every cited file myself rather than trusting the evidence line. C:118-137 and C:327-328 read exactly as quoted. I enumerated the shipped summary's keys with json in python3: 22 keys, none of them a history, generator, freeze, or contractor hash. I recomputed sha256 of the shipped summary (2b845725…) and of root_exact_pair_topologies.pkl.gz (5337734a…) and both differ from C's table rows d3d2cb89… and 48abeca4…. I tested and eliminated the most likely refutation — that a gzip-mtime difference explains the topology-ledger mismatch — by decompressing the pickle: its uncompressed sha256 9593bf47… also fails to match C's "canonical uncompressed" a7f13ca1…. I then went beyond the original evidence and grepped all nine of C's chain hashes across the whole cert tree, finding zero occurrences, which makes the gap unambiguous rather than a single-file mismatch. I confirmed the shipped files are byte-identical to those in cert/modular_haar_run/ (md5), so the shipped run really is the modular one. I checked the repo and found nothing recording this. The finding survives, but one clause of it is wrong and I corrected it: the `weight` column is not unexplained — modular_haar_contractor.py:458 sources it from a pickle whose sha256 the summary pins and whose bytes I verified, so the accurate charge is that the weights are unattributed (no shipped producer, no W2/R2 binding), not unexplained. I also verified the arithmetic is clean (D11 + W/2 == D_EXACT exactly in Fraction), so this is purely a provenance gap. Finally, the claim is correctly scoped: C's binding sentence points at an external path that is unverifiable in this repo, so this finding must be stated as "E does not exhibit C's chain", never as "C is false".

---

### 5.22 `oneface-agree-exactly`

| | |
|---|---|
| **severity** | medium |
| **class** | `overstated` |
| **lane** | `arithmetic` |
| **verifier confidence** | high |
| **where** | artifacts B §0, A §3 (point 1), D §1; /home/user/WORKHOUSE/corpus-import/records/transcripts/15 hour RUN.txt:10620 |

**Claim as stated.** B §0: "the two branches **agree exactly at one face** (`143/8960`)"; A §3: "the branches agree exactly at one face"; D §1 heading: "The one-face sector agrees exactly"

**What is wrong (originating auditor).** Only one side is exact. The F07 side is the exact rational 143/8960 (T1). The blind side exists only as a 12-significant-digit float print, `c4=+0.0159598214286`. The strongest supportable statement is agreement to 2.86e-14 absolute / 1.79e-12 relative — a T2 bound set by the print precision, not an exact identity. B §2 itself words it correctly ("equals the blind `size 1 c4` to full printed precision") and A §2's table row correctly labels it T2, so the three "exactly" sentences contradict the documents' own careful rows. The localization conclusion is unaffected (2.9e-14 vs a 10.29 gap), but the word "exactly" is the load-bearing one in A §3's three-step argument.

**Evidence (originating auditor).** 143/8960 = 0.0159598214285714285714…; printed blind value 0.0159598214286; |Δ| = 2.857089564933801e-14, relative 1.790e-12. Blind value known only to ±5e-14 from its own printed precision.

**Verifier's corrected statement — authoritative.**

> OVERSTATED (tier inflation), confirmed by direct inspection of the blind engine's source, not just its print.
> 
> What is exact (T1, and doubly so): the one-face gap coefficient is the rational 143/8960 = -13/896 + 39/1280 (143 = 11*13, 8960 = 2^8*5*7). Verified two independent ways in this repo:
>  - the F07-side inputs -13/896 and -39/1280, gated at /home/user/WORKHOUSE/corpus-import/programs/hodge_o4_adjudication/src/DATA_O4_OrderSchedule_Occurrence_Preflight_CPU.py:615 and .../ENGINE_O4_hodge_v10a21r_adjudicator_only_same_kernel.py:313,358;
>  - a cold, all-`fractions.Fraction` SU(3) character-basis Rayleigh-Schrodinger recomputation in .../ENGINE_O4_hodge_rootonly_firewall_v1.py:218-229, gating EXPECTED_GAP = (8/3, 1, 1/2, 7/32, 143/8960) at :43,:227.
> 
> What is NOT exact: the blind side. The blind per-size table is accumulated in a float64 numpy array — `totals=np.zeros(5,float); bysize=_v23c_dd(lambda: np.zeros(5,float))` at .../ENGINE_O4_hodge_v10a24c_rootedfullt1_dualcoldoracle_a100.py:7284 — and printed at 12 significant digits by `f'  size {k}: ... c4={x[4]:+.12g}'` at :7291. 8960 = 2^8*5*7 is not a dyadic denominator, so 143/8960 is not even representable in binary64; a float64 result cannot equal it exactly. No exact gate on the blind size-1 exists anywhere in v10a24c (grep for `Fraction(-13,896)` / `143, 8960` over the whole hodge_o4_adjudication/src tree returns only the F07-side and firewall files, never v10a24c); the nearest gates, :7294-7296, use tolerances 2e-5 / 2e-4 / 8e-4. And the cold firewall is explicitly decoupled from the blind runtime by design — its docstring, ENGINE_O4_hodge_rootonly_firewall_v1.py:4-6, states it "intentionally does *not* import or patch the historical v10a23/v10a25 runtime" — so it cannot stand in as the blind branch's own one-face output.
> 
> Quantified agreement. Printed blind value, /home/user/WORKHOUSE/corpus-import/records/transcripts/15 hour RUN.txt:10620: `size 1: c1=+1 c2=+0.5 c3=+0.21875 c4=+0.0159598214286`. 143/8960 = 0.0159598214285714285714...; float(143/8960) = 0.015959821428571427, and `'%.12g' % float(143/8960)` reproduces the transcript string `0.0159598214286` exactly — i.e. the print is *consistent with* exact agreement but carries no information below 1e-13. |Delta| = 2.857e-14 absolute (exact Fraction difference 288213/10088063165309911040 = 2.856970612466877e-14; naive float subtraction 2.857089564933801e-14 = 8235 ulps at this magnitude), relative 1.7901e-12. Print half-granularity is 5e-14.
> 
> The binding bound is tighter than print precision, and comes from the same table: the rows that must vanish identically print as c2 = -5.58442181386e-14 (size 3), +2.0872192863e-14 (size 4), -1.80966353014e-14 (size 5), and c4 = -1.3933298959e-14, -2.85049761573e-14 (`15 hour RUN.txt:10622-10625`). The engine's demonstrated numerical noise floor is therefore 5.58e-14 — 1.95x the 2.857e-14 print gap. So the honest statement is agreement at |Delta| <~ 1e-13, a T2 bound set by the blind engine's float noise, not an exact identity.
> 
> The three overstating sentences: B §0 line 22 ("the two branches **agree exactly at one face** (`143/8960`)"), B §2 heading line 51 ("Exact one-face agreement"), A §3 line 82 ("the branches agree exactly at one face"), D §1 heading line 31 ("The one-face sector agrees exactly"), and — strongest, and missed by the original finding — D §9 line 215 ("Start with two-face rooted clusters because the one-face sector is already proven equal"). "Proven equal" is a T1/T0 word applied to a 12-digit float print.
> 
> The documents' own careful rows contradict their prose: B §2 line 73 words it correctly ("equals the blind `size 1 c4` to full printed precision"); B §6 line 192 labels check 2 T2; A §2 line 58 labels the same row T2. So this is an internal inconsistency, not a dispute with the repo.
> 
> Not already recorded: grep over /home/user/WORKHOUSE/src/workhouse/ and /home/user/WORKHOUSE/ledger/ finds no occurrence of 8960 or 143/8960 — the verification layer has no entry for this at all.
> 
> Independence caveat: the second occurrence of the table, /home/user/WORKHOUSE/corpus-import/records/transcripts/15 hour RUN. results.txt:2861, is the same run (identical surrounding lines, including `elapsed=61095.0s`), so it is one observation, not two (AGENTS.md, "repetition is not independence").
> 
> Materiality: the localization conclusion is untouched — 2.9e-14 against a 10.293333600759848 branch gap is 12 orders of margin. But A §6 and B §7 propose landing this material as an `invariants.py` suite and a `ledger/gaps.yaml` line, and "the one-face sector is already proven equal" entering the ledger would be a silent T2->T1 promotion of exactly the kind AGENTS.md forbids ("Never move a result up a ladder silently"; CLAUDE.md non-negotiable #5). Recommended wording: "the branches agree at one face to 2.86e-14 absolute / 1.79e-12 relative, within the blind engine's own ~5.6e-14 float noise floor (T2); the F07-side value 143/8960 is exact (T1)."

**Why it holds.** I reproduced the finding from primary sources and strengthened it. The decisive new evidence, which the original finding did not have, is in the blind engine's source rather than its output: ENGINE_O4_hodge_v10a24c_...py:7284 accumulates the per-size table in np.zeros(5,float) and :7291 prints it with :+.12g, and no exact gate on the blind size-1 exists in that engine (its neighbouring gates at :7294-7296 use 2e-5/2e-4/8e-4 tolerances). Since 8960 = 2^8*5*7 is non-dyadic, a float64 value cannot equal 143/8960 exactly, so "agree exactly" is not merely unverified but unattainable on the blind side as computed. I checked and rejected the strongest counterargument: the corpus does contain an exact one-face gap vector, EXPECTED_GAP = (8/3,1,1/2,7/32,143/8960) at ENGINE_O4_hodge_rootonly_firewall_v1.py:43, gated at :227 by an all-Fraction RS series at :218-229 — but that file's docstring (:4-6) says it "intentionally does *not* import or patch the historical v10a23/v10a25 runtime", so it is a third independent exact computation, not the blind branch's output, and D §2 line 79 itself says the blind branch recomputes each cluster coefficient by a different route. I recomputed all arithmetic in fractions.Fraction: exact delta 288213/10088063165309911040 = 2.857e-14, relative 1.7901e-12, and confirmed '%.12g' % float(143/8960) reproduces the transcript string character-for-character, proving the print is uninformative below 1e-13. I also found a tighter bound than the auditor's print-precision argument — the same table's must-vanish entries reach 5.58442181386e-14 (:10622), 1.95x the gap — and a fifth overstating sentence the auditor missed (D:215, "already proven equal"). The repo has no existing record of this (no 8960 in src/workhouse/ or ledger/). Not too weak to state: the documents' own tier columns say T2 (A:58, B:192), so the prose contradicts them, and A §6/B §7 propose landing this into invariants.py and gaps.yaml.

---

### 5.23 `180-of-180-synthetic-tests-unsupported`

| | |
|---|---|
| **severity** | medium |
| **class** | `overstated` |
| **lane** | `certificate` |
| **verifier confidence** | high |
| **where** | cert/INDEPENDENT_REFEREE_REPORT.md:46 |

**Claim as stated.** "Three-way synthetic tests agreed on 180/180 contractions among two exact delta/partition implementations and the modular implementation." (INDEPENDENT_REFEREE_REPORT.md:46)

**What is wrong (originating auditor).** No code and no artifact in the package performs a 180-case three-way synthetic comparison. Grep of every .py for `180`, `synthetic`, `three-way`, `three_way` returns nothing. The claim is also arithmetically distinct from the three checks that ARE shipped (9,100 pure-six entries; 40 non-pure topologies; 44 stratified topologies), so it cannot be a restatement of them.

**Evidence (originating auditor).** `grep -rn "180\b|synthetic|three-way|three_way" cert/*.py` -> no matches. The three shipped counts I reproduced by running the code: 9100 = 90x90 support + 1000 seeded random probes, 40 actual topologies over 20 non-pure signatures, 44 stratified over all 22 signatures.

**Verifier's corrected statement — authoritative.**

> INDEPENDENT_REFEREE_REPORT.md:46 asserts "Three-way synthetic tests agreed on 180/180 contractions among two exact delta/partition implementations and the modular implementation." Nothing in the shipped certificate package supports it, and it is not reproducible here.
> 
> Reproduced facts (paths relative to /tmp/claude-0/-home-user-WORKHOUSE/384fab32-8991-52ce-b2bf-4999d379e3f5/scratchpad/cert):
> 1. `grep -rn "180" --include=*.py .` -> exit 1, zero matches. Same for `synthetic`, `three-way`, `three_way` (case-insensitive) across all 7 .py files. Repo-wide grep of the whole package finds the string "synthetic"/"three-way" on exactly one line: INDEPENDENT_REFEREE_REPORT.md:46.
> 2. No certificate JSON records a count of 180. The three machine-produced counts are, from the scripts' own output files: rank3_order4_exact_haar_summary/crosscheck -> `pure_six_scaled_projector_entries_checked = 9100` (= 90x90 complete nonzero support (crosscheck_modular_haar_reference.py:43 asserts len(support)==90) + 1000 seeded probes at line 58-70, 8100+1000=9100), `actual_frozen_topologies_checked = 40` over `actual_endpoint_signatures_checked = 20` (2 per non-pure signature, lines 74-96), and stratified_actual_topology_modular_audit.json `audited_topologies = 44` over `endpoint_signature_strata = 22` (independent_cross_check_actual_topologies.py:92-96). 180 is none of these and no combination of them (9100+40+44 = 9184).
> 3. Corroborating: AUDIT_REPORT.md:50-57 (byte-identical to WORKHOUSE_RANK3_ORDER4_MODULAR_HAAR_INDEPENDENT_AUDIT_20260823.md; `diff` reports IDENTICAL) enumerates the *same* "independent referee route" as six explicit bullets — inverse-Gram k=1,2,3; pure-six inverse-Gram; 9,100 projector-entry comparisons; 40 topologies over 20 non-pure signatures; 44 stratified over 22 signatures; the 69,800-record replay — and contains no three-way synthetic test and no 180. The 180/180 sentence appears only in the rewritten referee prose.
> 4. Also absent from documents A-D: `grep -niE "synthetic|three.?way|\b180\b"` over the four uploaded .md files returns nothing.
> 
> Scope caveat (the claim is UNSUPPORTED, not disproved): the referee's own tree is external and not present — crosscheck_modular_haar_reference.py:16-23 imports `ledger_generator` and `exact_su3_projector` from `rank3_order4_cubic_ledger/` and `independent_haar_audit/`, neither of which exists in the package. A 180-case synthetic suite may exist in that external tree. So the correct classification is: the 180/180 figure is a T3 assertion with no shipped code, no shipped artifact, and no corroboration in the package's own sibling audit report, in a package whose stated purpose is end-to-end auditability — it must not be counted as verified evidence. One correction to the original finding's evidence line: the shipped counts cannot be "reproduced by running the code" here (external imports missing); 9100/40/44 were confirmed from the scripts' own emitted certificates plus source reading.

**Why it holds.** I opened INDEPENDENT_REFEREE_REPORT.md at line 46 myself and confirmed the wording verbatim. I re-ran the greps independently: zero occurrences of 180, synthetic, three-way, or three_way in any of the 7 .py files; the only occurrence anywhere in the package is the cited line itself. I read crosscheck_modular_haar_reference.py and independent_cross_check_actual_topologies.py in full and confirmed the shipped comparisons are two-way (modular contractor vs one exact reference; modular vs the frozen primary ledger), not three-way, and I read the counts 9100 / 40 over 20 signatures / 44 over 22 strata directly out of the emitted certificate JSONs, matching the code. 180 is not any of those and is not a sum or product of them. The strongest independent corroboration is that AUDIT_REPORT.md:52-57 itemizes the identical referee route as six bullets and omits any synthetic test — so the omission is not merely a shipping accident of scripts but a discrepancy between two documents in the same package. I checked WORKHOUSE for a prior record of this and found none (only unrelated docs/referee/* notes). I withheld holds=false because nothing I found makes the finding an auditor artifact; I sharpened it to "unsupported/unreproducible in-package" rather than "false", since the referee's source tree (independent_haar_audit/, rank3_order4_cubic_ledger/) is external and absent, and I corrected the finding's overstated claim that the shipped counts were obtained by running the code here.

---

### 5.24 `document-C-describes-a-different-artifact-than-E`

| | |
|---|---|
| **severity** | medium |
| **class** | `graph-conflict` |
| **lane** | `certificate` |
| **verifier confidence** | high |
| **where** | artifact C §3 lines 122-140; cert/rank3_order4_exact_haar_summary.json; cert/SHA256SUMS.txt |

**Claim as stated.** Document C §3 "Frozen hash chain" tabulates: exact endpoint-Haar contractor f944bfef..., exact topology ledger gzip 48abeca4..., canonical uncompressed a7f13ca1..., final exact summary d3d2cb89..., and states "The exact-Haar summary binds the same history hash and the contractor hash in work/rank3_order4_exact_haar_run/rank3_order4_exact_haar_summary.json:1".

**What is wrong (originating auditor).** Zero of C's eight tabulated hashes appear anywhere in package E, and E's summary binds neither a history hash nor a contractor hash. C is describing the `exact_haar_sum.py` route under `work/rank3_order4_cubic_ledger/` / `work/rank3_order4_exact_haar_run/`; E is the `modular_haar_contractor.py` route. They are two different programs and two different artifact sets that (allegedly, and per my replay actually) land on the same D_EXACT. Anyone reading C's hash table as provenance for E will find nothing to check.

**Evidence (originating auditor).** Checked all 8 of C's hashes against SHA256SUMS.txt and against `find . -type f -exec sha256sum` over the whole package: 0 hits. E's topology ledger gz is 5337734a..., not C's 48abeca4...; E's summary is 2b845725..., not C's d3d2cb89...; E's contractor is 42eede1a... (AUDIT_REPORT.md:68), not C's f944bfef.... I also computed the uncompressed digests in case a7f13ca1 was one of them: pickle uncompressed = 9593bf47afe1253bbd18276e968f8d8b71067f6269f6c5ff2ce57b6f00e38b95 (12,458,390 B); ndjson ledger uncompressed = 047e66565493df54d3ef748aadc8452aee367656dac4cb27cdf1f35e58c0d624 (48,113,495 B). Neither is a7f13ca1. E's summary keys are exactly: source_topology_ledger_sha256=5337734a..., haar_ledger_sha256=1b9ed180... — no history hash, no contractor hash.

**Verifier's corrected statement — authoritative.**

> Certificate package E carries none of the provenance chain that document C §3 tabulates, and one shared filename makes the two routes easy to confuse. Verified: C holds 13 distinct SHA-256 digests (nine in the §3 chain table, C:122-131; three provenance digests, C:143-145; one at C:251). Hashing all 22 files in /tmp/.../scratchpad/cert (20 distinct digests) plus both gzip-uncompressed payloads gives 0 of 13 matches; a literal text search for C's digests across E's .md/.json/.py files also gives 0 hits. The auditor's uncompressed digests reproduce exactly: root_exact_pair_topologies.pkl.gz -> 9593bf47afe1253bbd18276e968f8d8b71067f6269f6c5ff2ce57b6f00e38b95 (12,458,390 B); rank3_order4_exact_haar_numerators.ndjson.gz -> 047e66565493df54d3ef748aadc8452aee367656dac4cb27cdf1f35e58c0d624 (48,113,495 B); neither is C's a7f13ca1... Also verified: E's rank3_order4_exact_haar_summary.json binds exactly two digests, source_topology_ledger_sha256=5337734a... and haar_ledger_sha256=1b9ed180..., set in the summary dict at modular_haar_contractor.py:520-543 and written at :544 — no history hash and no contractor hash. THREE CORRECTIONS to the finding as filed. (1) The count is nine chain hashes / 13 distinct in C, not "eight". (2) This is NOT a graph-conflict and C is not wrong: C:137 cites work/rank3_order4_exact_haar_run/rank3_order4_exact_haar_summary.json:1, which is EXTERNAL per the path mapping and UNVERIFIABLE HERE; E's identically-named file lives at package root and in modular_haar_run/ and is emitted by a different program, so it cannot refute C's claim about the file C actually names. E declares the separation itself (cert/AUDIT_REPORT.md: "independent modular audit"; "Only after completion was its result compared with the separately implemented primary run"), so "two different programs" is E's stated design, not a discovered inconsistency. (3) C's hashes are not unreliable: its single repo-rooted digest dc9ddfaab437ad4478c85eb631ed0319699c3e3304bd83b22bd31fc2f1f1107d (C:251) verifies exactly against /home/user/WORKHOUSE/corpus-import/programs/hodge_o4_adjudication/src/ENGINE_O4_hodge_v10a7_marked_linked_scalar.py. The two routes do agree on content: C:217 gives D_EXACT = -361008126292641364183/7250590288602460800 and E's summary records the identical rational, with 69,800 and 117,161 matching E's fully_unordered_nonzero_topologies and historical_orientation_sensitive_topologies. Correct classification: C §3's twelve external digests are UNVERIFIABLE HERE (0 hits in E, 0 hits anywhere in /home/user/WORKHOUSE), and the basename collision on rank3_order4_exact_haar_summary.json between the exact_haar_sum.py route (C) and the modular_haar_contractor.py route (E) is a live provenance hazard. Severity should drop from medium to low and kind from graph-conflict to unverifiable-here/provenance-gap.

**Why it holds.** I re-derived every number rather than trusting the evidence line: hashed all 22 files in E plus both uncompressed payloads, intersected against the 13 digests I extracted from C myself (empty), read the summary-writing dict directly in modular_haar_contractor.py:520-544 rather than inferring from the JSON, and confirmed the cited AUDIT_REPORT.md:68. All of the auditor's arithmetic and digest claims reproduce. But the framing does not survive: "document C describes a different artifact than E" is not a conflict, because C never references E, C's cited path is external and unverifiable here, and E's own AUDIT_REPORT.md states it is a separately implemented independent route compared against the primary run only after completion. The auditor also miscounted the hashes (eight vs nine/13). The decisive control is that C's one repo-rooted digest verifies bit-exactly, showing C is a careful document whose external chain is simply absent from the supplied materials — a provenance gap plus a filename-collision trap, both real and reproducible and neither recorded anywhere in the repo (0 grep hits), so the finding stands in the weaker corrected form rather than as filed.

---

### 5.25 `headline-scalar-is-the-repo-quarantined-value-undisclosed`

| | |
|---|---|
| **severity** | medium |
| **class** | `overstated` |
| **lane** | `certificate` |
| **verifier confidence** | high |
| **where** | cert/AUDIT_REPORT.md:28-34; cert/INDEPENDENT_REFEREE_REPORT.md:30-35; /home/user/WORKHOUSE/src/workhouse/constants.py:426-427 |

**Claim as stated.** "the requested final combination is m_{4,rest} = -160506019419340168451/14501180577204921600 ≈ -11.068479463778765" — presented in the Result section of both E reports with no status qualifier.

**What is wrong (originating auditor).** That exact rational is what WORKHOUSE already records as QUARANTINED_SCALAR, annotated "Rejected by both sides; recorded so it is never silently resurrected", with claim status `falsified` and register status `rejected-by-both`. Neither E report mentions this. E's scope caveats are about physical completeness of the generator (AUDIT_REPORT.md:59), not about the value's standing in the register. Document C does disclose the quarantine; the certificate package read on its own does not. A reader taking E at face value would treat a falsified-status scalar as newly certified.

**Evidence (originating auditor).** /home/user/WORKHOUSE/src/workhouse/constants.py:426-427 `#: Rejected by both sides; recorded so it is never silently resurrected.` / `QUARANTINED_SCALAR = Rational(-160506019419340168451, 14501180577204921600)`; /home/user/WORKHOUSE/ledger/contradictions.yaml:35-38 label "quarantined shortcut", `status: rejected-by-both`; /home/user/WORKHOUSE/index/claims.jsonl:150 `"id": "CONST:quarantined scalar", "status": "falsified", "tier": 3`. I confirmed the arithmetic identity exactly in Fractions: D_EXACT + 5315003/140454 - (-1474623/1675520) == -160506019419340168451/14501180577204921600, float -11.068479463778765.

**Verifier's corrected statement — authoritative.**

> E's two distinct report bodies present the exact rational -160506019419340168451/14501180577204921600 (float -11.068479463778765) as "the requested final combination ... m_{4,rest} = D_EXACT + F - V_linked" with no register-status qualifier, and the certificate package nowhere discloses that WORKHOUSE already carries that identical rational as a rejected value.
> 
> Reproduced independently:
> 
> 1. ARITHMETIC (exact, fractions.Fraction). D_EXACT = -361008126292641364183/7250590288602460800, F = 5315003/140454, V_link = -1474623/1675520. D_EXACT + F - V_link == -160506019419340168451/14501180577204921600 exactly, float = -11.068479463778765. This equals src/workhouse/constants.py:427 QUARANTINED_SCALAR bit-for-bit as a Rational (verified by importing workhouse.constants and comparing p/q). E's number is arithmetically CORRECT; the finding is about disclosure, not a numerical error.
> 
> 2. WHAT E SAYS. cert/AUDIT_REPORT.md:28-34 ("the requested final combination is m_{4,rest}=...") and cert/INDEPENDENT_REFEREE_REPORT.md:29-35 ("the requested combination is m_{4,rest}=..."). cert/WORKHOUSE_RANK3_ORDER4_MODULAR_HAAR_INDEPENDENT_AUDIT_20260823.md is byte-identical to AUDIT_REPORT.md (md5 1579a6f4a632bb3f9bda2b780466c29f for both), so all three .md files carry the unqualified presentation. A case-insensitive grep over the whole extracted package for quarant|reject|falsif|disput|shortcut|register|oracle|superseded|provisional returns ZERO hits. E's only scope caveat is AUDIT_REPORT.md:59, which disclaims physical completeness of the primitive generator ("a distinct provenance/modeling obligation") and says nothing about the value's standing in any register. The finding characterizes that caveat correctly.
> 
> 3. WHAT THE REPO SAYS. src/workhouse/constants.py:426-427 — "#: Rejected by both sides; recorded so it is never silently resurrected." then the assignment. ledger/contradictions.yaml:36-40, inside C1, label "quarantined shortcut", value/decimal, and `status: rejected-by-both` at line 40 (the finding cited 35-38; the status key is at 40 — minor citation slip, substance unaffected). index/claims.jsonl:150 — id "CONST:quarantined scalar", status "falsified", tier 3, evidence "record-backed".
> 
> 4. IT IS THE SAME QUANTITY, not a name collision. theory/superseded/MASTER_THEORY.md:416 describes the quarantined shortcut as exactly this construction: raw folded axial Gamma-block (-11.9485781794007) minus the linked-vacuum O(u^4) subtraction (-1474623/1675520), i.e. ax_rest - V_link — the same assembly E performs, under the same role name (mass-kernel rest value at order 4).
> 
> 5. DOCUMENT C DOES DISCLOSE IT, E DOES NOT. Document C:32 ("This does not by itself remove the physical-identification quarantine"), C:34-35 (names the value `M4_SHORTCUT`), C:357-358 ("whether the quarantined shortcut is physically complete or an exact artifact of a selected restricted prescription"). The certificate package read on its own loses a disclosure its companion document makes.
> 
> TWO QUALIFICATIONS the original finding does not make, which bound its strength:
> 
> (a) WORKHOUSE's own rejection status is T3, not machine-established. The only live check touching it, src/workhouse/invariants.py:397-400 (`@dispute.check("quarantined scalar decimal", "MASTER_THEORY §5.5", tier=2)`), verifies only `abs(float(K.QUARANTINED_SCALAR) - (-11.068479463778765)) < 1e-14` and appends "rejected by both sides" as unchecked prose in the detail string. Its cited source, MASTER_THEORY §5.5, resolves only to theory/superseded/MASTER_THEORY.md:416 — a document CLAUDE.md forbids reading as current. The current theory/MASTER_THEORY_UNIFIED_2026-08-20_v4_3.md contains no occurrence of the numerator, the decimal, or the string "quarantin". So the correct framing is: E omits a live register entry (constants.py, contradictions.yaml C1, claims.jsonl) that a WORKHOUSE reader needs — not that E asserts something the repo has proved false. Nothing in E is refuted by the repo.
> 
> (b) "newly certified" overstates the reader harm. E does bound itself to an arithmetic certificate for a frozen generator lineage (AUDIT_REPORT.md:59). The accurate harm is narrower: a reader of E alone would take the value as the certified end-value of the lineage and would not learn that the same rational sits on WORKHOUSE's register as rejected-by-both / falsified, whose displacement from the oracle is exactly local_shift + V_link.

**Why it holds.** I opened all cited lines myself rather than trusting the evidence line, and recomputed the rational in fractions.Fraction against the imported constants.QUARANTINED_SCALAR — identical. The three verifiable components all reproduce: (i) both E report bodies present the value unqualified at the cited lines, and a full-package grep for any rejection/quarantine vocabulary returns zero hits, so the non-disclosure is established by exhaustion rather than sampling; (ii) constants.py:426-427, contradictions.yaml C1 (status at line 40), and claims.jsonl:150 all carry the rejected/falsified standing; (iii) it is provably the same quantity, since theory/superseded/MASTER_THEORY.md:416 defines the quarantined shortcut as ax_rest - V_link, the assembly E performs. I tried three refutations and none landed: the value is not a different quantity sharing a decimal; the finding is not already recorded in the repo, since it concerns the uploaded artifact's omission; and AUDIT_REPORT.md:59 is genuinely a generator-completeness caveat, not a register caveat. Two corrections were needed and are folded in — the contradictions.yaml status key is at line 40, not 35-38, and the repo-side rejection is itself T3 record-backed sourced only from a superseded document (the sole machine check certifies the decimal, not the rejection) — so the finding must be stated as an undisclosed-standing gap, not as E asserting a refuted number. E's arithmetic is exactly right. Confidence high on the reproduced facts; the residual judgement is only whether an external arithmetic certificate owes disclosure of a downstream register, and since companion document C makes that disclosure at C:32 and C:357-358, the omission in E is a real asymmetry.

---

### 5.26 `qbound-lift-gate-is-a-tautology`

| | |
|---|---|
| **severity** | medium |
| **class** | `overstated` |
| **lane** | `certificate` |
| **verifier confidence** | high |
| **where** | cert/AUDIT_REPORT.md:41-44; cert/INDEPENDENT_REFEREE_REPORT.md:16-20; /tmp/claude-0/-home-user-WORKHOUSE/384fab32-8991-52ce-b2bf-4999d379e3f5/scratchpad/cert/validate_modular_haar_ledger.py:74-77 |

**Claim as stated.** "The exact integer-over-QBOUND lift is -3131555650840341423974721085483725619200000 / QBOUND, and reduces exactly to D_EXACT." (AUDIT_REPORT.md:43-44); "the integer-over-QBOUND lift reconstructs the same rational exactly" (INDEPENDENT_REFEREE_REPORT.md:20); summary field `D_EXACT_integer_over_QBOUND_equality: true`.

**What is wrong (originating auditor).** This is an identity, not a check. Given `d | Q`, the lift is defined as `n * (Q // d)` and `Fraction(n*(Q//d), Q)` is `n/d` by construction — it cannot fail once the divisibility assertion on the previous line has passed. One of the two headline "exactness gates" therefore carries no information. The other gate (`QBOUND % denominator == 0`) is real but is a regression fingerprint fitted to a completed run, not an a priori bound.

**Evidence (originating auditor).** validate_modular_haar_ledger.py:74-77: `assert QBOUND % d_exact.denominator == 0; lifted = d_exact.numerator * (QBOUND // d_exact.denominator); ...; assert Fraction(lifted, QBOUND) == d_exact`. Empirical demonstration: 20,000 random rationals with denominators dividing QBOUND — 0 failures of the lift equality. On the second gate: the true lcm of all 69,800 half-term denominators is 5336434452411411148800 = 2^12·3^6·5^2·7·11·13·17^3·19·23·29·31·37, while QBOUND = 2^36·3^20·5^7·7·11·13·17^3·19·23·29·31·37·47. The exponents of 17, 23, 29, 31, 37 match the observed data EXACTLY; slack exists only in 2, 3, 5 (a factor 2^24·3^14·5^5) plus the prime 47, which occurs in no denominator anywhere in the ledger. So QBOUND was calibrated to this run's output.

**Verifier's corrected statement — authoritative.**

> HOLDS, and understated: BOTH advertised QBOUND "exactness gates" are unfailable, not just one.
> 
> (1) Lift-equality is a pure tautology. `validate_modular_haar_ledger.py:74-77` reads `assert QBOUND % d_exact.denominator == 0; lifted = d_exact.numerator * (QBOUND // d_exact.denominator); assert int(summary["D_EXACT_QBOUND_numerator"]) == lifted; assert Fraction(lifted, QBOUND) == d_exact`. With k = QBOUND//d, Fraction(n*k, QBOUND) = Fraction(n*k, d*k) = n/d identically, so line 77 cannot fail once line 74 has passed. No empirics needed. The same pattern with no external comparison at all appears at `modular_haar_contractor.py:512-518`, and `modular_haar_contractor.py:539` emits `"D_EXACT_integer_over_QBOUND_equality": True` as a hardcoded literal. Validator line 76 (against the stored summary field) is not literally vacuous but is already implied by line 73 (`assert frac(summary["D_EXACT"]) == d_exact`) plus the same one-line formula.
> 
> (2) The divisibility gate is ALSO unfailable, which the candidate finding missed. Every accumulated term is weight_T * (n_T / q_product_T) / 2, so d_exact.denominator necessarily divides
>   A = lcm(896, lcm_T 2*denom(weight_T)*q_product_T) = 239017618379238526616076288000 = 2^24*3^13*5^3*7*11*13*17^3*19*23*29*31*37,
> and QBOUND / A = 263139840000 = 2^12*3^7*5^4*47 exactly (verified in Fraction/sympy). A is a function of the frozen weights and pattern lists ONLY — no computed Haar numerator enters it — and q_product is itself recomputed from the hardcoded Q_PATTERN at validate:46-49. Mutation test: 200 trials, ~1,396 Haar numerators per trial replaced by uniform random integers inside their own signed_uniqueness_bound (~280,000 corruptions total): 0 divisibility-gate failures, 0 lift-equality-gate failures. Both gates pass on arbitrarily wrong contraction output.
> 
> (3) The candidate's numeric evidence all reproduces: QBOUND = 62895057857493885215590055852113920000000 = 2^36*3^20*5^7*7*11*13*17^3*19*23*29*31*37*47; lcm of the 69,800 half-term (weighted_contribution/2) denominators = 5336434452411411148800 = 2^12*3^6*5^2*7*11*13*17^3*19*23*29*31*37; slack = 2^24*3^14*5^5*47; 47 divides no weight, haar, weighted_contribution denominator or q_product in the ledger (max q_product = 44789760 = 2^12*3^7*5). Recomputed lift = -3131555650840341423974721085483725619200000, matching AUDIT_REPORT.md:44 and the summary field.
> 
> (4) Correction to the candidate's inference: QBOUND was not calibrated to THIS run. The repo's own audit states its construction — /home/user/WORKHOUSE/corpus-import/records/audits/07-denominator-lift.md:35: "The corpus scan forms the prime-exponent LCM `QBOUND` of every `2 * weight.denominator * q_H` plus the analytic `D11=-13/896` term". That is exactly A's definition, but A != QBOUND here, so the frozen literal at modular_haar_contractor.py:47 is inherited from the predecessor 117,161-orientation-key F07 scan and exceeds this run's own scan-derived bound by 2^12*3^7*5^4*47. Either way it is a scan-derived LCM, not an a priori theorem — as 07-denominator-lift.md:59 lists it among "source assertions, not recorded passes" (:63), with only Medium confidence in its sufficiency (:130).
> 
> Scope limit: the certificate is not empty. The signed-uniqueness-bound check (validate:54,60), the CRT-modulus sufficiency check (validate:58), the per-record q/haar/contribution recomputations, the ledger SHA-256, and the 44-topology independent-contractor cross-check are genuine checks on the computed numerators. The defect is confined to the two QBOUND gates, which AUDIT_REPORT.md:41-44 lists as two of five "Exactness gates" and which INDEPENDENT_REFEREE_REPORT.md:48 counts as "both QBOUND gates. All checks passed."
> 
> Affected text: cert/AUDIT_REPORT.md:41-44; cert/WORKHOUSE_RANK3_ORDER4_MODULAR_HAAR_INDEPENDENT_AUDIT_20260823.md:41-44 (identical wording); cert/INDEPENDENT_REFEREE_REPORT.md:16-20 and :48; summary field D_EXACT_integer_over_QBOUND_equality and D_EXACT_denominator_divides_QBOUND; validation field QBOUND_divisibility_and_integer_lift_passed. Severity medium: D_EXACT itself is not impugned — it rests on the CRT/bound gates and the independent cross-check, not on these two.

**Why it holds.** Re-read both cited scripts at the cited lines and re-derived every number in Fraction/sympy from the shipped 69,800-record ledger. The tautology claim is algebraically exact (Fraction(n*(Q/d), Q) = n/d whenever d|Q) and confirmed at validate_modular_haar_ledger.py:74-77 and modular_haar_contractor.py:512-518, where the contractor version compares against nothing at all. The candidate's prime-exponent evidence reproduced exactly (lcm 5336434452411411148800; QBOUND/lcm = 2^24*3^14*5^5*47; 47 absent everywhere in the ledger). I then went further than the candidate and showed the second gate is unfailable too: d_exact.denominator provably divides A = lcm(896, lcm_T 2*denom(w_T)*q_T) = 2^24*3^13*5^3*7*11*13*17^3*19*23*29*31*37, a function of the frozen inputs alone, and QBOUND/A = 2^12*3^7*5^4*47 is an exact integer; a 200-trial mutation test corrupting ~280,000 Haar numerators produced zero failures of either gate. The repo's own corpus-import/records/audits/07-denominator-lift.md:35 independently documents QBOUND as a corpus-scan LCM rather than an a priori bound, corroborating the characterization while correcting "calibrated to this run" to "inherited from the predecessor 117,161-key scan". Not already recorded as a finding in this repo: 07-denominator-lift.md flags general doubt about denominator-bound sufficiency (:130) but nowhere states that the lift-equality gate is a tautology or that the divisibility gate cannot fail.

---

### 5.27 `summary-json-was-edited-after-generation`

| | |
|---|---|
| **severity** | medium |
| **class** | `provenance-gap` |
| **lane** | `certificate` |
| **verifier confidence** | high |
| **where** | cert/rank3_order4_exact_haar_summary.json:10-14; cert/AUDIT_REPORT.md:41-44; /tmp/claude-0/-home-user-WORKHOUSE/384fab32-8991-52ce-b2bf-4999d379e3f5/scratchpad/cert/modular_haar_contractor.py:544-546 |

**Claim as stated.** The "Exactness gates" bullets — `denominator(D_EXACT)` divides QBOUND, and "The exact integer-over-QBOUND lift is -3131555650840341423974721085483725619200000 / QBOUND" — are presented as outputs of the run, recorded in rank3_order4_exact_haar_summary.json.

**What is wrong (originating auditor).** The shipped summary is demonstrably NOT the byte output of the shipped contractor. modular_haar_contractor.py:544-546 writes it with `json.dumps(summary, indent=2, sort_keys=True)` and LF newlines. The shipped file is CRLF throughout EXCEPT for exactly five consecutive lines, and those five lines are exactly the QBOUND gate block — and two of them are out of the sort_keys=True order the code emits. So that block was inserted or rewritten after the file was produced. The values in it are arithmetically correct (validate_modular_haar_ledger.py:76 asserts the lift and passes), but the gates the reports headline are not, as shipped, run output.

**Evidence (originating auditor).** Byte scan of cert/rank3_order4_exact_haar_summary.json: 47 of 52 lines end CRLF; lines 10-14 end LF, and are D_EXACT_decimal, D_EXACT_QBOUND_numerator, D_EXACT_denominator_divides_QBOUND, D_EXACT_integer_over_QBOUND_equality, QBOUND. I re-ran the shipped contractor over the shipped pickle (367 s, 69,800 records): it emits key order ['D11','D_EXACT','D_EXACT_QBOUND_numerator','D_EXACT_decimal',...]; the shipped file has ['D11','D_EXACT','D_EXACT_decimal','D_EXACT_QBOUND_numerator',...] — the two are transposed. Parsed content is otherwise identical (only elapsed_seconds differs: 264.954 shipped vs 367.153 mine). Same CRLF pattern affects every JSON in the package while every .py and .md is LF, and cert/stratified_actual_topology_modular_audit.json leaks the origin path `C:\Users\Alex\Documents\Codex\2026-08-21\...\work\modular_haar_run\...`, so the artifacts passed through a Windows text transform after generation. Consequence for reproducibility: re-running validate_modular_haar_ledger.py yields sha256 0fdfe7c548fad36fff2e950b13cd866f85c13a4642502ff5b8196746932ae6f5, not the manifest's 7eb3ecb001dae85db0e2d4e1d87157e9b6d32fa42cee565c390e8663c05c3bcd (content identical after stripping CR).

**Verifier's corrected statement — authoritative.**

> PROVENANCE GAP CONFIRMED, with the finding's mechanism and consequence corrected.
> 
> REPRODUCED FACT 1 (byte anomaly). /tmp/claude-0/-home-user-WORKHOUSE/384fab32-8991-52ce-b2bf-4999d379e3f5/scratchpad/cert/rank3_order4_exact_haar_summary.json is 1586 bytes, 52 content lines. 47 lines end CRLF; exactly lines 10-14 end LF. Those five lines are, in shipped order: "D_EXACT_decimal", "D_EXACT_QBOUND_numerator", "D_EXACT_denominator_divides_QBOUND", "D_EXACT_integer_over_QBOUND_equality", "QBOUND" — i.e. exactly the QBOUND/decimal gate block that cert/AUDIT_REPORT.md:41-44 headlines under "## Exactness gates" (AUDIT_REPORT.md:36).
> 
> REPRODUCED FACT 2 (sort-order violation). modular_haar_contractor.py:545-546 writes the file as json.dumps(summary, indent=2, sort_keys=True) + "\n". The shipped top-level key list is ['D11','D_EXACT','D_EXACT_decimal','D_EXACT_QBOUND_numerator','D_EXACT_denominator_divides_QBOUND','D_EXACT_integer_over_QBOUND_equality','QBOUND','crt_prime_count_histogram',...]; sorted() gives ...'D_EXACT','D_EXACT_QBOUND_numerator','D_EXACT_decimal',... ('Q'=0x51 < 'd'=0x64). Of 20 keys, 19 are in exact sort_keys order and exactly one adjacent pair is transposed — at indices 2/3, both of which lie inside the five-line LF island. No invocation of json.dumps(sort_keys=True) can emit that order.
> 
> REPRODUCED FACT 3 (uniqueness). Of the five JSON files in the package, only the summary has any LF-only line and only the summary violates top-level sort order. rank3_order4_exact_haar_validation.json, rank3_order4_modular_reference_crosscheck.json, root_exact_pair_topologies.pkl.summary.json and stratified_actual_topology_modular_audit.json each have 0 LF-only lines and perfectly sorted keys. So this is not a package-wide packaging artifact.
> 
> REPRODUCED FACT 4 (predates the manifest). `sha256sum -c cert/SHA256SUMS.txt` passes on all 20 entries; the summary's shipped CRLF bytes hash to 2b845725b88120f0dc84f91d1ca6aa2f77e82a857098f0d9d7ea0bd4d2f801c6, which is what the manifest pins. The spliced bytes were therefore present before the package was hash-frozen — which strengthens the finding: the manifest certifies the edited file.
> 
> MECHANISM (only consistent explanation): the five gate lines were inserted into an already-written, already-CRLF summary by a line-level text splice (not a re-dump — a re-dump would have re-sorted everything and re-emitted uniform newlines). The splicer placed the block at the correct sorted position (lines 10-14 is exactly where sorted order puts all five) but transposed the first two, and its inserted lines carry LF while the surrounding file carries CRLF.
> 
> THREE CORRECTIONS TO THE FINDING AS FILED:
> (a) "the shipped contractor ... writes it with LF newlines" is WRONG. Path.write_text(s, encoding="utf-8") at modular_haar_contractor.py:545-546 uses platform default newline translation, so on the Windows machine evidenced by the origin-path leak in cert/stratified_actual_topology_modular_audit.json ("C:\\Users\\Alex\\Documents\\Codex\\2026-08-21\\...\\work\\modular_haar_run\\...") it emits CRLF. CRLF is the expected output; the LF lines are the deviation. Same conclusion, inverted polarity.
> (b) "the artifacts passed through a Windows text transform after generation" is an over-reach. No post-generation transform is needed: every .json is CRLF because it was written in Windows text mode at generation, and every .py/.md is LF because those came from an LF-normalized checkout. Only the five-line LF island requires a post-generation edit.
> (c) "the gates the reports headline are not, as shipped, run output" overstates the consequence. I ran validate_modular_haar_ledger.py on a copy of the shipped package: it exits 0 in 3.9 s, and its assertions at validate_modular_haar_ledger.py:74-77 recompute QBOUND % d_exact.denominator == 0, lifted = d_exact.numerator * (QBOUND // d_exact.denominator), int(summary["D_EXACT_QBOUND_numerator"]) == lifted, and Fraction(lifted, QBOUND) == d_exact — all from the 69,800-record ndjson ledger, not from the summary. I also recomputed independently: den = 7250590288602460800 divides QBOUND = 62895057857493885215590055852113920000000; -361008126292641364183 * (QBOUND//den) = -3131555650840341423974721085483725619200000 exactly; Fraction(that, QBOUND) == D_EXACT exactly; D_EXACT == -13/896 + weighted_haar_sum/2 exactly; format(float(D_EXACT),'.17g') == "-49.790170444484609" exactly. So the gate CLAIMS are machine-verified T1/T2; what is broken is only the BYTE PROVENANCE of the JSON that the reports cite as the run's record of them.
> 
> CONSEQUENCE, restated precisely. The manifest-hash divergence the finding cites attaches to cert/rank3_order4_exact_haar_validation.json, not to the summary: re-running validate_modular_haar_ledger.py on Linux regenerates it byte-identical except for line endings, hashing 0fdfe7c548fad36fff2e950b13cd866f85c13a4642502ff5b8196746932ae6f5 against the manifest's 7eb3ecb001dae85db0e2d4e1d87157e9b6d32fa42cee565c390e8663c05c3bcd — I confirmed 0fdfe7c5... is exactly sha256 of the shipped file with CRLF collapsed to LF, and confirmed it by actually re-running. The summary's own hash matches the manifest as shipped. So the reproducibility defect is: the package's hash manifest pins platform-dependent line endings, and separately, cert/rank3_order4_exact_haar_summary.json:10-14 cannot be cited as byte-provenance for the exactness gates because those five lines were spliced in after the contractor wrote the file.
> 
> NOT ALREADY RECORDED: grep across /home/user/WORKHOUSE for exact_haar_summary / modular_haar_contractor / rank3_order4_exact_haar in .md/.yaml/.py returns zero hits; the repo has no entry for this certificate package.
> 
> BOUNDARY NOTE (separate, unverifiable here): document C (be0baa19-...W2_R2_ORACLE_LINEAGE_TRACE...md:137) says "The exact-Haar summary binds the same history hash and the contractor hash in work/rank3_order4_exact_haar_run/rank3_order4_exact_haar_summary.json:1". The shipped summary has no history-hash or contractor-hash key at all, so either that is a different file (the cited path is EXTERNAL to this repo and not present) or the description is inaccurate. Not adjudicated here.

**Why it holds.** I re-derived every element from primary sources rather than trusting the evidence line. The byte scan reproduces exactly: 47 CRLF / 5 LF, with the LF island being precisely the five QBOUND-gate keys. The sort-order violation is dispositive and independent of any platform question: modular_haar_contractor.py:546 uses sort_keys=True, which is deterministic codepoint sorting, and the shipped file is 19/20 keys in exact sort order with one adjacent transposition sitting inside the LF island — no single call to json.dumps can produce that. I tried and eliminated the benign alternatives: a re-dump by any script would re-sort and re-normalize newlines; a lowercase-key variant ('D_EXACT_qbound_numerator') sorts to a different position than shipped; a post-hoc sed rename would not change line endings. Only a line-level splice explains both signatures at once. Uniqueness across the package's other four JSONs (all 0 LF-only lines, all perfectly sorted) rules out a global packaging artifact, and `sha256sum -c` passing on all 20 entries shows the splice predates the hash freeze. Where I disagreed with the auditor I checked instead of assuming: Path.write_text on Windows does translate to CRLF, so the finding's stated code-vs-file newline contrast is wrong reasoning that happens to reach the right island; and running validate_modular_haar_ledger.py myself (3.9 s, exit 0) shows the gate content is independently machine-verified from the ledger, so the finding's "not run output" consequence must be narrowed to byte provenance or the ledger would record something misleading. holds=true because the discrepancy is real, reproducible, unique to this file, inside the hash-frozen package, and unrecorded in the repo; the corrected statement carries the mitigation so the entry does not overstate.

---

### 5.28 `B-3897-misquote`

| | |
|---|---|
| **severity** | medium |
| **class** | `artifact-wrong` |
| **lane** | `citations-AB` |
| **verifier confidence** | high |
| **where** | artifact B §4 (B:143). Repo: corpus-import/records/transcripts/Monday 531 PM.txt:2925, 3897 |

**Claim as stated.** > "its incidence test was algebraically wired to reproduce v10a.20" — `:2925, :3897`

**What is wrong (originating auditor).** The quoted string is verbatim at line 2925 only. Line 3897 does not contain those words; it says "the supposed independent incidence adjudicator was effectively constructed to recover the v10a.20 ledger" — the same proposition in different words. Presenting one quotation under two line numbers makes a paraphrase look like a second independent attestation, which is exactly the "repetition is not independence" failure AGENTS.md names. (:3897 is nonetheless a real, on-point line — the citation is a quotation-accuracy problem, not a pointer error.)

**Evidence (originating auditor).** Monday 531 PM.txt:2925 = "The most egregious example is today: I first told you v10a.21 was the adjudicator, then recognized that its incidence test was algebraically wired to reproduce v10a.20, then immediately replaced it with v10a.22 and again called that the singular next calculation." Monday 531 PM.txt:3897 = "I spent hours repeatedly treating each newly exposed dependency as if it were the last serious obstacle. Then I finally caught a real structural flaw in v10a.21: the supposed independent incidence adjudicator was effectively constructed to recover the v10a.20 ledger. …"

**Verifier's corrected statement — authoritative.**

> Artifact B line 143 (/root/.claude/uploads/384fab32-8991-52ce-b2bf-4999d379e3f5/6a2b59cb-F07_VS_BLIND_TWOFACE_ADJUDICATION.md:143) presents one verbatim-marked quotation — "its incidence test was algebraically wired to reproduce v10a.20" — under two line citations, `:2925, :3897`, into /home/user/WORKHOUSE/corpus-import/records/transcripts/Monday 531 PM.txt. Only one of the two cited lines contains the quoted words.
> 
> Reproduced by exact substring search over the 9756-line transcript: the string occurs on exactly lines 2925 and 2981 — NOT 3897. Line 3897 reads "I spent hours repeatedly treating each newly exposed dependency as if it were the last serious obstacle. Then I finally caught a real structural flaw in v10a.21: the supposed independent incidence adjudicator was effectively constructed to recover the v10a.20 ledger. …" — the same proposition in different words, sharing no quoted phrase ("wired to reproduce" and "algebraically wired" appear nowhere in it).
> 
> Two corrections to the originating auditor's own evidence line, which must not be copied into the ledger as written:
> 
> (a) "verbatim at line 2925 only" is FALSE. The quote is byte-identical at 2925 and 2981 (both 378 chars; L[2924] == L[2980] exactly). The transcript records one assistant message twice — once rendered (~2896-2943) and once re-quoted with LaTeX source (~2945-2989). The correct verbatim citation is `:2925, :2981`, and even that is ONE originating utterance duplicated, not two attestations — AGENTS.md:63-67, "Repetition is not independence": "repeated statements are not independent evidence." The auditor's invocation of that principle is warranted; its count of occurrences was not.
> 
> (b) Severity should be LOW, not medium. Line 3897 is a real, on-point line stating the same proposition, and no numerical or structural claim in B rests on it; B:233 separately lists 3897 among provenance lines with no quote attached, which is legitimate. The defect is quotation accuracy only: B's other four §4 citations (:1978, :2287, :2548, :3702) are each verbatim at a single line (:2548's "…" a legitimate elision of "I identified"), establishing a single-line-verbatim convention that :3897 silently breaks.
> 
> Adjacent, outside this finding's scope and not part of it: B:141 introduces all five §4 quotes with "The maintainer already identified and retracted this route", but every one is an assistant utterance — :1978 and :3897 directly follow maintainer prompts at :1977 and :3892, and :2925 reads "I first told you v10a.21 was the adjudicator". Separate question for whoever owns it.

**Why it holds.** I re-opened both cited lines myself with sed and confirmed by exact substring search in python3 rather than trusting the auditor's evidence line. The core claim reproduces: the verbatim-marked string is absent from Monday 531 PM.txt:3897, so B:143 attaches a quotation to a line that does not contain it. I tried three ways to refute it and failed: (1) no alternate spelling — grep for "wired to reproduce" and "algebraically wired" returns only 2925 and 2981; (2) no off-by-one or alternate line numbering — the auditor quoted 3897's actual text correctly and my independent sed of 3895-3899 matches; (3) the invoked principle is real — AGENTS.md:63 is literally titled "Repetition is not independence". The finding survives, but its evidence line carries an error of its own: the quote is verbatim at 2925 AND 2981, not "2925 only", and those two are a byte-identical duplication of a single message, which changes what the corrected citation should be and sharpens rather than weakens the repetition point. I also judge medium severity too high — the cited line is substantively on point and nothing downstream depends on it — so the corrected statement records it as a low-severity quotation-accuracy defect.

---

### 5.29 `B-axrest-provenance`

| | |
|---|---|
| **severity** | medium |
| **class** | `provenance-gap` |
| **lane** | `citations-AB` |
| **verifier confidence** | high |
| **where** | artifact B §1 table (B:36) and B:46-47; artifact A §1 (A:38). Repo: src/workhouse/constants.py:428, 435; corpus-import/records/transcripts/15 hour RUN.txt:9112, 9130-9131, 10637 |

**Claim as stated.** "`ax_rest` (raw folded rest) | `−11.9485781794014` | `D_EXACT + FOLD`, pre-linked-vacuum" … "All values re-verified this session against `corpus-import/records/transcripts/15 hour RUN.txt` and `src/workhouse/constants.py`."

**What is wrong (originating auditor).** The value -11.9485781794014 appears in neither named file, nor anywhere else in the repository. Every corpus print of this quantity is -11.9485781794007 (or the run's derived variants ...400714 / ...400696), and constants.py records -11.9485781794007. B's number is the correct one (it is float(D_EXACT+FOLD) = -11.948578179401377, computed in the external exact-Haar package), so the number is right and the stated provenance is wrong. More usefully, the 6.77e-13 = 381 ulp divergence between the exact scalar and every recorded run float is itself a finding neither A nor B makes, and it is larger than the run's own quoted residual scales (fifth_residual_max = 2.53e-13, gamma_spread = 2.25e-13 at 15 hour RUN.txt:10646, :10648). The same gap silently propagates to B:42: with B's own ax_rest, M4_ORACLE − ax_rest = 11.17343231638246, not the RUN15_APPLIED_SHIFT = 11.17343231638178 it is equated to. Note the repo constant is NOT a transcription slip: -0.7751458630189173 − 11.17343231638178 = -11.948578179400696, i.e. constants.py:428 faithfully records the run's float.

**Evidence (originating auditor).** grep -rn "11\.94857817940" over the whole repo returns only ...4007 / ...400714 / ...400696 forms: src/workhouse/constants.py:428 `RAW_FOLDED_AXIAL_GAMMA_NUM = -11.9485781794007`; 15 hour RUN.txt:9112 `rest_direct = -11.9485781794007`, :9130 `scalar folded formula = -11.948578179400714`, :9131 `matrix H4 Gamma = -11.948578179400696`; Monday 531 PM.txt:5077, 6509, 6620, 6700, 6722, 8588. Gap: -11.948578179401377 − (-11.9485781794007) = -6.768e-13; math.ulp(11.9) = 1.7764e-15 → 381 ulps. A:38 rounds to -11.9486, hiding it entirely.

**Verifier's corrected statement — authoritative.**

> B's provenance sentence is false for one row of its §1 table. B:36 prints `ax_rest = −11.9485781794014` and B:46-47 states "All values re-verified this session against `corpus-import/records/transcripts/15 hour RUN.txt` and `src/workhouse/constants.py`." That value occurs in neither file, nor anywhere in /home/user/WORKHOUSE: `grep -rn "948578179401" /home/user/WORKHOUSE` returns rc=1, zero matches.
> 
> The number is nevertheless CORRECT and B is on the exact branch: using only repo-internal exact rationals, QUARANTINED_SCALAR (src/workhouse/constants.py:427, Rational(-160506019419340168451, 14501180577204921600)) + LINKED_VACUUM_4 (constants.py:430, Rational(-1474623, 1675520)) = -86634244910174898583/7250590288602460800 = float -11.948578179401377, whose '%+.15g' render is exactly -11.9485781794014. This matches the orchestrator-established float(D_EXACT+FOLD). Two further B numbers are likewise exact-branch renderings absent from the repo: B:40's -V_link = +0.880098715622613 is %+.15g of exact 1474623/1675520 = 0.8800987156226127 (zero grep hits; the corpus prints the C20 float-reconstruction 0.880098715622610 instead). So B's §1 table was produced from the external exact-Haar package, not from the two files it cites. (B:37's M4_SHORTCUT = -11.0684794637788 and B:38's M4_ORACLE = -0.7751458630189 ARE in 15 hour RUN.txt:10634, 10633 — the provenance sentence fails specifically on the ax_rest and -V_link rows.)
> 
> Every repo print of the raw folded axial Gamma rest is the float branch: constants.py:428 `RAW_FOLDED_AXIAL_GAMMA_NUM = -11.9485781794007`; 15 hour RUN.txt:9112 `rest_direct = -11.9485781794007` (a `+.15g` print, code at :6717), :9130 `scalar folded formula = -11.948578179400714`, :9131 `matrix H4 Gamma = -11.948578179400696`; also Monday 531 PM.txt:5077, 6509, 6527-6528, 6620, 6700, 6722, 8588; "# HODGE v10a.26 - Factor-(5,2) Comp.txt":9124, 9142-9143; "# HODGE v10a.24c - production runti.txt":8710, 8728-8729; "15 hour RUN. results.txt":1353, 1371-1372; NB_O4_hodge_v10a26_...alt2.ipynb:1389, 1407-1408; theory/superseded/MASTER_THEORY.md:416; index/claims.jsonl:229.
> 
> Quantified divergence between the exact scalar and the run float: -11.948578179401377 - (-11.9485781794007) = -6.76792e-13 = 381 ulps (math.ulp(11.9) = 1.7763568394002505e-15); against the run's full float -11.948578179400696 it is -6.80345e-13 = 383 ulps. constants.py:428 is NOT a transcription slip — it is the 15-significant-digit print of the run's own float: -0.7751458630189173 - 11.17343231638178 = -11.948578179400696 exactly, and the run defines ax_rest at 15 hour RUN.txt:7713 as `float(V23_AXIAL_SHAPE['rest_direct'])`, a matrix-computed float (constants.py:428 is 2.0 ulps from that full float, being the rounded print).
> 
> Consistency consequence inside B: with B's own exact ax_rest, M4_ORACLE - ax_rest = 11.17343231638246, not RUN15_APPLIED_SHIFT_NUM = 11.17343231638178 (constants.py:435); they differ by 6.803e-13. B:42 asserts that equality but prints only "+11.1734", so this is an identity-level mismatch, not a printed wrong digit. Artifact A:38 rounds ax_rest to -11.9486, hiding the branch difference entirely.
> 
> Two qualifications to the original finding. (1) The gap is not unnoticed in the corpus: Monday 531 PM.txt:6722,6724 computes -11.9485781794007 - (-0.880098715622610) = -11.0684794637781 and remarks it "agrees with the modern candidate to roughly 7x10^-13, consistent with the numerical residuals." It is un-quantified there and unrecorded in the ledger (C20 covers the 3.0e-15 LINKED_VACUUM_4 float-reconstruction; C22 covers gate-85), so recording it in ulps and against the exact rational is new, but "a finding neither A nor B makes" is weaker than "unknown to the corpus." (2) The comparison to the run's quoted residual scales (fifth_residual_max = 2.52575738102223e-13 at 15 hour RUN.txt:10646; gamma_spread = 2.25264251696444e-13 at :10648) gives factors of only 2.7x and 3.0x — same order of magnitude, and those residuals measure shape-fit closure and eigenvalue spread, not the error in rest_direct, so they do not refute the corpus's "consistent with the numerical residuals" judgement. State the 381-ulp gap as a documented provenance/precision split, not as evidence the run float is wrong.

**Why it holds.** Independently reproduced from primary sources. The whole-repo grep for "948578179401" returns zero matches, so B:36's value is genuinely absent from both files B:46-47 names, and I confirmed by reading the cited lines that constants.py:428 and 15 hour RUN.txt:9112/9130/9131 all carry the ...4007/...400714/...400696 float forms. I recomputed the exact value from two repo-internal exact rationals (QUARANTINED_SCALAR at constants.py:427 + LINKED_VACUUM_4 at constants.py:430) rather than relying on the external package, getting -86634244910174898583/7250590288602460800 -> -11.948578179401377, whose 15-sig-digit print is exactly B's number; and I recomputed the gap as 6.76792e-13 = 381 ulps against constants.py:428 and 383 ulps against the run's full float. I also confirmed the reverse-check that constants.py:428 faithfully tracks the run (M4_ORACLE - RUN15_APPLIED_SHIFT = -11.948578179400696 exactly) and located the run's definition of ax_rest as a matrix float at 15 hour RUN.txt:7713. I found one piece of corroboration the auditor missed (B:40's -V_link is likewise an exact-branch 15g render absent from the repo, while the corpus prints the C20 artifact value), which makes the provenance conclusion stronger. I trimmed two overstatements: the corpus does note the ~7e-13 gap at Monday 531 PM.txt:6724, and the residual-scale comparison is only 2.7x-3.0x on quantities that measure something else, so the finding should be stated as a provenance/precision split rather than as evidence the run float is defective.

---

### 5.30 `T2-rows-carry-no-tolerance`

| | |
|---|---|
| **severity** | medium |
| **class** | `overstated` |
| **lane** | `citations-AB` |
| **verifier confidence** | high |
| **where** | artifact A §2 row 6 (A:62); artifact B §6 row 5 (B:195). Repo: corpus-import/records/transcripts/15 hour RUN.txt:10620-10626; ledger/contradictions.yaml:49-54 |

**Claim as stated.** A §2: "blind table closes | T2 | Σ per-size `c4` = oracle `−0.7751458630189` (`:10626`)"; B §6 check 5: "`blind_table_sums_to_oracle` | T2 | Σ size-c4 = `−0.775145863…` (`:10626`)"

**What is wrong (originating auditor).** Stated as T2 with no tolerance, which CLAUDE.md's tier table requires ("float agreement within a stated tolerance … tolerance in the detail line"). The actual agreement is far looser than the quoted digits imply, because the per-size rows are printed to 12 significant figures. Summing the six printed rows as printed gives -0.7751458630184425, which differs from the printed TOTAL at :10626 by 4.748e-13 (4277 ulps of 0.775). Summing them the way B's own §2 block writes them (sizes 4 and 5 set to exact zero) gives -0.7751458630184, differing by 5.173e-13 — and that value equals 8*HAMER_A4_NUM (8 * -0.0968932328773) bit-for-bit, so the "table closes" check as written is really a check at the 1e-12 print-precision level, not a check of the oracle sum.

**Evidence (originating auditor).** 15 hour RUN.txt:10620-10625 rows, :10626 `TOTAL m1/m2/m3/m4 = 1.0 0.03594771241824929 -0.4371355568371267 -0.7751458630189173`. Python: sum of the six printed c4 = -0.7751458630184425, diff = 4.748423876321795e-13, /math.ulp(0.775) = 4277 ulps; with sizes 4,5 → 0.0, sum = -0.7751458630184 and 8*(-0.0968932328773) = -0.7751458630184 (equal as floats), diff from TOTAL = 5.173e-13. The repo already records this bridge honestly, with its tolerance: ledger/contradictions.yaml:49-54 "8 * a_4 = -0.7751458630184, agreeing to 5.2e-13".

**Verifier's corrected statement — authoritative.**

> Both T2 rows for the blind-table closure omit a tolerance, and artifact A's row additionally quotes more digits than its cited evidence can support.
> 
> (1) NO STATED TOLERANCE (both artifacts, confirmed). A:62 `| blind table closes | T2 | Σ per-size c4 = oracle −0.7751458630189 (:10626) |` and B:195 `| 5 | blind_table_sums_to_oracle | T2 | Σ size-c4 = −0.775145863… (:10626) |` are tagged T2 with no tolerance in the detail line. CLAUDE.md's tier table requires T2 = "float agreement within a stated tolerance … tolerance in the detail line". The companion check `f07_twoface_adjudication_check.py` cited at B:187 is present neither in /home/user/WORKHOUSE nor in the extracted certificate zip, so no tolerance is recoverable from the artifact set. The same omission applies verbatim to A:58 / B:190 (`one-face agreement | T2 | 143/8960 = blind size-1`), which the original finding did not flag.
> 
> (2) A:62 OVERSTATES PRECISION (A only). The cited evidence is the printed table at corpus-import/records/transcripts/15 hour RUN.txt:10620-10625, whose rows carry 12 significant figures. Summing the six printed c4 values gives -0.7751458630184425 against the TOTAL at :10626 of -0.7751458630189173: absolute diff 4.748423876321795e-13 = 4277 ulps of 0.775 (relative 6.126e-13). Summation order is immaterial — all 720 permutations give one of 3 doubles spanning 3e-16. A:62 prints the oracle to 13 significant figures (−0.7751458630189); the printed rows reproduce only 12 (−0.775145863018|4 vs |9). The honest bound from 12-sig-fig inputs is |Σ − oracle| < 1.55e-12 (worst-case accumulated half-ulp-of-last-printed-digit over the six rows), so this row can be asserted at T2 only with a ~1e-12 tolerance, not as an equality to 13 digits. B:195, which writes `−0.775145863…` with an explicit ellipsis at 9 significant figures, is NOT overstated on digits — its only defect is the missing tolerance.
> 
> (3) NOT ALREADY RECORDED, AND THE "8*a_4" INFERENCE DOES NOT FOLLOW. ledger/contradictions.yaml:49-53 records a different statement — the external Hamer bridge "8 * a_4 = -0.7751458630184, agreeing to 5.2e-13" — and no repo invariant checks the per-size table (grep of src/workhouse/invariants.py returns nothing). It is true that zeroing the size-4/size-5 numerical residues (-1.3933298959e-14, -2.85049761573e-14) gives sum = -0.7751458630184, the identical double to 8*(-0.0968932328773) (both exactly -0.7751458630184000497820306918583810329437255859375, diff from TOTAL 5.1725e-13 = 4659 ulps), but that is a coincidence of two quantities truncating to the same 13-digit decimal, not evidence that the closure check "is really" the Hamer bridge; and it does not hold for the rows as literally printed. That part of the original finding should be dropped.
> 
> Net: a tier-discipline / precision-labelling defect, not a numerical error — the oracle value itself is correct. Severity low-to-medium. Remedy is a detail line, e.g. "Σ printed per-size c4 = -0.7751458630184425 vs TOTAL -0.7751458630189173, |Δ| = 4.75e-13 (4277 ulps), within the 1.55e-12 print-precision bound of the 12-sig-fig source rows".

**Why it holds.** Reproduced independently from primary sources. Transcript lines 10619-10626 read directly and match the citation. Recomputed in python3: Σ six printed c4 = -0.7751458630184425 vs TOTAL -0.7751458630189173, diff 4.748423876321795e-13 = 4277 ulps of math.ulp(0.775)=1.1102230246251565e-16; a permutation sweep shows order-independence to 3e-16; the sizes-4,5-zeroed sum -0.7751458630184 is the same double as 8*(-0.0968932328773), checked via exact Decimal expansion, diff from TOTAL 5.1725e-13; worst-case print-rounding bound over the six 12-sig-fig rows = 1.55e-12. Read A:62 and B:195 verbatim — neither carries a tolerance, and a grep for tol/atol/rtol/within across both documents returns nothing relevant. `f07_twoface_adjudication_check.py` is absent from both the repo (find) and the certificate zip, so the omission cannot be rescued by inspecting the script. ledger/contradictions.yaml:49-53 read directly: it records the 8*a_4 Hamer bridge at 5.2e-13, a distinct claim, so the finding is not already recorded. I narrowed the finding on two points where the original auditor overreached: B:195's ellipsised 9-digit value is not digit-overstated, and the 8*HAMER bit-match is a shared-truncation coincidence requiring the printed size-4/5 residues to be discarded, so it supports no conclusion about what the check tests.

---

### 5.31 `check-script-8-vs-6`

| | |
|---|---|
| **severity** | medium |
| **class** | `graph-conflict` |
| **lane** | `citations-AB` |
| **verifier confidence** | high |
| **where** | artifact A §0 (A:27), §6 (A:147-148), appendix (A:163); artifact B (B:8-9, B:185-199, B:234) |

**Claim as stated.** A: "`f07_twoface_adjudication_check.py` — runnable 8-check screen; exit 0" (A:27), "the 8 machine-verified checks + the two OPEN discriminators" (A:148), "python3 f07_twoface_adjudication_check.py  # 8 checks, exit 0" (A:163). B §6 tabulates the same script as 6 rows: 5 machine checks + 1 FINDING.

**What is wrong (originating auditor).** A and B give different contents for the same named script, and the script does not exist anywhere reachable — not in /home/user/WORKHOUSE, not in the extracted certificate zip, not in the upload directory (a filesystem-wide find for the name returns nothing). So the count cannot be adjudicated, and neither document's "exit 0" / "Verified: the guard rejects an F07 size-2 value tagged with retired-engine provenance" (B:198-199) is checkable. Both documents lean on this artifact as their machine-verified spine ("If you read one thing: F … for the argument; the check for the machine-verified spine", A:29-30).

**Evidence (originating auditor).** `find / -name f07_twoface_adjudication_check.py` → no results. Certificate zip extraction at /tmp/claude-0/-home-user-WORKHOUSE/384fab32-8991-52ce-b2bf-4999d379e3f5/scratchpad/cert contains 23 entries, none named f07*. A:27 vs B:191-196 (rows numbered 1-6).

**Verifier's corrected statement — authoritative.**

> UNVERIFIABLE-SPINE (not a graph-conflict). The one artifact both A and B designate as their machine-verified spine — `f07_twoface_adjudication_check.py` — is unreachable, so nothing routed through it rises above T3.
> 
> Reproduced absence: `find / -name 'f07*' -not -path '/proc/*'` returns zero results (the identical invocation locates /home/user/WORKHOUSE/FRONTIER.md, so `find` is functional). `unzip -l /root/.claude/uploads/384fab32-8991-52ce-b2bf-4999d379e3f5/dc08a31e-WORKHOUSE_RANK3_ORDER4_MODULAR_HAAR_CERTIFICATE_20260823.zip` lists 22 files (23 entries incl. the `modular_haar_run/` dir), none named f07*; a case-insensitive grep for `f07|twoface|adjudication` over the extracted tree at /tmp/claude-0/-home-user-WORKHOUSE/384fab32-8991-52ce-b2bf-4999d379e3f5/scratchpad/cert yields exactly one hit, a coincidental hex substring inside a digest (cert/stratified_actual_topology_modular_audit.json:3082, "51c74da66f1f07c7…") — no real occurrence. grep for `twoface|adjudication_check` across /home/user/WORKHOUSE outside corpus-import: nothing. Artifacts C and D never mention the script.
> 
> Consequence, at cited lines: A:27 "runnable 8-check screen; exit 0", A:163 "python3 f07_twoface_adjudication_check.py  # 8 checks, exit 0", B:8-9 "(exit 0; writes nothing…)", and B:198-199 "Verified: the guard rejects an F07 size-2 value tagged with retired-engine provenance, and accepts one tagged with an independent (§5-compliant) source" are all unexecutable here. A:29-30 nevertheless routes the reader to "the check for the machine-verified spine".
> 
> CORRECTION to the candidate's headline: the 8-vs-6 count is NOT a demonstrated contradiction and is too weak to state on its own. B:185 titles §6 "The runnable check (summary)", and B itself describes a verified behavior appearing in no table row — the two-sided provenance guard at B:198-199. B's six rows are therefore provably not an exhaustive assertion inventory, and 5 table checks (B:191-195) + the target pin + guard-reject + guard-accept = 8 reconciles with A:147-148 "the 8 machine-verified checks". Likewise A's "two OPEN discriminators" vs B's single `twoface_adjudication_OPEN` FINDING row (B:196) is a granularity difference. Both differences are unadjudicable precisely because the script is missing — that is the finding, not the arithmetic of 8 vs 6.
> 
> Mitigating context that must travel with the finding: A:5-7 self-declares "No repository file was edited; the session was read-only and everything below lives in scratchpad until a maintainer decides what lands", and three of the six documents in A's own §0 set (rows A, C, F at A:21, A:23, A:26 — DENOMINATOR_LOCALIZATION_INVESTIGATION, ORACLE_COUNTERFACTUAL_AUDIT, F07_VS_BLIND_COORDINATION_NOTE) are also absent from the five uploaded artifacts. The absence is a systemic gap in the delivery, not evidence of fabrication. Suggested severity: medium for the unverifiability, none for the count.

**Why it holds.** I re-ran the search myself rather than trusting the evidence line, and validated the search tool against a known file. The script is absent from the filesystem, from the certificate zip (22 files listed by `unzip -l`, plus a content grep over the extraction), from the upload directory (5 files, listed), and from the repo. A:27/147-148/163 and B:8-9/185-199/234 read exactly as quoted. So the "exit 0" and the "Verified: the guard rejects…" sentence are unexecutable, and both documents explicitly lean on the script as their machine-verified spine (A:29-30) — that part of the finding reproduces cleanly and is material under the repo's rule that only a machine check confers status. But the candidate's framing as a graph-conflict overstates: B:185 calls its §6 a summary and B:198-199 describes a guard behavior outside the table, so B's 6 rows are not an exhaustive count, and 5 + pin + 2 guard behaviors = 8 reconciles the numbers. The count difference alone would be too weak to ledger; the unverifiability is not.

---

### 5.32 `retraction-attributed-to-maintainer`

| | |
|---|---|
| **severity** | medium |
| **class** | `overstated` |
| **lane** | `citations-AB` |
| **verifier confidence** | high |
| **where** | artifact B §4 (B:140); artifact A §4 (A:115-119) and §0 row E. Repo: corpus-import/records/transcripts/Monday 531 PM.txt:1977-1982, 2546-2549, 2925, 3891-3903 |

**Claim as stated.** "The maintainer already identified and **retracted** this route" (B §4); "was retired by the maintainer as unable to adjudicate (`Monday 531 PM.txt:1978/2287/3702`)" (A §4)

**What is wrong (originating auditor).** All five quoted lines are in the assistant's voice in the transcript, not the maintainer's. The maintainer's turn is line 1977 ("review all runs and give me a consistent fucking path forward. im sick of this fucking run around."); "Stop. Do not run v10a.21r." at 1978 opens the reply, which continues "I reviewed the run lineage…" at 1980. Same pattern at 3891 (user: "why are you fucking me over? … Just tell me the truth") → 3893 ("Because I overcorrected"). Line 2548 is a third thing again: it is the assistant quoting the v10a.22 script's own header block ("raw cluster values : RECOMPUTED FROM…" at :2546), not a standalone judgement. So the retraction is the same generator retracting its own prior claim. That is still evidence, but under CLAUDE.md ("No document is authority", "Some of it was written with AI assistance and some of it is wrong") it is materially weaker than a maintainer ruling, and A/B's phrasing converts it into one. The provenance guard both documents build on top of it inherits the inflation.

**Evidence (originating auditor).** Monday 531 PM.txt:1977 (user turn), 1978-1982 (reply); 2546-2549 (v10a.22 header block quoted, with :2548 inside it); 2925 ("I first told you v10a.21 was the adjudicator, then recognized that…"); 3891 (user) → 3893 ("Because I overcorrected."); 3696-3706 ("Within the same conversation I went from: … to: …").

**Verifier's corrected statement — authoritative.**

> MISATTRIBUTION (medium, overstated): artifacts A and B attribute the retirement of the v10a.21/v10a.21r adjudicator to the maintainer, but all six transcript lines they cite are in the assistant's voice, not the human's.
> 
> B:140 states "The maintainer already identified and **retracted** this route" and blockquotes five items; B:26 and A:117-118 repeat it ("was retired by the maintainer as unable to adjudicate (`Monday 531 PM.txt:1978/2287/3702`)"). I opened every cited line in /home/user/WORKHOUSE/corpus-import/records/transcripts/Monday 531 PM.txt:
> 
> - :1977 is the human turn ("review all runs and give me a consistent fucking path forward. im sick of this fucking run around."). :1978 "Stop. Do not run v10a.21r." OPENS THE REPLY, which continues at :1980 "I reviewed the run lineage, the preserved run logs, and the newest adjudicator code."
> - :2287 ("Retire v10a.21/v10a.21r as adjudicators…") is an item in the list opened at :2266-2268 ("The one consistent path forward / From here, I would freeze the project and follow exactly this sequence:"), preceded by :2254 ("That is the mistake. I should not have sent you into another expensive run…").
> - :2548 is inside the assistant's walkthrough of the v10a.22 script header, introduced at :2544 ("The header then tells you exactly how this differs from the previous adjudicator:") and spanning :2546-2555.
> - :2925 "I first told you v10a.21 was the adjudicator, then recognized that its incidence test was algebraically wired to reproduce v10a.20…" (verbatim duplicate at :2981).
> - :3702 is inside :3694-3706 ("I repeated exactly the behavioral pattern I had just identified. / Within the same conversation I went from: …").
> - :3897 answers human turn :3891 ("why are you fucking me over? … Just tell me the truth") after :3893 "Because I overcorrected."
> 
> Exhaustive count: grep "v10a\.21" over the 530,027-byte transcript returns 22 hits (:1978, 1982, 2151, 2256, 2287, 2441, 2548, 2804, 2925, 2981, 3640, 3642, 3677, 3698, 3702, 3845, 3885, 3897, 3919, 3990, 4036, 4306). 0 of 22 fall in a human turn. The human turns in that span are :1977, 2439, 2522, 2693, 2845, 3891, 4054, 4199 and none mentions v10a.21. No maintainer ruling retiring v10a.21 exists in the file.
> 
> Two aggravating details beyond the original finding: (1) B:147 quotes :2548 as "the circular construction … is gone", where the ellipsis elides exactly the two words "I identified" that mark the speaker as the assistant; (2) the transcript disclaims its own authority at :3889 — "My earlier '12 times' answer and this audit are themselves assistant-generated interpretations of that underlying record."
> 
> The charitable reading ("retired in the maintainer's session") is unavailable: B:140 ascribes agency ("already identified and retracted"), and B:217 fixes the term's meaning in the same document — "The relabel is a maintainer judgement for **Alex**" — matching CLAUDE.md, where the maintainer is Alex. So A/B convert one AI generator's self-retraction into a human ruling, which under CLAUDE.md ("No document is authority… Some of it was written with AI assistance and some of it is wrong") is a materially weaker warrant, and the provenance guard built on top inherits the inflation.
> 
> CONCLUSION IS NEVERTHELESS CORRECT, AND THE REPO HOLDS A STRONGER WARRANT. corpus-import/records/audits/08-rooted-adjudication.md:103 establishes the same thing from source code rather than chat: "The incidence identity is constructed to invert. RAW is defined as the zeta sum of DELTA_MIN, then the recursive transform is its literal Möbius inverse (source lines 7097-7124). Recovering DELTA_MIN is a useful historical implementation check, not a physical energy calculation. The destination architecture retires this adjudication instead of adding another oracle" — see also :102 ("Shared-corpus adjudication, not an independent oracle"). Remedy: keep the provenance guard, delete "by the maintainer" from A:117 and B:26/B:140, restore "I identified" at B:147, and re-cite the guard to audits/08-rooted-adjudication.md:102-103 (code-level) with the transcript demoted to corroborating assistant self-retraction.
> 
> Not previously recorded: grep for "Monday 531" across ledger/, notes/, src/, tests/ returns nothing; records/transcripts/README.md carries only the generic "Transcripts are not authority" warning.

**Why it holds.** Reproduced from primary sources. Opened every cited line of Monday 531 PM.txt myself and read enough surrounding context to fix each speaker: :1977 is the human turn and :1978 opens the reply ("I reviewed the run lineage" at :1980); :2287 sits inside "From here, I would freeze the project and follow exactly this sequence" (:2268); :2548 sits inside the v10a.22 header walkthrough introduced at :2544 and still contains "I identified"; :2925, :3702, :3897 are all first-person assistant self-criticism. An exhaustive grep shows all 22 occurrences of "v10a.21" in the 530,027-byte file are assistant-voice and no human turn (:1977, 2439, 2522, 2693, 2845, 3891, 4054, 4199) ever mentions it, so no maintainer ruling exists to cite. Re-read B:26/140-147/217 and A:25/115-119 to confirm the wording; B:217 ("a maintainer judgement for Alex") plus CLAUDE.md fixes "maintainer" as the human, closing off a charitable reading. I additionally found that B:147's ellipsis removes precisely the speaker marker, and that :3889 has the transcript disclaiming its own authority. The finding is not the auditor's error and is not already recorded (no hits for "Monday 531" in ledger/, notes/, src/, tests/). Severity is medium rather than high only because the underlying conclusion is independently and more strongly supported by the repo's own code-level audit at corpus-import/records/audits/08-rooted-adjudication.md:102-103, so the fix is a re-citation, not removal of the guard.

---

### 5.33 `twoface-vacuum-called-exact`

| | |
|---|---|
| **severity** | medium |
| **class** | `overstated` |
| **lane** | `citations-AB` |
| **verifier confidence** | high |
| **where** | artifact B §3 (B:91-108), esp. B:93 and B:103-107. Repo: corpus-import/programs/hodge_o4_adjudication/src/ENGINE_O4_hodge_v10a7_marked_linked_scalar.py:5192, 5425-5444; corpus-import/records/transcripts/Monday 531 PM.txt:5193-5205 |

**Claim as stated.** "## 3. Exact two-face vacuum (a clean input that *is* available) — The two-face attached-vacuum weight is exact and independent of the disputed axial construction: e4(C) = −54321/837760 … Verified two ways in the corpus: coplanar and perpendicular pairs **agree** … disconnected two-face vacuum spectator has **zero** linked O(u⁴)"

**What is wrong (originating auditor).** The cited corpus evidence is float, not exact. v10a.7 computes e4(C) and omega4 in floating point and gates them against the rationals at a tolerance (default 3e-9); the transcript's own output writes the rationals with a tilde — "e4(C)=-0.0648407658517953 ~ -54321/837760" — which is the corpus's notation for rational *recognition*, and B drops the tilde. The "zero" spectator is likewise `abs(_vfar_omega) < V10A7_TOL`. The exact rationals enter the record only as hard-coded constants in v10a21r:358-359. The identity B builds on them (e4(C) − 2·V1 = −327/83776) IS exact and I confirmed it in Fraction, so B's T1 label survives for the identity; what does not survive is "the two-face attached-vacuum weight is exact" as a statement about the corpus's evidence for the inputs.

**Evidence (originating auditor).** ENGINE_O4_hodge_v10a7_marked_linked_scalar.py:5192 `V10A7_TOL = float(os.environ.get('V10A7_TOL','3e-9'))`; :5433 `gate(f'v10a.7 vacuum {cls} pair full e4=-54321/837760', abs(z['e4']-float(_Q17(-54321,837760)))<V10A7_TOL, z['e4'])`; :5434 same shape for omega4; :5436 the coplanar/perpendicular "agree" gate is `abs(...)<V10A7_TOL`; :5444 `gate('v10a.7 disconnected two-face vacuum spectator has zero linked O(u^4)', abs(_vfar_omega)<V10A7_TOL, _vfar_omega)`. Transcript prints: Monday 531 PM.txt:5193 and :5198 both "e4(C)=-0.0648407658517953 ~ -54321/837760; omega4=-0.00390326585179523 ~ -327/83776"; :5204 "disconnected pair spectator omega4=+0.000e+00".

**Verifier's corrected statement — authoritative.**

> OVERSTATED (confirmed, with corrections). Artifact B:91-107 heads a section "Exact two-face vacuum (a clean input that *is* available)" and asserts at B:93 that "The two-face attached-vacuum weight is exact", citing corpus verification at B:102-107. The corpus evidence B cites is floating-point with tolerance gating, not exact arithmetic.
> 
> PROOF THAT THE COMPUTATION IS FLOAT (stronger than the tolerance argument alone): the transcript's own printed values differ from the rationals B calls exact.
> - /home/user/WORKHOUSE/corpus-import/records/transcripts/Monday 531 PM.txt:5196 prints e4(C) = -0.06484076585179532; float(Fraction(-54321,837760)) = -0.06484076585179527. Gap 5.5511e-17 = 4 ulps.
> - Same file :5197 prints omega4 = -0.0039032658517952346; float(Fraction(-327,83776)) = -0.0039032658517952636. Gap 2.9057e-17 = 67 ulps.
> An exact rational computation would agree to 0 ulps. The nonzero ulp gaps are positive evidence of float arithmetic, independent of any reading of the source.
> 
> MECHANISM, verified at the cited lines of /home/user/WORKHOUSE/corpus-import/programs/hodge_o4_adjudication/src/ENGINE_O4_hodge_v10a7_marked_linked_scalar.py:
> - :5192 V10A7_TOL = float(os.environ.get('V10A7_TOL','3e-9')).
> - :5383-5397 _v17_vac_cluster computes e1..e4 through _v17_inner; the state amplitudes are built as float(c)/den at :5375. e4 = Dd - e2*Nn in float.
> - :5425 linked = z['e4'] - 2.0*_v1['e4'] (float multiply).
> - :5433 gate(... abs(z['e4']-float(_Q17(-54321,837760))) < V10A7_TOL ...); :5434 the same shape for -327/83776; :5436 the coplanar/perpendicular "agree" gate is abs(difference) < V10A7_TOL.
> - :5265-5266 _v17_rational(x) = Fraction(float(x)).limit_denominator(1e9) — the tilde in the transcript print at :5429-5430 is rational *recognition*, not derivation. B drops the tilde when it reprints the transcript's numbers at B:97-98.
> Gate slack relative to the actual residual: 3e-9 / 5.5511e-17 = 5.40e7 for e4(C), and 3e-9 / 2.9057e-17 = 1.03e8 for omega4. A 3e-9 window around -0.0648407658517953 admits an enormous family of rationals with denominator under 1e9; the gate cannot single out 837760.
> 
> "VERIFIED TWO WAYS" IS ONE COMPUTATION ON TWO GEOMETRIES. :5423-5434 is a single loop calling the same _v17_vac_cluster on the coplanar and perpendicular representatives; Monday 531 PM.txt:5193 and :5198 print bit-identical e4(C) = -0.0648407658517953, so the :5436 agree-gate is comparing a difference of exactly 0.0. Per AGENTS.md ("repetition is not independence"), that is one originating computation, not two independent derivations. The same holds across files: every occurrence of -54321/837760 in the repo is either this identical gate line (v10a7:5433, v10a24c:6269, and its verbatim copies inside four transcripts) or its float printout.
> 
> NO EXACT DERIVATION EXISTS ANYWHERE IN THE REPO. I grepped the whole tree (excluding .venv) for 54321/837760 and 327/83776. The exact rationals enter exact (Fraction) arithmetic at exactly one place — ENGINE_O4_hodge_v10a21r_adjudicator_only_same_kernel.py:358-359, V1=_XQ(-39,1280) and VPAIR=_XQ(-327,83776) — as hard-coded inputs, which corpus-import/records/audits/08-rooted-adjudication.md:45 describes as "Each one-face embedding receives V1=-39/1280; each adjacent pair receives VPAIR=-327/83776". CORRECTION TO THE ORIGINAL FINDING: e4(C) = -54321/837760 is NOT among those hard-coded constants; it never enters exact arithmetic anywhere in the repo at all. Its only appearances are the float gate and the recognition print. Even the one-face input V1 is itself only float-gated in v10a.7 (:5411, abs(_v1['e4']+39/1280) < V10A7_TOL).
> 
> CORRECTION TO THE "ZERO SPECTATOR" PRONG (the weakest part of the finding). The gate at :5444 is indeed abs(_vfar_omega) < V10A7_TOL, but the recorded output at Monday 531 PM.txt:5204 is "disconnected pair spectator omega4=+0.000e+00" — at %.3e formatting that is an exact float 0.0, not a sub-tolerance residual. So B's word "zero" at B:105 matches the observed value literally. What remains true is that it is a float zero from a float pipeline, not a proof of exact vanishing — and that the source comment at :5438-5439 self-describes as an "Exact disconnected-spectator check" while gating at 3e-9, which is an internal mislabel in the corpus, not B's error.
> 
> WHAT SURVIVES FOR B. The identity e4(C) - 2*V1 = -327/83776 is exact and I reconfirmed it in Fraction: Fraction(-54321,837760) - 2*Fraction(-39,1280) == Fraction(-327,83776) is True. B's T1 label for the identity stands. What does not stand is the framing at B:91-93 of the two rationals themselves as an exact, available input: their corpus status is T2 (float agreement within a stated 3e-9 tolerance) from a single originating computation, with the rationals obtained by limit_denominator recognition.
> 
> NOT ALREADY RECORDED HERE. Neither 83776 nor 837760 appears anywhere in /home/user/WORKHOUSE/src, /ledger, /tests, /index, CERTIFIED.md, or FRONTIER.md, so this is not a known-and-recorded item.
> 
> CONTEXT THAT DOES NOT RESCUE B: theory/superseded/MASTER_THEORY.md:568 also writes "Vacuum sector exact: ... e_4(C)=-54321/837760, omega_4=-327/83776". That is T3 prose in a superseded document (CLAUDE.md non-negotiable 1: never read superseded as current), and corpus-import/theory/DOC_FLUX_constants_index.md:248 records 327/83776 with an occurrence count of 1 sourced to that same superseded file. B is echoing corpus prose, but under CLAUDE.md's "no document is authority, only a machine check is", the only machine check is the T2 float gate.
> 
> Note in passing (a separate finding, not this one): B:99 prints 83776 = 2^7*7*11*17^2, which is 2848384. sympy.factorint(83776) = {2:6, 7:1, 11:1, 17:1}.

**Why it holds.** I re-opened all cited lines rather than trusting the evidence line, and the mechanism reproduces exactly: V10A7_TOL=3e-9 at v10a7:5192; the e4/omega4 gates at :5433-5434 and the agree-gate at :5436 are all abs(...)<V10A7_TOL against float(_Q17(...)); _v17_rational at :5265-5266 is Fraction(float(x)).limit_denominator(1e9), i.e. recognition; the cluster amplitudes are float at :5375 and linked uses 2.0* at :5425. The decisive independent confirmation is numerical and was not in the original evidence line: the transcript's own printed values sit 4 ulps (5.5511e-17) and 67 ulps (2.9057e-17) away from float(-54321/837760) and float(-327/83776), which an exact computation could not produce, and the gate slack is 5.4e7x and 1.0e8x those residuals. A repo-wide grep shows no exact derivation of either rational anywhere; v10a21r:358-359 hard-codes only V1 and VPAIR as Fractions and e4(C) never enters exact arithmetic at all, which sharpens rather than weakens the finding. Nothing in src/, ledger/, tests/, index/, CERTIFIED.md or FRONTIER.md records this, so it is not already known. I mark two corrections: the finding misattributes e4(C) to the v10a21r hard-coded constants, and the disconnected-spectator prong is weaker than stated because Monday 531 PM.txt:5204 records an exact float 0.0, so B's word "zero" is literally what was observed there. B's exact identity e4(C)-2*V1 = -327/83776 verifies in Fraction, so only the "the input is exact" framing is overstated, which matches the finding's own kind=overstated and medium severity.

---

### 5.34 `v10a21r-size1-never-run`

| | |
|---|---|
| **severity** | medium |
| **class** | `provenance-gap` |
| **lane** | `citations-AB` |
| **verifier confidence** | high |
| **where** | artifact B §4 (B:124-131). Repo: corpus-import/programs/hodge_o4_adjudication/notebooks/NB_O4_hodge_v10a21r_adjudicator_only_same_kernel.ipynb; .../src/ENGINE_O4_hodge_v10a21r_adjudicator_only_same_kernel.py:132-137, 295-296, 361-366 |

**Claim as stated.** "`v10a.21r` … **does** yield an exact F07 per-size decomposition. Its size-1 weight is `143/8960` — matching. It is tempting to read off its size-2 weight and compare to the blind `−0.403971702978`."

**What is wrong (originating auditor).** No output from v10a.21 or v10a.21r exists anywhere in the corpus, so the statement about what the engine yields is unverifiable here. Both notebooks are unexecuted: execution_count is None and there are zero stored outputs in each; a grep for the engine's own size-table print strings ("exact linked weight by cluster size", "nonzero irreducible marked clusters by size", "MINIMAL-SUPPORT LEDGER sizes", "ADJUDICATOR-ONLY RESUME") matches only the source and the two empty notebooks, never a transcript. This is consistent with "Stop. Do not run v10a.21r." The claim is also non-obvious from the code, and turns on a subtlety worth recording for whoever tries it: v10a21r:296 puts analytic_11 = -13/896 on the singleton support frozenset((ROOT,)), and :361-363 attaches V1 to frozenset((ROOT,f)) for f in `_single_emb`, which is self-inclusive (`_V17_NEIGH = [...]  # includes self`), so exactly one V1 does land on {ROOT} — but whether the fold pieces (-2C, -E2*N, +J, :335-340) also contribute at {ROOT} cannot be settled without running the engine.

**Evidence (originating auditor).** json load of corpus-import/programs/hodge_o4_adjudication/notebooks/NB_O4_hodge_v10a21r_adjudicator_only_same_kernel.ipynb → cells [markdown, code], execution_count None, 0 outputs; same for NB_O4_hodge_v10a21_exact_rooted_cluster_adjudicator_a100.ipynb. ENGINE_O4_hodge_v10a21r_adjudicator_only_same_kernel.py:132-137 `_v21_size_table` groups by `len(S)`; :295-296 `ledger[frozenset((ROOT,))] += _XQ(analytic_11)`; :361-366 V1 → frozenset((ROOT,int(f))), VPAIR → frozenset(S|{ROOT}); ENGINE_O4_hodge_v10a7_marked_linked_scalar.py:5224 `_V17_NEIGH = [...]  # includes self`, :5448 `_single_emb=sorted(_V17_NEIGH[_mark])`, :5460 gate count 13.

**Verifier's corrected statement — authoritative.**

> PROVENANCE GAP CONFIRMED (narrowed). Artifact B §4 (B:124-128) states that `v10a.21r` "**does** yield an exact F07 per-size decomposition" whose "size-1 weight is `143/8960`". No execution of v10a.21 or v10a.21r exists anywhere in this repository, so that is a T3 assertion about unrun code.
> 
> (1) Both notebooks are unexecuted. `json.load` of /home/user/WORKHOUSE/corpus-import/programs/hodge_o4_adjudication/notebooks/NB_O4_hodge_v10a21r_adjudicator_only_same_kernel.ipynb gives 2 cells [markdown, code], `execution_count=None`, 0 outputs; NB_O4_hodge_v10a21_exact_rooted_cluster_adjudicator_a100.ipynb likewise (2 cells, exec None, 0 outputs, 295011-char code cell).
> 
> (2) No transcript. Fixed-string grep across the whole repo (excl. .git) for the engine's own print strings — "EXACT ROOTED MARKED-CLUSTER INCIDENCE ADJUDICATOR", "MINIMAL-SUPPORT LEDGER sizes", "nonzero clusters by size", "nonzero irreducible marked clusters by size", "exact linked weight by cluster size", "ADJUDICATOR-ONLY RESUME", "v10a.21 recursive incidence transform" — matches only ENGINE_O4_hodge_v10a21r_adjudicator_only_same_kernel.py and the two empty notebooks. Never a run log. The uploaded certificate bundle (scratchpad/cert, 19 files) contains no v10a.21 material either. This is consistent with "Stop. Do not run v10a.21r." — corpus-import/records/transcripts/Monday 531 PM.txt:1978, and with :2287 "Retire v10a.21/v10a.21r as adjudicators", :2441 "Use this. Do not run v10a.21/21r.", :3702.
> 
> (3) CORRECTION to the auditor's framing — the *value* is corroborated, only the *attribution* is not. `143/8960` is independently recorded in the corpus as the exact one-face order-4 coefficient, not as a v10a.21r output: transcript "Monday 531 PM.txt":9702 lists the exact one-face Gelfand regression targets `[8/3, 1, 1/2, 7/32, 143/8960]`, and NB_O4_hodge_v10a29b_m5_first_no_m4_rerun.ipynb hard-codes `V26_ONE_FACE_PREFIX_EXACT = ("8/3","1","1/2","7/32","143/8960")` (cell 1) with `float(Fraction(143,8960))` (cell 7). So B's "matching" is substantively supported elsewhere; what is unverifiable here is that v10a.21r produces it.
> 
> (4) STRUCTURAL SUBTLETY — verified, and the auditor's missing link closed. In ENGINE_O4_hodge_v10a21r_adjudicator_only_same_kernel.py: :132-137 `_v21_size_table` groups by `len(S)`; :313 passes `analytic_11=_XQ(-13,896)` for the D bilinear with `skip_11=True`, and :295-296 deposits it as `ledger[frozenset((ROOT,))] += _XQ(analytic_11)`; :357-363 sets `V1=_XQ(-39,1280)` and `for f in _single_emb: V_MIN[frozenset((ROOT,int(f)))] += V1`; :377-379 forms `DELTA_MIN = EA_MIN - V_MIN`. Whether a V1 lands on the singleton `{ROOT}` turns on `ROOT ∈ _single_emb`, which the auditor asserted from `_V17_NEIGH` self-inclusion alone — that is insufficient, because `_single_emb` is built around `_mark`, not around `ROOT`. I closed it: ENGINE_O4_hodge_v10a7_marked_linked_scalar.py:5224 `_V17_NEIGH = [frozenset(face_support_faces[f]) ...]  # includes self`; :5292 `_cycle_root=next(f for f,(v,a,b) in enumerate(faces) if v==(0,0,0) and (a,b)==(0,1))`; :5401 `_vac_seed=_cycle_root`; :5447 `_mark=_vac_seed`; :5448 `_single_emb=sorted(_V17_NEIGH[_mark])`; :5460 gates `len(_single_emb)==13`. Meanwhile :4491 `T1_POLS = ((1,2),(0,2),(0,1))` and :5570 `anchor_faces=[next(f ... v==(0,0,0) and (a,b)==pol) for pol in T1_POLS]`, so `ROOT = anchor_faces[2]` (v10a21r:112) selects the identical predicate as `_cycle_root`. Hence ROOT == _cycle_root == _vac_seed == _mark, `_single_emb = sorted(_V17_NEIGH[ROOT])` contains ROOT exactly once (it is a sorted frozenset), and exactly one V1 lands on `{ROOT}`. Therefore DELTA_MIN[{ROOT}] = -13/896 + 39/1280 + (fold contributions at {ROOT}) = 143/8960 + fold, verified exactly with fractions.Fraction. The fold pieces (-2*C_MIN, -E2N_MIN, +J_MIN at v10a21r:335-340) are built by `_v21_cluster_bilinear` WITHOUT `skip_11`, so their (1,1) blocks do produce singleton supports; whether they cancel at {ROOT} cannot be settled without running the engine. B's "143/8960" is thus an unverified prediction that the fold vanishes at one face, not a read-off.
> 
> (5) Not already recorded: grep of ledger/, FRONTIER.md, CERTIFIED.md, README.md, docs/ for "v10a.21"/"v10a21" returns nothing.

**Why it holds.** I independently reproduced every component. Notebook JSON load confirms 0 outputs and execution_count None in both v10a.21 notebooks. Repo-wide fixed-string grep for seven distinct engine print strings hits only source plus the two empty notebooks — no transcript, and nothing in the uploaded cert bundle. All cited line numbers (v10a21r:112, 132-137, 295-296, 313, 357-366, 377-379; v10a7:5224, 5292, 5401, 5447-5448, 5460, 5570) are exact. The arithmetic -13/896 + 39/1280 = 143/8960 checks exactly. I strengthened the finding by closing the gap in its own evidence chain: the auditor inferred "exactly one V1 lands on {ROOT}" from _V17_NEIGH self-inclusion, but _single_emb is indexed at _mark, not ROOT; I traced _mark = _vac_seed = _cycle_root and showed it selects the same face predicate as anchor_faces[2], so the conclusion holds for a reason the auditor did not give. I also narrowed the finding: 143/8960 is independently attested in the corpus as V26_ONE_FACE_PREFIX_EXACT c4 (transcript:9702, NB_O4_hodge_v10a29b cells 1 and 7), so only the attribution to v10a.21r output is unverifiable, not the value. Nothing in ledger/, FRONTIER.md or CERTIFIED.md mentions v10a.21, so it is not already recorded. Medium severity is right: artifact B itself says "Do not" read off size-2 and quotes the maintainer's retraction, so the document is describing a trap rather than promoting a result — but it still states an unrun engine's output as fact.

---

### 5.35 `c-invariant-line-range-wrong`

| | |
|---|---|
| **severity** | medium |
| **class** | `artifact-wrong` |
| **lane** | `citations-CD` |
| **verifier confidence** | high |
| **where** | artifact C §1 line 61; repo src/workhouse/invariants.py:414-418 vs :421-429 |

**Claim as stated.** C §1 lines 60-61: "the invariant explicitly says the final equality is target-derived and hence not an independent verification in `work/WORKHOUSE-readonly/src/workhouse/invariants.py:414-422`"

**What is wrong (originating auditor).** The cited range points mostly at a DIFFERENT invariant. invariants.py:414-418 is the tail of the C20 linked-vacuum float-reconstruction check; :419-420 are blank; :421-422 are only the decorator and `def _():` of the applied-shift check. The sentence C paraphrases lives at :428, outside the cited range. The substantive claim is TRUE of the repo — it is just cited to the wrong lines, which matters in a document whose entire value proposition is line-accurate forensic citation.

**Evidence (originating auditor).** invariants.py:414 = `not agree_to_float,`; :415-417 = the C20 f-string ("...NOT to float precision as C20 states..."); :418 = `)`; :421 = `@dispute.check("run's applied shift is not Delta_Gamma", "GLUEBALL §9.2 / C22", tier=2)`; :422 = `def _():`; :428 = `"— target-derived, so gate 85 is not an independent scalar verification",`. Correct citation would be invariants.py:421-429.

**Verifier's corrected statement — authoritative.**

> Artifact C cites `invariants.py:414-422` (C line 61; sentence spans C:59-61, not "60-61") for the statement that "the invariant explicitly says the final equality is target-derived and hence not an independent verification". Against WORKHOUSE at HEAD a76ccb7 (working tree clean), that range does not contain the paraphrased text. Line accounting of the 9 cited lines in /home/user/WORKHOUSE/src/workhouse/invariants.py: :414-418 (5 lines) are the tail of a DIFFERENT invariant — the C20 linked-vacuum float-reconstruction check, decorator at :403, corpus cite "MASTER_THEORY C20" (:414 `not agree_to_float,`; :415-417 f-strings; :418 `)`); :419-420 are blank; only :421-422 belong to the applied-shift check (:421 `@dispute.check("run's applied shift is not Delta_Gamma", "GLUEBALL §9.2 / C22", tier=2)`, :422 `def _():`). The paraphrased sentence is the sole occurrence of that phrasing in the file, at :428 — 6 lines past the cited end. The correct citation is :421-429. C's substantive claim is TRUE of the repo (comment at :423-424 plus :428).
> 
> CRITICAL CORRECTION to the finding's stated cause and severity: this is a STALE citation, not a wrong one. `git log` shows lines 414-422 were byte-exact for that same check block (decorator through closing paren) across 7 consecutive commits, 0cb3c50 through f643c4b (valid until 2026-08-21T21:41Z); commit fb8a35c (2026-08-21T23:50Z, "ADR 0010: tools enter through evidence tiers") displaced it exactly +7 lines to :421-429. So C's range was a precisely correct citation of an earlier revision, which refutes the finding's charge of carelessness in "a document whose entire value proposition is line-accurate forensic citation". C's three other repo citations (constants.py:203-214, constants.py:426-435, ADR 0002:50-57) are exact at HEAD, but `git diff f643c4b a76ccb7` shows both files byte-identical across that window, so they are equally exact at the old commit and cannot discriminate which snapshot C read. C pins SHA-256 for every external artifact (§3, C:120-131) but pins no commit/revision for `work/WORKHOUSE-readonly/`, so the snapshot is unpinnable from the document. Severity should be downgraded from medium to LOW: the reader lands 7 lines above the target in the same file and same dispute suite, the paraphrase is substantively accurate, and the root defect is an unpinned readonly-snapshot reference rather than a misreading of the repo. The generalizable ledger-worthy point is that C cites repo line ranges with no pinned revision, so every such range decays silently as the repo moves.

**Why it holds.** I independently reproduced every mechanical element from primary sources rather than trusting the evidence line: read invariants.py:400-432 with clean numbering, grepped the file for "target-derived" (single hit at :428), and read C:52-64 to confirm the exact citation text and line. All five of the finding's evidence claims check out at HEAD. However, defaulting to refutation led me to test the stale-snapshot hypothesis via git history, which the finding never considered: `git show` on each historical revision proves 414-422 was the exact bracket of that check across commits 0cb3c50..f643c4b, and fb8a35c shifted it +7 lines. That makes the citation demonstrably correct-for-an-older-revision, not arbitrary, so the finding's framing ("just cited to the wrong lines", plus the implied carelessness) is materially misleading even though its factual core survives. I then tried to discriminate which snapshot C read by checking its other three repo citations at both commits; `git diff f643c4b a76ccb7` shows constants.py and ADR 0002 unchanged, so the test is inconclusive and I report it as such rather than asserting C read HEAD. The finding holds as a reproducible fact about the repo as it stands, but only with the cause reclassified and severity dropped to low.

---

### 5.36 `d-one-face-exact-overstated`

| | |
|---|---|
| **severity** | medium |
| **class** | `overstated` |
| **lane** | `citations-CD` |
| **verifier confidence** | high |
| **where** | artifact D lines 29, 45-54, 215; repo corpus-import/records/transcripts/15 hour RUN.txt:10620-10624; corpus-import/programs/hodge_o4_adjudication/src/ENGINE_O4_hodge_v10a24c_rootedfullt1_dualcoldoracle_a100.py:7291 |

**Claim as stated.** D line 29: "The most useful new localization is exact: the one-face contribution agrees between the branches." D line 215: "the one-face sector is already proven equal."

**What is wrong (originating auditor).** The F07/preflight side is an exact rational; the blind side is a 12-significant-figure printout, so the agreement is established to roughly 6e-14 absolute, not exactly. "Exact" and "proven equal" are the wrong words for a float comparison. (The analytic side of D's claim is correct and I confirmed it exactly — see the confirmed list — but the blind side cannot be pinned better than its own print format and noise floor.)

**Evidence (originating auditor).** 143/8960 = 0.0159598214285714285714...; the transcript prints `c4=+0.0159598214286` under `%+.12g` (format string at ENGINE_O4_hodge_v10a24c...py:7291), which pins the true value only to +/-5e-14 absolute = +/-3.13e-12 relative. The blind branch's own numerical floor is the same order: rows where exact zero is required print c2 = -5.58442181386e-14 (size 3), +2.0872192863e-14 (size 4), -1.80966353014e-14 (size 5) at '15 hour RUN.txt':10622-10624. Contrast the F07 side, which is the exact rational -13/896 + 39/1280 = 143/8960.

**Verifier's corrected statement — authoritative.**

> Artifact D overstates the one-face result as exact/proven when only one side of the comparison is exact. D:29 ("The most useful new localization is exact: the one-face contribution agrees between the branches"), D:31 (heading "The one-face sector agrees exactly"), D:140 ("The exact one-face equality above further shows..."), and D:215 ("the one-face sector is already proven equal") assert an equality that the cited evidence cannot support, and D carries no qualifier anywhere.
> 
> The F07 side is exact: -13/896 + 39/1280 = 143/8960 = 0.01595982142857142857... (verified in Fraction). Note both inputs are cited only to files external to this repo (work/rank3_order4_exact_haar_package_verify/...:124-126 and work/fold_linked_exact/README.md:21-27), so the inputs themselves are UNVERIFIABLE here; only the arithmetic is verifiable, and it is correct.
> 
> The blind side is float64, not rational, by construction — not merely by print format. In the producing source embedded in the transcript, /home/user/WORKHOUSE/corpus-import/records/transcripts/15 hour RUN.txt:7673 declares `bysize=_v23c_dd(lambda:np.zeros(5,float))`, fed from `c=np.asarray([float(...)],dtype=float)` at :7235. The gate name "exact-SW" (:7667) means "canonical Hermitian SW/BCH; no polynomial fit/window" (:7670) — exact algebra evaluated in floating point, not exact rationals. No rational exists on the blind side to compare against.
> 
> Print resolution, computed exactly: the value is emitted under `%+.12g` at /home/user/WORKHOUSE/corpus-import/programs/hodge_o4_adjudication/src/ENGINE_O4_hodge_v10a24c_rootedfullt1_dualcoldoracle_a100.py:7291 (identical statement at '15 hour RUN.txt':7680). At this magnitude the 12-significant-figure grid spacing is 1e-13, so the token `c4=+0.0159598214286` at '15 hour RUN.txt':10620 pins the float64 only to [0.01595982142855, 0.01595982142865]. Because 143/8960 lies 2.857e-14 below the grid centre, the supported bound is sup|x - 143/8960| = 7.857e-14 absolute = 4.923e-12 relative = 5662 float64 ulps. (This corrects the auditor's stated +/-5e-14 / 3.13e-12, which is the half-grid width rather than the bound on the deviation.)
> 
> The blind branch's own numerical floor is the same order, in the same table: entries required to vanish print c2 = -5.58442181386e-14 (size 3, :10622), +2.0872192863e-14 (size 4, :10623), -1.80966353014e-14 (size 5, :10624), and for c4 specifically -1.3933298959e-14 (size 4, :10623) and -2.85049761573e-14 (size 5, :10624). So the comparison cannot be tightened below roughly 1e-13 absolute regardless of print format.
> 
> Defensible restatement: the blind rooted oracle's size-1 c4 agrees with the exact F07 one-face coefficient 143/8960 to within 7.86e-14 absolute (4.92e-12 relative) — a T2 numerical agreement, not a T1 derivation and not a proof. D's downstream inferences at :58-61 (ruling out four mechanisms) and :215 (directing the next computation to start at two-face) rest on that T2 result, which is strong evidence but is not the "proven equal" D claims.
> 
> Adversarial checks that did not refute: the v10a.23 polynomial-fit path (tolerances V23C_FIT_STAB_TOL=5e-3 at engine:6795 and err<2e-5 at engine:7278) was NOT used for this table — the v10a.26 exact-SW path returns fit_stability=0.0 ('15 hour RUN.txt':7242) — so that looser floor does not apply; it would have strengthened, not weakened, the finding. Not already recorded in the repo: grep for "8960" and "0159598" across src/, ledger/, tests/, theory/, index/ and top-level *.md returns no hits.

**Why it holds.** Reproduced from primary sources. Confirmed the `%+.12g` format at engine:7291 and at the transcript's own embedded source :7680, and confirmed the blind accumulator is numpy float64 (`np.zeros(5,float)` at :7673, `dtype=float` at :7235) — so the blind side has no exact rational at all, which is a stronger basis for the finding than the print format alone. Recomputed the bound exactly in Fraction: the printed 12-sig-fig token constrains the float only to +/-7.857e-14 absolute (4.923e-12 relative, 5662 ulps), slightly weaker than the auditor's quoted +/-5e-14. Confirmed the table's own intended-zero entries reach 5.58e-14 (c2) and 2.85e-14 (c4) at :10622-10624, matching that order. Re-read D and found no qualifier at lines 29, 31, 140, or 215, and found D building two downstream inferences on the claimed exactness. Checked the obvious refutation — that the coefficients might come from an exact-rational SW path — and it fails: "exact-SW" means no fit window, not rationals. Also checked that the repo does not already record this (no hits for 8960 or 0159598 outside corpus-import). The finding is a genuine tier overstatement under CLAUDE.md's T1/T2 boundary and AGENTS.md's "numerical agreement is not proof".

---

### 5.37 `83776-factorization-wrong`

| | |
|---|---|
| **severity** | medium |
| **class** | `artifact-wrong` |
| **lane** | `corpus-value-search` |
| **verifier confidence** | high |
| **where** | B §3 — vs corpus-import/records/transcripts/chat.txt:1770 |

**Claim as stated.** "83776 = 2⁷·7·11·17² (in-scope, | QBOUND)" (B §3)

**What is wrong (originating auditor).** 83776 = 2^6·7·11·17 = 64·1309. The printed product 2^7·7·11·17^2 equals 2848384, which is 34x too large. The corpus itself has the right factorization of the parent denominator: chat.txt derives 83776 = 2^6·1309 and 837760 = 2^7·5·7·11·17. The 17^2 appears to be imported from the fold denominator 140454 = 2·3^5·17^2. The divisibility half of B's claim is correct: 83776 | QBOUND.

**Evidence (originating auditor).** sympy.factorint(83776) = {2:6, 7:1, 11:1, 17:1}; 2**7*7*11*17**2 = 2848384; 83776 = 64*1309, 1309 = 7*11*17. QBOUND % 83776 == 0 (QBOUND = 2^36·3^20·5^7·7·11·13·17^3·19·23·29·31·37·47). Corpus correct value: corpus-import/records/transcripts/chat.txt:1770 "837760 = 2^7·5·1309".

**Verifier's corrected statement — authoritative.**

> ARTIFACT-WRONG (isolated transcription error, no downstream consequence). Document B (/root/.claude/uploads/384fab32-8991-52ce-b2bf-4999d379e3f5/6a2b59cb-F07_VS_BLIND_TWOFACE_ADJUDICATION.md:99) prints "83776 = 2⁷·7·11·17²  (in-scope, | QBOUND)". The factorization is false: sympy.factorint(83776) = {2:6, 7:1, 11:1, 17:1}, i.e. 83776 = 2^6·7·11·17 = 64·1309. The printed product 2^7·7·11·17^2 = 2848384, which is 34x = 2·17 times too large. Exponent errors are in two places at once (2^7 instead of 2^6, and 17^2 instead of 17^1); the 2^7 is the exponent of the parent denominator 837760 = 2^7·5·1309 quoted two lines above at B:97.
> 
> The parenthetical "| QBOUND" is true but non-discriminating: QBOUND = 62895057857493885215590055852113920000000 (cert/modular_haar_contractor.py:47, cert/independent_replay_modular_crt.py:24, cert/validate_modular_haar_ledger.py:14) = 2^36·3^20·5^7·7·11·13·17^3·19·23·29·31·37·47, so BOTH the true 83776 and the bogus 2848384 divide it. The divisibility gate cannot catch this error.
> 
> Blast radius is nil: every quantity B §3 actually uses is exact and correct — e4(C) = -54321/837760, omega4 = e4(C) - 2*V1 = -327/83776, V_link = -1474623/1675520 with 1675520 = 1280*1309 = 83776*20 = 2^8*5*7*11*17. Only the decorative prime factorization is wrong, so no numeric result in B, and no repo constant, is affected. Suggest severity LOW rather than medium.
> 
> Corroborating (not authoritative) corpus lines: /home/user/WORKHOUSE/corpus-import/records/transcripts/chat.txt:1750 derives 83776 = 2^6*1309 = 64*1309, and :1768/:1770 settle 837760 = 2^7*5*1309 = 2^7*5*7*11*17. Caveat: chat.txt is a self-correcting scratch transcript that also contains transient WRONG intermediates (:1750 "837760 = 2^9*5*7*11*17", :1760 "837760 = 640*1309"), retracted by :1768 — so cite factorint, not chat.txt, as the check.
> 
> Not previously recorded: grep for 83776 over /home/user/WORKHOUSE/ledger/, src/workhouse/, README.md, FRONTIER.md, CERTIFIED.md returns nothing; the single repo occurrence is theory/superseded/MASTER_THEORY.md:568, which states the value -327/83776 with no factorization. 83776 is not a registered constant in this repo, so no repo check exercises it.

**Why it holds.** Reproduced independently from primary sources. Byte-dumped B:99 to confirm the literal text "83776 = 2⁷·7·11·17²" (not a rendering artifact). Recomputed with sympy: factorint(83776) = {2:6,7:1,11:1,17:1}, and 2**7*7*11*17**2 = 2848384 != 83776. Opened corpus-import/records/transcripts/chat.txt at the cited region myself (:1750, :1768, :1770) and found the correct settled factorizations, plus transient wrong ones the auditor did not mention. Loaded QBOUND from the certificate zip and factored it, finding that the auditor's stated QBOUND factorization is exactly right but that the divisibility half is non-discriminating (2848384 also divides QBOUND) — a point the original finding missed. Confirmed no repo ledger/check already records this. The one part of the evidence line I could not confirm is the causal claim that 17^2 was imported from 140454 = 2·3^5·17^2: factorint(140454) does give {2:1,3:5,17:2} and FOLD_EX = 5315003/140454 is in the same pipeline (corpus-import/records/audits/07-denominator-lift.md:38), but nothing establishes the import, and the 2^7 is better explained by the adjacent 837760 = 2^7·5·1309 at B:97. I removed that speculation from the corrected statement and downgraded the suggested severity, since no numeric result depends on the erroneous factorization.

---

### 5.38 `twoface-vacuum-tier-and-route-count`

| | |
|---|---|
| **severity** | medium |
| **class** | `overstated` |
| **lane** | `corpus-value-search` |
| **verifier confidence** | high |
| **where** | A §2 row 4; B §3, §6 check 3 — vs corpus-import/programs/hodge_o4_adjudication/src/ENGINE_O4_hodge_v10a7_marked_linked_scalar.py:5192,5433-5444 |

**Claim as stated.** "two-face vacuum | T1 | e4(C) = −54321/837760, ω4 = −327/83776 (coplanar==perp)" (A §2); "Verified two ways in the corpus: coplanar and perpendicular pairs agree ... [and] disconnected two-face vacuum spectator has zero linked O(u⁴)" (B §3); check #3 tier T1 (B §6).

**What is wrong (originating auditor).** Two problems. (i) Tier: the corpus evidence for both values is a FLOAT gate at V10A7_TOL = 3e-9, i.e. T2, not T1. The only exact statement available is the rearrangement ω4 = e4(C) − 2·V1, which is a definitional identity once the two inputs are literals, not independent evidence for the value. (ii) Route count: the disconnected-spectator zero is a NULL CONTROL on a different configuration (a non-adjacent pair, whose ω4 must vanish); it produces no value for the connected pair and is therefore not a second route to −327/83776. The corpus's real second constraint — which the documents miss — is the exact closure 13·V1 + 124·VPAIR = V_link, which pins VPAIR given V_link, V1 and the integer counts. Counted properly the corpus has one originating measurement (v10a.7 `_v17_vac_cluster`, instantiated on two geometries) plus one exact closure constraint.

**Evidence (originating auditor).** corpus-import/programs/hodge_o4_adjudication/src/ENGINE_O4_hodge_v10a7_marked_linked_scalar.py:5192 `V10A7_TOL = float(os.environ.get('V10A7_TOL','3e-9'))`; :5433 `gate(... pair full e4=-54321/837760', abs(z['e4']-float(_Q17(-54321,837760)))<V10A7_TOL ...)`; :5434 same form for omega4; :5436 coplanar/perp agreement gate (also float); :5444 disconnected-spectator gate `abs(_vfar_omega)<V10A7_TOL`. Exact identity I verified: Fraction(-54321,837760) - 2*Fraction(-39,1280) == Fraction(-327,83776) → True.

**Verifier's corrected statement — authoritative.**

> OVERSTATED TIER + MISCOUNTED ROUTE, but the finding's own proposed replacement is itself wrong and must be dropped.
> 
> (i) TIER — CONFIRMED. A §2 row 4 (`52ebdfa7-RANK3_ORDER4_MASTER_RECORD.md:60`) labels "two-face vacuum | T1 | e4(C) = -54321/837760, omega4 = -327/83776 (coplanar==perp)", under the header at :52 "Every row is T1 (exact) or T2 (numerical)"; B §6 check 3 (`6a2b59cb-F07_VS_BLIND_TWOFACE_ADJUDICATION.md:193`) repeats tier T1. The corpus evidence for both values is float, not exact. `_v17_vac_cluster` (ENGINE_O4_hodge_v10a7_marked_linked_scalar.py:5383-5397) runs on a float vacuum vector (`_V17_VAC_VEC={_V17_VAC_ST:1.0}`, :5352) through a resolvent that divides in float (`out[sig]={st:float(c)/den ...}`, :5375). The values enter only as gates: :5433 `abs(z['e4']-float(_Q17(-54321,837760)))<V10A7_TOL` and :5434 the same form for omega4, with `V10A7_TOL = float(os.environ.get('V10A7_TOL','3e-9'))` at :5192 — an env-overridable float tolerance. The coplanar/perp agreement gate (:5436) is likewise float. Measured values (15 hour RUN.txt:7798-7805): e4 = -0.06484076585179532 vs float(-54321/837760) = -0.06484076585179527, |diff| 5.55e-17 = 4 ulps; omega4 = -0.0039032658517952346 vs float(-327/83776) = -0.0039032658517952636, |diff| 2.91e-17 = 67 ulps. Per CLAUDE.md's tier table that is T2. The only exact statement available is the rearrangement Fraction(-54321,837760) - 2*Fraction(-39,1280) == Fraction(-327,83776) (I recomputed: True), which is a definitional identity once both inputs are literals. No exact route exists elsewhere either: v10a.21r hardcodes the value — ENGINE_O4_hodge_v10a21r_adjudicator_only_same_kernel.py:359 `VPAIR=_XQ(-327,83776)` — it does not derive it. Stronger than the finding states: neither 54321 nor 83776 appears anywhere in /home/user/WORKHOUSE/src/, /ledger/ or /tests/, so in this repo both values are T3; and B §6's "runnable check" `f07_twoface_adjudication_check.py` is absent from certificate bundle E, so its tier labels are asserted, not shipped.
> 
> (ii) ROUTE COUNT — CONFIRMED. B §3:100-106 says "Verified two ways in the corpus:" and lists as the second way the disconnected-spectator zero. That gate is on a different configuration: :5439 `_far=next(f for f in range(P) if f!=_vac_seed and f not in _V17_NEIGH[_vac_seed])` — a non-adjacent face whose omega4 must vanish by factorization; measured +0.000e+00 (15 hour RUN.txt:7807). It yields no value for the connected pair and is a null control, not a second route to -327/83776. The genuine second instantiation is coplanar vs perpendicular (44 and 80 embeddings, :7810), which returned bit-identical floats through the same engine — one measurement apparatus on two geometries.
> 
> (iii) THE FINDING'S OWN REPLACEMENT IS WRONG — strike it. The finding asserts "the corpus's real second constraint ... is the exact closure 13*V1 + 124*VPAIR = V_link, which pins VPAIR given V_link, V1 and the integer counts." The arithmetic is right (I recomputed 13*Fraction(-39,1280) + 124*Fraction(-327,83776) == Fraction(-1474623,1675520), True) but the inference is not: V_link is nowhere independently established, it is *constructed from* V1 and VPAIR in both engines. v10a.7:5462-5464 builds `V4_LINKED_MARKED = len(_single_emb)*_v1['e4'] + sum(n*_vpair[cls]['linked_e4'])` and then float-gates it against -1474623/1675520 at V10A7_TOL. v10a.21r:357-371 builds `V_MIN` by summing the literals V1=_XQ(-39,1280) and VPAIR=_XQ(-327,83776) over embeddings and exact-gates the sum — so B §3:113 "exact sum gated: v10a.21r V_MIN == -1474623/1675520" is an exact check on the embedding counts (13 singles, 44+80=124 pairs) given the literals, not a constraint on VPAIR. The implication runs (V1, VPAIR, counts) -> V_link only; it is the same tautology the finding correctly objects to in (i).
> 
> Correct count: one originating float measurement (v10a.7 `_v17_vac_cluster`, instantiated on two adjacent-pair geometries, agreeing bit-for-bit), plus one exact rearrangement identity, plus one exact count-closure that tests the embedding counts rather than the value. Zero independent exact determinations of -54321/837760 or -327/83776. Correct tier for A §2 row 4 and B §6 check 3 is T2, not T1.
> 
> Note: the adjacent claim A §2 row 5 / B §6 check 4 ("V_link = -1474623/1675520") is separately already qualified in this repo — src/workhouse/invariants.py:403-418 (C20) records that the decimal the corpus prints, -0.8800987156226097 (15 hour RUN.txt:7813), is the float-reconstruction LINKED_VACUUM_4_ARTIFACT = -521965902/593076541, ~31 ulps from the exact gate value.

**Why it holds.** I reproduced both core sub-claims at the cited lines. (i) The two-face vacuum values are produced by a float engine (:5375 `float(c)/den`) and checked only by float gates at :5433-5434 against V10A7_TOL=3e-9 (:5192), with observed residuals of 4 and 67 ulps; the sole exact statement is the rearrangement, which is definitional once both inputs are literals, and v10a.21r:359 hardcodes VPAIR rather than deriving it. So T1 in A:60 and B:193 is an overstatement of exactly one tier. (ii) B:105-106 counts the disconnected-spectator gate (:5439-5444, a non-adjacent configuration whose omega4 is identically 0) as one of "two ways" of verifying the connected-pair value; it produces no such value. The finding is therefore right on substance and severity. I refuted its third clause: the 13*V1+124*VPAIR=V_link closure is exact but is built from V1 and VPAIR in both engines (v10a.7:5462-5464 float, v10a.21r:357-371 from literals), so it constrains the embedding counts, not VPAIR — that clause must not enter the ledger.

---

### 5.39 `vlink-face-decomposition-already-exact-with-counts`

| | |
|---|---|
| **severity** | medium |
| **class** | `overstated` |
| **lane** | `corpus-value-search` |
| **verifier confidence** | high |
| **where** | A §2 row 5; B §3, §6 check 4 — vs corpus-import/programs/hodge_o4_adjudication/src/ENGINE_O4_hodge_v10a21r_adjudicator_only_same_kernel.py:358-369 |

**Claim as stated.** "linked-vacuum decomposition | T1 | V_link = −1474623/1675520, 1675520 = 1280·1309 = 83776·20" (A §2); "V_link = V1·(single embeddings) + VPAIR·(pairs) (exact sum gated: v10a.21r V_MIN == −1474623/1675520)" (B §3); check #4 `vlink_face_decomposable` asserts only "1675520 = 1280·1309 = 83776·20" (B §6).

**What is wrong (originating auditor).** The corpus already has the full decomposition WITH the integer embedding counts, and gates it exactly; the documents' check reduces it to a denominator-factorization fact, which is strictly weaker and carries no information about the decomposition. v10a.21r constructs V_MIN from the concrete embeddings using V1 = −39/1280 over `_single_emb` and VPAIR = −327/83776 over `_pairs` and gates the exact rational sum. v10a.7 computes the same sum numerically as 13·e4(1-face) + Σ_cls n_cls·ω4(cls) and gates the count 13. The counts are recorded as 13 one-face embeddings and 124 pairs (80 perpendicular, 44 coplanar). I verified exactly: 13·(−39/1280) + 124·(−327/83776) = −1474623/1675520. Nothing in the documents states 13, 124, 80 or 44.

**Evidence (originating auditor).** corpus-import/programs/hodge_o4_adjudication/src/ENGINE_O4_hodge_v10a21r_adjudicator_only_same_kernel.py:358-369 (V1=_XQ(-39,1280); VPAIR=_XQ(-327,83776); gate('v10a.21 concrete vacuum marked-support ledger sums to exact attached subtraction', _v21_sum(V_MIN)==_XQ(-1474623,1675520)) — exact `==`, T1). ENGINE_O4_hodge_v10a7_marked_linked_scalar.py:5460 gate count 13; :5466 gate V4_LINKED_MARKED. Counts stated in theory/superseded/MASTER_THEORY.md:568 "embeddings 13 (one-face) + 124 (pairs: 80 perp, 44 coplanar)". Also derived independently in corpus-import/records/transcripts/chat.txt:1774-1817 ("n_total = 810960/6540 = 124"). My check: Fraction(13)*Fraction(-39,1280)+Fraction(124)*Fraction(-327,83776) == Fraction(-1474623,1675520) → True.

**Verifier's corrected statement — authoritative.**

> HOLDS, with the evidence line trimmed of three overstatements.
> 
> THE DEFECT (reproduced). Document B:194 registers check #4 under the name `vlink_face_decomposable` at tier T1, but its entire asserted content is `1675520 = 1280·1309 = 83776·20`. Document A:61 titles the same row "linked-vacuum decomposition | T1" and carries only `V_link = -1474623/1675520` plus that same factorization. The name and row title promise a decomposition; the machine content is a fact about a single integer.
> 
> WHY IT IS STRICTLY WEAKER (my computation, not the auditor's). 1280 = 2^8*5, 83776 = 2^6*7*11*17, and lcm(1280, 83776) = 2^8*5*7*11*17 = 1675520. So "1675520 = 1280*1309 = 83776*20" is exactly the statement that 1675520 is the lcm of the two summand denominators. It is true of the number 1675520 alone: it holds for a*V1 + b*VPAIR for EVERY pair of integers (a,b), and indeed would hold if V_link had no face interpretation at all. It carries zero information about the decomposition.
> 
> WHAT THE EXACT IDENTITY GIVES INSTEAD. 13*(-39/1280) + 124*(-327/83776) = -1474623/1675520 exactly (verified in fractions.Fraction). Clearing denominators: 51051a + 6540b = 1474623, i.e. 17017a + 2180b = 491541 with gcd(17017,2180)=1, so the solution lattice steps by (+2180, -17017); since 124 < 17017 and 13 < 2180, (a,b) = (13,124) is the UNIQUE non-negative integer solution. The exact identity therefore pins both counts; the factorization pins neither.
> 
> CORPUS SOURCES (opened at the cited lines, all confirmed verbatim):
> - corpus-import/programs/hodge_o4_adjudication/src/ENGINE_O4_hodge_v10a21r_adjudicator_only_same_kernel.py:359-369 — V1=_XQ(-39,1280); VPAIR=_XQ(-327,83776); accumulation over `_single_emb` and `_pairs`; gate('v10a.21 concrete vacuum marked-support ledger sums to exact attached subtraction', _v21_sum(V_MIN)==_XQ(-1474623,1675520)) — exact `==`. Because _v21_sum sums values and all terms share a sign (no key collision or prune can cancel), this gate is arithmetically identical to 13*V1 + 124*VPAIR == V_link given |_single_emb|=13, |_pairs|=124.
> - ENGINE_O4_hodge_v10a7_marked_linked_scalar.py:5460 — gate('v10a.7 one-face vacuum embedding count is 13', len(_single_emb)==13), an exact integer gate.
> - ENGINE_O4_hodge_v10a7_marked_linked_scalar.py:5436 — gates coplanar and perpendicular pair linked_e4 agree, which is what licenses v10a.21r's single uniform VPAIR.
> - theory/superseded/MASTER_THEORY.md:568 — "embeddings 13 (one-face) + 124 (pairs: 80 perp, 44 coplanar)".
> 
> THREE CORRECTIONS to the candidate's evidence line, each of which weakens it but none fatally:
> (1) "gates it exactly / T1" overstates status here. v10a.21r is a same-kernel Colab resume and is NOT runnable in this repository — `_XQ` has no definition anywhere in corpus-import (I grepped .py, .md and all notebook cells). This is already on record at corpus-import/records/audits/08-rooted-adjudication.md:110, which names `_XQ`, `gate` and `V10A7_PROGRESS` as prerequisites the preflight omits. Under CLAUDE.md the script is therefore a T3 document, not a T1 check of this repo.
> (2) Only the count 13 is gated. 124 is merely printed (v10a7:5458, `'adjacent-pair embeddings:', dict(_pair_counts), 'total=', len(_pairs)`); 80 and 44 appear only in theory/superseded/MASTER_THEORY.md:568, which CLAUDE.md forbids reading as current.
> (3) corpus-import/records/transcripts/chat.txt:1774-1817 is NOT an independent derivation of 124. It back-solves it from the gate value: "6540*n_total = 1474623 - 663663 = 810960 => n_total = 810960/6540 = 124". Citing it as independent is precisely the AGENTS.md "repetition is not independence" failure.
> 
> DOCUMENTS CHECKED. Grep of all four uploaded documents for the embedding counts returns nothing: no 124, no 80, no 44, and every "13" is either the numerator of -13/896 (A:57, B:69-70,76,79,81, D:36,49) or the "degree-6 fit on 13 points" (B:168, D:91). The candidate's "nothing in the documents states 13, 124, 80 or 44" is accurate.
> 
> NOT ALREADY RECORDED IN THIS REPO. src/workhouse/constants.py:430 holds LINKED_VACUUM_4 = Rational(-1474623, 1675520) as a bare value; src/workhouse/invariants.py:401-418 has only the C20 check (exact gate value vs the float-reconstruction -521965902/593076541, 3.0e-15 = 31 ulps); ledger/contradictions.yaml:242-262 records C20, which concerns the printed decimal, not the decomposition; corpus-import/records/audits/08-rooted-adjudication.md:45 states the V1/VPAIR attachment structure but gives no counts. Nothing in the verification layer reconstructs V_link from the counts.
> 
> CONSEQUENCE. The documents' T1 label is not false — `1675520 = 1280*1309 = 83776*20` is true — but the check is misnamed for what it verifies, and the corpus's own record already contains the stronger exact statement. The one-line replacement, entirely inside this repo's exact-rational discipline: assert Rational(13)*Rational(-39,1280) + Rational(124)*Rational(-327,83776) == K.LINKED_VACUUM_4, with the two counts sourced from the v10a.7:5460 gate (13, gated) and flagged as ungated-but-uniquely-determined (124, since it is the unique non-negative completion). Severity medium is right: overstated naming on a T1 row, in a repo whose one principle is that status is computed rather than asserted.

**Why it holds.** I re-opened every cited source rather than trusting the evidence line. The v10a.21r gate at :359-369 is verbatim as claimed (exact `==` on -1474623/1675520, built from V1 over `_single_emb` and VPAIR over `_pairs`); v10a7:5460 gates the count 13; MASTER_THEORY.md:568 gives 13 + 124 (80 perp, 44 coplanar). I recomputed 13*(-39/1280) + 124*(-327/83776) = -1474623/1675520 in Fraction (True). I then went past the auditor: 1675520 = lcm(1280, 83776) exactly, so the documents' factorization holds for every integer pair (a,b) and carries no decomposition content, whereas the exact identity has (13,124) as its unique non-negative integer solution (17017a+2180b=491541, gcd 1, lattice step 2180/-17017). Grepping all four documents confirms none states 13-as-count, 124, 80 or 44. I checked the repo does not already record this: constants.py:430 is a bare value, invariants.py:401-418 is the unrelated C20 ulp check, ledger C20 is about the decimal, and audit 08:45 gives the structure without counts. Three evidence-line overstatements needed correcting and are folded into the corrected statement: v10a.21r cannot run here (`_XQ` undefined, already recorded at audit 08:110, so it is T3 not T1); 124/80/44 are never gated; and chat.txt back-solves 124 from the gate rather than deriving it independently. Those trim the finding's force but do not touch its core, which is a name-versus-content mismatch on a T1-labeled check that I reproduced directly.

---

### 5.40 `artifact-blind-table-sums-to-oracle-overstated`

| | |
|---|---|
| **severity** | medium |
| **class** | `artifact-wrong` |
| **lane** | `hamer-circularity` |
| **verifier confidence** | high |
| **where** | artifact A line 62; artifact B line 195; corpus-import/records/transcripts/15 hour RUN.txt:7678-7680, 10620-10626 |

**Claim as stated.** A: "| blind table closes | T2 | Σ per-size `c4` = oracle `−0.7751458630189` (`:10626`) |"; B: "| 5 | `blind_table_sums_to_oracle` | T2 | Σ size-c4 = `−0.775145863…` (`:10626`) |"

**What is wrong (originating auditor).** Stated as an unqualified equality to 13 printed digits, it is false. The six printed per-size c4 values sum to -0.7751458630184425; the oracle TOTAL at :10626 is -0.7751458630189173. Gap 4.748e-13 = 4277 ulps; the two differ in the 12th significant figure. The claim is defensible only with a tolerance, and the right one is the printing budget: the sum of the six entries' 12-significant-figure half-ulps is 1.550e-12, so 4.7e-13 is comfortably inside it. There is also a structural reason exact equality was never available: the source accumulates `totals+=x` in cluster iteration order while `bysize[len(C)]+=x` accumulates per size (15 hour RUN.txt:7678), so the two are different float summation orders of the same terms even before printing. B's version ("−0.775145863…", truncated) is the safer wording; A's 13-digit form is the one that is wrong.

**Evidence (originating auditor).** printed six-row sum = -0.7751458630184425; oracle = -0.7751458630189173; difference 4.748423876321795e-13 = 4277 ulps. Σ of per-entry 12-sf half-ulps = 1.550e-12. Printing format confirmed as 12 significant figures by the source itself: `:+.12g` at 15 hour RUN.txt:7680.

**Verifier's corrected statement — authoritative.**

> Artifact A line 62 states the T2 row `Σ per-size c4 = oracle −0.7751458630189 (:10626)` with no tolerance, quoting 13 significant figures. Reproduced from primary source: the six per-size `c4` values printed at `corpus-import/records/transcripts/15 hour RUN.txt:10620-10625` sum, in printed order, to -0.7751458630184425, while the oracle TOTAL at `:10626` is -0.7751458630189173. Difference 4.748423876321795e-13 = 4277 ulps (ulp = 1.1102230246251565e-16); the two diverge in the 12th significant figure, so A's 13th digit (…189 vs …184) is not supported by the cited evidence. CLAUDE.md requires a T2 detail line to carry its tolerance; A's carries none. The correct tolerance is the printing budget: the table is printed at 12 significant figures (`:+.12g`, `15 hour RUN.txt:7680`) while the TOTAL is printed at full repr (`:7681`), and the sum of the six entries' 12-sf half-ulps is 1.5500e-12, comfortably covering 4.75e-13. The gap is print truncation, not arithmetic: 3.619e-13 of it (76%) is attributable to just two exactly-known entries — size 1 printed +0.0159598214286 vs 143/8960 (+2.857e-14) and size 6 printed -0.208333333333 vs -5/24 (+3.333e-13) — with the residual 1.129e-13 inside the 5e-13 half-ulps of sizes 2 and 3. CORRECTION to the original finding: its secondary "structural reason" (that `totals+=x` accumulates in cluster order while `bysize[len(C)]+=x` accumulates per size, `15 hour RUN.txt:7678`) is a true code fact but is NOT load-bearing here — with 203 concrete clusters (`:9174`) that reassociation term is a ~1e-14-scale effect, an order of magnitude below the observed gap, and must not be cited as its cause. The underlying claim is true by construction (`:7678` accumulates identical terms into both); only A's stated precision is wrong. B line 195's truncated `−0.775145863…` (9 sf) is correct and should stand. Severity is a precision/labeling defect, not a refutation: fix is to restate A:62 as `Σ per-size c4 = oracle to 12 sf, |Δ| = 4.75e-13 < 1.55e-12 print budget`. Not previously recorded: `ledger/contradictions.yaml:51` and `literature/index.yaml:495-496` record the unrelated M_GAMMA_4_NUM vs 8·a_4 coincidence (5.17e-13), and nothing in the repo sums this table.

**Why it holds.** I re-opened every cited line myself rather than trusting the evidence line. `15 hour RUN.txt:7680` confirms `:+.12g` 12-sf printing for the per-size rows and `:7681` shows the TOTAL printed at bare repr, so the two are printed at different precisions — the asymmetry neither artifact mentions. Recomputing the six printed values with fractions.Fraction and with float summation in printed order both give -0.7751458630184425 against the oracle -0.7751458630189173: gap 4.748423876321795e-13, 4277 ulps by bit-pattern subtraction. Half-ulp budget 1.5500e-12 reproduces. A:62 and B:195 read exactly as quoted, and grepping both artifacts for `tolerance`/`.12g`/`printed precision` shows no tolerance is stated for this check anywhere (B:73 uses "full printed precision" only for the size-1 check). I attempted to refute on three fronts and each failed: (1) the T2 tag does not rescue it, because CLAUDE.md defines T2 as agreement "within a stated tolerance, tolerance in the detail line" and A states none; (2) the artifacts' own "printed-precision" convention does not rescue it either, since the sum only supports 12 sf while A quotes 13; (3) the repo does not already record it — the nearby 5.17e-13 entries concern M_GAMMA_4_NUM vs 8·a_4, a different pair, and no repo file sums this table (grep for 403971702978/178800648136/bysize outside corpus-import and .venv is empty). Where I did push back successfully is on the finding's own reasoning: I attributed 76% of the gap to two exact rationals truncated at 12 sf (143/8960 and -5/24), which shows the summation-order argument is superfluous and, at 203 clusters (`:9174`), roughly an order of magnitude too small to be the cause — so that part of the finding is demoted rather than carried into the ledger. Separately, the orchestrator's "established" claim that the printed table sums to 8*HAMER_A4_NUM to the last float bit does not reproduce: -0.7751458630184425 vs -0.7751458630184 are 4.241e-14 / 382 ulps apart.

---

### 5.41 `hamer-tolerance-is-fitted-not-derived`

| | |
|---|---|
| **severity** | medium |
| **class** | `overstated` |
| **lane** | `hamer-circularity` |
| **verifier confidence** | medium |
| **where** | src/workhouse/constants.py:264; src/workhouse/invariants.py:388-394, 1299-1316; corpus-import/records/transcripts/15 hour RUN.txt:10641-10648 |

**Claim as stated.** src/workhouse/constants.py:264 HAMER_TOLERANCE = 5.3e-13, used as the bound in invariants.py:391 and :1308

**What is wrong (originating auditor).** The bound is set 2.5% above the observed gap rather than derived from an error budget, and it silently absorbs a real fact: the agreement EXCEEDS the paper's own printed precision. a_4's 12th significant figure sits at 1e-13, so its printed half-ulp is 5e-14; times the bridge factor 8 that is 4.0e-13. The observed gap is 5.173e-13 = 1.293x that bound. The sibling checks for n=2 and n=3 justify their bounds explicitly as 'printed half-ulp x bridge factor with margin' (invariants.py:1335-1339, :1358-1361); the a_4 check does not, and cannot. The missing term is the run's own float error — which is measurable from the same run against quantities with known exact values, and which fully accounts for the excess. The honest budget is print (4.0e-13) + run (~4.6e-13) ~ 8.6e-13, under which the agreement passes with real margin and for a stated reason. As written, the number reads as a tolerance chosen to fit.

**Evidence (originating auditor).** gap = |8*a_4 - M_GAMMA_4_NUM| = 5.172529071728604e-13; printed half-ulp of a_4 = 5e-14, x8 = 4.0e-13; ratio 1.293. Run's own accuracy on knowns (15 hour RUN.txt:10641-10648): A = 0.104166666666728 vs 5/48 → abs 6.133e-14, rel 5.887e-13; alpha = 0.41666666666691 vs 5/12 → abs 2.433e-13, rel 5.839e-13; D = 2.232e-13 where the exact value is 0; fifth_residual_max 2.526e-13; gamma_spread 2.253e-13. m_4 gap rel = 6.673e-13 — the same order as the run's demonstrated relative error on 5/48 and 5/12.

**Verifier's corrected statement — authoritative.**

> NARROWED AND PARTLY CORRECTED. Reproduced core: src/workhouse/constants.py:264 sets HAMER_TOLERANCE = 5.3e-13 with no derivation recorded anywhere in the repository (grep of all .py/.md/.yaml outside corpus-import/ finds only the definition, the two uses, and prose quoting "5.2e-13" in ledger/contradictions.yaml:52, CERTIFIED.md:501, docs/decisions/0002:53; the repo is a single squashed commit aa835a1, so no history explains it). Two live checks bind on it: src/workhouse/invariants.py:388-394 and :1299-1316.
> 
> Numbers I recomputed myself: gap = |8*HAMER_A4_NUM - M_GAMMA_4_NUM| = 5.172529071728604e-13 = 4659 ulps of M_GAMMA_4_NUM (rel 6.673e-13). HAMER_TOLERANCE/gap = 1.02464, i.e. 2.46% headroom - the check flips to FAIL on any drift of M_GAMMA_4_NUM past 1.27e-14 (114 ulps). Hamer prints a_4 as -0.968932328773 E-1 (per invariants.py:1289-1290), 12 significant figures, so printed half-ulp = 5e-14 and print-only budget = 5e-14 * 8 = 4.0e-13; gap/print = 1.29313.
> 
> The sharpest reproducible fact, stronger than the auditor stated it: across all five Hamer bridge comparisons in the repo, gap/print-budget = 0.994 (MA n=2, invariants.py:1331/1335), 0.557 (MA n=3, :1332/1336), 0.784 (MS n=2, :1355/1358), 0.681 (MS n=3, :1356/1359), and 1.293 (MA n=4, :390 and :1299). a_4 is the ONLY comparison whose gap exceeds its paper-print error budget, and the structural reason is unstated in the repo: the other four target exact corpus rationals (11/306, -109151/249696, -217/1020, -54049/520200), so paper rounding is their only error source, whereas a_4's target M_GAMMA_4_NUM = -0.7751458630189173 is a float produced by the blind numerical run and carries a second error term. That term is measurable in the same run block (corpus-import/records/transcripts/15 hour RUN.txt:10641-10648, confirmed verbatim: A = +0.104166666666728 vs 5/48 -> abs 6.133e-14, rel 5.887e-13; alpha = +0.41666666666691 vs 5/12 -> abs 2.433e-13, rel 5.839e-13; D = +2.232e-13 where the exact value is 0). Scaled onto |m_Gamma^(4)| = 0.7751, rel 5.887e-13 gives 4.564e-13 absolute, which comfortably covers the 1.17e-13 by which the gap overshoots the print budget.
> 
> Parts of finding #86 that DO NOT survive and must not go into the ledger as written:
> (a) "the agreement EXCEEDS the paper's own printed precision" is backwards. The disagreement exceeds the print-only budget; the agreement is worse than print precision alone predicts, not better.
> (b) "cannot" be justified as printed half-ulp x bridge factor with margin is false. 8.0e-13 = print budget x 2 is exactly the margin the MA n=2 and MS n=2 siblings use (bound/print = 2.000 for both), and the observed gap would sit at 0.65 of it. What is true is only that the current 5.3e-13 is not any natural multiple of 4.0e-13 (it is 1.325x) while sitting 1.0246x the observed gap.
> (c) the citation "invariants.py:1358-1361" does not support what it is cited for. Only invariants.py:1337 states a recipe ("bound 3e-12 = printed half-ulp x 4 with margin"), backed by the comment at :1327-1329. The MS check's detail at :1358-1361 prints "(bound 2e-12)" and "(bound 5e-13)" bare with no derivation, so an unjustified bound is not unique to the a_4 check.
> (d) "silently absorbs" overstates: both detail strings (:391-394, :1310-1314) print the measured gap, so nothing numeric is hidden.
> (e) the ~4.6e-13 run term is a two-point calibration against 5/48 and 5/12 from one run, not an error analysis; "the honest budget is 8.6e-13" is a plausible estimate, not a derived bound.
> 
> Severity is LOW, not medium: this is a derivation/documentation gap in a tolerance constant plus one unstated physical fact, not a numeric error. No check currently fails. Given CLAUDE.md's "never widen a tolerance", the prescription (raise 5.3e-13 -> 8.6e-13) should not be acted on; the recordable action is to state in constants.py:264 and in the two check details that the a_4 comparison alone carries a second error term (the blind run's own float error, calibrated in RUN.txt:10641-10648 at rel ~5.9e-13) and that this is why its gap exceeds the 4.0e-13 print-only budget while its four siblings do not. Note separately (outside this finding's scope) that invariants.py:392-393 still calls a_4 "an unverified notebook transcription", a caveat invariants.py:1285-1292 records as retired on 2026-08-21.

**Why it holds.** I independently reopened every cited file and recomputed every number. All six of the auditor's quantitative claims check out exactly: gap 5.172529071728604e-13, tol/gap 1.02464, print budget 4.0e-13, ratio 1.29313, and the five RUN.txt run-accuracy figures at the exact cited lines 10641-10648. Grep over the whole repo confirms no derivation of 5.3e-13 exists, and the single-commit history offers none. I also strengthened the finding by computing gap/print for all five Hamer bridge comparisons, which shows a_4 is the unique outlier for a structural reason (its target is a run float, not an exact rational). However four framing claims fail on re-reading the sources: the "exceeds printed precision" phrasing is inverted, the "cannot be print-justified" claim is refuted by the siblings' own 2x-print recipe, the cited sibling justification at :1358-1361 is not there (the MS bounds are bare), and "silently absorbs" is contradicted by the detail strings that print the gap. So the finding holds only in the narrowed form above, at low severity, and the proposed remedy (widening the tolerance) should be replaced by recording the second error term.

---

### 5.42 `two-live-checks-contradict-on-provenance`

| | |
|---|---|
| **severity** | medium |
| **class** | `repo-wrong-or-stale` |
| **lane** | `hamer-circularity` |
| **verifier confidence** | high |
| **where** | src/workhouse/invariants.py:388-394 vs :1279-1316; index/claims.jsonl:149 |

**Claim as stated.** src/workhouse/invariants.py:391-393 detail string: "a_4 is an unverified notebook transcription, so this is a normalization cross-check, not primary-source proof"

**What is wrong (originating auditor).** This is stale and directly contradicts the other live check on the same constant, which states at invariants.py:1285-1292 that "the caveat is retired" because the primary was obtained and pinned on 2026-08-21. Both checks are in `make verify` and both PASS, so a reader of the verify output is told two incompatible things about the provenance of HAMER_A4_NUM in the same run. The generated catalogue is stale in the same direction: index/claims.jsonl:149 records CONST:Hamer a_4 as tier 3, status "conditional", statement "notebook transcription; primary table not hashed".

**Evidence (originating auditor).** Ran both. invariants.py:388 → PASS T2 '|diff| = 5.17e-13; a_4 is an unverified notebook transcription, so this is a normalization cross-check, not primary-source proof'. invariants.py:1279 → PASS T2 '...the copy read is pinned as sha256 96b3ec0f6e2da458…'. index/claims.jsonl:149 tier 3 / conditional.

**Verifier's corrected statement — authoritative.**

> CONFIRMED, with two corrections and two additions to the auditor's version.
> 
> REPRODUCED. `make verify` (Makefile:22-23 -> `.venv/bin/workhouse verify`) runs both suites and prints two incompatible provenance statements about the same constant, HAMER_A4_NUM = -0.0968932328773 (src/workhouse/constants.py:239):
> 
> - src/workhouse/invariants.py:388-394, suite `dispute`, T2, PASS: "|diff| = 5.17e-13; a_4 is an unverified notebook transcription, so this is a normalization cross-check, not primary-source proof"
> - src/workhouse/invariants.py:1279-1316, suite `published`, T2, PASS: "...gap 5.17e-13 (bound 5.3e-13); the copy read is pinned as sha256 96b3ec0f6e2da458..., a_4 equals Table 1's M_A order-4 entry...", with the in-code comment at :1285-1292 stating "The caveat is retired, not forgotten".
> 
> Both ran clean and both PASS. The arithmetic is identical in the two checks and is correct: 8*(-0.0968932328773) = -0.7751458630184 vs M_GAMMA_4_NUM = -0.7751458630189173, gap 5.172529071728604e-13 = 4659 ulps of m_Gamma^(4), against the shared bound K.HAMER_TOLERANCE = 5.3e-13 (constants.py:264). No number disagrees; only the provenance prose does.
> 
> The repo's live ledger sides with the second check: literature/index.yaml:454-497 carries `source_sha256: 96b3ec0f...`, and the `bears_on: HAMER_A4_NUM / supplies-value` edge is `status: verified` with detail "Verified digit for digit against Table 1 (M_A column, order 4) of the pinned copy". So invariants.py:392-393 is the stale side.
> 
> MECHANISM (git). Commit 75f13c62 "Pin the Hamer 1989 primary..." (2026-08-21 15:06) rewrote the *published* check — its old title was literally "the strongest external check is a transcription, and says so" — and its message asserts "The check that used to assert its own caveat now asserts the pin instead". That is inaccurate: `git blame -L 386,394 src/workhouse/invariants.py` shows lines 391-394 still belong to aa835a1 (2026-08-21 01:32), untouched by the pinning commit. A second, independent caveat-asserting check was left behind.
> 
> CORRECTION 1 to the auditor's claim: index/claims.jsonl is NOT stale. src/workhouse/claims.py:198,206-207 builds each CONST row from `constant.note / .status / .evidence`, so claims.jsonl:149 (tier 3, "conditional", "notebook transcription; primary table not hashed") is a faithful regeneration of a stale SOURCE — src/workhouse/constants.py:647. `make catalogue` will not fix it; constants.py:647 must change first.
> 
> ADDITION 1 (missed by the auditor): the same file contradicts itself. constants.py:229-238 (added by 75f13c62) reads "Table 1 of the digest-pinned primary (sha256 in literature/index.yaml)... Read 2026-08-21 and verified against the rendered page image, not OCR", while constants.py:647 (untouched, from aa835a1) still reads "notebook transcription; primary table not hashed" — 400 lines apart in one module.
> 
> ADDITION 2 (missed by the auditor): index/claims.jsonl:29, the CHK row for the dispute check, propagates the retired caveat verbatim into the generated catalogue's `detail` field.
> 
> CORRECTION 2 on scope: the same wording in theory/GLUEBALL_DETAILED_FORMULA_2026-08-20_v3.1.md:95 and theory/superseded/MASTER_THEORY.md:85,413,425,616,762 is NOT a defect — theory/ is immutable evidence and correctly records what was believed before 2026-08-21.
> 
> Not recorded anywhere: no entry in ledger/contradictions.yaml, ledger/gaps.yaml, or docs/decisions/ mentions the surviving caveat. FRONTIER.md and CERTIFIED.md do not print check detail strings, so the contradiction is invisible there and surfaces only in `make verify` output and index/claims.jsonl.
> 
> SEVERITY: this is a bookkeeping/provenance-prose defect, not a numerical one — no value, tolerance, tier, or gap is wrong. Medium is defensible but at the low end of medium. The one substantive residue worth keeping is that neither check is a machine check of the primary: literature/index.yaml:461 records `fulltext: null` (publisher copyright, PDF not stored), so the digest pins a copy this repository cannot re-read, and invariants.py:1300-1308 verifies only that the ledger records a 64-char digest and a 'verified' edge — not that the reading occurred. Any repair should therefore replace "unverified notebook transcription" with the accurate limitation (primary read and digest-pinned 2026-08-21, copy not stored here, so the digit-for-digit reading is not re-checkable in-repo) rather than simply deleting the caveat.
> 
> MINIMAL REPAIR SET: src/workhouse/invariants.py:392-393; src/workhouse/constants.py:647; then `make catalogue` to refresh index/claims.jsonl:29 and :149.

**Why it holds.** I opened both cited line ranges myself and ran both checks through the repo's own CLI: invariants.py:388 PASSes printing "a_4 is an unverified notebook transcription... not primary-source proof", and invariants.py:1279 PASSes printing that the copy is pinned as sha256 96b3ec0f6e2da458 and that its comment at :1285-1292 declares "The caveat is retired". Both are reached by `make verify` (Makefile:22-23), so one run tells a reader both things. I recomputed the arithmetic (8*a_4 - m_Gamma^(4) = 5.172529071728604e-13 = 4659 ulps, bound 5.3e-13); it is identical and correct in both checks, so the conflict is purely about provenance. literature/index.yaml:454-497 pins the primary and marks the supplies-value edge 'verified', settling which side is stale. git blame proves the mechanism: commit 75f13c62 rewrote the published check (prior title "the strongest external check is a transcription, and says so") and its message claims the caveat-asserting check was converted, but blame shows invariants.py:391-394 still belongs to the earlier commit aa835a1 and was never touched. I found no record of this in ledger/contradictions.yaml, ledger/gaps.yaml, or docs/decisions/. I corrected the auditor on the catalogue: src/workhouse/claims.py:198,206-207 derives CONST rows straight from constants.py's Constant note/status/evidence, so claims.jsonl:149 is a faithful regeneration of the stale constants.py:647 rather than a stale artifact — the auditor also missed constants.py:647 itself (which contradicts constants.py:229-238 in the same file) and claims.jsonl:29.

---

### 5.43 `oracle-free-row-is-untiered-and-contested`

| | |
|---|---|
| **severity** | medium |
| **class** | `overstated` |
| **lane** | `invariants-tests` |
| **verifier confidence** | high |
| **where** | artifact A §2 (header and row 8); repo src/workhouse/invariants.py:631-651, :655-663 |

**Claim as stated.** A §2 header: "Every row is T1 (exact) or T2 (numerical), reproducible via the check." Row 8: "F07 oracle-free | — | two independent scanners, zero leakage (B §2, C §3)"

**What is wrong (originating auditor).** Internal contradiction: the header promises every row is T1 or T2, and row 8's tier is literally '—'. Worse, it sits in a table titled 'The certified spine (what is machine-verified)'. Substantively, this repository already certifies two blind spots in the corpus's own blindness machinery, so 'zero leakage' is not a conclusion this repo supports: the target-blindness scan misses the two scalar-determining targets, and it reads only the engine file. The artifacts' own two scanners live in external trees and are unverifiable here.

**Evidence (originating auditor).** src/workhouse/invariants.py:631-651 'FINDING: the target-blindness scan cannot see two scalar-determining targets' (T1, PASS) — uncovered targets include delta_gamma and hamer_8a4; src/workhouse/invariants.py:655-663 'FINDING: the contamination scan reads only the engine file' (T1, PASS). Mirrored in ledger/gaps.yaml:116-126.

**Verifier's corrected statement — authoritative.**

> HOLDS, with the auditor's repo-side evidence corrected as misdirected.
> 
> (1) Internal contradiction — CONFIRMED literally. Artifact A titles the table "The certified spine (what is machine-verified)" (A:51) and asserts "Every row is T1 (exact) or T2 (numerical), reproducible via the check." (A:53). The table has exactly 8 data rows (A:57-64) with tiers T1,T2,T1,T1,T1,T2,T1,—. Row 8 (A:64, "F07 oracle-free | — | two independent scanners, zero leakage (B §2, C §3)") is the single row whose tier cell is literally an em dash (U+2014). One of eight rows falsifies the header, and it is the row placed under a "machine-verified" banner with no tier at all — exactly the silent-promotion failure AGENTS.md forbids ("Never move a result up a ladder silently").
> 
> (2) "zero leakage" is not supported here — but NOT for the reason the auditor gave. The auditor's cited evidence is real and I reproduced it: src/workhouse/invariants.py:631-651 "FINDING: the target-blindness scan cannot see two scalar-determining targets" (tier 1, PASS; uncovered = ['A_target','alpha_target','delta_gamma','hamer_8a4','quarantined_shortcut'], of which delta_gamma and hamer_8a4 are scalar-determining) and src/workhouse/invariants.py:653-663 "FINDING: the contamination scan reads only the engine file" (tier 1, PASS). Auditor cited ":655-663"; the decorator block starts at 653. Mirrored at ledger/gaps.yaml:113-125 under gap G3 (auditor cited :116-126, off by ~3). HOWEVER both findings concern settlement/mce_adjudication_harness.py, whose CONTAMINATION_STRINGS digit-string scan reads the MCE engine source (harness:106-107, `src = open(engine, errors="ignore").read()`, GLUE3 v3.1 §18.1 protocol). That is a different pipeline from the artifacts' W2/R2 exact-Haar scan, so those two findings do not directly falsify A:64. Citing them as if they did is an analogy, not a derivation.
> 
> The conclusion survives on three directly checkable grounds instead:
>  (a) A:64's citation "(B §2, C §3)" uses A's OWN document lettering (A:17-27), where A's "B" = W2_R2_ORACLE_LINEAGE_TRACE (the orchestrator's artifact C) and A's "C" = ORACLE_COUNTERFACTUAL_AUDIT, which is NOT among the five uploaded artifacts. Half the citation is unreadable here.
>  (b) The one readable half, artifact C:111-115, is a scoped SYMBOL-NAME search for `M4_ORACLE`, `ax_rest`, `local_shift`, `K4_mass`, `M4_SHORTCUT` across the primitive manifest, generator, contractor, package builder, verifier and independent-Haar sources — all rooted at work/rank3_order4_cubic_ledger/ and work/rank3_order4_exact_haar_run/, which are EXTERNAL to this repository and absent. UNVERIFIABLE HERE. It is a name scan, not a numeric-digit scan, so it does not exclude an engine carrying the value 7751458630189173, Hamer's 8*a_4, or delta_gamma under another name — the same class of hole the repo certifies for the settlement harness, though on a different scanner.
>  (c) Decisively, artifact C's own Bottom Line (C:15-27) contradicts "zero leakage": "The stronger independence claim is not established… This is a target-known exact replay of the v10a.7/v10a.20 scalar construction, not a prospectively blind derivation," and the package "pins historical v10a.20 census values and its source hash… those choices do not numerically encode the final scalar, but they do preserve design/provenance dependence on the same lineage." A records that caveat itself at A:22 ("the exact-Haar package is oracle-free but a *target-known* replay") and then drops it at A:64.
> 
> Also of note: the words "scan"/"scanner"/"leakage" appear in ZERO of artifacts B, C, D, E; "two independent scanners" is A's own coinage (A:64 is the only occurrence across all five artifacts).
> 
> Correct disposition: artifact A is WRONG (overstated) at A:53 + A:64. Recommended repair is to A only — either qualify the A:53 header, or restate row 8 as "T3 / unverifiable here: scoped name-search over external trees; C:15-27 records that the stronger independence claim is not established." No repo change is warranted, and the finding must NOT be written into the ledger citing invariants.py:631-663 as its basis, because those checks are about a different scan.

**Why it holds.** I re-read artifact A directly: A:51 table title, A:53 header, and a field-parse of rows A:57-64 showing exactly one em-dash tier cell at A:64 — the internal contradiction is literal and reproducible, not an artifact of the auditor's reading. I then opened the cited repo lines myself and ran the checks: both FINDING checks exist, are tier 1, and PASS, with the uncovered set including delta_gamma and hamer_8a4 as claimed (minor line drift: block starts at 653 not 655; gaps.yaml is 113-125 under G3, not 116-126). But reading settlement/mce_adjudication_harness.py:62-111 showed that scan targets the MCE engine source, a different pipeline from the artifacts' W2/R2 exact-Haar package, so the auditor's evidence does not support its own conclusion — I corrected that. The conclusion still holds on stronger primary grounds I verified: A's internal doc-set lettering (A:17-27) makes half of A:64's citation point at ORACLE_COUNTERFACTUAL_AUDIT, which was never uploaded; the readable half (C:111-115) is a name-only search over work/rank3_order4_cubic_ledger/, external and absent per the path mapping; and artifact C's own Bottom Line (C:15-27) explicitly states the stronger independence claim is NOT established, a caveat A itself records at A:22 and drops at A:64. Grep across all five artifacts found zero occurrences of "scan"/"scanner"/"leakage" outside A:64, confirming the phrase is unsupported by the documents it cites.

---

### 5.44 `b-section-3-factorization-wrong`

| | |
|---|---|
| **severity** | medium |
| **class** | `artifact-wrong` |
| **lane** | `ledger-graph` |
| **verifier confidence** | high |
| **where** | artifact B §3 line 99; the same block is cited in A §2 row 5 |

**Claim as stated.** B §3: "ω4 = e4(C) − 2·V1 = −327/83776 (irreducible pair weight; VPAIR) / 83776 = 2⁷·7·11·17² (in-scope, | QBOUND)"

**What is wrong (originating auditor).** The factorization is wrong. 2^7*7*11*17^2 = 2848384, not 83776. This string would be transcribed verbatim into any ledger entry recording the two-face vacuum, so it matters in the ledger lane and not only in numerics.

**Evidence (originating auditor).** sympy.factorint(83776) = {2:6, 7:1, 11:1, 17:1}, so 83776 = 2^6*7*11*17. The stated product is 2848384, off by a factor of 34. The value itself is right: Fraction(-54321,837760) - 2*Fraction(-39,1280) = Fraction(-327, 83776) exactly. Adjacent claims the document gets right: 1675520 = 1280*1309 = 83776*20 with 1309 = 7*11*17 (factorint(1675520) = {2:8,5:1,7:1,11:1,17:1}); 143 = 11*13; 8960 = 2^8*5*7. "| QBOUND" is unverifiable — grep for QBOUND across src/, ledger/, theory/, index/ returns nothing.

**Verifier's corrected statement — authoritative.**

> Artifact B, line 99 (/root/.claude/uploads/384fab32-8991-52ce-b2bf-4999d379e3f5/6a2b59cb-F07_VS_BLIND_TWOFACE_ADJUDICATION.md:99) prints "83776 = 2⁷·7·11·17²  (in-scope, | QBOUND)". The factorization is wrong: sympy.factorint(83776) = {2:6, 7:1, 11:1, 17:1}, i.e. 83776 = 2⁶·7·11·17. The printed product evaluates to 2848384 = 34·83776 (spurious factor 2·17). Likely provenance of the slip: 837760 = 2⁷·5·7·11·17, so the exponent 2⁷ is carried over from the line above (B:97); the 17² has no source in any quantity on the page.
> 
> The VALUE is correct and is not in question: Fraction(-54321,837760) - 2*Fraction(-39,1280) == Fraction(-327,83776) exactly, and -327/83776 is independently recorded in-repo as the pair weight at /home/user/WORKHOUSE/corpus-import/programs/hodge_o4_adjudication/src/ENGINE_O4_hodge_v10a21r_adjudicator_only_same_kernel.py:359 (VPAIR=_XQ(-327,83776)) and gated at .../ENGINE_O4_hodge_v10a7_marked_linked_scalar.py:5433-5434.
> 
> Three scope corrections to the finding as originally stated:
> 1. The claim "the same block is cited in A §2 row 5" is FALSE. A:60 (/root/.claude/uploads/.../52ebdfa7-RANK3_ORDER4_MASTER_RECORD.md:60) reprints only the values `e4(C) = −54321/837760`, `ω4 = −327/83776` and carries no factorization. The defect is confined to the single line B:99; it appears nowhere else in A, B, C or D (grep for 83776 across all four).
> 2. Adjacent factorizations in the same documents are correct and should not be swept in: B:112 `1675520 = 1280·1309 = 83776·20` with factorint(1675520)={2:8,5:1,7:1,11:1,17:1} and 1309=7·11·17; A:56 `143/8960 (11·13 / 2⁸·5·7)`.
> 3. The "| QBOUND" annotation is UNVERIFIABLE HERE, not undefined. QBOUND is a real corpus object — the prime-exponent LCM of the projector/Haar denominators, defined at /home/user/WORKHOUSE/corpus-import/records/audits/07-denominator-lift.md:35 (source lines 6382–6433 of the external notebook) — but no integer value for it is recorded in this repo (grep QBOUND over src/, ledger/, theory/, index/ returns nothing), so divisibility cannot be checked here.
> 
> Severity should be LOW rather than medium: 2848384 appears nowhere in /home/user/WORKHOUSE (grep over *.md/*.py/*.yaml/*.tex), so the wrong factorization is the artifact's own annotation, is not sourced from the corpus, and nothing downstream consumes it. It matters only insofar as the string would be transcribed verbatim into a ledger entry for the two-face vacuum.

**Why it holds.** Reproduced independently from primary sources. Read B:97-99 directly: the document does print "83776 = 2⁷·7·11·17²". Recomputed in python3/sympy: factorint(83776)={2:6,7:1,11:1,17:1} and 2**7*7*11*17**2 = 2848384 = 34*83776, so the printed prime decomposition is arithmetically false. Confirmed the underlying value is right (Fraction(-54321,837760)-2*Fraction(-39,1280) == -327/83776) and matches the in-repo engine constant. Also confirmed the finding's own "where" clause overstates reach — A:60 carries no factorization — and that its QBOUND evidence line searched too narrow a set of directories, since QBOUND is defined in corpus-import/records/audits/07-denominator-lift.md:35. The core defect nonetheless survives every check, is not an auditor artifact, and is not recorded anywhere in the repo.

---

### 5.45 `g3-oneliner-half-restates-half-is-new`

| | |
|---|---|
| **severity** | medium |
| **class** | `overstated` |
| **lane** | `ledger-graph` |
| **verifier confidence** | high |
| **where** | artifact A §6 item 3 lines 149-150; repo ledger/gaps.yaml:44-50,69,126-131, tests/test_ledger.py:65-68, tests/test_frontier.py:20, FRONTIER.md:137 |

**Claim as stated.** A §6 item 3: "`ledger/gaps.yaml` one-liner on G3: 'the F07-vs-blind split is localized to size ≥ 2; the decisive test is the exact W22-off two-face recomputation.'"

**What is wrong (originating auditor).** Split verdict. The first clause is genuinely new to the verification layer; the second restates protocol item 10 plus audit_findings bullet 3, narrowed and stripped of the recorded blocker. "Decisive" is also wrong for G3 as scoped — by G3's own detail a Gamma-point recomputation cannot settle what G3 must settle. Mechanically it cannot go where a "protocol one-liner" would go.

**Evidence (originating auditor).** New half: grep of ledger/, src/workhouse/*.py, index/, CERTIFIED.md, FRONTIER.md for `143/8960|8960|13/896|39/1280|83776|54321` returns zero matches — the one-face agreement and the size>=2 localization appear nowhere. Restated half: ledger/gaps.yaml:69 and :126-131. "Decisive" conflicts with ledger/gaps.yaml:44-50: G3 "must now settle is the off-axis coefficient C_shp, since ... Phi_C(0) = 0 makes Gamma-point data structurally incapable of constraining Delta_C." Mechanics: `protocol` is an 11-item freeze — tests/test_ledger.py:65-68 `assert len(g3["protocol"]) == 11`; simulation appending the one-liner gave len=12 -> FAIL while validate stayed CLEAN. Unpinned homes: `audit_findings` (no test constrains it) or `status`. Either way `make frontier` must rerun: G3's detail renders verbatim into FRONTIER.md:137 and tests/test_frontier.py:20 fails on staleness.

**Verifier's corrected statement — authoritative.**

> A §6 item 3 (lines 149-150) proposes writing onto `ledger/gaps.yaml` G3 the one-liner "the F07-vs-blind split is localized to size >= 2; the decisive test is the exact W22-off two-face recomputation." Split verdict, confirmed on three of four legs; the finding's own frontier-mechanics evidence is wrong and is corrected below.
> 
> (1) FIRST CLAUSE — genuinely new, but narrower than the finding states. Grep over the verification layer (`ledger/`, `src/workhouse/`, `index/`, `CERTIFIED.md`, `FRONTIER.md`) returns ZERO hits for each of `F07`, `143/8960`, `8960`, `13/896`, `39/1280`, `83776`, `54321`, `403971702978`, `multi-face`. So the one-face agreement (`-13/896 + 39/1280 = 143/8960`) and the size>=2 localization are absent. But the two branch VALUES are already registered under other names: `src/workhouse/constants.py:427` `QUARANTINED_SCALAR = Rational(-160506019419340168451, 14501180577204921600)` (= -11.068479463778765, checked at `invariants.py:399`) is A's `M4_SHORTCUT`/F07 branch, and `constants.py:430` `LINKED_VACUUM_4 = Rational(-1474623, 1675520)` is A's `V_link` (also `ledger/contradictions.yaml:248`, as C20's gate value). What is new is the LOCALIZATION, not the split.
> 
> (2) SECOND CLAUSE — restates existing material, and more of it than the finding cites. The W22 toggle is protocol item 10 at `ledger/gaps.yaml:69` ("W_22 order-schedule toggle across all 33 rooted classes"), its blocker is `ledger/gaps.yaml:126-131` ("protocol item 10 (W22 toggle) is hardcoded OPEN ... the protocol has no path to closure until the engine exposes the toggle"), and it is ALREADY a registered machine check — `src/workhouse/invariants.py:670-676`, `src/workhouse/settlement.py:131-139`, surfaced as `index/claims.jsonl:50`. A's one-liner drops the blocker. Partial mitigation the finding understates: A's narrowing (two faces specifically, the BLIND branch recomputed W22-off, compared against blind `size 2 c4 = -0.403971702978`, as a cheap standalone rather than the 609-cluster run) is additional content, and its blocker is arguably not the harness blocker, since Knob B does not run the mce engine. Call it "restated and narrowed", not "pure restatement".
> 
> (3) "DECISIVE" IS WRONG FOR G3 AS SCOPED — confirmed and strengthened. `ledger/gaps.yaml:47-50`: "what G3 must now settle is the off-axis coefficient C_shp, since the Gamma-point scalar is externally validated against Hamer and Phi_C(0) = 0 makes Gamma-point data structurally incapable of constraining Delta_C." The only open contradiction G3 resolves is C2 (`tests/test_ledger.py:26-31`), whose own notes read "Hamer's Gamma-point scalar pins Delta_Gamma and places NO constraint on Delta_C." A's proposed test is entirely Gamma-scalar: the blind per-size `c4` table sums to `M4_ORACLE` = the Gamma scalar, so `size 2 c4` is a Gamma-scalar contribution and yields no `C^(4)`. Protocol item 11 (`gaps.yaml:70`) requires "both m_Gamma^(4) and C^(4) from the same run"; the two-face recomputation delivers neither `C^(4)` nor `C_shp`. If landed in `detail`, the contradiction becomes visible in the generated view: `FRONTIER.md:137` renders G3's detail verbatim under the heading "## 7. The cheapest decisive test available now" (`src/workhouse/frontier.py:322-324`), two lines from the C_shp sentence.
> 
> (4) MECHANICS — reproduced, with one correction. `protocol` is an 11-item freeze: `tests/test_ledger.py:65-68` asserts `len(g3["protocol"]) == 11`. I appended the one-liner in memory: len -> 12, the assertion FAILS, and `ledger.validate(led)` returns CLEAN — so nothing but that one test catches it. CORRECTION to the finding: its claim "Either way `make frontier` must rerun" is FALSE. I rendered `frontier.render()` from a ledger with the one-liner (a) appended to `harness.audit_findings` and (b) added as a new top-level `status` key on G3; both outputs were BYTE-IDENTICAL to `FRONTIER.md` (baseline render also byte-identical, confirming the file is current). `frontier.py:291` renders `status` only for DISCHARGED gaps, and G3 is open with no `status` key today (keys: id, tier, state, title, detail, resolves, unblocks, leads, protocol, inventory_trap, harness). Only appending to `detail` changes the render — that alone forces `make frontier` (`tests/test_frontier.py:20`) and also `make catalogue`, since `index/claims.jsonl` carries G3's detail verbatim (`tests/test_search.py:151`).
> 
> Net: the one-liner should not be landed as worded. Its second clause is redundant with `gaps.yaml:69` + `:126-131` + `invariants.py:670-676` and mislabels a Gamma-scalar test as decisive for a gap whose stated remaining job is off-axis; its first clause is worth landing but belongs as a check (the exact `-13/896 + 39/1280 = 143/8960` identity, 143 = 11*13, 8960 = 2^8*5*7) rather than as ledger prose, and it must not go in `protocol`.

**Why it holds.** I opened every cited line myself and reproduced each mechanical claim rather than trusting the evidence line. gaps.yaml:44-50, :69, :126-131, tests/test_ledger.py:65-68, tests/test_frontier.py:20 and FRONTIER.md:137 are all exactly as quoted. The protocol-append simulation gave len 12 with the assertion failing and validate CLEAN, as claimed. The "decisive" conflict is real and is reinforced by C2's own notes, which the finding did not cite. Two corrections were needed: the branch values (QUARANTINED_SCALAR, LINKED_VACUUM_4) and the W22-toggle check already exist in the verification layer, so the new/restated halves are both narrower than stated; and the finding's "Either way make frontier must rerun" is refuted by direct rendering — audit_findings and status appends leave FRONTIER.md byte-identical. The core verdict survives; confidence is high on legs 1, 3 and 4 and medium only on how strongly leg 2's "restates" should be worded.

---

### 5.46 `83776-factorization`

| | |
|---|---|
| **severity** | medium |
| **class** | `artifact-wrong` |
| **lane** | `localization-argument` |
| **verifier confidence** | high |
| **where** | B §3 line 99 |

**Claim as stated.** B §3 line 99: "83776 = 2^7 * 7 * 11 * 17^2 (in-scope, | QBOUND)".

**What is wrong (originating auditor).** 83776 = 2^6 * 7 * 11 * 17. The printed product 2^7*7*11*17^2 equals 2,848,384, which is 34x too large. The error sits in the section B offers as "a clean input that IS available" and it carries a divisibility claim ("| QBOUND") whose stated prime support is wrong by one factor of 2 and one factor of 17.

**Evidence (originating auditor).** sympy.factorint(83776) = {2:6, 7:1, 11:1, 17:1}; 2**7*7*11*17**2 = 2848384; 2**6*7*11*17 = 83776. For contrast the neighbouring factorizations in the same documents are right: 837760 = 2^7*5*7*11*17, 1675520 = 2^8*5*7*11*17 = 1280*1309 = 83776*20, 8960 = 2^8*5*7, 143 = 11*13.

**Verifier's corrected statement — authoritative.**

> Document B, /root/.claude/uploads/384fab32-8991-52ce-b2bf-4999d379e3f5/6a2b59cb-F07_VS_BLIND_TWOFACE_ADJUDICATION.md:99, prints "83776 = 2⁷·7·11·17² (in-scope, | QBOUND)". The factorization is wrong: sympy.factorint(83776) = {2:6, 7:1, 11:1, 17:1}, i.e. 83776 = 2⁶·7·11·17 = 64·1309 with 1309 = 7·11·17. The printed product 2**7*7*11*17**2 = 2848384 = 34·83776, too large by a factor 2·17. The rational itself is correct and unaffected: Fraction(-54321,837760) - 2*Fraction(-39,1280) = -327/83776 exactly, and the repo carries the same value at /home/user/WORKHOUSE/corpus-import/programs/hodge_o4_adjudication/src/ENGINE_O4_hodge_v10a7_marked_linked_scalar.py:5434 and /home/user/WORKHOUSE/corpus-import/programs/hodge_o4_adjudication/src/ENGINE_O4_hodge_v10a21r_adjudicator_only_same_kernel.py:359 (VPAIR=_XQ(-327,83776)). The error also contradicts B's own line 112 ("1675520 = 1280·1309 = 83776·20", exact: 1675520/83776 = 20 remainder 0), which forces 83776 = 2⁶·7·11·17; the printed product would give 2848384·20 = 56967680. SCOPE LIMIT: the accompanying "| QBOUND" divisibility assertion is NOT falsified. With QBOUND = 62895057857493885215590055852113920000000 = 2^36·3^20·5^7·7·11·13·17^3·19·23·29·31·37·47 (scratchpad/cert/modular_haar_contractor.py:47, independent_replay_modular_crt.py:24, validate_modular_haar_ledger.py:14), both 83776 | QBOUND and the erroneous 2848384 | QBOUND hold, so the gate's conclusion survives and only the stated prime support is wrong. This is therefore a transcription/presentation defect in a line B offers as "a clean input that is available", not a broken numerical result. Not recorded anywhere in /home/user/WORKHOUSE (the repo states the value -327/83776 but never its factorization).

**Why it holds.** I opened B:99 directly and confirmed the text, then recomputed everything myself with fractions.Fraction and sympy rather than trusting the finding's evidence line: factorint(83776)={2:6,7:1,11:1,17:1}, 2**7*7*11*17**2=2848384=34*83776, and e4(C)-2*V1 = -54321/837760 + 78/1280 = -327/83776 exactly, matching the denominator the repo's own gates use. Two adversarial escape routes were tested and closed: (a) the line is not a mis-rendering of a neighbouring quantity — 837760 = 2^7*5*7*11*17 and 1675520 = 2^8*5*7*11*17 both carry a 5 and 17^1, so neither is what was printed; (b) it is not already known/recorded in the repo. One escape route partially succeeded and I folded it into the correction: the "| QBOUND" claim still holds for both the true and the printed number, since QBOUND carries 2^36 and 17^3 — so the finding's phrasing that the divisibility claim's support is "wrong by one factor of 2 and one of 17" overstates the consequence; the divisibility conclusion is unharmed. I also found one factual overstatement in the auditor's evidence: "837760 = 2^7*5*7*11*17" is not printed in any of the five artifacts (B:97 gives the fraction bare), so it is not a neighbouring-factorization contrast; the genuine correct neighbours are B:70 (143 = 11·13, 8960 = 2⁸·5·7) and B:112 / A:61 (1675520 = 1280·1309 = 83776·20), all three verified exact. Net: the core claim reproduces exactly, so it holds, with the scope tightened.

---

### 5.47 `agree-exactly-overstated`

| | |
|---|---|
| **severity** | medium |
| **class** | `overstated` |
| **lane** | `localization-argument` |
| **verifier confidence** | high |
| **where** | A §2 line 58 vs §3 line 82; B §0 line 23, §2 line 83; D lines 29, 54 |

**Claim as stated.** A §3 line 82: "the branches agree exactly at one face". B §0 line 23: "the two branches agree exactly at one face (143/8960)". D §1 line 54: "The blind rooted oracle prints exactly that value for its size-one contribution". D line 29: "the one-face contribution agrees between the branches" (offered as "exact").

**What is wrong (originating auditor).** The blind side of the comparison is a 12-significant-digit printout, not an exact object, so "exactly" is not established at any tier above T2 and A's own §2 table correctly says T2 - the prose and the table disagree. The printed +0.0159598214286 differs from 143/8960 = 0.015959821428571427 by 2.857e-14 (8235 ulps), and the print resolution alone permits a true difference of up to 5e-14 absolute = 3.13e-12 relative. So yes: the blind size-1 c4 could differ from 143/8960 in the 13th decimal and nothing in the corpus would show it. Nothing on the blind side of this comparison is exact anywhere in the corpus - the SW/BCH cluster coefficients are float (double), gated only against an exact oracle at 5e-12.

**Evidence (originating auditor).** 143/8960 = 0.015959821428571427; printed value 15 hour RUN.txt:10620 = +0.0159598214286; |diff| = 2.8571e-14 = 8235 ulps; half-ulp of the last printed digit = 5e-14, relative 3.13e-12. A §2 line 58 labels the same fact T2 while A §3 line 82 calls it exact.

**Verifier's corrected statement — authoritative.**

> OVERSTATED (tier-labelling, conclusion unaffected). The one-face agreement between the F07/analytic branch and the blind rooted-oracle branch is exact on one side only; the artifacts' prose calls the agreement itself exact.
> 
> Exact side (T1, sound): -13/896 + 39/1280 = 143/8960 = 0.0159598214285714285714..., nearest float64 0.015959821428571427. Pinned as Q(143,8960) at /home/user/WORKHOUSE/corpus-import/programs/hodge_o4_adjudication/src/ENGINE_O4_hodge_rootonly_firewall_v1.py:43 (with Q(-13,896) at :42 and Q(-39,1280) at :41) and re-derived/hard-compared by one_face_certificate() at :218-230.
> 
> Blind side (float64 printout, T2 at best): the rooted incidence transform sums into np.zeros(5,float) and prints with '%+.12g' — code at /home/user/WORKHOUSE/corpus-import/records/transcripts/15 hour RUN.txt:7672-7679, output at :10620 "size 1: c1=+1 c2=+0.5 c3=+0.21875 c4=+0.0159598214286". That row is the sole numerical record of the quantity (the |C|=1 shape goes through the preflight path at :7609-7627 and never prints a "shape DONE" line). The same 12-digit string appears twice more, both from the same run: notebooks/NB_O4_hodge_v10a26_factor52complete_exactsw_rootedoracle_a100_alt2.ipynb:2897 and "15 hour RUN. results.txt":2861 — one originating computation, not three. No exact rational for the blind size-1 c4 exists anywhere in the repository.
> 
> Quantification: '%.12g' % float(143/8960) is exactly "0.0159598214286", so the printout is fully consistent with equality and bounds the blind value only by the half-quantum of its last printed digit: |c4_blind - 143/8960| < 5e-14 absolute = 3.13e-12 relative. The blind size-1 c4 could differ from 143/8960 in the 13th decimal and nothing in the corpus would show it.
> 
> No check exists at that precision. The rooted-transform size-1 c4 is never gated against 143/8960. The tightest gates on its constituents run at V10A7_TOL = 3e-9 ("15 hour RUN.txt":6011): one-face axial D vs -13/896 (:5504 and :5756; observed residual 0.0 at :8008) and one-face vacuum e4 vs -39/1280 (:6230; observed 4.51e-17 at :7793). Downstream the oracle's totals are gated only at 2e-5 / 2e-4 / 8e-4 (:7682-7684, passes at :10627-10629), and the |C|=1 "one" sector carries a reported Hermiticity residual of 3.75e-13 (:9184), itself larger than the 5e-14 print resolution.
> 
> The corpus already asserts exactness at T3, which is what the artifacts inherited: notebooks/NB_O4_hodge_v10a29b_m5_first_no_m4_rerun.ipynb sets V26_ONE_FACE_PREFIX_EXACT = ("8/3","1","1/2","7/32","143/8960") and substitutes float(Fraction(143,8960)) for the computed row, checking a preloaded computed row against it only at 3e-9 — while that same notebook's own markdown states "production coefficients remain floating-point computer-assisted results until separately adjudicated by an exact rational backend."
> 
> Where the artifacts overstate: A:82 "the branches agree exactly at one face" contradicts A:58, which labels the identical fact T2 and cites the printout; B:51 section heading "Exact one-face agreement" and B:21-22 "agree exactly at one face", although B:73 states it correctly as "equals the blind size 1 c4 to full printed precision"; D:31 heading "The one-face sector agrees exactly", D:29 "The most useful new localization is exact", D:54 "prints exactly that value", and most strongly D:215 "the one-face sector is already proven equal".
> 
> Correct wording: the one-face gap coefficient is exactly 143/8960 on the F07/analytic side (T1) and is structurally expected to be W22-independent at O4 (T1 layer-walk argument, DATA_O4_OrderSchedule_Occurrence_Preflight_CPU.py gates near :609-616, plus the exact 4x4 Gelfand toy exact_one_face_w22_sensitivity() at :317-338 which reproduces -13/896 at O4 and first differs at O5 by -5/7168); the blind rooted oracle's size-one c4 matches it to 12 printed significant digits, i.e. to within 5e-14 absolute / 3.13e-12 relative (T2). Exact equality of the blind value to 143/8960 is not established at any tier.
> 
> Do NOT record "the printed value differs from 143/8960 by 2.857e-14 / 8235 ulps" — that difference is the print rounding, not a measured disagreement.

**Why it holds.** Reproduced from primary sources, with three corrections to the auditor's evidence line. (1) The exact side is genuinely exact: /home/user/WORKHOUSE/corpus-import/programs/hodge_o4_adjudication/src/ENGINE_O4_hodge_rootonly_firewall_v1.py:41-43 fixes EXPECTED_VACUUM[4]=Q(-39,1280), EXPECTED_AXIAL[4]=Q(-13,896), EXPECTED_GAP[4]=Q(143,8960), and one_face_certificate() at :218-230 re-derives the series and raises GateFailure on any mismatch. (2) The blind side is a float64 printed at 12 significant digits: the rooted incidence transform accumulates into np.zeros(5,float) and prints via f'  size {k}: ... c4={x[4]:+.12g}' — source embedded in the run log at "15 hour RUN.txt":7672-7679, output at :10620. I confirmed '%.12g' % float(Fraction(143,8960)) == '0.0159598214286' exactly, so the printout is consistent with equality and constrains nothing tighter than the half-quantum of its last digit. Repo-wide grep for the printed string returns exactly three hits, all from the same run (transcript :10620, "15 hour RUN. results.txt":2861, NB_O4_hodge_v10a26_...alt2.ipynb:2897) — one origin, not three; grep for 143/8960 or Fraction(143,...) finds it only on the exact side and in a hand-installed comparator, never as a computed blind value. (3) No machine check anywhere ties the blind size-1 c4 to 143/8960. So the blind half of the comparison is a display, and 'exactly' is not established. Corrections: the auditor's '|diff| = 2.857e-14 = 8235 ulps' is not a measured disagreement, it is the print rounding of the correctly-rounded string — entering it in the ledger as a discrepancy would itself be a false finding; the only defensible numbers are the resolution bound 5e-14 abs / 3.13e-12 rel. The auditor's 'gated only against an exact oracle at 5e-12' is wrong: the 5e-12 constants in this program are matrix/Haar tolerances (e.g. ENGINE_O4_hodge_v10a24c_rootedfullt1_dualcoldoracle_a100.py:5599); the applicable tolerances are V10A7_TOL=3e-9 on the constituents and 2e-5/2e-4/8e-4 on the oracle totals. The auditor's pointer 'B §2 line 83' is wrong — that line is a citation; B:73 actually states the honest version ('equals the blind size 1 c4 to full printed precision'), while B's overstatement lives in its §2 heading at B:51 and abstract at B:21-22. Not already recorded: grep over src/, ledger/, tests/, theory/, CERTIFIED.md, FRONTIER.md finds no occurrence of 143/8960 and nothing on this agreement. Severity is a tier-labelling defect only: the localization conclusion (a 10.293 gap versus at most 5e-14 of one-face slack) survives unchanged, so low-to-medium rather than medium.

---

### 5.48 `twoface-vacuum-tier`

| | |
|---|---|
| **severity** | medium |
| **class** | `overstated` |
| **lane** | `localization-argument` |
| **verifier confidence** | high |
| **where** | A §2 lines 60-61; B §3 lines 96-114, §6 checks 3-4 (lines 193-194). Repo: /home/user/WORKHOUSE/corpus-import/programs/hodge_o4_adjudication/src/ENGINE_O4_hodge_v10a7_marked_linked_scalar.py:5192,5433-5434,5468 |

**Claim as stated.** A §2 line 60: "two-face vacuum | T1 | e4(C) = -54321/837760, omega4 = -327/83776 (coplanar==perp)". A line 61: "linked-vacuum decomposition | T1 | V_link = -1474623/1675520". B §6 checks 3 and 4 both tiered T1.

**What is wrong (originating auditor).** The corpus evidence for these two-face vacuum numbers is float gating at V10A7_TOL = 3e-9, not exact arithmetic. For omega4 = -327/83776 = 0.0039033 an absolute tolerance of 3e-9 is 7.7e-7 relative - four orders of magnitude looser than the one-face agreement the same table calls T2. The coplanar/perpendicular agreement is likewise a float comparison at 3e-9. What IS exact is only the closing arithmetic on top of assumed rationals: e4(C)-2*V1 == -327/83776 and 13*V1 + 124*VPAIR == -1474623/1675520 in Fraction. Tiering the measured inputs T1 because the arithmetic that consumes them is exact is the failure mode CLAUDE.md's tier table exists to prevent.

**Evidence (originating auditor).** V10A7_TOL = float(os.environ.get('V10A7_TOL','3e-9')) at v10a7:5192; gate 'v10a.7 vacuum {cls} pair full e4=-54321/837760', abs(z['e4']-float(...))<V10A7_TOL at :5433; gate '...omega4=-327/83776', abs(linked-float(...))<V10A7_TOL at :5434; gate 'v10a.7 linked vacuum O4 subtraction=-1474623/1675520', abs(V4_LINKED_MARKED-float(_V4_EX))<V10A7_TOL at :5468. Verified exactly here: -54321/837760 - 2*(-39/1280) = -327/83776 True; 13*(-39/1280) + 124*(-327/83776) = -1474623/1675520 True.

**Verifier's corrected statement — authoritative.**

> OVERSTATED TIER (confirmed, but re-quantified; the auditor's own numbers are partly wrong and must not be carried into the ledger).
> 
> WHAT IS WRONG. Artifact A line 60 (`| two-face vacuum | T1 | e4(C) = -54321/837760, omega4 = -327/83776 (coplanar==perp) |`) and line 61 (`| linked-vacuum decomposition | T1 | V_link = -1474623/1675520, 1675520 = 1280*1309 = 83776*20 |`), under A:53 "Every row is T1 (exact) or T2 (numerical)", assign T1 to values whose entire corpus provenance is a cold FLOAT run. B:93 states the same values "is exact"; B:193-194 tier checks 3 and 4 T1. CLAUDE.md's tier table reserves T1 for "re-derived symbolically from stated definitions, exactly" and puts "float agreement within a stated tolerance" at T2.
> 
> PRIMARY SOURCES, read at the cited lines (/home/user/WORKHOUSE/corpus-import/programs/hodge_o4_adjudication/src/ENGINE_O4_hodge_v10a7_marked_linked_scalar.py):
> - :5192 `V10A7_TOL = float(os.environ.get('V10A7_TOL','3e-9'))` — confirmed.
> - :5384-5397 `_v17_vac_cluster` returns Python floats (`e4=Dd-e2*Nn`); :5424 `linked=z['e4']-2.0*_v1['e4']`.
> - :5433 e4 gate, :5434 omega4 gate, :5436 coplanar/perpendicular agreement gate, :5460 integer count-13 gate, :5466 V_link gate — all four value gates are `abs(float - float(rational)) < 3e-9`.
> - :5265 `def _v17_rational(x,maxden=V10A7_RAT_DEN): return _Q17(float(x)).limit_denominator(int(maxden))`, maxden=1e9 (:5194). The printed "rational~" labels are float reconstructions, not derivations.
> CITATION CORRECTION: the V_link gate is at :5466, not the :5468 the auditor cites.
> 
> DECISIVE EVIDENCE THE AUDITOR MISSED. For A:61's own quantity the reconstruction demonstrably FAILED. The 15-hour run computed V4_LINKED_MARKED = -0.8800987156226097 and printed `rational~ -521965902/593076541` (/home/user/WORKHOUSE/corpus-import/records/transcripts/15 hour RUN. results.txt:55-56), while float(-1474623/1675520) = -0.8800987156226127: gap 2.998e-15 = 27 ulps bitwise (~31 under the relative-ulp convention the repo uses), passing the 3e-9 gate with 1.0e6x margin. The repo already carries this as contradiction C20 (/home/user/WORKHOUSE/ledger/contradictions.yaml:242-262, "kind: float-reconstruction") with a tier-2 FINDING check at /home/user/WORKHOUSE/src/workhouse/invariants.py:404-418, and /home/user/WORKHOUSE/index/claims.jsonl:201 tiers CONST:LINKED_VACUUM_4 at tier 3. A:61's T1 is thus two tiers above this repo's own computed tier for the identical constant, on precisely the value whose float reconstruction the repo already flags.
> 
> QUANTIFICATION CORRECTION. The auditor characterises the evidence by the gate tolerance: "3e-9 is 7.7e-7 relative — four orders of magnitude looser than the one-face agreement the same table calls T2". The gate tolerance is not the observed agreement. From the run's own printed values: e4(C) run -0.06484076585179532 vs float(-54321/837760) = -0.06484076585179527 → 5.55e-17 = 4 ulps; omega4 run -0.00390326585179523 vs -0.0039032658517952636 → 3.3e-17 (print-limited at 15 sig figs). The two-face agreement is ~4 ulps — TIGHTER than the T2 one-face row it is compared against (143/8960 = 0.015959821428571427 vs blind printed 0.0159598214286, 15 hour RUN.txt:10620 → 2.86e-14 absolute, 1.79e-12 relative, print-limited). limit_denominator(1e9) of the two-face run floats does recover -54321/837760 and -327/83776 exactly. So the two-face numbers are well pinned; what is wrong is the tier label, not the number.
> 
> WHAT IS GENUINELY T1 (verified here in fractions.Fraction): e4(C) - 2*V1 == -327/83776 with V1 = -39/1280 → True; 13*V1 + 124*VPAIR == -1474623/1675520 → True, with 124 = (V_link - 13*V1)/VPAIR exactly; 1675520 = 1280*1309 = 83776*20 = 2^8*5*7*11*17, and 83776 = 2^6*7*11*17. The exact-Fraction closure in v10a21r:359,370 (`VPAIR=_XQ(-327,83776)`, `_v21_sum(V_MIN)==_XQ(-1474623,1675520)`) consumes those rationals as HARDCODED INPUTS — it re-adds them, it does not re-derive them.
> 
> CORRECT LABELS: A:60 → T2 (agreement 5.6e-17 = 4 ulps against an assumed rational; gate 3e-9 at v10a7:5433-5434,5436), not T1. A:61 → T2 for the value V_link = -1474623/1675520 (whose cold run sits 3.0e-15 = 27 ulps away; repo C20), T1 only for the integer factorization and the 13/124 closure identity on assumed inputs. B:93 "is exact" → "float-measured to 4 ulps against an assumed rational". B:193-194 checks 3-4 → T2 for the values, T1 for the relations. No number changes; only the tier column and B:93's wording.

**Why it holds.** I opened every cited line myself rather than trusting the evidence line. V10A7_TOL=3e-9 at v10a7:5192 and the float gates at :5433, :5434, :5436, :5466 are confirmed (the auditor's :5468 is a two-line slip). _v17_rational at :5265 is Fraction(float(x)).limit_denominator(1e9) — reconstruction, not derivation — and greps for 54321/83776/837760/1474623 across src/, ledger/, tests/, lean/, index/, the hodge program sources, notebooks and transcripts turn up no exact symbolic derivation anywhere: only this float gate, its verbatim copies in v10a24c:6269-6270,6302, and hardcoded-input reuse in v10a21r:359,370. So the T1 labels on A:60-61 and B checks 3-4 are genuinely above what any machine check in reach establishes. I did not accept the auditor's framing: their central rhetorical number (gate 3e-9 => 7.7e-7 relative, "four orders looser than the T2 one-face row") is backwards — the observed two-face agreement is 4 ulps, tighter than the one-face T2 row's print-limited 1.8e-12 — so I refuted that half and replaced it with the V_link 27-ulp reconstruction failure recorded as C20, which is the real, in-corpus proof that these gated floats are not exact re-derivations. The tier inflation itself I reproduced directly, and it is not already recorded as a finding about these artifacts.

---

### 5.49 `w22-only-structural-difference`

| | |
|---|---|
| **severity** | medium |
| **class** | `graph-conflict` |
| **lane** | `localization-argument` |
| **verifier confidence** | high |
| **where** | A §2 line 59, §3 lines 88-92, §4 lines 96-113; contradicted by D §2, §4, §7 |

**Claim as stated.** A §2 line 59: "W22 (the branches' only structural difference)". A §3 line 89: "the branches differ structurally only in the Q2<->Q2 (W22) block."

**What is wrong (originating auditor).** Contradicted by document D, which enumerates several other structural differences: the representations themselves (exact trace-history state space vs cluster-local Gram/Krylov basis, D §2), the inventories (117,161/69,800 Haar classes vs 203/33 rooted clusters vs 609 marked vs 3,895 Stage-3H, D §4 - explicitly "different objects"), the polarization treatment (F07 fixes polarization_index=2 while the blind run uses one default polarization and the canonical calculation needs all three, D §2 and D §4), the rooted-Mobius vs global-fold assembly (D §3), and lattice-geometry retention (D §3 line 110). Naming W22 as the only difference is what licenses A's whole "one named suspect, two knobs" programme, and it is not what the document set says.

**Evidence (originating auditor).** D §2 lines 65-97 (three distinct representations, "Neither equality of representations has been certified"), D §4 lines 114-136 ("The counts must not be treated as competing enumerations of one corpus"), D §7 lines 165-174 (eight separate unclosed items, only one of which touches W22).

**Verifier's corrected statement — authoritative.**

> HOLDS, with one of the auditor's five sub-items removed as wrong and the "licenses the whole programme" clause downgraded.
> 
> THE DEFECT. Document A asserts twice that W22 is the sole structural difference between the two branches:
> - A:59 (inside the "certified spine" table, row labelled **T1**, under a header at A:53 reading "Every row is T1 (exact) or T2 (numerical), reproducible via the check"): "W22 (the branches' only structural difference) is exactly O4-null at one face".
> - A:88-89: "**The named suspect:** the branches differ structurally only in the Q2↔Q2 (W22) block."
> 
> Nothing in the document set or the repo supports "only", and three independent sources contradict it.
> 
> (1) A's own cited source says "earliest", not "only". D:83: "This is the earliest definite structural mismatch." D §2 is headed "Earliest implementation fork: state space and order schedule" and closes at D:97 with a second, independent difference in the same section: "The blind cluster-local Gram/Krylov basis supplies a third representation. Neither equality of representations has been certified."
> 
> (2) Document B — which A itself indexes as document E (A:25) — enumerates FIVE separate requirements for a valid two-face F07 computation at B:157-175, of which W22 is item 2 of 5. The other four are distinct axes: typed physical P/Q1/Q2 blocks or a proven isometry (B:163-166, because the exact-Haar package "forgets lattice geometry"), vacuum before rooted Möbius (B:171), all three T1 polarizations (B:172-173), Stage-3H/189-record mapping (B:174-175).
> 
> (3) A is internally self-contradictory. A:101-103 (Knob A) reproduces that same five-item list verbatim — "typed physical P/Q blocks or a proven isometry; W22 unschedulable; vacuum before Möbius; all 3 polarizations; map to Stage-3H" — and A:109 lists "rooted Möbius / polarization / Stage-3H crosswalk" as the alternative cause. If W22 were the only structural difference, neither line could exist. A's §5 self-correction (A:130-133) is on a different axis (W22's multi-face O4-nullity) and does not retract "only".
> 
> REPO-SIDE CORROBORATION (verified here, primary sources). The corpus's own prescription enumerates eleven requirements, "all eleven, or it does not count", at /home/user/WORKHOUSE/corpus-import/programs/hodge_o4_adjudication/README.md:27-40. The W22 order toggle is item 10 of 11; items 2, 3, 4, 7 are separate axes (exact order-four occurrence schedule; all 203x3=609 marked evaluations; rooted Möbius on the vacuum-subtracted object; cold 3,895-topology Stage-3H generation of an unshifted 189-record kernel). The repo already treats W22 as one item among several, never as the sole difference: settlement/mce_adjudication_harness.py:304,327,335 carries item8_R_holdout, item9_vacuum_ledger and item10_W22_toggle as three distinct protocol slots, and ledger/gaps.yaml:127-130 records only that item 10 is hardcoded OPEN. No repo file asserts anything like A's claim, so this is not already recorded.
> 
> Structural differences BETWEEN THE TWO BRANCHES that are neither W22 nor consequences of it, each verified:
> - representation: exact global trace-history bilinear, "no Q2 -> Q2 matrix block is constructed" (D:75) vs cluster-local Gram/Krylov closure "P + Q1 + Q2" printed at ENGINE_O4_hodge_v10a24c_rootedfullt1_dualcoldoracle_a100.py:6809; equality uncertified (D:97).
> - extraction: exact rational evaluation vs finite-u diagonalization with a degree-6 fit on 13 points — confirmed in repo source at ENGINE...v10a24c...py:6792-6794 (V23C_FIT_UMAX=0.055, V23C_FIT_DEG=6, V23C_FIT_N=13) and the fit at :6934-6941.
> - assembly: blind performs rooted Möbius on the vacuum-subtracted object (D:101-108); F07 "has no rooted Möbius ledger" and its canonicalization "explicitly renames physical links and forgets lattice geometry" (D:110).
> - inventories: 117,161 -> 69,800 Haar classes vs 203 clusters / 33 rooted shape classes; D:116 "The counts must not be treated as competing enumerations of one corpus", D:127-136 "There is currently no termwise map". The 203/33 figure is confirmed in-repo at corpus-import/records/transcripts/15 hour RUN.txt:10747.
> 
> CORRECTION TO THE AUDITOR. Polarization is NOT a branch-vs-branch difference and must be struck from the list: D:69 says F07 fixes polarization_index=2, and the blind engine defaults to the same single polarization — V23C_POL=int(os.environ.get('V10A23_CLUSTER_POL','2')) at ENGINE...v10a24c...py:6788. Both branches run one polarization, index 2; the 3-polarization requirement (609 = 203x3, README.md:31; "full T1 polarizations : 3" at ENGINE...v10a24c...py:6470) separates BOTH branches from the canonical calculation, not the branches from each other. Also downgrade "licenses A's whole programme": A:108-109's outcome table already branches on non-W22 causes, so the two-knob test itself survives; what fails is the "only" wording and its T1 label.
> 
> SHARPEST STATEMENT. A:59 carries an unverifiable universal-negative structural claim ("the branches' only structural difference") as a parenthetical inside a table row labelled T1 and declared reproducible by a machine check (A:53). It is T3 at best, and it is contradicted by A's own cited sources (D:83, D:97, B:157-175), by A's own §4 (A:101-103, A:109), and by the corpus's eleven-item §15.1 requirement list (corpus-import/programs/hodge_o4_adjudication/README.md:27-40). The defensible form is D's: W22 is the EARLIEST DEFINITE structural mismatch, and per D:91 even its effect on the fourth-order Taylor coefficient is not established ("the mere presence of the block does not prove that it changed the true fourth-order Taylor coefficient").

**Why it holds.** I re-opened every cited line myself. A:59 and A:88-89 do say "only", verbatim, and A:53 declares every row of that table T1/T2 and check-reproducible. D:83 says "earliest definite structural mismatch", not only, and D:97 gives a second uncertified difference (three distinct representations) inside the very same section. Document B — which A itself indexes as document E — lists five separate requirements at B:157-175 with W22 as item 2 of 5. A contradicts itself at A:101-103 and A:109, which reproduce the other four axes. Independent repo-side confirmation: the corpus's own §15.1 list at corpus-import/programs/hodge_o4_adjudication/README.md:27-40 has eleven requirements with the W22 toggle as item 10, and settlement/mce_adjudication_harness.py:304,327,335 carries W22 as one of three distinct protocol items. Nothing in ledger/ or src/ records A's claim, so it is not already known. I refuted one of the auditor's five sub-items: polarization is common to both branches (F07 fixes index 2 per D:69; blind defaults to V23C_POL=2 at ENGINE...v10a24c...py:6788), so it separates both branches from the canonical 609, not the branches from each other; and the "licenses the whole programme" clause overstates, since A:108-109 already branches on non-W22 causes. The core finding — that "only" is unsupported and contradicted, and worse, is carried under a T1 label — survives.

---

### 5.50 `cert-zip-cannot-land-as-a-run`

| | |
|---|---|
| **severity** | medium |
| **class** | `provenance-gap` |
| **lane** | `rules-compliance` |
| **verifier confidence** | high |
| **where** | artifact E (extracted cert dir); docs/decisions/0012-in-repo-runs-are-pinned-evidence.md, Decision paragraph; tests/test_runs.py:20-38; runs/mce_freeze_and_first_run_2026-08-22/ as the exemplar |

**Claim as stated.** the certificate zip presented as the pinned evidence for the exact-Haar package

**What is wrong (originating auditor).** All 20 listed digests verify, but the directory fails ADR 0012's pinning rule and tests/test_runs.py on three counts: (i) the manifest is named SHA256SUMS.txt, not SHA256SUMS; (ii) two on-disk files are unlisted — SHA256SUMS.txt itself and WORKHOUSE_RANK3_ORDER4_MODULAR_HAAR_INDEPENDENT_AUDIT_20260823.md, the latter byte-identical to AUDIT_REPORT.md (same sha256 99f31f3b…), i.e. an unpinned duplicate under a second name; (iii) four entries live under a modular_haar_run/ subdirectory whose four files duplicate four top-level files bit-for-bit, while the test compares recorded names against top-level names only. ADR 0012 requires the manifest to cover every file in the run directory, plus a README stating what was run, on what, and what it does and does not establish — no README is present.

**Evidence (originating auditor).** sha256sum -c SHA256SUMS.txt: 20/20 OK; unlisted on disk: SHA256SUMS.txt, WORKHOUSE_RANK3_ORDER4_MODULAR_HAAR_INDEPENDENT_AUDIT_20260823.md, modular_haar_run/; sha256(AUDIT_REPORT.md) == sha256(WORKHOUSE_..._INDEPENDENT_AUDIT_...md) == 99f31f3bb1ea52b8ff69f72dc03cfe6b55aef308c8e11b468fe083266657a662; tests/test_runs.py::test_every_run_dir_is_fully_pinned asserts set(recorded) == {p.name for p in run_dir.iterdir()} - {"SHA256SUMS"}

**Verifier's corrected statement — authoritative.**

> The shipped certificate package (artifact E, from /root/.claude/uploads/384fab32-8991-52ce-b2bf-4999d379e3f5/dc08a31e-WORKHOUSE_RANK3_ORDER4_MODULAR_HAAR_CERTIFICATE_20260823.zip) has a real, artifact-intrinsic pinning gap, and separately is not droppable into runs/ as-is. Reproduced from primary sources:
> 
> (1) ARTIFACT-INTRINSIC GAP (holds regardless of which repo rule applies). The zip contains 22 files (unzip -l trailer: "22 files"); SHA256SUMS.txt lists exactly 20. `sha256sum -c SHA256SUMS.txt` reports 20/20 OK and gives NO warning about the 2 unlisted files: SHA256SUMS.txt itself, and WORKHOUSE_RANK3_ORDER4_MODULAR_HAAR_INDEPENDENT_AUDIT_20260823.md. The latter is byte-identical to AUDIT_REPORT.md (`cmp` clean; both sha256 = 99f31f3bb1ea52b8ff69f72dc03cfe6b55aef308c8e11b468fe083266657a662, which is manifest line 1). Precisely: its BYTES are pinned under the other name, but the FILENAME is uncovered, so a later edit to that copy is invisible to `sha256sum -c` — exactly the silent-drift failure ADR 0012's rationale names (docs/decisions/0012-in-repo-runs-are-pinned-evidence.md, Decision + "The failure this prevents" paragraph).
> 
> (2) CANNOT LAND UNDER runs/ AS SHIPPED. Emulating tests/test_runs.py (file is 35 lines, not the cited 20-38): it aborts first at line 23, `assert (run_dir/"SHA256SUMS").exists()` — the manifest is named SHA256SUMS.txt. Past that, line 30 fails too: recorded - on_disk = the four `modular_haar_run/...` entries (test_runs.py:29 uses non-recursive `{p.name for p in run_dir.iterdir()}`, so slashed paths can never match), and on_disk - recorded = {SHA256SUMS.txt, WORKHOUSE_..._INDEPENDENT_AUDIT_20260823.md, modular_haar_run}. No README is present, which ADR 0012's Decision paragraph also requires.
> 
> (3) COUNT (iii) OF THE ORIGINAL FINDING IS WEAKER THAN STATED. The four modular_haar_run/ files are byte-identical to their four top-level twins (cmp clean) but BOTH copies are pinned — manifest lines 9-12 carry the same digests as lines 13-16 (1b9ed180…, 2b845725…, 7eb3ecb0…, d5800b40…). This is redundant packaging, not a provenance gap; it bites only the specific non-recursive name comparison in test_runs.py:29.
> 
> (4) FRAMING CORRECTION. The premise "presented as the pinned evidence" is the auditor's, not the collaborator's: no claim of ADR-0012 compliance or of a runs/ landing appears in artifacts A-D or in cert/AUDIT_REPORT.md:61-70 ("Hashes" / "The accompanying ZIP contains..."). ADR 0012's Context binds artifacts "generated in this repository by pinned code", explicitly contrasted with received transcripts (settlement/); this package was produced externally, so it is received evidence and the applicable intake is settlement/-class pinning (ADR 0006, tests/test_settlement.py) or `workhouse triage`, not runs/. ADR 0012 does not currently bind it — (2) is a conditional statement of what must change before it could be landed.
> 
> (5) NOT ALREADY RECORDED. grep over ledger/, docs/, runs/, README.md, FRONTIER.md, CERTIFIED.md for modular_haar / exact_haar / 99f31f3b / 5337734a finds only an unrelated `exact_haar_branches` SHA in runs/mce_freeze_and_first_run_2026-08-22/harness_preflight.log:44.

**Why it holds.** I reproduced all three counts independently. Verified: 20/20 digests OK; 22 files in the zip vs 20 manifest entries; the two unlisted names; byte-identity and shared sha256 99f31f3b… of the duplicate .md; byte-identity of the four modular_haar_run/ twins; and a direct emulation of tests/test_runs.py:20-35 showing both the missing-SHA256SUMS abort at line 23 and the set mismatch at line 30. ADR 0012's Decision paragraph does require SHA256SUMS covering every file plus a README, and no README exists. Nothing in the repo already records this package. The finding survives, but three qualifications are needed and are folded into the corrected statement: count (iii) is redundant-but-fully-pinned duplication rather than a pinning failure; the duplicate .md's bytes are pinned under the other name (only the filename is uncovered); and ADR 0012 by its own Context governs in-repo runs, while this is an externally produced, received package that nothing in A-D claims is ADR-0012 evidence — so the ADR-0012/test_runs.py half is intake-readiness guidance, not a current rule violation. The durable defect is the 2-of-22 manifest gap, which stands on its own.

---

### 5.51 `oneface-explanation-is-cited-not-derived`

| | |
|---|---|
| **severity** | medium |
| **class** | `overstated` |
| **lane** | `rules-compliance` |
| **verifier confidence** | medium |
| **where** | artifact A §2 row 3 (line 59); corpus-import/programs/hodge_o4_adjudication/src/DATA_O4_OrderSchedule_Occurrence_Preflight_CPU.py:610,614,615,616 |

**Claim as stated.** "| **one-face agreement is explained** | T1 | W22 (the branches' only structural difference) is exactly O4-null at one face; first bite O5 = `−5/7168` |"

**What is wrong (originating auditor).** Two problems. (i) Tier: what is offered is a citation of `gates.require(...)` declarations in a corpus program. Reading a gate is not running it, and corpus-import/ is T3 by CLAUDE.md's own table ("a document says so and nothing checks it"). Nothing in src/workhouse/invariants.py checks this, so it is T3 here, not T1 — though it is cheaply T1-able: I re-ran the corpus function itself in about a second and it reproduces exactly. (ii) Scope: the gate shows that zeroing the Q2↔Q2 entry of a hard-coded 4-state one-face model leaves the O4 coefficient unchanged. That is not an explanation of why the F07 and blind branches AGREE at one face — the blind branch reaches size-1 c4 by a different route entirely (des Cloizeaux one-particle block, coefficients extracted by a degree-6 fit on 13 points). "Explained" is one inferential step beyond the evidence; "W22 is ruled out as a one-face cause" is what was shown.

**Evidence (originating auditor).** Re-ran exact_one_face_w22_sensitivity(): o4_equal=True, full=(8/3, 1, −1/4, −1/16, −13/896, −23/12544), pruned O5=−57/50176, o5_difference=−5/7168 exactly; enumerate_closed_layer_walks(4) returns 9 walks; first_closed_order_with_block((Q2,Q2))=5. Function body is a 4x4 Fraction model at corpus-import/programs/hodge_o4_adjudication/src/DATA_O4_OrderSchedule_Occurrence_Preflight_CPU.py:317-338. Blind route's degree-6 fit: cited by D §2 at ENGINE...v10a24c...py:6928-6946.

**Verifier's corrected statement — authoritative.**

> Artifact A §2 (line 59, `52ebdfa7-RANK3_ORDER4_MASTER_RECORD.md`) labels the row "**one-face agreement is explained**" as **T1**, under a §2 header (line 52) reading "Every row is T1 (exact) or T2 (numerical), reproducible via the check." Both halves of that are wrong.
> 
> (i) TIER — verified, no repo check exists. `grep -rn` over `/home/user/WORKHOUSE/src`, `/tests`, `/ledger`, `/settlement` finds zero references to `DATA_O4_OrderSchedule_Occurrence_Preflight_CPU`, `exact_one_face_w22_sensitivity`, or the values `-13/896`, `143/8960`, `-5/7168`. `src/workhouse/invariants.py` has no W22/one-face-null check (its only "one-face" hits, :1000 and :1006, are an unrelated energy-manifold check). Artifact A's own companion screen does not cover it either: the check table in artifact B §6 (`6a2b59cb-…ADJUDICATION.md:189-195`) lists **6** rows — oneface_gap, oneface_matches_blind_size1, twoface_vacuum, vlink_face_decomposable, blind_table_sums_to_oracle, twoface_adjudication_OPEN — and **none** is a W22 check, so A's "reproducible via the check" is false for this specific row. (A also calls it an "8-check screen" at A:27 and A:147 against B's 6 rows, but that count mismatch is a separate defect.) What A cites instead is `gates.require(...)` declarations at `corpus-import/programs/hodge_o4_adjudication/src/DATA_O4_OrderSchedule_Occurrence_Preflight_CPU.py:610,614,615,616` — source text, not a recorded run: the only certificate shipped beside that program, `src/CERT_O4_hodge_fullt1_occurrence_preflight.json`, is a **FAIL** envelope (`status='FAIL'`, `error_type='SystemExit'`) for a *different* script (`ENGINE_O4_hodge_rootface_occurrence_preflight_colab.py`), and no JSON in `corpus-import/` carries an `exact_one_face` payload. By CLAUDE.md's table that is **T3**, not T1.
> 
> I did reproduce the underlying arithmetic exactly (loading the module and calling the function): `full = (8/3, 1, -1/4, -1/16, -13/896, -23/12544)`, `pruned = (…, -13/896, -57/50176)`, `o4_equal=True`, `o5_difference = -5/7168`; `len(enumerate_closed_layer_walks(4)) == 9`; `first_closed_order_with_block((Q2,Q2)) == 5`. So the numbers are right — but re-running the corpus program is *reproduction*, not the "re-derived symbolically from stated definitions" that T1 names: the model is a hard-coded 4×4 Fraction matrix with `h0=(8/3,20/3,12,32/3)`, `layers=(P,Q1,Q2,Q2)` at `DATA_O4…CPU.py:317-338`, itself asserted.
> 
> (ii) SCOPE — "explained" overstates the artifact set's own source document. A's row asserts W22 is "the branches' only structural difference", and the explanation is valid only if that uniqueness premise holds. Document D, which A §0 names as the source for this row, declines exactly that inference at `e22209c0-…STRUCTURAL_TRACE…md:83` ("the **earliest** definite structural mismatch", not the only one), at :91 ("the mere presence of the block does **not** prove that it changed the true fourth-order Taylor coefficient… An exact order-truncated `W22`-off comparison is therefore required"), and at :97 ("The blind cluster-local Gram/Krylov basis supplies a third representation. **Neither equality of representations has been certified.**"). The gate zeroes the Q2↔Q2 entry of a 4-state toy; it does not touch the blind engine's actual one-face model. The supported statement is "W22 is ruled out as an order-4 one-face cause", not "the one-face agreement is explained". Note also that the agreement itself (A §2 row 2, correctly labelled T2) is only a 12-significant-figure printed match: `143/8960 = 0.015959821428571427`, `'%+.12g'` → `+0.0159598214286`, which is verbatim the transcript's `size 1: … c4=+0.0159598214286` at `corpus-import/records/transcripts/15 hour RUN.txt:10620`; no residual is recoverable from the record.
> 
> CORRECTION TO THE ORIGINAL FINDING'S EVIDENCE (I could not confirm it and it is misattributed). The original said the blind branch reaches size-1 c4 "by a degree-6 fit on 13 points". That fit is real but belongs to the **v10a24c** engine (`ENGINE_O4_hodge_v10a24c_rootedfullt1_dualcoldoracle_a100.py:6793-6794` `V23C_FIT_DEG=6`, `V23C_FIT_N=13`; used in `_v23c_fit_cluster` at :6933-6941) — which is what D:91 is talking about. The number A actually cites (`15 hour RUN.txt:10620`) comes from a **v10a26** run whose `_v23c_fit_cluster` was replaced by order-truncated canonical Hermitian SW/BCH (`_v26_sw_blocks(one,4)` in `notebooks/NB_O4_hodge_v10a26_factor52complete_exactsw_rootedoracle_a100.ipynb`, `method='canonical Hermitian SW/BCH through O(u^4)'`), and the transcript itself prints at :10617 "production coefficient method: canonical Hermitian SW/BCH; no polynomial fit/window"; the legacy fit survives there only as a cross-check gate ("v10a.26 exact SW agrees with the retired symmetric fit on the one-face audit"). This partially *helps* A's inference — order-4-truncated SW is exactly the regime where the walk power-counting bites — but it is a float numpy eigendecomposition of a des-Cloizeaux basis, not the exact 4-state Fraction recurrence the gate runs, and it leaves D:97's uncertified-representation-equality premise untouched. The scope objection therefore stands on D's own text, not on the fit.

**Why it holds.** Both halves reproduce from primary sources. The tier half is hard: I confirmed by grep that no check anywhere in src/, tests/, ledger/ or settlement/ touches this claim, and that artifact A's own companion screen (B §6, six rows) has no W22 row, so A §2's blanket "reproducible via the check" is false for that row; the only corpus certificate beside the program is a FAIL envelope for a different script, so the cited gates.require lines are source text, not a recorded run — T3 by CLAUDE.md's table. The scope half is grounded in the artifact set's own source document D:83,:91,:97, which explicitly refuses the "explained" inference and states that representation equality is uncertified; A's parenthetical "the branches' only structural difference" is the unsupported premise. Confidence is medium rather than high because the original finding's evidence line misattributed the blind route: the degree-6/13-point fit is v10a24c, whereas the cited transcript value is from a v10a26 run using order-truncated SW/BCH with the fit explicitly retired. The finding holds after that correction, not as written, and the "explained vs ruled out" distinction is partly interpretive.

---

### 5.52 `tiers-asserted-not-computed`

| | |
|---|---|
| **severity** | medium |
| **class** | `overstated` |
| **lane** | `rules-compliance` |
| **verifier confidence** | high |
| **where** | artifact A §2 header (line 53) and row 8 (line 64); artifact A status line (lines 3-5) |

**Claim as stated.** "Every row is T1 (exact) or T2 (numerical), reproducible via the check." / "Every *check* it points to is machine-verified"

**What is wrong (originating auditor).** CLAUDE.md: "a claim's status is **computed, not asserted**", and the tier table's "Where it lives" column is part of the definition — T1/T2 live in src/workhouse/invariants.py. None of A §2's eight rows is registered there, and the script that allegedly computes them was not delivered, so every row is T3 in this repository's vocabulary today. Row 8's "—" is NOT a gap in the vocabulary: Suite.check defaults to tier=1 and raises on anything but 1 or 2, and the repo already registers dataflow/source-scan verdicts at that default. The tier is set by how the verdict is decided — an exact deterministic predicate over pinned bytes is T1 — not by subject matter. AGENTS.md's ban is on adding tiers, and none is needed. The honest tier for an out-of-tree scan whose transcript was not shipped is simply T3.

**Evidence (originating auditor).** src/workhouse/invariants.py:69-80 (tier default 1; `if tier not in (1,2): raise`); scan-type checks registered at the default tier: invariants.py:654 ("FINDING: the contamination scan reads only the engine file"), :666 ("FINDING: the harness can never report COMPLETE"), :697 ("quarantined targets never reach the engine process"); tests/test_invariants.py:25-40 fails a T1 check whose body matches `_NUM|TOLERANCE|\d+e-\d+|isclose`

**Verifier's corrected statement — authoritative.**

> Artifact A §2 applies this repository's closed verification-tier vocabulary to eight rows that this repository does not compute, under a header asserting they are machine-verified, and the machine was not delivered.
> 
> Verified facts:
> 
> (1) A:51 titles the section "The certified spine (what is machine-verified)"; A:53 states "Every row is T1 (exact) or T2 (numerical), reproducible via the check."; A:3-5 states "Every *check* it points to is machine-verified."
> 
> (2) None of the eight rows (A:57-64) is a registered check in /home/user/WORKHOUSE/src/workhouse/invariants.py. I enumerated all 140 checks across SUITES; none corresponds to one-face gap, one-face agreement, W22 O4-nullity, two-face vacuum, linked-vacuum decomposition, blind-table closure, anchoring-invariance, or oracle-freeness. Grep of invariants.py for 8960, 896, 1280, 83776, 837760, 1675520, 1474623, 54321, 7168, W22 returns zero hits. The sole touchpoint is constants.py:430 LINKED_VACUUM_4 = Rational(-1474623, 1675520), consumed at invariants.py:403-415, which checks a different proposition (exact gate value vs printed float-reconstruction, ~31 ulps) — not A:61's factorization 1675520 = 1280*1309 = 83776*20.
> 
> (3) The check A §0 cites (f07_twoface_adjudication_check.py, "runnable 8-check screen; exit 0; drop-in invariants.py suite") was not delivered: the uploads directory holds 4 .md files plus one zip; the extracted certificate zip holds 23 files, none named f07*. No reader here can run it.
> 
> Per CLAUDE.md ("T3 asserted | a document says so and nothing checks it"; "T3 is the default for everything in the corpus. Promoting a claim means writing the check, not citing the sentence"), all eight rows are T3 in this repository today. Truth is not tier: row 1 (-13/896 + 39/1280 = 143/8960) is exactly true and A's citations are accurate — corpus-import/records/transcripts/15 hour RUN.txt:10620 and corpus-import/programs/hodge_o4_adjudication/src/DATA_O4_OrderSchedule_Occurrence_Preflight_CPU.py:614,616 both exist and say what A says — but corpus-import/ is corpus, not the verification layer, so an in-corpus gates.require() is a document assertion, not a repo check.
> 
> (4) A:53 is internally contradicted by A:64 eleven lines later: row 8 ("F07 oracle-free") carries tier "—", which is neither T1 nor T2 and lies outside the closed tier set (AGENTS.md: "add tiers never"). "—" is not forced by a vocabulary gap: Suite.check defaults to tier=1 (invariants.py:69) and raises on anything but 1 or 2 (invariants.py:78-79, `if tier not in (1, 2): raise ValueError(f"{name}: a check establishes T1 or T2, not T{tier}")`), and the repo already registers source-scan/dataflow verdicts at that default — invariants.py:653-656 ("FINDING: the contamination scan reads only the engine file"), :665-668 ("FINDING: the harness can never report COMPLETE"), :697 ("quarantined targets never reach the engine process"). A deterministic predicate over pinned bytes is registrable as T1; the honest tier for an out-of-tree scan whose transcript was not shipped is T3.
> 
> (5) Corroboration that the rows are not machine-verified as stated: A:62 asserts as T2 that the per-size c4 column sums to the oracle -0.7751458630189. Summing the six printed values at 15 hour RUN.txt:10620-10625 in printed order gives -0.77514586301844246 against the :10626 TOTAL -0.7751458630189173 — gap 4.748e-13 = 4277 ulps; to the 13 digits A prints, the sum is ...0184, not ...0189. A states no tolerance for this T2 row.
> 
> Narrowing vs. the candidate as filed: the argument should not rest on reading the tier table's "Where it lives" column as definitional (that is interpretive); it rests on CLAUDE.md's T3 definition and the "computed, not asserted" principle. A:3's self-label of the *document* as T3 does not cover §2's per-row tiers or its "what is machine-verified" header.
> 
> Scope: this is a labelling/overstatement finding about artifact A. It says nothing about whether the eight propositions are true; several are, and rows 1-3 and 5 are re-derivable in seconds. Registering them would be cheap and would convert the claim from asserted to computed.

**Why it holds.** Reproduced independently from primary sources. Confirmed invariants.py:57/69/78-79 (tier default 1, raise outside {1,2}), the three scan-type checks registered at that default (:653-656, :665-668, :697), and tests/test_invariants.py:25-42 with the numeric regex at :35 — the evidence line's "25-40" is one row short. Enumerated all 140 registered checks and grepped invariants.py for every numerator/denominator in A §2: not one row is registered, and the only LINKED_VACUUM_4 consumer (invariants.py:403-415) checks a different proposition. Confirmed the cited check script is absent from both the uploads directory (4 .md + 1 zip) and the 23-file certificate zip. Confirmed the A:53 / A:64 internal contradiction verbatim. I tried three routes to refute and all failed: (a) A's self-declared T3 status at A:3 covers the document, not §2's per-row tier labels or its "what is machine-verified" header; (b) A's source citations are accurate and its underlying arithmetic is largely true, but truth is not tier under CLAUDE.md, and a gates.require() inside corpus-import/ is corpus text, not a repo check; (c) the "—" is not excused by a vocabulary gap, since the repo demonstrably registers scan verdicts at the default tier. I additionally recomputed A:62's T2 row myself and it fails as printed by 4.748e-13 = 4277 ulps, independently showing the section is not machine-verified as claimed. I trimmed the candidate's overreach on "Where it lives" being definitional and added the scope caveat that the propositions themselves may well be true.

---

### 5.53 `unremarked-census-divergence`

| | |
|---|---|
| **severity** | medium |
| **class** | `graph-conflict` |
| **lane** | `rules-compliance` |
| **verifier confidence** | high |
| **where** | artifact C §4 (lines 151-193); cert/root_exact_pair_topologies.pkl.summary.json; cert/INDEPENDENT_REFEREE_REPORT.md |

**Claim as stated.** C §4: "The new exact generator copies three of those as structural regressions: matched_h0_blocks = 5,400, raw_pair_upper_bound = 9,814,138, skipped_one_face = 54."

**What is wrong (originating auditor).** The shipped run's own summary reports two further census numbers that do NOT match the historical v10a.20b values the document quotes, and neither document remarks on it. Document C §4 records the notebook as gating 3,597 whole-block orbits and 1,829,147 pair occurrences; the delivered root_exact_pair_topologies.pkl.summary.json reports block_orbits 3642 (+45) and pair_occurrences 1831607 (+2460). The regression envelope covers exactly the three numbers that agree, and the referee report repeats those same three while omitting the two that differ. Whether the divergence is an expected consequence of the new unordered canonicalization is nowhere stated, and nothing gates it — which is the difference between a regression suite and a selection of passing regressions.

**Evidence (originating auditor).** cert/root_exact_pair_topologies.pkl.summary.json: {"block_orbits": 3642, "pair_occurrences": 1831607, "matches": 5400, "raw_pair_upper_bound": 9814138, "skipped_one_face_matches": 54}; artifact C §4 lines 158-172; cert/INDEPENDENT_REFEREE_REPORT.md "Topology census" paragraph lists only 5,400 / 9,814,138 / 54

**Verifier's corrected statement — authoritative.**

> CONFIRMED, and strengthenable in three ways. Both halves are independently verifiable here.
> 
> HISTORICAL SIDE (verifiable in this repo, not just in artifact C). The v10a.20b notebook is present at /home/user/WORKHOUSE/corpus-import/programs/hodge_o4_adjudication/notebooks/NB_O4_hodge_v10a20b_denominatorlift_exact_da_m4_a100.ipynb (single-line JSON, line 1). Its gate calls read verbatim: gate('...exact H0 block match census reproduces v10a.16', matches==5400), gate('...exact whole-block orbit census is strictly simplified from float v10a.16', len(tasks)==3597, f'..., float=3607, removed={3607-len(tasks)}'), gate('...exact raw-pair upper bound reproduces v10a.16', raw_upper==9814138), gate('...exact one-face skipped-match census reproduces v10a.16', skipped11==54), gate('...exact pair occurrence census removes float-split duplicates', pair_occ==1829147, f'exact={pair_occ}, float=1829187, ...'), plus the 117,161 nonzero-topology gate. Independently paraphrased at /home/user/WORKHOUSE/corpus-import/records/audits/07-denominator-lift.md:34. So artifact C:159 and C:161 quote the notebook correctly.
> 
> NEW SIDE. The two divergent counts are not merely in a side summary — they are inside the hash-pinned frozen artifact. cert/root_exact_pair_topologies.pkl.gz has SHA-256 5337734a57bd2e1fe690c636f19bc0f65c48bac86cc029a7e4dfe87251e8ff59, which is exactly the "Frozen source topology archive" hash asserted at cert/AUDIT_REPORT.md:63 and cert/INDEPENDENT_REFEREE_REPORT.md:67, and the "source_topology_ledger_sha256" in cert/rank3_order4_exact_haar_summary.json. Reading its opcodes without executing it (pickletools.genops; only 2 STACK_GLOBAL, both fractions.Fraction), the header dict carries counts = {matches: 0x1518=5400, block_orbits: 0x0e3a=3642, raw_pair_upper_bound: 0x0095c07a=9814138, skipped_one_face_matches: 54, pair_occurrences: 0x001bf2b7=1831607, nonzero_topologies: 69800, historical_orientation_sensitive_topologies: 0x0001c9a9=117161, pure_six_topologies: 10368} — byte-identical to cert/root_exact_pair_topologies.pkl.summary.json:2-18.
> 
> THE DIVERGENCE, quantified:
>   block_orbits      3642 vs historical exact 3597: +45  (+1.251043%); vs the float v10a.16 baseline 3607: +35 (+0.970335%)
>   pair_occurrences  1831607 vs historical exact 1829147: +2460 (+0.134489%); vs float baseline 1829187: +2420 (+0.132299%)
> The new values match neither the exact nor the float historical census, so "the run reverted to the pre-exact float count" is not available as an explanation.
> 
> SHARPENING THE AUDITOR'S PHRASING. "The regression envelope covers exactly the three numbers that agree" is imprecise: 117,161 also agrees and is also pinned (C:174-176, C:178-180). The precise statement is that all six historical census integers C names have counterparts in the frozen pkl's counts dict; the four that C reports as gated on the live production route (5,400; 9,814,138; 54; 117,161) all agree exactly, and the two that C:177 says are gated only inside the "unused older collapse function" (3,597 and 1,829,147) are precisely the two the frozen artifact contradicts.
> 
> NOWHERE REMARKED — verified by exhaustive grep. The strings 3642 / 3,642 / 1831607 / 1,831,607 appear in no prose document: not in artifacts A, B, C, D, not in cert/AUDIT_REPORT.md, not in cert/INDEPENDENT_REFEREE_REPORT.md, not in cert/WORKHOUSE_RANK3_ORDER4_MODULAR_HAAR_INDEPENDENT_AUDIT_20260823.md (byte-identical to AUDIT_REPORT.md), and in none of the seven shipped .py files. Conversely 3,597 / 1,829,147 appear only at artifact C:159, C:161, C:177 and nowhere in the cert bundle. cert/INDEPENDENT_REFEREE_REPORT.md:52 says "The underlying generation census STILL has 5,400 matched sectors, raw pair upper bound 9,814,138, and 54 deliberately skipped one-face matches" — naming three of the five generation-census integers carried in the very artifact it certifies and omitting the two that moved; "still" asserts a continuity two of those counts do not have. No shipped script gates either: cert/validate_modular_haar_ledger.py:69-78 gates only 69,800, zero_haar_topologies, weighted_haar_sum, D_EXACT, the QBOUND lift and the ledger SHA.
> 
> SCOPE LIMIT. This is a regression-coverage and disclosure gap, not an arithmetic error: none of these integers enters the scalar (C:180-186), and D_EXACT = -361008126292641364183/7250590288602460800 is separately replayed record-by-record over all 69,800 entries (cert/rank3_order4_exact_haar_validation.json). Also, the claim that ledger_generator.py:1215-1231 pins only three and that exact_haar_sum.py:218-272 is the unused path rests on artifact C's account of work/rank3_order4_cubic_ledger/*, which is EXTERNAL to this repo and UNVERIFIABLE HERE; what is verified here is that the two counts diverge, that they diverge inside the hash-pinned artifact, and that no delivered document or script mentions or gates them. Medium severity stands.

**Why it holds.** I reproduced every element from primary sources rather than the evidence line. (1) Read cert/root_exact_pair_topologies.pkl.summary.json directly: block_orbits 3642, pair_occurrences 1831607, matches 5400, raw_pair_upper_bound 9814138, skipped_one_face_matches 54. (2) Went behind the summary to the pickle itself — decoded its counts dict from raw opcodes (pickletools.genops, no execution) and confirmed the same integers, and confirmed sha256(root_exact_pair_topologies.pkl.gz) = 5337734a... equals the frozen-archive hash asserted in both audit reports, so the divergent counts are inside the pinned artifact. (3) Re-read artifact C:151-201 myself: C:159 and C:161 quote 3,597 and 1,829,147; C:164-171 lists exactly three regressions; C:177 places the 3,597/1,829,147 gates in the acknowledged-unused older collapse. (4) Went one step further than the auditor and verified the historical side inside this repo — the v10a.20b notebook's own gate calls (len(tasks)==3597, pair_occ==1829147, matches==5400, raw_upper==9814138, skipped11==54) and audit 07-denominator-lift.md:34 — so the comparison baseline is not taken on C's word. (5) The notebook additionally records float baselines 3607 and 1829187, and 3642/1831607 match neither, closing the most obvious innocent explanation. (6) Grepped all five artifacts, all cert .md files and all seven cert .py files for the new values: zero hits anywhere outside the data file, and cert/INDEPENDENT_REFEREE_REPORT.md:52 does list exactly the three agreeing numbers under the word "still". (7) Checked the repo for prior recording: 1831607 and root_exact_pair_topologies appear nowhere in /home/user/WORKHOUSE, so this is not already known. The only weakening I found is the auditor's "exactly the three" phrasing (117,161 also agrees and is also pinned), which I corrected without changing the finding's substance; and the external-code gating claims, which I flagged as unverifiable here.

---

### 5.54 `b4-quote-attribution`

| | |
|---|---|
| **severity** | low |
| **class** | `provenance-gap` |
| **lane** | `arithmetic` |
| **verifier confidence** | high |
| **where** | artifact B §4 (line 143); /home/user/WORKHOUSE/corpus-import/records/transcripts/Monday 531 PM.txt:2925,3897 |

**Claim as stated.** B §4: "> \"its incidence test was algebraically wired to reproduce v10a.20\" — `:2925, :3897`"

**What is wrong (originating auditor).** The quoted wording appears only at Monday 531 PM.txt:2925. Line 3897 is a differently worded passage ("the supposed independent incidence adjudicator was effectively constructed to recover the v10a.20 ledger") — the same substance but not the same sentence, presented inside quotation marks as if it were. The other four quotes in that block (:1978, :2287, :2548, :3702) are verbatim and correct.

**Evidence (originating auditor).** Monday 531 PM.txt:2925 contains "…then recognized that its incidence test was algebraically wired to reproduce v10a.20…"; :3897 contains "…the supposed independent incidence adjudicator was effectively constructed to recover the v10a.20 ledger…". :1978 = "Stop. Do not run v10a.21r."; :2287, :2548, :3702 verbatim as quoted.

**Verifier's corrected statement — authoritative.**

> Artifact B line 143 (/root/.claude/uploads/384fab32-8991-52ce-b2bf-4999d379e3f5/6a2b59cb-F07_VS_BLIND_TWOFACE_ADJUDICATION.md:143) reads: > "its incidence test was algebraically wired to reproduce v10a.20" — `:2925, :3897`. Verified against /home/user/WORKHOUSE/corpus-import/records/transcripts/Monday 531 PM.txt (9756 lines): the quoted string is a substring of line 2925 and of line 2981, and of no other line in that file nor any other file under corpus-import/records/transcripts/ (grep "algebraically wired to reproduce v10a.20" -> exactly 2 hits). Lines 2918-2930 and 2975-2985 are a duplicated transcript block, which is why it occurs twice. Line 3897 does NOT contain it; :3897 (359 chars) reads "I spent hours repeatedly treating each newly exposed dependency as if it were the last serious obstacle. Then I finally caught a real structural flaw in v10a.21: the supposed independent incidence adjudicator was effectively constructed to recover the v10a.20 ledger. At that point I realized I had been giving you more confidence than the evidence justified." — same substance, different words. So the second line number in a quotation-marked citation points to a paraphrase, inside a block where the other four citations are one-to-one verbatim (confirmed by exact substring test): :1978 = "Stop. Do not run v10a.21r." (26-char whole line); :3702 = "v10a.21 is structurally incapable of adjudicating this" (54-char whole line); :2287 (147 chars) and :2548 (84 chars) both exact substrings as quoted. TWO CORRECTIONS to the finding as originally stated: (1) its evidence line says the wording "appears only at :2925" — imprecise; it appears at :2925 AND :2981, so :2981 is the plausible intended second citation. (2) Mitigation: B line 233 independently lists `corpus-import/records/transcripts/Monday 531 PM.txt:1978,2287,2548,3702,3897` as the provenance set for "circularity retraction" generally, so :3897 is legitimate evidence for the retraction claim overall — only its placement inside quotation marks at :143 overstates it. Net: citation-precision / provenance defect, severity low; no substantive claim in B depends on it, since the retraction is supported verbatim at :2925/:2981 and in paraphrase at :3897.

**Why it holds.** Reproduced directly from primary sources. I re-read B:138-148 and B:233, then ran exact substring tests in python3 against Monday 531 PM.txt for all five quotes in the block: four match verbatim, the :3897 attribution does not. I also grepped the whole transcripts directory to be sure the auditor had not missed an occurrence, and found one they did (:2981) — which is why the corrected statement narrows their "only at :2925" wording. The defect is real and machine-checkable, but it is citation precision only, with no arithmetic or substantive consequence, and B's line 233 already cites :3897 correctly as part of the general retraction evidence set; any ledger entry should say that rather than implying a fabricated quote.

---

### 5.55 `d-exact-decimal-last-digit`

| | |
|---|---|
| **severity** | low |
| **class** | `artifact-wrong` |
| **lane** | `arithmetic` |
| **verifier confidence** | high |
| **where** | cert/INDEPENDENT_REFEREE_REPORT.md line 16; cert/rank3_order4_exact_haar_summary.json key D_EXACT_decimal; /home/user/WORKHOUSE/src/workhouse/constants.py:210-214 |

**Claim as stated.** Referee report: "The decimal is `-49.790170444484609`." (and cert `"D_EXACT_decimal": "-49.790170444484609"`)

**What is wrong (originating auditor).** Not the correctly rounded decimal of the exact rational. -361008126292641364183/7250590288602460800 = -49.7901704444846074944676901…, whose correctly rounded 15-dp form is -49.790170444484607. The printed …609 is the *double*'s decimal expansion (the nearest double is -49.79017044448460893590890918858349323272705078125), i.e. the value was rounded to binary before being printed. Absolute error of the printed string against the exact rational: 1.5056e-15. This is precisely the defect the repository already records for DELTA_GAMMA_NUM, and by the same mechanism.

**Evidence (originating auditor).** Exact 25-digit value -49.79017044448460749446769; float(D_EXACT) = -49.79017044448461; exact − double = +1.4414e-15; printed −49.790170444484609 vs exact −49.790170444484607494…: |Δ| = 1.5056e-15. Compare /home/user/WORKHOUSE/src/workhouse/constants.py:210-214 ("the printed digit is not the correctly rounded one").

**Verifier's corrected statement — authoritative.**

> CONFIRMED, with two corrections to the auditor's framing (severity is lower than stated, and the DELTA_GAMMA analogy is an overstatement).
> 
> WHAT IS TRUE. `cert/INDEPENDENT_REFEREE_REPORT.md:16` states "The decimal is `-49.790170444484609`." and `cert/rank3_order4_exact_haar_summary.json` carries `"D_EXACT_decimal": "-49.790170444484609"`. Both cited locations verified by direct read. The exact rational recorded immediately above (numerator -361008126292641364183, denominator 7250590288602460800, also present in the JSON as `D_EXACT`) evaluates to
>   -49.7901704444846074944676901292863398145657...
> so the correctly rounded 17-significant-digit (= 15-decimal-place) decimal is -49.790170444484607, not ...609. Recomputed with python3 `decimal` at 60-digit precision, ROUND_HALF_EVEN.
> 
> MECHANISM — CONFIRMED AT SOURCE, not merely inferred. `cert/modular_haar_contractor.py:535` emits
>   "D_EXACT_decimal": format(float(d_exact), ".17g")
> So the field is by construction the 17-significant-digit rendering of the *double* nearest the exact rational, i.e. the value was rounded to binary before being rendered to decimal. That double is exactly -49.79017044448460893590890918858349323272705078125.
> 
> NUMBERS (mine, slightly correcting the auditor's).
>   exact - double            = +1.44144e-15  (= 0.2029 ulp; ulp at this magnitude = 7.105427e-15)
>   printed(...609) - exact   = -1.50553e-15  (auditor wrote 1.5056e-15; correct is 1.5055e-15)
>   printed vs correctly rounded: 2 units in the 15th decimal place (609 vs 607)
> 
> CORRECTION 1 — THE DELTA_GAMMA ANALOGY IS TOO STRONG. The auditor writes "precisely the defect the repository already records for DELTA_GAMMA_NUM, and by the same mechanism." It is the same *class* (binary rounding intervening before decimal presentation) but strictly weaker and mechanically different:
>   (a) /home/user/WORKHOUSE/src/workhouse/constants.py:210-214 (read verbatim) describes rounding an *operand* (q_band^(4)) to a double before an otherwise exact subtraction; here the *result* is rounded once, correctly, and only the decimal rendering over-reaches.
>   (b) DELTA_GAMMA_NUM = 2.0827701250956417 and DELTA_GAMMA_AS_PRINTED_NUM = 2.0827701250956414 are two DIFFERENT doubles (float() of the two strings compares unequal — verified). By contrast float('-49.790170444484609') == float('-49.790170444484607') is True: both strings denote the identical double. No binary value is wrong here; only the 17th printed digit is not the correctly rounded 17th digit of the exact rational.
> 
> CORRECTION 2 — SEVERITY. Purely presentational. In both locations the exact rational is printed adjacent, and nothing consumes `D_EXACT_decimal`: it appears only at its point of generation (`modular_haar_contractor.py:535`) and is read by no script in the certificate bundle (grepped all *.py and *.md in cert/). No downstream exact computation is affected.
> 
> NOT ALREADY RECORDED IN THE REPO. Grep of /home/user/WORKHOUSE excluding corpus-import/ finds no occurrence of `D_EXACT`, `361008126292641364183`, or `49.7901704`. Within corpus-import/ the constant appears only as an exact rational, never as a decimal: corpus-import/theory/DOC_FLUX_constants_index.md:144, corpus-import/records/audits/08-rooted-adjudication.md:53, corpus-import/programs/hodge_o4_adjudication/src/ENGINE_O4_hodge_v10a21r_adjudicator_only_same_kernel.py:42. The ...609 decimal is introduced by the certificate, not inherited from the corpus.
> 
> CLASSIFICATION: artifact-wrong (referee-report prose), low severity, presentational only. Defensible ledger wording, narrow: the referee report's sentence at cert/INDEPENDENT_REFEREE_REPORT.md:16 asserts a 17-significant-digit decimal for the exact rational whose correctly rounded value is -49.790170444484607; the printed string is instead `%.17g` of the nearest double (generator: cert/modular_haar_contractor.py:535), overshooting the ~16 significant digits a double carries. |printed - exact| = 1.5055e-15.

**Why it holds.** I opened both cited artifact locations myself (INDEPENDENT_REFEREE_REPORT.md line 16 confirmed by grep -n; the JSON key confirmed by json.load and by raw grep) and recomputed the exact rational to 60 digits with python3 decimal. The correctly rounded 15-dp form is -49.790170444484607; the printed ...609 is not it. I additionally found the generator line the auditor did not cite — cert/modular_haar_contractor.py:535, format(float(d_exact), '.17g') — which proves the round-to-binary mechanism at source rather than by inference. I also read /home/user/WORKHOUSE/src/workhouse/constants.py:210-214 verbatim and re-derived the DELTA_GAMMA case, which showed the auditor's 'same mechanism / precisely the defect' claim is an overstatement: the two DELTA_GAMMA strings are distinct doubles, whereas ...609 and ...607 parse to the identical double, so this defect is strictly weaker and purely one of decimal over-precision. The auditor's error figure 1.5056e-15 is marginally off (1.5055e-15). Finally I confirmed it is not already recorded anywhere in the repo outside corpus-import (where only the exact rational appears, never a decimal) and that no cert script consumes the field. The core claim reproduces exactly, so it holds; the framing needs the two corrections above before it goes into the ledger.

---

### 5.56 `twoface-vacuum-tier`

| | |
|---|---|
| **severity** | low |
| **class** | `overstated` |
| **lane** | `arithmetic` |
| **verifier confidence** | high |
| **where** | artifacts A §2, B §3 (lines 93-100); /home/user/WORKHOUSE/corpus-import/programs/hodge_o4_adjudication/src/ENGINE_O4_hodge_v10a7_marked_linked_scalar.py:5192,5466; /home/user/WORKHOUSE/corpus-import/records/transcripts/Monday 531 PM.txt:5193-5202 |

**Claim as stated.** A §2 table: "two-face vacuum | **T1** | `e4(C) = −54321/837760`, `ω4 = −327/83776` (coplanar==perp)"; B §3: "The two-face attached-vacuum weight is **exact** and independent of the disputed axial construction"

**What is wrong (originating auditor).** The identity ω4 = e4(C) − 2·V1 = −327/83776, given the rationals, is genuinely T1 (I re-derived it exactly). But the corpus does not establish e4(C) = −54321/837760 exactly: v10a.7 computes a float and gates it against the rational with `abs(...) < V10A7_TOL` where V10A7_TOL defaults to 3e-9, and the transcript prints the values with a tilde ("e4(C)=-0.0648407658517953 ~ -54321/837760"). Corpus evidence for the two-face vacuum is therefore T2 at 3e-9, not T1. Same for the V_link total: gate at :5466 is a 3e-9 float comparison. (Observed residuals are far tighter than the gate — 2-4 ulps for e4, 67-77 ulps for ω4 — but a tolerance-gated float recognized as a rational is not an exact derivation, which is exactly the distinction CLAUDE.md non-negotiable #3 and #5 exist to protect.)

**Evidence (originating auditor).** ENGINE_O4_hodge_v10a7_marked_linked_scalar.py:5192 `V10A7_TOL = float(os.environ.get('V10A7_TOL','3e-9'))`; :5466 gate uses `abs(V4_LINKED_MARKED-float(_V4_EX))<V10A7_TOL`; Monday 531 PM.txt:5193,5196-5198,5201-5202 print "~ -54321/837760". Exact float(-54321/837760) = -0.06484076585179527 vs printed -0.0648407658517953 (2 ulps) and -0.06484076585179532 (4 ulps); float(-327/83776) = -0.0039032658517952636 vs printed -0.00390326585179523 (77 ulps) and -0.0039032658517952346 (67 ulps). Recomputed exactly: -54321/837760 - 2*(-39/1280) = -327/83776 (True).

**Verifier's corrected statement — authoritative.**

> Artifact A §2 (line 60) tiers the row "two-face vacuum | **T1** | `e4(C) = −54321/837760`, `ω4 = −327/83776` (coplanar==perp)", under the header "Every row is T1 (exact) or T2 (numerical)" (A:53); artifact B §3 (lines 91-101) states "The two-face attached-vacuum weight is **exact**". By CLAUDE.md's own tier table (T1 = re-derived symbolically from stated definitions, exactly; T2 = float agreement within a stated tolerance), the corpus evidence for these two values is T2 at 3e-9, not T1.
> 
> Verified from primary sources: `_v17_vac_cluster` (ENGINE_O4_hodge_v10a7_marked_linked_scalar.py:5378-5395) is pure IEEE-double arithmetic — `_v17_vac_R` (:5375) divides by `-float(Esg)` and all inner products go through float Haar contractions. The rationals are not derived but *recognized*: `_v17_rational(x) = Fraction(float(x)).limit_denominator(1e9)` (:5265), which is why the transcript prints a tilde. All three claims in A's row are tolerance gates against `V10A7_TOL = float(os.environ.get('V10A7_TOL','3e-9'))` (:5192):
>   - :5433 `abs(z['e4']-float(_Q17(-54321,837760))) < V10A7_TOL`
>   - :5434 `abs(linked-float(_Q17(-327,83776))) < V10A7_TOL`
>   - :5436 "coplanar/perpendicular vacuum pair linked weights agree" — also `abs(diff) < V10A7_TOL`, so even the "(coplanar==perp)" parenthetical is T2.
> The V_link total is gated the same way: :5465-5466 `_V4_EX=_Q17(-1474623,1675520)` / `abs(V4_LINKED_MARKED-float(_V4_EX)) < V10A7_TOL`.
> 
> Observed residuals are far tighter than the gate but nonzero. Exact `float(-54321/837760) = -0.06484076585179527`; transcript "Monday 531 PM.txt":5194 prints `-0.0648407658517953` (5.6e-17, 2 ulps) and :5196/:5201 print `-0.06484076585179532` (5.551e-17, 4 ulps). Exact `float(-327/83776) = -0.0039032658517952636`; :5194 prints `-0.00390326585179523` (77 ulps) and :5197/:5202 print `-0.0039032658517952346` (2.906e-17 = 67 ulps, rel 7.4e-15). The 3e-9 gate is ~5.4e7× looser than the observed e4 residual.
> 
> The identities themselves ARE exact and I reproduced them in Fractions: `-54321/837760 - 2*(-39/1280) == -327/83776` (True) and `13*(-39/1280) + 124*(-327/83776) == -1474623/1675520` (True, with 13 one-face and 124 = 80 perp + 44 coplanar pair embeddings from :5461-5463). Accordingly, A's *adjacent* row "linked-vacuum decomposition | T1" survives: NB_O4_hodge_v10a21_exact_rooted_cluster_adjudicator_a100.ipynb cell1:7050-7052 checks `_v21_sum(V_MIN) == _XQ(-1474623,1675520)` with exact Fraction `==` and no tolerance. But its inputs are hardcoded there (cell1:7039 `V1=_XQ(-39,1280)`, :7040 `VPAIR=_XQ(-327,83776)`) — i.e. the exact downstream arithmetic consumes constants whose only corpus justification is the 3e-9 float gate. The overstatement is specifically the "two-face vacuum" row, which asserts the *values*, not a relation between them.
> 
> No exact derivation exists to rescue the T1 label. `54321`/`837760` occur in exactly one originating computation, copied verbatim into five further engine/notebook variants (v10a.20 cell1:6004, v10a.21 cell1:6005, v10a.22 cell1:5443, ENGINE_...v10a24c_rootedfullt1...py:6269, v10a.26 cell1:6250) — repetition, not independence (AGENTS.md). theory/superseded/MASTER_THEORY.md:568 restates them (superseded, T3); corpus-import/theory/DOC_FLUX_constants_index.md:231 is a self-citing index row. Certificate zip E contains no occurrence of `54321` or `83776` — its exact-Haar summary covers D_EXACT/D11, not the vacuum sector. Any exact two-face vacuum derivation living under `work/rank3_order4_exact_haar_run/` or A's `f07_twoface_adjudication_check.py` is EXTERNAL and UNVERIFIABLE HERE.
> 
> Not already recorded in the repo: constants.py:429-430 stores `LINKED_VACUUM_4 = Rational(-1474623, 1675520)` with the comment "Exact gate value" (accurate as a description of the gate *target*), and invariants.py:405-419 is the C20 check about a printed float-reconstruction — a different issue. No repo file mentions 83776 or 54321, and no invariant re-derives the two-face vacuum. Severity low (kind: overstated tier label), but it is exactly the T1/T2 boundary CLAUDE.md non-negotiables #3 and #5 exist to protect.

**Why it holds.** I reproduced every element independently. (1) Opened ENGINE_O4_hodge_v10a7_marked_linked_scalar.py at :5192, :5265, :5375-5395, :5405-5436, :5461-5466 and confirmed the vacuum cluster is float-only, the "rational" is a limit_denominator recognizer, and every relevant gate is `abs(float diff) < 3e-9` — including the coplanar==perp gate the finding did not cite (:5436), which strengthens it. (2) Re-read transcript Monday 531 PM.txt:5185-5210 and confirmed the printed values and tildes verbatim. (3) Recomputed in fractions.Fraction: e4-2V1 == -327/83776 True; 13*V1+124*w4 == -1474623/1675520 True; and measured the ulp gaps by bit-pattern, getting exactly the 2/4 and 77/67 ulps the finding claims. (4) Searched for a rescuing exact derivation: repo-wide grep found only verbatim copies of the same float gate in five sibling engines/notebooks, a superseded MASTER_THEORY restatement, and a self-citing prose index entry; certificate zip E has no occurrence of these integers. (5) Confirmed the finding is not already recorded — the only nearby repo check (invariants.py:405) is C20, about a printing artifact. The one correction I made to the finding is a narrowing, not a refutation: v10a.21 cell1:7050-7052 does contain a genuine tolerance-free Fraction equality for the V_link decomposition, so A's "linked-vacuum decomposition | T1" row is defensible as an identity while its inputs remain float-gated; the finding's blanket "same for the V_link total" needed that qualification.

---

### 5.57 `independence-of-local-tensors-partially-overstated`

| | |
|---|---|
| **severity** | low |
| **class** | `overstated` |
| **lane** | `certificate` |
| **verifier confidence** | high |
| **where** | cert/INDEPENDENT_REFEREE_REPORT.md:39-43; cert/crosscheck_modular_haar_reference.py:31-34 |

**Claim as stated.** "I implemented a separate contractor with independently generated local tensors: balanced sectors through k=3 from an exact inverse permutation Gram matrix; ... pure-six sectors from the five-dimensional (2,2,2) invariant space ..." (INDEPENDENT_REFEREE_REPORT.md:39-43), and the checks `observed.BALANCED_INVERSE == {k: reference.balanced_projector(k)[1]}` / `observed.PURE_SIX_INVERSE == reference.pure_six_gram_inverse()`.

**What is wrong (originating auditor).** The two implementations share their mathematical inputs verbatim: PURE_SIX_BASIS is the identical five (2,2,2) tableaux in the identical order in both files, and both build the balanced Gram from the same Weingarten definition 3^cycles(sigma^-1 tau) and invert it by Gauss-Jordan over Fractions. So the two Gram-inverse equality assertions compare two copies of one algorithm on one matrix — near-tautologies. The genuinely independent evidence in this script is the 488-term permutation delta expansion checked entrywise against the Gram-inverse projector, and the two different contraction engines (modular factor-graph elimination vs delta/DSU). Those are real; the blanket phrase "independently generated local tensors" is not.

**Evidence (originating auditor).** AST-level comparison of the three modules: modular_haar_contractor vs independent_exact_su3_projector share 4 same-named top-level functions of which 1 (`inverse_permutation`) is byte-identical, and `compose` / `compose_permutations` are identical modulo the name — so the code is genuinely rewritten, the sharing is at the definition level. PURE_SIX_BASIS at modular_haar_contractor.py:129-135 and independent_exact_su3_projector.py:153-159 are character-for-character the same five tuples in the same order. Gram definitions: modular_haar_contractor.py:110-124 (`Fraction(RANK ** cycles(compose(inverse_permutation(sigma), tau)))`) vs independent_exact_su3_projector.py:134ff, same construction.

**Verifier's corrected statement — authoritative.**

> The two Gram-inverse assertions in the certificate's crosscheck are transcription checks, not independence checks, and one of the uploaded audit reports lists them as "Independent checks".
> 
> VERIFIED MECHANICS (recomputed in exact Fractions, pure-Python retranscription of both modules; numpy absent from this env so the modules were not exec'd directly, but the 488-term and 90-support reproductions below confirm the transcription is faithful):
> 
> 1. crosscheck_modular_haar_reference.py:31-33 asserts observed.BALANCED_INVERSE == {k: reference.balanced_projector(k)[1] for k in (1,2,3)}, and :34 asserts observed.PURE_SIX_INVERSE == reference.pure_six_gram_inverse(). Both sides are inverses of ELEMENTWISE-IDENTICAL rational matrices, not merely equal inverses. modular_haar_contractor.py:111-124 (balanced_inverse) and independent_exact_su3_projector.py:134-148 (balanced_projector) both build G[sigma][tau] = 3**cycles(sigma^-1 tau) over itertools.permutations(range(k)) in the same order; I recomputed both and they agree entry for entry for k=1,2,3 (k=2 Gram = [[9,3],[3,9]]). PURE_SIX_BASIS is character-for-character identical, same five (2,2,2) tableaux in the same order, at modular_haar_contractor.py:129-135 and independent_exact_su3_projector.py:153-159, so both pure-six Grams come out identical: [[36,12,-12,-12,12],[12,36,12,12,12],[-12,12,36,12,12],[-12,12,12,36,12],[12,12,12,12,36]], inverse [[1/12,-1/24,1/24,1/24,-1/24],[-1/24,1/18,-1/36,-1/36,1/72],[1/24,-1/36,1/18,1/72,-1/36],[1/24,-1/36,1/72,1/18,-1/36],[-1/24,1/72,-1/36,-1/36,1/18]]. Both are inverted by exact-rational Gauss-Jordan (modular_haar_contractor.py:84-103 vs independent_exact_su3_projector.py:106-130). Two deterministic Fraction Gauss-Jordan routines on one identical matrix can differ only on a transcription typo; there is no floating point and no tolerance. Evidential weight beyond typo-detection: none.
> 
> 2. AST comparison of the two modules confirms the code is genuinely rewritten and the sharing is at the definition level: exactly 4 shared top-level function names {epsilon, inverse_permutation, invert_fraction_matrix, permutation_sign}, of which exactly 1 is byte-identical (inverse_permutation, modular_haar_contractor.py:50-54 vs independent_exact_su3_projector.py:79-83); compose (modular:57-58) and compose_permutations (ref:86-89) have identical bodies modulo the name.
> 
> CORRECTIONS TO THE CANDIDATE AS FILED:
> 
> (a) Wrong locus. INDEPENDENT_REFEREE_REPORT.md:39-43 is not the strongest instance: that sentence itself discloses the shared construction ("balanced sectors through k=3 from an exact inverse permutation Gram matrix", "pure-six sectors from the five-dimensional (2,2,2) invariant space"), and "independently generated local tensors" is literally true at the code level -- both module docstrings assert non-importation (independent_exact_su3_projector.py:3, modular_haar_contractor.py:3-4) and I found no cross-import. The actual overstatement is at AUDIT_REPORT.md:52-53 (byte-identical duplicate at WORKHOUSE_RANK3_ORDER4_MODULAR_HAAR_INDEPENDENT_AUDIT_20260823.md:52-53), which lists "exact inverse-Gram agreement for balanced sectors k = 1,2,3" and "exact pure-six inverse-Gram agreement" as the first two of six bullets under the heading "## Independent checks".
> 
> (b) The candidate's own positive claim is wrong. The 488-term delta expansion is NOT independent of the Gram inverse: pure_six_permutation_coefficients() (independent_exact_su3_projector.py:193-216) calls pure_six_gram_inverse() at line 196. I reproduced 488 nonzero terms and the 90-element nonzero support (90**2 + 1000 = 9100 entry checks, matching AUDIT_REPORT.md:54). It is an independent ASSEMBLY route only -- signed sum over S3xS3 delta-permutations versus numpy V.T @ PURE_SIX_COEFFICIENT @ V at crosscheck_modular_haar_reference.py:39-40 with PURE_SIX_COEFFICIENT = integer_matrix(72, PURE_SIX_INVERSE) at modular_haar_contractor.py:189. So every pure-six check in this script stays inside the one shared Gram inverse. The only contraction-independent evidence in the script is crosscheck_modular_haar_reference.py:85-88 (40 actual topologies, modular CRT factor-graph elimination vs the reference's delta/union-find partition engine _exact_haar_impl at independent_exact_su3_projector.py:246-345) -- independent of the contraction, still not of the shared local-projector definitions.
> 
> (c) Provenance gap not noted by the candidate: the module the script actually imports as `reference` is exact_su3_projector from ROOT/independent_haar_audit/ (crosscheck_modular_haar_reference.py:19,23). That path is absent from the certificate zip and absent from SHA256SUMS.txt, which hashes only independent_exact_su3_projector.py (6ee16bd5...). Identifying the two by matching API (balanced_projector / pure_six_gram_inverse / pure_six_permutation_coefficients / exact_haar) is an inference, not a hash match; the same un-prefixed/prefixed renaming applies to modular_su3_projector in independent_cross_check_actual_topologies.py:19.
> 
> NOT PREVIOUSLY RECORDED in the repo: grep for "modular_haar" / "INDEPENDENT_REFEREE" / "inverse-Gram" / "independently generated local tensors" across .md/.yaml/.py outside corpus-import/ returns nothing. The finding is in the repository's own idiom per AGENTS.md:65-79 ("Repetition is not independence ... count distinct originating computations, not files").
> 
> SCOPE: this bears only on the strength of the independence framing. It does not challenge any number; D_EXACT, the Haar sum, and the 44-topology and 69,800-record replays are separate claims, and the ledger replay itself is UNVERIFIABLE here (work/rank3_order4_cubic_ledger/ and work/fold_linked_exact/ are external to this repo). Severity low.

**Why it holds.** Every mechanical element of the candidate reproduced from primary sources. I recomputed both Gram constructions in exact Fractions and found them elementwise identical (stronger than the candidate's "share their inputs"), so the two assertions at crosscheck_modular_haar_reference.py:31-34 invert one identical rational matrix via two transcriptions of one deterministic Gauss-Jordan algorithm and can fail only on a typo. The AST evidence line checks out exactly: 4 shared top-level names, exactly 1 (inverse_permutation) byte-identical, compose/compose_permutations identical modulo name; PURE_SIX_BASIS character-for-character identical at the cited lines (only defect: the Gram is at modular_haar_contractor.py:111-124, not 110-124 -- 110 is blank). The candidate holds but needed three corrections: the strongest overstatement is at AUDIT_REPORT.md:52-53 under the literal heading "## Independent checks" rather than at the referee-report sentence it cites (that sentence discloses the shared construction and is literally true at the code level); the candidate wrongly credits the 488-term expansion as independent evidence when independent_exact_su3_projector.py:196 derives it from the same pure_six_gram_inverse(); and the module actually imported as `reference` is not in the zip or in SHA256SUMS.txt. None of these refute the core point, and nothing about it is recorded anywhere in the repo.

---

### 5.58 `packaging-hygiene`

| | |
|---|---|
| **severity** | low |
| **class** | `other` |
| **lane** | `certificate` |
| **verifier confidence** | high |
| **where** | cert/SHA256SUMS.txt; cert/stratified_actual_topology_modular_audit.json |

**Claim as stated.** The zip as a self-contained audit bundle.

**What is wrong (originating auditor).** Three cosmetic-but-real packaging defects: (1) AUDIT_REPORT.md and WORKHOUSE_RANK3_ORDER4_MODULAR_HAAR_INDEPENDENT_AUDIT_20260823.md are the same bytes under two names, which invites double-counting them as two documents; (2) four run outputs (1.5 MB) are duplicated between the package root and modular_haar_run/, and the scripts disagree about which copy is canonical — validate_modular_haar_ledger.py reads modular_haar_run/, crosscheck writes modular_haar_run/, independent_cross_check reads WORK/modular_haar_run/; (3) the shipped stratified certificate embeds an absolute Windows authoring path.

**Evidence (originating auditor).** sha256 99f31f3b... for both .md files; 1b9ed180/2b845725/7eb3ecb0/d5800b40 each appear at two paths in SHA256SUMS.txt; cert/stratified_actual_topology_modular_audit.json field `primary_ledger` = `C:\Users\Alex\Documents\Codex\2026-08-21\https-github-com-ats314-workhouse-https\work\modular_haar_run\rank3_order4_exact_haar_numerators.ndjson.gz`.

**Verifier's corrected statement — authoritative.**

> The certificate zip is not a clean self-contained bundle. Three packaging defects, all reproduced from primary sources; none affects any numerical claim.
> 
> (1) Two names, one file. cert/AUDIT_REPORT.md and cert/WORKHOUSE_RANK3_ORDER4_MODULAR_HAAR_INDEPENDENT_AUDIT_20260823.md are byte-identical (3770 bytes each, sha256 99f31f3bb1ea52b8ff69f72dc03cfe6b55aef308c8e11b468fe083266657a662; `cmp` reports no difference). Correction to the original finding: cert/SHA256SUMS.txt lists only AUDIT_REPORT.md (line 1); the WORKHOUSE_..._20260823.md copy appears at no line of the manifest. A directory-vs-manifest diff yields present-not-in-manifest = {SHA256SUMS.txt, WORKHOUSE_RANK3_ORDER4_MODULAR_HAAR_INDEPENDENT_AUDIT_20260823.md}. So the manifest does not double-count; the defect is an unmanifested byte-duplicate that invites a reader to count two independent audit documents where there is one.
> 
> (2) 1,517,049 duplicated bytes (38.4% of the 3,952,114-byte bundle), read by nothing. rank3_order4_exact_haar_numerators.ndjson.gz (1,489,139 B), _summary.json (1,586 B), _validation.json (914 B) and rank3_order4_modular_reference_crosscheck.json (25,410 B) each exist at the package root and under modular_haar_run/, byte-identical (`cmp`), with pairwise-identical digests at cert/SHA256SUMS.txt:9-12 vs :13-16 (1b9ed180…, 2b845725…, 7eb3ecb0…, d5800b40…). Stronger than originally stated: grepping every .py for those four filenames shows NO script reads the package-root copies. cert/validate_modular_haar_ledger.py:10-13 uses ROOT=Path(__file__).parent, RUN=ROOT/"modular_haar_run"; cert/crosscheck_modular_haar_reference.py:111 writes ROOT/"modular_haar_run"/…; but cert/independent_cross_check_actual_topologies.py:17,62-64 sets WORK = HERE.parent and reads WORK/"modular_haar_run"/… — one level ABOVE the bundle root, unresolvable in-bundle (same WORK definition at cert/independent_replay_modular_crt.py:17). Executed check: running validate_modular_haar_ledger.py in a copy of the bundle exits 0 with "passed": true over 69800 records, and its regenerated modular_haar_run/rank3_order4_exact_haar_validation.json is JSON-semantically equal to the shipped one (byte diff is trailing whitespace only). modular_haar_run/ is the live copy; the root-level 1.45 MiB is dead weight.
> 
> (3) Absolute Windows authoring path. cert/stratified_actual_topology_modular_audit.json:9 reads "primary_ledger": "C:\\Users\\Alex\\Documents\\Codex\\2026-08-21\\https-github-com-ats314-workhouse-https\\work\\modular_haar_run\\rank3_order4_exact_haar_numerators.ndjson.gz". Mitigating and omitted by the original finding: line 10 carries "primary_ledger_sha256": "1b9ed1801e1125e15c4331cb0b06fe2a6782f0638efe725640f3602001f1b469", which I recomputed and which matches BOTH shipped copies exactly — so the content binding is intact and the defect is authoring-environment leakage plus a non-resolvable path, not a broken reference.
> 
> Not already recorded in the repo: grep over /home/user/WORKHOUSE (excluding corpus-import/) for AUDIT_REPORT, stratified_actual_topology, modular_haar_run, primary_ledger, 99f31f3b, 1b9ed180 returns no hits.
> 
> Flagged separately, NOT part of this finding: four scripts import module names the bundle does not ship — `exact_su3_projector` (cert/independent_modular_su3_projector.py:21, cert/crosscheck_modular_haar_reference.py:23) and `modular_su3_projector` (cert/independent_cross_check_actual_topologies.py:21, cert/independent_replay_modular_crt.py:21) — while the files are shipped as independent_exact_su3_projector.py and independent_modular_su3_projector.py, and `ledger_generator` comes only from the external work/rank3_order4_cubic_ledger. Only independent_exact_su3_projector.py and validate_modular_haar_ledger.py are runnable in-bundle. That is a larger defect deserving its own finding.

**Why it holds.** All three sub-claims reproduced independently: cmp/sha256sum confirm the byte-identical .md pair (99f31f3b…); cmp plus SHA256SUMS.txt:9-16 confirm the four duplicated run outputs; and line 9 of stratified_actual_topology_modular_audit.json literally contains the C:\Users\Alex\… path. Two refinements go against the auditor and are folded into the corrected statement — the duplicate .md is absent from the manifest rather than listed twice, and the Windows path is accompanied by a sha256 that matches both shipped copies, so it is cosmetic. One refinement strengthens the finding: I ran validate_modular_haar_ledger.py from a copy of the bundle (exit 0, passed=true, 69800 records, output semantically identical to shipped), establishing that modular_haar_run/ is canonical and that no script reads the 1.45 MiB of package-root duplicates at all. The finding is real, low-severity, and correctly scoped to packaging rather than to any numerical claim; nothing in the repo already records it.

---

### 5.59 `d-one-face-constants-sourced-externally`

| | |
|---|---|
| **severity** | low |
| **class** | `provenance-gap` |
| **lane** | `citations-CD` |
| **verifier confidence** | high |
| **where** | artifact D lines 39, 42, 45-54; repo corpus-import/programs/hodge_o4_adjudication/src/ENGINE_O4_hodge_v10a24c_rootedfullt1_dualcoldoracle_a100.py:5521,5773-5774,6247; ENGINE_O4_hodge_v10a7_marked_linked_scalar.py:5407-5408,5411; corpus-import/records/transcripts/15 hour RUN.txt:7793,8008,8525,9042,10620 |

**Claim as stated.** D §1: D11 = -13/896 "confirmed by the independent verifier at `work/rank3_order4_exact_haar_package_verify/...:124-126`"; e_{4,vac}^{(1)} = -39/1280 "at `work/fold_linked_exact/README.md:21-27`".

**What is wrong (originating auditor).** Both constants are sourced only to external, unverifiable files, when both are gated and PASSED inside this repository. D's strongest section rests on citations a reader here cannot check, while the in-repo evidence that would make it a T1 result went uncited. This is a missed corroboration, not an error.

**Evidence (originating auditor).** -13/896: gated at ENGINE_O4_hodge_v10a24c...py:5521 ("v10a.12 one-face axial D=-13/896") and :5773-5774; PASSED for all three polarizations at '15 hour RUN.txt':8008, :8525, :9042 (value -0.014508928571428572); and produced exactly (Fraction) by DATA_O4_OrderSchedule_Occurrence_Preflight_CPU.py which I executed. -39/1280: gated at ENGINE_O4_hodge_v10a7_marked_linked_scalar.py:5411 and ENGINE_O4_hodge_v10a24c...py:6247 ("v10a.7 one-face vacuum e4=-39/1280"); PASSED at '15 hour RUN.txt':7793 (value -0.030468750000000044). Stronger consequence D did not draw: the ENTIRE blind size-1 row reconstructs exactly from in-repo rationals — c2 = -1/4-(-3/4) = 1/2 = 0.5; c3 = -1/16-(-9/32) = 7/32 = 0.21875; c4 = -13/896-(-39/1280) = 143/8960 -> %.12g = 0.0159598214286 — matching all three printed strings at '15 hour RUN.txt':10620. Vacuum e2=-3/4 and e3=-9/32 gated at v10a7...py:5407-5408.

**Verifier's corrected statement — authoritative.**

> HOLDS, with the evidence line materially corrected and strengthened.
> 
> WHAT I CONFIRMED IN D. Artifact D §1 introduces both one-face constants with external-only provenance: line 36 `D_{11}=-13/896`, sourced at line 39 to `work/rank3_order4_exact_haar_package_verify/WORKHOUSE_RANK3_ORDER4_EXACT_HAAR_FINAL_AUDIT_20260823.md:124-126`; line 42 `e_{4,vac}^{(1)}=-39/1280`, sourced at line 45 to `work/fold_linked_exact/README.md:21-27`. Both paths are external to this repo and unverifiable here. `grep -n "896|1280|8960|firewall|preflight"` over D's 229 lines returns only lines 36, 42, 49, 50 — D cites no in-repo source for either constant anywhere in the document. Its only in-repo citation in §1 (line 53) is for the blind oracle's *printed* size-1 row, not for the constants.
> 
> THE MISSED IN-REPO EVIDENCE IS STRONGER THAN THE AUDITOR STATED, AND IN A DIFFERENT FILE. The auditor cited float gates; the decisive in-repo item is an exact rational routine they did not find: `/home/user/WORKHOUSE/corpus-import/programs/hodge_o4_adjudication/src/ENGINE_O4_hodge_rootonly_firewall_v1.py:41-43` declares, as `fractions.Fraction` literals,
>   EXPECTED_VACUUM = (0, 0, -3/4, -9/32, -39/1280)
>   EXPECTED_AXIAL  = (8/3, 1, -1/4, -1/16, -13/896)
>   EXPECTED_GAP    = (8/3, 1, 1/2, 7/32, 143/8960)
> and `one_face_certificate()` at :217-231 computes all three series from `exact_energy_series()` (:150-215, pure Fraction, no float, no external input) and raises `GateFailure` on any mismatch. I executed it (copy at scratchpad/rof.py, runs in under a second) and it returns exactly those tuples. So the whole of D §1 — both constants AND the difference 143/8960 that D derives — is derived exactly, self-containedly, inside this repository, and D cites none of it.
> 
> The blind size-1 row then reconstructs bit-exactly: `%.12g` of float(143/8960)=0.015959821428571427 is "0.0159598214286"; gap[2]=1/2 -> "0.5"; gap[3]=7/32 -> "0.21875" — all three match the printed strings at `corpus-import/records/transcripts/15 hour RUN.txt:10620` character for character.
> 
> FOUR CORRECTIONS TO THE AUDITOR'S EVIDENCE LINE (none fatal, all should be fixed before any ledger entry):
> 1. The gate `v10a.12 one-face axial D=-13/896` at `ENGINE_O4_hodge_v10a24c_rootedfullt1_dualcoldoracle_a100.py:5521` NEVER PASSED in the cited run: `grep -c "PASS] v10a.12" "15 hour RUN.txt"` = 0. The three PASSes at :8008, :8525, :9042 belong to the different gate `{label} one-face direct block=-13/896` at :5773-5774. The auditor merged two gates.
> 2. `_v10a11_oneface_axial_character()` (v10a24c:5330-5359) is pure float64 numpy and returns no `e3`; its gates use `V10A7_TOL = 3e-9` (v10a24c:6028). That evidence is T2 at 3e-9, not "in-repo evidence that would make it a T1 result".
> 3. The auditor's `-1/16` (axial e3) is unsourced in their evidence line and does not occur in v10a24c at all (`grep -n "1/16"` -> no hits). It is in-repo only at `ENGINE_O4_hodge_rootonly_firewall_v1.py:42` and as output of the exact routine in `DATA_O4_OrderSchedule_Occurrence_Preflight_CPU.py`.
> 4. The auditor's DATA_O4 claim checks out but covers only the axial side: I re-ran `exact_one_face_w22_sensitivity()` (:317-338) and got heff = (8/3, 1, -1/4, -1/16, -13/896, -23/12544), satisfying the exact gates at :615 (`== Fraction(-13,896)`) and :616 (`o5_difference == Fraction(-5,7168)`). It says nothing about -39/1280.
> 
> NUMERICS. Recorded PASS `-0.014508928571428572` (:8008/:8525/:9042) is bit-identical to float(-13/896) — 0 ulps. Recorded PASS `-0.030468750000000044` (:7793) sits 4.5103e-17 = 13 ulps from float(-39/1280) = -0.03046875, i.e. 1.5e-8 of the 3e-9 gate tolerance, so the float branch confirms -39/1280 only to 13 ulps while the firewall engine gives it exactly.
> 
> NOT ALREADY RECORDED. `grep -rn "13/896|39/1280|143/8960" src/ ledger/ theory/ tests/ index/ *.md` returns nothing — none of the three rationals is registered anywhere in the verification layer, and `ENGINE_O4_hodge_rootonly_firewall_v1.py` is referenced by no other file in the repo. So this is a genuine provenance gap and, separately, a live T1 promotion candidate: `one_face_certificate()` is exact, dependency-free, and executes in under a second.

**Why it holds.** Re-read D lines 36-53 directly: both constants carry external-only citations and D mentions no in-repo source. Opened every cited repo line myself. Found and executed a stronger in-repo source the auditor missed (ENGINE_O4_hodge_rootonly_firewall_v1.py one_face_certificate), which derives -39/1280, -13/896 and 143/8960 in exact Fractions; also re-ran the DATA_O4 exact routine. Confirmed the three rationals appear nowhere in src/ledger/theory/tests/index, so it is not already recorded. Also disproved three sub-claims in the auditor's evidence line (zero v10a.12 PASS lines in the transcript; the axial character function is float64 at tol 3e-9 and has no e3; -1/16 is absent from v10a24c), which correct but do not overturn the finding.

---

### 5.60 `document-C-invariants-line-cite-off`

| | |
|---|---|
| **severity** | low |
| **class** | `provenance-gap` |
| **lane** | `corpus-value-search` |
| **verifier confidence** | high |
| **where** | C §1 — vs /home/user/WORKHOUSE/src/workhouse/invariants.py:402-429 |

**Claim as stated.** "the invariant explicitly says the final equality is target-derived and hence not an independent verification in `.../src/workhouse/invariants.py:414-422`" (C §1)

**What is wrong (originating auditor).** The cited range straddles two different checks. Lines 402-418 are the C20 check ("exact gate value vs printed float-reconstruction"), which is about the V_link float artifact, not about target-derivation. The check C describes is at :421-429, "run's applied shift is not Delta_Gamma" ("Gate 85's equality was produced by construction with this shift, so it certifies internal bookkeeping rather than independent agreement"). C's substantive point is correct; the locator is not.

**Evidence (originating auditor).** /home/user/WORKHOUSE/src/workhouse/invariants.py:402-418 = `@dispute.check("C20: exact gate value vs printed float-reconstruction", ..., tier=2)`; :421-429 = `@dispute.check("run's applied shift is not Delta_Gamma", "GLUEBALL §9.2 / C22", tier=2)`.

**Verifier's corrected statement — authoritative.**

> Locator slip in document C, not a substantive error. Doc C lines 59-61 (/root/.claude/uploads/384fab32-8991-52ce-b2bf-4999d379e3f5/be0baa19-WORKHOUSE_RANK3_ORDER4_W2_R2_ORACLE_LINEAGE_TRACE_20260823.md:59-61) attribute "the invariant explicitly says the final equality is target-derived and hence not an independent verification" to /home/user/WORKHOUSE/src/workhouse/invariants.py:414-422. That 9-line window does not contain the statement. Verified against the file (working tree clean; last commit touching it is a76ccb7, 2026-08-22, i.e. predating doc C's 2026-08-23 date, so a stale-revision explanation is ruled out): lines 403-418 are a different check, `@dispute.check("C20: exact gate value vs printed float-reconstruction", "MASTER_THEORY C20", tier=2)` (decorator :403, body :404-418), which concerns the LINKED_VACUUM_4 vs LINKED_VACUUM_4_ARTIFACT ~31-ulp float artifact and says nothing about target-derivation; :419-420 are blank; the intended check is `@dispute.check("run's applied shift is not Delta_Gamma", "GLUEBALL §9.2 / C22", tier=2)` at :421 with body :422-429. Its asserted content sits at :423-424 ("Gate 85's equality was produced by construction with this shift, so it certifies internal bookkeeping rather than independent agreement") and :428 ("— target-derived, so gate 85 is not an independent scalar verification"), both outside the cited range. Quantified: 5 of the 9 cited lines (414-418) belong to the wrong check, 2 are blank, and only :421-422 (decorator + `def _():`) belong to the right one while carrying none of the quoted text; `grep "target-derived"` restricted to lines 414-422 returns 0 hits, and the phrase's sole occurrence in the file is :428. Correct locator is invariants.py:421-429 (:423-424 and :428 for the substantive text). Doc C's substantive point is correct — the invariant does state it — and this is an isolated slip rather than a systematic offset: C's three sibling citations in the same bullet list all check out (constants.py:203-214 with M_GAMMA_4_NUM = -0.7751458630189173 at :207 and DELTA_GAMMA_NUM at :214; constants.py:426-435 with QUARANTINED_SCALAR at :427, RAW_FOLDED_AXIAL_GAMMA_NUM = -11.9485781794007 at :428, RUN15_APPLIED_SHIFT_NUM = 11.17343231638178 at :435; docs/decisions/0002-anchoring-is-not-a-dispute.md:50-57). Severity low: provenance-gap only, no numeric or logical claim is affected. Note also that the originating auditor's own evidence line prints the C20 check as ":402-418"; line 402 is blank and the decorator is at :403.

**Why it holds.** I reproduced the discrepancy directly: reading invariants.py with line numbers shows the C20 check spanning 403-418 and the "run's applied shift is not Delta_Gamma" check spanning 421-429, with the phrase "target-derived" appearing only at line 428 — outside doc C's cited 414-422 range (grep over that window returns zero hits). Doc C's text at :59-61 was re-read verbatim. Git shows invariants.py unmodified since 2026-08-22, before the document's date, eliminating a line-drift explanation. C's other three repo citations in the same list were checked and are accurate, so this is a genuine one-off mis-citation rather than an artifact of a different numbering convention. The finding is real and reproducible, though correctly rated low severity since C's substantive claim about the invariant is true.

---

## 6. Candidate findings refuted at verification (68)

These are recorded in full because a refuted candidate is evidence too — several were
plausible enough that omitting them would leave the next reader to re-derive them. In
particular the terminology charge (`m_4`), the C1-reopening charge, and the Hamer
circularity charge were all pressed hard and all failed, which is a stronger endorsement
of those parts of the upload than silence would be.

### 6.1 `a1-hamer-validated-unqualified` — lane `arithmetic`

The textual observation is real but every load-bearing supporting claim fails, and the residue is already recorded in the repo.

WHAT IS TRUE. "Hamer" occurs exactly once in A (line 40) and twice in B (lines 20, 38); the cell "Hamer-validated; complete construction" appears verbatim at A:40 and B:38, and neither document mentions the normalization bridge anywhere (grep for conditional|bridge|normaliz over both returns only B:85, an unrelated local-root list). D does carry the qualifier at /root/.claude/uploads/384fab32-8991-52ce-b2bf-4999d379e3f5/e22209c0-WORKHOUSE_RANK3_ORDER4_F07_VS_BLIND_ORACLE_STRUCTURAL_TRACE_20260823.md:142. The numbers check out: 8*HAMER_A4_NUM = -0.7751458630184 vs M_GAMMA_4_NUM = -0.7751458630189173, |delta| = 5.172529071728604e-13 = 4659 ulps, rel 6.673e-13. forensics:60 is quoted correctly (verified by sed -n '55,65p'); ledger/contradictions.yaml:49-54 is the external_validation block as cited. The verdict line is at "15 hour RUN.txt":10751 (also 10654, 7739), not :10750.

WHY IT DOES NOT HOLD.

1. "Unproved normalization bridge" is wrong for the bridge actually used. /home/user/WORKHOUSE/src/workhouse/invariants.py:1366-1379 registers a T1 check (no tier= argument; default tier=1 per invariants.py:69) named "the m_n = 2^(n-1) a_n bridge is the x = 2u conversion", which re-derives it symbolically from Hamer eqs. (1)-(2) and states "Not a fit and not a convention choice - the two printed equations force it." The conversion the finding calls unproved (u = x/2) is precisely the proved half. forensics:60 concerns the RUN source's internal canonical-magnetic-normalization derivation, a narrower object; D:142 itself makes that distinction ("the external bridge from the source variable to canonical u"), which the finding collapses.

2. "Agreement is 5.2e-13, not exact" is not a defect and is already recorded. HAMER_A4_NUM = -0.0968932328773 (/home/user/WORKHOUSE/src/workhouse/constants.py:239) is a 13-decimal-place printed Table 1 value; the half-ulp of its last printed digit is 5e-14, times 8 = 4.0e-13, i.e. the printed precision alone accounts for most of the observed 5.1725e-13. Exactness is unattainable in principle. constants.py:264 sets HAMER_TOLERANCE = 5.3e-13 (gap = 97.6% of bound, not widened), and the agreement is a named, checked-in T2 claim: invariants.py:386 "Hamer 8*a_4 matches m_Gamma to ~5.2e-13", listed at /home/user/WORKHOUSE/CERTIFIED.md:501, with the magnitude also written into contradictions.yaml:51-52.

3. "Used as a tiebreaker against the F07 branch" is contradicted by the documents. A:12 "without promoting either side of the open contradiction"; A:42 "the real, open branch conflict"; A:45 the two are "rivals, not input/output"; A:78 "Neither side is promoted."; B:5-6 "the physical adjudication it localizes is open". Neither document invokes Hamer anywhere except the one table cell, so it is used for nothing, least of all adjudication.

4. "Complete construction is contradicted by the run's own verdict" conflates promotion with construction. RUN.txt:10751 forbids promoting either fourth-order claim; the same block (10740-10750) shows gates 82-86 PASS, "PASSED 86/86 v10a.23 GATES", and "canonical 189 nonzero anchored records :: 189". In context "complete construction" contrasts the oracle's full per-size linked-cluster sum (A:59, T2 row "blind table closes") with M4_SHORTCUT, which the same table labels a shortcut (ax_rest - V_link). A also reports the forcing correctly (A:43-45), so it is not eliding contradictions.yaml's by_construction_caveat (:55-61).

5. The unqualified phrasing is the repo's own. /home/user/WORKHOUSE/ledger/gaps.yaml:48-49 asserts as a premise "the Gamma-point scalar is externally validated against Hamer" with no qualifier, and contradictions.yaml:53 calls it "substantive external validation, not internal bookkeeping". A and B mirror the ledger's language. If the qualifier is missing anywhere, it is missing in the ledger first - which is exactly what D:203 already recommends fixing ("should be qualified as conditional on the unproved normalization bridge"). Charging A/B with it double-counts a recommendation the same upload set already makes against the repo.

6. Too weak even on its own terms. A:19-27 indexes D as required reading in its own document set, so A is a front-door index whose one-line summary cell does not repeat a qualifier its own indexed companion states. That is summarization compression in a document self-labelled T3 (A:3-4), not an overstatement worth a ledger entry.

If anything survives, it is a repo-side note, not an artifact finding: gaps.yaml:49 and contradictions.yaml:53 state the Hamer validation unqualified while /home/user/WORKHOUSE/corpus-import/records/audits/05-latest-run-forensics.md:60 lists the magnetic-normalization derivation as open - and that tension is already written up at D:203.

---

### 6.2 `ax-rest-reverification` — lane `arithmetic`

REFUTED. The finding's load-bearing assertion — that B's `ax_rest = -11.9485781794014` "cannot have been re-verified against either cited source, because neither carries that value" — is false for src/workhouse/constants.py, and B itself prints the verification route.

What I reproduced (exact, fractions.Fraction):
1. constants.py:427 QUARANTINED_SCALAR = Rational(-160506019419340168451, 14501180577204921600); constants.py:430 LINKED_VACUUM_4 = Rational(-1474623, 1675520). Their sum is exactly -86634244910174898583/7250590288602460800 = -11.94857817940137739778123..., float -11.948578179401377, and '%.13f' of that is EXACTLY -11.9485781794014 — B's printed figure to the digit. constants.py therefore does carry B's ax_rest, exactly, in two constants three lines apart in the same file.
2. B states that very identity one row down: artifact B line 37, `M4_SHORTCUT` = `ax_rest - V_link` = QUARANTINED_SCALAR; and B line 40 gives `-V_link = +0.880098715622613`, which is float(1474623/1675520) = 0.8800987156226127 -> '%.15g' = 0.880098715622613, i.e. LINKED_VACUUM_4 to the last bit. B is working consistently in the exact branch, not quoting the run's float.
3. Every other §1 value is likewise exactly reproducible from constants.py: M4_SHORTCUT -11.0684794637788 = '%.13f'(float(QUARANTINED_SCALAR) = -11.068479463778765); M4_ORACLE -0.7751458630189 = M_GAMMA_4_NUM (constants.py:207) = -0.7751458630189173. So "All values re-verified this session against ... src/workhouse/constants.py" is TRUE as written.

The auditor's arithmetic is right but attached to the wrong constant. constants.py:428 RAW_FOLDED_AXIAL_GAMMA_NUM = -11.9485781794007 is a `_NUM` float faithfully transcribing the run's printed `rest_direct` at corpus-import/records/transcripts/15 hour RUN.txt:9112 — it neither is nor claims to be the exact D_EXACT+FOLD. Nothing consumes it: its only other occurrence in the repo is the naming guard at tests/test_constants.py:68. So the alleged "consequence for the reader" is not a path the repo takes.

The second half also fails. B line 42 writes `local_shift = M4_ORACLE - ax_rest = +11.1734 (= RUN15_APPLIED_SHIFT)` to 4 dp, and at 4 dp both branches give 11.1734 (exact branch 11.17343231638246; float branch M_GAMMA_4_NUM - RAW_FOLDED_AXIAL_GAMMA_NUM = 11.173432316381783, 2 ulps from RUN15_APPLIED_SHIFT_NUM = 11.17343231638178 at constants.py:435, matching transcript :10637). Calling a 4-dp statement "false at the precision B uses one line earlier" holds B to a precision it deliberately did not use — a criticism of B's choice, not a discrepancy in B.

Internal slip in the finding: its `wrong` paragraph says the run sits "~6.8e-13 = 383 ulps" from exact ax_rest; the correct count for :9112 is 6.7679e-13 = 381 ulps (383 is :9131's count, and also the local_shift count). Its own evidence line says 381, so the two halves disagree.

Residual true kernel, well below finding-grade: B's 13-dp ax_rest does not appear verbatim in the transcript — nearest prints are :9112 -11.9485781794007 (381 ulps), :9130 -11.948578179400714 (373 ulps), :9131 -11.948578179400696 (383 ulps) from float(exact) — so "re-verified against the transcript" is loose for that one row, and the run's float pipeline genuinely sits ~6.77e-13 from exact (its D at :9129 prints -49.79017044448387 vs exact float(-361008126292641364183/7250590288602460800) = -49.79017044448461, 104 ulps; D_EXACT itself comes from artifact C:217, external, but the exact ax_rest is anchored entirely in repo constants). This is the benign float-vs-exact genus the repo already documents in place at constants.py:211-215 for DELTA_GAMMA_NUM ("Benign, but the printed digit is not the correctly rounded one"); it corrupts no check and does not support the stated finding.

---

### 6.3 `b2-zeroed-rows` — lane `arithmetic`

Refuted. The substitution is real but the finding's three supporting claims are all false, and the residue is too weak to state.

VERIFIED FACTS. Transcript /home/user/WORKHOUSE/corpus-import/records/transcripts/15 hour RUN.txt:10623 prints "size 4: c1=+0 c2=+2.0872192863e-14 c3=+1.33226762955e-15 c4=-1.3933298959e-14" and :10624 "size 5: ... c4=-2.85049761573e-14"; artifact B lines 60-61 print "size 4: c4 ~ 0  (numerical zero)" / "size 5: c4 ~ 0  (numerical zero)". Omitted sum = -4.24382751163e-14 (exact Decimal). Four printed nonzero rows sum = -0.7751458630184 = 8*(-0.0968932328773) exactly, bit-for-bit in float. Six printed rows sum = -0.7751458630184424382751163. TOTAL(-0.7751458630189173) - six-row sum = -4.748617248837e-13; TOTAL - four-row sum = -5.173e-13.

WHY IT FAILS.
(1) "8.9% of the very 4.75e-13 residual the section is adjudicating" — that residual does not appear in B. grep over all 236 lines of B finds no "4.75e-13", no row sum, no "HAMER", no "0968932328773". B section 2 adjudicates the ONE-FACE sector (143/8960 vs size-1 c4) and concludes only "the first disagreement must occur among connected clusters of size >= 2". The denominator is the auditor's own construction.
(2) "manufactures a spurious exactness ... inviting the reading that the table closes onto the Hamer bridge" — B never sums the rows and never mentions Hamer or the factor 8. The TOTAL B prints is the transcript's own -0.7751458630189173, which is 5.173e-13 AWAY from 8*HAMER_A4_NUM (src/workhouse/constants.py:239). Nothing in B invites that reading; the 12-digit coincidence lives in the transcript's printed digits and would be a separate finding about the transcript, not about B.
(3) "the same order as the size-3/size-6 print granularity" — wrong by an order of magnitude. Size 6 prints -0.208333333333 against exact -5/24, a print error of +3.3333e-13, 7.9x the omitted 4.2438e-14; the half-granularity of the 12-sig-fig rows is 5e-13, 11.8x it. The omitted amount is well BELOW the noise the table already carries.
(4) B does not assert exact zero: it writes "~ 0" and annotates "(numerical zero)". The block is visibly an extract (the c1/c2/c3 columns are dropped from every row), and the characterization is substantively correct — the sibling c2/c3 entries at sizes 3-6 are known-exact zeros printing at the same 1e-15..5e-14 magnitude.
(5) Nothing in B depends on it. Even under the most literal reading of "the oracle is the sum of its per-size contributions", the zeroed rows account for 8.2% of the 5.173e-13 gap a reader would find; the dominant term is the transcript's own print rounding (+3.33e-13 from size 6 alone), which B did not introduce.

Residue: an annotated approximation of two sub-1e-13 numerals inside a digest block that carries a line citation. Load-bearing on nothing, flagged as approximate, below the table's own print noise. Recording it would enter three incorrect quantitative statements into the ledger alongside it.

---

### 6.4 `c1-invariants-line-slip` — lane `arithmetic`

I opened /home/user/WORKHOUSE/src/workhouse/invariants.py at HEAD and confirmed the auditor's HEAD-side line numbers (C20 at 403-418, Delta_Gamma check at 421-429), and re-read artifact C line 61 to confirm it cites 414-422. Then I checked what the auditor did not: git history. Iterating every revision touching invariants.py showed the decorator at line 414 in f643c4b and earlier, 420 in fb8a35c, 421 at HEAD. Printing git show f643c4b:src/workhouse/invariants.py lines 412-424 showed the decorator on 414 and the closing paren on 422 — the cited range exactly. A one-off typo does not reproduce both endpoints of a real prior revision. I further confirmed constants.py did not drift across those same three commits and that ADR 0002:50-57 lands correctly, so invariants.py is the only drifted citation, which is consistent with the collaborator working from a ~2-day-stale read-only snapshot rather than mis-transcribing one range. Filing this as a provenance-gap against the artifact would write a false attribution of error into the ledger.

---

### 6.5 `cert-census-divergence` — lane `arithmetic`

The finding's arithmetic is right but its inference is not, on three independent grounds.

(1) The gate-failure counterfactual has no demonstrable code path, and its premise is external. `exact_haar_sum.py` lives under `work/rank3_order4_cubic_ledger/` and is NOT in this repo, so "lines 218-272 gate 3,597 and 1,829,147" rests entirely on artifact C's prose — which CLAUDE.md forbids treating as authority. Worse, I loaded the pickle: its only payload keys are schema / counts / pattern_histogram / signature_histogram / pair_weights / source_history_sha256, where pair_weights holds 69,800 fully-unordered (LXState,LXState)->Fraction entries. There are no block-level records in it. You cannot recompute 117,161 orientation-sensitive topologies from 69,800 unordered ones (unordered is the coarser quotient), so C's "older collapse ... can recompute and gate 117,161" cannot be running against this pickle — it is dead code from an earlier stage that did its own scan from the W2/R2 history. `block_orbits` and `pair_occurrences` are terminal summary scalars written by ledger_generator.py; the finding treats them as if they were the inputs to gates inside a different program. Two implementations agreeing on every terminal invariant (5400, 9814138, 54, 117161, 69800, and 2,468,250 compatible state pairs, which the pickle's source_history_sha256 block also records) while differing on one intermediate grouping count is the expected signature of two canonicalizations, not of a gate that would fire. Note also 2460/45 = 54.67, i.e. the two deltas are not even consistent with the simple "one-face matches included" story.

(2) The "C does not observe it" charge is refuted by C itself. C lines 164-172 state that the new exact generator copies exactly three censuses as structural regressions — matched_h0_blocks 5,400, raw_pair_upper_bound 9,814,138, skipped_one_face 54 — pointedly omitting 3,597 and 1,829,147. C therefore already discloses that those two are not pinned by the new generator.

(3) The "offered as a safety property" charge misreads C. C lines 188-189 ("They appear only in equality checks that raise on drift") is an anti-leakage argument, and C's very next bullet, lines 196-198, says explicitly that "changing an expected count can only make the program pass or fail; it cannot steer the accumulated numerator toward -11.0685." C already concedes the gates can fail; it argues only that they cannot inject the target.

Nothing about the certified result turns on this: cert/rank3_order4_exact_haar_validation.json passes with records=69800 and an independently recomputed weighted sum -805586892848311021/8092176661386675, and neither 3642 nor 1831607 appears anywhere in /home/user/WORKHOUSE (grep, excluding .venv false positives). Writing "two gates would raise" into the ledger would assert a failure of code no one here can read, against data it does not consume — audit category (iii) UNVERIFIABLE HERE presented as (i)/(ii).

---

### 6.6 `check-count-conflict` — lane `arithmetic`

Refuted: the finding rests on an incomplete read of B §6. Verified line-exact: A:27 ("runnable 8-check screen; exit 0") and A:163 ("# 8 checks, exit 0" — a second statement of the count the auditor missed) both say 8; A:147-148 says "the 8 machine-verified checks + the two OPEN discriminators"; B has exactly 6 numbered rows, at B:191-196 (not 187-199 as cited — 187 is the filename line). But B:185 titles the section "The runnable check (summary)", explicitly abbreviated, and B:198-199 names two further verified behaviors outside the table: "Verified: the guard rejects an F07 size-2 value tagged with retired-engine provenance, and accepts one tagged with an independent (§5-compliant) source." 6 table rows + 2 guard assertions = 8, matching A:27/A:163 exactly. A:147-148's "two OPEN discriminators" maps onto A §4's Knob A / Knob B (A:96 "The decisive test (two knobs)", A:101-104) — two future computations to be added when the script is landed as an invariants suite, not existing checks — so A does not imply 10 script checks. A competing reading does exist (A's 8 = A §2's eight spine rows, A:57-64, of which B lists five), but the finding asserts "they cannot both be right" while never testing B:198-199, the text that reconciles them; that assertion is therefore unsupported. Independently confirmed the script is absent everywhere (grep -rn f07_twoface_adjudication_check over /home/user/WORKHOUSE returns nothing; not in /root/.claude/uploads/384fab32-8991-52ce-b2bf-4999d379e3f5/; not among the 19 files in the extracted cert zip at /tmp/claude-0/-home-user-WORKHOUSE/384fab32-8991-52ce-b2bf-4999d379e3f5/scratchpad/cert), so the count is unverifiable in either direction. Even under the conflicting reading this is a prose count in two self-declared T3 scratchpad documents (A:3-4, B:4-6) about a nonexistent file, touching no value, tolerance, tier, or ledger entry — too weak to state as a finding.

---

### 6.7 `fold-and-linked-vacuum-are-supplied-not-derived` — lane `certificate`

I reproduced the auditor's mechanical greps exactly — they are correct — but the load-bearing inference drawn from them is refuted, on three independent grounds.

(1) MECHANICAL FACTS CONFIRMED. In the cert package, `5315003`, `140454`, `1474623`, `1675520` occur (underscore-normalized, over every file including gz/json) in exactly four places: the three .md reports and `cert/independent_replay_modular_crt.py:25-27`. `-13/896` occurs in .py at exactly `independent_replay_modular_crt.py:25`, `modular_haar_contractor.py:510`, `validate_modular_haar_ledger.py:72`, all bare literals with no comment. The reports' provenance words are `AUDIT_REPORT.md:21` / `WORKHOUSE_..._AUDIT_20260823.md:21` ("separately reproduced fold and linked-vacuum scalars") and `INDEPENDENT_REFEREE_REPORT.md:22`. Arithmetic re-verified exactly: D_EXACT = -13/896 + (1/2)(-805586892848311021/8092176661386675) = -361008126292641364183/7250590288602460800, and D_EXACT + F - V_link = -160506019419340168451/14501180577204921600 = -11.068479463778765.

(2) THE CENTRAL CLAIM IS FALSE: F IS DERIVED, IN THIS REPO, AND I RE-DERIVED IT. /home/user/WORKHOUSE/corpus-import/programs/hodge_o4_adjudication/src/ENGINE_O4_hodge_v10a6_gamma_q1_zero_scalar_ledger.py:668-670 *computes* E2_A, N_A, J_A from resolvent sums; :672-674 gate them exactly to Fraction(-5945,612), Fraction(511051,124848), Fraction(-48945521,25468992); :787 sets C_A = Fraction(0); :798 forms FOLD_A = -2*C_A - E2_A*N_A + J_A; :802 gates `FOLD_A == Fraction(5315003,140454)` with exact `==`, not a tolerance. I recomputed independently in `fractions`: -(-5945/612)*(511051/124848) + (-48945521/25468992) = 5315003/140454 exactly. So 5315003/140454 is not "a hardcoded literal" in the corpus — it is a gate target against an independently accumulated exact rational. The same pattern holds for the other two: `DATA_O4_OrderSchedule_Occurrence_Preflight_CPU.py:615` gates the *computed* `exact["full"][4] == Fraction(-13,896)` (built at :334 from `exact_one_face_w22_sensitivity()`, alongside the O5 sensitivity gate `Fraction(-5,7168)` at :616), and `ENGINE_O4_hodge_v10a21r_adjudicator_only_same_kernel.py:370` gates `_v21_sum(V_MIN) == -1474623/1675520`.

(3) THE CITATIONS THE FINDING SAYS DO NOT EXIST DO EXIST, IN THE SAME SUBMISSION. Artifact B cites the D11 derivation by file:line at `6a2b59cb-F07_VS_BLIND_TWOFACE_ADJUDICATION.md:79-80` ("DATA_O4_OrderSchedule_Occurrence_Preflight_CPU.py:615") and the V_link derivation at :114 ("exact sum gated: v10a.21r V_MIN == -1474623/1675520"). Artifact C cites the fold's lineage at `be0baa19-..._ORACLE_LINEAGE_TRACE_20260823.md:249` (the v10a7 engine path, with SHA-256 at :252) and :262 ("exact fold `-e2*N+J`: lines 5646-5653") — and that file, at :5646-5653 here, carries the comment "the entire axial fold is the separately certified rational -e2*N+J. We recompute it numerically here from the cold Gamma moments and gate the exact rational," then does so.

(4) ALREADY DISCLOSED, NOT CONCEALED. Artifact C:238-242 states the boundary in the collaborator's own words: "The fold and linked-vacuum values are not fitted to the final scalar in this contractor, but neither are they derived inside the 69,800-topology Haar loop. They are supplied as exact constants ... That is another provenance boundary, not an oracle edge into W2/R2." `INDEPENDENT_REFEREE_REPORT.md:60` likewise scopes the certificate to "the arithmetic over the frozen generator lineage."

WHAT SURVIVES is only the trivial and already-stated observation that the cert zip is not self-contained: its SHA256SUMS manifest covers 20 files, none of which derives F, V_link, or D11, so a reader of E alone cannot close the loop. That is a scoping remark the submission itself makes, not a defect, and it is far weaker than "nothing ... reproduces, derives, or even cites a source" and "no artifact supports it." Two secondary framing errors compound it: the evidence line treats "appears nowhere in WORKHOUSE outside corpus-import" as absence, but corpus-import *is* the corpus this repo verifies; and "hardcoded literal" mis-describes the corpus occurrences, which are exact gate assertions over computed quantities.

One real question the finding gestures at but does not establish, and which should NOT be logged under this id: whether the v10a.6 exact gate and the v10a.7 2e-8-tolerance gate (`ENGINE_O4_hodge_v10a7_marked_linked_scalar.py:5653`) are two independent computations of F or one origin duplicated (AGENTS.md, "Repetition is not independence"). Separately, F = 5315003/140454 has no entry in src/workhouse/constants.py and no invariant checks it, so it is T3 in this repo — but "not yet promoted to T1 here" is a gap-register item, not a provenance-gap finding against the collaborator's package. Logging #45 as written would put a false statement in the ledger.

---

### 6.8 `int64-safety-envelope-names-the-wrong-dimension` — lane `certificate`

Refuted on every prong; it is an artifact of conflating two different modules.

(i) The guard cited lives at /tmp/claude-0/-home-user-WORKHOUSE/384fab32-8991-52ce-b2bf-4999d379e3f5/scratchpad/cert/independent_modular_su3_projector.py:42-43, in a module where every factor-graph variable really is 3-valued. That file sets RANK = 3 (line 24), reshapes every tensor to (RANK,)*n (lines 81, 90, 109, 132), sets shape[union.index(item)] = RANK in the elimination (line 230) and sums exactly one axis of length 3 (line 238). No dimension-5 variable exists in it: pure_six_integer_tensor() (lines 93-109) contracts the 5-dimensional pure-six basis index away via invariants.T @ metric @ invariants and returns a (3,)^12 pure color tensor. The comment at line 236 ("Exactly one 3-valued color variable is removed per step") is therefore correct, and 3*max(CRT_PRIMES) names the right axis length for the code the guard actually guards.

(ii) The evidence line's "parallel guard in modular_haar_contractor.py" does not exist. grep -n "INT64\|iinfo\|overflow\|safety" cert/modular_haar_contractor.py returns no matches. The module that does create dimension-5 variables (line 338: dimensions[a] = dimensions[b] = 5) has no int64 safety envelope at all, so no guard there "names the wrong dimension".

(iii) Even transplanted, the proposed correction 5*p is wrong. cert/modular_haar_contractor.py:312-313 sets dimensions[sigma] = dimensions[tau] = math.factorial(k), which is 3! = 6 for the (3,3) balanced pattern — larger than 5. (3,3) genuinely occurs: in cert/rank3_order4_exact_haar_numerators.ndjson.gz the single largest pattern class, ((1,1),(1,1),(1,1),(2,2),(2,2),(2,2),(3,3)), holds 18,800 of 69,800 records. The correct summation bound for that module is 6*p, not 5*p.

(iv) The prose nit is misattributed. "greedy 3-color variable elimination modulo four primes" is cert/independent_replay_modular_crt.py:171, and that script imports modular_su3_projector as modular (line 21) — which diff shows byte-identical to independent_modular_su3_projector.py, i.e. the all-3-valued module, not modular_haar_contractor. The description is accurate for the module it describes.

(v) The "four primes" sub-nit crosses runs. crt_prime_count_histogram {"1": 1209, "2": 68591} (sum 69,800 = fully_unordered_nonzero_topologies) comes from cert/rank3_order4_exact_haar_summary.json, the modular_haar_contractor run, not from independent_replay_modular_crt.py whose method string is being criticized; that replay's output (independent_modular_crt_exact_haar_numerators.json.gz) is not in the bundle and is unverifiable here. Both select primes greedily until modulus > 2*bound, and "four primes" is a fair description of the four-entry CRT_PRIMES pool.

Arithmetic re-checked independently: max(CRT_PRIMES) = 1004535809, p^2 = 1009092191563284481 < INT64_MAX = 9223372036854775807; 3p = 3.0136e9 (1.53e9x headroom... precisely 3.06e9x), 5p = 5.0227e9, 6p = 6.0272e9 — all safe. The finding itself concedes no overflow occurs, so what remains is a naming complaint that turns out to be false for the file it targets.

---

### 6.9 `sha256sums-coverage-is-narrower-than-20-of-20-suggests` — lane `certificate`

I re-derived every primitive from the zip and the extracted tree rather than trusting the evidence line: 22 zip members, 20 manifest lines, `sha256sum -c` 20/20 OK, 16 distinct digests, 4 digests duplicated across root and modular_haar_run/, and AUDIT_REPORT.md == WORKHOUSE_RANK3_ORDER4_MODULAR_HAAR_INDEPENDENT_AUDIT_20260823.md byte-for-byte (99f31f3b…, 3770 bytes). Those raw facts reproduce. But they do not support the finding: duplicated content at two paths is not a coverage gap, since each of the 8 paths is a separate file on disk (distinct inodes) and each is separately hashed — so the manifest covers 20 of the 22 members, exactly as the "20/20" claim says. Furthermore no artifact asserts the coverage claim being rebutted; grepping A-E for sha256/manifest/checksum/digest shows SHA256SUMS.txt is never mentioned, so the finding attacks an auditor's own accurate summary. The self-exclusion and unsigned-manifest points are definitional. What remains is one uncovered path whose bytes are already attested at cert/SHA256SUMS.txt:1 under a different name — a real but immaterial packaging slip, well below the stated medium severity and too weak to write into the ledger as a provenance gap.

---

### 6.10 `zero-haar-stratum-essentially-unchecked-by-shipped-certificates` — lane `certificate`

All four raw numbers reproduce exactly, but the finding is mis-framed in three load-bearing ways and its own evidence line refutes the risk it names.

(1) WRONG BULLET. cert/AUDIT_REPORT.md:56 (the 44-topology stratified audit) is not "offered as coverage of the ledger". It is one of six bullets under "The independent referee route also passed"; the very next bullet, cert/AUDIT_REPORT.md:57, separately offers "an independent all-record replay of the final 69,800-entry ledger" as that coverage. The finding attacks line 56 for failing to do a job line 57 claims.

(2) WRONG LOCALIZATION. I read cert/validate_modular_haar_ledger.py:59-67: it takes `scaled_haar_numerator` from the ledger under audit and only recomputes q-product, signed bound, CRT-modulus sufficiency, haar = num/q, contribution and the sum. It never recontracts. So it adds zero independent-contraction coverage to ANY stratum. Independent recontraction in the shipped set is 44 (stratified, cert/independent_cross_check_actual_topologies.py:100-110) plus 40 (cert/crosscheck_modular_haar_reference.py:85-95) = at most 84 distinct records. Zero stratum: 1/9,184 = 0.0109%. Nonzero stratum: <=83/60,616 = 0.137%. Whole ledger: <=84/69,800 = 0.120%. Zeros are 12.6x less covered relatively, but both strata sit at ~0.1%. The finding says "13.2% of the ledger ... shipped certificates check almost none of it", which implies the other 86.8% is checked. It is not. Presenting a whole-ledger gap as a 13.2% one understates it ~7.6x while pointing at the wrong stratum.

(3) THE RISK ARGUMENT IS CONTRADICTED BY THE STRUCTURE. I grouped all 69,800 ledger records by endpoint signature: all 9,184 zeros are confined to exactly 2 of the 22 signatures - ((1,1)x3,(2,2)x3,(3,3)) at 5,376/18,800 = 28.60% zero, and ((1,1)x3,(2,2)x4) at 3,808/7,616 = 50.00% zero. The other 20 signatures contain no zeros at all. Both zero-bearing signatures ARE independently recontracted: stratified primary indices 506 (2/3), 67101 (0), 17293 (2), 67347 (1), plus 2+2 in the crosscheck. The bug class the finding invokes - "an empty factor graph, a dropped sector, a mis-signed epsilon" - is a property of the network shape, i.e. of the endpoint signature, so it would corrupt the nonzero members of those same two signatures, which are covered. The gap does not align with the named failure mode.

(4) SELF-REFUTED. The finding's own evidence line reports 20/20 agreement on a seeded sample including 10 zeros, and a full independent CRT replay over all 69,800 with 0 mismatches including all 9,184 zeros. The auditor falsified the risk before stating it.

Not already recorded in WORKHOUSE: grep for 69800 / 9184 / stratified / modular_haar across the repo (excluding .venv and corpus-import) returns nothing - this whole rank3/order4 modular Haar lineage is external to the repo.

What IS true and salvageable is a different, weaker, packaging-level observation, given below. Written into the ledger as stated, this finding would record a false characterization of AUDIT_REPORT.md:56-57 and a false localization of a whole-ledger coverage gap onto one 13.2% stratum.

---

### 6.11 `A-609-cluster-unsupported` — lane `citations-AB`

REFUTED — the finding is an artifact of the auditor's own search-scope error. It concludes "no corpus support I can find for 609 as a cluster count" from a grep confined to the transcripts (its evidence line admits this: "grep for '609' in the transcripts returns only elapsed-time and cache figures" — I confirmed that is true of `corpus-import/records/transcripts/15 hour RUN.txt`, whose only "609" hits are elapsed=609.6s at :10006 and cache/hash digits at :9039, :9236, :9439, :9598, :9624, :10329, :10580-10583). But a repo-wide grep shows 609 is one of the best-supported magnitudes in the corpus, and it is NOT the artifact author's own inference.

1. The corpus states the 203x3=609 derivation itself, verbatim, in three separate places:
   - `/home/user/WORKHOUSE/corpus-import/programs/hodge_o4_adjudication/README.md:31` — item 3 of "What the next run must do (corpus §15.1 — all eleven, or it does not count)": "All `203 × 3 = 609` exact marked-cluster evaluations."
   - `/home/user/WORKHOUSE/corpus-import/corpus/MASTER_THEORY_UNIFIED_2026-08-20_v3.md:1711` — "3. all \(203\times3=609\) exact marked-cluster evaluations;"
   - `/home/user/WORKHOUSE/corpus-import/corpus/GLUEBALL_DETAILED_FORMULA_DOCUMENT_2026-08-20_v3_1.md:1458`
   So the auditor's "plausibly the author's own inference (203 clusters × 3 polarizations)" reconstructs the corpus's own stated arithmetic; it is not an unsourced leap.

2. A's exact phrase "full-T1 ... 609" is a corpus token, not a coinage. `/home/user/WORKHOUSE/corpus-import/programs/hodge_o4_adjudication/src/DATA_SU3_Exact_MarkedCluster_m4_Colab.py:259-260` carries the key pair `"candidate_xy_concrete_supports": 203, "candidate_full_t1_cluster_evaluations": 609`.

3. Decisively, 609 is NOT T3 here — this repo machine-checks it. `/home/user/WORKHOUSE/src/workhouse/invariants.py:784` asserts `fz["preflight"]["total_exact_cluster_evaluations"] == 609` inside the registered `adjudication` freeze check, and `invariants.py:796` and `:821` name it in a registered FINDING check ("the run stage fail-closes on cluster 1 of 609 ... the smallest of 609; 474 are 3-face"), which is published at `/home/user/WORKHOUSE/CERTIFIED.md:394-396` with its own reproduction command. `/home/user/WORKHOUSE/settlement/mce_adjudication_harness.py:53` pins `AUTH_EVALS = 609`. Under CLAUDE.md's one principle, that is a machine check, which outranks the auditor's failure to find prose.

4. Arithmetic re-confirmed independently: `15 hour RUN.txt:9174` "concrete rooted clusters = 203", `:9173` "clusters=203, maximal=173", and 3*203 = 609 exactly. The two counts are consistent, not in tension.

The only residual is that artifact A §4 (A:111) carries no inline citation for 609 — but A is a summary record that cites heavily elsewhere, the magnitude is correct, corpus-sourced, and machine-pinned, and "a true, checked number lacked a footnote in a summary" is too weak to enter the ledger as a provenance-gap finding. Writing it in would misrepresent a T1/T2-pinned quantity as unsupported.

---

### 6.12 `B-forbidden-name-m4` — lane `citations-AB`

REFUTED as stated. The finding asserts `m_4` is "an explicitly forbidden spelling for this quantity" — i.e. unconditionally forbidden for m_Gamma^(4). That is not what the register says. Every statement of the rule in the repository is conditioned on the PAIR, not on the token: ledger/symbols.yaml:37-41 (id q_band_4) "Calling THIS AND m_Gamma^(4) BOTH \"m_4\" regenerates a contradiction that does not exist"; symbols.yaml:53-55 (id m_gamma_4) "same collision as q_band^(4); see ADR 0002"; ledger/contradictions.yaml:22-25 forbidden: "two m_4 values" / "Naming BOTH \"m_4\" regenerates the false contradiction"; docs/decisions/0002-anchoring-is-not-a-dispute.md:28,33 "manufactured entirely by calling BOTH quantities m_4" / "Writing \"two m_4 values\" is forbidden"; README.md:200-203 and CLAUDE.md:58 repeat the same conditional form. The forbidden entries exist to make `workhouse search m_4` warn (src/workhouse/search.py:210-215; tests/test_search.py:47-58 "m_4 is what someone types when they have the wrong model"), not to ban the token wherever it appears.

B does not commit the forbidden collision. I grepped B for every anchoring term: `q_band` occurs exactly once, at B:218-219, where B AFFIRMS the rule — "C1's `q_band` vs `m_Γ` naming resolution stands (ADR 0002)". B never labels q_band^(4) as m₄. Its two m₄-subscripted branches are m_Gamma^(4) (B:20, -0.7751458630189173 = M_GAMMA_4_NUM, src/workhouse/constants.py:207) and the quarantined shortcut (B:18, -11.068479463778765; I recomputed float(Fraction(-160506019419340168451,14501180577204921600)) == -11.068479463778765 exactly = QUARANTINED_SCALAR, constants.py:427). Grouping those two under one Γ-rest heading mirrors the repo's own C1 entry, which itself lists q_band^(4), m_Gamma^(4) AND "quarantined shortcut" under one register entry (contradictions.yaml:29-40). It does not regenerate the C1 false contradiction, which is specifically q_band^(4) vs m_Gamma^(4).

Three further weakenings. (1) B's glyph is `m₄` (U+2084), not the ASCII `m_4` the register matches: search.py:211 does `query.strip().lower() == forbidden["text"].lower()`, so the repo's own forbidden-name warning would not fire on B's spelling. (2) The corpus itself — immutable evidence — uses this spelling for exactly the oracle value: theory/GLUEBALL_SOURCE_CONSOLIDATION_GUIDE_2026-08-20_v4_3.md:267 ("not a completed \(m_4\) calculation"), theory/superseded/MASTER_THEORY.md:568 ("independent linked $m_4=-0.7751458630189173$"), and the engine prints it at corpus-import/programs/hodge_o4_adjudication/src/ENGINE_O4_hodge_v10a24c_rootedfullt1_dualcoldoracle_a100.py:7316 `print('  independent linked m4         =',repr(M4_ORACLE))`. The rule is discipline over repo-authored names, not a prohibition on quoting the corpus. (3) Citation slip in the finding: the occurrences in B are lines 3, 18 and 20, not "B:19-21".

Residual that is true but too weak to state as a finding: B:3/18/20 do attach an `m₄` label to a value registered at symbols.yaml:43-55 whose forbidden list contains the text `m_4`, and A does avoid it (A:1 "Γ-scalar", A:9). But a ledger entry saying so would be rebutted by the adjacent `why:` line, and the failure mode the register names is demonstrably absent from B — so the finding's severity is real-but-nil and its stated rationale is wrong.

---

### 6.13 `oneface-agreement-not-new` — lane `citations-AB`

Every factual sub-claim in the evidence line reproduces, but the interpretive claim (kind = "overstated") does not. (1) Repo facts CONFIRMED by direct read: ENGINE_O4_hodge_rootonly_firewall_v1.py:43 defines EXPECTED_GAP with Q(143,8960); :218 `def one_face_certificate()`, :223/:225/:227 raise GateFailure on vacuum/axial/gap mismatch; docstring :7-9 states exact SU(3) character-basis, all fractions.Fraction. Docs cite :41-42 and never :43 (grep of all four .md). Arithmetic CONFIRMED: Fraction(-13,896)+Fraction(39,1280) == Fraction(143,8960), float = 0.015959821428571427, |Δ| vs printed = 2.857089564933801e-14. RUN.txt:10620 is indeed the "size 1: ... c4=+0.0159598214286" line. (2) But the novelty reading is the auditor's own error. B:22-23 says "The decisive new fact is that the two branches **agree exactly at one face**" — the asserted novelty is the cross-branch agreement, which is precisely what the auditor itself concedes is genuinely new ("What is genuinely new is only the numerical comparison of 143/8960 against blind size-1 c4"). So B:22-23 claims exactly the right thing. (3) A §2 is headed "The certified spine (what is machine-verified)" with "Every row is T1 (exact) or T2 (numerical), reproducible via the check" — a verification-status list, not a novelty list; A:12-13 and A §3 name this session's contribution as the localization of the 10.293 gap to size >= 2, not the subtraction. So "present ... as this session's certified contribution" misreads "certified" as "new". (4) Decisively against the "reads as first derivation" reading: B:127 itself writes that v10a.21r's "size-1 weight is `143/8960` — matching", i.e. B explicitly records that another corpus engine already carries the value. (5) The AGENTS.md "Repetition is not independence" rule is aimed at counting duplicated support as independent evidence; here the documents count one-face agreement as one fact and correctly tier it, so the rule is not violated. Net: the value is right, the tier is right, the hedging is right; the missing :43 citation makes the documents' own claim weaker than the repo supports, which is not an overstatement. A false "overstated" finding written into the ledger would be worse than the omission it flags.

---

### 6.14 `c-design-coupling-quantifiable` — lane `citations-CD`

REFUTED on four independent grounds; only the raw value-equality survives, and it carries none of the weight the finding puts on it.

(1) The equality is real. `/home/user/WORKHOUSE/corpus-import/programs/hodge_o4_adjudication/notebooks/NB_O4_hodge_v10a20b_denominatorlift_exact_da_m4_a100.ipynb` cell 1 line 6382 reads verbatim `_LOCAL_Q={(1,1):3,(2,2):24,(3,3):120,(3,0):6,(0,3):6,(6,0):72,(0,6):72}`, and `local_q_pattern` in `/tmp/claude-0/-home-user-WORKHOUSE/384fab32-8991-52ce-b2bf-4999d379e3f5/scratchpad/cert/rank3_order4_exact_haar_summary.json` equals it as a mapping (checked in python3, key-tuple normalized: True).

(2) But equality is mathematically forced, so it cannot distinguish "copied" from "correct". 3, 24, 120 are precisely the U(3) Weingarten common denominators d, d(d^2-1), d(d^2-1)(d^2-4) at d=3 for n=1,2,3; 6 = 3! is the SU(3) epsilon-epsilon determinant denominator for the (3,0)/(0,3) patterns. Five of seven entries are textbook. Only (6,0)/(0,6)=72 has any latitude, and 72=6*6*2 is the natural composition. Moreover the notebook uses `_LOCAL_Q` solely inside `_x_haar_den_bound` (cell 1 lines 6390-6396) to build the rigorous divisor bound QBOUND (line 6413 onward) — it is a bound table, and the minimal valid bound is exactly this. Inferring provenance ("copied") from agreement on forced constants is the inference AGENTS.md's "repetition is not independence" section exists to block, run in reverse.

(3) The artifact contradicts "copied" directly. The same summary carries a SECOND table `local_triangle_bound` = {(0,3):1,(0,6):66,(1,1):1,(2,2):8,(3,0):1,(3,3):120,(6,0):66}, tighter than `_LOCAL_Q` on 6 of 7 keys ((1,1) 3->1, (2,2) 24->8, (3,0)/(0,3) 6->1, (6,0)/(0,6) 72->66). `grep -in "triangle"` over the entire v10a.20b code cell returns zero hits. The new package therefore did fresh work on exactly this object rather than copying the table.

(4) The finding misreads artifact C, and materially. C does NOT "list three census regressions and stop there". Within the cited range, C lines 174-186 additionally pin 2,468,250 and 117,161 (exact_haar_sum.py:35-41), 3,597 / 1,829,147 / 117,161 (lines 218-272), 69,800 (lines 276-368) and the replay verifier's 69,800/117,161 — and C lines 184-186 already state the hardest version of the coupling the finding says is absent: "117,161 is carried as the historical orientation-sensitive reference rather than recomputed by the production sum. The unused older collapse function is the code path that can recompute and gate 117,161." The historical gate is at notebook cell 1 line 6371 (`len(pairw)==117161`), and the census gates the finding quotes are at lines 6343 (5400), 6344 (3597), 6345 (9814138), 6346 (54), 6370 (1829147) — C's cited line ranges are accurate.

(5) The two supporting items are category errors. D11 = -13/896 is not a design choice but a value the historical notebook itself COMPUTES and gates (cell 1 line 5512: `gate('v10a.12 one-face axial D=-13/896', abs(d11+13/896)<V10A7_TOL, d11)`; assigned at line 6566 `D11=_XQ(-13,896)`); reproducing it is agreement on a derived result. And 117,161 is carried under the summary key literally named `historical_orientation_sensitive_topologies` — that is disclosure of the coupling, not concealment of it.

(6) Provenance is unverifiable here anyway: `work/rank3_order4_cubic_ledger/exact_haar_sum.py` and the rest of `work/rank3_order4_cubic_ledger/` are external to this repository and absent, so "copied" versus "independently recomputed and agreed" cannot be adjudicated from the summary JSON. Additionally the same `_LOCAL_Q` line appears in NB_O4_hodge_v10a20_...ipynb cell 1 line 6381 and NB_O4_hodge_v10a21_...ipynb cell 1 line 6382, so naming v10a.20b as "the" source is arbitrary.

Residue not worth a ledger entry: the summary does echo a table byte-equal to a historical one, which is weak corroboration of shared lineage — but C already concedes design/provenance coupling in stronger, better-sourced terms at lines 194-200 plus 174-186, so the finding would replace a correct qualitative statement with an unsupported provenance assertion. Writing it into the ledger would be a net loss.

---

### 6.15 `c-hash-chain-mismatch-vs-shipped-cert` — lane `citations-CD`

Every factual observation in the evidence line reproduces, but the finding's conclusion ("its one testable row fails") does not follow, and the residue is too weak to enter the ledger.

REPRODUCED. C line 131 reads "| final exact summary | `d3d2cb899966eef88e87f8bdc5216772a26a9620d6d77fce0b6341b67c87d9c7` |"; C:136-137 asserts the binding at work/rank3_order4_exact_haar_run/rank3_order4_exact_haar_summary.json:1. sha256sum of .../cert/rank3_order4_exact_haar_summary.json and .../cert/modular_haar_run/rank3_order4_exact_haar_summary.json both = 2b845725b88120f0dc84f91d1ca6aa2f77e82a857098f0d9d7ea0bd4d2f801c6, agreeing with cert/SHA256SUMS.txt:10 and :14 and differing from d3d2cb89... . The JSON has exactly 22 keys; the only hashes it binds are haar_ledger_sha256=1b9ed180... and source_topology_ledger_sha256=5337734a... — no history hash, no contractor hash. I grepped all nine C §3 hashes across the cert package, all of /home/user/WORKHOUSE, and the uploads: cert=0, repo=0, uploads=1 each (C itself). So 0/9 verifiable here.

WHY IT IS NOT A FINDING. (1) The delivered file is demonstrably a DIFFERENT run's artifact, not the one C cites. Its 22-key set is exactly the summary dict constructed at /tmp/.../cert/modular_haar_contractor.py:520-542 and written to the filename "rank3_order4_exact_haar_summary.json" at :544-547 — including modular-only fields crt_prime_count_histogram and peak_modular_factor_elements that only a CRT contractor produces. It sits in modular_haar_run/, and cert/AUDIT_REPORT.md states this modular route was "completed without using the historical decimal or rational value of D as an input. Only after completion was its result compared with the separately implemented primary run." E is therefore an independent downstream audit, not the work/rank3_order4_exact_haar_run/ package. A basename collision between two different runs' summaries is not evidence against C's row. C's chain also names artifacts E does not contain at all (exact topology ledger gzip 48abeca4..., canonical uncompressed a7f13ca1..., contractor f944bfef...), while E's source ledger is root_exact_pair_topologies.pkl.gz — different objects, not conflicting hashes of one object.

(2) C:137 cites work/rank3_order4_exact_haar_run/, which the task's own path mapping designates EXTERNAL and not present. The correct classification is (iii) UNVERIFIABLE HERE, which the finding itself half-concedes ("I cannot separate two readings") and then overstates into a failure.

(3) The delivered summary is internally sound, which argues against a packaging error: I recomputed in Fraction that D_EXACT = -13/896 + weighted_haar_sum/2 = -361008126292641364183/7250590288602460800 exactly matches its D_EXACT field; QBOUND % denominator == 0; Fraction(D_EXACT_QBOUND_numerator, QBOUND) == D_EXACT exactly; and D_EXACT + 5315003/140454 - (-1474623/1675520) == -160506019419340168451/14501180577204921600 exactly (= -11.068479463778765), matching the orchestrator's established value. C's own trivially checkable row also holds: 82384 + 82278 = 164662 (C:127).

RESIDUE, not ledger-grade. What survives is only: "C §3's nine-hash chain cites artifacts none of which is present in this repo or in certificate E (0/9), so the chain is unverifiable from the supplied materials." That is the baseline condition for every work/rank3_order4_cubic_ledger/ and work/rank3_order4_exact_haar_run/ citation in C and D, not a defect specific to line 131. Recording it as a medium-severity provenance-gap FINDING would put into the ledger an assertion that a testable row failed, when no test was actually run against the artifact C names. Nothing about this is recorded in /home/user/WORKHOUSE/ledger/ or FRONTIER.md (grep for "exact_haar"/"rank3_order4" returns nothing), so it is not already-known — it is simply not a finding.

---

### 6.16 `c-predates-is-version-string-only` — lane `citations-CD`

Refuted: the finding's headline ("no chronology is checkable in this repository"; "rests entirely on the version string") is false, and its README citation is a misreading. (1) Chronology IS machine-checkable here by reference asymmetry, with no appeal to 7 < 23. corpus-import/programs/hodge_o4_adjudication/src/ENGINE_O4_hodge_v10a7_marked_linked_scalar.py contains internal version tags only up to its own (v10a.2/.3/.4/.5/.6/.7; 46 hits on "v10a.7"), zero hits on v10a.23, v10a.24, V10A23_, V10A24_, and zero hits on "local_shift"; it DEFINES the V10A7_* env namespace at lines 5190-5200 (V10A7_GATE_START/_PROGRESS/_TOL/_SHAPE_TOL/_RAT_DEN/_DO_SHAPE/_SUPPORT_POLS/_UNBLIND/_RECHECK_Q1). ENGINE_O4_hodge_v10a24c_rootedfullt1_dualcoldoracle_a100.py CONSUMES that namespace (V10A7_TOL x22, V10A7_PROGRESS x16, V10A7_SUPPORT_POLS x8, V10A7_RECHECK_Q1 x4, V10A7_UNBLIND x3, V10A7_RAT_DEN x3, V10A7_DO_SHAPE x2, V10A7_SHAPE_TOL x2, V10A7_GATE_START x1), sets three of them in its own lines 6-8, cites "v10a.7" 25 times, and carries tags v10a.2 through v10a.24c. Its lines 11-23 are v10a7's lines 1-8 config block plus an inserted "# v10a.12: keep tiny irregular Haar contractions..." comment and four added thread env vars — a monotone edit on a shared block. The citation runs one way only: later consumes earlier, never the reverse. (2) README.md:25 does not warn that the numbering is not a chain; it says the series is "distinct experiments, not drafts of one document ... kept whole rather than version-pruned" (a warning against treating them as revisions of one artifact). README.md:21 in the same file calls it "the `Hodge_v10a2` -> `v10a32` run series". Corroborating T3 text: corpus-import/records/transcripts/Monday 531 PM.txt:2699 says the v10a.22 notebook "reruns the validated v10a.7 machinery". (3) The auditor's sub-facts reproduce but are non-probative, not decisive: git log --oneline -- corpus-import/programs/hodge_o4_adjudication/src/ returns only b594310 "Import ALL THEORY corpus under CLASS_TOPIC naming convention", and mtimes are import artifacts (v10a7 2026-08-23 21:12:03.156395910, v10a24c 21:12:03.148395910, 8 ms apart). Absence of git/mtime chronology is not absence of chronology. (4) C's substantive structural claim also checks out: grep -l local_shift over that program hits v10a23/v10a24/v10a24b/v10a24c/v10a25/v10a26 sources and notebooks and 0 times in v10a7. Residue too weak to state as a finding: reference asymmetry strictly establishes dependency order rather than wall-clock order, but dependency order is exactly what C's sentence ("predates the later v10a.23/v10a.24 local_shift branch") asserts operationally. C's cited SHA-256 for v10a7 also verifies: sha256sum = dc9ddfaab437ad4478c85eb631ed0319699c3e3304bd83b22bd31fc2f1f1107d, matching artifact C line 252.

---

### 6.17 `c-v10a7-lineage-is-float-and-fold-not-derived` — lane `citations-CD`

Every source fact in the evidence line reproduces, but the charge against artifact C does not.

WHAT I CONFIRMED IN THE SOURCE (all true):
- /home/user/WORKHOUSE/corpus-import/programs/hodge_o4_adjudication/src/ENGINE_O4_hodge_v10a7_marked_linked_scalar.py:5200 — V10A7_RECHECK_Q1 defaults to '0' (OFF). File SHA-256 is dc9ddfaab437ad4478c85eb631ed0319699c3e3304bd83b22bd31fc2f1f1107d, matching C's citation exactly.
- :5608/:5613 — in the default (else) branch e2/N/J are float() of hard-coded rationals, not recomputed.
- :5649 FOLD_A=-E2_A*N_A+J_A is float64; :5653 gates |FOLD_A - float(5315003/140454)| < 2e-8. I measured that residual: EXACTLY 0.0, i.e. 0 ulps. The gate is tautological in the default configuration.
- The identity is exact in Fractions: -(-5945/612)*(511051/124848) + (-48945521/25468992) == 5315003/140454.
- :5265-5266 _v17_rational(x) = Fraction(float(x)).limit_denominator(10^9); it prints m4_rest at :5706, :5744, :5747. M4_CAND = E4_A - V4_LINKED_MARKED is a float (V4_LINKED_MARKED at :5462 = len(_single_emb)*_v1['e4'], a cold float).
- The one recorded execution took the literal branch: corpus-import/records/transcripts/15 hour RUN.txt:9 sets V10A7_RECHECK_Q1="0"; :7773 prints 'recheck already-exact Q1 moments: False'; the [3]/[4] output there prints 'rational~' limit_denominator reconstructions throughout.

WHY THE FINDING STILL FAILS — three independent reasons, all from C's own text:

(1) C does not claim v10a7 was exact. C section 6 (lines 249-269) is headed 'Earliest direct-scalar lineage predates local_shift'; its claim is that 'Its call flow is already the same CONCEPTUAL construction'. The finding concedes all nine line citations are accurate. C's single use of 'exact' is the bullet 'exact fold -e2*N+J: lines 5646-5653' — and the fold's value IS exactly 5315003/140454 (verified above), and the label matches the source's own comment at :5646-5648 ('the entire axial fold is the separately certified rational -e2*N+J. We recompute it numerically here from the cold Gamma moments and gate the exact rational'). C's bullet points the reader at the very lines that say 'recompute it numerically'. No false statement in C is identified.

(2) The alleged omission is C's explicit position. C:296-297 says the new package 'materially improves that boundary by REPLACING FLOAT RATIONALIZATION with exact generation'; C:33 says it 'removes the numerical-rationalization objection to that prescription'; C:18 calls the whole thing 'a target-known exact replay'; C:338-345 says 'do NOT promote -11.0685 merely because its arithmetic is NOW exact ... Its remaining uncertainty is the physical/operator identity of that prescription, not its rational arithmetic.' The finding's own 'wrong' text concedes C says this. Sub-claim (2) restates C's conclusion and presents it as a gotcha against C.

(3) The repo-audit corroboration cuts the other way. C:293-295 already cites corpus-import/records/audits/07-denominator-lift.md:69-78. I read that range: it contains item 2 'Conditional exactness ... The history coefficients themselves originate as floats and are inferred with limit_denominator()' (:74) and item 4 'Injected fold ... F07 therefore does not provide self-contained provenance for every addend of m4_rest' (:76). C cites the exact lines the finding says C omits.

SALVAGEABLE, BUT IT IS A DIFFERENT FINDING AND ABOUT THE SOURCE, NOT C: the v10a.7 script's own concluding print at :5737 states '* The Q1 fold was reconstructed from cold e2/N/J and the independently exact C_A=0 theorem'. In the DEFAULT configuration — and in the only recorded run (transcripts/15 hour RUN.txt:7773) — that sentence is false: e2/N/J come from the hard-coded literals at :5613 and were never cold-recomputed, so the :5653 gate compares an identically-zero residual (0.0, 0 ulps) against a 2e-8 tolerance. That is a self-contradictory provenance banner inside the source, worth filing separately at low-to-medium severity. It does not sustain finding #18, whose kind is 'overstated' and whose subject is artifact C.

---

### 6.18 `d-audit06-is-about-v25` — lane `citations-CD`

The mechanical observable is real and I reproduced it: audit 06 is titled "Runtime forensics: `(2,5)` in v10a25" (06:1), its :50 heading is "Root cause: v25 builds the forbidden `W22` block", and :54-58 give v25 line numbers 6855-6863 / 6865-6870 / 6871-6876 / 6882-6886. D's own v10a24c numbers are independently correct (build_basis def at 6848, P 6867-6875, Q1 6877-6882, Q2 6883-6888, range ends 6889; dense W 6894-6898, herm at 6899 — D cites 6848-6889 and 6894-6899). But the inference fails on two counts. (1) D line 89 attributes only "the order trace and the later `(2,5)` failure" to 06:50-76, and both are genuinely in that range: the order trace at 06:60-74, including "P -> Q1 -> Q2 -> Q1 -> P" at 06:70-72 and "Adding `Q2 -> Q2` is a fifth magnetic step" at 06:74. D's word "later" explicitly flags the version difference, and D imports none of v25's line numbers. So there is no misattribution to correct. (2) The prescriptive half is wrong: the statement about the producing engine retaining W22 is in the very document D cited — 06:11 ("v26 then takes the wrong corrective direction: it leaves the `W22` construction in place and adds a `(5,2)/(2,5)` contractor") and 06:97 — not only at 05:96. D's cited range stops two lines before :97. Calling that a provenance gap, and prescribing a citation to a different audit file when the same statement sits inside the cited one, would put a false finding in the ledger.

---

### 6.19 `d-relabel-ignores-threshold-fragility-and-existing-check` — lane `citations-CD`

Refuted on three of its four sub-claims; the fourth is too weak to state.

(1) MISATTRIBUTED HEURISTIC. The 5x test at corpus-import/programs/hodge_o4_adjudication/src/ENGINE_O4_hodge_v10a24c_rootedfullt1_dualcoldoracle_a100.py:7339-7341 sets `scalar_verdict` only — an intermediate string printed at 'corpus-import/records/transcripts/15 hour RUN.txt':10648 ("SCALAR ORACLE RETURNS THIRD VALUE"). The FINAL VERDICT is decided at :7345-7350 and requires BOTH legs. The shape leg fails independently: dcold = |(-0.020213328886166577) - (-211835444920651/4405310420659200)| = 0.027873054295192174 against the `dcold<2e-4` threshold at :7342, a factor of 139.37. Line 7345 requires `shape_verdict.startswith('FOLDED MATRIX SUPPORTS')`, and 7347 requires scalar_verdict ending 'v10a.20 SHORTCUT'. So flipping the scalar leg alone leaves VERDICT = 'MIXED/THIRD RESULT — DO NOT PROMOTE EITHER FOURTH-ORDER CLAIM' unchanged. The FINAL VERDICT sentence at :10751 is NOT "1.2% from flipping"; it cannot flip on that margin at all.

(2) ARITHMETIC SLIP IN THE FINDING. Recomputed: dnew = 10.293333600759848, dold = 2.0827701250956414 (matching :10633-10634); dnew/5.0 = 2.0586667201519697; margin = dold - dnew/5 = 0.02410340494367169. That is 1.1573% of dold, and 1.1708% of the 0.2 ratio threshold (dold/dnew = 0.20234165197384574). The finding's "a 0.24% smaller dold would flip it" divides the margin by dnew instead of dold — wrong by 4.94x, and internally inconsistent with its own "1.17%" figure in the same sentence.

(3) FALSE PREMISE ABOUT THE LEDGER. `grep -n "MIXED\|DO NOT PROMOTE\|VERDICT" ledger/contradictions.yaml` returns zero hits. Lines 36-40 are five fields (label/value/decimal/kind/status); no FINAL VERDICT sentence exists there, so none "would be dropped with" the tag.

(4) PROVENANCE WRONG. The phrase's textual source is theory/superseded/MASTER_THEORY.md:416 ("...appears in [RUN15]'s unblind block and is rejected by both sides") and :767 (row 37, "(d) rejected by both sides"), not RUN.txt:10751. theory/MASTER_THEORY_UNIFIED_2026-08-20_v4_3.md contains neither the phrase nor the rational 160506019419340168451. This cuts toward D rather than against it: the label rests on a superseded document CLAUDE.md non-negotiable 1 forbids reading as current.

(5) THE SURVIVING FACT IS TOO WEAK. src/workhouse/invariants.py:397-400 is indeed tier=2 and its detail f-string ends "rejected by both sides", and D does not cite it (D does correctly cite src/workhouse/constants.py:426 comment and :649-655 Constant block, the other two occurrences). But the check's assertion is `abs(float(K.QUARANTINED_SCALAR) - (-11.068479463778765)) < 1e-14` — a pure decimal-transcription check whose pass/fail is independent of the label. Nothing "would have to move"; at most one detail string would be reworded. A one-word inventory omission in a recommendation D itself frames as a recommendation, not an edit, is below the bar for a ledger entry.

---

### 6.20 `d-w22-regression-already-exists` — lane `citations-CD`

REFUTED. The auditor's positive evidence all reproduces, but it does not support the conclusion, and the repository's own machine check asserts the opposite.

REPRODUCED (true): DATA_O4_OrderSchedule_Occurrence_Preflight_CPU.py header lines 13-17 read as quoted; exact_one_face_w22_sensitivity() at :317; gates at :609,:610,:614,:616 as quoted. Re-executed standalone in fractions.Fraction: full = 8/3, 1, -1/4, -1/16, -13/896, -23/12544; W22-pruned = 8/3, 1, -1/4, -1/16, -13/896, -57/50176; o4_equal=True; o5_difference = -5/7168 exactly. sha256 = 68782826d50ad6bcbb3a20d83649bfa7f66e42c5706d131361b7d189b1f99a8f, pinned at corpus-import/SHA256SUMS:358, and it is the "exact one-face preflight" row in artifact C line 143.

WHY THE CONCLUSION FAILS:

(1) SCOPE. The regression is a hand-written 4-state ONE-FACE toy model (h0=(8/3,20/3,12,32/3), layers (P,Q1,Q2,Q2), a literal 4x4 V) evaluated by an exact order-by-order scalar-P recurrence (_fraction_gelfand_scalar, :~588-604). It contains no cluster of size >= 2 and is not the blind engine. D line 91's "the blind fourth-order scalar" is the total over all rooted clusters. D itself declares the one-face sector already settled at lines 29, 63 and 215 ("Start with two-face rooted clusters because the one-face sector is already proven equal"), so the finding's own concession — "D's request survives only for clusters of size >= 2" — concedes the entire substance of line 91. What is left is not a wrong "blanket required", it is the request D actually made.

(2) MECHANISM. D's stated worry is fit contamination, not power counting: v10a24c's _v23c_fit_cluster does a float numpy degree-6 polyfit on 13 points over u in [-0.055, 0.055] (V23C_FIT_DEG=6 at ENGINE_O4_hodge_v10a24c_rootedfullt1_dualcoldoracle_a100.py:6793, V23C_FIT_N=13 at :6794, V23C_FIT_UMAX=0.055 at :6792) — D's "degree-six fit on 13 points" is verified accurate. An exact order-truncated recurrence that never fits cannot detect O(u^5) leakage into a fitted c4. The preflight is structurally incapable of discharging the concern even for one face. Separately, _v23c_build_basis's W assembly loop `for j,b in enumerate(basis)` at :6893-6897 applies W to every retained vector including layer 2, for every cluster of every size, so W22 is present in every multi-face matrix — confirming D:81 rather than refuting it.

(3) THE REPO ALREADY RECORDS THE OPPOSITE, AS A PASSING CHECK. src/workhouse/invariants.py:665-678, "FINDING: the harness can never report COMPLETE", asserts that protocol item 10 (the W22 order-schedule toggle) is hardcoded OPEN and that "the protocol has no path to closure until the engine exposes the toggle". Backed by ledger/gaps.yaml:126-130 and src/workhouse/settlement.py:127-143 (verdict_can_be_complete). Harness source settlement/mce_adjudication_harness.py:335 reads verdict["protocol"]["item10_W22_toggle"] = "OPEN (engine exposes no toggle flag)", with the completeness predicate rejecting any OPEN at :336. I executed it: S.verdict_can_be_complete() == False, so the FINDING check passes. WORKHOUSE's own machine check therefore states that the W22 toggle comparison is undischarged for the engine — corroborating D line 91 and contradicting the finding's core assertion that "the comparison already exists ... and passes".

The finding's cross-reference argument also inverts: C line 143 pins this file as a PROVENANCE document for the one-face preflight — the sector D concedes — so the pin binds the settled half, not the check D says is missing.

RESIDUAL (deliberately not offered as a corrected finding, too weak to enter the ledger): D section 2 does not cite the existing one-face W22-off regression, which is a citation-completeness nit, not an error — D covers the one-face sector separately in section 1 and section 5. Severity would be at most informational, and kind would be "artifact-incomplete", not "artifact-wrong".

---

### 6.21 `repo-raw-folded-381-ulps-unchecked` — lane `citations-CD`

I opened every cited file myself. The 381-ulp gap reproduces exactly in Fraction arithmetic, and is even computable purely from in-repo constants (QUARANTINED_SCALAR + LINKED_VACUUM_4), which is stronger than the auditor's external D_EXACT route. But the finding fails on its normative claim and on its evidence. Normatively: a float recorded from a 117,163-term float64 Haar run agreeing with its exact counterpart to 5.7e-14 relative is expected, not anomalous, and nothing in the repo or corpus asserts tighter agreement — unlike C20 (invariants.py:404), where the corpus DID claim float precision, which is what makes C20 a FINDING and this not one. The run's own two routes at :9130-9131 disagree by 10 ulps with each other, so a few-ulp standard is one the run itself cannot meet. "No invariant reads it" is the CLAUDE.md T3 default and is already surfaced by the repo's own generated catalogue at index/claims.jsonl:229. Evidentially, the finding misreads the transcript (:9112 and :9131 are one number at two print precisions, per source lines :6719 and :6738; the ulp figures 383/384 are wrong — they are 373/383) and misattributes to C §5 a treatment that section contains no diagram for, while C §8 explicitly denies the cross-branch arrow. Writing this into the ledger would register a nonexistent repo defect plus two wrong ulp counts and a misquotation of an artifact.

---

### 6.22 `C20-artifact-on-V_link-never-mentioned` — lane `corpus-value-search`

REFUTED on four independent grounds; the finding's own text concedes the documents are correct.

(1) The failure mode it warns about does not occur anywhere in the artifact set. A (/root/.claude/uploads/384fab32-8991-52ce-b2bf-4999d379e3f5/52ebdfa7-RANK3_ORDER4_MASTER_RECORD.md:61) and C (…/be0baa19-…:225) quote only the exact gate rational -1474623/1675520 with no decimal; the three cert reports in E (cert/INDEPENDENT_REFEREE_REPORT.md:26, cert/AUDIT_REPORT.md:25, cert/WORKHOUSE_RANK3_ORDER4_MODULAR_HAAR_INDEPENDENT_AUDIT_20260823.md:25) likewise quote only the fraction. The single decimal in the whole set is B (…/6a2b59cb-…:40) "+0.880098715622613"; I checked with fractions.Fraction that %.15g of float(-1474623/1675520) is 0.880098715622613 while %.15g of float(-521965902/593076541) is 0.88009871562261 — so B's quotation is unambiguous at 15 significant digits and is the gate value. Nothing propagates the artifact decimal -0.8800987156226097.

(2) The scope claim "all four documents use V_link" is false. Document D (…/e22209c0-…) never mentions V_link, -1474623/1675520, 1675520, or any decimal for it (grep over the whole file); it refers only generically to "linked-vacuum packages" and cites EXTERNAL work/fold_linked_exact/README.md:8-19,36-48.

(3) "A §2 certifies it T1" overstates A. The row at …/52ebdfa7-…:61 is titled "linked-vacuum decomposition" and its T1 statement is the factorization 1675520 = 1280*1309 = 83776*20 (which I verified exactly), not a provenance certification of V_link's value.

(4) The underlying issue is already recorded in the repo, in four places, and the repo itself classifies it as cosmetic: src/workhouse/constants.py:431-432, src/workhouse/invariants.py:402-418 (the FINDING check), ledger/contradictions.yaml:243-259 (machine_finding), theory/superseded/MASTER_THEORY.md:654. Under CLAUDE.md, "already known and recorded in the repo" is an explicit holds=false condition. The corpus print line is real and I confirmed it (corpus-import/records/transcripts/15 hour RUN.txt:7814-7815 pairs "=-1474623/1675520" with " :: -0.8800987156226097"), but it is a display artifact of the v10a.7 gate print, not something these documents touch.

Quantification note: the finding repeats the repo's "~31 ulps". Recomputed, float(-1474623/1675520) = -0.8800987156226127 and float(-521965902/593076541) = -0.8800987156226097; gap = 2.9976e-15, which is 27.0 true ulps (math.ulp = 1.1102e-16). The "31" comes from using 2**-53*|x| = 9.771e-17 as the unit (30.68), which is invariants.py:409's convention, not an ulp.

Also verified for context, exactly: D_EXACT + FOLD_EXACT - LINKED_VACUUM_EXACT = -160506019419340168451/14501180577204921600 = -11.068479463778765, i.e. the exact chain in C uses the gate value, not the artifact.

Residual truth, too weak to state as a finding: none of the four documents cites C20. Since no document quotes an ambiguous or wrong decimal, that is an omission of a resolved cosmetic note, not a provenance gap, and writing it into the ledger would cost more than it informs.

---

### 6.23 `F07-label-collides-with-corpus-feature-id` — lane `corpus-value-search`

REFUTED on three independent grounds, each checked against primary sources.

(1) The premise that "F07" denotes only a feature node and never the branch scalar is false in the corpus itself. Inside the F08 audit, /home/user/WORKHOUSE/corpus-import/records/audits/08-rooted-adjudication.md:52-54 reads: "It hard-codes the claimed completed F07 results: D_EXACT = -361008126292641364183/7250590288602460800; M4_EXACT = -160506019419340168451/14501180577204921600." The same file uses "Exact F07 scalar references D_EXACT and M4_EXACT" (:66), "a verdict selecting the F07 m4_rest" (:73), "the new F07 scalar" (:83), "F07 supplies exactified two-step histories and the candidate D_EXACT/M4_EXACT" (:117); 07-denominator-lift.md:83 says "F08 treats the F07 exact scalar as the target". The documents' "F07 branch"/"F07 total" is exactly that M4_EXACT: B:134 prints -160506019419340168451/14501180577204921600, byte-identical to 08-rooted-adjudication.md:54, and orchestrator-established as D_EXACT+FOLD-V_link. The documents therefore inherit the corpus's own naming rather than colliding with it.

(2) The attribution is corpus-correct, not a merge of two nodes. F07's stated responsibility at 00-features.md:25 is "Exactify two-step histories and convert the factorized Haar topology sum to rational D_A and m4_rest" — the branch quantity the documents name. Independent corroboration: D:120 tabulates "Exact F07 | 117,161 orientation-sensitive endpoint-Haar keys", matching 02-duplication-report.md:49 ("F07 has 117,161 Haar-pair topologies") and 07-denominator-lift.md:78,121. B:25-26's phrase "the one engine that yields an exact F07 per-size decomposition (v10a.21r)" parses as a per-size decomposition OF the F07 total, which is precisely what 00-features.md:26 and 08-rooted-adjudication.md:66,73,83 say F08 does with the F07 scalar. It is not a claim that v10a.21r is F07.

(3) The specific sub-claim "B §4 attributes the F08 adjudicator's gates to F07" is directly contradicted by B §4. B:124 names the engine "ENGINE_O4_hodge_v10a21r_adjudicator_only_same_kernel.py"; B:135-136 quote the gates verbatim as gate('v10a.21 minimal marked-history ledger sums to exact v10a.20 m4') and gate('v10a.21 full rooted recursive linked sum equals exact v10a.20 m4'). I confirmed both strings in the repo at corpus-import/programs/hodge_o4_adjudication/src/ENGINE_O4_hodge_v10a21r_adjudicator_only_same_kernel.py:383 and :447, with D_EXACT/M4_EXACT at :42-43. B thus reproduces the producer(v10a.21=F08)/target(v10a.20=F07) split exactly right.

(4) The "unquoted verdict" add-on is also weak. The corpus F07 verdict is explicitly mirror-scoped ("none stores a completed output in this project mirror … not verified evidence here", 00-features.md:25) while the documents assert an EXTERNAL completed package under work/rank3_order4_exact_haar_package_verify/ — unverifiable in this repo, but not contradicted by a mirror-scoped verdict. And the documents do carry the substantive caution: A:39 tags the scalar QUARANTINED_SCALAR, A:115-116 and B:122-152 reproduce the v10a.21r circularity and the maintainer's retirement, matching 08-rooted-adjudication.md:104 ("Target coupling").

Residual true kernel, too weak to state as a finding: A, B and D contain zero occurrences of the string "F08", so a reader mapping them onto the feature register must infer v10a.21/v10a.21r = F08 themselves. That is citation incompleteness, not a graph conflict, and it does not make any document statement wrong.

---

### 6.24 `W22-O4-nullity-is-size-independent-in-the-corpus` — lane `corpus-value-search`

REFUTED. I reproduced every cited number independently but the finding's conclusion does not survive.

(1) The Motzkin gate is real and I reproduced it. My own reimplementation of corpus-import/programs/hodge_o4_adjudication/src/DATA_O4_OrderSchedule_Occurrence_Preflight_CPU.py:124-147 returns exactly 9 closed four-step P->P walks, max layer Q2, walk_blocks == O4_BLOCKS (:53) = {(0,0),(0,1),(1,0),(1,1),(1,2),(2,1)}, (Q2,Q2) absent at order 4 and first present at order 5. Gates :606-611 confirmed. I also recomputed exact_one_face_w22_sensitivity (:317-338) from scratch in Fractions: full = (8/3, 1, -1/4, -1/16, -13/896, -23/12544), pruned c5 = -57/50176, o4_equal True, o5_difference = -5/7168; gates :614-616 confirmed; -13/896 + 39/1280 = 143/8960.

(2) A section 2 row 3 -- one of the two quoted targets -- is ACCURATE. It cites DATA_O4...:614,616, which are precisely the one-face gates, for a one-face statement. There is no overstatement to find there.

(3) A does NOT omit the geometry-free exclusion. A:89 says F07 and the canonical prescription are "W22-free by construction"; A:102 (Knob A) says "W22 unschedulable". A credits the schedule gate; it declines to call it a proof of nullity for the blind branch's numbers -- which is a different, and correct, judgement.

(4) A's load-bearing clause is CORRECT, and the finding misidentifies its referent. "Multi-face W22-O4-safety is fit-argued, not exactly gated" is about the BLIND branch, which never does order-truncated perturbation theory: ENGINE_O4_hodge_v10a24c_rootedfullt1_dualcoldoracle_a100.py:6934-6946 extracts c4 from a degree-6 numpy polynomial fit on 13 points over |u| <= 0.055 (V23C_FIT_UMAX=0.055, V23C_FIT_DEG=6, V23C_FIT_N=13 at :6792-6794), guarded only by fit_stability = |c[4]-c2[4]| between the full-range and inner-range fits (:6941-6945). Its basis builder applies W to every retained vector with no layer mask (:6895-6898, over layer2 too), so W22 IS in the blind matrix. A Motzkin theorem about the exact order-4 Taylor coefficient does not transfer to a finite-u polynomial fit: W22's O(u^5) contribution leaks into the fitted c4. D section 2 (:91) states this identical caveat and prescribes the identical remedy ("An exact order-truncated W22-off comparison is therefore required"), so the finding's appeal to D actually supports A rather than contradicting it.

(5) The finding itself overreaches. enumerate_closed_layer_walks HARDCODES the +-1/0 layer-step premise (:135, `for nxt in (here-1, here, here+1)`) rather than deriving or verifying it; it is a theorem about an abstract layer graph, not a per-cluster verification. The preflight contains zero multi-face/two-face/size-2/cluster-size references (case-insensitive grep count = 0), and declares its own scope at :629 as "M3 O4 order schedule and occurrence preflight only; no m4 or publication claim". Saying the gate "therefore holds for every cluster" is a model-level inference the corpus does not gate.

(6) Partly already recorded in the repo, in the OPPOSITE direction from the finding: src/workhouse/invariants.py:665-679 is an existing FINDING check ("the harness can never report COMPLETE") whose stated cause is that protocol item 10, the W22 order-schedule toggle, is hardcoded OPEN (settlement/mce_adjudication_harness.py:43 and :335), mirrored at ledger/gaps.yaml:127-131 and enforced by src/workhouse/settlement.py:128-142. The repository's own machine check already treats the W22 order-schedule toggle as un-exercised, which is nearer A's framing than the finding's.

Residual defect, below ledger threshold: A:90-91's phrase "The corpus proves W22 is O4-null only at one face" conflates "only exact instantiation" with "only proof" -- the schedule-level exclusion at :606-611 is geometry-free while the only end-to-end exact instantiation is the fixed 4x4 one-face toy. A itself corrects this at section 5:130-133 ("the corpus proves one-face W22-safety exactly and has a multi-face fit-stability guard"), in a document self-labelled T3 (A:3). It changes no number, no tier and no conclusion, so it is a wording nit, not a finding.

---

### 6.25 `blind-per-size-table-does-not-sum-to-printed-total` — lane `corpus-value-search`

The arithmetic in the finding is correct and I reproduced it independently, but its conclusion (kind: artifact-wrong, "the blind table does not close") is refuted; what survives is a presentation nit too weak to enter the ledger.

WHAT I REPRODUCED. /home/user/WORKHOUSE/corpus-import/records/transcripts/15 hour RUN.txt:10620-10625 verbatim: +0.0159598214286, -0.403971702978, -0.178800648136, -1.3933298959e-14, -2.85049761573e-14, -0.208333333333. Float sum in printed order = -0.7751458630184425 (exact decimal sum -7751458630184424382751163/10^25, same float). TOTAL at :10626 = -0.7751458630189173. gap = +4.748423876321795e-13; math.ulp = 1.1102230246251565e-16 -> exactly 4277 ulps. The auditor's numbers are right.

WHY IT IS REFUTED.
(1) The residual is fully inside the transcript's own 12-significant-figure print budget, and the dominant term is identifiable. Size 6 is -5/24; printed as -0.208333333333 it is high by +3.3333e-13. Size 1 is 143/8960 (the one-face gap the repo certifies, named at A:59 and B:69); printed as 0.0159598214286 it is high by +2.857e-14. Those two alone are +3.619e-13 of the +4.748e-13. The unexplained remainder is +1.129e-13, against a +/-5e-13 budget for size 2 and +/-5e-13 for size 3. Nothing is left over. The run's internal full-precision values do sum to the TOTAL; only the display cannot show it.
(2) Reductio on the same table. Applying the finding's method to the c2 column of :10620-10625 gives 0.03594771241795225 vs printed TOTAL m2 = 0.03594771241824929: gap -2.970e-13 = 42808 ulps, ten times worse than the m4 case. Yet 15 hour RUN.txt:10628 reads "[PASS] v10a.23 independent finite-cluster oracle recovers m2=11/306" (and :10629 likewise for m3, 2058 ulps). A method that flags a 42808-ulp "failure" in a column the source certifies as 11/306 is measuring the print format, not the mathematics.
(3) A:62 is not false on its natural reading. "| blind table closes | T2 | Sigma per-size c4 = oracle -0.7751458630189 (:10626) |" names the oracle by its value — exactly parallel to A:59, which names 143/8960 the same way — and asserts sum = oracle. That assertion is true of the run's quantities. A's real defect is that it states no tolerance, which A:53 ("Every row is T1 (exact) or T2 (numerical), reproducible via the check") promises and CLAUDE.md's T2 definition requires. That is a low-severity specification gap, not "the row is false".
(4) The finding's criticism of B is unsupported. B:195 states the target as "-0.775145863..." — nine decimals with an explicit ellipsis. The sum -0.775145863018... matches to nine decimals, so B's check 5 passes as written, and quoting to the precision a 12-sig-fig source actually supports is correct behaviour, not "hiding the residual". (B's script f07_twoface_adjudication_check.py is not in the extracted certificate zip, so its literal tolerance is UNVERIFIABLE here.)
(5) Ledger-pollution risk. This repo already tracks the 13-digit string 7751458630184 as Hamer's 8*a_4 and already records that it "diverge[s] at index 12" from the oracle 7751458630189173: /home/user/WORKHOUSE/src/workhouse/settlement.py:51, /home/user/WORKHOUSE/src/workhouse/invariants.py:646-649, /home/user/WORKHOUSE/ledger/gaps.yaml:118-120, /home/user/WORKHOUSE/ledger/contradictions.yaml:51, /home/user/WORKHOUSE/literature/index.yaml:495-496. Filing a second, unrelated "...630184 vs ...630189" under a heading that reads as a numerical inconsistency in RUN15 would be actively confusing.

SIDE CORRECTION TO THE ORCHESTRATOR'S PREAMBLE (not my lane, but load-bearing here). The stated fact that the blind per-size table "sums (in printed order) to -0.77514586301840004978, which equals 8*HAMER_A4_NUM = 8*(-0.0968932328773) to the last float bit" is wrong. 8*(-0.0968932328773) = -0.77514586301840004978, but the table sums to -0.77514586301844246030. They differ by -4.241e-14 = 382 ulps. The finding under review has the correct sum; the preamble does not.

WHAT WOULD SURVIVE, if anyone wants it (low severity, presentation only): A:62 quotes the target to 13 significant figures from a table printed to 12, and states no tolerance for a row labelled T2. The strongest reproducible statement from :10620-10626 is agreement to 4.748423876321795e-13 absolute (4277 ulps) / 6.1e-13 relative, which is print-limited, not run-limited.

---

### 6.26 `branch-gap-10.293-is-printed-in-the-corpus` — lane `corpus-value-search`

Refuted on both legs, though its mechanical sub-facts check out.

VERIFIED TRUE (reproduced independently): the line is verbatim at /home/user/WORKHOUSE/corpus-import/records/transcripts/15 hour RUN.txt:10633; the literal string 10.293333600759848 occurs in exactly three files (that line, "15 hour RUN. results.txt":2874, and the stored OUTPUT of code cell index 1, execution_count 1, of corpus-import/programs/hodge_o4_adjudication/notebooks/NB_O4_hodge_v10a26_factor52complete_exactsw_rootedoracle_a100_alt2.ipynb:2910). Stronger than stated: "15 hour RUN. results.txt" (2992 lines) and the notebook output (2993 lines) are line-for-line IDENTICAL and both are a contiguous block at the tail of "15 hour RUN.txt" (lines 7760-10752) -- one run stored three times, zero independent support. The value is correctly rounded: float(-0.7751458630189173) - float(-160506019419340168451/14501180577204921600) = 10.293333600759848, 0.17 ulp from the exact rational difference. And `workhouse search 10.293333600759848` does return "no claim matches" (also with --corpus).

LEG 1 FAILS -- the "overstated / presented as the session's discovery" charge is contradicted by the documents' own words. A:10-11 "two exact/measured branch values that disagree by 10.293; THIS SESSION LOCALIZED the entire disagreement to the multi-face sector"; A:80 "Localization (this session's contribution): the entire 10.293 gap lives in..."; B:21-23 "They disagree by 10.293333600759848. THE DECISIVE NEW FACT IS that the two branches agree exactly at one face"; B:47 "All values re-verified this session against corpus-import/records/transcripts/15 hour RUN.txt". Both documents credit the corpus for the gap and explicitly reserve novelty for the one-face localization. "The real, open branch conflict" (A:42, B:41) is a status characterization, not a discovery claim.

LEG 2 FAILS -- "in zero repository claims / the reportable fact is the registration gap" is misleading. The conflict IS registered; only a derived pairwise difference is not indexed. ledger/contradictions.yaml:35-39 lists "quarantined shortcut", value -160506019419340168451/14501180577204921600, decimal -11.068479463778765, status rejected-by-both, in the same C1 quantity list as m_Gamma^(4) = -0.7751458630189173 (:32-34). src/workhouse/constants.py:426-427 defines QUARANTINED_SCALAR with the comment "Rejected by both sides; recorded so it is never silently resurrected". src/workhouse/invariants.py:397-401 is a live T2 check on its decimal. `workhouse search -- "-11.068479463778765"` returns 2 claims; `workhouse search -- "-0.7751458630189173"` returns 11. Both operands are registered and findable; probing for their subtraction is a bad probe of a value-indexed registry, not evidence of a registration gap.

MINOR INACCURACY in the evidence line: "on a line the documents themselves cite for other purposes" is wrong for the accused documents. A:58,62,168 and B:54,192,195,232 all cite :10620-10626, not :10633. Only document D (e22209c0...:27) cites a range (:10619-10640) that contains it.

SALVAGEABLE RESIDUAL, but it is a DIFFERENT claim the finding does not make: the repo files the shortcut as rejected-by-both / falsified (contradictions.yaml:39, and `workhouse search` reports status "falsified - record-backed"), whereas A:39 and B:37 treat it as a live rival branch and A:137 recommends relabeling it away from "rejected-by-both". That repo-vs-document STATUS disagreement is worth raising on its own terms; the present finding as written is not.

---

### 6.27 `knob-B-and-the-five-requirements-are-existing-protocol-items` — lane `corpus-value-search`

REFUTED. The repo half of the evidence line reproduces; the charge against the documents does not, and two of the finding's own supporting assertions are wrong.

WHAT REPRODUCES (I opened all of it):
- corpus-import/programs/hodge_o4_adjudication/README.md:27 heading "What the next run must do (corpus §15.1 — all eleven, or it does not count)"; :30 item 2, :31 item 3 "All 203 × 3 = 609", :32 item 4 rooted Möbius on the vacuum-subtracted object, :34 item 6 no historical target, :35 item 7 cold 3,895-topology Stage-3H, :38 item 10 "The `W₂₂` order toggle across all 33 rooted classes", :45 "zero physics contractions ... It is the designated decider". All verbatim.
- settlement/mce_adjudication_harness.py:43 and :335 verbatim. src/workhouse/invariants.py:665-678 is the T1 FINDING "the harness can never report COMPLETE"; `workhouse search W22` returns it, passing.

WHY THE FINDING FAILS:

1. "A and B present the list as newly derived" is contradicted by the documents at the exact lines the finding cites. B:159 opens §5 with "Per `WORKHOUSE_RANK3_ORDER4_F07_VS_BLIND_..._STRUCTURAL_TRACE §9`" — explicit attribution to a sibling document, not a derivation claim. A:101-103 introduces Knob A as "(D §9: typed physical P/Q blocks or a proven isometry; W22 unschedulable; vacuum before Möbius; all 3 polarizations; map to Stage-3H)" — also attributed to D §9. Neither presents the list as its own.

2. A:113's "none of the five documents could draw alone" is scoped to the session's own document set, not to the corpus. A §0:19-27 enumerates that set (A–F plus the check script). The sentence is a synthesis claim over those documents; it makes no priority claim against corpus §15.1. Reading it as a novelty claim over the corpus is the auditor's interpolation.

3. The documents demonstrably read the eleven-item block. D:125 (in §4) cites "hodge_o4_adjudication/README.md:27-45" — a range that *is* the eleven-item list plus the "zero physics contractions / designated decider" status. The finding concedes this for the 609/3895 counts but does not follow it through: the same citation covers items 1-11 including item 10.

4. A explicitly credits the corpus for the W22 facts and retracts its own stronger framing. A:90-92 "The corpus proves W22 is O4-null **only at one face**; multi-face W22-O4-safety is fit-argued, not exactly gated". A:130-133 "**Correction, my own W22 framing.** 'W22 flips the suspect' was too strong. The corpus *proves* one-face W22-safety exactly and has a multi-face fit-stability guard." That is the opposite of the posture the finding charges.

5. The proposed test is explicitly scoped *down* from the eleven-item protocol, not offered as a substitute for it. A:111 "Both outcomes are decisive, finite, and far cheaper than the 609-cluster full-T1 run." Item 10 is a toggle "across all 33 rooted classes"; Knob B is a two-face W22-off recomputation — a strict sub-case, not the same object.

FINDING'S OWN ERRORS:

6. The "almost one-to-one onto items 2, 3, 4, 6 and 7" mapping does not hold. Checking each of B §5's five against README:29-39: B3 (vacuum before rooted Möbius) ≡ item 4 — match. B5 (3,895 Stage-3H → unshifted 189-record kernel) ≡ item 7 — match. B4 (all three T1 polarizations) is only the "×3" inside item 3's 203×3=609, partial. B1 (typed physical P/Q1/Q2 blocks or a proven isometry from the trace-history representation) is a state-space requirement; item 2 is the occurrence schedule — they touch only via the harness's own gloss at :39 ("engine self-test gates (P->W1->R1->W2->R2)"), partial. B2 (W22 unschedulable) maps to item **10**, which the finding excludes from the list. Item **6** (no historical target in the data flow) has *no* counterpart among B's five. So the list is off by one at each end: 2 clean matches, 2 partial, item 6 spurious, item 10 omitted.

7. "The engine that satisfies them ... also already exists" is false on the load-bearing item. `grep -c -i W22 corpus-import/programs/hodge_o4_adjudication/src/DATA_SU3_Exact_MarkedCluster_m4_Colab.py` returns **0** — no toggle, no flag, no mention. Its header (:1-19) does support four of B's five (typed P→W1→R1→W2→R2 at :6, endpoint- and polarization-resolved full-T1 moments at :9-10, rooted-cluster assembly at :8-9, "no fitted targets, retired coefficients, or Hamer data" at :17). But the repo's own passing T1 check says exactly why the fifth is missing: invariants.py:673-677 "protocol item 10 (W22 order-schedule toggle) is hardcoded OPEN ... the protocol has no path to closure until the engine exposes the toggle", and harness:335 `"OPEN (engine exposes no toggle flag)"`. A ledger entry saying the extant engine satisfies the W22 requirement would directly contradict a passing check in this repository.

8. B §5 item 2's factual grounding checks out against primary source, so there is no factual error to fall back on: ENGINE_O4_hodge_v10a24c_rootedfullt1_dualcoldoracle_a100.py:6793-6794 set `V23C_FIT_DEG=6` and `V23C_FIT_N=13`, and :6943-6947 (`_v23c_fit_cluster`) does the degree-6 polynomial fit with the inner-window `fit_stability` guard — exactly "a degree-6 fit on 13 points" as B:169 states.

RESIDUE, too weak to state as a finding: none of the four .md documents names §15.1, the eleven-item protocol, settlement/mce_adjudication_harness.py, or the existing FINDING check by name, so a reader of A alone would not learn that a W22 toggle is already protocol item 10 and already reported permanently OPEN here. That is a citation-completeness gap in A, mitigated by A's attribution chain to D §9 and D:125's citation of README:27-45. It is not an overstatement, and it does not support the finding as written.

---

### 6.28 `m4-is-a-forbidden-name` — lane `corpus-value-search`

REFUTED. (1) The rule is pair-scoped, not a blanket ban on the token `m_4`. Every statement of it in the repo names the collision, not the string: ADR 0002 Decision 2 (docs/decisions/0002-anchoring-is-not-a-dispute.md, "Writing \"two `m_4` values\" is forbidden"); ledger/contradictions.yaml:22 (`forbidden: "two m_4 values"`, why at :24 "Naming BOTH \"m_4\""); CLAUDE.md:58; README.md:202 ("Calling BOTH \"m_4\""); src/workhouse/frontier.py:429; and both `why` fields the finding cites — ledger/symbols.yaml:38-41 ("Calling THIS AND m_Gamma^(4) BOTH \"m_4\" regenerates a contradiction that does not exist") and :55 ("same collision as q_band^(4)"). The failure the rule names is a FALSE contradiction between two differently-anchored coordinates. (2) B/D's pair is not that pair, and both documents explicitly disclaim it. D:27 — "The genuine unresolved conflict is therefore **exact F07 branch versus blind linked-cluster branch**, not the old `q_band` versus `m_Gamma` naming issue." D:182 — "Keep C1's narrow resolution that `q_band^(4)` and `m_Gamma^(4)` are differently anchored coordinates ... unaffected by the exact F07 result." q_band^(4) (-2.857915988114559, constants.py:197) is never one of the two labelled quantities. (3) Both symbols carry disambiguating subscripts (F07 / blind), and B section 1 is headed "The three scalars (do not conflate)" (B:33) — so the claimed "header contradicts the body" does not follow; the scope line names a quantity family and the body separates its members. (4) No machine check flags this. src/workhouse/search.py:211 is an exact-string test (`query.strip().lower() == forbidden["text"].lower()`), so neither `m₄,blind` nor `m_{4,\mathrm{blind}}` triggers the banner; tests/test_ledger.py:41-47 only asserts the register keeps the wording, and tests/test_search.py:48-59 only asserts the bare query matches. Nothing in the repo scans documents for the token. (5) The repo and its own primary corpus use `m4` for exactly this value: corpus-import/records/transcripts/15 hour RUN.txt:10627 ("TOTAL m1/m2/m3/m4 = 1.0 0.03594771241824929 -0.4371355568371267 -0.7751458630189173") and :10632 ("independent linked m4 = -0.7751458630189173"); theory/superseded/MASTER_THEORY.md:568; and live code settlement/mce_adjudication_harness.py:27-28, 42, 44, 267-303, which uses `m4` as a neutral key. Under the finding's strict reading the repository violates its own rule in three places, which is the CLAUDE.md maintainer's-rule signal that the reading, not the documents, is wrong. Verified: ledger/symbols.yaml:36-41 and :53-55 do carry the forbidden entries, and `./.venv/bin/workhouse search m_4` does print the red banner twice — the finding's evidence line is accurate; its inference from that evidence is not. Separately, and NOT part of this finding: 15 hour RUN.txt:10633 labels -11.068479463778765 "quarantined scalar shortcut" and src/workhouse/constants.py:426 comments it "Rejected by both sides; recorded so it is never silently resurrected", while B:37/205 and A:39/137 rename it M4_SHORTCUT = "F07 branch" and recommend relabelling it away from rejected-by-both — that is a promotion-of-a-quarantined-value concern worth a separate finding, but it is not the naming-collision claim #122 makes.

---

### 6.29 `a2-a3-corroborations-carry-no-information` — lane `hamer-circularity`

REFUTED. I reproduced the arithmetic but it does not support the conclusion, the transcript citation is read backwards, and the repo's own registry disproves the reconstruction hypothesis.

1. The numerics reproduce but are non-probative — they are guaranteed, not observed. All four round-trips are exact under both ROUND_HALF_UP and ROUND_HALF_EVEN: 11/612 = 0.017973856209150326... -> 0.0179738562092 = HAMER_MA_NUM[0]; -109151/998784 = -0.109283889209278... -> -0.109283889209 = HAMER_MA_NUM[1]; -217/2040 = -0.106372549019607... -> -0.106372549020 = HAMER_MS_NUM[0]; -54049/2080800 = -0.025975105728565... -> -0.0259751057286 = HAMER_MS_NUM[1]. My half-ulp-times-bridge ratios: 0.9935, 0.5570, 0.7843, 0.6814 (auditor said 0.994, 0.557, 0.784, 0.681 — agrees). But "all under 1" is a tautology, not evidence. A 12-significant-figure decimal that agrees with a rational to within half an ulp IS, by definition, that rational's correctly-rounded 12-figure image. So exact round-tripping is a NECESSARY consequence of the corroboration claim itself and has exactly zero power to discriminate "read off the 1989 table" from "reconstructed from the rational". The auditor presents a logical identity as if it were a measurement.

2. The registry's composition refutes reconstruction. src/workhouse/constants.py:238-256 registers 18 Hamer decimals (HAMER_MA_NUM, HAMER_MS_NUM, HAMER_MT_NUM, orders n=2..7 each). Only the 4 cited have any corpus preimage. The other 14 cannot be round-trips of anything the program holds: the program's series stops at order 4, so MA orders 5,6,7 (-0.06981386378, -0.041089676435, -0.017154548532) and MS orders 5,6,7 have no preimage by construction, and constants.py:253 labels the entire MT column "external data with no in-program counterpart yet". A single table read explains all 18; reconstruction explains 4 and needs an unnamed source for 14.

3. The transcript the finding cites contains its own disproof. "corpus-import/records/transcripts/Monday 531 PM.txt":8843-8853 records the FULL M_A column, orders 0 through 7, and the orders 5/6/7 entries -0.069813863780, -0.041089676435, -0.017154548532 equal HAMER_MA_NUM[3],[4],[5] exactly while having no corpus preimage. The same block cites its source as a full-text PDF: "Hamiltonian_strong_coupling_expansions_f.pdf" at :8812, :8856, :9712, and ":6802 Hamer, Physics Letters B 224 (1989) 339-342; full-text table."

4. The 7205 quote is applied in the wrong direction. In context (:7195-7234) "those" refers to the PROGRAM's targets, not to Hamer's digits: ":7205 those are not results produced by the current run yet. They are already hard-coded in your source as known regression targets... :7213 Hamer's transformed published coefficients match the known m_2, m_3 targets embedded in your program... It does not yet constitute independent agreement from this run." That is a caution that one intermediate run had m_2/m_3 preloaded as "blind regression gates" and had not yet recomputed them (the transcript says the independent computation arrives at "section [16] ROOTED INCIDENCE TRANSFORM"). It says nothing about the Hamer decimals being generated from D_3.

5. The residual true kernel is already declared in the repo, so this is not a hidden circularity. literature/index.yaml:464-471 states plainly: "Publisher copyright: the paper is NOT stored. A maintainer-supplied copy of the published article was read on 2026-08-21, Table 1 was verified against the rendered page image (not OCR), and the digest below pins the copy read", with source_sha256 at :471. Mirrored at src/workhouse/constants.py:226-231. This is the repo-wide "pinned, not stored" convention (11 occurrences in literature/index.yaml, e.g. :143, :320, :367, :573, :620, :695, :793, :950). index.yaml:505-506 already separates the earlier local transcription from the pinned primary ("With the table pinned, that argument no longer rests on a transcription"), and src/workhouse/invariants.py:1352-1357 already flags the M_S n=3 target as a corpus certificate "not independently re-derived here".

The checks themselves (invariants.py:1317-1362) are honest T2: stated bounds, measured gaps printed in the detail line. The finding, if written into the ledger, would downgrade four legitimate falsifiable external checks on the strength of a tautology and a reversed quotation. Note the finding's own concession about a_4 cuts against it: a_4 has no preimage and sits in the same three-row block of the same table read as a_2 and a_3 — table rows are not read selectively.

---

### 6.30 `a4-last-digit-is-the-discriminator` — lane `hamer-circularity`

Re-derived everything with fractions/Decimal at prec=12. The evidence line's arithmetic is correct: m_4/8 = -0.09689323287736466283615044403632055 exactly (M_GAMMA_4_NUM = -0.7751458630189173); round12 = -0.0968932328774 under both ROUND_HALF_UP and ROUND_HALF_EVEN; registry a_4 = -0.0968932328773 (constants.py:239,243); diff 9.9994e-14; reg - m_4/8 = 6.4657e-14, x8 = 5.1725e-13. The four round-trips also check: 11/612 -> 0.0179738562092 = HAMER_MA_NUM[0]; D_3/4 = -109151/998784 -> -0.109283889209 = HAMER_MA_NUM[1]; -217/2040 -> -0.106372549020 = HAMER_MS_NUM[0]; -54049/2080800 -> -0.0259751057286 = HAMER_MS_NUM[1]. And trunc12(11/612) = 0.0179738562091 != registry, as claimed. So the auditor made no arithmetic error. The finding fails on inference and on novelty, four ways. (1) The alternative it dismisses reproduces a_4 exactly: trunc12(m_4/8) = -0.0968932328773, bit-for-bit the registry value. There is a one-step arithmetic route from the program's own float to a_4, so the fact is one printed ulp from neutral, not a discriminator. (2) The dismissal is a non-sequitur. The hypothesis being defeated is that a local transcriber manufactured a_4 from the program's m_4; Hamer's 1989 printing convention places no constraint at all on what such a transcriber would do. MA n=2 establishes only that Hamer rounded. (3) The repo's own precedent contradicts even the weaker premise that one round-trip fixes a table's convention: src/workhouse/invariants.py:1469-1471 records that in KPS eq. (6a) "the n = 2, 3, 5 entries are truncations rather than roundings of the exact decimal, hence the full-ulp rather than half-ulp bound" — one printed equation mixing both conventions. (4) It is redundant with recorded, strictly stronger material. a_4's provenance is not inference: literature/index.yaml:490-497 and invariants.py:1284-1292 record that on 2026-08-21 the four-page primary was digest-pinned (source_sha256 96b3ec0f..., index.yaml:470) and Table 1's M_A order-4 entry read "-0.968932328773 E-1" off the rendered page image rather than OCR, digit for digit; the published check at invariants.py:1296-1315 machine-asserts the 64-char digest and the single verified supplies-value edge. The circularity question also already has its own recorded answer at literature/index.yaml:499-505: "the oracle that produced m_Gamma^(4) ran with the historical target disabled and recovered m_1, m_2, m_3 first, so agreement with this paper is substantive rather than internal bookkeeping." A pinned primary read from the page image beats a rounding argument that truncation reverses. Also note the four round-tripping entries were transcribed on 2026-08-21 from that pinned copy, whereas a_4 predates the repository as a notebook transcription (corpus-import/corpus/MASTER_THEORY_UNIFIED_2026-08-20_v3.md:221, corpus-import/corpus/GLUEBALL_DETAILED_FORMULA_DOCUMENT_2026-08-20_v3_1.md:95, corpus-import/records/transcripts/Monday 531 PM.txt:6852) — so they are not products of one common "rule" whose failure on a_4 could mean anything. Putting this in the ledger as "the cheapest available answer to the circularity question" would install an argument a skeptic refutes in one line by truncating.

---

### 6.31 `hamer-a4-not-circular` — lane `hamer-circularity`

REFUTED AS A FINDING (the underlying facts largely reproduce; the thing being recorded does not qualify as a finding).

1) The candidate states its own `wrong:` field as "Nothing." It identifies no discrepancy, no transcription slip, no arithmetic error. Under CLAUDE.md "When a check fails" (steps 3-4), a FINDING is reserved for "a real discrepancy in the corpus," recorded as an explicit `FINDING:` check asserting the discrepancy. A confirmation that an existing ledger sentence is correct is the opposite of that.

2) The substance is ALREADY RECORDED, in stronger and machine-checked form:
 - ledger/contradictions.yaml:55-61 (`by_construction_caveat`) already makes the exact two-part distinction: "(1) The oracle value itself is an independent blind reconstruction - substantive. (2) The final assembled mass-kernel rest value is FORCED... See C22." The candidate's conclusion restates this.
 - literature/index.yaml:454-497 pins HAMER_1989 (source_sha256 96b3ec0f6e2d...), records Table 1 M_A order-4 verified "digit for digit" against the rendered page image, status `verified`, states the 5.17e-13 gap and already calls it "the strongest external validation the program has, now primary-source rather than a local transcription."
 - src/workhouse/invariants.py:1280-1315 is a live T2 check asserting the pinned digest, the single supplies-value/verified edge, HAMER_MA_NUM[2] == HAMER_A4_NUM, and gap < HAMER_TOLERANCE; invariants.py:388-394 checks the same bridge.
 The external half was therefore already promoted above T3; the candidate adds no tier.

3) Two of the three grounds cannot promote anything. Grounds (2) TEMPORAL ORDER and (3) NO PREIMAGE rest entirely on prose inside a chat transcript. I read them and they do say what is claimed - "Monday 531 PM.txt":6768 "Modern value near -11.06848: strongly expected"; :6778-6784 "There is a published m4. I missed it, and my previous expectation of -11.06848 was wrong"; :7228 "Hamer's -0.7751458630184 is now a prediction against which the unfinished run can be tested"; :7233 "The decisive evidence will be the future line: TOTAL m1/m2/m3/m4 = ..." (that line is "15 hour RUN.txt":10626). By CLAUDE.md's own table these are T3: a document says so and nothing checks it. "No document is authority" applies to a transcript's self-report of its own blindness too.

4) Ground (1), the only machine-checkable part, reproduces but was UNDER-checked. I re-ran it plus the repo's own EXTENDED_CONTAMINATION_STRINGS list (src/workhouse/settlement.py:47-56) over all 10751 lines of "15 hour RUN.txt":
 grep -ci hamer = 0 (confirmed; corpus-wide "hamer" appears only in "Monday 531 PM.txt" x94, 819gptultralocal.txt x8, SOURCEOFGOD.txt x6, #-Final-unified-theory.txt x1).
 7751458630184 = 0 hits; 0968932328773 = 0; 7751458630417 = 0; 2857915988 = 0; 1106847946 = 0.
 7751458630189173 -> 10626, 10632, 10748 only (own output).
 160506019419340168451 -> 7699, 10633; 7250590288602460800 and 20721577909065127111 -> 7700, 10634; 4405310420659200 and 211835444920651 -> 7701, 10636; 0827701250956414 -> 10634 only.
 Every rival-target string first appears at 7699-7701, inside "[17] FINAL FOURTH-ORDER UNBLIND" (header 7695-7698), strictly after totals[4] is computed at 7674-7681. The pre-unblind AssertionError gate is at 7689-7692; the m1/m2/m3 gates at 7683-7685 print PASS at 10627-10629. "historical m4 target : NOT LOADED" confirmed at :6034 (source) and :7771 (output). So the scan is stronger than reported - and still not a finding.

5) Even so it is necessary-not-sufficient, and the repo already says why. settlement.py:126-133 and the live FINDING at invariants.py:653-663 record that a single-file contamination scan is bypassed by "an engine that imports a helper module, loads a JSON/npz, or restores from the sqlite checkpoint." This run is in that class: "15 hour RUN.txt":6785 `V26_CHECKPOINT=os.environ.get('V10A26_CHECKPOINT','/content/hodge_v10a26_shapes.pkl')` and 7660-7662 "Rerun the same cell; compatible shapes resume automatically." The pickle's bytes are not in the transcript, and lineage across v10a.7 -> .23 -> .26 is not covered by a grep of the final cell. So ground (1) cannot carry the capitalised word "BLINDNESS"; it establishes only that this transcript's text carries no target before its own unblind block.

6) Arithmetic I recomputed, all supporting the ledger rather than contradicting it: 8*(-0.0968932328773) = -0.7751458630184 exactly; |8*a_4 - M_GAMMA_4_NUM| = 5.172529071728604e-13, consistent with contradictions.yaml:51-52 ("5.2e-13") and literature/index.yaml:127 ("5.17e-13"). Same bridge at lower orders: |2*a_2 - 11/306| = 9.94e-14, |4*a_3 + 109151/249696| = 1.11e-12, while the oracle's own errors against those exact rationals are 5.14e-14 and 1.28e-14 - i.e. the m_4 residual is dominated by Hamer's 12-digit printing, not oracle noise. "recovered m_1, m_2, m_3 first" is literally true; the gates enforcing it are loose (2e-5 / 2e-4 / 8e-4 at 7683-7685) while actual recovery is ~1e-13, so the ledger does not overstate.

UNRELATED MINOR OBSERVATION, not this finding: src/workhouse/invariants.py:392-393 still prints "a_4 is an unverified notebook transcription, so this is a normalization cross-check, not primary-source proof", which is stale against invariants.py:1288-1291 and literature/index.yaml:465-471, where the pinned maintainer copy retires exactly that caveat. Two live checks describe the same input's provenance differently.

Verdict: the candidate's facts are largely reproducible and its conclusion is correct, but it is a confirmation of an already-recorded, already-machine-checked repo statement (contradictions.yaml:55-61; literature/index.yaml:454-497; invariants.py:1280-1315), its two supporting grounds are T3 prose, and its one machine-checkable ground is a necessary-not-sufficient scan whose limitation the repo itself already documents (invariants.py:653-663). Not a finding.

---

### 6.32 `m2-m3-recovery-gates-are-loose` — lane `hamer-circularity`

Refuted on three independent grounds.

(1) The quantification is wrong by six orders of magnitude. Gates at "15 hour RUN.txt":7683-7685 are 2e-5 (m1), 2e-4 (m2), 8e-4 (m3). Achieved at :10626 are m1 = 1.0 (deviation exactly 0), |m2 - float(11/306)| = 5.1361692676721304e-14 = 7402 ulps, |m3 - float(-109151/249696)| = 1.27675647831893e-14 = 230 ulps. Gate/achieved ratios are 3.894e9 and 6.266e10, i.e. ~9.6 and ~10.8 orders of magnitude, not "four orders of magnitude". A finding misquantified by 1e6 must not enter the ledger as stated.

(2) The finding attacks a claim the repo does not make. ledger/contradictions.yaml:52-54 and literature/index.yaml:503-506 say only that the oracle "ran with the historical target disabled and recovered m_1, m_2, m_3 first". Neither mentions a gate or a tolerance. The evidentiary basis for "recovered" is the printed totals at :10626, which are 0/7402/230 ulps from target - ten orders tighter than the gates. The sentence is therefore true and supported by tight numbers; it is not a loose pre-registration dressed up as a tight one. The proposed remedy ("state the achieved figures instead of the gate") is moot because the gate is never stated.

(3) The blindness argument is structural, not tolerance-based, and holds independently. totals[4] is accumulated at :7676-7681; M4_SHORTCUT and Q3_OLD are first bound at :7699-7700 under "# 17. FINAL UNBLIND - disputed constants first appear here" (:7695). The historical values are literally not in scope when the oracle is computed. The finding concedes this ("the blindness argument rests on the achieved numbers, not on the gates"), which is precisely why the sentence is not overstated.

Additionally, the adjacent caveat the finding gestures at is already recorded: ledger/contradictions.yaml:55-61 (by_construction_caveat) and C22 at ledger/contradictions.yaml:272-278 ("gate 85 certifies internal bookkeeping, not independent agreement").

Residual true fact, not a finding about this repo: the run's own pre-unblind firewall at "15 hour RUN.txt":7688-7692 is enforced by 2e-5/2e-4/8e-4, so an m2 off by 1.5e-4 would have passed it. That is a design property of an external historical transcript, unfixable here and load-bearing on nothing the ledger asserts.

---

### 6.33 `primary-source-pin-is-unverifiable` — lane `hamer-circularity`

Every factual particular reproduces (predicate list at invariants.py:1302-1308, not 1299-1310 as cited; literature/index.yaml:464 fulltext: null and :470 digest; exactly 2 self-referential grep hits; check PASSes T2 with gap 5.17e-13 vs bound 5.3e-13), but the finding's inference fails on three independent grounds and its substance is already recorded. (a) Tier misread: invariants.py:69-79 restricts a check to tier 1 or 2 by raise ValueError, and :75-76 defines the rule 'A check that compares against a *_NUM constant or a stated tolerance is T2'. This check compares 8*HAMER_A4_NUM to M_GAMMA_4_NUM against HAMER_TOLERANCE=5.3e-13 (constants.py:264), so T2 is the only expressible and the correct label; the tier declares the verification method, not a warranty on each clause of the title. 'T3 inside a check labelled T2' is not a state this registry can represent. (b) Already recorded in five places including the check body itself: invariants.py:1287-1288 ('the publisher-copyright PDF is NOT stored'); literature/index.yaml:464-469 ('the paper is NOT stored'); src/workhouse/literature.py:13-21, a stated design principle 'A paper can be pinned without being stored' with the licence rationale; literature/README.md section 'What is stored, and what is not'; FRONTIER.md:194-197 which states the exact policy as policy ('Obtaining and digest-pinning a primary source upgrades its edges from assertion to verification -- the Hamer 1989 table did exactly that'), and literature/index.yaml:49-50 defines edge status 'verified' as an explicitly curated human verdict. (c) The implied remedy is barred, not overlooked: literature.py:210-243 validate() refuses a fulltext path under a non-redistributable licence, and HAMER_1989 is licence: publisher-copyright, so no predicate could ever machine-check that an unstored copyrighted PDF is Hamer 1989. Finally, nothing computed disagrees with anything -- no discrepancy was reproduced, so this is not a finding under CLAUDE.md's 'When a check fails' procedure. The only residue, too weak to ledger, is that CERTIFIED.md:579 shows the title alone; but index/claims.jsonl:89 and the check's own detail line say 'the copy read is pinned as sha256 96b3ec0f6e2da458...' -- pinned, explicitly not stored -- so no reader is misled.

---

### 6.34 `anchoring-invariance-duplicates-existing-t1` — lane `invariants-tests`

REFUTED. The finding's evidence lines are individually accurate but the inference from them is wrong: A §2 row 7 is not a duplicate of src/workhouse/invariants.py:340-356.

(1) Different scalar. A:23/43/84 define row 7's anchor as "the late diagonal shift", local_shift = M4_ORACLE - ax_rest = +11.1734. Exactly: -0.7751458630189173 - (-11.948578179401377) = 11.17343231638246, matching constants.py:435 RUN15_APPLIED_SHIFT_NUM = 11.17343231638178 to 383 ulps (the known 6.8e-13 stale RAW_FOLDED_AXIAL_GAMMA_NUM offset). invariants.py:340-356 is about Delta_Gamma = 2.0827701250956417 (constants.py:214). |11.17343231638178 - 2.0827701250956417| = 9.090662191286137. Treating these as one "anchoring shift" is exactly the conflation the repo's own T2 check at invariants.py:421-429 exists to prevent.

(2) Different object, and the repo check's hypothesis is not satisfied. The v10a.24c engine is in this repo: corpus-import/programs/hodge_o4_adjudication/src/ENGINE_O4_hodge_v10a24c_rootedfullt1_dualcoldoracle_a100.py:7324-7326 computes local_shift and applies it as `for a,f in enumerate(anchor_faces): K4_mass_cols[int(f),a]+=local_shift` — an addition to three (face, polarization) entries of a face-column kernel (anchor_faces at :6406, V23_AXIAL_H4_COLS at :6761), not +s*I on a 3x3. invariants.py:340-356 assumes the shift enters as a scalar multiple of the identity; that assumption is itself what row 7 has to establish here.

(3) Different logical type. invariants.py:340-356 is an algebraic identity ((h+dg*I)-(q+dg)*I == h-q*I, PASS T1 under `workhouse verify`); row 7 is a dataflow non-dependence claim about a program ("derivative of every upstream quantity w.r.t. the anchor scalar is 0"). The identity does not entail the dataflow claim. As it happens the dataflow claim is true and checkable here — V23_AXIAL_H4_COLS/V23_AXIAL_SHAPE fixed at :6761-6762, shift applied at :7326, mass_shape recomputed at :7327 — which makes it a distinct verifiable fact, not a restatement. `grep -rn "F07"` over src/, ledger/, tests/, index/ returns zero hits: the repo holds no F07 check to duplicate.

(4) The C22 half is mis-attributed. Row 7 says nothing about Gate-85 or target-derivation. A's only C22 sentence is A:139-140 "C22 (Gate-85) unchanged", which declines to reopen it — agreeing with the repo, not duplicating it. (workhouse why C22 does report resolved, cited by CHK run's-applied-shift-is-not-Delta-Gamma, PASS T2 — accurate but irrelevant to row 7.)

(5) No circularity is exhibited, so the `kind: circularity` label is unsupported too.

SEPARATE RESIDUE, deliberately not folded into a corrected #74: row 7's tier label is inflated. A:53 asserts every §2 row is "T1 (exact) or T2 (numerical), reproducible via the check", but the companion check's own table at B:189-196 lists 6 checks and none is the anchoring-invariance one; row 7's sole cited support is "audit C §4" = ORACLE_COUNTERFACTUAL_AUDIT (named at A:23), which is not among the five uploaded artifacts — the uploaded C is W2_R2_ORACLE_LINEAGE_TRACE, i.e. A's document B. By CLAUDE.md's tier table row 7 is T3-asserted within the delivered set, not T1. The underlying statement is nonetheless confirmable at engine :7322-7327, so it is mis-tiered rather than false. That is a different finding (tier inflation / missing cited document), and should be filed on its own evidence, not as a rescue of the duplication charge.

---

### 6.35 `blind-table-check-duplicates-hamer` — lane `invariants-tests`

I reopened the primary transcript (15 hour RUN.txt:10619-10626, where :10620 is size 1 and :10626 is TOTAL — the artifacts' line citations are correct) and both artifacts, and recomputed in python3 with struct-level bit/ulp comparison plus exact Fraction sums. The finding's central evidence — "the sum is bit-for-bit 8*HAMER_A4_NUM" — reproduces only when the two nonzero "numerical zero" rows are zeroed, which is not what the source prints; with the source values the two floats are 382 ulps apart and the required tolerances differ (4.7484e-13 vs 5.1725e-13). The duplication claim also fails on provenance: invariants.py:388-395 and :1285-1315 both draw their left-hand side from a digest-pinned external paper, whereas the proposed check draws on six numbers the repo references nowhere. So the check is new rather than a re-derivation, and the "circularity" kind is wrong. Only a precision-labelling defect in A:62 survives, at low severity.

---

### 6.36 `blind-total-is-not-the-row-sum` — lane `invariants-tests`

REFUTED — the finding's arithmetic is right but its diagnosis is wrong; the gap is a print-format artifact of the primary source, not an overstatement by A or B.

(1) FORMAT. In corpus-import/records/transcripts/15 hour RUN.txt:10620-10625 every per-size entry is rendered with %.12g (11-12 sig figs; 11 when the 12th digit is a trailing zero, as %g strips), while line 10626 prints the TOTAL with repr (16-17 sig figs: "1.0 0.03594771241824929 -0.4371355568371267 -0.7751458630189173"). Verified: '%.12g' % (143/8960) == '0.0159598214286' and '%.12g' % (-5/24) == '-0.208333333333', matching the printed rows exactly.

(2) DECISIVE CROSS-CHECK — the same "gap" is present in every column of the same table, and in the two columns with a known exact rational it is the TOTAL that is accurate and the printed-row-sum that is degraded:
  m2: Sigma printed rows = 0.035947712417952249, TOTAL = 0.035947712418249289, gap -2.9704e-13 (-42808 ulps). TOTAL vs 11/306 = -5.136e-14; row-sum vs 11/306 = -3.484e-13.
  m3: Sigma printed rows = -0.43713555683701244, TOTAL = -0.43713555683712668, gap +1.1424e-13 (+2058 ulps). TOTAL vs -109151/249696 = -1.277e-14; row-sum vs -109151/249696 = +1.015e-13.
  m4: Sigma printed rows = -0.77514586301844246, TOTAL = -0.7751458630189173, gap +4.7484e-13 (+4277 ulps).
The transcript's own [PASS] lines at :10627-10629 assert m2=11/306 and m3=-109151/249696 against the TOTALs. So "printed rows do not sum to the printed TOTAL" is a uniform property of the %.12g rendering across all three columns, not a fact about m4.

(3) MOST OF THE m4 GAP IS ONE ROW. Size 6 c4 prints as -0.208333333333, the %.12g rendering of -5/24 = -0.20833333333333334; that single truncation contributes +3.3334e-13 of the 4.7484e-13. The residual 1.4151e-13 sits well inside the +/-5e-13 rounding envelope of rows 2 and 3 (which are also 12-sig-fig, last place 1e-12).

(4) THE MECHANISM CLAIM IS OFF BY ONE. A:62 prints "-0.7751458630189", which is exactly %.13g of the oracle; %.13g of the row-sum is "-0.7751458630184". The digit strings 7751458630189173 and 7751458630184425 share a 12-character prefix, so index 12 is the FIRST DIFFERING digit — and A prints it. A's number is therefore distinguishable from the row-sum, not "truncated at exactly the digit where the two diverge".

(5) THE REPO CITATION IS A MISATTRIBUTION. src/workhouse/invariants.py:645-649 and ledger/gaps.yaml:117-121 concern the target-blindness contamination scan; the string 7751458630184 there is Hamer's 8*a_4 (src/workhouse/constants.py:239 HAMER_A4_NUM = -0.0968932328773; 8* that is exactly -0.7751458630184), and the point is that a scan for the substring 7751458630189173 will not catch an engine seeded with Hamer's constant. That is an oracle-vs-Hamer independent-quantity divergence. It documents nothing about a row-sum-vs-total divergence. (The finding is also self-undermining here: if the repo already documented it, it would be non-novel by its own framing.)

(6) WHAT B AND A ACTUALLY SAY IS SOUND. B section 2 (6a2b59cb-...md:53-63) states "The blind oracle is the sum of its rooted per-size contributions" — a true structural claim about a rooted-incidence/linked-cluster transform — and then reproduces the transcript block faithfully, including the TOTAL line as the transcript prints it, with sizes 4 and 5 honestly marked "~ 0 (numerical zero)". Nothing in B asserts that the 12-sig-fig printed rows sum to the 17-sig-fig total. B section 2's load-bearing claim is the one-face agreement (143/8960 vs size-1 c4), which is untouched by this.

CAVEAT: the engine cannot be rerun here, so bit-exact agreement of the full-precision rows with the TOTAL is not directly demonstrated; the m2/m3 evidence makes the print-artifact explanation overwhelming and no alternative is needed.

RESIDUE (not this finding, and far weaker): A:62 tags the row T2 without a stated tolerance, where CLAUDE.md requires the tolerance in the detail line. Stating the present finding as written would put a display-precision artifact into the ledger as a substantive high-severity overstatement.

---

### 6.37 `dispute-suite-cites-a-superseded-section` — lane `invariants-tests`

REFUTED on both the count and the inference. (1) Count is wrong. The dispute suite (`src/workhouse/invariants.py:294-429`) holds exactly 13 `@dispute.check` decorators, and TEN of them reference §5.5, not nine: seven carry the exact string "MASTER_THEORY §5.5" (lines 297, 303, 318, 369, 375, 382, 397) and three carry it with a register suffix — "MASTER_THEORY §5.5 / C1" (309, 342), "MASTER_THEORY §5.5 / C2" (360). The auditor's own evidence line is internally inconsistent: it says "nine" while listing ten line numbers, and two of those ten (340, 358) are the decorator's opening paren, not the section string (which sits at 342 and 360). File-wide the string appears 16 times, also in the `crosswalk` (436, 463, 474, 483) and `pencil` (515) suites and at 862, so scoping it to the dispute suite understates it too. (2) The factual premise about the theory tree is correct but the inference "repo-wrong-or-stale" is refuted by the repo itself. `theory/MASTER_THEORY_UNIFIED_2026-08-20_v4_3.md` indeed has §5 = 5.1/5.2/5.3 only (lines 644, 646, 702, 790) with the scalar adjudication at §7 (line 999), and §5.5 exists only at `theory/superseded/MASTER_THEORY.md:399` ("THE DISPUTE — two fourth-order kernels, neither promoted [DISPUTED]"). But that mapping is deliberate, documented, and machine-enforced, not drift: `ledger/documents.yaml:30-37` registers the alias `MASTER_THEORY` -> `theory/superseded/MASTER_THEORY.md` with `standing: superseded` and the note "the historical register whose §-numbering C1-C22 and most check cites carry. Its sections are stable and citable as HISTORY; the governing treatment of any claim lives in UNIFIED"; `theory/CLAUDE.md:19-23` states outright "`§5.5` and `§4.4` exist in `superseded/MASTER_THEORY.md` only — the governing document has no such sections. ... When you cite, name the document." — which the checks do, since "MASTER_THEORY" is precisely that file's stem and is distinct from the "UNIFIED"/"v4.3" aliases at `ledger/documents.yaml:23-29`. `tests/test_documents.py:33-66` makes the legend sound and every citation resolvable, so this is already a passing machine check, not an unrecorded defect. (3) The appeal to non-negotiable #1 is a misreading: it forbids reading a superseded document *as current*, and `theory/README.md` keeps `superseded/` precisely because "earlier checks were run against them and the audit trail needs them readable". (4) Consistency spot-check confirms the alias resolves uniformly to the superseded file, not ambiguously: `invariants.py:285` cites "MASTER_THEORY §5.3" for "exceptional ranks are exactly {3,4,5,6}", which is the content of `theory/superseded/MASTER_THEORY.md:322-327` ("the exceptional set is exactly {3,4,5,6}"), whereas unified §5.3 (line 790) is "Edges, holdout, stencil, and curvature". So there is no discrepancy to record — it is already known, already written down in two places, and already tested.

---

### 6.38 `eight-checks-vs-six` — lane `invariants-tests`

Refuted — the discrepancy is an artifact of the auditor's reading, and the artifacts reconcile at 8 by two independent routes.

(1) B §6 does not enumerate the script exhaustively and never claims to: its heading (B:185) is "The runnable check (summary)". The 6-row table (B:190-197) is followed at B:198-199 by two further stated run outcomes — "Verified: the guard rejects an F07 size-2 value tagged with retired-engine provenance, and accepts one tagged with an independent (§5-compliant) source" — i.e. a negative-case and a positive-case test of the provenance guard, outside the table. 6 table rows + 2 guard cases = 8, matching A:27 and A:163 exactly.

(2) The claim that A:148 "implies 10" misreads it. A:147-148 is a landing instruction for a *new* invariants suite: "the 8 machine-verified checks + the two OPEN discriminators". "The two OPEN discriminators" are Knob A and Knob B of A §4, titled "The decisive test (two knobs)" (A:96, A:101-104), where A:113 explicitly calls one "the discriminator between fit artifact and real physics". Those are proposed future computations, not existing script rows. So A says: land the script's 8 checks plus 2 new OPEN discriminator entries. Internally consistent with A:27 and A:163.

(3) The finding's assertion that "'8 checks' is unsupported by the artifacts' own enumeration" is directly false. A §2 enumerates 8 rows (A:57-64) and A:53 introduces them as "Every row is T1 (exact) or T2 (numerical), reproducible via the check" — a second passage in A that independently enumerates 8.

(4) The sub-argument that B's row 6 (tier FINDING) is not "machine-verified" contradicts this repo's own convention: FINDING checks are ordinary registered machine checks with tiers, e.g. /home/user/WORKHOUSE/src/workhouse/invariants.py:318 — @dispute.check("FINDING: the printed Delta_Gamma is one ulp low", "MASTER_THEORY §5.5", tier=2).

Confirmed independently: artifacts C (/root/.claude/uploads/384fab32-8991-52ce-b2bf-4999d379e3f5/be0baa19-...md) and D (e22209c0-...md) never mention f07_twoface_adjudication_check.py (grep returns nothing), so B §6 is the only enumeration — but three of A's own six-document set are also missing (A:21-26 lists DENOMINATOR_LOCALIZATION_INVESTIGATION, ORACLE_COUNTERFACTUAL_AUDIT, COORDINATION_NOTE, none uploaded), and the script is absent from the certificate zip (22 files under scratchpad/cert, no f07*/twoface*/adjudic* match). The true count therefore cannot be settled here — which is precisely why recording "artifact A is wrong: 8 vs 6" would be a false ledger entry, since a natural reading of the artifacts already reconciles them.

Residue (a different, much smaller defect, not the finding as written): A:53 asserts "Every row is T1 (exact) or T2 (numerical)" over a table whose row A:64 ("F07 oracle-free") carries tier "—". The row is honestly labelled in the table itself, so no reader is misled about its tier; only the lead-in sentence over-claims. Too weak to state as a medium-severity finding.

---

### 6.39 `f07-value-already-registered` — lane `invariants-tests`

Every repo-side cite in the evidence line is accurate and I reproduced it: /home/user/WORKHOUSE/src/workhouse/constants.py:427 QUARANTINED_SCALAR = Rational(-160506019419340168451, 14501180577204921600), whose float is exactly -11.068479463778765 (true value -11.06847946377876468205..., shortest-repr round-trip, 0 ulp); invariants.py:396-400 'quarantined scalar decimal' T2 check passes with |diff| = 0.00e+00, detail 'rejected by both sides'; ledger/contradictions.yaml:36-39 'quarantined shortcut ... status: rejected-by-both'; theory/superseded/MASTER_THEORY.md:416 (full decomposition: raw folded -11.9485781794007, linked vacuum -1474623/1675520, the quarantined rational) and :767 (register row 37); `workhouse search -- -11.068479463778765` returns exactly 2 claims (CONST:QUARANTINED_SCALAR, CONST:quarantined scalar). `git log -S` shows both the constant and the invariant landed in commit aa835a1, the repository's first commit, so 'for as long as the dispute suite has existed' is literally true.

The finding nonetheless fails, because its allegation is about the artifacts and the artifacts do not make it. (1) Both documents attribute the value to the registered constant in the identity column of the very table that introduces it: B:37 `| M4_SHORTCUT = F07 branch | -11.0684794637788 | ax_rest - V_link = QUARANTINED_SCALAR |` and A:39 the identical row. (2) B:46 states 'All values re-verified this session against corpus-import/records/transcripts/15 hour RUN.txt and src/workhouse/constants.py' — explicit dependence on the repo registry, the opposite of claiming discovery. (3) B itself names what it holds to be new, and it is not the number: B:21 'The decisive new fact is that the two branches agree exactly at one face (143/8960).' (4) The finding's proposed correction — that what is new is the identification as the F07 branch answer rather than a raw intermediate — is already the artifacts' own sentence, A:46: '-11.0685 is the complete F07-branch answer, not a raw intermediate (correction to document A §11.3, resolved in E/F; see §5 below).' A finding cannot be a discrepancy with a document when it restates that document's text.

'is now known exactly' (B:18) is a status contrast against the blind branch on the following line ('measures m4,blind = -0.7751458630189173'): exact rational versus measured float, not a provenance claim of novelty. Certificate E independently recomputes the same rational (cert/AUDIT_REPORT.md:31-34, m_4,rest = D_EXACT + F - V_linked = -160506019419340168451/14501180577204921600), which is a confirmation of a pre-registered value, not a rediscovery.

The declared kind 'circularity' is also unsupported — no circularity is exhibited anywhere in the cited passages. B in fact documents the one real circularity in this area and explicitly refuses to use it (B §4, lines ~114-130: the v10a.21r rooted-incidence engine is gated to sum back to M4_EXACT, 'Do not').

One adjacent issue is real but is a different candidate and I am not converting this one into it: neither A:39/46 nor B:37 discloses that the repo's registered status for this value is 'falsified · record-backed' / 'rejected by both sides' (constants.py:426, contradictions.yaml:39, invariants.py:400), while A:46 calls it 'the complete F07-branch answer'. That is a status-disclosure gap, not novelty overstatement or circularity, and needs its own adjudication.

---

### 6.40 `gap-10293-is-a-subtraction-of-two-registered-constants` — lane `invariants-tests`

REFUTED on its substantive point, and its evidence line contains a factual error.

(1) The arithmetic is correct and I reproduced it. python3: M_GAMMA_4_NUM (-0.7751458630189173, /home/user/WORKHOUSE/src/workhouse/constants.py:207) minus float(QUARANTINED_SCALAR) = float(Fraction(-160506019419340168451,14501180577204921600)) = -11.068479463778765 (constants.py:427) gives 10.293333600759848, bit-identical (0x4024962fd25c29b6) to the printed value; the exact-rational subtraction Fraction(M_GAMMA_4_NUM) - QUARANTINED_SCALAR rounds to the same double, so round-then-subtract and subtract-then-round agree. So the number IS a subtraction of two registered constants. That part is true.

(2) But the finding's charge — that the artifacts present it as a session result rather than as that subtraction — is contradicted by the artifacts themselves, which state it as the subtraction and name the repo constant:
  - B:35-38 (§1 "The three scalars"): the table gives `M4_SHORTCUT` = -11.0684794637788 with identity "`ax_rest − V_link` **= QUARANTINED_SCALAR**" and `M4_ORACLE` = -0.7751458630189, and only then B:41 writes "`|M4_ORACLE − M4_SHORTCUT| = 10.293333600759848`". A:39-42 carries the identical table with the same "= QUARANTINED_SCALAR" identity immediately above its line 42.
  - B:46-47: "All values re-verified this session against `corpus-import/records/transcripts/15 hour RUN.txt` and `src/workhouse/constants.py`." B:208 cites `constants.py:426-435,649-655` — the exact QUARANTINED_SCALAR block.
  - Neither document calls the gap new. B:21-23 explicitly reserves "new" for a different fact: "They disagree by **10.293333600759848**. The decisive new fact is that the two branches **agree exactly at one face** (`143/8960`)". A:9-13 likewise attributes the session result to the localization ("this session localized the entire disagreement to the multi-face (size >= 2) sector"), not to the gap number.
So there is nothing overstated to correct; the artifacts already say what the finding asks them to say.

(3) The finding's evidence line is wrong where it says "no corpus occurrence either". The decimal appears verbatim three times in the corpus, printed as exactly this subtraction:
  - /home/user/WORKHOUSE/corpus-import/records/transcripts/15 hour RUN.txt:10633 — "quarantined scalar shortcut = -160506019419340168451/14501180577204921600 = -11.068479463778765  |Δ|= 10.293333600759848"
  - /home/user/WORKHOUSE/corpus-import/records/transcripts/15 hour RUN. results.txt:2874 — same line
  - /home/user/WORKHOUSE/corpus-import/programs/hodge_o4_adjudication/notebooks/NB_O4_hodge_v10a26_factor52complete_exactsw_rootedoracle_a100_alt2.ipynb:2910 — same line
That line sits 10 lines below the "[16] ROOTED INCIDENCE TRANSFORM" block (15 hour RUN.txt:10620-10626) that B §2 cites by line number, so the artifacts are working directly against the source that prints it. I confirmed `.venv/bin/workhouse search 10.293333600759848` and `... --corpus` both return "no claim matches" — the auditor read that miss as absence from the corpus, which it is not (the prose index has MIN_MAG=1000 and both indexes join on exact rationals, not decimals; see src/workhouse/corpus_index.py:1-24).

(4) The only surviving true sub-claim is that no invariant asserts the difference: src/workhouse/invariants.py:399 asserts only |float(QUARANTINED_SCALAR) - (-11.068479463778765)| < 1e-14, and invariants.py:387-389 asserts the Hamer 8*a_4 vs M_GAMMA_4_NUM cross-check; nothing asserts their difference. That is a trivially-available T2 addition, not a defect in the artifacts and not something the artifacts claim otherwise. Too weak to state as a finding, and the "overstated" framing it is packaged in is refuted.

---

### 6.41 `search-cli-rejects-negative-rationals` — lane `invariants-tests`

I opened cli.py at the cited lines rather than trusting the evidence line. src/workhouse/cli.py:246-257 defines `_rescue_negative_query`, called at cli.py:263 as the first statement of main(), which inserts `--` when the token after `search`/`why` matches `^-\d+(/\d+)?$|^-\d*\.\d+([eE][-+]?\d+)?$` at cli.py:254. That alternation matches negative rationals, so the finding's claimed decimal-works/rational-fails asymmetry does not exist. Direct unit call: ['search','-327/83776'] -> ['search','--','-327/83776']; ['search','-54321/837760'] -> ['search','--','-54321/837760']. End-to-end, both `python3 -m workhouse.cli search -327/83776` and the installed /home/user/WORKHOUSE/.venv/bin/workhouse print `no claim matches '-327/83776'` with rc 0 -- no argparse error. `workhouse search -5/48` returns 7 matching claims including CONST:CUBE_COMPLETION_4. The fix is not local/uncommitted: `git status --porcelain src/workhouse/cli.py` is empty and `git show HEAD:src/workhouse/cli.py` contains the function at line 246. The finding's own evidence line betrays the misattribution -- its working example is `workhouse search --corpus -- "-327/83776"`, i.e. the auditor was running with `--corpus` before the value, which is the one ordering that genuinely still fails, and then wrote the failure up against the bare form. Since the filed claim (bare negative rationals die; the user must know to write `--`) is contradicted by direct reproduction, it must not enter the ledger as stated; the two narrow ordering defects are real but are a different, lower-severity statement.

---

### 6.42 `twoface-vacuum-has-no-current-theory-anchor` — lane `invariants-tests`

REFUTED — the greps are right, the conclusion drawn from them is not. It describes the repository's designed, majority, machine-enforced citation practice as a provenance gap, and the exact precedent it warns about already exists in the repo.

WHAT I REPRODUCED (all true):
1. Artifact text confirmed verbatim: /root/.claude/uploads/.../6a2b59cb-F07_VS_BLIND_TWOFACE_ADJUDICATION.md:97-99,193 and .../52ebdfa7-RANK3_ORDER4_MASTER_RECORD.md:60.
2. Current theory stack: grep -c for 83776, 54321, 837760, 1474623, 1675520, 8960, 1309 returns 0 in each of theory/MASTER_THEORY_UNIFIED_2026-08-20_v4_3.md, theory/GLUEBALL_DETAILED_FORMULA_2026-08-20_v3.1.md, theory/GLUEBALL_SOURCE_CONSOLIDATION_GUIDE_2026-08-20_v4_3.md. I also grepped the decimal forms (-0.06484076585179527, -0.0039032658517952636 and their prefixes "064831"/"0390326") — also 0, so it is not a LaTeX/decimal-rendering miss.
3. Only in-theory hit for 83776/54321 is theory/superseded/MASTER_THEORY.md:568. (1474623/1675520 additionally at :416 and :654.)
4. Transcript resolves: corpus-import/records/transcripts/Monday 531 PM.txt shows, at the cited lines, "[PASS] v10a.7 vacuum coplanar pair full e4=-54321/837760", "[PASS] ... omega4=-327/83776", the identical perpendicular pair, and "[PASS] v10a.7 coplanar/perpendicular vacuum pair linked weights agree". (Corpus breadth: 31 files contain 54321, 33 contain 83776 — file counts, not the finding's 63/61 occurrence counts, but consistent.)
5. Arithmetic: -54321/837760 - 2*(-39/1280) = -327/83776 exactly; 83776 = 2^6*7*11*17.

WHY IT IS NOT A FINDING:
(a) Citing superseded MASTER_THEORY is this repo's NORMAL and DOMINANT practice, not an exception. Of 140 `.check(...)` section strings in src/workhouse/invariants.py, 37 name MASTER_THEORY (35 "MASTER_THEORY §x", plus "MASTER_THEORY C20" and "MASTER_THEORY C7") — more than the 26 naming the whole current stack combined (14 UNIFIED, 11 GLUEBALL, 1 v4.3). Six more cite transcripts ("transcript ~170", "818 ~3963", etc.).
(b) The repo has a purpose-built mechanism for exactly this, and it is machine-checked. ledger/documents.yaml:31-40 legends alias MASTER_THEORY -> theory/superseded/MASTER_THEORY.md with `standing: superseded` and the note "Its sections are stable and citable as HISTORY"; transcript/818 carry `standing: corpus`. tests/test_documents.py:34-48,50+ (`test_legend_is_sound`, `test_every_check_citation_resolves`) makes an unlegended alias a build failure and keeps the standing vocabulary closed. So the finding's operative recommendation — "that should be stated when it lands" — is already automatic and enforced; the standing rides on the alias.
(c) The finding leans on non-negotiable #1, but that rule (CLAUDE.md; theory/CLAUDE.md "What is current") forbids reading a superseded document AS CURRENT, not citing it. theory/CLAUDE.md "Citing a section" says the opposite of the finding's implication: "§5.5 and §4.4 exist in superseded/MASTER_THEORY.md only — the governing document has no such sections. ... When you cite, name the document."
(d) The precedent is already in the repo, from the same superseded lines. LINKED_VACUUM_4 = Rational(-1474623, 1675520) at src/workhouse/constants.py:430 is sourced from theory/superseded/MASTER_THEORY.md:416/568 — the identical provenance situation — and already carries a registered T2 check at src/workhouse/invariants.py:404-418 citing "MASTER_THEORY C20", plus ledger/contradictions.yaml:224-248 and index/claims.jsonl:201. Nothing about registering e4(C)/ω4 would be novel or need a caveat that LINKED_VACUUM_4 did not need.
(e) The T3 half is a tautology. CLAUDE.md: "T3 is the default for everything in the corpus." Saying two unchecked corpus rationals are T3 is not a discrepancy; it is the baseline state of every value not yet in invariants.py.

Residual true kernel, not worth a ledger entry as written: these two rationals have no anchor in the v4.3/v3.1 stack and would be registered against superseded §/transcript standing — which is ordinary here. If anything in this area deserves a finding it is a different one: the ω4 identity is exact arithmetic among three transcript-quoted rationals (e4(C), one-face e4 = -39/1280), so a check on it would certify internal consistency of one engine's output, not an independent re-derivation — that claim is not what finding #77 states.

---

### 6.43 `w22-decisive-test-already-an-open-item` — lane `invariants-tests`

I re-opened every cited file. The repo-side evidence is real: invariants.py:665-678 defines 'FINDING: the harness can never report COMPLETE' and it PASSES (ran it: Result(passed=True, tier=1, line=665)); settlement.py:128-142 implements verdict_can_be_complete(); mce_adjudication_harness.py:43 and :335 read as quoted (:335 is unconditional, at function-body indent); gaps.yaml:127-131 carries the G3 audit_findings entry. The finding nevertheless fails on three independent grounds. (1) Misreading of A. A:112 reads "The W22-mask knob is the discriminator between *fit artifact* and *real physics* — a distinction none of the five documents could draw alone." Its explicit scope is A's own document set, enumerated at A:19-27 as documents A–F. A makes no assertion about the repository there, so the finding's headline ("A's claim ... is wrong about the repository") attributes a claim A does not make. (2) Conflation of two different items. Repo item 10 is a compliance requirement for a sealed MCE run that has never occurred ("no seal exists in this corpus", MASTER_THEORY.md:420), scoped to "all 33 rooted classes" on the marked-cluster engine the harness drives. I grepped that engine, corpus-import/programs/hodge_o4_adjudication/src/DATA_SU3_Exact_MarkedCluster_m4_Colab.py: grep -c "W22" returns 0, and there is no toggle, order-schedule, or matching identifier in it. A's Knob B (A:104, elaborated B:167-170) is an order-truncated two-face recomputation on a different engine, the blind v10a.24c (ENGINE...v10a24c...py:6894-6899, 6928-6946), against a specific target size-2 c4 = -0.403971702978 (15 hour RUN.txt:10621). Different engine, different scope (2 faces vs 33 rooted classes), different purpose (diagnostic on an existing blind run vs protocol compliance on a future sealed run). (3) The repo item cannot be "already blocking" A's distinction. mce_adjudication_harness.py:335 assigns verdict["protocol"]["item10_W22_toggle"] = "OPEN (engine exposes no toggle flag)" unconditionally, independent of any certificate content — that is exactly what settlement.py:139 detects and what makes the FINDING pass. So item 10 is a hardcoded stub: it would still print OPEN after a successful W22-off recomputation. It tracks a harness/engine-interface gap, not the state of the physics discriminator. Confirming the negative: grep -rn "W22" over the entire repo excluding corpus-import/ returns only settlement.py:131,139, invariants.py:670,673, mce_adjudication_harness.py:43,335, gaps.yaml:127 (plus an unrelated sympy test in .venv), and in theory/ only GLUEBALL:1465 and superseded MASTER_THEORY:420. Nothing in the repository registers a two-face W22-off recomputation or the F07-vs-blind size>=2 localization as an open item, so "the discriminator is already named, already open" is false in the sense the finding needs. Writing this into the ledger at high severity would itself install the conflation of a harness stub with an unresolved physics test.

---

### 6.44 `existing-slot-is-graph-invisible` — lane `ledger-graph`

The finding's own evidence line misdescribes graph.py (it emits 431 edges across 17 types from six sources spanning graph.py:118-206, not "blocks + register contradictions/gaps only"), and it misattributes to the artifacts a proposal none of them makes — D §8 and B §7 both explicitly name constants.py:426-435,649-655 alongside contradictions.yaml:36-40, and constants.py:649-655 is exactly what generates the CONST:quarantined scalar record in claims.jsonl:150 with status "falsified". So the amendment as actually proposed is not invisible. Separately, CONST-node graph isolation is documented intended behavior (graph.py:17-22, "no inferred edges") and affects 77/115 CONST records including C1's other two quantities, so it is not a gap specific to this slot. Only a narrow, low-severity residue survives: the `quantities` field is read by no code in src/workhouse/ and only partially by tests/test_ledger.py:49, so a YAML-only edit to the third quantity would trip no check.

---

### 6.45 `knob-b-is-a-strict-subset-of-protocol-item-10` — lane `ledger-graph`

Refuted as packaged. (1) The novelty charge misreads A. A's sentence (A:112-113) scopes the claim to the uploaded set — "a distinction none of the five documents could draw alone" — not to WORKHOUSE, and A files the question inside the protocol twice: A:78 "a sub-entry of C2 / G3" and A:149, which proposes writing it into ledger/gaps.yaml under G3. A does not present Knob B as independent of the frozen protocol, so "Not new" attacks a claim A does not make. D:91, cited as a third instance, asserts no novelty at all — it states a requirement ("An exact order-truncated W22-off comparison is therefore required").

(2) The finding's two prongs cancel. "Strict subset of protocol item 10" and "on a different code path, so running it would not discharge item 10" cannot both hold at full strength; a test on a different engine is a related cheaper experiment, not a subset of a requirement on the sealed MCE run (GLUEBALL_DETAILED_FORMULA_2026-08-20_v3.1.md:1454 "The next physical run must freeze and authenticate"; corpus-import/programs/hodge_o4_adjudication/README.md:26 "What the next run must do").

(3) The code-path claim is itself wrong. It asserts Knob B targets v10a24c's _v23c_fit_cluster. Knob B targets the number at corpus-import/records/transcripts/15 hour RUN.txt:10621 (size 2 c4 = -0.403971702978), and RUN.txt:7647-7670 shows that run's [15] block was v10a.26's exact-SW path — gate "v10a.26 exact SW block diagonalization closes through O(u^4)", printed field SWoff=4.44e-16 (RUN.txt:10613), and RUN.txt:10617 / :7670 "production coefficient method: canonical Hermitian SW/BCH; no polynomial fit/window". _v23c_fit_cluster (deg 6, 13 points, umax 0.055 — corpus-import/programs/hodge_o4_adjudication/src/ENGINE_O4_hodge_v10a24c_rootedfullt1_dualcoldoracle_a100.py:6792-6794, 6934-6946) survives there only as a duplicate cross-check (RUN.txt:7653). The auditor's engine identification, and hence the whole path-mismatch prong, is unverified.

(4) "Silently drops the recorded obstacle" is not supported. The recorded blocker (ledger/gaps.yaml:126-131; settlement/mce_adjudication_harness.py:335 verdict["protocol"]["item10_W22_toggle"] = "OPEN (engine exposes no toggle flag)"; src/workhouse/settlement.py:127-142 verdict_can_be_complete) is specifically about the marked-cluster engine's flag; transferring it to the blind oracle is the engine/inventory conflation gaps.yaml's own inventory_trap warns against. And D does not conflate silently: D:121-131 tabulates "Blind linked cluster: 203 concrete rooted clusters, 33 rooted shape classes" against "Canonical marked calculation: 203 x 3 = 609" and states "There is currently no termwise map", citing README:27-45 — the range containing item 10 at README:38.

Repo-side citations I did confirm verbatim: gaps.yaml:69 item 10 text (duplicated at GLUEBALL v3.1:1465, README:38, theory/MASTER_THEORY_UNIFIED_2026-08-20_v4_3.md:2354); gaps.yaml:126-131; harness:43 and :335; settlement.py:128-142. The 33/203 inventory at RUN.txt:7752 and :10747, spanning |C| = 1..6 (:10613 plus the per-size table :10620-10625).

What survives is only a scope observation, too weak to enter the ledger as a finding: size-2 rooted classes are a proper subset of the 33, so a W22-off recomputation at size 2 would not by itself satisfy item 10's "across all 33 rooted classes". Separately, on my own check rather than the repo's: grep of the v10a24c engine for W22/mask/layer-mask returns only the comment at :4525, and _v23c_build_basis (:6885-6899) applies W densely with no layer mask, so no engine in this repo exposes a W22 toggle either — a cost note on Knob B, not the overstatement alleged.

---

### 6.46 `m4-spelling-is-forbidden-for-m-gamma-4` — lane `ledger-graph`

Re-read all cited primary sources. Confirmed: symbols.yaml:43-55 does attach `forbidden: m_4` to m_gamma_4 with no pairing precondition, and search.py:210-216 / navigator.py:101-105 render it as the unconditional "never call it m_4", so the finding's interpretive core is arguable. But four load-bearing sub-claims fail. (a) The enforcement citation is wrong: tests/test_ledger.py:47 is `"m_4" in term["forbidden"]` where contradictions.yaml:22 makes term["forbidden"] the string "two m_4 values" — a trivially-true substring check on the ledger's own text, not a usage ban; a grep of src/ and tests/ shows no check scans documents for forbidden names. (b) Under the repo's own token-boundary regex (search.py:135) literal `m_4` occurs 0 times in A, B and D; D uses only subscript-disambiguated `m_{4,F07}`/`m_{4,blind}` (D:11,24), which is the opposite of the undifferentiated naming ADR 0002:28 blames, so D should not be charged. (c) B:3 is not "the exact substitution" of ADR 0002, whose substitution is the joint q_band^(4)+m_Gamma^(4)→m_4; B's pair excludes q_band^(4) (-2.857915988114559). (d) The failure mode the rule names does not occur: D:27, D:182, B:215 and B:218-219 each explicitly reaffirm ADR 0002 and keep q_band vs m_Γ apart, spelling the canonical names correctly. The proposed fix also coins `m_F07^(4)`, a name absent from the repo, where contradictions.yaml:36-40 and B's own table already supply M4_SHORTCUT / "quarantined shortcut". What remains is a one-line cosmetic nit at B:3 — far short of a high-severity artifact-wrong ledger entry.

---

### 6.47 `no-slot-c-register-is-closed` — lane `ledger-graph`

REFUTED on three counts.

(1) The artifact is not wrong. D:193 reads verbatim "Create a separate open contradiction **or sub-entry**:" — a disjunction — and the finding refutes only the first disjunct. The second is the compliant route and needs zero test edits: D §8's subsection is headed "C1: split the resolved naming issue from the newly genuine branch conflict" (D:180) and amends /home/user/WORKHOUSE/ledger/contradictions.yaml:36-40 (the `quarantined shortcut` quantity, status `rejected-by-both`, which I read). A sub-entry under C1 is unconstrained: tests/test_ledger.py:40-50 only requires the joined quantity labels still contain "band-kernel anchor" and "vacuum-subtracted", and ledger.validate never inspects `quantities`.

(2) The `where:` field misattributes. Grepping all five artifacts for C23|new contradiction|separate open contradiction|sub-entry yields exactly three hits: D:193, A:78 "sub-entry of C2 / G3", B:220 "a sub-entry of C2/G3". A and B take precisely the route the repo permits; citing them as instances of the error is wrong. No artifact proposes a C23 anywhere.

(3) The mechanics are half wrong. Simulated on scratch copies with the real loader (repo untouched), two configurations. Config A (C23 open, blocks:[G3], G3.resolves += C23, no R crosswalk): L.validate -> [] clean; :20 FAIL; :28 FAIL (open == ['C2','C23']); :131 FAIL (governing('C23') == []); :108-120 PASS; :77-95 PASS. Config B (same plus C23 appended to the EXISTING R5's `contradictions`): L.validate -> [] clean; :20 FAIL; :28 FAIL; :131 PASS (governing('C23') == ['R5']); :108-120 FAIL with extra ('R5','C23'); :77-95 PASS; :124 len(unmapped)==11 still PASS (23-12). So guards 3 and 4 are mutually exclusive exits of one guard, not independent — at most three assertions fail in any single configuration, never four. And the auditor's stated basis for guard 4, "that R-item cannot be invented — tests/test_ledger.py:77-95 re-extracts the register verbatim", is refuted: no new R-item is required, and the verbatim test (which compares only `title` and `text`) passes unchanged in config B. The only blocker there is the hand-authored pair set pinned at :108-120.

The one residual true statement — the C-register is closed at C1..C22 — is already recorded in the repo, at tests/test_ledger.py:12-18 and src/workhouse/ledger.py:5-9 ("transcribes the older MASTER_THEORY.md §8 register, which ... is not governing"). And `ledger.validate` passing clean is by design, not a hole: seq_complete (src/workhouse/ledger.py:135-149) enforces contiguity from 1, not a fixed maximum, because gaps.yaml deliberately grew G20-G23 (test_ledger.py:14-18); closure is enforced by pytest, which is what `make check` / CI runs (CLAUDE.md). Nothing here is an artifact defect worth a ledger entry.

---

### 6.48 `pair-already-registered-in-c1` — lane `ledger-graph`

The finding is refuted on three independent grounds. (1) Its central mechanism misreads document D. The finding asserts "a new entry would double-register the same rational with a contradictory verdict," but D §8 explicitly forecloses that: D:184-191 first says "Amend the third quantity at ...contradictions.yaml:36-40. The value -11.068479463778765 should no longer be labeled `rejected-by-both`" and supplies the replacement fields, and only then, at :193-199, proposes a separate open entry. Under D's actual recommendation the old verdict is removed, so no contradictory double-registration follows. The conflict exists only if you apply half of D's proposal. (2) Its site inventory is wrong. The finding says three sites "would then have to move together or conflict": contradictions.yaml:40, constants.py:652-655, invariants.py:400. But D:201 already names "src/workhouse/constants.py:426-435,649-655" — covering both constants.py sites, including the line 426 comment "Rejected by both sides; recorded so it is never silently resurrected." Only invariants.py:400 goes unnamed, and it is a free-text detail string, not a verdict field; the check's actual predicate is a decimal-agreement test that is indifferent to the label. (3) The claim that the register is unguarded overstates. It is true that ledger.py:130-227 never compares values or verdicts across entries, but it is not true that nothing constrains a new open entry: ledger.py:171-173 rejects an open contradiction with no `blocks`, and ledger.py:221-225 rejects one that no gap's `resolves` claims. A new open entry would fail `ledger.validate` unless wired into the gap graph, which is exactly the cross-check the finding says is absent. Beyond these errors, the finding is structurally not a WORKHOUSE finding: it identifies no disagreement between a machine check and a document — it concedes the repo's numbers are correct and objects to a hypothetical future edit. Per CLAUDE.md's "When a check fails" procedure, a FINDING: check must assert a reproducible discrepancy; there is nothing here to assert. And the substantive question the documents actually raise — whether the exact F07 branch has been independently replayed well enough to move the shortcut from `rejected-by-both` to `open` — rests entirely on work/rank3_order4_exact_haar_run/ and work/rank3_order4_exact_haar_package_verify/, which are external to this repository and UNVERIFIABLE HERE, so neither the finding nor the documents can be settled on that axis from inside WORKHOUSE.

---

### 6.49 `recommendations-omit-the-one-wrong-value` — lane `ledger-graph`

The arithmetic reproduces exactly (Fraction(-160506019419340168451,14501180577204921600)+Fraction(-1474623,1675520) -> -11.948578179401377; gap to the repo value 6.7679e-13 = 381.0 ulps at ulp=1.7764e-15; B's -11.9485781794014 is 13 ulps), but the diagnosis "the repo is wrong" is refuted on five grounds.

(1) /home/user/WORKHOUSE/src/workhouse/constants.py:428 `RAW_FOLDED_AXIAL_GAMMA_NUM = -11.9485781794007` is a verbatim transcription of the corpus's own printed float at /home/user/WORKHOUSE/corpus-import/records/transcripts/15 hour RUN.txt:9112 (`rest_direct            = -11.9485781794007`), correctly _NUM-suffixed per CLAUDE.md rule 3 and registered in /home/user/WORKHOUSE/tests/test_constants.py:68. Two higher-precision prints in the same block confirm the run genuinely computed that value: :9130 `scalar folded formula = -11.948578179400714` (373 ulps from the exact reconstruction) and :9131 `matrix H4 Gamma = -11.948578179400696` (383 ulps). So this is not a transcription slip in the registry.

(2) The 6.8e-13 gap is the run's own self-disclosed numerical noise: the same block prints D = +2.01583808996259e-13 (exact value 0), fifth_residual_max = +2.41584530158434e-13, gamma_spread = +2.16715534406831e-13 (15 hour RUN.txt:9114-9121). A 6.8e-13 disagreement is ~3x that spread, i.e. the Haar-sampled pipeline's error, not a repo defect.

(3) The proposed "correct value" is derived from QUARANTINED_SCALAR, which /home/user/WORKHOUSE/src/workhouse/constants.py:426-427 records as "Rejected by both sides; recorded so it is never silently resurrected". Overwriting a recorded corpus float with a reconstruction built on a quarantined rational is precisely CLAUDE.md non-negotiable #2, and rule 1's record-preserving spirit.

(4) The repo already has the correct pattern for exact-vs-printed-float disagreement, and it is not "fix the constant": /home/user/WORKHOUSE/src/workhouse/invariants.py:404-417 (C20) keeps BOTH LINKED_VACUUM_4 = -1474623/1675520 and LINKED_VACUUM_4_ARTIFACT = -521965902/593076541 and asserts the ~31-ulp gap as a FINDING rather than editing either.

(5) The sub-claims about the documents are wrong. Artifact C (be0baa19-...:56-58) prints "raw folded rest `-11.9485781794007`" and cites `.../constants.py:426-435` — the range containing line 428 — endorsing it as the repository's record; B:208 and D:201 cite the same range. And B section 7 (6a2b59cb-...:204-208) explicitly REFUSES the relabel ("**This document does not make that change**"), so "B §7 recommends relabeling" misreads it.

Residual (weaker, and not this finding): nothing in the repo checks the identity ax_rest = QUARANTINED_SCALAR + LINKED_VACUUM_4, which fails by 381 ulps against the run's printed rest_direct; likewise rest_direct - float(LINKED_VACUUM_4_ARTIFACT) = -11.06847946377809 vs float(QUARANTINED_SCALAR) = -11.068479463778765 (6.61e-13). That would be a FINDING check on the corpus's internal consistency, never an edit to constants.py:428.

---

### 6.50 `relabel-scope-misses-downstream-sites` — lane `ledger-graph`

I opened every cited file at every cited line. The one reproducible element — `invariants.py:400` carrying the string outside D's cited range, printed live by `workhouse verify` — is real, but the finding surrounds it with three false sites (CERTIFIED.md carries none of the quoted JSON fields and zero occurrences of the string; FRONTIER.md zero, so its staleness test is irrelevant; triage.py:48 keys the name, not the verdict), two derived-not-independent sites (claims.jsonl:30 and :150 both regenerate from the two source sites), a misstatement of B's scope (B §7:208 also cites contradictions.yaml:36-40, the real ledger copy the finding never mentions), and a wrong kind: nothing in the repo has drifted or is stale, since B explicitly declines to make the relabel and every occurrence is currently mutually consistent. Per CLAUDE.md, findings get written into the ledger; this one would enter with false file:line evidence.

---

### 6.51 `routing-to-g3-reverses-adr-0002` — lane `ledger-graph`

The finding rests on a paraphrase that materially strengthens the ADR, and the repo pins the opposite.

(1) MISQUOTE OF THE ADR. /home/user/WORKHOUSE/docs/decisions/0002-anchoring-is-not-a-dispute.md:61-63 reads verbatim: "G3's scope narrows: it no longer *needs to* adjudicate a scalar. What it must settle is `C_shp`, and `Phi_C(0) = 0` proves no amount of Gamma-point precision can substitute for that." The finding drops "needs to" and reads it as "no longer adjudicates a scalar" — a prohibition. The sentence is a relief of a required burden plus a statement that Gamma-point work cannot SUBSTITUTE for C_shp. Adding a Gamma-point sub-entry does not substitute for anything; it adds. That sentence occurs exactly once in the whole repo (grep over *.md/*.py/*.yaml excluding corpus-import: one hit, ADR 0002:61) — it is not restated anywhere as a rule.

(2) THE REPO PINS G3 RETAINING SCALAR WORK. Inside the same G3 entry that encodes the narrowing (ledger/gaps.yaml:44-50), the 11-item frozen protocol keeps two scalar items: gaps.yaml:68 "independent scalar ledger testing q_band^(4) - E_0^(4) =? m_Gamma^(4)" and gaps.yaml:70 "both m_Gamma^(4) and C^(4) from the same run". tests/test_ledger.py:65-69 asserts len(g3["protocol"]) == 11, so those scalar items are test-pinned INTO G3. gaps.yaml:51 also keeps resolves: [C2, C3, C22], and C22 (contradictions.yaml:272-277, "Gate-85 equality") is a scalar-equality item. A scope that "no longer adjudicates a scalar" is refuted by the register itself.

(3) THE CITED ENFORCEMENT DOES NOT COVER THE PROPOSAL. tests/test_ledger.py:53-57 asserts only `"C1" not in g3["resolves"]` and `"C2" in g3["resolves"]`. A §6 item 3 (lines 149-150) proposes a prose one-liner — "the F07-vs-blind split is localized to size >= 2; the decisive test is the exact W22-off two-face recomputation" — which touches no `resolves` list, no terminology, and names neither C1, q_band, m_Gamma, nor the forbidden "m_4". The test passes unchanged. Nothing mechanical is reversed.

(4) NO SELF-CONTRADICTION. The documents' concession is narrower than the finding reports. A:140 "C1's `q_band` vs `m_Gamma` resolution stands (ADR 0002)"; B:218-219 "C1's `q_band` vs `m_Gamma` NAMING resolution stands". ADR 0002 and contradictions.yaml:12-19 dissolve exactly that PAIR, related by DELTA_GAMMA = 2.0827701250956417. The conflict the documents route to C2/G3 is a different pair: M4_SHORTCUT = -160506019419340168451/14501180577204921600 = -11.068479463778765 vs M4_ORACLE = -0.7751458630189173, gap 10.293333600759848 — not a DELTA_GAMMA anchoring shift, and separated by V_link = -1474623/1675520. That third quantity is already on the register as C1's "quarantined shortcut", status "rejected-by-both" (contradictions.yaml:36-40; constants.py:427; invariants.py:396-401), and C1's resolution text dissolves only the q_band/m_Gamma pair — it offers no dissolution argument for the shortcut. Affirming C1's dissolution while raising a conflict over a third, undissolved quantity is consistent, not contradictory.

Also, both documents explicitly decline to change the register (B:208 "This document does not make that change"; A:137-139 flags the relabel as a maintainer call under non-negotiable #2), so no disputed value is promoted.

ADJACENT, NOT ESTABLISHED (do not ledger it on this finding's evidence): A:78 and B:220 call the split "a sub-entry of C2/G3", and C2's own title (contradictions.yaml:64) is "Fourth-order off-axis coefficient C_shp", while ADR 0002:46-48 states Phi_C vanishes on every axial cut. An axial Gamma-point scalar split therefore sits awkwardly under C2 specifically. That is a routing-label question about C2, not an ADR 0002 reversal via G3, and the documents route to "C2/G3" jointly rather than to C2 alone; I did not reproduce it as a defect and it is not what finding #57 asserts.

---

### 6.52 `same-physical-quantity-is-asserted-not-shown` — lane `ledger-graph`

Refuted on three of its four supporting claims, each checked against the primary text.

(1) The quote is real: B:15-17 does say the two values "are branches of the *same* physical quantity, not rival estimates of different coordinates."

(2) "D §7 states the opposite in the same set" is FALSE. D:165-174 lists eight items the exact package does not prove; none says the scalars are differently anchored coordinates. D:167 says only that the F07 formula is not proven canonical — a different, weaker proposition. D §8 then states B's framing outright: D:180 heads the section "split the resolved naming issue from the newly genuine branch conflict"; D:182 keeps C1's anchoring resolution as applying to q_band^(4) vs m_Gamma^(4) and "unaffected by the exact F07 result"; D:193-199 proposes "a separate open contradiction" between exactly -11.068479463778765 and -0.7751458630189173, "status: open". D agrees with B rather than contradicting it, so the alleged same-author self-contradiction does not exist.

(3) "None of A/B/C/D tests whether the two are related by a translation-local shift" is FALSE. A:23 names document C as "the anchoring counterfactual; F07 value is invariant under the late diagonal shift"; A:63 is a T1 spine row "F07 anchoring-invariant — derivative of every upstream quantity w.r.t. the anchor scalar is 0 (audit C §4)"; A:84-86 concludes "so the gap is neither anchoring nor one-face; it is purely multi-face accounting." Uploaded C:65-67 adds that the late fit forces -0.775, not -11.068, which "existed earlier and is merely loaded for comparison after the oracle unblind." The ORACLE_COUNTERFACTUAL_AUDIT itself is not among the five uploads, so its content is unverifiable here, but the finding's factual claim about the document set is wrong.

(4) The evidence's arithmetic is tautological. I recomputed in exact rationals plus float: with M4_SHORTCUT = float(-160506019419340168451/14501180577204921600) = -11.068479463778765 and V_link = -1474623/1675520 = -0.8800987156226127, ax_rest = -11.948578179401377, local_shift = M4_ORACLE - ax_rest = 11.17343231638246, and (local_shift + V_link) - (M4_ORACLE - M4_SHORTCUT) = 0.0 exactly, gap = 10.293333600759848. But local_shift is DEFINED as M4_ORACLE - ax_rest (engine lines 7322-7326, cited C:44-45; repo src/workhouse/constants.py:434 RUN15_APPLIED_SHIFT_NUM; src/workhouse/invariants.py:414-422 records the final equality as target-derived). Any two numbers decompose this way, so the identity carries no evidence of an anchoring relation.

Positively, B does argue the sameness rather than merely assert it: B:66-73 shows the F07 one-face weight -13/896 + 39/1280 = 143/8960 = 0.015959821428571427 equals the blind size-1 c4 = +0.0159598214286, and M4_SHORTCUT = ax_rest - V_link (A:39, B:22) is already linked-vacuum-subtracted, i.e. in m_Gamma^(4)'s anchoring class rather than q_band^(4)'s, so ADR 0002's alternative is not simply available. The repo's own register agrees with B's framing: ledger/contradictions.yaml:36-40 files -11.068479463778765 as a third quantity of the same fourth-order rest scalar, "rejected-by-both", and src/workhouse/constants.py:425-426 says "Rejected by both sides"; nothing in the repo calls it a different coordinate. Nor does any promotion follow from the sentence: A:78 "Neither side is promoted", B:3-6 self-labels T3 with the physical adjudication "open", A:140 leaves ADR 0002 standing.

Adjacent but distinct, and not support for this finding: B:4 and B:17-19 write m₄, m₄,F07, m₄,blind for both branches, which brushes ADR 0002:24-26's forbidden "two m_4 values" phrasing, though B:31 heads the table "The three scalars (do not conflate)". That is a terminology observation, not the asserted circularity.

---

### 6.53 `three-new-fields-are-a-fourth-vocabulary` — lane `ledger-graph`

I re-opened every cited line. The repo text is quoted accurately (AGENTS.md:38-51 incl. "Do not introduce a fourth vocabulary." at :49; constants.py:26, :28-37, :39-55; CLAUDE.md:71-73; D:186-191 verbatim). The finding nevertheless fails on four independently checked points. (1) Its discriminating test is not a test the repo applies. D §8 amends a *quantity* record at ledger/contradictions.yaml:36-40. `grep -n "quantit" src/workhouse/ledger.py` returns NOTHING; the only enum check is `c["status"]` at ledger.py:165-167 against CONTRADICTION_STATUSES, i.e. the contradiction entry, never its quantities. I ran `validate(load())` from src/workhouse/ledger.py: it returns `[]`. (2) The criterion condemns the repo itself. The value currently in that exact slot is `status: rejected-by-both` (ledger/contradictions.yaml:40) — its sole occurrence anywhere in the repo — and I computed `'rejected-by-both' in (STATUSES|EVIDENCE|CONTRADICTION_STATUSES|GAP_STATES) -> False`. A criterion that flags the repo's own passing, checked-in line as a fourth-vocabulary violation is not a finding. (3) The mapping `quarantine_reason` IS the existing `note` field is factually wrong for the record type D edits: `note` is a field of the Constant dataclass (constants.py:49); C1's quantity records carry keys {decimal, kind, label, source, value, status} and no `note`. Moreover contradictions.yaml is already an open prose schema — across its 22 entries it uses 18 distinct keys, only id/title/status universal, with 11 appearing exactly once (machine_finding, by_construction_caveat, external_validation, terminology, cold_rerun, delta_gamma_as_printed, notes, evidence, sides, delta, quantities). Adding `quarantine_reason` is indistinguishable from those. (4) The split is compliance with, not a violation of, the cited rules: AGENTS.md:46-48 explicitly endorses recording truth status and evidence independently, and CLAUDE.md:71 makes that a non-negotiable; D proposes no change to STATUSES, EVIDENCE, CONTRADICTION_STATUSES, GAP_STATES or TIERS, and adds no tier. Separately the finding's `where` clause misdescribes the echoes: A:137-139 calls the relabel "a **maintainer call**" and names no new fields; B:208 states "**This document does not make that change.**" Neither proposes `arithmetic_status`/`physical_status`/`quarantine_reason` at all.

---

### 6.54 `validate-is-not-the-gate` — lane `ledger-graph`

I reproduced the mechanical core (validate() accepts unknown keys, a bogus nested status, and a routed C23 — all returning []) but the finding's three load-bearing conclusions do not survive. B names no gate at all (grep: zero hits for make status/make check across all five artifacts), so the artifact-wrong framing attacks a statement B never makes. The constants.py claim is directly falsified by Constant.__post_init__ (constants.py:51-55), which I executed and which raises at import on D's literal proposed status string. The new-contradiction claim is falsified by tests/test_ledger.py:20, which hard-pins C1-C22 with an explicit "cannot grow" docstring. What remains — ledger.validate is not a schema — is true, self-declared in the module docstring, and is a property of the repo rather than an error in artifact B.

---

### 6.55 `which-axis-actually-moves` — lane `ledger-graph`

Three checks, each against primary sources.

(1) The finding misattributes an evidence-axis proposal to the documents. Its `claim` field says B/D ask to relabel "status `falsified` / evidence `record-backed` / note ...". Neither document mentions the evidence axis. D:201 reads "change its metadata from `falsified` / `rejected by both sides` ... to ..." — status plus note. B:205-208 reads "relabeling `M4_SHORTCUT` from `rejected-by-both` / `falsified`" — the contradictions.yaml:40 quantity label plus status. D:184 is explicit: "The value `-11.068479463778765` should no longer be labeled `rejected-by-both`." The documents deliberately target the status axis, and the "rejected by both sides" ground for that status (constants.py:426 comment, :655 note, contradictions.yaml:40 `status: rejected-by-both`) is a factual assertion about branch rejection that D:159-161 contests. Contesting the stated ground of a status verdict is a status-axis argument, not an evidence-axis one. The finding's "they targeted the wrong axis" is therefore itself the overstatement it accuses B/D of.

(2) The finding's claim that "`cold-reproduced` needs a replay in this repo" is false as a statement about this repo's vocabulary. C7 at ledger/contradictions.yaml:122-138 carries `evidence: cold-reproduced` (:125) for a run executed OUTSIDE this repository, with the note at :136-137 stating the generating script "is absent from this repository; settlement/SHA256SUMS pins the transcript". settlement/CLAUDE.md:1-13 defines the whole directory as "Transcripts and harness code from runs executed outside this repository". ADR 0012 (docs/decisions/0012-in-repo-runs-are-pinned-evidence.md:9, :45-47) says in-repo runs are "simply what `cold-reproduced` always meant, with the generating script present instead of absent" — i.e. in-repo-ness is not the criterion. So the finding's ceiling argument ("highest presently supportable is `output-certified`") is built on a false premise: the external package is the C7 shape exactly, and cold-reproduced would be the natural class if its transcript were vendored and pinned. Note also that AGENTS.md:44 lists cold-reproduced ABOVE output-certified, so the finding's ordering claim runs the wrong way.

(3) C7 also refutes the finding's implicit principle that new run-evidence cannot bear on status: C7's status is `falsified` precisely BECAUSE a cold rerun refuted it (:116, :126-132). AGENTS.md:46-48 says the axes are independent — you cannot infer one from the other — not that evidence never justifies a status change.

Everything the finding cites checks out verbatim (constants.py:652 "falsified", :653 "record-backed", :655 "rejected by both sides"; C_shp both "disputed" at :628 and :636; B:213 "physically incomplete"; D:165-176 the eight non-closures; AGENTS.md:44), so this is a reasoning failure, not a citation failure. One further correction: B does not propose the change at all — B:208 says "**This document does not make that change**" and B:217 defers it to Alex; only D:201 actively recommends it. Writing this finding into the ledger as stated would record a false claim about the repo's own evidence vocabulary.

---

### 6.56 `143-8960-already-in-corpus` — lane `localization-argument`

Refuted on its substance, and factually wrong about one of the two documents.

(1) The interpretive core is false. The finding asserts 143/8960 is "a complete one-plaquette Rayleigh-Schrodinger gap coefficient, not a difference of two partial terms," and that presenting it as -13/896 + 39/1280 "obscures what it actually is." But /home/user/WORKHOUSE/corpus-import/programs/hodge_o4_adjudication/src/ENGINE_O4_hodge_rootonly_firewall_v1.py:221 reads `gap = tuple(axial[i] - vacuum[i] for i in range(ORDER + 1))`. The corpus DEFINES EXPECTED_GAP as the elementwise difference of EXPECTED_AXIAL and EXPECTED_VACUUM and gates that identity at :223-228 (`if gap != EXPECTED_GAP: raise GateFailure`). So the documents' arithmetic is verbatim the corpus's own construction of the constant, not a reframing of it. Recomputed exactly in python3 fractions: A[i]-V[i] == G for all five orders, True; -13/896 + 39/1280 = 143/8960 = 0.015959821428571427. Also false that vacuum/axial are "partial terms": each is a complete intermediate-normalized RS series returned by exact_energy_series (:159-215, docstring :162).

(2) Only the trivial half is true: :43 does read EXPECTED_GAP = (Q(8, 3), Q(1), Q(1, 2), Q(7, 32), Q(143, 8960)), one line below the :41-42 cited by B:78 and B:227 (and A:165). 143/8960 also appears at corpus-import/programs/hodge_o4_adjudication/notebooks/NB_O4_hodge_v10a29b_m5_first_no_m4_rerun.ipynb:20,65,66,388,415. That reduces to "B could have cited one more line" - a citation-completeness nicety, not a defect, since the value B computes IS EXPECTED_GAP[4] and B never claims the combination is novel (B:74 claims only that the two inputs are corpus-exact, which they are).

(3) The finding misreports document D. D does NOT cite ENGINE_O4_hodge_rootonly_firewall_v1.py at all - grep for '8960|EXPECTED_GAP|firewall_v1' over D returns only line 50. D:39 cites work/rank3_order4_exact_haar_package_verify/WORKHOUSE_RANK3_ORDER4_EXACT_HAAR_FINAL_AUDIT_20260823.md:124-126 and D:45 cites work/fold_linked_exact/README.md:21-27, both external to this repo and unverifiable here. So the premise "Both documents cite :41-42 and stop short of :43" is half wrong.

(4) The causal rider is unsupported. There are no "two readings needing reconciling": D:36 gives D11 = -13/896 (= EXPECTED_AXIAL[4], :42) and D:48-51 subtracts the vacuum to reach 143/8960 (= EXPECTED_GAP[4], :43) within the same section. The corpus relation between the two is exactly the subtraction D performs; no tension exists for D to have failed to notice.

A low-severity provenance note whose stated mechanism is contradicted by line 221 of the very file it cites should not enter the ledger.

---

### 6.57 `ax-rest-provenance` — lane `localization-argument`

REFUTED on all three legs; the raw arithmetic in the evidence line is right but every inference drawn from it is wrong.

(1) The central assertion — "neither cited source contains it" — is FALSE. /home/user/WORKHOUSE/src/workhouse/constants.py:427 holds QUARANTINED_SCALAR = Rational(-160506019419340168451, 14501180577204921600) and :430 holds LINKED_VACUUM_4 = Rational(-1474623, 1675520). Their sum, computed from that file alone, is exactly -86634244910174898583/7250590288602460800 = -11.948578179401376786, which prints as -11.9485781794014 at 13 dp — digit-for-digit B:36. So constants.py, one of the two sources B:46-47 names, DOES contain the value, in the exact-rational form CLAUDE.md rule 3 ("Exact stays exact") makes authoritative. B quoting the exact-derived value rather than the run's float is B following the repo's own convention, not a provenance gap. (The literal string -11.9485781794014 appears nowhere else in the repo, so constants.py:427+430 is the provenance.)

(2) The "matters because" clause is FALSE. It asserts the 6.8e-13 gap "is itself the whole residual in the local_shift + V_link identity." There is no residual: M4_ORACLE − M4_SHORTCUT = local_shift + V_link is definitional (M4_SHORTCUT = ax_rest − V_link, local_shift = M4_ORACLE − ax_rest), so ax_rest cancels identically. Evaluated in floats with BOTH ax_rest choices, residual = 0.000e+00 exactly in each case (lhs = rhs = 10.293333600759169 with the run float; 10.293333600759848 with the exact). B smooths nothing away, because nothing in that identity depends on the choice. What actually carries 6.8e-13 is a different relation the finding does not state: RUN15_APPLIED_SHIFT_NUM = 11.17343231638178 (constants.py:435) matches M4_ORACLE − run-float-ax_rest to 3.55e-15 (2 ulps) but M4_ORACLE − exact-ax_rest to only 6.80e-13 — i.e. the run's floats are mutually consistent, which is expected, not defective.

(3) The repo is not wrong either. constants.py:428 RAW_FOLDED_AXIAL_GAMMA_NUM = -11.9485781794007 carries the _NUM suffix, enforced by tests/test_constants.py:59-74 (test_float_only_values_are_named_num, name listed at :68), which per CLAUDE.md rule 3 marks it as a value the corpus records ONLY as a float. It is a faithful transcription of corpus-import/records/transcripts/15 hour RUN.txt:9112 "rest_direct = -11.9485781794007" (opened directly; the transcript's only three hits are :9112, :9130 = -11.948578179400714, :9131 = -11.948578179400696, none equal to ...014). It makes no claim about the exact value and is referenced by no check — its only other occurrences are the test guard and the generated index/claims.jsonl:229. So the 381-ulp separation between constants.py:428 and constants.py:427+430 is two deliberately different representations (run artifact vs exact gate), correctly labelled, not an inconsistency.

(4) The parenthetical about A:38 is empty: -11.9486 is the correct 6-significant-figure round of BOTH -11.948578179401377 and -11.9485781794007, so it "hides" nothing A claims — it simply does not discriminate at its stated precision.

What survives is at most that B:36 prints 14 sig figs without naming which constants.py representation it used — a documentation nit far below ledger threshold. Writing this up as a provenance finding would record a defect that does not exist, against an artifact that followed the repo's exact-over-float rule correctly.

---

### 6.58 `blind-table-does-not-close` — lane `localization-argument`

REFUTED. The arithmetic reproduces but the inference does not, and the finding as written would put a false statement into the ledger.

1) Arithmetic reproduced, with one error in the finding's own evidence. Exact-decimal sum of the six printed c4 values at /home/user/WORKHOUSE/corpus-import/records/transcripts/15 hour RUN.txt:10620-10625 = -0.7751458630184424382751163; printed TOTAL at :10626 = -0.7751458630189173; gap = +4.748617248837e-13. math.fsum and naive float both give -0.7751458630184425. So the numbers check out — EXCEPT the finding states the relative gap as "6.1e-11". It is 6.126e-13. The finding is wrong by a factor of 100 in its own headline quantifier.

2) The gap is 100% a print-format artifact, quantitatively accounted for. The generating source is in the same transcript. "15 hour RUN.txt":7680 prints the rows with 12 significant digits:
    x=bysize[k]; print(f'  size {k}: c1={x[1]:+.12g} c2={x[2]:+.12g} c3={x[3]:+.12g} c4={x[4]:+.12g}')
while :7681 prints the total with bare print() of a numpy float64, i.e. full 17-digit repr:
    print('  TOTAL m1/m2/m3/m4 =',totals[1],totals[2],totals[3],totals[4])
Row 6 is exactly -5/24 = -0.20833333333333334; '%+.12g' % (-5/24) reproduces the printed '-0.208333333333' exactly, with error +3.3333333333e-13. Row 1 is exactly 143/8960 = 0.015959821428571427 (the orchestrator-established one-face gap); '%+.12g' reproduces '+0.0159598214286' exactly, error +2.857142857e-14. Those two known-exact rows alone contribute +3.619047619e-13 of the observed +4.748617249e-13 — 76% of it. The residual +1.129569630e-13 is attributable to rows 2 and 3, whose combined half-ulp allowance at 12 sig digits is 1.0e-12. Total worst-case print-rounding budget across the six rows is 1.550e-12; the observed gap is 0.306 of it. Nothing is unexplained.

3) The inferential core of the finding is therefore false. The finding asserts "the per-size table ... is only known to ~1e-13 per row, so no per-size claim can be tighter than that." The rows are only DISPLAYED to 12 significant digits. bysize[k] is a float64 numpy array. Decisively, :7678 accumulates both quantities from the identical vector inside one loop:
    omega[C]=x; totals+=x; bysize[len(C)]+=x
so sum_k bysize[k] and totals differ only by float re-association, ~1e-16, not 4.7e-13. The finding mistakes a format string for an epistemic limit.

4) Stating this finding would be actively harmful here. -0.7751458630184424 rounds at 13 digits to -0.7751458630184, which is already a load-bearing and semantically DISTINCT string in this repository: Hamer's 8*a_4, recorded at /home/user/WORKHOUSE/literature/index.yaml:495-496 ("8 a_4 = -0.7751458630184, agreeing with m_Gamma^(4) = -0.7751458630189173 to 5.17e-13 -- the strongest external validation the program has"), /home/user/WORKHOUSE/src/workhouse/settlement.py:51, /home/user/WORKHOUSE/settlement/mce_adjudication_harness.py:73, /home/user/WORKHOUSE/tests/test_settlement.py:73, and guarded as a target-blindness gap at /home/user/WORKHOUSE/ledger/gaps.yaml:118-120 and /home/user/WORKHOUSE/src/workhouse/invariants.py:646-648. Writing "the blind rows sum to -0.7751458630184" into the ledger injects a third, spurious provenance for exactly the digit string those guards exist to track. A false finding costs more than a missed one; this one costs a lot.

5) Two smaller corrections to the candidate. Its citation "A §2 line 64" is wrong: the row is at line 62 of 52ebdfa7-RANK3_ORDER4_MASTER_RECORD.md ("| blind table closes | T2 | Σ per-size `c4` = oracle `−0.7751458630189` (`:10626`) |"). B's citation is right: line 195 of 6a2b59cb-F07_VS_BLIND_TWOFACE_ADJUDICATION.md. Also, A's quoted number -0.7751458630189 is the correct 13-sig-digit rounding of the oracle at :10626; A quotes the ORACLE, and cites :10626 (the TOTAL line), not the row lines. Reading A's row as an assertion about re-adding the printed strings is the auditor's construction, not A's.

WHAT IS SALVAGEABLE (a different finding, not this one). Because :7678 accumulates totals and bysize from the same x in a single loop, "Σ per-size c4 = oracle" is a float re-association identity, not an independent check. A §2:62 tiering it "T2" and B §6:195 tiering it "T2" therefore both label a near-tautology as a numerical verification, and neither states a tolerance, which CLAUDE.md's T2 definition ("float agreement within a stated tolerance") requires. That is a real overstatement — but it is "the check is definitional and untoleranced", not "the table does not close". Separately, B's check script f07_twoface_adjudication_check.py referenced at B:187 is not present in artifact E and is unverifiable here.

---

### 6.59 `no-crosswalk-vs-termwise-comparison` — lane `localization-argument`

REFUTED on its central assertion, and one checkable sub-claim is outright false.

1. No self-contradiction. D §4 (D:127-136) scopes "no termwise map" to four named *inventories* (69,800 Haar classes / 203-609 rooted marked-cluster weights / 3,895 Stage-3H / 189 kernel). In the same section D:110 states the opposite of what the finding attributes to it: the F07 pair-collapse "uses the W2/R2 support labels to identify and skip the separate one-face term", then aggregates the *rest* by trace states. So D asserts one-face-is-separable AND full-rooted-crosswalk-is-missing, which are compatible. The finding's premise that "D §4 denies (i) and (iii) outright" is an overreading of a statement about four enumerations.

2. "no F07 face decomposition of any kind has ever been run" is false about the repo, and is contradicted by document B itself (B:122-138). /home/user/WORKHOUSE/corpus-import/programs/hodge_o4_adjudication/src/ENGINE_O4_hodge_v10a21r_adjudicator_only_same_kernel.py builds exactly one: `_v21_size_table` (:132-137); support-graded `D_MIN` with `skip_11=True, analytic_11=_XQ(-13,896)`, plus `E2_MIN,N_MIN,J_MIN,C_MIN` (:313-318); `EA_MIN` (:335-340); `V_MIN` from `V1=-39/1280` per single embedding and `VPAIR=-327/83776` per pair (:359-367); `DELTA_MIN=EA_MIN-V_MIN` (:377-380); size tables printed at :348-351 and :447-452. Never executed ("Stop. Do not run v10a.21r." — Monday 531 PM.txt:1978, verified verbatim, with :2287,:2925,:3702) and circular as an adjudicator (its incidence transform is the Mobius inverse of the zeta transform of DELTA_MIN, so `max_resid==0` at :441 is a tautology) — but that is precisely what B §4 already says, including refusing to read off its size-2 and encoding a provenance guard (B:130-153,196).

3. The finding's logical conditions are overstated. Localising the *gap* to "not one-face" needs only a one-face/rest split on each side, not a full termwise map. Condition (ii) (residue-free) provably HOLDS on the F07 side: gate "v10a.21 minimal marked-history ledger sums to exact v10a.20 m4", `_v21_sum(DELTA_MIN)==M4_EXACT` (:383-385); and on the blind side to 5.17e-13. Only (iii) is genuinely open, and all three documents already say so — D:63 hedges "or in their P-return/fold/incidence accounting", B:196 marks the two-face adjudication OPEN, A:99-104 gates the two-face test behind D §9's five unmet conditions. So the documents do not "draw a global conclusion" from a comparison they disclaim; they draw an explicitly-labelled-open one.

4. The concrete evidence is half-real and aimed at a comparison nobody makes. The union-convolution mechanism IS real and verifiable: `E2N_MIN=_v21_union_convolution(E2_MIN,N_MIN)` (:333, comment :331-332), entered into `EA_MIN` with weight -1 (:338) — so a product of two two-face entries is indeed assigned to the union support. But "+34.97 to +38.15" is UNVERIFIABLE here: E2_MIN/N_MIN require same-kernel prerequisites (`W1X,R1X,_single_emb,_pairs,...`, :23-38) absent from the repo, and the cell was never run. I can only bound the scale: -e2*N = -(-5945/612)(511051/124848) = +3038198195/76406976 = +39.76336133234746 exactly, and FOLD = -e2*N + J = +37.84159226508323, so a +35..+38 off-diagonal slice is arithmetically possible but unreproduced. And the size-3 comparison it warns against is one B:130 explicitly says "Do not" perform.

Exact chain independently reproduced: EA = D_EXACT - 2*C(=0) - e2*N + J = -86634244910174898583/7250590288602460800 = -11.948578179401377; EA - V_link = -160506019419340168451/14501180577204921600 exactly. Also V_link = 13*V1 + 124*VPAIR is the unique small-integer solution of -51051a-6540b = -1474623.

SEPARATE RESIDUAL WORTH ITS OWN CANDIDATE (not a narrowing of #94, so left out of corrected_statement): the F07 one-face weight 143/8960 is *asserted*, never computed. In the one available graded ledger it is DELTA_MIN[{ROOT}] = D_MIN[{R}] - 2*C_MIN[{R}] - E2_MIN[{R}]*N_MIN[{R}] + J_MIN[{R}] - V_MIN[{R}]. D:45-52, B:66-71 and A:82 all silently take it to be D_11 - V1 = -13/896 + 39/1280 = 143/8960, i.e. they assume C_MIN[{R}], J_MIN[{R}] and the size-1 union-convolution term E2_MIN[{R}]*N_MIN[{R}] all vanish. Nothing in the repo checks any of the three (the gates at :322-329 constrain only the *totals*: e2 sums to -5945/612, N to 511051/124848, J to -48945521/25468992, C to 0). B:126-127's "Its size-1 weight is 143/8960" carries no line cite and cannot, since v10a.21r was never executed. That is a checkable, sharply stated gap; #94 as written is not.

---

### 6.60 `rivals-claim-unsupported` — lane `localization-argument`

Refuted on three of its four legs; the surviving leg is not a defect.

(a) "M4_SHORTCUT is not an input to the oracle - TRUE and already recorded." Agreed, and I confirmed it (ADR 0002 Decision item 4; /home/user/WORKHOUSE/ledger/contradictions.yaml:55-61). But that means the artifacts are CORRECT here. A:46-47 and B:46-47 present these as "re-verified this session", not as new. Correctly restating a recorded fact is not an overstatement.

(b) "contradicted by D section 7" - REFUTED. D:167 says it is not yet proved that the frozen F07 formula IS the canonical physical coefficient. That is not a contradiction of "the two are branches of the same physical quantity"; it is the same open-adjudication posture B itself declares at B:4-6 ("the physical adjudication it localizes is open") and B:217-221 ("the open item is the F07-vs-blind multi-face split"). Worse for the finding: D:169 lists "rooted linked-cluster equality in the multi-face sector" as an open item, which PRESUPPOSES the two branches are commensurate. D supports B's framing rather than contradicting it.

(c) "unsupported" - overstated. B section 2 (B:51-87) supplies the support and it is machine-checkable: the F07 one-face weight -13/896 + 39/1280 = 143/8960 equals the blind size-1 c4 (15 hour RUN.txt:10620) to printed precision, sourced from ENGINE_O4_hodge_rootonly_firewall_v1.py:41-42, DATA_O4_OrderSchedule_Occurrence_Preflight_CPU.py:615, ENGINE_O4_hodge_v10a21r...py:313,358. Exact agreement of the size-1 rooted weight AFTER the same V1 = -39/1280 vacuum subtraction is evidence of shared normalization and anchoring - precisely what a differently-anchored-coordinate reading would have to explain away. Not conclusive, but it is support, and it is checks #1-#2 of the companion screen (B:191-192).

(d) "Structurally this pair has the C1 shape ADR 0002 warns about" - REFUTED, and this is the finding's own error. M4_ORACLE is float(totals[4]) at engine :7309, the rooted-incidence total, computed with no reference to ax_rest; local_shift is DEFINED at :7324 as M4_ORACLE - ax_rest, i.e. the discrepancy itself renamed. So "M4_ORACLE = ax_rest + local_shift" carries zero structural content. The C1 pair is not analogous: there Delta_Gamma is a genuine, independently meaningful vacuum-subtraction offset between two constructions; here local_shift is the residual. The finding's replacement framing - "a disagreement about the size of the vacuum/linkage subtraction applied to a shared ax_rest, 11.1734 versus 0.8801, a factor of 12.7 - not about multi-face axial accounting" - is therefore strictly LESS informative than B section 2's localization, and is affirmatively misleading, since the oracle applies no subtraction to ax_rest at all.

(e) "10.293 is not a third datum" - true but trivial. Neither document treats it as one; both write it as |M4_ORACLE - M4_SHORTCUT| (A:42, B:41).

Numerics reproduce but do not carry the claim. Exact ax_rest = QUARANTINED_SCALAR + LINKED_VACUUM_4 = -86634244910174898583/7250590288602460800 = -11.948578179401377. local_shift from exact ax_rest = 11.17343231638246, and local_shift + float(LINKED_VACUUM_4) = 10.293333600759848, bit-identical to |M4_ORACLE - M4_SHORTCUT| (residual exactly 0.0). The finding's 6.803e-13 residual appears only because it substituted constants.py:435 RUN15_APPLIED_SHIFT_NUM = 11.17343231638178. Its attribution of that residual to the ax_rest float error is directionally right but imprecise: the run's own float is -11.948578179400714 (15 hour RUN.txt:9130), 6.63e-13 = 373 ulps below exact, not the 6.77e-13 = 381 ulps the evidence line computes from the rounded :9112 print. Either way this confirms only the definitional identity the orchestrator already granted.

Finally, the one grain that could be salvaged - that B:15-17 states the same-quantity identification as a premise rather than as a checked result - is not recordable. B:4-6 labels the whole document T3 (asserted) and B:203-221 declines to relabel M4_SHORTCUT in contradictions.yaml:36-40, defers the judgement to Alex, and cites non-negotiable #2 while doing so. T3 prose inside a document that correctly declares itself T3 is the repository's normal state, not a finding. Writing this into the ledger as "overstated" would put an unsupported interpretive claim into the register while the artifacts' own status discipline is intact.

---

### 6.61 `v10a21r-size1-claim-false` — lane `localization-argument`

REFUTED. The finding's code reading is correct but its arithmetic conclusion is false: the "missing fold correction" is exactly zero, so B's statement stands.

Verified structural facts (all true, from primary source): _v21_union_convolution at ENGINE_O4_hodge_v10a21r_adjudicator_only_same_kernel.py:122-127 puts E2_MIN[{R}]*N_MIN[{R}] at the singleton; EA_MIN = D +1, C -2, E2N -1, J +1 at :336-339 (finding cites :334-338, off by ~1); D_MIN[{ROOT}] = -13/896 exactly, since skip_11 at :212 removes every 1x1 pair (the only source of a singleton union support, C = tSL|SR) and :295-296 injects analytic_11 (call site :312-314); V_MIN[{ROOT}] = V1 = -39/1280 because _single_emb = sorted(_V17_NEIGH[_mark]) (v10a7:5448) with _V17_NEIGH = [frozenset(face_support_faces[f])] "# includes self" (v10a7:5224), gate len==13 (v10a7:5460), and _mark = _vac_seed = _cycle_root = face at v=(0,0,0), pol (0,1) (v10a7:5401,5292) == anchor_faces[2] = ROOT (T1_POLS[2]=(0,1), v10a7:4491,5570), so frozenset((ROOT,ROOT)) collapses to the singleton at v10a21r:361-363. I also independently confirmed 13*V1 + 124*VPAIR = -1474623/1675520 exactly, unique small solution (13,124).

Where the finding fails: the correction -2C[{R}] - e2[{R}]*N[{R}] + J[{R}] is the one-face (1x1) sector, computed in closed form by _v10a11_oneface_axial_character() at ENGINE_O4_hodge_v10a24c_rootedfullt1_dualcoldoracle_a100.py:5330-5359, which returns e1,e2,sigma3,N,C,J,D as SEPARATE keys (so -13/896 is indeed only the D key, as the finding assumes). I re-ran that exact 4x4 construction in fractions.Fraction (odd irreps (1,0),(2,0),(3,0),(2,1); su3_c2_pq at :3235, fusions at :3240,:3248) and got exactly: e1=1, e2=-1/4, sigma3=0, N=1/16, C=0, J=-1/64, D=-13/896. Hence -2C - e2*N + J = 0 - (-1/4)(1/16) + (-1/64) = 1/64 - 1/64 = 0 EXACTLY. Therefore EA_MIN[{ROOT}] = -13/896 and DELTA_MIN[{ROOT}] = -13/896 + 39/1280 = 143/8960, exactly what B §4:126-127 asserts.

Corroboration: ENGINE_O4_hodge_rootonly_firewall_v1.py:40-42 pins EXPECTED_AXIAL[4] = -13/896, EXPECTED_VACUUM[4] = -39/1280, EXPECTED_GAP[4] = 143/8960 - i.e. the corpus already records the one-face AXIAL order-4 coefficient (not merely the D block) as -13/896, which is only consistent if the fold correction vanishes. The one-face prefix (8/3, 1, 1/2, 7/32, 143/8960) also appears in NB_O4_hodge_v10a29b_m5_first_no_m4_rerun.ipynb and NB_O4_hodge_v10a24c_section15_reduced_gpu_benchmark_fresh.ipynb.

Residual true-but-too-weak observation, not worth a ledger entry: the finding is right that no v10a.21/21r size-table OUTPUT exists in the repo (every "size sums=" hit is source or notebook code, never run output), so B's size-1 value is analytic-from-source rather than output-certified. But it is exactly derivable from the engine source plus the one-face character, as above, and B's surrounding paragraph (:129-152) explicitly refuses to use any v10a.21r number as evidence - so there is no misuse to record.

---

### 6.62 `w22-o4-nullity-understated` — lane `localization-argument`

Reproduced all cited arithmetic, then found the finding fails on three of four components. (1) `where` is wrong: D §2 line 91 states the general result explicitly ("exact perturbative power counting places the first W22 contribution at fifth order, so the mere presence of the block does not prove that it changed the true fourth-order Taylor coefficient"), and B §5 :167-170 makes no one-face restriction — so the documents do not "invert the evidential situation". (2) The premise that A hides the general gate is false: A:166 cites ":610,614,616", and :610 IS the order-five gate; A §2 line 59 ("exactly O4-null at one face; first bite O5 = -5/7168", cited to :614,616) is a true, correctly-cited statement, not a wrong one. (3) The conclusion "the named suspect has no support" is refuted: the suspect is W22 leakage into a finite-u degree-6 fit on 13 points (A:90, B:167-170, D:91, ENGINE…v10a24c…py:6928-6946), which is untouched by — indeed sharpened by — the order theorem being general, since fit truncation then becomes the sole contamination channel and A's Knob B (:104,:108) remains the correct discriminator. Additionally the finding ignores that the repo itself treats multi-face W22 as ungated: item10_W22_toggle is hardcoded OPEN with no path to closure, which is itself a registered FINDING at invariants.py:664-678, and README:38 lists the 33-rooted-class W22 toggle as an outstanding must-do. Filing this as high-severity artifact-wrong would put a false statement in the ledger; what remains is one imprecise word in one sentence of A.

---

### 6.63 `blind-table-does-not-close` — lane `rules-compliance`

REFUTED on four independent grounds. The row A:62 is correct as printed; the "gap" is a display-rounding artifact, and the finding's headline number is produced by the very error it accuses document B of.

(1) THE FINDING'S OWN SUM IS WRONG — it drops two rows. `/home/user/WORKHOUSE/corpus-import/records/transcripts/15 hour RUN.txt:10620-10625` prints six per-size c4 values: +0.0159598214286, -0.403971702978, -0.178800648136, -1.3933298959e-14, -2.85049761573e-14, -0.208333333333. Summed in printed order as doubles these give -0.7751458630184424603, NOT the -0.77514586301840005 the finding asserts. That quoted value is the sum of only FOUR rows — it silently discards sizes 4 and 5, which is precisely the omission the finding condemns in B §2 (lines 60-61, "~0 (numerical zero)"). |Σ(all 6) − TOTAL| = 4.748e-13 (4277 ulps), not 5.1725e-13.

(2) THE "BIT-IDENTICAL TO 8*HAMER_A4_NUM" CLAIM COLLAPSES, AND IS CONTENTLESS ANYWAY. Σ(all 6) = -0.7751458630184424603 vs 8*HAMER_A4_NUM = -0.77514586301840004978: they differ by 4.2407e-14 = 382 ulps, so bit-identity is FALSE for the actual table. It holds only for the truncated 4-row sum, and there it is a decimal-printing coincidence carrying zero information: the four strings 0.0159598214286, -0.403971702978, -0.178800648136, -0.208333333333 sum in EXACT decimal to exactly -0.7751458630184 (verified with fractions.Fraction), and 8 × float("-0.0968932328773") is exact in binary because ×8 is a power of two, so both expressions land on the double nearest the same 13-digit decimal. It is not evidence that "the table reproduces Hamer's a_4 rounding rather than the oracle float".

(3) THERE IS NO DISCREPANCY TO REPORT: the gap is far inside the print precision of the summands. The per-size values carry 12 significant figures. Half-ulp of the last printed digit is 5e-14 (size 1) and 5e-13 each (sizes 2, 3, 6), so Σ(printed) can legitimately differ from the true sum by up to 1.55e-12. Observed 4.748e-13 = 0.306 of that budget. Two rows are identifiable exactly and account for most of it: size 6 c4 = -5/24 = -0.20833333333333334, printed -0.208333333333, contributing -3.333e-13 alone; size 1 c4 = 143/8960 = 0.015959821428571427 (the T1 value in A:57), printed 0.0159598214286, contributing -2.857e-14. The residual after those two is 1.554e-13 — inside the ±5e-13 print budget of sizes 2 and 3 by itself. The table closes to every digit at which it is printed.

(4) THE SAME TRANSCRIPT PROVES THE TOTAL LINE, NOT THE PRINTED ROWS, IS THE FULL-PRECISION QUANTITY. `15 hour RUN.txt:10627-10630` validates TOTAL m2 = 0.03594771241824929 against exact 11/306 (gap 5.136e-14) and TOTAL m3 = -0.4371355568371267 against exact -109151/249696 (gap 1.277e-14). The identical ~1e-13 "failure to close" appears in the m2 and m3 columns of the very same table (Σ printed c2 ≈ 0.0359477124179, Σ printed c3 ≈ -0.4371355568494) and no one calls those broken. Comparing 12-sig-fig display values against a 17-sig-fig total is a category error, applied selectively here.

(5) THE 5.17e-13 RESIDUAL IS NOT AN UNRECORDED DISCOVERY — IT IS AN EXISTING T2 CHECK WITH A STATED TOLERANCE. `/home/user/WORKHOUSE/src/workhouse/invariants.py:388-395`: check "Hamer 8*a_4 matches m_Gamma to ~5.2e-13", d = |8*HAMER_A4_NUM − M_GAMMA_4_NUM| < HAMER_TOLERANCE, detail line "|diff| = {d:.2e}"; HAMER_TOLERANCE = 5.3e-13 at `src/workhouse/constants.py:264`. Re-registered at `invariants.py:1299-1315` with the literature pin. So the quantity the finding says "the row hides" is already machine-checked, tolerance-bearing, and documented at `constants.py:203-207`.

(6) THE CLAUDE.md CHARGE MISREADS THE TIER TABLE. "T2 numerical | float agreement within a stated tolerance | same, tolerance in the detail line" locates T2 in `src/workhouse/invariants.py`'s (passed, detail) return — it is the rule for registering an invariant, not a formatting rule for a collaborator's markdown summary. A and B are uploaded documents, not repo checks. Every T2 row in A §2 is tolerance-free (line 58, "one-face agreement", equally so), making the complaint generic rather than a finding against row 6.

(7) WHAT THE ARTIFACTS ACTUALLY SAY IS TRUE. `15 hour RUN.txt:10626` reads "TOTAL m1/m2/m3/m4 = 1.0 0.03594771241824929 -0.4371355568371267 -0.7751458630189173"; A:62 renders it -0.7751458630189, a correctly rounded 13-sig-fig transcription of the cited line. B §6 check 5 (line 195) is weaker still, printing "-0.775145863…" with an explicit ellipsis. Neither overstates.

ONE SEPARATE, MUCH WEAKER OBSERVATION (not this finding, and not verifiable here): no check named `blind_table_sums_to_oracle` exists in `src/workhouse/invariants.py` (grep for 10626 / "per-size" / "ROOTED INCIDENCE" returns nothing), and the extracted certificate bundle E contains no occurrence of the string "0.7751458630" in any of its 19 files. So A §2's preamble "reproducible via the check" is unbacked in this repo and in bundle E; the check, if it exists, lives in the external `work/rank3_order4_*` trees and is UNVERIFIABLE HERE. That is a citation-provenance issue of low severity, not the claimed high-severity "the table does not close".

---

### 6.64 `derivative-language-for-a-grep` — lane `rules-compliance`

REFUTED — the finding's central identification is an auditor lettering error, and the substance it attacks is verifiably true from repo primary source.

1) Two different lettering schemes. The orchestrator labels the uploads A-E; artifact A carries its OWN internal legend at A:19-26 (`## 0. The document set`), which is a different, six-item scheme: internal A=`DENOMINATOR_LOCALIZATION_INVESTIGATION`, B=`W2_R2_ORACLE_LINEAGE_TRACE` (= the upload the orchestrator calls C), C=`ORACLE_COUNTERFACTUAL_AUDIT`, D=`F07_VS_BLIND_ORACLE_STRUCTURAL_TRACE` (= upload D), E=`F07_VS_BLIND_TWOFACE_ADJUDICATION` (= upload B), F=`F07_VS_BLIND_COORDINATION_NOTE`. A:63's "(audit C §4)" therefore points at `ORACLE_COUNTERFACTUAL_AUDIT`, described at A:23 as "the anchoring counterfactual; F07 value is invariant under the late diagonal shift" — a counterfactual re-run, not a search.

2) The grep is cited by a DIFFERENT row, and is not tiered T1. The scoped-search sentence the finding quotes lives at upload C:110-113 (= internal B §2). A cites it one line lower, at A:64: "| F07 oracle-free | — | two independent scanners, zero leakage (B §2, C §3) |" — tier column "—", explicitly not T1. So no one dressed that grep as T1 calculus; the finding cross-wired A:63's citation onto A:64's evidence. Nothing in the delivered set shows internal C §4 is a grep; the finding assumes it.

3) The substance of the A:63 row is true and I reproduced it from the repo, not from a document. In /home/user/WORKHOUSE/corpus-import/programs/hodge_o4_adjudication/src/ENGINE_O4_hodge_v10a24c_rootedfullt1_dualcoldoracle_a100.py: `M4_SHORTCUT` is a hardcoded rational literal at :7310 (`_V23CF(-160506019419340168451,14501180577204921600)`); `ax_rest=float(V23_AXIAL_SHAPE['rest_direct'])` reads the pre-unblind shape and `local_shift=M4_ORACLE-ax_rest` is only defined on that same line :7324; `local_shift` is then used at exactly one place, :7326 (`K4_mass_cols[int(f),a]+=local_shift`). grep -n over the whole 307,724-byte engine returns local_shift only at 7324, 7326, 7329. So every F07-branch upstream quantity is independent of the anchor scalar by lexical construction — a one-line dataflow fact, and the claim it supports is correct.

Verified secondary points (true but not load-bearing): "derivativ" occurs exactly once across all five artifacts (A:63) and zero times in the extracted certificate set; `ORACLE_COUNTERFACTUAL_AUDIT` and `f07_twoface_adjudication_check.py` are not in the uploads dir or the cert zip; the repo quote at src/workhouse/invariants.py:654-661 is accurate. The finding's own concession ("the audit cited (internal C §4) was not delivered") shows it half-recognized the lettering, then still equated the row with upload C §2's grep in the same paragraph.

Residual worth noting, but too weak to be finding #113 and not what #113 says: A:53 asserts "Every row is T1 (exact) or T2 (numerical), reproducible via the check", yet A:63's sole cited support is a document absent from the delivered set, and "derivative ... w.r.t. the anchor scalar" is metaphorical for a discrete dataflow argument. That is a citation/tier-hygiene defect in a T3-self-labelled index document (A:3-7 already labels itself T3), not the "grep re-dressed as calculus" that #113 alleges. Writing #113 as stated into the ledger would record a false attribution.

---

### 6.65 `master-record-rounds-away-the-live-finding` — lane `rules-compliance`

REFUTED as an artifact-wrong finding, though its arithmetic mostly reproduces.

WHAT REPRODUCES. D_EXACT = -361008126292641364183/7250590288602460800 (corpus-import/records/audits/08-rooted-adjudication.md:53) plus FOLD_EX = 5315003/140454 (corpus-import/records/audits/07-denominator-lift.md:38) equals exactly -86634244910174898583/7250590288602460800 = -11.948578179401377. src/workhouse/constants.py:428 registers RAW_FOLDED_AXIAL_GAMMA_NUM = -11.9485781794007; the gap is 6.7740e-13 (the finding says 6.768e-13, 0.09% off), = 255.32 ulps at ulp=2^-52*|x|, 381.3 at math.ulp, 510.65 at 2^-53*|x|. Artifact A line 38 prints -11.9486 (2.1821e-05 from exact); artifact B line 36 prints -11.9485781794014 (2.248e-14 = 12.7 math.ulp). `workhouse triage` over the upload directory does rank A last and lists only "linked vacuum" for it.

WHY IT FAILS ANYWAY.

1. A asserts nothing false. -11.9486 is the correct 6-significant-figure rounding of -11.948578179401377, as are -11.0685 (of -11.068479463778765) and -0.7751 (of -0.7751458630189173). A also prints 10.293333600759848 at full precision at line 42, so it is not uniformly rounding; it rounds a three-row orientation table and self-labels "T3 (asserted) — a front-door index and synthesis" at line 3, pointing readers to F and to the runnable check. Rounding a summary row is an editorial choice, not an error, and "artifact-wrong" is a mischaracterization.

2. Nothing was rounded away. The repo-vs-exact discrepancy appears in NO artifact in the set. Artifact C line 57 prints the repo's -11.9485781794007; artifact B line 36 prints -11.9485781794014; neither flags any gap, and neither compares against D_EXACT+FOLD. A therefore cannot have destroyed a "live finding" the corpus of artifacts never contained. (The genuinely interesting residue here is that B:36 and C:57 disagree by 6.8e-13 on the same named scalar — but that is a different finding, about B and C, not about A.)

3. "the single number in the set where this repository is measurably wrong" is not supported. constants.py:428 faithfully transcribes theory/superseded/MASTER_THEORY.md:416, which itself records "-11.9485781794007" as the raw folded axial Gamma-block. Per CLAUDE.md rule 3 a corpus-recorded float stays a float with a _NUM suffix, which is what happened. Grep over src/, tests/ and ledger/ shows the symbol is referenced exactly twice: its definition (constants.py:428) and the float-naming guard (tests/test_constants.py:68). No check consumes it, no tolerance is attached, nothing fails. Whatever discrepancy exists is between two corpus records (a document float vs the exact sum of two other corpus rationals), exists independently of artifact A, and would need to be stated as a FINDING against the corpus — not charged to A's summary table.

4. The mechanical/retrievability sub-claim's stated cause is false. src/workhouse/triage.py:41-58 matches a fixed 14-name SIGNATURES roster with MIN_SIGNATURE_DIGITS=8. A does carry seven exact rationals at lines 57-61 (-13/896, 39/1280, 143/8960, -5/7168, -54321/837760, -327/83776, -1474623/1675520, 1675520=1280*1309=83776*20) and a 13-digit float -0.7751458630189 at line 62. Only -1474623/1675520 is on the roster; the other six are absent from it at any precision. So "every other coefficient in it is rounded below the signature threshold" is wrong. Only the quarantined-scalar and m_Gamma^(4) misses are rounding-caused (m_Gamma^(4)'s signature is the full repr digit string 07751458630189173, which A's 13-digit truncation misses; B matches because B:18-20 and B:63 print -0.7751458630189173 and -11.068479463778765 in full).

Net: the underlying number is real and worth stating somewhere, but as written this finding blames the wrong document for a corpus-level transcription question, misstates the repo's status, misstates its own gap figure, and gives a false mechanism for its one mechanical observation. Writing it into the ledger would record a defect in A that does not exist.

---

### 6.66 `proposed-adr-duplicates-three-rules` — lane `rules-compliance`

REFUTED — the finding is an artifact of reading only the gloss clause of the item it cites.

1) The cited evidence is factually correct but does not support the claim. I confirmed verbatim: CLAUDE.md:71-73 (non-negotiable #5, "'Certified' is never a synonym for 'proved'"); docs/decisions/0001-verify-do-not-adjudicate.md Context ¶2 ("a scientific error wearing an engineering disguise: the exact rational's *upstream identification* is precisely what is in question, and its exactness says nothing about it"); docs/decisions/0010-external-tools-enter-through-evidence-tiers.md:31-32 ("an enclosure-certified check is still T2 — 'certified' here means the *comparison* is rigorous, never that the claim is proved"); docs/decisions/ holds 0001-0012, so 0013 is next free.

2) The claim "names no failure they do not already prevent" is false on the artifact's own text. Artifact A:151-152 reads "**ADR** — the meta-pattern (§5): exactness certifies arithmetic, never physical identification." The "(§5)" reference is normative, and A:134-136 defines the meta-pattern as two items at two scales: "The capstone (a value passing all gates yet physics-open) and the v10a.21r trap (a decomposition passing all gates yet non-adjudicating) are one lesson at two scales — a concrete sharpening of non-negotiable #5." The v10a.21r trap is exactly what the finding declares to be new, ADR-uncovered, and "the ADR worth writing at id 0013". The finding cites A:134-136 in its own `where:` field while asserting the proposal lacks that content, and its recommended action (write ADR 0013 about the v10a.21r wired-decomposition pattern) is the action A already proposes at the next free id. The finding argues with the one-line summary and reaches the artifact's own conclusion.

3) The concealment premise fails: A:136 explicitly self-labels the item as "a concrete sharpening of non-negotiable #5", so derivation from #5 is declared, not disguised, and the maintainer's rule (CLAUDE.md:33-41) — which targets rules that fail to *name* the failure they prevent — does not bite on an item that names one (the v10a.21r non-adjudicating decomposition, detailed in artifact B:118-150).

4) The finding's own distinctness argument is weaker than stated, further undercutting it. The "true by construction certifies bookkeeping, not independent agreement" lesson is already generalized in ledger/contradictions.yaml:57-61 and :272-278 (C22, "the final diagonal shift was chosen to produce exactly that equality, so gate 85 certifies internal bookkeeping, not independent agreement") and in docs/decisions/0002-anchoring-is-not-a-dispute.md:50-58. And the v10a.21r circularity is not new to this document set: it is already recorded in-repo at corpus-import/records/transcripts/Monday 531 PM.txt:2246 ("already been wired into the definition of the raw cluster function"), :2287 ("Retire v10a.21/v10a.21r as adjudicators"), :2548, :2925 ("algebraically wired to reproduce v10a.20"), :3702 ("structurally incapable of adjudicating this").

5) Category error for a ledger finding. Nothing computed disagrees with anything. This is an editorial preference about the title of an unwritten ADR in a T3 planning list, not a bug in a check, a transcription slip, or a corpus discrepancy (CLAUDE.md:75-84). Writing it into the ledger would add rule-mass of exactly the kind the finding invokes against artifact A.

Residual (too weak to state as a finding): the summary clause at A:151-152, read in isolation from its "(§5)" pointer, restates CLAUDE.md #5 and ADR 0001 ¶2 and would be a poor ADR title. That is a wording note for whoever drafts 0013, not a defect.

---

### 6.67 `vlink-decomposition-is-an-lcm` — lane `rules-compliance`

The finding's arithmetic core is correct but its two load-bearing conclusions are not, and I refuted both from primary sources.

(1) VERIFIED. lcm(1280, 83776) = 1675520 (1280 = 2^8*5; 83776 = 2^6*7*11*17; lcm = 2^8*5*7*11*17). 1280*1309 = 83776*20 = 1675520, 1309 = 7*11*17. V1 = (e4(C) - w4)/2 = (-54321/837760 + 327/83776)/2 = -39/1280 (independently confirmed at `15 hour RUN.txt:7793`, "v10a.7 one-face vacuum e4=-39/1280"). Over 1675520 the numerators are -51051 and -6540, gcd = 3; 1474623 = 3^2*163847. So the string printed at artifact B:194 and artifact A:61 is, on its face, only "1675520 is a common multiple of den(V1) and den(w4)" and never touches the numerator. That much of the finding is real.

(2) REFUTED — "supported only by v10a.21r; the document's own trap appears inside its own evidence chain." Wrong. The face-count decomposition comes from v10a.7, the SAME engine artifact B cites two lines earlier at B:105-106. `corpus-import/records/transcripts/15 hour RUN.txt:7811-7815` prints: "one-face embeddings: 13"; "adjacent-pair embeddings: {'perpendicular': 80, 'coplanar': 44} total= 124"; "[PASS] v10a.7 one-face vacuum embedding count is 13"; "[PASS] v10a.7 linked vacuum O4 subtraction=-1474623/1675520". The engine source carries the same gate at `corpus-import/programs/hodge_o4_adjudication/src/ENGINE_O4_hodge_v10a7_marked_linked_scalar.py:5465-5466`. I recomputed in Fraction: 13*(-39/1280) + 124*(-327/83776) = -1474623/1675520 exactly. The census is independently recorded at `theory/superseded/MASTER_THEORY.md:568` ("embeddings 13 (one-face) + 124 (pairs: 80 perp, 44 coplanar)"). Moreover B:145-146 quotes the maintainer explicitly retaining v10a.21r as "useful as internal consistency checks of support bookkeeping" — vacuum bookkeeping is precisely that; the retraction at B:122-153 is scoped to the F07 size-2 AXIAL weight whose incidence transform is wired to M4_EXACT. So kind="circularity" is misassigned and the "trap inside its own evidence chain" charge fails.

(3) REFUTED — "one witness (a,b)=(13,124) among infinitely many" and the 1/3-density severity argument. Face-embedding counts are non-negative integers, and (13,124) is the UNIQUE non-negative solution of 51051a + 6540b = 1474623 (general solution a = 13 + 2180k, b = 124 - 17017k; only k=0 keeps both non-negative). Enumerating representable values: 3384 of the 491542 multiples of 3 up to 1474623 are expressible as 51051a + 6540b with a,b >= 0 — 0.688%, a criterion 145x sharper than "numerator is a multiple of 3." So the underlying claim is not near-vacuous; the auditor tested a strawman (a,b in Z) instead of the physically admissible (a,b in Z_>=0), and the actual counts are supplied by the corpus.

(4) UNVERIFIABLE. `f07_twoface_adjudication_check.py` is not in any of the five artifacts nor in the certificate zip (grep over both upload dir and .../scratchpad/cert returns only A and B, which merely name it). B:190 labels its table "The runnable check (summary)", so what check 4 actually asserts in code cannot be read here — and A:27/A:147/A:163 say the script has EIGHT checks while B's table lists six. The finding infers the check's content from an abbreviated summary row.

Net: what survives is a low-severity presentation defect (the printed T1 evidence understates the real, sharp identity), not a high-severity circularity finding. Writing it into the ledger as stated would record a false provenance claim about v10a.21r.

---

### 6.68 `what-to-land-omits-the-one-real-upgrade` — lane `rules-compliance`

REFUTED on all three limbs; the arithmetic is right but the diagnosis, the independence claim, and the reading of artifact A are all wrong.

ARITHMETIC I REPRODUCED (not in dispute). Using only constants already in the repo — QUARANTINED_SCALAR (src/workhouse/constants.py:427) + LINKED_VACUUM_4 (constants.py:430) — the exact raw folded axial value is -86634244910174898583/7250590288602460800 = -11.948578179401376786. Against RAW_FOLDED_AXIAL_GAMMA_NUM = -11.9485781794007 (constants.py:428) the gap is 6.7679195581e-13 = 381 ulps by math.ulp (ulp = 1.7764e-15 at this magnitude), relative 5.664e-14. The finding needed no external ledger at all: the evidence line's "re-derived here from the shipped 69,800-record ledger" is superfluous. (The orchestrator's "~255 ulps" is also wrong; the repo's own 2^-53*|x| convention used in the C20 check gives 510, math.ulp gives 381.)

LIMB 1 IS NOT A REPO DEFECT, AND IS ALREADY ON THE RECORD. (a) The repo constant is a faithful, correctly _NUM-suffixed transcription of RUN15's printed float rest_direct, not a botched copy of an exact value: corpus-import/records/transcripts/Monday 531 PM.txt:5077 ("Folded axial rest_direct  -11.9485781794007  Intermediate level coefficient, before linked subtraction"), :6509, :6620, :6700, and 15 hour RUN.txt:9112. The run's own higher-precision prints are -11.948578179400714 and -11.948578179400696 (Monday 531 PM.txt:6527-6528), which round to exactly the digits the repo records. No transcription slip, nothing stale. (b) DECISIVE: the corpus itself already states and explains the gap. Monday 531 PM.txt:6722-6726 computes -11.9485781794007 - (-0.880098715622610) = -11.0684794637781 "which agrees with the modern candidate to roughly 7x10^-13, consistent with the numerical residuals." The discrepancy the finding proposes to land as new is printed, quantified, and attributed to float accumulation in the primary source. Under CLAUDE.md's failure triage that is "a bug in the framing", not "a real discrepancy in the corpus". (c) STRUCTURAL DISANALOGY to the cases invoked: C20 is a finding precisely because the corpus CLAIMED agreement "to float precision" and the repo showed 31 ulps (invariants.py:404-419). Here nothing anywhere claims exactness — the corpus claims ~7e-13 and gets 6.77e-13 — so there is no false claim to refute. (d) The finding misstates the repo: it says the Hamer 5.2e-13 gap and C20 are things "the repo already asserts as FINDINGs". Neither carries the FINDING: prefix. The Hamer check (invariants.py:388-394) is a PASSING tolerance check (|diff| < HAMER_TOLERANCE), not a finding at all; the 20 FINDING-prefixed checks are a distinct set (invariants.py:265, 318, 632, 654, 666, 796, 1519, 1878, 1904, 2480, 2503, 2644, 2671, 2695, 2732, ...). (e) "No invariant references the name" is true but not distinguishing: 12 other module-level UPPER constants are equally unreferenced by invariants.py (DELTA_BETA_3, DELTA_Q_3, D_PLUS_2, HAMER_MT_NUM, MUNSTER_TM_F/G/H8, SIGMA_5_CRT_PRIMES, SIGMA_5_TOPOLOGIES, T_PLUS_2, ...). T3 is CLAUDE.md's stated default for everything.

LIMB 2 REFUTED OUTRIGHT. The certificate does not independently corroborate LINKED_VACUUM_4; it hardcodes it. cert/independent_replay_modular_crt.py:27 reads `LINKED_VACUUM = Fraction(-1_474_623, 1_675_520)` as a module-level literal alongside D11 and FOLD, consumed once at :167 (`full = direct + FOLD - LINKED_VACUUM`). The modular/CRT contraction produces only D_EXACT; cert/AUDIT_REPORT.md:22-26 calls F and V_linked "separately reproduced" but ships no derivation of either. That is textbook AGENTS.md "repetition is not independence" — the same rational reused, not a distinct originating computation. So "the one place an outside computation independently corroborates a registered constant" is false. And "landable immediately and not mentioned" is false too: LINKED_VACUUM_4 is already exercised at invariants.py:405-406 inside the C20 check.

LIMB 3 REFUTED. Artifact A does not "drop" the QUARANTINED_SCALAR metadata question. A:137-139 addresses it explicitly and deliberately: "The M4_SHORTCUT relabel (rejected-by-both -> 'exact F07-branch; physical audit-pending') is a maintainer call (non-negotiable #2...)". Keeping it off the land list at A:146-154 is an escalation, not an omission — and CLAUDE.md non-negotiable #2 makes an auditor-initiated relabel of a quarantined value exactly the move the repo forbids. (The cited repo state is real: constants.py:649-656 registers "quarantined scalar" as falsified / record-backed / "rejected by both sides", mirrored at ledger/contradictions.yaml:36-40; D:184-201 does recommend the amendment. That makes it a maintainer decision, not a finding.)

HEADLINE OVERSTATED ON ITS OWN TERMS. "A §6 omits the one real upgrade" fails because A §6 item 2 (A:147-148) is precisely a new invariants.py suite of 8 machine-verified checks plus two OPEN discriminators — a T3->T1/T2 move satisfying the AGENTS.md sentence the finding quotes. The only literally true part is the narrow one: none of the five items at A:146-154 touches src/workhouse/constants.py. That is not a defect.

WHAT SURVIVES, AND WHY IT IS BELOW LEDGER THRESHOLD. One true, unasserted, in-repo-checkable relation remains: QUARANTINED_SCALAR + LINKED_VACUUM_4 = -11.948578179401377 vs RAW_FOLDED_AXIAL_GAMMA_NUM = -11.9485781794007, gap 6.7679e-13 = 381 ulps, derivable from constants.py:427/428/430 with no external input. It could at most be registered as a tier-2 documentation check recording the run's known float-accumulation residual. It must NOT be written as a FINDING: it asserts no discrepancy the corpus has not already printed and explained (Monday 531 PM.txt:6726), and filing it would manufacture a contradiction where the primary source already states agreement within its own stated residual. I therefore leave corrected_statement empty rather than hand the ledger a demoted version to land.

---

## 7. Claims checked and confirmed correct (185)

Every line here was opened at the cited location or recomputed exactly, and found to
support the document's claim. This is the bulk of the upload, and it is the reason the
findings above are worth acting on rather than discarding the set.

### 7.1 `citations-AB` (26)

- ENGINE_O4_hodge_rootonly_firewall_v1.py:41-42 (A:165, B:78, B:227) — both vectors verbatim: :41 EXPECTED_VACUUM = (0,0,-3/4,-9/32,-39/1280), :42 EXPECTED_AXIAL = (8/3,1,-1/4,-1/16,-13/896). B lists them axial-first while the file is vacuum-first, but the cited range covers both. Not a stub: :218-229 derives them by exact Fraction SU(3) character-basis arithmetic and gates them.
- DATA_O4_OrderSchedule_Occurrence_Preflight_CPU.py:615 (B:80, B:228) — verbatim: `gates.require("exact one-face O4 coefficient is -13/896", exact["full"][4] == Fraction(-13, 896), str(exact["full"][4]))`. B renders the call as `gate(...)` rather than `gates.require(...)`; the message string and the Fraction are exact.
- DATA_O4_OrderSchedule_Occurrence_Preflight_CPU.py:610,614,616 (A:166, A:59) — all three verbatim and on-point: :610 "W22 first enters a closed walk at order five"; :614 "exact one-face coefficients agree with and without W22 through O4" (exact["o4_equal"]); :616 "exact one-face W22 sensitivity first appears at O5" with `exact["o5_difference"] == Fraction(-5, 7168)`. A's use of the dict key names `o4_equal` and `o5_difference` (A:98-99) is also accurate.
- Monday 531 PM.txt:5193-5202 (A:167, B:104, B:229) — exactly the two-face vacuum block. :5193 coplanar and :5198 perpendicular both print e4(C) ~ -54321/837760 and omega4 ~ -327/83776; :5196/:5197 and :5201/:5202 are the four PASS gates. The explicit "coplanar/perpendicular … agree" gate is one line past the range at :5203.
- ENGINE_O4_hodge_v10a7_marked_linked_scalar.py:5438-5444 (B:106, B:230) — exactly the disconnected-spectator block, in a 5748-line file: :5438-5439 the comment "a two-face vacuum cluster with no shared link must factorize, so its irreducible pair weight is identically zero", :5444 the gate. Precise citation.
- ENGINE_O4_hodge_v10a21r_adjudicator_only_same_kernel.py:42-43 (B:134, B:231) — :43 `M4_EXACT = _V21R_F(-160506019419340168451, 14501180577204921600)` verbatim, matching B's displayed rational digit for digit; :42 D_EXACT.
- ENGINE_O4_hodge_v10a21r…py:313,358 (B:82) — :313 `W2X,R2X,'v10a.21 D',skip_11=True,analytic_11=_XQ(-13,896)`; :358 `V1=_XQ(-39,1280)`. B pairs the two line numbers in the reverse order of the two values it names, but both are exact.
- The three gate strings B §4 quotes from v10a.21r are verbatim and all inside the cited 300-470 range: :383 'v10a.21 minimal marked-history ledger sums to exact v10a.20 m4' (M4_FROM_MIN==M4_EXACT), :447 'v10a.21 full rooted recursive linked sum equals exact v10a.20 m4' (M4_MOBIUS==M4_EXACT), :441 'v10a.21 recursive incidence transform exactly recovers minimal-support weights' (max_resid==0). B's characterization of the engine as gated to sum back to the F07 total is supported by its own source.
- B §3's parenthetical "exact sum gated: v10a.21r V_MIN == −1474623/1675520" — v10a21r:369-371 gates exactly that.
- 15 hour RUN.txt:10620-10626 (A:168, B:54, B:232) — the header "[16] ROOTED INCIDENCE TRANSFORM — INDEPENDENT RAW CLUSTERS" is at :10619 and the six size rows plus TOTAL occupy :10620-10626 as cited. All six c4 values B §2 reproduces are exact transcriptions: +0.0159598214286, -0.403971702978, -0.178800648136, -1.3933298959e-14, -2.85049761573e-14, -0.208333333333, TOTAL -0.7751458630189173. B honestly marks sizes 4-5 as "numerical zero" rather than printing them as 0.
- The two per-line pointers into that table are right: blind size-1 at :10620 (A:58, B:192) and blind size-2 c4 = -0.403971702978 at :10621 (A:104, B:161).
- Monday 531 PM.txt:1978 (A:118, A:169, B:142) — "Stop. Do not run v10a.21r." verbatim, first line of the reply.
- Monday 531 PM.txt:2287 (A:118, A:169, B:145-146) — "Retire v10a.21/v10a.21r as adjudicators. They are still useful as internal consistency checks of support bookkeeping, but they cannot distinguish m" verbatim; B's trailing ellipsis correctly marks where the transcript breaks the subscript across :2288-2293.
- Monday 531 PM.txt:3702 (A:118, A:169, B:144) — "v10a.21 is structurally incapable of adjudicating this" verbatim.
- Monday 531 PM.txt:2548 (B:147) — "v10a.21 DELTA_MIN / RAW : NOT USED — the circular construction I identified is gone." verbatim; B's ellipsis replaces "I identified". (Context: it sits inside a quotation of the v10a.22 header, :2546-2549.)
- Monday 531 PM.txt:2925 (B:143) — "…its incidence test was algebraically wired to reproduce v10a.20…" verbatim.
- ledger/contradictions.yaml:36-40 (B:207) — exactly the "quarantined shortcut" entry, value -160506019419340168451/14501180577204921600, decimal -11.068479463778765, `status: rejected-by-both` on :40.
- src/workhouse/constants.py:426-435 and :649-655 (B:208) — :426-427 the comment "Rejected by both sides; recorded so it is never silently resurrected" + QUARANTINED_SCALAR; :430 LINKED_VACUUM_4 = Rational(-1474623, 1675520); :435 RUN15_APPLIED_SHIFT_NUM = 11.17343231638178 (B:42-43's "= RUN15_APPLIED_SHIFT"); :649-656 the Constant entry with status "falsified" on :652. Both ranges support what B says they support.
- B §7's ledger statements: C22 (Gate-85) is `status: resolved` at ledger/contradictions.yaml:272-278, and ADR 0002 exists as docs/decisions/0002-anchoring-is-not-a-dispute.md. "C22 unchanged and correctly resolved; C1's q_band vs m_Γ resolution stands" is accurate.
- The v10a.24c fit parameters B describes are real in that engine: ENGINE_O4_hodge_v10a24c_rootedfullt1_dualcoldoracle_a100.py:6793 DEG default '6', :6794 N default '13', used by `_v23c_fit_cluster` at :6934-6946 — i.e. the pointer B:170 gives is correct about the file it names (the attribution to the 15-hour run's numbers is the problem, logged separately).
- Exact arithmetic, re-derived in Fraction: e4(C) − 2·V1 = -54321/837760 + 78/1280 == -327/83776 exactly; -13/896 + 39/1280 == 143/8960 exactly; 1675520 = 1280·1309 = 83776·20 with 1309 = 7·11·17 and 8960 = 2^8·5·7 (A §2 row 1's factorization is right, unlike B §3's for 83776).
- B §3's face decomposition "V_link = V1·(single embeddings) + VPAIR·(pairs)" is exactly true and I verified it with the corpus's own embedding counts, which B does not print: 13·(-39/1280) + 124·(-327/83776) == -1474623/1675520 exactly. Counts from Monday 531 PM.txt:5208 ("one-face embeddings: 13"), :5209 ("adjacent-pair embeddings: {'perpendicular': 80, 'coplanar': 44} total= 124"), gate at :5210.
- B:40's float is correct and better than the corpus's own: float(1474623/1675520) = 0.8800987156226127, which rounds to B's printed 0.880098715622613. The transcript's print at Monday 531 PM.txt:5211-5212 (-0.8800987156226097) is the one that is ~3e-15 off, and :5211 also prints a spurious rational recognition "-521965902/593076541" — already recorded in the repo as C20 at src/workhouse/constants.py:431-432.
- |M4_ORACLE − M4_SHORTCUT| = 10.293333600759848 (A:42, B:41) is printed verbatim at 15 hour RUN.txt:10633, alongside the exact rational for the shortcut.
- B's "| QBOUND" divisibility claim for 83776 holds: 7250590288602460800 % 83776 == 0 and 14501180577204921600 % 83776 == 0, and audit 07-denominator-lift.md:38 defines D_EXACT = TOTAL_NUM/QBOUND, so the reduced denominator divides QBOUND.
- B §5 item 5's numbers are corpus vocabulary, not invented: the "3,895 Stage-3H records" appear at corpus-import/records/transcripts/819gptultralocal.txt:78,124, ## Assessment.txt:517,609 and DATA_O4_OrderSchedule_Occurrence_Preflight_CPU.py:649 ("complete 3895-topology corpus"); the "189-record" kernel is gated in the run at 15 hour RUN.txt:10638 and :10650.

### 7.2 `citations-CD` (27)

- C §6 SHA-256 for ENGINE_O4_hodge_v10a7_marked_linked_scalar.py: asserted dc9ddfaab437ad4478c85eb631ed0319699c3e3304bd83b22bd31fc2f1f1107d. Computed sha256sum here = identical, AND independently pinned at corpus-import/SHA256SUMS:369. Verified twice.
- C §6 all nine v10a7 line ranges are accurate: :4548-4596 (W=-M — `_v10a3_apply_W` at :4579, docstring "Connected magnetic action W=-M", the -1.0 at :4592); :4599-4614 (normalized charge-odd source, `_v10a3_face_state` returning {st:s},{stc:-s} with s=1/sqrt(2)); :4652-4679 (`_v10a3_reduced_resolvent`, exact function bounds); :5483-5508 (`_v17_apply_W_labeled` 5483-5499, `_v17_R_labeled` 5502-5508); :5574-5589 (S0->W1L->R1L->W2L->R2L literally at 5580-5584); :5602-5624 (D=<W2|R2> at 5614, D_A at 5624); :5646-5653 (FOLD_A=-E2_A*N_A+J_A at 5649, gate vs 5315003/140454 at 5653); :5687-5707 (M4_CAND=E4_A-V4_LINKED_MARKED at 5702, "m4_rest candidate (blind)" at 5706); :5720-5747 (SystemExit on gate failure at 5731-5732, optional unblind at 5742-5744).
- C §6 quote "The source explicitly says no historical fourth-order mass is supplied at lines 5181-5182 and again at line 5707": verbatim. :5181 = "# NO historical m4 value is supplied anywhere in the construction."; :5182 = "# The final m4_rest is printed only after all hard gates pass."; :5707 = "print('  NOTE: no historical fourth-order mass value was loaded or used.')".
- C §1 v10a24c citations all exact: :7309 M4_ORACLE=float(totals[4]); :7310 M4_SHORTCUT=_V23CF(-160506019419340168451,14501180577204921600); :7314-7320 the oracle-vs-shortcut comparison and prints; :7322-7326 ax_rest and local_shift (both on :7324) plus the diagonal add; :7325-7326 adds local_shift to exactly THREE anchor diagonals (anchor_faces built per T1_POLS at :6406, indexed range(3) at :6700); :7335-7336 gates the shifted rest against M4_ORACLE (not the shortcut).
- C §1 constants.py:203-214 — M_GAMMA_4_NUM = -0.7751458630189173 at :207, inside the range, with the docstring C paraphrases.
- C §1 constants.py:426-435 — QUARANTINED_SCALAR at :427, RAW_FOLDED_AXIAL_GAMMA_NUM at :428, RUN15_APPLIED_SHIFT_NUM = 11.17343231638178 at :435. All three inside the range.
- C §1 ADR 0002:50-57 — exactly the passage C describes: item 4 keeps apart "the oracle value is an independent blind reconstruction ... substantive" from "the final assembled rest value is forced to equal that oracle by local_shift = M4_ORACLE - ax_rest — true by construction".
- C §7 audit citation 07-denominator-lift.md:69-78 — supports C's claim exactly: :74 "Conditional exactness. The final `D_EXACT` is exact relative to a recovered rational history ledger ... inferred with `limit_denominator()`"; :78 "No immutable artifact. The 117,161-topology ledger ... are not saved or checksummed"; :73 "No saved execution."
- C §3's three pinned provenance documents all resolve to in-repo files with matching hashes, computed here: 68782826... = corpus-import/programs/hodge_o4_adjudication/src/DATA_O4_OrderSchedule_Occurrence_Preflight_CPU.py (SHA256SUMS:358); 47c6ccc1... = corpus-import/programs/hodge_o4_adjudication/notebooks/NB_O4_hodge_v10a20b_denominatorlift_exact_da_m4_a100.ipynb (SHA256SUMS:331); 7332bf83... = corpus-import/records/audits/07-denominator-lift.md (SHA256SUMS:766). C's labels for all three are apt.
- C §4 census citations into the v10a.20b notebook are exact. The notebook has 2 cells; cell index 1 is the code cell with 6737 source lines, so C's "notebook cell index 1; described as 'cell 2' in the corpus audit" is right. Source lines 6343-6346 gate matches==5400, len(tasks)==3597, raw_upper==9814138, skipped11==54; lines 6370-6371 gate pair_occ==1829147 and len(pairw)==117161. All inside C's cited 6315-6346 and 6348-6371.
- C §7 all eight v10a.20b source ranges verified: 4373-4391 (exact SU(3) energy/fusion, `_v10a2_energy_dyn`/`_v10a2_fuse`); 4595-4615 (`_v10a3_project_action_dyn`); 4638-4653 (`_v10a3_face_state`/`_v10a3_face_pvec`); 6041-6080 (support-resolved recursion section header + `_v17_add_state`/`_v17_aggregate`); 6245-6310 (`_x_phys_blocks` at 6245, W2X exactified at 6305, R2X=_x_derive_R2(W2X) at 6307, gate at 6309); 6382-6433 (_LOCAL_Q at 6382, `_x_haar_den_bound` at 6390, QBOUND at 6425-6433); 6668-6672 (D_EXACT=_XQ(TOTAL_NUM,QBOUND) at 6668 plus its two gates).
- C §7's central dataflow claim is exact and is the strongest verified point in either document: the prior target appears strictly AFTER the exact accumulation. Notebook :6668 builds D_EXACT; :6674 comment "# The previous v10a.16 result is used only after the exact integer accumulation."; :6675 D_PREV=-49.7901704444838; :6680-6682 FOLD_EX=5315003/140454, VLINK_EX=-1474623/1675520, M4_EXACT=D_EXACT+FOLD_EX-VLINK_EX; :6683 M4_PREV=-11.068479463777946 only then.
- C §5 arithmetic verified exactly in Fractions: D_EXACT = -361008126292641364183/7250590288602460800 (and this value is independently confirmed by the delivered certificate's summary key /D_EXACT) plus 5315003/140454 minus -1474623/1675520 == -160506019419340168451/14501180577204921600 exactly, float = -11.068479463778765 exactly as C and D print.
- D: all four '15 hour RUN.txt' citations land correctly. :10619-10640 contains -0.7751458630189173 (at :10626 TOTAL and :10632); :10619-10626 contains `size 1: ... c4=+0.0159598214286` (at :10620); :10620-10622 contains `size 2: ... c4=-0.403971702978` (at :10621); :10743-10750 contains "finite-cluster shape classes: 33  concrete clusters: 203" (at :10747).
- D §2 v10a24c:6767-6777 supports its claim verbatim: "This second leg does NOT use any of the operator-moment ledgers above ... The W1/W2 histories are used only as a SUPPORT census. Each raw finite-cluster coefficient is recomputed by diagonalizing H_C(u)=H0+uV_C on that restricted cluster, constructing the Hermitian des-Cloizeaux one-particle block, subtracting an independently diagonalized vacuum level, and only then performing rooted incidence subtraction." (Caveat: this is a source comment, not a verified behavior.)
- D §2 v10a24c:6848-6889 correct — `_v23c_build_basis` at :6848, P seeds layer 0 at :6867-6875, layer1 = W(P) named 'W(P{j})' at :6877-6882, layer2 = W(Q1) named 'W(Q1{jj})' at :6883-6888.
- D §2 v10a24c:6894-6899 correct — the dense W loop applies W to EVERY basis column j and projects onto every index i sharing the H0 key, with no layer mask, so Q2<->Q2 entries are populated. Same loop is unchanged in v10a.26 ('15 hour RUN.txt':7094-7098).
- D §3 all four v10a24c claims exact: :6928-6932 forms the raw cluster gap as Heff[root_i,same] minus the independently computed vacuum energy Ev; :7105-7128 `_v24c_shape_key` docstring states the root is a separate key field preventing the old unrooted-cache collision; :7223-7255 builds CLUST from all rooted connected subsets and gates 'independent cluster poset is downward closed'; :7283-7289 subtracts every proper rooted connected subcluster from the already-formed raw gap.
- D §2 "degree-six fit on 13 points" is exactly right about the v10a24c source: V23C_FIT_DEG default '6' at :6793, V23C_FIT_N default '13' at :6794.
- D §2 audit 03-unified-proposal.md:17-27,134-143,153-161 — every element D lists is present: explicit physical P/Q1/Q2 at :20; typed key "(canonical joint irrep, exact H0 energy, canonical center flux)" verbatim at :21; no-W22 order schedule at :22, :139, :158; canonical Hermitian SW/BCH at :23; B B^T=K at :138 and B12 at :139; 3,895 records incl. the 2,417 formerly missing folded cases at :160; unshifted 189-record kernel at :161.
- D §4 program README:27-45 — 609 at :31 ("All 203 x 3 = 609 exact marked-cluster evaluations"), 3,895 Stage-3H at :35, "has produced zero physics contractions" at :45. All inside the cited range.
- D §4 audit 02-duplication-report.md:41-49 — the substantive row is :49 ("Corpus identities conflated | F07 has 117,161 Haar-pair topologies; F08 has rooted supports; F09 has rooted cluster classes and 189 records; canonical Gate 3 requires a different 3,895-topology corpus"), inside the cited range. Range is over-broad but contains the target.
- D §5 audit 05-latest-run-forensics.md:60 — exactly the sentence D describes: "The normalization bridge remains an assumption. The Hamer comparison asserts `H=W/2, u=x/2`; the project-wide audit still lists the canonical magnetic-normalization derivation as open. A numerical match under an unproved conversion cannot close that gate."
- D §8 all four ledger/contradictions.yaml ranges exact: :8-25 = C1 id/title/status/section/resolution/terminology (the differently-anchored-coordinates resolution); :36-40 = the third quantity, label 'quarantined shortcut', decimal -11.068479463778765, status: rejected-by-both; :49-54 = the external_validation block calling the blind value substantive; :272-278 = C22 in full.
- D §8 constants.py:426-435,649-655 — the 'falsified' status and 'rejected by both sides' reason are at :652 and :655 in the Constant("quarantined scalar", ...) entry; the 'Rejected by both sides' comment is at :426. Both cited ranges together cover what D says.
- D §2 order trace claim P -> Q1 -> Q2 -> Q1 -> P and 'W22 adds a fifth magnetic step' is corroborated three independent ways in-repo: audit 06:68-74; the inherited engine comment 'No W22 is built. It first enters one order later.' at '15 hour RUN.txt':4508; and the executed exact regression (o5_difference = -5/7168) in DATA_O4_OrderSchedule_Occurrence_Preflight_CPU.py.
- theory/SHA256SUMS pins NONE of the files cited by C or D — it has 13 entries, all under theory/ (MASTER_THEORY_UNIFIED v4_3, GLUEBALL docs, governance/, superseded/). corpus-import/SHA256SUMS DOES pin every in-repo file C and D cite: v10a7 engine :369, v10a24c engine :363 (935a3a5b..., recomputed and matching), program README :325, audits 02/03/05/06/07 at :756/:759/:763/:764/:766, '15 hour RUN.txt' :874 (a81bfe0f..., recomputed and matching).

### 7.3 `arithmetic` (46)

- A §2 / B §6.1 / B §2 / D §1 — one-face gap: -13/896 + 39/1280 = 143/8960 exactly (sympy/Fraction). 143 = 11·13; 8960 = 2^8·5·7. Both A's and B's factorizations correct.
- D §1 — 143/8960 = 0.015959821428571… : correctly rounded (exact 0.01595982142857142857…).
- B §2 — inputs EXPECTED_AXIAL = (8/3, 1, -1/4, -1/16, -13/896) and EXPECTED_VACUUM = (0, 0, -3/4, -9/32, -39/1280) are verbatim at ENGINE_O4_hodge_rootonly_firewall_v1.py:42 and :41 respectively (B cites 41-42; range correct, order swapped in prose). Bonus: line 43 carries EXPECTED_GAP = (…, 143/8960) directly.
- B §2 — "exact one-face O4 coefficient is -13/896" gate is at DATA_O4_OrderSchedule_Occurrence_Preflight_CPU.py:615 exactly as cited.
- A §2 / A appendix — W22 one-face facts: :610 "W22 first enters a closed walk at order five", :614 "exact one-face coefficients agree with and without W22 through O4" (o4_equal), :616 o5_difference == Fraction(-5,7168). A's 'first bite O5 = -5/7168' is verbatim correct; 7168 = 2^10·7.
- B §2 — V1 = -39/1280 at ENGINE_O4_hodge_v10a21r…py:358 and analytic_11 = -13/896 at :313, exactly as cited (":313,358").
- A §2 / B §3 / B §6.3 — e4(C) = -54321/837760 and omega4 = -327/83776 with coplanar == perpendicular: both printed and gated at Monday 531 PM.txt:5193-5202, exactly the cited range. Recomputed: -54321/837760 - 2·(-39/1280) = -327/83776 exactly.
- Orchestrator cross-check confirmed independently: e4(C) - 2·V1 = -327/83776 exactly, and 83776 = 2^6·7·11·17 (NOT the 2^7·7·11·17^2 = 2848384 that B §3 prints).
- A §2 / B §3 / B §6.4 — V_link = -1474623/1675520; 1675520 = 1280·1309 = 83776·20, both True. 1280 = 2^8·5, 1309 = 7·11·17, 83776 = 2^6·7·11·17, 1675520 = 2^8·5·7·11·17. Also 837760 = 10·83776 and 1675520 = 2·837760.
- B §3 — "V_link = V1·(single embeddings) + VPAIR·(pairs)" is exactly realizable and unique for counts < 400: 13·(-39/1280) + 124·(-327/83776) = -1474623/1675520 exactly. This is literally the construction at ENGINE_O4_hodge_v10a21r…py:361-371, whose gate `_v21_sum(V_MIN)==_XQ(-1474623,1675520)` is an exact Fraction equality (T1 within that engine).
- B §4 / C §1 / D — M4_EXACT = M4_SHORTCUT = -160506019419340168451/14501180577204921600, present verbatim at ENGINE_O4_hodge_v10a21r…py:43 (B cites :42-43) and at ENGINE_O4_hodge_v10a24c…py:7310 (C cites :7310). Matches constants.QUARANTINED_SCALAR exactly.
- C §5 / D executive / referee — D_EXACT = -361008126292641364183/7250590288602460800; FOLD_EXACT = 5315003/140454; LINKED_VACUUM_EXACT = -1474623/1675520; D_EXACT + FOLD - VLINK = -160506019419340168451/14501180577204921600 exactly. Independently re-derived in Fraction.
- C §5 / D — "≈ -11.068479463778765": the exact value is -11.06847946377876471634502…, whose correctly rounded 15-dp form is exactly -11.068479463778765, and float(exact) reprs identically. 0 ulps.
- B §1 — M4_SHORTCUT printed as -11.0684794637788: correctly rounded 13-dp of the exact value (20 ulps from the double, which is the expected print rounding). ax_rest printed as -11.9485781794014: correctly rounded 13-dp of the exact D_EXACT+FOLD (13 ulps).
- B §1 — "M4_SHORTCUT − ax_rest = +0.880098715622613 = −V_link": exactly -V_link = 1474623/1675520 = 0.880098715622612681436211…; the printed 15-dp form is the correctly rounded one (3 ulps from the double). Sign convention consistent throughout A/B/C.
- A §1 / B §1 — |M4_ORACLE − M4_SHORTCUT| = 10.293333600759848: reproduces to 0 ulps from M_GAMMA_4_NUM and float(QUARANTINED_SCALAR), and matches the transcript's own printed |Δ| at 15 hour RUN.txt:10633 verbatim.
- A §1 / B §1 — local_shift = M4_ORACLE − ax_rest = +11.1734: correct to the 4 dp quoted (exact-ax path gives 11.173432316382460, run path 11.173432316381783; both round to 11.1734). Identity M4_ORACLE − M4_SHORTCUT ≡ local_shift + V_link verified exactly.
- A §1 — the 4-dp values -11.9486, -11.0685, -0.7751 are all correctly rounded.
- C §9 — "approximately -0.775145863, not -11.068479464": both 9-dp roundings are correct (-11.0684794637787… → -11.068479464).
- C §1 — every v10a.24c line citation is exact: M4_ORACLE=float(totals[4]) at :7309; M4_SHORTCUT rational at :7310; the oracle-vs-shortcut comparison at :7314-7320; ax_rest / local_shift at :7324 (in the cited 7322-7326); the shift added to the anchor diagonals at :7325-7326; the gate against M4_ORACLE at :7335-7336.
- C §1 — M_GAMMA_4_NUM = -0.7751458630189173 at constants.py:207 (cited range 203-214); QUARANTINED_SCALAR at :427, raw folded rest -11.9485781794007 at :428, applied shift 11.17343231638178 at :435 (cited range 426-435). ADR 0002 separation at docs/decisions/0002-anchoring-is-not-a-dispute.md:50-57 — exact.
- C §6 — SHA-256 of ENGINE_O4_hodge_v10a7_marked_linked_scalar.py is dc9ddfaab437ad4478c85eb631ed0319699c3e3304bd83b22bd31fc2f1f1107d, byte-for-byte the value C prints.
- C §3 provenance table — all three pinned documents verified byte-for-byte against this repo: 68782826d50ad6bcbb3a20d83649bfa7f66e42c5706d131361b7d189b1f99a8f = DATA_O4_OrderSchedule_Occurrence_Preflight_CPU.py; 47c6ccc18079c49416c511c2a27a9d757525d6e279992514ed63f5ba413530fd = NB_O4_hodge_v10a20b_denominatorlift_exact_da_m4_a100.ipynb; 7332bf8363a13a44f329fca3d96d75584bc41447032906d5a7ae371889f4daf5 = corpus-import/records/audits/07-denominator-lift.md.
- C §4 / C §7 — every v10a.20b notebook count and line number checks out against the repo copy of the notebook (cell index 1): 5,400 matched blocks (:6343), 3,597 whole-block orbits (:6344), raw upper bound 9,814,138 (:6345), 54 skipped one-face matches (:6346) — all inside C's cited 6315-6346; 1,829,147 pair occurrences (:6370) and 117,161 nonzero canonical topologies (:6371) — inside C's cited 6348-6371.
- C §7 dataflow-separation claim — verified in the repo notebook: D_EXACT is constructed at :6668 and gated at :6669-6672; the prior float target D_PREV = -49.7901704444838 appears only afterwards at :6675, under the comment 'The previous v10a.16 result is used only after the exact integer accumulation' (:6674); FOLD_EX/VLINK_EX/M4_EXACT at :6680-6682 and M4_PREV = -11.068479463777946 at :6683 — exactly C's cited 6668-6672, 6674-6678, 6680-6688. C's 'proves dataflow separation inside that cell' is correct as stated.
- Bonus corroboration of C §5: FOLD_EXACT = 5315003/140454 is not external-only — it is literally in this repo at NB_O4_hodge_v10a20b…ipynb cell 1 line 6680 (FOLD_EX=_XQ(5315003,140454)).
- Referee report — weighted Haar sum: I replayed all 69,800 ledger records in exact Fractions. Σ weighted_contribution = -805586892848311021/8092176661386675, matching the report and the summary JSON exactly. Per record: weighted_contribution == weight·haar (0 failures), haar == scaled_haar_numerator/q_product (0 failures), q_product == Π local q over the pattern list (0 failures), CRT modulus > 2·signed bound (0 failures), indices strictly 1..69800.
- Referee report — D_EXACT = -13/896 + (1/2)·Σ: recomputed from my own replayed sum, gives -361008126292641364183/7250590288602460800 exactly. Adding 5315003/140454 and +1474623/1675520 gives QUARANTINED_SCALAR exactly. Three independently recorded values (cert D_EXACT, repo LINKED_VACUUM_4, repo QUARANTINED_SCALAR) mutually pin FOLD = 5315003/140454.
- Referee report — QBOUND divisibility and integer lift: QBOUND = 62895057857493885215590055852113920000000 = 2^36·3^20·5^7·7·11·13·17^3·19·23·29·31·37·47; 7250590288602460800 | QBOUND with quotient 8674474126108262400000; D_EXACT·QBOUND = -3131555650840341423974721085483725619200000 (integer, matches the recorded lift), and lift/QBOUND == D_EXACT. Also 8092176661386675 | QBOUND, so the weighted-sum denominator is in scope too.
- A §2 capstone 'den | QBOUND' — 14501180577204921600 = 2^8·3^6·5^2·7·11·13·17^3·19·29·31·37 divides QBOUND. Also 8960, 83776, 837760, 1675520, 140454, 7168 and 4405310420659200 all divide QBOUND.
- 14501180577204921600 == 2 · 7250590288602460800 (True). The two denominators differ by exactly one factor of 2 (2^8 vs 2^7); the extra 2 is supplied by the 1/2 in D_EXACT = D11 + (1/2)Σ. The V_link denominator 1675520 = 2^8·5·7·11·17 divides 14501180577204921600 evenly, and lcm(7250590288602460800, 140454, 1675520) = 14501180577204921600 exactly — so the final denominator is forced, not chosen (140454 = 2·3^5·17^2 contributes nothing new beyond 17^2 ⊂ 17^3).
- Referee report — 44-case independent modular certificate: cert/stratified_actual_topology_modular_audit.json holds 44 results spanning exactly 22 distinct endpoint signatures, and every one matches the primary ledger on haar value, weight, scaled numerator and q_product (0 mismatches). The 20/40 figures in rank3_order4_modular_reference_crosscheck.json belong to a different artifact and are not the ones the report cites.
- Referee report — census: 69,800 records, 10,368 containing a pure-six ((0,6)/(6,0)) sector, 9,184 with zero Haar value: all three recomputed from the ledger and matching. crt_prime_count_histogram {1:1209, 2:68591} sums to 69,800 and matches my per-record count. pattern_histogram in the pickle summary matches my recount from the ledger exactly for all seven patterns (total 530,016 local slots). endpoint_signature_count 22 confirmed. 488 pure-six delta-expansion terms confirmed present in the crosscheck JSON.
- cert/SHA256SUMS.txt — hashes of the two load-bearing ledgers verified against the actual files: 1b9ed1801e1125e15c4331cb0b06fe2a6782f0638efe725640f3602001f1b469 (Haar numerator ledger) and 5337734a57bd2e1fe690c636f19bc0f65c48bac86cc029a7e4dfe87251e8ff59 (source topology pickle), both matching the referee report's 'Artifacts' section. The two copies of the summary/validation/crosscheck JSONs in the zip are byte-identical.
- C §3 — 164,662 = 82,384 + 82,278 (arithmetic correct; the counts themselves are external).
- D §4 — 203 × 3 = 609 (arithmetic correct) and both numbers, plus 3,895 Stage-3H and the 189-record kernel, appear at corpus-import/programs/hodge_o4_adjudication/README.md:31, :35, :45 (inside D's cited 27-45), together with 'zero physics contractions'. 3,895 − 2,417 = 1,478, matching audits/01-theory-authority.md:84 ('expand Stage 3H from 1,478 to all 3,895 topologies, including 2,417 folded cases').
- D §4 — the blind 203 concrete clusters / 33 rooted shape classes are at 15 hour RUN.txt:10746, inside D's cited 10743-10750.
- D §2 — the W22 structural claim is correct for the file cited: ENGINE_O4_hodge_v10a24c…py:6894-6898 applies W to every retained basis vector and projects onto every compatible row with no layer mask. The P/Q1/Q2 build and the (2,5) forensics are at audits/06-pattern-2-5-runtime-forensics.md:50-76 as cited.
- D §2/§7 — the canonical-branch requirements (explicit physical P/Q1/Q2, typed block identity, W22 never built, canonical Hermitian SW/BCH, 3,895 Stage-3H, unshifted 189-record kernel) are verbatim at audits/03-unified-proposal.md:17-27 as cited.
- D §4 — the warning that F07 / rooted-support / rooted-cluster / Stage-3H inventories are not interchangeable is at audits/02-duplication-report.md:49, inside D's cited 41-49.
- D §5 — the normalization-bridge-is-an-assumption claim is verbatim at audits/05-latest-run-forensics.md:60 as cited.
- C §7 — the F07 evidence-boundary claims (conditional exactness on a recovered history; no immutable completed artifact) are at audits/07-denominator-lift.md:74 and :78, inside C's cited 69-78.
- B §4 / A §4 — the v10a.21r retraction quotes at Monday 531 PM.txt:1978, :2287, :2548, :3702 are verbatim and correctly located.
- D §8 / B §7 — ledger citations exact: contradictions.yaml:8-25 (C1 narrow resolution), :36-40 (quarantined shortcut labelled rejected-by-both), :49-54 (Hamer external validation), :272-278 (C22 resolution). All present as described.
- 117,161 vs 117,163 is NOT a conflict (I checked, because it looks like one): the v10a.20b notebook gate at cell 1 line 6371 reads 'exact nonzero topology census removes two float-split topologies: exact=117161, float=117163, removed=2'. The historical runs' 117,163 is the float census; 117,161 is the deliberate exact reduction. Same pattern at :6344 (3597 exact / 3607 float) and :6370 (1829147 exact / 1829187 float).
- A §2 / B §2 citation line numbers into the transcript are all exact: :10619 section header [16], :10620 size 1, :10621 size 2, :10625 size 6, :10626 TOTAL, :10632 independent linked m4, :10633 the |Δ| line, :10637 the applied shift.

### 7.4 `certificate` (11)

- Sigma w_T H_T = -805586892848311021/8092176661386675 and D_EXACT = -13/896 + Sigma/2 = -361008126292641364183/7250590288602460800: verified exactly in fractions.Fraction, and reproduced end-to-end. I re-ran the shipped modular_haar_contractor.py over the shipped pickle (367 s, 69,800 records) and it regenerated rank3_order4_exact_haar_numerators.ndjson.gz BYTE-IDENTICALLY, sha256 1b9ed1801e1125e15c4331cb0b06fe2a6782f0638efe725640f3602001f1b469, matching the manifest.
- The full 69,800-class independent modular/CRT replay (independent_replay_modular_crt.py, algorithmically distinct projector and contraction engine) agrees with the primary ledger on every single record: 0 unmatched topology keys, 0 scaled-numerator mismatches, 0 Haar-rational mismatches, 0 weight mismatches. It returns the same D_exact, the same total_integer_numerator_over_qbound = -3131555650840341423974721085483725619200000, and the same zero_haar_values = 9184. The independence claim is substantively TRUE; only its artifact is missing from the package.
- The package DOES produce -11.068479463778765 — but only through independent_replay_modular_crt.py, which computes `full = direct + FOLD - LINKED_VACUUM` at line 167 with FOLD and LINKED_VACUUM as hardcoded literals at lines 26-27. The one script that runs as shipped (validate_modular_haar_ledger.py) produces D_EXACT only and never touches -11.068479. m4_rest_exact = -160506019419340168451/14501180577204921600, confirmed exactly.
- validate_modular_haar_ledger.py runs as shipped from the package root: EXIT=0 in 3.9 s, 69,800 records, all asserts pass, and its emitted certificate is content-identical to the shipped rank3_order4_exact_haar_validation.json (byte-identical after stripping CR).
- crosscheck_modular_haar_reference.py, once its two missing imports are supplied, reproduces the shipped certificate exactly: balanced_inverse_gram_exact_matches [1,2,3], pure_six_inverse_gram_exact_match true, 488 delta-expansion terms, 9,100 pure-six projector-entry comparisons (8,100 = the complete 90x90 nonzero support, plus 1,000 seeded probes), 40 actual topologies over all 20 non-pure signatures. actual_topology_results equal element-for-element; only elapsed_seconds differs.
- independent_cross_check_actual_topologies.py, likewise repaired, reproduces the shipped stratified certificate exactly: 44 topologies, 22 signature strata, all_exact_values_and_lifted_numerators_match true, and the 44-element `results` array is equal element-for-element to the shipped one. Only the `primary_ledger` path string differs.
- Every census figure the reports quote is correct against the shipped ledger, recomputed by me: 69,800 records; 10,368 containing a pure-six sector; 9,184 with zero Haar value; 22 distinct endpoint signatures of which 20 are non-pure. Ledger keys are strictly increasing and unique.
- The exactness claim holds: no float or tolerance appears in the arithmetic path. Grepping the four exact-path modules for float(/np.float/dtype=float/1e-/isclose/round finds exactly two hits, both non-arithmetic — modular_haar_contractor.py:499 (ETA display) and :535 (the D_EXACT_decimal display string). The modular engine reduces mod p after every multiply, so int64 is never stressed.
- Target-leakage scan is CLEAN. Underscore-normalized grep of every .py in the package for M4_ORACLE, ax_rest, local_shift, M4_SHORTCUT, 7751458630189173, 7751458630184, 160506019419340168451, 11068479, 11.0685, 0827701250956, 4405310420659200, 7250590288602460800 returns zero hits. The only large literals in code are QBOUND (3 files), FOLD/LINKED_VACUUM (independent_replay_modular_crt.py:26-27), D11 = -13/896 (3 files), and the count 69_800 (validate line 69). None of these is the target scalar, and none can steer the accumulated numerator. The target numerator 160506019419340168451 appears only in the three .md reports, as an output.
- The CRT recovery is nowhere near critical: over all 69,800 records the tightest |numerator|/bound is 0.0123 (an 81x margin), and the smallest CRT headroom modulus/(2*bound) is 1.29 — above the required 1.0 at every record.
- Cross-linking E to the repo: D_EXACT + FOLD = -86634244910174898583/7250590288602460800 = -11.948578179401377 exactly, versus src/workhouse/constants.py:428 RAW_FOLDED_AXIAL_GAMMA_NUM = -11.9485781794007. Absolute gap 6.767919558114954e-13, relative 5.66e-14. In ulps at that magnitude (ulp = 2^-49 = 1.7763568394002505e-15) that is 381 ulps, not the ~255 quoted in the brief — the absolute gap agrees, the ulp normalization does not. The repo constant is a faithful transcription of the corpus float (theory/superseded/MASTER_THEORY.md:416), so this is a corpus-precision issue to record, not a constant to silently edit.

### 7.5 `ledger-graph` (10)

- D's four ledger citations are all exact: contradictions.yaml:8-25 is C1's resolution plus the terminology block; :36-40 is precisely the `quarantined shortcut` quantity block D proposes to amend; :49-54 is the `external_validation` prose D asks to qualify; :272-278 is C22 in full. Verified by reading each range.
- B's and D's constants.py citations are accurate: :426-435 is the comment plus QUARANTINED_SCALAR, RAW_FOLDED_AXIAL_GAMMA_NUM, LINKED_VACUUM_4, LINKED_VACUUM_4_ARTIFACT, RUN15_APPLIED_SHIFT_NUM; :649-655 is the Constant(...) registration (closing paren at 656).
- The branch gap is exactly as printed: float(Fraction(-160506019419340168451,14501180577204921600)) = -11.068479463778765 and -0.7751458630189173 minus that = 10.293333600759848, bit-identical to A §1 line 42 and B §1 line 41.
- The v10a24c degree-6 / 13-point fit is real and cited correctly: V23C_FIT_DEG default '6' and V23C_FIT_N default '13' at corpus-import/programs/hodge_o4_adjudication/src/ENGINE_O4_hodge_v10a24c_rootedfullt1_dualcoldoracle_a100.py:6793-6794, consumed by _v23c_fit_cluster at :6934-6946, with the dense W built with no layer mask at :6894-6899 as D §2 line 81 states.
- The blind per-size table exists where cited with the quoted values: 15 hour RUN.txt:10620-10626, sizes 1-6 with c4 = +0.0159598214286, -0.403971702978, -0.178800648136, -1.39e-14, -2.85e-14, -0.208333333333, TOTAL m4 = -0.7751458630189173.
- The 203/33 inventory D §4 quotes is in the transcript: 15 hour RUN.txt:10747 "finite-cluster shape classes: 33  concrete clusters: 203", and :10750 "FINAL VERDICT : MIXED/THIRD RESULT — DO NOT PROMOTE EITHER FOURTH-ORDER CLAIM", consistent with the documents' refusal to promote either side.
- The G3 item-10 blocker the documents skip is real and already recorded: ledger/gaps.yaml:126-131, settlement/mce_adjudication_harness.py:43 and :335, src/workhouse/settlement.py:128-142.
- Both documents correctly decline to make the relabel themselves (B §7 line 208 "This document does not make that change"; A §5 lines 137-140 "a maintainer call"), correctly leave C22 alone (D §8 lines 205-209 matches contradictions.yaml:272-278), and correctly say ADR 0002's C1 resolution stands. That restraint is right and should survive into whatever lands.
- The two-face vacuum arithmetic is exact as claimed: Fraction(-54321,837760) - 2*Fraction(-39,1280) = Fraction(-327,83776); 1675520 = 1280*1309 = 83776*20; 1309 = 7*11*17; 143 = 11*13; 8960 = 2^8*5*7. Only B's prime factorization of 83776 is wrong, not the value.
- The register does have room for the NEW content in one place: G3's `audit_findings` list (ledger/gaps.yaml:113-134) is free-form and unpinned — grep of tests/ for `audit_findings` returns nothing, unlike `protocol` (pinned at 11) and `inventory_trap` (pinned present) at tests/test_ledger.py:65-69.

### 7.6 `invariants-tests` (13)

- Suite count: FRONTIER.md:23 says 'fourth order, anchoring and the residual dispute | 13/13'. Confirmed — the suite registers exactly 13 checks at src/workhouse/invariants.py:294-429 and all 13 PASS.
- Total count: `make verify` and `workhouse verify` both report '140/140 checks passed'. `workhouse verify --tier 1` reports 111/111; `--tier 2` reports 29/29; 111+29 = 140. Nothing was modified.
- invariants.py:421-429 already states that the Gate-85 equality is target-derived, in both the code comment and the detail line: comment at :423-424 'Gate 85's equality was produced by construction with this shift, so it certifies internal bookkeeping rather than independent agreement'; detail at :427-428 'applied 11.17343231638178 vs Delta_Gamma 2.082770125095642 — target-derived, so gate 85 is not an independent scalar verification'. `workhouse why C22` confirms C22 resolved and cited by exactly that check.
- The F07 value IS already asserted by an invariant: src/workhouse/invariants.py:397-400 'quarantined scalar decimal' (T2) pins float(QUARANTINED_SCALAR) to -11.068479463778765 within 1e-14, reporting '|diff| = 0.00e+00'.
- -13/896 + 39/1280 == 143/8960 exactly; 143 = 11*13, 8960 = 2^8*5*7 (sympy.factorint). Confirmed.
- e4(C) - 2*V1 = -54321/837760 - 2*(-39/1280) = -327/83776 exactly. Confirmed. 83776 factors as 2^6*7*11*17 (not B §3's 2^7*7*11*17^2 = 2848384).
- 1675520 = 1280*1309 = 83776*20; 1309 = 7*11*17; 1675520 = 2^8*5*7*11*17. Confirmed.
- B §3's transcript citation resolves: corpus-import/records/transcripts/Monday 531 PM.txt:5193-5202 shows coplanar and perpendicular PASS gates both giving e4=-54321/837760 and omega4=-327/83776.
- B §2's blind per-size table transcribes corpus-import/records/transcripts/15 hour RUN.txt:10620-10626 faithfully, and the line numbers cited (:10620 size 1, :10621 size 2, :10626 TOTAL) are exact.
- B §2's one-face citations resolve exactly: EXPECTED_AXIAL/EXPECTED_VACUUM at corpus-import/programs/hodge_o4_adjudication/src/ENGINE_O4_hodge_rootonly_firewall_v1.py:41-42, and the -13/896 gate at .../DATA_O4_OrderSchedule_Occurrence_Preflight_CPU.py:615. A's W22 citations (:610, :614, :616) also resolve: :610 'W22 first enters a closed walk at order five', :614 'exact one-face coefficients agree with and without W22 through O4', :616 'exact one-face W22 sensitivity first appears at O5' == Fraction(-5,7168).
- 143/8960 is not a new number to the corpus: ENGINE_O4_hodge_rootonly_firewall_v1.py:43 already carries it as a named constant, EXPECTED_GAP = (Q(8,3), Q(1), Q(1,2), Q(7,32), Q(143,8960)).
- M_GAMMA_4_NUM - float(QUARANTINED_SCALAR) == 10.293333600759848 bit-for-bit, matching the artifacts' printed gap.
- `workhouse why C1` confirms C1 is resolved (an anchoring distinction, ADR 0002), and `workhouse why C2` confirms C2 is the one genuinely open contradiction with both sides recorded and neither promoted — consistent with what A §3 and B §7 say.

### 7.7 `hamer-circularity` (9)

- 8 * HAMER_A4_NUM = -0.7751458630184 exactly (hex bfe8cdfeb2696630), and |8*a_4 - M_GAMMA_4_NUM| = 5.172529071728604e-13 < HAMER_TOLERANCE = 5.3e-13. Both live checks (invariants.py:388 and :1279) run and PASS; I reproduced the arithmetic in Fraction and in raw bit patterns.
- HAMER_A4_NUM == HAMER_MA_NUM[2] as constants.py:239 claims (both -0.0968932328773).
- The printed-precision convention of the Hamer registry is 12 SIGNIFICANT figures with trailing zeros dropped by float repr, exactly as the constants.py:236-238 comment says (e.g. -0.10637254902 is the paper's 0.106372549020). Confirmed independently by the run's own print format `:+.12g` at 15 hour RUN.txt:7680, and by every one of the four exact round-trips.
- The bridge m_n = 2**(n-1) a_n is genuinely proved as algebra at invariants.py:1366-1379, given x = 2u and m*a = (g^2/2) M: M(2u)/2 has u^n coefficient 2^(n-1) a_n identically for n = 0..4. No 4**r ambiguity enters. (What it does NOT close is whether the program's u equals Hamer's x/2 — that is a separate, still-open normalization assumption.)
- 143/8960 = 0.015959821428571428... rounds at 12 significant figures to 0.0159598214286, which is exactly the printed blind size-1 c4 at 15 hour RUN.txt:10620. Artifact A line 58 and artifact B check 2 are correct as stated.
- The corpus's own pre-2026-08-21 documents are mutually consistent in flagging a_4 as an unpinned notebook transcription: theory/GLUEBALL_DETAILED_FORMULA_2026-08-20_v3.1.md:95, theory/MASTER_THEORY_UNIFIED_2026-08-20_v4_3.md:240, corpus-import/STATE.md:61, corpus-import/literature/README.md:10. Only the 2026-08-21 upgrade disagrees with them, and invariants.py:388 still carries the old text.
- The repo correctly keeps v10a.25 and v10a.26 apart, and this distinction is load-bearing. v10a.25 DOES hard-code the Hamer number (NB_O4_hodge_v10a25_hamer_gelfand_a100.ipynb:7416, `_HAMER_X4=-0.0968932328773`) and its blindness claim is recorded as FALSE at corpus-import/records/audits/05-latest-run-forensics.md:41. M_GAMMA_4_NUM is sourced from [RUN15] = v10a.26 (contradictions.yaml quantities block), which is the blind one. A sibling engine, ENGINE_O4_hodge_v10a27_...py:6, states it 'deliberately contains no Hamer coefficients'.
- C1's by_construction_caveat (contradictions.yaml) correctly flags that the final assembled mass-kernel rest value is FORCED to equal the oracle via local_shift = M4_ORACLE - ax_rest. The run confirms it: 'independently linked local shift= 11.17343231638178' and '[PASS] ... Gamma rest equals independent cluster oracle :: 1.998e-15' (15 hour RUN.txt:10638,10650). The repo does not treat that equality as evidence.
- HAMER_MS_NUM and HAMER_MT_NUM digits appear NOWHERE in the repository outside src/workhouse/constants.py and the generated index/. I grepped all twelve digit strings; zero hits elsewhere. Twelve numbers with no corpus preimage were introduced by the 2026-08-21 registration — which is evidence that whatever was read that day supplied genuinely new content.

### 7.8 `localization-argument` (17)

- FOLD is exactly 5315003/140454 and is exactly the RS renormalisation term: recomputed -2*C_A - E2_A*N_A + J_A with C_A=0, E2_A=-5945/612, N_A=511051/124848, J_A=-48945521/25468992 gives 5315003/140454 = +37.84159226508323 exactly (v10a6:798,802 gates it exactly in Fraction; v10a7:5653 gates it only to 2e-8).
- D_EXACT + FOLD - V_link == M4_SHORTCUT exactly: -361008126292641364183/7250590288602460800 + 5315003/140454 - (-1474623/1675520) = -160506019419340168451/14501180577204921600 = -11.068479463778765. Verified in Fraction.
- THE CENTRAL LOAD-BEARING FACT THE DOCUMENTS NEVER STATE, verified here exactly: the one-face part of the axial fold is EXACTLY ZERO. Running the corpus's own rootonly-firewall module, the isolated one-plaquette axial RS moments are e1=1, e2=-1/4, N=<VR^2V>=1/16, J=<VR^3V>=-1/64, C=C'=0, D=<VRVRVRV>=-13/896, so fold = -e1(C+C') - e2*N + e1^2*J = 1/64 - 1/64 = 0 and D = e4 = -13/896. The reason is a rank-1 accident: the parity-odd basis admits exactly ONE intermediate channel, (2,0) at E=20/3, i.e. Delta=-4 with weight 1 (the self-conjugate intermediates (1,1) and (0,0) are excluded by C-parity), so N=e2^2 and J=e2^3 identically and the fold cancels. Cauchy-Schwarz is saturated: N^2 = e2*J = 1/256. This is why the documents' one-face conclusion survives despite omitting the fold.
- ...and the same construction FAILS at the vacuum face: the one-face vacuum RS pieces are e1=0, e2=-3/4, N=9/32, J=-27/256, D=-309/1280, giving fold = -e2*N = +27/128 = 0.2109375, which is 13.2x the entire claimed one-face gap 143/8960. So 'the one-face fold vanishes' is not a principle; it holds only in the C-parity-odd sector.
- -13/896 + 39/1280 = 143/8960 exactly; 143 = 11*13, 8960 = 2^8*5*7. And EXPECTED_GAP[4] = 143/8960 is already in the corpus at rootonly_firewall:43.
- The blind size-1 row matches the exact one-plaquette gap series at EVERY order, not just c4 - stronger evidence than any of the documents present: printed c1=+1, c2=+0.5, c3=+0.21875, c4=+0.0159598214286 versus EXPECTED_GAP=(8/3, 1, 1/2, 7/32, 143/8960). c2 and c3 are exact in binary.
- NEW: the two branches also share their face-decomposition convention at orders 2 and 3, and the numbers match to print precision. E2_A - (-1/4) - 12*(-3/4) = -71/153 = -0.4640522875816993 versus the blind size-2 c2 = -0.464052287582 (|diff| 3.1e-13, within print rounding); N_A - 1/16 - 12*(9/32) = 40943/62424 = 0.6558855568371139 versus the blind size-2 c3 = -0.655885556837 with the expected sign flip since e3 = sigma3 - N and sigma3 = 0 (|diff| 1.1e-13). This corroborates the size-1 assignment E2[{R}]=-1/4, N[{R}]=1/16 - but note e2 and e3 carry NO fold at all (the fold is a purely O4 object), so the O2/O3 agreement gives zero support to the face decomposition at O4, which is exactly where the bilinear term appears.
- e4(C) - 2*V1 = -54321/837760 + 78/1280 = -327/83776 exactly, and 13*(-39/1280) + 124*(-327/83776) = -1474623/1675520 exactly; 1675520 = 1280*1309 = 83776*20, 1309 = 7*11*17, 837760 = 2^7*5*7*11*17.
- The v10a21r vacuum ledger does attach V1 to the singleton support: _single_emb = sorted(_V17_NEIGH[_mark]) and _V17_NEIGH is built from face_support_faces with the comment '# includes self', count gated == 13, so frozenset((ROOT,ROOT)) = {ROOT} receives V1 = -39/1280. Independently confirmed by solving 13*V1 + b*VPAIR = -1474623/1675520 for nonnegative integers: the unique small solution is (13, 124).
- M4_ORACLE - M4_SHORTCUT = local_shift + V_link holds to float precision: 11.17343231638178 + (-0.8800987156226127) = 10.293333600759167 versus the printed 10.293333600759848; the 6.803e-13 residual is entirely the run's ax_rest float (381 ulps below the exact D+FOLD). The v10a24c source does exactly what the documents say: local_shift = M4_ORACLE - ax_rest added to the diagonal at anchor faces, then gated against M4_ORACLE (v10a24c:7324-7336). So the 'rivals, not input/output' dataflow claim is correct - it is only the 'same coordinate' claim that is unsupported.
- The W22 line-number citations are accurate: DATA_O4...:614 'exact one-face coefficients agree with and without W22 through O4', :615 'exact one-face O4 coefficient is -13/896', :616 o5_difference == Fraction(-5,7168), :610 'W22 first enters a closed walk at order five'. B:80's citation of :615 and B:82's citation of v10a21r:313,358 (analytic_11 = -13/896, V1 = -39/1280) are both correct.
- D §2's claim that the blind cluster basis contains Q2<->Q2 is correct: v10a24c:6884-6899 applies W to every retained basis vector and projects onto every compatible row with no layer mask. D §2's caution that 'the mere presence of the block does not prove that it changed the true fourth-order Taylor coefficient' is also correct.
- The v10a24c fit parameters D §2 quotes are right for that file: V23C_FIT_UMAX=0.055, V23C_FIT_DEG=6, V23C_FIT_N=13 at v10a24c:6792-6794. (They are simply not the method behind the transcript the documents use.)
- D §3's account of the rooted-Mobius ordering in v10a24c is correct: vacuum is subtracted inside the raw cluster gap before Mobius (_v23c_cluster_gap_value returns Heff[root,same].sum() - Ev), the rooted poset is downward-closed, and proper rooted connected subclusters are subtracted from the raw gap (v10a24c:7283-7291).
- The v10a.21r retraction quotes B §4 relies on are verbatim in the corpus: Monday 531 PM.txt:1978 'Stop. Do not run v10a.21r.', :2287 'Retire v10a.21/v10a.21r as adjudicators...', :2548, :2925 ('algebraically wired to reproduce v10a.20'), :3702, :3897.
- The repo's RAW_FOLDED_AXIAL_GAMMA_NUM = -11.9485781794007 (constants.py:428) is a faithful transcription of the run's printed float (15 hour RUN.txt:9112), not a transcription slip; the 381-ulp gap to the exact D+FOLD is the run's own float error. RUN15_APPLIED_SHIFT_NUM = 11.17343231638178 (constants.py:436) matches the transcript exactly.
- The certificate zip (E) states D_EXACT = -13/896 + (1/2)*sum_T w_T H_T, i.e. -13/896 is genuinely a separated additive term of the F07 direct sum - consistent with v10a21r's analytic_11 injection, and legitimate precisely because the one-face fold vanishes (no double counting).

### 7.9 `rules-compliance` (12)

- One-face gap arithmetic (A §2 row 1): −13/896 + 39/1280 = 143/8960 exactly; 143 = 11·13, 8960 = 2^8·5·7. Recomputed in fractions.Fraction.
- Every corpus file the documents cite exists in this repository at the cited path: DATA_O4_OrderSchedule_Occurrence_Preflight_CPU.py, ENGINE_O4_hodge_rootonly_firewall_v1.py, ENGINE_O4_hodge_v10a21r_adjudicator_only_same_kernel.py, records/transcripts/15 hour RUN.txt, records/transcripts/Monday 531 PM.txt.
- Line citations are accurate, both A's and B's. Preflight :610 = "W22 first enters a closed walk at order five", :614 = "exact one-face coefficients agree with and without W22 through O4", :615 = "exact one-face O4 coefficient is -13/896", :616 = o5_difference == Fraction(-5,7168). A cites 610/614/616 and B cites 615; both are exactly right. ENGINE_O4_hodge_rootonly_firewall_v1.py:41-42 carries EXPECTED_VACUUM and EXPECTED_AXIAL verbatim as printed (and :43 already spells out EXPECTED_GAP with 143/8960). 15 hour RUN.txt:10619-10626 is the [16] ROOTED INCIDENCE TRANSFORM block.
- The W22 one-face facts reproduce exactly when the corpus function is executed here: o4_equal True, full = (8/3, 1, −1/4, −1/16, −13/896, −23/12544), pruned O5 = −57/50176, o5_difference = −5/7168, nine closed four-step layer walks, W22 first closed order 5. The content of A §2 row 3 is right; only its tier and its "explained" framing are not.
- The certificate's arithmetic re-derives completely and cheaply from the shipped pinned ledger: 69,800 records, indices sequential, 9,184 zero-Haar, every record satisfies haar == scaled_haar_numerator/q_product and weighted_contribution == weight·haar (0 exceptions), Σ w_T H_T = −805586892848311021/8092176661386675, D_EXACT = −13/896 + Σ/2 = −361008126292641364183/7250590288602460800, and D_EXACT + 5315003/140454 − (−1474623/1675520) = −160506019419340168451/14501180577204921600 = the repo's QUARANTINED_SCALAR. Runtime a few seconds over the 1.5 MB gz.
- QBOUND divisibility (the basis of A §6 item 5): 7250590288602460800 divides 62895057857493885215590055852113920000000 exactly (quotient 8674474126108262400000), and the stated lift −3131555650840341423974721085483725619200000/QBOUND reduces exactly to D_EXACT. Denominator factors 2^7·3^6·5^2·7·11·13·17^3·19·29·31·37; QBOUND factors 2^36·3^20·5^7·7·11·13·17^3·19·23·29·31·37·47.
- All 20 digests in cert/SHA256SUMS.txt verify against the extracted files (sha256sum -c: 20/20 OK).
- The package's LINKED_VACUUM_EXACT = −1474623/1675520 agrees exactly with the repo's registered LINKED_VACUUM_4 (constants.py:430) — a genuine outside corroboration of a registered exact constant.
- A §5 bullet 4 and B §7 are correct restraint: deferring the M4_SHORTCUT relabel to the maintainer, citing non-negotiable #2, is exactly what ADR 0001 requires ("This repository verifies arithmetic and records status. It does not adjudicate."). Quantifying the F07-vs-blind disagreement is explicitly permitted by the same ADR ("may quantify the disagreement *between* kernels. Neither is a promotion.").
- A §4's v10a.21r trap is correct and well-sourced; the retraction quotes resolve to real targets in corpus-import/records/transcripts/Monday 531 PM.txt at the cited lines, and it correctly refuses a route that would produce a green-looking comparison with no content.
- |M4_ORACLE − M4_SHORTCUT| = 10.293333600759848 as A §1 states; float(QUARANTINED_SCALAR) = −11.068479463778765 as the existing repo check asserts.
- `workhouse triage` runs cleanly on the upload directory and reports none of the five artifacts as byte-identical to anything already pinned — confirming they are unpinned outside material and that triage is the correct first move on them.

### 7.10 `corpus-value-search` (14)

- 143/8960 = -13/896 + 39/1280 exactly, and 143 = 11*13, 8960 = 2^8*5*7. Verified in Fraction; matches the corpus's own EXPECTED_GAP fifth entry at ENGINE_O4_hodge_rootonly_firewall_v1.py:43.
- -327/83776 = e4(C) - 2*V1 = -54321/837760 - 2*(-39/1280) exactly. Verified in Fraction. Both inputs are corpus-gated at ENGINE_O4_hodge_v10a7_marked_linked_scalar.py:5433-5434.
- 1675520 = 1280*1309 = 83776*20, and 1309 = 7*11*17. Verified; also stated in the corpus at corpus-import/records/transcripts/chat.txt:1770-1775.
- 13*V1 + 124*VPAIR = 13*(-39/1280) + 124*(-327/83776) = -1474623/1675520 exactly. Verified in Fraction; matches the corpus gate at ENGINE_O4_hodge_v10a21r_adjudicator_only_same_kernel.py:367-369 and the counts at theory/superseded/MASTER_THEORY.md:568 (13 one-face; 124 pairs = 80 perp + 44 coplanar).
- The certificate zip's `weighted_haar_sum` = -805586892848311021/8092176661386675 reconciles exactly with document C's D_EXACT: D11 + (1/2)*weighted_haar_sum = -13/896 + (1/2)*(-805586892848311021/8092176661386675) = -361008126292641364183/7250590288602460800. Verified in Fraction. C's stated formula D_EXACT = D11 + (1/2)*sum(weight*Haar) is internally consistent with E.
- Every denominator the documents rely on divides QBOUND = 62895057857493885215590055852113920000000 = 2^36*3^20*5^7*7*11*13*17^3*19*23*29*31*37*47: 14501180577204921600, 7250590288602460800, 8092176661386675, 83776, 837760, 1675520, 8960, 896, 1280, 140454, 7168. So the "den | QBOUND" capstone claim (A §2) checks out arithmetically for every value I could test.
- All four documents' line cites into corpus-import/records/transcripts/15 hour RUN.txt are accurate: :10620 size-1 row, :10621 size-2 row, :10626 TOTAL, :10633 the shortcut and |Δ|, :10743-10750 the 203/33 summary (203/33 appears at :10747).
- Document B's cites into DATA_O4_OrderSchedule_Occurrence_Preflight_CPU.py are accurate: :615 gates -13/896, :616 gates o5_difference == Fraction(-5,7168), and A's :614 is the o4_equal gate.
- Document B's cite ENGINE_O4_hodge_v10a21r_adjudicator_only_same_kernel.py:313,358 is accurate: :313 `analytic_11=_XQ(-13,896)`, :358 `V1=_XQ(-39,1280)`, :359 `VPAIR=_XQ(-327,83776)`. The names V1 and VPAIR are corpus vocabulary, not coinages (also records/audits/08-rooted-adjudication.md:45).
- The v10a.21r circularity claim (B §4) is correct and load-bearing. The engine hard-codes D_EXACT and M4_EXACT at :41-43 as "Exact values already independently certified by the completed v10a.20 run", then gates its Möbius total against M4_EXACT. records/audits/08-rooted-adjudication.md:52-54 independently describes it as hard-coding the claimed completed results.
- M4_SHORTCUT, M4_ORACLE, ax_rest, local_shift, W22, VPAIR, V1, D_EXACT, QBOUND and "two-face" are all corpus vocabulary (v10a.23/24c/26 sources, v10a.21r, the order-schedule preflight, audits 07/08). None is a repository coinage and none collides with a repo-coined name in ledger/symbols.yaml (whose only coined_here entry is Phi_C).
- The exact rational -160506019419340168451/14501180577204921600 = D_EXACT + FOLD - V_link is confirmed in Fraction, and the float -11.068479463778765 is its correct double.
- Document C's structural claim that the corpus separates M4_ORACLE, M4_SHORTCUT and ax_rest is right, and the repository agrees: constants.py:427-435 records QUARANTINED_SCALAR, RAW_FOLDED_AXIAL_GAMMA_NUM and RUN15_APPLIED_SHIFT_NUM as three distinct entries.
- The corpus's own 15-hour run already refuses to promote either side: 15 hour RUN.txt:10750 "FINAL VERDICT : MIXED/THIRD RESULT — DO NOT PROMOTE EITHER FOURTH-ORDER CLAIM". The documents' refusal to promote is consistent with the corpus record.

---

## 8. Claims not verifiable from this repository (79)

Neither confirmed nor refuted. Almost all are citations into the external
`work/rank3_order4_*` and `work/fold_linked_exact/` trees, which were not delivered.
Listing them is the point: it is the precise inventory of what would have to be shipped
for the upload's claims to become checkable here.

### 8.1 `citations-AB` (8)

- `f07_twoface_adjudication_check.py` (A:27, A:147, A:163; B:8, B:187, B:234) — does not exist anywhere on this machine (filesystem-wide find), is not in the extracted certificate zip, and was not uploaded. Every claim about it (exit 0; 8 checks per A / 6 rows per B; "Verified: the guard rejects an F07 size-2 value tagged with retired-engine provenance", B:198-199) is unverifiable.
- `exact_haar_sum.py:276-368, 81-111` (B:163-165, the claim that the exact-Haar package aggregates by endpoint trace-states and forgets lattice geometry) — external to this repo (work/rank3_order4_exact_haar_run/); no such file here. Unverifiable, neither confirmed nor refuted.
- "the F07 package fixes `polarization_index = 2`" (B:174-175) — external exact-Haar package; no in-repo occurrence.
- The exact scalar `D_EXACT + FOLD` and the identity `M4_SHORTCUT = ax_rest − V_link` are computed outside this repo. The repo does record the recipe secondhand at corpus-import/records/audits/07-denominator-lift.md:38 (`M4_EXACT = D_EXACT + FOLD_EX − VLINK_EX`, with FOLD_EX = 5315003/140454 and VLINK_EX = -1474623/1675520), but D_EXACT itself is a notebook runtime product, so I could not independently re-derive it here.
- The integer value of QBOUND — computed at notebook runtime as a prime-exponent LCM (07-denominator-lift.md:35), never serialized into the repo. I verified divisibility against den(D_EXACT) instead.
- Everything v10a.21/v10a.21r would *output*, including B §4's "Its size-1 weight is 143/8960": neither notebook was ever executed (execution_count None, zero outputs) and no transcript carries the engine's size-table prints. Only its source assertions are checkable, and those all check out.
- Three of the six documents in A's own §0 reading list are not among the five artifacts under audit: A's "A" = DENOMINATOR_LOCALIZATION_INVESTIGATION (referenced at A:21, A:66, A:125, A:154), A's "C" = ORACLE_COUNTERFACTUAL_AUDIT (A:23, A:63, A:64, A:138), A's "F" = F07_VS_BLIND_COORDINATION_NOTE (A:26, A:29, A:135, A:146). So A §2's rows "F07 anchoring-invariant … (audit C §4)" and "F07 oracle-free … (B §2, C §3)", and the §5 correction to "document A §11.3/§12", cannot be checked in my lane. Caution for the parent: A's internal letters A–F do NOT match this audit's A–E labels (A's "E" is this audit's B; A's "B" is this audit's C; A's "D" is this audit's D).
- A §2's capstone row "`den | QBOUND`, the C2 localization gate, a hash-frozen Lean-adjacent derivation" (A:66-70) cites document A §11.2 only; no in-repo pointer, and there is no Lean file in lean/Workhouse touching these values.

### 8.2 `citations-CD` (12)

- EXTERNAL — work/rank3_order4_cubic_ledger/primitive_rank3_order4_cubic.json (C §2 cites :3-14, :16-33, :36-43, :45-59, :61-70, :81-99; D §2 cites :3-14). Not present in this repo and not in the delivered certificate zip. NOTE: its `local_q_pattern` content is indirectly corroborated — the delivered summary's table is bit-identical to _LOCAL_Q at v10a.20b cell line 6382.
- EXTERNAL — work/rank3_order4_cubic_ledger/ledger_generator.py (C cites :1-12, :344-357 twice, :516-568, :700-751, :754-760, :763-809, :1199-1213, :1215-1231, :1285-1341, :1541-1608, :1653-1675; D cites :1199-1215 and :910-963,1250-1261). Absent. C's dataflow-independence argument (§2) rests almost entirely on this file; nothing here can confirm or refute it.
- EXTERNAL — work/rank3_order4_cubic_ledger/exact_haar_sum.py (C cites :35-41, :218-272, :276-368, :601-608, :606-608, :935-955, :957-959, :957-971, :1000-1037, :1073-1080, :1073-1088, :1135-1148, :1145-1154; D cites :81-111, :276-368). Absent.
- EXTERNAL — work/rank3_order4_cubic_ledger/verify_exact_haar_ledger.py:17-35 (C §4). Absent.
- EXTERNAL — work/rank3_order4_cubic_ledger/canonical_run_final_20260823/rank3_order4_cubic_freeze.json (C §3). Absent.
- EXTERNAL — work/rank3_order4_exact_haar_run/rank3_order4_exact_haar_summary.json:1 (C §3). A file of that exact name IS in certificate artifact E, but its SHA (2b845725...) does not match C's chain row and it binds no history or contractor hash — see finding c-hash-chain-mismatch-vs-shipped-cert. Whether E's copy is the same artifact C cites cannot be determined here.
- EXTERNAL — work/rank3_order4_exact_haar_package_verify/WORKHOUSE_RANK3_ORDER4_EXACT_HAAR_FINAL_AUDIT_20260823.md (D cites :9-40, :42-55, :57-91, :65-75, :93-126, :93-160, :124-126, :158-160). Absent from repo and from the certificate zip. D's D11 citation is the one claim here that is independently confirmable in-repo (see confirmed list).
- EXTERNAL — work/fold_linked_exact/README.md (D cites :8-19, :21-27, :36-48, :59-64). Absent from repo and certificate zip. The two values D draws from it, -39/1280 and the H = H0 - u M convention, are corroborated in-repo (gates at ENGINE_O4_hodge_v10a7_marked_linked_scalar.py:5411 and ENGINE_O4_hodge_v10a24c...py:6247); the README's target-independence claims for the fold/vacuum replayers are not checkable.
- C §3's nine-row frozen hash chain (primitive JSON 3685369c, canonical parsed 2eda6c89, generator a72a2c41, freeze e68d5158, history ledger 543869b1, contractor f944bfef, topology ledger gzip 48abeca4 and uncompressed a7f13ca1, summary d3d2cb89) plus the 164,662 = 82,384 W2 + 82,278 R2 record count. None of these hashes appears in corpus-import/SHA256SUMS or in the certificate zip's SHA256SUMS.txt.
- C §2's negative search result — "A scoped search across the primitive manifest, generator, contractor, package builder, verifier, and independent-Haar sources found no occurrence of M4_ORACLE, ax_rest, local_shift, K4_mass, or M4_SHORTCUT." All searched files are external. The claim is unfalsifiable from here.
- Both documents' physical-identification verdicts (C §9, D §7) — whether the frozen F07 trace-history formula equals the canonical physical-P/Q Hermitian SW/BCH coefficient. This is a mathematical open question, not a citation; nothing in the repo settles it, and both documents correctly decline to claim it.
- D §4's inventory table rows for the exact-F07 branch (117,161 -> 69,800) are corroborated numerically by the certificate summary (keys /historical_orientation_sensitive_topologies and /fully_unordered_nonzero_topologies) and by the v10a.20b notebook gate at cell line 6371, but the claimed lossless quotient map between them is not checkable here.

### 8.3 `arithmetic` (11)

- Everything rooted at work/rank3_order4_cubic_ledger/ — the primitive manifest (primitive_rank3_order4_cubic.json), ledger_generator.py, exact_haar_sum.py, verify_exact_haar_ledger.py. C §2, C §4 and C §5 hang almost entirely on these: the generator's module contract, the source->W1->R1->W2->R2 path at :1199-1213, the freeze at :1285-1341, the generate/audit subcommand separation at :1541-1608/:1653-1675, the census pins at :1215-1231 and exact_haar_sum.py:35-41/:218-272/:276-368/:957-971/:1000-1037/:1073-1088/:1135-1148, the geometry-forgetting canonicalization at :81-111, and the FOLD/LINKED constants declared at :601-608. None of these files is in this repo or in the certificate zip.
- C §3's hash chain, eight of eleven rows: raw primitive JSON, canonical parsed primitive content, final W2/R2 generator, final freeze file, W2/R2 history ledger, exact endpoint-Haar contractor, exact topology ledger (gzip and canonical uncompressed), final exact summary. Only the three *provenance-document* hashes (rows in the second table) are checkable here — and all three match. Note separately that two of the eight do not match the corresponding artifacts actually shipped in the certificate zip (see finding cert-no-history-binding).
- C §3's record counts 164,662 = 82,384 W2 + 82,278 R2. The arithmetic is right; the counts describe an external ledger.
- C §4's 2,468,250 compatible state pairs as a *pin in exact_haar_sum.py* — the number itself is corroborated in this repo (15 hour RUN.txt:9043 'pair-occ=2,468,250'), but that it is gated at exact_haar_sum.py:35-41 cannot be checked.
- C §6's line-level call flow inside ENGINE_O4_hodge_v10a7_marked_linked_scalar.py (:4548-4596, :4599-4614, :4652-4679, :5483-5508, :5574-5589, :5602-5624, :5646-5653, :5687-5707, :5720-5747, :5181-5182) was not spot-checked line by line; only the file's SHA-256 (which matches) and the two lines B cites (:5438-5444, the disconnected-spectator gate) were verified.
- D's citations into work/rank3_order4_exact_haar_package_verify/WORKHOUSE_RANK3_ORDER4_EXACT_HAAR_FINAL_AUDIT_20260823.md (:9-40, :42-55, :57-91, :93-126, :124-126, :65-75, :158-160) and work/fold_linked_exact/README.md (:8-19, :21-27, :36-48, :59-64). Both files are external. In particular the exact marked-vacuum replay giving e4_vac^(1) = -39/1280 is unverifiable from the cited source (though the value itself is corroborated at ENGINE_O4_hodge_rootonly_firewall_v1.py:41 and v10a21r:358).
- A §2's row 'F07 anchoring-invariant | T1 | derivative of every upstream quantity w.r.t. the anchor scalar is 0 (audit C §4)' and 'F07 oracle-free | two independent scanners, zero leakage (B §2, C §3)'. The ORACLE_COUNTERFACTUAL_AUDIT and the coordination note were not supplied; C §2's scoped-search claim ('found no occurrence of M4_ORACLE, ax_rest, local_shift, K4_mass, or M4_SHORTCUT') is over external sources.
- The companion script f07_twoface_adjudication_check.py itself — cited in A §0, A §6, B §0, B §6 and B §8 as exit-0 and machine-verified, and the source of the 8-vs-6 check-count conflict. Not present in the uploads or in /home/user/WORKHOUSE, so neither the count nor the claimed provenance guard behaviour ('the guard rejects an F07 size-2 value tagged with retired-engine provenance') can be checked.
- Referee report: 'Three-way synthetic tests agreed on 180/180 contractions among two exact delta/partition implementations and the modular implementation.' No artifact in the zip records 180; the reference-crosscheck JSON records only balanced_inverse_gram_exact_matches (3 entries), 20 signatures / 40 topologies, and the pure-six figures. Prose-only.
- Referee report: 'the earliest certificate fault is the old topology contractor's use of a floating Haar value followed by multiplication by q_H and rounding to an integer' and 'the earlier pair key was also representation-sensitive'. Historical claims about code not in the zip; the closest corroboration in this repo is audits/07-denominator-lift.md:74 and :46 of the duplication report, which say something compatible but not identical.
- A §4's blind two-face target -0.403971702978 is verifiable as a printed value (15 hour RUN.txt:10621) but the claim that the F07 two-face weight is 'unresolved' — and the whole Knob A / Knob B experimental design — is a statement about work not yet done, not a numeric claim.

### 8.4 `certificate` (9)

- Everything upstream of root_exact_pair_topologies.pkl.gz. The (topology, weight) pairs and the 69,800-class census ARE the physics input here; the package certifies only what is done to them. Nothing in the zip derives, checks, or hash-binds a single weight.
- "The frozen 117,161 orientation-sensitive topology keys were losslessly aggregated into 69,800 fully unordered contraction classes" and "The quotient was performed by summing exact weights before contraction; it does not change the scalar" (AUDIT_REPORT.md:5, INDEPENDENT_REFEREE_REPORT.md:54). No code or data in the package performs or witnesses this map. 117,161 exists only as an integer field inside the pickle's counts dict.
- The provenance of D11 = -13/896. It is a bare literal in three shipped scripts, contributes -0.014508928571 directly to D_EXACT, and has no derivation, citation, or source artifact anywhere in the package. It also appears nowhere in WORKHOUSE outside corpus-import.
- That FOLD = 5315003/140454 and V_linked = -1474623/1675520 were "separately reproduced". V_linked is corroborated independently by the repo (constants.py:430); FOLD is not — it exists in WORKHOUSE only inside corpus-import, and not at all in the package beyond the literal.
- The referee report's "Earliest historical certificate fault" section in its entirety (lines 56-60): the old topology contractor's float-then-round Haar value, the dense/long-double agreement, and the representation-sensitivity of the earlier pair key. None of those programs is in the package.
- "That factor [the final 1/2] is consistent with the stored sqrt(2) scaling of both halves of the bilinear" (INDEPENDENT_REFEREE_REPORT.md:58). The 1/2 is applied unconditionally at modular_haar_contractor.py:511 and independent_replay_modular_crt.py:108; nothing in the package establishes the sqrt(2) convention.
- The generation-census integers the referee report cites — 5,400 matched sectors, raw pair upper bound 9,814,138, 54 skipped one-face matches, 2,468,250 compatible state pairs, 3,642 block orbits, 1,831,607 pair occurrences. All are asserted integers inside the pickle; nothing recomputes any of them. (Note document C's §4 quotes the historical notebook as 3,597 orbits and 1,829,147 pair occurrences against the pickle's 3,642 and 1,831,607 — I cannot adjudicate that from E, but it is a discrepancy someone should chase.)
- Whether QBOUND = 2^36·3^20·5^7·7·11·13·17^3·19·23·29·31·37·47 was derived a priori or fitted. Its exponents for 17, 23, 29, 31 and 37 exactly equal the observed lcm of the run's term denominators, which is consistent with fitting, but no derivation is shipped. The unused prime 47 is unexplained.
- The disposition of the whole route relative to WORKHOUSE's C2 / physical-identification question. E explicitly disclaims it (AUDIT_REPORT.md:59, INDEPENDENT_REFEREE_REPORT.md:62) and that disclaimer is correct and should be preserved in any downstream write-up.

### 8.5 `ledger-graph` (5)

- Everything rooted at work/rank3_order4_cubic_ledger/, work/rank3_order4_exact_haar_run/, work/rank3_order4_exact_haar_package_verify/ and work/fold_linked_exact/ is absent from this repo. That covers the load-bearing new facts: the exact-Haar package producing -160506019419340168451/14501180577204921600 target-free, the 69,800-class ledger and its CRT uniqueness proof, D_11 = -13/896 as a replay output, e4_vac(1) = -39/1280 from work/fold_linked_exact/README.md:21-27, the 117,161 -> 69,800 lossless quotient, and the 3,895 Stage-3H record count. Neither confirmable nor refutable here.
- `QBOUND` (A §2 capstone "den | QBOUND", B §3 "in-scope, | QBOUND", A §6 item 5 "the frozen QBOUND cert") does not exist anywhere in this repository — grep across src/, ledger/, theory/, index/ returns zero matches. The divisibility claim cannot be checked here and no ledger entry could cite it without importing an undefined term.
- A §2's rows "F07 anchoring-invariant | T1 | derivative of every upstream quantity w.r.t. the anchor scalar is 0 (audit C §4)" and "F07 oracle-free | two independent scanners, zero leakage (B §2, C §3)" cite documents by internal letters that do not map onto the five artifacts supplied — A's own §0 table lists six documents A-F, of which ORACLE_COUNTERFACTUAL_AUDIT and F07_VS_BLIND_COORDINATION_NOTE were not uploaded. Those claims rest on documents I do not have.
- `f07_twoface_adjudication_check.py`, referenced throughout A and B as the runnable spine and as a drop-in invariants.py suite, was not supplied and is not in the repo. B §6's six-row check table and its "provenance guard" behaviour are asserted, not verifiable — including the claim that the guard "rejects an F07 size-2 value tagged with retired-engine provenance".
- Whether -11.068479463778765 and -0.7751458630189173 are rival estimates of one quantity or differently anchored coordinates cannot be settled from this repo. The one test ADR 0002 supplies — whether the difference is a translation-local scalar shift leaving the centered operator invariant — needs both branches' centered kernels, which are not here. This is the question the whole proposal turns on, and it is open in the strict sense.

### 8.6 `invariants-tests` (6)

- `f07_twoface_adjudication_check.py` itself was NOT uploaded — only described in A §0/§6 and B §6. Its actual check count, names, tolerances, exit code, and the behaviour of its 'provenance guard' (B §6: 'Verified: the guard rejects an F07 size-2 value tagged with retired-engine provenance, and accepts one tagged with an independent (§5-compliant) source') cannot be checked here. Everything I say about duplication is against the six rows B §6 tabulates and the eight rows A §2 tabulates, not against code.
- A §2 row 8 'F07 oracle-free — two independent scanners, zero leakage (B §2, C §3)': the two scanners are described in the external trace documents and run over work/rank3_order4_exact_haar_run/ and work/fold_linked_exact/, which are not in this repository. Not checkable here in either direction.
- B §5 item 1 cites `exact_haar_sum.py:276-368, 81-111`. No file named exact_haar_sum.py exists anywhere in /home/user/WORKHOUSE (find, excluding .venv). It is in the external work/rank3_order4_exact_haar_run/ tree.
- B §5's remaining structural requirements — the 3,895 Stage-3H records, the unshifted 189-record full-T1 kernel, the 609-cluster full-T1 run cost (A §4), the degree-6 fit on 13 points at ENGINE...v10a24c...py:6894-6899/6928-6946 (the file exists at corpus-import/programs/hodge_o4_adjudication/src/ENGINE_O4_hodge_v10a24c_rootedfullt1_dualcoldoracle_a100.py but I did not verify those line ranges; that is another lane's).
- A §2 row 7's underlying claim ('derivative of every upstream quantity w.r.t. the anchor scalar is 0, audit C §4') — the counterfactual audit is document C's, and its computation is external. Only the general anchoring-invariance statement is checkable here, and it already is (invariants.py:340).
- Whether either branch (F07 -11.0685 or blind -0.7751) is the canonical physical fourth-order coefficient. This is C2/G3 and is open by construction; nothing in this repo adjudicates it, and nothing in the uploaded documents does either — which both documents state correctly.

### 8.7 `hamer-circularity` (5)

- Whether Hamer 1989 Table 1 actually prints -0.968932328773 E-1. The PDF is not stored (literature/index.yaml:463-470, `fulltext: null`, publisher copyright) and the pin sha256 96b3ec0f... refers to a maintainer-supplied copy that exists nowhere in this repository. This is the ONE artifact that would close the a2/a3 circularity question, and it is the one that cannot be reproduced here.
- Whether HAMER_MA_NUM orders 5-7, HAMER_MS_NUM orders 4-7, and the entire HAMER_MT_NUM (2++) column correspond to the paper. They have no in-program counterpart and no corpus preimage, so nothing here can check them. Weak internal evidence only: their Domb-Sykes ratios are not smooth (MA: -6.08, +0.887, +0.721, +0.589, +0.418; MS: +0.244, +5.35, +0.967, +0.741, +0.234; MT: +0.459, +0.096, +2.73, +0.377, -0.086), which is unremarkable for a 6-term strong-coupling series with sign changes and proves nothing either way.
- KSS_1976's x^3 and x^4 coefficients — the one genuinely independent external cross-check on Hamer's a_3 and a_4 available in principle. literature/index.yaml:96,109-127 records the paper as `not-yet-obtained` (Elsevier open archive refuses automated retrieval). Reading it would turn Hamer's reported disagreement into a measured number and would, incidentally, test whether the registered Hamer digits behave like a real 1989 table.
- Whether the 2026-08-21 read was blind. Even granting that a real PDF was read, the reader already held the transcription in constants.py, so the read was a confirmation, not an independent transcription. Nothing in the repo records whether the digits were re-read cold or checked against the existing value. A record of that procedure (or a second, independent transcription by someone not shown the registry) would settle the a2/a3 question without needing the PDF.
- Everything rooted at work/rank3_order4_cubic_ledger/, work/rank3_order4_exact_haar_run/, work/rank3_order4_exact_haar_package_verify/, work/fold_linked_exact/ — external to this repository and absent. In my lane this touches artifact D's section 5, which cites work/fold_linked_exact/README.md:8-19 for the shared `H = H0 - u M` convention.

### 8.8 `localization-argument` (6)

- Everything under work/rank3_order4_cubic_ledger/ (primitive_rank3_order4_cubic.json, ledger_generator.py, exact_haar_sum.py), work/rank3_order4_exact_haar_run/, work/rank3_order4_exact_haar_package_verify/ (the FINAL_AUDIT document D cites at :9-40,42-55,57-91,93-160) and work/fold_linked_exact/README.md - external to this repo, not present. In particular D §1's provenance for e4_vac(1) = -39/1280 (work/fold_linked_exact/README.md:21-27) and D §6's claim that the fold and linked-vacuum replays are target-free (:36-48) cannot be checked here. The values themselves are independently corroborated inside this repo (rootonly_firewall:41 for -39/1280; v10a6:802 for the fold), so the numbers are fine; it is the independence claim that is unverifiable.
- The lattice values of E2_MIN[{ROOT}], N_MIN[{ROOT}], J_MIN[{ROOT}] and C_MIN[{ROOT}] - the quantities that decide whether the fold's singleton support really is zero on the lattice rather than in the isolated one-plaquette problem. ENGINE_O4_hodge_v10a21r_...py is a same-kernel Colab resume cell that raises RuntimeError unless ~30 globals from a completed v10a.20 run are in scope (:23-38), and no v10a.21/21r size table appears in any transcript (grep 'size sums' returns nothing corpus-wide). So the corpus's only F07 face decomposition has never been executed, or its output was never kept.
- S = sum_f E2_MIN[{ROOT,f}] * N_MIN[{ROOT,f}], the pair-times-pair term of the union convolution. It needs per-neighbour resolution that no corpus record contains. This leaves FOLD[size2] = -0.30692 - S and FOLD[size3] = +38.14851 + S individually undetermined (S cancels in the total). The uniform-neighbour estimate S = -3.179 gives +2.872 and +34.97; with S = 0 they are -0.307 and +38.15. Either way FOLD[size3] is 196x to 213x the blind size-3 weight, so the conclusion does not depend on S.
- Whether the exact-Haar package's D_EXACT and the v10a.26 run's cold-folded ax_rest are the same object beyond float agreement. The transcript's Gamma moment audit (15 hour RUN.txt:9129) prints D = -49.79017044448387, C = 0.0, N = 4.093385556837106, J = -1.9217690672642245 against the exact -49.790170444484609, 0, 511051/124848, -48945521/25468992 - agreement to ~1e-12 - but the transcript gives no exact rational for its own D, so 'the two branches share ax_rest' is T2 at ~1e-12, not T1.
- Whether the historical q_band^(4) = -2.857915988114559 stands in any definite relation to ax_rest or M4_SHORTCUT. There are now at least four anchorings of this scalar in the program (ax_rest -11.9486, M4_SHORTCUT -11.0685, q_band -2.8579, m_Gamma -0.7751) and only the q_band/m_Gamma pair has been adjudicated (ADR 0002). Placing M4_SHORTCUT in that lattice is exactly the open question and cannot be settled from arithmetic here.
- The QBOUND divisibility claims attached to 83776 in B §3 - QBOUND itself was not located in this lane, so only the factorization was checked, not the divisibility.

### 8.9 `rules-compliance` (9)

- Everything under work/rank3_order4_cubic_ledger/, work/rank3_order4_exact_haar_run/, work/rank3_order4_exact_haar_package_verify/ and work/fold_linked_exact/ — external to this repo and NOT supplied by the certificate zip either. The zip ships the audit half only (modular_haar_contractor.py, independent_*.py, validate_modular_haar_ledger.py, outputs); the generating half (primitive_rank3_order4_cubic.json, ledger_generator.py, exact_haar_sum.py, verify_exact_haar_ledger.py, rank3_order4_cubic_freeze.json) is absent. Every line citation in documents C and D into those trees is therefore uncheckable here.
- FOLD_EXACT = 5315003/140454. It is used and it makes the final assembly come out right, but nothing in this repository or in the delivered zip derives it; the fold reproducer lives in the absent work/fold_linked_exact/.
- The 164,662-record W2/R2 history (hash 543869b1…) and the claim that the contractor regenerates and verifies it before contracting — the history is not shipped, so what I re-derived is the ledger→scalar step, not the generation step.
- A §2 row 8, "two independent scanners, zero leakage": neither scanner nor transcript was shipped, and the audit that reports one (internal document C) was not delivered.
- A §2 row 7's anchoring-invariance derivative claim (audit C §4, not delivered).
- A §2's capstone and A §6 item 5, both of which rest on sections §5.5, §6 and §11.2 of the undelivered DENOMINATOR_LOCALIZATION_INVESTIGATION.
- Whether the "independent referee" route is independent in AGENTS.md's sense. Both routes are same-session, same-author, target-known; document C §7 concedes the design coupling in its own words ("the expected scalar and census were known when the algorithm and regression gates were frozen"). AGENTS.md: count distinct originating computations, not implementations.
- Whether the blind branch's size-1 c4 agrees with 143/8960 beyond the 12 significant digits the transcript prints. The printed 0.0159598214286 is the correct 12-digit rounding of 143/8960 (gap 2.86e-14), which is all the transcript can support; the underlying float is not recoverable from the record.
- Whether the +45 block-orbit / +2460 pair-occurrence divergence in finding `unremarked-census-divergence` is expected under the new canonicalization — the code that would settle it is not shipped.

### 8.10 `corpus-value-search` (8)

- Everything cited under work/rank3_order4_cubic_ledger/ (primitive_rank3_order4_cubic.json, ledger_generator.py, exact_haar_sum.py, verify_exact_haar_ledger.py), work/rank3_order4_exact_haar_run/, work/rank3_order4_exact_haar_package_verify/ and work/fold_linked_exact/ is external to this repository and absent. Every line cite in C §2, §3, §5, §7 and D §1, §2, §3, §6 into those paths is unverifiable here. The certificate zip E is the same package, so it corroborates nothing independently.
- The integers 69800, 2468250, 164662, 82384 and 82278 have ZERO occurrences anywhere in corpus-import/, src/, ledger/, theory/, docs/ or index/. They exist only in the external package and in E. The claim "164,662 = 82,384 W2 + 82,278 R2" (C §3) is arithmetically consistent but has no corpus anchor.
- The literal digits of QBOUND (62895057857493885215590055852113920000000) appear nowhere in the corpus — only in E (rank3_order4_exact_haar_summary.json:14, validation.json:7, and the three cert markdowns). QBOUND is a NAMED corpus concept (records/audits/07-denominator-lift.md:35,36,38,51,59,95,121; 08-rooted-adjudication.md:37) but its value is only ever constructed, never printed. So the divisibility checks I ran validate the external number's internal consistency, not its identity with the corpus's QBOUND.
- The rational -805586892848311021/8092176661386675 (E's weighted_haar_sum) has zero corpus occurrences.
- -361008126292641364183/7250590288602460800 (D_EXACT) occurs in only two corpus files, both prose, and the second quotes the first: records/audits/08-rooted-adjudication.md:53 and corpus-import/theory/DOC_FLUX_constants_index.md:144 (whose row literally cites audits/08:53). No executable corpus file stores it. So it is one asserted value with one origin, not an independently reproducible corpus constant.
- Whether the v10a.28 order-aware Gram firewall has ever been run at order four to produce its by_size table: no transcript in the corpus records that output, and NB_O4_hodge_v10a29b:13-30 explicitly forbids an order-4 v10a.28 invocation. So I can confirm the machinery exists (ENGINE_O4_hodge_v10a28_orderaware_gram_firewall_a100.py:1379-1409, V28_ORDER default 4) but not that it has produced a number.
- Whether the exact size-6 rooted weight is -5/24: the printed -0.208333333333 agrees with -5/24 to 3.33e-13, which is within the 12-significant-figure print precision, but the corpus never prints an exact rational for any size row and -5/24 appears nowhere in the hodge program. Flagged as a lead, not a result.
- Whether the F07 two-face weight exists anywhere: no transcript in the corpus contains the output of v10a.21r's `_v21_size_table` (grep for "MINIMAL-SUPPORT LEDGER sizes", "nonzero clusters by size", "nonzero irreducible marked clusters by size" across records/ returns nothing). The exact per-size F07 numbers have therefore never been recorded, only the code that would produce them.

---

## 9. Lane notes

Each lane's own closing note, verbatim.

### 9.1 `citations-AB`

SCOPE: I checked every file:line pointer in artifacts A and B that maps into /home/user/WORKHOUSE — 21 distinct pointers, plus the six Monday-transcript quotation lines and the two ledger/constants ranges.

HEADLINE: the pointers themselves are unusually good. Not one points at the wrong file, and only one is off by more than a couple of lines in substance (B:143's :3897, which is a paraphrase presented as a quotation). All five v10a.21r retraction quotes are real and verbatim at the lines given; the blind per-size table is exactly where both documents say it is and every digit they reproduce is right; the firewall vectors, the four preflight gates, the two-face vacuum block, and the disconnected-spectator block are all precise citations.

The failures are of a different kind — what the cited lines are made to mean:

1. B §3's `83776 = 2⁷·7·11·17²` is simply false (2^6·7·11·17; the printed product is 2848384, 34x too big). Independently confirms the orchestrator.

2. B §5(2) / A §4 Knob B rest on a retired method. The 15-hour run states three times, in the same file whose table they target, that production coefficients come from canonical Hermitian SW/BCH through O(u^4) with "no polynomial fit/window", and that the degree-6/13-point fit is retired to a one-face audit (agreement 2.267e-07). The cited v10a.24c line ranges are real but describe the older engine. The proposed "W22-off, order-truncated" discriminator is therefore aimed at a fit the run did not use — the run's coefficients are already order-truncated at O(u^4).

3. A §3 inverts its own citation. `DATA_O4_…Preflight_CPU.py:609-610` proves W22 cannot appear in any closed order-4 layer walk, face-independently (Motzkin walks on the Krylov layer index, :124-147; the module docstring says so flatly at line 13). A cites :610 in its appendix and then asserts in §3 that the corpus proves W22-O4-nullity "only at one face" and that multi-face safety is "fit-argued, not exactly gated". The one-face-specific thing is only the 4-state exact regression at :317-338.

Findings 2 and 3 both cut the same way: they weaken A §3's "named suspect" and the §4 "two knobs", which are the documents' claimed contribution. The one-face localization itself (finding "oneface-agreement-not-new") is solid but less new than advertised — 143/8960 is already EXPECTED_GAP at firewall :43, one line below the range both documents quote.

WORTH ESCALATING beyond my lane: the exact `D_EXACT + FOLD = -11.948578179401377` disagrees with every recorded run float of the same quantity (-11.9485781794007 and variants) by 6.77e-13 = 381 ulps, which is larger than the run's own fifth_residual_max (2.53e-13) and gamma_spread (2.25e-13). B prints the exact value and claims to have "re-verified" it against two files that contain a different number; A rounds it away to -11.9486. Neither treats the divergence as a finding. src/workhouse/constants.py:428 is NOT a transcription slip — it faithfully records the run's float, and is internally consistent with RUN15_APPLIED_SHIFT_NUM at :435. The open question is which side of the 6.8e-13 the folded axial rest actually lives on, and that is a real, cheap, in-scope check someone should write.

DISCIPLINE: both documents are careful in the ways that matter most — neither promotes a side of the split, both defer the M4_SHORTCUT relabel to Alex, both mark the retirement of v10a.21r rather than mining it. The main discipline slips are B's use of the forbidden name `m₄`, and two T2 rows asserted without a tolerance (CLAUDE.md requires it in the detail line) where the true agreement is ~5e-13, not the ~1e-13 the quoted digits suggest.

One attribution point that recurs across both: the v10a.21r retirement is the AI assistant retracting its own earlier claim inside the transcript, not a maintainer ruling. The maintainer's turns at Monday 531 PM.txt:1977 and :3891 are the prompts that provoked it. Both documents call it the maintainer's, which upgrades its authority in exactly the way CLAUDE.md's opening principle warns against.

### 9.2 `citations-CD`

SCOPE: every corpus citation in C and D that maps into /home/user/WORKHOUSE, plus the SHA-256 and manifest questions. All work read-only; scratch under the session scratchpad.

PATH TABLE (deduplicated by file):

IN-REPO, cited by C — all EXIST: src/workhouse/constants.py (:203-214, :426-435); src/workhouse/invariants.py (:414-422 — range wrong, see finding); docs/decisions/0002-anchoring-is-not-a-dispute.md (:50-57); corpus-import/programs/hodge_o4_adjudication/src/ENGINE_O4_hodge_v10a24c_...py (:7309, :7310, :7314-7320, :7322-7326, :7325-7326, :7335-7336); corpus-import/programs/hodge_o4_adjudication/src/ENGINE_O4_hodge_v10a7_marked_linked_scalar.py (+SHA, 9 ranges); corpus-import/records/audits/07-denominator-lift.md (:69-78). Plus three files reached indirectly through C's hash table, all present with matching hashes.

IN-REPO, cited by D — all EXIST: corpus-import/records/transcripts/15 hour RUN.txt (4 ranges); ENGINE_O4_hodge_v10a24c_...py (9 ranges); corpus-import/records/audits/{02,03,05,06}; corpus-import/programs/hodge_o4_adjudication/README.md (:27-45); ledger/contradictions.yaml (4 ranges); src/workhouse/constants.py (:426-435, :649-655).

EXTERNAL, not present: work/rank3_order4_cubic_ledger/* (5 files, ~30 citations), work/rank3_order4_exact_haar_run/*, work/rank3_order4_exact_haar_package_verify/* (8 citations), work/fold_linked_exact/README.md (4 citations). Detailed in the unverifiable list. Certificate artifact E supplies one same-named file (rank3_order4_exact_haar_summary.json) and nothing else from these paths.

MANIFEST ANSWER: theory/SHA256SUMS pins none of these (13 entries, all theory/). corpus-import/SHA256SUMS pins every in-repo file cited by either document; I recomputed three of them (v10a7 engine, v10a24c engine, 15 hour RUN.txt) and all three match their pinned values.

OVERALL SHAPE. The citation hygiene in both documents is unusually good — I checked roughly forty in-repo line ranges and only one (C's invariants.py:414-422) is wrong. The failures are not citation failures; they are inference failures on top of accurate citations.

C is the stronger document. Its central negative claim — that local_shift did not create -11.0685, and that the v10a.20b dataflow puts the prior target strictly after the exact accumulation — is verified line by line and is correct. Its SHA-256 assertion is right and independently pinned. Its weaknesses are all one kind: it treats "exact" as a property that survives being copied. The route it nominates as the earliest lineage computes in float64 and prints via limit_denominator; the fold addend it calls exact is, in the default configuration, an identity on three hard-coded literals; and its frozen hash chain is the one part of the document that could have been checked against the delivered certificate, and the one row that can be checked does not match.

D is weaker where it is most confident. Its section 2 is the load-bearing structural argument, and its premise is stale by two engine versions: the numbers it adjudicates come from v10a.26, which retired the polynomial fit that D makes the basis of its objection. Worse, the exact W22-off comparison D calls "required" already exists in this repository, passes, and is pinned by the very package D is auditing — I ran it: o4_equal True, first difference exactly -5/7168 at O(u^5). D's W22 observation itself is correct and survives (the dense matrix is unmasked in both engines), but the corpus already records it more sharply at 05-latest-run-forensics.md:96, which D did not cite.

A useful by-product: D's section 1 is right, and more strongly right than D argues. Using only in-repo material — the exact Fraction preflight I executed plus the gated vacuum coefficients e2=-3/4, e3=-9/32, e4=-39/1280 — the entire blind size-1 row reconstructs: c2 = 1/2, c3 = 7/32 = 0.21875, c4 = 143/8960 -> 0.0159598214286, matching all three printed strings at 15 hour RUN.txt:10620. D sourced both of its one-face constants to files nobody here can open, when both are gated and PASSED in this repo. That reconstruction is T1-grade and would be worth registering as an invariant.

One thing neither document notices and I could not fit elsewhere: the two branches' shared pre-subtraction intermediate does not agree exactly. The exact D_EXACT + FOLD = -11.948578179401377, while the folded-axial route printed -11.9485781794007 — 381 ulps apart, with the run's own two internal routes to that same object 1.8e-14 apart from each other. The repo records the float at constants.py:428 with no docstring and no invariant reading it.

On the governing rules: neither document edits theory/, promotes C_shp, applies a 4**r rescaling, or writes "two m_4 values" — D explicitly preserves the q_band/m_Gamma anchoring distinction. D's proposed relabel of the quarantined scalar keeps it unpromoted, so it does not breach non-negotiable 2, but the label it wants dropped traces to a 5x heuristic sitting 1.17% from flipping, and to a tier-2 invariant at invariants.py:397-400 that would have to move with it.

### 9.3 `arithmetic`

SCOPE. I re-derived every rational, decimal, factorization, difference and count in A, B, C and D from scratch in python3 (fractions.Fraction, sympy.factorint, decimal.Decimal at 50 digits) without using the orchestrator's list, and I replayed the certificate's full 69,800-record ledger in exact arithmetic. Scratch scripts are at /tmp/claude-0/-home-user-WORKHOUSE/384fab32-8991-52ce-b2bf-4999d379e3f5/scratchpad/work/r1.py through r5.py. No file in /home/user/WORKHOUSE was modified.

HEADLINE. The exact arithmetic in these documents is, with one exception, impeccable. Every rational identity checks: the one-face gap, the two-face vacuum, the V_link decomposition (which I strengthened — it is uniquely 13 single embeddings + 124 pairs), D_EXACT, the fold, the QBOUND lift, and the final -160506019419340168451/14501180577204921600. I independently reproduced D_EXACT from the raw 69,800 weighted contributions rather than accepting it, and it lands exactly. The single exact-arithmetic error is B §3's factorization of 83776.

The real defects are not arithmetic. They are three: (1) a stale attribution — the "degree-6 fit on 13 points" that A §4 makes the whole discriminator belongs to v10a.24c, while the numbers being adjudicated come from v10a.26, which retired the fit for exact Hermitian SW/BCH; (2) precision language — "agree exactly at one face" and "Σ per-size c4 = oracle -0.7751458630189" both assert exactness that the printed float data cannot carry (2.9e-14 and 4.7e-13 respectively); (3) a provenance gap — the certificate that ships with C contains no binding from its Haar ledger back to any frozen W2/R2 history, so the arithmetic is certified and the inputs are not.

TWO CORRECTIONS TO THE ORCHESTRATOR'S PRE-ESTABLISHED LIST (I re-derived rather than trusting, per instructions):
- "RAW_FOLDED_AXIAL_GAMMA_NUM = -11.9485781794007 (6.8e-13 = ~255 ulps low)". The gap is right but the ulp count is wrong: ulp(11.948) = 2^-49 = 1.7763568394002505e-15, and 6.767920e-13 / that = 381 ulps, not 255. (Against the exact value the repo constant is 381 ulps; the run's implied ax_rest is 383; B's printed value is 13.)
- "the blind per-size table sums (in printed order) to -0.77514586301840004978, which equals 8*HAMER_A4_NUM to the last float bit". That is the sum of only *four* rows — it silently adopts B §2's zeroing of sizes 4 and 5. The six rows the transcript actually prints sum to -0.7751458630184424382751163, which is 382 ulps from 8*HAMER_A4_NUM, not bit-identical. Both variants are within the ±1.55e-12 print envelope, so the T2 claim survives either way, but the "to the last float bit" coincidence is an artifact of the zeroing, not a property of the data.

ON THE T2 HONESTY QUESTION (asked explicitly). `blind_table_sums_to_oracle` is honest as a T2 claim, but only at tolerance ≥ 5.2e-13 — and the honest tolerance to *quote* is 1.6e-12, the worst-case propagated rounding envelope of the printed table (rows given to 1e-12, one to 1e-13). It is not honest at any tolerance tighter than ~5e-13, and A §2's 13-significant-digit phrasing of it is false in the last two digits. This is the same 5.2e-13 the repository already records at ledger/contradictions.yaml:51-52 and ADR 0002:53, so nothing new is being asked of the corpus — but A quotes it as an equality where the ledger quotes it as an agreement.

ON 14501180577204921600 = 2 × 7250590288602460800 (asked explicitly). True, and the factor of two is structural rather than coincidental: the two denominators are identical except 2^8 vs 2^7, and the extra 2 is exactly the 1/2 in D_EXACT = D11 + (1/2)·Σ w·H. The V_link denominator 1675520 = 2^8·5·7·11·17 divides in cleanly (its 2^8, 5, 7, 11, 17 are all already present in 14501180577204921600 = 2^8·3^6·5^2·7·11·13·17^3·19·29·31·37), and 140454 = 2·3^5·17^2 adds nothing new. Indeed lcm(7250590288602460800, 140454, 1675520) = 14501180577204921600 exactly — the final denominator is forced by the three addends, not chosen. That is a mildly reassuring structural fact none of the four documents states.

WHAT I WOULD DO NEXT, IF THE LANE ALLOWED WRITES. The v10a.26-vs-v10a.24c misattribution is the one finding that changes a research conclusion rather than a digit, and it is cheap to settle definitively: the transcript embeds its own source, so someone can diff the v10a.26 cluster-coefficient path against v10a.24c's and confirm whether the per-size c4 table at :10620-10626 came through _v26_sw_blocks. If it did — and :7121-7124, :7230-7246 and :10617 all say it did — then A §4's Knob B is testing a hypothesis the corpus already closed, and the two-face discriminator needs re-specifying around something other than fit contamination. That is the highest-value next operation in this lane.

### 9.4 `certificate`

SCOPE: package E audited on its own terms, read-only. Nothing in /home/user/WORKHOUSE was modified. All work under /tmp/claude-0/-home-user-WORKHOUSE/384fab32-8991-52ce-b2bf-4999d379e3f5/scratchpad/{run1,run2,pylibs}.

WHAT E ACTUALLY IS, in WORKHOUSE tiers. E is a T1 certificate of one arithmetic step: given the 69,800 (topology, weight) pairs in root_exact_pair_topologies.pkl.gz, the exact SU(3) Haar contraction, the weighted sum, and D_EXACT = -13/896 + sum/2 are correct, exactly, with no floats, and are confirmed by a genuinely distinct second implementation on all 69,800 records. Everything on either side of that step is T3: the weights and the topology census are supplied inputs, and F, V_linked and D11 are supplied constants. The final scalar -11.068479463778765 is T1-from-T3-inputs — the addition is exact, the addends are asserted.

THE HEADLINE TENSION. The package's three reports are, on the mathematics, honest and — where I could test them — correct. Every number they quote that I could recompute, recomputed. The problems are all about what is in the box versus what the box says is in it. Three of four validators cannot run; the primary generator cannot run; the one all-record independence claim has no shipped artifact; the entry-point pickle has no cryptographic tie to anything upstream; and the field in it literally named source_history_sha256 contains counts rather than a hash. A reviewer who does exactly what the package invites — unzip, `sha256sum -c`, run the scripts — gets 20/20 checksums and then three ImportErrors, and would reasonably conclude the certificate is broken. It is not broken; it is under-packed. The fix is small and specific: ship rank3_order4_cubic_ledger/ledger_generator.py, restore the two module names the importers expect (exact_su3_projector.py, modular_su3_projector.py), pin numpy, flatten or document the WORK=HERE.parent layout, and include independent_modular_crt_exact_haar_numerators.json.gz.

WHAT I ADDED THAT THE PACKAGE DID NOT SHIP. I reconstructed the missing environment and ran the whole route: the primary contractor regenerates the ledger byte-identically; the algorithmically independent modular/CRT contractor agrees with it on all 69,800 records with zero mismatches; and a third route (the delta/DSU projector) agrees on a seeded 20-record sample deliberately weighted to the zero-Haar stratum the shipped certificates barely touch. So the arithmetic content of E is stronger than E's own evidence package demonstrates. That is worth saying plainly, because the packaging faults would otherwise be read as substantive ones.

TWO THINGS I WOULD NOT LET PASS INTO A WRITE-UP. First, the shipped summary.json is not the byte output of the shipped contractor — five LF lines in a CRLF file, out of the code's own sort order, and they are exactly the QBOUND gate block that both reports headline. The values are right; the provenance is not clean, and in a repo whose one rule is that only a machine check is authority, an artifact that was hand-touched after the run is a provenance event, not a formatting one. Second, one of the two headline exactness gates is a tautology: given d | Q, Fraction(n*(Q//d), Q) == n/d always. It should be dropped from the gate list rather than counted as evidence.

DOCUMENT C VERSUS PACKAGE E. They are different artifacts. Zero of C's eight tabulated hashes appear in E; C's chain is the exact_haar_sum.py route, E's is the modular_haar_contractor.py route; C says the summary binds a history hash and a contractor hash, and E's summary binds neither. If C and E are cited side by side as one provenance chain, that is a category error — they are two independent routes to the same D_EXACT, which is good news for the number and bad news for anyone trying to follow one hash chain through both.

AND THE THING THE PACKAGE DOES NOT SAY. The scalar E certifies is the one WORKHOUSE records as QUARANTINED_SCALAR, status rejected-by-both, claim status falsified. E's own caveats are about physical completeness of the generator, not about that standing. C discloses the quarantine; E, read alone, does not. Certifying the arithmetic of a quarantined value is legitimate and useful work — it removes the numerical-rationalization objection — but it must not be reported as if it moved the value's status, and nothing here does move it.

HIGHEST-VALUE NEXT OPERATION: ask the collaborator for ledger_generator.py and the W2/R2 history ledger (543869b1...). With those, the chain primitives -> history -> pickle -> D_EXACT becomes checkable here end to end, and the one genuinely load-bearing unverifiable — that the 69,800 weights are the right weights — becomes testable. Everything downstream of the pickle is already settled.

### 9.5 `ledger-graph`

Answers in the order asked.

(1) No slot, and the register cannot grow one. tests/test_ledger.py:20 pins the contradiction ids to exactly C1..C22 with the docstring "C1-C22 is closed ... which cannot grow"; :28 pins the open set to exactly {C2}; :131 requires every open C to have a governing-register counterpart, and :77-95 / :108-120 make that counterpart un-inventable because the R-register is a verbatim transcription of the governing document. Meanwhile the PAIR is already registered — ledger/contradictions.yaml:32-40 prints -0.7751458630189173 and -11.068479463778765 side by side inside C1 — so a new entry duplicates. And "sub-entry of C2" is a category error: C2's own crosswalk (Phi_C(0)=0) proves a Gamma-point scalar constrains nothing C2 is about. What genuinely EXTENDS the register is the content, not the slot: the one-face agreement 143/8960 and the size>=2 localization appear nowhere in ledger/, src/workhouse/, index/, CERTIFIED.md or FRONTIER.md. Correct home: G3's unpinned `audit_findings`, plus a ledger/symbols.yaml entry if it is to be graph-visible at all — C1's quantity block emits no edges, verified via `workhouse why C1`.

(2) The evidence axis moves; the status axis does not. record-backed -> at most output-certified, and only once the external package lands under a pinned path here. `falsified` stays until some side accepts the value as the physical coefficient, which D §7 explicitly declines to claim. The proposed replacement string is not a value on either axis; it is a `note`. And yes, arithmetic_status / physical_status / quarantine_reason introduce a fourth vocabulary — worse, they rename the two axes that already exist plus the `note` field, which is AGENTS.md's own "re-derived under different notation" failure applied to the taxonomy itself.

(3) The validator accepts all of it. Simulated the full proposal against the real loader on scratch copies: three new fields on C1 quantities[2] plus a fully-routed open C23 -> ledger.validate returned [] (CLEAN), so `make status` reports nothing. src/workhouse/ledger.py:130-227 enumerates no permitted keys; it is a cross-reference checker, not a schema. Four pytest assertions catch it instead. Anyone recommending a ledger change here should name `make check`, not `make status`.

(4) A violation, but a cheap one to fix. Not of C1's forbidden PAIR — that names q_band^(4) vs m_Gamma^(4), and -11.0685 is a third quantity C1 records separately. It is a violation of ledger/symbols.yaml:53-55, which bans `m_4` for m_gamma_4 unconditionally: D line 24 writes exactly m_{4,blind} = -0.7751458630189173, and B line 3 writes "Gamma-point axial rest coefficient (m_4)". The deeper problem is B §0's "branches of the *same* physical quantity", which asserts what D §7 says is unproved and is the mechanism ADR 0002:28 blames for manufacturing C1. Renaming to m_F07^(4) vs m_Gamma^(4), and downgrading "same physical quantity" to "two candidate constructions of one coefficient, identification open", costs nothing and removes both objections.

(5) Knob B is a strict subset of protocol item 10 (size-2 classes out of all 33), on a different code path (v10a24c's fit route, not the marked-cluster harness item 10 governs), and it omits the recorded blocker that no engine exposes the toggle. Knob A (an exact rooted two-face F07 weight) IS new — nothing in the 11-item protocol asks for a rooted decomposition of the F07 trace-history formula.

(6) Half new, half restatement. "Localized to size >= 2" is new. "The decisive test is the W22-off two-face recomputation" restates item 10 plus audit_findings bullet 3. "Decisive" is also wrong relative to G3's stated scope. Mechanically it must NOT go in `protocol` (11-item freeze; simulation gave len=12 -> FAIL while validate stayed CLEAN) and requires `make frontier` afterwards.

One reconciliation for the orchestrator. I get a different number than the brief's premise on the blind-table sum. Summing the six printed c4 values in printed order gives -0.77514586301844246030 (exact decimal -0.7751458630184424382751163). 8*HAMER_A4_NUM = 8*(-0.0968932328773) = -0.77514586301840004978. Those are NOT bit-equal: they differ by 4.24e-14, which is the trailing-digit noise of the 12-significant-figure printed rows. The sum differs from M_GAMMA_4_NUM = -0.7751458630189173 by 4.748e-13, and |8*a_4 - m_Gamma^(4)| = 5.1725e-13. Honest statement: the row sum agrees with Hamer's 8*a_4 to 13 decimal places and with the printed TOTAL only to ~4.7e-13. Bearing on this lane: B §6 check #5 ("blind_table_sums_to_oracle", T2) would need a tolerance around 5e-13 — the same order as the existing HAMER_TOLERANCE = 5.3e-13 (constants.py:264) used by src/workhouse/invariants.py:388-394 ("Hamer 8*a_4 matches m_Gamma to ~5.2e-13"). It is arithmetically the same statement as a check the repo already has, routed through the per-size table, and should not be presented as an independent row of a "certified spine".

All work was read-only; the only writes were scratch copies of the three ledger YAMLs under /tmp/claude-0/-home-user-WORKHOUSE/384fab32-8991-52ce-b2bf-4999d379e3f5/scratchpad/lsim/ledger/.

### 9.6 `invariants-tests`

LANE ANSWER — mapping the documents' proposed checks onto what WORKHOUSE already checks.

== 1a. The 13 checks in "fourth order, anchoring and the residual dispute" ==
All at src/workhouse/invariants.py, suite declared at :294. All PASS. Tier composition: 2 x T1, 11 x T2.

 1. :297 T2  historical q_3 decimal expansion — "|diff| = 0.00e+00"
 2. :303 T1  C_old = (beta_pen_3 - 2*alpha_3)/16 — "= -211835444920651/4405310420659200"
 3. :309 T2  Delta_Gamma = m_Gamma^(4) - q_band^(4) — "double eval 2.0827701250956414; exact rounds to 2.082770125095642"
 4. :318 T2  FINDING: the printed Delta_Gamma is one ulp low — "certified: true Delta_Gamma = [2.0827701250956416755 +/- 2.68e-20]; the corpus's printed 2.0827701250956414 lies provably below it… gap 4.441e-16 = 1 ulp"
 5. :340 T1  a translation-local scalar shift changes nothing observable — "centered operator, eigenvectors, SOS factorization, mobility coefficients and bandwidth are all invariant under the anchoring shift, so q_band^(4) and m_Gamma^(4) are not competing estimates"
 6. :358 T2  Delta_C = C_new - C_old > 0 (the real discrepancy) — "0.027873054295192174 vs recorded 0.027873054295192174 (|diff| 0.0e+00)"
 7. :369 T2  beta_new = 8A + 16*C_new — "= 0.5099200711546681"
 8. :375 T2  off-axis band splits are 8*Delta_C and 16*Delta_C — "M: 0.2229844343615374, R: 0.4459688687230748; axial cuts agree exactly"
 9. :382 T2  bandwidth ratio W4_new / W4_old ~ 1.93 — "= 1.927907"
10. :388 T2  Hamer 8*a_4 matches m_Gamma to ~5.2e-13 — "|diff| = 5.17e-13; a_4 is an unverified notebook transcription, so this is a normalization cross-check, not primary-source proof"
11. :397 T2  quarantined scalar decimal — "|diff| = 0.00e+00; rejected by both sides"
12. :403 T2  C20: exact gate value vs printed float-reconstruction — "exact -0.8800987156226127 vs artifact -0.8800987156226097; gap 3.00e-15 = 31 ulps. They agree to ~14 significant digits, NOT to float precision as C20 states; the corpus's printed decimal tracks the artifact."
13. :421 T2  run's applied shift is not Delta_Gamma — "applied 11.17343231638178 vs Delta_Gamma 2.082770125095642 — target-derived, so gate 85 is not an independent scalar verification"

Note for the artifacts: check 12 IS the V_link number they call "-V_link = +0.880098715622613" (B §1). The repo already holds a FINDING that the two recorded forms of it differ by 31 ulps and that the corpus's printed decimal tracks the wrong one. Neither A nor B mentions C20's 31-ulp finding while quoting the C20-affected decimal.

== 1b. Coverage of the 8 proposed rows ==
"The 8" = A §2's table (B §6 tabulates only 6 — see finding eight-checks-vs-six).

ALREADY COVERED (do not re-add):
- A row 6 / B #5  blind table closes  ==>  DUPLICATE of :388 'Hamer 8*a_4 matches m_Gamma to ~5.2e-13'. Same numbers, same tolerance. See finding blind-table-check-duplicates-hamer.
- A row 7  F07 anchoring-invariant  ==>  DUPLICATE of :340 (T1) + :421 (T2, C22 half).
- B #6's "Gate-85 / anchoring is target-derived" component  ==>  DUPLICATE of :421 and of ledger C22 (resolved).
- The F07 scalar itself (-11.068479463778765) ==> already asserted by :397 and registered at constants.py:427.
- V_link = -1474623/1675520 ==> already constants.py:430 and gated by :403.
- A §3/§4's W22 "named suspect"/"decisive test" ==> already adjudication protocol item 10, hardcoded OPEN, with a passing FINDING at :665-678 and ledger/gaps.yaml:127-131.

GENUINELY NEW to the check layer (all would be T3 -> T1/T2 promotions, none is a new mathematical result — every one of them is already an exact constant or a PASS gate somewhere in corpus-import):
- A row 1 / B #1  -13/896 + 39/1280 = 143/8960. Zero occurrences of 143/8960, -13/896 or 39/1280 anywhere in src/ tests/ ledger/ theory/ index/ lean/. In the corpus: 143/8960 x6 (incl. ENGINE_O4_hodge_rootonly_firewall_v1.py:43 as EXPECTED_GAP), -13/896 x79, -39/1280 x43.
- A row 2 / B #2  143/8960 == blind size-1 c4. New; needs tolerance >= 2.86e-14 (float(143/8960)=0.015959821428571427 vs printed 0.0159598214286).
- A row 3  W22 exactly O4-null at one face; first bite O5 = -5/7168. New; -5/7168 has 2 corpus occurrences only.
- A row 4 / B #3  e4(C) = -54321/837760, omega4 = -327/83776. New; see finding twoface-vacuum-has-no-current-theory-anchor. (B §3's prose factorization "83776 = 2^7*7*11*17^2" is wrong — that product is 2848384; 83776 = 2^6*7*11*17.)
- A row 5 / B #4  1675520 = 1280*1309 = 83776*20. True; the value is in constants.py:430 but the factorization is unchecked. Trivial integer arithmetic — note that the substantive claim in B §3 ("V_link = V1*(single embeddings) + VPAIR*(pairs)") is NOT what the proposed check asserts.
- B #6  the -0.403971702978 pin + the v10a.21r provenance guard. New; 0.403971702978 appears nowhere in the check layer.
- A row 8  F07 oracle-free. Not a check (tier "—") and its posture conflicts with two passing repo FINDINGs.

== 1c. Targeted greps (check layer = src tests ledger theory index lean docs settlement literature notes runs scripts CERTIFIED.md FRONTIER.md README.md) ==
- 143/8960 : 0 hits in check layer. Corpus: Monday 531 PM.txt:9702; ENGINE_O4_hodge_rootonly_firewall_v1.py:43; corpus index 6 occurrences.
- 8960     : no relevant hit in check layer (only unrelated digest/CSV substrings).
- 83776    : check layer only theory/superseded/MASTER_THEORY.md:568. Corpus index: 61 occurrences of -327/83776.
- 54321    : check layer only theory/superseded/MASTER_THEORY.md:568. Corpus index: 63 occurrences of -54321/837760.
- 1675520  : constants.py:430; tests/test_corpus_registry.py:32; ledger/contradictions.yaml:248; index/claims.jsonl:201; theory/superseded/MASTER_THEORY.md:416,568,654.
- 1474623  : same set as 1675520.
- 7168     : ZERO relevant hits — every "71680" hit is Rational(47641149,71680) etc. in the Münster/Smit series, a different number. -5/7168 lives only in corpus-import (DATA_O4_OrderSchedule_Occurrence_Preflight_CPU.py:616, ENGINE_O4_test_hodge_orderschedule_occurrence_preflight_cpu.py:22).

== 2. Verify counts ==
`make verify` -> 140/140 checks passed.  `workhouse verify` -> 140/140.  `workhouse verify --tier 1` -> 111/111.  `workhouse verify --tier 2` -> 29/29.  Read-only throughout; no repo file touched. (`python -m workhouse verify` fails — no workhouse.__main__; use the console script at .venv/bin/workhouse.)

== 3. why / search results ==
- why C2  : open contradiction, both sides recorded, neither promoted; routed to G3; cited by 3 passing checks.
- why C1  : RESOLVED, "an anchoring distinction"; cited by :309 and :340 and by a published-comparison check.
- why C22 : RESOLVED, "Not a numerical contradiction but a status correction: the final diagonal shift was chosen to produce exactly that equality, so gate 85 certifies internal bookkeeping, not independent agreement." Cited by :421. B §7's "C22 (Gate-85) is unchanged and correctly resolved" is accurate.
- search -11.068479463778765 : 2 claims (CONST:QUARANTINED_SCALAR; CONST:quarantined scalar, status falsified/record-backed, cites MASTER_THEORY §5.5). ALREADY KNOWN.
- search 143/8960          : "no claim matches". Also no corpus occurrences shown — but that display is a bug (see finding search-corpus-suppresses-occurrences); the corpus index actually holds 6.
- search -327/83776        : argparse usage error without `--`; with `--corpus --` it prints "no claim matches" while the index holds 61 occurrences.
- search 10.293333600759848: no claim, and genuinely no corpus occurrence.
- search -0.403971702978   : no claim, and genuinely no corpus occurrence (the transcript prints it, but with a "c4=" prefix the rational index does not capture).
- search -0.775145863018 (control): resolves to the m_Gamma^(4) symbol card with the "never call it m_4" warning and 11 claims. So the front door works when the catalogue has an entry — the failure is specifically the corpus-only case.

== 4. invariants.py 414-422, quoted verbatim ==
414:        not agree_to_float,
415:        f"exact {exact!r} vs artifact {artifact!r}; gap {gap:.2e} = {gap / ulp:.0f} ulps. "
416:        f"They agree to ~14 significant digits, NOT to float precision as C20 states; "
417:        f"the corpus's printed decimal tracks the artifact.",
418:    )
419:
420:
421: @dispute.check("run's applied shift is not Delta_Gamma", "GLUEBALL §9.2 / C22", tier=2)
422: def _():

That range straddles two checks: the tail of C20 (:403-418) and the head of Gate-85 (:421-429). YES — the Gate-85 check states target-derivation explicitly, at :423-424 (comment) and :427-428 (detail line). NO invariant asserts the 10.293... gap. YES — the F07 value is asserted, by :397-400 'quarantined scalar decimal'.

== 5. If the proposed suite were added, the duplicates would be, precisely ==
(a) B #5 `blind_table_sums_to_oracle` duplicates `Hamer 8*a_4 matches m_Gamma to ~5.2e-13` (invariants.py:388, T2, GLUEBALL §2.3). Not a near-duplicate: the row sum is bit-identical to 8*HAMER_A4_NUM and needs the same 5.3e-13 tolerance.
(b) A §2 row 7 `F07 anchoring-invariant` duplicates `a translation-local scalar shift changes nothing observable` (invariants.py:340, T1) — and is itself already duplicated a third time as tests/test_constants.py:36-42.
(c) The Gate-85/target-derivation half of B #6 duplicates `run's applied shift is not Delta_Gamma` (invariants.py:421, T2).
(d) Any check re-pinning the F07 decimal duplicates `quarantined scalar decimal` (invariants.py:397, T2).
(e) B #4's V_link value duplicates constants.py:430 + `C20: exact gate value vs printed float-reconstruction` (invariants.py:403); only the integer factorization is additive.
Non-duplicates: B #1, B #2, B #3, A row 3, and the -0.403971702978 pin + provenance guard in B #6.
Caveat repeated: the script was not uploaded. This mapping is against the tables in A §2 and B §6, not against code.

== Recommended landing order (highest verification value first) ==
1. Fix src/workhouse/search.py:219-225 so --corpus occurrences print when the catalogue misses. It is a front-door false negative on exactly this dispute's rationals, and the docstring at :162-169 already says why that matters.
2. Add ONE T1 check: QUARANTINED_SCALAR + LINKED_VACUUM_4 == -86634244910174898583/7250590288602460800, and a FINDING that RAW_FOLDED_AXIAL_GAMMA_NUM is 6.768e-13 (381 ulps by math.ulp) below it. Two constants already registered, currently joined by nothing; RAW_FOLDED_AXIAL_GAMMA_NUM is read by no check at all today.
3. Add B #1/#2/#3 and A row 3 as T1/T2, each citing the corpus gate line rather than the artifact.
4. Do NOT add B #5 or A row 7. Extend the detail line of invariants.py:388 instead, to record that the blind per-size table sums to 8*a_4 and not to the printed oracle total — that is the one genuinely new fact inside the proposed check.
5. Leave C2/G3 untouched. Nothing here promotes either branch.

### 9.7 `hamer-circularity`

VERDICT ON THE LANE: (a) genuine external validation for a_4, with one real and narrower circularity that should be recorded, plus one provenance gap that keeps the whole thing one step short of machine-checked.

THE SEED FACT IS WRONG, AND CORRECTING IT MATTERS. The printed six-row table does not sum bit-for-bit to 8*a_4; it is 382 ulps away. The bit-exact identity needs the two numerical-zero rows dropped. Priced properly, even the 4-row coincidence is unremarkable: S4 = sum of four values rounded to 12 significant figures, so its rounding error is a sum of four uniforms with half-widths 5e-14, 5e-13, 5e-13, 5e-13 → sigma = 5.08e-13. S4 lands on a 1e-13 lattice; 8*a_4 lands on an 8e-13 lattice near the same true value. P(S4 hits that exact lattice point) ~ 1e-13 / (sigma*sqrt(2pi)) = 1e-13/1.274e-12 ~ 7.9%, i.e. about 1 in 13. Not a signal.

THE COINCIDENCE THAT IS REAL IS THE ONE IN THE OTHER DIRECTION, AND IT EXONERATES. The number that needs explaining is not the sum, it is a_4 itself: 12 significant figures written down BEFORE the run finished, landing 6.47e-14 from m_4/8. Price that under the confabulation hypothesis. Grant the guesser eight correct significant figures for free — which the transcript shows they did not have, their stated expectation was -11.06848 — and P ~ 2*6.47e-14/1e-9 ~ 1.3e-4. Grant only the order of magnitude and P ~ 2*6.47e-14/0.05 ~ 2.6e-12. a_4 encodes roughly eleven correct significant digits of a quantity that did not exist anywhere in the corpus at the time it was written. It did not come from this program. Whether it came from Hamer's page or from a model's recall of Hamer's page, it is external either way — which is what C1 claims.

WHAT SHOULD ACTUALLY CHANGE. The circularity is real but narrow and lives entirely in the a_2/a_3 edges, not in a_4. Four "corroborations" are marked `verified` in literature/index.yaml and FRONTIER.md, and all four are exact round-trips of rationals the program already held — with the transcript itself, at Monday 531 PM.txt:7205, recording that those rationals were loaded at the moment the table was produced. They should be demoted from independent corroboration to consistency-with-the-primary-read, because that is all they can be. The a_4 edge is the only one that carries information, and the reason is precisely that it is the only one that does NOT round-trip: round12(m_4/8) = ...774, the registry holds ...773. That asymmetry is the strongest single piece of evidence in the file and it is written down nowhere.

ON THE TOLERANCE, WITH THE CLAUDE.md RULE IN MIND. HAMER_TOLERANCE = 5.3e-13 is 2.5% above the observed 5.173e-13, and the observed gap is 1.293x the paper's own printed-precision bound of 4.0e-13. That looks like tolerance-fitting, and by the letter of "never widen a tolerance to make a finding disappear" it is close to the line. But the finding it would otherwise expose is not a discrepancy — it is the run's own float error, and the run measures that error itself against known exact values: relative 5.887e-13 on A = 5/48 and 5.839e-13 on alpha = 5/12, against 6.673e-13 relative for the m_4 gap. Same size. So the physics is fine and the bookkeeping is not: the bound should be stated as print (4.0e-13) + run (~4.6e-13) ~ 8.6e-13 with those measured numbers in the detail line, the way the n=2 and n=3 checks already do. That change strengthens the claim rather than weakening it, and it removes the appearance of a fitted number.

ONE THING WORTH SAYING PLAINLY. Hamer's a_4 is more accurate than this program's m_4. Under the reading that the paper is right, the program's fourth-order float is ~5e-13 low, consistent with its own demonstrated error budget. Treating the 5.2e-13 as "the gap between us and Hamer" is the wrong frame; it is the program's error bar, and Hamer is inside it.

SCOPE NOTE ON ARTIFACT D (outside my lane, flagged for whoever has it): D line 142 and line 203 call the Hamer agreement "conditional on the unproved normalization bridge", citing 05-latest-run-forensics.md:60. The citation is to an audit dated 2026-08-19 whose scope is the v10a.25 notebooks, not the v10a.26 run that produced the blind value; the specific item cited (normalization) is generic enough that the caveat survives, and it is substantively correct — invariants.py:1366 proves the bridge GIVEN x = 2u but does not establish that the program's u is Hamer's x/2. D should say which run it is talking about, since the same audit's item 1 (blindness claim false) applies to v10a.25 and emphatically does not apply to v10a.26.

### 9.8 `localization-argument`

LANE VERDICT, in one line: the localization argument reaches a conclusion that is probably right at one face, by an exact cancellation the documents neither state nor cite, and gives no support whatever for the step from "agree at one face" to "the gap is purely multi-face accounting" — while the mechanism it names for the gap (W22 fit contamination) is refuted by the very run whose table it uses.

Axis 1 (THE FOLD — the most important question). Answer: the fold is NOT a single global scalar. It is FOLD_A = -2*C_A - E2_A*N_A + J_A (v10a6:798), the Rayleigh-Schrodinger renormalisation term, and E2_A/N_A/J_A are each Gamma-point sums over a 13-face neighbourhood (v10a6:668-670). The -E2_A*N_A piece is BILINEAR in face-sums, so it does not decompose into a sum over faces at all without a convention; the corpus's only convention is _v21_union_convolution (v10a21r:122-127, 331-338), which sends E2[S]*N[T] to S∪T. Under that convention the fold's singleton entry is E2[{R}]*N[{R}] and, using the isolated one-face RS moments I computed exactly from the corpus's own module, the singleton fold is exactly 0 — so the documents' 143/8960 survives. But: (i) they never say so, never cite it, and never give FOLD a value; (ii) the zero is a rank-1 C-parity accident (one intermediate channel, N=e2^2, J=e2^3) that fails at the vacuum face (27/128) and has no reason to survive at two faces, where several energy denominators exist; (iii) 100% of FOLD = +37.8416 — 3.68x the gap being localized — sits in the size>=2 sector, with +34.97 to +38.15 of it at size 3 alone, and the union convolution puts a product of two two-face objects on a THREE-face support, which in linked-cluster language is an unlinked contribution. So the F07 per-size profile is a difference of large cancelling numbers, not a linked-cluster decomposition, and comparing its "size 2" to the blind "size 2" is not comparing like with like.

Axis 3 (WHAT ELSE WOULD HAVE TO BE TRUE). Six things, none established: (1) a bijection between F07 supports and blind rooted clusters — D §4 says explicitly there is none; (2) each total is the sum of its per-index terms with no unassigned residue — true for the blind branch by construction, unknown for F07; (3) "size" means the same thing on both sides — false for the fold, whose 3-face support carries a product of 2-face objects; (4) the fold's singleton part is zero — true, but unstated and fragile; (5) the vacuum is assigned to the same size classes on both sides — F07/v10a21r attaches V1 to {ROOT,f} for all 13 f (including f=ROOT), while the blind branch subtracts the vacuum inside each cluster gap; these coincide only at size 1; (6) no normalization that happens to be 1 at size 1 — but F07 fixes polarization_index=2 while the blind run uses one default polarization and the canonical calculation needs all three (D §2, D §4, D §9 item 4), a multiplicity mismatch that would be invisible at a polarization-degenerate size-1 cluster.

Axis 4 (IS 10.293 INFORMATIVE). The identity holds and I quantified it: local_shift + V_link = 10.293333600759167 versus the printed 10.293333600759848, residual 6.803e-13 = exactly the 381-ulp ax_rest float. So 10.293 is not a third datum. But it does not dissolve the conflict the way ADR 0002 dissolved C1, because both branches claim to be the vacuum-subtracted linked Gamma rest — the documents are right about the dataflow ("rivals, not input/output") and wrong to treat "same physical quantity" as settled, since D §7 lists precisely the missing equivalence certificate. The useful reframing the documents miss: the gap is a disagreement about the SIZE of the vacuum/linkage subtraction applied to a shared raw folded axial rest — 11.1734 versus 0.8801, a factor of 12.7 — not about multi-face axial accounting.

Axis 5 (W22). The documents have it backwards. The corpus's W22-at-O4 exclusion is a support-independent Motzkin layer-walk theorem (DATA_O4...:609-610); it is the one-face statement (:614,:616) that is the special case. And the "fit" the whole suspect rests on is not the method that produced the numbers: 15 hour RUN.txt is a v10a.26 run whose production coefficients come from order-truncated Hermitian SW/BCH, with the 13-point degree-6 fit explicitly retired to a one-face audit (:9143-9144, :10617). Knob B is a null experiment.

HIGHEST-VALUE NEXT OPERATION for the repo (not performed — read-only lane): register a FINDING invariant that the axial one-face RS fold vanishes exactly (-(-1/4)(1/16) + (-1/64) = 0, rank-1 by C-parity, saturating N^2 = e2*J = 1/256) while the vacuum one-face fold is 27/128, and record the fold's union-convolution face profile (0 / -0.30692-S / +38.14851+S) as the quantity any future two-face F07 weight must include. Both are pure rational algebra over corpus-exact inputs and are T1-promotable today; the second turns the documents' proposed two-face test from unfalsifiable into specified.

### 9.9 `rules-compliance`

LANE: the documents against WORKHOUSE's own rules, plus A §6.

=== 1. A §6, item by item ===

ITEM 1, "Corrected document A". Compliant only in a specific shape. It cannot go in theory/ (immutable, SHA-pinned, and adding to it is "a deliberate, reviewed event" through `make manifest` — and theory/ is the governing stack, not session output) nor in corpus-import/ (pinned, and test_corpus_integrity walks the directory since ADR 0006, so an added file breaks the pin). The precedent home for a dated, hand-written session analysis already exists: docs/referee/ holds eight such files, and docs/state_of_the_program_2026-08-22.md is the same genre. It lands at T3 and promotes nothing. Two required changes: (a) "Land the corrected A, not the uploaded one" inverts the retraction rule — see §5 below; (b) if the intent is to admit the whole set rather than one document, the sanctioned route is `workhouse triage` (which I ran; it works and reports nothing byte-identical to anything pinned) followed by a declared archive in ledger/notes.yaml with a per-digest verdict and a mandatory reason, under the closed vocabulary import/extract/duplicate/superseded/set-aside — and "No verdict promotes anything past T3."

ITEM 2, the check as an invariants.py suite. The only item that is straightforwardly in-charter and the only one that moves anything off T3, so it should land first — but not as drafted. Required shape: register on a `_suite(...)` in src/workhouse/invariants.py; cite the corpus section AND the document (README: "section numbers are not interchangeable across documents"); return `(passed, detail)` with the numbers a reader can argue with; declare tier=2 wherever a float or tolerance decides — tests/test_invariants.py:25-40 fails any T1 check whose body matches `_NUM|TOLERANCE|\d+e-\d+|isclose`. New exact constants go in constants.py as sympy.Rational with source document, section, status and evidence per CONTRIBUTING: −13/896, −39/1280, 143/8960, −54321/837760, −327/83776, −5/7168, D_EXACT, FOLD. I checked: none of them is in the registry today; only LINKED_VACUUM_4 already is. Blind per-size floats take the `_NUM` suffix. Row by row: checks 1 and 3 are clean T1; check 2 is T2 and must print its tolerance and say what it actually compares (an exact rational against a 12-significant-digit printout; the true statement is "0.0159598214286 is the correct 12-digit rounding of 143/8960", gap 2.86e-14); check 4 must be renamed and re-scoped, since what it verifies is a denominator lcm and not decomposability; check 5 must invert into a FINDING asserting the 5.17e-13 gap rather than a passing "closes"; check 6 is fine as a FINDING, but the provenance guard is only a check if the value-plus-provenance tuple lives in the repo — a guard over a string the repo does not hold is decoration. Then `make catalogue frontier certified` and `make check`, because the three generated views have staleness tests. Nothing here adjudicates, which ADR 0001 explicitly allows.

ITEM 3, the G3 one-liner. Non-compliant as worded — see finding `gamma-scalar-mis-routed-to-C2`. Compliant version: open C23 with both values side by side and neither promoted; route it to G3 the way C2 is; add to G3 at most a pointer that protocol item 10 restricted to two faces is a cheap partial discharge, cross-referencing the existing FINDING that the harness hardcodes item 10 OPEN. One more constraint: if "the entire gap lives in size ≥ 2" is stated as a claim rather than a note, it is an identification claim about two computations being the same quantity — the shape gaps.yaml's `unifying_candidates` requires a falsifier for. The falsifier is already written in A §4 ("W22-off blind(2) ≠ F07(2)"), so state it explicitly and the rule is satisfied.

ITEM 4, the new ADR. Duplicative — see finding `proposed-adr-duplicates-three-rules`. It is CLAUDE.md non-negotiable #5, ADR 0001's Context, and ADR 0010's Arb paragraph, all three. The maintainer's rule in CLAUDE.md makes rule-mass without a newly named failure a candidate for removal, not addition. Write ADR 0013 about the v10a.21r pattern instead: an engine algebraically wired to reproduce the total it is asked to adjudicate, and hence structurally incapable of adjudication. That failure has a name, a witness, a maintainer retraction in the corpus, and no existing ADR covering it. It is also distinct from C22, which is about a fitted diagonal shift rather than a wired transform.

ITEM 5, optional Lean. Recommend against — see §2.

=== 2. Is a QBOUND divisibility certificate a T0 statement, and is it worth it? ===

In FORM, yes. Integer divisibility and rational identity are exactly the "pure rational and polynomial algebra" lean/CLAUDE.md admits, and the whole thing is three lines:

  def QBOUND : ℤ := 62895057857493885215590055852113920000000
  def D_EXACT : ℚ := -361008126292641364183 / 7250590288602460800
  theorem den_dvd_qbound : (D_EXACT.den : ℤ) ∣ QBOUND := by norm_num
  theorem qbound_lift : (-3131555650840341423974721085483725619200000 : ℚ) / QBOUND = D_EXACT := by norm_num
  theorem m4_assembly : D_EXACT + 5315003/140454 - (-1474623/1675520)
      = -160506019419340168451/14501180577204921600 := by norm_num

In VALUE, no, for three reasons.

(a) It proves nothing that was ever in doubt. I verified all three statements in Python `Fraction` in well under a second, and the shipped validate_modular_haar_ledger.py already gates them. The failure mode here was never "the rational arithmetic might be wrong."

(b) The load-bearing content is not rational algebra. What matters is that D_EXACT IS the sum over the 69,800 contraction classes — an enumeration plus an SU(3) Haar contraction. ADR 0011 already ruled on precisely this: "the certificate certifies the Boolean/ZDD encoding, so T0 is reachable only if the physics-to-encoding step is itself proved in Lean; until then the ceiling is a certified T1." Getting the enumeration into Lean means entering the census as literals, i.e. axiomatizing the thing in question, which lean/CLAUDE.md forbids in as many words: "Do not axiomatize a physics assumption to get a compiling theorem. The point of formalizing is to *expose* the hypothesis an informal derivation left out; an axiom that hides it inverts the exercise."

(c) It buys a T0 stamp for a quarantined scalar. The theorem would sit in Basic.lean beside the sealed core, be counted in FRONTIER §1's theorem total, and require an entry in ledger/theorems.yaml naming the claims it formalizes and the checks it promotes (ADR 0007 item 3; test_graph.py enforces both directions and every `promotes` entry must be a theorem's whole statement). The only honest `formalizes` target is the quarantined scalar. That is exactly the misreading CLAUDE.md #5 and ADR 0001 exist to block — and A's own capstone says so, which makes item 5 self-contradictory with item 4. A one-line T1 check in invariants.py carrying the divisibility in its detail line delivers the same information and cannot be misread.

Note also that lean/README.md scopes the T0 layer as containing "nothing touching the disputed fourth-order kernel... because none of that reduces to rational arithmetic." Item 5 would be the first breach of that sentence, in exchange for a `norm_num`.

=== 3. Is A's self-description accurate? Per-row tier audit ===

The self-description is not accurate. "Every check it points to is machine-verified" — the check script is not in the delivery, and none of the eight rows is registered where CLAUDE.md's tier table says T1/T2 live. Tiers are computed, not asserted; every row is T3 here until the suite lands. Per row:

  1  one-face gap                        T1 claimed | arithmetic TRUE, T1-able, T3 as delivered
  2  one-face agreement                  T2 claimed | no tolerance stated; compares an exact rational to a 12-digit printout — the honest statement is a rounding check, gap 2.86e-14
  3  one-face agreement is explained     T1 claimed | content reproduces exactly, but it is a citation of gate declarations (T3) and "explained" overreaches the 4-state toy model
  4  two-face vacuum                     T1 claimed | e4(C) − 2·V1 = −327/83776 is TRUE and T1-able; B §3's factorization of 83776 as 2^7·7·11·17^2 is wrong (that product is 2848384; 83776 = 2^6·7·11·17) — A does not repeat the error
  5  linked-vacuum decomposition         T1 claimed | the stated identity is an lcm and cannot fail for the reason claimed; the real decomposition is gated only by the retired engine
  6  blind table closes                  T2 claimed | FALSE at printed precision; residual 5.17e-13, equal to 8·a_4 bit-for-bit; no tolerance
  7  F07 anchoring-invariant             T1 claimed | a scan dressed as a derivative; source audit not delivered
  8  F07 oracle-free                     "—"        | correct tier is T1 if it runs here over pinned bytes, T3 as delivered

On row 8's missing tier specifically: the repo's vocabulary DOES cover a dataflow-scan result, and no fourth tier is needed (AGENTS.md forbids adding one, correctly). `Suite.check` defaults to tier=1 and raises on anything other than 1 or 2, and the repository already registers scan/dataflow verdicts at that default — "FINDING: the contamination scan reads only the engine file" (invariants.py:654), "FINDING: the harness can never report COMPLETE" (:666), "quarantined targets never reach the engine process" (:697). The tier is fixed by how the verdict is decided, not by subject matter: an exact deterministic predicate over pinned bytes is T1; a float comparison is T2; an assertion nothing re-runs is T3. So the gap is in the document, not the ladder. The one thing the repo's own scan FINDINGs also teach is why an out-of-tree "zero leakage" result is weak: the harness's scan reads a single file, and the repo asserts as a FINDING that this misses anything arriving by import, JSON, npz or checkpoint. A scan run elsewhere, over an unshipped tree, with no transcript, is T3 and stays there.

=== 4. What tier can an out-of-tree run reach, and what must ship? ===

ADR 0012 draws the line at where the artifact was produced: settlement/ is received (evidence `record-backed`, or `cold-reproduced` when a rerun transcript exists), runs/ is produced here by pinned code, and the ADR is explicit that "the evidence vocabulary is unchanged (no fourth ladder): a run here is simply what `cold-reproduced` always meant, with the generating script present instead of absent." An out-of-tree run is therefore received evidence, T3 for what it asserts. It reaches T1/T2 here only through a check in invariants.py that recomputes something from pinned bytes — and the tier that results is the tier of that check, not of the run. It cannot reach T0 (ADR 0011's ceiling, lean/CLAUDE.md's axiomatization ban). Nothing about "exact", "CRT-unique", "certified" or "independent referee" changes this; ADR 0010's Arb precedent is the governing analogy — a rigorous comparison is still T2, and "certified" describes the comparison, never the claim.

Concretely, for the exact-Haar package to be admissible:
  1. runs/rank3_order4_exact_haar_2026-08-23/ — flat, manifest named exactly SHA256SUMS, covering EVERY file (fixes the three test_runs.py failures in finding `cert-zip-cannot-land-as-a-run`).
  2. README.md in that directory saying what was run, on what (interpreter, versions, wall clock — the summary records 264.95 s), and explicitly what it does and does not establish; ADR 0012 also requires naming what was withheld and why (the 164,662-record W2/R2 history is the obvious candidate). runs/mce_freeze_and_first_run_2026-08-22/README.md is the exemplar and is unusually good at the "does not establish" half.
  3. The GENERATING code, not only the audit code: primitive_rank3_order4_cubic.json, ledger_generator.py, exact_haar_sum.py, verify_exact_haar_ledger.py, rank3_order4_cubic_freeze.json. None is in the zip. Without them this is settlement/-class received evidence, because ADR 0012's whole distinction is that the generating script and the artifact are both present.
  4. The fold and linked-vacuum reproducers (work/fold_linked_exact/) — FOLD = 5315003/140454 enters the final scalar as a literal and nothing here derives it.
  5. Registry entries in constants.py for D_EXACT, the weighted Haar sum, FOLD_EXACT and QBOUND, exact as sympy.Rational/int, each with source document, section, status and evidence per CONTRIBUTING.
  6. Checks in invariants.py that parse the pinned ledger — ADR 0012: "Checks that cite a run parse the pinned artifacts; the heavy recomputation stays a documented one-command reproduction." I did the full ledger→D_EXACT→m4 re-derivation here in a few seconds over the 1.5 MB gz, so this is affordable inside `make verify`.
  7. uv.lock / environment pinning per CONTRIBUTING — "the lockfile is what makes a result reproducible rather than merely recorded."
  8. A reconciliation or a gate for the census divergence (block_orbits 3642 vs 3597, pair_occurrences 1831607 vs 1829147).
  9. An honest independence statement. Both routes are same-session, same-author, target-known; C §7 concedes it.
What it would then be worth: `cold-reproduced` in evidence, T1 for the ledger→scalar arithmetic, T3 for the physical identification, `open` in claim status. Not `proven`, not T0. That is not a small prize — a T1 check that the delivered ledger sums to the quarantined scalar, plus the LINKED_VACUUM_4 corroboration, plus the RAW_FOLDED FINDING, is three real moves off T3.

=== 5. The two self-corrections, and what is missing ===

Spirit: partly right. Both corrections are stated rather than deleted, both are in a numbered section labelled as corrections rather than folded silently into the prose, and the second names what survives ("multi-face W22-O4-safety is the one load-bearing claim that is fit-argued rather than exactly proven, and F07 does not rest on it"), which is the ADR-0005 move of separating the dead mechanism from the surviving reformulation. Three ways it falls short of the rule as written:
  (i) The rule says retract "in the repository, not just in conversation." Neither correction is in the repository, and neither is the document carrying them.
  (ii) ADR 0005's pattern keeps the failed claim as its own artifact and names it — "Retracts the mechanism proposed in ADR 0004" — with the exact step that failed ("one uncounted projection"). Here the superseded text is paraphrased, not quoted, and its home document was not delivered, so the diff is invisible. "Land the corrected A, not the uploaded one" is replacement, which is the failure the rule names: "Deleting a refuted claim destroys the evidence that it was tried." The parenthetical "(Kept, not silently overwritten…)" asserts compliance that the instruction itself defeats.
  (iii) The W22 self-correction never says where the too-strong claim was made, so a reader cannot find the original to judge the correction.

Documents A references that are NOT among the five artifacts:
  - DENOMINATOR_LOCALIZATION_INVESTIGATION (A's internal "A") — carries §5.5, §6, §11.2, §11.3, §12, all load-bearing for A §2's capstone, §5 bullet 1, and §6 item 5.
  - ORACLE_COUNTERFACTUAL_AUDIT (internal "C") — sole support for A §2 rows 7 and 8.
  - F07_VS_BLIND_COORDINATION_NOTE (internal "F") — the document A tells the reader to read first, and the source of connections C1 and C3 cited in §5 and §6.
  - f07_twoface_adjudication_check.py — the "machine-verified spine"; without it A §2's entire tier column is unsupported and A §6 item 2 has no object.
Referenced by D and also missing: WORKHOUSE_RANK3_ORDER4_EXACT_HAAR_FINAL_AUDIT_20260823.md (line-cited at :9-40, :42-55, :57-91, :93-160, :124-126, :158-160 — not in the zip, and the zip's AUDIT_REPORT.md is a different 70-line document), work/fold_linked_exact/README.md, and work/rank3_order4_cubic_ledger/{primitive_rank3_order4_cubic.json, ledger_generator.py, exact_haar_sum.py, verify_exact_haar_ledger.py, canonical_run_final_20260823/rank3_order4_cubic_freeze.json}.
In the other direction: the certificate zip that WAS delivered is not listed in A §0 at all, so A's index is wrong in both directions.

=== Overall ===
Of A §6's five items: item 2 is the right first move and needs three specific repairs; items 1 and 3 are landable only in changed form; item 4 should be replaced with a different ADR; item 5 should be dropped. The list also omits the two things that would actually move claims off T3 — a FINDING on RAW_FOLDED_AXIAL_GAMMA_NUM, and the LINKED_VACUUM_4 corroboration. The underlying work is careful and its restraint under ADR 0001 and non-negotiable #2 is genuine; the master record is the weakest document in the set, because it is the one that rounds, over-tiers, and mis-routes what the other three state precisely.

### 9.10 `corpus-value-search`

SEARCH-BY-VALUE INVENTORY (distinct ORIGINATING computations, not files; corpus_index scan over 928 files + targeted grep)

143/8960 — 3 files by index (misses a 4th: ENGINE_O4_hodge_rootonly_firewall_v1.py:43 writes `Q(143, 8960)`, which the Fraction pattern does not match). Named EXPECTED_GAP (firewall v1:43) and V26_ONE_FACE_PREFIX_EXACT (v10a.29b:66). ~3 distinct originating computations: (1) exact Rayleigh-Schrodinger series in one_face_certificate() at firewall_v1:218-229; (2) the v10a.26/v23g generic reduced-Haar numeric one-face fit regressed against it (v10a.24c section-15 benchmark, BENCHMARK 1); (3) the v10a.26 rooted size-1 row printed as +0.0159598214286 at 15 hour RUN.txt:10620. Monday 531 PM.txt:9702 and v10a.29b are quotations of (1)/(2).

-13/896 — 79 occurrences / 26 files, but ~3 origins: (a) firewall_v1 one_face_certificate exact series; (b) DATA_O4_OrderSchedule_Occurrence_Preflight_CPU.py:317-338 `exact_one_face_w22_sensitivity` (independent 4x4 exact Gelfand toy), gated :615; (c) literal injection `analytic_11=_XQ(-13,896)` in v10a.20/20b/21/21r. Everything else (14 notebooks, 6 transcripts) is a copy.

-39/1280 — 43 occurrences / 26 files, 2 origins: (a) firewall_v1 exact vacuum series (EXPECTED_VACUUM:41); (b) v10a.7 `_v17_vac_cluster({seed})` numeric, gated at :5411 with tol 3e-9. All later engines inherit the v10a.7 prelude.

-327/83776 — 61 occurrences / 25 files, ONE origin: v10a.7 `_v17_vac_cluster({seed,q})` at ENGINE_O4_hodge_v10a7_marked_linked_scalar.py:5423-5434, run on the coplanar and perpendicular representatives (float gate, tol 3e-9), plus the agreement gate :5436. Named VPAIR (v10a.21r:359, audits/08:45) and omega4. v10a.20:6021 is the inherited same gate; v10a.18:95 hardcodes `VAC_PAIR_LINKED = Fraction(-327, 83776)`; chat.txt:1750-1772 algebraically re-derives it from the two gate values (a verification, not an independent route).

-54321/837760 — 63 occurrences / 23 files, same single origin as above (gate at v10a.7:5433). Named e4(C) / "full e4".

-1474623/1675520 — 32 occurrences / 27 files, 2 origins: (a) v10a.7:5462-5466, V4_LINKED_MARKED = 13*e4(1face) + sum_cls n_cls*omega4(cls), float-gated; (b) v10a.21r:358-369, the same sum rebuilt from concrete embeddings in exact rationals and gated with `==`. This is the ONLY repo-registered value in the whole list: `workhouse search -1474623/1675520` returns CONST:LINKED_VACUUM_4. It also carries a recorded FINDING (C20) about the float-reconstruction the run printed beside it.

-5/7168 — 2 files, ONE origin: DATA_O4_OrderSchedule_Occurrence_Preflight_CPU.py:616 and its test companion at :22. It is the W22 sensitivity of a fixed 4x4 one-face toy at order five, not a branch difference.

5315003/140454 — 9 occurrences / 7 files, ~3 origins: (a) v10a.6 scalar Q1-fold gate (`gate("v10a.6 exact axial Q1 fold=5315003/140454", FOLD_A==Fraction(5315003,140454))`, in both NB_HAAR_..._v0_6.ipynb:802 and ENGINE_O4_hodge_v10a6_...py:802 — same code, two files); (b) v10a.7:5653 float re-gate at 2e-8; (c) v10a.23 "matrix fold collapses at Gamma to exact 5315003/140454" (NB v10a23_fullt1_operatorfold_k4:6793) — a genuinely different route (matrix fold vs scalar fold). Named FOLD_A / FOLD_EX.

-160506019419340168451/14501180577204921600 — 7 files, ONE origin (the completed v10a.20/20b denominator-lift run). v10a.21/21r hard-code it as a target; 15 hour RUN loads it after unblind; audits/08:54 and corpus-import/theory/DOC_FLUX_constants_index.md:136 quote each other. Repo names it QUARANTINED_SCALAR (constants.py:427), status falsified / "rejected by both sides".

-361008126292641364183/7250590288602460800 — 2 files, both prose, one quoting the other. See unverifiable.

-805586892848311021/8092176661386675 — 0 corpus occurrences (E only).

10.293333600759848, -0.403971702978, -0.178800648136, -0.208333333333, +0.0159598214286 — each 3 files, ONE originating computation: the 15-hour v10a.26 run. The two transcripts are the same run captured twice; the third file (NB_..._v10a26_..._alt2.ipynb) holds it as a STORED OUTPUT of that run, not as source. None of the five is in any repository claim.

69800 / 2468250 / 164662 / 82384 / 82278 / QBOUND-digits — 0 corpus occurrences.
117161, 9814138, 1829147, 5400 — 3 files each (v10a.20, v10a.20b, v10a.21), ONE origin (the v10a.20b census cell); the "3,597" of C §4 shares that origin.
3895 — corpus vocabulary for the Stage-3H inventory, and it is in the LIVE repository ledger: ledger/gaps.yaml:66,72 and docs/decisions/0011:20, plus audits/09-dual-cold-oracle.md:7,75,83 which records that Gate 3 (1,478 -> 3,895) is unimplemented anywhere in F09.
609 / 203 / 33 — corpus vocabulary; 609 = 203*3 marked evaluations is protocol item 3 (hodge README:31), 203 concrete clusters / 33 rooted shape classes printed at 15 hour RUN.txt:10747. Note 203 and 33 are low-entropy strings and their raw grep counts (232 / 772 files) are noise, not support.

ANSWERS

1. Which "new" facts already exist verbatim? Four of the six rows in B's check table. (i) The one-face gap 143/8960 is EXPECTED_GAP at firewall_v1:43, gated exactly at :218-229, one line below the line B cites — and it is already identified as the size-one ROOTED row in v10a.29b:13/66 and regression-tested against the generic reduced-Haar engine in the v10a.24c section-15 benchmark. It agrees at all five orders (8/3, 1, 1/2, 7/32, 143/8960), not only at c4. (ii) The two-face vacuum e4(C) and omega4, with the coplanar==perp agreement and the disconnected-spectator zero, are v10a.7:5433-5444. (iii) The V_link face decomposition exists in a stronger exact form with the actual counts 13 + 124 (80 perp, 44 coplanar) at v10a.21r:358-369, v10a.7:5460-5466 and theory/superseded/MASTER_THEORY.md:568. (iv) The branch gap 10.293333600759848 is printed at 15 hour RUN.txt:10633. Genuinely NOT in the corpus: the 69,800-class contraction, the 164,662-record W2/R2 freeze, the modular/CRT layer, and the exact D_EXACT as a machine-checkable artifact — all external and unverifiable here. Note the caveat that the fullest prose statement of (ii)+(iii) sits in theory/superseded/MASTER_THEORY.md, which CLAUDE.md forbids reading as current; the current-document version of that passage does not exist, so the machine-checkable sources (v10a.7, v10a.21r, audits/08:45) are the ones to cite.

2. -327/83776, and by how many routes? Already established, but by ONE originating measurement, not two. v10a.7's `_v17_vac_cluster` computes it for the coplanar and perpendicular pair representatives (same code path, two geometries) and float-gates both at 3e-9; that is a robustness check, not independence. The disconnected-spectator zero at :5444 is a NULL CONTROL on a non-adjacent pair — it produces no value for the connected pair and is not a route. The corpus does contain a second, genuinely independent constraint the documents miss: the exact closure 13*V1 + 124*VPAIR = V_link (v10a.21r:367-369, exact `==`), which pins VPAIR given V_link, V1 and the integer embedding counts. Tier: the corpus evidence is T2 at 3e-9, not the T1 that A §2 and B §6 assert; the only exact statement is the definitional rearrangement.

3. Per-size F07 decomposition outside v10a.21r? No — the trap is load-bearing and correct. Exhaustive grep over programs/ and records/ for `_v21_size_table`, "size sums", "by size", "bysize", "by_size", "per-size", "support_size" returns exactly four engine families: v10a.21/21r (the only F07-side one, and v10a.21r is a same-kernel resume of v10a.21 — one engine, two files), and v10a.24c, v10a.27, v10a.28, all on the BLIND rooted-cluster side. Stronger: no transcript anywhere in the corpus records v10a.21r's size-table output, so the exact F07 per-size numbers have never been written down at all. BUT the documents missed the mirror-image fact on the blind side: `ENGINE_O4_hodge_v10a28_orderaware_gram_firewall_a100.py:1379-1409` is an ORDER-AWARE engine with a by_size decomposition and V28_ORDER defaulting to 4 — i.e. Knob B's machinery already exists, unrun (and v10a.29b:22 forbids invoking it at order four). Combined with finding #1, the discriminator A §4 proposes is either already answered or aimed at the wrong engine.

4. Vocabulary. No coinage collides with a repo-coined name (ledger/symbols.yaml's only `coined_here: true` entry is Phi_C). All of M4_SHORTCUT, M4_ORACLE, ax_rest, local_shift, W22, VPAIR, V1 and "two-face" are corpus vocabulary used correctly. Two problems: (a) B and D use `m_4` / `m₄` as an umbrella symbol, which the register explicitly FORBIDS (R4 / ADR 0002); (b) "F07 branch" collides with the corpus feature id F07 = "Exact denominator-lift fourth-order arithmetic" (audits/00-features.md:25), and the per-size adjudicator the documents call F07 is corpus F08 (:26). "Blind linked-cluster oracle" is a paraphrase — the corpus writes "independent finite-cluster (linked-gap) oracle"; the exact phrase "blind linked-cluster" appears only in this repo's docs/decisions/0002. "Two-face adjudication" is new as a phrase; "two-face" is not.

HIGHEST-VALUE NEXT OPERATION (search-by-value lane): register the four load-bearing rationals that no repository claim currently reaches — 143/8960, -327/83776, -54321/837760 and -13/896 all return "no claim matches" from `workhouse search`, while -1474623/1675520 does not. A single invariants.py suite carrying (i) EXPECTED_GAP = EXPECTED_AXIAL - EXPECTED_VACUUM as T1 with the firewall_v1:43 cite, (ii) 13*V1 + 124*VPAIR == V_link as T1 with the v10a.21r:367 cite, and (iii) a FINDING that the printed per-size table misses its own printed total by 4277 ulps, would promote three T3 corpus assertions to T1 and record one real discrepancy — without touching either side of the open branch conflict.

---

## 10. Deliverables and state

| | |
|---|---|
| document | `docs/referee/rank3_order4_upload_review_2026-08-23.md` (548 lines) |
| commit | `b23fe61` on `claude/files-theory-graph-review-2mei2d` |
| pull request | [ats314/WORKHOUSE#31](https://github.com/ats314/WORKHOUSE/pull/31) (draft) |
| CI | `check` ✅, `Lean (T0)` ✅, `Shell lint` ✅ |
| mergeability | `clean` |
| review threads | none |
| local verification | `make check` exit 0 — ruff clean, 100 files formatted, 339 tests pass |
| invariants | 140/140, unchanged (this PR registers no check) |

Nothing in the repository's evidence layer moved. The referee report is a `docs/referee/`
document, the same class as the existing notes-review and novelty-search records.

### 10.1 What was deliberately *not* done

- **No relabel of `QUARANTINED_SCALAR`.** The evidence moves one axis (`record-backed` is
  stale) and not the other (`falsified` is a claim about physical identification, which
  nothing in the upload bears on). Non-negotiable #2 makes this a maintainer call.
- **No new contradiction entry.** The correct landing (amend C1's quantity block, or open
  C23) is a ledger write, and the review's job was to establish *where* it goes.
- **No tolerance widened.** `HAMER_TOLERANCE = 5.3e-13` sits 2.46% above the gap it gates;
  the finding is that its derivation is unrecorded, and the prescription is to record the
  reason, not to raise the bound.
- **No new invariants registered.** §11 lists five candidates so that registering them is
  a reviewed decision rather than a side effect of a referee report.
- **No repo bug fixed.** The `search.py` and `corpus_index` defects are real and one-line-ish,
  but they are a different change from this one.

---

## 11. Recommended next actions

Ordered by ratio of value to cost. None promotes either side of the open contradiction.

### 11.1 Cheap and unambiguous

1. **Fix `search.py:219-225`.** Move or duplicate the corpus-occurrences rendering above
   the early return. One line. Currently `workhouse search --corpus` prints "no claim
   matches" *and advises adding `--corpus`* for values with 61 corpus occurrences, while
   `cli.py:160-163` exits 0 on the basis of the scan it just discarded. Every rational in
   this dispute is affected: `-327/83776` (61 occurrences / 25 files), `-13/896` (79/26),
   `-54321/837760` (63/23), `-39/1280` (43/26), `143/8960` (6/3), `-5/7168` (2/2).
   Add a regression test — `tests/test_search.py:88` is already the no-hits case and does
   not pass an occurrences argument.

2. **Extend `corpus_index.PATTERNS` to aliased constructors.** It matches `a/b`,
   `Fraction(a, b)` and `\frac{}{}` but not `Q(143, 8960)` under `Q = Fraction`, so
   `_extract` returns **zero** rationals for `ENGINE_O4_hodge_rootonly_firewall_v1.py` and
   the entire `EXPECTED_VACUUM`/`AXIAL`/`GAP` block is invisible to search-by-value. With
   (1), this is why both indexes were blind to material the upload then re-derived — the
   failure mode `AGENTS.md` names by name.

3. **Reconcile the two Hamer provenance statements.** `invariants.py:392-393` calls `a_4`
   "an unverified notebook transcription" while `:1285-1292` records that caveat retired
   and `literature/index.yaml:454-497` pins the primary. `constants.py:229-238` and
   `constants.py:647` contradict each other the same way 400 lines apart, and
   `index/claims.jsonl:29,149` faithfully regenerate the stale side — so `make catalogue`
   will not fix it; `constants.py:647` must change first. The honest replacement is neither
   the old caveat nor silence: the primary was read and digest-pinned 2026-08-21, but
   `literature/index.yaml:461` records `fulltext: null`, so the digit-for-digit reading is
   not re-checkable in-repo.

### 11.2 Genuine T3 → T1/T2 promotions

4. **Register `one_face_certificate()` as a T1 invariant.** It executes and passes today,
   derives all five `EXPECTED_GAP` entries in exact `Fraction` from SU(3) characters, and
   `143/8960` appears nowhere in the verification layer.

5. **Register the exact `ax_rest` beside the stale float.** `constants.py:428` records
   `-11.9485781794007`; `QUARANTINED_SCALAR + LINKED_VACUUM_4 =
   -86634244910174898583/7250590288602460800 = -11.948578179401377`, a gap of `6.774e-13`
   = **381 ulps** (`math.ulp`), 511 under the `2^-53` convention the C20 check itself uses
   at `invariants.py:408`. Nothing reads the constant, so no suite would catch drift in it.
   The pattern already exists: `DELTA_GAMMA_NUM`/`DELTA_GAMMA_AS_PRINTED_NUM` carry a
   **one**-ulp discrepancy and it is a registered check at `invariants.py:327-334`. Cause
   is upstream and now measurable — RUN15's own float `D` is `7.375e-13` off the exact
   `D_EXACT`, and that propagates through `ax_rest = D + FOLD`.

6. **Register the one-face fold cancellation** `-2C - e2·N + J = 1/64 - 1/64 = 0`. It is
   the unstated premise the entire localization rests on, it is exact, and it is why
   `-13/896` can serve simultaneously as the full one-face `e4` and as v10a21r's direct
   `D[{ROOT}]` without contradiction.

7. **Record the reason `HAMER_TOLERANCE` is what it is** — without widening it. Across the
   five Hamer bridge comparisons, `gap/print-budget` is 0.994, 0.557, 0.784, 0.681 and
   **1.293 for `a_4` alone**. The other four target exact corpus rationals, so paper
   rounding is their only error source; `a_4`'s target is a float from the blind run
   carrying a second error term, calibrated in the same run block
   (`15 hour RUN.txt:10641-10648`: `A` vs `5/48` at rel `5.887e-13`, `alpha` vs `5/12` at
   rel `5.839e-13`). That covers the overshoot and belongs in the detail line.

### 11.3 Ledger writes (maintainer calls)

8. **Route the branch conflict to C1/C22 under G3.** Amend the quantity block at
   `contradictions.yaml:36-40` in place, or open **C23** (`C22` at `:272` is the current
   maximum). Both values side by side, neither promoted. Do **not** file under C2.

9. **If the G3 one-liner is landed, rewrite it.** Its first clause credits the session with
   a pre-existing corpus certificate; its second names a discriminator that is provably
   null. What is new is the size ≥ 2 *inference*, resting on the pre-existing one-face
   certificate.

10. **Do not add the proposed ADR.** "Exactness certifies arithmetic, never physical
    identification" is already CLAUDE.md non-negotiable #5, ADR 0001 and ADR 0010.

11. **Do not adopt `arithmetic_status` / `physical_status` / `quarantine_reason`.** Three
    new fields would be a fourth vocabulary, which `AGENTS.md` forbids. The existing
    status/evidence split already expresses exactly this distinction.

### 11.4 If the exact-Haar package is to become admissible evidence

Under ADR 0010 and ADR 0012, what would have to be shipped:

- `ledger_generator.py` (~1,700 lines per `C`'s own citations) — without it the frozen
  census is pass-through data recomputed nowhere, and the package cannot unpickle itself;
- the freeze JSON, the W2/R2 history ledger, and the primitive manifest, so the chain
  primitives → history → pickle is hash-bound rather than starting at the pickle;
- the output of `independent_replay_modular_crt.py`, which is the only all-record
  recomputation and is not in the manifest;
- a `requirements.txt`/README (there is none), and `SHA256SUMS` rather than
  `SHA256SUMS.txt` if it is to land under `runs/` (`tests/test_runs.py:23`);
- an explanation of the `summary.json` edit, or a regenerated file.

### 11.5 The decisive test that remains

Not Knob B. `C §9` states it correctly: prove or refute, from a target-free canonical
Schrieffer–Wolff/linked-cluster construction, the operator identity

```
D11 + (1/2)<W2,R2> + fold - attached_vacuum  =  canonical vacuum-subtracted order-4 Gamma coefficient
```

That is an operator identity, not another numerator replay, and no amount of exact
arithmetic on the F07 side substitutes for it. Note also that any two-face comparison is
undefined until the fold convention is fixed (§1.1b): the five-point specification in
`A:98-104` / `B:159-176` / `D:213-227` fixes a vacuum convention and no fold convention.

---

## Appendix — reproduction

```bash
python3 - <<'PY'
from fractions import Fraction as F
D=F(-361008126292641364183,7250590288602460800); FOLD=F(5315003,140454); V=F(-1474623,1675520)
assert D+FOLD-V == F(-160506019419340168451,14501180577204921600)   # == QUARANTINED_SCALAR
assert float(D+FOLD) == -11.948578179401377      # constants.py:428 records -11.9485781794007
assert F(-13,896)+F(39,1280) == F(143,8960)
assert F(-54321,837760)-2*F(-39,1280) == F(-327,83776) and 83776 == 2**6*7*11*17
assert 13*F(-39,1280)+124*F(-327,83776) == V     # unique non-negative integer solution
PY

# v10a.26 exact-SW provenance of the blind table
sed -n '3p;10614p;10617p;10619,10626p' "corpus-import/records/transcripts/15 hour RUN.txt"
sed -n '7220,7222p;7230,7236p;7246p'   "corpus-import/records/transcripts/15 hour RUN.txt"

# the pre-existing one-face certificate the documents never cite
sed -n '41,43p;218,230p' corpus-import/programs/hodge_o4_adjudication/src/ENGINE_O4_hodge_rootonly_firewall_v1.py

# the face-independent W22 gates
sed -n '606,616p'        corpus-import/programs/hodge_o4_adjudication/src/DATA_O4_OrderSchedule_Occurrence_Preflight_CPU.py

# repo defect, reproduces live
workhouse search --corpus -- "-327/83776"
```

*End of full working report.*