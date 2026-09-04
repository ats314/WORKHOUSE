---
id: EX-006
title: "Obstruction: gauge invariance forces Haar link marginals, so the small-field 'good set' carrying the matrix-hinge / Bakry-Émery curvature bound is exponentially atypical in the volume, and t"
kind: extraction
items: 6
status_breakdown: {"solid": 5, "conditional": 1}
program: yang_mills
extracted_by: claude-opus-5 subagent, 2026-09-01
stance: preservation (content extraction, not refereeing)
source_files:
  - HAAR/01_haar_mass/01_CORE_THEOREMS/01_matrix_hinge_haar_wilson.md
  - HAAR/01_haar_mass/01_CORE_THEOREMS/A_local_BE_curvature.md
  - HELFFER_SJOSTRAND/04_Decay_Localization_OS/Core_5__Local_Coercivity_and_Matrix_Hinge_on_Good_Set(1).md
  - HELFFER_SJOSTRAND/04_Decay_Localization_OS/EXCITING_05_LOCALIZATION_AVERAGED_BADNESS(1).md
  - HAAR/archive/duplicates/Appendix_A__Notation_and_Constants(1).md
  - LSI_POINCARE/archive/Appendix_I__Localization_Algebra(1).md
  - WILSON/archive/Appendix_J__Typicality_Mechanism_for_K(1).md
  - HAAR/01_haar_mass/04_SU2_CALCULATIONS/3_fixed_cutoff_mass_gap_su2.md
  - HELFFER_SJOSTRAND/04_Decay_Localization_OS/MG_Localization_Typicality_Unconditioning.md
  - _EXTRACT_FOR_LLM/02_candidates/CAND-002-structural-obstruction-the-small-field-set-carrying-the-matr.md
  - _EXTRACT_FOR_LLM/02_candidates/CAND-006-structural-obstruction-the-pointwise-matrix-hinge-good-set-i.md
  - HAAR/01_haar_mass/07_SAFE_REGION/11_haar_gauge_fixing_rigorous.md
---

# Obstruction: gauge invariance forces Haar link marginals, so the small-field "good set" carrying the matrix-hinge / Bakry-Émery curvature bound is exponentially atypical in the volume, and the localization inequality that consumes it is vacuous

> For any gauge-invariant measure on $G^{E}$ every link marginal is exactly Haar and, more strongly, the $|V|-1$ links of any spanning tree are i.i.d. Haar; hence $\mu(K_\Lambda(r))\le \mathrm{Haar}(B_r(\mathbf 1))^{|V|-1}\to 0$ exponentially in the volume for every $\beta$, which refutes Assumption A.11.2 of the corpus, makes the covariance-localization inequality $|\mathrm{Cov}_\mu|\le|\mathrm{Cov}_{\mu|K}|+8\|F\|_\infty\|G\|_\infty\mu(K^c)$ weaker than the trivial bound, and (with an explicit counterexample configuration) exposes the average-set/sup-set quantifier slip that the corpus uses to bridge the gap.

**6 extracted items** — 1 conditional, 5 solid

---

## 1. Theorem 1 (Haar link marginals for any gauge-invariant measure)

`status: solid` · `kind: theorem`

### Statement

Let $G$ be a compact (Hausdorff, second countable) topological group with normalized Haar measure $\mathrm{Haar}$. Let $\Gamma=(V,E)$ be a finite oriented multigraph with no self-loops (every $b\in E$ has distinct tail $t(b)$ and head $h(b)$). Put $M:=G^{E}$ and let the lattice gauge group $\mathcal G:=G^{V}$ act on $M$ by
$$(g\cdot U)_b := g_{t(b)}\,U_b\,g_{h(b)}^{-1},\qquad g=(g_x)_{x\in V}\in G^V,\ U=(U_b)_{b\in E}\in G^E .$$
Let $\mu$ be ANY $\mathcal G$-invariant Borel probability measure on $M$ (no Gibbs structure, no $\beta$, no dimension, no action assumed). Then for every link $b\in E$ the marginal law $\mu_b:=(\pi_b)_*\mu$ of $U_b$ is exactly the Haar probability measure on $G$:
$$\mu_b(A)=\mathrm{Haar}(A)\qquad\text{for every Borel }A\subseteq G .$$
In particular, for the Wilson–Haar Gibbs measure $\mu_{\Lambda,\beta}(dU)=Z^{-1}e^{-S_{\Lambda,\beta}(U)}\,\mathrm{vol}_{g_\Lambda}(dU)$ (Definition A.6.5 of the corpus), and for $\mu_{\Lambda,\beta}$ modified by ANY additional gauge-invariant term $S_{\mathrm{add}}$, and for every $\beta\in\mathbb R$ and every volume $\Lambda$, one has $\mathbb P_{\mu}[U_b\in B_r(\mathbf 1)]=\mathrm{Haar}(B_r(\mathbf 1))$.

Corollary 1.1 (single-link bound). With $K_\Lambda(r):=\{U\in M:\ U_b\in B_r(\mathbf 1)\ \forall b\in E\}$ the linkwise small-field set of $\S4$ of `01_matrix_hinge_haar_wilson.md` and of Theorem 5.4 of `A_local_BE_curvature.md`,
$$\mu(K_\Lambda(r))\ \le\ \mathrm{Haar}(B_r(\mathbf 1))\ <\ 1,$$
uniformly in $\beta$ and in $|\Lambda|$, for every gauge-invariant $\mu$.

### Derivation

Fix $b\in E$ and write $x:=t(b)$, $y:=h(b)$; by hypothesis $x\neq y$. Fix $\omega\in G$ and define the *one-vertex* gauge transformation
$$g^{(\omega)}\in\mathcal G,\qquad g^{(\omega)}_x:=\omega,\qquad g^{(\omega)}_z:=e\ \ (z\in V\setminus\{x\}).$$
Because $y\neq x$ we have $g^{(\omega)}_y=e$, hence
$$\bigl(g^{(\omega)}\cdot U\bigr)_b=g^{(\omega)}_x\,U_b\,\bigl(g^{(\omega)}_y\bigr)^{-1}=\omega\,U_b .$$
So the measurable bijection $T_\omega:M\to M$, $T_\omega(U):=g^{(\omega)}\cdot U$, acts on the $b$-th coordinate exactly by left multiplication by $\omega$: $\pi_b\circ T_\omega=\omega\cdot\pi_b$. (It also acts on the other links incident to $x$; this is irrelevant for the $b$-marginal.)

Gauge invariance of $\mu$ means $(T_\omega)_*\mu=\mu$. Therefore, for every Borel $A\subseteq G$,
$$\mu_b(A)=\mu\bigl(\pi_b^{-1}(A)\bigr)=\bigl((T_\omega)_*\mu\bigr)\bigl(\pi_b^{-1}(A)\bigr)=\mu\bigl(T_\omega^{-1}\pi_b^{-1}(A)\bigr)=\mu\bigl(\{U:\ \omega U_b\in A\}\bigr)=\mu_b(\omega^{-1}A).$$
Thus $\mu_b$ is a left-invariant Borel probability measure on the compact group $G$. By uniqueness of Haar measure on a compact group, $\mu_b=\mathrm{Haar}$. $\square$

Remarks that sharpen the statement.
(a) The argument uses ONLY invariance under gauge transformations supported at a single vertex. It is therefore insensitive to $\beta$, to the dimension $d$, to the choice of action (Wilson, improved, with any gauge-invariant $S_{\mathrm{add},\Lambda}$ of Section 5 of `A_local_BE_curvature.md`), and to boundary conditions.
(b) The same argument applied at the head vertex gives right invariance, so one also gets $\mu_b(A)=\mu_b(A\omega)$ directly; only one of the two is needed.
(c) The hypothesis $t(b)\neq h(b)$ holds for the periodic hypercubic lattice $\Lambda_L=(\mathbb Z/L\mathbb Z)^d$ as soon as $L\ge 2$ (for $L=2$ the graph is a multigraph with double edges, which is allowed).
(d) Corollary 1.1 is immediate: $K_\Lambda(r)\subseteq\pi_b^{-1}(B_r(\mathbf 1))$ for each fixed $b$, so $\mu(K_\Lambda(r))\le\mu_b(B_r(\mathbf 1))=\mathrm{Haar}(B_r(\mathbf 1))$.
[Reconstructed: the entire proof above is mine. The corpus states the fact only in the meta-document `_EXTRACT_FOR_LLM/02_candidates/CAND-002...md` as a two-line assertion; the mathematical files never state it, and `Appendix_A` Assumption A.11.2 assumes the opposite.]

### Constants and numbers

No constants beyond the group. The bound $\mathrm{Haar}(B_r(\mathbf 1))<1$ holds for every $r<\mathrm{diam}(G)$. Explicit values of $\mathrm{Haar}(B_r(\mathbf 1))$ for $G=\mathrm{SU}(2),\mathrm{SU}(3)$ are in Item 3. With the corpus's own admissible radius $r\le r_{\mathrm{sf}}\le \iota_G/8=\sqrt2\pi/8=0.5553603672697958$ (Definitions A.3.7, A.7.1, A.7.4), one gets $\mathrm{Haar}_{\mathrm{SU}(2)}(B_{r_{\mathrm{sf}}})\le 1.2460\times10^{-2}$ and $\mathrm{Haar}_{\mathrm{SU}(3)}(B_{r_{\mathrm{sf}}})\le 4.073\times10^{-6}$.

**Caveat.** Requires no self-loops, i.e. $L\ge 2$; and requires $\mu$ invariant under the full gauge group $G^{V}$ (a gauge-FIXED measure is not, and the theorem correctly says nothing about it).

**Why it matters.** It shows that the small-field domain on which the corpus's only genuine curvature theorem (the matrix hinge, Prop. 6 of `01_matrix_hinge_haar_wilson.md`; Theorem 5.4 of `A_local_BE_curvature.md`) is valid can never be typical, for structural reasons that no choice of $\beta$, action, Lyapunov function or concentration inequality can change. It converts an open technical gap ('turning a local hinge into a global statement requires a localization/typicality mechanism') into a proved impossibility for this class of good set.

