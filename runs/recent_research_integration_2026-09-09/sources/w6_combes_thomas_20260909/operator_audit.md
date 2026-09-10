# Operator audit of the proposed Combes--Thomas closure

9 September 2026 UTC. Read-only source audit and a new exact finite-matrix
control. This note does not modify the theory graph.

The dual inverse-form target is the appropriate one. The proposed proof of
its spectral anchor, however, changes the actual operator and uses a gap
monotonicity implication that is false even for positive Dirichlet jumps.
This does not disprove the coupled Wilson floor or W6.

## 1. What the established floor actually says

The preceding [bouquet proof](../w6_quantum_attempt_20260909/fast_agent.md),
lines 171--189, proves

\[
g^2 Q(H_u-2e_u)Q\ge I
\]

for sufficiently small \(g\). Here \(H_u=h_u\otimes I+I\otimes h_u\)
is the full scalar-wavefunction Schrödinger operator on the two-loop
configuration space, and \(Q\) is the complement of literal retained
observables times its true ground. The proof uses the full compact-rotor
spectral gap, exact tensor addition and exact vacuum inclusion.

It does not prove a pointwise lower bound on a magnetic curvature
endomorphism. For example, with the actual SU(2) convention
\(v(K)=2-\operatorname{ReTr}K\), \(T=i\sigma_3/2\),

\[
v(-e^{tT})=2+2\cos(t/2),\qquad
\left.\frac{d^2}{dt^2}v(-e^{tT})\right|_{t=0}=-\tfrac12.
\]

Thus the magnetic Hessian itself is not globally positive. A positive
quantum excitation energy is compatible with this negative curvature.
Likewise, the separate result \(\inf\sigma(D_g)\le3g^2/4\) is an
**upper** bound on the vertical infimum. It cannot supply a negative
correction \(-3g^2/4\) to the full coupled floor.

The source definition of the full fast form is a compression of the
vacuum-subtracted quantum Hamiltonian in its specified source chart:

\[
F_{g,\Lambda}=Q_\Lambda\widetilde H_{g,\Lambda}Q_\Lambda.
\]

[SP1](../../ALL%20THEORY/WORKHOUSE/docs/derivations/wilson-spatial-schur-excess.md),
lines 44--58, explicitly defines the reference form compression. Lines
288--305 give the interacting source-straightening jets; already the first
one contains \([H_0,K_1^{\rm src}]\), in addition to the electric,
magnetic and vacuum terms. A gauge projection on lattice one-forms is not
by definition this literal-source complement.

A proposed identification with a covariant lattice one-form Laplacian
plus a block curvature field therefore needs an explicit isometry or
intertwining map, a closed-form identity, and the image of the literal
source complement. Commuting a ground-transformed scalar diffusion with
derivatives instead produces a one-form operator whose coefficients
involve derivatives of the **true joint ground**, not merely the bare
magnetic Hessian. None of these operator identifications is supplied by
the bouquet gap theorem.

## 2. Positive Dirichlet jumps need not preserve an excitation gap

Let \(J_{ij}=(e_i-e_j)(e_i-e_j)^T\), and define

\[
H_0=\begin{pmatrix}
16/25&-12/25&0\\
-12/25&9/25&0\\
0&0&1/100
\end{pmatrix},\qquad
V=\frac{99}{200}J_{12}\ge0.
\]

Exact rational calculation gives

\[
\sigma(H_0)=\{0,1/100,1\},\qquad
\sigma(H_0+V)=\{1/100,1/100,99/50\}.
\]

The added form is precisely a positive Dirichlet jump,
\(\langle q,Vq\rangle=(99/200)|q_1-q_2|^2\), yet the excitation gap
decreases from \(1/100\) to zero. This is a statement about excitation
energies; every absolute ordered eigenvalue is still nondecreasing.

The effect does not rely on a nonpositive or degenerate initial ground.
For \(\epsilon>0\), set

\[
H_{0,\epsilon}=H_0+\epsilon J_{23},\qquad
H_{1,\epsilon}=H_0+V+\epsilon J_{23}.
\]

Both matrices have negative off-diagonal entries on a connected graph,
so both have a unique strictly positive ground vector. Since
\(0\le\epsilon J_{23}\le2\epsilon I\), min--max gives

