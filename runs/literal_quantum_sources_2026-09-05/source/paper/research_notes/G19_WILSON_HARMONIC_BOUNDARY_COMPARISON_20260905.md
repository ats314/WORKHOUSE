# Original-link harmonic boundary comparison at every planar block size

5 September 2026. Analytic continuation of the physical scale-block package. The main new result is an all-size coercivity and spectral-complement
bound that retains every interface edge. Its constants are independent of
the total number of blocks. It also gives a precise spectral frame for box
averages and identifies the frequency weight carried by literal face sources.

This calculation concerns the actual Wilson Hamiltonian's harmonic Hessian
on a finite planar lattice disk. The harmonic spectral projection is not
identified with an OS-history block map. Uniform nonlinear errors remain separate obligations. The
[three-dimensional companion](G19_WILSON_THREE_DIMENSIONAL_HARMONIC_BOUNDARY_20260905.md)
proves the periodic link-Hessian analogue with Coulomb and Bianchi constraints.

## 1. Established inputs and the open successor

Before calculating, `workhouse why G19` was queried. It records the live
continuum-trajectory route and the closed raw-averaging/diffusion route, with
`RESULT:CONDITIONAL_GRADIENT_REPAIR` and
`RESULT:WILSON_BLOCK_SCORE_OBSTRUCTION` as closures. The current research map
specifies the actual complement comparison for coupled or overlapping blocks
as the next target. Searches of current research notes and native sources
found no existing all-size planar curl/box-mean comparison of the form below.

The established two-square Hessian has frequencies sqrt(3), sqrt(5), from
its seven original links. The new identity recovers those values as one
instance and retains the edges coupling arbitrarily many neighboring boxes.
The earlier all-rank fourth-order, fixed-spacing, source-frame, and physical
strip theorems are not recomputed or assumed missing.

## 2. Quotient Hessians from the original oriented links

Let D0:R^V -> R^E be the oriented vertex-edge gradient and let
C:R^E -> R^F be the oriented edge-face curl of an nx-by-ny square-plaquette
rectangle with all its boundary links. The rectangle is a disk. Then

```text
C D0=0, rank D0=|V|-1, rank C=|F|=|E|-|V|+1,
ker C=ran D0.
```

For SU(N), use the established norm -2ReTr(XY), in every Lie-algebra color
coordinate. Write link variables exp(g x_e), u=g^-4, and use the actual
electric Hamiltonian (1/2)sum_e C2_e and shifted magnetic potential
2u sum_p[N-ReTr U_p]. The leading operator after division by sqrt(u) is

```text
h_link=-(1/2)Delta_(ker D0*)+(1/2)||C x||^2.             (1)
```

This removes the linear gauge gradients, and residual simultaneous Ad
invariance gives the physical harmonic subspace. There are no harmonic
one-form zero modes on this disk. On a graph with holes or on a torus,
such modes would have to be retained separately.

For the linearized face curvature phi=Cx, put K=C C*. The minimum-norm link
lift is x=C* K^-1 phi. Hence the quotient metric is K^-1 and its co-metric
is K. The exact face-coordinate oscillator is

```text
h_face=-(1/2)grad_phi* K grad_phi+(1/2)||phi||^2.         (2)
```

Each interior link shared by faces p,q contributes
(e_p-e_q)(e_p-e_q)* to K. Each exterior boundary link contributes e_p e_p*.
Consequently

```text
K=4I-A_face,                                           (3)
```

where A_face is nearest-neighbor adjacency of the face rectangle. In
particular every face has diagonal 4, including boundary faces. Replacing
this by the degree-minus-adjacency Neumann graph Laplacian deletes genuine
boundary-link energy and introduces a false zero mode.

The nonzero oscillator frequencies are the singular values of C, or
sqrt(lambda_j(K)). This formulation extends to a general finite complex
after restricting curl to the gauge quotient; face Bianchi dependencies
must then be removed, rather than treated as physical zero-frequency
oscillators. For the planar disk C has independent rows, so (2) is exact
without an additional face constraint.

## 3. All-size strip and rectangular spectra

Equation (3) is the Kronecker sum of two one-dimensional Dirichlet path
Laplacians. Separation of the sine eigenvectors gives

```text
lambda_pq=4-2cos(pi p/(nx+1))-2cos(pi q/(ny+1)),
1<=p<=nx, 1<=q<=ny.                                   (4)
```

