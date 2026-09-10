# A uniform Gaussian quantum fast floor on actual coupled planar rectangles

## Result

Let the open lattice have `2m` by `2n` square faces, with every original
edge included in the electric form. Partition its faces into disjoint
`2 x 2` blocks and retain the three components of the summed linear face
flux in each block. The exact Gaussian quantum operator, after subtraction
of its ground energy, satisfies

\[
\boxed{L_{0,\Lambda}\ge \frac1{\sqrt2}(I-P_{0,\Lambda}) .}
\tag{G1}
\]

Here `P0` is conditional expectation onto all retained flux vectors in
the *coupled Gaussian quantum ground measure*. In particular the closed
fast compression, on all oscillator degrees, obeys

\[
\boxed{F_{0,\Lambda}\ge\frac1{\sqrt2}I,\qquad
\|F_{0,\Lambda}^{-1}\|\le\sqrt2 .}
\tag{G2}
\]

The constants do not depend on either side length. The same assertions
hold after simultaneous color-rotation invariance is imposed. No
invariance of the retained subspace under `L0` is assumed.

This is a result for the actual coupled Gaussian tangent family. It does
not by itself assert a uniform finite-coupling quantum floor.

## Original edges give the face operator

Orient all horizontal and vertical edges of the rectangular grid. Write
`D` for its oriented face-edge incidence matrix: every face has four
entries `+1` or `-1`; the entries on a shared edge have opposite signs.
At the identity configuration the linear face variables are the curls of
the edge variables. Applying the original-edge electric derivatives to
functions of these curls gives exactly

\[
C_\Lambda=DD^T=4I-\operatorname{Adj}_\Lambda .
\tag{G3}
\]

There are no independent-block replacements in (G3). Every shared edge
produces its actual `-1` off-diagonal entry. Boundary edges contribute
their diagonal terms. A simply connected open rectangle has independent
face curls, and `C` is strictly positive.

With each face flux a vector in `R^3`, the normalized tangent Hamiltonian
is

\[
H_0=-\tfrac12\nabla^T(C\otimes I_3)\nabla
       +\tfrac12\sum_f|X_f|^2 .
\tag{G4}
\]

Its ground is proportional to
`exp[- X^T(C^(-1/2) tensor I3)X/2]`. Consequently the quantum ground
measure has covariance

\[
\Sigma=\tfrac12 C^{1/2}\otimes I_3,
\tag{G5}
\]

and its one-particle excitation operator is `h=C^(1/2)`.

## Two exact matrix certificates

Let `E` be the spatial subspace of vectors constant on each `2 x 2`
block. Write `P_E` for its ordinary Euclidean orthogonal projection and
`Q_E=I-P_E`. On one block, ordered row by row, put
`v=(1,-1,-1,1)^T`. Its four internal face-adjacency edges form a cycle,
whose graph Laplacian satisfies the exact identity

\[
L_B=2Q_{E,B}+\tfrac12vv^T.
\tag{G6}
\]

All edges joining distinct blocks add the nonnegative jump forms
`(e_f-e_k)(e_f-e_k)^T`. Original edges on the outer boundary add
`e_f e_f^T`. Summing (G6) therefore proves

\[
\boxed{C_\Lambda\ge2Q_E.}
\tag{G7}
\]

Also

\[
8I-C_\Lambda=
\sum_{\{f,k\}\text{ adjacent}}(e_f+e_k)(e_f+e_k)^T
+\sum_f(4-\deg f)e_f e_f^T\ge0.
\tag{G8}
\]

Thus `C <= 8I`, uniformly in the rectangle. These are explicit positive
matrix decompositions, not numerical eigenvalue inferences.

## The retained direction must use the true quantum covariance

Whiten the Gaussian variable by `Z=sqrt(2) C^(-1/4) X`. A retained linear
observation `e^T X`, with `e` in `E`, is
`(C^(1/4)e)^T Z/sqrt(2)`. Its correct Gaussian one-particle subspace is
therefore

\[
\mathcal R=C^{1/4}E,\qquad P_0=\Gamma(P_{\mathcal R}\otimes I_3).
\tag{G9}
\]

Replacing this covariance-weighted subspace by `E` would change the
source projection. The proof below uses (G9).

The source reduces the reference Hamiltonian on a single `2 x 2` block,
but generally fails to reduce it when those blocks share original edges.
This can be checked without numerical matrix roots: invariance of
`C^(1/4)E` under `sqrt(C)` is equivalent to invariance of `E` under `C`.
The latter fails already on the `2 x 4` rectangle. The exact controls
below include this nonreduction check on each tested rectangle.

