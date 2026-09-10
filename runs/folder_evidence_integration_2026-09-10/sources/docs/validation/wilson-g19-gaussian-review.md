# G19 Gaussian corpus review: nine distinct proofs and their actual inputs

9 September 2026. Read-only review requested before adjudicating G19 status.
Assignment source: `docs/validation/wilson-g19-corpus-review-manifest.json`,
entries with `review_group="gaussian"`. All nine representative documents
were read through the actual derivations, not only their scope statements.
SHA256 was checked for every listed copy: **9 distinct documents, 48 copies,
0 hash mismatches**. Repeated copies are not counted as independent results.
No shared repository, ledger, code, Lean, or generated file was edited.

## Outcome that changes the current continuation

The corpus already proves much of the correct Gaussian reference:
the entire literal quantum fast complement and complete low-window frame;
the actual normalized endpoint memory; the complete conditional covariance;
volume/regulator-uniform polynomial spatial and exponential temporal
conditional kernels; the full n-leg fast-energy shorting formula; and the
first actual Wilson ground/source cubic on its stated finite-complex domain.

In particular, the dynamic covariance proof supplies the reference-semigroup
budget R4 for the **actual flat Gaussian conditional fiber** at each fixed
blocking ratio, through the direct corollary proved in section 10 below.
It is too strong to say every reference-semigroup budget remains unproved.
Section 11 also computes the actual Gaussian outside-pressure Hessian:
it cancels the nonreducing quadratic cross term exactly, so the full Gaussian
R12 defect is zero without requiring that cross term to be small.

No reviewed document constructs the actual interacting source-fiber map
and proves the complete Wilson R5/R12 defect or W6 comparison through the
continuum trajectory. This conclusion follows from the operators and
quantified estimates actually derived below, rather than their labels.

## 1. Entire literal Gaussian quantum complement and source frame

**Document:** `G19_GAUSSIAN_QUANTUM_FAST_SOURCES_20260905.md`.
Representative: `C:/WORKHOUSE/WORKHOUSE-autonomous-20260905/paper/research_notes/G19_GAUSSIAN_QUANTUM_FAST_SOURCES_20260905.md`.
SHA256 `d26cd81a6db579c6ab231d0c381f16315c238f97792bb6c9022fcc2b0cc41556`;
4 copies, 334 lines.

**Accepted proof.** Lines 19-45 identify the literal source
Jf=f(Lq)Phi, with its actual Gaussian marginal, as the complete Fock range
Gamma(Omega^(-1/2) ran L*), by Wick ordering and density in every degree.
Lines 49-87, equations (4)-(7), convert the FULL matrix inequality
K>=kappa(I-P_S) into the inverse-frequency weighted inequality
Omega>=sqrt(kappa)Q_R; the compressed inverse argument keeps all cross
blocks and uses no commutation with the source. Lines 89-113, (8)-(9),
second-quantize it to

    H>=sqrt(kappa)[I-Gamma(P_R)]

on the entire closed Fock form domain. Lines 119-133, (10), then give the
whole-window literal frame lower bound 1-E_*/sqrt(kappa), and an explicit
bounded right inverse. Lines 139-153 justify restriction to the entire
residual compact-group invariant space by Haar averaging dense polynomials.

**Input supplied.** A full Gaussian quantum fast floor and complete literal
source frame, not merely a one-particle floor. The theorem applies to the
actual path once its own full matrix/source inequality is inserted. The
specific application in lines 160-207 instead uses the earlier normalized
box-indicator Coulomb source; its stronger constant must not be transplanted
to a different path source without that path's inequality.

**Remaining comparison.** Its ground is the regulated Gaussian, not the
interacting Wilson ground. Lines 202-207 explicitly retain harmonic modes
whose joint variance diverges as rho tends to zero. The proof requires an
actual L and true marginal; it cannot identify nonlinear observations by
tangent dimension alone. The fixed-regulator Schur realization in lines
280-313 has ||U||<=M/m, not a regulator-uniform dressing estimate.
Dependencies: the full incidence/Hodge inequality and the specified source;
no use of a presupposed nonlinear Wilson gap.

