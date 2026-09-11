# THEORY GRAPH protocol

Protocol: `workhouse-theory-graph/v1`.

Codex, Claude, Gemini and other agents use this shared contract to retrieve and
interpret the selected checkout's theory graph. Agent entry files link here;
they do not define separate graph meanings. Select the checkout through
[workspace operations](workspace_operations.md) before querying it.

## Start with a retained snapshot

Select graph targets from the user's task. The commands below use `G19` and
`5/612` as examples; replace them with the relevant graph IDs and search value.
Example IDs do not set research priorities, and `brief` has no default target.

Run from the selected checkout in its configured environment:

```text
git status --short --branch
uv run --no-sync workhouse brief --startup
uv run --no-sync workhouse search '5/612'
uv run --no-sync workhouse brief G19 --json --out .graph-state/TASK/start.json
```

Replace `TASK` with a new dated task identifier as well. `--startup` stands
alone: it prints the protocol location and startup notice without collecting the graph or
running calculations. It does not replace a target-specific briefing.

Supply every relevant target ID together to obtain one shared snapshot, for
example `workhouse brief G18 G19 --json`. `--out PATH` retains the JSON envelope,
creates missing parent directories and refuses to overwrite an existing file.
Use a new path for each start, update and end snapshot; retain earlier evidence.

Read each returned target, its hypotheses and source locators, registered
dependencies, nearby route records, formal coverage and remaining obligations.
Then read the actual argument and proof statements. `workhouse why ID` remains
a supplementary navigator. Retrieval of a relationship does not establish its
mathematical implication or complete coverage of the outer archive.

The [briefing implementation](../src/workhouse/briefing.py) identifies its input
scope, content hashes, snapshot fingerprint and checkout provenance. Keep that
envelope with the [manual task record](../graph-tasks/README.md), rather than
copying only a conclusion. Inspect live GitHub history before declaring that a
result is absent from the project.

## Discover related sources before choosing targets

Use the [discovery engine](graph_discovery.md) when the task spans differently worded sources or requires unexplored connections. `workhouse discover search "research question" --json` combines source passages, exact-value matches and weighted traversal of the saved graph. `workhouse discover connections ID --json` proposes unlinked candidates with recorded path witnesses. The discovery cache and relevance scores are retrieval metadata: they do not change source status, evidence, tier or scientific graph edges. Discovery indexes its explicit local source scope and records content hashes; it does not establish scientific-graph freshness. Retain a target-specific `brief` before mathematical work on selected candidates.

## Distinguish freshness from execution

| Command mode | Recorded meaning |
| --- | --- |
| `workhouse brief ID --json` | Reads the three saved index files. It executes no checks and never silently rebuilds missing files. |
| `workhouse brief ID --json --live` | Rebuilds a view from current inputs. Registered Python checks can execute or reuse observed cache results. |
| `workhouse brief ID --json --fresh` | Rebuilds a view with check-result cache reads and writes disabled. It does not compile Lean. |

Read the returned execution provenance. Saved verdicts, reused results and
checks executed for this request are different observations. These modes do
not change the claim's mathematical status or expand an existing proof's scope.
Live and fresh briefings may run substantial Python work; choose them knowingly.
They do not publish a replacement set of saved scientific index files.

For a saved snapshot, `matched` means its input and catalogue bytes match the
record of a successful local index generation. `stale` means recorded bytes
differ. `unknown` means sufficient local provenance is unavailable, including
a fresh clone without `.graph-state/index-inputs.json`. A saved snapshot can be
readable and returned successfully while stale or unknown; a zero exit status
alone does not establish freshness.

When current work requires a current graph, retain a rebuilt briefing and
compare it with the earlier snapshot. Hash equality concerns the declared
input scope, not a mathematical proof. External archives and excluded runtime
trees are not implicitly reviewed by a matching manifest.

