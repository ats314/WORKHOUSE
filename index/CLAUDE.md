# Generated catalogues

`claims.jsonl`, `symbols.jsonl`, and `graph.jsonl` are emitted by
`workhouse index --write` (`make catalogue`). Do not edit them; a test fails if
any is stale.

`claims.jsonl` — one record per claim this repository can point at: every
invariant check, registered constant, ledger entry, literature study, Lean
theorem, located derivation statement, reviewed archive record and ADR. Claim
wording and scope come from authored sources; mechanical verdicts and joins
come from the verifier. There is deliberately no `summary`, `topics`, or
`description` field:
a generated one-line gloss of a claim nobody wrote is the one place an error
could enter that no test can catch, and it would read like an index rather than
like a guess. A test asserts those fields stay absent.

`symbols.jsonl` — the curated aliases from `ledger/symbols.yaml`, joined to the
claims that mention them. The curated half lives in the YAML because it is
judgement; the join is derived.

`graph.jsonl` — one record per relationship between those records:
`{src, dst, type, how, source}`. Edge types are the verbatim field names of the
file each edge was read from, plus mechanically derived relationships. The
`how` and `source` fields identify whether an edge is curated or derived and
where it came from. Documentary `technical_appendix`, `navigation` and
`provenance` links come from `ledger/documents.yaml`; they do not make the
historical ALL THEORY collection the active checkout. Both endpoints must
resolve during validation. Shared vocabulary is not a dependency (ADR 0007).

Selected derivation routes emit `targets` to their exact objective and
`blocked_by` to explicitly authored completion inputs within that route.
Neither edge means every solution of the parent gap must use that route.
`bears_on` remains relevance. Curated priorities and their source status are
rendered in FRONTIER section 7 and in text/JSON `workhouse why` output.
Cached queries use their supplied catalogue snapshot; `--live` selects a
fresh catalogue. Proof tier and missing Lean coverage do not determine
whether an analytic target is complete.

Derivation source dependencies are curated in
`ledger/derivation_statements.yaml`. Its whole-statement `lean` entries produce
`LEAN -> DERIV formalizes`; scoped `lean_support` ingredients produce
`DERIV -> LEAN supported_by`. The source `DERIV:` node remains T3 independently
of its mathematical status. A linked Lean certificate does not promote every
claim in its source document.

`LEAN -> LEAN depends_on` edges come from `ledger/lean_dependencies.json`.
The strict exporter reads elaborated proof and type constants, traversing local
helpers to the next registered theorem. These edges describe kernel proof use;
the curated `DERIV:` dependencies describe the mathematical source argument.
Keep the two explicit, and preserve their direction and provenance in exports.

Prefer `workhouse search` over reading these by hand — it resolves a query four
ways at once and knows about forbidden and repo-coined names. For everything
recorded about one id, `workhouse why C2`.

## Regenerate from the inputs

Follow the [formalization workflow](../docs/formalization_workflow.md) after Lean
or statement-registry changes: refresh the strict kernel export first, then the
derivation proof map, then catalogue/frontier/certified. A stale dependency
export or changed derivation hash is a source-review problem; do not bypass it
by editing generated JSONL. `atlas.html` is a local rendered view and is not
checked in.

Review the affected `workhouse why` routes and the generated diff. Check
catalogue, graph and proof-map freshness when their inputs changed. For changes
only to this guide, follow [documentation maintenance](../docs/documentation_maintenance.md)
and leave generated scientific files alone. Coordinate exact-path commits with
other agents and report whether the resulting commit is local, pushed or merged.
