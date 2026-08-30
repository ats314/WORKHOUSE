# Refereeing the final edition

2026-08-29. Target: `paper/master_paper_2026-08-29.tex`, the final edition —
the 28 August united edition plus the two-cube section, the charge-even closed
form, the one-cube shell decomposition and the fourth-order geography.

Method: a nine-dimension audit run as a workflow — exact arithmetic, the
printed check labels, fidelity to the delivered two-cube documents, agreement
with the registry, provenance and counters, scope and overclaim, missing
content, LaTeX structure, and a hostile mathematical read — each finding then
handed to an adversarial verifier whose default was to refute it. What follows
is what changed the repository and the manuscript, not the full transcript.
Dimensions that return after this document was written are recorded by
extending it, not by replacing it.

## The headline

**The arithmetic holds.** Every displayed rational in the draft was
re-derived independently, symbolically in `N` where the statement is all-rank,
and every one checks: the four channel weights and their closed forms, `A_N`,
`B_N`, `t_N`, `ell_N`, the large-`N` series through `1/N^9`, the bandwidth
ratio and its `88/15`, the Weingarten pair as the inverse of the `S_2` Gram
matrix, the incidence identity by Gröbner reduction rather than sampling, the
charge-even cubic and its four high-symmetry spectra, the six-channel census
and its cutoff split, both two-cube spectra reassembled from the delivered
diagonals, the checkpoint algebra, and the fourth-order geography. No false
number was found anywhere in the draft.

What the audit found instead is **five things the paper said that its own
machinery did not support**, and they are the interesting part.

**1. The label guard read the wrong file.** The paper's central device is that
every displayed result prints the name of the machine check that establishes
it, and the repository's answer to "who checks the device?" was
`every \chk in the united paper names a check that exists and passes`. That
invariant hard-coded `master_paper_2026-08-28.tex`. So the 29 August draft
could — and did — print a label that resolved to nothing, while
`workhouse verify` reported everything green. The guard now reads a tuple,
`manuscript.CHK_EDITIONS`, and fails if any listed edition is missing or
carries an unresolved label. **The tuple is the thing to extend when an edition
lands.**

**2. A check name asserted more than the arithmetic under it.** The check
`the C-even range [-4, 12] is exact, and each edge is attained at one point
only` was true at the top and false at the bottom: the floor `lambda = -4` is
attained wherever some `k_j = pi`, which is the whole of three planes, and the
predicate it actually ran (all three eigenvalues equal `-4`) is the *triple*
root condition. It also contradicted its own sibling next door, which had the
planes right. Renamed to
`the C-even range [-4, 12] is exact; the top only at Gamma, the floor on three
planes`, with the attainment sets now asserted rather than implied. The
manuscript's Proposition was right all along; the registry was the thing that
had drifted.

**3. The paper's strongest new claim named a check that did not exist.**
`the B=6 six-channel census IS the Weingarten four-channel ledger, channel by
channel` was printed twice and registered nowhere; the only registered census
check was the *sum*, which the paper itself calls weak evidence. It exists now,
and it is the stronger statement: six delivered coefficients against four
weights computed from the dimension/Casimir table, with the two conjugate
coincidences the correspondence requires and no slack — 4 of 720 labellings
survive, exactly the `2 x 2` conjugate degeneracy.

**4. The rigidity proposition named its ingredient, not its statement.**
Proposition (boundary-factorised rigidity) printed the incidence identity,
which is what Theorem 1 prints. Nothing evaluated `a I + b S + B M B†` on the
carrier for a generic `M` — and "for every `M`" is the whole content, since it
is what makes the protection a property of the boundary operator rather than of
any particular correction. Registered, with nine free entries and the six
incidence variables kept independent.

**5. ~~The pinned commit did not exist.~~ RETRACTED — see *A retraction*
below.** The edition pins `5ca91a9` for a different and better reason, given
there.

## Two things the repository was wrong about

**`FRONTIER.md` under-reported the Lean layer.** `frontier._lean_counts`
matched `^\s*(theorem|lemma)\s`, so an `@[simp] theorem` was invisible to it —
while `certified.lean_claims` had already been fixed for exactly that bug and
counted them. Two generated views of the same tree reported 37 and 40. Fixed at
the scrape; both now say 40. A count that is wrong in one generated file and
right in another is worse than either, because whichever a reader opens first
reads as authoritative.

