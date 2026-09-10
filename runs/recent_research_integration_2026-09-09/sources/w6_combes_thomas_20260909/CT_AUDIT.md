# Combes–Thomas closure: audit and a version preserving fast energy

9 September 2026 UTC. Continuation of the proposed W6 closure.

The dual-resolvent reformulation is correct for a positive self-adjoint
fast form. The proposed Wilson closure does not follow: its local L2
residual bound is contradicted by the exact model used to motivate it,
and its identification of the coupled fast operator has not been proved.
A corrected localization theorem can retain the full energy denominator.

## 1. The valid dual identity, and the spectral parameter

For real z below the spectrum of the actual F, put A=F-z>0 and
a[q]=||A^(1/2)q||^2. A continuous antilinear residual functional rho on
the form domain satisfies

    sup_(q != 0) |rho(q)|^2/a[q]
      = ||A^(-1/2) rho||^2
      = <rho,A^(-1)rho>.                                  (CT1)

The last notation is the form-dual pairing when rho is not an L2 vector.
This is exactly the energy-dual quantity in Q7 of the preceding report.
It requires neither the vertical conditional gap nor a derivative norm
of rho. A proof by bounding weak first-order currents can nevertheless be
valid: it need not differentiate rho or lose horizontal energy.

For nonreal z, <u,(F-z)v> is not a Hilbert inner product, and the quadratic
resolvent value need not be real. Set B=F-Re(z)>0. Spectral calculus gives

    |<rho,(F-z)^(-1)rho>| <= <rho,B^(-1)rho>.                (CT2)

Thus a real-shift energy-dual estimate extends to the complex half-plane,
but the asserted positive Riesz identity does not apply directly there.
If F>=mI, the controlling distance is m-Re(z), not m alone.

## 2. The proposed extraction of C0 fails already in one block

In the established two-torus example, use p_n=e^(iny)/n, so b[p_n]=1.
The complete residual is

    rho_n = g n^3/[2(n^2+1)] cos(2k) e^(iny).

Orthogonality gives

    ||rho_n||_2^2/g^2 = n^6/[8(n^2+1)^2]
                      >= n^2/32 -> infinity,              (CT3)

whereas

    <rho_n,A_g^(-1)rho_n>
       <= g^2 n^6/[8(1-|g|)(n^2+1)^2(n^2+4)]
       <= g^2/[8(1-|g|)].                                 (CT4)

Consequently replacing a derivative norm by an unweighted L2 residual
norm still loses the essential horizontal inverse denominator n^2+4.
The desired local L2 operator norm C0 has infinite supremum in this exact
model. A finite maximum over sampled n cannot bound that supremum.
This is a counterexample to the asserted inference, not to Wilson W6.

The preceding 21 controls comprise six SU(2) algebra checks, seven torus
mode controls, and eight Euclidean conversion checks. They are not 21
Wilson residual vectors, nor a finite exhaustion of the retained domain.
They cannot be used to extract the proposed all-energy Wilson C0.

## 3. The bouquet floor is not a magnetic curvature endomorphism

The established bouquet floor concerns

    g^2 Q(H_u-2e_u)Q >= I

on physical scalar wavefunctions in the literal source complement. A
covariant lattice Laplacian d_U* d_U acts on lattice cochains, or on
sections of an explicitly specified vector bundle. These are different
operators and Hilbert spaces. No identification has been supplied that
turns the full transported quantum fast operator into the proposed sum
of a cochain Laplacian and block curvature endomorphisms.

The actual source defines F by restricting the complete, vacuum-subtracted
Hamiltonian form to Q. Source transport adds commutator terms; the true
conditional projection also depends on the joint ground. Even an exactly
nonnegative addition to the bare Hamiltonian does not preserve its gap
after its new ground energy is subtracted. A finite positive Dirichlet-jump
counterexample is given in [operator_audit.md](operator_audit.md).

The number 3g^2/4 is an upper bound on the infimum of the *vertical*
operator. It is not a negative correction to the full quantum floor.
The expression c0=1-3g^2/4 cannot be obtained from that result.

The concrete missing identity is a common-space comparison of the actual
coupled, vacuum-subtracted, source-transported Q form with the proposed
block reference, including interfaces. Positivity of a bare jump term
does not establish this identity or its lower bound.

## 4. A gap and a local bare operator do not establish projected CT decay

On a cycle of N vertices, let H=I, v=N^(-1/2)(1,...,1), and Q=I-|v><v|.
The compressed operator A=QHQ restricted to QH is exactly I_Q and has
floor one. Its inverse, embedded back into the site space, is

    Q A^(-1) Q=Q,
    <e_x,Q A^(-1)Q e_y>=-1/N,  x!=y.                      (CT5)

At separation N/2 this cannot satisfy a volume-independent estimate
C exp(-mu N/2) with mu>0. The bare H has range zero; the compression is
what destroys the claimed spatial decay. The site projections do not
preserve Q, and Q P_x Q are not an orthogonal family of projections.
This exact example does not identify the Wilson Q with this Q. It shows
why locality after the actual compression and transport needs proof.

A lattice many-body wavefunction space is also a tensor product (followed
by constraints), not automatically a direct sum of one-block spaces.
Local observable supports alone do not define orthogonal spatial P_B.

For an actual second-order differential operator, conjugation introduces
first-order operators. Their L2 operator norm is generally infinite:
already on a circle, ||partial_theta e^(in theta)||=|n|. Quantum SU(2)
electric derivatives likewise have arbitrarily high representation modes.
Compactness of the link group does not bound these differential operators.
They must be estimated relative to an energy form or resolvent. If the
gradient instead means bounded discrete incidence on cochains, that is a
different operator and does not resolve the identification in Section 3.

