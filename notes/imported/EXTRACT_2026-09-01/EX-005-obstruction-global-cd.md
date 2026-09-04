---
id: EX-005
title: "Obstruction: the global Bakry-Émery / CD(rho, infinity) constant of lattice Yang-Mills diverges to -infinity"
kind: extraction
items: 9
status_breakdown: {"solid": 7, "conditional": 1, "gap": 1}
program: yang_mills
extracted_by: claude-opus-5 subagent, 2026-09-01
stance: preservation (content extraction, not refereeing)
source_files:
  - F:/ANTIGRAVITY/antigravity/playground/scalar-cluster/proof/WILSON/05_proofs_reports/RECOMMENDED_02_Global_BE_Obstruction_and_Localization_v2.md
  - F:/ANTIGRAVITY/antigravity/playground/scalar-cluster/proof/RICCATI/03_stability/lemma_unity_stitched_curvature_rg.md
  - F:/ANTIGRAVITY/antigravity/playground/scalar-cluster/proof/RICCATI/03_stability/lemma_unity_curvature_rg_program.md
  - F:/ANTIGRAVITY/antigravity/playground/scalar-cluster/proof/POLARITY_GRIBOV/GRIBOV_HORIZON/referee_local_horizontal_convexity_BE_gap_and_RG.md
  - F:/ANTIGRAVITY/antigravity/playground/scalar-cluster/proof/RICCATI/01_riccati_flow/referee_riccati_spine_and_sigma_geom_sources.md
  - F:/ANTIGRAVITY/antigravity/playground/scalar-cluster/proof/HAAR/01_haar_mass/02_HAAR_MASS/PROJECT_HIGHLIGHTS_C_Haar_Mass.md
  - F:/ANTIGRAVITY/antigravity/playground/scalar-cluster/proof/HESSIAN/Core_Hessian/03_SU2_Concentration_BadMass.md
  - F:/ANTIGRAVITY/antigravity/playground/scalar-cluster/proof/HESSIAN/Core_Hessian/RECOMMENDED_06_Localization_Theorem_Template.md
  - F:/ANTIGRAVITY/antigravity/playground/scalar-cluster/proof/LSI_POINCARE/02_spectral_gap/02_bakry_emery_to_spectral_gap.md
  - F:/ANTIGRAVITY/antigravity/playground/scalar-cluster/proof/HAAR/01_haar_mass/02_HAAR_MASS/01_haar_mass_hessian_and_gribov_region.md
---

# Obstruction: the global Bakry-Émery / CD(rho, infinity) constant of lattice Yang-Mills diverges to -infinity

> On any closed manifold a non-constant potential forces a strictly negative Hessian direction (via int Delta f = 0), so the best global CD(rho,infinity) constant of the Wilson-Langevin generator obeys rho_glob(beta) <= k_max - beta*lambda with k_max(N) = N/2 exactly for SU(N)^|B| with the bi-invariant metric <X,Y> = -Tr(XY), and lambda >= 2(d-1)/N (2d/N on the gauge-invariant/horizontal sector, exact closed form at finite L) - so rho_glob is already negative for beta > N^2/(4d) and diverges like -(22N/3pi^2) log(1/a Lambda) along the asymptotically free trajectory.

**9 extracted items** — 1 conditional, 1 gap, 7 solid

---

## 1. Lemma A (Compact non-convexity lemma): no non-constant C^2 function on a closed manifold is convex anywhere-to-everywhere

`status: solid` · `kind: theorem`

### Statement

Let $(M,g)$ be a closed (compact, without boundary), connected Riemannian manifold and let $f\in C^2(M)$ be non-constant. Define
$$\lambda_f \;:=\; -\inf_{x\in M}\ \inf_{\substack{Y\in T_xM\\ \|Y\|_g=1}} \nabla^2 f(x)(Y,Y).$$
Then $\lambda_f>0$, the infimum is attained at some $(x^*,Y^*)$ in the unit sphere bundle $SM$, and
$$\nabla^2 f(x^*)(Y^*,Y^*) \;=\; -\lambda_f \;<\;0 .$$
Symbols: $\nabla^2 f$ is the Riemannian (Levi-Civita) Hessian, $\nabla^2f(Y,Y)=\frac{d^2}{dt^2}\big|_{t=0}f(\gamma(t))$ for the geodesic $\gamma$ with $\dot\gamma(0)=Y$; $\Delta f=\mathrm{tr}_g\nabla^2 f$ is the Laplace-Beltrami operator.

### Derivation

This is the rigorous replacement for the corpus argument. The corpus (`lemma_unity_curvature_rg_program.md`, Sec. 1, and its copy inside `lemma_unity_stitched_curvature_rg.md`) argues: "$f$ attains a global maximum at $U^*$; there $\nabla^2 f(U^*)\preceq 0$, so there is a direction $Y$ with $\nabla^2f(U^*)(Y,Y)=-\lambda<0$." That step is **not valid as written**: at a global maximum the Hessian is only negative *semi*definite, and it can vanish identically there (e.g. $f(x)=-x^4$ at $x=0$ in a chart). The conclusion is nevertheless true, and the correct proof is the one hinted at in the task statement, via $\int_M\Delta f=0$. I give it in full.

**Step 1 (the infimum is attained).**
The unit sphere bundle $SM=\{(x,Y): Y\in T_xM,\ \|Y\|_g=1\}$ is a compact manifold (compact base, compact fibre $S^{n-1}$). The map $q:SM\to\mathbb R$, $q(x,Y)=\nabla^2f(x)(Y,Y)$, is continuous because $f\in C^2$ and the Levi-Civita connection has continuous (indeed smooth) Christoffel symbols. A continuous function on a compact space attains its infimum; write $\inf_{SM} q = -\lambda_f$, attained at $(x^*,Y^*)$.

**Step 2 (suppose for contradiction $\lambda_f\le 0$).**
Then $q\ge 0$ on all of $SM$, i.e. $\nabla^2 f(x)\succeq 0$ for every $x\in M$ (a symmetric bilinear form is PSD iff it is $\ge0$ on unit vectors). Taking the $g$-trace,
$$\Delta f(x) \;=\; \mathrm{tr}_g\,\nabla^2 f(x)\;=\;\sum_{i=1}^{n}\nabla^2f(x)(e_i,e_i)\;\ge\;0\qquad\text{for all }x\in M,$$
where $\{e_i\}$ is any $g$-orthonormal frame at $x$.

**Step 3 (the divergence theorem kills it).**
$\Delta f=\mathrm{div}(\nabla f)$, and $M$ is closed, so by the divergence theorem
$$\int_M \Delta f\; d\mathrm{vol}_g \;=\;0 .$$
Combining with Step 2, $\Delta f\ge0$ with zero integral and $\Delta f$ continuous forces $\Delta f\equiv 0$ on $M$.

**Step 4 (harmonic on a closed manifold $\Rightarrow$ constant).**
Integrate by parts against $f$ itself:
$$\int_M \|\nabla f\|_g^2\, d\mathrm{vol}_g \;=\; -\int_M f\,\Delta f\, d\mathrm{vol}_g \;=\;0 .$$
Hence $\nabla f\equiv0$, and since $M$ is connected, $f$ is constant. This contradicts the hypothesis. Therefore $\lambda_f>0$. $\;\blacksquare$

