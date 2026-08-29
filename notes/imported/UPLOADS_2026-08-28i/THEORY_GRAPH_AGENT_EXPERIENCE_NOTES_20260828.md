# Theory Graph — Agent Experience Notes

Date: 2026-08-28  
Native investigation: `investigation_b7a825d5f36043b88acfee4f8f88ca3a`

This is an append-only working memo recording direct agent experience with the WORKHOUSE theory-graph interface while investigating the SU(3) fourth-order cubic off-axis coefficient conflict.

## Observation 1 — Native availability and health

- The graph is natively callable through the registered `research-map` interface; no wrapper or repository launch was needed.
- The first bounded context call completed successfully and quickly.
- Health reported schema `0.3.0`, a fresh retrieval projection, 83,750 documents, 511 formulas, 1,638 graph edges, and matching requested/projection fingerprints at ledger high-water sequence 163.
- The source-provenance payload is strong: record, manifestation, asset, extraction-run, offsets, page, text digest, and artifact digest are returned together.

## Observation 2 — First retrieval miss

- Query: historical 189-record SU(3) fourth-order kernel versus the target-blind HODGE v10a.26 `C_shape` value.
- Result: two unrelated spans about TFGN and philosophy of science.
- Interpretation: runtime health is good, but either the relevant WORKHOUSE/HODGE material is not in the active projection or ranking did not find it.
- The current result does not clearly distinguish those two cases for the caller.

## Initial improvement ideas

1. Expose active corpus/collection/manifest scope before or alongside search.
2. Add a low-relevance abstention mode instead of filling the result window with unrelated evidence.
3. Return a compact diagnostic explaining whether query terms exist anywhere in the active projection.
4. Add source-path, collection, repository, and ingestion-batch filters.
5. Show enough omitted-candidate information to distinguish budget truncation from a genuine retrieval miss.

## Observation 3 — Two different graph surfaces

- The registered `research-map` service and the repository-native WORKHOUSE graph are distinct systems.
- The registered service is a large semantic corpus projection with source-span provenance and proposal/investigation tools.
- The repository graph is a deterministic evidence graph generated from WORKHOUSE ledgers, claims, checks, symbols, literature records, provenance records, and note reviews.
- This distinction was not obvious from the user-facing tool names. A small capability/scope descriptor would prevent agents from querying the wrong graph.

## Observation 4 — Repository-native `why C2` succeeds

On current WORKHOUSE `main` (`95c150f8f1612958ebeba508d7693955da843c8a`), `workhouse why C2` returned:

- both coefficient branches and their numerical gap;
- the `C2 blocks G3` and `G3 resolves C2` relationship;
- the `R5` contradiction record;
- incoming T1/T2 checks, symbols, ADRs, literature, and uploaded-note records;
- exact provenance nodes for the historical 189-row kernel and executed v10a.26 notebook.

This is genuinely useful. It turns a scattered archive investigation into a bounded evidence neighborhood without inventing relationships or flattening disagreement.

## Observation 5 — Windows first-run friction

1. The bundled agent Python did not contain `PyYAML`, so the CLI stopped at import time.
2. The machine's existing project Python had the dependencies, but `workhouse why C2` then decoded a Lean source using Windows `cp1252` and failed on byte `0x81`.
3. Setting `PYTHONUTF8=1` made the command succeed without changing repository files.

Recommended fixes:

- Open repository text files explicitly with `encoding="utf-8"`.
- Add a Windows smoke test with UTF-8 mode disabled so locale-dependent reads are caught.
- Document a Windows invocation or launcher that forces UTF-8.
- Consider a dependency-light `why --checked-index` mode that reads the already-generated JSONL files without executing the live catalogue.
- Report missing optional/runtime dependencies as a short actionable diagnostic rather than a raw import traceback.

## Observation 6 — Graph-guided verification

Following the C2 neighborhood into the verifier produced three targeted passing checks:

1. **T1 exact raw-kernel reconstruction:**
   - reconstructs `q`, `c_X`, `c_M`, `c_R`, `alpha`, and `beta`;
   - proves `c_R = 2 c_M - c_X` on the raw records;
   - recovers
     `C_shp = -211835444920651/4405310420659200`
     for the historical kernel.
2. **T2 discrepancy check:**
   - recomputes `Delta_C = 0.027873054295192174` exactly as recorded.
3. **T2 off-axis consequence check:**
   - branch difference at M is `8 Delta_C = 0.2229844343615374`;
   - branch difference at R is `16 Delta_C = 0.4459688687230748`;
   - axial cuts agree.

This is the strongest part of the experience: the graph selected narrow executable checks instead of leaving the agent with a bibliography-like neighborhood.

## Observation 7 — Atlas and portability

- Atlas rendering succeeded: 2,215 connected nodes and 2,759 edges in one self-contained HTML file.
- Live graph validation found 0 dangling endpoints.
- A Windows live build and the checked graph have the same normalized edge set, but 47 provenance `source` fields differ bytewise because Windows paths use backslashes and the checked file uses forward slashes.

Recommended fix: normalize generated provenance paths to repository-relative POSIX form before serialization. This preserves byte-determinism across operating systems.

