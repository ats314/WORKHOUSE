# Gaussian Polarity & Reducible Strata (High leverage, plausibly publishable)

This file consolidates:

- `doc3_Gaussian_Polarity_and_Capacity.txt`
- `doc5_Polarity_Reducible_Connections_Gaussian.txt`

The novel idea: **reducible connections form an “infinite-codimension” constraint set and are capacity-zero (polar) for a Gaussian OU Dirichlet form**, and polarity transfers under bounded change of measure.

This is relevant because many functional-inequality arguments (LSI/spectral gap) get messy near singular strata; polarity says “the diffusion never hits it anyway.”

---

## 1. OU polarity for infinite-codimension affine subspaces

Let $H$ be a separable Hilbert space and $\mu_0$ a nondegenerate centered Gaussian measure.
Consider the Ornstein–Uhlenbeck (OU) Dirichlet form
\[
\mathcal{E}_0(f,f) = \int_H \|\nabla f\|_H^2\, d\mu_0.
\]
A set $E\subset H$ is **polar** if the OU process starting from $\mu_0$-a.e. point hits $E$ with probability $0$.

### Proposition (Polarity threshold)
Let $S\subset H$ be a closed linear subspace and write $H=S\oplus S^\perp$.
- If $\dim S^\perp = m <\infty$, then $S$ is polar iff $m\ge 3$.
- If $\dim S^\perp = \infty$, then $S$ is polar.

The $\infty$-codimension case follows by nesting: $S$ is contained in a decreasing family of finite-codimension subspaces $S_N$ with codim $N\ge 3$, and each $S_N$ is polar.

Affine translates are also polar.

---

## 2. Capacity comparison under bounded change of measure

Let $\mu$ satisfy $d\mu = \rho\, d\mu_0$ with
\[
0<c_1\le \rho \le c_2<\infty \quad \mu_0\text{-a.e.}
\]
Assume the carré du champ $\Gamma(f)=\|\nabla f\|^2$ is the same. Then capacities compare:
\[
c_1 \operatorname{Cap}_{\mu_0}(E)\le \operatorname{Cap}_\mu(E)\le c_2 \operatorname{Cap}_{\mu_0}(E).
\]
Hence:
\[
\operatorname{Cap}_{\mu_0}(E)=0 \iff \operatorname{Cap}_\mu(E)=0.
\]

---

## 3. Application: reducible connections are polar for Gaussian reference dynamics

Let $M$ be a compact 4-manifold and consider a Sobolev space of 1-forms with values in $\operatorname{ad}P$:
\[
\mathcal{H} := L_k^2(M,T^*M\otimes \operatorname{ad}P),
\qquad k>2.
\]
A connection $A=A_0+a$ is **reducible** if there exists a nonzero $\xi$ such that
\[
D_A \xi = 0.
\]
For fixed $\xi\ne 0$, the constraint can be written
\[
D_{A_0}\xi + [a,\xi]=0 \quad\Longleftrightarrow\quad T_\xi(a)=b_\xi,
\]
where $T_\xi(a)=[a,\xi]$ is linear in $a$.

Under the key analytic input (“$T_\xi$ has infinite rank”), the solution set $T_\xi(a)=b_\xi$ lies in an **affine infinite-codimension subspace**, hence is polar for the Gaussian OU form.

Taking a countable dense set $\{\xi_j\}$ gives:
\[
\Sigma \subset \bigcup_{j\ge 1}\Sigma_{\xi_j},
\]
and countable unions of polar sets are polar.

---

## 4. Why this matters to the mass-gap architecture

If a Yang–Mills (or effective) measure is a bounded perturbation of a Gaussian reference measure *in a regime of interest*, then the reducible set being polar suggests:

- the diffusion underlying BE/LSI analysis does not “see” the reducible stratum,
- singular strata can be ignored without boundary conditions,
- many arguments can be made on the regular stratum without worrying about Gribov-type hitting.

This is not the whole mass gap problem — but it removes a notoriously annoying obstruction *if the bounded-density transfer can be justified in the regime being used.*

---

## 5. What to do next (to make this a real theorem in a paper)

1. Prove/justify the “$T_\xi$ has infinite rank” lemma cleanly in the Sobolev setting.
2. Specify the exact Dirichlet form used for the “YM diffusion” and whether it shares the same carré du champ as the Gaussian reference.
3. Precisely state the bounded-density regime (finite volume? gauge-fixed? small-field?).

This is a rare part of the project that looks both **novel** and **mathematically tractable**.

