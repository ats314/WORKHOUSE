# Weighted curvature repair and an explicit compact Wilson rotor gap

Successor, 9 September 2026: `wilson-vacuum-aligned-assembly.md` VA8 proves
that the literal positive WR26 comparison below fails on large connected
physical Wilson lattices. VA9--VA11 replace it by true-vacuum conditional
projections with a volume-independent local floor. VA14--VA15 state the
remaining physical assembly and spatial-continuum estimates. The preceding
rotor and actual-link results remain applicable in their stated scope.

Date: 2026-09-08. Analytic results with separately scoped exact symbolic controls.
This continues `yangmills-pbh-wilson-test.md`; it does not reinstate its refuted
pointwise curvature claim. It constructs a positive replacement and then takes
it onto the actual overlapping-link Hamiltonian.

## WR1. Absorb negative curvature in the derivative energy

For the four-link SU(2) plaquette orbit use the original quotient metric
`dtheta^2`, 0 < theta < pi, and normalized density

    rho_beta = Z^-1 exp[-beta(1-cos theta)] sin^2 theta,
    W = beta(1-cos theta) - 2 log sin theta,
    L = d^2 - W' d,                 beta >= 0.

The previous negative pointwise value W''(2pi/3) does not prevent a gap.
Differentiation intertwines -L with the derivative operator

    B = -L + W''.

For h = csc theta an exact computation gives

    (B h)/h = 2 csc^2 theta - 1 >= 1.                    (WR1)

