# 3D Compact QED as a Worked Spark Flow Gap Example

This note is a “sanity anchor”: a model where the mass gap is known (Polyakov’s 3D compact QED), and where the **Spark–Flow–Gap** narrative has a concrete nonperturbative Spark.

The value is conceptual and methodological: it shows what a *real* Spark looks like and how it feeds the convexity engine.

---

## 1. The model and the known physics

Consider 3D compact \(U(1)\) lattice gauge theory (compact QED\(_3\)).

Polyakov’s classic result: monopoles proliferate, producing a Debye screening mass \(m>0\) and exponential decay of correlations. In modern language: the theory has a **mass gap**.

---

## 2. Duality viewpoint: monopoles generate a cosine potential

After duality (schematically), the long-distance degrees of freedom can be expressed in terms of a scalar “dual photon” field \(\phi\), and monopoles generate an effective term
\[
V(\phi)\ \approx\ \zeta\,\big(1-\cos \phi\big),
\]
where \(\zeta\) is the monopole fugacity (nonperturbatively small at weak coupling, but positive).

Near \(\phi=0\),
\[
V(\phi) = \frac{\zeta}{2}\,\phi^2 + O(\phi^4),
\]
so the effective potential has a **strictly positive quadratic curvature**.

This is the Spark.

---

## 3. How to phrase the Spark in the “block mode” language

Pick a block \(B\) of linear size \(L\) (large compared to monopole core scale), and let \(Y_B\) be the block-averaged dual mode (or an appropriate coarse gauge-invariant mode).

After integrating out short scales, the block effective potential \(V_B(Y_B)\) inherits the monopole-induced cosine term, hence near \(0\),
\[
\nabla^2_{Y_B} V_B(0)\ \approx\ \zeta.
\]
(Up to conventions: many summaries write \(2\zeta\); the point is a strictly positive constant set by monopole physics.)

So the Spark constant at some physical scale \(L_0\) is
\[
\kappa_0 \sim \zeta > 0.
\]

---

## 4. Flow: why the convexity survives coarse-graining

Once a Spark exists at a scale \(L_0\), the block convexity inequality is exactly the right tool:

- when you integrate out fine variables in a **strongly log-concave fiber** (or a conditionally convex shell),
- the Schur complement structure prevents the coarse Hessian from collapsing,
- provided coarse–fine couplings are controlled (the “\(B\)” issue).

In compact QED\(_3\), the monopole-induced curvature is a robust IR feature; it does not vanish under RG, it actually *organizes* the IR.

So the Spark–Flow mechanism matches the known mass generation.

---

## 5. Gap: from convexity to exponential decay

With a scale-stable convexity floor \(\kappa(L)\ge \kappa_*>0\), one gets:

- Poincaré / log-Sobolev inequalities for the coarse distribution,
- a spectral gap for the associated dynamics,
- and exponential decay of correlations at rate \(\sim \sqrt{\kappa_*}\).

This reproduces the mass gap narrative in a functional-inequality style.

---

## 6. Why this example matters for 4D Yang–Mills

The 4D Yang–Mills problem is “hard” because the Spark is not known.

Compact QED\(_3\) tells you what to look for:

- a **geometric/nonperturbative mechanism** that produces an effective convex potential for IR modes,
- with curvature that does **not** vanish like a UV artifact.

This is exactly why the Gribov/FMR entropic Spark conjecture is attractive: it proposes a monopole-like “geometric entropy” source of IR convexity in 4D.

---

## 7. Takeaway

This toy model does not prove anything about YM, but it validates the **architecture**:

\[
\text{(nonperturbative Spark)}\ \Rightarrow\ \text{(convexity survives RG)}\ \Rightarrow\ \text{(spectral gap)}.
\]

It also serves as a calibration target: if a candidate YM Spark is real, it should behave like the monopole-induced convexity here — *scale-stable and not UV-vanishing*.