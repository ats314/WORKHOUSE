# Operator audit of the September 9 GPU resolution runs

9 September 2026. The original scripts and JSON reports in
`runs/gpu_yangmills_millennium_resolutions_2026-09-09/` are preserved unchanged.
The eight Phase 1--4 files first inspected matched their supplied hashes.
Phase 5 subsequently appeared; its two files and the updated ten-file
manifest are also hash-checked. Phase 5 has the separate source-level audit
GA10 below; its eigenvalue scan is not independently replayed here.
No walkthrough.md was present in that run directory.
The user subsequently supplied the original walkthrough at
`C:/Users/Alex/.gemini/antigravity/brain/443680f7-da95-4547-9453-e97ea7042693/walkthrough.md`.
It was read and matches the pasted attachment after newline normalization.
Its original SHA256 is
`5b086225edcaa727435060e80c250b935b81e25999c2245a38fb89cb8502abf4`.
Its Phase 6 formalization claims are audited in section GA6 below.

The numbers are audited against the *operators actually constructed*.
Independent Fourier sums and tridiagonal Sturm calculations reproduce the
156 reported Phase 1--4 quantities without the GPU, within explicit
tolerances in `docs/validation/yangmills-gpu-audit-2026-09-09.json`.
Exact algebra checks have narrower scopes
than the analytic infinite-volume statements below.

## GA1. Phase 1 is a massive scalar model with an exact uniform theorem

The code sets m_fast=1.5, builds a two-dimensional scalar periodic Laplacian
Delta, and defines

    F0=-Delta+m^2 I, d_g=(g/4)|Delta|, Fg=F0+d_g,
    m=3/2, z=0, source=one lattice-site delta.

For L>=3 write K=-Delta with spec K in [0,8]. Entrywise absolute value gives
|Delta|=8I-K, so D=|Delta|/4=2I-K/4 and

    Fg=(1-g/4)K+(m^2+2g)I.                           (GA1)

These matrices commute and contain no SU(2) link variables, gauge projection,
physical vacuum subtraction or construction of the complete Wilson force
Q W1 J_z. Calling d_g a non-Abelian perturbation in a comment does not add
these structures to GA1. The positive fast mass was inserted, not derived.

There is nevertheless a stronger result than the sampled volume scan.
For g>=0 the exact multiplier of R0 d_g Rg is

    g(2-lambda/4)/[(m^2+lambda)(m^2+lambda+g(2-lambda/4))].

It increases with the nonnegative numerator parameter and decreases with
m^2+lambda. Its maximum is attained at lambda=0. Hence, for every volume
and every unit vector t,

    |<R0 t,d_g Rg t>|
       <=2g/[m^2(m^2+2g)] <=(32/81)g.                (GA2)

This proves the model's uniform linear bound for all g>=0, not only seven
sampled couplings. It does not identify its operators with those in W6.

For 0<=g<=4 put t_g=1-g/4, mu_g=m^2+2g. Exponential conjugation by graph
distance changes the real part of Fg by at most
4t_g(cosh eta-1). At eta=2 asinh(m/4), this is at most m^2/2. The accretive
inverse bound therefore proves

    |Rg(x,y)| <=(2/m^2)exp[-eta dist_L(x,y)].          (GA3)

This supplies a uniform Combes--Thomas type estimate for the coded model.
It explains its stable numbers without supplying the missing actual-Wilson
fast gap, conjugation estimate, force identification or source-frame norm.

The reported 0.052982 is a maximum over sampled couplings for one site
source, not an operator norm or an established supremum over all g. At
g=1/10 a normalized spatially constant vector gives

    |<R0 t,d_g Rg t>|/g =160/441 > 0.053.             (GA4)

Thus even the coded model needs a source-range/weight argument before the
sampled constant can be used for the complete-space matching budget.

## GA2. Phase 2's alleged domino is an exact tensor sum

