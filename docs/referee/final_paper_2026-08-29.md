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
`workhouse verify` reported everything green. The guard now globs `paper/*.tex`
and fails if any edition carries an unresolved label, naming which file. A glob
and not a list, deliberately: a list is one more thing to remember when an
edition lands, and forgetting it is the failure this check exists to prevent.
(This session first wrote it as a list; the parallel session wrote the glob, and
the glob is the one that survives.)

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
below.** The edition pins the last commit before it lands, for a different and
better reason, given there. That target moves every time the registry does,
which is the point of the rule, so it is named in the manuscript's
Reproducibility section and nowhere else — including not here, where it would
go stale on the next check.

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
several name checks that do not exist on that branch. A pin has to satisfy its
own edition. That is why this edition pins a commit on this branch — not
because the other commit is missing, but because it is not this edition's. The
rule that follows is mechanical and is now applied every time the registry
changes: pin the last commit before the manuscript lands, re-measure the
counters there, and re-pin whenever a new check is added, because a pin whose
labels no longer all resolve is exactly the failure this finding was about.

The general lesson is one AGENTS.md already states, and this session committed
anyway: **a negative asserted after two commands is not a negative.** It is the
same shape as re-deriving something that already exists under different
notation — search one lineage, find a hole in it, generalise.

## The parallel session, and what was taken from it

Two sessions worked this problem at once, off the same parent. The other one's
commit is `f25328f` — the one this review wrongly called missing — and its
package arrived after this branch was already pushed. Three of its findings are
the same three this audit made independently: the two Lean counters disagreeing,
the label guard reading one hard-coded edition, and the six-channel census being
the Weingarten ledger rather than merely summing to it. Converging on the same
three from different directions is worth more than either finding alone.

Where the two differ, the stronger half wins, and it is not always this one's:

- **The Lean scrape.** This session fixed the regex in `frontier.py` and left
  `certified.py` with its own copy. The parallel session factored one
  `frontier.LEAN_DECL` and had both import it, plus a test asserting the two
  generated counts agree. Two copies of a pattern is how they drifted in the
  first place; theirs is the fix, and it is taken.
- **The label guard.** This session wrote a `CHK_EDITIONS` tuple to extend when
  an edition lands. The parallel session globbed `paper/*.tex`. A list is one
  more thing to remember, and forgetting it is precisely the failure the check
  exists to prevent. Theirs is taken, with this one's per-edition reporting of
  *which* file carries a stray label kept on top.
- **The census check.** Both wrote it, under the same name, with the same
  content. This one's carries a rigidity gate — of the 720 ways to attach six
  measured values to six predicted slots, exactly 4 survive, which is the 2x2
  conjugate degeneracy and no slack — and theirs carries the better explanation
  of why the factor of two is the content. Merged, and switched to the public
  `constants.channel_weight` rather than reaching into another suite module.
- **The companion verifier.** Theirs had 29 checks to this one's 23, and the
  two sets are not nested. Theirs alone had the charge-even `Gamma` splitting,
  the second witness's off-axis separation, and the charge-odd half of the
  high-symmetry spectra; this one alone had the closed cube surface and the two
  connected two-cube spectra reassembled from the paper's own diagonals. The
  union ships, at 25 — the three taken from theirs are re-derived here rather
  than copied, so the `Gamma` levels come out of the cubic instead of being
  asserted as a literal.
- **The bibliography.** Theirs carries 23 entries to this one's 14, and the
  gap is not padding. This edition's introduction said local topology,
  line-graph constructions and compact localised states were "all established"
  and cited nobody, and its carrier section named the singular-flat-band
  mechanism with no reference at all. Four of their extra citations are papers
  this repository's own register already holds with full provenance — the
  Munster/Seo Euclidean series the external-comparisons paragraph *discusses by
  name* while citing only the 1985 table — and those are taken outright.
  Three more (Sutherland 1986, Mielke 1991, Bergman-Wu-Balents 2008) the
  register did not hold; they were verified against primary bibliographic
  records, indexed with what reading each would settle, and cited with the
  same "not read here" the Balaji citation already carries. The register
  refused them as stubs, correctly — *a stub that no indexed paper cites is
  decoration* — so they entered as papers bearing on G14, which is where the
  Hazra comparison already sits.
