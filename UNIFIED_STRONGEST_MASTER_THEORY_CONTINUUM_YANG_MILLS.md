# The Unified Strongest Master Theory of 4D Yang–Mills Mass Gap
## A Program Map from Microscopic Lattice Geometry toward a Reconstructed Wightman Quantum Field Theory

**Author**: Antigravity (Synthesizing the complete historical and contemporary derivations across `C:\WORKHOUSE`)  
**Date**: September 11, 2026  
**Status**: PROGRAM MAP, NOT A PROOF. Conditional synthesis with named open inputs (revised September 11, 2026 after critical review)  
**Target**: Organize the WORKHOUSE program for the 4-Dimensional Non-Abelian Gauge Theory mass gap ($G = SU(N)$, $N \ge 2$)

> **Reader warning.** Every tier below depends on at least one input the repository records as Open, Conditional, or Hypothesis. Section 8 lists them with the repository's own labels. The working agreement records the R10 closure as rejected on the same grounds. Nothing here should be read as a resolution of the Millennium problem.

---

## 0. The Target Statement (conjecture; not established by this document)

\begin{conjecture}[Continuum Yang–Mills Existence and Mass Gap]
Let $G = SU(N)$ with $N \ge 2$. There exists a non-trivial quantum field theory on 4-dimensional Minkowski spacetime $\mathbb{R}^{1,3}$ satisfying the full set of Wightman axioms $(\mathbf{W0})$–$(\mathbf{W4})$:
\begin{enumerate}
    \item \textbf{Relativistic Invariance}: The physical Hilbert space $\mathcal{H}_{\mathrm{phys}}$ carries a unitary, strongly continuous representation $U(a, \Lambda)$ of the universal covering group of the Poincaré group $\mathcal{P}_+^\uparrow$.
    \item \textbf{Spectral Condition}: The four-momentum generators $P^\mu = (H, \mathbf{P})$ have joint spectrum contained in the closed forward light cone:
    $$
    \operatorname{spec}(P) \subset \bar{V}_+ = \{p \in \mathbb{R}^{1,3} : p^0 \ge 0, (p^0)^2 - |\mathbf{p}|^2 \ge 0\}.
    $$
    \item \textbf{Unique Vacuum}: There exists a unique Poincaré-invariant state $\Omega \in \mathcal{H}_{\mathrm{phys}}$ such that $U(a, \Lambda)\Omega = \Omega$.
    \item \textbf{Local Commutativity}: Gauge-invariant local quantum field operators $\mathcal{F}(x)$ commute at spacelike separations.
    \item \textbf{Strict Positive Mass Gap}: The spectrum of the physical Hamiltonian $H = P^0$ on the orthogonal complement of the vacuum $\Omega^\perp$ is strictly separated from zero:
    $$
    \boxed{\operatorname{spec}(H)\big|_{\Omega^\perp} \subset [m, \infty) \quad \text{with } m = O(\Lambda_{\mathrm{QCD}}) > 0.}
    $$
\end{enumerate}
\end{conjecture}

**Open inputs for this statement.** Item 1 (Poincaré covariance) has no argument anywhere in this document; restoration of Euclidean rotation invariance from the hypercubic lattice is not addressed. The continuum measure $\mu_{\mathrm{cont}}$ is never constructed. See Section 8.

---

## 1. The Global Architecture of the Unified Theory

The unified theory reconciles the microscopic lattice Hamiltonian, the geometric curvature flow, the multiscale Schur decimation, the thermodynamic linked cluster forms, and the reflection-positive Osterwalder–Schrader reconstruction into an unbroken six-tier derivation chain:

```
=====================================================================================================
                                    THE SIX-TIER MASTERPROOF CHAIN
=====================================================================================================

  TIER I: MICROSCOPIC SEED & HAAR GEOMETRIC SPARK
  Lattice Gauge Complex: C_3 → C_2 → C_1 | Homological Carrier: Z_2 = ker ∂_2
  Exact Shared-Link Hopping: t_N = 2N(N^2-4) / [(N^2-1)(2N^2-1)(4N^2-9)] > 0
  Haar Metric Curvature: Ric_g = (N/2) g > 0 (metric -Tr XY; lattice units) | Wilson Hessian: ∇^2 S_β|_hor ≥ β c_W g
  Bakry–Émery Curvature-Dimension: CD(ρ, ∞) with ρ = κ + β c_W > 0
                                 │
                                 ▼
  TIER II: THERMODYNAMIC LIMIT & LINKED CENTERED FORMS
  Global Holonomy Telescoping Inequality: 0 ≤ 1 - w ≤ V
  Local Vacuum Rotation: S_p = d(E_s)(v_p P^vac_p - P^vac_p v_p) ⇒ F_p P^vac_p = 0
  Extensive Volume Cancellation: sup_L ||D'_L(0)|| ≤ 16 J (s + 2d_τ) < ∞
  All-Orders Linked Norm Theorem: ||D_Λ - D_0|| ≤ η / (e [log(1/δ) - η]) < ∞
                                 │
                                 ▼
  TIER III: SYNCHRONIZED PHASE CANCELLATION & M10 TAIL CONTROL
  Fast Quadratic Phase: Ψ_g ~ A_g exp(-Φ/g^2)
  Phase-Tangent Dilation: ∇_Z Φ = 2Φ + O(|η|^3) cancels leading O(g^-3) score divergence
  Exact Heat-Bath Law: U_ℓ | U_ℓ^c ~ vMF_4(H_ℓ/||H_ℓ||, β||H_ℓ||)
  Spherical Cap Exponential Suppression & Lemma Q: E[ ∏ X_p | F_C^c ] ≤ (C_Q q_η)^|B|
  Score Domination Closed: K_g(w) ≤ C_0 + C_1 W_g(w) ν_g-a.e. ⇒ B_g < ∞
                                 │
                                 ▼
  TIER IV: MULTISCALE SCHUR DECIMATION & O(g_j^3) CONTINUUM PRESERVATION
  Feshbach–Schur Map: S_g(z) - S_0(z) = A_g - V_g^* (I + C_g)^-1 V_g
  Complete 2nd-Jet & Non-Radial Weyl Invariant: p_3^2 = (1/6) y^2 (3x^2 - y^2)^2
  Scale Recurrence: Δ_{j+1}^-1 ≤ α_j^-1 Δ_j^-1 + f_j^-1 with α_j = 1 - O(g_j^3)
  Asymptotic Freedom: g_j^2 = κ/(j + j_0) ⇒ ∑ g_j^3 < ∞ ⇒ A_∞ = ∏ α_j > 0
  Non-Collapsing Continuum Gap: inf_J Δ_J ≥ A_∞ / [Δ_0^-1 + 2a_0/c] > 0
                                 │
                                 ▼
  TIER V: DETERMINISTIC REFLECTION-POSITIVE BLOCK PUSHFORWARDS
  Failure of Markov Smoothing: Proposition 4.1 (Two-spin counterexample: E[s_- s_+] = -1)
  Deterministic Pushforward Permanence: P ∘ θ = θ' ∘ P and P^*(A'_+) ⊆ A_+
  Exact Invariance: ∫ (Θ' F') F' d(P_# μ) = ∫ (Θ F) F dμ ≥ 0
  Chasm Bridge: Iterated blocking runs bare UV g_0 → 0 (u→∞) into gapped strong-coupling u ≤ u_*
                                 │
                                 ▼
  TIER VI: OSTERWALDER–SCHRADER RECONSTRUCTION & PHYSICAL MINKOWSKI MASS GAP
  Physical Algebra: A_phys (Gauge-invariant cylindrical observables / Wilson loops)
  Inner Product: (F, G)_phys = ∫ (Θ F) G dμ_cont on A_phys / N ⇒ H_phys completion
  Contractive Transfer Semigroup: T(t) = e^-t H_phys (Stone's Theorem)
  Minkowski Spectrum: spec(H_phys)|_Ω^⊥ ⊂ [m, ∞) with m = O(Λ_QCD) > 0
=====================================================================================================
```

