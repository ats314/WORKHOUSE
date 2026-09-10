# Vacuum-aligned Wilson assembly: connected-volume failure and exact repair

Continuation: [actual block estimates](wilson-true-vacuum-block-estimates.md)
optimizes the conditional gap to a square-root coupling loss and reduces
the remaining physical angle to a mixed ratio of the actual ground.
VA17 below remains a statement about the earlier, weaker VA10 floor.

9 September 2026. Continuation of WR25--WR28 in
`wilson-weighted-repair-and-rotor-gap.md`. The old comparison is tested on
actual connected periodic spatial Wilson lattices, then replaced using the
true ground before any local floor is discarded.

Analytic proofs below have separately scoped exact algebra controls. They
do not assert a continuum construction or a Lean formalization of the
semigroup, domain or spectral arguments.

## VA1. A local finite-energy bound for the actual quantum vacuum

Let Lambda be a finite three-dimensional periodic cubic lattice of side L>=3.
Every link belongs to q=4 plaquettes. Use unit-S3 SU(2) link metrics and

    H=-epsilon sum_e Delta_e+k sum_p s_p,
    s_p=1-(1/2)Tr U_p in [0,2], epsilon>0, k>=0.

Let Omega>0 be its normalized ground, E0 its energy, and mu=Omega^2 dU.
Compact ellipticity and positivity give a unique smooth ground, invariant
under the full gauge action. No infinite-volume ground is assumed.

For a set B of r links let p_B count plaquettes touching B. Split

    H=T_B+H_out+V_B,
    T_B=-epsilon sum_(e in B) Delta_e,
    0<=V_B<=2k p_B.

H_out acts only outside B, and includes only plaquettes disjoint from B.
Feynman--Kac positivity bounds, pointwise on nonnegative functions, give

    exp(-2k p_B t) exp(-t T_B)exp(-t H_out)
       <= exp(-t H) <= exp(-t T_B)exp(-t H_out).        (VA1)