## 2. Exact Gaussian history observability and physical algebra

**Document:** `G19_GAUSSIAN_OS_HISTORY_OBSERVABILITY_20260905.md`.
Representative: `C:/WORKHOUSE/WORKHOUSE-autonomous-20260905/paper/research_notes/G19_GAUSSIAN_OS_HISTORY_OBSERVABILITY_20260905.md`.
SHA256 `d7e986d12303c81b6b21d6028bcf058340bcbb6c164044b7e122d0ba6f10f720`;
4 copies, 400 lines.

**Accepted proof.** Lines 25-85, (1)-(3), compute the observed one-particle
OS range exactly as the spectral/Krylov span

    K=span{exp(-tOmega) B* a}=direct_sum_j ran(P_j B*).

The inverse Vandermonde argument with positive Euclidean sampling gives
each spectral component, including components of small nonzero residue.
Lines 88-123, (4)-(5), use Wick pairing and OS-continuous Gaussian density
to get the complete history range Gamma(K), which reduces H. This is a
different subspace from the equal-time range in document 1.

Lines 176-229 compute the actual seven-link two-square symmetric tangent:
frequencies sqrt(3),sqrt(5), and first missing physical energy
sqrt(3)+sqrt(5), realized by the mixed singlet Q.Z. The intrinsic fiber
class energy 2sqrt(5) is strictly larger and cannot replace that complement.
Lines 231-290 prove that arbitrarily small nonzero face-weight asymmetry
restores exact history observability, with high-frequency residue of order
epsilon^2. Lines 292-354 independently prove separate-slice SU(2) radial
history completeness for the two-mode example, including invariant density.
Lines 356-364 give the three-vector orientation obstruction to extending
that algebraic conclusion without another proof.

**Input supplied.** Exact Gaussian history/source identification when its
observability and actual invariant algebra are established; decisive tests
against identifying a fixed configuration fiber with a physical history
complement. It supports a correct carrier matching choice, not an actual
nonlinear quasi-locality or ground-pressure estimate.
Dependencies: positive Gaussian frequencies and a specified observation;
the actual seven-link harmonic geometry for the strip examples.

## 3. Actual Gaussian endpoint baseline, normalization and low window

**Document:** `G19_GAUSSIAN_PATH_ENDPOINT_BASELINE_20260906.md`.
Representative: `C:/WORKHOUSE/ALL THEORY/WORKHOUSE/docs/derivations/wilson-spatial-inputs/G19_GAUSSIAN_PATH_ENDPOINT_BASELINE_20260906.md`.
SHA256 `6ecf1868aaa3b8be3bec2c9cdb057b6f4d3b8cf352c8e5639657f25c874cccbb`;
5 copies, 456 lines.

**Accepted proof.** Lines 34-85, (1)-(2), prove the full-Fock endpoint
compression C_tau=Gamma(M_tau), K_tau=dGamma(-log(M_tau)/tau), with
G=W*Omega^(-1)W and its actual marginal normalization. Lines 87-140,
(3)-(6), give the phase-correct two-polarization actual path alias matrix
and retain all harmonic coordinates. Lines 142-250, (7)-(15), prove
G_high<=pi^8|K|^3 G_low/3072; congruence, rather than unjustified commuting
matrices, gives both endpoint frequencies and the complete low-Fock-window
relative comparison with delta_E=pi^11(LE/v)^2/(24576s).

Lines 260-303 prove the local unweighted row Gram and its exponentially
decaying inverse, but keep that operator distinct from G. Lines 305-355,
(19)-(20), compute the actual coupled conditional Fisher matrix
I=2BC^(-1)B*/g^2, including a concrete actual n=6,L=2 path whose B is nonzero.
Lines 357-409 show nonadditive full-Fock static Schur energies in a physical
invariant example, while the endpoint remains second quantized.

