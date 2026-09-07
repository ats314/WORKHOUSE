# The actual fast Green identity and a local Wilson harmonic obstruction

6 September 2026. Independent analytic derivation. The scope is the
actual regulated Gaussian tangent Hamiltonian and its literal path-source
projection. No nonlinear interacting remainder or continuum claim is made.

## 1. Inputs and the exact inverse being considered

The canonical `G19_CONDITIONAL_QUANTUM_PATH_COVARIANCE_20260906.md`
and `G19_GAUSSIAN_PATH_ENDPOINT_BASELINE_20260906.md` fix the physical
transverse space E, the actual path cotangents W, and

    Omega=(v^2 d1*d1+rho^2)^(1/2), rho>0,
    R=ran(Omega^(-1/2) W), P=Gamma(P_R), Q=I-P,
    H0=dGamma(Omega), F=Q H0 Q|ran Q.

Here v^2=2 b_rep u; coordinate vacuum covariance is Omega^(-1)/2.
For L=2 the established complete fast floor is F>=v/(2 sqrt(33)).
W includes all three harmonic directions. Positive rho gives an actual
Gaussian vacuum; rho=0 on a finite torus does not.

The conditional Gaussian precision on ker W* is a different operator
from F. In particular, its Ornstein--Uhlenbeck inverse cannot be substituted
for the inverse in this note.

## 2. Independent n-leg shorting calculation

Work first on an ordered n-fold tensor, n>=1, with color included as an
identity factor. Set

    D_n=sum_j Omega_j, L_n=tensor_j Omega_j^(-1/2),
    U_n=tensor_j W, B_n=L_n U_n,
    P_n=projection onto ran B_n, Q_n=I-P_n.

For a positive finite matrix D and an injective B, the embedded inverse
of its complementary compression is

    Q(Q D Q|ran Q)^(-1)Q
      =D^(-1)-D^(-1)B(B*D^(-1)B)^(-1)B*D^(-1).       (1)

Indeed the right-hand side is self-adjoint, annihilates B, and its product
on the left by QD is Q. These properties characterize the inverse on
ran Q. Formula (1) does not assume that D commutes with P.

L_n commutes with D_n. Applying (1) with B_n=L_n U_n and sandwiching
by L_n therefore gives exactly

    L_n Q_n(Q_n D_n Q_n|ran Q_n)^(-1)Q_n L_n
       =A_n-A_n U_n(U_n* A_n U_n)^(-1)U_n* A_n,
    A_n=(tensor_j Omega_j^(-1))/(sum_j Omega_j).       (2)

The permutations commute with all these maps. Restriction to symmetric
tensors gives the actual nth bosonic Wick sector, with U_n restricted to
the corresponding symmetric source tensor. Restriction to a compact
group's invariant subspace is valid because every map is equivariant.
For Lie cubics the invariant alternating color tensor selects the spatial
exterior-three representation; the same argument applies there. A zero
source space means that the subtracted term is zero.

Equation (2) uses the energy prior A_n. The equal-time prior is
tensor Omega^(-1), which lacks the sum-frequency denominator. Already
n=1 gives A_1=Omega^(-2). Neither tensorizing an all-fast one-particle
inverse nor replacing F by a conditional-fiber generator gives (2).
Physical coordinate creation contributes an additional factor 2^(-n/2),
with the usual symmetric-tensor normalization. Section 4 below computes
those factors directly, without relying on a tensor convention.

## 3. Three actual spatial modes and the ordered plaquette

Take the periodic positive-edge cubic lattice with even side n>=4,
L=2, and V=n^3 vertices. Define real, counting-norm-unit spatial modes

    r_x(x,i)=delta_(i,1)/sqrt(V),
    r_y(x,i)=delta_(i,2)/sqrt(V),
    f_y(x,i)=(-1)^(x_1) delta_(i,2)/sqrt(V).

They are mutually orthogonal and transverse. Their curl eigenvalues are
0,0,4 respectively. Both r_x and r_y lie in ran W. The actual path
average annihilates f_y: the average over the two starting x_1 values
cancels. Equivalently its alias k=(pi,0,0) has a_1(pi)=0, while the coarse
momentum is K=0. Thus r_x,r_y belong to R and f_y is orthogonal to R.
Their frequencies are rho,rho and

    omega_h=sqrt(4v^2+rho^2).

This three-mode subspace reduces Omega and P_R, even though the full
path-source projection is generally nonreducing.

Let X,Y,Z be its three Lie-valued coordinate amplitudes. On the oriented
12 plaquette based at x, put s_x=(-1)^(x_1). The four signed link
logarithms in the actual ordered Wilson word are

    X/sqrt(V), (Y-s_x Z)/sqrt(V),
    -X/sqrt(V), -(Y+s_x Z)/sqrt(V).

Its first two BCH terms are exactly

    F1=-2s_x Z/sqrt(V),
    F2=([X,Y]-s_x[X,Z]-s_x[Y,Z])/V.

Invariance of the Lie inner product gives

    <F1,F2>=-2s_x <Z,[X,Y]>/V^(3/2).                 (3)

This is an actual local magnetic coefficient, not a freely chosen cubic.
For v_rep(U)=dim(rep)-ReTr(rep(U)),

    v_rep(product exp(g z_j))
      =(b_rep/2)g^2 |F1|^2+b_rep g^3 <F1,F2>+O(g^4).

