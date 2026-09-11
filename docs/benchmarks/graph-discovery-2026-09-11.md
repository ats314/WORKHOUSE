# Theory graph discovery benchmark

11 September 2026. The final run found a listed relevant source in the first
ten primary results for **16 of 16 positive queries**, compared with **9 of 16**
for the original finder. The expanded lexical index also found all 16. These
are retrieval results on a small, source-reviewed fixture, not measurements
of mathematical validity or proof discovery.

The [compact JSON evidence](graph-discovery-2026-09-11.json) preserves exact
metrics, individual ranks, source and implementation hashes, and raw-artifact
digests. [Technique research](../research/graph-discovery-techniques-2026-09-11.md)
records the primary GitHub/Hugging Face sources, licenses, and design choices.

## Results at ten

| System | Queries with relevant hit | Recall at 10 | MRR at 10 | Mean warm-process query |
| --- | ---: | ---: | ---: | ---: |
| Original finder | 9/16 | 0.5625 | 0.3771 | 0.107 s |
| Expanded lexical index | 16/16 | 1.0000 | 0.6621 | 0.025 s |
| Discovery primary hits | 16/16 | 1.0000 | 0.6985 | 1.104 s |

All three exact catalogue controls rank first in every final system. All four
imported-source queries rank first in the expanded lexical and discovery
primary results. The absent-token control returns no primary result in every
system. There were zero query errors; saved graph input hashes were unchanged.

Recall here is the fraction of positive queries with at least one listed
relevant result. MRR is the mean reciprocal first relevant rank, with misses
and errors scored as zero. The negative control is excluded from those
denominators. Displayed numbers are rounded; the JSON retains full precision.

## Corpus scope and runtime

The final discovery index contains **17,382 saved records, 10,022 source
passages, and 29,302 saved edges**, with passages from **617 files**. The
original finder covers corpus-import, paper, and decision prose plus catalogue
records. Discovery additionally reaches theory, derivations, research notes,
imported notes, and other declared source roots. Improved coverage accounts
for part of the end-to-end gain. The same-expanded-index lexical comparison
helps separate that advantage from additional exact matching and source
diversity; it does not isolate a causal PageRank improvement.

The final run rebuilt the discovery index for its input fingerprint in
**9.297 seconds**. The original finder built its in-memory index in
**1.010 seconds**. The lexical comparison reused the already-built discovery
index. These are index construction timings; operating-system caches were
not cleared, so they are not cold-machine measurements.

Each system received one unscored warm-up, then each frozen query once in a
reused process. Complete discovery averaged **1.104 seconds** per query,
including related graph suggestions and input-freshness checks. The original
finder averaged **0.107 seconds**, and the expanded lexical query alone
averaged **0.025 seconds**. Complete discovery therefore improves retrieval
coverage here while taking more time than the original finder. Concurrent
repository validation may affect these single-run timings.

## Primary matches and graph suggestions

Related graph suggestions are a separate result band and do not enter the
primary metrics. The final run returned **80 suggestions** across the
positive queries; five queries had a listed relevant source in that band.
This fixture evaluates retrieval of selected sources, not the overall
quality or mathematical meaning of suggested graph connections.

The initial implementation fused graph scores into primary matches.
Registered records could receive both lexical and graph contributions, while
unregistered historical passages received lexical contributions alone.
The initial run found only **12 of 16** relevant sources with that combination,
although its expanded lexical index found all 16. Separating primary matches
from graph suggestions corrected that structural channel-availability bias.

The full initial regression remains preserved at the originating worktree's
local path:

    .workhouse-local/graph-discovery-benchmark/result-01.json

The complete final raw report is retained at:

    .workhouse-local/graph-discovery-benchmark/result-final.json

Both raw reports remain local artifacts outside ordinary clones. Their
SHA-256 digests and the relevant aggregate evidence are in the compact JSON.

## Per-query first relevant ranks

The [frozen fixture](../../tests/fixtures/discovery_queries.json) contains query
text, expected IDs or source paths, text markers, and source-review rationales.
Query text is not repeated in this publication.

| Query ID | Original finder | Expanded lexical | Discovery primary |
| --- | ---: | ---: | ---: |
| ground_derivative_budget | 5 | 2 | 2 |
| rare_fiber_transport_obstruction | miss | 5 | 5 |
| thermodynamic_cylinder_gradient | 1 | 2 | 1 |
| current_factorization_without_inverse | 4 | 3 | 3 |
| three_coordinate_anisotropy | 4 | 4 | 3 |
| hardy_conditional_score_tails | 3 | 3 | 3 |
| global_gaussian_reference_failure | 1 | 1 | 1 |
| matrix_mass_atom_persistence | miss | 1 | 1 |
| upper_decay_not_atom_lower_bound | miss | 1 | 1 |
| literal_wilson_source_frame | miss | 1 | 1 |
| blocked_zero_momentum_interface | miss | 1 | 1 |
| historical_signed_incidence | miss | 7 | 7 |
| historical_stranded_flux_zero_backend | miss | 3 | 3 |
| exact_rank_three_coefficient | 1 | 1 | 1 |
| exact_channel_difference | 1 | 1 | 1 |
| exact_plaquette_regular_graph | 1 | 1 | 1 |

## Provenance and limits

The fixture was chosen by reading source passages before viewing any new
engine rankings. Its SHA-256 remained unchanged from the initial through
final runs. The architecture was revised after inspecting the initial
results: the final scores are development-regression evidence, not an
untouched independent test set. Relevant sources are not exhaustively
annotated, and historical-source relevance does not endorse a source's
current scientific status.

The JSON pins the fixture, reviewed source files, implementation files, saved
indexes, and discovery corpus fingerprint. Implementation hashes still
matched when this publication was exported. The measured implementation had
uncommitted changes over the recorded base commit; file hashes identify the
tested bytes. No scientific graph generation, Python research check, or Lean
compilation was executed by the benchmark itself.

Run [the benchmark script](../../scripts/benchmark_discovery.py) explicitly
with a new output path to reproduce the procedure. It refuses to overwrite
earlier reports. The metric unit tests use synthetic data and do not run the
full research corpus.
