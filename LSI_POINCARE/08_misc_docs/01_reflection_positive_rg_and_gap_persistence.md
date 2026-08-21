# Reflection-Positive Coarse Graining and Gap Persistence in Projective Limits

This note extracts the **continuum-interface** ideas:

1. *Reflection positivity (RP) is stable under reflection-equivariant, positive-time-preserving coarse graining.*
2. *RP is stable under projective limits on cylinder observables.*
3. *A uniform spectral gap persists under monotone quadratic-form limits.*

The theme is “**do no harm**”: once fixed-cutoff RP + fixed-cutoff gap are proven, the continuum step should not require re-proving RP from scratch; instead, we isolate the exact compatibility conditions needed from the cutoff-removal architecture.

---

## 1. Reflected probability spaces and reflection positivity

A **reflected probability space** is a quintuple
\[
(\Omega,\mathcal F,\mu,\theta;\mathcal F_+),
\]
where $(\Omega,\mathcal F,\mu)$ is a probability space, $\theta:\Omega\to\Omega$ is a measurable involution ($\theta^2=\mathrm{id}$), and $\mathcal F_+\subset\mathcal F$ is a designated “positive-time” $\sigma$-algebra.

### Definition (Reflection positivity)
The space is **reflection positive** if for every bounded $\mathcal F_+$-measurable complex function $F$,
\[
\int_\Omega \overline{F(\omega)}\,F(\theta\omega)\,d\mu(\omega)\ \ge\ 0.
\]
Equivalently, for any finite family $F_1,\dots,F_n\in L^\infty(\mathcal F_+)$, the Gram matrix
\[
\Big(\langle F_i,\theta F_j\rangle_{L^2(\mu)}\Big)_{i,j=1}^n
\quad\text{with}\quad
\langle F,\theta G\rangle:=\int \overline{F(\omega)}\,G(\theta\omega)\,d\mu(\omega)
\]
is positive semidefinite.

This is the abstract OS condition used by reconstruction.

---

## 2. RP survives reflection-equivariant coarse graining (pushforward lemma)

Let $(\Omega,\mathcal F,\mu,\theta;\mathcal F_+)$ be RP (“fine” scale).
Let $(\Omega',\mathcal F',\theta';\mathcal F'_+)$ be a reflected measurable space (“coarse” scale).

Let $P:\Omega\to\Omega'$ be measurable and assume:

1. **Reflection equivariance**
   \[
   P\circ\theta=\theta'\circ P.
   \]
2. **Positive-time preservation**
   \[
   P^{-1}(\mathcal F'_+)\subset\mathcal F_+.
   \]
3. **Measure pushforward**
   \[
   \mu' := P_\#\mu.
   \]

### Lemma (Pushforward permanence of RP)
Under 1–3, $(\Omega',\mathcal F',\mu',\theta';\mathcal F'_+)$ is reflection positive.

**Proof.**
Take bounded $\mathcal F'_+$-measurable $G_1,\dots,G_n$ and define $F_i:=G_i\circ P$.
By positive-time preservation, $F_i$ are $\mathcal F_+$-measurable.

Compute, using $\mu'=P_\#\mu$:
\[
\langle G_i,\theta'G_j\rangle_{L^2(\mu')}
= \int_{\Omega'}\overline{G_i(\omega')}\,G_j(\theta'\omega')\,d\mu'(\omega')
= \int_\Omega \overline{G_i(P\omega)}\,G_j(\theta'(P\omega))\,d\mu(\omega).
\]
By reflection equivariance, $\theta'(P\omega)=P(\theta\omega)$, so this equals
\[
\int_\Omega \overline{F_i(\omega)}\,F_j(\theta\omega)\,d\mu(\omega)
=\langle F_i,\theta F_j\rangle_{L^2(\mu)}.
\]
Thus the coarse Gram matrix equals a fine Gram matrix, hence is PSD. $\square$

**Interpretation.**
Reflection positivity is *hard to kill*: any RG / blocking / flowed map that commutes with reflection and does not leak negative-time dependence into positive-time observables automatically preserves RP.

---

## 3. RP survives projective limits (cylinder-level)

Let $\mathcal I$ index cutoffs (think $a\downarrow 0$).
For each $i\in\mathcal I$, let
\[
(\Omega_i,\mathcal F_i,\mu_i,\theta_i;\mathcal F_{i,+})
\]
be RP.

Assume **projective consistency**: for $j\preceq i$ there is a measurable map $P_{i\to j}:\Omega_i\to\Omega_j$ with

1. $P_{i\to j}\circ\theta_i=\theta_j\circ P_{i\to j}$,
2. $P_{i\to j}^{-1}(\mathcal F_{j,+})\subset\mathcal F_{i,+}$,
3. $(P_{i\to j})_\#\mu_i=\mu_j$.

