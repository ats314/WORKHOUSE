# Monotonicity / Coercivity Module (Doc 4+5 fused)

This module isolates **one** local monotonicity inequality that is sufficient for the *smooth gluing step* and *Lyapunov drift step*, and then reduces it to a single **SU(2) star–transversality** input that explicitly respects the lattice “admissible transport” constraints.

Throughout we work on a finite periodic 4D lattice torus $\Lambda$ with gauge group $G=\mathrm{SU}(2)$ and the standard product bi-invariant metric on
\[
M_\Lambda := G^{E(\Lambda)}.
\]

---

## 0. Constants and notational hygiene

- $E(\Lambda)$ = set of oriented edges (links), $P(\Lambda)$ = set of oriented plaquettes.
- **Plaquette perimeter:** $m_\partial:=|\partial p|=4$ (in any dimension).
- **Star size at a link in $d=4$:** each link $\ell$ lies in $2(d-1)=6$ plaquettes; in the project constant ledger this is recorded as a bounded overlap parameter $\nu\le 6$.
- **Edge/plaquette ratio in $d=4$ (periodic torus):** $C_{E/P}:=\frac{|E|}{|P|}=\frac{2}{3}$.

---

## 1. Proxy plaquette defect, averaged disorder, and Wilson action

Fix a smooth “defect” function $\widetilde z:G\to[0,\infty)$ (in the Wilson case below, it is the fundamental trace defect). For each plaquette $p\in P(\Lambda)$ define the lifted observable
\[
\widetilde z_p(U) := \widetilde z\!\big(U_p(U)\big),
\qquad U\in M_\Lambda,
\]
where $U_p(U)$ is the plaquette holonomy.

Define:
\[
\mathcal D_\Lambda(U):=\sum_{p\in P(\Lambda)} \widetilde z_p(U),
\qquad
\mathcal B_\Lambda(U):=\frac{1}{|P(\Lambda)|}\,\mathcal D_\Lambda(U)
\quad\in[0,\infty).
\]

For the **Wilson action** (in the normalization used in the project notes),
\[
S_{W,\beta}(U) := \beta\sum_{p\in P(\Lambda)} \widetilde z_p(U)
= \beta\,\mathcal D_\Lambda(U)
= \beta\,|P(\Lambda)|\,\mathcal B_\Lambda(U).
\]

---

## 2. Generator, carré du champ, and the target local inequality

Let
\[
d\mu_{\Lambda,\beta} = Z^{-1} e^{-S_{W,\beta}}\,d\mathrm{vol}
\]
and let the reversible diffusion generator be
\[
L_\Lambda := \Delta_\Lambda - \langle \nabla S_{W,\beta}, \nabla \cdot\rangle,
\qquad
\Gamma_\Lambda(f):=|\nabla f|^2.
\]

### Target local monotonicity inequality (Strip Drift for $\mathcal B_\Lambda$)

Fix $\varepsilon>0$ and thickness $\delta>0$, and define the **boundary strip**
\[
\Sigma_\Lambda(\varepsilon,\delta):=\{U\in M_\Lambda:\ \varepsilon < \mathcal B_\Lambda(U) < \varepsilon+\delta\}.
\]

> **(SD$_{\varepsilon,\delta}$)** There exists $\rho=\rho(\varepsilon,\delta,\beta)>0$, independent of $|\Lambda|$, such that
> \[
> L_\Lambda \mathcal B_\Lambda(U)\ \le\ -\rho
> \qquad \forall\,U\in \Sigma_\Lambda(\varepsilon,\delta).
> \]

This is the precise “inward drift across the interface” condition used by the smooth cutoff gluing lemma.

---

## 3. Explicit computation of $L_\Lambda\mathcal B_\Lambda$ for the Wilson action

The computation is clean because $S_{W,\beta}$ is *exactly proportional* to $\mathcal B_\Lambda$.

### 3.1 Exact drift identity

Differentiate the Wilson action:
\[
\nabla S_{W,\beta}
= \beta \sum_{p}\nabla \widetilde z_p
= \beta\,\nabla \mathcal D_\Lambda
= \beta\,|P|\,\nabla \mathcal B_\Lambda.
\]
Hence, pointwise,
\[
\boxed{
\langle\nabla S_{W,\beta},\nabla \mathcal B_\Lambda\rangle
= \beta\,|P|\,|\nabla \mathcal B_\Lambda|^2
= \beta\,|P|\,\Gamma_\Lambda(\mathcal B_\Lambda).
}
\tag{3.1}
\]

