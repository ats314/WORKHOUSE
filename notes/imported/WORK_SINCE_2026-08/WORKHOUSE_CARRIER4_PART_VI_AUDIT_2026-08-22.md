# WORKHOUSE carrier4 Part VI — derivation audit

Date: 2026-08-22  
Scope: `carrier4.txt`, especially lines 250–295.  
Repository status: read-only; this report is external to the WORKHOUSE clone.

## Verdict

Part VI contains a valid and useful measure-theoretic core:

1. the bottom of a finite positive source measure is recovered from the large-time exponential rate;
2. the rescaled correlator decreases to the measure's atom at that bottom;
3. a cutoff-uniform lower bound on those atom weights passes to a subsequential finite-energy limit without assuming spectral isolation.

The text is **not correct as written**, however. The finite-time lower bound omits the source norm `C_a(0)`. The source must be normalized consistently across cutoffs. Time and energy must be expressed in common physical units. The limiting theorem needs vague compactness (or an explicit spectral-measure convergence hypothesis). Finally, an ordinary Hamiltonian-energy atom is not automatically a relativistic particle pole: the latter requires a fixed-momentum/joint-spectrum or Källén–Lehmann formulation.

The corrected result is therefore a **subsequential persistence theorem for a uniformly normalized carrier-visible spectral atom**. It is a genuine intermediate theorem. It does not by itself prove a stable, isolated particle.

## 1. Large-time rate and bottom atom

Let `mu` be a nonzero finite positive Borel measure on `[0,infinity)`, with finite support edge

`M = inf supp(mu)`,

and let

`C(t) = integral exp(-tE) dmu(E)`.

Then

`M = -lim_{t->infinity} t^(-1) log C(t)`.

Proof: `C(t) <= C(0) exp(-Mt)` gives the lower asymptotic bound. For every `epsilon>0`, the definition of support gives `mu([M,M+epsilon])>0`, and hence

`C(t) >= mu([M,M+epsilon]) exp[-t(M+epsilon)]`.

Taking logarithms, then `t->infinity`, and finally `epsilon->0`, proves the claim. Log-convexity is compatible with this conclusion but is not the only missing justification.

Define

`F(t) = exp(Mt) C(t) = integral exp[-t(E-M)] dmu(E)`.

The integrand is pointwise nonincreasing in `t`, so `F` is nonincreasing. Since the measure is finite, dominated convergence (equivalently, continuity from above after a standard approximation) gives

`F(t) downarrow mu({M})`.

Thus the definition

`Z = lim_{t->infinity} exp(Mt) C(t)`

is correct and `Z>0` exactly when this source measure has an atom at its own lower support edge.

Required qualifications:

- the source vector must be nonzero and finite norm, so that `mu` is nonzero and finite;
- the Hamiltonian must be semibounded and `M` finite;
- for a discrete transfer matrix, the source must not lie entirely in a zero-transfer subspace if a finite energy is claimed;
- `Z` is normalization dependent: replacing the source by `lambda_a O_a` multiplies both `C_a` and `Z_a` by `|lambda_a|^2`.

Consequently, a cutoff-uniform statement about `Z_a` requires a pinned renormalized source convention or normalization such as `C_a(0)=1`. Without that, `inf_a Z_a>0` is not invariant mathematical content.

## 2. Corrected sharp finite-time bound

Assume

`mu = Z delta_M + mu_tail`,

with `supp(mu_tail) subset [M+Delta,infinity)` and `Delta>0`. Put `q=exp(-Delta t)`. Then

`F(t) <= Z + q [C(0)-Z]`.

Therefore the sharp lower bound is

`Z >= max{0, [F(t)-q C(0)]/[1-q]}`.

If only `C(0)<=K` is known, a valid weaker bound is

`Z >= max{0, [F(t)-qK]/[1-q]}`.

If the measure is normalized by `C(0)=1`, this becomes the expression printed in Part VI:

`Z >= [F(t)-exp(-Delta t)]/[1-exp(-Delta t)]`.

The printed unnormalized formula is false. For example, take

`mu = delta_M + 9 delta_(M+Delta)` and choose `exp(-Delta t)=1/2`.

Then `Z=1`, `C(0)=10`, and `F(t)=5.5`. The printed formula incorrectly gives `Z>=10`; the corrected formula gives equality, `Z>=1`.

The corrected bound is sharp: equality holds when all tail weight lies exactly at `M+Delta`.

## 3. Corrected atom-persistence theorem

### Theorem

Let `mu_n` be finite positive Borel measures on `[0,infinity)` satisfying

1. `sup_n mu_n([0,infinity)) <= K`;
2. `M_n := inf supp(mu_n)` lies in a common compact interval `[m_-,m_+]`, with `m_->0`;
3. `mu_n({M_n}) >= z_*>0`;
4. all measures use the same physical-energy units and the same pinned source normalization.

Then every subsequence has a further subsequence for which `M_n->M` and `mu_n` converges vaguely to a finite positive measure `mu`. Every such limit satisfies

`mu({M}) >= z_*`.

If, in addition, the Laplace transforms converge for every physical time `t>0`, that convergence identifies the finite-energy vague limit. If convergence at `t=0` and an honest full spectral measure are required, add uniform energy tightness, for example

`lim_(R->infinity) sup_n mu_n([R,infinity)) = 0`,

