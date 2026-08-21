# Reflection positivity → OS reconstruction → Hamiltonian gap
*(Project extraction: Parts 16–19, especially the permanence of reflection positivity and the “one-step OS/Dirichlet” bridge)*

## 0. Why this matters
The project’s overall architecture is:

1. Prove a **configuration-space spectral gap** for the Langevin diffusion (a Poincaré/log‑Sobolev inequality).
2. Use **Osterwalder–Schrader (OS) reflection positivity** to reconstruct a **Hilbert space + Hamiltonian** from Euclidean lattice data.
3. Transfer the diffusion gap into a **Hamiltonian mass gap** via a *single comparison inequality*.

Steps (1) and (2) are classical in spirit, but the project’s writeup is unusually explicit about what has to be checked on the lattice, and it isolates the exact missing “bridge” inequality.

---

## 1. Lattice OS reflection positivity in one line
Let $\Lambda$ be a finite Euclidean lattice with a time reflection $\theta$ splitting links/plaquettes into “$+$” and “$-$” halves with a reflection plane.

For a suitable class of functions $F$ supported on the $+$ half, OS reflection positivity is
\[
\langle \Theta F\cdot F\rangle_{\mu_\Lambda}\ \ge\ 0,
\tag{1.1}
\]
where $\Theta$ is the reflection/complex-conjugation involution.

### Key input: nonnegative character expansion
For compact gauge group $G$, if the single-plaquette Boltzmann weight admits a character expansion
\[
e^{-\beta\,S_p(U)}=\sum_{R\in\widehat G} a_R(\beta)\,\chi_R(U),
\qquad a_R(\beta)\ge 0,
\tag{1.2}
\]
then OS positivity follows by factorization across the reflection plane and positivity of the coefficients.

This is exactly the lattice mechanism behind reflection positivity of Wilson-type actions.

*(The project writes this out in “Part 16: Lattice OS Axioms,” including the factorization argument and the bookkeeping.)*

---

## 2. OS reconstruction (transfer matrix and Hamiltonian)
Given a reflection-positive Euclidean measure and Euclidean time translations, OS reconstruction produces:

- a pre-Hilbert space $\mathcal H_0$ of “$+$-time observables” modulo the OS null space,
- a completion $\mathcal H$,
- a positivity-preserving contraction semigroup $T(t)$ induced by time translations,
- a self-adjoint Hamiltonian $H_{\mathrm{OS}}\ge 0$ with
  \[
  T(t)=e^{-t H_{\mathrm{OS}}}.
  \tag{2.1}
  \]

The vacuum vector is the class of the constant observable $1$.

### Correlator ↔ spectral gap dictionary
If $H_{\mathrm{OS}}$ has a gap
\[
\mathrm{spec}(H_{\mathrm{OS}})\cap(0,m)=\varnothing,
\tag{2.2}
\]
then suitable Euclidean two-point functions decay like $e^{-m t}$ at large Euclidean time separation.

Conversely, exponential decay plus reflection positivity can often be used to infer a positive spectral gap under standard cyclicity/separating assumptions.

---

## 3. The missing hinge: the one-step OS/Dirichlet comparison
The project isolates a single “bridge” inequality that would convert a configuration diffusion gap into a transfer-matrix/Hamiltonian gap.

### Desired shape (schematic)
Let $T$ be the one-step transfer operator ($T=e^{-aH_{\mathrm{OS}}}$ on $\mathcal H$ for Euclidean time step $a$).  
Let $\mathcal E_\Lambda^{\mathrm{diff}}$ be the diffusion Dirichlet form on configuration space.

The sought inequality is of the form
\[
\langle f,(I-T)f\rangle_{\mathcal H}
\ \le\
C(a)\,\mathcal E_\Lambda^{\mathrm{diff}}(f,f),
\tag{3.1}
\]
for a suitable identification of observables $f$ with elements of $\mathcal H$.

If (3.1) holds with $C(a)=O(a)$, then a diffusion spectral gap $\lambda_{\mathrm{diff}}$ implies a transfer-matrix gap:
\[
1-\|T\|_{\mathrm{mean\ zero}}
\ \gtrsim\ a\,\lambda_{\mathrm{diff}},
\]
which in turn implies a Hamiltonian mass gap $m\gtrsim \lambda_{\mathrm{diff}}$.

### Why this is hard
- $T$ is not obviously a local operator on configuration space; it is defined through Euclidean path integral factorization.
- The diffusion Dirichlet form is local and geometric.
- Bridging them requires a careful “one-step” kernel comparison, typically via:
  - transfer matrix integral kernel representations,
  - comparison with heat kernels,
  - or functional inequalities that compare $L^2$ contractions.

The project correctly flags this as the **single technical bottleneck** between “config gap” and “mass gap.”

---

## 4. Permanence of reflection positivity under coarse-graining and limits
A neat conceptual contribution in the project is the explicit statement:

### Lemma 4.1 (Reflection positivity survives pushforward)
If $\mu$ on fine configurations is reflection positive and $\pi$ is a coarse-graining map commuting with reflection (i.e. $\pi\circ\theta=\theta\circ\pi$), then the pushforward measure
\[
\nu:=\pi_*\mu
\]
is also reflection positive.

This is almost tautological but extremely useful: it says OS positivity is stable under the kinds of blocking maps used in RG.

### Lemma 4.2 (Projective limit stability)
If $\{\mu_n\}$ is a projective system of reflection-positive measures compatible under coarse-graining, then the projective limit measure is reflection positive.

This is the precise technical skeleton behind “RP persists into infinite volume / continuum,” provided the limiting construction is done at the measure level.

---

## 5. Why this is a good extraction target
These OS notes are not “new math” in the sense of inventing reflection positivity, but they *are* high-leverage because they:

- isolate the exact missing inequality (3.1) rather than hiding it in generalities,
- make precise which properties must be preserved under RG blocking,
- and set up a clean interface between probability/geometry (diffusion gap) and QFT (Hamiltonian mass gap).

That modularity is what you need if you want to turn this into a publishable program.

---

## 6. Concrete next research steps
1. **Prove (3.1) in a toy model.**  
   Start with an Abelian gauge theory or a scalar Gaussian field where both $T$ and the diffusion semigroup are explicit kernels.

2. **Use an operator interpolation inequality.**  
   Try to compare $I-T$ to the generator of a Markov chain induced by a one-step heat-bath update; then compare heat-bath Dirichlet forms to diffusion Dirichlet forms.

3. **Exploit stronger symmetry lattices.**  
   If the discretization has higher rotational symmetry (e.g. D4 / 16-cell honeycomb), transfer kernels may be better behaved in the continuum scaling window.

4. **Quantify coarse-graining compatibility.**  
   Make the “$\pi$ commutes with reflection” condition explicit for whatever blocking map you use (plaquette/loop based vs link based).

