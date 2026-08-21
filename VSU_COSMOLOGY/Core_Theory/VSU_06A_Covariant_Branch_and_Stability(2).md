# VSU 06A — Covariant Branch Completion and FLRW Stability (Making \(X<0\) Explicit)

**Scope.** The project’s covariant scalar sector defines
\[
X=\frac{g^{\mu\nu}\nabla_\mu\phi\nabla_\nu\phi}{a_0^2},
\qquad
F'(X)=1-e^{-\sqrt{X}},
\]
and then analyzes stress–energy and hyperbolicity assuming \(X>0\).  
But in an FLRW background with \(\phi=\phi_0(t)\), one has \(X_0<0\) (timelike gradient). This note makes that branch explicit **without changing the nonrelativistic (\(X>0\)) sector**, and then re-derives:

- hyperbolicity conditions and characteristic speed on FLRW,
- stress–energy positivity on the \(X<0\) branch.

**Primary sources:** `01.1_Action_and_Field_Equations.md`, `01.2_Stress_Energy_Tensor.md`, `01.3_Hyperbolicity_and_Characteristics.md`, `03.2_Scalar_Perturbations.md`, `03.1_Background_Cosmology.md`.

---

## 1. The issue: cosmology forces \(X_0<0\)

The covariant action in the project is

\[
S[g_{\mu\nu},\phi]
=
\int d^4x\sqrt{-g}
\left[
\frac{1}{16\pi G}R
+
\frac{a_0^2}{8\pi G}F(X)
+
\mathcal L_m
\right],
\qquad
X:=\frac{g^{\mu\nu}\nabla_\mu\phi\nabla_\nu\phi}{a_0^2}.
\]

On spatially flat FLRW,
\[
ds^2=-dt^2+a^2(t)d\mathbf x^2,
\]
a homogeneous background field \(\phi_0(t)\) gives

\[
X_0
=
\frac{g^{00}\dot\phi_0^2}{a_0^2}
=
-\frac{\dot\phi_0^2}{a_0^2}
<0.
\]

