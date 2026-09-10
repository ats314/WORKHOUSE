# G19 corpus review: all eight distinct fiber/shell/boundary documents

Review date: 9 September 2026. Reviewer: sc17_cut_locality.

I read all eight `review_group="fibers"` representatives in the manifest
`C:/WORKHOUSE/ALL THEORY/WORKHOUSE/docs/validation/wilson-g19-corpus-review-manifest.json`,
including their proof steps, not just their introductions or scope summaries.
They comprise 2,992 lines and 63 recorded copies of eight distinct hashes.
All eight representative SHA256 hashes were checked live and match the manifest.
Copies are not counted as independent proofs. No ledger, Lean, code, source,
or generated file was edited, and no described archived numerical/Lean run
was represented as freshly rerun in this review.

The findings below accept the mathematical results where the stated proof
supplies them. In particular, several results concern **actual nonlinear
finite-block vacua and complete physical shells**, not just Gaussian models.
Their applicability to G19 depends on matching their exact operator, source,
projection, normalization, and uniformity hypotheses to the proposed theorem.

## 1. Coupled-oscillator method review

Representative:
`C:/WORKHOUSE/WORKHOUSE-autonomous-20260905/paper/research_notes/G19_COUPLED_OSCILLATOR_METHOD_REVIEW_20260905.md`

SHA256: `e6ffb8b2243b9f79005f82aa5b7a862a4f36a5fb86d04735211411489d13d05d`.
Read lines 1-168 in full.

**Accepted inputs.** Lines 14-26 derive the exact matrix invariant
`G_u=u*p-u'*q`, with `partial_t G_u+i[H,G_u]=-(u''+Ku)*q=0`.
This supplies canonical linear invariants and a way to audit moving quadratic
frames. Lines 75-105 give a consistent unitary displacement, including
`iD'D*=-alpha' p_y-beta' y-alpha beta'`, and retain the corresponding
momentum-dependent dispersion rather than discarding it as a scalar phase.

Equations (1)-(2), lines 110-153, prove an actual relative-energy criterion:
with `kappa(t)=||K^-1/2 K' K^-1/2||` and `A(t)=int kappa`, differentiating
the energy gives `|E'|<=kappa E` and therefore comparison constants
`exp(+-A(t))`. The equivalent invariant matrix uses the full symplectic
fundamental solution. This is dimension-independent in form and handles
crossings without choosing a singular scalar normal-mode chart.

**Exact G19 contribution and remaining hypothesis.** This discharges the
algebra of the moving quadratic comparison once the actual transport and
finite relative-variation budget are supplied. It does not supply that
budget for a Wilson scale trajectory. The exact switched-frequency example,
lines 57-62, has `R_2R_1=diag(-1/2,-2)` despite positive instantaneous
Hamiltonians, so preservation of an invariant does not replace the missing
uniform comparison. Lines 127-130 explicitly concern total quadratic energy,
not a vacuum-subtracted spectral gap. It provides no estimate of the full
quantum pressure in SC17 R12 or the literal-source W6 pairing.

The original-paper corrections at lines 33-48 were reviewed as corrections
recorded in this supplied research document; I did not reread that original
PDF during this assigned eight-document review.

## 2. Actual finite-cell gap and boundary form

Representative:
`C:/WORKHOUSE/ALL THEORY/WORKHOUSE/docs/derivations/wilson-spatial-inputs/G19_WILSON_FINITE_CELL_GAP_AND_BOUNDARY_FORM_20260905.md`

SHA256: `5fc9ff6495b6197dbd13b1b69f61f6bbe8f35d953915486cd616b3a8909a8db5`.
Read lines 1-442 in full.

**Accepted theorem and its hypotheses.** Equations (1)-(4), lines 44-125,
give an actual nonlinear physical spectral theorem for a fixed finite cell
complex, fixed compact connected simple group, faithful representation, and
positive face weights. It requires both a unique flat gauge orbit and
injectivity of the weighted curl on `C=ker d0*`. The distinction is necessary:
lines 86-90 exhibit the face word a^2 with positive tangent Hessian but two
SU2 flat assignments. There are explicitly no unlisted surrounding faces
or fixed external holonomies (lines 92-95).

