---
id: EX-014
title: "RG coarse-graining, Schur-complement curvature propagation, the n-step gap cascade, and the Riccati / vHJ curvature-flow machinery"
kind: extraction
items: 12
status_breakdown: {"conditional": 3, "solid": 9}
program: yang_mills
extracted_by: claude-opus-5 subagent, 2026-09-01
stance: preservation (content extraction, not refereeing)
source_files:
  - RG_COARSE/01_Block_Convexity_Hinge/03_rg_intertwining_one_step_gap.md
  - lean/YangMills/RGGapCascade.lean
  - lean/Optimized_Lean/Continuum_Combined.lean
  - HESSIAN/Core_Hessian/09_rg_schur_complement_curvature.md
  - HESSIAN/03_misc_docs/RECOMMENDED_03_Block_Convexity_Engine_v2.md
  - HESSIAN/Core_Hessian/02_RG_Hessian_Schur_Stability.md
  - HESSIAN/Core_Hessian/04_block_convexity_rg_stability_mfip.md
  - RG_COARSE/00_Documentation_Indices/RECOMMENDED_01_Finite_Cutoff_Haar_Wilson_Windows_v2.md
  - RG_COARSE/01_Block_Convexity_Hinge/01_conditional_spectral_floor_monotonicity.md
  - HESSIAN/vHJ_Riccati/riccati_flow_hessian.tex
  - HESSIAN/vHJ_Riccati/gaussian_hessian_flow.tex
  - HESSIAN/vHJ_Riccati/02_vHJ_Hessian_Flow_and_Riccati.md
  - HESSIAN/vHJ_Riccati/02_vHJ_CurvatureFlow_Simulations_v2.md
  - HESSIAN/vHJ_Riccati/02_vhj_riccati_alpha_band.md
  - RICCATI/04_misc_docs/07_Horizontal_Tensor_Maximum_Principle.md
  - RICCATI/01_riccati_flow/SELECTED_02_Operator_Riccati_PBH_Flow.md
  - RICCATI/01_riccati_flow/DOC2_PBH_Flow_Riccati_Comparison_Gap_Persistence.md
  - RICCATI/01_riccati_flow/06_Riccati_Convexity_Attractor.md
  - RICCATI/01_riccati_flow/EXTRACT_04_Riccati_Mass_Gap_Mechanism_with_Simulation.md
  - RICCATI/01_riccati_flow/SIM_Riccati_ODE_Verification.md
---

# RG coarse-graining, Schur-complement curvature propagation, the n-step gap cascade, and the Riccati / vHJ curvature-flow machinery

> The corpus contains a complete and largely correct affine "gap cascade" machinery (one-step Poincaré recursion C_P^{(n)} ≤ L²C_RG·C_P^{(n+1)} + C_block, closed form r^n C_0 + C_block(1−r^n)/(1−r), fixed point C_block/(1−r)), a correct Schur-complement/Brascamp–Lieb theory of how curvature degrades under block marginalization (∇²S_eff = E[A] − Cov(∇_xS) ⪯ E[A], with quantitative loss M²/γ), a fully correct Hamilton-type horizontal tensor maximum principle reducing the vHJ/PBH Hessian flow to the scalar Riccati inequality λ̇ ≥ −αλ² + σ − ε, and — most valuably — a set of sharp obstructions showing why this machinery cannot reach the continuum (pure heat-flow coarse-graining has the exact solution H_t^{-1} = H_0^{-1} + 2νt so convexity decays like 1/(2t) with no source; the Haar spark scales as a²g²→0; decimation gives C_RG = 1 hence r = L² > 1; and gauge-covariant Markov coarse-graining kernels are algebraically impossible).

**12 extracted items** — 3 conditional, 9 solid

---

## 1. One-step RG Poincaré recursion via total variance and gradient intertwining

`status: conditional` · `kind: theorem`

### Statement

Setting. Let $\Lambda_n\subset\mathbb Z^4$ be a finite lattice of spacing $a_n$, $\Lambda_{n+1}$ the $L$-blocked lattice with $a_{n+1}=La_n$ ($L\ge 2$, typically $L=2$). Let $M_n=G^{E(\Lambda_n)}$ with $G$ a compact Lie group (the documents take $G=\mathrm{SU}(2)$), $\mu_n$ a Gibbs measure on $M_n$, and $\pi_n:M_n\to M_{n+1}$ a measurable block-spin map with $\mu_{n+1}=(\pi_n)_\#\mu_n$. Write $P f(V):=\mathbb E_{\mu_n}[f(U)\mid \pi_n(U)=V]$ for the conditional expectation, $\mathcal E_n(f):=\int_{M_n}|\nabla f|^2 d\mu_n$ for the fine Dirichlet form and $\nabla'$ for the coarse gradient. Define $C_P^{(n)}$ as the least constant with $\operatorname{Var}_{\mu_n}(f)\le C_P^{(n)}\mathcal E_n(f)$ for all $f\in L^2(\mu_n)$ in the form domain.

Hypotheses (all quantifiers explicit):
(A1) [Coarse Poincaré / induction anchor] There is $C_P^{(n+1)}<\infty$ such that for all $g$ in the coarse form domain, $\operatorname{Var}_{\mu_{n+1}}(g)\le C_P^{(n+1)}\int|\nabla' g|^2 d\mu_{n+1}$.
(A2) [Block/fibre gap] There is $C_{\mathrm{block}}<\infty$, independent of the volume and of $n$, such that for $\mu_{n+1}$-a.e. $V$ and all $f$, $\operatorname{Var}_{\mu_n(\cdot\mid V)}(f)\le C_{\mathrm{block}}\int|\nabla f|^2\,d\mu_n(\cdot\mid V)$.
(A3) [Gradient intertwining] There is a dimensionless constant $C_{\mathrm{RG}}$ such that for all $f$ and $\mu_{n+1}$-a.e. $V$, $|\nabla'(Pf)(V)|^2\le C_{\mathrm{RG}}\,\mathbb E_{\mu_n}\!\left[|\nabla f|^2\mid V\right]$.

Conclusion.
$$\boxed{\;C_P^{(n)}\;\le\;L^2\,C_{\mathrm{RG}}\,C_P^{(n+1)}\;+\;C_{\mathrm{block}}\;}$$
With $L=2$ the prefactor $L^2=4$ is the scale-conversion factor from expressing coarse Dirichlet energy in fine physical units.

Evaluation of $C_{\mathrm{RG}}$ for the two canonical block maps:
(i) Decimation ($\pi$ selects representative links): $C_{\mathrm{RG}}=1$ exactly, with no small-field restriction.
(ii) Geodesic (Karcher) averaging over a block of $N=L^d$ fine links, in the small-field regime $U_b=\exp(X_b)$, $\|X_b\|\le r\ll 1$: $C_{\mathrm{RG}}\le (1+O(r))/N$. For $L=2$, $d=4$: $N=16$, $C_{\mathrm{RG}}\le (1+O(r))/16$.

### Derivation

STEP 1 (law of total variance). For $f\in L^2(\mu_n)$ and $Pf(V)=\mathbb E[f\mid\pi_n(U)=V]$,
$$\operatorname{Var}_{\mu_n}(f)=\operatorname{Var}_{\mu_{n+1}}(Pf)+\mathbb E_{\mu_{n+1}}\!\left[\operatorname{Var}_{\mu_n(\cdot\mid V)}(f)\right].$$
This is the exact algebraic spine of every one-step RG gap estimate; it is an identity, not an inequality.

STEP 2 (fibre term). Apply (A2) fibrewise and integrate over $V$ with respect to $\mu_{n+1}$; the tower property $\mathbb E_{\mu_{n+1}}\mathbb E_{\mu_n(\cdot|V)}=\mathbb E_{\mu_n}$ gives
$$\mathbb E_{\mu_{n+1}}\!\left[\operatorname{Var}_{\mu_n(\cdot\mid V)}(f)\right]\;\le\;C_{\mathrm{block}}\int_{M_n}|\nabla f|^2 d\mu_n \;=\;C_{\mathrm{block}}\,\mathcal E_n(f).$$

STEP 3 (coarse term). By (A1) applied to $g=Pf$,
$$\operatorname{Var}_{\mu_{n+1}}(Pf)\le C_P^{(n+1)}\int|\nabla'(Pf)|^2 d\mu_{n+1}.$$
By (A3) and the tower property again,
$$\int|\nabla'(Pf)|^2 d\mu_{n+1}\le C_{\mathrm{RG}}\int \mathbb E_{\mu_n}[|\nabla f|^2\mid V]\,d\mu_{n+1}(V)=C_{\mathrm{RG}}\,\mathcal E_n(f).$$

STEP 4 (scale conversion — where $L^2$ comes from). Physical Dirichlet forms carry the lattice spacing: $\mathcal E_m^{\mathrm{phys}}(f):=a_m^{-2}\mathcal E_m(f)$. Since $a_{n+1}=La_n$,
$$\mathcal E_{n+1}^{\mathrm{phys}}=a_{n+1}^{-2}\mathcal E_{n+1}=L^{-2}a_n^{-2}\mathcal E_{n+1},$$
so when the coarse Poincaré constant $C_P^{(n+1)}$ (defined against $\mathcal E_{n+1}^{\mathrm{phys}}$) is re-expressed against fine-scale energy, it acquires a factor $L^2$. Combining Steps 2–4 and taking the best constant gives
$$\operatorname{Var}_{\mu_n}(f)\le \left(L^2 C_{\mathrm{RG}}C_P^{(n+1)}+C_{\mathrm{block}}\right)\mathcal E_n(f),$$
i.e. the boxed recursion. $\square$

STEP 5 (computation of $C_{\mathrm{RG}}$, decimation). If $\pi$ selects a subset of coordinates then $Pf$ depends only on those coordinates and $\nabla'(Pf)$ is a coordinate projection of $\nabla(Pf)$; by Jensen $|\nabla' Pf|^2 = |\mathbb E[\nabla_{\text{selected}}f\mid V]|^2 \le \mathbb E[|\nabla f|^2\mid V]$, so $C_{\mathrm{RG}}=1$ and it is attained. This is the sharp value; there is no gain.

STEP 6 (computation of $C_{\mathrm{RG}}$, geodesic averaging). Let a block contain $N=L^d$ fine links near the identity, $U_b=\exp(X_b)$ with $X_b\in\mathfrak g\cong\mathbb R^{\dim\mathfrak g}$ and $\|X_b\|\le r\ll1$. The Karcher (Riemannian barycentre) mean linearises to the arithmetic mean:
$$Y:=\pi(\{X_b\})=\frac1N\sum_{b=1}^N X_b+O(r^2).$$
Hence for any smooth $F$ of the coarse variable, $\partial_{X_b}(F\circ\pi)=\frac1N\partial_YF+O(r)$, so
$$\sum_{b=1}^N\bigl|\nabla_{X_b}(F\circ\pi)\bigr|^2=N\cdot\frac{1}{N^2}|\nabla_YF|^2\,(1+O(r))=\frac{1+O(r)}{N}\,|\nabla_YF|^2 .$$
Therefore $C_{\mathrm{RG}}\le (1+O(r))/N$. For $L=2$, $d=4$: $N=16$, $C_{\mathrm{RG}}\le (1+O(r))/16\approx 0.0625$.

STEP 7 (contraction condition). Setting $r_{\mathrm{contr}}:=L^2C_{\mathrm{RG}}$, the recursion contracts iff $r_{\mathrm{contr}}<1$, i.e. $C_{\mathrm{RG}}<L^{-2}$. For decimation, $r_{\mathrm{contr}}=L^2=4>1$ (no contraction; $C_P^{(0)}$ then scales like $4^{N_{\text{steps}}}$, matching the canonical $a^{-2}$ scaling of a Poincaré constant). For geodesic averaging in the small-field region, $r_{\mathrm{contr}}=4/16=1/4<1$ (contraction).

[Reconstructed remark, mine] The reason contraction is possible at all is structural: block marginalisation alone can only *lose* curvature (see the monotone-degradation item), and the *only* source of gain in this recursion is the geometric factor $L^{-2}$ hidden in $C_{\mathrm{RG}}\le 1/N=L^{-d}$. Contraction therefore requires the block map to contract gradients strictly faster than the naive scale factor, $C_{\mathrm{RG}}<L^{-2}$, which in $d=4$ with averaging means $L^{-4}<L^{-2}$ — satisfied, but only in the linearised (weak-field) chart.

### Constants and numbers

Blocking factor $L=2$; spatial dimension $d=4$; block size $N=L^d=16$ fine links.
Scale-conversion factor $L^2=4$.
Decimation: $C_{\mathrm{RG}}=1$ exactly ⇒ $r=L^2C_{\mathrm{RG}}=4$ (no contraction).
Geodesic/Karcher averaging, small-field ($\|X_b\|\le r\ll1$, e.g. $\sigma=0.05$ in the JAX harness): $C_{\mathrm{RG}}\le(1+O(r))/16=0.0625(1+O(r))$ ⇒ $r=L^2C_{\mathrm{RG}}=4/16=0.25$.
Empirical target for the JAX test harness: mean ratio $R\approx 1/N=0.0625$; warning threshold $\max R>0.1$ at small $\sigma$ indicates the Karcher iteration has left the normal neighbourhood.
Harness parameters actually used: batch 1024–4096, $N=16$ links/block, $\sigma\in[0.02,0.08]$, 20–25 Karcher fixed-point iterations, SU(2) as unit quaternions, principal-branch log.

### Code

Empirical test of hypothesis (A3) — the gradient-intertwining constant — for SU(2) geodesic (Karcher) averaging. Full source: RG_COARSE/05_Simulations_Numerics/05_jax_a3_rg_intertwining_test.md (also HESSIAN and RICCATI copies). Key functions and how to run:

  su2_exp(x), su2_log(q)                 # principal-branch exp/log, SU(2) as unit quaternions
  karcher_mean_quat(qs, num_iters=20)    # q_{t+1} = q_t * exp( mean_i log(q_t^{-1} q_i) )
  block_map_pi(x_block)                  # pi: (N,3) Lie-algebra coords -> coarse quaternion
  F_v_of_V(V, v) = <v, log(V)>           # linear test functions; |grad F_v|^2 = |v|^2
  R_ratio(x_block, v) = |grad(F_v o pi)|^2 / |v|^2      # this is exactly the (A3) ratio
  run_experiment(seed=0, batch_size=4096, N=16, sigma=0.05, num_iters=25)

Run: paste into one Colab/JAX cell and call run_experiment(...); it returns {mean_R, std_R, max_R, min_R}. Expected in the linearised regime: mean_R ≈ 1/N = 0.0625. Increasing sigma stress-tests whether (A3) holds beyond the small-field chart; blow-up of max_R is the diagnostic that (A3) is small-field only unless pi is replaced by decimation (for which C_RG = 1 exactly).

**Caveat.** (A2) and (A3) are hypotheses, not theorems, in the corpus. (A3) with $C_{\mathrm{RG}}\approx 1/16$ is proved only in the linearised small-field chart; the only unconditional value is the decimation value $C_{\mathrm{RG}}=1$, which does not contract.

**Why it matters.** This is the single load-bearing inequality of the whole RG programme: it isolates all the analytic difficulty into three local, numerically testable hypotheses, and it is the inequality whose iteration produces the n-step cascade and its IR fixed point.

---

## 2. n-step gap cascade: closed form, contraction, IR fixed point (with Lean formalisation)

`status: solid` · `kind: theorem`

### Statement

Let $L\in\mathbb N$, $L\ge2$, and let $C_{\mathrm{RG}}>0$, $C_{\mathrm{block}}>0$ be reals. Define the contraction factor $r:=L^2C_{\mathrm{RG}}$ and the one-step map $T(C):=rC+C_{\mathrm{block}}$. Define the $n$-step cascade by $\mathcal C_0:=C_{P,0}$ and $\mathcal C_{n+1}:=T(\mathcal C_n)$.

(i) [Closed form] For every $n\in\mathbb N$ and every $C_{P,0}\in\mathbb R$, if $0<r<1$ then
$$\boxed{\;\mathcal C_n \;\le\; r^n\,C_{P,0}\;+\;C_{\mathrm{block}}\,\frac{1-r^n}{1-r}\;}$$
with equality (the map is affine, so the inequality is saturated; the $\le$ form is what survives when each step is only an inequality, as in the RG recursion).

(ii) [Fixed point] If $r<1$ then $T$ has the unique fixed point $C_P^{*}=\dfrac{C_{\mathrm{block}}}{1-r}>0$, and $\mathcal C_n\to C_P^{*}$ geometrically with ratio $r$: $|\mathcal C_n-C_P^{*}|=r^n|C_{P,0}-C_P^{*}|$.

(iii) [Contraction criteria] $r<1\iff C_{\mathrm{RG}}<L^{-2}$. For $L=2$: $r<1\iff C_{\mathrm{RG}}<1/4$; and $C_{\mathrm{RG}}\le1/16$ (geodesic averaging) $\Rightarrow r\le1/4$.

