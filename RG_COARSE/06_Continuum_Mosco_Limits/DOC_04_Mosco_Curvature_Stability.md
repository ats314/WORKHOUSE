# DOC 04 — Mosco Convergence and Stability of Curvature/LSI in the Continuum Limit

## 0. Purpose

This note extracts the “analytic engine” that lets lattice inequalities survive \(a\to 0\):

- tightness \(\Rightarrow\) existence of a weak limit \(\mu\),
- Mosco convergence of lattice Dirichlet forms \(\mathcal{E}_a \to \mathcal{E}\),
- semigroup convergence \(P_t^a \to P_t\),
- stability of curvature-dimension bounds \(CD(\rho_0,\infty)\),
- hence lifting of LSI and spectral gaps.

Primary project sources:
- `02_MOSCO_STABILITY.md`
- `PROOF_10_Mosco_Convergence.md`
- `PROOF_07_UV_Log_Forest_Control.md`
- `PROOF_09_Tightness_and_Existence.md`

## 1. Lattice-to-continuum Dirichlet forms

Let \((\mathcal{X}_a,\mu_a)\) be lattice configuration spaces with measures \(\mu_a\).
For (local) observables \(F\), define the lattice Dirichlet energy
\[
\mathcal{E}_a(F,F) = \int_{\mathcal{X}_a} \|\nabla_a F\|^2\, d\mu_a.
\]

Assume the measures \(\mu_a\) are tight in a distribution space (e.g. \(H^{-s}\)) and \(\mu_a \Rightarrow \mu\).

Define the limit Dirichlet form
\[
\mathcal{E}(F,F) = \int \|\nabla F\|^2\, d\mu
\]
on a suitable core (cylindrical observables).

## 2. Mosco convergence: the two conditions

Mosco convergence \(\mathcal{E}_a \to \mathcal{E}\) consists of:

### (M1) Liminf inequality
If \(F_a \to F\) strongly in \(L^2(\mu)\) and \(\sup_a \mathcal{E}_a(F_a)<\infty\), then
\[
\mathcal{E}(F) \le \liminf_{a\to 0} \mathcal{E}_a(F_a).
\tag{Mosco-liminf}
\]

### (M2) Recovery sequence
For every \(F\in D(\mathcal{E})\) there exists \(F_a\) such that \(F_a\to F\) and
\[
\mathcal{E}_a(F_a) \to \mathcal{E}(F).
\tag{Mosco-recov}
\]

## 3. Key analytic inputs (project’s version)

### 3.1 Holonomy approximation (local observables)
For loop observables \(F\) built from holonomies, choose lattice approximants \(F_a\) using polygonal loop approximation. One needs quantitative convergence:
\[
|U_\gamma(A) - U_\gamma^{(a)}(A)| \le C a^{\alpha}\|A\|_{H^s},
\qquad \alpha=s-2>0.
\]

### 3.2 Gradient convergence
Show the discrete gradients converge to functional derivatives on cylindrical cores:
\[
\|\nabla_a F_a - \nabla F\| \to 0,
\]
pointwise on smooth fields.

### 3.3 Uniform integrability (the “UV control” bottleneck)
To pass limits under \(\mu_a\), one needs uniform integrability of \(|\nabla_a F_a|^2\).

The project’s proposed sufficient condition is a polylogarithmic “UV Log-Forest” bound:
\[
\mathbb{E}_{\mu_a}\big[\|\nabla_a F\|^2\big] \le C(F)\,(1+\log(1/a))^p,
\]
uniform in lattice volume.

With concentration from LSI plus moment bounds, one can invoke Vitali convergence to justify \(L^1\) convergence of gradients.

## 4. Semigroup convergence (Trotter–Kato)

Mosco convergence of closed Dirichlet forms implies strong convergence of the associated semigroups:
\[
P_t^a \to P_t \quad \text{strongly on } L^2
\]
for each fixed \(t>0\).

This is the key bridge that transports analytic inequalities expressed in terms of semigroups.

## 5. Stability of curvature-dimension / Bakry–Émery bounds

Assume each lattice model satisfies a curvature-dimension inequality
\[
\Gamma_{2,a}(f) \ge \rho_0\,\Gamma_a(f)
\qquad (\rho_0>0\ \text{uniform in }a).
\tag{CD}
\]

A standard equivalent form is gradient contraction:
\[
\|\nabla_a P_t^a f\|^2 \le e^{-2\rho_0 t}\,\|\nabla_a f\|^2.
\tag{GC-a}
\]

Using semigroup convergence and Mosco liminf/recovery arguments, one can pass (GC-a) to the limit:
\[
\|\nabla P_t f\|^2 \le e^{-2\rho_0 t}\,\|\nabla f\|^2,
\tag{GC}
\]
which is equivalent to
\[
\Gamma_2(f) \ge \rho_0\,\Gamma(f).
\]

Hence the continuum model inherits \(CD(\rho_0,\infty)\) and therefore an LSI with constant \(\rho_0\).

## 6. What is potentially novel here?

- The project treats **Mosco stability of CD(\(\rho\),\(\infty\))** as the core analytic bridge from lattice to continuum.
- The UV Log-Forest bound is positioned as the “minimal” estimate needed to keep the Dirichlet core alive in the continuum.

If the UV control can be proven with the required uniformity, then the remainder of the analytic pipeline is relatively standard and robust.

## 7. Next technical targets

1. **Prove the UV Log-Forest bound** from explicit multiscale estimates (or show a sharper bound).
2. **Make the holonomy approximation uniform** on the rough support of \(\mu\) (not just smooth fields).
3. **Check closability and quasi-regularity** of \(\mathcal{E}\) in the infinite-dimensional setting to ensure the associated diffusion is well-defined.

