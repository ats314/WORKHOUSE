# Immutable evidence

**Never edit a file in this directory.** Not to fix a typo, not to make a check
pass, not to update a superseded reference. `SHA256SUMS` pins every byte and
`tests/test_theory_sources.py` will fail. If a check disagrees with a document,
the check has found something — record it as a `FINDING:` invariant.

## What is current

`README.md` is the map. In short: the v4.3 stack is authority, the coefficient
appendix is still at v3.1, and `superseded/` is kept for the audit trail and
**must never be read as current** — including
`MASTER_THEORY_UNIFIED_2026-08-20_v3.md`, which upstream's own path index marks
`quarantine_only`.

`governance/` describes upstream's tree, not this one. It names directories that
do not exist here; it is kept so a cited path resolves.

## Citing a section

Section numbers are per document and they are not interchangeable. `§5.5` and
`§4.4` exist in `superseded/MASTER_THEORY.md` only — the governing document has
no such sections. `§18.1` and `§18.3` are the detailed formula document. When
you cite, name the document.

## Promoting a version

Move the old stack to `superseded/`, land the new one, run `make manifest`, and
extend `tests/test_theory_sources.py`. That test re-extracts §14 from both
versions and requires the new register to *extend* the old without retracting
anything — if a future version really does retract an item, the failure is the
record that it happened.
