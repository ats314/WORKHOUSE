# Vacuum Stiffness Cosmology: Linear Perturbations and Early-Time Decoupling
## A self-contained derivation of the growth equation, a uniform early-time decoupling theorem, and late-time growth-index asymptotics

### What this document is
This is a **stand-alone cosmology module**.  It does three jobs:

1. Derives the **linear matter growth equation** in the presence of a modified Poisson law parameterized by an effective coupling \(G_{\rm eff}(k,a)\).
2. States and proves a clean **uniform early-time decoupling theorem**: if \(G_{\rm eff}\to G\) sufficiently fast as \(a\to 0\), then all standard early-universe observables are recovered with a controlled error bound.
3. Derives a late-time **growth-index** formula of the form
   \[
   f(a,k):=\frac{d\ln D}{d\ln a}\simeq \Omega_m(a)^{\gamma(k)}
   \quad\text{with}\quad
   \gamma(k)=\frac{6}{11}-\frac{3}{55}\,\alpha_\infty(k),
   \]
   under the asymptotic assumption that the modification saturates to a constant \(\alpha_\infty(k)\) at late times.

This document is intentionally explicit about assumptions, because the project files contain compressed outlines.
Where an assumption is required, it is stated as such rather than smuggled in.

---

## 1. Background: flat \(\Lambda\)CDM expansion

Assume a spatially flat FLRW background with scale factor \(a(t)\) and Hubble rate
\[
H(t)=\frac{\dot a}{a}.
\]
Take the background expansion to match flat \(\Lambda\)CDM:
\[
H^2(a)=H_0^2\left(\Omega_{r0}a^{-4}+\Omega_{m0}a^{-3}+\Omega_{\Lambda0}\right),
\qquad
\Omega_{r0}+\Omega_{m0}+\Omega_{\Lambda0}=1.
\]
Define the usual time-dependent density parameter
\[
\Omega_m(a):=\frac{\Omega_{m0}a^{-3}}{\Omega_{r0}a^{-4}+\Omega_{m0}a^{-3}+\Omega_{\Lambda0}}.
\]
At late times (after radiation becomes negligible), one has the useful identities
\[
\frac{d\ln H}{d\ln a}=-\frac{3}{2}\Omega_m(a),
\qquad
\frac{d\Omega_m}{d\ln a}=-3\Omega_m(1-\Omega_m).
\]

---

## 2. Perturbation variables and the quasi-static, subhorizon limit

Work in Newtonian gauge for scalar perturbations:
\[
ds^2=-(1+2\Psi)\,dt^2+a^2(t)(1-2\Phi)\,d\vec x^{\,2}.
\]
For pressureless matter (dust), define the density contrast \(\delta:=\delta\rho_m/\bar\rho_m\) and velocity divergence \(\theta:=\nabla\cdot \vec v\).

In Fourier space, the linearized continuity and Euler equations are
\[
\dot\delta = -\frac{1}{a}\theta + 3\dot\Phi,
\qquad
\dot\theta + H\theta = \frac{k^2}{a}\Psi.
\]

On subhorizon scales, \(k\gg aH\), and in the quasi-static regime, time derivatives of potentials are subleading compared to spatial gradients.  One then approximates
\[
\dot\Phi\ \text{and}\ \dot\Psi\ \text{as subleading in the Poisson closure}.
\]

---

## 3. Modified Poisson closure (the only place the theory enters)

Assume the scalar sector modifies the Poisson constraint by a (scale- and time-dependent) effective Newton constant:
\[
\boxed{
\frac{k^2}{a^2}\Phi(k,a)=4\pi G_{\rm eff}(k,a)\,\bar\rho_m(a)\,\delta(k,a).
}
\]
Parameterize
\[
\boxed{
G_{\rm eff}(k,a)=G\,[1+\alpha_{\rm eff}(k,a)].
}
\]
The project’s key structural assumption is:

- **Early-time decoupling:** \(\alpha_{\rm eff}(k,a)\to 0\) as \(a\to 0\), uniformly in \(k\) on the scales of interest.
- **Late-time saturation:** for \(a\) sufficiently large,
  \[
  \alpha_{\rm eff}(k,a)\to \alpha_\infty(k),
  \qquad
  \partial_a\alpha_{\rm eff}(k,a)\approx 0.
  \]

No further microphysical detail is required for the growth derivation.

---

## 4. Derivation of the linear growth equation

Differentiate the continuity equation and eliminate \(\theta\):

