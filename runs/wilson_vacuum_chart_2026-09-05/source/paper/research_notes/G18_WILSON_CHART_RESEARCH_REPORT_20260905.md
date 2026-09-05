# The Wilson vacuum chart: research progress on 5 September 2026

This continuation supplies a local vacuum chart for the **actual symmetric
Wilson transfer at every fixed magnetic order**. It also derives an explicit
uniform bound for the entire second Taylor coefficient. Convergence to an
exact nonlinear chart and the complete thermodynamic Wilson source projection
remain the next tasks.

## Inputs and the question advanced

The imported 4 September excited-window note keeps

\[
 T_{\epsilon,L}(u)
 =e^{\tau uV_L/2}e^{-\tau K_{\epsilon,L}}e^{\tau uV_L/2}
\]

and its true Perron normalization. Its calibrated free kinetic gap is the
upstream physical input. The long temporal block used to describe the vacuum
and the shorter block used to separate the free excited shell have the same
Perron vector. The earlier note already established a local first rotation
and a uniform full-operator first derivative. It also exhibited why keeping
that rotation alone can leave an extensive quadratic vacuum-creation term.

The present work asks whether that next term can be removed locally, with
all spectator states retained, and whether the mechanism extends beyond
second order. It uses the actual bounded transfer product throughout.

## The new second-order result

Give each plaquette an independent coupling. Normalize each active subsystem
by its actual Perron eigenvalue and apply the first local rotation. Its
quadratic coefficient `A` has zero scalar vacuum component. On its link
support `X`, define

\[
 \chi_X=(1-D_X)^{-1}Q_XA\Omega_X,\qquad
 S_X=|\chi_X\rangle\langle\Omega_X|
      -|\Omega_X\rangle\langle\chi_X|,
 \qquad F_X=A+[D_X,S_X].
\]

The local gap bounds the inverse, and `F_X` annihilates the local vacuum on
both sides. A repeated plaquette occupies four links; an overlapping pair
occupies at most seven. Disjoint plaquette subsystems factor exactly,
including their Perron eigenvalues, so their quadratic contribution is the
product of the already anchored first coefficients.

This gives the complete operator coefficient, including its action on free
spectators. Counting supports that meet an arbitrary input excitation set
and damping untouched excitations yields

\[
 \sup_L\|[u^2]\widetilde{\mathcal D}_L\|
 \le\frac{40432}{5}f_*^2,
 \qquad f_*=J(s_1+2/E_s+\tau_0),\quad J=2N.
\]

This is the Taylor coefficient; the second derivative is twice it. The
bound is uniform in spatial volume, the admitted temporal meshes and link
representation dimension. The same local generators work for every positive
integer block power, because they are coefficients of its common rotated
Perron vector.

The full derivation is in
`G18_SECOND_ORDER_WILSON_VACUUM_CHART_20260905.md`.

## The arbitrary fixed-order extension

The same construction closes an induction on connected multivariate
monomials. After lower coefficients are anchored, disconnected degree-`n`
monomials already factor into anchored lower-degree components. A connected
residual has zero scalar vacuum part by the normalized eigenvector equation;
the inverse of `1-D_X` supplies the next local anti-Hermitian generator.

Thus every fixed degree has exact component factorization, support at most
`3n+1` links for each connected monomial, a uniform finite full-operator
coefficient bound, and generators independent of positive block power.
`G18_VACUUM_CHART_RECURSION_20260905.md` gives the induction and an explicit
Cauchy-bound recurrence. That recurrence proves finiteness at each degree;
it does not prove a positive convergence radius.

## What the executable checks establish

`src/workhouse/wilson_vacuum_chart.py` expands exact finite tensor models of
the symmetric transfer product in rational arithmetic. Its quadratic Perron
coefficient is computed before the rotations. The implementation distinguishes
a global rank-two vacuum-column rotation from the local rotations embedded
with identity on spectators; equality of vacuum columns alone would not
establish equality of these operator charts.

Live native invariant checks reconstruct:

