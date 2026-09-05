# Blocking the actual Wilson transfer: a uniform vacuum expansion and a source-visible spectral window

Research continuation, 4 September 2026. Repository read reference:
`8e44da1fbd4b8643a12d514a1fb83ac636edf094`.
No remote files or claim statuses were changed.

## 0. Result and dependency boundary

This note continues `UNIFORM_WILSON_WINDOW.md`, rather than replacing its transfer operator with the auxiliary Hamiltonian. It takes that note's heat-kernel minorization, exact fundamental clock, uniform one-link gap, and fixed-representation convergence as inputs. The abstract hard-core polymer expansion and its marked-correlation estimates are external mathematical inputs, in the precise Kotecky–Preiss/Ueltschi form stated below.

The new construction is nonperturbative in a common, existential, small magnetic-coupling disc. It gives:

* a scalar space-time polymer representation of powers of the **actual** Wilson transfer, with an explicit temporal-mesh-independent convergence test;
* vacuum normalization and bounded local multiplication-source correlations, analytic and exponentially clustering uniformly in spatial volume and the temporal mesh;
* spatially and temporally weighted convergence of these **unprojected** source correlations to those of the Hamiltonian as the temporal mesh tends to zero;
* a nonvanishing three-orientation source Gram matrix inside a fixed **Borel spectral window** around the plaquette energy, by a two-time-moment estimate.

It does **not** yet identify that window as a complete isolated three-component Riesz band. It does not prove totality in that window, a meromorphic source-resolvent extension near the plaquette pole, or matching of the band-projected kernels called h, G, S in G18 in their exponentially weighted spatial norm. A weaker, unweighted Borel-window Gram convergence is obtained in Section 6, conditional on the existing Hamiltonian G18 gap statement. A vacuum gap and a source-populated window are different from an isolated excited band. An explicit counterexample in Section 10 keeps that distinction testable.

The analytical arguments are written here. The accompanying tests check finite algebra, counting, a positive finite-state model, and a declared SU(3) one-plaquette truncation. They do not machine-certify the infinite-volume functional analysis.

## 1. Preserve the exact operator by blocking physical time

Retain

\[
T_{\epsilon,L}(u)=e^{\tau uV_L/2}e^{-\tau K_{\epsilon,L}}e^{\tau uV_L/2},
\quad \tau=\tau_F(\epsilon),\quad
K_{\epsilon,L}=\sum_\ell k_\epsilon(\ell),\quad
V_L=\sum_p v_p,\quad v_p=\chi_p+\bar\chi_p.
\]

Here \(\|v_p\|_\infty\le J=2N\), \(k_\epsilon(F)=C_F/2\), and the spatial Wilson coefficient is \(\beta_s=2Nu\tau\). The temporal coefficient remains \(\beta_t=2N/\epsilon\).

Choose a fixed block duration \(s_0>0\), eventually large enough for the one-link mixing estimate below. With \(0<\tau\le\tau_0\), set

\[
m_\epsilon=\lceil s_0/\tau\rceil,\qquad
s_\epsilon=m_\epsilon\tau\in[s_0,s_0+\tau_0],\qquad
B_{\epsilon,L}(u)=T_{\epsilon,L}(u)^{m_\epsilon}.
\tag{1}
\]

All these are exact definitions. For real u the transfer is positive, injective, self-adjoint, and compact in finite spatial volume. Its largest eigenvalue \(\lambda_{0,L}\) is simple, by the strictly positive continuous kernel. If \(b_{0,L}=\lambda_{0,L}^{m_\epsilon}\), then

\[
-\frac1{s_\epsilon}\log(B_{\epsilon,L}/b_{0,L})
=-\frac1\tau\log(T_{\epsilon,L}/\lambda_{0,L}).
\tag{2}
\]

Blocking preserves **every** excitation energy and spectral projection. There is no quasi-energy aliasing because the transfer spectrum is positive. We do not invoke a global BCH series or set the logarithm equal to \(K_\epsilon-uV\).

## 2. A physical-time block is uniformly smoothing and mixing

Let \(p_\epsilon\) be the normalized one-link Wilson density and let \(h_t\) be the heat kernel of \(e^{-tC_2/2}\). The previous note establishes, for a fixed \(a\in(0,1/2)\),

