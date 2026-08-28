# WORK_SINCE_2026-08 — triage and first-pass review evidence

**Date:** 2026-08-28.
**Archive:** branch `work-since-last-session` of ats314/WORKHOUSE, commit
`7bb4837` "work-since-last-session snapshot 2026-08-28" — a snapshot of the
maintainer's working folder (83 files, 82 unique digests, 136 MiB), covering
four days (2026-08-22/23) of AI-assisted work products.
**Method:** `workhouse triage` over the extracted tree, then seven parallel
reading agents (one per topical cluster), each instructed to treat every
document as a T3 claim, verify hashes and exact rationals where cheap, and
recommend verdicts. Every byte-identity claim recorded in `ledger/notes.yaml`
was **recomputed in this session** before being recorded — agent reports were
treated as leads, not evidence.
**Standing rule, observed throughout:** nothing here promotes anything.
C2 remains open with both sides recorded; no verdict changes any tier.

## Triage summary

- 0 files byte-identical to a pinned repository artifact; 1 in-archive
  duplicate pair (the MCE rerun notebook and its `(1)` copy).
- 18 coefficient-bearing files; census led by `linked vacuum` (11),
  `q_band^(4)` (8), the C1 quarantined scalar (8), `m_Γ^(4)` (6).
- 0 files carry the `4**r` coupling erratum.
- Misnamed file: `Carrier Persistence Problem.txt` is a **C2-dispute status
  note** (42-signature contraction proposal, Δw₍₁,₁,₀₎ = −25/256 prediction),
  not the carrier-persistence note. Triage by filename would misfile it.

## The seven clusters

### 1. MCE H0-closure 216 rerun readiness (G3)

One unexecuted Colab notebook, present twice (byte-identical, sha256
`a5119770…`). It pins `FROZEN_COMMIT = bcddd4a` (current main), verifies the
base engine hash `be9d77f5…` (matches `FREEZE.json`), and constructs a
cap-only derived engine with `max_states 100 → 216`, pinned sha256
`85940912…` — **recomputed here from the repo engine and confirmed exact**.
This is a *different* derivative from the run record's diagnostic fork
(100 → 100000, `9af3708e…`, full value also recomputed and consistent).

Two findings of consequence:

- **Not the unblock.** Every cell has `execution_count: null` — nothing ran.
  The harness freeze/run stages are present but hard-disabled
  (`AUTHORIZE_FREEZE = False`, `AUTHORIZE_609_CLUSTER_RUN = False`), and the
  default path does not re-run the contamination scan.
- **An expanded blocker claim, recorded nowhere in the repo:** the notebook's
  own output-sufficiency gate requires engine checkpoint/seal fields
  (`h4_endpoint_json`, `raw_h4_endpoint_ledger`, `h4_kernel`,
  `h4_kernel_sha256`, `shape`, `band_points`, `shape_extraction`, a blind-R
  declaration) — **none of these strings occur in the repo engine** (verified
  by grep), so by its own test the cap-216 engine still fail-closes. Per this
  notebook, the cap raise is necessary but not sufficient. Its hard-coded
  expected audit values (global closure max 216, 8 saturated topologies,
  243,288 R2 seeds, 1,449 link topologies) have **no stated provenance**;
  the repo's probe only ever measured the *first* oversize orbit at 216.

### 2. The rank3/order4 QBOUND family (C1/C22 territory, under G3)