1. A two-level negative control: the first chart leaves quadratic creation
   `97/96`, and the second generator `97/24` removes it exactly.
2. Overlapping/disjoint support identities, spectator operator entries and
   generator equality at distinct positive block powers.
3. Exact support maxima `16`, `336`, `2592/5`, including decreasing-tail
   inequalities, giving `40432/5` after the local activity factors.
4. The endpoint mixed-kick identity after substituting
   `x=exp(tau E_1), y=exp(tau E_2)`. Omitting the exponential's mixed kick
   leaves the exact residual `-tau^2/(xy-1)`, which is nonzero.

The focused tests include an independent two-level spectral oracle derived
from the trace and determinant of the unexpanded symmetric transfer. Two
noncommuting potentials check mixed coefficients, the temporal prefactor,
and the distinction between block-dependent Perron coefficients and
block-independent vacuum generators. Invalid supplied first generators and
nonisolated free vacuum inputs are rejected.

These are T1 finite algebra checks. The analytic untruncated and arbitrary-
order statements are research-note derivations under their explicit kinetic
premises; the Python results are not substituted for those arguments. The
finite local/global structural checks share a coefficient engine, whereas
the trace/determinant formulas provide a separate algebraic oracle. Execution
counts and sealed run outputs belong in their run record rather than this
authored overview.

The additional `src/workhouse/wilson_chart_recursion.py` oracle solves the
unrotated multivariate eigenproblem before constructing its local charts.
Its finite tensor-model checks pass through fourth order for overlapping
supports and through third order for a three-face chain. They compare the
single-face coefficients with closed spectral and diagonalizing-angle
formulas, reproduce the separate quadratic implementation, retain disjoint
and nonvacuum spectator factors, and test generator equality at different
block powers. A separate three-state characteristic-determinant calculation
with two noncommuting potentials also checks its cubic normalization. These
are tests of the implemented finite-order recursion, not machine proofs of
the analytic arbitrary-order theorem or of a convergence radius.

The endpoint-gauge note supplies a further exact reformulation of the actual
vacuum equation. Removing one magnetic endpoint retains the kinetic factor
beside the inverse and gives `r_tau(K_J)=tau/(exp(tau K_J)-1)` with the
proved bound `||r_tau(K_J)||<=1/(gamma |J|)` on exact excited-link support.
The disjoint-support creation algebra turns the normalized vacuum equation
into the exact connected-coordinate equation `v_J=r_tau(K_J) N_tau,J(u,v)`.
These endpoint and creator-log identities are proved in
`G18_WILSON_ENDPOINT_GAUGE_AND_MAJORANT_20260905.md`. Its nonlinear rooted
inequality (17), including uniform analytic definition on the stated ball,
remains unproved. That estimate would construct a convergent nonunitary
vacuum coordinate; a controlled unitary chart or an equivalent justified
excited-resolvent argument would still be required afterward.

## The next majorant and the preserved results

The endpoint gauge also has an exact creator-flow equation. Each local
plaquette contribution is a polynomial of degree at most eight in the
creator amplitudes: a nonzero product can use at most four disjoint creators
touching a four-link face on either side of its multiplication operator.
The remaining estimate concerns support-weight loss while integrating this
finite polynomial flow, together with the free kinetic damping. This gives
a concrete next calculation without presuming a convergence theorem.

The next calculation must control the growth of connected operator and
generator coefficients in a spatially rooted norm. A positive-radius
majorant for the transformed operator series is one intermediate result;
convergence and exact realization of the vacuum chart must also be proved.
The preceding excited-window theorem can then apply its full-operator
criterion, followed by thermodynamic range identification, source totality
and spatially weighted sharp-shell matching.

The native G18 gap remains open for these actual-Wilson tasks. Its completed
fixed-spacing Hamiltonian band/source construction remains recorded as
completed. This continuation does not reopen C2 or alter the established
all-rank coefficient results. It advances a different obstruction: the
nonlinear background-vacuum and operator/source bridge for the genuine
discrete-time transfer.