Let $(\Omega,\mu)$ be the inverse-limit space/measure with canonical projections $\pi_i:\Omega\to\Omega_i$ and induced reflection $\theta$ satisfying $\pi_i\circ\theta=\theta_i\circ\pi_i$.

A **cylinder function** is $F=\widetilde F\circ\pi_i$ for some $i$.

### Lemma (Projective-limit RP on cylinders)
If each $\mu_i$ is RP, then $\mu$ is RP on cylinder functions supported in positive time.

**Proof.**
Fix $i$ and bounded $\mathcal F_{i,+}$-measurable $\widetilde F_1,\dots,\widetilde F_n$.
Let $F_k=\widetilde F_k\circ\pi_i$.

Using the inverse-limit identity for cylinder expectations and $\pi_i\circ\theta=\theta_i\circ\pi_i$,
\[
\langle F_p,\theta F_q\rangle_{L^2(\mu)}
=\langle \widetilde F_p,\theta_i\widetilde F_q\rangle_{L^2(\mu_i)}.
\]
Hence the cylinder Gram matrix under $\mu$ is the same as the Gram matrix under $\mu_i$, which is PSD. $\square$

**Why cylinder-level is the correct granularity.**
OS reconstruction is built from the local/cylinder algebra; one does not need RP on an enormous $\sigma$-algebra to reconstruct the Hamiltonian.

---

## 4. A monotone form limit cannot destroy a uniform gap

This is the “functional-analytic battery” you can plug into any continuum construction once you have a common Hilbert space.

Let $\mathcal H$ be a Hilbert space and $\Omega\in\mathcal H$ a normalized vacuum vector.
Write $\mathcal K:=\mathbb C\Omega$ and $P_0$ the projection onto $\mathcal K$.

Let $\{q_n\}_{n\ge 1}$ be densely defined nonnegative quadratic forms on $\mathcal H$ with a common core $\mathcal D_0$, monotone:
\[
q_1(\psi)\le q_2(\psi)\le\cdots\le q_n(\psi)\le q_{n+1}(\psi)\le\cdots
\qquad(\psi\in\mathcal D_0),
\]
and vacuum normalization $q_n(\Omega)=0$.

Define on $\mathcal D_0$:
\[
q_{\mathrm{cont}}(\psi):=\sup_{n\ge 1} q_n(\psi),
\]
and let $\overline q_{\mathrm{cont}}$ denote its closure, represented by a self-adjoint $H_{\mathrm{cont}}\ge 0$ via
\[
\overline q_{\mathrm{cont}}(\psi)=\|H_{\mathrm{cont}}^{1/2}\psi\|^2.
\]

### Assumption (Uniform gap bound at each cutoff, form version)
There exists $\Delta_\star>0$ such that for all $n$ and all $\psi\in\mathcal D_0$,
\[
q_n(\psi)\ \ge\ \Delta_\star\,\|(I-P_0)\psi\|^2.
\]

### Proposition (Gap persistence under monotone limits)
Then for all $\psi\in D(\overline q_{\mathrm{cont}})$,
\[
\overline q_{\mathrm{cont}}(\psi)\ \ge\ \Delta_\star\,\|(I-P_0)\psi\|^2,
\]
equivalently, as quadratic forms,
\[
H_{\mathrm{cont}}\ \succeq\ \Delta_\star\,(I-P_0).
\]

**Proof (two lines).**
On the core $\mathcal D_0$, take $\sup_n$ of $q_n(\psi)\ge \Delta_\star\|(I-P_0)\psi\|^2$ to get
$q_{\mathrm{cont}}(\psi)\ge \Delta_\star\|(I-P_0)\psi\|^2$.
Then pass to the closure using $\psi_k\to\psi$ and boundedness of $I-P_0$. $\square$

### Corollary (Spectral consequence)
\[
\sigma(H_{\mathrm{cont}})\subseteq \{0\}\cup[\Delta_\star,\infty).
\]
If $\ker H_{\mathrm{cont}}=\mathbb C\Omega$, then $\mathrm{gap}(H_{\mathrm{cont}})\ge\Delta_\star$.

---

## 5. Why this is “new theory potential”

This package suggests a general blueprint:

1. Prove **fixed-cutoff** clustering $\Rightarrow$ fixed-cutoff OS gap at each $a$.
2. Construct any **reflection-equivariant** coarse-graining / projective architecture so RP survives to the limit on cylinders.
3. Realize the continuum Hamiltonian as a **monotone quadratic-form limit** of cutoff Hamiltonians on a common Hilbert space.
4. Conclude the **gap persists**.

Items 2–3 are “infrastructure,” but the lemmas above show you can make the infrastructure requirements extremely explicit and checkable.