---

## 2. Theorem 2 (tree-gauge factorization; the $|V|-1$ tree links are i.i.d. Haar; volume-exponential decay of the small-field set)

`status: solid` · `kind: obstruction`

### Statement

Setting as in Theorem 1, with $\Gamma=(V,E)$ finite, connected, no self-loops. Let $T\subseteq E$ be a spanning tree, $|T|=|V|-1$, and fix a root $x_0\in V$. Let $\mu$ be ANY $\mathcal G$-invariant Borel probability measure on $M=G^E$.

(i) (Factorization) In the tree-gauge coordinates $\Theta:G^{V\setminus\{x_0\}}\times G^{E\setminus T}\to G^{E}$ defined by
$$h_{x_0}:=e,\qquad U_b:=h_{t(b)}^{-1}h_{h(b)}\ \ (b\in T),\qquad U_b:=h_{t(b)}^{-1}W_b\,h_{h(b)}\ \ (b\in E\setminus T),$$
$\Theta$ is a bijection, and the pullback $\lambda:=(\Theta^{-1})_*\mu$ factorizes as
$$\lambda=\mathrm{Haar}^{\otimes (V\setminus\{x_0\})}\otimes \nu ,$$
where $\nu$ is the law of the reduced ('loop') variables $W\in G^{E\setminus T}$. That is: $h$ is uniform and independent of $W$.

(ii) (i.i.d. Haar tree links) Consequently the family $(U_b)_{b\in T}$ is i.i.d. with common law $\mathrm{Haar}$, and is independent of $W$.

(iii) (Volume-exponential atypicality) For every $r>0$,
$$\boxed{\ \mu\bigl(K_\Lambda(r)\bigr)\ \le\ \mathrm{Haar}\bigl(B_r(\mathbf 1)\bigr)^{\,|V|-1}\ }$$
with $K_\Lambda(r)=\{U:\ U_b\in B_r(\mathbf 1)\ \forall b\in E\}$. On $\Lambda_L=(\mathbb Z/L\mathbb Z)^4$ one has $|V|=L^4$, $|E|=4L^4$, $|P|=6L^4$, so $|V|-1=\tfrac16|P(\Lambda_L)|-1$ and
$$\mu_{\Lambda_L,\beta}\bigl(K_{\Lambda_L}(r)\bigr)\ \le\ \exp\Bigl(-c(r)\,|P(\Lambda_L)|+c(r)\Bigr),\qquad c(r):=\tfrac16\log\frac1{\mathrm{Haar}(B_r(\mathbf 1))}>0,$$
uniformly in $\beta$.

(iv) (Refutation of Assumption A.11.2) Assumption A.11.2 of `Appendix_A__Notation_and_Constants.md` states $\mu_{\Lambda_L,\beta}(K_{\Lambda_L}^c)\le \exp(-c_{\mathrm{typ}}|P(\Lambda_L)|)$ for some $c_{\mathrm{typ}}>0$. If $K_{\Lambda_L}=K_{\Lambda_L}(r)$ (the set on which the matrix hinge is actually proved), then A.11.2 is FALSE: (iii) gives $\mu(K)\le e^{-c(r)|P|+c(r)}$, so $1=\mu(K)+\mu(K^c)\le e^{-c(r)|P|+c(r)}+e^{-c_{\mathrm{typ}}|P|}<1$ for all $|P|$ large. In fact $\mu(K^c)\to 1$.

Correction to the corpus. `CAND-002` asserts the exponent $|E|-|V|+1$ (the cycle rank). That is the wrong count and is not provable: the $|E|-|V|+1$ reduced loop variables $W_b$ are NOT Haar (at large $\beta$ they concentrate near the identity up to global conjugation). The correct, provable exponent is the tree count $|V|-1$, which is exactly the number of gauge directions modulo the constant subgroup. The conclusion (exponential decay in the volume) is unaffected; in $d=4$ the corrected exponent is $|E|/4$ rather than $3|E|/4$.

### Derivation

Step 1: $\Theta$ is a bijection. Given $U\in G^E$, define $h$ recursively along $T$ from the root: $h_{x_0}:=e$; if $b\in T$ joins an already-assigned vertex to a new vertex, the relation $U_b=h_{t(b)}^{-1}h_{h(b)}$ determines the new $h$ uniquely (either $h_{h(b)}=h_{t(b)}U_b$ or $h_{t(b)}=h_{h(b)}U_b^{-1}$). Since $T$ is a spanning tree this assigns every $h_x$ exactly once. Then $W_b:=h_{t(b)}U_b h_{h(b)}^{-1}$ for $b\notin T$. Conversely $\Theta$ recovers $U$. Note the geometric meaning: $h\cdot U$ has all tree links equal to $e$ and free links equal to $W$, i.e. $h$ is the unique tree-gauge-fixing transformation normalized by $h_{x_0}=e$.

Step 2: how the gauge group acts in $(h,W)$ coordinates. Let $g\in\mathcal G$. Since $(hg^{-1})\cdot(g\cdot U)=h\cdot U=(e_T,W)$ and $(hg^{-1})_{x_0}=g_{x_0}^{-1}$, the normalized tree-gauge-fixer of $g\cdot U$ is $h'':=g_{x_0}\cdot(hg^{-1})$, i.e. $h''_x=g_{x_0}h_xg_x^{-1}$, and $h''\cdot(g\cdot U)=g_{x_0}\cdot(e_T,W)=(e_T,\mathrm{Ad}_{g_{x_0}}W)$ because a constant gauge transformation fixes $e$ on every link and conjugates the rest. Hence
$$g\cdot\Theta(h,W)=\Theta\bigl(\,(g_{x_0}h_xg_x^{-1})_{x\neq x_0}\,,\ g_{x_0}Wg_{x_0}^{-1}\,\bigr).$$

Step 3: factorization. Restrict to the subgroup $\mathcal G_0:=\{g\in\mathcal G:\ g_{x_0}=e\}\cong G^{V\setminus\{x_0\}}$. By Step 2, $g\in\mathcal G_0$ acts in coordinates by
$$(h,W)\longmapsto (h g^{-1},\,W)\qquad\text{(componentwise right multiplication on }h\text{, }W\text{ untouched)}.$$
This is a free transitive right action of the compact group $G^{V\setminus\{x_0\}}$ on the $h$-fiber, leaving $W$ fixed. Since $\lambda=(\Theta^{-1})_*\mu$ is invariant under this action, disintegrate $\lambda$ over $W$: the conditional law $\lambda(\,dh\mid W)$ is a right-invariant probability measure on $G^{V\setminus\{x_0\}}$ for $\nu$-a.e. $W$, hence equals $\mathrm{Haar}^{\otimes(V\setminus\{x_0\})}$ by uniqueness of Haar. Therefore $\lambda=\mathrm{Haar}^{\otimes(V\setminus\{x_0\})}\otimes\nu$. This proves (i).

Step 4: the tree links. $(U_b)_{b\in T}=(h_{t(b)}^{-1}h_{h(b)})_{b\in T}$ is a function of $h$ alone, hence independent of $W$. The map $\Psi: h\mapsto (h_{t(b)}^{-1}h_{h(b)})_{b\in T}$ pushes $\mathrm{Haar}^{\otimes(V\setminus\{x_0\})}$ onto $\mathrm{Haar}^{\otimes T}$: order $T$ by a breadth-first search from $x_0$, so that the $i$-th tree edge introduces exactly one new vertex $z_i$; conditionally on $h_{z_1},\dots,h_{z_{i-1}}$ the $i$-th tree-link variable is either $h_{\mathrm{parent}}^{-1}h_{z_i}$ or $h_{z_i}^{-1}h_{\mathrm{parent}}$, and in both cases $h_{z_i}\mapsto U_{b_i}$ is (left translation composed with, possibly, inversion) a Haar-preserving bijection of $G$. Hence conditionally on the past, $U_{b_i}\sim\mathrm{Haar}$; by induction the joint law is $\mathrm{Haar}^{\otimes T}$ and the coordinates are i.i.d. This proves (ii).

Step 5: the bound. $K_\Lambda(r)\subseteq\{U_b\in B_r(\mathbf 1)\ \forall b\in T\}$, whose probability is $\prod_{b\in T}\mathrm{Haar}(B_r(\mathbf 1))=\mathrm{Haar}(B_r(\mathbf 1))^{|V|-1}$ by (ii). This proves (iii); (iv) is arithmetic. $\square$

Sanity checks. (a) At $\beta=0$, $\mu=\mathrm{Haar}^{\otimes E}$ and $\mu(K(r))=\mathrm{Haar}(B_r)^{|E|}\le\mathrm{Haar}(B_r)^{|V|-1}$: consistent, and shows the bound is not tight at $\beta=0$. (b) For $\mu$ = uniform measure on the pure-gauge orbit $\{U_b=g_{t(b)}g_{h(b)}^{-1}\}$ (a genuine gauge-invariant measure) the tree links are exactly i.i.d. Haar and the bound is attained up to the free-link constraints, so the exponent $|V|-1$ is sharp in general. (c) The bound is tight in order at large $\beta$: there the loop variables $W$ concentrate, so the only binding constraints are the $|V|-1$ gauge directions.

[Reconstructed: Steps 1–5 are entirely mine. The corpus contains no tree-gauge factorization statement; `CAND-002` asserts the decay with the wrong exponent and no proof.]

### Constants and numbers

Hypercubic periodic $d=4$ counts (Lemma J.4.1 of Appendix J, verified): $|V|=L^4$, $|E|=4L^4$, $|P|=6L^4$, $|E|/|P|=2/3$, $\nu_P\le 2(d-1)=6$, $D_E\le 3\nu_P=18$, $m_\partial=4$.

