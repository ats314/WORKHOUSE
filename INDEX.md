# WORKHOUSE agent index

This is a navigation map for **this checkout**. Read [README.md](README.md) for the operating manual, [AGENTS.md](AGENTS.md) for research posture, and [CLAUDE.md](CLAUDE.md) for local rules. Check `git status --short` before editing.

## Task routes

| Task | First file | Next source |
|---|---|---|
| Establish the recorded frontier | [FRONTIER.md](FRONTIER.md) | [CERTIFIED.md](CERTIFIED.md), then the cited claim-specific check |
| Find a claim, exact value, or dependency | [Claim catalogue](index/claims.jsonl), [graph](index/graph.jsonl) | `workhouse why <id>`; `workhouse search <value-or-symbol>` |
| Identify governing obligations | [Governing register](ledger/governing_register.yaml) | [Gaps](ledger/gaps.yaml), [theorems](ledger/theorems.yaml) |
| Read or extend an exact calculation | [Invariants](src/workhouse/invariants/) | [Source instructions](src/workhouse/CLAUDE.md), [tests](tests/) |
| Locate a formal theorem | [Lean guide](lean/README.md) | [Workhouse Lean sources](lean/Workhouse/) |
| Trace an imported scientific statement | [Theory](theory/), [corpus import](corpus-import/) | Its source manifest and the claim graph |
| Follow original notes and review queues | [Notes guide](notes/README.md) | [Notes register](ledger/notes.yaml), `workhouse notes --queue` |
| Find external supporting work | [Literature guide](literature/README.md) | [Literature index](literature/index.yaml), `workhouse lit --for <id>` |
| Find manuscript sources and build recipes | [Paper guide](paper/README.md) | [Paper sources](paper/), linked evidence and reproduction commands |
| Reproduce a saved run | [Runs](runs/) | The selected run's README, scripts, outputs, and hashes |
| Understand a prior design or failed route | [Documentation](docs/) | `workhouse why <id>` and the relevant recorded decision |
| Set up or validate a change | [Contributing](CONTRIBUTING.md), [project metadata](pyproject.toml) | [Makefile](Makefile), local instructions and targeted tests |

## Command lookup

Use an environment configured for this checkout. In PowerShell, from its root:

```powershell
git status --short
uv sync --all-extras --frozen
uv run --no-sync workhouse --help
uv run --no-sync workhouse why G19
uv run --no-sync workhouse search '5/612'
uv run --no-sync workhouse lit --for G19
```

`uv sync` is environment setup, not a prerequisite for reading the checked-in navigation. Existing environments may need repair; an executable's presence does not confirm it can import the package. The Makefile recipes use Bash and `.venv/bin`, so consult the explicit commands when using PowerShell.

The command printed with a claim in `CERTIFIED.md` is the shortest route to rechecking that claim. Counts and statuses belong in the generated views rather than this index. Their presence alone does not mean this session reran the checks.

## Sources versus generated views

| Maintained source | Generated navigation/evidence view |
|---|---|
| `ledger/`, invariant implementations, formal sources, source records | `index/claims.jsonl`, `index/symbols.jsonl`, `index/graph.jsonl` |
| Registered checks and the claim catalogue | `FRONTIER.md`, `CERTIFIED.md` |

When substantive work requires refreshing these views, run the repository's existing generators in order:

```powershell
uv run --no-sync workhouse index -w
uv run --no-sync workhouse frontier --write
uv run --no-sync workhouse certified --write
```

Do not hand-edit them. Immutable corpus, run, and imported-note files retain their own provenance rules. This index does not revise scientific claims or replace the local working agreement.
