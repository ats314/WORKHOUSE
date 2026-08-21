# From Bakry–Émery curvature to a lattice Yang–Mills spectral gap

## Why this is one of the “load-bearing” proofs

Once you have a uniform lower bound on the Hessian of an effective action, the Bakry–Émery framework turns it into:
- Poincaré inequality (variance decays),
- log-Sobolev inequality (entropy decays),
- and therefore a **uniform spectral gap** for the Langevin generator.

This is a very clean “geometry → analysis → physics” pipeline.

---

## 1. Set-up: weighted Laplacian and carré du champ

Let \((M,g)\) be a Riemannian manifold and let
\[
\mu(d x)=Z^{-1} e^{-S(x)}\,\mathrm{vol}(d x)
\]
be a Gibbs measure with smooth potential \(S\).

The overdamped Langevin generator is
\[
L f=\Delta f - \langle \nabla S,\nabla f\rangle.
\]

Define the carré du champ
\[
\Gamma(f)=\frac12\bigl(L(f^2)-2fLf\bigr)=|\nabla f|^2,
\]
and the iterated carré du champ
\[
\Gamma_2(f)=\frac12\bigl(L\Gamma(f)-2\Gamma(f,Lf)\bigr).
\]

---

## 2. Bochner identity in Bakry–Émery form

A fundamental identity (Bochner + integration-by-parts repackage) gives
\[
\Gamma_2(f)=\|\nabla^2 f\|_{\mathrm{HS}}^2
+(\mathrm{Ric}+\nabla^2 S)(\nabla f,\nabla f).
\]

So if you have a pointwise lower bound
\[
\mathrm{Ric}+\nabla^2 S \;\succeq\; \rho\, g
\quad\text{for some }\rho>0,
\]
then automatically
\[
\Gamma_2(f)\ge \rho\,\Gamma(f).
\]

This is the curvature-dimension condition \(\mathrm{CD}(\rho,\infty)\).

---

## 3. Functional inequalities and spectral gap

### Poincaré inequality
If \(\mathrm{CD}(\rho,\infty)\) holds, then for all smooth \(f\),
\[
\mathrm{Var}_\mu(f)\le \frac1{\rho}\int |\nabla f|^2\,d\mu.
\]

### Log-Sobolev inequality
Similarly,
\[
\mathrm{Ent}_\mu(f^2)\le \frac{2}{\rho}\int |\nabla f|^2\,d\mu.
\]

### Spectral gap
Let \(H=-L\) be the self-adjoint operator on \(L^2(\mu)\).  
The Poincaré inequality implies that the first nonzero eigenvalue obeys
\[
\lambda_1(H)\ge \rho.
\]
Equivalently, semigroup correlations decay at rate \(\ge \rho\).

---

## 4. Apply to lattice gauge configuration space

For lattice \(SU(N)\) gauge theory on a finite lattice \(\Lambda\), the configuration space is
\[
\mathcal{C}_\Lambda = SU(N)^{|\mathcal B|},
\]
a compact product manifold with the product bi-invariant metric.

### Ricci positivity
Each \(SU(N)\) factor has strictly positive Ricci curvature (for bi-invariant metrics), so the product satisfies
\[
\mathrm{Ric}_{\mathcal{C}_\Lambda}\succeq \kappa_0\,g
\]
with \(\kappa_0>0\) depending only on \(N\) and the chosen normalization, not on lattice volume.

### Add the effective action Hessian
If the effective action satisfies, at least on the relevant directions (often horizontals),
\[
\nabla^2 S_{\mathrm{eff}}\succeq \rho_*(a,g,\beta)\,g
\quad\text{with }\rho_*>0,
\]
then
\[
\mathrm{Ric}+\nabla^2 S_{\mathrm{eff}}
\succeq (\kappa_0+\rho_*)\,g,
\]
hence \(\mathrm{CD}(\kappa_0+\rho_*,\infty)\).

Conclusion:
\[
\lambda_1(-L_\Lambda)\ge \kappa_0+\rho_*(a,g,\beta),
\]
**uniformly in lattice volume**.

---

## 5. Physics translation

- A uniform spectral gap for the Langevin generator implies exponential relaxation/mixing in stochastic quantization.
- Via standard relations between functional inequalities and correlation decay, one interprets
  \(\sqrt{\lambda_1}\) as a *mass scale* at finite cutoff.

This is a very attractive intermediate “finite-cutoff mass gap” theorem. The heavy lift is then to argue that along a renormalization trajectory the associated physical mass scale does not collapse to \(0\) as \(a\to 0\).