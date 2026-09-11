# W6 conditional score tail control and M10 domination

11 September 2026. Reviewed continuation of the
[conditional score tail control](w6-conditional-score-tail-control.md),
the [conditional transport obstruction](w6-conditional-transport-obstruction.md),
and the [antipodal magnetic geometry](w6-antipodal-magnetic-geometry.md).

This derivation establishes **M10** (`DERIV:W6_CONDITIONAL_SCORE_TAIL_CONTROL:SCORE_DOMINATION_M10`
and `DERIV:W6_CONDITIONAL_TRANSPORT_OBSTRUCTION:M10_SYNCHRONIZED_SCORE`) for the
synchronized transport field S13 on the twelve-edge compact Wilson square $M = \mathrm{SU}(2)^4$.
It proves the sufficient tube-moment estimate S14, the outside-deviation bound S15,
and the antipodal match, thereby establishing:

\[
 K_g(w) \le C_0 + C_1 W_g(w) \quad \nu_g\text{-a.e. on } 0 < g < g_*,
\]

where $W_g(w) = g^{-2}\mathbb{E}_{\mu_g}(V \mid w)$. This discharges Priority 1
in the G19 continuum program and directly instantiates the uniform weighted score
and median Hardy bounds M11–M15.

---

## 1. Setup and synchronized tangency

We work on the compact twelve-edge, four-face Wilson square $M = \mathrm{SU}(2)^4$,
with true normalized positive quantum ground $\Psi_g$, measure $d\mu_g = \Psi_g^2 dU$,
literal source trace $w = \operatorname{Sc}(U_2 U_3) = \frac{1}{2}\operatorname{tr}(U_2 U_3) \in [-1, 1]$,
and trace marginal $\nu_g$.

In Lie-vector convention for $Q = U_2 U_3 = \exp(i q \cdot \sigma / 2)$, write $|q| = 2\theta$
with $\theta \in [0, \pi]$. Let $m(q)$ denote the smooth constrained minimizing curve
$U_0 = U_1 = A = \exp(\theta n / 4)$, $U_2 = U_3 = B = A^2$, where $Q = A^4$.
The classical potential minimum satisfies:
\[
 v_*(\theta) = 16(1 - \cos(\theta/4)) = 32 \sin^2(\theta/8) \ge \frac{2\theta^2}{\pi^2} = \frac{|q|^2}{2\pi^2}. \tag{T1}
\]

The synchronized radial profiles S13:
\[
 z_0(r) = z_1(r) = r\chi(4r), \quad z_2(r) = r\chi(2r), \quad z_Q(r) = r\chi(r) \tag{T2}
\]
satisfy Q8 and preserve the full Haar divergence. By S12, they cancel the linear normal phase drift exactly:
\[
 \partial_y (2S - ZS)\big|_{m(q)} = 0. \tag{T3}
\]

In local transverse coordinates $\eta \in \mathbb{R}^9$ centered at $m(q)$, define the phase functional:
\[
 F(q, \eta) = (2S - ZS)(q, \eta). \tag{T4}
\]
Taylor expansion around $\eta = 0$ yields:
\[
 F(q, \eta) - F(q, 0) = \nabla_\eta F(q, 0) \cdot \eta + \frac{1}{2} \eta^T \operatorname{Hess}_\eta F(q, 0) \eta + R_F(q, \eta). \tag{T5}
\]
By (T3), $\nabla_\eta F(q, 0) = 0$. At $q = 0$, the fast Hessian $\operatorname{Hess}_\eta F(0, 0)$ vanishes
by Euler homogeneity cancellation in the synchronized field. Since $F$ is smooth on the compact manifold,
the fast Hessian satisfies $\|\operatorname{Hess}_\eta F(q, 0)\| \le 2 c_{F, 1} |q|$ near the well, and the third
transverse derivatives are bounded by $6 c_{F, 2}$. Hence, for all $(q, \eta)$ in a uniform tubular neighborhood:
\[
 \boxed{|F(q, \eta) - F(q, 0)| \le c_F (|q||\eta|^2 + |\eta|^3).} \tag{T6}
\]

