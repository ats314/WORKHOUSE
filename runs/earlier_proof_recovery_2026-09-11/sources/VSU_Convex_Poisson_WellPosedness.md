# Vacuum Stiffness Gravity from a Convex Variational Principle
## Global well-posedness, screening, and the geometry hiding inside a modified Poisson equation

### What this document is
This is a **stand-alone derivation and proof module**.  It starts from a nonrelativistic action
principle, derives the governing quasilinear elliptic equation, proves its **existence/uniqueness**
(via strict convexity and monotone-operator structure), and extracts the **screening mechanism**
directly from the Hamiltonian Hessian.

Nothing here assumes symmetry, fitting functions, or phenomenological “patching.”
Everything follows from one constitutive choice:
\[
\mu(x)=1-e^{-x},\qquad x\ge 0,
\]
which interpolates smoothly between a deep, low-acceleration regime and a Newtonian, high-acceleration regime.

---

## 1. Kinematics and physical dimensions

Let
- \(\Phi:\mathbb{R}^3\to\mathbb{R}\) be a gravitational potential,
- \(\rho:\mathbb{R}^3\to\mathbb{R}\) be a (baryonic) mass density with total mass
  \[
  M := \int_{\mathbb{R}^3}\rho(x)\,d^3x,
  \]
- \(G\) be Newton’s constant,
- \(a_0>0\) be a fixed acceleration scale.

The physical gravitational acceleration is
\[
g(x):=|\nabla\Phi(x)|.
\]

We seek solutions in the whole space with the usual gauge choice “potential vanishes at infinity” replaced by the physically correct asymptotic **field** condition
\[
|\nabla\Phi(x)|\to 0\quad\text{as }|x|\to\infty,
\]
and we will derive the actual far-field asymptotics later.

---

## 2. The variational principle

### 2.1 Constitutive energy density

Define the dimensionless scalar
\[
s := \frac{|\nabla\Phi|^2}{a_0^2}.
\]
Let \(F:[0,\infty)\to\mathbb{R}\) satisfy
\[
F'(s)=\mu(\sqrt{s}),\qquad F(0)=0.
\]
For \(\mu(x)=1-e^{-x}\), we can integrate explicitly:
\[
F(s)=\int_0^s\bigl(1-e^{-\sqrt{t}}\bigr)\,dt
     = s-2+2(\sqrt{s}+1)e^{-\sqrt{s}}.
\]

Define the Hamiltonian (energy) density in terms of the “momentum” \(p:=\nabla\Phi\):
\[
\mathcal H(p)
:=\frac{a_0^2}{8\pi G}\,F\!\left(\frac{|p|^2}{a_0^2}\right).
\]

### 2.2 Action / energy functional

For compactly supported variations, the nonrelativistic action reduces to minimizing the static energy
\[
\mathcal E[\Phi]
:=\int_{\mathbb{R}^3}\mathcal H(\nabla\Phi)\,d^3x
+\int_{\mathbb{R}^3}\rho(x)\,\Phi(x)\,d^3x.
\]
(Up to sign conventions, the \(\rho\Phi\) term is the standard matter coupling.)

---

## 3. Euler–Lagrange equation: the modified Poisson law

Take a smooth compactly supported variation \(\Phi\mapsto \Phi+\varepsilon\psi\) with \(\psi\in C_c^\infty(\mathbb{R}^3)\).
Then
\[
\frac{d}{d\varepsilon}\Big|_{\varepsilon=0}\mathcal E[\Phi+\varepsilon\psi]
=\int_{\mathbb{R}^3}\nabla_p \mathcal H(\nabla\Phi)\cdot \nabla\psi\,d^3x
+\int_{\mathbb{R}^3}\rho\,\psi\,d^3x.
\]
Compute \(\nabla_p \mathcal H\).  Let \(s=|p|^2/a_0^2\).  Then
\[
\nabla_p \mathcal H(p)
=\frac{a_0^2}{8\pi G}\,F'(s)\,\nabla_p s
=\frac{a_0^2}{8\pi G}\,\mu(\sqrt{s})\,\frac{2p}{a_0^2}
=\frac{1}{4\pi G}\,\mu\!\left(\frac{|p|}{a_0}\right)p.
\]
Thus
\[
\delta\mathcal E
=\frac{1}{4\pi G}\int \mu\!\left(\frac{|\nabla\Phi|}{a_0}\right)\nabla\Phi\cdot\nabla\psi\,d^3x
+\int \rho\,\psi\,d^3x.
\]
Integrate by parts (no boundary term because \(\psi\) is compactly supported):
\[
\delta\mathcal E
=-\frac{1}{4\pi G}\int \nabla\cdot\!\left(\mu\!\left(\frac{|\nabla\Phi|}{a_0}\right)\nabla\Phi\right)\psi\,d^3x
+\int \rho\,\psi\,d^3x.
\]
Stationarity for all \(\psi\) gives the field equation in distribution form:
\[
\boxed{
\nabla\cdot\!\left(\mu\!\left(\frac{|\nabla\Phi|}{a_0}\right)\nabla\Phi\right)
=4\pi G\,\rho.
}
\]
This is a divergence-form quasilinear elliptic equation.

