# Recovered Lean source review, 2026-09-07

All five archive-only Lean files were read in full. They comprise three
substantive modules and two import wrappers. The source scan found **no declared
axiom and no `sorry` or `admit`**. Two final tightness theorems use `native_decide`;
the witness source itself discloses the `Lean.ofReduceBool` trust consequence.
These are source observations, not a fresh Lean compilation or an executed
`#print axioms` audit.

`RECOVERED_LEAN_REVIEW.json` records exact hashes, original outer/nested/member
locations, declaration lines, imports and integer checks. The files remain at
their content-addressed object paths; no live Lean source or theorem register
was changed.

## What the code actually states

`Workhouse/DenominatorChecker.lean` defines prime support of denominators and
numerators separately. Negation, addition, subtraction and multiplication
preserve the appropriate support; inversion explicitly requires numerator
support. A `CertifiedAtom` carries its positive denominator bound and a proof
that the reduced denominator divides it. `ExactExpr` composes such atoms using
LCM at additive nodes and products at multiplicative nodes, and the main
induction proves denominator divisibility for that supplied expression.

Its CRT theorem requires an already supplied congruence modulo `M` and the
strict window `|(b-a)| < |M|`, expressed using integer `natAbs`. It proves
uniqueness within that window. It neither constructs a complete residue ledger
nor verifies physical history enumeration. These assumptions are explicit in
both definitions and explanatory text, not a hidden circularity.

`Rank3Order4QBoundCertificate.lean` proves arithmetic for named component bounds
and the displayed atom `-13/896`. The physical components `w2`, `r2` and `haar`
are arbitrary rationals with supplied denominator-divisibility hypotheses.
The final sum theorem requires that every supplied term already obey the bound.
It does not derive the physical atom or connect a symbolic value to a file hash.

`Rank3Order4QBoundWitnesses.lean` adds literal lists of 58 W2 and 181 R2 reduced
denominators. `by decide` checks membership-wise divisibility; explicit quotient
witnesses put each stage bound inside `qTight`. The capstone requires each term's
denominator to belong to one of those lists. The two `native_decide` facts show
that the literal lists' LCMs equal the named stage bounds. The external equality
between these lists and the hash-pinned physical history ledger remains an
extraction/modeling premise. The source says this clearly.

## Independent arithmetic and current-register comparison

Python integer arithmetic recomputed the exact list lengths and LCMs:
`881280` and `409824214482575692800`. It also checked every list divisor,
`qTight = 2*qW2*qR2*qHaar`, `896 | qTight`, both explicit quotient witnesses,
and `qPath/qTight = 68410380572018343936` with zero remainder. All passed.
This verifies the stated finite integer data independently of Lean parsing.

The live `lean/Workhouse/` tree and `ledger/theorems.yaml` contain no modules or
registered theorem namespaces named `DenominatorChecker`,
`Rank3Order4QBoundCertificate` or `Rank3Order4QBoundWitnesses`. Existing rank-law
and all-rank denominator-polynomial theorems are different statements. Therefore
these are useful unregistered formalization candidates, not merely byte-renamed
copies of those live declarations.

No recovered statement proves a volume-uniform nonlinear G19 scale comparison,
the new Wilson H2 remainder, the actual physical source-projection transport,
or a continuum mass gap. None claims to. Their useful contribution is a small,
typed denominator/CRT interface whose external certificate assumptions can be
connected to exact computational provenance in a later bounded integration.
Historical inventory labels such as 'complete' based on absence of tokens must
not substitute for a current toolchain build and actual axiom report.
