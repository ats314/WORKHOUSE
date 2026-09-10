# Workspace operations for agents

Use this guide for checkout selection, source intake, concurrent work and
closeout. It is the versioned operating contract shared by the local workspace
and GitHub clones. Outer navigation points here; dated audits record observed
state separately. The [working agreement](../CLAUDE.md) governs scientific
evidence and publication, and [workspace coordination](workspace_coordination.md)
records the archive layout and its reconciliation history.

## Select the working location

On the maintainer's workstation, `C:\WORKHOUSE` is the research workspace and
`C:\WORKHOUSE\REPO` is its canonical integration checkout. Read the outer
`WORKSPACE.json` for workspace roles and `navigation/relocations.json` for
physical locations and original-path redirects. These local records are the
source of truth for path selection; dated folder lists describe their own
observation. A fresh clone elsewhere is its own repository root; Windows archive
paths are local provenance, not installation requirements. Keep versioned tools
and guides relative to that root.

| Work | Destination |
| --- | --- |
| Integrated sources, proofs, checks and ledgers | The selected repository checkout's established directories |
| A concurrent implementation task | `C:\WORKHOUSE\worktrees\<topic>-<YYYYMMDD>` on its own named branch |
| Newly received, unsorted material | `C:\WORKHOUSE\INBOX\<topic>_<YYYYMMDD>` |
| Standalone investigation | `C:\WORKHOUSE\research\<topic>_<YYYYMMDD>` |
| Organized historical collections | `C:\WORKHOUSE\ARCHIVE\collections`, `publications` and `calculations`; follow the relocation map |
| Relocated historical worktrees | `C:\WORKHOUSE\worktrees\legacy`; inspect Git registration before use |
| Local scratch inside any clone | `.workhouse-local/<task-id>/`, ignored by Git |
| Preserved quarantine batches | `C:\WORKHOUSE\quarantine`; keep each batch's manifest and move record |

Use descriptive topics and the existing date conventions. Add a short README
that states purpose, sources, commands, outputs and current disposition. Record
a deliberate suffix when a task needs a second instance. Preserve source
locators and record path mappings when carrying out an authorized rename.

The September 10, 2026 physical organization placed historical collections in
the archive groups above and the autonomous worktree under `worktrees/legacy`.
The local relocation map identifies hidden compatibility junctions at their
original paths. A junction redirects to the same payload; it is not another
copy to remove. Preserve these aliases for existing scripts and source links.
Use the archive navigation's original-path links when a historical document's
relative links depend on that base. Do not recursively count both an alias and
its target as independent source collections.

