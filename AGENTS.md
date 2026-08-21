# Research mission

Three files, no overlap. `README.md` is the operating manual — reading order,
commands, how to add a check, what counts as done. `CLAUDE.md` is the
non-negotiables, and they bind. **This file is the posture**: what the work *is*
and how to decide what to do next.

## What this repository is

A verification layer over roughly four years of research on the SU(N) cubic
flux-band spectral program, developed iteratively with successive generations of
language models. The corpus is a **research history**, not a textbook: early
exploration, abandoned approaches, duplicated derivations, superseded formulas,
exact certificates, failed conjectures, corrections, and — in places —
mathematical structure that only emerged after years of iteration.

Some old files are wrong. Some new files are wrong. Age, filename, polish,
prose confidence, and which model wrote it are not evidence.

## What the job is

Not to summarize the corpus. To **continue the research program**: reconstruct
the strongest defensible structure, find what is actually unresolved, try to
break what looks solid, and derive new results where the evidence supports them.

The corpus is raw material. Do not assume the answer is already in it — but do
not assume it is absent either, because the measured failure mode here is
**re-deriving something that already exists under different notation**. Search
by value before concluding a result is new (see *Finding things* below).

## Evidence: use the vocabularies that exist

This is the one place the repository is opinionated, and it is worth being
precise about, because the natural six-level "proved / derived / numerical /
conjectured / asserted / refuted" ladder **collapses two axes that this corpus
deliberately keeps apart**.

Three vocabularies are already in use and all three are closed:

| Axis | Values | Where |
|---|---|---|
| **Verification tier** — what *this repo* has checked | T0 / T1 / T2 / T3 | `CLAUDE.md`, computed |
| **Claim status** — what the corpus asserts about truth | proven, conditional, disputed, open, superseded, falsified | `constants.STATUSES` |
| **Evidence level** — what the corpus ran to get it | analytic, cold-reproduced, output-certified, numerical, record-backed, prose-only | `constants.EVIDENCE` |

A claim can be `proven` in status and `record-backed` in evidence: the argument
is analytic but the artifact is missing. It can be `cold-reproduced` and still
`disputed`. Flattening those into one ladder loses exactly the distinction that
caught the fourth-order problems. **Do not introduce a fourth vocabulary.**
Extend `STATUSES` or `EVIDENCE` only alongside a change in the corpus's own
taxonomy, and add tiers never.

Two things stay true regardless of vocabulary:

- numerical agreement is not proof — `alpha_new` agrees to 2.4e-13 and misses
  the corpus's own 2.3e-13 bound;
- beautiful structure is not true structure — see ADR 0005, where a clean
  degree-bound mechanism for the tier collapse was proposed here and refuted
  here two hours later.

Never move a result up a ladder silently.

## Repetition is not independence

The single most useful sentence in any brief for this corpus: **repeated
statements are not independent evidence.** With 950 files and heavy copying,
consensus is manufactured by duplication. A value in forty files may have one
origin.

So when you count support, count **distinct originating computations**, not
files. The mechanics for that are already here:

- `workhouse.corpus_index` records every exact rational with the file, line, and
  source text, so you can see whether forty occurrences are forty derivations or
  one number pasted forty times;
- `corpus_registry.near_miss_pairs()` finds values that nearly agree — the sweep
  over the whole corpus returned exactly one pair, which was C20;
- `theory/superseded/` and the SHA-256 manifests make provenance chains
  followable rather than guessed.

Prefer `definitions → derivation → independent check → claim` over
`document A → document B quoting A → document C quoting B`. When two documents
disagree, that is a research problem, not a formatting problem. Reconstruct the
definitions, compare conventions, trace provenance, recompute. Then decide which
it is: different conventions, different anchoring, a transcription slip, an
approximation, a computational error, an incomplete derivation, a real
contradiction, or two different quantities being wrongly compared.

Resolve by mathematics, never by preference or recency. C1 was dissolved by
noticing that `q_band^(4)` and `m_Γ^(4)` are differently anchored coordinates —
not by picking the better-looking number.

## Finding things

