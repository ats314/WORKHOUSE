---
id: EX-009
title: "Obstruction: the Z_N center-flux witness refutes pointwise pairing coercivity, the Polyak–Łojasiewicz form, and the strip-drift hypothesis in the Foster–Lyapunov route to a volume-uniform Po"
kind: extraction
items: 9
status_breakdown: {"solid": 9}
program: yang_mills
extracted_by: claude-opus-5 subagent, 2026-09-01
stance: preservation (content extraction, not refereeing)
source_files:
  - LYAPUNOV/Core_Drift_Lyapunov/## 7. Lyapunov drift and uniform-in-volume functional inequalities.txt
  - LYAPUNOV/Core_Drift_Lyapunov/02_smooth_gluing_strip_drift_force_density.md
  - LYAPUNOV/Maxwell_Covariance/06_pairing_staple_projection_coercivity(1).md
  - LYAPUNOV/Simulations_Evidence/su2_outside_core_certificates.md
  - LYAPUNOV/Core_Drift_Lyapunov/01_su2_generator_laplacian_drift.md
  - LYAPUNOV/Core_Drift_Lyapunov/su2-drift-certificates.md
  - LYAPUNOV/Core_Drift_Lyapunov/su2_drift_simulation.py
  - LYAPUNOV/Maxwell_Covariance/pairing_term_coercivity_open_problem.md
  - LYAPUNOV/Gluing_Typicality/Doc3_Smooth_Gluing_Lemma_Barrier.md
  - LYAPUNOV/Maxwell_Covariance/05_pairing_noncancellation_structured.md
  - LYAPUNOV/Core_Drift_Lyapunov/G_drift_full_algebra.md
  - _EXTRACT_FOR_LLM/02_candidates/CAND-009-obstruction-no-volume-uniform-foster-lyapunov-drift-for-plaq.md
  - _EXTRACT_FOR_LLM/04_papers/PAPER-1-curvature-no-go/ABSTRACT.md
---

# Obstruction: the Z_N center-flux witness refutes pointwise pairing coercivity, the Polyak–Łojasiewicz form, and the strip-drift hypothesis in the Foster–Lyapunov route to a volume-uniform Poincaré inequality for lattice Wilson gauge theory

> Every Z_N-valued (center) link configuration is an exact critical point of the Wilson action with all plaquette holonomies central, so grad S_W = 0 and grad z_p = 0 identically while the plaquette-defect functional D_Lambda is extensive — this single explicit witness kills the pairing-coercivity assumption, the PL inequality, the strip drift hypothesis, and the numerical drift certificates, at every beta and every volume, on a set of positive Haar measure.

**9 extracted items** — 9 solid

---

## 1. Lemma 1 (Central Critical Point Lemma): the trace-defect gradient vanishes identically at central group elements

`status: solid` · `kind: theorem`

### Statement

Let $G$ be a compact connected Lie group with a bi-invariant metric induced by an $\mathrm{Ad}$-invariant inner product on $\mathfrak g$, and let $\rho:G\to U(n)$ be a faithful unitary representation. Define the smooth trace-defect proxy
$$\widetilde z:G\to[0,2],\qquad \widetilde z(g):=1-\tfrac1n\Re\mathrm{Tr}\,\rho(g).$$
Let $Z(G)_\rho:=\{g\in G:\rho(g)=\zeta I_n \text{ for some }\zeta\in\mathbb C,\ |\zeta|=1\}$ be the set of elements represented by a scalar (in particular, for $G=SU(N)$ and $\rho$ the fundamental, $Z(G)_\rho$ is exactly the center $Z_N=\{\omega^k I: \omega=e^{2\pi i/N}\}$).

Then for every $g\in Z(G)_\rho$:
$$\nabla_G\widetilde z(g)=0,\qquad \widetilde z(g)=1-\Re\zeta .$$
More precisely, for every $X\in\mathfrak g$,
$$\frac{d}{dt}\Big|_{t=0}\Big[1-\tfrac1n\Re\mathrm{Tr}\,\rho\big(g\,e^{tX}\big)\Big] \;=\; -\tfrac1n\,\Re\!\big(\zeta\,\mathrm{Tr}\,d\rho(X)\big)\;=\;0 ,$$
and the same holds for the right-translated variation $g\mapsto e^{tX}g$.

**Lattice corollary.** Let $\Lambda$ be a finite periodic hypercubic lattice in dimension $d$, $M_\Lambda=G^{E(\Lambda)}$ with the product bi-invariant metric, $U_p(U)$ the ordered plaquette holonomy, $\widetilde z_p(U):=\widetilde z(U_p(U))$, $\mathcal D_\Lambda:=\sum_p\widetilde z_p$, $S_W=\beta\mathcal D_\Lambda$, $V_\Lambda:=\sum_p\widetilde z_p^2$. If $U^*\in M_\Lambda$ is such that $\rho(U^*_p)$ is scalar for every plaquette $p$, then for **all** links $\ell$ and **all** plaquettes $p$:
$$\nabla_\ell \widetilde z_p(U^*)=0,\quad \nabla S_W(U^*)=0,\quad \nabla \mathcal D_\Lambda(U^*)=0,\quad \nabla V_\Lambda(U^*)=0,\quad \Gamma_\Lambda(V_\Lambda)(U^*)=0,$$
and hence the pairing functional
$$\mathcal P_\Lambda(U):=\sum_{p}\widetilde z_p(U)\,\big\langle\nabla S_W(U),\nabla\widetilde z_p(U)\big\rangle_{g_\Lambda}$$
satisfies $\mathcal P_\Lambda(U^*)=0$ exactly.

### Derivation

**Step 1 (one-parameter reduction).** Fix $g$ with $\rho(g)=\zeta I_n$, $|\zeta|=1$, and $X\in\mathfrak g$. Then
$$\rho(g e^{tX}) = \rho(g)\rho(e^{tX}) = \zeta\, e^{t\,d\rho(X)} .$$
Therefore
$$\Re\mathrm{Tr}\,\rho(g e^{tX}) = \Re\Big(\zeta\,\mathrm{Tr}\, e^{t\,d\rho(X)}\Big),$$
and differentiating at $t=0$,
$$\frac{d}{dt}\Big|_{0}\Re\mathrm{Tr}\,\rho(g e^{tX}) = \Re\big(\zeta\,\mathrm{Tr}\,d\rho(X)\big).$$
Hence $\frac{d}{dt}|_0\widetilde z(ge^{tX}) = -\frac1n\Re(\zeta\,\mathrm{Tr}\,d\rho(X))$.

**Step 2 (tracelessness).** $\rho$ is a unitary representation, so $d\rho(X)$ is anti-Hermitian for $X\in\mathfrak g$; therefore $\mathrm{Tr}\,d\rho(X)\in i\mathbb R$. If moreover $G$ is semisimple (e.g. $G=SU(N)$, $\mathfrak g=\mathfrak{su}(N)$) then $\mathfrak g=[\mathfrak g,\mathfrak g]$, so $d\rho(X)$ is a sum of commutators and $\mathrm{Tr}\,d\rho(X)=0$ outright.

In the semisimple case, $\mathrm{Tr}\,d\rho(X)=0$ gives the result immediately. In the general unitary case, write $\zeta=e^{i\phi}$ and $\mathrm{Tr}\,d\rho(X)=i\tau$ with $\tau\in\mathbb R$; then $\Re(\zeta\cdot i\tau) = -\tau\sin\phi$, which vanishes for the two real central values $\zeta=\pm1$. For $SU(N)$ the semisimple argument covers all $N$ center elements, so the statement is unconditional there. **This is the entire content of the obstruction.** Since $X$ was arbitrary and $\{X_\ell^a\}$ (right translations in each link coordinate) is an orthonormal frame for $T_gG$, the full gradient vanishes: $\nabla_G\widetilde z(g)=0$.

**Step 3 (from group to lattice).** By the one-link factorization lemma (corpus Lemma 7.28 of `## 7. Lyapunov drift ...txt`, reproduced here): for a plaquette $p$ and a boundary link $\ell\in\partial p$, holding the other three boundary links fixed, the map $g=U_\ell\mapsto U_p$ has the form
$$g\longmapsto \Psi(g)=A\,g^{\sigma}\,B,\qquad A,B\in G,\ \sigma\in\{+1,-1\},$$
and $\Psi$ is an **isometry** of $(G,g_G)$ because the metric is bi-invariant (left/right multiplication and inversion are isometries). Isometry-covariance of the gradient gives
$$\big|\nabla_\ell\widetilde z_p(U)\big| \;=\; \big|\nabla_G\widetilde z\big|\big(U_p(U)\big).$$
If $\ell\notin\partial p$ then $\widetilde z_p$ does not depend on $U_\ell$ and the derivative is $0$.

So if every plaquette holonomy $U_p(U^*)$ is central-in-$\rho$, Step 1–2 give $|\nabla_G\widetilde z|(U_p(U^*))=0$ for every $p$, hence $\nabla_\ell \widetilde z_p(U^*)=0$ for **every** pair $(\ell,p)$.

**Step 4 (assembling the functionals).** $\nabla S_W = \beta\sum_p\nabla\widetilde z_p = 0$ at $U^*$. $\nabla \mathcal D_\Lambda=\sum_p\nabla\widetilde z_p=0$. $\nabla V_\Lambda = 2\sum_p \widetilde z_p\nabla\widetilde z_p=0$, hence $\Gamma_\Lambda(V_\Lambda)=|\nabla V_\Lambda|^2=0$. Finally
$$\mathcal P_\Lambda(U^*)=\sum_p \widetilde z_p(U^*)\langle \underbrace{\nabla S_W(U^*)}_{=0},\nabla\widetilde z_p(U^*)\rangle = 0 .\qquad\square$$

**Remark (geometric picture, SU(2)).** In the normalization used by the corpus code (quaternion $q=(a,\mathbf v)$, $a=\tfrac12\Re\mathrm{Tr}U$; $SU(2)\cong S^3$ of radius $1$), writing $U_p=\exp(i\theta_p\hat n_p\!\cdot\!\sigma)$ one has $\widetilde z=1-\cos\theta$ and
$$|\nabla_G\widetilde z|=|\sin\theta| = \sqrt{\widetilde z\,(2-\widetilde z)} .$$
The defect $\widetilde z$ and the force $|\nabla\widetilde z|$ vanish **simultaneously at $\theta=0$** (vacuum, $\widetilde z=0$) **and the force alone vanishes at $\theta=\pi$** (the nontrivial center element $-\mathbf 1$, $\widetilde z=2$, the *maximum* of the defect). This is the corpus's own Section 4 of `02_smooth_gluing_strip_drift_force_density.md`; the present lemma is its non-perturbative, all-plaquettes-simultaneously version.

### Constants and numbers

SU(2), unit-$S^3$ normalization (the one used by `su2_drift_simulation.py`): $\widetilde z(\theta)=1-\cos\theta$, $|\nabla\widetilde z|^2=\sin^2\theta=\widetilde z(2-\widetilde z)$, $\mathrm{Hess}\,\widetilde z=\cos\theta\cdot g_G$, $\Delta_G\widetilde z = 3\cos\theta = 3(1-\widetilde z)$, $\Delta_G\big(\tfrac12\Re\mathrm{Tr}\big)=-3\cdot\tfrac12\Re\mathrm{Tr}$ so $C_2(\text{fund})=3$. Center values: $\widetilde z(+\mathbf 1)=0$, $\widetilde z(-\mathbf 1)=2$.
SU(N) with $\omega=e^{2\pi i/N}$: $\widetilde z(\omega^k I)=1-\cos(2\pi k/N)$. Verified numerically: SU(2) $\to 2.000000$, SU(3) $\to 1.500000$, SU(4) $\to 1.000000$ (exact match), and $\|\nabla S_W\|^2 = 0$ to $\le 4\times10^{-17}$ by exact matrix central differences at $\varepsilon=10^{-5}$.
Derived uniform SU(2) constants for the corpus's bookkeeping (Lemmas 7.25–7.29): $C^{(1)}_{\widetilde z}=\sup|\sin\theta|=1$; $C^{(2)}_{\widetilde z}=\sup|\cos\theta|=1$; $C_\Delta=\sup|\Delta_G\widetilde z|=3$; $C_\nabla=\sup_{\theta}\frac{\sin^2\theta}{1-\cos\theta}=\sup_{z\in(0,2]}(2-z)=2$ (supremum approached as $\theta\to0$). Overlap $\nu=2(d-1)=6$ in $d=4$; perimeter $m_\partial=4$.

### Code

