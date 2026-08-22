# 12. In-repo runs are pinned evidence, under runs/

Date: 2026-08-22. Status: accepted.

## Context

Until now every execution artifact in this repository was *received*:
`settlement/` vendors transcripts of runs performed elsewhere, and the
evidence vocabulary distinguishes them precisely (`cold-reproduced`,
`record-backed`). The settlement package recorded the marked-cluster
engine as absent, so nothing here could execute the G3 frozen protocol.

That record turned out to be stale. The corpus-import rename manifest
shows the engine arrived on 2026-08-20 as
`Hodge_SU3_Exact_MarkedCluster_m4_Colab.py` and was renamed to
`DATA_SU3_Exact_MarkedCluster_m4_Colab.py` by the import pipeline's
prefixing. Once located, the frozen protocol became executable *here*:
`freeze` passed (self-test 47/47, both preflight SHA pins reproduced),
and the first `run` stage ever executed fail-closed on cluster 1 of 609
(the shipped H0-closure cap; see G3 in the gaps ledger).

That produced a new kind of artifact: a transcript generated in this
repository by pinned code. It is stronger than received evidence — the
generating script AND the artifact are both present, so anyone can
re-run the generation — but it is still a transcript, and a transcript
that can drift silently stops being one.

## Decision

In-repo execution artifacts live under `runs/<name>/`, one directory per
run, each carrying its own `SHA256SUMS` covering every file in it and a
README stating exactly what was run, on what, and what it does and does
not establish. `tests/test_runs.py` verifies every run directory is
fully pinned. Checks that cite a run parse the pinned artifacts; the
heavy recomputation stays a documented one-command reproduction rather
than part of `make verify`.

The failure this prevents: quoting a number whose generating transcript
was edited after the fact — the same failure mode `theory/SHA256SUMS`
and `settlement/SHA256SUMS` exist to prevent, now covering artifacts we
generate ourselves.

## Consequences

- The evidence vocabulary is unchanged (no fourth ladder): a run here is
  simply what `cold-reproduced` always meant, with the generating script
  present instead of absent.
- Editing any file in a pinned run directory requires regenerating its
  `SHA256SUMS` in the same diff — deliberate and visible, exactly like a
  corpus re-pin.
- `RESUME_SECRET.json`-class credentials and multi-GB checkpoints are
  never vendored; the README of each run says what was withheld and why.
