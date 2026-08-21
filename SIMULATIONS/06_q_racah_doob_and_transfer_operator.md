# q-Racah Doob generator and composite transfer operator: a spectral laboratory

## 0. Why this exists in a YM program

This is a fully explicit toy model where “mass gap” is literally a computable spectral gap.
The role in the wider program is *computational confirmation* of the curvature/gap worldview:

- a deformation parameter $q\in(0,1)$ controls a robust positive gap,
- as $q\to 1$ the gap closes smoothly with critical scaling,
- a transfer-operator construction $\tilde T_q$ tracks the underlying gap (when not tuned into a near-projector).

Nothing here proves Yang–Mills. It’s a clean spectral sandbox.

---

## 1. q-Racah-type tridiagonal Hamiltonian

Fix an integer $N\ge 1$. Define a symmetric tridiagonal matrix $H\in\mathbb{R}^{(N+1)\times(N+1)}$ via coefficients $A_n,C_n,B_n$ for $n=0,\dots,N$:

$$
A_n^2 = \frac{(1-\alpha q^{n+1})(1-\beta\delta q^{n+1})(1-\gamma q^{n+1})(1-\delta q^{n+1})}{(1-\delta q^{2n+1})(1-\delta q^{2n+2})},
$$

$$
C_n^2 = \frac{(1-q^n)(1-\beta q^n)(1-\gamma q^n)(1-\alpha\delta q^n)}{(1-\delta q^{2n})(1-\delta q^{2n+1})},
$$

$$
B_n = -(A_n^2 + C_n^2).
$$

Then

- $H_{n,n}=A_n^2+C_n^2$,
- $H_{n,n+1}=H_{n+1,n}=-A_n$,
- $H_{n,n-1}=H_{n-1,n}=-C_n$,

with boundary $A_N=C_0=0$.

A heavily used stable regime is
$$\alpha=\beta=\gamma=\delta=1,\qquad q\in(0,1).$$

---

## 2. Doob transform to a Markov generator

Diagonalize $H$:
$$H\psi_k=E_k\psi_k,\qquad E_0\le E_1\le\cdots\le E_N.$$
Let $\psi_0$ be the (componentwise) positive ground state (numerically enforced by $|\cdot|$ and rejecting near-zero components).

Define $Q$ by the Doob transform

$$
Q_{ij}= -H_{ij}\,\frac{\psi_0(j)}{\psi_0(i)},\quad i\ne j,\qquad
Q_{ii}= -\sum_{j\ne i}Q_{ij}.
$$

Then $Q$ has nonnegative off-diagonals and zero row sums, so it is a continuous-time Markov generator.

---

## 3. Mass gap

Let $\{\lambda_k\}$ be eigenvalues of $Q$ sorted so that
$$0=\lambda_0 > \lambda_1\ge\lambda_2\ge\cdots\ge\lambda_N.$$
Define the gap
$$m_q(N) := -\lambda_1.$$

In the stable regime ($\alpha=\beta=\gamma=\delta=1$, $q<1$) the gap is strictly positive and decreases smoothly as $q\to 1$.

Example quoted in the project notes (representative): for $N=4$ and $q\approx 0.95$ one finds a nonuniform positive $\psi_0$ and eigenvalues with $m_q\approx 0.085$.

---

## 4. “Safe region” scanning and failure modes

A scanning harness classifies flows in parameter space as:

- **good\_monotone:** $Q$ valid everywhere and $m(t)$ monotone,
- **good\_nonmonotone:** $Q$ valid everywhere, $m(t)>0$ but nonmonotone,
- **collapse:** $\psi_0$ loses positivity or conditioning, Doob transform fails,
- **broken:** many invalid points.

Empirical finding: varying $q$ at fixed $\alpha=\beta=\gamma=\delta=1$ is robust (“good\_monotone”), while varying $\alpha$ at fixed $q$ often collapses.

---

## 5. Composite transfer operator $T_q$ on a boundary space

To mimic a transfer-matrix observable, define

- bulk evolution $T_{\rm bulk}=\exp(t_{\rm bulk}Q)$,
- boundary variables $\chi_j$, $j=1,\dots,n_\chi$,
- a Gaussian boundary kernel $R$ on $\chi$,
- a diagonal “Wilson-like” weight $W$ on $\chi$,
- a projection $\Lambda$ from boundary $\chi$ to bulk indices $\{0,\dots,N\}$.

The composite operator is
$$
T_q = \Lambda^\top\,T_{\rm bulk}\,\Lambda\,R\,W.
$$
Normalize by its spectral radius: $\tilde T_q := T_q/\rho(T_q)$. If $|\mu_1|$ is the 2nd-largest eigenvalue magnitude of $\tilde T_q$, define
$$m_{\rm eff} := -\log |\mu_1|.$$

Tuning $R$ and $\Lambda$ avoids a near-rank-1 projector and makes $m_{\rm eff}$ track the intrinsic bulk gap $m_q(N)$.

---

## 6. Minimal code pointers

The project includes complete code blocks (NumPy) in the Colab exports, and clean text derivations in:

- `01_q_racah_doob_massgap.txt`
- `02_q_flow_and_safe_region.txt`
- `04_composite_transfer_operator_Tq.txt`

This markdown is the “paper-ready” narrative version.