The original-link quotient is derived, not chosen: lines 129-166 use the
fundamental cycle matrix R, its exact cometric `RR*`, and an orthonormal
transverse basis Q to obtain equation (5),
`H_quad=-(1/2)Delta_z+b_rho u<z,K_Cz>`. Frequencies are
`omega_j=sqrt(2b_rho)sigma_j`. Lines 175-205 prove that the complete first
physical cluster has rank `m(m+1)/2`, because one adjoint quantum has no
singlet and the invariant bilinear form is unique.

The nonlinear remainder is supported by actual proof steps. Lines 209-225
use compact IMS/min-max to count harmonic islands. Equations (8)-(10),
lines 227-275, then use projected parity `PH1P=0` and finite physical Hermite
correctors with explicitly separated denominators to improve the actual
ground and first-cluster errors to O(1) in the original operator. This is
stronger than a formal oscillator approximation, and I accept it under the
stated fixed-complex hypotheses.

**Boundary and fast inputs accepted.** Equations (13)-(14), lines 314-345,
prove the exact discrete IMS identity for the original plaquette Hessian
and its row-sum error, including its sign. Equations (15)-(16), lines
347-365, retain the exact potential Schur square and the entire induced
kinetic cross term. Lines 367-384 correctly identify the harmonic physical
nonvacuum-fast threshold as `min(2omega_f,omega_s+omega_f)` when slow and
fast adjoint modes coexist; a separate class-function factor two is invalid.

**Exact G19 implication.** These are actual finite-cell low-energy ranks,
local UV gaps, and an explicit boundary form input. They discharge neither
the nonlinear remainder uniformly in a growing cell nor the actual source
complement identification. Equation (11), lines 279-310, proves
`sigma_min^2=4-4cos(pi/(L+1))`; hence the full first physical gap coefficient
decreases like 1/L. This identifies slow modes which must be retained,
rather than refuting fast-mode matching.

The first missing inference to the current W6/R12 target is precise:
equation (8) is only an L2 remainder on fixed polynomial-Gaussian vectors
(lines 228-238), and its constants include fixed charts, Gaussian moments,
and denominators (lines 273-275). It is not a relative-form estimate on the
actual coupled fast resolvent sources uniformly in volume. Lines 391-410
list the exact absent boundary, nonlinear, vacuum-shift, and history-range
comparisons. Later source/flat-holonomy documents may discharge portions
of those items; this document does not claim otherwise.

## 3. Global vertical spectral cap and coarse-potential sandwich

Representative:
`C:/WORKHOUSE/WORKHOUSE-autonomous-20260905/paper/research_notes/G19_WILSON_GLOBAL_VERTICAL_BARRIER_20260905.md`

SHA256: `87d042b19066479b084fc13756dc09002ec683b65134716ea6262b8982fe7d8e`.
Read lines 1-340 in full.

**Accepted all-coarse theorem.** The operators and common H1 domains are
specified in lines 13-32: actual intrinsic bouquet and strip vertical
operators, with `S(U)=15[8I-Ad(U)-Ad(U)*]^-1` and metric bounds 3/2,5/2.
For every u>0, every coarse U, and every counted full-fiber level j,
equations (3)-(6), lines 40-72, prove

    E_j(U)>=min(e_j,epsilon_N u),
    E_j(U)>=e_j+(u-e_j/epsilon_N)v(U),
    A_U-e0 >=delta(I-P_U)+(u-e1/epsilon_N)v(U)I,
    (u-e0/epsilon_N)v(U)<=E0(U)-e0<=2u m v(U),

where `epsilon_N=min(1,4/N)` and `0<=m<=1`. These are global operator/form
results, not finite matrix truncations or merely a small-field chart claim.

**Proof checked.** The Frobenius identity (8), lines 88-101, gives the
global outside barrier without choosing a square root. Lines 105-145
construct a genuine SU(N) root on the remaining region and establish the
noncommutative PSD trace estimate. Equations (14)-(19), lines 149-211,
retain the actual adjoint metric and derive `A_U>=tA_I+4u eta` after a
unitary translation; min-max proves all levels. Lines 213-228 give the
ground/complement assembly, and the actual central-ground trial in lines
232-253 proves the upper sandwich.

