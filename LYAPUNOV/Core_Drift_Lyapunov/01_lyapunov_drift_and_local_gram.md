# Lyapunov Drift for Lattice Yang–Mills via a Smooth Plaquette Proxy

## 0. What is extracted here

This file packages three pieces that, together, form a very sharp “reduce-to-a-finite-dimensional-inequality” step:

1. An **exact** drift identity for \(W=e^{\eta V}\) under the configuration diffusion generator \(L_\Lambda\).
2. A **volume-uniform** bound of \(\Gamma_\Lambda(V)\) in terms of \(V\), using only **incidence counting** and smoothness.
3. The reduction of a global Foster–Lyapunov drift inequality
   \[
   L_\Lambda W \le -\lambda W + b\,\mathbf 1_K
   \]
   to a **single local coercivity inequality**, plus (optional) two-regime strategies to prove it.

The crucial technical trick is replacing the nonsmooth \(d_G(\cdot,e)^2\) by a globally smooth proxy:
\[
\widetilde z(g)=1-\frac1N\Re\mathrm{Tr}(g),\qquad g\in \mathrm{SU}(N),
\]
so that all global sup-norm derivative constants exist.

---

## 1. Generator and carré du champ in link coordinates

Let
\[
M_\Lambda := G^{E(\Lambda)},\qquad G=\mathrm{SU}(N),
\]
with product bi-invariant metric. Fix an orthonormal basis \(\{T^a\}\) of \(\mathfrak g\).

For each link \(\ell\), let \(X_\ell^a\) be the right-invariant vector field acting on the \(\ell\)-factor only.
Define
\[
\Delta_\Lambda = \sum_{\ell\in E(\Lambda)}\sum_a (X_\ell^a)^2,\qquad
\Gamma_\Lambda(f,g)=\sum_{\ell,a}(X_\ell^a f)(X_\ell^a g),\quad \Gamma_\Lambda(f)=\Gamma_\Lambda(f,f).
\]

For a Gibbs measure \(d\mu_\Lambda\propto e^{-S_\Lambda}d\mathrm{vol}\),
the reversible diffusion generator is
\[
L_\Lambda f
=
\Delta_\Lambda f - \langle \nabla S_\Lambda,\nabla f\rangle
=
\sum_{\ell,a}\Big((X_\ell^a)^2 f-(X_\ell^a S_\Lambda)(X_\ell^a f)\Big).
\]

---

## 2. The exponential drift identity (exact)

Let
\[
V(U)=\sum_{p\in P(\Lambda)}\Phi(\widetilde z_p(U)),\qquad
W(U)=e^{\eta V(U)},
\]
where \(\Phi\in C^2([0,2])\) and
\[
\widetilde z_p(U) := \widetilde z(U_p(U)),\qquad \widetilde z(g)=1-\frac1N\Re\mathrm{Tr}(g).
\]

Then the diffusion chain rules give:

\[
\boxed{
\frac{L_\Lambda W}{W}=\eta\,L_\Lambda V+\eta^2\,\Gamma_\Lambda(V).
}
\]

Expanding \(L_\Lambda V\) termwise:
\[
\boxed{
L_\Lambda V
=
\sum_p \Phi'(\widetilde z_p)\,\Delta_\Lambda \widetilde z_p
+\sum_p \Phi''(\widetilde z_p)\,\Gamma_\Lambda(\widetilde z_p)
-
\langle \nabla S_\Lambda,\nabla V\rangle.
}
\]

So:
\[
\boxed{
\frac{L_\Lambda W}{W}
=
\eta\sum_p \Phi'(\widetilde z_p)\,\Delta_\Lambda \widetilde z_p
+\eta\sum_p \Phi''(\widetilde z_p)\,\Gamma_\Lambda(\widetilde z_p)
-\eta\,\langle \nabla S_\Lambda,\nabla V\rangle
+\eta^2\,\Gamma_\Lambda(V).
}
\]

Everything up to here is exact calculus on a compact product manifold.

---

## 3. Incidence counting: the volume-uniform \(\Gamma(V)\) bound

Define the plaquette incidence number
\[
P(\ell)=\{p\in P(\Lambda):\ \ell\subset \partial p\},\qquad
\nu:=\max_{\ell}|P(\ell)|.
\]
On the 4D hypercubic lattice: \(\nu=6\).

### 3.1 Uniform derivative constants for \(\widetilde z\)

Because \(G\) is compact and \(\widetilde z\in C^\infty(G)\), the following are finite:

\[
C_\nabla := \sup_{g\neq e}\frac{|\nabla \widetilde z(g)|^2}{\widetilde z(g)}<\infty,
\qquad
C_\Delta := \sup_{g\in G}|\Delta_G\widetilde z(g)|<\infty.
\]

