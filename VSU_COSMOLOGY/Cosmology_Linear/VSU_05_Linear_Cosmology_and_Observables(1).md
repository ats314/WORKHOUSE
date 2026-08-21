# VSU 05 — Linear Cosmology and Observable Projections (Analytic Skeleton + Two Consistency Stress Tests)

**Scope.** This note curates the linear-cosmology layer of VSU as it is written in the project files:

- background expansion fixed to flat \(\Lambda\)CDM,
- scalar perturbations in Newtonian gauge with \(\Phi=\Psi\),
- a modified Poisson sector encoded as \(G_{\rm eff}(k,a)=G[1+\alpha_{\rm eff}(k,a)]\),
- the resulting growth equation, and late-time asymptotics,
- analytic predictions for ISW, BAO, and Alcock–Paczynski (AP),
- a sign-consistency check for the weak-lensing mapping.

**Primary sources:** `03.1_Background_Cosmology.md`, `03.2_Scalar_Perturbations.md`, `03.3_Matter_Growth_Equation.md`, `03.5_Late_Time_Asymptotics.md`, `04.2_Weak_Lensing_and_S8.md`, `04.3_ISW_Sign_and_Amplitude.md`, `04.4_BAO_Phase_and_Peaks.md`, `04.5_Alcock_Paczynski_Consistency.md`.

---

## 1. Background: geometry unchanged by assumption

The project fixes the homogeneous background to flat matter+\(\Lambda\):

\[
ds^2=-dt^2+a^2(t)d\mathbf x^2,
\qquad
H^2(a)=H_0^2\left[\Omega_{m0}a^{-3}+\Omega_{\Lambda0}\right],
\qquad
\Omega_{m0}+\Omega_{\Lambda0}=1.
\]

This is a strong structural choice: **BAO and AP become purely geometric and GR-like at the background level**.

---

## 2. Linear scalar perturbations: \(\Phi=\Psi\) and the coupled system

In Newtonian gauge,

\[
ds^2=-(1+2\Phi)dt^2+a^2(t)(1-2\Psi)d\mathbf x^2.
\]

At linear order (project assumption: no anisotropic stress from matter or the scalar), one gets

\[
\boxed{\Phi=\Psi.}
\]

The time–time Einstein constraint (Fourier space) is written as

\[
\frac{k^2}{a^2}\Phi
=
4\pi G\left(\bar\rho_m\,\delta+\delta\rho_\phi\right),
\]
with \(\delta\rho_\phi\) expressed in terms of \(\delta\phi\) and \(\Phi\).

This is the project’s starting point for defining an effective gravitational coupling.

---

## 3. Growth equation and \(G_{\rm eff}\)

On sub-horizon scales, eliminating the velocity potential yields the standard form

\[
\ddot\delta+2H\dot\delta-\frac{k^2}{a^2}\Phi=0.
\]

Defining
\[
\frac{k^2}{a^2}\Phi
=
4\pi G_{\rm eff}(k,a)\bar\rho_m\,\delta,
\qquad
G_{\rm eff}(k,a)=G[1+\alpha_{\rm eff}(k,a)],
\]
gives the closed growth equation

\[
\boxed{
\ddot\delta+2H\dot\delta
-
4\pi G\bar\rho_m\,[1+\alpha_{\rm eff}(k,a)]\,\delta=0.
}
\]

### 3.1 Consistency stress test: GR limit of the \(\alpha_{\rm eff}\) ansatz

`03.3_Matter_Growth_Equation.md` proposes
\[
\alpha_{\rm eff}(k,a)
=
\frac{k^2}{k^2+a^2m_{\rm eff}^2}\,
\frac{1}{\mu(g/a_0)}.
\]

Two immediate observations:

1. If \(\mu\to 1\) (high-acceleration / screened), this becomes
   \(\alpha_{\rm eff}\to k^2/(k^2+a^2m_{\rm eff}^2)\), which does **not** vanish on small scales \(k\gg am_{\rm eff}\).  
   So GR recovery is not automatic without extra structure.
2. A GR-consistent Yukawa-filtered enhancement usually has the form
   \[
   \alpha_{\rm eff}\sim \left(\frac{1}{\mu}-1\right)\frac{k^2}{k^2+a^2m_{\rm eff}^2},
   \]
   so that \(\mu\to 1\Rightarrow \alpha_{\rm eff}\to 0\) at fixed \(k\).

This is not fatal, but it is one of the places where the project’s “minimality” narrative depends on getting the algebra exactly right.

---

## 4. Late-time asymptotics: growth index shift

For \(z\lesssim 2\), the project assumes saturation
\[
\alpha_{\rm eff}(k,a)\to\alpha_\infty(k),
\qquad \partial_a\alpha_{\rm eff}\approx 0.
\]

Using the growth-index ansatz \(f\simeq \Omega_m^{\gamma(k)}\), it derives

