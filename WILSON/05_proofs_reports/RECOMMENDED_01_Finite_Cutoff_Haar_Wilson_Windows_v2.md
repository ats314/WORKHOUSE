# Finite-Cutoff Convexity Windows from Haar vs. Wilson Curvature

This note is the “clean core” of the finite-cutoff story.
It fixes the sign/constant issues that show up in several longer drafts, and it uses a **conservative** Wilson Hessian bound that includes mixed link-derivatives.

The output is a pair of explicit strong-coupling windows:

- a **finite-cutoff uniform convexity window**, and  
- a stricter **RG-stable window** (convexity survives at least one coarse-graining step).

Both are *finite-cutoff* statements; they do **not** survive the asymptotically-free continuum limit \(a\to 0\).

---

## 1. Conventions

- Gauge group: \(G=\mathrm{SU}(N)\), Lie algebra \(\mathfrak g=\mathfrak{su}(N)\) (skew-Hermitian, traceless matrices).
- Inner product on \(\mathfrak g\):
  \[
  \langle X,Y\rangle := -\mathrm{Tr}(XY),
  \qquad 
  \|X\|^2 = -\mathrm{Tr}(X^2)\,.
  \]
- Lattice spacing \(a>0\), bare coupling \(g\), and \(\beta := \frac{2N}{g^2}\).

A link variable near the identity is parametrized by
\[
U_b = \exp(X_b), \qquad X_b = a g\, A_b,\quad A_b\in\mathfrak g.
\]

---

## 2. Haar Jacobian “mass term” in exponential coordinates

Write the Haar measure \(d\mu_H\) in exponential coordinates \(U=\exp(X)\):
\[
d\mu_H(U) = J(X)\, dX,
\qquad 
S_{\mathrm{Haar}}(X) := -\log J(X).
\]

A standard formula for compact Lie groups gives
\[
J(X)=\det_{\mathfrak g}\!\left(\frac{\sinh(\mathrm{ad}_X/2)}{\mathrm{ad}_X/2}\right),
\qquad 
\mathrm{ad}_X(Y)=[X,Y].
\]
Hence
\[
S_{\mathrm{Haar}}(X)= -\mathrm{Tr}_{\mathfrak g}\log\!\left(\frac{\sinh(\mathrm{ad}_X/2)}{\mathrm{ad}_X/2}\right).
\]

Using the expansion \(\log\!\left(\frac{\sinh z}{z}\right)=\frac{z^2}{6}+O(z^4)\), we get
\[
S_{\mathrm{Haar}}(X)= -\frac{1}{24}\mathrm{Tr}_{\mathfrak g}\big(\mathrm{ad}_X^2\big) + O(\|X\|^4).
\]

For \(\mathfrak{su}(N)\) in the above normalization,
\[
\mathrm{Tr}_{\mathfrak g}(\mathrm{ad}_X^2)= 2N\,\mathrm{Tr}(X^2).
\]
Therefore,
\[
S_{\mathrm{Haar}}(X)= -\frac{1}{24}(2N\,\mathrm{Tr}(X^2)) + O(\|X\|^4)
= \frac{N}{12}\|X\|^2 + O(\|X\|^4).
\]

So the **quadratic** Haar contribution is strictly convex:
\[
\mathrm{Hess}\,S_{\mathrm{Haar}}(0) = \frac{N}{6}\,I.
\]

On the lattice, with \(X_b = a g A_b\),
\[
S_{\mathrm{Haar}}^{(2)}(A)=\frac{N}{12}a^2 g^2\sum_b\|A_b\|^2,
\qquad 
\mathrm{Hess}\,S_{\mathrm{Haar}}^{(2)} = \underbrace{\frac{N}{6}}_{=:c_0}\,a^2 g^2\,I.
\]

We will use the shorthand constant
\[
c_0 := \frac{N}{6}.
\]

---

## 3. Conservative Wilson Hessian bound including mixed terms

The Wilson plaquette action is
\[
S_W(U)=\sum_p S_p(U_p),
\qquad 
S_p(U_p)=1-\frac{1}{N}\mathrm{Re}\,\mathrm{Tr}(U_p),
\]
where \(U_p\) is the ordered product of four link variables around plaquette \(p\).

### Lemma 3.1 one-plaquette Hessian bound
Let \(S_p(V_1,V_2,V_3,V_4)=1-\frac{1}{N}\mathrm{Re}\,\mathrm{Tr}(V_1V_2V_3V_4)\).
For the variation \(V_i(t)=e^{tX_i}V_i\) with \(X_i\in\mathfrak g\),
\[
\left|\frac{d^2}{dt^2}S_p(V_1(t),\dots,V_4(t))\Big|_{t=0}\right|
\le \frac{4}{N}\sum_{i=1}^4\|X_i\|^2.
\]

