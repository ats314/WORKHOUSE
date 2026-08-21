# Exponential decay of the massive Maxwell inverse kernel (Combes–Thomas and Davies)

\begin{center}
\textbf{Extracted from deterministic inverse-decay appendices: Combes–Thomas conjugation and Davies semigroup conjugation.}
\end{center}

## 1. The operator whose inverse we need

Work on the Hilbert space of \(\mathfrak g\)-valued 1-cochains,
\[
\mathcal C^1(\Lambda_L;\mathfrak g)\cong \ell^2\big(E(\Lambda_L);\mathfrak g\big)
\]
with the link-graph distance \(\mathrm{dist}_E\) (links are adjacent if they share a plaquette).

Define the discrete Maxwell operator
\[
\mathsf M_1 := d_1^*d_1,
\]
and the **massive Maxwell operator**
\[
\boxed{\quad M_{\Lambda_L} := m_H^2 I + \alpha_W\,\mathsf M_1,\qquad \alpha_W:=\beta/n.\quad}
\]
The positive “mass” term \(m_H^2\) is the curvature contribution coming from Haar/Jacobian geometry in exponential coordinates.

The target object is the inverse kernel blocks
\(
(M_{\Lambda_L}^{-1})_{bb'}\in\mathrm{End}(\mathfrak g)
\),
which feed directly into covariance bounds via the Helffer–Sjöstrand representation.

---

## 2. What “finite range” means here

Because \(\mathsf M_1=d_1^*d_1\) couples only links that share a plaquette, it has **range one** in the link graph:
\[
(\mathsf M_1)_{b\tilde b}=0\qquad\text{if }\mathrm{dist}_E(b,\tilde b)>1.
\]
Hence \(M_{\Lambda_L}\) also has range one.

To state quantitative decay, it is convenient to use row-sum constants such as
\[
C_0(\mathsf M_1):=\sup_b\sum_{\tilde b\neq b}\|(\mathsf M_1)_{b\tilde b}\|_{\mathrm{op}},
\]
and the “boundary row-sum” constant
\(C_\partial(\mathsf M_1)\), which only counts neighbors that increase/decrease distance to a fixed base link by exactly 1.

---

## 3. Combes–Thomas: one-shot resolvent decay

For a uniformly positive, self-adjoint, finite-range operator \(A\) on a finite graph,
Combes–Thomas conjugation yields a generic bound of the form
\[
\|(A^{-1})_{xy}\|_{\mathrm{op}}\le \frac{2}{a_0(A)}\,\exp\big(-\eta_{\mathrm{CT}}(A)\,\mathrm{dist}(x,y)\big),
\]
where
\(a_0(A)\) is the positivity constant (largest \(a_0>0\) with \(A\succeq a_0 I\)),
\(R(A)\) its range, and \(B_0(A)\) an off-diagonal row-sum; the decay rate is
\[
\boxed{\quad \eta_{\mathrm{CT}}(A) := \frac{1}{R(A)}\log\Big(1+\frac{a_0(A)}{2B_0(A)}\Big).\quad}
\]

Specializing to \(M_{\Lambda_L}\):
- \(a_0(M_{\Lambda_L})\ge m_H^2\) because \(\mathsf M_1\succeq 0\);
- \(R(M_{\Lambda_L})=1\);
- \(B_0(M_{\Lambda_L})\le \alpha_W C_0(\mathsf M_1)\).

So a clean “plug-in” decay rate is
\[
\eta_{\mathrm{CT}}(M_{\Lambda_L})\ \ge\ \log\Big(1+\frac{m_H^2}{2\alpha_W C_0(\mathsf M_1)}\Big).
\]
This is already enough to produce exponential clustering once inserted into the matrix Brascamp–Lieb hinge.

---

## 4. Davies method: semigroup conjugation (often sharper)

A different route starts from the Laplace-transform identity (finite-dimensional, self-adjoint \(L\ge 0\)):
\[
(m^2I+L)^{-1} = \int_0^\infty e^{-m^2 t}e^{-tL}\,dt.
\]
Let \(L:=\alpha_W\mathsf M_1\), so \(M_{\Lambda_L}=m_H^2I+L\).

Pick a base link \(b'\) and define the 1-Lipschitz weight
\[
\phi_{b'}(b):=\mathrm{dist}_E(b,b'),
\]
and the diagonal “Davies weight” operator
\[
(W_{\lambda,b'}X)_b := e^{\lambda\phi_{b'}(b)}X_b.
\]
Conjugating the semigroup gives
\(
W e^{-tL}W^{-1} = e^{-tL_{\lambda,b'}}
\)
for the similarity transform \(L_{\lambda,b'}:=WLW^{-1}\).

The key estimate is a bound on
\(
\|e^{-tL_{\lambda,b'}}\|_{\mathrm{op}}
\)
via a symmetric perturbation created by the conjugation. For range-one operators, one gets
\[
\|e^{-tL_{\lambda,b'}}\|_{\mathrm{op}}
\le
\exp\Big(t\,\alpha_W C_\partial(\mathsf M_1)(\cosh\lambda-1)\Big).
\]
Inserting this into the Laplace transform and undoing the conjugation yields:

\paragraph{Davies inverse-kernel bound.}
If
\(
\alpha_W C_\partial(\mathsf M_1)(\cosh\lambda-1) < m_H^2
\), then for all links \(b,b'\),
\[
\boxed{\quad
\|(M_{\Lambda_L}^{-1})_{bb'}\|_{\mathrm{op}}
\le
\frac{1}{m_H^2-\alpha_W C_\partial(\mathsf M_1)(\cosh\lambda-1)}\,e^{-\lambda\mathrm{dist}_E(b,b')}.
\quad}
\]

A convenient “canonical” choice is to set the denominator to \(m_H^2/2\), i.e.
\[
\alpha_W C_\partial(\mathsf M_1)(\cosh\lambda-1)=\frac{m_H^2}{2}
\quad\Rightarrow\quad
\boxed{\ \lambda = \operatorname{arcosh}\Big(1+\frac{m_H^2}{2\alpha_W C_\partial(\mathsf M_1)}\Big).\ }
\]
Then
\[
\|(M_{\Lambda_L}^{-1})_{bb'}\|_{\mathrm{op}}\le \frac{2}{m_H^2}\,e^{-\lambda\mathrm{dist}_E(b,b')}.
\]

---

## 5. Why two methods?

- **Combes–Thomas** is algebraic and very general; it packages everything into \(a_0,B_0,R\).
- **Davies** can be sharper for Laplacian-type operators because it exploits semigroup structure and can use the boundary constant \(C_\partial\) rather than the cruder \(C_0\).

Either way, once you have a clean exponential kernel bound for \(M^{-1}\), you can feed it into the Helffer–Sjöstrand / matrix BL pipeline to turn local curvature lower bounds into global exponential clustering.
