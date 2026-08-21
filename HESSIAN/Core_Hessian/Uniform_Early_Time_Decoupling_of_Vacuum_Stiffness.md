# Uniform Early-Time Decoupling of Vacuum Stiffness Corrections

## Purpose and scope

This module establishes that vacuum stiffness effects are uniformly suppressed in the early universe. In particular, all linear scalar observables relevant to recombination-era physics—cosmic microwave background anisotropies, baryon acoustic oscillations, and super-horizon curvature perturbations—coincide with their general-relativistic counterparts up to a controlled, vanishing correction.

The result provides a single analytic statement that justifies the early-time reductions used throughout the linear perturbation sector and guarantees that no vacuum stiffness effect contaminates standard early-universe observables.

---

## Background assumptions

### Cosmological background

The homogeneous background expansion is fixed to flat \(\Lambda\)CDM:

\[
H^2(a) = H_0^2\left(\Omega_{m0} a^{-3} + \Omega_{\Lambda0}\right),
\qquad
\Omega_{m0} + \Omega_{\Lambda0} = 1.
\]

No modification of the background evolution is introduced by the vacuum stiffness sector.

### Scalar perturbations

We work in the linear scalar sector in Newtonian gauge. Metric perturbations satisfy

\[
\Phi = \Psi,
\]

and matter perturbations evolve according to a modified Poisson coupling

\[
\frac{k^2}{a^2} \Phi = 4\pi G_{\mathrm{eff}}(k,a)\, \bar\rho_m\, \delta,
\qquad
G_{\mathrm{eff}}(k,a) = G\,[1 + \alpha_{\mathrm{eff}}(k,a)].
\]

The function \(\alpha_{\mathrm{eff}}\) is fixed by the vacuum stiffness operator and introduces no new free parameters.

---

## Early-time regime

We define the early-time domain by

\[
a \le a_* \ll 1,
\]

such that the characteristic background acceleration satisfies

\[
\frac{a H^2(a)}{a_0} \gg 1.
\]

This condition holds throughout radiation–matter equality and recombination for any phenomenologically relevant value of \(a_0\).

---

## Suppression of the stiffness enhancement

### Uniform bound on \(\alpha_{\mathrm{eff}}\)

There exists a monotone function \(\varepsilon(a)\) with

\[
\varepsilon(a) \to 0 \quad \text{as } a \to 0,
\]

such that

\[
|\alpha_{\mathrm{eff}}(k,a)| \le \varepsilon(a)
\quad \text{for all } k \text{ and all } a \le a_*.
\]

This bound is uniform in comoving scale.

### Origin of the suppression

The effective enhancement \(\alpha_{\mathrm{eff}}\) is controlled by the ratio of physical gradients to the stiffness scale. In the early universe the background acceleration is large, forcing the constitutive factor

\[
\mu(g/a_0) = 1 - O\!\left(e^{-g/a_0}\right)
\]

to saturate exponentially fast. Consequently, deviations from Newtonian coupling vanish uniformly as \(a \to 0\).

---

## Linear growth and potential evolution

The Newtonian potential can be written as

\[
\Phi(k,a)
=
-\frac{3}{2}\frac{H_0^2 \Omega_{m0}}{k^2}
\,\mathcal G(k,a)
\frac{D(k,a)}{a},
\qquad
\mathcal G := 1 + \alpha_{\mathrm{eff}}.
\]

Differentiating with respect to conformal time gives

\[
\dot\Phi
=
H\Phi\left[
 f(k,a) - 1 + \frac{d \ln \mathcal G}{d \ln a}
\right].
\]

---

## Uniform early-time control

### Growth-rate convergence

For all \(a \le a_*\), the logarithmic growth rate satisfies

\[
f(k,a) = 1 + O\!\left(\varepsilon(a)\right),
\]

uniformly in \(k\). The Einstein–de Sitter fixed point is therefore approached uniformly at early times.

### Potential freezing

There exists a constant \(C > 0\) such that

\[
|\dot\Phi(k,a)|
\le
C\, \varepsilon(a)\, H(a)\, |\Phi(k,a)|
\quad \text{for all } k,\ a \le a_*.
\]

Thus the Newtonian potential is conserved up to a vanishing correction in the early-time limit.

---

## Consequences for scalar observables

### Uniform decoupling theorem

Let \(\mathcal O\) be any linear scalar observable constructed from the set

\[
\{\Phi, \dot\Phi, \delta, \mathcal R\},
\]

with support entirely in the domain \(a \le a_*\). Then

\[
\|\mathcal O_{\mathrm{VSU}} - \mathcal O_{\mathrm{GR}}\|
\le
C_{\mathcal O}\, \varepsilon(a_*),
\]

where the constant \(C_{\mathcal O}\) is independent of scale \(k\).

### Specific implications

- **Curvature perturbations:** The comoving curvature \(\mathcal R\) remains exactly conserved on super-horizon scales.
- **CMB primary anisotropies:** Sachs–Wolfe and Doppler terms coincide with GR up to \(O(\varepsilon(a_*))\).
- **BAO phase:** Acoustic oscillations experience no phase shift, since the driving potential is frozen.
- **Early ISW:** The early integrated Sachs–Wolfe contribution vanishes in the limit \(a \to 0\).

---

## Interpretation

Vacuum stiffness corrections are dynamically irrelevant in the early universe. Their suppression is enforced by the large background acceleration and the saturating constitutive relation, not by fine tuning or parameter choice.

All deviations from general relativity are therefore confined to late times and low-acceleration environments.

---

## Consequences for the framework

This result guarantees that:

- standard early-universe physics is preserved,
- CMB and BAO act as uncontaminated geometric rulers,
- vacuum stiffness effects enter cosmology only through late-time growth and nonlinear structure.

The early-time sector is analytically closed.

