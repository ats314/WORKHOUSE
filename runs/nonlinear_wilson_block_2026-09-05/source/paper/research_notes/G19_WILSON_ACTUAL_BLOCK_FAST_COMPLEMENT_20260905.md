# Actual two-square fiber-ground complement above the true vacuum

5 September 2026. Analytic theorem for one adjacent two-square
Wilson block, with all seven original electric links retained, at each fixed
SU(N), N>=2. Earlier frozen source bytes are unchanged.

The conclusion concerns the bottom of the actual full Hamiltonian compressed
to the orthogonal complement of its exact conditional fiber-ground bundle,
after subtracting the **true full-block vacuum energy**. This is distinct from
the gap of a pointwise constrained rotor.

## 1. Actual operator, projection and theorem

Use the physical Haar Hilbert space

```text
H_phys=L2(SU(N)^2,dU1 dU2)^(simultaneous conjugation),
H(u)=-(1/2)[3 Delta_1+3 Delta_2+sum_a(L_1,a-R_2,a)^2]
       +2u[v(U1)+v(U2)],     v(U)=N-ReTr U.             (1)
```

The inner product on the Lie algebra is `-2 ReTr(XY)`. This is the same
nonnegative scalar convention as the established full two-square theorem.
Write `E_j(u)` for its ordered physical eigenvalues and
`E_vac(u)=E_0(u)` for its true full-block ground energy.

The global change of variables is `U=U1U2`, `K0=U1`, with measure `dU dK0`.
The actual vertical operator on each Haar fiber is

```text
A_U=-(1/2) sum_ab S(U)_ab D_a D_b
       +2u[v(K0)+v(K0^(-1)U)],
S(U)=15[8I-Ad(U)-Ad(U)*]^(-1).                          (2)
```

For each finite u and U it has a unique positive normalized ground
`varphi_(u,U)(K0)`. Define the exact decomposable orthogonal projections

```text
(P_u f)(U,K0)=varphi_(u,U)(K0)
          int conjugate(varphi_(u,U)(K)) f(U,K) dK,
Q_u=I-P_u.                                             (3)
```

They preserve the physical invariant subspace. Let `F_u` be the self-adjoint
operator associated with the closed form

```text
f_u[psi]=q_H(u)[psi]-E_vac(u)||psi||^2,
D(f_u)=H1(SU(N)^2) cap H_phys cap ran(Q_u).             (4)
```

Then

```text
inf spectrum(F_u)
 =(sqrt(3)+sqrt(5)) sqrt(u)+o_N(sqrt(u)).                (5)
```

Thus for each `epsilon>0`, at a sufficiently large fixed-rank threshold,

```text
Q_u(H(u)-E_vac(u))Q_u
 >=[sqrt(3)+sqrt(5)-epsilon]sqrt(u) I_(ran Q_u)          (6)
```

in the restricted-form sense. The left side is notation for (4), not an
unproved operator-domain product. The statement is a coercivity threshold
above the full vacuum; it is not the spacing between the first two eigenvalues
of the compressed operator F itself.

The established physical spectrum is essential. In the unrestricted two-mode
oscillator, the fast adjoint alone has excitation sqrt(5). Physical diagonal
Gauss excludes that vector; the first allowed complement vector is a mixed
slow-adjoint/fast-adjoint singlet. Its energy is sqrt(3)+sqrt(5), which is
smaller than the purely fast class excitation 2sqrt(5).

## 2. Established inputs and the form domain

The source
[full two-square physical proof](G19_WILSON_TWO_SQUARE_PHYSICAL_SHELLS_20260905.md),
sections 1–5, proves the actual low eigenvalue asymptotics and normalized
low-eigenvector harmonic convergence. Put `g=u^(-1/4)` and `d=N^2-1`. In the
balanced coordinates

```text
U=exp(sqrt(2)g q),
H=U^(1/2),  K0=H F,  F=exp(g z/sqrt(2)),
```

the limiting oscillator is

