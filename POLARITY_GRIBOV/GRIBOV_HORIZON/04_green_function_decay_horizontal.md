# Green’s function decay on the horizontal sector: \((m^2 I + t\,d_1^\ast d_1)^{-1}\)

This is the cleanest “analytic hinge” lemma downstream of the matrix covariance bound:

> On the horizontal (divergence-free) sector \(\ker d_0^\ast\), the Maxwell symbol becomes **scalar**, so the inverse of
> \[
> M := m^2 I + t\,d_1^\ast d_1
> \]
> has an explicit exponential off-diagonal bound.

The proof is a direct Fourier multiplier computation + a safe contour shift.

---

## 1. Infinite-lattice setup (no harmonic 1-forms)

Work on \(\mathbb Z^d\), \(d\ge 2\). Let \(E(\mathbb Z^d)=\{(x,\mu):x\in\mathbb Z^d,\ \mu\in\{1,\dots,d\}\}\) be oriented nearest-neighbor edges.

Let \(\ell^2\mathcal C^1 := \ell^2(E(\mathbb Z^d);\mathfrak g)\), with \(\mathfrak g\) a finite-dimensional inner-product space (e.g. a compact Lie algebra, but the estimate is componentwise).

Define \(d_0\) and \(d_0^\ast\) by
\[
(d_0\phi)_{x,\mu} := \phi_{x+\hat e_\mu}-\phi_x,\qquad
(d_0^\ast X)_x := \sum_{\mu=1}^d (X_{x-\hat e_\mu,\mu}-X_{x,\mu}).
\]
Define \(d_1:\mathcal C^1\to\mathcal C^2\) on an oriented plaquette \((x;\mu,\nu)\) by
\[
(d_1X)_{x;\mu,\nu} := X_{x,\mu}+X_{x+\hat e_\mu,\nu}-X_{x+\hat e_\nu,\mu}-X_{x,\nu}.
\]

Define the horizontal sector
\[
H := \ker(d_0^\ast)\subset \ell^2\mathcal C^1.
\]

Fix parameters \(m^2>0\), \(t>0\), and define
\[
M := m^2 I + t\,d_1^\ast d_1
\quad\text{as an operator on }H.
\]

Since \(d_1^\ast d_1\succeq 0\), one has \(M\succeq m^2 I\) and thus \(M\) is invertible on \(H\). Let \(G:=M^{-1}\).

We measure separation of edges by basepoint \(\ell^1\) distance:
\[
\mathrm{dist}_1\big((x,\mu),(y,\nu)\big) := |x-y|_1 := \sum_{j=1}^d |x_j-y_j|.
\]

---

## 2. Fourier diagonalization and the “symbol becomes scalar” fact

Let \(\mathbb T^d=[-\pi,\pi]^d\). For \(X\in\ell^2\mathcal C^1\), define
\[
\widehat X_\mu(k) := \sum_{x\in\mathbb Z^d} e^{-ik\cdot x} X_{x,\mu}.
\]

Define
\[
\lambda(k):=4\sum_{\mu=1}^d \sin^2\!\Big(\frac{k_\mu}{2}\Big).
\tag{2.1}
\]

A standard computation gives:

- Horizontal constraint in Fourier space:
  \[
  \overline q(k)\cdot \widehat X(k)=0,\qquad q_\mu(k):=e^{ik_\mu}-1.
  \tag{2.2}
  \]
- Maxwell symbol:
  \[
  \widehat{(d_1^\ast d_1 X)}(k) = \lambda(k)\,P_\perp(k)\,\widehat X(k),
  \tag{2.3}
  \]
  where \(P_\perp(k)\) is the orthogonal projection onto the transverse subspace \(\{\eta:\overline q(k)\cdot \eta=0\}\subset\mathbb C^d\).

### Lemma 2.1 (Scalarization on the horizontal sector)
If \(X\in H\) (i.e. \(\overline q\cdot \widehat X=0\)), then
\[
\widehat{(d_1^\ast d_1 X)}(k)=\lambda(k)\,\widehat X(k).
\tag{2.4}
\]

**Proof.**
If \(\overline q\cdot \widehat X=0\) then \(P_\perp(k)\widehat X=\widehat X\). Insert into (2.3). \(\square\)

So on \(H\),
\[
\widehat{(MX)}(k) = (m^2+t\lambda(k))\,\widehat X(k),
\qquad
\widehat{(GX)}(k) = \frac{1}{m^2+t\lambda(k)}\,\widehat X(k).
\tag{2.5}
\]

---

## 3. Statement: explicit exponential decay bound