Let h(c,v) denote the truncated class-rotor matrix with diagonal
c n(n+2)+v and off-diagonal -v/2. The actual builder adds

    kin_shared=(epsilon/4)[n1(n1+2)+n2(n2+2)].

Consequently, for every cutoff, its matrix is exactly

    H_code=h(5epsilon/4,v) tensor I
                     +I tensor h(5epsilon/4,v).      (GA5)

There is no mixed kinetic derivative and no inter-plaquette interaction.
The reported positive difference is

    F_code=2[E0(5epsilon/4,v)-E0(epsilon,v)],          (GA6)

which compares two different electric coefficients. It is not the WR26
frustration of the actual shared-link Hamiltonian.

The omission has an explicit witness. With T_a=i sigma_a/2 and
chi(U)=Tr U, the true cross derivative obeys

    sum_a (L_a chi)(U1)(R_a chi)(U2)
      =-(1/2)Tr(U1 U2)+(1/4)Tr U1 Tr U2
      =sin(theta1)sin(theta2)n1.n2.                   (GA7)

This function is invariant under simultaneous conjugation and is nonzero;
its squared product-Haar norm is 3/16. It is orthogonal to all products of
individual class functions, since independent axis averaging kills n1.n2.
The 25-by-25 product-character basis therefore omits physical angular
channels reached by the actual shared-link operator. The established
seven-edge strip Hamiltonian and complete source construction in the
September 5 notes retain this term.

There is a second representation issue. The script sets nu_i=|Psi0_i|^2
in the *character coefficient basis* and multiplies f_i componentwise.
That defines a valid finite weighted matrix/Doob form. It does not compute
the configuration-space integral epsilon integral |grad f(U)|^2
|Omega(U)|^2 dU; multiplication of configuration functions is not diagonal
in the character basis. The finite spectral Rayleigh bound follows for
all vectors from diagonalization of H_code, independently of the five
random trials. It establishes neither the missing angular sector nor
cutoff, volume or continuum uniformity. The output flag
poincare_bound_verified is hard-coded True rather than accumulated from
the five individual tests.

The true ground-state transform is mathematically valid and is already
used in VA9--VA11 of `wilson-vacuum-aligned-assembly.md`. It removes an
extensive penalty from the *representation of the centered form*. It does
not change the previously defined number E0-sum e_* into zero or prove the
remaining uniform conditional-projection assembly estimate.

## GA3. Phase 3 compares two radial discretizations, not a transfer matrix

The script diagonalizes two 1000-point tridiagonal differential matrices.
It never constructs or diagonalizes a Wilson/Luscher transfer matrix T.
The code's physical matrix is

    -.5 D2 + diag[-1+(beta/2)(1-cos theta)].

For its stated c=1/2 the correct Haar-conjugated constant is -1/2, not -1.
This shifts absolute energies by 1/2 and leaves the reported gap unchanged.
The diffusion matrix is the conjugated classical Wilson Langevin operator.
These two weights are not identified with each other by taking a ratio of
their first gaps.

The archived ratio at beta=32 is 0.9309624382138295, not 1.000. The printed
statement of a limit is not an additional measurement. Near the identity,
the two local harmonic models do have first radial gaps sqrt(2 beta) and
2 beta. This explains a possible limiting first-gap ratio of one under
the chosen constants, without proving spatial continuum passage.

It also cannot identify whole operators: at radial excitation number n,
those harmonic excitation energies are n sqrt(2 beta) and 2n beta.
Dividing the first by the square root of the second gives sqrt(n), not one
for all n. Nor is tau=t^2 a physical semigroup clock: exp[-(s+t)^2 L] is
not exp[-s^2 L]exp[-t^2 L] on a nonzero eigenmode.

Working with the established physical Hamiltonian and its exp(-tH)
semigroup does avoid a stochastic-time inference. This is the existing
Hamiltonian route, not something established by the script's ratio.
Identifying a finite-step Wilson transfer matrix with the desired
Hamiltonian still uses the existing transfer/matching hypotheses.

