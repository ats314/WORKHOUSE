# W6 Synchronized Transport and Conditional-Score Domination M10

## 1. Statement and Scope

The target inequality is conditional-score domination for the four-face compact $SU(2)^4$ Wilson block:
\[
  K_g(w) \le C_0 + C_1 g^{-2} \mathbb{E}_{\mu_g}(V \mid w) \quad \text{for } 0 < g < g_*, \tag{M10}
\]
where $w = \operatorname{Sc}(Q) = \operatorname{tr}(U_2 U_3)/2 \in [-1, 1]$, $K_g(w) = \operatorname{Var}_{\mu_g}(\sigma_g \mid w)$, and
\[
  \sigma_g = \frac{\partial_g \Psi_g + D \Psi_g / g}{\Psi_g}
\]
is the score of the quantum ground state under the dilation operator $D = Z + \frac{1}{2} \operatorname{div}_{\mathrm{Haar}} Z$.

This derivation establishes:
1. **Exact Linear Phase Drift Cancellation (T1)**: The synchronized radial transport $S_{13}$ satisfies
   \[
     \partial_y(2S - ZS)\big|_{m(q)} \equiv 0 \quad \text{identically for all } \theta \in [0, \pi),
   \]
   completely eliminating the $g^{-4}$ divergence that falsified unsynchronized cutoffs.
2. **Euler Cancellation at the Well (T1)**: At $q = 0$, $F = 2S - ZS \equiv 0$ to second order in $\eta$, yielding the sharp remainder bound $|F(q, \eta) - F(q, 0)| \le c_F (|q| |\eta|^2 + |\eta|^3)$.
3. **Tube Variance Domination (T3 / Analytic)**: On the conditional Agmon tube,
   \[
     \mathbb{E}_{\text{tube}} |\sigma_g - \beta_g|^2 \le C_0 + C_1 g^{-2} \mathbb{E}_{\mu_g}(V \mid Q),
   \]
   with explicit constants $C_0 = 4 c_F^2 c_6 + 2 c_a^2 c_2$ and $C_1 = 8 \pi^2 c_F^2 c_4$.
4. **Antipodal Morse-Bott Regularity & Score Invariance (T1 / T3)**: At $Q \to -I$, the 2-sphere minimizer $\mathcal{M}$ has 7 normal directions with $\lambda \ge 4(\sqrt{2}-1) > 0$. Gauge symmetry guarantees $d\sigma_g|_{T\mathcal{M}} = 0$, and the potential floor $v_*(\pi) = 16 - 8\sqrt{2} > 0$ provides a strictly positive $O(g^{-2})$ budget.

---

## 2. The Synchronized Radial Field S13 and Drift Cancellation

Let $Q = \exp(\theta n)$ with $n \in S^2$ and $\theta \in [0, \pi]$. In unit quaternions, $\alpha = \theta/4$. The conditional minimizer curve in fiber coordinates $y = (U_0, U_1, U_2)$ is:
\[
  m(\theta) = (\theta/4, \theta/4, \theta/2)^T, \quad U_3 = U_2^{-1} Q.
\]
The synchronized radial profiles are defined by:
\[
  z_0(r) = r \chi(4r), \quad z_1(r) = r \chi(4r), \quad z_2(r) = r \chi(2r), \quad z_Q(r) = r \chi(r),
\]
where $\chi$ is a smooth cutoff equal to $1$ near $0$ and supported on $[0, \theta_a]$ with $\theta_a < \pi$.

### Theorem 1 (Synchronized Tangency)
Along the minimizer curve $m(\theta)$, the dilation velocity matches the curve tangent exactly:
\[
  Z_y(m(\theta), \theta) - Dm(\theta) Z_Q(\theta) \equiv 0.
\]

#### Proof
At the minimizer, the angles on each factor are $r_0 = \theta/4$, $r_1 = \theta/4$, $r_2 = \theta/2$, and $r_Q = \theta$. Evaluating:
\[
  z_0(\theta/4) = \frac{\theta}{4} \chi(\theta), \quad z_1(\theta/4) = \frac{\theta}{4} \chi(\theta), \quad z_2(\theta/2) = \frac{\theta}{2} \chi(\theta), \quad z_Q(\theta) = \theta \chi(\theta).
\]
Since $Dm(\theta) = (1/4, 1/4, 1/2)^T$, we have:
\[
  Dm(\theta) Z_Q(\theta) = \begin{pmatrix} 1/4 \\ 1/4 \\ 1/2 \end{pmatrix} \theta \chi(\theta) = \begin{pmatrix} \frac{\theta}{4} \chi(\theta) \\ \frac{\theta}{4} \chi(\theta) \\ \frac{\theta}{2} \chi(\theta) \end{pmatrix} = Z_y(m(\theta), \theta).
\]
Differentiating the phase $F = 2S - ZS$ with respect to fiber variations $\eta = y - m(q)$ gives:
\[
  \partial_y (2S - ZS)\big|_{m(q)} = - B(q) [Z_y(m(q), q) - Dm(q) Z_Q(q)] \equiv 0.
\]
This completes the proof.

