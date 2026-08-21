# Closability of the Continuum Dirichlet Form

This file contains the non-circular version of Lemma M3 (closability), as drafted in the chat.

---

```tex
\begin{lemma}[Closability of the Continuum Dirichlet Form]
\label{lem:closability}
Let $\mu_a \Rightarrow \mu$ be the weak limit established in Theorem~E.
Define the quadratic form
\[
\mathcal{E}(F,F)
:=
\int_{\mathcal{A}_s}
\|\nabla F(A)\|^2 \, d\mu(A),
\qquad
F \in \mathcal{F}_{\mathrm{cyl}}.
\]
Then $\mathcal{E}$ is closable on $L^2(\mu)$.

More precisely: if $(F_n)\subset\mathcal{F}_{\mathrm{cyl}}$ satisfies
\[
F_n \to 0 \quad\text{in } L^2(\mu),
\qquad
\sup_n \mathcal{E}(F_n,F_n) < \infty,
\]
then
\[
\mathcal{E}(F_n,F_n) \longrightarrow 0.
\]
Thus the closure of $\mathcal{E}$ is a densely defined, symmetric,
Markovian Dirichlet form on $L^2(\mu)$.
\end{lemma}

\begin{proof}
Let $(F_n)$ be a sequence as above.

\emph{Step 1: Approximate $F_n$ by lattice functionals.}
For each $n$ and lattice spacing $a$, let $F_{n,a}$ be the lattice
cylindrical approximation constructed from polygonal approximations of 
the underlying loops.  
By Lemmas A--C (holonomy, gradient convergence, and uniform integrability),
\[
F_{n,a} \to F_n \quad\text{in } L^2(\mu),
\qquad
\mathcal{E}_a(F_{n,a},F_{n,a}) \to \mathcal{E}(F_n,F_n),
\]
and the convergence is uniform on bounded-energy sequences.

\emph{Step 2: Use closability at finite lattice spacing.}
For each fixed $a>0$, the form $\mathcal{E}_a$ is the gradient form of a 
finite-dimensional diffusion on $G^{E(\Lambda_a)}$ with smooth density;
hence $\mathcal{E}_a$ is closable.

Since $F_n \to 0$ in $L^2(\mu)$, we also have
$F_{n,a}\to 0$ in $L^2(\mu_a)$ for small enough $a$
(by weak convergence of $\mu_a$ and uniform convergence of $F_{n,a}$ on 
compact sets).  
Therefore closability of $\mathcal{E}_a$ yields
\[
\mathcal{E}_a(F_{n,a},F_{n,a})
\;\longrightarrow\; 0
\qquad\text{as } n\to\infty
\quad\text{for each fixed } a.
\]

\emph{Step 3: Pass $a\to 0$.}
Fix $\varepsilon>0$.
Choose $a$ sufficiently small so that the approximation property gives
\[
|\mathcal{E}_a(F_{n,a},F_{n,a}) - \mathcal{E}(F_n,F_n)|
< \varepsilon
\qquad\text{for all large } n.
\]
Then for these $n$,
\[
\mathcal{E}(F_n,F_n)
\;\le\;
\mathcal{E}_a(F_{n,a},F_{n,a}) + \varepsilon.
\]
Letting $n\to\infty$ and using $\mathcal{E}_a(F_{n,a},F_{n,a})\to 0$
yields $\limsup_n \mathcal{E}(F_n,F_n) \le \varepsilon$.
Since $\varepsilon$ was arbitrary, the limit is zero.

This proves closability.
\end{proof}
```
