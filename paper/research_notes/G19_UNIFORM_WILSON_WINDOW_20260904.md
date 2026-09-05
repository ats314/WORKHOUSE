# Uniform low-energy Wilson kinetic window and spatially weighted shell matching

**Research continuation — 4 September 2026**  
**WORKHOUSE reference checked:** `31255abac3829cb0cc1ce7c36c1852db8cdafbea`  
**Remote changes:** none.

## Result boundary

The uniform free kinetic window is established analytically, with an existential temporal-step threshold, for each fixed SU(N), N >= 3, uniformly in periodic spatial volume. The proof excludes all high representations; it does not extrapolate a finite representation scan.

For the actual symmetric Wilson transfer operator, this note derives its complete second-order charge-odd shell operator at finite temporal step, its first-order literal-Wilson source Gram matrix, and an O(epsilon^2) matching theorem at every fixed magnetic Taylor order in a spatially weighted norm. The latter is coefficientwise, not a summed nonperturbative theorem.

For SU(3), using the existing G18 construction as an upstream premise, the auxiliary Hamiltonians K_epsilon-uV have complete dressed-shell/source matching nonperturbatively at sufficiently small u. They are NOT the logarithms of the symmetric Wilson transfer operators. Establishing the corresponding summed statement for the actual Wilson transfer operator still requires a uniform discrete-time, marked-cluster construction. The remaining estimate is stated in Section 10. No G18/G19 status is changed here.

## 1. Definitions retained from the supplied matching note

Fix N. Haar measure is normalized and tr_F(T_a T_b)=delta_ab/2. Write

\[
 H_E=\frac12\sum_\ell C_2(\ell),\qquad H(u)=H_E-uV,
 \qquad V=\sum_p(\chi_p+\bar\chi_p).
\]

Put D=N^2-1, and define

\[
 p_\epsilon(U)=Z_\epsilon^{-1}e^{-\phi(U)/\epsilon},\qquad
 \phi(U)=2(N-\operatorname{ReTr}U),\qquad
 C_\epsilon f=p_\epsilon*f.
\]

This is the supplied temporal Wilson density at beta_t=2N/epsilon; the constant e^(2N/epsilon) has canceled. On the Peter--Weyl summand of R, C_epsilon acts by

\[
 \lambda_R(\epsilon)=\frac1{d_R}\int p_\epsilon(U)\bar\chi_R(U)\,dU.
\]

Every multiplier is strictly positive and at most one. Positivity follows by expanding exp[(chi_F+chi_Fbar)/epsilon] in tensor-product characters; every irrep appears. The contraction bound follows from the probability density. Inversion gives lambda_R=lambda_Rbar.

Define the calibrated clock and one-link energy by

\[
 \tau=\tau_F(\epsilon)=-\frac{2}{C_F}\log\lambda_F(\epsilon),\qquad
 k_\epsilon(R)=-\frac{\log\lambda_R(\epsilon)}{\tau},\qquad
 C_F=\frac{N^2-1}{2N}.
\]

Then k_epsilon(1)=0 and k_epsilon(F)=k_epsilon(Fbar)=C_F/2 EXACTLY. The supplied fixed-irrep expansion gives

\[
 \tau=\epsilon+O(\epsilon^2),\qquad
 k_\epsilon(R)=\frac{C_R}{2}+O_R(\epsilon^2).
 \tag{1}
\]

The many-link free kinetic operator is

\[
 K_{\epsilon,L}=\sum_\ell k_\epsilon(\ell).
\]

The actual transfer and its finite-volume generator are

\[
 T_{\epsilon,L}(u)=e^{\tau uV_L/2}e^{-\tau K_{\epsilon,L}}e^{\tau uV_L/2},
 \qquad G_{\epsilon,L}(u)=-\tau^{-1}\log T_{\epsilon,L}(u).
 \tag{2}
\]

The spatial Wilson coefficient must be beta_s=2Nu tau, as in the supplied note. At u=0, G_epsilon=K_epsilon. At nonzero u, in general G_epsilon != K_epsilon-uV.

## 2. Uniform high-representation exclusion

