# Generated catalogues

`claims.jsonl`, `symbols.jsonl`, and `graph.jsonl` are emitted by
`workhouse index --write` (`make catalogue`). Do not edit them; a test fails if
any is stale.

`claims.jsonl` — one record per claim this repository can point at: every
invariant check, every registered constant, every ledger entry, every literature
edge, every Lean theorem, every ADR, and every registered integer sequence
(`SEQ:`). An `OEIS:A######` node exists only where a scan recorded a *hit*: a
miss is recorded in `ledger/sequences.yaml` and emits no node, because a node
with nothing to connect to is a strand and inventing an edge to tidy the census
is what the "no inferred edges" rule forbids. **Every field is copied from a curated
source.** There is deliberately no `summary`, `topics`, or `description` field:
a generated one-line gloss of a claim nobody wrote is the one place an error
could enter that no test can catch, and it would read like an index rather than
like a guess. A test asserts those fields stay absent.

`symbols.jsonl` — the curated aliases from `ledger/symbols.yaml`, joined to the
claims that mention them. The curated half lives in the YAML because it is
judgement; the join is derived.

`graph.jsonl` — one record per relationship between those records:
`{src, dst, type, how, source}`. Edge types are the verbatim field names of the
file each edge was read from, plus six derived extractions (`cites`, `mentions`,
`amends`, `retracts`, `uses`, and `carries` — the last two are the largest
derived families and were missing from this sentence until 2026-08-28). No inferred edges, no invented nodes: an
edge exists only when both endpoints resolve, and ADR 0007 records why.

Prefer `workhouse search` over reading these by hand — it resolves a query four
ways at once and knows about forbidden and repo-coined names. For everything
recorded about one id, `workhouse why C2`.
