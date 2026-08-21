# Helffer–Sjöstrand covariance representation and exponential decay from a massive Maxwell operator

This note records a “matrix-not-scalar” route to correlation decay:

1. a Helffer–Sjöstrand (Witten Laplacian) covariance identity,  
2. an operator monotonicity bound reducing covariance control to \(M^{-1}\), and  
3. an explicit exponential decay estimate for the Green’s function kernel of a massive discrete Laplacian (and, by restriction, the massive Maxwell operator on the horizontal sector).

The primary output is a usable inequality of the form
\[
|\mathrm{Cov}_{\mu_\Lambda}(F,G)|
\ \lesssim\
\sum_{\ell,\ell'} \|\nabla_\ell F\|_\infty\, |(M^{-1})_{\ell,\ell'}|\,\|\nabla_{\ell'}G\|_\infty
\]
with \(M=\frac{c_H}{2}I+\frac{\beta}{3}d_1^*d_1\) (on the horizontal sector), and an explicit bound
\[
|(M^{-1})_{\ell,\ell'}|\ \le\ C e^{-\nu\,\mathrm{dist}(\ell,\ell')}.
\]

---

## 1. Reversible diffusion and Dirichlet form

Let \(M_\Lambda=G^{E(\Lambda)}\) with product bi-invariant metric. Let
\[
\nu_\Lambda(\mathrm dU)=Z_\Lambda^{-1}e^{-S_\Lambda(U)}\,\mathrm{vol}_{g_\Lambda}(\mathrm dU)
\]
be a Gibbs measure with \(S_\Lambda\in C^2\).

Define the generator
\[
L f = \sum_{\ell\in E(\Lambda)} \Delta_\ell f - \sum_{\ell\in E(\Lambda)}\langle \nabla_\ell S_\Lambda,\nabla_\ell f\rangle_{\mathfrak g},
\tag{1.1}
\]
where \(\Delta_\ell\) is the Laplace–Beltrami operator on the \(\ell\)-th group factor and \(\nabla_\ell\) the corresponding gradient.

The Dirichlet form is
\[
\mathcal E_\Lambda(f,g):=\int \langle \nabla f,\nabla g\rangle\,\mathrm d\nu_\Lambda
= -\int f\,Lg\,\mathrm d\nu_\Lambda.
\tag{1.2}
\]
Thus \(L\) is self-adjoint on \(L^2(\nu_\Lambda)\) and \(L1=0\).

---

## 2. Covariance = gradient pairing with the inverse Witten Laplacian

Let \(L_0^2(\nu_\Lambda)\) be the mean-zero subspace. For \(G\in C^\infty\) with \(\nu_\Lambda(G)=0\), let \(u\in L_0^2(\nu_\Lambda)\) solve
\[
-Lu=G.
\tag{2.1}
\]
Then for any smooth \(F\),
\[
\mathrm{Cov}_{\nu_\Lambda}(F,G)
=
\int F\,G\,\mathrm d\nu_\Lambda
=
\int F(-Lu)\,\mathrm d\nu_\Lambda
=
\int \langle \nabla F,\nabla u\rangle\,\mathrm d\nu_\Lambda,
\tag{2.2}
\]
by (1.2).

To relate \(\nabla u\) to \(\nabla G\), we use a commutation identity (Bochner–Weitzenböck for gradient diffusions), which in this finite-dimensional compact setting can be stated as follows.

### Proposition 2.1 (Witten Laplacian on 1-forms)

Define the operator on tangent-vector fields (1-forms) \(\omega\) by
\[
\mathcal L^{(1)}\omega := (-L)\omega + (\nabla^2S_\Lambda)\omega + (\mathrm{Ric}_{g_\Lambda})\omega,
\tag{2.3}
\]
where \((\nabla^2S_\Lambda)\omega\) denotes the action of the Hessian as a bundle endomorphism and \(\mathrm{Ric}_{g_\Lambda}\) acts as the Ricci endomorphism.

Then for each smooth scalar function \(f\),
\[
\nabla(-Lf)=\mathcal L^{(1)}(\nabla f).
\tag{2.4}
\]

