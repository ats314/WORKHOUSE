# WORKHOUSE matrix Källén–Lehmann carrier-atom theorem

Date: 2026-08-22  
Status: proved abstract implication; model-specific hypotheses remain to be established.  
Repository status: read-only; this theorem note is external to the WORKHOUSE clone.

## 1. Purpose

The scalar large-time argument in `carrier4.txt` is naturally an energy-measure statement. A relativistic particle, however, is a joint energy–momentum object: equivalently, a nonzero spectral projection of the continuum mass operator, or a delta component of a Källén–Lehmann invariant-mass measure.

This note gives the precise matrix-valued theorem that connects the two. It also fixes three ambiguities:

1. the source is normalized at a positive physical Euclidean time, so multiplicative UV normalization cancels;
2. the cutoff measures live in a rigorously specified zero-momentum fiber (or arise as controlled finite-volume fiber limits), not from a non-normalizable infinite spatial sum;
3. the conclusion is split into a carrier-visible mass component and the stronger isolated/stable-particle conclusion.

## 2. Cutoff source and separated-time normalization

For each cutoff `a`, assume an infinite-volume, translation-covariant, reflection-positive lattice theory has been OS reconstructed. Let

`(H_a, P_a, Omega_a)`

denote its physical Hamiltonian, spatial momentum, and vacuum. Work in the required gauge-invariant, `C=-`, cubic channel. Let `J_a(p)` be an `r`-component source map into the spatial-momentum fiber `p`, defined either by direct-integral disintegration or as the controlled limit of finite-volume Fourier-normalized source maps.

All energies below are in common physical units. Thus, if the lattice transfer matrix advances one time step `a_t`, use

`H_a^phys = -a_t^(-1) log T_a`,

not the dimensionless generator `-log T_a`.

Fix a physical Euclidean time `tau_0>0`. At `p=0` define the positive Gram matrix

`G_a = J_a(0)^* exp(-2 tau_0 H_a(0)) J_a(0)`.

Assume `G_a` is invertible on the chosen source space. Define the separated-time-normalized source map

`Psi_a = exp(-tau_0 H_a(0)) J_a(0) G_a^(-1/2)`.

Then `Psi_a^* Psi_a=I_r`. Its positive matrix-valued spectral measure is

`nu_a(B) = Psi_a^* E_{H_a(0)}(B) Psi_a`,

for Borel sets `B subset [0,infinity)`. Hence

`nu_a([0,infinity))=I_r`.

This normalization is invariant under a common scalar renormalization of the source. Whitening turns an invertible source-basis change into a unitary conjugation, so atom eigenvalues/generalized residues are invariant. Entrywise matrix-moment convergence, however, requires a coherent symmetry-covariant source basis across cutoffs (or a formulation solely in terms of invariant eigenvalues and subspaces); an arbitrarily varying unitary basis can destroy entrywise convergence.

For `r=1`, `nu_a` is simply a probability measure. For the WORKHOUSE carrier, `r=3` is the minimum cubic triplet, while a spin-resolved source space should contain both `J=1` and `J=3` tensor components and therefore be larger.

## 3. Matrix atom-persistence theorem

### Theorem 3.1

Let `nu_n` be positive `r x r` matrix-valued Borel measures on `[0,infinity)` with

`nu_n([0,infinity))=I_r`.

Assume:

1. **compact physical mass location:** there are `M_n in [m_-,m_+]`, with `0<m_-<m_+<infinity`;
2. **shrinking carrier islands:** there are compact intervals `I_n` containing `M_n`, with `diam(I_n)->0`;
3. **uniform normalized carrier weight:** for some `z_*>0`,

   `nu_n(I_n) >= z_* I_r`

   in Loewner order;
4. **finite-energy measure convergence:** `nu_n` converges vaguely, entrywise, to a positive matrix-valued measure `nu`.

Then, after passage to a subsequence with `M_n->M`,

`nu({M}) >= z_* I_r`.

In particular, the limiting source measure has a rank-`r` atom at `M`. If only

`tr nu_n(I_n) >= z_*`

is assumed, then the conclusion weakens to the nonzero statement

`tr nu({M}) >= z_*`.

No spectral isolation outside the source measure, no shell multiplicity, and no spin premise is needed for this conclusion.

### Proof

Fix `v in C^r`. The scalar measures

`mu_n^v(B)=v^* nu_n(B) v`

are finite positive measures with total mass `||v||^2`. By vague convergence, `mu_n^v` converges vaguely to

