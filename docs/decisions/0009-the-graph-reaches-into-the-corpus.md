# 9. The graph reaches into the corpus

Date: 2026-08-21

## Status

Accepted. Extends the substrate of ADR 0007.

## Context

The claim graph stopped at the repository's edge. `workhouse why C15` could
show every check, constant, theorem, symbol, and ADR bearing on a claim — but
not the corpus document the claimed value actually comes from. The G5 session
had to re-establish by hand that the tetrahedral row originates in one
transcript, that the mobility theorem originates the admission of the missing
artifact, and that the cube row's temporal classes originate in one derivation
record — and none of that judgement had anywhere durable to live. With 928
heavily copied files, originator-vs-carrier is the load-bearing distinction:
**repetition is not independence**, and a value in forty files may have one
origin.

## Decision

A fourth curated crosslink file, `ledger/provenance.yaml`, following the
symbols/theorems pattern exactly — judgement in the YAML, the join derived,
validation mechanical:

- an entry names one corpus document, its **corpus pin** (the sha256 must
  equal `corpus-import/SHA256SUMS`, so a corpus change breaks the register
  loudly), a role from a closed set, and a curated `meaning`;
- each `originates` item names a catalogue target, what of it the document
  originates, and an **observed quote near a recorded line** — the same
  observed-not-invented discipline as `symbols.yaml`'s corpus spellings;
- the catalogue gains `DOC:` records (kind `document`, tier **T3** — a
  document is still only a claim); the graph gains curated `originates`
  edges; `workhouse why` and `workhouse search` reach both with no new code.

The curation rule, and the whole value of the register: **originators only,
never carriers.** A document belongs here because a session established that
it is a distinct originating statement or computation — not because it
mentions the value. What is machine-checked is the provenance (this pinned
file says this, here); the truth of what it says stays with the checks.

## Consequences

- `workhouse why C15` now shows the transcript that asserts the value and the
  theorem note that admits the artifact is missing, alongside the checks that
  re-derived it — the full chain from corpus assertion to T0/T1 standing in
  one neighborhood.
- The register is seeded with the four documents whose originator role the
  G5 session verified (the final-theory transcript, the mobility theorem
  note, the prismatic cap notebook, and transcript 818). The concept is that
  every theory pass appends the originators it establishes, the same way it
  appends checks.
- `tests/test_provenance.py` makes rot loud: a moved file, a drifted quote,
  a renamed target, or a corpus re-pin each fail a named assertion.