# Exact matrix check of Lemma 1 for SU(N), N = 2,3,4 (no finite-difference in the
# statement itself: grad S_W is computed by central differences at eps=1e-5 along an
# orthonormal basis of su(N) on every link, and comes out 0 to machine precision).
# File: <scratchpad>/sun_center_check.py   (run: python sun_center_check.py)
#
#   U[x,mu] = omega^{e_mu(x)} * I_N ,  omega = exp(2 pi i / N)
#   e_mu(x) = sum_{nu<mu} m[mu,nu] x_nu   (m in {0,1})
#
# Output (L=2, d=4):
#   SU(2) double flux : distinct z_p = [0, 2]   Bavg=0.666667  ||grad S_W||^2 = 0.000e+00
#   SU(3) double flux : distinct z_p = [0, 1.5] Bavg=0.500000  ||grad S_W||^2 = 0.000e+00
#   SU(4) double flux : distinct z_p = [0, 1]   Bavg=0.333333  ||grad S_W||^2 = 0.000e+00
#   SU(4) maximal     : distinct z_p = [1]      Bavg=1.000000  ||grad S_W||^2 = 3.6e-17

def grad_norm2(U, N, beta, eps=1e-5):
    """||grad S_W||^2 by exact central differences along su(N) generators on each link."""
    import itertools, scipy.linalg as sla
    gens = su_n_generators(N); L = U.shape[0]; tot = 0.0
    for idx in itertools.product(range(L), repeat=4):
        for mu in range(4):
            for T in gens:
                Up = U.copy(); Um = U.copy()
                Up[idx][mu] = U[idx][mu] @ sla.expm( eps*T)
                Um[idx][mu] = U[idx][mu] @ sla.expm(-eps*T)
                d = (action(Up,N,beta) - action(Um,N,beta)) / (2*eps)
                tot += d*d
    return tot

**Caveat.** For a non-semisimple $G$ (e.g. $U(1)$ factors) the vanishing at a scalar $\rho(g)=\zeta I$ needs $\zeta\in\{\pm1\}$; for $SU(N)$ with the fundamental representation it is unconditional, which is the only case used.

**Why it matters.** This is the whole obstruction in one line: the Wilson force and the defect gradient are *simultaneously zero* on an entire nontrivial stratum of configuration space where the defect itself is maximal. Any argument of the form 'large plaquette defect $\Rightarrow$ large restoring force' — which is what pairing coercivity, the PL inequality, and strip drift all are — is false at these points, at every $\beta$ and every volume.

---

## 2. Construction: the explicit Z_N center-flux family and its exact defect spectrum

`status: solid` · `kind: construction`

### Statement

Let $d=4$, $\Lambda=(\mathbb Z/L)^4$ periodic, $G=SU(N)$, $\omega=e^{2\pi i/N}$, and let $S\subseteq\{(\mu,\nu):0\le\mu<\nu\le3\}$ be **any** subset of the six coordinate planes. Define the matrix $m\in\{0,1\}^{4\times4}$ by $m_{\nu\mu}:=\mathbf 1[(\mu,\nu)\in S]$ for $\mu<\nu$ (all other entries $0$), and set
$$\boxed{\;U^{*}_{x,\mu}\;:=\;\omega^{\,e_\mu(x)}\,I_N,\qquad e_\mu(x):=\sum_{\nu<\mu} m_{\mu\nu}\,x_\nu \ \ (\mathrm{mod}\ N).\;}$$
Assume $N\mid L$ (for $N=2$: all side lengths even), so $e_\mu$ descends to the torus.

Then:
1. Every link variable is central, hence every plaquette holonomy is central, and for $\mu<\nu$ the plaquette holonomy is **$x$-independent**:
$$U^{*}_{p_{\mu\nu}(x)}=\omega^{\,m_{\nu\mu}}\,I_N \quad\text{for every }x .$$
2. The plaquette defect spectrum is exactly two-valued:
$$\widetilde z_{p_{\mu\nu}} = \begin{cases}1-\cos(2\pi/N), & (\mu,\nu)\in S,\\[2pt] 0,&\text{otherwise,}\end{cases}$$
so with $|P(\Lambda)|=6L^4$,
$$\mathcal D_\Lambda(U^*)=\frac{|S|}{6}\,\big(1-\cos\tfrac{2\pi}{N}\big)\,|P(\Lambda)| ,\qquad B_{\rm avg}(U^*)=\frac{|S|}{6}\big(1-\cos\tfrac{2\pi}{N}\big).$$
For $SU(2)$: $B_{\rm avg}(U^*)=|S|/3\in\{0,\tfrac13,\tfrac23,1,\tfrac43,\tfrac53,2\}$ and $\mathcal D_\Lambda(U^*)=\tfrac{|S|}{3}|P|$ is **extensive** for every $|S|\ge1$.
3. By Lemma 1, $\nabla S_W(U^*)=\nabla\mathcal D_\Lambda(U^*)=\nabla V_\Lambda(U^*)=0$ and $\mathcal P_\Lambda(U^*)=0$: $U^*$ is an exact critical point of the Wilson action for **every** $\beta$.
4. The witness named in the corpus, $U^*_{x,2}=(-1)^{x_1}I,\ U^*_{x,4}=(-1)^{x_3}I$ (all other links $=I$), is exactly the case $N=2$, $S=\{(1,2),(3,4)\}$, giving $B_{\rm avg}=2/3$.
5. $|S|=6$ (the 'staggered' choice $e_\mu(x)=x_0+\dots+x_{\mu-1}$) makes **every** plaquette maximally defective: $\widetilde z_p\equiv 1-\cos(2\pi/N)$, $B_{\rm avg}=1-\cos(2\pi/N)$; for $SU(2)$ this is $B_{\rm avg}=2$, the **global maximum** of $S_W$ on $M_\Lambda$.

### Derivation

**Well-definedness on the torus.** $e_\mu(x)=\sum_{\nu<\mu}m_{\mu\nu}x_\nu$ is $\mathbb Z/N$-valued and depends on $x$ only through $x\bmod L$ provided $N\mid L$. (If $N\nmid L$ one still gets a perfectly legal configuration — it just carries a 'twist wall' and the plaquette defect is no longer homogeneous; the critical-point property is unaffected, see the numerics below.)

**Plaquette computation.** Use the corpus convention $U_{p_{\mu\nu}}(x)=U_\mu(x)\,U_\nu(x+\hat\mu)\,U_\mu(x+\hat\nu)^{-1}\,U_\nu(x)^{-1}$. All four factors are scalars $\omega^{\bullet}I$, hence commute, and the holonomy is $\omega^{\,\sigma_{\mu\nu}(x)}I$ with
$$\sigma_{\mu\nu}(x)=e_\mu(x)+e_\nu(x+\hat\mu)-e_\mu(x+\hat\nu)-e_\nu(x)\pmod N .$$
Now for $\mu<\nu$:
* $e_\mu(x+\hat\nu)-e_\mu(x)=m_{\mu\nu}$, and $m_{\mu\nu}=0$ because $\nu>\mu$ (only $m_{\mu\nu}$ with $\nu<\mu$ is allowed to be nonzero).
* $e_\nu(x+\hat\mu)-e_\nu(x)=m_{\nu\mu}$, and this is exactly the switch we set.

Hence $\sigma_{\mu\nu}(x)=m_{\nu\mu}$, independent of $x$. So every plaquette in plane $(\mu,\nu)$ carries center element $\omega^{m_{\nu\mu}}$. **The six planes are independently switchable.** (Consistency with the lattice Bianchi identity is automatic: in a $3$-cube each plane occurs on two opposite faces with opposite orientation, so the product of the six face elements is $1$ for any constant assignment.)

**Defect.** $\widetilde z=1-\frac1N\Re\mathrm{Tr}(\omega^{m}I_N)=1-\Re\,\omega^{m}=1-\cos(2\pi m/N)$, which is $0$ for $m=0$ and $1-\cos(2\pi/N)$ for $m=1$. Averaging over the six planes, each contributing $L^4$ plaquettes, gives $B_{\rm avg}=\frac{|S|}{6}(1-\cos\frac{2\pi}{N})$.

**Extensivity.** $\mathcal D_\Lambda(U^*)=B_{\rm avg}\cdot|P(\Lambda)| = \frac{|S|}{6}(1-\cos\frac{2\pi}{N})\cdot 6L^4$, which grows like the volume for any fixed $|S|\ge1$.

**Critical point.** All plaquette holonomies are scalar, so Lemma 1 applies verbatim: $\nabla_\ell\widetilde z_p(U^*)=0$ for all $(\ell,p)$.

**Not gauge-trivial.** For $N=2$, $|S|\ge1$, the $1\times1$ Wilson loop in a twisted plane has holonomy $-\mathbf 1$; $\mathrm{Tr}\,U_p$ is gauge invariant, so $U^*$ is not gauge-equivalent to the vacuum. It is also far from the corpus's small-field core: half of the links have $d_G(U^*_\ell,\mathbf 1)=\pi$, hence $U^*\notin K_\Lambda(r)$ for any $r<\pi$.

**Nature of the critical point.** For $|S|=0$ it is the global minimum of $S_W$; for $|S|=6$ (SU(2)) it is the global maximum ($\widetilde z_p\equiv2$ everywhere); for $1\le|S|\le5$ it is a saddle (directions attached to twisted plaquettes decrease $S_W$, those attached to untwisted plaquettes increase it).

**Gibbs weight (honest caveat).** $e^{-S_W(U^*)}=e^{-\beta\mathcal D_\Lambda(U^*)}=e^{-\beta\frac{|S|}{3}|P|}$ for SU(2): exponentially small in the volume. The configuration is atypical; the point is that the assumptions being refuted are stated as **pointwise inequalities for all $U$**, not as almost-sure statements.

### Constants and numbers

Counts in $d=4$, side $L$: $|V|=L^4$, $|E|=4L^4$, $|P|=6L^4$, so $|E|=\tfrac23|P|$; $\nu=6$ plaquettes per link; $m_\partial=4$ links per plaquette.

SU(2), $L=4$ ($|P|=1536$), exact plaquette-defect spectrum verified by direct computation:
| $|S|$ | twisted planes | $z_p$ values (count) | $B_{\rm avg}$ | $\mathcal D_\Lambda$ |
|---|---|---|---|---|
| 0 | — | $\{0\}$ (1536) | 0 | 0 |
| 1 | (0,1) | $\{0,2\}$ (1280, 256) | 1/3 | $\tfrac13|P|$ |
| 2 | (0,1),(2,3) | $\{0,2\}$ (1024, 512) | 2/3 | $\tfrac23|P|$ |
| 3 | +(0,2) | $\{0,2\}$ (768, 768) | 1 | $|P|$ |
| 4 | +(1,3) | $\{0,2\}$ (512, 1024) | 4/3 | $\tfrac43|P|$ |
| 6 | all | $\{2\}$ (1536) | 2 | $2|P|$ |

SU(N) center defect $1-\cos(2\pi/N)$: $N=2\to2$, $N=3\to1.5$, $N=4\to1$ (all confirmed numerically).
Robustness to the divisibility condition (verified): SU(2), $L=3$ (odd), $S=\{(0,1),(2,3)\}$ gives $z_p\in\{0,2\}$, $B_{\rm avg}=4/9=0.4444$, $\|\nabla S_W\|^2=0$ — still extensive, still a critical point.
Volume independence (verified, $\beta=6$, $\varepsilon_{\rm fd}=5\times10^{-3}$, mc$=400$): $L=2,4,6$ all give $B_{\rm avg}=0.666667$ exactly and $\sum_\ell\|F_\ell\|^2=0$ exactly.

### Code

def center_flux_config(L, twisted_planes):
    """Z_2 center configuration on a periodic L^4 lattice, quaternion coordinates.
       Links are +-I; eta_mu(x) = prod_{nu<mu} (-1)^{m[mu,nu] x_nu}.
       The plaquette sign in plane (mu,nu), mu<nu, is exactly (-1)^{m[nu,mu]}.
       Requires every L_mu even for periodicity."""
    import numpy as np
    d = 4
    m = np.zeros((d, d), dtype=int)
    for (mu, nu) in twisted_planes:
        assert mu < nu
        m[nu, mu] = 1
    U = np.zeros((L, L, L, L, d, 4)); U[..., 0] = 1.0     # quaternion (a,b,c,d), a = (1/2)ReTr
    coords = np.indices((L, L, L, L))
    for mu in range(d):
        expo = np.zeros((L, L, L, L), dtype=int)
        for nu in range(mu):
            expo = expo + m[mu, nu] * coords[nu]
        U[..., mu, 0] = (-1.0) ** (expo % 2)
    return U

# Corpus witness  U*_{x,2}=(-1)^{x_1} I,  U*_{x,4}=(-1)^{x_3} I  (1-based dirs)
# is  center_flux_config(L, [(0,1), (2,3)])  in 0-based dirs  ->  B_avg = 2/3.
# Global maximiser of S_W (SU(2)):  center_flux_config(L, list(itertools.combinations(range(4),2)))
# File: <scratchpad>/center_flux_witness.py

**Caveat.** $N\mid L$ is needed only for the defect to be homogeneous; without it the configuration is still central everywhere and still an exact critical point, only with a lower (still extensive) defect density.

**Why it matters.** It is a closed-form, one-line, volume-independent family covering the whole range $B_{\rm avg}\in\{0,\tfrac13,\tfrac23,1,\tfrac43,\tfrac53,2\}$ for SU(2), so whatever core threshold $\tau_0<2$ an argument picks, there is a witness strictly outside it. Nothing about the family depends on $\beta$, on $L$, or on which of the several Lyapunov proxies is used.