```text
H_osc=-(3/2)Delta_q-(5/2)Delta_z+(|q|^2+|z|^2)/2,
e_*=(d/2)[sqrt(3)+sqrt(5)].                            (7)
```

Its physical lowest vectors are

```text
Phi_q(q)Phi_z(z),
(|q|^2-d sqrt(3)/2)Phi_q(q)Phi_z(z),
(q.z)Phi_q(q)Phi_z(z),                                 (8)

Phi_q proportional to exp(-|q|^2/(2sqrt(3))),
Phi_z proportional to exp(-|z|^2/(2sqrt(5))).
```

The first two actual eigenvectors converge to the first two vectors in (8)
after local Haar normalization and rescaling. The corresponding eigenvalues
and the next physical one satisfy

```text
g^2 E0 ->e_*,
g^2 E1 ->e_*+2sqrt(3),
g^2 E2 ->e_*+sqrt(3)+sqrt(5).                           (9)
```

Passing from product logarithms in that theorem to balanced coordinates does
not add an assumption. Their rescaled change of variables tends on every
fixed compact set, with its derivatives and Haar Jacobian, to the linear
coarse/fine transformation in (7). The established potential tightness
controls the outside portion. Consequently the stated L2 limits are the same
in either local coordinate system.

For every fixed finite u, the global unbalanced family (2) is smooth on the
compact coarse group, uniformly elliptic in K0 and has common fiber operator
domain H2. Positivity improving ellipticity on the connected compact fiber
makes its ground simple; the positive normalized eigenvector depends smoothly
on U. These assertions are for each finite u; no u-uniform global conditional
gap or global derivative estimate is used.

The smooth kernel in (3), compactness and differentiation under the fiber
integral imply that P_u and Q_u preserve H1, with a finite bound that may
depend on u. They also map smooth functions to smooth functions. The ground
family is gauge covariant by uniqueness and positivity, so averaging over
the compact gauge group commutes with P_u and Q_u. Applying Q_u to a smooth
invariant approximation proves density of the domain (4) in `ran Q_u cap
H_phys`. Restriction of the closed full form to this closed Hilbert subspace
is closed, and its form domain embeds compactly into L2. Thus F_u is a
well-defined self-adjoint compact-resolvent compression.

Although P_u varies with u, the ambient H1 form domain of the full operator
is fixed. No assertion that the varying constrained subspaces have a common
u-independent operator domain is needed.

## 3. Projection convergence on the actual two low physical eigenvectors

The new input
[actual ground-bundle theorem](G19_WILSON_GROUND_BUNDLE_RELATIVE_FORM_20260905.md)
proves on a fixed principal-root neighborhood, in balanced Haar fiber space,

```text
Omega_(u,U)(F)=varphi_(u,U)(H F),
||Omega_(u,U)-Omega_(u,I)||<=C dist(U,I)^2,
||d_U Omega_(u,U)||<=C dist(U,I).                       (10)
```

The central rotor theorem in
[compact fiber theorem](G19_WILSON_PHYSICAL_FIBER_FAST_GAP_20260905.md), with its localization proof,
implies that the rescaled normalized central fiber ground tends in L2 to
Phi_z. In particular it is the same fiber vacuum as in (7),(8).
Explicitly, its potential gives tightness on the rescaled fiber, local
ellipticity gives compactness, and the converging ground energy forces every
limit to be the oscillator ground. Positivity fixes its phase and uniqueness
identifies the limit. Thus this ground-vector consequence uses the same
variational proof, rather than an assumed perturbation expansion.

Here is why these facts suffice without imposing a fiberwise constraint on a
cutoff eigenfunction. Let `psi_j(u)`, j=0,1, be the normalized actual low
physical eigenvectors. Their coarse mass is tight near U=I. Indeed the exact
unitary inequality `v(U1U2)<=2[v(U1)+v(U2)]` and positivity give

```text
H(u)>=u v(U),
int_(dist(U,I)>r) |psi_j|^2 <= C g^2/r^2               (11)
```

