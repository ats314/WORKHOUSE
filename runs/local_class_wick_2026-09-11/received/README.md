# Exact continuation of the local SU(N) class spectrum

This package develops the user's archived local-spectrum results into an
all-rank exact recurrence and computes both charge sectors through beta^-2.

- [Derivation and theorem](DERIVATION.md): the rank-uniform shell resolvent,
  all-order formal recurrence, recovered coefficients, c3- and c4+/- formulas,
  sign theorem, and precise scope.
- [Final coefficients](coefficients_order5.json): exact symbolic expressions
  and complete polynomial residual checks.
- [Independent checks](validation_order5.json): Cartesian SU(3)/SU(2)
  calculations through the final order and positive-polynomial sign witnesses.
- [Archive and structural checks](validation.json): 87 exact checks against
  the independent archived engine, low-rank cases and known formulas.
- [Provenance](provenance.json) and [task record](TASK.md).
- [Exact source inputs](sources/): preserved byte-identical copies.

The main structural result is the polynomial shell resolvent

    Pi_d = exp(-D/2) H_d exp(D/2),
    R_s  = sum_(d != s) Pi_d/(s-d),       D=Delta/2.

It eliminates the need to invert rank-dependent trace Gram matrices.
Every fixed perturbative order is a finite computation in Q[N,N^-1].

The recovered c0, c1, c2 and c3+ formulas belong to the prior research.
This continuation derives an explicit all-rank c3- and both c4 expressions.
The final formulas reproduce the recorded SU(3) c4 values exactly.

Validation completed: 87 archive/structural checks, 37 final-order checks,
and 45 symbolic residual/normalization/compatibility assertions in the
order-five run. The separate two-coordinate check through c3 also passed.
These checks have different scopes; their counts are not independent proofs
of the complete physical theory.

Scope: exact formal local Wilson oscillator expansion. No new finite-beta
remainder bound, interacting-volume theorem, continuum closure, Lean
compilation or repository tier promotion is claimed.

## Reproduce

Requires Python and SymPy 1.14.0. From this directory:

    python reproduce.py --out D:/WORKHOUSE-output/local-class-reproduction-NEW

Choose a destination that does not already exist. The runner preserves all
previous output, copies the small source package, runs the symbolic and
independent checks, and retains one log per command. The fifth-order symbolic
run took several minutes in this environment.

## Storage

C: was full when the first completed calculation attempted to save its JSON.
The original initial files remain at
C:/WORKHOUSE/research/local_class_wick_20260911.
This completed package is at D:/WORKHOUSE-output/local_class_wick_20260911.
No existing archive or canonical scientific files were modified or deleted.
This is a standalone local result; it has not been published or integrated.

