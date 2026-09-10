# Manual theory-graph task records

Follow the shared [THEORY GRAPH protocol](../docs/theory_graph_protocol.md).
Use this directory for dated, task-specific handoffs that preserve what an
agent read, what it established, and what remains. Automated task-record
validation is not implemented; reviewers check the record against its retained
snapshots and sources.

Choose a unique name such as `2026-09-10-target-review.md`. Do not replace
an earlier record or snapshot. Record an explicit continuation when a later
task updates the result.

For each task, retain these fields in a short Markdown record:

| Field | Required information |
| --- | --- |
| Identity | Task identifier, date, actual agent/model when known, checkout path, branch and observed Git revision. |
| Target | Graph IDs and the precise question, with hypotheses and regime. |
| Start snapshot | Retained briefing path, `snapshot_fingerprint`, input-manifest digest, freshness and execution provenance. |
| Established inputs | Source paths, statement locators and relevant content hashes; distinguish retrieved records from reviewed arguments. |
| Obligation | The exact statement being investigated and the downstream consequence it would enable. |
| Ownership | Exact files owned or changed, collaborators and shared processes coordinated. |
| Work and checks | Commands actually executed, outcomes, evidence paths, limitations and unexecuted checks. |
| End snapshot | New briefing path and fingerprint; explain relevant changed inputs or state why no end briefing was available. |
| Handoff | Established result or failed route, downstream consequence and remaining successor. |

The snapshot pair below uses `G19` as an example. Replace it with the graph ID
or IDs relevant to the user's task, and replace `TASK` with a new dated task
identifier. The example does not require work on G19.

```text
uv run --no-sync workhouse brief G19 --json --out .graph-state/TASK/start.json
uv run --no-sync workhouse brief G19 --json --live --out .graph-state/TASK/end.json
```

Saved snapshots may be stale or unknown; record that explicitly and follow the
protocol before using them as a current research basis. The end command can run
registered Python checks and reuse observed cached results. Select `--fresh`
only when uncached execution is intended; neither option compiles Lean.

`.graph-state` is local, ignored storage. Before sharing or publishing a task
record, retain the referenced snapshot JSON files with that task's reviewed
evidence package and update the record's locators. A path on one workstation
alone does not make its snapshot available to collaborators. Keep original
snapshot bytes and fingerprints when copying them into a retained package.

There is no automated task-record validation or task-record command in this
implementation. Do not report an automated validation or another agent's
conformance exercise as passed. The record describes observed work; proof review
determines whether the mathematical argument establishes its stated conclusion.
