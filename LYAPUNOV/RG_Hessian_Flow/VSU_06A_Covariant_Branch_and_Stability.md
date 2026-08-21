# VSU 06A — Covariant Completion on Both Signs of \(X\), and Re-derivations of Stability Pieces

This note removes the sign ambiguity in the covariant completion of the VSU scalar sector
by **defining a real branch for \(X<0\)** (timelike backgrounds), and then re-derives:

- hyperbolicity / characteristic speeds on an FLRW background,
- the linear scalar perturbation operator coefficients,
- stress–energy positivity on the homogeneous cosmological background.

Throughout we keep the original definitions:

\[
S_\phi=\frac{a_0^2}{8\pi G}\int d^4x\sqrt{-g}\,F(X),\qquad
X:=\frac{g^{\mu\nu}\nabla_\mu\phi\nabla_\nu\phi}{a_0^2}.
\]

The nonrelativistic weak-field regime corresponds to **spacelike gradients** (\(X>0\)),
while a homogeneous FLRW background \(\phi=\phi_0(t)\) gives **timelike gradients**
(\(X_0<0\)).

---

## 1. A real, unambiguous constitutive law for all real \(X\)

### 1.1 Define \(K(X)=F'(X)\) with a real square-root for both signs
Let
\[
s:=\sqrt{|X|}\ge 0.
\]

Define the constitutive derivative (the “\(\mu\)” analogue in the covariant theory) as
\[
\boxed{
K(X):=F'(X)=1-e^{-s}=1-e^{-\sqrt{|X|}},
\qquad X\in\mathbb R.
}
\]

This reproduces the original choice for \(X>0\) (spacelike / quasistatic) and gives
a **real** branch for \(X<0\) (timelike / homogeneous).

For \(X\neq 0\),
\[
\boxed{
K'(X)=F''(X)=\frac{e^{-\sqrt{|X|}}}{2\sqrt{|X|}}\;\mathrm{sgn}(X).
}
\]
So \(K'(X)>0\) on \(X>0\) and \(K'(X)<0\) on \(X<0\). This sign flip is expected:
\(\sqrt{|X|}\) has derivative \(\propto \mathrm{sgn}(X)\).

