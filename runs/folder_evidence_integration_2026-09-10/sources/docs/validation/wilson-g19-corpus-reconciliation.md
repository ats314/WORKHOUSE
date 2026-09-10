# Broader G19 review: accepted inputs and the precise continuum derivation

9 September 2026. This follows the user's request to inspect the G19 files
before deciding the new closure claim. The inventory contains 222 G19-named
files outside temporary/build folders and 43 distinct byte versions. Paths,
hashes, copies and representative choices are recorded in
[the inventory](wilson-g19-corpus-inventory.json) and
[review manifest](wilson-g19-corpus-review-manifest.json).
This is a review of that named collection and the cited closure sources,
not a claim to have audited every nested archive or every unnamed theory file.

Three independent reviewers read all 29 distinct assigned Gaussian, source
and physical-fiber documents in full and verified their representative hashes.
The root read the proof-bearing sections of the remaining 14 versions as
specified below, including the differences between the two continuum/RP
versions. Earlier statements of missing work were checked against later
proofs; a source's old scope paragraph was not used to override its successor.

## 1. What the broader review actually supplies

- [Nine Gaussian documents](wilson-g19-gaussian-review.md): complete regulated
  Gaussian fast quantum floors and source frames; normalized endpoint memory;
  full conditional covariance and time-integrated polynomial locality;
  first ground/source cubic coefficients; selected connected cubic synthesis;
  and the full downstream Schur theorem under its actual form hypotheses.
- [Twelve source documents](wilson-g19-sources-review.md): actual localized
  joint-vacuum scores, full literal-source complement inequalities, complete
  additive common-Gauss radial/pair frames, and endpoint comparison controlling
  high retained states. These are accepted at their stated operator scope.
- [Eight fiber documents](wilson-g19-fibers-review.md): actual nonlinear
  finite-cell shells with complete rank, actual two-square physical sources,
  Born-Huang and on-shell exchange corrections, all-coarse vertical barriers,
  and box-count-uniform harmonic coercivity with retained zero modes.

In particular, the documents are not all Gaussian approximations. Some prove
actual nonlinear local vacuum and source statements at large coupling.
For the older SU(2) convention H_E=-(1/2)sum Delta with metric -2ReTr,
Delta_old=Delta_unitS3/4 and 2u(2-Tr U_p)=4u s_p. Thus the current SC17
normalization has epsilon=1/8, k=4u and lambda=32u for that Hamiltonian.
No unidentified substitution of u for lambda is used.

Two further consequences are derived explicitly from the existing Gaussian
proofs and integrated into the SC17 note:

    beta_s(Omega_F) <= sqrt(33)L C_s^2/v,  0<=s<1,       (CR1)
    V_0,xx''+W_0,xx''=2epsilon A^2.                      (CR2)

CR1 is uniform in volume and bounded regulator at fixed blocking ratio L,
including t=0 on the ambient fast projector. CR2 retains the cross block B:
V_0,xx''=2epsilon(A^2+BB*) and W_0,xx''=-2epsilon BB*.
The complete Gaussian defect is exactly zero even when B is large.
This narrows the live SC17 target to the complete nonlinear excess over
that reference, its curved-fiber identification, and the required angle margin.

## 2. Root review of the continuum, transfer and reflection chain

Every filename below is resolved to a hash-pinned representative in the
manifest. Sections listed are the actual read scope, not a full-file claim.