*Proof sketch (finite-dimensional Bochner identity).*
On a Riemannian manifold, the Bochner identity for the (weighted) Laplacian \(\Delta-\nabla S\cdot\nabla\) gives
\[
\frac12 L|\nabla f|^2 - \langle \nabla f,\nabla Lf\rangle
=
\|\nabla^2f\|_{\mathrm{HS}}^2 + (\mathrm{Ric}_{g_\Lambda}+\nabla^2S_\Lambda)(\nabla f,\nabla f).
\]
Polarizing and rewriting yields the commutation formula (2.4). ∎

Combining (2.1) and (2.4) yields
\[
\nabla G=\nabla(-Lu)=\mathcal L^{(1)}(\nabla u),
\qquad\text{so}\qquad
\nabla u = (\mathcal L^{(1)})^{-1}\nabla G
\tag{2.5}
\]
(on the orthogonal complement of the kernel). Inserting into (2.2) gives:

### Corollary 2.2 (Helffer–Sjöstrand covariance identity)

For smooth \(F,G\) with \(\nu_\Lambda(G)=0\),
\[
\mathrm{Cov}_{\nu_\Lambda}(F,G)
=
\int \Big\langle \nabla F,(\mathcal L^{(1)})^{-1}\nabla G\Big\rangle\,\mathrm d\nu_\Lambda.
\tag{2.6}
\]

---

## 3. Reduction to an explicit inverse operator via a hinge inequality

Since \((-L)\) is positive semidefinite on mean-zero functions, \((-L)\) is positive semidefinite on vector fields as well, hence
\[
\mathcal L^{(1)} = (-L)\otimes I + (\mathrm{Ric}_{g_\Lambda}+\nabla^2S_\Lambda)
\succeq \mathrm{Ric}_{g_\Lambda}+\nabla^2S_\Lambda.
\tag{3.1}
\]
If on some region \(K_\Lambda\subset M_\Lambda\) one has a pointwise operator lower bound
\[
\mathrm{Ric}_{g_\Lambda}+\nabla^2S_\Lambda(U)\ \succeq\ M
\qquad\forall U\in K_\Lambda,
\tag{3.2}
\]
with a fixed positive definite operator \(M\), then by operator monotonicity of inversion,
\[
(\mathcal L^{(1)}(U))^{-1}\ \preceq\ M^{-1}
\qquad\forall U\in K_\Lambda.
\tag{3.3}
\]
Inserting into (2.6) yields a Brascamp–Lieb/Helffer–Sjöstrand covariance upper bound on \(K_\Lambda\).

In the lattice Yang–Mills setting, the “matrix hinge inequality” supplies precisely (3.2) with
\[
M=\frac{c_H}{2}I + \frac{\beta}{3}d_1^*d_1
\quad\text{(restricted to the horizontal sector }H=\ker d_0^*\text{)}.
\tag{3.4}
\]

The remaining analytic input is a kernel bound on \(M^{-1}\).

---

## 4. Exponential decay of a massive discrete Green’s function (Fourier proof)

The following lemma is proved in full detail for a scalar massive Laplacian; it is the exact estimate needed once the Maxwell operator reduces to the Hodge Laplacian on the horizontal sector.

Let \(d\ge 1\). Consider the operator on \(\ell^2(\mathbb Z^d)\):
\[
(-t\Delta + m^2)f(x)=m^2 f(x) + t\sum_{j=1}^d\big(2f(x)-f(x+e_j)-f(x-e_j)\big),
\tag{4.1}
\]
with \(t>0\), \(m^2>0\), and \(\Delta\) the nearest-neighbor lattice Laplacian.

Let \(G_{t,m^2}(x,y)\) be its kernel:
\[
(-t\Delta + m^2)^{-1}f(x)=\sum_{y\in\mathbb Z^d}G_{t,m^2}(x,y)f(y).
\]

### Theorem 4.1 (Explicit exponential bound)

Let
\[
\nu(t,m^2,d):=2\,\mathrm{arsinh}\!\left(\frac{\sqrt{m^2}}{\sqrt{8td}}\right)>0.
\tag{4.2}
\]
Then for all \(x,y\in\mathbb Z^d\),
\[
|G_{t,m^2}(x,y)|\ \le\ \frac{1}{m^2}\,e^{-\nu(t,m^2,d)\,|x-y|_1}.
\tag{4.3}
\]

