# Contributing

Use an existing intended checkout before creating another one. On the
maintainer's workstation, new integrated work belongs in `C:\WORKHOUSE\REPO`;
`C:\WORKHOUSE` is the full research workspace and archive. Elsewhere, clone
`https://github.com/ats314/WORKHOUSE` into your chosen working directory.
The [workspace guide](docs/workspace_coordination.md) explains the preserved
older checkouts and the relationship to GitHub.

Read [README.md](README.md), [AGENTS.md](AGENTS.md), [CLAUDE.md](CLAUDE.md),
and the generated [frontier](FRONTIER.md). Inspect `git status --short` and
coordinate file ownership before editing. Preserve existing work, including
uncommitted changes, failed attempts, duplicate sources, and historical runs.
Stage your exact paths; avoid bulk staging another agent's work.

## Setup and navigation

From the checkout root, with Python 3.11 or newer and uv available:

The query uses `G19` as an example. Substitute the graph ID relevant to your
task; the example does not prescribe a research target.

```text
uv sync --all-extras --frozen
uv run --no-sync workhouse --help
uv run --no-sync workhouse search "your exact value or claim"
uv run --no-sync workhouse why G19
```

The uv commands work on Linux/macOS and native Windows. The Make recipes use
Bash and `.venv/bin`, so they are for a Unix-style environment; native Windows
uses uv commands instead. On Linux/macOS, `make bootstrap` is also the CI setup
entry point. It uses the available Python installer; it does not use the
explicit `--frozen` option above. Lean is installed and checked separately:
see [lean/README.md](lean/README.md).

Search exact values, source filenames, and stable claim IDs before deriving
something already present. Check live GitHub history before calling a result
missing. The generated [proof map](docs/derivation_formalization.md) is the
entry point for source statements and remaining Lean obligations.

## Record the result at its actual scope

Every research change states its hypotheses, conclusion, provenance,
mathematical status, evidence, and consequence for the research objective.
Record established analytic results and their dependencies in the appropriate
ledgers, update affected routes, and connect proofs to precise source sections.
Use the [formalization workflow](docs/formalization_workflow.md) for Lean and
derivation records, including every helper theorem.

A finite control or a supporting lemma proves its stated scope. Preserve the
full analytic goal and construct its remaining objects and arguments. Do not
weaken a check, widen a tolerance, assume the desired conclusion, or change a
source to hide a disagreement. Changes to recorded constants cite their exact
source and explain any corrected status.

Keep received and sealed evidence intact. Add a correction or successor with
links to both versions; updating a maintained interpretation does not authorize
re-pinning historical evidence. Review deliberate evidence changes separately.
The [documentation guide](docs/documentation_maintenance.md) describes which
navigation files to update and which views are generated.

For dependency changes, deliberately update `uv.lock` with `make lock` or
`uv lock`, review the diff, then install and validate the result. An ordinary
setup should use the existing lockfile.

## Verification by change type

For a documentation-only change, inspect relative links, stated commands,
source/command consistency, and run:

```text
uv run --no-sync python scripts/check_docs.py
git diff --check
```

Check that scientific ledgers, proofs, pinned sources, and generated views
have not drifted. Do not
rebuild Lean, rerun research suites, or regenerate scientific views solely to
refresh prose. Record the focused checks actually performed and observe the
repository's current CI requirements.

For research, code, proof, or ledger changes, complete their focused checks and
the required repository verification. Linux/macOS:

```bash
make verify
make check
```

Native Windows equivalents for this repository's Python stack:

```powershell
uv run --no-sync workhouse verify
uv run --no-sync ruff check .
uv run --no-sync ruff format --check .
uv run --no-sync python scripts/check_docs.py
uv run --no-sync pytest -q
```

Run each command individually and stop on failure. PowerShell does not
necessarily stop on a native executable's nonzero exit code; inspect
`$LASTEXITCODE` before continuing. If the default pytest temporary directory is
unwritable, pass `--basetemp` with a new, dedicated directory inside the
workspace. Pytest manages that directory, so never point it at source or
existing research files. Shell changes also require the shell lint checks
listed in [CI](.github/workflows/ci.yml). Report any unavailable check explicitly.

The native Windows shell-hook tests need Git for Windows Bash. Check
`Get-Command bash`: a WindowsApps/WSL launcher does not accept the native paths
used by those tests. If Git uses its default installation location, put its
Bash first in this PowerShell session before running pytest:

```powershell
$env:PATH = "C:\Program Files\Git\bin;$env:PATH"
Get-Command bash
```

Use your actual Git installation path if different. This changes only the
current session's executable lookup; it does not change the machine settings.

For changed Lean or theorem registration, use the strict build and kernel
export workflow. For changed scientific inputs, regenerate in order:
kernel export when affected, proof map, catalogue, frontier, certified view;
render the optional atlas last. `make regen` covers only catalogue, frontier,
and certified, and should run without parallel Make. Exact commands and
focused provenance tests are in the
[formalization guide](docs/formalization_workflow.md#export-render-and-check).
Inspect `workhouse why <id>` for the affected source claims and proofs.

## Publish the tested result

Follow the [working agreement](CLAUDE.md). Review the diff, stage only owned
paths, commit, and record the tested commit SHA. Push that commit and open or
update its PR with the result, scope, remaining work, and actual verification.
If the PR head changes, complete the checks affected by that change and wait
for CI on the new head. A green run on an earlier commit is not current evidence.

Inspect CI, review comments, mergeability, and the live base/head before
merging. Land your green work through the normal PR process under the standing
repository authorization; respect an explicit review-only request and branch
protections. Confirm the merge and inspect GitHub `main` for the result and its
graph/documentation changes. Report local, pushed, merged, and post-merge CI
status separately. Fetching remote history does not require resetting or
switching a shared dirty checkout.

Use a short imperative commit subject and explain the reason in the body.
Reference stable claim, derivation, or gap IDs where they help the next reader.