| Document/version | Proof sections read | Accepted result and application boundary |
|---|---|---|
| G19_CONTINUUM_BRIDGE_20260830.md | Sections 2-5, Theorems 1-4 | Exact disjoint-domain and conditional scaling laws, Mosco gap passage, and source-visible atom passage. The recovery family, physical floor and nonzero residue are hypotheses. |
| G19_CONTINUUM_BRIDGE_INSERT.tex, both versions | Local-source matching through Mosco passage, plus the version diff and added RP witness | The bare a^9 factor is an absolute-weight power count; it does not determine a normalized residue. The atom and Mosco proofs retain their actual convergence hypotheses. |
| G19_BALABAN_BLOCKING_REFLECTION_POSITIVITY_20260830.md, both versions | Deterministic permanence, centered-path proof, two-spin example; added Proposition 3.2 | Reflection-adapted deterministic blocking preserves RP. A general equivariant Markov kernel does not. The later corner-path counterexample is a distinct cited exact certificate, not a new replay performed here. |
| G19_OS_BLOCKING_AND_REVERSE_MASS_MATCHING_20260905.md | Full sections 1-7 | Exact OS isometry J and T_f^b J=J T_c for the actual pushforward history measure. Full fine gap also needs the eliminated-mode bound (9). Physical scale and complete source matching remain explicit. |
| G19_TEMPORAL_WILSON_MATCHING_20260904.md | Sections 2, 4-6 | Fixed-volume Chernoff passage, retuned fundamental clock, normalization dictionary and relative-gap transport. The later shell inputs supply its matching premise only in their fixed-spacing interval. |
| G19_UNIFORM_WILSON_WINDOW_20260904.md | Sections 2-4, 8-10 | All-irrep kinetic exclusion, complete free physical shell, uniform free resolvents and coefficientwise linked matching. Its old all-orders task is subsequently addressed by the current Wilson shell package at fixed spacing. |
| G19_DISCRETE_TIME_VACUUM_AND_WINDOW_20260904.md | Sections 5-10 | Actual vacuum limits, full-source time-correlation matching and positive window Gram. The proof of window positivity is not an isolated-shell totality proof; later shell inputs address that separate stage. |
| G19_WILSON_BLOCKED_VACUUM_INSERT_20260904.tex | Uniform-vacuum theorem through final boundary | Same marked-expansion, full-source matching and Borel-window arguments in publication form. The physical-time limit is at fixed spatial spacing. |
| G19_WILSON_KINETIC_WINDOW_INSERT_20260904.tex | Definitions, kinetic exclusion, shell proof and actual second-order transfer calculation | Preserves d_tau(Delta)=(tau/2)coth(tau Delta/2); it does not replace the actual transfer logarithm by the auxiliary Hamiltonian. |
| G19_TRANSFER_RESOLVENT_UNIFORM_BOUNDS_20260905.md | Full scalar proof and operator consequences | Entire-spectrum |d_tau-1/Delta|<=min(tau/2,tau^2|Delta|/12), with its stated energy-domain hypothesis for the sharper composed bound. |
| G19_FLAT_HOLONOMY_SOURCES_AND_RANK_REPAIR_20260907.md | Sections 1 and 4-6 | Uniform flat-source right inverse; nonlinear linkwise submersion neighborhood; exact physical rank jump and redundant-source repair. These are source geometry, not the interacting conditional-vacuum comparison. |
| G19_GLUEBALL_REVERSE_TARGET_DATA_20260905.md | Full note | Numerical scale/observable guidance; no measured mass is used as a rigorous input. |

The G19 OS isometry is a valid alternative route to transport. Its equation
(9) still requires an estimate for the actual eliminated OS modes; a tangent
or coordinate-conditional Gaussian floor does not identify that complement.
The source-family endpoint theorem is another valid alternative to global
Fisher smallness. It requires the actual coupled complete frame and compatible
scale hierarchy. Neither route should be discarded merely because a different
absolute-norm estimate fails.

## 3. Exact failure in the newly claimed continuum construction

The promoted `yangmills-continuum-balaban-multiscale-proof.md` has SHA256
`0e0f561f2e6b106d5f03ecbd32f1ca31f85f7f3abcb8fb830d759bc5c8eaf68a`, unchanged
from the [BC2 audit](wilson-sc17-bc2-update-audit.md). The root additionally
read its RG contraction, continuum construction, OS and mass-gap passages.
The following calculation does not depend on the earlier source/ghost issues.

Even granting all estimates through (7.6), the claimed Cauchy passage fails.
Equations (7.2) and (7.6) bound successive expectations by C/k. The proof's
next sentence invokes summability of 1/k^2. There is no preceding estimate
that replaces 1/k by 1/k^2, and telescoping does not perform that replacement.

A bounded exact counterexample to that inference is the dyadic triangular
sequence. For 2^j<=n<=2^(j+1), define

    a_n=(n-2^j)/2^j                 if j is even,
    a_n=(2^(j+1)-n)/2^j             if j is odd.

The formulas agree at block endpoints. They give 0<=a_n<=1 and
|a_(n+1)-a_n|=2^(-j)<=2/n, while a_(2^(2j))=0 and
a_(2^(2j+1))=1. Thus bounded expectations with the stated increment estimate
need not be Cauchy. If desired these are actual probability expectations:
take mu_n=(1-a_n)delta_0+a_n delta_1 and O(x)=x. This is a counterexample to
the implication used in (7.6), not a proposed Wilson measure.

A precise sufficient repair, on a genuinely identified common Banach space,
is to prove uniform contractions K_(k+1)=F_k(K_k) with constant theta<1 and
uniform map drift ||F_k(x)-F_(k-1)(x)||<=d_k, sum d_k<infinity.
Then D_(k+1)<=theta D_k+d_k for D_k=||K_k-K_(k-1)||, and summation gives
sum D_k<infinity. Observable/reference/source maps also need summable drift
and uniform Lipschitz control. A bound d_k=O(g_k^4)=O(k^-2) would suffice.
The existing size bound ||K_(k+1)||<=theta||K_k||+C g_k^2 alone does not
supply this drift estimate or identify the varying reference spaces.

