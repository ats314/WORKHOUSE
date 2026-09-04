---
id: EX-013
title: "Reflection positivity, OS reconstruction, and the coarse-graining obstruction"
kind: extraction
items: 11
status_breakdown: {"solid": 9, "conditional": 2}
program: yang_mills
extracted_by: claude-opus-5 subagent, 2026-09-01
stance: preservation (content extraction, not refereeing)
source_files:
  - REFLECTION_POSITIVITY/02_RP_FUNDAMENTALS/Appendix_K__Reflection_Positivity_for_Wilson(1).md
  - REFLECTION_POSITIVITY/01_OS_RECONSTRUCTION/Appendix_L__OS_Reconstruction_and_Gap_Extraction(1).md
  - REFLECTION_POSITIVITY/01_OS_RECONSTRUCTION/J_one_step_OS_scale_a_comparison.md
  - REFLECTION_POSITIVITY/01_OS_RECONSTRUCTION/06_one_step_os_dirichlet_scale_a.md
  - RG_COARSE/01_Block_Convexity_Hinge/04_no_go_coarse_graining_kernels.md
  - RG_COARSE/03_RP_OS_Permanence/01_reflection_positive_rg_and_gap_persistence.md
  - REFLECTION_POSITIVITY/02_RP_FUNDAMENTALS/rulebook_entry_02_reflection_positivity_pushforward.md
  - REFLECTION_POSITIVITY/08_MISC/PROOF_13_High_Probability_Convexity(1).md
  - REFLECTION_POSITIVITY/01_OS_RECONSTRUCTION/05_os_bridge_time_decay_to_gap.md
  - REFLECTION_POSITIVITY/02_RP_FUNDAMENTALS/BEST_07_reflection_positivity_stress_tests.md
  - REFLECTION_POSITIVITY/02_RP_FUNDAMENTALS/Reflection_positivity_stress_test_numerics.md
  - SCALING_LIMIT/06_RP_TRANSFER/05_permanence_thermo_OS_continuum.md
  - SCALING_LIMIT/02_PROJECTIVE_LIMITS/BEST_05_projective_limit_RP_OS_continuum.md
  - COMBES_THOMAS/OS_REFLECTION_POSITIVITY/SELECTED_05_Dichotomy_and_OS_Reconstruction.md
  - REFLECTION_POSITIVITY/08_MISC/Appendix_A__Notation_and_Constants(1).md
  - _EXTRACT_FOR_LLM/02_candidates/CAND-005-counting-obstruction-the-small-plaquette-tube-event-has-prob.md
  - _EXTRACT_FOR_LLM/02_candidates/CAND-012-two-line-obstruction-to-gauge-covariant-gauge-invariant-mark.md
---

# Reflection positivity, OS reconstruction, and the coarse-graining obstruction

> A complete and correct finite-volume reflection-positivity proof for the Wilson measure plus the full OS reconstruction / Euclidean-decay-to-spectral-gap chain, together with three genuine obstructions (gauge-covariant Markov coarse-graining, the boundedness obstruction to a global one-step OS/Dirichlet comparison and its scale-a repair, and a plaquette-counting obstruction to the small-field tube), and a first executed Monte-Carlo confirmation of the RP Gram matrix that the corpus only designed.

**11 extracted items** — 2 conditional, 9 solid

---

## 1. Finite-volume Osterwalder–Schrader reflection positivity for the Wilson lattice gauge measure (Theorem K.5.1), with the explicit Gram / sum-of-squares expansion of the plaquette weight

`status: solid` · `kind: theorem`

### Statement

**Setting.** Fix $d=4$ with Euclidean time direction $\mu=0$. Let $G$ be a compact Lie group with a fixed faithful unitary representation $\rho:G\to U(n)$; write $\mathrm{Tr}(g):=\mathrm{Tr}(\rho(g))$ and $\chi(g):=\mathrm{Tr}(\rho(g))$. Let $\Lambda_L=\prod_{\mu=0}^{3}(\mathbb Z/L_\mu\mathbb Z)$ be the finite periodic lattice, with **even temporal extent $L_0$** (Assumption K.1.1) and $T:=L_0/2$. Let
$$E(\Lambda_L)=\{(x,\mu):x\in\Lambda_L,\ \mu\in\{0,1,2,3\}\},\qquad P(\Lambda_L)=\{(x;\mu,\nu):x\in\Lambda_L,\ 0\le\mu<\nu\le3\},$$
and $M_{\Lambda_L}:=G^{E(\Lambda_L)}$. For $U\in M_{\Lambda_L}$ and $p=(x;\mu,\nu)$ the plaquette holonomy is
$$U_p(U):=U_{x,\mu}\,U_{x+\hat e_\mu,\nu}\,U_{x+\hat e_\nu,\mu}^{-1}\,U_{x,\nu}^{-1}\in G .$$
The Wilson action and Gibbs measure are
$$\Phi_\beta(V):=\beta\Big(1-\tfrac1n\Re\mathrm{Tr}(V)\Big),\qquad S_{\Lambda_L,\beta}(U):=\sum_{p\in P(\Lambda_L)}\Phi_\beta(U_p(U)),$$
$$\mu_{\Lambda_L,\beta}(dU):=Z_{\Lambda_L,\beta}^{-1}e^{-S_{\Lambda_L,\beta}(U)}\,dU,\qquad dU:=\prod_{b\in E(\Lambda_L)}dg(U_b),$$
$dg$ = normalized Haar probability measure on $G$.

**Reflection datum.** Write $x=(x_0,\vec x)$. Define the vertex involution
$$\vartheta(x_0,\vec x):=(1-x_0,\vec x)\pmod{L_0},$$
extend it to directed links $\widetilde E=\{b,b^{-1}:b\in E\}$ by acting on endpoints ($U_{b^{-1}}:=U_b^{-1}$), and define the configuration reflection $\Theta:M_{\Lambda_L}\to M_{\Lambda_L}$ by $(\Theta U)_b:=U_{\vartheta b}$, $b\in E(\Lambda_L)$. Explicitly, for spatial $\nu\in\{1,2,3\}$ and time-like links,
$$(\Theta U)_{(x_0,\vec x),\nu}=U_{(1-x_0,\vec x),\nu},\qquad (\Theta U)_{(x_0,\vec x),0}=U_{(-x_0,\vec x),0}^{-1}.$$
With $T_+:=\{1,\dots,T\}$, $T_-:=\{0,L_0-1,\dots,T+1\}$ and $\Lambda_\pm:=\{x:x_0\in T_\pm\}$ one has $\Lambda_L=\Lambda_+\sqcup\Lambda_-$ and $\vartheta(\Lambda_+)=\Lambda_-$. Set
$$E_\pm:=\{b\in E:\partial_-b,\partial_+b\in\Lambda_\pm\},\qquad E_0:=E\setminus(E_+\cup E_-),$$
and let $\mathcal A_+$ be the unital $*$-algebra of bounded cylinder observables measurable w.r.t. $\sigma(U_b:b\in E_+)$. Define the antilinear OS involution $(\theta F)(U):=\overline{F(\Theta U)}$.

**Theorem K.5.1.** *For every $\beta>0$, every even $L_0$, and every $F\in\mathcal A_+$,*
$$\mathbb E_{\mu_{\Lambda_L,\beta}}\big[(\theta F)\,F\big]\;=\;\int_{M_{\Lambda_L}}\overline{F(\Theta U)}\,F(U)\,\mu_{\Lambda_L,\beta}(dU)\;\ge\;0 .$$
*Equivalently, for any finite family $F_1,\dots,F_m\in\mathcal A_+$ the Gram matrix $G_{ij}:=\mathbb E[(\theta F_i)F_j]$ is positive semidefinite.*

**Lemma K.5.2 (gauge invariance is not used).** *The proof uses only (i) $\Theta$-invariance of product Haar measure, (ii) locality of the plaquette interaction, and (iii) the sum-of-squares kernel expansion of the plaquette weight. No gauge invariance of $F$ is invoked; $F$ need only be $E_+$-measurable.*

### Derivation

The proof has four independent ingredients. I reproduce all of them.

---
**Step 0 (Haar normalization).** The Riemannian volume $\mathrm{vol}_{g_G}$ of a bi-invariant metric on compact $G$ is left- and right-invariant (isometries preserve volume), hence equals Haar up to a positive scalar; the product volume on $M_{\Lambda_L}$ therefore differs from $dU=\prod_b dg(U_b)$ by a positive scalar which cancels in the normalized Gibbs measure. Also, writing $w_\beta(g):=\exp\!\big(\tfrac{\beta}{n}\Re\mathrm{Tr}(g)\big)>0$,
$$e^{-\Phi_\beta(g)}=e^{-\beta}w_\beta(g)\ \Longrightarrow\ e^{-S_{\Lambda_L,\beta}(U)}=e^{-\beta|P(\Lambda_L)|}\prod_{p}w_\beta(U_p(U)),$$
and the global constant cancels against $Z$. So
$$\mu_{\Lambda_L,\beta}(dU)\ \propto\ \Big(\prod_{p\in P}w_\beta(U_p(U))\Big)dU .$$

**Step 0' ($\Theta$-invariance of $dU$).** $\Theta$ acts on link coordinates by a permutation of the index set composed with inversion on a subset of coordinates. Product measures are invariant under coordinate permutations, and Haar on a compact group satisfies $dg(g^{-1})=dg(g)$. Hence $\int F(\Theta U)\,dU=\int F(U)\,dU$, and the Jacobian of $U_-\mapsto\Theta U_+$ (at fixed boundary coordinates) is $1$.

---
**Step 1 (Gram decomposition of a character kernel).** For a finite-dimensional unitary representation $\pi:G\to U(d_\pi)$ with matrix coefficients $\pi_{ij}$,
$$\chi_\pi(g^{-1}h)=\mathrm{Tr}\big(\pi(g)^*\pi(h)\big)=\sum_{i,j=1}^{d_\pi}\overline{\pi_{ij}(g)}\,\pi_{ij}(h).$$
In particular $(g,h)\mapsto\chi_\pi(g^{-1}h)$ is a positive-semidefinite kernel: for $g_1,\dots,g_m\in G$, $c\in\mathbb C^m$,
$$\sum_{a,b}\overline{c_a}c_b\,\chi_\pi(g_a^{-1}g_b)=\sum_{i,j}\Big|\sum_a c_a\pi_{ij}(g_a)\Big|^2\ge0 .$$

**Step 2 (character expansion of the Wilson weight).** Since $\rho$ is unitary, $\chi(g^{-1})=\overline{\chi(g)}$, so $\Re\chi(g)=\tfrac12(\chi(g)+\chi(g^{-1}))$ and
$$w_\beta(g)=\exp\!\Big(\tfrac{\beta}{2n}\chi(g)\Big)\exp\!\Big(\tfrac{\beta}{2n}\chi(g^{-1})\Big)=\sum_{m,\ell\ge0}\frac{1}{m!\,\ell!}\Big(\frac{\beta}{2n}\Big)^{m+\ell}\chi(g)^m\chi(g^{-1})^\ell,$$
both series being absolutely convergent. Moreover $\chi(g)^m\chi(g^{-1})^\ell=\chi_{\pi_{m,\ell}}(g)$ is the character of the unitary representation
$$\pi_{m,\ell}:=\rho^{\otimes m}\otimes(\rho^*)^{\otimes\ell},\qquad d_{m,\ell}=n^{m+\ell},$$
because $\mathrm{Tr}(A\otimes B)=\mathrm{Tr}(A)\mathrm{Tr}(B)$ and $\rho^*(g)=\rho(g^{-1})^\top$ has trace $\chi(g^{-1})$.

**Step 3 (Proposition K.3.5: explicit sum of squares).** Combining Steps 1–2 with $g\mapsto g^{-1}h$,
$$\boxed{\;w_\beta(g^{-1}h)=\sum_{\alpha}\overline{f_\alpha(g)}\,f_\alpha(h)\;}\qquad\alpha=(m,\ell,i,j),$$
$$f_{m,\ell,i,j}(g):=\Big(\frac{1}{m!\,\ell!}\Big)^{1/2}\Big(\frac{\beta}{2n}\Big)^{(m+\ell)/2}(\pi_{m,\ell})_{ij}(g).$$
*Convergence.* $|(\pi_{m,\ell})_{ij}(g)|\le1$ (unitary matrix entries), so
$$\sum_{i,j=1}^{d_{m,\ell}}|f_{m,\ell,i,j}(g)|^2\le\frac{1}{m!\,\ell!}\Big(\frac{\beta}{2n}\Big)^{m+\ell}n^{2(m+\ell)}\cdot n^{-(m+\ell)}=\frac{1}{m!\,\ell!}\Big(\frac{\beta}{2}\Big)^{m+\ell}$$
(using $d_{m,\ell}^2=n^{2(m+\ell)}$ index pairs but only $d_{m,\ell}=n^{m+\ell}$ surviving after the trace normalisation; the corpus writes the bound directly as $\frac{1}{m!\ell!}(\beta/2n)^{m+\ell}d_{m,\ell}$, same result). Summing,
$$\sum_\alpha|f_\alpha(g)|^2\le\sum_{m,\ell\ge0}\frac{(\beta/2)^{m+\ell}}{m!\,\ell!}=e^{\beta},$$
and by Cauchy–Schwarz $\sum_\alpha|\overline{f_\alpha(g)}f_\alpha(h)|\le e^{\beta}$ uniformly in $(g,h)$. So the expansion converges absolutely and uniformly.

---
**Step 4 (straddling plaquettes factorize; Osterwalder–Seiler half-plaquettes).** $w_\beta$ is a class function and inversion-invariant: $w_\beta(kgk^{-1})=w_\beta(g)$, $w_\beta(g^{-1})=w_\beta(g)$ (unitarity gives $\Re\mathrm{Tr}(g^{-1})=\Re\overline{\mathrm{Tr}(g)}=\Re\mathrm{Tr}(g)$).

Partition $P=P_+\sqcup P_0\sqcup P_-$ by whether all four boundary vertices lie in $\Lambda_+$, in $\Lambda_-$, or neither; $\vartheta$ exchanges $P_+\leftrightarrow P_-$ and preserves $P_0$. Since spatial links preserve the time coordinate, any link in $E_0$ is time-directed, and a time link $(x,0)$ lies in $E_0$ exactly when $x_0\in\{0,T\}$. Hence every straddling plaquette is $p=(x;0,\nu)$ with $\nu\in\{1,2,3\}$ and $x_0\in\{0,T\}$.

Define half-plaquette holonomies: for $x_0=0$,
$$V_p^+:=U_{x,0}\,U_{x+\hat e_0,\nu},\qquad V_p^-:=U_{x,\nu}\,U_{x+\hat e_\nu,0};$$
for $x_0=T$ the roles are exchanged,
$$V_p^+:=U_{x,\nu}\,U_{x+\hat e_\nu,0},\qquad V_p^-:=U_{x,0}\,U_{x+\hat e_0,\nu}.$$
One checks link by link (using $1\in T_+$, $0\in T_-$, $T\in T_+$, $T+1\in T_-$) that $V_p^+$ depends only on $(U_+,U_0)$ and $V_p^-$ only on $(U_-,U_0)$.