### Lemma 3.1 (Exponential decay of \(M^{-1}\) on \(H=\ker d_0^\ast\))
Let \(d\ge2\), \(m^2>0\), \(t>0\). Define
\[
\nu(m^2,t) := 2\,\mathrm{arsinh}\!\Big(\frac{\sqrt{m^2}}{\sqrt{8td}}\Big).
\tag{3.1}
\]
Then the operator kernel of \(G=M^{-1}\) in the edge basis satisfies: for all edges \(\ell=(x,\mu)\), \(\ell'=(y,\nu)\),
\[
\big\|G_{\ell,\ell'}\big\|_{\mathrm{op}(\mathfrak g)}
\ \le\
\frac{2}{m^2}\,e^{-\nu(m^2,t)\,|x-y|_1}.
\tag{3.2}
\]

---

## 4. Proof (Fourier representation + safe contour shift)

### Step 1: Kernel representation
By (2.5), the kernel has the Fourier integral form
\[
G_{(x,\mu),(y,\nu)}
=
\int_{\mathbb T^d} e^{ik\cdot(x-y)}\,
\frac{(P_\perp(k))_{\mu\nu}}{m^2+t\lambda(k)}\,
\frac{dk}{(2\pi)^d}
\;\otimes\;
\mathrm{Id}_{\mathfrak g}.
\tag{4.1}
\]
Since \(\|P_\perp(k)\|\le 1\), it suffices to bound the scalar integral.

### Step 2: A uniform lower bound for the shifted denominator
Let \(z:=x-y\in\mathbb Z^d\). Choose a sign vector \(s\in\{-1,0,+1\}^d\) with \(s_j=\mathrm{sign}(z_j)\).

Fix \(\nu>0\) (chosen below) and consider the shift \(k\mapsto k+i\nu s\). Write \(\lambda(k)=4\sum_\mu \sin^2(k_\mu/2)\), which is entire in each coordinate.

For real \(\theta\) and real \(b\),
\[
\sin\Big(\frac{\theta+ib}{2}\Big)
=
\sin(\theta/2)\cosh(b/2) + i\cos(\theta/2)\sinh(b/2).
\]
Squaring and taking real parts yields the inequality
\[
\mathrm{Re}\,\sin^2\Big(\frac{\theta+ib}{2}\Big)\ \ge\ -\sinh^2(b/2).
\tag{4.2}
\]
Therefore, summing over coordinates,
\[
\mathrm{Re}\,\lambda(k+i\nu s)
\ \ge\
-4d\,\sinh^2(\nu/2).
\tag{4.3}
\]
Hence
\[
\mathrm{Re}\,\big(m^2+t\lambda(k+i\nu s)\big)
\ \ge\
m^2 - 4td\,\sinh^2(\nu/2).
\tag{4.4}
\]

Choose \(\nu\) so that
\[
4td\,\sinh^2(\nu/2)=\frac{m^2}{2}.
\tag{4.5}
\]
Then (4.4) implies
\[
\mathrm{Re}\,\big(m^2+t\lambda(k+i\nu s)\big)\ \ge\ \frac{m^2}{2},
\]
and thus \(|m^2+t\lambda(k+i\nu s)|\ge m^2/2\).

Solving (4.5) gives exactly \(\nu\) in (3.1).

### Step 3: Contour shift and exponential factor
By analyticity and \(2\pi\)-periodicity in each real coordinate, the rectangular contour shift from \(\mathrm{Im}\,k=0\) to \(\mathrm{Im}\,k=\nu s\) yields
\[
G_{(x,\mu),(y,\nu)}
=
\int_{\mathbb T^d} e^{i(k+i\nu s)\cdot z}
\frac{(P_\perp(k+i\nu s))_{\mu\nu}}{m^2+t\lambda(k+i\nu s)}
\frac{dk}{(2\pi)^d}
\otimes \mathrm{Id}_{\mathfrak g}.
\tag{4.6}
\]
But \(e^{i(k+i\nu s)\cdot z}=e^{ik\cdot z}e^{-\nu s\cdot z}=e^{ik\cdot z}e^{-\nu|z|_1}\). Therefore
\[
\|G_{(x,\mu),(y,\nu)}\|
\le
e^{-\nu|z|_1}\int_{\mathbb T^d}\frac{\|P_\perp\|}{|m^2+t\lambda|}\frac{dk}{(2\pi)^d}
\le
e^{-\nu|z|_1}\int_{\mathbb T^d}\frac{2}{m^2}\frac{dk}{(2\pi)^d}
=\frac{2}{m^2}e^{-\nu|z|_1}.
\]
This is (3.2). \(\square\)

---

## 5. Remarks for finite periodic volume

On a finite periodic torus there are genuine harmonic 1-forms, so the inverse kernel contains a small non-decaying (but volume-suppressed) harmonic contribution. For covariance bounds involving *local gradients*, this shows up as an additive \(O(|\Lambda|^{-1})\) term and vanishes in the thermodynamic limit.

On \(\mathbb Z^d\) (the present setting) there are no \(\ell^2\) harmonic 1-forms, so the pure exponential bound is clean.

---
