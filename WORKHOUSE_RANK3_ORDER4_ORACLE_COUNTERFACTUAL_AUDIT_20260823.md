# Oracle/local-shift counterfactual audit

## Verdict

The proposed dichotomy is incomplete.  The exact package does **not** inherit
or consume the later `local_shift`, and the later `local_shift` does **not**
force `-11.068479...`.

What the exact package independently reconstructs is the quantity that the
later v10a.24c source itself names `M4_SHORTCUT` and quarantines.  Its arithmetic
non-circularity is real.  Its physical completeness is not established by that
fact.

This is therefore the actual third case:

> The exact Haar route genuinely regenerates the target-known scalar shortcut
> without diagonal fitting, but it evaluates the same restricted shortcut
> construction.  It does not evaluate the later finite-cluster oracle or the
> complete full-T1/marked-cluster physical construction whose absence motivated
> the quarantine.

No repository file was edited.  This audit and its executable scanner live only
under `work/oracle_counterfactual/`.

## 1. The two quantities are explicitly different in v10a.24c

The line-addressable v10a.24c source has this dataflow:

```text
7309  M4_ORACLE   = float(totals[4])
7310  M4_SHORTCUT = -160506019419340168451 / 14501180577204921600
7324  ax_rest      = V23_AXIAL_SHAPE['rest_direct']
7324  local_shift  = M4_ORACLE - ax_rest
7325  K4_mass_cols = V23_AXIAL_H4_COLS.copy()
7326  diagonal anchor entries += local_shift
```

Thus `local_shift` is constructed to force the final rest scalar to
`M4_ORACLE`, not to `M4_SHORTCUT`.

The completed v10a.24c transcript records:

| quantity | value |
|---|---:|
| blind folded axial rest | `-11.9485781794007` |
| finite-cluster `M4_ORACLE` | `-0.7751458630189173` |
| quarantined `M4_SHORTCUT` | `-11.068479463778765` |
| actual `local_shift` | `+11.17343231638178` |
| final shifted rest | `-0.775145863018919` |

The transcript also prints
`|M4_ORACLE - M4_SHORTCUT| = 10.293333600759848` and concludes
`SCALAR ORACLE RETURNS THIRD VALUE`.

Therefore the statement “`-11.0685` is forced by `local_shift`” is false for
the preserved implementation and completed run.  The diagonal fit forces
`-0.775145863...`.

## 2. Exact package arithmetic

The independently contracted pieces are

\[
D_{\rm EXACT}
=-\frac{361008126292641364183}{7250590288602460800},
\]

\[
F=\frac{5315003}{140454},\qquad
V_{\rm link}=-\frac{1474623}{1675520}.
\]

Before the linked-vacuum subtraction, the exact raw folded scalar is

\[
r_0=D_{\rm EXACT}+F
=-\frac{86634244910174898583}{7250590288602460800}
\approx-11.948578179401377.
\]

This agrees with the pre-unblind v10a.24c folded rest to its floating-point
precision.  The exact package then computes

\[
r_{\rm shortcut}=r_0-V_{\rm link}
=-\frac{160506019419340168451}{14501180577204921600}
\approx-11.068479463778765.
\]

That fraction is byte-for-number identical to the v10a.24c
`M4_SHORTCUT` literal.  The adjustment from `r0` is

\[
-V_{\rm link}=\frac{1474623}{1675520}
\approx0.880098715622613,
\]

not the v10a.24c `local_shift` of approximately `11.17343231638178`.

## 3. Poison/dependency test

The scanner `audit_oracle_dependency.py` inspected every executable arithmetic
input used by the exact package:

- the exact primitive manifest;
- the W2/R2 generator;
- the endpoint-Haar contractor;
- the exact Q1 fold reproducer;
- the linked-vacuum reproducer; and
- the exact marked-cluster engine imported by that reproducer.

Across those inputs it finds zero occurrences of:

```text
local_shift
M4_ORACLE
M4_SHORTCUT
ax_rest
160506019419340168451
11.068479463
0.775145863
```

It also finds no `eval`, `exec`, `globals`, or `locals` route.  The imported
marked-cluster engine has one environment read for an authenticated sealed
Phase-3 source descriptor, but the linked-vacuum reproducer never enters that
Phase-3 path and no oracle/shift key is present.

The frozen W2/R2 ledger has SHA-256