## GA4. The additional Phase 4 has a valid conditional scalar limit

The new script inserts Delta0=1.25, f_j=2.5/a_j, a_j=2^-j and
eps_j=.053 g_j^3, with a one-loop running formula for g_j. None is obtained
by coarse-graining the Phase 2 or actual Wilson operators. In particular,
equation GA4 prevents using .053 as an unrestricted norm bound even for Phase 1,
and the initial running g0=2.586... exceeds that phase's sampled maximum .8.
Substituting the proved source-independent GA2 constant into the code's
eps0=C g0^3 gives approximately 6.83575, greater than one. Even the sharp
constant at that g0 gives 2.07202. Therefore this all-source substitution
cannot justify a positive first-step alpha0. A special source-range bound
or a separately controlled starting scale would have to be proved.

The telescope arithmetic is valid *conditional on its inputs*. Write

    eps_j=C(ell+j h)^(-3/2),
    ell=log 5, h=log 2, C=.053(2b0)^(-3/2),
    A_J=product_(j<J)(1-eps_j),
    B_J=Delta0^-1+sum_(j<J) A_(j+1)/f_j.

Here eps0<1 and sum eps_j is finite. Hence A_infty>0, B_infty<infty and
the scalar sequence Delta_J=A_J/B_J has a positive limit. This can be
proved rather than inferred from twenty steps. For J>=0 put

    I_J=2C/[h sqrt(ell+Jh)], S_J=I_J+eps_J.

Integral comparison and logarithmic product bounds give

    A_J exp[-S_J/(1-eps_J)] <= A_infty <= A_J exp[-I_J],
    B_J <= B_infty <= B_J+.8 A_J 2^-J.                (GA8)

These give explicit positive bounds on the scalar infinite limit. The
reported Delta20=.0054034556 is a finite iterate, not that limit. At J=20,
the analytic lower and upper formulas for Delta_infty evaluate to
approximately .0012689363 and .0013682341. These decimal evaluations are
diagnostics, not outward-rounded interval arithmetic. No
Wilson continuum measure or matching/source estimate is supplied by GA8.

The claimed 2x2 cluster again factorizes. Each plaquette appears in two
listed shared pairs, so the implemented matrix is

    H_2x2_code=sum_(i=1)^4 h_i(3epsilon/2,v).          (GA9)

Its actual dimension is 7^4=2401, not the comment's 4^4=256. There is no
shared-link cross derivative. The equal first excited energies in the
output are the degeneracy of exciting one of four identical independent
factors, not evidence that the omitted interaction has been controlled.

## GA5. Phase 5 keeps an admissible cube basis but changes its magnetic operator

The later cube script correctly enumerates 1013 admissible trivalent
spin assignments with 2j in {0,1,2}. Unlike Phase 2, this is a link-spin
basis. Its electric diagonal also has the stated sum j(j+1) convention.
The magnetic loop matrix, however, assigns the same -v/8 to every allowed
four-link shift. The following two-channel calculation tests that assignment
without depending on a choice of overall magnetic normalization.

Take two adjacent cube faces sharing link U. After grouping their other
three-link products as A and B, their character product is

    F(A,U,B)=chi(AU)chi(U^-1 B).

The three groups A,U,B are independently Haar distributed. Character
orthogonality gives ||F||^2=1 and the projection onto shared-link spin zero is

    P_(j_U=0) F = integral F dU = chi(AB)/2,
    ||P_(j_U=0)F||^2=1/4,
    ||P_(j_U=1)F||^2=3/4.                            (GA10)

The last equality uses 1/2 tensor 1/2=0 direct-sum 1. With the six outer
links in spin 1/2 there is a unique intertwiner at each trivalent vertex
for either shared spin. Thus these are exactly two normalized spin-network
channels, both present in the code's cutoff. Multiplication by the adjacent
plaquette trace on the initial fundamental loop must have amplitude
magnitudes in ratio sqrt(3), whereas the code assigns ratio one. Overall
normalization, phase conventions, or adding a constant to H cannot fix
that ratio. The source needs the actual SU2 recoupling matrix elements.

