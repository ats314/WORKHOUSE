# Staple–Projection Formula for the Pairing Term and a Route to Coercivity

This note rewrites the **pairing term**
\[
\langle \nabla S(U),\nabla \bar V(U)\rangle
\]
appearing in the Langevin drift
\[
L\bar V=\Delta \bar V-\langle \nabla S,\nabla \bar V\rangle
\]
in explicit **staple form**, and then recasts the desired **outside–core lower bound**
\[
\frac{\langle \nabla S,\nabla \bar V\rangle}{B_{\rm avg}}
\;\ge\; c_\star
\qquad\text{on }\{B_{\rm avg}\ge \tau_0\}
\]
as a finite–range geometric inequality on the lattice.

The goal is not to match the empirically observed constant \(c_\star\approx 20.9\) exactly, but to produce an analytic *structure theorem* that makes such a uniform-in-volume bound plausible and attackable.

---

## 1. Setup and conventions

Let the lattice be \(D\)-dimensional periodic hypercubic with link set \(E\) and plaquette set \(P\).
Each link carries \(U_\ell\in SU(2)\).

### 1.1 Plaquette defect

For each plaquette \(p\) with ordered product \(U_p\in SU(2)\), define the *defect*
\[
z_p \;:=\; 1 - \frac{1}{2}\Re\mathrm{Tr}(U_p)\in[0,2].
\]

Define the total defect and its mean:
\[
Z(U) := \sum_{p\in P} z_p,\qquad
B_{\rm avg}(U) := \frac{1}{|P|}Z(U),
\qquad
\bar V(U):=1+B_{\rm avg}(U).
\]

The Wilson action in the simulation is exactly
\[
S(U)=\beta\, Z(U).
\]

Hence **directional derivatives are proportional**:
for any tangent direction \(X\),
\[
D_X S=\beta\,D_X Z,\qquad
D_X\bar V = \frac1{|P|}D_X Z,
\qquad\Rightarrow\qquad
(D_X S)(D_X\bar V)=\frac{\beta}{|P|}(D_X Z)^2\ge 0.
\]

In particular \(\langle\nabla S,\nabla\bar V\rangle\ge 0\) is not mysterious: it is a scaled squared norm.

---

## 2. The link–staple expression for \(\nabla Z\)

Fix a link \(\ell=(x,\mu)\).
Let \(p\ni \ell\) denote plaquettes containing \(\ell\).
For each such plaquette, write the plaquette product in oriented form
\[
U_p \;=\; U_\ell\, K_{p,\ell},
\]
where \(K_{p,\ell}\in SU(2)\) is the product of the other three links of \(p\)
(the usual “staple” around \(\ell\) in that plaquette).

Define the **staple sum** at \(\ell\):
\[
\Omega_\ell \;:=\; \sum_{p\ni \ell} K_{p,\ell}.
\]
On a hypercubic lattice, each link belongs to \(2(D-1)\) plaquettes, so \(\Omega_\ell\) is a sum of \(2(D-1)\) \(SU(2)\) matrices.

### 2.1 Projection onto \(\mathfrak{su}(2)\)

For any \(2\times 2\) complex matrix \(M\), define the projection to the Lie algebra:
\[
\Pi_{\mathfrak{su}(2)}(M)
:= \frac12(M-M^\dagger) - \frac12\mathrm{tr}\!\left(\frac12(M-M^\dagger)\right)\mathbf 1,
\]
the traceless anti-Hermitian part.
This is the orthogonal projection with respect to the standard bi-invariant metric
\(\langle A,B\rangle = -\tfrac12\mathrm{Tr}(AB)\) on \(\mathfrak{su}(2)\).

**Representation-theoretic meaning.**
In the fundamental representation, \( \mathrm{End}(\mathbb C^2)\cong \tfrac12\otimes \tfrac12^\ast\cong 0\oplus 1\).
The trace part is the spin-0 component; the traceless anti-Hermitian part transforms in the spin-1 (adjoint) representation.
Thus \(\Pi_{\mathfrak{su}(2)}\) is literally the “adjoint projector.”

### 2.2 Differentiating \(Z\) at a link