By bi-invariance, these bounds transfer to plaquette functions \(\widetilde z_p(U)\).
In particular, for each plaquette \(p\) and link \(\ell\in\partial p\),
\[
\sum_a (X_\ell^a \widetilde z_p)^2 \le C_\nabla \widetilde z_p,
\qquad
\Big|\sum_a (X_\ell^a)^2\widetilde z_p\Big|\le C_\Delta,
\]
and summing over the 4 links of a plaquette yields
\[
\Gamma_\Lambda(\widetilde z_p)\le 4C_\nabla \widetilde z_p,\qquad |\Delta_\Lambda\widetilde z_p|\le 4C_\Delta.
\]

### 3.2 The combinatorics

First derivatives:
\[
X_\ell^a V = \sum_{p\in P(\ell)}\Phi'(\widetilde z_p)\,X_\ell^a\widetilde z_p.
\]

Use \(\big(\sum_{i=1}^m u_i\big)^2\le m\sum_{i=1}^m u_i^2\) with \(m\le\nu\), then sum over links and swap sums.
This gives
\[
\Gamma_\Lambda(V)
\le
4\nu C_\nabla \sum_{p}\big(\Phi'(\widetilde z_p)\big)^2\,\widetilde z_p.
\]

Introduce the one-variable constant
\[
K_\Phi := \sup_{s\in(0,2]}\frac{s(\Phi'(s))^2}{\Phi(s)}\in[0,\infty].
\]
If \(K_\Phi<\infty\), then \(s(\Phi')^2\le K_\Phi\Phi\) on \([0,2]\), hence:

\[
\boxed{
\Gamma_\Lambda(V)\ \le\ 4\nu C_\nabla K_\Phi\;V,
}
\]
with constants independent of \(|\Lambda|\).

This is the exact “overlap combinatorics” step: the only lattice input is \(\nu\).

---

## 4. Uniform upper bounds for the noncoercive drift terms

Define the extensive badness functional
\[
D(U):=\sum_{p\in P(\Lambda)}\widetilde z_p(U).
\]

Assume \(\Phi'(0)=0\). Then \(|\Phi'(s)|\le B_\Phi s\) on \([0,2]\), where
\[
B_\Phi:=\sup_{s\in(0,2]}\frac{|\Phi'(s)|}{s}\le \|\Phi''\|_\infty.
\]
Also \(A_\Phi:=\|\Phi''\|_\infty\).

Using the plaquette derivative bounds:
\[
\Big|\sum_p \Phi'(\widetilde z_p)\Delta_\Lambda \widetilde z_p\Big|
\le
4B_\Phi C_\Delta\,D,
\qquad
\sum_p \Phi''(\widetilde z_p)\Gamma_\Lambda(\widetilde z_p)
\le
4A_\Phi C_\nabla\,D.
\]

Therefore
\[
\boxed{
\frac{L_\Lambda W}{W}
\le
-\eta\,\langle \nabla S_\Lambda,\nabla V\rangle
+
\eta\,C_1 D
+\eta^2\,C_2 D,
}
\]
with \(C_1\) explicit in \((A_\Phi,B_\Phi,C_\nabla,C_\Delta)\) and \(C_2\) explicit via the \(\Gamma(V)\) estimate (and optionally \(V\lesssim D\) when \(\Phi(s)=s^2\), etc.).

---

## 5. The single missing inequality: coercivity of \(\langle \nabla S,\nabla V\rangle\)

Define
\[
\mathcal J(U):=\langle \nabla S_\Lambda(U),\nabla V(U)\rangle.
\]

Everything above reduces the Lyapunov drift
\[
L_\Lambda W \le -\lambda W + b\,\mathbf 1_K
\]
to showing, for some \(c_0>0\), \(b_0<\infty\), and a “small set” \(K\),
\[
\boxed{
\mathcal J(U)\ \ge\ c_0\,D(U)\ -\ b_0\,\mathbf 1_K(U),
}
\]
with \(c_0,b_0\) independent of \(\Lambda\).

Once this holds, choose \(\eta>0\) small enough to absorb the \(+(\eta C_1+\eta^2C_2)D\) error into the coercive \(-\eta c_0 D\) term.

This is the exact logical choke point.

---

## 6. What \(\mathcal J\) looks like for Wilson and why it’s not automatic

If \(S_\Lambda\) is Wilson:
\[
S_\Lambda=\beta\sum_q \widetilde z_q,
\]
then
\[
\mathcal J
=
\sum_{\ell,a}(X_\ell^a S_\Lambda)(X_\ell^a V)
=
\beta\sum_{\ell,a}
\Big(\sum_{q\in P(\ell)}X_\ell^a \widetilde z_q\Big)
\Big(\sum_{p\in P(\ell)}\Phi'(\widetilde z_p)X_\ell^a\widetilde z_p\Big).
\]

This is a bilinear form in the local vectors \(\{X_\ell^a \widetilde z_p\}_{p\in P(\ell)}\) with weights \(1\) and \(\Phi'(\widetilde z_p)\).
Unless the weights match (e.g. \(\Phi'\equiv 1\)), positivity is not automatic.

That is why the coercivity estimate is genuinely nontrivial.

---

## 7. A concrete finite-dimensional lemma you can prove exactly: the local Maxwell Gram matrix

One clean way to attack coercivity in the **small-field** regime is to linearize near the vacuum and reduce to discrete cochain operators.

Here is a fully explicit local Gram matrix computation that shows the relevant finite-dimensional matrix is strictly positive.

### 7.1 The local vectors \(w_p=d_1^\ast\delta_p\)

Work on the cochain complex
\[
\mathcal C^0 \xrightarrow{d_0} \mathcal C^1 \xrightarrow{d_1} \mathcal C^2.
\]
Let \(\delta_p\) be the plaquette basis vector in \(\mathcal C^2\). Define
\[
w_p := d_1^\ast\delta_p\in\mathcal C^1.
\]

For an oriented plaquette \(p=(x;\mu,\nu)\), \(\mu<\nu\), one has the explicit boundary-incidence formula
\[
w_{(x;\mu,\nu)} = e_{x,\mu} + e_{x+\hat\mu,\nu} - e_{x+\hat\nu,\mu} - e_{x,\nu},
\]
where \(e_{x,\mu}\) is the oriented edge basis in \(\mathcal C^1\).

### 7.2 Fix a link \(\ell=(x,\mu)\) and list its incident plaquettes

In \(d=4\), a link has \(m=6\) incident plaquettes:
for each \(\nu\neq \mu\), there are two:
\[
p_{\nu,+}:=(x;\mu,\nu),\qquad
p_{\nu,-}:=(x-\hat\nu;\mu,\nu).
\]

Define a sign vector \(s\in\{\pm1\}^6\) by the coefficient of the common edge \(e_{x,\mu}\) inside \(w_p\):
\[
s_{\nu,+}=+1,\qquad s_{\nu,-}=-1.
\]

### 7.3 The Gram matrix \(M\) and its determinant

Define the local Gram matrix
\[
M_{pq} := \langle w_p,w_q\rangle_{\mathcal C^1}.
\]

- Each \(w_p\) has exactly 4 nonzero edge coefficients \(\pm1\), so \(M_{pp}=4\).
- Any two distinct incident plaquettes share exactly one edge, namely the fixed link edge \(e_{x,\mu}\), with product sign \(s_p s_q\). Hence \(M_{pq}=s_ps_q\) for \(p\neq q\).

Therefore the matrix has the closed form
\[
\boxed{
M = 3I_6 + s s^\top.
}
\]

Since \(ss^\top\) has rank 1 and \(s^\top s=6\), the eigenvalues of \(M\) are
\[
\lambda=3 \text{ with multiplicity }5,\qquad
\lambda=3+6=9 \text{ with multiplicity }1.
\]
So
\[
\boxed{
\det M = 3^5\cdot 9 = 2187 >0,\qquad \lambda_{\min}(M)=3.
}
\]

This is an **exact**, volume-independent, purely local positivity statement.

### 7.4 Why this matters

When you linearize the Wilson action near the vacuum, the quadratic form is a multiple of \(d_1^\ast d_1\).
Local coercivity questions (especially those that appear in the small-field part of the drift coercivity estimate) reduce to finite-dimensional Gram bounds of this type.

---

## 8. Two-regime proof strategy for the nonlinear coercivity (what remains)

A common, sharp strategy is:

- **Large-field regime:** if some incident \(\widetilde z_p\) exceeds a threshold \(\varepsilon_0\), diagonal domination + smooth lower gradient bounds give coercivity with an explicit constant.
- **Small-field regime:** if all incident \(\widetilde z_p\le \varepsilon_0\), linearize \(U_\ell=\exp(X_\ell)\), reduce to discrete cochain operators, and use Gram positivity (as above) plus continuity.

The global Foster–Lyapunov drift is then obtained by summing the per-link inequalities and absorbing the small-field defect into the set \(K\).

That completes the reduction: the remaining work is finite-dimensional and geometric, not probabilistic.