(iv) [Standard parameters] With $L=2$, $C_{\mathrm{RG}}=1/16$, so $r=1/4$: $C_P^{*}=\tfrac43 C_{\mathrm{block}}$, IR spectral gap $\Delta:=1/C_P^{*}=\dfrac{3}{4C_{\mathrm{block}}}$, and (with the corpus's convention $m=\sqrt{2\Delta}$) $m=\sqrt{3/(2C_{\mathrm{block}})}$.

The correct reading in the RG application: the derived one-step inequality runs *fine ≤ coarse*, $C_P^{(k)}\le rC_P^{(k+1)}+C_{\mathrm{block}}$. Iterating $n$ times from a scale-$n$ anchor gives
$$C_P^{(0)}\;\le\;r^{\,n}C_P^{(n)}+C_{\mathrm{block}}\frac{1-r^{\,n}}{1-r}\;\xrightarrow[n\to\infty]{}\;\frac{C_{\mathrm{block}}}{1-r},$$
which is a bound on the *finest* Poincaré constant, uniform in the number of RG steps — exactly what a continuum limit needs.

### Derivation

PROOF OF (i), by induction on $n$.
Base $n=0$: RHS $=r^0C_{P,0}+C_{\mathrm{block}}\frac{1-1}{1-r}=C_{P,0}=\mathcal C_0$. ✓
Inductive step: assume $\mathcal C_n\le r^nC_{P,0}+C_{\mathrm{block}}\frac{1-r^n}{1-r}$. Since $r>0$,
$$\mathcal C_{n+1}=r\mathcal C_n+C_{\mathrm{block}}\;\le\;r\!\left(r^nC_{P,0}+C_{\mathrm{block}}\frac{1-r^n}{1-r}\right)+C_{\mathrm{block}}\;=\;r^{n+1}C_{P,0}+C_{\mathrm{block}}\frac{r(1-r^n)}{1-r}+C_{\mathrm{block}}.$$
Now use the algebraic identity $r(1-r^n)+(1-r)=1-r^{n+1}$, so
$$C_{\mathrm{block}}\frac{r(1-r^n)}{1-r}+C_{\mathrm{block}}=C_{\mathrm{block}}\frac{r(1-r^n)+(1-r)}{1-r}=C_{\mathrm{block}}\frac{1-r^{n+1}}{1-r},$$
using $1-r>0$. This is exactly the claim at $n+1$. $\square$

PROOF OF (ii). $T(C)=C\iff C(1-r)=C_{\mathrm{block}}\iff C=C_{\mathrm{block}}/(1-r)$; positivity follows from $C_{\mathrm{block}}>0$ and $1-r>0$. Subtracting the fixed-point equation from the recursion gives $\mathcal C_{n+1}-C_P^*=r(\mathcal C_n-C_P^*)$, hence $\mathcal C_n-C_P^*=r^n(C_{P,0}-C_P^*)$ and geometric convergence. $\square$

PROOF OF (iii)–(iv). Immediate: $r=L^2C_{\mathrm{RG}}$; $L=2,C_{\mathrm{RG}}=1/16\Rightarrow r=4/16=1/4$; $C_P^*=C_{\mathrm{block}}/(3/4)=\tfrac43C_{\mathrm{block}}$; $\Delta=1/C_P^*=3/(4C_{\mathrm{block}})$.

NUMERICAL VERIFICATION [mine]. With $r=1/4$, $C_{\mathrm{block}}=1$, $C_{P,0}=10$, direct iteration versus closed form agree to machine precision at $n=0,1,2,5,10,20$ (difference exactly $0$ in float64); the iterates are $10,\;3.5,\;1.875,\;1.341796875,\;1.3333415985,\;1.3333333333$, converging to $4/3$.

COEFFICIENT TABLE for $r=1/4$ ($C_P^{(0)}\le \rho_n C_P^{(n)}+\kappa_n C_{\mathrm{block}}$):
$n$: 0,1,2,3,4,5,6,7
$\rho_n=r^n$: 1, 0.25, 0.0625, 0.015625, 0.00390625, 0.0009765625, 0.000244140625, 0.00006103515625
$\kappa_n=(1-r^n)/(1-r)$: 0, 1, 1.25, 1.3125, 1.328125, 1.33203125, 1.333007812, 1.333251953 → $4/3$.

FAILURE MODE for decimation ($C_{\mathrm{RG}}=1$, $r=4$): the same algebra gives $C_P^{(0)}\le 4^nC_P^{(n)}+C_{\mathrm{block}}(4^n-1)/3$, which diverges; there is no fixed point and no uniform bound. This is the honest statement of what the cascade *cannot* do with the only unconditionally available block map.

LEAN FORMALISATION. The statement is formalised twice, with 0 `sorry`s in both files:
  lean/YangMills/RGGapCascade.lean  (namespace YangMills.RGGapCascade)
  lean/Optimized_Lean/Continuum_Combined.lean  (namespace YangMills.RGGapCascade, PART 2)
The definitions are
  structure RGParams : L : ℕ, C_RG C_block : ℝ, hL : L ≥ 2, hRG_pos, hBlock_pos
  contraction_factor p := (p.L:ℝ)^2 * p.C_RG
  one_step p C := contraction_factor p * C + p.C_block
  n_step_cascade p C 0 = C ; n_step_cascade p C (n+1) = one_step p (n_step_cascade p C n)
  contracts p := contraction_factor p < 1
and the theorems are `cascade_closed_form` (exactly (i), proved by the induction above, with `nlinarith` discharging the two arithmetic steps), `fixed_point`/`fixed_point_pos`, `contraction_L2`, `geodesic_contraction`, `standard_params`/`standard_contracts`/`standard_fixed_point` (= $(4/3)C_{\mathrm{block}}$), `standard_IR_gap` (= $3/(4C_{\mathrm{block}})$), `IR_gap_pos`, `cascade_mass_pos`.
This is one of the few places in the Lean corpus that formalises a genuine (if elementary) mathematical statement rather than arithmetic over named reals.

### Constants and numbers

$r=L^2C_{\mathrm{RG}}$. Standard parameters $L=2$, $C_{\mathrm{RG}}=1/16$ ⇒ $r=1/4$.
IR Poincaré constant $C_P^{*}=C_{\mathrm{block}}/(1-r)=\tfrac43C_{\mathrm{block}}\approx1.3333\,C_{\mathrm{block}}$.
IR spectral gap $\Delta=1/C_P^{*}=3/(4C_{\mathrm{block}})=0.75/C_{\mathrm{block}}$.
Physical mass (corpus convention $m=\sqrt{2\Delta}$): $m=\sqrt{3/(2C_{\mathrm{block}})}$.
Contraction thresholds: $L=2$ needs $C_{\mathrm{RG}}<1/4$; $C_{\mathrm{RG}}\le1/16\Rightarrow r\le1/4$.
Decimation $C_{\mathrm{RG}}=1$ ⇒ $r=4$, cascade coefficient $4^n$, divergent.
Block-gap bound quoted elsewhere in the corpus: $C_{\mathrm{block}}\le 1/c_H$ with $c_H$ the Haar mass curvature ($c_H\approx1/6$ per link for the normalisation used there, so $C_{\mathrm{block}}\lesssim6$), giving $\Delta\gtrsim0.125$ in those units.

### Code

Verification script (float64, numpy) reproducing the closed form and the coefficient table:

    import numpy as np
    def cascade(r, Cb, C0, n):
        x = C0
        for _ in range(n): x = r*x + Cb
        return x
    r, Cb, C0 = 0.25, 1.0, 10.0
    for n in [0,1,2,5,10,20]:
        closed = r**n*C0 + Cb*(1-r**n)/(1-r)
        assert abs(cascade(r,Cb,C0,n) - closed) < 1e-15
    print('fixed point', Cb/(1-r), 'gap', (1-r)/Cb)   # 1.3333333333333333 0.75

Lean sources (0 sorries, definitions + theorems named above):
  lean/YangMills/RGGapCascade.lean : theorem cascade_closed_form, fixed_point, standard_fixed_point, standard_IR_gap
  lean/Optimized_Lean/Continuum_Combined.lean : same, PART 2

**Caveat.** The algebra is unconditional; every physical claim rests entirely on the *inputs* $C_{\mathrm{RG}}<L^{-2}$ and $C_{\mathrm{block}}<\infty$ uniform in $n$ and volume, neither of which is established. The Lean `cascade_limit` theorem is vacuous as stated (its bound $\varepsilon+|C_{P,0}|$ does not force convergence); use (ii) above instead, which is a one-line exact statement.

**Why it matters.** This converts 'does the gap survive infinitely many RG steps?' into a finite algebraic check on two constants — the cleanest reduction in the entire corpus — and simultaneously exhibits, via $C_{\mathrm{RG}}=1$ for decimation, precisely why the check fails for the only unconditionally available block map.

---

## 3. Curvature under block marginalisation: exact Hessian identity, Brascamp–Lieb Schur bound, and the no-loss theorem

`status: solid` · `kind: theorem`

### Statement

Let $V\in C^2(\mathbb R^n_x\times\mathbb R^m_y)$ with $e^{-V(x,\cdot)}\in L^1(\mathbb R^m)$ for every $x$, and define the effective (coarse) action and the conditional (fibre) measure
$$V_{\mathrm{eff}}(x):=-\log\!\int_{\mathbb R^m}e^{-V(x,y)}dy,\qquad \nu_x(dy):=\frac{e^{-V(x,y)}}{\int e^{-V(x,\cdot)}}dy,$$
and write the block Hessian $\nabla^2V=\begin{pmatrix}A&B\\B^\top&C\end{pmatrix}$ with $A=\nabla^2_{xx}V$ ($n\times n$), $C=\nabla^2_{yy}V$ ($m\times m$), $B=\nabla^2_{xy}V$ ($n\times m$).

(1) [Exact identity] $\nabla V_{\mathrm{eff}}(x)=\mathbb E_{\nu_x}[\nabla_xV]$ and
$$\boxed{\;\nabla^2V_{\mathrm{eff}}(x)=\mathbb E_{\nu_x}\!\left[\nabla^2_{xx}V\right]-\operatorname{Cov}_{\nu_x}\!\left(\nabla_xV\right)\;}$$
where $\operatorname{Cov}_{\nu_x}(g)=\mathbb E[gg^\top]-\mathbb E[g]\mathbb E[g]^\top\succeq0$.

(2) [Brascamp–Lieb Schur bound] If $C(x,y)\succ0$ for all $(x,y)$ then
$$\operatorname{Cov}_{\nu_x}(\nabla_xV)\preceq\mathbb E_{\nu_x}\!\left[BC^{-1}B^\top\right]\quad\Longrightarrow\quad \nabla^2V_{\mathrm{eff}}(x)\succeq\mathbb E_{\nu_x}\!\left[\underbrace{A-BC^{-1}B^\top}_{\text{Schur complement of }\nabla^2V}\right].$$

(3) [Quantitative block-convexity engine] If uniformly in $(x,y)$: $A\succeq\alpha I_n$, $C\succeq\gamma I_m$ with $\gamma>0$, and $\|B\|_{\mathrm{op}}\le M$, then
$$\boxed{\;\nabla^2_xV_{\mathrm{eff}}(x)\succeq\Bigl(\alpha-\frac{M^2}{\gamma}\Bigr)I_n\;}$$
In particular if $M^2<\alpha\gamma$ the coarse action is uniformly convex with modulus $\rho_{\mathrm{new}}=\alpha-M^2/\gamma>0$. With the symmetric choice $\alpha=\gamma=\rho$: $\rho_{\mathrm{new}}\ge\rho-M^2/\rho=(\rho^2-M^2)/\rho$, so convexity survives one block step iff $\rho>M$.

(4) [No-loss / Prékopa-type theorem, $\alpha=1$] If the *joint* Hessian satisfies $\nabla^2_{(x,y)}V(x,y)\succeq\kappa I_{n+m}$ for all $(x,y)$, then $\nabla^2V_{\mathrm{eff}}(x)\succeq\kappa I_n$ for all $x$. Marginalisation does **not** reduce the convexity parameter when the joint potential is uniformly strongly convex.

### Derivation

PROOF OF (1). Write $Z(x)=\int e^{-V(x,y)}dy$, $V_{\mathrm{eff}}=-\log Z$. Differentiating under the integral,
$$\partial_iV_{\mathrm{eff}}=-\frac{\partial_iZ}{Z}=\frac{1}{Z}\int\partial_iV\,e^{-V}dy=\mathbb E_{\nu_x}[\partial_iV].$$
Differentiate once more. Since $\partial_j\!\left(\frac{e^{-V}}{Z}\right)=\frac{e^{-V}}{Z}\bigl(-\partial_jV+\mathbb E_{\nu_x}[\partial_jV]\bigr)$,
$$\partial_j\partial_iV_{\mathrm{eff}}=\mathbb E_{\nu_x}[\partial_j\partial_iV]+\int\partial_iV\,\partial_j\!\left(\tfrac{e^{-V}}{Z}\right)dy=\mathbb E[\partial_i\partial_jV]-\mathbb E[\partial_iV\,\partial_jV]+\mathbb E[\partial_iV]\mathbb E[\partial_jV],$$
which is exactly $\mathbb E[A]_{ij}-\operatorname{Cov}(\nabla_xV)_{ij}$. $\square$

PROOF OF (2). Brascamp–Lieb: if $d\nu\propto e^{-W(y)}dy$ with $\nabla^2W\succ0$ then for every $f\in C^1$, $\operatorname{Var}_\nu(f)\le\mathbb E_\nu\bigl[\nabla f^\top(\nabla^2W)^{-1}\nabla f\bigr]$. Fix $x$ and a unit vector $v\in\mathbb R^n$; take $W(y)=V(x,y)$ (so $\nabla^2W=C$) and $f(y)=v^\top\nabla_xV(x,y)$, whence $\nabla_yf=B^\top v$. Then
$$v^\top\operatorname{Cov}_{\nu_x}(\nabla_xV)v=\operatorname{Var}_{\nu_x}(f)\le\mathbb E_{\nu_x}\bigl[v^\top BC^{-1}B^\top v\bigr].$$
Since $v$ is arbitrary, $\operatorname{Cov}\preceq\mathbb E[BC^{-1}B^\top]$; insert into (1). $\square$

ALTERNATIVE PROOF OF (3) via Poincaré only (this is the version in 02_RG_Hessian_Schur_Stability.md, and avoids Brascamp–Lieb). If $C\succeq\gamma I$ then $\nu_x$ satisfies a Poincaré inequality $\operatorname{Var}_{\nu_x}(f)\le\gamma^{-1}\mathbb E_{\nu_x}\|\nabla_yf\|^2$ (Bakry–Émery). With $f_v(y)=v\cdot\nabla_xV(x,y)$ and $\nabla_yf_v=B^\top v$, $\|B^\top v\|\le M\|v\|=M$, so $\operatorname{Var}_{\nu_x}(f_v)\le M^2/\gamma$ for every unit $v$, i.e. $\operatorname{Cov}_{\nu_x}(\nabla_xV)\preceq(M^2/\gamma)I$. Combining with $\mathbb E[A]\succeq\alpha I$ and identity (1),
$$v^\top\nabla^2V_{\mathrm{eff}}v\ge\alpha-\frac{M^2}{\gamma}\qquad\forall\|v\|=1.\;\square$$

PROOF OF (4). Purely linear-algebraic. Let $H=\begin{pmatrix}A&B\\B^\top&C\end{pmatrix}\succeq\kappa I_{n+m}$; then $C\succeq\kappa I_m\succ0$ is invertible. Fix $u\in\mathbb R^n$ and choose the Schur-optimal $v:=-C^{-1}B^\top u$. Then
$$\begin{pmatrix}u\\v\end{pmatrix}^{\!\top}\!H\begin{pmatrix}u\\v\end{pmatrix}=u^\top Au+2u^\top Bv+v^\top Cv=u^\top Au-2u^\top BC^{-1}B^\top u+u^\top BC^{-1}CC^{-1}B^\top u=u^\top\!\left(A-BC^{-1}B^\top\right)\!u.$$
By hypothesis this is $\ge\kappa(\|u\|^2+\|v\|^2)\ge\kappa\|u\|^2$. Hence the Schur complement obeys $A-BC^{-1}B^\top\succeq\kappa I_n$ pointwise; taking $\mathbb E_{\nu_x}$ preserves the inequality, and (2) shows $\nabla^2V_{\mathrm{eff}}$ dominates that expectation. $\square$

SHARPNESS CHECK [mine]. (4) is sharp: for the Gaussian $V=\tfrac12(x,y)^\top H(x,y)$ the marginal is exactly Gaussian with Hessian the Schur complement $A-BC^{-1}B^\top$, and for $H=\kappa I$ the Schur complement is $\kappa I_n$. So no improvement over $\kappa$ is possible in general, and (3) is exactly the perturbative degradation when one only controls $A,C,B$ separately: $\alpha-M^2/\gamma$ is attained for $A=\alpha I$, $C=\gamma I$, $B$ with $\|B\|=M$ and $BB^\top=M^2 P$ for a rank-one projector $P$.

WHY $\alpha<1$ IN THE LATTICE APPLICATION (the honest list from 09_rg_schur_complement_curvature.md): (a) only a *local* convexity certificate (a SAFE region) is available, not a global one; (b) gauge/harmonic directions produce zero modes unless one quotients correctly; (c) a real RG map is not pure marginalisation — it includes a nonlinear block map with a Jacobian term; (d) one may be forced to integrate out directions where convexity is weak or only available after projection. The pragmatic statement that survives is: on the SAFE region, with block-map distortion $\le L$ and second derivative $\le M_2$, $\kappa'\ge\kappa_*-\varepsilon(L,M_2,\operatorname{Var}_{\nu_x})$, i.e. $\alpha=1-\varepsilon/\kappa_*$.

### Constants and numbers

Degradation per block step: $\Delta\rho=M^2/\gamma$; with $\alpha=\gamma=\rho$, $\rho_{\mathrm{new}}\ge(\rho^2-M^2)/\rho$.
One-step survival criterion: $M^2<\alpha\gamma$; symmetric form $\rho>M$.
No-loss regime: joint $\nabla^2V\succeq\kappa I$ ⇒ marginal $\succeq\kappa I$, i.e. $\alpha_{\text{loss}}=1$ exactly.
The corpus's 'placeholder' value $\alpha=0.976$ appearing in earlier drafts has no derivation behind it; the theorem above gives $\alpha=1$ under joint strong convexity and $1-M^2/(\alpha\gamma)$ otherwise.

**Caveat.** All four statements are Euclidean ($\mathbb R^n\times\mathbb R^m$). Transfer to $G^{E(\Lambda)}$ requires a chart, a gauge-fixed horizontal projection $\Pi_{\mathrm{phys}}(U)$ that is generically $U$-dependent, and control of the exponential-map Jacobian — none of which is supplied.

**Why it matters.** This is the correct, fully proved replacement for the hand-waved '$\kappa'\ge\alpha\kappa_*$' assumption that appears throughout the corpus, and it cleanly separates the easy convex analysis (Schur complements) from the hard physics (return-to-SAFE plus the gauge quotient).

---

## 4. Monotone degradation of convexity under block marginalisation (obstruction)

`status: solid` · `kind: obstruction`

### Statement

With the notation of the previous item ($V\in C^2$, $V_{\mathrm{eff}}(x)=-\log\int e^{-V(x,y)}dy$, $\nu_x$ the fibre measure, $A=\nabla^2_{xx}V$):

(a) For every $x$,
$$\boxed{\;\nabla^2V_{\mathrm{eff}}(x)\;\preceq\;\mathbb E_{\nu_x}\!\left[\nabla^2_{xx}V(x,\cdot)\right]\;}$$
with equality at $x$ if and only if $\nabla_xV(x,\cdot)$ is $\nu_x$-a.s. constant on the fibre. Consequently
$$\lambda_{\min}\bigl(\nabla^2V_{\mathrm{eff}}(x)\bigr)\;\le\;\lambda_{\min}\bigl(\mathbb E_{\nu_x}[A]\bigr).$$

(b) Hence *pure marginalisation can never increase the coarse curvature above the fibre-average of the fine $xx$-block*. Any RG scheme built solely from block marginalisation is monotonically curvature-losing; the deficit is exactly the Fisher-information/covariance term $\operatorname{Cov}_{\nu_x}(\nabla_xV)\succeq0$.

(c) Corollary (why the 'dream' monotonicity of the curvature defect is false as an identity). Define, for a target stiffness $\kappa_*>0$, the defect $\delta(H):=\max\{0,\kappa_*-\lambda_{\min}(H)\}$ and the scale functional $\Phi(a):=\mathbb E_{\mu_a}[\delta(H_a^{\mathrm{phys}})]$. The clean monotonicity $\Phi(a')\le\Phi(a)$ ($a'>a$) follows from Jensen + concavity of $\lambda_{\min}$ *if and only if* $H^{\mathrm{phys}}_{a'}=\mathbb E[H^{\mathrm{phys}}_a\mid\mathcal G_{a'}]$. By (a) that identity is false for genuine Wilsonian blocking, where $H_{a'}=\mathbb E[H_a\mid\mathcal G]-\operatorname{Cov}(\nabla S_a\mid\mathcal G)$ (up to Jacobian terms); the covariance term has a definite sign and pushes the defect the *wrong* way. Only the one-sided bound survives.

### Derivation

PROOF OF (a). By the exact identity of the previous item,
$$\nabla^2V_{\mathrm{eff}}(x)=\mathbb E_{\nu_x}[A]-\operatorname{Cov}_{\nu_x}(\nabla_xV).$$
A covariance matrix is positive semidefinite: for any $v$, $v^\top\operatorname{Cov}_{\nu_x}(\nabla_xV)v=\operatorname{Var}_{\nu_x}\!\bigl(v\cdot\nabla_xV\bigr)\ge0$. Hence $\nabla^2V_{\mathrm{eff}}\preceq\mathbb E[A]$. Equality in the matrix sense means $\operatorname{Var}_{\nu_x}(v\cdot\nabla_xV)=0$ for every $v$, i.e. $\nabla_xV(x,\cdot)$ is $\nu_x$-a.s. constant. Monotonicity of $\lambda_{\min}$ under the Loewner order ($P\preceq Q\Rightarrow\lambda_{\min}(P)\le\lambda_{\min}(Q)$, immediate from Rayleigh–Ritz) gives the eigenvalue statement. $\square$

PROOF OF (c). The 'dream' step is: $\lambda_{\min}$ is concave on symmetric matrices (Rayleigh–Ritz: an infimum of linear functionals), so $\lambda_{\min}(\mathbb E[H\mid\mathcal G])\ge\mathbb E[\lambda_{\min}(H)\mid\mathcal G]$; and $x\mapsto\max\{0,\kappa_*-x\}$ is convex and non-increasing, so Jensen yields $\delta(\mathbb E[H\mid\mathcal G])\le\mathbb E[\delta(H)\mid\mathcal G]$ and hence $\Phi$ decreases under conditioning. All of that is correct. What fails is the *hypothesis*: by (a) the coarse physical Hessian is not $\mathbb E[H\mid\mathcal G]$ but $\mathbb E[H\mid\mathcal G]$ minus a PSD covariance, so
$$\lambda_{\min}(H_{a'})\le\lambda_{\min}(\mathbb E[H_a\mid\mathcal G_{a'}])\quad\text{and}\quad\delta(H_{a'})\ge\delta(\mathbb E[H_a\mid\mathcal G_{a'}]),$$
so the two inequalities point in opposite directions and no defect monotonicity follows. The lemma remains usable only as a *lower bound on the averaged Hessian term*, i.e. to bound $\mathbb E[A]$ from below before subtracting the covariance. $\square$

