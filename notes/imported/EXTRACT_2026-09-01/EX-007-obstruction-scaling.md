---
id: EX-007
title: "Obstruction: the scaling dichotomy and dimensional transmutation in the lattice Yang-Mills convexity/curvature program"
kind: extraction
items: 8
status_breakdown: {"solid": 8}
program: yang_mills
extracted_by: claude-opus-5 subagent, 2026-09-01
stance: preservation (content extraction, not refereeing)
source_files:
  - UNIFORMITY_ASYMPTOTIC_FREEDOM/07_heat_kernel_weyl_denominator_scale_independent_sigma_geom.md
  - UNIFORMITY_ASYMPTOTIC_FREEDOM/01_pillarL_geometric_mass_gap_expanded.md
  - SCALING_LIMIT/08_EXTERNAL_SOURCES/04_continuum_obstruction_and_stabilizers.md
  - WILSON/03_decay_bounds/04_helffer_sjostrand_and_greens_decay.md
  - WILSON/04_curvature_flow/lemma_unity_stitched_curvature_rg.md
  - WILSON/05_proofs_reports/RECOMMENDED_02_Global_BE_Obstruction_and_Localization_v2.md
  - HAAR/01_haar_mass/02_HAAR_MASS/01_haar_mass_hessian_and_gribov_region.md
  - HAAR/01_haar_mass/02_HAAR_MASS/02_haar_mass_geometry.md
  - HAAR/01_haar_mass/07_SAFE_REGION/RECOMMENDED_01_Finite_Cutoff_Haar_Wilson_Windows_v2.md
  - WILSON/03_decay_bounds/03_wilson_hessian_maxwell.md
  - SCALING_LIMIT/08_EXTERNAL_SOURCES/05_sigma_geom_weyl_denominator_lower_bound.md
  - POLARITY_GRIBOV/03_misc_docs/12_Entropic_Spark_Conjecture.md
  - UNIFORMITY_ASYMPTOTIC_FREEDOM/06_Riccati_Convexity_Attractor.md
  - RICCATI/01_riccati_flow/referee_riccati_spine_and_sigma_geom_sources.md
  - COMBES_THOMAS/RICCATI_RG/03_localized_curvature_capacity_rg.md
  - lean/YangMills/AsymptoticFreedom.lean
---

# Obstruction: the scaling dichotomy and dimensional transmutation in the lattice Yang-Mills convexity/curvature program

> The corpus's "scale-independent geometric source" and its "vanishing a^2 g^2 Haar mass" are one and the same geometric constant kappa_G/3 = N/6 read in two charts related by X = a g_0 A; restoring the (a g_0)^2 Jacobian consistently shows every convexity-based mass in the program equals nu/a with nu a power of g_0(a), so m_phys diverges like 1/(a sqrt(log(1/a Lambda))) instead of converging to Lambda = a^{-1} exp(-1/(2 b_0 g_0^2)), and no power law in g_0 can ever reproduce a dimensionally transmuted scale.

**8 extracted items** — 8 solid

---

## 1. Chart-Jacobian Lemma: the a^2 g_0^2 in the 'Haar mass' is exactly the square of the coordinate Jacobian dX/dA = a g_0, and the invariant Haar/Ricci constant is kappa_G/3 = N/6

`status: solid` · `kind: theorem`

### Statement

Let $G=SU(N)$ with Lie algebra $\mathfrak g=\mathfrak{su}(N)$ and the bi-invariant metric $\langle X,Y\rangle=-\operatorname{Tr}(XY)$ (so $\|X\|^2=-\operatorname{Tr}X^2$ for anti-Hermitian $X$). Fix a lattice spacing $a>0$ and a bare coupling $g_0>0$. On one link consider the two standard charts near the identity:

(i) the **angle chart** $X\in\mathfrak g$, $U=\exp X$ (dimensionless; $X$ is the geodesic normal coordinate of the bi-invariant metric, and on the maximal torus $X=i\,\mathrm{diag}(\theta_1,\dots,\theta_N)$ with $\theta$ the eigenangles);

(ii) the **physical-field chart** $A\in i\mathfrak g$ (Hermitian traceless), $U=\exp(i a g_0 A)$, so that $A$ has mass dimension $1$.

The two are related by the linear map $X = i\,a g_0 A$, i.e. $\|X\| = a g_0 \|A\|$.

Define the **Haar potential** $S_H := -\log J$, where $J$ is the density of Haar measure with respect to Lebesgue measure in the chosen chart,
$$J(X)=\det{}_{\mathfrak g}\Big(\tfrac{\sinh(\operatorname{ad}_X/2)}{\operatorname{ad}_X/2}\Big).$$

Then:

**(a)** $\operatorname{Ric}_{g_G}=\kappa_G\,g_G$ with $\kappa_G=N/2$.

**(b)** In the angle chart, $S_H(X)=\tfrac{1}{6}\operatorname{Ric}(X,X)+O(\|X\|^4)=\tfrac{N}{12}\|X\|^2+O(\|X\|^4)$ and
$$\nabla^2_X S_H(0)=\tfrac13\operatorname{Ric}=\tfrac{\kappa_G}{3}\,\mathrm{Id}=\tfrac{N}{6}\,\mathrm{Id},$$
which is **independent of $a$ and of $g_0$**.

**(c)** In the physical-field chart, for every $C^2$ function $S$,
$$\nabla^2_A S = (a g_0)^2\,\nabla^2_X S,\qquad d^{\dim\mathfrak g}X=(ag_0)^{\dim\mathfrak g}\,d^{\dim\mathfrak g}A,$$
so in particular
$$\nabla^2_A S_H(0)=c_0\,a^2g_0^2\,\mathrm{Id},\qquad c_0=\tfrac{N}{6}=\tfrac{\kappa_G}{3}.$$

**(d)** The Bakry-Emery curvature relative to the metric (i.e. the endomorphism $g^{-1}(\operatorname{Ric}+\nabla^2 S)$, whose eigenvalues are what enters Bakry-Emery / Poincare / log-Sobolev constants) is **the same object in both charts**; the factor $a^2g_0^2$ appears only if one computes the Hessian as a bilinear form in $A$-coordinates and then compares it against the *flat* metric $\delta_{ab}dA^adA^b$ instead of the group metric $g^{(A)}=(ag_0)^2\delta$.

Consequently the corpus's two mutually contradictory statements -- 'the Haar/Ricci floor is an $a$-independent constant $c_H$' and 'the Haar mass is $c_0a^2g^2\to0$' -- are the *same* geometric fact stated in two charts, and $a^2g_0^2$ is a coordinate Jacobian, not a physical suppression.

### Derivation

**Step 1: the adjoint-trace identity.** For $\mathfrak{su}(N)$ with $\langle X,Y\rangle=-\operatorname{Tr}(XY)$ the Killing form is $\kappa(X,Y)=\operatorname{Tr}_{\mathfrak g}(\operatorname{ad}_X\operatorname{ad}_Y)=2N\operatorname{Tr}(XY)$. (Verified numerically to machine precision for $N=2,3,4$ on random $X$; see the code field.)

**Step 2: Ricci of a bi-invariant metric.** For a compact simple group with bi-invariant metric, $\operatorname{Ric}(X,X)=-\tfrac14\kappa(X,X)$. With Step 1, for anti-Hermitian $X$, $\kappa(X,X)=2N\operatorname{Tr}(X^2)=-2N\|X\|^2$, hence
$$\operatorname{Ric}(X,X)=\tfrac{N}{2}\|X\|^2\ \Longrightarrow\ \kappa_G=\tfrac N2 .$$

**Step 3: normal-coordinate expansion of the volume density.** In geodesic normal coordinates at the identity,
$$d\mathrm{vol}(\exp X)=J(X)\,dX,\qquad J(X)=1-\tfrac16\operatorname{Ric}(X,X)+O(\|X\|^3),$$
so $S_H(X)=-\log J(X)=\tfrac16\operatorname{Ric}(X,X)+O(\|X\|^3)$ and, since $\operatorname{Ric}(X,X)$ is quadratic,
$$\nabla^2_X S_H(0)=\tfrac{2}{6}\operatorname{Ric}=\tfrac13\operatorname{Ric}=\tfrac{\kappa_G}{3}\,\mathrm{Id}=\tfrac N6\,\mathrm{Id}.$$