- **A Windows invariant.** Their package reported the single failing check on a
  Windows host: `str(path.relative_to(...))` gives backslashes there, and the
  corpus pin file keys its rows with forward slashes, so the lookup silently
  missed. Fixed with `as_posix()`, and the guard extended — no relative path in
  `src/` may be stringified with the platform separator.

## What the reconciliation changed in the manuscript

Comparing the two editions region by region found things in this one that no
dimension of the audit had caught, because they only show up beside an
alternative.

- **The Weingarten values are the $U(N)$ ones, in a paper about $SU(N)$.** Both
  editions quote `Wg(e) = 1/(N^2-1)` and `Wg((12)) = -1/(N(N^2-1))`; those are
  the unitary-group values, and the central theorem of the second-order chain
  rests on them. The reduction is real and standard — a degree-(2,2) integrand
  is invariant under `U -> zU`, so the `SU(N)` and `U(N)` integrals agree
  provided the invariants at that degree are exhausted by permutation
  contractions, which holds exactly when the degree is below the rank, `2 < N`,
  i.e. the theorem's own `N >= 3`. At `N = 2` the extra `eps (x) eps` invariant
  appears and it fails, which is a second reason the construction begins at
  three, and the same `eps` channel that makes the `u^1` ledger row SU(3)-only.
  The parallel edition states the step; this one did not. It does now, and it
  is recorded as a fourth unchecked load-bearing premise rather than buried.
- **The all-rank theorem asserted more than one matrix element.** It stated the
  complete order-`u^2` momentum dependence on the torus as a theorem, while
  this paper's own Scope section listed the premise behind that promotion as
  unchecked — the paper contradicting itself about the status of its central
  result. The parallel edition splits it: an unconditional theorem for the
  adjacent shared-link coefficient, and a *conditional corollary* for the torus
  assembly, with the two hypotheses named. That split is taken. Its hypothesis
  (ii) is narrowed here to the part that is genuinely open, because the other
  part — that the diagonal is scalar — is provable on the torus by
  face-transitivity and is proved in the corollary's own proof.
- **The abstract's most-quoted sentence went with it.** "The complete momentum
  dependence through second order is the oriented edge-face Gram operator" is
  exactly the promoted claim; it now states the matrix element as exact and the
  assembly as conditional, and says the hypotheses are unchecked.
- **The self-contained list was self-refuting.** Its item 2 carried a premise
  no check covers and sat under the heading "self-contained". The coefficient
  and the channel lemma stay there; the assembly moves to the conditional list
  as its own item, and everything downstream that quotes a band edge or a
  bandwidth at order `u^2` is told it inherits those hypotheses.
- **"That is false in general and true here"** overstated what the
  vacuum-mediated route establishes. It kills one family of non-adjacent
  routes, by C-parity. It does not settle the enumeration, and the sentence
  introducing it now says which of the two it does.
- **The bibliography and the CBB attribution.** See above for the citations
  taken; the parallel edition also records Ciavarella-Burbano-Bauer as
  Phys. Rev. D 112, 054514 (2025) where this one keys it `CBB2026` off the
  arXiv preprint alone. That is flagged rather than changed, because the
  published reference has not been verified here.

Two further items from the comparison were flagged as larger than a merge, and
turned out to be one statement that a check settles. **The parallel edition is
right on both, and this edition was wrong on one.**

The remark "the 3 is the triple degeneracy of `B(0) = 0`, not `b_2(T^3)`" is
false. Under the discrete Fourier transform `ker d_2 = (+)_k ker d_2(k)`; at
`k != 0` the kernel block is exactly `im d_3(k)`, and `d_3(0) = 0`, so all of
`im d_3` sits at nonzero momenta and the quotient is supported entirely at
Gamma. The Gamma block *is* `H_2` and the 3 *is* `b_2(T^3)`. Two routes that
looked like an agreement worth checking are one decomposition read in two
bases — which is the better statement, and the one the paper now makes.

And the harmonic representatives the parallel edition constructs are correct:
`h_ij = (1/L) sum_r s_ij(r)` satisfies `d_2 h = 0` and `d_3^T h = 0` over Z at
`L = 2, 3, 4`; the harmonic subspace is exactly 3-dimensional, so the three
averages span it; and each single sheet differs from its own average by a
boundary, so they are the same homology class. The averaging is the `k = 0`
Fourier projection, and what it removes is precisely the non-harmonic part the
sibling FINDING measures at Rayleigh quotient 2. Nothing about that FINDING is
withdrawn — the generators Theorem 2 exhibits are still not harmonic — but the
subsection no longer ends on a negative it could have resolved in one line.
Registered as `the sheets average to harmonic representatives, and the Gamma
block IS b_2`, which carries the retraction in its own detail line.

