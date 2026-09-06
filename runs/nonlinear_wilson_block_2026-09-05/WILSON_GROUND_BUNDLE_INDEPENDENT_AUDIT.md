# Independent audit of the actual Wilson ground-bundle form

5 September 2026. Read-only mathematical and control review of
`NEAR_IDENTITY_WILSON_GROUND_BUNDLE.md`, final proof SHA256
`2f4078c123f039feb8b50657faae93cf846663b07bda67b3c869bd3edca2ab32`.
No canonical or sealed source is changed by this audit.

**Accepted at the stated finite-block, fixed-rank and near-identity scope.**
The proof supplies an actual relative O(g^2) magnetic-form estimate after
compression to the conditional quantum ground bundle. It does not supply the
full-vacuum fast compression or an OS reducing range.

The required scalar subtraction is explicit: the differentiated operator is
`H_U=A_U-V_c(U)`, with `V_c=4u(N-ReTr sqrt(U))`. The unshifted derivative
would contain an O(u|X|) scalar, so using its bare norm in the reduced-resolvent
estimate would fail. That failure is avoided, while the full scalar is restored
in the final projected form.

The common-domain argument is sound. The bi-invariant Casimir commutes with all
fiber Lie derivatives and with the anisotropic constant-coefficient kinetic
operator. Peter-Weyl decomposition therefore justifies both
`||L psi||<=k^-1||T_U psi||` and
`sum_ab||D_a D_b psi||^2=||L psi||^2`. The exact Haar integration-by-parts
identity bounds the potential/kinetic cross term below by `-Cu||psi||^2`.
It gives the stated graph norm with sqrt(u), rather than an uncontrolled
u-dependent elliptic constant.

The even balanced coefficients have first derivatives O(|X|) and bounded
second derivatives. Relative potential bounds use positivity under the trace,
so they remain valid without commutativity. The established full conditional
gap on a fixed coarse neighborhood is of order sqrt(u). Applying its reduced
resolvent to the centered differentiated eigen-equation gives
`||Omega_i||<=C|X|`. A second differentiation, retaining the normalization
component and controlling `H_i Omega_j` through the common graph domain,
gives `||Omega_ij||<=C`. All displayed products have justified domains.

The horizontal lift is the actual original-link metric lift. Direct rational
algebra verifies its two residual factors and the coefficients 1/8 and 7/24.
The residual is O(|X|), while a fiber derivative of the ground is O(u^(1/4));
therefore the intrinsic derivative and Born-Huang energy have the stated
`u^(1/4)|X|` and `sqrt(u)v(U)` bounds. The proof correctly does not identify
bounded balanced second derivatives with bounded intrinsic second derivatives.

The Haar-skew sign and half-density correction are correct. Positivity and real
normalization make the Berry term exactly zero. Substitution into the completed
horizontal-plus-vertical form gives the exact identity

```
q_full[J psi]=q_c[psi]+integral(V_c+e(U)+Phi_BH)|psi|^2.
```

Both `e(U)-e(I)` and the Born-Huang term are bounded in absolute value by
`C u^-1/2 V_c`. The resulting two-sided form comparison retains the actual
coarse Haar measure and kinetic metric and has no discarded additive error per
block. It closes on the stated Dirichlet chart. Its tensor extension has the
same relative constant only for additive disjoint-edge copies; a shared residual
Gauss constraint preserves the inequality but creates no omitted ambient
interactions.

The global vertical barrier is complementary, not a premise for the local
derivative proof. It does not turn the global conditional gap into sqrt(u): at
SU(2), U=-I has the exact order-one conditional gaps recorded in the companion
audit. Global patching, horizontal/off-diagonal memory, true full-vacuum
subtraction, literal/OS source matching and uniform interacting-block control
remain actual proof obligations.

The finite `check_ground_bundle_geometry.py` source was inspected and its
`controls()` function was independently replayed without writing to its files.
The payload exactly matches the saved JSON and all source bytes are unchanged.
The checks verify rational Schur/lift formulas, matching first coefficients,
evenness and one noncommuting spin-one Casimir/graph estimate. They do not
certify the uniform analytic theorem. Frozen SHA256 values are:

- Script: `d6846e21ad0bb0d0e5c9527df0b615bb2a5bb446a4fa278395924abd51137c76`.
- JSON: `bce312748d3b04602d00c2ec6a5f954b4986e760906f5725fa9f812507256524`.
