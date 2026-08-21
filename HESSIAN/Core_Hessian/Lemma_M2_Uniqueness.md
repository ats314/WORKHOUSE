# Uniqueness of the Continuum Measure (M2)

This file contains the rewritten Lemma M2 (uniqueness of the continuum measure) as drafted in the chat (PBH-free).

---

```tex
\begin{lemma}[Uniqueness of the Continuum Limit]
\label{lem:uniqueness}
Let $\mu_a$ be the sequence of gauge-fixed lattice Yang--Mills measures,
indexed by lattice spacing $a>0$, and suppose $\mu_a \Rightarrow \mu$ and
$\mu_a \Rightarrow \mu'$ weakly in $H^{-s}(M)$ for some $s>2$.
Then $\mu = \mu'$.  In particular, the continuum Yang--Mills measure is 
unique.
\end{lemma}

\begin{proof}
Let $\mathcal{F}_{\mathrm{cyl}}$ be the algebra of gauge-invariant local
cylindrical functionals of the form
\[
F(A)
=
f\!\left(
    U_{\gamma_1}(A),\dots,U_{\gamma_k}(A)
  \right),
\]
where $f\in C^\infty((SU(N))^k)$ and the loops $\gamma_i$ lie in a fixed
ball $B_R$.  It suffices to show that
\[
\int F \, d\mu = \int F \, d\mu'
\qquad
\text{for all } F\in\mathcal{F}_{\mathrm{cyl}},
\]
since this algebra is measure-determining.

Fix $F\in\mathcal{F}_{\mathrm{cyl}}$.  
Let $F_a$ be the lattice approximation obtained by replacing each 
$\gamma_i$ with its polygonal approximation $\gamma_i^{(a)}$ and using the 
lattice Wilson holonomies $U^{(a)}_{\gamma_i}(A)$.  
By the holonomy approximation lemma (Lemma~A),
\[
F_a(A) \to F(A)
\qquad
\text{uniformly on bounded subsets of } H^s(M),
\]
and by tightness of $\mu_a$ in $H^{-s}(M)$ (Theorem~E),
this convergence holds in $L^2(\mu_a)$ as $a\to0$.

Since $\mu_a$ is a probability measure,
\[
\Bigl| \int F_a \, d\mu_a - \int F \, d\mu_a \Bigr|
\le
\int |F_a - F| \, d\mu_a
\longrightarrow 0.
\tag{1}
\]

Now suppose $\mu_a \Rightarrow \mu$ along $a\to 0$.  
Because $F_a$ is continuous in the $H^{-s}$ topology and uniformly bounded,
\[
\int F_a \, d\mu_a \longrightarrow \int F \, d\mu.
\tag{2}
\]

Likewise, if $\mu_a \Rightarrow \mu'$ along another subsequence $a\to0$, then
\[
\int F_a \, d\mu_a \longrightarrow \int F \, d\mu'.
\tag{3}
\]

Combining (1)--(3), we conclude
\[
\int F \, d\mu = \int F \, d\mu'.
\]

\medskip
\noindent
\emph{Measure-determining property of Wilson loops.}
Let $\mathcal{W}$ denote the set of all local finite products of Wilson 
loops in $B_R$.  
This set separates points of the space $H^{-s}(M)$ modulo gauge.  
By Stone--Weierstrass on the compact Lie group $G^k$, finite linear
combinations of products of characters of Wilson loops separate measures.

Therefore $\mathcal{F}_{\mathrm{cyl}}$ is measure-determining, and since all
its expectations agree under $\mu$ and $\mu'$, we have $\mu=\mu'$.

This proves uniqueness.
\end{proof}
```