There is also a spectral-selection problem independent of GA10. The code
uses argmax of the overlap with each trial source, not the lowest nonvacuum
energy in a complete symmetry sector. Its own v=3 report has selected
tensor energy 2.6191346355 below selected scalar energy 3.4582997342.
Consequently its quantity called scalar mass cannot equal the full gap
there, even for its coded operator. At finite cubic spacing A1g and Eg
are cubic representations; continuum spin assignments require an additional
continuum identification. The valid basis enumeration is retained; neither
the magnetic operator nor a complete physical shell is certified by it.

## GA6. What the supplied Lean additions actually formalize

The outside work subsequently supplied five new declarations in Basic.lean.
They are retained, and registered under their literal statements. Their
comments have been corrected without changing the proof terms or statements.

`groundStateDirichlet_const` proves zero Dirichlet energy for constant test
functions. `ground_state_frustration_elimination` assumes a finite symmetric
matrix and an eigenvector equation and concludes

    finiteMatrixForm H psi - E sum_i psi_i^2 = 0.     (GA11)

There is no e_* in its statement. It even holds for excited eigenvectors;
it is not a characterization of a ground state or of a positive gap.
For example, H=[1], psi=[1], E=1 and a putative baseline e_*=0 satisfy
GA11, while E-e_*=1. Thus GA11 cannot imply the distinct assertion F=0.
The useful exact excited-state ground transform was already formalized in
`finite_ground_state_eigenform_identity`; physical uniform coercivity is
the additional VA14 input, not a consequence of substituting f=1.

`geom_sum_mul_sub` and `combes_thomas_geometric_bound` prove the geometric
identity and its positive finite-sum bound. The last new theorem,
`combes_thomas_pairing_volume_independent`, assumes literally

    hR : forall j in Finset.range n, |R j| <= C * rho^j

and proves sum_(j<n)|R j|<=C/(1-rho), with 0<=rho<1. It defines no
Wilson operator, inverse or dressed source. Its parameter g is unused,
and its conclusion is an absolute scalar sum, not a bilinear pairing.
The missing W6 derivation is precisely the actual-operator decay and
source estimate needed to supply such an hR with the required uniform
constants and norms. Compilation certifies the displayed conditional
statement; no conditional premise is silently promoted to a theorem.

Build and axiom diagnostics are recorded in the vacuum-assembly validation
report alongside, but separately from, the analytic infinite-volume proofs.

## GA7. The incoming smearing script measures spatial power, not spectral overlap

A later file, `phase6_smeared_spectral_bridge_g18.py`, appeared while the
graph was regenerating. This computational Phase 6 is distinct from the
walkthrough's Lean Phase 6. The updated twelve-file manifest is verified.
Its random-field smearing trajectory is not independently replayed here;
the source and its JSON summary are inspected directly.

The initializer samples independent near-identity link fluctuations. There
is no sampling from Omega^2, Hamiltonian construction, transfer correlation
or ground/excited eigenvector in the measurement. The returned statistic is

    Z_FFT = sum_(k!=0) |W_hat(k)|^2 exp[-|k|^2/(2m^2)]
                       / sum_(k!=0) |W_hat(k)|^2,
    m=1.2/a.

It is a spatial low-momentum power fraction. With k=2pi n/(La), the inserted
1/a in m cancels exactly, so its filter is independent of a. All excitation
energies at a given spatial momentum remain indistinguishable to this
statistic. It cannot supply |<Phi_exc,O Omega>|^2 or a complete source Gram
bound without a new operator and measure identification.

There is an explicit bound on the stated volume test. Since the zero mode
is removed and every nonzero Fourier mode on the L=8 torus has |ka|>=pi/4,

    Z_FFT <= exp[-25 pi^2/1152] = .807199747... < .85. (GA12)