**Input supplied.** A normalized complete Gaussian endpoint/physical-clock
baseline and a genuine low-window comparison. Its leading conditional score
need not be small. Consequently the next comparison must subtract this
coupled baseline; assuming a product reference loses an order-one effect.
It does not bound the difference between the interacting and Gaussian
endpoint/source maps. Dependencies: actual local-path alias estimate,
positive regulator or stated nonzero-mode model, and full Gaussian source
identification. No continuum field limit is inferred by removing harmonics.

## 4. Entire conditional quantum path covariance and summability

**Document:** `G19_CONDITIONAL_QUANTUM_PATH_COVARIANCE_20260906.md`.
Representative: `C:/WORKHOUSE/WORKHOUSE-autonomous-20260905/paper/research_notes/G19_CONDITIONAL_QUANTUM_PATH_COVARIANCE_20260906.md`.
SHA256 `6e2b216343bdeff53954012a0ec69436bfabeebe4daf96f9f89cd35601081181`;
4 copies, 363 lines.

**Accepted proof.** Lines 51-96, (1)-(3), compute the entire conditioned
covariance both by square completion and inverse compression:

    C_fast=C-CW(W*CW)^(-1)W*C
           =Q_F(Q_F Omega Q_F|F)^(-1)Q_F,
    Omega_F>=sqrt(v^2/(33L^2)+rho^2).

The probability covariance is C_fast/2, and integrating its conditional
Poincare inequality recovers the full literal quantum complement floor.
Lines 98-176, (4)-(6), cancel the principal alias pole exactly, including
the transverse projector and its continuous K=0 extension. Fast rank is
2L^3-2 at and away from zero.

Lines 178-286, (7)-(11), prove actual block-coordinate kernel decay
B(L,epsilon_*)v^(-1)(1+|x|)^(-4), uniform in volume and bounded rho/v.
The proof controls derivatives through order five on dyadic momentum
annuli, sums their Fourier bounds, and obtains finite tori by exact
periodization. This is an actual analytic locality estimate, not a norm-gap
analogy. Lines 288-321, (12), show a non-differentiable transverse mixed
symbol even at positive rho; exponential locality of this particular
conditional ambient kernel is therefore not available.

**Input supplied.** Complete flat Gaussian conditional floor and polynomial
spatial locality for the actual path. It directly supports weighted Schur
algebras with weights s<1 and the dynamic continuation. Constants are
fixed-L; uniformity in the number of blocks and regulator is explicit.
It does not identify the nonlinear conditional law or bound its excess.
Dependencies: actual path source/full cochain inequality and its alias
symbols. The low-pole cancellation, not deletion of physical modes, controls
the regulator limit on each fixed affine fiber.

## 5. Dynamic fiber covariance and selected cubic synthesis

**Document:** `G19_DYNAMIC_FIBER_COVARIANCE_AND_CUBIC_ENERGY_20260906.md`.
Representative: `C:/WORKHOUSE/ALL THEORY/WORKHOUSE/docs/derivations/wilson-spatial-inputs/G19_DYNAMIC_FIBER_COVARIANCE_AND_CUBIC_ENERGY_20260906.md`.
SHA256 `4fb0bfd9dc1fb1c545a147670fcfe9f6302773cbece6fe0642284d0a9ae387aa`;
5 copies, 363 lines.

**Accepted proof.** Lines 13-49 define the ACTUAL affine-fiber process with
Sigma_t=(1/2)Q_F Omega_F^(-1)exp(-tOmega_F)Q_F and assert the bound proved
in lines 54-190. The latter uses an ambient fixed spectral island for
vC_fast, excludes its zero island by a contour, transfers the conormal
derivative bounds through a resolvent identity, and performs the same
dyadic Fourier/periodization argument. It proves

    ||Sigma_t(x)||<= (B/v) exp[-vt/(2sqrt(33)L)](1+|x|)^(-4),

including time-integrated absolute spatial rows, uniformly in volume and
bounded regulator at fixed L.

