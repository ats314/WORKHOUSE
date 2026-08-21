# Literature

Published work, indexed by the claim it bears on. `index.yaml` is the map;
`workhouse lit` reads it, and `workhouse lit --holes` prints what the map is
structurally missing.

The corpus arrived with almost no bibliography. The governing document cites
"Hamer's table" for the decimal that carries its strongest external validation,
without a paper; the citation had to be recovered from a Python dict inside
`corpus-import/numerics/engines/ENGINE_Y6_su3_y5_historical_recovery_r2.py`,
and a 2026-07 audit had separately recorded that the bibliography *omits* it.
It is C. J. Hamer, Phys. Lett. B 224, 339–342 (1989).

That is the shape of the problem this directory addresses: the program leans on
published results that are not written down anywhere a reader can follow.

## What is here

Indexed papers, the claims they bear on, and — since v2 — the citation web
between them. The counts are printed by `workhouse lit` rather than written
here, where they would rot: how many edges rest on an unread source, which
papers the web itself leans on most, and which unobtained paper to acquire
next.

The verified edges are the ones checked against a paper actually read; the
strongest are:

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
- `MP_1999 → G18` and `LLL_2006 → G18` — the two modern spectra, one Euclidean
  and one Hamiltonian-limit, that any spectral bridge must land on. Both put
  the 1⁺⁻ at 2940 MeV centrally, read and pinned here.

## The citation web

Each indexed paper carries a curated `cites:` list, populated from primary
sources only — the INSPIRE reference list of its `inspire_recid`, or the
pinned PDF's own bibliography — and resolvable to another indexed paper or to
a stub in the `stubs:` section. A stub is a node, not an evidence entry: it
can be cited and ranked but bears on nothing and can promote nothing.

Two relevance weights, kept apart because they mean different things:
`inspire_citations` records the field's global count with its retrieval date;
the in-web in-degree is computed at generation time and measures what THIS
program's sources lean on. The most in-web-cited paper nobody here has read
is, automatically, the next acquisition target — `workhouse lit` and
FRONTIER §7b both print it.

`workhouse lit --holes` is the payoff: pairs of papers that bear on the same
claim with no citation path between them, and papers that bear on a claim
without citing the web's most-cited source for it. Each hole is a research
lead — either a connection the literature missed or a sign our own bears_on
curation conflates two threads — listed with what checking it would take.
A hole is never auto-promoted to anything.

The layer has already paid twice: Hamer 1989's reference [7], the series his
x³ and x⁴ terms disagree with, is the three-author Kogut–**Sinclair**–Susskind
1976 paper, which an earlier note here conflated with the two-author KS_1975
(the published-comparisons suite now asserts the disentanglement); and the
holes report surfaced that KRS_2023 constructs the same Hilbert space as
SZH_1997 with no citation link between the two lines.

## Getting the unobtained

The web computes what to fetch; the acquisition loop makes fetching it a
two-minute task instead of an archaeology session:

```bash
workhouse lit --acquire        # every unobtained paper, ranked, with links
workhouse lit --resolve ID     # arXiv / INSPIRE documents / KEK scans / OpenAlex
workhouse lit --intake         # identify inbox PDFs, print the digest to pin
```

`--resolve` touches only sources that welcome automation — a hit lands in the
gitignored `inbox/` with its digest printed. The walled-but-free archives
(ScienceDirect's open archive, APS) appear in `--acquire` as browser links: a
person fetches those in seconds, drops the file in `inbox/`, and `--intake`
does everything after the click except the curation itself, which stays a
judgement recorded in `index.yaml` after the paper is read. The KPS pass —
scan found, pinned, exact Table 2 promoted to checks the same day — is the
loop this tooling encodes.

## What is stored, and what is not

One paper. `KRS_2023` is CC BY-NC-ND, which permits a verbatim copy, so the
unmodified PDF is here and its bytes are hashed against the digest of the copy
that was read. Everything else is under publisher copyright or arXiv's
assumed-1991-2003 licence, neither of which permits redistribution; those are
pinned by `source_sha256` so the reading stays identifiable without the file
being republished.

The gate is enforced in `literature.py` and exercised by tests that mutate an
entry to confirm it fires — not remembered.