`mu^v(B)=v^*nu(B)v`.

For every `epsilon>0`, for all sufficiently large `n`,

`I_n subset K_epsilon := [M-epsilon,M+epsilon] intersect [0,infinity)`.

Therefore

`mu_n^v(K_epsilon) >= z_* ||v||^2`.

The compact-set Portmanteau inequality gives

`z_* ||v||^2 <= limsup_n mu_n^v(K_epsilon) <= mu^v(K_epsilon)`.

Let `epsilon downarrow 0`. Continuity from above yields

`v^*nu({M})v >= z_*||v||^2`.

Since this holds for every `v`, `nu({M})>=z_*I_r`. The trace-only version follows by applying the same compactness argument to the positive scalar measures `tr nu_n`. QED.

### Corollary 3.2: exact bottom atoms

If each cutoff measure has an exact bottom atom

`Z_n = nu_n({M_n})`,

then Theorem 3.1 applies with `I_n={M_n}`. This is the corrected normalized form of the Carrier Atom Theorem in `carrier4.txt`.

### Corollary 3.3: convergence from Euclidean correlators

Define normalized matrix correlators

`C_n(t)=integral exp(-tE) dnu_n(E)` for `t>0`.

If `C_n(t)` converges entrywise for every fixed physical `t>0`, every vague subsequential limit has that Laplace transform. Matrix Laplace transforms determine locally finite positive matrix measures after scalarization, so the vague limit is unique. Consequently the whole selected scaling sequence converges vaguely.

Convergence for `t>0` does not exclude spectral mass escaping to infinite energy, even in the separated-time-normalized probability measures; for example, `z delta_M+(1-z)delta_n` loses the second term vaguely. Positive-time convergence determines the finite-energy vague limit. If one claims that this limiting normalized energy measure still has total mass `I_r`, add tightness or the corresponding continuity-at-zero statement. Raw-measure tightness is separately required for claims about an unnormalized `t=0` source norm.

### Theorem 3.4: compact transfer-moment form

There is a cleaner formulation that absorbs possible UV escape and is especially well suited to an exact block RG. Fix a physical block time `A>0` and put

`x=exp(-AE) in [0,1]`.

Push `nu_n` forward to a positive matrix measure `eta_n` on `[0,1]`. The point `x=0` records energy escaping to infinity. Because the source was separated-time normalized,

`eta_n([0,1])=I_r`.

Its matrix moments are the normalized block-time correlators

`C_hat_n(mA)=integral x^m deta_n(x)=Psi_n^* exp(-mA H_n) Psi_n`,

for `m=0,1,2,...`.

Assume every matrix moment converges, and assume compact carrier intervals `J_n subset (0,1]` converge in Hausdorff distance to `{x_*}`, with

`eta_n(J_n) >= z_* I_r`.

Then the measures converge weakly to a unique positive matrix probability measure `eta`, and

`eta({x_*}) >= z_*I_r`.

Proof: compactness of `[0,1]` gives weak subsequential limits. Equality of all limiting matrix moments determines the limit uniquely after scalarization because polynomials are dense in `C([0,1])`. Compact-set Portmanteau applied to shrinking neighborhoods of `x_*` transports the Loewner lower bound exactly as in Theorem 3.1.

If `x_*=exp(-AM)` with `0<M<infinity`, the atom is a finite physical-energy atom at `M`. Unlike the uncompactified energy formulation, this theorem needs no separate UV tightness condition: all escaped UV mass is retained at `x=0`, while the desired atom remains separated from zero.

For raw correlators one may write the same construction directly. Let `G_n=C_n(tau_f,0)>0` at a fixed positive physical separation `tau_f`; then

`C_hat_n(mA)=G_n^(-1/2) C_n(tau_f+mA,0) G_n^(-1/2)`.

This is identical to the definition above with `tau_f=2 tau_0`.

## 4. Källén–Lehmann promotion

Assume now that the limiting Schwinger functions satisfy the OS axioms and reconstruct a Poincaré-covariant theory. Require the fixed-radius extended source to belong to one common Euclidean/Poincaré-covariant renormalized multiplet, including the rotated/boost-related components needed for its tensor Källén–Lehmann representation, with coherent source and joint spectral convergence. Require also that its separated-time Gram matrices converge to a positive-definite continuum Gram matrix, so the whitening maps have a coherent nonsingular limit. In addition, require an exact `p=0` interface: either the spatial Fourier-transformed two-point matrices converge locally uniformly in a neighborhood of `p=0`, or a controlled Fourier-normalized finite-volume `p=0` limit is proved to coincide with the continuum `p=0` Källén–Lehmann fiber. Distributional Schwinger convergence alone does not justify evaluation at one momentum, since direct-integral fibers are defined only almost everywhere.

