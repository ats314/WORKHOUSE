# Review of PR 150: R10 source-vacuum energy transport jets

Verdict: request changes. The submitted argument does not establish R10, so its promotion to proven and the G19 priority-2 closure are unsupported. This review identifies failed proof steps; it does not disprove R10.

Reviewed source: C:/WORKHOUSE/worktrees/r10-energy-jets-20260911, clean branch antigravity/r10-energy-jets-20260911 at 88e4d8228fd3fa89374ece36bfeb861e0b97df2e. Live GitHub PR 150 was OPEN, with this same head and no status-check entries. Live main was b9651bea3d772d3968eaddce72f0c6ad316928db. No repository source, ledger, index, or GitHub record was changed during this review.

## Findings

### 1. P1: Conditional differentiation omits the changing fiber measure

Source: docs/derivations/w6-source-energy-jets-r10.md:59-65, also 133-135.

The claimed identity f'(w)=E_mu[X(Phi)|w] does not follow from X(w)=1. Apply the predecessor's exact conditional-divergence identity SF7d to Phi X and X. At regular w, it gives

    d/dw E_mu[Phi|w] = E_mu[X(Phi)|w] + Cov_mu(Phi, div_mu X | w).

The omitted term includes the variation of the ground density and the fiber geometry. Neither its cancellation nor a bound is proved for this model. Consequently the subsequent Cauchy-Schwarz calculation does not discharge H0 with kappa_P=1. H3 repeats the same omission for Phi replaced by tilde_sigma Phi.

Exact demonstration that the asserted general rule fails: on [-1,1]^2 use density (1+a*w*y)/4 with |a|<1, X=partial_w, Phi=y. Then E[Phi|w]=a*w/3 and its derivative is a/3, whereas E[X(Phi)|w]=0. This is a counterexample to the general differentiation rule, not to actual-square H0.

Repair: retain the covariance term and establish a model-specific energy estimate, or prove the additional structure that cancels it.

### 2. P1: H1 loses two inverse powers of g and changes its premise in code

Source: derivation lines 88-101; src/workhouse/invariants/w6_source_energy_r10.py:51-65.

The document states a fiber diffusion gap at least c_trans and therefore a physical gap g^2*c_trans/2. Its displayed inverse estimate, after substituting ||V-E[V|w]|| <= C_V*g^2, is

    (2/(g^2*c_trans)) * (4/g^3) * (C_V*g^2) = 8*C_V/(c_trans*g^3),

not 8*C_V/(c_trans*g). Squaring gives a g^-6 bound, not H1's g^-2 bound. The Python check instead assigns gap=gamma_trans independent of g and verifies arithmetic under that stronger premise. It does not prove the new premise.

There is a separate analytic gap: the cited magnetic geometry concerns a local Hessian on nine-dimensional fixed-Q charts, with seven controlled directions and a soft branch. It is not a uniform spectral-gap theorem for the full eleven-dimensional regular w fibers with the actual conditional ground measure. The full-space score Poisson equation also cannot simply be replaced by a purely tangential fiber equation: normal derivatives and conditional coupling must be accounted for. The predecessor SF7e explicitly retains such terms.

Repair: prove the appropriate conditional operator identity, uniform physical fiber coercivity on the specified domain, and uniform forcing estimates. A full-space quantum gap is not an automatic fiber gap.

### 3. P1: H2 uses a false uniform scalar inequality

Source: derivation lines 119-123; invariant lines 76-88.

Write v=E[V|w]. The proof claims

    4*sqrt(32*kappa_0)*g^-4*sqrt(v) <= C_1*g^-2*(1+g^-2*v).

For v=g^2, the ratio of the left side to the right side without C_1 is 8*sqrt(2*kappa_0)/g, which diverges at zero. Thus the assumptions used in this step do not imply a g-independent C_1. This disproves the scalar implication used, not H2 itself for the actual ground.

The next sentence also supplies no uniform bound for the drift and flux terms: smoothness for every positive g does not bound their derivatives uniformly as g approaches zero.

Repair: obtain a stronger covariance/conditional-moment estimate or prove a cancellation in the complete SF7e identity, with explicit uniform drift and flux control.

### 4. P1: The second projection derivative drops mixed product-rule terms

Source: derivation lines 232-235.

Use the source's trivialization P=U^-1 Pi U, U'=-sigma U, and (U^-1)'=U^-1 sigma. Its displayed formula for P'' omits

    U^-1 (2*sigma*Pi' - 2*Pi'*sigma) U.

