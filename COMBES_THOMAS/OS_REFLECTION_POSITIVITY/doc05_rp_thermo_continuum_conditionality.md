# Reflection Positivity, Thermodynamic Limit, and Continuum Conditionality (Clay-safe phrasing)

*This note isolates what is proved at fixed cutoff vs. what is explicitly conditional in the continuum limit. The goal is a phrasing that is precise, referee-friendly, and does not overclaim beyond the project’s internal modules.*

---

## 1. What is unconditional in the project (fixed cutoff)

At fixed lattice spacing \(a>0\) and fixed gauge coupling parameter \(\beta\), the project’s internal “analytic spine” is designed to produce:

1. **Volume-uniform exponential clustering** for local observables:
\[
|\mathrm{Cov}_{\mu_{\Lambda,\beta}}(F,G)|
\ \le\ C(F,G)\,e^{-\eta(a)\,\mathrm{dist}(\mathrm{supp}F,\mathrm{supp}G)}
\]
with \(\eta(a)>0\) and constants uniform in \(|\Lambda|\) once the remaining fixed-cutoff inputs are closed.

2. **Thermodynamic limit permanence**: if \(\mu_{\Lambda,\beta}\) have a limit point \(\mu_{\infty,a}\), the same decay exponent persists in the limit.

3. **OS extraction** (external theorem, used as a black box): reflection positivity + time translation invariance + Euclidean time exponential decay implies a gap for the reconstructed Hamiltonian \(H_a\):
\[
\mathrm{gap}(H_a)\ \ge\ \frac{\eta(a)}{a}.
\]

---

## 2. Reflection positivity permanence under coarse graining and projective limits

To make the passage \(\Lambda\uparrow\mathbb Z^4\) and then \(a\downarrow 0\) “structurally monotone,” the project explicitly records:

- permanence of OS reflection positivity under reflection-equivariant coarse graining,
- permanence under projective limits on cylinder observables.

This is the infrastructure that allows one to talk about a scaling limit while keeping the OS axioms visible.

---

## 3. The cleanest Clay-safe continuum statement

The Clay problem is about the **continuum** Yang–Mills theory. The project’s fixed-cutoff theorem does not automatically imply the continuum statement unless one assumes extra “continuum architecture” and “physical scaling” inputs.

A Clay-safe way to write this is:

> **Theorem (conditional continuum gap transfer).**  
> Consider a sequence of lattice spacings \(a_n\downarrow 0\) with corresponding couplings \(\beta(a_n)\) along a chosen scaling trajectory. Assume:
> 1. *(Scaling-limit existence)* The lattice measures \(\mu_{a_n}\) converge (in the project’s cylinder-observable topology) to a reflection-positive, translation-invariant Euclidean field theory \(\mu_{\mathrm{cont}}\).  
> 2. *(RP/time-translation permanence)* Reflection positivity and time-translation invariance persist along the projective system used to define the limit.  
> 3. *(Uniform physical decay rate)* The Euclidean time decay exponents satisfy
>    \[
>    \inf_{n}\frac{\eta(a_n)}{a_n}\ >\ 0.
>    \]
> Then the OS reconstruction of \(\mu_{\mathrm{cont}}\) yields a continuum Hamiltonian \(H\) with a strictly positive spectral gap:
> \[
> \mathrm{gap}(H)\ \ge\ \inf_{n}\frac{\eta(a_n)}{a_n}\ >0.
> \]

This phrasing is “Clay-safe” because:
- it clearly states the additional hypotheses (existence + permanence + scaling),
- it does not claim to have proven RG control or counterterm renormalization,
- it separates the project’s internal achievements (fixed-cutoff decay, volume-uniform estimates) from continuum construction.

---

## 4. What would upgrade the conditional theorem to an unconditional continuum theorem

One needs to close three external items (exactly as flagged in the dependency ledger):

1. **Continuum architecture / projective limit with RP:** a precise projective-limit or RG framework that preserves reflection positivity at the level needed for OS reconstruction.

2. **Hamiltonian identification:** a theorem comparing the OS Hamiltonian extracted from the scaling limit with the “physical” Yang–Mills Hamiltonian.

3. **Uniform physical scaling of \(\eta(a)\):** a mechanism (e.g., RG monotonicity or a scale-stable defect functional) ensuring \(\eta(a)\sim m_0 a\) with \(m_0>0\) along the chosen scaling trajectory.

---

## 5. Where your \(\Phi(a)\) program fits

If you can show:
- \(\Phi(a)\) is scale-stable under coarse graining, and
- \(\eta(a)\) is controlled below by \(\Phi(a)\) in lattice units,

then hypothesis (3) becomes a *measurable*, potentially provable statement:
\[
\frac{\eta(a)}{a}\ \gtrsim\ \frac{\Phi(a)}{a}.
\]

That would be a very concrete route to a continuum gap lower bound without needing to compute the exact numerical value of the gap.

---

## Sources inside this project

- OS extraction interface and explicit “Euclidean decay \(\Rightarrow\) Hamiltonian gap”: `1 Introduction.md`
- Thermodynamic limit permanence and OS structure: `## 11.1 Thermodynamic limit at fixed cutoff...`
- Reflection positivity permanence under coarse graining / projective limits: `## 12.1 Reflection positivity permanence...`
- Continuum inputs explicitly flagged as external: `PROJECT_GAP_MAP.md`, `DEPENDENCY_LEDGER(1).md`