## Current scientific conclusion selected through the graph

- The historical 189-row kernel coefficient is an exact T1 proposition for that kernel.
- The v10a.26 coefficient is a separately pinned numerical/T3 result.
- The remaining open question is cross-engine identification, not absence of either branch's value.

## Observation 8 — Search and corpus presence

- `workhouse search C2` returned 16 relevant claims and was an effective discovery surface before using `why` on exact IDs.
- Searching the historical negative rational with `--corpus` found two occurrences, both in retained run transcripts.
- The result explicitly warned that repetition is not independence. This is excellent agent guidance and aligns with the graph's originator-versus-carrier model.
- The graph's deliberate refusal to infer missing relationships is a strength for this research program. Improvement work should preserve that boundary.

### Negative-value option-order bug

This natural command fails:

`workhouse search -211835444920651/4405310420659200 --corpus --limit 12`

The negative-query rescue inserts `--` before the value, causing later flags to become unrecognized arguments. This form succeeds:

`workhouse search --corpus --limit 12 -- -211835444920651/4405310420659200`

Recommended fix: make the rescue routine preserve trailing options, or require/document options before the negative positional. Add a regression test combining a negative rational with `--corpus` and `--limit`.

## Highest-value agent-interface additions

1. Add `--json` to `search`, `why`, and filtered `verify`.
2. Add `why --depth N`, `--relations ...`, and `--all` while keeping traversal deterministic and non-inferential.
3. Add `why --evidence` to include corpus pin, SHA-256, observed quote, and source location for origin documents.
4. Distinguish live-catalogue mode from checked-index mode in the command output.
5. Avoid ANSI by default when stdout is not a terminal, or add `--no-color`.
6. Include an explicit next-action field: a reproducible verifier command when a neighboring check exists.

## Observation 9 — Semantic projection does not contain C2

The registered `research-map` formula search returned zero records for the exact historical rational and symbol `C_shp`, despite reporting a fresh projection. Together with the unrelated general-query results, this strongly indicates that WORKHOUSE C2 evidence is not ingested into that projection.

Recommended architecture:

- Keep the deterministic WORKHOUSE graph as the authority for registered claims and curated/derived relationships.
- Export its nodes, edges, evidence pins, and source spans into the semantic `research-map` projection as a named collection.
- Preserve `how=curated|derived`, evidence tier, lifecycle status, and originator/carrier distinctions during export.
- Let semantic retrieval discover candidates, but route final claim inspection back through `workhouse why` and executable verification.

## Observation 10 — The graph is strongest at disagreement preservation

While building the derivation master, the graph prevented two tempting but incorrect merges:

- `C2` keeps the exact historical fourth-order coefficient and the numerical v10a.26 coefficient as separate branch results, rather than selecting one because it occurs in a newer document.
- `G10` keeps the imported fifth-order proven-status claim separate from current-repository verification, where only arithmetic consistency is rerun.

This is exactly the right behavior for scientific synthesis. A master document can present the claimed derivation conditionally while labeling its evidence as record-backed and its current verification as T3.

Recommended improvement: add a first-class “branchwise result” view that prints, for each conflicting symbol, value, tier, originator, retained payload, dependent claims, and the exact missing comparison needed for unification.

## Observation 11 — Status, tier, and replayability need separate fields

The graph currently contains enough information to reconstruct the distinction, but an agent has to infer it across claims, checks, constants, gaps, and imported notes. Three orthogonal fields would make this much safer:

1. mathematical status: proved, conditional, refuted, open;
2. verification tier: T0–T3;
3. replay status: cold-rerunnable, saved-output-rerunnable, arithmetic-only, payload-absent.

The pentagonal fifth-order coefficient is the clearest test case: imported proven-status claim, record-backed evidence, current T3 constant, arithmetic check passing, generating ledgers absent.

## Observation 12 — Live snapshot drift should be surfaced automatically

The checked summary files report a perfect verifier, but the Windows live run is 178/179 because one provenance key is serialized with backslashes while the manifest uses forward slashes. The mathematical kernel reconstruction still passes.

Recommended improvements:

- normalize repository-relative paths to POSIX form at graph and verifier boundaries;
- show “generated snapshot commit” and “live checkout commit” together;
- add an automatic stale-snapshot badge when live aggregate counts differ;
- classify a failing gate as arithmetic, payload, provenance, or platform before rolling it into one red total.

## Observation 13 — A derivation export would be high leverage

The graph made source selection dramatically faster, but producing a readable theorem chain still required manually ordering nodes and rewriting formulas from the controlling sources.

A useful `workhouse derive <claim>` export could emit:

- assumptions and convention;
- dependency-ordered lemmas;
- exact formulas;
- proof/check IDs;
- source and payload pins;
- conflicts and conditional edges;
- nonclaims;
- a compact Markdown section.

The export should remain non-inferential: include only registered edges, mark missing links, and never turn graph reachability into a theorem. A multi-root form such as `derive C2 G24 G10 --format md` would have removed most of the mechanical work in this master synthesis while preserving the graph’s strongest property—its refusal to invent provenance.
