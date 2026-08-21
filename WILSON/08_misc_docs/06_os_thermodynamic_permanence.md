# Thermodynamic limit and OS-structure permanence (fixed cutoff)

This note extracts the project’s “bridge to physics” layer:
how a sequence of finite-volume Wilson measures yields infinite-volume limit points,
and why Osterwalder–Schrader (OS) structure (especially reflection positivity) is preserved
under the limiting procedures the project uses.

It also highlights the clean functional-analytic step:
**Euclidean-time exponential decay implies an OS Hamiltonian spectral gap**.

---

## 1. Limit points at fixed cutoff: compactness of the configuration space

At fixed lattice spacing \(a>0\), each finite-volume configuration space \(M_\Lambda=G^{E(\Lambda)}\) is compact,
and cylinder observables live in finite-dimensional marginals.

The project’s thermodynamic limit strategy is:

1. take an increasing exhaustion \(\Lambda_n\uparrow\mathbb Z^d\) (often periodic tori),
2. view \(\mu_{\Lambda_n,\beta}\) as measures on cylinder \(\sigma\)-algebras,
3. use tightness/compactness to extract weak limit points on cylinder observables.

The important point is that at fixed cutoff, no continuum measure-theoretic pathology is needed:
all objects are finite-dimensional smooth measures before taking \(n\to\infty\).

---

## 2. Permanence of OS structure under limits and coarse graining

OS reconstruction requires a package of properties: reflection positivity, translation invariance, etc.
The project emphasizes that **reflection positivity is stable** under:

- reflection-equivariant coarse graining maps, and
- projective limits on cylinder observables (i.e. consistent marginals).

This “permanence” matters because the analytic machinery (functional inequalities, clustering)
is typically proved at finite volume, while OS reconstruction is an infinite-volume statement.

---

## 3. Exponential clustering \(\Rightarrow\) OS Hamiltonian gap (spectral theorem step)

One of the cleanest moments in the project is the purely functional-analytic bridge:

If for vectors \(\psi_F\) in the OS Hilbert space one has Euclidean-time decay
\[
\langle \psi_F,\ e^{-tH}\psi_F\rangle \le C\,e^{-mt},
\]
then by the spectral theorem the spectral measure of \(H\) associated to \(\psi_F\)
cannot have support in \((0,m)\),
so \(H\) has no spectrum below \(m\) on the orthogonal complement of the vacuum.

Thus a uniform Euclidean-time exponential clustering rate gives a uniform OS gap lower bound.

The project then packages the gap in terms of the Combes–Thomas rate \(\eta(a)\) and lattice spacing:
\[
\mathrm{gap}(H)\ \ge\ m_{\mathrm{Euc}}(a) = \frac{\eta(a)c_1}{a},
\]
and in representative specializations,
\[
m_{\mathrm{OS}}(\Lambda)\ \ge\ \frac{1}{a}\log\Big(1+\frac{m^2}{2\alpha D}\Big).
\]

---

## 4. Why this matters for “new theory” potential

The OS permanence layer is not flashy, but it is what converts
“we proved a functional inequality on a finite-dimensional manifold”
into
“the reconstructed quantum theory has a true spectral gap.”

The overall architecture suggests a broader program:

> **Geometric functional inequalities \(\to\) explicit linear propagators \(\to\) exponential clustering \(\to\) OS spectral gaps**,  
> with RG as the scale-bridging mechanism to physical units.

This is a plausible template that could be applied beyond pure Yang–Mills.

---

## 5. Further work that could expand this

1. **Eliminate localization errors**: the project flags that some OS gap deductions assume the localization error is negligible or removed; making this unconditional is a major strengthening.

2. **Control of harmonic/topological modes**: in finite volume, harmonic cochains appear; a robust infinite-volume argument should clarify how these modes decouple.

3. **Continuum scaling**: combine the fixed-cutoff OS gap with the RG iteration to show a nonzero physical mass scale survives as \(a\to0\).

