# Blocking the actual Wilson transfer: a uniform vacuum expansion and a source-visible window — 2026-09-04

Fourth package from the parallel GPT session, prepared against `8e44da1` and
reviewed here before integration. It continues
`runs/uniform_wilson_window_2026-09-04`: instead of replacing the logarithm of
the Wilson transfer by an auxiliary Hamiltonian, it blocks a fixed physical
duration of the actual transfer and expands the block in a scalar space-time
polymer gas.

## What it establishes, and how far

- **Uniform smoothing and mixing of a physical-time block (analytic).** From the
  heat-kernel minorization and the calibrated one-link gap of the preceding
  note: convolution powers of the one-link Wilson density are uniformly bounded
  at positive time, a block of fixed duration `s₀` is within `δ` of Haar on every
  link once `ε` is small, and the block kernel converges uniformly to the heat
  kernel.
- **A scalar polymer expansion for the actual block (analytic, conditional on the
  abstract cluster theorem).** Free Markov bridges on the links are independent,
  so the block kernel is a hard-core gas of temporal bonds and connected
  magnetic atoms with an explicit, mesh-independent Kotecký–Preiss criterion.
  With `δ ≤ e^{-(4+2ξ)}/16` and `y ≤ 1/256` the atom sum is exactly
  `1/8 + 1/14 = 11/56 < 1/4`, valid on the disc
  `|u| ≤ log(1 + e^{-(16+8ξ)}/(256(1+δ)⁴)) / (J(s₀+τ₀))`. Existential and very
  conservative; the mixing constants behind `s₀` are not evaluated. The suite
  "the blocked Wilson transfer: spectral block, cluster margin, source moments"
  re-derives the margin arithmetic.
- **Consequences (analytic).** The actual Perron vacuum and the full unprojected
  local-source correlations are analytic and exponentially clustering uniformly
  in volume and mesh, with a vacuum gap `≥ ξ/(s₀+τ₀)`; the unprojected odd-source
  correlations converge to the Hamiltonian ones in a weighted space-time sum;
  a two-moment estimate gives a three-orientation source Gram `≥ I/2` in a fixed
  Borel window around the plaquette energy.
- **What it does not establish, by its own account.** That the window is an
  isolated three-component Riesz band, totality of the source frame, or matching
  of the band-projected kernels in the exponentially weighted norm. Section 10
  gives a measure-theoretic counterexample: converging correlators with no
  isolated pole. The package is explicit that these results must not be read
  as closing G18 or G19.

## Files

Pinned as received, checksums in `PACKAGE_SHA256SUMS` (three entries there refer
to files moved or renamed: the two notes now live in `paper/research_notes/` as
`G19_DISCRETE_TIME_VACUUM_AND_WINDOW_20260904.md` and
`G19_WILSON_BLOCKED_VACUUM_INSERT_20260904.tex`, and the package's README is
`PACKAGE_README.md`). `prior/` is the package's own immutable copy of the
preceding note, kept as received.

| File | What it is |
|---|---|
| `verify_discrete_time_bridge.py`, `wilson_clock.py` | 26 finite diagnostics (exact combinatorics, a finite-state bridge model, a one-plaquette SU(3) truncation, negative controls); need NumPy and SciPy; pinned only |
| `discrete_time_certificate.json`, `checks.log` | the recorded results of that execution |
| `graph_proposal.json` | the session's staged dependency nodes; not applied |
| `source_manifest.json`, `environment.json`, `requirements.txt`, `PACKAGE_README.md`, `PACKAGE_SHA256SUMS` | provenance |
| `SHA256SUMS` | the pin of this directory |