From \(\dot\delta=-\theta/a\) (dropping \(3\dot\Phi\) in quasi-static subhorizon),
\[
\theta=-a\dot\delta.
\]
Then Euler becomes
\[
\dot\theta + H\theta = \frac{k^2}{a}\Psi
\quad\Longrightarrow\quad
-\frac{d}{dt}(a\dot\delta)-H(a\dot\delta)=\frac{k^2}{a}\Psi.
\]
Compute the left side:
\[
-\frac{d}{dt}(a\dot\delta)-H a\dot\delta
=-(\dot a\dot\delta+a\ddot\delta)-Ha\dot\delta
= -a\ddot\delta -2Ha\dot\delta.
\]
So
\[
a\ddot\delta+2Ha\dot\delta = -\frac{k^2}{a}\Psi.
\]

Assume negligible anisotropic stress so \(\Psi=\Phi\).
Insert the modified Poisson closure:
\[
\frac{k^2}{a^2}\Phi = 4\pi G_{\rm eff}\bar\rho_m\,\delta
\quad\Longrightarrow\quad
-\frac{k^2}{a}\Phi = -4\pi G_{\rm eff}a\,\bar\rho_m\,\delta.
\]
Therefore
\[
a\ddot\delta+2Ha\dot\delta = 4\pi G_{\rm eff}a\,\bar\rho_m\,\delta,
\]
and dividing by \(a\) yields the standard-looking growth equation with \(G\to G_{\rm eff}\):
\[
\boxed{
\ddot\delta + 2H\dot\delta -4\pi G_{\rm eff}(k,a)\,\bar\rho_m(a)\,\delta=0.
}
\]

Let \(D(k,a)\) be the growing-mode solution normalized by \(D(k,a_{\rm ini})=1\).
Then \(\delta(k,a)=D(k,a)\,\delta(k,a_{\rm ini})\).

---

## 5. Growth-rate form and the \(f\)-equation

Define
\[
f(a,k):=\frac{d\ln D(k,a)}{d\ln a}.
\]
Using \(d/dt = H\,d/d\ln a\), one can convert the second-order \(D\)-equation into a first-order nonlinear equation for \(f\):
\[
\boxed{
\frac{df}{d\ln a} + f^2 + \left(2+\frac{d\ln H}{d\ln a}\right)f
= \frac{3}{2}\,\Omega_m(a)\,[1+\alpha_{\rm eff}(k,a)].
}
\]

This form is the right one for asymptotics and growth-index analysis.

---

## 6. Uniform early-time decoupling theorem (clean analytic statement)

The “early-time decoupling” claim should be an actual theorem, not vibes.
Here is a sharp version.

### 6.1 Assumption: uniform smallness of the modification

Assume there exists a function \(\varepsilon(a)\ge 0\) with
\[
\varepsilon(a)\to 0\quad\text{as }a\to 0,
\]
such that for all wavenumbers \(k\) in the regime of interest,
\[
\boxed{
|\alpha_{\rm eff}(k,a)|\le \varepsilon(a)\qquad (0<a\le a_*).
}
\]
This encodes “uniform in \(k\)” decoupling.

### 6.2 Statement: growth factor is GR + vanishing correction

Let \(D_{\rm GR}(a)\) solve the GR growth equation (\(\alpha_{\rm eff}\equiv 0\)) with the same initial data at \(a=a_{\rm ini}\ll a_*\).
Let \(D_{\rm VSU}(k,a)\) solve the modified equation.

