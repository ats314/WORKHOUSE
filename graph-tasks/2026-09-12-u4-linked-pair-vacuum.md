# Task Record: 2026-09-12-u4-linked-pair-vacuum

## Identity
- **Task ID:** `2026-09-12-u4-linked-pair-vacuum`
- **Date:** `2026-09-12`
- **Agent / Model:** Claude Code (remote session), configured `claude-opus-5`
- **Checkout:** `/home/user/WORKHOUSE` (remote clone; the workstation checkout is `C:\WORKHOUSE\REPO`)
- **Branch / Revision:** `claude/theory-graph-review-8bpt0t`, based on `main` @ `c0b5c27`

## Target
- **Graph IDs:** `G25`, its live route *fourth-order domino, the U4 falsifier*; unifying
  candidate `U4`; ADR 0023.
- **Objective:** compute the connected (linked) two-face vacuum weight `conn_vac`
  at fourth order — the half of U4's fourth-order falsifier that this repository
  carried at T3 — and state exactly what remains.
- **Regime:** finite lattice, strong coupling; two-plaquette cluster sharing one
  link, SU(3) and ℚ(N).

## Start Snapshot
- **Snapshot Path:** `.graph-state/2026-09-12-theory-graph-review/start.json` (this
  session's start observation; `.graph-state/` is gitignored)
- **Fingerprint:** `36a8ece58ab40a49c9944f7a32bb06ba8e8c056c7de3ef1bfe4ea2be26e8efdf`
- **Freshness:** `unknown` at start — no local index-generation record in a fresh clone.

## Established Inputs
- **Reviewed Sources:** `ledger/gaps.yaml` G25 step *fourth-order domino, the U4
  falsifier* (PROGRESS 2026-09-03) and its all-orders half;
  `docs/decisions/0023-the-swap-odd-state-derives-the-c-even-identity.md`;
  `src/workhouse/invariants/swap_odd.py`; `src/workhouse/sixth_order_cluster.py`
  and `src/workhouse/invariants/sixth_order_cluster.py`;
  `runs/g9_direct_h6_pair_2026-09-11/` (`derive.py`, `pair_*_h4.json`);
  `src/workhouse/constants.py` `DECLARED_COINCIDENCES`.
- **Dependencies:** the existing T1 check *fourth-order rotor: gaps 1657/28000 and
  143/8960, vacuum -39/1280, route + vac = -63/800* supplies the disconnected half
  (`-63/800`) and the one-face control (`-39/1280`). Declared as `rests_on`.

## Obligation
- **Investigated Statement:** the linked two-face vacuum weights at orders two,
  three and four, for both shared-link pair geometries; and the consequence for
  `leak_(4,+) - t_(4,+) = 63/800 + conn_A - conn_vac`.
- **Downstream Consequence:** U4's fourth-order falsifier becomes a statement about
  one undetermined number, `conn_A`, with a derived target rather than a
  float-gated one.

## Ownership
- **Owned Files:** `src/workhouse/invariants/swap_odd.py` (one new check plus three
  helpers and imports), `ledger/gaps.yaml` (the G25 step's status, appended —
  the 2026-09-03 text is preserved verbatim beneath it),
  `docs/current_research.md` (one paragraph), this record, and the regenerated
  `FRONTIER.md`, `CERTIFIED.md`, `index/`.
- **Shared Processes:** none. No corpus file, run record, Lean source or theorem
  registration is touched; `theory/` and `runs/` bytes are unchanged.

## Work and Checks

### What was computed
Two independent exact routes to the same cumulant. A two-face cluster has exactly
two proper sub-clusters and both are single faces, so the linked weight is the
two-face vacuum sector minus twice the one face.

1. **SU(3), directly.** `loopcalc` at its default rank through the Bloch
   recursion with the Hermitian metric:
   - one face: `0, 0, -3/4, 9/32, -39/1280`
   - two faces, coplanar and perpendicular alike: `0, 0, -3/2, 9/16, -54321/837760`
   - linked: `0, 0, 0, 0, -327/83776`
2. **ℚ(N).** The retained pair record's vacuum series (word formula, `min_rank` 9)
   against the character engine's one face, for both geometries:

       ω₄(N) = -8 N³ (14 N² - 17) / (3 (N-1)³ (N+1)³ (4N-5) (4N+5) (4N² - 3))

   leading `-(7/12) N⁻⁵`, identical for the two geometries, regular at N = 3 and
   equal to `-327/83776` there.

### What that settles
- `ω₄ = -327/83776` at SU(3) is **derived exactly**, where the repository had only
  the v10a.7 engine's float gate with rational recognition (G25: "T3 here until
  re-derived").
- The linked O(u²) and O(u³) weights are **exactly zero**, as that engine reported
  in floats.
- The weight is the **same for the coplanar and the perpendicular pair** at every
  order through four — the corpus's claim, now exact.
- Therefore U4's fourth-order equality holds **if and only if**
  `conn_A = ω₄ - 63/800 = -173109/2094400`. That target now rests on a derivation.

### Scope limits, stated
- The ℚ(N) route's record is valid for N ≥ 9 (its words carry fluxes up to 8), so
  the closed form is asserted there. Its agreement at N = 3 corroborates the
  continuation; it does not derive the SU(3) value, which rests on route 1.
- The one-face control matters: `-3/4` and `-39/1280` are also the engine-free
  SU(3) fusion rotor's vacuum, a method sharing no primitive with the word
  calculus. Odd orders differ by the sign convention of `V`, which even orders
  cannot see, and the result is an even order.
- Nothing here computes `conn_A`, and nothing here promotes U4 past `supported`.
  A finite exact computation of one cumulant is not the all-orders mechanism.

### Commands Executed
- `workhouse verify --only 'the linked two-face vacuum' -v`
- `workhouse verify` — **683/683 checks passed** (682 before, plus this one)
- `workhouse index -w` (claims 19822, symbols 28, graph 32503), `frontier -w`,
  `certified --write`
- `pytest -q` — exit 0, full suite, no failures
- `ruff check .` clean; `ruff format --check .` 639 files already formatted
- `scripts/check_docs.py` — 42 maintained files, 601 local links, 0 errors
- `workhouse status` — *Ledgers structurally sound*

### Failed attempt, retained
The first plan was larger: compute `leak_(4,+) - t_(4,+)` outright from the pair
cluster's C-even block, which would have decided U4 at fourth order rather than
only sharpening its falsifier. Two things stopped it, and both are worth the next
attempt's time:

- `pair_cumulants` raises `NotImplementedError: family (6,0) on link 1` in the
  excited sector at order four. The fourth-order walk beside a charged neighbour
  reaches a degree-six Haar link family the loop calculus does not implement.
  This is the precise wall on `conn_A`, and it is narrower than the G25 note's
  "SU(3) recoupling coefficients": at SU(3) the `(6, 0)` family is nonzero only
  through the epsilon-tensor invariants that exist because `6 = 2N`.
- The engine's on-site cumulant is **not** the corpus's per-neighbour leakage
  without a proof of identification. Calibrating at order two over ℚ(N):
  `hop_even` equals the registered all-rank `ell_N = A_N + B_N + 1/C_F` exactly,
  but `site_even` does not — it is O(N⁻¹) where `ell_N` is O(N⁻³), and the
  difference `-4N(N⁴-6N²+3)/((N²-9)(N²-1)(N²+1))` carries a pole at N = 3, so the
  two objects treat intermediate states that become degenerate at SU(3)
  differently. Reading `leak` off `site_even` would have manufactured a
  falsification out of a definitional mismatch. Not done.

## End Snapshot
- **Snapshot Path:** `.graph-state/2026-09-12-u4-omega4/end.json`
- **Command:** `workhouse brief G25 --json --out .graph-state/2026-09-12-u4-omega4/end.json`
- **Fingerprint:** `178a1453df8383d81d1c04b01911e39b5e40108fad8ece3ec38f2875479e0e96`
- **Freshness:** `matched`, 683 recorded checks.

## Handoff
- **Established Result:** the linked two-face vacuum weight at fourth order, exact
  by two agreeing routes: `-327/83776` at SU(3) and the all-rank closed form above
  for N ≥ 9, with the linked second- and third-order weights exactly zero and no
  dependence on pair geometry. Registered as one T1 check on the swap-odd suite.
- **Failed Attempts / Obstructions:** the two above, retained rather than deleted.
- **Successor Obligation:** implement the `(6, 0)` Haar family at SU(3) — the
  epsilon-tensor invariants — then compute `conn_A` on the two-face cluster and
  compare with `-173109/2094400`. Equality leaves U4 standing at fourth order;
  inequality ends it at the first order its mechanism cannot reach. Separately, if
  `leak` is wanted from this engine, first prove the identification its on-site
  cumulant needs; the order-two calibration above is the test any such proof must
  pass.
