# Convex Vacuum Stiffness Gravity: Variational PDE, Screening, and the BTFR

\begin{center}
\textit{A curated synthesis of the project’s nonrelativistic core: the gravity law as a strictly convex variational principle.}
\end{center}

## Abstract

The nonrelativistic Vacuum Stiffness Unification (VSU) sector can be read as a single mathematical statement: the gravitational potential \(\Phi\) is the unique minimizer of a strictly convex energy functional whose Hamiltonian density saturates to a quadratic form at large field gradients.

From this alone one gets:

1. **Global well-posedness** (existence/uniqueness/stability) of the modified Poisson equation.
2. **Automatic Newtonian recovery** (“screening”) as the strong-field tangent theory.
3. **External Field Effect (EFE)** as a Hessian-domination phenomenon.
4. **Logarithmic far-field potential**, yielding asymptotically flat rotation curves and the **baryonic Tully–Fisher relation (BTFR)**.

The novelty (as a research direction) is not that quasilinear elliptic equations exist, but that *the same convexity principle* simultaneously generates screening, EFE, and the BTFR without auxiliary interpolation rules.

---

## 1. Constitutive choice and field equation

Start from the nonrelativistic action
\[
S_{\rm NR}[\Phi]=\int dt\,d^3x\,\Big[\frac{a_0^2}{8\pi G}F\!\left(\frac{|\nabla\Phi|^2}{a_0^2}\right)+\rho\,\Phi\Big],
\]
with constitutive relation
\[
\mu(x):=F'(x^2)=1-e^{-x},\qquad x\ge 0.
\]
The Euler–Lagrange equation is the quasilinear elliptic PDE
\[
\nabla\cdot\Big(\mu(|\nabla\Phi|/a_0)\,\nabla\Phi\Big)=4\pi G\rho.
\]

Two asymptotic regimes follow immediately from \(\mu\):

- **Strong field** \(|\nabla\Phi|\gg a_0\): \(\mu\to 1\) exponentially fast, so the equation reduces to \(\nabla^2\Phi\approx 4\pi G\rho\).
- **Weak field** \(|\nabla\Phi|\ll a_0\): \(\mu(x)\sim x\), so \(\nabla\cdot\big(|\nabla\Phi|\nabla\Phi\big)=4\pi G a_0\rho\) (a 3D \(p\)-Laplace–type structure with \(p=3\) after scaling).

---

## 2. Variational structure and strict convexity

