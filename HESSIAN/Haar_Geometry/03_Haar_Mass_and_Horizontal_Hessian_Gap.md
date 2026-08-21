# Haar Measure Mass Term and Horizontal Hessian Gap on \(SU(N)^{|\mathcal{B}|}\)  
*Finite-cutoff analytic kernel (clean derivation + robust statements)*

This note isolates a finite-dimensional computation that repeatedly appears as a “seed” in the project: **the Haar measure induces an explicit quadratic term** in exponential coordinates, producing **uniform convexity at finite cutoff**.

It also clarifies what is *coordinate/normalization dependent* and what is *invariantly true*.

---

## 1. Exponential coordinates and Haar Jacobian

Let \(G\) be a compact Lie group with Lie algebra \(\mathfrak{g}\). For \(A\in\mathfrak{g}\) near \(0\),
\[
U = \exp(A).
\]

The differential of the exponential map is
\[
(d\exp)_A
= L_{\exp(A)}\circ
\frac{1-e^{-\operatorname{ad}_A}}{\operatorname{ad}_A}.
\]

With respect to a bi-invariant Riemannian metric on \(G\) and Lebesgue measure on \(\mathfrak{g}\), the Jacobian of \(\exp\) is
\[
J(A)
=\det_{\mathfrak{g}}\!\left(
\frac{\sinh(\tfrac12\operatorname{ad}_A)}
     {\tfrac12\operatorname{ad}_A}
\right).
\]

Define the **Haar measure action**
\[
S_{\mathrm{Haar}}(A):=-\log J(A).
\]

---

## 2. Universal small-field expansion

Using \(\log(\sinh x/x)=x^2/6+O(x^4)\), with \(X=\tfrac12\operatorname{ad}_A\),
\[
S_{\mathrm{Haar}}(A)
= -\mathrm{Tr}_{\mathrm{ad}}\!\left(\frac{X^2}{6}\right) + O(\|X\|^4)
= \frac{1}{24}\,\mathrm{Tr}_{\mathrm{ad}}(\operatorname{ad}_A^2) + O(\|A\|^4).
\]

For compact semisimple \(\mathfrak{g}\), with the inner product \(\langle\cdot,\cdot\rangle\) induced by \(-\)Killing form,
\[
\mathrm{Tr}_{\mathrm{ad}}(\operatorname{ad}_A^2) = -C_2(\mathrm{ad})\,\|A\|^2,
\]
so
\[
S_{\mathrm{Haar}}(A) = c_0\,\|A\|^2 + O(\|A\|^4),
\qquad c_0:=\frac{C_2(\mathrm{ad})}{24}>0.
\]

**Invariant takeaway:** the quadratic term is **strictly positive** in the \(-\)Killing norm, regardless of conventions.

---

## 3. Lattice scaling and the “Haar mass”

On the lattice, near the identity one writes (physics convention)
\[
U_b = \exp(iagA_b),\qquad A_b\in\mathfrak{su}(N).
\]

Plugging \(A\mapsto iagA\) into the expansion yields
\[
S_{\mathrm{Haar}}(A_b)
= c_0\,a^2g^2\,\|A_b\|^2 + O(a^4\|A_b\|^4).
\]

Summing over bonds gives the quadratic “Haar mass” seed:
\[
S_{\mathrm{Haar,tot}}(A)
= c_0\,a^2g^2 \sum_{b\in\mathcal{B}}\|A_b\|^2
+ \text{higher-order}.
\]

---

## 4. Horizontal Hessian gap: robust finite-cutoff statement

Let the effective action be
\[
S_{\mathrm{eff}}(U)=\beta S_W(U) + S_{\mathrm{Haar}}(U),
\]
viewed as a smooth function on
\(\mathcal{C}_\Lambda = SU(N)^{|\mathcal{B}|}\).

At each \(U\), decompose tangent space into vertical (gauge) and horizontal directions:
\[
T_U\mathcal{C}_\Lambda = V_U \oplus H_U.
\]

Let \(\mathrm{Hess}^\perp S_{\mathrm{eff}}(U)\) denote the Hessian restricted to \(H_U\), and \(\lambda_{\min}(U)\) its smallest eigenvalue.

### Proposition (finite-cutoff lower bound under bounded interaction)

Suppose on horizontal directions the Wilson Hessian satisfies a uniform bound
\[
\mathrm{Hess}^\perp(\beta S_W)(U)\;\ge\;-C_W\,I
\quad\text{for all }U \text{ in the irreducible sector}.
\]
Then the Haar quadratic term implies
\[
\mathrm{Hess}^\perp S_{\mathrm{eff}}(U)
\;\ge\;
(c_0 a^2 g^2 - C_W)\,I.
\]
In particular, if \(c_0 a^2 g^2 > C_W\), then
\[
\lambda_{\min}(U)\ge c_0 a^2 g^2 - C_W \;>\;0
\]
uniformly in volume.

**Comment.** The constant \(C_W\) is the real analytic obstacle: it packages all “interaction curvature” terms in the Wilson action. On a finite lattice this is bounded; the question is how it behaves along the renormalization trajectory.

---

## 5. What is truly nontrivial here?

None of the Lie-theoretic Jacobian formulas are new by themselves. The potentially new ingredient is the *way they are used*:

- Haar convexity provides an explicit, local, cutoff-generated “mass-like” seed.  
- Together with horizontality + polarity of reducibles, it becomes a global curvature lower bound for the physical Dirichlet form.  
- This curvature lower bound is then fed into a Riccati / multiscale stability mechanism.

That combination is the conceptual novelty.

