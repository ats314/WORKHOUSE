# One active repository, a preserved research archive

The maintainer's four-year collection is `C:\WORKHOUSE`. The GitHub repository
is [ats314/WORKHOUSE](https://github.com/ats314/WORKHOUSE). They coordinate through
the canonical checkout **`C:\WORKHOUSE\REPO`**. `ALL THEORY` is an archive
collection within the larger workspace, not the name or root of the active project.

## Which location to use

| Location | Role | Default action |
| --- | --- | --- |
| `C:\WORKHOUSE\REPO` | Active GitHub-based source, proofs, graph and curated evidence | Start and integrate new repository work here. |
| `C:\WORKHOUSE\research` | Dated standalone investigations | Preserve the campaign, then integrate selected results with exact source locators. |
| `C:\WORKHOUSE\ALL THEORY` | Historical corpus collection | Search and cite it as source evidence. |
| `C:\WORKHOUSE\ALL THEORY\WORKHOUSE` | Preserved earlier checkout, local work and shared Git database | Recovery and provenance; do not use as the default for new work. |
| Named branch worktrees | Preserved research branches and review checkpoints | Use only when a task selects that branch. Reconcile results into the canonical checkout. |
| Other folders under `C:\WORKHOUSE` | Original proofs, manuscripts, code, archives and references | Follow the workspace directory index and corpus review queue. |

The canonical directory is a real Git worktree, not another copied project or
a junction into the old checkout. Its initial branch is
`codex/workspace-reconciliation-20260909`, based on refreshed `origin/main` at
`925d459e03a7932c96a5e65a96269a808f4bccca`. The nested checkout was 44 commits
behind that history and had uncommitted work. Reconciliation combines both
sources; neither the older working files nor their Git history were reset.

The shared Git administrative directory remains under the preserved nested
checkout. The local Lean dependency cache also reuses the same pinned packages.
Do not remove or move that directory. A later physical storage migration must
repair Git worktree metadata and provision an independent dependency cache.

## Start a session

Read this checkout's README, AGENTS, CLAUDE, generated FRONTIER and CERTIFIED.
Then check identity and pending work:

```powershell
Set-Location -LiteralPath 'C:\WORKHOUSE\REPO'
git status --short --branch
git remote -v
git fetch origin
git log --oneline --left-right HEAD...origin/main
uv run --no-sync workhouse why G19
```

From the outer workspace, `workhouse.ps1 where`, `workhouse.ps1 doctor`, and
`workhouse.ps1 why G19` route through the canonical path in `WORKSPACE.json`.
The doctor uses local Git references; it does not claim to have fetched GitHub.

## Bring archive work into the repository

1. Locate the existing source before creating another derivation. Use the outer
   path index, the full-corpus notes inventory and exact-value search.
2. Record the original path, bytes or digest, date and source lineage. Preserve
   failed routes and contradictory statements alongside their resolutions.
3. Copy only the source package needed for a result into the established
   `paper/`, `docs/`, `notes/` or pinned `runs/` structure. Retain the original.
4. Register the actual theorem, hypotheses and dependencies. Use
   `ledger/results.yaml` for integrated analytic results and the existing
   recent-research source registry for its preserved September campaigns.
5. Add scoped native checks and Lean declarations where appropriate; regenerate
   the scientific views with the repository CLI. Inventory and hash equality
   establish source identity, not mathematical review.
6. Test the change, stage exact paths, review the diff, and coordinate its GitHub
   integration. Never bulk-add the four-year outer archive or overwrite remote
   work with an older working copy.

GitHub is the shared version history. The outer archive contains additional
historical and working evidence; it is not a claim that every file is published,
reviewed, or already incorporated. The full-corpus queue records that distinction.

## Reconciliation record

The local workspace audit and preserved merge inputs are under
`C:\WORKHOUSE\navigation\reconciliation\2026-09-09`. They record source and
GitHub hashes, automatic matches, reviewed conflicts, imported corpus material
and validation. Earlier navigation bytes are retained under
`navigation/preserved/2026-09-09-canonical-workspace`.

The September integration run remains a dated record of checks in the older
checkout. Use this checkout's generated views and canonical validation report
for the combined state. Do not relabel an old report as a fresh run.
