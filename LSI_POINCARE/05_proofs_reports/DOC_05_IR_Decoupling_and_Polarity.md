# DOC 05 — IR Topology Decoupling and Polarity of Singular Strata

## 0. Purpose

This note extracts two project results that “clean up” the infrared:

1. **IR topology decoupling:** local observables feel a local spectral gap even if the global configuration space has slow/topological modes.
2. **Polarity:** the set of reducible (singular) connections has capacity zero, so it does not obstruct the Dirichlet form / Hamiltonian construction.

Primary project sources:
- `PROOF_08_IR_Topology_Decoupling.md`
- `PROOF_06_Continuum_Polarity.md`

## 1. IR topology decoupling from exact locality

### 1.1 Setup: local vs far variations

Fix a physical ball \(B_R\subset \mathbb{T}^4\).
On the lattice with spacing \(a\), decompose tangent directions (variations of link variables) as
\[
T_{A,a} = T^{\rm loc}_{A,a} \oplus T^{\rm far}_{A,a},
\]
where:
- \(T^{\rm loc}\): variations supported on links inside \(B_R\),
- \(T^{\rm far}\): variations supported on links at graph distance \(\ge L_a\) from \(B_R\), with \(L_a\sim 1/a\) for fixed physical separation.

### 1.2 Exact locality lemma (Hessian block diagonality)

Let \(H_a(A)\) be the Hessian of the gauge-fixed lattice action:
\[
S_a = S_a^{W} + S_a^{\rm gf}.
\]

Each term is finite-range local:
- Wilson plaquette action depends only on 4 links of each plaquette,
- gauge-fixing terms depend on a bounded neighborhood (vertex star).

**Lemma (Exact off-diagonal vanishing).**  
For \(X\in T^{\rm loc}\), \(Y\in T^{\rm far}\), and sufficiently small \(a\),
\[
\langle X, H_a(A) Y\rangle = 0.
\]

Intuition: no plaquette/star can overlap both supports once the supports are separated by more than one interaction range.

### 1.3 Local gap for local observables

Let \(F\) be a gauge-invariant local observable supported in \(B_R\). Then \(\nabla F\in T^{\rm loc}\).
If the local Hessian block satisfies a uniform positivity bound
\[
H^{\rm loc}_a \ge \rho_0\, I,
\tag{LocPos}
\]
then the inverse block obeys \((H^{\rm loc}_a)^{-1} \le \rho_0^{-1} I\) and the local Poincaré/LSI inequalities follow for such \(F\), uniformly in:
- lattice volume,
- topological sector,
- and global slow modes.

**Interpretation:** even if global topology produces flat directions, **strict locality prevents those modes from coupling into local energies for local observables.**

This is an elegant way to defuse the “torus/topology” worry without heavy global geometry.

## 2. Polarity: reducible connections have zero capacity

Let \(\Sigma\) denote the set of reducible connections (where the gauge action is not free). This is the “singular stratum” of the orbit space \(\mathcal{A}/\mathcal{G}\).

### 2.1 Capacity definition

For a Dirichlet form \(\mathcal{E}_\mu\), the capacity of a set \(S\) is
\[
\mathrm{Cap}_\mu(S)
=
\inf\Big\{
\mathcal{E}_\mu(u,u) + \|u\|_{L^2(\mu)}^2
:\ u\ge 1 \ \text{near } S
\Big\}.
\]

If \(\mathrm{Cap}_\mu(S)=0\), the set is **polar**: the associated diffusion avoids it quasi-surely, and it does not affect the quasi-regular Dirichlet form theory.

### 2.2 Stability of polarity under bounded density

The project uses a simple but powerful monotonicity:

Assume \(\mu\) is absolutely continuous w.r.t. a reference Gaussian measure \(\gamma\), with bounded density:
\[
d\mu = Z^{-1} e^{-S}\, d\gamma,\qquad 0\le e^{-S}\le 1.
\]

Then for any test function \(u\),
\[
\mathcal{E}_\mu(u,u)
=
\int |\nabla u|^2 e^{-S}\, d\gamma
\le
\int |\nabla u|^2\, d\gamma
=
\mathcal{E}_\gamma(u,u),
\]
and similarly \(\|u\|_{L^2(\mu)}\le \|u\|_{L^2(\gamma)}\).

Hence
\[
\mathrm{Cap}_\mu(\Sigma) \le \mathrm{Cap}_\gamma(\Sigma).
\]

If \(\mathrm{Cap}_\gamma(\Sigma)=0\) (true for sufficiently “thin” sets in infinite-dimensional Gaussian settings, e.g. infinite codimension submanifolds), then:
\[
\mathrm{Cap}_\mu(\Sigma)=0.
\]

### 2.3 Meaning for YM construction

- The Dirichlet form and associated diffusion/Hamiltonian are unaffected by the reducible/singular stratum.
- One can work “as if” the configuration space were a smooth manifold for the purposes of the energy form, at least quasi-surely.

## 3. What is potentially novel here?

- The IR/topology decoupling lemma is strikingly simple and robust: it relies only on **finite interaction range** and **lattice refinement**, not on delicate continuum topology.
- The polarity argument is a clean way to avoid technical disasters at singular strata, and may be reusable in other gauge-invariant infinite-dimensional settings.

## 4. Next steps

1. Make the “bounded density” assumption precise for the actual YM continuum measure relative to a chosen Gaussian reference (including renormalization issues).
2. Extend the IR decoupling logic to include more general local observables and to quantify finite-\(a\) corrections.
3. Use the decoupling to cleanly separate:
   - local gap (physical mass),
   - global topological superselection data (theta sectors, etc.).