`README.md` has the retrieval order and the search mechanics; do not re-derive
them here. The one thing worth repeating, because it is the thing agents get
wrong: the corpus is about 61 context windows, so reading it is not a plan, and
the join keys are **exact rationals, not concepts**. Search by value first —
`workhouse search` does that, and knows which names this repository coined and
which are forbidden.

## Prefer decisive calculations

Before an expensive run, ask what would settle it cheaply. In this program the
high-yield moves have been:

- evaluate at a high-symmetry point — `Φ_C(0) = 0` is why Γ-point data cannot
  constrain `Δ_C`, which is the whole shape of C2;
- symbolic `N` instead of a rank sweep;
- the smallest `L` that is not degenerate;
- an exact rational instead of a float — most "agreements" in this corpus are
  float coincidences until checked in `Rational`;
- a dimension or rank count;
- a parity or sign argument — `σ_n^phys = (-1)^n σ_n^raw` retired an entire
  class of sign disputes;
- one counterexample.

A cheap computation that eliminates a class of explanations beats a large one
that produces another coefficient.

## Try to break it

When something looks strong, attack it before defending it: smallest
counterexample, low rank, degenerate limit, boundary case, alternative
normalization, missing folded term, omitted subspace, hidden assumption,
finite-volume exception, known results in the literature.

A hypothesis that fails is recorded as failed — in the repository, with how it
failed. ADR 0005 is the pattern. Deleting a refuted claim destroys the evidence
that it was tried, and the reason it died usually narrows the next attempt.

## Watch the regime boundaries

finite lattice → infinite volume → continuum → physical observable.

Every crossing must be stated and either proved, tested, or marked as an
assumption. A theorem about a finite-dimensional effective Hamiltonian is not a
theorem about a continuum field theory. A protected lattice excitation is not a
particle. A perturbative coefficient is not a prediction outside its regime.
§12 of the governing document is the firewall; read it before any continuum
claim. G18 (the spectral bridge) and G19 (the continuum limit) are where this
program's largest unpaid debts sit.

## Look for the structure underneath

Ask actively whether separate results are one mechanism: symmetry, homology,
chain complexes, boundary operators, representation theory, invariant theory,
spectral geometry, Feshbach/resolvent constructions, linked-cluster
cancellation, conserved flux, graph structure, degeneracy, selection rules,
algebraic factorization.

`literature/index.yaml` is the external half of this: published results
indexed by the claim they bear on, queryable with `workhouse lit --for <id>`.
An external result counts because it is **independent** — produced without
knowledge of this program — not because it is published. It is T3 until
something checks it, same as any document here.

But distinguish analogy from derivation. If several results look like instances
of one principle, write the candidate general theorem down and say exactly what
would prove or falsify it. That statement is worth more than the analogy.

## Develop new mathematics when justified

Deriving identities the corpus does not contain, generalizing fixed-rank
results, finding exact forms for numerical sequences, sharpening bounds,
identifying minimal sufficient hypotheses, connecting separate observations,
designing decisive experiments — all in scope. Mark conjectures as conjectures
until something checks them, and when a claim of your own fails, retract it here
rather than in conversation.

Where a statement is pure rational or polynomial algebra, reducing it to a Lean
theorem is worth doing — not as ritual, but because a failed formalization
usually reveals the hypothesis the informal derivation omitted.

## The direction of travel

The goal is compression, not accumulation:

```
950 files  →  ~100 real results  →  ~20 structural principles  →  a few theorems
```

Progress is measurable. Today: 100 machine checks, 21 Lean theorems, 23
governing register items, 22 contradictions (one genuinely open: C2), 19 gaps
of which two are discharged (G1 largely, G2 fully — see their `status` fields),
and seven FINDING checks this repository holds against the corpus. Every
session should move at least one claim from T3 toward T1, or record why it
cannot be moved.

## Default loop

1. State the precise mathematical question.
2. Search by value and symbol, not by concept.
3. Separate independent sources from repetitions.
4. Reconstruct the strongest existing derivation and find what it rests on.
5. Try the cheapest falsification first.
6. Reproduce the calculation exactly, in rationals.
7. Compare rivals under one convention before judging them.
8. Look for the more invariant formulation.
9. State the strongest conclusion the evidence actually supports.
10. Record failures and open questions rather than tidying them away.
11. Say what the highest-value next operation is.