---

## 3. Refutation of Assumption 7.38 (pointwise coercive pairing inequality) and its off-core form

`status: solid` · `kind: obstruction`

### Statement

**Assumption 7.38 (as stated in the corpus, eq. (7.60)).** There exist $c_{\rm pair}>0$, $C_{\rm pair}\ge0$ depending only on $(G,g_G)$, $\rho$ and the action family — but **not** on $\Lambda$ — such that for all $\Lambda$ and all $U\in M_\Lambda$,
$$\mathcal P_\Lambda(U):=\sum_{p\in P(\Lambda)}\widetilde z_p(U)\,\big\langle\nabla S_\Lambda(U),\nabla\widetilde z_p(U)\big\rangle_{g_\Lambda}\;\ge\;c_{\rm pair}\sum_{p}\widetilde z_p(U)\;-\;C_{\rm pair}.$$

**Claim.** Assumption 7.38 is **false** for $S_\Lambda=S_W$ on $G=SU(N)$, for every $\beta>0$. So is its off-core weakening 'there is $c_\varepsilon>0$ with $\mathcal P_\Lambda\ge c_\varepsilon\mathcal D_\Lambda$ for all $U\notin K_\Lambda(\varepsilon)$', and so is the ratio form 'on $\{B_{\rm avg}\ge\tau_0\}$, $\langle\nabla S,\nabla\bar V\rangle\ge c_\star B_{\rm avg}$' for any $\tau_0<1-\cos(2\pi/N)$ (for $SU(2)$: any $\tau_0<2$).

Consequently Proposition 7.39 — the step that converts the exact drift identity into a Foster–Lyapunov bound $L_\Lambda W_\Lambda\le-\alpha W_\Lambda+\beta\mathbf 1_{K}$ for $W_\Lambda=e^{\kappa V_\Lambda}$ — has no valid hypothesis; the volume-uniform local-to-global route through §7.4 is broken at this exact point.

### Derivation

