# An interacting angular-energy window beyond the two-strip calculation

10 September 2026. G19 continuation from the W6 soft-residual investigation.
Analytic theorem for the specified coarse-interacting Gaussian-fiber reference
package; application to the complete nonlinear Wilson family remains conditional.
No literature-priority claim. The new result is the interaction-stability window
and its symmetry-sector refinement, not the previously established 11/80 coefficient.

## Source and advance

`paper/research_notes/G19_WILSON_STRIP_BO_AND_TWO_STRIP_SPLITTING_20260905.md`,
sections 5-6, already proves that the actual two-strip first coupling is

    W P psi = k sum_(i,a) Z_(i,a) L_(i,a) psi Phi,
    k=7/(2 sqrt(10)),   L_i=[Q_i,grad_Qi],

and that the direct angular correction is (3/4) sum_i ||L_i psi||^2.
The fiber covariance is <Z_(i,a) Z_(j,b)>=delta_ij delta_ab beta/2,
where beta=sqrt(5). On an uncoupled coarse oscillator eigenspace, L_i
preserves coarse energy; the negative exchange coefficient is 49/80,
leaving 3/4-49/80=11/80. The source explicitly does not establish a uniform
interacting-block theorem. Its local O(g^4) mechanism is also already present.

We replace the uncoupled coarse oscillator by a possibly interacting H_c.
The exact first-fiber-chaos inverse can still be computed without a product
coarse ground state and without requiring [H_c,L_i]=0. A quantitative lower
bound then preserves a positive part of the angular correction.

## 1. Exact elimination with an interacting coarse Hamiltonian

Let there be M fibers with d=dim su(N) coordinates each. Let H_c be
self-adjoint, bounded below, on the coarse space. The reference is

    H_ref = H_c tensor I + I tensor H_f,

where H_f is the sum of M isotropic fiber oscillators, ground energy
subtracted, with first excitation beta=sqrt(5). Let Phi be its normalized
product ground, P=I tensor |Phi><Phi|, Q=I-P. Let L_(i,a) be the actual
coarse angular generators on a common dense invariant core. Extend identities
to the domain with sum_(i,a)||L_(i,a)psi||^2 finite by continuity of the
quadratic forms. Assume the complementary inverse exists on the symmetry
sector in use. This is a second-order coefficient identity; construction of
a full self-adjoint nonlinear H_ref+gW+... is not inferred from it.

The image WP lies wholly in first fiber chaos. H_ref preserves that chaos,
and its restriction there is H_c+beta on each of the Md orthogonal labels.
Consequently, exactly,

    <WP psi, (Q(H_ref-E)Q)^(-1) WP psi>
      = (49 beta/80) sum_(i,a)
          <L_(i,a)psi,(H_c+beta-E)^(-1)L_(i,a)psi>.       (A1)

One can equivalently define A1 just on the invariant first-chaos range if
the full complementary inverse is unavailable; in that case it is not
claimed to be a full Feshbach coefficient. In the application in section 3,
the full physical-even complement has a positive floor, as checked there.

Proof of the constant: k^2=49/40 and ||Z_(i,a)Phi||^2=beta/2.
The remaining cross terms vanish by orthogonality of fiber labels, irrespective
of the coarse correlations. No sum over absolute spatial correlations and no
factor M is introduced. This establishes a complete synthesis-form identity,
not separate estimates on selected columns.

Define the angular part of the second-order effective form by

    A_E[psi] = (3/4) sum ||L_(i,a)psi||^2 - RHS(A1).     (A2)

The actual correction in the rescaled Hamiltonian is g^2 A_E. Other direct
second-order coefficients, nonlinear remainders and moving-source terms are
not part of A2.

## 2. Uniform positivity in a source-sector energy window

Suppose a reducing coarse subspace K contains every L_(i,a)psi under
consideration, and H_c|K >= E_* I. Write delta=E-E_*. If delta<beta,
spectral order in A1 yields

    A_E[psi] >= c(delta) sum ||L_(i,a)psi||^2,
    c(delta) = 3/4 - 49 beta/[80(beta-delta)]
             = (11 beta-60 delta)/[80(beta-delta)].     (A3)

Thus c(delta)>0 precisely when delta<11 beta/60. A non-strict inequality
gives nonnegativity at the endpoint. If E<=E_*, at least the original 11/80
survives, even when H_c is interacting and does not commute with individual L_i.
The same statements hold for every M with unchanged coefficients.

Without a useful K one may use E_*=inf spec H_c. For the first physical
excited band that crude bound is inadequate. The following symmetry argument
provides the useful E_*. The delta threshold is optimal for the information
H_c|K>=E_* alone: an angular source lying in its bottom eigenspace saturates
the inverse bound. This is an off-shell statement, not a classification of
which energies are actual physical eigenvalues.

## 3. Complete first even physical band under coarse interactions

Take M>=2 and

    H_osc = sum_i[-(3/2)Delta_(Q_i)+|Q_i|^2/2],
    alpha=sqrt(3),   E_base=M d alpha/2,
    H_c=H_osc+V,     ||V||<=v.

