# Working agreement

This repository is a verification layer over a scientific corpus. The usual
software instinct — make the failing check pass — is frequently **wrong** here.

This file is the rules. `AGENTS.md` is the posture — what the research is and
how to decide what to do next. `FRONTIER.md` is the current state, generated.
Read all three before changing anything; they are short on purpose.

## The one principle

**No document is authority. Only a machine check is.**

Text in `theory/`, `corpus-import/`, and `settlement/` states what someone
believed. Some of it was written with AI assistance and some of it is wrong —
this repository has already caught a reversed tensor-product identity, a
one-ulp transcription, a tolerance quoted tighter than its own data, and a
mechanism the author of this file proposed and then had to retract. Confidence
of phrasing carries no evidential weight.

So a claim's status is **computed, not asserted**:

| Tier | Meaning | Where it lives |
|---|---|---|
| **T0 proved** | Lean 4 compiles it, no `sorry`, standard axioms only | `lean/Workhouse/` |
| **T1 derived** | re-derived symbolically from stated definitions, exactly | `src/workhouse/invariants.py` |
| **T2 numerical** | float agreement within a stated tolerance | same, tolerance in the detail line |
| **T3 asserted** | a document says so and nothing checks it | `theory/`, the ledgers |

**T3 is the default for everything in the corpus.** Promoting a claim means
writing the check, not citing the sentence.

## Non-negotiables

1. **`theory/` is immutable evidence.** Never edit a source document to make a
   check pass. If a check disagrees with a document, the check has found
   something: record it. `theory/SHA256SUMS` pins the contents; changing it is
   a deliberate, reviewed event. `theory/superseded/` holds documents kept for
   the audit trail — never read one as current.

2. **Never promote a disputed value.** The off-axis coefficient `C_shp` is
   unresolved. Both sides are recorded side by side, and code must not pick
   one, average them, or prefer the exact rational because it looks more
   authoritative.

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

- `corpus-import/export/index/ENGINE_GOV_build_constants_index.py` — prose
  (`.md`, `.tex`), 322 files, magnitude floor 1000
- `src/workhouse/corpus_index.py` — code, certificates, notebooks and data
  (532 files), no magnitude floor, and cross-references the two

The second exists because the first cannot see the sealed core: `5/48`, `5/12`,
`5/612`, `11/306`, `7/102` have no entry in it, and `5/48` alone lives in 44
code files.

## Commands

```bash
make verify    # re-derive every exact claim (T1/T2)
make status    # contradiction and gap registers
make frontier  # regenerate FRONTIER.md — established / disputed / refuted / next
make check     # ruff + pytest, what CI runs
make lean      # T0: proof-check the Lean core (needs elan; see lean/README.md)
make manifest  # re-pin theory/ after a deliberate, reviewed corpus change

workhouse frontier --brief          # the block injected at session start
workhouse triage /path/to/archive   # survey an unpinned collection
```

`FRONTIER.md` is generated and checked in. A test fails if it is stale, because
a generated file that has drifted still reads as current.

## Adding a unifying candidate

`ledger/gaps.yaml` holds `unifying_candidates` — the claim that several results
are one mechanism. Each needs a **falsifier**: what would have to be exhibited
for the identification to fail. `ledger.validate` rejects one without it, and
that rule is the whole value of the list. A candidate with no falsifier is an
analogy, and analogies accumulate without ever being wrong.

## Adding an invariant

Register it on a suite in `src/workhouse/invariants.py`, cite the corpus
section, and return `(passed, detail)` where `detail` carries the numbers a
reader needs to argue with you. `tests/test_invariants.py` picks it up
automatically. If the statement is pure rational or polynomial algebra, prefer
promoting it to T0 in `lean/Workhouse/Basic.lean` instead.
