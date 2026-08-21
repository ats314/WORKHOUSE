# Clay Submission Checklist and Proof-Stack Audit

This file contains the “Clay submission checklist” style audit drafted in the chat: what appears rigorous vs what needs tightening/references.

---

## Base Setup, Function Spaces, Gauge Group

**Status:** Rigorous (modulo standard gauge theory literature).

Items to cite or standardize:
- Uhlenbeck slice theorem (or equivalent)
- Sobolev embeddings in 4D

---

## UV Control (Theorem A)

**Status:** Rigorous in structure; some quantitative details may need fuller writeup.

To tighten:
- Explicit Riccati/ODE inequalities with constants
- Explicit derivation of polylog factors (if used)

---

## Continuum Polarity (Theorem C)

**Status:** Rigorous and clean.

To tighten:
- Cite a reference for “infinite codimension ⇒ zero capacity”
- Cite standard gauge theory references identifying reducibles as infinite-codimension strata

---

## Off-Diagonal Hessian Decay (H3)

**Status:** Rigorous and strong (finite-range locality).

To tighten:
- Define graph-distance precisely and its scaling with physical distance

---

## Infrared Decoupling (Theorem IR)

**Status:** Rigorous given H3 and the local Hessian floor.

To tighten:
- Make “for sufficiently small a” explicit when invoking block structure

---

## Measure Existence, Uniqueness, Closability (Theorem E)

**Status:** Solid after H1/H2/H3 rewrites; references still needed.

To tighten:
- Prokhorov theorem application details
- Dirichlet-form closability references under Mosco/weak convergence

---

## Holonomy, Gradient, Uniform Integrability Lemmas

**Status:** Standard structure; needs citations and/or explicit estimates.

To tighten:
- Differentiability/continuity of holonomy maps in Sobolev topologies
- LSI ⇒ Herbst ⇒ exponential integrability (cite Bakry–Émery / Ledoux)

---

## Mosco Convergence & Curvature Stability (Theorem M)

**Status:** Rigorous modulo standard theorems.

To tighten:
- Cite a theorem: Mosco convergence ⇒ semigroup convergence
- Clarify cylindrical core and closure steps

---

## LSI Lifting & Spectral Gap (Theorem D)

**Status:** Standard once BE is established.

To tighten:
- Cite Bakry–Émery implication \(CD(\rho,\infty)\Rightarrow \mathrm{LSI}(\rho)\) in the relevant setting

---

## PBH / Geometric Flow Layer

**Status:** Optional after refactor.

Recommendation:
- Demote PBH flow to interpretative appendix unless fully formalized

---

## Reflection Positivity & OS Reconstruction (Theorem OS)

**Status:** Standard, but reference-heavy.

To tighten:
- Cite lattice reflection positivity for Wilson action (e.g. Osterwalder–Seiler, Seiler)
- Cite OS reconstruction theorem
- Provide a careful statement linking Euclidean semigroup/spectral gap to Hamiltonian mass gap (Feynman–Kac–Nelson style)

---

## Final Mass-Gap Theorem

**Status:** Structurally correct, conditional only on standard external frameworks once fully cited.

---

## Minimal “Submission Readiness” TODO list

1. Add authoritative references for:
   - gauge slice theory
   - capacity zero results
   - Mosco/Dirichlet-form stability
   - OS reconstruction and reflection positivity
2. Expand holonomy/gradient approximation lemmas with explicit constants or clear citations.
3. Ensure every “eventually”/“for small a” step has a precise lemma.