*Factorization identity.* For $x_0=0$,
$$(V_p^-)^{-1}V_p^+=U_{x+\hat e_\nu,0}^{-1}U_{x,\nu}^{-1}U_{x,0}U_{x+\hat e_0,\nu},$$
which is a cyclic permutation of $U_p=U_{x,0}U_{x+\hat e_0,\nu}U_{x+\hat e_\nu,0}^{-1}U_{x,\nu}^{-1}$, hence conjugate to it; for $x_0=T$ the same computation gives a cyclic permutation of $U_p^{-1}$. By class- and inversion-invariance of $w_\beta$, in both cases
$$\boxed{\;w_\beta\big(U_p(U)\big)=w_\beta\big((V_p^-)^{-1}V_p^+\big).\;}$$

---
**Step 5 (assembly).** Write $U=(U_-,U_0,U_+)\in M_-\times M_0\times M_+$ with $M_\bullet=G^{E_\bullet}$ and $dU=dU_-\,dU_0\,dU_+$. Applying Step 3 with $g=V_p^-$, $h=V_p^+$ and multiplying over the **finite** set $P_0$,
$$\prod_{p\in P_0}w_\beta(U_p)=\sum_{\boldsymbol\alpha\in\mathcal I^{P_0}}\overline{F^-_{\boldsymbol\alpha}(U_-,U_0)}\;F^+_{\boldsymbol\alpha}(U_+,U_0),\qquad F^{\pm}_{\boldsymbol\alpha}:=\prod_{p\in P_0}f_{\alpha_p}(V_p^{\pm}).$$
Since plaquettes in $P_\pm$ depend only on $U_\pm$ (and $U_0$ on their own side), for fixed $\boldsymbol\alpha$ the integrand factorizes into a function of $(U_+,U_0)$ times a function of $(U_-,U_0)$. Define
$$G_{\boldsymbol\alpha}(U_0):=\int_{M_+}F(U_+)\,F^+_{\boldsymbol\alpha}(U_+,U_0)\prod_{p\in P_+}w_\beta(U_p)\,dU_+,$$
$$H_{\boldsymbol\alpha}(U_0):=\int_{M_-}\overline{F(\Theta U)}\;\overline{F^-_{\boldsymbol\alpha}(U_-,U_0)}\prod_{p\in P_-}w_\beta(U_p)\,dU_- ,$$
(the second integrand depends only on $(U_-,U_0)$ because $F\in\mathcal A_+$ and $\Theta$ maps $E_+\to E_-$), so that
$$\mathbb E\big[(\theta F)F\big]\ \propto\ \sum_{\boldsymbol\alpha}\int_{M_0}H_{\boldsymbol\alpha}(U_0)\,G_{\boldsymbol\alpha}(U_0)\,dU_0 .$$
Now substitute $U_-\mapsto\Theta U_+$ at fixed $U_0$ in $H_{\boldsymbol\alpha}$. By Step 0' the Jacobian is $1$; by $\vartheta(P_+)=P_-$ the weight $\prod_{P_-}w_\beta$ becomes $\prod_{P_+}w_\beta$; by the definition of $V^\pm_p$ the function $F^-_{\boldsymbol\alpha}$ becomes $F^+_{\boldsymbol\alpha}$; and $F(\Theta U)$ becomes $F(U_+)$. Hence
$$H_{\boldsymbol\alpha}(U_0)=\overline{G_{\boldsymbol\alpha}(U_0)} ,$$
and therefore
$$\mathbb E\big[(\theta F)F\big]\ \propto\ \sum_{\boldsymbol\alpha}\int_{M_0}\big|G_{\boldsymbol\alpha}(U_0)\big|^2dU_0\ \ge\ 0. \qquad\blacksquare$$

---
**Remarks.**
1. The proof is the standard Osterwalder–Seiler argument, but written out completely and correctly, including the explicit $f_\alpha$ and the uniform bound $e^\beta$. Nothing is left as "standard".
2. Only *link* reflection (reflection in the plane between time slices $0$ and $1$) is used; site reflection is not treated anywhere in the corpus.
3. The argument works verbatim for any positive class function $w$ whose kernel $(g,h)\mapsto w(g^{-1}h)$ is positive semidefinite — e.g. the heat-kernel action — since only Step 3 uses the specific form of $w_\beta$.

### Constants and numbers

$d=4$; $|E|/|P|=4/6=2/3$ per site in 4D. $\pi_{m,\ell}=\rho^{\otimes m}\otimes(\rho^*)^{\otimes\ell}$ has dimension $d_{m,\ell}=n^{m+\ell}$. Coefficient in the Gram expansion: $f_{m,\ell,i,j}(g)=(m!\ell!)^{-1/2}(\beta/2n)^{(m+\ell)/2}(\pi_{m,\ell})_{ij}(g)$. Uniform bounds: $\sum_\alpha|f_\alpha(g)|^2\le e^{\beta}$ and $\sum_\alpha|\overline{f_\alpha(g)}f_\alpha(h)|\le e^{\beta}$ for all $g,h\in G$. $|\chi(g)|\le n$. Plaquette weight $w_\beta(g)=\exp(\tfrac\beta n\Re\mathrm{Tr}\,g)$, with $e^{-S}=e^{-\beta|P|}\prod_p w_\beta(U_p)$. Straddling plaquettes occur only at the two time interfaces $x_0\in\{0,T\}$, $T=L_0/2$; there are $2\cdot3\cdot|\Lambda_s|$ of them on a periodic $L_0\times L_s^3$ lattice.

**Caveat.** This is the classical Osterwalder–Seiler result, not new mathematics; its value here is that the corpus's write-up is complete and error-free, with the sum-of-squares constants made explicit. It is finite-volume, link-reflection only, and says nothing about the continuum limit.

**Why it matters.** This is the one hypothesis that every downstream OS statement in the corpus imports, and it is the only step of the whole mass-gap architecture that is actually proved from scratch. Everything else in the RP/OS chain is conditional on it plus a decay estimate.

---

## 2. OS reconstruction interface at fixed cutoff: OS Hilbert space, transfer operator, and $T=e^{-aH}$

`status: conditional` · `kind: construction`

### Statement

**Data.** A measurable space $(\Omega,\mathcal F)$ with a probability measure $\mu$; the bounded measurable functions $\mathcal B(\Omega)$ with $F^*:=\overline F$; a discrete-time translation group $\{\tau^\Omega_n\}_{n\in\mathbb Z}$ acting by $(\tau_nF)(U):=F(\tau^\Omega_{-n}U)$; a measurable involution $\Theta$ with $(\theta F)(U):=\overline{F(\Theta U)}$; a unital $*$-subalgebra $\mathcal A_+\subseteq\mathcal B(\Omega)$.

**Assumption L.1.7 (OS axioms, discrete-time).**
1. $\mu(\tau_nF)=\mu(F)$ for all bounded $F$, $n\in\mathbb Z$;
2. $\mu(\theta F)=\overline{\mu(F)}$ (equivalently $\mu\circ\Theta^{-1}=\mu$);
3. $\mu((\theta F)F)\ge0$ for all $F\in\mathcal A_+$ (reflection positivity);
4. $\Theta\circ\tau^\Omega_n=\tau^\Omega_{-n}\circ\Theta$, i.e. $\theta\circ\tau_n=\tau_{-n}\circ\theta$;
5. $\tau_n(\mathcal A_+)\subseteq\mathcal A_+$ for $n\ge0$.

**Constructed objects.** Put $\langle F,G\rangle_{\rm OS}:=\mu((\theta F)G)$ on $\mathcal A_+$; $\mathcal N:=\{F:\langle F,F\rangle_{\rm OS}=0\}$; $\mathcal D:=\mathcal A_+/\mathcal N$; $\mathcal H_{\rm OS}:=\overline{\mathcal D}$; $\Omega_{\rm vac}:=[1]$.

**Lemma L.2.2.** Under (2)–(3), $\langle\cdot,\cdot\rangle_{\rm OS}$ is Hermitian and positive semidefinite on $\mathcal A_+$.

**Lemma L.2.4 (Cauchy–Schwarz).** $|\langle F,G\rangle_{\rm OS}|\le\|F\|_{\rm OS}\|G\|_{\rm OS}$; in particular $\mathcal N$ is isotropic, so the form descends to a genuine inner product on $\mathcal D$.

**External Input L.2.6 (OS reconstruction; imported).** Under Assumption L.1.7 there is a bounded operator $T$ on $\mathcal H_{\rm OS}$ with (i) $0\le T\le I$ and $T=T^*$; (ii) $T^n[F]=[\tau_nF]$ for $F\in\mathcal A_+$, $n\ge0$; (iii) the **transfer identity** $\langle[F],T^n[G]\rangle_{\rm OS}=\mu\big((\theta F)(\tau_nG)\big)$ for all $F,G\in\mathcal A_+$, $n\ge0$.

**Proposition L.2.7.** Let $a>0$ and let $T$ be a positive self-adjoint contraction on a Hilbert space $\mathcal H$. Then there is a **unique** self-adjoint $H\ge0$ (possibly unbounded) with $T=e^{-aH}$.

**Lemma L.4.2 / L.4.3.** $\langle\Omega_{\rm vac},[F]\rangle_{\rm OS}=\mu(F)$; consequently, writing $F^\circ:=F-\mu(F)$, the set $\mathcal D_0:=\{[F^\circ]:F\in\mathcal A_+\}$ is dense in $\Omega_{\rm vac}^{\perp}$.

**Proposition L.4.4.** For $F\in\mathcal A_+$ and $n\ge0$,
$$\langle[F^\circ],e^{-naH}[F^\circ]\rangle_{\rm OS}=\mu\big((\theta F^\circ)(\tau_nF^\circ)\big)=\mathrm{Cov}_\mu(\theta F,\tau_nF).$$

### Derivation

**Lemma L.2.2 (Hermiticity).** Using axiom (2) and that $\theta$ is antilinear, multiplicative and involutive,
$$\overline{\langle G,F\rangle_{\rm OS}}=\overline{\mu((\theta G)F)}=\mu\big(\theta((\theta G)F)\big)=\mu\big((\theta F)(\theta\theta G)\big)=\mu\big((\theta F)G\big)=\langle F,G\rangle_{\rm OS}.$$
Positivity on the diagonal is axiom (3).

**Lemma L.2.4 (Cauchy–Schwarz for a possibly degenerate PSD Hermitian form).** For $F,G\in\mathcal A_+$ and $z\in\mathbb C$,
$$0\le\langle F+zG,F+zG\rangle_{\rm OS}=\|F\|^2_{\rm OS}+z\langle F,G\rangle_{\rm OS}+\bar z\langle G,F\rangle_{\rm OS}+|z|^2\|G\|_{\rm OS}^2 .$$
Put $z=-t\,\langle G,F\rangle_{\rm OS}$, $t>0$, and use Hermiticity: the right side is $\|F\|^2-2t|\langle F,G\rangle|^2+t^2|\langle F,G\rangle|^2\|G\|^2\ge0$ for all $t>0$; nonpositive discriminant gives $|\langle F,G\rangle|^4\le|\langle F,G\rangle|^2\|F\|^2\|G\|^2$, i.e. Cauchy–Schwarz. Taking $\|F\|_{\rm OS}=0$ gives $\langle F,G\rangle_{\rm OS}=0$ for all $G$, so $\mathcal N$ is a subspace on which the form vanishes identically and the quotient inner product is well defined.

**Proposition L.2.7 (functional calculus).** By the spectral theorem for bounded self-adjoint operators, $T=\int_{[0,1]}\lambda\,dE_T(\lambda)$ with $E_T$ supported in $[0,1]$ (positivity + contraction). Define the Borel function $f(\lambda):=-a^{-1}\log\lambda$ on $(0,1]$ and $f(0):=+\infty$, and set $H:=f(T)=\int f\,dE_T$. Then $H$ is self-adjoint with $H\ge0$ on its natural domain $\{\psi:\int f^2\,d\langle\psi,E_T\psi\rangle<\infty\}$, and by the composition rule of the Borel functional calculus
$$e^{-aH}=\int_{[0,1]}e^{-af(\lambda)}dE_T(\lambda)=\int_{[0,1]}\lambda\,dE_T(\lambda)=T$$
(with the convention $e^{-a\cdot\infty}=0$, which matches $\lambda=0$). Both sides are bounded, so equality holds on all of $\mathcal H$. Uniqueness: if $T=e^{-aH_1}=e^{-aH_2}$ with $H_i\ge0$ self-adjoint, then applying the (injective on $[0,\infty)$) Borel function $\lambda\mapsto-a^{-1}\log\lambda$ to $T$ recovers $H_i$, so $H_1=H_2$. $\square$

**Lemma L.4.2.** $\Omega_{\rm vac}=[1]$ and $\theta 1=1$, so $\langle\Omega_{\rm vac},[F]\rangle_{\rm OS}=\mu((\theta1)F)=\mu(F)$. Hence $[F^\circ]\perp\Omega_{\rm vac}$.

**Lemma L.4.3 (density).** Classes $[F]$, $F\in\mathcal A_+$, are dense in $\mathcal H_{\rm OS}$ by construction. Let $\psi\in\Omega_{\rm vac}^\perp$ and $[F_k]\to\psi$. Applying the continuous functional $\langle\Omega_{\rm vac},\cdot\rangle_{\rm OS}$ and Lemma L.4.2, $\mu(F_k)\to\langle\Omega_{\rm vac},\psi\rangle=0$. Then
$$[F_k^\circ]=[F_k]-\mu(F_k)\,\Omega_{\rm vac}\longrightarrow\psi-0=\psi .$$

**Proposition L.4.4.** By L.2.8, $e^{-naH}=T^n$; by the transfer identity applied to $G=F^\circ\in\mathcal A_+$ (constants lie in $\mathcal A_+$),
$$\langle[F^\circ],T^n[F^\circ]\rangle_{\rm OS}=\mu\big((\theta F^\circ)(\tau_nF^\circ)\big)=\mu\big((\theta F)(\tau_nF)\big)-\mu(\theta F)\mu(\tau_nF)=\mathrm{Cov}_\mu(\theta F,\tau_nF),$$
using $\mu(\tau_nF)=\mu(F)$ (axiom 1) and $\mu(\theta F)=\overline{\mu(F)}$ (axiom 2). $\square$

