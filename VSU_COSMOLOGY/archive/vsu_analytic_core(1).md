# Vacuum Stiffness Unification (VSU): Analytic Core (Nonrelativistic → Cosmology → Nonlinear)

## Scope

This document extracts the tight analytic core of the VSU framework from the project files:

- action principle and field equations,
- strict hyperbolicity of the covariant scalar sector,
- force law, screening, and EFE,
- global well-posedness (existence/uniqueness) of the quasilinear Poisson equation,
- energetic origin of screening via convex Hamiltonian,
- weak–strong field decoupling in structure formation.

No observational fitting is included.

---

## 1. Action and modified Poisson equation

Nonrelativistic action:
\[
S_{\mathrm{NR}}[\Phi]
=\int dt\int d^3x\left[\frac{a_0^2}{8\pi G}F\!\left(\frac{|\nabla\Phi|^2}{a_0^2}\right)+\rho\,\Phi\right],
\qquad
F'(Y)=\mu(\sqrt Y),\quad \mu(x)=1-e^{-x}.
\]

Euler–Lagrange equation:
\[
\boxed{\nabla\cdot\!\left(\mu\!\left(\frac{|\nabla\Phi|}{a_0}\right)\nabla\Phi\right)=4\pi G\rho.}
\]

---

## 2. Force law and BTFR

Spherical Gauss law yields
\[
g(r)\mu(g/a_0)=g_N(r)=\frac{GM(r)}{r^2}.
\]

Weak-field asymptotic gives \(g=\sqrt{a_0 g_N}\) and implies BTFR:
\[
\boxed{V^4=GMa_0.}
\]

---

## 3. Screening radius and EFE

Define \(r_s=\sqrt{GM/a_0}\). Strong-field regions \(r\ll r_s\) are Newtonian up to exponentially small corrections; strong external fields similarly enforce Newtonian internal dynamics (EFE).

---

## 4. Covariant scalar: hyperbolicity and characteristic speeds

Covariant scalar equation:
\[
\nabla_\mu(F'(X)\nabla^\mu\phi)=0,\qquad X=\frac{g^{\mu\nu}\nabla_\mu\phi\nabla_\nu\phi}{a_0^2}.
\]

Principal symbol defines an effective inverse metric
\[
G_{\mathrm{eff}}^{\mu\nu}=K(X_0)g^{\mu\nu}+\frac{2K'(X_0)}{a_0^2}u^\mu u^\nu.
\]
For \(\mu(x)=1-e^{-x}\), one finds strict hyperbolicity and \(1/2\le c_s^2<1\).

---

## 5. Global well-posedness of the quasilinear Poisson operator

The module *Global Well-Posedness of the Vacuum Stiffness Poisson Equation* proves:

- existence of a weak solution as an energy minimizer,
- strict monotonicity ⇒ uniqueness (up to constant; fixed by decay),
- interior regularity under \(\rho\in L^\infty\),
- far-field asymptotics matching the logarithmic potential and BTFR scaling.

---

## 6. Energetic origin of screening via convex vacuum Hamiltonian

The module *Energetic Origin of Screening via Convex Vacuum Hamiltonian* shows:

- Hamiltonian density \(\mathcal H(p)=\frac{a_0^2}{8\pi G}F(|p|^2/a_0^2)\) is strictly convex in \(p\),
- strong-field limit yields quadratic tangent theory \(\mathcal H(p)\sim |p|^2/(8\pi G)\),
- Newtonian recovery and EFE arise as corollaries of convexity/Hessian domination.

---

## 7. Weak–strong field decoupling in structure formation

The module *Weak–Strong Field Decoupling in Structure Formation* proves a separation principle:

- linear growth modifies boundary data in the weak-field regime;
- nonlinear collapse inside \(r_s\) is screened/Newtonian and insensitive to the linear enhancement;
- collapse threshold \(\delta_c\) and halo bias are stable under scale-dependent linear growth.

---

## 8. What is novel/high-leverage here

- A single fixed constitutive law \(\mu(x)=1-e^{-x}\) drives: force-law asymptotics, BTFR, screening, EFE, and a convex variational structure.
- The global PDE well-posedness and convex-Hamiltonian screening provide an analytic closure rarely made explicit in MOND-like modified Poisson theories.
- The weak–strong decoupling module closes the regime-mixing gap between linear cosmology and nonlinear collapse.

Next expansion targets:
- weld the covariant matter coupling derivation chain so the nonrelativistic Poisson equation is a strict weak-field limit of the covariant theory (you flagged this earlier);
- compute explicit constants for decay/screening bounds where needed.