Take $\Lambda=(\mathbb Z/L)^4$ with $L$ even, $G=SU(2)$, and $U^*=U^*(S)$ the center-flux witness with $|S|=2$ (the corpus's $U^*_{x,2}=(-1)^{x_1}I$, $U^*_{x,4}=(-1)^{x_3}I$).

**Left-hand side.** By Lemma 1, $\nabla S_W(U^*)=0$, hence
$$\mathcal P_\Lambda(U^*)=\sum_p\widetilde z_p(U^*)\,\langle 0,\nabla\widetilde z_p(U^*)\rangle = 0 .$$
(Numerically confirmed: the Monte-Carlo estimator gives $\texttt{gip}=8.6\times10^{-8}$ at $\varepsilon_{\rm fd}=5\times10^{-3}$ and $1.4\times10^{-10}$ at $\varepsilon_{\rm fd}=10^{-3}$, scaling exactly as $\varepsilon^{4}$ — i.e. pure finite-difference truncation of an identically zero quantity.)

**Right-hand side.** $\mathcal D_\Lambda(U^*)=\tfrac23|P(\Lambda)|=4L^4$.

**Contradiction.** Assumption 7.38 at $U=U^*$ reads
$$0\;\ge\;c_{\rm pair}\cdot 4L^4\;-\;C_{\rm pair}\qquad\Longleftrightarrow\qquad C_{\rm pair}\;\ge\;4\,c_{\rm pair}\,L^4 .$$
Since $c_{\rm pair}>0$ is fixed and $C_{\rm pair}$ must be independent of $\Lambda$, letting $L\to\infty$ (through even $L$) gives a contradiction. **Assumption 7.38 is false.** $\square$

**Off-core form.** The corpus's core is $K_\Lambda(\varepsilon)$ = configurations with small plaquette defect (or small $B_{\rm avg}$). At $U^*$, half of the link variables sit at geodesic distance $\pi$ from $\mathbf 1$ and $B_{\rm avg}(U^*)=2/3$; so $U^*\notin K_\Lambda(\varepsilon)$ for every $\varepsilon<2/3$, and the off-core inequality $\mathcal P_\Lambda\ge c_\varepsilon\mathcal D_\Lambda$ reads $0\ge c_\varepsilon\cdot\tfrac23|P|>0$: false immediately, with no volume limit needed. Choosing $|S|=3,4,5$ pushes $B_{\rm avg}$ to $1,\tfrac43,\tfrac53$, so **no** threshold $\varepsilon<2$ escapes.

**Ratio form (the version actually certified numerically).** The corpus's $\bar V=1+B_{\rm avg}$ variant has $\langle\nabla S_W,\nabla\bar V\rangle=\frac{\beta}{|P|}\|\nabla\mathcal D_\Lambda\|^2$ (see the staple/projection item), which is $0$ at $U^*$ while $B_{\rm avg}(U^*)=2/3\ge\tau_0=0.3883$. The certified requirement $\ge 20.951\times 0.6667 = 13.97$ fails by the full margin.

**Why the failure is structural, not an artefact.** The corpus's own §7.2 bookkeeping shows every other term in $(L_\Lambda W_\Lambda)/W_\Lambda$ is bounded by $\mathcal D_\Lambda$ with volume-uniform constants (Corollary 7.36):
$$\frac{L_\Lambda W_\Lambda}{W_\Lambda}\;\le\;(\kappa C_V+\kappa^2C_\Gamma)\,\mathcal D_\Lambda\;-\;2\kappa\,\mathcal P_\Lambda,\qquad C_V=A_1+A_2,\ C_\Gamma=A_3 ,$$
so $\mathcal P_\Lambda$ is the *only* source of negativity, and Proposition 7.39 further needs $c_{\rm pair}>C_V$ (which for $SU(2)$ means $c_{\rm pair}>40$). Not only is the inequality false, the required constant is large and the witness makes the pairing term exactly zero.

**What survives.** The purely diffusive part of the corpus's argument (Lemmas 7.24–7.29, Prop. 7.31, Prop. 7.35, Cor. 7.36) is correct and untouched: it is genuine, volume-uniform derivative bookkeeping. What is refuted is exactly the one hypothesis the corpus itself flagged as open.

### Constants and numbers

Witness $U^*$ ($SU(2)$, $|S|=2$, any even $L$): $\mathcal P_\Lambda(U^*)=0$ exactly; $\mathcal D_\Lambda(U^*)=\tfrac23|P|=4L^4$; $B_{\rm avg}=2/3$; required $C_{\rm pair}\ge 4c_{\rm pair}L^4$.
Monte-Carlo estimator of $\langle\nabla S_W,\nabla\bar V\rangle$ at $U^*$ ($L=4$, $\beta=6$, mc$=2000$): $\varepsilon=2\times10^{-2}\Rightarrow2.30\times10^{-5}$; $10^{-2}\Rightarrow1.44\times10^{-6}$; $5\times10^{-3}\Rightarrow8.99\times10^{-8}$; $2\times10^{-3}\Rightarrow2.30\times10^{-9}$; $10^{-3}\Rightarrow1.44\times10^{-10}$. Ratio between successive $\varepsilon$-decades matches $\varepsilon^4$ to 3 digits ($2.295\times10^{-5}/1.439\times10^{-10}=1.595\times10^{5}$ vs $20^4=1.6\times10^{5}$).
Explicit $SU(2)$ constants in Corollary 7.36 (derived here from $C_\Delta=3$, $C_\nabla=2$, $\nu=6$): $A_1=8C_\Delta=24$, $A_2=8C_\nabla=16$, $A_3=64\nu C_\nabla=768$; $C_V=40$, $C_\Gamma=768$; Proposition 7.39 therefore needs $c_{\rm pair}>40$ and $\kappa\le(c_{\rm pair}-40)/1536$.

**Caveat.** The witness has Gibbs probability $\sim e^{-\frac{2}{3}\beta|P|}$; a defender may propose restricting the drift to a high-probability set. That is not available here: Foster–Lyapunov requires a *pointwise* inequality off a core set which must itself carry a volume-uniform local Poincaré inequality, and enlarging the core to swallow the center stratum reintroduces exactly the mixing problem the argument was meant to solve.

**Why it matters.** Assumption 7.38 is, by the corpus's own accounting (Remark 7.40), 'the only remaining obstruction' between the exact drift identity and a volume-uniform Poincaré/LSI. Showing it is false — with a two-line witness valid at every $\beta$ and every volume — closes that route definitively rather than leaving it open.

---

## 4. Refutation of the Polyak–Łojasiewicz form, with a quantitative open-neighbourhood estimate

`status: solid` · `kind: obstruction`

### Statement

The corpus (`06_pairing_staple_projection_coercivity(1).md`, §4) proves that the desired pairing coercivity is *equivalent* to a Polyak–Łojasiewicz inequality for the total defect:
$$\big\|\nabla \mathcal D_\Lambda\big\|^2\;\ge\;\kappa_\star\,\mathcal D_\Lambda\qquad\text{on }\{\mathcal D_\Lambda\ge\tau_0|P|\},\qquad \kappa_\star:=c_\star/\beta .$$

**Claim (failure on an open set, quantitatively).** Let $G=SU(2)$, $d=4$, $\Lambda=(\mathbb Z/L)^4$ with $L$ even, and let $U^*$ be the center-flux witness with $|S|=2$ ($B_{\rm avg}=2/3$). For $\delta\in(0,\,1/4]$ define the $\ell^\infty$-ball
$$\mathcal N_\delta(U^*):=\big\{U\in M_\Lambda:\ \max_{\ell\in E(\Lambda)} d_G\big(U_\ell,U^*_\ell\big)\le\delta\big\}.$$
Then for every $U\in\mathcal N_\delta(U^*)$ and every volume $\Lambda$:
$$\big\|\nabla\mathcal D_\Lambda(U)\big\|^2\;\le\;384\,|P(\Lambda)|\,\delta^2, \qquad \mathcal D_\Lambda(U)\;\ge\;\tfrac12|P(\Lambda)| ,$$
hence
$$\boxed{\ \frac{\|\nabla\mathcal D_\Lambda(U)\|^2}{\mathcal D_\Lambda(U)}\;\le\;768\,\delta^2\qquad\text{for all }U\in\mathcal N_\delta(U^*),\ \text{uniformly in }\Lambda.\ }$$
Therefore, for any prescribed $\kappa_\star>0$, the PL inequality fails **everywhere** on $\mathcal N_{\delta}(U^*)$ with $\delta:=\min\{\sqrt{\kappa_\star/768},\,1/4\}$, a set of strictly positive Haar measure
$$\mathrm{Haar}\big(\mathcal N_\delta(U^*)\big)=\Big(\tfrac{\delta-\sin\delta\cos\delta}{\pi}\Big)^{|E(\Lambda)|}>0 .$$
So the violation is not a measure-zero/critical-point artefact.

### Derivation

Write $U_\ell=U^*_\ell\exp(v_\ell)$ with $|v_\ell|\le\delta$ ($SU(2)\cong S^3$ of radius $1$ in the corpus normalization, so $d_G(\mathbf 1,\exp v)=|v|$).

**Step 1 (plaquette angles stay near $0$ or $\pi$).** The metric is bi-invariant, so $d_G(ab,a'b')\le d_G(a,a')+d_G(b,b')$ and $d_G(a^{-1},a'^{-1})=d_G(a,a')$. A plaquette holonomy is a word of length $4$ in boundary links, hence
$$d_G\big(U_p(U),\,U_p(U^*)\big)\;\le\;\sum_{\ell\in\partial p}|v_\ell|\;\le\;4\delta .$$
Since $U_p(U^*)=\pm\mathbf 1$, the class angle satisfies $\theta_p\in[0,4\delta]$ (untwisted plaquette) or $\theta_p\in[\pi-4\delta,\pi]$ (twisted plaquette).

**Step 2 (force bound).** In both cases $|\sin\theta_p|\le\sin(4\delta)\le 4\delta$ (valid for $4\delta\le\pi/2$, i.e. $\delta\le\pi/8$; $\delta\le1/4$ suffices). By the isometry lemma (Lemma 7.28/7.29 of the corpus, reproduced in Lemma 1 Step 3),
$$\big\|\nabla_\ell \widetilde z_p(U)\big\| = \big|\nabla_G\widetilde z\big|(U_p) = |\sin\theta_p| \le 4\delta\qquad (\ell\in\partial p),$$
and $=0$ for $\ell\notin\partial p$.

**Step 3 (link gradient).** $\nabla_\ell \mathcal D_\Lambda=\sum_{p\ni\ell}\nabla_\ell \widetilde z_p$, a sum of at most $\nu=6$ terms, so by the triangle inequality $\|\nabla_\ell\mathcal D_\Lambda\|\le 6\cdot4\delta=24\delta$. Summing over links,
$$\|\nabla \mathcal D_\Lambda\|^2=\sum_{\ell\in E}\|\nabla_\ell\mathcal D_\Lambda\|^2\;\le\;|E|\,(24\delta)^2 = 576\,|E|\,\delta^2 = 576\cdot\tfrac23|P|\,\delta^2 = 384\,|P|\,\delta^2 ,$$
using $|E|=4L^4=\tfrac23\cdot6L^4=\tfrac23|P|$.

**Step 4 (defect stays extensive).** For a twisted plaquette, $\theta_p\ge\pi-4\delta$ gives
$$\widetilde z_p=1-\cos\theta_p\;\ge\;1+\cos(4\delta)\;\ge\;2-8\delta^2 .$$
With $|S|=2$ twisted planes out of six, $\tfrac13|P|$ plaquettes are twisted, so
$$\mathcal D_\Lambda(U)\;\ge\;\tfrac13|P|\,(2-8\delta^2)=\tfrac23|P|(1-4\delta^2)\;\ge\;\tfrac12|P|\quad\text{whenever }\delta\le\tfrac14 .$$

**Step 5 (combine).**
$$\frac{\|\nabla\mathcal D_\Lambda\|^2}{\mathcal D_\Lambda}\;\le\;\frac{384|P|\delta^2}{\tfrac12|P|}\;=\;768\,\delta^2 ,$$
independent of $\Lambda$. $\square$

**Step 6 (Haar measure of the violating set).** $SU(2)$ with this metric is the unit $S^3$; the normalized volume of a geodesic ball of radius $\delta$ is
$$\frac{\int_0^{\delta}\sin^2\theta\,d\theta}{\int_0^{\pi}\sin^2\theta\,d\theta}=\frac{\delta-\sin\delta\cos\delta}{\pi}\;\approx\;\frac{2\delta^3}{3\pi}\ \ (\delta\to0).$$
The $\ell^\infty$-ball is a product of $|E|$ such balls, giving the stated measure. It is positive but exponentially small in the volume — the honest reading is 'open set, not null set', not 'typical set'.

**[reconstructed]** Steps 1–6 are mine; the corpus asserted only that the violation 'holds on an open set by continuity' without a quantitative estimate, and CAND-009 explicitly lists this as a missing step. The bound $768\delta^2$ is verified below and is conservative by roughly an order of magnitude.

### Constants and numbers

Analytic bound: $\|\nabla\mathcal D_\Lambda\|^2/\mathcal D_\Lambda\le 768\,\delta^2$ on $\mathcal N_\delta(U^*)$, $\delta\le1/4$, $SU(2)$, $d=4$, any even $L$.
Measured (exact staple/projection computation, $L=4$, $|P|=1536$, 5 random perturbations per $\delta$, ranges over the 5 draws):
| $\delta$ | measured $\|\nabla\mathcal D\|^2/\mathcal D$ | analytic bound $768\delta^2$ |
|---|---|---|
| 0.00 | $0$ (exactly) | 0 |
| 0.01 | $6.13\times10^{-3}$ – $7.13\times10^{-3}$ | $7.68\times10^{-2}$ |
| 0.02 | $2.44\times10^{-2}$ – $2.84\times10^{-2}$ | $3.07\times10^{-1}$ |
| 0.05 | $1.49\times10^{-1}$ – $1.74\times10^{-1}$ | $1.92$ |
| 0.10 | $5.56\times10^{-1}$ – $6.41\times10^{-1}$ | $7.68$ |
| 0.20 | $1.71$ – $1.91$ | $30.7$ |
| 0.40 | $3.05$ – $3.15$ | $122.9$ |
The measured ratio is $\propto\delta^2$ over two decades, exactly as predicted, and $\to0$ as $\delta\to0$.
Haar measure of $\mathcal N_\delta$: $[(\delta-\sin\delta\cos\delta)/\pi]^{4L^4}$; e.g. $\delta=0.05$ gives $3.31\times10^{-5}$ per link.
Target constants in the corpus: $c_\star\approx20.9$ (i.e. $\kappa_\star=c_\star/\beta\approx3.49$ at $\beta=6$); the PL inequality with that $\kappa_\star$ fails on all of $\mathcal N_\delta$ with $\delta\le\sqrt{3.49/768}=0.067$.

### Code

def gradD2_and_D(U):
    """Exact (no finite differences) ||grad D_Lambda||^2 and D_Lambda in quaternion coords.
       grad_l D = -Pi_su2(U_l Omega_l), Omega_l = sum of the 6 staples at l;
       in quaternions Pi_su2 = imaginary part.  Returns (||grad D||^2, D)."""
    import numpy as np
    L = U.shape[0]; tot = 0.0
    for mu in range(4):
        Omega = np.zeros((L,L,L,L,4))
        for nu in range(4):
            if nu == mu: continue
            Unu = U[...,nu,:]; Umu = U[...,mu,:]
            # forward staple  U_nu(x+mu) U_mu(x+nu)^-1 U_nu(x)^-1
            s1 = qmul(qmul(np.roll(Unu,-1,axis=mu), qconj(np.roll(Umu,-1,axis=nu))), qconj(Unu))
            # backward staple U_nu(x+mu-nu)^-1 U_mu(x-nu)^-1 U_nu(x-nu)
            Unu_m = np.roll(Unu, 1, axis=nu)
            s2 = qmul(qmul(qconj(np.roll(Unu_m,-1,axis=mu)), qconj(np.roll(Umu,1,axis=nu))), Unu_m)
            Omega = Omega + s1 + s2
        M = qmul(U[...,mu,:], Omega)
        tot += float((M[...,1:]**2).sum())
    D = sum(float((1.0-plaquette(U,mu,nu)[...,0]).sum())
            for mu in range(4) for nu in range(mu+1,4))
    return tot, D
# File: <scratchpad>/center_flux_checks2.py, section 4.

**Caveat.** The violating set has Haar measure exponentially small in the volume; the estimate establishes 'open, positive measure', not 'non-negligible under the Gibbs measure'.

**Why it matters.** It upgrades 'the inequality fails at one point' to 'the inequality fails on a ball of computable radius, with a volume-uniform rate' — which is what is needed to rule out repairs that perturb away from exact critical points, or that quotient by a null set.

---

## 5. Refutation of the strip-drift hypothesis and the force-density condition

`status: solid` · `kind: obstruction`

### Statement

The corpus's smooth-gluing route (`Doc3_Smooth_Gluing_Lemma_Barrier.md`, hypothesis (H2); `02_smooth_gluing_strip_drift_force_density.md`, Hypothesis 5.2 and Corollary 7.1) requires a **pointwise** negative drift across a boundary strip: with $\mathcal B_\Lambda:=B_{\rm avg}$ and $L=\Delta-\langle\nabla S_W,\nabla\cdot\rangle$, there should exist $\rho>0$ independent of $|\Lambda|$ with
$$L\,\mathcal B_\Lambda\;\le\;-\rho\qquad\text{pointwise on }\Sigma=\{\varepsilon<\mathcal B_\Lambda<\varepsilon+\delta\},$$
delivered by the force-density Hypothesis 5.2 ('at least a fraction $\alpha$ of plaquettes have $\theta_p\in[\theta_{\min},\pi-\kappa]$').

**Claim.** Both are false. Precisely, using the exact affine Laplacian identity $\Delta_\Lambda\mathcal B_\Lambda=4C_2(1-\mathcal B_\Lambda)$ ($=12(1-\mathcal B_\Lambda)$ for $SU(2)$) and $\nabla\mathcal B_\Lambda(U^*)=0$:
$$L\,\mathcal B_\Lambda(U^*) \;=\; 4C_2\big(1-\mathcal B_\Lambda(U^*)\big)\;=\;12\Big(1-\tfrac{|S|}{3}\Big)\;>\;0\quad\text{for }|S|\in\{1,2\},$$
independent of $\beta$ and of the volume: $L\mathcal B_\Lambda=+8$ at $\mathcal B_\Lambda=1/3$ and $+4$ at $\mathcal B_\Lambda=2/3$. Hence **no** strip $\Sigma$ located anywhere in $\{\mathcal B_\Lambda<1\}$ (for $SU(2)$; $\{\mathcal B_\Lambda<1\}$ is where the drift is repulsive) admits a pointwise negative drift, and Hypothesis 5.2 fails at $U^*$ with $\alpha=0$ (**every** plaquette has $\theta_p\in\{0,\pi\}$, so the forceful set $\mathcal R_{\theta_{\min},\kappa}(U^*)=\emptyset$).

Moreover the failure persists on a neighbourhood: for $U\in\mathcal N_\delta(U^*)$ with $|S|=2$,
$$L\,\mathcal B_\Lambda(U)\;\ge\;4-\big(96+384\beta\big)\delta^2\;>\;0\qquad\text{whenever }\delta<\frac{2}{\sqrt{96+384\beta}} ,$$
e.g. $\delta<0.0408$ at $\beta=6$ — and empirically much further ($L\mathcal B_\Lambda>0$ still at $\delta=0.10$).

### Derivation

**Exact drift identity (corpus Lemma 3.1, correct).** $S_W=\beta|P|\,\mathcal B_\Lambda$, so $\nabla S_W=\beta|P|\nabla\mathcal B_\Lambda$ and
$$L\,\mathcal B_\Lambda=\Delta_\Lambda\mathcal B_\Lambda-\langle\nabla S_W,\nabla\mathcal B_\Lambda\rangle=\Delta_\Lambda\mathcal B_\Lambda-\beta|P|\,\big\|\nabla\mathcal B_\Lambda\big\|^2 .$$
The corpus's strategy is to make the **second** term large; the affine identity fixes the first term exactly.

**At the witness.** $\nabla\mathcal B_\Lambda(U^*)=0$ (Lemma 1), so the entire negative contribution disappears and
$$L\,\mathcal B_\Lambda(U^*)=\Delta_\Lambda\mathcal B_\Lambda(U^*)=4C_2\big(1-\mathcal B_\Lambda(U^*)\big).$$
For $SU(2)$, $4C_2=12$, giving $+12,+8,+4,0,-4,-8,-12$ for $|S|=0,1,2,3,4,5,6$. The values $|S|=1,2$ are the counterexamples to strip drift.

**Failure of Hypothesis 5.2.** By construction every plaquette of $U^*$ has $\theta_p\in\{0,\pi\}$, so for any $\theta_{\min}>0,\kappa>0$ the forceful set is empty and the hypothesis holds only with $\alpha=0$; Proposition 6.1's conclusion $\|\nabla\mathcal B_\Lambda\|^2\ge\frac{\alpha}{\nu}\frac{c_{\rm force}^2}{|P|}$ degenerates to $\ge0$, and Corollary 7.1's threshold $\beta_*=4\nu C_\Delta/(\alpha c_{\rm force}^2)$ blows up. So the sufficient condition is not merely unproved — it is violated on the very configurations that populate the strip.

**Persistence on a neighbourhood [reconstructed].** For $U\in\mathcal N_\delta(U^*)$, $|S|=2$:
* Untwisted plaquettes gain at most $\widetilde z_p\le1-\cos(4\delta)\le8\delta^2$; twisted ones lose at most $8\delta^2$. Hence $\mathcal B_\Lambda(U)\le\tfrac23+8\delta^2$ and $\Delta_\Lambda\mathcal B_\Lambda(U)=12(1-\mathcal B_\Lambda)\ge12(\tfrac13-8\delta^2)=4-96\delta^2$.
* $\beta|P|\|\nabla\mathcal B_\Lambda\|^2=\frac{\beta}{|P|}\|\nabla\mathcal D_\Lambda\|^2\le\frac{\beta}{|P|}\cdot384|P|\delta^2=384\beta\delta^2$ by Step 3 of the previous item.
Subtracting gives $L\mathcal B_\Lambda\ge4-(96+384\beta)\delta^2$. $\square$

**Interpretation.** The mechanism is transparent: the diffusive term $\Delta_\Lambda\mathcal B_\Lambda=4C_2(1-\mathcal B_\Lambda)$ pushes $\mathcal B_\Lambda$ *up* toward the Haar value $1$ whenever $\mathcal B_\Lambda<1$; only the drift $-\beta|P|\|\nabla\mathcal B_\Lambda\|^2$ can pull it back down, and on the center stratum that term is exactly zero. Entropy wins pointwise, for every $\beta$, because the coupling multiplies a vanishing quantity.

### Constants and numbers

Exact values (independent of $\beta$, $L$; verified numerically at $L=2,4,6$ and $\beta=6$, $\varepsilon_{\rm fd}=5\times10^{-3}$, mc$=400$):
| $|S|$ | $B_{\rm avg}$ | predicted $L\mathcal B_\Lambda=12(1-B)$ | measured $\texttt{LV}$ (=$\texttt{lap}-\texttt{gip}$) | measured $\texttt{gip}$ |
|---|---|---|---|---|
| 0 | 0.0000 | $+12$ | $11.9739\pm0.0189$ | $9.5\times10^{-8}$ |
| 1 | 0.3333 | $+8$ | $7.9796\pm0.0161$ | $8.9\times10^{-8}$ |
| 2 | 0.6667 | $+4$ | $3.9903\pm0.0114$ | $8.6\times10^{-8}$ |
| 3 | 1.0000 | $0$ | $-0.0073\pm0.0114$ | $8.3\times10^{-8}$ |
| 4 | 1.3333 | $-4$ | $-4.0050\pm0.0116$ | $9.4\times10^{-8}$ |
| 6 | 2.0000 | $-12$ | $-11.9739\pm0.0189$ | $9.5\times10^{-8}$ |
Neighbourhood threshold: $L\mathcal B_\Lambda>0$ guaranteed for $\delta<2/\sqrt{96+384\beta}$; at $\beta=6$ this is $\delta<0.0408$. Measured $L\mathcal B_\Lambda$ at $\beta=6$, $|S|=2$: $+4.00$ ($\delta=0$), $+3.31$ ($\delta=0.05$), $+1.39$ ($\delta=0.10$), $-4.43$ ($\delta=0.20$).

**Caveat.** The maximal witness $|S|=6$ ($B_{\rm avg}=2$) does *not* violate strip drift — there the Laplacian term is $-12$. The strip-drift refutation needs a witness with $B_{\rm avg}<1$, which is precisely why the partial-flux members of the family ($|S|=1,2$) matter.

**Why it matters.** The smooth-barrier gluing lemma (`Doc3`) is a correct and reusable piece of analysis, but its only nontrivial input (H2) is the pointwise strip drift. Showing (H2) is false on an explicit stratum tells you the gluing lemma can never be applied to $\mathcal B_\Lambda$ as the order parameter for Wilson $SU(N)$ — the order parameter itself has to change.

---

## 6. Collapse of the averaged (last-surviving) coercivity form

`status: solid` · `kind: obstruction`

### Statement

The corpus's archived Appendix I offered a weaker, averaged variant of pairing coercivity that is **not** immediately killed by a single global-maximiser argument:
$$(\mathrm{I.8})\qquad \mathcal P_\Lambda(U)\;\ge\;c_2\,|P(\Lambda)|\,B_{\rm avg}(U)^2\;-\;C_2\,|P(\Lambda)| ,\qquad c_2>0,\ C_2\ge0\ \text{volume-independent}.$$

**Claim [reconstructed].** The center-flux family forces $C_2\ge c_2\,\big(1-\cos\tfrac{2\pi}{N}\big)^2$ — for $SU(2)$, $C_2\ge 4c_2$ — and consequently the right-hand side of (I.8) is **non-positive for every configuration**, so (I.8) is consistent but **vacuous**: it can never supply the negative drift required by Proposition 7.39.

### Derivation

**Step 1 (constraint from the witnesses).** Evaluate (I.8) at each member $U^*(S)$ of the center family. By Lemma 1, $\mathcal P_\Lambda(U^*(S))=0$, while $B_{\rm avg}(U^*(S))=\frac{|S|}{6}(1-\cos\frac{2\pi}{N})$. Hence (I.8) requires, for every $S$,
$$0\;\ge\;c_2|P|\Big(\tfrac{|S|}{6}\big(1-\cos\tfrac{2\pi}{N}\big)\Big)^{2}-C_2|P| \qquad\Longleftrightarrow\qquad C_2\;\ge\;c_2\Big(\tfrac{|S|}{6}\big(1-\cos\tfrac{2\pi}{N}\big)\Big)^{2}.$$
Taking $|S|=6$ (the maximal witness) gives the sharpest constraint
$$\boxed{\;C_2\;\ge\;c_2\,\big(1-\cos\tfrac{2\pi}{N}\big)^{2}\;}\qquad\text{i.e.}\qquad C_2\ge 4c_2\ \ \text{for }SU(2).$$
Note this is a volume-**independent** constraint, so unlike Assumption 7.38 it is not self-contradictory — the averaged form genuinely survives as an inequality.

**Step 2 (the range of $B_{\rm avg}$).** For $SU(N)$ with the fundamental representation, $\widetilde z_p\in[0,2]$ and hence $B_{\rm avg}\in[0,2]$; for $SU(2)$ the value $2$ is attained (by the maximal witness). More sharply, for $SU(2)$, $\max_U B_{\rm avg}(U)=2$ exactly, attained at $|S|=6$.

**Step 3 (vacuity for $SU(2)$).** With $C_2\ge4c_2$ and $B_{\rm avg}\le2$,
$$c_2|P|B_{\rm avg}^2-C_2|P|\;\le\;c_2|P|\big(B_{\rm avg}^2-4\big)\;\le\;0\qquad\text{for every }U\in M_\Lambda .$$
So the right-hand side of (I.8) is never positive: the inequality says at most '$\mathcal P_\Lambda\ge$ (something $\le0$)'.

**Step 4 (it cannot drive the drift).** Corollary 7.36 of the corpus gives
$$\frac{L_\Lambda W_\Lambda}{W_\Lambda}\le(\kappa C_V+\kappa^2C_\Gamma)\,\mathcal D_\Lambda-2\kappa\,\mathcal P_\Lambda .$$
To get negativity outside a **volume-uniform** core one needs the coercive lower bound on $\mathcal P_\Lambda$ to beat $\tfrac12(C_V+\kappa C_\Gamma)\mathcal D_\Lambda$, i.e. writing $x:=B_{\rm avg}=\mathcal D_\Lambda/|P|\in[0,2]$ and using (I.8),
$$c_2|P|x^2-C_2|P|\;\ge\;\tfrac12(C_V+\kappa C_\Gamma)\,|P|\,x \quad\Longleftrightarrow\quad c_2\big(x^2-4\big)\;\ge\;\tfrac12(C_V+\kappa C_\Gamma)\,x ,$$
where we used $C_2\ge4c_2$. The left side is $\le0$ on $x\in[0,2]$ and the right side is $\ge0$ (all constants positive), with equality only at $x=0$. So the required inequality has **no solution** $x>0$. $\square$

**Reading.** The three coercivity variants the corpus targets are exactly: (7.60)/(I.5) pointwise-with-constant-subtraction — refuted by extensivity; (I.9) off-core — refuted immediately; (I.8) averaged-with-extensive-subtraction — consistent but, once the center witnesses fix $C_2/c_2\ge(\max B_{\rm avg})^2$, provably useless. That closes the family.

### Constants and numbers

$SU(2)$: $C_2\ge 4c_2$; $\max_U B_{\rm avg}=2$; drift condition would need $c_2(x^2-4)\ge\tfrac12(C_V+\kappa C_\Gamma)x$ with $C_V=40$, $C_\Gamma=768$, which has no solution in $x\in(0,2]$.
$SU(3)$: $1-\cos(2\pi/3)=1.5$, so $C_2\ge2.25\,c_2$, and $\max_U B_{\rm avg}\ge1.5$; the same argument applies on $x\in(0,1.5]$ using only the center witnesses (the true $\max B_{\rm avg}$ for $SU(3)$ is $\ge1.5$, which is all that is needed).
Corpus numerics consistent with the collapse: the recorded ratio certificate misses its own target $C_{\rm TARGET}=20$, reporting $c_{\min}(\tau_0)=13.47$ (and elsewhere $c_{\min}\approx10.72$), i.e. 'coercivity not yet met'.

**Caveat.** Step 2's use of $\max_U B_{\rm avg}=2$ is exact for $SU(2)$; for general $SU(N)$ I only use the center value $1-\cos(2\pi/N)$, which is a lower bound on the true maximum — enough for the argument on the corresponding sub-range.

**Why it matters.** CAND-010 in the corpus noted that the averaged form (I.8) survives the compactness/global-maximiser refutation. This closes that last door: the explicit witness family pins the ratio $C_2/c_2$ from below by the square of the maximal defect density, which is exactly the amount needed to make the bound's right-hand side identically non-positive.

---

## 7. Numerical refutation of the published SU(2) drift certificates

`status: solid` · `kind: numerical_result`

### Statement

The corpus's certificates, extracted verbatim:

**(C1)** (`su2_outside_core_certificates.md`, holdout, $n_\sigma=2$, pooled over $L\in\{8,12,16\}$, $\beta=6$): on $\{B_{\rm avg}\ge\tau_0\}$ with
$$\tau_0=0.3883,\qquad c_{\min}(\tau_0)=20.9510,\qquad d_{\max}(\tau_0)=-2.6909,$$
i.e. $\texttt{gip}\ge 20.9510\,B_{\rm avg}$ and $\texttt{LV}\le-2.6909\,B_{\rm avg}$.

**(C2)** (`01_su2_generator_laplacian_drift.md`, App. B, holdout): $\tau^*\approx0.2158$ with $\lambda^*=11.0012\,(L{=}8),\ 10.7230\,(L{=}12),\ 10.9799\,(L{=}16)$ in $\texttt{LV}+2\sigma\le-\lambda^*B_{\rm avg}$.

**(C3)** (`su2-drift-certificates.md`, §6): PASS at $\beta=12$, $\tau_0\approx0.2158$, $c_{\min,\rm all}\approx21.44$, $d_{\max,\rm all}\approx-21.44$, simultaneously for $L=8,12,16$.

**Claim.** The double-flux center witness ($B_{\rm avg}=2/3=0.6667$, outside every one of these cores) violates every one of (C1),(C2),(C3), by a wide margin, at every $\beta$, on every even lattice, and the violation survives random tangent perturbations of size $\delta=0.05$ and $\delta=0.10$. Reproduced with an independent numpy reimplementation of the estimators in `su2_drift_simulation.py`.

**$\beta$-independence.** The corpus's own $\beta$-rescaling rule (`beta_rescale_components`) keeps $\texttt{lap}$ fixed and scales $\texttt{gip}$ linearly in $\beta$. Since $\texttt{gip}(U^*)=0$ exactly, $\texttt{gip}$ stays $0$ and $\texttt{LV}(U^*)=\texttt{lap}(U^*)=+4$ for **every** $\beta$. The $\beta$-scan that produced (C3) therefore cannot escape the witness.

### Derivation

**Estimators (identical to the corpus code).** With $\bar V=1+B_{\rm avg}$, $S_\beta=\beta\sum_p z_p$, and i.i.d. standard Gaussian $\Xi\in(\mathbb R^3)^{E}$ per direction,
$$\texttt{lap}=\frac{\bar V(Ue^{+\varepsilon\Xi})+\bar V(Ue^{-\varepsilon\Xi})-2\bar V(U)}{\varepsilon^2},\qquad \texttt{gip}=\Big(\frac{S(Ue^{+\varepsilon\Xi})-S(Ue^{-\varepsilon\Xi})}{2\varepsilon}\Big)\Big(\frac{\bar V(Ue^{+\varepsilon\Xi})-\bar V(Ue^{-\varepsilon\Xi})}{2\varepsilon}\Big),$$
$\texttt{LV}=\texttt{lap}-\texttt{gip}$, averaged over `mc` directions with the sample standard error. Unbiasedness as $\varepsilon\to0$: $\mathbb E[\Xi_i\Xi_j]=\delta_{ij}$ makes $\mathbb E[(D_\Xi S)(D_\Xi\bar V)]=\langle\nabla S,\nabla\bar V\rangle$, and the second symmetric difference averages to the trace of the Hessian.

**Independent reimplementation.** I rewrote these estimators in numpy (same quaternion algebra, same `torch.roll`-style plaquette, same $\exp$ with stable sinc, same mean/SE accumulation) and ran them on the exact witnesses. Independently, I computed $\|\nabla\mathcal D_\Lambda\|^2$ by the exact staple/projection route (no finite differences) as a cross-check; it returns identically $0$.

**Result table** ($L=4$, $|P|=1536$, $\beta=6$, $\varepsilon_{\rm fd}=5\times10^{-3}$, mc$=400$, seed $12345$):
| config | $B_{\rm avg}$ | $\texttt{lap}$ | SE | $\texttt{gip}$ | $\texttt{LV}$ | $12(1-B)$ | $\sum_\ell\|F_\ell\|^2$ |
|---|---|---|---|---|---|---|---|
| trivial $|S|{=}0$ | 0.0000 | 11.9739 | 0.0189 | $9.47\times10^{-8}$ | 11.9739 | 12.0000 | $0$ |
| single $|S|{=}1$ | 0.3333 | 7.9796 | 0.0161 | $8.87\times10^{-8}$ | 7.9796 | 8.0000 | $0$ |
| double $|S|{=}2$ | 0.6667 | 3.9903 | 0.0114 | $8.60\times10^{-8}$ | 3.9903 | 4.0000 | $0$ |
| triple $|S|{=}3$ | 1.0000 | $-0.0073$ | 0.0114 | $8.27\times10^{-8}$ | $-0.0073$ | 0.0000 | $0$ |
| quad $|S|{=}4$ | 1.3333 | $-4.0050$ | 0.0116 | $9.42\times10^{-8}$ | $-4.0050$ | $-4.0000$ | $0$ |
| maximal $|S|{=}6$ | 2.0000 | $-11.9739$ | 0.0189 | $9.47\times10^{-8}$ | $-11.9739$ | $-12.0000$ | $0$ |

**Certificate check against (C1)** ($\tau_0=0.3883$, need $\texttt{gip}\ge20.951B$, $\texttt{LV}\le-2.6909B$), $L=4$, $\beta=6$, mc$=400$:
| witness | $\delta$ | $B_{\rm avg}$ | $\texttt{gip}$ | required | $\texttt{LV}$ | required | verdict |
|---|---|---|---|---|---|---|---|
| double | 0.00 | 0.6667 | $9.57\times10^{-8}$ | $\ge13.967$ | $+4.0020$ | $\le-1.794$ | gip FAIL, LV FAIL |
| double | 0.05 | 0.6719 | $0.6303$ | $\ge14.078$ | $+3.3060$ | $\le-1.808$ | gip FAIL, LV FAIL |
| double | 0.10 | 0.6875 | $2.356$ | $\ge14.404$ | $+1.3907$ | $\le-1.850$ | gip FAIL, LV FAIL |
| double | 0.20 | 0.7449 | $7.478$ | $\ge15.606$ | $-4.4263$ | $\le-2.004$ | gip FAIL, LV ok |
| triple | 0.00 | 1.0000 | $9.27\times10^{-8}$ | $\ge20.951$ | $-0.0035$ | $\le-2.691$ | gip FAIL, LV FAIL |
| triple | 0.05 | 1.0002 | $0.7421$ | $\ge20.955$ | $-0.7494$ | $\le-2.691$ | gip FAIL, LV FAIL |
| triple | 0.10 | 1.0009 | $2.785$ | $\ge20.970$ | $-2.8018$ | $\le-2.693$ | gip FAIL, LV ok |
| triple | 0.20 | 1.0039 | $8.984$ | $\ge21.033$ | $-9.0375$ | $\le-2.701$ | gip FAIL, LV ok |
The pairing certificate fails at **every** perturbation size tested; the drift certificate fails out to $\delta=0.10$.

**Check against (C2)** ($\beta=6$, $\tau^*=0.2158$, $\lambda^*\approx10.76$): need $\texttt{LV}\le-10.76\times0.6667=-7.17$; measured $+4.00$. FAIL.
**Check against (C3)** ($\beta=12$, $\tau_0=0.2158$, $c_{\min}=21.44$, $d_{\max}=-21.44$): by $\beta$-rescaling $\texttt{gip}=0$ and $\texttt{LV}=+4$; need $\texttt{gip}\ge14.3$ and $\texttt{LV}\le-14.3$. FAIL both.

**$\varepsilon$-convergence** ($L=4$, $|S|=2$, mc$=2000$, exact $\texttt{lap}=4$): $\texttt{lap}=4.0035,4.0067,4.0075,4.0077,4.0077$ at $\varepsilon=2\times10^{-2},10^{-2},5\times10^{-3},2\times10^{-3},10^{-3}$ (SE $\approx0.0053$), and $\texttt{gip}=2.30\times10^{-5},1.44\times10^{-6},8.99\times10^{-8},2.30\times10^{-9},1.44\times10^{-10}$, i.e. exactly $O(\varepsilon^4)$ — the signature of an identically zero gradient.

**Volume independence** ($|S|=2$, $\beta=6$, $\varepsilon=5\times10^{-3}$, mc$=400$): $L=2,4,6$ give $B_{\rm avg}=0.666667$, $\texttt{lap}=4.0873\pm0.0550,\ 4.0037\pm0.0119,\ 4.0098\pm0.0050$, $\texttt{gip}\approx9\times10^{-8}$, $\sum_\ell\|F_\ell\|^2=0$ exactly in all three.

**Exact $L_\Lambda V_\Lambda$ for the corpus's $V_\Lambda=\sum_p\widetilde z_p^2$** (using $\Delta_\Lambda\widetilde z_p=12(1-\widetilde z_p)$ and $\nabla\widetilde z_p=0$): $L_\Lambda V_\Lambda(U^*)=24\sum_p\widetilde z_p(1-\widetilde z_p)$, giving $-8|P|$, $-16|P|$, $-48|P|$ for $|S|=1,2,6$.

### Constants and numbers

See the tables in the derivation. Corpus certificate constants reproduced verbatim: (C1) $\tau_0=0.3883$, $c_{\min}=20.9510$, $d_{\max}=-2.6909$, $n_\sigma=2$, holdout, $L\in\{8,12,16\}$, $\beta=6$. (C2) $\tau^*=0.2158/0.2157/0.2159$ and $\lambda^*=11.0012/10.7230/10.9799$ at $L=8/12/16$, coverage $68.9\%/70.2\%/70.8\%$. (C3) PASS at $\beta=12$, $\tau_0\approx0.2158$, $c_{\min,\rm all}\approx21.44$, $d_{\max,\rm all}\approx-21.44$. $\beta$-sweep at $L=16$: $(\beta,\tau_0,\lambda_0)=(2,0.6361,2.1158),(4,0.6361,7.1795),(6,0.2158,10.7627),(8,0.2158,14.3460),(10,0.2158,17.9292)$, i.e. $\lambda_0/\beta\approx1.79$ for $\beta\ge4$. Affine Laplacian fit (corpus, holdout): $\hat a=11.999129/11.999289/11.999174$, $\hat b=-11.998889/-11.999223/-11.999189$, $R^2=0.9999993/0.9999999/1.0000000$, $\max|\Delta V-(12-12B)|=1.92\times10^{-2}/8.34\times10^{-3}/5.10\times10^{-3}$ at $L=8/12/16$.
Run parameters of my reproduction: numpy 2.3.5, Python 3.12.9, $d=4$, $L\in\{2,4,6\}$, $\beta=6$ (and $\beta=12$ by rescaling), $\varepsilon_{\rm fd}\in\{10^{-3},2\times10^{-3},5\times10^{-3},10^{-2},2\times10^{-2}\}$, mc $\in\{400,2000\}$, float64 throughout, seeds $12345/999/2024/31337$.

### Code

# Independent numpy reimplementation of su2_drift_simulation.py's estimators,
# specialised to a single deterministic configuration.
# File: <scratchpad>/center_flux_witness.py     (run: python center_flux_witness.py)

def estimate(U, beta, eps=5e-3, mc=400, seed=0):
    """lap ~ Delta Vbar, gip ~ <grad S_beta, grad Vbar>, LV = lap - gip, with MC SEs."""
    import numpy as np
    rng = np.random.default_rng(seed)
    _, V0, B0 = observables(U, beta)          # Vbar = 1 + Bavg,  S = beta*sum_p z_p
    laps, gips, lvs = [], [], []
    for _ in range(mc):
        Xi  = rng.standard_normal(U.shape[:-1] + (3,))   # one su(2) vector per link
        e_p = qexp(eps * Xi); e_m = qconj(e_p)
        Sp, Vp, _ = observables(qmul(U, e_p), beta)
        Sm, Vm, _ = observables(qmul(U, e_m), beta)
        lap = (Vp + Vm - 2.0 * V0) / (eps * eps)
        dS  = (Sp - Sm) / (2.0 * eps); dV = (Vp - Vm) / (2.0 * eps)
        gip = dS * dV
        laps.append(lap); gips.append(gip); lvs.append(lap - gip)
    f = lambda a: (float(np.mean(a)), float(np.std(a, ddof=1) / np.sqrt(len(a))))
    lapm, lapse = f(laps); gipm, gipse = f(gips); lvm, lvse = f(lvs)
    return dict(Bavg=float(B0), lap=lapm, lap_se=lapse, gip=gipm, gip_se=gipse,
                LV=lvm, LV_se=lvse)

def perturb(U, delta, seed):
    """U_l -> U_l exp(delta * Xi_l), Xi_l ~ N(0, I_3): random tangent noise of size delta."""
    import numpy as np
    rng = np.random.default_rng(seed)
    return qmul(U, qexp(delta * rng.standard_normal(U.shape[:-1] + (3,))))

**Caveat.** My reproduction is at $L\le6$ while the certificates were produced at $L\in\{8,12,16\}$; but every quantity involved is exactly volume-independent for these homogeneous configurations (verified at $L=2,4,6$), and the analytic argument needs no numerics at all.

**Why it matters.** The certificates were the corpus's strongest empirical evidence for the coercivity route, and they were produced by sampling $\sigma$-perturbed identity fields and Haar-random fields only — a sampler that can never reach the center stratum. A deterministic two-line configuration falsifies them, which shows the certificate methodology (sample, fit ratios, add $2\sigma$) cannot certify a universally quantified pointwise inequality.

---

## 8. Supporting exact identities: affine Laplacian law, staple/projection form of the pairing term, and the explicit SU(2) constants

`status: solid` · `kind: derivation`

### Statement

Three exact results from the corpus that the obstruction uses, reproduced with complete proofs and explicit constants.

**(a) Affine Laplacian identity.** Let $G$ be compact, $\rho$ a faithful unitary representation with $\Delta_G\,\Re\mathrm{Tr}\rho=-C_2\,\Re\mathrm{Tr}\rho$ (i.e. the fundamental character is a Laplacian eigenfunction with quadratic-Casimir eigenvalue $C_2$), and $\Delta_\Lambda=\sum_\ell\Delta_\ell$ on $M_\Lambda=G^{E(\Lambda)}$ with the product bi-invariant metric. Then for every plaquette $p$ (with $m_\partial=4$ boundary links),
$$\boxed{\ \Delta_\Lambda\widetilde z_p \;=\; 4\,C_2\,\big(1-\widetilde z_p\big)\ }$$
and hence $\Delta_\Lambda B_{\rm avg}=4C_2(1-B_{\rm avg})$ and $\Delta_\Lambda\bar V=4C_2(1-B_{\rm avg})$ for $\bar V=1+B_{\rm avg}$. For $SU(2)$, $C_2=3$, so $\Delta_\Lambda\bar V=12-12B_{\rm avg}$.

**(b) Staple/projection identity for the pairing term.** For $S_W=\beta\mathcal D_\Lambda$ and $\bar V=1+B_{\rm avg}=1+\mathcal D_\Lambda/|P|$,
$$\boxed{\ \big\langle\nabla S_W,\nabla\bar V\big\rangle=\frac{\beta}{|P|}\big\|\nabla\mathcal D_\Lambda\big\|^2=\frac{\beta}{|P|}\sum_{\ell\in E}\big\|\Pi_{\mathfrak{su}(2)}\big(U_\ell\Omega_\ell\big)\big\|^2\ \ge\ 0,\ }$$
where $\Omega_\ell=\sum_{p\ni\ell}K_{p,\ell}$ is the sum of the $2(D-1)$ staples at $\ell$ and $\Pi_{\mathfrak{su}(2)}(M)=\tfrac12(M-M^\dagger)-\tfrac{1}{2}\mathrm{tr}(\tfrac12(M-M^\dagger))\mathbf1$ is the orthogonal projection onto the Lie algebra (in quaternion coordinates: the imaginary part).

**(c) Explicit $SU(2)$ constants** for the corpus's uniform-derivative bookkeeping (Lemmas 7.25–7.29, Prop. 7.31, Cor. 7.36), in the normalization $SU(2)\cong S^3$ of radius $1$:
$$C^{(1)}_{\widetilde z}=1,\quad C^{(2)}_{\widetilde z}=1,\quad C_\Delta=3,\quad C_\nabla=2,\quad \nu=6,\quad m_\partial=4,$$
$$A_1=8C_\Delta=24,\quad A_2=8C_\nabla=16,\quad A_3=64\nu C_\nabla=768,\quad C_V=A_1+A_2=40,\quad C_\Gamma=A_3=768 .$$

### Derivation

**(a).** Fix a plaquette $p$ and one boundary link $\ell\in\partial p$. Holding the other three boundary links fixed, $U_p=A\,U_\ell^{\sigma}\,B$ with $A,B$ fixed and $\sigma=\pm1$; the map $g\mapsto Ag^\sigma B$ is an isometry of $(G,g_G)$ because the metric is bi-invariant. Isometries commute with the Laplace–Beltrami operator: $\Delta(f\circ\Psi)=(\Delta f)\circ\Psi$. Therefore, with $w(g):=\frac1n\Re\mathrm{Tr}\rho(g)$,
$$\Delta_\ell\, w(U_p) = \big(\Delta_G w\big)(U_p) = -C_2\,w(U_p).$$
Summing over the four boundary links (links outside $\partial p$ contribute $0$ since $\widetilde z_p$ is independent of them),
$$\Delta_\Lambda\,w(U_p)=-4C_2\,w(U_p).$$
Since $\widetilde z_p=1-w(U_p)$ and $\Delta_\Lambda 1=0$,
$$\Delta_\Lambda\widetilde z_p=+4C_2\,w(U_p)=4C_2\big(1-\widetilde z_p\big).\qquad\square$$
*Casimir value for $SU(2)$:* the code's exponential map is $\exp(v)=(\cos|v|,\ \mathrm{sinc}(|v|)v)$, so $SU(2)$ is the unit $S^3$ with $d_G(\mathbf 1,\exp v)=|v|$. For a radial function on the unit $S^3$, $\Delta=\partial_\theta^2+2\cot\theta\,\partial_\theta$. With $w=\cos\theta$: $\Delta w=-\cos\theta-2\cos\theta=-3\cos\theta=-3w$. So $C_2=3$, $4C_2=12$, matching the corpus's empirical fit $\hat a\simeq11.9991$, $\hat b\simeq-11.9989$, $R^2>0.9999993$.

**(b).** Since $S_W=\beta\mathcal D_\Lambda$ and $\bar V=1+\mathcal D_\Lambda/|P|$, the two gradients are **parallel**:
$$\nabla S_W=\beta\nabla\mathcal D_\Lambda,\qquad \nabla\bar V=\tfrac1{|P|}\nabla\mathcal D_\Lambda\ \Longrightarrow\ \langle\nabla S_W,\nabla\bar V\rangle=\tfrac{\beta}{|P|}\|\nabla\mathcal D_\Lambda\|^2\ge0 .$$
This makes the corpus's 'proof object B' (the empirically observed nonnegativity of $\texttt{gip}$ in 2048/2048 sampled configurations) a triviality — a scaled squared norm — and simultaneously explains why $\texttt{gip}$ can be *exactly zero*: it vanishes iff $\nabla\mathcal D_\Lambda=0$, i.e. at critical points of the Wilson action.
*Staple form.* Write $U_p=U_\ell K_{p,\ell}$ for $p\ni\ell$. With the left-invariant variation $U_\ell(t)=e^{tX}U_\ell$, $X\in\mathfrak{su}(2)$,
$$\frac{d}{dt}\Big|_0\Big(\tfrac12\Re\mathrm{Tr}(U_\ell(t)K_{p,\ell})\Big)=\tfrac12\Re\mathrm{Tr}\big(X\,U_\ell K_{p,\ell}\big).$$
Summing over $p\ni\ell$ and using $\langle A,B\rangle=-\tfrac12\mathrm{Tr}(AB)$ on $\mathfrak{su}(2)$,
$$D_X\mathcal D_\Lambda=-\tfrac12\Re\mathrm{Tr}\big(X\,U_\ell\Omega_\ell\big)=\big\langle X,\,-\Pi_{\mathfrak{su}(2)}(U_\ell\Omega_\ell)\big\rangle\ \Longrightarrow\ \nabla_\ell\mathcal D_\Lambda=-\Pi_{\mathfrak{su}(2)}(U_\ell\Omega_\ell).$$
*Representation-theoretic reading (corpus §6.2, correct):* $\mathrm{End}(\mathbb C^2)\cong\tfrac12\otimes\tfrac12^*\cong 0\oplus1$; the plaquette defect lives in the spin-$0$ (character) channel while the force lives in the spin-$1$ (adjoint) channel, and $\Pi_{\mathfrak{su}(2)}$ is exactly the adjoint projector. **The center-flux obstruction is precisely the statement that the adjoint channel of a scalar matrix is empty**: $\Pi_{\mathfrak{su}(2)}(\zeta I)=0$.
*Reformulation of coercivity (corpus §4, correct):* $\langle\nabla S_W,\nabla\bar V\rangle\ge c_\star B_{\rm avg}$ on $\{B_{\rm avg}\ge\tau_0\}$ $\iff$ $\|\nabla\mathcal D_\Lambda\|^2\ge\kappa_\star\mathcal D_\Lambda$ with $\kappa_\star=c_\star/\beta$: a Polyak–Łojasiewicz inequality for the total defect outside a small-defect core.

**(c).** In the unit-$S^3$ normalization, $\widetilde z(\theta)=1-\cos\theta$:
* $\nabla\widetilde z$ is radial with $|\nabla\widetilde z|=|\partial_\theta(1-\cos\theta)|=|\sin\theta|\le1$, so $C^{(1)}_{\widetilde z}=1$.
* $\mathrm{Hess}\,\widetilde z$ has radial eigenvalue $\partial_\theta^2\widetilde z=\cos\theta$ and tangential eigenvalues $\cot\theta\cdot\partial_\theta\widetilde z=\cos\theta$; so $\mathrm{Hess}\,\widetilde z=\cos\theta\cdot g_G$, $|\mathrm{Hess}|_{\rm op}=|\cos\theta|\le1$, $C^{(2)}_{\widetilde z}=1$.
* $\Delta_G\widetilde z=\mathrm{tr}\,\mathrm{Hess}=3\cos\theta$, so $C_\Delta=\sup_G|\Delta_G\widetilde z|=3$ (consistent with $\Delta_G\widetilde z=C_2(1-\widetilde z)$, $C_2=3$).
* Gradient domination: $\dfrac{|\nabla\widetilde z|^2}{\widetilde z}=\dfrac{\sin^2\theta}{1-\cos\theta}=\dfrac{(1-\cos\theta)(1+\cos\theta)}{1-\cos\theta}=1+\cos\theta=2-\widetilde z\in[0,2]$, so $C_\nabla=\sup=2$, attained in the limit $\theta\to0$. (This is the corpus's Lemma 7.26; its limiting value $2/(n\lambda_\rho)$ therefore fixes $n\lambda_\rho=1$.)
* Feeding $C_\Delta=3$, $C_\nabla=2$, $\nu=6$ into Prop. 7.31 gives $A_1=8C_\Delta=24$, $A_2=8C_\nabla=16$, $A_3=64\nu C_\nabla=768$; hence $C_V=40$, $C_\Gamma=768$, and Prop. 7.39's admissibility condition becomes $c_{\rm pair}>40$ with $\kappa\le(c_{\rm pair}-40)/1536$.

**Note on $|\nabla\widetilde z|^2=\widetilde z(2-\widetilde z)$.** This single identity contains the whole obstruction in miniature: the force vanishes not only at $\widetilde z=0$ but also at $\widetilde z=2$. Any inequality of the form $|\nabla\widetilde z|^2\ge c\,\widetilde z$ with $c>0$ must exclude a neighbourhood of the center element $-\mathbf 1$; the corpus states this correctly (`06_pairing_staple_projection_coercivity(1).md`, §5, and `02_smooth_gluing_strip_drift_force_density.md`, §4), and the center-flux family is the statement that this exclusion cannot be arranged, because there exist configurations in which *every* plaquette sits at $\theta=\pi$ (or at $\theta\in\{0,\pi\}$) simultaneously.

### Constants and numbers

$C_2(\text{fund},SU(2))=3$; $4C_2=12$; $\Delta_\Lambda\bar V=12-12B_{\rm avg}$ exactly. Corpus empirical confirmation (holdout regression $\Delta V\approx a+bB_{\rm avg}$, $\beta=6$, mc$=256$, $K_{\rm total}=2048$): $L=8$: $(\hat a,\hat b,R^2)=(11.999129,-11.998889,0.9999993)$, $\max|\Delta V-(12-12B)|=1.9225\times10^{-2}$; $L=12$: $(11.999289,-11.999223,0.9999999)$, $8.3439\times10^{-3}$; $L=16$: $(11.999174,-11.999189,1.0000000)$, $5.1037\times10^{-3}$. Split-half decomposition residual $z$: $\%(|z|>2)=3.66/4.30/4.69\%$, $\max|z|=3.231/3.224/3.498$.
$SU(2)$ constants: $C^{(1)}_{\widetilde z}=1$, $C^{(2)}_{\widetilde z}=1$, $C_\Delta=3$, $C_\nabla=2$, $\nu=6$, $m_\partial=4$; $A_1=24$, $A_2=16$, $A_3=768$; $C_V=40$, $C_\Gamma=768$; Prop. 7.39 needs $c_{\rm pair}>40$, $\kappa\le(c_{\rm pair}-40)/1536$.
General $SU(N)$: $\Delta_\Lambda\widetilde z_p=4C_2(1-\widetilde z_p)$; center defect $1-\cos(2\pi k/N)$; each link lies in $\nu=2(d-1)$ plaquettes.

**Caveat.** The value $C_2=3$ (hence the constant $12$) is normalization-dependent: it is fixed here by the exponential map used in `su2_drift_simulation.py`, which makes $SU(2)$ the unit $3$-sphere. Under a rescaled metric $C_2$ rescales and every downstream constant with it; the vanishing statements of Lemma 1 are normalization-independent.

**Why it matters.** These are the genuinely correct pieces of the corpus's Lyapunov machinery, and they are what make the obstruction sharp rather than vague: the affine Laplacian identity gives the drift *exactly* at the witness ($L\mathcal B_\Lambda=4C_2(1-\mathcal B_\Lambda)$, no estimation), the staple/projection identity shows the pairing term is a squared norm that vanishes exactly at critical points, and the explicit constants pin down how large a coercivity constant would have been needed ($c_{\rm pair}>40$ for SU(2)).

---

## 9. Verification harness: center_flux_witness.py / center_flux_checks2.py / sun_center_check.py

`status: solid` · `kind: code`

### Statement

Three standalone scripts (numpy + scipy only, no GPU, seconds to run at $L\le6$) that (i) construct the $Z_N$ center-flux family on a periodic $L^4$ lattice, (ii) reproduce the corpus's Monte-Carlo generator estimators exactly, (iii) compute $\|\nabla\mathcal D_\Lambda\|^2$ by an independent exact (finite-difference-free) staple/projection route, (iv) test the published drift certificates against the witness and its random perturbations, and (v) confirm the construction for $SU(2),SU(3),SU(4)$ by direct matrix algebra.

### Derivation

**`center_flux_witness.py`** — quaternion $SU(2)$ ops (`qmul`, `qconj`, `qexp` with the same stable sinc expansion as the corpus code); `plaquette(U,mu,nu)` using `np.roll` in the same orientation convention; `observables(U,beta)` returning $(S,\bar V,B_{\rm avg})$; `center_flux_config(L, twisted_planes)` building $U^*$; `estimate(U,beta,eps,mc,seed)` reproducing $\texttt{lap}/\texttt{gip}/\texttt{LV}$ with standard errors; `perturb(U,delta,seed)` applying $U_\ell\mapsto U_\ell\exp(\delta\Xi_\ell)$; `exact_link_force_norm(U)` computing $\sum_\ell\|\Pi_{\mathfrak{su}(2)}(U_\ell\Omega_\ell)\|^2$ from the forward and backward staples with no finite differences. Running it as `__main__` prints the six-row witness table and the certificate check table quoted in the numerical item.

**`center_flux_checks2.py`** — four follow-up sections: (1) $\varepsilon$-convergence of $\texttt{lap}$ and the $O(\varepsilon^4)$ decay of $\texttt{gip}$; (2) volume independence at $L=2,4,6$; (3) exact plaquette-defect spectra and the exact $L_\Lambda V_\Lambda=2\sum_p\widetilde z_p\cdot12(1-\widetilde z_p)$ for $V_\Lambda=\sum_p\widetilde z_p^2$; (4) the PL ratio $\|\nabla\mathcal D\|^2/\mathcal D$ over an $\ell^\infty$-ball of radius $\delta$, compared against the analytic bound $768\delta^2$.

**`sun_center_check.py`** — no quaternions: builds $U^*_{x,\mu}=\omega^{e_\mu(x)}I_N$ as complex $N\times N$ matrices, computes plaquettes by matrix products with `np.roll`, and computes $\|\nabla S_W\|^2$ by exact central differences at $\varepsilon=10^{-5}$ along an orthonormal basis of $\mathfrak{su}(N)$ on **every** link (`scipy.linalg.expm`). Confirms $\|\nabla S_W\|^2=0$ (to $\le4\times10^{-17}$) and the defect value $1-\cos(2\pi/N)$ for $N=2,3,4$, both when $N\mid L$ and when it does not.

**How to run.** `python center_flux_witness.py` (about 30 s at $L=4$, mc$=400$); `python center_flux_checks2.py` (about 3 min, imports the first); `python sun_center_check.py` (about 40 s at $L=2$; the exact-gradient loop is $O(L^4\cdot4\cdot\dim\mathfrak{su}(N))$ action evaluations, so keep $L$ small).

**Files.** `C:\Users\Alex\AppData\Local\Temp\claude\F--ANTIGRAVITY-antigravity-playground-scalar-cluster-proof\fd74385b-6527-446a-ae5a-90acb16ad82a\scratchpad\center_flux_witness.py`, `...\center_flux_checks2.py`, `...\sun_center_check.py`.

**Corpus code being reproduced.** `F:\ANTIGRAVITY\antigravity\playground\scalar-cluster\proof\LYAPUNOV\Core_Drift_Lyapunov\su2_drift_simulation.py` (612 lines, PyTorch, CPU/CUDA, argparse CLI, seeded, chunked over configs and MC directions, writes a flat `.npz`). Its estimators are correct; its only sampling modes are $\sigma$-perturbed identity fields and Haar-random fields, neither of which can reach the center stratum — which is precisely why its certificates missed this counterexample.

### Constants and numbers

Defaults used: $d=4$, $L\in\{2,3,4,6\}$, $\beta=6$, $\varepsilon_{\rm fd}=5\times10^{-3}$ (swept $10^{-3}\dots2\times10^{-2}$), mc $\in\{400,2000\}$, float64, seeds $\{0,7,999,2024,12345,31337\}$. Corpus code defaults (for comparison): `--Ls 8 12 16 --K_total 512 --beta 6.0 --eps_fd 5e-3 --mc 128 --mc_chunk 16 --sigma_list 0.0 0.1 0.2 0.4 0.8 1.6 --frac_haar 0.25 --dtype float64 --xi_dtype float32`.

### Code

# --- core of center_flux_witness.py (SU(2), quaternion coords) ---
import numpy as np

def qmul(q1, q2):
    a1,b1,c1,d1 = q1[...,0],q1[...,1],q1[...,2],q1[...,3]
    a2,b2,c2,d2 = q2[...,0],q2[...,1],q2[...,2],q2[...,3]
    return np.stack([a1*a2-b1*b2-c1*c2-d1*d2,
                     a1*b2+b1*a2+c1*d2-d1*c2,
                     a1*c2-b1*d2+c1*a2+d1*b2,
                     a1*d2+b1*c2-c1*b2+d1*a2], axis=-1)

def qconj(q):
    out = q.copy(); out[...,1:] *= -1.0; return out

def qexp(v):                       # su(2)=R^3 -> SU(2)=S^3, stable sinc
    th = np.linalg.norm(v, axis=-1, keepdims=True)
    safe = np.where(th > 1e-8, th, 1.0)
    sinc = np.where(th > 1e-8, np.sin(safe)/safe, 1.0 - th*th/6.0)
    return np.concatenate([np.cos(th), sinc*v], axis=-1)

def plaquette(U, mu, nu):          # U: (L,L,L,L, dir=4, quat=4)
    Umu, Unu = U[...,mu,:], U[...,nu,:]
    return qmul(qmul(qmul(Umu, np.roll(Unu,-1,axis=mu)),
                     qconj(np.roll(Umu,-1,axis=nu))), qconj(Unu))

def observables(U, beta):          # (S, Vbar, Bavg);  z_p = 1 - a_p
    dsum = 0.0; dmean = 0.0; cnt = 0
    for mu in range(4):
        for nu in range(mu+1, 4):
            defect = 1.0 - plaquette(U, mu, nu)[...,0]
            dsum += defect.sum(); dmean += defect.mean(); cnt += 1
    Bavg = dmean/cnt
    return beta*dsum, 1.0+Bavg, Bavg

# center_flux_config, estimate, perturb, exact_link_force_norm: see items above.
# Reproduce everything:  python center_flux_witness.py ; python center_flux_checks2.py

**Caveat.** The scripts live in a session scratchpad, not in the corpus; they must be copied out to be preserved. `sun_center_check.py` requires scipy for `expm`.

**Why it matters.** The refutation is analytic and needs no numerics, but a reader who wants to check it in five minutes can: the harness reproduces the corpus's own estimators, hits the witness, and shows the pairing term is zero to $O(\varepsilon^4)$ machine noise while the defect is extensive.

---

## How these fit together

The eight items form one closed argument, and it plugs into the rest of the corpus at a single, identifiable joint.

(1) The corpus's Lyapunov pipeline (`LYAPUNOV/Core_Drift_Lyapunov/## 7. Lyapunov drift ...txt`) is a chain: Lemma 7.33 (diffusion chain rule) -> Lemma 7.34 (exponential chain rule) -> Prop. 7.35 (exact drift identity for V_Lambda = sum_p z_p^2) -> Prop. 7.31 + Cor. 7.36 (every diffusion-generated term is bounded by D_Lambda with volume-uniform constants) -> **Assumption 7.38 (the pairing coercivity)** -> Prop. 7.39 (Foster-Lyapunov) -> Section 7.4 (local-to-global Poincare/LSI). Everything up to and including Cor. 7.36 is correct calculus and survives; item 8 supplies the explicit SU(2) constants (C_Delta=3, C_nabla=2, A_1=24, A_2=16, A_3=768, C_V=40) that the corpus left symbolic. Items 1-3 remove Assumption 7.38, which the corpus itself (Remark 7.40) calls "the only remaining obstruction". So the chain is severed at exactly one link, and the severing is a two-line algebraic fact.

(2) The same obstruction appears three more times in the corpus wearing different clothes, and one witness kills all of them: as the Polyak-Lojasiewicz inequality ||grad D||^2 >= kappa D (item 4, via the staple/projection reformulation in `Maxwell_Covariance/06_pairing_staple_projection_coercivity(1).md` Section 4); as the strip-drift hypothesis (H2) of the smooth-barrier gluing lemma (item 5, `Gluing_Typicality/Doc3_Smooth_Gluing_Lemma_Barrier.md` and `Core_Drift_Lyapunov/02_smooth_gluing_strip_drift_force_density.md` Hypothesis 5.2 / Cor. 7.1); and as the numerically certified ratio bounds (item 7, `Simulations_Evidence/su2_outside_core_certificates.md` and `su2-drift-certificates.md`). Item 6 closes the last variant (the averaged form (I.8) from the archived Appendix I) that a single global-maximiser argument leaves standing.

(3) The corpus already knew the *local*, one-plaquette version of this obstruction and states it correctly: |grad b| ∝ |sin θ| = sqrt(z(2-z)) vanishes at θ=0 AND at θ=π (`02_smooth_gluing_strip_drift_force_density.md` Section 4; `06_pairing_staple_projection_coercivity(1).md` Section 5). What was missing was the observation that the vanishing can be arranged at every plaquette simultaneously, by a configuration that is one line long and exists on every even lattice. That step - from "there is a bad conjugacy class" to "there is a bad configuration, with extensive defect, at every volume and every beta" - is the whole content of items 1-3.

(4) The affine Laplacian identity Delta_Lambda z_p = 4 C_2 (1 - z_p) is the corpus's own "crown jewel" conjecture (`su2-drift-certificates.md` Section 3: "if this identity can be proven exactly, it upgrades the entire drift story"). It is proved in item 8 in three lines from isometry-covariance of the Laplacian, and it is what makes the strip-drift refutation *exact* rather than numerical: L B_avg(U*) = 12(1 - B_avg(U*)) with no estimation at all. The identity the corpus hoped would save the drift is the identity that makes the drift provably positive on the center stratum.

(5) Relation to the other obstructions catalogued in `_EXTRACT_FOR_LLM/04_papers/PAPER-1-curvature-no-go/ABSTRACT.md`: this is Theorem E there. It is logically independent of Theorem A (global Bakry-Emery CD constant diverges), Theorem B (gauge invariance forces exactly-Haar link marginals, so any small-field good set has exponentially small measure), Theorem C (scaling dichotomy), and Theorem D (plaquette entropy beats the logarithmic growth of beta). Notably Theorem B explains *why* item 4's violating neighbourhood necessarily has exponentially small Haar measure and why that is not a defence: the corpus's own good sets have exponentially small measure too, so "the witness is atypical" is not an argument that distinguishes it.

(6) It is also independent of the second half of CAND-009 (part (B): no exponential-of-extensive Lyapunov weight can have volume-uniform exponential moments). Part (B) attacks the conclusion; the center-flux witness attacks the hypothesis. The witness does NOT by itself refute the Foster-Lyapunov conclusion: at U* one computes exactly L_Lambda V_Lambda = 24 sum_p z_p(1-z_p) = -16|P| < 0 (for |S|=2), so the drift bound happens to hold there for sign reasons. This is stated plainly in item 5's caveat and is the main honest limitation of the extraction: what is refuted is the route, its stated hypothesis, and its numerical certificates - not, by this argument alone, the existence of some other Lyapunov function.

(7) Method transfer: the same construction refutes any proposed inequality of the form "plaquette-defect density bounded below implies Wilson force bounded below" for any compact gauge group with nontrivial center, in any dimension d >= 2, for any faithful representation used in the action. It also transfers to the Cartan-alignment program (`HESSIAN/Core_Hessian/04_Coercivity_via_Cartan_Alignment.md`), whose conjecture "rough and non-Cartan-aligned implies ||grad S|| >= c |Lambda|^{1/2}" is satisfied vacuously by the center configurations (they are maximally Cartan-aligned - they are central) but whose GPU counterexample hunts never found them, because those hunts sampled by gradient descent from random starts and the center stratum is a measure-zero set of exact critical points, invisible to a descent search and unreachable by the sigma-perturbed/Haar sampler in su2_drift_simulation.py.

## Further material found but not fully extracted

Real material in this area that I found and verified but did not extract in full:

1. **The smooth-barrier gluing lemma itself** (`LYAPUNOV/Gluing_Typicality/Doc3_Smooth_Gluing_Lemma_Barrier.md`) is a complete, correct, and genuinely reusable proof, independent of Yang-Mills: given a C^2 order parameter B on a weighted compact manifold, a smooth cutoff chi_delta = psi((B-eps)/delta), hypotheses (H1) restricted Poincare on K and K^c, (H2) LB <= -rho on the strip, and (H3) |grad B|, |LB| <= M_B on the strip, it derives the between-set mixing bound p q (mu_K f - mu_{K^c} f)^2 <= C_mix E(f) + C_Sigma int_Sigma (f - mu f)^2 dmu, with the key mid-strip barrier estimate -L chi_delta >= c_psi rho / (2 delta) obtained by choosing delta so that ||psi''||_inf M_B^2 / delta^2 <= c_psi rho / (2 delta). Full 4-step proof with all constants. Only (H2) fails for Wilson; the lemma is correct and would apply verbatim to any order parameter whose drift can be signed. Worth extracting separately as a positive result.

2. **The linear Maxwell/Hodge coercivity lemma** (`LYAPUNOV/Maxwell_Covariance/05_pairing_noncancellation_structured.md`, Section 5): for horizontal A (d_0* A = 0) with F = d_1 A, ||d_1* F||^2 = <F, d_1 d_1* F> >= lambda_min ||F_perp||^2, giving max_l ||grad_l S_W|| >~ alpha ||F|| / sqrt(|E|) in the linearised regime. This document also correctly demolishes the "sum of rotated su(2) vectors cannot vanish unless collinear" heuristic with the equilateral-triangle counterexample Y_1 + Y_2 + Y_3 = 0. Both are correct and independent of the center-flux obstruction (they live in the small-field regime where all plaquettes are near the identity).

3. **The block-decomposition proof architecture** for a would-be finite-range coercivity inequality (`06_pairing_staple_projection_coercivity(1).md` Section 6.1): local block inequality on a 2^D hypercube with a 1-link buffer, disjoint tiling, positive density of bad blocks outside the global core. This is a sensible plan and the center-flux witness tells you exactly where it fails - the witness makes every block equally bad and every block force-free, so no block inequality with a positive constant can hold.

4. **The disjoint-plaquette selection/orthogonality argument** (`02_smooth_gluing_strip_drift_force_density.md`, Prop. 6.1): greedily select link-disjoint plaquettes from a forceful set R; each choice kills at most m_partial * nu = 24 candidates, so |Q| >= |R|/24; link-disjoint plaquette gradients are orthogonal in the product metric, hence ||grad B_avg||^2 >= (alpha/nu) c_force^2 / |P|. Clean combinatorial device, correct, reusable whenever the order parameter is an average of local terms.

5. **su2_drift_simulation.py** (612 lines) is a well-engineered, correct harness worth preserving on its own terms: chunked over both configurations and MC directions, seeded, float64/float32 split for the tangent noise, real argparse CLI, metadata JSON written into the .npz, plus two analysis utilities (`beta_rescale_components`, which exploits that lap is beta-independent while gip scales linearly, and `ratio_certificate_uniform_in_L`, which tracks the worst-case configuration index per tau). Its limitation is structural: it has no sampler, only sigma-perturbed identity fields and Haar-random fields, so no equilibrium statement derived from it is supported - and, as this extraction shows, its configuration space never touches the center stratum.

6. **Referenced but absent artifacts.** The .npz that produced the certificates (`decomp_Lsweep_results.npz`) and the companion analysis scripts are not present anywhere in the corpus, so the published tables cannot be regenerated end-to-end from what is here. The certificate numbers in `su2_outside_core_certificates.md` (tau_0=0.3883) and in `01_su2_generator_laplacian_drift.md` App. B/C (tau*=0.2158) come from different runs and are not mutually consistent as a single certificate; both are refuted by the same witness.

7. **A loose end I did not chase.** `HESSIAN/Core_Hessian/01_physical_hessian_hinge.md` line 171-172 asserts that the physical-Hessian hinge lemma on the small-field core K_Lambda(r) "fits the center-flux obstruction cleanly" because the center-flux configuration lies far outside K_Lambda(r). That is true and I verified it (half the links are at geodesic distance pi from the identity), but the accompanying claim that this makes the hinge lemma "topology-aware" rather than a patch deserves separate scrutiny - it is exactly the move that trades a global statement for one on a set of exponentially small measure, which is the subject of the corpus's own Theorem B.
