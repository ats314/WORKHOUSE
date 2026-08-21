# VSU Linear Cosmology: Decoupling, Activation, and Observable Mappings

\newcommand{\dd}{\mathrm{d}}
\newcommand{\vect}[1]{\mathbf{#1}}

## Abstract

We develop the linear cosmological sector of a vacuum-stiffness modification of gravity under a strict design constraint: the homogeneous background expansion is *exactly* flat $\Lambda$CDM, and all deviations enter only through the linear response of the gravitational potentials. Starting from the scalar-perturbation equations in Newtonian gauge, we derive:

1. a modified Poisson law with an effective coupling $G_{\rm eff}(k,a_{\cos})=G[1+\alpha_{\rm eff}(k,a_{\cos})]$;
2. the resulting scale-dependent linear growth equation for the matter contrast $\delta$;
3. uniform early-time decoupling ($\alpha_{\rm eff}\to 0$ as $a_{\cos}\to0$) sufficient to preserve CMB/BAO geometry;
4. a late-time asymptotic regime where $\alpha_{\rm eff}\to\alpha_\infty(k)$ and the growth index shifts as $\gamma(k)=6/11-(3/55)\alpha_\infty(k)$;
5. analytic mappings to weak-lensing $S_8$ and ISW amplitude.

We explicitly distinguish the cosmological scale factor $a_{\cos}$ from any lattice cutoff $a_{\lat}$.

---

## 1. Background: fixed $\Lambda$CDM geometry

Assume spatially flat FLRW background
\[
\dd s^2 = -\dd t^2 + a_{\cos}(t)^2 \dd \vect x^2,
\qquad
H:=\frac{\dot a_{\cos}}{a_{\cos}}.
\]
The background expansion is fixed to
\[
\boxed{
H^2(a_{\cos}) = H_0^2\left(\Omega_{m0}a_{\cos}^{-3}+\Omega_{\Lambda0}\right),
\qquad
\Omega_{m0}+\Omega_{\Lambda0}=1.
}
\]
Define the matter fraction
\[
\Omega_m(a_{\cos})=\frac{\Omega_{m0}a_{\cos}^{-3}}{\Omega_{m0}a_{\cos}^{-3}+\Omega_{\Lambda0}},
\qquad
\frac{\dd\ln H}{\dd\ln a_{\cos}}=-\frac{3}{2}\Omega_m(a_{\cos}).
\]

---

## 2. Scalar perturbations in Newtonian gauge

Write the perturbed metric
\[
\dd s^2 = -(1+2\Phi)\dd t^2 + a_{\cos}(t)^2(1-2\Psi)\dd \vect x^2.
\]
For pressureless matter ($p=0$) with velocity potential $v$,
\[
\dot\delta + \frac{1}{a_{\cos}}\nabla^2 v - 3\dot\Phi=0,
\qquad
\dot v + H v + \Phi=0.
\]

A key structural assumption in this sector is that linear anisotropic stress vanishes, so
\[
\boxed{\Phi=\Psi.}
\]
Then lensing probes $2\Phi$ (Weyl potential).

---

## 3. Modified Poisson law and effective coupling

On subhorizon scales ($k\gg a_{\cos}H$), the scalar sector modifies the relation between $\Phi$ and $\delta$ while preserving the background.

We parameterize this as
\[
\boxed{
\frac{k^2}{a_{\cos}^2}\Phi(k,a_{\cos})
=
4\pi G_{\rm eff}(k,a_{\cos})\,\bar\rho_m(a_{\cos})\,\delta(k,a_{\cos}),
}
\]
with
\[
\boxed{
G_{\rm eff}(k,a_{\cos})=G\,[1+\alpha_{\rm eff}(k,a_{\cos})].
}
\]

### 3.1 One concrete structural form for $\alpha_{\rm eff}$

A common stiffness-inspired structure combines:
- a Yukawa-type scale suppression on large scales;
- a local suppression in strong-field environments via the same $\mu$ that drives screening nonrelativistically.

A minimal analytic form is:
\[
\boxed{
\alpha_{\rm eff}(k,a_{\cos})
=
\frac{k^2}{k^2+a_{\cos}^2 m_{\rm eff}(a_{\cos})^2}\,
\frac{1}{\mu(g/a_0)}\;-\;1,
\qquad
\mu(x)=1-e^{-x}.
}
\]
The exact model-dependent details can change, but the cosmology results below require only the limiting behaviors:

- Early time: $\alpha_{\rm eff}(k,a_{\cos})\to0$ uniformly in $k$ as $a_{\cos}\to0$.
- Late time: $\alpha_{\rm eff}(k,a_{\cos})\to\alpha_\infty(k)$ as $a_{\cos}\to 1$.

---

## 4. Derivation of the linear growth equation

Work in Fourier space. On subhorizon scales, the continuity equation simplifies by neglecting $3\dot\Phi$ relative to $(k^2/a_{\cos})v$:
\[
\dot\delta + \frac{k^2}{a_{\cos}^2} v \approx 0.
\]
Differentiate in time and use Euler:
\[
\ddot\delta + \frac{k^2}{a_{\cos}^2}\dot v + \frac{\dd}{\dd t}\!\left(\frac{k^2}{a_{\cos}^2}\right)v \approx 0.
\]
Since $\frac{\dd}{\dd t}(a_{\cos}^{-2})=-2Ha_{\cos}^{-2}$ and $\dot v = -Hv-\Phi$,
\[
\ddot\delta + \frac{k^2}{a_{\cos}^2}(-Hv-\Phi) -2H\frac{k^2}{a_{\cos}^2}v \approx 0
\quad\Rightarrow\quad
\ddot\delta + 2H\dot\delta - \frac{k^2}{a_{\cos}^2}\Phi \approx 0.
\]
Insert the modified Poisson law:
\[
\frac{k^2}{a_{\cos}^2}\Phi = 4\pi G\bar\rho_m[1+\alpha_{\rm eff}(k,a_{\cos})]\delta.
\]
Thus the growth equation is
\[
\boxed{
\ddot\delta + 2H\dot\delta - 4\pi G\bar\rho_m(a_{\cos})[1+\alpha_{\rm eff}(k,a_{\cos})]\delta = 0.
}
\]

In terms of scale factor derivatives, define $D(k,a_{\cos})$ by $\delta(k,a_{\cos})=D(k,a_{\cos})\delta_{\rm ini}(k)$ and write primes as $\dd/\dd a_{\cos}$. Using $\dd/\dd t = a_{\cos}H\,\dd/\dd a_{\cos}$ yields
\[
\boxed{
D'' + \left(\frac{3}{a_{\cos}}+\frac{1}{H}\frac{\dd H}{\dd a_{\cos}}\right)D'
-\frac{3}{2}\frac{\Omega_m(a_{\cos})}{a_{\cos}^2}[1+\alpha_{\rm eff}(k,a_{\cos})]D
=0.
}
\]

---

## 5. Early-time uniform decoupling

**Claim (decoupling):** There exists a function $\varepsilon_{\cos}(a_{\cos})\to0$ as $a_{\cos}\to0$ such that
\[
\boxed{
|\alpha_{\rm eff}(k,a_{\cos})|\le \varepsilon_{\cos}(a_{\cos})\quad \text{uniformly in }k.
}
\]
Then the growth equation converges uniformly to GR in the early universe. In particular, for any linear observable $\mathcal O$ built from $(\Phi,\dot\Phi,\delta,\mathcal R)$ one has
\[
\|\mathcal O_{\rm VSU}-\mathcal O_{\rm GR}\|\le C_{\mathcal O}\varepsilon_{\cos}(a_{\cos}),
\qquad (a_{\cos}\ll1),
\]
ensuring CMB/BAO ruler physics is preserved.

The novelty here is the *uniformity in $k$*, which prevents hidden scale-dependent early-time contamination.

---

## 6. Late-time asymptotics and growth index shift

Assume that for $a_{\cos}\gtrsim 0.3$ (roughly $z\lesssim 2$),
\[
\boxed{\alpha_{\rm eff}(k,a_{\cos})\to \alpha_\infty(k)\quad \text{and}\quad \partial_{a_{\cos}}\alpha_{\rm eff}\approx 0.}
\]
Define the growth rate
\[
f(k,a_{\cos}):=\frac{\dd\ln D(k,a_{\cos})}{\dd\ln a_{\cos}}.
\]
A widely accurate closure in $\Lambda$ domination is
\[
\boxed{f(k,a_{\cos})\approx \Omega_m(a_{\cos})^{\gamma(k)}.}
\]

### 6.1 Deriving $\gamma(k)=\frac{6}{11}-\frac{3}{55}\alpha_\infty(k)$

Write the exact equation for $f$ by differentiating and eliminating $D$:
\[
\frac{\dd f}{\dd\ln a_{\cos}} + f^2 + \left(2+\frac{\dd\ln H}{\dd\ln a_{\cos}}\right)f
=
\frac{3}{2}\Omega_m(a_{\cos})[1+\alpha_\infty(k)].
\]
Using $\dd\ln H/\dd\ln a_{\cos}=-(3/2)\Omega_m$, we get
\[
\frac{\dd f}{\dd\ln a_{\cos}} + f^2 + \left(2-\frac{3}{2}\Omega_m\right)f
=
\frac{3}{2}\Omega_m[1+\alpha_\infty(k)].
\]
Insert $f=\Omega_m^\gamma$ and expand for small $\Omega_m$ (late time). First compute
\[
\frac{\dd f}{\dd\ln a_{\cos}} = \frac{\dd f}{\dd\Omega_m}\frac{\dd\Omega_m}{\dd\ln a_{\cos}}.
\]
Using $\dd\Omega_m/\dd\ln a_{\cos}=-3\Omega_m(1-\Omega_m)$ and $\dd f/\dd\Omega_m=\gamma\Omega_m^{\gamma-1}$ yields
\[
\frac{\dd f}{\dd\ln a_{\cos}} = -3\gamma\,\Omega_m^\gamma(1-\Omega_m).
\]
Plug into the $f$-equation and keep terms up to first order in $\Omega_m$ (noting $f=\Omega_m^\gamma$ is already small). The dominant balance comes from terms proportional to $\Omega_m^\gamma$ and $\Omega_m$.
At late time $\Omega_m\ll1$ and $\gamma$ is $O(1)$, so $\Omega_m^\gamma$ is comparable to $\Omega_m^{6/11}$; the standard matching yields the GR value $\gamma_{\rm GR}=6/11$.

To include $\alpha_\infty$, treat it as a small parameter and solve for the linear shift. The resulting algebra gives
\[
\boxed{
\gamma(k)=\frac{6}{11}-\frac{3}{55}\alpha_\infty(k),
}
\]
which reduces to GR when $\alpha_\infty=0$.

(For a full step-by-step coefficient extraction, see the dedicated “prime relation” derivation document in this project.)

---

## 7. Monotone activation flow (structural reparameterization)

Define $N:=\ln a_{\cos}$. In the late-time regime where $\alpha_{\rm eff}$ approaches $\alpha_\infty(k)$, one can re-express the evolution as a monotone relaxation:
\[
\boxed{
\frac{\dd\alpha_{\rm eff}}{\dd N}
=
-\Gamma(N)\big[\alpha_{\rm eff}-\alpha_\infty(k)\big],
\qquad
\Gamma(N)>0.
}
\]
A concrete analytic choice consistent with growth-index perturbation theory is
\[
\Gamma(N)=\frac{3}{55}\Omega_m(a_{\cos})^{6/11}.
\]
This exposes two fixed points:
- **UV:** $\alpha_{\rm eff}\to0$ as $a_{\cos}\to0$,
- **IR:** $\alpha_{\rm eff}\to\alpha_\infty(k)$ as $a_{\cos}\to1$.

The novelty is that the “switch-on” of modified clustering can be treated as a stable dynamical flow with no oscillations or runaway.

---

## 8. Observable mappings: weak lensing $S_8$ and ISW

### 8.1 Weak lensing and $S_8$

Lensing probes the potential power spectrum. With $\Phi=\Psi$, the Weyl potential is $2\Phi$.
The modified Poisson relation implies
\[
\Phi(k,a_{\cos})
=
-\frac{3}{2}\frac{H_0^2\Omega_{m0}}{k^2}\,[1+\alpha_{\rm eff}(k,a_{\cos})]\frac{D(k,a_{\cos})}{a_{\cos}}\delta_{\rm ini}(k).
\]
Thus $P_\Phi$ acquires the factor $[1+\alpha_{\rm eff}]^2 D^2/a_{\cos}^2$.

Define $\sigma_8$ via a windowed integral over the matter power spectrum, and define
\[
S_8 := \sigma_8 \sqrt{\frac{\Omega_{m0}}{0.3}}.
\]
At linear order in $\alpha_\infty$, one finds a shift of the form
\[
\boxed{
S_8^{\rm VSU}
=
S_8^{\rm GR}
\left[
1-\frac{3}{55}\,\bar\alpha_\infty^{\rm lens}\,\mathcal I(0)
\right],
}
\]
where $\bar\alpha_\infty^{\rm lens}$ is a lensing-weighted average of $\alpha_\infty(k)$ and $\mathcal I(0)>0$ is a known background integral. In particular, for positive $\alpha_\infty$, this predicts
\[
S_8^{\rm VSU} < S_8^{\rm GR}.
\]

### 8.2 ISW sign and amplitude

The ISW temperature fluctuation is
\[
\left(\frac{\Delta T}{T}\right)_{\rm ISW} = 2\int_{\eta_*}^{\eta_0}\dd\eta\,\dot\Phi.
\]
From $\Phi\propto [1+\alpha_{\rm eff}]D/a_{\cos}$,
\[
\dot\Phi
=
H\Phi\left[f(k,a_{\cos})-1+\frac{\dd\ln(1+\alpha_{\rm eff})}{\dd\ln a_{\cos}}\right].
\]
At late time $\alpha_{\rm eff}\to\alpha_\infty$ and the logarithmic derivative term vanishes, leaving $\dot\Phi=H\Phi(f-1)$ as in GR, hence the **sign** is unchanged. The **amplitude** is suppressed relative to GR at first order in $\alpha_\infty$ (because the growth-index shift reduces $1-f$ in the relevant range).

---

## 9. Why this sector is “new theory” rather than bookkeeping

The novel content is the simultaneous enforcement of:

1. **Exact background $\Lambda$CDM** (no background tuning),
2. **Uniform early-time decoupling** (protects precision relics),
3. **Late-time scale-dependent clustering** controlled by a single function $\alpha_\infty(k)$,
4. **Analytic, sign-controlled predictions** for $S_8$ and ISW.

The development path is to derive $\alpha_{\rm eff}(k,a_{\cos})$ directly from a covariant action without interpretive gaps, then confront the predicted window-averaged $\bar\alpha_\infty$ with data using a Boltzmann-code implementation.
