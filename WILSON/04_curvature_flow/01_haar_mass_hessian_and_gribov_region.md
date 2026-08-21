# Haar-Jacobian “geometric mass” and horizontal convexity (finite cutoff)

## The core idea

On a lattice, link variables live on a *compact* Lie group, e.g. \(SU(N)\).  
If you use exponential coordinates near the identity,
\[
U_b=\exp(iag\,A_b),\qquad A_b\in\mathfrak{su}(N),
\]
then the *Haar measure* is not flat in \(A_b\)-coordinates. The Jacobian of the exponential map produces a local “Haar action”
\[
S_{\mathrm{Haar}}(A):=-\log J(A),
\]
which contributes a **strictly positive quadratic form** in the small-field regime. In plain language: the *geometry* of \(SU(N)\) behaves like a built-in convexifier.

This is one of the most interesting ingredients in the project because it turns “measure theory + geometry” into an explicit lower bound on the Hessian of the effective action, which then feeds directly into spectral-gap machinery.

---

## 1. Haar Jacobian in exponential coordinates

A standard formula for the Jacobian density of the exponential map on a compact Lie group gives
\[
J(A)\;=\;\det_{\mathfrak g}\!\left(
\frac{\sinh\!\left(\tfrac{\mathrm{ad}_{iagA}}{2}\right)}{\tfrac{\mathrm{ad}_{iagA}}{2}}
\right),
\]
where \(\mathrm{ad}_X(Y)=[X,Y]\) and the determinant is taken on \(\mathfrak g=\mathfrak{su}(N)\).

Define the operator
\[
Y:=\frac{1}{2}\,\mathrm{ad}_{iagA}\quad\Longrightarrow\quad
J(A)=\det_{\mathfrak g}\!\left(\frac{\sinh Y}{Y}\right).
\]

Then
\[
S_{\mathrm{Haar}}(A)
=-\log J(A)
=-\mathrm{Tr}_{\mathfrak g}\log\!\left(\frac{\sinh Y}{Y}\right).
\]

---

## 2. Small-field expansion and the quadratic term

Use the scalar Taylor series at \(0\):
\[
\log\!\left(\frac{\sinh x}{x}\right) = \frac{x^2}{6} + O(x^4).
\]
By holomorphic functional calculus this extends to the operator \(Y\):
\[
\log\!\left(\frac{\sinh Y}{Y}\right) = \frac{Y^2}{6} + O(\|Y\|^4).
\]
Therefore
\[
S_{\mathrm{Haar}}(A)
= -\frac{1}{6}\,\mathrm{Tr}_{\mathfrak g}(Y^2)+O(\|Y\|^4).
\]

Since \(Y=\frac{1}{2}\mathrm{ad}_{iagA}\), we have \(Y^2=-\frac{a^2g^2}{4}\,\mathrm{ad}_A^2\). So
\[
-\mathrm{Tr}_{\mathfrak g}(Y^2)
=\frac{a^2g^2}{4}\,\mathrm{Tr}_{\mathfrak g}(\mathrm{ad}_A^2).
\]

A key algebraic input is the adjoint/fundamental trace proportionality:
\[
\mathrm{Tr}_{\mathfrak g}(\mathrm{ad}_A^2)=K_N\,\mathrm{Tr}(A^2),
\qquad K_N>0,
\]
with \(K_N\) depending only on \(N\) and normalization conventions (the project notes indicate the commonly used \(K_N=2N\) under a standard choice).

Putting this together:
\[
S_{\mathrm{Haar}}(A)
= \frac{c_0}{2}\,a^2g^2\,\|A\|^2 + O(a^4g^4\|A\|^4),
\]
for a constant \(c_0>0\) depending only on \(SU(N)\) (and trace normalization).  
Different sections quote different explicit forms for \(c_0\); the physically relevant thing is **strict positivity** and correct scaling in \(a,g\).

---

## 3. Hessian lower bound (local)

Differentiate twice at \(A=0\). The quartic remainder vanishes at the origin, and one gets the *local* Hessian:
\[
\mathrm{Hess}\,S_{\mathrm{Haar}}(0)\;=\;c_0\,a^2g^2\,I.
\]

Hence: there exists a normal neighborhood \(\|A\|\le r\) in which
\[
\mathrm{Hess}\,S_{\mathrm{Haar}}(A)\succeq c_0\,a^2g^2\,I
\quad\text{(as a quadratic form).}
\]

This is the “geometric bare mass” phenomenon: the Haar measure penalizes small fluctuations like a massive Gaussian.

---

## 4. Combine with the Wilson term: horizontal convexity and a Gribov-type region

Write the effective action (in exponential coordinates) schematically as
\[
S_{\mathrm{eff}}(U)=\beta S_W(U) + S_{\mathrm{Haar}}(U).
\]

The Wilson term is smooth but not globally convex; the project bounds its negative curvature contribution:
\[
\mathrm{Hess}\,(\beta S_W)\;\succeq\;-\,\beta C_V\,I
\]
when restricted to the **horizontal** subspace \(V_H\) (orthogonal complement to gauge orbits in the tangent space).

Therefore, on \(V_H\),
\[
\mathrm{Hess}\,S_{\mathrm{eff}}\;\succeq\;
\bigl(c_0 a^2g^2-\beta C_V\bigr)\,I
=: \rho_*(a,g,\beta)\,I.
\]

If \(\rho_*>0\), you get strict convexity on horizontals and a clean “Gribov region” picture:
\[
\Omega_G=\{U:\lambda_{\min}(U)>0\},\qquad
\partial\Omega_G=\{U:\lambda_{\min}(U)=0\},
\]
where \(\lambda_{\min}\) is the smallest eigenvalue of the horizontal Hessian.

---

## 5. Why this is promising (and where it bites you)

### The good
- It provides a *volume-independent* lower bound (a big deal in infinite-volume limits).
- It converts the non-abelian group geometry into a quantitative convexity constant \(\rho_*\).
- Once you have \(\rho_*\), Bakry–Émery machinery immediately produces spectral gaps.

### The bite
As \(a\to 0\) in an asymptotically free theory, bare \(g_0^2(a)\to 0\).  
Then \(c_0a^2g_0^2(a)\to 0\), so the Haar mass term *vanishes* in the continuum limit. This forces the bigger question:

> What mechanism preserves a mass gap when the explicit finite-cutoff convexifier disappears?

That is exactly what the project’s “RG stability / Riccati flow / MFIP recursion” pieces are trying to attack.