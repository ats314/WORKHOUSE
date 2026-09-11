# Discovery evaluation

- Status: ok
- Evidence: Held-out fixture: queries were authored before tuning; results are test evidence.
- Fixture: `C:\WORKHOUSE\worktrees\discovery-agents-20260911\tests\fixtures\discovery_heldout_queries.json` sha256 `8ce69a677ae7388e4cd5e5197a398b9060f56de0dd3dd98b86eff63193290f20` (36 queries, 30 positive, 6 negative)
- Git HEAD: `fdaadc40381e59e95a6f114b1079eec37a5e41a8`; dirty paths: 4
- Discovery cache: `52c54e76f96d5413edf69155bb70a77fdffc8baf895d776539fd3174787556fe` freshness matched (sources rehashed for this call; external files stat-checked and rehashed on change)
- Sources were rehashed for the unscored warm-up query only; engine.recheck_freshness was then set to False for every scored query.

## Configurations

| configuration | status | recall@k | MRR@k | recall incl. related | neg. empty | neg. below median | neg. weak-match (positives flagged) | families/top-k | cross-family | median s |
|---|---|---|---|---|---|---|---|---|---|---|
| lexical | ran | 83% | 0.560 | 83% (+0) | 0/6 | 0/6 | 3/6 (16) | 4.80 | 2/19 | 0.210 |
| lexical+graph | ran | 83% | 0.560 | 83% (+0) | 0/6 | 0/6 | 3/6 (16) | 4.80 | 2/19 | 0.230 |
| lexical+lexicon | ran | 73% | 0.526 | 73% (+0) | 0/6 | 0/6 | 3/6 (19) | 5.13 | 3/16 | 0.265 |
| lexical+graph+lexicon | ran | 73% | 0.526 | 77% (+1) | 0/6 | 0/6 | 3/6 (19) | 5.13 | 3/16 | 0.273 |
| plans | ran | 87% | 0.688 | 90% (+1) | 0/6 | 0/6 | 3/6 (17) | 4.90 | 2/20 | 0.642 |

## First relevant rank per query

| query | group | lexical | lexical+graph | lexical+lexicon | lexical+graph+lexicon | plans |
|---|---|---|---|---|---|---|
| heldout_deriv_01 | heldout_derivation | miss | miss | miss | miss | miss |
| heldout_deriv_02 | heldout_derivation | miss | miss | miss | miss | miss |
| heldout_deriv_03 | heldout_derivation | 3 | 3 | 2 | 2 | 2 |
| heldout_deriv_04 | heldout_derivation | 3 | 3 | 3 | 3 | 4 |
| heldout_deriv_05 | heldout_derivation | 5 | 5 | miss | miss | 10 |
| heldout_deriv_06 | heldout_derivation | 3 | 3 | 3 | 3 | 1 |
| heldout_deriv_07 | heldout_derivation | 2 | 2 | 2 | 2 | 2 |
| heldout_deriv_08 | heldout_derivation | 1 | 1 | 2 | 2 | 1 |
| heldout_hist_01 | heldout_historical | 3 | 3 | miss | miss | 2 |
| heldout_hist_02 | heldout_historical | 2 | 2 | 2 | 2 | 1 |
| heldout_hist_03 | heldout_historical | 1 | 1 | 1 | 1 | 1 |
| heldout_hist_04 | heldout_historical | 10 | 10 | miss | miss | 9 |
| heldout_hist_05 | heldout_historical | miss | miss | miss | miss | 6 |
| heldout_hist_06 | heldout_historical | miss | miss | miss | miss | miss |
| heldout_hist_07 | heldout_historical | miss | miss | miss | miss | miss |
| heldout_hist_08 | heldout_historical | 3 | 3 | 3 | 3 | 1 |
| heldout_nl_01 | heldout_notes_literature | 1 | 1 | 1 | 1 | 1 |
| heldout_nl_02 | heldout_notes_literature | 2 | 2 | 5 | 5 | 1 |
| heldout_nl_03 | heldout_notes_literature | 1 | 1 | 1 | 1 | 1 |
| heldout_nl_04 | heldout_notes_literature | 2 | 2 | 1 | 1 | 1 |
| heldout_nl_05 | heldout_notes_literature | 2 | 2 | 4 | 4 | 2 |
| heldout_nl_06 | heldout_notes_literature | 3 | 3 | 3 | 3 | 1 |
| heldout_nl_07 | heldout_notes_literature | 1 | 1 | 1 | 1 | 1 |
| heldout_nl_08 | heldout_notes_literature | 1 | 1 | 1 | 1 | 1 |
| heldout_exact_01 | heldout_exact | 1 | 1 | 1 | 1 | 1 |
| heldout_exact_02 | heldout_exact | 1 | 1 | 1 | 1 | 1 |
| heldout_exact_03 | heldout_exact | 1 | 1 | 1 | 1 | 1 |
| heldout_exact_04 | heldout_exact | 1 | 1 | 1 | 1 | 1 |
| heldout_exact_05 | heldout_exact | 1 | 1 | 1 | 1 | 1 |
| heldout_exact_06 | heldout_exact | 1 | 1 | 1 | 1 | 1 |
| heldout_neg_01 | heldout_negative | hits=10 | hits=10 | hits=10 | hits=10 | hits=10 |
| heldout_neg_02 | heldout_negative | hits=10 | hits=10 | hits=10 | hits=10 | hits=10 |
| heldout_neg_03 | heldout_negative | hits=10 | hits=10 | hits=10 | hits=10 | hits=10 |
| heldout_neg_04 | heldout_negative | hits=10 | hits=10 | hits=10 | hits=10 | hits=10 |
| heldout_neg_05 | heldout_negative | hits=10 | hits=10 | hits=10 | hits=10 | hits=10 |
| heldout_neg_06 | heldout_negative | hits=10 | hits=10 | hits=10 | hits=10 | hits=10 |