#### Contrast with Failed Unsynchronized Cutoffs
In the counterexample field where $z_i(r) = r \chi(r)$ on all factors,
\[
  Z_y(m(\theta)) - Dm(\theta) Z_Q(\theta) = \begin{pmatrix} \frac{\theta}{4} (\chi(\theta/4) - \chi(\theta)) \\ \frac{\theta}{4} (\chi(\theta/4) - \chi(\theta)) \\ \frac{\theta}{2} (\chi(\theta/2) - \chi(\theta)) \end{pmatrix} \ne 0.
\]
This generated a non-zero linear phase derivative, resulting in an uncontrollable $g^{-4}$ divergence in the conditional variance.

---

## 3. Tube Variance and Small-Angle Domination

Let $F(q, \eta) = 2S(m(q) + \eta, q) - ZS(m(q) + \eta, q)$.

### Lemma 2 (Euler Cancellation at the Well)
At $q = 0$, $F(\eta) \equiv 0$ to second order in $\eta$.

#### Proof
At $q = 0$, near the origin $\chi \equiv 1$, so $Z x = x$ is the linear Euler field. The Agmon phase $S(x)$ is a positive definite quadratic form $\frac{1}{2} x^T M x$. Thus $ZS = x \cdot \nabla S = 2S$, so $F = 2S - ZS \equiv 0$ identically. The Hessian $\partial_\eta^2 F$ vanishes at $q = 0$.

### Proposition 3 (Remainder and Tube Variance Bound)
For $q$ in a neighborhood of $0$,
\[
  |F(q, \eta) - F(q, 0)| \le c_F (|q| |\eta|^2 + |\eta|^3).
\]
Under the conditional tube moment hypotheses $\mathbb{E}|\eta|^{2j} \le c_{2j} g^{2j}$ ($j=1,2,3$) and differentiated relative-amplitude bound $|\nabla_\eta a_g| \le c_a / g$, with $\beta_g(q) = F(q, 0)/g^3 + a_g(q, 0)$:
\[
  \mathbb{E}_{\text{tube}} |\sigma_g - \beta_g|^2 \le 4 c_F^2 \left( c_4 \frac{|q|^2}{g^2} + c_6 \right) + 2 c_a^2 c_2.
\]
Since in Lie coordinates $|q| = 2\theta$ and $v_*(\theta) = 16(1 - \cos(\theta/4)) \ge \frac{2}{\pi^2} \theta^2 = \frac{1}{2\pi^2} |q|^2$, we have $|q|^2 \le 2\pi^2 v_*(\theta) \le 2\pi^2 \mathbb{E}(V \mid Q)$.
Therefore:
\[
  \mathbb{E}_{\text{tube}} |\sigma_g - \beta_g|^2 \le C_0 + C_1 g^{-2} \mathbb{E}(V \mid Q),
\]
with $C_0 = 4 c_F^2 c_6 + 2 c_a^2 c_2$ and $C_1 = 8\pi^2 c_F^2 c_4$.

---

## 4. Antipodal Degeneration (Q -> -I)

At $\theta = \pi$ ($Q = -I$), the minimizer set is the 2-sphere $\mathcal{M} = S^2$.

1. **Normal Coercivity**: The 9D Hessian decomposes into:
   - 2 zero eigenvalues spanning the gauge orbit $T\mathcal{M}$.
   - 7 normal eigenvalues satisfying $\lambda_{\text{normal}} \ge 4(\sqrt{2} - 1) > 0$.
2. **Gauge Invariance**: The Hamiltonian, Haar measure, ground state $\Psi_g$, and dilation $D$ are simultaneous-conjugation equivariant. The score $\sigma_g$ is invariant under the gauge action:
   \[
     d\sigma_g\big|_{T\mathcal{M}} = 0.
   \]
   Thus, there is zero first-order variance along the degenerate sphere $\mathcal{M}$.
3. **Strictly Positive Floor**:
   \[
     v_*(\pi) = 16 - 8\sqrt{2} \approx 4.68629 > 0.
   \]
   The potential expectation provides a strictly positive floor:
   \[
     g^{-2} \mathbb{E}(V \mid Q = -I) \ge \frac{16 - 8\sqrt{2}}{g^2} \ge \frac{4.68}{g^2}.
   \]
   Any $O(g^{-2})$ or $O(1)$ fluctuation near the antipode is absorbed by this divergent positive budget.

---

## 5. Status and Open Hypotheses

The algebraic core (tangency cancellation, Euler vanishing, antipodal spectrum, gauge score invariance) is verified at tier **T1**.
The full statement of M10 remains **conditional** (tier **T3**) on:
- Global validity of the Helffer-Sjöstrand Dirichlet-Agmon comparison across all non-caustic fibers.
- The differentiated relative-amplitude estimate $|\nabla_\eta a_g| \le c_a / g$.
- Exponential suppression of the outside complement deviation $\mathbb{E}[1_{\text{outside}} |\sigma_g - \beta_g|^2 \mid Q]$.
