# Smooth Gluing via Strip Drift, and the SU(2) Center Obstruction

## Abstract
This note extracts (and repairs) the most “hole-filling” part of the project: a **between-set / cross-term control** lemma (“gluing lemma”) based on a **smooth barrier** built from an order parameter, together with the **exact Wilson drift identity** for the averaged plaquette disorder.

The key mathematical obstruction is structural and specific: for SU(2) with the Wilson plaquette potential $b(g)=1-\tfrac12\Re\mathrm{Tr}(g)=1-\cos\theta$, the force $|\nabla b|\propto|\sin\theta|$ vanishes both at the vacuum class ($\theta=0$) **and** at the nontrivial center class ($\theta=\pi$).  Therefore, “large plaquette energy implies large force” is false without an additional exclusion.

The main deliverable here is a **referee-checkable sufficient condition** (a *force-density / center-avoidance* hypothesis) that implies a **uniform negative drift on the boundary strip**, exactly what the smooth gluing lemma needs.

---

## 1. Order parameter and the gluing target
Let $\Lambda$ be a finite periodic lattice and $M_\Lambda=G^{E(\Lambda)}$ with $G=\mathrm{SU}(2)$.  Let $\mu$ be the Wilson Gibbs measure.

Let $\mathcal B_\Lambda: M_\Lambda\to[0,2]$ be the averaged plaquette trace defect
\[
\mathcal B_\Lambda(U):=\frac{1}{|P(\Lambda)|}\sum_{p\in P(\Lambda)}\Bigl(1-\tfrac12\Re\mathrm{Tr}(U_p)\Bigr).
\]
Fix thresholds $\varepsilon<\varepsilon+\delta$ and define
\[
K:=\{\mathcal B_\Lambda\le\varepsilon\},\qquad
K^c:=\{\mathcal B_\Lambda\ge\varepsilon+\delta\},\qquad
\Sigma:=\{\varepsilon<\mathcal B_\Lambda<\varepsilon+\delta\}.
\]

A global Poincaré inequality via two-set decomposition requires control of the cross term
\[
\mu(K)\mu(K^c)\,\bigl(\mu_K f-\mu_{K^c} f\bigr)^2
\]
by the Dirichlet energy $\mathcal E(f)=\int|\nabla f|^2\,\mathrm d\mu$.

---

## 2. Smooth between-set control from a strip drift
We work with the reversible generator
\[
L:=\Delta-\langle \nabla S,\nabla\cdot\rangle,
\]
so that $\mathcal E(f,g)=\int\langle\nabla f,\nabla g\rangle\,\mathrm d\mu=-\int f\,Lg\,\mathrm d\mu$ on smooth functions.

### Lemma 2.1 (Smooth barrier gluing, schematic form)
Let $\chi: M_\Lambda\to[0,1]$ be a smooth cutoff with $\chi\equiv 1$ on $K$, $\chi\equiv 0$ on $K^c$, and $\mathrm{supp}(\nabla\chi)\subset\Sigma$.  Assume there exists $c_*>0$ such that
\[
- L\chi\ \ge\ c_*\quad \text{pointwise on }\Sigma.
\]
Then for all smooth $f$,
\[
\mu(K)\mu(K^c)\,\bigl(\mu_K f-\mu_{K^c} f\bigr)^2
\ \lesssim\ \frac{1}{c_*}\,\mathcal E(f)\ +\ \text{(strip variance term)}.
\]

*Proof idea.*  Integrate by parts against $\chi$ (or $1-\chi$), combine Cauchy–Schwarz with the pointwise barrier bound $-L\chi\ge c_*$, and isolate the difference of conditional means through the identity
\(\int f\chi\,\mathrm d\mu\approx \mu(K)\mu_K f\).
The strip variance term comes from replacing sharp indicators by $\chi$ and bounding the resulting approximation error by $\int_\Sigma(f-\mu f)^2\,\mathrm d\mu$.

**Remark.** In practice one chooses a one-dimensional profile $\chi=\psi\bigl((\mathcal B_\Lambda-\varepsilon)/\delta\bigr)$, so that $-L\chi$ is controlled by $-L\mathcal B_\Lambda$ and $|\nabla\mathcal B_\Lambda|^2$ on $\Sigma$.

---

## 3. Exact Wilson drift identity for the averaged badness
This is the “free algebra” part: for Wilson, $S$ is literally proportional to $\mathcal B_\Lambda$.

