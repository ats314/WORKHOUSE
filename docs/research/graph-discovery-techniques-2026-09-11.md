# Graph discovery techniques and evaluation design

11 September 2026. Engineering research for overlooked connections in the
WORKHOUSE corpus. This note records primary-source findings and implementation
choices. It adds no mathematical dependency, claim-status change, or tier.

## Integration choice

Use saved claims and edges as inputs to a separate retrieval layer. Combine
exact identifiers and rational values, lexical passage search, and propagation
through a weighted graph projection. Keep original edge direction, type,
source, and extraction method. Scores rank reading candidates; they do not
measure proof strength or independent evidence.

Return source passages, explicit chains of existing edges, channel
contributions, and commands to inspect the original records. Primary matches
use the direct retrieval channels; a separate related section presents graph
suggestions. An unregistered historical passage must not lose its direct-match
position merely because registered claims can receive an additional graph
score. Similarity may
suggest a relationship for review; it does not write a new dependency. Shared
copied prose is not independent support. General documentation hubs should
have weaker influence than precisely scoped mathematical connections.

The implementation uses small independently written algorithms. No upstream
source snippets are vendored and none of the full RAG frameworks below is a
required dependency. Model scores remain optional inputs whose provenance and
actual corpus performance require separate evaluation.

## Primary sources reviewed

### HippoRAG: propagation from relevant facts

