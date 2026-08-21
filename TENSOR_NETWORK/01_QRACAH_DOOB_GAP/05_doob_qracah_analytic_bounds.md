---
title: "Analytic control of the Doob–transformed q-Racah chain (gap, monotonicity, scaling)"
date: "2025-12-28"
---

## 0. Goal

The notebook construction

\[
H \;\xrightarrow{\text{ground state }\psi_0}\; Q \;=\; -\mathrm{diag}(\psi_0)^{-1}(H-E_0 I)\mathrm{diag}(\psi_0)
\]

produces a **one–dimensional continuous–time Markov chain** (a birth–death process) whose **spectral gap**
\[
m(N,q):= -\lambda_1(Q) = E_1(H)-E_0(H)
\]
is used as a toy “mass gap”.

This note tries to turn that into something you can actually *bound*:

- framework-level bounds for the gap in terms of edge conductances,
- a clean $q\uparrow 1$ scaling argument (why the exponent wants to be $1$ in this model),
- and a plausible route to monotonicity in $q$ (with a “what would it take to make it a theorem?” checklist).

Throughout we keep the “toy Hamiltonian” form used in the project:

- state space $n\in\{0,1,\dots,N\}$,
- symmetric tridiagonal $H$ with negative off-diagonals, built from $q$-Racah-shaped coefficients.

---

## 1. The Doob transform *is* a birth–death chain

Take a real symmetric tridiagonal matrix (Jacobi operator)
\[
(H f)_n = V_n f_n \;-\; a_n f_{n+1}\;-\; c_n f_{n-1},
\qquad a_n,c_n\ge 0,
\]
with the natural boundary convention $c_0=0$, $a_N=0$.

Assume irreducibility and Perron–Frobenius positivity of the ground state:

\[
H\psi_0 = E_0 \psi_0,\qquad \psi_0(n)>0.
\]

Define the Doob transform
\[
Q := -D^{-1}(H-E_0 I)D,\qquad D=\mathrm{diag}(\psi_0).
\]

**Claim (structure).**  $Q$ has nearest–neighbor jumps only:
\[
Q_{n,n+1} = a_n\,\frac{\psi_0(n+1)}{\psi_0(n)}=:b_n,\qquad
Q_{n,n-1} = c_n\,\frac{\psi_0(n-1)}{\psi_0(n)}=:d_n,
\]
and $Q_{nn}=-(b_n+d_n)$.  So $Q$ is a birth–death generator.

**Reversibility.**  Let
\[
\pi_n \propto \psi_0(n)^2.
\]
Then
\[
\pi_n b_n = \psi_0(n)^2 a_n\frac{\psi_0(n+1)}{\psi_0(n)} = a_n \psi_0(n)\psi_0(n+1)
= \pi_{n+1} d_{n+1},
\]
so $Q$ is reversible w.r.t. $\pi$.

That is the key simplification: *all* the spectral-gap technology for 1D reversible chains now applies.

---

## 2. Gap = Poincaré constant = a 1D inequality problem

For reversible $Q$, define the Dirichlet form
\[
\mathcal{E}(f,f)
:= -\langle f,Qf\rangle_\pi
= \sum_{n=0}^{N-1} c_n^{\mathrm{cond}}\,(f_{n+1}-f_n)^2,
\]
where the **edge conductance** is
\[
c_n^{\mathrm{cond}}
:= \pi_n b_n
= a_n\,\psi_0(n)\psi_0(n+1).
\]

The spectral gap (of $-Q$) is the best constant in the Poincaré inequality:
\[
m(N,q)=\inf_{\pi(f)=0}\frac{\mathcal{E}(f,f)}{\mathrm{Var}_\pi(f)}.
\]

So if you can bound conductances $c_n^{\mathrm{cond}}$ and cumulative masses
\[
\Pi_k := \sum_{n=0}^k \pi_n,
\]
you can bound the gap.

---

## 3. A “cheap but honest” analytic bound: Cheeger in 1D

For a reversible chain, define the conductance constant
\[
\Phi := \min_{\substack{S\subset\{0,\dots,N\}\\0<\pi(S)\le 1/2}}
\frac{\sum_{i\in S,j\notin S}\pi_i Q_{ij}}{\pi(S)}.
\]

In a birth–death chain, the minimizer can be taken as a prefix set $S_k=\{0,1,\dots,k\}$,
and the boundary flow across the cut is exactly one edge:

\[
\sum_{i\in S_k,j\notin S_k}\pi_i Q_{ij} = \pi_k b_k = c_k^{\mathrm{cond}}.
\]

Hence
\[
\boxed{
\Phi = \min_{0\le k\le N-1}\frac{c_k^{\mathrm{cond}}}{\min(\Pi_k,\,1-\Pi_k)}.
}
\]

Cheeger’s inequality then gives
\[
\boxed{
\frac{\Phi^2}{2}\;\le\; m(N,q)\;\le\; 2\Phi.
}
\]

What you gain:

- a clear “bottleneck diagnostic”: if some edge has tiny conductance compared to the mass on one side, the gap collapses,
- and a concrete thing to prove monotone in $q$: the ratio $c_k^{\mathrm{cond}}/\Pi_k$.

What you *don’t* gain:

- sharp constants (Cheeger can be loose),
- an explicit formula without understanding $\psi_0$.

But it is already a nontrivial analytic handle.

---