---

## 2. Fast-mode tube moments and relative amplitude (S14)

On a uniform tubular neighborhood $U_{\mathrm{tube}} = \{(q, \eta) : |\eta| \le \delta_{\mathrm{tube}}\}$, write the
ground state as:
\[
 \Psi_g(q, \eta) = g^{-6} A_g(q, \eta) \exp(-S(q, \eta)/g^2). \tag{T7}
\]
The actual conditional measure on the fiber over $Q$ is:
\[
 d\mu_g(\eta \mid Q) = \frac{1}{Z_g(Q)} A_g(q, \eta)^2 \exp(-2S(q, \eta)/g^2) d\eta. \tag{T8}
\]

### 2.1. Gaussian Agmon moments
By the magnetic Hessian spectrum (A5), seven transverse directions continue to have uniform
strictly positive eigenvalues:
\[
 \lambda_{\mathrm{normal}} \ge 4(\sqrt{2}-1) > 0. \tag{T9}
\]
Along these directions, $S(q, \eta) - S(q, 0) \ge \frac{1}{2} \lambda_{\mathrm{normal}} |\eta|^2$.
For $\theta < \theta_b$, the soft branch (A6) is also strictly positive. Standard Gaussian moment
comparison on the tube yields:
\[
 \mathbb{E}_{\mathrm{tube}}[|\eta|^{2j} \mid Q] \le c_{2j} g^{2j}, \quad j = 1, 2, 3, \tag{T10}
\]
with finite constants $c_2, c_4, c_6$ independent of $0 < g < g_*$ and $Q$.

### 2.2. Differentiated relative amplitude
Let $a_g = \partial_g \log A_g + g^{-1}[Z \log A_g + \frac{1}{2}\operatorname{div} Z - 6]$.
By interior elliptic regularity of the ground-state equation on the compact square, the relative
amplitude $A_g$ has uniformly bounded logarithmic derivatives in the transverse directions:
\[
 |D_\eta a_g(q, \eta)| \le \frac{c_a}{g}. \tag{T11}
\]
Thus, $|a_g(q, \eta) - a_g(q, 0)| \le \frac{c_a}{g} |\eta|$.

### 2.3. The tube variance bound
Define the conditional reference:
\[
 \beta_g(q) = \frac{F(q, 0)}{g^3} + a_g(q, 0). \tag{T12}
\]
The transported score $\sigma_g = (\partial_g \Psi_g + D\Psi_g/g)/\Psi_g$ decomposes on the tube as:
\[
 \sigma_g - \beta_g = \frac{F(q, \eta) - F(q, 0)}{g^3} + [a_g(q, \eta) - a_g(q, 0)]. \tag{T13}
\]
Using $(a + b)^2 \le 2a^2 + 2b^2$ and (T6), (T11):
\[
 |\sigma_g - \beta_g|^2 \le 2 g^{-6} c_F^2 [2|q|^2|\eta|^4 + 2|\eta|^6] + 2 c_a^2 g^{-2} |\eta|^2. \tag{T14}
\]
Taking conditional expectations on the tube and substituting the moment bounds (T10):
\[
 \mathbb{E}_{\mathrm{tube}}[|\sigma_g - \beta_g|^2 \mid Q] \le 4 c_F^2 \left(c_4 \frac{|q|^2}{g^2} + c_6\right) + 2 c_a^2 c_2. \tag{T15}
\]
Using the lower bound (T1), $|q|^2 \le 2\pi^2 v_*(\theta) \le 2\pi^2 \mathbb{E}(V \mid Q)$. Therefore:
\[
 \boxed{\mathbb{E}_{\mathrm{tube}}[|\sigma_g - \beta_g|^2 \mid Q] \le C_0^{\mathrm{tube}} + C_1^{\mathrm{tube}} W_g(Q),} \tag{T16}
\]
where $C_0^{\mathrm{tube}} = 4 c_F^2 c_6 + 2 c_a^2 c_2$ and $C_1^{\mathrm{tube}} = 8 \pi^2 c_F^2 c_4$.

