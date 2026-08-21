# Reflection Positivity and Limit Stability
*(pushforwards, projective limits, and monotone form limits as “permanence principles”)*

## 1. Reflection positivity on a measured reflected space

Let \((\Omega,\mathcal F,\mu)\) be a probability space and let \(\theta:\Omega\to\Omega\) be a measurable involution (\(\theta^2=\mathrm{id}\)). Let \(\mathcal F_+\subset\mathcal F\) be a “positive-time” \(\sigma\)-algebra.

### Definition 1.1 (Reflection positivity)
\((\Omega,\mu,\theta;\mathcal F_+)\) is reflection positive if for every bounded \(\mathcal F_+\)-measurable \(F\),
\[
\langle F,\theta F\rangle_{L^2(\mu)}:=\int \overline{F(\omega)}\,F(\theta\omega)\,d\mu(\omega)\ \ge\ 0,
\]
equivalently the Gram matrix \((\langle F_i,\theta F_j\rangle)\) is positive semidefinite for all finite families \(\{F_i\}\subset L^\infty(\mathcal F_+)\).

This is OS2 in measure-theoretic form.

---

## 2. RP survives reflection-equivariant coarse graining

### Lemma 2.1 (RP survives reflection-equivariant pushforward)
Let \((\Omega,\mathcal F,\mu,\theta;\mathcal F_+)\) be reflection positive. Let \((\Omega',\mathcal F',\theta';\mathcal F'_+)\) be another reflected measurable space, and let \(P:\Omega\to\Omega'\) be measurable such that:

1. \(P\circ\theta = \theta'\circ P\),
2. \(P^{-1}(\mathcal F'_+)\subset \mathcal F_+\),
3. \(\mu' := P_\#\mu\).

Then \((\Omega',\mu',\theta';\mathcal F'_+)\) is reflection positive.

**Proof.**
Take \(G_1,\dots,G_n\in L^\infty(\mathcal F'_+)\) and define \(F_i:=G_i\circ P\in L^\infty(\mathcal F_+)\) by (2). Then, using (3) and equivariance (1),
\[
\langle G_i,\theta' G_j\rangle_{L^2(\mu')}
=
\langle F_i,\theta F_j\rangle_{L^2(\mu)}.
\]
The right-hand Gram matrix is PSD by RP of \(\mu\), hence so is the left. \(\square\)

Interpretation: any RG/blocking map that commutes with the OS reflection and respects the positive half preserves RP.

---

## 3. RP survives projective limits (cylinder level)

Consider a directed system \(\{(\Omega_i,\mu_i,\theta_i;\mathcal F_{i,+})\}_{i\in\mathcal I}\) with compatible projections \(P_{i\to j}\) such that for \(j\preceq i\):

- \(P_{i\to j}\circ\theta_i=\theta_j\circ P_{i\to j}\),
- \(P_{i\to j}^{-1}(\mathcal F_{j,+})\subset \mathcal F_{i,+}\),
- \((P_{i\to j})_\#\mu_i=\mu_j\).

Let \(\mu\) be the projective limit measure on the inverse limit space \(\Omega\), and \(\pi_i:\Omega\to\Omega_i\) the canonical projections.

### Lemma 3.1 (RP passes to the projective limit on cylinder observables)
If each \(\mu_i\) is reflection positive, then \(\mu\) is reflection positive on cylinder observables: for any finite family of bounded \(F_k=\widetilde F_k\circ\pi_i\) with \(\widetilde F_k\in L^\infty(\mathcal F_{i,+})\), the Gram matrix \((\langle F_p,\theta F_q\rangle_{L^2(\mu)})\) is PSD.

**Proof.**
By definition of the projective limit, expectations of cylinder functions under \(\mu\) equal those under \(\mu_i\). Reflection commutes with projection, so
\[
\langle F_p,\theta F_q\rangle_{L^2(\mu)}
=
\langle \widetilde F_p,\theta_i \widetilde F_q\rangle_{L^2(\mu_i)}.
\]
The right-hand Gram matrix is PSD by RP of \(\mu_i\). \(\square\)

This is a minimal permanence lemma: it does not claim full OS reconstruction in the limit, only that RP itself is not destroyed by consistent limiting.

---

## 4. Uniform gaps persist under monotone quadratic-form limits (conditional lemma)

The following is a standard but essential “endgame” lemma when discussing \(a\to 0\) or \(|\Lambda|\to\infty\).

### Lemma 4.1 (Uniform gap persists under monotone form limits)
Assume:

1. A family of Hilbert spaces \(\mathcal H_a\) isometrically embeds into a common \(\mathcal H\) via \(\iota_a\), with consistent vacua \(\iota_a\Omega_a=\Omega\).
2. The closed quadratic forms of \(H_a\ge 0\) are monotone increasing in the sense
   \[
   \langle \psi, H_{a'}\psi\rangle \ge \langle \psi,H_a\psi\rangle
   \]
   on a common dense form core (after identification via \(\iota\)).
3. There is a uniform gap at each \(a\):
   \[
   \langle \psi,H_a\psi\rangle \ge \Delta_*\,\|\psi\|^2
   \qquad (\forall \psi\perp\Omega_a),
   \]
   with \(\Delta_*>0\) independent of \(a\).

Then any strong-resolvent (or form) limit \(H_{\mathrm{lim}}\) satisfies
\[
\langle \psi,H_{\mathrm{lim}}\psi\rangle \ge \Delta_*\,\|\psi\|^2
\qquad(\forall \psi\perp\Omega),
\]
hence
\[
\sigma(H_{\mathrm{lim}})\subset\{0\}\cup[\Delta_*,\infty).
\]

**Proof sketch.**
Approximate \(\psi\perp\Omega\) by \(\psi_a\in\iota_a(\mathcal H_a)\) with \(\psi_a\to\psi\) and \(\psi_a\perp\Omega\). Apply the uniform gap inequality to \(\psi_a\) and pass to the limit using lower semicontinuity of the limiting form. \(\square\)

---

## 5. Why this matters in the larger architecture

- Lemmas 2.1 and 3.1 say: **reflection positivity can be engineered to survive RG/blocking and consistent limits**, if coarse graining respects the reflection.
- Lemma 4.1 says: **if you can compare Hamiltonians across cutoffs in a monotone way**, a uniform gap at finite cutoff survives the limit.

In combination with conditional spectral floor monotonicity, these lemmas support a “permanence layer” of the proof architecture: once a gap is established at some stage, many subsequent bookkeeping moves cannot destroy it.