With $r=r_{\mathrm{sf}}=\iota_G/8=\sqrt2\pi/8=0.55536$ (the LARGEST radius the corpus ever allows, Definition A.7.4):
  SU(2): $\mathrm{Haar}(B_r)=1.24605\times10^{-2}$, $c(r)=\tfrac16\ln(1/1.24605\times10^{-2})=0.73077$ per plaquette.
  SU(3): $\mathrm{Haar}(B_r)=4.0734\times10^{-6}$, $c(r)=\tfrac16\ln(1/4.0734\times10^{-6})=2.0685$ per plaquette.
Resulting bounds $\mu(K_{\Lambda_L}(r_{\mathrm{sf}}))\le \mathrm{Haar}(B_{r_{\mathrm{sf}}})^{L^4-1}$:
  $L=4$ ($|V|-1=255$): SU(2) $\le e^{-1118}$; SU(3) $\le e^{-3165}$.
  $L=8$ ($|V|-1=4095$): SU(2) $\le e^{-1.796\times10^{4}}$; SU(3) $\le e^{-5.082\times10^{4}}$.
  $L=16$ ($|V|-1=65535$): SU(2) $\le e^{-2.874\times10^{5}}$; SU(3) $\le e^{-8.134\times10^{5}}$.
With the hinge-forced radius $r=c_0/\beta$ (see Item 5): e.g. $\beta=6$, $c_0=0.5$, $r=0.0833$: SU(2) $\mathrm{Haar}(B_r)=4.339\times10^{-5}$; SU(3) $\le 1.113\times10^{-12}$.

**Caveat.** The bound uses only the tree links, so it is not sharp at small $\beta$; and it says nothing about a gauge-FIXED measure, where the tree links are frozen by construction (that is precisely the escape route, at the cost of Gribov copies and slice boundaries — see `HAAR/01_haar_mass/07_SAFE_REGION/11_haar_gauge_fixing_rigorous.md`, which supplies no quantitative slice theorem).

**Why it matters.** This is the strongest mathematics in this part of the corpus: it upgrades 'the good set is not known to be typical' to 'the good set has probability $e^{-\Theta(\text{volume})}$ for every gauge-invariant measure', so no Lyapunov drift, LSI, Poincaré or concentration argument can ever supply Assumption A.11.2 for this good set. Combined with Item 4 it closes the small-field Bakry-Émery route as written.

---

## 3. Explicit Haar small-ball volumes for SU(N): exact closed form for SU(2), sharp elementary bound and verified numerics for SU(3)

`status: solid` · `kind: numerical_result`

### Statement

Metric normalization (Definitions A.3.4–A.3.6 of Appendix A): on $\mathfrak g=\mathfrak{su}(N)$ take $\langle X,Y\rangle_{\mathfrak g}:=-\Re\mathrm{Tr}\bigl(d\rho(X)d\rho(Y)\bigr)$ in the defining representation $\rho$ ($n=N$), i.e. $|X|^2=\mathrm{Tr}(X^\dagger X)=\|X\|_{HS}^2$; $g_G$ is the bi-invariant metric obtained by translating it. Write $D:=\dim G=N^2-1$, $\omega_D:=\pi^{D/2}/\Gamma(\tfrac D2+1)$ (volume of the unit ball in $\mathbb R^D$), $B_r(\mathbf 1)$ the geodesic ball, and $\mathrm{Haar}(B_r):=\mathrm{vol}_{g_G}(B_r)/\mathrm{vol}_{g_G}(G)$.

(a) Geometric constants. $\mathrm{Ric}_G=\tfrac N2\,g_G$ exactly, so Assumption A.3.8 holds with $\kappa_G=N/2$; the scalar curvature is $\mathrm{Scal}=\tfrac N2(N^2-1)$; the Haar mass of Definition A.8.3 is $m_H^2=\kappa_G/3=N/6$. Injectivity radius $\iota_G=\sqrt2\,\pi$ for all $N\ge2$. Total volumes
$$\mathrm{vol}(\mathrm{SU}(N))=\sqrt N\,\frac{(2\pi)^{(N^2+N-2)/2}}{1!\,2!\cdots (N-1)!},\qquad \mathrm{vol}(\mathrm{SU}(2))=4\sqrt2\,\pi^2,\quad \mathrm{vol}(\mathrm{SU}(3))=16\sqrt3\,\pi^5 .$$

(b) Universal elementary upper bound. For every $0<r\le\iota_G$,
$$\mathrm{vol}_{g_G}(B_r(\mathbf 1))\ \le\ \omega_D\,r^{D},\qquad\text{hence}\qquad \mathrm{Haar}(B_r(\mathbf 1))\ \le\ \frac{\omega_D\,r^{D}}{\mathrm{vol}(G)} .$$
Explicitly
$$\mathrm{Haar}_{\mathrm{SU}(2)}(B_r)\le \frac{r^3}{3\sqrt2\,\pi}=0.0750264\,r^3,\qquad \mathrm{Haar}_{\mathrm{SU}(3)}(B_r)\le \frac{r^8}{384\sqrt3\,\pi}=4.785841\times10^{-4}\,r^8 .$$

(c) SU(2): exact closed form. For $0\le r\le\sqrt2\pi$,
$$\mathrm{vol}_{g_G}(B_r)=4\pi r-2\sqrt2\,\pi\sin(\sqrt2\,r),\qquad \mathrm{Haar}_{\mathrm{SU}(2)}(B_r)=\frac{\sqrt2\,r-\sin(\sqrt2\,r)}{2\pi}.$$
($\mathrm{SU}(2)$ with this metric is the round 3-sphere of radius $\sqrt2$; the formula gives $1$ at $r=\sqrt2\pi$.)

(d) SU(3): exact integral representation and second-order expansion.
$$\mathrm{vol}(B_r)=\int_{\{|X|\le r\}\subset\mathfrak g} J(X)\,dX,\qquad J(X)=\prod_{\alpha\in\Delta^+}\Bigl(\frac{\sin(\alpha(X)/2)}{\alpha(X)/2}\Bigr)^2\le 1 ,$$
which reduces by Weyl integration on $\mathfrak g$ to a $2$-dimensional integral over the Cartan (code below). Second order: $\mathrm{vol}(B_r)=\omega_D r^D\bigl[1-\tfrac{\mathrm{Scal}}{6(D+2)}r^2+O(r^4)\bigr]$, i.e. $1-0.1\,r^2$ for SU(2) and $1-0.2\,r^2$ for SU(3).

### Derivation

1. Metric and Ricci. For $X\in\mathfrak{su}(N)$ (anti-Hermitian, traceless) $\langle X,X\rangle=-\Re\mathrm{Tr}(X^2)=\mathrm{Tr}(X^\dagger X)$. For a bi-invariant metric on a compact group, $\mathrm{Ric}(X,Y)=-\tfrac14 B(X,Y)$ with $B$ the Killing form. For $\mathfrak{su}(N)$, $B(X,Y)=2N\,\mathrm{Tr}(XY)=-2N\langle X,Y\rangle$, so $\mathrm{Ric}=\tfrac N2\langle\cdot,\cdot\rangle$, i.e. $\kappa_G=N/2$. Cross-check for $N=2$: $\mathrm{SU}(2)=\{a_0I+i\,\mathbf a\!\cdot\!\boldsymbol\sigma\}\cong S^3$; a tangent vector $X=i\mathbf a\!\cdot\!\boldsymbol\sigma$ has $|X|^2=2|\mathbf a|^2$, so the metric is $2\times$ the unit-sphere metric, i.e. a round $S^3$ of radius $R=\sqrt2$; then $\mathrm{Ric}=(3-1)R^{-2}g=g$, matching $\kappa_G=1$. This *proves* Assumption A.3.8 with an explicit constant (the corpus only assumes it).

2. The Haar-Jacobian bound $J\le1$. For a compact group with bi-invariant metric, $\exp$ is the Riemannian exponential at $\mathbf 1$ and its Jacobian is $J(X)=\det\bigl(\tfrac{1-e^{-\mathrm{ad}_X}}{\mathrm{ad}_X}\bigr)$. The nonzero eigenvalues of $\mathrm{ad}_X$ on $\mathfrak g_{\mathbb C}$ are $\{i\alpha(X)\}_{\alpha\in\Delta}$; pairing $\alpha$ with $-\alpha$,
$$\frac{1-e^{-i\alpha}}{i\alpha}\cdot\frac{1-e^{i\alpha}}{-i\alpha}=\frac{2-2\cos\alpha}{\alpha^2}=\Bigl(\frac{\sin(\alpha/2)}{\alpha/2}\Bigr)^2 ,$$
and the $\mathrm{rank}$ zero eigenvalues contribute $1$. Hence $J(X)=\prod_{\alpha\in\Delta^+}(\mathrm{sinc}(\alpha(X)/2))^2\in[0,1]$. For $r\le\iota_G$ the geodesic ball is $B_r(\mathbf 1)=\exp(\{|X|\le r\})$, so $\mathrm{vol}(B_r)=\int_{|X|\le r}J\,dX\le\int_{|X|\le r}dX=\omega_D r^D$. This gives (b). It is elementary and needs no volume comparison theorem.

3. Injectivity radius. Along a geodesic $t\mapsto\exp(tX)$ the first conjugate point occurs at the smallest $t>0$ with $\alpha(tX)=2\pi$ for some root $\alpha$. With our metric, for $X$ with eigenvalues $i\theta_1,\dots,i\theta_N$, $|X|^2=\sum\theta_j^2$ and $\alpha_{jk}(X)=\theta_j-\theta_k$, so $\max_\alpha|\alpha(X)|\le\sqrt2\,|X|$ with equality for $\theta=(\lambda,-\lambda,0,\dots)$. Hence the first conjugate point along a unit-speed geodesic is at $t=2\pi/\sqrt2=\sqrt2\pi$. The shortest closed geodesic through $\mathbf 1$ is $\exp(tX)$ with $\exp(X)=\mathbf 1$, i.e. $\theta_j\in2\pi\mathbb Z$, $\sum\theta_j=0$; the minimum of $|X|$ is $2\pi\sqrt2$ (take $\theta=2\pi(1,-1,0,\dots)$), so half of it is again $\sqrt2\pi$. Thus $\iota_G=\sqrt2\pi$.

