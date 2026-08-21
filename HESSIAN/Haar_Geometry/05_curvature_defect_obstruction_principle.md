# Curvature-defect rigidity and the obstruction principle
*(Project extraction: “Curvature-Defect Rigidity and the Obstruction Principle” + “Mass gap consequences” + integration with spectral-floor monotonicity)*

## 0. The core speculative mechanism (stated cleanly)
Define an intrinsic notion of “how non-Gaussian” the theory is at scale $a$:

- If the physical Hessian is uniformly stiff everywhere, the measure is strongly log-concave ⇒ strong functional inequalities ⇒ a gap.
- If, as $a\to0$, the stiffness defect collapses to $0$, then the measure becomes asymptotically Gaussian (free field).

So an interacting continuum limit should be obstructed unless a strictly positive defect persists at all small scales, and that persistent defect can be converted into a mass gap.

That is the “obstruction principle.”

This document formalizes the definitions, highlights what must be proved, and points out one place where the draft needs a careful correction (effective actions vs conditional expectations).

---

## 1. Setup and definitions

Let $\mu_a$ be the lattice Euclidean measure at lattice spacing $a$ (finite volume at first).
Let $S_a$ be the corresponding action functional on configuration space $M_a$.

### 1.1 Physical projection
Let $\Pi_{\mathrm{phys}}(U)$ denote an orthogonal projection from tangent space $T_UM_a$ onto “physical directions,” i.e. the complement of gauge directions.

> **Important subtlety:** in a non-Abelian gauge theory the gauge-orbit directions depend on $U$ (through the covariant derivative), so $\Pi_{\mathrm{phys}}$ is generally **$U$-dependent** unless you fix a gauge and work in gauge-fixed coordinates.  
> The draft assumes (or desires) a $U$-independent projection; that can be true in certain gauge-fixed charts, but needs to be made explicit.

Define the **physical Hessian**
\[
H_a^{\mathrm{phys}}(U):=
\Pi_{\mathrm{phys}}(U)\,\nabla^2 S_a(U)\,\Pi_{\mathrm{phys}}(U).
\tag{1.1}
\]

### 1.2 Pointwise curvature defect
Fix a target stiffness $\kappa_*>0$ and define
\[
\delta_a(U):=
\max\Big\{0,\ \kappa_* - \lambda_{\min}\big(H_a^{\mathrm{phys}}(U)\big)\Big\}.
\tag{1.2}
\]

### 1.3 Global curvature defect
Define the scale-dependent defect functional
\[
\Phi(a):=\mathbb E_{\mu_a}\big[\delta_a(U)\big].
\tag{1.3}
\]

Heuristics:
- $\Phi(a)=0$ means “physical Hessian $\ge \kappa_*$ everywhere” (uniform physical convexity).
- $\Phi(a)>0$ measures how much (and how often) the theory has “soft directions.”

---

## 2. The monotonicity dream and what actually needs to be shown