**`paper/verify_core.py` checked five of the nine groups its manuscript
claimed.** The draft's Reproducibility section listed nine claim groups; the
shipped verifier had five. It now has nine, in twenty-three checks: the
two-cube connected geometry rebuilt from oriented cell boundaries with both
truncation spectra, the census channel by channel, the charge-even cubic in the
same Gaussian-rational arithmetic the incidence identity uses, the checkpoint
algebra with `e_2` vanishing on every axial cut, the closed cube surface, and
the coupling convention. Still standard-library only, still float-free, still
under a second.

## What the manuscript gained

Corrections, all of them from the audit: the census result is called a Reported
result in the abstract and cross-references, not a Theorem; the two connected
diagonals are printed, so both spectra are one line of arithmetic for the
reader rather than an appeal to a delivery; the per-channel reconstruction
residual (`2.2e-15`) is separated from the delivery-wide one (`2.1e-14`), which
the draft had attached to the wrong object; the held-out star is described as
the delivery describes it, with its `Q_1`–`Q_1` magnetic block set to zero; the
22-dimensional `E_*` eigenspace and its `11 + 11` split are stated, so the
delivery's resolvent convention is visibly the paper's own; the shared
`pyclebsch` archive behind both the two-cube build and the `B = 6` cube is
named, because repetition is not independence; the same-face sextet threshold
is `20/3` and not the rounded integer label; the checkpoint momentum `P` is
defined; the charge-even tower is printed, without which five rows of its
ledger cannot be reproduced; and the torus fingerprint is attributed to the
certificate that actually contains it.

## What was derived here

Three statements the audit did not ask for, found while checking it.

**The one-cube shell, derived rather than assigned.** Both deliveries label the
single-cube charge-odd shell `A_1^{--} + T_1^{+-} + E^{--}` and neither builds
the symmetry matrices; the `B = 6` route's own gate 7 says so. On the closed
cube surface `G` commutes with all 24 proper rotations, `b_{+i} - b_{-i}`
carries the defining vector representation and `b_{+i} + b_{-i}` the
permutation representation of the three axes, and with the charge-odd inversion
the parities follow. The `G`-eigenvalues attach uniquely by dimension. And
`ker d_2` is one-dimensional, spanned by the sum of the six outward faces —
the fundamental class, `b_2(S^2) = 1`. So the cube's flat level is the same
homological object as the torus carrier, and it sits at the scalar for *every*
hopping coefficient: no truncation, no channel and no coefficient in dispute
anywhere in the paper can move it.

**The connected diagonal is orbit-constant.** Both deliveries print `D` as
eleven numbers. It is three: the open `(3,2,2)` prism has a symmetry group of
order 16, its face orbits are `8 + 2 + 1`, and `D` is constant on them in both
truncations. The eight-orbit is exactly the support of the four cross-cell
pairs, and it is the only orbit whose value moves with the cutoff — the end
caps stay at `-15/4` and the shared face at `0` at both `B = 4` and `B = 6`.
Together with the four cross-cell blocks carrying the whole off-diagonal
change, the entire `B = 4 -> B = 6` difference is confined to the faces that
carry connected transport.

**Which also explains the nonuniform `D`.** Where the faces of a complex are a
single orbit — the closed cube, the periodic torus — orbit-constancy forces the
diagonal to be scalar, and `alpha I + t G` is exact. The prism has three orbits
because it has a boundary. `D` is the open boundary showing up in the diagonal,
not a failure of the incidence form. The all-rank theorem's "the diagonal terms
are scalars in face-orbital space" now says why, and names the case where it
fails.

## What the scope audit changed

The dimension that read the paper as a hostile referee looking only for
overclaim found eight more, and none of them is arithmetic either.

- **"measured here on the 1,590,462-state space" contradicted "the construction
  was not re-run here"**, eleven lines apart, and it was the load-bearing
  justification for calling the census more than a coincidence of one sum. It
  now says what is true: the delivery resolves it on the two-cube space; what
  this repository checks is the identity the six delivered numbers satisfy.
- **1,590,462 is a basis dimension, not the scale of a computation.** The
  delivery says flatly that the magnetic matrix is never assembled at that
  dimension — the contraction runs over 794 paths and 398 reachable states. The
  abstract said "space of 1,590,462 states" and the body said
  "1,590,462-state construction" twice more. Only the first use, which names it
  as a truncation's basis, survives.