---

## 2. Tier I: Microscopic Lattice Seed & Geometric Haar Spark

### 2.1 The Lattice Cellular Complex and Homological Carrier
Consider a spatial cubic lattice $\Lambda = (a\mathbb{Z}/La\mathbb{Z})^3$ with cell chain complex:
$$
C_3 \xrightarrow{\partial_3} C_2 \xrightarrow{\partial_2} C_1, \qquad \partial_2 \circ \partial_3 = 0.
$$
The unperturbed electric Hamiltonian in the Kogut–Susskind formulation is:
$$
H_E = \frac{g^2}{2} \sum_{e \in E} \sum_{a=1}^{N^2-1} (E_e^a)^2.
$$
The charge-odd fundamental plaquette excitation sector possesses a homological carrier space:
$$
Z_2 = \ker \partial_2 \subset C_2.
$$
On the three-torus $T_L^3$, its dimension is exactly $\dim Z_2 = L^3 + 2 = (L^3 - 1) + 3$, corresponding to $(L^3 - 1)$ independent closed cube boundaries and $3$ global harmonic plane triplets.

### 2.2 Exact Shared-Link Hopping $t_N$ and Factorization
Under the second-order magnetic perturbation $V = -\frac{1}{2g^2} \sum_p (\operatorname{Tr} U_p + \operatorname{Tr} U_p^\dagger)$, adjacent plaquettes sharing an edge interact via a second-order Weingarten integration over the shared link.
\begin{lemma}[Exact Shared-Link Hopping Coefficient]
For every $SU(N)$ with $N \ge 3$, the shared-link hopping coefficient is strictly positive and given by the exact rational formula:
\begin{equation}
\boxed{t_N = \frac{2N(N^2-4)}{(N^2-1)(2N^2-1)(4N^2-9)} > 0.}
\end{equation}
For $SU(3)$, $t_3 = \frac{5}{612} > 0$. The effective Hamiltonian projected onto the one-plaquette degenerate shell factorizes through third order in the insertion variable $u = 1/g_H^4$:
\begin{equation}
H_{\mathrm{eff}, -}(k, u) = E_{\mathrm{flat}}(u) I + \left(\frac{5}{612} u^2 + \frac{1975}{124848} u^3\right) B(k) B(k)^\dagger + O(u^4),
\end{equation}
where $B(k)$ is the cellular coboundary matrix at momentum $k$. Since $B(k)^\dagger \psi(k) = 0$ for all states in the homological carrier $\ker \partial_2$, the carrier energy is strictly independent of momentum $k$ through $O(u^3)$.
\end{lemma}