Lines 192-248, (14)-(15), compute the exact connected Lie-cubic two-time
Wick decomposition and all three sum-of-frequency energy denominators.
Lines 250-294, (16)-(17), prove a volume-independent rooted fiber-energy
and synthesis bound PROVIDED the actual vertex coefficients have bounded
incidence and the retained means are bounded by M_0 on their cutoff
supports. Lines 296-339, (18)-(19), rigorously dominate the ACTUAL full
Gaussian complement inverse by the vertical inverse as quadratic forms.
The 1/18 versus 1/20 example verifies that these inverses differ.

**Inputs supplied.** In addition to the R4 corollary below, a selected
Gaussian cubic synthesis bound is available under explicit coefficient
incidence and retained-mean cutoffs. It can serve a component of a C_force
estimate only after the actual t1 p family and its source norm are matched
to those coefficients. Quadratic-form inverse order does not supply
entrywise absolute rows of the full n-leg inverse, or interaction bounds.
Dependencies: document 4 and bounded retained means/actual cubic incidence.

## 6. Full Gaussian fast Green and the energy-prior shorting identity

**Document:** `G19_FULL_GAUSSIAN_FAST_GREEN_20260906.md`.
Representative: `C:/WORKHOUSE/ALL THEORY/WORKHOUSE/docs/derivations/wilson-spatial-inputs/G19_FULL_GAUSSIAN_FAST_GREEN_20260906.md`.
SHA256 `ac6767464a2fbc1e6ec174b638bdf642e07dc473a60a4c08967fec6526f3ab7b`;
5 copies, 243 lines.

**Accepted proof.** Lines 40-98, (1)-(3), solve the constrained positive
matrix equation at every n and derive the actual coordinate-force kernel

    T_n=A_n-A_n U_n(U_n*A_nU_n)^(-1)U_n*A_n,
    A_n=(tensor Omega^(-1))/(sum_j Omega_j).

It is the inverse of the compressed full quantum operator, not a compressed
inverse or a tensor of one-leg fast inverses. The proof permits nonreducing
sources and restricts to physical symmetric/alternating color-spatial
tensors. Lines 102-115, (4), identify n=1 exactly with a conditioned
second-order inverse Omega^(-2), a useful real connection to Laplacian
methods which does not identify it with the equal-time covariance.
Lines 117-133 show omitted mixed retained/fast sectors explicitly.
Lines 135-174, (6), compute the exact full Lie-cubic exchange coefficient.

**Input supplied.** The exact Gaussian F0 inverse and energy denominators
needed for selected Feshbach/force calculations. It supplies a reference
formula; the interacting resolvent comparison Rg-R0 and full selected
remainder are absent. Lines 176-198 identify the retained-harmonic factor
1/[rho^2 omega_h(2rho+omega_h)], whose actual Wilson realization is in
document 8. Lines 200-224 correctly retain all quartic/electric/Haar/
moving-source/fast-form terms as the next combined calculation.
Dependencies: documents 1, 3, 4 for source and full fast floor; document 5
for the separate synthesis domination.

## 7. Actual first Wilson ground forcing and moving source

**Document:** `G19_CUBIC_GROUND_TRANSFER_20260906.md`.
Representative: `C:/WORKHOUSE/ALL THEORY/WORKHOUSE/docs/derivations/wilson-spatial-inputs/G19_CUBIC_GROUND_TRANSFER_20260906.md`.
SHA256 `e321d704a9e9a741523ed06d66736cd97e3fbae2910a493dd88b6d2111264e93`;
5 copies, 209 lines.

**Accepted proof.** The actual original-link electric and ordered Wilson
magnetic first jets in lines 32-77 contain one alternating Lie bracket.
On a fixed finite connected complex with a unique flat orbit and H^1=0,
this proves H1 Phi0=P_D Phi0 with D in exterior^3 E*. Lines 79-105 give
the COMPLETE first ground corrector C=-(Omega_1+Omega_2+Omega_3)^(-1)D,
and exact cancellation for cycle rank below three. This uses the stated
fixed-complex localization input; it is more than a magnetic-only vertex.

Lines 107-141, (3)-(4), prove the exact conditional cubic mean with no
first-order fast tadpole. Lines 143-180, (5)-(6), differentiate a moving
nonlinear source chart and keep its divergence/Jacobian contribution:
the marginal score includes both 2P_C(m(y)) and
2<G^(-1)y,Y1(m(y))>. The bracket argument kills its linear contractions.