[Reconstructed, mine] STRUCTURAL CONSEQUENCE FOR THE CASCADE. Item 1's recursion contracts only because of the geometric factor $L^{-2}$ concealed in $C_{\mathrm{RG}}\le L^{-d}$. Statement (a) says the *marginalisation* half of an RG step is unconditionally lossy. Therefore every gain in the RG cascade comes from rescaling/blocking geometry, never from integrating out. This is exactly why decimation ($C_{\mathrm{RG}}=1$, no gradient contraction, hence no geometric gain) cannot contract, and why the whole programme depends on a block map that is contractive in the *gradient* sense — a property proved in the corpus only in the linearised weak-field chart.

### Constants and numbers

Loss per marginalisation step in operator norm: $\|\operatorname{Cov}_{\nu_x}(\nabla_xV)\|\le M^2/\gamma$ under $\|B\|\le M$, $C\succeq\gamma I$ (previous item). Loss is exactly zero iff $\nabla_xV$ is fibre-constant, i.e. iff $B\equiv0$ ($x$ and $y$ decouple).

**Caveat.** Statement (a) is unconditional for pure marginalisation only; a real RG step also carries a block map with a Jacobian, which is not covered and is precisely where the $L^2$ rescaling enters.

**Why it matters.** It is the sharp structural reason the corpus's curvature programme can never gain convexity from coarse-graining alone, and it kills the 'defect monotonicity' route to the obstruction principle in its stated form while identifying the one-sided inequality that survives.

---

## 5. Curvature recursion under repeated blocking, the curvature-squared budget law, and the MFIP fixed point

`status: solid` · `kind: derivation`

### Statement

Let $\rho_k>0$ denote the uniform convexity modulus (curvature floor) after $k$ block steps and $M_k$ a uniform bound on the cross-block Hessian norm at step $k$.

(A) [Recursion] Taking $\alpha=\gamma=\rho_k$, $\|B\|\le M_k$ in the block-convexity engine gives
$$\rho_{k+1}\;\ge\;\rho_k-\frac{M_k^2}{\rho_k}\;(-\;\varepsilon_k),$$
where $\varepsilon_k\ge0$ collects truncation/approximation/non-ideality errors.

(B) [Curvature-squared budget law] If $\rho_{k+1}=\rho_k-M_k^2/\rho_k$ (with all $\rho_j>0$), then for every $k$
$$\boxed{\;\rho_k^2\;\ge\;\rho_0^2-2\sum_{j<k}M_j^2\;}$$
Hence convexity survives $k$ steps whenever the cumulative mixing energy satisfies $\sum_{j<k}M_j^2<\rho_0^2/2$.

(C) [MFIP fixed point, affine version with a source] If instead one has the affine recursion with a positive source,
$$\rho_{j+1}\;\ge\;K\rho_j-\varepsilon_j+\sigma_*,\qquad 0<K<1,$$
and $\varepsilon_\infty:=\limsup_{j\to\infty}\varepsilon_j<\infty$, then
$$\boxed{\;\liminf_{j\to\infty}\rho_j\;\ge\;\frac{\sigma_*-\varepsilon_\infty}{1-K}\;}$$
In particular $\sigma_*>\varepsilon_\infty$ implies $\rho_j$ is bounded away from $0$ uniformly in $j$.

### Derivation

PROOF OF (A). This is the previous item, statement (3), with $\alpha=\gamma=\rho_k$: $\rho_{k+1}\ge\rho_k-M_k^2/\rho_k$. Adding a catch-all $-\varepsilon_k$ for Jacobian/truncation terms is bookkeeping.

PROOF OF (B). Square the recursion:
$$\rho_{k+1}^2=\left(\rho_k-\frac{M_k^2}{\rho_k}\right)^2=\rho_k^2-2M_k^2+\frac{M_k^4}{\rho_k^2}\;\ge\;\rho_k^2-2M_k^2,$$
since $M_k^4/\rho_k^2\ge0$. Telescoping from $k=0$ gives $\rho_k^2\ge\rho_0^2-2\sum_{j<k}M_j^2$. $\square$
This is an exact and rather elegant statement: the *square* of the curvature is a budget which each RG step debits by at most $2M_k^2$. It gives the sharp criterion for how many steps a given curvature seed can survive: $k_{\max}=\max\{k:\sum_{j<k}M_j^2<\rho_0^2/2\}$; for constant $M_j\equiv M$, $k_{\max}=\lceil\rho_0^2/(2M^2)\rceil$.

PROOF OF (C). Iterate the affine inequality $n$ times from index $j$:
$$\rho_{j+n}\;\ge\;K^n\rho_j+\sum_{m=0}^{n-1}K^{\,n-1-m}\bigl(\sigma_*-\varepsilon_{j+m}\bigr).$$
(Induction: true for $n=1$; assuming it for $n$, apply $\rho_{j+n+1}\ge K\rho_{j+n}-\varepsilon_{j+n}+\sigma_*$ and collect.) Now let $n\to\infty$ with $j$ large enough that $\varepsilon_{j+m}\le\varepsilon_\infty+\eta$ for all $m\ge0$. Since $0<K<1$, $K^n\rho_j\to0$ and $\sum_{m=0}^{n-1}K^{n-1-m}\to\sum_{i\ge0}K^i=1/(1-K)$, so
$$\liminf_{n}\rho_{j+n}\;\ge\;\frac{\sigma_*-\varepsilon_\infty-\eta}{1-K}.$$
Letting $\eta\downarrow0$ gives the claim. $\square$

[Mine] RELATION BETWEEN (C) AND THE POINCARÉ CASCADE. (C) and the $C_P$ cascade of item 2 are the *same* affine fixed-point machinery read in dual directions. For the Poincaré constant one wants an *upper* bound and iterates $C\mapsto rC+C_{\mathrm{block}}$ down to $C^*=C_{\mathrm{block}}/(1-r)$; for the curvature modulus one wants a *lower* bound and iterates $\rho\mapsto K\rho+(\sigma_*-\varepsilon)$ up to $\rho^*=(\sigma_*-\varepsilon_\infty)/(1-K)$. Both are the geometric series $\sum_k K^k$; both require the same structural input, a contraction factor $<1$; and both have the identical failure mode when the contraction factor exceeds 1. Note also the different *shape* of (A) versus (C): (A) is a *nonlinear* (Riccati-like) recursion $\rho\mapsto\rho-M^2/\rho$ with **no** fixed point other than degradation to zero, while (C) is affine with a source and does have a positive fixed point. Everything therefore hinges on whether the RG step supplies a genuine positive source $\sigma_*$; without it, (B) says the curvature budget is strictly and irreversibly spent.

### Constants and numbers

Budget law: each step debits at most $2M_k^2$ from $\rho^2$. Constant-$M$ survival horizon $k_{\max}=\lceil\rho_0^2/(2M^2)\rceil$.
MFIP fixed point $\rho^*=(\sigma_*-\varepsilon_\infty)/(1-K)$; positivity criterion $\sigma_*>\varepsilon_\infty$.
Lattice instantiation (see the constants item): $M=\beta C_V(N)$, $\rho_0=\rho_*(a)=c_0a^2g^2-\beta C_V(N)$, giving $\rho_{\text{new}}\ge\rho_*-M^2/\rho_*=\rho_*-\dfrac{144}{g^4\rho_*}$ with the non-conservative $C_V=6/N$, $\beta=2N/g^2$ (so $M=12/g^2$).

**Caveat.** (B) is exact algebra but requires $\rho_j>0$ throughout; once $\rho_j$ hits zero the recursion is undefined. (C)'s hypotheses ($K<1$, summable/bounded $\varepsilon_j$, $\sigma_*>0$) are exactly the corpus's Conjectures A and B and are not proved.

**Why it matters.** The budget law $\rho_k^2\ge\rho_0^2-2\sum M_j^2$ is a crisp, exactly-provable quantitative statement of how many RG steps a curvature seed can survive, and it makes explicit that without a source the programme is a finite-budget scheme, not a fixed-point scheme.

---

## 6. Lattice Yang–Mills constants: Haar mass curvature, conservative Wilson Hessian bound, and the two strong-coupling windows

`status: conditional` · `kind: numerical_result`

### Statement

Conventions. $G=\mathrm{SU}(N)$, $\mathfrak g=\mathfrak{su}(N)$ (skew-Hermitian traceless), inner product $\langle X,Y\rangle=-\operatorname{Tr}(XY)$, $\|X\|^2=-\operatorname{Tr}(X^2)$; lattice spacing $a$, bare coupling $g$, $\beta=2N/g^2$; link variables $U_b=\exp(X_b)$ with $X_b=agA_b$, $A_b\in\mathfrak g$; Wilson action $S_W=\sum_pS_p$, $S_p=1-\tfrac1N\operatorname{Re}\operatorname{Tr}U_p$; $S_{\mathrm{eff}}=\beta S_W+S_{\mathrm{Haar}}$.

(H) [Haar mass curvature] Writing $d\mu_H(U)=J(X)dX$ with $J(X)=\det_{\mathfrak g}\!\bigl(\tfrac{\sinh(\mathrm{ad}_X/2)}{\mathrm{ad}_X/2}\bigr)$ and $S_{\mathrm{Haar}}=-\log J$,
$$S_{\mathrm{Haar}}(X)=\frac{N}{12}\|X\|^2+O(\|X\|^4),\qquad \operatorname{Hess}S_{\mathrm{Haar}}(0)=\frac N6 I,\qquad \operatorname{Hess}_AS^{(2)}_{\mathrm{Haar}}=\underbrace{\tfrac N6}_{=:c_0}a^2g^2 I.$$

(W) [Conservative Wilson Hessian bound, mixed derivatives included] For one plaquette, $\bigl|\tfrac{d^2}{dt^2}S_p\bigr|_{t=0}\le\tfrac4N\sum_{i=1}^4\|X_i\|^2$; in $d=4$ each link lies on at most $6$ plaquettes, so $\bigl|\langle A,\operatorname{Hess}S_W(U)A\rangle\bigr|\le C_V(N)\|A\|^2$ with $C_V(N)=24/N$ and $\beta C_V(N)=48/g^2$.

(C) [Finite-cutoff convexity window] With $\rho_*(a):=c_0a^2g^2-\beta C_V(N)=\tfrac N6a^2g^2-\tfrac{48}{g^2}$, if $\rho_*(a)>0$, i.e.
$$\boxed{\,g^4>\frac{288}{Na^2}\,}$$
then $S_{\mathrm{eff}}$ is uniformly horizontally convex with modulus $\rho_*(a)$ and the Langevin generator has spectral gap $\gtrsim\rho_*(a)$.

(R) [RG-stable subwindow] With $M:=\|\operatorname{Hess}(\beta S_W)\|_{\mathrm{op}}\le\beta C_V(N)=48/g^2$, the block-convexity criterion $\rho_*(a)>M$ becomes
$$\boxed{\,g^4>\frac{576}{Na^2}\,}$$
and then the coarse action after one blocking step is still uniformly convex.

(O) [Continuum obstruction] Along the asymptotically free trajectory $a\to0$, $g(a)\to0$, $\beta(a)=2N/g(a)^2\to\infty$: the Haar term $\sim a^2g(a)^2\to0$ while the Wilson term $\sim48/g(a)^2\to\infty$, so $\rho_*(a)\to-\infty$. Global uniform convexity of this type is *violently incompatible* with the continuum limit.

