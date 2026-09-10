# Exact blocking and a martingale repair of continuum convergence

Proof audit and further repair, 2026-09-09. The conclusions below distinguish a proved abstract convergence criterion from its unproved identification with the actual interacting continuum cutoff family. The cited source proofs are preserved unchanged.

## 1. What exact normalized blocking does prove

Let X_f,X_c be standard Borel configuration or full-history spaces, let pi:X_f->X_c be the actual deterministic blocking map, and let mu_c=pi_#mu_f. Let R(y,dx) be a regular conditional fine law given pi(x)=y. The exact blocked observable is

    B O(y)=int O(x) R(y,dx),
    int O dmu_f=int B O dmu_c.                           (B1)

In coordinates (y,z) where the fine law has density exp(-S_f(y,z)) against the appropriate coarea/reference measure, the conditional normalization is essential:

    B O(y)= int O(y,z) exp(-S_f(y,z)) dnu_y(z)
              / int exp(-S_f(y,z)) dnu_y(z).             (B2)

The denominator generates the exact coarse action. The entire interaction, Jacobian and gauge-compatible reference must occur in both integrals. This is the correct conditional-expectation interpretation of the target document's (7.4), lines 329-331. Its displayed unnormalized fluctuation integral alone does not establish (B1).

For two successive exact deterministic blockings, conditional expectations obey the tower property on the original fine probability space. No spatial Markov property is needed. This removes disconnected normalization factors exactly, but it compares observables under pushforwards of the *same* fine law. It does not, by itself, compare two independently specified UV-cutoff measures.

## 2. Exact corpus evidence: history pushforward versus endpoint compression

`G19_OS_BLOCKING_AND_REVERSE_MASS_MATCHING_20260905.md`, lines 106-120, starts with the explicit premise

    mu_c=P_#mu_f

on full configurations, together with reflection adaptation, positive-time support preservation and time-translation covariance. Its equation (5), lines 128-137, proves the exact OS isometry by this pushforward identity. Equations (6)-(7), lines 138-156, then prove

    T_f^b J=J T_c,       T_f J=J T_c^(1/b).

The proof explicitly distinguishes a true pushforward history law from agreement of time-zero marginals. It is a valid one-step theorem. It does not construct a common actual Wilson family at all refinement cutoffs. Lines 200-225 leave the actual reflection-positive RG trajectory, effective transfer and full source matching as premises of its forward/backward meeting theorem.

`G19_LITERAL_ENDPOINT_COMPLETE_WINDOW_20260905.md`, equation (3), lines 41-50, identifies

    C_tau f(U)=E[f(U_tau)|U_0=U]

under one actual stationary fine quantum-ground process. Its equation (17), lines 285-294, proves

    C_(tau+sigma)-C_tau C_sigma
       =J*exp(-tau h)Q exp(-sigma h)J.                   (B3)

At equal times this vanishes exactly when the retained projection reduces h. Lines 306-312 explicitly distinguish the Markov chain obtained by composing C_tau from the actual projected fine multitime history. Thus endpoint composition cannot replace the full-history conditional tower. It gives neither the required filtration nor projective consistency between different Hamiltonians/cutoffs. The exact compatible hierarchy in its (21), lines 366-385, is an additional premise of the scale theorem.

The previously reviewed 12 source-family proofs contain actual finite/additive identities, source frames and conditional hierarchies, but no construction of projectively consistent interacting Wilson measures across arbitrarily fine lattice spacings. The new SC17 physical-time result does supply an actual common infinite-volume history law at each fixed allowed coupling and fixed spacing. Successively blocking that already constructed law admits a genuine tower/reverse-martingale argument. That is an infrared coarsening of one fixed-spacing law; it does not identify the different microscopic laws of a continuum refinement trajectory.

## 3. A noncircular projective-family criterion

For each n>=0 let X_n be standard Borel, let pi_n:X_(n+1)->X_n be specified measurable refinement-to-coarse maps, and let mu_n be the *actual* normalized law at cutoff n. Assume the independently checkable identities

    (pi_n)_#mu_(n+1)=mu_n.                              (B4)

Compositions must be the chosen multi-step blocking maps. Define finite joint distributions by sampling x_N with law mu_N and setting x_n=pi_n ... pi_(N-1)x_N for n<N. Equation (B4) makes these distributions consistent as N changes. The countable product-extension theorem therefore constructs a common probability law on sequences (x_0,x_1,...), concentrated on pi_n x_(n+1)=x_n, with every prescribed marginal mu_n. This constructs the common law from cutoff data; it does not assume a continuum measure in advance.

Write F_n=sigma(x_n), completed under that law. Compatibility makes F_n increasing. Let R_n be the actual conditional refinement kernel for mu_(n+1) given x_n. If actual normalized observables O_n satisfy

    O_n(x_n)=int O_(n+1)(x_(n+1)) R_n(x_n,dx_(n+1)),
    sup_n int |O_n|^2 dmu_n < infinity,                 (B5)

then M_n=O_n(x_n) is an L2-bounded martingale. Its increments are orthogonal, so for N>n,

    E|M_N-M_n|^2=E|M_N|^2-E|M_n|^2.                    (B6)

The nondecreasing norms are bounded. Hence M_n is Cauchy in L2 and has a limit M_infinity. The exact expectations are equal at every n; the substantive conclusion is convergence of the specified renormalized observables themselves. This proof needs no absolute sum of their L2 increments.