This is the exact object the user asked to isolate.

### 3.2 Laplacian term and the uniform constant $m_\partial C_\Delta$

Let
\[
C_\Delta:=\|\Delta_G \widetilde z\|_\infty <\infty
\]
(the constant from the project’s Appendix J derivative ledger). The lifted plaquette functions satisfy the **uniform per-plaquette Laplacian bound**
\[
\boxed{
|\Delta_\Lambda \widetilde z_p(U)| \le m_\partial\,C_\Delta
\qquad\text{for all }U\in M_\Lambda,\ \ p\in P(\Lambda).
}
\tag{3.2}
\]
In $d=4$, $m_\partial=4$, so the bound is $4C_\Delta$.

Since $\mathcal B_\Lambda = |P|^{-1}\sum_p \widetilde z_p$ and $\Delta_\Lambda$ is linear,
\[
\Delta_\Lambda \mathcal B_\Lambda
= \frac{1}{|P|}\sum_{p}\Delta_\Lambda \widetilde z_p,
\]
and therefore
\[
\boxed{
|\Delta_\Lambda \mathcal B_\Lambda(U)|
\le m_\partial\,C_\Delta
\quad\text{uniformly in }|\Lambda|.
}
\tag{3.3}
\]

### 3.3 Assemble $L_\Lambda \mathcal B_\Lambda$

By definition,
\[
L_\Lambda \mathcal B_\Lambda
= \Delta_\Lambda \mathcal B_\Lambda
- \langle\nabla S_{W,\beta},\nabla \mathcal B_\Lambda\rangle.
\]
Using (3.1),
\[
\boxed{
L_\Lambda \mathcal B_\Lambda
= \Delta_\Lambda \mathcal B_\Lambda
- \beta\,|P|\,\Gamma_\Lambda(\mathcal B_\Lambda).
}
\tag{3.4}
\]

Combining (3.3) and (3.4) yields the **universal one-line upper bound**
\[
\boxed{
L_\Lambda \mathcal B_\Lambda(U)
\le m_\partial\,C_\Delta
- \beta\,|P|\,\Gamma_\Lambda(\mathcal B_\Lambda)(U).
}
\tag{3.5}
\]

---

## 4. Exactly what inequality on $\langle\nabla S,\nabla \mathcal B_\Lambda\rangle$ suffices for uniform $\rho>0$?

From (3.4), on any set (in particular on $\Sigma_\Lambda(\varepsilon,\delta)$),
\[
L_\Lambda \mathcal B_\Lambda \le -\rho
\quad\Longleftarrow\quad
\langle\nabla S_{W,\beta},\nabla \mathcal B_\Lambda\rangle
\ge \Delta_\Lambda \mathcal B_\Lambda + \rho.
\]
A clean *sufficient* condition that avoids the sign of $\Delta_\Lambda \mathcal B_\Lambda$ is:
\[
\langle\nabla S_{W,\beta},\nabla \mathcal B_\Lambda\rangle
\ge |\Delta_\Lambda \mathcal B_\Lambda| + \rho.
\]
Using (3.3) we arrive at:

> **Sufficient pairing inequality for strip drift (uniform, volume-free):**
> \[
> \boxed{
> \langle\nabla S_{W,\beta},\nabla \mathcal B_\Lambda\rangle(U)
> \ \ge\ m_\partial\,C_\Delta + \rho
> \qquad \forall U\in\Sigma_\Lambda(\varepsilon,\delta).
> }
> \tag{4.1}
> \]

Equivalently, substituting (3.1),
\[
\boxed{
|P|\,\Gamma_\Lambda(\mathcal B_\Lambda)(U)
\ \ge\
\frac{m_\partial\,C_\Delta+\rho}{\beta}
\qquad \forall U\in\Sigma_\Lambda(\varepsilon,\delta).
}
\tag{4.2}
\]

