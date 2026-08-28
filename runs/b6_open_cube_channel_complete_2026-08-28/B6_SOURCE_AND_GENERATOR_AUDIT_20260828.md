# Public-source audit for the channel-complete open cube

Date: 2026-08-28

## Bottom line

No public `B6_dim(3)` coefficient artifact exists in the inspected `ymcirc`
branches. The tempting `B6_dim(3_2)` name means spatial dimension `d=3/2`
(the `[4,2,1]` ladder), not a three-dimensional cube.

The public sources are nevertheless sufficient to generate the missing open
one-cube data directly. The practical target is `[2,2,2]`, full OBC, `B=6`,
with only the six cube plaquettes requested. Generating the 27-signature
universal `[4,4,4]` table is unnecessary and is the wrong first experiment.

## Exact public provenance

- `ymcirc` `develop`: `e9e190bfda405608de9cab71c0df0161cfcb1a10`.
  It contains the `B=6` and `B=7` `d=3/2` PBC tables and the `B=4`, `d=3`
  PBC table, but no path matching `B6_dim(3)`.
- `ymcirc` OBC feature branch: `feature/OBC-mixed-BC` at
  `ff79c01dbdb8eddf5cde3838442656710a2cc835`. It adds universal OBC data,
  including `B=6` and `B=7` for `d=3/2` and `B=3` for `d=3`, but still no
  `B6_dim(3)` artifact.
- `pyclebsch` generator branch and open PR 15:
  `feature/OBC-and-mixed-BC-ymcirc` at
  `2f632685b81c7ed514c6793665257e17ed04ae51`. The PR is open and unmerged.
- Both GitHub repositories are public but report `license: null`, and neither
  inspected Git tree contains a license file. Public visibility permits
  inspection and reproducibility work; it is not an affirmative software
  redistribution license. Obtain author permission before redistributing their
  code or coefficient tables in a release.

The local source ZIPs match the public branch source at the relevant Git blobs:

- `.scratch/literature/pyclebsch-feature-obc.zip` SHA-256
  `6d16ee0fa055b143d8373efa8d57e4f5a745b362bcab6eb12318a9c09922111b`.
- `.scratch/literature/ymcirc-feature-obc.zip` SHA-256
  `63d65a3030e36d399ca236fc802b786b02e10e44d7eaffe2261d6d4ff7d4bd19`.
- `run/gen_ymcirc_data.py`: Git blob
  `83ddb5b78ea936453efa4d44d702f8ebb6ef3f8f`, SHA-256
  `3bec41db86cc571408288bd832cb4a9816398fdc8b0be8eeaed73e27fec620b1`.
- `pyclebsch/matrix_elements/lattice_data.py`: Git blob
  `d83378a02efdf4ca0f1795148accb00d16b4c009`, SHA-256
  `0eebd22d10d7bdead992f625c49879f6bcbf148e4859645dfe4c2b13b6d5a41b`.
- `pyclebsch/matrix_elements/plaquette_matrix_elements.py`: Git blob
  `f048f4a8acbf33ecd8621452102eac94be00b5a4`, SHA-256
  `3d35eb1614bd6bf36432f6345bc16d45a51a6c68ab387a33dbfd47c77c045c45`.
- `pyclebsch/cgc.py`: Git blob
  `b7038ae80d9098cd1700b57119ae2d0f2a0f5b7c`, SHA-256
  `79192a2bfc0fae06269c93214f004fee16ee71ea4c6443db17a0a485507f7953`.

## Exact B6 and B7 ladder artifacts

All paths below are rooted at
`.scratch/literature/ymcirc-feature-obc/ymcirc-feature-OBC-mixed-BC/`.

| Artifact | Bytes | SHA-256 | Git blob on OBC branch |
|---|---:|---|---|
| `ymcirc/_ymcirc_data/magnetic-hamiltonian-box-term-matrix-elements/B6_dim(3_2)_magnetic_hamiltonian.json.gz` | 11,017 | `d72c876489193b89429b190426493e53219e79b58e2fe51b91ba5dd7f6e32f0e` | `9c62ce708ed15da937ef2cd792b6c0cd325637df` |
| `ymcirc/_ymcirc_data/magnetic-hamiltonian-box-term-matrix-elements/B6_dim(3_2)_PBC_magnetic_hamiltonian.json.gz` | 10,247 | `36f8c0992fb4e42b475878eb617034bba0511e45d725491ed8d9577c586f449f` | `34f445613943d6ab22db38b66a3446777256e054` |
| `ymcirc/_ymcirc_data/plaquette-states/B6_dim(3_2)_plaquette_states.json.gz` | 5,578 | `2f8bb2bbe0bf8bfb0b0883f166507cdf6ec2366eece2295becc0694e72fa06a9` | `66eebcfe89488336235193663b36e750f8c6152c` |
| `ymcirc/_ymcirc_data/plaquette-states/B6_dim(3_2)_PBC_plaquette_states.json.gz` | 5,160 | `e18a579b0ec5c28eeba1aff82f85a53277637793bb63ec9f2f25857e713ca7d2` | `ea50ca270e280fa12053dfaf09cd735b22c7aef3` |
| `ymcirc/_ymcirc_data/magnetic-hamiltonian-box-term-matrix-elements/B7_dim(3_2)_magnetic_hamiltonian.json.gz` | 15,625 | `bc1e16b88cbf6c53b2738c85f9c513e91ad0cc7b7a764541e4a17e2ef5f7208d` | `c2ef139939c3b1303183d22ba7dc58574a03768e` |
| `ymcirc/_ymcirc_data/magnetic-hamiltonian-box-term-matrix-elements/B7_dim(3_2)_PBC_magnetic_hamiltonian.json.gz` | 14,566 | `00c65c7714085b9373b10f13f359c4c34741b1e37624b0d178b74d1e84fe9644` | `4e4ea0bc7a19ed030e26e8c7361897d2e9349120` |
| `ymcirc/_ymcirc_data/plaquette-states/B7_dim(3_2)_plaquette_states.json.gz` | 7,197 | `331f707c479ecf4ed078773cced6830dd79b023189171ec42460718dc6fd507b` | `ab76bc7c78055a1b683218d48045c367b6295d0d` |
| `ymcirc/_ymcirc_data/plaquette-states/B7_dim(3_2)_PBC_plaquette_states.json.gz` | 6,624 | `9c34e16761b7250a1aa646bf321ee7e3592cbf7482c92d87a73b944867a559b8` | `ca7896e624f2b592e0fcba4b138e55277def0905` |

