# Working agreement

This repository is a verification layer over a scientific corpus. The usual
software instinct — make the failing check pass — is frequently **wrong** here.

## Non-negotiables

1. **`theory/` is immutable evidence.** Never edit the source documents to make
   a check pass. If a check disagrees with a document, the check has found
   something: record it, do not silence it. `theory/SHA256SUMS` pins the
   contents; changing it is a deliberate, reviewed event.

2. **Never promote a disputed value.** The off-axis coefficient (C2) is
   unresolved. Both sides are recorded side by side, and code must not pick one,
   average them, or quietly prefer the exact rational because it looks more
   authoritative.

   C1 is *not* in that category: `q_band^(4)` and `m_Gamma^(4)` are differently
   anchored coordinates, not rival estimates. Use those names — writing "two
   `m_4` values" regenerates a contradiction that does not exist. See ADR 0002.

3. **Exact stays exact.** Corpus rationals are `sympy.Rational`. Values the
   corpus records only as floats are Python floats and carry a `_NUM` suffix.
   A float that reads as exact is the single most dangerous bug in this
   codebase; `tests/test_constants.py` guards the boundary.

4. **Never apply a `4**r` rescaling.** The archived `Y = 2β/3 = 4u` line is a
   definition-label erratum (C4). The printed coefficients were already in the
   canonical coordinate `u = β_lat/6`. Rescaling them corrupts every order.

5. **Status and evidence are independent.** A claim can be analytic yet rest on
   a disputed input; a cold run can be numerically precise without proving a
   theorem. "Certified" is never a synonym for "proved". The vocabularies in
   `constants.STATUSES` and `constants.EVIDENCE` are closed — extend them only
   with a corresponding change to the corpus's own taxonomy.

## When a check fails

Work in this order:

1. Re-read the corpus section the check cites. The definition there controls.
2. Reproduce the disagreement in isolation and quantify it — ulps, absolute
   gap, relative gap. "Close" is not a finding; `3.0e-15 = 31 ulps` is.
3. Decide which of three things it is: a bug in the check, a transcription slip
   in the registry, or a real discrepancy in the corpus.
4. For the third, add it as an explicit `FINDING:` check that asserts the
   discrepancy, and write it into the README and the relevant ledger entry.
   Never widen a tolerance to make a finding disappear.

## Adding an invariant

Register it on a suite in `src/workhouse/invariants.py`, cite the corpus
section, and return `(passed, detail)` where `detail` carries the numbers a
reader needs to argue with you. `tests/test_invariants.py` picks it up
automatically — there is no separate test to write.

## Commands

```bash
make verify    # re-derive every exact claim (also: workhouse verify -v)
make status    # contradiction and gap registers
make check     # ruff + pytest, what CI runs
```
