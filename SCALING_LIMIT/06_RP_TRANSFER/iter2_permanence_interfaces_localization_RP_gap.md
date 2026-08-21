# Permanence Interfaces for the YM Program: Localization, Reflection Positivity, and Gap Stability

\newcommand{\dd}{\mathrm{d}}
\newcommand{\Id}{\mathrm{Id}}
\newcommand{\Cov}{\mathrm{Cov}}
\newcommand{\EE}{\mathbb{E}}
\newcommand{\RR}{\mathbb{R}}
\newcommand{\CC}{\mathbb{C}}

## Abstract

This document collects **three permanence mechanisms** that are foundational specifically because they allow new theory-building: they make it possible to push fixed-cutoff statements to larger volumes, to conditional/unconditional measures, and to continuum limits without turning key steps into folklore.

The mechanisms are:

1. **Covariance decomposition across an event** (localization algebra): exact identities that convert conditional bounds into unconditional bounds with explicit tail errors.
2. **Reflection positivity preservation** under projection/coarse-graining: conditions under which OS positivity survives when restricting to subalgebras or pushing forward measures.
3. **Gap stability under monotone limits** of positive operators: a functional-analytic lemma that makes “gap permanence” a theorem once one has uniform lower quadratic-form bounds.

All statements are given with proofs and with minimal hypotheses.

---

## 1. Localization algebra: covariance decomposition across an event

Let $(\Omega,\mathcal F,\mu)$ be a probability space and let $\mathcal K\in\mathcal F$ satisfy $0<\mu(\mathcal K)<1$.

Define conditional measures
\[
\mu_{\mathcal K}(A):=\mu(A\mid\mathcal K)=\frac{\mu(A\cap\mathcal K)}{\mu(\mathcal K)},
\qquad
\mu_{\mathcal K^c}(A):=\mu(A\mid\mathcal K^c)=\frac{\mu(A\cap\mathcal K^c)}{\mu(\mathcal K^c)}.
\]
For integrable $F$ define the conditional jump
\[
\Delta_{\mathcal K}F := \mu_{\mathcal K}(F)-\mu_{\mathcal K^c}(F).
\]
For integrable $F,G$, define covariance
\[
\Cov_\nu(F,G):=\nu(FG)-\nu(F)\nu(G).
\]

### Lemma 1.1 (exact covariance decomposition)

For bounded measurable $F,G$,
\[
\boxed{
\Cov_\mu(F,G)
=
\mu(\mathcal K)\Cov_{\mu_{\mathcal K}}(F,G)
+
\mu(\mathcal K^c)\Cov_{\mu_{\mathcal K^c}}(F,G)
+
\mu(\mathcal K)\mu(\mathcal K^c)\,\Delta_{\mathcal K}F\,\Delta_{\mathcal K}G.
}
\]

**Proof.** Write $\alpha:=\mu(\mathcal K)\in(0,1)$. Then $\mu=\alpha\mu_{\mathcal K}+(1-\alpha)\mu_{\mathcal K^c}$. Expand $\mu(FG)$ and $\mu(F)\mu(G)$ using this convex decomposition and regroup terms. The cross-term equals $\alpha(1-\alpha)(\mu_{\mathcal K}(F)-\mu_{\mathcal K^c}(F))(\mu_{\mathcal K}(G)-\mu_{\mathcal K^c}(G))$. ∎

### Lemma 1.2 (universal sup-norm bound)

For any probability measure $\nu$ and bounded $F,G$,
\[
|\Cov_\nu(F,G)|\le 4\|F\|_\infty\|G\|_\infty.
\]

**Proof.** Write $\Cov_\nu(F,G)=\nu((F-\nu(F))(G-\nu(G)))$ and bound by $\|F-\nu(F)\|_\infty\|G-\nu(G)\|_\infty\le (2\|F\|_\infty)(2\|G\|_\infty)$. ∎

### Proposition 1.3 (localization error bound)

For bounded $F,G$,
\[
\boxed{
|\Cov_\mu(F,G)|
\le
|\Cov_{\mu_{\mathcal K}}(F,G)|
+
8\|F\|_\infty\|G\|_\infty\,\mu(\mathcal K^c).
}
\]

**Proof.** Apply Lemma 1.1 and bound the $\mathcal K^c$ covariance and mean jumps using Lemma 1.2 and $|\Delta_{\mathcal K}F|\le 2\|F\|_\infty$. ∎

**Why this matters.** This mechanism is the rigorous way to insert typicality: the tail probability $\mu(\mathcal K^c)$ appears only as an additive error term.

---

## 2. Reflection positivity and OS: permanence under restriction and projection

### 2.1 Reflection positivity datum

Let $\Theta:\Omega\to\Omega$ be a measurable involution (reflection). Define
\[
(\theta F)(U):=\overline{F(\Theta U)}.
\]
Let $\mathcal A_+\subset L^\infty(\Omega)$ be a unital $*$-subalgebra (positive-time algebra). A measure $\mu$ is **reflection positive** if
\[
\mu\big((\theta F)F\big)\ge 0\qquad \forall F\in\mathcal A_+.
\]

Reflection positivity is the only positivity hypothesis needed for OS reconstruction.