for small fixed r, using `E_j=O(g^-2)`. The same estimate follows from the
full localization argument and does not refer to a global fiber gap.

On `dist(U,I)<=r`, replace the fiber line Omega_(u,U) by the constant
balanced line Omega_(u,I). The operator norm difference of the rank-one
projections is at most `2||Omega_(u,U)-Omega_(u,I)||<=C r^2`. The outside
part costs at most its L2 norm, because both projections are contractions
and commute with coarse cutoffs. Next rescale the central line and the low
eigenvector. The former converges to Phi_z and the latter to
`f_j(q)Phi_z(z)`. Boundedness of the projection and L2 convergence therefore
show that its complementary component tends to zero.

One can perform this last step first on fixed compact rescaled q,z sets and
then let those sets grow. The harmonic localization proof gives the required
L2 tails for both the full eigenvector and central rotor ground. No uniform
bound on the projections across the cut locus is invoked. Taking g to zero,
then r to zero, proves

```text
||Q_u psi_0(u)|| ->0,     ||Q_u psi_1(u)|| ->0.
```

Let `E_<(u)` be the orthogonal projection onto these two simple eigenspaces.
Their rank is two for all sufficiently large u, by the established isolated
physical shells. Hence

```text
epsilon_u=||Q_u E_<(u)|| ->0.                           (12)
```

This is the required projection convergence on the only actual spectral
space lying below the mixed shell. It does not assert norm convergence of
P_u on the entire infinite-dimensional Hilbert space.

## 4. Lower bound from the complete full physical spectrum

The exact spectral theorem for H(u) on H_phys gives

```text
H(u)>=E2(u) I-[E2(u)-E0(u)]E_<(u).                     (13)
```

It remains valid on the complete form domain; all higher physical energies
are at least E2, and the two lower energies are at least E0. For a normalized
`psi in ran Q_u`,

```text
||E_< psi||<=||E_< Q_u||=epsilon_u.
```

Subtracting the true E0 in (13) therefore gives the explicit surviving bound

```text
f_u[psi]>=[E2(u)-E0(u)](1-epsilon_u^2).                 (14)
```

Combining (9),(12),(14) proves the lower limit in (5). This argument cannot
lose an unobserved state below the mixed shell: E_< is the complete full
physical spectral projection below it, rather than a selected source span.
No energy-form estimate for P_u applied to arbitrary eigenvectors is required
for this lower bound.

## 5. A genuinely constrained upper trial with controlled projection cost

For the matching upper bound, merely projecting the actual mixed eigenvector
using L2 convergence would be insufficient: a small-norm removed component
might have large kinetic energy. The following trial controls that cost.

Let `rho_c,g(q)dq` and `rho_f,g(z)dz` be the exact Haar measures in the coarse
and fiber exponential charts above, including scale and Haar constants.
Choose smooth Ad-invariant even cutoffs in fixed unscaled logarithm balls.
They equal one near the identity and have support inside the fixed charts.
Define, with zero extension beyond those charts,

```text
a_g,b(U)=rho_c,g(q)^(-1/2) chi_c(U) q_b Phi_q(q),
theta_g,b(F)=rho_f,g(z)^(-1/2) chi_f(F) z_b Phi_z(z),
v_g(U,F)=sum_(b=1)^d a_g,b(U) theta_g,b(F).             (15)
```

These are smooth functions. Each vector family is Ad equivariant; their
contraction is physically invariant. The fiber vector theta is exactly odd
under F inversion: log(F^-1)=-log(F), the cutoff and Gaussian are even, and
the exponential Haar density satisfies `rho_f,g(-z)=rho_f,g(z)`.

The central operator at U=I is `-(5/4)Delta+4u v(F)`, invariant under F
inversion. Uniqueness and positivity make its ground Omega_(u,I) exactly
inversion even. Thus, on the full compact fiber and for every g,

```text
<Omega_(u,I),theta_g,b>=0.                              (16)
```

The cutoff mixed Gaussian has nonzero limiting norm and the correct limiting
full energy:

```text
||v_g||^2 -> d sqrt(15)/4 >0,
g^2 q_H(u)[v_g]/||v_g||^2
 -> e_*+sqrt(3)+sqrt(5).                               (17)
```

This follows by the exact local metric/potential expansion, Haar flattening
and Gaussian domination. Derivatives of the fixed unscaled cutoffs have
exponentially small rescaled tails. Only leading form convergence is needed;
no unproved adiabatic substitution or all-orders asymptotic expansion is used.

Write `P_u v_g=h_g(U)Omega_(u,U)(F)` on its coarse support. Equation (16) and
(10) give, uniformly with `X=log U`,

```text
m_g,b(U)=<Omega_(u,U),theta_g,b>,
|m_g,b(U)|<=C |X|^2,       |d_U m_g,b(U)|<=C |X|,
h_g=sum_b a_g,b m_g,b.                                 (18)
```

Here theta is U independent and has bounded L2 norm, so no derivative of a
moving fiber density or Gaussian is omitted. Elementary Gaussian moments
in (15) yield

```text
||h_g||^2=O(g^4),
q_c[h_g]=O(g^2),
int V_c(U)|h_g(U)|^2 dU=O(g^2).                        (19)
```

For the derivative estimate, the two terms are bounded by the integrals of
`|X|^4 sum_b|grad a_g,b|^2` and `|X|^2 sum_b|a_g,b|^2`; each is O(g^2).
For the potential estimate, `V_c<=C g^-4 |X|^2`, and the needed sixth
Gaussian moment is O(g^6). Coarse Haar and metric coefficients and their
local derivatives are uniformly bounded after their explicit scale factors;
cutoff derivative terms are again exponentially small.

The exact projected-form identity already proved in the ground-bundle note is

```text
q_H(u)[h_g Omega]=q_c[h_g]
       +int[V_c+e(U)+Phi_BH(U)]|h_g|^2 dU.
```

On this fixed neighborhood `e(U)<=C g^-2` and
`Phi_BH(U)<=C g^-2 |X|^2`. Together with (19), this gives the decisive
unscaled estimate

```text
||P_u v_g||=O(g^2),       q_H(u)[P_u v_g]=O(g^2).       (20)
```

It accounts for the whole fiber tail of P_u v_g through the exact projection
identity; P_u need not preserve the compact fiber support of the trial.

Set `w_g=Q_u v_g`. It is an exactly constrained, smooth physical form-domain
vector. Since the full unshifted form q_H is nonnegative, its form
Cauchy–Schwarz inequality gives

```text
|q_H[w_g]-q_H[v_g]|
 <=q_H[P_u v_g]+2 sqrt(q_H[v_g]q_H[P_u v_g])=O(1).
```

Also `||w_g||^2=||v_g||^2-||P_u v_g||^2`, with a positive limiting value.
Equations (9),(17),(20) therefore prove

```text
limsup_(u->infinity) inf spectrum(F_u)/sqrt(u)
 <=sqrt(3)+sqrt(5).                                    (21)
```

Together with (14), this proves (5). The o(sqrt(u)) remainder is sufficient
for a genuine positive fast form bound. A sharper rate would require a
quantitative version of the low-spectral projection convergence in section 3;
none is assumed here.

## 6. The actual block realizes the closed-form Schur factorization

For each fixed sufficiently large u, the complementary floor just proved
also permits an actual Schur realization with the infinite-dimensional
retained fiber-ground space. This corollary does not claim bounds uniform
in u or in the number of blocks for the resulting lift.

Write `h=q_H-E_vac||.||^2>=0`. Identify `ran P_u cap H_phys` with
`L2(G)^Ad` through the global Haar isometry

```text
J phi(U,K0)=phi(U)varphi_(u,U)(K0).
```

For this fixed u the full positive ground family and its first two
derivatives are smooth and bounded on the compact global group product.
Their bounds need not have the near-identity asymptotic size of (10).
The exact full horizontal form uses the global fields

