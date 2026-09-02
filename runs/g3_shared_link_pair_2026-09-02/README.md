# The shared-link amplitudes assembled from clusters — 2026-09-02

The G3 route "independent cross-amplitude computation", run. The two
fourth-order amplitudes the whole of C2 reduces to (ADR 0019: `C_shp = −5/96
− (ρ + π̃)/2`) live on pairs of plaquettes that share a link. This run
assembles the lattice fourth-order matrix element for three pairs by cluster
expansion, reading neither kernel: the coplanar pair (the in-plane orbit `π`),
the stacked pair (the normal orbit `ν`, which both kernels agree on and which
validates the method), and the perpendicular pair (the rotation orbit `ρ`).
ADR 0021 records the decision.

## Result

| element | record | assembled | |
|---|---|---|---|
| (0,1)→(0,1) at (1,0,0), in-plane `π` | `−20535103905179/1264270320593280` | `−20535103905179/1264270320593280` | **exact** |
| (0,1)→(0,1) at (0,0,1), normal `ν` | `−1050558388351/10081900483200` | `−1050558388351/10081900483200` | **exact** |
| (0,1)→(0,2) at (0,0,0), rotation `ρ` | `238714892212171339/29002361154409843200` = +0.0082309 | `588708011765248393/14501180577204921600` = +0.0405972 | **neither kernel's** |

The v10a.26 dump carries the opposite sign for `π` and `−0.0879716` for `ρ`.
So the cold pipeline is wrong on `u`, `π` and `ρ`; the historical kernel is
right on `u`, `π`, `ν` and wrong on `ρ`; and `C_shp = −5/96 − u − (ρ + π)/2`
with the assembled `ρ` is `−54822624038066723/853010622188524800 = −0.0642696`,
a third value, recorded as C2's third side and not promoted (see "What ρ rests on").

## How an element is assembled

A history of four insertions with net charge `P Q̄` is one of two kinds: `P`
and `Q̄` with one `X X̄` pair besides, or — when `P` and `Q` are two faces of one
cube — the cube's other four faces, each once, because a cube's six faces
have zero net triality. So

    H4_PQ = W(P,Q) + Σ_X [ W(P,Q,X) − W(P,Q) ] + Σ_cubes D_cube,

`X` over every plaquette sharing a link with `P` or `Q`, and `D_cube` the direct
term over the cube-completion histories on the six-face cluster, which no fold
or `A`-term reaches. That the sum stops there is checked: for an `X` five sites
away the cumulant is exactly zero on every orientation element (`gate` stage).

- **The pair cluster** is the engine's own full assembly
  `H4 = D − A C1 − C1ᵀ A − ½(K2 N + N K2) + A A J`, `A = PVP` the SU(3)
  baryonic vertex, baryonic histories `{Q, Q, P̄, P̄}` included. Two 4-cycles
  sharing one edge, traversed oppositely, is one abstract cluster, so the
  coplanar and perpendicular pairs have the same pair cluster and differ only
  through their dressings and the cube.
- **The dressings** need only `X`-touched histories, in which the `A`-terms and
  `J` cancel. Three classes occur: single-contact plaquettes at
  `−385/1997568`; plaquettes on the shared link at `135671797/105250609440`;
  and, for the perpendicular pair only, the two corner faces (three faces at
  a cube vertex, pairwise sharing a link) at `−2580244782961/398756546697600`.
  For the stacked pair the single-contact dressings are 0 and the four side
  faces are two-hop chains at `−u`.
- **The cube term** is `−5/48` for opposite faces — the primitive cube
  completion `ν̃`, computed — and `53/768` for adjacent faces.

Cluster machinery: `runs/g3_chain_amplitude_replication_2026-09-02/chain_amplitude.py`
(imported by path). Haar integrals: `workhouse.haar_epsilon`.

## What ρ rests on

Every component is validated on a record both kernels agree on or by a second
implementation: the pair cluster and both ordinary dressing classes on `π`
(exact); the cube term and the side chains on `ν` (exact); the corner cluster
by `workhouse.chain_cluster` — a block characteristic-polynomial resolvent,
the `PVP = 0` form, the engine's own Haar integrals — which returns the
identical rational in eleven seconds. What does not exist is a record both
kernels got right that contains a corner cluster, because only a
perpendicular shared-link pair has one. The assembled `ρ` is therefore
validated piecewise and not as a whole, and that is the difference between
recording it as C2's third side and promoting it.

## What made it tractable

The pinned engine's Haar contraction expands every ε-pair into its 3!
permutation deltas and carries set partitions. On the pair's baryonic words
that is six determinant links at ×6 each with nothing merging, then a pure-six
link at ×456: one integral took 264–398 s and gigabytes, and one element has
3,744 of them. `workhouse.haar_epsilon` evaluates the same integrals with the
ε's kept as ε's at 0.02 s each, agreeing with the engine exactly on every
family it can price and on two pure-six references
(`tests/test_haar_epsilon.py`).

## The ε-sector, and U5

`EPS_BLIND=1` runs the same assembly with every unbalanced-family integral
dropped — the "direct balanced contraction" U5 makes a prediction for (it also
sets `PVP = 0`). The dressings do not change; each pair cluster's C-odd element
moves by exactly `−55/13872`. So the ε-sector of `ρ + π̃` is `−55/6936`, against
U5's `−25/512`: its own falsifier has fired.

## A convention the records fix

The corpus orients its plane basis as (0,1), (1,2), (2,0). A (0,2) plaquette
traversed x-then-z is the conjugate of the record's plane and flips the sign of
every C-odd element (the replication run's zigzag chain shows it). The
perpendicular pair here is built with the (2,0) traversal, so its element
compares to `ρ` directly; both shared-link pairs have incidence `−1`, as
THM_FLUX Prop. 2's `S_□` has it.

## Files

| File | What it is |
|---|---|
| `shared_link_pair.py` | the run: `python shared_link_pair.py {normal,coplanar,perpendicular} {gate,dressing,cube,pair,all}`; `EPS_BLIND=1` for the balanced contraction |
| `assemble.py` | sums the stage outputs, compares with the records, writes the certificate |
| `console_*.log` | complete output of every stage as run here |
| `pair_route_*.json` | every cumulant, per stage and pair |
| `shared_link_pair_certificate.json` | the assembled elements and comparisons; the checks in the kernel-orbits suite read this |
| `SHA256SUMS` | the pin |

Reproduction: about three hours per pair on one CPU, dominated by the
three-plaquette dressings at seven minutes each; the cube terms take seconds.
