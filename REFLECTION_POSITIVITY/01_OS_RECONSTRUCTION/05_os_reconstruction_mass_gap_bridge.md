# OS Reconstruction and the Diffusion-to-Hamiltonian Mass Gap Bridge

*Project extraction (generated 2025-12-29).*

## 0. The bridge in one line

The project’s analytic pipeline can be summarized as

\[
\mathrm{Ric}_V\ge \rho_0 g
\;\Longrightarrow\;
\text{LSI}(\rho_0)
\;\Longrightarrow\;
\text{gap}(L)\ge \rho_0
\;\Longrightarrow\;
\text{exp.\ decay of Euclidean correlators}
\;\Longrightarrow\;
\text{mass gap of }H.
\]

The hard part is building a **uniform** $\rho_0>0$.

Once you have $\rho_0$, this module is the “physics legality” step: go from a probabilistic Euclidean theory to a quantum Hamiltonian with a gap.

---

## 1. LSI implies a spectral gap for the diffusion generator

Let $(\mu,L)$ be the invariant measure and generator of the (stochastic quantization / heat-flow) diffusion on field space.

Assume the LSI:
\[
\mathrm{Ent}_\mu(f^2)\le \frac{2}{\rho_0}\int |\nabla f|^2\,d\mu.
\]

Then (standard) the Poincaré inequality follows:
\[
\mathrm{Var}_\mu(f)\le \frac{1}{\rho_0}\int |\nabla f|^2\,d\mu.
\]

Equivalently, the spectral gap of $-L$ in $L^2(\mu)$ satisfies
\[
\lambda_1(-L)\ge \rho_0.
\]

---

## 2. Euclidean decay from the gap

For a centered observable $O$ with $\mu(O)=0$, consider the semigroup correlator
\[
C(t) := \langle O, e^{tL}O\rangle_{L^2(\mu)}.
\]

Expanding in the spectral decomposition of $L$ yields
\[
|C(t)|\le e^{-\rho_0 t}\,\|O\|^2_{L^2(\mu)}.
\]

So the diffusion-time correlator decays exponentially at rate $\rho_0$.

---

## 3. Reflection positivity and OS reconstruction

Assume the limiting Euclidean measure $\mu$ satisfies the OS axioms, in particular **reflection positivity**:

for a reflection $\Theta$ and any $f$ supported in positive time,
\[
\int (\Theta f)\,\overline{f}\,d\mu \ge 0.
\]

Then OS reconstruction builds:

- a physical Hilbert space $\mathcal{H}_{\mathrm{OS}}$,
- a vacuum vector $\Omega$,
- a self-adjoint Hamiltonian $H\ge 0$ such that time translations act as $e^{-tH}$.

---

## 4. From Euclidean decay to a Hamiltonian mass gap

For a suitable (time-zero) observable $O$ represented as a vector in $\mathcal{H}_{\mathrm{OS}}$,
\[
\langle \Omega,\, O\, e^{-tH} O\,\Omega\rangle
\]
is the Euclidean two-point function in time direction.

If this quantity decays as $\lesssim e^{-\rho_0 t}$, then the spectrum of $H$ above $0$ begins at least at $\rho_0$:
\[
\inf(\sigma(H)\setminus\{0\})\ge \rho_0.
\]

This is the **mass gap** conclusion.

---

## 5. Where subtlety lives

This bridge is classical — the subtleties are *compatibility subtleties*:

1. **Does reflection positivity survive the limit?**  
   Weak convergence of measures plus density of cylinder functions is the usual route.

2. **Is the diffusion generator $L$ the right object?**  
   One must identify the semigroup whose gap controls the physically reconstructed Hamiltonian.

3. **Local vs global:**  
   Even if the full theory has slow global/topological modes, locality arguments can protect a *local* gap that is sufficient for local correlators.

---

## 6. Why this is still worth extracting

In most attempted “mass gap from functional inequalities” strategies, the failure mode is:  
you can show some inequality, but you can’t push it through all the required limiting and reconstruction steps without losing constants or axioms.

This module is the repository’s attempt to keep that bridge explicit and modular — so if $\rho_0$ is secured, the rest is (in principle) mechanical.

