# SONT: Spectral obstruction as an intrinsic net invariant (speculative extract + toy computation)

*Status:* **speculative blueprint**, not a proof.  
*Theme:* replacing “action steepness” or “RG propagation” with an **intrinsic obstruction** that forces
a spectral gap at the operator-algebra level.

---

## 1. The SONT hypothesis (conceptual)

SONT (Spectral Obstruction Net Theory) posits:

- primitive data are a Haag–Kastler net $\mathcal O\mapsto \mathfrak A(\mathcal O)$,
  a vacuum state $\omega_0$, and a DHR/DR gauge reconstruction structure;
- there exists an intrinsic cohomology/extension class $[\alpha]$ (a cocycle/central extension datum)
  constraining the admissible translation representation;
- nontriviality of $[\alpha]$ obstructs the existence of low-energy non-vacuum states.

Provisional slogan:
\[
[\alpha]\neq 0 \quad\Longrightarrow\quad \mathrm{spec}(H)=\{0\}\cup[m([\alpha]),\infty).
\]

This is *not* currently established mathematics; it is a target for “new operator-algebraic
construction principles”.

---

## 2. Toy spectral obstruction: twisted boundary conditions on a ring

A clean place where a cocycle class is visible is quantum mechanics on a circle with a twist
(twisted line bundle). The Hamiltonian on an $N$-site ring with twist $\phi$ is the discrete Laplacian
with a phase on one link:
\[
H_\phi = 2I - \sum_{i=0}^{N-2}\big(|i\rangle\langle i{+}1|+|i{+}1\rangle\langle i|\big)
- e^{i\phi}|N{-}1\rangle\langle 0| - e^{-i\phi}|0\rangle\langle N{-}1|.
\]

- If $\phi=0$, the constant vector is an eigenvector with eigenvalue $0$.
- If $\phi\neq 0$, the constant vector is not allowed by the boundary condition, and the ground energy lifts:
\[
E_0(\phi) = 2 - 2\cos(\phi/N)\;\sim\; \frac{\phi^2}{N^2}\quad(N\to\infty).
\]

So: **a nontrivial twist forbids the zero mode**, but the induced gap scales like $1/N^2$ (finite-size),
not a true infinite-volume mass gap. It is still a good “spectral obstruction” cartoon.

---

## 3. Numerical check (code + output)

The file `sond_toy_twisted_ring.py` (included with this docs set) diagonalizes $H_\phi$ and prints
 the lowest eigenvalues.

**Output (representative run):**

```text
N |  phi (rad) |     E0 (num) |   E0 (exact) |     E1 (num)
-----------------------------------------------------------------
   10 |   0.000000 |  -0.00000000 |   0.00000000 |   0.38196601
   10 |   0.785398 |   0.00616533 |   0.00616533 |   0.29471967
   10 |   1.570796 |   0.02462332 |   0.02462332 |   0.21798695
   10 |   3.141593 |   0.09788697 |   0.09788697 |   0.09788697
   20 |   0.000000 |   0.00000000 |   0.00000000 |   0.09788697
   20 |   0.785398 |   0.00154193 |   0.00154193 |   0.07508953
   20 |   1.570796 |   0.00616533 |   0.00616533 |   0.05526016
   20 |   3.141593 |   0.02462332 |   0.02462332 |   0.02462332
   50 |   0.000000 |  -0.00000000 |   0.00000000 |   0.01577060
   50 |   0.785398 |   0.00024674 |   0.00024674 |   0.01207809
   50 |   1.570796 |   0.00098688 |   0.00098688 |   0.00887607
   50 |   3.141593 |   0.00394654 |   0.00394654 |   0.00394654
  100 |   0.000000 |   0.00000000 |   0.00000000 |   0.00394654
  100 |   0.785398 |   0.00006168 |   0.00006168 |   0.00302181
  100 |   1.570796 |   0.00024674 |   0.00024674 |   0.00222025
  100 |   3.141593 |   0.00098688 |   0.00098688 |   0.00098688
```

Interpretation: the twist lifts the ground energy at fixed $N$, consistent with the exact formula above.

---

## 4. How this could connect back to 4D YM

If one could define an intrinsic $[\alpha]$ for a *continuum* Yang–Mills observable net (e.g. a
translation/gauge 2-cocycle in the DHR field algebra), one could attempt to show:

- the vacuum sector (trivial cocycle) is the only sector supporting arbitrarily low energies;  
- all other sectors have a positive spectral threshold.

To get a true mass gap in infinite volume, one would need an obstruction that does **not** vanish as
the region size grows (unlike the ring twist, which softens with $N$). That suggests the invariant
must be tied to **locality/modular structure**, not just global topology.

---

## 5. Concrete “next math” tasks for SONT

1. Specify the *correct cohomology object*: which group acts (translations? their localizations?),
   what coefficients (center of the field algebra?), and what locality constraints.
2. Prove a “no massless charged sectors” theorem: nontrivial cocycle + locality $\Rightarrow$ no lightlike spectrum.
3. Relate the invariant to known YM structures (center symmetry, 't Hooft flux) **without** smuggling RG in.

---
