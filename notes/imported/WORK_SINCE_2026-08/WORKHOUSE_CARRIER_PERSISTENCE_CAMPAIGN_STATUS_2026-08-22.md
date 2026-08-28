# WORKHOUSE carrier-persistence campaign: audited status

**Date:** 2026-08-22  
**Mode:** WORKHOUSE repository read-only  
**Purpose:** record what has been proved, what remains conditional, and the precise point at which the carrier-to-continuum-particle argument presently stops.

For the concise theorem chain, see
[`WORKHOUSE_FIXED_SPACING_PROOF_CHAIN_AND_STOPPING_POINT_2026-08-22.md`](./WORKHOUSE_FIXED_SPACING_PROOF_CHAIN_AND_STOPPING_POINT_2026-08-22.md).

## Bottom line

The campaign made real progress at fixed lattice spacing, but the proposed reduction in *The Carrier Persistence Problem* does **not** turn the continuum bridge into one correlator-ratio estimate.

The decisive distinction is:

- a nonzero fixed-time correlator ratio proves that some normalized source weight remains at finite energy;
- an actual particle requires a nonzero **atom on an isolated invariant-mass shell**, plus joint energy-momentum/OS convergence;
- those two statements are not equivalent.

The fixed-spacing route has now been completed externally through the literal
Wilson source. The cleanest current stopping point is a uniform
source-carrying invariant-mass island along the continuum scaling limit. That
continuum step is genuinely open constructive four-dimensional Yang–Mills
work.

## Status by milestone

### 1. Exact electric-shell theorem — completed externally

For every periodic cubic lattice with `L >= 3`, in the gauge-invariant, charge-odd, neutral one-form-charge block,

\[
\mathbf 1_{(-\infty,4)}(H_{0,L})=P_{1,-},
\qquad \operatorname{rank}P_{1,-}=3L^3,
\]

and the shell energy is `8/3`. The complement begins exactly at `4`, so the electric gap is sharply `4/3`. For `L >= 6`, the same strict sub-4 classification does not require the center restriction.

This is supported by a self-contained proof and an independently rerunnable finite certificate. It has not been inserted into WORKHOUSE because the repository is read-only.

### 2. Uniform finite-volume Riesz patch — external proof transport completed

The exact cell regrouping gives:

- three outgoing links per product cell;
- gap-one rescaling by `3/2`;
- exact bundled interaction norm `epsilon(u)=27|u|`;
- bundled interaction support on four cells;
- plaquette excitation support on three grouped cells;
- conservative kinematic patch-separation ratio `1/33`.

With Yarotsky constants `c1,c2`, the sufficient existential domain is

\[
27|u|<c_1,
\qquad 27c_2|u|<\frac1{33}.
\]

In this domain, the desired restricted patch has rank `3L^3` along the entire
segment from `0` to `u`. The external import note supplies the periodic
finite-quotient hypergraph argument: bounded support, bounded incidence, and
rooted connected-set counting remain uniform in the torus size. This is a
derived proof transport, not a verbatim numbered theorem in Yarotsky. A
publication should typeset that finite-quotient rerun explicitly rather than
cite it as a black box. No numerical coupling threshold is certified because
`c1,c2` are existential.

### 3. Infinite-volume fixed-spacing lattice quasiparticle — CMP(1)–CMP(4) completed

The totality/no-dark-states step follows from Yarotsky's published unweighted
coefficient estimate and a Banach close-projection argument. The rooted form
of the same estimate, local product-vacuum continuity, and Yarotsky's
correlation bound then give an exponentially summable block Gram kernel and
a uniform frame. Consequently the physical charge-odd Riesz space is exactly

\[
\ell^2(\mathbb Z^3)\otimes\mathbb C^3,
\]

with an exponentially local `3 x 3` translation-invariant Hamiltonian, an
analytic Bloch matrix, and a true external gap inside the physical charge-odd
sector.

CMP(4) transfers the canonical frame to the literal Wilson multiplication
source without a new BCH expansion. The difference operator annihilates the
product vacuum; local continuity controls contact terms and clustering
controls the spatial tail. If `T_c` is the canonical source map,
`T_D` the projected difference, `G=T_c^*T_c`, and `C=T_c^*T_D`, then

\[
T_W=T_c\bigl(I+G^{-1}C\bigr),
\]

and the second factor is invertible in an exponentially weighted convolution
algebra for sufficiently small `u`. Thus the complete three-source Wilson
family has a positive-definite spectral-projection weight at every lattice
momentum. This is an isolated fixed-spacing lattice quasiparticle band—not a
relativistic continuum particle.

### 4. Continuum descendant — genuinely unresolved

