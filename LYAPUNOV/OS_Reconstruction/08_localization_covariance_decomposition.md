# Localization without exponent loss: covariance decomposition across a “good set” event

## Scope

The improved stack uses a sharp localization step:

*You can prove the matrix/Green’s-function covariance bound only on a canonical small-field set \(K_\Lambda\), then extend it to the full Gibbs measure \(\mu_\Lambda\) with an error controlled directly by \(\mu_\Lambda(K_\Lambda^c)\) (or by capacity bounds).*

This note extracts the exact covariance decomposition identity and the minimal inequality that isolates the only remaining analytic burden: controlling \(\mu_\Lambda(K_\Lambda^c)\) in a way that does not degrade the exponential rate.

---

## 1. Setup

Let \(\mu\) be a probability measure on a measurable space \((\Omega,\mathcal F)\), and let \(K\in\mathcal F\) with \(0<\mu(K)<1\). Define conditional measures
\[
\mu_K(\cdot):=\mu(\cdot\mid K),
\qquad
\mu_{K^c}(\cdot):=\mu(\cdot\mid K^c).
\]
For a bounded measurable \(F\), define the conditional mean gap
\[
\Delta_K F := \mu_K(F)-\mu_{K^c}(F).
\]

---

## 2. Exact covariance decomposition

### Lemma 2.1 (Covariance decomposition across an event)

For bounded measurable \(F,G\),
\[
\mathrm{Cov}_\mu(F,G)
=
\mu(K)\,\mathrm{Cov}_{\mu_K}(F,G)
+
\mu(K^c)\,\mathrm{Cov}_{\mu_{K^c}}(F,G)
+
\mu(K)\mu(K^c)\,\Delta_K F\ \Delta_K G.
\tag{2.1}
\]

**Proof.** Write \(\alpha=\mu(K)\). Then \(\mu=\alpha\mu_K+(1-\alpha)\mu_{K^c}\). Expand \(\mu(FG)-\mu(F)\mu(G)\) and regroup terms. \(\square\)

---

## 3. A crude but useful bound isolating the localization error

### Corollary 3.1 (Localization error bounded by \(\mu(K^c)\))

For bounded \(F,G\),
\[
\big|\mathrm{Cov}_\mu(F,G)\big|
\le
\big|\mathrm{Cov}_{\mu_K}(F,G)\big|
+
8\,\|F\|_\infty\,\|G\|_\infty\,\mu(K^c).
\tag{3.1}
\]

**Proof.** From (2.1), use \(|\mathrm{Cov}_\nu(F,G)|\le 4\|F\|_\infty\|G\|_\infty\) for any probability \(\nu\), and \(|\Delta_K F|\le 2\|F\|_\infty\). \(\square\)

---

## 4. Why this localization step is structurally important

Suppose one proves a sharp exponential clustering bound **on \(\mu_K\)**:
\[
|\mathrm{Cov}_{\mu_K}(F,G)|
\le
C\,|\nabla F|_\infty|\nabla G|_\infty\,
e^{-\eta\,\mathrm{dist}(\mathrm{supp}F,\mathrm{supp}G)}.
\tag{4.1}
\]

Then (3.1) yields:
\[
|\mathrm{Cov}_{\mu}(F,G)|
\le
C\,|\nabla F|_\infty|\nabla G|_\infty\,
e^{-\eta\,\mathrm{dist}(\mathrm{supp}F,\mathrm{supp}G)}
+
8\,\|F\|_\infty\|G\|_\infty\,\mu(K^c).
\tag{4.2}
\]

This is “exponent preserving” in the strongest possible sense: the exponential rate \(\eta\) is untouched. All that remains is to ensure \(\mu(K^c)\) is small enough (ideally superpolynomially small in \(|\Lambda|\), or controlled uniformly by a Lyapunov/capacity argument) so that it does not dominate in the regime of interest.

So the localization lemma cleanly separates:

* **matrix/Green’s-function analysis** (gives \(\eta\) on \(K\)),
* **global concentration/drift** (controls \(\mu(K^c)\)),

and prevents constant laundering by making the dependence explicit.

