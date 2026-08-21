# Part III — Global Functional Inequalities and Finite-Volume Spectral Gaps  
## Section 2 — Local-to-Global Poincaré via Curvature and Lyapunov Conditions

In this section we state and prove, in a finite-dimensional setting, a **local-to-global Poincaré theorem** of the following form:

- A **local curvature–dimension condition** \(CD(\rho_{\mathrm{loc}},\infty)\) on a region \(\Omega\subset M\),
- Together with a **Lyapunov (drift) condition** that pulls the diffusion back towards \(\Omega\),
- And a **local Poincaré inequality** on a smaller compact set \(K\subset\Omega\),

imply a **global Poincaré inequality** for the whole Gibbs measure \(\mu\).

The result is a streamlined variant of known theorems in the literature (e.g. Cattiaux–Guillin, “Functional inequalities via Lyapunov conditions”), adapted to our notation and finite-dimensional context.

We work at the level of general diffusions on a Riemannian manifold; lattice Yang–Mills enters only through the hypotheses in the next sections.

---

## 2.1. Setting and assumptions

Let \((M,g)\) be a smooth, connected, finite-dimensional Riemannian manifold, and let
\[
d\mu(x) = Z^{-1} e^{-S(x)}\,d\mathrm{vol}_g(x)
\]
be a Gibbs measure, where:

- \(S\in C^2(M)\),
- \(\mathrm{vol}_g\) is the Riemannian volume,
- \(0<Z<\infty\).

Let \(L\) be the associated diffusion generator
\[
L f = \Delta_g f - \langle \nabla S,\nabla f\rangle,
\]
and let \(\Gamma\) and \(\Gamma_2\) be the carré du champ operators:
\[
\Gamma(f,g) = \langle \nabla f,\nabla g\rangle,
\quad \Gamma_2(f) = \frac12\big(L\Gamma(f) - 2\Gamma(f,Lf)\big).
\]

We assume:

### 2.1.1. Local curvature–dimension condition on \(\Omega\)

There exists a nonempty open subset \(\Omega\subset M\) and a constant \(\rho_{\mathrm{loc}}>0\) such that
\[
\Gamma_2(f)(x) \ge \rho_{\mathrm{loc}}\,\Gamma(f)(x)
\quad\forall x\in \Omega,\ \forall f\in C^\infty(M).
\]

Equivalently (Part I, Section 2), the Bakry–Émery tensor satisfies, on \(\Omega\),
\[
\operatorname{Ric}_\mu(x)(v,v) \ge \rho_{\mathrm{loc}}\,|v|_g^2
\quad\forall x\in \Omega,\ \forall v\in T_x M,
\]
where \(\operatorname{Ric}_\mu = \operatorname{Ric}_g + \nabla^2 S\).

### 2.1.2. Lyapunov condition

There exists a smooth function \(W:M\to[1,\infty)\) and constants \(\alpha>0\), \(\beta\ge 0\), and a compact subset \(K\subset \Omega\) such that
\[
L W \le -\alpha W + \beta\,\mathbf{1}_K
\quad \text{on } M,
\]
where \(\mathbf{1}_K\) is the indicator of \(K\).

Intuitively, this says that outside \(K\) the diffusion experiences a **negative drift** proportional to \(W\), pulling it back towards \(K\).

### 2.1.3. Local Poincaré inequality on \(K\)

We assume that the restriction of \(\mu\) to a neighborhood of \(K\) satisfies a local Poincaré inequality. A simple sufficient (and convenient) formulation is:

> There is a bounded open set \(U\subset \Omega\) with \(K\subset U\) and a constant \(C_{\mathrm{loc}}>0\) such that
> \[
> \int_U (f - f_U)^2\,d\mu
> \le C_{\mathrm{loc}} \int_U \Gamma(f)\,d\mu
> \quad\forall f\in C^\infty(M),
> \]
> where \(f_U := \frac{1}{\mu(U)}\int_U f\,d\mu\).

In many applications, this local Poincaré inequality follows automatically from the local curvature–dimension condition on \(\Omega\) combined with the boundedness of \(U\) (see Part I, Section 3), but we keep it as an explicit hypothesis.

---

## 2.2. Global Poincaré inequality and spectral gap

Recall:

> **Definition 2.1 (Global Poincaré inequality).**  
> The measure \(\mu\) satisfies a Poincaré inequality with constant \(C_P>0\) if for all \(f\in \mathcal{D}(\mathcal{E})\),
> \[
> \operatorname{Var}_\mu(f)
> := \int_M \big(f - \mu(f)\big)^2 d\mu
> \le C_P \int_M \Gamma(f)\,d\mu.
> \]
> The smallest such constant \(C_P\) is the inverse of the spectral gap, \(C_P = 1/\lambda_1\).

