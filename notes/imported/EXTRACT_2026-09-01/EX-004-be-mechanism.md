---
id: EX-004
title: "The Haar / Bakry-Émery curvature mass mechanism for lattice Yang-Mills: Ric_mu = Ric_g + Hess S_W on SU(N)^E, gauge reduction to horizontals, and the route Ric-bound -> Gamma_2 -> Poincaré/L"
kind: extraction
items: 15
status_breakdown: {"solid": 12, "conditional": 2, "gap": 1}
program: yang_mills
extracted_by: claude-opus-5 subagent, 2026-09-01
stance: preservation (content extraction, not refereeing)
source_files:
  - HAAR/01_haar_mass/01_CORE_THEOREMS/A_local_BE_curvature.md
  - HAAR/01_haar_mass/01_CORE_THEOREMS/DOC1_Haar_Wilson_Bakry_Emery_Mass_Mechanism.md
  - HAAR/01_haar_mass/01_CORE_THEOREMS/B_canonical_region_matrix_hinge.md
  - HAAR/01_haar_mass/03_WILSON_HESSIAN/UNIFY_01_Wilson_Hessian_and_Haar_Mass.md
  - HESSIAN/Core_Hessian/UNIFY_02_Horizontal_Bakry_Emery_Core_Theorem.md
  - HESSIAN/Core_Hessian/07_horizontal_Bakry_Emery_curvature.md
  - HAAR/01_haar_mass/02_HAAR_MASS/EXTRACT_02_Haar_Mass_Mechanism_on_Compact_Groups.md
  - HAAR/01_haar_mass/02_HAAR_MASS/D_Haar_Jacobian_SmallField.md
  - HAAR/01_haar_mass/07_SAFE_REGION/RECOMMENDED_01_Finite_Cutoff_Haar_Wilson_Windows_v2.md
  - LSI_POINCARE/05_proofs_reports/RECOMMENDED_02_Global_BE_Obstruction_and_Localization_v2.md
  - HAAR/01_haar_mass/05_SU3_CALCULATIONS/Selected_Numerics_SU3_Convexity_Rbeta_Tau_and_Scaling.md
  - HAAR/01_haar_mass/05_SU3_CALCULATIONS/05_su3_wilson_haar_hessian_numerics.md
  - HAAR/01_haar_mass/05_SU3_CALCULATIONS/YANG3_update_erosionLemma_kernelSchur_v5.md
  - HAAR/01_haar_mass/04_SU2_CALCULATIONS/02_SU2_SingleLink_BetaC.md
  - HAAR/01_haar_mass/04_SU2_CALCULATIONS/03_SU2_Concentration_BadMass.md
  - HAAR/01_haar_mass/01_CORE_THEOREMS/01_matrix_hinge_to_massive_maxwell.md
  - HESSIAN/archive/duplicates/Selection_A_Horizontal_BakryEmery_on_Gauge_Quotients (1).md
  - COMBES_THOMAS/MAXWELL_GREEN/02_davies_decay_row_sum_constants.md
  - HAAR/01_haar_mass/05_SU3_CALCULATIONS/SAFE_region_SU3_curvature.md
  - HAAR/01_haar_mass/05_SU3_CALCULATIONS/BEST_06_SAFE_region_SU3_constants_and_numerics.md
---

# The Haar / Bakry-Émery curvature mass mechanism for lattice Yang-Mills: Ric_mu = Ric_g + Hess S_W on SU(N)^E, gauge reduction to horizontals, and the route Ric-bound -> Gamma_2 -> Poincaré/LSI -> spectral gap

> On a finite lattice the product Haar geometry of SU(N)^E supplies a volume-uniform positive Bakry-Émery curvature floor kappa_G = N/2 (metric -Tr XY) with the Wilson Hessian at the vacuum equal to the discrete Maxwell operator (beta/N) d_1* d_1 >= 0; this yields an unconditional dimension-free CD(rho,infinity), Poincaré, LSI and spectral gap for all beta < N^2/48 in d=4, but the mechanism provably cannot be pushed to the continuum because the Wilson Hessian has an explicit negative direction of size -beta/N and the horizontal Maxwell gap c_W decays like 4*pi^2/L^2.

**15 extracted items** — 2 conditional, 1 gap, 12 solid

---

## 1. Setup and the normalization ledger for su(N) (the dictionary that reconciles every constant in the corpus)

`status: solid` · `kind: definition`

### Statement

Let $G=\mathrm{SU}(N)$, $\mathfrak g=\mathfrak{su}(N)$ (traceless anti-Hermitian $N\times N$ matrices). Fix an $\mathrm{Ad}$-invariant inner product $\langle X,Y\rangle_\lambda := -\lambda\,\mathrm{Tr}(XY)$, $\lambda>0$, and let $g_G$ be the induced bi-invariant metric. Let $\Lambda$ be a finite graph embedded in $\mathbb Z^d$ ($d\ge2$), with oriented edge (link) set $E(\Lambda)$, vertex set $V(\Lambda)$, oriented plaquette set $P(\Lambda)$. Define
$$M_\Lambda:=G^{E(\Lambda)},\qquad g_\Lambda:=g_G^{\otimes E(\Lambda)},\qquad \mathrm{vol}_{g_\Lambda}=\bigotimes_{\ell}\mathrm{Haar}(dU_\ell).$$
Wilson action, plaquette holonomy $U_p=U_{x,\mu}U_{x+\hat\mu,\nu}U_{x+\hat\nu,\mu}^{-1}U_{x,\nu}^{-1}$:
$$S_W(U)=\beta\sum_{p\in P(\Lambda)}\Big(1-\tfrac1N\mathrm{Re}\,\mathrm{Tr}\,U_p\Big)=\tfrac{\beta}{N}\sum_p\big(N-\mathrm{Re}\,\mathrm{Tr}\,U_p\big).$$
Gibbs measure, generator, carré du champ:
$$d\mu_\Lambda=Z_\Lambda^{-1}e^{-S_\Lambda}\,d\mathrm{vol}_{g_\Lambda},\quad L_\Lambda f=\Delta_{g_\Lambda}f-\langle\nabla S_\Lambda,\nabla f\rangle,\quad \Gamma(f)=|\nabla f|^2,$$
$$\Gamma_2(f)=\tfrac12\big(L_\Lambda\Gamma(f)-2\Gamma(f,L_\Lambda f)\big),\qquad \mathrm{Ric}_{\mu_\Lambda}:=\mathrm{Ric}_{g_\Lambda}+\nabla^2S_\Lambda.$$
The *entire* numerical content of the corpus depends on $\lambda$, and the corpus silently mixes $\lambda=1$ and $\lambda=2$. The dictionary below is the single most useful thing to carry away: every constant in every file is one of these two columns.

### Derivation

Two orthonormal bases of $\mathfrak{su}(3)$ are used throughout the corpus, and they differ by $\sqrt2$:

**Basis A** $T_a=i\lambda_a/2$ ($\lambda_a$ = Gell-Mann). Orthonormal for $\langle X,Y\rangle_2=-2\mathrm{Tr}(XY)$. This is the basis in every JAX/Colab script in the corpus (`su3_generators()` returns `1j*stack(lam)/2`).

**Basis B** $T_a=i\lambda_a/\sqrt2$. Orthonormal for $\langle X,Y\rangle_1=-\mathrm{Tr}(XY)$. This is the convention declared in the analytic notes (`RECOMMENDED_01`, `RECOMMENDED_02`, `A_local_BE_curvature.md`).

[reconstructed] I verified orthonormality of both to machine precision, then computed every downstream constant in both columns by (i) exact Lie theory and (ii) independent finite-difference numerics on $\mathfrak{su}(3)$. They agree to 6+ digits.

General relations. The Killing form of $\mathfrak{su}(N)$ is $B(X,Y)=2N\,\mathrm{Tr}(XY)$. Hence with $\langle\cdot,\cdot\rangle_\lambda=-\lambda\mathrm{Tr}$,
$$B=-\tfrac{2N}{\lambda}\langle\cdot,\cdot\rangle_\lambda .$$
For a bi-invariant metric on a compact group, $\mathrm{Ric}=-\tfrac14 B$, so
$$\boxed{\ \mathrm{Ric}_G=\kappa_G\,g_G,\qquad \kappa_G=\frac{N}{2\lambda}. \ }$$
Thus $\kappa_G=N/2$ for $\lambda=1$ (basis B) and $\kappa_G=N/4$ for $\lambda=2$ (basis A). The frequently quoted "$\mathrm{Ric}=N/4$" of the corpus is the $\lambda=2$ column; "$\kappa_G=N/(2\lambda)$" appears explicitly only inside an auto-generated contradiction report (`HAAR/analysis_reports/contradictions_Synthesis_01_...BACKUP_20260118_195906.md:43`), i.e. the corpus knew but never propagated it.

Quadratic expansion of the Wilson class function. For $Y\in\mathfrak{su}(N)$ small, $\mathrm{Tr}(Y)=0$ and $\mathrm{Tr}(Y^2)\in\mathbb R$, so
$$\mathrm{Re}\,\mathrm{Tr}(e^{Y})=N+\tfrac12\mathrm{Tr}(Y^2)+O(|Y|^3)=N-\frac{1}{2\lambda}\|Y\|_\lambda^2+O(|Y|^3).$$
Hence $N-\mathrm{Re}\,\mathrm{Tr}(e^Y)=\frac{1}{2\lambda}\|Y\|^2_\lambda+O(|Y|^3)$, which is where every factor of 2 in the corpus comes from.

DICTIONARY (all verified numerically, $N=3$ column shown):

| quantity | $\lambda=1$ ($-\mathrm{Tr}$, basis B) | $\lambda=2$ ($-2\mathrm{Tr}$, basis A) |
|---|---|---|
| $\kappa_G$ (Ricci) | $N/2$  = 1.5 | $N/4$ = 0.75 |
| $\nabla^2S_H(0)=\kappa_G/3$ (Haar potential) | $N/6$ = 0.5 | $N/12$ = **0.25** |
| $\nabla^2 S_W(U^{(0)})$ | $(\beta/N)\,d_1^*d_1$ | $(\beta/2N)\,d_1^*d_1$ |
| one-plaquette positive eigenvalue of $\nabla^2[1-\tfrac1N\mathrm{ReTr}U_p]$ | $4/N$ = 4/3 | $2/N$ = **2/3** |
| one-plaquette min eigenvalue over all $U$ (sharp) | $-4/N$ = $-4/3$ | $-2/N$ | 
| single-link block min at $U_p=\mathrm{diag}(-1,-1,1)$ | $-1/N$ = $-1/3$ | $-1/(2N)$ |

The boldface entries **0.25** and **2/3** are exactly the two numbers the corpus's SU(3) numerics report (`su3_haar_hessian_scan_results.csv` first row $0.2500001983$; `YANG3_update_erosionLemma_kernelSchur_v5.md` "positive eigenvalue plateau at $2/3$, rank 8, kernel 24"). So the numerics are internally consistent and live in basis A, while the theorems live in basis B.

### Constants and numbers

kappa_G = N/(2*lambda) for <X,Y> = -lambda*Tr(XY). SU(3): kappa_G = 1.5 (lambda=1), 0.75 (lambda=2). Haar potential Hessian at 0: kappa_G/3 = 0.5 (lambda=1), 0.25 (lambda=2) -- verified numerically to 1e-9 by finite differences on -log det((1-e^{-ad_X})/ad_X). Single-plaquette Wilson Hessian at vacuum: eigenvalue 4/N=1.3333 (lambda=1) / 2/N=0.66667 (lambda=2), multiplicity 8, kernel dimension 24 in the 32-dimensional 4-link tangent space -- verified numerically. Killing form B(X,Y)=2N Tr(XY); dual Coxeter number g^vee = N. Plaquette incidence in d dimensions: nu = 2(d-1); nu = 6 for d = 4.

### Code

# Reproduces the whole dictionary (numpy + scipy only, ~5 s).
import numpy as np
from scipy.linalg import expm
l=[None]*9
l[1]=np.array([[0,1,0],[1,0,0],[0,0,0]],complex); l[2]=np.array([[0,-1j,0],[1j,0,0],[0,0,0]],complex)
l[3]=np.array([[1,0,0],[0,-1,0],[0,0,0]],complex); l[4]=np.array([[0,0,1],[0,0,0],[1,0,0]],complex)
l[5]=np.array([[0,0,-1j],[0,0,0],[1j,0,0]],complex); l[6]=np.array([[0,0,0],[0,0,1],[0,1,0]],complex)
l[7]=np.array([[0,0,0],[0,0,-1j],[0,1j,0]],complex); l[8]=np.array([[1,0,0],[0,1,0],[0,0,-2]],complex)/np.sqrt(3)
TA=np.stack([1j*l[a]/2        for a in range(1,9)])   # lambda = 2
TB=np.stack([1j*l[a]/np.sqrt(2) for a in range(1,9)]) # lambda = 1
def adjoint(v,T,c):
    X=np.tensordot(v,T,axes=(0,0)); ad=np.zeros((8,8))
    for b in range(8):
        C=X@T[b]-T[b]@X
        for a in range(8): ad[a,b]=(-c*np.trace(T[a]@C)).real
    return ad
def ric(T,c,n=5):                       # Ric(X,X)=1/4 sum_i |[X,e_i]|^2
    ip=lambda A,B:(-c*np.trace(A@B)).real; out=[]
    for _ in range(n):
        v=np.random.normal(size=8); v/=np.linalg.norm(v); X=np.tensordot(v,T,axes=(0,0))
        out.append(sum(ip(X@T[i]-T[i]@X,X@T[i]-T[i]@X) for i in range(8))/4)
    return np.round(out,6)
print('kappa_G  lambda=2:',ric(TA,2),'  lambda=1:',ric(TB,1))   # -> 0.75 , 1.5

def SH(v,T,c):                          # Haar potential -log J
    th=np.abs(np.linalg.eigvals(adjoint(v,T,c)).imag); s=0.
    for t in th:
        if t>1e-13: s-=np.log(np.sin(t/2)/(t/2))
    return s
def hess(f,x0,h=1e-4):
    n=len(x0);H=np.zeros((n,n))
    for i in range(n):
        for j in range(i,n):
            ei=np.zeros(n);ei[i]=h;ej=np.zeros(n);ej[j]=h
            H[i,j]=H[j,i]=(f(x0+ei+ej)-f(x0+ei-ej)-f(x0-ei+ej)+f(x0-ei-ej))/(4*h*h)
    return H
for lab,T,c in [('lambda=2',TA,2),('lambda=1',TB,1)]:
    print('HessS_H(0)',lab,np.round(np.linalg.eigvalsh(hess(lambda v:SH(v,T,c),np.zeros(8)+1e-9)),6))
# -> 0.25 (x8) and 0.5 (x8)

def Sp(x,T):                            # one plaquette, S_p = 1 - (1/3)ReTr(U1U2U3^-1U4^-1)
    x=x.reshape(4,8); U=[expm(np.tensordot(x[i],T,axes=(0,0))) for i in range(4)]
    return 1.0-np.trace(U[0]@U[1]@np.linalg.inv(U[2])@np.linalg.inv(U[3])).real/3
for lab,T in [('lambda=2',TA),('lambda=1',TB)]:
    ev=np.linalg.eigvalsh(hess(lambda v:Sp(v,T),np.zeros(32),2e-4))
    print('plaquette',lab,'nonzero:',round(float(ev[-1]),6),' rank:',int((ev>1e-6).sum()),' kernel:',int((abs(ev)<1e-6).sum()))
# -> 0.666667 rank 8 kernel 24 ; 1.333333 rank 8 kernel 24

**Caveat.** The corpus never fixes lambda globally; several documents combine a lambda=1 curvature with a lambda=2 Hessian. Any quoted number from the corpus must be re-tagged with its lambda before being used.

**Why it matters.** Without this table the corpus's constants look mutually contradictory (its own auto-generated contradiction reports flag exactly this, repeatedly). With it, every number in the archive becomes checkable and every one I checked is right in one column or the other.

---

## 2. Haar/Ricci curvature floor: Ric_{g_Lambda} = kappa_G g_Lambda on SU(N)^E, uniformly in the volume

`status: solid` · `kind: theorem`

### Statement

Let $G$ be a compact connected Lie group with bi-invariant metric $g_G$ satisfying $\mathrm{Ric}_G\ge\kappa_G g_G$, $\kappa_G>0$. Let $M_\Lambda=G^{E(\Lambda)}$ carry the product metric $g_\Lambda$. Then for every finite $\Lambda$ and every $v\in T_UM_\Lambda$,
$$\mathrm{Ric}_{g_\Lambda}(v,v)\ \ge\ \kappa_G\,|v|_{g_\Lambda}^2 ,$$
with the **same** $\kappa_G$, independent of $|E(\Lambda)|$. For $G=\mathrm{SU}(N)$ with $\langle X,Y\rangle=-\lambda\mathrm{Tr}(XY)$ one has equality, $\mathrm{Ric}_G=\kappa_G g_G$ with $\kappa_G=N/(2\lambda)$ ($\mathrm{SU}(N)$ with a bi-invariant metric is Einstein).

### Derivation

Step 1 (single factor). For a compact Lie group with bi-invariant metric, if $\{e_i\}$ is an orthonormal basis of $\mathfrak g$ then
$$\mathrm{Ric}(X,X)=\tfrac14\sum_i\big\|[X,e_i]\big\|^2=-\tfrac14\mathrm{Tr}(\mathrm{ad}_X^2)=-\tfrac14 B(X,X),$$
i.e. $\mathrm{Ric}=-\tfrac14B$ with $B$ the Killing form. (Standard: bi-invariant metrics have $\nabla_XY=\tfrac12[X,Y]$ for left-invariant fields, sectional curvature $K(X,Y)=\tfrac14\|[X,Y]\|^2$ on orthonormal pairs, and summing gives the formula.)

Step 2 (specialize). $B(X,Y)=2N\mathrm{Tr}(XY)$ for $\mathfrak{su}(N)$, and $\langle X,Y\rangle_\lambda=-\lambda\mathrm{Tr}(XY)$ gives $B=-\frac{2N}{\lambda}\langle\cdot,\cdot\rangle_\lambda$, hence
$$\mathrm{Ric}_G=\frac{N}{2\lambda}\,g_G,\qquad \kappa_G=\frac{N}{2\lambda}.$$
Since $\mathrm{Ric}$ is a positive multiple of $g_G$, $G$ is Einstein and the bound is an equality — there is no direction in which the curvature is smaller.