This holds for every nonconstant field in exact arithmetic, at every number
of smearing steps. An exact rational check already proves the strict .85
bound: pi>3 and exp(x)>=1+x give an upper bound 128/153<17/20. When the
power is below the code's threshold it instead returns zero. Thus its
claimed >=85 percent uniform result is impossible for its L=8 statistic.

The archived volume maxima are .5829956, .7415053, .8234238 and .8187607
for L=8,12,16,24; every one is below .85. The JSON's contrary conclusion is
hardcoded. Its bare fractions are about .12--.13, not the asserted <.04.
Its spacing scan keeps L=16 and beta=4 fixed and increases the number of
smearing steps; the physical box size La shrinks. The first two spacing
rows are labelled LOW, and the last is .9009996. These are smoothing
diagnostics, not continuum quantum-vacuum spectral-overlap estimates.

## GA8. The later G17 script inserts both its cluster coefficients and its mass

The further incoming `phase7_kotecky_preiss_g17.py` is also source-audited.
The current fourteen-file archive manifest is verified. Its scalar ratio
is x/(1-x), with x=38 beta exp(1)/4. The exact scalar condition ratio<=1
is beta<=2/[38 exp(1)], approximately .0193621. No actual polymer weights,
connected character integrals or Wilson partition function are constructed.
The JSON's hardcoded assertion of convergence through beta=.038 conflicts
with its own computed ratio 52.4751925 at that beta.

The claimed free energy is the inserted finite formula

    sum_(n=1)^8 [38^(n-1)/n!](beta/4)^n
                 [1+1_(n>=L) exp(-L)].

For L>8 it is literally independent of L, because the wrapping branch never
executes. Numerical equality between L=32 and L=64 therefore tests this
formula, not the Wilson log partition function or its remainder.

The correlation generator inserts m_true=1.25 at beta=2 and samples a
Gaussian scalar field with covariance G=(-Delta+m_true^2)^-1, then sets
P=field^2. This is not a Wilson link ensemble. Its exact uncentered-field
connected covariance is 2G(r)^2 by the Gaussian fourth-moment identity.
Subtracting the spatial sample mean, as the code does, instead yields

    E[(P_x-P_bar)(P_y-P_bar)]
       =2G(x-y)^2-(2/N)sum_z G(z)^2.                 (GA13)

This subtraction explains a nonzero negative finite-volume bias at long
distance. Selecting only positive noisy values for a logarithmic fit does
not prove an exponential upper bound. When fewer than three points survive,
the code returns m_measured=m_true without a fit; this occurs in its L=8
data. The value .0612 at L=64 is a fit to this Gaussian diagnostic, not a
derived Yang-Mills mass. The valid geometric-sum algebra and Gaussian
covariance identities are retained, with their actual inputs explicit.

## GA9. Phase 8 supplies an assumed block kernel, not conditional projections

The isolated `phase8_approximate_tensorization_va12.py` and its JSON were
read after the shared-ledger edit pause. Part 1 samples the classical
single-plaquette weight exp(beta Tr(U_p)/2) and bins one staple scalar. It
does not form E_e E_f-E_ef or an operator norm in the true quantum vacuum.
Its reported charged value 1.2844 also exceeds the maximum possible
projection-angle norm 1: the measured maximum binned response is a different
quantity. The analytic isolated-cycle statement VA13 remains valid.

Parts 2 and 3 assign M=2.1939 and C_0=.50, then evaluate the scalar kernels
C_0 exp(-M r) and C_0 exp(-2M|n|). No coupled-vacuum measure, conditional
integration, projection matrix or operator-norm maximization occurs there.
The single-link scalar sum is 1.0598751; the block scalar sum is .0528531,
not the .0431 in the script header. The former is an upper-bound failure
if the kernel is assumed as an envelope, not proof that actual kappa>1.

There is a rigorous infinite-volume scalar result available from these
inputs. Since |n|_2>=|n|_1/sqrt(3), put q=exp(-2M/sqrt(3)); then

    (1/2) sum_(n in Z^3, n!=0) exp(-2M|n|_2)
       <= (1/2) [((1+q)/(1-q))^3-1].                 (GA14)

