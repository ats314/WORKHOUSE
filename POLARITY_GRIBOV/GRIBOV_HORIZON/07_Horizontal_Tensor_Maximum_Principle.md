# Horizontal Tensor Maximum Principle with a Positive Source  
*Hamilton-type eigenvalue maximum principle on a horizontal subbundle, with an explicit “source survives errors” ledger.*

This note supplies the missing hinge behind the hand‑off: a **tensor maximum principle** for a symmetric endomorphism evolving by a **parabolic Riccati inequality** on the **horizontal bundle**. The point is not that Hamilton’s argument is new, but that **it gives you a clean scalar Riccati lower bound with the *same* positive constant that later becomes the local mixing rate**.

---

## 0. Executive summary

Let \(H\subset TM\) be a smooth metric subbundle (“horizontal directions”), with a metric connection \(\nabla^H\) and associated rough Laplacian \(\Delta_H\).  
Let \(P_t\in \Gamma(\mathrm{Sym}(H))\) be a symmetric endomorphism field. Assume the **parabolic Riccati inequality**
\[
(\partial_t-\Delta_H)P_t \ \succeq\ -\alpha\,P_t^2 \ +\ \Sigma_t,
\qquad \alpha>0,
\tag{MP}
\]
and assume the **source/error split**
\[
\Sigma_t(x)\ \succeq\ \sigma_*(t)\,I_H\ -\ E_t(x),
\qquad \|E_t(x)\|_{\mathrm{op}}\le \varepsilon(t).
\tag{SE}
\]
Then the global minimal eigenvalue
\[
\lambda(t):=\inf_{x\in M}\lambda_{\min}\big(P_t(x)\big)
\]
is a viscosity supersolution of the scalar Riccati ODE
\[
\dot\lambda(t)\ \ge\ -\alpha\,\lambda(t)^2 \ +\ \sigma_*(t)\ -\ \varepsilon(t).
\tag{R}
\]
In particular, if \(\sigma_*(t)-\varepsilon(t)\ge \underline{\sigma}>0\) for \(t\ge 0\), then \(\lambda(t)\) is bounded below by the stable fixed point
\[
\lambda(t)\ \gtrsim\ \sqrt{\underline{\sigma}/\alpha}
\quad\text{after a transient.}
\]
That inequality is exactly the “**positive source survives errors**” condition.

---

## 1. Geometric setting: horizontal bundle Laplacian

Let \((M,g)\) be a smooth Riemannian manifold. Let \(H\subset TM\) be a smooth subbundle with the restricted metric \(g_H:=g|_H\).  

Pick any **metric connection** \(\nabla^H\) on \(H\). Two natural choices in gauge problems:

1. **Projected Levi–Civita connection:** if \(\Pi:TM\to H\) is the \(g\)-orthogonal projection, define
   \[
   \nabla^H_X Y := \Pi(\nabla_X Y)
   \qquad (Y\in\Gamma(H)).
   \]
2. **Quotient connection:** on the principal (irreducible) stratum where the gauge quotient is a smooth manifold, \(H\) is naturally identified with \(T(M/\mathcal G)\) and \(\nabla^H\) is the Levi–Civita connection downstairs.

Given \(\nabla^H\), the rough Laplacian on \(H\)-endomorphisms is
\[
\Delta_H P := \mathrm{tr}_g\big( \nabla^H \nabla^H P\big),
\]
where \(\nabla^H\) is extended to \(\mathrm{End}(H)\) in the usual way.

> **Practical note.** In applications, your evolution may feature a **Lichnerowicz Laplacian** \(\Delta_L\). Write it as
> \[
> \Delta_L = \Delta_H + \text{(curvature commutators)},
> \]
> and treat the commutators as part of \(\Sigma_t\) (source) or \(E_t\) (errors), depending on sign.

---

## 2. The hinge lemma (horizontal tensor maximum principle)

### Lemma 2.1 (Horizontal Hamilton maximum principle with a source and error)

Assume:

- \(M\) is compact without boundary, or compact with boundary and boundary conditions chosen so that the scalar maximum principle applies (e.g. Neumann).  
- \(P_t\in C^\infty([0,T]\times M;\mathrm{Sym}(H))\) is smooth in \((t,x)\).  
- The parabolic inequality (MP) holds in the sense of quadratic forms on \(H\).  
- The source/error split (SE) holds.

