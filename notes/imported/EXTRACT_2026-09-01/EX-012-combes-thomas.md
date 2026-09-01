---
id: EX-012
title: "Combes–Thomas / Davies exponential decay for the massive lattice Maxwell resolvent: exponents, row-sum and level-set constants, and numerical validation"
kind: extraction
items: 9
status_breakdown: {"solid": 9}
program: yang_mills
extracted_by: claude-opus-5 subagent, 2026-09-01
stance: preservation (content extraction, not refereeing)
source_files:
  - COMBES_THOMAS/COMBES_THOMAS_BOUNDS/Appendix_G__Combes_Thomas_Finite_Range_Inverse_Decay(1).md
  - MAXWELL/Decay_Estimates/Appendix_H__Davies_Type_Decay_Massive_Maxwell_Green_Kernel(1).md
  - COMBES_THOMAS/MAXWELL_GREEN/davies_decay_massive_maxwell.md
  - COMBES_THOMAS/MAXWELL_GREEN/02_davies_decay_maxwell_boundary_rowsum(1).md
  - COMBES_THOMAS/COMBES_THOMAS_BOUNDS/CURATED_02_CombesThomas_InverseDecay.md
  - COMBES_THOMAS/COMBES_THOMAS_BOUNDS/EXCITING_03_COMBES_THOMAS_MAXWELL_DECAY.md
  - COMBES_THOMAS/DUPLICATES/Appendix_A__Notation_and_Constants(1).md
  - ARCHIVES/extracted_notebooks/Untitled125_extracted.py
  - ARCHIVES/extracted_notebooks/Untitled122_extracted.py
  - COMBES_THOMAS/MAXWELL_GREEN/03_maxwell_C0_decay_and_kappa_plateau.md
  - COMBES_THOMAS/MAXWELL_GREEN/03_greens_decay_combes_thomas.md
  - COMBES_THOMAS/EVIDENCE_SIMULATIONS/gauge_fixing_hodge_laplacian_constants.md
  - SIMULATIONS/sanity_check_maxwell_decay.py
---

# Combes–Thomas / Davies exponential decay for the massive lattice Maxwell resolvent: exponents, row-sum and level-set constants, and numerical validation

