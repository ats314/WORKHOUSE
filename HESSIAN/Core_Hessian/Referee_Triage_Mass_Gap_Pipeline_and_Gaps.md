# Referee Triage: Mass-Gap Pipeline — Surviving Claims, Conditional Chain, Removed/Downgraded Items (with reasons), and Missing Lemmas

## Scope and stance

This document triages the mathematical content present in the chat. It is not an exposition. It records which statements can be promoted, which require explicit hypotheses, and which are structurally invalid.

**Operating constraint used here:** the chat corpus is the only admissible input. Any named theorem from outside the corpus is treated as an **External Input** and used only conditionally.

---

## Document dependency ordering

- **Document 1** (finite-volume numerics) supplies data and computational definitions.
- **Document 2** supplies finite-dimensional analytic lemmas about \(\mathfrak{su}(3)\), \(\exp\), and matrix norms.
- This document uses both, and classifies the proof pipeline.

---

## 1. The intended pipeline (as stated in the chat)

The chat proposes the following logical chain:

1. **(Hessian erosion bound)** Establish a global inequality bounding the “negative curvature” induced by the Wilson action by a term \(\sim \beta \|A\|^2\).
2. **(Convexity radius)** Combine (1) with a positive “Haar floor” \(c_0\) to obtain a convexity radius \(R(\beta)\) inside which \(\nabla^2 S_\beta \succeq m_0^2 I\).
3. **(Dynamic restoration)** Show a curvature evolution inequality (Riccati-type) under gradient flow that forces entry into the convex region in finite time.
4. **(LSI / spectral gap)** Use Bakry–Émery or related functional-inequality machinery to deduce log–Sobolev and Poincaré (spectral gap) inequalities from uniform convexity.
5. **(Continuum limit)** Show uniformity of the gap along \(\beta(a)\to\infty\) as \(a\to 0\).
6. **(OS reconstruction)** Transfer Euclidean exponential clustering to a Hamiltonian mass gap via Osterwalder–Schrader reconstruction.

The numerics in Document 1 are intended to support steps (2) and (3) at fixed lattice size.

---

## 2. Classification of major claims

### 2.1 Proved statements (within corpus; finite-dimensional only)

**P1. Matrix calculus lemmas** (Document 2, Sections 0–5):
- unitary invariance of \(\|\cdot\|_{\mathrm{op}}\), \(\|\cdot\|_{\mathrm{HS}}\);
- commutator bounds \(\|[X,Y]\|\le 2\|X\|\|Y\|\) (with appropriate norm conventions);
- explicit Fréchet derivative formulas for \(\exp\) and bounds under \(A\in\mathfrak{su}(3)\).

**Novelty:** standard result; appears in literature (no novelty claim).

---

### 2.2 Conditionally correct statements (true if explicit hypotheses hold)

**C1. “Convexity radius formula” \(R(\beta)\propto \beta^{-1/2}\).**  
Conditionally correct **if** one proves a lower bound of the form
\[
\lambda_{\min}\bigl(\nabla^2 S_{\mathrm{W}}(A)\bigr)\;\ge\; -C\,\beta\,\|A\|_\infty^2
\]
for all \(A\) in the region of interest and if one proves a uniform positive curvature contribution \(c_0\) from the Haar term in the same coordinate system.

**Downgraded because:** the chat did not supply a correct proof of the required Wilson lower bound (see §3.1) and did not supply a derivation of \(c_0=0.125\) in the adopted coordinates.

**Novelty:** the scaling form is standard in perturbative intuition; the chat’s specific *operational definition* of \(R(\beta)\) is numeric.

---

**C2. Finite-dimensional implication “uniform convexity ⇒ LSI ⇒ spectral gap”.**  
Conditionally correct **if** one imports the Bakry–Émery theorem (External Input) in the relevant finite-dimensional setting and verifies its hypotheses (smoothness, log-concavity, etc.) for the measure \(e^{-S_\beta}dA\).

**Downgraded because:** Bakry–Émery / Gross LSI theorems are not proved in the corpus; they are External Inputs.

**Novelty:** standard result; appears in literature (no novelty claim).

---

