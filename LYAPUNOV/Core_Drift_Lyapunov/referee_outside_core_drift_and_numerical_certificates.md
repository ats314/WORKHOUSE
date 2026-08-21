# Outside-core control: Cartan alignment, noncancellation, drift/Lyapunov certificates, and what numerics actually certify

## What this document establishes

It isolates the project’s proposed mechanism for controlling the **complement** of a convex “core” set:

- a *geometric classification* of when Wilson forces can cancel (Cartan alignment locus),
- a resulting *uniform force lower bound* away from that locus when at least one plaquette is rough,
- a Lyapunov/drift inequality for a global disorder functional \(V\),
- numerical “certificates” that these drift inequalities appear to hold uniformly across moderate lattice sizes,
- a separate numerical SAFE-region convexity certificate for \(SU(3)\).

This is the project’s main attempt to globalize fixed-cutoff core convexity. It is also where the gap between numerics and proof is largest.

---

## 0. The core/complement split and why complement control is needed

Let \(\mathcal K\subset\mathcal C_\Lambda\) be a “SAFE core” region where one has strong convexity / matrix-hinge control.

To obtain global spectral gap/clustering, one must control \(A:=\mathcal C_\Lambda\setminus\mathcal K\).
Project strategy: prove a **Dirichlet Poincaré inequality** on \(A\) (equivalently, a uniform lower bound on the first Dirichlet eigenvalue \(\lambda_A\)), typically via Foster–Lyapunov drift.

---

## 1. The noncancellation lemma template (FC-02) and its real content

### 1.1 Local noncancellation statement as used

Fix a link \(\ell\) and consider the local “star” neighborhood \(\mathcal U_\ell\) of plaquettes incident to \(\ell\).

Define:
- a roughness indicator \(\widetilde z(U_p)\) for plaquette \(p\),
- a rough local set \(\mathcal R_\ell(\varepsilon)\) requiring at least one incident plaquette with \(\widetilde z\ge\varepsilon\),
- an “alignment locus” \(\mathcal A_\ell\) on which plaquette-force contributions can cancel by lying in a common Cartan direction.

Then the lemma sought is:

> **(FC-02 local noncancellation).**  
> On \(\mathcal R_\ell(\varepsilon;\tau):=\{U\in\mathcal U_\ell:\text{ roughness }\ge\varepsilon,\ \mathrm{dist}(U,\mathcal A_\ell)\ge\tau\}\),
> \[
> |\nabla_\ell S_W(U)| \ \ge\ c_{\mathrm{loc}}(\varepsilon,\beta,\tau)\ >0.
> \]

### 1.2 What is proved vs what is assumed

The “proof” is compactness/continuity:

- \(U\mapsto \nabla_\ell S_W(U)\) is continuous on \(\mathcal U_\ell\);
- if it has no zeros on a compact set, then \(|\nabla_\ell S_W|\) attains a positive minimum there.

So FC-02 reduces to the missing classification claim:

> **Classification sub-claim (missing).**  
> The zero set of the local force \(U\mapsto \nabla_\ell S_W(U)\) within the rough set coincides with the Cartan alignment locus \(\mathcal A_\ell\).

Without this identification, FC-02 is not established as stated.

---

## 2. From local to global: strip combinatorics

A standard combinatorial amplification is proposed:

- if an averaged disorder \(\mathcal B_\Lambda\) lies in a strip \([\varepsilon,\varepsilon+\delta]\), then a positive fraction of plaquettes must be rough,
- each link meets at most \(\nu\) plaquettes,
- therefore a positive fraction of links satisfy the local roughness condition,
- summing the local force lower bounds yields a global lower bound on \(|\nabla \mathcal B_\Lambda|^2\), which is the input for a **uniform negative strip drift** \(L\mathcal B_\Lambda\le -\rho\).

**Status.** Combinatorics is standard. The missing ingredient is an explicit \(c_{\mathrm{loc}}(\varepsilon,\tau)\) with a proven exceptional set description.

---

## 3. Drift certificates for \(SU(2)\): what they actually certify

The project uses a disorder/Lyapunov function of the form
\[
V(U)=12 - 12\,B_{\mathrm{avg}}(U),
\]
where \(B_{\mathrm{avg}}\) is the average plaquette observable (project conventions).

### 3.1 Near-identity Laplacian law (suggested identity)