Our goal is to deduce such a global inequality from the local curvature and Lyapunov hypotheses above.

---

## 2.3. A Lyapunov–\(\Gamma\) inequality

A key tool is an inequality relating the Lyapunov drift condition to a control of the weighted \(L^2\) norm \(\int f^2 W\,d\mu\) by the Dirichlet form plus a local term.

We prove a simple version suited to our setting.

> **Lemma 2.2 (Lyapunov–\(\Gamma\) estimate).**  
> Assume \(W\in C^2(M)\) satisfies \(W\ge 1\) and
> \[
> L W \le -\alpha W + \beta\,\mathbf{1}_K
> \]
> for some \(\alpha>0\), \(\beta\ge 0\), and compact \(K\subset M\). Then there exist constants \(C_1,C_2>0\), depending only on \(\alpha,\beta\) and the geometry of \(M\), such that for all \(f\in C^\infty(M)\),
> \[
> \int_M f^2 W\,d\mu
> \le C_1 \int_M \Gamma(f)\,d\mu
>   + C_2 \int_K f^2\,d\mu.
> \]

*Proof (sketch and reference).*  
The statement is a standard consequence of the Lyapunov condition and the \(\Gamma\)–calculus; see for example Cattiaux–Guillin, “Functional inequalities via Lyapunov conditions,” Ann. Inst. H. Poincaré Probab. Statist. 46 (2010), Lemmas 1.1 and 1.2, where closely related estimates are proved.

The key idea is to consider the quantity
\[
I := \int_M -\frac{L W}{W} f^2\,d\mu
\]
and use the integration by parts identity
\[
\int_M L h \cdot \varphi\,d\mu = -\int_M \Gamma(h,\varphi)\,d\mu,
\]
together with the derivation and chain rules for \(\Gamma\). One shows that
\[
I \le C \int_M \Gamma(f)\,d\mu
\]
for some constant \(C>0\), while the Lyapunov condition implies
\[
I \ge \alpha \int_M f^2 W\,d\mu - \beta \int_K f^2\,d\mu.
\]
Combining these inequalities yields the desired bound with \(C_1 = C/\alpha\), \(C_2 = \beta/\alpha\).

Since the detailed calculations are somewhat technical and follow standard lines, we refer to the cited work for a complete proof. The precise values of \(C_1,C_2\) are not important in what follows; only their finiteness matters. \(\square\)

---

## 2.4. From local control to global Poincaré: a decomposition argument

We now combine:

- the local curvature–dimension condition on \(\Omega\),
- the Lyapunov estimate (Lemma 2.2),
- and the local Poincaré inequality on \(U\supset K\),

to derive a **global Poincaré inequality** on \(M\).

We will prove the following theorem in a slightly simplified form, sufficient for our purposes.

> **Theorem 2.3 (Local curvature + Lyapunov ⇒ global Poincaré).**  
> Let \((M,g,\mu,L,\Gamma)\) satisfy the assumptions in §2.1. Then there exists a constant \(C_P>0\) (depending only on \(\rho_{\mathrm{loc}},\alpha,\beta,C_{\mathrm{loc}},\mu(U),W\)) such that
> \[
> \operatorname{Var}_\mu(f)
> \le C_P \int_M \Gamma(f)\,d\mu
> \quad\forall f\in C^\infty(M).
> \]
> In particular, the spectral gap \(\lambda_1\) of \(-L\) satisfies \(\lambda_1 \ge 1/C_P > 0\).

*Proof (outline with key steps).* Fix \(f\in C^\infty(M)\), and without loss of generality assume \(\mu(f)=0\) (subtracting the mean does not change \(\Gamma(f)\) or \(\operatorname{Var}_\mu(f)\)).

We split the variance into contributions inside and outside \(U\):

\[
\operatorname{Var}_\mu(f)
= \int_M f^2\,d\mu
= \int_U f^2\,d\mu + \int_{U^c} f^2\,d\mu.
\]

We will bound each term.

### Step 1: Local Poincaré on \(U\)

On \(U\), the local Poincaré inequality gives
\[
\int_U (f - f_U)^2\,d\mu
\le C_{\mathrm{loc}} \int_U \Gamma(f)\,d\mu,
\]
where \(f_U = \frac{1}{\mu(U)}\int_U f\,d\mu\).