- **The census shares its amplitudes with the thing it is checked against.**
  The two-cube build draws its local Wilson amplitudes from the same
  hash-pinned `pyclebsch` archive as the single-cube reconstructions, and the
  squared amplitudes that archive produces are the published `d_rho/N^2` — the
  numerator of the weight formula. So the census does not confirm the weights
  from an independent source; it tests the *assembly* that carries them: the
  reachable-channel list, the resolvent denominators, the operator-level fold,
  the even split between conjugates, and the geometry that survives each
  channel separately. That is a different statement, and the paper now makes it
  rather than the stronger one. Repetition is not independence, and neither is
  a shared upstream.
- **Target blindness was stated one notch above the delivery's own
  qualification.** The value is byte-present in the nested `B=4` package the
  `B=6` build seals as an authority object, and the delivery calls its
  chronology record-backed and only partly auditable. The defensible claim is
  dependency-path nonuse, and the paper says that now.
- **A third load-bearing prose premise was unadmitted.** The Scope section said
  "two"; there are three. That the charge-even sector's Bloch symbol is the
  unsigned incidence — the signed one with the boundary orientations dropped —
  is asserted and never argued, and the closed-form cubic, the range, the
  bandwidth and the `Gamma`-splitting all rest on it. The registry records it
  as a convention, not a result.
- **The second premise was also stated less precisely than it can be.** Three
  of its ingredients are settled: the two tensor-product decompositions are
  complete by representation theory, two distinct faces share at most one link,
  and the vacuum route vanishes by C-parity. What is not settled is that
  one-shared-link processes exhaust the second-order off-diagonal
  intermediates. The gap is in the process enumeration, not the channel list,
  and the paper's central theorem now carries that qualifier in the
  self-contained list rather than only in Scope.
- **The near-Gamma exclusion radius "survives the dispute" only as a two-way
  choice.** `K` depends on the kernel through `sqrt(W_4)`, and `W_4` depends on
  the coefficient; the larger `K` bounds the two *recorded* candidates and
  nothing else. C2 is open, not an interval. Retitled, and the limitation
  stated.
- **"A constraint on any candidate" outran its measurement.** The `A`-pinning
  result is a weight audit inside one fixed 189-record support. A kernel on a
  different support is not constrained by it, and the paper's own next item
  makes identical support an observation about the two records rather than a
  property of the problem.
- **Schierholz crossed the regime firewall the paper enforces two paragraphs
  earlier.** A `beta = 5.9` Euclidean Monte Carlo measurement and an `a -> 0`
  power law were being used to draw a structural conclusion about a
  strong-coupling finite-lattice program. It stays, as a warning about why G18
  must live in a smeared basis, with nothing transferred.

## What the coverage audit added

The dimension asked what the paper *should* carry and does not found four
things worth taking, beyond the three derived results above (which it
independently proposed, and which had already landed).

- **The channel list is a lemma, not an assumption.** The Scope section said
  the four fusion channels are "assumed" to exhaust the shared-link routes.
  Completeness of the *list* is one line: the shared link carries `F` or
  `Fbar`, one plaquette action tensors it by `F` or `Fbar`, and both products
  decompose completely and multiplicity-free. It is now a lemma in the body,
  and the corollary that makes it checkable — the weights sum to one per
  family, so a missing channel would leave a deficit — is named with it. What
  remains assumed is sharper and smaller: that one-shared-link processes
  exhaust the second-order *off-diagonal* intermediates. The gap is in the
  process enumeration, not the channel list.
- **The disputed coefficient had no magnitude anywhere in the paper.** The
  longest section is about `C_shp` and never printed either recorded value or
  the gap, which made "less than half the disputed gap" unreadable and left
  `25/1024` — a witness the paper itself says is not a physical candidate — as
  the only number attached to the dispute. Both values and the gap are printed
  now, side by side and in no order of preference, with the note that one is
  recorded exactly and the other only as a float. That asymmetry is a fact
  about the records, not an argument for either.
- **The `B = 7` scalar prediction was executed, and the paper reported it as
  arithmetic.** The delivery ran a six-face `B = 7` reachable-state probe:
  `alpha = 11/34`, `t = 5/612`, residual `1.1e-15`. So raising the cutoff past
  the same-face sextet threshold lowers all three absolute coefficients by
  exactly `1/4` and leaves the relative shell `{0, 5/153, 5/102}` untouched —
  a prediction made and then run, which is stronger than a subtraction. Its
  artifact did not travel, so it is reported and not checked.
