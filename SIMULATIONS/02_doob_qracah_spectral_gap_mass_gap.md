---
title: "A Doob-transformed q-Racah Jacobi operator as a toy model for a mass gap"
date: "2025-12-02"
---

# What this document captures

The notebooks build a **finite-dimensional, exactly computable “mass gap surrogate”** by:

1. constructing a symmetric tridiagonal matrix $H$ (a **Jacobi operator**) whose spectral theory is tied to **$q$-Racah polynomials**,
2. taking its positive ground state $\psi_0$,
3. applying a **Doob $h$-transform** to turn $H$ into a **Markov generator $Q$**,
4. interpreting the **spectral gap of $Q$** as a “mass gap” analogue, and
5. checking that simple correlation functions decay at an exponential rate consistent with that gap.

The individual ingredients are standard in isolation; the potentially novel thing is the **particular assembly**: a $q$-Racah / quantum-group-flavored Jacobi operator $\Rightarrow$ Doob transform $\Rightarrow$ stochastic dynamics whose gap is tracked as a function of $q$ and “size” $N$.

---

# 1. From a symmetric operator to a Markov generator via Doob transform

Let $H$ be a real symmetric matrix (finite state space for now),
\[
H = H^\top \in \mathbb{R}^{(N+1)\times(N+1)}.
\]

Assume:

- the lowest eigenvalue is $E_0$,
- the corresponding eigenvector $\psi_0$ has strictly positive entries:
  \[
  H\psi_0 = E_0 \psi_0,\qquad \psi_0(i)>0.
  \]

Define the diagonal matrix $D=\mathrm{diag}(\psi_0)$.

A standard Doob transform produces an operator similar to $H-E_0 I$:
\[
\widetilde{Q} := -D^{-1}(H-E_0 I)D.
\]

In coordinates (for $i\neq j$),
\[
\widetilde{Q}_{ij} = -H_{ij}\frac{\psi_0(j)}{\psi_0(i)}.
\]

If $H$ has nonpositive off-diagonal entries (an “$M$-matrix” style condition), then $\widetilde{Q}_{ij}\ge 0$ for $i\neq j$.

Finally define the diagonal by enforcing row-sum zero:
\[
Q_{ii} := -\sum_{j\ne i} Q_{ij}.
\]

Then $Q$ is a continuous-time Markov generator:

- off-diagonal rates $Q_{ij}\ge 0$,
- row sums $\sum_j Q_{ij}=0$,
- spectrum contained in $\{\lambda: \Re\lambda \le 0\}$ with one eigenvalue at $0$.

## Gap matching

Because $Q$ is similar (up to sign and shift) to $H-E_0I$, the **positive energy gap**
\[
E_1-E_0
\]
corresponds directly to the **Markov spectral gap**
\[
m := -\Re(\lambda_1(Q)),
\]
where $\lambda_1(Q)$ is the eigenvalue with largest real part after $0$.

That is the key “physics” identification: the stochastic relaxation scale $\sim e^{-mt}$ is a toy version of an inverse correlation length.

---

# 2. Choosing $H$ from $q$-Racah data

$q$-Racah polynomials are the most general finite orthogonal family at the top of the Askey scheme. They have a three-term recurrence, which defines a Jacobi matrix.

In the notebook, $H$ is built as a **$q$-Racah Jacobi matrix**
\[
H = H(N,q;\alpha,\beta,\gamma,\delta),
\]
depending on:

- size parameter $N$ (finite truncation / polynomial degree),
- deformation parameter $q$ (typically $0<q<1$ in the Markov scans),
- four “Askey parameters” $(\alpha,\beta,\gamma,\delta)$.

The explicit recurrence coefficients are code-defined; the essential structural point is:

- $H$ is symmetric tridiagonal,
- the ground state is computed numerically,
- positivity checks determine whether the Doob transform defines a valid generator.

---

# 3. Concrete example: explicit $H$, $Q$, and a mass-gap-like number

One run in the project produces:

A symmetric $5\times 5$ tridiagonal $H$ (shown here exactly as printed in the notebook output):
\[
H=\begin{pmatrix}
 0.004875 & -0.04134038 & 0 & 0 & 0\\
-0.04134038 & 0.00901832 & -0.06788456 & 0 & 0\\
0 & -0.06788456 & 0.01628785 & -0.09358721 & 0\\
0 & 0 & -0.09358721 & 0.0261009 & -0.11894883\\
0 & 0 & 0 & -0.11894883 & 0.01414882
\end{pmatrix}.
\]

The Doob generator is:
\[
Q=\begin{pmatrix}
-0.14362461 & 0.14362461 & 0 & 0 & 0\\
0.01189926 & -0.14776793 & 0.13586867 & 0 & 0\\
0 & 0.03391742 & -0.15503745 & 0.12112004 & 0\\
0 & 0 & 0.07231311 & -0.16485051 & 0.0925374\\
0 & 0 & 0 & 0.15289843 & -0.15289843
\end{pmatrix}.
\]

