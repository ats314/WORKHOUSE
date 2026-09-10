# Working agreement

This repository is a verification layer over a scientific corpus. The usual
software instinct — make the failing check pass — is frequently **wrong** here.

This file is the rules. `AGENTS.md` is the posture — what the research is and
how to decide what to do next. `FRONTIER.md` is the current state, generated.
Read them with the README and CERTIFIED before changing scientific claims.
For documentation work, use the
[maintenance guide](docs/documentation_maintenance.md); for proof work, use the
[formalization workflow](docs/formalization_workflow.md).

## Select the checkout and preserve the work

Use [workspace operations](docs/workspace_operations.md) as the shared operating
contract for local and GitHub agents. It defines startup observations, source
intake, cooperative file ownership, shared writers and preservation at closeout.

Use the shared [THEORY GRAPH protocol](docs/theory_graph_protocol.md) for graph
interpretation. Run `workhouse brief --startup`, retain the task's target
briefing, and keep a [manual task record](graph-tasks/README.md). Agent adapters
must link to that protocol rather than maintain separate graph meanings.

The workstation's active checkout is `C:\WORKHOUSE\REPO`; the outer workspace
and `ALL THEORY` contain preserved collections. Follow
[workspace coordination](docs/workspace_coordination.md), inspect local changes
and refresh the remote history before choosing a base or declaring a result
absent. Do not create another checkout inside an archive collection.

The maintainer's organization instruction is **do not erase anything**. Keep
source bytes, failed routes, duplicates, archives and uncommitted work. Preserve
the original bytes and path/hash record before revising maintained navigation,
as described in the maintenance guide. Reuse an existing preservation record
only when it matches the bytes being revised. Do not reset, clean, deduplicate
or move the research archive as part of routine organization.

Coordinate owned files when agents share a checkout. Use exact paths for staging
and commits; inspect both the working diff and staged diff so another agent's
work is not included accidentally. Isolate independent work where needed and
preserve concurrent changes when reconciling branches.

## The one principle

**A claim is established by its proof or computation under explicit
hypotheses. Its artifact must not claim more than that argument establishes.**

Text in `theory/`, `corpus-import/`, and `settlement/` states what someone
believed. Some of it was written with AI assistance and some of it is wrong —
this repository has already caught a reversed tensor-product identity, a
one-ulp transcription, a tolerance quoted tighter than its own data, and a
mechanism the author of this file proposed and then had to retract. Confidence
of phrasing carries no evidential weight.

The repository's machine-verification tier is computed, not assigned by
confidence. It is distinct from mathematical status and evidence:

| Tier | Meaning | Where it lives |
|---|---|---|
| **T0 proved** | Lean 4 compiles it, no `sorry`, standard axioms only | `lean/Workhouse/` |
| **T1 derived** | re-derived symbolically from stated definitions, exactly | `src/workhouse/invariants/` |
| **T2 numerical** | float agreement within a stated tolerance | same, tolerance in the detail line |
| **T3** | the full statement has no dedicated repository machine certification | source documents and curated analytic results |

**T3 is the default for machine certification.** An analytic result may
nevertheless be `proven` with `analytic` evidence when its derivation works.
Record the theorem, hypotheses, source and dependencies in `ledger/results.yaml`
and use `ledger/derivation_statements.yaml` for located derivation groups;
do not invent a Lean or exact-computation certification for its unformalized
steps. Conversely, a successful finite test does not prove a general theorem.
Novelty, publication, and the agent's prior familiarity decide neither case.

## The maintainer's rule

Rules accumulate, and some will be bad — written by an agent for a case that
no longer exists, then obeyed forever. So, from Alex, the maintainer: **use
common sense. If a rule seems stupid, it probably is — but neither silently
obey it nor silently break it. Argue with the failure mode it cites, and if
all else fails, ask Alex.** Every rule in this repository is supposed to name
the failure it prevents; one that doesn't is a candidate for removal, by pull
request, where the diff is visible.

## Non-negotiables

1. **`theory/` is immutable evidence.** Never edit a source document to make a
   check pass. If a check disagrees with a document, the check has found
   something: record it. `theory/SHA256SUMS` pins the contents; changing it is
   a deliberate, reviewed event. `theory/superseded/` holds documents kept for
   the audit trail — never read one as current.

