# Entropic potential from the Gribov horizon and the “Spark” conjecture

> **Status note.** This note is a distilled version of the project’s *most “new-theory-shaped”* idea: that **entropy from gauge-fixing constraints** can generate *strict convexity* in infrared variables even when the bare energetic part is almost flat.

## 1. The key decomposition: energetic vs entropic

Let \(\Lambda\) be a gauge-fixing–compatible constrained region in configuration space (think: a Fundamental Modular Region or a Gribov-type region), and split the gauge field into infrared and ultraviolet pieces:
\[
A \;=\; A_{\mathrm{IR}}(Y)\;+\;A_{\mathrm{UV}},
\]
where \(Y\) is a finite-dimensional set of “IR coordinates” (collective variables) extracted from \(A\).

Define the **fiber volume**
\[
\mathrm{Vol}(Y)
\;:=\;
\int \mathbf{1}_{A_{\mathrm{IR}}(Y)+A_{\mathrm{UV}}\in \Lambda}\; dA_{\mathrm{UV}}.
\]

The project defines an effective potential
\[
V_{\mathrm{eff}}(Y)
\;=\;
E(Y)\;-\;\log \mathrm{Vol}(Y),
\]
where \(E(Y)\) is the energetic contribution (Yang–Mills action evaluated/optimized along the fiber).

Interpretation:
- \(E(Y)\) is “energy”.
- \(-\log\mathrm{Vol}(Y)\) is “entropy as potential”: fewer admissible UV configurations means higher effective free energy.

---

## 2. Why the entropic term is the interesting one

A core physical observation in the notes is:

- For small \(Y\), the energetic term \(E(Y)\) can be *approximately flat* in IR directions (massless bare gluons).
- But the constraint \(\Lambda\) becomes tighter as \(Y\) moves away from the origin because of proximity to the **Gribov horizon**, so \(\mathrm{Vol}(Y)\) shrinks.
- Therefore \(-\log\mathrm{Vol}(Y)\) rises away from the origin, behaving like an **entropic confining potential** for \(Y\).

This is a clean mechanism: mass generation from **geometry of the allowed region**, rather than from an explicit mass term.

---

## 3. “Spark”: strict convexity at the origin with curvature scale \(\gamma^2\)

The project’s proposed quantitative statement is:

### (Theorem-shaped claim, at the level of a target)
There exists a Gribov scale \(\gamma>0\) and a constant \(c>0\) such that near \(Y=0\),
\[
\nabla^2 V_{\mathrm{eff}}(0)\;\succeq\; c\,\gamma^2\,I.
\]

### Spark conjecture (stated in the project)
In a simplified IR effective description,
\[
\operatorname{Hess}\,V_{\mathrm{IR}}(0)\;\ge\; c\,\gamma^2.
\]

This is the “spark” because it would ignite the whole Bakry–Émery → LSI → spectral gap chain at the continuum level:
a strictly positive Hessian at the IR origin is exactly the kind of input that functional inequality technology likes.

---

## 4. A promising rigorous route: convex geometry of slices (Prekopa/Brunn–Minkowski intuition)

Here is the mathematical skeleton hiding under the physics:

If \(\Lambda\) is **convex** in a high-dimensional linear space and \(Y=PA\) is a linear projection, then the slice volumes
\[
\mathrm{Vol}(Y)\;=\;\mathrm{Vol}\{A\in\Lambda: PA=Y\}
\]
are (under broad conditions) **log-concave** in \(Y\).

Log-concavity of \(\mathrm{Vol}(Y)\) implies convexity of \(-\log\mathrm{Vol}(Y)\). That is exactly the entropic convexity the project wants.

What remains nontrivial:
- showing the relevant \(\Lambda\) is convex (or “convex enough”) in a meaningful sense on orbit space,
- obtaining **strict** convexity and a **quantitative** curvature scale \(\sim \gamma^2\),
- proving the IR variable \(Y\) is the “right” projection for the dynamics and correlation decay.

---

## 5. Why this is bigger than a toy inequality

If the entropic term really produces a stable curvature scale \(\sim \gamma^2\) that survives \(a\to 0\), it would solve the specific failure mode identified elsewhere in the project:

> The finite-cutoff Haar-induced convexity scale behaves like \(a^2 g^2\) and vanishes along the asymptotically free trajectory, so it cannot by itself generate the continuum mass gap.

The entropic-Gribov mechanism is a candidate for the *replacement curvature source* in the continuum.

---

## 6. What “next work” would look like (concrete)

A productive next phase could aim at one of these “bite-size” targets:

1. **Model problem:** replace \(\Lambda\) by an explicit convex body \(K\subset\mathbb{R}^n\) with a “hard wall” and compute/estimate \(\nabla^2(-\log\mathrm{Vol}_K(Y))\) at \(Y=0\).
2. **Quantitative log-concavity:** turn Prekopa-style convexity into a lower Hessian bound, using curvature or isoperimetric data of \(\partial\Lambda\).
3. **Link \(\gamma\) to geometry:** interpret \(\gamma^{-1}\) as an IR radius \(R_{\mathrm{IR}}\) of the constrained body, making \(\gamma^2\) the natural curvature scale.
4. **Gauge-theory specificity:** show that the relevant constrained set in orbit space inherits the required convexity/log-concavity properties after gauge fixing.

---

## Provenance pointers (project internal)
This note distills the following internal objects/ideas:
- definition of \(V_{\mathrm{eff}}(Y)=E(Y)-\log\mathrm{Vol}(Y)\),
- the “entropic potential from Gribov horizon” observation,
- the strict convexity / Spark conjecture statement,
- the expected curvature scale \(R_{\mathrm{IR}}\sim 1/\gamma\) (so curvature \(\sim \gamma^2\)).

