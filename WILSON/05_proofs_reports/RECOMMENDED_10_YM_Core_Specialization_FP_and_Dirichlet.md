# Specializing the Localization Template to an Explicit Yang--Mills Core

This note specializes **RECOMMENDED_06 (Localization theorem template)** to a concrete, explicit choice of a Yang--Mills “core region” $\mathcal K_a$ and analyzes whether the complementary region $\mathcal C_a\setminus\mathcal K_a$ plausibly admits **quantitative return / Dirichlet control**.

The goal is not to “finish YM,” but to make a single decision:

> **Does the Bakry--Émery obstruction become a *doorway* (localize + control excursions) or a *brick wall* (no realistic complement control)?**

I’ll argue that among the suggested options, the most *actionable* core (for complement control) is an **FP-eigenvalue / Gribov-horizon boundary-layer core** on a gauge-fixed slice, because the **Faddeev--Popov determinant creates a genuine barrier** near the horizon.

---

## 1. State space and diffusion (finite lattice)

Fix a finite periodic hypercubic lattice $\Lambda_a\subset a\mathbb Z^4$ with gauge group $G=SU(N)$.

- Configuration space: $\mathcal C_a := G^{B_a}$ (one link variable per bond).
- Wilson action: $S_W(U)=\sum_{p} \Big(1-\frac1N\Re\Tr(U_p)\Big)$.
- Target measure: $\mu_a(dU) \propto e^{-\beta S_W(U)}\,d\mathrm{Haar}(U)$.

The template theorem in RECOMMENDED_06 applies to any reversible diffusion with Dirichlet form
\[
\mathcal E(f,f)=\int_{\mathcal C_a} \|\nabla f\|^2\,d\mu_a.
\]

The *global* Bakry--Émery bound fails in the continuum scaling because $\inf_U\lambda_{\min}(\nabla^2 S_{\mathrm{eff}}(U))\to -\infty$ (rare but catastrophically curved configurations).

So we try to **localize**.

---

## 2. The core choice: FP-eigenvalue / “away from the Gribov horizon”

### 2.1 Gauge fixing and the fundamental modular region (FMR)

Work in (minimal) Landau gauge via the standard lattice gauge functional
\[
F[g;U] := \sum_{x,\mu} \Re\,\Tr\big(g(x)\,U_{x,\mu}\,g(x+\hat\mu)^{-1}\big),
\]
and define the **fundamental modular region** (FMR)
\[
\mathrm{FMR}:=\{U\in\mathcal C_a: F[g;U]\text{ is maximized at }g\equiv\mathbf 1\text{ along its gauge orbit}\}.
\]
Heuristically: one representative per orbit, chosen by an absolute maximum.

On the FMR, the gauge-fixing Jacobian contributes the **Faddeev--Popov determinant**
\[
\det M(U),\qquad M(U):=\text{(lattice FP operator, i.e. the Hessian of }F\text{ along gauge directions)}.
\]
The “Gribov horizon” corresponds to $\det M(U)=0$ (equivalently $\lambda_{\min}(M(U))=0$).

So the gauge-fixed measure on the FMR takes the schematic form
\[
\mu_a^{\mathrm{gf}}(dU)\ \propto\ e^{-\beta S_W(U)}\,\det M(U)\,d\mathrm{vol}_{\mathrm{FMR}}(U).
\]

### 2.2 A volume-stable FP core

A naive condition $\lambda_{\min}(M(U))\ge \kappa$ with fixed $\kappa>0$ is too strong in large volume because the free Laplacian’s smallest nonzero eigenvalue scales like $L^{-2}$.

So define a **dimensionless normalized FP gap**
\[
\gamma_{\mathrm{FP}}(U) := \frac{\lambda_{\min}^{\perp}(M(U))}{\lambda_{\min}^{\perp}(-\Delta_{\mathrm{latt}})},
\]
where $\lambda_{\min}^{\perp}$ denotes the smallest eigenvalue on gauge transformations orthogonal to global gauge (constant) modes.

