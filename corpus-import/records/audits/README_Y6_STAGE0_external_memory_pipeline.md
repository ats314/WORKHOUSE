# SU(3) sixth-order rest-mass program — external-memory Stage 0/1

## Scope

This package advances the exact `m6` calculation from algebraic preflight to an executable six-insertion geometry and channel pipeline. It does **not** claim a value for `m6` yet.

The pipeline computes:

1. connected six-plaquette insertion supports modulo the rooted cubic stabilizer;
2. output plaquettes whose boundaries lie in the support complex;
3. all 256 orientation-sign assignments satisfying linkwise SU(3) triality;
4. canonical ordered six-insertion transition words;
5. exact local SU(3) fusion channels and the five intermediate energy denominators needed by the sixth-order folded/des-Cloizeaux formula.

## Why the architecture changed

The certified fifth-order corpus has 6,676,658 connected supports. A 16-window stratified sixth-order probe found an average of `116.9295875` raw child proposals per fifth-order support, corresponding to about `7.80699e8` raw proposals before global deduplication. The sixth-order census must therefore use sorted shards and k-way merge.

## Validation already completed

The new code independently reproduces the complete known Stage-0 results:

| order | connected supports | candidate pairs | canonical survivors | canonical ordered words |
|---:|---:|---:|---:|---:|
| 4 | 182,440 | 895,524 | 449 | 4,221 |
| 5 | 6,676,658 | 39,368,491 | 1,280 | 29,366 |

For fifth order, the first 20 Stage-1 records are structurally identical to the certified `y5_channel_denominator_manifest.json.gz`.

The stratified sixth-order sample contained 6,991,112 globally deduplicated supports, 48,309,953 candidate support/output pairs, 811 triality survivors, and 105,001 canonical ordered words. These are **sample statistics**, not complete sixth-order counts.

## Hardware

Stage 0 is a CPU exact-combinatorics job. An A100 does not accelerate the current integer canonicalization, sorting, or triality operations. Use many CPU cores and fast local SSD storage.

Recommended starting parameters:

```bash
export JOBS=32
export EXPAND_CHUNK=50000
export SCAN_CHUNK=250000
./run_y6_stage0_local.sh /content/Y6_RUN
```

The script regenerates the certified fifth-order support seed, produces sorted sixth-order shards, performs a global k-way merge, scans triality in parallel, and constructs ordered words in compiled C++.

## Stage 1

After Stage 0:

```bash
python yN_stage1_channel_denominator.py \
  --input /content/Y6_RUN/final/y6_ordered_transition_words.tsv \
  --output /content/Y6_RUN/final/y6_stage1_000000_001000.json.gz \
  --start 0 --end 1000
```

Shard across the complete word range and merge only after every shard passes. Stage 1 performs exact singlet-path feasibility, charge-conjugation pairing, resonance classification, and five-denominator energy enumeration.

## Next mathematical stage

Once the complete Stage-1 manifest exists:

1. extract only geometry-realized eight-event signatures;
2. build normalized intertwiners for the new `(4,4)`, `(0,6)`, and `(1,7)` sectors;
3. assemble trace-wiring blocks;
4. contract exact local paths with the certified sixth-order folded weights;
5. sum the zero-momentum triplet trace to obtain `m6`.

Do not infer `m6` from the partial census.
