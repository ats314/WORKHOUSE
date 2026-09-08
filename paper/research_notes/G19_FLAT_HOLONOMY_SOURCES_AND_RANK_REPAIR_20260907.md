# Flat-holonomy Wilson sources and a repair for the changing physical rank

7 September 2026. Analytic continuation of G19. The result is a uniform
geometric input to the compact-holonomy route, together with an obstruction
to differentiating its physical Coulomb projections across orbit types.
It does not assert the interacting quantum scale-comparison theorem.

The input is the actual matrix path observation and continuous alias
estimate in [the local-source theorem](G19_LOCAL_COVARIANT_AVERAGED_PATH_SOURCES_20260905.md),
Sections 2-5. The graph entries RESULT:WILSON_COVARIANT_BLOCK_SOURCES,
RESULT:WILSON_HARMONIC_CUBIC_OBSTRUCTION and G19 were read before this
continuation. Searches of the current research notes, decisions, ledgers and
imported note headings did not locate this background extension. That
targeted search is not a complete review of the wider corpus.

## 1. Objects, hypotheses and conclusions

Let n=Lm>=3, L>=2, on the labeled periodic cubic lattice used by the input.
Let G be a compact unitary matrix group, with Lie algebra of dimension D
and a fixed invariant inner product. Let U be any periodic flat G connection:
every elementary oriented plaquette has holonomy I. No assumption that its
three winding holonomies are central, small, or jointly contained in a
maximal torus of G is required. All edges, interfaces and winding paths are
retained. Flatness, rather than arbitrary compact coarse configurations,
is a hypothesis throughout the spectral statements below.

Use left-trivialized link variations U_e(t)=exp(t A_e)U_e. With

    (tau_i f)(x)=Ad(U_i(x)) f(x+e_i),
    nabla_i=tau_i-I,
    (d_U f)_i=nabla_i f,
    (c_U A)_ij=nabla_i A_j-nabla_j A_i,
    C_U=ker d_U*,              K_U=c_U* c_U |_C_U,

the norm is the original-link counting norm. Let M be exactly the input's
average of anchored length-L paths. At a flat U every summand in a fixed
M_i(v) equals the same group element U_c,i(v). Define its tangent by

    (T_U A)_i(v)= [d M_i(v)] U_c,i(v)^(-1).

This belongs to the represented Lie algebra. Let C_c,U=ker d_c,U* on the
coarse connection U_c, and let

    S_U=ran(T_U* |_C_c,U),    P_U=orthogonal projection onto S_U.

Then, as a full form on C_U,

    K_U >= 3072/(pi^10 L^2) (I_C_U-P_U)
        >= 1/(33 L^2) (I_C_U-P_U).                         (1)

The constant is independent of volume, all flat winding holonomies and
the dimension of their common stabilizer. If

    D_U=dim {X in Lie(G): Ad(H_j)X=X for j=1,2,3},

then

    dim C_U=2D n^3+D_U,        dim S_U=2D m^3+D_U,
    ker K_U subset S_U.                                     (2)

These are real dimensions. On SU(2), P_U cannot be norm-continuous across
central winding holonomies. Section 5 gives an explicit norm-one jump.
This does not contradict (1): the changing directions are changes of the
physical gauge quotient, and all physical zero modes remain observed.

There is a constructive repair for the coordinate problem. Keep all coarse
endpoint-covariant variables before imposing gauge invariance. T_U is then
onto the entire coarse link space, of fixed real dimension 3D m^3, and

    T_U T_U* >= L^(-2) I_coarse.                            (3)

uniformly in volume and flat U. Unlike P_U, the redundant source projection

    Ptilde_U=T_U*(T_U T_U*)^(-1)T_U                         (4)

has fixed rank and is smooth along smooth families of flat connections,
including at the rank change in (2). A fixed-background tangent chart of
the actual nonlinear observation also remains a submersion on a linkwise
neighborhood of radius 1/[2sqrt(6)L(7L-6)^2], independent of volume and
flat background. This is a smooth ambient observation construction, not
a replacement of the physical Gauss constraint or an identification with
the true-vacuum quantum source projection.

## 2. Flat connections give twisted cochains, not deleted harmonics

Flatness implies that the unitary translations tau_i commute, as do their
adjoints. Expanding squares gives exactly

    c_U d_U=0,
    ||c_U A||^2+||d_U* A||^2
       =sum_(i,j) ||nabla_i A_j||^2.                        (5)

Here c_U is the covariant curl in the chosen left trivialization; it is
the first plaquette variation at U. A Wilson character with quadratic
coefficient b_rep therefore has Hessian b_rep c_U* c_U at U, with the
same action normalization as in the input. Equation (5) retains every
original-link term. It does not replace the plaquettes by independent faces.