After `workhouse index -w` converges and validates successfully, it records
local input provenance in `.graph-state/index-inputs.json`. This local record
does not travel with an ordinary clone. Use the repository's ordered
[formalization workflow](formalization_workflow.md) when scientific inputs
need regeneration; do not regenerate scientific views just to edit prose.

Invalid targets, unavailable inputs and detected changes during a briefing
produce an explicit error envelope and a nonzero exit status. A missing or
broken executable is **brief unavailable**: retain the error and checkout
identity, read the exact source records, and restore the selected environment.
Independent source reading can continue. Do not invent a fingerprint or call a
fallback query a successful briefing.

## Preserve the recorded mathematical meanings

The corpus assertion-status and evidence vocabularies are defined in
[constants.py](../src/workhouse/constants.py). Machine tiers are separate.

| Axis | Values |
| --- | --- |
| Corpus assertion status | `proven`, `conditional`, `disputed`, `open`, `superseded`, `falsified` |
| Evidence level | `analytic`, `cold-reproduced`, `output-certified`, `numerical`, `record-backed`, `prose-only` |
| Machine verification tier | `T0`, `T1`, `T2`, `T3` |

Graph records retain their kind-specific status too: a route may be `dead`, a
contradiction `resolved`, and a check `passing`. Do not rewrite these values to
fit the corpus assertion vocabulary. Execution and freshness metadata are not
additional scientific evidence tiers.

T0 means Lean checked the encoded statement without `sorry` and with the
permitted standard axioms. T1 is an exact symbolic derivation; T2 is a numerical
check within its stated tolerance. T3 means the whole statement has no dedicated
repository machine certification. A valid analytic proof can be established
while its full Lean formalization remains unfinished. Assess novel arguments
under their actual hypotheses; publication and prior familiarity are not
prerequisites for accepting a working proof.

| Relationship | Interpretation |
| --- | --- |
| `depends_on` | A dependency in the recorded source's scope; Lean kernel use and curated argument dependencies remain distinguishable. |
| `LEAN -> DERIV formalizes` | Registered coverage of the whole named source statement; inspect the encoded hypotheses and conclusion. |
| `DERIV -> LEAN supported_by` | Coverage of a precisely scoped ingredient, not automatic coverage of the whole statement. |
| Closed or superseded route | Follow its recorded closer and retain the historical attempt; a renewed route must identify its changed premise. |
| Documentary or navigation link | Source identity or retrieval, without an implied proof dependency. |

Preserve edge direction, source and `how` fields. Shared words do not establish
a dependency. Keep finite-volume, infinite-volume, continuum and observable
regimes explicit. State the established input, next obligation, consequence
that discharging it enables, and remaining successor.

## Retain the handoff

Use a dated [manual task record](../graph-tasks/README.md) to retain the target
IDs, snapshot paths and fingerprints, source locators, assumptions, owned files,
commands, outcomes and unresolved successor. Before integrating mathematical
changes, obtain an end briefing and explain relevant input changes, including
concurrent edits. Register results and failed attempts in the existing ledgers
with actual dependencies and scoped evidence.

Task-record validation and actual multi-agent conformance exercises are **not
implemented by this integration**. Records are maintained and reviewed manually.
The earlier task-checker and conformance proposals remain preserved pending
sources; they are not required runnable commands or claims of agent compliance.
Passing a software fixture or retaining a fingerprint does not constitute
mathematical review or establish another agent's observed behavior.

## Source provenance

This operational guide adapts the preserved September 10 protocol from local
`worktrees/reconciliation/pending-research-20260910/docs/theory_graph_protocol.md`.
That source belongs to checkout revision `42b0762e4ce382efa153a969e8bb44bb77537844`
with uncommitted work. Its SHA-256 is
`c30a13bdbc59ba41ac20b72b1c77d75c4c84668f75123c713e672adf858fb8b6`.
The original remains preserved. This version limits the active contract to the
implemented briefing interface and manual handoff; it changes no scientific
ledger, proof, or claim status.