`ALL THEORY`, nested `WORKHOUSE` directories and older named worktrees are
preserved sources. Their names do not make them current defaults. Do not create
another Git checkout inside an archive collection, re-clone an archive's nested
repository as cleanup, or copy an entire project to start an ordinary task.
Select the appropriate existing checkout or a registered task worktree instead.
The [physical-organization record](workspace_coordination.md#physical-organization-september-10-2026)
describes the completed move and the deferred Git/storage work.

## Start with an observed Git and command state

Read the selected checkout's README, AGENTS, CLAUDE, FRONTIER and CERTIFIED.
Inspect identity and pending work before changing files:

```text
git rev-parse --show-toplevel --git-common-dir
git status --short --branch
git remote -v
git worktree list --porcelain
python scripts/workspace_status.py --workspace-root C:/WORKHOUSE --remote
uv run --no-sync workhouse --help
```

The [workspace status tool](../scripts/workspace_status.py) is read-only. The
explicit workspace root is for this workstation; use its `--help` to select the
appropriate scope in another clone. Record the local HEAD, branch, remote URL,
observed remote tip and observation time. Without a successful remote read,
state that remote freshness is unavailable. Remote-tracking refs are a local
snapshot until compared with the server. A live remote tip need not already
exist in the local object database.

Do not switch or reset a dirty canonical checkout to catch up. Coordinate a
single owner to refresh shared refs with `git fetch origin`, inspect the actual
differences and select a base that preserves pending work. A separate task
worktree can begin from a verified integration base while existing work is
reconciled. Check live GitHub before calling a result absent from the project.

Check documented CLI interfaces against the selected executable's help. If
session instructions require `workhouse brief`, confirm it is listed and inspect
`workhouse brief --help` before using its startup and task-record options. If it
is unavailable, report the unavailable interface and record the checkout and
help output in the task handoff. A successful `frontier --brief` or `why` query
does not certify the same briefing semantics. Follow the selected checkout's
available graph protocol and keep the requirement unresolved until the actual
interface is restored or the maintainer directs a different workflow.

For mathematical work, read the [current research map](current_research.md),
query the relevant graph IDs and follow the
[formalization workflow](formalization_workflow.md). Operational inventory,
source hashes and a clean Git status do not establish mathematical validity.

## Claim a task and coordinate shared writers

Before editing, record the task under the outer `navigation/tasks/` on this
workstation. Include the task ID, owner, purpose, checkout path, branch, starting
commit, exact owned paths, shared resources, current state and handoff location.
Read other active records and announce ownership conflicts before proceeding.
On another machine, use an identified local coordination directory outside
versioned research sources and communicate the same record to collaborators.

These records are cooperative ownership notes, not an automatic filesystem
lock. Recheck status and affected diffs when another agent may have changed the
same checkout. Keep independent implementations in task worktrees. Shared
ledgers, import roots and generated scientific views need an agreed integration
owner even when the source edits were isolated.

Serialize processes that write shared Lean packages, imports or build state.
Likewise serialize catalogue, frontier, certified-view and proof-export writers
against the intended source revision. Use the documented regeneration order
after their inputs change. Do not regenerate scientific views merely to tidy
navigation, and do not borrow a different checkout's editable Python install
without verifying where its imports resolve.

Keep logs, temporary exports and navigation preservation for portable clone
work under `.workhouse-local/<task-id>/` or another explicitly recorded local
preservation directory. Ignored files remain part of the preservation review;
they are not automatically disposable or included in GitHub history. Move a
selected reproducible result into its proper versioned location with source
identity and validation when integrating it.

## Receive and integrate source material

Create an intake folder under `INBOX/<topic>_<YYYYMMDD>` on this workstation.
Retain the received filenames and bytes. Its README names the source, intake
purpose and intended review route. Record each original path or source URL,
received date, preserved relative path, byte count and SHA-256 in a source
manifest. Keep unavailable sources explicitly marked unavailable.

Search existing inventories and exact source values before making another
derivation or copy. Intake and matching hashes establish source identity; they
do not mean the material is mathematically reviewed, incorporated or published.
Preserve failed attempts and conflicting statements with their source lineage.

A standalone campaign follows the existing `research/<topic>_<YYYYMMDD>`
convention. Integrate only the selected package into the checkout's existing
`paper/`, `docs/`, `notes/`, `runs/`, source or Lean structure. Record the original
source and the actual statement, hypotheses and dependencies using the native
ledgers. Keep the original intake and campaign in place after integration.
Elsewhere, keep intake in an explicitly identified local directory; do not add
the entire outer archive or local scratch to a repository commit.

## Close and publish a task

Review the working diff and staged diff, then stage only the task's exact
reviewed paths. Apply checks for the changed inputs and preserve their revision,
commands, results and limitations. Documentation-only changes follow
[documentation maintenance](documentation_maintenance.md); mathematical work
retains its independent proof and evidence requirements.

Follow the [working agreement](../CLAUDE.md) to publish and merge green work.
Before merging, refresh the observed remote base, check the exact PR head's CI,
resolve actionable review and preserve concurrent changes. Confirm the merged
commit and the resulting files on GitHub main. State separately what is local,
pushed and merged, and distinguish PR validation from post-merge CI.

Finish the task record with changed paths, local and remote commits, PR and CI
links, source/preservation records, remaining working files and next owner or
stopping point. Retain the completed record as the archive entry. A merged PR
does not prove that every file in its worktree was captured. Task closeout
does not delete files or implicitly remove a worktree.

## Carry out authorized organization with preservation

Follow the user's existing authorization and the agreed scope. The September
10 organization included authorized physical moves and quarantine; do not
restart an approval loop for work already covered by that instruction. Record
source and destination paths, preservation evidence, unique local commits and
files, dependencies and the restoration route. Seek clarification only when an
action falls outside the existing authorization or would change the agreed scope.

Trace Git common directories, linked-worktree metadata, junctions, runtime
installs, active processes and scripts that read the path. The workstation's
shared Git administration remains at `ALL THEORY/WORKHOUSE/.git`; REPO also
uses Lean packages through a junction into that earlier checkout. A clean
checkout, an older filename or a GitHub copy is
insufficient evidence that moving the directory is safe.

Before moving a Git/runtime-dependent location, coordinate writers and preserve
the relevant working files, including untracked and ignored content, plus Git administration,
local refs, reflogs and worktree metadata. Verify preserved bytes and record
inaccessible paths as incomplete. A Git bundle is useful additional evidence
for reachable history; it does not preserve all working files or administrative
state. A fresh GitHub clone does not capture unpublished local work.

Record each relocation, repair its affected dependencies and verify the result
against its preservation record. Retain the original-path redirects identified
by `navigation/relocations.json`; do not remove one as a duplicate folder.
Preserve source bytes, failed attempts and pending work throughout. Organization
does not imply deletion, deduplication, resetting a checkout or automatic
worktree removal.