```text
543869b10f5137ea74fbd5f27d25027dea66f936ce9844b77a029453b8bf8c97
```

and 164,662 records.  No diagonal/order-four scalar is an argument to
`build_exact_histories`: its W2/R2 path is the explicit
`source -> W1 -> R1 -> W2 -> R2` construction from H0/Fierz/fusion primitives.

### Important provenance qualification

The primitive manifest hash-gates the v10a.20b notebook, and that notebook
contains the already-known `M4_PREV=-11.068479...` regression literal after the
exact assembly.  The generator reads that notebook only to compare SHA-256 at
`ledger_generator.py:344-357`; it never parses its coefficients into W2/R2.

So this is not a prospectively blind discovery.  It is a target-known,
independent arithmetic replay.  The known target can have influenced which
construction was chosen and frozen, but there is no numeric target-to-output
dataflow edge.

## 4. Exact counterfactual in a diagonal parameter

Let `ell` denote an arbitrary scalar added only at the late v10a.24c diagonal
anchoring step.  Then the exact dependence is

| object | dependence on `ell` | derivative |
|---|---|---:|
| W2 histories | `W2(ell)=W2(0)` | 0 |
| R2 histories | `R2(ell)=R2(0)` | 0 |
| `D_EXACT` | `D(ell)=D(0)` | 0 |
| Q1 fold | `F(ell)=F(0)` | 0 |
| linked vacuum | `V(ell)=V(0)` | 0 |
| package shortcut | `r_shortcut(ell)=r_shortcut(0)` | 0 |
| v10a.24c final rest | `r_mass(ell)=r0+ell` | 1 |

Consequently:

- at `ell=0`, v10a.24c retains the blind raw fold `r0`;
- at `ell=-V_link`, the scalar happens to equal the shortcut, but this is the
  independently computed linked-vacuum subtraction, not the actual oracle
  shift; and
- at the v10a.24c oracle shift
  `ell=M4_ORACLE-r0`, the final rest equals `M4_ORACLE` by construction.

The centered shape is invariant under this last scalar anchor, but that does
not make the scalar recovery independent.

## 5. What this does and does not change

This audit upgrades one narrow statement:

> The exact Haar numerator calculation is not numerically circular through the
> v10a.24c `local_shift` or `M4_ORACLE`.

It does not upgrade the physical coefficient:

- the primitive manifest selects one polarization (`polarization_index=2`);
- the package computes the scalar `D=<W2|R2>` route, the Q1 scalar fold, and a
  one-/adjacent-two-face linked-vacuum subtraction;
- it does not run the complete 609-cluster full-T1 Phase-3 marked construction;
  and
- the completed later oracle disagrees with the shortcut by about 10.2933.

Therefore C1/C22 (or any equivalent full-construction/completeness quarantine)
should not be reopened merely because the shortcut numerator has now been
computed exactly.  The right next test is an exact, target-blind evaluation of
the omitted full physical construction, followed by a separate comparison to
both the shortcut and the numerical oracle.

## Evidence hashes

| artifact | SHA-256 |
|---|---|
| primitive manifest | `3685369c951036765f940612114419e76e27dd4f9efe79112053a48abd1faa33` |
| W2/R2 generator | `a72a2c412bfa3a7da3847ac4fe04c48fb5e1d1db7f95ae4e391c1ea31ca306ce` |
| exact endpoint contractor | `f944bfef52a2176de113d0ca66dd4d1c98ada7f4224ec3cccc8d4c4ae48b7e29` |
| Q1 fold reproducer | `063979837850c1c8ae3bacb4317a75020c7b92db89681b5785c2c22807a9ef3c` |
| linked reproducer | `ac7a0feb4581d64315cbea1e16fd81632f79754d4a30fc276d1e0411c54f25e8` |
| imported exact marked-cluster engine | `be9d77f5b245715ed6e4fe6dc9178a56ddfa5c68efe697eaa7cf4bb6adae27ad` |
| v10a.20b notebook | `47c6ccc18079c49416c511c2a27a9d757525d6e279992514ed63f5ba413530fd` |
| v10a.24c source | `935a3a5ba680d1373a5842486b10231d83232d8cb3393bbc250351bc51a68c8b` |
| completed v10a.24c result transcript | `aa053d110e0abb2c4464ad9c78b391a111d6ccb8be43e2e049783e95a0a3f40a` |
