# Permanence framework: uniform finite-volume decay \(\Rightarrow\) thermodynamic limit \(\Rightarrow\) OS gap; and what is needed for \(a\downarrow 0\)

## Scope

This note extracts a “permanence framework” that is **structurally clean** and mostly measure-theoretic / functional-analytic:

1. If a finite-volume exponential clustering estimate holds with constants uniform in the volume, then every thermodynamic limit point inherits the same exponent.
2. Reflection positivity (RP) is closed under weak limits and under reflection-equivariant pushforward maps.
3. If a continuum limit is organized as a monotone family of quadratic forms with a uniform gap bound, then the limiting Hamiltonian inherits the gap.

This is useful because it isolates what the project’s analytic estimates must actually deliver to make the remaining steps formal, without pretending to have solved constructive YM.

---

## 1. Uniform clustering survives the thermodynamic limit

Let \(\Omega:=G^{E(\mathbb Z^d)}\) be the infinite-volume configuration space (compact in product topology). Let \(\widetilde\mu_L\) be finite-volume Gibbs measures embedded into \(\Omega\) (e.g. by periodic extension from tori).

Assume a finite-volume exponential clustering bound with constants \(\eta>0\) and \(C_*(\beta)<\infty\) **independent of \(L\)** once supports fit:
\[
\big|\mathrm{Cov}_{\widetilde\mu_L}(F,G)\big|
\le
C_*(\beta)\,|\nabla F|_\infty\,|\nabla G|_\infty\,
e^{-\eta\,\mathrm{dist}(\mathrm{supp}F,\mathrm{supp}G)}.
\tag{1.1}
\]

### Proposition 1.1 (Thermodynamic limit inherits the same exponent)

If \(\widetilde\mu_{L^{(n)}}\Rightarrow \mu_\infty\) weakly on \(\Omega\), then (1.1) passes to the limit:
\[
\big|\mathrm{Cov}_{\mu_\infty}(F,G)\big|
\le
C_*(\beta)\,|\nabla F|_\infty\,|\nabla G|_\infty\,
e^{-\eta\,\mathrm{dist}(\mathrm{supp}F,\mathrm{supp}G)}
\tag{1.2}
\]
for all smooth cylinder observables \(F,G\).

**Reason:** for fixed supports, (i) wrap-around disappears for large tori, and (ii) covariance is a continuous functional of \(\mu\) for bounded cylinder functions, so the uniform inequality is closed under weak limits.

---

## 2. Reflection positivity is stable under limits and coarse-graining

Reflection positivity is the key input for OS reconstruction. Two stability facts are isolated.

### Lemma 2.1 (RP passes to weak limits)

Fix a reflection \(\Theta\) and positive-time \(\sigma\)-algebra \(\mathcal F_+\). If each \(\widetilde\mu_L\) is RP w.r.t. \(\Theta\), then any weak limit \(\mu_\infty\) is also RP, because the defining inequality is evaluated on bounded cylinder functions and is closed under weak convergence.

### Lemma 2.2 (RP survives reflection-equivariant pushforward)

