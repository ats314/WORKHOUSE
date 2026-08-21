# Matrix covariance via Helffer–Sjöstrand and explicit Green’s-function decay on \(\ker d_0^*\)

## Scope

This note extracts a coherent “operator pipeline” that appears in the improved stack:

1. Use Helffer–Sjöstrand/Witten-Laplacian representation to express covariance as an inverse operator on 1-forms.
2. Lower-bound the curvature matrix by a structured operator \(M = m^2 I + t\,d_1^*d_1\) on the horizontal sector.
3. Prove an explicit exponential off-diagonal bound for \(M^{-1}\) on \(\ker d_0^*\) by a Fourier-symbol scalarization.

The novelty here is not that each ingredient exists in the literature, but that the project keeps the **matrix** structure all the way to an explicit exponential exponent, avoiding absolute-value scalarization.

---

## 1. Helffer–Sjöstrand covariance representation (operator form)

Let \((M,g)\) be a compact Riemannian manifold and \(\nu\) a smooth probability measure with density \(e^{-S}\) w.r.t. \(\mathrm{vol}_g\). Let
\[
L = \Delta - \langle \nabla S,\nabla\cdot\rangle
\]
be the associated reversible generator, and let \(\mathcal E(F,G)=\int\langle\nabla F,\nabla G\rangle\,d\nu\) be the Dirichlet form.

For centered observables \(F,G\) (i.e. \(\int F\,d\nu=\int G\,d\nu=0\)), the project uses the Helffer–Sjöstrand formula:
\[
\mathrm{Cov}_\nu(F,G)
=
\int_M \big\langle \nabla F,\ (L^{(1)})^{-1}\nabla G\big\rangle\,d\nu,
\tag{1.1}
\]
where \(L^{(1)}\) is the Witten Laplacian on 1-forms:
\[
L^{(1)} = \nabla^*\nabla + \mathrm{Ric}_g + \nabla^2 S,
\tag{1.2}
\]
acting on vector fields / 1-forms under the metric identification.

Thus covariance is controlled by the inverse of a **matrix Schrödinger operator** whose potential term is exactly the Bakry–Émery curvature matrix \(\mathrm{Ric}_g+\nabla^2 S\).

---

## 2. The structured lower bound on the curvature matrix (the “hinge”)

On a lattice configuration manifold \(M_\Lambda=G^{E(\Lambda)}\), the project’s hinge inequalities show that on a canonical small-field region \(K_\Lambda\),
\[
\mathrm{Ric}_{\mu_\Lambda}(U)\big|_{H_{U^{(0)}}}
\ \succeq\
m^2 I + t\,d_1^*d_1
\quad\text{(as quadratic forms on }H_{U^{(0)}}=\ker d_0^*),
\tag{2.1}
\]
with
\[
m^2 \sim \frac{c_H}{2}>0 \quad\text{(Haar/Ricci floor)},\qquad
t\sim \frac{\beta}{3}>0 \quad\text{(Wilson quadratic form)}.
\]
This is the matrix object one wants to invert.

Define the operator
\[
M := m^2 I + t\,d_1^*d_1\quad\text{on }H_{U^{(0)}}=\ker d_0^*.
\tag{2.2}
\]
Since \(M\succeq m^2 I\), it is invertible and its inverse is the Green operator
\[
G := M^{-1}.
\]

When (2.1) holds pointwise in \(U\) (on \(K_\Lambda\)), (1.1) and operator monotonicity yield a schematic bound
\[
|\mathrm{Cov}_{\mu_\Lambda}(F,G)|
\ \lesssim\
\int_{K_\Lambda}\langle |\nabla F|,\ G\,|\nabla G|\rangle\,d\mu_\Lambda
\ +\ (\text{localization error}).
\tag{2.3}
\]

---

## 3. The “Maxwell symbol becomes scalar on \(\ker d_0^*\)” lemma

A key project-specific simplification is that on the **horizontal (divergence-free)** sector, the symbol of \(d_1^*d_1\) collapses to the scalar lattice Laplacian symbol. This allows a direct Fourier contour-shift proof of exponential decay with explicit exponent.