Define the energy functional
\[
\mathcal E[\Phi]=\int_{\mathbb R^3}\mathcal H(\nabla\Phi)\,dx+\int_{\mathbb R^3}\rho\,\Phi\,dx,
\qquad
\mathcal H(p)=\frac{a_0^2}{8\pi G}F\!\left(\frac{|p|^2}{a_0^2}\right).
\]
Then
\[
\nabla_p\mathcal H(p)=\frac{1}{4\pi G}\mu(|p|/a_0)\,p,
\]
and the Hessian is
\[
D_p^2\mathcal H(p)=\frac{1}{4\pi G}\Big[\mu(|p|/a_0)\,I+\frac{\mu'(|p|/a_0)}{a_0|p|}\,p\otimes p\Big].
\]
Since \(\mu'(x)=e^{-x}>0\), \(D_p^2\mathcal H\) is positive definite for \(p\neq 0\), so \(\mathcal H\) is **strictly convex**.

Interpretation: the vacuum behaves like a nonlinear “dielectric” medium for \(\nabla\Phi\), but one with a convex energy landscape—so it does not permit multiple branches or hysteresis.

---

## 3. Global well-posedness (the PDE is not a vibes-based law)

A standard direct-method argument applies:

1. **Coercivity:** \(\mathcal E\) controls \(\|\nabla\Phi\|_{L^2}\) up to a source-dependent constant.
2. **Lower semicontinuity:** convex integral functionals are weakly lower semicontinuous.
3. **Existence:** a minimizing sequence in \(H^1(\mathbb R^3)\) has a weakly convergent subsequence, yielding a minimizer.
4. **Uniqueness:** strict convexity/strict monotonicity of the Euler–Lagrange operator implies any two solutions differ by at most a constant, fixed by \(\Phi\to 0\) at infinity.

This is the correct “physics-to-math” translation: the *absence of extra screening parameters* is equivalent to uniqueness of minimizers.

---

## 4. Screening as the quadratic tangent theory

Because \(\mu(x)\to 1\) for large \(x\), the Hamiltonian density has the expansion
\[
\mathcal H(p)=\frac{|p|^2}{8\pi G}+O(e^{-|p|/a_0}),\qquad |p|\gg a_0.
\]
So, in strong-field regions, the vacuum energy becomes (up to exponentially small corrections) a quadratic penalty in \(\nabla\Phi\), which is exactly the Newtonian field energy.

This perspective is powerful: *Newtonian gravity is not “restored by hand”; it is the local quadratic tangent model of the convex vacuum energy*.

---

## 5. EFE as Hessian domination

Let \(\nabla\Phi=p_{\rm ext}+p_{\rm int}\) with \(|p_{\rm ext}|\gg a_0\). A Taylor expansion gives
\[
\mathcal H(p_{\rm ext}+p_{\rm int})
=\mathcal H(p_{\rm ext})+\langle\nabla_p\mathcal H(p_{\rm ext}),p_{\rm int}\rangle
+\tfrac12\langle p_{\rm int},D_p^2\mathcal H(p_{\rm ext})p_{\rm int}\rangle+\cdots.
\]
As \(|p_{\rm ext}|/a_0\to\infty\),
\[
D_p^2\mathcal H(p_{\rm ext})\to \frac{1}{4\pi G}I,
\]
so *internal fluctuations see an effectively Newtonian quadratic energy*.

This packages the EFE into a clean second-variation statement: an external strong field pushes you into the quadratic basin.

---

## 6. Asymptotics: flat rotation curves and BTFR

In spherical symmetry, Gauss’ law reduces the PDE to the algebraic relation
\[
\mu(g/a_0)\,g=g_N,\qquad g_N(r)=\frac{GM(r)}{r^2},\qquad g(r)=|\nabla\Phi|.
\]
In the far field where \(M(r)\to M_b\) and \(g\ll a_0\), one has \(\mu(x)\sim x\), hence
\[
\frac{g^2}{a_0}=\frac{GM_b}{r^2}
\quad\Rightarrow\quad
 g(r)=\frac{\sqrt{GM_b a_0}}{r}.
\]
Thus
\[
\Phi(r)\sim-\sqrt{GM_b a_0}\,\ln r,
\]
and circular motion \(V^2/r=g\) yields
\[
V^4=GM_b a_0.
\]
This is the BTFR with exact slope 4.

---

## 7. Where this can grow into a research program

1. **Rigorous matching (inner Newtonian / outer logarithmic)** without symmetry assumptions.
   - The project already has the variational uniqueness backbone; the next step is a matched-asymptotics theorem that quantifies the transition layer.

2. **A “convexity = screening” classification theorem.**
   - Replace \(\mu(x)=1-e^{-x}\) by a general saturating \(\mu\) and classify which \(\mu\) yield EFE + BTFR-like asymptotics.

3. **Nonlinear stability / dynamics.**
   - The present notes are elliptic (instantaneous). A dynamical relaxation flow (gradient flow of \(\mathcal E\)) would connect to well-posed evolution and could be compared with structure formation timescales.

4. **Relativistic embedding constraints.**
   - Hyperbolicity of the covariant scalar sector suggests a well-posed relativistic completion; the missing piece is a sharp statement linking the nonrelativistic convex energy to covariant energy conditions.

---

## Minimal “axioms → theorems” summary

- **Axiom:** the vacuum Hamiltonian \(\mathcal H\) is strictly convex and saturates to quadratic at large \(|\nabla\Phi|\).
- **Theorem:** unique minimizer exists (well-posedness).
- **Corollary:** Newtonian limit and EFE (Hessian domination).
- **Corollary:** logarithmic far-field potential \(\Rightarrow\) flat rotation curves \(\Rightarrow\) BTFR.


---

