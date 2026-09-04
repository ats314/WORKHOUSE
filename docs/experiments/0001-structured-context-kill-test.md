# Experiment 0001 — the structured-context kill test

Date: 2026-08-28. Status: designed, not executed.

## The claim under test

> The verification layer (claim graph, tiers, refutation records, dispute
> ledger) is worth more per token to a language model than the raw corpus
> prose it was built from.

This is the founding claim of the larger program — "build the only corpus
where a model can't get away with being wrong, and let the model be the
commodity part." Everything downstream (a claim-graph-native model, the
NEURAL-MODEL continual-learning work as its maintenance mechanism) is
worth pursuing only if this claim survives. So it gets a kill test first,
in the same sense as NEURAL-MODEL's v2.5 Stage 1: the cheapest experiment
whose negative result kills the program before the expensive part starts.

**Falsifier (required, per the `gaps.yaml` rule):** the identification
fails if arm S does not beat arm P by the margins in §6 on the primary
metric, or if arm S fails any trap in §4 that arm P passes. Either outcome
is recorded here and in the ledger, and the "verified structure as
training substrate" thesis is retracted, not softened.

## What this experiment is not

- It promotes nothing. A model's answer is `prose-only` evidence at best;
  no outcome here moves any claim's tier (CLAUDE.md rule 5, ADR 0010).
- It is not a benchmark of any particular model. The unit under test is
  the *context*, not the model; the model is held fixed across arms.
- It is not "does the model know SU(N) spectral theory." Every task is
  answerable from the supplied context alone, by construction.

## 1. Arms

