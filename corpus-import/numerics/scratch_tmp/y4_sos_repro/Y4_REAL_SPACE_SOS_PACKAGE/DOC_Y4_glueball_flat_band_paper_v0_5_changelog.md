# Draft v0.5 changelog

## New exact theorem

The momentum-space factorization is lifted to the local real-space operator identity

\[
C^\dagger(H_4-qI)C
=\frac{A}{4}\sum_iL_i^2
+\frac{B}{4}\sum_{i<j}L_iL_j,
\qquad
L_i=(T_i-I)^\dagger(T_i-I),
\]

with

\[
A=\frac5{12},\qquad
B=\frac{17607806155349}{275331901291200}.
\]

Equivalently,

\[
C^\dagger(H_4-qI)C
=\frac5{48}\sum_iL_i^2
+\frac{17607806155349}{1101327605164800}
\sum_{i<j}(\nabla_i\nabla_j)^\dagger(\nabla_i\nabla_j).
\]

The theorem identifies the two real-space carriers of fourth-order mobility:

- axial three-cube second differences `(-1,2,-1)`;
- planar four-cube checkerboard differences `(+1,-1,-1,+1)`.

## Exact 25-point stencil

The projected numerator operator is recorded explicitly with center, nearest-axis, double-axis, and face-diagonal weights. Its row sum vanishes exactly.

## Generalized eigenproblem

The paper now distinguishes the local numerator operator

\[
Q=C^\dagger(H_4-qI)C
\]

from the cube-boundary Gram operator

\[
G=C^\dagger C=\sum_iL_i.
\]

The physical fourth-order lift is therefore the generalized eigenproblem

\[
Q\phi=\lambda G\phi.
\]

## Verification update

Added the exact Fraction-arithmetic certificate `ENGINE_Y4_exact_real_space_sos_certificate.py`, the canonical semantic kernel hash, and the separate A100/PyTorch regression script `ENGINE_Y4_sos_a100_validation.py`.

## Outlook correction

The projected real-space SOS problem is no longer open. The remaining geometric refinement concerns the unprojected plaquette-space residual, while the principal group-theoretic bottleneck remains the stable-rank symbolic walled-Brauer contraction.
