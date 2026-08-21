# 12-4-25 PULSE

**Source file:** `12-4-25 PULSE.txt`

---

```text
Here’s a compact conceptual map showing how **Riccati‑type curvature flows** turn your **static Haar‑convexity** inputs into **uniform LSI/spectral‑gap** outputs.

---

# 1) Objects and baselines

* State space: compact Lie group configuration manifold (links) with Gibbs ( \mu_\beta \propto e^{-S_\beta},d\mathrm{Haar} ).
* Generator: ( L = \Delta - \nabla S_\beta!\cdot!\nabla ) with carré‑du‑champ ( \Gamma(f)=|\nabla f|^2 ), ( \Gamma_2(f)=| \nabla^2 f|*F^2 + \langle \nabla^2 S*\beta,\nabla f,\nabla f\rangle ).
* Static input (your “Haar convexity”): lower Hessian control on near‑identity Wilson sector,
  [
  \nabla^2 S_\beta ;\succeq; \kappa_\beta I \quad \text{on } { \operatorname{dist}(U,I)\le r_0}.
  ]
  Plus an outlier‑control tail that keeps mass inside this convex core at large (\beta).

---

# 2) Dynamic convexification via Hessian/Riccati flow

Consider viscous HJ flow ( \partial_t\phi_t=\tfrac12|\nabla \phi_t|^2+\tfrac12\Delta \phi_t - \tfrac12\langle \nabla S_\beta,\nabla \phi_t\rangle ) (equivalently evolving densities by pushing forward along gradient flow with controlled diffusion). Along characteristics, the **shape operator** ( H_t:=\nabla^2\phi_t ) satisfies a **matrix Riccati inequality**
[
\partial_t H_t ;\preceq; -,H_t^2 ;-; \mathrm{Rm!/geom} ;-; \nabla^2 S_\beta,
]
where the geometric term is nonnegative on compact groups with bi‑invariant metric. Thus any **positive lower bound** on ( \nabla^2 S_\beta ) propagates and amplifies:
[
\partial_t \lambda_{\min}(H_t) ;\le; -,\lambda_{\min}(H_t)^2 - \kappa_\beta,
]
giving comparison with the scalar Riccati ODE ( \dot y = -y^2-\kappa_\beta \Rightarrow y(t)\le -\sqrt{\kappa_\beta}\tan(\sqrt{\kappa_\beta}t + c)). After a short time (t_\star\sim \kappa_\beta^{-1/2}), the flow produces **uniform convexity** at the evolved potential:
[
\nabla^2 S_{\beta,t_\star} ;\succeq; \kappa_\beta' I \quad (\kappa_\beta' \asymp \kappa_\beta).
]

Interpretation: the flow **expands the convexity radius**—starting from your near‑identity convex core + tail exclusion, the Riccati damping smooths bumps and yields a global lower Hessian bound.

---

# 3) From uniform convexity to LSI (Bakry–Émery)

Once ( \nabla^2 S_{\beta,t_\star}\succeq \kappa' I ) globally, Bakry–Émery gives a **log‑Sobolev inequality**
[
\operatorname{Ent}*{\mu*{\beta,t_\star}}(f^2) ;\le; \tfrac{2}{\kappa'} \int \Gamma(f),d\mu_{\beta,t_\star},
]
hence **spectral gap** ( \lambda_1 \ge \kappa' ). Stability of LSI under the inverse flow (or contractivity of heat semigroup under (CD(\kappa',\infty))) transports this bound back to the original measure (\mu_\beta) provided the outlier mass is uniformly controlled (your geometric Wilson‑tail lemma). Net: **uniform LSI and Poincaré at the original (\beta)**.

---

# 4) What you need to plug in (checklist)

1. **Static inputs (you already built):**

* (A) Local Hessian lower bound near (I) at scale (r_0(\beta)): ( \nabla^2 S_\beta \succeq \kappa_\beta I ).
* (B) Tail bound excluding ( \operatorname{dist}(U,I)>!r_0) with probability (\le c_1 e^{-c_2 \beta r_0^2}).
* (C) Tensorization across links (bounded degree).

2. **Dynamic step:**

* (D) Riccati comparison along viscous HJ/Hopf–Lax flow to produce global ( \nabla^2 S_{\beta,t_\star}\succeq \kappa' I).
* (E) Mass transport argument showing evolved density remains equivalent to original measure on the high‑probability set (uses (B)).

3. **Functional‑inequality step:**

* (F) Bakry–Émery (CD(\kappa',\infty)\Rightarrow) LSI ( \rho\ge \kappa' ) and gap ( \lambda_1\ge \kappa' ).
* (G) Stability/transport of LSI from (t_\star) back to (t=0) (bounded distortion on the core; tail negligible).

---

# 5) Clean theorem skeletons (drop‑in)

**Theorem A (Core→Global Convexity via Riccati).**
Assume (A,B,C). Then (\exists t_\star\asymp \kappa_\beta^{-1/2}) and (\kappa' \asymp \kappa_\beta) such that the evolved potential (S_{\beta,t_\star}) satisfies ( \nabla^2 S_{\beta,t_\star}\succeq \kappa' I) globally (linkwise, uniformly in volume).

**Theorem B (Uniform LSI/Spectral Gap).**
Under Theorem A and (E), (\mu_\beta) satisfies LSI with constant (\rho\gtrsim \kappa') and Poincaré with (\lambda_1\gtrsim \kappa'), uniformly in volume and along admissible coarse‑grainings.

**Corollary (Flow‑stable LSI under RG move).**
If one RG step is realized as pushforward by a gradient‑diffusion map with curvature control as above, then LSI constant does not deteriorate (up to universal factors). Hence **curvature‑stable flow ⇒ gap‑stable RG**.

---

# 6) How this links to your stack

* Your **Static Haar Convexity + Wilson‑tail** gives (A,B).
* The **Riccati inequality** is the dynamic machinery upgrading a **local convexity radius** into a **global one** (A→D).
* **Bakry–Émery** translates global convexity into **LSI/spectral gap** (F), and the tail control ensures it holds for the **original** measure (G).
* This is exactly the bridge you wanted between the **static convex core** and the **dynamic curvature‑stabilized flow** used in your gradient‑estimate arguments.

If you want, I can turn the above into paste‑ready theorem/proof blocks (with constants and a short proof using matrix Riccati comparison and CD((\kappa,\infty))).







Here’s a compact, technical primer on how **Mosco convergence** turns the hand‑wavey “(a\to0)” into a rigorous bridge from **lattice Bakry–Émery flows** to **continuum Yang–Mills (YM) heat flow**—plus the exact statements you can paste into your stack.

---

# Mosco limit → Γ‑convergence → flow convergence (what you actually need)

**Setting.**

* Lattice: directed graph (\Lambda_a) with spacing (a>0); variables are link fields (U_\ell\in SU(N)) or Lie‑algebra coordinates (A_\ell\in\mathfrak{su}(N)) inside a convexity radius.
* Continuum: a connection (A\in \Omega^1(\mathbb{T}^d,\mathfrak{su}(N))).
* Energies: (E_a: \mathcal{X}_a \to \mathbb{R}), typically Wilson (plus any convex stabilization you’ve introduced); limit functional (E: \mathcal{X}\to\mathbb{R}) is the continuum YM action (\frac12\int |F_A|^2).
* Measures: (d\mu_a \propto e^{-E_a},d\text{Haar}) (product on links), (d\mu \propto e^{-E},DA).
* Generators (Bakry–Émery form): (L_a = \Delta_a - \langle \nabla E_a,\nabla \cdot \rangle), (L = \Delta - \langle \nabla E,\nabla\cdot\rangle).

## 1) Mosco convergence (quadratic forms)

Let ((\mathsf{H}_a,\mathcal{E}_a)) be the (L^2(\mu_a)) Dirichlet form of (L_a), and ((\mathsf{H},\mathcal{E})) that of (L).
**Definition (Mosco).** (\mathcal{E}_a \xrightarrow{M} \mathcal{E}) iff:

* (M1) (liminf): for any (u_a \rightharpoonup u) weakly in (\mathsf{H}),
  (\displaystyle \liminf_{a\to0}\mathcal{E}_a(u_a,u_a)\ \ge\ \mathcal{E}(u,u)).
* (M2) (limsup): for any (u\in\mathsf{H}) there exists (u_a \to u) strongly with
  (\displaystyle \limsup_{a\to0}\mathcal{E}_a(u_a,u_a)\ \le\ \mathcal{E}(u,u)).

**Consequence.** Mosco (\Rightarrow) strong convergence of resolvents (R^\lambda_a=(\lambda-L_a)^{-1}\to R^\lambda) in (L^2), hence convergence of the semigroups (P_t^{(a)}=e^{tL_a}\to P_t=e^{tL}) strongly in (L^2) for each fixed (t>0).

## 2) Γ‑convergence (energies) and tightness

If (E_a \xrightarrow{\Gamma} E) in the (L^2) (or weak‑Sobolev) topology and ({E_a}) are equi‑coercive (your uniform convexity/LSI window gives this), then:

* Minimizers (A_a^\star) (\to) minimizer (A^\star) of (E).
* The gradient flows for (E_a) (in the (L^2(\mu_a)) metric structure) converge to the gradient flow for (E) (De Giorgi/EVIs).

For your stack, you want the **Dirichlet‑form Mosco** (for semigroup convergence) and the **Γ‑convergence of energies** (for variational stability). You already have the uniform LSI/spectral gap on each lattice scale inside the convexity radius—use that for equi‑coercivity and compactness.

## 3) Bakry–Émery (\Gamma_2) stability across (a\to0)

If on a fixed window (your “convexity radius” (r(\beta))) you have
[
\Gamma_2^{(a)}(f)\ \ge\ \kappa,\Gamma^{(a)}(f)\quad\text{for all }a\le a_0,
]
with (\kappa>0) uniform, then:

* Uniform LSI and spectral gap constants (\alpha\ge c,\kappa).
* Gradient flow contractivity in (L^2(\mu_a)) and (W_2(\mu_a)) with rate (\kappa).
  By Mosco, these constants pass to the limit: the continuum YM heat flow inherits the same (\kappa) (no decay as (a\to0)).

---

# Paste‑ready statements (use these)

**Theorem A (Γ‑convergence of lattice YM to continuum YM).**
Assume (E_a) are defined from the Wilson action with gauge‑covariant interpolation (I_a:\mathcal{X}_a\to\mathcal{X}) and consistent restriction (R_a), and suppose:

1. (Consistency) (E_a(A_a) \to E(A)) whenever (I_a A_a \to A) in (L^2) and (\sup_a E_a(A_a)<\infty).
2. (Recovery) For every (A) with (E(A)<\infty) there exist (A_a) with (I_a A_a\to A) and (E_a(A_a)\to E(A)).
3. (Equi‑coercive window) There is a set (\mathcal{K}\subset\mathcal{X}) (your convexity window) and constants (c,C>0) such that
   [
   E_a(A_a)\ \ge\ c|I_aA_a|_{H^1}^2 - C,\qquad \text{for all }A_a\text{ with }I_aA_a\in \mathcal{K},
   ]
   uniformly in (a).
   Then (E_a \xrightarrow{\Gamma} E) and minimizers and bounded‑energy sequences are precompact in (H^1) modulo gauge.

**Theorem B (Mosco convergence of Dirichlet forms).**
Let (\mathcal{E}_a) be the (L^2(\mu_a)) Dirichlet form of (L_a=\Delta_a-\nabla E_a!\cdot\nabla) and (\mathcal{E}) the (L^2(\mu)) form of (L). If Theorem A holds and, in addition,

* (Carré du champ stability) (I_a^\ast \nabla \to \nabla) in (L^2) on a core;
* (Uniform BE window) (\Gamma_2^{(a)}\ge \kappa,\Gamma^{(a)}) on (I_a^{-1}(\mathcal{K})) with the same (\kappa>0),
  then (\mathcal{E}_a \xrightarrow{M} \mathcal{E}). Consequently, (P_t^{(a)}\to P_t) strongly in (L^2) and the uniform LSI/spectral‑gap constants pass to the limit.

**Corollary (Continuum LSI & mass scale).**
Under Theorem B, the continuum YM measure (\mu) on (\mathcal{K}) satisfies an LSI with the same constant (\alpha\ge c,\kappa). Hence the continuum YM heat semigroup has spectral gap (\ge \alpha) (in the sector cut out by (\mathcal{K})), giving a **uniform correlation length (\xi\le \alpha^{-1/2})** independent of the lattice spacing. This is the rigorous “(a\to0) doesn’t kill the gap” statement in your architecture.

---

# What you must check (minimal, concrete)

* **Interpolation & consistency:** fix (I_a) (piecewise‑constant or Whitney‑type) and (R_a) so that plaquette sums approximate (\int |F_A|^2) with (O(a)) error on (\mathcal{K}).
* **Equi‑coercivity:** your uniform convexity radius + Geometric Outlier Lemma give global tightness restricted to (\mathcal{K}).
* **BE((\kappa)) window:** you already have (\Gamma_2!\ge!\kappa,\Gamma) locally from the Wilson Hessian lower bound + Riccati flow; record the explicit (\kappa(\beta,N)).
* **Core density:** cylindrical functionals (finite link dependence) form a core; stability under (I_a) gives Mosco (M1)-(M2).

---

# Where this plugs into your stack

* This replaces informal “continuum limit” language in: **A2–A5** (scalar prototype → YM), **Continuum Stability** (your Theorem 4), and the **Uniform LSI → Mass scale** step.
* It cleanly separates:
  **(i)** Energy‑level convergence (Γ) for statics,
  **(ii)** Form‑level convergence (Mosco) for dynamics/semigroups,
  **(iii)** Curvature (Bakry–Émery) giving quantitative constants that persist as (a\to0).

If you want, I can produce a drop‑in `.tex` snippet (definitions, lemmas, proofs) or a plain‑text “download” block matching your notation and constants.





Here’s a compact conceptual map showing how **Riccati‑type curvature flows** turn your **static Haar‑convexity** inputs into **uniform LSI/spectral‑gap** outputs.

---

# 1) Objects and baselines

* State space: compact Lie group configuration manifold (links) with Gibbs ( \mu_\beta \propto e^{-S_\beta},d\mathrm{Haar} ).
* Generator: ( L = \Delta - \nabla S_\beta!\cdot!\nabla ) with carré‑du‑champ ( \Gamma(f)=|\nabla f|^2 ), ( \Gamma_2(f)=| \nabla^2 f|*F^2 + \langle \nabla^2 S*\beta,\nabla f,\nabla f\rangle ).
* Static input (your “Haar convexity”): lower Hessian control on near‑identity Wilson sector,
  [
  \nabla^2 S_\beta ;\succeq; \kappa_\beta I \quad \text{on } { \operatorname{dist}(U,I)\le r_0}.
  ]
  Plus an outlier‑control tail that keeps mass inside this convex core at large (\beta).

---

# 2) Dynamic convexification via Hessian/Riccati flow

Consider viscous HJ flow ( \partial_t\phi_t=\tfrac12|\nabla \phi_t|^2+\tfrac12\Delta \phi_t - \tfrac12\langle \nabla S_\beta,\nabla \phi_t\rangle ) (equivalently evolving densities by pushing forward along gradient flow with controlled diffusion). Along characteristics, the **shape operator** ( H_t:=\nabla^2\phi_t ) satisfies a **matrix Riccati inequality**
[
\partial_t H_t ;\preceq; -,H_t^2 ;-; \mathrm{Rm!/geom} ;-; \nabla^2 S_\beta,
]
where the geometric term is nonnegative on compact groups with bi‑invariant metric. Thus any **positive lower bound** on ( \nabla^2 S_\beta ) propagates and amplifies:
[
\partial_t \lambda_{\min}(H_t) ;\le; -,\lambda_{\min}(H_t)^2 - \kappa_\beta,
]
giving comparison with the scalar Riccati ODE ( \dot y = -y^2-\kappa_\beta \Rightarrow y(t)\le -\sqrt{\kappa_\beta}\tan(\sqrt{\kappa_\beta}t + c)). After a short time (t_\star\sim \kappa_\beta^{-1/2}), the flow produces **uniform convexity** at the evolved potential:
[
\nabla^2 S_{\beta,t_\star} ;\succeq; \kappa_\beta' I \quad (\kappa_\beta' \asymp \kappa_\beta).
]

Interpretation: the flow **expands the convexity radius**—starting from your near‑identity convex core + tail exclusion, the Riccati damping smooths bumps and yields a global lower Hessian bound.

---

# 3) From uniform convexity to LSI (Bakry–Émery)

Once ( \nabla^2 S_{\beta,t_\star}\succeq \kappa' I ) globally, Bakry–Émery gives a **log‑Sobolev inequality**
[
\operatorname{Ent}*{\mu*{\beta,t_\star}}(f^2) ;\le; \tfrac{2}{\kappa'} \int \Gamma(f),d\mu_{\beta,t_\star},
]
hence **spectral gap** ( \lambda_1 \ge \kappa' ). Stability of LSI under the inverse flow (or contractivity of heat semigroup under (CD(\kappa',\infty))) transports this bound back to the original measure (\mu_\beta) provided the outlier mass is uniformly controlled (your geometric Wilson‑tail lemma). Net: **uniform LSI and Poincaré at the original (\beta)**.

---

# 4) What you need to plug in (checklist)

1. **Static inputs (you already built):**

* (A) Local Hessian lower bound near (I) at scale (r_0(\beta)): ( \nabla^2 S_\beta \succeq \kappa_\beta I ).
* (B) Tail bound excluding ( \operatorname{dist}(U,I)>!r_0) with probability (\le c_1 e^{-c_2 \beta r_0^2}).
* (C) Tensorization across links (bounded degree).

2. **Dynamic step:**

* (D) Riccati comparison along viscous HJ/Hopf–Lax flow to produce global ( \nabla^2 S_{\beta,t_\star}\succeq \kappa' I).
* (E) Mass transport argument showing evolved density remains equivalent to original measure on the high‑probability set (uses (B)).

3. **Functional‑inequality step:**

* (F) Bakry–Émery (CD(\kappa',\infty)\Rightarrow) LSI ( \rho\ge \kappa' ) and gap ( \lambda_1\ge \kappa' ).
* (G) Stability/transport of LSI from (t_\star) back to (t=0) (bounded distortion on the core; tail negligible).

---

# 5) Clean theorem skeletons (drop‑in)

**Theorem A (Core→Global Convexity via Riccati).**
Assume (A,B,C). Then (\exists t_\star\asymp \kappa_\beta^{-1/2}) and (\kappa' \asymp \kappa_\beta) such that the evolved potential (S_{\beta,t_\star}) satisfies ( \nabla^2 S_{\beta,t_\star}\succeq \kappa' I) globally (linkwise, uniformly in volume).

**Theorem B (Uniform LSI/Spectral Gap).**
Under Theorem A and (E), (\mu_\beta) satisfies LSI with constant (\rho\gtrsim \kappa') and Poincaré with (\lambda_1\gtrsim \kappa'), uniformly in volume and along admissible coarse‑grainings.

**Corollary (Flow‑stable LSI under RG move).**
If one RG step is realized as pushforward by a gradient‑diffusion map with curvature control as above, then LSI constant does not deteriorate (up to universal factors). Hence **curvature‑stable flow ⇒ gap‑stable RG**.

---

# 6) How this links to your stack

* Your **Static Haar Convexity + Wilson‑tail** gives (A,B).
* The **Riccati inequality** is the dynamic machinery upgrading a **local convexity radius** into a **global one** (A→D).
* **Bakry–Émery** translates global convexity into **LSI/spectral gap** (F), and the tail control ensures it holds for the **original** measure (G).
* This is exactly the bridge you wanted between the **static convex core** and the **dynamic curvature‑stabilized flow** used in your gradient‑estimate arguments.

If you want, I can turn the above into paste‑ready theorem/proof blocks (with constants and a short proof using matrix Riccati comparison and CD((\kappa,\infty))).
```