These are positive-kernel inequalities, not an unsupported operator-order
monotonicity claim for the exponential of noncommuting operators.
Apply them to Omega and use exp(-tH)Omega=exp(-tE0)Omega. If m_tau,M_tau
bound the single-link Haar heat kernel at tau=epsilon t, then, for any two
configurations u,u' on B and the same outside configuration b,

    Omega(u,b)/Omega(u',b)
       <= exp(2k p_B t)(M_tau/m_tau)^r.                (VA2)

The common positive integral over B and the outside semigroup cancels in
the ratio. This is independent of the total number of links.

Here is a completely explicit kernel bound. The unit-S3 SU(2) heat kernel
has expansion sum_(n>=0)(n+1)exp[-n(n+2)tau] chi_n. Since |chi_n|<=n+1,

    |p_1-1| <= sum_(n>=1)(n+1)^2 exp[-n(n+2)]
       <= sum_(n>=1)(n+1)^2 (1/20)^n
        =1541/6859 < 1/4.                            (VA3)

Indeed n(n+2)>=3n and exp(3)>20, the latter already certified by the
Taylor polynomial through degree eight, 89641/4480>20. Hence
3/4<=p_1<=5/4. Choose t=1/epsilon and put

    R_B=(5/3)^r exp(2k p_B/epsilon).

The exact conditional vacuum density satisfies

    max rho_B(.|b)/min rho_B(.|b) <= R_B^2,
    rho_B(u|b) >= R_B^-2                              (VA4)

relative to normalized product Haar. These bounds concern the *true joint
quantum vacuum*, not a classical Wilson Gibbs density or the ground of a
frozen conditional link Hamiltonian.

## VA2. The WR25 remainder is extensive on actual connected lattices

Assume k/epsilon>=32. Use the preceding WR decomposition with v=k/4 and
q=4. Write

    e_*=E0(epsilon,k), delta=sqrt(epsilon k)/(16sqrt(2)),
    h_e=-epsilon Delta_e+(k/4)sum_(p containing e) s_p,
    Q_e=I-P_e, D_e=h_e-e_*-delta Q_e >=0.

P_e is the ground projection of the frozen-link operator, retaining the
entire boundary. The notation Q_e here is specific to WR24 and will be
replaced by true-vacuum conditional projections in VA4 below.

If the four staples around e have quaternion sum of norm alpha<=q/2=2,
the bad-region bound used to prove WR24 gives

    h_e-e_* >= k/2-3sqrt(epsilon k/2) >=16 delta,
    D_e >=15 delta                                   (VA5)

on that frozen boundary. Globally D_e>=0, so as direct-integral forms

    D_e >=15 delta 1_(alpha_e<=2).

There is a uniform positive probability of this event under mu. Select the
four opposite parallel links B_e, one in each plaquette containing e.
For L>=3 these are distinct, and each occurs in only its own staple among
the four. Conditional on all other links, their staples are four independent
Haar variables under product Haar: fixed left/right multiplication preserves
Haar. Require two staples to lie in the angle-pi/8 cap about I and two in
the corresponding cap about -I. Each differs from its prescribed center
quaternion by less than 1/2, so their sum has norm less than 2.

The cap has Haar measure

    b0=(2/pi)integral_0^(pi/8) sin^2(theta)dtheta
       =1/8-sqrt(2)/(4pi)>0.

There are r=4 links in B_e and at most p_B=16 touching plaquettes. VA4 yields

    mu(alpha_e<=2) >= p0,
    p0=b0^4 (3/5)^8 exp(-64k/epsilon)>0.              (VA6)

The event may depend on the frozen outside links; the conditional Haar
probability b0^4 is the same for each outside configuration, so VA4 applies.
All constants are independent of L. They can be extremely small; positivity
and volume independence, rather than numerical size, are what is used next.

Let A=sum_e delta Q_e, D=sum_e D_e, and F=E0-|E(Lambda)|e_*. Then exactly

    H-|E(Lambda)|e_*=A+D,
    <Omega,D Omega> = F-<Omega,A Omega>
                   >=15 delta p0 |E(Lambda)|.        (VA7)

This strengthens WR28 from strict positivity to an extensive *discarded*
vacuum remainder at every fixed allowed k/epsilon.

## VA3. WR26 is false on the physical vacuum complement at large volume

Choose one plaquette X. Its trace angle theta_X has a continuous positive
density in (0,pi) under mu, by smooth positivity of Omega and Haar
disintegration. Let C_L(theta) be its cumulative distribution and define

    f_X(U)=exp[2pi i C_L(theta_X(U))].

The probability integral transform gives mu(f_X)=0 and |f_X|=1. This bounded
gauge-invariant function belongs to H1: its radial density is bounded at
fixed finite L and has the usual sin^2(theta) endpoint factor. Thus
psi_X=Omega f_X is a normalized physical form-domain vector orthogonal to
Omega. Its definition may depend on L, which is permitted when testing a
uniform bound over the complete physical complement.

For e not in the four-link support X, P_e commutes with multiplication by
f_X. This is true even when its kernel depends on links of X: P_e integrates
only U_e. Since |f_X|=1, such edges have exactly unchanged expectations in
psi_X and Omega. For e in X, 0<=delta Q_e<=delta I bounds the increase by
delta. Hence VA7 gives

    <psi_X,(A-F)psi_X>
       <=4 delta-<Omega,D Omega>
       <=delta[4-15p0 |E(Lambda)|].                   (VA8)

For |E(Lambda)|>4/(15p0), this is negative. These are connected periodic
three-dimensional Wilson lattices, with the full Gauss law imposed on the
test vector. This is not an independent-copy surrogate and not a claim that
the actual Hamiltonian is gapless. It proves that a positive uniform bound
on the particular discarded-remainder expression WR26 cannot be obtained.

The old route must therefore be replaced, rather than left as an inequality
that might eventually follow from better estimates of the same expression.

## VA4. Exact cancellation before comparison

Use the ground-state transform already established in
`G19_GROUND_MARGINAL_SCHUR_SCORE_20260905.md`, not a newly claimed substitute
for that result. Its source is the `paper/research_notes/` directory of
`C:/WORKHOUSE/WORKHOUSE-autonomous-20260905`, commit
`4bf812428e0af51d1ffcda299b0d97b38b644926`; current file hashes are recorded
by `scripts/validate_wilson_vacuum.py`, together with the localized score
theorem and its center-score obstruction. Multiplication by Omega identifies the centered physical
form with

    <Omega f,(H-E0)Omega f>
                  =epsilon sum_e integral |grad_e f|^2 dmu. (VA9)

This has no discarded D, no sum of approximate vacuum baselines and no F.
It is an exact finite-volume identity for the interacting Wilson Hamiltonian.

Let E_e f=E_mu[f|U_(Lambda\{e})] and hat Q_e=I-E_e. These are orthogonal
conditional-expectation projections in L2(mu). They commute with the full
gauge action, preserve the physical subspace and satisfy hat Q_e 1=0.
Thus their sum has an exact common vacuum from the start. They are not the
frozen-Hamiltonian P_e used in WR24.

VA4 gives a uniform conditional Poincare bound for the *true* vacuum.
The Haar unit-S3 Poincare constant is 1/3. If a density has max/min<=R^2,
comparison of the variance infimum and the Dirichlet form gives

    Var_rho f <= (R^2/3) integral |grad f|^2 rho.

For one link r=1,p_B=4, this proves

    epsilon integral |grad_e f|^2 dmu
       >=gamma_* ||hat Q_e f||^2,
    gamma_*=(27/25)epsilon exp(-16k/epsilon)>0.         (VA10)

Consequently, for every finite periodic lattice at the stated epsilon,k,

    Omega^-1(H-E0)Omega >=gamma_* G_mu,
    G_mu=sum_e (I-E_e),                               (VA11)

on the full form domain and its gauge-invariant restriction. The local
constant is independent of volume; VA10 actually holds for every k>=0.
This is the positive repair after VA8: the vacuum cancellation is exact,
and a uniform true-conditional fast bound has been proved without identifying
the true conditional density with a classical Gibbs or frozen-link ground.

## VA5. Projection geometry, with the Gauss law retained

The intersection of the kernels of hat Q_e is the constants. At fixed L,
strictly positive smooth density on the compact product makes this immediate
from its equivalence to Haar. For a sufficient assembly criterion define

    E_ef=E_mu[.|all links except e,f],
    c_ef^phys=||(E_e E_f-E_ef)|_(gauge-invariant L2(mu))||.

The intersection of the ranges of E_e and E_f is the range of E_ef, also
after restricting to the physical subspace. For two orthogonal projections,
the standard angle decomposition, equivalently the spectrum of their sum,
gives

    {hat Q_e,hat Q_f} >=-c_ef^phys(hat Q_e+hat Q_f).

If kappa=sup_e sum_(f!=e)c_ef^phys<1, expanding G_mu^2 proves

    G_mu^2 >=(1-kappa)G_mu,
    gap_phys(H)>=gamma_*(1-kappa).                    (VA12)

All sums are finite here; a uniform bound would persist in the appropriate
thermodynamic construction. The inequality is sufficient, not asserted
necessary. Weighted or block variants may be better than this row bound.
General approximate tensorization methods are discussed by Caputo--Menz--
Tetali, *Approximate tensorization of entropy at high temperature*,
https://arxiv.org/abs/1405.0608 . No high-temperature hypothesis from that
paper is assumed for the present large-k/epsilon quantum ground measure.

The physical restriction matters. On an isolated four-link plaquette every
physical function is a class function of its total holonomy. Conditioning
on three links and integrating the fourth against the true ground density
therefore gives the full vacuum expectation. Hence, on that physical space,

    E_e=E_0 for every edge, G_mu=4(I-E_0), c_ef^phys=0. (VA13)

The noncommuting-boundary obstruction of the unreduced link space is absent
here. Independent cycles similarly group into their physical cycle factors;
one must not estimate these physical angles by unnecessarily large norms
of charged boundary sectors and then call the resulting loss physical.

## VA6. The next estimate and the attempts to establish it

After VA11 the next sufficient input is an actual physical approximate
tensorization estimate

    Var_mu(f) <= C_AT(L,epsilon,k)
                 sum_e E_mu Var_mu(f|all links except e),       (VA14)

for the full gauge-invariant form-domain class. It would give a physical gap
at least gamma_*/C_AT. A bound on the physical angles in VA12 is one concrete
way to obtain VA14. Neither locality of the bare Hamiltonian nor VA4 makes
the quantum ground density a finite-range Markov field.

Three specific further attempts are distinguished:

1. **Bound all joint densities using VA4.** Apply VA2 to the entire lattice.
   If m<=dmu/dHaar<=M, variance comparison and Haar tensorization give
   C_AT<=M/m. VA2 therefore supplies the explicit bound

       C_AT <= (25/9)^|E| exp(4k |P|/epsilon).

   This proves a finite-volume bound, but grows exponentially with volume.
2. **Use frozen-link projectors.** This changes E_e into the previous P_e,
   loses the common vacuum and reintroduces the actual failure VA8. The
   uniform barrier WR24 is not a substitute for the true E_e in VA12.
3. **Use the existing ground-score theorem.** Its exact cancellation and
   weighted Schur theorem apply after VA9. The true-ground localized Wilson
   score result proves a complete fixed-block source estimate and its
   additive-copy extension. Its proof explicitly uses independence of local
   scores for that extension; it does not bound the connected physical
   projection angles or full selected memory of the coupled cubic vacuum.
   The already disproved global Fisher-growth candidate cannot supply it.

There is also a quantitative pair-angle estimate from the new local bound.
For B={e,f}, p_B<=8, put R_2=(5/3)^2 exp(16k/epsilon). Each conditional
two-link joint density has max/min ratio T<=R_2^2. If its normalized density
is r(x,y), then r>=T^-2 r_x r_y: writing its minimum and maximum as m,M,
r/(r_x r_y)>=m/M^2>=1/T^2 because M<=mT and m<=1. Subtracting the product
part leaves a positive joint density with the same two marginals. The
conditional correlation operator on centered functions consequently has
norm at most 1-T^-2. Thus

    c_ef^phys <= 1-(3/5)^8 exp(-64k/epsilon).           (VA16)

This is a proved all-volume bound for each pair, but contains no dependence
on their separation. Inserting it into VA12 yields only
(|E|-1)[1-(3/5)^8 exp(-64k/epsilon)] as a row bound, which exceeds one for
large volume. It therefore cannot supply the required strict summable
budget. The failure of this estimate is not a claim that the true physical
angles themselves fail the criterion; VA13 already shows that the physical
angles can be much smaller than a general density comparison predicts.

The proposed exponential-angle replacement needs a quantitative smallness
test in addition to decay. Suppose the number of links at graph distance r
from a fixed link is at most C_geom(r+1)^2 and the actual physical angles
are bounded by C_0 exp(-M r), with q=exp(-M). Then a sufficient row budget is

    kappa <= C_0 C_geom [(1+q)/(1-q)^3-1] < 1.         (VA18)

The series identity follows by differentiating the geometric series twice:
sum_(r>=1)(r+1)^2 q^r=(1+q)/(1-q)^3-1. Finiteness for q<1
does not imply the displayed strict inequality. Near-neighbor terms may
instead be bounded individually, and only the remaining tail estimated
by this series. VA13 proves an isolated-cycle identity, not the exponential
bound on the interacting cubic vacuum assumed in VA18.

If the claimed decay is in physical distance a r with a fixed physical
rate M, substitute q=exp(-M a). This particular upper bound grows like
2 C_0 C_geom/(M a)^3 as a tends to zero. A spacing-independent C_0 therefore
does not certify a uniform strict row budget by this argument. This is a
loss in the proposed bound, not a lower bound on the actual angles. A
sharper amplitude estimate or a physical-block version of the criterion
could avoid it, but must be derived for the actual conditional projections.

The exact remaining calculation is therefore to estimate either the
physical conditional-projection angles c_ef^phys with a summable strict
budget, or the less restrictive variance ratio in VA14, for the actual
coupled true vacuum. I do not have a volume-uniform estimate from the stated
inputs. No such estimate is inferred from the mere existence of finite
conditional gaps or from an auxiliary sampling-time interpretation.

There is a direct downstream use of VA10 in the existing Schur theorem.
If P=E_e eliminates one link and Q=I-P, then the actual centered full Q
form satisfies F_Q>=gamma_* Q, so ||F_Q^-1||<=gamma_*^-1 independently of
volume. This discharges that theorem's fast-inverse existence/floor input
for this split. It does not discharge its intrinsic score budget: with
s_y=partial_y log rho_e and coarse metric A=2epsilon I, the additional
relative estimate is on A^(1/2)E(s s*)A^(1/2) against the Q energy. VA4
bounds the density oscillation, not its connected coarse derivatives.
The localized fixed-block score result supplies those derivatives only in
its stated geometry and energy region. In particular, the uniform but
exponentially weak gamma_* cannot be inserted as if it implied a small
Schur loss or the required relative-gap matching error.

For spatial continuum passage, restore the physical clock at each spacing
a and in addition require a positive lower bound on

    gamma_*(a)/C_AT(a),                              (VA15)

in that clock, together with continuum observables, a complete retained
shell/source frame and the existing matching budgets. VA10's constant is
exponentially small in k/epsilon; calling it volume uniform does not make
VA15 follow. Existing marked-shell and relative-gap transport theorems can
be invoked only after their actual interacting source hypotheses hold.

There is a further definite obstruction to using this particular floor for
the continuum. Suppose the physical-clock coefficients obey

    epsilon(a)=c_E g(a)^2/a, k(a)=c_B/[a g(a)^2],
    g(a)^2 ~ 1/[b log(1/a)], c_E,c_B,b>0.

This is a conditional test of a logarithmic trajectory, not a derivation
of asymptotic freedom. Substitution in the proved VA10 floor gives, with
ell=log(1/a),

    log gamma_*(a)
      = -16(c_B/c_E)b^2 ell^2 (1+o(1)) + ell + O(log ell),
    gamma_*(a) -> 0.                                 (VA17)

Moreover every permissible C_AT on these lattices is at least 1/4.
Choose a nonconstant gauge-invariant four-link plaquette function f. Its
conditional variance is zero outside those four links, and each remaining
expected conditional variance is at most Var_mu(f). Thus VA14 implies
Var_mu(f)<=4 C_AT Var_mu(f). Consequently gamma_*/C_AT<=4 gamma_* tends
to zero on the stated trajectory, even if volume-uniform tensorization
were supplied. This excludes the present crude local floor as a positive
continuum certificate; it does not exclude a physical continuum gap.

The two next derivations are therefore distinct: establish the connected
physical variance/score bound at fixed coefficients, and improve the local
or physical-block coercivity before inserting it into the physical-clock
matching iteration. VA10 discharges finite-spacing inverse existence;
VA17 shows exactly why that alone cannot discharge continuum transport.

The proposed block replacement can be stated precisely. For a covering by
link sets B, let m_* be the maximum number of blocks containing any link,
E_B the true conditional expectation integrating B, and G_blocks=sum_B(I-E_B).
If their conditional Dirichlet gaps are bounded below by gamma_B>=gamma_min,
then summing the block energies counts each link at most m_* times and gives

    Omega^-1(H-E0)Omega >= (gamma_min/m_*) G_blocks,
    gap_phys(H) >= (gamma_min/m_*)(1-kappa_blocks)     (VA19)

provided the actual physical projection-angle row sum is at most
kappa_blocks<1. This follows by the same two-projection argument as VA12;
the common kernel is constant because the blocks cover every link.
For |B|=r and p_B touching plaquettes, VA4 and the product-Haar gap 3 give
the proved conditional bound

    gamma_B >= 3 epsilon (3/5)^(2r) exp(-4k p_B/epsilon).

This is a true-vacuum bound uniform in the outside configuration. It is
not a gap of an isolated cube with a different measure. It retains the
continuum loss of the preceding comparison. Replacing it by a numerical
isolated-block eigenvalue needs a separate conditional comparison theorem.
The choice of blocks, covering multiplicity, and their actual conditional
angles must all be specified; center separation alone is not separation of
the link supports of neighboring blocks.

This is the new proof boundary after replacing, not repeating, WR26.
The supplied Jaffe--Witten PDF, p.11 section 6.5, specifies the unmet target:
“One must then verify the existence of limits of appropriate expectations of
gauge-invariant observables as the lattice spacing tends to zero and as the
volume tends to infinity.”
