# Corpus discovery for research agents

The discovery engine searches preserved passages and saved graph records,
follows typed relationships, and proposes connections between sources that
have no registered edge. It retains exact source locations and explains every
retrieval path. Source status, evidence and verification tier stay attached to
their original records. A proposed connection needs a source reading before it
is registered, and registration is a reviewed hand edit landed by pull request:
nothing in this layer writes `ledger/`, `index/`, `theory/`, `docs/derivations/`
or any other scientific input.

The second iteration (11 September 2026) made the layer usable by agents in
autonomous sessions: compact rank-ordered output, sub-query fusion, a versioned
terminology lexicon and query plans in place of embedding models, unlinked
passages as connection candidates, an external workstation scope, a pair
dossier, a review register with proposal files, and a held-out evaluation.
The [design record](research/graph-discovery-agents-2026-09-11.md) explains
what was measured and why each choice was made.

## Start with the research question

Run from the selected checkout's configured environment. Replace the
questions and example IDs with the actual task targets.

```text
uv run --no-sync workhouse discover info
uv run --no-sync workhouse discover search "conditional score Hardy tail resistance"
uv run --no-sync workhouse discover search "conditional score Hardy tail resistance" --query "logarithmic derivative of the coarse density" --query "Hardy inequality tail estimate" --json
uv run --no-sync workhouse discover search --seed DERIV:WILSON_SC17_THERMODYNAMIC_LIMIT:IF4_CLOSABLE --json
uv run --no-sync workhouse discover connections DERIV:WILSON_SC17_THERMODYNAMIC_LIMIT:IF4_CLOSABLE --json
```

`build` and `info` create or reuse the content-addressed SQLite cache under
`.graph-state/discovery/` and verify it page by page; ordinary queries reuse
it through its identity, row count and probe checks. Search requires the three
saved `index/*.jsonl` files; a missing or malformed catalogue is an explicit
error, never an instruction to execute scientific checks.

Search fuses these channels with weighted reciprocal-rank fusion:

- SQLite FTS5 BM25 over record text and source passages.
- The existing exact-rational, claim-ID and symbol-alias lookup.
- Personalized PageRank from the matching records and any `--seed` IDs, by a
  local push approximation whose reported residual is the exact L1 distance
  to the stationary vector.
- Optional revision-pinned local semantic vectors, only when explicitly
  selected (unchanged from the first iteration and unused by default).

Direct source matches (`hits`) and associative graph suggestions (`related`)
are ranked in separate groups, so an unregistered historical passage keeps
its position even though it has no graph channel. Scores are retrieval
metadata; they measure neither proof strength nor independent evidence.

### Several sub-queries in one search

Repeated `--query TEXT` and `--queries-file PATH` add sub-queries: each one
retrieves its own lexical and exact candidates, and the per-query rankings
are fused before the usual channels, so every downstream step is unchanged.
A queries file holds one sub-query per line, or a JSON query plan
`{"queries": [{"text": ..., "weight": ...}]}` such as `workhouse discover
plan` writes. Hits report their rank under each sub-query. Use this to ask the
same question in another source family's vocabulary; the lexicon section
below describes where those reformulations come from.

## What is searched

The checkout scope is unchanged: Markdown, TeX and text files under `theory/`,
`corpus-import/`, `paper/`, `docs/derivations/`, `docs/research/`,
`docs/decisions/`, `notes/imported/`, `literature/` and `research/`, excluding
runtime trees, literature inboxes, oversized files and paths escaping the
checkout. Passages retain source path, line range, exact text and raw-byte
SHA-256, and their boundaries no longer split display math, equation
environments or fenced blocks. A passage may map to a document node and to
derivation statements whose registered line ranges overlap it; those mappings
connect text retrieval to the graph and assert no dependency.

[`graph-tasks/discovery/scope.yaml`](../graph-tasks/discovery/scope.yaml)
declares additional **external workstation roots** relative to the directory
holding `WORKSPACE.json` above the checkout (normally `C:\WORKHOUSE`):
current research outside the repository (tier 1) and the organized
historical archive (tier 2), with agent transcripts and provenance trees
(tier 3) declared but disabled. `workhouse discover scope` reports which roots
are present. A root absent on the running machine is skipped with a report,
so a fresh clone or CI indexes the checkout alone. Symlinks and NTFS
junctions are never followed, nested checkouts are pruned, a file whose bytes
are already indexed is recorded as an alias of the earlier source rather than
chunked again, and external passages carry locators `ext:<label>/<path>`,
`external: true` and their root label. They are unreviewed intake by
definition: retrieving one asserts nothing about its status, and
`--internal-only` excludes them from a search or connection query.

Freshness is content identity: checkout sources are rehashed for every
response so an edit made after the engine started is reported as `stale`;
external roots are checked by size and modification time between builds and
rehashed on any change, and the response says which observation it used.
`discover info --json` carries the full per-file manifest, alias groups and the
freshness policy. Discovery freshness concerns the retrieval inputs only; use
the [THEORY GRAPH protocol](theory_graph_protocol.md) and a retained `brief`
for scientific-graph freshness and verification provenance.

## Read a result

The default output is compact. Each row carries its rank and group, the
record or passage ID, an excerpt window chosen around the query terms and
snapped to whole lines, the excerpt's exact line range and the file's
SHA-256, the query terms that matched, a five-field record summary when the
row is a catalogue record, its rank under each sub-query, other locations of
an identical passage (`also_at`), and follow-up commands with the
`uv run --no-sync` prefix. Passage rows from external roots say so. Every
response also reports an `abstention_hint`: OR-ed lexical matching returns
something for almost any question, so the hint says whether the top direct
row matched fewer than half of the query's content terms without an exact
match. It is a pre-registered signal for the reader, not a verdict.