### Lemma 3.1 (Exact drift identity)
Let
\[
S_W(U)=\beta\sum_{p\in P(\Lambda)}\Bigl(1-\tfrac12\Re\mathrm{Tr}(U_p)\Bigr)=\beta|P(\Lambda)|\,\mathcal B_\Lambda(U).
\]
Then
\[
\nabla S_W=\beta|P|\,\nabla\mathcal B_\Lambda,\qquad
L\mathcal B_\Lambda=\Delta\mathcal B_\Lambda-\beta|P|\,|\nabla\mathcal B_\Lambda|^2.
\]

*Proof.* Differentiate $S_W=\beta|P|\,\mathcal B_\Lambda$.

### Lemma 3.2 (Uniform Laplacian bound)
Let $C_\Delta:=\sup_{g\in G}|\Delta_G(1-\tfrac12\Re\mathrm{Tr}(g))|<\infty$.  Then
\[
\bigl|\Delta\mathcal B_\Lambda(U)\bigr|\le 4C_\Delta\qquad\forall U\in M_\Lambda,
\]
uniformly in the lattice volume.

*Reason.* Each plaquette depends on 4 link variables; the product Laplacian hits each link term at most once per plaquette, yielding a bounded-overlap factor $4$.

**What’s left to get a strip drift:** a lower bound on $|\nabla\mathcal B_\Lambda|^2$ on $\Sigma$.

---

## 4. The SU(2) center obstruction
For SU(2) every conjugacy class is represented by
\[
g(\theta,\hat n)=\exp\bigl(i\theta\,\hat n\cdot\sigma\bigr),\qquad \theta\in[0,\pi].
\]
For the Wilson trace defect
\[
 b(g)=1-\tfrac12\Re\mathrm{Tr}(g)=1-\cos\theta,
\]
one has
\[
|\nabla b(g)|\ \propto\ |\sin\theta|\ =\ \sqrt{b(g)\,(2-b(g))}.
\]
Hence $|\nabla b|=0$ at both $\theta=0$ (vacuum) **and** $\theta=\pi$ (the nontrivial center element $-\mathbf 1$).  Therefore:

> There is no constant $c(\varepsilon)>0$ such that $b(g)\ge\varepsilon\implies |\nabla b(g)|\ge c(\varepsilon)$ on SU(2).

This is exactly why a naive attempt to deduce a strip lower bound on $|\nabla\mathcal B_\Lambda|$ from the condition $\mathcal B_\Lambda\in(\varepsilon,\varepsilon+\delta)$ fails: the strip can be populated by configurations where a positive density of plaquettes lie very near $-\mathbf 1$ (large defect but tiny derivative).

---

## 5. A referee-grade sufficient condition: force density / center avoidance
The fix is to assume (or prove probabilistically) that on the strip, *enough plaquettes are away from the two endpoint critical classes*.

### Definition 5.1 (Forceful plaquettes)
Write each plaquette as $U_p=\exp(i\theta_p\hat n_p\cdot\sigma)$.  Fix parameters
\[
\theta_{\min}\in(0,\pi/2],\qquad \kappa\in(0,\pi/2].
\]
Define the set of forceful plaquettes
\[
\mathcal R_{\theta_{\min},\kappa}(U):=
\bigl\{p\in P(\Lambda):\ \theta_p(U)\in[\theta_{\min},\pi-\kappa]\bigr\}.
\]
On this band, $|\sin\theta_p|\ge c(\theta_{\min},\kappa):=\min\{\sin\theta_{\min},\sin\kappa\}$.

### Hypothesis 5.2 (Force-density on the strip)
There exist constants $\alpha\in(0,1]$ and $c_{\mathrm{force}}>0$ such that for every $U\in\Sigma$,
\[
\bigl|\mathcal R_{\theta_{\min},\kappa}(U)\bigr|\ge \alpha|P(\Lambda)|
\qquad\text{and}\qquad
\bigl|\nabla_G b(U_p)\bigr|\ge c_{\mathrm{force}}\ \ \forall p\in\mathcal R_{\theta_{\min},\kappa}(U).
\]
(For Wilson, $c_{\mathrm{force}}\asymp c(\theta_{\min},\kappa)$.)

This hypothesis is *exactly* the statement that the strip is not dominated by plaquettes near $\theta\approx 0$ or $\theta\approx\pi$.

---

## 6. From force density to a strip gradient lower bound
Let $\nu$ be the bounded overlap constant: each link belongs to the boundary of at most $\nu$ plaquettes (in $d=4$, $\nu=2(d-1)=6$), and let $m_\partial=4$ be the number of links in a plaquette.

