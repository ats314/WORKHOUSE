# Generated catalogues

`claims.jsonl`, `symbols.jsonl`, and `graph.jsonl` are emitted by
`workhouse index --write` (`make catalogue`). Do not edit them; a test fails if
any is stale.

`claims.jsonl` — one record per claim this repository can point at: every
invariant check, every registered constant, every ledger entry, every literature
edge, every Lean theorem, every ADR, every pinned originating document, every
reviewed note. **Every field is copied from a curated source.** There is deliberately no `summary`, `topics`, or `description` field:
a generated one-line gloss of a claim nobody wrote is the one place an error
could enter that no test can catch, and it would read like an index rather than
like a guess. A test asserts those fields stay absent.

`symbols.jsonl` — the curated aliases from `ledger/symbols.yaml`, joined to the
claims that mention them. The curated half lives in the YAML because it is
judgement; the join is derived.

`graph.jsonl` — one record per relationship between those records:
`{src, dst, type, how, source}`. Edge types are the verbatim field names of the
file each edge was read from, plus four derived extractions (`cites`,
`mentions`, `amends`, `retracts`). No inferred edges, no invented nodes: an
edge exists only when both endpoints resolve, and ADR 0007 records why.

Prefer `workhouse search` over reading these by hand — it resolves a query four
ways at once and knows about forbidden and repo-coined names. For everything
recorded about one id, `workhouse why C2`.
