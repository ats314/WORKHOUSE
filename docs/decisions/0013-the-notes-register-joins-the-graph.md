# 13. The notes register joins the graph

Date: 2026-08-28

## Status

Accepted. Extends the substrate of ADR 0007, following the pattern of ADR 0009.

## Context

ADR 0007 built `index/graph.jsonl` because relationships between records were
siloed across formats, and ADR 0009 extended it into the corpus with
`ledger/provenance.yaml`. The notes register (`ledger/notes.yaml`, the
maintainer's archive under review) arrived after both, and grew the same kind
of siloed relationships the graph exists to join: 116 reviews, of which 51
`extract` verdicts carry the mandatory `bears_on` field naming the claims the
note's content entered through — 58 recorded note→claim edges into G18 and
G20–G23, none of them visible to `workhouse why` or the atlas. `why G23` could
not show the 32 reviewed notes that entered it, and the reasons recorded on
`set-aside` verdicts — some of the sharpest curated judgements here, such as
the rebuttal of the unproved "exact nonabelian Markov coarse-graining forces
commutativity" no-go — were unreachable by `workhouse search`.

## Decision

1. **Every review is a catalogue record**: `NOTE:<digest12>` (the register's
   own short-digest labeling), kind `note`, tier **T3** — a review promotes
   nothing. The verdict is the status, the mandatory reason is the detail, the
   archive and full digest sit in `cites` so a search by digest resolves. An
   `import`'s `where` is its `imported_to` path; every other review points at
   the register itself. Set-asides join too: the reason is the point.

2. **The graph gains curated `bears_on` edges** `NOTE:<digest12> → target`,
   the verbatim field name, source `ledger/notes.yaml`, with the same target
   space as literature `bears_on` (ledger ids or registered constant names).

3. **What deliberately does not join.** Unreviewed manifest rows are inventory
   lines, not judgements — 1,597 nodes nothing curated would swamp the claim
   graph, so a note becomes a node only when a review exists. The note-to-note
   fields (`duplicate_of`, `superseded_by`) stay in the register: their far
   end is usually an unreviewed manifest row, the graph invents no nodes, and
   `notes.validate()` already checks those references against the manifests.

NOTE-id uniqueness rests on 12-hex digest prefixes; a collision (including a
same-digest review in a second archive) fails
`test_catalogue_ids_are_unique` loudly rather than merging two records.

## Consequences

- `workhouse why G21` now shows the reviewed notes that entered it beside the
  checks and papers that bear on it; `why NOTE:<digest12>` shows one review's
  verdict, reason, and targets; the atlas draws notes and corpus documents as
  their own legend groups instead of lumping them under "ledger claims".
- The catalogue grows by one record per review and the graph by one edge per
  recorded `bears_on` target; both stay staleness-tested via `make catalogue`.
- In the same change, `workhouse index --write` builds the catalogue once and
  threads it through claims, graph, and validation — it had been running the
  full check suite three times per regeneration for identical results.