Here V is any bounded self-adjoint interaction commuting with simultaneous
Ad(SU(N)) and with joint inversion Q_i -> -Q_i. It need not be a sum of
independent terms and need not commute with individual L_i. A scalar shift
of V can be absorbed in energies; the optimal v for these estimates is
half its spectral width when that width is finite.

For a physical even psi, each L_(i,a)psi lies in the even adjoint isotypic
subspace: the generators transform covariantly as the adjoint, preserve
joint inversion, and psi is invariant. This subspace reduces H_c.
In H_osc there is no adjoint at degree zero; degree one is odd. Every even
adjoint therefore has at least two quanta, so

    H_c|K_even,adj >= E_base+2alpha-v.                 (A4)

The physical even first excited band originates at degree two, of dimension
M(M+1)/2: the quadratic invariants Q_i.Q_j, with the diagonal constants
subtracted against the vacuum. The next even degree is at least four.
Min-max in the physical-even sector bounds the entire perturbed degree-two
cluster above by E_base+2alpha+v; the vacuum lies within E_base +/-v.
For v<alpha these clusters remain separated from one another and from
the higher even spectrum. The degree-two cluster can split internally.

For every spectral parameter E in this complete perturbed cluster, A4 gives
delta<=2v. Hence

    A_E[psi] >= [(11 beta-120v)/(80(beta-2v))]
                   sum ||L_(i,a)psi||^2,              (A5)
    provided 0<=v<11 beta/120 = 11 sqrt(5)/120.

This bound applies to arbitrary physical-even psi in the angular form
domain, not only an individually normalized eigenstate, at each such E.
The band width and constants do not grow with M, provided the stated norm
bound on the whole interaction V is uniform in M.

### Full complementary inverse in this application

Impose simultaneous Gauss on coarse AND fiber variables. With exactly one
fiber quantum, the fiber is adjoint. A physical state must have a coarse
adjoint, whose oscillator minimum is E_base+alpha. With at least two
fiber quanta, the coarse energy is at least E_base. Thus

    Q H_ref Q >= E_base + min(alpha+beta,2beta)-v
               = E_base+alpha+beta-v                 (A6)

on the full physical complement. Relative to the first-band upper
edge E_base+2alpha+v, this is a floor beta-alpha-2v.
The sufficient window in A5 indeed makes it positive, since
11 beta/60 < beta-alpha (equivalently alpha<49 beta/60).
Squaring gives 3 < 2401*5/3600, i.e. 10800<12005.

The sharper A4 bound concerns the range of WP, not the entire complement.
In Z_i L_i psi, L_i preserves coarse parity. Hence WP of an even coarse
psi is odd under TOTAL coordinate inversion. In that sector,
one fiber quantum pairs with an EVEN coarse adjoint, giving floor
E_base+2alpha+beta-v; two fiber quanta require ODD coarse content with
floor at least E_base+alpha+2beta-v; three or more give at least
E_base+3beta-v. Each exceeds the first-band edge for 2v<beta.
Therefore the needed odd complementary inverse exists throughout A5,
with a stronger source-range floor than A6. This distinction keeps the
odd first jet visible while also verifying the full physical inverse.

The cubic operator W need not preserve total coordinate inversion; the
two-strip common-Gauss source expressly retains a nonzero first jet.
At g=0 the even/odd sectors reduce H_ref; that is all the argument uses.

## 4. What this advances and what it does not

Established input -> actual two-strip first coupling and direct 3/4 angular term.
New implication -> a complete interacting-coarse reference cluster preserves
a positive angular coefficient under the explicit uniform window A5.
No independent coarse ground marginal or [H_c,L_i]=0 is required.

The next Wilson obligation is to realize a coarse interaction with the needed
source-sector lower bound (A4), or a sharper replacement, while controlling
changes to the fibers, connection coefficient, Haar terms and literal sources.
A sum of bounded local interactions generally has ||V|| growing with M;
A5 does NOT by itself prove uniformity for such an extensive Wilson interaction.
One must prove a volume-uniform difference of source-sector and band energies
or a connected form estimate. Neither an arbitrary cutoff nor a product law
has been inserted to assert it.

This isolates a constructive threshold rather than setting every first jet
to zero: retain and bound the nonzero exchange. It is a component of the
nonlinear Schur budget, not a proof of W6 or the continuum mass gap.

## Verification and provenance

`check_angular.py` uses exact SymPy matrices for two SU(2) adjoint factors,
an interacting total-Casimir coarse Hamiltonian, its full resolvent, and
all angular-source channels. It checks the source-norm identity, positivity
window, noncommutation with individual generators and failure beyond the
sharp threshold. The analytic Hilbert-space and band arguments above establish
the general quantifiers; finite matrices do not certify Wilson realizability.

Run with Python and SymPy: `python research/2026-09-10_interacting_angular_window/check_angular.py`.
The temporary dependency environment is separate from the pre-existing venv.
No Lean build or physical model simulation is claimed.

Live GitHub was refreshed to e872936. Its new W6 conditional transport note
records synchronized transport as an open successor; this reference angular
estimate neither replaces that work nor claims to discharge its M10 bound.
See the separate graph task record for briefing and integration state.