In particular, the beta-dependent terms cancel. Integration by parts gives

    integral [(u')^2 + W'' u^2] rho
      = integral h^2 [(u/h)']^2 rho
        + integral [(B h)/h] u^2 rho.                   (WR2)

Start on compactly supported u. For derivatives u=f' of smooth class functions,
u=O(theta) and u=O(pi-theta) at the endpoints. The boundary terms vanish and
cutoffs extend the inequality in the derivative form norm. The singular h
itself need not belong to that domain. Compact ellipticity on SU(2) supplies a
complete smooth class eigenbasis; applying WR2 to the derivative of each
nonconstant eigenfunction proves gap(-L)>=1. This is an integrated proof, not
a new assertion that W'' is positive.

There is also a coupling-growing bound. Conjugation by sqrt(rho) turns B into

    -d^2 + beta^2 sin^2(theta)/4 - beta cos(theta)/2
         + 2 csc^2(theta) - 1.

The sum of its first and inverse-square potential terms is at least
sqrt(2) beta. Therefore

    gap(-L) >= max{1, (sqrt(2)-1/2) beta - 1}.           (WR3)

The factor c must be restored for cL. The eigenfunction argument establishes
Poincare/spectral gap here; an LSI or physical-time identification is not
silently inferred. Independent copies tensorize without a volume loss.

Method context: the weighted-gradient intertwining mechanism is developed in
Bonnefont--Joulin, *Intertwining relations for one-dimensional diffusions and
application to functional inequalities*, arXiv:1304.3595,
https://arxiv.org/abs/1304.3595 . WR1--WR3 are derived above for this actual
Wilson density, rather than imported as a claim about it.

## WR2. A smooth non-Gaussian trial for the physical rotor

Now change operators explicitly. Work on the entire SU(2)=unit S^3, not only
class functions, with

    H(c,k) = -c Delta_S3 + k(1-cos theta),  c>0, k>=0.

The radial part of Delta is D=d^2+2 cot(theta)d. Put

    x=cos(theta/2),  A=sqrt(8k/c),
    psi_A(theta)=sinh(Ax)/(Ax),                          (WR4)

with its continuous value 1 when Ax=0. Its convergent even power series in x
is a smooth function of cos(theta), including both poles. It is positive.
In x coordinates,

    D f = [(1-x^2)f''+(2/x-5x)f']/4,
    f''+2f'/x=A^2 f.

Consequently its physical Hamiltonian residual is exactly

    R_A = (H psi_A)/psi_A
        = (3c/4)[Ax coth(Ax)-1].                       (WR5)

For z>=0, 0<=z coth z-1<=z, by tanh z<=z and e^(2z)>=1+2z.
Thus R_A is globally nonnegative and bounded above by 3cA/4. Rayleigh--Ritz
with this trial and, separately, the constant function gives

    E0(c,k) <= min{k, 3 sqrt(ck/2)}.                    (WR6)

This retains the nonconstant residual. It does not identify psi_A with the
true ground state, and it uses no comparison to a free Gaussian measure.

## WR3. A physical gap on the complete rotor space, at every coupling

Compact ellipticity and positivity give a unique positive ground state. By
conjugation symmetry it is radial. Decompose all other states into ordinary
S^2 angular momenta l=0,1,... in polar coordinates on S^3. Multiplication by
sin(theta) transforms the l-sector to the Friedrichs operator

    H_l = -c d^2 - c + k(1-cos theta)
          + c l(l+1)/sin^2(theta)                     (WR7)

on (0,pi), with Dirichlet endpoints for l=0 and the induced stronger
endpoint condition for l>0. This is a complete decomposition.

On this interval 1-cos(theta)>=2theta^2/pi^2. Extension by zero into the
half-line Dirichlet oscillator, followed by min--max, gives

    E0(c,k) >= 3 sqrt(2ck)/pi-c,
    E_rad,1(c,k) >= 7 sqrt(2ck)/pi-c.                  (WR8)

The half-line oscillator eigenvalues are the odd full-line levels, with
coefficients 3,7,11,... . At k=0 the same inequalities follow directly;
no discrete half-line oscillator is claimed in that case.
Also E_rad,1>=3c because the added potential is nonnegative. Combining WR6
and WR8 gives, with D0=sqrt(2)(7/pi-3/2)>1,

    gap_rad >= max{3c-k, D0 sqrt(ck)-c} >= c/2.         (WR9)

For the final inequality split k/c at 5/2. The exact estimate
pi<22/7 implies D0>8sqrt(2)/11>1.

For every l>=1 the centrifugal term gives gap_l>=2c. For a sharper bound
write s=1-cos(theta) and use sin^2(theta)=s(2-s)<=2s. For 0<=eta<=1,

    H_l(c,k) >= H_0(c,(1-eta)k) + eta k s + c/s
              >= E0(c,(1-eta)k) + 2 sqrt(eta ck).

Optimizing the resulting WR6/WR8 bound over eta yields

    gap_l >= [sqrt(4+18/pi^2)-3/sqrt(2)] sqrt(ck)-c
           >= (1/4) sqrt(ck)-c.                      (WR10)

The coefficient exceeds 1/4: pi^2<10 gives sqrt(4+18/pi^2)>sqrt(29/5),
whereas (3/sqrt(2)+1/4)^2=73/16+3sqrt(2)/4<91/16<29/5.
Taking the minimum over the *complete* radial and angular spectra proves

    gap H(c,k) >= max{c/2, (1/4)sqrt(ck)-c}
                >= max{c/2, sqrt(ck)/16}.             (WR11)

For the last inequality split k/c at 64. These constants are deliberately
conservative. The analytic domain and min--max arguments are not claimed
Lean-formalized; the exact identities and scalar budget algebra are checked
in `src/workhouse/invariants/wilson_weighted.py`.

In the previously specified four-link scaled Wilson convention,

    H_g=-2g^2 Delta_(SU2,radius 2) + 2g^-2(2-Tr U),
    c=g^2/2, k=4/g^2,
    gap H_g >= max{g^2/4, sqrt(2)/16},  g>0.           (WR12)

This is a fixed-cell scaled Hamiltonian. A lattice-spacing prefactor or a
renormalized physical clock must still be restored for a continuum claim.

## WR4. Volume passage that is already justified

A sum of M independent full rotors has the tensor product of their unique
ground states and gap at least WR11, uniformly in M. Restricting to
simultaneous conjugation preserves that vacuum and cannot introduce a lower
excited eigenvalue. Thus the statement includes color-paired states allowed
by a common Gauss constraint; it is not a tensorization only of class sectors.
For countably many independent rotors the product-ground representation and
closure of the finite-excitation Hamiltonian retain the same gap.

This applies to the additive rotor model (and its common-conjugation
restriction). It is not the cubic lattice with plaquettes sharing electric
links. The following calculation explicitly takes the trial onto that lattice.

## WR5. Actual shared-link residual, and a positive interacting repair

Let a finite SU(2) lattice have distinct four-edge plaquettes and product unit
S^3 link metrics. Use its actual Hamiltonian

    H_Lambda = -epsilon sum_e Delta_e + k sum_p s_p,
    s_p=1-(1/2)Tr U_p,  epsilon>0, k>=0.

Let q>=1 bound the number of plaquettes incident to an edge (q=2(d-1) on
the d-dimensional cubic lattice). Set c=4epsilon. The smooth positive
gauge-invariant trial is

    Psi_A(U)=product_p psi_A(U_p),  phi_p=log psi_A(U_p).

Ad-invariance and left/right invariance of the link metric imply
sum_(e in p) Delta_e phi_p=4D phi_p and
|grad_e phi_p|^2=|phi_p'|^2 for e in p. No gauge fixing or fixed-rank
horizontal projector is needed. The exact residual is

    R_Lambda = sum_p [k s_p-c D phi_p-c|phi_p'|^2]
      -2epsilon sum_e sum_(p<r containing e)
                    <grad_e phi_p,grad_e phi_r>.      (WR13)

The shared-link term is retained. It is not zero by gauge invariance.
Writing z=A cos(theta/2) and L(z)=coth z-1/z gives

    |phi_p'|^2 = (A^2 s_p/8)L(z_p)^2 <= A^2 s_p/8.

Use the exact incidence inequality

    |sum_(p containing e) v_p|^2
       <= q sum_(p containing e)|v_p|^2,

whose defect is a sum of pairwise squared differences, with zero padding if
the edge has fewer than q incident plaquettes. Choose the *damped* amplitude

    A^2=8k/(q c).                                    (WR14)

Unlike importing the isolated-rotor amplitude, this absorbs the entire
shared-link cross term. Direct substitution in WR13 proves globally

    R_Lambda >= (3c/4) sum_p [z_p coth z_p-1] >= 0.     (WR15)

More precisely its exact nonnegative remainder after the displayed sum is

    (q-1)c sum_p [A^2 s_p/8-|phi_p'|^2]
     +epsilon sum_e [q sum_(p containing e)|grad_e phi_p|^2
                         -|sum_(p containing e)grad_e phi_p|^2]. (WR16)

WR15--WR16 are an interacting lattice result with constants independent of
the number of plaquettes, not a statement about independent rotors. They
give a global trial residual floor, not a many-body spectral gap.

## WR6. The precise remaining derivation

There is now a concrete positive trial on the overlapping lattice, so test
the existing ground-state comparison, rather than stopping at PBH curvature.
Normalize nu_Lambda=Psi_A^2 dU/integral Psi_A^2 dU and define

    K_Lambda=-epsilon[sum_e Delta_e+2 grad log(Psi_A).grad],
    Psi_A^-1 H_Lambda Psi_A=K_Lambda+R_Lambda.          (WR17)

Under the smooth compact domains above this is an exact unitary transform
from L^2(nu_Lambda) after normalization. Let gamma_Lambda be the full
gauge-invariant gap of K_Lambda. The existing residual min--max theorem
(`yangmills-weighted-curvature.md`, GST-6) gives

    gap(H_Lambda) >= gamma_Lambda
                    -[E_(nu_Lambda) R_Lambda-inf R_Lambda]. (WR18)

The next inequality needed to close *this particular comparison* is

    E_(nu_Lambda) R_Lambda-inf R_Lambda
       <= gamma_Lambda-m_*,    m_*>0,                (WR19)

uniformly along the required volume/spacing trajectory with its physical
clock. WR15 supplies only the floor, not WR19. Even independent undamped
rotors show why one must localize this step: their nonconstant continuous
R_A has delta=E_nu R_A-min R_A>0 for k>0; M copies have residual loss M delta
while their weighted diffusion gap is the one-copy gap. Global WR19 then
fails for large M although WR11 tensorizes. Therefore WR18 must be applied
locally *before* assembly, or replaced by a connected residual comparison.

There is an exact stronger test of the proposed local assembly. On the full
four-link patch L^2(SU(2)^4), let Omega be the true positive ground state of
the patch Hamiltonian with link kinetic coefficient epsilon. It is gauge
invariant by uniqueness. Its squared probability measure has exactly Haar
single-link marginals: a gauge transformation at either endpoint translates
that link, so the invariant marginal is Haar. For any smooth f of one link,

    ||Omega f(U_e)||^2 = integral_SU2 |f|^2 dU,
    <Omega f,(H_patch-E0)Omega f>
                  = epsilon integral_SU2 |grad f|^2 dU. (WR20)

These are exact identities using the true ground-state transform; no
approximate wavefunction or weak-coupling limit occurs. Choosing a centered
fundamental coordinate, whose unit S^3 eigenvalue is 3, proves

    gap(H_patch on the full boundary space) <= 3epsilon
                         for every k>=0.             (WR21)

In contrast, the isolated *gauge-invariant* rotor has the positive bound
WR11 with c=4epsilon. Thus extending that quotient bound to a complete
unreduced patch is actually false at k/epsilon sufficiently large.

More generally choose all Peter--Weyl functions of that link of degrees
0<=n<=N. Their Casimirs are n(n+2) and their total dimension is
(N+1)(N+2)(2N+3)/6. WR20 and min--max give that many full-patch eigenvalues
(counting the ground) below or equal to epsilon N(N+2), uniformly in k.
At a fixed positive target gap as epsilon decreases, the required retained
boundary rank therefore grows at least on the order of epsilon^(-3/2).
A fixed finite boundary frame cannot supply a uniform fast floor in this
unreduced comparison. These boundary charges can combine across cells to
satisfy the global Gauss law; they are not individually global physical
excitations. This disproves neither a gap of the assembled physical lattice
nor a comparison retaining the full compact boundary space.

The same test survives imposing the *interior* Gauss law on a larger patch:
replace U_e by the holonomy U_gamma of a simple path with endpoints on the
patch boundary. This is invariant at every interior path vertex. The boundary
gauge action still forces its true-ground marginal to be Haar, and each of
the path's r distinct edges contributes once, giving epsilon r times the
one-link Dirichlet form in WR20. Thus the issue is not merely the inclusion
of interior gauge-redundant states. A full boundary-holonomy retention avoids
this particular finite-rank obstruction; it leaves its interacting fast
complement and connected residual to estimate.

The precise failure is therefore the attempted inference
`isolated physical rotor gap -> uniform full boundary-source fast gap`.
WR20--WR21 furnish its counterexample at every coupling, beyond the earlier
curvature test. The prior actual-block fast-complement and selected-source
results must supply this larger, properly retained frame before matching.

## WR7. Retain the full boundary: an actual-link fast barrier

The preceding counterexample has a constructive repair. Freeze the other
links, but retain their *entire* compact configuration space, and consider
one link e with q incident plaquettes and conditional Hamiltonian

    h_e(b)=-epsilon Delta_e + v sum_(p containing e) s_p,
    epsilon>0, v>0.                                   (WR22)

Orient each plaquette term as Re Tr(U_e S_p)/2. Each staple S_p is SU(2),
and a sum of real quaternions is a real quaternion. Therefore

    sum_p S_p = alpha V,  0<=alpha<=q,  V in SU(2),
    h_e(b) is unitarily equivalent to
        H(epsilon,v alpha)+v(q-alpha).                (WR23)

At alpha=0 the operator is just -epsilon Delta_e+vq; its positive ground
is constant, so an arbitrary choice of V has no effect. Let P_e(b) project
onto the exact conditional ground and put e_*=E0(epsilon,vq).
The ground energy of -epsilon Delta-v alpha cos(theta) is a concave even
function of alpha (variational infimum of affine functions; U -> -U gives
evenness). It is thus nonincreasing for alpha>=0. Consequently the ground
energy of h_e(b) is at least e_* for every boundary b.

If alpha>=q/2, WR11 yields a conditional gap at least
sqrt(epsilon vq)/(16sqrt(2)). If alpha<q/2, the nonnegative Laplacian and
potential give h_e(b)>=vq/2, whereas WR6 gives
e_*<=3sqrt(epsilon vq/2). For vq/epsilon>=32,

    vq/2-3sqrt(epsilon vq/2)
      >= sqrt(epsilon vq)/sqrt(2)
      >= sqrt(epsilon vq)/(16sqrt(2)).

The two regions therefore yield the single operator inequality

    h_e(b)-e_* >= delta_* [I-P_e(b)],
    delta_*=sqrt(epsilon vq)/(16sqrt(2)),
    vq/epsilon>=32, uniformly in every boundary b.     (WR24)

This is an actual Wilson-link statement, including staple cancellation and
all angular sectors. The direct-integral projection retains the full compact
boundary space and has infinite total rank. There is no differentiation of
a choice of V at alpha=0 in this proof. The low-curvature/bad-staple region
is absorbed by its action energy; it is not discarded probabilistically.
Uniqueness of the conditional ground makes P_e gauge covariant under changes
of the frozen boundary; its direct-integral operator commutes with the full
gauge action. Thus WR24 also restricts to the global physical Hilbert space.

## WR8. Where the repaired local bounds still require a new proof

For four-edge plaquettes choose v=k/4 in WR22. Then the full lattice
Hamiltonian is exactly sum_e h_e. Let e_{*,e}, delta_{*,e} use the actual
incidence q_e at each edge. Edges with q_e=0 keep their electric term
separately. Whenever the stated local coupling thresholds hold, WR24 gives

    H_Lambda - sum_e e_{*,e}
       >= sum_e delta_{*,e}(I-P_e).                   (WR25)

No claim of commuting P_e or a common conditional vacuum is made. Write
F_Lambda=E0(H_Lambda)-sum_e e_{*,e}>=0. The exact next implication needed
to get a physical gap from this sum is control, on the true vacuum
complement, of

    sum_e delta_{*,e}(I-P_e)-F_Lambda I.              (WR26)

In particular, neither dropping F_Lambda nor declaring the conditional
ground projections compatible is valid. This is a concrete improvement
over the earlier stopping point: the rotor estimate has now been carried
to a uniform actual-link fast barrier on the full boundary space. What is
still missing is a connected assembly estimate that cancels the local
vacuum/frustration contribution while controlling the noncommuting P_e,
with the spatial-scale errors required for matching. WR25 alone does not
bound WR26 positively on the physical vacuum complement. Its right-hand
side may itself be too crude; a stronger connected Schur comparison may be
needed. The proof does not assume that this candidate inequality is true.

An exact two-dimensional control shows that the missing projection geometry
is substantive. Put P1=|0><0| and P2=|v><v| with
v=(r,sqrt(1-r^2)), 0<r<1. Each h_i=I-P_i has gap one, but

    spec(h1+h2)={1-r,1+r},  F=1-r,  gap=2r.          (WR27)

Thus uniform local floors with their exact baseline do not, by themselves,
give a positive uniform assembled gap. This finite control is not asserted
to model the actual Wilson projectors. It isolates the further inequality
that must be proved about those projectors instead of being assumed.

The frustration term is also strictly positive on an actual finite lattice
as soon as an edge has two independently variable staples that fail to align
on a nonempty open set. To see this, the conditional ground energy
e(alpha)=inf spec(-epsilon Delta-v alpha cos(theta)) is strictly concave:

    e''(alpha)=-2v^2 <w,(h(alpha)-e(alpha))_perp^-1 w><0,
    w=(cos(theta)-<cos(theta)>) Omega_alpha.

Compact ellipticity gives a simple positive ground and a positive inverse
on its complement; w is nonzero because cos(theta) is nonconstant and the
ground is strictly positive. Evenness then makes e strictly decreasing on
alpha>=0. Thus h_e(b) has ground strictly above e_{*,e} wherever alpha<q_e.
The full finite-lattice ground is likewise positive everywhere, so its
expectation of this strict conditional excess is positive. Summing gives

    F_Lambda>0 on those overlapping lattices.         (WR28)

This proves that dropping F_Lambda is actually wrong there. It supplies
neither a volume-uniform upper budget for F_Lambda nor the missing connected
comparison. The statement excludes configurations-only arguments: it uses
an open set of positive measure and the actual positive ground density.

The supplementary exact controls in `scripts/validate_wilson_weighted.py`
check the quaternion factorization and WR24's scalar threshold. The
same validator checks the characteristic polynomial in WR27. The
conditional spectral projection, concavity and direct-integral arguments
are analytic, and are not claimed machine-formalized.

The unsupplied step is thus a bound on the *connected* contribution of WR13's
mixed link derivatives and WR16's residual to that complete boundary-source
frame, after local vacuum energies cancel, uniform in the spatial refinements.
WR11, WR15 and the stronger local barrier WR24 do not imply that bound. The
existing selected inverse estimate W6 in `wilson-selected-inverse-wall.md`
is a separate precise candidate for accomplishing it; it remains open.
The old pointwise curvature obstruction does not block WR1--WR16.

Once the complete interacting shell and relative-error/source estimates are
established, the matching and relative-gap theorems in
`wilson-marked-shell-transport.md` and `wilson-spatial-schur-excess.md`
apply with their stated budgets. Applying them to WR11 alone would transport
an independent-cell carrier rather than the actual overlapping Wilson one.

The supplied Jaffe--Witten PDF, page 11, section 6.5, identifies the still
unmet continuum requirement exactly: “One must then verify the existence of
limits of appropriate expectations of gauge-invariant observables as the
lattice spacing tends to zero and as the volume tends to infinity.” The
volume result WR4 is for the specified independent rotor model; WR15 is an
actual lattice trial inequality. Neither asserts those continuum limits.