### Proposition 6.1 (Disjoint-plaquette selection and orthogonality)
Assume Hypothesis 5.2.  Then for all $U\in\Sigma$,
\[
|\nabla\mathcal B_\Lambda(U)|^2\ \ge\ \frac{\alpha}{\nu}\,\frac{c_{\mathrm{force}}^2}{|P(\Lambda)|}.
\]

*Proof sketch (finite, combinatorial).*  Start with the forceful set $\mathcal R$.  Greedily select a subfamily $\mathcal Q\subset\mathcal R$ such that the plaquette boundaries $\{\partial p\}_{p\in\mathcal Q}$ are **link-disjoint**.  Since each chosen plaquette contains $m_\partial$ links and each link belongs to at most $\nu$ plaquettes, picking one plaquette “kills” at most $m_\partial\nu$ candidates.  Therefore
\[
|\mathcal Q|\ge \frac{|\mathcal R|}{m_\partial\nu}\ge \frac{\alpha|P|}{4\nu}.
\]
Now observe that for link-disjoint plaquettes, the gradients $\nabla b(U_p)$ live on disjoint coordinate sets and are orthogonal in the product metric.  Hence
\[
\Bigl|\sum_{p\in\mathcal Q}\nabla b(U_p)\Bigr|^2\ =\ \sum_{p\in\mathcal Q}|\nabla b(U_p)|^2.
\]
Using $\nabla\mathcal B_\Lambda=\frac{1}{|P|}\sum_p\nabla b(U_p)$ and discarding nonnegative terms,
\[
|\nabla\mathcal B_\Lambda|^2
\ge \frac{1}{|P|^2}\sum_{p\in\mathcal Q}|\nabla b(U_p)|^2
\ge \frac{1}{|P|^2}|\mathcal Q|\,c_{\mathrm{force}}^2
\ge \frac{\alpha}{\nu}\,\frac{c_{\mathrm{force}}^2}{|P|},
\]
where constants were simplified (absorbing fixed $m_\partial=4$).

---

## 7. Uniform negative drift on the strip
Combine Lemmas 3.1–3.2 with Proposition 6.1.

### Corollary 7.1 (Strip drift bound)
Assume Hypothesis 5.2.  Then on $\Sigma$,
\[
L\mathcal B_\Lambda(U)
\le 4C_\Delta-\beta|P|\,|\nabla\mathcal B_\Lambda(U)|^2
\le 4C_\Delta-\beta\,\frac{\alpha}{\nu}c_{\mathrm{force}}^2.
\]
In particular, if
\[
\beta>\beta_*:=\frac{4\nu C_\Delta}{\alpha c_{\mathrm{force}}^2},
\]
then there exists $\rho>0$ (independent of volume) such that
\[
L\mathcal B_\Lambda\le -\rho\qquad\text{pointwise on }\Sigma.
\]

Thus, the smooth barrier gluing lemma applies with constants that do **not** depend on $|\Lambda|$.

---

## 8. The “exceptional strip” variant (probabilistic quarantine)
Hypothesis 5.2 can be used either deterministically (by defining $\Sigma$ to include it) or probabilistically:

* Define $\Sigma^{\mathrm{fd}}$ to be the force-dense part of $\Sigma$ satisfying Hypothesis 5.2.
* Define the exceptional remainder $\Sigma^{\mathrm{exc}}:=\Sigma\setminus\Sigma^{\mathrm{fd}}$.

Then:

1. On $\Sigma^{\mathrm{fd}}$ you have pointwise drift $L\mathcal B_\Lambda\le-\rho$.
2. On $\Sigma^{\mathrm{exc}}$ you do not claim drift; instead you absorb its contribution into the strip variance/error term already present in Lemma 2.1.

This reduces the “hard” work to proving that $\mu(\Sigma^{\mathrm{exc}})$ is small enough (or has small capacity) to not spoil the global functional inequality.

---

## 9. Why this is potentially reusable beyond Yang–Mills
The barrier-gluing pattern
\[
\text{(drift along an order parameter)}\ +\ \text{(strip cutoff)}\ \Rightarrow\ \text{(between-well mixing control)}
\]
is a general technique.  The force-density condition is one concrete way to certify drift when your potential has endpoint critical classes (cosine-like class functions are *exactly* like this).  Similar obstructions occur in:

* multimodal Gibbs measures (metastability),
* compact spin systems with periodic potentials,
* constrained manifolds where order parameters have singular/critical conjugacy classes.

The “disjoint plaquette” orthogonality argument is a handy combinatorial device whenever the order parameter is an average of local terms.

