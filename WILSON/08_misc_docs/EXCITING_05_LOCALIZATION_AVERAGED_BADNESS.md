# Exciting Extract 05: Localization via an averaged plaquette badness constraint (and why the \(|P|^{-1/2}\) Lipschitz scaling is the right normalization)

This note extracts the localization bookkeeping that upgrades a **good-set** covariance estimate to a full Gibbs covariance estimate, and the geometric reason the canonical event is chosen as an *average* over plaquettes (rather than a maximum).

---

## 1. Covariance decomposition across an event

Let \((\Omega,\mathcal F,\mu)\) be a probability space and let \(K\in\mathcal F\) satisfy \(0<\mu(K)<1\). Define conditional measures
\[
\mu_K(\cdot):=\mu(\cdot\mid K),\qquad \mu_{K^c}(\cdot):=\mu(\cdot\mid K^c).
\]
For bounded \(F,G\), write \(\mathrm{Cov}_\nu(F,G)=\nu(FG)-\nu(F)\nu(G)\).

**Lemma 1.1 (law of total covariance, explicit form).**
\[
\mathrm{Cov}_\mu(F,G)
=
\mu(K)\,\mathrm{Cov}_{\mu_K}(F,G)
+
\mu(K^c)\,\mathrm{Cov}_{\mu_{K^c}}(F,G)
+
\mu(K)\mu(K^c)\,\Delta_KF\,\Delta_KG,
\tag{1.1}
\]
where
\[
\Delta_KF:=\mu_K(F)-\mu_{K^c}(F),\qquad \Delta_KG:=\mu_K(G)-\mu_{K^c}(G).
\tag{1.2}
\]

A quick and useful corollary is the raw error bound:

**Corollary 1.2 (localization error in terms of \(\mu(K^c)\)).**
\[
|\mathrm{Cov}_\mu(F,G)|
\le
|\mathrm{Cov}_{\mu_K}(F,G)|
+
8\,\|F\|_\infty\|G\|_\infty\,\mu(K^c).
\tag{1.3}
\]
So: if we can bound \(\mu(K^c)\) strongly enough, the complement contributes only a *distance-independent* additive error.

---

## 2. Canonical choice of \(K\): averaged plaquette badness

In the lattice gauge application, \(\Omega=M_\Lambda=G^{E(\Lambda)}\) and \(\mu=\mu_\Lambda\) is the Gibbs measure.

### 2.1 A conjugation-invariant plaquette badness interface

Fix \(\vartheta:G\to[0,\infty)\) with:
- \(\vartheta\in C^1(G)\),
- conjugation invariant: \(\vartheta(hgh^{-1})=\vartheta(g)\),
- \(\vartheta(\mathbf 1)=0\),
- bounded gradient: \(\|\nabla_G\vartheta\|_\infty<\infty\).

For each plaquette \(p\), define
\[
\vartheta_p(U):=\vartheta(U_p(U)).
\]

### 2.2 Averaged badness and the canonical event

Define
\[
\mathcal B_\Lambda(U):=\frac{1}{|P(\Lambda)|}\sum_{p\in P(\Lambda)}\vartheta_p(U),
\qquad
K_\Lambda(\varepsilon):=\{\mathcal B_\Lambda\le \varepsilon\}.
\tag{2.1}
\]

**Gauge invariance.** Because \(U_p\) transforms by conjugation under gauge transformations, \(\vartheta_p\) is gauge invariant, hence so are \(\mathcal B_\Lambda\) and \(K_\Lambda(\varepsilon)\).

**Why average, not max?** A max-event \(\{\max_p\vartheta_p\le\varepsilon\}\) has a complement controlled only by a union bound, typically producing a factor \(|P(\Lambda)|\). That factor is exactly what later poisons uniform bounds.

The average has a built-in variance suppression: its Lipschitz constant is order \(|P|^{-1/2}\).

---

## 3. Lipschitz scaling: \(\mathcal B_\Lambda\) is \(O(|P|^{-1/2})\)-Lipschitz

