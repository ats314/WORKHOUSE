# Discovery for autonomous agents: design record

11 September 2026. Engineering research and design decisions for the second
iteration of the corpus discovery layer. This note records what was measured,
what was decided and why, and what was rejected. It adds no mathematical
dependency, claim-status change or tier, and the tooling it describes never
writes `ledger/` or `index/`.

## Decisions taken with the maintainer

Eight direction questions were answered before implementation. The answers
that shaped the design:

- The consumers are agents in autonomous sessions, reading CLI and JSON
  output. Human-facing visual tooling is a low priority.
- All four connection kinds matter: reusable proof ingredients, disagreements
  and scope restrictions, forgotten archive results, and literature links.
- The index may extend to outer-workspace text (`.md`, `.tex`, `.txt`).
- Registration produces proposal files only; an agent applies them by hand
  after review and lands them by pull request. Review state is versioned
  outside the scientific ledgers.
- No local embedding models are evaluated. The semantic component is the
  frontier model already in the loop, driving query plans and rereading
  shortlists, plus a versioned, source-cited lexicon. The optional Hugging
  Face adapter from the first iteration stays in place, unused.
- The theory graph must never be modified by discovery tooling.

## What the first iteration cost, measured

A warm in-process profile of the merged first iteration on the measured
checkout (617 source files, 17,382 records, 29,302 edges) attributed the
roughly one second per query to four places: personalized PageRank by whole-
graph power iteration (about 0.42 s, 83-99 iterations), a second full
re-hash of every source file inside `metadata()` on every response (about
0.3 s on top of the hash already done at engine start), `path.resolve()`
on every walked file (about 0.2 s per walk on Windows), and deep copies of
every edge dictionary visited by the path search even for paths never
returned. Engine construction added about 0.4 s for graph projection copies
and, when a cache is reused, 0.44 s for SQLite's page-level `quick_check`
over a 117 MB file.

The JSON an agent had to parse was 56-96% provenance boilerplate: the
per-file source manifest (about 105,000 characters) was embedded in every
response, record hits carried their content twice, and a 16,000-character
context pack retained two of fifteen hits while silently dropping the
top-ranked one.

## Ranking: local push instead of power iteration

Personalized PageRank restarted from lexical seeds is a local quantity: the
stationary vector is concentrated near the seeds. The forward-push
approximation (Andersen, Chung and Lang's local algorithm, written
independently here in pure Python) settles `(1 - alpha)` of a node's
residual into its score and forwards `alpha` along the recorded transitions;
a dangling node restarts through the personalization exactly as the power
iteration does. The invariant `exact = scores + PPR(residual)` makes the
remaining residual mass an exact L1 error bound, which the engine reports
with every search.

On the real graph with three representative seed sets (54-137 seeds), push
at `epsilon = 1e-6` reproduced the power iteration's top-20 sets exactly and
its top-10 order exactly, with residuals near `2e-3` and run times of
0.10-0.14 s against 0.41-0.52 s. A degree-scaled threshold (the original
lazy-walk rule) was tried and rejected: it halved the time again but raised
the residual to `1e-2` and changed one top-20 entry. The power iteration
remains available as `method="power"` and a test bounds the distance between
the two by the reported residual.

Re-running the frozen development fixture of the first iteration after the
ranking, freshness and chunking changes gave the same 16 of 16 relevant
sources in the top ten, a mean reciprocal rank of 0.7068 against the
published 0.6985, and a mean warm query of 0.43 s against 1.10 s. The raw
report is retained with this task's evidence. Those numbers are regression
evidence on a development set; the held-out evaluation is reported
separately.

## Freshness: one walk per response, content hashes kept

The design principle that cache identity comes from content, never from
file size and modification time, is kept. What changed: the walk resolves
directories but not files (a plain regular file beneath a containment-checked
directory cannot escape the checkout, and a reparse point is refused by
`lstat`), the three index files are hashed without being re-parsed during a
re-check, and a batch session may explicitly reuse the observation made at
engine start (`recheck_freshness=False`), in which case the response says so.
The default still rehashes every source per response so that an edit made
after the engine started is reported as `stale`, and the existing regression
test for a same-size same-mtime edit still passes.

## Presentation: rank order, excerpts, named omissions

Compact rows replace full passages: each carries its rank and result group,
an excerpt window chosen around the query terms and snapped to whole lines,
the excerpt's exact line range and the file's SHA-256, the matched terms, a
five-field record summary, and follow-up commands with the `uv run
--no-sync` prefix. Context packs enter rows in rank order and shrink every
excerpt in steps before dropping the lowest-ranked row, and they name every
omitted row. The per-file manifest lives behind `--full` and `discover
info`. On the measured checkout the default search JSON fell from about
173,000 to about 20,000 characters.

Passage boundaries no longer split display math, equation environments or
fenced blocks: a window that reaches its token budget inside such a block
grows to the block's end while the character budget allows, and the one-line
overlap is skipped when it would open the next window inside a block.

## Candidates: unlinked passages are first-class

A read-only census of the index showed that every passage under
`notes/imported/`, `literature/` and `research/` maps to no catalogue record.
The first iteration's `connections` built its candidates from the claim IDs
of retrieved hits, so it could never propose an imported note, a literature
file or a campaign document, whatever the vocabulary. Passage candidates now
keep their locator, hash and excerpt, are marked `no_graph_identity`, receive
no witness or path, and take a reserved third of the slots by default. For
the M10 seed this immediately surfaced imported extraction notes that the
record-only design had missed.

## Sub-queries: decomposition without a model

`search` fuses several query texts: each retrieves its own lexical and exact
candidates, and the per-query rankings are fused by reciprocal rank into the
existing lexical and exact channels, so every downstream step is unchanged.
Hits report their per-query ranks. This is the substrate for agent-written
query plans and for lexicon expansion, both of which are documented in the
[agent guide](../graph_discovery.md).

## The research-map server

A user-scope MCP registration named `research-map` reaches every Claude Code
session on the workstation. It was assessed read-only: it launches a
separate proprietary package under the maintainer's NEURAL CLAUDE folder that
indexes 101 arXiv-style papers on machine learning and lattice field theory,
frozen since 28 August 2026, with no WORKHOUSE content (full-text queries for
`WORKHOUSE` and `Feshbach` return nothing). Its retrieval is sparse, its
proposal layer holds 854 never-reviewed proposals, and its instructions steer
agents to query it first. It plays no role in theory-graph discovery. Two of
its design ideas were re-implemented here in small form: a hash-chained,
append-only review register, and explicit omission counts in bounded output.

## Rejected and deferred

- Persisting parsed records or the graph projection to disk: parsing the
  17 MB of JSONL costs about 0.08 s and was not worth another cache identity.
- Degree-scaled push thresholds: faster, less faithful; see above.
- Local embedding models and hosted embedding APIs: excluded by the
  maintainer for this iteration; the adapter interface is unchanged.
- Indexing agent transcripts and chat histories from the outer archive:
  present in the scope file but disabled by default, because two thirds of
  the outer passages carry little mathematical signal.