### Derivation

DERIVATION OF (H). For a compact Lie group, $d\mu_H(\exp X)=\det_{\mathfrak g}\!\bigl(\frac{\sinh(\mathrm{ad}_X/2)}{\mathrm{ad}_X/2}\bigr)dX$. Using $\log\frac{\sinh z}{z}=\frac{z^2}{6}+O(z^4)$ with $z=\mathrm{ad}_X/2$,
$$\log J(X)=\operatorname{Tr}_{\mathfrak g}\log\!\Bigl(\frac{\sinh(\mathrm{ad}_X/2)}{\mathrm{ad}_X/2}\Bigr)=\frac{1}{24}\operatorname{Tr}_{\mathfrak g}(\mathrm{ad}_X^2)+O(\|X\|^4),$$
hence $S_{\mathrm{Haar}}(X)=-\tfrac1{24}\operatorname{Tr}_{\mathfrak g}(\mathrm{ad}_X^2)+O(\|X\|^4)$. The Killing form of $\mathfrak{su}(N)$ is $\operatorname{Tr}_{\mathfrak g}(\mathrm{ad}_X\mathrm{ad}_Y)=2N\operatorname{Tr}(XY)$, so $\operatorname{Tr}_{\mathfrak g}(\mathrm{ad}_X^2)=2N\operatorname{Tr}(X^2)=-2N\|X\|^2$. Therefore
$$S_{\mathrm{Haar}}(X)=\frac{2N}{24}\|X\|^2+O(\|X\|^4)=\frac{N}{12}\|X\|^2+O(\|X\|^4),$$
which is strictly convex near $0$ with $\operatorname{Hess}=\tfrac N6I$. [Sign check, mine: for skew-Hermitian $X$, $\mathrm{ad}_X$ has purely imaginary eigenvalues $iy_k$, so $J(X)=\prod_k\frac{\sin(y_k/2)}{y_k/2}\le1$ and $S_{\mathrm{Haar}}=-\log J\ge0$ — consistent, and confirming that the Haar Jacobian really is a convex 'mass' term, not a concave one.] Substituting $X_b=agA_b$: $S^{(2)}_{\mathrm{Haar}}(A)=\tfrac N{12}a^2g^2\sum_b\|A_b\|^2$, so $\operatorname{Hess}_A=\tfrac N6a^2g^2I$, i.e. $c_0=N/6$.

DERIVATION OF (W). Let $S_p(V_1,\dots,V_4)=1-\tfrac1N\operatorname{Re}\operatorname{Tr}(V_1V_2V_3V_4)$ with the variation $V_i(t)=e^{tX_i}V_i$. Differentiating $U_p(t)=V_1(t)\cdots V_4(t)$ twice at $t=0$ gives diagonal terms $(\cdots X_i^2V_i\cdots)$ and mixed terms $(\cdots X_iV_i\cdots X_jV_j\cdots)$, $i\neq j$. Since $|\operatorname{Tr}(\cdots X_i^2V_i\cdots)|\le\|X_i\|^2$ and $|\operatorname{Tr}(\cdots X_iV_i\cdots X_jV_j\cdots)|\le\|X_i\|\|X_j\|$ (unitarity + Cauchy–Schwarz),
$$|S_p''(0)|\le\frac1N\Bigl(\sum_i\|X_i\|^2+\sum_{i\ne j}\|X_i\|\|X_j\|\Bigr)=\frac1N\Bigl(\sum_i\|X_i\|\Bigr)^2\le\frac4N\sum_i\|X_i\|^2,$$
the last step by Cauchy–Schwarz with $4$ terms. Summing over the $\le6$ plaquettes containing a given link gives $C_V(N)=6\cdot\tfrac4N=\tfrac{24}N$. This is conservative precisely because it does *not* discard the mixed link derivatives.

DERIVATION OF (C). $\langle A,\operatorname{Hess}S_{\mathrm{eff}}A\rangle\ge(c_0a^2g^2-\beta C_V)\|A\|^2=\rho_*(a)\|A\|^2$ on horizontal directions. Then $\rho_*(a)>0\iff\tfrac N6a^2g^2>\tfrac{48}{g^2}\iff Na^2g^4>288\iff g^4>288/(Na^2)$.

DERIVATION OF (R). The block-convexity criterion (previous items) with $\alpha=\gamma=\rho_*$ requires $M<\rho_*$; taking $M=\beta C_V=48/g^2$ gives $\tfrac N6a^2g^2-\tfrac{48}{g^2}>\tfrac{48}{g^2}\iff\tfrac N6a^2g^2>\tfrac{96}{g^2}\iff g^4>576/(Na^2)$.

NUMERICAL INSTANTIATION [checked, mine]:
  SU(2) ($N=2$, $c_0=1/3$, $C_V=12$): convexity $g^4>144/a^2$, i.e. $g>144^{1/4}a^{-1/2}=\sqrt{12}\,a^{-1/2}\approx3.4641/\sqrt a$; RG-stable $g^4>288/a^2$, i.e. $g>288^{1/4}a^{-1/2}\approx4.1195/\sqrt a$.
  SU(3) ($N=3$, $c_0=1/2$, $C_V=8$): convexity $g^4>96/a^2$, $g>3.1302/\sqrt a$; RG-stable $g^4>192/a^2$, $g>3.7224/\sqrt a$.

TWO CONSTANT CONVENTIONS COEXIST IN THE CORPUS AND MUST NOT BE MIXED. The conservative set above uses $C_V(N)=24/N$ (mixed derivatives kept). Several longer drafts use the non-conservative $C_V(N)=6/N$ (one unit per plaquette, mixed terms dropped), giving $M=\beta C_V=12/g^2$, $\rho_{\text{new}}\ge\rho_*-144/(g^4\rho_*)$, and the softer windows $g^4>12/(c_0a^2)$ (convexity) and $g^4>24/(c_0a^2)$ (RG-stable); for SU(2) these read $g^4>36/a^2$ and $g^4>72/a^2$. The v2 note states explicitly that it fixes sign/constant issues in the longer drafts, so the conservative set is the one to quote.

DERIVATION OF (O). Along an asymptotically free trajectory $g(a)\to0$ as $a\to0$; then $c_0a^2g(a)^2\to0$ and $\beta(a)C_V(N)=48/g(a)^2\to+\infty$, so $\rho_*(a)=c_0a^2g(a)^2-48/g(a)^2\to-\infty$ monotonically past a finite $a$. Since the windows require $g^4a^2>\mathrm{const}$, i.e. $g\gtrsim a^{-1/2}\to\infty$, they are *strong-coupling* windows that recede from the continuum trajectory. Hence the strong-coupling window $0<\beta<\beta_c(a)$ cannot contain the continuum $\beta(a)$, and $\rho_*(a,\beta(a))$ must change sign before the continuum is reached.

### Constants and numbers

$c_0=N/6$ (SU(2): $1/3$; SU(3): $1/2$). Haar Hessian at identity: $\tfrac N6I$; per-link lattice Haar curvature $c_0a^2g^2$.
$C_V(N)=24/N$ conservative (SU(2): 12; SU(3): 8); $C_V(N)=6/N$ non-conservative (SU(2): 3; SU(3): 2).
$\beta=2N/g^2$; $\beta C_V=48/g^2$ (conservative) or $12/g^2$ (non-conservative).
$\rho_*(a)=\tfrac N6a^2g^2-\tfrac{48}{g^2}$.
Convexity window: $g^4>288/(Na^2)$ — SU(2) $144/a^2$ ($g>3.4641a^{-1/2}$), SU(3) $96/a^2$ ($g>3.1302a^{-1/2}$).
RG-stable window: $g^4>576/(Na^2)$ — SU(2) $288/a^2$ ($g>4.1195a^{-1/2}$), SU(3) $192/a^2$ ($g>3.7224a^{-1/2}$).
Non-conservative analogues: $g^4>12/(c_0a^2)$ and $g^4>24/(c_0a^2)$; SU(2): $36/a^2$, $72/a^2$.
Supporting SU(2) Wilson-Hessian scan (corpus numerics): $\lambda_{\min}(W)=-0.059,-0.137,-0.270$ at $\beta=0.5,1.0,2.0$; with the Haar term added $+0.191,+0.113,-0.020$ — the Haar term lifts the spectrum at moderate $\beta$ but does not cure negativity at $\beta=2$, consistent with (O).
Related SU(2) anomaly-source measurements (4^4 lattice, 50 configs, $\kappa=-1$, $\beta_0=22/3$): $\sigma_{\mathrm{anom}}=6.17,4.64,3.72,3.10,2.32\times10^{-2}$ at $\beta=1.5,2.0,2.5,3.0,4.0$ with $\langle F^2\rangle=0.996\pm0.011$ to $1.000\pm0.011$.

### Code

Exact Haar Jacobian potential (autodiff-friendly, torch.float64), from RG_COARSE/05_Simulations_Numerics/PRO12_CODE_Colab_Hessian_Flow.py:

  haar_potential(x, basis_T, quad_n=8)
      # V_Haar(X) = -log det( ∫_0^1 exp(-s ad_X) ds ),  X = sum_a x_a T_a
      # computes ad_X in an orthonormal basis (Tr(T_a T_b) = -1/2 δ_ab),
      # integrates by 8-node Gauss–Legendre on [0,1], then torch.linalg.slogdet.
  su2_basis(dev), su3_basis(dev)   # anti-Hermitian generators
  wilson_action(U, lat, beta)      # standard plaquette action
  hvp(action_fn, x, v)             # autodiff Hessian-vector products

Run: `python PRO12_CODE_Colab_Hessian_Flow.py --demo haar` (checks the Haar constant $N/6$ numerically at small $x$), `--demo su3 --L 2 --D 4 --beta 2.0`.
Note: the sign returned by slogdet must be positive; a flip means the exponential chart is larger than the SAFE radius $R_0$ and must be shrunk.

**Caveat.** $\rho_*(a)$ is a *global* bound over the whole configuration space; it is exactly this globality that (O) destroys. The conditional route left open by the corpus is a localised bound valid only on a high-probability core, with the complement controlled by measure or Dirichlet capacity.

**Why it matters.** These are the only fully explicit numbers in the whole coarse-graining programme, and (O) is the corpus's sharpest self-diagnosis: it proves the Haar spark is a finite-cutoff strong-coupling phenomenon, not a continuum mechanism, and thereby dictates that any continuum-relevant statement must come from a cutoff-independent source.

---

## 7. Conditional spectral floor monotonicity and defect monotonicity under conditioning

`status: solid` · `kind: theorem`

### Statement

(1) [Matrix version] Let $(\Omega,\mathcal F,\mathbb P)$ be a probability space, $H:\Omega\to\mathbb R^{n\times n}$ symmetric-matrix-valued and integrable, $\mathcal G\subseteq\mathcal F$ a sub-$\sigma$-algebra. Then for $\mathbb P$-a.e. $\omega$,
$$\boxed{\;\lambda_{\min}\bigl(\mathbb E[H\mid\mathcal G](\omega)\bigr)\;\ge\;\mathbb E\bigl[\lambda_{\min}(H)\mid\mathcal G\bigr](\omega).\;}$$

(2) [Quadratic-form version] Let $H(\omega)$ be random self-adjoint operators on a Hilbert space $\mathcal H$, uniformly bounded below ($H(\omega)\ge-CI$ for a fixed $C<\infty$), with a common dense form domain $\mathcal D$, and $\omega\mapsto\langle\psi,H(\omega)\psi\rangle$ integrable for each $\psi\in\mathcal D$. Let $\bar H$ be the self-adjoint operator associated with the closed form $\langle\psi,\bar H\psi\rangle:=\mathbb E[\langle\psi,H(\omega)\psi\rangle\mid\mathcal G]$. Then $\inf_{\|\psi\|=1}\langle\psi,\bar H\psi\rangle\ge\mathbb E[\inf_{\|\psi\|=1}\langle\psi,H(\omega)\psi\rangle\mid\mathcal G]$.

(3) [Defect monotonicity] For a target stiffness $\kappa_*>0$ set $\delta(A):=\max\{0,\kappa_*-\lambda_{\min}(A)\}$. Then $\delta(\mathbb E[H\mid\mathcal G])\le\mathbb E[\delta(H)\mid\mathcal G]$: defect cannot increase under conditioning.

(4) [Quotient lemma] Let $H$ be self-adjoint and bounded below on $\mathcal H$, and $\mathcal N\subseteq\mathcal H$ closed with $\mathcal N\subseteq\ker H$. Let $\widetilde H$ be the induced operator on $\mathcal H/\mathcal N$. Then $\lambda_{\inf}(\widetilde H)=\lambda_{\inf}(H)$: quotienting (as in OS reconstruction) cannot lower the spectral floor.

### Derivation

PROOF OF (1). Rayleigh–Ritz: $\lambda_{\min}(A)=\min_{\|v\|=1}\langle v,Av\rangle$, so $\lambda_{\min}$ is an infimum of linear functionals of $A$, hence *concave* on symmetric matrices. Fix a unit vector $v$. Linearity of conditional expectation gives
$$\langle v,\mathbb E[H\mid\mathcal G]v\rangle=\mathbb E[\langle v,Hv\rangle\mid\mathcal G]\;\ge\;\mathbb E[\lambda_{\min}(H)\mid\mathcal G],$$
using $\langle v,Hv\rangle\ge\lambda_{\min}(H)$ pointwise and monotonicity of conditional expectation. The right-hand side does not depend on $v$; minimise the left-hand side over unit $v$. $\square$
(Equivalently: conditional Jensen for the concave function $\lambda_{\min}$.)

PROOF OF (2). Identical, with $\mathcal D$ in place of $\mathbb R^n$ and the infimum taken over unit $\psi\in\mathcal D$; the uniform lower bound (H3) is what guarantees the averaged form is closed and bounded below so that $\bar H$ exists.

PROOF OF (3). $x\mapsto\max\{0,\kappa_*-x\}$ is convex and non-increasing; $\lambda_{\min}$ is concave; a non-increasing convex function of a concave function is convex. Apply conditional Jensen to the convex function $\delta\circ(\cdot)$, or directly: by (1), $\lambda_{\min}(\mathbb E[H|\mathcal G])\ge\mathbb E[\lambda_{\min}(H)|\mathcal G]$; applying the non-increasing map $x\mapsto\max\{0,\kappa_*-x\}$ reverses this to $\delta(\mathbb E[H|\mathcal G])\le\max\{0,\kappa_*-\mathbb E[\lambda_{\min}(H)|\mathcal G]\}$, and conditional Jensen for the convex map bounds the right-hand side by $\mathbb E[\delta(H)|\mathcal G]$. $\square$

PROOF OF (4). Every coset in $\mathcal H/\mathcal N$ has a representative orthogonal to $\mathcal N$; vectors in $\mathcal N$ carry zero $H$-energy, so the set of Rayleigh quotients is unchanged and the infima coincide. $\square$

NUMERICAL SANITY CHECK (recorded in the corpus and reproduced here). Draw $100$ i.i.d. symmetric $8\times8$ matrices $H_i=(A_i+A_i^\top)/2$ with $A_i$ standard Gaussian, seed 0; 'condition' by binning into $10$ groups of $10$; compare $\lambda_{\min}$ of the bin average with the bin average of $\lambda_{\min}$. All ten differences are positive, ranging $2.012$ to $2.352$ (rounded to 3 dp: 2.280, 2.161, 2.246, 2.012, 2.311, 2.167, 2.259, 2.352, 2.190, 2.281), with bin-average floors $\approx-1.0$ versus averaged floors $\approx-3.2$. The large positive gap is the expected Wigner-type effect: averaging $10$ independent GOE-like matrices shrinks the spectral radius by $\approx\sqrt{10}$.

SCOPE: WHERE THIS LEMMA MAY AND MAY NOT BE USED. It applies verbatim whenever a step of an argument is *literally* a conditional expectation of an operator in quadratic-form sense — the 'structural refactor' discipline of the corpus rewrites localisation, drift decomposition, clustering and thermodynamic-limit steps in this form, so that gap preservation becomes a one-line invariant. It does **not** apply to Wilsonian blocking, where the coarse Hessian is $\mathbb E[H\mid\mathcal G]-\operatorname{Cov}(\nabla S\mid\mathcal G)$ and the covariance defeats the inequality (see the monotone-degradation item).

### Constants and numbers

Sanity check: $n=8$, $100$ matrices, $10$ bins of $10$, seed 0. Differences $\lambda_{\min}(\mathbb E[H|\mathcal G])-\mathbb E[\lambda_{\min}(H)|\mathcal G]$ per bin: 2.280, 2.161, 2.246, 2.012, 2.311, 2.167, 2.259, 2.352, 2.190, 2.281; minimum 2.012 > 0.

### Code

    import numpy as np, numpy.linalg as la
    np.random.seed(0); n, num = 8, 100
    mats = [(lambda A: (A+A.T)/2)(np.random.normal(size=(n,n))) for _ in range(num)]
    for i in range(0, num, 10):
        g = mats[i:i+10]
        lam_avg  = la.eigvalsh(sum(g)/len(g))[0]              # lambda_min( E[H|G] )
        lam_cond = sum(la.eigvalsh(m)[0] for m in g)/len(g)   # E[ lambda_min(H) | G ]
        assert lam_avg >= lam_cond

