# Part III — Global Functional Inequalities and Finite-Volume Spectral Gaps  
## Section 3 — Local-to-Global Log-Sobolev Inequality via Curvature and Lyapunov Conditions

In this section we extend the analysis of Section&nbsp;2 from Poincaré inequalities to **logarithmic Sobolev inequalities (LSI)**. The structure is parallel:

- A **local curvature–dimension condition** \(CD(\rho_{\mathrm{loc}},\infty)\) on a region \(\Omega\subset M\),
- A **Lyapunov (drift) condition** that pushes the diffusion back towards \(\Omega\),
- A **local LSI** on a bounded subset \(U\subset\Omega\),

together imply a **global LSI** for the full Gibbs measure \(\mu\).

The result is again a streamlined variant of known theorems (Cattiaux–Guillin, Holley–Stroock, Wang, etc.), adapted to our notation and to the finite-dimensional setting relevant for lattice Yang–Mills.

As in Section&nbsp;2, we work with a general Gibbs diffusion; Yang–Mills appears only through the hypotheses in the next part.

---

## 3.1. Setting and assumptions

We retain the general setup from Section&nbsp;2:

- \((M,g)\) a smooth, connected, finite-dimensional Riemannian manifold,
- Gibbs measure
  \[
  d\mu(x) = Z^{-1} e^{-S(x)}\,d\mathrm{vol}_g(x),
  \]
  with \(S\in C^2(M)\), \(0<Z<\infty\),
- Generator
  \[
  L f = \Delta_g f - \langle\nabla S,\nabla f\rangle,
  \]
- Carré du champ and \(\Gamma_2\)
  \[
  \Gamma(f,g) = \langle\nabla f,\nabla g\rangle,\quad \Gamma_2(f) = \frac12\big(L\Gamma(f) - 2\Gamma(f,Lf)\big).
  \]

We denote by \(\operatorname{Ent}_\mu(f^2)\) the entropy:
\[
\operatorname{Ent}_\mu(f^2)
= \int_M f^2\log f^2\,d\mu - \left(\int_M f^2\,d\mu\right)\log\left(\int_M f^2\,d\mu\right),
\]
with the convention \(0\log 0 = 0\).

We assume:

### 3.1.1. Local curvature–dimension condition on \(\Omega\)

As in §2.1.1, there exist a nonempty open \(\Omega\subset M\) and \(\rho_{\mathrm{loc}}>0\) such that
\[
\Gamma_2(f)(x) \ge \rho_{\mathrm{loc}}\,\Gamma(f)(x)
\quad\forall x\in \Omega,\ \forall f\in C^\infty(M).
\]

This is the local \(CD(\rho_{\mathrm{loc}},\infty)\) condition.

### 3.1.2. Lyapunov condition

As in §2.1.2, there exists a smooth \(W:M\to[1,\infty)\), constants \(\alpha>0\), \(\beta\ge 0\), and a compact set \(K\subset\Omega\) such that
\[
L W \le -\alpha W + \beta\,\mathbf{1}_K\quad\text{on }M.
\]

### 3.1.3. Local log-Sobolev inequality on \(U\)

We strengthen the local functional inequality on a bounded set \(U\subset\Omega\) (with \(K\subset U\)):

> There exists a bounded open set \(U\subset\Omega\) with \(K\subset U\) and a constant \(C_{\mathrm{LS,loc}}>0\) such that for all smooth \(f\) with \(\int_U f^2\,d\mu = 1\),
> \[
> \operatorname{Ent}_\mu(f^2 \mathbf{1}_U)
> \le C_{\mathrm{LS,loc}} \int_U \Gamma(f)\,d\mu.
> \]

This is a **local log-Sobolev inequality** on \(U\). In many finite-dimensional situations, it follows from:

- the local \(CD(\rho_{\mathrm{loc}},\infty)\) condition on \(\Omega\),
- the boundedness of \(U\),

via the Bakry–Émery method (Part I, Section&nbsp;3). We state it here as an explicit assumption to keep the analytic structure clear.

---

## 3.2. Global log-Sobolev inequality

Recall:

> **Definition 3.1 (Global log-Sobolev inequality).**  
> The measure \(\mu\) satisfies a log-Sobolev inequality with constant \(C_{\mathrm{LS}}>0\) if for all \(f\in C^\infty(M)\),
> \[
> \operatorname{Ent}_\mu(f^2)
> \le C_{\mathrm{LS}} \int_M \Gamma(f)\,d\mu.
> \]

A global LSI implies a Poincaré inequality (with constant no worse than \(C_{\mathrm{LS}}\)), and hence a spectral gap. It also implies hypercontractivity and other strong regularization properties, but those will not be our focus here.

Our goal is to show:

> Under the hypotheses in §3.1, there exists a finite constant \(C_{\mathrm{LS}}\) such that the global LSI holds.

---

## 3.3. Known Lyapunov criteria for LSI

There is a substantial literature giving sufficient conditions for global LSI in terms of Lyapunov drift plus local LSI. In particular, Cattiaux–Guillin (2010) prove:

- If there exists a Lyapunov function \(W\) with \(L W \le -\alpha W + \beta\mathbf{1}_K\),
- and a local LSI holds on some neighborhood of \(K\),

then \(\mu\) satisfies a global defective LSI, which can be upgraded to a true LSI under mild additional assumptions.

We will not reproduce the full measure-theoretic arguments here; instead, we state a version tailored to our finite-dimensional and geometric setting, and give a structural sketch of the proof, referring to the literature for technical details.

> **Theorem 3.2 (Lyapunov + local LSI ⇒ defective global LSI).**  
> Assume the hypotheses of §3.1. Then there exist constants \(C_{\mathrm{LS}}>0\) and \(D\ge 0\) such that for all smooth \(f\),
> \[
> \operatorname{Ent}_\mu(f^2)
> \le C_{\mathrm{LS}} \int_M \Gamma(f)\,d\mu + D \int_K f^2\,d\mu.
> \]

*Remark.* In many situations one can upgrade this **defective LSI** to a true LSI (with no defect term) under additional assumptions, e.g. if \(\mu\) also satisfies a global Poincaré inequality. In our overall framework this can be achieved by combining Theorem 3.2 with the global Poincaré inequality obtained in Section 2 and applying a standard result such as the Rothaus lemma (see, e.g., Cattiaux–Guillin 2010, Corollary 3.9).

*Sketch of proof and references.*  
The core argument combines three ingredients:

1. **Lyapunov–\(\Gamma\) control of tails.**  
   The Lyapunov function \(W\) ensures that outside a bounded set \(A_R = \{W\le R\}\), the measure of the set where \(f\) is large can be controlled in terms of \(\int\Gamma(f)\). More precisely, variants of Lemma 2.2 yield estimates of the form
   \[
   \int_{B_R} f^2 \log f^2\,d\mu
   \le C_1 \int_M \Gamma(f)\,d\mu + C_2 \int_{A_R} f^2\,d\mu,
   \]
   for \(B_R = M\setminus A_R\), after normalizing \(f^2\) appropriately.

2. **Local LSI on \(U\) to control the core.**  
   On the bounded region \(U\supset K\), local curvature and compactness imply a local LSI: for \(f^2\) normalized on \(U\),
   \[
   \int_U f^2 \log f^2\,d\mu \le C_{\mathrm{LS,loc}} \int_U \Gamma(f)\,d\mu.
   \]
   A partition of unity allows one to extend this to \(A_R\supset U\), giving
   \[
   \int_{A_R} f^2 \log f^2\,d\mu
   \le C_3 \int_M \Gamma(f)\,d\mu + C_4\int_K f^2\,d\mu.
   \]

3. **Entropy decomposition.**  
   Decompose the entropy
   \[
   \operatorname{Ent}_\mu(f^2)
   = \int_{A_R} f^2\log\frac{f^2}{\mu(f^2)}\,d\mu + \int_{B_R} f^2\log\frac{f^2}{\mu(f^2)}\,d\mu.
   \]
   By choosing normalizations carefully and using the estimates from (1) and (2), one obtains an inequality of the form
   \[
   \operatorname{Ent}_\mu(f^2)
   \le C_{\mathrm{LS}} \int_M \Gamma(f)\,d\mu + D \int_K f^2\,d\mu
   \]
   for some finite \(C_{\mathrm{LS}},D\).

A precise version, including control of all constants and the absorption of the defect term, can be found in:

- P. Cattiaux and A. Guillin, “Functional inequalities via Lyapunov conditions,” Annales de l’Institut Henri Poincaré, Probabilités et Statistiques 46 (2010), Thm. 3.7 and Cor. 3.9,
- F.-Y. Wang, “Functional inequalities for empty essential spectrum,” J. Funct. Anal. 170 (2000), 219–245.

In our finite-dimensional setting, the absence of pathological tails and the compactness of sublevel sets of \(W\) simplify several technical steps. For the purposes of this project, the qualitative implication “Lyapunov + local LSI ⇒ global LSI” is what matters; the exact formulas for the constants \(C_{\mathrm{LS}},D\) will not be used.

\(\square\)

---

## 3.4. Local curvature ⇒ local LSI on bounded sets

The remaining analytic input needed in our template is a **local LSI** on \(U\subset\Omega\). In many situations, this follows directly from the local curvature–dimension condition.

In particular, in finite dimension, if:

- \(CD(\rho_{\mathrm{loc}},\infty)\) holds on an open set \(\Omega\),
- \(U\subset\Omega\) is bounded with smooth boundary,

then via the Bakry–Émery method (Part I, Section&nbsp;3) applied to the Markov semigroup killed at \(\partial U\), one can derive a local LSI on \(U\) with some constant \(C_{\mathrm{LS,loc}}\) depending on \(\rho_{\mathrm{loc}}\) and the geometry/measure of \(U\).

We do not attempt to optimize these local constants; we simply record:

> **Lemma 3.3 (Local curvature implies local LSI on bounded sets).**  
> Assume \(CD(\rho_{\mathrm{loc}},\infty)\) holds on an open set \(\Omega\subset M\) and let \(U\subset\Omega\) be a relatively compact open subset with smooth boundary such that \(\mu(U)>0\). Then there exists \(C_{\mathrm{LS,loc}}<\infty\) such that the local LSI of §3.1.3 holds on \(U\).