### Lemma 1: domination by a narrower heat kernel

Let r(U) be geodesic distance to identity in the bi-invariant metric for which the positive Casimir is -Delta. Let h_s be the normalized heat kernel of exp[-s C_2/2]. There are a_N>0 and epsilon_1>0, independent of R, such that

\[
 p_\epsilon(U)\ge a_N h_{\epsilon/4}(U),\qquad
 U\in SU(N),\quad 0<\epsilon<\epsilon_1.
 \tag{3}
\]

The numerical factor 1/4 is not optimized.

**Proof.** Along a shortest geodesic U=exp(iX), with r(U)^2=2 tr_F X^2,

\[
 \phi(U)=2\sum_j(1-\cos x_j)\le\sum_j x_j^2=r(U)^2/2.
\]

Identity is the unique zero of phi and its Hessian there is positive definite. Compactness, local coordinates, and a Gaussian integral therefore give

\[
 Z_\epsilon\le B_N\epsilon^{D/2}.
\]

The standard Gaussian upper heat-kernel estimate on a compact manifold with nonnegative Ricci curvature gives, for this normalization,

\[
 h_s(U)\le A_Ns^{-D/2}\exp[-r(U)^2/(4s)],\quad 0<s<s_0.
\]

For an explicit primary-source input use Buzano--Yudowitz, Theorem 1.5 and Corollary 1.4, specialized to the static bi-invariant metric (Sc=0, Ric >= 0), and replace their Delta time by s/2. Their estimate with denominator 8t becomes the displayed denominator 4s. Normalizing volume to Haar changes only A_N.

Set s=epsilon/4. The heat kernel is at most A_N 4^(D/2) epsilon^(-D/2) exp[-r^2/epsilon], whereas the Wilson density is at least B_N^(-1) epsilon^(-D/2) exp[-r^2/(2epsilon)]. Their ratio has a positive lower bound independent of epsilon and U. Taking a_N smaller than both this bound and 1/2 proves (3). This is a pointwise density comparison, not an unjustified order comparison between their Fourier coefficients. QED.

### Theorem 2: no bounded-energy representations escaping to infinity

There are c_N>0 and epsilon_2>0 such that, for every irrep R,

\[
 \boxed{k_\epsilon(R)\ge c_N\min\{C_R,\epsilon^{-1}\},
 \quad 0<\epsilon<\epsilon_2.}
 \tag{4}
\]

Consequently, for any fixed E>0, after making epsilon small enough,

\[
 k_\epsilon(R)\le E\quad\Longrightarrow\quad C_R\le E/c_N.
 \tag{5}
\]

Thus one fixed finite set of irreps contains every one-link state in any fixed low-energy window, uniformly as epsilon tends to zero.

**Proof.** For an inversion-symmetric probability density p,

\[
 \langle f,(I-C_p)f\rangle
 =\frac12\int p(U)\|L_Uf-f\|_2^2\,dU.
\]

Apply (3) to this nonnegative integrand. On an R summand,

\[
 1-\lambda_R(\epsilon)\ge a_N(1-e^{-\epsilon C_R/8}).
\]

Use -log x >= 1-x for 0<x<=1, tau<=2epsilon for small epsilon, and

\[
 1-e^{-x}\ge(1-e^{-1})\min\{x,1\}.
\]

Equation (4) follows with, for example, c_N=a_N(1-e^(-1))/16. If epsilon<c_N/E and C_R>=epsilon^(-1), (4) contradicts k_epsilon(R)<=E. Otherwise (4) directly gives (5). The number of dominant weights with bounded quadratic Casimir is finite. QED.

**What is NOT proved:** a lower bound proportional to C_R for all R at fixed epsilon, a numerical value for a_N or epsilon_2, or a bounded operator difference k_epsilon-C_2/2. None is needed for (5).

## 3. The exact physical low-energy window

### Theorem 3: calibrated Wilson kinetic shell

For each fixed N>=3 there is epsilon_0(N)>0 such that, for every 0<epsilon<epsilon_0(N) and every periodic L^3 lattice with L>=3,