A further [martingale repair](wilson-g19-martingale-repair.md) avoids absolute
summation of centered increments. Actual projective consistency of the
cutoff laws and normalized source compatibility give an L2-bounded martingale.
More generally, with r_k=E[M_(k+1)-M_k|F_k], it suffices to prove
sum ||r_k||_2<infinity and sum E Var(M_(k+1)|F_k)<infinity on a common
actual cross-cutoff coupling. The existing conditional fast gaps can bound
the second quantity after their kernels are identified. The OS theorem
assumes the required history pushforward; endpoint compression has its
explicit memory defect and cannot construct that history hierarchy by
composition. The reviewed proofs do not yet establish this actual
cross-cutoff law/source compatibility either.

There is a separate incompatibility at the claimed physical mass (8.14).
The choice in (6.10) gives kappa_k=(3/4)^k kappa_0. For any polymer-counting
constant C4>1, kappa_k-log C4 eventually becomes negative. It cannot equal
the claimed positive asymptotic m a_k. A proof in norms with a positive,
physically scaled margin kappa_k-log C4 is an additional quantitative input;
declaring that equality does not establish the required polymer bound.
Even replacing the schedule by kappa_k=log C4+m a_k leaves the geometric
prefactor 1/(1-exp(-m a_k)) divergent. The full marked-source normalization
and uniform two-marked norm must also be proved. The
[Cauchy and mass repair note](wilson-g19-cauchy-repair.md) gives the exact
summation formula and a sufficient entropy-inclusive connected estimate.

The earlier conditional-score papers do prove squared inverse-energy losses
and, for their additive models, summable scale budgets. The reviewed proofs
do not identify those recursions with the actual multiscale maps F_k and
observable/reference changes in (7.4)-(7.6). That is the exact attempted
repair still awaiting an actual interacting estimate.

## 4. Reconciliation of the four incoming closure claims

**G18.** The fixed-spacing theorem in
`paper/research_notes/G18_FIXED_SPACING_CARRIER_BRIDGE_INSERT.tex`, lines
164-213, constructs the complete three-component band and an onto literal
Wilson-source frame with a positive Gram floor in its small-u domain.
That fixed-spacing closure is accepted. The same corpus's continuum insert,
lines 95-165, makes continuum source matching a hypothesis and explains that
the common bare a^9 factor cancels in normalized spectral fractions.
Replacing a by fixed R removes an explicit power; it does not prove a
cutoff-uniform nonzero matched f_R or the continuum spectral measure.
G18's discharge must therefore be scoped to its fixed-spacing theorem,
with continuum source transport retained in G19.

**G19.** The two imported Lean statements cited for the new discharge have
the scalar scope established in [the late-ledger audit](wilson-sc17-late-ledger-audit.md).
They define N/4 and prove scalar limits/inequalities. The active Lean build
does not compile that imported file. The broader G19 collection supplies
the substantial inputs in sections 1-2, but not a repair of the displayed
continuum Cauchy or mass-scale step. G19 is not discharged by this chain.

**G22.** The proof in `docs/derivations/yangmills-simon-flat-directions.md`
really gives H_m>=T/2+g sqrt(m-1)sum|A_i| for its stated finite matrix model,
using the exact allocation H=T/2+sum K_i/[2(m-1)]. Its compactness argument
uses finite-dimensional Rellich compactness. Equation (3) bounds E0 before
vacuum subtraction. These results are retained. The document supplies no
identification with the actual gauge-coupled physical operator or a
volume-uniform vacuum-subtracted bound there; that G22 route stays live.

**G23 / VA14 / VA19.** SC17 and the Brownian-slab result close actual
strong-coupling assembly at fixed spacing, including the displayed lambda
<=1/73 interval. Their arithmetic Lean certificates have their exact scope.
The separate route whose name includes spatial refinement still requires
the large-lambda coupled comparison. Its completed fixed-spacing substeps
remain done, and its continuum extension remains live.
The [additional physical-time continuation](../derivations/wilson-sc17-physical-time-limit.md)
now identifies the actual free/periodic thermodynamic multitime correlations
with exp(-t K_mu) throughout 0<=lambda<=lambda_c. This closes that
fixed-spacing identification while retaining the cross-scale obligation.

## 5. Current derivation target after accepting the corpus inputs

For the signed SC17 route the full Gaussian baseline is now explicit:

    D_b=(V_B-V_0)''+(W_B-W_0)'',
    W_B=(H_out Omega)/Omega,
    ||D_b||_(s,infty)<=delta,
    2 beta_s(A)^2 delta/epsilon<1.

The actual nonlinear kinetic, moving-source and cutoff terms must be part
of that same comparison. CR1 supplies the flat-reference beta_s, and CR2
explains its exact zero defect. What remains is the complete interacting
excess and source-fiber comparison, or the alternative actual selected-W6 /
endpoint / OS eliminated-mode estimates with their stated matching hypotheses.
For the specific Balaban construction claimed in the incoming update, the
displayed stopping point is (7.6) to Theorem 7.1, before its measure and
spectral mass-gap conclusions can be applied.