**Closed and remaining hypotheses.** A global intrinsic vertical barrier
and a coarse-potential sandwich are supplied here and should not be listed
as wholly absent. However equation (5) subtracts the *central fiber* e0.
Lines 293-301 compute the true SU2 strip full-vacuum difference
`(3sqrt(3)/2)sqrt(u)`, larger than the vertical gap `sqrt(5)sqrt(u)`.
Thus this inequality cannot be relabeled as the fully vacuum-subtracted
coupled fast compression.

At U=-I, lines 255-281 prove exact conditional gaps 3/4 and 15/16 for every
u; this explains why retaining the large absolute coarse energy is necessary.
It does not contradict the actual physical block fast energy. The required
next identification is exactly the horizontal/vertical and ground-bundle
comparison in lines 303-311. In particular an E0(U) value sandwich is not
the missing all-field second derivative of `(H_out Omega)/Omega` in R12.

## 4. Planar harmonic boundary comparison and source frame

Representative:
`C:/WORKHOUSE/WORKHOUSE-autonomous-20260905/paper/research_notes/G19_WILSON_HARMONIC_BOUNDARY_COMPARISON_20260905.md`

SHA256: `8320a018c48230d28632bb361e190acb8722996aa4f6f70c7c0823220fcff981`.
Read lines 1-294 in full.

**Accepted uniform coercivity.** Lines 30-81 derive the original-link
quotient and face cometric `K=CC*=4I-A_face`, retaining the outer boundary
link energy. Equations (6)-(9), lines 113-181, give an exact decomposition
into internal Neumann box energies plus positive interface and exterior
squares, and prove

    K>=kappa_L Q, kappa_L=4sin^2(pi/(2L))>=4/L^2,
    lambda_(r+1)(K)>=kappa_L,
    H_harm-E0 >=sqrt(u kappa_L)(I-P_fast,0).

The constants are independent of the number r of boxes. This genuinely
handles all shared interfaces at the harmonic level; it is not a decoupled
block ansatz. The spectral normal-mode fast projection reduces the harmonic
Hamiltonian, and the physical restriction keeps the valid single-fast-quantum
floor because a slow adjoint can pair with it (lines 160-174).

**Accepted complete low-mode source statement.** Equation (10), lines
185-203, proves the full low-spatial-band frame bounds
`1-Lambda/kappa_L` and 1 for box means. The literal face sources are
identified in equations (11)-(12), lines 205-241, with the actual
`K^(1/4)` frequency weight and a frame lower bound proportional to
`sqrt(epsilon_band)`. Centered quadratic color contractions give the
physical two-quantum frame after symmetric tensoring. This proves source
totality on that stated band/sector, while exhibiting its infrared weight.

**Accepted relative harmonic comparison.** Equation (13), lines 243-273,
retains `K0=C-DF^-1D*` and `M=I+DF^-2D*` and proves
`f mu_j/(f+mu_j)<=lambda_j(K)<=mu_j`. The proof uses the exact negative-
energy Schur remainder and graph trial, not a small interface assumption.
This is a usable harmonic relative-gap input with its induced mass kept.

**Exact remaining map.** The coordinates are electric-dual/nonlocal unless
their frequency factors are retained (lines 207-233). The reducing spectral
projection has not been identified with a local Wilson or OS-history map
(lines 175-181, 287-294). Nonlinear remainder and generated interfaces are
not bounded here. Thus the harmonic f, M, and band source frame are closed
inputs; the actual coupled-vacuum W6/R12 comparison is not supplied by
renaming these harmonic objects.

## 5. Physical compact-rotor and constrained-fiber gap

Representative:
`C:/WORKHOUSE/WORKHOUSE-autonomous-20260905/paper/research_notes/G19_WILSON_PHYSICAL_FIBER_FAST_GAP_20260905.md`

SHA256: `904882b4b1d71ebb15cbb1b7325e85bb97f48bbf7a2298a66f3844e417881f6b`.
Read lines 1-438 in full.

**Accepted actual physical-energy theorem.** Equations (1)-(2), lines
16-84, give the full and class-function gaps of
`-kappa Delta+lambda v`, with leading frequencies `sqrt(kappa lambda)`
and twice that frequency. The theorem extends to a faithful representation
of a fixed compact connected simple group with the stated trace normalization.
Faithfulness rules out multiple zero wells. The proof is provided, not
inferred from a rank sweep: normal-coordinate and global unique-well estimates,
IMS with radius h^(1/4), explicit min-max codimension conditions, and cut-off
Hermite upper bounds appear in lines 90-176.

