# Tubular neighborhood of the flat stratum: a geometric reduction (idea seed with teeth)

> **What this is.** A distilled version of the project’s “tubular neighborhood proposition”:
> a strategy to reduce hard infinite-dimensional control (as lattice spacing \(a\to 0\))
> to **finite-dimensional Riemannian geometry** of the gauge orbit space at fixed cutoff.

This is not a completed theorem in the files; it’s a *high-leverage reduction* that tells you where the real work is.

---

## 1. The geometric object

At cutoff \(a>0\), configuration space is a compact Lie group product
\[
\mathcal C_a \;=\; G^{E(a)},
\]
one copy of \(G\) per lattice edge.

Gauge transformations form a compact group
\[
\mathcal G_a \;=\; G^{V(a)},
\]
acting smoothly on \(\mathcal C_a\) by the usual left/right multiplications at edge endpoints.
The orbit space (at least on the free-action locus) is the quotient manifold
\[
\mathcal M_a := \mathcal C_a / \mathcal G_a.
\]

The “vacuum / flat” stratum is the subset of connections with zero curvature (plaquette holonomies \(=I\)).
Call it \(\mathcal F_a\subset \mathcal M_a\).

---

## 2. The proposition (as a program)

**Proposed statement.** There exists a tubular neighborhood \(\mathcal T_a\) of \(\mathcal F_a\) in \(\mathcal M_a\)
such that, uniformly in \(a\to 0\),

1. the exponential map gives a diffeomorphism from a normal bundle neighborhood onto \(\mathcal T_a\);
2. the Jacobian of this chart (and its inverse) has uniform bounds;
3. the sectional curvature (or a suitable Bakry--Émery curvature matrix) on \(\mathcal T_a\) is uniformly bounded.

If true, local estimates (e.g. Bakry–Émery lower bounds needed for functional inequalities)
become uniform in \(a\), which is the geometric heart of taking a continuum limit in these methods.

---

## 3. Why this is plausible

The quotient map
\[
\pi:\mathcal C_a \to \mathcal M_a
\]
is a Riemannian submersion for natural product metrics (after choosing a horizontal distribution).
Curvature on \(\mathcal M_a\) is controlled by the O'Neill formulas:
it is the curvature of \(\mathcal C_a\) plus terms involving the integrability tensors of the horizontal distribution.

Since \(\mathcal C_a\) is a product of compact Lie groups with bounded geometry,
the only way curvature blows up is if the horizontal distribution becomes ill-conditioned,
which geometrically corresponds to approaching a singular orbit / stabilizer change.

But near the flat stratum, gauge orbits should be “as regular as possible” (no wild stabilizers),
so a uniform tubular neighborhood is not crazy.

---

## 4. What you would actually prove (concrete targets)

1. **Uniform slice theorem near flat connections.**  
   Produce a gauge-fixing slice (e.g. Coulomb/Landau) giving local coordinates transverse to gauge orbits,
   with constants independent of \(a\).

2. **Uniform bounds on the second fundamental form of orbits.**  
   Control the O’Neill \(A\)-tensor by explicit lattice differential operators.
   This is where discrete Hodge theory (and your stiffness lemmas) enter.

3. **Injectivity radius control.**  
   Show the quotient metric doesn’t develop arbitrarily short geodesic loops in \(\mathcal T_a\) as \(a\to 0\).

---

## 5. Why this might generalize (a “bigger theory” angle)

This program reframes “continuum gauge theory estimates” as:

> **Bounded-geometry control of a sequence of quotient manifolds \(\mathcal C_a/\mathcal G_a\)**  
> with increasing dimension but uniform local structure.

That is a perspective borrowed from geometric group actions and
could apply to other constrained lattice field theories (sigma models, spin foams, etc.)
where the continuum limit is hard precisely because orbit spaces get singular.

---
