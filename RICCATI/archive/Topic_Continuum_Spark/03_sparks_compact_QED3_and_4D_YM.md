# Sparks: Compact QED\(_3\) as a Working Example, and a 4D YM Conjecture

The finite-cutoff convexity window for lattice YM relies on a Haar-induced quadratic term that vanishes in the \(a\to 0\) scaling.  
So the project introduces a useful abstraction:

> A **spark** is a mechanism that creates (or maintains) a **positive curvature / convexity** in the relevant effective action at IR scales.

This note extracts two “spark narratives” from the project:

1. a known spark (compact QED\(_3\)), used as a sanity check model,  
2. a conjectural spark for 4D YM via **Gribov/FMR entropic convexity**.

---

## 1. Compact QED\(_3\): Polyakov’s monopole spark (benchmark)

For compact \(U(1)\) gauge theory in 3D, monopoles proliferate and generate a mass gap.

A common route is via duality to a scalar “dual photon” \(\phi\) with sine-Gordon action
\[
S_{\mathrm{dual}}(\phi)=\int_{\mathbb{R}^3}\left(\frac{1}{2e^2}|\nabla\phi|^2 - 2\zeta \cos\phi\right)\,dx,
\]
where \(\zeta>0\) is a monopole fugacity.

Expanding the cosine near \(\phi=0\),
\[
-2\zeta\cos\phi = -2\zeta\left(1-\frac{\phi^2}{2}+O(\phi^4)\right)
= \text{const}+\zeta\,\phi^2+O(\phi^4).
\]

Thus the IR effective potential has curvature \(\zeta>0\) at the minimum, producing a mass:
\[
m^2 \sim \zeta e^2.
\]

**Why it matters here:** it is an explicit example where a nonperturbative object (monopoles) creates a strictly positive quadratic term in an IR effective action.

---

## 2. 4D Yang–Mills: conjectural spark from Gribov/FMR entropic convexity

### 2.1. The geometric idea

Gauge fixing (e.g. Landau gauge) does not globally parametrize \(\mathcal{A}/\mathcal{G}\) because of Gribov copies.  
One response is to restrict the functional integral to a fundamental region (FMR) / Gribov region \(\Omega\).

Heuristically:
- \(\Omega\) is a **bounded / strongly constrained** region in field space (at least in IR directions),
- the boundary (“Gribov horizon”) acts like a **hard wall** where the Faddeev–Popov operator degenerates,
- integrating out UV fluctuations inside \(\Omega\) produces an **entropic effective potential** for coarse modes.

The project’s novel twist is to phrase this in *convex-geometry language*:

> The effective action for low modes can inherit a quadratic “entropic curvature” from the shrinking volume of high-dimensional slices near the boundary of \(\Omega\).

### 2.2. A toy convex-geometry template

Let \(\Omega\subset\mathbb{R}^{m+n}\) be a high-dimensional convex body, and split coordinates into “IR” \(x\in\mathbb{R}^m\) and “UV” \(y\in\mathbb{R}^n\).
Define a purely entropic marginal density on \(x\):
\[
e^{-V_{\mathrm{ent}}(x)} := \mathrm{Vol}\{y:(x,y)\in \Omega\}.
\]

Then
\[
V_{\mathrm{ent}}(x)=-\log \mathrm{Vol}(\Omega_x),
\qquad \Omega_x:=\{y:(x,y)\in\Omega\}.
\]

In many high-dimensional settings, the function \(-\log \mathrm{Vol}(\Omega_x)\) is **convex** (Brunn–Minkowski type effects).  
Near the “center”, one expects a quadratic approximation
\[
V_{\mathrm{ent}}(x)\approx \frac{1}{2}\,m_{\mathrm{ent}}^2\,\|x\|^2.
\]

The qualitative claim is:

- **hard walls + huge dimension \(\Rightarrow\) entropic convexity**.

### 2.3. Yang–Mills translation

Replace \(\Omega\) by a gauge-fixed fundamental region in configuration space; replace \((x,y)\) by an IR/UV mode split.

Then the conjectural YM spark is:

> **Conjecture (FMR/Gribov entropic spark).**  
> After integrating out UV modes subject to the restriction \(A\in\Omega\), the resulting effective action for IR modes contains a quadratic term
> \[
> S_{\mathrm{IR,eff}}(x)\supset \frac{1}{2}m_{\mathrm{ent}}^2\,\|x\|^2,
> \qquad m_{\mathrm{ent}}^2 \gtrsim \gamma^2,
> \]
> where \(\gamma\) is a Gribov scale parameter (horizon scale).

This is spiritually related to the Gribov–Zwanziger picture (a “Gribov mass”), but the novelty here is the **entropic/convexity formulation**: the spark is not a put-in-by-hand mass, it is a curvature induced by the geometry of the allowed region in field space.

### 2.4. What would make it rigorous?

A plausible rigorous program would require:

1. A precise definition of the “fundamental region” \(\Omega\) at finite cutoff (lattice or continuum with regulator).
2. A mode-splitting map \(A\mapsto (x,y)\) with controlled Jacobian.
3. A convexity result of the form
   \[
   \nabla_x^2\big(-\log\mathrm{Vol}(\Omega_x)\big)\succeq m_{\mathrm{ent}}^2 I,
   \]
   at least on a large-probability subset.
4. Stability of this convexity under the physical YM measure (not only uniform measure on \(\Omega\)).

If achieved, this spark would feed directly into the block-convexity engine, yielding an IR spectral gap.

---

## 3. Why this spark is exciting (and risky)

Exciting:
- It reframes “mass gap from confinement geometry” as a **high-dimensional convexity phenomenon**.
- It suggests importing tools from convex geometry and metric-measure analysis into YM.

Risky:
- The actual YM gauge-fixed region is not a clean convex body; Gribov regions have complicated geometry.
- One must disentangle gauge-fixing artifacts from gauge-invariant physics.

But as a research direction: it is one of the few ideas here that could plausibly survive the \(a\to 0\) limit.