**Actual geometry supplied.** Equations (8)-(13), lines 184-271, derive the
bouquet link metric and the strip shared-edge form, including the intrinsic
vertical Schur metric. At coarse U=I these give exactly

    H_bouquet=-Delta+4u v,
    H_strip=-(5/4)Delta+4u v,

with their true full and central class-function gaps. The uniform coarse-
neighborhood result (14)-(16a), lines 273-342, proves the direct-integral
vertical gap on a specified compact neighborhood after subtracting the
coarse-dependent intrinsic fiber ground energy. These are useful actual
finite-block UV floors, uniform over ambient volume because the same fixed
fiber is used, not merely a claim that a local oscillator is plausible.

**Important closed distinction.** Lines 344-378 explicitly compare the
physical rotor to the different weighted diffusion operator. The latter
unitarily produces `|grad v|^2` and `Delta v`, whereas the Wilson rotor pays
the positive height of a secondary well. Hence a rare diffusion well is
not a counterexample to the proved physical fast rotor gap.

**Exact remaining identification.** Lines 267-271 distinguish fixed coarse
coordinates from a reducing subspace. Lines 325-342 specify precisely the
direct-integral ground projection that has been controlled. Lines 401-409
retain the actual history intertwiner, vacuum subtraction, horizontal terms,
and interblock coupling as the remaining application inputs. The theorem
does not identify this intrinsic ground with `Omega(.|outside)` of a larger
coupled lattice, so it does not itself supply R12's pressure Hessian.

## 6. Strip Born-Oppenheimer geometry and actual two-strip splitting

Representative:
`C:/WORKHOUSE/WORKHOUSE-autonomous-20260905/paper/research_notes/G19_WILSON_STRIP_BO_AND_TWO_STRIP_SPLITTING_20260905.md`

SHA256: `96142f5f1be86e159b4f5eb9342e0c8d71ef95e61bd598c78d9d45d3f4a789d9`.
Read lines 1-681 in full.

**Accepted exact and asymptotic inputs.** Lines 14-66 keep the actual
horizontal square, vertical Schur form, balanced coarse/vertical magnetic
split, and the true intrinsic vertical ground. Lines 70-167 derive the
localized ground and its first parameter derivative, using the actual
vertical oscillator gap to turn Hermite residuals into norm statements.
Equation (1) gives the order-one coarse-dependent zero-point shift;
equation (2) proves a balanced-coordinate O(g^2) derivative.

Crucially, the intrinsic horizontal derivative is different: equation (3),
lines 169-207, has a nonzero order-g commutator term. Equations (4)-(6),
lines 209-265, retain the actual projected metric, Born-Huang scalar,
zero-point shift, and Haar term. Their combined quadratic coefficient is
`sqrt(5)(5-2N^2)/(160N)`. This supplies genuine quantum geometric terms
which a magnetic-only comparison would miss.

**A cancellation genuinely proved.** Equations (7)-(10), lines 267-382,
derive the first off-diagonal operator and prove it vanishes on the entire
jointly invariant single-strip domain. The exact group inversion argument
at lines 321-358 removes every odd physical local Taylor coefficient for
this geometry. This is stronger than a coefficient norm estimate. It does
not extend unchanged to several coarse holonomies: lines 384-389 exhibit
the distinct sum of commutators that survives the common Gauss constraint.

**Actual finite multi-holonomy correction and shell theorem.** The two strips
are actual edge-disjoint copies sharing only a base vertex, with their
common physical Gauss law (lines 391-408). Equations (11)-(12), lines
416-471, evaluate the on-shell Feshbach image using its exact extra energy
sqrt(5), and retain both self-energy `-49g^2/80 sum ||L_i psi||^2` and direct
metric correction, yielding `+11g^2/80 sum ||L_i psi||^2`. The mixed physical
state is an explicit nonzero witness.

Equations (13)-(14), lines 473-619, then prove an actual nonlinear first-
cluster splitting, not just a formal effective matrix. The ground and
rank-three cluster are counted by compact localization; two Hermite
correctors produce O(g^3) rescaled residuals, and the rank count excludes
extra eigenvalues. The actual mixed/radial splitting is
`(54N^2-15)/(160N)+O_N(u^-1/4)`. Its SU2 value is 201/320, independently
recovered from the original seven-link form in the recorded controls
(lines 667-677).