**Remark (a stronger, quantitatively useless but structurally instructive corollary).**
The same trace argument gives more: since $\int_M \mathrm{tr}_g\nabla^2 f\, d\mathrm{vol}=0$ and $f$ is non-constant, the set $\{x:\ \lambda_{\min}(\nabla^2f(x))<0\}$ has *positive measure*, not merely non-empty interior-free intersection. Indeed if $\Delta f$ were $\ge 0$ off a null set we would again get $\Delta f\equiv 0$. So the "bad set" for global convexity is never measure-zero. (This is the reason the corpus's own "defect gas" strategy has to argue that the bad set is *exponentially light under the Gibbs measure*, not that it is empty or null.)

**Remark (why this is the right lemma).** Nothing in Steps 1-4 uses the group structure, the Wilson action, gauge invariance, the dimension, or the volume. The obstruction is therefore not a defect of the particular action: *any* smooth non-constant potential on *any* compact configuration manifold has this property. Any programme whose only positive input is $\mathrm{Ric}\succeq k_{\min}\,g$ plus "$\beta\nabla^2 f\succeq 0$" is dead on arrival at large $\beta$.

### Constants and numbers

No numerical constants; $\lambda_f>0$ is the only output. In the Yang-Mills specialisation of Item D/E, $\lambda_f$ is pinned to $\lambda_f \ge 2(d-1)/N$ (all directions) and $\ge 2d(d-1)/\big(N(d-1+L^{-d})\big)$ (horizontal directions), with $f=S_W$ the Wilson plaquette action, metric $\langle X,Y\rangle=-\mathrm{Tr}(XY)$ on $\mathfrak{su}(N)$.

**Caveat.** The corpus version of this step (global maximum has $\nabla^2f\preceq 0$, hence a strictly negative direction) is a genuine logical gap; only $\preceq 0$ follows. The $\int_M\Delta f=0$ route above repairs it completely. [Repair is mine.]

**Why it matters.** It shows the obstruction is structural, not an artefact of the Wilson action, of $SU(N)$, or of the lattice: global $CD(\rho,\infty)$ with $\rho>0$ is impossible for *any* non-constant potential on *any* closed manifold once the potential is scaled up. Every localisation, typical-set, or 'spark' strategy in the corpus exists because of this one lemma.

---

## 2. Theorem B (Global Bakry-Émery constant diverges): rho_glob(beta) <= k_max - beta*lambda_f -> -infinity

`status: solid` · `kind: obstruction`

### Statement

Let $(M,g)$ be a closed connected Riemannian manifold of dimension $n$, let $f\in C^2(M)$ be non-constant, and for $\beta>0$ let
$$d\mu_\beta \;=\; Z_\beta^{-1} e^{-\beta f}\, d\mathrm{vol}_g,\qquad L_\beta \;=\; \Delta - \beta\,\langle \nabla f,\nabla\,\cdot\,\rangle ,$$
so that $L_\beta$ is the $\mu_\beta$-symmetric (overdamped Langevin) diffusion generator with carré du champ $\Gamma(u)=\|\nabla u\|^2$. Let
$$\rho_{\mathrm{glob}}(\beta)\;:=\;\inf_{x\in M}\ \inf_{\|Y\|_g=1}\Big[\mathrm{Ric}_x(Y,Y)+\beta\,\nabla^2 f(x)(Y,Y)\Big]$$
be the **optimal** curvature-dimension constant, i.e. the largest $\rho$ for which $\Gamma_2(u)\ge\rho\,\Gamma(u)$ holds for all $u\in C^\infty(M)$. Put
$$k_{\max}\;:=\;\sup_{x\in M}\ \sup_{\|Y\|=1}\mathrm{Ric}_x(Y,Y)\;<\;\infty,\qquad \lambda_f\;>\;0 \text{ as in Lemma A}.$$
Then for every $\beta>0$
$$\boxed{\;\rho_{\mathrm{glob}}(\beta)\;\le\;k_{\max}\;-\;\beta\,\lambda_f\;}$$
and consequently
$$\rho_{\mathrm{glob}}(\beta)<0 \quad\text{for all }\ \beta>\beta_*:=\frac{k_{\max}}{\lambda_f},\qquad\qquad \lim_{\beta\to\infty}\rho_{\mathrm{glob}}(\beta)=-\infty,$$
with divergence rate exactly linear in $\beta$: $\ \rho_{\mathrm{glob}}(\beta)/\beta \to -\lambda_f$.

### Derivation

**Step 1 (the displayed $\rho_{\mathrm{glob}}$ really is the optimal CD constant).**
Bochner's formula on a Riemannian manifold gives, for the weighted generator $L_\beta=\Delta-\beta\langle\nabla f,\nabla\cdot\rangle$ and $\Gamma(u)=\|\nabla u\|^2$,
$$\Gamma_2(u)\;:=\;\tfrac12 L_\beta\Gamma(u)-\Gamma(u,L_\beta u)\;=\;\|\nabla^2 u\|_{\mathrm{HS}}^2 \;+\; \big(\mathrm{Ric}+\beta\nabla^2 f\big)(\nabla u,\nabla u).$$
Hence $\Gamma_2\ge\rho\,\Gamma$ for all $u$ **iff** $\mathrm{Ric}+\beta\nabla^2 f\succeq \rho\, g$ pointwise. ("$\Leftarrow$" is immediate from $\|\nabla^2u\|^2_{\mathrm{HS}}\ge0$. "$\Rightarrow$": fix $x$ and unit $Y$; choose $u$ with $\nabla u(x)=Y$ and $\nabla^2u(x)=0$ — take $u$ = the linear-in-normal-coordinates function $u(\exp_x(v))=\langle v,Y\rangle$, cut off away from $x$; then $\Gamma_2(u)(x)=(\mathrm{Ric}+\beta\nabla^2f)(Y,Y)$ and $\Gamma(u)(x)=1$.) So the displayed infimum is the sharp $CD(\rho,\infty)$ constant, and any statement 'the theory satisfies $CD(\rho,\infty)$' entails $\rho\le\rho_{\mathrm{glob}}(\beta)$.

**Step 2 (evaluate at the bad point).**
Let $(x^*,Y^*)$ be the minimiser furnished by Lemma A, so $\nabla^2f(x^*)(Y^*,Y^*)=-\lambda_f$. Because $\rho_{\mathrm{glob}}(\beta)$ is an infimum over all $(x,Y)$, evaluating the bracket at this one point is an upper bound:
$$\rho_{\mathrm{glob}}(\beta)\;\le\;\mathrm{Ric}_{x^*}(Y^*,Y^*)+\beta\,\nabla^2f(x^*)(Y^*,Y^*)\;\le\; k_{\max}-\beta\lambda_f .$$
$k_{\max}<\infty$ because $\mathrm{Ric}$ is continuous on the compact $SM$. This is the boxed inequality. Letting $\beta\to\infty$ gives $\rho_{\mathrm{glob}}(\beta)\to-\infty$; setting the right-hand side $<0$ gives $\beta>\beta_*=k_{\max}/\lambda_f$.

**Step 3 (the rate is exactly $-\lambda_f$, not merely $\le$).**
By the same reasoning with $k_{\min}:=\inf\mathrm{Ric}$,
$$k_{\min}-\beta\,\lambda_f \;\le\;\rho_{\mathrm{glob}}(\beta)\;\le\;k_{\max}-\beta\lambda_f ,$$
the left inequality because $\mathrm{Ric}(Y,Y)+\beta\nabla^2f(Y,Y)\ge k_{\min}-\beta\lambda_f$ pointwise. Hence $\rho_{\mathrm{glob}}(\beta)=-\lambda_f\beta+O(1)$ with the $O(1)$ trapped in $[k_{\min},k_{\max}]$. In particular $\rho_{\mathrm{glob}}$ is a concave, eventually strictly decreasing, affine-asymptotic function of $\beta$ (it is an infimum of affine functions of $\beta$, hence concave). [Step 3 is mine; the corpus states only the upper bound.]

**Step 4 (what this does *not* say).**
On a compact $M$ with smooth positive density, $-L_\beta$ always has a strictly positive spectral gap $\lambda_1(\beta)>0$ (discrete spectrum, connected $M$). The theorem does not say the gap vanishes; it says that the **Bakry-Émery route to lower-bounding it is unavailable**, because the only inequality it delivers, $\lambda_1\ge\rho_{\mathrm{glob}}$, becomes vacuous (negative) beyond $\beta_*$ and then gets worse without bound.

**Step 5 (the negative-curvature fallback also fails, quantitatively).** [This step is mine; the corpus does not carry it.]
Under $CD(-K,\infty)$ with $K=-\rho_{\mathrm{glob}}(\beta)>0$ on a compact manifold of diameter $D$, every known lower bound for $\lambda_1$ in this class (Wang-type coupling estimates, Chen-Wang, the Zhong-Yang/Bakry-Ledoux family) degrades at best like
$$\lambda_1 \;\gtrsim\; \frac{c}{D^{2}}\,e^{-c'\,D\sqrt{K}} .$$
For the lattice configuration space $\mathcal C_\Lambda=SU(N)^{|B|}$ with the product metric the diameter is $D=\sqrt{|B|}\,D_N$ where $D_N=\mathrm{diam}\,SU(N)$ ($D_2=\pi\sqrt2\approx4.4429$ for $\langle X,Y\rangle=-\mathrm{Tr}XY$, i.e. the round $S^3$ of radius $\sqrt2$). With $K\asymp \tfrac{2d}{N}\beta$ this yields
$$\lambda_1\;\gtrsim\;\frac{c}{|B|D_N^2}\exp\!\Big(-c'\,D_N\sqrt{\tfrac{2d}{N}}\;\sqrt{|B|\,\beta}\Big),$$
which collapses **both** as the volume $|B|\to\infty$ **and** as $\beta\to\infty$. So the failure is not only a continuum-limit failure: past $\beta_*$ the global BE machinery already loses volume-uniformity, which is the property the whole finite-cutoff programme was built to have.

### Constants and numbers

General: $\rho_{\mathrm{glob}}(\beta)\le k_{\max}-\beta\lambda_f$; sign change at $\beta_*=k_{\max}/\lambda_f$; asymptotic slope exactly $-\lambda_f$; $O(1)$ offset trapped in $[k_{\min},k_{\max}]$.

Specialised to $d=4$ lattice $SU(N)$ Yang-Mills with $\langle X,Y\rangle=-\mathrm{Tr}(XY)$, $k_{\max}=k_{\min}=N/2$ (Item C), $\lambda_f=2d/N=8/N$ on the horizontal sector in the $L\to\infty$ limit (Item E):
  - $\beta_*=\dfrac{N^2}{4d}=\dfrac{N^2}{16}$: $\ \beta_*=0.25$ for $SU(2)$, $\beta_*=0.5625$ for $SU(3)$, $\beta_*=1.0$ for $SU(4)$.
  - Using only the all-directions constant $\lambda_f\ge 2(d-1)/N=6/N$ (valid at every finite $L$): $\beta_*=N^2/\big(4(d-1)\big)=N^2/12$, i.e. $0.333$ for $SU(2)$, $0.75$ for $SU(3)$.
  - For comparison, production lattice $SU(3)$ simulations run at $\beta\approx 5.7-6.5$: the global BE constant there is already $\rho_{\mathrm{glob}}\le 1.5-\tfrac83\cdot 6.0 = -14.5$.

Diameters: $D_2=\pi\sqrt2=4.44288$; $D_N<\infty$ depends only on $N$.

**Caveat.** Step 5 uses the *shape* $\lambda_1\gtrsim D^{-2}e^{-cD\sqrt K}$ common to the standard negative-curvature eigenvalue bounds; I have not pinned a specific author's constants $c,c'$, so treat the numerical prefactors there as structural rather than certified.

**Why it matters.** This is the headline obstruction. It converts the corpus's four-year programme ('prove uniform convexity, invoke Bakry-Émery, get a volume-uniform mass gap') into a proven impossibility for the *global* version, with an explicit threshold $\beta_*$ below the couplings anyone actually uses. Everything downstream in the corpus (typical-set curvature, Riccati/RG budget laws, localisation templates, 'sparks') exists to route around exactly this inequality.

---

## 3. Proposition C: k_max(N) for SU(N)^{|B|} with the bi-invariant metric - the group is Einstein with Ric = (N/2) Id

`status: solid` · `kind: derivation`

### Statement

Let $\mathfrak g=\mathfrak{su}(N)$ (traceless anti-Hermitian $N\times N$ matrices) carry the $\mathrm{Ad}$-invariant inner product
$$\langle X,Y\rangle_\lambda \;:=\; -\lambda\,\mathrm{Tr}(XY),\qquad \lambda>0,$$
(which is positive definite on anti-Hermitian $X$ since $\mathrm{Tr}(X^2)=-\mathrm{Tr}(XX^\dagger)\le0$), and let $G=SU(N)$ carry the induced bi-invariant metric $g_G$. Then $(G,g_G)$ is Einstein:
$$\boxed{\;\mathrm{Ric}_G \;=\; \kappa_G\, g_G,\qquad \kappa_G=\frac{N}{2\lambda}\;}$$
and for the product $\mathcal C_\Lambda=G^{|B|}$ with the product metric $g_\Lambda=\bigoplus_{b\in B} g_G$,
$$\mathrm{Ric}_{g_\Lambda}=\kappa_G\, g_\Lambda,\qquad\text{hence}\qquad k_{\max}=k_{\min}=\kappa_G=\frac{N}{2\lambda},$$
**independent of the lattice volume $|B|$, of the dimension $d$, and of $\beta$.** In the project's normalisation $\lambda=1$, $\langle X,Y\rangle=-\mathrm{Tr}(XY)$:
$$k_{\max}(N)=\frac N2 .$$

### Derivation

**Step 1 (curvature of a bi-invariant metric).** For a bi-invariant metric on a Lie group, the Levi-Civita connection on left-invariant fields is $\nabla_XY=\tfrac12[X,Y]$ and the curvature tensor is
$$R(X,Y)Z=-\tfrac14\big[[X,Y],Z\big].$$
With $\{E_i\}_{i=1}^{m}$ an orthonormal basis of $\mathfrak g$, $m=\dim\mathfrak g=N^2-1$,
$$\mathrm{Ric}(X,X)=\sum_{i=1}^m\langle R(E_i,X)X,E_i\rangle=\frac14\sum_{i=1}^m\big\|[X,E_i]\big\|^2 ,$$
using $\mathrm{Ad}$-invariance ($\mathrm{ad}_X$ skew-adjoint) to move brackets across the inner product.

**Step 2 (identify the sum with the Killing form).** Since $\mathrm{ad}_X$ is skew-adjoint,
$$\sum_{i}\big\|[X,E_i]\big\|^2=\sum_i\langle \mathrm{ad}_XE_i,\mathrm{ad}_XE_i\rangle=-\sum_i\langle \mathrm{ad}_X^2E_i,E_i\rangle=-\mathrm{tr}\big(\mathrm{ad}_X^2\big)=-B(X,X),$$
where $B(X,Y)=\mathrm{tr}(\mathrm{ad}_X\mathrm{ad}_Y)$ is the Killing form. Hence the standard identity
$$\mathrm{Ric}(X,Y)=-\tfrac14 B(X,Y).$$
(The corpus contains a well-documented sign muddle here — its own contradiction reports flag $\mathrm{Ric}=+\frac14B$ vs $-\frac14B$ in the same theorem; the correct statement is $\mathrm{Ric}=-\frac14 B$, which is positive because $B$ is negative definite on a compact semisimple algebra.)

**Step 3 (Killing form of $\mathfrak{su}(N)$).** $B(X,Y)=2N\,\mathrm{Tr}(XY)$, with $\mathrm{Tr}$ the trace in the defining $N$-dimensional representation. Therefore $\mathrm{Tr}(XY)=-\langle X,Y\rangle_\lambda/\lambda$ and
$$B(X,Y)=-\frac{2N}{\lambda}\langle X,Y\rangle_\lambda \quad\Longrightarrow\quad \mathrm{Ric}(X,Y)=-\tfrac14B(X,Y)=\frac{N}{2\lambda}\,\langle X,Y\rangle_\lambda .$$

**Step 4 (products).** The Levi-Civita connection, curvature tensor and Ricci tensor of a Riemannian product split blockwise with no cross terms. Since every factor is Einstein with the *same* constant $\kappa_G$, so is the product. Hence $k_{\max}=k_{\min}=\kappa_G$ on $\mathcal C_\Lambda$ for every $|B|$. This is the only genuinely volume-uniform positive input the whole programme has.

**Step 5 (sanity check on $SU(2)$).** With $\lambda=1$: take $X_a=i\sigma_a/\sqrt2$; then $\langle X_a,X_b\rangle=-\mathrm{Tr}(X_aX_b)=\tfrac12\mathrm{Tr}(\sigma_a\sigma_b)=\delta_{ab}$, orthonormal. $[X_1,X_2]=-i\sigma_3=-\sqrt2X_3$, so $\|[X_1,X_2]\|^2=2$ and the sectional curvature is $K=\tfrac14\|[X,Y]\|^2=\tfrac12$. Then $\mathrm{Ric}(X_1,X_1)=K(X_1,X_2)+K(X_1,X_3)=1=N/2$. Consistently, $SU(2)$ with this metric is the round $S^3$ of radius $\sqrt2$ (sectional curvature $1/r^2=1/2$, $\mathrm{Ric}=2/r^2=1$). Verified numerically for $N=2,3,4,5$ (see code).

**Step 6 (a normalisation warning that matters for the obstruction).** [Mine.]
Several corpus files add *both* $\mathrm{Ric}\succeq\kappa_G$ *and* a separate 'Haar mass' Hessian $\nabla^2S_{\mathrm{Haar}}\succeq c_0a^2g^2$. These are the same geometric fact counted twice in two different charts. In the intrinsic formulation the reference measure is the Riemannian volume ( = Haar), so the Gibbs measure is $d\mu=Z^{-1}e^{-\beta S_W}d\mathrm{vol}$ with **no** extra $S_{\mathrm{Haar}}$ term, and $\mathrm{Ric}=\tfrac N2\mathrm{Id}$ is the entire geometric contribution. If instead one insists on flat coordinates $U_b=\exp(iagA_b)$ with Lebesgue $dA$, the Jacobian potential $S_{\mathrm{Haar}}(A)=-\log J(A)$ satisfies $\nabla^2_AS_{\mathrm{Haar}}(0)=\tfrac13\mathrm{Ric}\cdot(ag)^2 = \tfrac{N}{6}(ag)^2 I$ — but then $\|A\|$ and $\|X\|$ differ by exactly the factor $ag$, and converting back to the group metric gives $\nabla^2 S_{\mathrm{Haar}}\succeq \tfrac N6 I$, an **$a$-independent $O(N)$ constant**, not $O(a^2g^2)$. Either way the positive part of the BE tensor is an $a$-independent number of order $N$, while the negative part is $-\beta\lambda_f$ with $\beta\to\infty$. So the widely-repeated claim in the corpus that 'the Haar spark $c_0a^2g^2$ vanishes in the continuum' is a normalisation artefact; the true statement is stronger and simpler: *the positive part is bounded, the negative part is not.*

### Constants and numbers

$\kappa_G = N/(2\lambda)$ with $\langle X,Y\rangle=-\lambda\,\mathrm{Tr}(XY)$.
For $\lambda=1$: $k_{\max}(N)=N/2$. Numerically verified (exact to machine precision):
  SU(2): $\dim\mathfrak g=3$, $\mathrm{Ric}=1.000000$;
  SU(3): $\dim=8$, $\mathrm{Ric}=1.500000$;
  SU(4): $\dim=15$, $\mathrm{Ric}=2.000000$;
  SU(5): $\dim=24$, $\mathrm{Ric}=2.500000$.
Derived quantities the corpus uses: $c_H=\kappa_G/3=N/(6\lambda)$ (Haar-Jacobian Hessian at the identity); for $N=3,\lambda=1$: $\kappa_G=1.5$, $c_H=0.5$, $c_H/2=0.25$ (the corpus's SU(3) 'SAFE ball' floor $\kappa_*=0.25$, ball radius $R_0=0.05$).
Other normalisations: $\langle X,Y\rangle=-\tfrac12\mathrm{Tr}(XY)$ ($\lambda=1/2$) gives $\kappa_G=N$; $SU(2)$ round-$S^3$ radius $\sqrt{2\lambda}$.

### Code

import numpy as np, math

def su_basis(N):
    """Orthonormal basis of su(N) for <X,Y> = -Tr(XY)."""
    B = []
    for i in range(N):
        for j in range(i+1, N):
            E = np.zeros((N,N), complex); E[i,j]=1;  E[j,i]=-1; B.append(E)
            F = np.zeros((N,N), complex); F[i,j]=1j; F[j,i]=1j; B.append(F)
    for k in range(1, N):
        d = np.zeros(N, complex); d[:k] = 1j; d[k] = -1j*k; B.append(np.diag(d))
    O = []
    for X in B:
        for Y in O:
            X = X - (-np.trace(X@Y).real)*Y
        O.append(X/math.sqrt(-np.trace(X@X).real))
    return O

for N in (2,3,4,5):
    E = su_basis(N); X = E[0]
    ric = 0.25*sum(-np.trace((X@Ei-Ei@X)@(X@Ei-Ei@X)).real for Ei in E)
    print(N, ric, N/2)   # ->  2 1.0 1.0 ; 3 1.5 1.5 ; 4 2.0 2.0 ; 5 2.5 2.5

**Caveat.** The constant is convention-dependent ($\kappa_G=N/(2\lambda)$); every number quoted downstream must be read with its metric normalisation attached. The corpus is internally inconsistent about $\lambda$ in places.

**Why it matters.** It supplies the explicit, volume-independent $k_{\max}(N)=N/2$ that makes Theorem B a *numerical* statement rather than a qualitative one, and it identifies (Step 6) that the corpus's supposedly-vanishing 'Haar spark' is really a bounded $O(N)$ constant — which strengthens the obstruction and removes a source of confusion in half a dozen files.

---

## 4. Theorem D: explicit sharp negative Hessian direction for the Wilson action (-1/N per plaquette, -2(d-1)/N on the lattice)

`status: solid` · `kind: construction`

### Statement

Let $\mathcal C_\Lambda=SU(N)^{|B|}$ on $\Lambda=(\mathbb Z/L\mathbb Z)^d$ ($N\ge2$, $d\ge2$, $L\ge2$) with the product bi-invariant metric $\langle X,Y\rangle=-\mathrm{Tr}(XY)$, and let
$$S_W(U)=\sum_{p}\Big(1-\tfrac1N\mathrm{Re}\,\mathrm{Tr}\,U_p\Big)$$
be the Wilson plaquette action, $U_p$ the ordered holonomy around $p$.

**(a) Single plaquette, sharp.** For $S_p(U)=1-\tfrac1N\mathrm{Re}\mathrm{Tr}(U)$ on $SU(N)$,
$$\inf_{U\in SU(N)}\ \inf_{\|X\|=1}\ \nabla^2S_p(U)(X,X)\;=\;-\frac1N,$$
and the infimum is **attained** at
$$U_0=\mathrm{diag}(-1,-1,1,\dots,1)\in SU(N),\qquad X=\frac{i}{\sqrt2}\,\mathrm{diag}(1,-1,0,\dots,0)\in\mathfrak{su}(N),\ \|X\|=1 .$$

**(b) Full lattice.** Let $U^*\in\mathcal C_\Lambda$ be the configuration $U^*_{b}=I$ for all links $b$ except a single link $b_0=(x_0,\hat 1)$ where $U^*_{b_0}=U_0$. Let $\mathbf X\in T_{U^*}\mathcal C_\Lambda$ be the unit tangent vector supported on $b_0$ with value $X$. Then
$$\nabla^2 S_W(U^*)(\mathbf X,\mathbf X)\;=\;-\frac{2(d-1)}{N}\qquad(=-6/N \text{ in } d=4),$$
so $\ \inf_{U}\lambda_{\min}\big(\nabla^2S_W(U)\big)\le -2(d-1)/N$, uniformly in the lattice volume.

### Derivation

**Preliminaries.** For a bi-invariant metric, $t\mapsto e^{tX}U$ is a geodesic with $\|\dot\gamma(0)\|=\|X\|$; hence directional second derivatives along such curves *are* the Riemannian Hessian, $\nabla^2f(X,X)=\frac{d^2}{dt^2}\big|_0 f(e^{tX}U)$. We use the left-trivialisation $T_U\mathcal C\cong\bigoplus_{b\in B}\mathfrak{su}(N)$, $\mathbf Z=(Z_b)$, $\|\mathbf Z\|^2=\sum_b\|Z_b\|^2$.

**(a) Computation.** $\frac{d^2}{dt^2}\big|_0\mathrm{Tr}(e^{tX}U)=\mathrm{Tr}(X^2U)$, so
$$S_p''(0)=-\frac1N\,\mathrm{Re}\,\mathrm{Tr}(X^2U).$$
With $U=U_0$ and $X$ as stated: $X^2=-\tfrac12\,\mathrm{diag}(1,1,0,\dots,0)=:-\tfrac12P$, and $\|X\|^2=-\mathrm{Tr}(X^2)=1$. Then $X^2U_0=(-\tfrac12 P)U_0=+\tfrac12 P$ (because $U_0=-I$ on $\mathrm{ran}\,P$), whose trace is $1$. Hence $S_p''(0)=-1/N$. Note $X$ is traceless and anti-Hermitian, so $X\in\mathfrak{su}(N)$, and $\det U_0=(-1)^2=1$, so $U_0\in SU(N)$.

**(a) Sharpness.** Set $H:=-X^2$. For $X$ anti-Hermitian, $H\succeq0$ and $\mathrm{Tr}H=\|X\|^2=1$. Then $-S_p''(0)=\tfrac1N\mathrm{Re}\mathrm{Tr}(X^2U)=-\tfrac1N\mathrm{Re}\mathrm{Tr}(HU)$. By von Neumann's trace inequality, for $H\succeq0$ and $U$ unitary (all singular values $=1$),
$$\big|\mathrm{Tr}(HU)\big|\;\le\;\sum_i\sigma_i(H)\,\sigma_i(U)\;=\;\mathrm{Tr}(H)\;=\;1 ,$$
so $-S_p''(0)\le 1/N$, i.e. $S_p''(0)\ge -1/N$. Equality needs $U=-\mathbb 1$ on $\mathrm{ran}\,H$; since $X\in\mathfrak{su}(N)$ is traceless with purely imaginary eigenvalues summing to zero, $\mathrm{rank}\,H\ge2$, and the rank-2 choice above realises equality with $\det U=1$. So $-1/N$ is the exact minimum. (Random search over $2\times10^5$ pairs $(U,X)$ never beats it: best found $-0.4998$ for $N=2$ vs $-0.5$; $-0.3262$ for $N=3$ vs $-0.3333$.)

**(b) From one plaquette to the lattice.** Vary only the link $b_0$. For a plaquette $p\ni b_0$, cyclicity of the trace lets us write the holonomy with $U_{b_0}$ first, $U_p\sim U_{b_0}S_p$ where $S_p$ is the product of the other three links (the 'staple'); if $b_0$ occurs with reversed orientation use $\mathrm{Re}\mathrm{Tr}(M)=\mathrm{Re}\mathrm{Tr}(M^\dagger)$ and $(e^{-tX})^\dagger=e^{tX}$ (X anti-Hermitian) to bring it to the same form. Hence for each $p\ni b_0$,
$$\frac{d^2}{dt^2}\Big|_0\Big(-\tfrac1N\mathrm{Re}\mathrm{Tr}\,U_p(t)\Big)=-\frac1N\mathrm{Re}\mathrm{Tr}\big(X^2 V_p\big),\qquad V_p:=\text{plaquette holonomy based just before }b_0 .$$
At $U^*$ every other link is $I$, so $V_p=U_{b_0}^{\pm1}=U_0$ (note $U_0^2=I$, so both orientations give $U_0$). Plaquettes not containing $b_0$ are unchanged by the variation and contribute $0$. In $d$ dimensions a link belongs to exactly $2(d-1)$ plaquettes (for each of the $d-1$ transverse directions $\nu$, the plaquettes $(x_0,\hat1\hat\nu)$ and $(x_0-\hat\nu,\hat1\hat\nu)$). Therefore
$$\nabla^2S_W(U^*)(\mathbf X,\mathbf X)=2(d-1)\cdot\Big(-\frac1N\mathrm{Re}\mathrm{Tr}(X^2U_0)\Big)=-\frac{2(d-1)}{N}.$$

**Numerical confirmation on a real lattice.** Central finite differences of $S_W$ along $t\mapsto e^{tX}U_{b_0}$ on a periodic $4^4$ lattice in $d=4$ give
$$SU(2): -2.99999989\ (\text{vs }-3),\quad SU(3): -1.99999963\ (\text{vs }-2),\quad SU(4): -1.49999995\ (\text{vs }-1.5).$$

**Sanity check at the vacuum.** At $U\equiv I$ every $V_p=I$, so the same formula with the full multi-link variation gives $\frac{d^2}{dt^2}(-\tfrac1N\mathrm{Re}\mathrm{Tr}U_p)=\tfrac1N\|(d z)_p\|^2\ge0$: the Wilson Hessian is PSD at its global minimum, as it must be.

### Constants and numbers

Single plaquette: exact minimum $-1/N$ ($-0.5$ for SU(2), $-1/3$ for SU(3), $-0.25$ for SU(4), $-1/6$ for SU(6)).
Lattice, single-link direction: $-2(d-1)/N$. In $d=4$: $-6/N$, i.e. $-3$ (SU(2)), $-2$ (SU(3)), $-1.5$ (SU(4)), $-1.2$ (SU(5)). In $d=3$: $-4/N$; in $d=2$: $-2/N$.
Metric: $\langle X,Y\rangle=-\mathrm{Tr}(XY)$. Configuration: $U_0=\mathrm{diag}(-1,-1,1,\dots,1)$, $X=\tfrac{i}{\sqrt2}\mathrm{diag}(1,-1,0,\dots,0)$.
Verified by finite differences ($h=10^{-4}$) on a $4^4$ periodic lattice, $d=4$, to 7 significant figures.

### Code

import numpy as np, math, itertools
from scipy.linalg import expm

L, d = 4, 4
idx = lambda x: tuple(np.mod(x, L))

def SW(U, N):
    tot = 0.0
    for x in itertools.product(range(L), repeat=d):
        xa = np.array(x)
        for mu in range(d):
            for nu in range(mu+1, d):
                a = U[(idx(xa), mu)]
                b = U[(idx(xa+np.eye(d,dtype=int)[mu]), nu)]
                c = U[(idx(xa+np.eye(d,dtype=int)[nu]), mu)]
                e = U[(idx(xa), nu)]
                tot += 1 - np.trace(a@b@c.conj().T@e.conj().T).real/N
    return tot

for N in (2,3,4):
    U0 = np.diag([-1.0]*2 + [1.0]*(N-2)).astype(complex)
    X  = np.zeros((N,N), complex); X[0,0]=1j/math.sqrt(2); X[1,1]=-1j/math.sqrt(2)
    U  = {(x,mu): np.eye(N,dtype=complex)
          for x in itertools.product(range(L),repeat=d) for mu in range(d)}
    b  = ((0,0,0,0), 0); U[b] = U0.copy(); h = 1e-4
    def f(t):
        U[b] = expm(t*X) @ U0
        return SW(U, N)
    print(N, (f(h)-2*f(0)+f(-h))/h**2, -2*(d-1)/N)
    # SU(2) -2.99999989 vs -3 ; SU(3) -1.99999963 vs -2 ; SU(4) -1.49999995 vs -1.5

**Caveat.** This gives a *lower bound on the magnitude* of the negativity (an upper bound on $\lambda_{\min}$); the true infimum of $\lambda_{\min}(\nabla^2 S_W)$ over $\mathcal C_\Lambda$ is more negative still (see Items E and H).

**Why it matters.** It converts the abstract $\lambda_f>0$ of Lemma A into an explicit, checkable, volume-uniform number for the actual Wilson action, and — because the single-plaquette bound is *sharp* by von Neumann — it pins the per-plaquette constant exactly at $1/N$ rather than leaving it as an unspecified 'operator-norm constant'.

---

## 5. Theorem E: the obstruction survives restriction to the gauge-invariant (horizontal) sector, with an exact closed form

`status: solid` · `kind: theorem`

### Statement

Setting as in Theorem D: $\Lambda=(\mathbb Z/L)^d$, $\mathcal C_\Lambda=SU(N)^{|B|}$, metric $\langle X,Y\rangle=-\mathrm{Tr}(XY)$. Let the lattice gauge group $\mathcal G=SU(N)^{V(\Lambda)}$ act isometrically by $(h\cdot U)_{x\mu}=h_xU_{x\mu}h_{x+\hat\mu}^{-1}$, with infinitesimal action $D_U:\bigoplus_x\mathfrak{su}(N)\to\bigoplus_b\mathfrak{su}(N)$,
$$(D_U\xi)_{x\mu}=\xi_x-\mathrm{Ad}_{U_{x\mu}}\xi_{x+\hat\mu},$$
vertical space $V_U=\mathrm{im}\,D_U$ and horizontal space $H_U=V_U^{\perp}=\ker D_U^{*}$. (For gauge-invariant $f$, $\nabla f\in H_U$, so $H_U$ is exactly the sector the Bakry-Émery bound must control.)

Let $U^*$ and $X$ be as in Theorem D. Then there is an **explicit horizontal** vector $\mathbf H\in H_{U^*}$ with
$$\boxed{\;\frac{\nabla^2S_W(U^*)(\mathbf H,\mathbf H)}{\|\mathbf H\|^2}\;=\;-\,\frac{2d(d-1)}{N\big(d-1+L^{-d}\big)}\;}$$
for every $N\ge2$, $d\ge2$, $L\ge2$. In particular
$$\lambda_{\min}\Big(P_{H_{U^*}}\nabla^2S_W(U^*)P_{H_{U^*}}\Big)\;\le\;-\frac{2d(d-1)}{N(d-1+L^{-d})}\;\xrightarrow[L\to\infty]{}\;-\frac{2d}{N}\;\;\Big(=-\frac8N\ \text{in }d=4\Big),$$
and for all $L\ge2$ it is $\le -2(d-1)/N$. Consequently the **horizontal** (gauge-invariant-sector) Bakry-Émery constant obeys
$$\rho^{\mathrm{hor}}_{\mathrm{glob}}(\beta):=\inf_{U}\inf_{\substack{Y\in H_U\\ \|Y\|=1}}\big[\mathrm{Ric}(Y,Y)+\beta\nabla^2S_W(Y,Y)\big]\;\le\;\frac N2-\beta\,\frac{2d(d-1)}{N(d-1+L^{-d})}\;\xrightarrow[\beta\to\infty]{}\;-\infty .$$

### Derivation

This closes the one loophole the corpus's obstruction leaves open. Every corpus statement of the mechanism ( `referee_local_horizontal_convexity_BE_gap_and_RG.md`, `lemma_unity_stitched_curvature_rg.md` §5-6, `02_bakry_emery_to_spectral_gap.md` §4) is careful to restrict the convexity claim to horizontal directions, since gauge directions are 'redundancy'. The corpus's obstruction note, by contrast, exhibits only a *single-link* negative direction, which is manifestly **not** horizontal. So a reader could object: maybe the horizontal Hessian is fine. It is not — it is strictly worse. Here is the complete argument. [The whole of this item is my reconstruction; the corpus does not contain it.]

**Step 0 (why the single-link direction is not horizontal).** $\mathbf X$ supported on $b_0=(x_0,\hat1)$ satisfies $(D^*_{U^*}\mathbf X)_{x_0}=X\ne0$, so $\mathbf X\notin\ker D^*$.

**Step 1 (an abelian subspace where everything is computable).** The key structural fact is
$$[X,U_0]=0 \quad\text{and}\quad [X,I]=0,$$
since $X=\tfrac{i}{\sqrt2}\mathrm{diag}(1,-1,0,\dots,0)$ and $U_0=\mathrm{diag}(-1,-1,1,\dots,1)$ are both diagonal. So $X$ commutes with **every** link variable of $U^*$. For a real function $z:B\to\mathbb R$ define the tangent vector $\mathbf Z^{(z)}$ by $Z^{(z)}_b:=z_b\,X$. Introduce the abelian lattice differentials
$$(dz)_p:=\sum_{b\in\partial p}\epsilon_b z_b \ \ (\text{oriented sum around }p),\qquad (d^*z)_x:=\sum_{\mu}\big(z_{x\mu}-z_{x-\hat\mu,\mu}\big),$$
$$(dc)_{x\mu}:=c_x-c_{x+\hat\mu},\qquad d^*d=-\Delta \ \ (\text{lattice Laplacian}),\qquad d\circ d=0 .$$

**Step 2 (horizontality reduces to $d^*z=0$).** Because $\mathrm{Ad}_{U_b}X=X$ for every $b$,
$$(D^*_{U^*}\mathbf Z^{(z)})_x=\sum_\mu Z_{x\mu}-\sum_\mu\mathrm{Ad}^{-1}_{U_{x-\hat\mu,\mu}}Z_{x-\hat\mu,\mu}=\Big(\sum_\mu(z_{x\mu}-z_{x-\hat\mu,\mu})\Big)X=(d^*z)_x\,X .$$
Hence $\mathbf Z^{(z)}\in H_{U^*}\iff d^*z=0$.

**Step 3 (the second variation reduces to an abelian quadratic form).** Along the geodesic $U_b(t)=e^{tz_bX}U^*_b$, since $e^{tz_bX}$ commutes with every $U^*_{b'}$, all the exponentials can be pulled out of the ordered plaquette product:
$$U_p(t)=e^{\,t\,(dz)_p X}\,U_p^* .$$
Therefore
$$\nabla^2S_W(U^*)(\mathbf Z^{(z)},\mathbf Z^{(z)})=\frac{d^2}{dt^2}\Big|_0\sum_p\Big(1-\tfrac1N\mathrm{Re}\mathrm{Tr}\big(e^{t(dz)_pX}U^*_p\big)\Big)=-\frac1N\sum_p (dz)_p^2\,\mathrm{Re}\mathrm{Tr}\big(X^2U^*_p\big).$$
With $X^2=-\tfrac12P$, $P=\mathrm{diag}(1,1,0,\dots,0)$:
$$\mathrm{Tr}(X^2U_p^*)=\begin{cases}\mathrm{Tr}(X^2)=-1, & U_p^*=I \quad(p\not\ni b_0),\\[2pt] -\tfrac12\mathrm{Tr}(PU_0)=-\tfrac12(-2)=+1, & U^*_p=U_0\quad(p\ni b_0).\end{cases}$$
Hence the **exact abelian formula**
$$\boxed{\ \nabla^2S_W(U^*)(\mathbf Z^{(z)},\mathbf Z^{(z)})=\frac1N\Big[\ \|dz\|^2-2\!\!\sum_{p\ni b_0}\!\!(dz)_p^2\ \Big]\ },\qquad \|\mathbf Z^{(z)}\|^2=\|z\|^2_{\ell^2(B)} .$$
(Check with $z=\delta_{b_0}$: $(dz)_p=\pm1$ on the $2(d-1)$ plaquettes through $b_0$ and $0$ elsewhere, giving $\tfrac1N[2(d-1)-4(d-1)]=-2(d-1)/N$, exactly Theorem D.)

**Step 4 (project onto the horizontal sector — for free, because $d\circ d=0$).** Let $c:V(\Lambda)\to\mathbb R$ solve the lattice Poisson equation
$$-\Delta c \;=\; d^*\delta_{b_0}\;=\;\delta_{x_0}-\delta_{x_1},\qquad x_1:=x_0+\hat1 .$$
This is solvable on the torus because the source is orthogonal to the constants (the kernel of $\Delta$). Put
$$z^{\mathrm{hor}}:=\delta_{b_0}-dc,\qquad \mathbf H:=\mathbf Z^{(z^{\mathrm{hor}})}.$$
Then:
  * $d^*z^{\mathrm{hor}}=d^*\delta_{b_0}-d^*dc=(\delta_{x_0}-\delta_{x_1})-(-\Delta c)=0$, so $\mathbf H\in H_{U^*}$ — **it is exactly horizontal**;
  * $dz^{\mathrm{hor}}=d\delta_{b_0}-d(dc)=d\delta_{b_0}$, since $d\circ d=0$. **The curl is unchanged.**
Therefore, by the boxed formula of Step 3, the numerator is *identical* to the single-link one:
$$\nabla^2 S_W(U^*)(\mathbf H,\mathbf H)\;=\;\nabla^2S_W(U^*)(\mathbf X,\mathbf X)\;=\;-\frac{2(d-1)}{N}.$$
Only the norm shrinks. This is the mechanism: the vertical projection is a pure gradient, which is invisible to the plaquette curl.

**Step 5 (the norm, in closed form via the lattice Green function).** By orthogonality ($dc$ is the vertical part),
$$\|z^{\mathrm{hor}}\|^2=\|\delta_{b_0}\|^2-\|dc\|^2=1-\langle c,-\Delta c\rangle=1-(c_{x_0}-c_{x_1}).$$
Let $G$ be the torus Green function, $-\Delta G=\delta_0-L^{-d}$. Then $c=G(\cdot-x_0)-G(\cdot-x_1)$ and $c_{x_0}-c_{x_1}=2\big(G(0)-G(e_1)\big)$. Evaluating $-\Delta G$ at the origin and using hypercubic symmetry ($G(\pm e_\mu)$ all equal),
$$2d\,G(0)-\sum_{\mu}\big(G(e_\mu)+G(-e_\mu)\big)=2d\big(G(0)-G(e_1)\big)=1-L^{-d}\quad\Longrightarrow\quad G(0)-G(e_1)=\frac{1-L^{-d}}{2d}.$$
Hence
$$\|dc\|^2=\frac{1-L^{-d}}{d},\qquad \|\mathbf H\|^2=\|z^{\mathrm{hor}}\|^2=1-\frac{1-L^{-d}}{d}=\frac{d-1+L^{-d}}{d}.$$

**Step 6 (assemble).**
$$\frac{\nabla^2S_W(U^*)(\mathbf H,\mathbf H)}{\|\mathbf H\|^2}=\frac{-2(d-1)/N}{(d-1+L^{-d})/d}=-\frac{2d(d-1)}{N(d-1+L^{-d})}.$$
Since $\|\mathbf H\|\le\|\mathbf X\|=1$, this is $\le-2(d-1)/N$ for every $L$; and $L\to\infty$ gives $-2d/N$. $\;\blacksquare$

**Step 7 (why this suffices for the BE conclusion on gauge-invariant functions).** For gauge-invariant $u$, $\nabla u$ is horizontal, and Bochner gives $\Gamma_2(u)=\|\nabla^2u\|^2_{\mathrm{HS}}+(\mathrm{Ric}+\beta\nabla^2S_W)(\nabla u,\nabla u)$. So the sharp CD constant on the gauge-invariant sector is exactly $\rho^{\mathrm{hor}}_{\mathrm{glob}}(\beta)$, and it is bounded above by $\tfrac N2-\beta\cdot\tfrac{2d(d-1)}{N(d-1+L^{-d})}$ by evaluating at $(U^*,\mathbf H/\|\mathbf H\|)$ and using $\mathrm{Ric}=\tfrac N2\mathrm{Id}$ (Item C).

**Independent numerical verification.** Building $D_{U^*}$ explicitly, projecting with $P_V=D\,D^{+}$, and evaluating the second derivative of $S_W$ by finite differences along the geodesic in direction $\mathbf H$ reproduces the closed form to 6-7 digits:

| $N$ | $d$ | $L$ | $\|\mathbf H\|^2$ numeric | $\|\mathbf H\|^2$ closed form | Rayleigh numeric | Rayleigh closed form |
|---|---|---|---|---|---|---|
| 2 | 4 | 2 | 0.765625 | 0.765625 | $-3.918368$ | $-3.918367$ |
| 3 | 4 | 2 | 0.765625 | 0.765625 | $-2.612244$ | $-2.612245$ |
| 2 | 3 | 3 | 0.679012 | 0.679012 | $-2.945455$ | $-2.945455$ |
| 2 | 2 | 4 | 0.531250 | 0.531250 | $-1.882353$ | $-1.882353$ |

### Constants and numbers

Exact closed form: $\ \mathcal R(N,d,L)=-\dfrac{2d(d-1)}{N(d-1+L^{-d})}$, with $\|\mathbf H\|^2=\dfrac{d-1+L^{-d}}{d}$ and $\|\text{vertical part}\|^2=\dfrac{1-L^{-d}}{d}$.

$L\to\infty$ limit: $-2d/N$. In $d=4$: $-8/N$, i.e. $-4$ (SU(2)), $-8/3\approx-2.6667$ (SU(3)), $-2$ (SU(4)), $-1.6$ (SU(5)).

Finite-$L$ values verified numerically (agreement to all printed digits):
  $(N,d,L)=(2,4,2)$: $-3.918368$; $(3,4,2)$: $-2.612244$; $(2,3,3)$: $-2.945455$; $(2,2,4)$: $-1.882353$.

Resulting sign-change threshold for $\rho^{\mathrm{hor}}_{\mathrm{glob}}$, using $k_{\max}=N/2$:
$\beta_*=\dfrac{N^2}{4d}$ as $L\to\infty$: $\ 0.2500$ (SU(2), $d=4$), $0.5625$ (SU(3), $d=4$), $1.0000$ (SU(4), $d=4$); $0.3333$/$0.7500$ for $d=3$; $0.5000$/$1.1250$ for $d=2$.

Corollary: the corpus's uniform bound $C_V(N)=6/N$ on $|\langle A,\mathrm{Hess}\,S_W A\rangle|/\|A\|^2$ is violated by $\mathbf H$ already at $L=2$, $d=4$: $3.918>3$ for SU(2), $2.612>2$ for SU(3).

### Code

import numpy as np, math, itertools
from scipy.linalg import expm
# needs su_basis() from Item C

def horizontal_test(N, L, d):
    T = su_basis(N); m = len(T)
    sites = list(itertools.product(range(L), repeat=d)); sidx = {s:i for i,s in enumerate(sites)}
    links = [(s,mu) for s in sites for mu in range(d)]; lidx = {b:i for i,b in enumerate(links)}
    nl = len(links)
    sh = lambda x,mu: tuple((np.array(x)+np.eye(d,dtype=int)[mu]) % L)
    U  = [np.eye(N,dtype=complex) for _ in links]
    U0 = np.diag([-1.0]*2+[1.0]*(N-2)).astype(complex)
    b0 = lidx[(sites[0],0)]; U[b0] = U0.copy()
    plaq = [(lidx[(x,mu)], lidx[(sh(x,mu),nu)], lidx[(sh(x,nu),mu)], lidx[(x,nu)])
            for x in sites for mu in range(d) for nu in range(mu+1,d)]
    def SW(Ul):
        return sum(1 - np.trace(Ul[a]@Ul[b]@Ul[c].conj().T@Ul[e].conj().T).real/N
                   for (a,b,c,e) in plaq)
    # D : site field -> link field,  (D xi)_{x,mu} = xi_x - Ad_U xi_{x+mu}
    D = np.zeros((nl*m, len(sites)*m))
    for (x,mu) in links:
        bi = lidx[(x,mu)]; y = sh(x,mu)
        for a in range(m):
            Ad = U[bi] @ T[a] @ U[bi].conj().T
            for c in range(m):
                D[bi*m+c, sidx[x]*m+a] += -np.trace(T[a]@T[c]).real
                D[bi*m+c, sidx[y]*m+a] -= -np.trace(Ad   @T[c]).real
    X = np.zeros((N,N),complex); X[0,0]=1j/math.sqrt(2); X[1,1]=-1j/math.sqrt(2)
    xv = np.zeros(nl*m)
    for c in range(m): xv[b0*m+c] = -np.trace(X@T[c]).real
    h = xv - (D @ np.linalg.pinv(D)) @ xv          # horizontal projection
    fld = lambda v: [sum(v[i*m+c]*T[c] for c in range(m)) for i in range(nl)]
    def d2(dirs, s=1e-4):
        f = lambda t: SW([expm(t*dirs[i]) @ U[i] for i in range(nl)])
        return (f(s) - 2*f(0) + f(-s)) / s**2
    R_num = d2(fld(h)) / (h@h)
    R_cf  = -2*d*(d-1) / (N*(d-1 + L**(-d)))
    return (h@h, (d-1+L**(-d))/d, R_num, R_cf)

for (N,L,dd) in [(2,2,4),(3,2,4),(2,3,3),(2,4,2)]:
    print(N, dd, L, horizontal_test(N,L,dd))
# (2,4,2): (0.765625, 0.765625, -3.918368, -3.918367)
# (3,4,2): (0.765625, 0.765625, -2.612244, -2.612245)
# (2,3,3): (0.679012, 0.679012, -2.945455, -2.945455)
# (2,2,4): (0.531250, 0.531250, -1.882353, -1.882353)

**Caveat.** This bounds $\lambda_{\min}$ of the horizontal Hessian from above at one configuration; the true infimum over $\mathcal C_\Lambda$ is more negative still. Also, $U^*$ is a smooth interior configuration, not a Gribov-horizon or reducible point, so it cannot be excised by the corpus's polarity/capacity arguments.

**Why it matters.** It removes the last escape hatch. Every constructive part of the corpus is phrased on horizontal directions precisely to dodge gauge redundancy; this theorem shows the horizontal restriction makes the obstruction *worse* by the factor $d/(d-1)$ (33% worse in $d=4$), and gives an exact finite-$L$ formula that can be checked against any implementation. It also independently falsifies the corpus's central Wilson-Hessian constant $C_V(N)=6/N$.

---

## 6. Corollary F: divergence rate of rho_glob along the asymptotically free trajectory (explicit logarithm in 1/a)

`status: conditional` · `kind: numerical_result`

### Statement

Assume the one-loop asymptotically free running of the bare lattice coupling in $d=4$ pure $SU(N)$ Yang-Mills,
$$\mu\frac{dg}{d\mu}=-\frac{11N}{3}\frac{g^3}{16\pi^2}\quad\Longrightarrow\quad \frac{1}{g^2(a)}=\frac{11N}{24\pi^2}\,\ln\frac{1}{a\Lambda},\qquad \beta(a)=\frac{2N}{g^2(a)}=\frac{11N^2}{12\pi^2}\ln\frac{1}{a\Lambda}.$$
Then the horizontal global Bakry-Émery constant of the lattice Wilson-Langevin diffusion, in the infinite-volume limit, obeys
$$\boxed{\;\rho^{\mathrm{hor}}_{\mathrm{glob}}(a)\;\le\;\frac N2\;-\;\frac{22N}{3\pi^2}\,\ln\frac{1}{a\Lambda}\;}$$
i.e. it diverges to $-\infty$ **logarithmically in the inverse lattice spacing**, with slope $\frac{22N}{3\pi^2}\approx0.74296\,N$ per $e$-fold. It first becomes negative at
$$a\Lambda \;=\; \exp\!\Big(-\frac{3\pi^2}{44}\Big)\;=\;0.5102\qquad\text{(independent of }N\text{)}.$$

### Derivation

**Step 1.** Theorem E ($L\to\infty$, $d=4$) plus Proposition C give, for any $\beta$,
$$\rho^{\mathrm{hor}}_{\mathrm{glob}}(\beta)\;\le\;\frac N2-\frac{2d}{N}\beta\;=\;\frac N2-\frac{8\beta}{N}.$$

**Step 2.** One-loop running. From $\mu\,dg/d\mu=-b_0g^3/(16\pi^2)$ with $b_0=11N/3$,
$$\frac{d}{d\ln\mu}\,g^{-2}=-2g^{-3}\frac{dg}{d\ln\mu}=\frac{2b_0}{16\pi^2}=\frac{11N}{24\pi^2},$$
so $g^{-2}(\mu)=\frac{11N}{24\pi^2}\ln(\mu/\Lambda)$. Identify the cutoff $\mu=1/a$ and use the lattice convention $\beta=2N/g^2$:
$$\beta(a)=\frac{2N\cdot 11N}{24\pi^2}\ln\frac{1}{a\Lambda}=\frac{11N^2}{12\pi^2}\,\ln\frac{1}{a\Lambda}.$$

**Step 3.** Substitute:
$$\frac{8}{N}\beta(a)=\frac{8}{N}\cdot\frac{11N^2}{12\pi^2}\ln\frac1{a\Lambda}=\frac{88N}{12\pi^2}\ln\frac1{a\Lambda}=\frac{22N}{3\pi^2}\ln\frac1{a\Lambda},$$
which is the boxed statement. Numerically $\frac{22}{3\pi^2}=0.742963$.

**Step 4 (zero crossing).** $\tfrac N2=\tfrac{22N}{3\pi^2}L_a$ gives $L_a=\ln\frac{1}{a\Lambda}=\frac{3\pi^2}{44}=0.67288$, i.e. $a\Lambda=e^{-0.67288}=0.5102$. The factor $N$ cancels: the crossing point is universal in $N$.

**Step 5 (interpretation).** For $SU(3)$: $\rho^{\mathrm{hor}}_{\mathrm{glob}}(a)\le 1.5-2.2291\ln\frac1{a\Lambda}$. At a typical modern lattice spacing $a\approx0.1\,\mathrm{fm}$ with $\Lambda\approx0.2\,\mathrm{GeV}$ ($\Lambda^{-1}\approx1\,\mathrm{fm}$), $\ln(1/a\Lambda)\approx2.3$, giving $\rho\lesssim-3.6$; using the *measured* $\beta=6.0$ instead of one-loop running gives directly $\rho\le 1.5-\tfrac83\cdot6.0=-14.5$.

**Contrast with the finite-cutoff 'convexity window'.** The corpus's window is $\rho_*(a,g)=c_0a^2g^2-\beta C_V(N)$, positive only for $g^4>12/(c_0a^2)$ (and $g^4>24/(c_0a^2)$ for one-step RG stability). Since $g(a)\to0$ while $a\to0$, the window closes; the corpus states this correctly. What the present corollary adds is the *rate*: the failure is not a delicate near-miss but a logarithmic divergence with an $O(N)$ coefficient, and it has already occurred at $a\Lambda\approx0.5$ — i.e. at every lattice spacing anyone has ever simulated.

### Constants and numbers

One-loop coefficient: $b_0=11N/3$; $\,g^{-2}(a)=\frac{11N}{24\pi^2}\ln\frac{1}{a\Lambda}$; $\beta(a)=\frac{11N^2}{12\pi^2}\ln\frac{1}{a\Lambda}$.
Divergence slope: $\frac{22N}{3\pi^2}=0.742963\,N$ per $e$-fold of $1/a$.
  SU(2): $\rho\le 1.0-1.48593\,\ln(1/a\Lambda)$.
  SU(3): $\rho\le 1.5-2.22889\,\ln(1/a\Lambda)$.
  SU(4): $\rho\le 2.0-2.97185\,\ln(1/a\Lambda)$.
Universal zero crossing: $a\Lambda=e^{-3\pi^2/44}=0.5102$, i.e. $\ln(1/a\Lambda)=0.67288$.
At $SU(3)$, $\beta=6.0$: $\rho^{\mathrm{hor}}_{\mathrm{glob}}\le-14.5$.
Using the weaker all-directions constant $6/N$ instead of $8/N$: slope $\frac{11N}{2\pi^2}=0.55722\,N$, crossing at $\ln(1/a\Lambda)=\pi^2/11=0.89720$, $a\Lambda=0.4077$.

### Code

import math
for N in (2,3,4):
    slope = 22*N/(3*math.pi**2)          # d=4, horizontal constant 2d/N = 8/N
    print(N, N/2, slope, math.exp(-(N/2)/slope))
# 2 1.0 1.48593 0.5102
# 3 1.5 2.22889 0.5102
# 4 2.0 2.97185 0.5102

**Caveat.** Conditional on the one-loop bare-coupling running being the correct asymptotic trajectory (standard, but it is an input, not a theorem proved here); the $\Lambda$ normalisation is scheme-dependent so $a\Lambda=0.51$ carries scheme ambiguity. The inequality itself (Step 1) is unconditional.

**Why it matters.** It turns 'the global BE constant goes to $-\infty$' into a rate and a scale, and shows the crossing already happened at $a\Lambda\approx0.5$: the global BE route is not 'good until the continuum then fails', it is unusable at every physically interesting coupling. This is the sharpest quantitative form of the corpus's own conclusion.

---

## 7. Proposition G: the exact global BE constant of the one-link SU(N) model, and the exponentially small measure of the bad set

`status: solid` · `kind: numerical_result`

### Statement

**(a) Exact one-link BE constant.** Let $G=SU(N)$ with $\langle X,Y\rangle=-\mathrm{Tr}(XY)$, $S_p(U)=1-\tfrac1N\mathrm{Re}\mathrm{Tr}\,U$, $d\mu_\beta\propto e^{-\beta S_p}d\mathrm{Haar}$. Then the optimal curvature-dimension constant is **exactly**
$$\rho^{\mathrm{1link}}_{\mathrm{glob}}(\beta)\;=\;\frac N2-\frac{\beta}{N},$$
negative precisely for $\beta>N^2/2$. For $N=2$ ($SU(2)$ = round $S^3$ of radius $\sqrt2$) the Bakry-Émery tensor is pointwise isotropic and known in closed form:
$$\mathrm{Ric}+\nabla^2(\beta S_p)\;=\;\Big(1+\frac\beta2\cos\theta\Big)\,g,\qquad \tfrac12\mathrm{Tr}\,U=\cos\theta,\ \theta\in[0,\pi],$$
so $\rho^{\mathrm{1link}}_{\mathrm{glob}}(\beta)=1-\beta/2$, attained at $U=-I$.

**(b) The bad set is exponentially light.** For $SU(2)$ and $\beta>2$ the set where the BE tensor is negative is exactly $\{\theta>\theta_c(\beta)\}$, $\theta_c(\beta)=\arccos(-2/\beta)$, and its Gibbs mass under $d\mu_\beta\propto\sin^2\theta\,e^{\beta\cos\theta}\,d\theta$ decays like $e^{-\beta}$ up to algebraic factors; the normalisation is exactly $\int_0^\pi\sin^2\theta\,e^{\beta\cos\theta}d\theta=\pi I_1(\beta)/\beta$ ($I_1$ = modified Bessel).

### Derivation

**(a) General $N$.** $\mathrm{Re}\mathrm{Tr}$ is the restriction to $SU(N)\subset\mathbb C^{N\times N}$ of a *linear* functional, and (Theorem D(a)) $\nabla^2S_p(U)(X,X)=-\tfrac1N\mathrm{Re}\mathrm{Tr}(X^2U)$. By the von Neumann argument of Theorem D(a), $\inf_{U,\|X\|=1}\nabla^2S_p(U)(X,X)=-1/N$, attained. Adding $\mathrm{Ric}=\tfrac N2\mathrm{Id}$ (Proposition C) gives $\rho^{\mathrm{1link}}_{\mathrm{glob}}(\beta)=\tfrac N2-\tfrac\beta N$ exactly (both bounds attained at the same $(U_0,X)$). Sign change at $\beta=N^2/2$: $\beta=2$ for $SU(2)$, $4.5$ for $SU(3)$, $8$ for $SU(4)$.

**(a) $N=2$, closed form.** $SU(2)$ with $\langle X,Y\rangle=-\mathrm{Tr}(XY)$ is the round $S^3$ of radius $r=\sqrt2$ (Prop. C, Step 5). Write $U=\exp(i\theta\,\hat n\cdot\vec\sigma)$, so $\tfrac12\mathrm{Tr}U=\cos\theta$ and the geodesic distance from $I$ is $\varrho=\sqrt2\,\theta$. Now $\cos\theta$ is the restriction to $S^3\subset\mathbb R^4$ of a linear coordinate; a linear function $\ell$ on $\mathbb R^{n+1}$ restricted to the sphere of radius $r$ obeys $\nabla^2\ell=-r^{-2}\ell\,g$. Hence
$$\nabla^2\big(\beta(1-\cos\theta)\big)=\frac{\beta\cos\theta}{r^2}\,g=\frac{\beta\cos\theta}{2}\,g .$$
(Direct check via the radial formula: for $\phi(\varrho)=\beta(1-\cos(\varrho/\sqrt2))$ the radial eigenvalue is $\phi''=\tfrac\beta2\cos\theta$ and the two tangential eigenvalues are $\tfrac{\phi'}{r}\cot(\varrho/r)=\tfrac1{\sqrt2}\cdot\tfrac\beta{\sqrt2}\sin\theta\cdot\cot\theta=\tfrac\beta2\cos\theta$ — all three equal, hence isotropic.) Adding $\mathrm{Ric}=1\cdot g$ gives the boxed tensor; its infimum over $\theta\in[0,\pi]$ is at $\theta=\pi$, value $1-\beta/2$, consistent with $\tfrac N2-\tfrac\beta N$ at $N=2$.

**(b) The bad-set computation.** Under $d\mu_\beta\propto\sin^2\theta\,e^{\beta\cos\theta}d\theta$ (Haar $\times$ Wilson weight, after integrating out $\hat n\in S^2$), the negative-BE set is $\cos\theta<-2/\beta$. Its mass, computed by quadrature against the exact normalisation $\pi I_1(\beta)/\beta$:

| $\beta$ | $\theta_c=\arccos(-2/\beta)$ | $\rho^{\mathrm{1link}}_{\mathrm{glob}}=1-\beta/2$ | $\mu_\beta(\text{bad})$ | $e^{-\beta}$ |
|---|---|---|---|---|
| 2.5 | 2.498092 | $-0.25$ | $2.883\times10^{-3}$ | $8.21\times10^{-2}$ |
| 3 | 2.300524 | $-0.50$ | $3.874\times10^{-3}$ | $4.98\times10^{-2}$ |
| 4 | 2.094395 | $-1.00$ | $2.716\times10^{-3}$ | $1.83\times10^{-2}$ |
| 5 | 1.982313 | $-1.50$ | $1.343\times10^{-3}$ | $6.74\times10^{-3}$ |
| 6 | 1.910633 | $-2.00$ | $5.890\times10^{-4}$ | $2.48\times10^{-3}$ |
| 8 | 1.823477 | $-3.00$ | $9.856\times10^{-5}$ | $3.36\times10^{-4}$ |
| 10 | 1.772154 | $-4.00$ | $1.528\times10^{-5}$ | $4.54\times10^{-5}$ |
| 20 | 1.670964 | $-9.00$ | $1.002\times10^{-9}$ | $2.06\times10^{-9}$ |
| 50 | 1.610807 | $-24.00$ | $1.481\times10^{-22}$ | $1.93\times10^{-22}$ |

Asymptotics: the Gibbs weight peaks at $\theta=0$ with $e^{\beta}$; on the bad set $\cos\theta\le-2/\beta$ so the weight is $\le e^{-2}$; hence the ratio is $\asymp e^{-\beta}$ up to $\beta^{3/2}$ factors — visible in the table (at $\beta=20$, $1.00\times10^{-9}$ vs $e^{-20}=2.06\times10^{-9}$).

**(b') Reproduction of the corpus's own table.** `03_SU2_Concentration_BadMass.md` reports a *coordinate* (flat-chart, Jacobian-included) radial eigenvalue $\lambda_{\mathrm{rad}}(\theta,\beta)=\tfrac12(\csc^2\theta-\theta^{-2})+\tfrac\beta4\cos\theta$, first negative at $\beta_c$. I recomputed independently and reproduce every digit of the corpus's table:
$\beta_c=4.413915$; and

| $\beta$ | $r_{\text{start}}$ | $r_{\text{end}}$ | nonconvex mass | bad mass |
|---|---|---|---|---|
| 4.5 | 2.038649 | 2.201505 | $1.081864\times10^{-3}$ | $1.880604\times10^{-3}$ |
| 5 | 1.924823 | 2.332324 | $1.659518\times10^{-3}$ | $1.844956\times10^{-3}$ |
| 6 | 1.831386 | 2.454436 | $9.566965\times10^{-4}$ | $9.748608\times10^{-4}$ |
| 8 | 1.747900 | 2.581050 | $1.830831\times10^{-4}$ | $1.833402\times10^{-4}$ |
| 10 | 1.706223 | 2.654222 | $2.983515\times10^{-5}$ | $2.983933\times10^{-5}$ |
| 20 | 1.633771 | 2.812795 | $2.113171\times10^{-9}$ | $2.113171\times10^{-9}$ |
| 50 | 1.595101 | 2.938592 | $3.249038\times10^{-22}$ | $3.249038\times10^{-22}$ |

The two versions differ only by the chart/normalisation ($\beta_c=4.4139$ in the corpus chart, $\beta_c=2$ in the intrinsic one); the *structure* — a $\theta$-interval of negative curvature opening at a finite $\beta_c$, whose Gibbs mass then decays like $e^{-\beta}$ — is chart-independent.

**The moral, stated precisely.** The bad set is never empty (Lemma A) but is exponentially light. That is exactly the configuration in which the *classical* perturbation tools fail: Holley-Stroock requires $\sup|\delta S|$, not $\mu(\text{bad})$, and $\sup|\delta S|$ here grows like $\beta$ *and* like the volume (the bad set is a union over links). This is the precise reason the corpus needed, and did not obtain, a localisation theorem rather than a perturbation argument.

### Constants and numbers

Exact: $\rho^{\mathrm{1link}}_{\mathrm{glob}}(\beta)=N/2-\beta/N$; zero at $\beta=N^2/2$ ($2$ for SU(2), $4.5$ for SU(3), $8$ for SU(4), $12.5$ for SU(5)).
SU(2) BE tensor: $(1+\tfrac\beta2\cos\theta)g$; bad set $\theta>\arccos(-2/\beta)$; normalisation $\int_0^\pi\sin^2\theta e^{\beta\cos\theta}d\theta=\pi I_1(\beta)/\beta$.
Bad-set masses (intrinsic): $2.883\times10^{-3}$ ($\beta{=}2.5$), $1.343\times10^{-3}$ ($\beta{=}5$), $1.528\times10^{-5}$ ($\beta{=}10$), $1.002\times10^{-9}$ ($\beta{=}20$), $1.481\times10^{-22}$ ($\beta{=}50$).
Corpus chart: $\beta_c=4.413915$; masses as tabulated above, reproduced exactly.

### Code

import math
import numpy as np
from scipy.integrate import quad
from scipy.special import iv
from scipy.optimize import brentq

# (a)+(b) intrinsic SU(2): Ric + Hess(beta S_p) = (1 + (beta/2) cos theta) g
for beta in (2.5,3,4,5,6,8,10,20,50):
    tc = math.acos(-2/beta)
    num,_ = quad(lambda t:(math.sin(t)**2)*math.exp(beta*(math.cos(t)-1)), tc, math.pi, limit=400)
    den   = math.pi*iv(1,beta)/beta*math.exp(-beta)          # exact normalisation
    print(beta, tc, 1-beta/2, num/den, math.exp(-beta))

# (b') corpus-chart radial eigenvalue and its bad-mass table
lam = lambda t,b: 0.5*(1/math.sin(t)**2 - 1/t**2) + (b/4)*math.cos(t)
def roots(b, n=400000):
    th = np.linspace(1e-6, math.pi-1e-6, n)
    v  = 0.5*(1/np.sin(th)**2 - 1/th**2) + (b/4)*np.cos(th)
    s  = np.sign(v); i = np.where(s[:-1]*s[1:] < 0)[0]
    return [brentq(lambda x: lam(x,b), th[j], th[j+1]) for j in i]
beta_c = brentq(lambda b: min(0.5*(1/np.sin(np.linspace(1e-6,math.pi-1e-6,400000))**2
                 - 1/np.linspace(1e-6,math.pi-1e-6,400000)**2)
                 + (b/4)*np.cos(np.linspace(1e-6,math.pi-1e-6,400000))), 3.0, 8.0, xtol=1e-12)
print('beta_c =', beta_c)     # 4.413915

**Caveat.** The corpus's $\beta_c=4.4139$ is a flat-chart (Jacobian-included) quantity, not the intrinsic BE constant; the intrinsic one changes sign at $\beta=2$. Both are correct in their own normalisation - do not mix them.

**Why it matters.** It supplies the one place in this whole circle of ideas where the global BE constant is known *exactly* in closed form, giving an independent, fully rigorous confirmation of Theorem B in the simplest nontrivial case, and it quantifies the trade-off ('the bad set is exponentially rare but never empty, and rarity is the wrong currency for Holley-Stroock') that motivated the corpus's entire localisation programme.

---

## 8. Refutation and repair of the corpus constant C_V(N) = 6/N (uniform Wilson Hessian bound)

`status: solid` · `kind: obstruction`

### Statement

The corpus asserts throughout (`referee_local_horizontal_convexity_BE_gap_and_RG.md` §2, `lemma_unity_stitched_curvature_rg.md` §4, and every downstream 'convexity window' formula $\rho_*=c_0a^2g^2-\beta C_V(N)$) that in $d=4$
$$\big|\langle A,\mathrm{Hess}\,S_W(U)A\rangle\big|\;\le\;C_V(N)\|A\|^2\quad\forall U,\forall A,\qquad C_V(N)=\frac6N .$$
**This is false.** The stated proof ('each plaquette contributes $\le1/N$ per link, each link is in 6 plaquettes') bounds only the *block-diagonal* (single-link) part of the Hessian and omits the mixed second derivatives between different links of the same plaquette. A correct crude replacement in $d$ dimensions is
$$\big|\langle A,\mathrm{Hess}\,S_W(U)A\rangle\big|\;\le\;\frac{14(d-1)}{N}\,\|A\|^2 \qquad\Big(=\frac{42}{N}\ \text{in } d=4\Big).$$

### Derivation

**Counterexample (analytic).** Theorem E exhibits, at $L=2$, $d=4$, an explicit direction $\mathbf H$ with $|\langle \mathbf H,\mathrm{Hess}S_W\mathbf H\rangle|/\|\mathbf H\|^2 = 2d(d-1)/(N(d-1+L^{-d}))=3.918>3=6/N$ for $SU(2)$ and $2.612>2$ for $SU(3)$. As $L\to\infty$ the value is $2d/N=8/N>6/N$. So $6/N$ fails already on horizontal directions.

**Counterexample (numerical, random configurations).** Full finite-difference Hessians at random $SU(2)$ configurations:

| $d$ | $L$ | seed | $\lambda_{\min}$ | $\lambda_{\max}$ | corpus bound $2(d-1)/N$ |
|---|---|---|---|---|---|
| 2 | 3 | 0 | $-1.9142$ | $2.4619$ | $1.0$ |
| 2 | 3 | 1 | $-1.6326$ | $2.8352$ | $1.0$ |
| 2 | 3 | 2 | $-2.3183$ | $1.9986$ | $1.0$ |
| 3 | 2 | 0 | $-2.9711$ | $3.4147$ | $2.0$ |
| 3 | 2 | 1 | $-3.2198$ | $3.2928$ | $2.0$ |
| 3 | 2 | 2 | $-2.8743$ | $3.4201$ | $2.0$ |

Violations by factors of $2$-$3$ at generic configurations.

**Repair (a correct bound).** Fix a plaquette $p$ with links $\ell_1,\dots,\ell_4$ in cyclic order and vary $U_{\ell_i}\to e^{tA_i}U_{\ell_i}$. Writing $P_i:=U_{\ell_1}\cdots U_{\ell_i}$ and $B_i:=P_{i-1}A_iP_{i-1}^{-1}$ (so $\|B_i\|=\|A_i\|$, conjugation being an isometry), one has the exact identity
$$e^{tA_1}U_{\ell_1}e^{tA_2}U_{\ell_2}\cdots=e^{tB_1}e^{tB_2}e^{tB_3}e^{tB_4}\,U_p .$$
Expanding the ordered product to second order, $\prod_ie^{tB_i}=1+t\sum_iB_i+\tfrac{t^2}{2}\big(\sum_iB_i^2+2\sum_{i<j}B_iB_j\big)$, and using $\sum_iB_i^2+2\sum_{i<j}B_iB_j=B^2+\sum_{i<j}[B_i,B_j]$ with $B:=\sum_iB_i$,
$$\frac{d^2}{dt^2}\Big|_0\Big(-\tfrac1N\mathrm{Re}\mathrm{Tr}\,U_p(t)\Big)=-\frac1N\mathrm{Re}\Big[\mathrm{Tr}(B^2U_p)+\sum_{i<j}\mathrm{Tr}\big([B_i,B_j]U_p\big)\Big].$$
Bound each piece:
  * $|\mathrm{Tr}(B^2U_p)|\le\|B\|^2$ by von Neumann ($-B^2\succeq0$, trace $=\|B\|^2$, $U_p$ unitary), and $\|B\|^2\le(\sum_i\|A_i\|)^2\le4\sum_i\|A_i\|^2$ (Cauchy-Schwarz);
  * $|\mathrm{Tr}([B_i,B_j]U_p)|\le\|[B_i,B_j]\|_1\le2\|B_i\|_2\|B_j\|_2=2\|A_i\|\|A_j\|$ (Hölder for Schatten norms, $\|XY\|_1\le\|X\|_2\|Y\|_2$), and $2\sum_{i<j}\|A_i\|\|A_j\|\le3\sum_i\|A_i\|^2$.
Hence per plaquette the second variation is bounded by $\tfrac7N\sum_{\ell\in p}\|A_\ell\|^2$. Summing over plaquettes and using that each link lies in $2(d-1)$ plaquettes gives the stated $14(d-1)/N$. Consistency with the numerics: for $d=2$, $N=2$ the bound is $7$ (observed max $2.84$); for $d=3$, $N=2$ it is $14$ (observed max $3.42$) — crude but valid.

**Effect on the corpus's downstream formulas.** Every occurrence of $C_V(N)=6/N$ should be read as $\ge 8/N$ (the horizontal lower bound of Theorem E) and $\le 42/N$ (the crude upper bound above). This *strengthens* the obstruction (larger $\lambda_f$, faster divergence) and *weakens* the corpus's convexity window: the window condition $c_0a^2g^4>2NC_V$ becomes at least $7\times$ harder ($g^4>84/(c_0a^2)$ instead of $12/(c_0a^2)$), and the mixed-block constant $M=\beta C_V$ in the block-Hessian RG inequality is at least $\tfrac{4}{3}\times$ and possibly $7\times$ larger than quoted.

### Constants and numbers

Corpus claim: $C_V(N)=2(d-1)/N=6/N$ in $d=4$. FALSE.
Lower bound (from Theorem E, exact): $C_V(N)\ge 2d(d-1)/(N(d-1+L^{-d}))\to 2d/N=8/N$ in $d=4$.
Upper bound (derived here): $C_V(N)\le 14(d-1)/N$, i.e. $42/N$ in $d=4$, $14/N$ in $d=2$, $28/N$ in $d=3$.
Measured $\lambda_{\min}$ at random SU(2) configurations: $-2.32$ ($d{=}2$, $L{=}3$), $-3.22$ ($d{=}3$, $L{=}2$), against corpus bounds $-1$ and $-2$.
Consequences: corpus convexity window $g^4>12/(c_0a^2)$ becomes $g^4>84/(c_0a^2)$; RG-stable subwindow $g^4>24/(c_0a^2)$ becomes $g^4>168/(c_0a^2)$; mixed-block norm $M=\beta C_V=12/g^2$ becomes $\le 84/g^2$.

### Code

# full finite-difference Wilson Hessian on a small periodic lattice; prints (lam_min, lam_max)
# (uses su_basis from Item C). Runtime ~25 s for the two cases below.
import numpy as np, math, itertools
from scipy.linalg import expm

def hess_spectrum(N, L, d, seed=0, h=2e-3):
    T = su_basis(N); m = len(T)
    sites = list(itertools.product(range(L), repeat=d))
    links = [(s,mu) for s in sites for mu in range(d)]; lidx={b:i for i,b in enumerate(links)}
    sh = lambda x,mu: tuple((np.array(x)+np.eye(d,dtype=int)[mu]) % L)
    P = np.array([(lidx[(x,mu)], lidx[(sh(x,mu),nu)], lidx[(sh(x,nu),mu)], lidx[(x,nu)])
                  for x in sites for mu in range(d) for nu in range(mu+1,d)])
    rng = np.random.default_rng(seed); nl = len(links); U = []
    for _ in range(nl):
        A = rng.normal(size=(N,N))+1j*rng.normal(size=(N,N)); Q,R = np.linalg.qr(A)
        Q = Q@np.diag(np.diag(R)/abs(np.diag(R))); U.append(Q/np.linalg.det(Q)**(1/N))
    U = np.array(U); n = nl*m; e = np.eye(n)
    def SW(Ua):
        Up = Ua[P[:,0]]@Ua[P[:,1]]@np.conj(np.transpose(Ua[P[:,2]],(0,2,1)))\
                                 @np.conj(np.transpose(Ua[P[:,3]],(0,2,1)))
        return np.sum(1-np.trace(Up,axis1=1,axis2=2).real/N)
    val = lambda v: SW(np.array([expm(sum(v[i*m+c]*T[c] for c in range(m)))@U[i] for i in range(nl)]))
    f0 = val(np.zeros(n)); fp = np.array([val(h*e[i]) for i in range(n)])
    fm = np.array([val(-h*e[i]) for i in range(n)]); H = np.zeros((n,n))
    for i in range(n):
        H[i,i] = (fp[i]-2*f0+fm[i])/h**2
        for j in range(i+1,n):
            H[i,j] = H[j,i] = (val(h*(e[i]+e[j]))+val(-h*(e[i]+e[j]))
                               -fp[i]-fm[i]-fp[j]-fm[j]+2*f0)/(2*h**2)
    w = np.linalg.eigvalsh(H); return w[0], w[-1]

print(hess_spectrum(2,3,2,0))   # (-1.9142, 2.4619)  vs corpus bound 1.0
print(hess_spectrum(2,2,3,0))   # (-2.9711, 3.4147)  vs corpus bound 2.0

**Caveat.** The repaired constant $14(d-1)/N$ is crude (a factor of a few above the observed operator norms); a sharp value is not determined here. The refutation of $6/N$ is unconditional.

**Why it matters.** $C_V(N)=6/N$ propagates into every quantitative statement in the corpus's finite-cutoff programme (the convexity window, the $12/g^2$ and $24/N$ constants, the block-Hessian mixing norm $M$). It needs to be corrected wherever it appears; the correction makes the obstruction sharper and the claimed windows narrower.

---

## 9. Localization template: local Poincaré on a core K + Dirichlet gap on the complement => global spectral gap

`status: gap` · `kind: theorem`

### Statement

Let $(\Omega,\mu)$ carry a reversible Markov generator $L$ with invariant probability $\mu$, carré du champ $\Gamma$, Dirichlet form $\mathcal E(f,f)=\int\Gamma(f)d\mu$ on domain $\mathcal D(\mathcal E)$. Fix a measurable core $K\subset\Omega$ with $\mu(K)>0$, $A:=\Omega\setminus K$, $\mu_K:=\mu(\cdot\cap K)/\mu(K)$.

**(H1)** *Local Poincaré on the core:* $\exists\rho_K>0$ with $\mathrm{Var}_{\mu_K}(f)\le\rho_K^{-1}\int_K\Gamma(f)\,d\mu_K$ for all $f\in\mathcal D(\mathcal E)$.

**(H2)** *Dirichlet gap on the complement:* $\lambda_A:=\inf\big\{\mathcal E(g,g)\big/\!\int_\Omega g^2d\mu\ :\ g\in\mathcal D(\mathcal E),\ g|_K=0,\ g\ne0\big\}>0$.

Then $\mu$ satisfies a global Poincaré inequality $\mathrm{Var}_\mu(f)\le C_P\,\mathcal E(f,f)$ with
$$C_P\;\le\;\max\Big\{\frac1{\rho_K},\ \frac{1+1/\mu(K)}{\lambda_A}\Big\},\qquad\text{i.e.}\qquad \lambda_1(-L)\;\ge\;\min\Big\{\rho_K,\ \frac{\mu(K)}{1+\mu(K)}\lambda_A\Big\},$$
and if $\mu(K)\ge1/2$ then $\lambda_1\ge\min\{\rho_K,\tfrac13\lambda_A\}$.
Crucially: **no global curvature lower bound is used**, so this route is not blocked by Theorem B.

### Derivation

Source: `RECOMMENDED_06_Localization_Theorem_Template.md` (six near-identical copies in the corpus; the version cited is complete). The proof is correct and short; I reproduce it in full and then flag the one genuine gap.

Let $f\in\mathcal D(\mathcal E)$ with $\int f\,d\mu=0$; put $m_K=\int f\,d\mu_K$, $m_A=\int f\,d\mu_A$. The two-set variance decomposition reads
$$\mathrm{Var}_\mu(f)=\mu(K)\mathrm{Var}_{\mu_K}(f)+\mu(A)\mathrm{Var}_{\mu_A}(f)+\mu(K)\mu(A)(m_K-m_A)^2 .$$

*Term 1.* By (H1), after converting the normalised inequality, $\mu(K)\mathrm{Var}_{\mu_K}(f)\le\rho_K^{-1}\int_K\Gamma(f)d\mu$.

*Term 2.* $\mu(A)\mathrm{Var}_{\mu_A}(f)\le\int_Af^2d\mu$. Put $g:=f\mathbf 1_A$, which vanishes on $K$; (H2) gives $\int_Af^2d\mu=\int g^2d\mu\le\lambda_A^{-1}\mathcal E(g,g)\le\lambda_A^{-1}\int_A\Gamma(f)d\mu$.

*Term 3.* From $\int f\,d\mu=0$: $\mu(K)m_K+\mu(A)m_A=0$, so $m_A=-\tfrac{\mu(K)}{\mu(A)}m_K$ and $m_K-m_A=m_K/\mu(A)$, whence
$$\mu(K)\mu(A)(m_K-m_A)^2=\frac{\mu(K)}{\mu(A)}m_K^2 .$$
On the other hand $\int_Af^2d\mu\ge\mu(A)m_A^2=\tfrac{\mu(K)^2}{\mu(A)}m_K^2$, so
$$\frac{\mu(K)}{\mu(A)}m_K^2\;\le\;\frac1{\mu(K)}\int_Af^2d\mu\;\le\;\frac1{\mu(K)\lambda_A}\int_A\Gamma(f)\,d\mu .$$

*Collect.* $\mathrm{Var}_\mu(f)\le\rho_K^{-1}\int_K\Gamma(f)d\mu+\big(\lambda_A^{-1}+(\mu(K)\lambda_A)^{-1}\big)\int_A\Gamma(f)d\mu\le C_P\,\mathcal E(f,f)$ with $C_P$ as stated, since $\Gamma(f)\ge0$ and $K,A$ partition $\Omega$. The spectral-gap form follows from the variational characterisation $\lambda_1=\inf\{\mathcal E(f,f)/\mathrm{Var}_\mu(f)\}$. $\square$

**The gap (identified; the corpus flags it parenthetically but does not fix it).** For a *diffusion* (local Dirichlet form, e.g. the Langevin generator on $\mathcal C_\Lambda$), $g=f\mathbf 1_A$ is generally **not** in $\mathcal D(\mathcal E)$: multiplying by a sharp indicator destroys the Sobolev regularity, and the chain rule $\mathcal E(f\mathbf 1_A,f\mathbf 1_A)\le\int_A\Gamma(f)$ is not available. The standard repair is a buffer: choose $K\subset K'$ and a Lipschitz cutoff $\chi$ with $\chi=1$ on $A=K^c$, $\chi=0$ on $\Omega\setminus K'$, and pay
$$\mathcal E(\chi f,\chi f)\;\le\;2\int\chi^2\Gamma(f)\,d\mu+2\int f^2\,\Gamma(\chi)\,d\mu ,$$
so the theorem survives with an extra term $\propto\|\Gamma(\chi)\|_\infty\,\mu(K'\setminus K)\,\|f\|_\infty^2$ that must be absorbed. On $\mathcal C_\Lambda$, where $K$ would be a set of the form $\{\|U_p-I\|\le\varepsilon\ \forall p\}$, $\|\Gamma(\chi)\|_\infty$ scales like (buffer width)$^{-2}$ and $\mu(K'\setminus K)$ is the *boundary layer* mass, not the bad-set mass — this is precisely where a volume-uniform estimate is needed and is not supplied anywhere in the corpus. In the *discrete/nonlocal* setting (jump kernels) the theorem as stated is fine.

**Where the two Yang-Mills inputs would come from.** (H1): a *localised* horizontal Hessian bound $\nabla^2S_{\mathrm{eff}}\succeq\rho_K\,I$ on the core; note $\rho_K$ may be positive even though $\rho_{\mathrm{glob}}<0$, because the bad configuration $U^*$ of Theorem D/E (one plaquette equal to $\mathrm{diag}(-1,-1,1,\dots)$) is far from the identity and carries Gibbs weight $\sim e^{-2\beta\cdot 2(d-1)/N\cdot\ldots}$ — cf. Item G, mass $\sim e^{-\beta}$ per link. (H2): an exit-time bound $\sup_{x\in A}\mathbb E_x[\tau_K]\le T$ gives $\lambda_A\ge1/T$, or a capacity bound on $A$.

### Constants and numbers

$C_P\le\max\{1/\rho_K,\ (1+1/\mu(K))/\lambda_A\}$; $\lambda_1\ge\min\{\rho_K,\ \tfrac{\mu(K)}{1+\mu(K)}\lambda_A\}$; for $\mu(K)\ge1/2$, factor $\tfrac{\mu(K)}{1+\mu(K)}\ge\tfrac13$.
Exit-time conversion: $\sup_{x\in A}\mathbb E_x[\tau_K]\le T\Rightarrow\lambda_A\ge1/T$.
Corpus SU(3) SAFE-region candidates for the core (all quoted, none certified): ball radius $R_0=0.05$ in exponential coordinates; convexity floor $\kappa_*=0.25$ (scan minimum $0.252$, values $0.291,0.275,0.265,0.260,0.257,0.255$ at $r=0.00,\dots,0.05$); Wilson variation budget $\delta\approx0.006$; per-step retention $\alpha=(\kappa_*-\delta)/\kappa_*\approx0.976$; BCH remainder coefficients $C_2\approx0.011$, $C_3\approx0.10$, $C_4\approx1.1$.

**Caveat.** Two real gaps: (i) $f\mathbf 1_A\notin\mathcal D(\mathcal E)$ for a diffusion - needs a buffer/cutoff and a boundary-layer estimate; (ii) neither (H1) nor (H2) is established for lattice Yang-Mills anywhere in the corpus with volume-uniform constants.

**Why it matters.** This is the correct constructive response to Theorem B: the impossibility is specific to the *global* infimum, and this theorem shows precisely what pair of local statements would replace it. Its constants are explicit and its proof (modulo the cutoff) is correct, so it is a usable target rather than a slogan.

---

## How these fit together

All eight items are one chain. Lemma A (compact + non-constant => a strictly negative Hessian direction, proved via int Delta f = 0) is the abstract engine; Theorem B turns it into the divergence rho_glob(beta) <= k_max - beta*lambda_f -> -infinity for the optimal CD(rho,infinity) constant of the Langevin generator; Proposition C supplies k_max(N) = N/2 exactly (SU(N)^|B| is Einstein with the bi-invariant metric, volume-independently); Theorem D supplies lambda_f >= 2(d-1)/N with a sharp explicit configuration; Theorem E upgrades D to the horizontal / gauge-invariant sector where the corpus's whole programme actually lives, with the exact closed form -2d(d-1)/(N(d-1+L^-d)) -> -2d/N, closing the only loophole; Corollary F feeds asymptotic freedom in and gets the log-divergence rate and the universal crossing at a*Lambda = 0.51; Proposition G gives the one exactly solvable case (one-link SU(N): rho = N/2 - beta/N, and for SU(2) the pointwise BE tensor (1 + (beta/2)cos theta) g) plus the exponentially small Gibbs mass of the bad set, which is simultaneously the reason localisation is plausible and the reason Holley-Stroock perturbation cannot deliver it. Item H (refutation of C_V(N)=6/N) is a byproduct of E and it re-prices every constant in the corpus's finite-cutoff 'convexity window' (rho_* = c_0 a^2 g^2 - 12/g^2, RG subwindow g^4 > 24/(c_0 a^2), mixed-block norm M = 12/g^2 - all of these need C_V >= 8/N, <= 42/N). Item I is the constructive escape route the obstruction forces, and the corpus's other continuum-facing modules attach to it: the discrete Riccati / curvature-budget law rho_{k+1} >= rho_k - M_k^2/rho_k with its consequence rho_k^2 >= rho_0^2 - 2 sum M_j^2 (a correct algebraic reading of the Schur-complement/Brascamp-Lieb block-Hessian lemma), the typical-set BE constant rho_typ(a;epsilon), and the two scale-free 'sigma_*' candidates (Weyl-denominator convexity, orbit-volume/FP determinant convexity). Proposition C Step 6 also resolves a normalisation confusion that pervades the corpus: the 'Haar spark c_0 a^2 g^2' and 'Ric >= kappa_G' are the same geometric fact in two charts, so the positive side of the BE tensor is an a-independent O(N) constant, never an a^2 g^2 one - which makes the obstruction cleaner, not weaker.

## Further material found but not fully extracted

Not extracted in full, but real and in my area: (1) The block-Hessian / Schur-complement lemma - if Hess S = [[A,B],[B^T,C]] with A >= alpha, C >= gamma > 0, ||B|| <= M, then after marginalising y, Hess_x S_coarse >= (alpha - M^2/gamma) I, with the correct mechanism Hess_x S_coarse = E[A] - Cov(grad_x S) controlled by Brascamp-Lieb. This is stated correctly in several files (RECOMMENDED_03, lemma_unity_stitched_curvature_rg.md §7.1, referee_local_horizontal_convexity...md §5) but the proof is only sketched; it is the one genuinely reusable analytic lemma in the RG lane and deserves its own full write-up. (2) The Weyl-denominator convexity lemma in RICCATI/01_riccati_flow/referee_riccati_spine_and_sigma_geom_sources.md §3: for S_geom(theta) = -log|Delta(theta)|^2 = -sum_{i<j} log(4 sin^2((theta_i-theta_j)/2)) on the regular set of the maximal torus, delta^2 S_geom[x,x] = (1/2) sum_{i<j} csc^2((theta_i-theta_j)/2) (x_i-x_j)^2 >= (N/2)||x||^2 on sum x_i = 0. That identity and the >= N/2 constant look correct and are scale-free; it is the cleanest 'sigma_*' candidate in the corpus and I did not verify the restriction step in detail. (3) The orbit-volume / Faddeev-Popov determinant Hessian decomposition delta^2 S_orb = -(1/2)Tr(M^{-1} delta^2 M) + (1/2)Tr(M^{-1} delta M M^{-1} delta M) with M(U) = D_U^* D_U, second term manifestly >= 0 - the decomposition is rigorous, the uniform lower bound is not established. (4) HESSIAN/Core_Hessian/05_curvature_defect_obstruction_principle.md contains a genuinely interesting 'obstruction principle' (defect functional Phi(a) = E_mu[max(0, kappa_* - lambda_min(H_phys))]; if Phi(a_n) -> 0 the continuum limit is Gaussian, so an interacting limit forces inf Phi > 0), together with an honest correction that the dream monotonicity identity H_{a'} = E[H_a | G_{a'}] is false for Wilsonian blocking (the effective Hessian carries an extra covariance/Fisher term). Worth a separate extraction. (5) F_global_curvature_heat_kernel_template.md gives the positive counterpart: for heat-kernel (Villain) plaquette weights V_t = -log K_t, a global CD(kappa_G - nu*C_hol*M_2(t), infinity) holds - i.e. global BE IS available at fixed smoothing time t, which is exactly the regime the Wilson action fails; the t-dependence of M_2(t) as t -> 0 is where it breaks and is not computed. (6) The polarity/capacity result (reducible configurations form a codim >= 2 real algebraic set, hence Cap = 0 for the elliptic Dirichlet form) is correct and independent of everything above. (7) COLAB_RUNS/ notebooks carry stored outputs; I did not mine them for BE-curvature scans.