Small `u` is strong coupling, while the Hamiltonian continuum direction is `u -> infinity`. No analytic continuation presently connects the fixed-spacing patch to that limit.

The required continuum-side statement remains a uniform source-carrying invariant-mass-island theorem. Along a reflection-positive scaling sequence, one must control in physical units:

- a finite nonzero limiting mass;
- a nonzero normalized source weight in shrinking invariant-mass tubes;
- a true empty invariant-mass annulus in the full symmetry sector, including states dark to the chosen source;
- convergence of the joint energy-momentum spectral data and the OS Schwinger family;
- full shell multiplicity and restored rotations for spin identification.

Once these hold, pole persistence, OS reconstruction, and Haag–Ruelle supply the standard final particle theorem. They are not consequences of the finite-order WORKHOUSE coefficients.

## Audit of *The Carrier Persistence Problem*

### What survives

Several observations are useful and should be retained:

1. For a positive normalized energy measure,

   \[
   \frac{C(t)}{C(0)}=\int e^{-tE}\,d\mu(E),
   \qquad
   \inf\operatorname{supp}\mu
   \le \frac1t\log\frac{C(0)}{C(t)}.
   \]

   Thus a noncollapsing fixed-time ratio prevents all normalized source weight from escaping to infinite energy.

2. Exact charge conjugation removes the vacuum/disconnected term and gives a valid superselection decomposition.

3. A source at fixed physical radius is the right numerical object. A bare shrinking plaquette can lose useful overlap even when a physical state exists.

4. The `L^-2` internal spacing is naturally interpreted as momentum spacing within a dispersive cluster. It blocks a volume-uniform contour around one internal sheet, but not a contour around the complete externally isolated cluster.

5. The bare diagonal continuum tensor contains both `J=1` and `J=3` operator components. The exact `3/5 : 2/5` split is a kinematic tensor-norm decomposition, **not** a `60% : 40%` split of spectral residues or particle couplings.

6. The reported internal mass ratio near `6.43` is a useful numerical consistency check against the modern `1^{+-}` value near `6.065`, but it is not residue evidence. The covariance needed for the ratio error is absent, the raw ground fraction is consistent with zero, and the fitted amplitude is explicitly not a normalized overlap probability.

### The fatal error in the proposed one-ratio theorem

Hypotheses `(C),(S),(O),(D)` do not imply an isolated particle. Two counterexamples settle this.

#### Counterexample A: positive ratio with no particle atom

Let the normalized charge-odd source measure be absolutely continuous on `[M,M+1]`:

\[
d\mu(E)=\mathbf 1_{[M,M+1]}(E)\,dE.
\]

It has a positive fixed-time ratio, bottom `M`, a mass gap above the vacuum, exact charge conjugation, and no accumulation of discrete masses because it has no discrete masses at all. Yet it has no atom, no isolated mass shell, and no one-particle state.

The same example can be realized within an OS-positive generalized-free-field framework using a continuous positive Kallen-Lehmann density.

#### Counterexample B: ratio survives while the desired residue vanishes

Let

\[
\mu_a=\varepsilon_a\delta_M+(1-\varepsilon_a)\delta_{M+\Delta},
\qquad \varepsilon_a\to0.
\]

At every cutoff the desired atom at `M` exists and is isolated. Nevertheless,

\[
\frac{C_a(t)}{C_a(0)}
\longrightarrow e^{-(M+\Delta)t}>0,
\]

while the residue of the `M` atom tends to zero. Therefore a nonzero one-time ratio does not preserve the target pole.

The filtering inequality in the note is algebraically correct only after one assumes a nonzero bottom atom, a gap, and a controlled rest-to-pole weight ratio. Those are precisely the missing spectral inputs; the inequality cannot generate them.

### Why charge conjugation does not supply isolation

Charge conjugation is a selection rule, not a particle theorem. It does not prove:

- that the bottom of the charge-odd spectrum is attained by an atom;
- that an isolated charge-odd particle or a lightest `0++` particle exists;
- that Haag–Ruelle scattering states have already been constructed;
- that the continuum threshold equals `M_{C-}+m_{0++}`;
- that no continuous or bound-state spectrum begins at the same mass.

The Clay mass gap isolates the vacuum. It does not supply the additional "upper gap" around an excited one-particle shell. The official Jaffe–Witten statement explicitly lists existence of an isolated one-particle state as a further extension beyond the mass-gap problem.

Numerically, `2m_{0++}=6.810 sqrt(sigma)` is a charge-even two-particle threshold. A conjectural charge-odd two-particle threshold would instead be `M_{1+-}+m_{0++}=9.470 sqrt(sigma)`, and even that identification presupposes the relevant particles and scattering structure.

