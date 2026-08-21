# VSU Stress–Energy, Conservation, and Hyperbolicity (with a Key Caveat)

## Abstract

This note extracts the covariant pieces of the VSU framework that are most consequential for **well-posedness** and **stability**:

- the scalar stress–energy tensor derived by metric variation,
- on-shell conservation and positivity conditions,
- the principal symbol of the scalar PDE and its effective characteristic metric,
- characteristic speeds \(c_s\) and hyperbolicity conditions.

It also flags a **nontrivial sign/branch issue** in the definition of the invariant \(X\) when one moves between quasistatic (spacelike-gradient) systems and FLRW (timelike-gradient) cosmology.

---

## 1. Covariant scalar sector

Start from a covariant action with Einstein–Hilbert gravity and a scalar \(\phi\):
\[
S[g_{\mu\nu},\phi]
=
\int d^4x\sqrt{-g}\left[
\frac{1}{16\pi G}R
+
\frac{a_0^2}{8\pi G}F(X)
+
\mathcal L_m
\right],
\qquad
X:=\frac{g^{\mu\nu}\nabla_\mu\phi\nabla_\nu\phi}{a_0^2}.
\]

The scalar equation of motion is
\[
\boxed{
\nabla_\mu\!\left(F'(X)\nabla^\mu\phi\right)=0.
}
\]

The constitutive choice is encoded by
\[
K(X):=F'(X),\qquad
K(X)=1-e^{-\sqrt{X}}\quad (X>0 \text{ branch}).
\]

---

## 2. Stress–energy tensor and its properties

Define the scalar stress–energy tensor by metric variation:
\[
T^{(\phi)}_{\mu\nu}:=
-\frac{2}{\sqrt{-g}}\frac{\delta S_\phi}{\delta g^{\mu\nu}}.
\]

Using
\[
\delta\sqrt{-g}=-\tfrac12\sqrt{-g}\,g_{\mu\nu}\,\delta g^{\mu\nu},
\qquad
\delta X=\frac{1}{a_0^2}\nabla_\mu\phi\,\nabla_\nu\phi\,\delta g^{\mu\nu},
\]
one finds the exact expression
\[
\boxed{
T^{(\phi)}_{\mu\nu}
=
\frac{a_0^2}{4\pi G}\left[
\frac{F'(X)}{a_0^2}\nabla_\mu\phi\,\nabla_\nu\phi
-\tfrac12 g_{\mu\nu}F(X)
\right].
}
\]

### 2.1 On-shell conservation

Using the scalar EOM and \(\nabla_\mu g_{\alpha\beta}=0\),
\[
\boxed{\nabla^\mu T^{(\phi)}_{\mu\nu}=0.}
\]

### 2.2 Positivity in quasistatic configurations

For a timelike unit vector \(u^\mu\),
\[
\rho_\phi:=T^{(\phi)}_{\mu\nu}u^\mu u^\nu
=
\frac{a_0^2}{4\pi G}\left[
\frac{F'(X)}{a_0^2}(u^\mu\nabla_\mu\phi)^2+\tfrac12 F(X)
\right].
\]

In quasistatic settings with \(u^\mu\nabla_\mu\phi=0\),
\[
\rho_\phi=\frac{a_0^2}{8\pi G}F(X).
\]
If \(F(X)\ge 0\) up to an additive constant and \(F'(X)>0\), then \(\rho_\phi\ge 0\) (no ghosts in this sector).

---

## 3. Hyperbolicity and the effective characteristic metric

Linearize about a background \(\phi_0\) by \(\phi=\phi_0+\varepsilon\varphi\), and define
\[
u_\mu:=\nabla_\mu\phi_0,\qquad X_0:=\frac{g^{\mu\nu}u_\mu u_\nu}{a_0^2}.
\]

The principal (second-derivative) part of the linearized operator is
\[
\mathcal P(\varphi)=
\left[
K(X_0)g^{\mu\nu}+\frac{2K'(X_0)}{a_0^2}u^\mu u^\nu
\right]\nabla_\mu\nabla_\nu\varphi+\cdots
\]

Define the **effective inverse metric**
\[
\boxed{
G^{\mu\nu}_{\rm eff}:=
K(X_0)g^{\mu\nu}+\frac{2K'(X_0)}{a_0^2}u^\mu u^\nu.
}
\]

Characteristics satisfy \(G^{\mu\nu}_{\rm eff}\xi_\mu\xi_\nu=0\).

### 3.1 Hyperbolicity conditions

A sufficient (standard) condition for hyperbolicity is that \(G^{\mu\nu}_{\rm eff}\) has Lorentzian signature, which holds if
\[
\boxed{
K(X_0)>0,\qquad K(X_0)+2X_0K'(X_0)>0.
}
\]

For \(K(X)=1-e^{-\sqrt{X}}\) on the \(X>0\) branch, both conditions hold.

---

## 4. Characteristic speed

In a local inertial frame where the background gradient is purely “time-directed,”
\[
u^\mu=(\dot\phi_0,0,0,0),
\]
one finds
\[
G^{00}_{\rm eff}=-(K+2X_0K'),\qquad G^{ij}_{\rm eff}=K\,\delta^{ij}.
\]

The squared characteristic speed is
\[
\boxed{
c_s^2=\frac{K(X_0)}{K(X_0)+2X_0K'(X_0)}.
}
\]

For the \(X>0\) constitutive branch:
- if \(X_0\ll 1\): \(K\simeq\sqrt{X}\), \(K'\simeq (2\sqrt{X})^{-1}\), so \(c_s^2\to \tfrac12\);
- if \(X_0\gg 1\): \(K\to 1\), \(K'\to 0\), so \(c_s^2\to 1\).

Hence \(1/2\le c_s^2<1\): causal, stable propagation *on that branch*.

---

## 5. The key caveat: the sign/branch of \(X\)

With the metric convention used in many cosmology notes,
\[
ds^2=-dt^2+a^2(t)d\mathbf x^2,
\]
a homogeneous background \(\phi_0(t)\) has a timelike gradient, so
\[
X_0=\frac{g^{00}\dot\phi_0^2}{a_0^2}=-\frac{\dot\phi_0^2}{a_0^2}<0.
\]

But the constitutive prescription \(K(X)=1-e^{-\sqrt{X}}\) was written for \(X>0\).

So, as currently stated, the covariant sector implicitly assumes **either**
- a different invariant definition, **or**
- a two-branch analytic continuation of \(K(X)\), **or**
- a restriction to backgrounds where \(\nabla_\mu\phi\) is spacelike (hard in FLRW), **or**
- an additional structure (e.g., a preferred foliation vector) that changes what “\(X\)” means covariantly.

### 5.1 Plausible resolutions (research directions)

**(A) Two-branch definition.** Define \(K(X)\) differently for timelike vs spacelike gradients, e.g.
\[
K(X)=
\begin{cases}
1-e^{-\sqrt{X}}, & X\ge 0,\\[4pt]
1-e^{-\sqrt{-X}}, & X<0,
\end{cases}
\]
or more generally \(K(X)=1-e^{-\sqrt{|X|}}\) with carefully tracked signs in the EOM.  
This is common in MOND-like relativistic completions: the same functional form can be used on both branches, but the PDE type/stability must be re-checked.

**(B) Redefine the invariant.** Use a sign-flipped invariant
\[
X_{\rm alt}:=-\frac{g^{\mu\nu}\nabla_\mu\phi\nabla_\nu\phi}{a_0^2},
\]
so that homogeneous timelike gradients give \(X_{\rm alt}>0\).  
Then rebuild the nonrelativistic limit so that the quasistatic equation still produces \(\mu(|\nabla\Phi|/a_0)\). This may force \(F\) to have different behavior for spacelike gradients.

**(C) Add a (possibly nondynamical) unit timelike vector field.** Project gradients onto spatial hypersurfaces:
\[
X_{\perp}:=\frac{(g^{\mu\nu}+u^\mu u^\nu)\nabla_\mu\phi\nabla_\nu\phi}{a_0^2},
\]
with \(u^\mu\) the cosmological rest-frame vector.  
This keeps \(X_\perp\ge 0\) for quasistatic configurations, but introduces extra structure that must be justified.

**Bottom line:** the hyperbolicity and stress–energy results are compelling, but a clean, explicit resolution of the \(X\)-branch issue is essential for a fully consistent relativistic/cosmological completion.