\[
p_\epsilon\ge a h_{\epsilon/4},\qquad
\tau/\epsilon\longrightarrow1,\qquad
\|C_\epsilon|_{1^\perp}\|_{2\to2}\le e^{-\gamma\tau},
\quad \gamma=C_F/2.
\tag{3}
\]

### Lemma 1 (uniform convolution smoothing)

For sufficiently small epsilon, every integer \(m\ge1\) satisfies

\[
\|p_\epsilon^{*m}\|_\infty
\le A\left[1+(m\tau)^{-D/2}\right],\qquad D=N^2-1,
\tag{4}
\]

with A independent of epsilon and m.

**Proof.** Put \(r_\epsilon=(p_\epsilon-a h_{\epsilon/4})/(1-a)\), an inversion-symmetric central probability density. Laplace localization also gives the elementary upper bound \(\|p_\epsilon\|_\infty\le C\epsilon^{-D/2}\): the normalizing integral is bounded below by a Gaussian integral on a ball of radius proportional to \(\sqrt\epsilon\).

Expand the convolution power as a binomial mixture. A term with k heat factors contains \(h_{k\epsilon/4}\). If \(k\ge am/2\), its sup norm is at most \(C[1+(m\epsilon)^{-D/2}]\), since convolution by a probability density is an L-infinity contraction. The binomial lower tail \(k<am/2\) has probability at most \(e^{-am/8}\). It contains at least one r factor and hence has sup norm at most \(C\epsilon^{-D/2}/(1-a)\). The elementary finite supremum \(\sup_{x\ge1}x^{D/2}e^{-ax/8}\) absorbs this part into \(C(m\epsilon)^{-D/2}\). Finally tau and epsilon are uniformly comparable. QED.

### Lemma 2 (arbitrarily small coarse temporal bonds)

For every \(\delta>0\), one can choose finite \(s_0\) and then sufficiently small epsilon such that

\[
\boxed{\|p_\epsilon^{*m_\epsilon}-1\|_\infty\le\delta.}
\tag{5}
\]

The same choice can include the heat-kernel comparator \(h_{s_\epsilon}\).

**Proof.** Fix a smoothing duration \(t_r>0\) and let \(j=\lceil t_r/\tau\rceil\). Equation (4) bounds \(\|p_\epsilon^{*j}-1\|_2^2\) by a constant \(A_r\). Split the convolution into j, m-2j, j factors. On the zero-mean middle factor use (3), and on the outer factors use their L2 norms. Uniformly in the group argument,

\[
|p_\epsilon^{*m}(U)-1|
\le A_r e^{-\gamma(m-2j)\tau}
\le A_r e^{-\gamma(s_\epsilon-2t_r-2\tau_0)}.
\]

Choose \(s_0\ge2t_r+2\tau_0+\gamma^{-1}\log(A_r/\delta)\), enlarging it for the heat kernel if necessary. QED.

This avoids using the one-fine-step density as a small perturbation of Haar; it is not small as epsilon tends to zero.

### Lemma 3 (uniform free kernel convergence at positive time)

If \(m\tau\to s>0\), then

\[
p_\epsilon^{*m}\longrightarrow h_s
\quad\hbox{uniformly on }SU(N).
\tag{6}
\]

The convergence is locally uniform in s away from zero.

**Proof.** In the binomial decomposition above, the bad part has sup norm bounded by \(C\epsilon^{-D/2}e^{-am/8}\), which tends to zero. Every good part has a heat factor of duration at least a positive constant times s. Its Peter–Weyl tail is uniformly bounded by
\(\sum_{C_R>Q}d_R^2e^{-c s C_R}\), which tends to zero as Q increases. This uses the trace-class heat kernel on the fixed compact group; the other probability convolution factors have multipliers of modulus at most one. On the remaining finite set of irreps, \(\lambda_R^m=e^{-m\tau k_\epsilon(R)}\to e^{-sC_R/2}\). Truncate, pass to the limit, and then remove the truncation. QED.

## 3. Exact free-bridge activities for a full time block

