# Graph discovery implementation

Task: 2026-09-11-graph-discovery. Owner: Codex root with bounded research,
indexing, graph-algorithm and benchmark collaborators.

Checkout: `C:/WORKHOUSE/worktrees/graph-discovery-20260911`;
branch `codex/graph-discovery-20260911`, initial revision `c448fd2`.
This is a software/retrieval task, not a mathematical claim adjudication.

The user prioritized discovering overlooked connections. The implementation
adds a content-addressed passage index, exact-symbol/lexical/graph rank fusion,
unlinked candidate explanations, bounded dependency and context tools, and an
optional revision-pinned local embedding channel. Original status, evidence,
tiers and scientific edges are retained. The reviewed external techniques and
scope are in [the discovery guide](../docs/graph_discovery.md) and its technique
review. No external corpus text was uploaded to model services.

The illustrative start target G19 exercised existing graph routing; it does not
set mathematical priority. Its local saved briefing is retained at
`.graph-state/graph-discovery-20260911/start.json`. The initial snapshot is saved
with unknown local generation provenance in this new checkout and executed no
checks. Local operational ownership and preserved navigation hashes are under
the outer workspace's `navigation/tasks/2026-09-11-graph-discovery.md` and
`navigation/preserved/2026-09-11-graph-discovery/MANIFEST.json`.

Validation and benchmark observations are recorded below. Final remote
integration state is retained in the outer workspace task record. The fixed benchmark cases were selected before the new
rankings were observed. Remaining semantic-model quality is explicitly separate
from default offline retrieval performance.

## Retained snapshot comparison

- start: `.graph-state\graph-discovery-20260911\start.json`; fingerprint `57e4fea13922a291d3caa43e8f266e46b6d3741cadd812de1c6612cdf3e45590`; input digest `3fe2246f16e54b9e5b22fe48ed99e1a1bd99ae536f1a874706186610c1dacaff`; saved freshness `unknown`; executed checks 0.
- end: `.graph-state\graph-discovery-20260911\end.json`; fingerprint `1040ccf1e342dfb5745d8b91a7bb787d91e8f8ef0409b037306283a38b095f31`; input digest `bd14358500ce1adf7723df2b51277061266b4ba3b1c47cab7800bf9e92c01fe0`; saved freshness `unknown`; executed checks 0.

Saved graph digest `6726a567f314d3016bdca68d5a1f19b7b46ab803c3b91f634ceccc7988b56d8b` is identical in both snapshots. New code changes the input manifest; no scientific catalogue, source, tier or edge was edited. The separate `workhouse verify --json` run passed all 579 checks. A retained briefing reads saved verification metadata and is not that execution.

The [benchmark report](../docs/benchmarks/graph-discovery-2026-09-11.md) and its compact evidence retain the fixed query comparison. Optional semantic adapters passed synthetic vector/schema tests; no actual embedding model was downloaded or quality-benchmarked.

The original JSON bytes are also retained with this published task record: [start snapshot](evidence/2026-09-11-graph-discovery/start.json) and [end snapshot](evidence/2026-09-11-graph-discovery/end.json). Copies preserve their fingerprints and contain the recorded input scope and actual checkout identity.


## Validation and handoff

The full local regression completed with **1,656 passed, 2 skipped and 11
subtests passed**, in 701.93 seconds. A final small CLI error-handling change
was verified separately by all 19 focused orchestration/CLI tests. The actual
registered verification execution passed **579/579** checks. Repository-wide
Ruff lint and formatting passed; the maintained documentation check passed
33 documents and 541 links with no errors or warnings. No Lean source changed
and this task did not run a local Lean compilation.

The fixed development benchmark improved relevant-source retrieval at ten
from **9/16 to 16/16** positive queries; MRR rose from 0.3771 to 0.6985. It
covers 617 source files, 10,022 passages, 17,382 saved records and 29,302 edges.
Expanded lexical retrieval alone also reached 16/16. Full discovery is slower
than the old finder because it also computes graph suggestions and freshness.
The report distinguishes source coverage, ranking, development-set revision,
related suggestions, and untested semantic-model quality.

Independent review findings concerning signed mathematical tokens, literal
source filenames, locator normalization, passage attribution, context-budget
limits, freshness metadata, and malformed semantic input were resolved and
covered by focused regressions. The CLI and agent guide expose search,
connection candidates, bounded paths, dependency impact, and context packs.
All suggested connections remain retrieval evidence; scientific assertions
and verified dependency edges retain their original status and provenance.
