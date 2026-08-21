# Vacuum Stiffness Unification (VSU): exponential interpolation, screening, and late-time cosmology

\begin{center}
\textbf{Extracted from the VSU sequence (01–06): force law \(\mu(x)=1-e^{-x}\), screening/EFE, linear growth, and observable mappings.}
\end{center}

## 1. Core postulate: a single-scale nonlinear stiffness

In the nonrelativistic limit, VSU postulates an action
\[
S_{\mathrm{NR}}[\Phi]=\int dt\,d^3x\left[\frac{a_0^2}{8\pi G}F\left(\frac{|\nabla\Phi|^2}{a_0^2}\right)+\rho\Phi\right],
\]
with constitutive law
\[
\mu(x):=F'(x^2)=1-e^{-x}.
\]
Variation gives the modified Poisson equation
\[
\boxed{\ \nabla\cdot\big(\mu(|\nabla\Phi|/a_0)\nabla\Phi\big)=4\pi G\rho.\ }
\]
This is a quasilinear elliptic PDE whose nonlinearity depends only on the local field magnitude.

---

## 2. Two asymptotic regimes and their “built-in” predictions

For a spherically symmetric mass profile with Newtonian field \(g_N(r)=GM(r)/r^2\), the field satisfies
\[
\mu(g/a_0)\,g=g_N.
\]

### 2.1 Strong-field (screened) regime

If \(g\gg a_0\), then \(\mu\to 1\) exponentially fast, so
\[
\boxed{\ g\simeq g_N\quad\text{(Newtonian)},\qquad\text{corrections }\sim e^{-g/a_0}.\ }
\]

### 2.2 Weak-field (unscreened) regime

If \(g\ll a_0\), then \(\mu(x)\simeq x\), giving
\[
\boxed{\ g=\sqrt{a_0 g_N}.\ }
\]
For a point mass, \(g\propto 1/r\), hence \(\Phi\sim -\sqrt{GMa_0}\,\ln r\) at large \(r\).

### 2.3 BTFR and the screening radius

For circular orbits, \(g=V^2/r\). In the weak-field regime with total baryonic mass \(M_b\),
\[
\boxed{\ V^4 = G M_b a_0\ }\qquad(\text{BTFR slope }4).
\]
The transition occurs at
\[
\boxed{\ r_s:=\sqrt{GM/a_0}\ },
\]
defined by \(g_N(r_s)=a_0\).

---

## 3. External Field Effect (EFE) as an operator-level phenomenon

Because \(\mu\) depends on the **total** field magnitude \(|\nabla\Phi|\), a slowly varying external field \(\mathbf g_{\rm ext}\) modifies internal dynamics:
\[
\mathbf g=\mathbf g_{\rm int}+\mathbf g_{\rm ext}.
\]
If \(|\mathbf g_{\rm ext}|\gg a_0\), then \(\mu(|\mathbf g|/a_0)\simeq 1\) even when \(|\mathbf g_{\rm int}|\ll a_0\), implying
\[
\boxed{\ \nabla^2\Phi_{\rm int}=4\pi G\rho_{\rm int}+O\big(a_0/|\mathbf g_{\rm ext}|\big).\ }
\]
So “screening” and “EFE” are two faces of the same quasilinear operator.

---

## 4. Linear cosmology: keep \(H(a)\) \(\Lambda\)CDM, modify perturbations

The background expansion is fixed to flat \(\Lambda\)CDM:
\[
H^2(a)=H_0^2\big[\Omega_{m0}a^{-3}+\Omega_{\Lambda0}\big].
\]
Scalar perturbations in Newtonian gauge satisfy \(\Phi=\Psi\) at linear order.

On sub-horizon scales, the matter contrast obeys a modified growth equation
\[
\boxed{\ \ddot\delta+2H\dot\delta-4\pi G\bar\rho_m\big[1+\alpha_{\rm eff}(k,a)\big]\delta=0,\ }
\]
with a scale- and time-dependent effective coupling
\[
G_{\rm eff}(k,a)=G\,[1+\alpha_{\rm eff}(k,a)].
\]
Late-time asymptotics are summarized by a scale-dependent growth index
\[
\gamma(k)=\frac{6}{11}-\frac{3}{55}\alpha_\infty(k),\qquad f=\Omega_m^{\gamma(k)},
\]
and the mapping to weak lensing includes a window-averaged enhancement \(\bar\alpha_\infty^{\rm lens}\) controlling \(S_8\).

---

## 5. A sharp caveat (and a concrete repair plan): the covariant scalar’s domain

Several covariant formulas use
\[
X:=\frac{g^{\mu\nu}\nabla_\mu\phi\nabla_\nu\phi}{a_0^2}
\]
and simultaneously write \(F'(X)=1-e^{-\sqrt{X}}\). But for a homogeneous time-dependent field \(\phi(t)\), one has \(X=-\dot\phi^2/a_0^2<0\), so \(\sqrt{X}\) is not real.

A minimal, technically clean repair is to redefine the invariant as
\[
X_\star:= -\frac{g^{\mu\nu}\nabla_\mu\phi\nabla_\nu\phi}{a_0^2}\ge 0\quad\text{for timelike gradients},
\]
and set \(F'(X_\star)=1-e^{-\sqrt{X_\star}}\). This preserves:

- the nonrelativistic reduction (spacelike gradients \(\Rightarrow X_\star\approx |\nabla\Phi|^2/a_0^2\)),
- the hyperbolicity calculation (with \(X_\star\) positive),
- the stress–energy algebra,

while eliminating the sign inconsistency.

A second cleanup flagged by the project’s lint is that quantities like \(m_{\rm eff}\) (appearing in \(\alpha_{\rm eff}(k,a)\)) need an explicit definition: e.g. as a background-dependent effective mass extracted from the second variation of the scalar action around \(\phi_0(t)\).

---

## 6. Why this is interesting (as a research direction)

VSU is an aggressively minimal “single-scale” modification: one new parameter \(a_0\), a fixed interpolation \(\mu(x)=1-e^{-x}\), automatic screening and an EFE, and a cosmological sector designed to keep background distances \(\Lambda\)CDM-like while allowing modified clustering. The most leveraged next steps are:

1. make the covariant invariant choice and global domain explicit (timelike vs spacelike gradients);
2. derive \(m_{\rm eff}\) and \(\alpha_{\rm eff}(k,a)\) from the covariant action without hand-inserted factors;
3. test whether the same \(a_0\) that fits galactic BTFR can produce the required late-time \(S_8\)/ISW shifts without spoiling CMB/BAO.
