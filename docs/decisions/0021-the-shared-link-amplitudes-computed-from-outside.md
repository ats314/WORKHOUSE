# 21. The shared-link amplitudes are computed from outside both pipelines

Date: 2026-09-02. Status: accepted. Closes the G3 route "independent cross-amplitude computation"; refutes U5; gives C2 a third side; bears on G14. Promotes nothing.

## Context

ADR 0019 reduced C2 to two numbers, `C_shp = −5/96 − (ρ + π̃)/2`, with `ρ` the
rotation-orbit amplitude and `π̃ = π + 2u` the reduced in-plane one, both
living on pairs of plaquettes that share a link. ADR 0020 settled `u` from
outside both pipelines: the historical exact kernel right, the cold v10a.26
dump wrong by 4.13. The shared-link pair was the next bounded step, and the
obstacle was priced there: its baryonic histories `{Q, Q, P̄, P̄}` reach the
pure-six Haar family, which the pinned engine evaluates in 264–398 s and
gigabytes per integral, and one element of one pair needs 3,744 of them.

## What was built

`workhouse.haar_epsilon`: the same Haar integrals with the ε-tensors kept as
ε's. The engine expands every ε-pair into 3! permutation deltas and carries
set partitions, which is exact and efficient for balanced families and
exponential for determinant ones (six links at ×6 each, nothing merging, then
×456). After the projectors are inserted the integrand is a closed δ/ε
network, and such a network reduces by three identities alone — `εε` fully
contracted is 6, sharing two indices is `2δ`, sharing one is `δδ − δδ` —
branching at most two ways per ε-pair. Balanced links still go through the
engine's own per-link contraction first. The module agrees with the engine
exactly on every family the engine can price and on two pure-six integrals
the engine took 400 s each to produce; it does those in 0.02 s.

## What was computed

`runs/g3_shared_link_pair_2026-09-02`. The lattice fourth-order element
between two plaquettes is a finite sum of connected cluster cumulants. A
four-insertion history with net charge `P Q̄` is one of two kinds: `P` and `Q̄`
with one `X X̄` pair besides, or — when `P` and `Q` are two faces of one cube —
the cube's *other four faces*, each once, because a cube's six faces have zero
net triality. So

    H4_PQ = W(P,Q) + Σ_X [W(P,Q,X) − W(P,Q)] + Σ_cubes D_cube,

`X` over the plaquettes sharing a link with the pair (an `X` five sites away
gives exactly zero on every element: the linked-cluster gate), and `D_cube` the
direct term over the cube-completion histories on the six-face cluster, which
no fold or `A`-term reaches. The pair cluster is the engine's full assembly
with `A = PVP` the baryonic vertex and the baryonic histories included. The
cluster machinery is the replication run's; nothing reads either kernel.

- **In-plane, π.** Pair cluster `−17612026391/1147250744640`, eighteen
  single-contact dressings at `−385/1997568`, two shared-link plaquettes at
  `135671797/105250609440`, no cube (coplanar faces share none): total
  `−20535103905179/1264270320593280`, the historical record to the digit.
- **Normal, ν.** Disjoint pair 0, sixteen single-contact dressings 0, the four
  side faces at `−u` each, and the cube completion through those four faces
  `−5/48`: total `−5/48 − 4u`, the agreed record to the digit. The primitive
  cube completion is the cube-completion channel, computed.
- **Rotation, ρ.** The same pair cluster (two 4-cycles sharing one edge is one
  abstract cluster), fourteen single-contact dressings, two shared-link
  plaquettes, two *corner* faces (three faces at a cube vertex, pairwise
  sharing a link) at `−2580244782961/398756546697600`, and the cube
  completion through the other four faces of the shared cube at `53/768`, not
  `5/48`: total `588708011765248393/14501180577204921600 = +0.0405972`.
  The historical record is `+0.0082309`, the cold `−0.0879774`. Neither.
- **The ε-sector.** The ε-blind assembly (every unbalanced-family integral
  dropped: the "direct balanced contraction" U5 makes a prediction for)
  leaves every dressing unchanged and moves each pair cluster by exactly
  `−55/13872`, so the ε-sector of `ρ + π̃` is `−55/6936`, not U5's `−25/512`.
- **A convention.** The corpus orients its plane basis (0,1), (1,2), (2,0). An
  x-then-z traversal of a (0,2) plaquette is the record's conjugate and flips
  every C-odd element; the perpendicular pair here uses the (2,0) traversal.

## What the ρ result rests on

Every component is validated on a record both pipelines agree on, or by a
second implementation: the pair cluster and both dressing classes on `π`
(exact); the cube term and the side chains on `ν` (exact); the corner cluster
by `workhouse.chain_cluster`, a different resolvent, a different assembly form
and the engine's own Haar integrals, which returns the identical rational.
What is *not* available is a record both kernels got right that contains a
corner cluster, because only a perpendicular shared-link pair has one. So
the assembled `ρ` is validated piecewise and not as a whole, and that is the
difference between recording it and promoting it.

## Decision

- **G3.** The route "independent cross-amplitude computation" is `done`. The
  wall it was blocked on was the representation, not the hot loop.
- **U5.** `refuted`, by its own falsifier. What that leaves open is C10's
  question about the continuation shift `Δβ_3 = 25/64`: it is not the
  ε-sector's contribution to the shape.
- **C2.** Decided against the cold dump on every amplitude checked (`u`, `π`,
  `ρ`), and against the historical kernel on `ρ` — so the historical `C_shp`
  is not the fourth-order coefficient either. The assembled value
  `C_shp = −5/96 − u − (ρ + π)/2` is recorded as C2's third side, not
  promoted; C2 stays `open`, because the coefficient now rests on the corner
  cluster and the corner cluster has no agreed record. What closes it is a
  third implementation of the corner cluster, or the historical pipeline's
  own face-resolved ledger for the eighteen three-clusters, which this
  repository does not hold.
- **G14.** The Hodge form's single weight on the cube Laplacian is a
  reparametrisation, not the mechanism: the cube-completion channel is
  `−5/48` for opposite faces and `53/768` for adjacent ones. A mechanism for
  the tier collapse has to produce both.

## Consequences

- Checks in the kernel-orbits suite reading the pinned certificate: the
  linked-cluster gate, `π` exact, `ν` exact, the corner cluster's agreement
  between implementations (run live), the `ρ` finding, the `C_shp` finding,
  the U5 finding; the dressing constants, the corner cumulant, the ε-sector
  and the assembled values registered by value.
- `workhouse.haar_epsilon` with `tests/test_haar_epsilon.py`; the engine stays
  the source of every projector and of the balanced contraction.
- The run record holds every stage's console log and per-stage JSON for the
  three pairs; the assembled certificate is what the checks read.
