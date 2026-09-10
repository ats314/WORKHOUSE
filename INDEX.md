# WORKHOUSE task index

Read [README.md](README.md), [AGENTS.md](AGENTS.md), and [CLAUDE.md](CLAUDE.md).
On the maintainer's workstation use `C:\WORKHOUSE\REPO`; elsewhere use your
clone root. Inspect local changes and live GitHub history before deciding that
a result is absent. See [workspace coordination](docs/workspace_coordination.md).
Use the [THEORY GRAPH protocol](docs/theory_graph_protocol.md) for one shared
briefing contract across agents and retain [manual task records](graph-tasks/README.md).

## Choose the maintained source

| Task | Start here | Next source or command |
| --- | --- | --- |
| Start a graph task and retain its provenance | [THEORY GRAPH protocol](docs/theory_graph_protocol.md), [task records](graph-tasks/README.md) | `workhouse brief --startup`, then `workhouse brief ID --json --out PATH` |
| Find current mathematical results and obligations | [Current research](docs/current_research.md), [research goal](docs/research_goal.md) | `workhouse why ID`, then the exact source |
| Reproduce a checked claim | [CERTIFIED.md](CERTIFIED.md), [FRONTIER.md](FRONTIER.md) | Its printed verifier command and hypotheses |
| Trace a derivation into Lean | [Proof map](docs/derivation_formalization.md) | [Statement inventory](ledger/derivation_statements.yaml), `workhouse why DERIV:...` |
| Add or extend a formal proof | [Formalization workflow](docs/formalization_workflow.md), [Lean guide](lean/README.md) | [Theorem register](ledger/theorems.yaml), [kernel dependencies](ledger/lean_dependencies.json) |
| Add an exact or numerical check | [Source guide](src/workhouse/CLAUDE.md), [Contributing](CONTRIBUTING.md) | Matching module in [invariants/](src/workhouse/invariants/), relevant [tests/](tests/) |
| Record a result, route or dependency | [Ledger guide](ledger/CLAUDE.md) | [Results](ledger/results.yaml), [gaps and routes](ledger/gaps.yaml) |
| Interpret an edge or refresh a graph view | [Index guide](index/CLAUDE.md) | [Claim catalogue](index/claims.jsonl), [graph](index/graph.jsonl), generator source |
| Review or import historical research | [Corpus coverage](docs/corpus_coverage.md), [notes guide](notes/README.md) | `workhouse notes --queue`; preserve source identity and review scope |
| Acquire or connect an external paper | [Literature guide](literature/README.md), [literature rules](literature/CLAUDE.md) | [Literature register](literature/index.yaml), `workhouse lit --for ID` |
| Inspect an earlier manuscript or run | [Paper guide](paper/README.md), [runs](runs/) | The selected edition's manifest and dated instructions |
| Update documentation or agent guidance | [Documentation maintenance](docs/documentation_maintenance.md) | [Documentation manifest](docs/documentation_manifest.json), `python scripts/check_docs.py` |
| Publish a verified change | [Contributing](CONTRIBUTING.md) | Exact-path commit, PR checks/reviews, merge, then verify GitHub main |

## Search before broad reading

With the checkout environment configured, prefix commands with `uv run --no-sync`:

```text
workhouse search '5/612'
workhouse brief G19 --json
workhouse why G19
workhouse why DERIV:YANGMILLS_RECONSTRUCTION:R3
workhouse why LEAN:closed_extension_of_integration_by_parts
workhouse lit --for G19
```

An exact value, statement ID, symbol or filename is a better starting point
than recursively reading a large archive. Follow the source's provenance and
scope rather than treating a directory name or timestamp as an authority.

## Sources and generated outputs

| Maintained input | Generated output | Update command |
| --- | --- | --- |
| Lean sources, import root, toolchain pins, theorem registry | `ledger/lean_dependencies.json` | `python scripts/export_lean_dependencies.py` (builds and writes) |
| Derivation statements and theorem registry | `docs/derivation_formalization.md` | `python scripts/render_derivation_coverage.py` |
| Ledgers, registered checks and source records | `index/claims.jsonl`, `index/symbols.jsonl`, `index/graph.jsonl` | `workhouse index -w` |
| Current claim catalogue and registered checks | `FRONTIER.md`, `CERTIFIED.md` | `workhouse frontier --write`, then `workhouse certified --write` |
| Current graph | local ignored `atlas.html` | `workhouse atlas` |

These are command names, not a substitute for the complete ordered
[formalization workflow](docs/formalization_workflow.md). The kernel exporter
requires the pinned Lean environment and a working `lake` on PATH. Do not run
generators just to tidy prose, and never re-pin old research evidence to make
a documentation or integrity check pass.
