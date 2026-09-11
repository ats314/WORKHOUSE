# Discovery evaluation

- Status: ok
- Evidence: Development fixture: regression evidence only, not held-out evidence.
- Fixture: `C:\WORKHOUSE\worktrees\discovery-agents-20260911\tests\fixtures\discovery_queries.json` sha256 `8f94958ea28412e540d73cdc318da4eb69059466c4812e868f1840c9eb513e2c` (17 queries, 16 positive, 1 negative)
- Git HEAD: `fdaadc40381e59e95a6f114b1079eec37a5e41a8`; dirty paths: 4
- Discovery cache: `52c54e76f96d5413edf69155bb70a77fdffc8baf895d776539fd3174787556fe` freshness matched (sources rehashed for this call; external files stat-checked and rehashed on change)
- Sources were rehashed for the unscored warm-up query only; engine.recheck_freshness was then set to False for every scored query.

## Configurations

| configuration | status | recall@k | MRR@k | recall incl. related | neg. empty | neg. below median | neg. weak-match (positives flagged) | families/top-k | cross-family | median s |
|---|---|---|---|---|---|---|---|---|---|---|
| lexical | ran | 100% | 0.678 | 100% (+0) | 1/1 | 1/1 | 1/1 (0) | 4.69 | 0/13 | 0.191 |
| lexical+graph | ran | 100% | 0.678 | 100% (+0) | 1/1 | 1/1 | 1/1 (0) | 4.69 | 0/13 | 0.189 |
| lexical+lexicon | ran | 94% | 0.595 | 94% (+0) | 1/1 | 1/1 | 1/1 (1) | 4.75 | 0/12 | 0.202 |
| lexical+graph+lexicon | ran | 94% | 0.595 | 94% (+0) | 1/1 | 1/1 | 1/1 (1) | 4.75 | 0/12 | 0.198 |
| plans | unavailable: no query plans supplied | | | | | | | | | |

## First relevant rank per query

| query | group | lexical | lexical+graph | lexical+lexicon | lexical+graph+lexicon |
|---|---|---|---|---|---|
| ground_derivative_budget | derivation_discovery | 3 | 3 | 3 | 3 |
| rare_fiber_transport_obstruction | derivation_discovery | 8 | 8 | 9 | 9 |
| thermodynamic_cylinder_gradient | derivation_discovery | 1 | 1 | 1 | 1 |
| current_factorization_without_inverse | derivation_discovery | 3 | 3 | 3 | 3 |
| three_coordinate_anisotropy | derivation_discovery | 3 | 3 | 3 | 3 |
| hardy_conditional_score_tails | derivation_discovery | 4 | 4 | 3 | 3 |
| global_gaussian_reference_failure | derivation_discovery | 1 | 1 | 4 | 4 |
| matrix_mass_atom_persistence | imported_discovery | 1 | 1 | 1 | 1 |
| upper_decay_not_atom_lower_bound | imported_discovery | 1 | 1 | 2 | 2 |
| literal_wilson_source_frame | imported_discovery | 3 | 3 | 3 | 3 |
| blocked_zero_momentum_interface | imported_discovery | 1 | 1 | 1 | 1 |
| historical_signed_incidence | theory_discovery | 7 | 7 | miss | miss |
| historical_stranded_flux_zero_backend | theory_discovery | 1 | 1 | 1 | 1 |
| exact_rank_three_coefficient | exact_control | 1 | 1 | 1 | 1 |
| exact_channel_difference | exact_control | 1 | 1 | 1 | 1 |
| exact_plaquette_regular_graph | exact_control | 1 | 1 | 1 | 1 |
| absent_token_control | negative_control | hits=0 | hits=0 | hits=0 | hits=0 |

## Link recovery (hidden registered edges)

Skipped.

## Leakage check

0 of 16 positive queries contain an expected path stem or claim id; 0 exact-control queries consist of their id (listed, not counted).

## Resources

- Engine build: 1.02 s; total: 18.2 s; repeat 1
- tracemalloc peak: n/a; working set: 188 MB; peak working set: 211 MB (psapi GetProcessMemoryInfo)
- Each scored query ran once per repeat in a reused process after one warm-up; medians over queries are reported per configuration. tracemalloc was off; peak memory comes from the process counters.

## Meaning

- Retrieval relevance only; never proof, support or scientific status.
- Passed (empty): no primary hit. Passed (below median): top score below the median top score of positive queries in the same configuration.
- Fraction of assessed positive queries whose first relevant hit lies outside the families implied by the query group.
- None; the saved scientific graph and index are read only.
