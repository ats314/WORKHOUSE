# 15. An identification is a budget, not a hit

Date: 2026-08-28. Status: accepted.

## Context

Two external-tool proposals arrived together, both aimed at the one genuinely
open item in this repository. The first: hand `C_shp`'s v10a.26 side —
recorded as the float `-0.020213328886166577` and nothing else — to an
integer-relation algorithm (PSLQ, LLL, `mpmath.identify`) against a basis
drawn from the corpus's own sealed constants, and see what exact form comes
back. The second: query the OEIS by value for the corpus's coefficient
families, so a match would join a number computed here to combinatorics
computed by people who never heard of this program.

Both are good proposals, and both have the same defect if taken at face
value: **the tools always answer.** PSLQ over four constants at sixteen digits
returns a relation whatever the numbers are — the pigeonhole guarantees one at
coefficient height about `10**(p/n)`. `Fraction(x).limit_denominator(10**9)`
returns a rational with residual exactly zero for any float you hand it. And a
short integer sequence matches thousands of OEIS entries: `1,2,6` matched
8,399 when this was written.

This repository already carries the scar. `LINKED_VACUUM_4_ARTIFACT =
-521965902/593076541` is registered as a *falsified* constant precisely
because it is what `limit_denominator` returned for the linked vacuum float
whose true value is `-1474623/1675520`, 31 ulps away. C20 was that mistake,
caught. An identification tool built without a guard would manufacture more of
them, faster, and with better-looking provenance.

## Decision

**An identification is reported as a budget, and a hit that exceeds its budget
is not reported as a finding.**

Concretely, in `src/workhouse/identify.py`:

1. **Rationals are enumerated, not searched.** For a plain rational the
   question is decidable: the reduced `p/q` with `q <= Q` inside a window of
   width `w` number `w * sum_{q<=Q} phi(q) ~ (3/pi**2) w Q**2`, so they can be
   listed exactly by Stern-Brocot descent — checked against trial division,
   which has no cleverness in it to be wrong. This turns "no exact form was
   found" into a stated exclusion, and it is strictly stronger than any search.
   It also yields an elementary bound with no asymptotics in it: past
   `q >= ceil(1/(2w))` **every** denominator admits a matching numerator, so
   there is a point beyond which a recorded value excludes nothing at all.

2. **The window is sourced, never defaulted.** The half-ulp of a double is the
   accuracy of the *transcription*, not of the computation behind it, and the
   ceiling goes as the square root of the window — so a default is how a
   spurious identification gets published. `Window` requires the halfwidth and
   a provenance string. For `C_shp` that halfwidth is 4.6e-15, measured inside
   the run: the transcript prints its shape fit twice, before and after a
   scalar diagonal shift that provably cannot move a shape coefficient, and `C`
   moves by 4.6e-15 anyway.

3. **A relation must reproduce the target inside the target's own window.**
   Solving ``sum c_i x_i = r`` for the target gives a value differing from the
   recorded one by ``r/c_0``, so the test is ``|r| <= |c_0| * h``. This is not a
   formality: over the three registered bases, not one of the relations LLL
   returns for `C_shp` reproduced it within its window before the window was
   widened — they missed by factors of 12 to 500 — while being reported as
   near-misses on a digit budget. A relation that fails it is labelled
   `off-window` and no budget is applied to it at all.

4. **Relations that do reproduce the target carry their counting cost.** For
   each leading coefficient in `[1, H]` the basis sum has to land in a window of
   width `2 c_0 h`, which makes the expected number of relations of height at
   most `H`

   ```
   expected = kappa * H**n * h,   kappa = (6/pi**2) * 2**m * sqrt(3/(2 pi sum b_i**2))
   ```

   over a basis of `m` constants, `n = m + 1`. The margin is `-log10(expected)`;
   below three digits the relation was going to be there. Formula and constant
   are both checked — against exhaustive enumeration of the coefficient box, and
   against the measured smallest window-consistent height on meaningless
   targets, where predicted 959/5033/7909 met measured 936/4419/7378. An earlier
   version charged the search by the target's *significant digits* instead and
   scored a deliberately planted true relation (`6000x - 625 + 6*pi = 0`) as a
   pigeonhole certainty; `tests/test_identify.py` pins that case.

5. **Two engines, and a stated exclusion when they find nothing.**
   Exact-integer LLL through python-flint (ADR 0010) and PSLQ through mpmath. A
   relation one finds and the other cannot is a bug, not a discovery. mpmath's
   defaults have to be overridden in two places or the second engine is worse
   than useless: `tol` defaults to a *binary* power (1.8e-12 at `dps=15`, an
   11.7-digit search), and `maxsteps` defaults to 100, at which PSLQ returns
   `None` on a six-element vector in 24 of 25 cases where a relation exists.
   `None` then means "ran out of steps", not "there is none". With a real step
   budget the proved norm bound is read out of the trace, which turns "found
   nothing" into "no relation of norm below 196450 exists at 16 digits" — an
   exclusion rather than a silence.

