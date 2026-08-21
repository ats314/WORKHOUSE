# Combes–Thomas Inverse-Decay Lemma for Finite-Range Operators (Extract)

## Why this module matters
This is one of the project’s most reusable “drop-in” lemmas: it upgrades a **spectral gap + finite-range locality** into **exponential decay of the inverse kernel**.  

In the mass-gap program it is the step:
\[
\text{(massive Maxwell / 1-form operator)}^{-1}
\quad\Rightarrow\quad
\text{exponential clustering of covariances}.
\]
But the lemma itself is completely abstract and can be used in any lattice system with a banded positive operator.

---

## 1. Setting

Let \((\mathcal{X},d)\) be a countable metric space (e.g. edges of a lattice) and let \(\mathcal{H}=\ell^2(\mathcal{X})\otimes \mathbb{C}^m\) (finite internal dimension \(m\)).

Let \(M\) be a bounded self-adjoint operator on \(\mathcal{H}\) with integral kernel \(M(x,y)\in\mathbb{C}^{m\times m}\).

Assume:

1. **Finite range \(R\):** \(M(x,y)=0\) whenever \(d(x,y) > R\).

2. **Spectral gap \(c>0\):** \(M \ge c\,I\) (as a quadratic form).

3. **Uniform row bound:** \(\sup_x\sum_{y}\|M(x,y)\| < \infty\).

(For a finite-range lattice operator, (3) is automatic from bounded degree.)

---

## 2. Conclusion (exponential inverse decay)

### Theorem (Combes–Thomas type bound)
There exist constants \(C,\alpha>0\) depending only on \(c\), \(R\), and the uniform row bound, such that the inverse kernel satisfies
\[
\boxed{
\|M^{-1}(x,y)\|\ \le\ C\,e^{-\alpha\, d(x,y)} \qquad \forall x,y\in\mathcal{X}.
}
\]

---

## 3. Proof sketch (conjugation / resolvent trick)

Fix a “weight function” \(\phi:\mathcal{X}\to\mathbb{R}\) that is 1-Lipschitz:
\[
|\phi(x)-\phi(y)| \le d(x,y).
\]
For \(t\in\mathbb{R}\), define a diagonal multiplication operator \((W_t f)(x)=e^{t\phi(x)}f(x)\).

Consider the conjugated operator
\[
M_t := W_t\, M\, W_t^{-1}.
\]
Its kernel is
\[
M_t(x,y)= e^{t(\phi(x)-\phi(y))}\,M(x,y).
\]
Because \(M\) has range \(R\), we have \(|\phi(x)-\phi(y)|\le R\) whenever \(M(x,y)\neq 0\), hence
\[
\|M_t(x,y)\|\le e^{|t|R}\,\|M(x,y)\|.
\]

Now decompose \(M_t = M + (M_t-M)\). One shows:
- \(M_t-M\) is bounded with \(\|M_t-M\| \le C_1 |t|\) for \(|t|\) small, using the finite-range bound and the mean value theorem on \(e^{t(\phi(x)-\phi(y))}\).
- Therefore, for \(|t|\le t_0\) small enough, \(M_t\) remains invertible with a uniform bound \(\|M_t^{-1}\|\le 2/c\).

Finally, the inverse kernel identity
\[
M_t^{-1} = W_t\, M^{-1}\, W_t^{-1}
\]
implies
\[
M^{-1}(x,y) = e^{-t(\phi(x)-\phi(y))}\,M_t^{-1}(x,y).
\]
Taking norms, bounding \(\|M_t^{-1}(x,y)\|\le \|M_t^{-1}\|\), and optimizing over a choice of \(\phi\) with \(\phi(x)-\phi(y)=d(x,y)\) (take \(\phi(z)=d(z,y)\), clipped if needed), yields
\[
\|M^{-1}(x,y)\|\ \le\ \frac{2}{c}\,e^{-t\,d(x,y)}.
\]
Choose \(t=t_0\) to obtain the stated exponential decay with \(\alpha=t_0\).

\(\square\)

---

## 4. How it plugs into the gauge theory pipeline
In the project, \(M\) is the **massive Maxwell / 1-form operator** on the horizontal subspace, of the form
\[
M = c_H I + d_1^\* d_1,
\]
or a small quasi-local perturbation thereof.

- The hinge analysis provides \(c_H>0\).
- The lattice differential \(d_1\) has finite range.
- Therefore \(M^{-1}\) has exponential off-diagonal decay.
- Inserting \(M^{-1}\) into Helffer–Sjöstrand covariance representations gives exponential clustering.

This lemma is “boring” in the best possible way: it is robust, reusable, and it turns geometry + locality into quantitative decay.

