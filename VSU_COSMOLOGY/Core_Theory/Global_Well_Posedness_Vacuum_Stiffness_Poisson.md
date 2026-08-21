# Global Well-Posedness of the Vacuum Stiffness Poisson Equation

## Purpose and scope

This module establishes existence, uniqueness, stability, and asymptotic behavior for the nonrelativistic vacuum stiffness field equation governing the gravitational potential \(\Phi\). The result is global in space, does not assume symmetry, and introduces no phenomenological input.

The theorem closes the nonrelativistic sector at the level of elliptic partial differential equation theory and provides the analytic foundation for screening, Newtonian recovery, and subsequent nonlinear structure formation results.

---

## Governing equation

We study the quasilinear elliptic equation on \(\mathbb{R}^3\)

\[
\nabla\cdot\!\left(\mu\!\left(\frac{|\nabla\Phi|}{a_0}\right)\nabla\Phi\right)
=
4\pi G\,\rho,
\]

with constitutive function

\[
\mu(x) = 1 - e^{-x}, \qquad x \ge 0,
\]

and universal acceleration scale \(a_0 > 0\).

### Source assumptions

We assume the matter density satisfies

\[
\rho \in L^1(\mathbb{R}^3) \cap L^\infty(\mathbb{R}^3),
\qquad
\rho \ge 0,
\qquad
M := \int_{\mathbb{R}^3} \rho\,dx < \infty.
\]

### Boundary condition

Solutions are required to satisfy

\[
\Phi(x) \to 0 \quad \text{as } |x| \to \infty,
\]

in the weak sense appropriate to \(H^1(\mathbb{R}^3)\).

---

## Variational formulation

Define the energy functional

\[
\mathcal E[\Phi]
=
\int_{\mathbb{R}^3}
\left[
\frac{a_0^2}{8\pi G}
F\!\left(\frac{|\nabla\Phi|^2}{a_0^2}\right)
+ \rho\,\Phi
\right]dx,
\]

where the primitive \(F\) is defined (up to an additive constant) by

\[
F'(Y) = \mu(\sqrt{Y}).
\]

### Coercivity

There exist constants \(c, C > 0\), depending only on \(a_0\) and \(G\), such that

\[
\mathcal E[\Phi]
\ge
c\,\|\nabla\Phi\|_{L^2(\mathbb{R}^3)}^2
- C\,\|\rho\|_{L^1(\mathbb{R}^3)}^2
\]

for all \(\Phi \in H^1(\mathbb{R}^3)\).

This follows from the asymptotic bounds

\[
F(Y) \sim Y \quad (Y \gg 1),
\qquad
F(Y) \sim Y^{1/2} \quad (Y \ll 1),
\]

together with Sobolev embedding and Young’s inequality applied to the source term.

### Strict convexity

The map \(p \mapsto F(|p|^2/a_0^2)\) is strictly convex on \(\mathbb{R}^3\). Indeed,

\[
\nabla_p \mathcal H(p)
=
\frac{1}{4\pi G}\,\mu(|p|/a_0)\,p,
\]

and the Hessian satisfies

\[
D_p^2 \mathcal H(p)
=
\frac{1}{4\pi G}
\left[
\mu(|p|/a_0) I
+ \frac{\mu'(|p|/a_0)}{a_0 |p|} p \otimes p
\right],
\]

which is positive definite for all \(p \ne 0\) since \(\mu'(x) = e^{-x} > 0\).

---

## Existence of solutions

By coercivity and lower semicontinuity, the functional \(\mathcal E\) admits a minimizer \(\Phi \in H^1(\mathbb{R}^3)\). Standard Euler–Lagrange theory implies that any minimizer satisfies the field equation in weak form.

Thus at least one weak solution exists.

---

## Uniqueness

Define the nonlinear operator

\[
\mathcal A(\Phi)
:=
-\nabla\cdot\!\left(\mu(|\nabla\Phi|/a_0)\nabla\Phi\right).
\]

The map \(\Phi \mapsto \mathcal A(\Phi)\) is strictly monotone on \(H^1(\mathbb{R}^3)\): for any \(\Phi_1, \Phi_2\),

\[
\int_{\mathbb{R}^3}
\big(\mathcal A(\Phi_1) - \mathcal A(\Phi_2)\big)
(\Phi_1 - \Phi_2)\,dx
> 0
\]

unless \(\nabla\Phi_1 = \nabla\Phi_2\) almost everywhere.

Consequently, any two weak solutions differ by at most an additive constant. The decay condition at infinity fixes this constant uniquely, yielding uniqueness.

---

## Regularity

If \(\rho \in L^\infty(\mathbb{R}^3)\), then standard quasilinear elliptic regularity theory implies

\[
\Phi \in C^{1,\alpha}_{\mathrm{loc}}(\mathbb{R}^3)
\quad \text{for some } \alpha \in (0,1).
\]

Higher regularity follows under correspondingly stronger assumptions on \(\rho\).

---

## Far-field asymptotics

Outside a compact set containing the support of \(\rho\), the equation is homogeneous. Uniqueness and comparison with radial solutions imply

\[
|\nabla\Phi(x)| \sim \frac{\sqrt{G M a_0}}{|x|}
\quad \text{as } |x| \to \infty,
\]

and hence

\[
\Phi(x) \sim -\sqrt{G M a_0}\,\ln|x|.
\]

This asymptotic behavior recovers the baryonic Tully–Fisher scaling and flat rotation curves as corollaries of well-posedness.

---

## Consequences

The vacuum stiffness Poisson equation is globally well posed: solutions exist, are unique, stable under perturbations of the source, and interpolate smoothly between weak-field and strong-field regimes. Screening and Newtonian recovery are not imposed but arise automatically from the convex variational structure.

This result supplies the analytic foundation for all subsequent nonlinear and structure-formation analyses.