```text
D_a=E_a^U+D_(b(U)T_a)^K0,
b(U)=(4I-Ad(U)*)[8I-Ad(U)-Ad(U)*]^(-1),
C_uu(U)=8I-Ad(U)-Ad(U)*.                               (22)
```

Here the coarse E_a are Haar-skew and the fiber translation has zero Haar
divergence. All coefficients are smooth and bounded globally. For smooth
physical `q in ran Q_u`, fiber orthogonality implies, pointwise in U,

```text
<varphi,q>_fiber=0,
<varphi,D_b q>_fiber=-<D_b varphi,q>_fiber.             (23)
```

The vertical cross form vanishes because `A_U varphi=E_0^fiber(U)varphi`.
The scalar full-vacuum subtraction also has zero cross inner product.
Thus the only cross contribution is

```text
h[J phi,q]=(1/2) int sum_ab C_ab [
  conjugate(E_a phi)<varphi,D_b q>
   +conjugate(phi)<D_a varphi,D_b q>] dU.               (24)
```

Use (23) in the first term and integrate E_a by parts on coarse Haar once.
The result has no derivative of phi: its coefficients multiply q or one
coarse/fiber derivative of q, with first/second derivatives of varphi and
first derivatives of C. Fixed-u smoothness and fiber Cauchy–Schwarz give

```text
|h[J phi,q]|<=C(u)||phi||_(L2(U)) ||q||_(H1(G^2)).      (25)
```

This is the useful cancellation of the apparently second-coarse-order
cross block. It is an identity of the actual metric form, not an assumed
small coupling. Density extends (25) to the constrained form domain.

Let f>0 be any valid lower bound for F_u from (6). Full ellipticity and
nonnegativity of the magnetic potential give

```text
||q||^2<=f^(-1) h[q],
||grad q||^2<=C[q_H[q]]
            =C[h[q]+E_vac||q||^2]<=C(u)h[q].           (26)
```

Conversely `h[q]<=C(u)||q||H1^2`. The F_u form norm is therefore equivalent
to H1 on the constrained domain. Riesz representation in that form Hilbert
space supplies a unique lift

```text
U_u:ran P_u ->D(F_u^(1/2)) subset ran Q_u,
f_u[U_u p,q]=h[p,q],
||F_u^(1/2)U_u p||<=C(u)||p||.                         (27)
```

The cross form in (27) is the bounded extension (25) if p is only in L2.
In particular U_u is bounded as an L2-to-L2 map, and by (26) also as an
L2-to-H1 map. Set `B_u=F_u^(1/2)U_u`, a bounded operator on the retained
Hilbert space with values in the complementary Hilbert space.

The retained form `h_PP[p]=h[p]` has domain `J H1(G)^Ad`. This follows both
from the global version of the exact projected-form identity and from the
H1 boundedness of P_u. It is a closed semibounded coarse elliptic form.
Define

```text
k0[p]=h_PP[p]-||B_u p||^2.                             (28)
```

The subtraction is bounded in the retained L2 norm, so k0 is closed with
the same form domain. It is nonnegative: for a retained form vector p,
`q=-U_u p` lies in the complementary form domain, and the defining Riesz
identity gives `k0[p]=h[p-U_u p]>=0`.

Completing the square gives the exact actual factorization

```text
h[p+q]=k0[p]+||F_u^(1/2)(q+U_u p)||^2.                 (29)
```

Its domain is exactly the triangular pullback

```text
p in D(k0),            q+U_u p in D(F_u^(1/2)).
```

Indeed P_u,Q_u preserve the original H1 form domain, and U_u maps every
retained L2 vector into complementary H1. Thus this condition is equivalent
to the original split H1 domain; neither an unbounded cross operator nor
an unverified operator-domain product has been inserted.

