# Flat-background path sources and the physical rank repair

This run accompanies the analytic flat-holonomy theorem and the obstruction
to differentiating its physical Coulomb source projection across stabilizer
changes. The complete proof is preserved in `PROOF.md`; the identical
canonical source is
`paper/research_notes/G19_FLAT_HOLONOMY_SOURCES_AND_RANK_REPAIR_20260907.md`.

With the repository's SymPy dependency available, run:

```text
python -B check_flat_holonomy.py --replay CONTROLS.json
```

Replay checks the full manifest, rebuilds the mathematical report in Q(i),
and compares every field. It reads no repository module or external data.
The checker also accepts `--output` at a fresh path. Optimized Python and
duplicate JSON keys are rejected. `tests/test_flat_holonomy_sources.py`
performs a cold relocation, rejects an altered and repinned mathematical
report, and checks that the canonical proof matches the frozen copy.

The controls cover every Fourier/alias direction on n=4,L=2 for the neutral
color and three charged-background cases. The noncentral phases have exact
SU(2) lifts: for a+ib on the unit circle with a>-1, use
diag(c+is,c-is), c=sqrt((1+a)/2), s=b/(2c). Its adjoint on E12 is a+ib.
For phase -1 use diag(i,-i). The conjugate character supplies the real
charged color plane, and the neutral character is the identity case.

Direct differentiated anchored words are checked against separately built
cochain and Fourier matrices. Exact Hermitian elimination checks the full
physical inequality with constant 1/132 and the unreduced tangent Gram
bound 1/4. A separate real-space construction checks boundary-column
multiplicity, transport and right-inverse normalization at (n,L)=(4,2),
(3,3), and (4,4), including a single coarse box with winding paths.

The negatives are mathematical: freezing the identity source loses an
actual shifted harmonic; deleting a transport phase breaks the cochain
identity; and the false fast constant 100 fails. The projection-jump
witness is harmonic and retained at identity but is a gauge gradient at
the noncentral background. It is not a physical fast-gap counterexample.

The all-size theorem, the smooth-family construction and the explicit
nonflat neighborhood follow from the analytic proof. These finite checks
do not prove those quantifiers, an interacting true-vacuum comparison,
an OS-history identification or a continuum mass gap. No native CHK or
Lean theorem is added by this run.