**Caveat.** Correct and elementary; the only real risk is misapplication — the corpus itself notes that a Wilsonian effective Hessian is not a conditional expectation of fine Hessians, so this lemma is a bound on the averaged term only, never an identity for the coarse Hessian.

**Why it matters.** It is the one nontrivial inequality needed to make every 'localise / average / restrict' step in a multiscale proof gap-preserving by construction, and (4) seals the OS-reconstruction quotient seam.

---

## 8. vHJ effective-action flow: Hessian evolution equation, exact Gaussian solution, and the resolved α-universality

`status: solid` · `kind: derivation`

### Statement

Let $S_0:\mathbb R^m\to\mathbb R$ be smooth with $e^{-S_0}$ integrable, and define the heat-smoothed family $e^{-S_t}:=e^{t\nu\Delta}e^{-S_0}$ (so $\rho_t:=e^{-S_t}$ solves $\partial_t\rho=\nu\Delta\rho$).

(1) [vHJ equation] $S_t$ solves $\;\partial_tS_t=\nu\Delta S_t-\nu\|\nabla S_t\|^2$ (written below with $\nu=1$).

(2) [Hessian flow] With $H_t:=\nabla^2S_t$,
$$\boxed{\;\partial_tH_t=\Delta H_t-2H_t^2-2\sum_{k=1}^m(\partial_kS_t)\,\partial_kH_t\;}$$
i.e. $\partial_tH=\Delta H-2H^2-2\nabla_{\nabla S}H$: a matrix Riccati reaction $-2H^2$, a diffusion, and a pure *transport* term (no zeroth order), which is exactly what makes a tensor maximum principle applicable.

(3) [Exact Gaussian solution] If $S_0(x)=\tfrac12x^\top H_0x$ with $H_0\succ0$, then for all $t\ge0$, $S_t(x)=\tfrac12x^\top H_tx+\mathrm{const}$ with
$$\boxed{\;H_t^{-1}=H_0^{-1}+2\nu t\,I\;}\qquad\Longleftrightarrow\qquad \frac{1}{\lambda_i(t)}=\frac{1}{\lambda_i(0)}+2\nu t,\qquad \dot\lambda_i=-2\nu\lambda_i^2,$$
with eigenvectors *frozen*. Hence $\lambda_{\min}(t)=\lambda_{\min}(0)/(1+2\nu t\lambda_{\min}(0))\sim1/(2\nu t)\to0$.

(4) [Resolution of the 'universal α' phenomenon — mine] The corpus reports as a mysterious empirical fact that fitted Riccati coefficients $\alpha_i$ in $1/\lambda_i(t)=1/\lambda_i(0)+\alpha_it$ are nearly identical across eigenmodes (relative spread $\sim0.04$–$0.1\%$). By (3), for quadratic initial data the mode-independence of $\alpha$ is an **exact identity**, $\alpha_i\equiv2\nu$ for every $i$, not an empirical coincidence: the flow of $H^{-1}$ is a rigid translation by $2\nu tI$.

### Derivation

PROOF OF (1). Put $\rho_t=e^{-S_t}$. Then $\partial_t\rho=-(\partial_tS)e^{-S}$ and $\Delta\rho=e^{-S}(-\Delta S+\|\nabla S\|^2)$. Substituting into $\partial_t\rho=\Delta\rho$ and cancelling $e^{-S}>0$ gives $\partial_tS=\Delta S-\|\nabla S\|^2$. $\square$

PROOF OF (2). Differentiate the vHJ equation twice. First, $\partial_i\partial_j\Delta S=\Delta(\partial_i\partial_jS)=(\Delta H)_{ij}$. Second,
$$\partial_i\|\nabla S\|^2=2\sum_k(\partial_kS)(\partial_i\partial_kS)=2\sum_k S_kH_{ik},$$
$$\partial_j\partial_i\|\nabla S\|^2=2\sum_k\bigl[(\partial_j\partial_kS)(\partial_i\partial_kS)+(\partial_kS)(\partial_j\partial_i\partial_kS)\bigr]=2(H^2)_{ij}+2\sum_kS_k\,\partial_jH_{ik}.$$
Because $\partial_jH_{ik}=\partial_i\partial_j\partial_kS$ is totally symmetric in $(i,j,k)$, $\partial_jH_{ik}=\partial_kH_{ij}$, so the last term is $2\sum_k(\partial_kS)(\partial_kH_{ij})=2\nabla_{\nabla S}H_{ij}$. Hence
$$\partial_tH_{ij}=(\Delta H)_{ij}-2(H^2)_{ij}-2\sum_k(\partial_kS)(\partial_kH_{ij}).\;\square$$
The corpus records this in two equivalent forms; note that the residual is *not* a generic 'remainder $R_t$' but a genuine transport term, which is why the maximum principle applies with no extra hypotheses.

PROOF OF (3). $e^{-S_0}$ is (up to normalisation) the Gaussian density with covariance $\Sigma_0=H_0^{-1}$. The heat semigroup at time $t$ is convolution with the Gaussian of covariance $2\nu tI$; convolution of Gaussians adds covariances, so $\Sigma_t=\Sigma_0+2\nu tI$ and $H_t=\Sigma_t^{-1}=(H_0^{-1}+2\nu tI)^{-1}$. Diagonalising $H_0=Q^\top\Lambda_0Q$ gives $H_t=Q^\top(\Lambda_0^{-1}+2\nu tI)^{-1}Q$, i.e. eigenvectors fixed and $\lambda_i(t)=\lambda_i(0)/(1+2\nu t\lambda_i(0))$; differentiating, $\dot\lambda_i=-2\nu\lambda_i^2$. Consistency with (2): for a quadratic $S$, $\nabla H\equiv0$ and $\Delta H\equiv0$, so (2) reduces to $\dot H=-2H^2$, whose solution in functional calculus is exactly $H_t^{-1}=H_0^{-1}+2t$. $\square$

NUMERICAL CONFIRMATION [mine]. Random $H_0=AA^\top+2I$ ($4\times4$, seed 0), $\nu=1$: computing $(1/\lambda_i(t)-1/\lambda_i(0))/t$ at $t=0.05$ and $t=0.135$ gives exactly $[2,2,2,2]$ to machine precision for all four modes.

REPRODUCTION OF THE CORPUS'S RECORDED 4D RUNS [mine]. The recorded tables are 4×4 centre-point Hessian spectra of a JAX vHJ solver on a $24^4$ periodic grid over $[-2,2)^4$ ($dx=1/6$), sampled every 30 steps to step 270. Refitting $1/\lambda_i$ against step index by least squares reproduces the corpus's published $\alpha_i$ to all printed digits:
  quadratic baseline: $\alpha=(1.0022789,\,1.0026004,\,1.0028736,\,1.0033081)\times10^{-3}$, intercepts $(0.3187423,0.2630756,0.2272640,0.1831388)$; mean $1.002765\times10^{-3}$, spread $1.03\times10^{-6}$ ($0.103\%$); max relative residual of the Riccati fit $0.9$–$3.8\times10^{-4}$.
  Haar-augmented: $\alpha=(7.880153,\,7.916689,\,7.939418,\,7.967519)\times10^{-4}$, mean $7.92595\times10^{-4}$, spread $8.7\times10^{-6}$ ($1.10\%$); residuals $1.5$–$2.9\times10^{-3}$.
  Haar+YM+SU(3)-type: mean $7.99543\times10^{-4}$, spread $3.845\times10^{-6}$ ($0.48\%$).
CALIBRATION [mine]: since (3) gives $\alpha_{\text{per unit time}}=2\nu$ exactly, the measured *per-step* $\alpha=1.002765\times10^{-3}$ implies an effective $\nu\,dt=5.0138\times10^{-4}$. For $dx=1/6$ in $d=4$, the explicit-Euler heat-stability bound is $dt\le dx^2/(4d\nu)=1.736\times10^{-3}$, so the run sits comfortably inside stability at $\nu=1$, $dt\approx5\times10^{-4}$. Everything about the baseline run is therefore fully explained.
CORRECTION [mine]: the corpus reports $\alpha_3=7.627501\times10^{-4}$ for the Haar+YM+SU(2)-adjoint run and quotes spread $3.533\times10^{-5}$. Refitting its own printed eigenvalue table gives $\alpha_3=7.963723\times10^{-4}$ and spread $1.057\times10^{-5}$ ($1.33\%$); the published $\alpha_3$ is inconsistent with the published table and is almost certainly a transcription error. It is that single value which creates the apparent SU(2) 'anisotropy' outlier.
INTERPRETATION [mine]: within each run the fit is essentially exact ($10^{-4}$ relative residuals for the quadratic run — the signature of the exact Gaussian identity), while the *non*-quadratic runs have residuals 10–40× larger ($2$–$4\times10^{-3}$), confirming that the added isotropic 'Haar' terms genuinely make the flow nonlinear. The drop in $\alpha$ from $1.0028\times10^{-3}$ (quadratic) to $\approx7.9\times10^{-4}$ (Haar-stabilised), a factor $0.786$–$0.794$, is the one genuinely non-trivial claim in the α-band data: an isotropic curvature source slows the Riccati decay by about $21\%$. (A confound remains: the same ratio would result from a different $\nu\,dt$ in those runs; the corpus does not record per-run $dt$.)

### Constants and numbers

Exact law: $1/\lambda_i(t)=1/\lambda_i(0)+2\nu t$, $\alpha_{\text{true}}=2\nu$ per unit time, mode-independent.
Grid: $L=24$ per dimension, box $[-2,2)^4$, $dx=4/24=0.166667$; explicit stability $dt\le dx^2/(4d\nu)=1.736\times10^{-3}$; inferred $\nu\,dt=5.0138\times10^{-4}$.
α-band (per step, 4D runs, 270 steps sampled every 30):
  Quadratic:      mean $1.002765\times10^{-3}$, spread $1.03\times10^{-6}$ ($0.10\%$)
  Haar:           mean $7.92595\times10^{-4}$, spread $8.74\times10^{-6}$ ($1.10\%$)
  Haar+YM:        mean $\approx7.8125\times10^{-4}$
  Haar+YM+SU(2):  mean $7.93814\times10^{-4}$, spread $1.057\times10^{-5}$ [corrected; corpus reports mean $7.85408\times10^{-4}$, spread $3.533\times10^{-5}$]
  Haar+YM+SU(2)+SU(3): mean $7.99543\times10^{-4}$, spread $3.845\times10^{-6}$
  SU(3)-commutator: mean $7.95186\times10^{-4}$, spread $1.4112\times10^{-5}$
2D/other run reported in the alpha-band note: $\alpha=1.0214540\times10^{-3}$, intercept $b=1/\lambda(0)=0.2387851562$.
Ratio Haar/quadratic $\approx0.786$–$0.794$.

### Code

Core 4D JAX solver (HESSIAN/vHJ_Riccati/02_vHJ_CurvatureFlow_Simulations_v2.md), copy-paste runnable:

    def make_grid_4d(L=24, X=2.0):
        dx = (2*X)/L
        xs = jnp.linspace(-X, X, L, endpoint=False)
        return jnp.stack(jnp.meshgrid(xs,xs,xs,xs, indexing='ij'), axis=-1), dx
    def laplace4(S, dx):
        return (-8.0*S + sum(jnp.roll(S,s,a) for a in range(4) for s in (1,-1)))/(dx*dx)
    def grad2_4(S, dx):
        return sum(((jnp.roll(S,-1,a)-jnp.roll(S,1,a))/(2*dx))**2 for a in range(4))
    @jax.jit
    def vHJ_step(S, dx, dt, nu=1.0):
        return S + dt*(nu*laplace4(S,dx) - grad2_4(S,dx))
    hessian4_at(S, dx, idx)          # 4x4 centre Hessian by central differences
    center_hessian_eigs(S, dx)       # sorted eigvalsh of the centre Hessian
    make_S0_family(grid, Hmat, m2, lam4, gamma_YM, lambda_SU2, lambda_SU3, C2_SU3=3.0)
        # quad + (m2/2) r^2 + lam4 r^4 + gamma_YM * sum_{i<j} x_i^2 x_j^2
        #      + lambda_SU2 * 2(x1^2+x2^2+x3^2) + lambda_SU3 * C2 * r^2

α-extraction and the exactness check (mine, numpy):

    steps = np.array([0,30,60,90,120,150,180,210,240,270])
    alpha, b = np.polyfit(steps, 1/lam_i, 1)          # 1/lambda_i = b + alpha*step
    pred = 1/(b + alpha*steps); resid = np.max(abs(pred-lam_i)/lam_i)
    # Gaussian exactness: for any H0>0, ( 1/eig(inv(inv(H0)+2*nu*t*I)) - 1/eig(H0) )/t == 2*nu

**Caveat.** Only the centre-point Hessian is tracked, on a periodic box whose diffusion length reaches the boundary within the simulated window; nothing here is gauge-covariant, uniform in volume, or connected to a transfer-matrix spectrum.

**Why it matters.** It supplies the exact solution of the corpus's central dynamical object, converts its headline 'mode-universal Riccati decay' from a mystery into a one-line identity, calibrates the simulation parameters, corrects a published fitted constant — and, most importantly, exhibits $\lambda_{\min}(t)\sim1/(2\nu t)\to0$: pure heat-flow coarse-graining destroys convexity, so any gap must come from a source term.

---

## 9. Horizontal tensor maximum principle: matrix Riccati inequality ⇒ scalar Riccati inequality

`status: conditional` · `kind: theorem`

### Statement

Let $(M,g)$ be a compact Riemannian manifold without boundary (or with boundary and Neumann conditions), $H\subset TM$ a smooth metric subbundle ('horizontal directions'), $\nabla^H$ a metric connection on $H$ (e.g. the projected Levi-Civita connection $\nabla^H_XY:=\Pi(\nabla_XY)$, $\Pi:TM\to H$ the $g$-orthogonal projection), and $\Delta_H P:=\operatorname{tr}_g(\nabla^H\nabla^HP)$ the rough Laplacian on $\operatorname{End}(H)$.

Hypotheses. Let $P_t\in C^\infty([0,T]\times M;\operatorname{Sym}(H))$ satisfy, in the sense of quadratic forms on $H$,
$$(\mathrm{MP})\qquad(\partial_t-\Delta_H)P_t\;\succeq\;-\alpha P_t^2+\Sigma_t,\qquad\alpha>0,$$
with the source/error split
$$(\mathrm{SE})\qquad\Sigma_t(x)\;\succeq\;\sigma_*(t)\,I_H-E_t(x),\qquad\|E_t(x)\|_{\mathrm{op}}\le\varepsilon(t)\ \ \forall x\in M.$$

Conclusion. $\lambda(t):=\min_{x\in M}\lambda_{\min}(P_t(x))$ is locally Lipschitz and satisfies, in the viscosity sense (hence for a.e. $t$),
$$\boxed{\;\dot\lambda(t)\;\ge\;-\alpha\,\lambda(t)^2+\sigma_*(t)-\varepsilon(t)\;}$$
and if $\ell$ solves $\dot\ell=-\alpha\ell^2+\sigma_*(t)-\varepsilon(t)$ with $\ell(0)\le\lambda(0)$, then the tensor bound propagates: $P_t(x)\succeq\ell(t)I_H$ for all $(t,x)\in[0,T]\times M$.

Corollary ('positive source survives errors'). If $\sigma_*(t)\ge\sigma_0$ and $\varepsilon(t)\le\varepsilon_0$ with $\sigma_{\mathrm{eff}}:=\sigma_0-\varepsilon_0>0$, the comparison ODE has the stable fixed point $\lambda_*=\sqrt{\sigma_{\mathrm{eff}}/\alpha}>0$, and $\lambda(0)\ge0$ implies $\lambda(t)\to\lambda_*$. The single algebraic requirement is $\boxed{\sigma_0>\varepsilon_0}$.

### Derivation

FULL PROOF (reproduced; this is one of the most carefully executed arguments in the corpus).

Step 1 — reduce $\lambda_{\min}$ to a scalar test function. Fix $t_0\in(0,T)$ and choose $x_0\in M$ attaining $\lambda(t_0)=\lambda_{\min}(P_{t_0}(x_0))$ (exists by compactness and continuity of $\lambda_{\min}$). Choose a unit $v_0\in H_{x_0}$ with $P_{t_0}(x_0)v_0=\lambda(t_0)v_0$. Extend $v_0$ to a local section $v\in\Gamma(H)$ by $\nabla^H$-parallel transport along radial geodesics from $x_0$, so that
$$|v(x)|\equiv1,\qquad(\nabla^Hv)(x_0)=0.$$
Set $\phi(x,t):=\langle P_t(x)v(x),v(x)\rangle_{g_H}$. Then $\phi(x_0,t_0)=\lambda(t_0)$ and, since $|v(x)|=1$,
$$\phi(x,t_0)\ge\lambda_{\min}(P_{t_0}(x))\ge\lambda(t_0)=\phi(x_0,t_0),$$
so $x\mapsto\phi(x,t_0)$ has a *local minimum at $x_0$*.