On the universal cubic cover choose g(x) to be background transport from
the origin to x. Path independence follows by elementary square moves
and backtracking, since the cubical cover is simply connected and U is
flat. Thus g(x+e_i)=g(x)U_i(x). The transformed links are identity and
the transformed variation is a(x)=Ad(g(x))A(x). For the based winding
holonomies H_j,

    g(x+n e_j)=H_j g(x),
    a(x+n e_j)=Theta_j a(x),       Theta_j=Ad(H_j).           (6)

The H_j commute because they represent the three generators of pi_1(T^3).
The orthogonal maps Theta_j commute even if a common group torus has not
been selected. This trivialization preserves the norm on a fundamental
cell and turns (5) into the ordinary difference identity on twisted
sections. It is used separately at each U; no derivative of a diagonalizing
frame is taken.

In this frame every anchored path has identity background transport.
Differentiating its actual word gives the same three maps as the input,
now acting on sections with boundary condition (6):

    T=R-d_c Phi,
    R d=d_c B,                Phi d=B-E,
    T d=d_c E.                                           (7)

Here R averages the length-L straight path sums, Phi averages the anchor
path sums, B averages site fields in a box, and E restricts them to
coarse vertices. The coarse sections have the same twists Theta_j over
m coarse steps. Reverse traversals carry their transported minus signs.
Thus for b in ker d_c*,

    T* b=R* b,              d* R* b=B* d_c* b=0.           (8)

This proves the physical cochain statement at the actual flat background.
It would not follow by using an untwisted source while changing the curl.

## 3. Shifted Fourier grids preserve the full source bound

Complexify the real color space. Simultaneous unitary diagonalization of
the commuting Theta_j gives common characters exp(i theta_j). Within each
character the fine and coarse momenta are

    k_j=(2pi l_j+theta_j)/n,
    K_j=(2pi s_j+theta_j)/m,
    k=(K+2pi r)/L modulo 2pi,       r in {0,...,L-1}^3.    (9)

Choose K in [-pi,pi]^3; boundary ties only relabel aliases. Put

    d_i(k)=exp(i k_i)-1,       D_i(K)=exp(i K_i)-1,
    a_i(k_i)=L^(-1) sum_(s=0)^(L-1) exp(i s k_i),
    r_i(k)=L^(-1/2) product_j a_j(k_j) a_i(k_i).

The exact symbol of R is diag(r_i(k)), summed over aliases. Its identity

    a_i(k_i)d_i(k)=D_i(K)/L                               (10)

retains the phases and proves (8) character by character. At the principal
alias k0=K/L, all |a_i(k0_i)|>=2/pi. For any principal transverse A0, set

    b_i=A0_i/conjugate(r_i(k0)).                          (11)

Equation (10) proves D* b=0. Thus R* b matches A0 exactly, and T* is
injective on the coarse transverse space. When K=0 this statement has
three components; it never divides by |D| or deletes those components.

For completeness the estimate being transferred is pointwise in K, not
an assertion about the old grid. Set b_j(r_j)=|a_j(k_j)|^2 and b_j0=b_j(0).
Finite Fourier orthogonality and the variance of two independent uniform
integers in {0,...,L-1} give

    sum_(r_j) b_j(r_j)=1,
    1-b_j0 <= K_j^2/12.

The squared high-alias tail of (11), in component i, divided by |A0_i|^2,
is

    [sum_(r_i) b_i(r_i)^2]/[b_i0^2 product_(j!=i)b_j0]-1
       <= (pi/2)^8 |K|^2/6.

Since |K|^2<=pi^2 L^2 q(k0)/4, q(k)=sum_i |d_i(k)|^2,

    ||s_high||^2 <= pi^10 L^2/6144 . q(k0)||A0||^2.       (12)

Every high alias has q(k)>=4/L^2. For general transverse A choose s by
(11), matching its principal part. Then

    dist(A,S_U)^2 <= ||A_high-s_high||^2
      <=2||A_high||^2+2||s_high||^2
      <=pi^10 L^2/3072 . <A,K_U A>.                     (13)

The argument holds at every real K and so applies to every shifted grid
(9), uniformly in its twists and sample count. Summing characters, then
restricting the real structure, proves (1). The weaker rational constant
uses pi<22/7 and 22^10<33*3072*7^10, as in the input.

For a nontrivial character none of its momenta is zero. Each momentum
has two transverse directions. Each trivial character instead contributes
one zero momentum with three transverse directions. There are D_U trivial
characters. This proves (2) by injectivity in (11). Moreover every zero
mode is exactly a principal zero mode, so (11) also proves ker K_U subset
S_U without assuming a fixed value of D_U.

## 4. Smooth redundant sources with a uniform inverse