Pi depends on g because it is conditional expectation for mu_g. These terms cannot be suppressed as derivatives of a fixed projection. The exact finite-dimensional check uses Omega=(cos t,sin t), Pi conditional expectation onto constants with probabilities (cos^2 t,sin^2 t), and U=diag(1/Omega). At t=pi/4 the true P'' minus the displayed formula equals [[0,-4],[-4,0]].

Repair: use the complete derivative expansion and bound every mixed commutator.

### 5. P1: Higher fiber/operator bounds are asserted from integrated ground-jet bounds

Source: derivation lines 212-216 and 246-249.

R8a controls the actual ground derivatives in the global q_g norm. It does not by itself control conditional L2 norms uniformly over w, the conditional moments of sigma_g^2, or the energy action of multiplication by the conditional mean m_g. Dividing a global ground jet by Omega and invoking the same decomposition does not supply these missing estimates. The proof also states A_P''=[P''',P]+[P'',P'] but subsequently only claims a bound for the first commutator.

Repair: state and prove the higher conditional moments, spatial estimates and mixed operator bounds needed by each term, including the parameter derivatives of m_g. The r=1,2 argument remains incomplete even if H0-H4 were separately established.

### 6. P1: Verification functions report analytic closure without testing it

Source: src/workhouse/invariants/w6_source_energy_r10.py:25-40, 69-101, 122-182; tests/test_w6_source_energy_r10.py.

H2 computes a ratio but never checks it, then returns True. H3 and Kato derivatives also return True unconditionally. The bridge checks positivity of 2^(1+d0) and returns True. H0 only simplifies Gamma_ww/Gamma_ww. Other checks confirm exponent arithmetic under inserted assumptions or positivity at arbitrary constants. The tests then assert these return values and message substrings.

All nine checks are registered with the default T1 tier; none declares rests_on inputs. The verifier emits PASS T1 with prose claiming the analytic hypotheses are proved. Fresh execution confirmed 9/9 passes while the exact independent counterchecks above detect invalid steps. Passing these tests does not support the ledger's promotion of R10 or removal of its priority.

Repair: restrict each check's name, message and evidence scope to the exact algebra it computes; implement decisive checks where possible, and keep unproved analytic hypotheses explicit. Restore the open/conditional scientific statuses until the actual estimates are established. Preserve the attempt as evidence.

## Additional unresolved H4 step

Derivation lines 159-175 assume a normalized semiclassical marginal profile, its differentiated remainder, and control outside a tube. These estimates are not supplied. A tube with radius O(g^2) does not literally carry all probability for a smooth positive ground. The g^2 factor for 1-w^2 requires endpoint localization; an interior bound O(1) would instead give O(g^-4) under the displayed m'_g scaling. Even at an endpoint, weighted derivative and tail estimates are needed. The cited w6-synchronized-m10-domination.md file is absent from the reviewed worktree.

A useful conditional simplification survives: if H0 is proved with uniform kappa_P, applying it to Phi=sigma_g and using R8a yields

    b_g[m_g] <= kappa_P*q_g[chi_g] <= kappa_P*D_1^2*g^-2.

Thus H4 would follow from a valid H0 and the established first ground jet, without the new profile assumption. This implication does not prove H0.

## What remains usable

The reviewed predecessor supplies R8a ground jets, R8b vacuum-only transport, the SF4-SF5 complete generator representation, SF6 score Poisson equation, SF7e exact conditional energy identity, and SF9 as a conditional order-zero reduction under H0-H4. The R10-to-R11/R12 conditional implication remains available. The new submission has not discharged the required actual-source input, and has not settled the interacting-grid successor.

## Verification and provenance

- Startup briefing executed; target-specific saved snapshot retained in start.json. Freshness matched the local generation record, fingerprint 99e87f5b1eaeb03616d12607bded38a5ae0aaf66e7dad5fd5dd28b0a1d89fd50. Saved briefing itself executed zero checks.
- Independently ran python -m pytest -p no:cacheprovider tests/test_w6_source_energy_r10.py -q: nine tests passed, exit 0.
- Independently ran workhouse verify --only 'W6 R10' -v: nine PASS T1 outputs, exit 0.
- counterchecks.py reproduced the derivative-rule counterexample, H1 power mismatch, divergent H2 ratio and missing P'' terms using exact SymPy calculations. Results in counterchecks.json.
- The claimed 1,969-test full run was not rerun and its historical console output is not present in the pasted transcript. This review verifies only the focused executions listed above.
- No Lean build was run; the PR introduces no Lean proof for these bounds.
- Repository and GitHub scientific state were left unchanged. This is a local review artifact, not a posted GitHub review or correction PR.
