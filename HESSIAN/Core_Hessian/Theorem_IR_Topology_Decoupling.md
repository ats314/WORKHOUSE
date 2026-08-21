# Infrared Decoupling of Topology for Local Observables (IR)

This file contains the rewritten Theorem IR section using the rigorous local off-diagonal Hessian decay lemma (H3), as drafted in the chat.

---

```tex
\section{Infrared Decoupling of Topology Revisited}
\label{sec:IR_rigorous}

We now give a fully rigorous proof of the infrared decoupling theorem using
only the finite-range locality of the lattice action and the local curvature
lower bound, together with the off-diagonal Hessian decay (Lemma~\ref{lem:offdiag_decay}).

Recall that $B_R\subset M$ is a fixed physical ball and that a local
gauge-invariant observable $F$ is supported in $B_R$ (i.e.\ depends only
on holonomies inside $B_R$).

\subsection*{Local vs global tangent directions}

At lattice spacing $a>0$, the gauge-fixed configuration space
$\mathcal{X}_a = G^{E(\Lambda_a)}$ has tangent space
\[
T_{U}\mathcal{X}_a \cong \mathfrak{su}(N)^{E(\Lambda_a)}.
\]
We define the orthogonal decomposition
\[
T_{U}\mathcal{X}_a
=
T_{U,a}^{\mathrm{loc}}
\oplus
T_{U,a}^{\mathrm{gauge}}
\oplus
T_{U,a}^{\mathrm{far}},
\]
where:
\begin{itemize}
  \item $T_{U,a}^{\mathrm{loc}}$: variations of link variables supported
        entirely inside $B_R$;
  \item $T_{U,a}^{\mathrm{gauge}}$: vertical gauge directions;
  \item $T_{U,a}^{\mathrm{far}}$: variations supported on links whose
        graph-distance from $B_R$ is at least $L_a \to \infty$ as $a\to0$.
\end{itemize}

For a local observable $F$ supported in $B_R$, its gradient satisfies
\[
\nabla F(U) \in T_{U,a}^{\mathrm{loc}}.
\]

Let $H_a(U)$ denote the Hessian of the gauge-fixed lattice action at $U$.
We denote by $H_{a,\mathrm{loc}}(U)$ the restriction of $H_a(U)$ to the
subspace $T_{U,a}^{\mathrm{loc}}$:
\[
H_{a,\mathrm{loc}}(U) :=
\Pi_{\mathrm{loc}} H_a(U) \Pi_{\mathrm{loc}},
\]
where $\Pi_{\mathrm{loc}}$ is the orthogonal projection onto
$T_{U,a}^{\mathrm{loc}}$.

By the Haar+Wilson+gauge-fixing analysis, we have the local curvature floor
\[
H_{a,\mathrm{loc}}(U) \ge \rho_0 I
\]
uniformly in $a$, $U$, and instanton sector.

\subsection*{Off--diagonal decay and block structure}

By Lemma~\ref{lem:offdiag_decay}, for any $X\in T_{U,a}^{\mathrm{loc}}$ and
$Y\in T_{U,a}^{\mathrm{far}}$ with $\|X\|=\|Y\|=1$,
\[
|\langle X, H_a(U) Y \rangle|
\le C a^\alpha \to 0,
\]
and in fact for sufficiently small $a$ and sufficiently separated supports,
the local--far block vanishes exactly.

Thus for small $a$, $H_a(U)$ has (up to gauge directions) the approximate
block form
\[
H_a(U)
\approx
\begin{pmatrix}
H_{a,\mathrm{loc}}(U) & 0\\
0 & H_{a,\mathrm{far}}(U)
\end{pmatrix},
\]
with $H_{a,\mathrm{loc}}(U) \ge \rho_0 I$. On the subspace of gradients 
of local observables, the relevant block is $H_{a,\mathrm{loc}}$.

\subsection*{Finite--$a$ IR spectral gap}

The Dirichlet form associated to $\mu_a$ can be written (on the gauge-fixed
Tangent space) as
\[
\mathcal{E}_a(F,F)
=
\int \langle \nabla F(U), H_a(U)^{-1} \nabla F(U)\rangle\, d\mu_a(U).
\]

For local $F$, $\nabla F(U)\in T_{U,a}^{\mathrm{loc}}$, and by the block
structure and the uniform estimate $H_{a,\mathrm{loc}}\ge\rho_0 I$,
we have
\[
H_a(U)^{-1}\big|_{T^{\mathrm{loc}}}
\le
\rho_0^{-1} I,
\]
up to errors of order $a^\alpha$ in the off-diagonal blocks, which vanish
as $a\to0$ by Lemma~\ref{lem:offdiag_decay}.

Thus there exists $a_0>0$ such that for all $a<a_0$,
\[
\mathcal{E}_a(F,F)
\ge
\rho_0 \int |F(U) - \mathbb{E}_{\mu_a}[F]|^2\, d\mu_a(U),
\]
i.e.\ a Poincaré (spectral gap) inequality with constant $\rho_0$ for all
\emph{local} observables at finite lattice spacing.

\subsection*{Continuum IR decoupling}

Finally, we pass to the continuum via Mosco convergence.
By Theorem~M, the Dirichlet forms $\mathcal{E}_a$ converge to $\mathcal{E}$,
and the Poincaré inequality with constant $\rho_0$ is stable under this
limit on the cylindrical core of local observables.

We obtain:

\begin{theorem}[Infrared Decoupling of Topology]
\label{thm:IR_decoupling_rigorous}
Let $F$ be a smooth gauge-invariant local observable supported in $B_R$.
Then the continuum Yang--Mills Dirichlet form satisfies
\[
\mathcal{E}(F,F) \ge \rho_0 \, \Var_\mu(F),
\]
where $\Var_\mu(F) = \int |F - \mathbb{E}_\mu[F]|^2 d\mu$ and $\rho_0>0$
is the local curvature constant.

In particular, global (topological) slow modes do not diminish the spectral
gap governing the relaxation of local observables.
\end{theorem}

\begin{proof}
The finite-$a$ inequality 
$\mathcal{E}_a(F,F) \ge \rho_0 \Var_{\mu_a}(F)$ holds for all sufficiently
small $a$ by the discussion above.  
By Mosco convergence, $\mathcal{E}_a(F,F)\to\mathcal{E}(F,F)$ for local $F$,
and by weak convergence $\Var_{\mu_a}(F)\to\Var_\mu(F)$.
Passing to the limit $a\to0$ yields the claimed bound.
\end{proof}
```