\[
 \boxed{\operatorname{spec}\left(K_{\epsilon,L}|_{\mathcal H_{\rm phys}^{(0)}}\right)
 \cap[0,5C_F/2)=\{0,2C_F\}.}
 \tag{6}
\]

The zero eigenspace is the vacuum. The eigenspace at 2C_F is exactly the oriented elementary fundamental-plaquette span. Its neutral charge-odd part has dimension 3L^3 and the free physical external margin is at least C_F/2. Both the energy and the projector are exact, not only asymptotic in epsilon.

**Proof.** Combine Theorem 2 with (1). Fixed-irrep convergence now becomes uniform over every low-energy set. Shrink epsilon_0 to get the three shelves

\[
\begin{aligned}
 k_\epsilon(R)&\ge C_F/2 &&(R\ne1),\\
 k_\epsilon(R)&>5C_F/8 &&(R\notin\{1,F,\bar F\}),\\
 k_\epsilon(R)&>5C_F/6 &&(R\ne1\text{ of zero N-ality}).
\end{aligned}
\tag{7}
\]

There is no infinite family left over in this argument: use (5) with an energy cutoff exceeding all three thresholds; outside that finite set the desired inequalities already hold. Inside it, the first strict Casimir separation and the shelves in Revision 6 apply. In particular C_R>=N for nonzero zero-N-ality representations, and N/2>5C_F/6. The fundamental equality is supplied exactly by the clock.

An energy below 5C_F/2 can have at most four nontrivial links. Gauge invariance forbids degree-one vertices. The original short-cycle argument in Revision 6 then applies unchanged: the connected support is a 3-cycle or a 4-cycle. A 3-cycle is an L=3 winding loop; trivial one-form flux forces zero N-ality, so (7) excludes it. The L=4 straight winding 4-cycle is excluded as well. A remaining 4-cycle is an elementary plaquette and its degree-two intertwiners force the same irrep all around it. The second shelf in (7) excludes every irrep except F and Fbar. Four fundamental link energies give exactly 2C_F. Two nonempty components would require at least six nontrivial links. Orthogonality and the parity count are the same as in Revision 6. QED.

The representation and support classification is inherited from Revision 6, Theorem 1. The new step is the uniform all-irrep exclusion that makes that classification apply to the logarithmic Wilson kinetic energies.

For SU(3), (6) reads

\[
 \operatorname{spec}(K_{\epsilon,L}|_{\mathcal H_{\rm phys}^{(0)}})
 \cap[0,10/3)=\{0,8/3\},\qquad \operatorname{gap}_{\rm ext}^{\rm free}\ge2/3.
\]

## 4. Kinematic contour and volume-uniform free resolvent matching

The G18 construction starts on the factorized kinematic link space, so its contour must be checked there too. In SU(3), the free one-link energies in units of 1/6 start with numerators 4,9,10,16. The additive spectrum immediately around 16 is 14,16,17. The original kinematic 16/6 eigenspace includes nonphysical configurations; it must not be identified with the physical plaquette shell before restriction.

By Theorem 2 and the exact minimum 2/3 per excited link, all configurations below any fixed energy use a bounded number of links with labels in a common finite set. Their energies differ from the Casimir sums by O(epsilon^2), with the constant independent of L. Therefore, after reducing epsilon_0,

\[
 \boxed{\Gamma:\ |z-8/3|=1/12,\qquad
 \sup_{L,\epsilon<\epsilon_0}\sup_{z\in\Gamma}
 \|(K_{\epsilon,L}-z)^{-1}\|\le24.}
 \tag{8}
\]

For example choose epsilon_0 so every relevant finite sum has error below 1/24. Target sums stay within 1/24 of 8/3; the nearest upper competitor stays at least 17/6-1/24. The contour clearance is at least 1/24. All higher sums are excluded by the bounded-energy argument. The contour projector on the kinematic space is exactly the sum of the same Peter--Weyl configurations as the original Casimir projector, because both operators are diagonal in the same basis. After physical/flux/odd restriction it is the same 3L^3-dimensional plaquette projector.

