# Rigorous q–6j Error Certification Module

This note extracts a self-contained “computer-assisted proof module” present in the project corpus: a plan to rigorously bound the difference between the quantum \(q\)-\(6j\) symbol and its classical limit using explicit asymptotics of the Faddeev quantum dilogarithm, plus certified interval arithmetic.

While not SU(3) Wilson-HOTRG directly, it is presented in the corpus as an auxiliary pillar: a way to certify constants that appear in deformation / quantum-group steps.

## Target inequality (as stated in corpus)

The corpus aims to bound an “error term” \(\Delta\) in a \(q\)-\(6j\) asymptotic by an explicit polynomial-in-spin factor times \(b^2\theta^2\):
\[
|\Delta| \;\le\; C_{\mathrm{rig}}\; b^2\,\theta^2\,J_{\max}^{5/2},
\]
uniformly on a compact domain in the parameters with explicit constraints:
- \(b\in(0,1]\),
- \(\theta\in[0,\theta_0]\),
- spins in a bounded integer box and “away from degeneracy” (stated as a polynomial nonvanishing condition).

Here \(q=e^{i\pi b^2}\) is the quantum parameter and \(J_{\max}\) is the maximum spin.

**Source pointers (project files):**
- `q6j_faddeev_merged_expanded.txt` (lemma pack and stated error bound goal).
- `q6j_error_bound_execution_plan.txt` (detailed certification plan to compute \(C_{\mathrm{rig}}\)).

## Local asymptotics of Faddeev quantum dilogarithm (extracted lemma form)

A central ingredient is a local expansion for the logarithm of the Faddeev quantum dilogarithm \(\Phi_b(z)\) at small \(b\):
\[
\log \Phi_b(z)
=
\frac{1}{2i\hbar}\,\mathrm{Li}_2(-e^{2\pi b z})
\;+\;
\frac{1}{2}\log(1+e^{2\pi b z})
\;+\;
R_b(z),
\]
where \(\hbar = \pi b^2\) and the remainder \(R_b\) is controlled uniformly on a compact complex strip.

The corpus uses this to control phase cancellations and ultimately isolate the \(O(b^2)\) remainder that contributes to \(\Delta\).

**Source pointers (project files):**
- `q6j_faddeev_merged_expanded.txt` (the explicit local lemma and the remainder structure).

## Certification plan (interval arithmetic)

The corpus specifies a concrete “execution plan” to certify \(C_{\mathrm{rig}}\) without requiring human analytic bounding at every step:

1. **Factor the dominant exponential part.**  
   Represent the error integrand as
   \[
   \exp(\Phi)\cdot E
   \]
   where \(\Phi\) is a polynomial/analytic “phase” and \(E\) is the residual.

2. **Certified bounds on \(E\).**  
   Bound \(|E|\) uniformly on compact domains using interval arithmetic.

3. **Stationary region handling.**  
   Split the domain into “stationary” and “nonstationary” regions and apply:
   - direct bounds away from stationary points,
   - quadratic/Taylor enclosure near stationary points.

4. **Uniform denominators and away-from-degeneracy constraints.**  
   Explicitly track conditions ensuring denominators do not vanish (triangular inequalities and a nondegeneracy polynomial).

5. **Compute a numeric \(C_{\mathrm{rig}}\) and store it with a certificate.**

**Source pointers (project files):**
- `q6j_error_bound_execution_plan.txt` (step-by-step algorithm and tooling suggestions).

## Why this module is interesting (purely technically)

- It is explicitly structured as a *certified bound computation* rather than a heuristic asymptotic.
- The plan separates symbolic factoring and numerical certification cleanly.
- The intended end product is a reusable constant \(C_{\mathrm{rig}}\) that can be injected into later steps as a verified parameter.

## Next development steps

1. Implement the interval-arithmetic evaluator with rigorous rounding (e.g. MPFI / Arb bindings).
2. Encode the domain constraints and degeneracy-avoidance polynomial.
3. Produce a machine-checkable certificate: domain cover + max bound per tile + proof of cover completeness.