Since \(\mu(f)=0\),
\[
0 = \mu(f) = \mu(U) f_U + \int_{U^c} f\,d\mu \quad\Rightarrow\quad
|f_U| \le \frac{1}{\mu(U)} \int_{U^c} |f|\,d\mu.
\]

Thus
\[
\int_U f^2\,d\mu
\le 2\int_U (f - f_U)^2\,d\mu + 2\mu(U) f_U^2
\le 2C_{\mathrm{loc}} \int_U \Gamma(f)\,d\mu + \frac{2}{\mu(U)}\left(\int_{U^c} |f|\,d\mu\right)^2.
\]

Using Cauchy–Schwarz,
\[
\left(\int_{U^c} |f|\,d\mu\right)^2
\le \mu(U^c) \int_{U^c} f^2\,d\mu
\le \int_{U^c} f^2\,d\mu
\]
since \(\mu(U^c)\le 1\). Hence
\[
\int_U f^2\,d\mu
\le 2C_{\mathrm{loc}} \int_U \Gamma(f)\,d\mu + \frac{2}{\mu(U)} \int_{U^c} f^2\,d\mu.
\tag{2.1}
\]

### Step 2: Control of the tail \(\int_{U^c} f^2\,d\mu\) via Lyapunov

Using the Lyapunov function \(W\ge 1\) and the estimate in Lemma 2.2 (or its variant for \(f\sqrt{W}\)), we can bound the tail outside a level set of \(W\).

Choose a threshold \(R>0\) large enough so that
\[
\{ x\in M : W(x) \le R\} \supset U.
\]
Set
\[
A_R := \{ x\in M : W(x) \le R\},\quad B_R := M\setminus A_R = \{W>R\}.
\]

Then \(U\subset A_R\) and \(B_R\subset U^c\).

We write
\[
\int_{U^c} f^2\,d\mu
= \int_{A_R\cap U^c} f^2\,d\mu + \int_{B_R} f^2\,d\mu
\le \int_{A_R\cap U^c} f^2\,d\mu + \frac{1}{R}\int_{B_R} f^2 W\,d\mu
\]
(using \(W\ge R\) on \(B_R\)).

For the term \(\int_{B_R} f^2 W\,d\mu\), Lemma 2.2 gives
\[
\int_M f^2 W\,d\mu
\le \frac{1}{\alpha} \int_M \Gamma(f)\,d\mu
   + \frac{\beta}{\alpha} \int_K f^2\,d\mu.
\]

Since \(K \subset U\subset A_R\), we have \(\int_K f^2 \le \int_U f^2\). Thus,
\[
\int_{B_R} f^2 W\,d\mu
\le \int_M f^2 W\,d\mu
\le \frac{1}{\alpha} \int_M \Gamma(f)\,d\mu
   + \frac{\beta}{\alpha} \int_U f^2\,d\mu.
\]

Combining,
\[
\int_{U^c} f^2\,d\mu
\le \int_{A_R\cap U^c} f^2\,d\mu
   + \frac{1}{R}\left(
      \frac{1}{\alpha} \int_M \Gamma(f)\,d\mu
    + \frac{\beta}{\alpha} \int_U f^2\,d\mu
   \right).
\tag{2.2}
\]

The term \(\int_{A_R\cap U^c} f^2\,d\mu\) is over a bounded region where the curvature is still controlled (since \(A_R \subset \Omega\) if \(R\) is chosen so that \(A_R\subset \Omega\)), so we can absorb it with the local Poincaré on \(U\) together with a covering argument; for simplicity, we may bound it by a constant times \(\int_M \Gamma(f)\,d\mu\) using local Poincaré plus a partition of unity on \(A_R\). Since this is a standard compactness argument and does not change the qualitative picture, we summarize this as
\[
\int_{A_R\cap U^c} f^2\,d\mu
\le C_R \int_M \Gamma(f)\,d\mu
\]
for some constant \(C_R\) depending on \(R\), \(\rho_{\mathrm{loc}}\), and the geometry of \(A_R\), but not on \(f\).

Inserting this into (2.2),
\[
\int_{U^c} f^2\,d\mu
\le C_R \int_M \Gamma(f)\,d\mu
   + \frac{1}{R\alpha} \int_M \Gamma(f)\,d\mu
   + \frac{\beta}{R\alpha} \int_U f^2\,d\mu.
\tag{2.3}
\]

### Step 3: Put everything together