For the assigned M=21939/10000, 2M/sqrt(3)>5/2 and exp(5/2)>12,
so q<1/12 and the right side is less than 433/1331<1. Thus this
scalar envelope has a strict infinite-volume budget without relying on
a finite cutoff. Identifying it as an envelope for the actual block
projection angles is exactly the premise still required.

Part 4 assigns gamma_block=2.483202 from the Phase 2 tensor-sum model.
It supplies no true-vacuum conditional block estimate. VA19 states the
correct conditional block theorem, including the covering multiplicity
and the block floor obtainable from the already proved density bound.
The M=.8 scenario has scalar kappa=2.7682279>1 and computed gap=-4.3908670;
the final hardcoded PASS therefore contradicts this scenario's own output.
Neither the successful scalar budgets nor that failing scalar scenario
determine the actual interacting Wilson gap.

Five further quantitative facts about the same file are recorded here,
because each one bears on how the reported numbers should be read.

First, Part 1's statistic is exactly zero as a population statement, for a
reason that involves no lattice. Write S=q2 q3 q4. For each fixed S the map
q1 -> q1 S preserves Haar measure, so U_p is Haar and independent of S; the
weight is a function of U_p alone, so the reweighted conditional law of U_p
given S does not depend on S. Hence for every centered class function f,

    E_w[f(U_p)|S]=E_w[f(U_p)]=0.                      (GA15)

The reported .1051181855075641 is therefore the sampling error of an exact
zero, not a small measured angle, and the print label "(Identically 0)" is
attached to a %.2e field that renders it 1.05e-01. An independent replay of
the same statistic gives .0560 at 2*10^5 samples, .0236 at 2*10^6 and .0072
at 2*10^7: the n^(-1/2) decay of a Monte-Carlo zero. Read instead at face
value, .1051 would fail the criterion outright, since the row sum multiplies
it by the coordination number. It is not read either way: max_dev_phys occurs
only in the print at line 104 and the results dict at line 109, and Parts 2 to
4 take the literals instead. Part 1 therefore neither supports nor is used by
what follows.

Second, the single-link defect is a choice of amplitude at the third
decimal. Its closed form is 12 C_0 q(1+q)/(1-q)^3 with the r=1 shell
replaced by 12 C_0 q; the r=1 term alone is .6688867399152452, 63.1 percent
of the total 1.0598751292540503. Holding M fixed, kappa_single=1 already at

    C_0=.47175368701396414, and at M=2.2335482877424226
    holding C_0=.50 fixed.                            (GA16)

A 5.7 percent smaller amplitude, or a 1.8 percent larger mass, and the
criterion this script calls a defect would have passed at a single link.
The volume uniformity in Part 3 is likewise the tail of a rapidly convergent
lattice sum rather than a proved uniformity: at M=2.1939 the L=8 box already
agrees with the infinite sum to 2.7*10^-5 and the L=16 box to 6.8*10^-9.

Third, the block geometry is asserted rather than derived, and the margin
depends on it. The block sum runs over Z^3 and the single-link shell count
12 r^2 is a three-dimensional count. That is defensible in the Hamiltonian
formulation, whose spatial lattice is three-dimensional and in which VA12
bounds gap_phys(H); the file never states the choice or its ground, and the
choice is quantitatively decisive. Under the same scalar ansatz on Z^4,
with shells 32 r^3 and block separation 2|n|_2,

    kappa_single=3.7277368217004136,
    kappa_block=.08671045222831368  (M=2.1939),
               =.4994513456079787   (M=1.5515),
               =8.756411538859295   (M=.8000).        (GA17)

The two passing scenarios survive the change and the conservative one fails
by an order of magnitude. The reported margin is therefore a property of the
assumed geometry as much as of the assumed envelope, and it is the envelope
premise, not the arithmetic, that would have to be established either way.