Use a left-invariant variation \(U_\ell(t)=e^{tX}U_\ell\) with \(X\in\mathfrak{su}(2)\).
For one plaquette \(p\ni\ell\),
\[
\frac{d}{dt}\Big|_{t=0}\left(\frac12\Re\mathrm{Tr}(U_\ell(t)K_{p,\ell})\right)
=\frac12\Re\mathrm{Tr}(X\,U_\ell K_{p,\ell}).
\]
Summing over plaquettes incident to \(\ell\) gives
\[
D_X Z \;=\; -\frac12\Re\mathrm{Tr}\!\left(X\,U_\ell\Omega_\ell\right)
\;=\; \left\langle X,\; -\Pi_{\mathfrak{su}(2)}(U_\ell\Omega_\ell)\right\rangle.
\]
Therefore the link component of the gradient is
\[
\nabla_\ell Z(U)\;=\;-\Pi_{\mathfrak{su}(2)}(U_\ell\Omega_\ell)\;\in \mathfrak{su}(2).
\]

---

## 3. Pairing term as a sum of squared projected staples

Since \(S=\beta Z\) and \(\bar V = 1 + Z/|P|\),
\[
\nabla S = \beta\,\nabla Z,\qquad
\nabla \bar V = \frac{1}{|P|}\nabla Z.
\]
Hence
\[
\boxed{
\langle \nabla S,\nabla \bar V\rangle
=\frac{\beta}{|P|}\,\|\nabla Z\|^2
=\frac{\beta}{|P|}\sum_{\ell\in E}\big\|\Pi_{\mathfrak{su}(2)}(U_\ell\Omega_\ell)\big\|^2.
}
\]
This is the staple/projection form you want.

If one prefers the standard lattice-gauge “force” tensor,
define
\[
F_\ell := \Pi_{\mathfrak{su}(2)}(U_\ell\Omega_\ell)\in\mathfrak{su}(2).
\]
Then
\[
\langle \nabla S,\nabla \bar V\rangle
=\frac{\beta}{|P|}\sum_{\ell}\|F_\ell\|^2.
\]

---

## 4. Reformulating the desired coercivity bound

The target inequality
\[
\langle \nabla S,\nabla\bar V\rangle \ge c_\star B_{\rm avg}
\qquad \text{on }\{B_{\rm avg}\ge\tau_0\}
\]
is equivalent to
\[
\frac{\beta}{|P|}\|\nabla Z\|^2 \;\ge\; c_\star\,\frac{Z}{|P|}
\qquad\Leftrightarrow\qquad
\boxed{
\|\nabla Z\|^2 \;\ge\; \kappa_\star\, Z
\quad\text{on }\{Z\ge \tau_0|P|\},
}
\]
where \(\kappa_\star := c_\star/\beta\).

So the pairing coercivity problem is exactly a **Polyak–Łojasiewicz type inequality** for the total defect functional \(Z\), but only outside a “small-defect” core.

---

## 5. Local SU(2) geometry: defect vs adjoint size on one plaquette

For a single \(SU(2)\) element written as
\[
U = \cos\theta\,\mathbf 1 + i\sin\theta\,\hat n\cdot\sigma,
\qquad \theta\in[0,\pi],
\]
the defect is \(z=1-\cos\theta\) and the adjoint (imaginary) magnitude is
\[
\|\Pi_{\mathfrak{su}(2)}(U)\|^2 = \sin^2\theta = z(2-z).
\]

Consequences:

- For **positive-trace plaquettes** (\(\cos\theta\ge 0\), equivalently \(z\le 1\)),
  \[
  \sin^2\theta = z(2-z)\;\ge\; z.
  \]
- If plaquettes can approach the center element \(-\mathbf 1\) (\(z\to 2\)),
  then \(\sin^2\theta\to 0\) while \(z\to 2\).
  So **no global inequality** of the form \(\sin^2\theta \ge c z\) can hold without excluding the neighborhood of \(z=2\).

This is the unavoidable “near-\(-\mathbf 1\)” obstruction that any rigorous coercivity statement must explicitly control.

---

## 6. What remains: a finite-range coercivity inequality

Using the staple formula, we have
\[
\|\nabla Z\|^2
=\sum_{\ell}\|F_\ell\|^2
=\sum_{\ell}\big\|\Pi_{\mathfrak{su}(2)}(U_\ell\Omega_\ell)\big\|^2.
\]
Meanwhile
\[
Z=\sum_{p} z_p.
\]