**Input supplied.** An actual Wilson first-order ground/source coefficient
and a required moving-source correction, on its stated finite-complex
domain. It does not provide a volume-uniform remainder or a growing-periodic
complex with retained noncommuting harmonics. Second order must combine
cubic exchange, quartic Wilson, electric metric, Haar and source terms.
Dependencies: exact finite-cell quotient/localization theorem, Gaussian
conditional identities, and a specified submersive nonlinear source chart.

## 8. Actual local Wilson harmonic exchange and signed cancellation

**Document:** `G19_WILSON_HARMONIC_CUBIC_OBSTRUCTION_20260906.md`.
Representative: `C:/WORKHOUSE/ALL THEORY/WORKHOUSE/docs/derivations/wilson-spatial-inputs/G19_WILSON_HARMONIC_CUBIC_OBSTRUCTION_20260906.md`.
SHA256 `3ac41920cde3f580e45dba0730e0cc29846bcb996b7e3199c8e95c6b625c9399`;
5 copies, 218 lines.

**Accepted proof.** Lines 26-66 independently derive the full energy-prior
shorting identity. Lines 68-115 choose actual periodic transverse modes:
two retained constant modes and one source-null alternating mode, and
compute the ordered plaquette BCH coefficient
-2(-1)^x1<Z,[X,Y]>/V^(3/2). Lines 117-158 construct the actual physical
Lie-invariant Fock vector and prove its resolvent-energy contribution

    v^4 C_A d/[2V^3 rho^2 omega_h(2rho+omega_h)].

The coefficient diverges like rho^(-2) at each fixed even torus despite a
uniform fast floor. Lines 163-177 calculate the exact spatial cancellation
of that sector in the global sum, since sum_x(-1)^x1=0.

**Input supplied.** A real constraint on the admissible norm/order of
cancellation in W6: absolute local rooted norms before summing are stronger
than the signed global coefficient and fail on this unrestricted reference
family. This is NOT a refutation of the actual compact Wilson gap or of
the complete first ground coefficient. The true retained compact dynamics,
bounded-mean cutoffs, or signed cancellation can address it; the document
does not estimate their complete interaction. Dependencies: actual path
alias/source geometry, Lie tensor normalization, and the regulated reference.

## 9. General closed-form Schur scale comparison and full graph frame

**Document:** `G19_FORM_SCHUR_SCALE_COMPARISON_20260905.md`.
Representative: `C:/WORKHOUSE/ALL THEORY/WORKHOUSE/docs/derivations/wilson-spatial-inputs/G19_FORM_SCHUR_SCALE_COMPARISON_20260905.md`.
SHA256 `df1737860dd8fd6e59398170c8c5204c05f5fb41c216a8a7009ef9949e0e6acd`;
11 copies, 529 lines.

**Accepted proof.** Lines 16-80 construct the exact closed-form square,
retaining M=I+U*U. Lines 84-157 prove
f mu_j/(f+mu_j)<=lambda_j<=mu_j by shifted square completion and negative
index, with essential-spectrum qualifications. Lines 169-200 identify the
full vacuum and complete gap. Lines 202-245 extend the theorem to arbitrary
retained Hilbert spaces under a closed triangular factorization and bounded
U; the infinite-dimensional hypotheses are not silently dropped.

Lines 247-291 give the exact energy-dependent resolvent memory. Lines
318-362 prove the COMPLETE graph-source window frame with lower bound
1-(E/f)^2 and an explicit right inverse. Lines 367-408 prove the inverse-gap
cascade PROVIDED gap(L_j)>=Delta_j is separately proved for the actual
normalized Schur coarse Hamiltonian at every step.

The vacuum-mismatch calculation in lines 410-510 is also substantive:
even uncoupled gapped sites give an exponentially bad raw complement and
graph norm when the wrong vacuum projection is retained. Exact onsite
dressing repairs that example, motivating the actual dressed Wilson source
comparison rather than excusing its omission.

