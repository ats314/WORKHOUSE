# The off-axis channels, taken in the ledger's order — 2026-08-30

The off-axis route's step 2 is the in-plane nearest-neighbour transfer and its
step 3 is the orbital rotation. Both were attempted here. **The order is
wrong**: step 2 is not reachable in this channel at all, step 3 is, and step 3
does not settle the sign it was expected to.

## Step 2 is order eight, not four

`c_prim` completes a **closed** cell — every edge in exactly two faces with
opposite orientations — and its order is `r = faces - 2`. So a fourth-order
completion needs a closed cell of exactly six unit squares.

`boxes.py` builds lattice boxes tiled by unit squares and lets `cellular.Cell`
validate them:

| cell | unit faces | r | coplanar edge-sharing pairs |
|---|---|---|---|
| unit cube | 6 | **4** | **0** |
| 1x2x1 box | 10 | **8** | 4 |
| 1x1x2 box | 10 | 8 | 4 |

The only closed six-unit-square cell on the cubic lattice is the unit cube, and
it has no coplanar face pair. The smallest closed cell that carries one is the
1x2x1 box, at `r = 8`. **The in-plane nearest-neighbour transfer is order eight
in the primitive channel**, so the fourth-order in-plane record has to come
from the folded/linked or adjoint terms `cellular`'s own scope note excludes —
not from extending that module.

## Step 3 is reachable, and is a new coefficient

A unit cube offers exactly two fourth-order primitive completions:

| sector | ordered pairs | histories | `S_4` | `c_4(N)` | at `N = 3` |
|---|---|---|---|---|---|
| opposite (normal hop) | 6 | 24 | `-20` | `-160/(N(N^2-1)^3)` | `-5/48` |
| **perpendicular** | **24** | **14** | **`-11`** | **`-88/(N(N^2-1)^3)`** | **`-11/192`** |

Uniform over all 24 ordered perpendicular pairs, ratio exactly `11/20` to the
normal channel at every rank. The corpus does not record this coefficient.

## But it does not settle the ±f/2 sign

`rot2.py` builds both channels' Bloch matrices in the same convention, from the
repository's own cube boundary `d_3` (whose six faces carry signs
`-1, +1, +1, -1, -1, +1`), and fits the four-shape basis.

The **normal** sector lands in the span, and the fit is the control that
validates the construction:

```
A = -160/(N(N^2-1)^3) = -alpha_N/4      C = +80/(N(N^2-1)^3) = -A/2      B = D = 0
```

Note the sign. The self-test committed earlier asserted `A = +alpha_N/4`; with
the repository's own boundary signs it is **negative**. What survives the
convention is `|A| = alpha_N/4` and the ratio `C/A = -1/2`. The corpus fixes the
overall sign itself, by taking `|c_4|`. That check has been corrected to assert
only the magnitude and the ratio.

The **perpendicular** sector does not land in the span. `rot4.py` reports:

- cubic permutation invariant: **True** (so the construction is sound)
- in the four-shape span: **False**
- displacement range per axis: ±2 — **but see the correction below**

### Correction: it is range-1, and it is a different channel

The ±2 line was first read as "the channel is range-2". That is wrong, and
`shells.py` shows why: ±2 is a property of the carrier projection
`psi^dag H psi`, which inherits psi's own displacement content, since each
`d_j = e^{ik_j} - 1` spans displacements 0 and 1. The **operator** has
`max |displacement| = 1`.

| channel | records | shells | max &#124;δ&#124; |
|---|---|---|---|
| normal (opposite) | 6 | (0,0,1)×6 | 1 |
| perpendicular | 24 | (0,0,0)×6, (0,0,1)×12, (0,1,1)×6 | 1 |

The real reason the recorded rotation row does not apply is **structural**:
this channel's Bloch entry is `H_[(12),(13)] = -conj(d_2) d_3`, while the
recorded row is `+conj(d_n) d_m`. Those are *minus the conjugate* of one
another — different off-diagonal structures — so `C = -f/2` is a statement
about the other one, and the span failure follows from that rather than from
range.

The census points the same way. The perpendicular channel's 24 records spread
across **three** shells, so they sit in no single recorded block: `MIXED
(0,1,1)` is also 24 records, but all in one shell. The control that makes the
census trustworthy is the normal channel — its 6 records at shell (0,0,1)
match the recorded `NORMAL (0,0,1)` block of 6 **exactly**.

So the answer to "this channel plus something else, or a different channel
entirely" is **a different channel**. What stays open is narrower: which
channel the recorded `ROTATION` block (120 records, contributing `-0.004080`
of C) actually is.

## Scope

Nothing is adjudicated and no disputed value moves. One caveat on `rot4.py`'s
axis-parity line, recorded rather than dropped: it tests `k_j -> -k_j` without
transforming the face basis, and under a reflection the faces containing that
axis also flip orientation. So that line is **not** evidence either way and no
conclusion here rests on it. The span and range results do not depend on it.

| File | What it is |
|---|---|
| `boxes.py` | closed lattice boxes tiled by unit squares; the r = 4 vs r = 8 count |
| `rot2.py` | both channels' Bloch matrices and the four-shape fit |
| `rot3.py` | the perpendicular numerator, and its Hermiticity |
| `rot4.py` | invariance, displacement range, and the span test |
