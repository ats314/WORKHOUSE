# 7. The research OS is a graph the repository already stores in pieces

Date: 2026-08-21

## Status

Accepted

## Context

An external recommendation proposed turning WORKHOUSE into an "interactive
mathematical research operating system" and sketched fourteen tools: a research
navigator, an interactive theory graph, a claim inspector, a contradiction
explorer, a frontier dashboard, an AI investigator, a conjecture forge, a
constant genealogy, an equation search engine, a proof-promotion pipeline, a
research time machine, a theory diff, a blind verification runner, and a
literature cross-examiner.

Measured against the repository rather than against an empty page, the list
splits three ways.

**Already built, as CLI rather than UI.** The equation search engine is
`workhouse search` — it matches by value (`-10/96` finds `-5/48`), by decimal
prefix, by alias, and by claim id, and it knows the forbidden and repo-coined
names. The frontier dashboard is `FRONTIER.md` §5–7: the leverage numerator is
the §6 transitive gating count, the denominator is the ledger's cost tier, and
§7 is the argmax. The constant genealogy is `corpus_index` plus
`corpus_registry` (file, line, and source text for every exact rational — forty
derivations versus one number pasted forty times). The blind verification
runner is the settlement harness and its seven adjudication checks. The
literature cross-examiner is `literature/index.yaml` with its typed relations,
including `confusable`. The promotion pipeline's ranking half is
`CERTIFIED.md`.

**Rejected, because it would assert what nothing computes.** Progress bars on
open mathematics ("G3 ███████░░ 70%") and probability-ranked candidate
explanations ("representation selection 31%") are numbers no check produces;
rendering them would create exactly the confident-looking unchecked text this
repository exists to resist. The research time machine fails on its premise
here: this repository has 26 commits and the corpus arrived in one bulk import
on 2026-08-20, so the four years of history live in `theory/superseded/` and
the manifests, not in `git log`. The theory diff needs the canonical-symbol
crosswalk layer first and is deferred with it.

**Actually missing: the joins.** The relationships between entities exist but
are siloed in at least six formats. The ledger has typed edge fields
(`blocks`, `resolves`, `unblocks`, `depends_on`, and the register's
`contradictions`/`gaps` lists). Checks cite claims only inside free-text
section strings — `"MASTER_THEORY §5.5 / C1"`, `"(C7)"` in a check name,
`"(G11)"` in a suite name. Papers point at claims in `literature/index.yaml`.
ADRs reference ids in prose. And the 21 Lean theorems — the strongest results
here — are machine-linked to nothing: `index/claims.jsonl` did not contain
them at all, and no structured record said which claim or check any theorem
formalizes. Nobody could ask "what bears on G14" in one query. That single
missing substrate underlies five of the fourteen proposals (navigator, theory
graph, claim inspector, contradiction explorer, constant genealogy's join).

## Decision

Build the substrate as generated data, in the repository's own idiom —
computed, checked in, staleness-tested — and put one query command on top.

1. **`index/graph.jsonl`** — one record per edge:
   `{src, dst, type, how, source}`. Curated edge types are the verbatim field
   names of the file each edge is read from (`blocks`, `resolves`, `unblocks`,
   `depends_on`, `contradictions`, `gaps`, `claims`, `code_names`, `bears_on`,
   `supported_by`, `formalizes`, `promotes`); derived types name the
   extraction (`cites` for ids parsed out of a check's registered name,
   section, or suite name; `mentions` for ids appearing in an ADR body;
   `amends`/`retracts` from ADR status lines). `how` is `curated` or
   `derived`; there are **no inferred edges** — where no source records a
   relationship, the graph stays silent rather than guessing. An edge is
   emitted only when both endpoints resolve to catalogue records;
   `workhouse index` reports what dangles instead of inventing nodes for it.

2. **`index/claims.jsonl` gains `kind: theorem` and `kind: decision`.** The
   claim catalogue was missing the T0 layer entirely, and the ADRs — which
   carry the claim-lifecycle events, including this repository's own
   retraction — were invisible to search.

3. **`ledger/theorems.yaml`** — the curated map from each Lean theorem to the
   claims it bears on and the checks it promotes, following the
   `ledger/symbols.yaml` precedent: judgement lives in a hand-curated YAML,
   the join is derived, and validation is mechanical (every theorem name must
   exist in `Basic.lean`, every target must resolve, every check name must
   match exactly one registered check).

4. **`workhouse why <id>`** — the navigator: one query, the whole recorded
   evidence neighborhood of a claim, computed at call time. For `C2` that
   means both sides and the delta, never a preference; for `G14` it includes
   the retraction.

What this deliberately does not do: no fourth vocabulary (nodes carry their
existing tier/status/evidence strings verbatim; the only new enum is the
edge-provenance pair `curated`/`derived`, which describes extraction, not
truth); no generated prose; no probabilities; no percent-complete. ADR 0004's
retracted G14→G9 dependency is never materialized as a dependency edge — the
ADR nodes may `mention` both ids, and a test pins the absence of anything
stronger.

## Consequences

The graph is regenerated by `make catalogue` and a test fails when it is
stale, like every other generated artifact here. The later tools become
consumers of this data rather than new sources of assertion: an HTML atlas can
render `graph.jsonl` without adding a single claim; an investigator agent can
walk it, and anything it conjectures still enters through
`unifying_candidates` with a falsifier or not at all. If a curated edge in
`theorems.yaml` is wrong, it is one reviewed line in one YAML file — the same
blast radius as a wrong alias in `symbols.yaml`, and the same fix.