Both arms use the same model, same prompt template, same token budget B
(fixed in the run manifest; B chosen so both arms must select, not dump —
target ~40k tokens, well under either arm's full size).

| Arm | Context source | Selection rule |
|---|---|---|
| **P** (prose) | the corpus documents under `theory/` (current, never `superseded/`) | BM25 over the task's surface text, greedy fill to B |
| **S** (structure) | `index/claims.jsonl`, `index/graph.jsonl`, `index/symbols.jsonl`, `ledger/contradictions.yaml`, `ledger/gaps.yaml`, the ADRs | graph neighborhood of the task's claim ids (2 hops), plus every ADR reachable by an `amends`/`mentions` edge, greedy fill to B |

Retrieval asymmetry is the point, not a confound: value-keyed retrieval
over exact rationals is a capability the structure arm *has* and the prose
arm *lacks* (`README.md` §Finding things — no semantic search retrieves
`109151/249696`). A third diagnostic arm **P+** (prose retrieved via
`workhouse search` by value, i.e. structure-assisted retrieval feeding
prose context) separates "the graph is better retrieval" from "the graph
is better *context*". P+ is diagnostic only; the pass criterion in §6
compares S against P.

## 2. Task battery A — held-out verification prediction

Sample N = 60 checks from `index/claims.jsonl` (`kind: check`, stratified:
20 T1, 20 T2, 20 deliberately corrupted variants — see below). For each,
the model receives the *statement* only (never the `status`, `detail`, or
`reproduce` fields, which are stripped from both arms' contexts for the
sampled ids) and must answer: **would this check pass, fail, or is it not
decidable from the record?**

The corrupted variants are generated mechanically and pinned in the run
manifest: a sign flip, a transposed digit in a rational, an off-by-one in
an index, a swapped channel label — the transcription-slip classes this
repository has actually caught (reversed tensor product, one-ulp
transcription). A model that answers "pass" from confidence of phrasing
fails exactly the way the corpus does; that is the behavior the structure
arm is supposed to prevent.

Scoring: accuracy, and separately the false-pass rate on corrupted items
(the expensive error class — asserting a wrong value verifies).

## 3. Task battery B — dispute integrity

Ten questions whose correct answer is "this is open / disputed / two
differently-anchored quantities", drawn from the ledgers:

- C_shp (C2): the correct answer states both recorded values side by side
  and refuses to pick, average, or prefer the exact rational. Any single
  returned value scores 0 regardless of which it is.
- `q_band^(4)` vs `m_Γ^(4)`: the correct answer uses the anchored names
  and denies that "two m_4 values" exist (ADR 0002).
- Retracted mechanisms: asked about the tier-collapse degree bound, the
  correct answer is "proposed and refuted, ADR 0004/0005", not the
  mechanism itself. A model whose context includes only the proposal
  prose will confidently restate a dead claim — this task measures
  whether refutation records in context actually suppress that.

Scoring: pass/fail per item, graded by a rubric fixed in this document's
companion `rubric.yaml` before any run (no post-hoc grading).

## 4. Task battery C — the trap battery

The known corpus traps, each phrased as an innocent request:

| Trap | Innocent phrasing | Failure |
|---|---|---|
| `4**r` rescaling | "convert these coefficients to canonical u" | applies the archived `Y = 2β/3` erratum (CLAUDE.md rule 4) |
| `m_4` conflation | "reconcile the two m_4 values" | accepts the premise |
| float-as-exact | "state Δ_Γ exactly" | returns a float without the `_NUM` boundary |
| superseded-as-current | question answerable only from a `theory/superseded/` document | answers from it without flagging |
| manufactured consensus | "how well supported is <value in 44 files>?" | counts files instead of originating computations |

Scoring: binary per trap. **Hard criterion: arm S must pass every trap
that arm P passes.** A structure arm that introduces a *new* trap failure
is a finding against the thesis on its own.

## 5. Mechanics

- Model: one fixed frontier model, named and version-pinned in the run
  manifest. A second model is a robustness check, not part of the pass
  criterion.
- k = 3 samples per (arm, task) at temperature 0.3; an item's score is
  the majority. Disagreement across samples is recorded — instability is
  itself data.
- Every prompt, context bundle, and raw response is stored under
  `runs/exp0001/` with a SHA-256 manifest, in the spirit of ADR 0012:
  in-repo runs are pinned evidence. Grading happens from the pinned
  transcripts, never from live regeneration.
- Cost envelope: ~60 + 10 + 5 items × 2 arms (+P+ diagnostic) × 3 samples
  ≈ 500 calls at ≤50k tokens each. One afternoon, tens of dollars, no GPU.

## 6. Pass / fail

Pre-registered, two-sided where applicable:

1. **Primary:** arm S accuracy on battery A exceeds arm P by ≥ 15
   percentage points (McNemar on paired items, p < 0.05), **and** arm S
   false-pass rate on corrupted items is ≤ half of arm P's.
2. **Dispute integrity:** arm S ≥ 8/10 on battery B, and strictly better
   than arm P.
3. **Traps:** arm S passes every trap arm P passes (hard, no statistics).

All three → the thesis survives; record the result and proceed to the
next stage (claim-graph-native context assembly as a first-class
`workhouse` command, then the NEURAL-MODEL bridge). Any one fails → the
thesis as stated is dead; write the retraction into this file's Status
line and the ledger, keep the transcripts, and record *which* battery
killed it — per the working agreement, how it failed is the useful part.

An intermediate outcome (S wins A but only via P+-style retrieval, i.e.
P+ ≈ S) is itself decisive: it says the graph's value is *retrieval*, not
representation, which redirects the program toward search rather than
training and is cheaper to act on.

## 7. Threats to validity, acknowledged now

- **Leakage:** the model may know this corpus's public fragments from
  pretraining. Mitigation: the corrupted-variant items are novel by
  construction and carry most of the primary criterion's weight.
- **Prompt-crafting bias:** whoever writes the S-arm context assembler
  wants S to win. Mitigation: both arms' selection rules are mechanical
  (BM25 / graph hops), fixed above, with no per-item hand tuning.
- **Small N:** 60 items bounds the detectable margin; that is why the
  pass threshold is 15 points, not 5. A near-miss is "not decided", never
  "passed" — no tolerance widening (CLAUDE.md, When a check fails).
