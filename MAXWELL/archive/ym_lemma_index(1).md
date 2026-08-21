
# Yang–Mills Project: Lemma and Derivation Index

This index groups the existing project notes and code by topic and points to
the cleaned, rigorously structured mass–gap document.

## 1. Right–Invariant SU(3) Geometry and Wilson Hessian

**Primary sources:**
- `#  RIGHT–INVARIANT SU(3) YANG–MILLS GEOMETRY.txt`
- `B-SHIFT YANG.txt`
- `Discrete 1-form Laplacian on 4D torus, L=2.txt`
- `L2 SU3 Wilson Hessian.txt`

**Core content:**
- Definition of right–invariant tangent frame δU = U X.
- Construction of the Wilson action in these coordinates.
- Gauge generator `G_L(U)` and projector `P_L(U)`.
- Numerical verification on L = 2 that
  - `ker(Δ_1) = gauge ⊕ toron`,
  - the physical sector of the Wilson Hessian is strictly positive.

These ingredients are abstracted into the projector and coercivity lemmas in
`ym_mass_gap_path.tex` (Sections 1–2).

---

## 2. Curvature, Γ₂, and Local Log–Sobolev Inequalities

**Primary sources:**
- `12-5-25 LEMMA.txt`
- `LEMMA 12-5-25.txt`
- `12-5-25 LEMMA2.txt`
- `12-6-25 LEMMA.txt`
- `ym_curvature_flow.py`

**Core content:**
- Gauge–projected Bakry–Émery curvature operator Γ₂ on the physical sector.
- Derivation of a local curvature–dimension bound from the Hessian lower bound.
- Conditional local LSI and spectral gap:
  `Ent(f^2) ≤ (2/C_W) ∫ |P∇f|^2 dμ`.
- Riccati (viscous Hamilton–Jacobi) flow and its Hessian evolution equation.

These are consolidated and cleaned in `ym_mass_gap_path.tex` (Sections 3–4),
with explicit separation between proved lemmas and Hypotheses (H1)–(H2).

---

## 3. HOTRG and Hessian Pushforward

**Primary sources:**
- `ym_hotrg.py`
- `ym_hotrg_jacobian.py`
- `ym_su3_tensor.py`
- `12-4-25 CODERUN*.txt`
- `12-5-25 SIMULATION LONG A100 GEMINI RUN.pdf`
- `12-5-25 CODE 100 RUN.pdf`

**Core content:**
- Definition of the SU(3) Wilson tensor on a block.
- Implementation of a single HOTRG coarse–graining step.
- Numerical Jacobian construction for the HOTRG map.
- Empirical studies of Hessian spectra before/after RG.

In `ym_mass_gap_path.tex` (Section 5), these elements appear as the RG map
`\mathcal R` and its differential `J`, together with a clearly stated
RG–stability hypothesis (H3).

---

## 4. Faddeev Quantum Dilogarithm and q–6j Asymptotics

**Primary sources:**
- `q6j_faddeev_local_asymptotics.txt`
- `q6j_faddeev_lemma_pack.txt`
- `q6j_faddeev_merged_expanded.txt`
- `q6j_error_bound_execution_plan.txt`

**Core content:**
- Local semiclassical expansion of Faddeev’s quantum dilogarithm Φ_b(z).
- Translation to asymptotic formulas for q–6j symbols.
- Strategy for rigorous, computer–assisted error bounds on the q–6j
  approximation, suitable for certified numerics.

These notes form a semi–independent ``toolbox’’ subproject: a path from
analytic properties of Φ_b to validated, interval–arithmetic bounds on
q–6j symbols, to be plugged into any tensor network or spin–foam
representation where they appear.

---

## 5. Grand Challenge and Numerical Evidence

**Primary sources:**
- `=== YANG-MILLS GRAND CHALLENGE INFI.txt`
- `12-5-25 PULSE*.txt`
- `GPT CODE PRODCUTIOPN TEST.txt`
- Run logs and PDFs referenced above.

**Core content:**
- GPU–accelerated Lanczos spectra on large lattices (L=16, 32, …).
- Convexity experiments with Haar mass terms and curvature flow.
- Implementation details and historical conversation logs.

From a rigorous standpoint these files serve as **evidence and guidance**, not
as proofs.  They are intentionally \emph{not} imported into theorems in
`ym_mass_gap_path.tex`, but they motivate Hypotheses (H1)–(H3).

---

## 6. Main Conditional Chain to the Mass Gap

The document `ym_mass_gap_path.tex` distills the rigorous part of the project
into the following chain:

1. Right–invariant SU(3) geometry and gauge projector `P_L(U)`.
2. Gauge–projected coercivity of the Wilson Hessian (Lemma 2.1).
3. Bakry–Émery curvature and local LSI (Theorem 3.1).
4. Riccati stability of the Hessian under curvature flow (Hypothesis H2).
5. RG stability of the Hessian under HOTRG (Hypothesis H3).
6. OS reconstruction from lattice to continuum (Assumption OS).
7. Conditional mass–gap theorem (Theorem 6.1).

Everything that is genuinely proved or standard (geometry of SU(3),
properties of the projector, formal Γ₂ calculus) is kept as lemmas/theorems.
Everything that is still analytic or numerical work in progress is clearly
labeled as a hypothesis.

This index should make it easy to attach future detailed writeups to the
appropriate section of the main logical chain.
