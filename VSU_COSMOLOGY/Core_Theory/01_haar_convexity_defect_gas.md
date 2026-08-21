# Haar-induced convexity and the “defect gas” picture (an SU(2) toy model)

> **Status note.** This document is a cleaned-up extraction/synthesis of *project-internal* derivations and numerical checks. It is **not** a complete proof of anything like the 4D continuum mass gap. It is a concrete “microscopic mechanism + failure mode + possible repair strategy” note.

## 1. Why this toy model matters

A recurring obstacle in Yang–Mills mass-gap programs is that *global* convexity of the action is hard to maintain:
- the **Haar measure** term is convex and geometric (entropic),
- the **Wilson (energetic)** term can introduce negative curvature in “large-field” regions,
- but at large inverse coupling (large \(\beta\)), the measure often **concentrates** on small-field regions anyway.

The project’s idea is to treat the nonconvex region as a **sparse set of “defects”**: rare, localized excursions into bad curvature, whose overall influence might be controlled by concentration/capacity/perturbation arguments.

This document extracts the *cleanest explicit computation* supporting that storyline.

---

## 2. SU(2) exponential coordinates and the Haar Jacobian

Work in the Lie algebra \(\mathfrak{su}(2)\cong \mathbb{R}^3\) with an axis-angle exponential map
\[
U(\alpha) \;=\; \exp\!\Big(\frac{i}{2}\,\alpha\cdot\sigma\Big),
\qquad \alpha\in\mathbb{R}^3,
\qquad r := \frac{\|\alpha\|}{2}\in[0,\pi].
\]

In these coordinates, the Haar measure has Jacobian
\[
J(\alpha) \;=\;\Big(\frac{\sin r}{r}\Big)^2,
\]
so the “Haar action” (negative log-Jacobian) is
\[
S_{\mathrm{Haar}}(\alpha)\;:=\;-\log J(\alpha)
\;=\;-2\log\!\Big(\frac{\sin r}{r}\Big).
\]

---

## 3. **Explicit Hessian eigenvalues of the Haar action** and the global \(1/6\) bound

Because \(S_{\mathrm{Haar}}(\alpha)\) is radial, its Hessian at \(\alpha\neq 0\) splits into:
- one **radial** eigenvalue \(\lambda_r(r)\),
- two **tangential** eigenvalues \(\lambda_t(r)\) (degenerate).

A core project derivation (and a JAX cross-check) gives:
\[
\lambda_r(r)
= \frac12\Big(\csc^2 r - \frac{1}{r^2}\Big),
\qquad
\lambda_t(r)
= \frac{1-r\cot r}{2r^2},
\qquad (r>0),
\]
with the smooth limit
\[
\lambda_r(0)=\lambda_t(0)=\frac{1}{6}.
\]

### Key structural facts
- As \(r\to 0\), a Taylor expansion shows \(\lambda_r(r)=\lambda_t(r)=\tfrac16+O(r^2)\).
- As \(r\to \pi\), both \(\lambda_r(r)\) and \(\lambda_t(r)\) diverge \(+\infty\) (the Jacobian collapses at the cut-locus, so the entropic penalty becomes extremely stiff).
- The *global* lower bound in this model is therefore
\[
\nabla^2 S_{\mathrm{Haar}}(\alpha)\;\succeq\;\frac16\,I_3
\quad\text{for all }\alpha\text{ in the principal exponential chart.}
\]

### Numerical verification
A dedicated script verifies:
1) the analytical formulas against automatic differentiation, and  
2) the inequality \(\lambda_{\min}\ge 1/6\) across a scan of \(r\in[0,\pi)\).

---

## 4. Adding a Wilson-type energetic term: where convexity can fail

A simplified “one-link / one-plaquette” energetic term used in the project is
\[
S_{\mathrm{W}}(\alpha;\beta)\;=\;-\frac{\beta}{2}\,\Re\mathrm{Tr}\,U(\alpha),
\]
and the total toy action is
\[
S_{\mathrm{tot}}(\alpha;\beta)
=
S_{\mathrm{Haar}}(\alpha) + S_{\mathrm{W}}(\alpha;\beta).
\]