A related result holds in operator norm, uniformly in volume:

\[
 \boxed{\sup_L\|(1+K_{\epsilon,L})^{-1}-(1+H_{E,L})^{-1}\|\longrightarrow0.}
 \tag{9}
\]

To prove it, split configurations at an energy M. If either of their two energies is at most M, their link count and representation labels range over a volume-independent finite list; the inverse-energy difference is at most B_M epsilon^2. If both energies exceed M, bound it by 2/(1+M). Thus

\[
 \sup_L\|(1+K_{\epsilon,L})^{-1}-(1+H_{E,L})^{-1}\|
 \le B_M\epsilon^2+2/(1+M).
 \tag{10}
\]

First let epsilon tend to zero with M fixed, then M tend to infinity. This does NOT give a global O(epsilon^2) rate because B_M has not been bounded as M grows. The common contour gives the corresponding uniform contour-resolvent convergence by the resolvent identity. There is also uniform free semigroup matching for t in compact subsets of (0,infinity), replacing the high-energy tail in (10) by 2 exp(-tM).

## 5. The actual transfer operator's reduced-resolvent weight

A finite-step transfer calculation cannot use 1/(E_m-E_s) unchanged. Let P be a degenerate eigenspace of a free K with energy E_s and let its first-order PVP be scalar, as for the SU(3) odd plaquette shell. Put c=e^(-tau E_s), d_m=e^(-tau E_m). Expansion of T=e^(tau uV/2)e^(-tau K)e^(tau uV/2) gives

\[
 T_1=\frac\tau2(VT_0+T_0V),\qquad
 T_2=\frac{\tau^2}{8}(V^2T_0+T_0V^2)+\frac{\tau^2}{4}VT_0V.
\]

For an intermediate Q_m, the direct plus folded effective-transfer coefficient is

\[
 \frac{\tau^2}{4}(c+d_m)
 +\frac{\tau^2}{4}\frac{(c+d_m)^2}{c-d_m}
 =\frac{\tau^2c}{2}\frac{c+d_m}{c-d_m}.
\]

Taking -log(T_eff)/tau cancels the purely internal (PVP)^2 term and gives

\[
 \boxed{[u^2]G_{\epsilon,\rm eff}
 =-\sum_{m\notin P} d_\tau(E_m-E_s)PVQ_mVP,\qquad
 d_\tau(\Delta)=\frac\tau2\coth\frac{\tau\Delta}{2}.}
 \tag{11}
\]

Vacuum subtraction is performed separately. This formula handles intermediates below E_s by the oddness of d_tau. In the continuous-time limit,

\[
 d_\tau(\Delta)=\Delta^{-1}+\tau^2\Delta/12-\tau^4\Delta^3/720+O(\tau^6).
\]

The formula is a derived transfer identity, not an analogy with the Hamiltonian resolvent.

## 6. Complete second-order odd shell at finite temporal step

The kinetic operator preserves link representations, link-centre charges, and the fundamental equality. The process-completeness classification in Revision 6 therefore remains valid. Define

\[
 w_\rho^W=-\frac{d_\rho}{N^2}d_\tau(C_F+k_\epsilon(\rho)),\quad
 A_W=w_1^W+w_{\rm Adj}^W,\quad
 B_W=w_{\Lambda^2F}^W+w_{\operatorname{Sym}^2F}^W,\quad
 t_W=B_W-A_W.
 \tag{12}
\]

The gap is C_F+k_epsilon(rho) because the intermediate contains six private fundamental links and the shared irrep, against four fundamental links in the external shell. Link-disjoint odd exchange states are still orthogonal and have the same electric energy, so their cross term vanishes. The same-face odd route remains diagonal. Consequently the full off-diagonal operator is exactly t_W times the signed incidence adjacency.

For SU(3), let E_F=8/3 and

\[
 \ell_W=A_W+B_W+2d_\tau(E_F),\qquad
 \sigma_W=-d_\tau(4k_\epsilon(6)-E_F),\qquad
 s_{2,W}=\sigma_W+2d_\tau(E_F)+12\ell_W-4t_W.
\tag{13}
\]