`B=6` and `B=7` use the same six representation labels
`1, 3, bar(3), 6, 8, bar(6)`, but they are not interchangeable truncations:
the larger cutoff admits additional gauge-invariant local configurations.

## Measured size anchors

The existing `B=6`, `d=3/2` OBC table separates into two end signatures and
one all-trivalent signature:

- directed local entries: `34 + 1000 + 34 = 1068`;
- all-trivalent signature: 836 physical local states;
- all-trivalent nonzero directed transitions: 1,000;
- 486 distinct initial states participate, with mean outgoing degree 2.058 and
  maximum outgoing degree 7.

For comparison:

- universal `B=3`, `d=3` OBC data contains 190,870 local plaquette states and
  5,506 matrix-element keys (1,502,330-byte and 64,912-byte gzip files);
- `B=4`, `d=3` PBC data contains 731,987 local plaquette states and 40,275
  matrix-element keys (6,428,643-byte and 465,787-byte gzip files).

This is why a universal `B=6`, `[4,4,4]` generation should not be the first
attempt. A direct one-cube table should need six trivalent face signatures,
each of the same approximately 1,000-transition class. Its magnetic table is
therefore expected to remain in the low-thousands of logical entries and the
rough 10--100 KB compressed range, rather than requiring a universal high-
valence corpus. This is a size estimate from measured neighboring artifacts,
not a completed generation benchmark.

No trustworthy wall-clock record for the `B=6` generator is present in the
public branch, PR, metadata, or local notes. The expensive and unbenchmarked
part is uncached CGC/site-factor generation. A one-face smoke run must be timed
before promising minutes or hours. Basis construction and sparse embedding are
not the bottleneck at the physical dimensions below.

## Exact open-cube state-space result

For `[2,2,2]` OBC at `B=6`:

- 8 vertices, 12 links, 6 plaquettes;
- six link irreps: `1, 3, bar(3), 6, 8, bar(6)`;
- 24 allowed ordered trivalent singlet triples, all multiplicity one;
- exact gauge-invariant physical dimension: **3,864**.

Do not adapt the old `B=4` basis loop literally: scanning `6^12 =
2,176,782,336` link assignments is unnecessary. The cube is bipartite. Choose
the four vertices of one parity; their 24 allowed triples assign every edge
once, so only `24^4 = 331,776` candidates are formed. Testing the four opposite
vertices leaves exactly 3,864 basis states.

A dense float64 matrix at this dimension is about 119 MB, but the operator is
sparse. The measured local degree suggests a global directed box operator in
the tens-of-thousands-nnz regime, comfortably handled by SciPy sparse storage
and eigensolvers.

## Recommended execution route

1. Pin the `pyclebsch` PR-15 source commit and record the no-license caveat.
2. Add a dedicated generator case for `[2,2,2]`, OBC, `B=6`, requesting only
   the six actual cube plaquettes. Do not generate the `[4,4,4]` universal file.
3. Time one face first with a fresh, manifest-hashed CGC cache; then exploit
   cached CGCs for the remaining five faces.
4. Build the 3,864-state basis with the bipartite `24^4` join.
5. Embed the six directed face operators sparsely and verify Hermiticity after
   adding adjoints, Gauss closure, charge commutation, and cubic covariance.
6. Project the charge-odd six-face shell and compare its second-order operator
   with the predicted channel-complete coefficient `+5/612`.
7. Use `B=7` only as an adjacent-truncation robustness check, not as a proxy for
   the `B=6` theorem.

## Remaining blockers

- The `B=6`, `d=3` cube coefficients have not been generated or published.
- The required OBC generator branch is public but unmerged and unlicensed.
- A cold one-face CGC runtime has not been measured.
- Charge conjugation in the six-irrep basis may carry nontrivial basis phases;
  it must be solved from the generated Hamiltonian/intertwiner conventions,
  not assumed to be a bare label permutation.
- The `B=4` brute-force basis enumerator must be replaced before a `B=6` run.
