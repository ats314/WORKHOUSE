# A box-count-uniform fast bound for periodic three-dimensional Wilson links

5 September 2026. Analytic harmonic boundary theorem. This proves an actual
three-dimensional cubic link-Hessian bound with all interbox edges present.
It supplies the fast squared-frequency hypothesis for the Gaussian Schur
comparison. It does not assert a positive unregulated torus Gaussian
vacuum, a nonlinear Wilson fast gap, or a local physical history block map.

## 1. Established Hodge input and the precise target

Before deriving this extension the current G14 graph and its curl/Hodge
records were queried. The exact existing check in
`src/workhouse/invariants/tier.py` proves the Fourier incidence identity
`B B*=qI-d conjugate(d)^T`. The existing plaquette-Hodge check proves the
complementary scalar-symbol identity for the up and down Laplacians.
The older Wilson Hessian derivation, recovered with digest
`ab2c9981fecceba6d4c4ed88ac6e9df8936908d3a7bbf2317acfbe0a24a8983b`, already
identifies the Hessian with the cochain curl energy. These are inputs,
not unresolved premises.

The new step is an explicit three-dimensional retained space with a fast
lower bound independent of the number of boxes. It repairs the dimensional
limitation of the planar face-box construction by working with link
cochains, imposing Coulomb transversality and retaining the torus harmonic
directions. The retained projection is generally spatially nonlocal.

## 2. Periodic cell conventions and exact Hodge identity

Let the cubic torus have basepoints `x in (Z/nZ)^3`, with n>=3. A positively
oriented edge is the pair `(x,j)`, j=1,2,3, with head x+e_j. Its reverse is
the negative of this oriented cell, not a separately identified basepoint
edge. Oriented faces use ordered pairs i<j; all coordinate additions are
modulo n. Periods one and two require separate multiplicity/orientation
conventions and are not part of this statement or its controls.

For a scalar site field define `delta_i f(x)=f(x+e_i)-f(x)`. A link field
is A=(A_1,A_2,A_3), with original-link norm
`||A||²=sum_(x,j)|A_j(x)|²`. All statements tensor with the chosen Lie
algebra and its fixed invariant inner product. Set

```text
(d0 f)_i=delta_i f,
(d1 A)_ij=delta_i A_j-delta_j A_i,              i<j,
d0* A=sum_i delta_i* A_i,
(d2 F)_123=delta_1 F_23-delta_2 F_13+delta_3 F_12.
```

The forward differences commute with one another and with their adjoints.
Direct expansion gives both cochain identities `d1 d0=0`, `d2 d1=0`, and
the exact link Hodge identity

```text
||d1 A||²+||d0* A||² = sum_(i,j) ||delta_i A_j||².         (1)
```

Equivalently `d1*d1+d0d0*=Delta_scalar tensor I_3`. The mixed terms cancel
after commuting the scalar forward/backward differences and taking real
parts of the inner products. This is also the real-space form of the
established Fourier identity, with scalar symbol
`q(k)=4sum_i sin²(k_i/2)`.

Define the transverse link space and its orthogonal projection by

```text
C=ker d0*,
P_C=I-d0(Delta_scalar)^+ d0*,
K_C=d1*d1 restricted to C.                               (2)
```

The pseudoinverse removes only the constant scalar gauge parameter. It
does not remove the constant link fields. Fourier decomposition shows

```text
dim C=2n³+1,
ker K_C=H1={A_j(x)=a_j, j=1,2,3},   dim H1=3             (3)
```

per scalar cochain component. With Lie-algebra values H1 has dimension
3dim(g). At every nonzero momentum the gradient has rank one, transverse
space has rank two, and K_C=q(k) on that space. At zero momentum all three
link directions are transverse and have zero curl.

Faces are not independent oscillators: `d2 d1=0` is the linear Bianchi
identity. Indeed `rank d1=2n³-2`, whereas there are 3n³ face coordinates.
Using all face components as an unconstrained potential space would insert
spurious directions. The proof below uses only the original link space.

## 3. Box means and the transverse retained space

Let L>=2 divide n and partition the basepoints into
`r=(n/L)^3` disjoint L-by-L-by-L boxes. For each box and each link direction
take the normalized indicator of its basepoints, with value L^(-3/2).
The resulting map

```text
B:R^(3r) -> R^(3n³),       B*B=I,
P_B=BB*,                  S=ran(P_C B) subset C          (4)
```

averages the basepoint components of all three link directions separately.
Edges crossing a box boundary still belong to the box of their basepoint;
they remain edges of the full torus and are not discarded from the energy.

Let P_S be the orthogonal projection onto S inside C, and
`Q_f=P_C-P_S` on the full link space. Then

```text
dim S<=3r,
H1 subset S,
ran Q_f=C intersect S_perp=ker d0* intersect ker B*.      (5)
```

The last equality follows from
`<A,P_C Bv>=<A,Bv>` for A in C. Thus fast fields have zero average of each
component in every box as well as zero divergence. Although these
constraints are explicit, the orthogonal retained projection uses the
global periodic Green operator in P_C and is generally nonlocal.

## 4. The uniform fast theorem

The Neumann path Laplacian on L sites has eigenvalues

```text
4sin²(pi j/(2L)),                  j=0,...,L-1.
```

Tensoring the three path bases proves the scalar cube Poincare inequality
with sharp first positive constant

```text
kappa_L=4sin²(pi/(2L)) >= 4/L².                          (6)
```

The elementary bound uses `sin t>=2t/pi` for 0<=t<=pi/2.
For each link component, sum its internal box gradient energies. Every
term omitted from the full periodic gradient form is the square of a
difference across an interface or a wrapping box boundary. Hence these
omitted terms are nonnegative, and (1), on C, gives