Define the global minimal eigenvalue
\[
\lambda(t):=\min_{x\in M}\lambda_{\min}\big(P_t(x)\big),
\]
(which exists for each \(t\) by compactness and continuity of \(\lambda_{\min}\)).  
Then \(\lambda\) is locally Lipschitz and satisfies, in the viscosity sense (hence a.e. in \(t\)),
\[
\dot\lambda(t)\ \ge\ -\alpha\,\lambda(t)^2\ +\ \sigma_*(t)\ -\ \varepsilon(t).
\tag{2.1}
\]

Moreover, if \(\ell(t)\) solves the scalar comparison ODE
\[
\dot \ell(t)= -\alpha\,\ell(t)^2 + \sigma_*(t)-\varepsilon(t), 
\qquad \ell(0)\le \lambda(0),
\tag{2.2}
\]
then the tensor lower bound propagates:
\[
P_t(x)\ \succeq\ \ell(t)\,I_H
\qquad\forall (t,x)\in[0,T]\times M.
\tag{2.3}
\]

---

## 3. Proof (with all the moving parts shown)

### Step 1: reduce “minimal eigenvalue” to a scalar test function

Fix \(t_0\in(0,T)\). Let \(x_0\in M\) be a point realizing the minimum:
\[
\lambda(t_0)=\lambda_{\min}\big(P_{t_0}(x_0)\big).
\]
Pick a unit eigenvector \(v_0\in H_{x_0}\) such that
\[
P_{t_0}(x_0)v_0 = \lambda(t_0)\,v_0.
\]

Extend \(v_0\) to a smooth local section \(v\in\Gamma(H)\) near \(x_0\) by **\(\nabla^H\)-parallel transport along geodesics** from \(x_0\). This gives
\[
|v(x)|\equiv 1,\qquad (\nabla^H v)(x_0)=0.
\tag{3.1}
\]

Define the scalar function
\[
\phi(x,t):=\langle P_t(x)v(x),\,v(x)\rangle_{g_H}.
\tag{3.2}
\]
At the chosen point,
\[
\phi(x_0,t_0)=\lambda(t_0).
\]
Also, for every \(x\) near \(x_0\),
\[
\phi(x,t_0)\ \ge\ \lambda_{\min}\big(P_{t_0}(x)\big)\ \ge\ \lambda(t_0)=\phi(x_0,t_0),
\]
so \(x\mapsto \phi(x,t_0)\) has a **local minimum at \(x_0\)**.

### Step 2: compute \((\partial_t-\Delta)\phi\) at the minimum

Because \(v\) has no \(t\)-dependence, differentiating (3.2) in \(t\) gives
\[
\partial_t \phi(x,t)=\langle (\partial_t P_t(x))v(x),v(x)\rangle.
\tag{3.3}
\]

For the Laplacian at \((x_0,t_0)\), use the standard product rule for the rough Laplacian on bundle-valued objects:
\[
\Delta\langle P v, v\rangle
=
\langle (\Delta_H P)v, v\rangle
+2\sum_i \langle (\nabla^H_{e_i}P)(\nabla^H_{e_i}v),v\rangle
+2\sum_i \langle (\nabla^H_{e_i}P)v,\nabla^H_{e_i}v\rangle
+2\langle P\Delta_H v,v\rangle
+2\sum_i \langle P\nabla^H_{e_i}v,\nabla^H_{e_i}v\rangle,
\tag{3.4}
\]
where \(\{e_i\}\) is a local orthonormal frame for \(TM\) near \(x_0\).

At \(x_0\) we have \((\nabla^H v)(x_0)=0\), so all terms involving \(\nabla^H v\) vanish at \(x_0\), leaving the clean identity
\[
(\Delta \phi)(x_0,t_0)=\langle (\Delta_H P_{t_0})(x_0)v_0, v_0\rangle
+2\langle P_{t_0}(x_0)(\Delta_H v)(x_0), v_0\rangle.
\tag{3.5}
\]
We do **not** need to know \((\Delta_H v)(x_0)\) as a vector. We only need its inner product with \(v_0\).

