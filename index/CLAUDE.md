# Generated catalogues

`claims.jsonl` and `symbols.jsonl` are emitted by `workhouse index --write`
(`make catalogue`). Do not edit them; a test fails if they are stale.

`claims.jsonl` — one record per claim this repository can point at: every
invariant check, every registered constant, every ledger entry, every literature
edge. **Every field is copied from a curated source.** There is deliberately no
`summary`, `topics`, or `description` field: a generated one-line gloss of a
claim nobody wrote is the one place an error could enter that no test can catch,
and it would read like an index rather than like a guess. A test asserts those
fields stay absent.

`symbols.jsonl` — the curated aliases from `ledger/symbols.yaml`, joined to the
claims that mention them. The curated half lives in the YAML because it is
judgement; the join is derived.

Prefer `workhouse search` over reading these by hand — it resolves a query four
ways at once and knows about forbidden and repo-coined names.
