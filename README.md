# WORKHOUSE

[![CI](https://github.com/ats314/WORKHOUSE/actions/workflows/ci.yml/badge.svg?branch=main)](https://github.com/ats314/WORKHOUSE/actions/workflows/ci.yml)

WORKHOUSE connects four years of mathematical research on the SU(N) cubic
flux-band spectral program and the Yang-Mills existence and mass-gap problem.
It brings analytic derivations, exact and numerical checks, Lean proofs, and
their source histories into a queryable theory graph.

## Start here

| Need | Read |
| --- | --- |
| Understand the established results and current obligations | [Current research](docs/current_research.md) and [research goal](docs/research_goal.md) |
| Find a derivation's Lean coverage and remaining work | [Derivation proof map](docs/derivation_formalization.md) |
| Inspect checked claims and reproduce one | [Frontier](FRONTIER.md), [certified catalogue](CERTIFIED.md), then `workhouse why ID` |
| Begin an agent session | [THEORY GRAPH protocol](docs/theory_graph_protocol.md), [task index](INDEX.md), [research instructions](AGENTS.md), [working agreement](CLAUDE.md) |
| Coordinate local and GitHub work, intake and task ownership | [Workspace operations](docs/workspace_operations.md) |
| Set up, test, contribute, and publish | [Contributing](CONTRIBUTING.md) |
| Add a formal proof and precise dependency links | [Formalization workflow](docs/formalization_workflow.md) |
| Find another guide or a historical record | [Documentation index](docs/README.md) |

On the maintainer's workstation, the active checkout is **`C:\WORKHOUSE\REPO`**.
The surrounding `C:\WORKHOUSE` is the full research archive; `ALL THEORY` is
one collection within it. Older checkouts and their Git metadata remain
preserved sources. On another machine, use the root of your own clone.
[Workspace coordination](docs/workspace_coordination.md) explains both cases.

The September reconciliation and analytic formalization reached GitHub main
in [PR #113](https://github.com/ats314/WORKHOUSE/pull/113). This is a dated
integration milestone; use the live guides and generated views for current
scope and counts. GitHub holds the versioned verification project and selected
evidence, while the larger local archive retains its original files.

The [September 10 Hodge and polymer scope correction](docs/research/formalization-scope-2026-09-10.md)
separates abstract operator proofs and scalar ingredients from their remaining
physical-model identifications, with preserved source inputs and exact proof links.
The [W6 continuation](docs/derivations/w6-ground-jets-and-transport-budget.md)
adds actual fixed-square ground and operator derivative bounds and an explicit
criterion for the complete source-transport budget.
The [conditional transport continuation](docs/derivations/w6-conditional-transport-obstruction.md)
derives the exact true-ground conditional score, locates its constrained Agmon
centers, and proves that some admissible Q8 cutoffs fail M10 in the actual model.
It specifies synchronized radial profiles that follow those centers; their
uniform M10 estimate remains open.

For questions spanning the corpus, use the [discovery engine](docs/graph_discovery.md) to combine source passages, exact symbols and graph paths across the checkout and the declared workstation archive, compare candidate pairs, and retain each reading in the [review register](graph-tasks/discovery/README.md); registration stays a reviewed hand edit.

The [G9 sixth-order continuation](paper/research_notes/G9_SIXTH_ORDER_COMBINED_20260911.md)
derives the complete formal 18-word electric fold formula and evaluates one
SU(3) plaquette through order six. Combining all H4-induced terms proves
that an extra rational band shape survives every local direct H6 under the
recorded third-order factorization. Direct multi-plaquette H6 word coefficients,
including the q e2/e3 terms, remain open. The earlier walk census does not
establish a physical RUR amplitude.

The [moving-time gap criterion](docs/derivations/moving-time-spectral-gap.md)
proves a limiting spectral gap from approximate sources and one growing physical
observation time per cutoff. Its sharp power-law budget retains source-amplitude
and finite-horizon losses. Actual continuum measures, source totality and the
Wilson one-time estimates remain explicit application hypotheses.

The [cellular Hodge correction](docs/derivations/universal-cellular-hodge-tetrahedral.md)
establishes the finite-cell incidence identities and tetrahedral face commutant,
and adds an all-power Lean operator proof for the shifted `R S^m R` formula.
An exact projection diagnostic keeps the physical tetrahedral history
identification and the broader U3/U7 unification open. The received claims,
review findings, and corrected verification are preserved with the source package.
The [completed repair record](graph-tasks/2026-09-11-universal-cellular-hodge-repair.md)
retains the final full verification and matched graph snapshot.

## Quick start

The [September 10 folder review](runs/folder_evidence_integration_2026-09-10/README.md)
traces all 114 files in the requested archive derivation, research and validation
folders to preserved bytes, scoped reviews and graph entries. It extracts the
reusable convergence criteria and connects historical validation logs without
treating their earlier executions as new mathematical certification.

From an existing checkout, with Python 3.11 or newer and `uv` available:

The queries below illustrate syntax using real graph IDs and values. Replace
`G19` and the sample search value with targets relevant to your task; these
examples do not set research priorities.

```text
git status --short --branch
uv sync --all-extras --frozen
uv run --no-sync workhouse --help
uv run --no-sync workhouse brief --startup
uv run --no-sync workhouse search '5/612'
uv run --no-sync workhouse brief G19 --json
```

Before starting a new branch, inspect local changes, coordinate the shared-ref
refresh and select the base under
[workspace operations](docs/workspace_operations.md#start-with-an-observed-git-and-command-state).
Follow [Contributing](CONTRIBUTING.md) for a fresh clone, native PowerShell
commands, Lean setup, and validation. Existing uncommitted work must be kept.
Reading the checked-in guides does not require installing anything.

For mathematical work, follow the [shared protocol](docs/theory_graph_protocol.md)
and retain a briefing with `--out` plus a [manual task record](graph-tasks/README.md).
A fresh clone's saved graph has unknown freshness until local generation
provenance exists; saved briefing mode never silently rebuilds it. `--live`
rebuilds with observed cache use; `--fresh` requests uncached Python checks.

Search by a claim ID, exact value, symbol, or filename before scanning a large
collection. A useful source-to-proof query pair is:

```text
uv run --no-sync workhouse why DERIV:WILSON_SC17_THERMODYNAMIC_LIMIT:IF4_CLOSABLE
uv run --no-sync workhouse why LEAN:closed_extension_of_integration_by_parts
```

The first shows the precise derivation statement and its scoped formal support.
The second shows the compiled theorem and its registered dependency links.
The [kernel export](ledger/lean_dependencies.json) also records directly used
constants and transitive axioms. Source dependencies and kernel dependencies
answer different questions; both belong in the graph.

## What a verification claim means

The [supported Track A statements](docs/derivations/track-a-supported-statements.md)
connect W6 variational bounds, SC17 Riccati comparison, and corrected G17
probability-source estimates to their Lean proofs. The original report is
preserved with [source hashes and verification evidence](runs/track_a_formalization_2026-09-09/README.md).
The proof map distinguishes these complete abstract results from the remaining
Wilson-model and SU(2) Haar identifications.

The [reviewed current and geometry connections](paper/research_notes/THEORY_CURRENT_BRIDGES_20260910.md)
add an explicit current for the fixed square's complete first residual, with
constant below `1/840`, and connect it to selected-inverse control, source
totality, Schur metrics and Riccati residual certificates. The variational
energy estimate is inverse-free; the checked W6 composition retains its
bounded-inverse assumptions. Start with `workhouse why RESULT:SQUARE_FIRST_CURRENT_BUDGET`
and the [integration evidence](runs/theory_current_bridges_2026-09-10/README.md).

Accept a derivation when its mathematical argument works under its explicit
hypotheses. Publication status, novelty, and an agent's prior familiarity do
not determine whether it is valid. Record exactly what its proof establishes.

| Machine tier | Meaning |
| --- | --- |
| T0 | Lean proof-checks the encoded statement, with no `sorry` and standard axioms only |
| T1 | An exact symbolic calculation re-derives the stated claim |
| T2 | A numerical calculation agrees within its stated tolerance |
| T3 | The full statement has no dedicated repository machine certification |

Mathematical status and evidence level are separate from these tiers. An
established analytic theorem can remain T3 while its full formalization is
unfinished. A finite test or a supporting Lean lemma does not certify a
larger theorem. The [proof map](docs/derivation_formalization.md) distinguishes
whole-statement `formalizes` links from scoped `supported_by` links and records
the remaining construction for every indexed group.

For a concrete claim, read its hypotheses, source, verification result, and
dependencies together. A hash proves which bytes were used; an inventory or
extraction does not mean those bytes have received mathematical review.

## Working with the graph

Choose IDs and filters for your task. `C2`, `G19`, and the values below are
examples, not required targets.

```text
uv run --no-sync workhouse search 109151/249696
uv run --no-sync workhouse brief C2 G19 --json
uv run --no-sync workhouse why C2
uv run --no-sync workhouse verify --only 'h_4^side = A_+'
uv run --no-sync workhouse notes --queue
uv run --no-sync workhouse lit --for G19
uv run --no-sync workhouse atlas
```

`why` follows recorded dependencies, route closures, checks, sources, and
theorems. `search` understands exact values and recorded aliases. The atlas
renders the graph to local `atlas.html`; it is a generated, ignored view.
The [task index](INDEX.md) routes each kind of change to its source files.

Full verification and regression runs can take many minutes. Use an exact
claim filter or an affected test file during iteration, then complete the
applicable publication gates. Do not rely on old timing estimates or treat
`make quick` as a guarantee of a short run.

## Preserve sources and keep current guidance current

- Keep original research, failed attempts, duplicates, and historical
  checkpoints. Do not clean, reset, relocate, or deduplicate the archive.
- Preserve the exact previous navigation bytes and SHA-256 before revising
  existing guidance. The [documentation maintenance guide](docs/documentation_maintenance.md)
  describes the preservation record and the distinction from scientific pins.
- Edit the maintained source for a generated view. Do not hand-edit
  `FRONTIER.md`, `CERTIFIED.md`, `index/*.jsonl`, or the generated proof map.
  Prose-only changes do not require scientific regeneration.
- When source or proof records change, follow the ordered generators and
  validation in [the formalization workflow](docs/formalization_workflow.md).
- Publish tested work, inspect CI and reviews, merge when green, and verify
  the exact files on GitHub main. Report whether work is local, pushed, or
  merged; a successful local command alone is not publication.

Historical research narratives remain in their derivations, sealed runs and
[the reconciled README snapshot](https://github.com/ats314/WORKHOUSE/blob/742033a604484bf2caf00611bc0d4f0973fe12c4/README.md).
Their dated “next” statements describe that stage. Use the current research map
and live graph before reopening a completed route.

## Repository map

| Path | Role |
| --- | --- |
| [docs/](docs/README.md) | Current guides plus dated derivations, decisions and validation records |
| [ledger/](ledger/CLAUDE.md) | Claim, source, route, theorem and derivation statement records |
| [src/workhouse/](src/workhouse/CLAUDE.md) | Mathematical checks, graph construction and CLI |
| [lean/](lean/README.md) | Formal statements, proofs and dependency extraction |
| [index/](index/CLAUDE.md) | Generated claim, symbol and edge catalogues |
| [tests/](tests/) and [scripts/](scripts/) | Regression checks, generators and maintenance commands |
| [theory/](theory/) and [corpus-import/](corpus-import/) | Pinned source history; access by precise locator |
| [notes/](notes/README.md) | Content-addressed note inventories and review routes |
| [literature/](literature/README.md) | Source acquisition, reading evidence and citation relationships |
| [paper/](paper/README.md), [runs/](runs/), [settlement/](settlement/) | Preserved manuscripts and execution evidence |

## Licence

All rights reserved. See [NOTICE](NOTICE). Third-party source records retain
their own declared licences and storage restrictions.