```text
<A,K_C A> >= kappa_L ||(I-P_B)A||²,       A in C.         (7)
```

For any such A, `P_C P_B A` belongs to S and

```text
dist(A,S) <= ||A-P_C P_B A||
          = ||P_C(I-P_B)A|| <= ||(I-P_B)A||.             (8)
```

Combining (7)-(8) proves the full quadratic-form inequality

```text
K_C >= kappa_L (I_C-P_S),
F=Q_f K_C Q_f restricted to ran Q_f >= kappa_L I.        (9)
```

This is uniform in r, with exact constant depending only on L. It does not
require the coupling between S and its complement to be small. All
interfaces remain in K_C and in its off-diagonal retained/fast blocks.
Positive face weights bounded below by w_min give the immediate variant
`F>=w_min kappa_L`, using their curl form lower bound; the identity (1)
itself is the unweighted identity.

There is also a useful explicitly positive decomposition. Put
`Delta_1=Delta_scalar tensor I_3` and
`R=Delta_1-kappa_L(I-P_B)>=0`. Since `P_C K_C P_C=P_C Delta_1 P_C`,

```text
K_C-kappa_L(I_C-P_S)
 = P_C R P_C + kappa_L[P_S-P_C P_B P_C] on C.            (10)
```

The second summand is nonnegative: `T=P_C B` is a contraction with range
S, so `TT*<=P_S`. This decomposition retains the Coulomb projection and
shows why a large number of interfaces does not destroy the fast constant.

## 5. Harmonic Wilson interpretation and the zero modes

In the original-link metric the Wilson tangent Hamiltonian on C has

```text
H_harm(u)=-(1/2)Delta_C+b_rho u <A,K_C A>,
Omega²=2b_rho u K_C.                                    (11)
```

For fundamental SU(N) in the established metric `b_rho=1/2`, its squared
frequencies are u times the eigenvalues of K_C. The positive fast
compression (9) therefore supplies a squared-frequency threshold
`2b_rho u kappa_L` for the retained/fast coordinate split.

However (11) on its full Euclidean tangent space has three harmonic
cochain directions per color with zero potential. It has no normalized
Gaussian vacuum in those directions. The compact torus Wilson problem
also has a nontrivial flat-holonomy space. Consequently the unique-flat-
orbit finite-cell theorem cannot be invoked on this torus.

Two precise ways to use the fast statement are available:

1. Add an explicitly declared positive squared-frequency regulator
   `mu² I_C` to the scaled matrix K_C. Then the Gaussian matrix is strictly
   positive and the fast compression is at least `kappa_L+mu²`. The
   Gaussian Schur memory/spectral theorem applies with this f, while all
   harmonic cochain directions stay in the retained space. No uniform
   positive full gap as mu tends to zero is inferred.
2. Keep the zero modes in the retained coarse Hamiltonian and use (9) as
   the fast quadratic input relative to that sector. A quantization and
   treatment of its flat variables must be specified; a covariance
   `(2Omega)^(-1)` on those zero modes is not defined.

The f in this paragraph is a lower bound for a finite squared-frequency
matrix. It is not automatically a bound on the restricted nonlinear
Hamiltonian form Q_H H Q_H in the closed-form Schur scale theorem. That
projection acts in a quantum Hilbert space, not in the link-coordinate
space C. A bridge between the two remains an explicit spectral obligation.

At the harmonic level a scale separation with L fixed gives frequency
order `sqrt(u)/L`; after the physical conversion
`H_phys=c_H(a)g_H² H/a`, `u=g_H^-4`, its fast scale is order
`c_H(a)/(La)`. The purpose of retaining S is exactly to allow the slow
frequencies, including (3), to remain coarse.

## 6. Source, history and nonlinear scope

P_C B is a specific Coulomb-projected coordinate construction. It is not
claimed to be the tangent of a prescribed local Wilson-loop block, and its
global Green kernel makes a locality identification substantive. Residual
global color rotations act equivariantly, but actual local gauge and
reflection/time-covariance conditions for a history map still require proof.

Even if its coordinate observation were fixed, the Gaussian observability
theorem says its whole-time history range can exceed its equal-time retained
space. Thus S, the Gaussian OS range and the graph of a Hamiltonian Schur
lift must not be equated by dimension counting. A regulator makes that
observability calculation well-defined but does not decide its answer.

The next nonlinear step requires a uniform control of the actual Wilson
form around the retained fields, including varying coarse ground energy,
interactions and the flat sector. The proven statement here removes the
planar restriction for the harmonic fast estimate: three-dimensional
shared edges and Bianchi constraints are handled with a constant uniform
in box count. It does not remove the spatial lattice cutoff or supply a
full continuum gap by itself.

## 7. Exact finite controls

[check_periodic_3d_fast_bound.py](../../runs/continuum_scale_comparison_2026-09-05/check_periodic_3d_fast_bound.py) constructs
the actual periodic oriented-link, face and cube incidence matrices for
periods n=3 and n=4, using respectively L=3 and L=2. It checks the two
cochain identities, exact Hodge matrix and positive interface decomposition.
Rational Fourier Green kernels certify the scalar pseudoinverse; selected
Coulomb projections test idempotence, all three retained harmonic directions
and the contraction in (8). Explicit divergence-free zero-box-mean fields
test the fast Rayleigh bound in the original link metric. The controls do
not construct the full retained projector P_S or infer an all-size theorem
from a large matrix positivity test. The nonlocal tail of a projected box
is recorded, and n=2 is deliberately rejected without a separate orientation
convention.

The saved JSON reports finite exact identities and examples. The proof for
every admitted n,L and box count is (1), the tensor Neumann inequality and
the projection argument (7)-(10); those analytic and all-size statements
are not inferred from the two finite cells.