Fourth, the assembled chain is inconsistent with its own inputs. The script
reads M=2.1939 both as the physical glueball gap and as the decay rate of
the angles, and then concludes

    gap_phys >= gamma_block(1-kappa_block)=2.351957
                                          > M=2.1939, (GA18)

and 1.8487621549030637>1.5515 at its second coupling. A lower bound on the
gap inferred from a decay rate cannot exceed that rate when the rate is the
gap. This is a self-consistency failure of the assembly, independent of
whether the envelope premise holds.

Fifth, the assigned rates are relabelled from elsewhere in the run, and the
shell count is weaker than the criterion being discharged. Both are Phase 3's
delta_phys rounded to five digits: 2.1938796882942624 at beta=4 and
1.5515160971960493 at beta=1. Phase 3 diagonalizes a one-variable SU(2)
radial class-function discretization on theta in (0,pi), which GA3 already
records as comparing two radial discretizations and constructing no Wilson
transfer. Its first gap is imported here as the physical glueball gap and as
the spatial decay rate of the conditional projection angles, two roles it was
not computed in, and Phase 9 reuses it again as Delta_phys. The run's own
glueball spectrum, Phase 5, reports M(0++) between 2.6563646 and 4.2022981
across its whole coupling scan, so the glueball label is contradicted by the
run that supplied it. The shell branch the script names as the root cause of
the defect is a no-op, since its special case z(1)=12 equals the generic
12 r^2 at r=1. And VA18 fixes the shell form C_geom(r+1)^2, which at the
same assigned C_0=.50 and C_geom=12 gives

    kappa=C_0 C_geom[(1+q)/(1-q)^3-1]
         =3.5072160891245714,                        (GA19)

3.31 times the 1.0598751292540503 the script reports for its own weaker
12 r^2. Separately, VA17 proves that every permissible C_AT on these
lattices is at least 1/4, so the conservative branch's -.5655379641574655
is not a tensorization constant of any measure.

Every deterministic quantity in the file is now replayed in
`docs/validation/yangmills-gpu-audit-2026-09-09.json` under
`phase8_supplementary_ansatz_replay`: twenty-two comparisons covering
kappa_single, all fifteen block scans, the three infinite-volume sums and
the three assembled gaps, together with the thresholds and the
four-dimensional recomputation. What is reproduced is the arithmetic of the
ansatz. The estimate VA19 requires -- the actual conditional block angles,
with the block choice and covering multiplicity specified -- is not among it.

## GA10. Phase 9 verifies a Gram identity, an inserted exponential and a Haar moment

The further incoming `phase9_os_reconstruction_wightman.py` claims
Osterwalder--Schrader reflection positivity, exponential clustering, and
Wightman non-triviality S!=I. Each of the three is a statement about a typed
array. The eighteen-file manifest is verified.

The reflection matrix is built from a 6x4 table of hand-entered matrix
elements A[i][n], the energy list [0,2.1939,2.9250,3.5000] and six
observable times, as M_ij=sum_n A[i][n]A[j][n]exp(-E_n(t_i+t_j)). With
V[i][n]=A[i][n]exp(-E_n t_i) this is exactly M=V V^T, and the n=0 column of
A is identically zero. Therefore

    M is the Gram matrix of six vectors in a three-dimensional
    space: rank at most 3, three exact zero eigenvalues, and
    M>=0 for every choice of A, E and t.              (GA20)

The archived spectrum agrees. Its three entries -5.63*10^-20, -1.54*10^-21
and 2.04*10^-22 are roundoff of those exact zeros, and its three nonzero
eigenvalues reproduce the invariants of the 3x3 Gram matrix to 3.5*10^-18 in
trace and 1.9*10^-24 in determinant. The script's own comment states the
conclusion, that Gram matrices are always positive semidefinite, so OS2 is
asserted rather than tested. T_time=16, n_configs=5000 and beta=4.0 are
assigned in this part and never used; no gauge configuration, transfer
matrix or time reflection is constructed.