**Input supplied.** A non-Gaussian, fully closed-form downstream theorem
that can transport a physical gap and a whole graph-source frame once the
actual factorization, fast floor, coarse comparison and source identification
are established. It does not itself establish those Wilson hypotheses.
It explicitly accommodates large baseline cross terms, so a weak raw
off-diagonal bound is not a required substitute for the true Schur budget.
Dependencies: closed positive forms, actual F>=f, bounded dressing for
infinite P, and an independently controlled normalized coarse operator.

## 10. Newly extracted corollary: R4 is available for the flat Gaussian fiber

This corollary reuses the ACTUAL proof in document 5, not merely its stated
scope. Fix L>=2 and 0<=rho/v<=epsilon_*<infinity. Put

    c=1/(sqrt(33)L), M=sqrt(12+epsilon_*^2),
    A=Omega_F, H_epsilon(K)=v C_fast(K),
    spec H_epsilon(K) subset {0} union [1/M,1/c].

The positive fast island has constant rank 2L^3-2, including K=0. Although
the unconditioned fine/coarse transverse spaces separately gain one
direction there, conditioning retains every harmonic direction and their
rank difference is unchanged. Document 4, lines 167-176, establishes this
fact and the continuous covariance extension.

Choose the fixed contour Gamma from document 5, lines 79-98, around the
positive island and excluding zero, with Re(1/z)>=c/2. For s=vt define
f_s(z)=exp(-s/z) near the positive island, and define it to be zero in a
disjoint neighborhood of the zero island. Dunford calculus gives the
exact ambient operator

    U_t(K)=Q_F exp(-tA)Q_F
      =(1/(2pi i)) integral_Gamma exp(-vt/z)
                                     (zI-H_epsilon(K))^(-1) dz.    (GC1)

At t=0 this equals Q_F, not the full ambient identity. This is legitimate
holomorphic calculus on a disconnected spectral neighborhood. No inverse
has been assigned to retained or unphysical zero eigenvalues.

The proof in document 5 has H=B+R with
||partial^alpha R||<=C_alpha |K|^(1-|alpha|), |alpha|<=5, B smooth, and
both spectra separated from Gamma. Its resolvent difference (10) retains
one R factor; differentiated product estimates (11) therefore hold unchanged.
Insert f_s in place of the document's z exp(-s/z). All momentum derivatives
fall on RESOLVENTS, not on f_s. On Gamma,

    |f_s(z)|<=exp(-cvt/2).

Thus the same bounds are valid uniformly INCLUDING t=0:

    ||partial^alpha[U_t-U_t^B]||
       <=C_alpha exp(-cvt/2)|K|^(1-|alpha|),
    ||partial^alpha U_t^B||<=C_alpha exp(-cvt/2), |alpha|<=5. (GC2)

No polynomial t factor is missing. Sacrificing half the positive frequency
floor in the fixed contour absorbs the behavior one would otherwise see
by differentiating an exponential directly. The same contour, distances,
and derivative constants work for all allowed regulator ratios.

The dyadic Fourier proof in document 5, lines 168-190, now gives

    ||U_t,infinity(x)||op
       <=B_U(L,epsilon_*) exp(-cvt/2)(1+|x|)^(-4).        (GC3)

At t=0 it also proves summability of Q_F. Exact periodization holds on
every finite coarse torus. For the symmetric polynomial weighted Schur
norm with 0<=s_w<1, the sum
sum_(x in Z^3)(1+|x|)^(s_w-4) is finite. The torus distance is no greater
than the distance of each periodized representative; consequently

    ||Q_F exp(-tA)Q_F||_(s_w)
       <=C_(s_w)(L,epsilon_*) exp(-cvt/2),               (GC4)
    beta_(s_w)(A)=integral_0^infinity
                      ||Q_F exp(-tA)Q_F||_(s_w)^2 dt
       <= C_(s_w)^2/(cv)
        =sqrt(33)L C_(s_w)^2/v.                          (GC5)

