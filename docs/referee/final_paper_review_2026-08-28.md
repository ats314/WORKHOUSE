> **Provenance note (2026-08-28, this repository).** This review was produced
> in an external session against commit `ca3d440` and uploaded by the
> maintainer. The twenty checks it describes as "what the repository gained"
> were written in that session but never committed; the commit that adds this
> file reconstructs them (as 23 checks, 148 → 171, including
> `src/workhouse/torus.py`) together with the master-paper edition the review
> asked for. One correction to the text below: exhibited cycles bound the
> kernel from BELOW and mod-p rank bounds it from ABOVE, not the reverse.

# Refereeing the flat-band manuscript

2026-08-28. Target: `paper/homological_flat_bands_2026-08-28.pdf`, which pins
this repository at `ca3d440a7f93c17569e12d0511847505b6b72c5a` — the commit this
review started from.

Method: nine independent claim classes, each re-deriving from the manuscript's
own stated definitions before looking at anything here, then three adversarial
verifiers under distinct lenses (recompute / coverage / convention-and-scope),
then a completeness critic asked what nobody examined. 154 rows asserted a
problem or a coverage hole; 129 survived. What follows is what changed the
repository, not the full transcript.

## The headline

The manuscript is careful and its arithmetic holds. Every displayed rational
was re-derived independently and every one checks. Its §9 counters are correct
at the commit it pins. Its §6 fourth-order firewall holds *by measurement* —
this repository's own coefficient-signature scanner finds `{d_3, b_3, leak_3}`
in it and no fourth-order signature at all. Its Hamer cross-check reproduces
the residual this repository independently measures.

Three things are worth an author's attention, and none is an arithmetic error.

**1. §9's "The analytic proof in this paper is self-contained" is jointly
refuted by three places in the paper.** eq. (18)'s "isotropy" is asserted in
one word; Lemma 4 carries no proof environment; Remark 5's "exact enumeration"
was performed elsewhere. Individually each is defensible. Together they
contradict the global claim.

**2. Theorem 3's proof needs one more clause, and this repository has the
receipt.** "Every second-order inter-plaquette process uses one shared link" is
false in general. The vacuum-mediated route `<p'|V|0><0|V|p>/(E_0)` connects any
pair of plaquettes, sharing a link or not, and is worth `1/C_F` per pair. It
vanishes in the charge-odd sector only because `V` is C-even and
`<0|V|p,-> = 0`. C13 in this repository is the record of what omitting it costs:
`A_3 + B_3 = -481/612` is exactly the superseded C-even hopping, corrected to
`-11/306` by the missing `3/4`. The manuscript's result is right; the sentence
as written would license the error that produced C13.

**3. §6's "three harmonic sheets" are not harmonic.** The only generators
Theorem 2 exhibits are the wrapping sheets. They are cycles — `d_2 s = 0`
exactly — but they are not in `ker d_3*`, and `L_up = d_3 d_3*` moves them with
Rayleigh quotient exactly 2 at every `L >= 2`. The manuscript uses `H_2` in two
incompatible senses four pages apart: the quotient in Theorem 2, where the
sheets span it, and the harmonic subspace in §6, where `L_up` annihilates it.
Nothing downstream breaks — Proposition 7 rests on `B* w = 0`, which covers all
of `ker d_2` — but §6's real-space restatement does not cover the objects
Theorem 2 constructs.

Smaller: Table 1 row 5's "32 lifter classes" is three classes over 32 numerator
patterns each (96 in total); the abstract attaches "For L >= 3" to a count that
Theorem 2 does not need; Table 2's `u^1` row is SU(3)-*only* rather than an
SU(3) specialization, and its scope is not stated; and Lemma 4's "unmatched"
must mean multiplicity exactly one, since a link carrying three fundamental
indices does not integrate to zero for SU(3) — the manuscript's own `+u` is
that channel.

## What the repository gained

Twenty checks, 148 -> 168. The ones that are not bookkeeping:

- **Theorem 2 is now checked.** Both existing checks were arithmetic on the
  formula: one simplified `(L^3-1)+3 - (L^3+2)` to zero, the other evaluated
  that formula at L = 3, 4, 5. Neither ever built a boundary map. The new
  `src/workhouse/torus.py` builds the periodic cubical complex over Z from the
  manuscript's eqs. (41)/(42) and settles the ranks, with rank over `F_p`
  bounding the kernel from below and the exhibited cycles bounding it from
  above — the manuscript's own proof, carried out.
- **Theorem 1 and Theorem 2 are joined for the first time.** The manuscript
  states a 3x3 spectrum and an `(L^3+2)`-dimensional carrier and never remarks
  that the two agree. Summing the Bloch nullity over the allowed momenta gives
  profile `{3 at Gamma once, 1 at each of the other L^3-1}` — the same two
  numbers from different objects: the 3 is `B(0) = 0`'s triple degeneracy, not
  `b_2(T^3)`, and the `L^3-1` counts momenta, not cubes.
- **`A_N` and `B_N` stop being transcriptions.** They now follow from the
  dimension/Casimir table through `w_R = -(d_R/N^2)/(C_F + C_R/2)`, with each
  channel gap verified as `E_intermediate - E_external` and the weights shown
  to sum to one per family.
- **`ell_N` is promoted from T3.** The corpus prints the all-rank C-even
  hopping and gates it in a notebook as `factor(Wmix + Wlike + 1/CF)`; nothing
  here checked it. Registering it turns C13's one-line, one-rank resolution
  into a formula: the omitted vacuum route is exactly `1/C_F = 2N/(N^2-1)`, at
  every rank.
- **One assembly formula replaces four separate ledger facts.**
  `E_s(lambda, r) = tower_{r,s} + 12 leak_{r,s} + lambda t_{r,s}` reproduces
  all eight registered band values across both charge sectors and both orders.
  The tower term is the already-certified coupling conversion `4 Delta(3u/2)`,
  so nothing unregistered enters — which means the coupling erratum (C4/G2) and
  the band ledger turn out to be the same statement.
- **The manuscript's §4 unsigned-incidence control is not hypothetical.** It is
  the C-even sector: the signed span 12 gives the C-odd width `12 t_- = 5/51`
  and the unsigned span 16 gives the C-even width `16|t_+| = 88/153`. The
  corpus certificate's own key for the second is literally
  `corrected_Ceven_bandwidth_16|t|`.
- **Two FINDINGs**: the wrapping sheets are cycles but not harmonic, and no
  Gamma-point datum can constrain the hopping.

## A retraction

Mid-review this session concluded that `b_3 = 1975/124848` was not established.
That was wrong, and it is worth recording how.

The Hodge-Haar resolvent notebook sets itself an explicit gate — "cold evaluate
`P V R V R V P` ... **without using** the recorded full third-order
coefficient" — and its three stored attempts return 0 histories with two FAILED
gates, a crash, and a truncation. Gate 20 in the same notebook says in its own
detail line that the direct target is "inferred from independent full record".
All of that is true, and it is a fact about that lineage only. A different one,
the abstract-domino engine `ENGINE_FLUX_su3_domino_d3.py`, computes `b_3`
directly with 251 gates passing.

One lineage was searched, a hole was found in it, and the conclusion was
generalized — the exact failure mode `AGENTS.md` names, committed by the review
doing the catching. The algebra that came with it survives and is now a check:
Hamer's rest-frame series pins `12 leak_3 - 4 b_3` and neither coefficient
alone, because `q(0) = 0`. What separates them is the `lambda = 8` band top,
and the corpus already had it.

## The decisive next test

From the coverage the review leaves behind: an orientation-resolved Weingarten
evaluation at N = 3 and N = 4 returning `A_N` and `B_N` **separately**. It is
the only way to move eq. (18)'s isotropy premise — the single unproved physical
input of the entire second-order chain, and the thing every other statement in
Section 4 rests on — from asserted to derived. The ingredients are already
here: `invariants.py` carries `Wg(e)`, `Wg((12))` and the N = 3 fourth moment
`|U_11|^4 = 1/6`, and the published-comparisons suite already establishes that
the Weingarten route imports nothing from the corpus.
