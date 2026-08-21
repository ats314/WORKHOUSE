# q-Racah Doob Transform Toy Model: A Trackable “Mass Gap” and a Critical Exponent

## 1. The toy Hamiltonian \(H(N,q)\)

Fix \(N\in\mathbb{N}\). Define a symmetric tridiagonal matrix \(H\in\mathbb{R}^{(N+1)\times(N+1)}\) with entries
\[
H_{n,n} = A_n^2 + C_n^2,\qquad
H_{n,n+1}=H_{n+1,n}=-A_n,\qquad
H_{n,n-1}=H_{n-1,n}=-C_n,
\]
where \(A_n,C_n\ge 0\) are q-Racah-type coefficients (with parameters \(\alpha,\beta,\gamma,\delta\)):

\[
A_n^2 = \frac{(1-\alpha q^{n+1})(1-\beta\delta q^{n+1})(1-\gamma q^{n+1})(1-\delta q^{n+1})}
{(1-\delta q^{2n+1})(1-\delta q^{2n+2})},
\]
\[
C_n^2 = \frac{(1-q^n)(1-\beta q^n)(1-\gamma q^n)(1-\alpha\delta q^n)}
{(1-\delta q^{2n})(1-\delta q^{2n+1})}.
\]
In the “stable” regime heavily used in the project:
\[
\alpha=\beta=\gamma=\delta=1,\qquad q\in(0,1).
\]

## 2. Doob transform → Markov generator

Diagonalize
\[
H\psi_k = E_k \psi_k,\qquad E_0\le E_1\le \cdots \le E_N,
\]
and take the ground state \(\psi_0>0\) (enforced numerically by absolute value + positivity checks). Define the continuous-time Markov generator \(Q\) by the Doob transform:
\[
Q_{ij} = -H_{ij}\frac{\psi_0(j)}{\psi_0(i)}\quad (i\neq j),\qquad
Q_{ii} = -\sum_{j\neq i} Q_{ij}.
\]
Then \(Q\) has nonnegative off-diagonals and row sums zero.

**Toy “mass gap”:** define
\[
m_q(N) := -\lambda_1(Q),
\]
where \(\lambda_1(Q)<0\) is the second-largest eigenvalue (largest is \(0\)).

## 3. Observed behavior in q-flows

A representative scan (for \(N=4\)) reports monotone decrease of the gap as \(q\to 1\):
\[
\begin{array}{c|c}
q & m_q \\
\hline
0.85 & 0.1991\\
0.87 & 0.1801\\
0.89 & 0.1590\\
0.91 & 0.1361\\
0.93 & 0.1114\\
0.95 & 0.0851\\
0.97 & 0.0575\\
0.99 & 0.0295
\end{array}
\]
This is exactly the kind of “gap closes at criticality” behavior one wants a toy model to have.

By contrast, flows in other parameters (e.g. \(\alpha\)-flows at fixed \(q\)) tend to “collapse” (gap not monotone, invalidity due to loss of positivity), so the q-direction behaves like the physically meaningful deformation axis.

## 4. Finite-size scaling and a fitted exponent

Using \(N\in\{4,6,8,10,12\}\) and \(q\) near 1, the project fits
\[
m_q \sim (1-q)^\nu
\quad\text{and reports}\quad
\nu \approx 0.9668.
\]
This is intriguingly close to 1, suggesting a near-linear closing of the gap in \((1-q)\) in the studied window.

## 5. Composite transfer operator \(T_q\): embedding into a boundary/bulk picture

A more ambitious construction defines a composite operator
\[
T_q := \Lambda^\top\, R\, e^{tQ}\, W\, R^\top\, \Lambda,
\]
where:
- \(e^{tQ}\) is bulk evolution under the Doob Markov semigroup,
- \(R\) is an overlap kernel (q-Racah / hypergeometric in the ideal version),
- \(W\) is a Wilson-loop multiplication operator,
- \(\Lambda\) is a boundary-to-bulk projection.

Then the effective boundary gap is extracted from the spectral radius:
\[
m_{\mathrm{eff}} := -\log |\lambda_1(T_q)|.
\]

In the repository this is a **template**: several pieces are placeholders (e.g. simplified kernels), but the algebraic architecture is a plausible bridge between:
- q-special function data,
- Markov generators / transfer matrices,
- and “mass gap as spectral gap” thinking.

## 6. Why this toy model is potentially useful

- It provides a sandbox where “mass gap” is literally a computable spectral gap.
- The Doob transform ties spectral theory to probability (mixing rates).
- The q-direction is a clean deformation axis with numerically nice monotonicity.
- The exponent \(\nu\approx 0.97\) is the kind of emergent universality number worth re-checking with more precision and a larger window.

## 7. Next steps that would actually strengthen it

1. Replace placeholder kernels in \(R\) and \(W\) with **true representation-theoretic** q-Racah overlap data.
2. Prove (or computer-assist) monotonicity of \(m_q(N)\) in \(q\) in the stable parameter regime.
3. Push finite-size scaling to larger \(N\) and quantify fitting uncertainty for \(\nu\).
4. Look for a direct mapping between this q-model and blocks in a spin-foam/tensor-network discretization where q–6j symbols are local Boltzmann weights.

If the YM program needs a toy model that “rhymes” with the hard problem, this is a decent candidate.