**Exact remaining step.** The on-shell inverse is evaluated only on its
actual finite image; no entire unbounded coarse-spectrum inverse is
asserted (lines 426-434, 560-592). The graph has no inter-strip interaction
or boundary-crossing plaquette (lines 393-405, 613-619). The projected
intrinsic-ground space is explicitly a compression, not a reducing full
ground space (lines 211-223). Accordingly these results supply real pieces
of a source-compatible Feshbach calculation, but no box-count-uniform
bound on the surviving multiblock term or on the coupled-vacuum R12 defect.

## 7. Three-dimensional harmonic boundary theorem

Representative:
`C:/WORKHOUSE/WORKHOUSE-autonomous-20260905/paper/research_notes/G19_WILSON_THREE_DIMENSIONAL_HARMONIC_BOUNDARY_20260905.md`

SHA256: `f3732dbc32a8f2529e29c01e6e156cf275fe2dfda5a63c2677753d8c4d18a1df`.
Read lines 1-263 in full.

**Accepted actual all-size harmonic input.** Lines 29-86 give the full
periodic orientation conventions, Hodge identity, transverse dimension,
three harmonic link directions per color, and Bianchi constraint.
Equations (4)-(5), lines 88-117, specify the retained space exactly as
`S=ran(P_C B)` and fast space `ker d0* intersect ker B*`; boundary-crossing
links stay in their basepoint box and in the full energy.

The proof in lines 121-176 combines scalar cube Poincare, the exact Hodge
identity, and an explicit projection contraction. It establishes

    K_C>=kappa_L(I_C-P_S),
    Q_f K_C Q_f>=kappa_L I, kappa_L>=4/L^2,

uniformly in the number of boxes, with all interface couplings retained.
The positive decomposition (10) proves why those interfaces do not create
a growing error. This closes a real three-dimensional harmonic fast
coercivity hypothesis; it should not be described as merely a finite check.

**Further valid implication derived during this review.** The same Hodge
symbol bounds `0<=K_C<=12I`. Functional calculus therefore gives
`sqrt(K_C)>=K_C/sqrt(12)`, and the specified fast compression obeys

    Q_f sqrt(K_C) Q_f >= kappa_L/sqrt(12) I.

After retaining or regulating the harmonic modes, this supplies a positive
Gaussian conditional *precision* floor for this specified Coulomb-box-mean
fiber as well. This is an implication of reviewed equations (1),(9),(11),
not claimed as a new statement quoted from the document. It does not
identify this Q with an actual averaged-path source projection and does
not prove the weighted semigroup budget beta_s for R4.

**Exact remaining identification.** Lines 192-215 retain the zero modes
and distinguish the coordinate squared-frequency compression from a
quantum-Hilbert-space fast restriction. Lines 225-243 distinguish the
nonlocal Coulomb box projection from a local gauge/time-compatible source
and its full-history range. Thus the all-size harmonic lower bound is a
closed input. A uniform nonlinear/coupled-vacuum defect, actual quantum
projection, and weighted reference budget are not proved here.

## 8. Actual two-square physical shells and complete Wilson source frame

Representative:
`C:/WORKHOUSE/WORKHOUSE-autonomous-20260905/paper/research_notes/G19_WILSON_TWO_SQUARE_PHYSICAL_SHELLS_20260905.md`

SHA256: `b680b1f05cfae6ef22becdd63291d48bd9f841f1d37c4b66862029a350c3adb0`.
Read lines 1-366 in full.

**Accepted full nonlinear local theorem.** Equation (1), lines 20-42,
derives the actual seven-link Hamiltonian, including its shared-edge
electric cross term. The full physical block gap in equations (2)-(4),
lines 44-77, has leading coefficient `2sqrt(3)sqrt(u)` and three isolated
simple physical excited shells at frequencies `2sqrt(3)`,
`sqrt(3)+sqrt(5)`, and `2sqrt(5)`.

