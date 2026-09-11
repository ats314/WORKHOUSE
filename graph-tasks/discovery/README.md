# Discovery review register

`workhouse discover` returns reading candidates. A candidate becomes a
registered relationship only after someone reads both arguments and a human
lands a reviewed edit in a scientific ledger. This directory holds the record
between those two events: what was compared, what was concluded, which
evidence was read, and — once a human has landed it — where it landed.

It lives under `graph-tasks/` because that is the one tree no catalogue
collector, check cache, briefing fingerprint or discovery source root reads.
A record here cannot become a graph edge, cannot invalidate a cached check and
cannot be retrieved as a passage. The failure this prevents: a review reading
as evidence. Nothing in this workflow writes under `ledger/`, `index/`,
`theory/`, `corpus-import/`, `lean/`, `docs/derivations/`, `docs/decisions/`
or `paper/`, and the tool refuses an `--out` path in any of them.

Two subdirectories:

- `reviews/` — one YAML file per review, schema `workhouse-discovery-review/v1`,
  written only by `workhouse discover review add` and `mark`.
- `proposals/` — one YAML file per emitted proposal, schema
  `workhouse-discovery-proposal/v1`, written by `workhouse discover propose`.
  A proposal is text for a human to paste; it registers nothing.

Both are versioned like any other file here. The full CI suite runs on a
change to them (only `*.md` under `graph-tasks/` takes the documentation fast
path), which is intended: a review record is a claim about what was read.

## A review record

```text
uv run --no-sync workhouse discover search "conditional score Hardy tail" --json --out .graph-state/TASK/search.json
uv run --no-sync workhouse discover review add --seed RESULT:W6_COMPACT_CONDITIONAL_SCORE_TAIL_CONTROL --target docs/derivations/w6-conditional-score-tail-control.md:120-160 --kind reusable-ingredient --note "the compact tail bound is the input of the interval repair; same normalization of the score" --reviewer claude-fable-5-1 --evidence .graph-state/TASK/search.json
```

Fields, and the rule each one enforces:

| Field | Rule and the failure it prevents |
| --- | --- |
| `seed`, `target` | A record id from `index/claims.jsonl` (or `SYM:` symbol) or a passage locator `path:start-end` that points at an existing UTF-8 file with a sane line range. Both are checked on `add` and on `validate`, so a review cannot name something that does not exist. |
| `relationship_kind` | Closed: `shared-operator`, `compatible-hypothesis`, `reusable-ingredient`, `equivalent-construction`, `scope-restriction`, `disagreement`, `literature-bearing`, `documentary`, `unrelated`. A free-text kind lets "related" stand in for a dependency. |
| `state` | Closed: `pending → reviewing → established | rejected`, then `established → registered`. No step is skippable, so nothing is called established without a recorded reading step, and no state is ever silently reverted. `rejected` and `registered` are terminal. |
| `reasoning`, `reviewer` | Mandatory. An unattributed or unreasoned review cannot be questioned later. `--reviewer` may come from `WORKHOUSE_REVIEWER`. |
| `created`, `updated`, `history[].at` | ISO-8601 with offset, from `--timestamp`, `WORKHOUSE_REVIEW_TIMESTAMP` or the clock. The register is ordered by creation; `add` refuses a timestamp earlier than the last record and `mark` refuses one earlier than the last history entry. |
| `history` | Every transition with its reason. `registered` additionally needs `--registered-as` naming the PR or commit **and** the ledger id and field the relationship landed on, supplied by the human who landed it. |
| `evidence` | Per discovery JSON passed with `--evidence`: the reconstructed `argv`, the discovery cache `fingerprint` observed when the review was recorded, the rows naming the seed or target in compact form, `source_hashes` (path, lines, SHA-256 of the file bytes in this checkout), and `excerpt_sha256` over the copied excerpts. When no row names the pair, the top rows are copied and `selection` says so. |
| `previous`, `genesis`, `sha256` | The hash chain, below. |

The record never carries a `status`, `evidence` level or `tier` of its own.
Those belong to the claims it names and stay where they are.

## The hash chain