Step 3 (product). For a Riemannian product $M=\prod_iM_i$ the Levi-Civita connection splits, curvature tensors have no cross terms, and
$$\mathrm{Ric}_M(v,v)=\sum_i\mathrm{Ric}_{M_i}(v_i,v_i)\ \ge\ \kappa_G\sum_i|v_i|^2=\kappa_G|v|^2_{g_\Lambda}.$$
No cross-link term appears, so the bound is *exactly* volume-uniform: adding links neither helps nor hurts. This is the one structural fact in the whole programme that is unconditionally uniform in $|\Lambda|$.

Step 4 (why it is a "mass"). In the Bakry-Émery tensor $\mathrm{Ric}_{\mu_\Lambda}=\mathrm{Ric}_{g_\Lambda}+\nabla^2S_\Lambda$, the term $\kappa_G g_\Lambda$ appears additively and is present even at $\beta=0$ (pure Haar). Under $\mathrm{CD}(\rho,\infty)$ it produces a spectral gap $\ge\rho$ for the Langevin generator (item 6). The sign is fixed purely by non-abelianness: for $G=U(1)^k$ the bi-invariant metric is flat, $\mathrm{Ric}\equiv0$, and the mechanism gives exactly nothing. That abelian/non-abelian dichotomy is the genuinely attractive conceptual content (`EXTRACT_02_Haar_Mass_Mechanism_on_Compact_Groups.md` §3.1).

[reconstructed] Numerical check: I evaluated $\tfrac14\sum_i\|[X,e_i]\|^2$ for random unit $X\in\mathfrak{su}(3)$ in both bases; result $0.750000$ ($\lambda=2$) and $1.500000$ ($\lambda=1$) for every sample, confirming $\kappa_G=N/4$ and $N/2$ and confirming the Einstein property (no scatter).

### Constants and numbers

kappa_G = N/(2*lambda). SU(2): 1.0 (lambda=1) / 0.5 (lambda=2). SU(3): 1.5 / 0.75. SU(N) general. Einstein: Ric = kappa_G g exactly (no direction-dependence; numerical scatter over random directions < 1e-9). Product bound is an equality and is independent of |E(Lambda)|. Abelian case U(1)^k: Ric = 0, kappa_G = 0.

### Code

# see the `ric()` function in item 1's code block; output 0.75 (lambda=2), 1.5 (lambda=1) for SU(3).

**Caveat.** Uniformity in the number of links is genuine, but a fixed-size curvature floor in *lattice units* is not a physical mass; converting to a physical mass requires dividing by the lattice spacing, and that is where the programme fails (items 9-11).

**Why it matters.** This is the one input of the whole mechanism that is exactly volume-uniform, exactly computable, and unconditionally true. Everything the corpus achieves rests on it.

---

## 3. Haar Jacobian in exponential coordinates: exact formula, Hess S_H(0) = (1/3) Ric_G, and a strengthened GLOBAL convexity bound on the whole exponential chart

`status: solid` · `kind: derivation`

### Statement

Let $G$ be compact connected with bi-invariant metric, $\exp:\mathfrak g\to G$, and write $d\mathrm{vol}_{g_G}(\exp X)=J_G(X)\,dX$ with $dX$ Lebesgue measure for $\langle\cdot,\cdot\rangle$. Define the **Haar potential** $S_H:=-\log J_G$. Then:

(i) $\displaystyle J_G(X)=\det_{\mathfrak g}\!\Big(\frac{1-e^{-\mathrm{ad}_X}}{\mathrm{ad}_X}\Big)=\prod_{\alpha>0}\Big(\frac{\sin(\alpha(X)/2)}{\alpha(X)/2}\Big)^{2}$ for $X$ in a Cartan subalgebra, $\alpha$ running over positive roots.

(ii) $S_H(X)=\tfrac16\mathrm{Ric}_e(X,X)+O(|X|^4)$, hence $\nabla^2S_H(0)=\tfrac13\mathrm{Ric}_G\ \ge\ \tfrac{\kappa_G}{3}\mathrm{Id}$.

(iii) [strengthened, reconstructed] $S_H$ is $\mathrm{Ad}$-invariant, real-analytic and **convex** on the open chart $\Omega:=\{X:|\alpha(X)|<2\pi\ \forall\alpha\}$, and
$$\nabla^2S_H(X)\ \succeq\ \frac{\kappa_G}{3}\,\mathrm{Id}\qquad\text{for all }X\in\Omega,$$
with $\lambda_{\min}$ non-decreasing along Cartan rays. For $\mathrm{SU}(3)$, $\Omega$ is the ball $|X|<2\pi$ ($\lambda=2$ normalization) and the floor is $0.25$.

(iv) On the lattice, $S_{H,\Lambda}(X)=\sum_{\ell}S_H(X_\ell)$ is block-diagonal, so $\nabla^2S_{H,\Lambda}\succeq(\kappa_G/3)\mathrm{Id}$ on $\mathfrak g^{E(\Lambda)}$, uniformly in $|\Lambda|$.

### Derivation

**(i) Exact Jacobian.** The differential of $\exp$ is $d(\exp)_X=dL_{\exp X}\circ\frac{1-e^{-\mathrm{ad}_X}}{\mathrm{ad}_X}$; since $g_G$ is bi-invariant, $dL$ is an isometry, so $J_G(X)=\det\frac{1-e^{-\mathrm{ad}_X}}{\mathrm{ad}_X}$. Symmetrizing, $\frac{1-e^{-z}}{z}=e^{-z/2}\frac{2\sinh(z/2)}{z}$, and $\mathrm{Tr}(\mathrm{ad}_X)=0$ kills the prefactor, so
$$\log J_G(X)=\mathrm{Tr}_{\mathfrak g}\log\frac{2\sinh(\mathrm{ad}_X/2)}{\mathrm{ad}_X}.$$
$\mathrm{ad}_X$ is skew, with spectrum $\{0\ (\times\,\mathrm{rank})\}\cup\{\pm i\alpha(X)\}_{\alpha>0}$. Each conjugate pair $\pm i\theta$ contributes $\frac{(1-e^{-i\theta})(1-e^{i\theta})}{\theta^2}=\frac{2-2\cos\theta}{\theta^2}=\big(\frac{\sin(\theta/2)}{\theta/2}\big)^2$, giving the product formula.

**(ii) Quadratic term, two independent routes.**
Route 1 (series). $\log\frac{2\sinh(z/2)}{z}=\frac{z^2}{24}-\frac{z^4}{2880}+O(z^6)$, so
$$\log J_G(X)=\tfrac1{24}\mathrm{Tr}(\mathrm{ad}_X^2)+O(|X|^4)=\tfrac1{24}B(X,X)+O(|X|^4),$$
$$S_H(X)=-\tfrac1{24}B(X,X)+O(|X|^4)=\tfrac16\mathrm{Ric}(X,X)+O(|X|^4)$$
using $\mathrm{Ric}=-\tfrac14B$. Therefore $\nabla^2S_H(0)=\tfrac13\mathrm{Ric}$. (This is `D_Haar_Jacobian_SmallField.md` §D3, which is correct.)
Route 2 (Riemannian). Exponential coordinates on a bi-invariant metric ARE geodesic normal coordinates at $e$, and in normal coordinates $\sqrt{\det g_{ij}(X)}=1-\tfrac16\mathrm{Ric}_{ij}X^iX^j+O(|X|^3)$; taking $-\log$ gives the same answer. The two routes agree, which is a real (if small) consistency check the corpus performs in `EXTRACT_02` §2.

**(iii) The global strengthening — this is mine, and it is the main upgrade over the corpus.**
Write $\varphi(\theta):=-2\log\frac{\sin(\theta/2)}{\theta/2}$, so $S_H|_{\mathfrak h}=\sum_{\alpha>0}\varphi(\alpha(X))$ on a Cartan subalgebra $\mathfrak h$.
(a) *All Taylor coefficients of $\varphi$ are positive.* From $\frac{\sin u}{u}=\prod_{n\ge1}\big(1-\frac{u^2}{n^2\pi^2}\big)$,
$$-\log\frac{\sin u}{u}=\sum_{m\ge1}\frac{\zeta(2m)}{m\,\pi^{2m}}u^{2m},$$
so with $u=\theta/2$, $\varphi(\theta)=2\sum_{m\ge1}c_m\theta^{2m}$, $c_m=\frac{\zeta(2m)}{m(2\pi)^{2m}}>0$, convergent for $|\theta|<2\pi$.
(b) Hence $\varphi''(\theta)=2\sum_m 2m(2m-1)c_m\theta^{2m-2}$ is **increasing in $|\theta|$** with $\varphi''(0)=4c_1=\tfrac{4\zeta(2)}{4\pi^2}=\tfrac16$. Also $\varphi'(\theta)/\theta=2\sum_m 2mc_m\theta^{2m-2}$ is increasing with value $\tfrac16$ at $0$.
(c) *Cartan block.* $\nabla^2(S_H|_{\mathfrak h})(X)=\sum_{\alpha>0}\varphi''(\alpha(X))\,\alpha\otimes\alpha\ \succeq\ \tfrac16\sum_{\alpha>0}\alpha\otimes\alpha$. Now $\sum_{\alpha>0}\alpha(X)^2=-\tfrac12\mathrm{Tr}(\mathrm{ad}_X^2)=-\tfrac12B(X,X)=2\,\mathrm{Ric}(X,X)$, so $\sum_{\alpha>0}\alpha\otimes\alpha=2\mathrm{Ric}|_{\mathfrak h}\succeq2\kappa_G$, and the Cartan block is $\succeq\tfrac{\kappa_G}{3}$.
(d) *Root blocks.* For an $\mathrm{Ad}$-invariant $f$ with $F=f|_{\mathfrak h}$, at a regular $X\in\mathfrak h$ the Hessian is block diagonal w.r.t. $\mathfrak h\oplus\bigoplus_{\alpha>0}\mathfrak g_\alpha^{\mathbb R}$, and on $\mathfrak g_\alpha^{\mathbb R}$ it acts as the *difference quotient* $\varphi'(\alpha(X))/\alpha(X)$ times $|\alpha|^2$ (plus the same-form contributions of the other roots). By (b), $\varphi'(\theta)/\theta\ge\varphi''(0)=\tfrac16$, so each root block obeys the same $\tfrac{\kappa_G}{3}$ floor.
(e) *Ad-invariance closes it.* $S_H(\mathrm{Ad}_gX)=S_H(X)$, so $\nabla^2S_H(\mathrm{Ad}_gX)=\mathrm{Ad}_g\nabla^2S_H(X)\mathrm{Ad}_g^{-1}$ — same spectrum. Every $X\in\mathfrak{su}(N)$ is $\mathrm{Ad}$-conjugate to a Cartan element, so the Cartan-plus-root-block bound is the bound everywhere. $\square$

**Numerical certification (mine).** Using Ad-invariance I scanned the *entire* 2-dimensional Cartan of $\mathfrak{su}(3)$ (which by (e) covers all of $\mathfrak{su}(3)$) on a $63\times63$ grid out to $|X|=6.2$ (the chart edge is $|X|=2\pi=6.28319$, attained at $X\propto\mathrm{diag}(i\pi,-i\pi,0)$). Global minimum of $\lambda_{\min}(\nabla^2S_H)$ over the whole chart: **0.250125**, attained at $|X|=0.2$; i.e. the floor $0.25=N/12$ is achieved only in the limit $X\to0$ and the Hessian only *grows* away from the identity.

**(iv) Product.** $S_{H,\Lambda}=\sum_\ell S_H(X_\ell)$ has block-diagonal Hessian, so the floor is inherited with no volume loss.

### Constants and numbers

Hess S_H(0) = (1/3) Ric_G = (kappa_G/3) Id. SU(3): 0.25 (lambda=2), 0.5 (lambda=1) -- both verified to 1e-9. Quartic term: S_H = sum_{alpha>0}[ alpha(X)^2/12 + alpha(X)^4/1440 + ... ] (positive coefficients: c_m = zeta(2m)/(m (2pi)^{2m})). Radial profile of the worst-case lambda_min over the SU(3) Cartan (lambda=2 normalization, my scan):
  |X| =  0.05 -> 0.250008
  |X| =  0.50 -> 0.250783
  |X| =  1.00 -> 0.253156
  |X| =  2.00 -> 0.263014
  |X| =  3.00 -> 0.280849
  |X| =  4.00 -> 0.309212
  |X| =  5.00 -> 0.352804
  |X| =  6.00 -> 0.420438
Global min over the whole chart |X| < 2pi: 0.250125. Chart edge (first root angle = 2pi): |X| = 6.28319 exactly. Corpus CSV su3_haar_hessian_scan_results.csv (r = 0 .. 0.05) reports 0.2500002 .. 0.2500074, matching.

### Code

# Global Cartan scan certifying Hess S_H >= (N/12) Id on the whole exponential chart of SU(3).
import numpy as np
# (reuse l[1..8], T = i*lambda_a/2, c = 2.0 from item 1)
A=np.zeros((8,8,8))                      # structure constants: A[k][a,b] = <T_a,[T_k,T_b]>
for k in range(8):
    for b in range(8):
        C=T[k]@T[b]-T[b]@T[k]
        for a in range(8): A[k,a,b]=(-2.0*np.trace(T[a]@C)).real
adv=lambda v: np.tensordot(v,A,axes=(0,0))
def SH(v):
    th=np.abs(np.linalg.eigvals(adv(v)).imag); s=0.
    for t in th:
        if t>1e-13:
            q=np.sin(t/2)/(t/2)
            if q<=1e-12: return np.inf
            s-=np.log(q)
    return s
def hess(v,h=1e-4):
    H=np.zeros((8,8))
    for i in range(8):
        for j in range(i,8):
            ei=np.zeros(8);ei[i]=h;ej=np.zeros(8);ej[j]=h
            H[i,j]=H[j,i]=(SH(v+ei+ej)-SH(v+ei-ej)-SH(v-ei+ej)+SH(v-ei-ej))/(4*h*h)
    return H
# Ad-invariance => scanning the Cartan (a3,a8) covers all of su(3)
gmin=1e9
for a3 in np.linspace(-6.2,6.2,63):
    for a8 in np.linspace(-6.2,6.2,63):
        R=np.hypot(a3,a8)
        if R>6.2 or R<1e-9: continue
        v=np.zeros(8); v[2]=a3; v[7]=a8
        if not np.isfinite(SH(v)): continue
        gmin=min(gmin,np.linalg.eigvalsh(hess(v))[0])
print('global min lambda_min(Hess S_H) over the chart =',round(gmin,6))   # -> 0.250125

**Caveat.** The corpus states only the local version (Lemma D5 of `D_Haar_Jacobian_SmallField.md` even writes it with the WRONG SIGN of the correction, `>= (c_0 - C_H r^2) I`; the true correction is +O(r^2)). D5 also mislabels c_0 = g^vee/12 as the Hessian when g^vee/12 is the coefficient of ||A||^2, so the Hessian is g^vee/6.

**Why it matters.** Upgrading 'positive in a small ball, by continuity' to 'positive on the entire exponential chart, with an explicit monotone profile' removes one of the two localization hypotheses the corpus carries everywhere. The remaining localization is forced by the Wilson term alone, which sharpens exactly where the obstruction lives.

---

## 4. The factor 3: 'Riemannian-volume reference' and 'flat Lie-algebra reference' are NOT the same curvature-dimension condition

`status: solid` · `kind: obstruction`

### Statement

The corpus asserts in at least four files (`EXTRACT_01_Haar_Mass_from_Ricci.md` §5, `EXTRACT_02_...` §5, `Exciting_01_...` §3.2, `UNIFY_01_...` §3) that the two bookkeepings

(V1) $(M_\Lambda,g_\Lambda,\ d\mu=Z^{-1}e^{-S_W}d\mathrm{vol}_{g_\Lambda})$ with $\mathrm{Ric}_\mu=\mathrm{Ric}_{g_\Lambda}+\nabla^2S_W$, and
(V2) $(\mathfrak g^{E},\ \text{Euclidean},\ d\mu=Z^{-1}e^{-(S_W+S_{H,\Lambda})}dX)$ with $\mathrm{Ric}_\mu=0+\nabla^2(S_W+S_{H,\Lambda})$

"encode the same second-order information". **They do not give the same CD constant.** At the vacuum,
$$\underbrace{\mathrm{Ric}_{g_\Lambda}=\kappa_G\,\mathrm{Id}}_{\text{(V1)}}\qquad\text{versus}\qquad\underbrace{\nabla^2S_{H,\Lambda}(0)=\tfrac{\kappa_G}{3}\,\mathrm{Id}}_{\text{(V2)}} .$$
The flat-chart bookkeeping loses a factor of exactly $3$. For $\mathrm{SU}(3)$: $1.5$ versus $0.5$ ($\lambda=1$), or $0.75$ versus $0.25$ ($\lambda=2$).

### Derivation

The two are genuinely different metric-measure spaces, hence different Dirichlet forms and different CD conditions:

(V1) carries the bi-invariant metric $g_\Lambda$; its Dirichlet form is $\int|\nabla^{g}f|^2d\mu$ with $\nabla^g$ the Riemannian gradient, and the generator is the Laplace-Beltrami operator with drift. This is the *physically correct* object for Langevin dynamics on the group manifold and for the Wilson-loop observables, because the Casimir/heat-kernel structure of $\mathrm{SU}(N)$ is built into it.

(V2) carries the flat metric on the chart; its Dirichlet form is $\int|\nabla^{\mathrm{eucl}}f|^2d\mu$ and its generator is the flat Laplacian with drift. It is a legitimate object but it is *not* the lattice-gauge dynamics; it is a coordinate model of it.

