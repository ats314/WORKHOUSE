---
id: EX-011
title: "The matrix hinge → Helffer–Sjöstrand → Combes–Thomas/Davies → exponential clustering → OS Hamiltonian gap chain for lattice Yang–Mills at fixed cutoff"
kind: extraction
items: 12
status_breakdown: {"solid": 8, "conditional": 4}
program: yang_mills
extracted_by: claude-opus-5 subagent, 2026-09-01
stance: preservation (content extraction, not refereeing)
source_files:
  - HELFFER_SJOSTRAND/04_Decay_Localization_OS/Core_5__Local_Coercivity_and_Matrix_Hinge_on_Good_Set(1).md
  - HELFFER_SJOSTRAND/02_Helffer_Sjostrand_Covariance/Appendix_F__Helffer_Sjostrand_Covariance(2).md
  - COMBES_THOMAS/COMBES_THOMAS_BOUNDS/Appendix_G__Combes_Thomas_Finite_Range_Inverse_Decay(1).md
  - MAXWELL/Decay_Estimates/Appendix_H__Davies_Type_Decay_Massive_Maxwell_Green_Kernel(1).md
  - REFLECTION_POSITIVITY/01_OS_RECONSTRUCTION/Appendix_L__OS_Reconstruction_and_Gap_Extraction(1).md
  - HELFFER_SJOSTRAND/04_Decay_Localization_OS/Core_6__Conditional_Covariance_Bound_via_HS_and_Hinge.md
  - COMBES_THOMAS/COMBES_THOMAS_BOUNDS/Core_7__Conditioned_Exponential_Clustering_via_Inverse_Decay.md
  - LSI_POINCARE/08_misc_docs/Core_8__Localization_and_Transfer_to_Infinite_Volume.md
  - RICCATI/04_misc_docs/Core_9__Thermodynamic_Limit_and_OS_Gap_at_Fixed_Cutoff.md
  - HESSIAN/Core_Hessian/Appendix_D__Wilson_Action_Vacuum_Expansion_and_Hessian.md
  - COMBES_THOMAS/DUPLICATES/Appendix_A__Notation_and_Constants(1).md
  - TENSOR_NETWORK/06_LATTICE_QCD_SECTORS/Appendix_B__Lattice_Cell_Complex_and_Cochains.md
  - HELFFER_SJOSTRAND/01_Matrix_Hinge_Convexity/EXCITING_01_MATRIX_HINGE(1).md
  - LSI_POINCARE/archive/Appendix_I__Localization_Algebra(1).md
  - REFLECTION_POSITIVITY/02_RP_FUNDAMENTALS/Appendix_K__Reflection_Positivity_for_Wilson(1).md
  - HELFFER_SJOSTRAND/02_Helffer_Sjostrand_Covariance/04_helffer_sjostrand_and_greens_decay.md
  - HELFFER_SJOSTRAND/04_Decay_Localization_OS/BEST_05_Lattice_Mass_Gap_Pipeline_from_Hinge_to_OS.md
  - WILSON/01_core_theorems/YM_MatrixHinge_to_MassGap.md
  - HELFFER_SJOSTRAND/01_Matrix_Hinge_Convexity/01_fixed_cutoff_engine.md
  - _EXTRACT_FOR_LLM/02_candidates/CAND-004-quantitative-no-go-the-haar-ricci-hinge-mass-is-a-cutoff-sca.md
---

# The matrix hinge → Helffer–Sjöstrand → Combes–Thomas/Davies → exponential clustering → OS Hamiltonian gap chain for lattice Yang–Mills at fixed cutoff

> A complete, correctly-hypothesised conditional theorem chain at fixed lattice spacing — vacuum Hessian = discrete Maxwell operator, matrix hinge on a good set, Helffer–Sjöstrand covariance, Combes–Thomas/Davies kernel decay, exponential clustering, OS reconstruction to gap(H) ≥ η/a — together with a decisive counterexample showing the corpus's kernel-form step does not follow, a repair (Combes–Thomas applied directly to the Witten Laplacian on 1-forms) that restores the same constants, all explicit constants (κ_G = N/2, m_H² = N/6, α_W = β/n, C₀(d₁*d₁) = 18 exactly in d=4), and two obstructions showing the chain's good-set and continuum hypotheses cannot both hold.

**12 extracted items** — 4 conditional, 8 solid

---

## 1. Setting, notation and the constants ledger (Appendix A, reconstructed and verified)

`status: solid` · `kind: definition`

### Statement

Fix $d=4$, $\mathsf I_d=\{0,1,2,3\}$ with $0$ the Euclidean time direction, and a lattice spacing $a\in(0,\infty)$. Let $\Lambda_L=\prod_{\mu}(\mathbb Z/L_\mu\mathbb Z)$ be a finite periodic lattice, $V(\Lambda_L)=\Lambda_L$, $E(\Lambda_L)=\{(x,\mu)\}$ the positively oriented links (from $x$ to $x+\hat e_\mu$), $P(\Lambda_L)=\{(x;\mu,\nu):\mu<\nu\}$ the oriented plaquettes, with signed boundary $\partial p=(x,\mu)+(x+\hat e_\mu,\nu)-(x+\hat e_\nu,\mu)-(x,\nu)$ and incidence coefficients $\sigma_{p,b}\in\{-1,0,+1\}$.

**Group data.** $G$ compact Lie, $\mathfrak g=T_{\mathbf 1}G$, $\rho:G\to U(n)$ a fixed faithful unitary representation, $d\rho:\mathfrak g\to\mathfrak u(n)$. Inner product $\langle X,Y\rangle_{\mathfrak g}:=B_\rho(X,Y):=-\Re\operatorname{Tr}(d\rho(X)d\rho(Y))$ (positive definite by faithfulness); $g_G$ the bi-invariant metric obtained by translating it; $\iota_G$ the injectivity radius at $\mathbf 1$; $\kappa_G>0$ the Ricci floor, $\mathrm{Ric}_G\succeq\kappa_G\, g_G$.

**Configuration space.** $\mathcal M_{\Lambda_L}:=G^{E(\Lambda_L)}$ with the product metric $g_{\Lambda_L}=\bigoplus_b g_G$. Right-trivialization $\omega_U^R:T_U\mathcal M_{\Lambda_L}\to\mathfrak g^{E(\Lambda_L)}\equiv\mathcal C^1(\Lambda_L;\mathfrak g)$, $(\omega^R_UV)_b=(dR_{U_b^{-1}})(V_b)$, inverse $\tau^R_U$.

**Cochains.** $\mathcal C^0=\mathfrak g^{V}$, $\mathcal C^1=\mathfrak g^{E}$, $\mathcal C^2=\mathfrak g^{P}$ with $\ell^2$ inner products; $(d_0\varphi)_{(x,\mu)}=\varphi_{x+\hat e_\mu}-\varphi_x$, $(d_1X)_p=\sum_b\sigma_{p,b}X_b$, adjoints $d_0^*,d_1^*$; $\mathsf M_1:=d_1^*d_1$.

**Action.** $U_p(U)=U_{x,\mu}U_{x+\hat e_\mu,\nu}U^{-1}_{x+\hat e_\nu,\mu}U^{-1}_{x,\nu}$; $\Phi_\beta(V)=\beta(1-\tfrac1n\Re\operatorname{Tr}\rho(V))$; $S_{\Lambda_L,\beta}=\sum_p\Phi_\beta(U_p)$; $\mu_{\Lambda_L,\beta}(dU)=Z^{-1}e^{-S}\,\mathrm{vol}_{g_{\Lambda_L}}(dU)$; vacuum $U^{(0)}_b=\mathbf 1$.

**Named constants.**
$m_\partial:=4$ (links per plaquette); $\nu_P:=\sup_b\#\{p:\sigma_{p,b}\neq0\}$; $D_E:=$ max degree of the link-adjacency graph ($b\sim b'$ iff some plaquette boundary contains both); $\mathrm{dist}_E$ the induced graph distance; $r_{\log}=\iota_G/2$, $r_{\mathrm{sf}}=\min\{r_{\log},r_{\mathrm{BCH}},r_{\mathrm{Tr}}\}/4$; $m_H^2:=\kappa_G/3$; $\alpha_W:=\beta/n$; $M_{\Lambda_L}:=m_H^2\mathrm{Id}+\alpha_W\mathsf M_1$; $C_0(\mathsf M_1):=\sup_b\sum_{b'\ne b}\|(\mathsf M_1)_{bb'}\|_{\mathrm{op}}$.

**Combes–Thomas parameters.** For self-adjoint $A$ on $\ell^2(V;\mathsf H_0)$: $a_0(A)=\max\{a:A\succeq aI\}$, $R(A)=\min\{R:A_{xy}=0\ \text{if}\ \mathrm{dist}(x,y)>R\}$, $B_0(A)=\sup_x\sum_{y\ne x}\|A_{xy}\|_{\mathrm{op}}$, and $\eta_{\mathrm{CT}}(A):=R(A)^{-1}\log\!\big(1+\tfrac{a_0(A)}{2B_0(A)}\big)$.

### Derivation

Everything above is definitional except four quantitative facts, which I verified.

