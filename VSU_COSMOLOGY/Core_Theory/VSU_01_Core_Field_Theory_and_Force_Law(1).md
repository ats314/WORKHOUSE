# VSU 01 — Core Field Theory and Force Law (Action → Operator → Phenomenology)

**Scope.** This note distills the analytic spine of the Vacuum Stiffness Unification (VSU) framework:

- an action principle for a nonrelativistic potential \(\Phi(\mathbf x)\),
- a quasilinear modified Poisson equation with a **fixed constitutive law**,
- the exact spherical force law and its two asymptotic regimes,
- the logarithmic potential and the BTFR scaling.

**Primary sources:** `01.1_Action_and_Field_Equations.md`, `02.1_Force_Law_and_Asymptotics.md`, `02.2_BTFR_Derivation.md`.

---

## 1. Nonrelativistic action and Euler–Lagrange equation

Consider a nonrelativistic gravitational potential \(\Phi(\mathbf x)\) coupled to matter density \(\rho(\mathbf x)\) through

\[
S_{\rm NR}[\Phi]
=
\int dt\int d^3x\left[
\frac{a_0^2}{8\pi G}\,
F\!\left(Y\right)
+\rho\,\Phi
\right],
\qquad
Y:=\frac{|\nabla\Phi|^2}{a_0^2}.
\]

The constitutive function is fixed by

\[
\mu(x):=F'(x^2),
\qquad
\mu(x)=1-e^{-x},
\qquad x\ge 0.
\]

Vary \(\Phi\). Using
\[
\delta Y = \frac{2}{a_0^2}\,\nabla\Phi\cdot\nabla(\delta\Phi),
\]
integrating by parts, and discarding boundary terms yields the modified Poisson equation:

\[
\boxed{
\nabla\cdot\!\left(
\mu\!\left(\frac{|\nabla\Phi|}{a_0}\right)\nabla\Phi
\right)=4\pi G\,\rho.
}
\]

**Operator remark.** This is a quasilinear, uniformly elliptic equation in any region where \(\mu\) is bounded away from \(0\). In VSU, \(\mu(x)>0\) for all \(x>0\).

---

## 2. Gauss law and the exact spherical force law

Define the gravitational field
\[
\mathbf g:=-\nabla\Phi,\qquad g:=|\mathbf g|.
\]

Integrate the field equation over a volume \(V\) and apply the divergence theorem:

\[
\oint_{\partial V}\mu\!\left(\frac{g}{a_0}\right)\,\mathbf g\cdot d\mathbf S
=
4\pi G\,M(V).
\]

For spherical symmetry, \(\mathbf g = g(r)\,\hat{\mathbf r}\) and \(M(V)=M(r)\), so

\[
\boxed{
g(r)\,\mu\!\left(\frac{g(r)}{a_0}\right)=\frac{GM(r)}{r^2}
=:g_N(r).
}
\]

This is an **algebraic** relation at each radius.

---

## 3. Monotonicity ⇒ uniqueness (no “branches”)

With \(\mu(x)=1-e^{-x}\), define
\[
f(g):=g\left(1-e^{-g/a_0}\right).
\]
Then
\[
f'(g)=1-e^{-g/a_0}+\frac{g}{a_0}e^{-g/a_0}>0\qquad (g>0),
\]
so \(f\) is strictly increasing and therefore invertible on \(g\ge 0\).

\[
\boxed{
\text{For each }g_N\ge 0\text{ there is a unique physical solution }g=g(g_N)\ge 0.
}
\]

This “no-branching” property is unusually clean compared to many nonlinear modified-gravity closures.

---

## 4. Asymptotic regimes

### 4.1 Strong-field regime: \(g\gg a_0\) (screened)

Since \(e^{-g/a_0}\to 0\),
\[
\mu\!\left(\frac{g}{a_0}\right)\to 1,
\]
and the force law becomes
\[
\boxed{g(r)\simeq g_N(r)=\frac{GM(r)}{r^2},}
\]
with **exponentially small** deviations.

### 4.2 Weak-field regime: \(g\ll a_0\) (unscreened)

For small \(x\),
\[
\mu(x)=1-e^{-x}\simeq x,
\]
so
\[
g\,\frac{g}{a_0}\simeq g_N
\quad\Rightarrow\quad
\boxed{g(r)=\sqrt{a_0\,g_N(r)}.}
\]

For a point mass \(M\), \(g_N=GM/r^2\) gives
\[
\boxed{g(r)=\frac{\sqrt{GMa_0}}{r}.}
\]

---

## 5. Potential behavior

Since \(g(r)=-\partial_r\Phi\):

- **Newtonian regime**
  \[
  g=\frac{GM}{r^2}\quad\Rightarrow\quad \Phi(r)\simeq-\frac{GM}{r}.
  \]

- **Weak-field regime**
  \[
  g=\frac{\sqrt{GMa_0}}{r}\quad\Rightarrow\quad
  \boxed{\Phi(r)\simeq -\sqrt{GMa_0}\,\ln r.}
  \]

A logarithmic potential is the classic route to asymptotically flat rotation curves.

---

## 6. BTFR and asymptotically flat rotation curves

For a circular orbit, \(V^2/r=g(r)\). In the weak-field regime with total baryonic mass \(M_b\),

\[
\frac{V^2}{r}=\frac{\sqrt{GM_ba_0}}{r}
\quad\Rightarrow\quad
V^2=\sqrt{GM_ba_0}
\quad\Rightarrow\quad
\boxed{V^4=G\,M_b\,a_0.}
\]

This is the Baryonic Tully–Fisher Relation (BTFR) with fixed slope \(4\) and normalization set solely by \(a_0\).

---

## 7. Why the exponential \(\mu\) is structurally distinctive

Many MOND-like schemes choose interpolation functions approaching \(\mu\to 1\) as a power law. VSU’s choice

\[
\mu(x)=1-e^{-x}
\]

approaches unity exponentially fast, making the high-acceleration (Newtonian) regime unusually “stiff”: corrections disappear rapidly once \(g/a_0\gtrsim \text{few}\).

That’s a strong falsifiability feature: you don’t get to dial away high-field tests with extra knobs; the function is fixed.

---

## References (project files)

- `01.1_Action_and_Field_Equations.md`
- `02.1_Force_Law_and_Asymptotics.md`
- `02.2_BTFR_Derivation.md`
