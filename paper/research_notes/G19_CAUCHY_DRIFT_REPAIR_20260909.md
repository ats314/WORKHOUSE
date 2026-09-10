# Audit and sufficient repair of the proposed continuum Cauchy step

Mathematical audit and repair, 2026-09-09. Target: `C:\WORKHOUSE\ALL THEORY\WORKHOUSE\docs\derivations\yangmills-continuum-balaban-multiscale-proof.md`. This note proves the abstract repair below; it does not claim its actual Wilson RG hypotheses have been discharged. The target source is preserved unchanged.

## 1. Exact failed implication

The target's (7.2), line 324, and (7.6), line 338, give only

    |m_(k+1)(O)-m_k(O)| <= C_O g_k^2 <= C'_O/(k+k0).

Line 339 then says, exactly: “Since $\sum_{k=1}^\infty \frac{1}{k^2} < \infty$ and the increments are telescoping, the sequence is Cauchy in $\mathbb{C}$.”

No square on the increment occurs in (7.2) or (7.6). Telescoping gives

    |m_n(O)-m_m(O)| <= C'_O sum_(k=m)^(n-1) 1/(k+k0),

whose supremum over n>m does not tend to zero. Boundedness of O does not repair this: the bounded sequence sin(log(k+1)) has successive differences at most 1/(k+1), by the mean-value theorem, and has distinct subsequential limits +1 and -1. This is an insufficiency of the displayed estimate, not a proof that the actual expectations fail to converge.

An earlier independent missing step is (7.5), lines 335-336. Theorem 6.2 controls the magnitude of K_(k+1) in a different Banach space E_(k+1); it gives neither a difference estimate between two RG maps nor a common-space bound for S_(k+1)^eff-S_k^eff. The local action S_k^loc contains the running 1/g_k^2 coefficient (lines 254-258), and the observable changes under integration (7.4). Reference measures, coordinates, marginal action, and sources cannot be omitted when taking this difference.

Even granting (6.5) and a common space, the recurrence ||K_(k+1)|| <= theta||K_k||+C/(k+k0) implies ||K_k||=O(1/k) and hence K_k -> 0. This could prove convergence of expectations if they were uniformly Lipschitz functions of K_k relative to one fixed reference and one fixed observable. The target supplies neither identification. Convergence of the remainder does not establish convergence of the changing reference/action/source system.

## 2. Common-space contractive RG drift theorem

Let D be a closed subset of a Banach space X. For k>=0 let F_k:D->D satisfy

    ||F_k(x)-F_k(y)|| <= theta ||x-y||,       0<=theta<1.       (R1)

Let x_(k+1)=F_k(x_k). Assume, separately from (R1), an actual map-drift estimate

    sup_(x in D) ||F_k(x)-F_(k-1)(x)|| <= d_k,   k>=1,
    sum_(k>=1) d_k < infinity.                                (R2)

Writing Delta_k=||x_k-x_(k-1)|| gives exactly

    Delta_(k+1)
      <= ||F_k(x_k)-F_k(x_(k-1))||
           + ||F_k(x_(k-1))-F_(k-1)(x_(k-1))||
      <= theta Delta_k+d_k.                                 (R3)

Induction and summation of a nonnegative geometric convolution give

    Delta_(n+1) <= theta^n Delta_1
                    + sum_(j=1)^n theta^(n-j) d_j,
    sum_(k>=1) Delta_k <= (Delta_1+sum_(j>=1)d_j)/(1-theta).  (R4)

Therefore x_k converges in D. More locally,

    sum_(k=m+1)^infinity Delta_k
       <= [theta Delta_m+sum_(j=m)^infinity d_j]/(1-theta),   (R5)

which tends to zero, and is a usable truncation bound.

For the specified physical observable, let Phi_k:D->C obey

    |Phi_k(x)-Phi_k(y)| <= L_O ||x-y||,
    sup_D |Phi_k(x)-Phi_(k-1)(x)| <= e_(O,k),
    sum_(k>=1)e_(O,k) < infinity.                            (R6)

If its actual normalized expectation is m_k(O)=Phi_k(x_k), then

    |m_k(O)-m_(k-1)(O)| <= L_O Delta_k+e_(O,k).              (R7)

Equations (R4) and (R6) prove absolute summability of the actual increments and hence Cauchy convergence. No unproved cancellation of their signs is used.

### What has to be transported

For native scale spaces X_k and actual maps R_k:X_k->X_(k+1), supply norm-controlled charts U_k onto a common invariant domain, with

    F_k = U_(k+1) R_k U_k^(-1),    x_k=U_k z_k.

