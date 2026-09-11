# Universal Cellular Hodge-Feshbach Algebra and Tetrahedral Scope

Date: 2026-09-11. Corrected by Codex following review of the submitted
Universal Cellular Hodge-Feshbach package. Targets: U3, U7, G14, G9.

The received sources are preserved byte-for-byte under
`runs/universal_cellular_hodge_repair_2026-09-11/received/`, with original
paths and SHA-256 digests in `received-manifest.json`. The earlier review is
`runs/universal_cellular_hodge_review_2026-09-11/README.md`. This edition
corrects the shifted operator, the Pi4 expansion, physical-history claims,
and formalization scope. It supersedes the received interpretation, while
retaining its valid cellular and commutant algebra.

## 1. Scope and established inputs

We distinguish three spaces: cellular face chains, the cubic Bloch fibre,
and the physical Haar/Fierz Hilbert space. A boundary-flux label does not
identify a vector or a retained projector in the third space.

The existing `RESULT:HODGE_FESHBACH_SPLITTING` establishes the cubic Hodge
relations, while `RESULT:TIER_COLLAPSE_ACTUAL_H4_SUPPORT` establishes the
fourth-order consequence for the actual support `{I,U,S,S^2,R}`. These results
are retained. The broader R-degree-only assertion had already been refuted
by `sigma(UR)=-2 q e2`; the present result does not revive it.

## 2. Part I: The Universal Cellular Hodge-Feshbach Spectral Theorem

### 2.1 Cellular setting

Let M be the connected, closed, orientable boundary of a single regular
polyhedral 3-cell. Its faces and edges form a regular cellulation of S^2;
face boundaries use each incident edge once, and each edge belongs to two
faces. Use the unweighted orthonormal cellular bases over the reals.

Write F for the number of faces, B for the edge-by-face boundary matrix,
and psi for the fundamental cycle with face coordinates +1 or -1.
Orientations are arbitrary provided psi records their signs. The 3-cell
boundary map sends its generator to psi. Define

\[
L_d=B^T B,\quad L_u=\psi\psi^T,\quad
P=\psi\psi^T/F,\quad Q=I-P.
\]

### 2.2 Universal spectral identities

**Theorem 1.** The face-cycle kernel is `ker L_d = ker B = R psi`,
`L_d L_u=0`, `L_u psi=F psi`, and `L_u Q=Q L_u=0`.

At every edge, `Bz=0` equates the two incident face coefficients after
orientation signs are removed. The connected dual adjacency graph makes
all these signed coefficients equal; thus z=c psi. Conversely B psi=0.
Since `z^T L_d z=||Bz||^2`, the two kernels agree. Finally
`||psi||^2=F`, so `P^2=P=P^T` and `L_u=F P`; multiplication proves all the
remaining identities. The eigenvalue F is the unique nonzero eigenvalue
of the **up-Laplacian**, not an assertion about the top eigenvalue of every
operator appearing in the research program.

### 2.3 Universal Up-Harmonicity of Excursions

**Theorem 2.** For any linear face operator R, the projected excursion
`phi=Q R psi` satisfies `L_u phi=0`.

This follows by multiplying the operator identity `L_u Q=0` by `R psi`.
The finite-dimensional linear operator is bounded. The Lean lemma proves
this rank-one inner-product identity without needing a cellular realization.

### 2.4 Total Laplacian Diagonal & Regularity Criterion

**Theorem 3.** For a face of perimeter p_f,

\[
(L_d+L_u)_{ff}=p_f+1.
\]

The column of B has p_f entries of magnitude one; the corresponding
coordinate of psi also has magnitude one. Their squared norms give the
formula. A scalar diagonal is equivalent to equal face perimeters, not to
geometric regularity. For instance, every triangulated polyhedral sphere
has diagonal 4, including a triangular bipyramid. For an n-gonal prism,
cap entries are n+1 and side entries are 5; equality holds only for n=4.
Scalar diagonal and scalar total operator are different statements.

## 3. Part II: Tetrahedral Face Algebra and the Physical-History Obligation

### 3.1 Tetrahedral Hodge duality

Use the coherently oriented tetrahedron, with psi=(1,1,1,1)^T and J=psi psi^T.

**Theorem 4.** `L_d=4I-J=4Q`, `L_u=J=4P`, `L_d+L_u=4I`,
and `L_d L_u=0`. Every pair of distinct faces shares one edge with opposite
signs; hence the diagonal of L_d is 3 and its off-diagonal entries are -1.
This calculates the claimed matrices directly. The unital Hodge algebra
is `span(P,Q)`, since the two nonzero orthogonal projections sum to I.

### 3.2 The S4 commutant

**Theorem 5.** On the real permutation representation on four faces,
`Comm(S4)=span(P,Q)`. Every commuting operator M satisfies `QMP=PMQ=0`
and `QMQ=c Q`; its traceless restriction to Im(Q) vanishes.

To prove necessity directly over the reals, simultaneous permutation of
row and column indices has just two orbits: diagonal entries and ordered
pairs of distinct indices. Thus a commuting matrix has one diagonal value a
and one off-diagonal value b. Conversely every such matrix commutes with
all permutations, and

\[
(a-b)I+bJ=(a+3b)P+(a-b)Q.
\]

The two projections are independent, proving the dimension and compression
statements. `Tr(Q)=3` removes the scalar part exactly. For the natural oriented
chain action a common sign twist leaves the commutant unchanged; changing face
orientations conjugates the matrices. No identification with a physical
Hamiltonian or its momentum-dependent coefficients is implied. Even a scalar
carrier coefficient can depend on momentum, so scalar compression alone is
not a theorem of no dispersion.