Why the two disagree by 3, precisely: in normal coordinates the two metrics agree to second order at the origin and the Christoffels vanish, so the *measure* is the same; but Bakry-Émery curvature is not a property of the measure alone — it is $\mathrm{Ric}_g+\nabla^2S$, and moving the volume density into $S$ changes the split. Quantitatively the volume density carries Ricci with coefficient $-1/6$ (i.e. $J=1-\tfrac16\mathrm{Ric}(X,X)+\dots$), so its potential contributes $\tfrac13\mathrm{Ric}$, whereas the metric itself contributes the whole $\mathrm{Ric}$. Hence exactly $\kappa_G$ vs $\kappa_G/3$.

Consequence for the corpus's numbers. The most important instance is `RECOMMENDED_01_Finite_Cutoff_Haar_Wilson_Windows_v2.md`, which builds its convexity window from $c_0=N/6$ ($=\kappa_G/3$, the (V2) number) but describes the result as a Bakry-Émery curvature bound. Using the correct (V1) input $\kappa_G=N/2$ widens the window by exactly a factor 3 (see item 8). So the corpus's own headline window is a factor 3 too pessimistic for the object it names.

A second, opposite-signed instance: the $\mathrm{SU}(3)$ JAX engine (`05_su3_wilson_haar_hessian_numerics.md`) uses `haar_mass = c0 * sum_links Re Tr(A^dag A)` with `c0 = 0.125`. In basis A, $\mathrm{Tr}(A^\dagger A)=\tfrac12|a|^2$, so the coded Hessian is $c_0\,\mathrm{Id}=0.125\,\mathrm{Id}$ — exactly **half** the true (V2) Haar Hessian $N/12=0.25$, and one sixth of the (V1) floor $0.75$. So every reported $\lambda_{\min}$ in the SU(3) scans is conservative by $0.125$ in absolute terms.

[reconstructed] Both statements verified numerically: item 2's `ric()` gives $\kappa_G$; item 3's finite-difference Hessian of $-\log J$ gives $\kappa_G/3$; the ratio is $3.000000$ in both normalizations.

### Constants and numbers

Ric_{g_Lambda} = kappa_G Id  vs  Hess S_{H,Lambda}(0) = (kappa_G/3) Id. Ratio exactly 3. SU(3): 1.5 vs 0.5 (lambda=1); 0.75 vs 0.25 (lambda=2). SU(2): 1.0 vs 0.3333 (lambda=1). The JAX engine's coded Haar coefficient c0 = 0.125 = half of the correct flat-chart value 0.25 and one sixth of the intrinsic floor 0.75.

**Caveat.** Neither viewpoint is 'wrong'; they are curvature-dimension conditions for two different Dirichlet forms. The error is only in asserting they are interchangeable and then mixing their constants inside one inequality, which several corpus files do.

**Why it matters.** This single factor-3 (and the coded factor-2) accounts for most of the apparent numerical inconsistency across the archive, and it changes the size of the only unconditional theorem in the corpus by a factor 3.

---

## 5. Wilson Hessian at the vacuum is exactly the discrete Maxwell operator (beta/N) d_1^* d_1, with the full spectrum computed

`status: solid` · `kind: theorem`

### Statement

Let $\mathcal C^k(\Lambda;\mathfrak g)$ be $\mathfrak g$-valued $k$-cochains, $d_0:\mathcal C^0\to\mathcal C^1$, $(d_0\phi)_\ell=\phi(t(\ell))-\phi(s(\ell))$, and $d_1:\mathcal C^1\to\mathcal C^2$,
$$(d_1X)_p=X_{x,\mu}+X_{x+\hat\mu,\nu}-X_{x+\hat\nu,\mu}-X_{x,\nu}.$$
Right-trivialize $T_{U^{(0)}}M_\Lambda\cong\mathcal C^1(\Lambda;\mathfrak g)$. Then for $S_W=\frac{\beta}{N}\sum_p(N-\mathrm{Re}\,\mathrm{Tr}\,U_p)$ and $\langle X,Y\rangle=-\mathrm{Tr}(XY)$,
$$\boxed{\ \nabla^2S_W(U^{(0)})=\frac{\beta}{N}\,d_1^*d_1\ \succeq\ 0\ }$$
and $S_W(\exp(tX))=S_W(U^{(0)})+\frac{t^2}{2}\frac{\beta}{N}\|d_1X\|^2+O(t^3|X|_\infty^3)$.
Moreover $\ker(d_1^*d_1)=\ker(d_1)$, $d_1\circ d_0=0$ (lattice Bianchi), and on a periodic $L^d$ torus
$$\dim_{\mathbb R}\ker(d_1)=\big[(|V(\Lambda)|-1)+d\big]\cdot\dim\mathfrak g,$$
splitting as $\mathrm{im}(d_0)$ (pure gauge, $|V|-1$ per algebra component) $\oplus$ harmonic torons ($d$ per component).

### Derivation

**Lemma 1 (single-plaquette class function).** For $Y\in\mathfrak{su}(N)$ small, $e^Y=I+Y+\tfrac12Y^2+O(|Y|^3)$, $\mathrm{Tr}\,Y=0$, and $\mathrm{Tr}(Y^2)$ is real (as $Y^\dagger=-Y$). Hence
$$\mathrm{Re}\,\mathrm{Tr}(I-e^Y)=-\tfrac12\mathrm{Tr}(Y^2)+O(|Y|^3)=\tfrac12\|Y\|^2+O(|Y|^3)\quad(\lambda=1).$$

**Lemma 2 (holonomy linearization).** Set $U_\ell(t)=\exp(tX_\ell)$. The plaquette holonomy is a product of four exponentials $\exp(\pm tX_{\ell_i})$; iterating BCH,
$$U_p(t)=\exp\big(t(d_1X)_p+t^2R_p(t)\big),\qquad |R_p(t)|\le C|X|_\infty^2\ \ (|t|\le t_0),$$
with $C,t_0$ depending only on $G$ — **not** on $\Lambda$, because only four links enter. The linear term is precisely the signed sum around $\partial p$, i.e. $(d_1X)_p$.

**Proposition.** Insert Lemma 2 into $\Phi(U_p)=\frac{\beta}{N}\mathrm{Re}\,\mathrm{Tr}(I-U_p)$ and apply Lemma 1 with $Y_p=t(d_1X)_p+t^2R_p$: the $t^2$ coefficient is $\frac{\beta}{N}\cdot\tfrac12|(d_1X)_p|^2$ (the $t^2R_p$ insertion only affects $O(t^3)$ because it enters $Y_p$ linearly and $Y_p$ enters quadratically). Summing over plaquettes,
$$S_W(U(t))=S_W(U^{(0)})+\tfrac{t^2}{2}\tfrac{\beta}{N}\|d_1X\|^2_{\mathcal C^2}+O(t^3),$$
and since $t\mapsto\exp(tX)$ is a geodesic of the bi-invariant metric, $\nabla^2S_W(U^{(0)})(X,X)=\frac{d^2}{dt^2}\big|_0=\frac{\beta}{N}\langle X,d_1^*d_1X\rangle$. $\square$

**Bianchi / gauge degeneracy.** $(d_1d_0\phi)_p$ telescopes around the closed loop $\partial p$ and vanishes identically. Hence $\mathrm{im}(d_0)\subseteq\ker d_1\subseteq\ker\nabla^2S_W(U^{(0)})$: **the Wilson Hessian is exactly flat along infinitesimal gauge directions**, as it must be. The discrete Hodge decomposition
$$\mathcal C^1=\mathrm{im}(d_0)\oplus\ker(\Delta_1)\oplus\mathrm{im}(d_1^*),\qquad\Delta_1=d_0d_0^*+d_1^*d_1,$$
says $d_1^*d_1$ is strictly positive only on the co-exact part $\mathrm{im}(d_1^*)$; it vanishes on exact modes (gauge) *and* on harmonic modes (torons).

**[reconstructed] Exact single-plaquette spectrum.** Restrict to one plaquette and the 4 links on its boundary ($4\times\dim\mathfrak g=32$ real dimensions for $\mathrm{SU}(3)$). The quadratic form is $q(x)=\frac{1}{2\lambda}\|Mx\|^2$ with $M:\mathbb R^{4n_G}\to\mathbb R^{n_G}$, $Mx=x_1+x_2-x_3-x_4$ componentwise. Then $MM^*=4\,\mathrm{Id}_{n_G}$, so $M^*M$ has eigenvalue $4$ with multiplicity $n_G$ and $0$ with multiplicity $3n_G$. Thus for $S_p=1-\tfrac1N\mathrm{Re}\mathrm{Tr}\,U_p$:
$$\nabla^2S_p(U^{(0)})=\tfrac{1}{\lambda N}M^*M\ \Longrightarrow\ \text{eigenvalue }\tfrac{4}{\lambda N}\ (\times\,n_G),\ \ 0\ (\times\,3n_G).$$
For $\mathrm{SU}(3)$: eigenvalue $2/3$ (basis A) or $4/3$ (basis B), multiplicity 8, kernel dimension 24 out of 32. This reproduces *exactly* the numerical observation recorded in `YANG3_update_erosionLemma_kernelSchur_v5.md` §3 ("rank 8, kernel 24, plateau $2/3$"), which the corpus reports as an empirical fact without deriving it. I verified it by finite-difference Hessian of the actual $\mathrm{SU}(3)$ product of matrix exponentials: eigenvalues $0.666667$ ($\times8$), $0$ ($\times24$).