Let \((\Omega,\mu,\theta;\mathcal F_+)\) be RP. Let \(P:\Omega\to\Omega'\) be measurable such that

1. \(P\circ\theta=\theta'\circ P\) (reflection equivariance),
2. \(P^{-1}(\mathcal F'_+)\subset \mathcal F_+\) (positive-time support respected),
3. \(\mu':=P_\#\mu\).

Then \((\Omega',\mu',\theta';\mathcal F'_+)\) is RP.

**Reason:** Gram matrices for observables \(G_i\) on \(\Omega'\) pull back to Gram matrices for \(F_i=G_i\circ P\) on \(\Omega\), and positivity is preserved.

This lemma is the minimal “RG map is allowed” condition if one wants reflection positivity to survive a blocking transformation.

---

## 3. From Euclidean exponential time decay to an OS Hamiltonian gap

OS reconstruction gives a Hilbert space \(\mathcal H\), vacuum \(\Omega\), and Hamiltonian \(H\ge 0\) such that time translations correspond to \(e^{-tH}\).

A standard spectral-measure argument gives:

### Lemma 3.1 (Exponential decay implies a spectral gap)

If for every centered local observable \(F\) there exists \(C(F)\) and \(m>0\) such that
\[
|\mathbb E_\mu[F\,\tau_t F]|\le C(F)e^{-mt}\quad \forall t\ge 0,
\tag{3.1}
\]
then \(\sigma(H)\cap(0,m)=\emptyset\), i.e. \(\mathrm{gap}(H)\ge m\).

This is the *operational* meaning of “mass” in the Euclidean theory.

---

## 4. The \(a\downarrow 0\) cutoff removal: what must be uniform (and what must scale)

At lattice spacing \(a\), a “one-step” Euclidean decay exponent \(\eta(a)\) corresponds to a physical mass lower bound
\[
m(a)\ \gtrsim\ \frac{\eta(a)}{a}.
\tag{4.1}
\]
Therefore, to obtain a **finite nonzero continuum mass** \(m_{\mathrm{gap}}>0\), one needs
\[
\eta(a)\sim m_{\mathrm{gap}}\,a\quad\text{as }a\downarrow 0,
\tag{4.2}
\]
not merely \(\eta(a)\ge \eta_0>0\) (which would imply \(m(a)\gtrsim 1/a\), a cutoff artifact).

This is why the project’s continuum step is framed as a permanence theorem: one must organize the \(a\)-family so that physical units are tracked.

---

## 5. Gap persistence under monotone quadratic-form limits (conditional but sharp)

Suppose one has OS Hamiltonians \(H_a\) on \(\mathcal H_a\) along a cutoff family, embedded into a common Hilbert space \(\mathcal H\), and define quadratic forms \(q_a(\psi)=\|H_a^{1/2}\psi\|^2\).

Assume:

1. A common dense form core \(D_0\subset\bigcap_a D(q_a)\).
2. Monotonicity under refinement: \(q_{a'}(\psi)\ge q_a(\psi)\) on \(D_0\) for \(a'\) coarser than \(a\).
3. A uniform gap bound: for all \(\psi\perp\Omega\), \(q_a(\psi)\ge \Delta_* \|\psi\|^2\) with \(\Delta_*>0\) independent of \(a\).

Define the limiting form \(q_{\mathrm{cont}}(\psi)=\sup_a q_a(\psi)\) on \(D_0\), close it, and let \(H_{\mathrm{cont}}\) be the associated self-adjoint operator.

### Lemma 5.1 (Uniform gap passes to the limit)

Under the hypotheses above,
\[
q_{\mathrm{cont}}(\psi)\ \ge\ \Delta_*\|\psi\|^2
\quad\forall \psi\perp\Omega,
\]
hence
\[
\sigma(H_{\mathrm{cont}})\subset\{0\}\cup[\Delta_*,\infty),
\qquad
\mathrm{gap}(H_{\mathrm{cont}})\ge \Delta_*.
\tag{5.1}
\]

This is a clean “don’t lose the gap in the limit” lemma — but it is conditional on (i) having a coherent embedding across cutoffs, and (ii) proving the physically scaled uniform gap \(\Delta_*\), not just a lattice-step bound.

---

## 6. What this permanence framework demands from the analytic engine

To make the full story close, the analytic part of the project must deliver, at each fixed cutoff \(a\):

1. Exponential clustering with an exponent \(\eta(a)\) *uniform in volume* (thermodynamic stability).
2. RP (for OS reconstruction), stable under the limiting procedure.
3. Control of \(\eta(a)\) along a scaling trajectory \(\beta(a)\) so that (4.2) holds (continuum nontriviality).

The permanence lemmas remove the temptation to “handwave” these steps: either the needed uniformities are proved, or they are not.

