# Localization bookkeeping: covariance decomposition across an event

\begin{abstract}
This note records the exact “law of total covariance” decomposition used to upgrade a conditional (good-set) covariance bound to an unconditional bound under the full Gibbs measure. The payoff is an explicit, *distance-independent* error term proportional to $\mu(K^c)$.
\end{abstract}

## 1. Setting

Let $(\Omega,\mathcal F,\mu)$ be a probability space and let $K\in \mathcal F$ satisfy $0<\mu(K)<1$. Define the conditional measures
\[
\mu_K(H):=\mu(H\mid K)=\frac{\mu(H\cap K)}{\mu(K)},
\qquad
\mu_{K^c}(H):=\mu(H\mid K^c)=\frac{\mu(H\cap K^c)}{\mu(K^c)}.
\]
For integrable $F,G$, define
\[
\mathrm{Cov}_\nu(F,G) := \nu(FG)-\nu(F)\nu(G).
\]

## 2. Exact identity

\begin{lemma}[Covariance decomposition across an event]
For any bounded measurable $F,G$, writing $\alpha:=\mu(K)$,
\[
\mathrm{Cov}_\mu(F,G)
=
\alpha\,\mathrm{Cov}_{\mu_K}(F,G)
+(1-\alpha)\,\mathrm{Cov}_{\mu_{K^c}}(F,G)
+\alpha(1-\alpha)\,(\Delta_K F)\,(\Delta_K G),
\]
where
\[
\Delta_K F := \mu_K(F)-\mu_{K^c}(F),
\qquad
\Delta_K G := \mu_K(G)-\mu_{K^c}(G).
\]
\end{lemma}

\begin{proof}
Use the convex decomposition $\mu = \alpha\mu_K + (1-\alpha)\mu_{K^c}$ and expand
$\mu(FG)-\mu(F)\mu(G)$; the cross term simplifies to $\alpha(1-\alpha)(\mu_K(F)-\mu_{K^c}(F))(\mu_K(G)-\mu_{K^c}(G))$.
\end{proof}

## 3. A raw but useful error bound

\begin{corollary}[Localization error in terms of $\mu(K^c)$]
For bounded measurable $F,G$,
\[
|\mathrm{Cov}_\mu(F,G)|
\le
|\mathrm{Cov}_{\mu_K}(F,G)|
+8\,\|F\|_\infty\,\|G\|_\infty\,\mu(K^c).
\]
\end{corollary}

\begin{proof}
From the identity, use:
(i) $|\mathrm{Cov}_\nu(F,G)|\le 4\|F\|_\infty\|G\|_\infty$ for any probability measure $\nu$, and
(ii) $|\Delta_KF|\le 2\|F\|_\infty$, $|\Delta_KG|\le 2\|G\|_\infty$.
\end{proof}

## 4. How it plugs into the mass-gap chain

If Part 6 gives an exponential-in-distance bound on $\mathrm{Cov}_{\mu_K}(F,G)$ (via Helffer--Sj"ostrand plus Green kernel decay), then the only obstruction to upgrading it to $\mu$ is arranging that $\mu(K^c)$ is small enough.

The key bookkeeping point: the localization error term is distance-independent, so to preserve an exponent $e^{-\eta\,\mathrm{dist}}$ you need $\mu(K^c)$ to be negligible in the regimes where distances are large (e.g. exponentially small in volume, or controlled in a way that does not scale with separation).