It is legitimate to construct consistent laws by choosing refinement kernels supported on pi_n x_(n+1)=x_n. However, unless their resulting marginal is proved to equal the stated interacting Wilson cutoff law, this constructs a different model. Likewise (B5) describes conditional/renormalized sources, not automatically a fixed bare plaquette or an independently discretized continuum field. Identifying that source is a required part of the repair.

The projective probability space is initially an inverse-limit configuration space. Showing that it represents distributional continuum gauge fields, that the chosen observables exist there, and that the necessary Euclidean/OS properties hold remains a separate task. The criterion does not silently identify this space with S'(R4).

### Why exact integration inside every finite cutoff is insufficient

Starting with each finest cutoff N separately gives a triangular family

    mu_n^[N]=(pi_n ... pi_(N-1))_#mu_N,      n<=N.

For fixed N, all tower identities hold. They do not imply

    mu_n^[N+1]=mu_n^[N]

or even convergence as N increases. A minimal counterexample takes every X_n={0,1}, every blocking map the identity, and mu_n^[N] the point mass at the parity of N. Each finite hierarchy is perfectly normalized and internally consistent, with bounded observables and zero within-hierarchy conditional variances, while the expectations of x alternate across cutoffs. Therefore a variance estimate along each finite blocking chain cannot compare different finest-cutoff theories without a cross-cutoff premise.

## 4. Reverse-martingale criterion for one established fine/history law

Let (Omega,mu) be one probability space with decreasing completed sigma-algebras G_0 superset G_1 superset ... generated by nested coarsenings. For Z in L2(mu), set

    M_n=E[Z|G_n].                                      (B7)

Orthogonal projection and the tower property give

    E|M_n-M_(n+1)|^2=||M_n||_2^2-||M_(n+1)||_2^2,
    sum_n E|M_n-M_(n+1)|^2<=||Z||_2^2,
    ||M_n-M_N||_2^2=||M_n||_2^2-||M_N||_2^2.           (B8)

The norms decrease to a finite limit, proving L2 Cauchy convergence. The limit lies in every closed subspace L2(G_n), and its conditional-expectation defining identity against bounded G_infinity-measurable tests identifies it with E[Z|G_infinity]. This is the required reverse-martingale convergence argument at the level needed here.

Thus normalized blocking can replace absolute summability *when it is applied inside one actual nested common law*. Using an unknown continuum law as that common law would be circular. The projective construction in Section 3 is one noncircular way to supply it, provided (B4) is proved for the actual cutoffs.

## 5. A conditional-variance repair with a controlled predictable drift

Exact martingale source compatibility is stronger than necessary. On the common filtered space of Section 3, let M_n be any adapted L2 observables and set

    r_n=E[M_(n+1)-M_n|F_n],
    xi_(n+1)=M_(n+1)-M_n-r_n.                          (B9)

The xi are martingale differences. Suppose

    sum_n ||r_n||_2 < infinity,
    sum_n E|xi_(n+1)|^2 < infinity.                     (B10)

Then for N>n, orthogonality of the xi and the triangle inequality give

    ||M_N-M_n||_2
      <=sum_(j=n)^(N-1)||r_j||_2
         +[sum_(j=n)^(N-1)E|xi_(j+1)|^2]^(1/2).        (B11)

Consequently M_n and its expectations converge. The variance term is exactly

    E|xi_(n+1)|^2=E Var(M_(n+1)|F_n).                  (B12)

This is a useful place for actual conditional block-gap estimates. If the true refinement conditional measures obey

    Var_(R_n(x,.))(f) <= gamma_n^(-1) E_(fast,n,x)(f,f),

then

    E|xi_(n+1)|^2
       <= gamma_n^(-1) int E_(fast,n,x)(O_(n+1),O_(n+1)) dmu_n(x). (B13)

A summable bound on the right, plus the separate drift bound in (B10), proves convergence. For g_n^2=O(1/n), conditional fluctuation variances O(g_n^4) are summable. A predictable drift O(g_n^3), O(|g_(n+1)^2-g_n^2|) along a bounded-variation coupling, or an exactly vanishing drift is also sufficient. A generic O(g_n^2) predictable drift is not controlled by the variance term. Conditional centering is the missing structural fact; one cannot square an uncentered expectation increment.

For the actual refinement kernels, r_n is explicitly

    r_n(x_n)=R_n O_(n+1)(x_n)-O_n(x_n).                (B14)

Thus (B10) is a concrete source-matching estimate, rather than an assumption that the desired expectations converge. It requires the true conditional measure and the actual normalized observable. The fixed/additive conditional identities in the reviewed G19 sources and the fixed-spacing SC17 estimates supply valid ingredients in their stated regimes; none identifies the actual cross-cutoff kernels and proves (B13)-(B14) uniformly along the continuum trajectory.

## 6. Exact point reached

The martingale strategy is mathematically viable and more flexible than absolute summability of all raw increments. It becomes applicable after proving either:

1. actual projective consistency (B4) and L2-bounded exact source compatibility (B5); or
2. a common actual cross-cutoff coupling/filtration with summable conditional variances (B12)-(B13) and summable predictable source drift (B14).

The reviewed exact OS pushforward theorem supplies the one-step identity under precisely the first missing premise. The literal endpoint theorem supplies true two-time conditional transitions but also proves their temporal memory, so it cannot substitute for the needed history hierarchy. No reviewed proof presently discharges that cross-cutoff identification. This leaves a precise derivation to attempt, without treating martingale convergence itself as unavailable or assuming that the continuum family cannot be constructed.