Consequently the established
[closed-form Schur theorem](G19_FORM_SCHUR_SCALE_COMPARISON_20260905.md) applies to this actual block
with `M_u=I+U_u*U_u` and the normalized retained operator
`L_u=M_u^(-1/2)K0_u M_u^(-1/2)`. Its form domain is the appropriate bounded
pullback of D(k0); preservation of coarse H1 by M_u^(-1/2) need not be
assumed. Compactness of the coarse H1 embedding implies compact resolvent
for K0_u and L_u. The true full vacuum is unique, so the exact kernel
correspondence gives a one-dimensional kernel for L_u as well.

For the positive min-max energies in the scope of that theorem, one has

```text
f mu_j/(f+mu_j)<=lambda_j<=mu_j,                        (30)
```

where lambda_j belong to the actual full vacuum-subtracted H and mu_j to
L_u. Its whole-window graph-source conclusion also applies below energy f.
Explicitly, for `Pi=1_[0,E](H-E_vac)` with `E<f`, the actual graph isometry
`J_graph a=(p,-U_u p)`, `p=M_u^(-1/2)a`, satisfies
`Pi J_graph J_graph* Pi >=[1-(E/f)^2]Pi`, so `Pi J_graph` is onto that entire
physical low window. This is the established graph-source theorem applied
to (29), not an identification of a prescribed Wilson observable family.
This realizes the closed-form hypotheses for one actual nonlinear Wilson
block with an infinite-dimensional retained space. It does not identify L_u
with a proposed bare coarse Wilson Hamiltonian, its graph source with literal
Wilson sources, or its projection with an OS-history range. No u-uniform or
many-block bound for U_u or B_u is supplied by this fixed-u construction.

## 7. What this closes and what it does not

This supplies an **actual vacuum-subtracted fast-compression floor for one
full physical Wilson block**, with the exact conditional quantum ground
bundle as retained space. It addresses the F-block premise of the earlier
closed-form Schur scale theorem at a fixed finite-block level, and improves
on an estimate for a pointwise constrained rotor with its own ground removed.
The mixed physical channel is the true first complement channel.

No reducing-subspace property of P_u or Q_u is assumed or concluded. The
full vacuum generally has a small Q_u component even though that component
tends to zero in this fixed-block limit. The positive lower bound on the
compressed form is consistent with that fact: a component of a zero-energy
vector need not itself have zero energy when the decomposition does not
reduce the operator.

The theorem has no volume-uniformity claim. Tensoring approximate retained
vacuum lines can make their joint overlap with the actual vacuum decay with
the number of blocks; the earlier product-vacuum mismatch example prohibits
deducing a uniform many-block floor from (5) alone. Shared-boundary kinetic
and magnetic interactions, uniform estimates and Wilson identification for
the actual normalized coarse Schur operator and its lift, vacuum-adapted
transport across blocks, and the OS-history map remain separate obligations.
No continuum mass or all-scale recursion follows merely from this one-block
result.

In the project's physical units `H_physical=c_H(a) g_H^2 H/a` with
`u=g_H^-4`, (5) is a fast compression threshold
`[sqrt(3)+sqrt(5)+o(1)]c_H(a)/a`. It supplies a local ultraviolet energy
scale; it is not itself a finite continuum glueball mass.

## 8. Reproducible finite mechanism controls

[check_actual_complement_mechanism.py](../../runs/nonlinear_wilson_block_2026-09-05/check_actual_complement_mechanism.py),
with [saved exact output](../../runs/nonlinear_wilson_block_2026-09-05/check_actual_complement_mechanism.json), checks a
rational four-state example of (14) with equality, including a nonzero
component of the true vacuum in Q. Its projected trial has the same
`O(g^2)` norm and unscaled energy bounds used in (20). It separately verifies
the mixed physical harmonic polynomial, its inversion parity, and its exact
excitation sqrt(3)+sqrt(5). These finite algebra checks do not certify the
actual Wilson projection limit or the general infinite-dimensional form
argument; those conclusions follow from sections 2–6 and the pinned analytic
inputs under the stated fixed-block hypotheses.

The [nonlinear block run](../../runs/nonlinear_wilson_block_2026-09-05/README.md) preserves the original proof,
independent review, finite controls and native replay with their exact scopes.