The printed eigenvalues satisfy one eigenvalue $\approx 0$ and the others negative:
\[
\lambda(Q)\approx\{-0.31695,\,-0.21450,\,-0.14761,\,-0.08512,\,0\}.
\]

So the “mass gap” proxy is
\[
\boxed{m_q \approx 0.0851.}
\]

---

# 4. Correlators decay with an effective rate comparable to the gap

Pick an observable $f$ on the state space (in the demo, $f(n)=n$). Define a correlation function along the Markov semigroup:
\[
C(t) := \langle f, e^{tQ} f\rangle_\pi - \langle f\rangle_\pi^2,
\]
for a suitable stationary measure $\pi$ (in the reversible case, $\pi\propto \psi_0^2$).

The notebook prints an effective decay rate
\[
\lambda_{\mathrm{eff}}(t) := -\frac{1}{t}\log\left|\frac{C(t)}{C(0)}\right|.
\]

In the shown run, $\lambda_{\mathrm{eff}}(t)$ settles near $\sim 0.09$, close to $m_q\approx 0.085$, consistent with a leading-exponential relaxation mode.

This is a sanity check that the spectral gap is the right “decay scale”.

---

# 5. Parameter scans: how $m_q$ behaves under $q$-flows and $\alpha$-flows

## q-flows (holding Askey params fixed)

A scan of “q-flow” experiments is classified as **good\_monotone**: the gap decreases monotonically as $q$ increases, while retaining validity of the Doob generator.

The printed summary includes, for example:
- a flow from $q_0=0.8$ to $q_1=0.99$ with $\alpha=\beta=\gamma=\delta=1$ has
  \[
  \text{min\_gap}\approx 0.0159,\qquad \text{max\_gap}\approx 0.2372,
  \]
  and is monotone decreasing.

This is tantalizingly RG-like: “turning $q$ toward $1$” weakens the gap.

## Near-$q\approx 1$ scaling fit: a critical exponent estimate (empirical)

Another notebook cell fits the smallest gap (over a list of sizes $N$) to a power law
\[
m(q)\sim (1-q)^\nu
\qquad\text{for } q\to 1^-,
\]
by regressing
\[
\log m \approx \nu \log(1-q)+c
\]
using only data with $q>0.92$.

The printed result is
\[
\boxed{\nu \approx 0.9668.}
\]

This is **not a proof** and depends on the chosen fit window and finite-size procedure, but it is a concrete quantitative target for future analysis.



## alpha-flows (holding $q$ fixed)

By contrast, “alpha-flow” experiments (varying $\alpha$ between two values at fixed $q$) are flagged as **collapse** in the summary. Interpreting the code logic, “collapse” means either:

- invalid points (loss of positivity or ground-state issues), or
- a non-robust gap profile (non-monotone / unstable).

That’s actually useful information: it suggests that not all parameter directions are physically meaningful in the Markov/gap sense.

---

# 6. Where this could go (how to upgrade from toy to theory)

## (A) Make the recurrence coefficients representation-theoretic

Right now, $H$ is “$q$-Racah-shaped”. A natural upgrade is to **derive $H$ directly from $U_q(\mathfrak{su}(2))$ recoupling** so that:

- states correspond to representation labels (spins, intertwiners, etc.),
- coefficients come from exact orthogonality measures,
- the Doob positivity conditions become theorems (or at least constrained by representation theory).

## (B) Understand the $N\to\infty$ limit

If $N$ is a truncation, then an actual “mass gap” story demands controlling:

- existence of a positive limiting gap $m(q)>0$ for fixed $q<1$,
- how $m(q)$ behaves as $q\to 1$,
- whether tuning $q\to 1$ at the same time as $N\to\infty$ yields a finite continuum scale.

## (C) Connect to Wilson loops / transfer matrices

The project also sketches a composite transfer operator $T_q$ built from $e^{Q}$ and boundary kernels. If that is made representation-theoretic, the gap of $T_q$ becomes a candidate for a **string tension / area law** proxy.

---

# 7. A crisp conjecture worth testing

A minimal, testable conjecture suggested by the scans is:

> **Conjecture (toy confinement criterion).**  
> For a representation-theoretically normalized $q$-Racah Jacobi operator $H(N,q)$ with $0<q<1$, the Doob-transformed generator exists for all $N$, and its spectral gap is bounded below uniformly in $N$:
> \[
> \inf_{N} m(N,q) \;>\;0.
> \]
> Moreover, $m(N,q)$ decreases as $q\uparrow 1$.

This would be the toy-model analogue of “a mass gap exists at finite lattice spacing and vanishes only in the continuum limit”.