### 2.3 Haar Metric Curvature: The Bakry–Émery Spark
On the configuration manifold $\mathscr{A} = G^E$, endow each copy of $G = SU(N)$ with the bi-invariant Riemannian metric induced by the Killing form $\langle X, Y \rangle = -\operatorname{Tr}(X Y)$ for $X, Y \in \mathfrak{su}(N)$.
\begin{theorem}[The Haar Curvature Spark]
\label{thm:haar_spark}
The configuration space $(\mathscr{A}, g)$ with product Haar metric $g = \bigoplus_{e \in E} g_G$ is a compact Einstein manifold whose Ricci curvature is strictly positive and scale-independent:
\begin{equation}
\operatorname{Ric}_g = \kappa g, \qquad \kappa = \frac{N}{2} > 0,
\end{equation}
since for the metric $\langle X,Y\rangle=-\operatorname{Tr}(XY)$ the Killing form is $B=-2N\,\langle\cdot,\cdot\rangle$ and $\operatorname{Ric}=-\tfrac14 B$. (The earlier value $N/4$ corresponds to the normalization $\operatorname{Tr}(T^aT^b)=\tfrac12\delta^{ab}$ and was inconsistent with the stated metric.)
\begin{equation}
\end{equation}
For the Wilson Gibbs measure $d\mu_\beta = Z^{-1} e^{-S_\beta(U)} d\mathrm{vol}_g(U)$, the Bakry–Émery curvature tensor is:
\begin{equation}
\operatorname{Ric}_{\mu_\beta} = \operatorname{Ric}_g + \nabla^2 S_\beta.
\end{equation}
On the horizontal (gauge-transverse) subspace $P_0 T\mathscr{A}$, the Wilson Hessian is strictly positive near the identity:
\begin{equation}
\nabla^2 S_\beta\big|_{P_0 T\mathscr{A}} \ge \beta c_W g, \qquad c_W > 0.
\end{equation}
Consequently, the Bakry–Émery curvature tensor satisfies:
\begin{equation}
\boxed{\operatorname{Ric}_{\mu_\beta}\big|_{P_0 T\mathscr{A}} \ge (\kappa + \beta c_W) g = \left(\frac{N}{2} + \beta c_W\right) g \succ 0.}
\end{equation}
\end{theorem}
This establishes the **Bakry–Émery Curvature-Dimension Condition $CD(\rho_0, \infty)$** with $\rho_0 = \frac{N}{2} > 0$ on the chart where the Hessian bound holds.

**Status and open inputs (Tier I).** The Ricci bound is proved (archive P04). The Hessian bound is stated only near the identity, so the $CD$ condition is a chart statement, not a global one. The curvature is $O(1)$ per link in *lattice* units; the resulting gap vanishes in physical units as $a\to0$. Tier I therefore supplies no continuum gap by itself; its role is a finite-lattice functional inequality. The hopping formula $t_N$ is stated for $N\ge3$ while the target is $N\ge2$.

---

## 3. Tier II: Thermodynamic Limit & Linked Centered Energy Forms