Since \(|v|\equiv 1\), we have the identity
\[
0=\Delta\langle v,v\rangle
=2\langle \Delta_H v,v\rangle + 2\sum_i \|\nabla^H_{e_i} v\|^2.
\tag{3.6a}
\]
At \(x_0\) we arranged \((\nabla^H v)(x_0)=0\), hence \(\langle (\Delta_H v)(x_0), v_0\rangle=0\). Because \(v_0\) is an eigenvector of \(P_{t_0}(x_0)\) with eigenvalue \(\lambda(t_0)\),
\[
\langle P_{t_0}(x_0)(\Delta_H v)(x_0), v_0\rangle
=
\langle (\Delta_H v)(x_0), P_{t_0}(x_0)v_0\rangle
=
\lambda(t_0)\,\langle (\Delta_H v)(x_0), v_0\rangle
=0.
\tag{3.6b}
\]
Therefore (3.5) simplifies to
\[
(\Delta \phi)(x_0,t_0)=\langle (\Delta_H P_{t_0})(x_0)v_0, v_0\rangle.
\tag{3.6}
\]


Putting (3.3) and (3.6) together:
\[
(\partial_t-\Delta)\phi(x_0,t_0)=
\left\langle \big((\partial_t-\Delta_H)P_{t_0}\big)(x_0)v_0,\,v_0\right\rangle.
\tag{3.7}
\]

### Step 3: maximum principle sign at the spatial minimum

Since \(x\mapsto \phi(x,t_0)\) has a local minimum at \(x_0\),
\[
(\Delta \phi)(x_0,t_0)\ \ge\ 0.
\tag{3.8}
\]
Equivalently,
\[
(\partial_t \phi)(x_0,t_0)\ \ge\ (\partial_t-\Delta)\phi(x_0,t_0).
\tag{3.9}
\]

### Step 4: use the tensor inequality and take the “worst direction”

Apply (MP) at \((x_0,t_0)\) and test on \(v_0\):
\[
\left\langle \big((\partial_t-\Delta_H)P_{t_0}\big)(x_0)v_0,v_0\right\rangle
\ \ge\ 
-\alpha\,\langle P_{t_0}(x_0)^2 v_0,v_0\rangle
+\langle \Sigma_{t_0}(x_0)v_0,v_0\rangle.
\tag{3.10}
\]
Because \(v_0\) is an eigenvector with eigenvalue \(\lambda(t_0)\),
\[
\langle P_{t_0}(x_0)^2 v_0,v_0\rangle=\lambda(t_0)^2.
\tag{3.11}
\]
And by (SE),
\[
\langle \Sigma_{t_0}(x_0)v_0,v_0\rangle
\ \ge\ 
\sigma_*(t_0)-\varepsilon(t_0).
\tag{3.12}
\]

Combining (3.9)–(3.12) yields
\[
\partial_t \phi(x_0,t_0)
\ \ge\ 
-\alpha\,\lambda(t_0)^2 + \sigma_*(t_0)-\varepsilon(t_0).
\tag{3.13}
\]

### Step 5: convert \(\partial_t \phi\) into a statement about \(\lambda\)

The last subtlety is that \(\lambda(t)\) is a **minimum over space and directions**, so it may fail to be differentiable where the minimizer \((x_t,v_t)\) jumps. The clean way to state the conclusion is:

- Inequality (3.13) shows that \(\lambda\) is a **viscosity supersolution** of the ODE (2.1).  
- Hence \(\lambda\) is locally Lipschitz and satisfies (2.1) for almost every \(t\).  
- Standard ODE comparison yields the propagation (2.3).

(If you prefer a more elementary route: take the lower right Dini derivative of \(\lambda\) and use an \(\eta\)-minimizer \((x_0,v_0)\) to get the same inequality with an \(o(1)\) term as \(\eta\to0\).)

This completes the proof.

---

## 4. Corollary: “positive source survives errors” (the condition you actually need)

Assume \(\sigma_*(t)\ge \sigma_0>0\) and \(\varepsilon(t)\le \varepsilon_0\) with \(\varepsilon_0<\sigma_0\). Then \(\lambda\) satisfies
\[
\dot\lambda \ \ge\ -\alpha\lambda^2 + (\sigma_0-\varepsilon_0)=:-\alpha\lambda^2 + \sigma_{\mathrm{eff}}.
\]
The scalar Riccati ODE has the stable fixed point
\[
\lambda_*=\sqrt{\sigma_{\mathrm{eff}}/\alpha}\ >0,
\]
and comparison implies:

- if \(\lambda(0)\ge 0\) then \(\lambda(t)\) increases toward \(\lambda_*\);  
- if \(\lambda(0)<0\) then \(\lambda(t)\) is still driven upward and crosses to \(\ge 0\) in finite time provided \(\sigma_{\mathrm{eff}}>0\).

So the only “real” algebraic requirement is the inequality
\[
\boxed{\ \sigma_0\ >\ \varepsilon_0\ }.
\]
That is exactly the phrase “a genuine positive source surviving errors,” in honest mathematical clothing.

---

## 5. Yang–Mills translation: where \(\sigma_0\) and \(\varepsilon_0\) come from

This section is schematic on purpose: it tells you what to bound, not how you will bound it.

### 5.1 The source \(\sigma_0\)

In your YM hand‑off, \(\Sigma_t\) should contain:

- **Intrinsic geometry:** a term like \(\mathrm{Ric}^\sharp|_H\), which on \(SU(N)^{|\mathcal B|}\) with bi‑invariant metric is strictly positive and independent of \(a\).  
- **Anomaly / effective convexity sources:** whatever part of the RG‑evolved effective action contributes a positive horizontal Hessian (trace anomaly, induced mass, etc.).  
- (At finite cutoff, you can also include the **Haar Jacobian mass term** as an explicit positive source, but it vanishes with \(a\to0\) so it is not the continuum anchor.)

The “source constant” \(\sigma_0\) is the lower bound you can certify on \(\lambda_{\min}(\Sigma_t)\) on the region where your maximum principle is run (e.g. a SAFE block).

### 5.2 The error \(\varepsilon_0\)

All of the following are legitimate candidates for the error bundle \(E_t\):

- **Coarse‑graining nonlocality:** truncation / block spin errors / Doob tilt errors that perturb the vHJ PDE.
- **Gauge projection artifacts:** commutators of projection with Laplacians, failure of a chosen connection to preserve horizontality exactly, etc.
- **Interface gluing:** any additional negative term created when you patch local SAFE charts into a global argument.

Your job is to show these are either uniformly bounded and small, or decaying along the multiscale recursion.

---

## 6. Optional add‑on: how projection errors enter (ledger form)

If you start from a PDE for a tensor on \(TM\) and then restrict to \(H\) via an orthogonal projection \(\Pi\), the Laplacian does not commute with \(\Pi\) and you pick up commutators schematically of size
\[
[\Delta,\Pi] \sim (\nabla\Pi)\nabla + (\nabla^2\Pi).
\]
A clean way to package this is:

- derive an identity
  \[
  (\partial_t-\Delta_H)(\Pi P \Pi)
  =
  \Pi(\partial_t-\Delta)P\Pi
  + \mathcal{C}_1(\nabla\Pi,\nabla P)
  + \mathcal{C}_2(\nabla^2\Pi,P),
  \]
- bound the commutators in operator norm:
  \[
  \|\mathcal{C}_1\|_{\mathrm{op}}\le C\|\nabla\Pi\|\,\|\nabla P\|,\qquad
  \|\mathcal{C}_2\|_{\mathrm{op}}\le C\|\nabla^2\Pi\|\,\|P\|.
  \]
On a SAFE chart, \(\|\nabla\Pi\|\) and \(\|\nabla^2\Pi\|\) are geometric constants; the *actual* size is then controlled by whatever a priori bounds you have on \(P\) and \(\nabla P\).  

This is exactly where your multiscale recursion and/or “typical set” restrictions are meant to pay rent: they convert these commutator terms into an \(\varepsilon(t)\) small enough to preserve \(\sigma_0-\varepsilon_0>0\).

---

## 7. What this lemma buys you downstream

Once you have (2.3), you can identify the single constant
\[
\alpha_{\mathrm{mix}}:=\inf_{t\ge 0}\ell(t)
\]
as the **local Bakry–Émery curvature floor**, hence a Poincaré constant and (with tails) an LSI constant for the Langevin generator at scale \(t\).  

So this one lemma is the “spine” connecting:

\[
\text{(parabolic Hessian PDE)}\ \Rightarrow\ \text{(Riccati lower bound)}\ \Rightarrow\ \text{(local BE curvature)}\ \Rightarrow\ \text{(local gap)}\ \Rightarrow\ \text{(global gap via your gluing)}.
\]

That is the entire game.

