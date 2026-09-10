# W6 continuation: actual square block and full inverse-energy control

The next calculation has been carried through the actual twelve-edge
2x2 plaquette block. It produces a nonzero complete first force and a
sharp inverse-energy estimate for all retained radial states.

## What the strip verification opened

The three-plaquette calculation established that the complete first
transported operator vanishes on physical states even though its electric
and source corrections separately do not. The exact index identity extends
to every finite open strip. This discharged the strip first-order
obligation and directed the calculation to the first block with two spatial
directions: the 2x2 square.

The strip proof and checks are in
`../w6_three_strip_20260909/geometry.md`, `source.md`, and `graph.md`.
In particular the nonreducing Gaussian graph on the three-strip was
retained. Its cancellation was not inferred from replacing that graph
by the source injection.

## The square gives an actual nonzero force

For the two middle holonomy vectors X0,X1 and the two top holonomy vectors
X2,X3, put Tijk=Xi.(Xj cross Xk) and a=|X2+X3|^2/2. The complete result is

\[
\boxed{t_1\varphi=\frac{\sqrt2-4}{7}
(T_{023}+T_{123})\varphi'(a).}
\]

This includes the original shared-edge electric operator, the coupled
Gaussian ground correction, the literal outer observation and its true
marginal, and an explicit full source-compatible unitary generator.
The coefficient of the second radial derivative cancels exactly.

The Gaussian outer source reduces the square's reference operator.
Thus its exact reference graph is the source inclusion. The force has
one retained oscillator excitation and two fast excitations. Its full
inverse denominator contains all three energies.

## Sharp bound, with no radial-energy cutoff

With the retained reference form b, the exact constant is

\[
\boxed{\langle t_1\varphi,F_0^{-1}t_1\varphi\rangle
\le\frac{(4-\sqrt2)^3}{1372}\,b[\varphi].}
\]

The constant is approximately 0.012601546560747265. It is attained by
the first centered radial excitation a-3sqrt(2). The proof applies to
every radial finite-energy state by spectral truncation, not just to
the finite polynomial checks. See `inverse_synthesis.md` for the exact
factorization and proof.

For the first excitation the inverse image is explicitly

\[
u_0=F_0^{-1}t_1\varphi_1
=\frac{\sqrt2-4}{7(4+\sqrt2)}(T_{023}+T_{123}),
\]

and its inverse energy is (528sqrt(2)-600)/343.

## Complete defect insertion and all-source bound

The next W6 operation has also been completed:
\(\rho_1=QW_1F_0^{-1}t_1\varphi\), with
\(W_1=H_1+[H_0,K]\) and the explicit complete source generator in
`source.md`. It includes all terms of the original coupled operator.
Independent original-coordinate differentiation verifies the full
radial formula used in the norm calculation.

For every retained radial finite-energy state,

\[
\boxed{\|\rho_1\varphi\|^2\le K_{\rm res}b[\varphi],
\quad K_{\rm res}=0.0037824649150914063\ldots<\frac1{256},}
\]
\[
\boxed{\langle\rho_1\varphi,F_0^{-1}\rho_1\varphi\rangle
\le\frac1{512}b[\varphi],\qquad
\langle u_0,W_1u_0\rangle=0.}
\]

The all-source proof keeps the full horizontal inverse before estimating
the residual. The second radial derivative cancels; an exact Gaussian
moment identity and radial integration by parts then give the bound.
The first diagonal coefficient vanishes by parity. See
`residual_inverse.md` and the independent derivation
`residual_all_energy.md`.

For the first radial excitation the complete residual has 66 Hermite
components in degrees two and four, including the fourth Gaussian mode.
Its full inverse energy is 0.0108488157709989641..., or
0.0003196362999798721... times its retained energy. This exact finite
calculation independently agrees with the all-source moment identity.

## Actual finite-g quantum coercivity

The compact square's magnetic potential has a unique minimum and its
original-edge electric form is uniformly elliptic. Rescaled localization,
compactness and quantum min-max prove convergence of its first physical
gap to 2sqrt(2), including subtraction of the true quantum ground.
Consequently, for some fixed-block threshold g_*>0,

\[
\boxed{F_g\ge2I\quad(0<|g|<g_*).}
\]

This is the full physical conditional compression of the actual compact
operator. Equivalently, its actual quantum ground measure satisfies the
full-edge Poincare inequality on conditionally centered physical states.
The proof is in `finite_g_quantum_floor.md`.

Combining that actual floor with the established L2 coefficient estimate
also proves, under any unitary fast-space identification,

\[
\boxed{\langle g\rho_1\varphi,A_g^{-1}g\rho_1\varphi\rangle
\le\frac{g^2}{512}b[\varphi],}
\]

where A_g is the actual interacting fast operator in that identification.
This controls the computed leading residual component with the
interacting inverse, without an upper or near-unit lower Gaussian form
comparison.

## Finite-g source domain and precise remaining comparison

The exact Gaussian quantile source transport is globally isometric, but
does not preserve the whole Gaussian energy domain. The explicit centered
source

\[
p(a)=\sqrt{2/3}\left[e^{a/(8\sqrt2)}-(4/3)^{3/2}\right]
\]

has b0[p]=1 and infinite compact source energy after that transport for
every fixed g>0. This is proved from the actual smooth positive quantum
marginal's endpoint asymptotics in `finite_g_source_domain.md`.

The same note constructs a compact Haar quantile source identification
with the fixed weighted domain
\(\int_{-1}^1(1-w^2)|f'(w)|^2d\mu_H(w)<\infty\).
Its full source-compatible unitary preserves the physical H1 form domain
on every closed positive-coupling interval. A dense common core is also
supplied if the original Gaussian normalization is retained.

The remaining comparison is explicit: bound the **complete finite-g
residual**, beyond its computed first coefficient, in the actual
interacting dual norm on that admissible core, then justify its closure
in the stated source norm. Replacing the Gaussian source norm by the
compact transported norm changes the target and must be stated.
The fixed-square floor is discharged; a uniform residual remainder and
uniformity over coupled growing volumes are not established by these
fixed-block calculations.

## Reproducible evidence

`geometry.md` derives the original twelve-edge operator and exact outer
trace carré du champ. `source.md` constructs the full source-compatible
unitary and proves the specific cubic obstruction to the strip normal
form. `graph.md` computes the full cubic inverse. `inverse_synthesis.md`
proves the sharp first-force theorem. The residual, quantum-floor and
source-domain proofs are linked above.

Independent executable controls are `verify_square_geometry.py`,
`verify_complete_force_geometry.py`, `verify_source.py`,
`verify_graph.py`, and `verify_inverse_synthesis.py`, with their
corresponding JSON records. They check exact operator and polynomial
identities; the all-energy conclusion uses the analytic proof as well.
`provenance.json` records the complete current control inventory and
source hashes. These analytic results are not claimed as Lean proofs.