The disjoint vacuum bubble is -2d_tau(E_F); the same-face sextet route is sigma_W. Exactly the original twelve-neighbour/bubble count therefore yields

\[
 \boxed{T_{\le2}h^W_{\epsilon,u}(k)
 =\left(\frac83+u+s_{2,W}u^2\right)I
 +t_Wu^2B(k)B(k)^\dagger.}
 \tag{14}
\]

This is a finite-magnetic-order operator theorem for the ACTUAL transfer generator, without an irrep cutoff, once epsilon lies in Theorem 3's domain. It is not a nonperturbative remainder estimate. In particular the Hodge carrier survives exactly at second magnetic order at finite temporal step, with a regulator-dependent hopping coefficient.

### Exact next kinetic coefficients and matching errors

The script `exact_su3_laplace.py` independently integrates the local Weyl expansion in Cartan variables (a,b,-a-b), with Gaussian exp[-2(a^2+ab+b^2)] and Vandermonde squared. All integrals are exact rational Gaussian moments. To specify the finite calculation explicitly, put x=(a,b,-a-b), d=(a-b,2a+b,a+2b) and

\[
 A_4=\frac1{12}\sum_i x_i^4,\quad A_6=-\frac1{360}\sum_i x_i^6,\quad
 J_1=-\frac1{12}\sum_i d_i^2,\quad
 J_2=\frac1{360}\sum_i d_i^4+\frac1{144}\sum_{i<j}d_i^2d_j^2.
\]

The density corrections are D_1=A_4+J_1 and D_2=A_6+A_4^2/2+J_2+A_4 J_1. Integrate them times the character expansion against the normalized Vandermonde-squared Gaussian. The underlying Gaussian covariance is [[1/3,-1/6],[-1/6,1/3]], its Vandermonde-squared expectation is 3/2, and the normalized D_1,D_2 means are -1/6 and -5/108. For each normalized even-character expansion 1+e f_1+e^2 f_2+e^3 f_3, the cubic normalized integral is

\[
 \langle f_3\rangle+\langle f_2D_1\rangle+\langle f_1D_2\rangle
 -\langle D_1\rangle(\langle f_2\rangle+\langle f_1D_1\rangle)
 +(\langle D_1\rangle^2-\langle D_2\rangle)\langle f_1\rangle.
\]

An unknown third density correction cancels between numerator and denominator. The fundamental, adjoint and sextet characters are Tr(U), |Tr(U)|^2-1, and Tr(U)^2-Tr(U)^*, respectively, divided by their dimensions. This fully specifies the exact finite Gaussian computation. It gives

\[
\begin{aligned}
 \lambda_3&=1-\tfrac23\epsilon+\tfrac1{36}\epsilon^2+\tfrac{13}{648}\epsilon^3+O(\epsilon^4),\\
 \lambda_8&=1-\tfrac32\epsilon+\tfrac{11}{16}\epsilon^2+\tfrac1{96}\epsilon^3+O(\epsilon^4),\\
 \lambda_6&=1-\tfrac53\epsilon+\tfrac{65}{72}\epsilon^2-\tfrac{55}{1296}\epsilon^3+O(\epsilon^4).
\end{aligned}
\]

Hence

\[
 \tau=\epsilon+\frac7{24}\epsilon^2+\frac{13}{144}\epsilon^3+O(\epsilon^4),\quad
 k_\epsilon(8)=\frac32-\frac5{96}\epsilon^2+O(\epsilon^3),\quad
 k_\epsilon(6)=\frac53-\frac5{72}\epsilon^2+O(\epsilon^3).
\]

Substitution in (12)--(13), without fitting any coefficients, gives

\[
 \boxed{t_W=\frac5{612}+\frac{175}{280908}\epsilon^2+O(\epsilon^3),\qquad
 s_{2,W}=\frac{11}{306}-\frac{89159}{2247264}\epsilon^2+O(\epsilon^3).}
 \tag{15}
\]

