# Codimension + mass-gap \(\Rightarrow\) rational Hankel response

## 0. The demand

You want the Hankel-channel rule
\[
M(k)=1+\frac{\mu^2}{k^2}
\]
not as an *ansatz*, but as the **forced** spectral footprint of a local variational principle built from:

- a **codimension-2** reduction (log potential in the disk sector), and
- a **single mass-gap scale** \(\mu\) (so the theory has one new length \(\ell_\mu=1/\mu\)).

This note frames the cleanest “inevitability” route.

---

## 1. The codimension‑2 / mass‑gap kernel (WIZ 2/3 backbone)

In the WIZ 2/3 style derivation, a bulk massive field reduced onto a 2D (codim‑2) sector produces the Green function
\[
G_\mu(\mathbf{z})=\frac{1}{2\pi}K_0(\mu|\mathbf{z}|),
\]
whose small‑argument expansion is
\[
K_0(\mu R)=-\ln\!\left(\frac{\mu R}{2}\right)-\gamma_E+\mathcal O\!\big((\mu R)^2\ln(\mu R)\big).
\]

That is the precise way a **mass gap** \(\mu\) yields a **log potential** regime for \(\mu R\ll 1\).

In Fourier (2D), the same object has the canonical rational symbol
\[
\widehat G_\mu(k)=\frac{1}{k^2+\mu^2}.
\]

This is the crucial “spectral rigidity” fact:  
**local quadratic actions \(\Rightarrow\) polynomial operators \(\Rightarrow\) rational spectral response.**

---

## 2. “Inevitable” rational forms from local operators

A local second‑order operator in the disk plane has symbol \(k^2+m^2\) (up to normalization).
Therefore any mapping between two such sectors (e.g. massless vs massive, or two coupled constraints) will produce *ratios* of polynomials in \(k^2\).

If you demand only:
1. one new scale \(\mu\),
2. UV recovery \(M(k)\to 1\) as \(k\to\infty\), and
3. locality (no arbitrary function of \(k\)),

then the *only* rational option with a single pole/zero is
\[
M(k)=\frac{k^2+\mu^2}{k^2}=1+\frac{\mu^2}{k^2}.
\]

So in that very strict sense, the anti‑kernel is the unique “one‑scale, UV‑clean” ratio you can get from local second‑order operators.

---

## 3. A concrete constrained action that makes \(1+\mu^2/k^2\) appear

Here is a minimal local disk-sector construction (the “inevitability engine”):

- Let \(\psi\) be the codimension‑2 (log) response field sourced by baryons.
- Let \(\Phi\) be the “physical” potential that matter feels.

Impose the Poisson equation for \(\psi\) as a *constraint* (via a Lagrange multiplier \(\Lambda\)), and couple \(\psi\) back into the \(\Phi\) equation with strength \(\mu^2\):

\[
S[\Phi,\psi,\Lambda]
=
\int d^2x\left[
\frac{1}{8\pi G}|\nabla\Phi|^2
-\rho\,\Phi
-\frac{\mu^2}{4\pi G}\,\psi\,\Phi
+\Lambda\left(-\Delta\psi-4\pi G\rho\right)
\right].
\]

Euler–Lagrange variation gives

1) constraint (from \(\delta\Lambda\)):
\[
-\Delta\psi=4\pi G\rho,
\]

2) modified Poisson (from \(\delta\Phi\)):
\[
-\Delta\Phi=4\pi G\rho+\mu^2\psi.
\]

Eliminate \(\psi\) in Fourier:
\[
\psi(k)=\frac{4\pi G\rho(k)}{k^2},
\qquad
\Phi(k)=\frac{4\pi G\rho(k)}{k^2}\left(1+\frac{\mu^2}{k^2}\right).
\]

So the *physical* response differs from the Newtonian one by precisely the anti‑kernel multiplier \(1+\mu^2/k^2\).

This is fully local at the action level: the nonlocality appears only after integrating out \(\psi\) (a standard EFT move).

---

## 4. How this connects back to the Hankel channel

For axisymmetric disks, \(g(r)=-\partial_r\Phi(r)\) and the order‑1 Hankel transform is the right diagonal basis for the radial operator.

Because the multiplier \(M(k)\) acts on \(\Phi(k)\), it acts on \(g(k)\) as well (up to the standard factor relating \(g\) and \(\Phi\) in Hankel space).
So the disk acceleration response inherits the same rational form.

That is the “make it inevitable” story:
- codim‑2 log response gives you the \(1/k^2\),
- locality + single scale gives you the \((k^2+\mu^2)\),
- their ratio is forced.

---

## 5. What still needs doing (to be a theory, not a trick)

This disk‑sector inevitability is only step one. The real work is:

1. **predicting \(\mu\)** (or relating it to a covariant sector),
2. eliminating per‑galaxy amplitude degeneracies (UPG_03),
3. handling dwarfs by geometry/leakage (UPG_04),
4. fixing the covariant sign-domain problem so cosmology exists (UPG_05).

Once those are in place, you can meaningfully compute \(\alpha_{\rm eff}(k,a)\) rather than postulate it.