These charts must identify the same physical coarse fields and reference/action data. They also have to define Phi_k from the actual observable and actual normalized measure. If marginal directions are not contractive, they must instead be explicit parameters of F_k with separately bounded total variation; hiding them in a polymer remainder does not establish (R1). Likewise a changing covariance, background minimizer, source Gram metric, vacuum subtraction, or physical clock contributes to (R2) or (R6), unless an exact identification proves its cancellation. This is why (R2) is a concrete missing estimate and is not a restatement that the expectations converge.

An approximate recurrence x_(k+1)=F_k(x_k)+r_k is also covered if its states stay in the domain and sum ||r_k||<infinity: replace d_k in (R3) by d_k+||r_k||+||r_(k-1)||. If the actual additive errors have a summable successive-difference bound, that sharper bound suffices instead. Norm equivalence/chart errors must be included before claiming a uniform theta<1.

## 3. A genuinely square-summable coupling drift mechanism

Put t_k=g_k^2. Suppose, on the same domain and with the same transported reference/action/source data, the actual maps satisfy

    sup_D ||F(t,x)-F(s,x)|| <= L_t |t-s|,
    sup_D ||F_k(x)-F(t_k,x)|| <= r_k,
    sum r_k < infinity.                                     (R8)

Then d_k=L_t|t_k-t_(k-1)|+r_k+r_(k-1) satisfies (R2) whenever t_k has finite total variation. For a decreasing positive t_k, the variation telescopes exactly to t_0-lim t_k. This turns an O(t_k) size of the forcing into an O(|t_k-t_(k-1)|) drift of the map; the conversion requires (R8).

For example, an actually proved running equation

    1/t_(k+1)-1/t_k = b+eta_k,
    b>0,    |eta_k| <= b/2

implies t_(k+1)<=t_k and

    0 <= t_k-t_(k+1)=(b+eta_k)t_k t_(k+1)
                       <= (3b/2)t_k^2.                      (R9)

Thus the 1/k^2 budget is justified by an actual cross-step difference, together with (R8), rather than by replacing 1/k in (7.6). The O(g_k^2) remainder in the target's (6.11) has to have a proved uniform constant and small enough initial/tail coupling before this deduction is available. An asymptotic formula t_k~C/k alone does not imply a summable variation bound for an arbitrary oscillating sequence.

There is a second possible sufficient mechanism. If actual normalized source/action matching gives

    m_(k+1)(O)-m_k(O)
       = A_(O,k)(t_(k+1)-t_k)+r_(O,k),
    sup_k |A_(O,k)|<infinity,    sum_k |r_(O,k)|<infinity,    (R10)

then Cauchy follows directly. Formula (R10) must be derived with the partition-function derivative included. For a differentiable common-space interpolation with density exp(-S_s) and observable O_s, the exact identity is

    d/ds mu_s(O_s)=mu_s(partial_s O_s)
                     - Cov_(mu_s)(O_s,partial_s S_s).       (R11)

A uniform bound on these two terms for interpolation by t supplies (R10). Gaussian parity alone does not remove the covariance or source derivative. In (7.4), the exact blocked observable must be the normalized conditional expectation under the full fluctuation weight; an unnormalized Gaussian integral with interaction inserted is not that conditional expectation.

## 4. What the reviewed earlier corpus actually supplies

The previous review read all 12 distinct `sources`-group proofs in the G19 corpus manifest, not merely their scope sections. The strongest relevant cancellations are real, but none of those proofs establishes (R2), (R8), or (R10) for the coupled continuum RG trajectory.

* `G19_CONDITIONAL_GRADIENT_REPAIR_20260905.md`, lines 173-216, proves a quadratic loss for a separated 2x2 coarse/fiber form: lambda_max L(A,B,c)<=A[1+c^2/(1-theta)] when B<=theta A. Lines 236-258 explicitly make c_k=M_k/kappa_k=O(g_k^2) an additional actual-RG estimate. Its sum c_k^2 is a configuration-form product budget. It is not a bound on successive expectations; its square cannot be transferred into (7.6).
* `G19_TRUE_GROUND_LOCALIZED_WILSON_SCORE_20260905.md`, lines 116-118 and 150-162, proves A_1 Phi_0=0 for the actual fixed two-loop ground: the bracket contraction is [Q,Q]=0. This removes its first ground correction. Lines 456-464 use centered independent product conditional scores to remove cross terms and obtain an additive common-Gauss chart bound. These proofs do not identify consecutive interacting scales or show cancellation of a general observable's O(g_k^2) correction.
* `wilson-spatial-schur-excess.md`, lines 254-286, derives full second-order ground jets and an actual fixed-complex O(g^3) quasimode remainder. Lines 288-305 state the source-straightening dependence of the full operator coefficient. Lines 480-499 correctly observe that O(g_j^3), unlike a generic O(g_j^2) bound under logarithmic running, is summable, and require the complete generated form, clock, vacuum, sources, and memory to be matched. This is a viable stronger target for r_k and e_(O,k), not an already proved uniform coupled-scale estimate.
* The same note, SP20-SP25, lines 414-476, supplies exact gap/frame/observable-amplitude iteration once actual scale comparison and summable source errors are available. It explicitly distinguishes a complete frame from preservation of each chosen observable and from convergence of physical energies/correlation measures. `G19_LITERAL_ENDPOINT_COMPLETE_WINDOW_20260905.md` supplies complete-window transport under its exact matched hierarchy and summable inverse-fast-energy budget; this likewise does not construct the successive reference/action/source drift needed here.