### Correct use of the ratio

After separately proving convergence and identification of normalized continuum source measures, a lower bound `C_a(t)/C_a(0) >= c > 0` implies nonzero finite-energy source weight and an upper bound on the source support edge. More quantitatively, if `e^{-tR}<c`, then

\[
\mu_a([0,R])
\ge
\frac{c-e^{-tR}}{1-e^{-tR}}.
\]

That is a valuable tightness/falsifier estimate. It is not pole persistence.

If an atom at `M` and an empty gap through `M+Delta` have already been established, then a ratio can lower-bound its weight:

\[
z\ge
\frac{r(t)-e^{-(M+\Delta)t}}
     {e^{-Mt}-e^{-(M+\Delta)t}},
\]

when the numerator is positive. This is a useful final estimate, but it assumes the very atom and gap that the proposed reduction tried to eliminate.

## PMBSF assessment

PMBSF is a potentially useful technical reference, not an already available carrier proof.

- Equation `(14.37)` appears under **Open Theorem C** and states a desired upper bound; its acceptance criteria are explicitly future work.
- The current canonical PMBSF line no longer treats that source-weighted expansion as load-bearing after a positivity-based reformulation.
- PMBSF's sources are nonnegative SU(2) rare-defect ramps or indicators and use positive real tilts.
- The WORKHOUSE carrier is a signed, charge-odd SU(3) source. In SU(2), charge conjugation is gauge-trivial and the relevant `C=-` carrier sector is absent.
- Absolute upper bounds on marked activities can aid convergence and clustering, but cannot prove the required lower residue bound, exclude cancellations, or create a spectral atom.
- PMBSF itself says that infinite volume, continuum scaling, OS reconstruction, a physical mass gap, and uniform scaling constants remain outside its closure.

The claimed inventory of `238` unread continuum notes is unsupported by the corpus audit. It appears to conflate unmatched simulation notebooks with a separate research-summary backlog. Those files may still contain useful leads, but their count is not evidence of an unreviewed continuum proof reserve.

## Spin firewall

The existence theorem and spin theorem should remain separate.

For the leading continuum tensor,

\[
S_{iii}=H_{iii}+\frac35V_i,
\qquad V_i=S_{ijj},
\]

where `V` is `J=1` and the symmetric-traceless `H` is `J=3`. The raw diagonal carrier is one cubic `T1` triplet embedded across both continuum components.

A proof of a stable massive charge-odd particle does not require resolving this mixture. To prove specifically `J=1`, either:

1. construct a renormalized axial source `V_i` with nonzero shell residue; or
2. prove that the complete restored-rotation mass-shell fiber has dimension exactly three.

A `J=3` endpoint requires the `A2 + T1 + T2` partner structure. At finite spacing, absence of degenerate `A2/T2` partners does not by itself prove `J=1`; the criterion becomes decisive only as rotations are restored.

## GPU decision

No GPU is needed for the analytic conclusions above.

The A100 would be useful for a **falsification and orientation campaign**, not a proof:

- at least three lattice spacings and controlled physical volumes;
- a fixed physical flow/smearing radius;
- a variational source basis containing clean `V_{T1}`, `H_{T1}`, `H_{A2}`, and `H_{T2}` operators;
- correlated estimates of the normalized spectral weights and masses;
- scaling tests for the source ratio, residue, `A2/T2` partner pattern, and finite-volume thresholds.

The A100 is the preferable first target for this workload. The local 7900 XTX may be useful after the code path is known to support it, but software support is more likely to become the bottleneck than raw arithmetic.

Such a run can kill a bad carrier hypothesis early or identify the correct spin branch. It cannot replace the uniform invariant-mass and OS theorem.

## Precise handoff choices

The project now has three honest next directions:

1. **Close the fixed-spacing composite theorem.** Prove the six rooted/composite estimates listed in Milestone 3. This is the strongest rigorous next step and appears feasible without new physics assumptions.
2. **Run the A100 scaling diagnostic.** Build the spin-resolved fixed-radius source basis and measure whether the normalized carrier weight and partner pattern improve or collapse toward the continuum.
3. **Begin the continuum constructive program.** Formulate and attack the source-carrying invariant-mass-island theorem directly. This is the scientifically decisive route, but it is also the least presently tractable and is comparable in difficulty to the unresolved constructive 4D Yang–Mills problem.

The recommended order is `1`, then `2`, using the results to decide whether the very expensive direction `3` is justified.

## Integrity statement

No file in the WORKHOUSE repository was created, modified, or deleted during this campaign. All deliverables were written outside the read-only clone under `outputs/`.
