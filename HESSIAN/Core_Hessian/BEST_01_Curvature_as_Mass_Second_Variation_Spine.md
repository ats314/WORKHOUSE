# Curvature-as-Mass: the Second-Variation Spine (Continuum ↔ Cosmology ↔ Lattice ↔ OS)

## Why this document exists

This project repeatedly produces the same mathematical object in different disguises:

- **Continuum stiffness gravity:** the *second variation* (Hessian) of a convex vacuum Hamiltonian,
- **Linear cosmology:** the *Fourier symbol* of the linearized stiffness operator (plus an IR completion),
- **Lattice gauge:** the *Bakry–Émery curvature endomorphism* (Ricci + Wilson Hessian),
- **OS reconstruction:** the *Hamiltonian spectral gap* extracted from Euclidean-time decay.

The nontrivial claim with theory-building potential is that **“mass” is not a parameter** but a **spectral datum of a second variation operator**—i.e. a curvature lower bound in configuration space.

This file isolates the shared algebraic spine.

---

## 1. Continuum: convex energy ⇒ linearized operator is a Hessian

### 1.1 Vacuum stiffness energy and Euler–Lagrange equation

Take the nonrelativistic energy functional
\[
\mathcal E[\Phi]
=
\int_{\mathbb R^3}\left[
\frac{a_0^2}{8\pi G}\,
F\!\left(\frac{|\nabla\Phi|^2}{a_0^2}\right)
+\rho\,\Phi\right]\,dx,
\qquad
F'(Y)=\mu(\sqrt{Y}),\quad \mu(x)=1-e^{-x}.
\]

Its Euler–Lagrange equation is the quasilinear Poisson law
\[
\nabla\cdot\!\left(\mu\!\left(\frac{|\nabla\Phi|}{a_0}\right)\nabla\Phi\right)=4\pi G\rho.
\]

### 1.2 Second variation with respect to the field gradient