Fifteen documents and six zips, all self-dated 2026-08-23 — the **source
corpus of the upload PR #31 refereed the next day**, not a response to it
(no file cites any PR #31 finding). Hash-level results:

- The `MODULAR_HAAR` zip is **byte-identical to PR #31's artifact E**,
  every packaging defect intact (`ledger_generator.py` absent, the
  post-edited summary `2b845725…`, the misnamed SHA file).
- The `EXACT_HAAR_FINAL` zip is **the artifact PR #31 could not obtain**:
  its summary hashes to exactly the `d3d2cb89…` "final exact summary" the
  referee found cited-but-not-shipped, and it **ships `ledger_generator.py`
  (`a72a2c41…`)**, the exact contractor, a manifest, and the CUBIC zip
  nested bit-identically. PR #31's "not replayable as shipped" and "no
  upstream binding" defects were defects of the *wrong package having been
  uploaded*. Not repaired: per-topology numerator independence still rests
  on the modular route's ≤0.120%-coverage artifacts, and one provenance
  wrinkle is new (two byte-different files both named
  `rank3_order4_cubic_freeze.json` inside the package).
- The oracle counterfactual audit and the denominator-localization
  investigation are **two of the four documents PR #31 reported missing**;
  the coordination note and the 8-check screen remain missing.
- A size-2 extension lane (`NATIVE_PQ_SIZE2` direct-D certificate,
  independent verification, Route A/B hostile adjudication) claims exact
  target-free reproduction of the F07 size-2 values (singleton −13/896,
  4+8 total −31127086619/8435667240 — arithmetic re-verified here) with W22
  structurally excluded through order 4; its underlying artifact zips are
  **absent from the archive** (hashes only). The Route A/B adjudication
  independently corrects the master record's `83776` factorization error
  and the 381-ulp stale float at `constants.py:428` — converging with
  PR #31 from a parallel session.
- No document claims to resolve C2; the `C2_ACCEPTANCE_GATE` package is
  explicitly a necessary-condition prospective gate ("never prefers a
  side"). The recurring relabel pressure on the C1 quarantined scalar
  ("rejected-by-both" → "exact F07-branch, physical audit-pending") is a
  maintainer-only call, and PR #31's calibration stands: the *evidence*
  axis moved (record-backed is stale), the *status* axis did not.

### 3. The carrier-persistence campaign (G17/G18/G19)

A note in four revisions (carrierv2 → carrier3 → carrier4, with a
self-scorecard: 3 of 5 proposed reductions refuted by its own hostile-referee
passes), three audits that partially demolish it (the printed finite-time
residue bound is **false as written** — counterexample μ = δ_M + 9δ_{M+Δ}
gives printed Z ≥ 10 vs true Z = 1; PMBSF (14.37)-type upper bounds can
never yield the needed lower residue bound; the one-ratio reduction dies on
two explicit counterexamples), and a positive fixed-spacing chain
(F1→F5, CMP(1)–(4)) claiming an isolated infinite-volume lattice
quasiparticle band at small u — explicitly *not* a continuum particle, with
the stopping point stated as the five uniform continuum hypotheses and the
Clay firewall respected.

**Provenance hole, blocking:** the campaign's own sha256 manifest pins 8
documents; **4 are absent from the snapshot** (the electric-shell theorem
proof, the Yarotsky import note, both CMP(1) documents) — precisely the
chain's foundations — and at least 8 further referenced theorem/audit files
are absent, as are the H0 audit's three verification scripts. The 4 present
files byte-match their digests (verified). Until the absent files arrive,
every "Proved" in the chain ledger resting on them is an unauditable
assertion.

The same-day documents also disagree internally without marking it (the
master chain calls fixed-contour TE the target; the H0 audit calls it the
wrong target and the alias gap g(b) the binding one) — no single document
is the campaign's current position.

### 4. Lean artifacts (PR #30's external-workspace origin)

Exact relation map, every hash recomputed here:

| snapshot file | PR #30 counterpart | relation |
|---|---|---|
| `WORKHOUSE_CarrierAtom.lean` | `lean/Workhouse/AtomLemma.lean` | byte-identical (rename at export) |
| `WORKHOUSE_FiberGap.lean` | `lean/Workhouse/FiberGap.lean` | byte-identical |
| `WORKHOUSE_Flatness.lean` | `lean/Workhouse/Flatness.lean` | byte-identical |
| `WORKHOUSE_Incidence.lean` | `lean/Workhouse/Incidence.lean` | byte-identical |
| `WORKHOUSE_CarrierAtomGap.lean` | `lean/Workhouse/CarrierAtomGap.lean` | earlier draft; PR adds `gap_asymptotic` |
| `WORKHOUSE_Spectrum.lean` | `lean/Workhouse/Spectrum.lean` | earlier draft; PR adds the multiplicity-two block |
| three `WORKHOUSE_*` md notes | `lean/Workhouse/review/{H0_FREE_CARRIER_AUDIT, KEY_DERIVATIONS, MULTIPLICITY_TWO}.md` | byte-identical |

Two audit documents are **not** on the PR branch and contradict each other
on the load-bearing question: `WORKHOUSE_carrier_atom_lean_audit.md` finds
the FiberGap coefficient `2861009/8438730300` to be the **isotropic
pentagonal-prism cap band** value (repo `DELTA_E_CAP_4`/`PENT_BANDWIDTH_4`),
wrongly transplanted into the cubic-carrier chain (claimed correct cubic
coefficient 5/12, ratio ≈ 614.5) and the "C2-disputed" label a
mis-attribution (the value is neither C2 side); `WORKHOUSE_LEAN_EXPERIMENT_
FINDINGS_20260823.md` calls the same literal "the C2-disputed coefficient"
throughout — and PR #30 ships that second attribution. Adjudication of this
contradiction is the center of the PR #30 review (in progress, separately).

### 5. NB_FLUX SU(3) A100 Monte Carlo (G18 instrumentation and data)

A complete hash-chained pipeline: defective original notebook → forensic
review (decisive finding: ordered Gram–Schmidt reunitarization is **gauge
non-covariant**, RMS defect 0.4319; repaired with polar/SVD projection,
defect 1.75e-7) → validated repaired engine (16/16 gates, twice) → spin-
resolved engine (T1⁺⁻ with J=1/J=3 partner channels, corpus improved
source, fixed-physical-radius flow) → A100 runs at β = 6.0625, 16³×20:
one 48-config tuning chain (analyzed: torelon a√σ = 0.1916(59) consistent
with the configured Athenodorou–Teper scale; exact A1⁻⁻ null control to
1.4e-19; **no mass plateau — ~10 effective samples**) and a **4×256-config
raw campaign, delivered unanalyzed** (the shared correlated analysis is the
actual next step). Bears on **G18 only**: the torelon here is a scale
channel, not G7's strong-coupling series; nothing touches C2 or G3.
Caveats recorded: GPU runs used an unlocked discovery runtime; the shipped
SHA manifest matches the zips' provenance copies but the archive-root
copies are CRLF-normalized (proved benign, but naive verification fails);
1024 configs sit below the engine's own `min_physics_blocks` threshold at
the declared blocking.

### 6. Denominator smoothness → localization (provenance forensics)

Three versions of one report page (v3 carries a **retracted** central claim
— the 17²/17³ two-scope split, corrected by the consolidated investigation,
which also records that the 17² estimate would have wrongly rejected the
legitimate C_shp), a GPT theory audit ("real but stated too broadly": the
fourth-order prime superset includes 23 and 47; the 56-entry census dropped
`KPS_T6`), a runnable implementation packet (13/13 tests pass against repo
HEAD — **reproduced here**; its ADR is misnumbered 0010, colliding with the
repo's existing 0010), and a side-neutral C2 acceptance gate
(`den | QBOUND`, support ⊆ S4) proposed as harness "item 12".

The capstone caution, re-verified exactly this session: an external
exact-Haar package computed `D_EXACT + FOLD − V_link` and landed
**byte-exactly on the C1 quarantined scalar** while passing every
denominator/QBOUND/Lean gate, presenting it as "the requested final
combination" with no quarantine flag. The investigation's forensics
exonerate its arithmetic (oracle-free) and identify what it skipped: the
anchoring step that *is* the dispute. **The certificate stack is necessary,
not sufficient — provenance, not physics.** Byproducts worth recording as
claims when this cluster is reviewed in depth: the candidate exact form
`ax_rest = −86634244910174898583/7250590288602460800` for the stale float
`RAW_FOLDED_AXIAL_GAMMA_NUM`, and the exact anchor gap
`ax_rest − q_band^(4) = −2179000819/239696600` (ADR 0002's
differently-anchored coordinates, now in exact form).

### 7. Strategy and meta

`MASTER_PROOF_STATE.md` (Rev. 4) is the apex self-audit — [V]/[R]/[R!]/[X]
labels, honest concessions (the rigorous fixed-spacing domain and the
continuum sit at opposite ends of the coupling axis; "T1 implies J=1" is
false — the carrier couples to J=3⁺⁻ at leading order; the decisive uniform
continuum step is flatly OPEN), and it partly retracts the OFF AXIS LEDGER's
independence framing (the three kernel copies are two executions of one
program). `OFF AXIS LEDGER.txt` *extends* the repo's C2 record — channel
decomposition of the 189-record kernel, `C_normal = −A_normal/2`, the
record-level tier-collapse cancellations (bears G14), a proposed engine-free
decisive test via `workhouse.cellular` — with every load-bearing arithmetic
claim under adversarial recomputation in this session (separately reported).
`STRONGEST_THEORY` rev 2 corrects rev 1 downward and corroborates the
pentagonal transplant. The four library files are byte-identical duplicates
of `literature/library/volume2/` (verified). The arXiv tarball is an
unrelated 798-page treatise (the archive's own KEY_DERIVATIONS records the
negative-connection finding). Two hygiene items: `gemini chat.txt` embeds
the maintainer's personal chat sidebar, and the Tabletop patent docx is
confidential — both flagged for removal from the pushed branch; neither
enters the tree.

## First-pass verdicts recorded (22 of 82)

Only structural verdicts — byte-identity and supersession chains, every
hash recomputed in this session:

- **duplicate (4):** the four library files, against their pinned
  `literature/library/volume2/` counterparts.
- **set-aside (12):** the seven files byte-identical to unmerged PR #30
  content and the two earlier drafts of PR #30 modules (the register
  correctly refuses references to content that is in neither the repo tree
  nor a manifest; re-verdict as duplicate/superseded if PR #30 lands);
  `gemini chat.txt` (content duplicated by GEMINI NOTES 822, plus the
  privacy exposure); the patent docx (confidential, unrelated); the arXiv
  tarball (unrelated).
- **superseded (6):** carrierv2/carrier3 → carrier4; Denominator Smoothness
  v1/v2/v3 → the consolidated investigation (v3's entry carries the
  retraction warning); STRONGEST_THEORY rev 1 → rev 2.

**Deliberately left pending (60)** — everything substantive: the QBOUND
certificate stack (import candidates gated on in-repo replay of the 69,800-
term ledger and digest verification), the carrier chain (blocked on the
absent pinned documents), the NB_FLUX pipeline (import candidates gated on
full manifest verification and a cold validation re-run), the MCE notebook
(its expected-values provenance must be found or the claims marked
unanchored), MASTER_PROOF_STATE / OFF AXIS LEDGER / STRONGEST_THEORY rev 2 /
the localization investigation (extract candidates whose named claims are
under recomputation now), and the two Lean audit documents (their findings
route into the PR #30 review).

## Asks recorded for the maintainer

1. **Missing pinned evidence:** the 4 manifest-pinned carrier-chain
   documents (`WORKHOUSE_ELECTRIC_SHELL_THEOREM_PROOF.md`,
   `WORKHOUSE_YAROTSKY_SPECTRAL_LOCALIZATION_IMPORT_NOTE.md`, both CMP(1)
   documents), the ~8 further referenced theorem/audit files, the
   `NATIVE_PQ_SIZE2` certificate zips (`a5710adf…`, `689a698f…`), the
   Route B checkpoint, and the h0_*.py verification scripts.
2. **Branch hygiene:** remove `gemini chat.txt` (or redact the sidebar) and
   the patent docx from `work-since-last-session`.
