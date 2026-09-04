# The corner cluster from a third implementation, and the historical ledger read by cluster — 2026-09-04

The last untried route on G3, run both ways at once. ADR 0024 records the
decision.

## Result

| quantity | this run | 2026-09-02 run | historical Stage-3I ledger |
|---|---|---|---|
| corner cumulant, C-odd, (0,2) basis | `+2580244782961/398756546697600` | `−…` in the (2,0) traversal | `+2580244782961/398756546697600` |
| corner cumulant, C-even | `−56022878647/4153714028100` | same | same |
| single-contact dressing, C-odd, (0,2) basis | `+385/1997568` ×14 | `−…` ×14 | `+385/1997568` ×14 |
| shared-link fan, C-odd, (0,2) basis | `−135671797/105250609440` ×2 | `+…` ×2 | `−135671797/105250609440` ×2 |
| adjacent-face cube completion, C-odd, (0,2) basis | `−53/768` | `−53/768` (raw W entry) | **`−31/1536`** (8 of 24 orderings) |
| rotation element `ρ`, kernel basis | `−588708011765248393/14501180577204921600` | `+…` (conjugate basis) | `+238714892212171339/29002361154409843200` |
| `ρ_historical − ρ_assembled` | `25/512` exactly | | |
| `C_shp` assembled, kernel basis | `−13035490122347/550663802582400 = −0.0236723` | `−0.0642696` (conjugate basis) | `−0.0480864` |

Every cluster of the rotation record agrees between the historical pipeline's
own ledger, the 2026-09-02 assembly and this third engine, except the
adjacent-face cube completion, where the historical ledger holds 8 of the 24
insertion orderings with the right weight each (`2, 1, 4, 2, 8, 8, 2, 4` in
units of `1/1536`) and lacks the 16 that sum to `−25/512`. In the kernel's own
basis the assembled off-axis coefficient is `C_SHP_HISTORICAL + 25/1024`.

## What was run

`corner_from_scratch.py`, about four minutes on one CPU:

1. `workhouse.loopcalc`, the third engine — no engine primitive, no kernel,
   no run record read: the second-order constants; `u` on three chain types
   with the incidence signs; all 58 three-cluster cumulants of the coplanar,
   stacked and perpendicular pairs in the kernel's (0,2) basis, plus a
   plaquette five sites away (zero); the cube completion between opposite
   faces and between adjacent faces in both traversals.
2. `workhouse.cellular.c_full`: the cube completion with multi-loop
   intermediates, symbolic in `N`.
3. `workhouse.stage3i`: the pinned Stage-3I fixture decoded and hash-checked,
   reassembled by Stage 3J's rule into the pinned 189 records, and regrouped
   by support set for the rotation record in both sectors.
4. The rotation element in the kernel's basis from this run's dressings, the
   2026-09-02 pair cluster (the one piece not recomputed here, which the
   historical ledger also holds to the digit), and the cube term; then
   `C_shp = −5/96 − u − (ρ + π)/2`.

## Files

| File | What it is |
|---|---|
| `corner_from_scratch.py` | the run |
| `console.log` | its complete output |
| `certificate.json` | every number above, with the per-X dressings of all three pairs; the checks in the third-implementation suite read this |
| `SHA256SUMS` | the pin |