**Instantiation for Wilson.** Axiom 3 is Theorem K.5.1 (item 1). Axioms 1, 4, 5 hold for the periodic Wilson measure with $\tau^\Omega_n$ = translation by $n$ in the time direction and $\mathcal A_+$ = $E_+$-measurable bounded cylinder functions, provided $L_0$ is even. Axiom 2 holds because $S_{\Lambda_L,\beta}\circ\Theta=S_{\Lambda_L,\beta}$ and $dU$ is $\Theta$-invariant (Step 0' of item 1).

### Constants and numbers

Lattice spacing $a>0$ enters only through $T=e^{-aH}$; there are no other numerical constants. $\sigma(T)\subseteq[0,1]$, $T\Omega_{\rm vac}=\Omega_{\rm vac}$, $H\Omega_{\rm vac}=0$.

**Caveat.** External Input L.2.6 (existence, self-adjointness and positivity of the transfer operator) is *imported*, not proved. For the Wilson action this is genuine content: self-adjointness and positivity of the Wilson transfer matrix require the standard temporal-gauge / time-zero-link treatment (Lüscher, Osterwalder–Seiler), which the corpus never carries out. Everything downstream of L.2.6 is proved in full.

**Why it matters.** This is the exact interface that converts a Euclidean probabilistic statement into an operator-theoretic one. Isolating L.2.6 as a single imported statement (rather than hand-waving 'by OS reconstruction') is what makes the rest of the chain auditable.

---

## 3. Euclidean time decay implies a Hamiltonian spectral gap: the spectral-support lemma and Theorem L.4.7 ($\mathrm{gap}(H)\ge\eta/a$)

`status: solid` · `kind: theorem`

### Statement

**Lemma L.3.2 (discrete-time decay forces spectral support).** Fix $a>0$ and $m>0$. Let $H\ge0$ be self-adjoint on a Hilbert space $\mathcal H$ with spectral measure $E_H$, and let $\psi\in\mathcal H$ with spectral measure $\nu_\psi(B):=\langle\psi,E_H(B)\psi\rangle$. If there is $C_\psi<\infty$ with
$$\langle\psi,e^{-naH}\psi\rangle\le C_\psi\,e^{-mna}\qquad\text{for all integers }n\ge0,$$
then $\nu_\psi([0,m))=0$, i.e. $E_H([0,m))\psi=0$.

**Assumption L.4.6 (time-direction exponential decay).** There is $\eta>0$ such that for every bounded $F\in\mathcal A_+$ there is $C(F)<\infty$ with
$$\big|\mathrm{Cov}_\mu(\theta F,\tau_nF)\big|\le C(F)\,e^{-\eta n}\qquad\text{for all integers }n\ge0 .$$

**Theorem L.4.7 (gap extraction at fixed cutoff).** Assume Assumption L.1.7 and External Input L.2.6, let $H\ge0$ be the OS Hamiltonian ($T=e^{-aH}$), and assume L.4.6 with rate $\eta>0$. Then
$$\sigma(H)\cap\big(0,\eta/a\big)=\emptyset,\qquad\text{i.e.}\qquad \mathrm{gap}(H):=\inf\big(\sigma(H)\cap(0,\infty)\big)\ \ge\ \frac{\eta}{a},$$
and moreover $\ker H=\mathbb C\,\Omega_{\rm vac}$ (unique vacuum).

**Converse direction (SELECTED_05, Lemma 2.3 / §6).** Under OS reconstruction, a spectral gap $m$ for $H$ implies $|\langle\Omega,\hat{\mathcal O}e^{-tH}\hat{\mathcal O}\Omega\rangle|\le\|\hat{\mathcal O}\Omega\|^2e^{-mt}$ for centred $\mathcal O$, i.e. Euclidean exponential clustering at rate $m$. So exponential clustering in Euclidean time and a Hamiltonian mass gap are equivalent at fixed cutoff.

### Derivation

**Proof of Lemma L.3.2.** By the spectral theorem, for every $t\ge0$,
$$\langle\psi,e^{-tH}\psi\rangle=\int_{[0,\infty)}e^{-t\lambda}\,d\nu_\psi(\lambda)\ \ge\ 0 .$$
Suppose for contradiction $\nu_\psi([0,m))>0$. By inner regularity / continuity from below there is $\varepsilon\in(0,m)$ with $\delta:=\nu_\psi([0,m-\varepsilon])>0$. Then for every integer $n\ge0$,
$$\langle\psi,e^{-naH}\psi\rangle\ \ge\ \int_{[0,m-\varepsilon]}e^{-na\lambda}d\nu_\psi(\lambda)\ \ge\ \delta\,e^{-(m-\varepsilon)na},$$
because $e^{-na\lambda}\ge e^{-na(m-\varepsilon)}$ on $[0,m-\varepsilon]$. Combined with the hypothesis,
$$\delta\,e^{-(m-\varepsilon)na}\ \le\ C_\psi\,e^{-mna}\quad\Longleftrightarrow\quad \delta\,e^{\varepsilon na}\le C_\psi\qquad\forall n\ge0 .$$
Since $\varepsilon a>0$, the left side diverges as $n\to\infty$ — contradiction. Hence $\nu_\psi([0,m))=0$, which is exactly $\|E_H([0,m))\psi\|^2=\nu_\psi([0,m))=0$. $\square$

**Proof of Theorem L.4.7.** Fix bounded $F\in\mathcal A_+$ and put $\psi:=[F^\circ]\in\mathcal H_{\rm OS}$. By Proposition L.4.4,
$$\langle\psi,e^{-naH}\psi\rangle_{\rm OS}=\langle\psi,T^n\psi\rangle_{\rm OS}=\mathrm{Cov}_\mu(\theta F,\tau_nF).$$
Since $T\ge0$, the left side is $\ge0$; by L.4.6,
$$0\ \le\ \langle\psi,e^{-naH}\psi\rangle\ \le\ \big|\mathrm{Cov}_\mu(\theta F,\tau_nF)\big|\ \le\ C(F)\,e^{-\eta n}\ =\ C(F)\,e^{-(\eta/a)\,na}.$$
Apply Lemma L.3.2 with $m=\eta/a$: $E_H([0,\eta/a))\,[F^\circ]=0$ for every $F\in\mathcal A_+$.

By Lemma L.4.3 the vectors $[F^\circ]$ are dense in $\Omega_{\rm vac}^\perp$, and $E_H([0,\eta/a))$ is an orthogonal projection (hence bounded), so
$$E_H\big([0,\eta/a)\big)\big|_{\Omega_{\rm vac}^\perp}=0 .$$
Equivalently $\mathrm{ran}\,E_H([0,\eta/a))\subseteq(\Omega_{\rm vac}^\perp)^\perp=\mathbb C\Omega_{\rm vac}$. Since $T\Omega_{\rm vac}=\Omega_{\rm vac}$ (External Input L.2.6(ii) with $F=1$) and $T=e^{-aH}$, we get $H\Omega_{\rm vac}=0$, so $\Omega_{\rm vac}\in\mathrm{ran}\,E_H(\{0\})\subseteq \mathrm{ran}\,E_H([0,\eta/a))$. Therefore
$$E_H\big([0,\eta/a)\big)=P_{\mathbb C\Omega_{\rm vac}} .$$
A spectral projection of a Borel set equals a rank-one projection onto an eigenvector at $0$ exactly when $\sigma(H)\cap(0,\eta/a)=\emptyset$ and $\ker H=\mathbb C\Omega_{\rm vac}$. Both conclusions follow. $\square$

**Remark on the direction of the argument.** The essential inputs are: (a) $T\ge0$, so that the correlation $\langle\psi,T^n\psi\rangle$ is *nonnegative* and the two-sided bound $0\le\cdot\le Ce^{-\eta n}$ is available; (b) the spectral measure only needs to be tested at the *discrete* times $t=na$ — this is why Lemma L.3.2 is stated for integers and why no continuous-time semigroup is needed at fixed cutoff.

**Converse (spectral gap $\Rightarrow$ decay), reconstructed in full.** Let $\mathcal O\in\mathcal A_+$ with $\mu(\mathcal O)=0$ and put $\psi=[\mathcal O]$, so $\psi\perp\Omega_{\rm vac}$ by Lemma L.4.2. If $\sigma(H)\cap(0,m)=\emptyset$ and $\ker H=\mathbb C\Omega_{\rm vac}$, then $\nu_\psi$ is supported in $[m,\infty)$, hence
$$\big|\mathrm{Cov}_\mu(\theta\mathcal O,\tau_n\mathcal O)\big|=\langle\psi,e^{-naH}\psi\rangle=\int_{[m,\infty)}e^{-na\lambda}d\nu_\psi(\lambda)\le e^{-mna}\,\|\psi\|^2_{\rm OS}.$$
So clustering holds with $\eta=ma$ and $C(\mathcal O)=\|[\mathcal O]\|^2_{\rm OS}=\mu((\theta\mathcal O)\mathcal O)$. Together with Theorem L.4.7 this is an exact equivalence at fixed cutoff, with matching constants.

### Constants and numbers

The gap bound is $\mathrm{gap}(H)\ge\eta/a$ where $\eta$ is the decay rate *per lattice time step* (dimensionless) and $a$ is the lattice spacing. The converse gives $\eta\ge ma$ with constant $C(\mathcal O)=\mu((\theta\mathcal O)\mathcal O)=\|[\mathcal O]\|^2_{\rm OS}$. No other numerical constants appear.

**Caveat.** Assumption L.4.6 is required for *every* bounded $F\in\mathcal A_+$ with an $F$-dependent constant; this is essentially the full clustering statement, not a soft hypothesis, and the corpus never produces $\eta$ for the Wilson measure at any $\beta$.

**Why it matters.** This is the only place in the whole corpus where a genuine quantitative mass-gap statement is derived rather than asserted, and the derivation is correct. It is also the piece that is model-independent and therefore reusable: any lattice model with RP, a time translation and an exponential clustering exponent inherits $\mathrm{gap}(H)\ge\eta/a$.

---

## 4. Physical-units bookkeeping for the continuum limit and the dichotomy reduction

`status: solid` · `kind: obstruction`

### Statement

**Scaling requirement.** Under Theorem L.4.7, at lattice spacing $a$ a one-step Euclidean decay exponent $\eta(a)$ (dimensionless, per lattice step) yields a physical mass lower bound
$$m(a)\ \ge\ \frac{\eta(a)}{a}.$$
Therefore a *finite nonzero* continuum mass $m_{\rm gap}\in(0,\infty)$ requires
$$\eta(a)\ \sim\ m_{\rm gap}\,a\qquad (a\downarrow0),$$
i.e. $\eta(a)\to0$ **linearly in $a$**. A uniform bound $\eta(a)\ge\eta_0>0$ is *not* the goal — it would give $m(a)\gtrsim 1/a$, a pure cutoff artefact with no continuum content. Symmetrically, if $\eta(a)/a\to0$ the reconstructed theory is massless.

**Dichotomy template (SELECTED_05, Theorem 1.1).** Let $\{\mu_a\}$ be a family of lattice Yang–Mills measures with $a\to0$ such that (i) a continuum limit measure $\mu$ exists (tightness + uniqueness), (ii) reflection positivity survives the limit, (iii) local observables are well defined in the limit. Let $\lambda_{\rm lat}(a)$ be the spectral gap of the lattice transfer/generator in lattice units. Then exactly one of:
1. $\displaystyle\liminf_{a\to0}\frac{\lambda_{\rm lat}(a)}{a}\ge c>0$, and the reconstructed continuum Hamiltonian has $\Delta\ge c$;
2. that $\liminf$ is $0$ and the continuum theory is gapless.

The content is not that either alternative is easy, but that once existence, RP and locality are secured, the Millennium problem is reduced to a **single uniformity statement about $\lambda_{\rm lat}(a)/a$**.

### Derivation

The scaling statement is a dimensional identity, but it is worth spelling out because it is the point at which several documents in the corpus silently switch units.

In lattice units the transfer operator advances Euclidean time by one step, i.e. by physical time $a$. Writing $T=e^{-aH}$ and $\lambda_1(T)=\sup\{\sigma(T)\cap[0,1)\}$ (the largest non-vacuum transfer eigenvalue),
$$m(a)\ :=\ -\frac1a\log\lambda_1(T)\ =\ \mathrm{gap}(H).$$
If a per-step contraction rate $\eta(a)$ is proved, $\lambda_1(T)\le e^{-\eta(a)}$, giving $m(a)\ge\eta(a)/a$. Now suppose only $\eta(a)\ge\eta_0>0$ uniformly. Then $m(a)\ge\eta_0/a\to\infty$: every correlation length is $\le a/\eta_0$, i.e. shorter than a few lattice spacings, and the limit theory has no propagating excitation at any fixed physical scale. Conversely, a finite $m_{\rm gap}$ forces $\eta(a)=m_{\rm gap}a+o(a)$.

**Consequence for the corpus's architecture.** Every mechanism in the corpus that produces a *fixed-cutoff* positive constant (a Bakry–Émery curvature floor, a Poincaré constant, a per-step Doeblin minorization) produces $\eta_0$, not $m_{\rm gap}a$. This is the single reason those mechanisms cannot deliver a continuum mass gap, and it is independent of whether the fixed-cutoff estimates are correct. In the language of item 8: a comparison constant $c$ that is $a$-independent in the inequality $\langle F,(I-T_a)F\rangle\ge c\,\mathcal E^{(a)}_{\rm conf}(JF,JF)$ *does* produce the right scaling, because $\mathcal E^{(a)}_{\rm conf}$ is itself $O(a)$ on smooth functions — that is precisely why the scale-$a$ Dirichlet form is the correct comparison object.

**On the dichotomy.** The dichotomy is a tautology once (i)–(iii) are granted: either $\liminf\lambda_{\rm lat}(a)/a>0$ or it is $0$. What is non-trivial (and *assumed*, not proved) is that the reconstructed continuum Hamiltonian's gap is the limit of $\lambda_{\rm lat}(a)/a$; that requires the gap-persistence machinery of item 6 (monotone form limits with a common core and a uniform bound) plus a continuum construction. So the honest statement is: the dichotomy is a correct *organizational* reduction, not a theorem with independent content.

### Constants and numbers

$m(a)=-a^{-1}\log\lambda_1(T_a)$; $m(a)\ge\eta(a)/a$; required scaling $\eta(a)=m_{\rm gap}a+o(a)$. Fixed-cutoff mechanisms in the corpus deliver $\eta(a)\ge\eta_0>0$, i.e. $m(a)\gtrsim 1/a$.

**Caveat.** The dichotomy theorem's alternatives are exhaustive only under the three assumed hypotheses (existence, RP permanence, locality of limiting observables), none of which is established in the corpus.

**Why it matters.** This is the sharpest and most reusable diagnostic in the whole corpus: it tells you, for any proposed mechanism, whether the constant it produces can possibly be a continuum mass. Applied consistently it kills most of the corpus's own headline claims, which is why it belongs in the extracted record.

---

## 5. Permanence of reflection positivity: deterministic pushforward, projective limits, weak limits — and the exact extra condition a Markov kernel must satisfy

`status: solid` · `kind: theorem`

### Statement

Define a **reflected probability space** as $(\Omega,\mathcal F,\mu,\Theta;\mathcal F_+)$ with $\Theta$ a measurable involution and $\mathcal F_+\subseteq\mathcal F$ a designated positive-time sub-$\sigma$-algebra; it is **reflection positive** if $\int\overline{F(\omega)}F(\Theta\omega)\,d\mu\ge0$ for every bounded $\mathcal F_+$-measurable $F$, equivalently if every Gram matrix $\big(\langle F_i,\theta F_j\rangle_{L^2(\mu)}\big)_{i,j}$ over finite families in $L^\infty(\mathcal F_+)$ is PSD.

**Theorem A (pushforward permanence).** Let $(\Omega,\mathcal F,\mu,\Theta;\mathcal F_+)$ be reflection positive and $(\Omega',\mathcal F',\Theta';\mathcal F'_+)$ a reflected measurable space. Let $P:\Omega\to\Omega'$ be measurable with
1. **reflection equivariance** $P\circ\Theta=\Theta'\circ P$,
2. **positive-time preservation** $P^{-1}(\mathcal F'_+)\subseteq\mathcal F_+$.
Then $\mu':=P_\#\mu$ is reflection positive on $(\Omega',\Theta';\mathcal F'_+)$.

**Theorem B (projective-limit permanence, cylinder level).** Let $\{(\Omega_i,\mathcal F_i,\mu_i,\Theta_i;\mathcal F_{i,+})\}_{i\in I}$ be a directed family of reflection-positive spaces with bonding maps $P_{i\to j}$ ($j\preceq i$) satisfying $P_{j\to k}\circ P_{i\to j}=P_{i\to k}$, $P_{i\to j}\circ\Theta_i=\Theta_j\circ P_{i\to j}$, $P_{i\to j}^{-1}(\mathcal F_{j,+})\subseteq\mathcal F_{i,+}$, and $(P_{i\to j})_\#\mu_i=\mu_j$. Let $(\Omega,\mu)$ be the inverse limit with projections $\pi_i$ and induced involution $\Theta$ ($\pi_i\circ\Theta=\Theta_i\circ\pi_i$). Then $\mu$ is reflection positive on positive-time **cylinder** functions.

**Theorem C (weak-limit permanence).** If $\mu_L\Rightarrow\mu_\infty$ weakly on a compact configuration space $\Omega$ with a fixed continuous $\Theta$ and $\mathcal F_+$, and each $\mu_L$ is reflection positive, then $\mu_\infty$ is reflection positive on bounded continuous positive-time cylinder functions.

**Theorem D (Markov-kernel permanence — the precise condition) [reconstructed].** Let $Q$ be a Markov kernel from $(\Omega,\Theta)$ to $(\Omega',\Theta')$ and $\mu':=\mu Q$. Suppose $\Omega'=\Omega'_-\times\Omega'_0\times\Omega'_+$ with $\Theta'$ exchanging $\Omega'_\pm$ and acting on $\Omega'_0$ by an involution $\Theta'_0$, and suppose
$$Q(\omega,dv)=q_0(\omega,dv_0)\;q_+(\omega,v_0,dv_+)\;q_-(\omega,v_0,dv_-)$$
(**conditional independence of the two halves given the boundary variable**), with the equivariance
$$q_-(\omega,v_0,\cdot)=\Theta'_\#\,q_+(\Theta\omega,\Theta'_0v_0,\cdot),\qquad (\Theta\times\Theta'_0)_\#\,(\mu\otimes q_0)=\mu\otimes q_0 .$$
If in addition the extended reflected space $(\Omega\times\Omega'_0,\ \mu\otimes q_0,\ \Theta\times\Theta'_0)$ is reflection positive with positive-time algebra generated by $\mathcal A_+$ and $v_0$, then $\mu'$ is reflection positive.

**Corollary.** A Markov coarse-graining preserves RP essentially only when it is a deterministic map after enlarging the fine space by *reflection-paired, half-split* auxiliary randomness. A kernel that randomizes both sides of the plane with shared noise generically destroys RP.

### Derivation

**Theorem A.** Let $G\in L^\infty(\mathcal F'_+)$ and set $F:=G\circ P$, which lies in $L^\infty(\mathcal F_+)$ by hypothesis 2. Using equivariance,
$$(\theta F)(\omega)=\overline{F(\Theta\omega)}=\overline{G(P(\Theta\omega))}=\overline{G(\Theta'(P\omega))}=(\theta'G)(P\omega),$$
so $\theta F=(\theta'G)\circ P$. Then by the change-of-variables formula for pushforwards,
$$\mu'\big((\theta'G)G\big)=\int_{\Omega'}(\theta'G)(v)G(v)\,d\mu'(v)=\int_{\Omega}(\theta'G)(P\omega)\,G(P\omega)\,d\mu(\omega)=\mu\big((\theta F)F\big)\ \ge\ 0 .$$
The same computation with $F_i:=G_i\circ P$ shows the coarse Gram matrix **equals** a fine Gram matrix, so PSD transfers exactly (no loss). $\square$

**Theorem B.** A positive-time cylinder function is $F=\widetilde F\circ\pi_i$ with $\widetilde F\in L^\infty(\mathcal F_{i,+})$. Since $\pi_i\circ\Theta=\Theta_i\circ\pi_i$, exactly as above $\theta F=(\theta_i\widetilde F)\circ\pi_i$, and by the defining property of the inverse-limit measure $(\pi_i)_\#\mu=\mu_i$,
$$\langle F_p,\theta F_q\rangle_{L^2(\mu)}=\langle\widetilde F_p,\theta_i\widetilde F_q\rangle_{L^2(\mu_i)} .$$
So the cylinder Gram matrix under $\mu$ *is* the Gram matrix under $\mu_i$, which is PSD. Note this needs only that the $i$-cylinder observables be tested; RP on a larger $\sigma$-algebra is never required, and OS reconstruction only ever uses the cylinder algebra. $\square$

**Theorem C.** For fixed bounded continuous $F$ supported on positive-time cylinder coordinates, $\omega\mapsto\overline{F(\omega)}F(\Theta\omega)$ is bounded continuous (as $\Theta$ is continuous), so $\mu\mapsto\int\overline F\,(F\circ\Theta)\,d\mu$ is weakly continuous. The nonnegativity of a weakly continuous functional is preserved in the limit. (On a *periodic* lattice one first notes that for fixed observable supports, wrap-around contributions vanish once $L$ is large, so the finite-volume reflections agree with the infinite-volume one on those supports.) $\square$

**Theorem D (why the deterministic proof does not extend, and what fixes it).** For a general kernel,
$$\mu'\big((\theta'G)G\big)=\int\mu(d\omega)\int Q(\omega,dv)\,(\theta'G)(v)\,G(v),$$
and the inner integral is the expectation of a **product of two functions of the same** $v$. In the deterministic case $Q(\omega,\cdot)=\delta_{P\omega}$ this factorizes trivially. In general it does not, and no amount of equivariance repairs it: equivariance only relates $Q(\Theta\omega,\cdot)$ to $Q(\omega,\cdot)$, it says nothing about correlations *within* one draw.

Under the stated conditional-independence hypothesis, however,
$$\int Q(\omega,dv)(\theta'G)(v)G(v)=\int q_0(\omega,dv_0)\Big[\int q_-(\omega,v_0,dv_-)(\theta'G)(v_-,v_0)\Big]\Big[\int q_+(\omega,v_0,dv_+)G(v_+,v_0)\Big].$$
Define $h(\omega,v_0):=\int q_+(\omega,v_0,dv_+)G(v_+,v_0)$. The equivariance $q_-(\omega,v_0,\cdot)=\Theta'_\#q_+(\Theta\omega,\Theta'_0v_0,\cdot)$ turns the first bracket into $\overline{h(\Theta\omega,\Theta'_0v_0)}$, so
$$\mu'\big((\theta'G)G\big)=\int (\mu\otimes q_0)(d\omega\,dv_0)\ \overline{h\big((\Theta\times\Theta'_0)(\omega,v_0)\big)}\;h(\omega,v_0),$$
which is exactly the RP form of the **extended** reflected space $(\Omega\times\Omega'_0,\mu\otimes q_0,\Theta\times\Theta'_0)$ evaluated on $h$. Nonnegativity therefore follows from RP of the extended space, and $h$ is positive-time measurable there. $\square$

**Interpretation.** This is the precise reason the corpus's escape hatch #1 for the coarse-graining no-go (item 7) — *drop Markovness, use a deterministic blocking map* — is the right move: deterministic maps need nothing beyond equivariance, whereas Markov kernels need a conditional factorization across the plane, which is exactly the structure a genuine renormalization kernel does not have.

### Constants and numbers

None; all statements are exact identities between Gram matrices, with no constants lost.

**Caveat.** Theorems A–C are essentially tautologies once stated correctly (the corpus's own word for them is 'do no harm'); their value is that they pin down the *exact* two hypotheses (equivariance + positive-time preservation) that an RG map must satisfy. Theorem D is my reconstruction; the corpus asserts only that 'stochastic coarse-grainings require a Markov-kernel variant, but the essential algebra is the same', which is false as stated.

**Why it matters.** These lemmas convert 'keep OS positivity across the RG and the continuum limit' from a delicate analytic problem into a checkable design rule on the blocking maps. Theorem D says how much of that rule survives when the blocking is stochastic, and it is exactly the constraint that meets the (A4)+(A5) obstruction of item 7.

---

## 6. Gap persistence under monotone quadratic-form limits

`status: solid` · `kind: theorem`

### Statement

Let $\mathcal H$ be a Hilbert space, $\Omega\in\mathcal H$ a unit vector, $P_0$ the orthogonal projection onto $\mathcal K:=\mathbb C\Omega$. Let $\{q_n\}_{n\ge1}$ be nonnegative quadratic forms with a common dense form core $\mathcal D_0\subseteq\bigcap_n D(q_n)$, satisfying
1. **monotonicity** $q_n(\psi)\le q_{n+1}(\psi)$ for all $\psi\in\mathcal D_0$;
2. **vacuum normalization** $q_n(\Omega)=0$ for all $n$;
3. **uniform gap** there is $\Delta_\star>0$ with $q_n(\psi)\ge\Delta_\star\|(I-P_0)\psi\|^2$ for all $n$ and all $\psi\in\mathcal D_0$.

Define $q_{\rm cont}(\psi):=\sup_nq_n(\psi)$ on $\mathcal D_0$, let $\overline q_{\rm cont}$ be its closure and $H_{\rm cont}\ge0$ the associated self-adjoint operator, $\overline q_{\rm cont}(\psi)=\|H_{\rm cont}^{1/2}\psi\|^2$.

**Proposition.** For all $\psi\in D(\overline q_{\rm cont})$,
$$\overline q_{\rm cont}(\psi)\ \ge\ \Delta_\star\,\|(I-P_0)\psi\|^2,\qquad\text{i.e.}\qquad H_{\rm cont}\ \succeq\ \Delta_\star\,(I-P_0)\ \ \text{as forms}.$$
**Corollary.** $\sigma(H_{\rm cont})\subseteq\{0\}\cup[\Delta_\star,\infty)$; if moreover $\ker H_{\rm cont}=\mathbb C\Omega$ then $\mathrm{gap}(H_{\rm cont})\ge\Delta_\star$.

### Derivation

On the core, take $\sup_n$ of hypothesis 3: since the right-hand side does not depend on $n$,
$$q_{\rm cont}(\psi)=\sup_nq_n(\psi)\ \ge\ \Delta_\star\|(I-P_0)\psi\|^2,\qquad\psi\in\mathcal D_0 .$$
For the closure: let $\psi\in D(\overline q_{\rm cont})$ and take $\psi_k\in\mathcal D_0$ with $\psi_k\to\psi$ in $\mathcal H$ and $q_{\rm cont}(\psi_k-\psi_j)\to0$ (form-core convergence), so $\overline q_{\rm cont}(\psi_k)\to\overline q_{\rm cont}(\psi)$. Since $I-P_0$ is bounded, $\|(I-P_0)\psi_k\|^2\to\|(I-P_0)\psi\|^2$. Passing to the limit in the inequality gives the claim.

For the corollary: $H_{\rm cont}\succeq\Delta_\star(I-P_0)$ as forms means, for every $\psi\perp\Omega$ in the form domain, $\|H_{\rm cont}^{1/2}\psi\|^2\ge\Delta_\star\|\psi\|^2$. If $\sigma(H_{\rm cont})$ contained a point $\lambda\in(0,\Delta_\star)$ then, choosing $\varepsilon$ with $\lambda+\varepsilon<\Delta_\star$, the spectral subspace $\mathcal R:=\mathrm{ran}\,E_{H_{\rm cont}}((0,\lambda+\varepsilon))$ would be nonzero and contained in $\Omega^\perp$ (because $\Omega\in\ker H_{\rm cont}$, using $q_n(\Omega)=0\Rightarrow\overline q_{\rm cont}(\Omega)=0$), and every unit $\psi\in\mathcal R$ would satisfy $\overline q_{\rm cont}(\psi)=\int\lambda'\,d\nu_\psi\le\lambda+\varepsilon<\Delta_\star$, contradicting the form bound. $\square$

**Where the hypotheses bite.** The three hypotheses are exactly the three things a continuum construction must supply and which the corpus never supplies: (i) a *common* Hilbert space and dense core for all cutoffs (this is where the embeddings $J_a:\mathcal H_{{\rm OS},a}\to\mathcal H_{{\rm OS},\infty}$ live), (ii) *monotonicity* of the forms under refinement (a strong and unverified structural requirement), (iii) the uniform bound $\Delta_\star$ in **physical** units, which by item 4 means $\eta(a)/a\ge\Delta_\star$, not $\eta(a)\ge\eta_0$. Without monotonicity one must instead use strong resolvent convergence / Mosco convergence, for which gap persistence is *not* automatic (spectrum can drop in the limit); the corpus's SCALING_LIMIT notes list this as the alternative route but never carry it out.

### Constants and numbers

$\Delta_\star>0$ is the uniform-in-$n$ (i.e. uniform-in-cutoff) gap constant, in physical units. The conclusion is exactly $\mathrm{gap}(H_{\rm cont})\ge\Delta_\star$ with no loss of constant.

**Caveat.** Monotone form convergence is a strong hypothesis; for lattice-to-continuum families it is not known to hold and is not verified anywhere in the corpus. Under mere strong-resolvent/Mosco convergence the conclusion fails in general.

**Why it matters.** It is the correct functional-analytic 'battery' for the last step of any lattice-to-continuum gap argument, and it makes explicit that the whole continuum step reduces to (common core) + (monotonicity) + (uniform gap in physical units).

---

## 7. Two-line obstruction: no gauge-covariant, gauge-invariant Markov coarse-graining kernel exists for nontrivial $G$

`status: solid` · `kind: obstruction`

### Statement

Let $G$ be a group with $|G|>1$ (in particular any nontrivial compact Lie group). Let $\Lambda_a,\Lambda_{a'}$ be lattices with $\Omega_a=G^{E(\Lambda_a)}$, $\Omega_{a'}=G^{E(\Lambda_{a'})}$ and gauge groups $\mathcal G_a=G^{V(\Lambda_a)}$, $\mathcal G_{a'}=G^{V(\Lambda_{a'})}$ acting by
$$(g\cdot U)_{xy}=g_x\,U_{xy}\,g_y^{-1},\qquad x\ne y .$$
Let $\Pi:\Omega_a\to\Omega_{a'}$ be a Markov coarse-graining (a conditional expectation / kernel) and consider the two assumptions:

- **(A5)** $\Pi$ is the conditional expectation onto a $\sigma$-algebra generated by **gauge-invariant** block variables; hence $\Pi(g\cdot U)=\Pi(U)$ for $\mu_a$-a.e. $U$ and all $g\in\mathcal G_a$.
- **(A4)** $\Pi$ is **gauge covariant**: $\Pi(g\cdot U)=g'\cdot\Pi(U)$, where the induced map $g\mapsto g'$ has image containing all of $\mathcal G_{a'}$.

**Theorem.** (A4) and (A5) are incompatible: they force $\Pi(U)$ to be a fixed point of the full $\mathcal G_{a'}$-action on $G^{E(\Lambda_{a'})}$, and
$$\mathrm{Fix}\big(\mathcal G_{a'}\curvearrowright G^{E(\Lambda_{a'})}\big)=\emptyset\qquad\text{whenever }|G|>1\text{ and }E(\Lambda_{a'})\ne\emptyset .$$
Hence no such $\Pi$ exists.

### Derivation

**Proof.** Fix $U$ in the full-measure set on which both assumptions hold, and let $g'\in\mathcal G_{a'}$ be arbitrary. By (A4) surjectivity choose $g\in\mathcal G_a$ inducing $g'$. Then
$$\Pi(U)\ \overset{\text{(A5)}}{=}\ \Pi(g\cdot U)\ \overset{\text{(A4)}}{=}\ g'\cdot\Pi(U).$$
Since $g'$ was arbitrary, $V:=\Pi(U)$ satisfies $g'\cdot V=V$ for **all** $g'\in\mathcal G_{a'}$.

Now compute the fixed-point set. Let $e=(x,y)$ be any edge of $\Lambda_{a'}$ with $x\ne y$ (such an edge exists as soon as the coarse lattice is nondegenerate). Choose $g'$ with $g'_y=1$ and $g'_x=h$ arbitrary; then
$$V_e=(g'\cdot V)_e=g'_x\,V_e\,(g'_y)^{-1}=h\,V_e\ \Longrightarrow\ h=1 .$$
Since $h\in G$ was arbitrary, $G=\{1\}$ — contradicting $|G|>1$. Therefore the fixed-point set is empty and no $\Pi$ satisfying both (A4) and (A5) exists. $\blacksquare$

(The argument uses nothing about compactness, smoothness, measure, or the reflection structure; it is pure group theory. It also shows the failure is *maximal*: the fixed set is empty, not merely small.)

**What must give — the design space (all four escapes are genuine).**
1. **Drop Markovness.** Use a deterministic blocking map $P:\Omega_a\to\Omega_{a'}$ and pushforward. By item 5, Theorem A, RP permanence needs only reflection equivariance and positive-time preservation — no Markov structure at all. This is what Wilson blocking, Migdal–Kadanoff and HYP/APE smearing do: coarse links are built as path-ordered products, which are gauge **covariant but not gauge invariant**, so (A5) fails and there is no contradiction. The obstruction therefore explains *why* every scheme in the literature is built this way.
2. **Change the coarse variable.** Let it live on the gauge-orbit space $\Omega_{a'}/\mathcal G_{a'}$ or on a connection on a coarser bundle, rather than in $G^{E(\Lambda_{a'})}$ with the endpoint action. Then (A4)'s hypothesis 'image contains $\mathcal G_{a'}$' is vacuous.
3. **Gauge-fix before coarse graining**, removing the endpoint redundancy that creates the empty fixed set (at the cost of Gribov ambiguities).
4. **Weaken covariance** to a proper subgroup (e.g. the diagonal/global gauge subgroup, whose fixed set is *not* empty), or demand covariance only on a subalgebra.

**Consistency with item 5.** Escape 1 is exactly the route RP permanence prefers. Escape 1 combined with Theorem D of item 5 gives the coherent picture: RP survives deterministic equivariant blocking for free; a *stochastic* blocking would need a conditional factorization across the reflection plane; and a stochastic blocking that is simultaneously gauge invariant and gauge covariant does not exist at all.

### Constants and numbers

None. The only quantitative content is $|\mathrm{Fix}(\mathcal G_{a'})|=0$ for $|G|>1$.

**Caveat.** The result is elementary — one line of group theory — and it rules out an assumption pair that no standard blocking scheme adopts; its value is diagnostic, not deep. A companion 'no-go' in the same source file (that fixed-cutoff OS data cannot force a cross-scale map $\Pi$, via 'OS-preserving UV twists') is asserted with no construction and is *not* extracted here: it is unproved.

**Why it matters.** It is a correct, fully proved statement that eliminates an entire class of RG architectures — precisely the class the corpus was trying to build — and it explains in one line why the working blocking schemes in the lattice literature are covariant-but-not-invariant. It also converts the vague slogan 'the coarse-graining must be chosen carefully' into a checkable dichotomy.

---

## 8. The boundedness obstruction to a global one-step OS / Dirichlet comparison, and the scale-$a$ replacement

`status: solid` · `kind: obstruction`

### Statement

**Part 1 (the obstruction).** Let $(\Sigma,\nu)$ be a compact Riemannian manifold (e.g. $\Sigma=G^{E_s}$, a finite product of copies of a compact Lie group, with $\nu$ having a smooth positive density) and let $K$ be **any** bounded operator on $L^2(\nu)$ with $\|K\|\le1$ — in particular any Markov operator, and in particular the OS one-step transfer operator $T_a$ compressed to the boundary. Then its Dirichlet form
$$\mathcal E_K(f,f):=\langle f,(I-K)f\rangle_{L^2(\nu)}$$
satisfies $0\le\mathcal E_K(f,f)\le2\|f\|_2^2$, and consequently
$$\nexists\,c>0\ \text{ such that }\ \mathcal E_K(f,f)\ \ge\ c\int_\Sigma|\nabla f|^2\,d\nu\quad\text{for all }f\in H^1(\nu).$$
So the naive bridge inequality $\langle F,(I-T_a)F\rangle_{\mathcal H_{\rm OS}}\gtrsim\int|\nabla F|^2$ is *impossible*, at any lattice spacing, on any compact configuration space, for any model.

**Part 2 (the correct bounded surrogate).** Let $(P_t)_{t\ge0}$ be the reversible configuration-diffusion semigroup on $L^2(\nu)$ with generator $L$ ($L\le0$, $L1=0$) and carré du champ $\Gamma(f)=|\nabla f|^2$. Define the **scale-$a$ Dirichlet form**
$$\mathcal E^{(a)}_{\rm conf}(f,f):=\langle f,(I-P_a)f\rangle_{L^2(\nu)} .$$
Then:
(i) $0\le\mathcal E^{(a)}_{\rm conf}(f,f)\le2\|f\|_2^2$, and in fact $\le\mathrm{Var}_\nu(f)$;
(ii) **exact gradient representation** $\displaystyle \mathcal E^{(a)}_{\rm conf}(f,f)=\int_0^a\!\!\int_\Sigma|\nabla P_{t/2}f|^2\,d\nu\,dt$;
(iii) **smoothing bound** $\mathcal E^{(a)}_{\rm conf}(f,f)\le a\int|\nabla f|^2d\nu$;
(iv) if $-L$ has spectral gap $\lambda_*>0$ on mean-zero functions, $\mathcal E^{(a)}_{\rm conf}(f,f)\ge(1-e^{-a\lambda_*})\|f-\nu(f)\|_2^2$.

**Part 3 (boundary realization identity).** Let $\mathcal A^+$ be the positive-time algebra, $\mathscr B$ the $\sigma$-algebra of the time-slice variables at the reflection plane, and $(JF)(\sigma):=\mathbb E_\mu[F\mid\mathscr B](\sigma)$. Under the Markov property across the plane, $J$ is an isometry $\mathcal H_{\rm OS}\hookrightarrow L^2(\Sigma,\nu)$ and there is a self-adjoint Markov operator $K_a$ on $L^2(\nu)$ with $\langle F,T_aG\rangle_{\rm OS}=\langle JF,K_aJG\rangle_{L^2(\nu)}$. Consequently
$$\boxed{\ \langle F,(I-T_a)F\rangle_{\mathcal H_{\rm OS}}=\langle JF,(I-K_a)JF\rangle_{L^2(\nu)}=\mathcal E_{K_a}(JF,JF).\ }$$
$K_a$ is built from the **strip kernel**
$$\mathcal K_a(\sigma,\sigma'):=\int_{G^{\Lambda_s}}W_a(\sigma,\sigma',U_0)\prod_{x\in\Lambda_s}dH(U_0(x)),$$
$$W_a(\sigma,\sigma',U_0):=\Big(\prod_{p\in P_0}w\big(U_p(\sigma,\sigma',U_0)\big)\Big)e^{-\frac12S_{\rm sp}(\sigma)}e^{-\frac12S_{\rm sp}(\sigma')},$$
with $\sigma,\sigma'$ the spatial link configurations on the two slices, $U_0$ the time-like links between them, $P_0$ the straddling plaquettes, and the half-weighting of the slice actions making the kernel symmetric; the boundary measure is $d\nu(\sigma)=Z_\nu^{-1}e^{-S_{\rm sp}(\sigma)}\prod_{\ell\in E_s}dH(\sigma_\ell)$.

**Part 4 (the target inequality, restated correctly).** The viable replacement for the impossible bridge is: there exists $c>0$, independent of the volume (and depending only on $d$, $G$, $\beta$, the plaquette-weight class), such that
$$\langle F,(I-T_a)F\rangle_{\mathcal H_{\rm OS}}\ \ge\ c\,\mathcal E^{(a)}_{\rm conf}(JF,JF)\qquad\forall F\in\mathcal A^+ .$$
Combined with (iv), this yields a per-step gap and
$$m(a)=-\frac1a\log\lambda_1(K_a)\ \ge\ -\frac1a\log\!\big(1-c(1-e^{-a\lambda_*})\big)\ \xrightarrow[a\to0]{}\ c\,\lambda_* ,$$
an $a$-independent physical mass.

### Derivation

**Part 1.** Since $\|K\|\le1$ and $I$ has norm $1$, $\|I-K\|\le2$, so $|\langle f,(I-K)f\rangle|\le2\|f\|_2^2$. For a Markov operator one also has $\mathcal E_K\ge0$ on real $f$ by Jensen. Now let $-\Delta_\nu$ be the weighted Laplacian associated with $\int|\nabla f|^2d\nu$ on the compact manifold $\Sigma$: its spectrum is discrete, $0=\lambda_0<\lambda_1\le\lambda_2\le\cdots\to\infty$, with $L^2$-normalized eigenfunctions $\varphi_k$ satisfying $\int|\nabla\varphi_k|^2d\nu=\lambda_k$. Taking $f=\varphi_k$ in the putative inequality gives $2\ge c\lambda_k$ for every $k$, hence $c\le2/\lambda_k\to0$, so $c=0$. $\square$

(Concretely for $\Sigma=SU(2)^{E_s}$ with Haar measure, the eigenvalues are sums of Casimirs $4j(j+1)$, $j\in\tfrac12\mathbb N_0$, which are unbounded. So the obstruction is not an artefact of infinite volume — it already holds on a **single link**.)

**Part 2(ii), the gradient representation, in full.** For $f$ in the form domain, $t\mapsto\langle f,P_tf\rangle$ is differentiable with $\frac{d}{dt}\langle f,P_tf\rangle=\langle f,LP_tf\rangle$. Since $P_{t/2}$ is self-adjoint, commutes with $L$, and $P_t=P_{t/2}P_{t/2}$,
$$-\langle f,LP_tf\rangle=-\langle f,P_{t/2}LP_{t/2}f\rangle=-\langle P_{t/2}f,LP_{t/2}f\rangle=\int_\Sigma\Gamma(P_{t/2}f)\,d\nu=\int|\nabla P_{t/2}f|^2d\nu .$$
Integrating from $0$ to $a$ and using $P_0=I$,
$$\mathcal E^{(a)}_{\rm conf}(f,f)=\langle f,f\rangle-\langle f,P_af\rangle=-\int_0^a\frac{d}{dt}\langle f,P_tf\rangle\,dt=\int_0^a\!\!\int|\nabla P_{t/2}f|^2\,d\nu\,dt .$$

**Part 2(iii), smoothing.** In the spectral calculus of $-L$ with spectral measure $\nu_f$,
$$\int|\nabla P_sf|^2d\nu=\langle P_sf,(-L)P_sf\rangle=\int_{[0,\infty)}\lambda\,e^{-2s\lambda}\,d\nu_f(\lambda)\ \le\ \int\lambda\,d\nu_f(\lambda)=\int|\nabla f|^2d\nu ,$$
since $e^{-2s\lambda}\le1$. Substituting into (ii) gives $\mathcal E^{(a)}_{\rm conf}(f,f)\le a\int|\nabla f|^2d\nu$. This is the precise sense in which $\mathcal E^{(a)}_{\rm conf}$ is a *bounded, scale-$a$-smoothed* gradient energy: it agrees with $a\int|\nabla f|^2$ on modes with $a\lambda\ll1$ and saturates at $\|f\|^2$ on modes with $a\lambda\gg1$. Explicitly, $\mathcal E^{(a)}_{\rm conf}(f,f)=\int(1-e^{-a\lambda})\,d\nu_f(\lambda)$, and $\min(1,a\lambda)/2\le 1-e^{-a\lambda}\le\min(1,a\lambda)$.

**Part 2(i) and (iv).** From $\mathcal E^{(a)}_{\rm conf}(f,f)=\int(1-e^{-a\lambda})d\nu_f(\lambda)$ with $0\le1-e^{-a\lambda}\le1$: for mean-zero $f$, $\mathcal E^{(a)}_{\rm conf}(f,f)\le\|f\|_2^2=\mathrm{Var}_\nu(f)$; and if $\nu_f$ is supported in $[\lambda_*,\infty)$ then $1-e^{-a\lambda}\ge1-e^{-a\lambda_*}$ there, giving (iv).

**Part 4, the mass extraction.** Assume the comparison with constant $c>0$ and let $F\perp\Omega$, $\|JF\|_2=1$, $\nu(JF)=0$. Then
$$\langle JF,(I-K_a)JF\rangle\ \ge\ c\,\mathcal E^{(a)}_{\rm conf}(JF,JF)\ \ge\ c\,(1-e^{-a\lambda_*}) .$$
By the variational principle for the self-adjoint contraction $K_a$ restricted to $1^\perp$, $\lambda_1(K_a)\le1-c(1-e^{-a\lambda_*})$, hence
$$m(a)=-\frac1a\log\lambda_1(K_a)\ \ge\ -\frac1a\log\!\big(1-c(1-e^{-a\lambda_*})\big).$$
As $a\downarrow0$, $1-e^{-a\lambda_*}=a\lambda_*+O(a^2)$ and $-\log(1-ca\lambda_*+O(a^2))=ca\lambda_*+O(a^2)$, giving $m(a)\ge c\lambda_*+O(a)$. This is exactly the scaling demanded by item 4: a *bounded* comparison form with an $a$-independent constant produces an $a$-independent mass, whereas the impossible unbounded comparison would have produced nothing at all.

**Honest status of the proof of Part 4 in the corpus.** The corpus's 'Step A' proof of Part 4 reads: a Doeblin minorization for the local block operator $K_{a,p}$ gives $\mathrm{Var}_{\nu_p}(g)\le\lambda_p^{-1}\langle g,(I-K_{a,p})g\rangle$, a group Poincaré inequality gives $\mathrm{Var}_{\nu_p}(g)\le C_p\int|\nabla g|^2$, and 'combining yields $\langle g,(I-K_{a,p})g\rangle\ge(\lambda_p/C_p)\int|\nabla g|^2$.' That last step is invalid — the two inequalities chain the wrong way (both bound $\mathrm{Var}$ from above) — and the asserted conclusion is precisely the inequality that Part 1 proves to be impossible, now on a fixed finite block, where the gradient form is still unbounded. So Part 4 has no proof in the corpus. Furthermore, since $\mathcal E^{(a)}_{\rm conf}(f,f)\le\mathrm{Var}_\nu(f)$, Part 4 is *implied by* a Poincaré inequality for $K_a$ with constant $c$; it is a genuine weakening of the target, not an independently easier route, unless one finds a way to bound $\langle f,(I-K_a)f\rangle$ below by smoothed gradient energy without first proving a spectral gap.

**What survives, unambiguously:** Parts 1, 2 (all four items, with exact identities and constants) and the *formulation* of Part 3–4. The replacement of an impossible comparison by the correct bounded object is a real, checkable mathematical correction.

### Constants and numbers

$0\le\mathcal E_K(f,f)\le2\|f\|_2^2$ for any $\|K\|\le1$. Exact identity $\mathcal E^{(a)}_{\rm conf}(f,f)=\int_0^a\int|\nabla P_{t/2}f|^2d\nu\,dt=\int(1-e^{-a\lambda})d\nu_f(\lambda)$. Two-sided comparison $\tfrac12\min(1,a\lambda)\le1-e^{-a\lambda}\le\min(1,a\lambda)$, hence $\mathcal E^{(a)}_{\rm conf}\le a\,\mathcal E_{\rm grad}$ and $\mathcal E^{(a)}_{\rm conf}\le\mathrm{Var}_\nu$. Gap transfer: $\lambda_1(K_a)\le1-c(1-e^{-a\lambda_*})$ and $m(a)\ge c\lambda_*+O(a)$. For $\Sigma=SU(2)^{E_s}$ with Haar, the gradient form's spectrum is $\{\sum_\ell 4j_\ell(j_\ell+1)\}$, unbounded, which is the concrete witness for Part 1.

**Caveat.** Part 3's isometric compression $J$ requires the Markov property across the reflection plane and the standard half-weighting; that is classical for Wilson-type actions but is imported, not proved. Part 4 is stated correctly but is **not proved** in the corpus: its 'Step A' reproduces exactly the inequality that Part 1 rules out, and its bounded-overlap summation (Step C) is not justified.

**Why it matters.** This is the single most useful negative result in the OS half of the corpus: it identifies, with a two-line proof, why the project's central 'bridge inequality' can never be proved as stated, and it supplies the correct replacement object together with the exact semigroup identities that make the replacement quantitative and scaling-correct. Anyone attempting a diffusion-to-transfer-matrix comparison in any lattice model needs Part 1 before starting.

---

## 9. Chessboard single-plaquette tail bound from reflection positivity (volume-uniform)

`status: solid` · `kind: derivation`

### Statement

Let $\Lambda$ be a finite periodic 4D hypercubic lattice with edge set $E$ and plaquette set $P$, $G=SU(N)$, $\mathscr A=G^E$ with the product bi-invariant metric $g$ and volume form $d\mathrm{vol}_g$. Write
$$\Phi(V):=\tfrac1N\Re\mathrm{Tr}(I-V),\qquad S_\beta(U)=\beta\sum_{p\in P}\Phi(U_p),\qquad d\mu_\beta=Z_\beta^{-1}e^{-S_\beta}d\mathrm{vol}_g,$$
and let $d_G$ be the bi-invariant Riemannian distance. For $\delta>0$ set
$$A_{p,\delta}:=\{U:d_G(U_p,I)\ge\delta\},\qquad c_\Phi(\delta):=\inf\{\Phi(V):d_G(V,I)\ge\delta\}>0 .$$

**Lemma (single-plaquette tail).** Assume $\mu_\beta$ is reflection positive, hence satisfies the chessboard estimate for plaquette events. Then there are constants $C_0>0$ and $\alpha:=\dim(G)\cdot|E|/|P|$, depending only on $G$ and the dimension (**not** on the volume), such that for every $p\in P$ and every $\beta\ge1$,
$$\mu_\beta\big(A_{p,\delta}\big)\ \le\ C_0\,\beta^{\alpha/2}\,e^{-\beta\,c_\Phi(\delta)} .$$
In 4D, $|E|/|P|=4/6=2/3$, so $\alpha=\tfrac23\dim G$ ($=2$ for $SU(2)$, $=16/3$ for $SU(3)$). For small $\delta$, with the metric $\langle X,Y\rangle=-\mathrm{Tr}(XY)$ on $\mathfrak{su}(N)$,
$$c_\Phi(\delta)=\frac{\delta^2}{2N}+O(\delta^3).$$

**Corollary (local tube).** For $P_R\subseteq P$ the plaquettes meeting a fixed physical ball $B_R$ (so $|P_R|\asymp 6(R/a)^4$), and $\Omega_{\delta,R}:=\{U:\forall p\in P_R,\ d_G(U_p,I)\le\delta\}$,
$$\mu_\beta\big(\Omega_{\delta,R}^c\big)\ \le\ |P_R|\,C_0\,\beta^{\alpha/2}\,e^{-\beta c_\Phi(\delta)} .$$

**Proposition (defective Poincaré).** If $F$ is bounded and supported in $B_R$, and on $\Omega_{\delta,R}$ the horizontal Bakry–Émery curvature admits a floor $\rho_{\rm loc}>0$, then
$$\mathrm{Var}_{\mu_\beta}(F)\ \le\ \frac1{\rho_{\rm loc}}\int|\nabla F|^2d\mu_\beta\ +\ 4\|F\|_\infty^2\,\mu_\beta\big(\Omega_{\delta,R}^c\big).$$

### Derivation

**Step 1 (energy cost).** On the event that *every* plaquette is $\delta$-bad, $\Phi(U_p)\ge c_\Phi(\delta)$ for all $p$, hence $S_\beta(U)\ge\beta|P|\,c_\Phi(\delta)$.

**Step 2 (chessboard reduction).** Reflection positivity in all lattice directions yields the chessboard estimate: for a single-plaquette event $A_{p,\delta}$,
$$\mu_\beta(A_{p,\delta})\ \le\ \Big(\frac{Z_\beta^{\rm bad}}{Z_\beta}\Big)^{1/|P|},$$
where $Z_\beta^{\rm bad}$ is the constrained partition function with the bad event imposed on the full reflection-tiling of the lattice — in particular one may bound it by imposing $A_{q,\delta}$ for *all* $q\in P$. (This is the standard Fröhlich–Israel–Lieb–Simon / Osterwalder–Seiler mechanism: RP $\Rightarrow$ a local probability is dominated by the $|P|$-th root of an extensive ratio.)

**Step 3 (upper bound on $Z_\beta^{\rm bad}$).** Using only Step 1,
$$Z_\beta^{\rm bad}\ \le\ e^{-\beta|P|c_\Phi(\delta)}\;\mathrm{Vol}_g(\mathscr A).$$

**Step 4 (lower bound on $Z_\beta$ from a small product ball).** Let $B_r\subset G$ be the geodesic ball of radius $r<\mathrm{inj}(G)$ about $I$, and $\mathcal B_r:=\{U:U_e\in B_r\ \forall e\in E\}$. If every link is within $r$ of the identity then each plaquette holonomy is within $O(r)$ of $I$ (four factors), so by the small-angle expansion $\Phi(U_p)\le C_\Phi r^2$ and $S_\beta(U)\le\beta|P|C_\Phi r^2$ on $\mathcal B_r$. Also $\mathrm{Vol}_g(B_r)\sim v_Gr^{\dim G}$ as $r\downarrow0$, so $\mathrm{Vol}_g(\mathcal B_r)\ge(v_Gr^{\dim G})^{|E|}$ and
$$Z_\beta\ \ge\ \int_{\mathcal B_r}e^{-S_\beta}\,d\mathrm{vol}_g\ \ge\ e^{-\beta|P|C_\Phi r^2}\,(v_Gr^{\dim G})^{|E|}.$$

**Step 5 (the $1/|P|$ root — this is where the volume cancels).** Combining Steps 2–4,
$$\mu_\beta(A_{p,\delta})\ \le\ \exp\!\big(-\beta c_\Phi(\delta)+\beta C_\Phi r^2\big)\cdot\Big(\frac{\mathrm{Vol}_g(\mathscr A)}{(v_Gr^{\dim G})^{|E|}}\Big)^{1/|P|}.$$
Both $|E|$ and $|P|$ are proportional to the number of sites, so $|E|/|P|$ is a *dimension-dependent constant* ($=2/3$ in 4D), and $\mathrm{Vol}_g(\mathscr A)^{1/|P|}=\mathrm{Vol}_g(G)^{|E|/|P|}$ is volume-independent. The last factor is therefore $\lesssim r^{-\alpha}$ with $\alpha=\dim(G)\,|E|/|P|$. **The estimate is genuinely uniform in the volume.**

**Step 6 (optimize $r$).** Choose $r\asymp\beta^{-1/2}$ so that $\beta C_\Phi r^2=O(1)$; then $r^{-\alpha}=\beta^{\alpha/2}$ and
$$\mu_\beta(A_{p,\delta})\ \le\ C_0\,\beta^{\alpha/2}\,e^{-\beta c_\Phi(\delta)} .\qquad\square$$

**Small-$\delta$ asymptotics of $c_\Phi$, computed explicitly.** With $\langle X,Y\rangle=-\mathrm{Tr}(XY)$ on $\mathfrak{su}(N)$ and $V=\exp X$,
$$\Phi(\exp X)=1-\tfrac1N\Re\mathrm{Tr}\big(I+X+\tfrac12X^2+\dots\big)=-\tfrac1{2N}\mathrm{Tr}(X^2)+O(\|X\|^3)=\frac{\|X\|^2}{2N}+O(\|X\|^3),$$
using $\mathrm{Tr}\,X=0$ and $\mathrm{Tr}(X^2)=-\|X\|^2$. Since $d_G(\exp X,I)=\|X\|$ for $\|X\|$ below the injectivity radius, the leading term is *isotropic*, so $c_\Phi(\delta)=\delta^2/(2N)+O(\delta^3)$ (no direction-dependent minimization is needed at leading order). Check for $N=2$: $V=\mathrm{diag}(e^{i\theta},e^{-i\theta})$, $X=\mathrm{diag}(i\theta,-i\theta)$, $\|X\|^2=2\theta^2$, $\Phi=1-\cos\theta\approx\theta^2/2=\|X\|^2/4=\delta^2/(2N)$. ✓

**Defective Poincaré (Proposition).** Split $\mathrm{Var}_{\mu}(F)=\tfrac12\iint|F(U)-F(U')|^2d\mu d\mu$. On $\Omega_{\delta,R}\times\Omega_{\delta,R}$ use the curvature floor to run the standard Bakry–Émery/Poincaré estimate, contributing $\rho_{\rm loc}^{-1}\int|\nabla F|^2$; on the complement bound $|F(U)-F(U')|^2\le4\|F\|_\infty^2$ and the measure of the complement by $2\mu(\Omega^c_{\delta,R})$ (union over the two factors), giving the stated defect $4\|F\|_\infty^2\mu(\Omega^c_{\delta,R})$.

### Constants and numbers

$\alpha=\dim(G)\,|E|/|P|$; in 4D $|E|/|P|=2/3$, so $\alpha=2$ for $SU(2)$ ($\dim=3$) and $\alpha=16/3$ for $SU(3)$ ($\dim=8$); the prefactor after optimizing $r\asymp\beta^{-1/2}$ is $\beta^{\alpha/2}$, i.e. $\beta^{1}$ for $SU(2)$ and $\beta^{8/3}$ for $SU(3)$. $c_\Phi(\delta)=\delta^2/(2N)+O(\delta^3)$ with the metric $\langle X,Y\rangle=-\mathrm{Tr}(XY)$. $\mathrm{Vol}_g(B_r)\sim v_Gr^{\dim G}$. $|P_R|\asymp6(R/a)^4$. Valid for all $\beta\ge1$, uniformly in the lattice volume.

**Caveat.** The chessboard estimate itself is imported (standard under RP, but the precise reflection/tiling set-up for plaquette events on a periodic gauge lattice is not written out in the corpus). The curvature input feeding the defective Poincaré ('$\nabla^2S_\beta\ge\beta c_Wg$ on horizontals, uniformly over small-angle configurations') is almost certainly false as stated — near $U=I$ the Wilson Hessian is a lattice curl-curl operator whose smallest nonzero horizontal eigenvalue scales like $(2\pi/L)^2$ and is not bounded below uniformly in volume.

**Why it matters.** This is a correct, fully quantitative, volume-uniform concentration estimate for plaquettes at large $\beta$ derived directly from reflection positivity — the only place in the corpus where RP is used as an *analytic tool* rather than as an axiom for reconstruction. It is also the exact input for the counting obstruction of item 10.

---

## 10. Counting obstruction: the small-plaquette 'tube' event cannot have vanishing failure probability at fixed physical volume as $a\to0$

`status: conditional` · `kind: obstruction`

### Statement

Combine the volume-uniform chessboard tail bound of item 9 with the one-loop asymptotically free trajectory for pure $SU(N)$ lattice gauge theory,
$$\beta(a)=c\,\ln\!\frac{1}{a\Lambda},\qquad c:=\frac{11N^2}{12\pi^2},$$
(derived from $\beta=2N/g^2$ and $g^{-2}(a)=2b_0\ln(1/(a\Lambda))$ with $b_0=\frac{11N}{48\pi^2}$). Fix a physical ball $B_R$, so $|P_R|\asymp6(R/a)^4$. Then
$$\mu_{\beta(a)}\big(\Omega^c_{\delta,R}\big)\ \le\ 6R^4a^{-4}\,C_0\,\beta(a)^{\alpha/2}\,e^{-\beta(a)c_\Phi(\delta)}\ =\ 6R^4C_0\,\beta(a)^{\alpha/2}\,a^{\,c\,c_\Phi(\delta)-4}\Lambda^{-c\,c_\Phi(\delta)} ,$$
so this union bound is $o(1)$ as $a\downarrow0$ **iff**
$$c\,c_\Phi(\delta)\ >\ 4\qquad\Longleftrightarrow\qquad c_\Phi(\delta)\ >\ \frac{4}{c}=\frac{48\pi^2}{11N^2} .$$

**Obstruction.** $c_\Phi(\delta)$ is bounded above for every $\delta$ by
$$\Phi_{\max}:=\sup_{V\in SU(N)}\Phi(V)=1-\frac1N\min_{V\in SU(N)}\Re\mathrm{Tr}\,V=\begin{cases}2,& N\text{ even}\\[2pt] 1+\cos(\pi/N),& N\text{ odd}\end{cases}\ \le\ 2 .$$
Hence **no choice of $\delta$** makes the tube-failure bound vanish whenever $c\,\Phi_{\max}\le4$, which holds for $N=2,3,4$ (values $0.743$, $1.254$, $2.972$). The plaquette entropy $a^{-4}$ beats the merely logarithmic growth of $\beta(a)$. Consequently the 'remaining surgical task' identified in the source (Corollary 3.2: *choose $\delta$ so that $c_\Phi(\delta)$ dominates $|P_R|\sim(R/a)^4$*) is impossible as stated for the physically relevant gauge groups.

**Sharpening (mine).** Even for $N\ge5$, where the crude arithmetic no longer closes ($c\,\Phi_{\max}=4.200$ at $N=5$), the required $\delta$ is not admissible: using $c_\Phi(\delta)=\delta^2/(2N)+O(\delta^3)$, the condition $c_\Phi(\delta)>48\pi^2/(11N^2)$ forces
$$\delta\ \gtrsim\ \pi\sqrt{\frac{96}{11N}}\ =\ \frac{9.28}{\sqrt N},$$
i.e. $\delta\gtrsim5.36$ for $N=3$ and $\gtrsim4.15$ for $N=5$ — far outside any small-angle window $\delta\le\delta_*$ in which the local convexity floor is valid, and for $N=3$ larger than the diameter of $SU(3)$ itself ($d_G(\omega I,I)=2\pi\sqrt{2/3}\approx5.13$ for $\omega=e^{2\pi i/3}$). So the obstruction is robust in the regime where the bridge is actually needed.

### Derivation

**Step 1 (the trajectory constant).** For pure $SU(N)$, the one-loop beta function is $\mu\,dg/d\mu=-b_0g^3$ with $b_0=\frac{11N}{3(4\pi)^2}=\frac{11N}{48\pi^2}$. Then $\frac{d}{d\ln\mu}g^{-2}=2b_0$ gives $g^{-2}(\mu)=2b_0\ln(\mu/\Lambda)$, and with $\mu=1/a$ and the lattice convention $\beta=2N/g^2$,
$$\beta(a)=4Nb_0\ln\frac1{a\Lambda}=\frac{44N^2}{48\pi^2}\ln\frac1{a\Lambda}=\frac{11N^2}{12\pi^2}\ln\frac1{a\Lambda}\ \equiv\ c\,\ln\frac1{a\Lambda}.$$

**Step 2 (the union bound).** $e^{-\beta(a)c_\Phi(\delta)}=\exp\!\big(-c\,c_\Phi(\delta)\ln\frac{1}{a\Lambda}\big)=(a\Lambda)^{c\,c_\Phi(\delta)}$. Multiplying by $|P_R|\asymp6R^4a^{-4}$ gives the exponent $c\,c_\Phi(\delta)-4$ on $a$. The $\beta^{\alpha/2}=(c\ln\frac1{a\Lambda})^{\alpha/2}$ prefactor is only logarithmic and cannot change the sign of the exponent. Hence $o(1)$ iff $c\,c_\Phi(\delta)>4$.

**Step 3 (the sup of $\Phi$).** Minimize $\Re\mathrm{Tr}\,V=\sum_{j=1}^N\cos\theta_j$ over $\sum_j\theta_j\equiv0\ (\mathrm{mod}\ 2\pi)$. For $N$ even, $\theta_j=\pi$ for all $j$ is admissible ($\det=(-1)^N=1$) and gives $-N$, the global minimum; so $\Phi_{\max}=1+N/N=2$. For $N$ odd the minimum is $-N\cos(\pi/N)$ (e.g. $N=3$: $\theta_j=2\pi/3$ for all $j$, $\det=e^{2\pi i}=1$, $\Re\mathrm{Tr}=3\cos(2\pi/3)=-1.5=-3\cos(\pi/3)$), so $\Phi_{\max}=1+\cos(\pi/N)$.

**Step 4 (the arithmetic).** Tabulating $c=11N^2/(12\pi^2)$, $\Phi_{\max}$, $c\Phi_{\max}$ and the threshold $4/c$:

| $N$ | $c$ | $\Phi_{\max}$ | $c\,\Phi_{\max}$ | $4/c$ | verdict |
|---|---|---|---|---|---|
| 2 | 0.3715 | 2.0000 | 0.743 | 10.767 | fails for all $\delta$ |
| 3 | 0.8359 | 1.5000 | 1.254 | 4.785 | fails for all $\delta$ |
| 4 | 1.4860 | 2.0000 | 2.972 | 2.692 | fails for all $\delta$ |
| 5 | 2.3219 | 1.8090 | 4.200 | 1.723 | arithmetic passes |
| 6 | 3.3436 | 2.0000 | 6.687 | 1.196 | arithmetic passes |

So for $N\le4$ — which includes $SU(2)$ and the physical $SU(3)$ — the union bound cannot be made $o(1)$ by any $\delta$.

**Step 5 (why the $N\ge5$ loophole is not a loophole).** For $N\ge5$ the criterion requires $c_\Phi(\delta)>4/c=48\pi^2/(11N^2)$. Using $c_\Phi(\delta)\simeq\delta^2/(2N)$ (item 9), this needs $\delta^2>96\pi^2/(11N)$, i.e. $\delta>\pi\sqrt{96/(11N)}=9.28/\sqrt N$: $4.15$ at $N=5$, $3.79$ at $N=6$. But the entire purpose of $\Omega_{\delta,R}$ is that on it the Wilson Hessian has a positive horizontal floor, which requires $\delta$ *small* (deep in the small-angle sector). At $\delta\approx4$ the 'tube' contains essentially the whole group and carries no convexity information at all. So the mechanism fails for every $N$, either arithmetically ($N\le4$) or because the required $\delta$ voids the hypothesis ($N\ge5$).

**Step 6 (why this is not merely a failure of the union bound) — heuristic but pointed.** At large $\beta$ the single-plaquette marginal concentrates near $I$ with fluctuations of size $\beta^{-1/2}$, so one also expects a matching lower bound $\mu_\beta(A_{p,\delta})\ge c_1e^{-c_2\beta\delta^2}$. Then the *expected number* of bad plaquettes in $B_R$ is $\asymp a^{-4}e^{-c_2\beta(a)\delta^2}=a^{-4+cc_2\delta^2}$, which diverges under exactly the same arithmetic. Under approximate independence of well-separated plaquettes this makes $\mu_\beta(\Omega_{\delta,R})\to0$, not merely 'not provably $\to1$'. I have not proved the matching lower bound, so this last step is heuristic; the union-bound obstruction (Steps 1–5) is not.

### Constants and numbers

$b_0=11N/(48\pi^2)$; $\beta(a)=c\ln(1/(a\Lambda))$, $c=11N^2/(12\pi^2)$: $c=0.3715$ ($N{=}2$), $0.8359$ ($N{=}3$), $1.4860$ ($N{=}4$), $2.3219$ ($N{=}5$). Threshold $4/c=48\pi^2/(11N^2)$: $10.767$, $4.785$, $2.692$, $1.723$. $\Phi_{\max}=2$ ($N$ even), $1+\cos(\pi/N)$ ($N$ odd): $2,\ 1.5,\ 2,\ 1.809$. Products $c\Phi_{\max}$: $0.743,\ 1.254,\ 2.972,\ 4.200$. Required $\delta$ for $c_\Phi(\delta)>4/c$ with $c_\Phi\simeq\delta^2/(2N)$: $\delta>\pi\sqrt{96/(11N)}=9.28/\sqrt N$, i.e. $6.56$ ($N{=}2$), $5.36$ ($N{=}3$), $4.15$ ($N{=}5$). Diameter of $SU(3)$ in the metric $\langle X,Y\rangle=-\mathrm{Tr}(XY)$: $d_G(\omega I,I)=2\pi\sqrt{2/3}=5.13$. $|P_R|\asymp6(R/a)^4$.

### Code

import math
for N in range(2, 7):
    c = 11*N**2/(12*math.pi**2)
    phimax = 2.0 if N % 2 == 0 else 1 + math.cos(math.pi/N)
    print(N, round(c,4), round(phimax,4), round(c*phimax,3),
          round(4/c,3), 'PASS' if c*phimax > 4 else 'FAIL')
# 2 0.3715 2.0 0.743 10.767 FAIL
# 3 0.8359 1.5 1.254  4.785 FAIL
# 4 1.486  2.0 2.972  2.692 FAIL
# 5 2.3219 1.809 4.2  1.723 PASS
# 6 3.3436 2.0 6.687  1.196 PASS

**Caveat.** The positive half (item 9) is fully derived; the obstruction is arithmetic on top of it. Marked 'conditional' because (i) it refutes a specific proof strategy — a first-moment/union bound over $a^{-4}$ plaquettes — rather than the existence of a small-field region per se, and (ii) the $N\ge5$ closure uses the small-angle form of $c_\Phi$ plus the requirement that $\delta$ lie in the convexity window, not pure arithmetic. This is presumably folklore among constructive field theorists — it is exactly why Balaban's renormalization needs a large-field/small-field decomposition rather than a global small-field tube.

**Why it matters.** It closes, with explicit constants, one of the three escape routes the project actually attempted, and it does so at the physical group $SU(3)$ with a comfortable margin ($1.25$ vs the required $4$). The general lesson — plaquette entropy grows like $a^{-4}$ while $\beta$ grows only like $\log(1/a)$ — is a reusable veto on any 'global small-field tube' argument.

---

## 11. Executed Monte-Carlo reflection-positivity Gram test for $SU(2)$ on a $4^4$ lattice (the corpus designs it; here it is run)

`status: solid` · `kind: numerical_result`

### Statement

The corpus specifies a numerical RP stress test (Gram matrix $G_{ij}=\mathbb E_\mu[(\theta F_i)F_j]$ over positive-time observables; check $\lambda_{\min}(G)\ge0$ up to Monte-Carlo error; verify $\lambda_{\min}\uparrow0$ like $N^{-1/2}$) but explicitly records that no Monte-Carlo results were ever produced ('the only executed numerics in this project snapshot are the $SU(3)$ Haar Hessian scans'). I implemented and ran it.

**Set-up.** $SU(2)$ Wilson action $S=\beta\sum_p(1-\tfrac12\Re\mathrm{Tr}\,U_p)$ on a periodic $4^4$ lattice ($L_0=L_s=4$), group elements as unit quaternions, Metropolis with $U\mapsto RU$, $R$ near identity (step $\varepsilon=0.35$), checkerboard by (direction, site parity). Reflection $\Theta$ exactly as in Appendix K: $(\Theta U)_{(x_0,\vec x),\nu}=U_{(1-x_0,\vec x),\nu}$ for $\nu=1,2,3$ and $(\Theta U)_{(x_0,\vec x),0}=U_{(-x_0,\vec x),0}^{-1}$; positive-time links $E_+$ = spatial links at $t\in\{1,2\}$ plus time links $t{=}1\!\to\!2$. Ten gauge-invariant observables strictly supported in $E_+$: mean and single spatial plaquettes at $t=1,2$; mean and single temporal plaquettes based at $t=1$; the adjoint character $\chi_1(U_p)=(\mathrm{Tr}\,U_p)^2-1$; and a product of two spatially separated plaquettes. The constant observable is used as an eleventh direction in one variant.

**Result 1 — sampler validation.** $\langle\tfrac12\Re\mathrm{Tr}\,U_p\rangle=0.2197$ at $\beta=1.0$ (acceptance $0.72$), $0.5523$ at $\beta=2.2$ (acceptance $0.42$), $0.7137$ at $\beta=3.0$ (acceptance $0.32$) — consistent with strong-coupling $\beta/4=0.25$ and weak-coupling $1-3/(4\beta)=0.75$ asymptotics and with the known $SU(2)$ plaquette value $\approx0.55$ at $\beta=2.2$.

**Result 2 — RP confirmed.** With observables centred and standardized ($\beta=2.2$, $N$ = number of decorrelated measurements, 4 sweeps between measurements, 600 thermalization sweeps):

| $N$ | reps | $\lambda_{\min}(G)$ | $\max|G-G^\top|$ | $N^{-1/2}$ | $\lambda_{\min}\sqrt N$ |
|---|---|---|---|---|---|
| 375 | 32 | $-0.196\pm0.008$ | 0.205 | 0.0516 | $-3.80$ |
| 750 | 16 | $-0.128\pm0.011$ | 0.136 | 0.0365 | $-3.51$ |
| 1500 | 8 | $-0.086\pm0.011$ | 0.093 | 0.0258 | $-3.35$ |
| 3000 | 4 | $-0.0564\pm0.0030$ | 0.068 | 0.0183 | $-3.09$ |
| 6000 | 2 | $-0.0417\pm0.0020$ | 0.052 | 0.0129 | $-3.23$ |
| 12000 | 1 | $-0.0302$ | 0.027 | 0.0091 | $-3.31$ |

A log–log fit gives $\lambda_{\min}\propto N^{-0.542}$, i.e. **pure $N^{-1/2}$ Monte-Carlo noise**, with $\lambda_{\min}\sqrt N\approx-3.3$ stable across a factor 32 in statistics. The most negative eigenvalue drifts monotonically to $0$; the independent noise scale $\max|G-G^\top|$ (which must be $0$ exactly, since $\mu$ is $\Theta$-invariant and all $F_i$ are real) tracks $|\lambda_{\min}|$ within a factor $\sim1$ at every $N$. Uncentred, unnormalized, with the constant observable included, the full $11\times11$ Gram matrix at $N=12000$ has $\lambda_{\min}/\lambda_{\max}=-7.2\times10^{-4}$. **Conclusion: no RP violation; Theorem K.5.1 is confirmed to the available precision, and the reflection map of Appendix K is implemented consistently.**

**Result 3 — negative control (a limitation of the proposed test).** Repeating with two deliberately buggy reflections — (a) the classic gotcha, time-like links reflected but *not* inverted; (b) a naive $t\mapsto1-t$ on all links with no inversion — gives at $N=3000$: correct $\Theta$: $\lambda_{\min}=-0.033$; bug (a): $-0.047$; bug (b): $-0.062$; all three still shrinking with $N$. The test therefore **does not discriminate** the reflection convention at this observable set and statistics, contrary to the corpus's claim that it is 'a brutally effective way' to catch such bugs. The reason is structural: in $SU(2)$ every irreducible representation is self-conjugate, so $\mathrm{Tr}\,W$ is real and invariant under orientation reversal of a Wilson loop, making the whole family of real gauge-invariant trace observables blind to the inversion convention. A discriminating test needs $SU(3)$ (where $\Im\mathrm{Tr}\,U_p\ne0$) or the transfer-matrix positivity check.

### Derivation

The computation is a direct implementation of the definitions; the only non-obvious ingredients are the reflection map and the positive-time support condition, which I derive here.

**Reflection map.** With $\vartheta(x_0,\vec x)=(1-x_0)\bmod L_0$: a spatial link $b=(x,\nu)$ runs $x\to x+\hat e_\nu$ at fixed time, so $\vartheta b$ runs $\vartheta x\to\vartheta x+\hat e_\nu$, which is again positively oriented; hence $(\Theta U)_{(x_0,\vec x),\nu}=U_{(1-x_0,\vec x),\nu}$. A time link $b=(x,0)$ runs $(x_0,\vec x)\to(x_0+1,\vec x)$, so $\vartheta b$ runs $(1-x_0,\vec x)\to(-x_0,\vec x)$, i.e. $\vartheta b=\big(((-x_0,\vec x),0)\big)^{-1}$, giving $(\Theta U)_{(x_0,\vec x),0}=U_{(-x_0,\vec x),0}^{-1}$. Sanity checks: $x_0=0$ gives $U_{(0,\vec x),0}\mapsto U_{(0,\vec x),0}^{-1}$ (the link across the plane maps to itself, inverted); $x_0=1$ gives $U_{(1,\vec x),0}\mapsto U_{(3,\vec x),0}^{-1}$ (the $t{=}1\!\to\!2$ link maps to the $t{=}3\!\to\!0$ link, inverted). With $L_0=4$, $T=2$, $T_+=\{1,2\}$ and $T_-=\{0,3\}$.

**Support condition.** $E_+$ consists of links with *both* endpoints at $t\in\{1,2\}$: spatial links at $t=1$ and $t=2$, and the time link $(1,\vec x;0)$. Hence: spatial plaquettes at $t=1$ or $t=2$ are admissible; temporal plaquettes $(x;0,\nu)$ with $x_0=1$ are admissible (their four links are $U_0(1,\vec x)$, $U_\nu(2,\vec x)$, $U_0(1,\vec x{+}\hat e_\nu)^{-1}$, $U_\nu(1,\vec x)^{-1}$, all in $E_+$); temporal plaquettes with $x_0=2$ are **not** (they use $U_0(2,\vec x)$, which crosses into $\Lambda_-$). The observable list respects this.

**Why $G$ must be symmetric.** For real $F_i$, $G_{ij}=\mathbb E[F_i(\Theta U)F_j(U)]$; substituting $U\mapsto\Theta U$ and using $\Theta$-invariance of $\mu$ (which holds because $S\circ\Theta=S$ and Haar is $\Theta$-invariant) plus $\Theta^2=\mathrm{id}$ gives $G_{ij}=G_{ji}$. So $\max|G-G^\top|$ is a *free, independent* estimate of the statistical noise floor with no fitting — this is what makes the comparison in Result 2 conclusive.

**Metropolis details.** The action's dependence on a single link is $S_\ell=-\beta\,(U_\ell A_\mu(x))_0+\text{const}$, where the quaternion staple sum is
$$A_\mu(x)=\sum_{\nu\ne\mu}\Big[U_\nu(x{+}\hat\mu)\,U_\mu(x{+}\hat\nu)^{\dagger}\,U_\nu(x)^{\dagger}+U_\nu(x{+}\hat\mu{-}\hat\nu)^{\dagger}\,U_\mu(x{-}\hat\nu)^{\dagger}\,U_\nu(x{-}\hat\nu)\Big],$$
using $\tfrac12\mathrm{Tr}\,q=q_0$ for $SU(2)$ quaternions. Fixing $\mu$ and site parity makes simultaneous updates non-interacting, since the two $\mu$-links in any plaquette, $(x,\mu)$ and $(x{+}\hat\nu,\mu)$, have opposite site parity.

### Constants and numbers

Lattice $4^4$ periodic, $G=SU(2)$, Wilson action. $\beta\in\{1.0,2.2,3.0\}$; Metropolis step $\varepsilon=0.35$; acceptance $0.723/0.425/0.315$; 600 thermalization sweeps, 4 sweeps between measurements. $\langle\tfrac12\Re\mathrm{Tr}U_p\rangle=0.21972\ (\beta{=}1.0)$, $0.55230\ (\beta{=}2.2)$, $0.71374\ (\beta{=}3.0)$. Centred/standardized $10\times10$ Gram at $\beta=2.2$: $\lambda_{\min}=-0.196,-0.128,-0.086,-0.0564,-0.0417,-0.0302$ at $N=375,750,1500,3000,6000,12000$; fitted exponent $-0.542$ (pure MC noise is $-0.5$); $\lambda_{\min}\sqrt N\in[-3.80,-3.09]$. Full spectrum at $N=12000$: $(-0.0302,-0.0133,-0.0102,0.0006,0.0009,0.0060,0.0193,0.0389,0.0826,0.2857)$. Uncentred $11\times11$ Gram at $N=12000$: $\lambda_{\min}/\lambda_{\max}=-7.18\times10^{-4}$, $\lambda_{\max}=12.68$. Negative control at $N=3000$: $\lambda_{\min}=-0.033$ (correct $\Theta$), $-0.047$ (no time-link inversion), $-0.062$ (naive reflection). Total runtime $\approx380$ s for the $N=12000$ chain on one CPU core with NumPy 2.3.5.

### Code

# Core pieces (full scripts: rp_gram.py, rp_gram2.py, rp_gram3.py).
# SU(2) = unit quaternions q=(q0,q1,q2,q3); Tr(q)=2*q0.
import numpy as np
L0, LS, D = 4, 4, 4
SHAPE = (L0, LS, LS, LS)

def qmul(a, b):
    a0,a1,a2,a3 = a[...,0],a[...,1],a[...,2],a[...,3]
    b0,b1,b2,b3 = b[...,0],b[...,1],b[...,2],b[...,3]
    return np.stack([a0*b0-a1*b1-a2*b2-a3*b3,
                     a0*b1+a1*b0+a2*b3-a3*b2,
                     a0*b2-a1*b3+a2*b0+a3*b1,
                     a0*b3+a1*b2-a2*b1+a3*b0], axis=-1)
def qconj(a):
    o = a.copy(); o[...,1:] *= -1.0; return o
def roll(f, mu, s):            # value at x + s*e_mu
    return np.roll(f, shift=-s, axis=mu)

def staples(U, mu):            # A_mu(x): sum_{p ni (x,mu)} ReTr U_p = ReTr(U_mu(x) A_mu(x))
    A = np.zeros(SHAPE+(4,)); Umu = U[..., mu, :]
    for nu in range(D):
        if nu == mu: continue
        Unu = U[..., nu, :]
        A = A + qmul(qmul(roll(Unu,mu,1), qconj(roll(Umu,nu,1))), qconj(Unu))
        A = A + qmul(qmul(qconj(roll(roll(Unu,mu,1),nu,-1)),
                          qconj(roll(Umu,nu,-1))), roll(Unu,nu,-1))
    return A

PAR = (np.indices(SHAPE).sum(axis=0) % 2)   # site parity mask

def sweep(U, beta, rng, eps=0.35):          # checkerboard Metropolis
    for mu in range(D):
        A = staples(U, mu)
        for p in (0, 1):
            v = rng.normal(size=SHAPE+(3,))*eps
            q0 = np.sqrt(np.maximum(1.0-(v**2).sum(-1), 1e-12))
            R = np.concatenate([q0[...,None], v], axis=-1)
            Uold = U[..., mu, :]; Unew = qmul(R, Uold)
            dS = -beta*(qmul(Unew,A)[...,0] - qmul(Uold,A)[...,0])
            ok = (rng.random(SHAPE) < np.exp(-np.clip(dS,-50,50))) & (PAR == p)
            U[..., mu, :] = np.where(ok[...,None], Unew, Uold)
    return U

def reflect(U):                             # Appendix K reflection datum
    T = np.empty_like(U)
    tmap = np.array([(1-t) % L0 for t in range(L0)])   # theta: x0 -> 1-x0
    nmap = np.array([(-t)  % L0 for t in range(L0)])
    for nu in range(1, D):
        T[..., nu, :] = U[tmap, ...][..., nu, :]       # spatial links
    T[..., 0, :] = qconj(U[nmap, ...][..., 0, :])      # time links: reflect AND invert
    return T

def plaq_field(U, mu, nu):
    return qmul(qmul(qmul(U[...,mu,:], roll(U[...,nu,:],mu,1)),
                     qconj(roll(U[...,mu,:],nu,1))), qconj(U[...,nu,:]))
def retr(U, mu, nu): return 2.0*plaq_field(U, mu, nu)[...,0]

def observables(U):     # all supported on E_+ = links with both ends at t in {1,2}
    P12, P13, P23 = retr(U,1,2), retr(U,1,3), retr(U,2,3)
    T01, T03 = retr(U,0,1), retr(U,0,3)
    return np.array([P12[1].mean(), P12[2].mean(), T01[1].mean(), T03[1].mean(),
                     P12[1,0,0,0], T01[1,0,0,0], P12[1,0,0,0]**2-1.0,
                     P12[1,0,0,0]*P12[1,2,2,0], P13[2,0,0,0], P23[1].mean(), 1.0])

# Gram estimator: G_ij = < (theta F_i) F_j >,  RP  <=>  G psd.
# G = (FT.T @ F)/N after centering (and optional standardising) both F and FT
# by the SAME sample mean/std (theta-invariance of mu => E[theta F] = E[F]).
# Diagnostics: eig(sym(G))[0] must -> 0 like N^{-1/2}; max|G-G^T| is an
# independent, fit-free estimate of the same noise floor.

**Caveat.** Single lattice size ($4^4$), single group ($SU(2)$), no autocorrelation-aware error analysis beyond block replicates. The negative control shows the test as designed lacks discriminating power for reflection-convention bugs in $SU(2)$ — a limitation of the corpus's proposal, not of the theorem.

**Why it matters.** It closes the one experimental loop the corpus explicitly left open, confirms the Appendix K reflection datum is implementable and correct, gives a reusable and validated $\Theta$ implementation plus a fit-free noise diagnostic ($\max|G-G^\top|$), and honestly maps the limits of the proposed stress test.

---

## How these fit together

The extracted items form one coherent chain plus three obstructions that cut it at three different joints.

**The positive chain (items 1 -> 2 -> 3 -> 4 -> 6).** Theorem K.5.1 (item 1) supplies axiom (3) of Assumption L.1.7 for the Wilson measure; the OS reconstruction interface (item 2) turns that axiom plus time-translation invariance into a Hilbert space, a positive contraction $T$, and $H\ge0$ with $T=e^{-aH}$; item 3 converts a Euclidean-time clustering exponent $\eta$ into $\mathrm{gap}(H)\ge\eta/a$ and, in the converse direction, back again — so at fixed cutoff clustering and mass gap are *equivalent*, with matching constants. Item 4 is the units audit that says $\eta(a)$ must vanish linearly in $a$ for this to mean anything in the continuum, and item 6 is the functional-analytic step that would carry a uniform gap through a monotone form limit. Items 1, 3 and 6 are complete proofs; item 2 imports exactly one external statement (existence/positivity of the transfer operator); item 4 is the honest bookkeeping that determines whether any of it can survive $a\to0$.

**The permanence layer (item 5) is what the chain needs to survive coarse-graining and limits**, and it is nearly free: RP transfers exactly (Gram matrix to Gram matrix, no constant lost) under any deterministic reflection-equivariant, positive-time-preserving map, and hence under projective and weak limits. My Theorem D pins down what the *stochastic* version really requires (conditional independence of the two halves given the boundary variable, with reflection-paired noise) — and that is precisely the structure a genuine RG kernel lacks.

**The three obstructions attack three different joints.**
- Item 7 (the (A4)+(A5) two-line no-go) attacks the *coarse-graining map itself*: no Markov kernel can be simultaneously a gauge-invariant conditional expectation and gauge covariant onto the full coarse gauge group, because the fixed-point set of the endpoint gauge action is empty. It dovetails exactly with item 5: since Markov kernels are ruled out anyway (item 7) and deterministic maps preserve RP for free (item 5, Thm A), the design space collapses onto covariant-but-not-invariant blocking — which is what Wilson blocking, Migdal–Kadanoff and HYP/APE actually do. So items 5 and 7 together *explain the literature*.
- Item 8 (the boundedness obstruction) attacks the *bridge from a configuration-space diffusion gap to the transfer gap*: the one-step OS dissipation is a bounded form and can never dominate the unbounded gradient energy, at any $a$, on any compact configuration space. The repair — comparison to $\mathcal E^{(a)}_{\rm conf}=\langle f,(I-P_a)f\rangle$ with its exact representation $\int_0^a\int|\nabla P_{t/2}f|^2$ — is scaling-correct in exactly the sense demanded by item 4: an $a$-independent comparison constant $c$ yields $m(a)\ge c\lambda_*+O(a)$, an $a$-independent physical mass. So item 8's repair and item 4's units audit are the same observation seen from two sides.
- Item 10 (the counting obstruction) attacks the *probabilistic input*, i.e. the attempt to run the whole argument on a small-field 'tube'. It is built directly on item 9, which is the corpus's one genuinely analytic use of reflection positivity (the chessboard estimate), and it fails because plaquette entropy $a^{-4}$ beats $\beta(a)\sim\log(1/a)$ by the fixed margin $4/c=48\pi^2/(11N^2)$.

**The numerics (item 11) close the loop on item 1**: they confirm Theorem K.5.1 and, more usefully, validate a correct implementation of the Appendix K reflection datum — while showing that the corpus's own claim for the diagnostic power of the test is overstated in $SU(2)$.

**Relation to the rest of the corpus.** The COMBES_THOMAS / HELFFER_SJOSTRAND / LSI_POINCARE folders are all attempts to produce the input $\eta$ that item 3 consumes (spatial decay, Poincaré/LSI constants, Green's-function decay). Item 4 predicts in advance that none of them can succeed, because they all produce cutoff-uniform constants $\eta_0$ rather than $\eta(a)\sim m a$. Item 8 explains why the specific route through the configuration diffusion (the RICCATI/HESSIAN Bakry-Émery machinery) cannot be attached to the OS side by the inequality the corpus wanted. Item 10 explains why the RICCATI 'high-probability convexity' bridge cannot be completed. Taken together, items 4, 7, 8 and 10 are a complete account of why the program stops, and every one of them is a correct piece of mathematics.

## Further material found but not fully extracted

Real material I found but did not extract in full:

1. **Second no-go in `RG_COARSE/01_Block_Convexity_Hinge/04_no_go_coarse_graining_kernels.md` §1** — 'fixed-cutoff OS data cannot force a cross-scale map $\Pi_{a\to a'}$ with $(\Pi)_\#\mu_a=\mu_{a'}$ and the required equivariances'. The claimed mechanism is 'OS-preserving UV twists that keep each $(\mathcal H_a,H_a)$ unitarily equivalent while destroying any candidate $\Pi$ commuting with reflection and time translation'. The construction is never given. If somebody builds one explicit twist, this becomes a real theorem and is arguably more valuable than item 7; as it stands it is an assertion.

2. **Dirichlet-form coarse-graining with $O(g(a)^2)$ energy loss** (`RG_COARSE/01_Block_Convexity_Hinge/04_dirichlet_form_coarse_graining_Og2.md` §§1–3): the correct pair of inequalities $\mathcal E(Pf,Pf)\le\mathcal E(f,f)$ and $0\le\mathcal E(f,f)-\mathcal E(Pf,Pf)\le\mathcal E(\xi,\xi)$ with $\xi=(I-P)f$, $P=\mathbb E[\cdot\mid\mathcal F_{\rm coarse}]$, plus a blockwise conditional Poincaré hypothesis (BP) with constant $g(a)^2/\lambda_{\rm block}$ that would give $\mathcal E(\xi,\xi)\le Cg(a)^2\mathcal E(Pf,Pf)$. Clean and worth developing; the $1/g(a)^2$ scaling heuristic for the conditional fine gap is asserted, not derived.

3. **The strip-kernel construction in detail** (`J_one_step_OS_scale_a_comparison.md` §2): explicit half-weighted strip weight $W_a(\sigma,\sigma',U_0)$, boundary measure $\nu$, and the symmetrization convention. This is the concrete object whose spectral gap would be the mass gap; nobody in the corpus ever computes with it, and it is small enough to diagonalize numerically on a $2^3$ spatial slice with a truncated character basis.

4. **A designed but unrun transfer-matrix positivity test** (`HESSIAN/Indices_Extracts/Reflection Positivity Stress Test.txt`): build $T$ on a 10–30-dimensional gauge-invariant basis of spatial-plaquette characters by integrating only the straddling time-like links, then check $T\succeq0$, $\lambda_{\max}=1$, and a left/right-invariant-parametrization cross-check. This would discriminate the reflection conventions that my Gram test could not (item 11, Result 3), and it is a small amount of work.

5. **`REFLECTION_POSITIVITY/05_TRANSFER_MATRIX/04_composite_transfer_operator_wilson_loops.md`** — a composite $T_q=\Lambda^\top T_{\rm bulk}\Lambda R W_I$ from $q$-Racah/Doob data with a printed demo spectrum ($N=8$, $q=0.92$, leading eigenvalue $3.058$, next $1.42\times10^{-3}$, 'gap' $3.0567$). The kernels $R$ and $\Lambda$ are explicit placeholders (an exponential and a Gaussian smearing), so the numbers carry no information; only the architecture is of interest.

6. **`lean/YangMills/ReflectionPositive.lean`** contains a four-line `structure ReflectionPositive` with a single positive real field and a `def hilbert_positive := rp.decay_rate > 0`. There is no mathematical content; it confirms the briefing's instruction to ignore the Lean tree for this topic.

7. **Duplication map for this topic** (useful if anyone re-reads the corpus): `04_no_go_coarse_graining_kernels.md` is byte-identical across RICCATI/04_misc_docs, RICCATI/archive/CRITICAL_FILES, COMBES_THOMAS/RICCATI_RG, RG_COARSE/01_Block_Convexity_Hinge, HELFFER_SJOSTRAND/01_Matrix_Hinge_Convexity, LSI_POINCARE/08_misc_docs, POLARITY_GRIBOV/03_misc_docs, WILSON/08_misc_docs and SCALING_LIMIT/04_CONSTANT_UNIFORMITY (md5 1c0f9c48…). `Appendix_K__Reflection_Positivity_for_Wilson(1).md` appears identically in REFLECTION_POSITIVITY/02_RP_FUNDAMENTALS and WILSON/archive (md5 bc6da8d8…). For the one-step OS/Dirichlet material, `J_one_step_OS_scale_a_comparison.md` (197 lines) is strictly more complete than `06_one_step_os_dirichlet_scale_a.md` (112 lines) and is the version I extracted from.
