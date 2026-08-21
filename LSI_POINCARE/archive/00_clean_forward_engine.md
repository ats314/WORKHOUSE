# Clean Forward Engine for a Lattice Yang–Mills Mass Gap

*(Curvature → functional inequalities → diffusion gap → OS transfer gap → mass gap)*

## 0. Purpose

The project notes contain many interlocking parts. This file distills the core dependency graph that keeps showing up across the drafts:

\[
\boxed{
\text{(local Bakry–Émery curvature on a safe set)}
\Longrightarrow
\text{(global LSI / Poincaré)}
\Longrightarrow
\text{(configuration diffusion gap)}
\Longrightarrow
\text{(OS transfer gap)}
\Longrightarrow
\text{(mass gap)}
}
\]

The *interesting* aspect is methodological: the hard analysis is pushed into **finite-dimensional geometric inequalities** on the compact manifold
\[
M_\Lambda := G^{E(\Lambda)}\qquad (G=\mathrm{SU}(N)),
\]
and then into a single **OS identification** step. “Thermodynamic limit” issues become (nontrivial!) bookkeeping about keeping constants uniform in \(|\Lambda|\) and along a continuum scaling trajectory.

The other extracted documents are the engines; this one is the roadmap.

---

## 1. The common objects

### 1.1 Configuration manifold and Gibbs law

Fix a finite hypercubic region \(\Lambda\subset\mathbb Z^4\) with oriented edges \(E(\Lambda)\) and plaquettes \(P(\Lambda)\).
The configuration space is
\[
M_\Lambda := G^{E(\Lambda)}
\]
with product bi-invariant metric and volume.

A lattice Gibbs law has density
\[
\mu_\Lambda(dU) = Z_\Lambda^{-1} e^{-S_\Lambda(U)}\, d\mathrm{vol}(U),
\]
where \(S_\Lambda\) is local and gauge-invariant (Wilson + optional stabilizers).

### 1.2 Reversible configuration diffusion

The canonical symmetric generator is
\[
L_\Lambda f
=
\Delta_\Lambda f - \langle \nabla S_\Lambda,\nabla f\rangle,
\]
with carré du champ \(\Gamma_\Lambda(f)=|\nabla f|^2\) and Dirichlet form
\[
\mathcal E_\Lambda(f,f)
=
\int_{M_\Lambda}\Gamma_\Lambda(f)\,d\mu_\Lambda
=
-\int_{M_\Lambda} f(L_\Lambda f)\,d\mu_\Lambda.
\]

A uniform Poincaré inequality is exactly a uniform spectral gap for \(-L_\Lambda\):
\[
\mathrm{Var}_{\mu_\Lambda}(f)\le C_P \int\Gamma_\Lambda(f)\,d\mu_\Lambda
\quad\Longleftrightarrow\quad
-L_\Lambda \succeq \lambda_1 I\text{ on }L_0^2(\mu_\Lambda),\ \lambda_1=1/C_P.
\]

---

## 2. The “safe set + Lyapunov” paradigm

### 2.1 Why a safe set exists

For gauge theory you typically do **not** have a global curvature lower bound for the Bakry–Émery tensor
\[
\mathrm{Ric}_{\mu_\Lambda} := \mathrm{Ric}_{g_\Lambda}+\nabla^2 S_\Lambda.
\]

But you often can show:

- on a **small-field / near-vacuum** region \(K_\Lambda\subset M_\Lambda), \(\mathrm{Ric}_{\mu_\Lambda}\) is uniformly positive on the physical (horizontal) directions;
- the dynamics (or the measure) has a **Lyapunov drift** that keeps typical configurations from spending much time in \(K_\Lambda^c\).

This is the conceptual bridge from “local convexity” to “global functional inequality.”

### 2.2 The minimal analytic template

A typical template is:

1. (**Local CD/LSI/Poincaré on \(K_\Lambda\)**)  
   Prove a local functional inequality on \(K_\Lambda\) with constants independent of \(|\Lambda|\).

2. (**Lyapunov drift**)  
   Find \(W\ge 1\) such that
   \[
   L_\Lambda W \le -\lambda W + b\,\mathbf 1_{K_\Lambda}
   \]
   with \(\lambda,b\) uniform in \(\Lambda\).

3. (**Localization removal**)  
   Use (2) to control \(\mu_\Lambda(K_\Lambda^c)\) and upgrade the local inequality to a global one.

This is the “clean forward engine” in the notes.

---

## 3. Where the gauge geometry gives you a mass term

A recurring theme in the drafts is that the compact group geometry provides a **strictly positive** contribution:

- On a compact semisimple \(G\) with bi-invariant metric,
  \(\mathrm{Ric}_G\ge \kappa_G g_G\) with \(\kappa_G>0\).
- On the product \(M_\Lambda=G^{E(\Lambda)}\), this gives a uniform term
  \(\mathrm{Ric}_{g_\Lambda}\ge \kappa_G g_\Lambda\).

This “Haar mass” (in the pulled-back exponential-coordinate picture: Jacobian convexity) is what prevents the Maxwell operator \(d_1^\ast d_1\) from being purely massless in the horizontal sector.

That mechanism is formalized in the **core curvature theorem** (see `02_haar_mass_and_core_curvature.md`).

---

## 4. How correlation decay enters without “absolute values”

Once you have a pointwise lower bound on a 1-form operator of the form
\[
\mathrm{Ric}_{g_\Lambda}+\nabla^2 S_\Lambda \ \succeq\ m^2 I + t\, d_1^\ast d_1
\quad\text{(on the horizontal sector)},
\]
you can use the Helffer–Sjőstrand/Witten-Laplacian covariance representation to write
\[
\mathrm{Cov}_{\mu_\Lambda}(F,G)
=
\int \langle \nabla F,(\mathcal L^{(1)})^{-1}\nabla G\rangle\,d\mu_\Lambda
\ \le\
\int \langle \nabla F, (m^2 I+t d_1^\ast d_1)^{-1}\nabla G\rangle\,d\mu_\Lambda
\]
on the safe set.

The key point: **no termwise absolute values of Hessian entries**.  
All signs are preserved inside the PSD operator \(d_1^\ast d_1\).

The Green’s function decay for \((m^2I+t d_1^\ast d_1)^{-1}\) on \(\ker d_0^\ast\) is explicit (see `03_helffer_sjostrand_and_green_decay.md`).

---

## 5. The OS bridge

The final conceptual jump is:

- Euclidean functional inequalities / clustering live in the measure \(\mu_\Lambda\).
- The physical mass gap lives in the spectrum of the OS transfer operator \(T_a=e^{-aH}\).

The project’s OS bridge files (`05_os_bridge_mass_gap.md` + Part 21 in the notes) isolate the exact missing lemma: a **one-step identification** of a time-slice reversible operator with the OS transfer on the physical subspace.

This is where a hostile referee will focus.

---

## 6. The bottlenecks that remain “real work”

The extracted derivations reduce the program to a small set of checkable bottlenecks:

1. **Lyapunov coercivity**: prove \(\langle \nabla S_\Lambda,\nabla V\rangle\) controls a bulk badness functional outside a small set (see `01_lyapunov_drift_and_local_gram.md`).

2. **Uniformity along scaling**: keep the safe-set and Lyapunov constants uniform as \(a\to 0\) along the continuum trajectory (Part 19).

3. **OS identification**: show the one-step slice operator really *is* the OS transfer on the physical subspace (Part 21).

If those three land cleanly, the rest of the engine is already in place.