4. SU(2) exact ball volume. $\mathfrak{su}(2)\cong\mathbb R^3$ with $|X|=\rho$; one positive root, $\alpha(X)=2\lambda$ where $\pm i\lambda$ are the eigenvalues of $X$, and $|X|^2=2\lambda^2$ so $\lambda=\rho/\sqrt2$. Then $J=(\sin\lambda/\lambda)^2$ and
$$\mathrm{vol}(B_r)=\int_0^r 4\pi\rho^2\frac{\sin^2(\rho/\sqrt2)}{(\rho/\sqrt2)^2}d\rho=8\pi\int_0^r\sin^2\!\bigl(\rho/\sqrt2\bigr)d\rho=4\pi r-2\sqrt2\pi\sin(\sqrt2 r).$$
Dividing by $\mathrm{vol}(\mathrm{SU}(2))=4\sqrt2\pi^2$ gives (c). Taylor: $\mathrm{Haar}(B_r)=\tfrac{(\sqrt2 r)^3}{12\pi}-\dots=\tfrac{r^3}{3\sqrt2\pi}\bigl(1-\tfrac{r^2}{10}+\dots\bigr)$, matching (b) and the curvature correction $1-\mathrm{Scal}\,r^2/(6(D+2))=1-3r^2/30$.

5. SU(3) numerical evaluation (independent of the volume formula, cross-checked by Monte Carlo). Parametrize the Cartan $\mathfrak t=\{\mathrm{diag}(i\theta_1,i\theta_2,i\theta_3):\sum\theta_j=0\}$ by an orthonormal basis $e_1=\tfrac1{\sqrt2}(1,-1,0)$, $e_2=\tfrac1{\sqrt6}(1,1,-2)$: $\theta=ue_1+ve_2$, $|X|^2=u^2+v^2$; the three positive roots are $\alpha_1=\sqrt2\,u$, $\alpha_2=-u/\sqrt2+\sqrt{3/2}\,v$, $\alpha_3=u/\sqrt2+\sqrt{3/2}\,v$. Weyl integration on the algebra gives, for $\mathrm{Ad}$-invariant $f$, $\int_{\mathfrak g}f\,dX=C\int_{\mathfrak t}f\,\Delta^2\,dH$ with $\Delta=\prod_{\alpha>0}\alpha$ and a constant $C$ fixed by the $f\equiv1$, small-radius case: $\omega_8r^8=C\,I_0(1)r^8$ with $I_0(1)=\int_{u^2+v^2\le1}\Delta^2$, so $C=\omega_8/I_0(1)$. Hence
$$\mathrm{vol}(B_r)=\frac{\omega_8}{I_0(1)}\int_{u^2+v^2\le r^2}J\,\Delta^2\,du\,dv .$$
Numerically $I_0(1)=0.19634951$ ($=\pi/16$), and (dividing by $16\sqrt3\pi^5=8480.666$) the resulting $\mathrm{Haar}_{\mathrm{SU}(3)}(B_r)$ is tabulated below. Independent Monte-Carlo check with $4\times10^5$ Haar-random SU(3) matrices (QR of a complex Ginibre matrix, phase-fixed, determinant-normalized; $d(\mathbf 1,U)=\min\sqrt{\sum\theta_j^2}$ over lifts $\theta_j\equiv\arg\lambda_j\pmod{2\pi}$ with $\sum\theta_j=0$) gives $\mathbb P[d\le2.0]=5.396\times10^{-2}$ vs. the formula's $5.394\times10^{-2}$ — agreement to $4\times10^{-4}$ relative, which validates both the Weyl reduction and the value $\mathrm{vol}(\mathrm{SU}(3))=16\sqrt3\pi^5$.

[Reconstructed: items 1–5 are mine. The corpus supplies only the symbols $\kappa_G$, $\iota_G$, $r_{\mathrm{sf}}$, $\chi_G(r)$ (Definition J.2.2) with no evaluation anywhere.]

### Constants and numbers

Universal: $\omega_3=4\pi/3=4.1887902$, $\omega_8=\pi^4/24=4.0587121$. $\iota_G=\sqrt2\pi=4.4428829$; $r_{\log}=\iota_G/2=2.2214415$; $r_{\mathrm{sf}}\le r_{\log}/4=0.5553604$.
SU(2): $D=3$, $\kappa_G=1$, $\mathrm{Scal}=3$, $m_H^2=1/3$, $\mathrm{vol}(G)=4\sqrt2\pi^2=55.830914$, leading coefficient $1/(3\sqrt2\pi)=0.07502636$.
SU(3): $D=8$, $\kappa_G=3/2$, $\mathrm{Scal}=12$, $m_H^2=1/2$, $\mathrm{vol}(G)=16\sqrt3\pi^5=8480.6663$, leading coefficient $1/(384\sqrt3\pi)=4.7858411\times10^{-4}$.

Table of $\mathrm{Haar}(B_r(\mathbf 1))$ (exact for SU(2), Weyl-integral numerics for SU(3); last column = ratio to the elementary bound $\omega_Dr^D/\mathrm{vol}(G)$):
 r      SU(2) exact     ratio     SU(3) numeric   ratio
 0.05   9.375951e-06    0.99975   1.868534e-14    0.99950
 0.10   7.495137e-05    0.99900   4.776278e-12    0.99800
 0.20   5.978146e-04    0.99601   1.215410e-09    0.99203
 0.30   —               —         3.083945e-08    0.98215
 0.50   9.146609e-03    0.97530   1.778155e-06    0.95116
 0.5554 1.246046e-02    0.96960   4.073429e-06    0.94006
 0.80   —               —         7.060984e-05    0.87940
 1.00   6.787125e-02    0.90463   3.913390e-04    0.81770
 1.50   —               —         7.770915e-03    0.63355
 2.00   4.011270e-01    0.66831   5.393870e-02    0.44025
 4.4429 1.000000e+00    0.15198   —               —
Monte-Carlo cross-check SU(3) ($M=4\times10^5$): $r=1.0$: $3.65\times10^{-4}$ (formula $3.913\times10^{-4}$, $\sim146$ hits so $\pm 8\%$); $r=1.5$: $7.998\times10^{-3}$ (formula $7.771\times10^{-3}$); $r=2.0$: $5.396\times10^{-2}$ (formula $5.394\times10^{-2}$).

### Code

# Haar small-ball measure of SU(2) (exact) and SU(3) (Weyl integral). Run: python haar.py
import numpy as np
from scipy.special import gamma
pi = np.pi
omega = lambda d: pi**(d/2)/gamma(d/2+1)          # unit-ball volume in R^d
VolSU2 = 4*np.sqrt(2)*pi**2                        # 55.830914
VolSU3 = 16*np.sqrt(3)*pi**5                       # 8480.6663

# ---- SU(2): exact closed form, valid for 0 <= r <= sqrt(2)*pi ----
haar_su2 = lambda r: (np.sqrt(2)*r - np.sin(np.sqrt(2)*r))/(2*pi)

# ---- SU(3): vol(B_r) = (omega_8/I0(1)) * int_{|H|<=r, H in Cartan} J(H) Delta(H)^2 dH ----
s2, s32 = np.sqrt(2), np.sqrt(1.5)
def roots(u, v):                                   # 3 positive roots in an ON basis of the Cartan
    return s2*u, -u/s2 + s32*v, u/s2 + s32*v
def Delta2(u, v):
    a1, a2, a3 = roots(u, v); return (a1*a2*a3)**2
def sinc2(a):
    x = a/2.0
    return np.where(np.abs(x) < 1e-12, 1.0, (np.sin(x)/np.where(x == 0, 1, x))**2)
def J(u, v):
    a1, a2, a3 = roots(u, v); return sinc2(a1)*sinc2(a2)*sinc2(a3)
def polar(r, f, n=3000, m=3000):                   # midpoint polar quadrature on the 2d Cartan disc
    rho = (np.arange(n)+0.5)/n*r; phi = (np.arange(m)+0.5)/m*2*pi
    R, P = np.meshgrid(rho, phi, indexing='ij')
    return (f(R*np.cos(P), R*np.sin(P))*R).sum()*(r/n)*(2*pi/m)
I0 = polar(1.0, Delta2)                            # = pi/16 = 0.19634951
haar_su3 = lambda r: omega(8)*polar(r, lambda u, v: J(u, v)*Delta2(u, v))/I0/VolSU3

# elementary universal upper bounds (J <= 1):  Haar(B_r) <= omega_D r^D / vol(G)
bound_su2 = lambda r: omega(3)*r**3/VolSU2         # = r^3/(3 sqrt2 pi)
bound_su3 = lambda r: omega(8)*r**8/VolSU3         # = r^8/(384 sqrt3 pi)
for r in [0.05, 0.1, 0.2, 0.5, 0.5553604, 1.0, 2.0]:
    print(r, haar_su2(r), bound_su2(r), haar_su3(r), bound_su3(r))

**Caveat.** The SU(3) values in the table are numerical quadrature (relative error $<10^{-4}$ by grid refinement, and confirmed independently by Monte Carlo at $r=2$); only the upper bound $\omega_Dr^D/\mathrm{vol}(G)$ and the SU(2) closed form are exact in closed form.

**Why it matters.** It turns the obstruction from qualitative to quantitative: it supplies the only number the obstruction needs, $\mathrm{Haar}(B_r(\mathbf 1))$, in closed or verified numerical form, and simultaneously supplies proved values ($\kappa_G=N/2$, $\iota_G=\sqrt2\pi$, $m_H^2=N/6$) for constants the corpus leaves as unevaluated symbols in Appendix A.

---

## 4. The localization inequality and its vacuity (law of total covariance, correct constants 2/6/8, and the failure of the constant 4)

`status: solid` · `kind: derivation`

### Statement

Let $(\Omega,\mathcal F,\mu)$ be a probability space and $K\in\mathcal F$ with $0<\mu(K)<1$; write $\mu_K:=\mu(\cdot\mid K)$, $\mu_{K^c}:=\mu(\cdot\mid K^c)$, $\alpha:=\mu(K)$, and for bounded measurable $F,G$ put $\Delta_KF:=\mu_K(F)-\mu_{K^c}(F)$.