\[
\operatorname{gap}(H_{0,\epsilon})\ge1/100-2\epsilon,
\qquad
\operatorname{gap}(H_{1,\epsilon})\le2\epsilon.
\]

Their gap ratio tends to zero as \(\epsilon\downarrow0\), although
\(H_{1,\epsilon}-H_{0,\epsilon}=V\) is the same positive jump.
Subtracting a scalar constant if desired changes neither conclusion;
these are finite graph Schrödinger operators. This counterexample does
not claim that a Wilson interface has this spectrum. It disproves the
proposed inference from positive jump energy to a preserved
true-ground-subtracted floor.

The rational spectra and characteristic polynomial were checked exactly
with SymPy 1.14, using rational inputs:

\[
\det(\lambda I-H_0-V)
=\frac{(50\lambda-99)(100\lambda-1)^2}{500000}.
\]

The unique-positive-ground and \(\epsilon\)-bounds are analytic
consequences of irreducibility and form order, not finite sample claims.

## 3. The source graph already records the interface obligation

- [The native W6 note](../../ALL%20THEORY/WORKHOUSE/docs/derivations/wilson-selected-inverse-wall.md),
  lines 169--176, explains why positive bare perturbations do not imply
  the desired order after true vacuum subtraction, and supplies a
  simpler two-dimensional diagonal counterexample.
- [The common-Gauss theorem](../../WORKHOUSE-flat-holonomy-20260907/paper/research_notes/G19_WILSON_COMMON_GAUSS_LITERAL_FAST_FLOOR_20260905.md),
  lines 3--6, assumes no plaquette interactions between blocks. Lines
  424--433 state that ambient plaquettes and shared electric derivatives
  change the true vacuum and exact excitation-support decomposition;
  their comparison is the next interacting obligation.
- [The finite-cell and boundary theorem](../../WORKHOUSE-flat-holonomy-20260907/paper/research_notes/G19_WILSON_FINITE_CELL_GAP_AND_BOUNDARY_FORM_20260905.md),
  lines 314--343, proves an IMS identity with a controlled boundary error.
  It explicitly assumes no sign of the off-diagonal curl entries and
  records that transverse projection is nonlocal. Lines 279--310 give
  actual filled \(L\times L\) Wilson patches whose full physical gap has
  leading scaled coefficient proportional to
  \(\sqrt{4-4\cos(\pi/(L+1))}\to0\). This concerns the full physical
  gap, not a correctly chosen fast complement, and explains why the
  slow modes must be retained.
- [The physical fiber theorem](../../WORKHOUSE-flat-holonomy-20260907/paper/research_notes/G19_WILSON_PHYSICAL_FIBER_FAST_GAP_20260905.md),
  lines 321--342 and 401--409, separates its constrained-fiber energy
  and projection from the actual coupled quantum complement and
  explicitly leaves horizontal cross terms and ground energies to be
  compared.

## 4. The precise surviving floor target

One must prove the lower bound on the actual transported, vacuum-subtracted
form, on its actual literal-source complement. Bare interface positivity
alone gives, at best,

\[
H_{\rm coupled}-E_{\rm coupled}
\ge H_{\rm add}-E_{\rm add}
 -(E_{\rm coupled}-E_{\rm add})I,
\]

on a common Hilbert space before also accounting for the moving source.
It supplies no uniform excitation floor unless the ground-energy change
and source change are controlled in the relevant sector. A common exact
ground annihilated by the added positive interaction would be a useful
stronger hypothesis, but it is not established for the coupled Wilson
interfaces.

After an actual bound \(F_{g,\Lambda}\ge f I\) is proved, a **real**
shift \(z\le f-\delta\) gives the positive form
\(A_{g,\Lambda}\ge\delta I\). For complex \(z\), only the corresponding
accretivity statement follows; the complex resolvent pairing is not a
positive dual Hilbert norm. The real-energy W6 interval is the natural
setting of the Riesz dual-norm identity.

No graph claim was promoted. The source audit and exact jump example
identify why the proposed spectral anchor is still an independent
theorem rather than a consequence of the established bouquet floor.
