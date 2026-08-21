# Uniqueness of Scaling Limits for Wilson Loop Expectations (Conservative Form)

This file contains the conservative uniqueness argument drafted in the chat, where continuum Wilson loop expectations are defined by lattice limits.

---

```tex
\begin{theorem}[Uniqueness of the Scaling Limit of Wilson Loop Expectations]
\label{thm:uniqueness_conservative}

Let $\mu_a$ be the gauge-fixed lattice Yang--Mills measures on 
$\mathcal{X}_a = G^{E(\Lambda_a)}$ with lattice spacing $a>0$.
Let $F$ be any gauge-invariant cylindrical observable specified by finitely
many continuum loops 
$\gamma_1,\dots,\gamma_k \subset M$ 
and a smooth function 
$f \in C^\infty((SU(N))^k)$.

For each $a>0$ define the lattice observable 
\[
F_a(U) 
=
f\bigl( U_{\gamma_1^{(a)}}(U), \dots, U_{\gamma_k^{(a)}}(U) \bigr),
\]
where $\gamma_i^{(a)}$ is a piecewise-linear lattice approximation of 
$\gamma_i$.

Assume:
\begin{itemize}
\item the sequence $\{\mu_a\}$ is tight in $H^{-s}(M)$ for $s>2$;
\item holonomy approximation: 
      $F_a \to F_b$ in $L^2(\mu_a)$ whenever $a,b$ are small;
\item uniform integrability: $\sup_a \mathbb{E}_{\mu_a}[|F_a|^p]<\infty$
      for every $p<\infty$ (from LSI and UV bounds).
\end{itemize}

Then the limit
\[
\lim_{a\to0} \int_{\mathcal{X}_a} F_a \, d\mu_a
\]
exists and is independent of the subsequence.
In particular, every cylindrical observable has a unique continuum
expectation, and the continuum Yang--Mills measure is unique.
\end{theorem}

\begin{proof}
\textbf{Step 1: Define continuum expectations by lattice limits.}
We do not evaluate $F$ on continuum fields $A \in H^{-s}(M)$.
Instead, we define its continuum expectation \emph{by}
\[
\langle F \rangle := 
\lim_{a\to0} \int F_a \, d\mu_a,
\]
provided the limit exists and is unique.  
Thus all analysis is performed explicitly on the lattice observables $F_a$.

\medskip

\textbf{Step 2: The sequence $\{\mathbb{E}_{\mu_a}[F_a]\}$ is Cauchy.}
Fix $\varepsilon>0$.
Choose $a_\varepsilon>0$ so small that for all $a,b<a_\varepsilon$:
\[
\|F_a - F_b\|_{L^2(\mu_a)} < \varepsilon/3
\quad\text{and}\quad
\mu_a(\|A\|_{H^s}>M)<\varepsilon/3
\]
for some large $M$, using holonomy approximation,
tightness, and uniform LSI bounds.

Then:
\[
\begin{aligned}
\Bigl|
\mathbb{E}_{\mu_a}[F_a] - \mathbb{E}_{\mu_b}[F_b]
\Bigr|
&\le
\Bigl|
\mathbb{E}_{\mu_a}[F_a - F_b]
\Bigr|
+
\Bigl|
\mathbb{E}_{\mu_a}[F_b] - \mathbb{E}_{\mu_b}[F_b]
\Bigr|.
\end{aligned}
\]

The first term is $<\varepsilon/3$ by the $L^2(\mu_a)$-convergence of $F_a$ to
$F_b$.
The second term is $<\varepsilon/3$ by tightness and weak convergence of
$\mu_a$ to some limit measure (Prokhorov's theorem).

Hence:
\[
|\mathbb{E}_{\mu_a}[F_a] - \mathbb{E}_{\mu_b}[F_b]|
< \varepsilon
\quad\forall a,b < a_\varepsilon,
\]
so the sequence is Cauchy.

\medskip

\textbf{Step 3: Uniqueness of the limit across subsequences.}
Let $a_n \to 0$ and $b_n\to0$ be two vanishing sequences.
By Step~2,
\[
\mathbb{E}_{\mu_{a_n}}[F_{a_n}]
-
\mathbb{E}_{\mu_{b_n}}[F_{b_n}]
\;\to\; 0.
\]
Thus all subsequences converge to the same limit.  
Hence $\langle F \rangle$ is well-defined.

\medskip

\textbf{Step 4: Wilson loops determine the measure.}
Let $\mu$ and $\mu'$ be two possible continuum limit measures.
For every cylindrical $F$,
\[
\int F \, d\mu = \langle F\rangle = \int F \, d\mu'.
\]
But finite products of Wilson loops generate a separating algebra on the
gauge-equivalence classes of connections, hence determine probability
measures uniquely on $H^{-s}(M)$.
Therefore $\mu = \mu'$.

\end{proof}
```
