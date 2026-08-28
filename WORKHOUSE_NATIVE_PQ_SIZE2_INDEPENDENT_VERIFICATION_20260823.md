# Independent verification of the native physical-P/Q size-two certificate

**Date:** 2026-08-23  
**Verdict:** **PASS, within a narrower and explicit scope**  
**Implementation under test:** `WORKHOUSE_NATIVE_PQ_SIZE2_CERTIFICATE_FILES_20260823.zip`  
**Repository/implementation edits:** none

## Bottom line

The native Route A certificate is reproducible and internally coherent. I found no dependency of its support-size-two values on F07, a fitted fourth-order result, an oracle value, a transcript coefficient, the supplied report, the supplied result JSON, or the target-bearing post-hoc validator.

The exact result is:

- one-face direct D: `-13/896`;
- coplanar per-placement size-two root-polarization increment: `-44119723/138858720`;
- orthogonal per-placement size-two root-polarization increment: `-291514199/964076256`;
- signed cubic `4+8` size-two total:
  `-31127086619/8435667240`.

The last fraction was reconstructed independently from all 12 placement records and also by the direct identity

```text
4*(-44119723/138858720) + 8*(-291514199/964076256)
= -31127086619/8435667240.
```

Only after those native values and their source/result hashes were frozen did the verifier open the older F07 crosswalk. F07 agrees exactly on the singleton, both geometry-class per-face values, the size-two total, and singleton-plus-size-two total.

The important scope correction is:

> This directly certifies the canonical `xy` root/input-polarization-2 row, resolved over all three output polarizations, for all 12 rooted placements. It does **not** directly enumerate a full `3 x 3` input/output polarization matrix. The displayed `2 x 2` matrices are root/neighbor **endpoint-space** matrices, not polarization-space matrices.

The other two input rows require an additional cubic-covariance transport argument. The certificate states that limitation correctly in its interpretation section.

## Frozen identities

### Source package

| artifact | SHA-256 |
|---|---|
| supplied ZIP | `a5710adfdc298e598d6c1da8803554e544b343e6b41a4cc96476a9f4c90bbd02` |
| supplied report | `77f8b8acec75d51e1057ec6c1aeaa30cba7988c053f66afb80180a9ca13feece` |
| internal checksum index | `c976c9bc6039e230cb6d81f4e59a5378785ddf42f07c6a501280e02e5cee6912` |
| upstream dependency index | `0bc1257f599d0eb678cec28336ebd8f389581cd2ea136bc74440419221791de0` |

All nine internal checksum entries and all five external dependency entries reconcile.

### Executed implementation

| artifact | SHA-256 |
|---|---|
| native calculator | `bc203ad16a7825f24dcff69fb69f8adf094a7d003639b6c2adce022ea1749014` |
| exact Haar tensor backend | `dc275cf8076fbc56102f1d3d7c21e10d88fcc18d3b78b7ed0d79ab0f9e53b3f4` |
| marked-cluster engine | `be9d77f5b245715ed6e4fe6dc9178a56ddfa5c68efe697eaa7cf4bb6adae27ad` |
| order-schedule guard | `68782826d50ad6bcbb3a20d83649bfa7f66e42c5706d131361b7d189b1f99a8f` |
| supplied validator | `4b054011fe12239cd52715086b5f432e0c15e9d6afcc9a0feec76274120f6d33` |

### Reproduced outputs

Four untouched calculator executions were performed:

1. normal Python;
2. optimized Python (`-O`);
3. normal Python with an empty alternate bytecode-cache path;
4. optimized Python with an empty alternate bytecode-cache path.

Every execution produced the same 99,137 bytes:

`fac8cb8b957f967409243a28aac6c2f0712f096639dc4dfc1843230a50a1881b`

The empty-cache reruns matter because `-B` stops Python from *writing* bytecode but does not, by itself, prove that pre-existing `.pyc` files were ignored. An empty `-X pycache_prefix=...` plus `-B` removed that ambiguity. Neither empty cache directory was created, and the exact sealed result still reproduced.

The supplied validator passed normally and under `-O`. Both validation files are byte-identical:

`334bf6a5b0a936e994246f6490859de10c67bcfcd7a15ffc1b37ac2a3dd2027c`

The independent verifier also passed normally and under `-O`; its two result files are byte-identical:

`cd2fcc1b50917f2538102bf6ddcd0dc4c4377829ef1053fe8c04b2d15ff7debe`

## Target-leakage audit

### Calculator input surface

Static AST inspection found exactly three dynamic module inputs:

- `ENGINE_PATH`;
- `ORDER_GUARD_PATH`;
- `TENSOR_HAAR_PATH`.

The calculator does not import its validator, report, result JSON, F07 program/result, a coefficient ledger, or any directory-discovered file. It has no `json.load`/`json.loads`, generic `open`, glob, environment lookup, eval/exec, pickle, marshal, subprocess, or network input path. Its only `read_bytes` call is the provenance hash helper; the result JSON is write-only.

The calculator's accessed order-guard API is exactly:

- `first_closed_order_with_block`;
- `exact_one_face_w22_sensitivity`;
- constant `Q2`.

It reads only `o4_equal` and `o5_difference` from the sensitivity result.

### Literal and encoded-value scan

No support-size-two numerator, denominator, exact fraction, or decimal prefix occurs in the calculator, tensor backend, marked engine, order guard, or decoded embedded geometry manifest. The scan covered:

- both endpoint-matrix fractions;
- both per-placement increment fractions;
- both root-row fractions;
- the final `4+8` fraction;
- decimal prefixes of all of those values;
- `11.0685`, `M4_ORACLE`, and `local_shift`.

The engine's embedded base85/gzip geometry manifest was decoded independently:

- decoded length: 216,942 bytes;
- SHA-256: `748e72ec7b1cffa42b5c8b9fd73be9be0da29956a8541ee1af577c2407974c94`.

It contains none of `F07`, `oracle`, `local_shift`, `M4_ORACLE`, `transcript`, or any scanned final fraction/decimal fragment.

Two target-adjacent strings deserve explicit disclosure:

1. The marked engine contains `DualColdOracle` once, at source line 310, solely inside a `SOURCE_AUTHORITIES` provenance filename. The native calculator never accesses `SOURCE_AUTHORITIES` or a production/oracle API.
2. The loaded order-guard source contains the independently known analytic singleton `-13/896` once, at line 615, as a regression inside the guard's standalone runner. The native caller never calls that runner and never reads the sensitivity function's `full[4]`; it reads only equality through order four and the nonzero order-five W22 difference. The native one-face D is separately reconstructed from its character `W2` and `R2` tables.

Therefore a claim that *no loaded source text contains any known result* would be too absolute. The scientifically relevant claim survives: neither the support-size-two values nor the native singleton calculation has a data path from those inert strings, F07, or a fitted/oracle target.

The post-hoc validator intentionally contains the expected final fractions. That is not circular because the calculator's load allowlist excludes it and the validator runs only after the result bytes have been written.

## Independent exact reconstruction

### One-face value

Without using the validator's expected constant, the verifier recomputed

```text
(1/2) * sum_rep W2(rep) * R2(rep) = -13/896.
```

The charge-odd and no-singlet flags are true.

### Representative endpoint matrices

For each representative, the verifier ignored the stored matrix initially and grouped the 28 nonzero action-ledger records by `(bra_face, ket_face)`. Exact summation gives:

```text
coplanar:
[[-8554053551/26994135168, -129523931/8435667240],
 [-129523931/8435667240, -8554053551/26994135168]]

orthogonal representative:
[[-8554053551/26994135168,  129523931/8435667240],
 [ 129523931/8435667240, -8554053551/26994135168]]
```

These independently summed matrices exactly match the stored matrices. Grouping the same ledger records by support also exactly reconstructs each reported support sum. Hermiticity is exact, the two diagonals agree, and the two geometry representatives have opposite off-diagonal signs as required by orientation.

Mapping each endpoint to its T1 polarization reconstructs the stored canonical input-polarization-2 rows:

| class | root row `(out 0,out 1,out 2)` | pair increment after singleton subtraction |
|---|---|---|
| coplanar | `(0, 0, -184537657/555434880)` | `(0, 0, -44119723/138858720)` |
| orthogonal representative | `(0, 129523931/8435667240, -8554053551/26994135168)` | `(0, 129523931/8435667240, -291514199/964076256)` |

### Exact quotient and Haar gates

Both representatives independently report and freshly reproduce:

- Krylov ranks `8, 16, 24, 24`;
- physical rank `24`;
- E0 nullity `2`;
- bordered dimension `26`;
- closure depth `3`;
- moments through degree `6`;
- maximum raw two-face closure dimension `24`;
- exact-zero equation and Q-constraint residuals for all eight histories;
- pair and singleton sources retained in one joint physical quotient.

The runtime triality-compatible family census is exactly

`(0,3), (0,6), (1,1), (2,2), (3,0), (3,3), (6,0)`.

No `(2,5)` or `(5,2)` occurrence was contracted. Independent runtime poison calls confirm:

- tensor backend rejects `(2,5)`;
- marked engine rejects `(2,5)` as explicit poison;
- marked engine rejects unsupported zero-triality `(7,1)`.

The calculator's pure-six gate executed on every fresh run and reports the full `729 x 729` integer-tensor comparison, rank `5`, trace `5`, and identity `native_numerator = 72 * tensor_numerator`. A separate backend self-certificate reproduces the supported-family set, denominator `72`, rank `5`, trace `5`, and 488 pure-six permutation terms.

W22 remains structurally forbidden through order four. The first closed order using W22 is five, with nonzero full-minus-pruned witness `-5/7168`.

## Independent 12-placement audit

The verifier independently enumerated every plaquette sharing exactly one link with the canonical `xy` root. It found exactly 12:

- 4 coplanar;
- 8 orthogonal.

For every placement it independently enumerated signed coordinate permutations and translations that preserve the root plaquette and map the representative neighbor to the target. It then recomputed:

- root and neighbor vertex maps;
- permutation determinant;
- ordered-face tangent orientation;
- root and neighbor C-odd signs;
- relative sign;
- complete candidate count and relative-sign inventory;
- the lexicographically selected positive-relative witness when available;
- the transported endpoint matrix;
- the output-polarization row;
- singleton subtraction.

Every stored witness matches. The independent sign census is:

```text
coplanar:  +1 x 4
orthogonal: -1 x 4, +1 x 4
```

The orthogonal off-polarization term therefore changes sign under the appropriate placements; it was not silently scalarized. Summing only the canonical root-polarization increments produces the exact `4+8` result quoted above.

## Post-freeze F07 comparison

The F07 crosswalk was opened only after the native result, source firewall, exact ledger reconstruction, quotient gates, and 12-placement sum were frozen in memory. Its SHA-256 in this comparison was:

`1a80eff56006f53466b6ead184b7885d996cf12b8ae15d65d7ba6991966768be`

Exact matches:

| quantity | native Route A | F07 |
|---|---:|---:|
| singleton | `-13/896` | `-13/896` |
| coplanar per face | `-44119723/138858720` | `-44119723/138858720` |
| orthogonal per face | `-291514199/964076256` | `-291514199/964076256` |
| size-two total | `-31127086619/8435667240` | `-31127086619/8435667240` |
| singleton plus size two | `-499991665799/134970675840` | `-499991665799/134970675840` |

This agreement is substantive because F07 is not an input to the native calculation.

## Validator hardening note

The supplied validator's main entry point pins the complete result SHA-256 before parsing, so added fields, alternate rational spellings, or any other byte change fail closed. Its recursive float rejection also works under normal and optimized Python.

At the inner `validate_document()` layer, the validator does not independently reject every possible extra key or every noncanonical-but-equivalent rational string. This is not an exploit against the sealed workflow because `main()` first requires the exact 99,137-byte result hash. The independent verifier adds exact top-level schema checking, duplicate-key rejection, canonical reduced-rational checking, and decimal/non-finite JSON rejection.

## What this does and does not close

This verification supports the following claim:

> The support-size-one and rooted support-size-two physical-P/Q direct-D calculation has a native, exact, target-independent implementation for the canonical input-polarization-2 row, with full output-channel retention and signed transport across all 12 nearest rooted placements.

It does **not** certify:

- support size three or larger;
- the complete embedded/Möbius `Gamma`;
- fold terms;
- linked-vacuum terms;
- the final fourth-order `m4` coefficient;
- a directly enumerated full `3 x 3` polarization matrix.

No Route B result was imported into this verdict.

## Commands used

All commands were run from the workspace root or the isolated scratch directory, without modifying the frozen implementation.

```powershell
# Untouched native runs, writing only to scratch
& 'work/uv-cache/archive-v0/p5HMSCWIhZMzPNsKrqXNK/Scripts/python.exe' -B `
  'work/native_pq_size2/native_pq_size2_exact.py' --output `
  'work/oracle_native_pq_cleanrun/fresh_native_normal.json'

& 'work/uv-cache/archive-v0/p5HMSCWIhZMzPNsKrqXNK/Scripts/python.exe' -O -B `
  'work/native_pq_size2/native_pq_size2_exact.py' --output `
  'work/oracle_native_pq_cleanrun/fresh_native_optimized.json'

# Source-only runs with an empty alternate bytecode cache
& 'work/uv-cache/archive-v0/p5HMSCWIhZMzPNsKrqXNK/Scripts/python.exe' `
  -X 'pycache_prefix=work/oracle_native_pq_cleanrun/empty_pycache_normal' -B `
  'work/native_pq_size2/native_pq_size2_exact.py' --output `
  'work/oracle_native_pq_cleanrun/fresh_native_normal_nopyc.json'

& 'work/uv-cache/archive-v0/p5HMSCWIhZMzPNsKrqXNK/Scripts/python.exe' -O `
  -X 'pycache_prefix=work/oracle_native_pq_cleanrun/empty_pycache_optimized' -B `
  'work/native_pq_size2/native_pq_size2_exact.py' --output `
  'work/oracle_native_pq_cleanrun/fresh_native_optimized_nopyc.json'

# Supplied validator, normal and optimized
& 'work/uv-cache/archive-v0/p5HMSCWIhZMzPNsKrqXNK/Scripts/python.exe' -B `
  'validate_native_pq_size2.py'
& 'work/uv-cache/archive-v0/p5HMSCWIhZMzPNsKrqXNK/Scripts/python.exe' -O -B `
  'validate_native_pq_size2.py'

# Independent verifier, normal and optimized
& 'work/uv-cache/archive-v0/p5HMSCWIhZMzPNsKrqXNK/Scripts/python.exe' -B `
  'independent_verify_native_pq.py'
& 'work/uv-cache/archive-v0/p5HMSCWIhZMzPNsKrqXNK/Scripts/python.exe' -O -B `
  'independent_verify_native_pq.py'
```