Use the positive-kernel path representation of (1). Conditional on the two coarse endpoint configurations U and U', the free paths on different spatial links are independent Markov bridges. For each plaquette set

\[
F_p(\text{path};u)
=\exp\!\left[u\tau\left(\tfrac12v_p(U_0)+
 \sum_{j=1}^{m-1}v_p(U_j)+\tfrac12v_p(U_m)\right)\right]-1.
\tag{7}
\]

For complex u on a disc,

\[
|F_p|\le b(u):=e^{J(s_0+\tau_0)|u|}-1.
\tag{8}
\]

For a finite set X of distinct plaquettes, define its bridge activity

\[
M_{\epsilon,X}(U',U;u)=\mathbb E_{\epsilon;U',U}\prod_{p\in X}F_p.
\]

Then, exactly and without a representation cutoff,

\[
\boxed{\|M_{\epsilon,X}\|_\infty\le b(u)^{|X|}.}
\tag{9}
\]

If X splits into components with disjoint link supports, its activity is the product of their activities, by independence of the free bridges. Thus the full kernel is

\[
B_{\epsilon,L}(U',U;u)
=\left[\prod_\ell P_{\epsilon,\ell}(U',U)\right]
\sum_{\{X_1,\ldots,X_q\}\ \text{link-disjoint}}
\prod_{i=1}^q M_{\epsilon,X_i},
\tag{10}
\]

where every X_i is connected in the plaquette shared-link graph and
\(P_{\epsilon,\ell}=p_\epsilon^{*m_\epsilon}(U'_\ell U_\ell^{-1})\).
The empty family contributes one. Equation (10) sums **all magnetic orders inside the slab**; it is not a truncation in u.

For later convenience absorb each occupied link's P factor into its magnetic activity:

\[
A_{\epsilon,X}=M_{\epsilon,X}\prod_{\ell\in\operatorname{links}(X)}P_{\epsilon,\ell},
\qquad
\|A_{\epsilon,X}\|_\infty\le[(1+\delta)^4 b(u)]^{|X|}.
\tag{11}
\]

On the links not occupied by a magnetic X, expand \(P_\ell=1+q_\ell\), with \(\|q_\ell\|_\infty\le\delta\). Temporal q bonds and magnetic X atoms in the same slab may not occupy the same link. Magnetic X atoms in that slab must also be link-disjoint. These exclusions remain part of the exact representation; they are not discarded when evaluating weights.

## 4. A uniform space-time polymer criterion

The coarse space-time variables are pairs z=(spatial link, coarse time). A temporal bond q has two sites. A magnetic X atom lies on the two boundary slices of its slab and has at most 8r sites, where r=|X|. Use the auxiliary graph in which cofacial spatial links are neighbors and consecutive time copies of a link are neighbors. Each atom's support is connected in this graph.

In three spatial dimensions a link belongs to four plaquettes, and a plaquette has twelve shared-link neighbors for L>=3. A connected plaquette set of size r containing a fixed plaquette is bounded in number by \(144^{r-1}\): assign a deterministic depth-first traversal of a rooted spanning tree, of length 2(r-1), then bound its choices by \(12^{2(r-1)}\). The visited set recovers X, so this is a valid overcount. Consequently at most \(8\,144^{r-1}\) magnetic atoms of size r contain one coarse site (four root plaquettes and two adjacent time slabs).

Fix \(\xi>0\). If \(b_A\) denotes an atom's sup-norm bound and S_A its site support, then

\[
\sup_z\sum_{A\ni z}b_Ae^{(2+\xi)|S_A|}
\le
2e^{4+2\xi}\delta+\frac{8y}{1-144y},
\quad
 y=e^{16+8\xi}(1+\delta)^4b(u).
\tag{12}
\]

A fully explicit sufficient choice is

\[
\boxed{
\delta\le\frac{e^{-(4+2\xi)}}{16},\qquad y\le\frac1{256}.
}
\tag{13}
\]

Then the right side of (12) is at most

\[
\frac18+\frac1{14}=\frac{11}{56}<\frac14.
\tag{14}
\]

After s_0 is chosen by Lemma 2, (13) holds throughout the nonzero disc

\[
\boxed{
|u|\le u_c:=
\frac1{J(s_0+\tau_0)}
\log\left(1+\frac{e^{-(16+8\xi)}}{256(1+\delta)^4}\right).
}
\tag{15}
\]

Use a smaller closed disc when differentiating. This is an existential, extremely conservative domain, not a claimed practical simulation threshold. The mixing constants determining s_0 have not been evaluated numerically.

### Why (12) really gives a scalar polymer expansion

For a finite space-time torus, write \(\operatorname{Tr}B^M\) as the integral of the product of slab kernels. Take M>=3 to avoid time-identification degeneracies. Expand (10)--(11) and the unoccupied temporal bonds. Group the chosen atoms into connected components under site-support intersection. An admissible connected collection Gamma is one scalar polymer, with weight

\[
w(\Gamma)=\int\prod_{A\in\Gamma}f_A\,d\mu_{\cup_AS_A},
\qquad |w(\Gamma)|\le\prod_{A\in\Gamma}b_A.
\tag{16}
\]

The same-slab exclusions above define admissibility within Gamma. Components with disjoint supports factor under product Haar measure. Therefore the partition function is exactly a hard-core polymer gas; two polymers are incompatible precisely when their supports overlap. Dropping the same-slab exclusions is used only to upper-bound positive sums of absolute values.

For clarity, the atom-to-polymer bound can be proved before invoking the external theorem. Sum rooted atom trees with vertex weight
\(\widetilde b_A=b_Ae^{(1+\xi)|S_A|}\). The rooted-tree majorants obey the increasing iteration

\[
T_A^{(0)}=\widetilde b_A,\qquad
T_A^{(n+1)}=\widetilde b_A
\exp\left(\sum_{B:S_B\cap S_A\ne\varnothing}T_B^{(n)}\right).
\tag{17}
\]

Connected finite atom sets are bounded by these trees: every connected set has a spanning tree, and allowing repeated labels only increases the sum. The exponential accounts for unordered children; equivalently use labeled trees with their factorial weights.

Inductively \(T_A^{(n)}\le b_Ae^{(2+\xi)|S_A|}\), since the exponent in (17) is at most \(|S_A|\sup_z\sum_{B\ni z}T_B^{(n)}\le|S_A|\). Hence

\[
\sup_z\sum_{\Gamma:z\in\operatorname{supp}\Gamma}
|w(\Gamma)|e^{|\operatorname{supp}\Gamma|
 +\xi\sum_{A\in\Gamma}|S_A|}
\le \frac{11}{56}.
\tag{18}
\]

For any fixed polymer Gamma_0, summing over the sites in its support gives the Kotecky--Preiss condition

\[
\sum_{\Gamma\not\sim\Gamma_0}|w(\Gamma)|
e^{a(\Gamma)+b(\Gamma)}\le a(\Gamma_0),
\quad a(\Gamma)=|\operatorname{supp}\Gamma|,
\quad b(\Gamma)=\xi\sum_{A\in\Gamma}|S_A|.
\tag{19}
\]

The abstract hard-core cluster theorem now supplies an absolutely convergent log partition function and its marked versions. This application uses Ueltschi, Theorem 1 and the marked estimates in Theorems 2--3, with incompatibility zeta=-1. All hypotheses and the model-specific summation giving (19) are displayed here. Neither a matrix logarithm nor a noncommutative cluster theorem has been substituted for this scalar path representation.

## 5. Consequences for the actual vacuum, uniformly in the mesh

Add a bounded local multiplication observable as a marked atom \(e^{\theta A}-1\) on a time slice. Its norm is at most \(e^{|\theta|\|A\|_\infty}-1\); choose a small complex theta-disc that fits in the strict margin of (18). Source derivatives of the convergent logarithm give connected correlations. Clusters contributing to two different marks have to connect their supports. The extra b weight in (19) therefore gives

\[
|\langle A B\rangle_c|
\le C_{A,B}e^{-\xi d(S_A,S_B)}.
\tag{20}
\]

Constants depend on the fixed mark supports and norms but not on L, the number of coarse time slices, or epsilon. The series and the bound are locally uniform in complex u strictly inside (15). The thermodynamic and zero-temperature limits of these local multiplication-observable correlations exist and commute: any contribution sensitive to a receding boundary has a connected support reaching that boundary and is bounded by the exponentially small tail in (19).

In a fixed finite spatial volume, the zero-temperature limit is **the actual top transfer eigenvector state**, not an auxiliary state. Indeed B is a compact strictly positive kernel; its Perron eigenvalue is simple, and the normalized trace with finitely many time-zero marks converges to that eigenvector correlation as the number of time slices tends to infinity. The uniform expansion establishes that this identification and the limiting local correlations have a common small-u domain for all volumes.

For real u, positivity of B and (20) imply a uniform gap above the vacuum in energy units. For a centered multiplication source A, its time correlation is a positive moment measure of \(D=B/b_0\):

\[
\langle A\Omega,D^jA\Omega\rangle_c
=\int_{[0,1)}\lambda^j\,d\mu_A(\lambda)
\le C_Ae^{-\xi j}.
\]

Thus \(\operatorname{supp}\mu_A\subset[0,e^{-\xi}]\). In finite volume, bounded multiplication functions times the strictly positive vacuum vector are dense in the Hilbert space. The spectral theorem then yields

\[
\boxed{\operatorname{gap}_{\rm vacuum}(G_{\epsilon,L})
\ge \frac{\xi}{s_0+\tau_0}>0.}
\tag{21}
\]

Use any slightly smaller exponent if desired when combining spatial and time weights. No numerical value is claimed for this conservative gap. This is a fixed-spacing small-u statement. The unique vacuum is gauge invariant and charge even; the same symmetries commute with T as in the preceding notes. Restriction to the physical sector does not invalidate (21).

For the infinite-volume assertion, it suffices here to use the reflection-positive Euclidean/transfer Hilbert space reconstructed from these local multiplication sources. Reflection positivity and the contraction inequalities pass to the limit in each finite quadratic form, so its block transfer is a positive contraction. No blanket identification with all bounded local operators on a separate pre-existing GNS representation is assumed. A possible kernel of the limiting block transfer is not excluded by this argument; every finite energy window below is defined directly by a Borel interval strictly inside the positive transfer spectrum, without taking a logarithm on that kernel. The complete G18 excited-band identification remains a later task.

## 6. Full (unprojected) source-correlation matching

The heat-kernel Hamiltonian comparator at block duration s is \(e^{-s(H_E-uV)}\), with its Brownian Feynman--Kac bridge representation. The same bounds (8)--(19) apply to it with the same s_0, after decreasing the common coupling disc if needed.

### Finite-block kernel matching used in the proof

For each fixed finite plaquette set Y,

\[
[T_{\epsilon,Y}(u)]^{m_\epsilon}(U',U)
- e^{-s_\epsilon(H_{E,Y}-uV_Y)}(U',U)\longrightarrow0
\tag{22}
\]

uniformly in endpoint group variables and locally uniformly for complex u. All links in the finite support of Y are retained; no representation cutoff is imposed.

Here are details justifying the stronger kernel topology. Expand the bounded magnetic exponentials by total insertion number n. Both the discrete ordered sum and the continuous Dyson integral have total absolute weight at most \((s\|V_Y\||u|)^n/n!\). Among their n+1 kinetic gaps, one has duration at least s/(n+1). On that gap use the L1-to-L-infinity estimate (4), tensorized over the finitely many links, and use probability-kernel L1 and L-infinity contraction on the other gaps. Thus the n-th kernel is bounded by

\[
C_Y[1+((n+1)/s)^{D|\operatorname{links}(Y)|/2}]
(s\|V_Y\||u|)^n/n!.
\tag{23}
\]

This is summable on every fixed complex u-disc. For each fixed n, exclude kinetic gaps smaller than a fixed eta; their ordered-time measure tends to zero with eta, and coincident discrete insertions have vanishing total weight as tau tends to zero. The same bound by a longest gap controls the excluded contributions. On the remaining compact time simplex, Lemma 3 and product-kernel contraction give uniform convergence and ordinary Riemann-sum convergence. Take tau to zero, eta to zero, and then sum n using (23). This proves (22).

By finite inclusion--exclusion, M_X is the sum of the kernels in (22) with subsets Y contained in X, divided by the free endpoint kernel. In this identity every subset kernel is embedded on the common link space links(X), with the unused links propagated freely; the denominator is the free kernel on that same space. That denominator is at least \((1-\delta)^{|\operatorname{links}(X)|}\). Therefore each fixed atom converges uniformly, including complex u. Each finite scalar polymer consequently converges. The uniform weighted bound (19) permits termwise limits of the normalized marked expansion.

### Theorem (weighted source-correlation matching)

For the normalized literal odd sources \(O_{x,\alpha}=(\chi_{p(x,\alpha)}-\bar\chi_{p(x,\alpha)})/\sqrt2\), define their infinite-volume, vacuum-normalized, **unprojected** matrices

\[
C^W_{\epsilon,j;\alpha\beta}(x;u)
=\langle O_{0,\alpha}\Omega_\epsilon,
 D_\epsilon^j O_{x,\beta}\Omega_\epsilon\rangle,
\quad j\ge0,
\tag{24}
\]

and the corresponding Hamiltonian matrices \(C^H_{j;\alpha\beta}(x;s_\epsilon,u)\), with time \(j s_\epsilon\). Odd one-point functions vanish. For some positive mu and nu, independent of epsilon,

\[
\boxed{
\sum_{j\ge0}\sum_x e^{\mu|x|_1+\nu j}
\max_{\alpha,\beta}
|C^W_{\epsilon,j;\alpha\beta}(x;u)
-C^H_{j;\alpha\beta}(x;s_\epsilon,u)|\longrightarrow0.
}
\tag{25}
\]

The convergence is locally uniform in a common small complex u-disc. A safe choice takes exponents strictly smaller than those supplied by (20). For example, the auxiliary cofacial-link graph gives a spatial displacement of at most two lattice units per step and a time displacement of at most one; use mu<xi/8 and nu<xi/4 and absorb fixed source radii into the prefactor. The resulting exponential envelope is summable over x and j. Fixed x,j convergence follows from the polymer argument; dominated convergence proves (25).

Thus one now has an all-orders, spatially weighted matching of the **full source correlations**, rather than only of their fixed-u Taylor coefficients. No O(epsilon^2) rate for (25) is asserted; fixed-support constants in (23) have not been optimized jointly with the support tails.

### Corollary: continuous-time and thermodynamic limits for the source measures

For each momentum fiber, the matrices C_j are the moments of a positive finite matrix measure on [0,1], in the variable \(\lambda=e^{-s_\epsilon E}\). The uniform convergence of every C_j and the uniform bound on C_0 imply convergence against every continuous function of lambda: first approximate it uniformly by a polynomial, use moment convergence, and then bound the approximation error by the source norm. Polarization gives the matrix statement. No analytic continuation of a Laplace transform is used.

Consequently the source energy measures converge against every continuous compactly supported function of E. If a sequence of integers n_epsilon satisfies \(n_\epsilon\tau\to t>0\), its actual fine-time correlation is the integral of \(\lambda^{n_\epsilon/m_\epsilon}\). These functions converge uniformly on [0,1] to \(\lambda^{t/s_0}\). Hence the local source correlators converge at **every fixed positive physical time**, not only at the displayed coarse multiples. The t=0 statement is C_0 convergence. The uniform space-time cluster estimates allow the spatial thermodynamic and zero-temperature limits to be interchanged with this temporal limit for these fixed local source correlators.

The source spectral measures therefore match in the continuous-time limit after the spatial thermodynamic limit. This is stronger than the previous fixed-finite-volume product formula, but it still does not imply that every finite-epsilon measure already has an isolated pole.

There is also a useful weaker form of projected-source matching. Taking the existing G18 Hamiltonian shell theorem as an additional premise, choose a fixed energy interval I whose endpoints lie in its common external gaps and which contains precisely that complete Hamiltonian shell. Approximate the interval indicator from above and below by continuous functions differing only in small endpoint neighborhoods. Those neighborhoods have zero Hamiltonian spectral weight. The moment convergence then gives

\[
\sup_k\|Z^W_{\epsilon,I}(k,u)-Z^H_I(k,u)\|\longrightarrow0,
\tag{25a}
\]

where the left projection is merely Borel and the right one is the Hamiltonian Riesz projection. The same conclusion holds for the source energy moment with the bounded factor E on I. With the positive source Gram bound, the associated three-source **compressed** Hamiltonian matrices converge in unweighted operator norm. This does not show that the Wilson source-generated subspace is invariant or exhausts its window. Nor does (25a) establish convergence in the exponential spatial norm: applying a sharp spectral cutoff is exactly where the unresolved excited-spectrum localization enters.

## 7. A nonperturbative, uniformly source-visible plaquette window

This section uses only the first three time moments of the actual source correlator. It does not assume an isolated excited band.

For SU(3), let \(E_s=8/3\), \(c_\epsilon=e^{-s_\epsilon E_s}\), and let C_j(k,u) be the spatial Fourier matrices of (24). At u=0, the calibrated physical plaquette states are exact eigenstates and are orthonormal, so

\[
C_0(k,0)=I_3,\quad C_1(k,0)=c_\epsilon I_3,
\quad C_2(k,0)=c_\epsilon^2 I_3.
\]

Set

\[
\mathcal V_\epsilon(k,u)
=C_2-2c_\epsilon C_1+c_\epsilon^2C_0.
\tag{26}
\]

For real u it is positive semidefinite, since it is the Gram form of \((D_\epsilon-c_\epsilon)O\Omega_\epsilon\). It vanishes at u=0. Analyticity on a symmetric real interval implies its first derivative there is zero: apply positivity to every quadratic form for both signs of u. Thus a common Cauchy estimate in the spatially weighted norm gives

\[
\|\mathcal V_\epsilon(\cdot,u)\|_{\mu,\sharp}\le K u^2,
\qquad C_0(k,u)\succeq\tfrac34 I_3
\tag{27}
\]

on a sufficiently small common coupling interval. More explicitly, on a circle |u|=R within the cluster domain let \(M_j\) uniformly bound \(\|C_j\|_{\mu,\sharp}\). One may take
\(M_V=M_2+2M_1+M_0\), \(K=2M_V/R^2\), and require \(|u|\le R/2\) and \(2M_0|u|/R\le1/4\).

Take any fixed \(0<\Delta< E_s\), for example \(\Delta=1/12\), and let
\(I_\Delta=(E_s-\Delta,E_s+\Delta)\). The distance, in block-transfer eigenvalue, from c_epsilon to the complement of this energy window is at least

\[
d_* = e^{-(s_0+\tau_0)E_s}(1-e^{-s_0\Delta})>0.
\tag{28}
\]

In infinite volume the notation for the energy-window projector means exactly the block-transfer projector on \( (e^{-s_\epsilon(E_s+\Delta)},e^{-s_\epsilon(E_s-\Delta)})\); no global logarithm assumption is required. Functional calculus gives

\[
1_{I_\Delta^c}(G_\epsilon)
\le d_*^{-2}(D_\epsilon-c_\epsilon)^2.
\]

For the matrix spectral measure of the three sources, write
\(Z_{\epsilon,I}(k,u)=J_\epsilon(k,u)^*
1_{I_\Delta}(G_\epsilon(k,u))J_\epsilon(k,u)\). Then

\[
\boxed{
Z_{\epsilon,I}(k,u)\succeq C_0(k,u)-d_*^{-2}\mathcal V_\epsilon(k,u)
\succeq\tfrac12 I_3
}
\tag{29}
\]

provided also \(K u^2\le d_*^2/4\). This holds on every finite-volume momentum grid, uniformly in L and epsilon, and in the infinite-volume energy--momentum decomposition almost everywhere. Equivalently one can define the fiberwise matrix spectral measures by the Hausdorff moments C_j(k,u); their positivity is inherited from finite volumes.

The estimate is for the stated normalization and concerns absolute projected source norms. It is not a claim that one rank-one carrier has a positive 3-by-3 Gram matrix. The projection here includes the whole energy window, and can contain more states than the three source-generated directions.

**What is now proved:** the actual Wilson theory has a three-orientation source-visible spectral window around the calibrated plaquette energy, in a common sufficiently small coupling interval. A loss of all local Wilson-source weight into unrelated energies is excluded there.

**What is not proved:** that this window is separated from the rest of the spectrum, that its range equals the three-component source frame, or that a unique internal carrier sheet has been identified in it. The source-window synthesis map is bounded below and gives a closed embedded copy of the three-component coefficient space, but its range need not be reducing for the transfer Hamiltonian.

## 8. Why blocking does not quietly change the continuum question

The number of fine steps m grows while their physical duration stays finite. Equation (2) makes blocking an exact power of the same regulator, not a replacement by a heat-kernel action. The heat-kernel Hamiltonian enters only as the limit in (22) and (25). The coupling u remains in an existential strong-coupling interval, at fixed spatial spacing. No spatial continuum trajectory, physical anisotropy renormalization, or spin-one rather than spin-three identification is obtained.

## 9. The precise remaining excited-band task

The uniform vacuum normalization and full source-correlation sum are no longer missing. What remains is a **spectral localization / totality theorem for the excited window**. One direct target is the vacuum-dressed block transfer acting on exact-support excitation coefficients: a rooted operator bound small enough on a contour around \(e^{-s_\epsilon E_s}\), followed by the GNS/Euclidean range identification.

A second, equivalent research direction is a convergent irreducible source-tube kernel with analytic continuation to the plaquette spectral neighborhood. The massless-looking singularity of the internal q(k) splitting should be treated only after the complete external window has been isolated. Bounds near transfer eigenvalue 1 that establish a vacuum gap do not reach that neighborhood automatically.

Once that missing Riesz/totality step is proved, the previous coefficientwise matching and relative-q(k) arguments can be used for the band-projected kernels. This note must not be registered as closure of every part of G18 or G19.

## 10. Negative control: summed correlators still need not identify an isolated pole

Let \(E_s>\Delta>0\) and

\[
\mu_\eta=(1-\eta^2)\delta_{E_s}
+\frac{\eta^2}{2\Delta}1_{[E_s-\Delta,E_s+\Delta]}(E)\,dE.
\tag{30}
\]

These positive measures have a common gap above zero. Their Laplace transforms converge, at order eta^2, to \(e^{-E_s t}\), even in an exponentially weighted time sum with weight exponent below \(E_s-\Delta\). Yet every eta>0 has continuous spectral weight arbitrarily close to E_s; the central atom is not an isolated spectral point. An even stronger alternative replaces the central atom by a shrinking continuous interval and gives converging moments with no atom at any eta>0. The first version is included in the numerical checks.

This is not a proposed Wilson spectrum. It is a counterexample to the inference that the results in Sections 5--7, by themselves, prove the final isolated-band statement. Separately, a fourth state at energy E_s+Delta/2 orthogonal to all three sources leaves their positive 3-by-3 window Gram matrix unchanged while making the full window four-dimensional. This finite counterexample tests why source positivity is not totality.

## 11. External inputs and provenance

* `UNIFORM_WILSON_WINDOW.md`, Sections 2--4: heat-kernel minorization, uniform calibrated one-link gap, low-energy shell, fixed-irrep convergence. The accompanying archive is the preceding conversation deliverable.
* Revision 6, Theorem 1 and equations (2)--(4): canonical Hamiltonian, normalized odd plaquette source, and physical free shell.
* D. Ueltschi, *Cluster expansions & correlation functions*, Moscow Mathematical Journal 4 (2004), 511--522, arXiv:math-ph/0304003v3, Theorems 1--3: the abstract hard-core cluster and marked-correlation estimates. The model-specific atom decomposition and criterion are proved here.
* R. Kotecky and D. Preiss, *Cluster expansion for abstract polymer models*, Communications in Mathematical Physics 103 (1986), 491--498, DOI 10.1007/BF01211762: the convergence criterion underlying the invoked theorem.
* R. Buzano and L. Yudowitz, *Gaussian upper bounds for the heat kernel on evolving manifolds*, arXiv:2007.07112: only the static compact-group heat estimates, already used in the prior note.

The proof does not invoke Yarotsky's Hamiltonian perturbation theorem as a theorem about a Wilson logarithm. It instead uses positivity, exact time blocking, independent free bridges, and a scalar space-time cluster expansion.
