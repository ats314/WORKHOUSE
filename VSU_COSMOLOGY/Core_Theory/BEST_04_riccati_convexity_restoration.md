# Riccati Convexity Restoration for Hessian Flows (PBH/RG Engine)

This note extracts the cleanest “convexification under flow” mechanism from the project:  
a **matrix Riccati comparison** that yields an explicit, scale-stable lower bound on the minimum Hessian eigenvalue.

---

## 1. Abstract flow and the quantity you control

Let \(V_t:\mathbb R^n\to\mathbb R\) be a time-dependent effective potential along a coarse-graining / PBH-type flow.

Write the Hessian field
\[
H_t(x) := \nabla^2 V_t(x) \in \mathrm{Sym}(n).
\]

Define the *global* minimum eigenvalue lower envelope
\[
u(t) := \inf_{x}\ \lambda_{\min}(H_t(x)).
\]

Uniform positivity \(u(t)\ge \kappa>0\) is exactly the “convexity constant” you want, since it implies (in standard settings) a Bakry–Émery curvature lower bound and thus PI/LSI.

---

## 2. Matrix Riccati inequality ⇒ scalar Riccati inequality

### Assumption (matrix Riccati lower differential inequality)
Assume there exists a nonnegative forcing term \(K(t)\ge 0\) such that for all \(x\),
\[
\dot H_t(x)\ \succeq\ -H_t(x)^2 + K(t)\,I.
\tag{R}
\]

(Exactly this form appears in the project’s PBH/RG “Hessian restoration” notes.)

### Lemma (scalar comparison for the minimum eigenvalue)
Under (R), the envelope \(u(t)\) satisfies, in the viscosity / Dini derivative sense,
\[
\dot u(t)\ \ge\ -u(t)^2 + K(t).
\tag{r}
\]

#### Proof sketch (eigenvector test)
Fix \(t\) and an approximate minimizer \((x_t,v_t)\) with \(\|v_t\|=1\) such that
\[
u(t)\approx v_t^\top H_t(x_t) v_t.
\]
Differentiate along \(t\):
\[
\frac{d}{dt}\big(v_t^\top H_t(x_t) v_t\big)
= v_t^\top \dot H_t(x_t) v_t
\ \ge\
-\,v_t^\top H_t(x_t)^2 v_t + K(t).
\]
Using \(v_t^\top H^2 v_t \ge (v_t^\top Hv_t)^2\), we get
\[
\dot u(t)\ \gtrsim\ -u(t)^2 + K(t).
\]
A standard minimizing-sequence argument turns this into (r).

---

## 3. Explicit “burn-in convexification” bound

### Proposition (constant forcing)
If \(K(t)\equiv \kappa>0\) and \(u(t_0)\ge 0\), then the solution \(\underline u\) of
\[
\dot{\underline u} = -\underline u^2 + \kappa,\qquad \underline u(t_0)=u(t_0)
\]
is explicit:
\[
\underline u(t)
=
\sqrt{\kappa}\,
\tanh\!\Big(\sqrt{\kappa}(t-t_0) + \operatorname{arctanh}\!\frac{u(t_0)}{\sqrt{\kappa}}\Big).
\]

In particular, if \(u(t_0)=0\),
\[
u(t)\ \ge\ \sqrt{\kappa}\,\tanh(\sqrt{\kappa}(t-t_0)).
\]

So convexity appears *even if it starts at zero* and then saturates at \(\sqrt{\kappa}\).

---

## 4. Translation to PI/LSI constants (the reason you care)

In the clean Bakry–Émery regime (no gauge subtleties), a uniform bound
\[
\nabla^2 V_t \succeq u(t)\,I
\]
implies an LSI constant at least \(u(t)\), hence a diffusion spectral gap at least \(u(t)\).

So this Riccati mechanism provides a dynamic lower bound on:

- the LSI constant,
- the diffusion gap,
- and (after your bridge theorem) the OS mass gap.

---

## 5. How this becomes an “RG invariant”

If you can show that each coarse-graining step yields an (R)-type inequality with a **scale-independent** forcing floor \(\kappa\), then:

- \(u(t)\) cannot decay with scale,
- and may even increase (“geometric convexification”).

This is the analytic expression of your project’s central slogan:

> the universality class is controlled by a convexity parameter propagated by RG.

---

## 6. What’s still model-specific

The only hard step is turning your RG/PBH map into a verified inequality of the form (R) *on the physical sector* and *uniformly in volume*, including:

- handling gauge directions (degenerate directions),
- showing the forcing term \(K(t)\) is not killed by projection,
- and controlling commutator / BCH error terms.

That is where your SAFE-region constants and SU(3) numerics plug in.