Even though \(S_{\mathrm{Haar}}\) is uniformly convex, \(S_{\mathrm{W}}\) can introduce **negative curvature** in “large-field” directions (roughly where \(\cos r<0\) in an axis-angle picture). The project therefore defines a *convexity-loss radius* \(r_{\mathrm{crit}}(\beta)\) by scanning the smallest Hessian eigenvalue along a radial ray and finding the first \(r\) where
\[
\lambda_{\min}\big(\nabla^2 S_{\mathrm{tot}}(r;\beta)\big) < 0.
\]

A key empirical observation encoded in the analysis scripts is:

- there is a threshold \(\beta\) above which global convexity is lost, and
- the nonconvex region occurs only beyond a moderately large \(r_{\mathrm{crit}}(\beta)\).

---

## 5. Concentration-of-measure: “bad curvature” has exponentially small probability at large \(\beta\)

For the one-link toy model, the combined weight has the form
\[
e^{-S_{\mathrm{tot}}}\,d\alpha
=
\underbrace{\Big(\frac{\sin r}{r}\Big)^2}_{e^{-S_{\mathrm{Haar}}}}
\underbrace{e^{\beta \cos r}}_{e^{-S_{\mathrm{W}}}}
\cdot (4\pi r^2\,dr)
\;\propto\;
\sin^2 r\; e^{\beta\cos r}\;dr.
\]

So the *radial* probability density is
\[
p_\beta(r)\;\propto\;\sin^2 r\,e^{\beta\cos r},\qquad r\in[0,\pi].
\]

Define the “bad set” \(B_\beta := [r_{\mathrm{crit}}(\beta),\pi]\). The bad mass ratio is
\[
\mathrm{BadMass}(\beta)
:=
\frac{\int_{r_{\mathrm{crit}}(\beta)}^\pi \sin^2 r\,e^{\beta\cos r}\,dr}
{\int_0^\pi \sin^2 r\,e^{\beta\cos r}\,dr}.
\]

### Large-\(\beta\) intuition
As \(\beta\to\infty\), the measure concentrates near \(r=0\) because \(\cos r\) is maximized there. A Laplace-style estimate suggests \(\mathrm{BadMass}(\beta)\) decays like \(e^{-c\beta}\) for some \(c>0\) whenever \(r_{\mathrm{crit}}(\beta)\) stays bounded away from \(0\).

The project includes a script that:
- computes \(r_{\mathrm{crit}}(\beta)\) by Hessian scan, and
- numerically integrates the above ratio for a range of \(\beta\).

---

## 6. The “defect gas” picture on an actual lattice

The project makes the following operational definition:

- A **defect** is a link whose “radius”
  \[
  r(U):=\arccos\!\Big(\frac12\Re\mathrm{Tr}\,U\Big)
  \]
  exceeds a fixed threshold \(r_{\mathrm{crit}}\) extracted from the one-link convexity analysis.

A Monte Carlo prototype then:
- runs a 4D SU(2) lattice update (Metropolis-style),
- measures the **defect density** \(\rho\),
- checks a crude clustering diagnostic to see whether defects look “gas-like” (roughly independent) rather than forming extended correlated structures.

This is not yet a proof tool, but it is the right sort of “physics diagnostic” if one wants to justify a *cluster expansion / polymer model* picture of curvature-violating events.

---

## 7. Bigger-theory connection: how this could scale up

This toy analysis supports a plausible strategy:

1. Prove **good-region** functional inequalities (Poincaré/LSI) using Haar-induced convexity.
2. Prove the **bad region** has tiny probability and/or tiny capacity.
3. Use a perturbative stability principle (Holley–Stroock type, or capacity-based localization) to extend inequalities to the full measure.
4. Interpret the resulting uniform (in volume) spectral gap as an IR mass scale.

The rest of the project’s notes explore how to make steps (2)–(3) robust enough for an actual continuum limit.

---

## Provenance pointers (project internal)
- `analysis_haar_bound.py`: analytic Haar Hessian eigenvalues + JAX verification + global \(1/6\) bound.
- `analysis_concentration.py`: computes \(r_{\mathrm{crit}}(\beta)\) and integrates \(\mathrm{BadMass}(\beta)\).
- `analysis_lattice_mc.py`: lattice experiment measuring defect density/clustering.