(i) (Law of total covariance, exact identity)
$$\mathrm{Cov}_\mu(F,G)=\alpha\,\mathrm{Cov}_{\mu_K}(F,G)+(1-\alpha)\,\mathrm{Cov}_{\mu_{K^c}}(F,G)+\alpha(1-\alpha)\,\Delta_KF\,\Delta_KG .$$

(ii) (Sup-norm localization bound) $\ |\mathrm{Cov}_\nu(F,G)|\le 2\|F\|_\infty\|G\|_\infty$ for every probability measure $\nu$, hence
$$|\mathrm{Cov}_\mu(F,G)|\ \le\ |\mathrm{Cov}_{\mu_K}(F,G)|+6\,\|F\|_\infty\|G\|_\infty\,\mu(K^c),$$
and a fortiori the corpus's Proposition I.3.2 with the constant $8$ (which uses the weaker $|\mathrm{Cov}_\nu|\le4\|F\|_\infty\|G\|_\infty$). In oscillation seminorms $\mathrm{osc}(F):=\sup F-\inf F$ the sharper form is
$$|\mathrm{Cov}_\mu(F,G)|\le|\mathrm{Cov}_{\mu_K}(F,G)|+\tfrac54\,\mathrm{osc}(F)\,\mathrm{osc}(G)\,\mu(K^c).$$
The constant $4$ written in `MG_Localization_Typicality_Unconditioning.md` §3 is NOT obtainable from this decomposition (the two error terms already contribute $2+4=6$ in sup norm) and should be read as $6$ or $8$.

(iii) (Vacuity under Theorem 2) The unconditional trivial bound is $|\mathrm{Cov}_\mu(F,G)|\le2\|F\|_\infty\|G\|_\infty$. If $\mu(K^c)\ge1/3$ the error term in (ii) already exceeds it, so the inequality carries no information whatsoever. By Theorem 2, for $K=K_\Lambda(r)$ one has $\mu(K^c)\ge 1-\mathrm{Haar}(B_r(\mathbf 1))^{|V|-1}$, which for SU(2), $r=r_{\mathrm{sf}}$, $L=4$ is $\ge 1-e^{-1118}$. Hence the entire conditional-to-unconditional bridge of `Appendix_I` / `Core_6` / `BEST_05` degenerates: the bound obtained after paying for a conditional Helffer–Sjöstrand estimate is strictly worse than writing down $|\mathrm{Cov}|\le2\|F\|_\infty\|G\|_\infty$ with no work at all.

### Derivation

(i) Write $A:=\mu_K(F)$, $B:=\mu_{K^c}(F)$, $C:=\mu_K(G)$, $D:=\mu_{K^c}(G)$. Since $\mu=\alpha\mu_K+(1-\alpha)\mu_{K^c}$,
$$\mu(FG)=\alpha\mu_K(FG)+(1-\alpha)\mu_{K^c}(FG)=\alpha\bigl(\mathrm{Cov}_{\mu_K}+AC\bigr)+(1-\alpha)\bigl(\mathrm{Cov}_{\mu_{K^c}}+BD\bigr),$$
$$\mu(F)\mu(G)=\bigl(\alpha A+(1-\alpha)B\bigr)\bigl(\alpha C+(1-\alpha)D\bigr)=\alpha^2AC+\alpha(1-\alpha)(AD+BC)+(1-\alpha)^2BD .$$
Subtracting and using $\alpha-\alpha^2=(1-\alpha)-(1-\alpha)^2=\alpha(1-\alpha)$,
$$\mathrm{Cov}_\mu=\alpha\mathrm{Cov}_{\mu_K}+(1-\alpha)\mathrm{Cov}_{\mu_{K^c}}+\alpha(1-\alpha)\bigl(AC+BD-AD-BC\bigr),$$
and $AC+BD-AD-BC=(A-B)(C-D)=\Delta_KF\,\Delta_KG$. $\square$

(ii) For any probability $\nu$: $|\mathrm{Cov}_\nu(F,G)|\le|\nu(FG)|+|\nu(F)||\nu(G)|\le2\|F\|_\infty\|G\|_\infty$. Also $|\Delta_KF|\le|\mu_K(F)|+|\mu_{K^c}(F)|\le2\|F\|_\infty$ and likewise for $G$. Feed into (i), use $\alpha\le1$, $\alpha(1-\alpha)\le(1-\alpha)=\mu(K^c)$:
$$|\mathrm{Cov}_\mu|\le|\mathrm{Cov}_{\mu_K}|+\mu(K^c)\cdot2\|F\|_\infty\|G\|_\infty+\mu(K^c)\cdot4\|F\|_\infty\|G\|_\infty=|\mathrm{Cov}_{\mu_K}|+6\mu(K^c)\|F\|_\infty\|G\|_\infty .$$
The corpus's Lemma I.3.1 instead bounds $|\mathrm{Cov}_\nu|\le\|F-\nu F\|_\infty\|G-\nu G\|_\infty\le4\|F\|_\infty\|G\|_\infty$, giving $4+4=8$: correct, just lossier. For the oscillation version use the sharp bound $|\mathrm{Cov}_\nu(F,G)|\le\tfrac14\mathrm{osc}(F)\mathrm{osc}(G)$ (Grüss inequality) and $|\Delta_KF|\le\mathrm{osc}(F)$ (both conditional means lie in $[\inf F,\sup F]$), yielding $\tfrac14+1=\tfrac54$.

(iii) Immediate: $6\mu(K^c)\|F\|_\infty\|G\|_\infty>2\|F\|_\infty\|G\|_\infty$ as soon as $\mu(K^c)>1/3$, and Theorem 2 gives $\mu(K^c)=1-o(1)$ doubly fast in the volume. Note also that the same conclusion follows already from Corollary 1.1 alone at $\Lambda$-independent level: $\mu(K^c)\ge1-\mathrm{Haar}(B_r(\mathbf 1))\ge1-1.25\times10^{-2}$ for SU(2) at $r=r_{\mathrm{sf}}$, so the localization inequality is vacuous even in a single fixed volume, before any thermodynamic limit is taken.

[Reconstructed: (i) and the $8$-constant version are in the corpus (`Appendix_I__Localization_Algebra(1).md`, Lemma I.2.1 and Proposition I.3.2) and are correct; the constants $2$, $6$, $5/4$, the Grüss refinement, the identification of the erroneous $4$, and part (iii) are mine.]

### Constants and numbers

Constants in the localization error: sup-norm $6$ (sharp for this route), corpus value $8$ (valid), $4$ (invalid). Oscillation-seminorm constant $5/4$. Vacuity threshold: the inequality is weaker than the trivial bound as soon as $\mu(K^c)>1/3$ (sup-norm, constant $6$), $\mu(K^c)>1/4$ (constant $8$). Actual values under Theorem 2: $\mu(K^c)\ge1-1.246\times10^{-2}$ from one link alone (SU(2), $r=r_{\mathrm{sf}}$); $\ge1-e^{-1118}$ on $L=4$; $\ge1-e^{-2.87\times10^5}$ on $L=16$.

**Caveat.** The identity and the bounds are exact and unconditional; the vacuity conclusion is specific to good sets of the linkwise or plaquette-sup type (it does not apply to the averaged good set $K(\varepsilon)$ of Appendix J, which is genuinely typical — but which does not support the pointwise hinge; see Item 6).

**Why it matters.** This is the precise point where the obstruction bites the corpus's main pipeline. `Core_6`, `BEST_05_Lattice_Mass_Gap_Pipeline_from_Hinge_to_OS.md` and `Core_8` all pass from conditional to unconditional clustering through exactly this inequality; Item 4 shows the passage is not merely unproved but delivers a bound worse than doing nothing.

---

## 5. The plaquette (gauge-invariant) small-field set: conditional-resampling bound and explicit thresholds

`status: conditional` · `kind: obstruction`

### Statement

The Haar-marginal argument of Theorem 1 does not apply to the gauge-INVARIANT good set of Definition Core-5.1.2,
$$\mathcal K^{\mathrm{plaq}}_{\Lambda,\beta}(r):=\bigl\{U:\ d_G\bigl(U_p(U),\mathbf 1\bigr)\le r\ \ \forall p\in P(\Lambda)\bigr\},$$
so a separate argument is needed. Setting: $G=\mathrm{SU}(N)$ in the defining representation, $\mu_{\Lambda,\beta}$ the Wilson–Haar Gibbs measure, $d=4$, $\nu_P\le6$, $D_E\le18$, $D=\dim G=N^2-1$, $L_\vartheta:=\sup_G|\nabla_G\vartheta|\le N^{-1/2}$ for $\vartheta(V)=1-\tfrac1N\Re\mathrm{Tr}V$.

Lemma 5.1 (conditional independence on a link-independent set). Let $S\subseteq E(\Lambda)$ contain no two links lying on a common plaquette. Then, conditionally on $(U_b)_{b\notin S}$, the variables $(U_b)_{b\in S}$ are independent, and the conditional law of $U_b$ is $\nu_b(dV)\propto e^{-\beta\Psi_b(V)}\,\mathrm{Haar}(dV)$ with $\Psi_b(V):=\sum_{p\ni b}\vartheta(U_p(V,\cdot))$, $0\le\Psi_b\le2\nu_P$, $\mathrm{Lip}(\Psi_b)\le\nu_PL_\vartheta$. Such an $S$ with $|S|\ge|E|/(D_E+1)\ge|E|/19$ exists by greedy colouring of the link-adjacency graph.

Lemma 5.2 (one-link small-ball bound). For every Borel $\mathcal A\subseteq G$ and every $0<\rho\le\pi/\sqrt2$,
$$\nu_b(\mathcal A)\ \le\ e^{\beta\nu_PL_\vartheta\rho}\ \frac{\mathrm{Haar}(\mathcal A)}{\mathrm{Haar}(B_\rho(\mathbf 1))} .$$

