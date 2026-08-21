# VSU Linear Cosmology and Observable Projections (Analytic Skeleton + Consistency Notes)

## Abstract

This note curates the linear-cosmology layer of VSU:

- background expansion fixed to flat \(\Lambda\)CDM,
- scalar perturbations in Newtonian gauge with \(\Phi=\Psi\),
- modified Poisson equation encoded in \(G_{\rm eff}(k,a)=G[1+\alpha_{\rm eff}(k,a)]\),
- the resulting linear growth equation for \(\delta\) and \(D(a,k)\),
- late-time asymptotics (\(z\lesssim 2\)) with a scale-dependent growth index,
- analytic sign/magnitude predictions for ISW, weak lensing, BAO, and AP.

Where helpful, I include brief consistency checks and one numerical constant.

---

## 1. Background: geometry unchanged

Assume spatially flat FLRW,
\[
ds^2=-dt^2+a^2(t)d\mathbf x^2,\qquad H:=\frac{\dot a}{a}.
\]

Matter+\(\Lambda\) gives
\[
\boxed{
H^2(a)=H_0^2\left[\Omega_{m0}a^{-3}+\Omega_{\Lambda 0}\right],
\qquad
\Omega_{m0}+\Omega_{\Lambda 0}=1.
}
\]

Define the time-dependent matter fraction
\[
\boxed{
\Omega_m(a)=\frac{\Omega_{m0}a^{-3}}{\Omega_{m0}a^{-3}+\Omega_{\Lambda0}}.
}
\]

So all distance indicators (BAO rulers, AP distortions) remain *geometric* and \(\Lambda\)CDM-like at the background level.

---

## 2. Scalar perturbations and \(\Phi=\Psi\)

In Newtonian gauge,
\[
ds^2=-(1+2\Phi)\,dt^2+a^2(t)(1-2\Psi)\,d\mathbf x^2.
\]

At linear order, the scalar sector carries no anisotropic stress in this construction, so
\[
\boxed{\Phi=\Psi.}
\]

Weak lensing therefore probes the Weyl potential \(\Phi_W=\Phi+\Psi=2\Phi\).

---

## 3. Modified Poisson equation \(\Rightarrow\) effective gravitational coupling

On sub-horizon scales, the scalar contribution can be packaged into an effective coupling
\[
\boxed{
\frac{k^2}{a^2}\Phi = 4\pi G_{\rm eff}(k,a)\,\bar\rho_m\,\delta,
\qquad
G_{\rm eff}(k,a)=G[1+\alpha_{\rm eff}(k,a)].
}
\]

In the VSU narrative, \(\alpha_{\rm eff}\) becomes:
- small at early times and/or large scales,
- saturated to \(\alpha_\infty(k)\) at late times on fixed comoving scales,
- suppressed in strong-field environments via the same \(\mu(g/a_0)\) nonlinearity.

(An explicit expression for \(\alpha_{\rm eff}\) is model-dependent; the key point is that it is **not** a free function tuned per dataset.)

---

## 4. Linear growth equation

For pressureless matter, combining the continuity + Euler equations yields (sub-horizon)
\[
\ddot\delta+2H\dot\delta-\frac{k^2}{a^2}\Phi=0.
\]
Using the modified Poisson relation gives the fundamental growth equation
\[
\boxed{
\ddot\delta+2H\dot\delta
-
4\pi G\bar\rho_m\,[1+\alpha_{\rm eff}(k,a)]\,\delta
=0.
}
\]

In terms of the growth factor \(D(a,k)\) (with \(\delta\propto D\)),
\[
\boxed{
D''+\left(\frac{3}{a}+\frac{1}{H}\frac{dH}{da}\right)D'
-
\frac{3}{2}\frac{\Omega_m(a)}{a^2}[1+\alpha_{\rm eff}(k,a)]D=0.
}
\]

Define the logarithmic growth rate \(f:=d\ln D/d\ln a\). Then
\[
\boxed{
\frac{df}{d\ln a}+f^2+\left(2+\frac{d\ln H}{d\ln a}\right)f
=
\frac{3}{2}\Omega_m(a)\,[1+\alpha_{\rm eff}(k,a)].
}
\]

---

## 5. Late-time asymptotics (\(z\lesssim 2\)): growth index shift

Assume the enhancement saturates:
\[
\alpha_{\rm eff}(k,a)\to\alpha_\infty(k),\qquad \partial_a\alpha_{\rm eff}\approx 0.
\]

Adopt the growth-index form
\[
f(a,k)\simeq \Omega_m(a)^{\gamma(k)}.
\]

Expanding to leading order gives
\[
\boxed{
\gamma(k)=\frac{6}{11}-\frac{3}{55}\alpha_\infty(k).
}
\]

So \(\alpha_\infty(k)>0\) lowers \(\gamma\) and increases \(f\) at late times (since \(\Omega_m<1\)).

### 5.1 Relative growth-factor enhancement

A convenient analytic ratio is
\[
\mathcal R_D(k,a):=\frac{D_{\rm VSU}(k,a)}{D_{\rm GR}(a)}
\simeq
\exp\!\left[
-\frac{3}{55}\alpha_\infty(k)\int^a\frac{da'}{a'}\Omega_m(a')^{6/11}\ln\Omega_m(a')
\right].
\]

Because \(\Omega_m<1\) at late times, \(\ln\Omega_m<0\), so the integral is negative and **\(\alpha_\infty>0\) enhances growth**.