## What is still not checked, and what a referee should press on

Recorded because a review that hides its gaps is worse than none.

- **One-shared-link processes are assumed to exhaust the second-order
  off-diagonal intermediates.** The *channel* list is no longer in that
  category — Lemma "The channel list is complete" derives it from the fusion
  rules in three lines, and the weight-sum corollary is checked. What is still
  prose is the enumeration of *processes*: that no other second-order route
  contributes off-diagonally. The paper says so in its Scope section, and it
  has no check.
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

## The second round: six more findings, applied

The nine-dimension audit and the seven-region reconciliation both finished
after the first version of this document was written. Most of what they
returned had already been applied. Six had not, and all six are now in the
tree — five as new checks, one as a correction to a check that was already
there.

**A false contrast, printed twice.** §7.1 said that "at third order the
charge-odd leakage separates from the charge-odd hopping". They were never
together: `leak_2- = -11/306` against `t_2- = 5/612` already at second order.
The pairing that actually parts is the charge-odd leakage against the
charge-**even** hopping — equal at `r = 2` (both `-11/306`, and that is `ell_3`
at every rank), unequal at `r = 3` (`-12331/249696` against `-6335/249696`).
The manuscript copied the sentence from the registry check's own detail line,
so both were wrong and both are fixed; the check now asserts the arithmetic
(`leak_2- != t_2-` at both orders, `leak_2- == t_2+` at the second and not the
third) instead of describing it, which is what would have caught it.

**"Cubic symmetry alone permits" was the wrong attribution.** The shape family
`{1, q, e_2, 4e_2/q, e_3/q}` is not what symmetry permits. The point group
permutes `(a_1, a_2, a_3)`, so its invariants are the symmetric polynomials,
and the numerators of degree at most three with no constant term span a
**six**-dimensional space `{q, q^2, e_2, q^3, q e_2, e_3}` — one per partition.
The recorded basis keeps five; the missing direction is `q^3`, the shape `q^2`,
which is cubic invariant and regular at Gamma, so neither the point group nor
the carrier projection excludes it. The omission is a property of the two-hop
enumeration that produced the family, and it is load-bearing, because the
obstruction certificate is a rank statement about *this* span. Registered as
`the shape family is not symmetry-complete: cubic symmetry alone permits q^2 as
well`, which computes both ranks.

**The Casimir retention rule had an unstated boundary convention.** "Fits
inside the truncation" was never resolved to `<= B` or `< B`, and both
retentions the section leans on sit exactly on a boundary: `Lambda^2 F = bar3`
has endpoint budget exactly `4` and the sextet exactly `6`. Under a strict rule
`B = 4` would reach `{1}` alone and `B = 6` would lose the sextet,
contradicting both delivered censuses. So the deliveries fix the convention —
which also means the budget arithmetic is not an independent confirmation of
either census, and the check says so.

**The rest-frame blindness did not need the incidence ansatz.** The paper
argued it from "the hopping enters only through `tau(u) q(k)`, and `q(0) = 0`",
an argument inside an ansatz that Proposition "boundary-factorised rigidity"
warns is not unconditional. Schur decides it outright, and decides both sectors
at once. At Gamma the little group is the full cubic point group. The
charge-odd state is the *oriented* 2-cell, on which a proper rotation acts by
its exterior square — which is the rotation itself under Hodge duality, the
defining `T_1`, irreducible, commutant dimension one, so the block is scalar at
every order. Charge conjugation drops the orientation, so the charge-even state
is the *unoriented* plane and the action is the axis permutation, `A_1 + E`,
commutant dimension two. The two commutant dimensions are exactly the two level
counts the sectors report, `{-4,-4,-4}` and `{12,0,0}`. Registered as `Schur
alone fixes both Gamma blocks`, which builds the 24 rotations, verifies the
exterior square, and solves both commutants.