### Lemma 2.2 (permanence under subalgebra restriction)

If $\mu$ is reflection positive on $(\Omega,\Theta,\mathcal A_+)$, and if $\mathcal B_+\subset \mathcal A_+$ is a unital $*$-subalgebra, then $\mu$ is reflection positive on $(\Omega,\Theta,\mathcal B_+)$.

**Proof.** Immediate: the inequality holds for all $F\in\mathcal A_+$, hence for all $F\in\mathcal B_+$. ∎

### 2.3 Pushforward and projected observables

Let $\pi:\Omega\to\Omega'$ be measurable. Define the pushforward measure $\mu':=\mu\circ\pi^{-1}$ on $\Omega'$.
Suppose there is a reflection $\Theta':\Omega'\to\Omega'$ such that
\[
\pi\circ\Theta = \Theta'\circ\pi.
\tag{2.1}
\]
Let $\mathcal A_+'$ be a unital $*$-subalgebra of bounded functions on $\Omega'$. Define its pullback $\pi^*\mathcal A_+' := \{F'\circ\pi: F'\in\mathcal A_+'\}$.

### Lemma 2.4 (reflection positivity preserved under compatible pushforward)

Assume (2.1). If $\mu$ is reflection positive on $\pi^*\mathcal A_+'$, then $\mu'$ is reflection positive on $\mathcal A_+'$.

**Proof.** For $F'\in\mathcal A_+'$,
\[
\mu'\big((\theta'F')F'\big)
=
\int_{\Omega'} \overline{F'(\Theta' u')}F'(u')\,\mu'(\dd u')
=
\int_{\Omega} \overline{F'(\Theta'\pi u)}F'(\pi u)\,\mu(\dd u).
\]
Use compatibility $\Theta'\pi=\pi\Theta$ to rewrite as
\[
\int_{\Omega} \overline{F'(\pi\Theta u)}F'(\pi u)\,\mu(\dd u)
=
\mu\big((\theta (F'\circ\pi))(F'\circ\pi)\big)\ge 0,
\]
by reflection positivity of $\mu$ on $\pi^*\mathcal A_+'$. ∎

**Why this matters.** This is the exact statement needed to justify that reflection positivity survives coarse-graining when the reflection intertwines with the projection.

---

## 3. Gap stability from quadratic-form bounds (operator permanence)

This section provides a functional-analytic lemma that turns “gap persistence” into a theorem once one has uniform lower bounds on quadratic forms.

### 3.1 Quadratic-form lower bounds and spectral gaps

Let $H$ be a self-adjoint operator on a Hilbert space $\mathcal H$ with $H\ge 0$. A **spectral gap** at size $m>0$ means that the spectrum satisfies
\[
\mathrm{spec}(H)\cap (0,m)=\varnothing,
\]
equivalently, $H\succeq m\,P$ on the orthogonal complement of its ground space projection $P_0$.

A sufficient condition for a gap is a uniform lower bound on a dense domain:
\[
\langle\psi,H\psi\rangle \ge m\|\psi\|^2
\quad\text{for all }\psi\perp \ker(H).
\tag{3.1}
\]

### 3.2 Monotone limits (strong resolvent convergence)

Let $H_n$ be self-adjoint, nonnegative operators. Suppose:

1. There exists $m>0$ such that for all $n$,
   \[
   H_n \succeq m\,\Id \quad \text{on a common dense core } \mathcal D.
   \tag{3.2}
   \]
2. $H_n\to H$ in the **strong resolvent sense**, i.e. $(H_n+1)^{-1}\to (H+1)^{-1}$ strongly.

### Proposition 3.3 (gap permanence under strong resolvent limits)

Under (3.2) and strong resolvent convergence, one has
\[
H\succeq m\,\Id
\quad\text{(as a quadratic form).}
\]
In particular, $H$ has spectral gap at least $m$ above its ground space.

**Proof.** Strong resolvent convergence implies convergence of bounded continuous functional calculus. In particular, for $\lambda<m$, the spectral projections $E_{H_n}([0,\lambda])$ converge strongly to $E_H([0,\lambda])$. But (3.2) forces $E_{H_n}([0,\lambda])=0$ on $\mathcal D$ for all $\lambda<m$. Hence $E_H([0,\lambda])=0$ for $\lambda<m$, i.e. $\mathrm{spec}(H)\cap[0,m)=\{0\}$ with the same ground space. ∎

**Why this matters.** In the YM program, once an OS Hamiltonian $H_{a_{\lat},L}$ has a uniform gap $\ge m(a_{\lat})$ at fixed cutoff and volumes $L$, this proposition is the mechanism by which a thermodynamic limit (and later continuum limit) can inherit a positive gap—provided the convergence is formulated in a strong resolvent framework.

---

## 4. How these permanence interfaces glue into the YM pipeline

- §1 converts conditional clustering to unconditional clustering with an explicit tail term.
- §2 ensures reflection positivity (and thus OS reconstruction) survives the algebraic restrictions and projections used in localization/thermodynamic limits.
- §3 ensures once a gap is proved uniformly along an approximating sequence, the limit theory retains the gap.

These are foundational not because they are exotic, but because they make the “big arrows” in the mass-gap program **structural theorems** rather than narrative steps.
