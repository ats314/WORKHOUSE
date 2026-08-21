# SU(2) θ-Term Attempts in the Fusion Basis: Positivity Obstruction and a Practical q-6j Caching Strategy
*(A “negative result + algorithmic salvage” note extracted from the SU(2) roadmap / MoA session.)*

## 0. Why include a document that says “no”?

Because a well-grounded “no” is scientific gold: it prevents you from spending six months trying to make a square circle.

The SU(2) material in the project is not “a finished derivation of a θ-term TN from Wilson SU(2) Yang–Mills.”  
What it *does* contain is:

1. a clear argument that **strict local non-negativity** fails in the standard fusion/irrep tensor basis (even at \(\theta=0\) due to oscillatory 6j signs, and certainly for \(\theta\neq 0\) where q-6j’s are complex), and therefore
2. the correct computational posture is **deterministic contraction** (TRG/TNR) with complex tensors, not importance-sampling Monte Carlo, and
3. a plausible engineering plan to make the core expensive ingredient (quantum 6j-symbols) computationally feasible via symmetry reduction + caching.

---

## 1. The positivity obstruction in the fusion/irrep basis

In the fusion-basis construction:

- Link (plaquette) weights from the character expansion are positive (Bessel-function coefficients).
- Gauge invariance is enforced by **vertex intertwiners** built from SU(2) recoupling coefficients (3j/6j symbols).

### Key point

- For \(q=1\) (classical SU(2)), Wigner \(6j\) symbols are real but take **both signs**.
- For \(q\neq 1\) (quantum group \(U_q(\mathfrak{su}(2))\)), \(q\)-\(6j\) symbols are generally **complex**.

Therefore, even if link weights are positive, the fully gauge-invariant vertex tensor cannot have all entries \(\ge 0\) in this representation.

> **Consequence (as stated in the roadmap):**  
> In this fusion/irrep basis, SU(2) lattice gauge TNs cannot be made strictly sign-problem-free at the local level.  
> Monte Carlo is not viable; TRG-style deterministic contraction is the correct tool.

This is the same “phase-isolation dream” as in U(1), but here the phase is intrinsic to the intertwiners.

---

## 2. What *is* salvageable: a TRG-optimized approach

If you accept complex tensors, the goal shifts:

- build the best possible local tensor representation (symmetry-aware, stable, truncated at \(J_{\max}\)),
- contract deterministically with TRG/HOTRG/TNR,
- measure observables as functions of \(\theta\) (or of the quantum-group deformation parameter).

This turns “sign problem” into “complex contraction,” which is hard but not exponentially doomed in the Monte Carlo way.

---

## 3. q-6j symbol computation: caching with symmetry reduction

The expensive step is computing many \(q\)-\(6j\) symbols.

### 3.1 Symmetry reduction idea

6j symbols enjoy large permutation symmetry (and Regge symmetries in the classical case).  
The project discussion suggests exploiting these symmetries to reduce the number of unique values stored by a factor of \(\sim 72\)–\(144\) (depending on which symmetries are used and how they’re counted).

### 3.2 Canonicalization

Define a function
\[
\mathrm{canon}(j_1,\dots,j_6)
\]
that maps any 6-tuple of spins to a canonical representative under the symmetry group, and use that as the hash key in a lookup table.

### 3.3 Recurrence-based generation

Instead of direct summation formulas for each query, compute \(q\)-\(6j\)’s using recurrence relations (quantum analogues of Racah–Wigner recurrences), memoizing base cases and building up.

### 3.4 Back-of-the-envelope feasibility

For \(J_{\max}\approx 10\)–\(20\), a cached table of unique symbols can plausibly live in memory (hundreds of MB to a few GB), and then each vertex-tensor element becomes “just a lookup” plus a short sum over internal channels.

This does not magically make the SU(2) problem easy, but it changes the bottleneck from “hopeless” to “HPC + careful engineering.”

---

## 4. Connection back to the project’s “big idea”

The rotor and U(1) work is about *pushing phases to the boundary* by tracking an additive integer charge.  
The SU(2) story says: in this basis, the phase is welded into the recoupling coefficients.

This suggests a more abstract research question:

> **Working question:**  
> Is there a dual set of variables (loops, surfaces, categorical data) in which the SU(2) θ-phase couples to an additive integer that can be accumulated like a rotor winding number?

If the answer is “yes,” it would be a genuine conceptual breakthrough: it would unify SU(2) with the project’s phase-isolation principle.  
If “no,” then the roadmap’s conclusion stands: embrace complex tensors + deterministic contraction.

Either way, it’s a clean fork in the research tree.

---

## Sources in the project

This note is condensed from:
- `TN_SU2_Roadmap_v2.md` (positivity obstruction + consequences + conceptual q-deformation framing),
- `MoA_Session_2025-11-26T00-12-49.txt` (detailed argumentation and caching/optimization sketches).

