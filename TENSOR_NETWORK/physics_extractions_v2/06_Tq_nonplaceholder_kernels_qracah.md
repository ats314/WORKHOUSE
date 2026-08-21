---
title: "Replacing placeholder kernels in $T_q$ by honest $q$-Racah / $q$-6$j$ data"
date: "2025-12-28"
---

## 0. The problem with the prototype $T_q$

The prototype transfer operator in the notebook is structurally great:

\[
T_q
=
\Lambda^{\top}\,e^{Q}\,\Lambda\;R\;W_I,
\]

but two pieces were explicitly placeholders:

- $R(\chi,\chi')\approx \exp(-|\chi-\chi'|(1-q))$,
- $\Lambda$ a Gaussian smearing between a continuous boundary grid and the bulk label $n$.

This note gives **two non-placeholder replacements** that keep the architecture but turn it into something you can analyze.

---

## 1. First replacement: build $\Lambda$ from the *actual* spectral transform of $H$

### 1.1 Orthogonal diagonalization data is already a kernel

Because $H$ is real symmetric, it has an orthonormal eigenbasis:
\[
H U = U \,\mathrm{diag}(E_x),\qquad U^\top U=I.
\]

For a Jacobi operator tied to $q$-Racah data, those eigenvectors can be written (up to normalization)
in terms of $q$-Racah polynomials evaluated on the discrete spectral set $x\in\{0,\dots,N\}$.

Define the boundary label to *be* this spectral index $x$ and set

\[
\boxed{\Lambda := D^{-1}U},
\qquad D=\mathrm{diag}(\psi_0),
\]
so that columns of $\Lambda$ are eigenvectors of the Doob generator $Q$:

\[
Q\Lambda = \Lambda\,\mathrm{diag}\big(-(E_x-E_0)\big).
\]

Then the bulk step becomes diagonal in this boundary basis:
\[
\boxed{
\Lambda^\top e^{Q}\Lambda = \mathrm{diag}\big(e^{-(E_x-E_0)}\big).
}
\]

This is not a hack; it is the exact spectral representation of the bulk evolution.

**Why this matters:** once $\Lambda$ is chosen this way, every other kernel you insert is “the only place”
where nontrivial physics can hide. You’ve isolated the degrees of freedom.

---

## 2. Second replacement: choose $R$ to be an honest $q$-Racah recoupling kernel

There are two very natural “boundary bases” in a spin-network / tensor category setting:

1. a basis labeled by one intermediate coupling channel,
2. a basis labeled by a different coupling channel.

The change-of-basis matrix between those two is the **$F$-move** (a $6j$ symbol).  
For $U_q(\mathfrak{su}(2))$ at generic $q$, that $F$-move is a **quantum $6j$**, and its entries are expressible in terms of **$q$-Racah polynomials**.

So the non-placeholder choice is:

\[
\boxed{
R_{x y}
=
(-1)^{\sigma}\,
\sqrt{[2x+1]_q\,[2y+1]_q}\;
\left\{\begin{matrix}
a&b&x\\ c&d&y
\end{matrix}\right\}_q,
}
\]

where:

- $a,b,c,d$ are fixed external spins (boundary data),
- $x,y$ are the two intermediate channel labels (running over an admissible finite range),
- $[n]_q$ is the standard $q$-integer,
- the quantum $6j$ is the **unitary recoupling kernel**.

This $R$ is:

- finite-dimensional,
- (after the right normalization conventions) unitary/orthogonal,
- representation-theoretic (not a smoothing ansatz).

In the “polynomial language”, the same statement is: $R$ is the orthonormal matrix whose entries are normalized $q$-Racah polynomials:
\[
R_{x y} \propto \frac{R_x(\lambda(y))}{\sqrt{h_x}}\,\sqrt{w(y)}.
\]

Either way, you’ve replaced the exponential placeholder by the actual recoupling move.

---

## 3. Wilson insertion $W_I$: make it a character, not a monomial

The notebook used
\[
(W_I)_{kk} = z(\chi_k)^I,\qquad z=\chi+\chi^{-1}.
\]

A more faithful (and still simple) choice is to use the **character recursion** (fusion ring) of $\mathrm{SU}(2)$,
which survives for generic $U_q(\mathfrak{su}(2))$:

Let $X$ be the fundamental character variable (classically $X=2\cos\theta$; in the toy you can take $X=z$).
Define polynomials $\chi_I(X)$ by

\[
\chi_0(X)=1,\qquad \chi_{1/2}(X)=X,\qquad
\chi_{I+1/2}(X)=X\,\chi_I(X)-\chi_{I-1/2}(X).
\]

Then set
\[
\boxed{
(W_I)_{xx} := \chi_I\big(X_x\big),
}
\]
where $X_x$ is the boundary spectral coordinate associated to label $x$
(e.g. $X_x=\lambda(x)$ in the standard $q$-Racah parametrization, or $X_x=\chi_x+\chi_x^{-1}$ if you choose a multiplicative coordinate).

This replacement is minimal but conceptually important: it enforces the correct representation-ring structure.

---

## 4. The resulting non-placeholder transfer operator

With those choices, the composite operator becomes

\[
\boxed{
T_q
=
\underbrace{\Lambda^{\top} e^{Q}\Lambda}_{\text{diagonal bulk decay}}
\;
\underbrace{R}_{\text{true recoupling / $6j$}}
\;
\underbrace{W_I}_{\text{character insertion}}.
}
\]

If you keep the spectral boundary basis (so that $\Lambda^\top e^{Q}\Lambda$ is diagonal),
the only nontrivial mixing is $R W_I$.

If instead you keep the “geometric boundary basis” (where $W_I$ is diagonal),
then $R$ is the thing that transports the Wilson insertion into the channel where bulk propagation is diagonal.

That is exactly what you want in a transfer-matrix picture.

---

## 5. Immediate analytic payoff: crude but clean spectral bounds for $T_q$

If $R$ is unitary/orthogonal and $\Lambda$ is an isometry (as above), then operator norms satisfy

\[
\|T_q\| \le \| \Lambda^\top e^{Q}\Lambda\|\;\|W_I\|
= \max_x e^{-(E_x-E_0)}\;\max_x |\chi_I(X_x)|.
\]

Moreover, the bulk gap $m=E_1-E_0$ implies
\[
\max_{x\ne 0} e^{-(E_x-E_0)} \le e^{-m}.
\]

So as long as the Wilson insertion doesn’t blow up with truncation, you inherit an **exponential suppression scale**
directly from the bulk gap.

This is the first place where “mass gap surrogate $\Rightarrow$ Wilson observable decay” becomes an actual inequality,
not a vibe.

---

## 6. What to do next (the “audacity pipeline”)

1. Choose a concrete recoupling problem (fixed boundary spins $a,b,c,d$) and implement $R$ from an actual $q$-6$j$ routine.
2. Choose the boundary spectral coordinate $X_x$ so that characters are bounded on the admissible range.
3. Measure how the leading ratio $|\mu_1|/|\mu_0|$ of $T_q$ scales with:
   - $q\uparrow 1$,
   - truncation (spin cutoff),
   - Wilson representation $I$.
4. Prove (or disprove) a uniform-in-truncation gap lower bound for $Q$ in the same parameter regime.

That’s the route from “prototype” to “operator-theoretic confinement toy model”.

