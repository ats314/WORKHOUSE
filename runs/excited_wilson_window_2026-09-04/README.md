# From a source-visible window to operator-level isolation — 2026-09-04

Fifth package from the parallel GPT session, prepared against `d2f46c5` and
reviewed here before integration. It takes the blocked Wilson transfer of
`runs/discrete_time_wilson_2026-09-04` and asks what an operator-level
isolation of the plaquette window would take, keeping the actual positive
transfer throughout.

## What it establishes, and how far

- **The spectrally optimal block (exact).** With the odd shell at `4γ` and the
  rest of the odd spectrum at or above `5γ`, a block of duration `s` guarantees
  the separation `x⁴(1−x)`, `x = e^{−γs}`, maximal at `x = 4/5` with value
  `256/3125`; rounding to whole steps of at most `s_sp/4` keeps `1024/15625`.
  For SU(3), `s_sp = (3/2) log(5/4)`.
- **A cutoff-free finite-volume theorem (analytic).** At each fixed volume the
  actual, untruncated Wilson transfer has an isolated complete plaquette shell
  and an invertible literal-source frame (Gram `≥ 9/16`) on an explicit,
  mesh-uniform coupling interval. The interval shrinks with volume, as
  `P^{−3/2}` in the source bound; not a thermodynamic statement.
- **A volume-uniform first derivative (analytic).** The raw derivative of the
  normalized block grows like `√(2P)`; an explicit local vacuum rotation removes
  that growth, and the rotated first derivative is bounded in full operator norm
  by `16J(s + 2d_τ(E_s))`, the 16 being four links per plaquette times four
  plaquettes per link at `x = 4/5`. A first-order chart only; the package's own
  product-system control shows a first-order rotation is not an all-orders one.
- **Two abstract criteria (analytic, conditional).** An all-orders theorem turns
  a norm `η ≤ 1/400` on locally vacuum-annihilating operator activities into a
  full-Hilbert-space bound `≤ 1/158` and hence isolation; a source-span versus
  complement criterion (`A ≥ a`, `QDQ ≤ b < a`) gives isolation and
  completeness by a Schur complement. Neither hypothesis is established for the
  dressed Wilson operator; the package says so.
- **Exact source-moment identities.** `R*R = G^{−1/2}(C₂ − C₁G^{−1}C₁)G^{−1/2}`
  and `G^{−1/2}(C₂ − 2cC₁ + c²G)G^{−1/2} = (A − c)² + R*R`, separating motion
  inside the source span from leakage out of it; a dark state orthogonal to
  the sources leaves the moments unchanged while enlarging the window. The
  suite "the blocked Wilson transfer: spectral block, cluster margin, source
  moments" checks the block arithmetic and these identities exactly.
- **Open, by its own account.** The all-orders Wilson activity bound, the
  thermodynamic complete band, spatially weighted sharp-shell matching, any
  continuum statement.

## Files

Pinned as received, checksums in `PACKAGE_SHA256SUMS` (three entries there refer
to files moved or renamed: the two notes now live in `paper/research_notes/` as
`G18_EXCITED_WINDOW_OPERATOR_BRIDGE_20260904.md` and
`G18_WILSON_EXCITED_OPERATOR_INSERT_20260904.tex`, and the package's README is
`PACKAGE_README.md`). `prior/` holds the package's own copies of its inputs.

| File | What it is |
|---|---|
| `verify_excited_window.py` (with `prior/wilson_clock.py`) | 33 checks: exact block arithmetic, the derivative cancellation, the factor-16 bound, an exact all-orders sum over 198 disjoint families in a six-site model, source-moment and Schur identities, the dark-state and product-system controls, a one-plaquette SU(3) truncation; need NumPy and SciPy; pinned only |
| `excited_window_certificate.json`, `checks.log` | the recorded results of that execution |
| `graph_proposal.json` | the immutable staged proposal; its scoped results now map to G18/G19 and their operator-chart routes |
| `source_manifest.json`, `environment.json`, `requirements.txt`, `PACKAGE_README.md`, `PACKAGE_SHA256SUMS` | provenance |
| `SHA256SUMS` | the pin of this directory |

## ZIP provenance and native graph integration

The input `workhouse_excited_window_operator_bridge.zip` has SHA-256
`3fc9447a6120b93e45114da8f7b04cf150ea71ae20b8730265dce9ffaff70d14`. On 2026-09-05 every one of its 14 file members was compared byte for byte with the preserved
repository destination. `import_manifest.json` records the complete mapping,
sizes and hashes, including the relocated paper notes and the unchanged
package README/checksum file. The original ZIP remains an external input;
the repository retains every file member rather than depending on that local path.

`RUN:excited_wilson_window_2026-09-04` is registered as evidence on both G18 and G19.
The proposal's analytic claims and remaining targets are integrated into
`ledger/gaps.yaml`; its original JSON remains immutable provenance. The
new routes require an exact Wilson vacuum chart, full operator activities,
and thermodynamic range/source identification. No broad G18/G19 completion
or machine proof of the analytic construction is inferred from this import.