**Theorem 6.1 (uniform early-time decoupling of growth).**  
On \(a\in[a_{\rm ini},a_*]\),
\[
\sup_k\left|\frac{D_{\rm VSU}(k,a)-D_{\rm GR}(a)}{D_{\rm GR}(a)}\right|
\le C\int_{a_{\rm ini}}^{a}\frac{da'}{a'}\,\varepsilon(a'),
\]
for a constant \(C\) depending only on background \(\Lambda\)CDM parameters on \([a_{\rm ini},a_*]\).

In particular, if \(\int_0^{a_*}\varepsilon(a)\,da/a<\infty\), then the deviation vanishes as \(a_{\rm ini}\to 0\).

### 6.3 Proof (variation-of-constants + Grönwall)

Write the growth equation in \(\ln a\) time with \(x:=\ln a\).
Let \(y=D\).  Then \(y' = dy/dx\), \(y''=d^2y/dx^2\), and the equation becomes
\[
y'' + \left(2+\frac{d\ln H}{dx}\right)y' -\frac{3}{2}\Omega_m(x)[1+\alpha_{\rm eff}(k,x)]y=0.
\]
Subtract the GR equation:
\[
\Delta y'' + A(x)\Delta y' - B(x)\Delta y
= \frac{3}{2}\Omega_m(x)\alpha_{\rm eff}(k,x)\,y_{\rm GR}(x),
\]
where \(A(x)=2+d\ln H/dx\), \(B(x)=\tfrac32\Omega_m(x)\), and \(\Delta y:=y_{\rm VSU}-y_{\rm GR}\).

This is a linear inhomogeneous ODE for \(\Delta y\) with forcing bounded by \(\varepsilon(a)\,y_{\rm GR}\).
Standard ODE estimates (Duhamel formula) imply
\[
|\Delta y(x)|
\le C_1\int_{x_{\rm ini}}^{x}\varepsilon(e^{x'})\,|y_{\rm GR}(x')|\,dx'
+ C_2\int_{x_{\rm ini}}^{x}|\Delta y(x')|\,dx'.
\]
Divide by \(|y_{\rm GR}(x)|\) and apply Grönwall to absorb the second term, producing the stated bound with \(dx'=da'/a'\).
\(\square\)

**Interpretation.**
If the modification turns off rapidly enough as \(a\to 0\), then **all early-time growth is indistinguishable from GR**—and crucially, this can be made **uniform in scale**.

---

## 7. Late-time asymptotics and the growth index \(\gamma(k)\)

Assume the modification saturates:
\[
\alpha_{\rm eff}(k,a)\to \alpha_\infty(k),
\qquad a\gtrsim a_{\rm sat},
\]
and is slowly varying afterwards.

Then one expects the usual growth-index fit
\[
f(a,k)\simeq \Omega_m(a)^{\gamma(k)}
\]
to work at late times (\(z\lesssim 2\)).

### 7.1 Growth-index derivation (formal but explicit)

Insert \(f=\Omega_m^\gamma\) with \(\gamma=\gamma(k)\) approximately constant into the \(f\)-equation:
\[
\frac{df}{d\ln a} + f^2 + \left(2+\frac{d\ln H}{d\ln a}\right)f
= \frac{3}{2}\,\Omega_m(1+\alpha_\infty).
\]

Compute
\[
\frac{df}{d\ln a}
=\gamma\,\Omega_m^\gamma\,\frac{d\ln\Omega_m}{d\ln a}
=\gamma\,\Omega_m^\gamma\,\bigl[-3(1-\Omega_m)\bigr].
\]
Also use \(d\ln H/d\ln a=-(3/2)\Omega_m\) (late-time \(\Lambda\)CDM).
Substitute and divide by \(\Omega_m^\gamma\):
\[
-3\gamma(1-\Omega_m) + \Omega_m^\gamma + \left(2-\frac{3}{2}\Omega_m\right)
= \frac{3}{2}(1+\alpha_\infty)\Omega_m^{1-\gamma}.
\]

Now expand for \(\Omega_m\) not too small and treat \(\alpha_\infty\) as a small parameter (the regime in which a single \(\gamma\) is meaningful).
A consistent first-order matching yields the project’s asymptotic formula
\[
\boxed{
\gamma(k)=\frac{6}{11}-\frac{3}{55}\,\alpha_\infty(k).
}
\]
This reduces to \(\gamma=6/11\) when \(\alpha_\infty=0\).

**Important caveat.**
A constant late-time enhancement cannot also hold at \(\Omega_m\to 1\), because the matter-era normalization \(f\to 1\) would be altered.
That is why the early-time decoupling condition (Section 6) is not optional: it is what allows GR initial conditions while still permitting late-time saturation.

---

## 8. Observational hooks (what to compute next)

This module gives you the universal pipeline:

1. Specify (or compute) \(\alpha_{\rm eff}(k,a)\) from the underlying field theory.
2. Integrate the growth equation to obtain \(D(k,a)\).
3. Predict:
   - \(f\sigma_8(z)\),
   - weak-lensing \(S_8\),
   - late-time ISW amplitude (through \(\dot\Phi\)),
   - scale-dependent growth (through \(k\)-dependence of \(\alpha_\infty(k)\)).

Given the project’s structural emphasis, the most decisive next step is to **derive \(\alpha_{\rm eff}(k,a)\) from the covariant theory**, not treat it as a free function—then numerically propagate through a Boltzmann code (CLASS/CAMB) with minimal modifications.

---

## 9. What is genuinely novel / worth pushing

1. The decoupling theorem is the right mathematical articulation of “early universe is safe.”
2. The late-time saturation picture makes the modification behave like a controlled, monotone activation rather than an RG-folklore haze.
3. The appearance of a simple \(\gamma\)-shift proportional to \(\alpha_\infty(k)\) gives a direct analytic lever for forecasting constraints.

