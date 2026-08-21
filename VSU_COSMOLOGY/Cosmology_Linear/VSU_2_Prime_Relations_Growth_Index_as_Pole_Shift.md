# Prime Relations: the Growth-Index Shift as a Spectral Pole Shift

\begin{center}
\textit{A cleaned LaTeX synthesis of the project’s “prime relations” work: why}
\(\gamma(k)=\tfrac{6}{11}-\tfrac{3}{55}\,\alpha_\infty(k)\)
\textit{can be read as a first-order pole shift of a linear growth resolvent.}
\end{center}

## Abstract

This note repackages the derivations in `PRIME RELATIONS.txt` into a compact, citation-ready LaTeX narrative. The key claim is that the numerical factor \(-3/55\) is not an empirical tuning knob: it is a fixed coefficient arising from linear operator perturbation theory applied to the late-time growth kernel. In the project’s language, \(6/11\) is the unperturbed “pole location” of the GR growth resolvent, and \(3/55\) is its first-order shift under a multiplicative Poisson enhancement.

The discussion below is deliberately narrow: it isolates the coefficient algebra and the operator interpretation, leaving cosmological parameter fitting to other modules.

---

## 1. Late-time input and the growth-rate equation

Use the logarithmic time variable \(N:=\ln a\). Define the growth rate
\[
 f:=\frac{d\ln D}{dN}.
\]
The first-order exact equation for \(f\) is
\[
\frac{df}{dN}+f^2+\Bigl(2+\frac{d\ln H}{dN}\Bigr)f
=\frac{3}{2}\,\Omega_m(N)\,[1+\alpha_{\rm eff}(k,N)].
\]
In the late-time regime used throughout the project, the enhancement saturates
\[
\alpha_{\rm eff}(k,N)\to \alpha_\infty(k),\qquad \partial_N\alpha_{\rm eff}\approx 0,
\]
so the right-hand side is perturbed by a constant factor \(1+\alpha_\infty(k)\).

---

## 2. “Kernel moment” route to the coefficient \(-3/55\)

The `PRIME RELATIONS` derivation proceeds by computing a late-time correction to the growth factor \(D\), then differentiating to get the correction to \(f\), and finally translating that into a growth-index shift.

### 2.1 Late-time kinematics for \(\Omega_m\)

In the late-time limit (small \(\Omega_m\)), one uses
\[
\frac{d\Omega_m}{dN}=-3\Omega_m(1-\Omega_m)\simeq -3\Omega_m.
\]
This converts integrals in \(N\) into power integrals in \(\Omega_m\).

### 2.2 The moment integral

The “moment” appearing in the resolvent/kernal expansion is an integral of the form
\[
\int dN\,\Omega_m^{12/11}.
\]
Using \(dN\simeq -\frac{1}{3}\frac{d\Omega_m}{\Omega_m}\),
\[
\int dN\,\Omega_m^{12/11}
\simeq -\frac{1}{3}\int \Omega_m^{1/11}\,d\Omega_m
= -\frac{1}{3}\cdot \frac{11}{12}\,\Omega_m^{12/11}
= -\frac{11}{36}\,\Omega_m^{12/11}.
\]
In the project’s normalization this produces a relative correction
\[
\frac{\delta D}{D_0}=+\frac{11}{24}\,\alpha_\infty\,\Omega_m^{12/11}.
\]

### 2.3 Differentiate to get \(\delta f\)

By definition, \(f=d\ln D/dN\), so to first order
\[
\delta f=\frac{d}{dN}\Bigl(\frac{\delta D}{D_0}\Bigr).
\]
Differentiating the \(\Omega_m^{12/11}\) power and again using \(d\Omega_m/dN\simeq -3\Omega_m\), the derivation yields
\[
\boxed{\delta f= -\frac{3}{55}\,\alpha_\infty\,\Omega_m^{6/11}.}
\]
Since the corresponding GR scaling is \(f_0=\Omega_m^{6/11}\), this can be summarized as
\[
 f\simeq \Omega_m^{6/11}\Bigl(1-\frac{3}{55}\alpha_\infty\Bigr).
\]

### 2.4 Convert \(\delta f\) into a growth-index shift

Defining \(\gamma\) through the project’s growth-index form \(f\approx \Omega_m^{\gamma}\), the same first-order correction is equivalently encoded as
\[
\boxed{\gamma(k)=\frac{6}{11}-\frac{3}{55}\,\alpha_\infty(k).}
\]

---

## 3. Operator language: \(-3/55\) as a pole shift

The same constant reappears when the growth dynamics are written as a linear operator with a perturbed resolvent.

### 3.1 Perturbation setup

Write the GR growth operator as \(L_0\) and the VSU correction as a multiplicative perturbation \(\delta L\) proportional to \(\alpha_\infty\). The `PRIME RELATIONS` file phrases the eigenvalue (pole) shift as
\[
\boxed{\delta\lambda=\langle \psi_0,\,\delta L\,D_0\rangle,}
\]
where \(D_0\) is the relevant unperturbed mode and \(\psi_0\) is the corresponding adjoint mode.

### 3.2 Where the “11” comes from

In the project’s asymptotic normalization, the GR modes scale as
\[
D_0\sim \Omega_m^{6/11},\qquad \psi_0\sim \Omega_m^{-5/11},
\]
so their product carries a simple weight \(\psi_0D_0\sim \Omega_m^{1/11}\). Evaluating the required overlaps with \(d\Omega_m/dN\simeq -3\Omega_m\) produces a clean rational factor \(1/11\), which the file explicitly identifies as the origin of the prime \(11\).

### 3.3 The final identification

With these overlaps, the pole shift computed from \(\delta\lambda\) translates into exactly the same growth-index correction,
\[
\gamma(k)=\frac{6}{11}-\frac{3}{55}\,\alpha_\infty(k),
\]
and the file emphasizes the conceptual point:

- \(6/11\) is the unperturbed pole location of the GR resolvent,
- \(3/55\) is the first-order pole shift under the Poisson enhancement.

---

## 4. Why this is a useful “hook” (and how to generalize it)

1. **General modified-growth models.** If a model’s only effect is to multiply the Poisson source term by a slowly varying factor, then the same perturbation-theory skeleton applies; the coefficient becomes a computable overlap, not an empirical constant.

2. **Scale dependence enters only through \(\alpha_\infty(k)\).** Once you accept the saturation hypothesis, the whole scale dependence is carried by the map \(k\mapsto \alpha_\infty(k)\); the rest is fixed algebra.

3. **A target for simulation cross-checks.** Even if the coefficient is derived analytically, it is easy to test numerically by integrating the growth equation with a constant enhancement and fitting \(\gamma\). If the simulation does not return \(-3/55\), you know exactly where the approximation broke.