Then fix an $\varepsilon\in(0,1)$ and define the **FP-eigenvalue core**
\[
\boxed{\ \mathcal K_a(\varepsilon) := \big\{U\in\mathrm{FMR}: \gamma_{\mathrm{FP}}(U)\ge \varepsilon\big\}.\ }
\]

Interpretation: the FP operator is not *anomalously* close to singular compared to the free Laplacian.

This is the version I “actually believe” is (i) typical at weak coupling and (ii) not murdered by volume.

---

## 3. How the localization template specializes

Let $A_a(\varepsilon):=\mathcal C_a\setminus\mathcal K_a(\varepsilon)$.

The RECOMMENDED_06 theorem reduces the global gap to two tasks:

1. **(H1) Local Poincaré/LSI on $\mathcal K_a(\varepsilon)$**

   Prove
   \[
   \mathrm{Var}_{\mu_{\mathcal K}}(f)\le \frac{1}{\rho_{\mathcal K}}\int_{\mathcal K_a(\varepsilon)} \|\nabla f\|^2\,d\mu_a^{\mathrm{gf}},
   \]
   with $\rho_{\mathcal K}$ uniform in volume.

   *Where it could come from in this project’s narrative:*
   - “Entropic spark” convexity for the lowest modes on a gauge-fixed slice (effective potential Hessian positive near $0$).
   - Block convexity engine for the UV + a genuine IR source term.

2. **(H2) Dirichlet/exit-time control on $A_a(\varepsilon)$**

   Prove a Dirichlet Poincaré inequality on $A_a(\varepsilon)$, equivalently a lower bound on the first Dirichlet eigenvalue $\lambda_{A}$, or an upper bound on the expected hitting time $\tau_{\mathcal K}$.

The user’s question is: **is (H2) realistically provable for this core?**

---

## 4. The complement problem becomes 1-dimensional near the horizon

The key structural advantage of an FP-based core is that on the gauge-fixed slice the density contains
\[
\det M(U)=\prod_{j=1}^{n} \lambda_j(M(U)).
\]
Near the Gribov horizon, at least one eigenvalue (say $\lambda_1$) is small.

### 4.1 Local model near the horizon

Under mild non-degeneracy assumptions (generic transversal crossing of $\lambda_1=0$), one expects locally
\[
\det M(U)\ \approx\ \lambda_1(U)\,G(U),\qquad G(U)\ge c>0\ \text{on a neighborhood away from other eigenvalue collisions}.
\]
Thus the gauge-fixed measure has a factor $\lambda_1(U)$ suppressing the horizon.

This is **exactly the kind of structure where capacity/Dirichlet control is believable**:
- the bad region $\{\lambda_1\le t\}$ is a *thin boundary layer*,
- and it has *vanishing density* as $t\downarrow 0$.

### 4.2 A concrete “Dirichlet control lemma” to aim for

Let
\[
A(t):=\{U\in\mathrm{FMR}: \lambda_1(U)\le t\},\qquad \mathcal K(t):=\{\lambda_1\ge t\}.
\]
(Think $t=\varepsilon\,\lambda_{\min}^{\perp}(-\Delta_{\mathrm{latt}})$.)

A natural target statement is:

> **Lemma (Hardy/exit-time control from the FP boundary layer).**
> There exist constants $c,C>0$ independent of volume such that for all sufficiently small $t$,
> \[
> \int_{A(t)} f^2\,d\mu_a^{\mathrm{gf}}\ \le\ C\,t^2\int_{A(t)} \|\nabla f\|^2\,d\mu_a^{\mathrm{gf}}
> \quad\text{for all }f\in\mathcal D(\mathcal E)\text{ with }f|_{\mathcal K(t)}=0.
> \]
> Equivalently, the Dirichlet eigenvalue satisfies
> \[
> \lambda_{A(t)}\ \ge\ \frac{c}{t^2}.
> \]

This is the right scaling for a one-dimensional boundary layer: the smaller the layer, the larger the Dirichlet eigenvalue.

### 4.3 Why this lemma is plausible (and what you’d actually prove)

