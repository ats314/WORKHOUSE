# Runtime forensics: `(2,5)` in v10a25

Date: 2026-08-19  
Scope: `NB_O4_hodge_v10a25_hamer_gelfand_a100.ipynb` and the separately supplied `pasted-text.txt` runtime transcript  
Method: read-only source/runtime tracing, version comparison, and comparison with the executed v10a2 physical-Q frontier

## Verdict

The `(2,5)` value was not a literal inserted into v25 source. It was generated deterministically because the newly appended Gelfand finite-cluster builder constructed a `Q2<->Q2` (`W22`) matrix block. That block is one magnetic step beyond the selected fourth-order calculation, and the same inherited source explicitly says: `No W22 is built. It first enters one order later.`

This is a concrete order-boundary and instruction-compliance failure. v26 then takes the wrong corrective direction: it leaves the `W22` construction in place and adds a `(5,2)/(2,5)` contractor so the fifth-order workload can proceed. The canonical O4 repair is to remove `W22`, not to support Factor52.

The artifacts establish this technical failure. They do not establish malicious intent. The user reports that this is the sixth recurrence; the available retained conversation/memory search did not recover the earlier five instances, so that count is recorded as user-reported rather than independently verified here.

## Evidence identity

- Runtime transcript: `C:\Users\Alex\.codex\attachments\40f03d3f-bb13-4c52-8cfa-20bcf5d1df96\pasted-text.txt`
- Transcript SHA-256: `DC47574224DEF0A7BAD1D82E33B1486EFEE38DC8E31F4C7F0CB1459BC871FDD2`
- Transcript size: 170,970 bytes, 1,449 lines
- v25 notebook SHA-256: `4E0F7970D659CF569BD99E7EBDDBF41F3590E1DFEC615A6CDD6F5498F9BFE61D`
- v26 notebook SHA-256: `96E3263BCA6534E6E598FEC07F2310EAF88EB48266C0B7EAE17CBEC26D0DC9CA`

The saved v25 notebook has null execution metadata and no stored outputs, but the external transcript is genuine execution evidence. It completes the folded-H4 leg, reports 189 blind records, enters the new Gelfand firewall, and then crashes. There are no earlier `[FAIL]` records in the transcript.

## Exact failure path

The transcript records the following sequence:

1. The folded-H4 leg reports 189 records at transcript line 1376.
2. The Gelfand branch starts for root face 0, polarization 2 at line 1382.
3. The first root-only one-particle cluster calls `_z0=_v23c_fit_cluster(_C0)` at lines 1390-1398.
4. `_v23c_build_basis(C,False)` builds the restricted basis at lines 1400-1405.
5. Its dense `W` assembly projects a generated block against a retained basis state at lines 1407-1412.
6. The state inner product reaches `haar(a,b)` at lines 1428-1438.
7. `_canon` raises `Q2 Haar unsupported occurrence pattern (2, 5)` at lines 1442-1449.

The crash is on the smallest root-only cluster, before the disconnected-spectator fit. It is therefore not evidence of a missing geometric cluster class.

## How the pattern is generated

In v25 logical code:

- `lx_combine_bra_ket` conjugates the bra and joins its occurrences to the ket at lines 504-507.
- `_canon` groups those occurrences per link and defines `pat=(len(U),len(B))` at lines 4174-4181.
- The installed contractor supports only `(1,1)`, `(2,2)`, `(3,3)`, `(3,0)`, `(0,3)`, `(4,1)`, `(1,4)`, `(6,0)`, and `(0,6)` at line 4172.
- Every other center-neutral pattern raises at line 4188.

There is no literal `(2,5)` or `(2, 5)` in v25 source. The pair is runtime state-algebra output. Since `2-5=-3`, it is center-neutral; center neutrality alone does not make it part of the fourth-order workload.

## Root cause: v25 builds the forbidden `W22` block

The finite-cluster builder creates layers:

- P at logical lines 6855-6863;
- Q1 from `W(P)` at 6865-6870;
- Q2 from `W(Q1)` at 6871-6876.

It then ignores the stored layer labels and applies `W` to every basis column while projecting onto every compatible basis row at lines 6882-6886. This includes Q2 against `W(Q2)`: `W22`.

The seven local occurrences identify the layer provenance:

- P carries at most one occurrence per link;
- Q1 at most two;
- Q2 at most three;
- `W(Q2)` at most four;
- a combined seven-occurrence `(2,5)` pair therefore requires Q2 against `W(Q2)`.

For the selected O4 path, the deepest closed magnetic route is:

```text
P -> Q1 -> Q2 -> Q1 -> P
```

Adding `Q2 -> Q2` is a fifth magnetic step. The inherited v10a3/v25 source states at logical line 4511 that `W22` first enters one order later. v25's new builder contradicts that rule.

The canonical v1.4 text independently states that a fourth-order word contains at most six character factors (`p+q<=6`). The project text does not explicitly prove that those character-factor counts are identical to `_canon`'s local `len(U),len(B)` counts, so this is supporting rather than standalone evidence. The direct layer trace above supplies the implementation-level bridge for this failure.

## Executed canonical-frontier evidence

The stored v10a2 run, `sources/NB_O4_hodge_v10a2_fullt1_k2_q2_frontier_a100.ipynb`, executed cell 2, reports:

- 52,608 new-Q2 actions;
- 4,524 unique canonical frontier networks;
- observed Q2 Haar pairs exactly `(0,3)`, `(0,6)`, `(1,1)`, `(1,4)`, `(2,2)`, `(3,0)`, `(3,3)`, `(4,1)`, `(6,0)`;
- no `(2,5)` or `(5,2)`;
- the explicit support gate passes;
- all 17/17 v10a2 gates pass.

This run proves the configured canonical Q1-to-Q2 frontier does not require Factor52. It does not by itself prove a universal SU(3) impossibility; the order-aware `W22` trace is what makes Factor52 irrelevant to this O4 failure.

## The missing preflight

V25 contains `_v10a2_q2_frontier_census` at logical lines 4325-4364. It computes the set difference between observed pair patterns and supported patterns. Static call inspection shows that neither this census nor `v10_q2_preflight` is invoked by v25's new finite-cluster branch. The code reuses the contractor's label “already-certified,” but its startup gates certify selected tensor identities, not coverage of the newly appended workload.

## Why v26 is not the fix

The v24c-to-v25 change keeps the old contractor and adds the all-basis finite-cluster `W` build. V26 keeps that build and reroutes finite-cluster inner products to a new contractor with a `(5,2)/(2,5)` branch. It therefore normalizes the O4-forbidden `W22` workload rather than restoring the order boundary.

No Factor52 implementation belongs in the one canonical fourth-order system.

## One corrective path

There is one path forward:

1. Retire the v25 Gelfand tail and the entire v26 Factor52 tail from production.
2. Start from the executed v10a2 physical P/Q1/Q2 frontier.
3. Use a typed, order-aware block schedule that permits only the blocks required for `P -> Q1 -> Q2 -> Q1 -> P`; make scheduling `W22` impossible at O4.
4. Before any Haar contraction, census the actual scheduled workload and enforce `p+q<=6` plus the executed v10a2 supported-pattern set.
5. If `(2,5)/(5,2)` appears, stop immediately and serialize the layer pair, basis indices, H0/flux key, link, and both `LXState` objects. Do not expand the contractor.
6. Continue through the one canonical Hermitian SW/BCH and 3,895-topology path only after that preflight passes.

Do not run v25 again, do not run v26, and do not create v27. The next runnable artifact should be the small order-schedule/occurrence preflight for the single canonical runner, not another appended notebook.