**Proof (direct expansion + Cauchy–Schwarz).**  
Differentiate \(U_p(t)=V_1(t)V_2(t)V_3(t)V_4(t)\) twice.
At \(t=0\),
\[
U_p''(0)=\sum_{i}(\cdots X_i^2V_i\cdots)\;+\;\sum_{i\neq j}(\cdots X_iV_i\cdots X_jV_j\cdots).
\]
Thus \(S_p''(0)=-(1/N)\mathrm{ReTr}(U_p''(0))\) splits into diagonal and mixed parts.

- Diagonal terms: \(|\mathrm{Tr}(\cdots X_i^2V_i\cdots)|\le \|X_i\|^2\).
- Mixed terms: \(|\mathrm{Tr}(\cdots X_iV_i\cdots X_jV_j\cdots)|\le \|X_i\|\,\|X_j\|\).

So
\[
|S_p''(0)|\le \frac{1}{N}\left(\sum_i\|X_i\|^2+\sum_{i\neq j}\|X_i\|\|X_j\|\right)
=\frac{1}{N}\left(\sum_i\|X_i\|\right)^2
\le \frac{4}{N}\sum_i\|X_i\|^2.
\]
\(\square\)

### Corollary 3.2 global bound in 4D
In \(d=4\), each link belongs to at most \(6\) plaquettes, so
\[
\big|\langle A,(\mathrm{Hess}\,S_W(U))A\rangle\big|
\le \frac{24}{N}\|A\|^2,
\qquad 
C_V(N):=\frac{24}{N}.
\]

This \(C_V(N)\) is conservative but safe: it does not rely on ignoring mixed derivatives.

---

## 4. Finite-cutoff convexity window

Consider the coordinate-form effective action
\[
S_{\mathrm{eff}} = \beta S_W + S_{\mathrm{Haar}}.
\]

Restricting to horizontal directions (mod gauge), the quadratic-form estimate becomes
\[
\langle A, \mathrm{Hess}\,S_{\mathrm{eff}}(U)A\rangle
\;\ge\;
\big(c_0 a^2 g^2 - \beta C_V(N)\big)\,\|A\|^2,
\]
with \(c_0=N/6\), \(C_V(N)=24/N\), and \(\beta=2N/g^2\).

Define
\[
\rho_*(a) := c_0 a^2 g^2 - \beta C_V(N)
= \frac{N}{6}a^2 g^2 - \frac{48}{g^2}.
\]

### Theorem 4.1 finite-cutoff convexity
If \(\rho_*(a)>0\), i.e.
\[
\frac{N}{6}a^2 g^2 > \frac{48}{g^2}
\quad\Longleftrightarrow\quad
g^4 > \frac{288}{N a^2},
\]
then \(S_{\mathrm{eff}}\) is uniformly convex (horizontally) with curvature \(\rho_*(a)\).
Consequently, the associated Langevin generator has a spectral gap \(\gtrsim \rho_*(a)\).

**Example (SU(2)).** \(g^4>144/a^2\), so \(g>\sqrt[4]{144}/\sqrt a=\sqrt{12}/\sqrt a\approx 3.46/\sqrt a\).

---

## 5. RG-stable strong-coupling subwindow

Combine the curvature bound \(\rho_*(a)\) with the block Hessian RG inequality (see **RECOMMENDED_03_Block_Convexity_Engine.md**).

If a coarse/fine split has off-diagonal Hessian operator norm bounded by \(M\), the coarse action remains convex provided \(M^2 < \rho_*(a)^2\).
A robust choice is to take
\[
M := \|\mathrm{Hess}(\beta S_W)\|_{\mathrm{op}} \le \beta C_V(N)=\frac{48}{g^2}.
\]

A sufficient (not necessary) stability condition is
\[
\rho_*(a) > M,
\]
i.e.
\[
\frac{N}{6}a^2 g^2 - \frac{48}{g^2} > \frac{48}{g^2}
\quad\Longleftrightarrow\quad
g^4 > \frac{576}{N a^2}.
\]

**Example (SU(2)).** \(g^4>288/a^2\), so \(g>\sqrt[4]{288}/\sqrt a\approx 4.12/\sqrt a\).

---

## 6. Why this cannot be the continuum mass gap

Along the asymptotically-free continuum scaling trajectory, \(g(a)\to 0\) as \(a\to 0\), hence

- the Haar quadratic scale \(\sim a^2 g(a)^2 \to 0\),
- while \(\beta(a)=2N/g(a)^2\to \infty\).

So the lower bound
\[
\rho_*(a)=\frac{N}{6}a^2 g(a)^2-\frac{48}{g(a)^2}
\]
dives to \(-\infty\): **global uniform convexity is violently incompatible with the UV limit.**

This is not a bug; it’s a diagnostic:
the Haar-vs-Wilson convexity window is a **finite-cutoff strong-coupling phenomenon**.
Anything continuum-relevant must either:

1. be **localized** (convexity holds on a high-probability core region, not globally), or
2. find a new **Spark** that generates IR convexity at a physical scale independent of the cutoff.

Both directions are developed in the rest of the recommended bundle.