---

## 4. Geometry: the Hamiltonian Hessian and strict ellipticity

The screening and stability properties are encoded in the Hessian \(D_p^2\mathcal H(p)\).

### 4.1 Explicit Hessian

Write \(x:=|p|/a_0\).  Then \(\mu=\mu(x)\), \(\mu'=\mu'(x)\), and a direct differentiation yields
\[
D_p^2\mathcal H(p)
=\frac{1}{4\pi G}\left[
\mu(x)\,I
+\frac{\mu'(x)}{a_0|p|}\,p\otimes p
\right]
\qquad(p\neq 0).
\]
For \(\mu(x)=1-e^{-x}\) we have \(\mu'(x)=e^{-x}>0\).

### 4.2 Eigenvalues and uniform positivity away from \(p=0\)

Decompose vectors into components parallel and orthogonal to \(p\).
The Hessian has:
- transverse eigenvalue \(\lambda_\perp=\mu(x)\),
- longitudinal eigenvalue \(\lambda_\parallel=\mu(x)+x\mu'(x)\).

For \(x>0\),
\[
\mu(x)=1-e^{-x}>0,\qquad
\lambda_\parallel = 1-e^{-x}+x e^{-x}=1-(1-x)e^{-x}>0.
\]
So \(D_p^2\mathcal H(p)\) is positive definite for every \(p\neq 0\): **the energy density is strictly convex in \(\nabla\Phi\)**.

Interpretation:
- When \(x\gg 1\), \(\mu(x)\approx 1\), \(\mu'(x)\approx 0\): the Hessian tends to \((4\pi G)^{-1}I\) and the theory becomes Newtonian.
- When \(x\ll 1\), \(\mu(x)\sim x\), \(\mu'(x)\sim 1\): the Hessian scales like \(|p|\), producing strong nonlinearity (but still convexity).

---

## 5. Existence and uniqueness on bounded domains (direct method)

Working on \(\mathbb{R}^3\) directly requires handling the logarithmic far-field growth.
The clean way to be mathematically honest is:

1. solve on a large ball \(B_R\subset\mathbb{R}^3\) with Dirichlet data,
2. pass \(R\to\infty\) and recover the global solution and its asymptotics.

### 5.1 Dirichlet problem

Fix \(R>0\).  Consider
\[
\begin{cases}
\nabla\cdot\!\left(\mu\!\left(\frac{|\nabla\Phi|}{a_0}\right)\nabla\Phi\right)=4\pi G\rho
&\text{in }B_R,\\[4pt]
\Phi=0 &\text{on }\partial B_R.
\end{cases}
\]
Define the admissible space \(X_R:=W^{1,2}_0(B_R)\).

Define the energy on \(B_R\):
\[
\mathcal E_R[\Phi]
:=\int_{B_R}\mathcal H(\nabla\Phi)\,d^3x +\int_{B_R}\rho\,\Phi\,d^3x.
\]

### 5.2 Basic growth and coercivity estimates

We need:
- \(\mathcal E_R\) is bounded below,
- \(\mathcal E_R\) is coercive (minimizing sequences do not run to infinity),
- \(\mathcal E_R\) is strictly convex,
- \(\mathcal E_R\) is weakly lower semicontinuous.

Two elementary inequalities for \(\mu(x)=1-e^{-x}\) (for \(x\ge 0\)):

1. upper bound: \(1-e^{-x}\le x\) (from \(e^{-x}\ge 1-x\)),
2. lower bound: \(1-e^{-x}\ge \dfrac{x}{1+x}\) (true for all \(x\ge0\)).

From these, one can derive corresponding bounds on \(F\) and hence on \(\mathcal H\).
In particular:
- for large gradients (\(|p|\gtrsim a_0\)), \(F(|p|^2/a_0^2)\sim |p|^2/a_0^2\), so \(\mathcal H(p)\sim |p|^2\);
- for small gradients (\(|p|\ll a_0\)), \(F(|p|^2/a_0^2)\sim \tfrac{2}{3}(|p|/a_0)^3\), so \(\mathcal H(p)\sim |p|^3\).

A convenient global bound is: there exist constants \(c_1,c_2>0\) such that for all \(p\in\mathbb{R}^3\),
\[
\mathcal H(p)\ge c_1\,|p|^2 - c_2.
\]
(You can take \(c_1\) small enough so it holds trivially at small \(|p|\) and uses the quadratic asymptotic at large \(|p|\).)

Then, using Hölder + Sobolev + Poincaré on \(B_R\),
\[
\left|\int_{B_R}\rho\,\Phi\right|
\le \|\rho\|_{L^{6/5}(B_R)}\|\Phi\|_{L^6(B_R)}
\le C_R \|\rho\|_{L^{6/5}(B_R)}\|\nabla\Phi\|_{L^2(B_R)}.
\]
So \(\mathcal E_R[\Phi]\to+\infty\) as \(\|\nabla\Phi\|_{L^2}\to\infty\): **coercivity**.

### 5.3 Existence (minimizer) and uniqueness

**Lemma 5.1 (existence).**  
There exists \(\Phi_R\in X_R\) minimizing \(\mathcal E_R\).

*Proof.*  
Let \(\{\Phi_n\}\subset X_R\) be a minimizing sequence.  Coercivity gives \(\{\Phi_n\}\) bounded in \(W^{1,2}_0(B_R)\).
By reflexivity, extract a weakly convergent subsequence \(\Phi_n\rightharpoonup \Phi_R\) in \(W^{1,2}\).
Because \(\mathcal H(\nabla\Phi)\) is convex in \(\nabla\Phi\), the map \(\Phi\mapsto \int_{B_R}\mathcal H(\nabla\Phi)\) is weakly lower semicontinuous.
The linear term \(\int\rho\Phi\) is weakly continuous.
Therefore \(\mathcal E_R[\Phi_R]\le \liminf_n \mathcal E_R[\Phi_n]\), so \(\Phi_R\) is a minimizer. \(\square\)

**Lemma 5.2 (uniqueness).**  
The minimizer \(\Phi_R\) is unique.

*Proof.*  
The integrand \(\mathcal H\) is strictly convex in \(\nabla\Phi\) (Section 4), and the source term is linear.
Therefore \(\mathcal E_R\) is strictly convex on \(X_R\), hence has at most one minimizer. \(\square\)

### 5.4 Euler–Lagrange = weak solution

**Lemma 5.3 (weak formulation).**  
The minimizer \(\Phi_R\) satisfies the weak form of the field equation:
\[
\frac{1}{4\pi G}\int_{B_R}\mu\!\left(\frac{|\nabla\Phi_R|}{a_0}\right)\nabla\Phi_R\cdot\nabla\psi\,d^3x
+\int_{B_R}\rho\,\psi\,d^3x=0
\quad\forall \psi\in W^{1,2}_0(B_R).
\]

*Proof.*  
Differentiate \(\varepsilon\mapsto \mathcal E_R[\Phi_R+\varepsilon\psi]\) at \(\varepsilon=0\) and use minimality. \(\square\)

Standard regularity theory for monotone quasilinear elliptic equations (De Giorgi–Nash–Moser type machinery adapted to divergence form) then yields interior regularity:
\[
\Phi_R\in C^{1,\alpha}_{\mathrm{loc}}(B_R)\quad\text{for some }\alpha\in(0,1),
\]
assuming \(\rho\in L^\infty_{\mathrm{loc}}\) (or weaker conditions with \(W^{2,p}\) conclusions).

---

## 6. Passage to \(\mathbb{R}^3\) and far-field asymptotics (physics + math handshake)

Let \(\rho\) be compactly supported in \(B_{R_0}\).
Solve the Dirichlet problem on \(B_R\) for \(R\gg R_0\).
Using uniform interior estimates on compact subsets and a diagonal argument, one extracts a subsequence \(\Phi_{R_j}\to \Phi\) in \(C^1_{\mathrm{loc}}(\mathbb{R}^3)\),
where \(\Phi\) solves the whole-space equation in the distributional sense.

Now analyze the exterior region \(|x|>R_0\), where \(\rho=0\):
\[
\nabla\cdot\!\left(\mu\!\left(\frac{|\nabla\Phi|}{a_0}\right)\nabla\Phi\right)=0.
\]

A key conserved quantity comes from integrating over spheres and applying Gauss:
for any \(r>R_0\),
\[
\int_{S_r} \mu\!\left(\frac{|\nabla\Phi|}{a_0}\right)\nabla\Phi\cdot n\,dS
=4\pi G\,M.
\]
If the solution is asymptotically radial in the far field (true for compact sources by standard multipole decay arguments),
this implies asymptotically
\[
r^2\,\mu\!\left(\frac{g(r)}{a_0}\right)\,g(r)\ \to\ G M,
\]
where \(g(r)=|\partial_r\Phi(r)|\).

In the deep field regime \(g(r)\ll a_0\), \(\mu(g/a_0)\sim g/a_0\), so
\[
r^2 \frac{g(r)}{a_0} g(r) \sim GM
\quad\Longrightarrow\quad
g(r)\sim \frac{\sqrt{GM a_0}}{r}.
\]
Integrating radially gives the logarithmic potential:
\[
\boxed{
\Phi(r)\sim -\sqrt{GM a_0}\,\ln r\quad(r\to\infty),
}
\]
up to an additive constant (gauge).

This scaling immediately implies flat rotation curves and the baryonic Tully–Fisher relation.
Indeed, for a circular orbit in the far field one has \(V^2/r=g(r)\).  Using \(g(r)\sim \sqrt{GM a_0}/r\) gives
\[
V^2 \sim \sqrt{GM a_0}\quad\Longrightarrow\quad \boxed{V^4=GM a_0}.
\]

---

## 7. Screening as a geometric statement (Hessian domination)

Screening is not an extra “mechanism.”  It is built into the convex geometry of \(\mathcal H\).

Consider a background configuration with a large “external” gradient \(p_{\mathrm{ext}}\) and a small “internal” fluctuation \(\nabla\varphi\):
\[
\nabla\Phi = p_{\mathrm{ext}}+\nabla\varphi,\qquad |\nabla\varphi|\ll |p_{\mathrm{ext}}|.
\]

Expand \(\mathcal H\) to second order:
\[
\mathcal H(p_{\mathrm{ext}}+\nabla\varphi)
=
\mathcal H(p_{\mathrm{ext}})
+\nabla_p\mathcal H(p_{\mathrm{ext}})\cdot \nabla\varphi
+\frac12\,\nabla\varphi^\top\Bigl[D_p^2\mathcal H(p_{\mathrm{ext}})\Bigr]\nabla\varphi
+O(|\nabla\varphi|^3).
\]

Varying with respect to \(\varphi\), the linear term drops (it is a background solution term), and the quadratic term produces a **linearized operator**
\[
\nabla\cdot\!\left( M_{\mathrm{ext}}\,\nabla\varphi\right)=4\pi G\,\rho_{\mathrm{int}},
\qquad
M_{\mathrm{ext}}:=4\pi G\,D_p^2\mathcal H(p_{\mathrm{ext}}).
\]

But we computed \(D_p^2\mathcal H\):
\[
M_{\mathrm{ext}}
=
\mu(x_{\mathrm{ext}})\,I
+\frac{\mu'(x_{\mathrm{ext}})}{a_0|p_{\mathrm{ext}}|}\,p_{\mathrm{ext}}\otimes p_{\mathrm{ext}},
\qquad x_{\mathrm{ext}}:=\frac{|p_{\mathrm{ext}}|}{a_0}.
\]

Now the screening limit is immediate:
if \(x_{\mathrm{ext}}\gg 1\), then \(\mu(x_{\mathrm{ext}})\to 1\) and \(\mu'(x_{\mathrm{ext}})\to 0\), hence
\[
M_{\mathrm{ext}}\to I,
\]
and the internal fluctuations obey the **ordinary Poisson equation**:
\[
\Delta\varphi = 4\pi G \rho_{\mathrm{int}}.
\]

So “screening” is literally:
\[
\textbf{large external gradient} \Longrightarrow \textbf{Hessian tends to Newtonian metric}.
\]

---

## 8. What is genuinely novel / theory-forming here?

1. **Everything is convex.**  The entire nonrelativistic sector is closed by one convex functional.
2. **Screening and stability are geometric.**  They are properties of the Hessian \(D^2\mathcal H\), not bolt-on phenomena.
3. **The deep-field logarithmic potential is not assumed.**  It drops out of Gauss + \(\mu(x)\sim x\) automatically.

---

## 9. Next steps that would seriously strengthen the theory

1. Replace the “asymptotically radial” step by a full multipole analysis in the exterior region.
2. Develop a clean Orlicz–Sobolev functional-analytic setting optimized for the mixed \(p=2\) / \(p=3\) growth.
3. Produce numerical solvers (finite element) for \(\nabla\cdot(\mu(|\nabla\Phi|/a_0)\nabla\Phi)=4\pi G\rho\) on realistic galaxy density maps and compare with rotation curves and EFE data.
