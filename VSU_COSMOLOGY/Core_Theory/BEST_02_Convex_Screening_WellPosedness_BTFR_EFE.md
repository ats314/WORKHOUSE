# Convex Vacuum Hamiltonian ⇒ Screening, EFE, BTFR, and Global PDE Closure

## Source modules distilled

This document is a curated extraction (with light reorganization) of the most structurally powerful continuum arguments scattered across:

- `global_well_posedness_of_the_vacuum_stiffness_poisson_equation.md`
- `energetic_origin_of_screening_via_convex_vacuum_hamiltonian.md`
- `02.1_Force_Law_and_Asymptotics.md`
- `02.2_BTFR_Derivation.md`
- `02.3_Screening_Radius_and_EFE.md`

The common mechanism is **strict convexity** of the vacuum Hamiltonian in the field gradient.

---

## 1. The continuum field equation as a convex variational problem

### 1.1 Energy functional

Let \(a_0>0\) and define
\[
\mu(x)=1-e^{-x},\qquad x\ge 0.
\]
Let \(F\) satisfy \(F'(Y)=\mu(\sqrt{Y})\). Consider
\[
\mathcal E[\Phi]
=
\int_{\mathbb R^3}\left[
\frac{a_0^2}{8\pi G}\,F\!\left(\frac{|\nabla\Phi|^2}{a_0^2}\right)
+\rho\,\Phi\right]\,dx,
\]
with \(\rho\in L^1\cap L^\infty\), \(\rho\ge 0\), \(M=\int\rho<\infty\), and decay \(\Phi(x)\to 0\) as \(|x|\to\infty\).

### 1.2 Euler–Lagrange equation

A minimizer satisfies
\[
\nabla\cdot\!\left(\mu\!\left(\frac{|\nabla\Phi|}{a_0}\right)\nabla\Phi\right)=4\pi G\rho.
\]

---

## 2. The strict convexity mechanism (the engine behind everything)

Let \(p=\nabla\Phi\) and define the Hamiltonian density
\[
\mathcal H(p)=\frac{a_0^2}{8\pi G}\,F\!\left(\frac{|p|^2}{a_0^2}\right).
\]
Then
\[
\nabla_p\mathcal H(p)=\frac{1}{4\pi G}\,\mu(|p|/a_0)\,p,
\]
\[
D_p^2\mathcal H(p)=\frac{1}{4\pi G}\left[\mu(|p|/a_0)I+\frac{\mu'(|p|/a_0)}{a_0|p|}\,p\otimes p\right],
\qquad \mu'(x)=e^{-x}>0.
\]

**Key point:** \(D_p^2\mathcal H(p)\succ 0\) for \(p\neq 0\). So \(p\mapsto\mathcal H(p)\) is strictly convex.

Everything below is a corollary of that convexity plus the asymptotic saturation \(\mu(x)\to 1\) as \(x\to\infty\).

---

## 3. Global well-posedness (existence + uniqueness)

### Theorem 3.1 (Existence by the direct method)

Under the source assumptions above, \(\mathcal E\) admits a minimizer \(\Phi\in H^1(\mathbb R^3)\). Any minimizer is a weak solution of the field equation.

*Proof sketch.* Coercivity follows from the growth \(F(Y)\sim Y\) at \(Y\gg 1\) and \(F(Y)\sim Y^{1/2}\) at \(Y\ll 1\), combined with Sobolev embedding and Young’s inequality controlling \(\int\rho\Phi\). Lower semicontinuity gives existence of a minimizer. Standard Euler–Lagrange calculus gives the weak PDE.

### Theorem 3.2 (Uniqueness by strict monotonicity)

Define
\[
\mathcal A(\Phi):=-\nabla\cdot\left(\mu(|\nabla\Phi|/a_0)\nabla\Phi\right).
\]
Strict convexity implies strict monotonicity:
\[
\int(\mathcal A(\Phi_1)-\mathcal A(\Phi_2))(\Phi_1-\Phi_2)\,dx>0
\]
unless \(\nabla\Phi_1=\nabla\Phi_2\) a.e., hence solutions differ only by a constant. The decay condition fixes the constant, hence the solution is unique.

---

## 4. Spherical Gauss-law reduction: the exact force law

Assume spherical symmetry with enclosed mass \(M(r)\). Gauss’ law gives
\[
\mu\!\left(\frac{g(r)}{a_0}\right)\,g(r)=\frac{GM(r)}{r^2}=:g_N(r),
\qquad g(r):=|\nabla\Phi(r)|.
\]
Since
\[
\frac{d}{dg}\left[g(1-e^{-g/a_0})\right]
=
1-e^{-g/a_0}+\frac{g}{a_0}e^{-g/a_0}>0,
\]
the physical field \(g(r)\) is uniquely determined by \(g_N(r)\).

---

## 5. The two asymptotic regimes (Newtonian recovery + MOND-like tail)

### Proposition 5.1 (Strong-field Newtonian tangent theory)

If \(g\gg a_0\), then \(e^{-g/a_0}\to 0\) and
\[
g(r)=g_N(r)\,\bigl[1+O(e^{-g/a_0})\bigr].
\]
Equivalently, on regions with \(|\nabla\Phi|\ge \Lambda a_0\) and \(\Lambda\gg 1\),
\[
\nabla^2\Phi = 4\pi G\rho + O(e^{-\Lambda}).
\]

### Proposition 5.2 (Weak-field square-root regime)

If \(g\ll a_0\), then \(\mu(g/a_0)\sim g/a_0\) and
\[
\frac{g(r)^2}{a_0}=g_N(r)
\quad\Rightarrow\quad
g(r)=\sqrt{a_0\,g_N(r)}.
\]
For a point mass \(M\), \(g(r)=\sqrt{GMa_0}/r\), hence
\[
\Phi(r)\sim -\sqrt{GMa_0}\,\ln r.
\]

---

## 6. BTFR as a theorem (no fitting, no halo modeling)

For a circular orbit, \(g_{\rm obs}=V^2/r=g(r)\). In the weak-field asymptotic region \(M(r)\to M_b\),
\[
\frac{V^2}{r}=\frac{\sqrt{G M_b a_0}}{r}
\quad\Rightarrow\quad
\boxed{V^4=GM_b a_0.}
\]

---

## 7. Screening radius as the matching scale

Define \(r_s(M)\) by \(g_N(r_s)=a_0\). For a point mass,
\[
\boxed{r_s(M)=\sqrt{\frac{GM}{a_0}}.}
\]
Then:
- \(r\ll r_s\): strong-field Newtonian tangent regime,
- \(r\gg r_s\): weak-field square-root regime.

This is the natural “regime boundary” used later in structure formation to decouple linear from nonlinear dynamics.

---

## 8. External Field Effect (EFE) as Hessian domination

Decompose the field gradient into an external and internal component,
\[
\nabla\Phi=p_{\rm ext}+p_{\rm int},
\qquad |p_{\rm ext}|\gg a_0.
\]
Expand the convex Hamiltonian:
\[
\mathcal H(p_{\rm ext}+p_{\rm int})
=
\mathcal H(p_{\rm ext})
+\langle \nabla_p\mathcal H(p_{\rm ext}),p_{\rm int}\rangle
+\tfrac12\langle p_{\rm int},D_p^2\mathcal H(p_{\rm ext})\,p_{\rm int}\rangle+\cdots.
\]
As \(|p_{\rm ext}|/a_0\to\infty\), \(\mu\to 1\) and \(\mu'\to 0\), so
\[
D_p^2\mathcal H(p_{\rm ext})\to \frac{1}{4\pi G}I.
\]
Therefore internal fluctuations see an **effectively Newtonian quadratic energy**, i.e. internal dynamics become Newtonian even if the internal field is weak. This is precisely the EFE and it is not an extra mechanism: it is the quadratic tangent structure of a convex Hamiltonian.

---

## 9. Theory-building payload

The non-obvious structural claim is:

> Screening, EFE, uniqueness/stability, and the MOND-like tail are **the same theorem** viewed in different projections: all are consequences of strict convexity + saturation of \(\mu\).

That claim is reusable: once the vacuum Hamiltonian is fixed, these effects are not optional knobs; they are rigid.