This is precisely the R4 reference budget on the fast subspace, represented
in fixed ambient block coordinates. If individual fine-component rows are
required, the finite factor sqrt(3L^3) from the document must be retained.
Hermiticity supplies the matching column bound. A color-identity tensor
does not add an operator-norm color factor.

The constants are finite and uniform in volume and bounded rho/v, with
fixed L. They have not been numerically optimized or proved uniform as
L itself grows. This is nevertheless the relevant fixed blocking-ratio
Gaussian reference input for an RG step. It is NOT a bound on the actual
interacting charged inverse, nor does it choose product coordinates for
the nonlinear physical observation fibers. A strict reference angle margin
and that geometric identification remain separate from (GC5).

## 11. Exact Gaussian outside-pressure cancellation

The nonreducing conditional Gaussian in document 3, lines 307-323, also
lets the R12 reference term be evaluated, rather than presumed negligible.
Use fast coordinates x and retained coordinates y, and write the full
constant ground precision as

    Omega=[[A,B],[B*,C]],
    Omega_0(x,y)=const exp[-(x*A x+2x*B y+y*C y)/2],
    H0=-epsilon Delta+epsilon <(x,y),Omega^2(x,y)>.

Let V_B contain all potential terms depending on x and let H_out contain
the y kinetic term and the remaining y-only potential. Direct differentiation
gives

    Hess_x V_B=2epsilon(A^2+B B*),
    W_B,0=(H_out Omega_0)/Omega_0,
    Hess_x W_B,0=-2epsilon B B*.

Therefore

    Hess_x(V_B+W_B,0)=2epsilon A^2,
    D_B,0=Hess_x(V_B+W_B,0)-2epsilon A^2=0.              (GC6)

The true conditional ground has precision A, as proved by document 4;
the pressure calculation explains exactly why it is A rather than
sqrt(A^2+B B*). The baseline quantum pressure can be large and negative.
No smallness of B was used.

For the nonlinear Wilson continuation the required defect is accordingly
the COMPLETE difference from (GC6), including the interacting pressure
variation W_B,g''-W_B,0'', actual source/kinetic changes and cutoff terms.
It is not appropriate to demand that W_B,g'' alone vanish or be small.
The reviewed documents compute first coefficients and selected exchange
pieces but do not bound this full nonlinear remainder uniformly on the
actual Wilson fibers through the scale trajectory.

## 12. Dependency verdict for the current G19 claim

Accepted chain from the reviewed proofs:

    actual tangent path/cochain bound
      -> entire Gaussian fast quantum floor and literal low-window frame
      -> exact endpoint/marginal/conditional baseline
      -> polynomial spatial, exponentially temporal Gaussian fiber kernels
      -> R4 flat-reference semigroup budget and zero Gaussian R12 defect
      -> exact cubic forcing, moving-source first coefficient and selected
         Gaussian energy/synthesis formulas.

The general Schur theorem additionally proves the complete downstream
spectral/frame transport once its actual coarse/source hypotheses hold.
None of those accepted arrows assumes that novelty is absent; they use
the constructed operators and proof equations in the corpus.

The next unproved arrow within these nine documents is

    actual compact Wilson conditional/source fiber
      -> full signed nonlinear potential-plus-pressure/kinetic/cutoff defect
         small enough relative to (GC5), with a strict angle budget,

or an alternative actual selected W6 estimate plus complete coarse/source
Schur matching. The first-order finite-complex corrector does not bound
its all-volume remainder. The Gaussian fast floor does not control the
retained harmonic variance; document 8 supplies an exact local witness and
the signed cancellation that a viable repair must preserve.

Accordingly this broader review DOES close an additional Gaussian R4 input
and identifies the exact zero-defect reference for R12. It does not locate
a valid interacting large-lambda/coarse-source bridge superseding the
current wall. The file `Continuum_Combined.lean` and the repaired BC2 source
are separately audited artifacts; their claims are not inputs to any of
the nine concrete proofs reviewed here. No numerical or Lean replay of
these archived controls was represented as performed in this read-only
review; the accepted statements above are the inspected analytic arguments.