Step 2 — compute $(\partial_t-\Delta)\phi$ at $(x_0,t_0)$. Since $v$ is $t$-independent, $\partial_t\phi=\langle(\partial_tP_t)v,v\rangle$. For the Laplacian, the product rule in a local orthonormal frame $\{e_i\}$ gives
$$\Delta\langle Pv,v\rangle=\langle(\Delta_HP)v,v\rangle+2\sum_i\langle(\nabla^H_{e_i}P)(\nabla^H_{e_i}v),v\rangle+2\sum_i\langle(\nabla^H_{e_i}P)v,\nabla^H_{e_i}v\rangle+2\langle P\Delta_Hv,v\rangle+2\sum_i\|{\cdot}\|\text{-terms in }\nabla^Hv.$$
At $x_0$, $(\nabla^Hv)(x_0)=0$ kills every term containing $\nabla^Hv$, leaving
$$(\Delta\phi)(x_0,t_0)=\langle(\Delta_HP_{t_0})(x_0)v_0,v_0\rangle+2\langle P_{t_0}(x_0)(\Delta_Hv)(x_0),v_0\rangle.$$
The second term vanishes: differentiating $|v|^2\equiv1$ twice gives $0=\Delta\langle v,v\rangle=2\langle\Delta_Hv,v\rangle+2\sum_i\|\nabla^H_{e_i}v\|^2$, so at $x_0$ (where $\nabla^Hv=0$) $\langle(\Delta_Hv)(x_0),v_0\rangle=0$; and since $v_0$ is an eigenvector, $\langle P(\Delta_Hv),v_0\rangle=\langle\Delta_Hv,Pv_0\rangle=\lambda(t_0)\langle\Delta_Hv,v_0\rangle=0$. Hence
$$(\partial_t-\Delta)\phi(x_0,t_0)=\bigl\langle\bigl((\partial_t-\Delta_H)P_{t_0}\bigr)(x_0)v_0,v_0\bigr\rangle.$$

Step 3 — maximum-principle sign. At an interior spatial minimum, $(\Delta\phi)(x_0,t_0)\ge0$, hence $\partial_t\phi(x_0,t_0)\ge(\partial_t-\Delta)\phi(x_0,t_0)$.

Step 4 — insert (MP) and (SE), testing on $v_0$:
$$\bigl\langle((\partial_t-\Delta_H)P_{t_0})v_0,v_0\bigr\rangle\ge-\alpha\langle P_{t_0}^2v_0,v_0\rangle+\langle\Sigma_{t_0}v_0,v_0\rangle.$$
Since $v_0$ is an exact eigenvector with eigenvalue $\lambda(t_0)$, $\langle P_{t_0}^2v_0,v_0\rangle=\lambda(t_0)^2$ **exactly** (no inequality is needed here). By (SE), $\langle\Sigma_{t_0}v_0,v_0\rangle\ge\sigma_*(t_0)-\varepsilon(t_0)$. Combining with Step 3,
$$\partial_t\phi(x_0,t_0)\ge-\alpha\lambda(t_0)^2+\sigma_*(t_0)-\varepsilon(t_0).$$

Step 5 — from $\partial_t\phi$ to $\lambda$. $\lambda(t)$ is a min over space *and* direction and may fail to be differentiable where the minimiser jumps; but the above shows $\lambda$ is a viscosity supersolution of the ODE, hence locally Lipschitz and satisfying it for a.e. $t$; the Dini-derivative route with $\eta$-minimisers gives the same with an $o(1)$ term. Standard ODE comparison then yields $\lambda(t)\ge\ell(t)$, i.e. the propagated tensor bound. $\square$

[Mine] TECHNICAL CORRECTION TO A RELATED ARGUMENT IN THE CORPUS. Two other files (SELECTED_02_Operator_Riccati_PBH_Flow.md, BEST_04_riccati_convexity_restoration.md) prove the analogous *operator* statement ($\partial_tH\succeq-2H^2+\sigma I$ on a Hilbert space $\Rightarrow\dot\lambda\ge-2\lambda^2+\sigma$ for $\lambda=\inf\operatorname{spec}H$) and invoke '$\langle v,H^2v\rangle\ge\langle v,Hv\rangle^2$ (Cauchy–Schwarz for the spectral measure)'. That inequality points the *wrong way* for a lower bound on $\dot\lambda$. The step is unnecessary when $\lambda$ is attained by an eigenvector (then $\langle v,H^2v\rangle=\lambda^2$ exactly, as in Step 4). When the infimum is not attained, the correct fix is a spectral-projection argument: for $\epsilon>0$ take a unit $v$ in the range of the spectral projection $E_{[\lambda,\lambda+\epsilon]}(H)$; then $\langle v,H^2v\rangle\le\max\{\lambda^2,(\lambda+\epsilon)^2\}$, so $-2\langle v,H^2v\rangle\ge-2\max\{\lambda^2,(\lambda+\epsilon)^2\}$, and letting $\epsilon\downarrow0$ recovers $D^+\lambda\ge-2\lambda^2+\sigma$. This repairs the operator version.

PBH SPECIALISATION (the intended application). On the regular stratum $\mathcal M_{\mathrm{reg}}=\mathcal A_{\mathrm{reg}}/\mathcal G$ with $V_t=\nabla_HS_t$, $h_t=\nabla^2_HS_t$ and the horizontal vHJ equation $\partial_tS_t=\Delta_HS_t-|\nabla_HS_t|^2+J_t$, differentiating twice gives the Projected Bochner–Hessian flow
$$\partial_th_t=\Delta_Hh_t-2\nabla_{V_t}h_t-2h_t^2+S_{\mathrm{anom}}(t)+\mathfrak G(S_t,h_t),\qquad S_{\mathrm{anom}}(t):=\nabla^2_HJ_t,$$
where $\mathfrak G$ bundles curvature commutators and horizontal non-integrability corrections. Under (Curv) $|K_t(X,Y)|\le C_0g(t)^2$, (Trace) $\sum_i\max\{\lambda_i,0\}\le H_{\mathrm{Tr}}$, one gets $|\langle\mathfrak G,v\otimes v\rangle|\le C_1g(t)^2H_{\mathrm{Tr}}$, and under (Anom) $\langle v,S_{\mathrm{anom}}v\rangle\ge\sigma_A$ the theorem yields
$$\partial_t\lambda_{\min}\ge-2\lambda_{\min}^2+\sigma_A-C_1g(t)^2H_{\mathrm{Tr}}.$$
Under (AF) $g(t)\to0$, choose $T_1$ with $C_1g(t)^2H_{\mathrm{Tr}}<\sigma_A/2$ for $t\ge T_1$; then $\partial_t\lambda_{\min}\ge-2\lambda_{\min}^2+\sigma_A/2$ with stable equilibrium $\lambda_{\mathrm{eq}}=\sqrt{\tfrac12\cdot\tfrac{\sigma_A}{2}}=\tfrac{\sqrt{\sigma_A}}{2}$.

[Mine] CORRECTION TO THE COROLLARY AS STATED IN THE SOURCE. The source asserts that if $\lambda(0)<0$ the solution is 'still driven upward and crosses to $\ge0$ in finite time provided $\sigma_{\mathrm{eff}}>0$'. That is false: the comparison ODE has an *unstable* fixed point at $-\lambda_*$, and initial data below it blow down to $-\infty$ in finite time. The correct hypothesis is $\lambda(0)>-\sqrt{\sigma_{\mathrm{eff}}/\alpha}$.

### Constants and numbers

Comparison ODE fixed point $\lambda_*=\sqrt{\sigma_{\mathrm{eff}}/\alpha}$; for the vHJ normalisation $\alpha=2$, $\lambda_*=\sqrt{\sigma_{\mathrm{eff}}/2}$.
PBH specialisation: after the (AF) cut, $\sigma\to\sigma_A/2$ and $\lambda_{\mathrm{eq}}=\sqrt{\sigma_A}/2$.
Error-dominance condition: $C_1g(t)^2H_{\mathrm{Tr}}<\sigma_A/2$ for $t\ge T_1$.
Basin of attraction (corrected): $\lambda(0)>-\sqrt{\sigma_{\mathrm{eff}}/\alpha}$.

### Code

Numerical proxy for the source term $R:=\dot H+2H^2$ on the horizontal sector (RG_COARSE/05_Simulations_Numerics/PRO12_CODE_Colab_Hessian_Flow.py):

  pbh_source_quadratic_form(action_fn, x, proj, dt, n_samples=32, seed=0)
      # H(v) := proj( hvp(action_fn, x, proj(v)) )
      # x_next = flow_step_coords(x, action_fn, dt)   # explicit Euler on x' = -grad S
      # dH.v  ≈ ( H(v, x_next) - H(v, x) ) / dt
      # R.v   = dH.v + 2*H(H(v,x), x)
      # returns (min, mean, max) of v^T R v over random horizontal unit v
  commutator_norm_estimate(H_op, P_mask, n, n_iter=25)   # ||[H,P]|| by power iteration
  make_spatial_projector_links(lat, radius)              # local/nonlocal split for mixing tests

Caveat on this diagnostic: the flow used is coordinate gradient flow $x'=-\nabla S$, not the vHJ semigroup, so $\dot H$ along it is $-\nabla^3S\cdot\nabla S$, not $\Delta H-2H^2-2\nabla_{\nabla S}H$; positivity of the sampled $v^\top Rv$ is evidence about a proxy, not the PBH source.

**Caveat.** The theorem itself is correct and complete on a compact manifold with a smooth $\operatorname{Sym}(H)$-valued solution; the Yang–Mills application needs a stratified gauge quotient (reducible configurations are excluded and only conjectured polar), and (Curv), (Trace), (Anom) are unproved.

**Why it matters.** This is the hinge of the entire Riccati programme: it is the only place where a genuine PDE statement is converted into the scalar ODE that everything else assumes, and unlike most of the corpus it is proved carefully and correctly.

---

## 10. Scalar Riccati gap ODE: fixed points, stability, explicit solutions, comparison bounds, and the blow-down threshold

`status: solid` · `kind: theorem`

### Statement

Consider $\dot\lambda=-c\lambda^2+\sigma(t)$ with $c>0$ (the corpus uses $c=2$ from the vHJ $-2H^2$ term, and $c=1$ in one variant).

(1) [Constant source] For $\sigma(t)\equiv\sigma>0$ the fixed points are $\lambda_\pm=\pm\sqrt{\sigma/c}$; $\lambda_+$ is stable and $\lambda_-$ unstable, with linearisation $\dot\epsilon=-2c\lambda_\pm\epsilon$, i.e. decay rate $\gamma=2\sqrt{c\sigma}$ at $\lambda_+$ ($=2\sqrt{2\sigma}$ for $c=2$).

(2) [Threshold / basin of attraction — the crucial caveat] For every $\lambda_0>\lambda_-=-\sqrt{\sigma/c}$ the solution exists globally and $\lambda(t)\to\lambda_+$. For $\lambda_0<\lambda_-$ the solution blows down to $-\infty$ in the finite time $t_{\mathrm{blow}}=\frac{1}{2c\lambda_+}\log\Bigl|\frac{\lambda_0-\lambda_+}{\lambda_0+\lambda_+}\Bigr|$.

(3) [Explicit solutions] With $a:=\sqrt{\sigma/c}$ and $\gamma:=2\sqrt{c\sigma}=2ca$,
$$\lambda(t)=a\,\frac{(\lambda_0+a)+(\lambda_0-a)e^{-\gamma t}}{(\lambda_0+a)-(\lambda_0-a)e^{-\gamma t}}\;=\;a\tanh\!\Bigl(\tfrac{\gamma}{2}t+\operatorname{artanh}\tfrac{\lambda_0}{a}\Bigr)\ \ (|\lambda_0|<a),$$
and in particular $\lambda(0)=0\Rightarrow\lambda(t)=\sqrt{\sigma/c}\,\tanh(\sqrt{c\sigma}\,t)$; for $c=2$, $\lambda(t)=\sqrt{\sigma/2}\tanh(\sqrt{2\sigma}\,t)$. Convergence is exponential: $|\lambda(t)-\lambda_+|\le Ce^{-\gamma t}$.

(4) [Zero source] $\sigma\equiv0$ gives $\lambda(t)=\lambda_0/(1+c\lambda_0t)\to0$ algebraically: **no source ⇒ no gap**.

(5) [Time-dependent source, comparison] If $0<\sigma_{\min}\le\sigma(t)\le\sigma_{\max}<\infty$ then for admissible initial data
$$\sqrt{\sigma_{\min}/c}\;\le\;\liminf_{t\to\infty}\lambda(t)\;\le\;\limsup_{t\to\infty}\lambda(t)\;\le\;\sqrt{\sigma_{\max}/c}.$$

(6) [Global existence] If $\sigma(t)\ge\sigma_{\min}>0$ and $\lambda_0>-\sqrt{\sigma_{\min}/c}$ the solution exists for all $t\ge0$: while $\lambda\ge0$, $\dot\lambda\le\sigma_{\max}$ bounds it above; while $\lambda\in(-\sqrt{\sigma_{\min}/c},0)$, $\dot\lambda>0$.

### Derivation

PROOF OF (1). $-c\lambda^2+\sigma=0\iff\lambda=\pm\sqrt{\sigma/c}$. $f(\lambda)=-c\lambda^2+\sigma$ has $f'(\lambda)=-2c\lambda$, so $f'(\lambda_+)=-2c\sqrt{\sigma/c}=-2\sqrt{c\sigma}<0$ (stable) and $f'(\lambda_-)=+2\sqrt{c\sigma}>0$ (unstable).

PROOF OF (2)–(3) [separation of variables, full]. Write $\dot\lambda=-c(\lambda^2-a^2)=c(a-\lambda)(a+\lambda)$. Then $\frac{d\lambda}{(a-\lambda)(a+\lambda)}=c\,dt$ and, by partial fractions $\frac{1}{(a-\lambda)(a+\lambda)}=\frac{1}{2a}\bigl(\frac{1}{a-\lambda}+\frac{1}{a+\lambda}\bigr)$,
$$\frac{1}{2a}\log\Bigl|\frac{a+\lambda}{a-\lambda}\Bigr|=ct+C\;\Longrightarrow\;\frac{a+\lambda}{a-\lambda}=A\,e^{2act}=A\,e^{\gamma t},\qquad A=\frac{a+\lambda_0}{a-\lambda_0}.$$
Solving for $\lambda$: $\lambda=a\frac{Ae^{\gamma t}-1}{Ae^{\gamma t}+1}$; multiplying numerator and denominator by $(a-\lambda_0)e^{-\gamma t}$ gives the stated rational form. Writing $\lambda=a\tanh\theta$ turns the ODE into $\dot\theta=\sqrt{c\sigma}$ (check: $\dot\lambda=a\dot\theta\operatorname{sech}^2\theta$ and $-c\lambda^2+\sigma=\sigma(1-\tanh^2\theta)=\sigma\operatorname{sech}^2\theta$, so $\dot\theta=\sigma/a=\sqrt{c\sigma}$), giving the tanh form.
For $\lambda_0<-a$: $\lambda^2>a^2$ so $\dot\lambda<0$ and $\lambda$ decreases; the same primitive gives the escape time $\int_{-\infty}^{\lambda_0}\frac{d\lambda}{c(\lambda^2-a^2)}=\frac{1}{2ca}\log\Bigl|\frac{\lambda_0-a}{\lambda_0+a}\Bigr|$, finite. Hence finite-time blow-down.

PROOF OF (4). $\dot\lambda=-c\lambda^2$ separates to $-d(1/\lambda)=-c\,dt$... precisely $\frac{d}{dt}\lambda^{-1}=c$, so $1/\lambda(t)=1/\lambda_0+ct$, $\lambda(t)=\lambda_0/(1+c\lambda_0t)$.

PROOF OF (5). Let $\underline\lambda,\overline\lambda$ solve the autonomous equations with $\sigma_{\min},\sigma_{\max}$ and the same initial data. Since $\sigma_{\min}\le\sigma(t)\le\sigma_{\max}$, standard scalar ODE comparison (the vector field is monotone in $\sigma$ and locally Lipschitz in $\lambda$) gives $\underline\lambda\le\lambda\le\overline\lambda$ for all $t$; then apply (1)/(3) to each.

NUMERICAL VERIFICATION [reproduced by me exactly, RK4, $c=2$]. Case A, $\sigma=1$ ($\lambda_*=\sqrt{1/2}=0.707106781187$), RK4 on $[0,10]$ with 20 000 steps:
  $\lambda_0=-1.0$: blows down (numerically near $t=0.624$); analytic $t_{\mathrm{blow}}=\frac{1}{4a}\log\bigl|\frac{\lambda_0-a}{\lambda_0+a}\bigr|=0.6232252401$
  $\lambda_0=-0.8$: blows down near $t=0.986$
  $\lambda_0=-0.7$: $\lambda(10)=0.707106781041$
  $\lambda_0=-0.5$: $0.707106781182$;  $\lambda_0=0$: $0.707106781186$;  $\lambda_0=1$: $0.707106781187$;  $\lambda_0=2$: $0.707106781187$.
Case B, $\sigma(t)=1+\tfrac12\sin t$ ($\sigma_{\min}=0.5$, $\sigma_{\max}=1.5$), RK4 on $[0,20]$, 40 000 steps, $\lambda(0)=0$ — reproduced to 8 decimals:
  $t=0$: $\lambda=0$, $\sigma=1$, $\dot\lambda=1$
  $t=2$: $\lambda=0.85630298$, $\sigma=1.45464871$, $\dot\lambda=-0.01186088$
  $t=5$: $\lambda=0.52181601$, $\sigma=0.52053786$, $\dot\lambda=-0.02404604$
  $t=10$: $\lambda=0.66664947$, $\sigma=0.72798944$, $\dot\lambda=-0.16085359$
  $t=20$: $\lambda=0.82263764$, $\sigma=1.45647263$, $\dot\lambda=0.10300727$