## Link recovery (hidden registered edges)

40 of 980 eligible curated edges (seed 20260911, limit 20, 0 errors, 35.8 s).

| variant | slice | n | @5 | @20 | MRR |
|---|---|---|---|---|---|
| connections | overall | 40 | 25% | 45% | 0.170 |
| connections | bears_on | 14 | 21% | 43% | 0.148 |
| connections | depends_on | 13 | 38% | 46% | 0.263 |
| connections | supported_by | 13 | 15% | 46% | 0.099 |
| connections | same_family | 20 | 40% | 50% | 0.265 |
| connections | cross_family | 20 | 10% | 40% | 0.075 |
| retrieval_only | overall | 40 | 10% | 42% | 0.056 |
| retrieval_only | bears_on | 14 | 0% | 43% | 0.042 |
| retrieval_only | depends_on | 13 | 15% | 38% | 0.061 |
| retrieval_only | supported_by | 13 | 15% | 46% | 0.067 |
| retrieval_only | same_family | 20 | 10% | 50% | 0.063 |
| retrieval_only | cross_family | 20 | 10% | 35% | 0.050 |

Method: Every edge joining the sampled pair is removed from an in-memory graph copy; the engine's graph is swapped for the copy during the two calls and restored. Recovery of a registered edge is a retrieval property of the engine; it does not validate the edge or suggest new ones.

## Leakage check

0 of 30 positive queries contain an expected path stem or claim id; 3 exact-control queries consist of their id (listed, not counted).
- heldout_exact_04: exact_id_lookup C15
- heldout_exact_05: exact_id_lookup DERIV:WILSON_MARKED_TRANSFER:WT3
- heldout_exact_06: exact_id_lookup RESULT:COMPACT_ROTOR_FAST_GAP

## Resources

- Engine build: 1.00 s; total: 99.5 s; repeat 1
- tracemalloc peak: n/a; working set: 218 MB; peak working set: 228 MB (psapi GetProcessMemoryInfo)
- Each scored query ran once per repeat in a reused process after one warm-up; medians over queries are reported per configuration. tracemalloc was off; peak memory comes from the process counters.

## Meaning

- Retrieval relevance only; never proof, support or scientific status.
- Passed (empty): no primary hit. Passed (below median): top score below the median top score of positive queries in the same configuration.
- Fraction of assessed positive queries whose first relevant hit lies outside the families implied by the query group.
- None; the saved scientific graph and index are read only.