### 3.3 Feshbach Intermediate Annihilation of Retained Vectors

**Theorem 6.** If P is an orthogonal projector, Q=I-P, and the **actual input**
v to an intermediate projected resolvent lies in Im(P), then Qv=0 and every
subsequent linear map in that projected chain produces zero. In the rank-one
case `P=psi psi^T/||psi||^2`, this applies to v=c psi.

Proof: Pv=v implies `(I-P)v=0`. This does not prove that any particular
unprojected insertion prefix remains that same vector when earlier Q
projections and resolvents are inserted. Actual projected states must be
used at every step. The Lean theorem proves the rank-one retained-vector
identity, not a physical history enumeration or perturbative coefficient.

### 3.4 Open physical-history identification

The submitted enumeration starts from the boundary flux of face 0, adds
four signed face boundaries, and ends at face 1. There are 96 such additive
paths. Exactly 60 have a strict prefix equal to the start boundary, end
boundary, or zero; the other 36 lack that predicate. Including all four
positive face boundaries instead gives 62 flagged paths. None of these
counts incorporates Haar contractions, Fierz channels, electric denominators,
or a physical retained projection.

For the face-space projector above, `Q psi=0` but

\[
Q e_0=(3,-1,-1,-1)^T/4,\qquad \|Qe_0\|^2=3/4.
\]

Therefore a return to a face boundary is not established to be a return to
this carrier line. Likewise a zero flux label is not the zero Hilbert vector.
The earlier inference that all 60 physical contributions vanish is withdrawn
as unsupported. The desired physical vanishing is **open**, not refuted by
this face-space diagnostic. Construct the actual retained space, insertion
states, projections, and resolvents to decide it. U3 and the broader U7
unification remain conjectured; their established algebraic ingredients survive.

## 4. Part III: The R S^m R Carrier Symbol Master Theorem

### 4.1 The shifted cubic operator

Use exactly `HF._ops()` in `src/workhouse/invariants/hodge_feshbach.py`:

\[
U=L_u,\quad L_d+U=qI,\quad U^2=qU,\quad
S=L_d-4I=(q-4)I-U.
\]

Thus `L_tot=qI`, while `S psi=-4 psi` and S acts as `(q-4)I` on ker U.
The normalized carrier projector requires q>0; polynomial identities below
also hold at q=0, where the cubic carrier vector is zero.

### 4.2 Polynomial recurrence and operator powers

Define `Pi_0(q)=0` and

\[
\Pi_m(q)=\sum_{j=0}^{m-1}(-4)^j(q-4)^{m-1-j},\qquad
\Pi_{m+1}(q)=(q-4)^m-4\Pi_m(q).
\]

**Theorem 8 (all-power operator identity).** For linear endomorphisms U,R
over a field, if `U^2=qU`, then for every integer m>=0,

\[
S^m=(q-4)^m I-\Pi_m(q)U,\qquad
R S^m R=(q-4)^m R^2-\Pi_m(q)RUR.
\]

Induction starts at I. Multiplication by `(q-4)I-U` gives the next identity
using `U^2=qU` and the displayed recurrence. Multiplying on the left and
right by R gives the sandwich formula. The same induction gives
`q Pi_m(q)=(q-4)^m-(-4)^m`. For q nonzero one may divide; at q=0 use the
polynomial sum, with `Pi_m(0)=m(-4)^(m-1)` for m>=1 and Pi_0=0.
These operator and cleared-polynomial statements are formalized in Lean.

### 4.3 The carrier symbol

**Theorem 7 (carrier symbol).** In the cubic Laurent realization, use the
unnormalized symbol `sigma(A)=psi^dagger A psi` and elementary invariants
`q=e1`, e2, e3. The existing exact evaluations
`sigma(R^2)=q e2+3e3` and `sigma(RUR)=4e2^2`, substituted into Theorem 8, give

\[
\sigma(R S^m R)=(q-4)^m(qe_2+3e_3)-4\Pi_m(q)e_2^2.
\]

The first polynomials are:

- Pi_0=0;
- Pi_1=1;
- Pi_2=q-8;
- Pi_3=q^2-12q+48;
- **Pi_4=q^3-16q^2+96q-256**.

The general formula has an analytic proof with an all-power Lean operator
ingredient and separately exact Laurent base-symbol checks. It is not claimed
that the full Laurent realization is formalized in Lean. The two R-sandwiched
operator directions suffice for all m; the coefficients of `q e2` and `3e3`
in the R^2 contribution share the same multiplier. Which operator words the
sixth-order physical dynamics populates remains a G9/G10 obligation.

## 5. Verification and consequences

`src/workhouse/invariants/universal_cellular_hodge.py` calculates seven finite
cell controls, the full 16-variable S4 commutant, the scoped flux-count finding,
and master-symbol instances m=0,...,4 with the exact Laurent premises.
`scripts/verify_universal_hodge_tetrahedral.py` runs that same registered suite.
The tests additionally check reoriented faces, a nonregular triangulated cell,
q=0, explicit Pi4, and the distinction between raw and projected prefixes.

The source-to-proof ledger separates the full rank-one and operator-power
statements from their support of cellular, commutant, and Laurent claims.
The correction enables exact finite-cell Hodge reasoning and arbitrary-length
R S^m R reduction. It does not establish the physical tetrahedral history
identification, the U3/U7 common mechanism, the sixth-order dynamics, or a
continuum conclusion. Validation and publication receipts are maintained in
`runs/universal_cellular_hodge_repair_2026-09-11/README.md`.