### 2.1 Dream statement (conditioning monotonicity)
If coarse-graining is literally “conditioning on a coarse sigma-algebra,” and if the coarse-scale Hessian were the conditional expectation of the fine Hessian, i.e.
\[
H_{a'}^{\mathrm{phys}} = \mathbb E\big[H_{a}^{\mathrm{phys}}\mid \mathcal G_{a'}\big],
\tag{2.1}
\]
then the conditional spectral-floor lemma implies
\[
\lambda_{\min}(H_{a'}^{\mathrm{phys}})
\ge
\mathbb E[\lambda_{\min}(H_a^{\mathrm{phys}})\mid\mathcal G_{a'}],
\]
and therefore defect is monotone:
\[
\Phi(a')\le \Phi(a)
\qquad (a'<a).
\tag{2.2}
\]

### 2.2 The correction: effective actions are log-integrals
In genuine Wilsonian RG, the coarse effective action is
\[
S_{a'}(U') = -\log\int e^{-S_a(U)}\,\delta(\pi(U)-U')\,dU,
\]
so its Hessian contains **both**:
- an averaged fine Hessian term,
- and a covariance (Fisher information) term coming from the log.

So (2.1) is generally false as an identity.

**But:** the conditional spectral-floor lemma still matters, because it can be used to bound the averaged Hessian term from below, and covariance terms often have a sign. The correct monotonicity statement likely becomes a *one-sided inequality* rather than equality.

---

## 3. Rigidity theorem (Gaussianization when defect → 0)

### Theorem 3.1 (Rigidity, conditional form)
Assume there exists a sequence $a_n\to0$ such that:

1. (Defect collapse) $\Phi(a_n)\to0$.
2. (Uniform cubic remainder control) There exists $C_3$ such that for $\mu_{a_n}$-typical configurations, the Taylor remainder of $S_{a_n}$ around its minimizer is uniformly controlled by $C_3\|h\|^3$ in physical directions.
3. (Covariance convergence) The two-point function converges along $a_n$ to a limiting covariance operator.

Then the continuum limit along $a_n$ is Gaussian (free field), in the sense that all connected $k$-point functions for $k\ge3$ vanish in the limit.

### Proof sketch
If $\Phi(a_n)\to0$, then $\delta_{a_n}(U)$ is small on average, hence (by Markov + concentration) the set where $\lambda_{\min}(H_{a_n}^{\mathrm{phys}})$ dips below $\kappa_*$ has vanishing $\mu_{a_n}$-weight.

Under the cubic remainder bound, a uniformly convex action forces the measure to be close to a Gaussian with covariance given by the inverse Hessian. Covariance convergence then fixes the Gaussian limit.

*(This is the step that wants the most careful functional-analytic work: you need to control higher cumulants using uniform convexity + third derivative bounds.)* ∎

---

## 4. Obstruction principle (interacting ⇒ positive defect ⇒ gap)
Take the contrapositive:

If the continuum limit is **interacting** (nonzero connected 3-point function, or nontrivial beta function, etc.), then defect cannot collapse:
\[
\inf_{a\ \text{small}}\Phi(a)\ >\ 0.
\tag{4.1}
\]

Now connect defect to a mass gap:

- Uniform lower bounds on physical Hessians are the Bakry–Émery input for log-Sobolev/Poincaré inequalities.
- Those functional inequalities imply a **configuration diffusion spectral gap**.
- Via OS reconstruction + the one-step comparison inequality, the diffusion gap yields a **Hamiltonian mass gap**.

So the obstruction principle would become:

> **Interacting continuum limit forces persistent curvature defect; persistent defect forces a mass gap.**

This is a beautiful conceptual loop if the missing technical steps can be made rigorous.

---

## 5. Where this is genuinely new (and where it is currently conditional)
**New / high-potential:**
- defining $\Phi(a)$ as a *scale diagnostic* and trying to make it monotone,
- using it as an “order parameter” for Gaussian vs interacting continuum limits,
- integrating it into the OS/diffusion mass gap pipeline.

**Currently conditional:**
- constructing a mathematically clean $\Pi_{\mathrm{phys}}$ that behaves well under RG (or selecting a gauge-fixed chart where it is constant),
- replacing the false identity (2.1) with a correct inequality for the effective Hessian,
- proving the rigidity theorem with explicit cumulant bounds.

---

## 6. Concrete next steps to make this publishable

1. **Work in a model where (2.1) is true.**  
   Start with a Gaussian measure or a convex scalar field where coarse-graining is linear and conditioning matches.

2. **Derive the correct Hessian identity for Wilsonian blocking.**  
   Write $\nabla^2 S_{a'}$ as:
   \[
   \mathbb E[\nabla^2 S_a\mid U'] - \mathrm{Cov}(\nabla S_a,\nabla S_a\mid U')
   \]
   (up to Jacobian terms), and determine the sign structure after projecting to physical directions.

3. **Prove a quantitative “Gaussian approximation under uniform convexity” lemma.**  
   This is a standard-looking statement but needs to be tailored to gauge-fixed configuration manifolds.

4. **Exploit redundancy rigidity (Bianchi self-stress).**  
   The Maxwell–Calladine/Bianchi mechanism suggests a geometric reason physical Hessians should stay stiff—use that as an input to control $\Phi(a)$ from below.

