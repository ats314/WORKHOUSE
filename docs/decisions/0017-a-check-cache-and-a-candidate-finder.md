# 17. A per-check result cache, and a natural-language candidate finder outside the tiers

Date: 2026-09-01. Status: accepted.

## Context

Two costs were measured on 2026-09-01. A full `verify` runs 265 checks in
about four minutes; a regeneration of the views runs them three times over and
loops the catalogue to a fixpoint, ten minutes; the test suite fifteen. A
session that edits one check pays the whole bill on every regeneration, and
this session hit the stale-index cycle twice waiting for it. Separately, the
exact-rational search is the right front door for a value and no front door at
all for a question, and the 2026-08-28 agent experience note asked for a
semantic surface with one condition: candidates only, promoting nothing.

## Decision

**Cache.** `check_cache.CheckCache` memoises each check's `Result` on disk
outside the repository, keyed on a fingerprint of every input a check can
read: the whole `src/workhouse` tree, the ledgers, the pinned paper, the runs,
the literature, the notes register, `theory/`, the ADRs, the Lean tree, and the
corpus through its manifest. Any edit anywhere invalidates everything, which
costs one four-minute run and never a stale verdict. The generated `index/` is
keyed separately and only for checks whose source names it, so the catalogue's
fixpoint loop does not invalidate the other checks on each pass. The
collectors — catalogue, CERTIFIED.md, FRONTIER.md — use it. `workhouse verify`
never does: that command is the promise to re-derive, and a cached verdict is
not a re-derivation; a test reads the code to hold that. `WORKHOUSE_NO_CACHE=1`
disables it; `workhouse cache --clear` empties it. CI has no cache and runs
everything live, which is what makes the cached views trustworthy: the
staleness tests hold them equal to a live build at every commit.

**Finder.** `workhouse ask "<question>"` ranks chunks of the corpus prose, the
pinned paper sources, the ADRs and every catalogue record by BM25, prints each
hit with its file and line or its catalogue id and `why` command, and says on
every run that it is T3. It is lexical rather than embedded on purpose: no
model, no download, no new dependency, deterministic on every machine, and the
join keys of this corpus are tokens (`5/48`, `C_shp`, `t_N`) that an embedding
would blur. Nothing in the evidence layer reads it: the finder is an external tool in
the sense of ADR 0010, and enters under that rule, outside the tiers. If a
semantic backend ever earns its weight it goes behind the same interface, as
an optional extra, and under the same rule. The cache serves the graph
substrate of ADR 0007 and changes no edge in it.

## Consequences

A warm regeneration takes seconds. A question in words has a front door that
ends in `why`. Neither changes what is established: the cache renders the same
verdicts the tests already pin, and the finder finds documents that were T3
before it and are T3 after.
