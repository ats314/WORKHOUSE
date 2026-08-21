# Cartan Alignment, Local Cancellation, and the Coercivity Input A′ (SU(2) \(\to\) SU(3))

*This note extracts the “geometric bottleneck” of the fixed-cutoff route: show that rough local plaquette data cannot produce vanishing Wilson force except on a lower-dimensional Cartan-aligned exceptional set.*

---

## 1. The global coercivity input (A′)

Let
\[
\mathcal B_\Lambda(U):=\frac1{|P(\Lambda)|}\sum_{p\in P(\Lambda)}
\Bigl(1-\tfrac1N\Re\operatorname{Tr}U_p\Bigr)
\]
be a disorder functional, and define a “bad set”
\[
K^c(\varepsilon_0):=\{U:\ \mathcal B_\Lambda(U)\ge \varepsilon_0\}.
\]

**Assumption (A′):** there exist constants \(\varepsilon_0,c_0>0\) such that
\[
U\in K^c(\varepsilon_0)\quad\Longrightarrow\quad
|\nabla S_\Lambda(U)|\ge c_0,
\]
with \(c_0\) independent of \(|\Lambda|\).

Interpretation: **no flat rough plateaus** in the Wilson energy landscape.

---

## 2. Reduction to a single link (local cancellation problem)

Fix a link \(\ell\). In \(d=4\), \(\ell\) is incident to \(m=6\) plaquettes, naturally grouped into three transverse pairs. The linkwise force has the schematic form
\[
\nabla_\ell S(U)=\sum_{p\ni\ell}\sigma_{p,\ell}\,\mathrm{Ad}_{g_{p,\ell}(U)}(X_p(U)),
\qquad
X_p(U):=\nabla\Phi_\beta(U_p)\in\mathfrak{su}(N).
\]

A single rough plaquette already contributes a force vector of \(\mathfrak{su}(N)\)-norm bounded below:

**Single-plaquette coercivity:**  
If \(e_p(U):=1-\tfrac1N\Re\operatorname{Tr}(U_p)\ge\varepsilon\), then \(|X_p(U)|\ge c_1(\varepsilon,\beta)>0\) by compactness.

So the *only* way to violate A′ is a high-dimensional conspiracy of cancellations among the transported force vectors at many links.

---

## 3. The SU(2) mechanism: “overdetermined cancellation across three planes”

In \(\mathfrak{su}(2)\cong\mathbb R^3\), the transported forces are ordinary vectors.

If \(\nabla_\ell S(U)=0\) while at least one incident plaquette is rough, then cancellation must occur in **every** transverse plane pair. Each pairwise cancellation imposes that two vectors of comparable magnitude are related by a rotation that preserves their axis. Doing this simultaneously in three independent transverse planes is generically overdetermined.

This suggests the following core lemma:

> **Local cancellation \(\Rightarrow\) Cartan alignment (SU(2)).**  
> Fix \(\varepsilon>0\). Suppose at least one plaquette incident to \(\ell\) satisfies \(e_p\ge \varepsilon\).  
> Then \(|\nabla_\ell S(U)|\ge c(\varepsilon,\beta)\) unless the incident plaquette forces are all aligned in a common Cartan direction and the transports preserve that axis.

Once this is proved at one link with a uniform constant \(c(\varepsilon,\beta)\), A′ follows by a simple incidence-counting argument: if the global average disorder is \(\ge\varepsilon_0\), there exists at least one rough plaquette, hence at least one link adjacent to a rough plaquette, hence a uniform lower bound on \(|\nabla S|\).

---

## 4. Closing the lemma by compactness (what remains to be formalized)

Let \(\mathcal C_\ell\) be the compact (gauge-fixed) finite-dimensional “star” configuration space at \(\ell\).

Define the exceptional set \(\mathcal E_\ell(\varepsilon)\subset \mathcal C_\ell\) to be the set of configurations satisfying:
- at least one incident plaquette is \(\varepsilon\)-rough, and
- \(\nabla_\ell S(U)=0\).

To conclude a uniform lower bound away from \(\mathcal E_\ell\), it is enough to show:

1. **Transport-compatibility constraints are respected:** the \(g_{p,\ell}(U)\) are not arbitrary rotations; they are products of neighboring links. The definition of \(\mathcal E_\ell\) must incorporate these constraints.

2. **Closedness and lower-dimensionality:** show \(\mathcal E_\ell\) is closed and contained in a Cartan-aligned stratum.

3. **Quantitative minimum:** on the compact set
\[
\{U\in\mathcal C_\ell:\ \max_{p\ni\ell} e_p(U)\ge\varepsilon\}\setminus \mathcal E_\ell,
\]
the continuous map \(U\mapsto |\nabla_\ell S(U)|\) attains a positive minimum.

This is “just” compactness + continuity, provided the exceptional set is characterized correctly.

---

## 5. SU(3): what changes and what should survive

For \(G=\mathrm{SU}(3)\), \(\dim\mathfrak{su}(3)=8\) and the maximal torus (Cartan) has dimension 2.

The natural SU(3) generalization of the SU(2) picture is:

- A plaquette force \(X_p\in\mathfrak{su}(3)\) is generically **regular**, with a 2D commuting subalgebra (a Cartan) and a 6D adjoint orbit of noncommuting directions.
- “Alignment” should mean: the six transported forces all lie in a common Cartan subalgebra \(\mathfrak t\subset\mathfrak{su}(3)\), and the transports preserve \(\mathfrak t\) (equivalently: the local configuration reduces to an embedded abelian gauge field).

So the expected SU(3) analogue of the local cancellation lemma is:

> **Local cancellation \(\Rightarrow\) common Cartan (SU(3), expected).**  
> If at least one incident plaquette is rough, then \(\nabla_\ell S=0\) can occur only if all incident plaquette forces lie in a common Cartan and the local transports preserve it.

The proof strategy should again be:
- turn \(\nabla_\ell S=0\) into simultaneous constraints across three transverse plane-pairs,
- show these constraints imply abelianization (common Cartan),
- then apply compactness to get a quantitative lower bound away from the exceptional set.

---

## 6. Why this is a “theory seed” (not just a lemma)

If this Cartan-exception-set mechanism is correct and robust, it becomes a general *design pattern*:

- **Nonabelian stiffness** emerges from the impossibility of multi-plane cancellations unless the configuration abelianizes.
- The only “nearly-flat” directions are those where the dynamics reduces to a maximal torus.

That’s a conceptual bridge between:
- gauge theory (nonabelian holonomy),
- rigidity theory (overdetermined constraints),
- and “rare-event” control (Cartan-aligned exceptional sets behave like thin tubes in configuration space).

---

## Sources inside this project

- Formal statement of A′ and local reduction at one link: `02_Assumption_A_and_LocalCancellation_SU2.docx`
- Project gap map and route decomposition: `PROJECT_GAP_MAP.md`
- Coercivity/drift and K/\(K^c\) gluing overview: `GEMINI 12-17 nOTES.txt`, `APPENDIX_I.md`
