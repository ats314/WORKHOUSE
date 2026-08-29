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

**5. The pinned commit did not exist.** `f25328f8…` is not an object in this
repository, so the printed reproduction recipe could not be run and no row of
the counter table could be checked. Re-pinned, and every counter re-measured.
The `T_1`, `T_2` and test rows matched no state the tree has ever been in, which
is exactly what a hash that does not resolve stops anyone from noticing.

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