For a one-face-wide m-strip the values are
4-2cos(pi p/(m+1)), so its minimum stays above 2 as m grows. For an L-by-L
disk, lambda_min=4-4cos(pi/(L+1)), which is asymptotic to
2pi^2/(L+1)^2. A uniform long-strip gap therefore cannot be substituted for
a gap uniform under growth in both directions.

There is no adjoint singlet with one oscillator quantum. Two quanta in a
lowest-frequency mode have a scalar color contraction. Thus the exact first
physical harmonic gap is

```text
gap_phys,harm=2sqrt(u)sqrt(lambda_min(K)).               (5)
```

This recovers the two-square value 2sqrt(3)sqrt(u). At each fixed finite
rectangle the same compact harmonic-well localization used by the earlier
strip work promotes the leading coefficient to the nonlinear finite-graph
gap with an o(sqrt(u)) error. The argument here supplies no bound on that
error uniform in nx,ny; the all-size claims below concern the exact Hessian.

## 4. Gluing retains a positive sum of all interface energies

Partition an nx-by-ny rectangle into r disjoint L-by-L face boxes, with
nx and ny multiples of L and L>=2. Let B:R^r -> R^F map a coefficient to
the normalized constant on its box (value 1/L). Then B*B=I; put P=BB*,
Q=I-P. Let L_N(B_i) be the internal graph Laplacian of a single box,
with Neumann boundary, and take the direct sum over boxes. Original-link
incidence gives the exact identity

```text
K = direct_sum_i L_N(B_i)
    +sum_(inter-box edges p~q) (e_p-e_q)(e_p-e_q)*
    +sum_(outer boundary links at p) e_p e_p*.          (6)
```

No interface has been discarded from the operator. Both final sums are
positive semidefinite, so they may be dropped only for a lower bound.

The internal box Neumann eigenvalues are

```text
4sin^2(pi p/(2L))+4sin^2(pi q/(2L)),  0<=p,q<L.
```

Its constants form the kernel. The first nonzero value is
kappa_L=4sin^2(pi/(2L)); sin x>=2x/pi for 0<=x<=pi/2 gives
kappa_L>=4/L^2. Summing the exact internal Poincare bounds in (6) proves

```text
K >= kappa_L Q >= (4/L^2)Q.                            (7)
```

This is the requested size-controlled comparison. It holds independently
of r and of the size of the full rectangle. Unequal rectangular boxes have
the same statement with the largest box side replacing L. Boxes with
partial boundary can be handled with their own internal Poincare constants;
an arbitrary geometric partition is not automatically covered by (7).

## 5. An exactly reducing harmonic fast complement

Order the spatial eigenvalues increasingly. Since P has rank r, min-max
applied to (7) gives

```text
lambda_(r+1)(K)>=kappa_L.                              (8)
```

Retain the lowest r spatial normal modes, including all N^2-1 color copies,
and require the remaining oscillator modes to be in their joint ground
state. This ground projection P_fast,0 is invariant under the global color
action and reduces the exact harmonic Hamiltonian. Its orthogonal
complement contains at least one fast quantum, so

```text
H_harm-E0 >= sqrt(u)sqrt(kappa_L)(I-P_fast,0)
          >= (2sqrt(u)/L)(I-P_fast,0).                 (9)
```

The same inequality holds on the physical invariant subspace. A physical
complement vector may pair one fast adjoint quantum with a slow adjoint
quantum; its energy must not be estimated by automatically doubling the
fast frequency. Inequality (9) uses the valid one-quantum lower bound.

With the established convention
H_phys=c_H(a)g_H^2 H/a, u=g_H^-4, the lower bound in (9) becomes
2c_H(a)/(La). If a_coarse=La, this is a positive constant times
1/a_coarse, uniformly in the number of boxes. This is the scale behavior
needed for a harmonic ultraviolet complement. It does not assert that the
global normal-mode projection is a local Wilson or OS blocking map.

## 6. Box averages form a stable low-mode frame

Let E_Lambda be any spectral projection of K supported in [0,Lambda],
where Lambda<kappa_L. For v in its range, (7) implies

```text
||Qv||^2 <= Lambda/kappa_L ||v||^2,
E_Lambda P E_Lambda >= (1-Lambda/kappa_L)E_Lambda.      (10)
```

Thus the vectors E_Lambda B e_i form a frame for the whole low spatial
subspace, with bounds 1-Lambda/kappa_L and 1. The inverse of its frame
operator has norm at most (1-Lambda/kappa_L)^-1. This is a frame statement:
the coefficient map into r box labels can be redundant. An injective map
from low modes to box averages is not asserted to be onto all r labels.

