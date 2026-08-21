# BEST_04 — Scale-dependent \(G_{\rm eff}(k,a)\) with Environmental Screening Factor (Linear Growth Bridge)

## 1. Growth equation closure used in the project

The project linear-growth file defines an effective Poisson relation
\[
\frac{k^2}{a^2}\Phi
=
4\pi G_{\rm eff}(k,a)\,\bar\rho_m(a)\,\delta,
\qquad
G_{\rm eff}(k,a)=G\,[1+\alpha_{\rm eff}(k,a)],
\]
and closes the growth equation by substituting this into the standard sub-horizon elimination of the velocity potential.

This produces the familiar form
\[
\ddot\delta+2H\dot\delta
-4\pi G\bar\rho_m\,[1+\alpha_{\rm eff}(k,a)]\,\delta=0.
\]

---

## 2. The project’s explicit \(\alpha_{\rm eff}\) ansatz

In `03.3_Matter_Growth_Equation.md`, the project writes
\[
\boxed{
\alpha_{\rm eff}(k,a)
=
\frac{k^2}{k^2+a^2 m_{\rm eff}^2}\,
\frac{1}{\mu(g/a_0)},
\qquad
\mu(x)=1-e^{-x}.
}
\]

This is structurally the product of:

1. a Yukawa-like scale dependence \(k^2/(k^2+a^2 m_{\rm eff}^2)\) (tending to 1 on small scales and to 0 on large scales), and
2. an **environmental** factor \(1/\mu(g/a_0)\), importing the same \(\mu\)-function used in the nonrelativistic modified-Poisson sector.

---

## 3. Why this is a novelty candidate (conceptual linkage rather than standard algebra)

The nonstandard element is not the growth equation itself; it is the project’s attempt to *glue together*:

- a **scale-dependent** modification (in \(k\)),
- an **environment-dependent** screening factor (in local acceleration \(g\)),
- using the **same constitutive \(\mu\)** that appears in galaxy-scale phenomenology.

If made derivation-tight from the covariant field equations, this would be a unification of:
- galaxy phenomenology \(\leftrightarrow\) cosmological growth anomalies,
within a single constitutive choice.

---

## 4. What is missing inside the current project corpus

The file explicitly attributes the modified Poisson relation to `03.2_Scalar_Perturbations.md`, and the latter is not internally consistent with the domain of the constitutive law as written (see BEST\_03).

In particular, within the provided files the following are not derived:

- a definition of \(m_{\rm eff}(a)\) from the underlying scalar dynamics,
- a derivation of the Poisson modification from the linearized field equations,
- a justification of inserting an acceleration-dependent \(\mu(g/a_0)\) into a cosmological linear-response object \(G_{\rm eff}(k,a)\).

Thus the content here is best read as the project’s *proposed bridge term* rather than a completed derivation.

---

## Source pointers (project-local)

- `03.3_Matter_Growth_Equation.md`: definition of \(G_{\rm eff}\) and the explicit \(\alpha_{\rm eff}\) ansatz.
- `03.2_Scalar_Perturbations.md`: asserted origin of the modified Poisson relation (but the file has constitutive-domain issues).
- Nonrelativistic sector files (`02.1`, `02.2`): use the same \(\mu(x)=1-e^{-x}\) in galaxy-scale phenomenology.