2. **Never promote a disputed value.** A dispute closes by derivation or
   not at all: both sides stay recorded side by side, and code must not pick
   one, average them, or prefer the exact rational because it looks more
   authoritative. The off-axis coefficient `C_shp` (C2) closed that way on
   2026-09-04 — every cluster of the rotation record is the historical
   pipeline's own number, and the one that is not is explained ordering by
   ordering (ADR 0024). Its two recorded values stay in the registry with
   their verdicts.

   The `Γ` scalars are *not* in that category: `q_band^(4)` and `m_Γ^(4)` are
   differently anchored coordinates, not rival estimates. Use those names —
   writing "two `m_4` values" regenerates a contradiction that does not exist.
   See ADR 0002.

3. **Exact stays exact.** Corpus rationals are `sympy.Rational`. Values the
   corpus records only as floats are Python floats and carry a `_NUM` suffix.
   A float that reads as exact is the single most dangerous bug here;
   `tests/test_constants.py` guards the boundary.

4. **Never apply a `4**r` rescaling.** The archived `Y = 2β/3 = 4u` line is a
   definition-label erratum. The printed coefficients were already in the
   canonical coordinate `u = β_N/(2N)` (`β_3/6` is the SU(3) specialization).
   Rescaling them corrupts every order.

5. **Status and evidence are independent.** A claim can be analytic yet rest on
   a disputed input; a cold run can be numerically precise without proving a
   theorem. "Certified" is never a synonym for "proved".

## When a check fails

1. Re-read the corpus section the check cites — but read it as a *claim*.
2. Reproduce the disagreement in isolation and quantify it — ulps, absolute
   gap, relative gap. "Close" is not a finding; `3.0e-15 = 31 ulps` is.
3. Decide which of three it is: a bug in the check, a transcription slip in the
   registry, or a real discrepancy in the corpus.
4. For the third, add an explicit `FINDING:` check that asserts the
   discrepancy, and write it into the README and the ledger. **Never widen a
   tolerance to make a finding disappear.**

## When your own claim fails

Retract it in the repository, not just in conversation. Keep the failed attempt
and record how it failed — ADR 0005 exists because a proposed mechanism died on
one uncounted projection, and that is more useful to the next attempt than
silence. Deleting a refuted claim destroys the evidence that it was tried.

## Finding things

The join keys of this corpus are **exact rationals, not concepts**. No semantic
search retrieves `109151/249696` from a natural-language query. Two indexes
cover it:

- `corpus-import/export/index/ENGINE_GOV_build_constants_index.py` — the
  historical prose index (`.md`, `.tex`), with a magnitude floor
- `src/workhouse/corpus_index.py` — code, certificates, notebooks and data,
  with no magnitude floor and cross-references to the prose index

The second exists because the first cannot see the sealed core: `5/48`, `5/12`,
`5/612`, `11/306`, `7/102` can be absent from the prose index while their
computations are present in code files.

`workhouse why <id>` is the front door: one query, everything recorded about
a claim — both sides of a dispute, every check with its verdict, what each
check rests on, the routes tried and which are dead, and the corpus files
that carry a value. Every file `corpus-import/` pins is a graph node (ADR
0016), so `why <path>` works on a corpus file too. `workhouse search` is
the front door to the two indexes above, plus the claim catalogue and the
curated aliases in `ledger/symbols.yaml`. It matches by *value* rather than
spelling (`-10/96` finds `-5/48`), and it carries two warnings a grep cannot:
forbidden names (`m_4`) and names coined here that the corpus never uses
(`Phi_C`, which the corpus writes as `4e_2/q_a`).

## Complete the result, then land your own green work

For each research iteration, include its consequence for the governing
[Clay objective](docs/research_goal.md): which obligation changed and what
the new result enables. Record mathematical scope and repository landing
status separately. A count of successful checks cannot replace that account.

A research result is not finished while it lives only in a response, run
directory, or branch. Before handoff:

1. Record the precise statement, hypotheses, regime and proof source. Preserve
   original received and sealed evidence; correct current interpretations in
   maintained ledgers and navigation, with links to the historical stage.
