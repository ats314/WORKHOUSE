# Independent audit: tagged literal sources and complete physical range

5 September 2026. Scope: Sections 2–3 of `LITERAL_SOURCE_FRAME.md`, the
source-sector interpretation, and the previously proved onto bridge.
No canonical files changed.

**Accepted.** The tagged estimate controls the complete synthesis operator
on square-summable plaquette coefficients. Its constants and its
infinite-dimensional completeness step are valid under the explicitly
retained calibrated physical-window and actual-transfer inputs. The new
argument does not replace those inputs with a one-link gap or a finite
matrix experiment.

## 1. Inputs checked against the pinned proofs

The two proof files match their existing `paper/SHA256SUMS` entries:

- `G18_WILSON_CARDINALITY_UNITARY_CHART_20260905.md`:
  `15ae9409d96220d41c6cf9c77ce7a294bc2760a586d2e0a245235fd02e6e908f`.
- `G18_WILSON_WEIGHTED_ACTIVITY_BOUND_20260905.md`:
  `45458b4e3666f82563c05c797271e546defe3407ab2e3e16c8620c6b97bdfbb0`.

The chart supplies assigned connected plaquette footprints, its uniform
interaction norm at `rho_plus=1+log(2)`, the generator's symmetry
covariance, the correct time-reversed inverse evolution, and local
operator-norm convergence of both conjugations. The activity proof
supplies `G<=E<=(568/145)q`, the common value `q<=1/10000` at `u0`, the
actual subsystem Perron normalization and the full transfer norm error
`epsilon<=1/998`. Both notes retain the physical free-window premise
separately from their abstract tensor estimates.

## 2. The tagged commutator estimate has the required incidence factors

Let `s_X=exp(rho|X|)||S_X||` and
`a_(p,Y)=exp(rho|Y|)||A_(p,Y)||`. A commutator has support label
`X union Y`, requires `X intersect Y` nonempty, and retains the original
source tag p. Since rho is nonnegative,

    exp(rho|X union Y|) <= exp(rho|X|)exp(rho|Y|).

For a fixed output root i, split the union-root indicator by
`1_(i in X union Y)<=1_(i in X)+1_(i in Y)`. The first part is at most

    2 sum_(X contains i) s_X
         sum_(p,Y intersects X) a_(p,Y)
      <= 2 m_i(S;rho) ||A||_rho^tag.

The second is at most

    2 sum_(p,Y contains i) a_(p,Y)
         sum_(X intersects Y) s_X
      <= 2 g(s) m_i(A;rho).

Thus the tag adds neither an unbounded source-count factor nor a lost
cardinality factor. The decreasing weight `rho'=-2g` cancels the second
term root by root. The half-unit weight reserve gives
`M1(S;rho)<=2g/e<=g`. With the inhomogeneous four-link initial sources,
`M1(C0)=4||C0||` in the corresponding rooted bound. Hence

    D^+ ||A||^tag <= 2g ||A||^tag +10g C_*,
    C_*=4 exp(4rho0)c_N=64 e^2 c_N.

Integrating yields exactly the stated
`D<=640 e^2 c_N G exp(2G)` at weight log(2). All final supports retain
the original four-link anchor. Finite tagged truncations justify the
Dini estimate; the positive uniform majorant permits their removal.

## 3. Termwise centering and the Gram–Schur step are valid

Charge conjugation here is the unitary pullback on link wavefunctions,
not scalar complex conjugation as an antiunitary map. Each magnetic
plaquette interaction is even under it, the vacuum and exact-support
projections are invariant, and uniqueness of creator-velocity inversion
preserves this symmetry for every assigned generator coefficient.
Thus each iterated tagged commutator of the odd literal source is odd.
The product vacuum on its assigned support is invariant, so its local
expectation vanishes separately. No cancellation between different
support labels is being assumed.

For disjoint Y,Z, the product Hilbert-space inner product of the two
centered local vectors factorizes into their zero vacuum expectations.
The overlap restriction in the Gram row estimate is therefore exact.
The two norm conversions are also correct:

    sup_i sum_(q,Z contains i)||f_(q,Z)|| <= D/16,
    sum_Y |Y| ||f_(p,Y)|| <= D/4.

The first uses `|Z|>=4`; the second uses a fixed anchor link of p and
`n 2^(-n)<=1/4` for `n>=4`. Consequently

    sum_q |<F_p,F_q>| <= (D/16) sum_Y |Y|||f_(p,Y)|| <= D^2/64.

Hermiticity supplies the column bound. Schur therefore controls the
entire error synthesis by `D/8`, rather than each column separately.
The same bound on all finite coefficient sequences, followed by the
established local source limits, gives the infinite synthesis operator.

## 4. Constants and completeness

On `|u|<=u0/(8N)`, the arithmetic is

    N G <= 71/1450000 < 1/20000,
    ||J-J0|| <=2160 N G
              <=1917/18125 <27/250 <1/8.

The coarse factors `e^2<9`, `sqrt(2)<3/2`, `exp(2G)<2` have the right
direction and are valid on the stated regime. The additional interval
depends on fixed rank N, as the source norm requires, and remains
independent of volume and temporal mesh.

The onto proof in Section 4 is valid: its coefficient operator has a
Neumann inverse, and a vector in the target projection range killed by
J0* must vanish because the two projections are norm-close by less than
one. It does not infer surjectivity from coercivity alone.

The stronger independently derived Sylvester/direct-rotation bridge may
replace its weaker constants without changing the source estimate:

    delta<=epsilon/(g_star-epsilon)<=1/9,
    minimum singular value(Pi J)>=559/648,
    J*Pi J >=312481/419904 I >9/16 I,
    ||(Pi J)^(-1)||<=648/559<6/5.

## 5. Actual physical and Euclidean identification

The normalized literal source is gauge invariant, center neutral and
charge odd. Its free vectors are the complete orthonormal plaquette
shell only under the retained calibrated physical-window theorem;
this is correctly stated as an input. The unique symmetric chart
preserves those sectors, so the transported source columns lie in the
same physical odd Hilbert space as the transfer projection.

The parallel `INFINITE_TRANSFER_AND_PHYSICAL_BAND.md` supplies a common
product Hilbert-space operator limit and passes the full physical free
window to its closed sector. Its joint local-observable/transfer-moment
identification is the needed connection to the actual Wilson GNS
transfer, not just a vacuum-state comparison.

For the Euclidean multiplication-history representation, that note
correctly avoids assuming equal-time multiplication is cyclic on the
whole quantum Hilbert space. Its reducing history space contains every
literal source and therefore every projected literal source by bounded
functional calculus. Since the source theorem maps onto the complete
Riesz range, this entire band lies in that representation. The converse
inclusion follows from reduction. This supplies the precise physical
cyclicity required for the band.

No issue requiring a repair was found in the tagged estimate, Gram–Schur
argument, or source-completeness application. The result remains a
fixed-spacing, admitted calibrated-mesh strong-coupling theorem. It does
not itself supply temporal Hamiltonian matching or a spatial continuum
limit; the proof notes already keep those later assertions separate.
