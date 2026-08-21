# GAP-FC-02: Cartan alignment and non-cancellation of Wilson forces (SU(2) focus)

## Problem statement

Let \(G=\mathrm{SU}(2)\) and \(\Lambda\subset\mathbb Z^4\) be a finite periodic lattice.
For the Wilson action
\[
S_\Lambda(U)=\beta\sum_{p\in P(\Lambda)}\vartheta(U_p(U)),
\qquad
\vartheta(g)=1-\tfrac12\Re\operatorname{Tr}(g),
\]
define the disorder functional
\[
\mathcal B_\Lambda(U)=\frac{1}{|P(\Lambda)|}\sum_{p\in P(\Lambda)}\vartheta(U_p(U)).
\]

**GAP-FC-02** asks for a *uniform* quantitative statement of the form:

> There exist \(\varepsilon,c_0>0\) independent of \(|\Lambda|\) such that
> \[
> \mathcal B_\Lambda(U)\ge \varepsilon
> \quad\Longrightarrow\quad
> \|\nabla S_\Lambda(U)\|\ge c_0.
> \tag{FC-02}
> \]

Equivalently (and more locally), at a single link \(\ell\),
\[
\nabla_\ell S_\Lambda(U) \neq 0
\]
whenever the incident plaquette data are sufficiently rough, *unless* the configuration lies in an explicitly defined exceptional “Cartan-aligned” set.

This note extracts the clean geometry behind the claim and formulates a precise target lemma. It also sketches a plausible analytic route (via real-analytic stratification and transversality) to make the lower bound quantitative.

---

## 1. Local force decomposition at a link

Fix an oriented link \(\ell=(x,\mu)\).
Let \(\mathcal P(\ell)\) be the plaquettes containing \(\ell\). In \(d=4\), \(|\mathcal P(\ell)|=6\).

Write each plaquette holonomy as
\[
U_p(U)=U_\ell\,W_p(U),
\]
where \(W_p(U)\in \mathrm{SU}(2)\) is the “staple” product of the other three links around \(p\) (with orientation consistent with \(\ell\)).

A standard variation computation gives
\[
\nabla_\ell S_\Lambda(U)
=
\beta\sum_{p\in\mathcal P(\ell)} \nabla_\ell\vartheta\!\bigl(U_\ell W_p(U)\bigr).
\tag{1.1}
\]

For \(G=\mathrm{SU}(2)\), \(\vartheta(g)=1-\frac12\Re\operatorname{Tr}(g)\) is a class function, and \(\nabla\vartheta(g)\) is tangent to the conjugacy class of \(g\).
Identifying \(\mathfrak{su}(2)\cong\mathbb R^3\) via the standard basis, the adjoint action is \(\mathrm{Ad}:\mathrm{SU}(2)\to \mathrm{SO}(3)\).

Thus each term in (1.1) can be written as a rotated “plaquette field”
\[
\nabla_\ell\vartheta\!\bigl(U_\ell W_p(U)\bigr)
=
\mathrm{Ad}_{G_p(U)}\,X_p(U),
\tag{1.2}
\]
for some \(G_p(U)\in \mathrm{SU}(2)\) and some vector \(X_p(U)\in\mathfrak{su}(2)\cong\mathbb R^3\).
Crucially:

- \(\|X_p(U)\|\) is controlled by the conjugacy angle of the plaquette holonomy \(U_p(U)\),
- the \(\mathrm{Ad}_{G_p(U)}\) are not arbitrary rotations; they come from the surrounding link transport geometry.

Equation (1.1) is therefore a **finite sum of rotated vectors in \(\mathbb R^3\)**.

---

## 2. A quantitative “rough plaquette ⇒ large local vector” bound

Write the conjugacy class parameterization \(g=\exp(\theta\,\hat n\cdot i\sigma)\) with \(\theta\in[0,\pi]\).
Then
\[
\vartheta(g)=1-\cos\theta,
\qquad
\|\nabla\vartheta(g)\|\asymp \sin\theta,
\tag{2.1}
\]
with constants depending only on the metric normalization.

In particular, if \(\vartheta(g)\ge \varepsilon\) and \(\varepsilon\) is bounded away from 0 and 2, then \(\sin\theta\) is bounded below, hence so is \(\|\nabla\vartheta(g)\|\).

A useful local quantitative statement is:

> If \(U_p(U)\) lies outside a small neighborhood of the center \(\{\pm I\}\), then the corresponding force contribution has magnitude bounded below.

This is one ingredient needed to prevent “rough but flat” directions.

---

## 3. What cancellation means: the Cartan-aligned exceptional set

Because \(\mathfrak{su}(2)\cong\mathbb R^3\), cancellation of the local force at \(\ell\) is the condition
\[
\sum_{p\in\mathcal P(\ell)} \mathrm{Ad}_{G_p(U)}\,X_p(U)=0.
\tag{3.1}
\]

A configuration is **Cartan-aligned at \(\ell\)** if all incident plaquette holonomies \(U_p(U)\) commute (equivalently, they lie in a common maximal torus).
In \(\mathrm{SU}(2)\), this means:

- there exists an axis \(\hat n\in S^2\) such that every \(U_p(U)\) is a rotation around \(\hat n\),
- equivalently, all the corresponding \(\mathfrak{su}(2)\) vectors \(X_p(U)\) are collinear.