**Step 4: the same thing from the exponential-map Jacobian (this is the corpus's route, done in the angle chart).** Put $Y:=\tfrac12\operatorname{ad}_X$, so $J=\det_{\mathfrak g}(\sinh Y/Y)$ and $S_H=-\operatorname{Tr}_{\mathfrak g}\log(\sinh Y/Y)$. Using $\log(\sinh y/y)=y^2/6+O(y^4)$ and holomorphic functional calculus,
$$S_H(X)=-\tfrac16\operatorname{Tr}_{\mathfrak g}(Y^2)+O(\|X\|^4)=-\tfrac1{24}\operatorname{Tr}_{\mathfrak g}(\operatorname{ad}_X^2)+O(\|X\|^4).$$
By Step 1, $\operatorname{Tr}_{\mathfrak g}(\operatorname{ad}_X^2)=2N\operatorname{Tr}(X^2)=-2N\|X\|^2$, hence
$$S_H(X)=\tfrac{N}{12}\|X\|^2+O(\|X\|^4),\qquad \nabla^2_XS_H(0)=\tfrac N6\,\mathrm{Id}. $$
This agrees with Step 3, as it must.

**Step 5: the chart change.** The corpus writes $U_b=\exp(iag A_b)$ and expands *the same* $S_H$ in $A$. Substituting $X=iag_0A$ into Step 4 gives directly
$$S_H(A)=\tfrac{N}{12}a^2g_0^2\|A\|^2+O(a^4g_0^4\|A\|^4),\qquad \nabla^2_AS_H(0)=\tfrac N6 a^2g_0^2\,\mathrm{Id}=c_0a^2g_0^2\,\mathrm{Id},\ c_0=\tfrac N6 .$$
This is exactly the corpus formula $\mathrm{Hess}\,S_{\mathrm{Haar}}=c_0a^2g^2 I$ with $c_0=N/6$ (RECOMMENDED_01 §3, lemma_unity §3, 01_haar_mass_hessian §3). Comparing with Step 4, the *entire* $a$- and $g_0$-dependence is the chain-rule factor $(\partial X/\partial A)^2=(ag_0)^2$.

**Step 6: why the invariant statement has no $a$ in it.** The bi-invariant metric written in $A$-coordinates is $g^{(A)}=(ag_0)^2\delta$. The Bakry-Emery operator whose eigenvalues control Poincare/LSI constants is the endomorphism $\mathcal R := (g)^{-1}(\operatorname{Ric}+\nabla^2S)$. In the $A$-chart,
$$\mathcal R^{(A)}=\big[(ag_0)^2\delta\big]^{-1}\Big[(ag_0)^2\big(\operatorname{Ric}^{(X)}+\nabla^2_XS\big)\Big]=\operatorname{Ric}^{(X)}+\nabla^2_XS=\mathcal R^{(X)} .$$
So the eigenvalue is $\kappa_G+\kappa_G/3=\tfrac N2+\tfrac N6=\tfrac{2N}{3}$ in **both** charts. The number $c_0a^2g_0^2$ arises only when the $A$-chart Hessian (a bilinear form of dimension $[A]^{-2}=\mathrm{length}^2$) is compared against the flat metric $\delta$, which is not the group metric. That mismatch is the entire source of the corpus's 'contradiction 7/8/11' (documented in HAAR/analysis_reports/contradictions_*).

**Step 7 (independent cross-check on the Cartan, using the Weyl denominator).** On the maximal torus $X=i\,\mathrm{diag}(\theta)$, $\operatorname{ad}_X$ has eigenvalues $i(\theta_i-\theta_j)$ on the root spaces and $0$ on the Cartan, so with $u_{ij}:=(\theta_i-\theta_j)/2$,
$$J(X)=\prod_{i\neq j}\frac{\sinh(iu_{ij})}{iu_{ij}}=\prod_{i<j}\Big(\frac{\sin u_{ij}}{u_{ij}}\Big)^2,\qquad S_H(\theta)=-2\sum_{i<j}\log\frac{\sin u_{ij}}{u_{ij}} .$$
Differentiating twice along $\theta\mapsto\theta+tx$ (so $\dot u_{ij}=(x_i-x_j)/2$):
$$\delta^2S_H[x,x]=\tfrac12\sum_{i<j}\Big(\csc^2u_{ij}-\tfrac1{u_{ij}^2}\Big)(x_i-x_j)^2\ \xrightarrow[\theta\to0]{}\ \tfrac16\sum_{i<j}(x_i-x_j)^2=\tfrac N6\|x\|^2,$$
using $\csc^2u-u^{-2}\to 1/3$ and $\sum_{i<j}(x_i-x_j)^2=N\|x\|^2$ on $\sum_ix_i=0$. So $\nabla^2S_H(0)|_{\mathrm{Cartan}}=(N/6)\mathrm{Id}$, matching Steps 3-4. (Verified numerically: eigenvalues $0.3333,0.5,0.6667,0.8333$ for $N=2,3,4,5$ versus $N/6$.) [The $\theta\to0$ limit step and the numerical confirmation are mine; the corpus computes only $-\log|\Delta|^2$, never the difference.]

**Step 8 (SU(2) sanity check, the corpus's own example).** For $SU(2)$, $U=\exp(ir\,\hat n\cdot\sigma)$, Haar $\propto\sin^2r\,dr\,d\Omega$ against flat $r^2dr\,d\Omega$, so $J(r)=(\sin r/r)^2$ and $S_H(r)=-2\log(\sin r/r)=r^2/3+O(r^4)$. Since $r^2=\|X\|^2/2$ in the metric $-\operatorname{Tr}$, $S_H=\|X\|^2/6$ and $\nabla^2S_H(0)=\tfrac13\mathrm{Id}=\tfrac N6\mathrm{Id}$ at $N=2$. ✓

### Constants and numbers

kappa_G = N/2 (Ricci of SU(N), bi-invariant metric <X,Y> = -Tr XY).
kappa_G(SU(2)) = 1, kappa_G(SU(3)) = 3/2.
c_0 = kappa_G/3 = N/6: Hess S_Haar(0) = (N/6) Id in the angle chart.
  SU(2): 1/3 = 0.33333. SU(3): 1/2 = 0.50000. SU(4): 2/3. SU(5): 5/6.
  (Numerically confirmed to 5 decimals on the Cartan by finite differences of -log J.)
Adjoint-trace: Tr_g(ad_X ad_Y) = 2N Tr(XY); verified to 1e-15 relative for N = 2,3,4.
Bakry-Emery identity part in the angle chart: Ric + Hess S_Haar = (N/2 + N/6) Id = (2N/3) Id.
  SU(2): 4/3 = 1.3333. SU(3): 2.
Chart Jacobian: dX/dA = a g_0, so Hess_A = (a g_0)^2 Hess_X; the corpus's c_0 a^2 g^2 with c_0 = N/6.
Note on corpus conventions: several files quote 'c_H = 1/6' for SU(2); that is the coefficient of Ric(X,X) in S_H, not the Hessian (which is 1/3 = 2 x 1/6). CAND-018 reports the same object as '0.5*I' for SU(3), which is N/6 at N=3. Also quoted in the corpus: c_0 = (N^2-1)/(2N) (01_pillarL_expanded §2.1), which does not match N/6 for any N >= 2 and appears to be an unrelated Casimir; the value that is reproducible from the stated Jacobian is N/6.

### Code

# Verifies (i) Tr_g(ad_X^2) = 2N Tr(X^2) on su(N), (ii) Hess(-log J)|_Cartan(0) = (N/6) I.
# Run: python checks.py   (numpy only)
import numpy as np, math

def su_basis(N):
    B=[]
    for i in range(N):
        for j in range(i+1,N):
            E=np.zeros((N,N),complex); E[i,j]=1;  E[j,i]=-1; B.append(E)
            E=np.zeros((N,N),complex); E[i,j]=1j; E[j,i]=1j; B.append(E)
    for k in range(1,N):
        d=np.zeros(N,complex); d[:k]=1j; d[k]=-1j*k; B.append(np.diag(d))
    ON=[]
    for X in B:                       # Gram-Schmidt wrt <X,Y> = -Tr(XY)
        for Y in ON: X = X - (-np.trace(X@Y)).real*Y
        ON.append(X/math.sqrt((-np.trace(X@X)).real))
    return ON

for N in (2,3,4):
    ON=su_basis(N); dim=len(ON)
    X=sum(np.random.randn()*b for b in ON)
    ad=np.array([[(-np.trace((X@ON[b]-ON[b]@X)@ON[a])).real for b in range(dim)]
                 for a in range(dim)])
    print(N, np.trace(ad@ad).real / (2*N*np.trace(X@X).real))   # -> 1.000000

def SHaar_cartan(th):                 # -log J on the maximal torus
    s=0.0
    for i in range(len(th)):
        for j in range(i+1,len(th)):
            u=(th[i]-th[j])/2.0; s += -2*math.log(math.sin(u)/u)
    return s

def hess_num(f,x0,h=1e-3):
    n=len(x0); H=np.zeros((n,n))
    for i in range(n):
        for j in range(n):
            ei=np.zeros(n); ei[i]=h; ej=np.zeros(n); ej[j]=h
            H[i,j]=(f(x0+ei+ej)-f(x0+ei-ej)-f(x0-ei+ej)+f(x0-ei-ej))/(4*h*h)
    return H

for N in (2,3,4,5):
    th=1e-3*np.arange(N); th-=th.mean()
    P=np.eye(N)-np.ones((N,N))/N       # project onto sum x_i = 0
    ev=np.sort(np.linalg.eigvalsh(P@hess_num(SHaar_cartan,th)@P))[1:]
    print(N, ev, N/6)                  # -> all eigenvalues equal N/6

**Caveat.** The identification is exact only for the quadratic (vacuum) term; away from the identity the two charts are still related by the same diffeomorphism, but 'Hess = c_0 a^2 g^2 I' is a statement at A = 0 only, valid in a normal neighbourhood.

**Why it matters.** This single lemma dissolves the corpus's central internal contradiction and is the precondition for stating the scaling dichotomy correctly. Once it is in place, 'find an a-independent geometric source sigma_geom' and 'the Haar mass vanishes like a^2 g^2' are seen to be the same statement, so no repair can consist of preferring one over the other.

---

## 2. The scaling dichotomy: every chart reading of the convexity floor gives m_phys -> infinity or m_phys -> 0, never a finite continuum mass

`status: solid` · `kind: obstruction`

### Statement

Fix $N\ge2$, $d=4$. Let $a\mapsto g_0(a)$ run along the asymptotically free trajectory, so that $g_0(a)\downarrow0$ and $\beta(a)=2N/g_0^2(a)\to\infty$ as $a\downarrow0$. Let $S_{\mathrm{eff}}=\beta S_W+S_{\mathrm{Haar}}$ on $\mathcal C=SU(N)^{|B|}$ and let $\rho$ denote any convexity/Bakry-Emery floor produced by the program. Write $\hat m(a)$ for the resulting **dimensionless lattice-unit** mass and $m_{\mathrm{phys}}(a)=\hat m(a)/a$. Then exactly one of the following happens, depending on which chart the floor is read in, and none of them is a continuum mass gap:

**(H1) Angle/eigenangle chart, floor $a$-independent.** If one takes the floor to be the $a$-independent constant available in the angle chart -- $\sigma_{\mathrm{geom}}\ge N/2$ from the Weyl denominator, or $\kappa_G+\kappa_G/3=2N/3$ from Ricci + Haar, or the Riccati fixed point $\lambda_*=\sqrt{\sigma/2}$ -- and identifies $\hat m=\lambda_*$, then
$$m_{\mathrm{phys}}(a)=\frac{\lambda_*}{a}\ \xrightarrow[a\to0]{}\ +\infty\quad\text{like } a^{-1}.$$

**(H2) Physical-field chart, floor $=c_0a^2g_0^2$.** If one restores the $(ag_0)^2$ Jacobian and takes $\Delta_{\mathrm{lat}}=c_0a^2g_0^2(a)$ (the corpus's own honest source, and literally what its Lean file proves), then
$$m_{\mathrm{phys}}(a)=\frac{\Delta_{\mathrm{lat}}}{a}=c_0\,a\,g_0^2(a)\ \xrightarrow[a\to0]{}\ 0 .$$
This reading is moreover dimensionally inconsistent: $\nabla^2_AS$ has dimension $[A]^{-2}=\mathrm{length}^2$, so $\Delta_{\mathrm{lat}}/a$ has dimension $\mathrm{length}$, not $\mathrm{length}^{-1}$.

**(H3) The chart-invariant reading (the honest one).** The only chart-independent quantity built from the hinge $\operatorname{Ric}_\mu\succeq m_H^2I+\alpha_W d_1^*d_1$ is the ratio $m_H^2/\alpha_W$, and the associated lattice-unit decay exponent is
$$\nu(a)=\operatorname{arcosh}\!\Big(1+\frac{m_H^2}{2\alpha_W}\Big)=\sqrt{\frac{m_H^2}{\alpha_W}}\,(1+O(g_0^2))=\sqrt{\tfrac N3}\;g_0(a)\,(1+O(g_0^2)),$$
so
$$m_{\mathrm{phys}}(a)=\frac{\nu(a)}{a}\ \asymp\ \frac{g_0(a)}{a}\ \asymp\ \frac{1}{a\sqrt{\log(1/a\Lambda_L)}}\ \xrightarrow[a\to0]{}\ +\infty .$$

In all three cases $m_{\mathrm{phys}}(a)/\Lambda_L\to\infty$ or $\to0$; none converges to a finite nonzero multiple of $\Lambda_L$.

### Derivation

**Setup and normalizations (all in the angle chart, which is the only self-consistent one).**
Configuration manifold $\mathcal C=SU(N)^{|B|}$, bi-invariant product metric from $\langle X,Y\rangle=-\operatorname{Tr}(XY)$. Wilson action
$$S_W(U)=\sum_p\Big(1-\tfrac1N\Re\operatorname{Tr}U_p\Big),\qquad \beta=\frac{2N}{g_0^2},$$
and $S_{\mathrm{eff}}=\beta S_W+S_{\mathrm{Haar}}$.

*Wilson Hessian at the vacuum.* In exponential coordinates $\log U_p=(d_1X)_p+O(\|X\|^2)$ and $\Re\operatorname{Tr}(I-e^{Y})=\tfrac12\|Y\|^2+O(\|Y\|^3)$, so
$$\beta S_W(\exp X)=\text{const}+\frac{\beta}{2N}\,\|d_1X\|^2+O(\|X\|^3),\qquad \nabla^2_X(\beta S_W)(0)=\frac{\beta}{N}\,d_1^*d_1=\frac{2}{g_0^2}\,d_1^*d_1 .$$
(This is WILSON/03_decay_bounds/03_wilson_hessian_maxwell.md eq. (4.2), $\nabla^2S_W=2c_Wd_1^*d_1$, with $c_W=\beta c_{\rm HS}/(2N)$ and $c_{\rm HS}=1$.)

*Haar Hessian at the vacuum.* By the Chart-Jacobian Lemma, $\nabla^2_XS_{\mathrm{Haar}}(0)=(N/6)\,\mathrm{Id}$.

*Ricci.* $\operatorname{Ric}=(N/2)\mathrm{Id}$ on the product.

Hence the **matrix hinge** in the angle chart, at (and in a normal neighbourhood of) the vacuum,
$$\operatorname{Ric}_\mu=\operatorname{Ric}+\nabla^2S_{\mathrm{eff}}\ \succeq\ m_H^2\,I+\alpha_W\,d_1^*d_1,\qquad m_H^2=\frac{2N}{3},\quad \alpha_W=\frac{\beta}{N}=\frac{2}{g_0^2}.$$
If one drops the Ricci contribution and keeps only the Haar Jacobian, $m_H^2=N/6$.

**(H1).** In this chart both $m_H^2$ and every candidate $\sigma_{\mathrm{geom}}$ (Weyl denominator: $N/2$; Ricci+Haar: $2N/3$) are numbers, independent of $a$ and $g_0$. The Riccati mechanism (UNIFORMITY_ASYMPTOTIC_FREEDOM/06) then yields the attractor $\lambda_*=\sqrt{\sigma/2}$, again a pure number. The program's stated bridge to a physical mass is $\Delta=\hat m/a$ (Exciting_03_One_Step_Gap_Bridge Thm 4.1: $\Delta\ge a^{-1}(-\log(1-c\lambda_*))\ge c\lambda_*/a$; Synthesis_10 §: '$\Delta_\Lambda\ge c_*\lambda_*/a$'). Since $\lambda_*$ is $a$-independent and positive, $m_{\mathrm{phys}}=\lambda_*/a\to\infty$. This is not a mass gap; it is the statement that the correlation length is a fixed number of lattice spacings, i.e. that the theory has no continuum limit at all along this trajectory.

**(H2).** In the $A$-chart the same object reads $c_0a^2g_0^2$ with $c_0=N/6$. Applying the *same* bridge $\Delta_{\rm lat}/a$ gives $m_{\mathrm{phys}}=c_0ag_0^2(a)\to0$. This leg is literally formalized in the corpus: `lean/YangMills/AsymptoticFreedom.lean` defines `lattice_gap_bound c0 a g0_sq := c0 * a^2 * g0_sq`, `physical_mass D a := D / a`, and proves
```
theorem mass_finite : physical_mass (lattice_gap_bound c0 a g0_sq) a = c0 * a * g0_sq
```
under the docstring 'Mass survival ... m_phys = O(Lambda)'. The proved arithmetic is correct; the docstring's conclusion is the opposite of what it says, because $c_0\,a\,g_0^2(a)\to0$. Note also that (H2) is not merely wrong in magnitude: $\nabla^2_AS$ carries dimension $\mathrm{length}^2$, so the very expression $\Delta_{\rm lat}/a$ mixes two different Dirichlet forms (the group-metric one and the flat-$A$ one). The corpus's convexity window inherits the same defect: RECOMMENDED_01 Thm 4.1 states the window as $g^4>288/(Na^2)$, which is dimensionally inhomogeneous ($g$ is dimensionless in $d=4$, $a$ is a length).

**(H3): the chart-invariant computation.** Both $m_H^2$ and $\alpha_W$ scale by $(ag_0)^{2}$ under the chart change, so the **ratio** $m_H^2/\alpha_W$ is invariant:
$$\frac{m_H^2}{\alpha_W}\Big|_{X\text{-chart}}=\frac{2N/3}{2/g_0^2}=\frac{N g_0^2}{3},\qquad \frac{m_H^2}{\alpha_W}\Big|_{A\text{-chart}}=\frac{(N/6)a^2g_0^2}{2a^2}\cdot 4=\frac{Ng_0^2}{3}\ \ (\text{same}).$$
(Haar-only: $Ng_0^2/12$ in both charts.) The physical content of the hinge is therefore the *dimensionless* ratio $Ng_0^2/3$, and it is $O(g_0^2)$, not $O(1)$.

The Green's function of $M=m_H^2I+\alpha_W d_1^*d_1$ on $\ker d_0^*$ decays with the exact axial rate (see the separate Combes-Thomas item)
$$\nu=\operatorname{arcosh}\!\Big(1+\frac{m_H^2}{2\alpha_W}\Big)=2\operatorname{arsinh}\!\Big(\frac{m_H}{2\sqrt{\alpha_W}}\Big)=\sqrt{\frac{m_H^2}{\alpha_W}}\big(1+O(m_H^2/\alpha_W)\big)=\sqrt{\tfrac N3}\,g_0\,(1+O(g_0^2)).$$
This $\nu$ is a decay rate *per lattice step*, hence dimensionless, hence $m_{\mathrm{phys}}=\nu/a$ is legitimate. Substituting one-loop asymptotic freedom $g_0^2(a)=\big(2b_0\log(1/a\Lambda_L)\big)^{-1}$,
$$m_{\mathrm{phys}}(a)=\frac{1}{a}\sqrt{\frac{N}{3}}\,\frac{1}{\sqrt{2b_0\log(1/a\Lambda_L)}}\ \Longrightarrow\ \frac{m_{\mathrm{phys}}(a)}{\Lambda_L}=\sqrt{\frac{N}{6b_0}}\;\frac{1}{a\Lambda_L\sqrt{\log(1/a\Lambda_L)}}\ \to\ \infty .$$
The divergence is by a factor $1/(a\Lambda_L)$ up to a $\sqrt{\log}$, i.e. by the whole UV/IR ratio.

**Interpretation of (H3) as a physical statement.** The lattice measure written in the $A$-chart has quadratic part
$$a^2\Big[\|d_1A\|^2+\tfrac{N}{12}g_0^2\sum_b\|A_b\|^2\Big],$$
so the Haar Jacobian is a genuine gluon mass term of size $m_{\rm Haar}\sim g_0(a)/a$ in physical units -- an $O(g_0)$ fraction of the cutoff. This is the correct physical reading of the 'Haar mass': it is a *cutoff-scale* mass, and it disappears from the continuum theory not because it is small but because it is removed by the (multiplicative) renormalization that defines the continuum limit. There is no chart in which it becomes $\Lambda$.

**Why the corpus never sees this.** WILSON/03_decay_bounds/04 computes $\nu$ and says verbatim that 'the lattice-unit mass behaves like $\beta^{-1/2}$', then defers the $a$-dependence to 'a separate continuum-limit argument'. That argument is never written. Substituting $\beta(a)\asymp\log(1/a\Lambda)$ into $\nu\asymp\beta^{-1/2}$ and dividing by $a$ is the missing arithmetic. [Attribution: the substitution is mine; the two halves are the corpus's.]

### Constants and numbers

Angle chart, SU(N), d = 4, metric <X,Y> = -Tr XY:
  Ric = (N/2) I ;  Hess S_Haar(0) = (N/6) I ;  Hess (beta S_W)(0) = (beta/N) d1* d1 = (2/g0^2) d1* d1.
  Hinge: m_H^2 = 2N/3 (Ric+Haar) or N/6 (Haar only);  alpha_W = beta/N = 2/g0^2.
Chart-invariant ratio m_H^2 / alpha_W = N g0^2 / 3 (Ric+Haar)  or  N g0^2 / 12 (Haar only).
Exact CT exponent nu = arcosh(1 + m_H^2/(2 alpha_W)).
  Numerically (Ric+Haar): nu / g0 -> sqrt(N/3): SU(2) 0.7768, 0.8021, 0.8091, 0.8142 at beta = 2,6,12,40 (limit 0.8165);
                            SU(3) 0.9046, 0.9624, 0.9803, 0.9939 at beta = 2,6,12,40 (limit 1.0000).
  Haar only: nu / g0 -> sqrt(N/12): SU(3) 0.4856, 0.4949, 0.4974, 0.4992 (limit 0.5).
Beta-function coefficients (pure SU(N), MS-like lattice conventions):
  b0 = 11N/(48 pi^2):  b0(2) = 0.0464388, b0(3) = 0.0696577.
  b1 = (34 N^2/3)/(16 pi^2)^2: b1(2) = 1.817934e-3, b1(3) = 4.090352e-3.
  b1/(2 b0^2) = 51/121 = 0.4214876 (N-independent).
  2-loop: a Lambda_L = (b0 g0^2)^{-51/121} exp(-1/(2 b0 g0^2)).
SU(3) divergence of m_pipe = nu/a (with nu = sqrt(N/3) g0), target m/Lambda = 3:
  beta=6   g0^2=1.00  nu=1.000  a*Lam=2.35e-3  m_pipe/Lam=4.26e+2   (x142 too big)
  beta=8   g0^2=0.75  nu=0.866  a*Lam=2.42e-4  m_pipe/Lam=3.58e+3   (x1.19e3)
  beta=12  g0^2=0.50  nu=0.707  a*Lam=2.40e-6  m_pipe/Lam=2.95e+5   (x9.83e4)
  beta=20  g0^2=0.30  nu=0.548  a*Lam=2.07e-10 m_pipe/Lam=2.64e+9   (x8.80e8)
  beta=40  g0^2=0.15  nu=0.387  a*Lam=1.13e-20 m_pipe/Lam=3.43e+19  (x1.14e19)
  beta=100 g0^2=0.06  nu=0.245  a*Lam=1.12e-51 m_pipe/Lam=2.20e+50  (x7.32e49)
SU(2) same construction: m_pipe/Lambda = 9.2e1, 1.06e4, 1.59e6, 2.66e8, 8.68e12, 1.22e22, 1.54e45 at beta = 2,4,6,8,12,20,40.
Horn (H2) numbers: m_phys = c0 a g0^2(a) = (N/6) a g0^2(a) -> 0; at SU(3), beta=12, a Lambda = 2.4e-6: m_phys/Lambda = 0.5 x 2.4e-6 x 0.5 = 6.0e-7.

### Code

# Reproduces the (H3) divergence table and the SU(2)/SU(3) coefficients.
# Run: python scaling.py   (numpy only)
import numpy as np

def b0(N): return 11.0*N/(48*np.pi**2)
def b1(N): return (34.0*N**2/3.0)/(16*np.pi**2)**2

def aLambda(g2, N):                    # 2-loop lattice asymptotic scaling
    B0, B1 = b0(N), b1(N)
    return (B0*g2)**(-B1/(2*B0**2)) * np.exp(-1.0/(2*B0*g2))

for N in (2, 3):
    print(f"SU({N})  b0={b0(N):.7f}  b1={b1(N):.6e}  b1/(2b0^2)={b1(N)/(2*b0(N)**2):.7f}")
    for beta in (2, 4, 6, 8, 12, 20, 40, 100):
        g2 = 2.0*N/beta
        nu = np.sqrt(N/3.0)*np.sqrt(g2)          # chart-invariant lattice-unit exponent
        aL = aLambda(g2, N)
        print(f"  beta={beta:5}  g0^2={g2:7.4f}  nu={nu:7.4f}"
              f"  a*Lambda={aL:11.4e}  m_phys/Lambda={nu/aL:11.4e}")

**Caveat.** The three horns are exhaustive for the specific bridges the corpus uses (Delta = lambda_*/a and the Green's-function exponent); a different, unspecified bridge between a Bakry-Emery constant and a Hamiltonian gap is not excluded by this argument alone -- it is excluded by the separate dimensional-transmutation item.

**Why it matters.** This is the decisive scaling argument. It shows the two apparently opposite failure modes the corpus oscillates between are two readings of one chart error, and it computes the honest third reading, which still misses by the full UV/IR ratio. It converts 'the continuum limit is an open sub-gap' into 'this mechanism gives a cutoff-scale mass, by construction'.

---

## 3. Dimensional-transmutation no-go: no power of g_0 can be a Yang-Mills mass, with a scale-invariant diagnostic chi(g) -> 1

`status: solid` · `kind: obstruction`

### Statement

Let $\Lambda_L>0$ and let $g_0(a)$ solve the two-loop lattice renormalization-group equation, so that
$$a\Lambda_L=\big(b_0g_0^2\big)^{-b_1/(2b_0^2)}\exp\!\Big(-\frac{1}{2b_0g_0^2}\Big),\qquad b_0=\frac{11N}{48\pi^2},\ \ b_1=\frac{34N^2/3}{(16\pi^2)^2},\ \ \frac{b_1}{2b_0^2}=\frac{51}{121}.$$
Suppose the continuum theory has a mass gap $m\in(0,\infty)$. Then the **required** lattice-unit gap is
$$\hat m(a):=m\,a=\frac{m}{\Lambda_L}\,\big(b_0g_0^2\big)^{-51/121}\exp\!\Big(-\frac{1}{2b_0g_0^2}\Big).$$
Define, for any candidate lattice-unit gap function $F:(0,g_{\max})\to(0,\infty)$, the **transmutation index**
$$\chi_F(g):=-2b_0\,g^2\log F(g).$$
Then:

**(a)** $\chi_{\hat m}(g)\to1$ as $g\downarrow0$.

**(b)** If $F(g)=Cg^{2p}\,(1+o(1))$ for some $C>0$ and $p\in\mathbb R$ -- i.e. $F$ is any power of the coupling, in particular $p=0$ (an $a$-independent 'geometric source'), $p=1/2$ (the Combes-Thomas/Haar hinge $\nu\asymp g_0$), or any $\sigma_*$-driven Riccati fixed point $\lambda_*=\sqrt{\sigma_*/2}$ with $\sigma_*$ a power of $g_0$ -- then $\chi_F(g)\to0$.

**(c)** More generally, if $F$ extends to a function that is $O(g^{-K})$ for some $K$ as $g\downarrow0$ (any power-bounded behaviour, including logs and rational functions of $g$ and $\log g$), then $\chi_F(g)\to0$. Hence $F\ne\hat m$ eventually, and
$$\frac{m_{\mathrm{phys}}(a)}{\Lambda_L}=\frac{F(g_0(a))}{a\Lambda_L}\longrightarrow+\infty .$$

Equivalently: the required $\hat m(a)$ vanishes **faster than every power of $g_0$** as $g_0\downarrow0$ (it is flat at $g_0=0$), so no mechanism whose output is analytic, or merely power-bounded, in the bare coupling can produce a Yang-Mills mass gap.

### Derivation

**(a)** Take logs of the required gap:
$$\log\hat m=\log\frac{m}{\Lambda_L}-\frac{51}{121}\log(b_0g_0^2)-\frac{1}{2b_0g_0^2}.$$
Multiply by $-2b_0g^2$ with $g=g_0$:
$$\chi_{\hat m}(g)=-2b_0g^2\log\frac{m}{\Lambda_L}+\frac{102}{121}b_0g^2\log(b_0g^2)+1\ \xrightarrow[g\downarrow0]{}\ 1,$$
since $g^2\to0$ and $g^2\log g^2\to0$.

**(b)** $\chi_{Cg^{2p}}(g)=-2b_0g^2(\log C+2p\log g)\to0$, again because $g^2\to0$ and $g^2\log g\to0$.

**(c)** If $F(g)\le Ag^{-K}$ and $F(g)\ge A'g^{K'}$ for small $g$ (power-bounded from both sides), then $|\log F(g)|\le \max(K,K')\,|\log g|+O(1)$, so $|\chi_F(g)|\le 2b_0g^2\big(\max(K,K')|\log g|+O(1)\big)\to0$. Since $\chi_{\hat m}\to1\ne0=\lim\chi_F$, $F\ne\hat m$ for all small $g$, and the ratio $F/\hat m=\exp\big[(\chi_{\hat m}-\chi_F)/(2b_0g^2)\big]$ diverges: indeed $F/\hat m=\exp\big[\frac{1+o(1)}{2b_0g^2}\big]\to\infty$. Dividing by $a$, $m_{\rm phys}/\Lambda_L=F/(a\Lambda_L)=(F/\hat m)\cdot(m/\Lambda_L)\to\infty$.

**Why every candidate in the corpus is power-bounded.** The three sources proposed as $\sigma_*$ are
* Weyl-denominator convexity: $\sigma_{\rm geom}\ge N/2$, a pure number ($p=0$);
* Ricci of the compact group: $\kappa_G=N/2$, a pure number ($p=0$);
* the Haar Jacobian in the physical chart: $c_0a^2g_0^2$, i.e. $\propto g_0^2$ after removing the chart factor $a^2$ ($p=1$);
and the Riccati attractor turns $\sigma_*$ into $\lambda_*=\sqrt{\sigma_*/2}$, halving the exponent but preserving power-boundedness. The trace-anomaly source proposed in SCALING_LIMIT/08/04 §4, $\sigma_{\rm anom}=\mathcal K\,(\beta(g)/g)\langle\operatorname{Tr}F^2\rangle$, is likewise a power of $g$ times a condensate; the only way it could evade the no-go is if $\langle\operatorname{Tr}F^2\rangle$ is itself measured in units of $\Lambda^4$, which presupposes the scale one is trying to derive.

**The corpus's own statement of the correct requirement.** POLARITY_GRIBOV/03_misc_docs/12_Entropic_Spark_Conjecture.md §3.3 gets to the right requirement and stops there. Its text runs: it first writes '$\lambda_*=\sqrt{\sigma_0/2}\implies m_{phys}=\frac{\lambda_*}{a}\cdot a=\lambda_*\cdot\frac1a\cdot a=\lambda_*$', then says 'Wait, that's wrong. Let me reconsider the scaling', then derives correctly that $\hat m_*\sim\sqrt\sigma$ and $m_{\rm phys}=\hat m_*/a$, hence '**Refined Conjecture:** the source $\sigma$ scales as $a^2$: $\sigma(a)=\sigma_0a^2\implies m_{\rm phys}=\sqrt{\sigma_0/2}$'. That refined conjecture is exactly the dimensional-transmutation requirement in disguise. Written out with the RG relation it reads
$$\sigma(a)=2m^2a^2=2\Big(\frac{m}{\Lambda_L}\Big)^2\big(b_0g_0^2\big)^{-102/121}\exp\!\Big(-\frac{1}{b_0g_0^2}\Big),$$
i.e. the geometric source would have to be **exponentially small in $1/g_0^2$**, whereas every candidate is $O(1)$ or $O(g_0^2)$. The corpus never performs this substitution. [Attribution: the substitution and the $\chi$ diagnostic are mine; the refined conjecture and the RG relation are standard/corpus material.]

**Remark on the corpus's Lean normalization.** `lean/YangMills/AsymptoticFreedom.lean` defines `beta_0 N := 11*N/3` and `running_coupling b a L := 1/(b * log(1/(a*L)))`, i.e. it uses $g_0^2=1/(\beta_0\log(1/a\Lambda))$ with $\beta_0=11N/3$. This absorbs $16\pi^2$ and a factor 2 relative to the standard $g_0^2=1/(2b_0\log(1/a\Lambda))$ with $b_0=11N/(48\pi^2)$; the two agree up to the redefinition $g^2\mapsto g^2/(16\pi^2)$ and a factor 2, and nothing in the no-go depends on which is used, since $\chi_F\to0$ for any power law in any of these normalizations.

### Constants and numbers

b0 = 11N/(48 pi^2): b0(2)=0.0464388, b0(3)=0.0696577; 1/(2 b0(3)) = 7.17849.
b1 = (34N^2/3)/(16 pi^2)^2: b1(2)=1.817934e-3, b1(3)=4.090352e-3.
b1/(2 b0^2) = 51/121 = 0.42148760 exactly, independent of N.
SU(3): beta = 2N/g0^2 = 0.835893 * ln(1/(a Lambda_L)) at one loop.
Transmutation index chi(g) = -2 b0 g^2 log F(g), SU(3), target m/Lambda = 3:
  g0^2 = 1.00 : chi(required m_hat) = 0.6905 ; chi(nu = sqrt(N/3) g0) = -0.00000
  g0^2 = 0.50 : 0.8249 ; 0.0241
  g0^2 = 0.20 : 0.9192 ; 0.0224
  g0^2 = 0.10 : 0.9555 ; 0.0160
  g0^2 = 0.02 : 0.9892 ; 0.0055
  (chi -> 1 for the true scaling function; chi -> 0 for every power law.)
Required source for the corpus's own 'Refined Conjecture' sigma(a) = 2 m^2 a^2, SU(3), m/Lambda = 3:
  g0^2 = 0.5 (beta = 12): sigma_required = 2*9*(2.398e-6)^2 = 1.04e-10,
  versus sigma_candidate = N/2 = 1.5 (Weyl) or N/6 = 0.5 (Haar) -- a discrepancy of 10 orders of magnitude at beta = 12 alone, growing like exp(1/(b0 g0^2)).

### Code

# chi-diagnostic: chi -> 1 for the true dimensionally-transmuted scaling function,
# chi -> 0 for any power law in g0.  Run: python chi.py
import numpy as np, math
b0 = lambda N: 11.0*N/(48*np.pi**2)
b1 = lambda N: (34.0*N**2/3.0)/(16*np.pi**2)**2
def aL(g2,N):
    B0,B1 = b0(N), b1(N)
    return (B0*g2)**(-B1/(2*B0**2))*np.exp(-1.0/(2*B0*g2))

N, mOverLambda = 3, 3.0
for g2 in (1.0, 0.5, 0.2, 0.1, 0.02):
    chi = lambda F: -2*b0(N)*g2*math.log(F)
    print(f"g0^2={g2:5.2f}  chi(required)={chi(mOverLambda*aL(g2,N)):8.5f}"
          f"  chi(power law nu=sqrt(N/3)g0)={chi(math.sqrt(N/3)*math.sqrt(g2)):8.5f}")

**Caveat.** The argument assumes the continuum gap exists and is a finite multiple of Lambda_L; it is therefore a consistency (reductio) argument about a proof strategy, not an unconditional theorem about Yang-Mills. It also assumes the scaling trajectory is the asymptotically free one -- it says nothing about a hypothetical non-trivial UV fixed point.

**Why it matters.** This is the sharp form of the obstruction and the only part that is chart-independent, mechanism-independent, and quantitative. The index chi(g) is a one-line test any future proposed 'source term' must pass; every candidate in this corpus, and every candidate of the same shape, fails it identically.

---

## 4. Exact Combes-Thomas/Fourier exponent for the matrix hinge on ker d_0*, and its beta^{-1/2} scaling

`status: solid` · `kind: derivation`

### Statement

Work on $\mathbb Z^d$, $d\ge2$ ($d=4$ for lattice YM). Let $\mathcal C^k(\mathbb Z^d;\mathfrak g)$ be $\mathfrak g$-valued $k$-cochains, $d_0$ the discrete gradient, $d_1$ the discrete curl, and $H:=\ker d_0^*\subset\ell^2\mathcal C^1$ the horizontal (divergence-free) sector. Let
$$M:=m^2 I+t\,d_1^*d_1\ \ \text{on }H,\qquad m^2>0,\ t>0,\qquad G:=M^{-1}.$$

**(i) (Scalarization on $\ker d_0^*$.)** With $q_\mu(k)=e^{ik_\mu}-1$ and $\lambda(k)=\sum_\mu|q_\mu(k)|^2=4\sum_\mu\sin^2(k_\mu/2)$, the symbol of $d_1^*d_1$ is $\lambda(k)I-q(k)\otimes\overline{q(k)}$; on $H$ the constraint $\overline{q(k)}\cdot\widehat X(k)=0$ kills the rank-one term, so
$$\widehat{(MX)}(k)=\big(m^2+t\lambda(k)\big)\widehat X(k).$$

**(ii) (Exact axial decay rate.)** The kernel of $G$ decays along a coordinate axis exactly at rate
$$\nu_{\rm exact}(m^2,t)=\operatorname{arcosh}\!\Big(1+\frac{m^2}{2t}\Big)=2\operatorname{arsinh}\!\Big(\frac{m}{2\sqrt t}\Big).$$

**(iii) (Contour-shift bound, the corpus's version.)** The uniform bound obtained by shifting all $d$ momenta simultaneously is
$$\big\|G_{(x,\mu),(y,\nu)}\big\|_{\mathrm{op}}\le\frac{2}{m^2}\,e^{-\nu(m^2,t)|x-y|_1},\qquad \nu(m^2,t)=2\operatorname{arsinh}\!\Big(\frac{m}{\sqrt{8td}}\Big)=\operatorname{arcosh}\!\Big(1+\frac{m^2}{4td}\Big).$$

**(iv) (YM scaling.)** With the lattice-YM hinge constants in the angle chart, $m^2=2N/3$ (Ricci + Haar) and $t=\alpha_W=\beta/N=2/g_0^2$, both exponents are
$$\nu\ =\ c_N\,g_0\,(1+O(g_0^2))\ \asymp\ \beta^{-1/2},\qquad c_N=\sqrt{N/3}\ \text{(exact rate)},\quad c_N=\sqrt{N/(6d)}\ \text{(bound, }d=4).$$
Hence $m_{\rm phys}=\nu/a\asymp g_0(a)/a\asymp 1/(a\sqrt{\log(1/a\Lambda_L)})\to\infty$.

### Derivation

**(i)** $d_1$ acts on a 1-cochain $X$ by $(d_1X)_{p}= X_{\mu}(x)+X_{\nu}(x+\hat\mu)-X_\mu(x+\hat\nu)-X_\nu(x)$ for the plaquette $p=(x,\mu\nu)$; in Fourier variables its symbol is $\widehat{d_1}(k)_{\mu\nu}=q_\mu(k)\delta_\nu-q_\nu(k)\delta_\mu$, whence
$$\widehat{d_1^*d_1}(k)=\Big(\sum_\mu|q_\mu|^2\Big)I-q\otimes\bar q=\lambda(k)I-q\otimes\bar q .$$
The divergence constraint $d_0^*X=0$ reads $\sum_\mu\overline{q_\mu(k)}\widehat X_\mu(k)=0$, i.e. $\bar q\cdot\widehat X=0$, and therefore $(q\otimes\bar q)\widehat X=q(\bar q\cdot\widehat X)=0$. So on $H$ the operator is the *scalar* multiplier $m^2+t\lambda(k)$. This is the step the corpus correctly identifies as the reason it can keep the matrix structure and still get an explicit exponent (WILSON/03_decay_bounds/04 §3).

**(ii)** Write the kernel along the $1$-axis as
$$G(x,0)=\int_{[-\pi,\pi]^d}\frac{e^{ik\cdot x}}{m^2+t\lambda(k)}\,\frac{d^dk}{(2\pi)^d}.$$
Doing the $k_1$ integral by residues, the nearest singularity in the complex $k_1$-plane sits where
$$m^2+t\Big[2(1-\cos k_1)+\textstyle\sum_{\mu\ge2}2(1-\cos k_\mu)\Big]=0,$$
which for $k_2=\dots=k_d=0$ gives $\cos k_1=1+m^2/(2t)$, i.e. $k_1=i\nu$ with $\cosh\nu=1+m^2/(2t)$. Hence the exponential decay rate along the axis is $\nu_{\rm exact}=\operatorname{arcosh}(1+m^2/(2t))$. The identity $\operatorname{arcosh}(1+z)=2\operatorname{arsinh}(\sqrt{z/2})$ gives the second form. For $m^2/t\to0$, $\nu_{\rm exact}=\sqrt{m^2/t}\,(1+O(m^2/t))$.

**(iii)** Shift $k\mapsto k+i\nu s$ with $s_\mu=\pm1$ aligned with $\operatorname{sign}(x_\mu-y_\mu)$. Then
$$\Re\lambda(k+i\nu s)=\sum_\mu 2\big(1-\cos k_\mu\cosh\nu\big)\ \ge\ 2d\,(1-\cosh\nu),$$
so $\Re(m^2+t\lambda)\ge m^2-2td(\cosh\nu-1)$. Demanding $\ge m^2/2$ gives $\cosh\nu-1\le m^2/(4td)$, i.e.
$$\nu=\operatorname{arcosh}\!\Big(1+\frac{m^2}{4td}\Big)=2\operatorname{arsinh}\!\Big(\frac{m}{\sqrt{8td}}\Big),$$
which is eq. (3.1) of WILSON/03_decay_bounds/04. The residual denominator bound $\ge m^2/2$ produces the prefactor $2/m^2$, and the shift produces $e^{-\nu|x-y|_1}$. Note this bound is uniformly worse than (ii) by a factor $\approx\sqrt{2d}$ in the small-$m^2/t$ regime (numerically: $m^2=1,t=100$: exact $0.09996$, bound $0.03535$, ratio $2.83=\sqrt{8}$). Both are $\propto m/\sqrt t$.

**(iv)** Insert the YM constants derived in the Chart-Jacobian Lemma. In the angle chart $m^2=\operatorname{Ric}+\nabla^2S_{\rm Haar}=N/2+N/6=2N/3$ and $t=\alpha_W=\beta/N=2/g_0^2$. Then $m^2/t=Ng_0^2/3$ and
$$\nu_{\rm exact}=\operatorname{arcosh}\Big(1+\tfrac{N g_0^2}{6}\Big)=\sqrt{\tfrac N3}\,g_0+O(g_0^3).$$
With the Haar Jacobian alone ($m^2=N/6$) one gets $\nu=\sqrt{N/12}\,g_0+O(g_0^3)$. Numerically the convergence is fast: for $SU(3)$, $\nu/g_0=0.9046,0.9624,0.9803,0.9939$ at $\beta=2,6,12,40$ against the limit $1$; Haar-only $\nu/g_0=0.4856,0.4949,0.4974,0.4992$ against $1/2$.

Since $\nu$ is a decay rate per lattice step and $\beta=2N/g_0^2$, this is precisely the corpus's own statement that 'the lattice-unit mass behaves like $\beta^{-1/2}$' (WILSON/03_decay_bounds/04 §4), now with the exact constant. Composing with asymptotic freedom, $\beta(a)=4Nb_0\log(1/a\Lambda_L)$, gives
$$m_{\rm phys}(a)=\frac{\nu}{a}=\frac{1}{a}\sqrt{\frac{N}{3}}\Big(2b_0\log\frac{1}{a\Lambda_L}\Big)^{-1/2}\asymp\frac{1}{a\sqrt{\log(1/a\Lambda_L)}}\ \to\ \infty .$$

**Auxiliary constant (used in the Davies/row-sum variant).** The off-diagonal row sum of $d_1^*d_1$ in $d=4$ is exactly $18$ per link. The level-set ("boundary row-sum") refinement $C_\partial\le C_0$ removes only the co-plaquette neighbours at equal distance, an $O(2)$ improvement in $C$, hence $\sqrt2$ in $\nu$; it does not change the $g_0$ scaling. (COMBES_THOMAS/MAXWELL_GREEN/24_Davies_Resolvent_Decay.md uses $D_E\approx6$ instead of $18$ and its illustrative $\xi\approx8$ is wrong.)

### Constants and numbers

nu_exact(m^2,t) = arcosh(1 + m^2/(2t)) = 2 arsinh(m/(2 sqrt t)).
nu_bound(m^2,t,d) = 2 arsinh(m / sqrt(8 t d)) = arcosh(1 + m^2/(4 t d)); prefactor 2/m^2.
Comparison (d = 4):
  m^2=2.0,  t=1     : exact 1.31696, bound 0.49493, sqrt(m^2/t) 1.41421
  m^2=1.0,  t=10    : exact 0.31492, bound 0.11175, sqrt(m^2/t) 0.31623
  m^2=1.0,  t=100   : exact 0.09996, bound 0.03535, sqrt(m^2/t) 0.10000
  m^2=0.5,  t=1000  : exact 0.02236, bound 0.00791, sqrt(m^2/t) 0.02236
YM hinge, angle chart: m^2 = 2N/3 (Ric+Haar) or N/6 (Haar only); t = alpha_W = beta/N = 2/g0^2.
m^2/t = N g0^2 / 3 (Ric+Haar), N g0^2 / 12 (Haar only) -- chart invariant.
nu / g0 -> sqrt(N/3) = 0.8165 (SU(2)), 1.0000 (SU(3)) for Ric+Haar;
           sqrt(N/12) = 0.4082 (SU(2)), 0.5000 (SU(3)) for Haar only.
Corpus's own parameters (m^2 = c_H/2, t = beta/3, d = 4) give nu = 2 arsinh(sqrt3 sqrt(c_H)/(4 sqrt(beta) sqrt d)) ~ sqrt3 sqrt(c_H)/(2 sqrt(beta d)); with c_H = N/6, beta = 2N/g0^2, d = 4 this is g0/8 exactly in the small-g0 limit, independent of N.
Off-diagonal row sum of d1* d1 in d = 4: 18 per link (exact).

### Code

import math
nu_exact  = lambda m2,t   : math.acosh(1 + m2/(2*t))
nu_bound  = lambda m2,t,d : 2*math.asinh(math.sqrt(m2)/math.sqrt(8*t*d))

for N in (2,3):
    for beta in (2,6,12,40):
        g2 = 2*N/beta; t = beta/N
        for lab, m2 in (("Haar only", N/6.0), ("Ric+Haar", 2*N/3.0)):
            nu = nu_exact(m2,t)
            print(f"SU({N}) beta={beta:3} g0^2={g2:6.3f} {lab:10} "
                  f"m^2={m2:6.3f} t={t:7.3f} m^2/t={m2/t:8.4f} "
                  f"nu={nu:8.5f} nu/g0={nu/math.sqrt(g2):7.4f}")

**Caveat.** The hinge Ric_mu >= m_H^2 I + alpha_W d_1* d_1 is only established near the vacuum / on a small-field 'good set'; the corpus's typicality claim for that set is separately false (each link's marginal under any gauge-invariant measure is exactly Haar). The exponent computation itself is unconditional linear algebra and does not depend on that.

**Why it matters.** This supplies the exact constant in front of the beta^{-1/2} that the corpus stops one arithmetic step short of, and it is the chart-invariant route: it shows the pipeline's answer is a cutoff-scale mass of size g_0(a)/a for reasons that survive every change of coordinates.

---

## 5. The Weyl-denominator source sigma_geom: correct constant N/2, and its exact decomposition into a coordinate (Vandermonde) singularity plus the a-independent Haar residue N/6

`status: solid` · `kind: theorem`

### Statement

Let $G=SU(N)$, $T$ a maximal torus, $W=S_N$, and eigenangle coordinates $\theta=(\theta_1,\dots,\theta_N)$, $\sum_i\theta_i=0$, $t(\theta)=\mathrm{diag}(e^{i\theta_1},\dots,e^{i\theta_N})$. Let
$$|\Delta(\theta)|^2=\prod_{i<j}4\sin^2\frac{\theta_i-\theta_j}{2},\qquad S_{\rm geom}(\theta):=-\log|\Delta(\theta)|^2 .$$

**(a) (Universality of the Jacobian; corpus Theorem 2.)** For any probability measure $\mu=\rho\,dg$ on $G$ whose density $\rho$ is a class function, the pushforward $\nu=\pi_*\mu$ to conjugacy classes $T/W$ has density $\rho(t(\theta))|\Delta(\theta)|^2/Z$ with respect to $d\theta$. In particular the factor $|\Delta|^2$ is independent of $\rho$, hence independent of any RG/smoothing scale; if $\rho_t=\rho_0*K_t$ evolves by heat-kernel convolution, $d\nu_t\propto\rho_t(t(\theta))|\Delta(\theta)|^2d\theta$ for every $t\ge0$.

**(b) (Hessian is a weighted complete-graph Laplacian.)** On the regular set,
$$\delta^2S_{\rm geom}(\theta)[x,x]=\tfrac12\sum_{i<j}\csc^2\!\Big(\tfrac{\theta_i-\theta_j}{2}\Big)(x_i-x_j)^2,\qquad \nabla^2S_{\rm geom}=\tfrac12L_{w(\theta)},\ \ w_{ij}=\csc^2\tfrac{\theta_i-\theta_j}{2}.$$

**(c) (Correct constant.)** Since $\csc^2\ge1$ and $\sum_{i<j}(x_i-x_j)^2=N\|x\|^2$ on $\sum_ix_i=0$,
$$\nabla^2S_{\rm geom}\big|_{\sum x_i=0}\ \succeq\ \frac N2\,I .$$
The value $N/4$ quoted in SCALING_LIMIT/08/05 is a factor-2 slip inconsistent with the Hessian entries stated in that same file; $N/4$ is correct only for the *one-power* potential $S_{\rm Weyl}=-\log|\Delta|$ (as the heat-kernel note 07 §5 remarks).

**(d) (Exact decomposition -- this is the point.)** Let $u_{ij}=(\theta_i-\theta_j)/2$ and let $S_H=-\log J$ be the Haar/exponential-map potential on the Cartan. Then, *exactly*,
$$S_{\rm geom}(\theta)=S_H(\theta)-2\sum_{i<j}\log|u_{ij}|+\text{const},$$
and correspondingly
$$\underbrace{\tfrac12\sum_{i<j}\csc^2u_{ij}\,(x_i-x_j)^2}_{\nabla^2S_{\rm geom}}=\underbrace{\tfrac12\sum_{i<j}\Big(\csc^2u_{ij}-\tfrac1{u_{ij}^2}\Big)(x_i-x_j)^2}_{\nabla^2S_H\ \to\ (N/6)\|x\|^2\ \text{as}\ \theta\to0}\ +\ \underbrace{\tfrac12\sum_{i<j}\tfrac{(x_i-x_j)^2}{u_{ij}^2}}_{\text{Vandermonde/radial coordinate Jacobian}} .$$
The second term diverges as $\theta\to0$ (like $2/u_{ij}^2$) and is a coordinate artifact of eigenangle coordinates -- it is the Jacobian of passing from the $(N-1)$-dimensional Cartan to the radial variables, and is exactly cancelled by the vanishing of the density $|\Delta|^2$ there. The **genuine, scale-independent geometric residue** is the first term, whose value at the vacuum is $\kappa_G/3=N/6$ -- i.e. it is the same object as the 'Haar mass'.

**(e) (Consequence for the scaling dichotomy.)** Since $\theta=ag_0\cdot(\text{physical field})$, the residue carries the factor $(ag_0)^2$ exactly as in the Chart-Jacobian Lemma. So $\sigma_{\rm geom}$ is not a *new*, $a$-independent source: it is the same $\kappa_G/3$ (plus a coordinate singularity), and it falls into horn (H1)/(H2) of the scaling dichotomy.

### Derivation

**(a)** For $\varphi$ bounded on $T/W$, $\varphi\circ\pi$ is a class function on $G$, so Weyl's integration formula gives
$$\int_{T/W}\varphi\,d\nu=\int_G\varphi(\pi(g))\rho(g)dg=\frac1{|W|}\int_T\varphi(\theta)\rho(t(\theta))|\Delta(\theta)|^2d\theta,$$
which identifies the density. The heat-kernel corollary follows because $K_t$ is central ($K_t(hgh^{-1})=K_t(g)$) and convolution of central densities is central, so $\rho_t$ is a class function for every $t$; the semigroup property $K_s*K_t=K_{s+t}$ then makes blocking of $L$ independent heat-smeared links into a block holonomy amount to $t\mapsto Lt$, leaving $|\Delta|^2$ untouched. (This is the corpus's Theorem 2 / Corollary 3 in UNIFORMITY_ASYMPTOTIC_FREEDOM/07; the proof is correct as written.)

**(b)** $S_{\rm geom}=-2\sum_{i<j}\log|2\sin u_{ij}|$. Along $\theta\mapsto\theta+tx$, $\dot u_{ij}=(x_i-x_j)/2$ and
$$\frac{d}{dt}\big(-2\log\sin u\big)=-2\cot(u)\,\dot u,\qquad \frac{d^2}{dt^2}=2\csc^2(u)\,\dot u^2=\tfrac12\csc^2(u)(x_i-x_j)^2 .$$
Summing over $i<j$ gives the stated quadratic form. Its matrix entries are $\partial^2_{ij}S_{\rm geom}=-\tfrac12w_{ij}$ ($i\ne j$), $\partial^2_{ii}S_{\rm geom}=\tfrac12\sum_{k\ne i}w_{ik}$, i.e. $\tfrac12L_{w}$ -- exactly the entries stated in SCALING_LIMIT/08/05 §2; and $x^\top(\tfrac12L_w)x=\tfrac12\sum_{i<j}w_{ij}(x_i-x_j)^2$, which is why the '$\tfrac14$' on the next line of that file is a slip.

**(c)** $\csc^2\ge1$ everywhere finite, and $\sum_{i<j}(x_i-x_j)^2=N\sum_ix_i^2-(\sum_ix_i)^2=N\|x\|^2$ on the constraint plane. Hence $\delta^2S_{\rm geom}\ge\tfrac12N\|x\|^2$. Numerically, minimizing $\delta^2S_{\rm geom}[x,x]/\|x\|^2$ over $2\times10^4$ random $(\theta,x)$ pairs gives $1.0000$ for $SU(2)$ and $1.5027$ for $SU(3)$, matching $N/2=1,1.5$; for $N=4,5$ the sampled minima ($2.14,2.93$) exceed $N/2=2,2.5$, since not all pairs can be maximally separated simultaneously -- so $N/2$ is a valid, and for $N\le3$ sharp, lower bound.

**(d)** From the Chart-Jacobian Lemma Step 7, on the Cartan
$$J(X)=\prod_{i<j}\Big(\frac{\sin u_{ij}}{u_{ij}}\Big)^2\ \Longrightarrow\ S_H=-2\sum_{i<j}\log\frac{\sin u_{ij}}{u_{ij}}=-2\sum_{i<j}\log\sin u_{ij}+2\sum_{i<j}\log u_{ij},$$
while $S_{\rm geom}=-2\sum_{i<j}\log\sin u_{ij}-\tfrac{N(N-1)}{2}\log4$. Subtracting gives the stated identity. Differentiating the extra term twice: $\frac{d^2}{dt^2}(-2\log u)=2\dot u^2/u^2=\tfrac12(x_i-x_j)^2/u^2$. Using $\csc^2u-u^{-2}\to\tfrac13$ as $u\to0$,
$$\nabla^2S_H(0)\big|_{\rm Cartan}[x,x]=\tfrac12\cdot\tfrac13\sum_{i<j}(x_i-x_j)^2=\tfrac N6\|x\|^2 ,$$
confirming $\nabla^2S_H(0)=(N/6)\mathrm{Id}=(\kappa_G/3)\mathrm{Id}$ once more, now purely from the Weyl denominator. [The decomposition (d) and this consequence are mine; the corpus states (a),(b),(c) but never subtracts the Vandermonde part and therefore never notices that the 'new scale-independent source' is the old Haar constant.]

**(e)** The residue is a Hessian with respect to $\theta$ (the angle chart). Under $\theta=ag_0A$ it becomes $(ag_0)^2(N/6)$, exactly horn (H2). The divergent Vandermonde part cannot be used as a convexity source in any invariant sense, because (i) it is not a Hessian of a term in the action -- it is the Jacobian of the coordinates chosen -- and (ii) it is multiplied by a density that vanishes to matching order there, so the measure $e^{-S_{\rm geom}}d\theta=|\Delta|^2d\theta$ is perfectly regular at $\theta=0$.

### Constants and numbers

sigma_geom = N/2 for S_geom = -log|Delta|^2 in eigenangle coordinates with the Euclidean metric sum d theta_i^2 (which IS the restriction of <X,Y> = -Tr XY under X = i diag(theta)).
  SU(2): 1 ; SU(3): 1.5 ; SU(4): 2 ; SU(5): 2.5.
  Numerical min over 2e4 random (theta,x): 1.0000 (N=2), 1.5027 (N=3), 2.1390 (N=4), 2.9337 (N=5).
N/4 (the value in SCALING_LIMIT/08/05) is the constant for S_Weyl = -log|Delta| (one power).
Vandermonde divergence: for SU(3), theta = (eps, 0, -eps), x = (1,-1,0)/sqrt2, d^2 S_geom = 5.25/eps^2 exactly:
  eps = 1e-1: 5.2550e2 ; 1e-2: 5.2501e4 ; 1e-3: 5.2500e6.
Regular residue at theta -> 0: csc^2(u) - 1/u^2 -> 1/3, giving Hess S_H(0)|_Cartan = (N/6) I:
  SU(2) 0.33333, SU(3) 0.50000, SU(4) 0.66667, SU(5) 0.83333 (finite differences, 5 decimals).

### Code

import numpy as np, math

def q_Sgeom(theta, x):            # delta^2 S_geom [x,x] = (1/2) sum_{i<j} csc^2(u) (x_i-x_j)^2
    s = 0.0; N = len(theta)
    for i in range(N):
        for j in range(i+1, N):
            u = (theta[i]-theta[j])/2.0
            s += 0.5/math.sin(u)**2 * (x[i]-x[j])**2
    return s

def q_SH(theta, x):               # the regular residue: csc^2(u) - 1/u^2
    s = 0.0; N = len(theta)
    for i in range(N):
        for j in range(i+1, N):
            u = (theta[i]-theta[j])/2.0
            s += 0.5*(1.0/math.sin(u)**2 - 1.0/u**2) * (x[i]-x[j])**2
    return s

rng = np.random.default_rng(0)
for N in (2,3,4,5):
    worst = 1e9
    for _ in range(20000):
        th = rng.uniform(-math.pi, math.pi, N); th -= th.mean()
        x  = rng.normal(size=N); x -= x.mean(); x /= np.linalg.norm(x)
        worst = min(worst, q_Sgeom(th, x))
    th = 1e-4*np.arange(N); th -= th.mean()
    x  = rng.normal(size=N); x -= x.mean(); x /= np.linalg.norm(x)
    print(f"SU({N}): inf d^2 S_geom = {worst:.4f} (bound N/2 = {N/2});  "
          f"residue at theta~0 = {q_SH(th,x):.5f} (N/6 = {N/6:.5f})")

**Caveat.** Part (a) is a statement about a single link holonomy / single block holonomy. Extending it to a lattice orbit space with shared links and Bianchi constraints is genuinely open; the corpus lists this as 'next technical target 1' and does not do it.

**Why it matters.** This is the load-bearing repair of the folder's headline result. The Weyl integration formula and the N/2 bound are correct mathematics; the decomposition shows the 'scale-independent geometric source' is not a new mechanism but the Haar constant plus a coordinate singularity, which closes the last escape route from the scaling dichotomy.

---

## 6. Chart-consistent finite-cutoff convexity window: beta < N^2/9, and the global Bakry-Emery constant -> -infinity

`status: solid` · `kind: theorem`

### Statement

Let $\mathcal C=SU(N)^{|B|}$ with the bi-invariant product metric, $S_{\rm eff}=\beta S_W+S_{\rm Haar}$, $S_W=\sum_p(1-\tfrac1N\Re\operatorname{Tr}U_p)$, $d=4$.

**(a) (Wilson Hessian bound.)** For a single-link variation, $|S_p''(0)|\le\tfrac1N\|X\|^2$ per plaquette; each link lies in $2(d-1)=6$ plaquettes, so $\|\nabla^2S_W\|_{\rm op}\le C_V(N)$ with $C_V(N)=6/N$ (single-link) or, allowing all four links of a plaquette to vary, $C_V(N)=24/N$.

**(b) (Chart-consistent window.)** Computing **both** terms in the angle chart, where $\nabla^2S_{\rm Haar}(0)=(N/6)I$ and $\operatorname{Ric}=(N/2)I$,
$$\operatorname{Ric}+\nabla^2S_{\rm eff}\ \succeq\ \Big(\frac{2N}{3}-\beta\,C_V(N)\Big)I ,$$
so uniform convexity holds iff
$$\boxed{\ \beta<\frac{2N}{3C_V(N)}\ }=\begin{cases}N^2/9,&C_V=6/N,\\ N^2/36,&C_V=24/N.\end{cases}$$
This condition contains **no** $a$ and no $g$-power. Dropping Ricci and keeping only the Haar Jacobian gives $\beta<N^2/36$ resp. $N^2/144$.

By contrast, the corpus's window $\rho_*(a)=c_0a^2g^2-\beta C_V(N)>0$, i.e. $g^4>288/(Na^2)$ (RECOMMENDED_01 Thm 4.1) or $g^4>12/(c_0a^2)$ (lemma_unity §5), is dimensionally inhomogeneous: $g$ is dimensionless in $d=4$ while $a$ is a length. It is the direct symptom of adding an $A$-chart Hessian to an $X$-chart Hessian.

**(c) (The window closes before the scaling window opens.)** For $SU(3)$ the chart-consistent window is $\beta<1$ (or $\beta<0.25$ with the conservative $C_V$), while the asymptotic-scaling window used in lattice practice is $\beta\gtrsim5.5$ and the continuum limit requires $\beta\to\infty$. So there is no overlap, at any $a$.

**(d) (Sharp global obstruction.)** Take $U_0=\mathrm{diag}(-1,-1,1,\dots,1)\in SU(N)$ and $X\in\mathfrak{su}(N)$ supported in the upper-left $2\times2$ block with $X^2=-\tfrac12I_2$ there and $\|X\|^2=-\operatorname{Tr}X^2=1$ (e.g. $X=\sqrt2\,i\sigma_3/2$). Then
$$\frac{d^2}{dt^2}\Big|_{t=0}S_p(e^{tX}U_0)=-\frac1N\Re\operatorname{Tr}(X^2U_0)=-\frac1N .$$
Hence $\inf_U\lambda_{\min}(\nabla^2S_W(U))\le-1/N$ and the global Bakry-Emery constant obeys
$$\rho_{\rm BE}(\beta)\ \le\ \frac N2-\frac{\beta}{N}\ \xrightarrow[\beta\to\infty]{}\ -\infty .$$
So no *global* $CD(\rho,\infty)$ bound with $\rho>0$ can survive $\beta\to\infty$, independently of the chart question.

### Derivation

**(a)** Vary one link: $U_p(t)=\cdots e^{tX}V\cdots$, so $S_p''(0)=-\tfrac1N\Re\operatorname{Tr}(X^2U_p)$. With $H:=-X^2\succeq0$ and von Neumann's trace inequality, $|\operatorname{Tr}(HU_p)|\le\sum_i\sigma_i(H)\sigma_i(U_p)=\operatorname{Tr}H=\|X\|^2$ (the singular values of a unitary are all $1$). So $|S_p''(0)|\le\|X\|^2/N$. In $d=4$ a link belongs to $2(d-1)=6$ plaquettes, giving $C_V=6/N$. If instead all four links of a plaquette are varied, expanding $U_p''(0)=\sum_i(\cdots X_i^2V_i\cdots)+\sum_{i\ne j}(\cdots X_iV_i\cdots X_jV_j\cdots)$ and bounding each term gives $|S_p''(0)|\le\tfrac1N(\sum_i\|X_i\|)^2\le\tfrac4N\sum_i\|X_i\|^2$, hence $C_V=24/N$ after summing $6$ plaquettes per link.

**(b)** In the angle chart, $\langle X,\nabla^2S_{\rm eff}X\rangle\ge(N/6)\|X\|^2-\beta C_V\|X\|^2$; adding $\operatorname{Ric}\succeq(N/2)I$ gives $\operatorname{Ric}_\mu\succeq(2N/3-\beta C_V)I$. Positivity is $\beta<2N/(3C_V)$. With $C_V=6/N$ this is $\beta<2N^2/18=N^2/9$; with $C_V=24/N$, $\beta<2N^2/72=N^2/36$.
[Attribution: the chart-consistent window is mine; the corpus computes $\rho_*=c_0a^2g^2-\beta C_V$, mixing charts.]

**(c)** $N^2/9$: $SU(2)\Rightarrow0.444$, $SU(3)\Rightarrow1$. $N^2/36$: $SU(2)\Rightarrow0.111$, $SU(3)\Rightarrow0.25$. Haar-only versions: $N^2/36$ and $N^2/144$, i.e. $\le0.25$. Standard $SU(3)$ scaling-window simulations run at $\beta\in[5.7,6.5]$ and higher; the two ranges are disjoint by an order of magnitude.

**(d)** With $U_0$ as stated, on the $2\times2$ block $U_0=-I_2$ and $X^2=-\tfrac12I_2$, so $X^2U_0=(-\tfrac12I_2)(-I_2)=+\tfrac12I_2$ with trace $1$; all other blocks contribute $0$ because $X$ vanishes there. Hence $\Re\operatorname{Tr}(X^2U_0)=1$ and $S_p''(0)=-1/N$. Because $\operatorname{Ric}$ is bounded above on the compact $\mathcal C$ by $\kappa_{\max}=N/2$ (bi-invariant metric on a simple group has constant Ricci), evaluating the Bakry-Emery form at $(U_0,X)$ gives $\rho_{\rm BE}\le N/2-\beta/N$.
(This is Lemma 2.1 / Corollary 2.2 of WILSON/05_proofs_reports/RECOMMENDED_02, reproduced verbatim in content; it is correct.)

**Relation to the scaling dichotomy.** (d) is a *different* obstruction from the dichotomy: it says the finite-cutoff mechanism itself has a $\beta$-window and the window is $\beta=O(1)$. The dichotomy says that *even if* one had a positive floor at all $\beta$ (by localization onto a good set, say), the resulting mass would be $\nu/a$ with $\nu$ a power of $g_0$, hence not $\Lambda$. The two obstructions are independent and both must be defeated.

**Companion: the discrete Riccati budget.** The corpus's block-marginalization lemma is correct and worth recording. If $\nabla^2S(x,y)=\begin{pmatrix}A&B\\B^\top&C\end{pmatrix}$ with $A\succeq\alpha I$, $C\succeq\gamma I>0$, $\|B\|\le M$, and $e^{-S_{\rm coarse}(x)}=\int e^{-S(x,y)}dy$, then $\nabla^2_xS_{\rm coarse}=\mathbb E[A]-\operatorname{Cov}(\nabla_xS)$ and Brascamp-Lieb gives $\operatorname{Cov}\preceq M^2/\gamma$, so
$$\nabla^2_xS_{\rm coarse}\succeq\Big(\alpha-\frac{M^2}{\gamma}\Big)I,\qquad \rho_{k+1}\ge\rho_k-\frac{M_k^2}{\rho_k},\qquad \rho_k^2\ge\rho_0^2-2\sum_{j<k}M_j^2 .$$
With $M=\beta C_V$ and $\alpha=\gamma=\rho_*$ this halves the window again ($\rho_*>\beta C_V$, i.e. $\beta<N/(3C_V)$, e.g. $\beta<N^2/18$ for $C_V=6/N$).

### Constants and numbers

C_V(N) = 6/N (single-link variation) or 24/N (all four links of a plaquette).
Witness for negativity: U_0 = diag(-1,-1,1,...,1), X = sqrt2 * i sigma_3/2 in the upper-left block, ||X||^2 = 1, S_p''(0) = -1/N (exact).
Global BE upper bound: rho_BE(beta) <= N/2 - beta/N.
Chart-consistent convexity windows (a-free):
  Ric + Haar, C_V = 6/N : beta < N^2/9   -> SU(2) 0.4444, SU(3) 1.0000
  Ric + Haar, C_V = 24/N: beta < N^2/36  -> SU(2) 0.1111, SU(3) 0.2500
  Haar only,  C_V = 6/N : beta < N^2/36  -> SU(2) 0.1111, SU(3) 0.2500
  Haar only,  C_V = 24/N: beta < N^2/144 -> SU(2) 0.0278, SU(3) 0.0625
RG-stable subwindow (rho_* > M = beta C_V): halves the above, e.g. beta < N^2/18 = 0.5 for SU(3) with C_V = 6/N.
Corpus versions for comparison: rho_*(a) = (N/6) a^2 g^2 - 48/g^2 with C_V = 24/N (RECOMMENDED_01), window g^4 > 288/(N a^2); and rho_*(a,g) = c_0 a^2 g^2 - 12/g^2 with C_V = 6/N (lemma_unity), window g^4 > 12/(c_0 a^2). Both are dimensionally inhomogeneous.
Scaling window in practice: SU(3) lattice simulations use beta = 5.7-6.5 and above; the convexity window is beta <= 1.

**Caveat.** Part (b) is a bound on the global infimum near the vacuum only if the O(||X||^2) corrections to the Haar Hessian are controlled; away from the vacuum the Haar Hessian is still positive on SU(N) (it is the Hessian of -log(sin/id) type functions, convex on the alcove) but the constant N/6 is only guaranteed in a normal neighbourhood.

**Why it matters.** It gives the honest, dimensionally consistent version of the corpus's headline finite-cutoff theorem, and the number is stark: the convexity window is beta < 1, entirely inside strong coupling. Together with (d) it shows the mechanism has no overlap with the scaling window even before the continuum question is asked.

---

## 7. Heat-kernel coarse-graining cannot supply a constant positive Riccati source: ergodicity forces sigma_0 = 0

`status: solid` · `kind: obstruction`

### Statement

Let $(M,g)$ be a compact, connected Riemannian manifold without boundary (e.g. $M=\mathcal C=SU(N)^{|B|}$ with the bi-invariant product metric), and let $\rho_t$ solve the heat equation $\partial_t\rho_t=\Delta\rho_t$ with smooth positive initial density $\rho_0$, $\int\rho_0\,d\mathrm{vol}=1$. Write $S_t:=-\log\rho_t$ and $\lambda(t,x):=\lambda_{\min}\big(\nabla^2S_t(x)\big)$.

**(i)** $\rho_t\to1/\mathrm{vol}(M)$ in $C^k(M)$ for every $k$, exponentially fast at rate $\lambda_1(-\Delta)>0$. Hence $S_t\to\log\mathrm{vol}(M)$ in $C^k$, so $\nabla^2S_t\to0$ uniformly and $\displaystyle\lim_{t\to\infty}\ \min_{x\in M}\lambda(t,x)=0$.

**(ii)** Suppose that for some $\alpha>0$ and some constant $\sigma_0\ge0$ the differential inequality
$$\partial_t\lambda\ \ge\ \Delta\lambda-\langle b_t,\nabla\lambda\rangle-\alpha\lambda^2+\sigma_0$$
holds in the viscosity sense on $[0,\infty)\times M$ for some locally bounded vector field $b_t$ (this is the form asserted in UNIFORMITY_ASYMPTOTIC_FREEDOM/01_pillarL §4.2, 06_Riccati_Convexity_Attractor §2, and SCALING_LIMIT/08/04 §3). Then $\sigma_0=0$.

Equivalently: on the specific flow the corpus uses to model coarse-graining -- heat flow on the compact configuration manifold -- there is no constant positive geometric source, and the Riccati attractor $\lambda_*=\sqrt{\sigma_0/\alpha}$ is $0$.

### Derivation

**(i)** Expand $\rho_0-\mathrm{vol}(M)^{-1}$ in the $L^2$ eigenbasis of $-\Delta$ on $M$. Since $M$ is compact and connected, $0$ is a simple eigenvalue with constant eigenfunction, and $\lambda_1:=\lambda_1(-\Delta)>0$. Then
$$\|\rho_t-\mathrm{vol}(M)^{-1}\|_{L^2}\le e^{-\lambda_1 t}\|\rho_0-\mathrm{vol}(M)^{-1}\|_{L^2}.$$
Parabolic (Schauder / hypercontractive) regularity upgrades $L^2$-convergence to $C^k$-convergence for every $k$, with the same exponential rate up to constants: $\|\rho_t-\mathrm{vol}(M)^{-1}\|_{C^k}\le C_k e^{-\lambda_1(t-1)}$ for $t\ge1$. Since $\rho_0>0$ and $\rho_t\to\mathrm{vol}(M)^{-1}>0$ uniformly, $\rho_t$ is bounded away from $0$ for large $t$, so $S_t=-\log\rho_t$ converges in $C^k$ to the constant $\log\mathrm{vol}(M)$, and therefore $\|\nabla^2S_t\|_{C^0}\to0$. In particular $\min_x\lambda(t,x)\to0$.

**(ii)** Suppose $\sigma_0>0$ and set $\ell_*:=\sqrt{\sigma_0/\alpha}$. Let $\Lambda(t):=\min_{x\in M}\lambda(t,x)$. At a point $x_t$ realizing the minimum, $\Delta\lambda\ge0$ and $\nabla\lambda=0$, so by the standard first-variation/viscosity argument for minima of a continuous family (Hamilton's trick),
$$\frac{d^-}{dt}\Lambda(t)\ \ge\ -\alpha\Lambda(t)^2+\sigma_0 \qquad\text{(lower Dini derivative)}.$$
By (i) there is $t_0$ with $|\Lambda(t_0)|<\ell_*$. Compare with the ODE $\dot\ell=-\alpha\ell^2+\sigma_0$, $\ell(t_0)=\Lambda(t_0)\in(-\ell_*,\ell_*)$. Its explicit solution is $\ell(t)=\ell_*\tanh\big(\alpha\ell_*(t-t_0)+\operatorname{artanh}(\Lambda(t_0)/\ell_*)\big)$, which increases monotonically to $\ell_*$. By the comparison principle $\Lambda(t)\ge\ell(t)$ for $t\ge t_0$, so
$$\liminf_{t\to\infty}\Lambda(t)\ \ge\ \ell_*=\sqrt{\sigma_0/\alpha}>0,$$
contradicting $\Lambda(t)\to0$ from (i). Hence $\sigma_0=0$. $\square$

**Consistency check with the corpus's own Gaussian example.** SCALING_LIMIT/08/04 §2 and lemma_unity §2.3 both note that for Gaussian initial data on $\mathbb R^n$ the exact solution is $\lambda_i(t)=\lambda_i(0)/(1+2t\lambda_i(0))\sim1/(2t)\to0$, i.e. $\dot\lambda=-2\lambda^2$ with $\sigma_0=0$. The theorem above says this is not an accident of Gaussianity but a consequence of ergodicity on any compact manifold. The corpus's proposed repair -- 'intrinsic positive Ricci curvature of the compact group factors contributes additively to the eigenvalue lower bound' (01_pillarL §5 Step C) -- cannot be right as stated, because the Ricci curvature is exactly what makes the heat semigroup ergodic and drives $\nabla^2S_t\to0$.

**Scope.** This refutes the constant-source Riccati mechanism *for heat-kernel coarse-graining on the compact configuration manifold*, which is the only flow the corpus writes down concretely. A different (unspecified) flow -- one that is not a Markov semigroup with the uniform measure as its invariant state, e.g. a genuine Wilsonian RG map with a rescaling step -- is not covered. But note that any Markov coarse-graining whose invariant measure is Haar has the same defect, and any flow whose invariant measure is the *interacting* Gibbs measure has $\nabla^2S_\infty=\nabla^2S_{\rm eff}$, i.e. the fixed point is the original problem. [Attribution: CAND-003 states the two-line version; the comparison/viscosity argument, the choice of $t_0$, and the scope discussion are mine.]

### Constants and numbers

Riccati ODE lambda' = -alpha lambda^2 + sigma_0: fixed point lambda_* = sqrt(sigma_0/alpha); with the corpus's normalization alpha = 2, lambda_* = sqrt(sigma_0/2).
Explicit solution from lambda(0) = 0: lambda(t) = sqrt(sigma/2) tanh(t sqrt(2 sigma)); linearized decay rate at the fixed point is -2 sqrt(2 sigma) (corpus 06_Riccati_Convexity_Attractor §3-4; the algebra there is correct).
Heat-flow decay rate: lambda_1(-Delta) on SU(N)^{|B|} with the bi-invariant metric is the smallest nonzero Casimir eigenvalue, = N for SU(N) in the normalization <X,Y> = -Tr XY (fundamental representation Casimir); it is volume-independent, so the convergence rho_t -> uniform is uniform in |B| per link but the mixing time in the product is the same.
Gaussian benchmark: lambda_i(t) = lambda_i(0)/(1 + 2 t lambda_i(0)) ~ 1/(2t).
Corpus's claimed numerical target: lambda_* ~ 0.3 in lattice units on a 4^4 lattice at beta = 2.3, from sigma = c_H = 1/6 (06_Riccati_Convexity_Attractor §7). Note sqrt(c_H/2) = sqrt(1/12) = 0.289, so the claimed number is internally consistent -- but by the theorem above it cannot be produced by the heat flow they specify.

**Caveat.** The argument assumes the inequality is asserted with a constant sigma_0 on all of [0,infinity); a time-decaying source sigma(t) with integral behaviour is not excluded (the corpus itself notes in 06 §5.3 that sigma(t) = sigma_0 e^{-gamma t} survives iff gamma < 2 sqrt(2 sigma_0)) -- but a decaying source cannot produce an a-independent floor either.

**Why it matters.** It closes the last dynamical escape route. The corpus's answer to the scaling dichotomy is 'the flow injects a scale-free positive source'; on the only flow it writes down, ergodicity forces that source to vanish. Anyone continuing this line must first exhibit a coarse-graining map that is not ergodic to Haar.

---

## 8. Reproducible scaling table: the pipeline mass versus the true scaling function, SU(2) and SU(3)

`status: solid` · `kind: numerical_result`

### Statement

Along the two-loop asymptotic-scaling trajectory $a\Lambda_L=(b_0g_0^2)^{-51/121}e^{-1/(2b_0g_0^2)}$ with $b_0=11N/(48\pi^2)$, the convexity pipeline's lattice-unit gap $\nu=\sqrt{N/3}\,g_0$ (the exact Combes-Thomas exponent for the Ricci+Haar hinge) gives a physical mass $m_{\rm pipe}=\nu/a$ whose ratio to $\Lambda_L$ diverges as tabulated. The correct target ($m/\Lambda_L$ a fixed $O(1)$ number, e.g. $\approx3$ for the $0^{++}$ glueball in $\Lambda_L$ units) is missed by a factor that grows like $e^{1/(2b_0g_0^2)}$: from $\times1.4\cdot10^2$ at $\beta=6$ to $\times7\cdot10^{49}$ at $\beta=100$ for $SU(3)$.

### Derivation

Compose three exact ingredients:
1. the chart-invariant hinge ratio $m_H^2/\alpha_W=Ng_0^2/3$ (Chart-Jacobian Lemma + Wilson Hessian $=(\beta/N)d_1^*d_1$);
2. the exact axial Green's-function exponent $\nu=\operatorname{arcosh}(1+m_H^2/(2\alpha_W))$, which for small $g_0$ is $\sqrt{N/3}\,g_0$;
3. the two-loop lattice scaling relation for $a\Lambda_L$.
Then $m_{\rm pipe}/\Lambda_L=\nu/(a\Lambda_L)$. The exponent $b_1/(2b_0^2)=51/121$ is $N$-independent because $b_1/b_0^2=(34N^2/3)/(16\pi^2)^2\cdot(48\pi^2/(11N))^2=34\cdot48^2/(3\cdot256\cdot121)=102/121$.
The interesting feature of the table is that at $\beta\approx6$ (SU(3)) the pipeline exponent is $\nu\approx1$, i.e. a correlation length of exactly one lattice spacing -- close enough to the physically measured $a m_{0^{++}}\approx0.5$-$1$ at that coupling that the failure is invisible at a single $\beta$. The failure only shows up when $\beta$ is varied, because $\nu$ decreases like $\beta^{-1/2}$ while $a$ decreases like $e^{-\beta/(4Nb_0)}$.

### Constants and numbers

SU(3), b0 = 0.0696577, b1 = 4.090352e-3, b1/(2b0^2) = 0.4214876, target m/Lambda_L = 3:
  beta   g0^2     nu       a*Lambda_L    m_pipe/Lambda_L   overshoot
     6   1.0000   1.0000   2.3461e-03    4.2623e+02        1.42e+02
     8   0.7500   0.8660   2.4205e-04    3.5779e+03        1.19e+03
    12   0.5000   0.7071   2.3984e-06    2.9483e+05        9.83e+04
    20   0.3000   0.5477   2.0749e-10    2.6398e+09        8.80e+08
    40   0.1500   0.3873   1.1293e-20    3.4296e+19        1.14e+19
   100   0.0600   0.2449   1.1152e-51    2.1965e+50        7.32e+49
SU(2), b0 = 0.0464388, b1 = 1.817934e-3, same exponent 0.4214876:
  beta   g0^2     nu       a*Lambda_L    m_pipe/Lambda_L
     2   2.0000   1.1547   1.2503e-02    9.2352e+01
     4   1.0000   0.8165   7.6898e-05    1.0618e+04
     6   0.6667   0.6667   4.1893e-07    1.5913e+06
     8   0.5000   0.5774   2.1718e-09    2.6584e+08
    12   0.3333   0.4714   5.4332e-14    8.6764e+12
    20   0.2000   0.3651   2.9964e-23    1.2186e+22
    40   0.1000   0.2582   1.6733e-46    5.9761e+45
   100   0.0400   0.1633   1.7849e-116   9.1489e+114
Horn (H2) for the same trajectory: m_phys = (N/6) a g0^2(a); SU(3), beta = 12: 0.5 x 2.3984e-6 x 0.5 = 6.0e-7 in Lambda units (i.e. -> 0).

### Code

# Full table generator. Run: python scaling_table.py
import numpy as np

b0 = lambda N: 11.0*N/(48*np.pi**2)
b1 = lambda N: (34.0*N**2/3.0)/(16*np.pi**2)**2

def aLambda(g2, N):
    B0, B1 = b0(N), b1(N)
    return (B0*g2)**(-B1/(2*B0**2)) * np.exp(-1.0/(2*B0*g2))

TARGET = 3.0                        # m / Lambda_L, an O(1) number
for N in (2, 3):
    print(f"\nSU({N}): b0={b0(N):.7f} b1={b1(N):.6e} b1/(2b0^2)={b1(N)/(2*b0(N)**2):.7f}")
    print(f"{'beta':>6}{'g0^2':>9}{'nu':>9}{'a*Lam':>13}{'m_pipe/Lam':>14}{'overshoot':>12}")
    for beta in (2, 4, 6, 8, 12, 20, 40, 100):
        g2 = 2.0*N/beta
        nu = np.sqrt(N/3.0)*np.sqrt(g2)          # exact CT exponent, small-g0 limit
        aL = aLambda(g2, N)
        print(f"{beta:6}{g2:9.4f}{nu:9.4f}{aL:13.4e}{nu/aL:14.4e}{nu/aL/TARGET:12.2e}")

**Caveat.** The number m/Lambda_L = 3 is illustrative; the divergence conclusion is independent of it, since only the a-dependence matters. The nu used is the leading small-g0 form; the exact arcosh differs by O(g0^3) and changes nothing.

**Why it matters.** It converts the obstruction from a limit statement into an auditable table, and it exposes why the error was invisible for four years: at the single coupling beta ~ 6 where most intuition was built, the pipeline's prediction of a one-lattice-spacing correlation length is coincidentally close to reality.

---

## How these fit together

The seven items form one argument. The Chart-Jacobian Lemma (item 1) is the hinge: it identifies the folder's "scale-independent geometric source" and its "vanishing a^2 g^2 Haar mass" as one constant kappa_G/3 = N/6 read in two charts related by X = a g_0 A, and it explains the corpus's own catalogued "contradictions 7, 8 and 11" (HAAR/analysis_reports/contradictions_*) as a single coordinate error rather than three separate defects. Item 5 closes the last escape route by showing that the Weyl-denominator source sigma_geom >= N/2, which looked like a genuinely new a-independent mechanism, is exactly the same N/6 residue plus a divergent Vandermonde term that is a coordinate artifact of eigenangle variables (and is cancelled by the vanishing of |Delta|^2 there). With those two in place, item 2 (the dichotomy) enumerates the possible readings and item 3 (dimensional transmutation, with the chi(g) diagnostic) kills all of them at once, because chi -> 0 for every power of g_0 whereas chi -> 1 for the true scaling function. Item 4 supplies the exact constant in the one chart-invariant route (Combes-Thomas exponent nu = arcosh(1 + m_H^2/(2 alpha_W)) = sqrt(N/3) g_0), which is the arithmetic the corpus stops one step short of in WILSON/03_decay_bounds/04 §4. Item 7 tabulates the resulting divergence.

Items 6 and 7 are logically independent of the dichotomy and attack the same programme from two other directions. Item 6 (chart-consistent convexity window beta < N^2/9, plus the explicit witness U_0 = diag(-1,-1,1,...,1) giving rho_BE(beta) <= N/2 - beta/N -> -infinity) says the finite-cutoff mechanism has no overlap with the scaling window at any a; item 6's Riccati budget rho_k^2 >= rho_0^2 - 2 sum M_j^2 is the correct discrete form of the corpus's coarse-graining bookkeeping. Item 6 (heat-flow ergodicity) says the dynamical repair -- "the flow injects a scale-free positive source" -- cannot work on the one flow the corpus writes down.

Relations to other parts of the corpus that other extractions will cover: the "shrinking convexity core" numerics (HESSIAN/Numerics, CAND-018: R(beta) ~ 0.14/beta^0.9 for SU(3)) is a quantitative companion to item 6 -- the convex core shrinks like 1/beta while typical field amplitudes shrink only like g_0 ~ beta^{-1/2}, so typical configurations leave the core as beta grows; the DOMAIN_ASSESSMENTS note on WILSON refines this by showing the linear-in-r erosion sits entirely in the vertical (gauge) block, so the horizontal convexity radius really does go like beta^{-1/2}, i.e. exactly at the typical fluctuation scale -- marginal, not safe. The "typicality" of the small-field good set K_Lambda(r) = {||log U_l|| <= r} is separately false (each link's marginal under any gauge-invariant measure is exactly Haar), which undercuts the localization repair proposed in RECOMMENDED_02 §4. Finally, the corpus's own honest documents -- Referee_Triage_Mass_Gap_Pipeline_and_Gaps.md, 06_conjectures_target_lemmas.md, COMBES_THOMAS/RICCATI_RG/03_localized_curvature_capacity_rg.md §1, and the "Wait, that's wrong" passage in POLARITY_GRIBOV/03_misc_docs/12_Entropic_Spark_Conjecture.md §3.3 -- state most of the ingredients; what is missing everywhere is the substitution of beta(a) into nu(beta) and the comparison with a Lambda_L.

## Further material found but not fully extracted

Not extracted in full, but real and in this area:

1. **Orbit-volume / Faddeev-Popov determinant convexity** (UNIFORMITY_ASYMPTOTIC_FREEDOM/06_fp_weyl_determinant_orbit_space_hessian.md, and RICCATI/01_riccati_flow/referee_riccati_spine §4). With the orbit Gram matrix M(U) = D_U* D_U, (D_U xi)_b = xi_x - Ad_{U_b} xi_y, and S_orb = -(1/2) log det M, the exact second variation is
   delta^2 S_orb = -(1/2) Tr(M^{-1} delta^2 M) + (1/2) Tr(M^{-1} delta M M^{-1} delta M),
   whose second term is manifestly >= 0 (trace of a square). The decomposition is rigorous; the uniform lower bound requires controlling Tr(M^{-1} delta^2 M) near reducibles and is not done. This is the second candidate sigma_* and is structurally the right object for the lattice orbit space, unlike the single-holonomy Weyl computation. It is worth a separate extraction, together with the polarity/capacity statement (reducibles lie in real algebraic subvarieties of codimension >= 2, hence have zero capacity for the elliptic Dirichlet form, hence the Langevin diffusion a.s. never hits them).

2. **The Helffer-Sjostrand covariance identity derivation from scratch** in WILSON/01_core_theorems/YM_MatrixHinge_to_MassGap.md §3 is clean and complete (solve -Lu = F, apply d, use dL = L^{(1)} d, get Cov(F,G) = <dF, (L^{(1)})^{-1} dG>), as is the Bochner identity L^{(1)} = nabla* nabla + Ric_mu. Both are textbook but correctly reproduced and are the load-bearing analytic interface of the whole programme.

3. **Two "landmine defuser" no-go results** in SCALING_LIMIT/04_CONSTANT_UNIFORMITY/04_no_go_coarse_graining_kernels.md. The second is a genuine two-line obstruction: assumptions (A5) "Pi is a conditional expectation onto gauge-invariant block variables, so Pi(g.U) = Pi(U)" and (A4) "Pi is gauge covariant, Pi(g.U) = g'.Pi(U)" together force Pi(U) to lie in the fixed-point set of the coarse gauge action, which is empty for nontrivial G. Hence no gauge-covariant gauge-invariant Markov coarse-graining kernel exists. Short, correct, and directly relevant to any RG-based repair.

4. **The Davies / level-set ("boundary row-sum") sharpening** of Combes-Thomas (COMBES_THOMAS/MAXWELL_GREEN/02_davies_decay_maxwell_boundary_rowsum.md): conjugating by e^{lambda phi} with phi 1-Lipschitz gives perturbation entries (cosh(lambda(phi(b)-phi(b'))) - 1) M_{bb'}, so only level-crossing pairs contribute and C can be taken to be C_partial rather than the full row sum C_0 = 18 (d = 4). Gains sqrt2 in the exponent; sketch only, no theorem written anywhere.

5. **The SU(2) one-link convexity threshold** beta_c = 4.413914663153596 at theta* = 2.118504088, with the non-convex annulus carrying Gibbs mass ~ e^{-beta} (2.11e-9 at beta = 20). Independently reproducible to 12 digits from HESSIAN/Core_Hessian/02_SU2_SingleLink_BetaC.md and 03_SU2_Concentration_BadMass.md. It is a chart-dependent Euclidean Hessian threshold, not a Bakry-Emery threshold, but the computation is exact and the annulus table is correct.

6. **The corpus's Lean file** lean/YangMills/AsymptoticFreedom.lean is worth keeping as an exhibit: every theorem in it is correct arithmetic (beta_0 = 11N/3, running_coupling positivity, physical_mass monotonicity, and mass_finite : physical_mass (lattice_gap_bound c0 a g0_sq) a = c0 * a * g0_sq), and the one theorem that matters proves exactly horn (H2) of the dichotomy while its docstring claims the opposite. It is the cleanest single demonstration in the corpus that the formalization layer was checking arithmetic rather than physics.