2. Update the relevant claim and route states. Give established analytic
   results stable `RESULT:` ids in `ledger/results.yaml`; declare actual
   `depends_on` inputs, downstream `bears_on` connections, and the narrow
   scope of each `supported_by` control. Link completed routes with
   `closed_by` and open successor routes with their inputs. A keyword match
   or a shared gap does not establish a mathematical dependency.
3. Update `README.md`, `docs/current_research.md`, and other affected current
   documentation. Search relevant live check descriptions for the old claim
   or open-task wording. Keep frozen proof sources and dated reports as
   evidence of their stage; their latest status belongs in the current map.
4. Register every new Lean theorem in `ledger/theorems.yaml`, including
   helper lemmas, and import its subject module from `lean/Workhouse.lean`.
   Locate its source statement and map full coverage or scoped support as
   described below. Run the strict dependency exporter and refresh the proof
   map before `make regen` (catalogue, frontier, certified, in that order).
   Inspect
   `workhouse why` for the changed results and gap, and complete the required
   verification below. Generated views are never edited by hand.
5. Push the tested commit, inspect its CI and reviews, and merge when green.
   Confirm the merge and the presence of the result and graph changes on
   GitHub `main`. State separately whether work is local, pushed, or merged.

From Alex, 2026-08-29: agents were leaving green PRs open, waiting for a
review that was never coming. So: **when your PR is green — CI passing, no
merge conflict, no unaddressed review comment — mark it ready and merge it
yourself.** Do not wait for a human to press the button. The failure this
prevents: verified work stranded in open PRs while the branch drifts.

Verification follows the changed inputs. Scientific or executable changes need
the applicable regression checks, `make check` and `make verify`; Lean changes
also need the strict build and refreshed dependency export. Regenerate views
when their source inputs changed. For a documentation-only change, inspect the
diff, resolve relative links, check documented commands against their actual
entry points and run the documentation checks in the maintenance guide. Do not
rerun research or rewrite generated scientific evidence merely to edit prose.
Required remote CI must still pass before merging; a red or conflicted PR is
yours to fix, never to merge.

Recheck the remote base and exact head before merging so concurrent agents'
changes are included. Use the normal PR merge path without bypassing branch
protection, keep independent work in isolated branches/worktrees, and resolve
conflicts without discarding another agent's work. If CI or review identifies
a concrete failure, fix it and rerun the affected checks. A green PR needs no
extra human button press unless the user has explicitly requested review-only
work or a repository protection requires it.

On 2026-09-05 a completed proof and regenerated graph remained in draft
PR #98 after all checks passed. The repository's `main` page therefore looked
unchanged. The completion rule includes merging and verifying `main` to
prevent that same failure recurring.

## Commands

Query IDs, search values and filters below are examples. Select them from the
user's task; `G19` is not a default or required research target. Follow the
[shared protocol](docs/theory_graph_protocol.md) for target selection and snapshots.

```bash
make verify    # run every registered mathematical check (T1/T2)
make status    # contradiction and gap registers
make frontier  # regenerate FRONTIER.md — established / disputed / refuted / next
make certified # regenerate CERTIFIED.md — every checked claim, ranked by tier
make catalogue # regenerate index/ — claims.jsonl, symbols.jsonl, graph.jsonl
make lit       # published work, and which claim each paper bears on
make check     # ruff + documentation links + pytest; CI Python entry point
make lean      # T0: proof-check the Lean core (needs elan; see lean/README.md)
make manifest  # re-pin theory/ after a deliberate, reviewed corpus change

workhouse verify --only 'h_4^side'  # re-establish ONE claim, with its numbers
workhouse verify --tier 1           # only the exact re-derivations
workhouse brief --startup           # shared protocol notice; no calculations
workhouse brief G19 --json          # saved target snapshot; inspect freshness
workhouse frontier --brief          # supplementary frontier summary
workhouse why C2                    # everything recorded about one claim id
workhouse derive C2 G3 --out f.md   # evidence chains as Markdown, registered edges only
workhouse branches C2               # every conflicting value, both branches side by side
workhouse export -o graph.json      # claims+symbols+edges as one versioned JSON envelope
workhouse triage /path/to/archive   # survey an unpinned collection
workhouse notes                     # the notes register: reviewed vs pending, per archive
workhouse notes --queue             # the next notes to review, highest signal first
workhouse ask "<question in words>" # candidate finder over corpus prose and the catalogue; T3, ends in `why`
workhouse cache --clear             # the per-check result cache the collectors use (never `verify`)
```

