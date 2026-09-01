# hecke_cover_correspondence — a candidate Hecke-eigenline mechanism

**Definition of done:** the generator, the verifier, and both JSON
certificates the note names are landed here with their SHA-256 digests, and
an invariant in this repository re-derives — not merely re-transcribes — at
least one of the ten target-blind prime values from the stated lattice
construction, independent of the external engine.

## What is here now

- `NOTE_FLUX_hecke_cover_correspondence_2026-08-31.md` — the maintainer's
  result note, transcribed 2026-08-31. Record-backed only: this is the one
  artifact of the six the note names that actually reached this repository.

## What is not here

`ENGINE_FLUX_hecke_cover_correspondence.py`, the geometric certificate, the
post-hoc verifier, the replay report, and the nine-test suite the note
describes all remain on the maintainer's own machine
(`/C:/ALL THEORY/programs/gauge_dressed_spectral_zeta_20260830/
harmonic_packet_20260831/`). Nothing in this campaign has re-run them.

## Claimed connection to the open dispute

The note's infrared parameters (`tau`, `C`, `S_0`, `A`) and its quartic
harmonic `H_4` share vocabulary with this corpus's own fourth-order shape
coefficients (`C2`, `G3`, `UNIFIED §5.1`). The note does not itself assert
an identification, and this repository has not derived one — see the
"Open question" section of the note, and unifying candidate `U6` in
`ledger/gaps.yaml`, which states the falsifier that would settle it.

## What this repository has checked

Exactly one thing: that the printed target-blind table is internally
arithmetically consistent (`A_p = p^4 lambda_p` for all ten listed primes,
exactly, in `sympy.Rational`). See
`src/workhouse/invariants/hecke.py`. That is a transcription guard, not
independent evidence for the construction itself.