For Lambda<=kappa_L/4 the bounds are 3/4 and 1, independent of r. The same
quadratic-form proof works on l2(Z^2) with a periodic partition into finite
boxes, since all sums are locally finite and the operators are bounded.
This infinite-lattice statement is about the harmonic spatial operator,
not a nonlinear Wilson state or its OS Hilbert space.

## 7. Coordinate and literal-source identification

In (2), K occurs in the kinetic energy. A local-index unit-kinetic operator
with potential K is obtained by Fourier exchange of face position and
momentum: its coordinate xi is electric-dual to phi. Equivalently one may
use y=K^-1/2 phi, but that coordinate transformation is spatially nonlocal.
Accordingly, the box mean in that unit-kinetic chart is not automatically
the arithmetic mean of literal face holonomies.

In normal-mode Fock space, the literal linearized face coordinate satisfies

```text
phi(b)Omega=(1/sqrt(2)) a*(K^1/4 b)Omega,
xi(b)Omega=(1/sqrt(2)) a*(K^-1/4 b)Omega.                (11)
```

For a spectral band I=[epsilon,Lambda] with epsilon>0 and
Lambda<kappa_L, projected literal face sources have frame operator

```text
S_phi=(1/2)E_I K^1/4 P K^1/4 E_I,
(1/2)(1-Lambda/kappa_L)sqrt(epsilon) E_I
 <= S_phi <= (1/2)sqrt(Lambda) E_I.                    (12)
```

The lower bound degenerates when the band reaches zero frequency. Removing
that weight requires K^-1/4, an infrared-unbounded normalization in an
infinite volume. This is a concrete source-normalization obligation, not
an absence of low modes.

The linear sources in (11) transform in the adjoint representation and are
not physical scalar sources by themselves. Centered quadratic contractions
sum_a :phi_a(b)phi_a(c): create the singlet two-quantum states. After the
standard color and bosonic normalization, their synthesis map is the
symmetric tensor square of the one-particle map in (11). Therefore frame
bounds tensor-square on that physical two-quantum sector. They do not by
themselves span higher invariant oscillator sectors.

## 8. Connection to the exact harmonic Schur comparison

In the unit-kinetic chart split the spatial matrix using the box-mean
projection P and its complement Q:

```text
K=[[C,D],[D*,F]], F>=fI, f=kappa_L,
K0=C-D F^-1 D*, M=I+D F^-2 D*.
```

The [closed-form Schur proof](G19_FORM_SCHUR_SCALE_COMPARISON_20260905.md),
Section 5, retains the exact frequency-dependent memory term. Its static graph trial has potential K0 and norm M. If mu_j
are the eigenvalues of M^-1/2 K0 M^-1/2, the full spatial eigenvalues obey

```text
f mu_j/(f+mu_j) <= lambda_j(K) <= mu_j,  1<=j<=rank P.  (13)
```

This was independently checked: for 0<x<f the negative-energy Schur
complement satisfies

```text
S_-(x)=K0-xM-x^2 D F^-2(F-xI)^-1D*
      >=K0-[xf/(f-x)]M.
```

Schur inertia at x=f mu_j/(f+mu_j) proves the lower bound. The graph
q -> (q,-F^-1D*q) and min-max prove the upper bound. No small interface
coupling is required, and the conclusion does not assume every retained
lambda_j is below f. At low mu/f this gives the precise small parameter
for a harmonic Markov approximation, with its induced mass matrix kept.

## 9. Exact controls and remaining mathematical step

`check_harmonic_incidence_comparison.py` constructs original vertex/edge/face
matrices for six disks and checks the quotient lift and co-metric. Four
larger tiled rectangles retain every interface and boundary square, and
exact characteristic-polynomial root counts verify the retained-dimension
bound. Rational LDL certificates prove the local conservative Poincare
bound for box sides 2, 3, 4. A 4-by-4 low-mode calculation checks the frame
and literal-source frequency factor. The false Neumann outer boundary
creates the expected spurious zero mode. All acceptance uses exact
arithmetic; its JSON is reproducible from the fresh-output entry point.

The next full-theory step is specific: realize a reflection/time-compatible
Wilson block map whose linearization retains a comparable slow space;
bound its nonlinear and generated interface interactions relative to the
harmonic estimate (7), while keeping the induced kinetic mass and literal
source normalization. The [three-dimensional companion](G19_WILSON_THREE_DIMENSIONAL_HARMONIC_BOUNDARY_20260905.md)
proves a separate original-link Hodge bound with all torus harmonic modes
retained. Neither harmonic projection is identified with a nonlinear
OS-history complement or a literal local Wilson block map.