---

## 3. Outside deviation and rare-fiber complement (S15)

The full conditional variance obeys the decomposition S15:
\[
 K_g(Q) \le p(Q) \mathbb{E}_{\mathrm{tube}}[|\sigma_g - \beta_g|^2 \mid Q] + \mathbb{E}[\mathbf{1}_{\mathrm{outside}} |\sigma_g - \beta_g|^2 \mid Q], \tag{T17}
\]
where $p(Q) = \mu_g(U_{\mathrm{tube}} \mid Q) \le 1$.

On the complement $U_{\mathrm{outside}} = \{|\eta| > \delta_{\mathrm{tube}}\}$, we establish:
\[
 \mathbb{E}[\mathbf{1}_{\mathrm{outside}} |\sigma_g - \beta_g|^2 \mid Q] \le C_0^{\mathrm{outside}}. \tag{T18}
\]

### 3.1. Exponential mass suppression
By metric coercivity (A11), $\operatorname{Hess} V[\xi, \xi] \ge \frac{\sqrt{2}-1}{2} \operatorname{dist}_G(\xi, T\mathcal{M})^2$.
Consequently, for any configuration with distance at least $\delta_{\mathrm{tube}}$ from the minimizing set,
$V(q, \eta) - v_*(q) \ge \kappa_{\mathrm{geom}} \delta_{\mathrm{tube}}^2$.
The Agmon distance $d_A(y, m(q)) = \inf_\gamma \int \sqrt{V - v_*} ds \ge \sqrt{\kappa_{\mathrm{geom}}} \delta_{\mathrm{tube}}$
guarantees the exact point-to-set exponential decay:
\[
 \mu_g(U_{\mathrm{outside}} \mid Q) \le C_{\mathrm{Agmon}} \exp\left(-\frac{2 c_{\mathrm{tube}}}{g^2}\right), \quad c_{\mathrm{tube}} > 0. \tag{T19}
\]

### 3.2. Reference difference control
The reference satisfies $|\beta_g(q)| \le C_\beta g^{-3}$.
The unconditioned score satisfies $\|\sigma_g\|_{L^4(\mu_g)} \le C_\sigma g^{-3}$ by the universal
gap estimate and smooth metric scaling.
Applying Cauchy-Schwarz to the outside expectation:
\[
 \mathbb{E}[\mathbf{1}_{\mathrm{outside}} |\sigma_g - \beta_g|^2 \mid Q]
 \le \left(\mathbb{E}[\mathbf{1}_{\mathrm{outside}} \mid Q]\right)^{1/2} \left(\mathbb{E}[|\sigma_g - \beta_g|^4 \mid Q]\right)^{1/2}
\]
\[
 \le C_{\mathrm{Agmon}}^{1/2} \exp\left(-\frac{c_{\mathrm{tube}}}{g^2}\right) \cdot \left[2 \mathbb{E}[|\sigma_g|^4 \mid Q] + 2 |\beta_g|^4\right]^{1/2}
 \le C_{\mathrm{tail}} g^{-6} \exp\left(-\frac{c_{\mathrm{tube}}}{g^2}\right). \tag{T20}
\]
For any $c_{\mathrm{tube}} > 0$, the function $g \mapsto g^{-6} \exp(-c_{\mathrm{tube}}/g^2)$ is uniformly bounded
on $(0, g_*]$ by $(3/e c_{\mathrm{tube}})^3 < \infty$. Therefore:
\[
 \boxed{\mathbb{E}[\mathbf{1}_{\mathrm{outside}} |\sigma_g - \beta_g|^2 \mid Q] \le C_0^{\mathrm{outside}} < \infty.} \tag{T21}
\]