Borrowed from append-only journals. `genesis` is the SHA-256 of the fields
fixed at creation (`schema`, `id`, `seed`, `target`, `relationship_kind`,
`reasoning`, `reviewer`, `created`, `evidence`, `previous`); `previous` is the
`genesis` of the preceding review in creation order, or `null` for the first;
`sha256` covers the whole record as the tool last wrote it. Hashes are over
canonical JSON of the loaded values, so re-flowing the YAML by hand changes
nothing, while editing a value, flipping a state, deleting a record or
backdating one is reported by:

```text
uv run --no-sync workhouse discover review validate
```

Chaining the creation hash rather than the file bytes is what lets a record
change state through `mark` without breaking every later link. The chain is
tamper-*evident*, not tamper-proof: anyone can recompute it. Its job is to make
an unrecorded edit visible in review, not to authenticate an author.

## Advancing and proposing

```text
uv run --no-sync workhouse discover review list [--state established] [--json]
uv run --no-sync workhouse discover review show <id>
uv run --no-sync workhouse discover review mark <id> --state reviewing --reason "read both derivations"
uv run --no-sync workhouse discover review mark <id> --state established --reason "same operator, same normalization, regime finite volume"
uv run --no-sync workhouse discover propose <id> --surface results
```

`propose` needs state `established` and refuses kind `unrelated` (a recorded
negative has nothing to register). It writes
`proposals/<id>-<surface>.yaml`, or `--out PATH` outside every scientific
tree, containing:

- the verbatim YAML fragment for one surface — `results` (`depends_on`,
  `bears_on` or a `supported_by` item with a `scope` to fill), `gaps` (a new
  `unifying_candidates` entry with the next `U` id and a falsifier placeholder
  that **must** be filled: `ledger.validate` rejects an empty one, and that rule
  is the whole value of the list), `derivation` (`depends_on` or a
  `lean_support` item), `documents` (`cites` or `bears_on`), `literature`
  (`bears_on` item; `disagreement` fixes the relation to `contradicts`);
- a checklist: hypotheses compared, regime stated, normalization compared,
  independence of origin checked, falsifier stated, source hashes matched. Only
  the last is filled in by the tool, from the file bytes in the checkout;
- the review's evidence, and the apply steps.

`--surface contradictions` is refused with the reason: `ledger/contradictions.yaml`
is a verbatim transcription of the corpus's register, pinned by tests to
C1–C22 with zero open items. A disagreement is recorded as a literature
relation `contradicts`, a route `cannot_decide`, or a unifying candidate with
`status: refuted`.

Applying a proposal is a hand edit of the named file — one field per proposal,
everything else untouched — followed by the read-only validators
(`uv run --no-sync workhouse status`; `results.load()`;
`derivation_statements._checked()`; `workhouse lit` for literature) and the
documented regeneration order inside a reviewed pull request. After the merge,
`mark <id> --state registered --registered-as "<PR or commit> <ledger id and field>"`
closes the record. The tool never runs `workhouse index`, `verify` or `make regen`.

## Replaying evidence later

A review names what was read, not what is true now. A later agent checks
whether the evidence still reads the same:

```text
uv run --no-sync workhouse discover review replay <id> [--json]
```

For every evidence entry it re-runs the recorded `argv` through
`uv run --no-sync workhouse ...` with `--json`, then reports per entry:
`fingerprint` (the discovery cache the replay used versus the recorded one),
`excerpt_sha256` (the rows naming the pair, re-selected and re-hashed), and
each recorded source as `matched`, `changed` or `missing` from the file bytes
now. Exit code 0 means everything matched, 2 means something changed, 1 means
a replay could not run. A match says the inputs are the same bytes; it does
not re-establish the review, and a change does not refute it — it says the
reading must be repeated before the proposal is applied.

## What this register is not

It is not a fourth claim vocabulary (ADR 0007, ADR 0015 lineage: the states
are on review records, never on claims), not a source of graph edges, not a
place for scientific results, and not a substitute for the dated task record
described in [the graph-tasks README](../README.md). A retrieval score or a
shared vocabulary is not evidence; the review's reasoning has to say why the
two arguments are the same object under the same hypotheses.