> The abelian/linear core of the corpus is correct and reproducible: two rigorous conjugation theorems (Combes–Thomas, giving η ~ m²; Davies form-conjugation, giving η ~ m) for M = m²I + α d₁*d₁ on link 1-cochains, with a level-set row-sum refinement, exact combinatorial constants D_E = C₀(Δ₁) = 18 in d=4 (the corpus's FFT value 43.9077 is a reproducible symbol-convention artifact, corrected here), and an exact closed form for the lattice Maxwell Green kernel giving the sharp decay exponent κ = arcosh(1+m²/2α), against which all the bounds and the FFT κ-plateau numerics are calibrated.

**9 extracted items** — 9 solid

---

## 1. Theorem CT (Combes–Thomas exponential decay of inverse blocks for uniformly positive finite-range operators with finite-dimensional fibre)

`status: solid` · `kind: theorem`

### Statement

Let $(V,\mathrm{dist})$ be a finite (or countable, bounded-degree) set with an integer-valued graph metric. Let $\mathsf H_0$ be a finite-dimensional real Hilbert space (in the application $\mathsf H_0=\mathfrak g$, the Lie algebra) and put $\mathcal H=\ell^2(V;\mathsf H_0)$, with block representation $(Af)(x)=\sum_{y\in V}A_{xy}f(y)$, $A_{xy}\in\mathrm{End}(\mathsf H_0)$, and $\|\cdot\|_{\rm op}$ the operator norm both on $\mathrm{End}(\mathsf H_0)$ and on $\mathcal H$.

Let $A=A^{*}$ on $\mathcal H$ satisfy

(H1) **uniform positivity**: $A\succeq a_0 I$ with $a_0:=a_0(A)>0$;
(H2) **finite range**: there is an integer $R=R(A)\ge 1$ with $A_{xy}=0$ whenever $\mathrm{dist}(x,y)>R$;
(H3) **off-diagonal row-sum bound**: $B_0:=B_0(A)=\sup_{x\in V}\sum_{y\neq x}\|A_{xy}\|_{\rm op}<\infty$.

Then $A$ is invertible and **for all** $x,y\in V$
$$\boxed{\ \bigl\|(A^{-1})_{xy}\bigr\|_{\rm op}\ \le\ \frac{2}{a_0}\,\exp\bigl(-\eta_{\rm CT}(A)\,\mathrm{dist}(x,y)\bigr),\qquad \eta_{\rm CT}(A):=\frac1R\log\Bigl(1+\frac{a_0}{2B_0}\Bigr).\ }$$
If $B_0=0$ the bound holds with $\eta_{\rm CT}=+\infty$ (then $A$ is block-diagonal). All constants are independent of $|V|$, so the bound survives the thermodynamic limit whenever $a_0,R,B_0$ are volume-uniform.

Applied to the massive lattice Maxwell operator $M_\Lambda=m^2 I+\alpha\,d_1^{*}d_1$ on $\mathcal C^1(\Lambda;\mathfrak g)\cong\ell^2(E(\Lambda);\mathfrak g)$ with the *link graph* metric $\mathrm{dist}_E$ ($b\sim b'$ iff some plaquette boundary contains both), the hypotheses hold with $a_0=m^2$, $R=1$, $B_0\le\alpha\,C_0(\Delta_1)$, so
$$\bigl\|(M_\Lambda^{-1})_{bb'}\bigr\|_{\rm op}\le\frac{2}{m^2}\exp\Bigl(-\log\bigl(1+\tfrac{m^2}{2\alpha C_0(\Delta_1)}\bigr)\,\mathrm{dist}_E(b,b')\Bigr).$$

### Derivation

This is the fully rigorous version from `COMBES_THOMAS/COMBES_THOMAS_BOUNDS/Appendix_G__Combes_Thomas_Finite_Range_Inverse_Decay(1).md` (Lemma G.2.1 + Proposition G.3.1 + Proposition G.4.1). Six near-duplicate write-ups exist (CURATED_02, EXCITING_03, 03/05/06_combes_thomas_inverse_decay.md, Core_7); Appendix G is the only one that proves the block Schur step, and is the version reproduced here. I have checked every step.

**Lemma (block Schur test).** Let $K$ have blocks $K_{xy}\in\mathrm{End}(\mathsf H_0)$ with
$$\sup_x\sum_y\|K_{xy}\|_{\rm op}\le R_0,\qquad \sup_y\sum_x\|K_{xy}\|_{\rm op}\le C_0'.$$
Then $\|K\|_{\rm op}\le\sqrt{R_0C_0'}$; if in addition $K=K^{*}$ then $\|K\|_{\rm op}\le R_0$.

*Proof.* By Cauchy–Schwarz in $\mathsf H_0$, $|\langle g(x),K_{xy}f(y)\rangle|\le |g(x)|\,\|K_{xy}\|_{\rm op}\,|f(y)|$, so
$$|\langle g,Kf\rangle|\le\sum_{x,y}\|K_{xy}\|_{\rm op}|g(x)||f(y)|.$$
Apply $ab\le\frac12(a^2+b^2)$ with $a=|g(x)|\|K_{xy}\|^{1/2}$, $b=|f(y)|\|K_{xy}\|^{1/2}$:
$$|\langle g,Kf\rangle|\le\tfrac12\sum_x|g(x)|^2\!\sum_y\|K_{xy}\|+\tfrac12\sum_y|f(y)|^2\!\sum_x\|K_{xy}\|\le\tfrac12 R_0\|g\|^2+\tfrac12 C_0'\|f\|^2.$$
Replacing $g\mapsto\lambda g$ and optimising over $\lambda>0$ gives $|\langle g,Kf\rangle|\le\sqrt{R_0C_0'}\|g\|\|f\|$. If $K=K^{*}$ then $K_{xy}=K_{yx}^{*}$, hence $\|K_{xy}\|_{\rm op}=\|K_{yx}\|_{\rm op}$ and the column bound follows from the row bound with the same constant. $\square$

**Proof of the theorem.**

*Step 0 (weight).* Fix a base point $y_0\in V$ and set $\phi(x):=\mathrm{dist}(x,y_0)$. By the triangle inequality $\phi$ is 1-Lipschitz: $|\phi(x)-\phi(z)|\le\mathrm{dist}(x,z)$. For $t\ge0$ let $W_t$ be the diagonal multiplication operator $(W_tf)(x)=e^{t\phi(x)}f(x)$, $W_t^{-1}=W_{-t}$, and set $A_t:=W_tAW_t^{-1}$. Similarity gives $A^{-1}=W_t^{-1}A_t^{-1}W_t$.

*Step 1 (blocks of the conjugation).* For any $f$,
$$(A_tf)(x)=e^{t\phi(x)}\sum_z A_{xz}e^{-t\phi(z)}f(z)\ \Longrightarrow\ (A_t)_{xz}=e^{t(\phi(x)-\phi(z))}A_{xz}.$$
Put $K_t:=A_t-A$, so $(K_t)_{xz}=\bigl(e^{t(\phi(x)-\phi(z))}-1\bigr)A_{xz}$ and $(K_t)_{xx}=0$.

*Step 2 (row and column bounds).* If $A_{xz}\neq0$ then $\mathrm{dist}(x,z)\le R$ by (H2), hence $|\phi(x)-\phi(z)|\le R$. For $|u|\le R$ one has $|e^{tu}-1|\le\max\{e^{tR}-1,\,1-e^{-tR}\}=e^{tR}-1$. Therefore for $x\neq z$
$$\|(K_t)_{xz}\|_{\rm op}\le(e^{tR}-1)\|A_{xz}\|_{\rm op}.$$
Summing over $z\ne x$ and taking $\sup_x$ gives the row bound $(e^{tR}-1)B_0$. For the column bound use $A=A^{*}$: $\|A_{xz}\|_{\rm op}=\|A_{zx}\|_{\rm op}$, so $\sum_{x\ne z}\|A_{xz}\|_{\rm op}=\sum_{x\ne z}\|A_{zx}\|_{\rm op}\le B_0$. The block Schur lemma then gives
$$\|K_t\|_{\rm op}\le(e^{tR}-1)B_0.\qquad(\star)$$

*Step 3 (Neumann series).* (H1) gives $\|A^{-1}\|_{\rm op}\le a_0^{-1}$. Suppose $t\ge0$ is such that $\|K_t\|_{\rm op}\le a_0/2$. Then $\|K_tA^{-1}\|_{\rm op}\le\frac12$, and since $A+K_t=(I+K_tA^{-1})A$,
$$A_t^{-1}=A^{-1}(I+K_tA^{-1})^{-1},\qquad \|A_t^{-1}\|_{\rm op}\le\frac{1}{a_0}\cdot\frac{1}{1-\tfrac12}=\frac{2}{a_0}.$$
By $(\star)$ a sufficient condition is $(e^{tR}-1)B_0\le a_0/2$, i.e. exactly
$$t\le\frac1R\log\Bigl(1+\frac{a_0}{2B_0}\Bigr)=\eta_{\rm CT}(A).$$

*Step 4 (extract the kernel bound).* From $A^{-1}=W_t^{-1}A_t^{-1}W_t$ at block level, $(A^{-1})_{xz}=e^{-t\phi(x)}(A_t^{-1})_{xz}e^{t\phi(z)}$. Take $z=y_0$, where $\phi(y_0)=0$:
$$\|(A^{-1})_{xy_0}\|_{\rm op}=e^{-t\,\mathrm{dist}(x,y_0)}\|(A_t^{-1})_{xy_0}\|_{\rm op}\le e^{-t\,\mathrm{dist}(x,y_0)}\|A_t^{-1}\|_{\rm op}\le\frac{2}{a_0}e^{-t\,\mathrm{dist}(x,y_0)},$$
using $\|T_{xz}\|_{\rm op}\le\|T\|_{\rm op}$ for any block of any operator. Choose $t=\eta_{\rm CT}(A)$. Since $y_0$ was arbitrary the bound holds for every pair. $\blacksquare$

**Verification of the hypotheses for $M_\Lambda=m^2I+\alpha d_1^{*}d_1$** (from EXCITING_03 §3.2, verified numerically in item "Exact combinatorial row-sum constants"):
1. $\langle X,MX\rangle=m^2\|X\|^2+\alpha\|d_1X\|^2\ge m^2\|X\|^2$, so $a_0=m^2$ regardless of $\alpha$ — the positivity is purely the mass, not the kinetic term.
2. $(d_1X)_p$ depends only on the four links of $\partial p$ and $d_1^{*}$ redistributes a plaquette value to those four links, so $(d_1^{*}d_1)_{bb'}\ne0$ only if $b=b'$ or $b\sim b'$: range $R=1$ in $\mathrm{dist}_E$.
3. Each link lies in $\nu_P=2(d-1)$ plaquettes and each plaquette boundary contains $3$ other links, so $\#\{b'\sim b\}\le 3\nu_P$; the incidence coefficients are $\pm1$ and $\mathfrak g$-scalar, so $B_0(\alpha\Delta_1)\le\alpha\cdot3\nu_P=18\alpha$ in $d=4$.

### Constants and numbers

Definitions used (Appendix A of the corpus): $\nu_P:=\sup_b\#\{p: b\in\partial p\}=2(d-1)$; $D_E:=\sup_b\#\{b'\ne b: b'\sim b\}\le 3\nu_P$; in $d=4$, $\nu_P=6$, $D_E=18$, $m_\partial=4$ (links per plaquette).

Massive Maxwell in $d=4$, $m^2=0.3$, $\alpha=1$ (the corpus's standard parameter point, $m=0.547723$):
  $a_0=m^2=0.3$, $R=1$, $B_0=\alpha C_0(\Delta_1)=18$;
  $\eta_{\rm CT}=\log(1+0.3/36)=\mathbf{0.0082988}$ (prefactor $2/m^2=6.667$).
The corpus reports $\eta_{\rm CT}=0.003410$ because it used the artefactual $C_0=43.9077$; with the correct $C_0=18$ the exponent is $2.43\times$ larger.

Small-mass asymptotics: $\eta_{\rm CT}\simeq \dfrac{a_0}{2RB_0}=\dfrac{m^2}{2R\alpha C_0}$ — **quadratic** in $m$.

Cross-check in $d=2$ (from `SIMULATIONS/sanity_check_maxwell_decay.py`, $L=12$, $m^2=\alpha=1$): the script computes $\nu=\max_b\sum_{b'\ne b}|(\alpha d_1^{*}d_1)_{bb'}|=6.000000$ directly from the sparse matrix, i.e. $C_0(\Delta_1)=6=D_E$ in $d=2$. NB the script prints $\log(1+m^2/\nu)=0.154151$, which drops the factor $2$ of the theorem; the theorem's value is $\log(1+m^2/(2\nu))=0.080043$.

### Code

Hypothesis check for $M=m^2I+\alpha d_1^*d_1$, $d=2$, and empirical slope — `SIMULATIONS/sanity_check_maxwell_decay.py` (byte-identical copy at `MAXWELL/Decay_Estimates/sanity_check_maxwell_decay.py`). Key function:

    def inverse_decay_data(L, m2=1.0, alpha=1.0):
        d1, edge_index = build_d1(L)               # C^1 -> C^2 on Z_L^2, 4 signed entries per plaquette
        K  = (d1.T @ d1).astype(float)             # Delta_1 on edges
        M  = m2*np.eye(nE) + alpha*K
        G  = np.linalg.inv(M)
        i0 = edge_index[(0,0,0)]
        # BFS on the nonzero off-diagonal pattern of K  ->  dist_E
        # envelope max_{dist=r} |G[i0,j]| , then polyfit of log(env) on r=1..10
        off_row_sums = np.sum(np.abs(alpha*K),axis=1) - np.abs(np.diag(alpha*K))
        nu = float(np.max(off_row_sums))           # = C_0(Delta_1) = 6 in d=2
        eta_bound = math.log(1.0 + m2/nu)          # NOTE: theorem needs m2/(2*nu)

Run: `python SIMULATIONS/sanity_check_maxwell_decay.py`. Executed output ($L=12$, $m^2=\alpha=1$, 288 links):

    nu = 6.000000 ;  eta >= log(1+m/nu) = 0.154151 ;  empirical fit slope b = -0.832613
    dist |  max|G|   |  mean|G|  | count
       0 | 6.270e-01 | 6.270e-01 |   1
       1 | 1.509e-01 | 1.468e-01 |   6
       2 | 7.110e-02 | 3.131e-02 |  16
       3 | 1.454e-02 | 8.143e-03 |  24
       4 | 4.976e-03 | 2.844e-03 |  32
       5 | 2.116e-03 | 1.105e-03 |  40
       6 | 9.285e-04 | 4.611e-04 |  47
       7 | 4.859e-04 | 2.456e-04 |  41
       8 | 3.078e-04 | 1.313e-04 |  32
       9 | 1.651e-04 | 6.879e-05 |  24
      10 | 8.035e-05 | 3.599e-05 |  16
      11 | 3.992e-05 | 2.062e-05 |   8
      12 | 2.838e-05 | 2.838e-05 |   1

**Caveat.** The theorem is standard textbook Combes–Thomas; the corpus's contribution is a careful, constant-explicit, matrix-valued statement, not a new method. The rate is very far from sharp: at $m^2=0.3,\alpha=1$ the bound gives $0.0083$ against a true axis rate of $0.5411$ (a factor $65$).

**Why it matters.** This is the one link in the corpus's mass-gap chain that is unconditionally correct: it converts a spectral gap ($M\succeq m^2I$) plus locality into volume-uniform exponential kernel decay, with every constant explicit and none depending on $|\Lambda|$. It is the input to the Helffer–Sjöstrand covariance bound and hence to any clustering statement.

---

## 2. Theorem D (Davies form-conjugation decay: one-parameter family, sharp threshold θ*, and the O(m) small-mass rate)

`status: solid` · `kind: theorem`

### Statement

Let $\mathcal H=\ell^2(V;\mathsf H_0)$ with $V$ finite, $\mathsf H_0$ finite-dimensional, and let $L=L^{*}\succeq0$ on $\mathcal H$ have blocks $L_{xz}$ and interaction range $1$ in a graph metric $\mathrm{dist}$. Put $M:=m^2I+L$ with $m^2>0$.

Fix a base point $z_0\in V$, let $\phi(x):=\mathrm{dist}(x,z_0)$ (1-Lipschitz, integer-valued) and define the **level-set (boundary) row-sum constant**
$$C_\partial(L):=\sup_{z_0\in V}\ \sup_{x\in V}\ \sum_{\substack{z\ne x\\ |\phi(x)-\phi(z)|=1}}\bigl\|L_{xz}\bigr\|_{\rm op}\ \le\ C_0(L):=\sup_x\sum_{z\ne x}\|L_{xz}\|_{\rm op}.$$

**(a) One-parameter family.** For every $\lambda\ge0$ with $C_\partial(L)(\cosh\lambda-1)<m^2$, and all $x,z_0\in V$,
$$\boxed{\ \bigl\|(M^{-1})_{xz_0}\bigr\|_{\rm op}\ \le\ \frac{1}{m^2-C_\partial(L)(\cosh\lambda-1)}\ e^{-\lambda\,\mathrm{dist}(x,z_0)}.\ }$$

**(b) Sharp threshold.** The admissible exponents are exactly $\lambda\in[0,\theta^{*})$ with
$$\theta^{*}:=\operatorname{arcosh}\Bigl(1+\frac{m^2}{C_\partial(L)}\Bigr)=2\operatorname{arsinh}\Bigl(\frac{m}{2\sqrt{C_\partial(L)}}\Bigr),$$
the prefactor blowing up as $\lambda\uparrow\theta^{*}$.

**(c) Canonical (clean-prefactor) choice.** Taking $\lambda=\eta_{\rm DG}$ with $C_\partial(L)(\cosh\eta_{\rm DG}-1)=m^2/2$, i.e.
$$\eta_{\rm DG}=\operatorname{arcosh}\Bigl(1+\frac{m^2}{2C_\partial(L)}\Bigr)=2\operatorname{arsinh}\Bigl(\frac{m}{2\sqrt{2C_\partial(L)}}\Bigr),$$
gives $\bigl\|(M^{-1})_{xz_0}\bigr\|_{\rm op}\le\frac{2}{m^2}e^{-\eta_{\rm DG}\mathrm{dist}(x,z_0)}$.

**(d) Small-mass scaling.** $\theta^{*}=\dfrac{m}{\sqrt{C_\partial(L)}}\bigl(1+O(m^2)\bigr)$ and $\eta_{\rm DG}=\dfrac{m}{\sqrt{2C_\partial(L)}}\bigl(1+O(m^2)\bigr)$ — **linear in $m$**, versus $\eta_{\rm CT}\simeq m^2/(2C_0)$ from Theorem CT.

Specialised to $M_\Lambda=m^2I+\alpha\,d_1^{*}d_1$ on $\ell^2(E(\Lambda);\mathfrak g)$ with the link metric $\mathrm{dist}_E$: $L=\alpha\Delta_1$, $C_\partial(L)=\alpha C_\partial(\Delta_1)\le\alpha C_0(\Delta_1)\le\alpha D_E$, and
$$\bigl\|(M_\Lambda^{-1})_{bb'}\bigr\|_{\rm op}\le\frac{2}{m^2}\exp\Bigl(-\operatorname{arcosh}\bigl(1+\tfrac{m^2}{2\alpha C_\partial(\Delta_1)}\bigr)\,\mathrm{dist}_E(b,b')\Bigr).$$

### Derivation

Best source: `MAXWELL/Decay_Estimates/Appendix_H__Davies_Type_Decay_Massive_Maxwell_Green_Kernel(1).md` (Lemmas H.1.1–H.3.5, Propositions H.4.1–H.4.4) — this is the only version in the corpus that gets the full one-parameter family and the level-set constant right from the start. `COMBES_THOMAS/MAXWELL_GREEN/davies_decay_massive_maxwell.md` and `02_davies_decay_maxwell_boundary_rowsum(1).md` are readable summaries of the same argument. Two independent routes to (a) exist; I give both because the second (numerical range) is shorter and the first (Laplace/semigroup) is the corpus's.

---
**Route 1 (Appendix H: Laplace transform + conjugated semigroup).**

*Step 1 (resolvent as Laplace transform).* $L=L^{*}\succeq0$ on a finite-dimensional space has an orthonormal eigenbasis $Lv_j=\lambda_jv_j$, $\lambda_j\ge0$. For each $j$, $(m^2+\lambda_j)^{-1}=\int_0^\infty e^{-(m^2+\lambda_j)t}dt$, so by linearity
$$M^{-1}=\int_0^{\infty}e^{-m^2t}\,e^{-tL}\,dt,$$
the integral converging in operator norm since $\|e^{-tL}\|\le1$ and $\int_0^\infty e^{-m^2t}dt=m^{-2}<\infty$.

*Step 2 (Davies weight).* Let $W_\lambda$ be multiplication by $e^{\lambda\phi}$, $\phi=\mathrm{dist}(\cdot,z_0)$. Then $(W_\lambda LW_\lambda^{-1})_{xz}=e^{\lambda(\phi(x)-\phi(z))}L_{xz}$, and $W_\lambda LW_\lambda^{-1}$ is **not** self-adjoint; its adjoint is $W_{-\lambda}LW_{-\lambda}^{-1}$ (conjugation by a positive diagonal). Hence its symmetric part is
$$\tfrac12\bigl(W_\lambda LW_\lambda^{-1}+W_{-\lambda}LW_{-\lambda}^{-1}\bigr)=L+Q_\lambda,\qquad (Q_\lambda)_{xz}=\bigl[\cosh\bigl(\lambda(\phi(x)-\phi(z))\bigr)-1\bigr]L_{xz},$$
using $\tfrac12(e^{u}+e^{-u})=\cosh u$. Note $(Q_\lambda)_{xx}=0$ since $\cosh0-1=0$, and $Q_\lambda=Q_\lambda^{*}$.

*Step 3 (the level-set bound — where $C_\partial$ enters).* If $L_{xz}\ne0$ with $x\ne z$, then $\mathrm{dist}(x,z)=1$, so by 1-Lipschitzness and integrality $|\phi(x)-\phi(z)|\in\{0,1\}$. **If it is $0$ the factor $\cosh(0)-1$ vanishes identically**; only pairs crossing a level set of $\phi$ contribute. If it is $1$ then $\cosh(\lambda\cdot(\pm1))-1=\cosh\lambda-1$. Hence
$$\sup_x\sum_{z\ne x}\|(Q_\lambda)_{xz}\|_{\rm op}\le(\cosh\lambda-1)\sup_x\!\!\sum_{\substack{z\ne x\\|\phi(x)-\phi(z)|=1}}\!\!\|L_{xz}\|_{\rm op}\le(\cosh\lambda-1)\,C_\partial(L),$$
and since $Q_\lambda$ is self-adjoint with zero diagonal, the block Schur lemma (self-adjoint case, proved in Theorem CT above) gives
$$\|Q_\lambda\|_{\rm op}\le C_\partial(L)\,(\cosh\lambda-1)=:q_\lambda.$$

*Step 4 (conjugated semigroup).* $W_\lambda e^{-tL}W_\lambda^{-1}=e^{-tW_\lambda LW_\lambda^{-1}}$ (expand the exponential series and use $(WAW^{-1})^k=WA^kW^{-1}$). Let $u(t)=e^{-tW_\lambda LW_\lambda^{-1}}u_0$; then
$$\tfrac{d}{dt}\|u\|^2=-2\,\Re\langle u,W_\lambda LW_\lambda^{-1}u\rangle=-2\langle u,(L+Q_\lambda)u\rangle\le 2q_\lambda\|u\|^2,$$
using $L\succeq0$ and $\langle u,Q_\lambda u\rangle\ge-q_\lambda\|u\|^2$. Gronwall (i.e. $h(t)=e^{-2q_\lambda t}\|u(t)\|^2$ has $h'\le0$) gives $\|u(t)\|\le e^{q_\lambda t}\|u_0\|$, i.e.
$$\bigl\|W_\lambda e^{-tL}W_\lambda^{-1}\bigr\|_{\rm op}\le e^{q_\lambda t}.$$

*Step 5 (integrate).* Conjugating the Laplace formula,
$$\bigl\|W_\lambda M^{-1}W_\lambda^{-1}\bigr\|_{\rm op}\le\int_0^{\infty}e^{-m^2t}e^{q_\lambda t}\,dt=\frac{1}{m^2-q_\lambda},$$
convergent **iff** $q_\lambda<m^2$, which is exactly $\lambda<\theta^{*}$.

*Step 6 (extract the kernel).* $\bigl(W_\lambda M^{-1}W_\lambda^{-1}\bigr)_{xz_0}=e^{\lambda(\phi(x)-\phi(z_0))}(M^{-1})_{xz_0}=e^{\lambda\,\mathrm{dist}(x,z_0)}(M^{-1})_{xz_0}$ since $\phi(z_0)=0$. Taking $\|\cdot\|_{\rm op}$ and $\|T_{xz}\|_{\rm op}\le\|T\|_{\rm op}$ yields (a). $\blacksquare$

---
**Route 2 (numerical range — shorter, same constant) [reconstructed].** With $M_\lambda:=W_\lambda MW_\lambda^{-1}=m^2I+W_\lambda LW_\lambda^{-1}$, Step 2–3 give for every $f$
$$\Re\langle f,M_\lambda f\rangle=m^2\|f\|^2+\langle f,Lf\rangle+\langle f,Q_\lambda f\rangle\ \ge\ \bigl(m^2-q_\lambda\bigr)\|f\|^2.$$
If $c:=m^2-q_\lambda>0$ then $\|M_\lambda f\|\|f\|\ge|\langle f,M_\lambda f\rangle|\ge c\|f\|^2$, so $\|M_\lambda f\|\ge c\|f\|$; the same holds for $M_\lambda^{*}=W_{-\lambda}MW_{-\lambda}^{-1}$, so $M_\lambda$ is invertible with $\|M_\lambda^{-1}\|_{\rm op}\le 1/c$. Step 6 is unchanged. This route makes clear that **no semigroup is needed** — only that the antisymmetric part of the conjugated operator is invisible to the lower bound on the real part of the numerical range.

---
**Proof of (b), (c), (d).** $q_\lambda=C_\partial(\cosh\lambda-1)$ is strictly increasing on $[0,\infty)$ from $0$, so $q_\lambda<m^2\iff\cosh\lambda<1+m^2/C_\partial\iff\lambda<\theta^{*}$. The identity $\operatorname{arcosh}(1+2s^2)=2\operatorname{arsinh}(s)$ with $s=m/(2\sqrt{C_\partial})$ gives the $\operatorname{arsinh}$ form (check: $\cosh(2\operatorname{arsinh} s)=1+2\sinh^2(\operatorname{arsinh} s)=1+2s^2$). Setting $q_\lambda=m^2/2$ gives (c) and prefactor $1/(m^2-m^2/2)=2/m^2$. For (d), $\operatorname{arcosh}(1+x)=\sqrt{2x}\,(1-x/12+O(x^2))$ as $x\downarrow0$, so $\theta^{*}=\sqrt{2m^2/C_\partial}\,(1+O(m^2))\cdot\tfrac{1}{\sqrt2}\cdot\sqrt2=m/\sqrt{C_\partial}+O(m^3)$, and likewise $\eta_{\rm DG}=m/\sqrt{2C_\partial}+O(m^3)$. $\square$

---
**Why Davies beats Combes–Thomas (the actual mechanism).** Both arguments conjugate by the same exponential weight. The difference is *what is bounded*:
- CT bounds the **full** perturbation $\|K_t\|\le(e^{tR}-1)B_0\simeq tRB_0$ — **linear** in $t$ — and needs $\|K_t\|\le a_0/2$, giving $t\simeq a_0/(2RB_0)\sim m^2$.
- Davies bounds only the **symmetric part** $\|Q_\lambda\|\le C_\partial(\cosh\lambda-1)\simeq \tfrac12\lambda^2C_\partial$ — **quadratic** in $\lambda$ — and needs $\|Q_\lambda\|<m^2$, giving $\lambda\lesssim m/\sqrt{C_\partial}\sim m$.
The quadratic-vs-linear behaviour at small $\lambda$ is the entire gain, and it is exactly the statement that the antisymmetric (odd in $\lambda$) part of the conjugation cannot destroy coercivity.

### Constants and numbers

All values for $M=m^2I+\alpha\Delta_1$, $\alpha=1$, computed exactly; $C$ below is $C_\partial(\Delta_1)$ or an upper bound for it.

$d=4$, $m^2=0.3$ ($m=0.547723$):
| constant $C$ | source | $\theta^{*}=\operatorname{arcosh}(1+m^2/C)$ | $\eta_{\rm DG}=\operatorname{arcosh}(1+m^2/2C)$ | $\eta_{\rm CT}=\log(1+m^2/2C)$ |
|---|---|---|---|---|
| 18 | $\Delta_1$, link-graph metric ($=C_0=D_E$) | 0.182322 | **0.129010** | 0.008299 |
| 8 | Feynman-gauge / scalar Laplacian, $2d$ | 0.273013 | **0.193348** | 0.018576 |
| 6 | $\Delta_1$, linear weight $\phi=x_\mu$ | 0.314925 | 0.223144 | 0.024693 |
| 2 | one-dimensional / directional | **0.541097** | 0.384918 | 0.072321 |
Exact axis decay rate of the true kernel: $\kappa_{\rm axis}=\operatorname{arcosh}(1+m^2/2\alpha)=\mathbf{0.541097}$.
The two boldface $\eta_{\rm DG}$ values 0.129010 and 0.193348 are exactly the corpus's reported $\eta_{\rm DG}(D_E)$ and gauge-fixed $\eta$ (`Untitled125_extracted.py` output lines).

$d=2$, $m^2=1$ (the `sanity_check_maxwell_decay.py` point), $C_0(\Delta_1)=D_E=6$:
  $\theta^{*}=0.569618$, $\eta_{\rm DG}=0.405465$, $\eta_{\rm CT}=0.080043$; exact $\kappa_{\rm axis}=\operatorname{arcosh}(1.5)=0.962424$; measured link-graph envelope slope $0.8326$.

**Sharpness of $\theta^{*}$.** For the scalar massive lattice Laplacian $m^2I+\alpha\Delta$ on $\mathbb Z$ ($C_\partial=2$), $\theta^{*}=\operatorname{arcosh}(1+m^2/2\alpha)=\kappa_{\rm axis}$ **exactly**: the Davies threshold is attained, not merely a bound. The loss in $d$ dimensions with the $\ell^1$ metric and $C_\partial=2d$ is exactly $\theta^{*}/\kappa_{\rm axis}\to1/\sqrt d$ as $m\to0$; numerically at $d=4$, $m^2=0.05$: $0.111745/0.223144=0.5008\approx1/2$.

### Code

The theorem is analytic; the constant table above is produced by:

    import math
    def rates(m2, alpha, C):
        return (math.acosh(1+m2/(alpha*C)),          # theta*  (sharp threshold)
                math.acosh(1+m2/(2*alpha*C)),        # eta_DG  (prefactor 2/m^2)
                math.log (1+m2/(2*alpha*C)))         # eta_CT  (Theorem CT)
    for C in (18, 8, 6, 2): print(C, rates(0.3, 1.0, C))

The combinatorial inputs $C_0,C_\partial$ are computed in `verify_ct_davies.py` parts A and E (see the "level-set refinement" item).

**Caveat.** The $\operatorname{arcosh}$ form is the standard optimised discrete Combes–Thomas/Davies exponent, not a new method; the corpus overstates it as a distinct 'Davies improvement'. The corpus also never uses the sharp $\theta^{*}$ of part (b), only the half-gap $\eta_{\rm DG}$ of part (c), losing a further factor $\sqrt2$.

**Why it matters.** This is the strongest correct decay statement in the corpus: it is the only version of the estimate whose exponent tracks the physical mass linearly ($\eta\sim m/\sqrt{C}$), which is the difference between 'a gap exists' and 'the bound sees the gap'. Part (b) — the full admissible family, with the sharp threshold and the diverging prefactor — is present in Appendix H but is never used numerically anywhere in the corpus; exploiting it improves the reported exponent by a further 41%.

---

## 3. Exact combinatorial row-sum and degree constants for Δ₁ = d₁*d₁ on a periodic hypercubic lattice

`status: solid` · `kind: numerical_result`

### Statement

Let $\Lambda=(\mathbb Z/L)^d$ be the periodic hypercubic lattice, $E(\Lambda)$ its oriented links, $d_1:\mathcal C^1\to\mathcal C^2$ the plaquette exterior derivative with unit incidence coefficients, and $\Delta_1=d_1^{*}d_1$ acting on $\ell^2(E(\Lambda);\mathfrak g)$ (block-scalar in $\mathfrak g$). Let $b\sim b'$ iff some plaquette boundary contains both. Then, **exactly and independently of $L$** (for $L\ge4$):
$$(\Delta_1)_{bb}=\nu_P\,\mathrm{Id}_{\mathfrak g}=2(d-1)\,\mathrm{Id}_{\mathfrak g},\qquad \|(\Delta_1)_{bb'}\|_{\rm op}=1\ \ \text{for each of the }D_E=3\nu_P=6(d-1)\text{ neighbours},$$
$$\boxed{\ C_0(\Delta_1)=\sup_b\sum_{b'\ne b}\|(\Delta_1)_{bb'}\|_{\rm op}=D_E=6(d-1)\ }$$
In $d=4$: diagonal $=6$, $D_E=18$, $C_0(\Delta_1)=18$. In $d=2$: diagonal $=2$, $D_E=6$, $C_0(\Delta_1)=6$. The bound $C_0(\Delta_1)\le D_E$ of the corpus's Proposition A.9.5 is therefore an **equality** for the standard incidence convention.

For the Feynman-gauge (Hodge) operator $\alpha\,d_1^{*}d_1+\xi\,d_0d_0^{*}$ at $\xi=\alpha$, the mixed terms cancel identically in the symbol and $C_0=2d$ ($=8$ in $d=4$).

### Derivation

**Analytic count.** Fix a link $b=(x,\mu)$. (i) *Diagonal.* $(\Delta_1)_{bb}=\sum_{p\ni b}\sigma_{p,b}^2=\#\{p:b\in\partial p\}=\nu_P$. In $d$ dimensions a link $(x,\mu)$ lies in the plaquettes based at $x$ and at $x-e_\nu$ in each of the $(d-1)$ planes $(\mu\nu)$, $\nu\ne\mu$: $\nu_P=2(d-1)$. (ii) *Off-diagonal.* $(\Delta_1)_{bb'}=\sum_{p\ni b,b'}\sigma_{p,b}\sigma_{p,b'}$. Two distinct links of a hypercubic lattice share **at most one** plaquette, so $|(\Delta_1)_{bb'}|\in\{0,1\}$, $=1$ exactly for the neighbours. (iii) *Neighbour count.* For each $\nu\ne\mu$ the two $(\mu\nu)$-plaquettes containing $b$ contribute the six links
$$(x,\nu),\ (x+e_\mu,\nu),\ (x+e_\nu,\mu)\quad\text{and}\quad (x-e_\nu,\nu),\ (x-e_\nu+e_\mu,\nu),\ (x-e_\nu,\mu),$$
all distinct and distinct across different $\nu$. Hence $D_E=6(d-1)=3\nu_P$, and since every off-diagonal entry has modulus exactly $1$, $C_0(\Delta_1)=D_E$. $\square$

**Numerical confirmation.** I built $d_1$ explicitly as a sparse signed incidence matrix on $(\mathbb Z/L)^4$ (four entries $+1,+1,-1,-1$ per plaquette, oriented boundary $\partial p_{x,\mu\nu}=(x,\mu)+(x{+}e_\mu,\nu)-(x{+}e_\nu,\mu)-(x,\nu)$), formed $\Delta_1=d_1^{T}d_1$ and read off the diagonal, the maximum and minimum off-diagonal absolute row sums, and the maximum off-diagonal sparsity degree. Result at $L=4,5,6$ ($1024$, $2500$, $5184$ links):
$$\text{diag}=\{6\},\quad \max_b\!\sum_{b'\ne b}|(\Delta_1)_{bb'}|=\min_b(\cdots)=18,\quad \max\deg=18,$$
i.e. the row sum is *constant* over links (translation and rotation invariance) and volume-independent, as the theory requires of a finite-range stencil.

The corpus's own BFS on the link graph (`Untitled125_extracted.py`, $L=16$, $d=4$) independently returns `Max degree D_E = 18`, agreeing.

### Constants and numbers

$d=4$ (verified at $L=4,5,6$): $\nu_P=6$, $m_\partial=4$, $D_E=18$, $C_0(\Delta_1)=18$ (max = min over links), $(\Delta_1)_{bb}=6$.
$d=2$: $\nu_P=2$, $D_E=6$, $C_0(\Delta_1)=6$, $(\Delta_1)_{bb}=2$ (confirmed by `sanity_check_maxwell_decay.py`, which prints $\nu=6.000000$).
Feynman gauge $\xi=\alpha$, $d=4$: $C_0=8=2d$ (confirmed by `Untitled125_extracted.py`: `New C0 (Laplacian): 8.0000`).
General $d$: $\nu_P=2(d-1)$, $D_E=C_0(\Delta_1)=6(d-1)$, diagonal $=2(d-1)$.

### Code

`verify_ct_davies.py`, part A (scratchpad copy at `C:\Users\Alex\AppData\Local\Temp\claude\F--ANTIGRAVITY-antigravity-playground-scalar-cluster-proof\fd74385b-6527-446a-ae5a-90acb16ad82a\scratchpad\verify_ct_davies.py`):

    def build_Delta1(L, d=4):
        links = [(x, mu) for x in itertools.product(range(L), repeat=d) for mu in range(d)]
        lidx  = {b: i for i, b in enumerate(links)}
        plaqs = [(x, mu, nu) for x in itertools.product(range(L), repeat=d)
                 for mu in range(d) for nu in range(mu+1, d)]
        rows, cols, vals = [], [], []
        for pi, (x, mu, nu) in enumerate(plaqs):
            xm = list(x); xm[mu] = (xm[mu]+1) % L; xm = tuple(xm)
            xn = list(x); xn[nu] = (xn[nu]+1) % L; xn = tuple(xn)
            for b, s in [((x,mu),1), ((xm,nu),1), ((xn,mu),-1), ((x,nu),-1)]:
                rows.append(pi); cols.append(lidx[b]); vals.append(s)
        d1 = sp.coo_matrix((vals,(rows,cols)), shape=(len(plaqs),len(links))).tocsr()
        return (d1.T @ d1).tocsr().astype(float), links

Executed output:

    L=4: diag=[6.], C0=max off-diag row-sum=18, min=18, D_E=max degree=18
    L=5: diag=[6.], C0=max off-diag row-sum=18, min=18, D_E=max degree=18
    L=6: diag=[6.], C0=max off-diag row-sum=18, min=18, D_E=max degree=18

**Caveat.** The value $18$ is for unit incidence coefficients ($\sigma_{p,b}=\pm1$) and the plaquette-adjacency link metric; a different normalisation of $d_1$ or a different metric rescales it.

**Why it matters.** $C_0(\Delta_1)$ is the single number that sets every decay exponent in the corpus's chain. Fixing it at the exact, volume-independent value $18$ (rather than the reported, volume-divergent $43.9077$) multiplies the reported Combes–Thomas exponent by $2.44$ and, more importantly, restores the volume-uniformity that the whole thermodynamic-limit argument depends on.

---

## 4. Correction: the reported C₀(Δ₁) ≈ 43.9077 is a reproducible symbol-convention artifact with √L divergence

`status: solid` · `kind: obstruction`

### Statement

The corpus computes $C_0(\Delta_1)$ numerically (`Untitled125_extracted.py`; quoted in `03_maxwell_C0_decay_and_kappa_plateau.md`, `03_greens_decay_combes_thomas.md`, `gauge_fixing_hodge_laplacian_constants.md`) by inverse-FFT of the momentum-space symbol
$$Q_{\mu\nu}(p)=\hat p^{\,2}\delta_{\mu\nu}-\hat p_\mu\hat p_\nu,\qquad \hat p_\mu:=2\sin(p_\mu/2)\ \ (\textbf{real}),$$
taking the real part of the resulting kernel and summing absolute values. This yields $C_0\approx43.9077$ at $L=16$, $d=4$.

**Claim.** That number is not $C_0(\Delta_1)$. It is a lattice artifact with two independent causes, and it diverges like $\sqrt L$:
$$C_0^{\rm reported}(L)\ \approx\ 11.33\sqrt L-1.0\qquad(L=8\ldots32).$$
The exact value is $C_0(\Delta_1)=18$, independent of $L$, and the correct FFT recipe returns $18.000000$ at every $L$.

**Cause 1 (half-frequency symbol).** $2\sin(p/2)=|e^{ip}-1|$ is *not* a trigonometric polynomial in $e^{ip}$: its inverse DFT over integer sites is a long-tailed oscillatory sequence, so the products $\hat p_\mu\hat p_\nu$ ($\mu\ne\nu$) have kernels that are not finite-range. The correct forward-difference symbol is $\tilde p_\mu:=e^{ip_\mu}-1$, for which $Q_{\mu\nu}=\delta_{\mu\nu}\sum_\rho|\tilde p_\rho|^2-\overline{\tilde p_\mu}\tilde p_\nu$ is an exact trigonometric polynomial.

**Cause 2 (discarding the imaginary part).** With real $\hat p_\mu$, the block $-\hat p_\mu\hat p_\nu$ ($\mu\ne\nu$) is odd under $p_\mu\mapsto-p_\mu$ alone, so its exact inverse transform is purely imaginary; the code's `.real` therefore keeps only the residual Nyquist-aliasing part, which is what grows with $L$.

### Derivation

**Exact reproduction of the reported numbers.** Re-implementing the corpus recipe verbatim in numpy (`fftfreq` momenta, $\hat p_\mu=2\sin(p_\mu/2)$, `ifftn(...).real`, $C_0=\max_\mu\bigl[\sum_{\nu,x}|K_{\mu\nu}(x)|-|K_{\mu\mu}(0)|\bigr]$) gives
$$L=8:\ 29.7764,\quad L=12:\ 37.4119,\quad L=16:\ \mathbf{43.9077},\quad L=20:\ 49.5511,\quad L=24:\ \mathbf{54.5495},\quad L=32:\ 63.1373,$$
matching to all printed digits both the corpus's own $L=16$ figure ($43.9077$) and the two spot checks recorded in the corpus's dead-ends file ($29.78$ at $L=8$, $54.55$ at $L=24$). The reproduction is therefore exact, and the diagnosis below applies to the actual code that produced the corpus number.

**Block decomposition of the artifact.** Splitting $C_0^{\rm reported}$ by $(\mu,\nu)$ block for $\mu=0$:
| $L$ | diagonal block $\mu=\nu$ | each off-diagonal block $\mu\ne\nu$ | total |
|---|---|---|---|
| 8 | 6.00000 | 7.92548 | 29.7764 |
| 16 | 6.00000 | 12.63591 | 43.9077 |
| 24 | 6.00000 | 16.18317 | 54.5495 |
| 32 | 6.00000 | 19.04575 | 63.1373 |
The diagonal block is **exactly 6** at every $L$ — correct, because $Q_{\mu\mu}=\sum_{\rho\ne\mu}(2-2\cos p_\rho)$ *is* a lattice trigonometric polynomial, whose kernel is $2\delta_0-\delta_{+e_\rho}-\delta_{-e_\rho}$ per direction, giving off-origin $\ell^1$ mass $2\times(d-1)=6$. The entire divergence sits in the three off-diagonal blocks, exactly as the two causes predict. Their correct values are $4$ each (the kernel of $-\overline{\tilde p_\mu}\tilde p_\nu$ has four unit entries), giving the exact total $6+3\times4=18$.

**The corrected recipe.** Replacing $\hat p_\mu\to\tilde p_\mu=e^{ip_\mu}-1$ and taking $|K|$ of the *complex* kernel returns $C_0=18.000000$ at $L=8,12,16,20,24,32$ — volume-independent, and equal to the exact combinatorial value computed from the sparse incidence matrix.

**Consequence for the 'constant unification' conjecture.** `03_maxwell_C0_decay_and_kappa_plateau.md` §5 conjectures that a fitted drift constant $\hat b\approx43.1239$ and $C_0\approx43.9077$ are 'controlled by the same underlying row-sum'. Since $C_0^{\rm reported}$ is a $\sqrt L$-divergent artifact anchored to $L=16$ while the true $C_0$ is $18$, the numerical coincidence carries no information.

**Consequence for the exponents.** With $m^2=0.3,\alpha=1$: $\eta_{\rm CT}$ improves from the reported $0.003410$ to $0.008299$ ($2.44\times$); $\eta_{\rm DG}(C_0)$ improves from the reported $0.082635$ to $0.129010$ ($1.56\times$), i.e. it coincides with the corpus's $\eta_{\rm DG}(D_E)=0.129010$ — as it must, since $C_0(\Delta_1)=D_E=18$ exactly.

### Constants and numbers

Reported (artifact), $d=4$, corpus recipe: $C_0(L{=}8)=29.7764$, $C_0(12)=37.4119$, $C_0(16)=43.9077$, $C_0(20)=49.5511$, $C_0(24)=54.5495$, $C_0(32)=63.1373$. Fit: $C_0^{\rm reported}\approx11.33\sqrt L-1.0$ (residual $<0.5$ over $L\in[8,32]$).
Correct: $C_0(\Delta_1)=18.000000$ at every $L$.
Block split at $L=16$: diagonal $6.00000$ (correct), off-diagonal $12.63591$ each (should be $4$).
Repaired exponents at $m^2=0.3$, $\alpha=1$: $\eta_{\rm CT}=0.008299$ (was $0.003410$); $\eta_{\rm DG}=0.129010$ (was $0.082635$); sharp $\theta^{*}=0.182322$ (never computed in the corpus).

### Code

`verify_ct_davies.py`, part B. Both recipes side by side:

    def C0_corpus(L):            # reproduces 29.7764 / 43.9077 / 54.5495 exactly
        P = grids(L); hp = [2*np.sin(P[mu]/2) for mu in range(d)]     # REAL half-frequency
        p2 = sum(h**2 for h in hp); C0 = 0.0
        for mu in range(d):
            s = 0.0
            for nu in range(d):
                Q = (p2 if mu == nu else 0.0) - hp[mu]*hp[nu]
                K = np.fft.ifftn(np.asarray(Q, dtype=complex)).real   # <-- .real discards the block
                a = np.abs(K)
                if nu == mu: a[(0,)*d] = 0.0
                s += a.sum()
            C0 = max(C0, float(s))
        return C0

    def C0_correct(L):           # returns 18.000000 at every L
        P = grids(L); tp = [np.exp(1j*P[mu]) - 1.0 for mu in range(d)] # forward-difference symbol
        p2 = sum(np.abs(t)**2 for t in tp); C0 = 0.0
        for mu in range(d):
            s = 0.0
            for nu in range(d):
                Q = (p2 if mu == nu else 0.0) - np.conj(tp[mu])*tp[nu]
                K = np.fft.ifftn(np.asarray(Q, dtype=complex)); a = np.abs(K)
                if nu == mu: a[(0,)*d] = 0.0
                s += a.sum()
            C0 = max(C0, float(s))
        return C0

Executed output:

    L=  8  corpus recipe =   29.7764   correct symbol = 18.000000
    L= 12  corpus recipe =   37.4119   correct symbol = 18.000000
    L= 16  corpus recipe =   43.9077   correct symbol = 18.000000
    L= 20  corpus recipe =   49.5511   correct symbol = 18.000000
    L= 24  corpus recipe =   54.5495   correct symbol = 18.000000
    L= 32  corpus recipe =   63.1373   correct symbol = 18.000000

**Caveat.** The corpus's own note `02_davies_decay_row_sum_constants.md` §5 already flags the mismatch ('should be volume-independent for a finite-range stencil') without diagnosing it; the diagnosis and repair above are mine.

**Why it matters.** The corpus published a decay-relevant 'measured constant' that is volume-divergent — precisely the property that would destroy the thermodynamic-limit uniformity the theorems are for. Pinning it (exactly reproducing it, isolating the two causes, and giving the corrected recipe that returns the exact combinatorial answer at every volume) turns a silent numerical bug into a usable, verified constant and improves every downstream exponent.

---

## 5. Exact closed form and sharp exponential decay rate for the massive lattice Maxwell Green kernel

`status: solid` · `kind: derivation`

### Statement

On the periodic lattice $(\mathbb Z/L)^d$, let $\tilde p_\mu=e^{ip_\mu}-1$, $\hat p^{\,2}=\sum_\rho|\tilde p_\rho|^2=\sum_\rho(2-2\cos p_\rho)$, and let $\Delta_{\rm sc}$ denote the *componentwise* scalar lattice Laplacian (symbol $\hat p^{\,2}\,\mathrm{Id}$). Let $M=m^2I+\alpha\,d_1^{*}d_1$ on 1-cochains with $m^2>0$, $\alpha>0$. Then
$$\boxed{\ M^{-1}\ =\ \frac{1}{m^{2}}\,I\ -\ \frac{\alpha}{m^{2}}\ \Delta_1\,\bigl(m^{2}I+\alpha\Delta_{\rm sc}\bigr)^{-1}.\ }$$
Consequently:
1. the off-coincidence part of the Green kernel is $-\tfrac{\alpha}{m^2}$ times the *finite-range* operator $\Delta_1$ applied to the **scalar** massive lattice propagator $G_{\rm sc}=(m^2+\alpha\Delta_{\rm sc})^{-1}$;
2. hence the exact decay along a coordinate axis is
$$\kappa_{\rm axis}=\operatorname{arcosh}\Bigl(1+\frac{m^{2}}{2\alpha}\Bigr)=2\operatorname{arsinh}\Bigl(\frac{m}{2\sqrt\alpha}\Bigr),$$
independent of $d$, with the standard $r^{-(d-1)/2}$ prefactor: $|G(r e_1)|\sim A\,r^{-(d-1)/2}e^{-\kappa_{\rm axis}r}$;
3. in particular no exponent produced by Theorem CT or Theorem D can exceed $\kappa_{\rm axis}$, and $\kappa_{\rm axis}$ is exactly the $C_\partial=2$ (one-dimensional) instance of the Davies threshold $\theta^{*}$.

Explicitly for one diagonal component: $G_{11}(x)=G_{\rm sc}(x)+\tfrac{\alpha}{m^{2}}\bigl[2G_{\rm sc}(x)-G_{\rm sc}(x+e_1)-G_{\rm sc}(x-e_1)\bigr]$.

### Derivation

[reconstructed — the transverse/longitudinal symbol decomposition is the corpus's (`gauge_fixing_hodge_laplacian_constants.md` §2, `Untitled125_extracted.py`), but the closed form, the resolution of the longitudinal-tail puzzle, and the sharp exponent are mine.]

*Step 1 (symbol).* With $\tilde p_\mu=e^{ip_\mu}-1$, the lattice $d_1$ has symbol $(\widehat{d_1A})_{\mu\nu}=\tilde p_\mu A_\nu-\tilde p_\nu A_\mu$, so
$$(\widehat{\Delta_1})_{\mu\nu}(p)=\hat p^{\,2}\delta_{\mu\nu}-\overline{\tilde p_\mu}\,\tilde p_\nu=\hat p^{\,2}\,(P_T)_{\mu\nu}(p),\qquad (P_L)_{\mu\nu}:=\frac{\overline{\tilde p_\mu}\tilde p_\nu}{\hat p^{\,2}},\ \ P_T=I-P_L,$$
$P_T,P_L$ being the orthogonal projectors onto the transverse/longitudinal subspaces at momentum $p$ ($P_L$ is rank one for $p\ne0$).

*Step 2 (inverse symbol).* $\widehat M=(m^2+\alpha\hat p^{\,2})P_T+m^2P_L$, so
$$\widehat{M^{-1}}=\frac{P_T}{m^2+\alpha\hat p^{\,2}}+\frac{P_L}{m^2}.$$

*Step 3 (the key rearrangement).* Write $P_L=I-P_T$:
$$\widehat{M^{-1}}=\frac{I}{m^2}+P_T\Bigl[\frac{1}{m^2+\alpha\hat p^{\,2}}-\frac{1}{m^2}\Bigr]=\frac{I}{m^2}-\frac{\alpha}{m^2}\cdot\frac{\hat p^{\,2}P_T}{m^2+\alpha\hat p^{\,2}}=\frac{I}{m^2}-\frac{\alpha}{m^2}\cdot\frac{\widehat{\Delta_1}}{m^2+\alpha\hat p^{\,2}},$$
using $\hat p^{\,2}P_T=\widehat{\Delta_1}$ from Step 1. Inverse-transforming gives the boxed identity.

*Step 4 (why this resolves an apparent contradiction).* Taken separately, the longitudinal term $m^{-2}P_L$ has a kernel decaying only like $|x|^{-d}$ (because $P_L(p)$ is not smooth at $p=0$), which appears to contradict the exponential decay guaranteed by Theorem CT. Step 3 shows the resolution: the non-smooth pieces of $P_T/(m^2+\alpha\hat p^2)$ and $P_L/m^2$ cancel exactly, leaving $m^{-2}\delta$ plus $-\tfrac{\alpha}{m^2}\widehat{\Delta_1}/(m^2+\alpha\hat p^{\,2})$, in which $\widehat{\Delta_1}$ is a trigonometric polynomial and the denominator is real-analytic and non-vanishing for $p$ in a complex strip.

*Step 5 (sharp exponent).* The decay rate along the $x_1$ axis is the width of the strip of analyticity of $p_1\mapsto1/(m^2+\alpha\hat p^{\,2})$ at $p_2=\dots=p_d=0$. Setting $p_1=i\theta$ gives $2-2\cos(i\theta)=2-2\cosh\theta$, so the symbol vanishes when $m^2+\alpha(2-2\cosh\theta)=0$, i.e.
$$\cosh\theta=1+\frac{m^2}{2\alpha}\ \Longrightarrow\ \theta=\kappa_{\rm axis}=\operatorname{arcosh}\bigl(1+\tfrac{m^2}{2\alpha}\bigr)=2\operatorname{arsinh}\bigl(\tfrac{m}{2\sqrt\alpha}\bigr).$$
Saddle-point evaluation of the remaining $(d-1)$ transverse momentum integrals produces the standard $r^{-(d-1)/2}$ prefactor. $\square$

*Step 6 (numerical verification).* Built both sides on $T^4$, $L=16$, $m^2=0.3$, $\alpha=1$ by explicit inverse FFT of all $16$ blocks: $\max_{\mu\nu,x}\bigl|G_{\mu\nu}(x)-\text{RHS}_{\mu\nu}(x)\bigr|=2.220\times10^{-16}$. Also $G_{00}(0)=0.9412344592$, whence $(m^2/2)|G(0)|=0.1412$, which is exactly the corpus's reported 'max ratio $\approx0.1412$ at distance 0' in the bound check — confirming that the corpus's verification statistic is dominated by the coincident value and therefore does not test the exponent at all.

*Step 7 (relation to the bounds).* Since the Davies threshold with the one-dimensional constant $C_\partial=2$ is $\operatorname{arcosh}(1+m^2/2\alpha)=\kappa_{\rm axis}$, the Davies method is **exactly sharp** in the directional/1-D case; all loss in higher $d$ comes from the Schur bound treating all $C_\partial$ neighbours as though each contributed fully to moving away from the source.

### Constants and numbers

$m^2=0.3,\ \alpha=1$: $\kappa_{\rm axis}=\operatorname{arcosh}(1.15)=\mathbf{0.5410973}$ (this is the corpus's `kappa_axis` benchmark, printed as $0.541097$).
$m^2=1,\ \alpha=1$ (the $d=2$ sanity-check point): $\kappa_{\rm axis}=\operatorname{arcosh}(1.5)=0.9624237$.
Mass scan at $\alpha=1$: $\kappa_{\rm axis}(m^2)=0.223144,\,0.314925,\,0.443568,\,0.541097,\,0.693147,\,0.962424$ for $m^2=0.05,0.10,0.20,0.30,0.50,1.00$.
Identity check at $L=16$, $d=4$: max block error $2.220\times10^{-16}$; $G_{00}(0)=0.9412344592$; $(m^2/2)G_{00}(0)=0.1412$.
Explicit axis values of the scalar propagator $G_{\rm sc}$ at $L=64$, $d=4$, $m^2=0.3$, $\alpha=1$ (used as the plateau ground truth): $G(0)=1.438676\times10^{-1}$, $G(1)=2.426262\times10^{-2}$, $G(2)=5.171072\times10^{-3}$, $G(4)=4.705547\times10^{-4}$, $G(8)=1.590082\times10^{-5}$, $G(12)=9.478656\times10^{-7}$, $G(16)=6.915410\times10^{-8}$, $G(20)=5.609209\times10^{-9}$, $G(24)=4.858703\times10^{-10}$.

### Code

`verify_ct_davies.py`, part C:

    P  = grids(L); tp = [np.exp(1j*P[mu]) - 1.0 for mu in range(d)]
    p2 = sum(np.abs(t)**2 for t in tp); p2s = np.where(p2 > 0, p2, 1.0)
    for mu in range(d):
        for nu in range(d):
            PL = np.where(p2 > 0, np.conj(tp[mu])*tp[nu]/p2s, (1.0 if mu == nu else 0.0))
            PT = (1.0 if mu == nu else 0.0) - PL
            G[mu,nu]  = np.fft.ifftn(PT/(m2 + alpha*p2) + PL/m2)                      # direct
            Q         = (p2 if mu == nu else 0.0) - np.conj(tp[mu])*tp[nu]            # Delta_1 symbol
            CF[mu,nu] = np.fft.ifftn((1.0/m2 if mu == nu else 0.0)
                                     - (alpha/m2)*Q/(m2 + alpha*p2))                  # closed form

Executed output:

    max |M^-1 - [ m^-2 I - (a/m^2) Delta_1 (m^2 + a Delta_sc)^-1 ]| = 2.220e-16
    G_00(0) = 0.9412344592 ;  (m^2/2)|G(0)| = 0.1412   <- corpus max-ratio 0.1412

Axis profile of $G_{\rm sc}$ at $L=64$ without materialising the $64^4$ grid (`verify_ct_davies.py`, part D2):

    k  = 2*np.pi*np.arange(L)/L; t1 = 2 - 2*np.cos(k)
    T3 = (t1[:,None,None] + t1[None,:,None] + t1[None,None,:]).ravel()
    S  = np.array([np.sum(1.0/(m2 + alpha*(a + T3))) for a in t1])     # partial sum over 3 momenta
    G  = np.array([np.sum(np.cos(k*r)*S) for r in range(L//2+1)]) / L**4

**Caveat.** Valid only for the abelian/free operator $M=m^2I+\alpha d_1^{*}d_1$ (the linear theory). In the non-abelian setting no such symbol exists and Theorems CT/D are the only available tools — which is precisely why they are worth keeping.

**Why it matters.** It supplies the ground truth against which every bound and every numerical estimator in this part of the corpus can be calibrated, replacing 'the bound is respected with slack' by a quantitative statement of how much is lost. It also shows that in the abelian case the whole Combes–Thomas apparatus is unnecessary — the answer is exact — and pins the sharpness ceiling: no conjugation bound can beat $\operatorname{arcosh}(1+m^2/2\alpha)$.

---

## 6. The level-set / boundary row-sum refinement C_∂ ≤ C_0: correct mechanism, no gain isotropically, 3× gain with a linear weight, sharp in 1-D

`status: solid` · `kind: theorem`

### Statement

**(a) General weighted Davies bound.** Let $M=m^2I+L$ as in Theorem D. For *any* real weight $\phi:V\to\mathbb R$ and any $\theta\ge0$, define
$$E(\phi,\theta):=\sup_{x\in V}\sum_{z\ne x}\bigl\|L_{xz}\bigr\|_{\rm op}\Bigl[\cosh\bigl(\theta(\phi(x)-\phi(z))\bigr)-1\Bigr].$$
Then whenever $E(\phi,\theta)<m^2$, for all $x,z_0$,
$$\bigl\|(M^{-1})_{xz_0}\bigr\|_{\rm op}\ \le\ \frac{1}{m^{2}-E(\phi,\theta)}\ e^{-\theta\,(\phi(x)-\phi(z_0))}.$$
Optimising over $(\phi,\theta)$ gives the best bound this method can produce.

**(b) Level-set form.** For a 1-Lipschitz integer-valued $\phi$ and a range-1 operator, $E(\phi,\theta)=(\cosh\theta-1)\cdot\sup_x\sum_{z:|\phi(x)-\phi(z)|=1}\|L_{xz}\|_{\rm op}$: *only couplings crossing a level set of $\phi$ are charged*. Taking $\phi=\mathrm{dist}(\cdot,z_0)$ recovers $C_\partial(L)\le C_0(L)$ of Theorem D.

**(c) Negative result for the isotropic weight.** For $L=\alpha\Delta_1$ on the $d=4$ periodic lattice with $\phi=\mathrm{dist}_E(\cdot,b_0)$,
$$C_\partial(\Delta_1)=C_0(\Delta_1)=18:$$
the refinement gives **no improvement**, because there exist links all $18$ of whose neighbours cross a level set. (The *typical* link has only $11$–$12$ crossing neighbours, but the Schur test needs the supremum.) The same phenomenon holds for the scalar Laplacian on $\mathbb Z^d$ with the $\ell^1$ metric: every one of the $2d$ neighbours crosses a level set of $|x|_1$, so $C_\partial=C_0=2d$.

**(d) Positive result for a linear weight.** Taking $\phi(b):=x_\mu(b)$, the $\mu$-coordinate of the base site — 1-Lipschitz for the link adjacency — gives
$$C(\phi=x_\mu)=6\quad\text{for }\Delta_1\text{ in }d=4\ \ (\text{a }3\times\text{ gain over }C_0=18),$$
and the resulting bound decays in $|x_\mu(b)-x_\mu(b')|$ with threshold $\theta^{*}=\operatorname{arcosh}(1+m^2/6\alpha)$.

**(e) Sharpness.** For the scalar massive Laplacian $m^2I+\alpha\Delta$ on $\mathbb Z^d$ with the linear weight $\phi(x)=x_1$, only the two neighbours $x\pm e_1$ cross a level set, so $E=2\alpha(\cosh\theta-1)$ and the threshold is
$$\theta^{*}=\operatorname{arcosh}\Bigl(1+\frac{m^{2}}{2\alpha}\Bigr)=\kappa_{\rm axis},$$
i.e. the level-set-refined Davies bound is **exactly sharp** in every coordinate direction, for every $d$.

### Derivation

Sources: `COMBES_THOMAS/MAXWELL_GREEN/davies_decay_massive_maxwell.md` §4 (the level-set version of $C_\partial$, correct); `02_davies_decay_maxwell_boundary_rowsum(1).md` §5 (a weaker set-based version $C_\partial(\mathcal S)=\sup_{b\in\mathcal S}\sum_{b'\notin\mathcal S}|K_{bb'}|$ with a vaguer corollary); Appendix A Definition A.9.4 and Appendix H Lemma H.3.3 (the version used in the proof). The corpus states $C_\partial\le C_0$ 'often strictly' and offers the slogan 'only couplings that cross distance level sets matter' as a general method; (a), (d), (e) below make that slogan precise and sharp, and (c) is a negative result I established.

**Proof of (a) and (b).** Repeat Steps 2–6 of the proof of Theorem D with the general weight $\phi$ in place of $\mathrm{dist}(\cdot,z_0)$. The only place the metric was used is the bound on $Q_\theta$, whose blocks are $(Q_\theta)_{xz}=[\cosh(\theta(\phi(x)-\phi(z)))-1]L_{xz}$; $Q_\theta$ is self-adjoint with zero diagonal, so the block Schur lemma gives $\|Q_\theta\|_{\rm op}\le E(\phi,\theta)$ directly. Step 6 becomes $\bigl(W_\theta M^{-1}W_\theta^{-1}\bigr)_{xz_0}=e^{\theta(\phi(x)-\phi(z_0))}(M^{-1})_{xz_0}$. For (b), if $\phi$ is integer-valued and 1-Lipschitz and $L$ has range 1, then $\phi(x)-\phi(z)\in\{-1,0,+1\}$ on the support of $L$, and $\cosh(0)-1=0$. $\square$

**Proof of (c) (computation).** I built $\Delta_1$ on $(\mathbb Z/6)^4$ (5184 links), ran BFS from a fixed link $b_0$ to get $\phi=\mathrm{dist}_E(\cdot,b_0)$, and for every link $b$ summed $|(\Delta_1)_{b\tilde b}|$ over neighbours with $|\phi(b)-\phi(\tilde b)|=1$. Distribution of that crossing row sum over the 5184 links ($L=6$; the $L=8$ run, 16384 links, is identical in shape):
$$\{6:5,\ 7:6,\ 8:18,\ 10:102,\ 11:2604,\ 12:2321,\ 14:102,\ 16:24,\ \mathbf{18:2}\}.$$
Two links (near the source, where the distance function has a cone point) have all 18 neighbours crossing, so $C_\partial=18=C_0$. The *median* is 12, so an argument that could use a typical rather than worst-case crossing count would gain a factor 1.5.

**Proof of (d) (computation + count).** With $\phi(b)=x_1$(base site of $b$), the crossing row sum takes only two values over the 5184 links: $\{4:3888,\ 6:1296\}$, so $C(\phi=x_1)=6$. Structurally: from $b=(x,\mu)$ the 18 neighbours are, for each $\nu\ne\mu$, the six links $(x,\nu),(x{+}e_\mu,\nu),(x{+}e_\nu,\mu),(x{-}e_\nu,\nu),(x{-}e_\nu{+}e_\mu,\nu),(x{-}e_\nu,\mu)$; their base sites differ from $x$ by $0,\pm e_\mu,\pm e_\nu$, and only those shifted along direction 1 change $\phi$. Counting: if $\mu=1$, the shifts $\pm e_\mu$ occur for two neighbours per $\nu$, giving 6; if $\mu\ne1$, the shifts $\pm e_\nu$ with $\nu=1$ give 4.

**Proof of (e).** For $L=\alpha\Delta$ (scalar) on $\mathbb Z^d$ and $\phi(x)=x_1$: $L_{x,x\pm e_\rho}=-\alpha$, and $\phi(x)-\phi(x\pm e_\rho)=\mp\delta_{\rho1}$. So $E(\phi,\theta)=2\alpha(\cosh\theta-1)$ and the admissibility condition $E<m^2$ reads $\cosh\theta<1+m^2/(2\alpha)$, whose supremum is exactly $\kappa_{\rm axis}$ from the closed-form item. Since the true kernel satisfies $|G(re_1)|\asymp r^{-(d-1)/2}e^{-\kappa_{\rm axis}r}$, no larger exponent is possible: the bound is sharp up to the polynomial prefactor (which the diverging constant $1/(m^2-E)$ accounts for as $\theta\uparrow\theta^{*}$). $\square$

**Practical upshot.** The right way to use the corpus's 'flux across level sets' idea is not the geodesic-sphere weight (which for isotropic stencils charges everything) but a **linear/anisotropic** weight, one direction at a time, then take the best direction. For $\Delta_1$ in $d=4$ at $m^2=0.3,\alpha=1$ this raises the achievable exponent from $0.182322$ (isotropic $\theta^{*}$, graph metric) to $0.314925$ (linear weight, coordinate metric) — within a factor $1.72$ of the exact $0.541097$, versus a factor $65$ for the corpus's published $\eta_{\rm CT}$.

### Constants and numbers

$\Delta_1$, $d=4$, $L=6$ (5184 links), $\phi=\mathrm{dist}_E(\cdot,b_0)$: crossing-row-sum histogram $\{6{:}5,7{:}6,8{:}18,10{:}102,11{:}2604,12{:}2321,14{:}102,16{:}24,18{:}2\}$; $C_\partial=18=C_0$; median $=12$.
$\Delta_1$, $d=4$, $\phi=x_1$: histogram $\{4{:}3888,\ 6{:}1296\}$; $C(\phi)=6$.
Resulting thresholds at $m^2=0.3$, $\alpha=1$: isotropic $\theta^{*}=0.182322$; linear-weight $\theta^{*}=0.314925$; exact $\kappa_{\rm axis}=0.541097$. Ratio to exact: $0.337$ vs $0.582$.
Scalar Laplacian on $\mathbb Z^d$, $\ell^1$ metric: $C_\partial=C_0=2d$ (no gain); linear weight: $C=2$ (sharp).
Small-mass loss factor of the isotropic $\ell^1$ bound versus the true axis rate: $\theta^{*}/\kappa_{\rm axis}\to1/\sqrt d$; measured at $d=4$, $m^2=0.05$: $0.111745/0.223144=0.5008$.

### Code

`verify_ct_davies.py`, part E:

    D1, links = build_Delta1(L=6)
    A = abs(D1).tolil(); A.setdiag(0); A = A.tocsr(); A.eliminate_zeros()
    # BFS from link 0 -> dist  (isotropic weight)
    for i in range(n):
        js = A.indices[A.indptr[i]:A.indptr[i+1]]; ws = A.data[A.indptr[i]:A.indptr[i+1]]
        Cb   = max(Cb,  ws[np.abs(dist[js] - dist[i]) == 1].sum())            # C_bdry
        dphi = np.array([((links[j][0][0] - links[i][0][0] + L//2) % L) - L//2 for j in js])
        Clin = max(Clin, ws[np.abs(dphi) == 1].sum())                          # linear weight x_1

Executed output:

    isotropic weight phi = dist_E(.,b0):  C_bdry = 18   (= C0 = 18, NO gain)
    linear    weight phi = x_1(base):     C(phi)  = 6   (3x gain over C0 = 18)

**Caveat.** Part (d) yields decay in the coordinate $|x_\mu(b)-x_\mu(b')|$, not in $\mathrm{dist}_E$; converting to the $\ell^1$/graph metric by $\|x\|_\infty\ge\|x\|_1/d$ throws the gain away, so the anisotropic bound is the better one only when a directional (e.g. Euclidean-time / reflection-positivity) statement is what is wanted — which is the case for OS reconstruction.

**Why it matters.** It converts the corpus's slogan ('only couplings crossing distance level sets matter') into a precise optimisation over weights, settles it negatively for the geodesic-sphere weight it was proposed with, and shows that the same idea with a linear weight is exactly sharp for the free massive lattice Laplacian and gives a clean $3\times$ gain for curl–curl. That is a usable, portable analytic device for any finite-range anisotropic operator.

---

## 7. FFT verification of exponential decay: shell-envelope mass scan and the prefactor-corrected κ plateau

`status: solid` · `kind: numerical_result`

### Statement

Exact (FFT-diagonalised, no Monte Carlo) decay diagnostics for the massive lattice propagator on $T^4$, $L=64$, $\alpha=1$, double precision, at six masses. Two estimators are compared against the exact $\kappa_{\rm axis}=\operatorname{arcosh}(1+m^2/2\alpha)$:

**(i) $\ell^1$-shell envelope slope.** $\mathrm{env}(r)=\max_{\|x\|_1=r}|G(x)|$, local slopes $s(r+\tfrac12)=\log\mathrm{env}(r)-\log\mathrm{env}(r+1)$, median over $r\in[6,20]$ (14 bins). Reproduces the corpus's table to all printed digits.

**(ii) Prefactor-corrected axis plateau.** Because $G(re_1)\sim A\,r^{-(d-1)/2}e^{-\kappa r}$, the estimator is the slope of $\log|G(r)|+\tfrac{d-1}{2}\log r$ against $r$. This is the only estimator in the corpus that recovers $\kappa_{\rm axis}$; the raw (uncorrected) slope over the same window overshoots by 20%.

**Headline calibration ($m^2=0.3$, $\alpha=1$, $d=4$):**
| quantity | value |
|---|---|
| exact $\kappa_{\rm axis}$ | 0.541097 |
| raw axis local slope at $r=15$ | 0.64957 (+20.0%) |
| prefactor-corrected LS fit, $r\in[10,28]$ | 0.544303 (+0.59%) |
| prefactor-corrected LS fit, $r\in[12,30]$ | 0.541772 (+0.12%) |
| prefactor-corrected LS fit, $r\in[14,31]$ | 0.536691 ($-$0.81%, wrap contamination) |
| $\ell^1$-shell envelope median, $r\in[6,20]$ | 0.390352 |
| rigorous $\eta_{\rm CT}$, $C_0=8$ | 0.018576 (21.0× too small) |
| rigorous $\theta^{*}$, $C_0=8$ | 0.273013 (1.43× too small) |

### Derivation

Sources of the original runs: `ARCHIVES/extracted_notebooks/Untitled122_extracted.py` (executed on an A100, torch, `device=cuda`, `d=4`, `L=64`, `m2=0.3`, `alpha=1.0`, stored outputs preserved) and `COMBES_THOMAS/MAXWELL_GREEN/03_greens_decay_combes_thomas.md` §4 (the six-mass table). I re-derived all of it independently in numpy on CPU; the agreement is exact, including a torch-vs-numpy median convention.

**Method (i).** $\widehat G(p)=1/(m^2+\alpha\sum_\rho(2-2\cos p_\rho))$ on the $64^4$ momentum grid, $G=\mathrm{ifftn}(\widehat G)$ in complex128; torus $\ell^1$ distance $\mathrm{dist}(x)=\sum_i\min(x_i,L-x_i)$; envelope by `np.maximum.at`; median of the 14 local slopes with mid-points in $[6,20]$.

Reproduced table ($L=64$, $d=4$, $\alpha=1$):
| $m^2$ | $c_{\rm shell}$ (median) | corpus value | $\eta_{\rm CT}=\log(1+m^2/16)$ | $\theta^{*}=\operatorname{arcosh}(1+m^2/8)$ | $\kappa_{\rm axis}$ |
|---|---|---|---|---|---|
| 0.05 | 0.227135 | 0.22713 | 0.003120 | 0.111745 | 0.223144 |
| 0.10 | 0.274889 | 0.27489 | 0.006231 | 0.157950 | 0.314925 |
| 0.20 | 0.343195 | 0.34319 | 0.012423 | 0.223144 | 0.443568 |
| 0.30 | 0.390352 | 0.39035 | 0.018576 | 0.273013 | 0.541097 |
| 0.50 | 0.454507 | 0.45451 | 0.030772 | 0.351737 | 0.693147 |
| 1.00 | 0.592375 | 0.59238 | 0.060625 | 0.494933 | 0.962424 |
The match is exact once one uses `torch.median`'s convention for an even sample (lower of the two middle values); with numpy's averaging convention the numbers are $0.232354,0.278604,0.344988,0.393031,0.462077,0.598807$, and the mean is $0.395472$ at $m^2=0.3$ — which is precisely the corpus's separately printed `c_shell mean = 0.395472`. Both statistics therefore reproduce.

*Reading of the table.* The corpus's conclusion — 'CT is safe but 10–75× too loose' — is confirmed for $\eta_{\rm CT}$ (ratios $72.8,44.1,27.6,21.0,14.8,9.8$). But the *same* method's sharp threshold $\theta^{*}$ (Theorem D(b), never evaluated in the corpus) is only $1.4$–$2.0\times$ below the measured envelope slope, and its ratio to $\kappa_{\rm axis}$ is $\to1/\sqrt d=1/2$: at $m^2=0.05$, $0.111745/0.223144=0.5008$. So the method is far better than the corpus's own numbers suggest.

**Method (ii).** For the axis profile I avoid materialising the $64^4$ array: partial-summing three momenta first,
$$S(p_1)=\sum_{p_2,p_3,p_4}\frac{1}{m^2+\alpha\sum_\rho(2-2\cos p_\rho)},\qquad G(re_1)=\frac{1}{L^4}\sum_{p_1}\cos(p_1r)\,S(p_1).$$
Local slopes of $\log|G|$ and of $\log|G|+\tfrac32\log r$ (executed, $m^2=0.3$):
| $r$ | $G(r)$ | raw slope | corrected slope |
|---|---|---|---|
| 4 | 4.705547e-04 | 1.09665 | 0.66513 |
| 8 | 1.590082e-05 | 0.76374 | 0.56344 |
| 12 | 9.478656e-07 | 0.67983 | 0.54931 |
| 15 | 1.314427e-07 | **0.64957** | 0.54608 |
| 20 | 5.609209e-09 | 0.62072 | 0.54378 |
| 24 | 4.858703e-10 | 0.60671 | 0.54287 |
| 28 | 4.439879e-11 | 0.59079 | 0.53624 |
| 31 | 9.711324e-12 | 0.41348 | 0.36429 (wrap) |
The raw slope at $r=15$ is $0.64957$, **exactly** the corpus's reported 'directional (tail-envelope) median slope, axis $(1,0,0,0)$: 0.64957' — an independent CPU/numpy reproduction of an A100/torch number. The corrected slope converges monotonically to $\kappa_{\rm axis}=0.541097$ from above with an $O(1/r^2)$ residual, then collapses past $r\approx28$ from torus wrap-around.

Least-squares fits of $\log|G|+\tfrac32\log r=a-\kappa r$:
$$[6,20]\!:0.549530,\quad[8,24]\!:0.546143,\quad[10,28]\!:0.544303,\quad[12,30]\!:0.541772,\quad[14,31]\!:0.536691.$$
The corpus's reported $\kappa_{\rm plateau}(\text{axis})=0.537792$ (deviation $-0.003305$ from $\kappa_{\rm axis}$) sits inside this window-sensitivity band, closest to the $[14,31]$ fit ($0.536691$, deviation $-0.004407$) — i.e. their window reached into the wrap-contaminated region. **Conclusion: the plateau method works, with a window-choice systematic of $\pm0.005$ ($\approx1\%$) at $L=64$; the correct window is $r\in[12,30]$, which gives $0.541772$, within $0.12\%$ of exact.**

**What the corpus's own 'bound check' actually tested.** `Untitled125_extracted.py` reports $\max_b\frac{m^2}{2}|G(b,b_0)|e^{\eta\,\mathrm{dist}_E(b,b_0)}\approx0.1412$ at $\mathrm{dist}=0$ for *all three* candidate $\eta$'s. I reproduce $0.1412$ exactly, and identify it as $\frac{m^2}{2}G_{00}(0)=0.15\times0.9412344592$: the statistic is attained at coincidence and is completely insensitive to $\eta$. It confirms the prefactor $2/m^2$, not the exponent. (The corpus notes this in `03_greens_decay_combes_thomas.md` §6.1.)

### Constants and numbers

Parameters: $d=4$, $L=64$ (torus $T^4$, $16\,777\,216$ sites), $\alpha=1.0$, float64/complex128, exact FFT inversion (no sampling error). Shell fit window $r\in[6,20]$, 14 bins; $L/2=32$ is the wrap radius per axis.
Six-mass shell table and comparisons: see the table in the derivation. $c_{\rm shell}/\eta_{\rm CT}=72.8,\,44.1,\,27.6,\,21.0,\,14.8,\,9.8$ for $m^2=0.05\ldots1.00$; $\theta^{*}/c_{\rm shell}=0.492,\,0.575,\,0.650,\,0.699,\,0.774,\,0.835$.
Axis, $m^2=0.3$: exact $0.541097$; raw slope at $r=15$: $0.64957$; corrected LS $[12,30]$: $0.541772$ ($+0.000675$); corpus plateau $0.537792$ ($-0.003305$).
Bound-check statistic: $\max$ ratio $=0.1412$ at distance 0, $=\frac{m^2}{2}G_{00}(0)$ with $G_{00}(0)=0.9412344592$ (at $L=16$).
Corpus's separate 'shell ratio' PASS ($03\_maxwell\_C0...$ §2): median shell ratio $0.3418$ vs $e^{-0.2777}=0.7575$ — a per-shell ratio test, distinct from the max-ratio test.
Also reproduced from `Untitled122`: at $L=32$, $d=4$, matrix-free PCG (not FFT), $K=(\Delta_1)^{R}$: $R=1$ gives $C_0=8$, $\eta_{\rm CT}=0.0185764$, measured $c_{\rm med}=0.440021$; $R=2$ gives $C_0=184$, $\eta_{\rm CT}=4.07\times10^{-4}$, $c_{\rm med}=0.232472$; $R=3$ gives $C_0=3392$, $\eta_{\rm CT}=1.474\times10^{-5}$, $c_{\rm med}=0.408776$ — i.e. $C_0$ grows and $\eta_{\rm CT}$ collapses like $1/R\cdot1/C_0$ while the measured slope stays $O(1)$, a clean demonstration of how badly the row-sum bound degrades for longer-range stencils.

### Code

`verify_ct_davies.py`, parts D1 and D2. Core of D1 (mass scan, ~1.4 GB peak, ~90 s):

    n = np.arange(L); t = 2 - 2*np.cos(2*np.pi*n/L)
    lam  = t[:,None,None,None] + t[None,:,None,None] + t[None,None,:,None] + t[None,None,None,:]
    dx   = np.minimum(n, (L-n) % L).astype(np.int16)
    dist = (dx[:,None,None,None] + dx[None,:,None,None]
            + dx[None,None,:,None] + dx[None,None,None,:]).astype(np.int16)
    g   = np.fft.ifftn((1.0/(m2 + alpha*lam)).astype(complex)).real
    env = np.zeros(d*(L//2)+1); np.maximum.at(env, dist.ravel(), np.abs(g).ravel())
    y   = np.log(np.maximum(env, 1e-300)); sl = -(y[1:]-y[:-1])
    mid = np.arange(0.5, 0.5+len(sl)); msk = (mid >= 6) & (mid <= 20)
    s = np.sort(sl[msk]); c_shell = s[len(s)//2 - 1]        # torch.median convention

Core of D2 (plateau, memory-light):

    y  = np.log(np.abs(Gax[1:])) + (d-1)/2*np.log(r[1:])     # prefactor correction
    A  = np.vstack([np.ones(m.sum()), -rr[m]]).T
    kappa = np.linalg.lstsq(A, y[m], rcond=None)[0][1]

Executed output:

     m^2   c_shell(median)  eta_CT=log(1+m2/16)  theta*=arcosh(1+m2/8)  kappa_axis
     0.05   0.227135         0.003120            0.111745           0.223144
     0.10   0.274889         0.006231            0.157950           0.314925
     0.20   0.343195         0.012423            0.223144           0.443568
     0.30   0.390352         0.018576            0.273013           0.541097
     0.50   0.454507         0.030772            0.351737           0.693147
     1.00   0.592375         0.060625            0.494933           0.962424
     exact kappa_axis = arcosh(1+m^2/2a) = 0.541097
     raw local slope at r=15 : 0.64957   <- corpus 0.64957
     corrected LS fit r in [ 6,20]: kappa = 0.549530 (dev +0.008433)
     corrected LS fit r in [10,28]: kappa = 0.544303 (dev +0.003206)
     corrected LS fit r in [12,30]: kappa = 0.541772 (dev +0.000675)
     corrected LS fit r in [14,31]: kappa = 0.536691 (dev -0.004407)

**Caveat.** These are free-field (quadratic-action) diagnostics: the propagator is diagonalised exactly in momentum space, so they test the *estimators* and the *bounds*, not any interacting or gauge-field physics.

**Why it matters.** It is the only place in this part of the corpus where a claimed number can be checked end-to-end, and it checks out to the last printed digit on independent hardware and software. It also converts 'the bound holds with slack' into a quantitative loss budget ($\eta_{\rm CT}$ off by 10–75×, $\eta_{\rm DG}$ by ~4×, sharp $\theta^{*}$ by 1.4–2×), and it validates the prefactor-corrected plateau as a $\sim1\%$-accurate mass estimator while showing the raw tail-envelope estimator is biased 20% high.

---

## 8. Gauge-fixing collapses the row-sum constant: C₀ = 18 → 2d = 8 in Feynman gauge

`status: solid` · `kind: construction`

### Statement

Add an exactness penalty to the Maxwell form on 1-cochains:
$$M_\xi:=m^2I+\alpha\,d_1^{*}d_1+\xi\,d_0d_0^{*},\qquad \xi>0,$$
whose quadratic form is $m^2\|A\|^2+\alpha\|d_1A\|^2+\xi\|d_0^{*}A\|^2$. In momentum space
$$\widehat{M_\xi}(p)=(m^2+\alpha\hat p^{\,2})P_T(p)+(m^2+\xi\hat p^{\,2})P_L(p).$$
At **$\xi=\alpha$ (Feynman gauge)** the projectors recombine, $\widehat{M_\alpha}(p)=(m^2+\alpha\hat p^{\,2})\,\mathrm{Id}$: the operator is $d$ decoupled copies of the scalar massive lattice Laplacian. Consequently
$$C_0\bigl(\alpha d_1^{*}d_1+\alpha d_0d_0^{*}\bigr)/\alpha=2d\ (=8\text{ in }d=4)\quad\text{versus}\quad C_0(d_1^{*}d_1)=6(d-1)\ (=18),$$
and the Davies exponents improve accordingly. Moreover the resulting bound is then *exactly sharp* in a coordinate direction (Theorem D(b) with $C_\partial=2$).

### Derivation

Source: `COMBES_THOMAS/EVIDENCE_SIMULATIONS/gauge_fixing_hodge_laplacian_constants.md` (best write-up) and `Untitled125_extracted.py` (executed).

*Algebra.* $d_1^{*}d_1+d_0d_0^{*}$ is the full Hodge Laplacian $\Delta^{\rm Hodge}_1$ on 1-cochains, whose symbol is $\hat p^{\,2}\mathrm{Id}$ because $\widehat{d_1^{*}d_1}=\hat p^{\,2}P_T$ and $\widehat{d_0d_0^{*}}=\hat p^{\,2}P_L$ with $P_T+P_L=\mathrm{Id}$. So at $\xi=\alpha$ the mixed-derivative terms $\overline{\tilde p_\mu}\tilde p_\nu$ cancel identically and the operator is block-diagonal in the Lorentz index with each block the scalar massive Laplacian.

*Row sum.* The scalar lattice Laplacian has diagonal $2d$ and $2d$ off-diagonal entries of modulus 1, so $C_0=2d$. In $d=4$, $C_0=8$ versus $18$ ungauged.

*Executed confirmation.* The corpus's script (`Untitled125_extracted.py`) rebuilds $Q_{\rm GF}=\alpha(\hat p^2\delta_{\mu\nu}-\hat p_\mu\hat p_\nu)+\xi\hat p_\mu\hat p_\nu$ at $\xi=\alpha$, inverse-FFTs it and computes the row sum, printing
$$\texttt{New C0 (Laplacian): 8.0000},\qquad \texttt{New Eta (Theory): 0.1933}.$$
Check: $\eta_{\rm DG}=2\operatorname{arsinh}\bigl(m/(2\sqrt{\alpha\cdot8})\bigr)=2\operatorname{arsinh}(0.0968246)=0.193348$. ✓ Note this FFT computation is *not* affected by the half-frequency artifact of the ungauged case: with $\xi=\alpha$ the offending $\hat p_\mu\hat p_\nu$ terms cancel exactly before the transform, leaving a genuine trigonometric polynomial. (This is itself corroborating evidence for the diagnosis of the artifact: the same code returns the exact answer as soon as the problematic terms are gone.)

*Interpretation.* The 'bad' constant for curl–curl is entirely an artifact of taking absolute values: the mixed-derivative couplings cancel in the quadratic form but not in $\sum|K_{bb'}|$. A gauge in which the stencil is diagonal makes the cancellation manifest.

*Caveat on what this buys.* $M_\xi\ne M$ as operators (they differ on the longitudinal sector), so this is not a bound on $M^{-1}$; it is a bound for a different, gauge-fixed operator. The corpus's proposal — prove functional inequalities gauge-fixed and then transfer to gauge-invariant observables — is stated but not carried out anywhere.

### Constants and numbers

$d=4$, $m^2=0.3$, $\alpha=\xi=1$ ($m=0.547723$):
| operator | $C_0$ | $\eta_{\rm CT}=\log(1+\tfrac{m^2}{2\alpha C_0})$ | $\eta_{\rm DG}=\operatorname{arcosh}(1+\tfrac{m^2}{2\alpha C_0})$ | $\theta^{*}=\operatorname{arcosh}(1+\tfrac{m^2}{\alpha C_0})$ |
|---|---|---|---|---|
| $\alpha d_1^{*}d_1$ (ungauged) | 18 | 0.008299 | 0.129010 | 0.182322 |
| $\alpha\Delta^{\rm Hodge}_1$ ($\xi=\alpha$) | 8 | 0.018576 | **0.193348** | 0.273013 |
| directional weight, either | 2 | 0.072321 | 0.384918 | **0.541097** $=\kappa_{\rm axis}$ |
Corpus's printed values: `New C0 (Laplacian): 8.0000`, `New Eta (Theory): 0.1933` — both confirmed.
General $d$: ungauged $C_0=6(d-1)$; Feynman gauge $C_0=2d$; ratio $3(d-1)/d\to3$.

### Code

From `ARCHIVES/extracted_notebooks/Untitled125_extracted.py` (stored output present in the notebook):

    xi = alpha                                    # Feynman gauge
    inv_trans = 1.0/(m2 + alpha*p2)
    inv_long  = 1.0/(m2 + xi   *p2)               # equals inv_trans when xi == alpha
    # M^{-1} = inv_trans*I + (inv_long - inv_trans)*P_L   ->  diagonal scalar propagators
    Q_GF = zeros(d,d,L,L,L,L)
    for mu: Q_GF[mu,mu] += alpha*p2
    for mu,nu: Q_GF[mu,nu] -= alpha*hatp[mu]*hatp[nu]     # curl-curl
    for mu,nu: Q_GF[mu,nu] += xi   *hatp[mu]*hatp[nu]     # grad-div  -> cancels at xi=alpha
    KDelta_GF = ifftn(Q_GF).real
    C0_GF = max_mu ( sum_{nu,x} |KDelta_GF[mu,nu,x]| - |KDelta_GF[mu,mu,0]| )
    eta_GF = 2*math.asinh(m/(2*math.sqrt(C0_GF)))

    # printed:  New C0 (Laplacian): 8.0000     New Eta (Theory): 0.1933

**Caveat.** $M_\xi\neq M$: the improvement is for a different (gauge-fixed) operator, and the transfer back to gauge-invariant observables is nowhere carried out in the corpus. As a statement about $C_0$ it is exact; as a step in a proof it is a proposal.

**Why it matters.** It correctly identifies *why* the curl–curl row-sum constant is bad — absolute values destroy the mixed-derivative cancellations that the quadratic form enjoys — and gives a concrete algebraic move that removes the problem, improving $\eta_{\rm DG}$ by $1.5\times$ and $\theta^{*}$ by $1.5\times$. It is also a clean independent corroboration of the $C_0=43.9$ artifact diagnosis.

---

## 9. Reproduction and verification code

`status: solid` · `kind: code`

### Statement

A single self-contained numpy+scipy script that verifies every quantitative claim above: the exact combinatorial constants of $\Delta_1$, the level-set/boundary constants, the exact reproduction and correction of the $C_0=43.9077$ artifact, the closed-form identity for the massive Maxwell Green kernel, and the FFT decay diagnostics (mass scan + $\kappa$ plateau).

### Derivation

The script is organised in five parts, each printing the corpus's originally reported number next to the independently computed one.

- **A** builds $d_1$ as a signed sparse incidence matrix on $(\mathbb Z/L)^4$ and reports $\mathrm{diag}(\Delta_1)$, $C_0(\Delta_1)$ (max and min over links) and $D_E$ at $L=4,5,6$.
- **E** BFSes the link graph and computes the level-set crossing row sums for the isotropic weight $\phi=\mathrm{dist}_E(\cdot,b_0)$ and for the linear weight $\phi=x_1$.
- **B** implements both FFT recipes for $C_0$ (the corpus's half-frequency + `.real` version, and the correct complex forward-difference version) at $L=8,\dots,32$.
- **C** builds the full $4\times4$ block Green kernel on $T^4$ ($L=16$) two ways — from $P_T/(m^2+\alpha\hat p^2)+P_L/m^2$ and from the closed form $m^{-2}I-\tfrac{\alpha}{m^2}\Delta_1(m^2+\alpha\Delta_{\rm sc})^{-1}$ — and reports the max difference.
- **D** runs the six-mass $\ell^1$-shell envelope scan at $L=64$ and the memory-light axis plateau fit.

Runtime ~2–3 minutes; peak RAM ~1.5 GB (part D1 materialises one $64^4$ complex array at a time). No GPU, no torch, no seeds — everything is deterministic linear algebra and exact FFT.

### Constants and numbers

Full executed output:

    == A. exact combinatorial constants for Delta_1 on T^4 ==
       L=4: diag=[6.], C0=max off-diag row-sum=18, min=18, D_E=max degree=18
       L=5: diag=[6.], C0=max off-diag row-sum=18, min=18, D_E=max degree=18
       L=6: diag=[6.], C0=max off-diag row-sum=18, min=18, D_E=max degree=18
    == E. level-set (boundary) row-sum constants, L=6 ==
       isotropic weight phi = dist_E(.,b0):  C_bdry = 18   (= C0 = 18, NO gain)
       linear    weight phi = x_1(base):     C(phi)  = 6   (3x gain over C0 = 18)
    == B. the FFT C0 artifact ==
       L=  8  corpus recipe =   29.7764   correct symbol = 18.000000
       L= 12  corpus recipe =   37.4119   correct symbol = 18.000000
       L= 16  corpus recipe =   43.9077   correct symbol = 18.000000
       L= 20  corpus recipe =   49.5511   correct symbol = 18.000000
       L= 24  corpus recipe =   54.5495   correct symbol = 18.000000
       L= 32  corpus recipe =   63.1373   correct symbol = 18.000000
    == C. exact closed form for the massive Maxwell Green kernel (L=16, d=4) ==
       max |M^-1 - [ m^-2 I - (a/m^2) Delta_1 (m^2 + a Delta_sc)^-1 ]| = 2.220e-16
       G_00(0) = 0.9412344592 ;  (m^2/2)|G(0)| = 0.1412   <- corpus max-ratio 0.1412
    == D1. shell-envelope mass scan, T^4, L=64, alpha=1, window r in [6,20] ==
        m^2   c_shell(median)  eta_CT=log(1+m2/16)  theta*=arcosh(1+m2/8)  kappa_axis
        0.05   0.227135         0.003120            0.111745           0.223144
        0.10   0.274889         0.006231            0.157950           0.314925
        0.20   0.343195         0.012423            0.223144           0.443568
        0.30   0.390352         0.018576            0.273013           0.541097
        0.50   0.454507         0.030772            0.351737           0.693147
        1.00   0.592375         0.060625            0.494933           0.962424
    == D2. prefactor-corrected kappa plateau on the axis (m^2=0.3, alpha=1) ==
       exact kappa_axis = arcosh(1+m^2/2a) = 0.541097
       raw local slope at r=15 : 0.64957   <- corpus 0.64957
       corrected LS fit r in [ 6,20]: kappa = 0.549530 (dev +0.008433)
       corrected LS fit r in [10,28]: kappa = 0.544303 (dev +0.003206)
       corrected LS fit r in [12,30]: kappa = 0.541772 (dev +0.000675)
       corrected LS fit r in [14,31]: kappa = 0.536691 (dev -0.004407)

### Code

File: `C:\Users\Alex\AppData\Local\Temp\claude\F--ANTIGRAVITY-antigravity-playground-scalar-cluster-proof\fd74385b-6527-446a-ae5a-90acb16ad82a\scratchpad\verify_ct_davies.py`. Run with `python verify_ct_davies.py` (numpy 2.3.5, scipy 1.17.1 tested). The five entry points are `partA_E()`, `partB()`, `partC()`, `partD()`; each is independent and can be run alone. The essential fragments are quoted in the `code` fields of the individual items above.

Corpus code that this cross-checks (all paths corpus-relative):
- `SIMULATIONS/sanity_check_maxwell_decay.py` — dense $d=2$ Green kernel + BFS + envelope fit; runs as-is, output quoted in the Theorem CT item.
- `ARCHIVES/extracted_notebooks/Untitled125_extracted.py` (from `COLAB_RUNS/04_misc_notebooks/Untitled125.ipynb`) — link-graph BFS, $D_E=18$, tensor Green kernel by FFT, the $C_0$ computation, the max-ratio bound check, and the Feynman-gauge experiment. Stored outputs preserved.
- `ARCHIVES/extracted_notebooks/Untitled122_extracted.py` (from `Untitled122.ipynb`) — the $T^4$ $L=64$ shell-envelope diagnostics, the directional tail-envelope slopes, and the matrix-free PCG $R$-power stress test. Stored outputs preserved.

**Caveat.** Part D1 allocates a $64^4$ complex128 array per mass value; on a memory-constrained machine reduce to $L=48$ (the shell medians shift by $<0.5\%$).

**Why it matters.** It makes the whole extraction independently checkable in one command, and it is the artefact that turns 'the corpus reports 43.9077' into 'the corpus's recipe reproducibly returns 43.9077, here is why, and here is the correct 18'.

---

## How these fit together

**Internal logical structure.** Theorem CT and Theorem D are the same conjugation argument differing only in *what norm is bounded*: CT bounds the full perturbation ($\|K_t\|\lesssim tRB_0$, linear in $t$), Davies bounds only the symmetric part ($\|Q_\lambda\|\lesssim\tfrac12\lambda^2C_\partial$, quadratic in $\lambda$). That single difference is the whole $m^2\to m$ improvement, and it is why the level-set constant $C_\partial$ is available at all: the vanishing factor $\cosh(0)-1$ only appears once you symmetrise. So items 2 and 5 are one theorem, and item 1 is its weaker, older sibling.

The chain of constants runs: $\nu_P=2(d-1)\Rightarrow D_E=3\nu_P=6(d-1)\Rightarrow C_0(\Delta_1)=D_E$ (equality, item 3) $\Rightarrow$ all exponents. Item 4 (the $43.9077$ artifact) breaks that chain in the corpus's numerics and is repaired here; item 7 (Feynman gauge) short-circuits it a different way, replacing $6(d-1)$ by $2d$, and independently corroborates item 4's diagnosis because the same buggy FFT code returns the exact answer once the offending mixed-derivative terms cancel. Item 5's linear-weight refinement gets to $C=6$ by a third route, and $C=2$ (one direction) is the common sharp limit of items 2, 5 and 6.

Item 6 (the closed form $M^{-1}=m^{-2}I-\tfrac{\alpha}{m^2}\Delta_1(m^2+\alpha\Delta_{\rm sc})^{-1}$) is the calibration spine: it makes $\kappa_{\rm axis}=\operatorname{arcosh}(1+m^2/2\alpha)$ exact, which is simultaneously (i) the ground truth for item 8's numerics, (ii) the ceiling no bound can exceed, and (iii) exactly the $C_\partial=2$ instance of Theorem D's threshold $\theta^*$ — so the sharpness of the Davies method in one dimension is not a coincidence but the same computation seen twice.

**Relation to the rest of the corpus.** This body of work is the *last* step of the corpus's intended pipeline: Haar-mass matrix hinge $\Rightarrow$ $M\succeq m_H^2 I$ (`CURATED_01_HaarMass_MatrixHinge.md`) $\Rightarrow$ Helffer–Sjöstrand covariance representation ($\mathrm{Cov}\lesssim\langle\nabla F,M^{-1}\nabla G\rangle$, `04_Helffer_Sjostrand_Covariance.md`) $\Rightarrow$ **[this work]** kernel decay of $M^{-1}$ $\Rightarrow$ exponential clustering $\Rightarrow$ OS reconstruction $\Rightarrow$ Hamiltonian gap. Every earlier link in that chain is flagged elsewhere in the corpus as broken (the pointwise-vs-average good-set mismatch in the typicality step; the horizontal restriction at non-vacuum configurations; the uniform Bakry–Émery bound that vanishes along the asymptotically free trajectory). What is extracted here is the one link that is unconditionally true and volume-uniform — which is exactly why it is worth preserving separately from the pipeline it was built for.

The constants $D_E$, $\nu_P$, $C_0$, $C_\partial$ are Appendix A objects shared with the Hodge/gauge-fixing notes (`MAXWELL/`), the Helffer–Sjöstrand covariance notes (`HELFFER_SJOSTRAND/`) and the OS-bridge notes (`COMBES_THOMAS/OS_REFLECTION_POSITIVITY/`). Fixing $C_0(\Delta_1)=18$ therefore propagates to every quantitative statement in those folders that quotes $43.9077$.

**Duplication map** (for anyone returning to the sources): the Combes–Thomas lemma appears in at least seven files (`CURATED_02`, `EXCITING_03` ×3 copies, `03/05/06_combes_thomas_inverse_decay.md`, `Core_7`, `Synthesis_16`) — Appendix G is the only one with a proved Schur step. The Davies lemma appears in at least six (`davies_decay_massive_maxwell.md`, `02_davies_decay_row_sum_constants.md`, `02_davies_decay_maxwell_boundary_rowsum.md` ×2, `01_Davies_Maxwell_Green_Decay.md`, `24_Davies_Resolvent_Decay.md`) — Appendix H is the only one with the full one-parameter family and the correct $C_\partial$ from the start. `24_Davies_Resolvent_Decay.md` should not be used: it garbles $D_E$ ("$6\times4-2=22$ approx? Actually formulated in source as $D_E\approx6$") and carries a stray factor 2 in the perturbation bound. `03_maxwell_C0_decay_and_kappa_plateau.md` is duplicated verbatim in five folders (`MAXWELL/01_maxwell_core/`, `MAXWELL/Decay_Estimates/`, `LYAPUNOV/Maxwell_Covariance/`, `SIMULATIONS/`, plus the original).

## Further material found but not fully extracted

Things I found in this area but did not extract in full:

1. **`COMBES_THOMAS/MAXWELL_GREEN/EXTRACT_01_massive_maxwell_hs_clustering.md` and `02_hs_covariance_massive_maxwell.md`** — the Helffer–Sjöstrand step that consumes the kernel bound. This is the adjacent topic and where the decay bound actually gets used; it deserves its own extraction pass.

2. **`ARCHIVES/extracted_notebooks/Untitled122_extracted.py`, lines ~2280–2600 and ~3300–4200** — a second family of executed diagnostics I only sampled: a 3-D torus cochain complex built with explicit `build_ops_3d_torus` ($d_0,d_1$, harmonic-flow projection, CG solve at $L=24$, $n_1=41472$, giving `c_local median = 0.523138` vs `c_pred = 0.541097`, a 3.3% agreement), plus a "predictor (no knobs)" section that chooses a per-radius power $k$ from exponent+prefactor and a `kappa_k(m2,alpha,k)` directional-dispersion function with a full `dir/k/step_L1/kappa_step/kappa_L1/cL1(nmin=...)` table. That table looks like a genuine attempt at direction-resolved lattice dispersion and I did not mine it.

3. **`COMBES_THOMAS/MAXWELL_GREEN/05_simulation_appendix_maxwell_and_a100_su2.md`** (19 KB) — the fullest simulation appendix, containing the Feynman-gauge experiment plus an A100 SU(2) workload I did not look at.

4. **`COMBES_THOMAS/MAXWELL_GREEN/massive_maxwell_mass_scan.md`** — a Langevin mass-extraction scan. The corpus's own critical pass already established that its extractor $m_R=\sqrt{\text{intercept}/\text{slope}}\cdot\sqrt{m^2_{\rm bare}}$ fails its one hard sanity check (returns $0.1532$ at $\lambda=0$ where the exact answer is $0.5477$). Worth noting that the closed form in my item 6 gives the exact free-field answer against which that scan could be recalibrated: $\kappa_{\rm axis}=\operatorname{arcosh}(1+m^2_{\rm bare}/2\alpha)$, i.e. $0.541097$ at $m^2=0.3$, not $\sqrt{m^2}=0.5477$ — the two differ by 1.2% and the scan conflates them.

5. **`COMBES_THOMAS/RICCATI_RG/Riccati_Flux_Derivation_of_Exponential_Kernel_Decay.md`** — a proposed third decay engine via a surface-flux identity $dE/dr=2F(r)$ and a Riccati inequality $g'+g^2\ge\alpha^2$ on distance shells. As the corpus's own critical pass notes, the comparison step is invalid as written ($g\equiv-\alpha$ solves the inequality, so an initial-condition argument is needed and is absent). I did not attempt to repair it; if repaired it would be the discrete analogue of the classical Agmon/Carleman weighted estimate, which is a known route to the same $O(m)$ exponent and would be a genuine third proof.

6. **The Appendix G/H "horizontal restriction" interface** (Propositions G.4.2, H.4.2) — the claim that the kernel bound transfers to the horizontal sector $\ker(d_0^*)$. This is correct *at the vacuum* (where $M$ preserves $\ker d_0^*$), and the corpus's `05_projection_inversion_safety_lemma.md` derives the exact Schur-complement obstruction $PM^{-1}P-(PMP)^{-1}=A^{-1}B(C-B^*A^{-1}B)^{-1}B^*A^{-1}\succeq0$ that governs the general case. That identity is real mathematics and is the right object for anyone wanting to make the restriction step honest; I did not extract it.

7. **`COMBES_THOMAS/MAXWELL_GREEN/maxwell_inverse_decay_L12_d2.png`** — the plot produced by `sanity_check_maxwell_decay.py`; regenerable by running the script.
