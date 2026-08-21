# Analytic Cosmological Signatures of Vacuum Stiffness Unification

## Purpose and scope

This document collects the most **testable analytic predictions** of the VSU perturbation sector, emphasizing quantities that:

1. depend on the stiffness enhancement only through a small set of scale-weighted combinations, and
2. do **not** require modifying the background expansion (geometry remains ΛCDM).

The emphasis is on late-time growth and its projections (RSD, lensing, ISW) together with “protected” geometric observables (BAO phase, Alcock–Paczynski consistency).

---

## Standing setup

- Background expansion: flat ΛCDM
  \[
  H^2(a)=H_0^2\left[\Omega_{m0}a^{-3}+\Omega_{\Lambda0}\right].
  \]
- Linear scalar sector: \(\Phi=\Psi\) (no slip), Weyl potential \(\Phi_W=\Phi+\Psi=2\Phi\).
- Modified Poisson coupling:
  \[
  \frac{k^2}{a^2}\Phi = 4\pi G_{\rm eff}(k,a)\,\bar\rho_m\,\delta,
  \qquad
  G_{\rm eff}(k,a)=G\,[1+\alpha_{\rm eff}(k,a)].
  \]
- Late-time saturation on fixed comoving scales:
  \[
  \alpha_{\rm eff}(k,a)\to\alpha_\infty(k),
  \qquad
  \partial_a\alpha_{\rm eff}\approx 0
  \quad (z\lesssim 2).
  \]

---

## 1) Growth index shift (late time)

Define the logarithmic growth rate \(f:=d\ln D/d\ln a\). In the Λ-dominated regime one may use
\[
f(a,k)\simeq \Omega_m(a)^{\gamma(k)}.
\]

Substituting into the late-time growth equation and expanding to leading order yields the scale-dependent growth index
\[
\boxed{
\gamma(k)=\frac{6}{11}-\frac{3}{55}\,\alpha_\infty(k).
}
\]

**Interpretation.** Positive \(\alpha_\infty\) enhances growth (reduces \(\gamma\)), but does not remove late-time freezing of \(D\).

---

## 2) Integrated Sachs–Wolfe signal: sign protected, amplitude suppressed

The ISW contribution satisfies
\[
\left(\frac{\Delta T}{T}\right)_{\rm ISW}=2\int d\eta\,\dot\Phi.
\]

Using
\[
\dot\Phi = H\Phi\left[f(k,a)-1+\frac{d\ln(1+\alpha_{\rm eff})}{d\ln a}\right],
\]
and late-time saturation \(d\ln(1+\alpha_{\rm eff})/d\ln a\to 0\), one finds
\[
\dot\Phi \simeq H\Phi\,[f(k,a)-1].
\]

Since \(\Phi<0\) in overdensities and \(f<1\) at late times, **the sign matches GR** (positive ISW temperature signal).

Define the amplitude ratio
\[
\mathcal R_{\rm ISW}(k,a):=\frac{\dot\Phi_{\rm VSU}}{\dot\Phi_{\rm GR}}
=\frac{1-f_{\rm VSU}(k,a)}{1-f_{\rm GR}(a)}.
\]
Expanding to first order in \(\alpha_\infty\),
\[
\boxed{
\mathcal R_{\rm ISW}(k,a)
\simeq
1+\frac{3}{55}\alpha_\infty(k)
\frac{\Omega_m(a)^{6/11}\ln\Omega_m(a)}{1-\Omega_m(a)^{6/11}}.
}
\]
Since \(\ln\Omega_m<0\), this implies **ISW suppression** when \(\alpha_\infty>0\).

---

## 3) Weak lensing and \(S_8\): window-averaged stiffness imprint

Weak lensing probes the Weyl potential, which here is \(2\Phi\). The convergence spectrum is
\[
P_\kappa(\ell)=\int_0^{\chi_H}d\chi\,\frac{W_L(\chi)^2}{\chi^2}\,
P_\Phi\!\left(k=\frac{\ell}{\chi},z(\chi)\right).
\]

At linear order, the only stiffness dependence entering \(\sigma_8\) and \(S_8\) is a window-weighted average of \(\alpha_\infty(k)\):
\[
\boxed{
\bar\alpha_\infty^{\rm lens}
=
\frac{
\int d\ln k\,W_8(k)^2P_{\rm ini}(k)\,\alpha_\infty(k)
}{
\int d\ln k\,W_8(k)^2P_{\rm ini}(k)
}.
}
\]

Expanding,
\[
\boxed{
S_8^{\rm VSU}
=
S_8^{\rm GR}\left[1-\frac{3}{55}\,\bar\alpha_\infty^{\rm lens}\,\mathcal I(0)\right],
}
\]
with \(\mathcal I(0)>0\) determined by the ΛCDM background integral. Thus \(\alpha_\infty>0\) implies a **downward shift in \(S_8\)** relative to GR for the same primordial normalization.

---

## 4) BAO phase protection

The BAO phase is sensitive to the time dependence of the gravitational potential during the photon–baryon acoustic oscillations. In the early-time domain one has \(\dot\Phi\to 0\), so the driving term does not induce a phase shift.

Thus, at leading order the BAO peak locations are protected:
\[
\boxed{\text{No BAO phase shift from vacuum stiffness (linear order).}}
\]

---

## 5) Alcock–Paczynski consistency: geometry remains ΛCDM

Because the homogeneous expansion history is fixed to ΛCDM, the mapping between observed angles/redshifts and comoving separations is unchanged. Therefore AP consistency relations remain those of standard cosmology:
\[
\boxed{\text{AP/BAO geometric inferences remain standard; deviations appear in growth.}}
\]

---

## Summary of “clean” observational handles

- **Geometry locked:** BAO peak positions, AP ratios follow ΛCDM.
- **Growth modified:** \(\gamma(k)=6/11-(3/55)\alpha_\infty(k)\).
- **ISW:** sign as in GR; amplitude **suppressed** for \(\alpha_\infty>0\).
- **Lensing:** \(S_8\) shifts through a lensing-window average \(\bar\alpha_\infty^{\rm lens}\).

These relations are analytic and can be used as a compact forward model for parameter inference once a model for \(\alpha_\infty(k)\) is specified.