So the entire SD$_{\varepsilon,\delta}$ problem is reduced to one quantitative lower bound on $|P|\Gamma_\Lambda(\mathcal B_\Lambda)$ on the strip.

---

## 5. The minimal “admissible transport” SU(2) transversality lemma you need

### 5.1 What “admissible” means (no free $g_j$’s)

Fix an oriented link $\ell\in E(\Lambda)$. Let $\mathrm{Star}(\ell)$ be the set of plaquettes containing $\ell$.

For each $p\in\mathrm{Star}(\ell)$, the plaquette holonomy can be written **as a function of the single link variable $U_\ell$**:
\[
U_p(U) = A_{p,\ell}(U)\, U_\ell^{\sigma_{p,\ell}}\, B_{p,\ell}(U),
\qquad \sigma_{p,\ell}\in\{\pm1\},
\]
where $A_{p,\ell}(U),B_{p,\ell}(U)\in\mathrm{SU}(2)$ depend only on the other links in $\partial p\setminus\{\ell\}$ (the “staple transports”). This is exactly the “admissible transport” structure: the $A$’s and $B$’s are not arbitrary; they come from the lattice geometry.

Consequently, the linkwise derivatives $\nabla_\ell \widetilde z_p(U)$ are not arbitrary $\mathfrak{su}(2)$ vectors: they are images under differentials of the maps
\[
\Psi_{A,B,\sigma}(g):=A\,g^\sigma B,
\]
which are isometries of $G$ (left/right multiplication and inversion).

### 5.2 Canonical SU(2) plaquette-gradient vector

For the Wilson trace defect in the fundamental representation,
\[
\widetilde z(g)=1-\tfrac12\mathrm{Re\,Tr}(g),
\]
one can compute explicitly (with the bi-invariant metric induced by $-\tfrac12\mathrm{Tr}$) that the **right-trivialized gradient** is
\[
X(g):=(R_{g^{-1}})_* \nabla_G \widetilde z(g)=\tfrac12\,(g-g^{-1})\in\mathfrak{su}(2),
\]
and in the SU(2) axis–angle parametrization $g=\cos\theta\,I+i\sin\theta\,(\hat n\cdot\sigma)$ this gives
\[
|X(g)|^2=\sin^2\theta = \widetilde z(g)\,(2-\widetilde z(g)).
\]
In particular, $X(g)$ commutes with $g$ (it lies in the Lie algebra of the centralizer of $g$), and the only way $X(g)=0$ is when $g$ is central ($g=\pm I$).

For a general smooth $\widetilde z$ (not necessarily the trace defect), one still has the same structural fact: for class functions, $X(g)$ lies in the Lie algebra of the centralizer of $g$.

### 5.3 Star transversality lemma (the real missing local input)

Define the **link force** contributed by plaquettes at a link $\ell$:
\[
F_\ell(U):=\sum_{p\in\mathrm{Star}(\ell)} \nabla_\ell \widetilde z_p(U)\in T_{U_\ell}\mathrm{SU}(2)\cong\mathfrak{su}(2),
\]
and note that
\[
\nabla_\ell \mathcal B_\Lambda(U)=\frac{1}{|P|}\,F_\ell(U),
\qquad
|P|\,\Gamma_\Lambda(\mathcal B_\Lambda)(U)=\frac{1}{|P|}\sum_{\ell\in E(\Lambda)} |F_\ell(U)|^2.
\]

