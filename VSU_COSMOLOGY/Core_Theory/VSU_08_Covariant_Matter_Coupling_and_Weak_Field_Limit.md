# VSU_08 — Covariant Matter Coupling that Reproduces the Sourced Modified Poisson Equation

## Abstract

The project’s nonrelativistic sector is defined by an **AQUAL-like** action for a potential \(\Phi\) with an explicit matter coupling \(\rho\,\Phi\), yielding the sourced quasilinear elliptic equation
\[
\nabla\!\cdot\!\bigl(\mu(|\nabla\Phi|/a_0)\,\nabla\Phi\bigr)=4\pi G\,\rho,
\qquad
\mu(x)=1-e^{-x}.
\]
In contrast, the covariant scalar extension written in `01.1_Action_and_Field_Equations.md` gives an *unsourced* scalar equation
\[
\nabla_\mu\!\left(F'(X)\nabla^\mu\phi\right)=0,
\]
unless matter is coupled to \(\phi\) explicitly.

This note **writes the covariant matter coupling explicitly** (no handwaving) such that the *weak-field, quasistatic* limit of the covariant theory yields **exactly** the nonrelativistic sourced modified Poisson equation used throughout the VSU force-law, screening, and collapse files.

---

## 1. The mismatch we are fixing

### 1.1 Nonrelativistic sector (already in the project)

The nonrelativistic action is (project file `01.1_Action_and_Field_Equations.md`)
\[
S_{\rm NR}[\Phi]
=
\int dt\,d^3x\left[
\frac{a_0^2}{8\pi G}\,
F\!\left(\frac{|\nabla\Phi|^2}{a_0^2}\right)
+\rho\,\Phi
\right],
\qquad
\mu(x)=F'(x^2)=1-e^{-x}.
\]
Varying \(\Phi\) gives the sourced modified Poisson equation
\[
\nabla\!\cdot\!\bigl(\mu(|\nabla\Phi|/a_0)\,\nabla\Phi\bigr)=4\pi G\,\rho.
\]
This operator is the backbone of the spherical force law (`02.1_Force_Law_and_Asymptotics.md`) and of screening/EFE (`05.1_Nonlinear_Screening_Mechanism.md`, `02.3_Screening_Radius_and_EFE.md`).  

### 1.2 Covariant sector as currently written (project)

The minimal covariant action is written as
\[
S[g_{\mu\nu},\phi,\psi]
=
\int d^4x\sqrt{-g}\left[
\frac{1}{16\pi G}R
+\frac{a_0^2}{8\pi G}F(X)
\right]
+S_m[g_{\mu\nu},\psi],
\qquad
X:=\frac{g^{\mu\nu}\nabla_\mu\phi\nabla_\nu\phi}{a_0^2}.
\]
Varying \(\phi\) gives
\[
\nabla_\mu\!\left(F'(X)\nabla^\mu\phi\right)=0,
\]
i.e. **no matter source**.

So the “this reduces to the nonrelativistic equation” sentence in `01.1` is only true if we make the matter coupling explicit.

---

## 2. Minimal covariant matter coupling that sources \(\phi\)

The cleanest diffeomorphism-invariant way to make matter source \(\phi\) is to let matter couple to a **Jordan-frame metric** \(\tilde g_{\mu\nu}\) that depends on \(\phi\). The simplest choice with no extra fields is a conformal coupling:
\[
\boxed{
\tilde g_{\mu\nu}
=
e^{-2\phi}\,g_{\mu\nu}.
}
\]
Then matter action is
\[
\boxed{
S_m \;=\; S_m[\tilde g_{\mu\nu},\psi]
\;=\;
\int d^4x\,\sqrt{-\tilde g}\,\mathcal L_m(\tilde g_{\mu\nu},\psi).
}
\]

### 2.1 Full covariant action (the “welded” version)

Including a cosmological constant \(\Lambda\) if desired:
\[
\boxed{
S[g,\phi,\psi]
=
\int d^4x\sqrt{-g}\left[
\frac{1}{16\pi G}(R-2\Lambda)
+\frac{a_0^2}{8\pi G}F(X)
\right]
+S_m[e^{-2\phi}g,\psi].
}
\]
This introduces **no new free functions** beyond \(F\) (already fixed by \(\mu(x)=1-e^{-x}\)) and no new mass scales beyond \(a_0\).

---

## 3. Field equations with this coupling

Define
\[
K(X):=F'(X).
\]
(If you adopt the branch-explicit completion \(K(X)=1-e^{-\sqrt{|X|}}\), this is real for both \(X>0\) and \(X<0\).)

### 3.1 Scalar equation: now sourced by matter

Varying the scalar sector gives the usual k-essence principal part:
\[
\delta S_\phi
=
-\frac{1}{4\pi G}\int d^4x\sqrt{-g}\,
\nabla_\mu\!\left(K(X)\nabla^\mu\phi\right)\delta\phi.
\]

The matter action varies because \(\tilde g_{\mu\nu}\) depends on \(\phi\). Using
\[
\delta S_m
=
\frac12\int d^4x\sqrt{-\tilde g}\,\tilde T^{\mu\nu}\,\delta\tilde g_{\mu\nu},
\qquad
\tilde T:=\tilde g_{\mu\nu}\tilde T^{\mu\nu},
\]
and
\[
\delta\tilde g_{\mu\nu}
=
\delta(e^{-2\phi}g_{\mu\nu})
=
-2\,e^{-2\phi}g_{\mu\nu}\,\delta\phi
=
-2\,\tilde g_{\mu\nu}\,\delta\phi,
\]
we obtain
\[
\delta S_m
=
-\int d^4x\sqrt{-\tilde g}\,\tilde T\,\delta\phi.
\]
Since \(\sqrt{-\tilde g}=e^{-4\phi}\sqrt{-g}\), stationarity \(\delta S=0\) for all \(\delta\phi\) yields:
\[
\boxed{
\nabla_\mu\!\left(K(X)\nabla^\mu\phi\right)
=
-4\pi G\,e^{-4\phi}\,\tilde T.
}
\]

For pressureless matter, \(\tilde T\simeq -\rho\), so the RHS becomes \(+4\pi G\,\rho\) (up to the tiny factor \(e^{-4\phi}\approx 1\) in weak fields).

---

## 4. Weak-field, quasistatic limit \(\Rightarrow\) *exact* VSU modified Poisson equation

Assume:

- weak gravity, slowly varying fields,
- nonrelativistic matter (\(p\ll\rho\)),
- quasistatic field: \(|\partial_t\phi|\ll|\nabla\phi|\),
- background metric approximately Minkowski (or FLRW with sub-horizon, local patch).

Then
\[
X
=
\frac{g^{\mu\nu}\nabla_\mu\phi\nabla_\nu\phi}{a_0^2}
\simeq
\frac{\delta^{ij}\partial_i\phi\,\partial_j\phi}{a_0^2}
=
\frac{|\nabla\phi|^2}{a_0^2}
=:Y.
\]
Hence
\[
K(X)\;\to\;F'(Y)\;=\;\mu(\sqrt{Y})\;=\;\mu(|\nabla\phi|/a_0).
\]

Also \(e^{-4\phi}\to 1\) and \(-\tilde T\to \rho\). The scalar equation becomes
\[
\boxed{
\nabla\!\cdot\!\left(\mu(|\nabla\phi|/a_0)\,\nabla\phi\right)
=
4\pi G\,\rho,
\qquad
\mu(x)=1-e^{-x}.
}
\]
Identifying \(\phi\) with the Newtonian potential \(\Phi\) in the nonrelativistic sector,
\[
\phi\equiv\Phi,
\]
we recover **exactly** the project’s defining modified Poisson equation (the one used in the force-law and screening files).

This is the explicit “weld” between the covariant and nonrelativistic sectors.

---

## 5. Check: the matter action reduces to \(\int\rho\,\Phi\) in the Newtonian limit

Take matter as point particles moving on geodesics of \(\tilde g_{\mu\nu}\):
\[
S_{\rm pp}=-\sum_a m_a\int ds_{\tilde g}.
\]
In a weak-field, slow-motion limit with \(\tilde g_{00}\simeq-(1+2\Phi)\) and \(\tilde g_{ij}\simeq(1-2\Phi)\delta_{ij}\), the line element gives
\[
ds_{\tilde g}\simeq (1+\Phi-\tfrac12 v^2)\,dt,
\]
so
\[
S_{\rm pp}\simeq\int dt\left(\sum_a \frac12 m_a v_a^2 -\sum_a m_a \Phi\right)+\text{const}.
\]
Passing to a continuum description, \(\sum_a m_a\Phi\to\int d^3x\,\rho\,\Phi\), reproducing the \(\rho\Phi\) term in \(S_{\rm NR}\).

---

## 6. What this choice implies (and what still needs to be checked)

### 6.1 Background cosmology is no longer “free” by assumption

With the coupling above, homogeneous matter has \(\tilde T\neq 0\), so \(\phi_0(t)\) is sourced on FLRW:
\[
\frac{1}{a^3}\frac{d}{dt}\Bigl(a^3 K(X_0)\dot\phi_0\Bigr)
=
-4\pi G\,e^{-4\phi_0}\tilde T_0.
\]
So the project’s “background absorbed into \(\Lambda\)” assumption (`03.1_Background_Cosmology.md`) must be re-checked with this explicit coupling:
either the sourced \(\phi_0\) is dynamically driven to a regime where its energy density is effectively constant / negligible,
or the background evolution is not exactly \(\Lambda\)CDM.

This is not a bug; it is the price of making the covariant theory honest.

### 6.2 Conformal coupling and lensing

A purely conformal relation \(\tilde g_{\mu\nu}=e^{-2\phi}g_{\mu\nu}\) leaves **null geodesic paths** invariant (conformal transformations preserve light cones). If you want \(\phi\) to contribute to lensing in the same way it contributes to nonrelativistic dynamics, you may need a **disformal** component (Bekenstein-type) rather than a strictly conformal one.

VSU’s current lensing/ISW files treat \(\Phi\) as the metric potential that also lenses; so the precise “physical metric” choice will matter if this is pushed into a full relativistic phenomenology.

### 6.3 The minimal next-step calculation

With the coupling fixed, you can now redo the linear perturbation system in `03.2_Scalar_Perturbations.md` with a *sourced* scalar equation (source \(\propto\delta\tilde T\)). This is exactly the missing link behind whether the growth-sector \(\alpha_{\rm eff}(k,a)\) is derivable rather than inserted by ansatz (`03.3_Matter_Growth_Equation.md`).

---

## 7. Summary: what we achieved

- We specified an explicit, diffeomorphism-invariant matter coupling:
  \[
  S_m=S_m[e^{-2\phi}g,\psi].
  \]
- This produces a sourced scalar equation:
  \[
  \nabla_\mu(K\nabla^\mu\phi)=-4\pi G e^{-4\phi}\tilde T.
  \]
- In the weak-field, quasistatic limit it reduces exactly to the VSU modified Poisson equation:
  \[
  \nabla\cdot(\mu(|\nabla\Phi|/a_0)\nabla\Phi)=4\pi G\rho,
  \quad
  \mu(x)=1-e^{-x}.
  \]

This is the explicit “weld” between the covariant and nonrelativistic sectors that the project was implicitly relying on but had not written down.

---

## Dependencies (project files)

- `01.1_Action_and_Field_Equations.md` (NR action and intended covariant extension)
- `02.1_Force_Law_and_Asymptotics.md` (spherical reduction depends on the sourced NR equation)
- `05.1_Nonlinear_Screening_Mechanism.md`, `02.3_Screening_Radius_and_EFE.md` (screening/EFE from the same operator)
- `03.1_Background_Cosmology.md`, `03.2_Scalar_Perturbations.md` (cosmology must be revisited once the coupling is explicit)
