# Cosmology in VSU: Early-Time Decoupling and a Monotone Enhancement Flow

> Curated extraction from:
> `uniform_early_time_decoupling_of_vacuum_stiffness_corrections.md`,
> `03.3_Matter_Growth_Equation.md`,
> `effective_flow_of_vacuum_stiffness_enhancement.md`,
> `03.5_Late_Time_Asymptotics.md`,
> `04.2_Weak_Lensing_and_S8.md`,
> `04.3_ISW_Sign_and_Amplitude.md`.

## 1. The core observational safety feature: uniform early-time decoupling

A persistent problem for modified-gravity ideas is “accidentally ruining the CMB era”.
The VSU documents explicitly build in (and prove) the opposite:

\[
\boxed{
\alpha_{\rm eff}(k,a)\le \varepsilon(a)\quad \text{for all }k,\ \text{with }\varepsilon(a)\to 0\text{ as }a\to 0.
}
\]

Interpretation:

- **No $k$-window survives.** Corrections vanish *uniformly* in wavenumber.
- **GR is the UV fixed point.** The early universe is automatically screened/decoupled.

This is an extremely strong “theory hygiene” constraint.

---

## 2. The matter growth equation with a scale-dependent effective coupling

In linear theory, the growth factor $D(k,a)$ obeys a modified growth equation:
\[
\boxed{
D''+\left(\frac{3}{a}+\frac{H'}{H}\right)D'
-\frac{3}{2}\frac{\Omega_m(a)}{a^2}\Bigl[1+\alpha_{\rm eff}(k,a)\Bigr]D
=0,
}
\]
with the usual definitions $f:=d\ln D/d\ln a$ and $P(k,a)\propto D(k,a)^2$.

So the entire cosmology impact is pushed into the single function $\alpha_{\rm eff}(k,a)$.

---

## 3. A useful “RG-like” rewriting: the effective enhancement flow

The notes introduce a clean phenomenological evolution law:
\[
\boxed{
\frac{d\alpha_{\rm eff}(k,a)}{dN}
=
-\Gamma(a)\Bigl(\alpha_{\rm eff}(k,a)-\alpha_\infty(k)\Bigr),
\qquad N:=\ln a,
}
\]
with properties:
- $\Gamma(a)\ge 0$ (activation rate),
- $\alpha_{\rm eff}\to \alpha_\infty(k)$ at late times,
- the flow is monotone when $\Gamma$ varies slowly.

This is basically “renormalization group structure without the mystical baggage”:
a UV fixed point at $\alpha=0$ and an IR attractor $\alpha_\infty(k)$.

---

## 4. Late-time asymptotics: growth index shift

The late-time file derives a compact first-order correction to the growth index:
\[
\boxed{
\gamma(k)=\frac{6}{11}-\frac{3}{55}\alpha_\infty(k),
\qquad
f(k,a)=\Omega_m(a)^{\gamma(k)}.
}
\]
This pins the sign logic:
- $\alpha_\infty>0$ lowers $\gamma$ and increases growth $f$ at fixed $\Omega_m$.

---

## 5. Two observation-facing predictions that fall out analytically

### 5.1 Weak lensing and $S_8$

The lensing convergence scales like
\[
C_\ell^\kappa \propto \mathcal G^2 P_m,
\qquad
\mathcal G=1+\alpha_{\rm eff}.
\]
At late times $\alpha_{\rm eff}\to \alpha_\infty$, so (to first order)
\[
\boxed{
\frac{S_8^{\rm VSU}}{S_8^{\rm GR}}
\simeq
1-\frac{3}{110}\alpha_\infty.
}
\]
So **positive** $\alpha_\infty$ suppresses $S_8$.

### 5.2 ISW sign is unchanged, amplitude is suppressed

The ISW source is $\dot\Phi$; the notes show:
- sign matches GR,
- amplitude is suppressed when $\alpha_\infty>0$.

This is attractive because it tends to “soften” late-time potential evolution without flipping it.

---

## What’s theory-worthy here

The exciting theoretical feature is the trifecta:

1. **Uniform early-time decoupling (UV safety).**
2. **A monotone activation flow (no chaotic enhancement).**
3. **Closed-form late-time signatures (ISW/lensing/growth) in terms of $\alpha_\infty(k)$.**

That’s a *framework* rather than a one-off model.

---

## Further work to expand this

1. **Derive $\Gamma(a)$ from the underlying field theory** (instead of positing it).
2. **Map $\alpha_\infty(k)$ to screening radii and halo environments** (bridge linear to nonlinear).
3. **Forward-model CMB lensing + ISW cross-correlations** with the analytic suppression factor as a starting prior.
4. **Stability audits**: prove absence of ghosts/gradient instabilities in the covariant completion under the same convexity conditions.
