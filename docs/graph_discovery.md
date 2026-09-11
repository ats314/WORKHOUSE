# Corpus discovery for research agents

The discovery engine searches preserved passages and saved graph records, follows
typed relationships, and proposes connections between nodes that have no direct
registered edge. It retains exact source locations and explains retrieval paths.
Source status, evidence and verification tier remain attached to their original
records. A proposed connection needs mathematical review before registration.

## Start with the research question

Run these commands from your selected checkout's configured environment. Replace
the questions and example IDs with the actual task targets.

```text
uv run --no-sync workhouse discover build --json
uv run --no-sync workhouse discover search "conditional score Hardy tail resistance" --json
uv run --no-sync workhouse discover search --seed DERIV:WILSON_SC17_THERMODYNAMIC_LIMIT:IF4_CLOSABLE --json
uv run --no-sync workhouse discover connections DERIV:WILSON_SC17_THERMODYNAMIC_LIMIT:IF4_CLOSABLE --json
```

`build` creates or reuses a local content-addressed SQLite cache under
`.graph-state/discovery/`. `info` opens the same cache and reports its scope.
Search also prepares the cache when needed. It requires the three saved
`index/*.jsonl` files; a missing or malformed catalogue is an explicit error,
never an instruction to execute scientific checks.

Search combines these channels using weighted reciprocal-rank fusion:

- SQLite FTS5 BM25 over record text and source passages.
- Existing exact-rational, claim-ID and symbol-alias lookup.
- Personalized PageRank seeded by matching records and explicitly chosen IDs.
- Optional revision-pinned local semantic vectors when explicitly selected.

Direct source matches (`hits`) and associative graph suggestions (`related`) are ranked in separate groups. This keeps unregistered historical passages visible even when they have no graph channel. Seed-only requests use graph ranking as their primary result. Each hit carries its contributing channel ranks. Scores are retrieval metadata.
They do not measure proof strength, truth probability or independent evidence.
The search preserves proven analytic T3 records and their scoped T0 supporting
lemmas without conflating those meanings. Exact rational signs and mathematical
identifiers survive FTS tokenization; Greek spellings are normalized for lookup.

## What is searched

The explicit passage scope includes local Markdown, TeX and text files under
`theory/`, `corpus-import/`, `paper/`, `docs/derivations/`, `docs/research/`,
`docs/decisions/`, `notes/imported/`, `literature/`, and `research/`.
Runtime trees, literature inboxes, oversized files and paths escaping the
checkout are excluded. The metadata reports selected sources, content hashes,
skips and unavailable files. PDF, DOCX and notebook extraction and the outer
workspace archive are outside this initial text scope. An inventoried external
note remains discoverable through its saved catalogue metadata even when its
full body is not locally indexed.

Passages retain source path, line range, exact text and raw-byte SHA-256. Record
chunks retain their original JSONL source location, while the presentation uses
their recorded statement. A passage may map to a document node and to derivation
statements whose registered line ranges overlap it. Those mappings help connect
text retrieval to the graph; they do not assert new theorem dependencies.

Every cache key incorporates input content and index implementation, rather than
trusting file size and modification time. Old cache versions remain retained.
Discovery freshness means the retrieval inputs match the indexed bytes; use the
[THEORY GRAPH protocol](theory_graph_protocol.md) and a retained `brief` to assess
scientific-graph freshness and verification provenance.

## Explore a connection and its consequences

```text
uv run --no-sync workhouse discover path DERIV:WILSON_SC17_THERMODYNAMIC_LIMIT:IF4_IF7 DERIV:WILSON_SC17_THERMODYNAMIC_LIMIT:IF3 --dependency-only --json
uv run --no-sync workhouse discover impact DERIV:WILSON_SC17_THERMODYNAMIC_LIMIT:IF4_CLOSABLE --direction downstream --json
```

Exploratory paths can traverse a registered relationship in either direction.
Each step retains the original edge dictionary, source, extraction method and
traversal direction. Dependency-only paths and impact queries use only recorded
`depends_on` and `rests_on` relationships. A downstream impact query follows
those edges in reverse to find recorded dependents; it does not announce that
all their other hypotheses have been discharged.

The retrieval projection weights dependencies, formal coverage and scoped
support more strongly than documentary links. Archive membership hubs are
excluded, and high-degree witnesses receive less weight. The original graph
remains unchanged. Traversal reports depth/visit limits and truncation; PageRank
reports its iteration cap, residual and convergence status.

