# Energetic Origin of Screening via Convex Vacuum Hamiltonian

## Purpose and scope

This module establishes that gravitational screening, Newtonian recovery in strong fields, and the external field effect arise as direct consequences of a single variational principle: strict convexity of the vacuum Hamiltonian with respect to the gravitational field gradient.

No symmetry assumptions, interpolation rules, or auxiliary screening parameters are introduced. Screening is shown to be energetically inevitable once the vacuum stiffness action is specified.

---

## Vacuum stiffness Hamiltonian

In the nonrelativistic regime, the gravitational potential \(\Phi\) minimizes the energy functional

\[
\mathcal E[\Phi]
=
\int_{\mathbb R^3}
\mathcal H(\nabla\Phi)\,dx
+
\int_{\mathbb R^3} \rho\,\Phi\,dx,
\]

with Hamiltonian density

\[
\mathcal H(p)
:=
\frac{a_0^2}{8\pi G}
F\!\left(\frac{|p|^2}{a_0^2}\right),
\qquad p := \nabla\Phi,
\]

where the constitutive function satisfies

\[
F'(Y) = \mu(\sqrt{Y}),
\qquad
\mu(x) = 1 - e^{-x}.
\]

---

## Strict convexity

### Pointwise convexity

The gradient of the Hamiltonian density is

\[
\nabla_p \mathcal H(p)
=
\frac{1}{4\pi G}\, \mu(|p|/a_0)\, p.
\]

The Hessian is given by

\[
D_p^2 \mathcal H(p)
=
\frac{1}{4\pi G}
\left[
\mu(|p|/a_0)\, I
+
\frac{\mu'(|p|/a_0)}{a_0 |p|}
\, p \otimes p
\right].
\]

Since \(\mu'(x) = e^{-x} > 0\) for all \(x \ge 0\), the Hessian is positive definite for all \(p \neq 0\). Consequently, \(\mathcal H\) is strictly convex on \(\mathbb R^3\).

---

## Euler–Lagrange equation and screening

The Euler–Lagrange equation associated with \(\mathcal E\) is

\[
\nabla \cdot \nabla_p \mathcal H(\nabla \Phi)
=
4\pi G \, \rho,
\]

i.e.

\[
\nabla\cdot\!\left(\mu\!\left(\frac{|\nabla\Phi|}{a_0}\right)\nabla\Phi\right)
=
4\pi G\,\rho.
\]

---

## Energetic saturation and Newtonian recovery

### Quadratic tangent regime

As \(|p|/a_0 \to \infty\), the constitutive function saturates:

\[
\mu(|p|/a_0) \to 1,
\qquad
F(Y) = Y + O(e^{-\sqrt{Y}}).
\]

Therefore,

\[
\mathcal H(p)
=
\frac{|p|^2}{8\pi G}
+
O\!\left(e^{-|p|/a_0}\right).
\]

Large gradients are penalized quadratically, and the vacuum behaves as a rigid Newtonian medium.

### Strong-field screening

Let \(\Omega \subset \mathbb R^3\) be a region where

\[
|\nabla \Phi| \ge \Lambda a_0,
\qquad \Lambda \gg 1.
\]

Then throughout \(\Omega\), the Euler–Lagrange equation reduces to

\[
\nabla^2 \Phi
=
4\pi G\, \rho
+
O\!\left(e^{-\Lambda}\right).
\]

Newtonian gravity is therefore the universal strong-field limit, independent of geometry or environment.

---

## External field effect as Hessian domination

Consider a decomposition of the total field

\[
\nabla \Phi = p_{\mathrm{ext}} + p_{\mathrm{int}},
\qquad |p_{\mathrm{ext}}| \gg a_0.
\]

Expanding the Hamiltonian density around \(p_{\mathrm{ext}}\) yields

\[
\mathcal H(p_{\mathrm{ext}} + p_{\mathrm{int}})
=
\mathcal H(p_{\mathrm{ext}})
+
\langle \nabla_p \mathcal H(p_{\mathrm{ext}}), p_{\mathrm{int}} \rangle
+
\tfrac12 \langle p_{\mathrm{int}}, D_p^2 \mathcal H(p_{\mathrm{ext}}) p_{\mathrm{int}} \rangle
+ \cdots.
\]

Since

\[
D_p^2 \mathcal H(p_{\mathrm{ext}})
\to
\frac{1}{4\pi G} I
\quad \text{as } |p_{\mathrm{ext}}|/a_0 \to \infty,
\]

internal variations experience an effectively Newtonian quadratic energy. Consequently, internal dynamics are screened and decouple from the stiffness sector.

---

## Stability and uniqueness

Strict convexity of \(\mathcal H\) implies:

- uniqueness of energy minimizers,
- continuous dependence of solutions on the source \(\rho\),
- absence of bifurcations or multiple branches.

Screening is therefore a stability mechanism, not an imposed rule.

---

## Conceptual synthesis

This module shows that:

1. Screening is energetic saturation of a convex vacuum Hamiltonian.
2. Newtonian gravity is the quadratic tangent theory of the vacuum at large field gradients.
3. External field effects arise from Hessian domination by a background field.
4. Stability, uniqueness, and screening share a common variational origin.

No additional assumptions beyond convexity and the constitutive relation are required.

---

## Consequences for the framework

All nonlinear results—screening radii, Newtonian recovery, environmental dependence, and robustness of collapse—are corollaries of convexity. The vacuum stiffness framework is therefore not a phenomenological modification but a rigid var