# Full-root corpus coverage, 2026-09-07

This run establishes an auditable source inventory and review queue. It does
**not** establish that all mathematical content was reviewed, or promote a
Yang–Mills claim. The initial checkout and GitHub main both resolved to
`7957743917d11a62d873b6b3b72cf32bf03ba0a2`.

The [maintained coverage report](../../docs/corpus_coverage.md) explains the
scope and unresolved work. The canonical inventory is
[`notes/WORKHOUSE_FULL_2026-09-07.jsonl`](../../notes/WORKHOUSE_FULL_2026-09-07.jsonl).

## Snapshot and independent replay

The physical census contains 58,119 regular files, 17,612 unique byte streams,
and explicit infrastructure exclusions. Recursive archive reading adds 1,476
member-only streams. After explicit per-file/member exclusions, the complete
eligible union has **12,108 distinct contents**. It records every source path
and container chain, current quarantine locators, extraction limitations,
exact previous registrations and original review references.

```console
python scripts/verify_full_corpus_coverage.py --manifest notes/WORKHOUSE_FULL_2026-09-07.jsonl --run runs/full_corpus_coverage_2026-09-07
```

Run this from the repository root. Add `--workspace-root C:/WORKHOUSE` to
recheck the current bytes of all 36 quarantined/retained file pairs. Portable
CI verifies their identities in the independently pinned original census.
The coverage gate derives the expected content/path union from the frozen
inputs, checks metadata and rejects missing content rather than trusting the
output manifest's own count. The test suite includes corruption controls.

`COVERAGE_CONTRACT.json` records both compressed and decompressed input hashes.
The gzip inputs contain metadata, not extracted full texts. `SOURCE_COPY_MAP.json`
records copied original reports/scripts and any lossless compression. Frozen
sources keep their original filenames, dates and scope; some script paths refer
to the original local audit workspace. Regenerating a census requires those
sources and a fresh output directory. Replaying the coverage gate does not.

## What was extracted and what remains unread

The inventory has 8,938 text representations, 1,528 numeric-array header records,
1,307 image metadata records, 61 safe pickle opcode summaries, 243 audited
container records, six empty texts, 24 explicitly unsupported representations
and one Office owner-lock record. There are no unrecorded parser failures.
PDF equations/layout, image content and numeric data still need the review
appropriate to their mathematical use. Serialized Python objects were not
executed. Protected configuration and raw external papers were not published.

The original source paths and extraction locators describe a dated snapshot.
Mutable working paths may subsequently change; verify a digest before relying
on their present bytes. The archive's earlier source manifest still has 58
unresolved byte identities after 90 of its 148 entries were located. Sources
on other drives and unavailable historical exports were not presumed absent.

The existing notes register had 265 recorded verdicts and 1,572 pending
archive entries. The new inventory creates **zero new review verdicts**.
The queue now reuses 229 exact hashes with genuine prior reviews, preserving
the original archive, verdict and reason. Consequently 11,879 entries in this
new snapshot remain pending. A registered path alone does not remove a source
from the queue. The original staging report in `history/` predates this queue
repair and its 12,108-pending count is historical.

## Source review findings

- [Document and provenance audit](documentation/CORPUS_DOCUMENTATION_AUDIT.md):
  historical scope contradictions, missing/recovered source identities and
  meaningful versus merely asserted review evidence.
- [Synthesis review](documentation/SYNTH_COPY_REVIEW.md): 4,896 of 26,730 lines,
  two full reads and 17 partial reads, with exact unread intervals. It preserves
  valid conditional mechanisms and specific counterexamples/repairs. Eight
  finite algebra/counterexample controls pass; no blanket proof verdict follows.
- [Graph and mathematical-source review](graph/GRAPH_CORPUS_COVERAGE_REVIEW.md):
  current C2, all-rank and G18 status, exact registration coverage and four
  bounded source arguments bearing on the interacting comparison.
- [Archive intake](archives/ARCHIVE_INTAKE_REVIEW.md): all 27 supplied ZIP
  members already preserved, nested recovery and external-library provenance.
- [Recovered Lean review](archives/RECOVERED_LEAN_REVIEW.md): five complete
  source reads and independently recomputed integer data. No fresh Lean build
  or T0 promotion is claimed; physical-history premises remain explicit.

These reviews give candidates and precise failure locations for continued
G19/G23 work. They do not establish that no further mechanism exists in the
unread corpus, nor that the interacting scale theorem has been proved.

## Quarantine record

The maintainer requested moves without deletion. The 36 exact duplicates in
`capture/QUARANTINE_PLAN.json` were moved with verified original, destination
and retained digests; `capture/MOVES.jsonl` records the successful operations.
The local destination is `C:/WORKHOUSE/quarantine/2026-09-07-exact-duplicates`.
Unique research, original repositories and sealed evidence were not moved.
Redirect notes identify the retained loose proof and paper collections.

Historical or failed proofs remain research evidence. Neither unread status
nor membership in an old quarantine folder is a reason to discard their content.
