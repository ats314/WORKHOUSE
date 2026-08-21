# Literature

Published work, indexed by the claim it bears on. `index.yaml` is the map;
`workhouse lit` reads it.

The corpus arrived with almost no bibliography. The governing document cites
"Hamer's table" for the decimal that carries its strongest external validation,
without a paper; the citation had to be recovered from a Python dict inside
`corpus-import/numerics/engines/ENGINE_Y6_su3_y5_historical_recovery_r2.py`,
and a 2026-07 audit had separately recorded that the bibliography *omits* it.
It is C. J. Hamer, Phys. Lett. B 224, 339–342 (1989).

That is the shape of the problem this directory addresses: the program leans on
published results that are not written down anywhere a reader can follow.

## What is here

Eight papers and twelve edges. The index prints how many rest on a source nobody
here has read, rather than hiding it.

Three edges are verified against a paper actually read:

- `CS_2006 → C7` — the Weingarten calculus that falsified the stranded-flux zero
  backend, now re-derived from the general formula rather than quoted from a
  transcript.
- `SCHIERHOLZ_1988 → G18` — an independent 1988 measurement of the same
  few-percent bare-operator overlap, *and* the scaling `a^5` that makes the
  smeared basis structural rather than a convenience.
- `KRS_2023 → U1` — a modern, unrelated construction of the gauge-invariant
  SU(3) Kogut–Susskind Hilbert space, by prepotentials rather than by a chain
  complex. Two routes to the same object is what would turn U1 from an
  observation into a mechanism.

## What is stored, and what is not

One paper. `KRS_2023` is CC BY-NC-ND, which permits a verbatim copy, so the
unmodified PDF is here and its bytes are hashed against the digest of the copy
that was read. Everything else is under publisher copyright or arXiv's
assumed-1991-2003 licence, neither of which permits redistribution; those are
pinned by `source_sha256` so the reading stays identifiable without the file
being republished.

The gate is enforced in `literature.py` and exercised by tests that mutate an
entry to confirm it fires — not remembered.
