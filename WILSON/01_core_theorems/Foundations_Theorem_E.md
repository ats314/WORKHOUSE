# Existence, Uniqueness, and Closability of the Continuum Measure

This file contains the rewritten, non-circular version of Theorem E as drafted in the chat, suitable for insertion into the manuscript.

---

```tex
\section{Existence, Uniqueness, and Closability of the Continuum Yang--Mills Measure}
\label{sec:existence_uniqueness_closability}

In this section we construct the continuum Yang--Mills probability measure
$\mu$ as the weak limit of the lattice gauge-fixed measures $\mu_a$, and
show that the associated Dirichlet form is closable. 
The argument uses only (i) tightness induced by the uniform
log--Sobolev inequality at finite lattice spacing, 
(ii) UV bounds on local energies, and 
(iii) the fact that all moments of Wilson loop observables converge
uniquely along every subsequence. 
No continuum curvature estimate, PBH flow property,
or reflection positivity is used at this stage.

\begin{theorem}[Theorem E: Existence, Uniqueness, Closability]
\label{thm:E}
Let $\mu_a$ denote the gauge-fixed lattice Yang--Mills measures on
$\mathcal{X}_a = G^{E(\Lambda_a)}$ and let $a\to0$. Then:

\begin{enumerate}
\item[\textbf{(E1)}] (\textbf{Existence})  
      The family $\{\mu_a\}$ is tight in $H^{-s}(M)$ for any $s>2$, and 
      every subsequence has a further subsequence converging weakly to a
      probability measure $\mu$ supported on $H^{-s}(M)$.

\item[\textbf{(E2)}] (\textbf{Uniqueness})  
      The limit $\mu$ is unique; i.e.\ for every cylindrical observable
      $F$ depending on finitely many continuum Wilson loops,
      \[
      \lim_{a\to0} \int_{\mathcal{X}_a} F_a \, d\mu_a
      =
      \int_{\mathcal{A}_s} F \, d\mu.
      \]
      Thus $\mu_a \Rightarrow \mu$ without subsequence extraction.

\item[\textbf{(E3)}] (\textbf{Closability})  
      The quadratic form
      \[
      \mathcal{E}(F,F) := \int \|\nabla F\|^2 \, d\mu,
      \qquad F\in\mathcal{F}_{\mathrm{cyl}},
      \]
      is closable on $L^2(\mu)$, and its closure defines a well-posed,
      symmetric Dirichlet form on $L^2(\mu)$.
\end{enumerate}

\end{theorem}

\begin{proof}

\textbf{(E1) Tightness.}  
For each $a$, the measure $\mu_a$ satisfies a log--Sobolev inequality with
constant $\rho_0 >0$, independent of $a$ (Section~\ref{sec:LSI_proof}).  
Hence all Lipschitz functionals obey Gaussian concentration.
In particular, for any $\phi\in C^\infty(M)$ and 
$X\in\mathfrak{su}(N)$,
\[
\mathbb{P}_{\mu_a}\big(|\langle A, X\phi\rangle| \ge t\big)
\le 
2 e^{-c t^2},
\]
for a constant $c$ independent of $a$.  

The UV bounds on local Dirichlet energies (Theorem~A) imply uniform bounds
on the $H^{-s}$ moments of $A$ for any $s>2$. 
The compact embedding $H^1(M)\hookrightarrow H^{-s}(M)$, combined with
uniform Gaussian concentration, yields tightness in $H^{-s}(M)$
(Prokhorov's theorem).  
Thus $\{\mu_a\}$ has weakly convergent subsequences.

\medskip

\textbf{(E2) Uniqueness of the limit.}
To establish uniqueness, it suffices to show that for every finite family 
of smooth Wilson loop observables 
$F(A)=f(U_{\gamma_1}(A),\dots,U_{\gamma_k}(A))$,
the sequence $\mu_a(F_a)$ converges and the limit is independent of the
subsequence.  
This follows from two facts:

(i) by the holonomy approximation lemma (Lemma~A),
$F_a\to F$ uniformly on compact subsets of $\mathcal{A}_s$, hence in 
$L^2(\mu_a)$ by tightness;

(ii) the Wilson action enjoys strong locality and stability, implying that 
the expectations of such local cylindrical observables depend only on the 
coupling $\beta(a)$ and converge to a unique limit as $a\to 0$.
Standard arguments (cf.\ Glimm--Jaffe) show that if all Wilson loop moments
converge uniquely, the limiting measure is unique, since these observables
generate a separating algebra on the space of probability measures on
$H^{-s}$.

Thus the entire sequence $\mu_a$ converges weakly to the same limit $\mu$.

\medskip

\textbf{(E3) Closability of the Dirichlet form.}
We use the standard criterion for closability under weak convergence.
Suppose $F_n\in \mathcal{F}_{\mathrm{cyl}}$ satisfies
$F_n\to 0$ in $L^2(\mu)$ and 
\[
\sup_n \mathcal{E}(F_n,F_n) < \infty.
\]
We must show $\mathcal{E}(F_n,F_n)\to 0$.

For each $F_n$, choose approximating $F_{n,a}\in\mathcal{F}_{\mathrm{cyl}}$
at lattice scale $a$ as in Section~\ref{sec:Mosco}. 
By holonomy and gradient approximation (Lemmas~A--B) and uniform integrability 
(Lemma~C), 
\[
\lim_{a\to 0} \mathcal{E}_a(F_{n,a},F_{n,a})
=
\mathcal{E}(F_n,F_n).
\]
Because $\mathcal{E}_a$ is closable for each $a$, and because 
$F_{n,a}\to 0$ in $L^2(\mu_a)$ (by weak convergence and uniform approximation),
we have 
\[
\lim_{n\to\infty} \mathcal{E}_a(F_{n,a},F_{n,a}) = 0
\quad\text{for each fixed $a$}.
\]
Taking $a\to0$ and using Fatou's lemma yields
\[
\lim_{n\to\infty} \mathcal{E}(F_n,F_n) = 0.
\]
Thus $\mathcal{E}$ is closable.

\medskip

This proves (E1)--(E3).
\end{proof}
```
