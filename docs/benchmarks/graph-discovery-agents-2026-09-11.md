# Discovery evaluation for autonomous agents

11 September 2026. Held-out and development measurements of the second
discovery iteration, run in the task worktree at `fdaadc4` with the
discovery cache `52c54e76…` (checkout plus the declared external
workstation roots; freshness matched). The raw reports, with per-query rows,
timings and process counters, are retained under
[the task evidence](../../graph-tasks/evidence/2026-09-11-discovery-agents/)
as `heldout-evaluation.json` and `dev-evaluation.json` with their Markdown
renderings. These are retrieval measurements on small purposive fixtures;
they measure neither mathematical validity nor proof discovery.

## What was compared

- **lexical**: BM25 passages and records plus exact lookup, no graph channel.
- **lexical+graph**: the default search. The graph channel never enters the
  primary band by construction, so it can change only the related band.
- **lexical+lexicon**: the question plus the automatic lexicon expansion
  (`discovery_lexicon.expand`, focused mode, weight 0.7).
- **lexical+graph+lexicon**: the default search with those expansions.
- **plans**: the default search with a query plan written blind by a
  frontier-model agent from the query text and the lexicon only, two to four
  reformulations in other families' vocabulary with weights 0.4-0.8. The 36
  plans are retained under `tests/fixtures/discovery_heldout_plans/`.

The [held-out fixture](../../tests/fixtures/discovery_heldout_queries.json)
(SHA-256 `8ce69a67…`) has 30 positive queries in three families plus six
exact-symbol and six negative controls; it was authored blind and frozen
before any change of this iteration was tuned. The
[development fixture](../../tests/fixtures/discovery_queries.json) is the
first iteration's regression set.

## Held-out results at ten

| Configuration | Recall | MRR | Negative controls (empty / below median / weak-match) | Positives flagged weak | Families per top ten | Median warm query |
| --- | ---: | ---: | --- | ---: | ---: | ---: |
| lexical | 25/30 (83%) | 0.560 | 0/6 / 0/6 / 3/6 | 16 | 4.80 | 0.21 s |
| lexical+graph | 25/30 (83%) | 0.560 | 0/6 / 0/6 / 3/6 | 16 | 4.80 | 0.23 s |
| lexical+lexicon | 22/30 (73%) | 0.526 | 0/6 / 0/6 / 3/6 | 19 | 5.13 | 0.27 s |
| lexical+graph+lexicon | 22/30 (73%) | 0.526 | 0/6 / 0/6 / 3/6 | 19 | 5.13 | 0.27 s |
| plans | 26/30 (87%) | 0.688 | 0/6 / 0/6 / 3/6 | 17 | 4.90 | 0.64 s |

All six exact controls rank first in every configuration. The first
iteration's original finder, run on the same fixture through the older
benchmark script, found 16 of 30 (MRR 0.353); the lexical channel alone
found 23 of 30 (MRR 0.476).

What the table supports:

- **Agent-written plans are the semantic component that works.** Blind
  reformulations lifted MRR from 0.560 to 0.688 and recovered one miss
  (`heldout_hist_05`, rank 6) while improving nine other first ranks; two
  queries fell (`heldout_deriv_05` 5 to 10, `heldout_deriv_04` 3 to 4). The
  cost is one engine call with five fused sub-queries, about 0.64 s warm.
- **Automatic lexicon expansion hurts.** Adding the expansions without an
  agent's judgement lost three queries on the held-out set and one on the
  development set (100% to 94%, MRR 0.678 to 0.595). The lexicon therefore
  ships as a plan-authoring aid whose rows an agent keeps or deletes; search
  never expands a query on its own.
- **The graph channel does not change primary hits**, by design; its related
  band recovered one held-out miss and no development miss.
- **Abstention is unsolved.** No configuration returns an empty result for a
  negative control, and every top reciprocal-rank score equals 1/61, so a
  score threshold cannot separate negatives. The pre-registered weak-match
  rule (top row covers under half of the query's content terms with no exact
  match) catches three of six negatives but also flags 16-19 of the 30
  paraphrased positives, so it is informational, not a filter.
- Five held-out misses survive every configuration: two derivation queries
  whose targets are long hypothesis lists, and two historical queries whose
  targets use symbols the paraphrase replaced by words. Archive copies of
  repository documents (near-duplicates with different chunk boundaries) still
  compete with the originals for these queries; byte-identical copies are
  collapsed, near-duplicates are not.

## Link recovery

Forty curated `depends_on`, `bears_on` and `supported_by` edges between
records with substantive statements were hidden one pair at a time in an
in-memory copy of the graph, and `connections` was asked for the source
record's candidates (limit 20).

| Variant | Slice | n | Recovered at 5 | Recovered at 20 | MRR |
| --- | --- | ---: | ---: | ---: | ---: |
| connections | overall | 40 | 25% | 45% | 0.170 |
| connections | depends_on | 13 | 38% | 46% | 0.263 |
| connections | bears_on | 14 | 21% | 43% | 0.148 |
| connections | supported_by | 13 | 15% | 46% | 0.099 |
| connections | same family | 20 | 40% | 50% | 0.265 |
| connections | cross family | 20 | 10% | 40% | 0.075 |
| retrieval only | overall | 40 | 10% | 42% | 0.056 |
| retrieval only | cross family | 20 | 10% | 35% | 0.050 |

Shared-witness explanation triples the reciprocal rank over retrieval alone
and helps mostly inside a source family; across families the two variants are
close, which is the gap the passage-candidate quota and agent plans address.
Recovery of a registered edge is a retrieval property; it validates nothing.

## Development fixture

| Configuration | Recall | MRR | Median warm query |
| --- | ---: | ---: | ---: |
| lexical | 16/16 | 0.678 | 0.19 s |
| lexical+graph | 16/16 | 0.678 | 0.19 s |
| lexical+lexicon | 15/16 | 0.595 | 0.20 s |

The first iteration's benchmark script, rerun after the ranking, freshness
and chunking changes but before the external roots were indexed, gave 16/16
with MRR 0.7068 and a mean warm query of 0.43 s against the published 1.10 s;
that report is retained as `dev-fixture-after-speed.json`.

## Resources and provenance

Engine build 1.0 s; the held-out run totalled 99.5 s including link
recovery (35.8 s); peak working set 228 MB by the process counters
(`tracemalloc` was off because it inflates wall time four to eight times).
Sources were rehashed for the unscored warm-up query only. Zero of 30
positive queries contain an expected file stem or id; the three exact
controls that consist of an id are listed, not counted. The saved scientific
graph and index were read only; no check or Lean build ran.
