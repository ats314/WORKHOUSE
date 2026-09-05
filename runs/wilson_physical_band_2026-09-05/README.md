# The complete infinite-volume physical Wilson band

The analytic proof constructs the actual normalized Wilson transfer in
infinite volume, proves its vacuum gap, and identifies its complete isolated
odd band in the physical Euclidean reconstruction. The projected literal
plaquette sources form an onto frame, with Gram between 9/16 and 81/64,
on |u|<=u_star/(10022400000 N), uniformly over admitted volumes and temporal
meshes at fixed rank and spatial spacing.

The proof is [pinned here](source/paper/research_notes/G18_WILSON_INFINITE_VOLUME_PHYSICAL_BAND_20260905.md).
Its mechanisms are local vacuum anchoring, an absolutely convergent activity
limit on local Hilbert spaces, a tagged source Gram-Schur estimate, a
two-sided projection inverse and selective OS cyclicity on the whole band.
Its energy gap is in electric-time units; the spatial continuum trajectory
and physical normalization remain separate obligations.

## Executed finite controls

Five native checks and ten targeted tests pass. The controls compare exact
rotated projections and both inverse identities; centered overlapping source
Grams and an uncentered negative control; noncommuting four-link transfer
matrices and disjoint activity exhaustion with nonzero tails; completeness
counterexamples; and the rational source/gap constants. PSD certificates use
all principal minors. The finite controls do not certify the general
infinite-dimensional theorem or a continuum Yang-Mills theory.

The certificate pins eight executed source files. Independent source and
operator derivations, their audit and exact controls are preserved in
`independent/`. Their conservative intermediate bounds remain valid; the
combined proof uses the stronger direct-rotation bound. The source code
snapshots and all run files are pinned by SHA256SUMS.

## Replay

From the repository root with its pinned Python dependencies:

```text
python runs/wilson_physical_band_2026-09-05/replay_frozen.py
python scripts/verify_wilson_physical_band.py --output outputs/fresh-band-certificate.json
pytest -q tests/test_wilson_physical_band.py
```

The frozen replay loads only the pinned input engine and pinned control
module, verifies source hashes and compares the exact payload. The live
runner refuses to overwrite existing evidence and rejects optimized Python.