**Jordan's inequality was applied where it is weakest.** It is tight at `k = 0`
and at the zone corner; the exclusion radius needs a lower bound on `q` over
`|k| >= r`, whose minimiser is on a coordinate *axis*, where Jordan is loose by
`pi^2/4`. The sharp minimum is elementary: writing `q = sum h(k_m^2)` with
`h(t) = 2(1 - cos sqrt t)`, the identity `(s cos s - sin s)' = -s sin s <= 0`
makes `h` concave and increasing on `[0, pi^2]`, so the minimum over the
simplex is at a vertex and equals `4 sin^2(r/2)`. The radius becomes
`2 arcsin((u/2) sqrt(W_4/(theta t_3)))`, leading constant
`sqrt(W_4/(theta t_3))` — exactly `2/pi` times the Jordan constant, so `17.04`
and `23.66` become `10.85` and `15.06`. The Jordan statement was never wrong,
only loose, and both `chk` labels now stand side by side. The non-vacuity
threshold `u < 0.133` is unchanged, because the two bounds agree exactly at the
corner, where the ball fills the zone.

**The even-`L` hypothesis was carried for one sector and dropped for the
other.** The manuscript proved `q_max(L) = 12` only at even `L` for the
charge-odd sector, then quoted the charge-even span `16`, the bandwidth
`88/153` and the `88/15` ratio with no qualifier. The charge-even floor `-4` is
`mu = 0`, i.e. some `ahat_m = 0`, i.e. some `k_m = pi` — which the periodic
grid samples only at even `L`, exactly as for the charge-odd top. The
charge-even *top* is different and needs no hypothesis: it sits at Gamma. The
new check tabulates the sampled floor for `L = 2..8` and shows the odd-`L`
deficit closing; the qualifier is now on the span, on the appendix rows, and on
the ratio.

Two smaller things went in with them. The second-witness subsection now says
plainly that exhibiting a witness adds no logical strength — the obstruction
theorem already proves the whole line is consistent — and that it is a concrete
handle, not evidence. And the three flat-band priority papers entered last
round (Sutherland 1986, Mielke 1991, Bergman–Wu–Balents 2008) had stranded the
graph census; they are now accounted for by name, with the reason recorded:
not-yet-obtained, so no primary reference list exists to build citation edges
from, and inventing one is what `literature/index.yaml` forbids.

## The Lean layer, and a false reassurance about C2

Found last, while checking why CI's `Lean (T0)` job passing did not license
dropping the counter table's caveat. Two sentences about the Lean layer were
false, and one of them was false about the single genuinely open item here.

**"Nothing that bears on `C_shp` appears there."** It does.
`lean/Workhouse/Basic.lean` has a section headed *The historical SU(3) kernel*
that defines `C_shp_old` as the exact rational
`-211835444920651/4405310420659200` — the historical side of C2 — and proves
three theorems about it: `C_from_beta`, `width_eq_alpha_add_beta`, and
`beta_from_A_and_C`. The stated reason for the claim was self-defeating: it
said `C_shp` does not reduce to rational arithmetic, and the file reduces it to
rational arithmetic on the next line.

The true statement is the better one, and it is now a check rather than a
sentence: the Lean layer proves *internal-consistency relations* of the
historical kernel and contains no spelling of the v10a.26 value anywhere in
the tree. So it touches `C_shp` and still prefers neither side — an absence
established by inspection, which is what the corpus rule about C2 asks for and
what a claimed absence cannot give. Registered as `the Lean core DOES carry the
historical C_shp side, and still adjudicates nothing`; T2, because naming the
rival value means reading a float.

**"It is exact-rational and polynomial algebra only."** Also false, and the
correction is a strengthening. The checkpoint deltas the same paragraph credits
are stated over `ℝ` and use `Real.sin_pi_div_four` and `Real.sin_pi_div_two`;
that section exists precisely because the extraction theorems formalised only
half a statement without it.

Two smaller things went in beside them. `verify_core.py`'s Casimir-budget check
now asserts that the strict rule contradicts both delivered censuses, not just
that the weak one reproduces them — the boundary is the content — and the
manuscript's group-six description credits it. And a note on what CI does and
does not establish: the `Lean (T0)` job runs `lake build`, which type-checks
the tree. `sorry` is a *warning* in Lean 4, not an error, so a green build does
not by itself establish sorry-freeness — that rests on the declaration scrape —
and nothing computes the axiom footprint at all. The counter table's caption
already says only what is supported, and it stays as it is.

## The full audit, aggregated

