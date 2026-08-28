# WORKHOUSE cubic rank-3, order-4 QBOUND reconciliation

Date: 2026-08-23

## Result

The frozen exact-history denominator envelope and the independent conservative
source-only envelope are arithmetically consistent.

The frozen tighter bound is

```text
QTIGHT = 62895057857493885215590055852113920000000
       = 2^36 * 3^20 * 5^7 * 7 * 11 * 13 * 17^3
         * 19 * 23 * 29 * 31 * 37 * 47.
```

Its generated components are

```text
QW2       = 881280
QR2       = 409824214482575692800
QHAAR     = 87071293440000 = 2^18 * 3^12 * 5^4
QBILINEAR = 2
QANALYTIC = 896
QPAIR     = 2 * QW2 * QR2 * QHAAR = QTIGHT
lcm(QANALYTIC, QPAIR) = QTIGHT.
```

The earlier source-only path envelope is

```text
QPATH = 4302674844130269372677454153332635148085549843213189120000000
      = 2^56 * 3^45 * 5^7 * 7^2 * 11^2 * 13 * 17^3
        * 19 * 23 * 29 * 31 * 37 * 47.
```

Lean kernel-checks

```text
QTIGHT | QPATH
QPATH / QTIGHT = 68410380572018343936 = 2^20 * 3^25 * 7 * 11.
```

The reduction is explained by exact addition and reduction of all generated
W2/R2 trace-network coefficients before their denominator LCMs are taken.  The
larger path envelope assigns worst-case local denominators before those exact
cancellations.  No published target coefficient is used to select `QTIGHT`.

## Analytic term and zero-gap gate

The analytic one-face coefficient is not supplied as a target literal.  The
external generator evaluates a four-state exact recurrence using `Fraction`
arithmetic from an H0 vector and interaction matrix pinned to the `DATA_O4`
source.  It obtains orders zero through four

```text
[8/3, 1, -1/4, -1/16, -13/896].
```

Lean encodes the final value as an already-reduced rational, proves it equals
`(-13 : Q) / 896`, and proves `896 | QTIGHT`.  Lean does not re-run the
recurrence or verify its source hash.

The external exact generator now closes the previous `E0/P0` premise before
applying the reduced resolvent.  It constructs the scaled plaquette band and
uses exact SU(3) Haar Gram arithmetic support by support.  The final freeze
records one W1 and 25 W2 resonant groups, zero residual norm in every group,
and 52 exact resonant signature exclusions after that proof.  Its
`unresolved_premises` object is empty.

This E0/P0 proof is external and hash-pinned; the small Lean arithmetic file
does not re-implement it.

## What Lean verifies

The compiled files verify:

- the displayed component and `QTIGHT` factorizations;
- `QPAIR = QTIGHT`, `896 | QTIGHT`, and the LCM identity;
- `QTIGHT | QPATH` with the exact quotient above;
- exact rational encodings of `1/2` and `-13/896`;
- generic allowed-prime closure for rational sums and products;
- conditional denominator composition for a W2/R2/Haar pair term;
- finite-sum assembly once every external term carries a denominator witness;
- a centered CRT uniqueness theorem from a supplied combined congruence and
  strict uniqueness window.

The final build completed successfully with 861 jobs and contains no `sorry`
or `admit`.

## Precise trust boundary

The Lean kernel does **not** parse the frozen JSON, compute SHA-256, prove the
external ledger complete, or derive the per-history coefficient witnesses.
The current end-to-end claim therefore has two explicit layers:

1. The hash-pinned external generator constructs and tests the exact W2/R2
   history, exact E0/P0 cancellation, the analytic recurrence, compatibility
   census, and denominator envelopes.
2. Lean verifies the small arithmetic consequences of the resulting declared
   integers and of caller-supplied per-term denominator witnesses.

To make the bridge fully kernel-connected, a later generated Lean certificate
must emit:

- a denominator witness for every frozen W2 and R2 coefficient;
- an exact endpoint-Haar value or denominator witness for every compatible
  pair;
- an expression tree proving that the intended assembled coefficient equals
  `analyticRat + terms.sum`;
- optionally, a verified parser/hash layer if authentication itself must move
  inside Lean.

The frozen package still does not contract and sum the 117,161 endpoint-Haar
topologies, produce the final `D_EXACT`, or certify the injected fold term.
Thus it is an exact Q-reduced denominator certificate, not yet the complete
fourth-order scalar coefficient certificate.

## Frozen provenance

```text
generator file SHA-256:
  a72a2c412bfa3a7da3847ac4fe04c48fb5e1d1db7f95ae4e391c1ea31ca306ce
primitive file SHA-256:
  3685369c951036765f940612114419e76e27dd4f9efe79112053a48abd1faa33
primitive canonical-JSON SHA-256 embedded in freeze:
  2eda6c8940280d269e27983800d8f51d9cc51dc27735ef71823dfff37b1362ab
history ledger SHA-256:
  543869b10f5137ea74fbd5f27d25027dea66f936ce9844b77a029453b8bf8c97
freeze file SHA-256:
  e68d515899f03d1a84a028645b2f42e176bb0bb54c3b21be8be030da41f1dc26
freeze canonical self-hash:
  5020661c4e52a84ac2fa64753f44c934780e25390ad2fc887939b90331e2a6c3
DATA_O4 source SHA-256:
  68782826d50ad6bcbb3a20d83649bfa7f66e42c5706d131361b7d189b1f99a8f
```

Independent verification on 2026-08-23 re-read the freeze and history hashes,
checked all freeze self-checks, and ran all 16 generator tests successfully.

