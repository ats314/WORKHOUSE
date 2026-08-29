# The two-cube kernel: B4 and B6 on a real face-sharing Hilbert space

Every prior cube result in this repository — `balaji_open_cube_b4_t1`,
`b6_open_cube_channel_complete` — lives on ONE cube. The adjacent-face hopping
was read off a single cell and a graph ansatz. This release does it on an
actual face-sharing two-cube prism, with the connected part obtained by
literal operator-level Möbius subtraction rather than by fitting a scalar.

    B4  (8,361 states)      K_conn = -1/12 · G_conn + D_B4
    B6  (1,590,462 states)  K_conn = +5/612 · G_conn + D_B6

## What was verified here

`independent_verification.log`. The builder needs `pyclebsch` and ~9.6 MB of
NPZ artifacts that did not travel with the documents, so this is a check of
the sealed bytes and the arithmetic, not a re-execution.

**Seals.** Every uploaded file hashes to the value the detached manifest
records for it, and the manifest itself hashes to `021558ce…`, the root the
theorem document states. The bytes are the sealed release bytes.

**The channel census is this registry's own rank law.** The six shared-link
coefficients, recovered target-blind, resolve exactly into the four the
all-ranks suite already carries:

    3 + 3bar = -1/6  = w_3bar        1 = +1/12  = -w_1
    6 + 6bar = -2/9  = w_6           8 = +16/51 = -w_8
    like-orientation sum = B_3       mixed-orientation sum = -A_3
    census = B_3 - A_3 = 5/612 = hopping(3)

So `t_N = B_N - A_N` — an abstract rank law in `constants.py` — appears here
as an actual sign on individual channels in a two-cube contraction. The minus
on the mixed-orientation family is the charge-odd projection, made operational.

**Matrix and spectrum.** `K_conn - (5/612)·G_conn` is exactly diagonal, with
`G_conn` built from geometry alone (zero diagonal, `-1` on the four cross-cell
pairs), and the residual diagonal is the document's `D_B6` to the integer.
Spectra: B6 `{0, (-15/4)², (-34/9)⁴, (-129/34)⁴}`, B4 `{0, (-15/4)², (-11/6)⁴,
(-5/3)⁴}`, both exact.

**The restored channels are the bridge's own completion.** `6 + 6bar + 8 =
14/153`, which is `w_6 - w_8` — the number registered from the CBB bridge
before any two-cube calculation existed, reached here by a different route.

## What this does not establish

The documents are candid and their limits are kept: second order in `u` only;
finite volume; `D_B6` is B6-truncated and not proved stable under larger
cutoffs; the finite-`u` check is a 66-dimensional `P+Q1` star, not the full
1.59-million-state Hamiltonian; radius three was preflighted and stopped; no
external group has reproduced it.

Two boundaries stated by the release itself and worth repeating. "Exact" means
exact rational reconstruction from hash-pinned **finite-precision** CGCs, not
a symbolic-CGC proof. And the deterministic replay is the same builder, so it
proves reproducibility, not independence.

The `5/612` target-blindness claim is dependency-path nonuse, which the
release says plainly rather than overstating: the value occurs elsewhere in
sealed metadata, the comparator is classed `posthoc_only`, and the chronology
is record-backed rather than cryptographically preregistered.