The nine-dimension workflow finished long after its individual dimensions had
been applied: 98 agents, 88 findings put to an adversarial verifier, 72
surviving. Checking the survivor list against the edition mechanically —
probing each finding's quoted text against the current file — found all but one
already applied across the three rounds above. Recording the sweep because a
list of findings nobody re-checked is not evidence that they were addressed.

The residue was a notation hole rather than a false claim. The assembly formula
credits its tower term to "the certified coupling conversion $4\Delta(3u/2)$",
and `Δ` was never defined anywhere in the manuscript — so the sentence that
says the assembly "takes no unregistered input" could not be checked from the
page even though it is true. Both series are now written out where the erratum
is discussed:

    Δ_-(x) = 2/3 + x/6 + (1/18)x² + (7/432)x³
    Δ_+(x) = 2/3 − x/6 + (13/180)x² + (101/2700)x³,   x = β_3/4 = 3u/2

which is exactly what the passing check `the printed towers are canonical-u`
converts. Writing it out surfaced a second, smaller problem it would have been
easy to introduce: `Δ` already carries four other meanings in the paper — the
checkpoint differences `Δ_X, Δ_M, Δ_P, Δ_R`, the coefficient gap `Δ_C`, and the
finite-volume separation `Δ_L`. The sector subscript is now stated to be the
only one that means this series.

Nothing else in the 72 survived contact with the current edition. Two things
the verifiers added to their finders' accounts are worth keeping, since both
sharpen rather than soften: the census residual belongs to the six channel
coefficients at 2.2e-15, not to the delivery as a whole at 2.1e-14 (the paper
now prints both and says which is which); and the held-out finite-u control is
a 66-dimensional star with the Q1–Q1 magnetic block *set to zero*, which is a
second unexecuted computation rather than a modelling choice.

## The reconciliation, aggregated

The seven-region comparison against the parallel session's edition also
finished: 77 agents, 62 recommendations surviving verification. Forty-one said
keep this edition's half, twenty-one said take the other's or merge. As with
the audit, most had already been applied — but six had not, and five of those
are defects a reader would hit on the first page.

**The title named a concept the paper never uses.** "Nested-quotient temporal
histories" appears exactly once in the manuscript: in the title. Zero of the
121 `\chk` labels touch it, and no section develops it. The title is now
"Homological flat bands and channel-resolved two-cube hopping in strong-coupling
SU(N) Hamiltonian lattice gauge theory", which is what the paper delivers.

**A sentence was broken.** "This repository and this repository re-thresholds
those gates" — a merge residue that survived three rounds of audit because
every dimension was reading for content, not prose.

**`W_4` and `θ` were used and never defined.** Five uses of `W_4`, four of `θ`,
no definition of either, in the one quantitative fourth-order statement the
paper makes. Both are now defined at first use: `W_4 = sup_k |ε_4(k) − ε_4(0)|`
and `θ` the fraction of the isolation gap the fourth-order spread may occupy,
fixed at `1/2` throughout.

**`H_2` meant two things.** The perturbative expansion wrote
`H_eff,- = P_-H_E P_- + uH_1 + u²H_2 + …` while §3 uses `H_2` for cellular
homology, in the same paper, twenty pages apart. The perturbative operators are
now `K^(r)_-`, matching the two-cube section's own `K^(2)_conn`, with the
reservation stated where the expansion is written.

**The retained-shell premise was asserted three ways at once.** §2 stated it as
a derived fact ("its range *is* the charge-odd one-plaquette span, since…"),
the assembly corollary *assumed* it as hypothesis (i), and Scope listed it as
an unchecked prose premise. Under the first reading the corollary's hypothesis
assumes nothing. It is now one object, `\eqref{eq:shell}`, carried as a
hypothesis in §2 with the loop-length count as its support rather than its
proof, and referenced by that label in both later places.

The same alignment fixed a stale pointer the theorem split had left behind:
Scope still said the process-exhaustion premise "is assumed in
Theorem thm:allrank". Since the split, the theorem is a statement about one
matrix element and does not need it — it is hypothesis (ii) of the conditional
corollary, and Scope now says so.

Two recommendations were declined. The near-Γ subsection keeps this edition's
framing rather than the parallel one's, because "a near-Γ statement that does
not adjudicate" is the more precise title and the parallel edition's version
drops the explicit non-bound disclaimer. And the charge-even section does not
gain a second display of `N(k)`: the determinant contrast it would carry is
already made, with its check, in "The orientation signs are essential".
