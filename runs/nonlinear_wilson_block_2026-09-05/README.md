# Nonlinear Wilson block evidence, 2026-09-05

This run preserves three canonical analytic proofs: the global vertical barrier,
the near-identity ground-bundle relative form, and the actual full-block fast
compression with its exact Schur realization. Their general operator arguments
remain analytic. The five native T1 checks certify specified finite PSD/trace,
SU(2), scalar-budget, geometry and compression identities. They do not certify
the complete analytic conclusions, volume-uniform estimates or a continuum limit.

The native report is `certificate.json`; all nine inputs are copied byte for
byte under `source/`. The original conservative and sharpened global derivations,
ground-bundle and full-complement drafts, all three independent audits, and all
three original exact-control programs/reports are preserved at the run root.
Historical pre-format/pre-locator certificates are left in the original outputs;
they are not advertised as replayable against a later source snapshot here.

From the repository's declared environment (`uv sync --all-extras --frozen`):

```powershell
.venv/Scripts/python.exe -B runs/nonlinear_wilson_block_2026-09-05/replay_frozen.py
```

This command loads only the pinned native files under empty package paths,
recomputes every native payload/check record and all original control payloads,
rejects four corrupt or incomplete mathematical inputs, and prohibits NumPy/SciPy
imports. It validates the complete manifest before and after without changing
evidence. Existing outputs and optimized Python are separately rejected.

The original global-barrier verifier records outputs-relative source paths.
`original_tree/` preserves that exact layout, both original proof versions and
all predecessor inputs, so its unchanged `source_hashes()` and original replay
work after relocation. The top-level source/report copies preserve canonical
documentation links; to run that original CLI directly, use its copy beneath
`original_tree/outputs/wilson_complete_band_20260905/next_scale/next_nonlinear/`.
The main `replay_frozen.py` invokes that correctly located original replay.

The seven new Lean lemmas formalize real-scalar inequalities under explicit
analytic inputs. They do not formalize SU(N), elliptic operators, spectral
min-max, a ground bundle, the full-block vacuum or a volume limit. The original
strict scalar build and complete strict canonical build are captured under
`lean/`; all seven canonical modules, the original scalar source and locked
Lean project metadata are under `source/lean/`. Both builds used the same pinned
Lean compiler and warning-as-error mode. No .olean binaries are required or
included. Python replay checks the recorded source/build pins; it does not
rerun the compiler or prove the reported compilation outcome anew.

For an independent compiler replay, use the copied `source/lean/` project with
its pinned toolchain and dependency manifest, obtain the declared Mathlib
dependencies, and run `lake build --wfail`. The captured helper scripts retain
their original absolute paths as provenance; those paths are not needed by
the exact Python replay. `canonical_build_result.json` and the strict log identify
the compiler, commands, source digests and output digests actually observed.

`source_integrity.json`, `copy_provenance.json` and `SHA256SUMS` record unchanged
inputs and the exact complete file set. `canonical_link_validation.json` checks
all planned run links and current local links in the maintained summaries and
three new notes. `negative_control_validation.json` records tamper, overwrite
and -O rejection. `cold_relocation_validation.json` records a copied-run replay
outside the checkout with -I, no PYTHONPATH and source-read auditing, plus a
fresh copied-runner certificate matching every non-runtime field. This uses
the existing declared interpreter environment rather than claiming a fresh
dependency installation. No previous sealed run is modified.