Since the incidence kernel is finite-range, (15) is a spatially weighted O(epsilon^2) matching statement for the complete second-order matrix, not only for a dispersion at one momentum. One coarse bound is ||BB^dagger||_(mu,sharp)<=4+12 exp(2mu).

A useful cancellation: with an exact heat-kernel kinetic step (k_R=C_R/2), the O(tau^2) hopping correction cancels. Both tensor-product families have the same dimension-weighted mean Casimir, 2C_F. For SU(3),

\[
 t_{HK}(\tau)=\frac5{612}+\frac1{3888}\tau^4+O(\tau^6).
 \tag{16}
\]

This does NOT make the whole operator fourth-order accurate: the heat-kernel flat scalar already has a +(1/9)tau^2 correction at second magnetic order. Under Wilson kinetics the leading hopping error in (15) comes from the calibrated nonfundamental energies.

## 7. Literal Wilson sources: the first Gram correction

Use the same fixed normalization as the source bridge,

\[
 O_p^-=(\chi_p-\bar\chi_p)/\sqrt2,
 \qquad O_p^-\Omega_0=|p,-\rangle.
\]

Let Pi_epsilon(u) be the complete physical odd-shell projection in finite volume, and set

\[
 G^W_{pq}(u)=\langle O_p^-\Omega_\epsilon(u),
 \Pi_\epsilon(u)O_q^-\Omega_\epsilon(u)\rangle.
\]

This is the absolute projected-source Gram matrix, not a normalized spectral fraction.

The first vacuum derivative from transfer perturbation is

\[
 \Omega'_\epsilon(0)=\sqrt2 d_\tau(E_F)\sum_r |r,+\rangle.
\]

Projection of O_p^-|r,+> onto the odd shell vanishes for r!=p. For r=p the SU(3) determinant relation gives -|p,->/sqrt2. Finally P Pi'(0) P=0. Thus

\[
 \boxed{G^W_\epsilon(k,u)
 =I-2u\,d_\tau(E_F)I+O(u^2).}
 \tag{17}
\]

The Hamiltonian coefficient is -2/E_F=-3/4, and

\[
 [u](G^W_\epsilon-G^H)=-\frac49\epsilon^2 I+O(\epsilon^3).
 \tag{18}
\]

This is a volume-independent, momentum-independent source coefficient. A finite plaquette parity-resolved diagonalization independently checks it. It does not, by itself, give a nonperturbative lower bound for the full Wilson source frame.

## 8. Spatially weighted matching at each fixed magnetic order

### Theorem 4: coefficientwise weighted matching

Choose compatible vacuum-normalized, symmetry-covariant complete-shell frames, agreeing at u=0; for example the canonical rank-one-creator Gram frame used in G18. At every fixed n, the linked infinite-lattice Taylor coefficients of the actual transfer and Hamiltonian shell energy, Gram, and source-synthesis kernels exist and obey

\[
 \boxed{
 \|[u^n](h^W_\epsilon-h^H)\|_{\mu,\sharp}
 +\|[u^n](G^W_\epsilon-G^H)\|_{\mu,\sharp}
 +\|[u^n](S^W_\epsilon-S^H)\|_{\mu,\sharp}
 \le A_{n,\mu}\epsilon^2.}
 \tag{19}
\]

For fixed n the constant is independent of sufficiently large periodic volume. The finite-volume coefficients are periodizations once no connected n-insertion support wraps; a sufficient conservative restriction is L>4(n+2). Wrapping small-volume cases are not silently equated with their infinite-volume coefficients.

Here h and S on the Wilson side mean their compatible formal linked coefficients; (19) does NOT assume that their full u-series has a uniform radius or already defines a thermodynamic Wilson band.

**Proof.** (i) An order-n matrix element contains at most n magnetic insertions plus its fixed source marks. Each insertion is a fundamental or antifundamental plaquette. All visited link representations therefore occur in tensor products of a bounded number (at most n plus the fixed source degree) of fundamental factors. There are finitely many such representations and finitely many intertwiner directions. A finite Peter--Weyl truncation containing every such path computes the order-n coefficient exactly; excursions beyond it require additional magnetic insertions. No all-order cutoff is being imposed.