Let `rho(ds)` be the resulting positive matrix-valued Källén–Lehmann measure. At zero spatial momentum, with standard scalar conventions,

`C_raw(t,0) = integral_[0,infinity) exp(-sqrt(s)t)/(2 sqrt(s)) drho(s)`.

Tensor sources have the same spectral-measure conclusion after their kinematic tensor structures are separated.

Let `A` be the atom matrix of the unnormalized zero-momentum energy measure at `E=M>0`. The change of variables `s=E^2` gives

`rho({M^2}) = 2M A`,

up to the chosen Fourier normalization. The separated-time-normalized atom of Theorem 3.1 is

`Z = G^(-1/2) exp(-2 tau_0 M) A G^(-1/2)`.

Thus `Z` is nonzero if and only if `rho({M^2})` is nonzero. The lower bound in Theorem 3.1 therefore produces a nonzero spectral projection of the continuum mass operator at `M^2` in the cyclic subspace generated by the carrier source family.

### Conclusion supplied by the KL atom

Under the OS/Poincaré/source-convergence and exact-`p=0` interface hypotheses, a nonzero `rho({M^2})` proves a carrier-visible mass-`M` Poincaré/Wigner component. Charge conjugation and parity label that component if those symmetries survive the limit and the source transforms covariantly.

### Conclusions not supplied by the KL atom alone

The theorem does not prove:

- that the mass hyperboloid is isolated from the complete joint spectrum;
- that source-dark states do not accumulate at the same invariant mass;
- Haag–Ruelle scattering or asymptotic completeness;
- multiplicity one;
- `J=1` rather than `J=3` or a mixture.

Those statements require additional full-sector and symmetry information. In particular, Haag–Ruelle stability by the current WORKHOUSE route requires a true invariant-mass annulus/tubular gap around the complete shell.

## 5. Spin firewall

The raw continuum limit of the diagonal carrier source has the tensor decomposition

`S_iii = H_iii^(J=3) + (3/5) V_i^(J=1)`.

Accordingly, a positive `3 x 3` `T1` atom only proves that the raw source family sees some mass component whose restriction contains `T1`. It does not identify spin. A spin theorem must use either:

1. a pure axial source `V_i=S_ijj` with positive KL atom and an SO(3)-covariant residue;
2. the full traceless `H_ijk` multiplet and its `A2+T1+T2` partners; or
3. complete full-sector fiber rank plus restored rotations.

A complete three-dimensional irreducible rest fiber with restored SO(3) forces `J=1`. A nonzero `J=3` atom requires a seven-dimensional `A2+T1+T2` completion.

## 6. Exact remaining model-specific target

For carrier-visible continuum particle existence, the abstract theorem reduces the source part of the bridge to the following concrete statement:

> For a fixed physical flow radius and fixed `tau_0>0`, construct the same normalized gauge-invariant `C=-` source family at every cutoff, construct its zero-momentum fiber measures `nu_a`, and prove that there are shrinking physical-mass intervals `I_a` and constants `m_-,m_+,z_*>0`, independent of `a`, such that
>
> `I_a subset [m_-,m_+]` and `nu_a(I_a) >= z_* I`.

The fixed-spacing CMP theorem proves the analogue for the complete three-source Riesz island in its small-`u` domain. It does not yet prove this estimate along the weak-coupling continuum scaling trajectory. An exact RG/OS source intertwiner could transport it without loss; an approximate RG route must prove transfer-entry and source-entry errors small enough to preserve the lower bound.

Full isolation is not a premise of Theorem 3.1. It remains a separate requirement only for the stronger stable-isolated-particle conclusion.

## 7. Logical status

- **Proved here:** matrix atom compactness; separated-time normalization; KL promotion under OS/Poincaré/coherent-source convergence plus the stated exact-`p=0` interface.
- **Proved at fixed small `u` by the audited CMP package:** a positive-definite full-island frame/residue for the literal Wilson source.
- **Not yet supplied by the corpus:** a cutoff-uniform normalized carrier island along the continuum scaling trajectory, or an exact/controlled RG source intertwiner that transports the CMP island there.
- **Separate after existence:** full-sector isolation, Haag–Ruelle stability, multiplicity, and spin.