The established CT method for differential operators handles weighted
conjugations through forms and resolvent-relative estimates; see
[Shen, Section 4](https://arxiv.org/pdf/1207.3782). Our finite-range
weighted-block theorem below is derived directly, with its hypotheses
made explicit.

## 5. A correct energy-weighted Combes–Thomas theorem

Suppose a genuine orthogonal decomposition H=direct_sum_B H_B has been
constructed. Let D=direct_sum_B D_B be a positive reference operator
retaining the horizontal energies, with D_B>=d_*>0. Define by forms

    A=D^(1/2) B D^(1/2),    B>=kappa I, kappa>0.           (CT6)

For a simple sufficient realization take B bounded and self-adjoint.
Allowing an unbounded diagonal requires a separately justified closed-form
realization and compatible diagonal domain, as discussed in
[ct_repair.md](ct_repair.md). Suppose its off-diagonal
blocks have interaction range R and uniform row and column sums

    sup_B sum_(C != B) ||B_BC|| <= J.

For J>0, set

    mu = R^(-1) log(1+kappa/(2J)).                         (CT7)

Conjugation by bounded truncated weights exp(mu min(d(B,B0),L)) changes B
by an operator of norm
at most J(exp(mu R)-1)=kappa/2. The inverse Neumann estimate, followed
by removal of the weight and letting L grow, proves

    ||D_B^(1/2) P_B A^(-1) P_C D_C^(1/2)||
        <= (2/kappa) exp(-mu d(B,C)).                      (CT8)

The kernel in (CT8) denotes its bounded form extension. If J=0 there are
no off-diagonal inverse blocks. Bounded truncated weights give the same
argument on an infinite graph once the operator and decomposition exist.

The local input is now in the appropriate norm:

    f_B=D_B^(-1/2)rho_B,
    sum_B ||f_B||^2 <= C_loc^2 g^2 b[p].                  (CT9)

Unlike (CT3), this retains the local inverse denominator. On a cubic
d-dimensional block graph, the Schur estimate gives

    <rho,A^(-1)rho>
        <= (2 C_loc^2/kappa) M_d(mu) g^2 b[p],
    M_d(mu)=[(1+exp(-mu))/(1-exp(-mu))]^d.                (CT10)

In fact, if (CT6) and the true orthogonal decomposition are already
available, inverse form order gives the sharper estimate immediately:

    <rho,A^(-1)rho> <= C_loc^2 g^2 b[p]/kappa.             (CT11)

CT is unnecessary for this particular global norm; its role is to prove
off-diagonal decay or to control a nonorthogonal synthesis of local
residuals. The lattice sum formula in the proposal is correct for d=4.
The Hamiltonian source in the present spatial derivation uses three
spatial directions; d must match the block geometry actually identified.

If local residuals are synthesized in a many-body space instead, write
rho=g sum_B S_B f_B, where S_B takes values in the actual A-energy dual.
Set T_B=A^(-1/2)S_B. A sufficient, properly typed local theorem is

    ||T_B* T_C|| <= K exp(-mu d(B,C)),
    sum_B ||f_B||^2 <= C_loc^2 b[p].                      (CT12)

The Schur test then yields K C_loc^2 M_d(mu) g^2 b[p]. This formulation
does not assert an orthogonal block decomposition of the physical
wavefunction space. Proving (CT12) for the actual complete residual,
possibly using CT after a justified auxiliary-space construction, is a
concrete remaining route.

Uniformity in volume alone is insufficient for W6. The constants must also
have the required uniformity as g tends to zero. In particular kappa must
stay positive, the relative hopping J must stay controlled, and mu must
not tend to zero unless its loss is compensated elsewhere. For small mu,
M_4(mu) is asymptotic to 16 mu^(-4). No numerical choice of mu from the
bouquet vertical upper bound proves those properties.

## 6. Diagonal defect and the actual conclusion

Suppose a valid argument establishes

    <rho,A_g^(-1)rho> <= K_res g^2 b[p]
    and |d_g[u,u]| <= K_diag |g| b[p],
    u=A_0^(-1)t_1p,

uniformly on the required domain and parameter range. The exact residual
identity then gives

    |<t_1p,(A_g^(-1)-A_0^(-1))t_1p>|
       <= (K_diag+K_res g0)|g| b[p],  |g|<=g0.             (CT13)

The final addition is valid. The proposed numerical C0 and c0 are not
established inputs to it.

The stopping point is now: identify and bound the actual transported
coupled fast operator in the energy-weighted localization construction,
and establish local energy-dual synthesis for the complete residual.
Neither task can be discharged by taking a maximum over the earlier
finite controls. This audit does not prove or disprove coupled Wilson W6.

## Files and evidence

- [Residual audit](residual_audit.md): exact all-energy L2 obstruction,
  complex spectral parameter and finite-control scope.
- [Operator audit](operator_audit.md): source identities, bouquet scope,
  and failure of gap monotonicity under positive jump additions.
- [Conditional localization theorem](ct_repair.md): energy-weighted CT,
  operator domains and many-body synthesis.
- `verify_residual.py` and `verify_audit.py`: finite exact controls,
  supplementary to the analytic proofs above.

No graph status or existing source theorem was changed. The earlier
[continuation report](../w6_quantum_attempt_20260909/QUANTUM_CONTINUATION.md)
is annotated with this audit.