Numerical tests report a near-identity:
\[
\Delta V \approx 12 - 12\,B_{\mathrm{avg}},
\]
with residuals decreasing in \(L\). This is proposed as a candidate for an exact identity tied to \(SU(2)\) geometry and the particular \(V\).  

**Referee ruling:** until proved, it is only an empirical observation.

### 3.2 “Sign test”: nonnegativity of the pairing term

For tested samples,
\[
\langle \nabla S,\nabla V\rangle \ge 0
\]
appears to hold, which would make \(LV=\Delta V-\langle\nabla S,\nabla V\rangle\) easier to sign-control.

**Referee ruling:** again empirical unless proved analytically.

### 3.3 A global affine ceiling (too weak to globalize)

A fitted global bound of the form
\[
LV \le -\lambda V + b
\]
is reported with \(\lambda=0\) and \(b\approx 12.0183\) (no holdout violations at a \(5\sigma\) margin in the logged run).

**Referee ruling:** this is a ceiling, not a Foster–Lyapunov “return to core” inequality.

### 3.4 The proof-shaped object: ratio certificates on a tail domain

Define tail-domain “ratio certificates” (with an \(n\sigma\) safety margin on holdout data):
\[
c_{\mathrm{gip}}(\tau)
=\inf_{B_{\mathrm{avg}}\ge\tau}\frac{\texttt{gip}-n\sigma\,\texttt{gip\_se}}{B_{\mathrm{avg}}},
\qquad
d_{LV}(\tau)
=\sup_{B_{\mathrm{avg}}\ge\tau}\frac{\texttt{LV}+n\sigma\,\texttt{LV\_se}}{B_{\mathrm{avg}}}.
\]

For \(\tau_0=0.3883\), the file reports numerical certification of
\[
\texttt{gip}\ge c_{\min}(\tau_0)\,B_{\mathrm{avg}},
\qquad
\texttt{LV}\le d_{\max}(\tau_0)\,B_{\mathrm{avg}},
\]
with
\[
c_{\min}(\tau_0)=20.9510,
\qquad
d_{\max}(\tau_0)=-2.6909.
\]

This is the right *shape*: negative drift proportional to \(B_{\mathrm{avg}}\) on a tail set.

**Referee ruling:** this is still not a proof; it is a numerical certificate on sampled configurations plus a statistical margin.

---

## 4. SAFE-region convexity for \(SU(3)\): what it certifies

A separate numerical module provides a small-field convexity budget for \(SU(3)\):

- baseline “Haar curvature” \(\kappa_*\approx 0.25\),
- Wilson perturbation budget \(\delta\approx 0.006\),
- hence a target lower bound \(\kappa_*-\delta\approx 0.244\) for the physical-sector Hessian on a specified SAFE region.

The file states an intended certified inequality of the form
\[
\nabla^2 S_{\rm tot}(U)\big|_{\rm phys} \succeq (\kappa_*-\delta)\,I
\quad\text{on }\Omega_{\rm SAFE}(R_0),
\]
and reports scan minima \(\approx 0.248\), leaving margin over \(0.244\).

**Referee ruling:** this is numerically supported and structurally plausible, but it is not a proof without certified (not sampled) bounds on the relevant third-derivative/Lipschitz constants.

---

## 5. What would convert this module into mathematics

To turn the outside-core program into a usable proof component:

1. **Exact force cancellation classification** (or a rigorously enlarged exceptional set with explicit capacity bounds).
2. **Quantitative separation**: explicit \(c_{\mathrm{loc}}(\varepsilon,\tau)\), not just existence.
3. **Exact \(\Delta V\) computation** (if relied upon).
4. **Lyapunov-to-Dirichlet**: a fully written argument that the drift inequality implies a uniform lower bound on \(\lambda_A\) with explicit constants.

Until (1)–(3) are completed, the outside-core module remains conjectural, with some statistically-motivated evidence.

---

## Internal sources in this project

Primary modules:
- `1_local_cancellation_su2.md`, `CURATED_05_CartanAlignment_NonCancellation(1).md`
- `su2_outside_core_certificates.md`, `su2-drift-certificates.md`, `su2_a100_stress_test.py`
- `SAFE_region_SU3_curvature.md`, `YANG3_03_SU3_Wilson_Haar_convexity_numerics.md`
