# Complete square-source currents and spectral totality

10 September 2026. Analytic continuation of the preserved 9 September actual
twelve-edge square calculation. The new contributions are an explicit current
for its complete first residual coefficient, the sharper constant below, a
conditional selected-inverse estimate without a separate diagonal estimate,
and a small-source totality bridge. None establishes the finite-coupling,
coupled-volume W6 remainder or a continuum Yang--Mills theorem.

The original square geometry, source-compatible unitary, complete operator jet,
and prior all-energy residual bound remain the inputs in
[source.md](../../runs/recent_research_integration_2026-09-09/sources/w6_square_block_20260909/source.md),
[residual_inverse.md](../../runs/recent_research_integration_2026-09-09/sources/w6_square_block_20260909/residual_inverse.md),
and [residual_all_energy.md](../../runs/recent_research_integration_2026-09-09/sources/w6_square_block_20260909/residual_all_energy.md).
The exact checker reconstructs the current and its moments from these inputs;
it does not merely evaluate the final constant.

The [reviewed theorem register](../../paper/research_notes/THEORY_CURRENT_BRIDGES_20260910.md)
records the integration's joint conclusions and their qualifications.

## SCB0A. Degenerate energy variational certificate

Let E,L be real Hilbert spaces, Y:E->L a bounded linear map, kappa>0,
and a[v]>=kappa ||Yv||^2. Suppose rho(v)=g<j,Yv>. Completing the square gives

    2rho(v)-a[v] <= 2g<j,Yv>-kappa||Yv||^2
                 <= g^2||j||^2/kappa.                    (SCB0A)

Indeed the last difference is ||g j-kappa Yv||^2/kappa>=0. This statement
allows a kernel of Y and requires neither an inverse nor a positive lower
bound against the original Hilbert norm. The relevant residual vanishes on
ker(Y) by its specified factorization. The same proof applies to a form-domain
map Y when every displayed pairing and form inequality is defined there.

## SCB0B. Bounded-inverse W6 composition

Suppose A is bounded self-adjoint with an actual bounded inverse R, its form
obeys <v,Av>>=kappa||Yv||^2, and the vector r represents rho. Evaluating SCB0A
at v=Rr gives

    <r,Rr> <= g^2||j||^2/kappa.

The existence of R is a hypothesis; no uniform bound on ||R|| is consumed.
For bounded self-adjoint A0,Ag with their actual two-sided bounded inverses
R0,Rg, put u=R0t and r=(Ag-A0)u. The variational identity is

    <t,(Rg-R0)t>=-<u,(Ag-A0)u>+<r,Rg r>.

If the actual residual has the current factorization of SCB0A, its current
obeys ||j||^2<=CJ b, the diagonal obeys |<u,(Ag-A0)u>|<=a|g|b, and
|g|<=g0, then

    |<t,(Rg-R0)t>| <= (a+g0 CJ/kappa)|g|b.                (SCB0B)

This composes an inverse-free energy inequality with an inverse-dependent
W6 identity. It does not formalize W6 for an operator lacking a bounded
inverse. The complete unbounded closed-form version requires its own
domain/weak-inverse realization, as retained in SCB3 and the earlier W6 source.

## SCB1. The complete first current in the actual square convention

Use the independent three-vectors q,u,s,v of source Q12--Q16. Their component
variances are sqrt(2), 1/2, 2, sqrt(6)/4, respectively. The electric cometric
and Gaussian precision are

    M0 = diag(4 Iq, 2 Iu, 8 Is, 3 Iv),
    G0 = diag((sqrt(2)/4) Iq, Iu, (1/4) Is, (sqrt(6)/3) Iv).

Thus mu0 is proportional to exp(-Y.G0.Y), and the ground-transformed
Gaussian form is ell0[h]=(1/2) integral grad(h)* M0 grad(h) dmu0. The checker
also obtains M0 by transforming the original four-by-four electric matrix;
the metric is not inferred from an unrelated oscillator convention.

Write [x]cross y=x cross y and retain the source's coefficients

    A=(2sqrt(2)-1)/7, B=(sqrt(2)-4)/14,
    C=(4-sqrt(2))/7, D=sqrt(2)/4.

Define a symmetric matrix field M1 by its nonzero upper off-diagonal blocks

    M1_qu=A[s]cross, M1_us=B[q]cross, M1_qs=C[q]cross,
    M1_qv=D[q]cross, M1_uv=-D[u]cross,                    (SCB1)