## 4. Why the gap saturates in $N$ for fixed $q<1$ (localization argument)

In the notebook’s “$\alpha=\beta=\gamma=\delta=1$” scan, the recurrence coefficients have two crucial features for any fixed $0<q<1$:

1. **Near $n=0$** they are small (because of factors like $(1-q^n)$),
2. **As $n\to\infty$** they converge exponentially fast to constants:
   \[
   a_n\to a_\infty,\qquad c_n\to c_\infty,
   \]
   because $q^n\to 0$.

That makes the semi-infinite operator a **compact perturbation** of a constant–coefficient Jacobi operator.  
The constant–coefficient tail has an “essential spectrum” band; any eigenvalues below the band are discrete and have exponentially decaying eigenvectors.

Translated to the Doob picture: for fixed $q<1$, the ground state $\psi_0$ is **exponentially localized** near the defect region where coefficients are small, so enlarging $N$ past that localization length barely changes $E_0,E_1$, hence barely changes the gap.

A quantitative (and provable) way to turn that into a bound is **Dirichlet–Neumann bracketing**:

- restrict to $\{0,\dots,M\}$ with a hard wall at $M$ (Dirichlet) to get an upper bound on low eigenvalues,
- compare with the full chain to get monotone convergence as $M\to\infty$.

Because the coefficients approach their limiting values exponentially fast in $n$, the truncation error decays like $O(q^M)$ (up to model-dependent constants). That gives an *analytic* “finite box suffices” criterion.

---

## 5. The cleanest analytic scaling: $q\uparrow 1$ gives exponent $\nu=1$ (in this toy)

Write $q=1-\varepsilon$ with $0<\varepsilon\ll 1$.

Use the elementary inequality/expansion
\[
1-q^k = 1-(1-\varepsilon)^k = k\varepsilon + O(\varepsilon^2).
\]

Plugging that into the project’s coefficient model (schematically: products/ratios of $(1-q^k)$),
one finds for each fixed $n$:

- off-diagonal coefficients scale linearly:
  \[
  a_n(q) = \varepsilon\,\widehat a_n + O(\varepsilon^2),
  \qquad
  c_n(q) = \varepsilon\,\widehat c_n + O(\varepsilon^2),
  \]
  where $\widehat a_n,\widehat c_n$ are explicit rational polynomials in $n$ and Askey parameters,
- diagonal terms are quadratic:
  \[
  V_n(q)=a_n(q)^2+c_n(q)^2 = O(\varepsilon^2).
  \]

Therefore, as an operator,
\[
H(q)= -\varepsilon\,K \;+\; O(\varepsilon^2),
\]
where $K$ is the tridiagonal matrix with off-diagonals $(\widehat a_n,\widehat c_n)$ and (to leading order) zero diagonal.

By standard analytic perturbation theory for finite matrices (or by min–max + norm bounds),
\[
E_k(q)= -\varepsilon\,\kappa_k + O(\varepsilon^2),
\]
hence the gap satisfies
\[
\boxed{
m(N,q)=E_1-E_0=\varepsilon\,(\kappa_0-\kappa_1)+O(\varepsilon^2)
\;\propto\; (1-q).
}
\]

So this toy naturally predicts an exponent
\[
\boxed{\nu=1}
\]
for the near-$q=1$ vanishing of the gap at fixed $N$ (and often still in the localized $N\to\infty$ regime).

This is exactly what the empirical fit in the project was seeing.

---

## 6. Monotonicity in $q$: a plausible route to a theorem

Empirically, many scans show $m(N,q)$ decreases as $q\uparrow 1$.

A robust theorem strategy (that avoids trying to take derivatives of eigenvalues) is:

1. Prove that for the relevant parameter region, **conductances** scale like
   \[
   c_n^{\mathrm{cond}}(q) \approx (1-q)\,\text{(slowly varying in $q$)}.
   \]
   This is a statement about $a_n(q)$ and the localized ground state.

2. Use the 1D Cheeger formula
   \[
   \Phi(q)=\min_k \frac{c_k^{\mathrm{cond}}(q)}{\min(\Pi_k(q),1-\Pi_k(q))}
   \]
   and show the denominator is relatively stable under $q$ (again, localization helps: $\Pi_k$ saturates quickly).

3. Conclude $\Phi(q)$ (hence $m(q)$) decreases with $q$ at least on a neighborhood of $q=1$, and likely globally.

If you want a more brute-force route: show that the *symmetric conjugate* of $Q$,
\[
\mathcal{L}:= -\mathrm{diag}(\sqrt{\pi})\,Q\,\mathrm{diag}(1/\sqrt{\pi}),
\]
has a quadratic form whose coefficients are monotone in $q$; then apply min–max monotonicity.

That last step is where real work lives (but it’s exactly the kind of work that becomes feasible once you’ve reduced to 1D).

---

## 7. What would make this “new theory” and not just a toy?

If you can prove **any** one of the following, the toy graduates:

1. **Uniform gap for fixed $q<1$**:
   \[
   \inf_{N} m(N,q)>0.
   \]

2. A **scaling limit** as $q\uparrow 1$ with $N\to\infty$ that yields a nontrivial continuum gap function.

3. A **representation-theoretic identification** of the coefficients $a_n,c_n$ (and hence $\psi_0$) so that positivity and localization become structural facts, not numerical observations.

Those three are the stepping stones to wiring this into a transfer-operator/Wilson-loop story with actual teeth.