or an equivalent uniform continuity-at-zero condition.

### Proof

After extraction, let `M_n->M` and `mu_n->mu` vaguely. For every `epsilon>0`, eventually

`M_n in [M-epsilon,M+epsilon]`.

Hence the compact interval `K_epsilon=[M-epsilon,M+epsilon] intersect [0,infinity)` contains the atom at `M_n`, and

`mu_n(K_epsilon) >= z_*`.

The compact-set Portmanteau inequality gives

`z_* <= limsup_n mu_n(K_epsilon) <= mu(K_epsilon)`.

Letting `epsilon downarrow 0` and using continuity from above yields `mu({M})>=z_*`. Similarly, every relatively compact interval strictly below `M` has zero limiting measure, so `M` remains the lower support edge of the retained finite-energy measure. QED.

If the Laplace transforms converge to the same `C(t)` for every `t>0`, the vague limit is unique because Laplace transforms determine finite measures. In that case the whole selected scaling sequence converges vaguely, not merely a further subsequence. The same uniqueness also forces `M_n` to have a single cluster point: two distinct cluster points would make the common vague limit both contain an atom at the lower one and have no support below the higher one.

### UV escape qualification

The assumptions above do not prevent unrelated norm from escaping to infinite energy. For example,

`mu_n = z delta_M + (K-z) delta_n`

has `C_n(0)=K` but `C_n(t)->z exp(-Mt)` for every `t>0`. This does not damage the surviving atom, but it shows why convergence for positive time is naturally vague rather than automatically weak at `t=0`.

## 4. What is and is not removed from the bridge

The corrected theorem genuinely removes the following from the **atom-persistence statement**:

- an empty annulus around the atom;
- control of source-dark states;
- shell multiplicity;
- spin identification.

But hypothesis 3 is still precisely a uniform nonvanishing-residue assumption. Defining `Z_a` proves that the number exists; it does not prove

`inf_a Z_a > 0`.

So the mathematical burden has been focused into one scalar target, not discharged.

There is also an important distinction between three objects:

1. an atom of a chosen source's Hamiltonian-energy measure;
2. a delta atom of its invariant-mass/Källén–Lehmann measure;
3. an isolated full-sector mass hyperboloid admitting Haag–Ruelle scattering.

The corrected theorem proves object 1 if its hypotheses are formulated for a legitimate energy measure. A relativistic particle statement needs object 2, which requires joint energy-momentum/Poincaré or Källén–Lehmann structure. Stability and isolation require object 3 and therefore reintroduce full-sector gap information.

For a local normalizable source in infinite spatial volume, even a one-particle shell normally produces a continuous **energy** distribution because momenta are integrated. A zero-momentum spatial sum is generally not a normalizable GNS vector. The rigorous continuum formulation must therefore use one of:

- finite spatial volume followed by a controlled direct-integral/fiber limit;
- a momentum-smeared joint spectral measure and then a fiber statement;
- a matrix-valued Källén–Lehmann invariant-mass measure for the carrier source family.

Only in that formulation does a surviving atom have the intended particle interpretation.

## 5. Consequences for a scaling computation

At finite time, `Z_a <= F_a(t)`. Thus a certified statement

`F_a(t) -> 0`

along the scaling sequence refutes a cutoff-uniform positive lower bound on `Z_a`.

A merely downward trend across three lattice spacings does not logically do so: the values may decrease to a positive plateau. A finite computation can refute a proposed numerical bound `Z_a>=z_*` when a controlled upper confidence bound for `F_a(t)` falls below `z_*`; it cannot refute every possible positive `z_*` from finitely many points.

Conversely, after consistent normalization, a certified tail gap `Delta_a` and the corrected sharp inequality can provide a lower bound. The required `Delta_a` is a gap in the **rest of the chosen source measure**. A gap to the next fitted `T1` level is enough only if no continuum or unobserved source-visible weight begins earlier. A full stability theorem requires the stronger full-sector gap including dark states.

## 6. The `a^9` prediction

The dimensional estimate `a^(2d-3)`, and hence `a^9` for a dimension-six carrier operator, is a useful candidate scaling law only after specifying:

- the normalization of the zero-momentum source;
- whether `Z_a` means raw atom amplitude or the normalized fraction `Z_a/C_a(0)`;
- operator mixing and multiplicative renormalization;
- anomalous logarithms;
- the fixed-physical-radius flow/smearing convention.

A fixed physical flow radius can remove the bare-source power suppression for a properly renormalized flowed source, but it does not by itself prove an `a`-independent nonzero residue. Consequently, observing `a^9` under that fully pinned flowed convention would be strong evidence against the intended smearing construction; observing a flat sequence would be consistent with survival but would not prove it.

## Final status

- **Confirmed:** the large-time support-edge formula; monotonicity of `F_a`; `Z_a=mu_a({M_a})`; subsequential persistence of uniformly weighted bottom atoms.
- **Correct after normalization:** the sharp finite-time lower bound.
- **Not derived:** `inf_a Z_a>0`; existence of a common renormalized continuum source; invariant-mass interpretation; isolation, stability, multiplicity, or spin.
- **Best honest claim:** Part VI supplies a valid intermediate carrier-visible atom theorem after the corrections above. It does not yet prove that the WORKHOUSE carrier becomes an actual stable continuum particle.
