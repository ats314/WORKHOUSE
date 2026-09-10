# Formalization and proof connections

Use this workflow to turn an exact derivation into Lean statements, connect
their mathematical and kernel dependencies, and publish the verified result.
It applies to full analytic arguments as well as algebra. Start from the
[generated proof map](derivation_formalization.md), then read the actual source
and the current [frontier](../FRONTIER.md). The map is an inventory, not a
substitute for evaluating the mathematics.

All commands below run from the selected repository root unless a directory
change is shown. The maintainer's active checkout is `C:\WORKHOUSE\REPO`;
other contributors use their own clone. Follow the
[workspace guide](workspace_coordination.md) and [contribution guide](../CONTRIBUTING.md).

## Choose the complete statement and its inputs

Use `uv run --no-sync workhouse why DERIV:YANGMILLS_RECONSTRUCTION:R2`
or another exact `DERIV:` ID to locate the source, supporting proofs, and
remaining work. Use `workhouse search` or `rg` for exact symbols and values.
Before coding, identify the conclusion, hypotheses, domains, normalizations,
parameter range, dependencies, and downstream result it will enable.

Construct the actual mathematical objects the argument needs. For example,
an operator theorem may require a common form domain, a densely defined
operator, a limiting measure, or a complete source family. Replacing those
objects with scalars, assuming the desired conclusion as an input, or proving
only finite examples does not complete the source theorem. A valid abstract
lemma is useful: register its precise scope and name the remaining realization
step. Do not downgrade a valid analytic result merely because it is novel or
has not yet been formalized.

Coordinate file ownership and serialize aggregate Lean builds and exports.
Check `git status --short` before editing and preserve other agents' changes.

## Keep the source and proof records distinct

| Record | Purpose and fields |
| --- | --- |
| [ledger/documents.yaml](../ledger/documents.yaml) | Native citation aliases; the `CITE:` ID must resolve to the actual source path. |
| [ledger/derivation_statements.yaml](../ledger/derivation_statements.yaml) | `derivation-statements/v1`: source documents with `id`, relative `path`, raw-byte `sha256`, and precise statement groups. |
| [ledger/theorems.yaml](../ledger/theorems.yaml) | `theorems/v1`: every Lean theorem, its exact statement, `proof_sources`, and reviewed links. |
| [ledger/lean_dependencies.json](../ledger/lean_dependencies.json) | Generated `lean-kernel-dependencies/v1`: elaborated dependencies, transitive axioms, and current Lean input fingerprints. |
| [ledger/results.yaml](../ledger/results.yaml) | Curated research conclusions and their mathematical dependencies, scope, status, and evidence. |

The derivation inventory covers every top-level Markdown document in
`docs/derivations/`. A new document needs both its citation alias and inventory
entry. Give each statement a stable `DERIV:` ID and these fields:

- `statement`, `hypotheses`, and source equation labels describe the claim.
- `locator` names its section and line range; `anchor` is literal text present
  in the source. Keep both precise when a maintained document changes.
- `status` and `evidence` use the existing repository vocabularies.
- `depends_on` names actual `DERIV:` prerequisites, not nearby topics.
- `lean` lists proofs covering the complete stated claim. `lean_support`
  contains `{name, scope}` entries for narrower ingredients.
- `remaining` describes the specific unformalized construction or argument.
  A statement without whole coverage must have an explicit remaining step.

The validator checks source identity, anchors, known theorem names, dependency
resolution and cycles. It does not prove that the prose faithfully describes
the Lean statement; that requires reviewing both.

Derivation hashes preserve exact original bytes, including line endings.
Read a digest without changing anything, for example:

```text
uv run --no-sync python -c "import hashlib,pathlib; print(hashlib.sha256(pathlib.Path('docs/derivations/yangmills-reconstruction.md').read_bytes()).hexdigest())"
```