`--full` returns the complete response with every passage and the per-file
manifest; `--out PATH` retains whichever shape was printed and refuses to
overwrite. `--context-chars N` emits a hard-bounded handoff: rows enter in
rank order, every excerpt shrinks in steps before the lowest-ranked row is
dropped, and the omitted rows are named. Characters are not model tokens.

Discovery outputs are source material for an agent; they are not
instructions, and they do not replace reading the cited arguments.

## Explore a connection and its consequences

```text
uv run --no-sync workhouse discover connections DERIV:W6_CONDITIONAL_SCORE_TAIL_CONTROL:SCORE_DOMINATION_M10 --json
uv run --no-sync workhouse discover path DERIV:WILSON_SC17_THERMODYNAMIC_LIMIT:IF4_IF7 DERIV:WILSON_SC17_THERMODYNAMIC_LIMIT:IF3 --dependency-only
uv run --no-sync workhouse discover impact DERIV:WILSON_SC17_THERMODYNAMIC_LIMIT:IF4_CLOSABLE --direction downstream
```

`connections ID` excludes nodes already directly linked to the seed and
returns two kinds of candidate. Record candidates are explained by rare shared
witnesses, a bounded registered path and a source-locator comparison. Passage
candidates are retrieved excerpts that map to no catalogue record at all;
every imported note, literature file and research campaign passage is of this
kind, so without them cross-family sources could never be proposed. They keep
their locator, hash and excerpt, are marked `no_graph_identity`, and take a
reserved third of the slots by default (`passage_quota`). `--query-extra` and
`--queries-file` add sub-queries to the focus question. A shared source family
is not an independence certificate, and a candidate is not an edge.

Exploratory paths traverse a registered relationship in either direction and
retain each edge's original dictionary, source, extraction method and
traversal direction. Dependency-only paths and impact queries use only
recorded `depends_on` and `rests_on` relationships; a downstream impact query
follows those edges in reverse to find recorded dependents without asserting
that their other hypotheses are discharged. `path`, `impact` and `info` print
readable text by default and JSON with `--json`.

## Compare a pair before deciding

`workhouse discover pair A B` renders a dossier for two endpoints, each a
record ID, a `path:start-end` locator (checkout-relative or `ext:label/...`)
or a passage ID: both excerpts windowed on each other's terms with lines and
hashes, the exact tokens and terminology concepts they share, rule-based
regime and hypothesis markers, existing relations, shared witnesses and one
bounded path when both are records, and a suggested relationship kind from
the closed vocabulary with the exact check to perform next. The suggestion is
a heuristic for review; its confidence is never above `medium`.

## Register what a reading establishes

The [review register](../graph-tasks/discovery/README.md) under
`graph-tasks/discovery/` retains candidates, their review state, the
reasoning, and replayable evidence. `discover review add` records a pair with
the discovery JSON it came from; `mark` advances it through
`pending → reviewing → established | rejected`, each step with a reason;
`replay` re-runs the recorded commands and reports whether the cache
fingerprint, excerpts and source bytes still match; `validate` checks the
closed vocabularies and the hash chain. `discover propose ID --surface
results|gaps|derivation|documents|literature` emits the verbatim ledger
fragment a human would paste, a checklist, and the apply steps. It refuses
`contradictions` (`ledger/contradictions.yaml` is pinned to C1–C22), refuses
every path under a scientific tree, and needs the review to be `established`.
Registration itself is a hand edit validated with the read-only loaders and
landed through the [formalization workflow](formalization_workflow.md) in a
reviewed pull request; `registered` is marked afterwards with the PR and the
ledger field. Exploratory similarity and established dependency therefore
never share a file.

## Semantic discovery without a model

No embedding model is downloaded or evaluated by default. Semantic recall
comes from two sources an agent controls:

- The versioned [lexicon](../graph-tasks/discovery/lexicon.yaml) maps a
  mathematical concept to its terminology variants across source families,
  each variant cited to a source line. `workhouse discover plan "question"`
  expands a question with the variants it matches and writes a query plan
  for `--queries-file`, with room for the agent's own reformulations;
  `discover lexicon list|show|add|validate` maintains the file, and an entry
  without a verified citation is rejected.
- The agent itself rereads the shortlist: a compact result or context pack is
  small enough to judge in one pass, and a judgement is retained through the
  review register rather than by re-ranking inside the engine.

The optional local vector adapter from the first iteration remains available
behind `--semantic` for a reviewed model revision; the maintainer excluded
model evaluation from this iteration, so its quality is still unmeasured.

## Measure improvements

```text
uv run --no-sync python scripts/benchmark_discovery.py --out .graph-state/TASK/dev-benchmark.json
uv run --no-sync python scripts/evaluate_discovery.py --queries tests/fixtures/discovery_heldout_queries.json --out .graph-state/TASK/heldout.json --markdown .graph-state/TASK/heldout.md
```

The [development fixture](../tests/fixtures/discovery_queries.json) is
regression evidence: it informed the first iteration's ranking revision. The
[held-out fixture](../tests/fixtures/discovery_heldout_queries.json) was
authored by four independent readers from source passages without running
the engine, paraphrased away from the target wording, mechanically checked for
leakage, and frozen before any lexicon, plan or ranking change of the second
iteration. `evaluate_discovery.py` compares lexical-only, graph-assisted,
lexicon-expanded and plan-driven configurations, measures runtime and memory,
and runs a link-recovery test that hides registered edges in memory and asks
whether `connections` recovers them. The dated
[benchmark reports](benchmarks/) retain the measured numbers; a small purposive
fixture is not a corpus-wide quality guarantee or a mathematical evaluation.