(ii) On this finite space, (1) is an O(epsilon^2) matrix estimate. Symmetric product splitting has logarithm -tau(K_epsilon-uV)+O(tau^3), uniformly for u on a fixed bounded complex disc on this one finite cluster. Therefore its energy generator differs from H_E-uV by O(epsilon^2). The finite-cluster vacuum and complete-shell contour projections, energy kernels, and Gram inverse square roots consequently differ by O(epsilon^2). Cauchy's formula in u gives the same estimate for any fixed coefficient. The contours are fixed energy contours, not shrinking transfer-eigenvalue contours.

(iii) Disjoint link-support components factorize exactly: T_(X disjoint Y)=T_X tensor T_Y, so its logarithm is additive. Vacuum normalization removes disconnected bubbles; a disconnected component containing just one odd source has zero expectation. The complete-shell frame respects this factorization. Thus only linked supports joining the marks contribute. At order n they have uniformly bounded diameter, bounded number of plaquettes, and finitely many rooted placements on a bounded-degree cubic lattice. Apply the finite-cluster estimate to this finite list. Multiplying by exp(mu|x|_1) introduces only a finite factor depending on n, not on L. Algebraic products and inverse-square-root series preserve finite-order linked support. This proves (19). QED.

Nothing in this argument bounds A_(n,mu) as n tends to infinity. Merely checking more magnetic orders does not replace that missing bound.

## 9. A nonperturbative intermediate result, with the operator distinguished

For SU(3), define the auxiliary family

\[
 H^{\rm aux}_{\epsilon,L}(u)=K_{\epsilon,L}-uV_L.
 \tag{20}
\]

Taking the existing G18 coefficient/GNS construction as an upstream input, the same construction can be run uniformly for this family at sufficiently small u. The reasons its hypotheses remain uniform are explicit:

* the vacuum vector and gauge/charge/flux symmetries are unchanged;
* after the original three-link cell grouping and 3/2 rescaling, the onsite gap is exactly one;
* (8) supplies a common externally isolated kinematic shell contour;
* the interaction has the original local bound 27|u| and the same support;
* the free physical seed shell and its energy are exactly unchanged.

Yarotsky's constants depend on the fixed interaction range and the normalized gap, not an upper bound on the onsite spectrum. The G18 rooted resolvent estimates also use the common contour clearance. Thus its same small complex u-disc and a slightly reduced spatial exponent can be selected for the entire auxiliary family. This assertion inherits the G18 analytic construction; it is not an independent reproof of its GNS transport.

Their uniform weighted Taylor majorants, together with finite-order matching, yield

\[
 \|h^{\rm aux}_{\epsilon,u}-h^H_u\|_{\mu,\sharp}
 +\|G^{\rm aux}_{\epsilon,u}-G^H_u\|_{\mu,\sharp}
 +\|S^{\rm aux}_{\epsilon,u}-S^H_u\|_{\mu,\sharp}\to0
 \tag{21}
\]

locally uniformly in that u-disc. A rate is not supplied without order-dependent coefficient bounds. The common positive Gram bound transports the complete source frame.

Equation (21) is useful, but is NOT the requested full Wilson result: (11) proves directly that the actual transfer generator has d_tau(Delta), not 1/Delta. An application of a Hamiltonian stability theorem to (20), followed by calling it the Wilson transfer logarithm, would change the operator under study.

## 10. The remaining actual-Wilson matching estimate

The exact all-orders Wilson statement is not established by this note. A sufficient next result is a discrete-time analogue of G18's vacuum and one-mark contour construction with constants uniform in epsilon. It must construct the actual vacuum and complete Riesz shell, prove totality of the source frame, and bound the linked kernel coefficients. In particular a useful kernel bound would be

\[
 \sup_{0<\epsilon<\epsilon_0}
 \|\Phi^W_{\epsilon,n}\|_{\mu,\sharp}\le MR^{-n},
 \qquad \Phi\in\{h,G,S\},
 \tag{22}
\]

with one M,R,mu, together with the rooted-projection bounds that identify the sums with the actual spectrum. An estimate on formal coefficients alone is not a proof of that identification.