**Matrix lemma.** Suppose `C>0`, `C>=c Q_E`, and `C<=M I`. Set
`R=C^(1/4)E`. Then

\[
\boxed{C^{1/2}\ge\frac{c}{\sqrt M}Q_{\mathcal R}.}
\tag{G10}
\]

Proof: The first assumption is equivalent, by conjugation and equality
of the two operator norms, to

\[
Q_E C^{-1}Q_E\le c^{-1}Q_E.
\tag{G11}
\]

For `z` perpendicular to `R`, let `f=C^(1/4)z`. Then `f` is perpendicular
to `E`. Consequently

\[
\langle z,C^{-1/2}z\rangle
=\langle f,C^{-1}f\rangle
\le c^{-1}\|f\|^2
\le\frac{\sqrt M}{c}\|z\|^2.
\tag{G12}
\]

The final inequality uses `C^(1/2)<=sqrt(M) I` and
`||f||^2=<z,C^(1/2)z>`. Thus
`Q_R C^(-1/2) Q_R <= sqrt(M)/c Q_R`. The same conjugation/norm
equivalence gives (G10). Taking `c=2`, `M=8` yields

\[
h=C^{1/2}\ge\frac1{\sqrt2}Q_{\mathcal R}.
\tag{G13}
\]

The comparison is a full operator inequality on the one-particle space,
not merely a lower bound on its restricted diagonal block.

## All oscillator degrees, including the nonreducing source graph

The ground-state transformed quantum operator is `L0=dGamma(h tensor
I3)`. On the `N`-particle symmetric tensor space, (G13) gives

\[
d\Gamma(h)\ge\frac1{\sqrt2}\sum_{j=1}^{N}(Q_{\mathcal R})_j
\ge\frac1{\sqrt2}(I-P_{\mathcal R}^{\otimes N}).
\tag{G14}
\]

The second inequality holds because the commuting projections on the
different tensor factors count at least one fast particle off the
all-retained tensor subspace. Summing over all `N`, including the vacuum,
proves (G1). Finite Gaussian polynomials are a form core, so closure
proves the assertion for every state in the quantum form domain.

The simultaneous color rotations commute with `L0` and with `P0`.
Restriction to their invariant space preserves (G1), and conditional
expectation of an invariant state is an invariant function of the
retained vectors. Thus this is exactly the physical retained source
space, rather than a larger unphysical replacement.

For a complex shift with `Re z < 1/sqrt(2)`, the corresponding resolvent
bound is

\[
\|(F_{0,\Lambda}-z)^{-1}\|
\le(1/\sqrt2-\operatorname{Re}z)^{-1}.
\tag{G15}
\]

In the ground measure, (G1) is the complete-edge conditional inequality

\[
\frac12\int(\nabla f)^T(C\otimes I_3)\nabla f\,d\mu_0
\ge\frac1{\sqrt2}\|f\|_{L^2(\mu_0)}^2,
\qquad E_{\mu_0}[f\mid \{\text{block flux vectors}\}]=0.
\tag{G16}
\]

## The exact reference Schur graph remains available

Decompose `L0` using its actual retained projection, and let `J0 p` be
the form-minimizing extension of a retained source `p`. Its fast part is
`Q J0 p=-F0^(-1) B0* p` wherever the block expression is defined, with
the same identity in the form-dual realization otherwise. Put
`s0[p]=a0[J0 p]`, the exact Schur form. Equation (G1) gives

\[
\boxed{\|QJ_0p\|^2\le\sqrt2\,s_0[p].}
\tag{G17}
\]

Thus growing-volume nonreduction does not obstruct either the reference
fast inverse or its graph lift. This conclusion retains the actual source
covariance and all oscillator levels.

## Remaining transport requirement

To transfer this theorem to the full coupled finite-coupling operator,
one needs an estimate in a common source-compatible form realization
that preserves a positive portion of (G1), uniformly over the coupled
rectangles. Fixed-block low-eigenvalue convergence does not provide
that estimate. Also, `sqrt(C)` and the covariance-weighted source
projection are nonlocal, so (G1) alone is not a finite-range
Combes--Thomas hypothesis. An independently proved `L2` synthesis bound
for the full residual would already combine with an interacting analogue
of (G2) without needing spatial differentiation of that residual.

## Reproducible checks

`grid_verify_gaussian_floor.py` verifies the original incidence matrix,
both exact positive decompositions, and the block projector identities
with rational arithmetic on a family of rectangles. Its optional NumPy
diagnostics check the covariance-weighted projection, the fractional
comparison and nonreduction; these diagnostics are explicitly separate
from the exact algebra and from the proof for arbitrary size above.