Let
\[
p:=\nabla\Phi,\qquad \mathcal H(p):=\frac{a_0^2}{8\pi G}\,F\!\left(\frac{|p|^2}{a_0^2}\right).
\]
Then
\[
\nabla_p\mathcal H(p)=\frac{1}{4\pi G}\,\mu(|p|/a_0)\,p,
\]
and the Hessian in the gradient variable is
\[
D_p^2\mathcal H(p)
=
\frac{1}{4\pi G}
\left[
\mu(|p|/a_0)\,I
+\frac{\mu'(|p|/a_0)}{a_0|p|}\,p\otimes p
\right],
\qquad \mu'(x)=e^{-x}>0.
\]
This is **positive definite** for \(p\neq 0\). Convexity is strict.

### 1.3 Linearization about a background field

Let \(\Phi=\Phi_0+\varepsilon\varphi\) with background gradient \(p_0=\nabla\Phi_0\), \(g_0=|p_0|\), \(s_0=g_0/a_0\).
Then the linearized flux derivative (stiffness tensor) is
\[
K_0(x):=4\pi G\,D_p^2\mathcal H(p_0(x))
=
\mu(s_0(x))\,I+\frac{\mu'(s_0(x))}{a_0 g_0(x)}\,p_0(x)\otimes p_0(x),
\]
and the **linearized continuum operator** is the divergence-form Hessian operator
\[
\boxed{\;\mathcal L_{\Phi_0}\varphi:=-\nabla\cdot\big(K_0(x)\nabla\varphi\big).\;}
\]

This is the continuum template: linear response is controlled by a **second variation** (curvature) object.

---

## 2. Fourier variables: the Yukawa denominator is a resolvent of the Hessian

### 2.1 Translation-invariant / locally isotropic regime

If \(K_0\) is approximately constant over a patch, the Fourier symbol is
\[
\widehat{\mathcal L_{\Phi_0}}(k)\approx k^\top K_0\,k.
\]
In an isotropized regime \(K_0\approx \mu_{\rm iso} I\), this becomes \(\mu_{\rm iso}k^2\).

Then the *uncompleted* linear response has the Coulombic form
\[
\hat\varphi(k)\propto \frac{1}{k^\top K_0\,k}\,\widehat{\delta\rho}(k)
\quad\text{or}\quad
\hat\varphi(k)\propto \frac{1}{\mu_{\rm iso}k^2}\,\widehat{\delta\rho}(k).
\]

### 2.2 IR completion as a spectral datum (not an inserted scale)

To define an IR scale without adding a new parameter, place the operator on a causal patch \(\Omega_H(a)\) and take the **first nonzero eigenvalue**
\[
\lambda_1(a):=\inf_{\psi\perp 1}\frac{\langle \psi,\mathcal L_{\Phi_0}^{(a)}\psi\rangle}{\langle \psi,\psi\rangle}.
\]
Define
\[
\boxed{\lambda_{\min}(a):=\lambda_1(a)=a^2m_{\rm eff}(a)^2.}
\]

The IR-completed resolvent is then
\[
(\mathcal L_{\Phi_0}^{(a)}+\lambda_1(a))\varphi = 4\pi G\,\delta\rho,
\]
so in Fourier variables (locally translation invariant),
\[
\boxed{\;
\hat\varphi(k)\;\sim\;\frac{1}{k^2+a^2m_{\rm eff}(a)^2}\times(\text{Hessian}/\mu\text{ factor})\;\widehat{\delta\rho}(k).
\;}
\]

This is exactly the “cosmology structural factor” you asked to justify:
\[
(k^2+a^2m_{\rm eff}^2)^{-1}\times(\cdots).
\]

The point: \(m_{\rm eff}\) is a **lowest-eigenvalue parameter** of \(\mathcal L_{\Phi_0}\), i.e. a curvature floor.

---

## 3. Lattice gauge: curvature endomorphism ⇒ a built-in mass scale \(m_H\)

The lattice stack implements the same logic on configuration space \(M_\Lambda=G^{E(\Lambda)}\):

- the Gibbs weight is \(d\mu\propto e^{-S}\,d\mathrm{vol}_g\),
- the generator \(L\) is \(\mu\)-symmetric,
- the Bakry–Émery curvature endomorphism is
  \[
  \mathrm{Ric}_\mu=\mathrm{Ric}_g+\nabla^2S.
  \]

### 3.1 Vacuum Hessian = discrete Maxwell stiffness

At the vacuum configuration \(U^{(0)}\), the Wilson action Hessian reduces to a discrete Maxwell operator:
\[
\nabla^2S(U^{(0)})=\alpha_W\,d_1^*d_1.
\]
The *geometric* Ricci term of the product group manifold gives a uniform positive contribution
\[
\mathrm{Ric}_g\succeq \kappa_G I.
\]
The lattice pipeline defines
\[
m_H^2:=\kappa_G/3,
\qquad
M_{\Lambda}:=m_H^2 I+\alpha_W d_1^*d_1,
\]
and then aims to prove a **matrix hinge** on a canonical good set \(\mathcal K_{\Lambda,\beta}\):
\[
\boxed{\;\mathrm{Ric}_\mu(U)\succeq M_{\Lambda}^{\mathrm{hinge}}
\quad\text{for }U\in\mathcal K_{\Lambda,\beta}.\;}
\]
(Here \(M^{\mathrm{hinge}}\) is a slightly weakened but deterministic operator, e.g.
\(m_H^2 I+\tfrac12\alpha_W d_1^*d_1\).)

**Interpretation:** \(m_H\) is literally a **curvature lower bound** in configuration space; it plays the exact role of a “mass term” in the inverse kernel.

### 3.2 Helffer–Sjöstrand: covariance is controlled by an inverse Hessian-like operator

The HS identity expresses covariance as
\[
\mathrm{Cov}_\mu(F,G)
=
\int\left\langle \nabla F,\ (\mathcal L^{(1)})^{-1}\nabla G\right\rangle\,d\mu,
\]
where \(\mathcal L^{(1)}\) is the Witten Laplacian on gradients:
\[
\mathcal L^{(1)} = ((-L)\otimes I)+\mathrm{Ric}_\mu.
\]
Since \(((-L)\otimes I)\succeq 0\), a pointwise hinge \(\mathrm{Ric}_\mu\succeq M\) implies
\[
\mathcal L^{(1)}\succeq M
\quad\Rightarrow\quad
(\mathcal L^{(1)})^{-1}\preceq M^{-1}.
\]
Thus the decay of correlations reduces to the decay of a **deterministic inverse kernel** \(M^{-1}\), i.e. a massive Green’s function.

### 3.3 Combes–Thomas / Davies: finite-range + positivity ⇒ exponential kernel decay

The massive Maxwell operator is finite-range and strictly positive, so standard conjugation arguments yield
\[
\|(M^{-1})_{xy}\|\lesssim e^{-\eta\,\mathrm{dist}(x,y)}.
\]
The decay rate \(\eta\) is controlled by the mass floor \(m_H\) (and the stiffness term).

This is the lattice analogue of “Yukawa denominator”: inverse kernels decay exponentially because the operator has a **spectral gap**.

---

## 4. OS reconstruction: Euclidean decay ⇒ Hamiltonian mass gap

Reflection positivity + time translation invariance (Appendix K/L) reconstruct an OS Hilbert space and a positive contraction \(T\) implementing one-step Euclidean time evolution, with
\[
T=e^{-aH},\qquad H\ge 0.
\]
A spectral-support lemma shows:

> If centered Euclidean-time correlations decay like \(\exp(-\eta n)\), then the reconstructed Hamiltonian has a spectral gap \(\mathrm{gap}(H)\ge \eta/a\).

So the lattice “mass” extracted from OS reconstruction is again a **gap**—a spectral datum forced by curvature-induced clustering.

---

## 5. Working dictionary (the theory-bridge content)

The project already contains a natural “mass dictionary”:

- **Continuum cosmology:** \(a^2m_{\rm eff}^2=\lambda_1(\mathcal L_{\Phi_0}^{(a)})\) (IR spectral closure).
- **Lattice gauge:** \(m_H^2\) is a curvature floor in \(\mathrm{Ric}_g\), which feeds into \(\mathrm{Ric}_\mu=\mathrm{Ric}_g+\nabla^2S\), which controls \(M^{-1}\), which controls Euclidean decay, which controls the OS Hamiltonian gap.

This is the clean, non-metaphorical statement:
\[
\boxed{\text{“Mass” = (lower bound on) second variation = curvature floor = spectral gap parameter.}}
\]

---

## 6. The single missing hinge that would collapse the lattice stack into a theorem

The lattice pipeline is structurally complete except for a single local analytic bound:

**Core-5.EI.1:** a volume-uniform small-field stability estimate comparing \(\nabla^2S(U)\) to \(\nabla^2S(U^{(0)})\) on \(\mathcal K_{\Lambda,\beta}\).

Proving that estimate turns the “matrix hinge” from an external input into a lemma, and the rest of the mass-gap pipeline becomes a deterministic consequence of the already-written appendices.

That is the sharpest “one missing brick” in the entire corpus.