This commuting locus is the natural candidate exceptional set: on it, one can engineer large plaquette angles while local force cancels via algebraic symmetries.

### Target definition (local exceptional set)

For fixed \(\varepsilon>0\), define the “rough-at-\(\ell\)” set
\[
\mathcal R_\ell(\varepsilon)
:=
\Bigl\{U:\ \max_{p\in\mathcal P(\ell)}\vartheta(U_p(U))\ge \varepsilon\Bigr\}.
\]
Define the Cartan-aligned set
\[
\mathcal A_\ell
:=
\Bigl\{U:\ [U_p(U),U_{p'}(U)]=e\ \text{for all }p,p'\in\mathcal P(\ell)\Bigr\}.
\]

---

## 4. Desired local quantitative lemma

A clean local statement that would close GAP-FC-02 (modulo standard patching arguments) is:

### Lemma (local non-cancellation outside Cartan alignment)

For each \(\varepsilon\in(0,2)\) there exist constants \(c(\varepsilon)>0\) and \(\delta(\varepsilon)>0\) such that for every lattice \(\Lambda\) and every link \(\ell\),
\[
U\in \mathcal R_\ell(\varepsilon)\ \cap\ \mathcal A_\ell^{\,c}
\quad\Longrightarrow\quad
\|\nabla_\ell S_\Lambda(U)\|\ge c(\varepsilon).
\tag{4.1}
\]
Moreover, \(c(\varepsilon)\) is independent of \(|\Lambda|\).

Given (4.1), a global bound of the form (FC-02) follows by a compactness/finite-overlap argument:
if \(\mathcal B_\Lambda\ge\varepsilon\), then a positive fraction of links are in \(\mathcal R_\ell(\varepsilon')\) for some \(\varepsilon'\asymp \varepsilon\), hence at least one link has a force lower bound.

---

## 5. Why the lemma is plausible in \(d=4\)

At a link in \(d=4\), plaquettes come in three orthogonal planes \((\mu,\nu)\) with \(\nu\neq \mu\), two orientations per plane.
Heuristically:

- within each plane, the two plaquettes share much of the same transport data,
- across distinct planes, the transport data are transverse / overdetermined,
- simultaneous cancellation across three planes forces a strong alignment constraint.

In other words: “local roughness” supplies vectors of nontrivial magnitude, and “global cancellation” demands that these vectors conspire to sum to zero in \(\mathbb R^3\).
Outside a commuting locus, this conspiracy should be unstable.

---

## 6. A plausible analytic route to quantitative bounds

The maps
\[
U\ \mapsto\ \nabla_\ell S_\Lambda(U)\in \mathfrak{su}(2)
\]
and
\[
U\ \mapsto\ \{U_p(U):p\in\mathcal P(\ell)\}
\]
are **real-analytic** on the compact manifold \(G^{E(\Lambda)}\).
This opens several robust tools:

1. **Stratify the zero set.**  
   Let \(Z_\ell:=\{U:\nabla_\ell S_\Lambda(U)=0\}\). As the zero set of analytic functions, \(Z_\ell\) admits a finite analytic stratification.

2. **Identify the relevant stratum.**  
   Show that on \(\mathcal R_\ell(\varepsilon)\), the only strata that can persist are contained in \(\mathcal A_\ell\) (commuting/Cartan-aligned locus).

3. **Łojasiewicz-type inequality.**  
   For analytic maps on compact sets, one has inequalities of the form
   \[
   \|\nabla_\ell S_\Lambda(U)\|
   \ \gtrsim\
   \operatorname{dist}(U,Z_\ell)^{k}
   \]
   for some finite exponent \(k\). If \(\mathcal R_\ell(\varepsilon)\cap Z_\ell\subset \mathcal A_\ell\), then on \(\mathcal R_\ell(\varepsilon)\cap \mathcal A_\ell^{c}\) the distance to \(Z_\ell\) is bounded below, giving (4.1).

4. **Uniformity in volume.**  
   Since \(\nabla_\ell S_\Lambda\) depends only on a bounded neighborhood of \(\ell\), all constants can be made independent of \(|\Lambda|\) once the statement is proved on the corresponding finite local configuration space.

This route is attractive because it converts “force cancellation” into a **finite-dimensional analytic geometry problem**.

---

## 7. What would count as a full closure of GAP-FC-02

To mark GAP-FC-02 as closed, the project needs:

1. a **rigorous definition** of \(\mathcal A_\ell\) in the actual lattice transport geometry (not an abstract “independent rotations” model),
2. a proof that on \(\mathcal R_\ell(\varepsilon)\cap\mathcal A_\ell^c\), the map \(U\mapsto \nabla_\ell S_\Lambda(U)\) is bounded away from 0 by a uniform constant \(c(\varepsilon)\),
3. a clean statement of **uniformity** in \(|\Lambda|\) (locality implies this should be possible).

---

## 8. Why this gap is high-upside

If (FC-02) (or a workable local form) is proved, it unlocks:

- Lyapunov drift \(\Rightarrow\) global Poincaré/LSI with volume-uniform constants,
- concentration/typicality of small-field sets \(K\),
- removal of localization conditioning in exponential clustering,
- and, via OS machinery, a fixed-cutoff mass gap lower bound with a plausible route to RG iteration.

It is an unusually crisp finite-dimensional geometric problem sitting at the heart of a deep quantum field theory question—exactly the sort of place where a “new trick” can pay off.