The Wilson magnetic term is 2u v_rep, so its cubic coefficient is
v^2<F1,F2>. This statement concerns the original-link exponential tangent
chart restricted to the transverse slice. It does not assert that the
local magnetic piece equals the complete electric-plus-magnetic first
ground forcing in another nonlinear coordinate chart.

## 4. Exact physical Fock component and its resolvent energy

Choose a real orthonormal Lie basis with
f_abc=<T_c,[T_a,T_b]> and sum_abc f_abc^2=C_A d, where d=dim Lie(G).
The vector

    Psi=sum_abc f_abc a*(r_x,T_a) a*(r_y,T_b)
                            a*(f_y,T_c) Phi

has squared norm C_A d. It is invariant under simultaneous adjoint
rotation. The distinct spatial modes make the occupation states
orthogonal, so no factorial occurs in this norm. It lies in ran Q and
is an exact eigenvector of F with energy 2rho+omega_h.

For a unit spatial mode of frequency omega, coordinate multiplication
on the vacuum is a*/sqrt(2omega). Thus the projection of the centered
local magnetic force Q V_x^(3) Phi onto this occupation sector is

    -v^2 s_x Psi / sqrt(2 V^3 rho^2 omega_h).         (4)

Color alternation kills every internal Gaussian contraction. Equation
(4) is therefore unaffected by Wick subtraction or by conditional
centering with P. Other occupation sectors are orthogonal, and the
selected eigenvector reduces F.

Writing b_x=Q V_x^(3) Phi, the actual fast resolvent diagonal satisfies

    <b_x,F^(-1)b_x>
       >=v^4 C_A d/[2 V^3 rho^2 omega_h(2rho+omega_h)]. (5)

This is also the exact contribution of the selected sector to the
time integral of <b_x,exp(-tF)b_x>. For any fixed even torus and v>0,

    lim_(rho->0) rho^2 times the right-hand side
       =v^2 C_A d/(8 V^3)>0.                        (6)

Consequently neither sum_y |<b_x,F^(-1)b_y>| nor the stronger
integral_0^infinity sum_y |<b_x,exp(-tF)b_y>| dt admits a bound uniform
in rho on this full Gaussian vacuum family. Its diagonal alone diverges.
The complete fast spectral gap stays positive throughout. The failure
comes from the growing retained harmonic coordinate variance, not from
a hidden slow state in ran Q or a nonphysical color choice.

For SU(2) in the fundamental convention <X,Y>=-2ReTr(XY), one has
b_rep=1/2, C_A=2 and d=3. The checker verifies all these factors directly.

## 5. Spatial cancellation and the scope of the obstruction

The selected contribution to the local exchange matrix is the positive
rank-one matrix

    G_selected(x,y)=s_x s_y
       v^4 C_A d/[2 V^3 rho^2 omega_h(2rho+omega_h)].

Since sum_x s_x=0, the projection of the global sum of all parallel
plaquette cubics onto Psi is exactly zero. This is an actual spatial
cancellation. It does not rescue an absolute rooted bound on the local
matrix, whose diagonal is positive and bounded below by (5). Conversely,
the obstruction does not prove that the fully summed Wilson first
corrector has this divergence: that assertion would discard the
cancellation just computed.

Three distinct questions must therefore remain separate:

* The exact actual full-Q inverse is given by the energy-prior shorting
  formula (2), with the full source tensor removed.
* A fixed-retained-mean conditional fiber estimate may remain uniform
  for bounded retained means. It does not integrate their unrestricted
  rho-dependent Gaussian variance for free.
* Removing/fixing harmonic modes, controlling their variance by the
  actual compact nonlinear law, or retaining cancellations before
  taking absolute values may repair the intended interacting estimate.
  None is supplied merely by the positive fast floor.

After zero modes are excluded, proving spatial summability of (2) still
requires estimates for the complete n-leg shorted symbol. Equal-time
summability and a scalar gap alone do not prove that estimate. This note
makes no unproved uniform-root claim for that modified problem.

## 6. Reproducible evidence and limitations

`check_local_plaquette_fast_obstruction.py` supplies independent exact
finite controls: original path averaging and curl at n=4 and n=6;
the ordered four-link BCH coefficient and direct SU(2) matrix-character
expansion; Lie-invariant Fock normalization; a rational regulator family
and its symbolic divergent limit; and the spatial-sum cancellation.
The checker accepts `--output` at a fresh path or `--replay` of the full
report, checks source hashes, and rejects optimized Python execution.
Its finite geometry controls support the explicit all-even-n calculation
above; they do not certify a nonlinear asymptotic theorem.

The independently implemented general finite nonreducing energy-prior
controls are the parent's sibling `../check_full_fast_green.py` and
`../FULL_FAST_GREEN_CONTROLS.json`. They are separate evidence for (2).

## Repository provenance

The [sealed reproduction run](../../runs/dynamic_fast_green_2026-09-06/README.md)
preserves the original proof, exact programs and reports, independent review,
and the reconstruction record for this canonical copy. Program paths named
in the derivation refer to those preserved original inputs. The complete
analytic statement is recorded separately from its finite controls.
