# Extract 06 — Localization Algebra: Turning Conditional Clustering into Unconditional Clustering

\begin{center}
\textbf{Theme:} a clean, reusable covariance identity that lets you prove things on a “good event” $K$ and then safely export them to the full measure $\mu$.
\end{center}

## 0. Why this matters

A recurring headache in rigorous statistical mechanics and constructive field theory is:

- you can prove strong convexity / spectral gaps / kernel decay only on a *typical* set $K$ (small-field region, high-curvature region, “good geometry” region, etc.),
- but your real observable of interest lives under the *full* Gibbs measure $\mu$.

**Appendix I** provides the exact algebra you need to bridge that gap.

The core idea: if $\mu(K^c)$ is tiny (typically exponentially small in volume), then any covariance bound proved under the conditional law $\mu(\cdot\mid K)$ becomes a bound under $\mu$ with an explicit, controlled error term.

This is the kind of “boring-looking lemma” that becomes the keystone of an entire mass-gap/clustering pipeline.

---

## 1. Setting

Let $(\Omega,\mathcal F,\mu)$ be a probability space and let $K\in\mathcal F$ satisfy
\[
0<\mu(K)<1.
\]
Define conditional measures
\[
\mu_K(A):=\mu(A\mid K)=\frac{\mu(A\cap K)}{\mu(K)},
\qquad
\mu_{K^c}(A):=\mu(A\mid K^c)=\frac{\mu(A\cap K^c)}{\mu(K^c)}.
\]
For integrable observables $F,G: \Omega\to\mathbb R$, define
\[
\mathrm{Cov}_\nu(F,G):=\nu(FG)-\nu(F)\,\nu(G)
\]
and the **conditional mean jump** across $K$
\[
\Delta_K F := \mu_K(F)-\mu_{K^c}(F),
\qquad
\Delta_K G := \mu_K(G)-\mu_{K^c}(G).
\]

---

## 2. Covariance decomposition across an event

Because $\mu$ is the mixture
\[
\mu = \mu(K)\,\mu_K + \mu(K^c)\,\mu_{K^c},
\]
expectations split as
\[
\mu(F)=\mu(K)\mu_K(F)+\mu(K^c)\mu_{K^c}(F),
\quad
\mu(G)=\mu(K)\mu_K(G)+\mu(K^c)\mu_{K^c}(G),
\]
and similarly for $\mu(FG)$. Expanding
\(
\mu(FG)-\mu(F)\mu(G)
\)
then gives the exact identity
\[
\boxed{
\mathrm{Cov}_\mu(F,G)
=
\mu(K)\,\mathrm{Cov}_{\mu_K}(F,G)
+
\mu(K^c)\,\mathrm{Cov}_{\mu_{K^c}}(F,G)
+
\mu(K)\mu(K^c)\,\Delta_K F\,\Delta_K G.
}
\]

Interpretation:

- the first term is the “good” covariance you actually know how to estimate,
- the second term is “whatever happens on the bad set,”
- the third term is the **mixture penalty**: if $F$ and $G$ have different conditional means on $K$ vs $K^c$, mixing them creates covariance even if each component were independent.

---

## 3. A crude but universal localization error bound (sup norm)

A cheap but effective bound is obtained by:

1. bounding the bad-set covariance in sup norm, and
2. bounding the mean-jump terms by sup norms.

### 3.1 Universal sup-norm covariance bound

For any probability measure $\nu$ and bounded $F,G$,
\[
|\mathrm{Cov}_\nu(F,G)|
\le 4\,\|F\|_\infty\,\|G\|_\infty.
\]
This is a one-line consequence of
\(
\mathrm{Cov}_\nu(F,G)=\nu\big((F-\nu(F))(G-\nu(G))\big)
\)
plus $\|F-\nu(F)\|_\infty\le 2\|F\|_\infty$.

### 3.2 Bounding the mean jump

For bounded $F$,
\[
|\Delta_K F|
=|\mu_K(F)-\mu_{K^c}(F)|
\le |\mu_K(F)|+|\mu_{K^c}(F)|
\le 2\|F\|_\infty,
\]
and similarly $|\Delta_K G|\le 2\|G\|_\infty$.

### 3.3 Result

Insert these into the decomposition to get
\[
\boxed{
|\mathrm{Cov}_\mu(F,G)|
\le
|\mathrm{Cov}_{\mu_K}(F,G)|
+
8\,\|F\|_\infty\,\|G\|_\infty\,\mu(K^c).
}
\]

This is “raw” (sup norm is usually pessimistic), but it is extremely robust:

- it needs zero geometry,
- it needs zero convexity,
- it needs only that $\mu(K^c)$ is small.

---

## 4. How this plugs into the project’s mass-gap / clustering story

In the lattice gauge part of the project, the workflow is:

1. Use geometric/analytic tools to prove a **conditional** exponential clustering bound on $K_{\Lambda_L}$:
   \[
   |\mathrm{Cov}_{\mu_{\Lambda_L,\beta}(\cdot\mid K_{\Lambda_L})}(F,G)|
   \lesssim
   e^{-\eta\,\mathrm{dist}(\mathrm{supp}\,F,\mathrm{supp}\,G)}.
   \]
2. Use a **typicality mechanism** (Appendix J) to show
   \[
   \mu_{\Lambda_L,\beta}(K_{\Lambda_L}^c)
   \le
   \exp\big(-c_{\mathrm{typ}}\,|P(\Lambda_L)|\big),
   \]
   i.e. the bad event has exponentially small probability in volume.
3. Apply the localization inequality above to convert (1) into an unconditional bound with a remainder term
   \(
   O(\mu(K_{\Lambda_L}^c))
   \)
   that vanishes as $L\to\infty$.

In other words: **Appendix I is the exact algebraic checkpoint where “typicality” becomes “physics.”**

---

## 5. What could be pushed further

This is a good place to sharpen the knife:

1. **Replace sup-norm by $L^2$ or Orlicz norms.**
   Sup norm is stable but wasteful. If one can bound $\Delta_K F$ in variance or entropy terms, the constants improve and the error can become distance-sensitive.

2. **Two-event / multi-event decompositions.**
   In many RG/localization arguments you naturally get a hierarchy of good sets $K_1\supset K_2\supset\dots$; a multi-level decomposition can yield better bookkeeping.

3. **Distance-dependent error terms.**
   The sup-norm bound produces an error independent of separation. If $K^c$ is localized (e.g. “bad plaquettes are sparse”), one might upgrade the $\mu(K^c)$ term to something decaying with distance between supports.

4. **Generalization to non-product conditioning.**
   Conditioning on $K$ is the simplest cut. In some gauge models one wants conditioning on sigma-algebras associated with blocks, which leads to martingale-covariance decompositions (Efron–Stein style).

---

## 6. Mini “why it feels novel” note

The identities themselves are measure-theoretic classics. The novelty here is \textbf{architectural}: in this project they function as the formal interface between

- geometric convexity on a high-probability small-field region,
- analytic inverse-decay bounds (Combes–Thomas / Davies),
- and OS reconstruction that extracts a Hamiltonian gap from Euclidean clustering.

That three-way splice is not standard textbook fare; it’s a pretty elegant blueprint.