Here use all coarse cotangents, rather than ker d_c*. There is a direct
local right inverse with an explicit constant. For each coarse output
(v,i), let E_(v,i) be its L^2 fine boundary edges with basepoint
x in B_v and x_i=v_i+L-1, in direction i. No anchor traverses such an
edge: the anchors stay inside a box. No other coarse output uses it.
Precisely L of the straight paths of output (v,i) traverse each such
edge, one for every starting i-coordinate in the box.

At a flat background, their prefixes from v to that edge have the same
transport, by flat path independence in the two-box lift. Every full
path has the same holonomy U_c,i(v). Thus the derivative coefficient of
that edge in the left-trivialized output is exactly L^(-2) O_(v,e),
where O_(v,e) is the orthogonal adjoint transport from its tail to v.
These edge sets are disjoint over all coarse outputs. This remains true
for a single coarse box: the labeled crossing is retained, and the
prefixes just described precede that crossing on the cover.

Write T_partial for T restricted to these boundary-edge input columns.
Its Gram matrix is therefore

    T_partial T_partial* = L^2 L^(-4) I = L^(-2) I,
    T T* = T_partial T_partial* + T_internal T_internal*
         >= L^(-2) I.                                    (14)

This proves (3) for all volumes and flat backgrounds without taking a
compactness minimum or choosing Fourier eigenvectors. It supplies a local
right inverse: for prescribed coarse b, put A_e=O_(v,e)^(-1)b_(v,i) on
E_(v,i), and zero on the internal edges. Then T A=b and ||A||=L||b||.
The right inverse is an unreduced source lift; it need not satisfy Gauss.

There is a separate consistency check in Fourier variables. If T(K)*b=0,
equation (7) gives E(K)*D(K)*b=0. The restriction alias row E(K) is
L^(-3/2)(1,...,1) up to unitary phases, so D*b=0. Then T*b=R*b and the
nonzero principal block in (11) forces b=0. This independently explains
why the redundant source rank does not change at D=0.

The map U -> T_U, defined by the actual differentiated path products and
the flat coarse link right trivialization, is smooth in ambient group
coordinates. Formula (3) and inversion prove smoothness of (4) on every
smooth flat family. No smoothly chosen Cartan, Coulomb basis, character
eigenvectors or quotient chart is needed to define (4).

There are also direct uniform local derivative controls. In the matrix
Hilbert-Schmidt norm, let ell=7L-6 be the maximum path length. Unitarity,
Cauchy-Schwarz on each differentiated word, and convexity over the L^3
paths imply, for the original nonlinear matrix observation at any U,

    ||D M(U)[A]||_ell2 <= sqrt(6) ell ||A||_ell2.        (15)

Indeed each output is supported on two adjacent boxes. A fixed link
basepoint can occur in at most six outputs, and each averaged word has
at most ell occurrences of that link. The sum of weighted occurrences
is at most 6ell; the wordwise Cauchy-Schwarz contributes another ell.
Repeated traversals are counted, not canceled to improve the constant.
This also gives a genuine nonlinear neighborhood, in the representation
Hilbert-Schmidt metric. Fix a flat U0, and suppose
max_e ||U_e-U0_e||_op<=delta. Identify input tangent vectors by the same
left Lie coordinates. Telescoping the unitary factors of each word shows
that each term in its differentiated word changes by at most
ell delta ||A_e||_HS. The same incidence estimate proves

    ||D M(U)-D M(U0)||_(ell2->ell2)
       <=sqrt(6) ell^2 delta.                            (15a)

Inverse traversals satisfy the identical bound because
||U_e^(-1)-U0_e^(-1)||_op=||U_e-U0_e||_op. Products with an inserted
Lie variation contain at most ell background factors, including repeated
occurrences; thus no factor is omitted in the telescope.

Let Pi0_i(Y)=proj_Lie(Y U0_c,i^(-1)), an orthogonal map of norm one, and
define the fixed-background coarse coordinate Z0(U)=Pi0 M(U). Its
derivative at U0 is T_U0. By (3) and (15a),

    ||D Z0(U)* b|| >= [1/L-sqrt(6)ell^2 delta] ||b||.

Consequently for delta<=1/[2sqrt(6)L ell^2],

    D Z0(U) D Z0(U)* >= (4L^2)^(-1) I.                  (15b)

This neighborhood is measured linkwise, not in a product ball whose
per-link radius shrinks with volume. It allows nonflat configurations.
Z0 is an auxiliary chart of the actual observation, jointly covariant
under transforming U and the reference U0. It is not the entire matrix
observation algebra, nor a globally gauge-fixed physical coordinate.
The original M and its exact endpoint gauge action remain the retained
objects. No estimate on a quantum conditional ground state, its measure,
or the probability of this neighborhood is inferred from (15b).