with the reverse blocks given by transpose. Each column divergence is zero.
The complete physical Q12 operator, including the ground and source jet, is

    W1tilde = -(1/(2mu0)) div(mu0 M1 grad).                (SCB2)

Indeed its principal part gives the five second-order terms in Q12; the
first-order term M1 G0 Y gives exactly their Gaussian conjugation terms.
There is no zeroth-order term since W1 Omega0=0. The equality is on the
physical polynomial core, where the supplied Gauss-divergence relations hold.

Put a=|q|^2, T=q.(u cross s), delta=(2-4sqrt(2))/7, m=4+sqrt(2), and

    f=phi', psi=(S+m)^(-1)f,
    S=-8a partial_a^2+(2sqrt(2)a-20)partial_a,
    u0=delta T psi(a), rho1=Q0 W1tilde u0.                (SCB3)

This uses the full inverse before estimating a source. It is the complete
Q16 residual, including the v-mode contribution. Define

    j1=(1/sqrt(2)) M0^(-1/2) M1 grad(u0).

For every physical fast core test h,

    <h,rho1> = <(1/sqrt(2)) M0^(1/2) grad(h),j1>,
    |<h,rho1>| <= sqrt(ell0[h]) ||j1||.                   (SCB4)

Projection Q0 disappears in this pairing because h is fast. The v component
of j1 is nonzero even though u0 does not depend on v. Omitting it changes the
current norm. A current is an admissible dual-norm bound; it is not asserted
to be the minimum-norm Hodge representative or the exact inverse energy.

## SCB2. Exact current moments and an all-source constant