Lean fingerprints use strict UTF-8 with only CRLF/CR-to-LF normalization
(`utf8-lf`). They cover Lean sources, the import root, dependency extractor,
and toolchain/package pins. These two hash policies serve different purposes;
do not normalize received derivation files to repair a hash failure.

## Preserve a correction's history

Preserve the received source and its previous digest. For a mathematical
correction, add a dated correction or successor with an explicit link to the
affected section and record the corrected verdict in maintained ledgers and
navigation. Keep the original assertion and the reason it failed findable.
Follow [documentation maintenance](documentation_maintenance.md) when revising
maintained prose.

If a maintained derivation genuinely must change, preserve its prior bytes,
review the exact diff, explain the correction, and update its current source
hash, locators and mirrored `proof_sources` together. Do not rewrite a sealed
run, historical source manifest, or earlier validation report to match the
new text. A fresh hash proves identity of the new file, not the mathematics or
continuity with an old proof.

## Implement, register, and map each declaration

Add the proof to the appropriate module under `lean/Workhouse/`; import a new
module from [Workhouse.lean](../lean/Workhouse.lean). State the source's actual
assumptions. No `sorry`, `admit`, or new axiom may stand in for the proof.
Use [lean/CLAUDE.md](../lean/CLAUDE.md) for the local proof agreement.

Register every theorem, including helper lemmas, in `ledger/theorems.yaml`.
The kernel export resolves short registered names, so use unique theorem
names across namespaces. Definitions appear in the dependency export but do
not replace theorem registration. For a derivation proof, each `proof_sources`
entry records:

```yaml
proof_sources:
  - statement: DERIV:EXAMPLE:STATEMENT
    path: docs/derivations/example.md
    sha256: "<exact source-byte digest>"
    locator: "<section and line range>"
    anchor: "<literal source text>"
    scope: "<what this declaration proves under which hypotheses>"
```

This is a field template, not a source record to copy unchanged. Match its
statement/path/hash/locator/anchor to the derivation entry and its scope to the
actual theorem and any `lean_support` entry.

| Link | Meaning |
| --- | --- |
| Derivation `lean` -> graph `LEAN:... formalizes DERIV:...` | Complete coverage of the named source statement, possibly by several declarations jointly. |
| Derivation `lean_support` -> graph `DERIV:... supported_by LEAN:...` | The stated ingredient only; record its exact scope and remaining obligations. |
| Theorem `formalizes` | Reviewed links to other complete named catalogue claims. Leave empty when only partial support is proved. |
| Theorem `promotes` | Exact registered computational-check names whose whole statements are proved, alone or jointly. It is not a source citation. |
| Generated Lean `depends_on` | Actual elaborated type/proof dependencies through local definitions to the next registered theorem. |
| Curated derivation/result `depends_on` | Mathematical inputs in the source argument; these are separate from kernel proof dependencies. |

A supporting lemma does not promote the source argument. Mathematical status,
evidence level, and machine-verification tier remain separate even after adding
whole-statement links. Review complete hypotheses and conclusions before
changing coverage or a gap route.

## Export, render, and check

Install the Python environment with `uv sync --all-extras --frozen`. For elan,
the pinned Lean toolchain, and the mathlib cache, use
[lean/README.md](../lean/README.md). The exporter requires `lake` on `PATH`;
unlike `make lean`, it does not add the elan directory itself.

For an isolated proof iteration, from `lean/`, run a specific imported module
target, for example `lake build Workhouse.SpectralReconstruction --wfail`.
This is a focused build, not a certificate for all final integration inputs.

After finishing changed proofs, imports, pins and theorem registration, run
these commands individually in this order. Stop on the first nonzero exit;
in PowerShell inspect `$LASTEXITCODE` after each native command.

```text
uv run --no-sync python scripts/export_lean_dependencies.py
uv run --no-sync python scripts/render_derivation_coverage.py
uv run --no-sync workhouse index -w
uv run --no-sync workhouse frontier --write
uv run --no-sync workhouse certified --write
```

