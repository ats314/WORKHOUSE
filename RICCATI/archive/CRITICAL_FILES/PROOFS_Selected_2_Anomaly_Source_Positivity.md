# Selected Proof 2: Anomaly Source Positivity Across Regimes (Lattice, Perturbative UV, Functional-Inequality View)

**Source backbone:**  
- `Lattice_Anomaly_Source_Bound_Proof.md`  
- `Perturbative_Anomaly_Source_Bound_v2_Clean - REVIEWED.md`  
- `Bakry_Emery_Toy_Model_Proof.md` and `Bakry_Emery_Anomaly_Source_Bound_Proof.md`

This document distills what is (in my view) the most portable idea in the whole project:

> **The “anomaly source” is a convexifier.**  
> In multiple regimes and by multiple methods, the RG/measure-induced term produces a **uniformly positive contribution to the Hessian**, which is exactly the ingredient that makes the Riccati/maximum-principle machinery bite.

---

## 1. The object: the anomaly source operator

In the PBH-flow framework, the effective action \(S_t\) is forced by an RG term \(J_t\) in a viscous Hamilton–Jacobi equation, and the corresponding Hessian forcing is
\[
S_{\mathrm{anom}}(t) := \nabla_H^2 J_t.
\]

One can summarize the role of \(S_{\mathrm{anom}}\) in a single inequality:

\[
\boxed{
\inf_{x\in\mathcal{M}_{\mathrm{reg}}}\;\inf_{\|v\|=1}
\langle v, S_{\mathrm{anom}}(t,x)v\rangle \ge \sigma_A > 0
}
\qquad\text{(uniform anomaly positivity).}
\]

The project contains three qualitatively different routes to \(\sigma_A>0\). The conceptual win is that these routes *agree on the sign* and (up to normalization conventions) on the scaling.

---

## 2. Prong A: lattice gauge-fixing generates a positive mass term

On a finite lattice, after gauge fixing, the effective action splits as
\[
S_{\mathrm{eff}} = S_W + S_{FP},
\]
where \(S_W\) is the Wilson action and \(S_{FP}\) is the effective action coming from the Faddeev–Popov determinant.

In the small-field expansion around the vacuum, the project derives a quadratic contribution of the form
\[
S_{FP}(A) = c_{FP}\,\|A\|^2 + O(A^4),
\qquad
c_{FP} \sim \frac{N g_0^2 a^2}{12}.
\]
Taking the Hessian at \(A=0\) yields a strictly positive operator. In one common normalization,
\[
\boxed{
\lambda_{\min}\big(\mathrm{Hess}(S_{\mathrm{eff}})\big)\Big|_{A=0}
\;\ge\;
\frac{N g_0^2 a^2}{12}
\;>\;0.
}
\]
**Interpretation:** the gauge-fixing measure contribution lifts the would-be zero modes of the Wilson quadratic form, producing a positive “seed gap” at the lattice scale.

*Note on factors of 2.* Depending on whether one writes the quadratic part as \(\tfrac12 m^2\|A\|^2\) or \(m^2\|A\|^2\), the minimal eigenvalue of the Hessian differs by a factor of 2. The key invariant point is **strict positivity with scale** \( \sim g_0^2 a^2\).

---

## 3. Prong B: perturbative UV bound from the one-loop \(\beta\)-function

In the perturbative UV, the project derives a clean, explicit lower bound for the anomaly source at momentum scale \(k\).

Let \(g(k)\) be the running coupling and \(\beta_0 = \tfrac{11N}{48\pi^2}\) the one-loop coefficient. Then the anomaly source operator satisfies
\[
\boxed{
\sigma_A(k) = 2\beta_0\, g(k)^2\, k^2
\qquad\Rightarrow\qquad
\sigma_A(k) > 0\ \text{for}\ g(k)>0.
}
\]
Equivalently,
\[
\sigma_A(k) = \frac{11N}{24\pi^2}\, g(k)^2\, k^2.
\]

**Interpretation:** asymptotic freedom does not merely say “\(g(k)\to 0\)”; it says the RG forcing is organized by a negative \(\beta\)-function, and its Hessian contribution is **positive** and scales like \(g^2 k^2\).

This is an excellent example of “physics folklore” becoming a usable inequality: it upgrades *sign information* into a quantitative coercivity bound.

---

## 4. Prong C: Bakry–Émery / functional-inequality viewpoint

A different lens comes from diffusion generators and curvature-dimension conditions.

Consider a finite-dimensional Gibbs measure
\[
d\mu = Z^{-1} e^{-V}\,dx
\]
with Langevin generator \(L=\Delta-\nabla V\cdot\nabla\). Bakry–Émery theory identifies the relevant curvature as
\[
\mathrm{Ric} + \mathrm{Hess}(V).
\]
If one can show
\[
\mathrm{Hess}(V)\ge \rho I
\]
(with \(\rho>0\)), then the measure satisfies \(CD(\rho,\infty)\), yielding a Poincaré inequality and a spectral gap \(\lambda_1\ge \rho\).

### 4.1 The toy model (fully explicit)

In the toy model document, the potential is
\[
V(x)=\frac12|x|^2 - \varepsilon f(x),
\]
and if \(f\) is uniformly concave (\(\nabla^2 f\le -\sigma I\)), then
\[
\nabla^2 V \ge (1+\varepsilon\sigma)I,
\qquad
\lambda_1 \ge 1+\varepsilon\sigma.
\]
This is the distilled mechanism: **a concave “anomaly term” makes the effective potential more convex, hence increases the gap**.

### 4.2 The lattice heuristic

The lattice Bakry–Émery note argues that the gauge-fixing term provides a uniform convexity contribution to \(V=S_{\mathrm{eff}}\), producing an effective curvature
\[
\rho \sim \frac{N g_0^2 a^2}{6}.
\]
The mathematical *template* is correct: if you can promote the convexity bound to the global configuration space (or to a region of overwhelming measure with controlled tails), you get a functional-inequality proof of positivity.

**Caution / research opportunity:** global uniform convexity for Wilson-type actions is subtle because the configuration variables live on a compact group and the action is not globally convex in naive coordinates. The toy model is the rigorous “mechanism proof”; the lattice step is the “upgrade target”.

---

## 5. Synthesis: anomaly as curvature, curvature as mass

Across all three prongs, the same conceptual identification emerges:

\[
\text{“Anomaly source”} \quad \longleftrightarrow \quad
\text{positive Hessian/curvature} \quad \longleftrightarrow \quad
\text{spectral gap / mass}.
\]

This is a bridge between:

- renormalization-group structure (via \(\beta(g)\)),
- measure geometry (via convexity and Bakry–Émery curvature),
- and spectral theory (via Poincaré/LSI and PBH/Riccati comparison).

It is hard to overstate how reusable this pattern could be: wherever you can identify an RG-induced convexifier and control geometric errors, you have the bones of a gap theorem.

---

## References within the project

- `Lattice_Anomaly_Source_Bound_Proof.md`  
- `Perturbative_Anomaly_Source_Bound_v2_Clean - REVIEWED.md`  
- `Bakry_Emery_Toy_Model_Proof.md`  
- `Bakry_Emery_Anomaly_Source_Bound_Proof.md`