Let cA=(9-4sqrt(2))/49 and cD=(159+11sqrt(2))/196. Exact fast Wick integration
and radial integration by parts give

    ||j1||^2 = delta^2 E[(cA a^2/4+cD a)|psi|^2
                                  +16cA a^2|psi'|^2].    (SCB5)

For reproducibility, before radial integration by parts the three coefficient
polynomials multiplying |psi|^2, Re(conj(psi)psi'), and |psi'|^2 are

    (cA/2)a^2+(279-124sqrt(2))a/196+15cA,
    ((8-9sqrt(2))/49)a^2+20cA a,
    16cA a^2.

The radial measure dmu is proportional to a^(1/2) exp(-a/(2sqrt(2))) da.
Integration of the middle coefficient cancels the constant term and gives
SCB5. The v-current is included throughout this computation.

Put dnu=a dmu, N=E[a|psi|^2], G=E[a^2|psi'|^2], I=E[a^2|psi|^2]. On the
positive radial Friedrichs realization, <psi,S psi>_nu=8G and

    I=5sqrt(2)N+4sqrt(2) Re E[a^2 conj(psi)psi'].

Cauchy--Schwarz and Young with parameter 1/12 imply

    I <= (60sqrt(2)/11) N+(1152/11) G.

Consequently, with

    Astar=cD+(15sqrt(2)/11)cA, dstar=(58/11)cA,

SCB5 is at most delta^2 <psi,(Astar+dstar S)psi>_nu. Both coefficients are
positive and 2Astar-dstar m>0. Therefore

    (Astar+dstar x)/(m+x)^2 <= Astar/m^2, x>=0.

Use this joint spectral bound, rather than separately maximizing its two
terms. Since psi=(S+m)^(-1)f and b[phi]=8||f||_nu^2, it proves

    ||j1||^2 <= Kstar b[phi],
    Kstar=delta^2 Astar/(8m^2)
         =(48213-16675sqrt(2))/20706224
         =0.0011895451748... <1/840.                     (SCB6)

SCB4 gives ||rho1||_(ell0*)^2<=Kstar b[phi], hence the same upper bound for
<rho1,F0^(-1)rho1>. The prior residual_inverse R7--R8 already gives an
all-source inverse bound below 1/512, with exact coefficient approximately
0.0018912324575; SCB6 improves that coefficient and supplies a first-order
current realization. It does not replace an old 1/256 bound while ignoring
the intervening sharper result.

The polynomial computation extends to every radial finite-energy source:
radial polynomials are a form core, S+m has its positive Friedrichs inverse,
and SCB6 makes the current map continuous in the retained form norm. For
complex sources the integrated cross term is its real part. No pointwise
derivative hypothesis on arbitrary form-domain sources is added.

## SCB3. A selected-inverse implication without a separate diagonal bound

Let a0,ag be positive closed fast forms with the required weak inverse
realizations, u0=A0^(-1)t in D(ag), wg=Ag^(-1)t, and

    S0=<t,A0^(-1)t>, Sg=<t,Ag^(-1)t>,
    rho(v)=ag[v,u0]-<v,t>.

Suppose S0<=C0 b and ||rho||_(ag*)<=epsilon sqrt(b), with b,C0,epsilon>=0.
Testing the actual residual against wg gives

    |Sg-S0| <= epsilon sqrt(b) sqrt(Sg).

Writing x=sqrt(Sg), y=sqrt(S0), the case x>=y gives x-y<=epsilon sqrt(b);
the other case already gives x<=y. Thus

    |Sg-S0| <= (epsilon sqrt(C0)+epsilon^2)b.             (SCB7)

No separate estimate of ag[u0]-a0[u0] is needed under these hypotheses.
This is a conditional finite-coupling theorem. A bound for rho1 alone is
not its residual hypothesis. For the square reference the supplied full
force gives C0=delta^2/(4m)=(44-25sqrt(2))/686, attained by phi'=constant.
Taking epsilon=O(|g|) yields an O(|g|) selected-inverse estimate only after
the full finite-g current/remainder and interacting coercivity are supplied.

## SCB4. Intrinsic score currents and exact centering corrections

Adopt the linked ground-marginal construction's hypotheses: A=A(U) depends
only on the retained coordinate, rho_U is the normalized actual conditional
density, and conditional differentiation and fiber integration by parts hold
on a common form core with justified boundary conditions. The displayed
Poisson solution/current and its finite weighted cost are assumptions. In
particular A grad f is fiber-constant; a fiber-dependent coarse cometric
would introduce an additional derivative term in the divergence calculation.

The [true marginal identity](../../paper/research_notes/G19_GROUND_MARGINAL_SCHUR_SCORE_20260905.md)
has s_a=partial_a log(rho)+div_rho(b_a). If

    -div_rho(S grad_F chi_a)=partial_a log(rho),
    J_a=S grad_F chi_a-b_a,

then s_a=-div_rho(J_a). For a retained f and a conditional-mean-zero v,

    h[f,v]=-(1/2) integral grad_F(v).J_(A grad f) dnu,
    |h[f,v]|^2 <= Jcost[f] ell_F[v],
    Jcost[f]=(1/2) integral J_(A grad f)* S^-1
                                     J_(A grad f) dnu.   (SCB8)

The difference defining J remains inside its squared norm. A minimum-current
construction may reduce the cost further; the explicit current suffices.
An explicit finite cost proves continuity in the vertical dual norm without
requiring a uniform conditional spectral gap. At zero spectral shift the
positive horizontal/vertical split supplies h>=ell_F. At positive shift the
separate lower-form coercivity must still be proved.

The supplied balanced strip connection has r_E=(7sqrt(2)/24)g[Q,E]+O(g^2),
A=6I+O(g^2), S=5I/2+O(g^2). Its geometric score is already a divergence,
so its current cost matrix is

    A^(1/2) r* S^-1 r A^(1/2)
       =(49/120)g^2 ad_Q* ad_Q+O_R(g^3).

For a single-block class-source direction this current vanishes exactly,
by the [centralizer identity](../../paper/research_notes/G19_TRUE_GROUND_LOCALIZED_WILSON_SCORE_20260905.md).
The parameter-density current is a separate obligation. The fixed-chart
statement does not control arbitrary retained backgrounds.

Two centering corrections are indispensable. If q=D_x* j, then

    c q=D_x*(c j)+j.D_x c.

The last term vanishes for a coefficient depending only on retained
coordinates, but not for a general inverse-smoothed source coefficient.
Likewise P_g r_g=0 gives P_g r'_g=-P'_g r_g. The anti-self-adjoint connection
K_g=[P'_g,P_g] makes r'_g-K_g r_g centered. This is the source-motion
commutator retained in [SP16](wilson-spatial-schur-excess.md), not a proof
that its all-volume source transport is spatially local.

The BA4 true conditional gap is uniform in volume and outside configuration,
but its reciprocal grows like exp(C/g^2) on k/epsilon proportional to g^-4.
It cannot absorb a merely polynomial weak-g residual estimate. The sharper
SC17 small-k/epsilon interval is a different regime. These observations
motivate explicit current bounds rather than a substitution of conditional
inverse estimates from an incompatible regime.

## SCB5. Tiny exponential sources imply totality by differentiation

Let mu be a probability measure and A a family of bounded real observables
whose centered span is dense in the intended vacuum-orthogonal Hilbert space.
For f in A put s_alpha(f)=exp(alpha f)-E exp(alpha f). If |f|<=B and alpha!=0,

    ||s_alpha(f)/alpha-(f-Ef)||_2
        <= |alpha| B^2 exp(|alpha|B).                    (SCB9)

This follows from the uniform Taylor remainder
|exp(alpha f)-1-alpha f|<=alpha^2 B^2 exp(|alpha|B)/2 and subtracting its
expectation. Hence any bounded operator killing s_alpha_n(f) for a sequence
of nonzero alpha_n tending to zero kills f-Ef. Density then kills the entire
operator on the intended vacuum-orthogonal space.

Assume an actual positive spectral representation for H>=0. For every such
f,n, suppose its centered exponential source has temporal correlation at
most A_fn exp(-m t), with a common m>0 and finite A_fn, at arbitrarily late
times. The prefactor, admissible small-tilt sequence, and onset of the time
bound may depend on the source. Positivity excludes spectral weight below
m for each source; SCB9 and density exclude the low-energy projection on
the whole intended space. Thus no uniform footprint radius or uniform
source prefactor is needed for this particular vacuum-gap implication.

The endpoint with bounds for all nonnegative times is already formalized in
[SpectralReconstruction.lean](../../lean/Workhouse/SpectralReconstruction.lean)
by total_family_spectral_projection_gap; the source-dependent late-time
version uses the same positive-measure argument along an unbounded sequence.
[SourceTilt.lean](../../lean/Workhouse/SourceTilt.lean) supplies the actual
centered L2 vector and vacuum orthogonality. The tangent/density composition
here is analytic unless separately registered with complete Lean coverage.

Gauge-invariant cylinders are dense in the physical space when the actual
compact gauge averaging/core construction applies, as in the supplied SC17
thermodynamic construction. For a charge-odd subspace additionally require
a commuting measure-preserving charge involution and project the cylinder
family there; for odd f, the projected exponential is sinh(alpha f).
An SU(2) physical-space argument is not an SU(3) odd-shell identification.
Plaquette traces alone are not assumed to be a total family. The checker
retains a finite dark-state example showing why totality matters.

## SCB6. Uniform normalized mesoscopic source amplitudes

For a finite footprint of size N>0 put X=sum_p V_p and K(s)=log E exp(sX).
Assume differentiation is justified and the actual tilted susceptibility
obeys K''(s)<=sigma N throughout the interval joining 0 to 2alpha. Then

    Y_alpha=exp(alpha X)/E exp(alpha X)-1,
    ||Y_alpha||_2^2=exp(K(2alpha)-2K(alpha))-1,
    K(2alpha)-2K(alpha)
       =alpha^2 integral_0^1 integral_0^1 K''(alpha(u+v))du dv.

Consequently ||Y_(t/sqrt(N))||_2^2<=exp(sigma t^2)-1, uniformly in N. A
matching lower tilted susceptibility kappa N gives the corresponding
lower bound exp(kappa t^2)-1. Untilted variance alone does not supply the
interval hypothesis, and this normalized source is distinct from the raw
fixed-alpha exponential whose radius obstruction is proved in
[SourceRadiusGrowth.lean](../../lean/Workhouse/SourceRadiusGrowth.lean).

## Verification and outstanding realization

Run `python -B scripts/verify_source_current_bridges.py` for exact controls
and source fingerprints; the default command writes only to standard output.
The controls cover the transformed cometric, full polynomial operator action,
current moments, radial integration by parts, rational constant bounds,
scalar inverse algebra, projection/source centering, and a totality negative
example. They do not machine-certify unbounded-domain closure, the physical
spectral representation, actual tilted susceptibility, or continuum limits.

The remaining W6 task is the complete finite-g source current and its
remainder, with a common lower energy and a retained-source budget uniform
in the required volume, background, spectral interval, and coupling range.
The current/Hodge geometric refinements in the companion graph must be used
with their actual source metric. A positive common physical decay rate and
nonzero limiting source measures remain separate continuum inputs.