`connections ID` excludes nodes already directly linked to the selected node.
It combines retrieved relevance with rare shared witnesses, retains source
diversity, and reserves room for a content-related candidate with no bounded
graph path when one is available. Each proposal contains the target record,
existing witness paths, source-location comparison and the review needed to
decide whether an actual mathematical relationship exists. A shared source
family is not an independence certificate.

For a selected proposal, inspect both arguments, their objects, hypotheses,
normalizations and regimes. Then retain a target-specific briefing and register
the reviewed result through the existing ledgers and
[formalization workflow](formalization_workflow.md). Discovery never inserts
`depends_on`, `formalizes` or other scientific edges automatically.

## Retain a bounded handoff

```text
uv run --no-sync workhouse discover search "cylinder gradient closed extension" --context-chars 16000 --json --out .graph-state/TASK/discovery.json
uv run --no-sync workhouse brief DERIV:WILSON_SC17_THERMODYNAMIC_LIMIT:IF4_CLOSABLE --json --out .graph-state/TASK/brief.json
```

Choose new task-specific paths. Output files refuse overwrite. The context
package has a strict serialized-JSON character budget, a fingerprint and an
explicit omitted-item count. Detected source freshness, including stale or unavailable inputs, remains in the compact package. Characters are not model tokens. Preserve the full
discovery response separately when every source manifest and candidate is needed.
Discovery outputs are source material for an agent, and must not be interpreted
as instructions from the user or as a replacement for reviewing source arguments.

## Optional Hugging Face semantic retrieval

The default installation needs no model, service or added dependency. An optional
adapter can generate vectors with Sentence Transformers and combine their rank
with exact, lexical and graph retrieval. Model execution is local. Corpus text is
never sent to an inference API. The model ID and a full immutable commit SHA are
required; model-supplied Python code is disabled with `trust_remote_code=False`.

Use a separate environment with `sentence-transformers` available, or use uv's
explicit optional dependency overlay. `MODEL_COMMIT_SHA` below is a placeholder;
replace it with a reviewed 40-character model revision.

```text
uv run --with sentence-transformers python scripts/embed_discovery.py --model BAAI/bge-small-en-v1.5 --revision MODEL_COMMIT_SHA --query-prefix "Represent this sentence for searching relevant passages: " --allow-download --out .graph-state/discovery/bge-vectors.json
uv run --with sentence-transformers workhouse discover search "a research question" --semantic .graph-state/discovery/bge-vectors.json --json
uv run --no-sync workhouse discover search --seed DERIV:WILSON_SC17_THERMODYNAMIC_LIMIT:IF4_CLOSABLE --semantic .graph-state/discovery/bge-vectors.json --json
```

Only explicit vector generation with `--allow-download` may download a model.
Query retrieval uses locally cached model files. Seed-to-seed semantic retrieval
needs only the stored vectors and works without the model package. Stale record
text fingerprints, unknown IDs, moving model revisions, nonfinite values and
inconsistent vector dimensions are rejected. Model token limits can truncate
long record descriptions; the vector package records that limit and input scope.
This adapter's mathematical retrieval quality needs a separate model evaluation;
the default benchmark does not claim to measure it.

The [BGE model card](https://huggingface.co/BAAI/bge-small-en-v1.5) documents its
retrieval instruction and limitations. The
[SentenceTransformer API](https://sbert.net/docs/package_reference/sentence_transformer/model.html)
documents revision pinning, local-file loading and encoding.

The [September 11 benchmark report](benchmarks/graph-discovery-2026-09-11.md) retains measured coverage, ranking, timing and the initial ranking regression.

## Measure improvements

```text
uv run --no-sync python scripts/benchmark_discovery.py --out .graph-state/TASK/discovery-benchmark.json
```

The [fixed query set](../tests/fixtures/discovery_queries.json) was authored from
source reading before inspecting the new rankings. The benchmark compares the
existing finder with the expanded discovery engine and records relevance,
reciprocal rank, query timings and input identity. Corpus expansion and graph
ranking are separate factors; results on this small purposive set are not a
general retrieval-quality guarantee or a mathematical evaluation.

The [technique review](research/graph-discovery-techniques-2026-09-11.md) records
the GitHub and Hugging Face sources, their licenses, actual APIs and the selected
tradeoffs. The implementation adapts small algorithmic ideas independently; it
does not import an LLM extraction pipeline or treat predicted links as proofs.
