# IR Closure in Linear Cosmology: Causal Patch Gap, Fixed Geometry Constant, and Non-Circular \(\mu_{\rm iso}(a)\)

## What this document extracts (and why)

This is the distilled “IR closure block” of the cosmology stack, merging:

- `VSU_IR_Closure_Causal_Patch_Spectral_Gap_and_Yukawa_Kernel.md`
- `VSU_IR_Closure_mu_iso_field_strength_proxy.md`
- the modified Poisson coupling interface in `03.3_Matter_Growth_Equation.md`

The goal is a *closed* and *non-circular* definition of:
\[
\lambda_{\min}(a)=a^2m_{\rm eff}(a)^2,
\qquad
\alpha_{\rm eff}(k,a),
\qquad
\mu_{\rm iso}(a),
\]
with no new phenomenological parameters once the causal patch geometry is fixed.

---

## 1. Linearization about a background: the continuum stiffness operator

Let \(\Phi_0\) be a background solution (in the quasi-static scalar sector). Define
\[
p_0(x)=\nabla\Phi_0(x),
\qquad
g_0(x)=|p_0(x)|,
\qquad
s_0(x)=\frac{g_0(x)}{a_0}.
\]

With \(\mu(x)=1-e^{-x}\) and \(\mu'(x)=e^{-x}\), the linearized stiffness tensor is
\[
K_0(x)=\mu(s_0(x))\,I+\frac{\mu'(s_0(x))}{a_0 g_0(x)}\,p_0(x)\otimes p_0(x),
\]
and the linearized spatial operator is the divergence-form Hessian operator
\[
\boxed{\;\mathcal L_{\Phi_0}\varphi:=-\nabla\cdot(K_0(x)\nabla\varphi).\;}
\]

In an isotropized regime, define the scalar reduction
\[
\boxed{\;\mu_{\rm iso}(a):=\mu(s_0(a))+\frac13\,s_0(a)\,\mu'(s_0(a)).\;}
\]
Then locally \(\mathcal L_{\Phi_0}\approx -\mu_{\rm iso}(a)\Delta\).

---

## 2. IR mechanism: causal comoving patch spectral gap

### 2.1 Fix the IR domain (geometry choice)

Take the causal comoving patch to be a 3-torus of comoving side length equal to the comoving horizon scale:
\[
\boxed{\;\Omega_H(a)=\mathbb T^3_{L_H(a)},\qquad L_H(a):=\frac{c}{aH(a)}.\;}
\]

This fixes the geometry constant uniquely.

### 2.2 Define the IR spectral datum

Realize \(\mathcal L_{\Phi_0}\) on \(\Omega_H(a)\) with periodic boundary conditions and restrict to the mean-zero sector
\[
L^2_0(\Omega_H)=\Big\{\psi:\int_{\Omega_H}\psi=0\Big\}
\]
(to remove the constant mode).

Define \(\lambda_1(a)>0\) as the **first nonzero eigenvalue** of this realization and set
\[
\boxed{\;\lambda_{\min}(a):=\lambda_1(a)=a^2m_{\rm eff}(a)^2.\;}
\]

---

## 3. Fixing the geometry constant \(C_\Omega\)

### Lemma 3.1 (First eigenvalue on the causal torus; scalar regime)

If \(\mathcal L_{\Phi_0}\approx -\mu_{\rm iso}(a)\Delta\) on \(\mathbb T^3_{L_H(a)}\), then
\[
\lambda_1(a)=\mu_{\rm iso}(a)\left(\frac{2\pi}{L_H(a)}\right)^2
=\mu_{\rm iso}(a)\,(2\pi)^2\left(\frac{aH(a)}{c}\right)^2.
\]

*Proof.* The first nonzero Laplacian eigenvalue on \(\mathbb T^3_L\) is \((2\pi/L)^2\); multiply by \(\mu_{\rm iso}\). \(\square\)

### Corollary 3.2 (Closed form for \(m_{\rm eff}(a)\))

Using \(\lambda_1=a^2m_{\rm eff}^2\),
\[
\boxed{\;m_{\rm eff}(a)^2=(2\pi)^2\,\mu_{\rm iso}(a)\,\frac{H(a)^2}{c^2}.\;}
\]
Equivalently, in the shorthand
\[
\boxed{\;m_{\rm eff}(a)^2=C_\Omega\,\mu_{\rm iso}(a)\,\frac{H(a)^2}{c^2},
\qquad C_\Omega=(2\pi)^2.\;}
\]

This is the promised “geometry constant fix”: no hidden \(\mathcal O(1)\) fudge factor remains once \(\Omega_H\) is chosen.

---

## 4. Closing \(\mu_{\rm iso}(a)\) without circularity

This is the only subtle point: \(\mu_{\rm iso}\) must be evaluated on something that does **not** depend on \(\alpha_{\rm eff}\) (or else the closure becomes circular).

### Assumption 4.1 (Background is fixed)

The stack assumes \(H(a)\) is fixed to flat \(\Lambda\)CDM and receives no backreaction from the stiffness sector at the homogeneous level.

### Definition 4.2 (Deterministic cosmological field-strength proxy)

Define the background IR acceleration proxy
\[
\boxed{\;g_{\rm IR}(a):=cH(a)\;}
\]
and its dimensionless activation argument
\[
\boxed{\;s_{\rm IR}(a):=\frac{g_{\rm IR}(a)}{a_0}=\frac{cH(a)}{a_0}.\;}
\]

Define the background-evaluated constitutive factor
\[
\boxed{\;\mu_{\rm IR}(a):=\mu(s_{\rm IR}(a))=1-e^{-s_{\rm IR}(a)}\;}
\]
and close the isotropic scalar stiffness coefficient by
\[
\boxed{\;\mu_{\rm iso}(a):=\mu_{\rm IR}(a)+\frac13\,s_{\rm IR}(a)\,e^{-s_{\rm IR}(a)}
=1-e^{-s_{\rm IR}(a)}+\frac13\,s_{\rm IR}(a)\,e^{-s_{\rm IR}(a)}.\;}
\]

### Proposition 4.3 (Non-circular evaluation order)

Under a fixed \(H(a)\), the following map is deterministic and acyclic:
\[
H(a)\ \longrightarrow\ s_{\rm IR}(a)\ \longrightarrow\ (\mu_{\rm IR}(a),\mu_{\rm iso}(a))
\ \longrightarrow\ m_{\rm eff}(a)\ \longrightarrow\ \alpha_{\rm eff}(k,a).
\]
No step depends on \(\alpha_{\rm eff}\) or on the modified potential.

---

## 5. Propagation into the modified Poisson kernel

The cosmology stack uses
\[
\frac{k^2}{a^2}\Phi=4\pi G_{\rm eff}(k,a)\bar\rho_m\delta,
\qquad
G_{\rm eff}=G[1+\alpha_{\rm eff}(k,a)].
\]
with enhancement
\[
\boxed{\;
\alpha_{\rm eff}(k,a)
=
\frac{k^2}{k^2+a^2m_{\rm eff}(a)^2}\cdot\frac{1}{\mu_{\rm IR}(a)}.
\;}
\]

Substituting the causal-patch closure gives the fully explicit kernel:
\[
\boxed{\;
\alpha_{\rm eff}(k,a)
=
\frac{k^2}{k^2+a^2(2\pi)^2\,\mu_{\rm iso}(a)\,\frac{H(a)^2}{c^2}}
\cdot\frac{1}{1-e^{-cH(a)/a_0}}.
\;}
\]

---

## 6. Limiting checks (recorded as formal propositions)

### Proposition 6.1 (Early-time decoupling)

Fix comoving \(k\neq 0\). If \(aH(a)\to\infty\) as \(a\to 0\) and \(\mu_{\rm iso}(a)\) does not vanish fast enough to cancel \((aH)^2\), then
\[
\frac{k^2}{k^2+a^2m_{\rm eff}(a)^2}\to 0
\quad\Rightarrow\quad
\alpha_{\rm eff}(k,a)\to 0.
\]
So GR is an early-time fixed point.

### Proposition 6.2 (Subhorizon recovery of the pure stiffness factor)

At fixed \(a\), for \(k^2\gg a^2m_{\rm eff}(a)^2\),
\[
\frac{k^2}{k^2+a^2m_{\rm eff}^2}=1+O\!\left(\frac{a^2m_{\rm eff}^2}{k^2}\right),
\]
hence
\[
\alpha_{\rm eff}(k,a)=\frac{1}{\mu_{\rm IR}(a)}+O\!\left(\frac{a^2m_{\rm eff}^2}{k^2}\right)\frac{1}{\mu_{\rm IR}(a)}.
\]

---

## 7. What is genuinely “new” here (as theory content)

The non-obvious step is the IR definition
\[
a^2m_{\rm eff}^2=\lambda_1(\mathcal L_{\Phi_0}^{(a)}\text{ on }\Omega_H(a)),
\]
which makes the Yukawa denominator a **spectral datum** of the linearized second-variation operator, rather than a new inserted scale.

Once that is accepted, the cosmology kernel becomes a resolvent of the same object that generates screening and stability in the nonrelativistic sector.