**(a) $\nu_P=2(d-1)=6$ and $D_E=3\nu_P=18$ in $d=4$, and $C_0(\mathsf M_1)=18$ exactly.**
A link $b=(x,\mu)$ lies in $\partial p$ exactly for $p=(x;\mu,\nu)$ and $p=(x-\hat e_\nu;\mu,\nu)$, $\nu\ne\mu$: $2(d-1)=6$ plaquettes. By Lemma B.4.4 of the corpus, $(\mathsf M_1)_{bb'}=\big(\sum_p\sigma_{p,b}\sigma_{p,b'}\big)\mathrm{Id}_{\mathfrak g}$ — every block is a *scalar* multiple of the identity. Proof: $(\mathsf M_1X)_b=\sum_p\sigma_{p,b}(d_1X)_p=\sum_{b'}\big(\sum_p\sigma_{p,b}\sigma_{p,b'}\big)X_{b'}$.
Two distinct links share **at most one** plaquette in the hypercubic lattice: if $b=(x,\mu)$, $b'=(x,\nu)$ ($\mu\ne\nu$) the only common plaquette is $(x;\mu\wedge\nu,\mu\vee\nu)$; if $b,b'$ are parallel and offset by $\pm\hat e_\nu$ the only common plaquette is the one spanned by $(\mu,\nu)$ at the appropriate corner; otherwise none. Hence $|\sum_p\sigma_{p,b}\sigma_{p,b'}|\in\{0,1\}$ for $b\ne b'$, and there is no cancellation. Each of the $\nu_P=6$ plaquettes containing $b$ contributes $m_\partial-1=3$ distinct partners, and these $18$ partners are pairwise distinct (two plaquettes containing $b$ meet only in $b$). Therefore
$$C_0(\mathsf M_1)=D_E=3\nu_P=18\quad(d=4),$$
so the corpus's bound $C_0\le 3\nu_P$ (Lemma B.4.6) is an **equality**, not an inequality. Also $(\mathsf M_1)_{bb}=\nu_P\,\mathrm{Id}=6\,\mathrm{Id}$, and $R(\mathsf M_1)=1$ in $\mathrm{dist}_E$. I verified all of this by explicit construction of $d_1$ in $d=2,3,4$ (code below): $C_0=6,12,18$ and $\mathrm{diag}=2,4,6$, all row sums *constant*, all off-diagonal entries $\pm1$.

**(b) $\kappa_G=N/2$ for $G=\mathrm{SU}(N)$ in this normalization.** [reconstructed]
With $\rho$ the fundamental, $\langle X,Y\rangle_{\mathfrak g}=-\Re\operatorname{Tr}(XY)=-\operatorname{Tr}(XY)$ on $\mathfrak{su}(N)$. For a bi-invariant metric on a compact group, $\mathrm{Ric}(X,X)=\tfrac14\sum_i|[X,e_i]|^2=-\tfrac14 B(X,X)$ with $B$ the Killing form; for $\mathfrak{su}(N)$, $B(X,Y)=2N\operatorname{Tr}(XY)$. Hence $\mathrm{Ric}(X,X)=\tfrac{N}{2}\langle X,X\rangle$, i.e.
$$\boxed{\kappa_G=N/2,\qquad m_H^2=\kappa_G/3=N/6.}$$
Numerically verified via $\tfrac14\sum_i|[e_a,e_i]|^2$ on orthonormal bases: $\mathrm{SU}(2)\to 1.0$, $\mathrm{SU}(3)\to 1.5$, $\mathrm{SU}(4)\to 2.0$ (code below).

**(c) The Haar/Jacobian identity $\nabla^2S_H(0)=\tfrac{\kappa_G}{3}\mathrm{Id}$ (Lemma A.8.2) is exact, not just an inequality.** [reconstructed]
$(\exp_G)^*\mathrm{vol}_{g_G}=J_G(X)dX$ with $J_G(X)=\det\!\big(\tfrac{1-e^{-\mathrm{ad}_X}}{\mathrm{ad}_X}\big)$. The eigenvalues of $\mathrm{ad}_X$ come in pairs $\pm i a_j$ plus zeros; each pair contributes $\frac{|1-e^{ia_j}|^2}{a_j^2}=\big(\frac{\sin(a_j/2)}{a_j/2}\big)^2$. Hence $S_H(X)=-\log J_G=-2\sum_j\log\frac{\sin(a_j/2)}{a_j/2}=\tfrac1{12}\sum_ja_j^2+O(|X|^4)$. Since $\sum_{\text{all eigen}}\lambda^2=\operatorname{Tr}(\mathrm{ad}_X^2)=B(X,X)=-2\sum_ja_j^2$ and $-B(X,X)=4\,\mathrm{Ric}(X,X)=4\kappa_G|X|^2$, one gets $\sum_ja_j^2=2\kappa_G|X|^2$ and $S_H(X)=\tfrac{\kappa_G}{6}|X|^2+O(|X|^4)$, so $\nabla^2S_H(0)[X,X]=2\cdot\tfrac{\kappa_G}{6}|X|^2=\tfrac{\kappa_G}{3}|X|^2$.
**Normalization warning (this matters).** $\nabla^2 S_H(0)$ and $\mathrm{Ric}_{g_\Lambda}\succeq\kappa_G$ are *two representations of the same curvature*, not two additive contributions: in the Bakry–Émery formulation $\mathrm{Ric}_\mu=\mathrm{Ric}_{g}+\nabla^2S$ with $S$ the **Wilson action only** (Haar is the reference measure), whereas in flat exponential coordinates the Jacobian appears as a potential and the Ricci term does not. Core-5 correctly uses only $\mathrm{Ric}_{g_\Lambda}\succeq\kappa_G\,\mathrm{Id}=3m_H^2\,\mathrm{Id}$; several survey/guide files in the corpus (e.g. `MAXWELL/00_FOLDER_GUIDE.md`, quoted in CAND-004 as "Total curvature $\succeq(1/6)\mathbf 1+(\beta/N)d_1^*d_1$") add the two and double-count. Use $\mathrm{Ric}_{g_\Lambda}\succeq\kappa_G$ only.

**(d) $\alpha_W=\beta/n$ is forced by the trace normalization** — see the vacuum Hessian item.

### Constants and numbers

d = 4; m_∂ = 4; ν_P = 2(d−1) = 6; D_E = 3ν_P = 18; C₀(M₁) = 18 EXACTLY (verified: d=2→6, d=3→12, d=4→18; diagonal blocks ν_P·Id = 6·Id in d=4; all off-diagonal blocks ±1·Id_g); R(M₁) = 1 in dist_E.
κ_G = N/2 for SU(N) with ⟨X,Y⟩ = −Tr(XY) (verified numerically: SU(2)=1.0, SU(3)=1.5, SU(4)=2.0).
m_H² = κ_G/3 = N/6: SU(2) → 1/3, SU(3) → 1/2.
α_W = β/n = β/N; with β = 2N/g², α_W = 2/g² independent of N.
SU(2), β=2.5: α_W = 1.25, m_H² = 0.3333. SU(3), β=6 (g²=1): α_W = 2, m_H² = 0.5.
Injectivity radius SU(2) in this metric: geodesic exp(t·iσ₃/√2) closes at t = 2√2π ≈ 8.886, so ι_G = √2π ≈ 4.443, r_log ≈ 2.22, r_sf ≤ 0.555.
∇²S_H(0) = (κ_G/3)Id exactly.

### Code

# Verifies C_0(M_1) = D_E = 3*nu_P exactly, and kappa_G = N/2.
# Run: python this_file.py   (numpy only)
import numpy as np

def build_d1(L, d):
    pts = [tuple(np.unravel_index(i, (L,)*d)) for i in range(L**d)]
    eidx = {}
    for x in pts:
        for mu in range(d): eidx[(x, mu)] = len(eidx)
    plaqs = [(x, mu, nu) for x in pts for mu in range(d) for nu in range(mu+1, d)]
    D1 = np.zeros((len(plaqs), len(eidx)))
    sh = lambda x, mu: tuple((x[i] + (i == mu)) % L for i in range(d))
    for k, (x, mu, nu) in enumerate(plaqs):
        D1[k, eidx[(x, mu)]]        += 1
        D1[k, eidx[(sh(x, mu), nu)]] += 1
        D1[k, eidx[(sh(x, nu), mu)]] -= 1
        D1[k, eidx[(x, nu)]]        -= 1
    return D1, eidx

for d, L in ((2,6), (3,6), (4,4)):
    D1, _ = build_d1(L, d); K = D1.T @ D1
    off = np.abs(K) - np.diag(np.abs(np.diag(K)))
    print(f"d={d}: diag={set(np.diag(K))}, C_0={off.sum(1).max():.0f}, "
          f"D_E={(off>0).sum(1).max():.0f}, max|off entry|={off.max():.0f}")
# d=2: diag={2.0}, C_0=6,  D_E=6,  max=1
# d=3: diag={4.0}, C_0=12, D_E=12, max=1
# d=4: diag={6.0}, C_0=18, D_E=18, max=1

def su_basis(N):
    B = []
    for a in range(N):
        for b in range(a+1, N):
            E = np.zeros((N,N), complex); E[a,b]=E[b,a]=1;  B.append(1j*E/np.sqrt(2))
            F = np.zeros((N,N), complex); F[a,b]=1; F[b,a]=-1; B.append(F/np.sqrt(2))
    for k in range(1, N):
        dg = np.zeros(N); dg[:k] = 1; dg[k] = -k
        B.append(1j*np.diag(dg).astype(complex)/np.sqrt(k*(k+1)))
    return B

ip = lambda X, Y: np.real(-np.trace(X @ Y))
for N in (2,3,4):
    B = su_basis(N)
    assert np.allclose([[ip(X,Y) for Y in B] for X in B], np.eye(len(B)))
    ric = [sum(ip(X@e-e@X, X@e-e@X) for e in B)/4 for X in B]
    print(f"SU({N}): Ric = {set(np.round(ric,10))}, predicted N/2 = {N/2}")
# SU(2): 1.0 ; SU(3): 1.5 ; SU(4): 2.0

**Caveat.** The corpus is internally inconsistent about whether the Haar-Jacobian Hessian and the Riemannian Ricci floor are the same object; several survey files add them. Use Ric_{g_Λ} ⪰ κ_G only. The bound C₀ ≤ 3ν_P is tight (equality), so no improvement is available there.

**Why it matters.** Every quantitative statement downstream (the hinge, the decay rate, the certified gap) is a rational expression in exactly these constants. Pinning C₀ = 18 exactly and κ_G = N/2 makes the whole chain numerically evaluable rather than schematic, and exposes the double-counting error that inflates m_H² in parts of the corpus.

---

## 2. Vacuum Hessian identity: ∇²S_{Λ,β}(U⁽⁰⁾) = α_W d₁*d₁ on C¹(Λ;g)

`status: solid` · `kind: theorem`

### Statement

Let $\Lambda_L$ be a finite periodic lattice, $G$ compact with bi-invariant $g_G$ induced by $\langle X,Y\rangle_{\mathfrak g}=-\Re\operatorname{Tr}(d\rho(X)d\rho(Y))$, and $S_{\Lambda_L,\beta}=\sum_{p}\Phi_\beta(U_p)$ the Wilson action, $\Phi_\beta(V)=\beta(1-\tfrac1n\Re\operatorname{Tr}\rho(V))$. Then, under the identification $T_{U^{(0)}}\mathcal M_{\Lambda_L}\cong\mathcal C^1(\Lambda_L;\mathfrak g)$ by right-trivialization,
$$\nabla S_{\Lambda_L,\beta}(U^{(0)})=0,\qquad \nabla^2S_{\Lambda_L,\beta}(U^{(0)})=\alpha_W\,d_1^*d_1,\qquad \alpha_W=\frac{\beta}{n},$$
as self-adjoint operators on $\mathcal C^1(\Lambda_L;\mathfrak g)$; equivalently $\nabla^2S(U^{(0)})[X,Z]=\alpha_W\langle d_1X,d_1Z\rangle_{\mathcal C^2}$ for all $X,Z\in\mathcal C^1$.

### Derivation

Full reproduction of Appendix D (`HESSIAN/Core_Hessian/Appendix_D__Wilson_Action_Vacuum_Expansion_and_Hessian.md`), which is complete and correct.

**Step 1 (geodesics through the vacuum).** For $X\in\mathcal C^1$ define $\gamma_X(t)_b:=\exp(tX_b)$. On a compact group with bi-invariant metric every one-parameter subgroup is a geodesic; the product metric makes $\gamma_X$ a geodesic in $\mathcal M_{\Lambda_L}$, with $\omega^R_{U^{(0)}}(\dot\gamma_X(0))=X$ (right-trivialization is componentwise and equals the identity at $\mathbf 1$).

**Step 2 (linearization of the plaquette holonomy is exactly $d_1$).** Differentiating $g(t)g(t)^{-1}=\mathbf 1$ at $t=0$ with $g(0)=\mathbf 1$ gives $\frac{d}{dt}\big|_0 g(t)^{-1}=-\dot g(0)$. For $p=(x;\mu,\nu)$, $\mathrm{Hol}_p(U)=U_{x,\mu}U_{x+\hat e_\mu,\nu}U^{-1}_{x+\hat e_\nu,\mu}U^{-1}_{x,\nu}$; along $\gamma_X$ every factor equals $\mathbf 1$ at $t=0$, so the derivative of the product is the sum of factor derivatives with a minus sign on inverted factors:
$$\frac{d}{dt}\Big|_{0}\mathrm{Hol}_p(\gamma_X(t))=X_{x,\mu}+X_{x+\hat e_\mu,\nu}-X_{x+\hat e_\nu,\mu}-X_{x,\nu}=(d_1X)_p .$$
This is exactly $\sum_b\sigma_{p,b}X_b$ by the boundary convention. (Equivalently, a two-term BCH expansion gives $U_p(\gamma_X(t))=\exp\!\big(t(d_1X)_p+O(t^2)\big)$.)

**Step 3 (Hessian of $\Phi_\beta$ at $\mathbf 1$).** Put $A:=d\rho(Y)\in\mathfrak u(n)$, so $\rho(\exp tY)=\exp(tA)$ and
$$\Re\operatorname{Tr}e^{tA}=n+t\,\Re\operatorname{Tr}A+\tfrac{t^2}{2}\Re\operatorname{Tr}A^2+O(t^3).$$
$A$ anti-Hermitian $\Rightarrow\operatorname{Tr}A\in i\mathbb R\Rightarrow\Re\operatorname{Tr}A=0$. Hence
$$\Phi_\beta(\exp tY)=\beta\Big(1-\tfrac1n\big(n+\tfrac{t^2}{2}\Re\operatorname{Tr}A^2\big)\Big)+O(t^3)=-\tfrac{\beta}{2n}\Re\operatorname{Tr}(A^2)\,t^2+O(t^3).$$
By the metric normalization $|Y|^2_{\mathfrak g}=-\Re\operatorname{Tr}(A^2)$, so $\Phi_\beta(\exp tY)=\tfrac{\beta}{2n}|Y|^2t^2+O(t^3)$. Therefore $\nabla\Phi_\beta(\mathbf 1)=0$ and, since $t\mapsto\exp(tY)$ is a geodesic,
$$\nabla^2\Phi_\beta(\mathbf 1)[Y,Y]=\frac{d^2}{dt^2}\Big|_0\Phi_\beta(\exp tY)=\frac{\beta}{n}|Y|^2_{\mathfrak g}=\alpha_W|Y|^2_{\mathfrak g},$$
and by polarization $\nabla^2\Phi_\beta(\mathbf 1)[Y,Z]=\alpha_W\langle Y,Z\rangle_{\mathfrak g}$.

**Step 4 (critical point).** $U_p(U^{(0)})=\mathbf 1$ for all $p$ and $\nabla\Phi_\beta(\mathbf 1)=0$, so each summand $\Phi_\beta\circ\mathrm{Hol}_p$ has vanishing gradient at $U^{(0)}$; hence $\nabla S(U^{(0)})=0$.

**Step 5 (chain rule at a critical value).** For $F:M\to N$ smooth and $f:N\to\mathbb R$ with $df(F(x_0))=0$, the second fundamental form term drops out of
$$\nabla^2_M(f\circ F)(x_0)[X,Y]=\nabla^2_Nf(y_0)[dF X,dF Y]+df(y_0)[(\nabla dF)(X,Y)],$$
leaving $\nabla^2_M(f\circ F)=\nabla^2_Nf\circ(dF\times dF)$. Applying this with $f=\Phi_\beta$, $F=\mathrm{Hol}_p$, $y_0=\mathbf 1$, using Steps 2–3 and summing over $p$:
$$\nabla^2S(U^{(0)})[X,X]=\alpha_W\sum_{p}|(d_1X)_p|^2_{\mathfrak g}=\alpha_W\,|d_1X|^2_{\mathcal C^2}=\alpha_W\langle X,d_1^*d_1X\rangle_{\mathcal C^1}.$$
Polarizing gives the bilinear form, and since it holds for all $X,Z$ the operator identity follows. $\square$

**Remark (why this is the "structural miracle").** Two independent facts conspire: (i) the vacuum is a critical point of $\Phi_\beta$, killing the second-fundamental-form term of the highly nonlinear holonomy map; (ii) the linearization of the ordered product around the identity is *exactly* the signed sum $\sum_b\sigma_{p,b}X_b$, i.e. the simplicial coboundary. Together they turn the second variation of a nonabelian gauge action into a linear-algebra object — the discrete Maxwell (curl–curl) operator — with no approximation.

### Constants and numbers

α_W = β/n exactly (n = dim of the defining representation ρ). For SU(N) with the fundamental rep, α_W = β/N = 2/g². The identity holds at any β, any volume, any compact G, any faithful ρ, with the specific metric normalization ⟨X,Y⟩ = −Re Tr(dρ(X)dρ(Y)). Under a different metric normalization ⟨·,·⟩' = c⟨·,·⟩ the coefficient rescales as α_W' = α_W/c.

**Caveat.** The identity is an identity at the vacuum only; away from U⁽⁰⁾ the Hessian acquires (a) Ad-twists turning d₁ into a covariant coboundary d₁^U, and (b) a second-fundamental-form term proportional to dΦ_β(U_p) = O(β·|log U_p|). Controlling both is exactly External Input Core-5.EI.1.

**Why it matters.** This is the single load-bearing computation of the whole programme: it is what makes 'mass gap' expressible as a curvature statement, and it is the only place a Maxwell operator with its cochain complex structure (d₁d₀ = 0, gauge zero modes, horizontal invariance) enters. It is fully correct.

---

## 3. Localized matrix hinge on a small-field set, with the complete error budget

`status: conditional` · `kind: theorem`

### Statement

**(Hinge, linkwise good set — the version that is actually proved.)** Let $\nu:=\nu_P$ be the plaquette–link overlap constant, let $F(g_1,g_2,g_3,g_4):=\Re\operatorname{Tr}(\mathbf 1-\rho(g_1g_2g_3^{-1}g_4^{-1}))$ so that $S_{\Lambda,\beta}=\tfrac{\beta}{n}\sum_pF(U_{\partial p})$, and for $r_\star\in(0,r_{\mathrm{sf}}]$ set
$$M_3(r_\star):=\sup_{g\in(\overline{B^G_{r_\star}(\mathbf 1)})^4}\|D^3F(g)\|_{\mathrm{op}}<\infty .$$
Define the linkwise small-field set $K_\Lambda(r):=\{U:\ d_G(U_b,\mathbf 1)<r\ \forall b\}$. Then for every $0<r\le r_\star$ and every $U\in K_\Lambda(r)$,
$$\nabla^2S_{\Lambda,\beta}(U)\ \succeq\ \alpha_W\,d_1^*d_1\ -\ R_W(r)\,\mathrm{Id},\qquad R_W(r):=\frac{\beta}{n}\cdot 2\nu\,M_3(r_\star)\cdot r .$$
Consequently, with $\mathrm{Ric}_{g_\Lambda}\succeq\kappa_G\,\mathrm{Id}=3m_H^2\,\mathrm{Id}$,
$$\mathrm{Ric}_{\mu_{\Lambda,\beta}}(U)=\mathrm{Ric}_{g_\Lambda}(U)+\nabla^2S(U)\ \succeq\ \big(3m_H^2-R_W(r)\big)\mathrm{Id}+\alpha_W\,d_1^*d_1,\qquad U\in K_\Lambda(r),$$
and if $r$ is chosen so that $R_W(r)\le 2m_H^2$, i.e.
$$\boxed{\ r\ \le\ r^{\mathrm{hinge}}:=\frac{m_H^2\,n}{\nu\,M_3(r_\star)\,\beta}\ =\ \Theta(\beta^{-1})\ }$$
then the **matrix hinge** holds:
$$\mathrm{Ric}_{\mu_{\Lambda,\beta}}(U)\ \succeq\ M^{\mathrm{hinge}}_\Lambda:=m_H^2\,\mathrm{Id}+\tfrac12\alpha_W\,d_1^*d_1,\qquad \forall U\in K_\Lambda(r).$$
All constants are independent of the volume $|\Lambda|$.

**(Hinge, plaquette good set — the version the rest of the chain wants.)** With $\mathcal K_{\Lambda,\beta}:=\{U:\ U_p(U)\in\exp(B_{r_\beta}(0))\ \forall p\}$, $r_\beta=r_{\mathrm{sf}}\min\{1,\beta^{-1/2}\}$, the same conclusion holds **conditional on External Input Core-5.EI.1**: there is $C_{\mathrm{WH}}=C_{\mathrm{WH}}(G,\rho,d)$, independent of $L,\beta$, with
$$\big\langle X,\big(\nabla^2S(U)-\nabla^2S(U^{(0)})\big)X\big\rangle\ \ge\ -C_{\mathrm{WH}}\,\beta\,r_\beta\,|X|^2,\qquad U\in\mathcal K_{\Lambda,\beta},$$
and the numerical constraint $C_{\mathrm{WH}}\beta r_\beta\le 2m_H^2$, which again forces $r_\beta=O(\beta^{-1})$.
$\mathcal K_{\Lambda,\beta}$ is gauge invariant; $K_\Lambda(r)$ is not.

### Derivation

**(1) Single-plaquette Hessian stability.** Let $\gamma$ be the minimizing geodesic in $G^4$ from $\mathbf 1^4$ to $g$ and $\psi(t):=D^2F(\gamma(t))(\xi,\xi)$. Then $\psi'(t)=D^3F(\gamma(t))(\dot\gamma,\xi,\xi)$ so $|\psi'|\le M_3(r_\star)|\dot\gamma||\xi|^2$; integrating over $t\in[0,1]$,
$$D^2F(g)(\xi,\xi)\ \ge\ D^2F(\mathbf 1^4)(\xi,\xi)-M_3(r_\star)\,d_{G^4}(g,\mathbf 1^4)\,|\xi|^2 .$$
$M_3(r_\star)<\infty$ because $F$ is smooth and $(\overline{B_{r_\star}})^4$ is compact.

**(2) Summation over plaquettes with bounded overlap.** Take $g=U_{\partial p}$, $\xi=X_{\partial p}$. On $K_\Lambda(r)$, $d_{G^4}(U_{\partial p},\mathbf 1^4)=\big(\sum_{b\in\partial p}d_G(U_b,\mathbf 1)^2\big)^{1/2}\le\sqrt4\,r=2r$. Summing over $p$ and multiplying by $\beta/n$:
$$\nabla^2S(U)(X,X)\ \ge\ \nabla^2S(U^{(0)})(X,X)-\tfrac{\beta}{n}M_3(r_\star)\cdot 2r\sum_p|X_{\partial p}|^2 .$$
Now $\sum_p|X_{\partial p}|^2=\sum_p\sum_{b\in\partial p}|X_b|^2=\sum_b\#\{p\ni b\}|X_b|^2\le\nu\,|X|^2_{\mathcal C^1}$, giving $R_W(r)=\tfrac{\beta}{n}\,2\nu M_3(r_\star)\,r$. Combined with $\nabla^2S(U^{(0)})=\alpha_Wd_1^*d_1$ (previous item) this is the displayed inequality.

**(3) Bakry–Émery assembly.** $\mathrm{Ric}_\mu=\mathrm{Ric}_{g}+\nabla^2S$; the product metric gives $\mathrm{Ric}_{g_\Lambda}=\bigoplus_b\mathrm{Ric}_{g_G}\succeq\kappa_G\mathrm{Id}$ uniformly in $U$ and in the volume. With $\kappa_G=3m_H^2$ and $R_W(r)\le2m_H^2$,
$$\mathrm{Ric}_\mu(U)\succeq(3m_H^2-2m_H^2)\mathrm{Id}+\alpha_Wd_1^*d_1=m_H^2\mathrm{Id}+\alpha_Wd_1^*d_1\succeq M^{\mathrm{hinge}}_\Lambda .\qquad\square$$

**(4) Why the radius must be $O(1/\beta)$ — a structural, not technical, constraint.** [reconstructed]
The error term $-R_W(r)\mathrm{Id}$ is **isotropic**: it is negative on *all* of $\mathcal C^1$, including $\mathrm{im}(d_0)$ (pure-gauge directions), where $d_1^*d_1$ vanishes identically ($d_1d_0=0$). So on $\mathrm{im}(d_0)$ the hinge reads $\mathrm{Ric}_\mu\succeq(\kappa_G-R_W(r))\mathrm{Id}$: the Maxwell stiffness cannot absorb any of the error there. The only $\beta$-independent positive reservoir is $\kappa_G$, while $R_W(r)\propto\beta r$. Hence $r\lesssim\kappa_G/\beta$ is forced by the *gauge directions alone*, for any variant of the argument that produces a deterministic comparison operator on all of $\mathcal C^1$. This is what the two independent bookkeepings in the corpus (`EXCITING_01` §3–4 and `Core_5` §5.2.4, which agree) are really recording.

**(5) Gauge invariance of $\mathcal K_{\Lambda,\beta}$ (Lemma Core-5.1.3).** $U_p(g\cdot U)=g_xU_p(U)g_x^{-1}$ with $x$ the basepoint of $p$; bi-invariance makes conjugation an isometry, so $\mathrm{dist}_G(\mathbf 1,U_p(g\cdot U))=\mathrm{dist}_G(\mathbf 1,U_p(U))$, and the defining condition is invariant. $\square$ (The linkwise set $K_\Lambda(r)$ has no such property.)

### Constants and numbers

R_W(r) = (β/n)·2ν_P·M₃(r_⋆)·r, with ν_P = 6 in d = 4.
Hinge threshold: R_W(r) ≤ 2m_H² ⟺ r ≤ r^hinge = m_H²·n/(ν_P M₃ β) = κ_G n/(3ν_P M₃ β).
For SU(3), d=4: m_H² = 1/2, n = 3, ν_P = 6 ⟹ r^hinge = 1/(4 M₃ β).
Hinge operator: M^hinge = m_H² Id + (α_W/2) d₁*d₁, with a₀(M^hinge) = m_H² EXACTLY (since d₁*d₁ has a kernel of dimension |V|−1+b₁ per g-component, so the Maxwell term contributes nothing to the bottom of the spectrum), R = 1, B₀(M^hinge) = (α_W/2)C₀(M₁) = 9α_W.
Core-5's own choice r_β = r_sf min{1, β^{−1/2}} does NOT satisfy the constraint; Core-5 explicitly proposes replacing it by r_β^hinge = r_sf min{1, β^{−1}}.

**Caveat.** The plaquette (gauge-invariant) version rests on Core-5.EI.1, which is stated as an External Input; the linkwise version is proved but on a set that is not gauge invariant. Also, on the plaquette good set the natural comparison operator is the *covariant* curl–curl (d₁^U)*d₁^U, not the vacuum d₁*d₁, because dHol_p at general U carries Ad-twists — this is why the linkwise set (not the plaquette set) is what the proof in EXCITING_01 actually controls.

**Why it matters.** This isolates the entire model-specific content of the programme into one local, finite-range, third-derivative estimate, and — via step (4) — shows exactly why that estimate forces a good-set radius of order 1/β. That single scaling is what later kills the whole approach (see the good-set obstruction item).

---

## 4. Helffer–Sjöstrand covariance identity and the matrix Brascamp–Lieb bound (Appendix F, reconstructed in full)

`status: conditional` · `kind: derivation`

### Statement

Let $(M,g)$ be a compact Riemannian manifold, $S\in C^2(M)$, $d\mu=Z^{-1}e^{-S}d\mathrm{vol}_g$, $L=\Delta-\langle\nabla S,\nabla\cdot\rangle$ the $\mu$-symmetric generator, $\mathrm{Ric}_\mu:=\mathrm{Ric}_g+\nabla^2S$. Define the **Helffer–Sjöstrand operator** (Witten Laplacian on vector fields)
$$\mathcal L^{(1)}\Xi:=\big((-L)\otimes I\big)\Xi+\mathrm{Ric}_\mu(\Xi),\qquad \big((-L)\otimes I\big)\Xi:=-\sum_i\big(\nabla_{e_i}\nabla_{e_i}\Xi-\nabla_{\nabla_{e_i}e_i}\Xi\big)+\nabla_{\nabla S}\Xi .$$
Assume: **(F2)** Poisson solvability, $(-L)^{-1}$ exists on $L^2_0(\mu)$; **(F7)** the vector-field integration-by-parts identity $\int\langle\Xi,((-L)\otimes I)\Xi\rangle d\mu=\int|\nabla\Xi|^2_{\mathrm{HS}}d\mu$; **(F12)** strict positivity/invertibility of $\mathcal L^{(1)}$. Then:

1. **(Commutation)** $\nabla(-Lu)=\mathcal L^{(1)}(\nabla u)$ for all $u\in C^\infty(M)$.
2. **(HS identity)** For $F,G\in C^\infty(M)$ with $\mu(G)=0$,
$$\mathrm{Cov}_\mu(F,G)=\int_M\big\langle\nabla F,(\mathcal L^{(1)})^{-1}\nabla G\big\rangle_g\,d\mu .$$
3. **(Bochner dominance)** $\mathcal L^{(1)}\succeq\mathrm{Ric}_\mu$ as quadratic forms on $L^2(\mu;TM)$.
4. **(Order reversal)** If $\mathsf A\succeq\mathsf B\succeq cI$, $c>0$, then $\mathsf A^{-1}\preceq\mathsf B^{-1}$.
5. **(Matrix Brascamp–Lieb)** If $\mathrm{Ric}_\mu(U)\succeq M\succeq m^2I$ for all $U$ in the relevant domain, with $M$ a fixed operator on the model fiber, then $\mathcal L^{(1)}\succeq M$, $(\mathcal L^{(1)})^{-1}\preceq M^{-1}$, and
$$\big|\mathrm{Cov}_\mu(F,G)\big|\le\Big(\int\langle\nabla F,M^{-1}\nabla F\rangle d\mu\Big)^{1/2}\Big(\int\langle\nabla G,M^{-1}\nabla G\rangle d\mu\Big)^{1/2}.$$
**(Conditioned version.)** For $\Omega\subseteq M$ relatively compact with piecewise-$C^2$ boundary, $\mu^\Omega:=\mu(\cdot\mid\Omega)$, assume **(F20)** existence of the $\mu^\Omega$-symmetric reflecting (Neumann) generator $L^\Omega$ with the corresponding IBP and Poisson solvability. Then 2.–5. hold verbatim with $\mu\to\mu^\Omega$, $\mathcal L^{(1)}\to\mathcal L^{(1),\Omega}$, and the pointwise hinge required only on $\Omega$.

### Derivation

**1. Commutation $\nabla(-Lu)=\mathcal L^{(1)}\nabla u$.** Work at $U\in M$ in a frame normal at $U$ ($\nabla_{e_i}e_j(U)=0$).
*Laplace part.* Bochner: $\nabla(-\Delta u)=-\Delta(\nabla u)+\mathrm{Ric}_g(\nabla u)$, obtained by tracing the curvature commutator $\nabla_{e_i}\nabla_{e_j}\nabla u-\nabla_{e_j}\nabla_{e_i}\nabla u=R(e_i,e_j)\nabla u$.
*Drift part.* Put $h:=\langle\nabla S,\nabla u\rangle$. For any tangent $X$,
$$Xh=\langle\nabla_X\nabla S,\nabla u\rangle+\langle\nabla S,\nabla_X\nabla u\rangle=\langle(\nabla^2S)(\nabla u),X\rangle+\nabla^2u(X,\nabla S),$$
and by symmetry of $\nabla^2u$, $\nabla^2u(X,\nabla S)=\langle\nabla_{\nabla S}\nabla u,X\rangle$. Since $X$ is arbitrary,
$$\nabla\langle\nabla S,\nabla u\rangle=(\nabla^2S)(\nabla u)+\nabla_{\nabla S}\nabla u .$$
*Collect.* $-Lu=-\Delta u+\langle\nabla S,\nabla u\rangle$, so
$$\nabla(-Lu)=\big[-\Delta(\nabla u)+\nabla_{\nabla S}\nabla u\big]+\mathrm{Ric}_g(\nabla u)+(\nabla^2S)(\nabla u)=\big((-L)\otimes I\big)\nabla u+\mathrm{Ric}_\mu(\nabla u).\ \square$$

**2. HS identity.** For $\mu(G)=0$ let $u=(-L)^{-1}G$. Then $\mathrm{Cov}_\mu(F,G)=\int FG\,d\mu=\int F(-Lu)\,d\mu=\int\langle\nabla F,\nabla u\rangle d\mu$ by IBP. By 1., $\mathcal L^{(1)}(\nabla u)=\nabla(-Lu)=\nabla G$, so $\nabla u=(\mathcal L^{(1)})^{-1}\nabla G$; substitute. $\square$

**3. Bochner dominance.** By (F7), $\int\langle\Xi,((-L)\otimes I)\Xi\rangle d\mu=\int|\nabla\Xi|^2_{\mathrm{HS}}d\mu\ge0$, hence $\int\langle\Xi,\mathcal L^{(1)}\Xi\rangle d\mu\ge\int\langle\Xi,\mathrm{Ric}_\mu\Xi\rangle d\mu$. $\square$ (In the lattice case (F7) is provable directly in the global right-invariant orthonormal frame.)

**4. Order reversal.** $x\mapsto1/x$ is operator-monotone decreasing on $(0,\infty)$; apply the spectral theorem. $\square$

**5. Matrix BL.** By 3. and the pointwise hinge, for every $\Xi$,
$$\int\langle\Xi,\mathcal L^{(1)}\Xi\rangle d\mu\ \ge\ \int\langle\Xi,\mathrm{Ric}_\mu\Xi\rangle d\mu\ \ge\ \int\langle\Xi,M\Xi\rangle d\mu,$$
i.e. $\mathcal L^{(1)}\succeq M\otimes I\succeq m^2I$ on $L^2(\mu;TM)\cong L^2(\mu)\otimes\mathcal C^1$ (using right-trivialization, $M$ acting fiberwise). By 4., $(\mathcal L^{(1)})^{-1}\preceq M^{-1}$. Since both are positive, Cauchy–Schwarz in the $(\mathcal L^{(1)})^{-1}$-inner product followed by the domination gives
$$|\langle\nabla F,(\mathcal L^{(1)})^{-1}\nabla G\rangle|\le\langle\nabla F,(\mathcal L^{(1)})^{-1}\nabla F\rangle^{1/2}\langle\nabla G,(\mathcal L^{(1)})^{-1}\nabla G\rangle^{1/2}\le\langle\nabla F,M^{-1}\nabla F\rangle^{1/2}\langle\nabla G,M^{-1}\nabla G\rangle^{1/2}.\ \square$$

**Correction to Prop. F.15 as stated in the corpus.** The corpus states 5. "as quadratic forms on vector fields $\Xi$ supported in $\mathcal D$". A form inequality restricted to a *subclass* of vectors does not permit inversion. The statement is correct only when the hinge holds $\mu$-a.e. on the whole space over which $\mathcal L^{(1)}$ acts — which is exactly what the conditioned version (F.22/F.23, $\Omega=\mathcal K$) provides. So the conditioned route is the only sound one, and this is the route Core-6 uses.

**Correction to Prop. F.18 / Core-6.5.2 (horizontal refinement).** These claim that for gauge-invariant $F$ one may replace $M^{-1}$ by its restriction to $H^{(0)}=\ker d_0^*$. The proof of horizontality (Lemma Core-5.3.2) gives $\nabla^RF(U)\in\ker\big((d_0^U)^*\big)$ with the *$U$-dependent* covariant coboundary $(d_0^U\phi)_{(x,\mu)}=\phi_x-\mathrm{Ad}_{U_{x,\mu}}\phi_{x+\hat e_\mu}$. Only at $U=U^{(0)}$ does this coincide with $\ker d_0^*$. So the horizontal refinement is valid at the vacuum and is **not** established on the good set. (The corpus's own `Extract_09` §8 lists "extend horizontality beyond the vacuum" as open.) The main chain does not need it.

### Constants and numbers

No new constants. Structural facts used downstream: (i) L^(1) = (rough Laplacian with drift) + Ric_μ, with the first summand ⪰ 0; (ii) a₀(L^(1),Ω) ≥ inf_{U∈Ω} λ_min(Ric_μ(U)) ≥ m_H²; (iii) on M_Λ = G^{E} with the product metric, the Levi-Civita connection splits over link factors, so ((−L)⊗I) is block-diagonal in the link index and Ric_{g_Λ} is block-diagonal — used in the repair item.

**Caveat.** Three genuine external inputs remain (F.2/F.7/F.12 and, for the conditioned version, F.20 — existence of a reflecting diffusion on a domain with corners). The Cauchy–Schwarz form of the matrix BL bound carries NO distance information; see the next item.

**Why it matters.** This is the analytic bridge that converts a pointwise curvature lower bound into a covariance bound with a *deterministic* operator, and it is derived correctly and in full. It is the reusable core of the programme, valid for any Gibbs measure on a compact manifold.

---

## 5. Counterexample: the kernel-form covariance bound (Core-6.4.3) does not follow from the matrix Brascamp–Lieb bound — and a repair that restores all constants

`status: solid` · `kind: obstruction`

### Statement

**Part A (the counterexample).** The following implication, asserted as Proposition Core-6.4.3 and used by Core-7, Core-8 and Core-9, is **false**:
> *If $\mathrm{Ric}_\mu(U)\succeq M\succeq m^2I$ on $\Omega$ and the conditioned HS identity holds, then for cylinder observables with link supports $A,B$,*
> $$|\mathrm{Cov}_{\mu^\Omega}(F,G)|\le\sum_{b\in A}\sum_{b'\in B}\big\|\mathbb E|(\nabla^RF)_b|^2\big\|^{1/2}\,\big\|(M^{-1})_{b,b'}\big\|_{\mathrm{op}}\,\big\|\mathbb E|(\nabla^RG)_{b'}|^2\big\|^{1/2}.$$

**Witness.** Take $\Omega=\mathcal M_\Lambda$, $\Lambda$ two links $b_1,b_2$, $G=\mathrm{SU}(2)$, $S(U)=-c\,\Re\operatorname{Tr}(U_{b_1}U_{b_2})$ with $|c|$ small. Then $\mathrm{Ric}_{g}=\kappa_G\mathrm{Id}$ and $\|\nabla^2S\|\le C|c|$, so $\mathrm{Ric}_\mu\succeq m^2I$ with $m^2:=\kappa_G-C|c|>0$. The choice $M:=m^2I$ satisfies **both** hypotheses ($\mathrm{Ric}_\mu\succeq M$ and $M\succeq m^2I$). But $M^{-1}=m^{-2}\mathrm{Id}$ is diagonal, so $(M^{-1})_{b_1b_2}=0$ and the asserted bound would give $\mathrm{Cov}(F,G)=0$ for every $F=f(U_{b_1})$, $G=g(U_{b_2})$. This is false: expanding $e^{c\Re\operatorname{Tr}(U_1U_2)}=\sum_j a_j(c)\chi_j(U_1U_2)$ with $a_{1/2}(c)\ne0$ for $c\ne0$, and using $\chi_j(U_1U_2)=\sum_{mn}D^j_{mn}(U_1)D^j_{nm}(U_2)$, one gets $\mathrm{Cov}(\chi_{1/2}(U_1),\chi_{1/2}(U_2))\propto a_{1/2}(c)\ne0$. $\square$

The reason is structural: $A\preceq B$ for positive $A,B$ gives $|\langle u,Av\rangle|\le\langle u,Bu\rangle^{1/2}\langle v,Bv\rangle^{1/2}$ — the Cauchy–Schwarz form, which contains no cross-support information — but **not** any bound on the individual matrix elements $|\langle u,Av\rangle|$ by $|\langle u,Bv\rangle|$. Distance decay must come from the kernel of $(\mathcal L^{(1)})^{-1}$ itself, never from that of a dominating operator.

**Part B (the repair — and it gives the same constants).** Let $\Omega\subseteq\mathcal M_{\Lambda_L}$, $\mu^\Omega$, $\mathcal L^{(1),\Omega}$ as in the HS item, and assume
(i) $\mathrm{Ric}_{\mu}(U)\succeq m_H^2\,\mathrm{Id}$ for $\mu^\Omega$-a.e. $U\in\Omega$;
(ii) $B_S:=\sup_{U\in\Omega}\ \sup_{b}\sum_{b'\ne b}\big\|\big(\nabla^2S_{\Lambda_L,\beta}(U)\big)_{bb'}\big\|_{\mathrm{op}(\mathfrak g)}<\infty$.
Then $\mathcal L^{(1),\Omega}$, viewed as a self-adjoint operator on $\bigoplus_{b\in E(\Lambda_L)}L^2(\mu^\Omega;\mathfrak g)$, satisfies $a_0=m_H^2$, $R=1$ in $\mathrm{dist}_E$, $B_0\le B_S$, and hence
$$\Big\|\big((\mathcal L^{(1),\Omega})^{-1}\big)_{bb'}\Big\|_{\mathrm{op}}\ \le\ \frac{2}{m_H^2}\,e^{-\eta\,\mathrm{dist}_E(b,b')},\qquad \eta=\log\Big(1+\frac{m_H^2}{2B_S}\Big)\ \ \text{(Combes–Thomas)},$$
or, by the Davies route, $\eta=\operatorname{arcosh}\big(1+\tfrac{m_H^2}{2B_S}\big)$. Consequently, for smooth cylinder observables with link supports $A,B$,
$$\big|\mathrm{Cov}_{\mu^\Omega}(F,G)\big|\ \le\ \frac{2}{m_H^2}\,e^{-\eta\,\mathrm{dist}_E(A,B)}\ \mathsf L_E(F)\,\mathsf L_E(G),\qquad \mathsf L_E(F):=\sum_{b}\sup_U\big|(\nabla^RF(U))_b\big|_{\mathfrak g}.$$
At the vacuum $B_S=\alpha_W C_0(\mathsf M_1)=18\alpha_W$ exactly, so the repaired exponent reproduces the corpus's number.

### Derivation

**Part B, in detail.** [reconstructed — this argument is not in the corpus, although `01_fixed_cutoff_engine.md` §5 names the correct route ("Combes–Thomas decay of $\mathcal L^{-1}$") without carrying it out.]

*Step 1 (fibered structure).* $\mathcal M_{\Lambda_L}=\prod_bG$ is a Riemannian product, so the global right-invariant trivialization gives an isometry
$$L^2(\mu^\Omega;T\mathcal M_{\Lambda_L})\ \cong\ \bigoplus_{b\in E(\Lambda_L)}L^2(\mu^\Omega;\mathfrak g)=\ell^2\big(E(\Lambda_L);\mathsf H_0\big),\qquad \mathsf H_0:=L^2(\mu^\Omega;\mathfrak g).$$
The index set $E(\Lambda_L)$ is finite; the fiber $\mathsf H_0$ is infinite-dimensional, which is harmless (see Step 4).

*Step 2 (range one).* Decompose $\mathcal L^{(1),\Omega}=\big((-L^\Omega)\otimes I\big)+\mathrm{Ric}_{g_\Lambda}+\nabla^2S$.
(a) For a Riemannian product the Christoffel symbols mixing different factors vanish, so $\nabla$ preserves the splitting $T\mathcal M=\bigoplus_b\pi_b^*TG$; hence the rough Laplacian and the drift term $\nabla_{\nabla S}$ map the $b$-component to the $b$-component: $\big((-L^\Omega)\otimes I\big)$ is **block-diagonal** in $b$.
(b) $\mathrm{Ric}_{g_\Lambda}=\bigoplus_b\mathrm{Ric}_{g_G}$ is block-diagonal.
(c) $\big(\nabla^2S(U)\big)_{bb'}$ for $b\ne b'$ equals the mixed second partial $\partial_{b}\partial_{b'}S$ (the connection correction $\Gamma^c_{bb'}\partial_cS$ vanishes off-diagonally by (a)). Since $S=\sum_p\Phi_\beta(U_p)$ and each summand depends only on the four links of $\partial p$, $\big(\nabla^2S\big)_{bb'}=0$ unless $b,b'$ lie on a common plaquette, i.e. unless $\mathrm{dist}_E(b,b')\le1$.
Therefore $R(\mathcal L^{(1),\Omega})=1$ and $B_0(\mathcal L^{(1),\Omega})\le B_S$.

*Step 3 (uniform positivity).* By Bochner dominance (item above) and hypothesis (i),
$$\big\langle\Xi,\mathcal L^{(1),\Omega}\Xi\big\rangle\ \ge\ \int_\Omega\langle\Xi,\mathrm{Ric}_\mu\Xi\rangle\,d\mu^\Omega\ \ge\ m_H^2\|\Xi\|^2,$$
so $a_0(\mathcal L^{(1),\Omega})\ge m_H^2$ and $\|(\mathcal L^{(1),\Omega})^{-1}\|\le m_H^{-2}$.

*Step 4 (Combes–Thomas with an infinite-dimensional fiber).* The proof of Proposition G.3.1 (reproduced in the next item) uses only: Cauchy–Schwarz in the fiber; finiteness of the index set; self-adjointness (to get $\|A_{xz}\|=\|A_{zx}\|$ from $A_{xz}=A_{zx}^*$); and a Neumann series. None of these requires $\dim\mathsf H_0<\infty$. Applying it with $V=E(\Lambda_L)$, $\mathrm{dist}=\mathrm{dist}_E$, $A=\mathcal L^{(1),\Omega}$ yields the displayed kernel bound with $\eta=\log(1+m_H^2/(2B_S))$. The Davies variant (Appendix H) also transfers verbatim: write $\mathcal L^{(1),\Omega}=m_H^2I+\mathcal N$ with $\mathcal N\succeq0$, note that the off-diagonal blocks of $\mathcal N$ are those of $\mathcal L^{(1),\Omega}$, and run the weight conjugation to get $\eta=\operatorname{arcosh}(1+m_H^2/(2B_S))$ with the same prefactor $2/m_H^2$.

*Step 5 (clustering).* By the conditioned HS identity, and expanding in the link blocks,
$$\mathrm{Cov}_{\mu^\Omega}(F,G)=\sum_{b,b'}\Big\langle(\nabla^RF)_b,\ \big((\mathcal L^{(1),\Omega})^{-1}\big)_{bb'}(\nabla^RG)_{b'}\Big\rangle_{\mathsf H_0}.$$
Cylinder supports force $(\nabla^RF)_b=0$ for $b\notin A$ and $(\nabla^RG)_{b'}=0$ for $b'\notin B$. Bounding each term by $\|(\nabla^RF)_b\|_{\mathsf H_0}\,\|(\cdots)_{bb'}\|_{\mathrm{op}}\,\|(\nabla^RG)_{b'}\|_{\mathsf H_0}$, inserting Step 4, using $\mathrm{dist}_E(b,b')\ge\mathrm{dist}_E(A,B)$ on $A\times B$, factoring the double sum, and bounding $L^2(\mu^\Omega)$-norms by sup-norms gives the stated bound. $\square$

**Three consequences worth stating plainly.**
1. The repaired chain reaches *exactly* the conclusion Core-7.2.3 asserts, with $B_S$ in place of $B_0(M^{\mathrm{hinge}})=9\alpha_W$: at the vacuum $B_S=18\alpha_W$, so the exponent is $\log\!\big(1+\tfrac{m_H^2}{36\alpha_W}\big)$ — which is exactly the constant Appendix G already records for the *unhalved* operator $M_{\Lambda_L}$ (eq. G.4.3). So nothing quantitative is lost.
2. The repair uses **only the scalar part** of the hinge, $\mathrm{Ric}_\mu\succeq m_H^2\mathrm{Id}$. The Maxwell term $\tfrac{\alpha_W}{2}d_1^*d_1$ contributes nothing to $a_0$ (it has a large kernel: $\mathrm{im}\,d_0\oplus H^1$), and only *increases* $B_0$. The corpus's headline claim that keeping the matrix structure is essential is therefore inverted: for this bound, the matrix structure is a liability, and it is the $\beta$-independent scalar floor $m_H^2$ that does all the work.
3. The repair also dissolves the covariant-versus-vacuum coboundary problem: one never needs $\nabla^2S(U)\approx\alpha_Wd_1^*d_1$, only $\nabla^2S(U)$'s *range* and *row sums*, which are uniform over all of $\mathcal M_{\Lambda_L}$.

### Constants and numbers

B_S = sup_{U∈Ω} sup_b Σ_{b'≠b} ‖(∇²S(U))_{bb'}‖. At U⁽⁰⁾: B_S = α_W·C₀(M₁) = 18 α_W exactly. On K_Λ(r): B_S ≤ 18 α_W (1 + O(M₃ r)). Globally: B_S ≤ 3ν_P (β/n) sup_{g∈G⁴}‖D²F(g)‖ < ∞.
Repaired exponent (CT):      η = log(1 + m_H²/(2B_S)) = log(1 + m_H²/(36 α_W)).
Repaired exponent (Davies):  η = arcosh(1 + m_H²/(36 α_W)).
Prefactor 2/m_H² in both cases.
SU(3), β=6 (α_W = 2, m_H² = 0.5, B_S = 36): η_CT = 0.006920, η_Davies = 0.117783.
SU(2), β=2.5 (α_W = 1.25, m_H² = 1/3, B_S = 22.5): η_CT = 0.007380, η_Davies = 0.121641.
Corpus value for comparison: η_CT(M^hinge) = log(1 + m_H²/(α_W·3ν_P)) = log(1 + m_H²/(18α_W)) — a factor 2 larger in the argument, i.e. an artifact of halving the Maxwell coefficient, not a real gain.

**Caveat.** The repair inherits the same external inputs as the HS item (F.7, F.12, F.20 on Ω), and hypothesis (i) is still the hinge, which is still conditional on Core-5.EI.1. What the repair removes is a *logical* gap, not an analytic hypothesis.

**Why it matters.** This is the single most consequential finding on this topic. As written, the corpus's clustering theorem (Core-7.2.2/7.2.3), its unconditioning (Core-8.3.1) and its gap theorem (Core-9.5.5) all rest on a step that admits a two-link counterexample. The repair is short, keeps every constant, and simultaneously shows that the programme's advertised novelty (the matrix structure) is not what makes the estimate work.

---

## 6. Combes–Thomas block inverse decay for uniformly positive finite-range operators (Appendix G, full proof)

`status: solid` · `kind: theorem`

### Statement

Let $V$ be a **finite** set with a graph distance $\mathrm{dist}$, $\mathsf H_0$ a real Hilbert space, and $A$ a self-adjoint operator on $\ell^2(V;\mathsf H_0)$ with block representation $(A_{xy})_{x,y\in V}$, $A_{xy}\in\mathcal B(\mathsf H_0)$. Suppose
$$a_0(A)>0\ \ (A\succeq a_0I),\qquad R(A)<\infty\ \ (A_{xy}=0\text{ if }\mathrm{dist}(x,y)>R),\qquad B_0(A)=\sup_x\sum_{y\ne x}\|A_{xy}\|_{\mathrm{op}}<\infty .$$
Then $A$ is invertible and for all $x,y\in V$
$$\big\|(A^{-1})_{xy}\big\|_{\mathrm{op}}\ \le\ \frac{2}{a_0(A)}\exp\big(-\eta_{\mathrm{CT}}(A)\,\mathrm{dist}(x,y)\big),\qquad \eta_{\mathrm{CT}}(A)=\frac{1}{R(A)}\log\Big(1+\frac{a_0(A)}{2B_0(A)}\Big),$$
with $\eta_{\mathrm{CT}}=+\infty$ (and $A$ block-diagonal) when $B_0(A)=0$.

**Auxiliary (block Schur bound).** If $K$ has blocks $K_{xy}$ with $\sup_x\sum_y\|K_{xy}\|\le R_0$ and $\sup_y\sum_x\|K_{xy}\|\le C_0$, then $\|K\|_{\mathrm{op}}\le\sqrt{R_0C_0}$; if $K=K^*$ then $\|K\|_{\mathrm{op}}\le R_0$.

**Specialization.** For $M_{\Lambda_L}=m_H^2\mathrm{Id}+\alpha_W d_1^*d_1$ on $\mathcal C^1(\Lambda_L;\mathfrak g)$ with $V=E(\Lambda_L)$, $\mathrm{dist}=\mathrm{dist}_E$: $a_0=m_H^2$, $R=1$, $B_0=\alpha_WC_0(\mathsf M_1)=18\alpha_W$ (exactly, in $d=4$), hence
$$\big\|(M_{\Lambda_L}^{-1})_{bb'}\big\|_{\mathrm{op}}\ \le\ \frac{2}{m_H^2}\exp\Big(-\log\Big(1+\frac{m_H^2}{36\,\alpha_W}\Big)\mathrm{dist}_E(b,b')\Big),$$
uniformly in the volume.

### Derivation

**Block Schur bound.** By Cauchy–Schwarz in $\mathsf H_0$, $|\langle g(x),K_{xy}f(y)\rangle|\le|g(x)|\,\|K_{xy}\|\,|f(y)|$, so
$$|\langle g,Kf\rangle|\le\sum_{x,y}\|K_{xy}\|\,|g(x)|\,|f(y)|\le\tfrac12\sum_x|g(x)|^2\sum_y\|K_{xy}\|+\tfrac12\sum_y|f(y)|^2\sum_x\|K_{xy}\|\le\tfrac12R_0\|g\|^2+\tfrac12C_0\|f\|^2,$$
using $ab\le\tfrac12(a^2+b^2)$ with $a=|g(x)|\|K_{xy}\|^{1/2}$, $b=|f(y)|\|K_{xy}\|^{1/2}$. Replacing $g\to\lambda g$ and optimizing over $\lambda>0$ gives $|\langle g,Kf\rangle|\le\sqrt{R_0C_0}\|g\|\|f\|$. If $K=K^*$ then $K_{xy}=K_{yx}^*$, so $\|K_{xy}\|=\|K_{yx}\|$ and one may take $C_0=R_0$. $\square$

**Main proof (weight conjugation).** Fix $y_0\in V$, set $\phi(x):=\mathrm{dist}(x,y_0)$ — 1-Lipschitz by the triangle inequality — and for $t\ge0$ let $W_t$ be the diagonal operator $(W_tf)(x)=e^{t\phi(x)}f(x)$, $A_t:=W_tAW_t^{-1}$, so that $A^{-1}=W_t^{-1}A_t^{-1}W_t$.

*Step 1 (conjugated blocks).* $(A_t)_{xz}=e^{t(\phi(x)-\phi(z))}A_{xz}$, hence with $K_t:=A_t-A$,
$$(K_t)_{xz}=\big(e^{t(\phi(x)-\phi(z))}-1\big)A_{xz},\qquad (K_t)_{xx}=0 .$$

*Step 2 (norm of the perturbation).* If $A_{xz}\ne0$ then $\mathrm{dist}(x,z)\le R$, so $|\phi(x)-\phi(z)|\le R$ and $|e^{tu}-1|\le e^{tR}-1$ for $|u|\le R$, $t\ge0$. Hence $\|(K_t)_{xz}\|\le(e^{tR}-1)\|A_{xz}\|$ for $x\ne z$, and summing over $z\ne x$ (resp. over $x\ne z$, using self-adjointness) gives row and column sums $\le(e^{tR}-1)B_0$. The block Schur bound then gives
$$\|K_t\|_{\mathrm{op}}\le\big(e^{tR}-1\big)B_0 .$$

*Step 3 (Neumann series).* $A\succeq a_0I$ gives $\|A^{-1}\|\le1/a_0$. If $t$ is chosen so that $\|K_t\|\le a_0/2$, then $\|K_tA^{-1}\|\le1/2$, $I+K_tA^{-1}$ is invertible, $A_t^{-1}=A^{-1}(I+K_tA^{-1})^{-1}$, and
$$\|A_t^{-1}\|\le\frac{1}{a_0}\cdot\frac{1}{1-1/2}=\frac{2}{a_0}.$$
The condition $\|K_t\|\le a_0/2$ is implied by $(e^{tR}-1)B_0\le a_0/2$, i.e. $t\le\frac1R\log(1+\frac{a_0}{2B_0})=\eta_{\mathrm{CT}}(A)$.

*Step 4 (extract decay).* $(A^{-1})_{xz}=e^{-t\phi(x)}(A_t^{-1})_{xz}e^{t\phi(z)}$; taking $z=y_0$ (so $\phi(y_0)=0$) and using $\|(A_t^{-1})_{xy_0}\|\le\|A_t^{-1}\|$,
$$\|(A^{-1})_{xy_0}\|\le e^{-t\,\mathrm{dist}(x,y_0)}\cdot\frac{2}{a_0}.$$
Choosing $t=\eta_{\mathrm{CT}}(A)$ and letting $y_0$ range over $V$ completes the proof. $\square$

**Specialization to $M_{\Lambda_L}$.** $\mathsf M_1\succeq0$ (since $\langle X,\mathsf M_1X\rangle=|d_1X|^2$), so $M_{\Lambda_L}\succeq m_H^2\mathrm{Id}$ and $a_0=m_H^2$. The mass term is diagonal; the off-diagonal blocks are $\alpha_W(\mathsf M_1)_{bb'}$, which vanish for $\mathrm{dist}_E>1$ (two links at $\mathrm{dist}_E\ge2$ share no plaquette so $\sigma_{p,b}\sigma_{p,b'}=0$ for all $p$), giving $R=1$; and $B_0=\alpha_WC_0(\mathsf M_1)=18\alpha_W$. Insert. $\square$

**Horizontal restriction (Prop. G.4.2), reproduced.** $H^{(0)}:=\ker d_0^*$ is $M_{\Lambda_L}$-invariant: for $X\in H^{(0)}$, $d_0^*(\mathsf M_1X)=d_0^*d_1^*d_1X=(d_1d_0)^*d_1X=0$. Since $M_{\Lambda_L}$ is invertible on the whole space and maps $H^{(0)}$ into itself, it restricts to a bijection of $H^{(0)}$; uniqueness of solutions then gives $(M_{\Lambda_L}|_{H^{(0)}})^{-1}=(M_{\Lambda_L}^{-1})|_{H^{(0)}}$, so ambient kernel bounds apply verbatim to horizontal inputs.

### Constants and numbers

a₀(M_Λ) = m_H²; R(M_Λ) = 1; B₀(M_Λ) = α_W·C₀(M₁) = 18 α_W (exact, d=4).
η_CT(M_Λ) = log(1 + m_H²/(36 α_W)).
For M^hinge = m_H² + (α_W/2)d₁*d₁: B₀ = 9α_W, η_CT = log(1 + m_H²/(18 α_W)).
Prefactor 2/m_H² in all cases.
SU(3), β = 6: η_CT(M_Λ) = 0.006920, η_CT(M^hinge) = 0.013830.
Direct numerical check on a 2-torus (L = 12, m² = 1, α = 1): C₀ = 6, η_CT bound = 0.0800, measured decay of max|(M⁻¹)_{b₀b}| over dist_E = 1..10 gives slope 1.059 — the bound holds with a factor ≈ 13 of slack.

### Code

# Numerical check of the CT bound against the true inverse-kernel decay.
# (Adapted from SIMULATIONS/sanity_check_maxwell_decay.py, generalized to d dimensions.)
import numpy as np, math
from collections import deque

def build(L, d):
    pts = [tuple(np.unravel_index(i, (L,)*d)) for i in range(L**d)]
    eidx = {}
    for x in pts:
        for mu in range(d): eidx[(x, mu)] = len(eidx)
    plaqs = [(x, mu, nu) for x in pts for mu in range(d) for nu in range(mu+1, d)]
    D1 = np.zeros((len(plaqs), len(eidx)))
    sh = lambda x, mu: tuple((x[i] + (i == mu)) % L for i in range(d))
    for k, (x, mu, nu) in enumerate(plaqs):
        D1[k, eidx[(x,mu)]] += 1;  D1[k, eidx[(sh(x,mu),nu)]] += 1
        D1[k, eidx[(sh(x,nu),mu)]] -= 1; D1[k, eidx[(x,nu)]] -= 1
    return D1, eidx

def analyse(L, d, m2, alpha):
    D1, eidx = build(L, d); K = D1.T @ D1; nE = K.shape[0]
    G = np.linalg.inv(m2*np.eye(nE) + alpha*K)
    i0 = eidx[(tuple([0]*d), 0)]
    adj = [np.nonzero(K[i])[0] for i in range(nE)]
    dist = -np.ones(nE, int); dist[i0] = 0; q = deque([i0])
    while q:
        i = q.popleft()
        for j in adj[i]:
            if j != i and dist[j] < 0: dist[j] = dist[i]+1; q.append(j)
    mx = {r: np.abs(G[i0, dist == r]).max() for r in range(dist.max()+1)}
    C0 = (np.abs(K) - np.diag(np.abs(np.diag(K)))).sum(1).max(); B0 = alpha*C0
    rs = [r for r in mx if 1 <= r <= min(6, max(mx))]
    true = -np.polyfit(rs, [math.log(mx[r]) for r in rs], 1)[0]
    return C0, math.log(1+m2/(2*B0)), math.acosh(1+m2/(2*B0)), true

for (L,d,m2,al) in [(12,2,1.,1.),(12,2,.3,1.),(8,3,1.,1.),(6,4,1.,1.),(6,4,.3,1.)]:
    C0,ct,dv,tr = analyse(L,d,m2,al)
    print(f"d={d} m2={m2} a={al}: C0={C0:.0f} eta_CT={ct:.5f} eta_Davies={dv:.5f} measured={tr:.5f}")
# d=2 m2=1.0: C0=6  eta_CT=0.08004 eta_Davies=0.40547 measured=1.05917
# d=4 m2=1.0: C0=18 eta_CT=0.02740 eta_Davies=0.23516 measured=1.21549
# d=4 m2=0.3: C0=18 eta_CT=0.00830 eta_Davies=0.12901 measured=1.08683

**Caveat.** The bound is correct but very slack: the Neumann-series (CT) exponent behaves like m²/(2B₀) as m² → 0, whereas the truth behaves like √(m²/α). The Davies variant closes most of that gap; see the next item.

**Why it matters.** This is the one piece of the chain that is complete, self-contained, textbook-quality mathematics, valid for an arbitrary Hilbert fiber — which is precisely what makes the repair in the previous item possible.

---

## 7. Davies conjugation: the sharp-order Combes–Thomas exponent, and the exact decay rate of the massive lattice Maxwell resolvent

`status: solid` · `kind: derivation`

### Statement

**(a) Davies bound.** Let $L\succeq0$ be self-adjoint and finite-range (range 1 in $\mathrm{dist}_E$) on $\ell^2(E(\Lambda_L);\mathfrak g)$, $M=m^2\mathrm{Id}+L$, and let
$$C_\partial:=\sup_{b'}\sup_{b}\sum_{\tilde b\ne b,\ |\phi_{b'}(b)-\phi_{b'}(\tilde b)|=1}\|L_{b\tilde b}\|_{\mathrm{op}},\qquad \phi_{b'}(\cdot)=\mathrm{dist}_E(\cdot,b')\ \ (\le C_0:=\textstyle\sup_b\sum_{\tilde b\neq b}\|L_{b\tilde b}\|).$$
If $\lambda\ge0$ satisfies $C_\partial(\cosh\lambda-1)<m^2$, then
$$\big\|(M^{-1})_{bb'}\big\|_{\mathrm{op}}\ \le\ \frac{1}{m^2-C_\partial(\cosh\lambda-1)}\ e^{-\lambda\,\mathrm{dist}_E(b,b')} .$$
Choosing $C_\partial(\cosh\lambda-1)=m^2/2$, i.e.
$$\lambda=\operatorname{arcosh}\Big(1+\frac{m^2}{2C_\partial}\Big)=2\operatorname{arsinh}\Big(\frac{m}{2\sqrt{C_\partial}}\Big),$$
gives $\|(M^{-1})_{bb'}\|\le\frac{2}{m^2}e^{-\lambda\,\mathrm{dist}_E(b,b')}$. Since $\operatorname{arcosh}(1+x)\sim\sqrt{2x}$ while $\log(1+x)\sim x$, the Davies rate is $O(m)$ as $m\to0$ where the Neumann-series rate is $O(m^2)$.

**(b) Scalarization on the horizontal sector.** On $\ker d_0^*\subset\ell^2\mathcal C^1(\mathbb Z^d;\mathfrak g)$ the symbol of $d_1^*d_1$ collapses to a scalar: with $q_\mu(k)=e^{ik_\mu}-1$ and $\lambda(k)=\sum_\mu|q_\mu|^2=4\sum_\mu\sin^2(k_\mu/2)$,
$$\widehat{d_1^*d_1}(k)=\lambda(k)I-q(k)\overline{q(k)}^{\,\mathsf T},\qquad \overline q\cdot\widehat X=0\ \Rightarrow\ \widehat{d_1^*d_1X}=\lambda(k)\widehat X .$$
Hence for $M=m^2I+t\,d_1^*d_1$ restricted to $\ker d_0^*$, a Fourier contour shift gives
$$\big\|G_{(x,\mu),(y,\nu)}\big\|_{\mathrm{op}}\ \le\ \frac{2}{m^2}\,e^{-\nu(m^2,t)\,|x-y|_1},\qquad \nu(m^2,t)=2\operatorname{arsinh}\!\Big(\frac{m}{\sqrt{8td}}\Big).$$

**(c) Exact (sharp) rate.** On $\mathbb Z^d$, the true asymptotic decay of every block of $(m^2I+\alpha\,d_1^*d_1)^{-1}$ along a coordinate axis, per unit $\mathrm{dist}_E$, is
$$\boxed{\ \theta_\star=\operatorname{arcosh}\Big(1+\frac{m^2}{2\alpha}\Big)\ }$$
with a power prefactor $\sim n^{-(d-1)/2}$. Therefore the certified Davies rate with $C_\partial\le C_0=18$ under-estimates the truth by a factor $\to\sqrt{18}=4.243$ as $m^2/\alpha\to0$, and the Neumann-series CT rate under-estimates it by an unbounded factor $\asymp\sqrt{18\alpha/m^2}$.

### Derivation

**(a) Davies proof.** Let $W_\lambda$ be the diagonal weight $(W_\lambda X)_b=e^{\lambda\phi_{b'}(b)}X_b$ and $L_\lambda:=W_\lambda LW_\lambda^{-1}$, so $(L_\lambda)_{b\tilde b}=e^{\lambda\Delta\phi}L_{b\tilde b}$, $\Delta\phi:=\phi_{b'}(b)-\phi_{b'}(\tilde b)$. Since $W_\lambda$ is positive diagonal, $L_{-\lambda}=L_\lambda^*$, and the symmetric perturbation
$$Q_\lambda:=\tfrac12(L_\lambda+L_{-\lambda})-L,\qquad (Q_\lambda)_{b\tilde b}=\big(\cosh(\lambda\Delta\phi)-1\big)L_{b\tilde b},\quad (Q_\lambda)_{bb}=0,$$
is self-adjoint with zero diagonal. Because $L$ has range 1, $L_{b\tilde b}\ne0$ forces $\mathrm{dist}_E(b,\tilde b)\le1$, so $|\Delta\phi|\in\{0,1\}$ by 1-Lipschitzness; the terms with $\Delta\phi=0$ **vanish identically** ($\cosh0-1=0$). Hence only level-crossing pairs contribute and the self-adjoint Schur bound gives $\|Q_\lambda\|\le C_\partial(\cosh\lambda-1)$.
Now solve $\partial_tu=-L_\lambda u$: $\frac{d}{dt}\|u\|^2=-2\Re\langle u,L_\lambda u\rangle=-2\langle u,(L+Q_\lambda)u\rangle\le2\|Q_\lambda\|\,\|u\|^2$ (using $L\succeq0$), so by Grönwall $\|e^{-tL_\lambda}\|\le e^{t\|Q_\lambda\|}$. Combine with the Laplace representation, valid since $L\succeq0$ in finite dimensions,
$$M^{-1}=\int_0^\infty e^{-m^2t}e^{-tL}\,dt\ \Longrightarrow\ W_\lambda M^{-1}W_\lambda^{-1}=\int_0^\infty e^{-m^2t}e^{-tL_\lambda}dt,$$
whence $\|W_\lambda M^{-1}W_\lambda^{-1}\|\le\int_0^\infty e^{-t(m^2-\|Q_\lambda\|)}dt=(m^2-\|Q_\lambda\|)^{-1}$ whenever $\|Q_\lambda\|<m^2$. Finally $(M^{-1})_{bb'}=e^{-\lambda\phi_{b'}(b)}(W_\lambda M^{-1}W_\lambda^{-1})_{bb'}$ since $\phi_{b'}(b')=0$; take norms. $\square$

**(b) Scalarization and contour shift.** For $X_{x,\mu}=e^{ik\cdot x}v_\mu$, $(d_1X)_{(x;\mu\nu)}=e^{ik\cdot x}(q_\mu v_\nu-q_\nu v_\mu)$, so
$$\sum_{\mu<\nu}|q_\mu v_\nu-q_\nu v_\mu|^2=|q|^2|v|^2-\big|\textstyle\sum_\nu\overline{q_\nu}v_\nu\big|^2,$$
i.e. the symbol is $\lambda(k)I-q\overline q^{\mathsf T}=\lambda(k)P_T(k)$. The constraint $d_0^*X=0$ reads $\overline q\cdot\widehat X=0$, which annihilates $q\overline q^{\mathsf T}$; hence the multiplier is the scalar $(m^2+t\lambda(k))^{-1}$. Shifting each $k_\mu\to k_\mu+i\nu\,\mathrm{sgn}(x_\mu-y_\mu)$ produces the factor $e^{-\nu|x-y|_1}$ and requires $\Re(m^2+t\lambda)\ge m^2/2$. Since $\Re\big(2-2\cos(k_\mu+i\nu)\big)=2-2\cos k_\mu\cosh\nu\ge-4\sinh^2(\nu/2)$, one needs $4td\sinh^2(\nu/2)\le m^2/2$, i.e. $\nu=2\operatorname{arsinh}\big(m/\sqrt{8td}\big)$, and the denominator bound yields the prefactor $2/m^2$. $\square$

**(c) Sharp rate.** [reconstructed] In Fourier, with $s_\mu(k)=e^{ik_\mu}-1$, $|s|^2=\sum_\mu(2-2\cos k_\mu)$ and $P_L=ss^\dagger/|s|^2$,
$$\widehat{M^{-1}}(k)=\frac{1}{m^2}P_L+\frac{1}{m^2+\alpha|s|^2}P_T=\frac{1}{m^2+\alpha|s|^2}\,I+\frac{\alpha}{m^2}\cdot\frac{s\,s^\dagger}{m^2+\alpha|s|^2}.$$
The apparent longitudinal singularity cancels: the second term has an *entire* trigonometric-polynomial numerator, so the whole symbol is analytic in a complex strip and the kernel decays exponentially (there is no power-law tail, contrary to naive expectation). The nearest singularity in complex $k_0$ at zero transverse momentum solves $m^2+\alpha(2-2\cosh\theta)=0$, i.e. $\cosh\theta=1+m^2/(2\alpha)$. Equivalently, integrating out transverse momenta gives $G(n,0,\dots,0)=\int\frac{d^{d-1}k_\perp}{(2\pi)^{d-1}}\,c(k_\perp)e^{-E(k_\perp)|n|}$ with $\cosh E(k_\perp)=1+\frac{m^2+\alpha\omega(k_\perp)}{2\alpha}$, minimized at $k_\perp=0$. Hence $\theta_\star=\operatorname{arcosh}(1+m^2/(2\alpha))$ and Laplace's method gives the $n^{-(d-1)/2}$ prefactor.
**Numerical confirmation** ($d=4$, $L=128$ in $k_0$, $48^3$ transverse, component $(\mu,\nu)=(1,1)$ along the $0$-axis): the local slope $\log(|G(n)|/|G(n+1)|)$ approaches $\theta_\star+\tfrac{3/2}{n}$:
| $m^2,\alpha$ | $\theta_\star$ | slope at $n{=}47$ | $\theta_\star+1.5/47$ |
|---|---|---|---|
| $0.05,1$ | 0.22314 | 0.25487 | 0.2551 |
| $0.3,1$ | 0.54110 | 0.57420 | 0.5730 |
| $1,10$ | 0.31492 | 0.34813 | 0.3468 |
Agreement to $3$–$4$ digits.
**Distance calibration.** For the pair $b=(0,\mu{=}1)$, $b'=(n\hat e_0,\mu{=}1)$ one has $\mathrm{dist}_E(b,b')=n$ exactly (verified by BFS on the link-adjacency graph, $d=4$, $L=10$), so $\theta_\star$ is directly comparable to the certified rates, which are stated per unit $\mathrm{dist}_E$.

### Constants and numbers

Sharp rate per unit dist_E along an axis: θ⋆ = arcosh(1 + m²/(2α)) = 2 arsinh(m/(2√α)).
Certified Davies rate with C_∂ ≤ C₀ = 18: arcosh(1 + m²/(36α)).
Certified CT rate: log(1 + m²/(36α)).
Ratio θ⋆ / η_Davies → √18 = 4.243 as m²/α → 0 (measured: 4.202 at m²/α = 0.25; 4.232 at 0.20; 4.240 at 0.015).
Horizontal-sector ℓ¹ rate (Lemma 3.1 of 04_helffer_sjostrand_and_greens_decay): ν = 2 arsinh(m/√(8td)); smaller than θ⋆ by √(2d) = √8 ≈ 2.83 in d = 4 (it controls the ℓ¹ distance in all directions simultaneously).
Exact off-diagonal row-sum in d = 4: C₀ = 18. The level-set restriction C_∂ can remove only the equal-distance co-plaquette neighbours, an O(1) (at most factor ≈ 2) gain, i.e. at most a factor √2 in η.
Benchmark: SU(3), β = 6 (m_H² = 0.5, α_W = 2): θ⋆ = 0.494933, η_Davies = 0.117783, η_CT = 0.006920.
Small-coupling asymptotics: η_Davies ≈ m_H/√(18 α_W) = g√N/(6√6); for SU(3), η_Davies ≈ 0.1179·g (exact at g = 1: 0.11778).

### Code

# (c) Exact axis decay rate of (m^2 + alpha d1*d1)^{-1} in d=4, transverse momenta summed.
import numpy as np, math

def axis_profile(L, m2, alpha, comp=(1,1), Lt=48):
    k0 = 2*np.pi*np.arange(L)/L
    kt = 2*np.pi*np.arange(Lt)/Lt
    g1, g2, g3 = np.meshgrid(kt, kt, kt, indexing='ij')
    w = (2-2*np.cos(g1)) + (2-2*np.cos(g2)) + (2-2*np.cos(g3))
    s = [None, np.exp(1j*g1)-1, np.exp(1j*g2)-1, np.exp(1j*g3)-1]
    mu, nu = comp
    H = np.empty(L, complex)
    for i, a in enumerate(k0):
        s0 = np.exp(1j*a) - 1
        den = m2 + alpha*(abs(s0)**2 + w)
        smu = s0 if mu == 0 else s[mu]; snu = s0 if nu == 0 else s[nu]
        H[i] = ((1.0/den)*(mu == nu) + (alpha/m2)*smu*np.conj(snu)/den).mean()
    return np.fft.ifft(H).real

for m2, alpha in [(1.,1.), (.3,1.), (.05,1.), (1.,10.)]:
    p = np.abs(axis_profile(128, m2, alpha)[1:50])
    slope = math.log(p[45]/p[46])
    print(f"m2={m2} a={alpha}: arcosh(1+m2/2a)={math.acosh(1+m2/(2*alpha)):.5f} "
          f"local slope at n=46: {slope:.5f}  (predicted {math.acosh(1+m2/(2*alpha))+1.5/46:.5f})")

# dist_E calibration: BFS on the link-adjacency graph confirms
#   dist_E((0,mu=1), (n*e_0, mu=1)) = n     for n = 0..5
#   dist_E((0,mu=1), (n*e_1, mu=1)) = n+1   (offset along the link's own direction)

**Caveat.** The Davies/level-set refinement is only sketched in the corpus (three near-duplicate notes, no theorem); the file that is rigorous (Appendix G) deliberately uses the weaker O(m²) rate, so the headline chain never benefits from it. The sharp rate θ⋆ and the numerical confirmation are mine. Note also that one corpus simulation note reports C₀ = 43.91 for d₁*d₁ — that value is wrong; the correct value is exactly 18.

**Why it matters.** It converts a schematic 'exponential decay' into a fully explicit correlation length, quantifies exactly how much the certified bound loses (a factor √C₀ = 4.24, not more), and shows that no refinement of Combes–Thomas can change the β-scaling — the certified rate is Θ(g) whichever variant is used, which is what drives the continuum obstruction.

---

## 8. Localization algebra: conditional clustering ⇒ unconditional clustering (Appendix I / Core-8, full proof)

`status: solid` · `kind: theorem`

### Statement

Let $(\Omega,\mathcal F,\mu)$ be a probability space and $K\in\mathcal F$ with $0<\mu(K)<1$; write $\mu_K:=\mu(\cdot\mid K)$, $\mu_{K^c}:=\mu(\cdot\mid K^c)$, $\Delta_KF:=\mu_K(F)-\mu_{K^c}(F)$. For bounded measurable $F,G$:

1. **(Exact decomposition)** $\mathrm{Cov}_\mu(F,G)=\mu(K)\,\mathrm{Cov}_{\mu_K}(F,G)+\mu(K^c)\,\mathrm{Cov}_{\mu_{K^c}}(F,G)+\mu(K)\mu(K^c)\,(\Delta_KF)(\Delta_KG).$
2. **(Sup-norm localization)** $\big|\mathrm{Cov}_\mu(F,G)\big|\le\big|\mathrm{Cov}_{\mu_K}(F,G)\big|+8\|F\|_\infty\|G\|_\infty\,\mu(K^c).$
3. **(Distance conversion)** On $\Lambda_L$ with $d=4$, every link lies on at least one plaquette and each plaquette has $m_\partial=4$ links, so $|E(\Lambda_L)|\le m_\partial|P(\Lambda_L)|$; since the link-adjacency graph is connected with $|E|$ vertices, $\mathrm{dist}_E(A,B)\le|E(\Lambda_L)|\le m_\partial|P(\Lambda_L)|$, hence $e^{-c|P(\Lambda_L)|}\le e^{-(c/m_\partial)\mathrm{dist}_E(A,B)}$.
4. **(Unconditional clustering)** If additionally $\mu(K^c)\le e^{-c_{\mathrm{typ}}|P(\Lambda_L)|}$ and the conditional clustering bound holds with exponent $\eta$ and prefactor $\tfrac{2}{m_H^2}\mathsf L_E(F)\mathsf L_E(G)$, then
$$\big|\mathrm{Cov}_{\Lambda_L,\beta}(F,G)\big|\le\Big[\tfrac{2}{m_H^2}\mathsf L_E(F)\mathsf L_E(G)+8\|F\|_\infty\|G\|_\infty\Big]\exp\Big(-\min\big\{\eta,\ \tfrac{c_{\mathrm{typ}}}{m_\partial}\big\}\,\mathrm{dist}_E(A,B)\Big),$$
with an exponent independent of the volume.

### Derivation

**1.** Write $\alpha:=\mu(K)$, so $\mu=\alpha\mu_K+(1-\alpha)\mu_{K^c}$ and, with $A=\mu_K(F),B=\mu_{K^c}(F),C=\mu_K(G),D=\mu_{K^c}(G)$,
$$\mu(F)\mu(G)=\alpha^2AC+\alpha(1-\alpha)(AD+BC)+(1-\alpha)^2BD.$$
Subtract from $\mu(FG)=\alpha\mu_K(FG)+(1-\alpha)\mu_{K^c}(FG)$, add and subtract $\alpha AC$ and $(1-\alpha)BD$, and regroup. The first group is $\alpha\,\mathrm{Cov}_{\mu_K}+(1-\alpha)\mathrm{Cov}_{\mu_{K^c}}$; the remainder is
$$\alpha(1-\alpha)AC+\alpha(1-\alpha)BD-\alpha(1-\alpha)(AD+BC)=\alpha(1-\alpha)(A-B)(C-D).\ \square$$
**2.** For any probability $\nu$, $|\mathrm{Cov}_\nu(F,G)|\le\|F-\nu F\|_\infty\|G-\nu G\|_\infty\le4\|F\|_\infty\|G\|_\infty$; also $|\Delta_KF|\le2\|F\|_\infty$, $|\Delta_KG|\le2\|G\|_\infty$. Insert into 1., use $\mu(K)\le1$, and add the two error terms: $4+4=8$. $\square$
**3.** Any path in a finite graph visits at most $|E|$ vertices, so $\mathrm{dist}_E\le|E|-1<|E|$. Each link $(x,\mu)$ lies on the plaquette $(x;\mu\wedge\nu,\mu\vee\nu)$ for any $\nu\ne\mu$ (exists since $d=4\ge2$); counting (plaquette, link) incidences gives $|E|\le m_\partial|P|$. Monotonicity of $\exp$ finishes. $\square$
**4.** Combine 2., the assumed conditional bound, 3. and $e^{-\eta_ir}\le e^{-\min_i\eta_i\,r}$. $\square$

### Constants and numbers

m_∂ = 4. Error constant 8 (= 4 from Cov on K^c + 4 from the mean-jump term). Unified exponent η_⋆ = min{η_clustering, c_typ/m_∂} = min{log(1 + m_H²/(36α_W)), c_typ/4} (or with arcosh for the Davies variant). Prefactor: (2/m_H²)·L_E(F)L_E(G) + 8‖F‖_∞‖G‖_∞.

**Caveat.** Step 3 is extremely wasteful — it converts a volume-scale bound into a distance-scale bound by the crudest possible route — but it is correct and suffices because c_typ|P| ≫ dist_E. The whole item is conditional on the typicality assumption μ(K^c) ≤ e^{−c_typ|P|}, which is FALSE for the good set the hinge needs (see the good-set obstruction item).

**Why it matters.** It is the clean, fully proved measure-theoretic hinge between 'analysis on a nice set' and 'a statement about the actual Gibbs measure'. Reusable verbatim in any conditioning-based argument.

---

## 9. Reflection positivity, OS reconstruction, and the extraction of a Hamiltonian gap from Euclidean-time decay (Appendices K, L; Core-9)

`status: conditional` · `kind: theorem`

### Statement

**RP (proved).** Assume $L_0$ even. Let $\vartheta(x_0,\vec x)=(1-x_0,\vec x)$ be the link reflection, $\Theta$ the induced configuration involution, $(\theta F)(U):=\overline{F(\Theta U)}$, and $\mathcal A_+$ the bounded cylinder observables depending only on links at nonnegative time. Then the Wilson Gibbs measure is reflection positive:
$$\mathbb E_{\Lambda_L,\beta}\big[(\theta F)\,F\big]\ \ge\ 0\qquad\text{for all }F\in\mathcal A_+ .$$

**OS interface (external input L.2.6).** Under the OS structural axioms — time-translation invariance $\mu(\tau_nF)=\mu(F)$; reflection invariance $\mu(\theta F)=\overline{\mu(F)}$; reflection positivity; $\Theta\tau_n^\Omega=\tau_{-n}^\Omega\Theta$; $\tau_n(\mathcal A_+)\subseteq\mathcal A_+$ for $n\ge0$ — there exist $\mathcal H_{\mathrm{OS}}=\overline{\mathcal A_+/\mathcal N}$ (with $\langle F,G\rangle_{\mathrm{OS}}=\mu((\theta F)G)$, $\mathcal N$ its null space), a vacuum $\Omega=[1]$, and a positive self-adjoint contraction $0\le T\le I$ with $T^n[F]=[\tau_nF]$ and $\langle[F],T^n[G]\rangle_{\mathrm{OS}}=\mu((\theta F)(\tau_nG))$.

**Hamiltonian.** For $a>0$ there is a unique self-adjoint $H\ge0$ with $T=e^{-aH}$.

**Gap extraction (Theorem L.4.7).** If there is $\eta>0$ such that for every bounded $F\in\mathcal A_+$ there is $C(F)<\infty$ with $|\mathrm{Cov}_\mu(\theta F,\tau_nF)|\le C(F)e^{-\eta n}$ for all integers $n\ge0$, then
$$\sigma(H)\cap\big(0,\eta/a\big)=\emptyset,\qquad\text{i.e.}\qquad \mathrm{gap}(H)\ \ge\ \frac{\eta}{a},\qquad\text{and}\qquad \ker H=\mathbb C\,\Omega .$$

**Spatial ⇒ temporal decay (Core-9.5).** $t(b):=x_0$ is 1-Lipschitz for link adjacency, so $\mathrm{dist}_E(A,B)\ge\max\{0,t_{\min}(B)-t_{\max}(A)\}$; for $F\in\mathcal A_+$ one has $t_{\max}(\mathrm{supp}_E\theta F)\le0$ and $t_{\min}(\mathrm{supp}_E\tau_{n\hat e_0}F)\ge n+1$, hence $\mathrm{dist}_E\ge n+1$ and spatial exponential clustering with rate $\eta_\star$ implies the temporal hypothesis with the same rate.

**Thermodynamic limit (Core-9.2–9.4).** $\Omega_\infty=G^{E(\mathbb Z^4)}$ is compact metrizable; the periodic embeddings $\widetilde\mu_L=(\iota_L)_\#\mu_{\Lambda_L,\beta}$ have weak limit points; translation invariance, reflection invariance, reflection positivity and volume-uniform exponential clustering all pass to any limit point.

### Derivation

**RP.** The proof (Appendix K, Theorem K.5.1) is the standard Osterwalder–Seiler argument, correctly executed: (i) rewrite $\mu\propto\prod_pw_\beta(U_p)dU$ with $w_\beta=e^{-\Phi_\beta}$; (ii) split $U=(U_-,U_0,U_+)$ and $P=P_+\sqcup P_0\sqcup P_-$, plaquettes in $P_\pm$ depending only on $U_\pm$; (iii) for each straddling $p\in P_0$ write $U_p=(V_p^-)^{-1}V_p^+$ with $V^+_p$ a function of $(U_+,U_0)$ and $V^-_p$ of $(U_-,U_0)$, and expand $w_\beta(g^{-1}h)=\sum_\alpha\overline{f_\alpha(g)}f_\alpha(h)$ (a positive-definite class function has a character/sum-of-squares expansion with nonnegative coefficients, convergent uniformly); (iv) multiply over $p\in P_0$ and integrate out $U_0$ last, obtaining $\mathbb E[(\theta F)F]=\sum_{\boldsymbol\alpha}\int|\,\cdot\,|^2\ge0$. Only the support restriction $F\in\mathcal A_+$ is used; no gauge invariance is needed.

**$T=e^{-aH}$.** Spectral theorem for the bounded self-adjoint $T$ with $\sigma(T)\subseteq[0,1]$: define $f(\lambda)=-(1/a)\log\lambda$ on $(0,1]$, $f(0)=+\infty$, and $H:=f(T)$ by Borel functional calculus. Then $e^{-aH}=\int e^{-af(\lambda)}dE_T(\lambda)=\int\lambda\,dE_T=T$, and $H\ge0$. Uniqueness: $H_i=-(1/a)\log T$ for both. $\square$

**Spectral-support lemma (L.3.2).** Let $\nu_\psi(B)=\langle\psi,E_H(B)\psi\rangle$. Suppose $\langle\psi,e^{-naH}\psi\rangle\le C_\psi e^{-mna}$ for all integers $n\ge0$ but $\nu_\psi([0,m))>0$. Pick $\varepsilon\in(0,m)$ with $\delta:=\nu_\psi([0,m-\varepsilon])>0$. Then
$$\langle\psi,e^{-naH}\psi\rangle=\int e^{-na\lambda}d\nu_\psi\ \ge\ \int_{[0,m-\varepsilon]}e^{-na\lambda}d\nu_\psi\ \ge\ \delta e^{-(m-\varepsilon)na},$$
and $\delta e^{\varepsilon na}\to\infty$ contradicts the upper bound. Hence $E_H([0,m))\psi=0$. $\square$

**Gap extraction.** Fix bounded $F\in\mathcal A_+$, set $F^\circ=F-\mu(F)$ and $\psi:=[F^\circ]$. Since $\Omega=[1]$ and $\theta1=1$, $\langle\Omega,[F]\rangle_{\mathrm{OS}}=\mu(F)$, so $\psi\perp\Omega$. By the transfer identity,
$$\langle\psi,e^{-naH}\psi\rangle_{\mathrm{OS}}=\langle\psi,T^n\psi\rangle=\mu\big((\theta F^\circ)(\tau_nF^\circ)\big)=\mathrm{Cov}_\mu(\theta F,\tau_nF),$$
using $\mu(\tau_nF)=\mu(F)$, $\mu(\theta F)=\overline{\mu(F)}$. The hypothesis bounds this by $C(F)e^{-\eta n}=C(F)e^{-(\eta/a)na}$, so the spectral lemma with $m=\eta/a$ gives $E_H([0,\eta/a))\psi=0$. The classes $[F^\circ]$ are dense in $\Omega^\perp$: if $[F_k]\to\chi\in\Omega^\perp$ then $\mu(F_k)=\langle\Omega,[F_k]\rangle\to0$, so $[F_k^\circ]=[F_k]-\mu(F_k)\Omega\to\chi$. Since $E_H([0,\eta/a))$ is a bounded projection vanishing on a dense subset of $\Omega^\perp$, it vanishes on $\Omega^\perp$; hence $\sigma(H)\cap(0,\eta/a)=\emptyset$. Finally $E_H(\{0\})\le E_H([0,\eta/a))$ so $\ker H\cap\Omega^\perp=\{0\}$, while $T\Omega=\Omega$ gives $\Omega\in\ker H$; thus $\ker H=\mathbb C\Omega$. $\square$

**Time Lipschitz property.** If $b\sim b'$ they lie on a common plaquette, which spans a coordinate 2-plane whose vertices' time coordinates differ by at most 1; chaining along a geodesic path of length $k$ gives $|t(b)-t(b')|\le k=\mathrm{dist}_E(b,b')$. $\square$

**Permanence under weak limits.** $\Omega_\infty$ is compact metrizable (product of compact metric $G$ over a countable index set; diagonal extraction gives sequential compactness), so $\mathcal P(\Omega_\infty)$ is weakly compact and limit points exist. For a cylinder $F$ and $L$ large enough that $\mathrm{supp}_EF$ embeds without wrap-around, $F\circ\iota_L$ is a finite-volume cylinder observable; each of the four properties (translation invariance, reflection invariance, $\int(\theta F)F\ge0$, and the covariance bound) is an inequality/equality between integrals of bounded continuous functions, hence survives weak convergence. Also, for large $L$ the periodic $\mathrm{dist}_E$ equals the $\mathbb Z^4$ distance (shortest paths do not wrap), so the exponent is preserved. $\square$

### Constants and numbers

gap(H) ≥ η_⋆/a with η_⋆ = min{ log(1 + m_H²/(36 α_W)), c_typ/m_∂ } (or arcosh in place of log for the Davies route), m_∂ = 4.
Illustrative plug-in, SU(3) at β = 6 (a ≈ 0.093 fm, g² = 1, m_H² = 1/2, α_W = 2, B_S = 36), assuming c_typ/4 is not the binding constraint:
  Davies route: η_⋆ = 0.11778  →  gap ≥ 0.11778/0.093 fm = 1.267 fm⁻¹ ≈ 250 MeV.
  CT route:     η_⋆ = 0.006920 →  gap ≥ 14.7 MeV.
  Sharp deterministic rate (not certified for L^(1)): 0.4949 → 1050 MeV.
(The physical scalar glueball is ≈ 1700 MeV. These numbers are illustrative only — the chain is conditional on hypotheses that are false; see the obstruction items.)
Requires L₀ even (Assumption K.1.1).

**Caveat.** OS reconstruction itself (existence of T with the transfer identity) is imported as External Input L.2.6, not proved. Everything downstream of it (the functional calculus, the spectral-support lemma, the density argument, the gap theorem) is proved in full and is correct.

**Why it matters.** This is the second fully clean block of the chain. The RP proof is genuine Osterwalder–Seiler, and the 'time decay ⇒ spectral gap' argument is complete, quantitative and correctly handles the density issue that similar arguments often skip. It converts a Euclidean statement into a genuine Hamiltonian statement with an explicit rate.

---

## 10. Master conditional theorem: the full fixed-cutoff chain with every hypothesis explicit (repaired form)

`status: conditional` · `kind: theorem`

### Statement

Fix $d=4$, a compact gauge group $G$ with faithful $\rho:G\to U(n)$, the metric normalization $\langle X,Y\rangle_{\mathfrak g}=-\Re\operatorname{Tr}(d\rho X\,d\rho Y)$, a lattice spacing $a>0$, a coupling $\beta>0$, and set $m_H^2=\kappa_G/3$, $\alpha_W=\beta/n$, $\nu_P=6$, $m_\partial=4$.

Assume:

**(H0) Ricci floor.** $\mathrm{Ric}_G\succeq\kappa_G\,g_G$ with $\kappa_G>0$ (true for semisimple $G$; $\kappa_G=N/2$ for $\mathrm{SU}(N)$).

**(H1) Good set.** For each periodic $\Lambda_L$ ($L_0$ even) a measurable, gauge-invariant $\mathcal K_{\Lambda_L}\subseteq\mathcal M_{\Lambda_L}$ with $0<\mu_{\Lambda_L,\beta}(\mathcal K_{\Lambda_L})<1$.

**(H2) Scalar hinge on the good set.** $\mathrm{Ric}_{\mu_{\Lambda_L,\beta}}(U)=\mathrm{Ric}_{g_{\Lambda_L}}(U)+\nabla^2S_{\Lambda_L,\beta}(U)\succeq m_H^2\,\mathrm{Id}$ for all $U\in\mathcal K_{\Lambda_L}$. (The corpus's matrix hinge $\succeq m_H^2\mathrm{Id}+\tfrac{\alpha_W}{2}d_1^*d_1$ implies this; only the scalar part is used.)

**(H3) Uniform row-sum bound.** $B_S:=\sup_L\sup_{U\in\mathcal K_{\Lambda_L}}\sup_b\sum_{b'\ne b}\|(\nabla^2S_{\Lambda_L,\beta}(U))_{bb'}\|_{\mathrm{op}}<\infty$. (Automatic: $B_S\le 3\nu_P\alpha_W\sup_{g\in G^4}\|D^2F(g)\|$, and $B_S=18\alpha_W$ at $U^{(0)}$.)

**(H4) Conditioned HS machinery.** External Inputs F.2, F.7, F.12 and F.20 hold for $\Omega=\mathcal K_{\Lambda_L}$: a $\mu^{\mathcal K}$-symmetric reflecting (Neumann) generator exists with the associated integration-by-parts and Poisson solvability, so the conditioned HS identity $\mathrm{Cov}_{\mu^{\mathcal K}}(F,G)=\int\langle\nabla F,(\mathcal L^{(1),\mathcal K})^{-1}\nabla G\rangle d\mu^{\mathcal K}$ holds.

**(H5) Typicality.** $\mu_{\Lambda_L,\beta}(\mathcal K_{\Lambda_L}^c)\le e^{-c_{\mathrm{typ}}|P(\Lambda_L)|}$ for all large volumes, some $c_{\mathrm{typ}}>0$.

**(H6) OS reconstruction.** External Input L.2.6 for the infinite-volume limit point.

Define
$$\eta_\star:=\min\Big\{\operatorname{arcosh}\Big(1+\frac{m_H^2}{2B_S}\Big),\ \frac{c_{\mathrm{typ}}}{m_\partial}\Big\}\ \ \Big(\ \ge\min\Big\{\log\Big(1+\frac{m_H^2}{36\alpha_W}\Big),\frac{c_{\mathrm{typ}}}{4}\Big\}\Big).$$

**Conclusion.** For every smooth cylinder pair $F,G$ with link supports $A,B$, uniformly in the volume,
$$\big|\mathrm{Cov}_{\Lambda_L,\beta}(F,G)\big|\ \le\ \Big[\tfrac{2}{m_H^2}\mathsf L_E(F)\mathsf L_E(G)+8\|F\|_\infty\|G\|_\infty\Big]e^{-\eta_\star\,\mathrm{dist}_E(A,B)};$$
every periodic thermodynamic limit point $\mu_\infty$ is translation invariant, reflection invariant, reflection positive and satisfies the same clustering bound on $E(\mathbb Z^4)$; and the reconstructed OS Hamiltonian satisfies
$$\boxed{\ \sigma(H)\cap\big(0,\eta_\star/a\big)=\emptyset,\qquad \mathrm{gap}(H)\ \ge\ \frac{\eta_\star}{a},\qquad \ker H=\mathbb C\Omega.\ }$$

### Derivation

Chain of implications, each proved in the items above:

$$\underbrace{\text{(H0)+(H2)}}_{\text{Bakry–Émery floor on }\mathcal K}\ \xrightarrow[\text{Bochner}]{\ \mathcal L^{(1)}\succeq\mathrm{Ric}_\mu\ }\ \underbrace{a_0(\mathcal L^{(1),\mathcal K})\ge m_H^2}_{\text{HS item, Lemma F.9}}$$
$$\underbrace{\text{(H3)}+\text{product structure}}_{\text{Repair item, Step 2}}\ \Longrightarrow\ R(\mathcal L^{(1),\mathcal K})=1,\ B_0\le B_S$$
$$\xrightarrow[\text{arbitrary Hilbert fiber}]{\text{Combes–Thomas / Davies}}\ \big\|\big((\mathcal L^{(1),\mathcal K})^{-1}\big)_{bb'}\big\|\le\tfrac{2}{m_H^2}e^{-\eta\,\mathrm{dist}_E(b,b')},\ \eta=\operatorname{arcosh}\big(1+\tfrac{m_H^2}{2B_S}\big)$$
$$\xrightarrow[\text{(H4): conditioned HS identity + cylinder supports}]{}\ \big|\mathrm{Cov}_{\mu^{\mathcal K}}(F,G)\big|\le\tfrac{2}{m_H^2}e^{-\eta\,\mathrm{dist}_E(A,B)}\mathsf L_E(F)\mathsf L_E(G)$$
$$\xrightarrow[\text{(H5): }\mu(\mathcal K^c)\le e^{-c_{\rm typ}|P|},\ \mathrm{dist}_E\le m_\partial|P|]{\text{Appendix I localization}}\ \big|\mathrm{Cov}_{\Lambda_L,\beta}(F,G)\big|\le[\cdots]e^{-\eta_\star\mathrm{dist}_E(A,B)}$$
$$\xrightarrow[\text{weak limits of bounded continuous functionals}]{\text{Core-9.2–9.4}}\ \text{same bound for every }\mu_\infty,\ \text{with OS axioms (Appendix K + permanence)}$$
$$\xrightarrow[t(\cdot)\text{ 1-Lipschitz}]{\text{Core-9.5: }\mathrm{dist}_E(\mathrm{supp}\,\theta F,\mathrm{supp}\,\tau_{n\hat e_0}F)\ge n+1}\ \big|\mathrm{Cov}_{\mu_\infty}(\theta F,\tau_{n\hat e_0}F)\big|\le C(F)e^{-\eta_\star n}$$
$$\xrightarrow[\text{(H6)}]{\text{Appendix L: }T=e^{-aH},\ \text{spectral-support lemma, density in }\Omega^\perp}\ \mathrm{gap}(H)\ge\eta_\star/a .$$

**Deviations from the corpus's own statement of the chain, and why.**
1. The corpus routes the decay through the *deterministic* comparison operator $M^{\mathrm{hinge}}$; that step is invalid (see the counterexample item). Here Combes–Thomas is applied to $\mathcal L^{(1),\mathcal K}$ itself. All constants are preserved.
2. Consequently the Maxwell part of the hinge is not used: (H2) needs only the scalar floor.
3. The optional "horizontal restriction" (F.18 / Core-6.5.2) is dropped: it is valid only at the vacuum.
4. $\eta_\star$ is stated with $\operatorname{arcosh}$ (Davies) rather than $\log$ (Neumann series); the Davies argument transfers verbatim and is a factor $\asymp\sqrt{2B_S/m_H^2}$ better.

**Status of the hypotheses.** (H0) is a theorem. (H3) is a theorem. (H2) is a theorem given the third-derivative estimate, on a good set of radius $O(1/\beta)$. (H4) is a genuine, standard-but-unverified analytic input (reflecting diffusion on a domain with corners). (H5) is **false** for the good set that (H2) requires — see the next item. (H6) is standard but imported.

### Constants and numbers

η_⋆ = min{arcosh(1 + m_H²/(2B_S)), c_typ/4}, B_S = 18α_W at the vacuum.
gap(H) ≥ η_⋆/a.
Explicit: with m_H² = N/6, α_W = 2/g², B_S = 36/g²:
  η_Davies = arcosh(1 + N g²/216) ≈ g√N/(6√6) for small g.
  SU(3): η ≈ 0.1179 g; SU(2): η ≈ 0.0962 g.
Prefactor (2/m_H²)L_E(F)L_E(G) + 8‖F‖_∞‖G‖_∞ with 2/m_H² = 12/N.
Volume-uniform: no constant depends on L.

**Caveat.** The theorem is a genuine conditional theorem with a correct proof, but hypothesis (H5) is inconsistent with hypothesis (H2) for the good sets the argument can supply — the chain is conditional on a set of hypotheses that cannot all hold. It is still valuable as a template: any other route to (H2)+(H5) with a volume-uniform good set would immediately yield the conclusion.

**Why it matters.** This is the real, extractable product of the whole corpus on this topic: a correctly proved implication with every hypothesis named and every constant explicit, from a local curvature statement to a Hamiltonian spectral gap. It also makes the failure diagnosable: exactly two hypotheses ((H2) with a volume-uniform radius, and (H5)) carry all the risk, and they are in direct conflict.

---

## 11. Obstruction I: the hinge's good set has radius O(1/β) while typical plaquettes fluctuate at scale β^{-1/2}, so the typicality hypothesis (H5) is false

`status: solid` · `kind: obstruction`

### Statement

Let $\mathcal K_{\Lambda,\beta}(r)$ be either the linkwise small-field set $\{d_G(U_b,\mathbf 1)<r\ \forall b\}$ or the plaquette small-field set $\{\|\log U_p\|\le r\ \forall p\}$. Then:

**(i) (Radius forced by the hinge.)** Any version of the matrix-hinge argument that produces a *deterministic* comparison operator on all of $\mathcal C^1(\Lambda;\mathfrak g)$ requires
$$r\ \le\ r^{\mathrm{hinge}}=\Theta\!\big(\kappa_G/\beta\big),$$
because the Hessian error term is isotropic ($-C\beta r\,\mathrm{Id}$) while on $\mathrm{im}(d_0)$ the Maxwell stiffness vanishes identically, leaving only the $\beta$-independent reservoir $\kappa_G$ to absorb it.

**(ii) (Typical fluctuation scale.)** In the Gaussian (leading large-$\beta$) regime of the Wilson measure on the periodic 4-torus,
$$\mathbb E\big|\mathbf Y_p\big|^2_{\mathfrak g}\ \longrightarrow\ \frac{\operatorname{rank}(d_1)\cdot\dim\mathfrak g}{\alpha_W\,|P(\Lambda)|}\ =\ \frac{n\,\dim\mathfrak g}{2\beta}\big(1+O(|\Lambda|^{-1})\big),\qquad \mathbf Y_p=\log U_p,$$
using $\operatorname{rank}d_1=3|\Lambda|-3$, $|P|=6|\Lambda|$, $\alpha_W=\beta/n$. Hence $|\mathbf Y_p|\asymp\beta^{-1/2}$, which exceeds $r^{\mathrm{hinge}}=\Theta(1/\beta)$ by a factor $\asymp\beta^{1/2}\to\infty$.

**(iii) (Volume.)** Even at the more generous radius $r\asymp\beta^{-1/2}$, the good set is a **sup** over $|P(\Lambda)|=6|\Lambda|$ plaquettes of quantities with Gaussian tails at scale $\beta^{-1/2}$, so $\sup_p|\mathbf Y_p|\asymp\beta^{-1/2}\sqrt{\log|P(\Lambda)|}\to\infty$ in the volume: for any fixed $r$ and $\beta$, $\mu_{\Lambda,\beta}(\mathcal K_{\Lambda,\beta}(r))\to0$ as $|\Lambda|\to\infty$.

**Conclusion.** Assumption A.11.2 / Core-8.2.1, $\mu(\mathcal K^c)\le e^{-c_{\mathrm{typ}}|P(\Lambda)|}$, is not merely unproven: it is false for the good sets on which the hinge can hold. The localization inequality $|\mathrm{Cov}_\mu|\le|\mathrm{Cov}_{\mu_{\mathcal K}}|+8\|F\|_\infty\|G\|_\infty\mu(\mathcal K^c)$ becomes vacuous because $\mu(\mathcal K^c)\to1$.

### Derivation

**(i)** From the hinge item: $R_W(r)=\tfrac{\beta}{n}2\nu_PM_3(r_\star)r$ and the hinge requires $R_W(r)\le\kappa_G-m_H^2=2m_H^2$. Crucially, the error is a multiple of the identity, so it must be absorbed by the identity part of the comparison operator. On $\mathrm{im}(d_0)$ we have $d_1^*d_1=0$ (from $d_1d_0=0$), so on those directions the hinge asserts $\mathrm{Ric}_\mu\succeq m_H^2\mathrm{Id}$ with only $\kappa_G-C\beta r$ available. Hence $r\le 2m_H^2n/(2\nu_PM_3\beta)=\Theta(1/\beta)$. The same constraint appears independently in `Core_5` ($C_{\rm WH}\beta r_\beta\le 2m_H^2$, whose own remedy is to set $r_\beta=r_{\rm sf}\min\{1,\beta^{-1}\}$) and in `EXCITING_01` §4.1.

**(ii)** [reconstructed] Expand $U_b=\exp(X_b)$ near the vacuum. To leading order in $1/\beta$ the Wilson measure is the Gaussian with quadratic form $\tfrac{\alpha_W}{2}|d_1X|^2$ on $\mathcal C^1$, degenerate along $\ker d_1$; the covariance of $X$ on the non-degenerate sector is $\alpha_W^{-1}(d_1^*d_1)^+$. Hence $\mathbf Y=d_1X$ has covariance
$$\mathrm{Cov}(\mathbf Y)=\alpha_W^{-1}\,d_1(d_1^*d_1)^+d_1^*=\alpha_W^{-1}P_{\mathrm{im}\,d_1}\otimes\mathrm{Id}_{\mathfrak g},$$
so $\sum_p\mathbb E|\mathbf Y_p|^2=\alpha_W^{-1}\operatorname{rank}(d_1)\dim\mathfrak g$. On the periodic 4-torus, per $\mathfrak g$-component, $\dim\mathcal C^1=4|\Lambda|$, $\dim\mathrm{im}(d_0)=|\Lambda|-1$, $\dim H^1=4$, so $\operatorname{rank}d_1=4|\Lambda|-(|\Lambda|-1)-4=3|\Lambda|-3$. With $|P|=6|\Lambda|$,
$$\mathbb E|\mathbf Y_p|^2\approx\frac{n}{\beta}\cdot\frac{3|\Lambda|\dim\mathfrak g}{6|\Lambda|}=\frac{n\dim\mathfrak g}{2\beta}.$$
For $\mathrm{SU}(2)$ ($n=2$, $\dim\mathfrak g=3$): $\mathbb E|\mathbf Y_p|^2=3/\beta$. For $\mathrm{SU}(3)$ ($n=3$, $\dim\mathfrak g=8$): $12/\beta$.
**Sanity check against the small-field chart.** At $\mathrm{SU}(2)$, $\beta=2.5$: $\mathbb E|\mathbf Y_p|^2=1.2$, so $|\mathbf Y_p|\approx1.10$, while $\iota_G=\sqrt2\pi\approx4.44$, $r_{\log}=\iota_G/2\approx2.22$ and $r_{\mathrm{sf}}\le\iota_G/8\approx0.555$. Typical plaquettes are already *outside* the canonical small-field radius at the physically relevant coupling, before any hinge constraint is imposed. At $\mathrm{SU}(3)$, $\beta=6$: $\mathbb E|\mathbf Y_p|^2=2$, $|\mathbf Y_p|\approx1.41$.

**(iii)** Each $|\mathbf Y_p|^2$ is (to leading order) a quadratic form in Gaussians with $\mathbb E|\mathbf Y_p|^2\asymp1/\beta$ and sub-exponential tails $\mathbb P(|\mathbf Y_p|>u)\le e^{-c\beta u^2}$; there are $6|\Lambda|$ of them with only finite-range correlations, so $\sup_p|\mathbf Y_p|$ concentrates at $\asymp\beta^{-1/2}\sqrt{\log|\Lambda|}$. Hence for fixed $r$ the probability of the sup-event tends to $0$; a lower-bound argument along a set of plaquettes with pairwise disjoint "private" links (conditioning on all other links and using that each conditional law has a density bounded above w.r.t. Haar) gives an explicit exponential rate in $|\Lambda|$ for small enough $r$.

**What the corpus itself says.** `EXCITING_05_LOCALIZATION_AVERAGED_BADNESS` states the mechanism verbatim: "A max-event $\{\max_p\theta_p\le\varepsilon\}$ has a complement controlled only by a union bound, typically producing a factor $|P(\Lambda)|$. That factor is exactly what later poisons uniform bounds." The only typicality bound anywhere in the corpus (`Appendix J`, `WILSON/archive`) proves $\mu(K(\varepsilon)^c)\le e^{-c_{\rm typ}|P|}$ for the **averaged** good set $K(\varepsilon)=\{\text{mean plaquette potential}\le\varepsilon\}$, and then instructs the reader to "set $K_{\Lambda_L}:=K_{\Lambda_L}(\varepsilon)$" — substituting the average set for the sup set. On the average set the *pointwise* matrix hinge fails: an average constraint permits $\varepsilon|\Lambda|$ arbitrarily bad plaquettes, and the hinge is a pointwise matrix inequality. This substitution is where the chain breaks.

### Constants and numbers

r^hinge = 2m_H² n/(2ν_P M₃ β) = κ_G n/(3ν_P M₃ β) = Θ(1/β).
Typical plaquette log: E|Y_p|² = n·dim(g)/(2β) + O(1/|Λ|). SU(2): 3/β. SU(3): 12/β.
SU(2) at β = 2.5: E|Y_p|² = 1.2, |Y_p| ≈ 1.10, vs ι_G = √2π ≈ 4.443, r_log ≈ 2.22, r_sf ≲ 0.555.
SU(3) at β = 6: E|Y_p|² = 2.0, |Y_p| ≈ 1.41.
Mismatch factor between the allowed radius and the typical fluctuation: Θ(β^{1/2}).
Volume factor: sup over |P(Λ)| = 6|Λ| plaquettes ⟹ sup_p|Y_p| ≍ β^{−1/2}√(log|Λ|) → ∞.
Rank count on the 4-torus: rank d₁ = 3|Λ| − 3 per g-component; dim im d₀ = |Λ| − 1; dim H¹ = 4.

**Caveat.** Part (ii) is the leading-order Gaussian computation, exact only as β → ∞; part (iii)'s exponential-in-volume rate is sketched (the private-link conditioning argument gives an explicit rate only for r small relative to β). The scaling conclusions are robust; the constants in (iii) are not sharp.

**Why it matters.** This is the decisive structural obstruction for the chain: the two hypotheses the chain needs — a pointwise hinge (which forces radius O(1/β)) and typicality (which needs radius ≫ β^{-1/2}·√log|Λ|) — are quantitatively incompatible, by an unbounded factor. It also explains *why*: the isotropic Hessian error must be absorbed on the pure-gauge directions where the Maxwell stiffness is identically zero. This is a rediscovery, in Bakry–Émery dress, of the large-field problem of constructive field theory.

---

## 12. Obstruction II: the certified clustering rate is Θ(g(a)) in lattice units, so the certified gap diverges as a → 0

`status: solid` · `kind: obstruction`

### Statement

Suppose, counterfactually, that every hypothesis of the master conditional theorem could be met uniformly along a scaling trajectory $a\downarrow0$ with $\beta=\beta(a)$. In the metric normalization used throughout ($\langle X,Y\rangle_{\mathfrak g}=-\Re\operatorname{Tr}(d\rho X\,d\rho Y)$, which is $a$-independent), $\kappa_G=N/2$ and $m_H^2=N/6$ are $a$-independent, while $\alpha_W=\beta/n=2/g^2$. Therefore the certified exponent obeys
$$\eta_\star(a)\ \le\ \operatorname{arcosh}\Big(1+\frac{m_H^2}{2B_S}\Big)=\operatorname{arcosh}\Big(1+\frac{N g^2}{216}\Big)\ \sim\ \frac{\sqrt N}{6\sqrt6}\,g(a)\ \xrightarrow[a\to0]{}0,$$
but only as $\Theta(g)=\Theta\big((\log(1/a\Lambda))^{-1/2}\big)$. Since the theorem's conclusion is $\mathrm{gap}(H_a)\ge\eta_\star(a)/a$, and one-loop asymptotic freedom gives $g^2(a)=\big(\beta_0\log(1/a^2\Lambda^2)\big)^{-1}$ with $\beta_0=\frac{11N}{48\pi^2}$,
$$\mathrm{gap}(H_a)\ \ge\ \frac{\eta_\star(a)}{a}\ \asymp\ \frac{1}{a\sqrt{\log(1/a\Lambda)}}\ \xrightarrow[a\to0]{}\ +\infty .$$
If the continuum theory has a finite mass gap $m_\ast$, then the dimensionless lattice gap must satisfy $\hat m(a)=m_\ast a\to0$ **linearly** in $a$, whereas the pipeline certifies $\hat m(a)\gtrsim1/\sqrt{\log(1/a)}$. These are incompatible by an unbounded factor $\asymp1/(a\sqrt{\log(1/a)})$.

**Consequence.** No completion of this chain can be uniform in $a$: at least one of (H2) with an $a$-uniform $m_H^2$, (H5) typicality, or the unconditioning step must fail along the scaling trajectory — and the failure is by an unbounded factor, not a constant. No sharpening of Combes–Thomas can help: the Davies/sharp exponent has the same $\Theta(g)$ scaling, and the level-set refinement $C_\partial\le C_0$ buys at most a factor $\sqrt2$.

### Derivation

**Step 1 (the exponent's $\beta$-scaling is $\beta^{-1/2}$, not $\beta^{-1}$ or $\beta^0$).**
$B_S=18\alpha_W$ at the vacuum, $m_H^2=N/6$, $\alpha_W=\beta/N=2/g^2$. With $x:=m_H^2/(2B_S)=\frac{N/6}{36\alpha_W}=\frac{Ng^2}{432}$,
$$\eta_{\mathrm{Davies}}=\operatorname{arcosh}(1+2x)\Big|_{2x=Ng^2/216}=2\operatorname{arsinh}\sqrt{x}\ \sim\ 2\sqrt{x}=\frac{g\sqrt N}{6\sqrt6},$$
verified numerically: SU(3) at $g=1$ gives $0.117783$ against the asymptotic $0.117851$; SU(3) at $g^2=0.06$ gives $0.028867$ against $0.028868$. The Neumann-series rate $\eta_{\mathrm{CT}}=\log(1+2x)\sim Ng^2/216=\Theta(g^2)$ is worse still. Since $g^2=2N/\beta$, both are $\Theta(\beta^{-1/2})$ and $\Theta(\beta^{-1})$ respectively. (The corpus's own `04_helffer_sjostrand_and_greens_decay.md` §4 reaches the same $\beta^{-1/2}$ conclusion by the Fourier route, $\nu\sim\sqrt3\sqrt{c_H}/(2\sqrt\beta\sqrt d)$, and then explicitly defers the $a$-dependence to "a separate continuum-limit argument" that is nowhere carried out.)

**Step 2 ($m_H^2$ is $a$-independent).** $\kappa_G$ is a property of $(G,g_G)$ alone; the metric used on each link factor is a fixed bi-invariant metric on $G$ and does not carry the lattice spacing. Hence $m_H^2=\kappa_G/3=N/6$ for all $a$. (Files that write $c_0\,a^2g^2$ for this constant are using a different, incompatible normalization; mixing them is the double-counting error flagged in the constants item.)

**Step 3 (substitute the trajectory).** $g^2(a)=1/(\beta_0\log(1/a^2\Lambda^2))$, so $g(a)\asymp(\log(1/a\Lambda))^{-1/2}$ and
$$\frac{\eta_\star(a)}{a}\asymp\frac{g(a)}{a}\asymp\frac{1}{a\sqrt{\log(1/a\Lambda)}}\to\infty .$$

**Step 4 (the reductio).** A nontrivial continuum limit with a finite gap $m_\ast$ requires the *lattice-unit* correlation length $\xi(a)=1/\hat m(a)$ to diverge like $1/(m_\ast a)$; the pipeline certifies $\xi(a)\le1/\eta_\star(a)\asymp\sqrt{\log(1/a)}$, which diverges only logarithmically. A certified upper bound on the correlation length that grows like $\sqrt{\log(1/a)}$ is incompatible with the required linear-in-$1/a$ growth. $\square$

**Where the loss actually occurs.** The certified rate is set by the ratio (curvature floor)/(interaction strength) $=m_H^2/B_S$. The numerator is a fixed geometric constant of the group manifold — a *cutoff-scale* mass. The denominator grows like $\beta$. The mechanism produces a gap of order the cutoff, which is exactly the wrong scale: this is the folklore statement that "curvature/convexity methods give you a gap at the cutoff scale", here made quantitative with the exponent $\beta^{-1/2}$.

**Remark on what is and is not proved.** The reductio assumes that the continuum limit exists and has a finite gap — i.e. it assumes what the programme sets out to prove — so it is a consistency argument rather than an unconditional theorem about Yang–Mills. What it *does* prove unconditionally is a statement about the proof strategy: the chain cannot be completed $a$-uniformly. It also makes `Foundations_Theorem_E.md` (existence/uniqueness/closability of the continuum measure) vacuous rather than conditional, since that file assumes an $a$-uniform log-Sobolev constant $\rho_0$, which is exactly the hypothesis this argument rules out.

### Constants and numbers

m_H² = N/6 (a-independent); α_W = β/n = 2/g²; B_S = 18α_W = 36/g².
η_Davies = arcosh(1 + N g²/216) ≈ (√N/(6√6))·g. SU(3): 0.11785 g; SU(2): 0.09621 g.
η_CT = log(1 + N g²/216) ≈ N g²/216 = Θ(g²).
Verified: SU(3) β=6 (g=1): η_D = 0.117783 vs asymptote 0.117851. SU(3) β=100 (g²=0.06): 0.028867 vs 0.028868. SU(2) β=10 (g²=0.4): 0.060849 vs 0.060858.
β₀ = 11N/(48π²) (one loop, pure gauge). g²(a) = 1/(β₀ log(1/a²Λ²)).
gap(H_a) ≥ η_⋆/a ≍ 1/(a √log(1/aΛ)) → ∞.
Required for a finite continuum gap: m̂(a) = m_⋆ a → 0 linearly. Discrepancy factor: ≍ 1/(a √log(1/a)).
Illustrative absolute numbers (SU(3), a ≈ 0.093 fm, β = 6): certified gap ≥ 250 MeV (Davies) or 14.7 MeV (CT); the ratio to the true glueball mass 1.7 GeV is 0.15 and 0.009, and this ratio would *increase past 1 and diverge* as a → 0.

**Caveat.** Assumes one-loop asymptotic freedom (β(a) ≍ log(1/a)) and the existence of a finite continuum gap — so it is a consistency argument about the strategy, not an unconditional theorem about Yang–Mills. It is also sensitive to the metric normalization: the corpus uses three incompatible ones (κ_G = N/2 intrinsically; c₀ = 1/6 in the flat exponential chart; c₀a²g² elsewhere), and a referee would demand one fixed convention.

**Why it matters.** Together with Obstruction I this is the mathematically strongest content on this topic. It converts an informal worry into an explicit quantitative reductio with the exponent β^{−1/2} and an explicit constant √N/(6√6), and it shows that the failure is not a matter of sharpening constants: the Davies exponent, the level-set refinement and even the exactly sharp rate arcosh(1 + m²/2α) all scale as Θ(g), so no refinement of the decay estimate can rescue the continuum limit.

---

## How these fit together

The nine items form one linear chain plus two transverse obstructions, and the way they interlock is the real content.

**The forward chain.** Constants ledger → vacuum Hessian identity (∇²S(U⁰) = α_W d₁*d₁, the only place the cochain complex enters) → matrix hinge on a good set (Ric_μ ⪰ m_H² + (α_W/2)d₁*d₁, conditional on a third-derivative estimate) → Helffer–Sjöstrand covariance identity with Bochner dominance (L^(1) ⪰ Ric_μ, hence a spectral floor) → Combes–Thomas or Davies kernel decay (needs only a₀ > 0, finite range, bounded row sums) → conditional exponential clustering → localization algebra removes the conditioning → Core-9 passes everything to the thermodynamic limit → Appendix K's reflection positivity plus Appendix L's spectral-support lemma converts Euclidean-time decay into gap(H) ≥ η_⋆/a. The master conditional theorem is that chain with the hypotheses named.

**The break and the repair, and how they change the reading of everything else.** The corpus routes decay through the *deterministic* operator M^hinge: it uses the matrix Brascamp–Lieb bound to justify a double-sum over link supports weighted by the blocks of (M^hinge)⁻¹. That step admits a two-link counterexample (take M = m²I; the blocks are diagonal, so the asserted bound gives zero covariance between observables on distinct links, which is false). Repairing it — apply Combes–Thomas directly to the Witten Laplacian L^(1) on 1-forms, whose fiber L²(μ^K;g) is infinite-dimensional but which the Appendix G proof handles without change — restores every constant, because B₀(L^(1)) = B_S = 18α_W at the vacuum, matching Appendix G's own bound for M_Λ. But the repair also reveals that the Maxwell part of the hinge is never used: a₀(m_H² + α d₁*d₁) = m_H² exactly, since d₁*d₁ has a large kernel, and the Maxwell term only *raises* B₀. So the corpus's advertised novelty — "never scalarize; keep d₁*d₁ intact all the way to the covariance bound" — is, for this estimate, a liability rather than an asset. The scalar Haar/Ricci floor m_H² = κ_G/3 does all the work.

**Why that observation feeds directly into both obstructions.** Because only the scalar floor matters, the entire certified rate is the ratio (curvature floor)/(interaction strength) = m_H²/B_S = Θ(g²), giving η = Θ(g) (Davies) or Θ(g²) (Neumann series). Obstruction II is then two lines of arithmetic: m_H² is a fixed geometric constant of the group manifold, so η/a ≍ g(a)/a → ∞ under asymptotic freedom. Obstruction I comes from the *same* structural fact seen from the other side: the isotropic Hessian error −Cβr·Id must be absorbed on the pure-gauge directions im(d₀), where d₁*d₁ ≡ 0 (this is d₁d₀ = 0, the same cochain identity that makes the vacuum Hessian a Maxwell operator), so only the β-independent reservoir κ_G is available and the good-set radius is forced to O(1/β) — while typical plaquette logs fluctuate at β^{-1/2}. So the very identity that makes the programme work at the vacuum (d₁d₀ = 0) is what kills it on the good set and in the continuum limit.

**What survives independently.** Three blocks are self-contained and correct regardless of the programme: (a) the vacuum Hessian identity, which is a clean statement about any compact group and any faithful representation; (b) the Combes–Thomas/Davies inverse-decay machinery, valid over an arbitrary Hilbert fiber, together with the sharp comparison — the certified Davies rate loses exactly a factor √C₀ = √18 = 4.24 against the true rate arcosh(1 + m²/2α), verified numerically to four digits; (c) the OS block — reflection positivity for Wilson and the spectral-support argument giving gap(H) ≥ η/a with ker H = CΩ. These three would transfer verbatim to any lattice model with a positive Bakry–Émery floor on a typical set — which is exactly the class of models the obstructions say lattice Yang–Mills is not in.

**Relation to neighbouring corpus areas.** The typicality file (Appendix J, WILSON/archive) proves the exponential bound only for an *averaged* badness set and then silently substitutes it for the sup-type set the hinge needs; that substitution is the seam where Obstruction I enters. Foundations_Theorem_E (existence/uniqueness/closability of the continuum measure) assumes an a-uniform log-Sobolev constant, which is the same hypothesis Obstruction II rules out — so Theorem E is downstream of a false hypothesis, i.e. vacuous rather than conditional. The horizontal-sector material (Extract_09, and the Fourier scalarization lemma) is correct at the vacuum only, and the corpus itself lists "extend horizontality beyond the vacuum" as open; the repaired chain does not need it.

## Further material found but not fully extracted

Not extracted in full, but real and locatable:

1. **The horizontal-sector Fourier scalarization** (`HELFFER_SJOSTRAND/02_.../04_helffer_sjostrand_and_greens_decay.md`, Lemma 3.1). On ker d₀* the symbol of d₁*d₁ collapses to the scalar lattice Laplacian λ(k) = 4Σ sin²(k_μ/2), because the constraint q̄·X̂ = 0 annihilates the rank-one longitudinal piece. A contour shift then gives ‖G_{(x,μ),(y,ν)}‖ ≤ (2/m²)e^{−ν|x−y|₁} with ν = 2 arsinh(m/√(8td)) — a correct, complete proof, better than the Neumann-series rate, and worth writing up on its own. I verified the symbol algebra; the caveat is that it applies to horizontal inputs, which is established only at the vacuum.

2. **Appendix J typicality mechanism** (`WILSON/archive/Appendix_J__Typicality_Mechanism_for_K(1).md`) and `RICCATI/.../PROOF_13_High_Probability_Convexity(1).md`. The latter contains a genuinely correct chessboard-estimate derivation of a *volume-uniform* single-plaquette tail bound μ_β(d_G(U_p,1) ≥ δ) ≤ C₀β^{α/2}e^{−βc_Φ(δ)} with α = dim(G)|E|/|P| = 2dim(G)/3 in 4D — energy cost, chessboard reduction to (Z^bad/Z)^{1/|P|}, small-ball lower bound on Z, the 1/|P| root that cancels the volume. That lemma is solid and reusable. CAND-005 supplies the arithmetic showing the union bound over 6(R/a)⁴ plaquettes cannot be beaten by the logarithmic growth of β(a), because c_Φ(δ) ≤ 2 always while 4/c = 48π²/(11N²) ≈ 4.8 for N = 3.

3. **Appendix K in full** (`REFLECTION_POSITIVITY/02_RP_FUNDAMENTALS/`) — the complete Osterwalder–Seiler proof including the sum-of-squares/character expansion of w_β (Prop K.3.5), the plaquette partition P = P₊ ⊔ P₀ ⊔ P₋, and the straddling-plaquette factorization U_p = (V_p⁻)⁻¹V_p⁺. Sections K.1–K.4 are careful and would need only light editing to be publishable as an exposition.

4. **Appendix E, Bakry–Émery calculus** (`HELFFER_SJOSTRAND/04_.../Appendix_E__Bakry_Emery_Calculus(1).md`, 26 KB) — the Γ₂ machinery and the vector-field integration-by-parts identity that Appendix F imports as External Input F.7. Since the lattice case has a global right-invariant orthonormal frame, F.7 is almost certainly provable directly there; the file may already contain enough for it.

5. **The reflecting-diffusion input (External Input F.20)** is the one analytic hypothesis in the chain that nobody in the corpus attempts. The good set K_{Λ,β} is an intersection of sublevel sets with corners; existence of the Neumann generator and the associated Poisson solvability on such a domain is a real, self-contained PDE question.

6. **`SIMULATIONS/sanity_check_maxwell_decay.py` and `sanity_checks.py`** — runnable, correct code for the 2D massive Maxwell resolvent decay, the transverse/longitudinal projector inversion, and a local Gram-matrix check (eigenvalues {3,3,3,3,3,9}, determinant 2187). `05_simulation_appendix_maxwell_and_a100_su2.md` claims an L = 16 4-torus FFT check with maximum bound ratio 0.1412, but that maximum is attained at distance 0, so it tests the prefactor, not the exponent; and its reported C₀ = 43.91 for d₁*d₁ is wrong (the correct value is exactly 18 — I verified this by direct construction).

7. **Core_4 (`MAXWELL/Hodge_Structure/`) and Appendix B (`TENSOR_NETWORK/06_LATTICE_QCD_SECTORS/`)** contain the complete discrete Hodge/cochain algebra: d₁d₀ = 0, the orthogonal splitting C¹ = im(d₀) ⊕ ker(d₀*), M₁-invariance of horizontals, and the block-entry formula (M₁)_{bb'} = (Σ_p σ_{p,b}σ_{p,b'})·Id. All correct, all elementary, and the source of every combinatorial constant.

8. **Harmonic zero modes.** On the 4-torus, ker d₁ ⊇ im d₀ ⊕ H¹ with dim H¹ = 4 per g-component. The mass term m_H² resolves them, but nobody in the corpus isolates the exact kernel structure; `Extract_09` §8 lists it as open. It matters for any attempt to work on the horizontal sector, and it is a finite, tractable computation.
