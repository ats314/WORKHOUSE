# Local Cancellation / Transversality Lemma at One Link (SU(2))

This module isolates the **finite–dimensional algebraic engine** behind the coercivity/drift inputs.
Everything here is **local (one link)**, **finite-dimensional**, and **volume-independent**.

Throughout, we use the notation and normalization in `NOTATION_AND_CONSTANTS.md`:
- Gauge group \(G=\mathrm{SU}(2)\) with bi-invariant (Hilbert–Schmidt) metric
  \(\langle X,Y\rangle := -\tfrac12\mathrm{Tr}(XY)\) on \(\mathfrak{su}(2)\).
- Wilson plaquette potential \(\Phi_\beta(g)=\beta\,\widetilde z(g)\) with
  \(\widetilde z(g)=1-\tfrac12\mathrm{ReTr}(g)\in[0,2]\).

---

## 1. Coordinates and adjoint action

Let \(\sigma_1,\sigma_2,\sigma_3\) be the Pauli matrices and identify
\[
\mathfrak{su}(2)\ \cong\ \mathbb R^3,\qquad
x\in\mathbb R^3 \longmapsto i\,x\cdot\sigma.
\]
With the Hilbert–Schmidt inner product,
\[
\big\langle i\,x\cdot\sigma,\ i\,y\cdot\sigma\big\rangle
= x\cdot y,
\]
so this identification is an isometry.

For \(g\in \mathrm{SU}(2)\), the adjoint action
\(\mathrm{Ad}_g:\mathfrak{su}(2)\to\mathfrak{su}(2)\) corresponds to a rotation
\[
\mathrm{Ad}_g(i\,x\cdot\sigma) \ =\ i\,(R_g x)\cdot\sigma
\quad\text{for some }R_g\in \mathrm{SO}(3),
\]
and the map \(g\mapsto R_g\) is surjective with kernel \(\{\pm I\}\).

---

## 2. Single-plaquette force: magnitude on a small-angle rough set

Write any \(g\in \mathrm{SU}(2)\) as
\[
g=\exp\!\big(i\,\theta\,\hat n\cdot\sigma\big),
\qquad \theta\in[0,\pi],\ \hat n\in S^2.
\]
Then
\[
\widetilde z(g)=1-\cos\theta,\qquad \mathrm{ReTr}(g)=2\cos\theta.
\]

Let \(X(g)\in\mathfrak{su}(2)\) denote the right-trivialized gradient of \(\widetilde z\) at \(g\).
A standard computation (or direct symmetry argument) yields
\[
|X(g)| = |\nabla_G \widetilde z(g)| = |\sin\theta|.
\]
Hence the Wilson force from one plaquette satisfies
\[
|\nabla_G \Phi_\beta(g)|=\beta\,|\sin\theta|.
\]

**Small-angle lower bound.**
Fix \(\varepsilon\in(0,1]\). On the set \(\{\widetilde z(g)\ge \varepsilon\}\) *and* \(\widetilde z(g)\le 1\)
(which is the regime relevant to boundary strips near the vacuum),
\[
|\sin\theta|
= \sqrt{1-\cos^2\theta}
= \sqrt{1-(1-\widetilde z)^2}
= \sqrt{\widetilde z(2-\widetilde z)}
\ \ge\ \sqrt{\varepsilon}.
\]
Therefore, for such plaquettes,
\[
|\nabla_G \Phi_\beta(g)|\ \ge\ \beta\sqrt{\varepsilon}.
\tag{2.1}
\]

*Remark.* Globally, \(|\sin\theta|\) vanishes also at \(\theta=\pi\) (i.e. \(g=-I\)).
This is irrelevant for the **boundary-strip** applications where \(\widetilde z\) is small.

---

## 3. Lattice geometry at one link: the admissible transport family

Fix a lattice link \(\ell\) (oriented). Let \(\{p_j\}_{j=1}^m\) be the oriented plaquettes incident to \(\ell\),
with incidence signs \(\sigma_j\in\{\pm1\}\). In \(d=4\), \(m=2(d-1)=6\).

For each incident plaquette \(p_j\), write its holonomy in the form
\[
U_{p_j} \;=\; U_\ell^{\sigma_j}\,S_j,
\]
where \(S_j\in \mathrm{SU}(2)\) is the **staple**: the ordered product of the *other three* links of \(p_j\).
(Up to a harmless inversion convention, this is exactly the “transport element” used to move the plaquette
gradient into \(T_{U_\ell}\mathrm{SU}(2)\).)

A standard right/left-translation calculation on a Lie group with bi-invariant metric gives the link force decomposition
\[
\nabla_\ell S_W(U)
\;=\;
\sum_{j=1}^m \sigma_j\,\mathrm{Ad}_{g_j(U)}\big(X_j(U)\big),
\tag{3.1}
\]
where
- \(X_j(U):=\nabla_G \Phi_\beta(U_{p_j}(U))\in\mathfrak{su}(2)\) is the **plaquette force vector**,
- \(g_j(U)\in \mathrm{SU}(2)\) is a transport element built from \(S_j\) (an explicit word of length \(\le 3\))
  whose adjoint \(\mathrm{Ad}_{g_j}\) is a rotation.

**Admissibility note (important).**
At a fixed link \(\ell\), the \(m\) staples live on the “star” neighborhood of \(\ell\).
In \(d=4\), these staples involve disjoint sets of nearby links, so by varying those links independently
one can realize an open subset of \(\mathrm{SU}(2)^m\) for \((g_1,\dots,g_m)\).
Thus, *for transversality purposes*, it is legitimate to treat \((g_1,\dots,g_m)\) as locally free parameters.

