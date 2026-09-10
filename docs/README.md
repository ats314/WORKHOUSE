# Documentation index

Use this directory to find derivations, research routes and their evidence.
Start with the repository [operating guide](../README.md), [research posture](../AGENTS.md)
and [working agreement](../CLAUDE.md). The generated [FRONTIER](../FRONTIER.md)
and [CERTIFIED](../CERTIFIED.md) describe the active checkout's registered state;
their reproduction commands establish whether that state remains current.

## Choose a route

| Need | Start here | How to use it |
| --- | --- | --- |
| Mathematical arguments and explicit hypotheses | [derivations/](derivations/) | Follow the stated operator, regime and source references. |
| Exact statement-to-Lean coverage and remaining work | [Derivation proof map](derivation_formalization.md) | Follow source-pinned statement IDs and kernel-extracted dependencies. |
| Current research directions and integration reviews | [research/](research/) | Query the named graph obligation before restarting a route. |
| Recorded checks, audits and independent reviews | [validation/](validation/) | Read the run date, source revision and precise checked statement. |
| Reasons for repository and mathematical decisions | [decisions/](decisions/) | Follow amendments and retractions as well as the original decision. |
| Prior session context and authoring handoffs | [handoff/](handoff/) | Treat instructions and status as dated context; reconcile with current sources. |
| Manuscript and corpus referee reports | [referee/](referee/) | Check which manuscript or source version each report reviewed. |
| Bounded experimental proposals and findings | [experiments/](experiments/) | Keep their stated hypotheses and stopping criteria attached. |

For September 1–9 work, the [integration run](../runs/recent_research_integration_2026-09-09/README.md)
is the main entry point. Its [document coverage map](../runs/recent_research_integration_2026-09-09/docs_coverage.json)
links the priority documents to native citation IDs. The
[recent research ledger](../ledger/recent_research.yaml) registers the standalone
anisotropy and W6 results, exact source locators, assumptions and remaining routes.
The [Lean guide](../lean/README.md) describes the active proof modules, while the
[theorem registry](../ledger/theorems.yaml) records what each declaration formalizes.

## September source routes

| Topic | Documents to follow |
| --- | --- |
| Wilson transfer and complete-shell matching | [Marked transfer](derivations/wilson-marked-transfer.md), [shell transport](derivations/wilson-marked-shell-transport.md), [unchanged shell inputs](derivations/wilson-shell-inputs/README.md), [September 8 route](research/next-path-wilson-transfer-2026-09-08.md) |
| Spatial comparison, sources and selected inverse | [Schur excess](derivations/wilson-spatial-schur-excess.md), [selected-inverse obstruction](derivations/wilson-selected-inverse-wall.md), [unchanged spatial inputs](derivations/wilson-spatial-inputs/README.md), [continuum route](research/spatial-continuum-passage-2026-09-08.md) |
| Vacuum assembly and weighted repair | [Vacuum-aligned assembly](derivations/wilson-vacuum-aligned-assembly.md), [weighted repair and rotor gap](derivations/wilson-weighted-repair-and-rotor-gap.md), [true-vacuum block estimates](derivations/wilson-true-vacuum-block-estimates.md), [independent block check](derivations/wilson-true-blocks-independent-check.md) |
| Background continuation and SC17 | [Background covariance](derivations/wilson-background-covariance-continuation.md), [spatial closure](derivations/wilson-sc17-spatial-closure.md), [thermodynamic limit](derivations/wilson-sc17-thermodynamic-limit.md), [physical-time limit](derivations/wilson-sc17-physical-time-limit.md), [independent SC17 review](validation/wilson-sc17-independent-review.md) |
| Quantum reconstruction and comparison forms | [Reconstruction](derivations/yangmills-reconstruction.md), [flat directions](derivations/yangmills-simon-flat-directions.md), [weighted curvature](derivations/yangmills-weighted-curvature.md), [formal bridges](derivations/yangmills-formal-bridges.md) |
| September 8–9 Feshbach integration | [Source integration and scope corrections](research/september_feshbach_integration.md), including the exact word counterexample and the exact/numerical resolvent split |
| Source review and proposed closure checks | [G19 corpus reconciliation](validation/wilson-g19-corpus-reconciliation.md), [Gaussian review](validation/wilson-g19-gaussian-review.md), [continuum Cauchy repair](validation/wilson-g19-cauchy-repair.md), [GPU/operator audit](derivations/yangmills-gpu-resolution-audit.md) |

The standalone anisotropy, strip, square-block and compact-continuation campaigns
are preserved with their source hashes in the integration run's
[sources/](../runs/recent_research_integration_2026-09-09/sources/).
Use the recent research ledger to select the result and proof locator within
those packages; a summary filename alone does not establish its scope.

## Agent workflow and evidence

From the repository root in the configured environment:

```powershell
uv run --no-sync workhouse why G18
uv run --no-sync workhouse why G19
uv run --no-sync workhouse why RESULT:W6_SQUARE_SHARP_INVERSE_ENERGY
uv run --no-sync workhouse verify --only anisotropy
```

Use [document aliases](../ledger/documents.yaml) for source standing and
relationships, [gaps](../ledger/gaps.yaml) for active obligations, and the
[contribution guide](../CONTRIBUTING.md) when adding a check. Regenerate scientific
indexes through the operating guide's commands; preserve original source evidence.

T0 denotes compiled Lean proofs with their explicit assumptions; T1 denotes
exact executable derivations; T2 denotes numerical checks with stated tolerances;
T3 denotes statements without that native machine verification. A source can
contain an analytic proof while its citation record remains T3. Document links,
preserved logs and source hashes establish provenance; they do not rerun a check
or turn a component proof into a theorem about a larger operator or limit.

## Historical snapshots

[State of the program — August 22, 2026](state_of_the_program_2026-08-22.md)
and [State of the theory — August 28, 2026](state_of_the_theory_2026-08-28.md)
remain historical accounts. Use their dates when citing them. For active
registered results and unresolved dependencies, return to the generated frontier,
current ledgers and the source-specific graph queries above.