- **A two-point argument where a determinant identity was available.** "The
  unsigned spectra at Gamma and R share no eigenvalue, so no level can be
  momentum independent" samples two momenta for an all-`k` conclusion. Reading
  straight off the boundary formulas, `det B(k) = 0` identically — a zero
  eigenvalue at every momentum, which *is* the flat band — while
  `det N(k) = -2 prod_j (1 + e^{i k_j})` vanishes only where some `k_j = pi`.
  One identity replaces the sample, and the registry already had it.

## What CI caught that no dimension did

The repository's own Windows smoke job failed on the first push, and it was
right to. `workhouse why C2` prints the theory graph's arrows (U+2192, U+2190);
a default Windows console encodes cp1252; the command died with
`UnicodeEncodeError`. It reproduces identically on `main`, so it is not this
work's — but it is exactly the failure class `tests/test_portability.py`
already guards in the other direction, and that guard covers only text the
repository *reads*. The output side was never covered.

Fixed where the input fix went: the CLI names its output error handler
(`backslashreplace`) instead of inheriting whatever the console can encode, so
one character degrades rather than the command dying, and every UTF-8 platform
is byte-identical. The guard now covers both directions, in a subprocess with
the console encoding forced — because the failure is in the stream, not in the
string, and an in-process assertion would pass everywhere and prove nothing.

## A retraction

Finding 5 above said the draft's pinned commit
`f25328f8d6658af63588fb3d30dbd3b7f6ede9c0` did not exist in this repository, on
any branch, so no row of its counter table could be reproduced. That is false,
and it is worth recording exactly how it went wrong.

The commit exists. It is a **sibling** of this work: a parallel session, off the
same parent `afc946c`, committed *Two counters disagreed, and a channel census
turned out to be a ledger* at 19:27 UTC on 29 August. It sits in no ref — it was
pushed by hash — so a clone that has fetched only branch heads does not have the
object, and `git cat-file -t` on an object you have not fetched is
indistinguishable from `git cat-file -t` on an object that was never made.
`git log --all` agrees with it, for the same reason. Two commands, one blind
spot, and the conclusion was generalised from both. The decisive command was
never run: `git fetch origin <sha>`, which succeeds.

And the counters were right. At `f25328f` the tree carries T0 = 40, T1 = 179,
T2 = 46 — precisely the numbers the draft printed. The parallel session's own
package says the 472-test row was pinned-commit provenance rather than a fresh
local run, and labels it as such. So the draft's Reproducibility section was
accurate for the commit it named, and the finding against it was an artifact of
this session's clone.

What survives is smaller and still worth having: those counters describe
`f25328f`, and this edition's printed labels do not all resolve there, because
several name checks that exist only in `5ca91a9`. A pin has to satisfy its own
edition. That is why this edition pins `5ca91a9` — not because the other commit
is missing, but because it is not this edition's.

The general lesson is one AGENTS.md already states, and this session committed
anyway: **a negative asserted after two commands is not a negative.** It is the
same shape as re-deriving something that already exists under different
notation — search one lineage, find a hole in it, generalise.

## What is still not checked, and what a referee should press on

Recorded because a review that hides its gaps is worse than none.

- **The four fusion channels are assumed to exhaust the shared-link routes.**
  The Weingarten theorem fixes the weight of each channel; nothing establishes
  that the list is complete. The paper says so in its Scope section, and it has
  no check.
- **That the range of `P_-` is exactly the charge-odd one-plaquette span for
  `L >= 3`** is argued in prose from the link count of a reduced fundamental
  loop. Also stated, also unchecked.
- **The Lean layer was not re-compiled for this edition.** The `T_0` row counts
  theorem declarations with no `sorry`, which is a scrape; `make lean` is what
  compiles them, and the environment this edition was typeset in carries no
  toolchain. The counter table says so.
- **The `1,590,462`-state build was not re-run.** Its arithmetic is audited
  against geometry rebuilt locally; its generators need `pyclebsch` and three
  sealed inputs that did not travel. No external group has reproduced it.
- **The all-rank even split is a conjecture with a falsifier and no attempt.**
  A link-resolved census at `N = 4` in a truncation retaining every adjacent
  shared-link channel needs `B >= 33/4`, and none has been run.