Once (22) and that identification are supplied, Theorem 4 yields for |u|<R

\[
 \|\Phi^W_{\epsilon,u}-\Phi^H_u\|_{\mu,\sharp}
 \le \epsilon^2\sum_{n=0}^m A_{n,\mu}|u|^n
 +\frac{2M(|u|/R)^{m+1}}{1-|u|/R}.
 \tag{23}
\]

Take epsilon to zero at fixed m and then m to infinity. This proves summed weighted matching o(1). A summed O(epsilon^2) rate additionally needs convergence of sum_n A_(n,mu)|u|^n.

A concrete favorable factor in a discrete-time expansion is

\[
 \tau\sum_{j\ge0}e^{-\gamma j\tau}
 =\frac{\tau}{1-e^{-\gamma\tau}}\le\gamma^{-1}+\tau.
 \tag{24}
\]

Thus the divergent number of time slices is not, by itself, an obstruction. This elementary bound is NOT a substitute for the full connected, source-marked expansion; it does not bound all high-energy matrix elements or prove linked cancellations.

When the matched full kernels are available, the previously proved weighted-centering theorem transfers the Hamiltonian carrier to the Wilson carrier: a matching error eta_epsilon(u) in A_mu gives a centered error gamma_mu eta_epsilon(u) q(k). The common carrier gap persists whenever 2 gamma_mu eta_epsilon(u) is less than its Hamiltonian q(k)-coefficient. Source synthesis matching transports its nonzero residues. These implications do not impose a new excluded ball near Gamma.

**Current frontier:** free kinetic pollution is ruled out; finite-order energy and source matching is established. The outstanding part of the requested nonperturbative Wilson result is (22) with its vacuum/Riesz/source identification, not another single-link Casimir test.

## 11. Executed checks and provenance

`verify_kinetic_window_and_shell.py` passed 23 checks. They comprise exact symbolic transfer algebra, exact Gaussian moment coefficients, Casimir/semigroup and contour arithmetic, a 231-irrep SU(3) scan (p+q<=20) at five temporal steps with 384^2 and 768^2 grids, channel-based complete second-order shell predictions, a finite-plaquette literal-source derivative test, and negative controls for moving high-irrep pollution and nonuniform Taylor summation.

The last two temporal steps give matching-error orders 2.01083 for t_W, 2.02489 for the flat scalar, and 2.00526 for the first source Gram coefficient. These numerical observations support the exact expansions; they do not prove the high-irrep theorem, give a rigorous quadrature enclosure, or bound a nonperturbative Taylor tail. No microscopic fourth-order WORKHOUSE coefficient is used.

Sources:

1. Supplied `WILSON_HAMILTONIAN_MATCHING.md`: transfer and clock definitions, fixed-irrep second-order matching, and the stated unresolved high-irrep/weighted-shell task.
2. Revision 6, Theorem 1 and Lemma 22/Theorem 23: physical spin-network support census, flux restriction, process completeness, and the four channel norms. Its kinematic numerator/contour arithmetic is used in Section 4.
3. WORKHOUSE `paper/research_notes/G18_INTERNAL_BBDAGGER_SHEET_CLOSURE_20260830.tex` and `G18_FIXED_SPACING_CARRIER_BRIDGE_INSERT.tex`: the Hamiltonian weighted symbol and complete-frame construction, used as upstream premises, not relabeled as Wilson theorems.
4. R. Buzano and L. Yudowitz, *Gaussian upper bounds for the heat kernel on evolving manifolds*, arXiv:2007.07112, Theorem 1.5 and Corollary 1.4. Only their static nonnegative-Ricci specialization is required here.
5. D. A. Yarotsky, *Quasi-particles in weak perturbations of non-interacting quantum lattice systems*, arXiv:math-ph/0411042, Theorems 1--3, Lemma 1 and equation (14). This applies directly to (20), not directly to the logarithm in (2).

No exhaustive priority claim is made. The results are new derivations within this continuation, not a claim that the component mathematical methods were previously unknown.