**C3. “Gradient flow restores convexity in finite time”.**  
Conditionally correct **if**:
- the flow is well-posed globally (finite-dimensional ODE; likely true but not proved in the corpus),
- one proves a differential inequality for \(\lambda_{\min}(\nabla^2 S(A_t))\) along the flow (External Input or additional derivation),
- and one bounds the relevant forcing terms by the same quantities that define the convexity radius.

**Downgraded because:** the chat’s Riccati inequality step uses unproved curvature-evolution identities (External Input or missing lemma).

**Novelty:** the *idea* of “convexity restoration under flow” is a nonstandard organizing device; see §4.

---

### 2.3 Conjectural / heuristic statements

**H1. Uniformity in the continuum limit \(a\to 0\).**  
No controlled renormalization argument appears in the corpus. The claim that any constant \(m_{\min}\) obtained at fixed \(a\) remains bounded below uniformly along \(\beta(a)\to\infty\) is not derived.

**Downgraded because:** asserts uniformity without justification; confuses finite-volume computations with scaling limits.

---

**H2. OS reconstruction yields Hamiltonian mass gap \(m_{\mathrm{gap}}>0\).**  
Even if one had uniform Euclidean clustering, the transfer to a Hamiltonian gap requires:
- reflection positivity,
- existence and identification of the continuum measure,
- OS axioms,
- control of the scaling limit,
none of which is established in the corpus.

**Downgraded because:** spectral claims are asserted without OS/transfer justification within the corpus.

---

**H3. “Reducible strata are polar / capacity zero, hence ignorable”.**  
This invokes capacity theory and Dirichlet forms. No rigorous construction of the relevant Dirichlet form, capacity, or proof of polarity appears in the corpus. It also implicitly assumes absolute continuity and quasi-regularity in a way not established here.

**Downgraded because:** uses named theorems (Fukushima et al.-type results) without stating hypotheses or proving applicability.

---

### 2.4 Incorrect or structurally invalid statements

These items must be removed from any “proof” draft.

#### I1. The claimed global Wilson Hessian bound as stated in the chat

Claimed (in several variants):
\[
\|\nabla^2 S_{\mathrm{W}}(A)\|
\le
C\,\beta \sum_\ell \|A_\ell\|^2.
\]

**Removed / downgraded because (precise reason):**
- At \(A=0\), the RHS is \(0\). The Wilson action has a nontrivial quadratic part (though gauge-degenerate) and hence \(\nabla^2 S_{\mathrm{W}}(0)\) is not identically the zero operator. Therefore the inequality in operator norm cannot hold as stated.
- The proof sketch in the chat introduced ad hoc restrictions \(\|A\|\le \rho\) and then “absorbed exponentials into constants,” which is not a global argument.
- The inequality needed for the convexity-radius mechanism concerns the **negative part / minimal eigenvalue** of the Wilson Hessian, not the operator norm of the full Hessian.

**What may survive as a corrected target statement:**
A plausible (but unproved) replacement consistent with the numerical narrative is:
\[
\lambda_{\min}\bigl(\nabla^2 S_{\mathrm{W}}(A)\bigr) \ge -C\,\beta\,\|A\|_\infty^2
\quad\text{for } \|A\|_\infty \text{ sufficiently small}.
\]
This is not established in the corpus.

---

#### I2. Any statement treating finite-sample numerics as proof

Examples: “Theorem verified,” “mass gap restored,” “convexity persists with no volume collapse.”

**Removed / downgraded because:** finite-sample Monte Carlo + approximate Lanczos eigenvalues do not imply analytic inequalities, nor do they imply behavior as \(L\to\infty\) or \(a\to 0\).

---

## 3. Salvageable reformulations and corrected dependency chain

### 3.1 Corrected analytic bottleneck

The pipeline requires an inequality of the schematic form:
\[
\nabla^2 S_{\mathrm{Haar}}(A) + \nabla^2 S_{\mathrm{W}}(A)
\;\succeq\;
c_0 I - C\,\beta\,\|A\|_\infty^2 I
\quad\text{(in some region)}.
\]

The corpus supplies:
- numerical evidence for the *resulting* dependence \(\lambda_{\min}\approx c_0 - C\beta r^2\) (Document 1),
- basic matrix calculus lemmas (Document 2),
but does not supply the missing inequality as a theorem.

Thus the strongest honest statement available is conditional:

> If one proves a uniform lower bound on the minimal eigenvalue of the Wilson Hessian of order \(-\beta\|A\|^2\) and one proves a positive Haar curvature floor \(c_0\) in the adopted coordinates, then a convexity radius \(R(\beta)\sim \beta^{-1/2}\) follows.

---

## 4. Structural contributions to preserve

### 4.1 Pipeline Architecture (nonstandard organizing principle)
**Claim:** Use a flow to drive configurations into a convex region where functional inequalities can be invoked.

- **Status:** plausible architecture; not a proof.
- **Novelty:** I do not know whether this exact combination (“curvature-stable flow” as the central mediator between nonconvex action and LSI) exists in the literature in this form. It may be new as an organizing principle.

### 4.2 Rigidity Mechanism (convex core controlled by Haar term)
**Claim:** a positive “Haar floor” plus a quadratic-in-amplitude bound on negative Wilson curvature yields a convex core.

- **Status:** conditional; depends on the missing Wilson lower bound and on a precise Haar-curvature statement.
- **Novelty:** the mechanism is standard in spirit (mass terms regularize), but the specific implementation via “Haar curvature floor” in exponential coordinates may be a nonstandard repackaging.

### 4.3 Numerical mapping as evidence (finite-volume)
**Claim:** the convexity boundary \(R(\beta)\) computed by conservative bisection is stable and monotone in \(\beta\) at \(L=8\).

- **Status:** proved only as “the program printed these numbers”; it is a reproducible numerical record if code is retained.
- **Novelty:** plausibly novel as a specific multi-\(\beta\) convexity-boundary scan for SU(3) in 4D; cannot be promoted without external verification and independent replication.

---

## 5. What is known vs new (as far as can be inferred here)

- Commutator and exponential derivative bounds: **Standard result; appears in literature.**
- “Uniform convexity ⇒ LSI ⇒ spectral gap”: **Standard result**, but **External Input** in this corpus.
- OS reconstruction: **Standard framework**, but **External Input** and not instantiated here.
- “Curvature-stable flow enters convex core”: **No clear prior equivalent known to me** in this precise packaging; **plausibly novel**, but currently only heuristic/conditional.

---

## 6. What strengthens this work most

### 6.1 Missing lemmas (minimal list)

**M1. Correct Wilson Hessian erosion bound (core gap).**  
A rigorous statement bounding the *negative part* (or minimal eigenvalue) of \(\nabla^2 S_{\mathrm{W}}(A)\) by a constant times \(\beta \|A\|_\infty^2\) in a specified region. This must be stated with correct norms and must not contradict the behavior at \(A=0\).

**M2. Haar curvature floor in the adopted coordinate chart.**  
A derivation of \(c_0>0\) (and of the numerical value 0.125 if claimed) for \(\nabla^2 S_{\mathrm{Haar}}\) in the specific exponential coordinates used by the code.

**M3. Well-posedness and curvature evolution inequality along the chosen flow.**  
A lemma deriving the differential inequality used for “Riccati restoration” (or an alternative comparison principle that does not require unproved Γ₂ identities).

**M4. Controlled limit procedures.**  
If the goal is a continuum statement: a renormalization/tightness argument showing that the relevant constants do not degrade as \(a\to 0\), plus OS positivity verification in the limit.

### 6.2 The single sharpest theorem the corpus currently supports

**Sharpest supported statement (non-analytic):**  
For \(L=8\) and \(c_0=0.125\) as implemented, the code outputs an empirical convexity boundary \(R(\beta)\) (Document 1, §C.1) and demonstrates at least one instance of restoration under gradient descent from an unstable configuration (Document 1, §D).

This is evidence, not a theorem about SU(3) Yang–Mills.

### 6.3 Minimum additional assumption to close the main gap

Assume:

- (A) a proven lower bound of the form
  \[
  \lambda_{\min}\bigl(\nabla^2 S_{\mathrm{W}}(A)\bigr)\ge -C\beta \|A\|_\infty^2
  \quad \text{for }\|A\|_\infty\le r_\ast,
  \]
  for explicit \(C,r_\ast>0\);
- (B) a proven Haar floor \(\nabla^2 S_{\mathrm{Haar}} \succeq c_0 I\) in the same region.

Then the convexity-radius mechanism becomes a straightforward corollary, and all later functional-inequality steps become conditional only on standard external theorems (Bakry–Émery; OS reconstruction; continuum limit construction).

---