The proof retains the exact Gauss constraint (5). Contracting it gives
`L1.R2=R1.L2` on physical functions; this yields exact physical inversion
symmetry and the even cometric form (6)-(8), lines 79-153. The original
metric has eigenvalues 3 and 5. The invariant quadratic shells are counted
completely in lines 155-208, including their separation from every cubic
or higher possible invariant. Compact localization and physical min-max
in lines 210-258 prove actual nonlinear eigenvalue asymptotics and rank,
with O_N(u^1/4) errors. This is not an assumed Born-Oppenheimer remainder.

**Accepted complete actual-vacuum source result.** Equations (17)-(20),
lines 260-341, construct bounded gauge-invariant Wilson functions S_Q,S_M,S_Z,
centered at the true full-block Omega_u, and scale them by sqrt(u).
Their synthesis onto the actual rank-three spectral range has Gram tending
to I_3, hence bounds I_3/2 and 3I_3/2 for sufficiently large u and onto
range. The lowest physical shell has nonzero S_Q overlap. The proof does
not rely only on L2 eigenfunction convergence: lines 309-335 establish
potential-energy tail convergence and use the explicit form bound
`|S_j|<=2P` to pass every projected source matrix element. This discharges
both complete-shell rank and source totality for the specified actual
nonlinear finite block.

**Exact remaining transport.** Lines 343-366 give the physical UV scale
`2sqrt(3)c_H(a)/a+O(c_H g_H/a)` and explicitly retain the surrounding
plaquettes, induced couplings, ground shifts, slow-band projection, and
actual history intertwiner as the application inputs. Therefore this is
a genuine finite-block source/carrier input, but it does not itself map
that three-dimensional shell onto the requested interacting continuum
carrier or supply a literal-source W6 estimate in arbitrary volume.

## Joint conclusion for G19/W6 and SC17's actual quantum defect

The eight documents discharge concrete hypotheses that must be preserved:

1. Correct original-link and intrinsic vertical metrics, local physical
   UV gaps, and a global all-coarse vertical spectral/potential barrier.
2. Actual nonlinear finite-cell ground/first-shell asymptotics, exact
   shell multiplicities, and an explicit complete actual-vacuum Wilson
   source frame for the two-square block.
3. Real horizontal, Born-Huang, zero-point, and on-shell self-energy terms,
   with both a proved single-strip cancellation and a proved nonzero
   multi-holonomy correction.
4. Box-count-uniform planar and 3D harmonic fast coercivity, retained flat
   modes, complete stated low-band frames, and a relative harmonic Schur
   bound with the induced mass and memory kept.

None of these eight supplies an equation identifying its intrinsic fiber
ground or finite-shell projection with the actual coupled lattice's
conditional ground/fast projection. None gives the volume- and scale-uniform
bound on the complete nonlinear defect

    D_b=V_B''+[(H_out Omega)/Omega]''-2epsilon A^2

required by SC17 R5/R12, including actual metric/projector/cutoff terms.
The precise unproved transition is not the existence of any local gap or
source frame: it is the bound/comparison on the **matched actual coupled
vacuum and literal-source family**. A local finite-energy quasimode error,
an all-coarse intrinsic vertical barrier before full-vacuum subtraction,
and a harmonic coordinate compression are distinct inputs to that comparison.

For W6 in its stated source-restricted form, these documents do not prove

    sup_Lambda sup_(b_Lambda=1)
       |d_(g,Lambda,QQ)[R_(0,Lambda)t1p,R_(g,Lambda)t1p]|
       <=C|g|,

on the complete actual source family. They supply geometric coercivity,
spectral denominators, and exact low-mode examples that a proof can use.
The separate Gaussian/source documents in the full manifest must be
considered before deciding which of the remaining matching hypotheses
have since been discharged; this group review makes no claim that these
eight are the whole G19 corpus.

No result in this group invalidates the current SC17 fixed-coupling
completion or proves its full large-lambda quantum defect. Conversely,
the review confirms that large-magnetic **local nonlinear** results and
nontrivial source totality were already proved and should not be treated
as unavailable merely because SC17's new global route starts elsewhere.

## Normalization check

These older documents use the metric -2ReTr and H_E=-(1/2)sum Delta.
For SU2, Delta_old=(1/4)Delta_unitS3 and
`2u(2-Tr U)=4u(1-Tr U/2)`. Thus that exact Hamiltonian has epsilon=1/8,
k=4u and current lambda=k/epsilon=32u. No direct numerical identification
of their u with the current SC17 lambda should be made without this
conversion and the separately stated physical prefactor.