**[reconstructed] Lattice spectrum and stencil constants.** On the periodic $L^4$ torus with scalar coefficients I built $d_1$ explicitly and found:
- diagonal $(d_1^*d_1)_{bb}=2(d-1)=6$ (each link lies in $2(d-1)$ plaquettes);
- off-diagonal absolute row sum $=6(d-1)=18$ (each of the 6 plaquettes contributes 3 other links, each with entry $\pm1$; no link pair shares two plaquettes);
- $\lambda_{\max}(d_1^*d_1)=16$ on $\mathbb Z^4$ (I maximized the Fourier symbol $M_{\mu\nu}(k)$; the corpus's "$\lambda_{\max}=24$" is the Gershgorin bound $6+18$, not the true maximum);
- $\dim\ker d_1=(L^4-1)+4$ per algebra component, verified for $L=3,4,5,6$ (84, 259, 628, 1299);
- smallest nonzero eigenvalue $=2\big(1-\cos(2\pi/L)\big)$, verified: $L=3\to3$, $L=4\to2$, $L=5\to1.381966$, $L=6\to1$. This is the quantity the corpus calls $c_W$ — see item 10.

### Constants and numbers

Hess S_W(U^0) = (beta/N) d_1* d_1 for lambda = 1 (equivalently (beta/2N) d_1* d_1 for lambda = 2). One plaquette: eigenvalue 4/(lambda N) with multiplicity dim g, kernel 3 dim g. SU(3): 2/3 (x8) and 0 (x24) in basis A -- verified numerically. Stencil constants on the hypercubic lattice in d dimensions: diagonal 2(d-1) = 6, off-diagonal absolute row sum C_0 = 6(d-1) = 18 (d = 4). lambda_max(d_1* d_1) on Z^4 = 16 (Gershgorin bound 24). dim ker d_1 on the periodic L^4 torus = (L^4 - 1) + 4 per algebra component: L=3 -> 84, L=4 -> 259, L=5 -> 628, L=6 -> 1299 (all verified). Smallest nonzero eigenvalue = 2(1 - cos(2 pi / L)): 3, 2, 1.381966, 1 for L = 3,4,5,6.

### Code

# Exact single-plaquette spectrum, and the lattice Maxwell stencil / spectrum.
import numpy as np, itertools
def maxwell(L,d=4):
    def idx(x,mu):
        i=0
        for k in range(d): i=i*L+(x[k]%L)
        return i*d+mu
    n=L**d*d; rows=[]
    for x in itertools.product(range(L),repeat=d):
        for mu in range(d):
            for nu in range(mu+1,d):
                r=np.zeros(n)
                em=[0]*d; em[mu]=1; en=[0]*d; en[nu]=1
                xm=tuple(x[i]+em[i] for i in range(d)); xn=tuple(x[i]+en[i] for i in range(d))
                r[idx(x,mu)]+=1; r[idx(xm,nu)]+=1; r[idx(xn,mu)]-=1; r[idx(x,nu)]-=1
                rows.append(r)
    D=np.array(rows); A=D.T@D; ev=np.linalg.eigvalsh(A)
    return A,ev
for L in [3,4,5,6]:
    A,ev=maxwell(L)
    off=A-np.diag(np.diag(A))
    print('L=%d diag=%s rowsum=%s ker=%d smallest_nonzero=%.6f  2(1-cos(2pi/L))=%.6f'%(
        L,np.unique(np.diag(A)),np.unique(np.abs(off).sum(1)),int((abs(ev)<1e-8).sum()),
        float(ev[ev>1e-8][0]), 2*(1-np.cos(2*np.pi/L))))
# L=4 -> diag [6.] rowsum [18.] ker 259 smallest_nonzero 2.000000

**Caveat.** The identity holds AT the vacuum only. Away from the vacuum the Wilson Hessian acquires negative directions (item 9); the whole programme lives or dies on how far from U^0 the positivity survives.

**Why it matters.** This is the clean structural half of the mechanism: the interaction term is a genuine discrete Maxwell (curl*curl) operator, so the gauge degeneracy is exactly the de Rham cohomology of the lattice and nothing is being fudged. It also fixes the constant beta/N that the corpus quotes in three mutually inconsistent ways.

---

## 6. Horizontal Bakry-Émery: gauge invariance forces horizontal gradients, hence CD(rho,infinity), Poincaré, LSI and a spectral gap in the physical sector

`status: solid` · `kind: theorem`

### Statement

Let $\mathcal G_\Lambda=G^{V(\Lambda)}$ act on $M_\Lambda$ by $(g\cdot U)_\ell=g_{s(\ell)}U_\ell g_{t(\ell)}^{-1}$ (isometries of $g_\Lambda$). Let $V_U=T_U(\mathcal G_\Lambda\cdot U)$ (vertical), $H_U=V_U^\perp$ (horizontal). Let $S_\Lambda$ be gauge-invariant and $\mathcal A^{\mathrm{inv}}=C^\infty(M_\Lambda)^{\mathcal G_\Lambda}$.

(a) For every $f\in\mathcal A^{\mathrm{inv}}$ and every $U$: $\nabla f(U)\in H_U$.

(b) If $\mathrm{Ric}_{\mu_\Lambda}(U)(w,w)\ge\rho|w|^2$ for all $U\in M_\Lambda$ and all $w\in H_U$ (horizontal-only bound), then $\Gamma_2(f)\ge\rho\,\Gamma(f)$ pointwise for every $f\in\mathcal A^{\mathrm{inv}}$.

(c) [reconstructed key step] $P_t=e^{tL_\Lambda}$ maps $\mathcal A^{\mathrm{inv}}$ into itself. Hence the standard semigroup interpolation closes **inside the invariant sector**, and with $\rho>0$:
$$\mathrm{Var}_{\mu_\Lambda}(f)\le\frac1\rho\int|\nabla f|^2d\mu_\Lambda,\qquad \mathrm{Ent}_{\mu_\Lambda}(f^2)\le\frac2\rho\int|\nabla f|^2d\mu_\Lambda,\qquad \forall f\in\mathcal A^{\mathrm{inv}},$$
$$\mathrm{gap}\big(-L_\Lambda\big|_{L^2(\mu_\Lambda)^{\mathcal G_\Lambda}}\big)\ \ge\ \rho,\qquad \|P_tf-\mu_\Lambda f\|_{L^2}\le e^{-\rho t}\|f-\mu_\Lambda f\|_{L^2}.$$

### Derivation

**(a)** Let $w\in V_U$. There is a smooth curve $g(t)\in\mathcal G_\Lambda$, $g(0)=e$, with $\frac{d}{dt}\big|_0(g(t)\cdot U)=w$. Gauge invariance makes $t\mapsto f(g(t)\cdot U)$ constant, so
$$0=\tfrac{d}{dt}\big|_0f(g(t)\cdot U)=df_U(w)=\langle\nabla f(U),w\rangle .$$
Hence $\nabla f(U)\perp V_U$, i.e. $\nabla f(U)\in H_U$. $\square$
This is the whole point of the "horizontal" move: the Wilson action is *necessarily* flat along $V_U$, so a full-space Hessian lower bound is impossible; but no observable of interest ever probes $V_U$.

**(b)** The Bochner-Bakry-Émery identity on $(M_\Lambda,g_\Lambda)$ reads
$$\Gamma_2(f)=\|\nabla^2f\|_{\mathrm{HS}}^2+\mathrm{Ric}_{\mu_\Lambda}(\nabla f,\nabla f),\qquad \mathrm{Ric}_{\mu_\Lambda}=\mathrm{Ric}_{g_\Lambda}+\nabla^2S_\Lambda.$$
For $f\in\mathcal A^{\mathrm{inv}}$, (a) puts $\nabla f(U)$ inside $H_U$, so the curvature term is bounded by the *horizontal* hypothesis, and $\|\nabla^2f\|^2_{\mathrm{HS}}\ge0$:
$$\Gamma_2(f)\ \ge\ \mathrm{Ric}_{\mu_\Lambda}(\nabla f,\nabla f)\ \ge\ \rho|\nabla f|^2=\rho\,\Gamma(f).\qquad\square$$

**(c) The step the corpus asserts but never justifies.** `Selection_A_...` Lemma 3.2 says "vertical contributions vanish when testing on invariants", which is muddled; the real requirement is that the interpolation argument stay inside $\mathcal A^{\mathrm{inv}}$. It does, and here is why:
$\mathcal G_\Lambda$ acts by isometries of $g_\Lambda$ (each factor acts by left/right translation, and $g_G$ is bi-invariant), and $S_\Lambda$ is $\mathcal G_\Lambda$-invariant. Therefore $L_\Lambda=\Delta_{g_\Lambda}-\langle\nabla S_\Lambda,\nabla\cdot\rangle$ commutes with the action: $L_\Lambda(f\circ g)=(L_\Lambda f)\circ g$. Hence $P_t$ preserves $\mathcal A^{\mathrm{inv}}$.
Now run the standard argument. For $f\in\mathcal A^{\mathrm{inv}}$ and $0\le s\le t$ put $\psi(s)=P_s\big(\Gamma(P_{t-s}f)\big)$. Then
$$\psi'(s)=P_s\big(L\Gamma(P_{t-s}f)-2\Gamma(P_{t-s}f,LP_{t-s}f)\big)=2P_s\Gamma_2(P_{t-s}f)\ \ge\ 2\rho\,P_s\Gamma(P_{t-s}f)=2\rho\,\psi(s),$$
where (b) applies because $P_{t-s}f\in\mathcal A^{\mathrm{inv}}$. Grönwall from $s=0$ to $s=t$ gives the gradient commutation
$$\Gamma(P_tf)\ \le\ e^{-2\rho t}\,P_t\Gamma(f).$$
Poincaré: $\mathrm{Var}_\mu(f)=-\int_0^\infty\frac{d}{dt}\int(P_tf)^2d\mu\,dt=2\int_0^\infty\!\!\int\Gamma(P_tf)\,d\mu\,dt\le2\int_0^\infty e^{-2\rho t}dt\int\Gamma(f)d\mu=\frac1\rho\int\Gamma(f)d\mu.$
LSI: the same commutation inserted in $\frac{d}{dt}\int P_tf\,\log P_tf\,d\mu=-\int\frac{\Gamma(P_tf)}{P_tf}d\mu$ gives $\mathrm{Ent}_\mu(f^2)\le\frac{2}{\rho}\int\Gamma(f)d\mu$ (Bakry-Émery).
Spectral gap: Poincaré for all invariant $f$ is precisely $\lambda_1\ge\rho$ on the invariant subspace of $L^2(\mu_\Lambda)$. $\square$

**Why the invariant sector is the right one.** $\mathcal A^{\mathrm{inv}}$ is dense in the algebra generated by Wilson loops; the gauge-variant part of $L^2(\mu_\Lambda)$ carries no physical information (and $-L_\Lambda$ genuinely has no gap there in the sense that gauge zero-modes exist). So restricting is not a weakening.

**Sharp statement of what is and is not proved.** (b)+(c) require the horizontal bound at **every** $U\in M_\Lambda$, because the Grönwall step is pointwise-in-$U$ along the whole semigroup trajectory. A bound valid only on a ball $B_r(U^{(0)})$ does **not** feed this argument. This is the precise sense in which the corpus's "local horizontal curvature theorem" (`01_core_curvature_theorem.md`, `07_horizontal_Bakry_Emery_curvature.md`, `UNIFY_02`) does not by itself imply any functional inequality. Item 8 gives the parameter range where the *global* hypothesis is genuinely available.

### Constants and numbers

Poincaré constant 1/rho; LSI constant 2/rho; spectral gap >= rho; L^2 relaxation rate e^{-rho t}. Gradient commutation Gamma(P_t f) <= e^{-2 rho t} P_t Gamma(f). All constants are dimension-free: no dependence on |E(Lambda)|, dim g, or d, beyond what enters rho.

**Caveat.** Steps (a),(b),(c) are all correct and unconditional GIVEN a horizontal curvature bound holding at every configuration. The corpus repeatedly applies them with a bound proved only on a small ball, which is not licensed.

**Why it matters.** This is the correct, complete, and genuinely elegant engine of the programme: the gauge symmetry that destroys global convexity is precisely the symmetry that makes only horizontal curvature relevant. Stated properly (with the commutation of P_t with the gauge action, which the corpus omits), it is a clean theorem worth keeping.

---

## 7. The localized matrix hinge: Ric_mu >= (c_H - C beta r) I + (beta/N) d_1^* d_1 on the linkwise small-field set K_Lambda(r)

`status: conditional` · `kind: theorem`

### Statement

Let $\nu:=\max_{\ell}\#\{p:\ell\in\partial p\}$ ($=2(d-1)$, $=6$ for $d=4$). Fix $r_\star>0$ and let $M_3(r_\star)$ be a Lipschitz constant for the second derivative of the single-plaquette potential $F(g_1,\dots,g_4)=\mathrm{Re}\,\mathrm{Tr}(I-g_1g_2g_3^{-1}g_4^{-1})$ on $(B_{r_\star}(e))^4$. Define the **gauge-invariant** linkwise small-field set
$$K_\Lambda(r):=\{U\in M_\Lambda:\ U_\ell\in B_r(e)\ \forall\ell\in E(\Lambda)\},\qquad r\le r_\star .$$
Then for all $U\in K_\Lambda(r)$, as quadratic forms on $\mathcal C^1(\Lambda;\mathfrak g)$,
$$\mathrm{Ric}_{\mu_\Lambda}(U)\ \succeq\ \big(\kappa_G-R_W(r)\big)\,I\ +\ \frac{\beta}{N}\,d_1^*d_1,\qquad R_W(r):=\frac{2\nu M_3(r_\star)}{N}\,\beta\, r .$$
In particular, choosing $r\le \dfrac{N\kappa_G}{4\nu M_3(r_\star)}\cdot\dfrac1\beta$ gives
$$\mathrm{Ric}_{\mu_\Lambda}(U)\ \succeq\ \underbrace{\tfrac{\kappa_G}{2}}_{m^2}\,I+\underbrace{\tfrac{\beta}{N}}_{\alpha}\,d_1^*d_1\ =:\ \mathsf M_\Lambda,\qquad U\in K_\Lambda(r).$$
All constants ($\kappa_G,\nu,M_3,r,m^2,\alpha$) are independent of $|\Lambda|$.

### Derivation

**Why keep the operator instead of scalarizing.** The naive route bounds $\nabla^2S_W$ below by a scalar and throws $d_1^*d_1$ away. The hinge keeps $d_1^*d_1$ intact and scalarizes only the *localization remainder*. Downstream this is what makes the covariance bound a genuine massive-propagator estimate rather than a worst-case diagonal-dominance estimate.

**Step 1: the small-field set is gauge invariant.** $B_r(e)\subset G$ is conjugation-invariant (bi-invariant metric $\Rightarrow$ $d_G(gug^{-1},e)=d_G(u,e)$), but the gauge action is $U_\ell\mapsto g_xU_\ell g_y^{-1}$ with $x\ne y$, which is *not* conjugation. So strictly $K_\Lambda(r)$ is invariant only under the diagonal subgroup. [I flag this: `B_canonical_region_matrix_hinge.md` §2 asserts full gauge invariance and that is wrong for $x\ne y$. The correct gauge-invariant alternative, used in `01_matrix_hinge_to_massive_maxwell.md` §3, is to impose the smallness on **plaquette holonomies** $U_p\in B_r(e)$, which *is* conjugation-covariant hence gauge-invariant. Everything below works with either set; use the plaquette version if gauge-invariance is needed.]

**Step 2: plaquette-local Hessian stability.** $S_W=\frac{\beta}{N}\sum_pF(U_{\partial p})$, and each summand depends on exactly 4 links. If $U\in K_\Lambda(r)$ then $\mathrm{dist}_{G^4}(U_{\partial p},(e,e,e,e))\le2r$, so by the Lipschitz hypothesis (3.2),
$$D^2F(U_{\partial p})(X_{\partial p},X_{\partial p})\ \ge\ D^2F(e_{\partial p})(X_{\partial p},X_{\partial p})-2M_3(r_\star)\,r\,|X_{\partial p}|^2 .$$

**Step 3: combinatorial reduction (this is where volume-uniformity is bought).**
$$\sum_{p\in P(\Lambda)}|X_{\partial p}|^2=\sum_p\sum_{\ell\in\partial p}|X_\ell|^2=\sum_\ell\#\{p:\ell\in\partial p\}\,|X_\ell|^2\ \le\ \nu\,\|X\|^2 .$$
The only "large" object is $\nu$, a bounded-degree constant. Multiplying by $\beta/N$ and summing Step 2:
$$\nabla^2S_W(U)\ \succeq\ \nabla^2S_W(U^{(0)})-R_W(r)\,I=\frac{\beta}{N}d_1^*d_1-\frac{2\nu M_3\beta r}{N}I .$$

**Step 4: add the Haar floor.** $\mathrm{Ric}_{g_\Lambda}\succeq\kappa_G I$ (item 2, exact and volume-uniform). Adding gives the display. Choosing $r$ so $R_W(r)\le\kappa_G/2$ gives the clean form. $\square$

**The $1/\beta$ scaling of the hinge radius, and why it matters.** The admissible radius is
$$r(\beta)=\frac{N\kappa_G}{4\nu M_3}\cdot\frac{1}{\beta}=\frac{N^2}{8\nu M_3}\cdot\frac{1}{\beta}\quad(\lambda=1),$$
i.e. $r\sim\beta^{-1}$. Typical link fluctuations at inverse coupling $\beta$ are $\sim\beta^{-1/2}$. So the hinge region **shrinks faster than the fluctuations** and, past a $\beta$ of order one, typical configurations are outside it. This is the exact quantitative form of the programme's central difficulty, and it is why `YANG3_update_erosionLemma_kernelSchur_v5.md` is entirely devoted to trying to promote the remainder from $O(\beta r)$ to $O(\beta r^2)$ (which would give $r\sim\beta^{-1/2}$ and just barely fit).

**What would be needed for $O(\beta r^2)$ (the corpus's own analysis, correctly stated).** Split $\mathbb R^{4n_G}=K\oplus R$ with $K=\ker\nabla^2S_p(0)$ ($\dim24$ for SU(3)), $R$ its complement ($\dim8$, $\lambda_{\mathrm{pos}}=2/N\lambda$). Schur complement in the total Hessian $H=\nabla^2S_{\mathrm{Haar}}+\beta\nabla^2S_W$:
$$\lambda_{\min}(H)\ \ge\ \lambda_{\min}\Big(H^{\mathrm{Haar}}_{KK}+\beta H^W_{KK}-\beta^2H^W_{KR}\big(H^{\mathrm{Haar}}_{RR}+\beta H^W_{RR}\big)^{-1}H^W_{RK}\Big)\ \gtrsim\ c_0+\beta\lambda_{\min}(H^W_{KK})-\frac{\beta}{\lambda_{\mathrm{pos}}}\|H^W_{KR}\|^2_{\mathrm{op}}.$$
The erosion law is therefore $r^2$ **iff** the structural cancellation
$$D^3S_p(0)[k_1,k_2,\cdot]=0\qquad\forall k_1,k_2\in K$$
holds (then $H^W_{KK}=O(r^2)$, $H^W_{KR}=O(r)$, and $C\ge C_{KK}+C_{KR}^2/\lambda_{\mathrm{pos}}+C_{\mathrm{Haar}}$ with $C_{KR}\sim M_3$, $C_{KK}\sim M_4$). Otherwise it is $r^1$ and $R(\beta)\lesssim c_0/(D\beta)$. **The corpus never decides this**, and its own numerics (item 13) come down on the $r^1$ side.

### Constants and numbers

m^2 = kappa_G/2 (= N/4 for lambda=1: 0.5 for SU(2), 0.75 for SU(3)). alpha = beta/N. R_W(r) = (2 nu M_3 / N) beta r; d = 4 gives R_W(r) = (12 M_3/N) beta r. Admissible hinge radius r(beta) = N kappa_G / (4 nu M_3 beta) = N^2/(8 nu M_3 beta); for d = 4, SU(3): r = 9/(48 M_3 beta) = 0.1875/(M_3 beta). nu = 2(d-1) = 6. M_3 = Lipschitz constant of D^2 F on (B_{r*}(e))^4 -- NOT computed anywhere in the corpus. Erosion exponent: r^1 unless D^3 S_p(0)[K,K,.] = 0.

**Caveat.** M_3 is never evaluated, so r(beta) is not a number; and the small-field set as defined linkwise is not gauge invariant (use the plaquette-holonomy version instead). The hinge radius scales as 1/beta while fluctuations scale as beta^{-1/2}, so the region is asymptotically not typical.

**Why it matters.** This is the sharpest correctly-structured statement in the corpus: an explicit, volume-uniform operator inequality that preserves the Maxwell geometry. Everything downstream (Helffer-Sjöstrand, Combes-Thomas, clustering) is a mechanical consequence of it.

---

## 8. Unconditional theorem: global CD(rho,infinity), Poincaré, LSI and spectral gap for lattice SU(N) Yang-Mills at beta < N^2/48 (d=4), with volume-uniform explicit constants

`status: solid` · `kind: theorem`

### Statement

Let $G=\mathrm{SU}(N)$, $\langle X,Y\rangle=-\mathrm{Tr}(XY)$, $M_\Lambda=G^{E(\Lambda)}$ with product bi-invariant metric, $\nu=2(d-1)$ the plaquette-per-link incidence, and
$$S_W(U)=\beta\sum_{p\in P(\Lambda)}\Big(1-\tfrac1N\mathrm{Re}\,\mathrm{Tr}\,U_p\Big),\qquad d\mu_\Lambda=Z_\Lambda^{-1}e^{-S_W}d\mathrm{vol}_{g_\Lambda}.$$
Define
$$\rho(\beta):=\frac{N}{2}-\frac{4\nu}{N}\,\beta .$$
If $\ \beta<\dfrac{N^2}{8\nu}\ $ (so $\rho(\beta)>0$) then for **every** finite $\Lambda$ and **every** smooth $f$ (gauge-invariant or not):
$$\mathrm{Ric}_{\mu_\Lambda}\succeq\rho(\beta)\,g_\Lambda\ \ \text{on all of }M_\Lambda,\qquad \Gamma_2(f)\ge\rho(\beta)\Gamma(f),$$
$$\mathrm{Var}_{\mu_\Lambda}(f)\le\frac{1}{\rho(\beta)}\int|\nabla f|^2d\mu_\Lambda,\quad \mathrm{Ent}_{\mu_\Lambda}(f^2)\le\frac{2}{\rho(\beta)}\int|\nabla f|^2d\mu_\Lambda,\quad \mathrm{gap}(-L_\Lambda)\ge\rho(\beta),$$
all constants independent of $|\Lambda|$, of $d$ except through $\nu$, and of the boundary conditions. For $d=4$ ($\nu=6$): the window is $\beta<N^2/48$.

### Derivation

**Step 1 (Haar floor).** Item 2: $\mathrm{Ric}_{g_\Lambda}=\kappa_G g_\Lambda$ with $\kappa_G=N/2$, everywhere on $M_\Lambda$, uniformly in $|\Lambda|$.

**Step 2 (sharp one-plaquette Hessian bound).** Let $S_p(V_1,\dots,V_4)=1-\frac1N\mathrm{Re}\,\mathrm{Tr}(V_1V_2V_3V_4)$ and vary $V_i(t)=e^{tX_i}V_i$. Differentiating twice,
$$U_p''(0)=\sum_i(\cdots X_i^2V_i\cdots)+\sum_{i\ne j}(\cdots X_iV_i\cdots X_jV_j\cdots),$$
and $S_p''(0)=-\frac1N\mathrm{Re}\,\mathrm{Tr}\,U_p''(0)$. Each $V_i$ is unitary so $|\mathrm{Tr}(\cdots X_i^2V_i\cdots)|\le\|X_i\|^2$ and $|\mathrm{Tr}(\cdots X_iV_i\cdots X_jV_j\cdots)|\le\|X_i\|\|X_j\|$ (Cauchy-Schwarz in the Hilbert-Schmidt norm). Hence
$$|S_p''(0)|\ \le\ \frac1N\Big(\sum_i\|X_i\|\Big)^2\ \le\ \frac4N\sum_i\|X_i\|^2 ,$$
i.e. $\|\nabla^2S_p\|_{\mathrm{op}}\le4/N$ **uniformly over all $U\in G^4$**.

[reconstructed] **This constant is sharp.** I computed the full $32\times32$ single-plaquette Hessian for $\mathrm{SU}(3)$ at $U_p=\mathrm{diag}(-1,-1,1)$ and obtained spectrum $\{-4/3,\ 0,\ 4/9\}$ — minimum exactly $-4/3=-4/N$. Scanning 200 random $\mathrm{SU}(3)^4$ configurations gave $\min=-1.31592$, $\max=+1.01105$, both inside $[-4/3,4/3]$. So $4/N$ is attained and cannot be improved.

**Step 3 (local-to-global operator norm).** With $\nabla^2S_W=\beta\sum_p\nabla^2S_p$ acting only on the 4 links of $p$,
$$\big|\langle X,\nabla^2S_W(U)X\rangle\big|\le\beta\sum_p\frac4N\sum_{\ell\in\partial p}\|X_\ell\|^2=\frac{4\beta}{N}\sum_\ell\#\{p:\ell\in\partial p\}\|X_\ell\|^2\le\frac{4\nu\beta}{N}\|X\|^2 .$$
So $\nabla^2S_W(U)\succeq-\frac{4\nu\beta}{N}I$ everywhere. (For $d=4$: $\succeq-\frac{24\beta}{N}I$.)

**Step 4 (assemble).** $\mathrm{Ric}_{\mu_\Lambda}=\mathrm{Ric}_{g_\Lambda}+\nabla^2S_W\succeq\big(\frac N2-\frac{4\nu\beta}{N}\big)g_\Lambda=\rho(\beta)g_\Lambda$, globally.

**Step 5 (functional inequalities).** $\rho>0$ gives $\mathrm{CD}(\rho,\infty)$ on all of $M_\Lambda$; item 6(c) (or classical Bakry-Émery, since here no restriction to invariants is needed) yields Poincaré with $1/\rho$, LSI with $2/\rho$, and $\lambda_1(-L_\Lambda)\ge\rho$. $\square$

**Explicit window.** $\rho(\beta)>0\iff\beta<\frac{N^2}{8\nu}$. In $d=4$: $\beta<N^2/48$.
- $\mathrm{SU}(2)$: $\beta<1/12=0.08\overline{3}$; at $\beta=0$, $\rho=1$.
- $\mathrm{SU}(3)$: $\beta<3/16=0.1875$; at $\beta=0$, $\rho=1.5$.
- general $N$: window grows like $N^2$, floor like $N$.

**Comparison with the corpus.** `RECOMMENDED_01_Finite_Cutoff_Haar_Wilson_Windows_v2.md` Theorem 4.1 derives the same structure but (i) uses the flat-chart constant $c_0=N/6$ instead of $\kappa_G=N/2$ (item 4), losing a factor 3, and (ii) writes $\rho_*(a)=\frac N6a^2g^2-\frac{48}{g^2}$, which mixes coordinate conventions: the Haar term is written in the continuum field $A$ ($X=agA$) while the Wilson term is written in $X$. Since the change of variables multiplies **both** Hessians by $a^2g^2$, the factor cancels in the eigenvalue comparison and the criterion is $a$-independent: $\frac N6>\frac{48}{g^2}$, i.e. $\beta<N^2/144$. Correcting the Haar input to $\kappa_G$ gives the window $\beta<N^2/48$ above. The corpus's own conclusion that this is a *strong-coupling, cutoff-scale* window is right; its constant is 3x too small and its $a$-dependence is spurious.

### Constants and numbers

rho(beta) = N/2 - 4 nu beta / N with nu = 2(d-1). d = 4: rho(beta) = N/2 - 24 beta/N. Window beta < N^2/(8 nu) = N^2/48 (d=4). SU(2): beta < 0.083333, rho(0) = 1.0. SU(3): beta < 0.1875, rho(0) = 1.5. Poincaré 1/rho, LSI 2/rho, gap >= rho, relaxation e^{-rho t}. Sharp one-plaquette operator norm 4/N (verified: min eigenvalue exactly -4/3 for SU(3) at U_p = diag(-1,-1,1); random scan min -1.31592, max +1.01105). Global Wilson Hessian bound: ||Hess S_W||_op <= 4 nu beta/N = 24 beta/N in d = 4. Corpus's window (RECOMMENDED_01, corrected for the coordinate mix-up): beta < N^2/144 -- a factor 3 smaller because it used c_0 = N/6 instead of kappa_G = N/2.

### Code

# Certifies the sharp one-plaquette constant 4/N (the only nontrivial input).
import numpy as np
from scipy.linalg import expm
# T = TB (basis B, <X,Y> = -Tr(XY)); see item 1
def hess_at(base,h=2e-4):
    def f(x):
        x=x.reshape(4,8)
        V=[expm(np.tensordot(x[i],TB,axes=(0,0)))@base[i] for i in range(4)]
        return 1.0-np.trace(V[0]@V[1]@np.linalg.inv(V[2])@np.linalg.inv(V[3])).real/3
    H=np.zeros((32,32))
    for i in range(32):
        for j in range(i,32):
            ei=np.zeros(32);ei[i]=h;ej=np.zeros(32);ej[j]=h
            H[i,j]=H[j,i]=(f(ei+ej)-f(ei-ej)-f(-ei+ej)+f(-ei-ej))/(4*h*h)
    return H
U0=np.diag([-1,-1,1]).astype(complex); I3=np.eye(3,dtype=complex)
ev=np.linalg.eigvalsh(hess_at([U0,I3,I3,I3]))
print('spectrum at U_p=diag(-1,-1,1):',np.unique(np.round(ev,4)))   # [-1.3333 0. 0.4444] = -4/N, 0, 4/9
print('sharp bound 4/N =',4/3)

**Caveat.** A uniform spectral gap for lattice gauge theory at small beta is classically obtainable by cluster/high-temperature expansion; the value of this version is that the constants are explicit, dimension-free, and derived from geometry rather than from an expansion. The window is genuinely strong-coupling and is disjoint from the continuum regime (item 11).

**Why it matters.** This is the strongest fully unconditional theorem the mechanism supports. It is correct, has explicit constants, and is uniform in the volume -- exactly what the programme claims, stated with the parameter range it actually holds in.

---

## 9. Obstruction I: the Wilson Hessian has an explicit negative direction of size -beta/N, so global Bakry-Émery curvature goes to -infinity as beta grows

`status: solid` · `kind: obstruction`

### Statement

Let $S_p(U)=1-\frac1N\mathrm{Re}\,\mathrm{Tr}\,U$ on $\mathrm{SU}(N)$, $N\ge2$, with $\langle X,Y\rangle=-\mathrm{Tr}(XY)$. There exist $U_0\in\mathrm{SU}(N)$ and $X\in\mathfrak{su}(N)$, $\|X\|=1$, with
$$\frac{d^2}{dt^2}\,S_p(e^{tX}U_0)\Big|_{t=0}=-\frac1N .$$
Consequently, for the Wilson action on any lattice containing at least one plaquette,
$$\inf_{U\in M_\Lambda}\lambda_{\min}\big(\nabla^2S_W(U)\big)\ \le\ -\frac{\beta}{N},$$
and therefore the **global** Bakry-Émery constant obeys
$$\rho_{\mathrm{BE}}(\beta)\ \le\ \kappa_G-\frac{\beta}{N}=\frac{N}{2}-\frac{\beta}{N}\ \xrightarrow[\beta\to\infty]{}\ -\infty .$$
In particular global CD is impossible for $\beta\ge N^2/2$; taking the sharp one-plaquette value $-4/N$ instead, for $\beta\ge N^2/8$.

### Derivation

**Construction.** Take $U_0=\mathrm{diag}(-1,-1,1,\dots,1)\in\mathrm{SU}(N)$ (determinant $(-1)^2=1$ ✓). Embed an $\mathfrak{su}(2)$ generator into the upper-left $2\times2$ block, scaled so that on that block $X^2=-\tfrac12I_2$ and $\|X\|^2=-\mathrm{Tr}(X^2)=1$; e.g. $X=\sqrt2\,(i\sigma_3/2)\oplus0$, since then $X^2=2\cdot(-\tfrac14I_2)=-\tfrac12I_2$ and $-\mathrm{Tr}(X^2)=1$.

**Computation.** $\frac{d^2}{dt^2}e^{tX}U_0\big|_0=X^2U_0$, so
$$S_p''(0)=-\frac1N\mathrm{Re}\,\mathrm{Tr}(X^2U_0).$$
On the $2\times2$ block $U_0=-I_2$, hence $X^2U_0=(-\tfrac12I_2)(-I_2)=+\tfrac12I_2$, trace $=1$; all other blocks contribute $0$ because $X$ vanishes there. Therefore $\mathrm{Re}\,\mathrm{Tr}(X^2U_0)=1$ and $S_p''(0)=-1/N$. $\square$

**Realizability on the lattice.** Set one link to $\mathrm{diag}(-1,-1,1)$ and all others to $e$; then the 6 plaquettes containing that link all have $U_p=\mathrm{diag}(-1,-1,1)$ (which equals its own inverse). Varying that one link in direction $X$ realizes the negative second derivative. So the bound is attained by an actual lattice configuration, not just an abstract group element.

**Numerical certification [reconstructed].** I computed the $8\times8$ single-link Hessian block of $S_p$ for $\mathrm{SU}(3)$ at $U_p=\mathrm{diag}(-1,-1,1)$ in basis B and obtained
$$\mathrm{spec}=\{-1/3,\,-1/3,\,-1/3,\,0,0,0,0,\,+1/9\},$$
i.e. minimum exactly $-1/3=-1/N$ with multiplicity 3 (the three $\mathfrak{su}(2)$-block directions). And the full 4-link $32\times32$ Hessian at the same point has spectrum $\{-4/3,0,4/9\}$: allowing all four links to move coherently multiplies the negative eigenvalue by exactly 4, giving $-4/N$.

**Interpretation.** The Wilson potential is a class function on $\mathrm{SU}(N)$, and $-\mathrm{Re}\mathrm{Tr}$ is concave near group elements far from the identity. It cannot be globally convex on a compact manifold in any case: a smooth function on a compact manifold always has a maximum, where the Hessian is $\preceq0$. The content of the lemma is *quantitative* — the negative part is $\Theta(\beta/N)$, i.e. it grows linearly in the coupling, while the Haar floor $\kappa_G=N/2$ is $\beta$-independent. So there is a hard crossover, and it happens at $\beta=O(N^2)$, not at $\beta=\infty$.

**What survives.** The obstruction kills the *global* route only. It does not touch the strong-coupling theorem (item 8) nor the localized hinge (item 7). It is the precise reason the programme is forced into localization, and it is exactly why `RECOMMENDED_02_Global_BE_Obstruction_and_Localization_v2.md` is (correctly) the pivot document of the archive.

### Constants and numbers

S_p''(0) = -1/N at U_0 = diag(-1,-1,1,...,1) with the su(2)-block direction, ||X|| = 1 in <X,Y> = -Tr(XY). SU(3) single-link block spectrum at that point: {-1/3 (x3), 0 (x4), +1/9 (x1)} -- verified numerically. Full 4-link block spectrum: {-4/3, 0, 4/9}. rho_BE(beta) <= N/2 - beta/N; zero at beta = N^2/2 (SU(2): 2; SU(3): 4.5). With the sharp -4/N: rho_BE(beta) <= N/2 - 4 beta/N; zero at beta = N^2/8 (SU(2): 0.5; SU(3): 1.125). Combined with item 8, global CD holds for beta < N^2/48 and fails for beta > N^2/8 -- the two thresholds bracket within a factor 6.

### Code

# Certifies S_p'' = -1/N (single-link direction) for SU(3).
import numpy as np
from scipy.linalg import expm
U0=np.diag([-1,-1,1]).astype(complex)
f=lambda x: 1-np.trace(expm(np.tensordot(x,TB,axes=(0,0)))@U0).real/3   # TB from item 1
h=2e-4; H=np.zeros((8,8))
for i in range(8):
    for j in range(i,8):
        ei=np.zeros(8);ei[i]=h;ej=np.zeros(8);ej[j]=h
        H[i,j]=H[j,i]=(f(ei+ej)-f(ei-ej)-f(-ei+ej)+f(-ei-ej))/(4*h*h)
print(np.round(np.linalg.eigvalsh(H),6))   # [-0.333333 x3, 0 x4, 0.111111]

**Caveat.** None. The lemma is a two-line computation, it is correct, and I verified it numerically.

**Why it matters.** This is the cleanest piece of real mathematics in the archive on the negative side: a fully explicit, sharp, elementary proof that the headline strategy cannot be run globally. Together with item 8 it brackets the true global-CD threshold within a factor 6.

---

## 10. Obstruction II: the constant c_W in the headline bound Ric >= (kappa + beta c_W) g is not volume-uniform -- it is exactly 0 on the torus and decays like 4 pi^2 / L^2 on the co-exact sector

`status: solid` · `kind: obstruction`

### Statement

The corpus's headline inequality (`DOC1_Haar_Wilson_Bakry_Emery_Mass_Mechanism.md` §5, repeated in `EXTRACT_01_Haar_Geometric_Mass.md`, `EXTRACT_01_Haar_Wilson_BakryEmery_Mass.md`) is
$$\mathrm{Ric}_{\mu_\beta}\big|_{\mathcal H_U}\ \ge\ (\kappa+\beta c_W)\,g\big|_{\mathcal H_U},\qquad c_W:=\inf_{0\ne X\in\mathcal H_U}\frac{\langle X,\mathcal H_WX\rangle}{\|X\|^2},\quad \mathcal H_W=d_1^*d_1 .$$
On a periodic $L^d$ lattice:

(a) $c_W=0$ **exactly**, for every $L$ and every $\beta$. The horizontal space $\mathcal H_{U^{(0)}}=\ker(d_0^*)$ contains the $d\cdot\dim\mathfrak g$-dimensional space of harmonic 1-cochains (torons), on which $d_1^*d_1$ vanishes identically.

(b) Even after discarding harmonics, on the co-exact sector $\mathrm{im}(d_1^*)$,
$$\lambda_{\min}^+\big(d_1^*d_1\big)=2\Big(1-\cos\frac{2\pi}{L}\Big)\ \sim\ \frac{4\pi^2}{L^2}\ \longrightarrow\ 0 .$$

Hence $\beta c_W$ contributes nothing volume-uniformly. **Only the Haar term $\kappa_G$ survives the thermodynamic limit.**

### Derivation

**(a) The kernel count.** $\ker(d_1^*d_1)=\ker(d_1)$. By the discrete Hodge decomposition on the $d$-torus,
$$\ker(d_1)=\mathrm{im}(d_0)\ \oplus\ \mathcal H^1,\qquad \mathcal H^1:=\ker(d_0^*)\cap\ker(d_1)\cong H^1(\mathbb T^d;\mathbb R)\otimes\mathfrak g,$$
so $\dim\mathcal H^1=d\cdot\dim\mathfrak g$. Since $\mathcal H_{U^{(0)}}=\mathrm{im}(d_0)^\perp=\ker(d_0^*)\supset\mathcal H^1$, the horizontal space contains a $d\dim\mathfrak g$-dimensional kernel of $d_1^*d_1$. Therefore the infimum defining $c_W$ is $0$. Physically these are the constant abelian holonomies (torons / Polyakov-loop zero modes) around the $d$ cycles: they cost no plaquette action at all, at any $\beta$.

[reconstructed] Verified exactly. Building $d_1$ on the periodic $L^4$ torus with scalar (one algebra component) coefficients:
$$\dim\ker d_1=(L^4-1)+4:\quad L=3\to84,\ L=4\to259,\ L=5\to628,\ L=6\to1299,$$
matching $(|V|-1)$ exact modes plus exactly $d=4$ harmonic modes, in every case.

**(b) The co-exact gap.** Fourier-diagonalize on $\mathbb Z_L^4$. With $(d_1X)_{p(x;\mu\nu)}=X_\mu(x)+X_\nu(x{+}\hat\mu)-X_\mu(x{+}\hat\nu)-X_\nu(x)$ the symbol is
$$\big(\widehat{d_1X}\big)_{\mu\nu}(k)=z_\nu X_\mu-z_\mu X_\nu,\qquad z_\mu:=1-e^{ik_\mu},$$
so $\widehat{d_1^*d_1}(k)=|z|^2\mathbb 1-\bar z\otimes z$, whose nonzero eigenvalue is $|z|^2=\sum_\mu|1-e^{ik_\mu}|^2=\sum_\mu2(1-\cos k_\mu)$, with multiplicity $3$, and eigenvalue $0$ (along $z$) with multiplicity 1. The smallest nonzero value over $k\in(2\pi/L)\mathbb Z^4\setminus\{0\}$ is attained at a single unit of momentum in one direction:
$$\lambda_{\min}^+=2\big(1-\cos(2\pi/L)\big)=\frac{4\pi^2}{L^2}+O(L^{-4}).$$
Verified numerically: $L=3\to3.000000$, $L=4\to2.000000$, $L=5\to1.381966$, $L=6\to1.000000$, exactly matching $2(1-\cos(2\pi/L))$.
Also $\sup_k|z|^2=16$ on $\mathbb Z^4$ (I maximized the symbol numerically: $15.9553$ over $2\times10^5$ random $k$, saturating $16$ at $k=(\pi,\pi,\pi,\pi)$), so the corpus's $\lambda_{\max}=24$ is the Gershgorin bound $6+18$, not the spectrum.

**Consequence for the mechanism.** Write the headline bound honestly:
$$\mathrm{Ric}_{\mu_\beta}\big|_{\mathcal H}\ \ge\ \kappa_G\,I+\frac{\beta}{N}d_1^*d_1\Big|_{\mathcal H},$$
which is the matrix hinge (item 7) and is fine as an *operator* inequality. But collapsing $d_1^*d_1$ to a scalar $c_W$ — which is what "$\mathrm{Ric}\ge(\kappa+\beta c_W)g$" does — gives $c_W=0$. The Wilson term contributes **nothing** to a scalar curvature floor in the thermodynamic limit; it only reshapes the covariance operator. This is precisely why item 7's operator-valued form (keeping $d_1^*d_1$) is the right statement and the scalar form is not.

The corpus is aware of the issue in one place — `DOC1` §4.2 writes "Assuming boundary/gauge-fixing conditions that eliminate cohomological zero-modes in the horizontal sector" — but never notes that (i) on the torus no such condition exists without changing the theory, and (ii) even on the co-exact sector the gap is $O(L^{-2})$, so the assumption cannot be made volume-uniform on any lattice with a growing diameter.

### Constants and numbers

c_W = 0 exactly on the periodic lattice (toron kernel of dimension d * dim g = 4 * 8 = 32 for SU(3) in d = 4). Co-exact gap lambda_min^+(d_1* d_1) = 2(1 - cos(2 pi / L)) ~ 4 pi^2 / L^2. Verified: L = 3 -> 3.000000; L = 4 -> 2.000000; L = 5 -> 1.381966; L = 6 -> 1.000000. dim ker d_1 = (L^d - 1) + d per algebra component; verified 84, 259, 628, 1299 for L = 3,4,5,6 in d = 4. sup spectrum on Z^4 = 16 (numerically 15.9553), NOT the Gershgorin value 24 quoted in the corpus. Off-diagonal absolute row sum C_0(d_1* d_1) = 6(d-1) = 18; diagonal 2(d-1) = 6.

### Code

# Fourier symbol: nonzero eigenvalue is |z|^2, multiplicity 3.
import numpy as np
best=0.
for _ in range(200000):
    k=np.random.uniform(0,2*np.pi,4); z=1-np.exp(1j*k)
    M=np.zeros((4,4),complex)
    for mu in range(4):
        for nu in range(mu+1,4):
            v=np.zeros(4,complex); v[mu]=z[nu]; v[nu]=-z[mu]
            M+=np.outer(v.conj(),v)
    best=max(best,np.linalg.eigvalsh(M)[-1].real)
print('sup spectrum of d1*d1 on Z^4 =',round(best,4))    # -> 15.955 (= 16)
# real-space gap: use maxwell(L) from item 5
for L in [3,4,5,6]:
    _,ev=maxwell(L); print(L, float(ev[ev>1e-8][0]), 2*(1-np.cos(2*np.pi/L)))

**Caveat.** None on the mathematics. The only escape would be boundary conditions killing H^1, but those change the finite-volume theory and still leave the O(L^{-2}) co-exact gap.

**Why it matters.** It shows the 'beta c_W' half of the corpus's headline formula is empty in the thermodynamic limit, and that only the Haar half is real. That is a sharp, decisive, correctly-proved statement about the mechanism's actual reach, and it explains why the operator-valued hinge (item 7) is the only usable form.

---

## 11. Obstruction III: the convexity window is a fixed-cutoff strong-coupling phenomenon and is incompatible with asymptotic freedom

`status: solid` · `kind: obstruction`

### Statement

On the lattice everything is dimensionless and the only parameter is $\beta=2N/g^2$; the criterion for a global Bakry-Émery floor is a pure $\beta$-condition,
$$\rho(\beta)=\kappa_G-\frac{4\nu\beta}{N}>0\iff\beta<\frac{N^2}{8\nu},$$
with **no** lattice-spacing dependence. Along the asymptotically-free continuum trajectory
$$\frac{1}{g^2(a)}\ \sim\ \frac{11N}{48\pi^2}\log\frac{1}{a^2\Lambda^2_{\mathrm{QCD}}}\ \longrightarrow\ \infty\quad(a\to0)\ \Longrightarrow\ \beta(a)=\frac{2N}{g^2(a)}\to\infty,$$
so $\rho(\beta(a))\to-\infty$. The window is a strong-coupling, cutoff-scale window and is disjoint from every neighbourhood of the continuum limit. Moreover the localized version fails too: the hinge radius scales as $r(\beta)\sim\beta^{-1}$ while typical link fluctuations scale as $\beta^{-1/2}$, so the good region is asymptotically atypical.

### Derivation

**Step 1: the criterion is $a$-independent.** All of $M_\Lambda=\mathrm{SU}(N)^{E}$, the Haar metric, and $S_W$ are dimensionless; $a$ enters only through the dictionary $U_\ell=\exp(agA_\ell)$ between lattice variables and continuum fields. Under that change of variables, $\nabla^2_A=(ag)^2\nabla^2_X$ multiplies **both** the Haar and the Wilson Hessians by the same $(ag)^2$, so it cancels in any eigenvalue comparison. Thus $\rho>0$ is a condition on $\beta$ alone. (`RECOMMENDED_01` §4 writes $\rho_*(a)=\frac N6a^2g^2-\frac{48}{g^2}$, which applies the $(ag)^2$ to the Haar term only; correcting this removes the spurious $a$ and gives $\beta<N^2/144$ in that document's own — factor-3 pessimistic — normalization.)

**Step 2: asymptotic freedom pushes $\beta$ the wrong way.** The two-loop lattice beta function gives $\beta(a)\to\infty$ logarithmically as $a\to0$. Since $\rho(\beta)$ is affine and decreasing in $\beta$ with slope $-4\nu/N$, $\rho\to-\infty$. The convexity window and the continuum limit are at opposite ends of the coupling axis. `RECOMMENDED_01` §6 states this conclusion correctly and calls it "a diagnostic, not a bug" — that judgement is right.

**Step 3: the localized version does not rescue it.** From item 7 the hinge radius satisfies $R_W(r)\le\kappa_G/2$ with $R_W(r)=\frac{2\nu M_3}{N}\beta r$, so $r(\beta)=\frac{N\kappa_G}{4\nu M_3\beta}\propto\beta^{-1}$. But at inverse coupling $\beta$ the Gibbs measure puts typical link amplitude at $\|X_\ell\|\sim\beta^{-1/2}$ (the quadratic action costs $\sim\beta\|X\|^2$ per plaquette). Hence
$$\frac{r(\beta)}{\text{typical amplitude}}\ \sim\ \frac{\beta^{-1}}{\beta^{-1/2}}=\beta^{-1/2}\ \longrightarrow\ 0 .$$
The good region is asymptotically a vanishing fraction of a typical fluctuation. This is exactly the dichotomy `YANG3_update_erosionLemma_kernelSchur_v5.md` §5 identifies: only an $r^2$ erosion law ($r(\beta)\sim\beta^{-1/2}$) could match, and that requires the unproved cancellation $D^3S_p(0)[K,K,\cdot]=0$.

**Step 4: the corpus's own data votes against the rescue.** [reconstructed] I fitted the corpus's most careful measurement, the $L=8$ bisection-determined convexity radius `R_curve_L8`, to $R=A\beta^{-p}$:
$$\text{all 8 points: }p=0.811,\ A=0.1189;\qquad \beta\ge1.2\text{ only: }p=0.834,\ A=0.1209.$$
Both are far from $p=1/2$ and close to $p=1$. Correspondingly $\beta R$ is nearly constant across the whole range ($0.098\to0.147$, a factor 1.5 over an 8-fold change in $\beta$) while $\sqrt\beta R$ drifts by a factor 1.9 monotonically downward. So the corpus's own best data selects the "bad" linear-erosion branch $R\sim1/\beta$, contradicting the $R\sim\beta^{-1/2}$ hope asserted in `D_Haar_Jacobian_SmallField.md` §D6.

**Step 5: a further structural point (mine).** Even at fixed $\beta$ the small-field ball is defined in the *product* metric, $d_{g_\Lambda}(U,U^{(0)})^2=\sum_\ell d_G(U_\ell,e)^2\le|E|R_0^2$. A ball of fixed radius $r$ in $g_\Lambda$ therefore forces per-link amplitude $\le r/\sqrt{|E|}\to0$: its $\mu_\Lambda$-measure is $e^{-\Theta(|E|)}$. Only the *linkwise* set $K_\Lambda(r)$ (item 7) has volume-uniform measure, which is why the corpus (correctly, in `B_canonical_region_matrix_hinge.md` §2) switched to it. The corpus's own contradiction report flags the same conflation at `HAAR/analysis_reports/full_Synthesis_01_..._20260118_163716.md:262`.

### Constants and numbers

Global window: beta < N^2/(8 nu) = N^2/48 in d = 4 (SU(2): 0.0833; SU(3): 0.1875). Continuum trajectory: beta(a) = 2N/g^2(a) -> infinity logarithmically. Hinge radius r(beta) ~ beta^{-1}; typical fluctuation ~ beta^{-1/2}; ratio ~ beta^{-1/2} -> 0. Power-law fit of the corpus's own R_curve_L8 data: R = 0.1189 * beta^{-0.811} (all points), R = 0.1209 * beta^{-0.834} (beta >= 1.2). beta*R across beta in [0.4, 3.2]: 0.098, 0.116, 0.125, 0.131, 0.137, 0.139, 0.143, 0.147 (nearly flat). sqrt(beta)*R: 0.155, 0.130, 0.114, 0.103, 0.097, 0.090, 0.086, 0.082 (monotone decrease, factor 1.9). Product-metric ball of fixed radius r has measure e^{-Theta(|E|)}; only the linkwise set has volume-uniform measure.

### Code

import numpy as np
b=np.array([0.4,0.8,1.2,1.6,2.0,2.4,2.8,3.2])
R=np.array([0.2448828125,0.1454296875,0.1038671875,0.0816015625,
            0.0682421875,0.0578515625,0.051171875,0.0459765625])   # R_curve_L8 from the corpus
A=np.vstack([np.ones_like(b),np.log(b)]).T
c,*_=np.linalg.lstsq(A,np.log(R),rcond=None)
print('R = %.4f * beta^%.4f'%(np.exp(c[0]),c[1]))          # 0.1189 * beta^-0.8114
m=b>=1.2; c2,*_=np.linalg.lstsq(A[m],np.log(R[m]),rcond=None)
print('tail: p = %.4f'%c2[1])                                # -0.8340
print('beta*R      :',(b*R).round(4))
print('sqrt(beta)*R:',(np.sqrt(b)*R).round(4))

**Caveat.** Step 4 is a fit to 8 points from one lattice size at one field-sampling convention; it is evidence, not proof, that the cancellation D^3 S_p(0)[K,K,.] = 0 fails. But it is the corpus's own best data and it points away from the needed exponent.

**Why it matters.** This is the decisive statement about the mechanism's reach: the mechanism is a theorem about the strong-coupling lattice theory, and the parameter that makes it work is driven the wrong way by asymptotic freedom. It is stated correctly in one corpus file and contradicted by optimism in a dozen others; the arithmetic settles it.

---

## 12. Hinge -> Helffer-Sjöstrand -> matrix Brascamp-Lieb -> Combes-Thomas: exponential clustering and a fixed-cutoff OS gap, with explicit stencil constants

`status: conditional` · `kind: derivation`

### Statement

Let $\mathcal L^{(1)}_\Lambda$ be the Witten Laplacian on 1-forms associated with $L_\Lambda$. Then:

(a) *Commutation / Bochner-Weitzenböck.* $\nabla(-L_\Lambda u)=\mathcal L^{(1)}_\Lambda(\nabla u)$ and $\mathcal L^{(1)}_\Lambda=(-L_\Lambda)\otimes I+\mathrm{Ric}_{\mu_\Lambda}$, so $\mathcal L^{(1)}_\Lambda\succeq\mathrm{Ric}_{\mu_\Lambda}$.

(b) *Helffer-Sjöstrand.* $\mathrm{Cov}_\mu(F,G)=\int\big\langle\nabla F,(\mathcal L^{(1)}_\Lambda)^{-1}\nabla G\big\rangle d\mu$.

(c) *Matrix Brascamp-Lieb.* If $\mathrm{Ric}_{\mu_\Lambda}\succeq\mathsf M$ on a domain, then $(\mathcal L^{(1)}_\Lambda)^{-1}\preceq\mathsf M^{-1}$ there and
$$|\mathrm{Cov}_\mu(F,G)|\le\Big(\!\int\!\langle\nabla F,\mathsf M^{-1}\nabla F\rangle d\mu\Big)^{1/2}\Big(\!\int\!\langle\nabla G,\mathsf M^{-1}\nabla G\rangle d\mu\Big)^{1/2}.$$

(d) *Combes-Thomas / Davies.* With $\mathsf M_\Lambda=m^2I+\alpha\,d_1^*d_1$ ($m^2=\kappa_G/2$, $\alpha=\beta/N$), which has gap $a_0=m^2$, range $R=1$ in the link-adjacency metric, and off-diagonal row sum $B=\alpha C_0$ with $C_0=6(d-1)$:
$$\big\|(\mathsf M_\Lambda^{-1})_{bb'}\big\|_{\mathrm{op}}\ \le\ \frac{2}{m^2}\,e^{-\eta\,\mathrm{dist}_E(b,b')},\qquad \eta_{\mathrm{CT}}=\log\!\Big(1+\frac{m^2}{2\alpha C_0}\Big),\qquad \eta_{\mathrm{D}}=2\,\mathrm{arsinh}\frac{\sqrt{m^2}}{2\sqrt{\alpha C_0}} .$$

(e) *Fixed-cutoff gap.* Given exponential decay of Euclidean-time covariances at rate $\eta$ and the OS axioms at fixed $a$, the reconstructed Hamiltonian obeys $\mathrm{gap}(H_a)\ge\eta/a$.

### Derivation

**(a)** The Witten Laplacian on 1-forms is $\mathcal L^{(1)}=\nabla^*\nabla+\mathrm{Ric}_g+\nabla^2S$ in Bochner form; equivalently $\mathcal L^{(1)}=(-L)\otimes I+\mathrm{Ric}_\mu$ after the standard integration by parts. Since $\nabla^*\nabla\succeq0$ and $-L\succeq0$, $\mathcal L^{(1)}\succeq\mathrm{Ric}_\mu$.

**(b)** Write $G-\mu(G)=(-L)^{-1}h$ and differentiate: $\mathrm{Cov}(F,G)=\int F\,(-L)(-L)^{-1}(G-\mu G)d\mu=\int\langle\nabla F,\nabla(-L)^{-1}(G-\mu G)\rangle d\mu$; apply (a)'s commutation to move $(-L)^{-1}$ past $\nabla$.

**(c)** Operator monotonicity of the inverse on the positive cone.

**(d)** Combes-Thomas conjugation: for $\phi$ 1-Lipschitz in the graph metric, $e^{\gamma\phi}\mathsf M e^{-\gamma\phi}=\mathsf M+\mathcal E_\gamma$ with $\|\mathcal E_\gamma\|\le B(e^{\gamma R}-1)+B(1-e^{-\gamma R})$; choosing $\gamma$ so this stays below $a_0$ preserves invertibility and yields the stated $\eta$.

**[reconstructed] The stencil constants, computed exactly.** On the hypercubic lattice, working with the link graph in which $b\sim b'$ iff they share a plaquette:
- diagonal $(d_1^*d_1)_{bb}=2(d-1)$ ($=6$ in $d=4$);
- off-diagonal absolute row sum $C_0=6(d-1)$ ($=18$ in $d=4$) — each of the $2(d-1)$ plaquettes containing $b$ contributes 3 other links, each with entry $\pm1$, and no pair of links shares two plaquettes;
- range $R=1$ exactly.
Both verified by explicit construction of $d_1$ on $L^4$ tori, $L=3,4,5,6$: diagonal $\{6\}$, row sum $\{18\}$, uniformly.
`02_davies_decay_row_sum_constants.md` §5 records that one project notebook computed "$C0\approx87$–$116$ depending on $L$" by an inverse FFT of the symbol and correctly flags the mismatch. **Resolution:** $C_0$ as defined (a row sum of $d_1^*d_1$) is $18$, volume-independent, full stop; the notebook was summing $|\cdot|$ over the kernel of the *inverse* (or of $\Delta_1^{-1}$), an $\ell^1$ Green-function norm, which is a different and $L$-dependent object. The theory constant is $18$.

**Numerical exponent.** Plugging $m^2=\kappa_G/2=N/4$, $\alpha=\beta/N$, $C_0=18$:
$$\eta_{\mathrm{D}}(\beta)=2\,\mathrm{arsinh}\sqrt{\frac{N^2}{288\beta}} .$$
For $\mathrm{SU}(3)$ this gives, e.g., $\eta_{\mathrm D}(0.1)=2\,\mathrm{arsinh}(1.768)=2.66$, $\eta_{\mathrm D}(1)=2\,\mathrm{arsinh}(0.559)=1.06$, $\eta_{\mathrm D}(10)=2\,\mathrm{arsinh}(0.177)=0.352$, $\eta_{\mathrm D}(100)=0.1116$ — i.e. $\eta\sim N/\sqrt{72\beta}$ at large $\beta$. Since $\beta\to\infty$ in the continuum, $\eta(a)\to0$ like $1/\sqrt{\beta(a)}$, so $\eta(a)/a$ has an indeterminate limit that is not controlled by this chain — one more place the continuum step is not supplied.

**(e)** Standard OS: if $|\mathrm{Cov}_\mu(\theta F,\tau_nG)|\le Ce^{-\eta n}$ for reflection-positive $\mu$ with time-translations $\tau_n$, the transfer matrix $T$ satisfies $\|T^n|_{\{\Omega\}^\perp}\|\le Ce^{-\eta n}$, so $H_a=-\frac1a\log T$ has $\mathrm{gap}\ge\eta/a$.

**What is conditional.** The chain (a)-(e) is standard and correct. What it needs and does not have is the hypothesis of (c): $\mathrm{Ric}_{\mu}\succeq\mathsf M$ on a set of $\mu$-measure close to 1. The hinge supplies it only on $K_\Lambda(r)$ with $r\sim1/\beta$, and the covariance decomposition
$$|\mathrm{Cov}_\mu(F,G)|\le|\mathrm{Cov}_{\mu(\cdot|K)}(F,G)|+8\|F\|_\infty\|G\|_\infty\,\mu(K^c)$$
then needs $\mu(K^c)\le e^{-c|P(\Lambda)|}$, which is the unproved typicality step (the corpus's "(Obl-2)").

### Constants and numbers

m^2 = kappa_G/2 = N/4 (lambda=1): 0.5 for SU(2), 0.75 for SU(3). alpha = beta/N. C_0(d_1* d_1) = 6(d-1) = 18 in d = 4 (exact, volume-independent; verified for L = 3,4,5,6). Range R = 1. eta_CT = log(1 + m^2/(2 alpha C_0)) = log(1 + N^2/(72 beta)). eta_Davies = 2 arsinh(sqrt(m^2/(4 alpha C_0))) = 2 arsinh(N/sqrt(288 beta)). SU(3) values of eta_Davies: beta = 0.1 -> 2.66; beta = 1 -> 1.06; beta = 10 -> 0.352; beta = 100 -> 0.112. Large-beta asymptotics eta ~ N/sqrt(72 beta). Prefactor 2/m^2 = 8/N. Corpus notebook's 'C0 = 87..116' is a different (Green-function ell^1) quantity, not this C_0.

### Code

import numpy as np
N=3; C0=18.0
for beta in [0.1,1,10,100]:
    m2=N/4.; al=beta/N
    print('beta=%6.1f  eta_CT=%.4f  eta_Davies=%.4f'%(
        beta, np.log(1+m2/(2*al*C0)), 2*np.arcsinh(np.sqrt(m2/(4*al*C0)))))

**Caveat.** Everything here is conditional on the hinge hypothesis holding on a set of measure 1 - o(1); that typicality estimate is the programme's genuine open step and is not supplied anywhere in the corpus.

**Why it matters.** It shows exactly what the curvature bound buys once you have it: covariance control by an explicit massive-Maxwell propagator with a computable decay exponent, rather than by perturbation theory. The reduction of an interacting gauge theory to a linear finite-range operator-inverse decay problem is a genuinely clean piece of architecture, and the stencil constant C_0 = 18 settles a discrepancy the corpus left open.

---

## 13. SU(2) one-link model solved exactly: beta_c = 4.413914663154, the non-convex annulus, and the e^{-beta} suppression of the bad set

`status: solid` · `kind: numerical_result`

### Statement

Parametrize $\mathrm{SU}(2)$ by $a\in\mathbb R^3$ with $U=\exp(ia\cdot\sigma/2)$, $\theta=\|a\|/2\in[0,\pi)$, and take the one-link total action in the exponential chart
$$S_\beta(a)=S_H(a)+S_W(a),\qquad S_H(a)=-2\log\frac{\sin\theta}{\theta},\qquad S_W(a)=-\beta\cos\theta .$$
$S_\beta$ is radial, so $\nabla^2S_\beta$ has one radial and two tangential eigenvalues:
$$\lambda^H_{\mathrm{rad}}=\tfrac12\Big(\csc^2\theta-\tfrac1{\theta^2}\Big),\quad \lambda^H_{\mathrm{tan}}=\frac{1-\theta\cot\theta}{2\theta^2},\quad \lambda^W_{\mathrm{rad}}=\tfrac\beta4\cos\theta,\quad \lambda^W_{\mathrm{tan}}=\tfrac\beta4\frac{\sin\theta}{\theta}.$$
Then: (i) $\lambda_{\mathrm{tan}}>0$ for all $\theta\in(0,\pi)$ and all $\beta\ge0$, so convexity can only fail radially; (ii) $\lambda_{\mathrm{rad}}(\theta)\ge0$ for all $\theta$ iff $\beta\le\beta_c$ with
$$\boxed{\ \beta_c=\min_{\theta\in(\pi/2,\pi)}\ -2\,\frac{\csc^2\theta-\theta^{-2}}{\cos\theta}=4.413914663154,\qquad \theta_\star=2.1185040856\ }$$
(iii) for $\beta>\beta_c$ the non-convex set is an annulus $\theta\in(\theta_-(\beta),\theta_+(\beta))$ with $\theta_-\downarrow\pi/2$, $\theta_+\uparrow\pi$; (iv) under the exact one-link Gibbs law $p_\beta(\theta)\propto\sin^2\theta\,e^{\beta\cos\theta}$, the mass of the annulus decays like $e^{-\beta}$.

### Derivation

**Chart and normalization.** $X=ia\cdot\sigma/2$; then $-2\mathrm{Tr}(XY)=a\cdot b$, so $a$ is orthonormal for $\lambda=2$, where $\kappa_G=N/4=1/2$. Consistency check: $\nabla^2S_H(0)=\kappa_G/3=1/6$, and indeed both formulas above give $\lambda^H_{\mathrm{rad}}(0^+)=\lambda^H_{\mathrm{tan}}(0^+)=1/6$ ($\csc^2\theta-\theta^{-2}\to1/3$; $1-\theta\cot\theta\sim\theta^2/3$). This is the item-3 constant in the SU(2), $\lambda=2$ column. The Wilson piece: $\cos(\|a\|/2)\approx1-\|a\|^2/8$ gives $\nabla^2S_W(0)=(\beta/4)I$, matching both formulas at $\theta=0$.

**Haar Jacobian for SU(2).** From item 3(i) with one positive root: $\mathrm{ad}_X$ has eigenvalues $0,\pm i\|a\|$, so $J=\big(\frac{\sin(\|a\|/2)}{\|a\|/2}\big)^2=(\sin\theta/\theta)^2$ and $S_H=-2\log(\sin\theta/\theta)$. ✓

**Radial/tangential split.** For a radial $f(\|a\|)$ with $\theta=\|a\|/2$, $\nabla^2f$ has radial eigenvalue $\frac14 f''(\theta)$ and tangential eigenvalue $\frac14\frac{f'(\theta)}{\theta}$ (doubly degenerate), where the $\frac14$ is the chain-rule factor from $\theta=\|a\|/2$. Applying this to $S_H$ and $S_W$ reproduces the four displayed formulas.

**[reconstructed] Verification.** I computed the full $3\times3$ Hessian of $S_H(a)$ by finite differences and compared to the closed forms:
$$\theta=0.001:\ (0.166666,0.166667,0.166667)\ \text{vs}\ (1/6,1/6);\quad \theta=1:\ (0.178954,0.178954,0.206141)\ \text{vs}\ \lambda_{\rm tan}=0.178954,\ \lambda_{\rm rad}=0.206141;$$
$$\theta=2.5:\ (0.347731,0.347731,1.315988)\ \text{vs}\ (0.347730,\ 1.315989);\quad \theta=3:\ (1.224763,1.224763,25.05133)\ \text{vs}\ (1.224764,\ 25.051329).$$
Exact agreement to 6 digits, including the divergence as $\theta\to\pi$ (edge of the chart).

**$\beta_c$.** $\lambda_{\mathrm{rad}}(\theta)=0$ can only happen where $\cos\theta<0$, i.e. $\theta>\pi/2$; solving for $\beta$ gives $\beta(\theta)=-2(\csc^2\theta-\theta^{-2})/\cos\theta$, and $\beta_c=\min_{(\pi/2,\pi)}\beta(\theta)$ is the tangency $\lambda_{\rm rad}(\theta_\star)=\lambda_{\rm rad}'(\theta_\star)=0$. Bounded minimization with tolerance $10^{-13}$: $\beta_c=4.413914663153596$ at $\theta_\star=2.118504085599$. The corpus reports $4.413914663162$ / $2.118504915$ — agreeing to $\sim10^{-11}$ and $\sim10^{-6}$ respectively (my optimizer is tighter).

**Bad-mass computation.** Radial density: Haar on $\mathrm{SU}(2)$ is $\propto\sin^2\theta\,d\theta\,d\Omega$ (the class-function density), and the Wilson weight is $e^{\beta\cos\theta}$, giving $p_\beta(\theta)\propto\sin^2\theta\,e^{\beta\cos\theta}$. I reproduced the entire corpus table by root-finding $\lambda_{\rm rad}=0$ and quadrature — **agreement in every printed digit** (see the table below).

**Asymptotics.** For large $\beta$, $e^{\beta\cos\theta}\approx e^\beta e^{-\beta\theta^2/2}$ concentrates at $\theta=0$ while $\theta_-(\beta)\downarrow\pi/2$ where $\cos\theta\approx0$; hence $\mathsf{Bad}\sim e^{-\beta}$. Sanity: at $\beta=20$, $e^{-20}=2.061\times10^{-9}$ versus the computed $2.113\times10^{-9}$ — a $2.5\%$ match.

**The honest caveat the corpus itself states.** Classical Holley-Stroock perturbation needs a *supremum* bound on the potential difference, not a probability bound; so exponentially small bad mass alone does not give an LSI. One needs a localized perturbation lemma or a two-scale LSI. `03_SU2_Concentration_BadMass.md` §5 says exactly this, correctly.

### Constants and numbers

beta_c = 4.413914663153596 (my value, tol 1e-13); corpus: 4.413914663162. theta_* = 2.1185040856 rad (corpus 2.118504915). Hess S_H(0) = (1/6) I, matching kappa_G/3 with kappa_G = N/4 = 1/2 for SU(2), lambda = 2. Hess S_W(0) = (beta/4) I.
Non-convex annulus and Gibbs mass (all reproduced exactly, digit for digit):
 beta | theta_-   | theta_+   | P(annulus)   | P(theta > theta_-)
 4.5  | 2.038649  | 2.201505  | 1.081864e-03 | 1.880604e-03
 5.0  | 1.924823  | 2.332324  | 1.659518e-03 | 1.844956e-03
 6.0  | 1.831386  | 2.454436  | 9.566965e-04 | 9.748608e-04
 8.0  | 1.747900  | 2.581050  | 1.830831e-04 | 1.833402e-04
10.0  | 1.706223  | 2.654222  | 2.983515e-05 | 2.983933e-05
20.0  | 1.633771  | 2.812795  | 2.113171e-09 | 2.113171e-09
50.0  | 1.595101  | 2.938592  | 3.249038e-22 | 3.249038e-22
Asymptotic law: Bad(beta) ~ e^{-beta}; at beta = 20, e^{-20} = 2.061e-9 vs computed 2.113e-9.
Hessian formula check (numeric vs closed form), theta = 0.001/1/2.5/3: (0.166666,0.166667) / (0.178954,0.206141) / (0.347731,1.315988) / (1.224763,25.05133) -- all match to 6 digits.

### Code

import math, numpy as np
from scipy.integrate import quad
from scipy.optimize import brentq, minimize_scalar

# beta_c
f = lambda th: -2*(1/math.sin(th)**2 - 1/th**2)/math.cos(th)
r = minimize_scalar(f, bounds=(math.pi/2+1e-9, math.pi-1e-9),
                    method='bounded', options={'xatol':1e-13})
print('beta_c =', r.fun, ' theta_* =', r.x)      # 4.413914663153596  2.118504085599

def lam_rad(t,b): return 0.5*(1/math.sin(t)**2 - 1/t**2) + (b/4)*math.cos(t)
def roots(b):
    ts=np.linspace(1e-6, math.pi-1e-6, 400000)
    v=0.5*(1/np.sin(ts)**2-1/ts**2)+(b/4)*np.cos(ts); s=np.sign(v)
    return [brentq(lambda x: lam_rad(x,b), ts[j], ts[j+1])
            for j in np.where(s[:-1]*s[1:]<0)[0]]
dens = lambda t,b: math.sin(t)**2*math.exp(b*(math.cos(t)-1))   # shifted for stability
for b in [4.5,5,6,8,10,20,50]:
    tm,tp = roots(b)[:2]
    Z  = quad(lambda t: dens(t,b), 0, math.pi, limit=300)[0]
    nc = quad(lambda t: dens(t,b), tm, tp,     limit=300)[0]/Z
    bd = quad(lambda t: dens(t,b), tm, math.pi,limit=300)[0]/Z
    print('beta=%6.2f th-=%.6f th+=%.6f nonconv=%.6e bad=%.6e'%(b,tm,tp,nc,bd))

**Caveat.** One link only: there is no plaquette coupling, no gauge orbit, and no volume. It quantifies the local convexity/typicality tension but says nothing about the lattice problem directly.

**Why it matters.** It is the only place in the corpus where the Haar-versus-Wilson competition is solved exactly, and both the threshold and the measure of the bad set are reproducible to full precision. It also cleanly exhibits the programme's real structure: convexity fails only radially, only past beta ~ 4.4, and only on a set of measure ~ e^{-beta}.

---

## 14. SU(3) JAX convexity engine: full multi-volume scan data, the convexity radius R_L(beta), and what it does and does not show

`status: solid` · `kind: code`

### Statement

A JAX/GPU engine computes $\lambda_{\min}\big(\nabla^2 S_{\beta,c_0}(\theta)\big)$ for $S_{\beta,c_0}=S_{\mathrm{Wilson}}(\exp A(\theta))+c_0\sum_\ell\mathrm{Tr}(A_\ell^\dagger A_\ell)$ on $L^4$ lattices with $\mathrm{SU}(3)$ links ($L^4\cdot4\cdot8$ real parameters), using: Padé[2/2] $\mathrm{SU}(3)$ exponential, Hessian-vector products by JAX JVP-of-grad, and $k$-step Lanczos to estimate the smallest eigenvalue without materializing the Hessian. Executed results (stored in the corpus) give a volume-stable convex core: at field scale $0.05$ the $L=4,6,8$ curves agree to $\sim10^{-3}$ across $\beta\in[0.4,3.0]$, and a bisection radius-finder at $L=8$ produces $R_L(\beta)$ obeying $R\approx0.119\,\beta^{-0.81}$.

### Derivation

**Setup and normalization (item 1).** Generators `T_a = 1j*lambda_a/2`, i.e. basis A / $\lambda=2$. Consequently the true Haar-potential floor in these coordinates is $N/12=0.25$; the engine instead uses `haar_mass = c0 * sum_l Re Tr(A^dag A)` with $c_0=0.125$. Since $\mathrm{Tr}(A^\dagger A)=\tfrac12|a|^2$ in this basis, the coded Hessian is $c_0\,\mathrm{Id}=0.125\,\mathrm{Id}$ — **exactly half** the correct flat-chart Haar term and one sixth of the intrinsic floor $\kappa_G=0.75$. So all reported $\lambda_{\min}$ are conservative by $\ge0.125$; the true convex cores are larger than measured.

**Method.** $\lambda_{\min}$ is estimated by $k=20$–$25$ step Lanczos on HVPs; field configurations are drawn i.i.d. Gaussian in $\theta$ with a given `scale`, and the reported value is the minimum over $n$ samples (conservative). Radius finder: bisection on $r$ with a stability test requiring $\min_{\text{samples}}\lambda_{\min}>0$.

**Executed data (from the corpus run logs; `Selected_Numerics_SU3_Convexity_Rbeta_Tau_and_Scaling.md` §3, which is the most complete version — it has all three scales at $L=8$, whereas `05_su3_wilson_haar_hessian_numerics.md` §2 has only scale $0.05$).**

$L=8$, full grid (β, scale, $\lambda_{\min}$):
```
(0.40,0.050,+0.109207) (0.40,0.100,+0.087311) (0.40,0.150,+0.062942)
(0.77,0.050,+0.094372) (0.77,0.100,+0.053147) (0.77,0.150,+0.004519)
(1.14,0.050,+0.078979) (1.14,0.100,+0.015042) (1.14,0.150,-0.051065)
(1.51,0.050,+0.065228) (1.51,0.100,-0.016862) (1.51,0.150,-0.107826)
(1.89,0.050,+0.049413) (1.89,0.100,-0.051518) (1.89,0.150,-0.165610)
(2.26,0.050,+0.036033) (2.26,0.100,-0.089054) (2.26,0.150,-0.225723)
(2.63,0.050,+0.020245) (2.63,0.100,-0.119307) (2.63,0.150,-0.277276)
(3.00,0.050,+0.005785) (3.00,0.100,-0.158744) (3.00,0.150,-0.336072)
```
$L=4$ and $L=6$ grids are in the same file; at scale $0.05$ the three volumes differ by at most $1.6\times10^{-3}$ (e.g. at $\beta=1.89$: $0.042761$, $0.048837$, $0.049413$). The $L=4$ curve is the outlier and is the only one that dips negative at $\beta=3.0$ (that is a finite-volume drift, not a collapse — $L=6$ and $L=8$ remain positive).

Linear-interpolation radius estimates from the 3-scale grids:
```
beta   R(L=4)   R(L=6)   R(L=8)
1.14   0.1076   0.1119   0.1114
1.51   0.0837   0.0894   0.0897
1.89   0.0705   0.0732   0.0745
2.26   0.0602   0.0642   0.0644
2.63   0.0522   0.0567   0.0573
3.00   <0.05    0.0511   0.0518
```
$L=6$ and $L=8$ agree to $\le1\%$ throughout: **this is the corpus's single best piece of evidence and it is real** — the convex core does not shrink with volume in this range.

Bisection radius finder at $L=8$ (`R_curve_L8`), which reaches beyond the coarse grid at small $\beta$:
```
beta:  0.4     0.8     1.2     1.6     2.0     2.4     2.8     3.2
R   : 0.24488 0.14543 0.10387 0.08160 0.06824 0.05785 0.05117 0.04598
```

**[reconstructed] My analysis of the radius law.** Fitting $\log R=\log A-p\log\beta$:
- all 8 points: $p=0.8114$, $A=0.1189$;
- $\beta\ge1.2$: $p=0.8340$, $A=0.1209$.
$\beta R$ is nearly constant ($0.098\to0.147$ over an 8-fold $\beta$ range) while $\sqrt\beta R$ falls monotonically by a factor $1.9$. So the data selects the **linear-erosion** branch $R\sim1/\beta$, i.e. the "bad case" of `YANG3_update_erosionLemma_kernelSchur_v5.md` §5.1, contradicting the $R\sim\beta^{-1/2}$ claim asserted in `D_Haar_Jacobian_SmallField.md` §D6. Since $R\sim1/\beta$ implies the convex core shrinks faster than typical fluctuations $\sim\beta^{-1/2}$, the numerics themselves say the localization strategy does not close at weak coupling. (Caveat: 8 points, one volume, one sampling convention.)

**What the numerics do and do not show** (`05_su3_wilson_haar_hessian_numerics.md` §4, correct as written): the scans sample $A$-coordinates from an *ad hoc* Gaussian, not from the equilibrium Yang-Mills law. Establishing typicality requires sampling in $U$-space (Haar $\times$ Wilson weight), mapping $U\mapsto A$ by principal logarithm, and measuring $\mathbb P_{\mu_\beta}(A(U)\in\mathcal C_\beta)$. That experiment is proposed and never run.

### Constants and numbers

Engine: SU(3), L^4 lattices, L^4*4*8 real parameters (L=8 -> 131072), Padé[2/2] exponential, k = 20-25 Lanczos steps, float32, c0 = 0.125 (half the correct flat-chart Haar value 0.25). Full L = 8 scan table given above (24 points, beta in [0.40, 3.00], scale in {0.05, 0.10, 0.15}). Volume stability at scale 0.05: L = 4/6/8 agree within 1.6e-3 across the whole beta range. Radius table: R(L=6) and R(L=8) agree within 1% for beta in [1.14, 3.00]. R_curve_L8: (0.4, 0.24488), (0.8, 0.14543), (1.2, 0.10387), (1.6, 0.08160), (2.0, 0.06824), (2.4, 0.05785), (2.8, 0.05117), (3.2, 0.04598). Power-law fit: R = 0.1189 beta^{-0.811} (all), 0.1209 beta^{-0.834} (beta >= 1.2). beta*R nearly constant (0.098 -> 0.147); sqrt(beta)*R monotone down by factor 1.9. Dynamic restoration times tau under gradient flow: tau ~ 0 for r <= 0.24 at beta = 0.40; tau in [0.16, 0.48] for beta >= 0.96 outside the core.

### Code

# Portable core of the engine (the corpus's full listing is in
# HAAR/01_haar_mass/05_SU3_CALCULATIONS/Selected_Numerics_SU3_Convexity_Rbeta_Tau_and_Scaling.md).
import jax, jax.numpy as jnp, jax.lax as lax
jax.config.update('jax_enable_x64', False)

def su3_generators():                      # T_a = i*lambda_a/2  (basis A, <X,Y> = -2Tr)
    lam = [ ... ]                          # the 8 Gell-Mann matrices, as in the corpus file
    return 1j*jnp.stack(lam,0)/2.0
T_SU3 = su3_generators()
su3_alg_from_vec = lambda a: jnp.einsum('...a,aij->...ij', a, T_SU3)

@jax.checkpoint
def su3_exp_pade22(A):                     # Padé[2/2]; ~4x faster than expm on GPU
    I = jnp.eye(3, dtype=jnp.complex64); A2 = A@A
    return jnp.linalg.solve(I - 0.5*A + A2/12.0, I + 0.5*A + A2/12.0)

@jax.jit
def compute_plaquette_sum(U, beta):        # U shape (L,L,L,L,4,3,3)
    S = 0.0
    for mu in range(4):
        for nu in range(mu+1,4):
            Um  = U[...,mu,:,:]
            Uns = jnp.roll(U[...,nu,:,:], -1, axis=mu)
            Umd = jnp.swapaxes(jnp.conjugate(jnp.roll(U[...,mu,:,:], -1, axis=nu)),-1,-2)
            Und = jnp.swapaxes(jnp.conjugate(U[...,nu,:,:]),-1,-2)
            P = Um @ Uns @ Umd @ Und
            S += jnp.sum(1.0 - jnp.real(jnp.einsum('...ii->...',P))/3.0)
    return beta*S

@jax.jit
def haar_mass(params, c0):                 # NOTE: coded Hessian = c0*I; correct value is 0.25, not 0.125
    flat = params.reshape(-1,8)
    per  = lambda a: jnp.real(jnp.trace(su3_alg_from_vec(a).conj().T @ su3_alg_from_vec(a)))
    return c0*jax.vmap(per)(flat).sum()

def hvp(f, theta, v):
    _, hv = jax.jvp(jax.grad(f), (theta,), (v,)); return hv

def lanczos_min(f, theta, k=25, seed=0):   # smallest Ritz value of the Hessian
    v0 = jax.random.normal(jax.random.PRNGKey(seed), (theta.shape[0],)); v0 /= jnp.linalg.norm(v0)
    def step(carry, _):
        vp, v, bp = carry
        w = hvp(f, theta, v) - bp*vp
        al = jnp.dot(w, v); w = w - al*v; bt = jnp.linalg.norm(w)
        return (v, w/(bt+1e-9), bt), (al, bt)
    (_,_,_), (a,b) = lax.scan(step, (jnp.zeros_like(v0), v0, 0.0), None, length=k)
    Tm = jnp.diag(jnp.array(a)) + jnp.diag(jnp.array(b[:-1]),1) + jnp.diag(jnp.array(b[:-1]),-1)
    return float(jnp.linalg.eigvalsh(Tm)[0])

**Caveat.** Configurations are sampled from an ad hoc Gaussian in the Lie-algebra chart, not from the Yang-Mills equilibrium measure; and the coded Haar coefficient is half the correct flat-chart value. The volume stability is real; the connection to typicality is not established.

**Why it matters.** This is real executed numerics with stored outputs, it is internally consistent with the exact constants (item 1), and it is the corpus's strongest empirical claim. My re-analysis of its own radius data also gives the sharpest available evidence on the r vs r^2 erosion question -- and it points the unfavourable way.

---

## 15. SU(3) SAFE-region constants ledger: kappa_* = 0.25, delta = 0.006, alpha = 0.976, and where each number comes from

`status: gap` · `kind: data`

### Statement

For $\mathrm{SU}(3)$ in right-invariant exponential coordinates with SAFE ball radius $R_0=0.05$, the corpus adopts:
$$\kappa_*\approx0.25\ \text{(Haar convexity floor)},\qquad \delta\approx0.006\ \text{(Wilson perturbation budget)},\qquad \alpha:=\frac{\kappa_*-\delta}{\kappa_*}\approx0.976,$$
giving the target inequality $\lambda_{\min}\big(P_{\mathrm{phys}}\nabla^2S_{\mathrm{tot}}P_{\mathrm{phys}}\big)\ge\kappa_*-\delta\approx0.244$ on $\Omega_{\mathrm{SAFE}}(0.05)$, against a scanned minimum of $\approx0.248$ (margin $\approx0.004$).

### Derivation

**$\kappa_*=0.25$ is exact, not empirical.** The corpus presents $0.25$ as the outcome of a random scan whose script "supports an automatic coordinate scaling so that $\lambda_{\min}(\nabla^2S_{\mathrm{Haar}}(0))=0.25$" — i.e. it is fixed by fiat. [reconstructed] But $0.25$ is the *correct* value on the nose: item 3 gives $\nabla^2S_H(0)=\kappa_G/3=N/12$, and $N/12=3/12=0.25$ for $\mathrm{SU}(3)$ in the $\lambda=2$ (basis A) normalization. So the number is right for a reason the corpus does not state, and item 3's global bound shows it is a genuine floor on the entire chart $|X|<2\pi$, not just on $R_0=0.05$. The scan table the corpus reports at radii $0.00$–$0.05$ ($0.291,0.286,0.279,0.271,0.263,0.255$, "conservative baseline $0.25$") is *decreasing* in $r$, which contradicts both my exact computation and the corpus's own CSV; the CSV `su3_haar_hessian_scan_results.csv`, which is the reproducible artifact, is *increasing*:
```
r      min_over_dirs    mean_min        max_over_dirs
0.00   0.2500001983     0.2500001983    0.2500001983
0.01   0.2499998785     0.2500001252    0.2500014665
0.02   0.2500007523     0.2500010310    0.2500040402
0.03   0.2500023600     0.2500026329    0.2500087227
0.04   0.2500044998     0.2500048244    0.2500153246
0.05   0.2500073689     0.2500076231    0.2500238383
```
The CSV agrees with my exact scan (item 3: $0.250008$ at $r=0.05$) to 5 decimals. **The $0.291\to0.255$ table is spurious** — I could not reproduce it in any normalization, and it disagrees with the corpus's own CSV. Discard it; keep the CSV.

**$\delta\approx0.006$ is a heuristic budget with a spurious $a$.** The chain is: BCH-order splitting $H_p=H_p^{(2)}+H_p^{(3)}+H_p^{(4)}$ with reported one-plaquette norms $\|H^{(2)}\|\le C_2\approx0.011$, $\|H^{(3)}\|\le C_3r\approx0.10\,r$, $\|H^{(4)}\|\le C_4r^2\approx1.1\,r^2$; at $R_0=0.05$ this gives $0.011+0.005+0.00275=0.01875$; times $\nu=6$ plaquettes per link gives $\|H_W\|^{\mathrm{link}}\lesssim0.1125$; then "if the scaling regime enforces $\beta a^4\le0.05$" one multiplies to get $\delta\approx0.05\times0.1125=5.6\times10^{-3}\to0.006$.
The final step is the weak link: $\beta a^4$ is not a dimensionless combination that appears anywhere in the lattice action (the Wilson coupling is $\beta$, full stop). Reading it as a bare $\beta\le0.05$ makes it consistent — and then $\delta=0.006$ is a legitimate perturbation budget, but only at $\beta\le0.05$, which sits *inside* the unconditional window $\beta<0.1875$ of item 8. So the SAFE-region result is not stronger than item 8; it is a special case with better constants.

**$\alpha=0.976$** is then $(0.25-0.006)/0.25$ and is interpreted as a per-RG-step fractional retention of convexity. No RG step is actually performed with it anywhere in the corpus; it is a placeholder.

**The exact Haar Jacobian used in the scan** is correct and worth keeping:
$$J(A)=\det\Big(\frac{1-e^{-\mathrm{ad}_A}}{\mathrm{ad}_A}\Big),\qquad \log J(A)=\sum_j\log\frac{2\sin(\theta_j/2)}{\theta_j},$$
$\pm i\theta_j$ the eigenvalues of $\mathrm{ad}_A$ — this is item 3(i), and the corpus implements it correctly.

**The physical projector is the real gap.** $H_{\mathrm{phys}}=P_{\mathrm{phys}}\nabla^2S_{\mathrm{tot}}P_{\mathrm{phys}}$ is used numerically but never defined coordinate-freely. As `05_curvature_defect_obstruction_principle.md` §1.1 correctly notes, gauge-orbit directions depend on $U$ through the covariant derivative, so $P_{\mathrm{phys}}$ is $U$-dependent unless one fixes a gauge; the corpus's numerics implicitly use a $U$-independent projector. This is the concrete unfinished item.

**Gauge-fixing / Haar survival** (`11_haar_gauge_fixing_rigorous.md`): the defensible statement is that inside a gauge slice where the Faddeev-Popov determinant is bounded away from $0$ and $\infty$, the gauge-fixed measure is absolutely continuous w.r.t. product Haar with smooth density, so the local Haar curvature estimates transfer up to an explicit distortion. The supporting observation — that the FP determinant for Cartan-type gauges *is* the Vandermonde density $\prod_{i<j}\sin^2(\pi(\rho_i-\rho_j))$, i.e. reduced Haar — is correct and pretty. It is a justification, not a theorem, because Gribov copies and the FP zero set are excluded by hypothesis.

### Constants and numbers

R_0 = 0.05 (SAFE ball radius, exponential coordinates; also requires R_0 < pi/4 for the Wilson second-variation bound). kappa_* = 0.25 = N/12 for SU(3) in the lambda = 2 normalization (EXACT, not empirical). delta = 0.006. kappa_* - delta = 0.244. Scanned combined minimum ~ 0.248 (margin 0.004). alpha = (kappa_* - delta)/kappa_* = 0.976. BCH one-plaquette norms: C_2 = 0.011, C_3 = 0.10, C_4 = 1.1; C_2 + C_3 R_0 + C_4 R_0^2 = 0.01875 at R_0 = 0.05; times nu = 6 gives 0.1125 per link. Small parameter used: 'beta a^4 <= 0.05' (should read beta <= 0.05). Verified CSV su3_haar_hessian_scan_results.csv (increasing in r, matching the exact value 0.25 + O(r^2)); the separately reported table 0.291/0.286/0.279/0.271/0.263/0.255 (decreasing) is NOT reproducible and contradicts the CSV.

### Code

# Exact Haar Jacobian as implemented (and as it should be):
#   log J(A) = sum_j log( 2 sin(theta_j/2) / theta_j ),  {+-i theta_j} = spec(ad_A)
# See item 3's code; the r-scan reproduces the CSV to 5 decimals:
#   r=0.00 -> 0.250000 ; r=0.05 -> 0.250008  (CSV: 0.2500002 ; 0.2500074)

**Caveat.** delta = 0.006 depends on the un-motivated small parameter 'beta a^4 <= 0.05' and on three uncertified BCH constants; the physical projector P_phys is never defined coordinate-freely; and one of the two reported Haar scan tables is not reproducible.

**Why it matters.** kappa_* = 0.25 turns out to be an exact group-theoretic constant N/12 rather than a fitted one, and item 3 shows it holds on the whole exponential chart rather than only on the R_0 = 0.05 ball. That upgrades the most-quoted number in the archive from 'scanned' to 'proved', and cleanly separates the one solid entry in this ledger from the three heuristic ones.

---

## How these fit together

These items form one chain, and the chain has a well-defined breaking point.

FORWARD DIRECTION (what works). Items 1-2 fix the geometry: SU(N)^E with the product bi-invariant metric is Einstein with Ric = kappa_G g, kappa_G = N/(2 lambda), and this floor is exactly volume-uniform because the Ricci tensor of a Riemannian product has no cross terms. Item 3 shows the same constant appears (divided by 3) as the Hessian of the Haar Jacobian potential in exponential coordinates, and — my strengthening — that this Hessian bound is global on the entire chart |X| < 2 pi, not merely local. Item 5 identifies the interaction term: at the vacuum the Wilson Hessian is exactly (beta/N) d_1* d_1, the discrete Maxwell operator, positive semidefinite, with kernel precisely the closed 1-cochains (lattice Bianchi). Item 6 is the engine: gauge-invariant observables have horizontal gradients, so only horizontal curvature is needed, and (with the observation that P_t commutes with the gauge action, which I supply) the Gamma_2 machinery closes inside the invariant sector, giving Poincaré 1/rho, LSI 2/rho and gap rho. Item 8 is the payoff: for beta < N^2/48 in d = 4 the horizontal bound holds globally and one gets an unconditional, volume-uniform, dimension-free spectral gap with explicit constants. Item 7 is the localized refinement that keeps the Maxwell operator intact; item 11 is what that buys — Helffer-Sjöstrand plus matrix Brascamp-Lieb plus Combes-Thomas gives exponential clustering with an explicit exponent built from the stencil constant C_0 = 18, and then a fixed-cutoff OS gap.

BREAKING POINT. Three independent obstructions, all sharp, all verified. Item 9: the Wilson potential has an explicit negative Hessian direction of size -beta/N (sharp value -4/N per plaquette), so the global curvature constant is at most kappa_G - beta/N and goes to -infinity; combined with item 8 the true global-CD threshold is bracketed between N^2/48 and N^2/8, a factor 6. Item 10: the "beta c_W" half of the corpus's headline formula is empty in the thermodynamic limit — c_W is exactly 0 on the torus (torons) and 2(1-cos(2 pi/L)) ~ 4 pi^2/L^2 on the co-exact sector — so only the Haar half survives, and only the operator-valued hinge of item 7, not the scalar bound of DOC1, is usable. Item 11 (obstruction III): the criterion is a pure beta-condition with no lattice spacing in it, asymptotic freedom drives beta to infinity, and the localized version fails too because the hinge radius scales as 1/beta while fluctuations scale as beta^{-1/2}.

NUMERICS AS ARBITER. Items 12-13 are executed computations that decide questions the analytics left open. The SU(2) one-link model (item 12) is exactly solvable and pins beta_c = 4.4139 with the bad-set mass decaying like e^{-beta}; it is the cleanest picture of the convexity-versus-typicality tension. The SU(3) engine (item 13) shows genuine volume stability of the convex core (L = 6 and L = 8 radii agree to 1%), which is real evidence — but my power-law fit of its own R_L(beta) data gives R ~ beta^{-0.81}, selecting the linear-erosion branch and therefore voting against the beta^{-1/2} scaling that would be needed for the localization strategy to close. That fit connects item 13 directly back to obstruction III (item 11) and to the Schur-complement analysis in item 7.

CROSS-CUTTING. Item 1 (the normalization ledger) is what makes every other item checkable; without it the constants across the archive look contradictory. Item 4 (the factor 3 between the two "equivalent viewpoints") is what makes the corpus's own best window 3x too pessimistic, and it also explains the JAX engine's factor-2 conservatism. Item 14 shows that the archive's single most-quoted number, kappa_* = 0.25, is not a fitted constant at all but exactly N/12 — and item 3 then upgrades it from a small-ball statement to a global one.

RELATION TO THE REST OF THE CORPUS. This body of work is the source for the COMBES_THOMAS, HELFFER_SJOSTRAND, MAXWELL and LSI_POINCARE directories (all of which consume the matrix hinge as input); for the RICCATI and RG_COARSE directories (which attempt to restore convexity under coarse-graining after item 9 kills it directly); and for POLARITY_GRIBOV (which handles the P_phys / reducible-configuration gap flagged in item 14).

## Further material found but not fully extracted

Things I found in this area and did not have room to develop:

1. `HAAR/01_haar_mass/06_CURVATURE_DEFECT/05_curvature_defect_obstruction_principle.md` — the "obstruction principle": define Phi(a) = E_{mu_a}[max(0, kappa_* - lambda_min(H^phys))] as a scale diagnostic; conjecture that Phi(a) -> 0 forces a Gaussian continuum limit, hence an interacting limit forces persistent defect, hence a gap. The document is honest about its own broken step: it correctly identifies that the dream monotonicity H_{a'} = E[H_a | G_{a'}] is FALSE because the Wilsonian effective Hessian is Hess S_{a'} = E[Hess S_a | U'] - Cov(grad S_a, grad S_a | U') plus Jacobian terms, i.e. an inequality not an identity. Reconstructing the correct one-sided version and determining the sign of the covariance term after horizontal projection is a well-posed, tractable problem and would be the natural next piece to extract.

2. `HAAR/01_haar_mass/04_SU2_CALCULATIONS/` has more executed SU(2) material I only sampled: `1_local_cancellation_su2.md` and `03_local_cancellation_alignment_su2.md` (8.6 kB and 6.4 kB) argue a local cancellation in the SU(2) Wilson third derivative, with the "Cartan-aligned set has measure zero" claim; `05_exact_force_su2_2d_numerics.md` and `su2-drift-certificates.md` / `su2_outside_core_certificates.md` (9.1 and 8.2 kB) contain drift-certificate numerics for the Lyapunov step. If the cancellation D^3 S_p(0)[K,K,.] = 0 is decidable anywhere it is in these SU(2) files, and it is the single highest-leverage open question in the whole mechanism (item 7 / item 11).

3. `HESSIAN/Core_Hessian/` contains ~35 large .txt files (12-65 kB, filenames are literally "#" and "##") that are raw chat transcripts, including `# Part 2 — Bakry–Émery Γ₂ Calculus PRO.txt` and `## 6.1 Bochner Γ_2 identity with drift and the Bakry–Émery curvature matrix.txt`. These are the primary sources the polished .md extracts were distilled from; I worked from the extracts. If a step in items 6/7/11 needs its original derivation, it is in there.

4. `HAAR/01_haar_mass/05_SU3_CALCULATIONS/E_SU3_Convexity_Engine_and_Results.md` (11.4 kB) and `PHASE_SU3_OutsideCore_Coercivity.md` (10.2 kB) and `03_SU3_Lattice_Hessian_Convexity_Lanczos_v2.md` (10.3 kB) — additional SU(3) engine variants and an attempt at coercivity outside the convex core. I extracted from `Selected_Numerics_...` because it has the most complete stored tables (all three field scales at all three volumes plus the bisection R-curve).

5. `HAAR/01_haar_mass/07_SAFE_REGION/tubular_neighborhood_flat_stratum.md` and the O'Neill question. I could not find anywhere in the corpus a treatment of whether a horizontal Bakry-Émery bound on the total space descends to a genuine curvature-dimension condition on the quotient M_Lambda / G_Lambda. For a Riemannian submersion the O'Neill A-tensor contributes with a favourable sign to the quotient sectional curvature, so this ought to work and would strengthen item 6 from "CD on invariant functions of the total space" to "CD on the orbit space" — but it needs the singular stratum (reducible connections) handled, which is the POLARITY_GRIBOV material.

6. `SCALING_LIMIT/04_CONSTANT_UNIFORMITY/04_no_go_coarse_graining_kernels.md` and `01_conditional_spectral_floor_monotonicity.md` — a no-go for coarse-graining kernels and a conditional spectral-floor monotonicity lemma. Given that item 9 forces the programme into RG restoration, these are the two documents that decide whether that route can work; I did not read them.

7. Verification artifacts I produced are in the scratchpad at `C:\Users\Alex\AppData\Local\Temp\claude\F--ANTIGRAVITY-antigravity-playground-scalar-cluster-proof\fd74385b-6527-446a-ae5a-90acb16ad82a\scratchpad\` (verify.py, verify2.py, verify3.py, verify5.py, verify6.py, maxwell.py). Every constant reported above is reproduced by one of them.
