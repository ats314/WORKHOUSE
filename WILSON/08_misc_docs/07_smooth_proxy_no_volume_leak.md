# Smooth plaquette proxies and the “no $O(|P|)$ leakage” trick

\begin{abstract}
A recurring technical failure in Lyapunov drift / localization arguments on large product manifolds is accidentally producing an $O(|P(\Lambda)|)$ contribution from Laplacians or second-derivative terms when summing local quantities over plaquettes. This note records the key mitigation used in the appendices: choose a globally smooth plaquette proxy $\tilde z(g)$ and a Lyapunov aggregation $V_\Lambda=\sum_p \Phi(\tilde z_p)$ with $\Phi'(0)=0$, so that any Laplacian term automatically carries a factor of $\tilde z_p$ and cannot sum to $O(|P|)$.
\end{abstract}

## 1. The setup

Let $M_\Lambda=G^{E(\Lambda)}$ be the configuration manifold and let
\[
L_\Lambda f = \Delta_\Lambda f - \langle \nabla S_\Lambda, \nabla f\rangle
\]
be the symmetric diffusion generator with respect to the Gibbs measure $\mu_\Lambda\propto e^{-S_\Lambda} d\mathrm{vol}$.

For each plaquette $p$, define a **globally smooth**, conjugation-invariant proxy $\tilde z_p(U)=\tilde z(U_p(U))\ge 0$ where $\tilde z:G\to\mathbb R_+$ is smooth everywhere (no cut locus) and satisfies $\tilde z(e)=0$ and $\tilde z(g)\asymp \|\log g\|^2$ near $e$.

## 2. Lyapunov aggregation and the dangerous term

Take an aggregation
\[
V_\Lambda(U):=\sum_{p\in P(\Lambda)} \Phi(\tilde z_p(U)),
\]
with $\Phi\in C^2(\mathbb R_+)$ nonnegative. For drift, one expands
\[
L_\Lambda V_\Lambda = \sum_p \Big( \Phi'(\tilde z_p)L_\Lambda \tilde z_p + \Phi''(\tilde z_p)\,\Gamma_\Lambda(\tilde z_p)\Big).
\]
The problematic contribution is the Laplacian piece
\(
\sum_p \Phi'(\tilde z_p)\,\Delta_\Lambda \tilde z_p
\),
because if $\Delta_\Lambda\tilde z_p$ is only bounded by a constant, summing over $p$ can yield an unwanted $O(|P|)$.

## 3. The trick: impose $\Phi'(0)=0$

If $\Phi'(0)=0$ and $\Phi'$ is Lipschitz, then $\Phi'(\tilde z_p)$ carries a factor $\tilde z_p$ (near $0$), which is precisely the “smallness weight” needed for volume-uniform control.

The simplest (and used in the appendices) is
\[
\Phi(s)=s^2 \quad\Rightarrow\quad \Phi'(s)=2s.
\]

## 4. A representative lemma (no-volume leakage)

Assume that for each plaquette $p$ and all configurations $U$, one has a uniform bound
\[
|\Delta_\Lambda \tilde z_p(U)|\le C_\Delta,
\]
where $C_\Delta$ depends on $G$ and the proxy but **not** on $\Lambda$.
This holds because $(X_\ell^a)^2\tilde z_p\equiv 0$ unless $\ell\in\partial p$, so only a bounded number of link-derivatives contribute to $\Delta_\Lambda$.

Then for $\Phi(s)=s^2$,
\[
\sum_{p\in P(\Lambda)} \Phi'(\tilde z_p)\,\Delta_\Lambda \tilde z_p
=2\sum_p \tilde z_p\,\Delta_\Lambda \tilde z_p
\le 2C_\Delta \sum_p \tilde z_p.
\]
Crucially, there is **no** naked $\sum_p 1 = |P|$ term.

## 5. Why this matters

This single weighting choice (
$\Phi'(0)=0$
) prevents a common catastrophic bookkeeping error in Lyapunov programs: turning a local differential bound into a volume-divergent drift term.

It does *not* by itself close the remaining “pairing-term coercivity” gap (the term involving $\langle \nabla S_\Lambda, \nabla \tilde z_p\rangle$), but it means any failure there is a genuine coercivity issue, not a hidden volume leak.