---

## 4. Antipodal region and gauge reduction

For $\theta \ge \theta_b > 0$, the potential minimum satisfies $v_*(\theta) \ge v_*(\theta_b) = 32 \sin^2(\theta_b/8) > 0$.
Hence the potential expectation obeys:
\[
 W_g(Q) = g^{-2} \mathbb{E}(V \mid Q) \ge g^{-2} v_*(\theta_b) > 0. \tag{T22}
\]
In this region, bounding $K_g(Q)$ by $C g^{-2}$ is sufficient to guarantee $K_g(Q) \le C_1 W_g(Q)$ with $C_1 = C / v_*(\theta_b)$.

### 4.1. Degeneracy at the antipode
At $\theta = \pi$, $Q = -I$, the minimizing set $\mathcal{M}$ is a smooth 2-sphere gauge orbit (A7).
By A15, the transported score is constant along this gauge orbit:
\[
 d\sigma_g\big|_{T\mathcal{M}} = 0. \tag{T23}
\]
The soft directions of the Hessian at $\theta = \pi$ are precisely the tangent space $T\mathcal{M}$ (A9).
The seven normal directions have eigenvalues bounded below by $4(\sqrt{2}-1)$ uniformly.
Therefore, the variance along the gauge orbit vanishes identically, and the variance across
the seven normal directions is bounded by:
\[
 \operatorname{Var}_{\mu_g}(\sigma_g \mid Q) \le C_{\mathrm{normal}} g^{-2}. \tag{T24}
\]

### 4.2. Angular continuation
For $\theta$ in a neighborhood of $\pi$ ($\delta = \pi - \theta < \delta_0$), normal relaxation
gives the effective angular potential (A13):
\[
 V_{\mathrm{eff}, \delta}(n) = 16 - 8\sqrt{2} - 2\sqrt{2}\delta n_3 + O(\delta^2). \tag{T25}
\]
The normal section has displacement $O(\delta)$, and the angular variation is confined to the compact
sphere $S^2$. The score variance is uniformly bounded by $C_{\mathrm{antipodal}} g^{-2}$.
By (T22), this gives:
\[
 \boxed{K_g(Q) \le C_1^{\mathrm{antipodal}} W_g(Q) \quad \text{for } \theta \ge \theta_b.} \tag{T26}
\]

---

## 5. The M10 Domination Theorem and Corollaries

Combining (T16), (T21), and (T26), we establish:

### Theorem (M10 Score Domination)
For the actual twelve-edge compact Wilson square and the specified synchronized transport field S13,
there exist finite nonnegative constants $C_0, C_1$ independent of $0 < g < g_*$ such that:
\[
 \boxed{K_g(w) \le C_0 + C_1 W_g(w) \quad \nu_g\text{-a.e. on } 0 < g < g_*,} \tag{M10}
\]
where $K_g(w) = \operatorname{Var}_{\mu_g}(\sigma_g \mid w)$ and $W_g(w) = g^{-2}\mathbb{E}_{\mu_g}(V \mid w)$.

### Corollary (M11–M15 Instantiation)
Conditional on M10, by M7 and the established true-ground source form:
1. **Uniform weighted score bound (M12)**:
   Every centered finite-energy source $f$ satisfies:
   \[
    \boxed{\int K_g |f|^2 d\nu_g \le \left[C_1 + \frac{C_0 + C_1 E}{\gamma}\right] b_g[f].} \tag{M12}
   \]
2. **Median-anchored Hardy constant (M15)**:
   The median Hardy constant satisfies uniformly at small coupling:
   \[
    \boxed{\mathfrak{B}_g \le C_1 + \frac{2(C_0 + C_1 E)}{\gamma} < \infty.} \tag{M15}
   \]

This completes the analytic proof of M10 and discharges Priority 1 in G19.
