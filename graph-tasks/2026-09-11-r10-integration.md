# R10 repair: independent re-review — 2026-09-11

Owner: Claude (Fable 5.1). State: review complete; R10 remains open.
Reviewed: the R10 repair (abb3942, Codex) as merged into main by PR 150 (merge bc9da02),
docs/derivations/w6-source-energy-jets-r10.md.
Targets: DERIV:W6_GROUND_JETS_TRANSPORT_BUDGET:SOURCE_ENERGY_JETS_R10 and the SF9 hypotheses
H0-H4 of docs/derivations/w6-source-generator-score-frame.md.

An earlier Codex review (navigation/tasks/2026-09-11-r10-pr150-review.md) rejected the
original submission 88e4d82. This record reviews the repair that replaced it.

## Re-review

Checked by hand against the established inputs on main:

- C1 (conditional derivative with the covariance term) follows from SF7d applied to X and
  Phi X; the exact counterexample to the frozen-measure shortcut is correct.
- C3 (sufficient horizontal-score criterion): |X(Phi)|^2 <= Gamma(Phi,Phi)/(2a), the Young
  split, and g^2 integral Gamma(Phi,Phi) dmu_g = 2 L_g[Omega_g Phi] give
  b_g[Pi_g Phi] <= (2 + 2C_B/gamma) q_g[Omega_g Phi] under C3a. Sufficient only.
- C4 (H0 plus R8a implies H4): R8a states ||Omega_g^(n)||_q <= D_n g^-n, so
  q_g[chi_g] <= D_1^2 g^-2; substituting Phi = sigma_g into H0 gives b_g[m_g] <= kappa_P D_1^2 g^-2.
  C4a uses L_g[Omega_g f] = b_g[f] (normalization checked) and ||P chi|| <= ||chi||. C4b's
  rank-one q-norm bound 2 sqrt(E+gamma) sqrt(1+kappa_P) D_1/(gamma g) is reproduced.
- C5 is the product rule; the finite 2x2 witness is correct.

Verdict: C1-C5 are correct conditional statements; H0 remains open and R10 remains open,
exactly as the repair states. The order-zero sufficient list is now H0-H3. This is the
strongest unconditional-in-form reduction of the R10 package to date: H4 is no longer an
independent hypothesis.

## Process note

An integration branch of the unpushed repair was prepared in parallel
(claude/r10-integrate-20260911, 627/627 checks, 163 focused tests passed) and became
redundant when PR 150 merged with the same content. This record is what remains of it.
