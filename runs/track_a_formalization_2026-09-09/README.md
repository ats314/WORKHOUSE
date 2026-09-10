# Supported Track A formalization

This run formalizes the supported W6, SC17 and G17 statements from the report
supplied on 9 September 2026. The
[successor derivation](../../docs/derivations/track-a-supported-statements.md)
states the exact mathematical scope; the generated
[proof map](../../docs/derivation_formalization.md) and kernel dependencies are
the live source-to-proof records.

## Result and remaining application steps

| Mechanism | Formal result | Remaining model application |
| --- | --- | --- |
| W6 | Actual bounded-Hilbert variational residual identity, continuous-functional dual norm, factorization bound and selected-inverse error certificate; exact Gaussian coefficient substitutions | Construct the complete Wilson residual factorization, prove its diagonal/coercivity budgets, and justify any unbounded form-domain realization |
| SC17 | Continuous small-root barrier, constructed noncommutative Banach fixed point, scalar-reference inverse, and exact default interval | Derive the comparison from the actual Markov/Duhamel evolution and bound the complete outside-pressure, metric, projector and cutoff defect |
| G17 | Source-dependent probability partition bound; actual centered L2 variance and bounded-footprint radius; strict tilt and independent-product growth obstructions | Identify the physical probability/source representation and its admissible footprints; SU(2) Haar construction and moment evaluation remain explicit prerequisites of that specialization |

The four new modules contain 63 registered theorem declarations, organized in
11 successor statement groups. The original W6 and SC17 operator claims receive
explicitly scoped supporting links. No false source-independent constant or
unrestricted source-radius claim is registered as a proved result. This is not
a completion of the interacting continuum problem or the full derivation backlog.

## Preservation and environment

[source_manifest.json](source_manifest.json) records exact bytes and original
paths for the received drafts and arithmetic outputs. Their completion language
is preserved as history. The reviewed successor supplies their current scope.
Existing source files and unrelated uncommitted work were not overwritten.

The work was integrated in the named Git worktree
`C:/WORKHOUSE/worktrees/lean-supported-track-a-20260909`, based on published
main `1d6c079`, while another agent edited the canonical `REPO` checkout.
The canonical workspace default remains `C:/WORKHOUSE/REPO`.
The integration worktree reuses the pinned local package cache and Python
environment. Full Lean builds/exports are serialized on Windows. Concurrent
exploratory builds encountered cache/allocation failures; final validation is
the separately recorded serial run.

Original maintained navigation and ledgers were preserved before revision at
`C:/WORKHOUSE/navigation/preserved/2026-09-09-lean-track-a/manifest.json`.
That organization record is separate from the scientific source manifest.

## Verification

The final run receipt is [verification.json](verification.json). The strict
Lean exporter checks elaborated dependencies and transitive axioms; only
`propext`, `Classical.choice`, and `Quot.sound` are accepted. It does not infer
that an abstract theorem has been realized by the physical Wilson model.

Reproduce from the repository root after installing the pinned environments:

```text
python scripts/export_lean_dependencies.py
python scripts/render_derivation_coverage.py
workhouse index -w
workhouse frontier --write
workhouse certified --write
python scripts/render_derivation_coverage.py --check
pytest -q tests/test_derivation_statements.py tests/test_lean_dependencies.py tests/test_track_a_formalization.py
workhouse why DERIV:TRACK_A_SUPPORTED:W6_E
workhouse why DERIV:TRACK_A_SUPPORTED:SC17_P
workhouse why DERIV:TRACK_A_SUPPORTED:G17_I
```

Use the repository environment, for example `uv run --no-sync` before these
commands. Complete broader checks from [CONTRIBUTING.md](../../CONTRIBUTING.md)
when changing the integrated scientific records. Publication state belongs to
the tested commit and GitHub PR, not to this dated source snapshot.