So the constitutive prescription written as \(F'(X)=1-e^{-\sqrt{X}}\) is ambiguous unless the \(X<0\) branch is defined.

---

## 2. Minimal branch-explicit completion: \(\sqrt{X}\mapsto \sqrt{|X|}\) in \(F'\)

Define \(s:=\sqrt{|X|}\ge 0\). For all real \(X\), set

\[
\boxed{
K(X):=F'(X)=1-e^{-s}=1-e^{-\sqrt{|X|}}.
}
\]

Then for \(X\neq 0\),

\[
\boxed{
K'(X)=F''(X)=\frac{e^{-s}}{2s}\,\mathrm{sgn}(X),
\qquad s=\sqrt{|X|}.
}
\]

This reproduces the project’s expressions on the \(X>0\) branch and keeps everything real on the timelike \(X<0\) branch.

A continuous primitive \(F(X)\) with \(F(0)=0\) can be chosen piecewise as:

\[
F(X)=
\begin{cases}
X+2(1+\sqrt X)e^{-\sqrt X}-2, & X\ge 0,\\[6pt]
X-2(1+\sqrt{-X})e^{-\sqrt{-X}}+2, & X\le 0.
\end{cases}
\]

(The additive constants correspond to a vacuum-energy choice and can be absorbed into \(\Lambda\), consistent with the project’s “background absorbed into \(\rho_\Lambda\)” stance.)

---

## 3. Hyperbolicity on the timelike FLRW branch

The principal symbol analysis in `01.3_Hyperbolicity_and_Characteristics.md` gives the effective inverse metric

\[
G_{\rm eff}^{\mu\nu}
=
K(X_0)g^{\mu\nu}
+
\frac{2K'(X_0)}{a_0^2}u^\mu u^\nu,
\qquad u_\mu:=\nabla_\mu\phi_0.
\]

A standard sufficient condition for hyperbolicity is

\[
\boxed{
K_0>0,
\qquad
K_0+2X_0K_0'>0,
}
\qquad
K_0:=K(X_0),\ K_0':=K'(X_0).
\]

Write \(X_0=\pm s^2\) with \(s=\sqrt{|X_0|}=|\dot\phi_0|/a_0>0\).  
With the branch choice above,

\[
K_0 = 1-e^{-s},
\qquad
K_0+2X_0K_0'
=
1-e^{-s}+s e^{-s}
=
\boxed{1-e^{-s}(1-s)}.
\]

Since \(1-e^{-s}(1-s)>0\) for all \(s>0\), we get:

\[
\boxed{
\text{The scalar equation is strictly hyperbolic on FLRW for all }X_0\neq 0.
}
\]

### 3.1 Characteristic speed on FLRW

In the local rest frame of the background (timelike gradient), the sound speed is

\[
\boxed{
c_s^2
=
\frac{K_0}{K_0+2X_0K_0'}
=
\frac{1-e^{-s}}{1-e^{-s}+s e^{-s}},
\qquad s=\sqrt{|X_0|}.
}
\]

Limits:

- \(s\ll 1\): \(c_s^2\to \tfrac12\),
- \(s\gg 1\): \(c_s^2\to 1\).

Thus \(1/2\le c_s^2<1\) on the timelike branch as well.

---

## 4. Stress–energy positivity on the timelike FLRW branch

The scalar stress–energy tensor derived in `01.2_Stress_Energy_Tensor.md` is

\[
T_{\mu\nu}^{(\phi)}
=
\frac{a_0^2}{4\pi G}
\left[
\frac{K(X)}{a_0^2}\nabla_\mu\phi\nabla_\nu\phi
-\frac12 g_{\mu\nu}F(X)
\right].
\]

For a homogeneous background \(\phi_0(t)\), the energy density is

\[
\rho_\phi=T_{00}^{(\phi)}
=
\frac{a_0^2}{4\pi G}\left[-X_0K_0+\frac12F(X_0)\right].
\]

On the \(X_0=-s^2\) branch, \(K_0=1-e^{-s}\) and (with the primitive above)
\[
F(X_0)=-s^2-2(s+1)e^{-s}+2.
\]

Substituting gives a compact expression

\[
\boxed{
\rho_\phi
=
\frac{a_0^2}{4\pi G}
\left[
1+\frac{s^2}{2}
-e^{-s}(s^2+s+1)
\right],
\qquad
s=\frac{|\dot\phi_0|}{a_0}.
}
\]

Define \(f(s)=1+\tfrac12s^2-e^{-s}(s^2+s+1)\). Then

\[
f(0)=0,
\qquad
f'(s)=s\bigl[1-e^{-s}(1-s)\bigr]>0\quad (s>0),
\]

so \(f(s)>0\) for all \(s>0\). Therefore

\[
\boxed{
\rho_\phi\ge 0\ \text{on the entire timelike branch, with equality only at }X_0=0.
}
\]

This is the “background positivity” statement one wants before trusting perturbation theory.

---

## 5. Linear perturbations: coefficients are now unambiguous

The linearized scalar equation in `03.2_Scalar_Perturbations.md` involves the combination

\[
A_0:=K_0+2X_0K_0'
\]
as the time-kinetic coefficient and \(K_0\) as the gradient coefficient:

\[
A_0\,\ddot{\delta\phi}+3HK_0\,\dot{\delta\phi}+\frac{K_0}{a^2}k^2\delta\phi=S_\Phi.
\]

With the explicit \(X<0\) branch:

- \(K_0=1-e^{-s}\in(0,1)\),
- \(K_0'<0\) but \(A_0=1-e^{-s}+se^{-s}>0\).

So (i) the kinetic term is positive, (ii) the gradient term is positive, and (iii) the sound speed is \(c_s^2=K_0/A_0\in[1/2,1)\).

---

## 6. A conceptual checkpoint (not “just a sign”)

This branch completion fixes a **mathematical** mismatch (cosmology wants \(X_0<0\)).  
But it does *not* by itself resolve a deeper modeling question already present in the project’s covariant extension:

- The covariant scalar equation \(\nabla_\mu(K\nabla^\mu\phi)=0\) is source-free.
- The nonrelativistic sector has an explicit matter source \(4\pi G\rho\) in the \(\Phi\) equation.

Reconciling these cleanly typically requires specifying how matter couples to the scalar (directly or via an effective “physical metric”). That step determines whether the nonrelativistic modified Poisson equation is truly the weak-field limit of the covariant theory, or a separate effective closure.

---

## References (project files)

- `01.1_Action_and_Field_Equations.md`
- `01.2_Stress_Energy_Tensor.md`
- `01.3_Hyperbolicity_and_Characteristics.md`
- `03.1_Background_Cosmology.md`
- `03.2_Scalar_Perturbations.md`
