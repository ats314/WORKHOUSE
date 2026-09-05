# Continuum scale-comparison evidence, 2026-09-05

This run preserves six analytic research notes, their original derivations,
seven precisely scoped native checks, and seven original exact-control families.
The native certificate is `certificate.json`; every one of its eleven source
inputs is mirrored byte for byte under `source/`. The sixth note reviews a supplied
coupled-oscillator paper and is preserved as provenance, not an additional native
mathematical certificate. No new Lean theorem is claimed by this run.

The proved analytic results cover fixed-cell physical harmonic gaps, positive
interface comparison, the periodic three-dimensional Coulomb fast Hessian bound,
Gaussian history observability, and conditional closed-form Schur spectral/frame
comparison. They retain the torus zero modes, source-coordinate distinctions,
and the open nonlinear Wilson fast-form, history/locality and continuum hypotheses.
Finite controls certify the displayed algebra and examples; they do not substitute
for the general proofs. The raw-vacuum projection counterexample is additional
exact evidence and is deliberately not counted as an eighth native check.

From a repository environment installed using `uv sync --all-extras --frozen`:

```powershell
.venv/Scripts/python.exe -B runs/continuum_scale_comparison_2026-09-05/replay_frozen.py
```

The replay uses only pinned native modules under empty package paths, checks
both native payloads and every invariant record, and recomputes all seven original
control payloads. It prohibits NumPy/SciPy imports. The two original Gaussian
scripts write beside their source, so byte-identical copies run in fresh temporary
directories; the frozen original scripts and JSONs remain unchanged. The other
originals are called through their read-only calculation functions. Five corrupt
spectral/window inputs must be rejected. `python -O`, certificate overwrites and
manifest corruption are separately rejected in `negative_control_validation.json`.
`SHA256SUMS` covers the exact complete file set and forbids bytecode caches.

`copy_provenance.json` records every source and unchanged copy. The archived curl
predecessor is portable at `provenance/EXTRACT_02_Wilson_Hessian_Discrete_Curl.md`
(SHA256 `ab2c9981fecceba6d4c4ed88ac6e9df8936908d3a7bbf2317acfbe0a24a8983b`).
The user-supplied PDF is `provenance/quantumrep-01-00009.pdf`; its text, three selected
page images, exact method controls and independent review remain at the run root.
The paper is compared at its actual coupled-oscillator scope; it is not asserted
to prove a Yang-Mills result. Canonical proof links are checked in
`canonical_link_validation.json`. Frozen dependency metadata is under `environment/`.

`source_integrity.json` records equal hashes before and after assembly. The native
runner independently checks its own source hashes before and after calculation.
The final read-only replay also rechecks the complete manifest after all work.
The saved replay log was generated while assembling this new run; final sealing
and a further read-only replay are reported to the parent research task.
