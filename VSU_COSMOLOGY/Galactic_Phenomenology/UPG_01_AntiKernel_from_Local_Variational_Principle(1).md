# Anti-kernel as a local variational principle (Hankel channel)

## 0. Goal

In the SPARC Hankel pipeline, the **anti-kernel** is the multiplicative rule
\[
\widehat g_{\mu}(k) = M_{\rm anti}(k)\,\widehat g_b(k),
\qquad
M_{\rm anti}(k)=1+\frac{\mu^2}{k^2}.
\]

This note shows a concrete sense in which that multiplier is *inevitable* once you demand:

- locality in real space (no arbitrary nonlocal kernel inserted by hand),
- a single new inverse-length scale \(\mu\),
- and an axisymmetric (Hankel) diagonalization of the relevant radial operator.

The punchline: \(1+\mu^2/k^2\) is the **spectral symbol** of a local, second‑order radial operator inverse.

---

## 1. Hankel‑1 transform conventions (axisymmetric)

For a radial function \(f(r)\) in the disk plane, define the order‑1 Hankel pair
\[
\widehat f(k)=\int_0^\infty dr\, r\, f(r)\,J_1(kr),
\qquad
f(r)=\int_0^\infty dk\, k\,\widehat f(k)\,J_1(kr).
\]

This is exactly the transform pair implemented in the SPARC Hankel scripts.

---

## 2. The operator that Hankel‑1 diagonalizes

Define the order‑1 Bessel radial operator
\[
\mathcal L_1[f](r)
\;\equiv\;
-\left(f''(r)+\frac{1}{r}f'(r)-\frac{1}{r^2}f(r)\right).
\]

A standard Bessel identity gives:
\[
\widehat{\,\mathcal L_1 f\,}(k)=k^2 \widehat f(k)
\]
for sufficiently nice \(f\) (decay and regularity so boundary terms vanish).

So in the Hankel‑1 channel, \(\mathcal L_1\) is literally “multiply by \(k^2\)”.

---

## 3. Anti-kernel as an operator identity

Starting from
\[
\widehat g_{\mu}(k)=\left(1+\frac{\mu^2}{k^2}\right)\widehat g_b(k),
\]
multiply through by \(k^2\):
\[
k^2\widehat g_{\mu}(k)=(k^2+\mu^2)\widehat g_b(k).
\]

Using \(\widehat{\mathcal L_1 f}=k^2\widehat f\), this is equivalent in real space to
\[
\mathcal L_1 g_{\mu}=(\mathcal L_1+\mu^2)\,g_b.
\]

Solving for \(g_\mu\),
\[
g_{\mu}=g_b+\mu^2\,\mathcal L_1^{-1}g_b.
\]

So the anti‑kernel is not a “mystery filter”: it is exactly the map
> **add \(\mu^2\) times the \(\mathcal L_1\)-Poisson solve of \(g_b\)**.

---

## 4. A local variational principle that generates \(\mathcal L_1^{-1}\)

Introduce an auxiliary field \(\chi(r)\) with action (disk plane, axisymmetric)
\[
S[\chi;g_b]
=
\int_0^\infty dr\,r\left[
\frac12\left(\chi'^2+\frac{1}{r^2}\chi^2\right) - g_b(r)\chi(r)
\right].
\]

Varying \(\chi\) gives the Euler–Lagrange equation
\[
\mathcal L_1\chi=g_b.
\]

Define the modified acceleration as
\[
g_\mu \equiv g_b + \mu^2 \chi.
\]

Then by construction,
\[
g_\mu = g_b + \mu^2\mathcal L_1^{-1}g_b,
\]
and therefore (by Hankel diagonalization),
\[
\widehat g_\mu(k)=\left(1+\frac{\mu^2}{k^2}\right)\widehat g_b(k).
\]

**Everything is local.** The nonlocality only appears after you integrate out \(\chi\), i.e. after you solve its local field equation.

---

## 5. Boundary conditions and the IR pole

The formal pole at \(k=0\) is the spectral signature of the inverse operator \(\mathcal L_1^{-1}\).
Any practical implementation must specify:
- finite support (\(R_{\max}\)) \(\Rightarrow\) an effective \(k_{\rm IR}\sim\pi/R_{\max}\),
- thickness/leakage regulators \(\Rightarrow\) \(k^2\to k^2+k_z^2\),
- windowing/tapering \(W(k)\) for numerical stability.

The right philosophy is:

> choose IR regularization from geometry/physics, not from “dwarf exceptions”.

(See UPG_04.)

---

## 6. What’s actually “new” here?

Not the Hankel algebra — that is classical.

The potentially novel angle is:
- treating the anti‑kernel as the **inverse of a local radial operator**,
- which makes it compatible with a constrained local action,
- and suggests a principled way to build a covariant completion (the auxiliary field becomes a genuine dynamical field in 3+1D).

That’s the bridge from “fitting kernel” \(\rightarrow\) “derivable response”.