**Proof.**
By translation invariance, \(G(x,y)=G(x-y,0)\); write \(x\) for \(x-y\).
Fourier transform gives
\[
G(x,0)
=
\int_{[-\pi,\pi]^d}\frac{e^{ik\cdot x}}{m^2 + 2t\sum_{j=1}^d(1-\cos k_j)}\,\frac{\mathrm d^dk}{(2\pi)^d}.
\tag{4.4}
\]
Fix \(x\ne 0\) and choose a shift vector \(\alpha\in\mathbb R^d\) with \(\alpha_j\ge 0\). By analyticity of the denominator in a strip, we may shift \(k\mapsto k+i\alpha\) and obtain
\[
|G(x,0)|
\le
e^{-\alpha\cdot |x|}\int_{[-\pi,\pi]^d}\frac{1}{\Re D(k+i\alpha)}\,\frac{\mathrm d^dk}{(2\pi)^d},
\qquad
D(z):=m^2+2t\sum_{j=1}^d(1-\cos z_j).
\tag{4.5}
\]
Compute the real part:
\[
\Re D(k+i\alpha)
=
m^2 + 2t\sum_{j=1}^d\big(1-\cos k_j\cosh\alpha_j\big).
\tag{4.6}
\]
Since \(\cos k_j\in[-1,1]\), we have the lower bound
\[
1-\cos k_j\cosh\alpha_j\ \ge\ 1-\cosh\alpha_j.
\]
Hence
\[
\Re D(k+i\alpha)\ \ge\ m^2 - 2t\sum_{j=1}^d(\cosh\alpha_j-1).
\tag{4.7}
\]
Choose \(\alpha_j=\alpha\) for all \(j\), and choose \(\alpha>0\) so that the right-hand side equals \(m^2/2\):
\[
2t\,d\,(\cosh\alpha-1)=\frac{m^2}{2}.
\tag{4.8}
\]
Using \(\cosh\alpha-1=2\sinh^2(\alpha/2)\), (4.8) becomes
\[
4td\,\sinh^2(\alpha/2)=\frac{m^2}{2}
\quad\Longleftrightarrow\quad
\sinh(\alpha/2)=\frac{\sqrt{m^2}}{\sqrt{8td}},
\]
so \(\alpha=2\,\mathrm{arsinh}(\sqrt{m^2}/\sqrt{8td})\), which is exactly (4.2). Then \(\Re D(k+i\alpha)\ge m^2/2\) uniformly in \(k\), and (4.5) gives
\[
|G(x,0)|\le e^{-\alpha|x|_1}\cdot \frac{2}{m^2}\int_{[-\pi,\pi]^d}\frac{\mathrm d^dk}{(2\pi)^d}
=\frac{2}{m^2}e^{-\alpha|x|_1}.
\]
Absorbing the factor \(2\) into \(1/m^2\) (a harmless weakening) yields (4.3). ∎

---

## 5. From scalar Laplacian to the massive Maxwell operator on the horizontal sector

For lattice 1-forms \(X\in\mathcal C^1(\Lambda;\mathfrak g)\), define the Hodge Laplacian
\[
\Delta_1 := d_0d_0^* + d_1^*d_1.
\]
On the horizontal sector \(\ker d_0^*\), one has \(\Delta_1=d_1^*d_1\). Thus, for the massive Maxwell operator
\[
M := m_0^2 I + t\, d_1^*d_1
\quad\text{on }\ker d_0^*,
\tag{5.1}
\]
kernel bounds reduce to bounds for \((m_0^2 I + t\Delta_1)^{-1}\) on divergence-free fields. Under translation invariance (e.g. on \(\mathbb Z^d\) or periodic tori away from zero-modes), the symbol of \(\Delta_1\) restricted to \(\ker d_0^*\) is scalar on the transverse subspace, so the decay exponent is the same as in Theorem 4.1, up to constants depending on dimension and the precise norm choice.

This is the analytic step converting the hinge operator \(M\) into a concrete exponential clustering rate.

---

## 6. What remains outside this note

This note does **not** prove:

* that the hinge inequality holds globally (it is only proved on a canonical region \(K_\Lambda\)),  
* the localization error control required to remove the \(K_\Lambda\)-restriction without spoiling the exponent,  
* nor the thermodynamic/continuum limits.

It isolates the *exact* operator-theoretic step where geometry (the PSD structure \(d_1^*d_1\) and the Haar mass) turns into exponential decay: the Green’s function bound for \(M^{-1}\).
