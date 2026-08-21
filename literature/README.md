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

Six papers, eight edges, and three named gaps. Six of the eight edges rest on a
source nobody here has read — the index prints that count rather than hiding it.

The one verified edge is `CS_2006 → C7`: the Weingarten calculus that falsified
the stranded-flux zero backend, now re-derived from the general formula in the
`published comparisons` invariant suite rather than quoted from a transcript.

## What is not here

Full text. Every indexed paper is under publisher copyright or arXiv's
assumed-1991-2003 licence, neither of which permits redistribution. The licence
gate in `literature.py` is enforced by a test, so this stays true by
construction rather than by memory.