[HippoRAG](https://github.com/OSU-NLP-Group/HippoRAG) uses the
[MIT license](https://github.com/OSU-NLP-Group/HippoRAG/blob/main/LICENSE).
In [`src/hipporag/HippoRAG.py`](https://github.com/OSU-NLP-Group/HippoRAG/blob/main/src/hipporag/HippoRAG.py),
`run_ppr` takes a restart distribution and damping parameter, invokes weighted
igraph personalized PageRank on an undirected projection, and extracts passage
scores. `graph_search_with_fact_entities` combines fact and passage relevance
to construct restart weights and penalizes frequent entities.
`add_synonymy_edges` incrementally searches new entities against existing
embeddings using nearest neighbors and a similarity threshold.

The reusable idea is associative retrieval from relevant seeds across several
steps. WORKHOUSE keeps proof directions intact; any reverse traversal is an
explicitly labeled navigation projection. Its existing curated graph makes
HippoRAG's complete LLM extraction and generation stack unnecessary here.

### LightRAG: separate entity, relationship, and passage retrieval

[LightRAG](https://github.com/HKUDS/LightRAG) has an
[MIT license](https://github.com/HKUDS/LightRAG/blob/main/LICENSE).
[`QueryParam`](https://github.com/HKUDS/LightRAG/blob/main/lightrag/base.py)
separates local, global, hybrid, and mixed retrieval and gives entity,
relationship, and total context separate budgets.

[`_perform_kg_search`](https://github.com/HKUDS/LightRAG/blob/main/lightrag/operate.py)
retrieves entities from low-level keywords, relations from high-level keywords,
and passages from the query. It batches embeddings and keeps chunk-source
tracking. The inspected merge uses round-robin interleaving, not reciprocal
rank fusion. The useful principle is that a relation is searchable information
with its own evidence source, rather than an unlabeled line between nodes.

### BM25s: efficient local lexical candidates

[BM25s](https://github.com/xhluca/bm25s) has an
[MIT license](https://github.com/xhluca/bm25s/blob/main/LICENSE).
[`bm25s/__init__.py`](https://github.com/xhluca/bm25s/blob/main/bm25s/__init__.py)
provides BM25 construction, tokenized indexing, retrieval, and saved indexes.
Results can carry the caller's original metadata dictionaries.

Mathematical identifiers and fractions should survive tokenization as join
keys. The original WORKHOUSE finder already implements BM25: adding that
algorithm alone would not be new functionality. The improvement must come
from coverage, indexing, graph-aware retrieval, explanations, and measured
results against that baseline.

### Haystack: reciprocal-rank fusion

[Haystack](https://github.com/deepset-ai/haystack) uses the
[Apache-2.0 license](https://github.com/deepset-ai/haystack/blob/main/LICENSE).
The inspected reference is
[`_reciprocal_rank_fusion`](https://github.com/deepset-ai/haystack/blob/main/haystack/utils/misc.py);
[`DocumentJoiner`](https://github.com/deepset-ai/haystack/blob/main/haystack/components/joiners/document_joiner.py)
provides a public wrapper with per-channel weights.

The rule adds contributions proportional to weight divided by 60 plus the
one-based rank. It avoids equating BM25, PageRank, and cosine score scales.
WORKHOUSE's independently written implementation also deduplicates channels
and reports their contributions. Installing Haystack is unnecessary for this
small algorithm.

### Hugging Face: optional semantic candidates and reranking

[BAAI/bge-small-en-v1.5](https://huggingface.co/BAAI/bge-small-en-v1.5) is marked
MIT, with 384-dimensional embeddings and a 512-token context. Its model card
provides SentenceTransformer and Transformers usage, normalization, and query
instructions. Raw similarity thresholds require calibration on actual data.

[cross-encoder/ms-marco-MiniLM-L6-v2](https://huggingface.co/cross-encoder/ms-marco-MiniLM-L6-v2)
is marked Apache-2.0 and demonstrates CrossEncoder prediction over query and
passage pairs. It was trained for MS MARCO passage ranking and can rerank a
shortlist. These models were inspected but not downloaded or run during this
source research. Their mathematical retrieval quality remains unmeasured.
Model revision, normalization, chunking, and corpus hashes must accompany
imported scores.

## Frozen evaluation

The [query fixture](../../tests/fixtures/discovery_queries.json) was selected by
reading source passages before viewing new engine rankings. It contains seven
derivation queries, four imported-source queries, two historical theory-section
queries, three exact catalogue controls, and one absent-token control. Each
positive query retains source locators and a rationale. Relevance labels do
not endorse a historical source's current scientific status.

[`benchmark_discovery.py`](../../scripts/benchmark_discovery.py) explicitly
reads saved graph files and passes the catalogue to the original finder. It
never calls collection or executes registered checks. Missing saved inputs
fail before retrieval. Both systems receive identical frozen queries and
cutoffs. An expanded-index lexical variant is reported separately.

Run from the selected checkout, using a new result path:

```text
python scripts/benchmark_discovery.py --limit 10 --out .workhouse-local/discovery-benchmark/result-01.json
```

The JSON retains query and saved-graph hashes, index provenance, setup time,
warm-process query time, per-query results, errors, and grouped metrics. It
refuses to overwrite prior output. Recall at k means the fraction of positive
queries finding at least one listed relevant hit; it is not exhaustive document
recall. Mean reciprocal rank uses the first relevant position, scoring misses
and errors as zero. Negative controls have a separate denominator.

The original finder covers fewer source directories. Gains can reflect
expanded coverage, chunking, tokenization, source quotas, or ranking. The
lexical variant uses the same expanded index. Its comparison with primary
engine hits measures additional exact matching and source diversity. Related
graph suggestions are retained separately and never count toward primary
hit metrics. Do not present either comparison as an isolated causal PageRank
gain.

This small purposive fixture is not a corpus-wide quality estimate. It does
not measure proof discovery, mathematical truth, novelty, or another agent's
downstream success. Preserve disappointing rankings. Future evaluations should
add independently written queries and held-out curated links, excluding target
identifiers from query features to prevent leakage.

## Confidence and remaining work

APIs, algorithms, and license labels were inspected in primary code and model
cards. Suitability for this corpus is an engineering inference. GitHub links
use moving default branches; attempted web API requests did not recover exact
upstream revisions. Pin revisions and retain notices before future vendoring.

The metric tests use synthetic hits and fixture validation only. Whole-corpus
benchmark results belong in retained JSON artifacts, so this research note
does not acquire stale performance claims.