At \(X=0\), \(K(0)=0\) and \(K'\) diverges like \(1/\sqrt{|X|}\), as required to reproduce
the deep-MOND \(F\sim |X|^{3/2}\) structure.

---

### 1.2 Choose an explicit primitive \(F(X)\) (continuous at \(X=0\))
Integrate \(K(X)\) separately on \(X>0\) and \(X<0\) and fix constants so that \(F(0)=0\):

- For \(X\ge 0\) (\(s=\sqrt X\)):
\[
\boxed{
F(X)=X+2(1+\sqrt X)e^{-\sqrt X}-2.
}
\]

- For \(X\le 0\) (\(s=\sqrt{-X}\)):
\[
\boxed{
F(X)=X-2(1+\sqrt{-X})e^{-\sqrt{-X}}+2.
}
\]

These satisfy \(F'(X)=1-e^{-\sqrt{|X|}}\) on their respective domains and match continuously at 0.
The two additive constants (\(\pm2\)) correspond to a vacuum-energy shift and can be absorbed
into \(\Lambda\), consistent with treating the background expansion as \(\Lambda\)CDM.

---

## 2. Hyperbolicity re-derived on a timelike FLRW background (\(X_0<0\))

### 2.1 Principal symbol and effective metric
Linearizing \(\nabla_\mu(K(X)\nabla^\mu\phi)=0\) about a background \(\phi_0\) with
\(u_\mu:=\nabla_\mu\phi_0\), one obtains the principal part

\[
\left[
K(X_0)g^{\mu\nu}
+\frac{2K'(X_0)}{a_0^2}u^\mu u^\nu
\right]\nabla_\mu\nabla_\nu\varphi
\quad+\quad(\text{lower order})=0,
\]

so the effective inverse characteristic metric is

\[
\boxed{
G_{\rm eff}^{\mu\nu}
=
K_0\,g^{\mu\nu}
+\frac{2K_0'}{a_0^2}u^\mu u^\nu,
\qquad
K_0:=K(X_0),\;\;K_0':=K'(X_0).
}
\]

---

### 2.2 Hyperbolicity conditions, valid for both signs
For a k-essence-type scalar, strict hyperbolicity requires

\[
\boxed{
K_0>0,
\qquad
K_0+2X_0K_0'>0.
}
\]

With the branch defined above, write \(X_0=\pm s^2\). Then for either sign one finds

\[
K_0+2X_0K_0'
=
1-e^{-s}+s\,e^{-s}
=
\boxed{
1-e^{-s}(1-s)
}
>0
\quad \forall s>0.
\]

So **the scalar is strictly hyperbolic for all backgrounds with \(X_0\neq 0\)**.

---

### 2.3 Characteristic speed (timelike background)
In a local inertial frame where \(u^\mu\) is purely timelike, the squared signal speed is

\[
\boxed{
c_s^2
=\frac{K_0}{K_0+2X_0K_0'}
=
\frac{1-e^{-s}}{1-e^{-s}+s e^{-s}},
\qquad s=\sqrt{|X_0|}.
}
\]

Limits:
- \(s\ll1:\; c_s^2\to 1/2\),
- \(s\gg1:\; c_s^2\to 1\).

Thus \(1/2\le c_s^2<1\) holds on the cosmological \(X_0<0\) branch as well.

---

## 3. Stress–energy positivity on the homogeneous cosmological background

The stress–energy tensor is
\[
T^{(\phi)}_{\mu\nu}
=
\frac{a_0^2}{4\pi G}
\left[
\frac{K(X)}{a_0^2}\nabla_\mu\phi\nabla_\nu\phi
-\frac12 g_{\mu\nu}F(X)
\right].
\]

For \(\phi=\phi_0(t)\) in FLRW, \(X_0=-\dot\phi_0^2/a_0^2=-s^2\) and the energy density is
\[
\rho_\phi = T^{(\phi)}{}_{00}
=
\frac{a_0^2}{4\pi G}\left[-X_0K_0+\frac12F(X_0)\right].
\]

Insert \(K_0=1-e^{-s}\) and \(F(X_0)=-s^2-2(s+1)e^{-s}+2\) to obtain
\[
\boxed{
\rho_\phi
=
\frac{a_0^2}{4\pi G}
\left[
1+\frac{s^2}{2}
-e^{-s}(s^2+s+1)
\right],
\qquad s=\sqrt{-X_0}=\frac{|\dot\phi_0|}{a_0}.
}
\]

Define \(f(s)=1+s^2/2-e^{-s}(s^2+s+1)\). Then
\[
f(0)=0,\qquad
f'(s)=s\bigl[1-e^{-s}(1-s)\bigr]>0\quad (s>0).
\]
So \(f(s)>0\) for all \(s>0\), hence
\[
\boxed{\rho_\phi\ge 0 \text{ on the entire timelike branch, with equality only at } X_0=0.}
\]

This is the cosmological-background positivity statement.

---

## 4. Linear perturbations: coefficients are real and positive on \(X_0<0\)

Define the “time-kinetic” combination
\[
\boxed{
A_0:=K_0+2X_0K_0' >0,
}
\]
which is precisely the hyperbolicity condition.

The scalar perturbation equation on FLRW takes the schematic form
\[
\boxed{
A_0\,\ddot{\delta\phi}
+3HK_0\,\dot{\delta\phi}
+\frac{K_0}{a^2}k^2\,\delta\phi
= \text{(metric/matter sources)}.
}
\]

Two key positivity facts:

- **No ghost / positive time-kinetic term:** \(A_0>0\).
- **No gradient instability:** \(K_0>0\).

Both are guaranteed by the branch choice above for any \(X_0\neq 0\).

The sound speed is \(c_s^2=K_0/A_0\in[1/2,1)\).

---

## 5. Practical takeaway

To make the covariant theory *mathematically unambiguous* and keep all previous stability
claims, it is enough to adopt:

\[
K(X)=1-e^{-\sqrt{|X|}},\qquad
K'(X)=\frac{e^{-\sqrt{|X|}}}{2\sqrt{|X|}}\,\mathrm{sgn}(X),
\]

with the continuous primitive \(F(X)\) given above.

This resolves the “\(\sqrt{X}\)” ambiguity for \(X<0\) and makes the cosmological
background (\(X_0<0\)) compatible with the hyperbolicity and stress–energy arguments.
