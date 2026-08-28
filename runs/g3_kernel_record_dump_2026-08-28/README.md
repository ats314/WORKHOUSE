# The v10a.26 kernel records, written down — 2026-08-28

The cold fourth-order kernel's 189 per-record values, which the 15-hour
A100 transcript proves existed and never dumped, reproduced on this
container's CPU in **12.3 minutes** by `scripts/g3_kernel_record_dump.py`:
the pinned v10a.26 script (digest `c123287a…`, ledger/notes.yaml) executed
verbatim up to the rooted-oracle cut, with only `PREFER_GPU` flipped to 0.

Every gate in the executed sections passed, and the reproduced kernel
matches the transcript's printed fingerprints exactly: 189 anchored
records, A = 5/48 (0.10416666666672), B and D at fit noise, and
**C_direct = -0.020213328886166577 — bit-identical to the registered
`C_SHP_NEW_NUM`**. The 15-hour wall was the scalar-oracle leg; the
C-bearing kernel leg was never the expensive half.

## The structural comparison

`block_comparison.txt` (from `scripts/g3_block_comparison.py`) runs both
189-record kernels — this dump and the pinned historical certificate —
through one standalone reimplementation of the transcript's own 4-point
Bloch shape fit. The extractor validates on both sides: it returns each
kernel's registered C exactly (historical -0.048086383181, cold
-0.020213328886) and A = 5/48 for both.

What it establishes, with neither side promoted:

- **Identical support**: the same 189 (displacement, plane-pair) records.
- **One scale factor `s = 4.132743700859206` explains 144 of 189 records
  to a spread of 2.2e-12** — the entire rotation-type bulk (63% of the
  kernel) has identical relative structure in both kernels.
- **The divergence is three amplitudes**: the cross-plane amplitude (one
  value per kernel, 24 records, opposite sign: historical ±0.0082308779
  vs cold ∓0.0879773614), the nearest-neighbour same-plane amplitudes
  (NORMAL + IN-PLANE, 18 records), and the on-site scalar (the known
  q_band vs m_Gamma anchor difference — its swap moves C by exactly 0).
- **The ΔC attribution is linear and exact**: swapping the divergent
  classes one at a time into the rescaled historical kernel produces
  class contributions summing to +0.178515368304 = the actual difference
  C_cold − s·C_hist, with the nn same-plane block the largest single
  contributor (+0.117518633316).

This is the localization G3's rewrite asked step 2 for: the two rival
kernels do not disagree diffusely — they disagree in exactly the
A-carrying sector the registered A-pins-the-normal-block result predicted,
and agree, relative structure identical to twelve digits, everywhere else.

## Files

| File | What it is |
|---|---|
| `g3_kernel_records.json` | the 189 cold records: displacement, plane pair, value; plus source digest, cut marker, shape fingerprint |
| `kernel_dump.log` | full console transcript of the CPU rerun, every gate |
| `block_comparison.txt` | the record-by-record comparison and ΔC attribution |