A realistic proof strategy on a finite lattice is:

1. **Use $r(U):=\lambda_1(U)$ as a “radial coordinate.”**

2. **Coarea decomposition:** write integrals over $A(t)$ as integrals over level sets $\{r=s\}$.

3. **Lower bound the density:** near the horizon, $d\mu^{\mathrm{gf}}\sim s\,ds\,d\sigma$ (up to bounded factors), because of $\det M\sim s$.

4. **Control $|\nabla r|$ from above and below:**
   - On a finite lattice, $M(U)$ is a finite matrix depending smoothly on $U$.
   - Eigenvalue perturbation theory gives Lipschitz bounds on $r(U)$ away from eigenvalue crossings.

5. **Apply a 1D Hardy inequality:**

   For $\nu(ds)=s\,ds$ on $(0,t)$, one has
   \[
   \int_0^t g(s)^2\,s\,ds\ \lesssim\ t^2\int_0^t |g'(s)|^2\,s\,ds
   \quad\text{for }g(t)=0.
   \]

6. **Push back to $U$ using the chain rule** $|\nabla(f\circ r)|\le |f'(r)|\,|\nabla r|$.

This turns (H2) into something you can realistically grind out.

---

## 5. The decision: doorway or brick wall?

### 5.1 For the FP-eigenvalue core: **doorway** (plausible)

I think **yes**, it is realistic to prove quantitative Dirichlet/exit-time control on the complement of an FP-eigenvalue core, *provided you are willing to work on a gauge-fixed slice where the FP determinant is part of the measure*.

The reason is structural, not wishful:

- The “bad set” is literally a **boundary layer near a vanishing determinant**.
- Vanishing density near the boundary is exactly what powers Hardy-type inequalities and small-capacity results.
- The relevant “badness coordinate” ($\lambda_1$) is a finite-dimensional eigenvalue on the lattice, so you can do perturbation theory.

The hard work is real but of the *right type*.

### 5.2 For plaquette-defect / no-near-center cores: **leans brick wall** (hard)

For a plaquette-defect core
\[
\mathcal K_a^{\mathrm{plaq}}(\delta)=\{U: \forall p,\ 1-\tfrac1N\Re\Tr(U_p)\le \delta\},
\]
(or a “no-near-center plaquettes” variant), the complement typically has:

- no singular vanishing factor like $\det M$;
- a potentially **connected, roaming defect geometry** (you can move the “bad plaquette” around while staying outside the core);
- thus no obvious uniform lower bound on the Dirichlet eigenvalue without a much deeper metastability argument.

It may still be true, but it looks substantially less provable with the current toolkit.

---

## 6. What to do next (minimal viable proof plan)

If you want a crisp path that can be attacked in a month-scale sprint (not a decade-scale saga), it’s this:

1. **Finite lattice FP geometry lemma.**
   Show that on the FMR away from eigenvalue collisions,
   \[
   \det M(U) = \lambda_1(U)\,G(U)\quad\text{with }G(U)\ge c>0.
   \]

2. **Gradient bounds for $\lambda_1(U)$.**
   Prove a uniform (in volume) Lipschitz estimate
   \[
   \|\nabla \lambda_1(U)\|\le C.
   \]
   (The constant should depend on $N$ and local combinatorics, not on $|\Lambda|$.)

3. **Hardy/coarea inequality ⇒ $\lambda_{A(t)}$ bound.**
   Turn the boundary-layer structure into a quantitative Dirichlet estimate.

4. **Only then worry about (H1) on $\mathcal K_a(\varepsilon)$.**
   If (H2) is solid, the obstruction is no longer fatal; it is a *localized nuisance*.

---

## 7. Bottom line

- **Core I’d pick:** FP-eigenvalue (normalized gap) core on the FMR.
- **Complement control:** realistically provable via Hardy/coarea + vanishing FP determinant.
- **Verdict:** the BE obstruction looks like a **doorway** *if* you accept working on a gauge-fixed slice with FP determinant built into the measure.