The clustering part evaluates S_2^c(t)=.85^2 exp(-2.1939 t)+.10^2
exp(-2.9250 t) for t=1..10 and stores plateau_mass=float(Delta_phys). All
ten archived values are reproduced to 10^-18. The reported plateau mass is
the inserted mass returned unchanged, and the effective-mass column is the
ratio of consecutive terms of a two-exponential formula.

The non-triviality part samples one SU(2) matrix, forms O=Tr U-<Tr U> under
the single-plaquette weight and reports S_4^c=m4-3 m2^2 != 0. That is the
excess kurtosis of Tr U for a single group element, and it is nonzero for
the free measure. At beta=0, Tr U=2u_0 with u_0 semicircular of density
(2/pi)sqrt(1-u^2), so E[u_0^2]=1/4 and E[u_0^4]=1/8 give

    m2=1, m4=2, S_4^c=-1 exactly at beta=0.           (GA21)

The coded criterion |T|>10^-4 is therefore met by Haar measure with no
interaction at all, and at beta=1 the same statistic is negative. The
reported T_matrix_element=26.43883580325791 divides an eight-term geometric
sum built from S_4^c(0)exp(-2 Delta_phys t) by the square of the inserted
two-point sum. No Wightman function, Hilbert-space reconstruction or
scattering amplitude is constructed, and a nonzero one-variable fourth
cumulant is not the connected four-point function of a field theory. The
deterministic quantities are replayed under
`phase9_supplementary_typed_input_replay`; the beta=4 moments are
Monte-Carlo statistics with no stored seed and are not replayed.

The walkthrough supplied on 9 September, SHA-256
`f6452918246a2c4344de8f6f200f7562353ded05287715d584045e78818950da`,
adds Phase 8 and Phase 9 sections that restate these JSON files. Three
things about its presentation are recorded. It writes
c_ef^phys<=1.05*10^-1 -> 0 and glosses that as identical cancellation, so
the sampling error of GA15 is carried forward as a result. Its Phase 8 table
lists only passing scenarios and drops the M=.8000 row that the same script
computes with a negative constant and gap -4.3908670. And its Lean section
lists the eight declarations already registered above; none of them concerns
approximate tensorization, reflection positivity or a four-point function,
so neither phase has formal content behind it.

## Consequence for the active derivation

The updated pasted walkthrough was checked against this source audit. Its
SHA-256 is
`d6ae50fc0c198fbcb289c6e2af92d65c8f2422fe19e315e8ab775ad6658aa050`.
It adds the Phase 6/7 claims above and three further Lean declarations.
`kotecky_preiss_cluster_sum_bound` bounds a finite geometric sum;
`kotecky_preiss_polymer_activity_bound` substitutes rho=D*w and assumes
D*w<1; `polymer_free_energy_cauchy_bound` applies the triangle inequality
after assuming deviations from a common f_inf. These valid declarations
do not construct Wilson activities, prove the strict incompatibility
budget, or construct f_inf. All eight incoming declarations are registered;
the fresh build completed 3034 jobs and their axiom reports contain only
propext, Classical.choice and Quot.sound.

The archive supplies reproducible numerical controls and, via GA2--GA3
and GA8, provable statements about its scalar model and scalar iteration.
It does not discharge the operator identification in W6, the complete
physical source frame, or the interacting physical variance/angle estimate
VA14--VA16. The independent continuation has nevertheless replaced the
false WR26 target by exact vacuum-aligned conditional projections and
proved their volume-independent local Poincare floor.

The next unproved estimate remains the spatially summable physical
projection interaction (or the more general approximate tensorization
VA14). VA17 additionally proves that the present crude local floor tends
to zero on the stated physical-clock logarithmic trajectory. A sharper
local or physical-block coercivity estimate is therefore needed before
continuum matching. The numerical scripts above do not compute these
projections, this variance ratio, or the sharper physical bound.