So the analytic task is now *purely local/combinatorial*:

> **Goal.** Prove there exists \(\kappa>0\) and \(\tau_0\in(0,2)\), independent of volume, such that
> \[
> \sum_{\ell}\|F_\ell\|^2 \;\ge\; \kappa \sum_{p} z_p
> \qquad\text{on }\left\{\frac1{|P|}\sum_p z_p \ge \tau_0\right\},
> \]
> possibly after excluding a neighborhood of plaquettes with \(z_p\approx 2\).

### 6.1 A workable proof architecture (block lemma)

A strategy that *can* be volume-independent:

1. **Local block inequality.**
   On a fixed finite block \(B\) (say a \(2^D\) hypercube with a 1-link buffer),
   show an inequality of the form
   \[
   \sum_{\ell\subset B}\|F_\ell\|^2 \;\ge\; \kappa_B \sum_{p\subset B} z_p
   \]
   unless all \(z_p\) in the block are tiny (the block is “good/core-like”).
   Here \(\kappa_B>0\) is a block constant, independent of global volume.

2. **Covering/packing.**
   Tile the lattice by disjoint translated copies of \(B\) (or a bounded-overlap cover).
   Sum the block inequalities.

3. **Core set handling.**
   Blocks where all \(z_p\) are tiny fall into the core region.
   Outside the global core \(\{B_{\rm avg}<\tau_0\}\),
   there must be a positive density of “bad” blocks where the inequality triggers,
   giving a global constant \(\kappa\) independent of volume.

This mirrors exactly the empirical “two-region” story: outside a defect-density core,
a finite-range inequality should force strong drift.

### 6.2 Why the adjoint projector is the right representation tool

The decomposition \( \tfrac12\otimes\tfrac12^\ast\cong 0\oplus 1\) is the clean reason the **force lives in spin-1** while the **defect is spin-1/2**:

- The plaquette term uses the fundamental character \(\chi_{1/2}(U_p)=\mathrm{Tr}(U_p)\).
- Differentiating \(\chi_{1/2}\) inserts a Lie algebra generator, i.e. moves you into the adjoint channel.
- The operator \(\Pi_{\mathfrak{su}(2)}\) is exactly the projection onto that channel.

So proving coercivity is, at heart, proving that “enough adjoint content” is generated whenever the fundamental-character defect density is large.

---

## 7. Practical next steps (analytic + diagnostic)

1. **Rule out the center obstruction explicitly.**
   Decide whether your proof will:
   - exclude configurations with a positive density of \(z_p\) near \(2\), or
   - add a second Lyapunov term that blows up as \(z_p\to 2\).

2. **Inspect worst-case configurations near \(\tau_0\).**
   In your empirical certificate, the worst points controlling \(c(\tau)\) at \(\tau\approx 0.39\)
   are the ones to study: do they look like local cancellations of staples, or like near-center plaquettes?

3. **Try a cube-wise lemma.**
   The smallest nontrivial local object that couples plaquettes and link-forces is an elementary cube.
   The lattice Bianchi identity ties the six face plaquettes of a cube.
   That is the natural place to stop staple cancellations from happening “for free.”

4. **Linearize only as a *local* heuristic.**
   Near-identity fields reduce to a gauge-covariant divergence/curl story,
   but that regime is precisely the *core*.
   Your outside-core inequality must exploit nonlinearity / bounded geometry, not small-angle expansions.

---

## 8. Summary

- The pairing term has the exact staple/projection identity
  \[
  \langle \nabla S,\nabla \bar V\rangle
  =\frac{\beta}{|P|}\sum_{\ell}\big\|\Pi_{\mathfrak{su}(2)}(U_\ell\Omega_\ell)\big\|^2.
  \]
- The desired coercivity is equivalent to a PL-type inequality
  \[
  \|\nabla Z\|^2 \ge \kappa Z
  \quad\text{outside a defect-density core}.
  \]
- Representation theory enters cleanly via
  \(\mathrm{End}(\mathbb C^2)\cong 0\oplus 1\):
  the force is the adjoint projector of staples.

The remaining obstacle is now sharply localized:
prove a **finite-range block inequality** preventing staples from canceling too efficiently
whenever the block carries nontrivial defect density, while explicitly managing the near-\(-\mathbf 1\) obstruction.

