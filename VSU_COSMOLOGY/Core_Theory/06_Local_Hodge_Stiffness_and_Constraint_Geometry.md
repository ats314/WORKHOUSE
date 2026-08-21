# Local Hodge stiffness, gauge exactness, and a Maxwell–Calladine constraint picture

This note extracts a conceptual lemma used throughout the project:
the $1$-form Laplacian and related “stiffness matrices” inherit a structured kernel from **exactness** (gauge) and from **Bianchi-type constraints**.
The project frames this using a mechanical-rigidity analogy (Maxwell–Calladine).

---

## 1. Chain complex structure on the lattice

On a lattice with a cellular structure, there is a cochain complex
\[
C^0 \xrightarrow{d_0} C^1 \xrightarrow{d_1} C^2 \xrightarrow{d_2} C^3 \to \cdots
\]
satisfying exactness identities (always):
\[
d_1 d_0 = 0,
\qquad
d_2 d_1 = 0.
\]

In gauge theory language:
- $d_0$ generates gauge (exact) $1$-forms,
- $d_1$ computes curvature (plaquette “field strength”),
- $d_2$ encodes Bianchi constraints.

---

## 2. The stiffness matrix and its inevitable nullspaces

Consider the $1$-form Laplacian (stiffness operator)
\[
\Delta_1 := d_1^* d_1.
\]

Then:
- $\mathrm{Im}(d_0) \subset \ker(\Delta_1)$ (pure gauge directions carry no curvature),
- and $\ker(d_1)$ (closed $1$-forms) is the larger nullspace containing harmonic sectors.

The project emphasizes a subtle point for nonabelian theories:
even when linearizing, **Bianchi constraints** can behave like “self-stress” constraints in mechanical rigidity.

---

## 3. Maxwell–Calladine analogy

In rigidity theory, a framework has:

- a **compatibility matrix** $R$ mapping displacements to edge-length changes,
- a **stiffness matrix** $R^T R$,
- a kernel from rigid motions,
- and a cokernel (“self-stress”) from constraint dependencies.

The analogy is:

- $d_1$ plays the role of the compatibility matrix,
- $d_1^*d_1$ plays the role of stiffness,
- $\mathrm{Im}(d_0)$ are gauge “motions” in the kernel,
- and the Bianchi identity $d_2 d_1=0$ plays the role of constraint dependence / self-stress.

This picture is useful because it tells you what *cannot* be true:
you cannot hope for strict positivity of $\Delta_1$ without quotienting out gauge and handling constraint dependencies correctly.

---

## 4. Why this matters for decay bounds and functional inequalities

Davies/Combes–Thomas decay bounds (Part 9) for $(m^2 I + \alpha \Delta_1)^{-1}$ depend on controlling off-diagonal couplings of $\Delta_1$.
The project introduces row-sum constants such as
\[
C_0(\Delta_1)
= \max_b \sum_{b'\neq b} |\Delta_1(b,b')|,
\]
and boundary versions $C_\partial$ for localized regions.
These are robust to nullspaces: the mass term $m^2 I$ lifts the kernel.

In the functional-inequality layer, understanding the constraint geometry clarifies where coercivity must come from:
**not** from the linearized stiffness alone, but from nonlinear Wilson-action curvature terms on $K^c$.

---

## 5. Open problem suggested by this viewpoint

Prove a quantitative decomposition:
\[
\|A\|_{C^1}^2
\;\lesssim\;
\|d_1 A\|_{C^2}^2
\;+\;
\mathrm{dist}(A,\mathrm{Im}(d_0))^2
\;+\;
\text{(Bianchi/self-stress correction)}.
\]

Such an inequality would be a “nonabelian Hodge stiffness with constraint correction” statement,
and it would be valuable beyond this project.