For a representative \(\Omega_{m0}=0.3\), the integral to \(a=1\) evaluates to approximately
\[
\int_0^1\frac{da'}{a'}\Omega_m(a')^{6/11}\ln\Omega_m(a')
\approx -0.383,
\]
so at \(z=0\),
\[
\mathcal R_D(k,1)\approx \exp\!\bigl(0.021\,\alpha_\infty(k)\bigr).
\]

---

## 6. ISW: sign unchanged, amplitude suppressed (for \(\alpha_\infty>0\))

The ISW temperature shift is
\[
\left(\frac{\Delta T}{T}\right)_{\rm ISW}=2\int d\eta\,\dot\Phi.
\]

Using \(\Phi\propto \mathcal G\,D/a\) with \(\mathcal G:=1+\alpha_{\rm eff}\), one finds
\[
\dot\Phi=H\Phi\left[f-1+\frac{d\ln\mathcal G}{d\ln a}\right].
\]

At late times \(\alpha_{\rm eff}\to\alpha_\infty\) (time-independent), so \(d\ln\mathcal G/d\ln a\to 0\) and
\[
\dot\Phi\simeq H\Phi\,(f-1).
\]

Since overdensities have \(\Phi<0\) and \(f<1\) at late times, \(\dot\Phi<0\), implying the **same ISW sign** as GR (a positive ISW temperature signal).

To first order in \(\alpha_\infty\), an analytic ratio is
\[
\boxed{
\mathcal R_{\rm ISW}(k,a)
:=
\frac{\dot\Phi_{\rm VSU}}{\dot\Phi_{\rm GR}}
\simeq
1+\frac{3}{55}\alpha_\infty(k)
\frac{\Omega_m(a)^{6/11}\ln\Omega_m(a)}{1-\Omega_m(a)^{6/11}}.
}
\]
Because \(\ln\Omega_m<0\), the bracket is negative, so \(\alpha_\infty>0\) gives \(\mathcal R_{\rm ISW}<1\): **suppressed ISW amplitude**.

---

## 7. Weak lensing and \(S_8\): kernel-weighted sensitivity

With \(\Phi=\Psi\), the convergence power spectrum is
\[
P_\kappa(\ell)
=
\int d\chi\,\frac{W_L^2(\chi)}{\chi^2}\,
P_\Phi\!\left(k=\frac{\ell}{\chi},z(\chi)\right),
\]
and
\[
P_\Phi(k,a)
=
\left(\frac{3}{2}\frac{H_0^2\Omega_{m0}}{k^2}\right)^2
\mathcal G^2(k,a)\frac{D^2(k,a)}{a^2}P_{\rm ini}(k).
\]

A useful compression is the lensing-weighted enhancement
\[
\boxed{
\bar\alpha_\infty^{\rm lens}=
\frac{\int d\ln k\,W_8^2(k)P_{\rm ini}(k)\alpha_\infty(k)}{\int d\ln k\,W_8^2(k)P_{\rm ini}(k)}.
}
\]

### 7.1 Consistency note about the sign in the project text

A common integral used in the expansion is
\[
\mathcal I(z)=\int_z^\infty \frac{dz'}{1+z'}\,\Omega_m(z')^{6/11}\ln\Omega_m(z').
\]
Since \(\Omega_m(z')\le 1\) and \(\ln\Omega_m\le 0\) for finite \(z'\), **\(\mathcal I(z)\) is non-positive** for standard \(\Lambda\)CDM backgrounds.

So, holding the primordial amplitude fixed, \(\alpha_\infty>0\) increases \(D\) and therefore increases \(\sigma_8\) and \(S_8\).  
If one wants \(S_8\) to *decrease*, this must come from either (i) a different sign convention, (ii) different physics in \(\mathcal G\) vs growth, or (iii) parameter re-fitting (e.g., lowering \(A_s\)) when matching CMB constraints.

---

## 8. BAO: phase and peak positions unchanged

BAO peak positions are set by the sound horizon at recombination,
\[
r_s(\eta_*)=\int_0^{\eta_*}c_s(\eta)\,d\eta,
\qquad k_n r_s(\eta_*)=n\pi.
\]

Because the background expansion and photon–baryon physics are unmodified, \(r_s\) is unchanged.  
Further, the model is constructed so that early-time modifications vanish (so \(\Phi\) is nearly constant during oscillations), preventing a phase shift.

Therefore:
\[
\boxed{\Delta\phi_{\rm BAO}=0,\quad \text{BAO peak positions are invariant.}}
\]

Only **late-time amplitudes** can shift via \(D(k,z)\).

---

## 9. Alcock–Paczynski (AP): purely geometric, unchanged

The AP observable
\[
F_{\rm AP}(z)=(1+z)D_A(z)H(z)
\]
depends only on the background \(H(z)\) and distances. Since the background is \(\Lambda\)CDM-like,
\[
\boxed{F_{\rm AP}^{\rm VSU}(z)=F_{\rm AP}^{\rm GR}(z).}
\]

Thus AP + BAO form an internal “geometry lock,” while RSD + lensing probe growth.

---

## 10. What this linear layer buys you

This architecture is attractive because it creates **correlated, cross-checkable predictions**:

- geometry observables (BAO/AP) stay standard,
- growth observables shift in a tied way via \(\alpha_\infty(k)\),
- ISW suppression emerges with a definite sign for \(\alpha_\infty>0\),
- lensing and RSD measure different window-averages of \(\alpha_\infty(k)\),
- nonlinear structure (collapse/bias) can lift degeneracies further.