Accordingly, the earlier proofs suggest two precise repair routes: prove full second-order matched remainders O(g_k^3) uniformly, or prove common-space Lipschitz dependence of the complete actual RG map on t_k=g_k^2 and bounded variation of all remaining parameters. Merely citing either quadratic Schur loss or local ground parity leaves (7.6)->(7.3) unjustified.

## 5. Incompatible polymer-weight and mass schedules

The target defines a_k=a_0 L^(-k), L>=2 (actually L=3), in (2.5), lines 72-73. Lines 290-291 set

    kappa_(k+1)=(3/4)kappa_k,
    hence kappa_k=kappa_0(3/4)^k -> 0.                    (M1)

In contrast, (8.14), line 430, claims

    (kappa_k-log C4)/a_k = c0 Lambda_QCD >0               (M2)

at all scales. For C4>1, kappa_k-log C4 is negative as soon as kappa_0(3/4)^k<log C4. If kappa_0>log C4, this happens for k>log(kappa_0/log C4)/log(4/3); if it is initially below, failure is immediate. The geometric sum in (8.13) then does not converge. Equations (M1) and (M2) are algebraically incompatible.

Even replacing C4 by 1 does not establish the claimed finite scale-invariant rate: kappa_k/a_k=(kappa_0/a_0)(3L/4)^k diverges for L>=2. It is not c0 Lambda_QCD. A fast covariance rate eta0/a_k does not identify the low-energy physical mass or the polymer weight's flow.

There is also a prefactor obligation before taking a continuum limit. For r_k=kappa_k-log C4>0, the exact geometric sum is

    sum_(n>=ceil(R/a_k)) exp(-r_k n)
       = exp(-r_k ceil(R/a_k))/(1-exp(-r_k)).              (M3)

If r_k~m a_k, its prefactor behaves as 1/(m a_k). The asserted k-independent C(O1,O2) in (8.13) does not follow from this estimate. The number of root cells touched by a fixed physical support and the normalization of the two marked sources require control as well.

### Sufficient mass repair without claiming an exact mass value

If one insists on the counting argument, its schedule must at least obey r_k>=m a_k>0 and compensate the factor in (M3), together with the physical source/root normalization. The exact intended schedule r_k=m a_k would require

    kappa_(k+1)=log C4+(kappa_k-log C4)/L,

not (M1); the RG contraction must be reproved for that schedule.

A cleaner sufficient connected estimate incorporates entropy into the norm from the outset: for the actual normalized two-marked expansion prove, uniformly in k,

    sum_(X meets supp O1 and supp O2)
       exp(m diam_phys(X)) |K_k(X;O1,O2)| <= C(O1,O2),    (M4)

with m>0 in the common physical clock and source normalization. Since diam_phys(X)>=R, this yields |Cov_k(O1,O2)|<=C(O1,O2)exp(-mR) directly, without the extra C4 counting or geometric prefactor. A rooted weighted norm can furnish (M4) if its marked-source insertion and root normalization are actually controlled; the unmarked norm bound alone does not do so.

Together with convergence of the relevant physical-time correlations and the reconstruction hypotheses, such a bound supports a lower mass-gap bound. It does not prove that the exact gap equals c0 Lambda_QCD. Alternatively, the existing SP20-SP25 actual-Hamiltonian scale theorem can transport a positive gap with summable matched errors, avoiding the false identification of a chosen polymer norm weight with a physical eigenvalue.

The precise current stopping point in this proposed proof is therefore: no actual common-space cross-step map/observable estimate converts (7.6)'s O(g_k^2) increments into a summable bound, and its chosen kappa recursion cannot support its displayed mass extraction. The derived repairs specify the missing estimates without assuming they cannot be proved.