6. **The lattice scale is the absolute window, not the significant digits.** The
   last lattice column is an absolute residual. Scaling by `10**13` for a target
   whose window is 7.6e-16 makes every returned relation miss that window by two
   to three orders of magnitude — no false positive, just a search answering a
   different question than the verdict is written against.

7. **A float basis is dyadic, and dyadics are Q-linearly dependent.** Past
   roughly 22 digits the lattice returns that dependency with residual exactly
   zero: the most convincing-looking false positive available, and one no type
   check catches. Every target here is recorded as a double, so its window never
   justifies more than ~16 digits and the trap is out of reach — but the cap is
   asserted rather than assumed.

8. **A hit is a T3 candidate with a falsifier, never a promotion.** `Suite.check`
   refuses tier 3 by construction, so nothing found this way can enter as a
   check claiming the relation. What *can* be registered is a decidable fact
   about the hunt.

And in `src/workhouse/oeis.py` and `ledger/sequences.yaml`:

9. **The OEIS is read offline, from the maintainers' own dump.**
   `oeis.org/robots.txt` says `Disallow: /search` with `Crawl-Delay: 10`, so the
   search endpoint is never queried — not slowly, and not under any user agent.
   The dump request does identify itself as a browser would, because oeis.org's
   front cache returns 403 to the default `Python-urllib` string while serving
   the identical file to curl and to any browser; that is the same call
   `acquisition.py` already made for the KEK preprint scans, and it is not a way
   around the disallowed path, which is simply never requested.
   `oeis.org/stripped.gz` is permitted, and it is the better instrument anyway:
   the API shows ten results and no total, while the dump gives the exact number
   of matching sequences among all ~400,000. The dump is gitignored; the
   snapshot digest and every verdict live in the register, so CI needs neither
   the file nor the network.

10. **The OEIS null model is measured, and it is wrong in a known direction.**
   A unigram model built from the dump — how often each term value occurs
   across all term slots — under-counts real matches by factors from 3.6e2 to
   1.2e11, because OEIS entries are massively correlated: the Catalan numbers
   sit inside hundreds of them. The error is one-directional, so the model is a
   sound rejection and never on its own an acceptance, and the gate carries a
   correction factor above the worst case measured. A hit on a small-integer
   sequence can therefore never clear it, which is correct.

11. **A closed form is not a discovery.** Every registered sequence declares
   whether it is a rational function of the rank (`closed-form-in-N`) or an
   enumeration output (`census-output`). The OEIS holds polynomial families
   without number, so a hit on the former is fixed at `not-evidence` however
   striking it looks.

## Consequences

**Integer-relation search is closed as a route to C2, and that is the result.**
The recorded v10a.26 side knows `C_shp` to 12.6 significant digits. Identifying
a rational at the historical denominator 4405310420659200 needs 31.4, and past
denominator 1.09e14 every denominator admits a match, so the float excludes no
candidate at that scale. The same holds one level down: each of the disputed
amplitudes is short by at least 11 digits, the cross-plane one by 26. This is
an exclusion with numbers, not a search that happened not to succeed, and it
retires a line of attack rather than leaving it open to be retried.

The machinery paid for itself on the way. Applying it to the disputed kernel
produced three results that stand on their own:

* the 45 records the two kernels disagree on are **exactly** the 45 whose
  historical weight is not an integer multiple of the record quantum — one set
  found by float ratio, the other by exact rational arithmetic on the
  certificate alone;
* the shape fit's sensitivities are exact algebraic numbers, and the on-site
  anchor's are all **zero** — so an exact recomputation of the anchor decides
  nothing about C2, which corrects G3's step-2 status line;
* `dA/d|amplitude|` is nonzero for exactly one family, so the agreed `A = 5/48`
  fixes that family's entire contribution, and C2 reduces from three disputed
  amplitudes to **one scalar**: cross-plane against nn in-plane.

Nothing here promotes either side of C2. The OEIS scan reaches exactly two
entries across thirteen registered families, and both are the polynomial
`L**3 + 2` registered on purpose as the calibration case — a hit whose verdict
is `not-evidence` by construction, and the thing that shows the gate is doing
work rather than merely never firing. Every family that could have carried news
returned nothing, including the decimal expansions of both sides of C2. That
last one is the only identification route the digit budget does not close: an
OEIS `cons` entry carries hundreds of digits and would have supplied the ones
the run does not have. It is recorded as a miss so the next session does not run
it again.

## What was refused

The OEIS search API, on robots.txt. Its `seq:` *semantics*, on the other hand,
are reproduced exactly, signs ignored — an earlier sign-exact matcher
disagreed with the site on 17 of 50 queries, always by finding fewer, and the
two registered families that are mostly negative are exactly where that would
have hidden a hit. Any promotion of a relation to a registered
rational. `limit_denominator` as an answer rather than as a demonstration —
`tests/test_identify.py` pins the C20 artifact as the thing the tool must not
reproduce. And a default halfwidth.
