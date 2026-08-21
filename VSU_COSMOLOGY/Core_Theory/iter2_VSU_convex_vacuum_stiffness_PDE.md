# Vacuum Stiffness Unification (VSU), Nonrelativistic Core

\newcommand{\dd}{\mathrm{d}}
\newcommand{\RR}{\mathbb{R}}
\newcommand{\vect}[1]{\mathbf{#1}}
\newcommand{\grad}{\nabla}

## Abstract

We derive a nonlinear modification of the Newtonian gravitational potential from a **convex variational principle** with a single universal acceleration scale $a_0>0$ and constitutive law
\[
\mu(x)=1-e^{-x},\qquad x\ge 0.
\]
The Euler–Lagrange equation is a quasilinear elliptic PDE
\[
\grad\cdot\!\left(\mu(|\grad\Phi|/a_0)\,\grad\Phi\right)=4\pi G\rho.
\]
We show (i) why strict convexity gives uniqueness and stability of solutions, (ii) how Newtonian gravity emerges as the **quadratic tangent theory** at large field gradients (automatic screening), (iii) how an external field enforces Newtonian internal dynamics (EFE), and (iv) how the weak-field limit yields the baryonic Tully–Fisher relation (BTFR) with exact slope 4.

This document is self-contained.

---

## 1. Variational definition of the theory

### 1.1 Energy functional

Let $\rho:\RR^3\to\RR$ be a mass density with finite total mass
\[
M:=\int_{\RR^3} \rho(x)\,\dd x <\infty,
\]
and consider the gravitational potential $\Phi:\RR^3\to\RR$ with $\Phi(x)\to 0$ as $|x|\to\infty$.

Fix a universal acceleration scale $a_0>0$ and a function $F:[0,\infty)\to\RR$ such that
\[
F'(Y)=\mu(\sqrt{Y}),\qquad \mu(x)=1-e^{-x}.
\]
Define the energy functional
\[
\mathcal E[\Phi]
=
\int_{\RR^3}
\left[
\frac{a_0^2}{8\pi G}\,F\!\left(\frac{|\grad\Phi|^2}{a_0^2}\right)
+\rho\,\Phi
\right]\dd x.
\]

**Interpretation.** The first term is a vacuum “elastic energy” depending only on the field gradient; the second term is the usual coupling to matter.

### 1.2 Euler–Lagrange equation

Let $Y:=|\grad\Phi|^2/a_0^2$. Vary $\Phi\mapsto \Phi+\epsilon\psi$ with compactly supported $\psi$. Then
\[
\delta Y = \frac{2}{a_0^2}\,\grad\Phi\cdot\grad\psi,
\qquad
\delta F(Y)=F'(Y)\delta Y.
\]
Therefore,
\[
\delta\mathcal E
=
\int_{\RR^3}
\left[
\frac{a_0^2}{8\pi G}\,F'(Y)\frac{2}{a_0^2}\,\grad\Phi\cdot\grad\psi
+\rho\psi
\right]\dd x
=
\int_{\RR^3}
\left[
\frac{1}{4\pi G}\,F'(Y)\,\grad\Phi\cdot\grad\psi
+\rho\psi
\right]\dd x.
\]
Integrate by parts (boundary term vanishes since $\psi$ is compactly supported):
\[
\delta\mathcal E
=
-\int_{\RR^3}
\psi\,\left[
\grad\cdot\!\left(\frac{1}{4\pi G}F'(Y)\grad\Phi\right)-\rho
\right]\dd x.
\]
Stationarity for all $\psi$ yields
\[
\grad\cdot\!\left(F'(Y)\grad\Phi\right)=4\pi G\rho.
\]
Using $F'(Y)=\mu(\sqrt{Y})=\mu(|\grad\Phi|/a_0)$ gives the **modified Poisson equation**
\[
\boxed{
\grad\cdot\!\left(\mu(|\grad\Phi|/a_0)\,\grad\Phi\right)=4\pi G\rho.
}
\]

---

## 2. Structural properties from convexity

### 2.1 Flux form and monotonicity

Define the gravitational field $\vect g:=-\grad\Phi$ and its magnitude $g:=|\vect g|$.

The flux vector is
\[
\vect J(\vect g):=\mu(g/a_0)\,\vect g.
\]
The PDE becomes
\[
\grad\cdot\vect J(\vect g) = -4\pi G\rho
\quad\text{(since $\vect g=-\grad\Phi$)}.
\]

Because $\mu(x)=1-e^{-x}$ satisfies $\mu(x)\ge 0$, $\mu'(x)=e^{-x}>0$, the mapping $\vect g\mapsto \vect J(\vect g)$ is **strictly monotone**:
for $\vect g_1\neq \vect g_2$,
\[
(\vect J(\vect g_1)-\vect J(\vect g_2))\cdot(\vect g_1-\vect g_2) > 0.
\]
One way to see this is via the Hamiltonian Hessian below.

### 2.2 Hamiltonian density and strict convexity

Define $p:=\grad\Phi\in\RR^3$ and Hamiltonian density
\[
\mathcal H(p)=\frac{a_0^2}{8\pi G}F(|p|^2/a_0^2).
\]
Then
\[
\nabla_p\mathcal H(p)
=
\frac{a_0^2}{8\pi G}F'(Y)\,\nabla_p Y
=
\frac{a_0^2}{8\pi G}\mu(|p|/a_0)\,\frac{2}{a_0^2}p
=
\frac{1}{4\pi G}\mu(|p|/a_0)\,p.
\]
Differentiate again. Using $\mu'(|p|/a_0)=e^{-|p|/a_0}$ and $\nabla_p|p|=p/|p|$ (for $p\neq0$),
\[
D_p^2\mathcal H(p)
=
\frac{1}{4\pi G}\left[
\mu(|p|/a_0)\,I
+
\frac{\mu'(|p|/a_0)}{a_0|p|}\,p\otimes p
\right].
\]
Both coefficients are nonnegative and for $p\neq0$ the second term is strictly positive in the $p$-direction because $\mu'>0$. Hence $D_p^2\mathcal H(p)$ is positive definite for $p\neq0$; at $p=0$ it is positive semidefinite by continuity. Thus:

\[
\boxed{\mathcal H \text{ is strictly convex in } p.}
\]

### 2.3 Consequences: uniqueness and stability (sketch-level PDE facts)

Convexity implies strict monotonicity of the operator
\[
\Phi\mapsto -\grad\cdot(\mu(|\grad\Phi|/a_0)\,\grad\Phi).
\]
For appropriate function classes (e.g. $\Phi\in H^1(\RR^3)$ with $\Phi\to0$ at infinity), strict monotonicity gives:

- **Uniqueness:** if $\Phi_1,\Phi_2$ solve the PDE for the same $\rho$, then $\Phi_1=\Phi_2$.
- **Stability:** small changes in $\rho$ induce small changes in $\Phi$ in the weak topology.

These are standard consequences of monotone-operator methods; the key “physics novelty” here is that they are enforced by convexity of a single Hamiltonian density, not by ad hoc screening prescriptions.

---

## 3. Force law in spherical symmetry and regimes

Assume spherical symmetry for a moment. Let $M(r)$ be mass enclosed within radius $r$.
By Gauss’ law, integrating the PDE over a ball gives
\[
4\pi r^2\,\mu(g(r)/a_0)\,g(r) = 4\pi G M(r).
\]
Therefore the field satisfies the algebraic relation
\[
\boxed{
\mu(g/a_0)\,g = g_N:=\frac{GM(r)}{r^2}.
}
\]
With $\mu(x)=1-e^{-x}$ this is
\[
g\,(1-e^{-g/a_0})=g_N.
\]

### 3.1 Existence and uniqueness of $g(g_N)$

Define $f(g):=g(1-e^{-g/a_0})$. Then
\[
f'(g) = 1-e^{-g/a_0} + \frac{g}{a_0}e^{-g/a_0} > 0
\quad\text{for }g>0.
\]
So $f$ is strictly increasing from $0$ to $\infty$, hence invertible. Thus for each $g_N\ge0$ there is a unique $g\ge0$.

### 3.2 Strong-field (screened) asymptotics

If $g\gg a_0$, then $e^{-g/a_0}\approx0$, so $\mu\approx1$ and
\[
g(1-e^{-g/a_0})=g_N
\quad\Rightarrow\quad
g = g_N\,(1+O(e^{-g/a_0})).
\]
Thus in strong fields the theory reduces to Newtonian gravity up to exponentially small corrections:
\[
\boxed{g\simeq g_N \quad (g\gg a_0).}
\]

### 3.3 Weak-field (stiffness-dominated) asymptotics

If $g\ll a_0$, then $1-e^{-g/a_0}\simeq g/a_0$, so
\[
g\cdot\frac{g}{a_0} \simeq g_N
\quad\Rightarrow\quad
\boxed{g \simeq \sqrt{a_0 g_N}\quad (g\ll a_0).}
\]
For an isolated mass $M$ (so $M(r)\to M$), $g_N=GM/r^2$ and
\[
g(r) \simeq \frac{\sqrt{GMa_0}}{r}.
\]
Integrating $g=-\partial_r\Phi$ yields an asymptotically logarithmic potential:
\[
\Phi(r)\simeq -\sqrt{GMa_0}\,\ln r + \text{const}.
\]

### 3.4 Screening radius

Define the transition radius by $g_N(r_s)=a_0$:
\[
\boxed{r_s = \sqrt{\frac{GM}{a_0}}.}
\]
Then:
- $r\ll r_s$ implies $g_N\gg a_0$ and Newtonian behavior;
- $r\gg r_s$ implies $g_N\ll a_0$ and stiffness behavior.

---

## 4. External Field Effect (EFE) from the operator structure

Let the total field decompose as
\[
\grad\Phi = p_{\mathrm{ext}} + p_{\mathrm{int}},
\qquad |p_{\mathrm{ext}}|\gg a_0,
\]
where $p_{\mathrm{ext}}$ varies slowly across the system.

Expand the Hamiltonian density around $p_{\mathrm{ext}}$:
\[
\mathcal H(p_{\mathrm{ext}}+p_{\mathrm{int}})
=
\mathcal H(p_{\mathrm{ext}})
+
\langle \nabla_p\mathcal H(p_{\mathrm{ext}}),p_{\mathrm{int}}\rangle
+
\frac12\langle p_{\mathrm{int}}, D_p^2\mathcal H(p_{\mathrm{ext}})\,p_{\mathrm{int}}\rangle
+\cdots
\]
As $|p_{\mathrm{ext}}|/a_0\to\infty$, we have $\mu(|p_{\mathrm{ext}}|/a_0)\to 1$ and $\mu'(|p_{\mathrm{ext}}|/a_0)\to 0$, hence
\[
D_p^2\mathcal H(p_{\mathrm{ext}})\to \frac{1}{4\pi G}I.
\]
Therefore internal fluctuations see an effectively Newtonian quadratic energy, and the internal field equation linearizes to
\[
\boxed{
\Delta\Phi_{\mathrm{int}} = 4\pi G \rho_{\mathrm{int}} + O(e^{-|p_{\mathrm{ext}}|/a_0}).
}
\]
This is the EFE: a strong background field “screens” the stiffness sector for internal dynamics.

---

## 5. BTFR derivation (exact in the asymptotic weak-field regime)

Consider a test particle on a circular orbit of radius $r$ with speed $V(r)$. The centripetal acceleration is
\[
g_{\mathrm{obs}}(r)=\frac{V(r)^2}{r}.
\]
In the quasistatic nonrelativistic regime, $g_{\mathrm{obs}}=g$.

In the weak-field regime $g\ll a_0$ around an isolated mass $M$,
\[
g(r)=\frac{\sqrt{GMa_0}}{r}.
\]
Equate with centripetal acceleration:
\[
\frac{V^2}{r}=\frac{\sqrt{GMa_0}}{r}
\quad\Rightarrow\quad
V^2=\sqrt{GMa_0}.
\]
Square:
\[
\boxed{V^4 = GMa_0.}
\]
Interpreting $M$ as the total baryonic mass $M_b$ yields the **baryonic Tully–Fisher relation (BTFR)** with exact slope 4 and normalization fixed by $a_0$.

---

## 6. Why this core is “theory-generating”

The key nonstandard move is: **screening and Newtonian recovery are not imposed**; they are consequences of strict convexity plus saturation of $\mu\to1$ at large gradients. This makes the strong-field limit a theorem (quadratic tangent theory), and it strongly constrains what modifications can exist without breaking high-acceleration tests.

A development path is to couple this nonrelativistic convex structure consistently into a covariant theory and quantify how the scalar sector back-reacts (or is absorbed) into effective $\Lambda$ while retaining early-universe consistency.