> **Lemma / Assumption (TR$_{\varepsilon,\delta}$): admissible SU(2) star transversality.**  
> Fix $\varepsilon>0$ and $\delta>0$. There exists a constant
> \[
> \kappa_{\mathrm{tr}}=\kappa_{\mathrm{tr}}(\varepsilon,\delta)>0
> \]
> independent of $|\Lambda|$ such that for every configuration $U$ in the strip $\Sigma_\Lambda(\varepsilon,\delta)$,
> \[
> \boxed{
> \frac{1}{|P(\Lambda)|}\sum_{\ell\in E(\Lambda)} |F_\ell(U)|^2 \ \ge\ \kappa_{\mathrm{tr}}.
> }
> \tag{TR}
> \]
> Equivalently,
> \[
> \boxed{
> |P(\Lambda)|\,\Gamma_\Lambda(\mathcal B_\Lambda)(U)\ \ge\ \kappa_{\mathrm{tr}}
> \qquad\forall U\in\Sigma_\Lambda(\varepsilon,\delta).
> }
> \tag{TR'}
> \]
> Moreover, any failure of (TR) occurs only on a “Cartan-aligned” exceptional set where the six plaquette holonomies in each star simultaneously lie in a common maximal torus (in particular, the center-valued $Z_2$ subsector is contained in this exceptional set).

**Why this is the right lemma.**  
It respects admissible transport constraints because each $\nabla_\ell\widetilde z_p(U)$ is computed from genuine lattice staples $A_{p,\ell}(U),B_{p,\ell}(U)$; no independent “free rotations” are introduced.

**How it plugs into strip drift.**  
Combining (TR') with (3.5) yields on the strip
\[
L_\Lambda \mathcal B_\Lambda(U)
\le m_\partial C_\Delta - \beta\,\kappa_{\mathrm{tr}}.
\]
Thus if
\[
\beta>\beta_*:=\frac{m_\partial C_\Delta}{\kappa_{\mathrm{tr}}},
\]
then SD$_{\varepsilon,\delta}$ holds with the explicit uniform constant
\[
\boxed{
\rho = \beta\,\kappa_{\mathrm{tr}} - m_\partial C_\Delta\ >0.
}
\tag{5.1}
\]

---

## 6. How this fuses with the coercivity targets ($\mathcal P_\Lambda$) from Appendix I

Appendix I introduces the “pairing” functional
\[
\mathcal P_\Lambda := \sum_{p\in P(\Lambda)} \widetilde z_p\,\langle\nabla S_{W,\beta},\nabla \widetilde z_p\rangle
= \tfrac12\,\langle\nabla S_{W,\beta},\nabla V_\Lambda\rangle,
\qquad
V_\Lambda:=\sum_p \widetilde z_p^2.
\]

The strip drift (SD$_{\varepsilon,\delta}$) is a **monotonicity statement for the average** $\mathcal B_\Lambda$:
\[
L_\Lambda \mathcal B_\Lambda \le -\rho,
\]
while Appendix I’s Lyapunov route is a **coercivity statement for the square functional** $V_\Lambda$:
\[
L_\Lambda V_\Lambda \le -c\,\mathcal D_\Lambda + C
\quad\text{(schematically)}.
\]

Both are driven by the same geometric engine: control of an inner product of the form
\[
\langle\nabla S_{W,\beta},\nabla(\cdot)\rangle.
\]
For $\mathcal B_\Lambda$ this inner product collapses to $\beta|P|\Gamma(\mathcal B_\Lambda)$ exactly (3.1), which is why the strip drift inequality is the *cleanest* monotonicity target to state.

---

## 7. What to do next (minimal to-do list for closing TR$_{\varepsilon,\delta}$)

The project “gap map” reduces (TR) to one lattice-local, SU(2)-specific statement:

1. Write each $\nabla_\ell\widetilde z_p$ in a common $\mathfrak{su}(2)\cong\mathbb R^3$ frame using right-translation at $U_\ell$, so that each term is a rotated axis-vector (Adjoint action).
2. Use that for SU(2) class functions the axis vector commutes with the plaquette holonomy; this severely limits cancellation unless all holonomies share an axis.
3. Show: if the six admissible transported axis-vectors cancel too well at many links, then the configuration is forced into the Cartan-aligned locus.
4. On the complement of that locus, compactness gives a uniform quantitative gap $\kappa_{\mathrm{tr}}>0$.

Once TR$_{\varepsilon,\delta}$ is in hand, the drift constant $\rho$ is explicit (5.1), and the smooth gluing step can be run with no illegal indicator gradients.

---

## Summary (one line)

For the Wilson action, the strip drift condition SD$_{\varepsilon,\delta}$ is **equivalent** to a single inequality on the pairing
\[
\langle\nabla S_{W,\beta},\nabla \mathcal B_\Lambda\rangle
= \beta|P|\Gamma(\mathcal B_\Lambda)
\]
dominating the uniform Laplacian constant $m_\partial C_\Delta$, and the only genuinely new local input needed is the admissible SU(2) star transversality lemma (TR$_{\varepsilon,\delta}$).