Late window $t\in[50,100]$: $\lambda\in[0.5203,0.8598]$, inside the comparison band $[\sqrt{0.5/2},\sqrt{1.5/2}]=[0.5000,0.8660]$. ✓

WORKED YANG–MILLS EXAMPLE (recomputed exactly by me). Take $\sigma_*=\sigma_{\mathrm{anom}}=4.64\times10^{-2}$ (SU(2), $\beta=2.0$, $4^4$ lattice, 50 configurations) and $\lambda(0)=0.01$ (a deliberately tiny seed, modelling the vanishing Haar term). Then $c=2$, $\lambda_*=\sqrt{\sigma_*/2}=0.152315$, $\gamma=2\sqrt{2\sigma_*}=0.609262$, $t_{99\%}=\log100/\gamma=7.559$, and $\lambda(t)=\lambda_*\tanh(\sqrt{2\sigma_*}\,t+\operatorname{artanh}(0.01/\lambda_*))$:
  $t=0$: 0.010000 (6.6% of $\lambda_*$);  $t=1$: 0.053969 (35.4%);  $t=2$: 0.089602 (58.8%);  $t=5$: 0.140127 (92.0%);  $t=7.6$: 0.149733 (98.3%);  $t=10$: 0.151713 (99.6%);  $t=20$: 0.152314 (100.0%).
(The corresponding table in the corpus reads 0.082 at $t=2$ and 0.137 at $t=5$; the exact values are 0.0896 and 0.1401.)

INTERNAL INCONSISTENCY IN THE CORPUS, RESOLVED. Riccati_Equation_Analysis_Proof.md Theorem 6.1 asserts convergence 'regardless of initial UV value $\lambda_0$ (even if $\lambda_0<0$)' and tabulates $\lambda_0=-1.0\Rightarrow\lambda(10)=0.706$ for $\sigma=1$. That row is wrong: $\lambda_-=-0.7071$, so $\lambda_0=-1$ blows down at $t=0.6232$ (verified numerically and analytically above). The same file's own §8 summary states the correct hypothesis ('as long as $\lambda_0>-\sqrt{\sigma_{\min}/2}$'), as does SIM_Riccati_ODE_Verification.md. Use the restricted form.

### Constants and numbers

$c=2$ (vHJ normalisation): $\lambda_*=\sqrt{\sigma/2}$, $\gamma=2\sqrt{2\sigma}$, zero-data solution $\sqrt{\sigma/2}\tanh(\sqrt{2\sigma}t)$.
$c=1$ variant: $\lambda_*=\sqrt\kappa$, $\gamma=2\sqrt\kappa$, zero-data solution $\sqrt\kappa\tanh(\sqrt\kappa t)$.
$\sigma=1$, $c=2$: $\lambda_*=0.707106781187$; blow-down times $t_{\mathrm{blow}}(\lambda_0=-1)=0.6232252401$, $t_{\mathrm{blow}}(\lambda_0=-0.8)\approx0.986$.
Oscillatory $\sigma=1+0.5\sin t$: late-time range $[0.5203,0.8598]$ vs comparison band $[0.5000,0.8660]$.
SU(2) worked example: $\sigma_*=4.64\times10^{-2}$ ⇒ $\lambda_*=0.152315$, $\gamma=0.609262$, $t_{99\%}=7.559$.
SU(3) order-of-magnitude estimate quoted in the corpus (one-loop $b_0\approx(11/3)g^2/(16\pi^2)$): $m\gtrsim0.13\,g$.
Measured SU(2) $\sigma_{\mathrm{anom}}$ ($4^4$, 50 configs, $\kappa=-1$, $\beta_0=22/3$): $6.17,4.64,3.72,3.10,2.32\times10^{-2}$ at $\beta=1.5,2.0,2.5,3.0,4.0$ ⇒ $\lambda_*=\sqrt{\sigma/2}=0.176,0.152,0.136,0.124,0.108$.

### Code

Copy-paste runnable RK4 verification (pure Python, no dependencies), from RICCATI/01_riccati_flow/SIM_Riccati_ODE_Verification.md:

    import math
    def rk4(f, t0, y0, t1, n):
        h=(t1-t0)/n; t,y=t0,y0; ts,ys=[t0],[y0]
        for _ in range(n):
            k1=f(t,y); k2=f(t+h/2,y+h*k1/2); k3=f(t+h/2,y+h*k2/2); k4=f(t+h,y+h*k3)
            y+= (h/6)*(k1+2*k2+2*k3+k4); t+=h; ts.append(t); ys.append(y)
        return ts, ys
    riccati_const = lambda sig: (lambda t,l: -2.0*l*l + sig)
    riccati_osc   = lambda: (lambda t,l: -2.0*l*l + (1.0 + 0.5*math.sin(t)))
    # Experiment A: sigma = 1.0, lam0 in [-1,-0.8,-0.7,-0.5,0,1,2], t in [0,10], n = 20000
    # Experiment B: sigma(t) = 1 + 0.5 sin t, lam0 = 0, t in [0,20], n = 40000

Analytic blow-down time (mine):
    a = math.sqrt(sigma/2)
    t_blow = (1/(4*a))*math.log(abs((lam0-a)/(lam0+a)))   # valid for lam0 < -a

**Caveat.** The only genuine subtlety is the basin of attraction: the mechanism fails for initial curvature below $-\sqrt{\sigma/c}$. In the intended application the initial gap is positive, so the caveat is benign there — but it must be carried, because two corpus documents state the result without it.

**Why it matters.** This is the 'mechanism theorem' the whole programme reduces to: once a positive source $\sigma_*$ is available, a strictly positive infrared curvature scale is forced, exponentially fast, and independently of the UV seed — which is exactly what is needed once the Haar spark is known to vanish as $a\to0$.

---

## 11. The Riccati envelope as an exact spectral semigroup, and why it cannot restore convexity

`status: solid` · `kind: theorem`

### Statement

For $\eta\ge0$ and symmetric $H\succeq0$ define the *Riccati envelope*
$$\Phi_\eta(H):=H(I+\eta H)^{-1}\;=\;(H^{-1}+\eta I)^{-1}\ \ (\text{if }H\succ0).$$

(1) [Spectral action] If $H=U\operatorname{diag}(\lambda_i)U^\top$ then $\Phi_\eta(H)=U\operatorname{diag}(\phi_\eta(\lambda_i))U^\top$ with $\phi_\eta(\lambda)=\lambda/(1+\eta\lambda)$; eigenvectors are unchanged.
(2) [Exact semigroup] $\Phi_\tau\circ\Phi_\eta=\Phi_{\eta+\tau}$ for all $\eta,\tau\ge0$; hence $\Phi_\eta^{\,n}=\Phi_{n\eta}$ and $\lambda_i^{(n)}=\lambda_i/(1+n\eta\lambda_i)$.
(3) [ODE] $H(t):=\Phi_t(H_0)$ solves $\dot H=-H^2$ in functional calculus; eigenvalues obey $\dot\lambda=-\lambda^2$.
(4) [Unconditional curvature cap] $0\preceq\Phi_\eta(H)\preceq\eta^{-1}I$ for every $H\succeq0$, independent of dimension. Consequently, for any linear coarse-graining map $J$, the composite RG step $\mathcal R(H):=\Phi_\eta(JHJ^\top)$ satisfies $0\preceq\mathcal R(H)\preceq\eta^{-1}I_M$ unconditionally.
(5) [Conditional lower bound on a physical subspace] If $P$ is an orthogonal projector and $H\succeq mP$ with $m>0$, then $\Phi_\eta(H)\succeq\frac{m}{1+\eta m}P$. If in addition $JP_{\mathrm{fine}}J^\top\succeq s^2P_{\mathrm{coarse}}$ for some $s>0$ and $H\succeq mP_{\mathrm{fine}}$, then $\mathcal R(H)\succeq\frac{ms^2}{1+\eta ms^2}P_{\mathrm{coarse}}$.
(6) [Obstruction — mine] $\phi_\eta(\lambda)\le\lambda$ for all $\lambda\ge0$, so $\Phi_\eta(H)\preceq H$ and $\lambda_{\min}(\Phi_\eta(H))\le\lambda_{\min}(H)$. The envelope therefore **never increases the spectral floor**: it restores boundedness, not convexity. The name 'Riccati convexity restoration' is a misnomer; the only genuine restoration mechanism is a positive source in the Riccati ODE (previous item).

### Derivation

PROOF OF (1). $H$ commutes with $I+\eta H$; apply the spectral theorem.
PROOF OF (2). On eigenvalues,
$$\phi_\tau(\phi_\eta(\lambda))=\frac{\lambda/(1+\eta\lambda)}{1+\tau\lambda/(1+\eta\lambda)}=\frac{\lambda}{(1+\eta\lambda)+\tau\lambda}=\frac{\lambda}{1+(\eta+\tau)\lambda}=\phi_{\eta+\tau}(\lambda).$$
Diagonalise. $\square$
PROOF OF (3). $\lambda(t)=\lambda_0/(1+t\lambda_0)$ gives $\dot\lambda=-\lambda_0^2/(1+t\lambda_0)^2=-\lambda(t)^2$.
PROOF OF (4). $0\le\lambda/(1+\eta\lambda)\le1/\eta$ for all $\lambda\ge0$ (the map is increasing with supremum $1/\eta$); apply in the diagonal basis of $JHJ^\top\succeq0$.
PROOF OF (5). $\phi_\eta$ is increasing on $[0,\infty)$; $H\succeq mP$ means every eigenvalue of $H$ restricted to $\operatorname{im}P$ is $\ge m$, hence maps to $\ge m/(1+\eta m)$. For the composite, $H\succeq mP_{\mathrm{fine}}\Rightarrow JHJ^\top\succeq mJP_{\mathrm{fine}}J^\top\succeq ms^2P_{\mathrm{coarse}}$; apply the previous sentence. $\square$
PROOF OF (6). $\lambda-\phi_\eta(\lambda)=\eta\lambda^2/(1+\eta\lambda)\ge0$.

EXACT MATCH TO THE RECORDED HOTRG NUMERICS [verified by me]. The corpus records a HOTRG pushforward $H\mapsto JHJ^\top$ (with $J$ the finite-difference Jacobian of a vertical HOTRG merge about $T=\mathbf1$, $D=4$, $\chi=4$, $\varepsilon=10^{-6}$) producing a coarse Hessian with $\lambda_{\min}\approx-6\times10^{-11}$ and $\lambda_{\max}\approx2.654\times10^5$, followed by iterated Riccati steps at $\eta=0.1$. The recorded trajectory is $\lambda_{\max}=9.999623,\;5,\;3.333291,\;2.5,\;2,\;1.666,\;1.428564$. By (2), $\lambda^{(n)}=\lambda_0/(1+n\eta\lambda_0)$ with $\lambda_0=2.654\times10^5$, $\eta=0.1$; computing gives
  $n=1$: 9.999623;  $n=2$: 4.999906;  $n=3$: 3.333291;  $n=4$: 2.499976;  $n=5$: 1.999985;  $n=6$: 1.666656;  $n=7$: 1.428564.
This reproduces every recorded digit. Asymptotically $\lambda^{(n)}\approx1/(n\eta)=10/n$ for $\eta\lambda_0\gg1$: the cap is reached in one step and then decays as $1/n$.

WHAT THE NUMERICS ACTUALLY DEMONSTRATE [mine]. Combining (4) and (6): the observed 'curvature control' is entirely explained by the unconditional cap, and the observed fact that $\lambda_{\min}$ 'stays near numerical zero' at every layer is (6) in action — the envelope cannot lift a near-zero mode. So the HOTRG+Riccati loop demonstrates that a coarse-graining map which amplifies curvature by $10^5$ can be re-normalised, and demonstrates nothing at all about restoring a curvature *floor*, which is the quantity the mass-gap programme needs.

HONEST-MAPPING CORRECTION RECORDED IN THE CORPUS. The pipeline pushes forward the *stiffness* $H\mapsto CHC^\top$, which is not the Gaussian integration rule. For a Gaussian fine measure $\propto e^{-\frac12y^\top H_{\mathrm{phys}}y}$ the correct pushforward is on the *covariance*: $\Sigma_{\mathrm{coarse}}=C\Sigma_{\mathrm{phys}}C^\top=CH_{\mathrm{phys}}^{+}C^\top$, and the Gaussian-consistent coarse stiffness is $H^{\mathrm{coarse}}_{\mathrm{gauss}}=(CH_{\mathrm{phys}}^{+}C^\top)^{+}$. This is exactly what removes the spurious $10^5$ curvature blow-up: pushing stiffness forward through a contracting map inflates eigenvalues, pushing covariance forward does not. Here $C=JL_{\mathrm{phys}}=JLQ$ with $Q$ an orthonormal basis of $\operatorname{im}P$, $P=I-G(G^\top G)^{-1}G^\top$ the horizontal projector and $L=\partial\operatorname{vec}T(x)/\partial x|_{x_\star}$ the (missing) tensor-construction Jacobian.

### Constants and numbers