### Lemma 3.1 (Exponential decay of \(G=M^{-1}\) on \(\ker d_0^*\), infinite lattice)

Work on \(\mathbb Z^d\), \(d\ge 2\). Let
\[
H_{U^{(0)}}:=\ker(d_0^*)\subset \ell^2\mathcal C^1(\mathbb Z^d;\mathfrak g),
\qquad
M=m^2I+t\,d_1^*d_1
\quad\text{on }H_{U^{(0)}},
\]
with \(m^2>0\), \(t>0\). Let \(G=M^{-1}\).

Define the explicit decay exponent
\[
\nu(m^2,t)\;:=\;2\,\operatorname{arsinh}\!\Big(\frac{\sqrt{m^2}}{\sqrt{8td}}\Big).
\tag{3.1}
\]
Then the Green kernel blocks satisfy
\[
\big\|G_{(x,\mu),(y,\nu)}\big\|_{\mathrm{op}(\mathfrak g)}
\ \le\
\frac{2}{m^2}\,e^{-\nu(m^2,t)\,|x-y|_1}.
\tag{3.2}
\]

In the project’s parameters \(m^2=c_H/2\), \(t=\beta/3\),
\[
\nu(c_H,\beta)
=
2\,\operatorname{arsinh}\!\Big(\frac{\sqrt{3}\sqrt{c_H}}{4\sqrt{\beta}\sqrt{d}}\Big),
\qquad
\|G_{\ell,\ell'}\|\ \le\ \frac{4}{c_H}e^{-\nu(c_H,\beta)\,|x-y|_1}.
\tag{3.3}
\]

### Proof sketch (the decisive step only)

Let \(q_\mu(k)=e^{ik_\mu}-1\) and
\[
\lambda(k)=\sum_{\mu=1}^d|q_\mu(k)|^2
=
4\sum_{\mu=1}^d\sin^2(k_\mu/2).
\]
The Fourier symbol of the Maxwell operator on 1-forms is
\[
\widehat{(d_1^*d_1X)}(k)
=
\big(\lambda(k)I-q(k)\otimes\overline{q(k)}\big)\widehat X(k).
\]
The horizontal constraint \(d_0^*X=0\) becomes \(\overline{q(k)}\cdot \widehat X(k)=0\), which implies \((q\otimes\overline q)\widehat X=0\). Therefore **on \(\ker d_0^*\)**:
\[
\widehat{(d_1^*d_1X)}(k)=\lambda(k)\widehat X(k).
\]
Hence the multiplier for \(M\) on the horizontal subspace is scalar:
\[
\widehat{(MX)}(k)=(m^2+t\lambda(k))\widehat X(k),
\qquad
\widehat{(GX)}(k)=\frac{1}{m^2+t\lambda(k)}\widehat X(k).
\]
One then writes the kernel as a Fourier integral and performs a complex contour shift \(k\mapsto k+i\nu s\) aligned with the sign of \(x-y\), choosing \(\nu\) so that
\[
\Re(m^2+t\lambda(k+i\nu s))\ge m^2/2,
\]
which is exactly solved by (3.1). The shift produces the factor \(e^{-\nu|x-y|_1}\) and the denominator bound yields the prefactor \(2/m^2\). \(\square\)

---

## 4. Why this matters: a concrete mass scale in lattice units

The exponent \(\nu(c_H,\beta)\) is a lattice-unit decay rate extracted from the inverse operator controlling covariances. It is an explicit “mass” in the sense of exponential clustering:
\[
\mathrm{Cov}(F,G)\ \lesssim\ e^{-\nu\,\mathrm{dist}(\mathrm{supp}F,\mathrm{supp}G)}.
\]

As \(\beta\to\infty\),
\[
\nu(c_H,\beta)\sim \frac{\sqrt{3}\sqrt{c_H}}{2\sqrt{\beta}\sqrt{d}},
\]
so the lattice-unit mass behaves like \(\beta^{-1/2}\) in this simplified operator model.

Whether this produces a *finite continuum* mass scale requires a separate continuum-limit argument that tracks the \(a\)-dependence of \(c_H\) and \(\beta(a)\) along the scaling trajectory.