`FRONTIER.md` and `CERTIFIED.md` are generated and checked in. A test fails if
either is stale, because a generated file that has drifted still reads as
current.

`CERTIFIED.md` is the answer to "what is the best-established thing here, and
how do I check it myself?" — every claim ranked by tier, every row carrying its
own reproduction command. Point a reader seeking verification there first.

## Connect derivations to formal proofs

`ledger/derivation_statements.yaml` uses `derivation-statements/v1`: native
`CITE:` document identity, raw source SHA-256, exact locators and anchors,
stable `DERIV:` statement IDs, hypotheses, curated source dependencies and
explicit remaining work. In a statement record, `lean` lists whole-statement
proofs; `lean_support` lists a theorem and the precise ingredient it proves.
The graph emits `LEAN -> DERIV formalizes` for the former and
`DERIV -> LEAN supported_by` for the latter. Supporting a statement never
silently promotes the full statement's machine-verification tier.

`ledger/theorems.yaml` inventories every theorem. Keep `promotes` empty unless
the theorem proves the entire named check. Use a suitable module under
`lean/Workhouse/`, including analytic modules; `Basic.lean` is not the default
destination for every proof. Establish the actual object, domain and limit
hypotheses needed by the source, or record exactly what remains unformalized.

`python scripts/export_lean_dependencies.py` strictly builds Lean and exports
elaborated type/proof constants and transitive axioms into
`ledger/lean_dependencies.json`. Registered theorem dependencies traverse local
helpers and stop at the next registered theorem. The loader checks them against
the declaration records and source fingerprints; identifiers mentioned in
comments are not proof dependencies. Lean fingerprints normalize line endings
only (`utf8-lf`); derivation fingerprints preserve received bytes. Do not edit
the export to make a stale-source or axiom failure disappear.

After proof or registry changes, follow the regeneration order in the
[formalization workflow](docs/formalization_workflow.md), including
`python scripts/render_derivation_coverage.py`. The generated
[proof map](docs/derivation_formalization.md) supplies current coverage counts;
keep changing counts out of agent rules. Mathematical source dependencies and
kernel proof dependencies answer different questions and must remain distinct.

## The notes archive

The maintainer's own research notes — three years of them — enter through the
same discipline as published papers, via `ledger/notes.yaml` and `notes/`
(see `notes/README.md`): declared, inventoried by content digest, reviewed
with a closed verdict vocabulary and a mandatory reason per verdict. An
`import` is byte-verified against its digest; an `extract` must name the
claims it entered through; `set-aside` is a recorded judgement, never a
deletion. No verdict promotes anything past T3.

## Adding a unifying candidate

`ledger/gaps.yaml` holds `unifying_candidates` — the claim that several results
are one mechanism. Each needs a **falsifier**: what would have to be exhibited
for the identification to fail. `ledger.validate` rejects one without it, and
that rule is the whole value of the list. A candidate with no falsifier is an
analogy, and analogies accumulate without ever being wrong.

## Adding an invariant

Register it on a suite in `src/workhouse/invariants/`, cite the corpus
section, and return `(passed, detail)` where `detail` carries the numbers a
reader needs to argue with you. Declare the checks it takes as inputs with
`rests_on=(...)` so the graph can say what falls if one is refuted, and return
an exact value it establishes as a third element `{NAME: value}` so `workhouse
search` can reach it by value (a float needs the `_NUM` suffix, as in the
registry). `tests/test_invariants.py` picks it up automatically. Formalize
reusable mathematical statements in the appropriate Lean module when possible,
with the source scope and registration described above. A finite computation
remains useful evidence even when the associated analytic theorem requires
additional arguments.

## Recording an attempt

A gap's `plan` steps in `ledger/gaps.yaml` are routes, each with a `state`
from `untried | live | dead | done`. When a run or a finding closes one, set
the state and name the closer in `closed_by`; when an instrument is
structurally unable to reach a claim, say so in `cannot_decide`. The failure
this prevents: a dead route reading as open work, which cost four sessions on
G3. `workhouse why <gap>` prints the routes; see ADR 0015.