Finally S_U subset ran T_U*. Thus on C_U the same fast inequality remains
valid with the smaller distance to ran T_U*:

    <A,K_U A> >= (33 L^2)^(-1) ||(I-Ptilde_U)A||^2.     (16)

Ptilde_U need not preserve C_U. Equations (4) and (16) are ambient tools
for keeping smooth redundant observations; they are not an orthogonal
physical Schur projection. The coarse gauge action must still be imposed
exactly on the retained nonlinear algebra.

## 5. The physical projection has an unavoidable rank jump

Take G=SU(2), with T_a=-i sigma_a/2, and the periodic constant-link family

    U_1(t)=exp(t T_3/n),     U_2(t)=U_3(t)=I,
    0<=t<2pi.

Its winding holonomies are exp(t T_3), I, I. For 0<t<2pi their invariant
Lie space is span(T_3), so D_U=1. At t=0 it has dimension 3. Therefore

    rank P_t=6m^3+1 (t>0),      rank P_0=6m^3+3.        (17)

There is an explicit fixed real witness. Let A have the constant unit
color T_1 in direction 1 and zero in the other directions, normalized
over the n^3 links. At t=0 it is a retained harmonic mode, so P_0 A=A.
For t>0, Ad(U_1(t))-I is invertible on span(T_1,T_2). Choose a constant
site field xi_t in that plane with

    (Ad(U_1(t))-I)xi_t=A_1.

Then A=d_U xi_t. Since S_t subset ker d_U*, P_t A=0. It follows that

    ||P_t-P_0||=1,             0<t<2pi.                 (18)

The upper bound is the standard elementary norm bound for a difference
of orthogonal projections; the displayed unit vector gives equality.
The T_2 direction gives a second independent witness. Their gauge
parameters diverge as t tends to zero, consistently with the increasing
stabilizer. No physical fast-gap counterexample is produced: A is a gauge
direction for t>0 and a physical harmonic direction at t=0.

Consequently there is no differentiable global fixed-rank Coulomb source
bundle having fibers S_U across this family. Any proposed moving-source
calculation that differentiates P_U there must be replaced. Equations
(3)-(4) provide a repair at the observation level using the same actual
block M, with coarse gauge redundancy retained. No additional arbitrary
physical observable or deletion of a harmonic direction is necessary for
this geometric repair. Establishing interacting estimates in that
redundant formulation remains a substantive task.

## 6. What this changes for the interacting comparison

The compact-holonomy proposal passes its first spectral test: the actual
path map retains all covariantly slow modes over every flat background,
with the same full spatial fast constant. Its physical source projection
fails the smooth fixed-rank premise. The exact same matrix observation
has a smooth, uniformly invertible redundant tangent realization, so that
failure has a concrete geometric repair rather than a discarded mode.
The right inverse has norm L, and (15b) extends the observation submersion
to a linkwise nonflat neighborhood with explicit volume-independent radius.
This is a nonlinear source-geometric estimate, not just a Gaussian identity.

At a reducible background, harmonic infinitesimal vectors need not
integrate to a family of flat connections. In particular the noncommuting
slow variables can acquire quartic magnetic energy. None of these
quadratically zero directions has been discarded or assumed to commute;
their interacting compact quantum dynamics remains to be controlled.

The next analytic question is now posed on the original compact link
configuration space with its exact Gauss action and actual observation M.
It is to control the interacting true-vacuum source isometry and full
complementary energy form there, using (1) locally in flat backgrounds and
the smooth ambient source map instead of derivatives of P_U. Nonflat
fluctuations, compact slow quantum dynamics, vacuum subtraction, induced
metric, direct energy and exchange, and the full retained energy tails
must occur in the same comparison. Flat-background coercivity alone does
not provide their localization or uniform remainder.

In particular this theorem does not replace a quantum marginal by a Haar
or Wilson Gibbs marginal, identify a configuration complement with an
OS-history complement, remove generated temporal memory, or yield a
continuum vacuum by taking a Gaussian regulator to zero. The full Wilson
scale-comparison route and G19 remain open.

## 7. Reproduction and verification boundary

The accompanying [run](../../runs/flat_holonomy_sources_2026-09-07/README.md)
checks the twisted cochain squares and actual path-word derivatives,
finite noncentral SU(2) adjoint backgrounds, the full finite source
inequality, complete physical ranks, the fixed-rank redundant source,
and the projection-jump witness using exact arithmetic. Negative controls
drop a transport phase or freeze the identity source and must fail.
The run also records the source scope and proof review.

The all-volume, all-flat-background statements and smooth-family argument
above have analytic evidence. Finite controls do not formalize those
quantifiers, prove a nonlinear quantum remainder or promote this result
to a Lean theorem.
