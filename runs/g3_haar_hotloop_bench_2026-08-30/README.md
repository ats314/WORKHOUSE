# The G3 performance wall, measured — 2026-08-30

G3's live step is one cross-plane amplitude, and its register entry says the
blocker is engineering:

> What unblocks it: an upstream engine revision replacing the pure-Python
> union-find/canon hot loop in the exact Haar contraction with a compiled core
> (C or flint) — the measured 50%+ self-time there implies 10-100x, which
> turns the 30-cluster assembly into hours. Engineering, not physics.

The first half is right. **The 10-100x is not**, and this directory records
why, because a register that carries a wrong multiplier plans the next session
into the wrong work.

## The wall, reproduced

One exact Haar inner product on a degree-3 balanced state (four links at
degree 3, partition size 48) through the pinned engine
`corpus-import/.../DATA_SU3_Exact_MarkedCluster_m4_Colab.py`:

| what | time |
|---|---|
| `haar_inner`, unmodified | **13.3 s** |

`prof.py` gives the profile, and it confirms the register's reading:

| function | tottime | cumtime | share |
|---|---|---|---|
| `merge_classes` | 8.5 s | **44.8 s** | **81%** |
| ` └ find` (47.5M calls) | 11.9 s | | |
| ` └ union` (15.3M calls) | 9.2 s | | |
| `canon` | 7.9 s | 20.5 s | |
| `Fraction` arithmetic | | ~6 s | 11% |

(cumulative on a 55.4 s profiled run; profiling roughly 4x's the wall clock.)

## What a compiled core actually buys

`haarcore.c` is a CPython extension doing exactly what `merge_classes` does —
parent array, union by first label occurrence, union the Weingarten pairs,
canonical relabel — with no Python object churn. It agrees with the pinned
implementation on **60,000 random partitions, bit-identical, zero mismatches**,
and on every real inner product below.

```
gcc -O3 -shared -fPIC -I/usr/include/python3.11 haarcore.c -o _haarcore.so
```

| case | partition | baseline | +C core | +C +flint | total |
|---|---|---|---|---|---|
| deg2, 4 links | 32 | 0.007 s | 0.003 s | 0.002 s | 4.4x |
| deg2, 2 links | 48 | 0.004 s | 0.002 s | 0.001 s | 3.0x |
| **deg3, 4 links** | **48** | **12.9 s** | **3.37 s** | **1.66 s** | **7.8x** |

Every value bit-identical to the pinned engine's own answer.

## The correction

**The compiled core gives 3.9x, not 10-100x.** Amdahl caps it: `merge_classes`
was 81% of cumulative time, so removing it entirely cannot exceed
`1/0.19 ≈ 5.3x`, and the measured 3.9x is close to that ceiling. The register
read "50%+ self-time" as if eliminating it were worth 10-100x overall; it is
worth at most ~5x.

After the swap the profile *moves*, and `prof2.py` shows where:

| function | share, C core active |
|---|---|
| `fractions.Fraction` arithmetic | **56%** |
| `contract_link_partition` own overhead | 13% |
| `_haarcore.merge_classes` | **5.6%** |

So the second wall is exact rational arithmetic. `flint.fmpq` — already a
dependency of this repository — is **7.7x** faster than `fractions.Fraction`
on the relevant add/multiply mix and gives identical exact values, which takes
the degree-3 case from 3.37 s to 1.66 s.

Combined: **7.8x measured, values exact.** Not the register's 10-100x, and not
obviously enough: the register's own measurement was that a single 2-face
half-history ran 1h51m *still inside its first Haar Gram*, so 7.8x turns that
Gram into roughly 14 minutes and leaves the 30-cluster assembly plausibly days
rather than hours.

## What would go further, and what would not

The remaining 13% is `contract_link_partition`'s Python overhead — the
`(sigma, tau)` double loop, and a `MappingProxyType` provenance dict built
with `repr(left)`/`repr(right)` on **every** call and read only on error.
Moving that whole loop into the compiled core would amortise the partition
read over all 36 merges and drop 35 redundant label-union passes; that is the
next honest increment, and it is bounded.

What this does *not* need: the `flint` swap is not a drop-in. The engine
builds its Weingarten inverse-Gram in `Fraction` at import time, so changing
the arithmetic type means converting those tables too (`stack.py` does this
for the benchmark). That is the point at which a hot-loop swap stops being a
drop-in and becomes the "upstream engine revision" the register names — which
is correct, but larger than the union-find loop it identifies.

## Scope

Nothing here is committed into the pinned engine: `corpus-import/` is
evidence. The C core is an independent reimplementation of one function,
verified against the original, and the benchmarks monkey-patch the module in
memory only. No coefficient, tolerance or claim moves.

`dict2.py` is separate: it verifies the range-1 operator-structure dictionary
that the cheaper off-axis route rests on. Three of its four rows are exact;
the orbital-rotation sign is convention-dependent. That is now a registered
check — see `each range-1 operator structure has a fixed shape coefficient,
and the rotation sign is a convention`.

| File | What it is |
|---|---|
| `haarcore.c` | the compiled `merge_classes`, verified bit-exact on 60k random partitions |
| `prof.py`, `prof2.py` | the profile before and after the swap |
| `bench2.py` | the wall, by Haar degree |
| `stack.py` | the combined C + flint measurement, against the engine's own values |
| `dict2.py` | the range-1 shape dictionary, in exact band variables |