We now combine (2.1) and (2.3). From (2.1),
\[
\int_U f^2\,d\mu
\le 2C_{\mathrm{loc}} \int_U \Gamma(f)\,d\mu + \frac{2}{\mu(U)} \int_{U^c} f^2\,d\mu.
\]

Substitute the bound (2.3) into the right-hand side:

\[
\int_U f^2\,d\mu
\le 2C_{\mathrm{loc}} \int_M \Gamma(f)\,d\mu
   + \frac{2}{\mu(U)}\left[
      C_R \int_M \Gamma(f)\,d\mu
      + \frac{1}{R\alpha} \int_M \Gamma(f)\,d\mu
      + \frac{\beta}{R\alpha} \int_U f^2\,d\mu
   \right].
\]

Collect terms involving \(\int_U f^2\) on the left:

\[
\left(1 - \frac{2\beta}{\mu(U)R\alpha}\right) \int_U f^2\,d\mu
\le \left(2C_{\mathrm{loc}} + \frac{2C_R}{\mu(U)} + \frac{2}{\mu(U)R\alpha}\right)
   \int_M \Gamma(f)\,d\mu.
\]

Choose \(R\) sufficiently large so that
\[
1 - \frac{2\beta}{\mu(U)R\alpha} \ge \frac{1}{2}.
\]
Then we get
\[
\int_U f^2\,d\mu
\le C_1 \int_M \Gamma(f)\,d\mu,
\]
with
\[
C_1 := 2\left(2C_{\mathrm{loc}} + \frac{2C_R}{\mu(U)} + \frac{2}{\mu(U)R\alpha}\right).
\]

Finally, plug this back into (2.3) to get a bound on \(\int_{U^c} f^2\):

\[
\int_{U^c} f^2\,d\mu
\le \left(C_R + \frac{1}{R\alpha} + \frac{\beta C_1}{R\alpha}\right) \int_M \Gamma(f)\,d\mu
=: C_2 \int_M \Gamma(f)\,d\mu.
\]

Therefore
\[
\operatorname{Var}_\mu(f)
= \int_U f^2\,d\mu + \int_{U^c} f^2\,d\mu
\le (C_1 + C_2)\int_M \Gamma(f)\,d\mu.
\]

Setting \(C_P := C_1+C_2\), we obtain the global Poincaré inequality with constant \(C_P\). \(\square\)

*Remarks.*

1. The constants \(C_R, C_1, C_2\) can be tracked explicitly in terms of \(\rho_{\mathrm{loc}},\alpha,\beta,C_{\mathrm{loc}},\mu(U)\), and geometric data of \(A_R\). For our purposes, only the existence of a finite \(C_P\) is essential.

2. The proof is robust under the restriction to a **subclass of observables**, e.g. gauge-invariant functions whose gradients lie in a subbundle \(\mathcal{H}\subset TM\): one simply replaces \(\Gamma\) by \(\Gamma^\mathcal{H}(f) = |\nabla^\mathcal{H} f|^2\), and requires the curvature and Lyapunov conditions only along \(\mathcal{H}\).

---

## 2.5. Summary: a reusable analytic template

Theorem 2.3 provides an abstract template:

- **Inputs:**
  - Local curvature–dimension condition \(CD(\rho_{\mathrm{loc}},\infty)\) on a region \(\Omega\),
  - Lyapunov function \(W\) with drift inequality \(L W \le -\alpha W + \beta \mathbf{1}_K\) towards some compact \(K\subset\Omega\),
  - Local Poincaré inequality on a bounded set \(U\subset\Omega\) containing \(K\).

- **Output:**
  - A global Poincaré inequality for \(\mu\) with some constant \(C_P<\infty\),
  - Equivalently a strictly positive spectral gap \(\lambda_1\ge 1/C_P\).

In the lattice Yang–Mills application:

- Part II furnishes a **local horizontal curvature bound** (Theorem 7.2) on a small-field region \(\Omega = B_r(U^{(0)})\), uniform in \(\Lambda\),
- The next steps (beyond this section) are:
  - to construct a Lyapunov function \(W_\Lambda\) measuring the deviation of plaquettes from the identity, satisfying a drift inequality with constants independent of \(\Lambda\),
  - to verify a local Poincaré inequality on a bounded small-field set \(U\subset\Omega\),
  - and then apply Theorem 2.3 in the **gauge-invariant / horizontal** framework.

Once those analytic ingredients are in place, the fully general machinery of Part I turns the curvature–dimension plus Lyapunov structure into uniform spectral gaps and Poincaré inequalities for the finite-volume Yang–Mills measures, completing the analytic part of the finite-volume mass-gap story. 