Write the product gradient as a sum of link-gradients:
\[
|\nabla f|^2 = \sum_{\ell\in E(\Lambda)}|\nabla_\ell f|^2.
\]

Because each \(\vartheta_p\) depends on only four links and the metric is bi-invariant, for any link \(\ell\),
\[
|\nabla_\ell \vartheta_p(U)| \le \|\nabla_G\vartheta\|_\infty\,\mathbf 1_{\{\ell\in\partial p\}}.
\tag{3.1}
\]

Differentiate the average:
\[
\nabla_\ell\mathcal B_\Lambda(U)=\frac{1}{|P|}\sum_{p:\,\ell\in\partial p}\nabla_\ell\vartheta_p(U).
\tag{3.2}
\]
If \(\deg_P(\ell)\) is the number of plaquettes containing \(\ell\), then \(\deg_P(\ell)\le \nu\) (bounded overlap), hence
\[
|\nabla_\ell\mathcal B_\Lambda(U)|
\le \frac{\nu}{|P|}\,\|\nabla_G\vartheta\|_\infty.
\tag{3.3}
\]
Summing over links and using \(|E|/|P|=O(1)\) on the periodic hypercubic lattice gives:

**Lemma 3.1 (Lipschitz constant).**  
There exists \(L_0<\infty\), independent of \(\Lambda\), such that
\[
\sup_U|\nabla\mathcal B_\Lambda(U)|
\ \le\ \frac{L_0}{\sqrt{|P(\Lambda)|}}.
\tag{3.4}
\]

This is the geometric backbone for typicality: averaging produces the correct normalization.

---

## 4. Typicality via a volume-uniform concentration mechanism (what is needed)

The localization error in (1.3) is useful only if \(\mu_\Lambda(K_\Lambda(\varepsilon)^c)\) is small enough.

A standard route is: if \(\mu_\Lambda\) satisfies a log-Sobolev inequality (LSI) with constant \(C_{\mathrm{LSI}}\) uniform in \(\Lambda\), then any \(L\)-Lipschitz \(f\) satisfies Gaussian concentration:
\[
\mu_\Lambda\big(f-\mu_\Lambda f\ge t\big)\le \exp\!\Big(-\frac{t^2}{2C_{\mathrm{LSI}}L^2}\Big).
\tag{4.1}
\]
Applying (4.1) to \(f=\mathcal B_\Lambda\) and using \(L\sim |P|^{-1/2}\) gives tails of the form
\[
\mu_\Lambda\big(\mathcal B_\Lambda-\mu_\Lambda\mathcal B_\Lambda \ge t\big)
\le \exp\!\big(-c\,t^2\,|P(\Lambda)|\big),
\tag{4.2}
\]
exactly the scale needed to make the error term in (1.3) negligible without spoiling distance exponents.

### Where the project is honest about a remaining gap

The draft’s dependency ledger flags that, while **global Poincaré** can be obtained via Lyapunov patching under reasonable drift assumptions, a **global LSI** (or an SPI\(\Rightarrow\)LSI conversion theorem) is not yet fully closed in the chain. There are two possible continuations:

- Prove a global LSI (or a suitable concentration inequality) with uniform constants, and then (4.2) is automatic.
- Redesign the localization step to require only Poincaré/drift/capacity estimates, giving weaker but still sufficient control of \(\mu(K^c)\).

---

## 5. What could be developed further

This localization framework suggests an intriguing general philosophy:

> If the “good set” needed for a hard analytic bound is defined by a *spatial average* of a local gauge-invariant defect functional, then the manifold/product geometry plus bounded overlap gives \(|P|^{-1/2}\) Lipschitz scaling “for free,” and concentration becomes a functional-inequality problem rather than a combinatorial union-bound problem.

The real creative space is in optimizing:
- the choice of \(\vartheta\) (to best match the good-set analytic mechanism),
- the concentration mechanism (LSI vs capacity/drift),
- and the error-vs-distance balance needed for exponential clustering.