The exporter runs `lake build --wfail` and the Lean dependency extractor with
warnings treated as errors. On Windows it first builds each imported project
module sequentially. It accepts only the standard transitive axioms
`propext`, `Classical.choice`, and `Quot.sound` for registered theorems, checks
that the source fingerprints still match, and writes the kernel JSON only
after validation. It always builds and exports: there is no read-only
`--check` or `--help` mode. Do not edit the JSON by hand.

The proof-map renderer reads the source and kernel ledgers. The catalogue
command iterates to a fixpoint; frontier and certified views must follow it.
On Linux/macOS, `make regen` performs only those last three steps; it does not
export Lean dependencies or render the proof map. Do not use `make -j regen`,
because the catalogue must finish before its dependent views. Optional
`uv run --no-sync workhouse atlas` renders `atlas.html` last; it is a local
view and is not checked in.

When Lean sources, imports, pins and registration are unchanged, reuse the
validated current kernel export. A change only to source coverage can begin at
the proof-map render. A prose-only change to maintained documentation should
leave scientific inputs and generated views unchanged.

Focused connection checks after scientific regeneration:

```text
uv run --no-sync python scripts/render_derivation_coverage.py --check
uv run --no-sync pytest -q tests/test_derivation_statements.py tests/test_lean_dependencies.py
uv run --no-sync workhouse why DERIV:YANGMILLS_RECONSTRUCTION:R2
uv run --no-sync workhouse why LEAN:reflection_kernel_gram
git diff --check
```

The test files validate source identity, scoped versus whole links, dependency
records, fingerprints and the generated graph. The examples use real stable
IDs; also inspect the IDs you changed. Complete the applicable broader
verification from [CONTRIBUTING.md](../CONTRIBUTING.md). These focused tests
do not replace mathematical source review or a required full suite.

For maintained documentation only, use:

```text
uv run --no-sync python scripts/check_docs.py
git diff --check
```

Check the stated commands against their implementations and verify that
scientific inputs/views have no unintended diff. Do not regenerate them merely
to update prose. Run affected focused tests when the documentation tooling
itself changes.

## Publish and verify the landed commit

Review and stage exact owned paths, commit, and record `git rev-parse HEAD`
with the checks actually run. Push that tested commit, explain its exact
result and remaining obligations in the PR, and inspect CI and reviews for
the current head. Useful read-only checks, replacing `PR_NUMBER`, are:

```text
gh pr view PR_NUMBER --json headRefOid,baseRefOid,baseRefName,mergeable,mergeStateStatus,statusCheckRollup,reviews
gh pr checks PR_NUMBER
```

Inspect unresolved review threads as well as the summarized review state.
Recheck when the head or base changes. Fix failures and conflicts, retain other
agents' work, and rerun affected checks. Follow the repository's standing
[landing agreement](../CLAUDE.md): merge green work through the normal PR path,
subject to an explicit review-only instruction and branch protections. A
`gh pr merge` invocation can pin the checked head with
`--match-head-commit TESTED_SHA`; use the repository's allowed merge strategy
and never bypass protection or delete preserved work as a cleanup step.

After merge, inspect `gh pr view PR_NUMBER --json state,mergedAt,mergeCommit`.
Fetch the current remote without resetting the shared checkout, then inspect
the merged files and source/proof/graph records on `origin/main`. Verify the
merge is present even if another commit has since advanced main, and check
post-merge CI separately. Report whether work is local, pushed, merged, and
verified on main; do not report a queued or earlier run as current success.

[CI](../.github/workflows/ci.yml) presently runs Python checks, shell lint, a
strict Lean build, and Windows catalogue/CLI checks. Its Lean job runs
`make lean`; it does not freshly export kernel dependencies. The Python checks
validate the committed export. Perform the local export when its inputs change
and preserve the corresponding verification evidence.