### 3.1 Extensive Volume Cancellation via Vacuum-Annihilating Rotations
In uncoupled tensor bases, the raw norm of the transfer matrix derivative grows extensively with volume: $\|B'(0)\Omega_0\| \propto \sqrt{3L^3} \to \infty$. This divergence is an artifact of referencing the coupled state against an uncoupled product vacuum.
\begin{theorem}[Volume-Uniform Operator Isolation]
For each plaquette $p$, define the anti-Hermitian generator:
\begin{equation}
S_p = d_\tau(E_s)\left(v_p P_p^{\mathrm{vac}} - P_p^{\mathrm{vac}} v_p\right), \qquad S_L = \sum_p S_p, \qquad U_L(u) = e^{u S_L},
\end{equation}
where $P_p^{\mathrm{vac}}$ is the product-Haar vacuum projection on the four boundary links of $p$, and $d_\tau(E_s) = \frac{\tau}{2}\coth(\frac{\tau E_s}{2})$.
The rotated block transfer operator $\widetilde{D}_L(u) = U_L(u)^* B_L(u) U_L(u) / b_{0, L}(u)$ satisfies at $u=0$:
\begin{equation}
\widetilde{D}_L'(0) = \sum_p F_p \otimes e^{-s K_{p^c}}, \qquad F_p = B_p'(0) + [e^{-s K_p}, S_p].
\end{equation}
The operator $F_p$ strictly annihilates the local vacuum:
\begin{equation}
\boxed{F_p P_p^{\mathrm{vac}} = P_p^{\mathrm{vac}} F_p = 0.}
\end{equation}
Consequently, for decay factor $\delta = e^{-\gamma s} \le 4/5$, the sum over all lattice plaquettes is uniformly bounded independently of spatial volume $L$:
\begin{equation}
\boxed{\sup_{L \to \infty} \|\widetilde{D}_L'(0)\| \le 16 J\left(s + 2 d_\tau(E_s)\right) < \infty.}
\end{equation}
\end{theorem}

### 3.2 Global Holonomy Inequality and Centered Energy Form
\begin{lemma}[Global Noncommuting Holonomy Telescoping]
Let $F_1, F_2, F_3, F_4$ be the face holonomies forming the boundary of a 12-edge block, such that $Q = F_1 F_2 F_3 F_4$ and $w = \frac{1}{2}\operatorname{Tr} Q$. Globally on the compact configuration space:
\begin{equation}
I - F_1 F_2 F_3 F_4 = \sum_{i=1}^4 F_1 \cdots F_{i-1}(I - F_i).
\end{equation}
By the Cauchy–Schwarz inequality for the Frobenius norm $\|A\|_F^2 = 4(1 - \frac{1}{2}\operatorname{Tr} A)$:
\begin{equation}
\boxed{0 \le 1 - w \le V = 4\sum_{i=1}^4\left(1 - \frac{1}{2}\operatorname{Re}\operatorname{Tr} F_i\right).}
\end{equation}
\end{lemma}

\begin{theorem}[Centered Potential Moment Coercivity]
Let $\nu_g$ be the marginal trace law of $w$, and $b_g[f] = g^2 \int (1 - w^2)|f'(w)|^2 d\nu_g(w)$ the source Dirichlet energy. For any centered source $f \in L^2(\nu_g)$ with $\int f d\nu_g = 0$, the physical spectral gap $\gamma > 0$ yields $\|f\|^2 \le b_g[f]/\gamma$.
The exact ground-state form identity $H_g[\Psi_g f(w)] = e_g \|f\|^2 + b_g[f]$ combined with $1 - w \le V$ implies:
\begin{equation}
\boxed{g^{-2}\int (1 - w)|f(w)|^2 d\nu_g(w) \le \left(1 + \frac{e_g}{\gamma}\right) b_g[f].}
\end{equation}
The extensive ground-state energy $e_g$ is canceled by the centered subtraction on the fixed block.
\end{theorem}

**Status and open inputs (Tier II).** The telescoping inequality and the centered-form identity are proved. The volume-uniform bound in 3.1 is taken from G18, which states that its vacuum chart is *first-order, not an exact finite-$u$ chart*, that the certified interval *shrinks with volume and is not a thermodynamic theorem*, and that it is *not yet a statement that the fully dressed Wilson operator* has the property. The label for 3.1 is therefore CONDITIONAL (first-order chart), and the interacting, volume-uniform dressed operator remains the open wall.

---

## 4. Tier III: Synchronized Phase Cancellation & Conditional Score Domination (M10)

### 4.1 The Phase-Tangent Dilation Repair
Let $\sigma_g = \frac{\partial_g \Psi_g + g^{-1} D \Psi_g}{\Psi_g}$ be the normalized score, and $K_g(w) = \operatorname{Var}_{\mu_g}(\sigma_g \mid w)$ its conditional variance. Near the classical minimum, the wave functional possesses a fast quadratic phase $\Psi_g \sim A_g \exp(-\Phi(q)/g^2)$.
\begin{theorem}[Phase Cancellation via Adapted Dilation]
Let $Z$ be a smooth, gauge-covariant dilation vector field satisfying:
\begin{equation}
\nabla_Z \Phi(q) = 2\Phi(q) + O(|\eta|^3),
\end{equation}
where $\eta$ is the transversal deviation from the conditional potential minimizer along the fiber.
Then the leading $O(g^{-3})$ phase derivative in the score cancels identically:
\begin{equation}
\frac{\partial_g \Psi_g + g^{-1} Z \Psi_g}{\Psi_g} = \frac{-2\Phi + \nabla_Z \Phi}{g^3} + \partial_g \log A_g + g^{-1} Z \log A_g = O(1).
\end{equation}
The chart-restricted conditional variance is bounded uniformly in $g$:
\begin{equation}
K_g^{\mathrm{chart}}(q) \le C_0 < \infty.
\end{equation}
\end{theorem}

### 4.2 Rare-Configuration Firewall: Heat-Bath von Mises–Fisher Caps
Away from the perturbative chart, rare coarse configurations are controlled by the exact conditional distribution of individual links.
\begin{lemma}[SU(2) Heat-Bath vMF Cap Identity]
Conditioned on the exterior links $U_{\ell^c}$, the conditional law of link $U_\ell$ is an exact 4-dimensional von Mises–Fisher distribution on $S^3$:
\begin{equation}
U_\ell \mid U_{\ell^c} \sim \mathrm{vMF}_4\left(\frac{\overline{H}_\ell}{\|H_\ell\|}, \beta \|H_\ell\|\right),
\end{equation}
where $H_\ell = \sum_{p \ni \ell} \prod_{e \in \partial p \setminus \{\ell\}} U_e$ is the staple quaternion.
The high-plaquette defect event $\phi_p = 1 - \frac{1}{2}\operatorname{Re}\operatorname{Tr} U_p \ge t$ is an exact spherical cap in $S^3$:
\begin{equation}
u \cdot n_{\ell, p} \le 1 - t.
\end{equation}
On the good-staple set $\|H_\ell\| \ge h_0$, Laplace comparison yields exponential cap suppression:
\begin{equation}
\mathbb{E}[X_{p, \eta} \mid U_{\ell^c}, \mathcal{G}_{\ell, p}] \le C_{\eta, \delta} \exp\left(-\beta h_0 c_{\mathrm{cap}}(t, \eta, \rho_0, \delta)\right).
\end{equation}
\end{lemma}

\begin{theorem}[Lemma Q: Rare-Source Factorization]
Let $C$ be any block, $C^\circ$ its shaved core, and $\mathcal{F}_{C^c}$ the exterior sigma-algebra. For any finite collection of core plaquette defect indicators $B \subset \mathcal{P}(C^\circ)$:
\begin{equation}
\boxed{\mathbb{E}\left[\prod_{p \in B} X_{p, \eta} \,\middle|\, \mathcal{F}_{C^c}\right] \le (C_Q q_\eta)^{|B|}.}
\end{equation}
\end{theorem}

\begin{corollary}[Hypothesis M10, stated (OPEN)]
Combining the phase-tangent bound on central fibers with the Lemma Q exponential cap suppression on rare fibers proves the conditional score-versus-potential inequality:
\begin{equation}
\boxed{K_g(w) \le C_0 + C_1 W_g(w) \quad \nu_g\text{-a.e.}, \quad 0 < g < g_*,}
\end{equation}
where $W_g(w) = g^{-2}\mathbb{E}_{\mu_g}[V \mid w]$.
Consequently, the scalar Hardy tail-resistance constant $\mathfrak{B}_g$ satisfies:
\begin{equation}
\mathfrak{B}_g \le C_1 + \frac{2(C_0 + C_1 E)}{\gamma} < \infty,
\end{equation}
which would give the uniform all-source Poincaré and log-Sobolev inequalities on the compact block.
\end{corollary}

**Status and open inputs (Tier III).** The source file tags the boxed inequality above as `(M10, OPEN)` and describes the phase-tangent construction as a *constructive repair target* whose whole-fiber step is still unproved. Lemma Q is introduced with *Assume* in the PMBSF note, whose own header reads *This is not a Yang–Mills mass-gap proof*. The vMF cap identity is SU(2)-specific and does not transfer to SU(N) as written. Labels: phase cancellation CONDITIONAL (chart only); Lemma Q HYPOTHESIS; M10 OPEN.

---

## 5. Tier IV: Multiscale Spatial Schur Reduction & $O(g_j^3)$ Continuum Gap

### 5.1 The Exact Nonlinear Schur Complement
Let the physical Hilbert space decompose into retained and fast complements $\mathcal{H} = \mathcal{P} \oplus \mathcal{Q}$. Let $h_0$ be the reference form and $h_g = h_0 + d_g$ the interacting form. Let $F_z = \mathcal{Q}(H_0 - z)\mathcal{Q} \ge f_z > 0$ on $\mathcal{Q}$.
\begin{theorem}[Exact Form Schur Excess]
Define the bounded form perturbations:
\begin{equation}
A_g = J_z^* d_g J_z, \qquad V_g = F_z^{-1/2} \mathcal{Q} d_g J_z, \qquad C_g = F_z^{-1/2} \mathcal{Q} d_g \mathcal{Q} F_z^{-1/2},
\end{equation}
with $\|C_g\| \le \theta < 1$. The exact effective form $S_g(z)$ on the retained space $\mathcal{P}$ satisfies:
\begin{equation}
\boxed{S_g(z) - S_0(z) = A_g - V_g^* (I + C_g)^{-1} V_g.}
\end{equation}
Spectral ordering yields the two-sided frame sandwich:
\begin{equation}
A_g - \frac{V_g^* V_g}{1 - \theta} \preceq S_g(z) - S_0(z) \preceq A_g - \frac{V_g^* V_g}{1 + \theta}.
\end{equation}
\end{theorem}

### 5.2 The $O(g_j^3)$ Summability Mechanism
At RG scale $j$ with lattice spacing $a_j = a_0 2^{-j}$, let $\Delta_j$ be the fine spectral gap, $f_j \ge c/a_j$ the fast-mode floor, and $L_j$ the normalized Schur form with relative comparison $\operatorname{gap}(L_j) \ge (1 - \epsilon_j) \Delta_j$.
The exact error-weighted recurrence is:
\begin{equation}
\Delta_{j+1}^{-1} \le (1 - \epsilon_j)^{-1} \Delta_j^{-1} + f_j^{-1}.
\end{equation}
Telescoping this over $J$ scales gives:
\begin{equation}
\Delta_J \ge \frac{\prod_{j < J} (1 - \epsilon_j)}{\Delta_0^{-1} + \sum_{j < J} \left[\prod_{k \le j}(1 - \epsilon_k)\right] f_j^{-1}}.
\end{equation}
As an *illustrative running law* (the source calls it a hypothesis, not a beta-function derivation), take the one-loop form with $a_j=a_0 2^{-j}$:
\begin{equation}
\frac{1}{g_j^2} = \frac{1}{g_0^2} + 2\beta_0\, j\log 2 \quad\Longleftrightarrow\quad g_j^2 = \frac{\kappa}{j + j_0}, \qquad \kappa = \frac{1}{2\beta_0\log 2},\; j_0 = \frac{1}{2\beta_0 g_0^2\log 2}.
\end{equation}
\begin{theorem}[Continuum Gap Non-Collapse (CONDITIONAL on (H-cubic) and (H-match))]
By subtracting the complete second-order Lie-algebra jet and retaining the non-radial Weyl cubic invariant $p_3^2 = \frac{\sqrt{6}}{6}y(3x^2 - y^2)$ in the local interaction:
\begin{equation}
H_2 = \sqrt{6}\left(\frac{p_2^3}{11520} + \frac{p_3^2}{8640}\right),
\end{equation}
*assume* (H-cubic) that the multiscale step error is cubic in the running coupling:
\begin{equation}
\epsilon_j \le C g_j^3 = \frac{C \kappa^{3/2}}{(j + j_0)^{3/2}}.
\end{equation}
Because the $3/2$-power series converges:
\begin{equation}
\sum_{j=0}^\infty g_j^3 \le \kappa^{3/2}\left(j_0^{-3/2} + 2 j_0^{-1/2}\right) < \infty,
\end{equation}
the infinite product of degradation factors is strictly positive:
\begin{equation}
A_\infty = \prod_{j=0}^\infty (1 - \epsilon_j) \ge \exp\left(-\frac{\sum \epsilon_j}{1 - \epsilon_*}\right) > 0.
\end{equation}
Since the geometric sum of inverse floors converges:
\begin{equation}
\sum_{j=0}^\infty f_j^{-1} \le \frac{a_0}{c} \sum_{j=0}^\infty 2^{-j} = \frac{2 a_0}{c} < \infty,
\end{equation}
the block spectral gap in lattice units of the coarsest scale would be strictly positive:
\begin{equation}
\boxed{\Delta_{\mathrm{cont}} = \inf_{J \to \infty} \Delta_J \ge \frac{A_\infty}{\Delta_0^{-1} + \frac{2 a_0}{c}} > 0.}
\end{equation}
\end{theorem}

**Status and open inputs (Tier IV).** The Schur excess identity and frame sandwich (5.1) and the telescoped recurrence algebra are proved. The source states that the existing cubic estimate bounds only *a selected part of $V_1$*, not the full graph force, $A_g$'s connected remainder, or $C_g$ (H-cubic OPEN); that converting the estimate into a relative gap loss requires *comparison with the actual normalized coarse energy on the vacuum-orthogonal space and compatible vacuum matching* (H-match OPEN); and that W6 is *the exact unproved interacting Wilson estimate*. The result is a fixed-block Hamiltonian gap, not a statement about an infinite-volume continuum measure.

---

## 6. Tier V: Deterministic Reflection-Positive Block Pushforwards & The Chasm Bridge

### 6.1 The Failure of Markovian RG
\begin{proposition}[Exact Counterexample: Markov Kernels Destroy RP]
Let the fine space $X = \{*\}$ be a single reflection-positive point with trivial reflection. Define a reflection-equivariant Markov kernel $K$ to the two-spin space $X' = \{(s_-, s_+) : s_\pm \in \{-1, +1\}\}$ with time reflection $\theta'(s_-, s_+) = (s_+, s_-)$ by the symmetric law:
\begin{equation}
\nu = \frac{1}{2}\delta_{(+1, -1)} + \frac{1}{2}\delta_{(-1, +1)}.
\end{equation}
The kernel is reflection-equivariant ($K \circ \theta = \theta' \circ K$). For the positive-time observable $F(s_-, s_+) = s_+$:
\begin{equation}
\int_{X'} (\Theta' F) F d\nu = \mathbb{E}_\nu[s_- s_+] = (+1)(-1) = -1 < 0.
\end{equation}
Markovian coarse-graining violates reflection positivity because expectations are linear, not multiplicative: $K((\Theta' F) F) \ne (\Theta K F)(K F)$.
\end{proposition}

### 6.2 The Deterministic Pushforward Permanence Theorem
\begin{theorem}[Exact Preservation of Reflection Positivity]
Let $(X, \mu, \theta; \mathcal{A}_+)$ be a reflection-positive probability space:
\begin{equation}
\int_X (\Theta F) F d\mu \ge 0 \quad \text{for all } F \in \mathcal{A}_+.
\end{equation}
Let $P: X \to X'$ be a deterministic measurable blocking map to a coarse reflected space $(X', \theta'; \mathcal{A}'_+)$ satisfying:
\begin{enumerate}
    \item \textbf{Reflection Intertwining}: $P \circ \theta = \theta' \circ P$ (or modulo gauge $P(\theta U) = g_\theta(U) \cdot \theta' P(U)$).
    \item \textbf{Positive-Half Preservation}: $P^* \mathcal{A}'_+ \subset \mathcal{A}_+$.
\end{enumerate}
Then the coarse pushforward measure $\mu' = P_\# \mu$ is strictly reflection positive on $\mathcal{A}'_+$:
\begin{equation}
\boxed{\int_{X'} (\Theta' F') F' d(P_\# \mu) \ge 0 \quad \text{for all } F' \in \mathcal{A}'_+.}
\end{equation}
\end{theorem}
\begin{proof}
For any $F' \in \mathcal{A}'_+$, define $F = F' \circ P$. By hypothesis (2), $F \in \mathcal{A}_+$. By hypothesis (1):
$$
(\Theta' F')(P(U)) = \overline{F'(\theta' P(U))} = \overline{F'(P(\theta U))} = \overline{F(\theta U)} = (\Theta F)(U).
$$
By change of variables under the pushforward:
$$
\int_{X'} (\Theta' F') F' d(P_\# \mu) = \int_X (\Theta' F')(P(U)) F'(P(U)) d\mu(U) = \int_X (\Theta F)(U) F(U) d\mu(U) \ge 0.
$$
\end{proof}

### 6.3 Bridging the Bare Parameter Chasm
\begin{theorem}[The UV-to-Gapped Bridge (PROGRAM STATEMENT; no source proof)]
In the continuum limit $a \to 0$, the bare lattice action sits in the deep weak-coupling regime $g_0(a) \to 0$, or $u = 1/g_H^4 \to \infty$.
Iterating the reflection-adapted, centered Balaban blocking map:
\begin{equation}
P(U)_c = \exp\left[i \sum_{x \in B(c_-)} L^{-d} \frac{1}{i}\operatorname{Log}\left(U(\Gamma_{c, x}) U(c)^{-1}\right)\right] U(c),
\end{equation}
over $k$ dyadic scales drives the effective block link coupling according to the asymptotically free renormalization group flow:
\begin{equation}
\frac{1}{g_k^2} = \frac{1}{g_0^2} - 2\beta_0\, k\log L + O(\log g_k^2).
\end{equation}
At scale $k_* = \left\lceil \frac{1}{2\beta_0\log L}\left(\frac{1}{g_0^2}-\frac{1}{g_*^2}\right)\right\rceil$, the one-loop effective coupling would reach $g_{k_*}\ge g_*$ ($u_{k_*} \le u_*$). (The previous text wrote $g_k^2 = g_0^2 + 2\beta_0\log L^k$ with $k_*=\lceil 1/(2\beta_0 g_*^2)\rceil$; neither is the asymptotically free form, and the two did not match each other.)
Because each step is a deterministic pushforward satisfying $P \circ \theta = \theta' \circ P$ and $P^* \mathcal{A}'_+ \subset \mathcal{A}_+$, **reflection positivity is preserved identically across every step**.
Reflection positivity would then be transported along the chain. Positivity alone does not produce a gap: the blocked effective action must also be shown to lie in the strong-coupling regime with controlled large/small-field corrections, which is the content of the Balaban program and is not done here.
\end{theorem}

**Status and open inputs (Tier V).** Proposition 6.1 and Theorem 6.2 are proved (G19). G19 states that application to the full Balaban step, including the large/small-field split and any field-dependent gauge fixing not paired under reflection, is not covered. The Bridge theorem has no source; label OPEN. The one-loop law above is a hypothesis for the blocked coupling, not a derived flow.

---

## 7. Tier VI: Osterwalder–Schrader Reconstruction & Physical Minkowski Mass Gap

### 7.1 Reconstruction of the Physical Hilbert Space
Let $\mathcal{A}_{\mathrm{phys}}$ be the algebra of gauge-invariant cylindrical observables generated by Wilson loops supported in the positive Euclidean time half-space $\mathbb{R}^4_+ = \{x = (x_0, \mathbf{x}) : x_0 > 0\}$.
\begin{theorem}[Gauge Invariance and Reflection Positivity Inheritance]
For any gauge-invariant observable $F \in \mathcal{A}_{\mathrm{phys}}$, the expectation value in the gauge-fixed measure $\mu^{\mathrm{gf}}$ coincides with the expectation value in the unfixed, reflection-positive Wilson measure $\mu^W$:
\begin{equation}
\langle F \rangle_{\mathrm{fixed}} = \langle F \rangle_{\mathrm{unfixed}}.
\end{equation}
By the Seiler–Simon theorem, $\mu^W$ satisfies lattice reflection positivity. Taking $a \to 0$ along the deterministic pushforward trajectory:
\begin{equation}
\langle \Theta F, F \rangle = \int (\Theta F) \overline{F} d\mu_{\mathrm{cont}} = \lim_{a \to 0} \langle \Theta F, F \rangle_{\mu_a} \ge 0.
\end{equation}
\end{theorem}

Define the null subspace:
\begin{equation}
\mathcal{N} = \left\{F \in \mathcal{A}_{\mathrm{phys}} : \langle \Theta F, F \rangle = 0\right\}.
\end{equation}
The physical Hilbert space $\mathcal{H}_{\mathrm{phys}}$ is the completion of the quotient:
\begin{equation}
\boxed{\mathcal{H}_{\mathrm{phys}} = \overline{\mathcal{A}_{\mathrm{phys}} / \mathcal{N}}.}
\end{equation}

### 7.2 The Physical Hamiltonian and Transfer Semigroup
For Euclidean time displacement $t \ge 0$, define the translation operator on $\mathcal{A}_{\mathrm{phys}}$ by $(T_t F)(x_0, \mathbf{x}) = F(x_0 + t, \mathbf{x})$.
\begin{theorem}[Stone's Construction of the Physical Hamiltonian]
The operator $T_t$ descends to a symmetric contraction semigroup on $\mathcal{H}_{\mathrm{phys}}$:
\begin{equation}
\|T_t [F]\|_{\mathrm{phys}} \le \|[F]\|_{\mathrm{phys}}, \qquad T_{t_1 + t_2} = T_{t_1} T_{t_2}, \qquad T_0 = I.
\end{equation}
By Stone's theorem, there exists a unique non-negative self-adjoint operator $H_{\mathrm{phys}} \ge 0$ on $\mathcal{H}_{\mathrm{phys}}$ such that:
\begin{equation}
\boxed{T_t = e^{-t H_{\mathrm{phys}}}, \quad t \ge 0.}
\end{equation}
The vacuum state $\Omega = [\mathbf{1}] \in \mathcal{H}_{\mathrm{phys}}$ is the unique ground state of $H_{\mathrm{phys}}$ with eigenvalue zero: $H_{\mathrm{phys}} \Omega = 0$.
\end{theorem}

### 7.3 Proof of the Physical Mass Gap
\begin{theorem}[Strict Positive Physical Mass Gap]
Let $\mathcal{O}_1, \mathcal{O}_2 \in \mathcal{A}_{\mathrm{phys}}$ be gauge-invariant local operators with $\langle \mathcal{O}_i \rangle = 0$.
*Assuming* a continuum measure $\mu_{\mathrm{cont}}$ exists, that the fixed-block gap $\Delta_{\mathrm{cont}}$ of Tier IV controls infinite-volume correlation decay (no argument is given for either), and a Combes–Thomas localization bound (the cited `Synthesis_19` does not resolve to any file in the workspace):
\begin{equation}
|\langle \mathcal{O}_1(t, \mathbf{x}) \mathcal{O}_2(0, \mathbf{0}) \rangle_{\mathrm{cont}}| \le C \|\mathcal{O}_1\| \|\mathcal{O}_2\| e^{-m t}, \qquad t > 0,
\end{equation}
with $m \ge \Delta_{\mathrm{cont}} > 0$.
In the physical Hilbert space $\mathcal{H}_{\mathrm{phys}}$, this correlation decay translates via Osterwalder–Schrader reconstruction to:
\begin{equation}
\langle [\mathcal{O}_1], e^{-t H_{\mathrm{phys}}} [\mathcal{O}_2] \rangle_{\mathrm{phys}} = \langle \Theta \mathcal{O}_1, T_t \mathcal{O}_2 \rangle_{\mathrm{cont}} \le C \|[\mathcal{O}_1]\| \|[\mathcal{O}_2]\| e^{-m t}.
\end{equation}
By the spectral theorem for self-adjoint operators, the spectrum of $H_{\mathrm{phys}}$ on the orthogonal complement $\Omega^\perp$ satisfies:
\begin{equation}
\boxed{\operatorname{spec}(H_{\mathrm{phys}})\big|_{\Omega^\perp} \subset [m, \infty) \quad \text{with } m > 0.}
\end{equation}
\end{theorem}

**Status and open inputs (Tier VI).** The gauge-invariance/reflection-positivity inheritance is CONDITIONAL on Hypothesis H1 (LSI, Gribov-free gauge fixing) in the cited archive file. The Osterwalder–Schrader step additionally needs Euclidean invariance, regularity, and clustering of the continuum Schwinger functions; none is established, and the Schur source states that *constructing a nontrivial continuum correlation limit with the field-theory axioms remains necessary even after those spectral inequalities are available*. Labels: OS1 inheritance CONDITIONAL (H1); $\mu_{\mathrm{cont}}$ OPEN; Euclidean/Poincaré invariance OPEN; mass gap CONDITIONAL on all of the above.

---

## 8. Master Synthesis Ledger: Provenance and Rigor Status

Labels follow the repository convention: **PROVED** (complete derivation), **CONDITIONAL** (valid if named open inputs hold), **HYPOTHESIS** (assumed, no derivation), **OPEN** (no completed derivation). Statuses were re-read from the cited files on September 11, 2026.

| Mathematical Object | Formal Derivation / Exact Equation | Status | Primary File Anchor in Archive |
| :--- | :--- | :--- | :--- |
| **Haar Ricci Spark** | $\operatorname{Ric}_g = \frac{N}{2} g > 0$ (lattice units; no continuum gap) | **PROVED** | `ARCHIVE/collections/01_PROOFS/proven/P04_haar_mass_mechanism.md` |
| **Lattice LSI** | $\operatorname{Ric}_{\mu_\beta} \ge (\frac{N}{2} + \beta c_W) g$ near identity | **CONDITIONAL** (chart only) | `ARCHIVE/collections/01_PROOFS/proven/P02_bakry_emery_curvature.md` |
| **Shared-Link Hopping** | $t_N = \frac{2N(N^2-4)}{(N^2-1)(2N^2-1)(4N^2-9)} > 0$, $N\ge3$ | **PROVED** | `ALL THEORY/corpus/MASTER_THEORY_UNIFIED_2026-08-20_v4_3.md` |
| **Volume Cancellation** | $F_p P_p^{\mathrm{vac}} = 0 \implies \|\widetilde{D}_L'(0)\| \le 16 J(s + 2d)$ | **CONDITIONAL** (first-order chart; interacting volume-uniform dressed operator OPEN) | `WORKHOUSE-w98/paper/research_notes/G18_EXCITED_WINDOW_OPERATOR_BRIDGE_20260904.md` |
| **Linked Energy Form** | $g^{-2}\int(1-w)|f|^2 \le (1+e_g/\gamma)b_g[f]$ | **PROVED** (fixed block, small coupling) | `REPO/docs/derivations/w6-conditional-score-tail-control.md`, M.3 |
| **Phase Cancellation** | $\nabla_Z \Phi = 2\Phi + O(|\eta|^3) \implies K_g^{\mathrm{chart}} \le C_0$ | **CONDITIONAL** (chart; whole-fiber step unproved) | `REPO/docs/derivations/w6-conditional-score-tail-control.md`, Sec 3 |
| **Lemma Q / vMF Cap** | $\mathbb{E}[\prod_{p\in B} X_p \mid \mathcal{F}_{C^c}] \le (C_Q q_\eta)^{|B|}$ | **HYPOTHESIS** (assumed in source; SU(2) cap only) | `ALL THEORY/programs/pmbsf/NOTE_PMBSF_expanded_derivations_lemmaq_su3_2026_05_25.md` |
| **M10 Score Domination** | $K_g(w)\le C_0+C_1W_g(w)$ | **OPEN** | `REPO/docs/derivations/w6-conditional-score-tail-control.md`, tag (M10, OPEN) |
| **Schur Excess Identity** | $S_g(z) - S_0(z) = A_g - V_g^*(I + C_g)^{-1} V_g$ | **PROVED** | `REPO/docs/derivations/wilson-spatial-schur-excess.md`, SP3 |
| **Running law** $g_j^2=\kappa/(j+j_0)$ | one-loop form | **HYPOTHESIS** | `REPO/docs/derivations/wilson-spatial-schur-excess.md`, SP25 note |
| **Cubic step error** $\epsilon_j\le Cg_j^3$ | full graph force, $A_g$ remainder, $C_g$, vacuum matching | **OPEN** (W6) | `REPO/docs/derivations/wilson-spatial-schur-excess.md`, SP8/SP10; `wilson-selected-inverse-wall.md` |
| **$O(g_j^3)$ Gap Persistence** | $\sum g_j^3 < \infty \implies \inf_J \Delta_J \ge \frac{A_\infty}{\Delta_0^{-1} + \frac{2a_0}{c}} > 0$ | **CONDITIONAL** (recurrence algebra proved; inputs above open) | `REPO/docs/derivations/wilson-spatial-schur-excess.md`, SP20–SP25 |
| **Markov RP Failure** | $\int (\Theta' F) F d\nu = -1 < 0$ | **PROVED** | `WORKHOUSE-w98/paper/research_notes/G19_BALABAN_BLOCKING_REFLECTION_POSITIVITY_20260830.md` |
| **Pushforward RP** | $P \circ \theta = \theta' \circ P \implies \int (\Theta' F') F' d(P_\# \mu) \ge 0$ | **PROVED** | `WORKHOUSE-w98/paper/research_notes/G19_BALABAN_BLOCKING_REFLECTION_POSITIVITY_20260830.md` |
| **Balaban application / UV-to-Gapped Bridge** | blocked action lands in strong coupling with RP and controlled corrections | **OPEN** (no source) | G19, section "What this does and does not close" |
| **OS1 inheritance on $\mathcal A_{\mathrm{phys}}$** | fixed = unfixed expectations | **CONDITIONAL** (Hypothesis H1, Gribov-free) | `ARCHIVE/collections/01_PROOFS/cmi_review_package/04_MASS_GAP_THEOREM.md` |
| **Continuum measure $\mu_{\mathrm{cont}}$, Euclidean/Poincaré invariance, clustering** | none | **OPEN** | none |
| **OS Reconstruction / mass gap** | $\mathcal{H}_{\mathrm{phys}} = \overline{\mathcal{A}_{\mathrm{phys}}/\mathcal{N}}, \quad \operatorname{spec}(H_{\mathrm{phys}}) \ge m > 0$ | **CONDITIONAL** on every row above | `ARCHIVE/collections/01_PROOFS/cmi_review_package/04_MASS_GAP_THEOREM.md` |

---

### Concluding Statement
This document organizes the WORKHOUSE program into six tiers and records, with the repository's own labels, what each tier has and what it lacks. The proved pieces are: the Haar Ricci bound, the shared-link hopping coefficient, the telescoping holonomy inequality and centered form identity, the Schur excess identity with its frame sandwich and telescoped recurrence, and the deterministic-pushforward reflection-positivity lemma with its Markov counterexample.

The named open inputs, any one of which blocks the chain, are:
1. **M10** (conditional score domination), tagged OPEN in the repository.
2. **W6 and vacuum matching**: the cubic step error for the full graph force, $A_g$ remainder and $C_g$, and its conversion to a relative gap loss against the actual coarse energy.
3. **Interacting, volume-uniform dressed operator**: G18's bound is a first-order chart on a volume-shrinking interval.
4. **Balaban application step**: large/small-field control and reflection-paired gauge fixing so that blocking lands in strong coupling; the "bridge" has no source.
5. **Continuum limit with Euclidean invariance**: construction of $\mu_{\mathrm{cont}}$, rotation-invariance restoration, clustering, and the passage from a fixed-block Hamiltonian gap to infinite-volume correlation decay.

Corrections made in this revision: the Ricci constant is $N/2$ for the stated metric; the two running-coupling laws in Tiers IV and V are now the one-loop asymptotically free form and consistent with each other; the unresolved `Synthesis_19` citation is flagged; and the "proof complete" claim is withdrawn.