$\eta=0.1$ ⇒ unconditional cap $1/\eta=10$.
HOTRG pushforward before damping: $\lambda_{\min}\approx-6\times10^{-11}$, $\lambda_{\max}\approx2.654\times10^5$ ($D=4$, $\chi=4$, finite-difference $\varepsilon=10^{-6}$, background $T=\mathbf1$).
Envelope trajectory $\lambda^{(n)}=\lambda_0/(1+n\eta\lambda_0)$, $n=1..7$: 9.999623, 4.999906, 3.333291, 2.499976, 1.999985, 1.666656, 1.428564 (matches the corpus's recorded log exactly).
Multi-layer loop: before damping $\lambda_{\max}\sim10^{5}$–$10^{5.5}$ at every layer; after damping $\lambda_{\max}\approx10$ at every layer; $\lambda_{\min}$ remains at numerical zero throughout.

### Code

Envelope and HOTRG Jacobian (RICCATI/01_riccati_flow/hotrg_riccati_curvature_rg.md; envelope theory in riccati_envelope_semigroup.md):

    def riccati_step(H, eta=0.1):
        w, v = np.linalg.eigh(H)
        Hn = (v * (w/(1 + eta*w))) @ v.T
        return 0.5*(Hn + Hn.T)

    def hotrg_merge_vertical(T1, T2, chi):      # jax; SVD-truncated vertical merge
        M = jnp.tensordot(T1, T2, axes=((1,), (1,)))
        l1,r1,d1,l2,r2,d2 = M.shape
        U,S,Vh = jnp.linalg.svd(M.reshape(l1*l2, r1*r2*d1*d2), full_matrices=False)
        T = (U[:,:chi] @ jnp.diag(jnp.sqrt(S[:chi]))).reshape(l1,l2,chi)
        N = (jnp.diag(jnp.sqrt(S[:chi])) @ Vh[:chi,:]).reshape(chi,r1,r2,d1,d2)
        return jnp.einsum('abc,cdefg->acde', T, N)

    def hotrg_jacobian_tensor(D=4, chi=4, eps=1e-6):   # finite-difference J about T = ones
        ...  # column i = (merge(T + eps*e_i) - merge(T)) / eps

Gaussian-consistent replacement for the stiffness pushforward (RICCATI/03_stability/honest_hotrg_mapping.md):

    def coarse_hessian_gaussian(H_phys, C, tol=1e-12):
        # H_gauss = ( C H_phys^+ C^T )^+     -- pushes forward the covariance, not the stiffness

Verification of the semigroup against the recorded log (mine):
    eta, lam0 = 0.1, 2.654e5
    [lam0/(1+n*eta*lam0) for n in range(1,8)]
    # -> 9.999623, 4.999906, 3.333291, 2.499976, 1.999985, 1.666656, 1.428564

**Caveat.** The whole item is exact finite-dimensional linear algebra. Its only physical content is negative: (6) shows the envelope can never raise a curvature floor, so this cannot be the convexity-restoration mechanism the programme needs.

**Why it matters.** It gives a complete, exact account of the corpus's most eye-catching numerics (a $10^5$-fold curvature blow-up 'cured' in one step), shows the numbers are the scalar map $\lambda\mapsto\lambda/(1+n\eta\lambda)$ and nothing more, and identifies precisely why the effect is not evidence for the mass-gap mechanism.

---

## 12. Obstruction bundle: four independent reasons this class of RG cannot reach the continuum

`status: solid` · `kind: obstruction`

### Statement

Four distinct, individually correct obstruction arguments. Together they are the strongest mathematics in the coarse-graining part of the corpus.

(O1) [Heat-flow RG destroys convexity — no source, no gap] For $S_0(x)=\tfrac12x^\top H_0x$, $H_0\succ0$, and the heat-semigroup coarse-graining $e^{-S_t}=e^{t\nu\Delta}e^{-S_0}$, one has exactly $H_t^{-1}=H_0^{-1}+2\nu tI$, hence $\lambda_{\min}(H_t)>0$ for all $t$ but $\lambda_{\min}(H_t)\sim1/(2\nu t)\to0$. In flat space with pure heat-flow RG, bare convexity alone does **not** produce a permanent mass gap. More generally $\dot\lambda=-c\lambda^2$ (no source) gives algebraic collapse $\lambda\to0$; for abelian $G=U(1)$ the configuration space is flat, $\sigma=0$, and this is precisely the massless photon.

(O2) [Haar spark dies in the continuum] With $\rho_*(a)=c_0a^2g^2-\beta C_V(N)=\tfrac N6a^2g^2-\tfrac{48}{g^2}$, along an asymptotically free trajectory $a\to0$, $g(a)\to0$, $\beta(a)=2N/g(a)^2\to\infty$: the Haar term $\to0$ and the Wilson term $\to\infty$, so $\rho_*(a)\to-\infty$. The strong-coupling window $g^4>288/(Na^2)$ (equivalently $0<\beta<\beta_c(a)$) cannot contain the continuum $\beta(a)$; $\rho_*(a,\beta(a))$ must change sign before the continuum is reached.

(O3) [Decimation cannot contract] For a decimation block map, $C_{\mathrm{RG}}=1$ exactly and hence $r=L^2C_{\mathrm{RG}}=L^2\ge4>1$; the cascade coefficient is $L^{2n}$ and $C_P^{(0)}\le L^{2n}C_P^{(n)}+C_{\mathrm{block}}\frac{L^{2n}-1}{L^2-1}$ diverges. The only block map for which contraction is established, geodesic (Karcher) averaging with $C_{\mathrm{RG}}\le(1+O(r))/L^d$, is proved contractive **only** in the linearised small-field chart $\|X_b\|\le r\ll1$.

(O4) [Gauge-covariant Markov coarse-graining is impossible] Let $G$ be a nontrivial compact Lie group, $\Omega_a=G^{E(\Lambda_a)}$, $\Omega_{a'}=G^{E(\Lambda_{a'})}$, with gauge groups $\mathcal G_a=G^{V(\Lambda_a)}$, $\mathcal G_{a'}=G^{V(\Lambda_{a'})}$. There is **no** Markov kernel $\Pi:\Omega_a\to\Omega_{a'}$ satisfying both
  (A5) $\Pi$ is a conditional expectation onto a $\sigma$-algebra generated by *gauge-invariant* block variables — so $\Pi(g\cdot U)=\Pi(U)$ $\mu_a$-a.s. for all $g\in\mathcal G_a$; and
  (A4) $\Pi$ is gauge covariant for an induced coarse action whose image contains $\mathcal G_{a'}$ — so $\Pi(g\cdot U)=g'\cdot\Pi(U)$.

(O5) [Fixed-cutoff OS data cannot force cross-scale permanence] Fixed-cutoff OS reflection positivity plus a spectral gap at every $a$ carries no information forcing the existence (or uniqueness) of an equivariant cross-scale map $\Pi_{a\to a'}$ with $(\Pi_{a\to a'})_\#\mu_a=\mu_{a'}$: one can construct OS-preserving 'UV twists' that leave each $(\mathcal H_a,H_a)$ unitarily equivalent (hence preserve every fixed-cutoff gap) while destroying any candidate $\Pi$ commuting with reflection and time translation.

### Derivation

PROOF OF (O1). See the vHJ item: convolution of Gaussians adds covariances, $\Sigma_t=\Sigma_0+2\nu tI$, so $H_t=(H_0^{-1}+2\nu tI)^{-1}$ and $\lambda_i(t)=\lambda_i(0)/(1+2\nu t\lambda_i(0))\to0$ like $1/(2\nu t)$. There is no free parameter to fix this: it is an identity. Hence any curvature-based gap mechanism operating through heat-flow-like coarse-graining *must* supply a strictly positive source term.

PROOF OF (O2). See the constants item. Explicitly, along $a\to0$ the two terms of $\rho_*$ move in opposite directions with no cancellation, and the windows require $g\gtrsim a^{-1/2}\to\infty$, i.e. they recede from asymptotic freedom.

PROOF OF (O3). For decimation $Pf$ depends on a subset of coordinates and $\nabla'(Pf)$ is a coordinate projection; Jensen gives $|\nabla'Pf|^2\le\mathbb E[|\nabla f|^2\mid V]$ with equality for functions of the selected coordinates alone, so $C_{\mathrm{RG}}=1$ is attained. Then $r=L^2>1$ and the closed form of the cascade with $r>1$ gives $\rho_n=r^n\to\infty$, $\kappa_n=(r^n-1)/(r-1)\to\infty$.

PROOF OF (O4). Combining (A5) and (A4): for every $g'$ in the image of the induced action, and in particular for every $g'\in\mathcal G_{a'}$,
$$g'\cdot\Pi(U)=\Pi(g\cdot U)=\Pi(U)\qquad\mu_a\text{-a.s.}$$
So $\Pi(U)$ lies in the fixed-point set of the $\mathcal G_{a'}$-action on $\Omega_{a'}=G^{E(\Lambda_{a'})}$. But that fixed-point set is empty for nontrivial $G$: a configuration $(V_{xy})$ is fixed iff $g_xV_{xy}g_y^{-1}=V_{xy}$ for all $g\in G^{V}$; taking $g_y=e$ and $g_x$ arbitrary forces $g_xV_{xy}=V_{xy}$, i.e. $g_x=e$ for all $g_x\in G$ — impossible unless $G$ is trivial (assuming at least one edge). Contradiction. $\square$

ESCAPE HATCHES FOR (O4) (the design space the no-go dictates): (i) drop Markovness — use a *deterministic* blocking map $P:\Omega_a\to\Omega_{a'}$ and pushforward; reflection-positivity permanence needs only a map, not a kernel; (ii) change the coarse variable so it lives in a quotient or on a coarser bundle rather than in $G^{E(\Lambda_{a'})}$ with endpoint gauge action; (iii) gauge-fix before coarse-graining, eliminating the endpoint redundancy; (iv) weaken (A4) to covariance under a restricted subgroup or on a subalgebra only.

PROOF SKETCH OF (O5) (as recorded). The mechanism is an explicit family of OS-preserving UV twists: they leave the reconstructed $(\mathcal H_a,H_a)$ unitarily equivalent for each $a$ (hence every intrascale gap is preserved) while destroying the equivariance any candidate $\Pi_{a\to a'}$ would need. The conclusion is a clean separation: *intrascale* (fixed-cutoff clustering ⇒ fixed-cutoff gap) is a theorem, while *interscale* (cutoff removal) requires extra architecture — a renormalisation trajectory / projective system / coarse-graining scheme — as an additional hypothesis, not a consequence of the OS axioms at each scale.

RELATED QUANTITATIVE FACT (the $O(g^2)$ energy-loss estimate). For a symmetric Dirichlet form $\mathcal E$ and $P=\mathbb E[\cdot\mid\mathcal F_{\mathrm{coarse}}]$, write $f=\bar f+\xi$, $\bar f=Pf$, $P\xi=0$. Markov/Jensen contraction gives $\mathcal E(Pf,Pf)\le\mathcal E(f,f)$ and $0\le\mathcal E(f,f)-\mathcal E(Pf,Pf)\le\mathcal E(\xi,\xi)$ — with *no* linear-in-fluctuation term, precisely because $P\xi=0$ centres the fine component. If in addition a conditional blockwise Poincaré inequality (BP) holds with constant $g(a)^2/\lambda_{\mathrm{block}}$ (heuristically because the fine generator carries $1/g(a)^2$, so its conditional gap is $\asymp1/g(a)^2$), summing blockwise gives $\mathcal E(\xi,\xi)\le Cg(a)^2\mathcal E(\bar f,\bar f)$ and hence $\mathcal E(f,f)-\mathcal E(Pf,Pf)=O(g(a)^2)\mathcal E(\bar f,\bar f)$. This is the *positive* counterpart to (O3): energy loss under conditioning is controllably small at weak coupling, but (O4) says the conditioning cannot simultaneously be gauge-covariant.

LOCALITY STRESS TEST (numerical corroboration recorded in the corpus). Local (Laplacian-type) terms show smallest eigenvalues decreasing with $L$ as expected; nonlocal/mean-field modifications pin eigenvalues, distort the infrared structure, and can *reduce* the low-energy gap while raising overall energies. Any coarse-graining that accidentally introduces nonlocality therefore sabotages the very gap mechanism it is meant to preserve.

### Constants and numbers

(O1) $\lambda_{\min}(H_t)=\lambda_{\min}(H_0)/(1+2\nu t\lambda_{\min}(H_0))\sim1/(2\nu t)$; measured per-step decay in the 4D runs $\alpha\approx1.0028\times10^{-3}$ (= $2\nu\,dt$ with $\nu\,dt\approx5.014\times10^{-4}$).
(O2) $\rho_*(a)=\tfrac N6a^2g^2-48/g^2$; windows $g^4>288/(Na^2)$ and $g^4>576/(Na^2)$ require $g\gtrsim a^{-1/2}$.
(O3) decimation $C_{\mathrm{RG}}=1$, $r=L^2=4$, cascade coefficient $4^n$; contraction needs $C_{\mathrm{RG}}<L^{-2}=1/4$, available only via averaging with $C_{\mathrm{RG}}\le1/16$ in the small-field chart.
(O4) fixed-point set of the coarse gauge action on $G^{E}$ is empty for any nontrivial $G$ and any lattice with at least one edge.
Energy-loss estimate: $\mathcal E(f,f)-\mathcal E(Pf,Pf)=O(g(a)^2)\mathcal E(Pf,Pf)$ under (BP) with conditional block gap $\asymp1/g(a)^2$.

**Caveat.** (O5) is a sketch: the OS-preserving UV twists are described mechanistically but not constructed explicitly in the corpus. (O1)–(O4) are complete arguments.

**Why it matters.** These are the results that actually settle the question the corpus set out to answer, and each is reusable outside it: (O1) says curvature-based RG needs a source, (O2) that the Haar mechanism is finite-cutoff only, (O3) that contraction is a property of the block map and fails for the unconditional one, (O4) that gauge covariance and Markov coarse-graining are algebraically incompatible on nontrivial compact groups, and (O5) that cutoff removal is an extra hypothesis, not a corollary of the OS axioms.

---

## How these fit together

All twelve items are instances of two pieces of machinery, applied in the two directions an RG can be read.\n\n(1) THE AFFINE FIXED-POINT MACHINE. The one-step Poincaré recursion (item 1) and the MFIP curvature recursion (item 5C) are the same object: $X\\mapsto rX+b$ with $|r|<1$, whose closed form is $r^nX_0+b(1-r^n)/(1-r)$ and whose fixed point is $b/(1-r)$ (item 2, formalised in Lean). Read as an upper bound on the Poincaré constant it gives $C_P^*=C_{\\mathrm{block}}/(1-r)$; read as a lower bound on the curvature modulus it gives $\\rho^*=(\\sigma_*-\\varepsilon_\\infty)/(1-K)$. Both stand or fall on a single number, the contraction factor, and item 12(O3) shows exactly when it fails.\n\n(2) THE RICCATI MACHINE. Marginalisation (item 3) subtracts a covariance from the averaged Hessian; heat-flow coarse-graining (item 8) subtracts $2H^2$ from the Hessian evolution; the discrete curvature recursion (item 5A) subtracts $M_k^2/\\rho_k$. All three are the same negative feedback, and all three drive curvature to zero unless a positive source is supplied. The horizontal tensor maximum principle (item 9) is the bridge that turns the matrix statement into the scalar ODE (item 10), whose stable fixed point $\\sqrt{\\sigma/c}$ is the only place a nonzero infrared curvature can come from.\n\nHOW THE TWO MACHINES MEET. Item 4 is the join: block marginalisation is *unconditionally* curvature-losing ($\\nabla^2S_{\\mathrm{eff}}\\preceq\\mathbb E[\\nabla^2_{xx}S]$, with deficit exactly the Fisher/covariance term). Therefore the only source of gain in the Poincaré cascade is the geometric factor $L^{-2}$ hidden inside $C_{\\mathrm{RG}}\\le L^{-d}$, and the only source of gain in the Riccati flow is the source $\\sigma_*$. This is why decimation ($C_{\\mathrm{RG}}=1$, no geometric gain) cannot contract, and why the sourceless vHJ flow decays like $1/(2\\nu t)$.\n\nCONSTANTS PROPAGATE COHERENTLY ACROSS ITEMS. The Haar Hessian $c_0=N/6$ (item 6) is simultaneously: the seed $\\rho_0$ in the curvature budget law (item 5B); the origin of $C_{\\mathrm{block}}\\le1/c_H$ quoted in the cascade (item 2); and the term whose $a^2g^2$ scaling produces obstruction (O2). The value $C_{\\mathrm{RG}}=1/16$ used in the Lean 'standard parameters' is exactly the $1/N=1/L^d$ computed for geodesic averaging in item 1 with $L=2$, $d=4$; $r=L^2C_{\\mathrm{RG}}=1/4$ therefore ties the Lean file, the markdown derivation, and the JAX test harness to one number. The Riccati coefficient $c=2$ used everywhere in items 9–10 is exactly the $-2H^2$ of the vHJ Hessian equation derived in item 8, whose Gaussian solution in turn explains the observed $\\alpha$-band.\n\nRELATION TO THE REST OF THE CORPUS. The conditional spectral floor lemma (item 7) is the technical hinge used across the Helffer–Sjöstrand, reflection-positivity and thermodynamic-limit folders to make every 'localise / average / restrict' step gap-preserving; item 4 states precisely where it may not be used. The Combes–Thomas / Helffer–Sjöstrand material supplies the covariance-decay inputs that would bound $M$ in the block-convexity engine. The Mosco-convergence folder is where the cascade's IR fixed point would be handed to the continuum, and obstruction (O5) is exactly the statement that this handoff needs its own hypothesis.

## Further material found but not fully extracted

Not extracted in full, but real and worth a later pass:\n\n1. RG_COARSE/01_Block_Convexity_Hinge/04_dirichlet_form_coarse_graining_Og2.md contains the full $O(g(a)^2)$ Dirichlet-energy-loss estimate under a conditional blockwise Poincaré hypothesis (BP), including the exact statement $0\\le\\mathcal E(f,f)-\\mathcal E(Pf,Pf)\\le\\mathcal E(\\xi,\\xi)$ with no linear term. It is the quantitative counterpart to hypothesis (A2) and deserves its own extraction.\n\n2. RICCATI/04_misc_docs/07_Horizontal_Tensor_Maximum_Principle.md §5 (which I only skimmed) gives the Yang–Mills translation of $\\sigma_0$ and $\\varepsilon_0$; and RICCATI/synthesis/model_creation/Synthesis_03_Renormalization_Riccati.md Chapters 6 and 9.5 contain the Anomaly–Curvature Identity $\\sigma_{\\mathrm{anom}}=\\kappa\\frac{\\beta(g)}{g}\\langle\\operatorname{Tr}F^2\\rangle$ and its numerical evaluation (gpu_gluon_condensate.py, SU(2), $4^4$, 50 configs; $\\sigma_{\\mathrm{anom}}=6.17,4.64,3.72,3.10,2.32\\times10^{-2}$ at $\\beta=1.5,2,2.5,3,4$ with $\\langle F^2\\rangle\\approx1.000$). Note the identity's sign depends on an undetermined constant $\\kappa$ (set to $-1$ by hand), so this is the weakest link in the 'hand-off' story and would repay a dedicated critical/extractive pass.\n\n3. RG_COARSE/06_Continuum_Mosco_Limits/ (04_mosco_convergence_curvature_lifting.md, SELECTED_04_Mosco_Curvature_Stability.md) is where the cascade's IR fixed point is supposed to be transferred to the continuum via Mosco convergence of Dirichlet forms; I did not read it. Its interface with obstruction (O5) is the natural next question.\n\n4. RG_COARSE/01_Block_Convexity_Hinge/05_projection_inversion_safety_lemma.md and 07_physical_projection_rg_compatible.md address the $U$-dependence of the horizontal projector $\\Pi_{\\mathrm{phys}}(U)$ — the single technical gap that blocks transferring every Euclidean Schur-complement result in item 3 to the lattice gauge setting.\n\n5. HESSIAN/vHJ_Riccati/PRO12_CODE_Colab_Hessian_Flow.py contains a covariant horizontal projector via a Faddeev–Popov conjugate-gradient solve and autodiff Hessian-vector products for the exact Haar Jacobian potential; it is the most substantial piece of working code in the corpus on this topic and would support an independent numerical check of $c_0=N/6$ and of the mixed-derivative Wilson bound $C_V(N)=24/N$.\n\n6. RG_COARSE/05_Simulations_Numerics/safe_scan_results_scaled.csv plus plot_convexity_scale005.py hold an executed convexity scan I did not open; and COLAB_RUNS/ contains 172 notebooks with stored outputs (01_su2_simulations/ and 02_tensor_network/gauge_theory_trg_colab.ipynb look most relevant to HOTRG curvature).\n\n7. A discrepancy left unresolved: the Haar-augmented vHJ runs give $\\alpha\\approx7.9\\times10^{-4}$ versus $1.0028\\times10^{-3}$ for the quadratic baseline, a ratio of $0.786$–$0.794$. If the added term were exactly quadratic and $\\nu\\,dt$ unchanged, the exact Gaussian identity forces identical $\\alpha$. The residual analysis (2–4$\\times10^{-3}$ versus $1$–$4\\times10^{-4}$) says the Haar runs are genuinely nonlinear, but the corpus does not record per-run $dt$, so a change of timestep cannot be excluded. Recording $dt$ per run and re-running would settle whether the '$\\alpha$-band' is physics or bookkeeping.