Proposition 5.3 (plaquette good set is exponentially atypical at the hinge-admissible radius). Suppose the hinge radius is $r=c_0/\beta$ (this is what Core-5's own constraint $C_{\mathrm{WH}}\beta r_\beta\le2m_H^2$ forces: $c_0=2m_H^2/C_{\mathrm{WH}}=N/(3C_{\mathrm{WH}})$). Then, with $\rho:=\sqrt N/(\beta\nu_P)$ (admissible once $\beta\ge\sqrt N\sqrt2/(\nu_P\pi)$),
$$\mu_{\Lambda,\beta}\bigl(\mathcal K^{\mathrm{plaq}}_{\Lambda,\beta}(r)\bigr)\ \le\ q^{\,|S|}\ \le\ q^{\,|E(\Lambda)|/19},\qquad q:=e\,\Bigl(\frac\pi2\Bigr)^{N(N-1)}\Bigl(\frac{c_0\,\nu_P}{\sqrt N}\Bigr)^{D},$$
which is $\beta$-independent. Hence if $q<1$ — equivalently $c_0<c_0^{\mathrm{crit}}(N)$ — the plaquette good set has probability $e^{-\Theta(|\Lambda|)}$ uniformly in $\beta$, and Corollary 4(iii) again applies.

Explicit thresholds ($\nu_P=6$): $\mathrm{SU}(2)$: $q=512.204\,c_0^3$, so $q<1$ iff $c_0<0.124983$. $\mathrm{SU}(3)$: $q=8.46718\times10^{5}\,c_0^{8}$, so $q<1$ iff $c_0<0.181565$.

### Derivation

Lemma 5.1. Write $S_{\Lambda,\beta}=\beta\sum_p\vartheta(U_p)$. By construction each plaquette $p$ contains at most one link of $S$, so $\vartheta(U_p)$ depends on at most one $S$-variable. Grouping,
$$e^{-S_{\Lambda,\beta}(U)}=\Bigl(\prod_{b\in S}\prod_{p\ni b}e^{-\beta\vartheta(U_p)}\Bigr)\cdot\prod_{p:\,\partial p\cap S=\emptyset}e^{-\beta\vartheta(U_p)} ,$$
and the first product factorizes over $b\in S$ with the $b$-th factor depending only on $U_b$ and on links outside $S$. Since the reference measure $\mathrm{Haar}^{\otimes E}$ is a product, the conditional law given $(U_b)_{b\notin S}$ is the stated product. The bounds on $\Psi_b$ follow from $0\le\vartheta\le2$ (Lemma J.1.2) and $\#\{p\ni b\}\le\nu_P$. The Lipschitz bound uses bi-invariance: $V\mapsto U_p(V,\cdot)$ is an isometry $G\to G$ up to left/right translation and inversion, and $\vartheta$ is $L_\vartheta$-Lipschitz; $L_\vartheta\le N^{-1/2}$ because $\frac{d}{dt}\vartheta(e^{tX}V)|_{t=0}=-\tfrac1N\Re\mathrm{Tr}(XV)$ and $|\mathrm{Tr}(XV)|\le\|X\|_{HS}\|V\|_{HS}=|X|\sqrt N$. Existence of $S$: the link-adjacency graph ($b\sim b'$ iff a plaquette contains both) has maximal degree $D_E\le3\nu_P\le18$ (Proposition A.2.11); a greedy independent set has size $\ge|E|/(D_E+1)$.

Lemma 5.2. Let $\Psi_b^{\min}:=\min_G\Psi_b$, attained at some $V_*$. Numerator: $\int_{\mathcal A}e^{-\beta\Psi_b}\le e^{-\beta\Psi_b^{\min}}\mathrm{Haar}(\mathcal A)$. Denominator: on $B_\rho(V_*)$, $\Psi_b\le\Psi_b^{\min}+\nu_PL_\vartheta\rho$, so $\int_Ge^{-\beta\Psi_b}\ge e^{-\beta\Psi_b^{\min}-\beta\nu_PL_\vartheta\rho}\mathrm{Haar}(B_\rho(V_*))$, and $\mathrm{Haar}(B_\rho(V_*))=\mathrm{Haar}(B_\rho(\mathbf 1))$ by invariance. Divide.

Proposition 5.3. For each $b\in S$ pick one plaquette $p(b)\ni b$; distinct $b$'s give distinct $p(b)$'s. Writing $U_{p(b)}=A_bU_b^{\pm1}B_b$ with $A_b,B_b$ depending only on links outside $S$, the event $\{d(U_{p(b)},\mathbf 1)\le r\}$ is $\{U_b\in\mathcal A_b\}$ for a set $\mathcal A_b$ obtained from $B_r(\mathbf 1)$ by left/right translation and possibly inversion; since Haar is bi-invariant and inversion-invariant, $\mathrm{Haar}(\mathcal A_b)=\mathrm{Haar}(B_r(\mathbf 1))$. Therefore, by Lemma 5.1,
$$\mu\bigl(\mathcal K^{\mathrm{plaq}}(r)\bigm|(U_b)_{b\notin S}\bigr)\le\prod_{b\in S}\nu_b(\mathcal A_b) .$$
Apply Lemma 5.2 to each factor and take expectations. It remains to bound $\mathrm{Haar}(B_r)/\mathrm{Haar}(B_\rho)$. Upper bound on the numerator: $\mathrm{Haar}(B_r)\le\omega_Dr^D/\mathrm{vol}(G)$ (Item 3(b)). Lower bound on the denominator: for $|X|\le\rho$ and any root $\alpha$, $|\alpha(X)|\le\sqrt2\rho$, so if $\rho\le\pi/\sqrt2$ then $|\alpha(X)/2|\le\pi/2$ and $\sin u/u\ge2/\pi$ there, whence $J(X)\ge(2/\pi)^{2|\Delta^+|}=(2/\pi)^{N(N-1)}$ and $\mathrm{Haar}(B_\rho)\ge(2/\pi)^{N(N-1)}\omega_D\rho^D/\mathrm{vol}(G)$. Hence
$$\frac{\mathrm{Haar}(B_r)}{\mathrm{Haar}(B_\rho)}\le\Bigl(\frac\pi2\Bigr)^{N(N-1)}\Bigl(\frac r\rho\Bigr)^{D}.$$
Choosing $\rho=1/(\beta\nu_PL_\vartheta)$ makes $e^{\beta\nu_PL_\vartheta\rho}=e$; with $L_\vartheta=N^{-1/2}$ this is $\rho=\sqrt N/(\beta\nu_P)$ and $r/\rho=(c_0/\beta)\cdot\beta\nu_P/\sqrt N=c_0\nu_P/\sqrt N$, giving the stated $\beta$-independent $q$. $\square$

Interpretation (the mechanism named in `CAND-006`). $\rho\asymp\beta^{-1}$ appears only because of the *Lipschitz* lower bound; the true conditional fluctuation of a link is $\asymp\beta^{-1/2}$, since $\vartheta(e^Y)=|Y|^2/(2N)$ so $\beta\Psi_b$ is quadratic with curvature $\asymp\beta$. Using that instead of Lipschitz replaces $r/\rho$ by $r\beta^{1/2}=c_0\beta^{-1/2}$, which $\to0$: the hinge-forced radius $\beta^{-1}$ is a factor $\beta^{-1/2}$ below the typical plaquette deviation $\beta^{-1/2}$, so $\nu_b(\mathcal A_b)=O(\beta^{-D/2})\to0$ and the good-set probability is $e^{-\Theta(|\Lambda|\log\beta)}$. Making that quantitative requires a uniform Laplace lower bound on $\int e^{-\beta\Psi_b}$, which I have not written out; the Lipschitz version above is what is fully proved here.

[Reconstructed: Lemmas 5.1, 5.2 and Proposition 5.3, including the thresholds, are mine. The corpus states only the qualitative reason — `EXCITING_05`, §2.2: a max-event's complement 'is controlled only by a union bound, typically producing a factor $|P(\Lambda)|$. That factor is exactly what later poisons uniform bounds.']

### Constants and numbers

$\nu_P\le6$, $D_E\le18$, $|S|\ge|E|/19$, $m_\partial=4$, $L_\vartheta\le N^{-1/2}$ ($=0.7071$ for SU(2), $0.5774$ for SU(3)), $\rho=\sqrt N/(\beta\nu_P)$ admissible for $\beta\ge\sqrt{2N}/(\nu_P\pi)$ ($\beta\ge0.106$ for SU(2), $\beta\ge0.130$ for SU(3)).
Threshold constants: SU(2) $q=e(\pi/2)^2(6/\sqrt2)^3c_0^3=512.204\,c_0^3$, $c_0^{\mathrm{crit}}=0.124983$; SU(3) $q=e(\pi/2)^6(6/\sqrt3)^8c_0^8=8.46718\times10^5\,c_0^8$, $c_0^{\mathrm{crit}}=0.181565$.
Core-5's own constraint reads $C_{\mathrm{WH}}\beta r_\beta\le2m_H^2$ with $m_H^2=\kappa_G/3=N/6$; equivalently $r\le c_0/\beta$, $c_0=N/(3C_{\mathrm{WH}})$. The parallel constraint in `01_matrix_hinge_haar_wilson.md` §6 is $R_W(r)=C_W\beta r\le c_H/2=\kappa_G/2$, i.e. $r\le N/(4C_W\beta)$. Both are $\propto1/\beta$.

**Caveat.** Conditional in two ways: it needs $q<1$, i.e. the (never evaluated) corpus constant $C_{\mathrm{WH}}$ to satisfy $C_{\mathrm{WH}}>N/(3c_0^{\mathrm{crit}})$; and it uses the Lipschitz rather than the Laplace lower bound on the conditional normalization, so the true decay ($\beta^{-D/2}$ per link) is stronger than what is proved here.

**Why it matters.** It closes the only escape route left after Theorem 2: replacing the linkwise good set by the gauge-invariant plaquette-sup good set (which is what Core-5 actually does, precisely to make the set gauge invariant) does not restore typicality. Together, Theorem 2 and Proposition 5.3 cover both good sets that appear anywhere in the corpus.

---

## 6. The average-set / sup-set quantifier slip, with an explicit configuration on which the matrix hinge fails inside the typical set

`status: solid` · `kind: obstruction`

### Statement

The corpus's only proved typicality estimate (Theorem J.4.3 of `Appendix_J__Typicality_Mechanism_for_K(1).md`) concerns the AVERAGED good set
$$K_\Lambda(\varepsilon):=\Bigl\{U:\ \overline\vartheta_\Lambda(U):=\tfrac1{|P(\Lambda)|}\textstyle\sum_{p}\vartheta(U_p)\le\varepsilon\Bigr\},$$
and states $\mu_{\Lambda_L,\beta}(K_\Lambda(\varepsilon)^c)\le e^{-c_{\mathrm{typ}}|P(\Lambda_L)|}$ with $c_{\mathrm{typ}}=\beta(\varepsilon-L_\vartheta m_\partial r)-\tfrac23\chi_G(r)$, $\chi_G(r)=\log(\mathrm{vol}(G)/\mathrm{vol}(B_r))$. That theorem is CORRECT (its proof — chessboard-free: bound $e^{-S}\le e^{-\beta\varepsilon|P|}$ on the complement, and bound $Z$ below by restricting to the linkwise ball $A_\Lambda(r)$ — is valid), but it is a statement about a DIFFERENT set from the one the matrix hinge needs. Definition J.5.2 then sets '$K_{\Lambda_L}:=K_{\Lambda_L}(\varepsilon)$', and `3_fixed_cutoff_mass_gap_su2.md` §2 bridges with the phrase that hypothesis (H-GOOD) 'is produced by the matrix hinge + Bakry–Émery module on a small-field region (and then extended to $K$ as needed)'. That extension is false.

Proposition 6 (the pointwise hinge fails inside $K_\Lambda(\varepsilon)$, explicitly). Let $G=\mathrm{SU}(2)$, $d=4$, $\Lambda=\Lambda_L$, $\nu_P=6$, and let $U^*$ be the configuration with $U^*_{b_0}=-I$ for one fixed link $b_0$ and $U^*_b=I$ for all other links. Then:
(i) $\overline\vartheta_\Lambda(U^*)=12/|P(\Lambda_L)|=2/L^4$, so $U^*\in K_\Lambda(\varepsilon)$ for every $\varepsilon>0$ as soon as $L^4\ge2/\varepsilon$;
(ii) there is a unit vector $X$ in the $b_0$-fibre with
$$\nabla^2S_{\Lambda,\beta}(U^*)(X,X)=-\,\frac{\nu_P\beta}{N}\,|X|^2=-3\beta,\qquad \mathrm{Ric}_{\mu_{\Lambda,\beta}}(U^*)(X,X)=\kappa_G-3\beta=1-3\beta ;$$
(iii) hence for every $\beta>1/3$ the Bakry–Émery curvature of $\mu_{\Lambda,\beta}$ has a NEGATIVE eigenvalue at a point of $K_\Lambda(\varepsilon)$, so Proposition Core-5.2.4 ($\mathrm{Ric}_\mu\succeq m_H^2\,\mathrm{Id}+\tfrac12\alpha_Wd_1^*d_1\succ0$) and hypothesis (H-GOOD) cannot hold on $K_\Lambda(\varepsilon)$.
General $N$: the same construction gives $\mathrm{Ric}_\mu(U^*)(X,X)\le\kappa_G-\nu_P\beta/N=\tfrac N2-\tfrac{6\beta}N$, negative for $\beta>N^2/12$.

Conclusion. Exactly one of the two sets can be had at a time: the averaged set $K_\Lambda(\varepsilon)$ is typical (Theorem J.4.3) but does not support the pointwise hinge (Proposition 6); the linkwise set $K_\Lambda(r)$ and the plaquette-sup set $\mathcal K^{\mathrm{plaq}}(r)$ support the hinge but are exponentially atypical (Theorem 2, Proposition 5.3). Assumption A.11.2 is therefore either true-but-useless or useful-but-false, depending on which set it is read for.

### Derivation

(i) $\vartheta(V)=1-\tfrac12\Re\mathrm{Tr}V$ so $\vartheta(I)=0$ and $\vartheta(-I)=1+1=2$. Every plaquette not containing $b_0$ has holonomy $I$ and $\vartheta=0$. Every plaquette $p$ containing $b_0$ has holonomy equal to the ordered product of four link variables, three of which are $I$ and one is $(-I)^{\pm1}=-I$, so $U^*_p=-I$ and $\vartheta=2$. There are exactly $\nu_P=6$ such plaquettes on the $d=4$ hypercubic lattice. Hence $\sum_p\vartheta=12$ and $\overline\vartheta=12/|P|=12/(6L^4)=2/L^4$.

(ii) Let $X\in\mathfrak{su}(2)$ with $|X|^2=-\mathrm{Tr}(X^2)=1$, placed in the $b_0$ fibre and zero on all other links; e.g. $X=i\sigma_3/\sqrt2$. Because the metric is bi-invariant, the curve $t\mapsto e^{tX}U^*_{b_0}$ is a geodesic in the $b_0$-factor and hence $t\mapsto U^*(t)$ (all other links frozen) is a geodesic in $M_\Lambda$; therefore the Riemannian Hessian equals the second $t$-derivative. For a plaquette $p\ni b_0$, $U_p(t)=e^{\pm tX}\cdot(-I)$ up to a global conjugation (which leaves $\mathrm{Tr}$ invariant), so
$$\vartheta(U_p(t))=1-\tfrac12\Re\mathrm{Tr}\bigl(-e^{\pm tX}\bigr)=1+\tfrac12\Re\mathrm{Tr}\,e^{\pm tX},\qquad \tfrac{d^2}{dt^2}\Big|_{0}=\tfrac12\mathrm{Tr}(X^2)=-\tfrac12|X|^2=-\tfrac12 .$$
(Numerically verified by central differences: $-0.5000000$.) Note $\tfrac12=\tfrac1N$ for $N=2$, so each bad plaquette contributes $-\beta/N$. Summing the $\nu_P=6$ plaquettes through $b_0$ (all other plaquettes are at $U_p=I$ and are unaffected by $X$, since they do not contain $b_0$):
$$\nabla^2S_{\Lambda,\beta}(U^*)(X,X)=\beta\sum_{p\ni b_0}\tfrac{d^2}{dt^2}\vartheta(U_p(t))\Big|_0=-\tfrac{\nu_P\beta}{N}=-3\beta .$$
Adding $\mathrm{Ric}_{g_\Lambda}(X,X)=\kappa_G|X|^2=1$ (Lemma 3.1 of `A_local_BE_curvature.md` together with $\kappa_G=N/2=1$ from Item 3) gives $\mathrm{Ric}_\mu(U^*)(X,X)=1-3\beta$.

(iii) $M^{\mathrm{hinge}}_{\Lambda}=m_H^2\mathrm{Id}+\tfrac12\alpha_Wd_1^*d_1\succeq m_H^2\mathrm{Id}=\tfrac13\mathrm{Id}\succ0$; but $\mathrm{Ric}_\mu(U^*)(X,X)=1-3\beta<0<\tfrac13|X|^2$ for $\beta>1/3$. Hence the hinge fails at $U^*\in K_\Lambda(\varepsilon)$. Likewise (H-GOOD), a Poincaré inequality on $K$ with a volume-uniform constant, cannot be obtained from Bakry–Émery on $K_\Lambda(\varepsilon)$, since the curvature is not bounded below by a positive constant there.

Remark (why $\varepsilon$-averaging cannot be fixed by shrinking $\varepsilon$). $\overline\vartheta\le\varepsilon$ constrains only the average, so it permits $\lfloor\varepsilon|P|/2\rfloor$ plaquettes with $\vartheta=2$; more precisely $\#\{p:\vartheta_p\ge t\}\le\varepsilon|P|/t$ by Markov. For any fixed $\varepsilon>0$ the number of admissible maximally-bad plaquettes grows linearly with the volume, so the pointwise matrix inequality can never be recovered on $K_\Lambda(\varepsilon)$ at any $\varepsilon>0$.

Remark (Theorem J.4.3 is nonvacuous only at large $\beta$). Positivity of $c_{\mathrm{typ}}=\beta(\varepsilon-L_\vartheta m_\partial r)-\tfrac23\chi_G(r)$ requires $\beta\ge\tfrac{2\chi_G(r)}{3(\varepsilon-4L_\vartheta r)}$, and $\chi_G(r)\sim D\log(1/r)+\log(\mathrm{vol}(G)/\omega_D)$ blows up as $r\downarrow0$, so $r$ must be chosen at a fixed positive value and $\beta$ correspondingly large — the opposite regime from the small-$\beta$ convexity window used elsewhere in the corpus.

[Reconstructed: Proposition 6 (the explicit $U^*$, the value $-\nu_P\beta/N$, the threshold $\beta>1/3$, and the Markov remark) is mine; the numerical value $-\beta/N$ per bad plaquette also appears in the corpus as `HESSIAN/.../RECOMMENDED_02` Lemma 2.1. The identification of the quantifier slip is stated without proof in `CAND-002`/`CAND-006`.]

### Constants and numbers

SU(2), $d=4$: $\vartheta(-I)=2$; $\overline\vartheta(U^*)=12/|P|=2/L^4$; number of bad plaquettes $=\nu_P=6$; per-plaquette Hessian eigenvalue $-\beta/N=-\beta/2$ (verified by central differences to $2\times10^{-8}$); total $\nabla^2S(U^*)(X,X)=-3\beta$; $\kappa_G=1$; $\mathrm{Ric}_\mu(U^*)(X,X)=1-3\beta$, which equals $0.400$ at $\beta=0.2$, $0$ at $\beta=1/3$, $-0.500$ at $\beta=0.5$, $-5.000$ at $\beta=2$, $-17.000$ at $\beta=6$. General $N$: threshold $\beta>N^2/(2\nu_P)=N^2/12$, i.e. $\beta>1/3$ (SU(2)), $\beta>3/4$ (SU(3)).
Appendix J constants: $c_{E:P}=|E|/|P|=2/3$ in $d=4$; $c_{\mathrm{typ}}(\beta;\varepsilon,r)=\beta(\varepsilon-L_\vartheta m_\partial r)-\tfrac23\chi_G(r)$; sufficient condition $\beta\ge2c_{E:P}\chi_G(r)/(\varepsilon-L_\vartheta m_\partial r)$; with $\varepsilon\in(0,2)$, $m_\partial=4$, $L_\vartheta\le N^{-1/2}$.

### Code

# Verifies the per-plaquette Hessian eigenvalue -beta/N at U_p = -I for SU(2).
import numpy as np
from scipy.linalg import expm
s3 = np.array([[1, 0], [0, -1]], dtype=complex)
X  = 1j*s3/np.sqrt(2)                       # |X|^2 = -Tr(X^2) = 1
theta = lambda V: 1 - np.trace(V).real/2    # vartheta(V) = 1 - Re Tr V / N,  N = 2
A = -np.eye(2, dtype=complex)               # the bad plaquette holonomy U_p = -I
f = lambda t: theta(expm(t*X) @ A)
h = 1e-4
print(theta(A), (f(h) - 2*f(0) + f(-h))/h**2)      # -> 2.0 , -0.5000000  (= -1/N)
for beta in [0.2, 1/3, 0.5, 2.0, 6.0]:
    print(beta, 1 + 6*beta*(-0.5))                  # Ric_mu(U*)(X,X) = kappa_G - nu_P*beta/N

**Caveat.** Proposition 6 shows the pointwise hinge fails at a specific point of $K_\Lambda(\varepsilon)$; it does not by itself rule out a weaker, non-pointwise functional inequality on $K_\Lambda(\varepsilon)$ obtained by other means.

**Why it matters.** It converts 'the corpus silently substitutes one good set for another' from an editorial observation into a proof: the substitution is not a technical convenience but a logical error, and the explicit configuration $U^*$ exhibits it at every volume, at every $\varepsilon>0$, for every $\beta>1/3$.

---

## How these fit together

The six items form one closed chain, and they connect outward to the rest of the corpus in a specific way.

Internal logic. Item 1 (Haar link marginals) is the seed; Item 2 strengthens it from one link to the $|V|-1$ links of a spanning tree by exhibiting the tree-gauge factorization $\mu \cong \mathrm{Haar}^{\otimes(V\setminus x_0)}\otimes\nu$, which is what upgrades "$\mu(K)<1$" to "$\mu(K)=e^{-\Theta(\text{volume})}$". Item 3 supplies the single number that makes Items 1, 2 and 5 quantitative, and along the way proves (rather than assumes) Appendix A's $\kappa_G$ and evaluates $\iota_G$, $r_{\rm sf}$, $m_H^2$. Item 4 is where the obstruction lands on the corpus's actual pipeline: the localization inequality of Appendix I is the sole bridge from conditional to unconditional clustering in `Core_6`, `Core_8` and `BEST_05`, and Items 2/5 make its error term larger than the trivial bound. Item 5 covers the one good set Item 2 does not (the gauge-invariant plaquette-sup set of Core-5, which was introduced precisely to be gauge invariant and therefore immune to Item 1). Item 6 closes the last door: the only good set in the corpus with a proved typicality bound (Appendix J's averaged set) is shown by explicit counterexample not to support the hinge.

Relation to the corpus's own statements. The matrix hinge itself (`01_matrix_hinge_haar_wilson.md` Prop. 6; `A_local_BE_curvature.md` Thm. 5.4; `Core_5` Prop. Core-5.2.4) is, as a LOCAL statement, correct and worth keeping — the mechanism (product Ricci from Haar geometry + Lipschitz control of the Wilson Hessian) is sound, and `A_local_BE_curvature.md` is the most complete write-up of it. What these six items kill is only the localization/typicality step. `EXCITING_05` already contains the correct diagnosis in one sentence ("A max-event ... complement controlled only by a union bound, typically producing a factor $|P(\Lambda)|$. That factor is exactly what later poisons uniform bounds") but then proposes the averaged set as the fix, without noticing that the hinge does not survive averaging — which is exactly Item 6.

Corrections to the extract layer. `CAND-002` gives the exponent $|E|-|V|+1$; the provable exponent is $|V|-1$ (Item 2). `MG_Localization_Typicality_Unconditioning.md` §3 gives the localization constant 4; the correct sup-norm constant for that route is 6 (Appendix I's 8 is valid but lossy) — Item 4.

Relation to the neighbouring obstruction. `CAND-005` (the chessboard/tube counting obstruction, from `RICCATI/.../PROOF_13_High_Probability_Convexity`) attacks the same target from the continuum side: a small-plaquette tube in a fixed physical volume has probability going to zero as $a\to0$ because $6R^4a^{-4}$ beats $e^{-\beta c_\Phi(\delta)}$ along $\beta(a)=c\ln(1/a\Lambda)$, since $c_\Phi\le2$ while $4/c=48\pi^2/(11N^2)\approx4.8$ for $N=3$. That is the $a\to0$ version of the same phenomenon; Items 2 and 5 here are the fixed-$a$, $|\Lambda|\to\infty$ version, and are unconditional (they need no asymptotic freedom input). Read together they say: the small-field good set is atypical both in the thermodynamic limit at fixed cutoff and in the continuum limit at fixed physical volume.

Relation to the escape route. Every item is a statement about GAUGE-INVARIANT measures. The one route they do not close is passing to the gauge-fixed quotient, where the tree links are frozen by construction and Item 2's factorization is exactly what has been quotiented away. `HAAR/01_haar_mass/07_SAFE_REGION/11_haar_gauge_fixing_rigorous.md` is the corpus's only file on that route; it correctly notes that the Faddeev-Popov determinant reproduces the Haar/Vandermonde density on the Cartan, and correctly lists Gribov copies, FP-zero sets and residual holonomies as the obstacles, but supplies no quantitative slice theorem. That is where a continuation would have to start.

## Further material found but not fully extracted

Things I found in this area and did not extract fully.

1. `HAAR/01_haar_mass/01_CORE_THEOREMS/A_local_BE_curvature.md` is the single best-written mathematical file I read in this part of the corpus — 311 lines, self-contained, with real proofs (product Ricci splitting, second-order Taylor of $\Re\mathrm{Tr}(I-e^Y)$, BCH linearization of the plaquette holonomy giving $\nabla^2S_W(U^{(0)})=\frac\beta N d_1^*d_1$, uniform third-derivative bound with the $\nu^{3/2}$ triple-Cauchy-Schwarz factor, and the resulting $r=\min\{1,\rho_0/(2L_W)\}$, $\rho_{\rm loc}=\rho_0/2$). Its Theorem 5.4 is stated on a geodesic ball $B_r(U^{(0)})$ in the PRODUCT metric, which is far smaller than the linkwise set $K_\Lambda(r)$ (it forces $\sum_\ell d(U_\ell,e)^2\le r^2$, i.e. per-link radius $r/\sqrt{|E|}$), so the obstruction bites even harder there — worth extracting as its own item.

2. `WILSON/archive/Appendix_J__Typicality_Mechanism_for_K(1).md` contains a fully correct and quite pretty self-contained proof of the averaged-set typicality bound: subadditivity of $d_G$ under multiplication proved from scratch via path concatenation, the plaquette displacement bound $d(U_p,\mathbf 1)\le m_\partial r$, the partition-function lower bound $Z\ge e^{-\beta L_\vartheta m_\partial r|P|}\mathrm{vol}(B_r)^{|E|}$, and the reduction of the mixed $|E|/|P|$ exponent to a pure $|P|$ exponent via $c_{E:P}=2/3$. It deserves extraction on its own merits as a correct theorem (about the wrong set).

3. The $\beta$-independence strand of `CAND-006`: because $\kappa_G=N/2$ is independent of $\beta$ and of the lattice spacing $a$, any completed hinge chain would give a lattice-unit gap $m_{\rm eff}=\sqrt{c_H/2}$ uniform in $\beta$, hence a physical gap $m_{\rm eff}/a\to\infty$ as $a\to0$. I did not extract this because it is a separate obstruction (continuum limit, not typicality), but with $\kappa_G=N/2$ now proved (Item 3) the arithmetic is immediate and it would make a clean companion item.

4. `HELFFER_SJOSTRAND/04_Decay_Localization_OS/Core_6__Conditional_Covariance_Bound_via_HS_and_Hinge.md` and `BEST_05_Lattice_Mass_Gap_Pipeline_from_Hinge_to_OS.md` are the downstream consumers; I read enough to locate where $\mu(K^c)$ enters but did not audit the Helffer-Sjöstrand order-comparison step (Appendix F, Prop. F.15) or the reflecting-diffusion External Input F.20, which Core-5.1.4 flags as needed on the corner-boundaried domain $\mathcal K$.

5. `HAAR/01_haar_mass/07_SAFE_REGION/11_haar_gauge_fixing_rigorous.md` states the one defensible gauge-fixed claim ("inside a gauge slice where the FP determinant is bounded away from zero and infinity, the gauge-fixed measure is absolutely continuous w.r.t. product Haar with a smooth density"). Quantifying the "bounded away from zero" on a slice of growing volume is the natural next question the obstruction raises, and nothing in the corpus addresses it.

6. Duplication note: `MG_Localization_Typicality_Unconditioning.md` exists byte-identically in `HELFFER_SJOSTRAND/04_Decay_Localization_OS/`, `COMBES_THOMAS/CORE_THEORY/` and `LSI_POINCARE/08_misc_docs/`; `3_fixed_cutoff_mass_gap_su2.md` in five places; `Appendix_I`/`Appendix_J` survive only in `LSI_POINCARE/archive/` and `WILSON/archive/` respectively (the non-archive copies appear to have been deleted), so those archive paths are the canonical ones.
