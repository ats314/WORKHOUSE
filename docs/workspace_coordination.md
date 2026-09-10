# One active repository, a preserved research archive

The maintainer's four-year collection is `C:\WORKHOUSE`. The GitHub repository
is [ats314/WORKHOUSE](https://github.com/ats314/WORKHOUSE). They coordinate through
the canonical checkout **`C:\WORKHOUSE\REPO`**. `ALL THEORY` is an archive
collection within the larger workspace, not the name or root of the active project.

The versioned [workspace operations](workspace_operations.md) guide is the shared
operating contract for local and GitHub agents. Follow it for startup, intake,
task ownership, shared writers, closeout and quarantine review. This guide
records the workspace layout and reconciliation history.

The canonical reconciliation and source-linked formalization were merged in
[PR #113](https://github.com/ats314/WORKHOUSE/pull/113), merge commit `742033a`.
This is the integration baseline, not a permanent assertion about the latest
GitHub revision. Check live Git state before starting work.

The Windows paths in this guide describe the maintainer's workstation. A fresh
GitHub clone elsewhere is a normal repository checkout; it does not require
copies of the outer archive to run the tracked project. Use repository-relative
paths for portable docs, proofs and tools, and treat unavailable external source
paths as provenance to resolve rather than files to invent.

For the workstation's current physical layout, read
`C:\WORKHOUSE\WORKSPACE.json` and `C:\WORKHOUSE\navigation\relocations.json`.
The former identifies workspace roles; the latter records each relocated path
and whether an original-path junction exists. Use these local records when a
historical path or older folder list differs from the current layout.

## Which location to use

| Location | Role | Default action |
| --- | --- | --- |
| `C:\WORKHOUSE\REPO` | Active GitHub-based source, proofs, graph and curated evidence | Start and integrate new repository work here. |
| `C:\WORKHOUSE\research` | Dated standalone investigations | Preserve the campaign, then integrate selected results with exact source locators. |
| `C:\WORKHOUSE\ARCHIVE\collections` | Organized historical proof, manuscript, simulation and reference collections | Follow the archive index and retained source lineage. |
| `C:\WORKHOUSE\ARCHIVE\publications` | Preserved manuscript and publication packages | Select the exact edition and its evidence. |
| `C:\WORKHOUSE\ARCHIVE\calculations` | Historical computational campaigns and their outputs | Keep scripts, source inputs, manifests and checkpoints together. |
| `C:\WORKHOUSE\ALL THEORY` | Historical corpus collection | Search and cite it as source evidence. |
| `C:\WORKHOUSE\ALL THEORY\WORKHOUSE` | Preserved earlier checkout, local work and shared Git database | Recovery and provenance; do not use as the default for new work. |
| `C:\WORKHOUSE\worktrees\legacy` | Relocated historical Git worktrees | Inspect Git registration and use only for an explicitly selected source or branch. |
| Named branch worktrees | Preserved research branches and review checkpoints | Use only when a task selects that branch. Reconcile results into the canonical checkout. |
| `C:\WORKHOUSE\quarantine` | Recorded preservation batches | Follow their manifests and move records. |
| Other folders under `C:\WORKHOUSE` | Original proofs, manuscripts, code, archives and references | Follow the workspace directory index and corpus review queue. |

The canonical directory is a real Git worktree, not another copied project or
a junction into the old checkout. During the September 9 reconciliation its initial branch was
`codex/workspace-reconciliation-20260909`, based on refreshed `origin/main` at
`925d459e03a7932c96a5e65a96269a808f4bccca`. The nested checkout was 44 commits
behind that history and had uncommitted work. Reconciliation combined both
sources; neither the older working files nor their Git history were reset.
That branch was merged through PR #113. It is historical setup information;
use the current branch and task scope instead of switching back to it by default.

The shared Git administrative directory remains at
`C:\WORKHOUSE\ALL THEORY\WORKHOUSE\.git`. REPO's Lean packages also use a
junction to that checkout's `lean/.lake/packages`. Both dependencies remain
operationally required. A later storage migration must preserve the Git and
working state, repair worktree metadata and provide the required dependencies.

## Physical organization: September 10, 2026

The authorized first physical pass grouped historical sources into
`ARCHIVE/collections`, `ARCHIVE/publications` and `ARCHIVE/calculations`, moved
the autonomous worktree with Git to `worktrees/legacy/autonomous-20260905`, and
preserved the selected clutter/test trees in a dated quarantine batch. File
hash verification and the move journals are recorded locally under
`navigation/checkpoints/2026-09-10-workspace-organization/`; the closeout is
`physical-organization-result.json` in that directory.

Archived collections and the relocated worktree retain hidden directory
junctions at their original paths. Those entries are compatibility redirects
to the same files, not duplicate payloads. Preserve them. The archive index
uses the original-path redirects so historical relative links retain their
original base. The relocation map separately records quarantine paths without
redirects; do not infer that every old path has an alias.

At that closeout, Windows denied the flat-holonomy worktree move, so
`WORKHOUSE-flat-holonomy-20260907` remained at its original root path. Shared Git
storage under `ALL THEORY/WORKHOUSE`, canonical REPO's dirty-work reconciliation
and synchronization with GitHub, and the mixed application/runtime collections
remained for later focused work. The physical organization did not merge that
pending research. Inspect the current status before continuing a deferred task.

## Start a session

Follow the [startup procedure](workspace_operations.md#start-with-an-observed-git-and-command-state)
to select the checkout, inspect pending work, observe the remote and verify
available commands. Then read the [current research map](current_research.md)
for mathematical work and [formalization workflow](formalization_workflow.md)
for source-to-proof integration.

From the outer workspace, `workhouse.ps1 where`, `workhouse.ps1 doctor`, and
`workhouse.ps1 why G19` route through the canonical path in `WORKSPACE.json`.
`G19` is an example query target; substitute the ID relevant to your task.
The doctor uses local Git references; it does not claim to have fetched GitHub.

Coordinate exact file ownership when agents work concurrently. Preserve
uncommitted changes and stage only the intended files. Agree on one process
for shared Lean dependency/build state and generated scientific views. A
separate task's successful build is useful evidence only for its actual revision
and checked scope.

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
   Source statement mappings belong in `ledger/derivation_statements.yaml`;
   follow the formalization workflow for whole proofs and scoped ingredients.
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

The [recent-research integration run](../runs/recent_research_integration_2026-09-09/README.md)
retains checks from its recorded checkout and stage. The later
[analytic formalization run](../runs/analytic_formalization_2026-09-09/README.md)
freezes the new proofs, source inventory and dependency evidence integrated in
PR #113. Use live ledgers, generated views and the validation for the revision
being reviewed to assess subsequent changes. Do not relabel either old record
as a fresh execution or edit a frozen run to describe new work.

Maintained READMEs, indexes and workflow guides may be refreshed. Preserve their
previous bytes and original path/hash before a revision in this workspace, using
`navigation/preserved/<dated-change>/`. Keep those navigation backups separate
from scientific run manifests. Dated derivations, source snapshots, failed
attempts and original runs retain their source history; record a correction
and explicit relationship rather than silently changing their historical claim.