\[
\boxed{
\gamma(k)=\frac{6}{11}-\frac{3}{55}\alpha_\infty(k).
}
\]

So \(\alpha_\infty>0\) lowers \(\gamma\) and increases the growth rate \(f\) relative to GR, while still allowing eventual freeze-out under \(\Lambda\) domination.

---

## 5. ISW: sign unchanged, amplitude suppressed for \(\alpha_\infty>0\)

`04.3_ISW_Sign_and_Amplitude.md` writes

\[
\dot\Phi
=
H\Phi\left[f(k,a)-1+\frac{d\ln(1+\alpha_{\rm eff})}{d\ln a}\right].
\]

At late times \(d\ln(1+\alpha_{\rm eff})/d\ln a\to 0\), so \(\dot\Phi\propto (f-1)\). Since \(0<f<1\) at late times, \(\dot\Phi<0\) and the ISW sign matches GR.

The project’s amplitude ratio is

\[
\boxed{
\mathcal R_{\rm ISW}(k,a)\simeq
1+\frac{3}{55}\alpha_\infty(k)\,
\frac{\Omega_m(a)^{6/11}\ln\Omega_m(a)}{1-\Omega_m(a)^{6/11}}.
}
\]

Because \(\ln\Omega_m(a)<0\) for \(\Omega_m<1\), \(\alpha_\infty>0\Rightarrow \mathcal R_{\rm ISW}<1\): suppressed ISW amplitude.

---

## 6. BAO: no phase shift, peaks unchanged

The BAO phase is set by the sound horizon \(r_s\) at recombination:

\[
r_s(\eta_*)=\int_0^{\eta_*}c_s(\eta)\,d\eta.
\]

The project argues:

- background expansion is unchanged,
- early-time \(\alpha_{\rm eff}\to 0\),
- \(\Phi\) is effectively constant during acoustic oscillations.

Therefore

\[
\boxed{\Delta\phi_{\rm BAO}=0,}
\]
and BAO peak positions are invariant (only late-time amplitudes can change through \(D(k,z)\)).

---

## 7. Alcock–Paczynski (AP): purely geometric, unchanged

The AP observable is

\[
F_{\rm AP}(z)=(1+z)D_A(z)H(z).
\]

Since \(H(z)\) and distances are fixed to \(\Lambda\)CDM in the project’s background choice,

\[
\boxed{
F_{\rm AP}^{\rm VSU}(z)=F_{\rm AP}^{\rm GR}(z).
}
\]

This makes AP/BAO a clean way to separate geometry from growth in multi-probe tests.

---

## 8. Weak lensing and \(S_8\): sign consistency check

`04.2_Weak_Lensing_and_S8.md` writes the late-time enhancement of \(\sigma_8\) in terms of

\[
\mathcal I(z)=\int_z^\infty \frac{dz'}{1+z'}\,\Omega_m(z')^{6/11}\ln\Omega_m(z'),
\]
and then states “\(\mathcal I(0)>0\)”, implying \(\alpha_\infty>0\Rightarrow S_8^{\rm VSU}<S_8^{\rm GR}\).

**But:** for a \(\Lambda\)CDM-like background, \(0<\Omega_m(z')\le 1\) for finite \(z'\), so \(\ln\Omega_m(z')\le 0\). The prefactor \(dz'/(1+z')\) and \(\Omega_m^{6/11}\) are positive. Therefore

\[
\boxed{\mathcal I(z)\le 0\ \text{for all finite }z.}
\]

So either:

- the file’s \(\mathcal I\) is missing an overall minus sign, **or**
- a sign convention differs between the late-time asymptotics and the lensing mapping, **or**
- the claim “\(S_8\) decreases for \(\alpha_\infty>0\)” is contingent on parameter refits (e.g. lowering \(A_s\) to keep CMB fixed), which needs to be stated explicitly.

This is a small-looking sign, but it flips the qualitative lensing prediction.

---

## 9. Where this becomes a *test program* (not just algebra)

Because the background is fixed, the model is unusually overconstrained:

- BAO/AP nail distances,
- growth (RSD) nails \(f\sigma_8\),
- lensing nails a different kernel-weighted combination of \(D\) and \(G_{\rm eff}\),
- ISW nails the time derivative of potentials.

If VSU has real teeth, the same \(\alpha_{\rm eff}(k,a)\) must fit *all four* without hidden re-tunings.

---

## References (project files)

- `03.1_Background_Cosmology.md`
- `03.2_Scalar_Perturbations.md`
- `03.3_Matter_Growth_Equation.md`
- `03.5_Late_Time_Asymptotics.md`
- `04.2_Weak_Lensing_and_S8.md`
- `04.3_ISW_Sign_and_Amplitude.md`
- `04.4_BAO_Phase_and_Peaks.md`
- `04.5_Alcock_Paczynski_Consistency.md`
