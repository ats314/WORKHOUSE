# Rank-3/order-4 cubic exact QBOUND audit

## Result

The new generator closes the half-history denominator question without float reconstruction or target-driven fitting.

- It symbolically derives every nonzero scaled W2 coefficient (82,384 records) and every nonzero Q-reduced scaled R2 coefficient (82,278 records) using `Fraction` arithmetic.
- It proves the E0/P0 subtraction exactly before removing resonant signatures: one W1 and 25 W2 physical E0 groups all have post-projection Gram norm `0/1`.
- It derives the analytic one-face coefficient by an independent exact scalar-P recurrence. The primitive manifest contains no `-13/896` literal; the recurrence emits `8/3, 1, -1/4, -1/16, -13/896` through order four.
- It freezes and hashes the complete 164,662-record history ledger and QBOUND before the separate target scanner reads `constants.py`.
- All 10 enforced target denominators divide the frozen QBOUND. This is denominator compatibility only, not independent validation of their numerators or physics derivations. `LINKED_VACUUM_4_ARTIFACT` remains quarantined; a generic prime is forensic evidence, not an automatic artifact verdict.

All 16 bounded fail-closed, regression, hash, E0, and audit tests passed. A fresh final generation, frozen-hash verification, and separate target audit also passed.

An additional independent E0/P0 harness confirms the integrated proof by a separate union-find Haar contraction. It obtains an exact `2 I` Gram matrix for the 192 translated/oriented plaquette vectors, exact-zero W1/W2 residuals, and exact agreement on 98,698 distinct state-pair Haar values. That harness, its certificate, and its README are included under `independent_e0_audit/` in the package.

## Exact-history bound

The frozen bound is

```text
QBOUND = 62895057857493885215590055852113920000000
       = 2^36 * 3^20 * 5^7 * 7 * 11 * 13 * 17^3
         * 19 * 23 * 29 * 31 * 37 * 47.
```

Its exact components are:

```text
LCM(den W2) = 881280
            = 2^7 * 3^4 * 5 * 17

LCM(den R2) = 409824214482575692800
            = 2^10 * 3^4 * 5^2 * 7 * 11 * 13 * 17^2
              * 19 * 23 * 29 * 31 * 37 * 47

Haar divisor = 87071293440000
             = 2^18 * 3^12 * 5^4

bilinear denominator = 2
analytic denominator = 896 = 2^7 * 7
```

Thus the pair branch contributes the displayed QBOUND directly. The analytic denominator already divides it, so the final `lcm` does not enlarge the bound.

The prime exponents are transparent:

- `2^36 = 2^(7 W2 + 10 R2 + 18 Haar + 1 bilinear)`;
- `3^20 = 3^(4 W2 + 4 R2 + 12 Haar)`;
- `5^7 = 5^(1 W2 + 2 R2 + 4 Haar)`;
- `7, 11, 13, 19, 23, 29, 31, 37, 47` come from exact R2 gap histories, with `7` also present in the independently derived one-face term;
- `17^3 = 17^(1 W2 + 2 R2)`.

Endpoint Haar `q_h` is therefore included exponent-wise. The compatibility census checks all 2,468,250 H0/translation/center-flux-compatible state pairs, observes exactly the seven supported local patterns, and proves a maximum of 24 total occurrences. Dynamic programming over those patterns yields the universal `2^18 * 3^12 * 5^4` Haar divisor. This is conservative because it does not yet use the actual pattern multiset of each of the 117,161 collapsed topologies.

## Why this is much tighter than the independent envelope

The independent path-level envelope is

```text
QPATH = 4302674844130269372677454153332635148085549843213189120000000
      = 2^56 * 3^45 * 5^7 * 7^2 * 11^2 * 13 * 17^3
        * 19 * 23 * 29 * 31 * 37 * 47.
```

The exact relation is

```text
QPATH / QBOUND = 68410380572018343936
                = 2^20 * 3^25 * 7 * 11.
```

So `QBOUND` divides `QPATH` exactly. The difference is methodological: `QPATH` assigns worst-case local-H denominator-6 exponents to 9,392 W2 and 9,201 R2 paths before addition. The new generator first performs every exact trace-network addition, cancellation, projector action, and fraction reduction, then takes the denominator LCM of the resulting coefficients. Both retain the same universal endpoint-Haar envelope. The improvement is therefore symbolic history reduction, not use of any audited target denominator.

## Non-circularity and exact E0 handling

Generation consumes only the exact primitive manifest and pinned source-document hashes. It constructs `W1 -> R1 -> W2 -> R2`, derives both denominator LCMs, derives the one-face term, performs the compatibility census, freezes QBOUND, serializes the full ledger, and verifies temporary hashes before publishing.

At each reduced-resolvent step, gap equality is exact. More importantly, gap-zero blocks are not merely discarded: the generator constructs the scaled charge-odd plaquette band for every matching H0 signature, evaluates the required SU(3) Haar Gram products exactly (balanced k=1, balanced k=2, and determinant channels), subtracts `<p,v>/<p,p> p` supportwise, and requires residual norm exactly zero. Only after that proof are the 52 raw resonant signature branches excluded.

The target audit is a separate invocation. It re-verifies the freeze self-hash and full history hash before AST-reading exact constants. It cannot change the frozen ledger or QBOUND. Its pass means only that each enforced denominator divides QBOUND; it does not independently validate target numerators or the physical derivation of those constants.

## Remaining boundary

This is an exact Q-reduced denominator certificate, not yet the complete fourth-order scalar certificate. It does not calculate exact endpoint-Haar numerators for all 117,161 collapsed topologies, perform the final `D_EXACT` integer sum, or combine the fold and linked-vacuum scalar terms. Those are the next arithmetic layer over this frozen input lineage. Separately, identifying the generator's frozen scope and primitives with the intended physical perturbation expansion remains a theory/modeling obligation outside this arithmetic certificate.

## Key hashes

```text
generator              a72a2c412bfa3a7da3847ac4fe04c48fb5e1d1db7f95ae4e391c1ea31ca306ce
primitive file         3685369c951036765f940612114419e76e27dd4f9efe79112053a48abd1faa33
history ledger         543869b10f5137ea74fbd5f27d25027dea66f936ce9844b77a029453b8bf8c97
freeze file            e68d515899f03d1a84a028645b2f42e176bb0bb54c3b21be8be030da41f1dc26
freeze self-hash       5020661c4e52a84ac2fa64753f44c934780e25390ad2fc887939b90331e2a6c3
target audit           aad538ae95c70d3fd1f3017c33eccef9e2b8b2d33dc528f41b331295ba9dcbb5
```