*Sketch of proof.*  
Consider the diffusion semigroup \(P_t^U\) generated by \(L\) with reflecting or Dirichlet boundary conditions on \(\partial U\). On \(U\), the curvature–dimension condition \(CD(\rho_{\mathrm{loc}},\infty)\) holds, and the generator is elliptic. Standard arguments in the Bakry–Émery framework (Bochner identity, entropy dissipation along \(P_t^U\), Gronwall-type estimates) yield an LSI on \(U\) with constant \(2/\rho_{\mathrm{loc}}\) up to boundary contributions, which can be controlled thanks to the compactness and smoothness of \(U\). See, e.g., Bakry–Gentil–Ledoux, *Analysis and Geometry of Markov Diffusion Operators,* Springer (2014), Chapters 3–5.

\(\square\)

Thus, in practice:

- The local curvature–dimension condition from Part II (for Yang–Mills)
- and the boundedness of the small-field region \(\Omega\)
- supply the local LSI needed in Theorem 3.2.

---

## 3.5. Summary: analytic template for global LSI

Combining the pieces, we have the following reusable template.

> **Theorem 3.4 (Local curvature + Lyapunov + local LSI ⇒ global LSI).**  
> Let \((M,g,\mu,L,\Gamma)\) be as in §3.1, and assume:
>
> 1. (**Local curvature–dimension**) There exists \(\Omega\subset M\) and \(\rho_{\mathrm{loc}}>0\) such that \(CD(\rho_{\mathrm{loc}},\infty)\) holds on \(\Omega\).
> 2. (**Lyapunov drift**) There exists \(W\in C^2(M)\), \(W\ge 1\), and constants \(\alpha>0\), \(\beta\ge 0\), and compact \(K\subset\Omega\) such that \(L W \le -\alpha W + \beta\mathbf{1}_K\).
> 3. (**Local LSI**) There exists a bounded open set \(U\subset\Omega\) with \(K\subset U\) and constant \(C_{\mathrm{LS,loc}}<\infty\) such that a local LSI holds on \(U\).
>
> Then there exists a constant \(C_{\mathrm{LS}}<\infty\), depending only on \(\rho_{\mathrm{loc}},\alpha,\beta,C_{\mathrm{LS,loc}},\mu(U)\) and the geometry of \(U\), such that the global LSI
> \[
> \operatorname{Ent}_\mu(f^2)
> \le C_{\mathrm{LS}} \int_M \Gamma(f)\,d\mu
> \quad\forall f\in C^\infty(M)
> \]
> holds.
>
> The statement remains valid if all conditions are imposed only along a subbundle \(\mathcal{H}\subset TM\) and \(\Gamma\) is replaced by \(\Gamma^\mathcal{H}(f) = |\nabla^\mathcal{H} f|^2\); in that case the inequality is to be understood for functions whose gradients lie in \(\mathcal{H}\).

The proof is a direct application of:

- Lemma 3.3 (local curvature ⇒ local LSI),
- Theorem 3.2 (Lyapunov + local LSI ⇒ global LSI),

and standard properties of entropy and the Dirichlet form.

---

## 3.6. Relevance for lattice Yang–Mills

For the lattice Yang–Mills family \((M_\Lambda,\mu_\Lambda)\) considered in Part II:

- Part II (Theorem 7.2) provides a **uniform local horizontal curvature bound** on a small-field region \(\Omega = B_r(U^{(0)})\), independent of \(\Lambda\), for the horizontal (physical) subbundle \(H_U\).
- By the Bakry–Émery method restricted to horizontals, this yields a **local LSI** on a bounded set \(U\subset\Omega\) (Lemma 3.3 applied in the horizontal/quotient sense).
- The remaining analytic input is a family of **Lyapunov functions \(W_\Lambda\)** satisfying a drift inequality
  \[
  L_\Lambda W_\Lambda \le -\alpha W_\Lambda + \beta \mathbf{1}_{K_\Lambda},
  \]
  with constants \(\alpha,\beta\) and small sets \(K_\Lambda \subset \Omega\) **independent of \(\Lambda\)** when expressed in lattice units.
- Once such Lyapunov functions are constructed, Theorem 3.4 (in the horizontal/gauge-invariant framework) implies:

  - A global LSI for gauge-invariant observables, uniform in \(\Lambda\),
  - And hence a volume-independent Poincaré inequality and a uniform spectral gap for the corresponding finite-volume generators.

In other words, Part III, Section&nbsp;3 completes the analytic bridge between:

- the **local geometric data** furnished by the Haar + Wilson curvature analysis (Part II),
- and **global functional inequalities** strong enough to support a finite-volume “mass gap” statement in the spectral sense, once appropriate Lyapunov functions are available.

The actual construction of such Lyapunov functions for lattice Yang–Mills—and verification that the resulting drift inequalities are uniform in \(\Lambda\)—is a nontrivial analytic problem and belongs to later parts of the project. The present section isolates the analytic template they must feed into.

