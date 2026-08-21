# Monotone Cosmological Activation: Flow of \(\alpha_{\mathrm{eff}}(k,a)\) and Early-Time Decoupling

\begin{center}
\textit{A unified note connecting (i) uniform early-time suppression of vacuum-stiffness corrections and (ii) the effective “activation flow” of the enhancement.}
\end{center}

## Abstract

The VSU cosmology notes aim to do two things at once: keep early-universe physics indistinguishable from GR, while allowing late-time, low-acceleration deviations that are bounded and scale dependent. In the project, both requirements are packaged as a single dynamical statement: at fixed comoving scale \(k\), the enhancement \(\alpha_{\mathrm{eff}}(k,a)\) obeys a monotone first-order flow with two fixed points—\(\alpha_{\mathrm{eff}}\to 0\) as \(a\to 0\) and \(\alpha_{\mathrm{eff}}\to \alpha_{\infty}(k)\) as \(a\to 1\).

The conceptual move (and the “novel hook”) is to interpret this as **environmental activation** rather than parameter running: the acceleration scale \(a_0\) does not flow, but the universe gradually enters the low-acceleration regime where the stiffness sector becomes active.

---

## 1. Early-time decoupling as a uniform bound

The early-time module asserts a strong form of decoupling: there exists a monotone function \(\varepsilon(a)\to 0\) as \(a\to 0\) such that
\[
\boxed{|\alpha_{\mathrm{eff}}(k,a)|\le \varepsilon(a)\quad \text{for all }k\text{ and all }a\le a_*.}
\]
This uniformity in comoving scale is the important part: it aims to prevent “hidden” small-scale modifications from leaking into recombination-era observables.

In that formulation, every linear scalar observable \(\mathcal O\) built from \(\{\Phi,\dot\Phi,\delta,\mathcal R\}\) and supported in \(a\le a_*\) satisfies a bound of the schematic form
\[
\|\mathcal O_{\mathrm{VSU}}-\mathcal O_{\mathrm{GR}}\|\le C_{\mathcal O}\,\varepsilon(a_*).
\]
The mechanism is attributed to large background accelerations forcing the constitutive factor \(\mu(g/a_0)=1-O(e^{-g/a_0})\) to saturate rapidly.

---

## 2. The activation flow equation

Introduce \(N:=\ln a\). The “effective flow” module starts from the exact growth-rate equation and linearizes the difference from GR, using the late-time relation
\[
\Delta f(k,N)\equiv f_{\mathrm{VSU}}-f_{\mathrm{GR}}=-\frac{3}{55}\,\alpha_{\mathrm{eff}}(k,N)+O(\alpha_{\mathrm{eff}}^2).
\]
Differentiating and closing the system yields the proposed flow
\[
\boxed{\frac{d\alpha_{\mathrm{eff}}}{dN}=-\Gamma(N)\,[\alpha_{\mathrm{eff}}-\alpha_{\infty}(k)]}
\qquad\text{with}\qquad
\Gamma(N)=\frac{3}{55}\,\Omega_m(a)^{6/11}>0.
\]
This is structurally a stable relaxation equation: \(\alpha_{\mathrm{eff}}\) is driven toward \(\alpha_{\infty}(k)\) at a rate \(\Gamma\) controlled by the background \(\Omega_m(a)\).

---

## 3. Fixed points and why monotonicity is guaranteed

Because \(\Gamma(N)>0\), the flow has no oscillations and no runaway trajectories.

- **Ultraviolet (early-time) fixed point.** As \(a\to 0\), the module asserts \(\alpha_{\mathrm{eff}}(k,a)\to 0\). The flow interpretation is that GR is a stable UV fixed point.

- **Infrared (late-time) fixed point.** As \(a\to 1\), \(\Gamma\to 0\) and the flow freezes at \(\alpha_{\mathrm{eff}}\to \alpha_{\infty}(k)\). This is the IR endpoint.

The explicit solution is
\[
\alpha_{\mathrm{eff}}(k,a)=\alpha_{\infty}(k)\left[1-\exp\Bigl(-\int_{\ln a_i}^{\ln a}\Gamma(N')\,dN'\Bigr)\right],
\]
with \(a_i\ll 1\) an early reference time.

---

## 4. “Activation” vs “renormalization”

A distinctive interpretive claim is that \(a_0\) does not run. The scale \(a_0\) enters only through the determination of \(\alpha_{\infty}(k)\), while the flow itself is fixed by background \(\Omega_m\). The language used in the project is:

- \(\alpha_{\mathrm{eff}}\) runs (activates),
- \(a_0\) does not (no renormalization of the fundamental acceleration scale).

This turns the late-time phenomenology into a mapping problem: compute \(\alpha_{\infty}(k)\) from the underlying stiffness/screening physics, then the flow is essentially determined.

---

## 5. What to do next (high-leverage extensions)

1. **Derive \(\varepsilon(a)\) explicitly.** The early-time result is currently phrased existentially. Turning it into a concrete bound (even order-of-magnitude) would make the claim falsifiable.

2. **Compute \(\alpha_{\infty}(k)\) from nonlinear screening.** The framework repeatedly points to \(\alpha_{\infty}(k)\) as the “only” scale-dependent input. A derivation of \(\alpha_{\infty}(k)\) from the nonrelativistic convex PDE (e.g., via an effective medium approximation) would connect galaxies and large-scale structure.

3. **Connect to observables as windowed averages.** The lensing and ISW modules show that real data probe window-weighted integrals of \(\alpha_{\infty}(k)\). A compact “transfer-function” note could make those mappings mechanically reusable.

4. **Consistency checks with the prime-relations coefficient.** The same \(-3/55\) appears in both the flow closure and the operator-theoretic growth-index shift; enforcing that equivalence provides an internal consistency test.