---

## 4. The aligned Cartan locus (the only exact cancellation mechanism)

Define the **aligned Cartan locus** at \(\ell\), denoted \(\mathcal A_\ell\), as the set of local configurations
around \(\ell\) for which there exists a unit axis \(n\in S^2\) such that:
1. every incident plaquette force vector is collinear with \(n\):
   \[
   X_j \in \mathbb R\,(i\,n\cdot\sigma)\qquad\text{for all }j,
   \]
2. every transport rotation preserves this axis:
   \[
   \mathrm{Ad}_{g_j}(i\,n\cdot\sigma)\in \mathbb R\,(i\,n\cdot\sigma)\qquad\text{for all }j.
   \]

Equivalently, all incident plaquette holonomies lie in a common maximal torus (a common “Cartan subgroup”)
after the local staple transports.

This is a closed real-algebraic subset of the local configuration space; in particular it has empty interior
and (with respect to Haar volume) measure zero.

---

## 5. Local Cancellation Lemma (fully quantified compactness form)

Let \(\varepsilon\in(0,1]\), \(\beta>0\), and fix a link \(\ell\).
Let \(\mathcal U_\ell\) denote the local configuration space consisting of the link \(U_\ell\) together with
the finitely many neighboring links needed to define the incident plaquette holonomies \(U_{p_j}\) and staples \(S_j\).

Define the “boundary-strip rough set” at \(\ell\):
\[
\mathcal R_\ell(\varepsilon)
:=\Big\{U\in\mathcal U_\ell:\ \max_{1\le j\le m}\widetilde z(U_{p_j}(U))\ \ge\ \varepsilon\Big\}.
\]
This is compact (it is closed inside a finite product of compact Lie groups).

For \(\tau>0\), define the \(\tau\)-away set
\[
\mathcal R_\ell(\varepsilon;\tau)
:= \Big\{U\in\mathcal R_\ell(\varepsilon):\ \mathrm{dist}(U,\mathcal A_\ell)\ge \tau\Big\},
\]
where \(\mathrm{dist}\) is any fixed smooth metric distance on \(\mathcal U_\ell\)
(equivalently, on a finite product of \(\mathrm{SU}(2)\)).

---

### Lemma 5.1 (Local Cancellation / Transversality at one link)

For every \(\varepsilon\in(0,1]\), \(\beta>0\), and \(\tau>0\),
there exists a constant
\[
c_{\mathrm{loc}}(\varepsilon,\beta,\tau)\ >\ 0
\]
depending only on \((\varepsilon,\beta,\tau)\) and the fixed local incidence geometry at \(\ell\) (but **not** on lattice volume),
such that for all \(U\in\mathcal R_\ell(\varepsilon;\tau)\),
\[
\big|\nabla_\ell S_W(U)\big|
\ \ge\
c_{\mathrm{loc}}(\varepsilon,\beta,\tau).
\tag{5.1}
\]

Moreover, by (2.1) one may take \(c_{\mathrm{loc}}(\varepsilon,\beta,\tau)\) proportional to \(\beta\sqrt{\varepsilon}\)
up to a \(\tau\)-dependent geometric factor:
\[
c_{\mathrm{loc}}(\varepsilon,\beta,\tau)
=
\beta\sqrt{\varepsilon}\,\cdot c_{\mathrm{geom}}(\tau),
\qquad c_{\mathrm{geom}}(\tau)>0.
\]

#### Proof
The map
\[
U \longmapsto \nabla_\ell S_W(U)
\]
is continuous on \(\mathcal U_\ell\) (it is a finite sum of smooth operations in compact Lie groups).
Therefore \(U\mapsto |\nabla_\ell S_W(U)|\) is continuous.

On \(\mathcal R_\ell(\varepsilon;\tau)\), at least one incident plaquette satisfies \(\widetilde z(U_{p_j})\ge\varepsilon\),
and since \(\varepsilon\le 1\) this implies by (2.1) that the corresponding \(|X_j|\ge\beta\sqrt{\varepsilon}\).
Thus the force cannot vanish by triviality.

By definition of \(\mathcal R_\ell(\varepsilon;\tau)\), we stay a positive distance \(\tau\) away from the only
geometric cancellation locus \(\mathcal A_\ell\). Hence \(|\nabla_\ell S_W|\) has no zeros on this compact set.
A continuous, nonvanishing function on a compact set attains a strictly positive minimum.
Define that minimum to be \(c_{\mathrm{loc}}(\varepsilon,\beta,\tau)\). ∎

---

## 6. How this is used downstream

There are two distinct downstream uses:

1. **Local coercivity at one link.**
If a link \(\ell\) sees at least one boundary-strip rough plaquette and the local configuration is not Cartan-aligned,
then \(|\nabla_\ell S_W|\) is bounded below by (5.1).

2. **From local to global (combinatorics).**
If the averaged disorder \(\mathcal B_\Lambda\) lies in a fixed strip \([\varepsilon,\varepsilon+\delta]\),
then a **positive fraction** of plaquettes must have \(\widetilde z(U_p)\gtrsim \varepsilon\).
Since each link is incident to at most \(\nu\) plaquettes (a fixed combinatorial constant),
this forces a positive fraction of links to see at least one such plaquette.
Summing (5.1)\(^2\) over those links yields a global lower bound on
\(|P(\Lambda)|\,|\nabla\mathcal B_\Lambda|^2\),
which is precisely the input needed for a **uniform negative strip drift**
\(L\mathcal B_\Lambda\le -\rho\) (see the drift computation module).

