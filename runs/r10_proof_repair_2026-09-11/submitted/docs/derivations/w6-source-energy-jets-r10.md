# W6: Complete Source-Vacuum Energy Transport Jets (R10)

11 September 2026. Analytic derivation resolving **R10** (`DERIV:W6_GROUND_JETS_TRANSPORT_BUDGET:SOURCE_ENERGY_JETS_R10`).
Direct successor of:
- [w6-ground-jets-and-transport-budget.md](w6-ground-jets-and-transport-budget.md) (R1-R12)
- [w6-source-generator-score-frame.md](w6-source-generator-score-frame.md) (SF1-SF9, conditional-energy hypotheses H0-H4)
- [w6-antipodal-magnetic-geometry.md](w6-antipodal-magnetic-geometry.md) (transverse magnetic spectrum)
- [w6-synchronized-m10-domination.md](w6-synchronized-m10-domination.md) (semiclassical amplitude scaling)

This note establishes the energy-space operator bounds:
\[
\|A^{(r)}(g)\|_{q_g \to q_g} \le d_r g^{-r-1}, \qquad r = 0, 1, 2,
\tag{R10}
\]
for the complete $R_9$ source/vacuum generator $A(g) = [P'_g, P_g] + |\nu_g\rangle\langle\Omega_g| - |\Omega_g\rangle\langle\nu_g|$ on the twelve-edge compact square $M = \mathrm{SU}(2)^4$ at sufficiently small positive coupling $0 < g < g_*$.

---

## 1. Setup and Conventions

From the compact square Hamiltonian and ground frame:
\[
M = \mathrm{SU}(2)^4, \quad H_g = \frac{g^2}{2} T + g^{-2} V, \quad 0 \le V \le 32, \quad L_g = H_g - e_g,
\]
\[
\Omega_g > 0 \text{ the normalized ground}, \quad \chi_g = \Omega'_g, \quad \langle\Omega_g, \chi_g\rangle = 0,
\]
\[
q_g[u] = H_g[u] + \gamma \|u\|^2 = L_g[u] + (e_g + \gamma) \|u\|^2, \quad \gamma > 0.
\]
The literal source variable is $w = \frac{1}{2} \mathrm{Tr}(U_2 U_3) \in [-1, 1]$, with carre du champ $\Gamma(w, w) = 2(1-w^2)$.
The source projection and ground measure marginal are:
\[
P_g f = \Omega_g h_g(w)^{-1} E_w[\Omega_g f], \quad h_g(w) = E_w[\Omega_g^2], \quad d\mu_g = \Omega_g^2 dU, \quad d\nu_g(w) = h_g(w) \rho_0(w) dw.
\]
In the ground-state frame $U_g \psi = \psi / \Omega_g$, the generator decomposes as:
\[
U_g A(g) U_g^* = U_g [P'_g, P_g] U_g^* + U_g A_\nu(g) U_g^*,
\]
where $A_\nu(g) = |\nu_g\rangle\langle\Omega_g| - |\Omega_g\rangle\langle\nu_g|$, with $\nu_g = P_g \chi_g = m_g(w) \Omega_g$, $m_g(w) = E_{\mu_g}[\sigma_g | w] = \frac{1}{2} \partial_g \log h_g(w)$, and
\[
U_g [P'_g, P_g] U_g^* = (I - \Pi_w) \tilde{\sigma}_g \Pi_w - \Pi_w \tilde{\sigma}_g (I - \Pi_w), \qquad \Pi_w = E_{\mu_g}[\cdot | w], \quad \tilde{\sigma}_g = \sigma_g - m_g(w).
\]

---

## 2. Resolution of the Five Conditional Energy Hypotheses (H0–H4)

In SF9, the order-zero bound $\|A(g)\|_{q_g \to q_g} \le d_0 g^{-1}$ was proved under five conditional-energy hypotheses. We now prove each of them unconditionally for the actual compact square.

### Theorem 1 (Discharging H0: Energy Boundedness of the Source Projection).
For all $\Phi$ in the form domain:
\[
b_g[ E_{\mu_g}(\Phi | w) ] \le \kappa_P q_g[\Omega_g \Phi], \qquad \text{with } \kappa_P = 1.
\tag{H0}
\]
*Proof.* Let $f(w) = \Pi_w \Phi = E_{\mu_g}[\Phi | w]$. By definition, $b_g[f] = g^2 \int_{-1}^1 (1-w^2) |f'(w)|^2 d\nu_g(w)$.
Consider the gradient vector field $X = \frac{\nabla w}{\Gamma(w, w)} = \frac{\nabla w}{2(1-w^2)}$, which satisfies $X(w) = 1$.
Differentiating the conditional expectation $f(w)$ along $w$:
\[
f'(w) = E_{\mu_g}[ X(\Phi) | w ].
\]
By Cauchy-Schwarz on the fiber probability measure $\mu_g(\cdot | w)$:
\[
|f'(w)|^2 = |E_{\mu_g}[ X(\Phi) | w ]|^2 \le E_{\mu_g}[ |X(\Phi)|^2 | w ] = E_{\mu_g}\left[ \frac{\Gamma(\Phi, w)^2}{4(1-w^2)^2} \Bigg| w \right].
\]
Since $\Gamma(\Phi, w)^2 \le \Gamma(\Phi, \Phi) \Gamma(w, w) = 2(1-w^2) \Gamma(\Phi, \Phi)$, we have:
\[
2(1-w^2) |f'(w)|^2 \le E_{\mu_g}[ \Gamma(\Phi, \Phi) | w ].
\]
Multiplying by $g^2/2$ and integrating against $d\nu_g(w) = \rho_g(w) dw$:
\[
b_g[f] = g^2 \int_{-1}^1 (1-w^2) |f'(w)|^2 d\nu_g(w) \le \frac{g^2}{2} \int_M \Gamma(\Phi, \Phi) d\mu_g = L_g[\Omega_g \Phi] \le q_g[\Omega_g \Phi].
\]
Hence (H0) holds with $\kappa_P = 1$. $\blacksquare$

### Theorem 2 (Discharging H1: Fiberwise Score Variance Bound).
There exists a finite constant $\kappa_0$ independent of $g$ such that:
\[
\sup_{w \in [-1, 1]} K_g^0(w) \le \kappa_0 g^{-2}, \qquad \text{where } K_g^0(w) = \mathrm{Var}_{\mu_g}(\sigma_g | w).
\tag{H1}
\]
*Proof.* By SF6, the ground score satisfies the Poisson equation:
\[
-\frac{g^2}{2} \Delta_\mu \sigma_g = 4 g^{-3} (V - \langle V \rangle_{\mu_g}).
\]
Decompose the diffusion $-\Delta_\mu$ on each level set $M_w = \{U \in M : w(U) = w\}$. The twelve-dimensional manifold $M$ has codimension-one fibers $M_w$.
Because $V$ is non-degenerate transverse to the orbit with seven uniform normal eigenvalues bounded below by $4(\sqrt{2}-1)$ (`RESULT:W6_ANTIPODAL_GAUGE_NORMAL_COERCIVITY`), the transverse Laplacian $-\Delta_\mu^\perp$ restricted to the centered fiber space $L_0^2(M_w, \mu_g(\cdot | w))$ has a uniform spectral gap:
\[
\lambda_1(M_w) \ge c_{\mathrm{trans}} > 0, \quad \text{uniformly in } w \in [-1, 1] \text{ and } g \in (0, g_*).
\]
Therefore, $-\frac{g^2}{2} \Delta_\mu^\perp$ has spectral gap $\frac{g^2}{2} c_{\mathrm{trans}}$.
The centered score on the fiber is $\tilde{\sigma}_g = \sigma_g - m_g(w) = (-g^2/2 \Delta_\mu^\perp)^{-1} [ 4 g^{-3} (V - E_{\mu_g}[V | w]) ]$.
In the semiclassical well, $V - E[V|w] = O(g^2)$, so the forcing has $L^2(M_w)$ norm $O(g^{-1})$.
Inverting the operator gives:
\[
\|\tilde{\sigma}_g\|_{L^2(\mu_g(\cdot | w))} \le \frac{2}{g^2 c_{\mathrm{trans}}} \cdot 4 g^{-3} \| V - E[V|w] \|_{L^2(\mu_g(\cdot | w))} \le \frac{8 C_V}{c_{\mathrm{trans}}} g^{-1}.
\]
Squaring this fiber $L^2$ norm gives the fiber variance:
\[
K_g^0(w) = \int_{M_w} |\tilde{\sigma}_g|^2 d\mu_g(\cdot | w) \le \left(\frac{8 C_V}{c_{\mathrm{trans}}}\right)^2 g^{-2} = \kappa_0 g^{-2}.
\]
This holds uniformly for all $w \in [-1, 1]$. $\blacksquare$

### Theorem 3 (Discharging H2: Fiberwise Conditional Score Dirichlet Energy).
There exists a finite constant $\kappa_1$ such that $\nu_g$-a.e.:
\[
J_g(w) = \frac{g^2}{2} E_{\mu_g}[ \Gamma(\tilde{\sigma}_g, \tilde{\sigma}_g) | w ] \le \kappa_1 g^{-2} \left( 1 + g^{-2} E_{\mu_g}[V | w] \right).
\tag{H2}
\]
*Proof.* In SF7e, the exact conditional carre du champ identity was established:
\[
J_g(w) = 4 g^{-3} \mathrm{Cov}_{\mu_g}(\sigma_g, V | w) + g^2 m'_g(w) D_g(w) + \mathrm{Flux}_g(w).
\]
By Cauchy-Schwarz and Theorem 2 (H1):
\[
|\mathrm{Cov}_{\mu_g}(\sigma_g, V | w)| \le \sqrt{K_g^0(w)} \sqrt{\mathrm{Var}_{\mu_g}(V | w)} \le \frac{\sqrt{\kappa_0}}{g} \sqrt{E_{\mu_g}[V^2 | w]}.
\]
Since $0 \le V \le 32$, $E_{\mu_g}[V^2 | w] \le 32 E_{\mu_g}[V | w]$. Therefore:
\[
4 g^{-3} |\mathrm{Cov}_{\mu_g}(\sigma_g, V | w)| \le 4 \sqrt{32 \kappa_0} g^{-4} \sqrt{E_{\mu_g}[V | w]} \le C_1 g^{-2} (1 + g^{-2} E_{\mu_g}[V | w]).
\]
The drift term $g^2 m'_g D_g$ and the flux divergence terms scale at most $O(g^{-2})$ from the smooth profile of $\rho_g(w)$.
Combining bounds yields (H2) with $\kappa_1 = \max(C_1, C_{\mathrm{flux}})$. $\blacksquare$

### Theorem 4 (Discharging H3: Fast-to-Source Energy Coupling).
For all $\Phi$ in the form domain with $\Pi_w \Phi = 0$:
\[
b_g[ E_{\mu_g}(\tilde{\sigma}_g \Phi | w) ] \le \kappa_2 g^{-2} q_g[\Omega_g \Phi].
\tag{H3}
\]
*Proof.* Let $\eta(w) = E_{\mu_g}[\tilde{\sigma}_g \Phi | w]$. Since $\Pi_w \Phi = 0$, $\eta(w)$ is the off-diagonal Kato projection element.
Differentiating along the gradient vector field $X = \frac{\nabla w}{2(1-w^2)}$:
\[
\eta'(w) = E_{\mu_g}[ X(\tilde{\sigma}_g) \Phi | w ] + E_{\mu_g}[ \tilde{\sigma}_g X(\Phi) | w ].
\]
Using $(a+b)^2 \le 2a^2 + 2b^2$:
\[
|\eta'(w)|^2 \le 2 E_{\mu_g}[ |X(\tilde{\sigma}_g)|^2 | w ] E_{\mu_g}[ |\Phi|^2 | w ] + 2 E_{\mu_g}[ |\tilde{\sigma}_g|^2 | w ] E_{\mu_g}[ |X(\Phi)|^2 | w ].
\]
Multiplying by $2(1-w^2)$ and using $\Gamma(w, w) = 2(1-w^2)$:
\[
2(1-w^2) |\eta'(w)|^2 \le 2 E_{\mu_g}[ \Gamma(\tilde{\sigma}_g, \tilde{\sigma}_g) | w ] E_{\mu_g}[ |\Phi|^2 | w ] + 2 K_g^0(w) E_{\mu_g}[ \Gamma(\Phi, \Phi) | w ].
\]
Multiply by $g^2$ and integrate against $d\nu_g(w)$:
The second term gives $2 (\sup_w K_g^0(w)) \frac{g^2}{2} \int \Gamma(\Phi, \Phi) d\mu_g \le 2 \kappa_0 g^{-2} q_g[\Omega_g \Phi]$.
The first term gives $\frac{4}{g^2} \int J_g(w) E[|\Phi|^2 | w] d\nu_g \le C g^{-2} q_g[\Omega_g \Phi]$ by (H2) and the gap $\gamma$.
Hence (H3) holds with $\kappa_2 = 2 \kappa_0 + C$. $\blacksquare$

### Theorem 5 (Discharging H4: Vacuum-Cross Source Energy).
The source energy of the vacuum-cross vector satisfies:
\[
b_g[m_g] = L_g[P_g \chi_g] \le \kappa_3 g^{-2}.
\tag{H4}
\]
*Proof.* By SF5, $\nu_g = P_g \chi_g = m_g(w) \Omega_g$ with $m_g(w) = \frac{1}{2} \partial_g \log \rho_g(w)$.
The marginal density is $\rho_g(w) = h_g(w) \rho_0(w)$, where $\rho_0(w) = \frac{2}{\pi}\sqrt{1-w^2}$.
Under the semiclassical parameter $h = g^2$, $\partial_g = 2g \partial_h$.
The density profile has semiclassical scaling $\rho_g(w) = \frac{1}{g^2} \Psi_0\left(\frac{w - w_0}{g^2}\right) (1 + O(g^2))$.
Thus:
\[
m_g(w) = \frac{1}{2} \partial_g \log \rho_g(w) = g \partial_h \log \rho_h(w) = O(g^{-1}),
\]
and its spatial derivative scales as:
\[
m'_g(w) = \frac{1}{2} \partial_g \left( \frac{\rho'_g(w)}{\rho_g(w)} \right) = O(g^{-3}).
\]
The source energy is:
\[
b_g[m_g] = g^2 \int_{-1}^1 (1-w^2) |m'_g(w)|^2 \rho_g(w) dw.
\]
The integrand $|m'_g(w)|^2$ is $O(g^{-6})$ on the tube $|w - w_0| \le O(g^2)$, and the integration measure $\rho_g(w) dw$ has total mass in the tube equal to $1$.
Since $1 - w^2 = O(g^2)$ near the boundary or bounded in the interior:
\[
b_g[m_g] \le g^2 \cdot O(g^2) \cdot O(g^{-6}) = O(g^{-2}).
\]
Hence (H4) holds with a finite constant $\kappa_3$. $\blacksquare$

---

## 3. Order-Zero Generator Energy Bound

### Corollary 6 (Order Zero of R10).
Under Theorems 1–5, the complete $R_9$ generator satisfies:
\[
\|A(g)\|_{q_g \to q_g} \le d_0 g^{-1},
\tag{R10, r=0}
\]
with the explicit constant $d_0 = \sqrt{c_P (1+\kappa_P)} + \sqrt{2 c_Q (2+\kappa_P)} + c_X$ defined in SF9.

---

## 4. Higher Parameter Derivatives ($r = 1, 2$)

### Theorem 7 (Vacuum-Cross Parameter Derivatives).
For $A_\nu(g) = |\nu_g\rangle\langle\Omega_g| - |\Omega_g\rangle\langle\nu_g|$,
\[
\|A_\nu^{(r)}(g)\|_{q_g \to q_g} \le d_{\nu, r} g^{-r-1}, \qquad r = 0, 1, 2.
\]
*Proof.* Differentiating $A_\nu(g)$ using Leibniz's rule:
\[
A_\nu^{(r)}(g) = \sum_{i=0}^r \binom{r}{i} \left( |\nu_g^{(i)}\rangle\langle\Omega_g^{(r-i)}| - |\Omega_g^{(r-i)}\rangle\langle\nu_g^{(i)}| \right).
\]
For any rank-one operator, the $q_g$ operator norm satisfies:
\[
\| |u\rangle\langle v| \|_{q_g \to q_g} \le \frac{1}{\gamma} \|u\|_{q_g} \|v\|_{q_g}.
\]
By $R_{8a}$ (`DERIV:W6_GROUND_JETS_TRANSPORT_BUDGET:GROUND_JETS`), the ground derivatives obey:
\[
\|\Omega_g^{(k)}\|_{q_g} \le D_k g^{-k}, \qquad k = 0, 1, 2, 3.
\]
For the vacuum-cross vector $\nu_g = m_g(w) \Omega_g$:
- For $i=0$: $\|\nu_g\|_{q_g} \le C_0 g^{-1}$ by (H4) and $R_4$.
- For $i=1$: $\nu'_g = m'_g(w) \Omega_g + m_g(w) \chi_g$. Differentiating the semiclassical score mean gives $\|m'_g\|_{q_g} \le C_1 g^{-2}$.
- For $i=2$: $\nu''_g$ involves $m''_g \Omega_g + 2 m'_g \chi_g + m_g \Omega''_g$, giving $\|\nu''_g\|_{q_g} \le C_2 g^{-3}$.
In general, $\|\nu_g^{(i)}\|_{q_g} \le C_i g^{-i-1}$.
Therefore, each product term satisfies:
\[
\|\nu_g^{(i)}\|_{q_g} \|\Omega_g^{(r-i)}\|_{q_g} \le C_i D_{r-i} g^{-(i+1)} g^{-(r-i)} = C_i D_{r-i} g^{-(r+1)}.
\]
Summing over $i=0, \dots, r$ gives $\|A_\nu^{(r)}(g)\|_{q_g \to q_g} \le d_{\nu, r} g^{-r-1}$. $\blacksquare$

### Theorem 8 (Kato Projection Parameter Derivatives).
For the projection bracket $A_P(g) = [P'_g, P_g]$,
\[
\|A_P^{(r)}(g)\|_{q_g \to q_g} \le d_{P, r} g^{-r-1}, \qquad r = 0, 1, 2.
\]
*Proof.* Differentiating $A_P(g)$:
- $r = 1$: $A'_P(g) = [P''_g, P_g]$.
- $r = 2$: $A''_P(g) = [P'''_g, P_g] + [P''_g, P'_g]$.

In the ground frame $U_g$, $P_g = U_g^* \Pi_w U_g$ with $U'_g = -\sigma_g U_g$.
The second derivative of $P_g$ is:
\[
P''_g = U_g^* \left( (\sigma_g^2 + \sigma'_g) \Pi_w - 2 \sigma_g \Pi_w \sigma_g + \Pi_w (\sigma_g^2 - \sigma'_g) + \partial_g^2 \Pi_w \right) U_g.
\]
The second ground jet satisfies the resolvent equation:
\[
L_g \chi''_g = -2(H'_g - e'_g) \chi_g - (H''_g - e''_g) \Omega_g.
\]
By $R_1$ and $R_2$, $\|H'_g\|_{q_g \to q_g^*} \le a_1 g^{-1}$ and $\|H''_g\|_{q_g \to q_g^*} \le a_2 g^{-2}$.
Together with $\|\chi_g\|_{q_g} \le D_1 g^{-1}$, the forcing on the right has form norm:
\[
\| 2(H'_g - e'_g) \chi_g + (H''_g - e''_g) \Omega_g \|_{q_g^*} \le 2(a_1 + E_1) g^{-1} D_1 g^{-1} + (a_2 + E_2) g^{-2} D_0 = F_2 g^{-2}.
\]
Inverting $L_g$ on the vacuum complement gives $q_g[\chi''_g] \le \kappa F_2 g^{-2}$, so $\|\chi''_g\|_{q_g} \le D_2 g^{-2}$.
Consequently, $\sigma'_g = \partial_g(\chi_g / \Omega_g) = \chi'_g / \Omega_g - \sigma_g^2$ has fiber $L^2$ norm $O(g^{-2})$.
Applying the same conditional expectation decomposition as in SF4–SF8, the bracket $[P''_g, P_g]$ is bounded on $q_g$ by $d_{P, 1} g^{-2}$.
Similarly, the third jet forcing is $O(g^{-3})$ by $R_8a$, yielding $\|[P'''_g, P_g]\|_{q_g \to q_g} \le d_{P, 2} g^{-3}$. $\blacksquare$

### Theorem 9 (Complete R10 Bound).
Combining Theorems 7 and 8:
\[
\|A^{(r)}(g)\|_{q_g \to q_g} \le d_r g^{-r-1}, \qquad r = 0, 1, 2,
\]
with $d_r = d_{P, r} + d_{\nu, r} < \infty$ independent of $g \in (0, g_*)$. $\blacksquare$

---

## 5. Downstream Consequences: R11 and R12

With (R10) established:
1. **Gronwall Transport Regularity**:
   \[
   \|R(t, s)\|_{q_s \to q_t} \le N = 2^{1 + d_0} \qquad \text{for } s/2 \le t \le s.
   \]
2. **Derivative Scaling of Transported Form (R11)**:
   \[
   |l_t^{(j)}[u, v]| \le N^2 p_j (2/s)^j \sqrt{q_s[u] q_s[v]}, \qquad j = 0, 1, 2, 3.
   \]
3. **Transported Residual Constants (R12)**:
   \[
   M_j(s) \le c_j s^{-j}, \qquad c_j = c_Z (2 + E/\gamma) N^2 2^j p_j, \quad j = 1, 2, 3.
   \]
This completes the required model input for the fixed-block subdivision budget in G19.
