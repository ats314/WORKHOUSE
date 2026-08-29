# The B = 6 open cube: the channel-complete branch

This closes the second and last branch of the test the finite-N bridge named
as remaining. `runs/balaji_open_cube_b4_t1_2026-08-28` did the `T1 = B = 4`
branch and found the reversed ordering; this one restores the **6** and **8**
shared-link channels and finds the sign flipped back.

    B = 4 (T1)          t = -1/12        doublet lowest
    B = 6 (complete)    t = +5/612       signed cube boundary lowest

`independent_arithmetic_audit.log` is this session's own audit. The generator
could not be re-run here — it needs `pyclebsch` and an adapter that did not
travel with the bundle — so what is checked is the certificate's arithmetic,
not its physics:

    gap matrix  ==  (39/68) I + (5/612) G          to 8.4e-15
    eigenvalues  =  {39/68, 371/612 x3, 127/204 x2}
    relative     =  {0, (5/153) x3, (5/102) x2}
    census       =  1/12 - 1/6 - 2/9 + 16/51  =  5/612   exactly

## The scalar disagreed, and the disagreement is the interesting part

The bridge predicted an open-cube scalar of `11/34`. This run reports `39/68`.
The difference is **exactly 1/4** — and `39/68 - 1/4 = 11/34`.

That is not an error on either side. The bridge's own section 5.1 names a
local **same-face sextet** route worth `-1/4`, and this certificate
independently reports that the same-face sextet first enters at cutoff **7**.
So `B = 6` is channel-complete for the adjacent-face hopping `t` but *not* for
the on-site scalar, which needs `B = 7`. Two calculations identified the same
missing route from opposite directions without being told to.

## Scope

Second order in `u` only, and the global `B = 6` basis was deliberately **not**
enumerated (`full_B6_global_basis_enumerated: false`): only states reachable by
one action of `M` are needed for a second-order coefficient. So this is exact
at `O(u^2)` in a reduced space, not a finite-coupling diagonalisation.

## Upstream licensing, for the record

The source audit notes that both upstream repositories (`ymcirc`, `pyclebsch`)
report `license: null`. Recorded as a fact about the provenance chain, not as
a blocker: this repository is private, nothing is being redistributed, and the
maintainer has independently re-derived the construction.

Nothing from either upstream repository is stored here — what is stored is the
reconstructor's own instrument and certificate, and derived physics results.
