# Research-folder semantic integration review

Reviewed 2026-09-10 against freshly fetched main baseline `42b0762`. The complete structured report is [research_review.json](research_review.json).

All three research documents are already published in the refreshed baseline. Two match the requested archive bytes exactly; the Feshbach review has a correct newer U7 reconciliation. Correct results are substantially registered. Needed integration repairs are source-to-statement routing and obsolete live gap/route interpretations, not replacement of current main by the older checkout.

All three docs/research files were read in full. Their concrete assertions, hypotheses, historical-status language and machine-check claims were compared to current main's source proofs, result and derivation ledgers, generated catalogue and active Feshbach checks. This is a scoped semantic integration review, not a fresh proof of every dependency or a Lean build.

## What this review changed

- `ledger/gaps.yaml` / `G14.feshbach_channel_2026_09_08`: Replaced R-degree-only/current whole-zone projector interpretation with corrected support result, q>0 scope and finite word-table scope; preserved exact original scalar under historical_feshbach_channel_2026_09_08_before_2026_09_10 and explicit reason.
- `ledger/gaps.yaml` / `G22.resolvent_comparison_2026_09_09`: Corrected two-T1/three-T2 split, inverse-domain/relative-form scope and rho>=1 positivity error; preserved exact original scalar under historical_resolvent_comparison_2026_09_09_before_2026_09_10 and explicit reason.
- `ledger/gaps.yaml` / `U3.cubic_half_derived_2026_09_08`: Corrected cubic support explanation, distinguished scalar momentum dependence from no dispersion, retained unproved proper-return identification; preserved exact original scalar under historical_cubic_half_derived_2026_09_08_before_2026_09_10 and explicit reason.
- `ledger/gaps.yaml` / `G14.plan historical route ROUTE:G14:derive-why-the-fourth-order-dynamics-is--076bf3`: Reframed live task as deriving actual H4 support from histories, including absence of UR/RU and repeated R; dependency is now RESULT:TIER_COLLAPSE_ACTUAL_H4_SUPPORT instead of falsified RESULT:TIER_COLLAPSE_IS_R_DEGREE. Kept state untried. Preserved original step/state/dependencies/cannot_decide under historical_record_before_2026_09_10. Step-derived current route id changes during normal graph regeneration.

No gap, candidate or route state changed. The original three paragraph bodies were independently compared with their pre-edit Git text and retained exactly after line-ending normalization. The historical G14 route text and dependencies are also retained. Current U7 was already correct and is unchanged.

## Source disposition

| Source | Selected main relation | Review conclusion |
| --- | --- | --- |
| `docs/research/next-path-wilson-transfer-2026-09-08.md` | Exact archive match | Keep existing main file; exact archive match. No missing mathematical result found in this research source. |
| `docs/research/september_feshbach_integration.md` | Main has correct newer U7 reconciliation | Keep newer main file. Preserve older archive bytes as provenance. Implemented scoped gap/route repairs; parent owns alias/source integration. |
| `docs/research/spatial-continuum-passage-2026-09-08.md` | Exact archive match | Keep existing main file; exact archive match. All substantive statements already registered; improve precise retrieval. |

## next-path-wilson-transfer-2026-09-08.md

Historical selection of the actual symmetric Wilson marked-shell and uniform Taylor-majorant target. Its opening now points to the completed fixed-spacing continuation; older open-target paragraphs remain evidence of that earlier checkpoint.

**Mathematical scope.** Fixed spatial spacing, SU(3), small magnetic coupling, actual symmetric Wilson transfer and calibrated fundamental-character clock. Current continuation proves complete shell/source construction and common weighted majorant under stated upstream inputs; summed relative carrier transport remains conditional on the same G18/window hypotheses. This is not a spatial continuum result.

**Correct work retained.** The actual transfer operator/clock distinction, fixed-order error plus geometric tail, volume-independent spatial row counting, Gamma degeneracy, full frame versus specified-observable distinction, and temporal versus spatial scope are retained correctly.

**Retrieval or interpretation repair.** The source alias carries only G17/G18/G19 relevance at baseline and does not directly lead to the six completed successor groups. A reader of the historical target can unnecessarily reopen a proved construction.

- Add documentary citations to the Wilson-shell derivation and route-audit alias.
- Link the historical proposal via superseded_by to the precise current shell/source/majorant/transport records; preserve S18_S20 conditional status and the later G19 obligations.
- Explain in the maintained alias note that open-target language is historical, already superseded at the recorded fixed-spacing scope.

**Located source-to-claim mapping.**

- `docs/research/next-path-wilson-transfer-2026-09-08.md`, Opening continuation notice; The theorem to attempt; What success would give: Historical target and precise W1/h,G,S operator/source requirements.
- `docs/derivations/wilson-marked-shell-transport.md`, Sections 2-4, S2-S15: Actual marked cancellation, anchored operator comparison, complete odd shell, holomorphic literal-source chart and Gram bounds.
- `docs/derivations/wilson-marked-shell-transport.md`, Section 5, S16-S17: Cauchy operator bound plus support radius 12n and row count 3(24n+1)^3 gives the common weighted majorant M=187500 M_op and R=R0/(2 exp(12 mu)); intrinsic torus distance includes wrapping.
- `docs/derivations/wilson-marked-shell-transport.md`, Sections 6-7, S18-S22: Finite-order-plus-tail convergence; no summed O(epsilon^2) rate asserted. Conditional carrier gap >(t3/4)u^2q(k) and onto-frame bound 9/16; a specified observable needs its own positive overlap margin.
- `ledger/derivation_statements.yaml`, CITE:WILSON_SHELL: Five source groups proven and S18_S20 conditional under explicit hypotheses; no whole-statement Lean certification is claimed.
- `docs/validation/next-path-wilson-transfer-2026-09-08.json`, Dated route-audit snapshot: Historical target-selection check evidence; registration is not a fresh replay.

Native ids: `CITE:SEPT_DOC_NEXT_PATH_WILSON_TRANSFER_2026_09_08`, `CITE:WILSON_SHELL`, `RESULT:WILSON_INFINITE_PHYSICAL_BAND`, `DERIV:WILSON_MARKED_SHELL_TRANSPORT:S2_S7`, `DERIV:WILSON_MARKED_SHELL_TRANSPORT:S8_S9`, `DERIV:WILSON_MARKED_SHELL_TRANSPORT:S10_S15`, `DERIV:WILSON_MARKED_SHELL_TRANSPORT:S16_S17`, `DERIV:WILSON_MARKED_SHELL_TRANSPORT:S18_S20`, `DERIV:WILSON_MARKED_SHELL_TRANSPORT:S21_S22`.

Archive SHA-256: `72c82dbf0d192bfb5eb180984ee1f20ac3cf066ac3e7988aa7aedf1e98f0e67a`; selected main SHA-256: `72c82dbf0d192bfb5eb180984ee1f20ac3cf066ac3e7988aa7aedf1e98f0e67a`.

## september_feshbach_integration.md

Reviewed exact Hodge carrier calculus and resolvent comparison, preserving valid identities while correcting R-degree-only exclusion, Gamma projector degeneracy, numerical-check tiers and the failed sufficient-margin inference.

**Mathematical scope.** Cubic Laurent identities and exact recorded H4 support; a finite 39-word table through length three; tetrahedral/prism incidence hypotheses; general algebraic/variational resolvent identities under compatible inverse domains with conditional relative-form estimate. These are not higher-order dynamics or a uniform interacting Wilson constant.

**Correct work retained.** All four substantive current RESULT records are already present. The corrected support mechanism proves B=D=0, and the resolvent comparison remains an available analytic input under explicit relative-form and domain hypotheses.

**Retrieval or interpretation repair.** At baseline HODGE_FESHBACH_CHANNEL alias, G14's Feshbach paragraph, G22's resolvent paragraph, U3's cubic-half paragraph and a G14 live route still repeat conclusions explicitly refuted by this review. Main's U7 record itself is already corrected.

- Keep main's newer U7 wording and preserve the archive variant separately.
- Update maintained original-source alias summaries and add explicit links to the corrected review and result ids.
- Retain historical gap paragraphs/route while replacing current interpretations with q>0, actual H4 support, 2 T1+3 T2 and sufficient-margin scope.
- Make the G14 support-explanation route depend on the actual-H4-support result, not the falsified R-degree-only result.

**Located source-to-claim mapping.**

- `docs/research/september_feshbach_integration.md`, Hodge channel: preserved identities and corrected scope: q>0 projector scope; sigma(UR)=sigma(RU)=-2q e2; actual H4 support span {q,q^2,e2}; RR/RUR and finite word-table statements.
- `docs/research/september_feshbach_integration.md`, Hodge-word hypotheses in other cells: Main correctly recognizes registered U7. Tetrahedron/prism carrier eigenvalues are 4/7; prism total Laplacian diag(6,6,5,5,5,5,5) need not be scalar. Proper-return identification remains separate.
- `docs/research/september_feshbach_integration.md`, Resolvent comparison: exact identities and numerical checks: Mixed-pairing identity, oriented sandwich for either coupling sign, rho/(1-rho)^2 sufficient bound; rho>=1 does not prove loss of positivity.
- `ledger/results.yaml`, RESULT:HODGE_FESHBACH_SPLITTING, RESULT:TIER_COLLAPSE_IS_R_DEGREE, RESULT:TIER_COLLAPSE_ACTUAL_H4_SUPPORT, RESULT:FESHBACH_RESOLVENT_COMPARISON: Current result statements already preserve proven analytic results, falsified universal inference and scoped native supports.
- `src/workhouse/invariants/hodge_feshbach.py`, Ten hodge.check definitions including actual H4 support and UR FINDING: Exact controls use Laurent polynomials and actual 189-term kernel reconstruction; normalized carrier exclusions are explicit.
- `src/workhouse/invariants/feshbach_resolvent.py`, Five feshbach.check definitions and _CASES: Two exact controls on four rational finite fixtures; three floating controls. No uniform Wilson kappa supplied.
- `tests/test_september_feshbach.py`, All six regression tests: Counterexample/rank, Gamma degeneracy, 2-T1/3-T2 split, oriented sandwich and rho-margin/positivity boundary.

Native ids: `CITE:HODGE_FESHBACH`, `CITE:FESHBACH_RESOLVENT`, `CITE:HODGE_FESHBACH_CHANNEL`, `CITE:FESHBACH_RESOLVENT_COMPARISON`, `RESULT:HODGE_FESHBACH_SPLITTING`, `RESULT:TIER_COLLAPSE_IS_R_DEGREE`, `RESULT:TIER_COLLAPSE_ACTUAL_H4_SUPPORT`, `RESULT:FESHBACH_RESOLVENT_COMPARISON`, `U7`, `G14`, `G22`, `U3`.

Archive SHA-256: `aa67731fa11cb13c272ed7154f368df49627737678e72f6239d15a0188e9b58c`; selected main SHA-256: `d28bae87bc5bbd3b4e85bd4de45fe7f984132cfed4c39ec8218ca6f54ee2d76d`.

## spatial-continuum-passage-2026-09-08.md

Correct concise synthesis of full-reference Schur excess, complete second-order Wilson/source terms, conditional accumulated physical-gap and source budgets, and the Gaussian comparison obstruction leading to selected-inverse W6.

**Mathematical scope.** Analytic identities and conditional complete-form scale comparison under compatible physical chart/domain, fast floor, direct/force and source remainder, retained energy, induced metric and clock hypotheses. SP11-SP19 jets and SP25 illustrative summability are established at their recorded finite/model scope; actual uniform interacting W6 and continuum construction remain separate.

**Correct work retained.** The entire second-order generated operator and source normalization, physical clock, quadratic memory and selected-inverse repair survive. The displayed gap recursion and illustrative cubic summability are mathematically correct under the recorded premises.

**Retrieval or interpretation repair.** Baseline source alias only bears_on G19/G23; it does not directly expose its precise Schur/selected-inverse records. Its historical local-only publication sentence and two-Lean-lemma count must not be read as current main state.

- Add cites to Wilson spatial/selected derivation and validation aliases, with supported_by or bears_on links to the exact statement groups at their recorded scopes.
- Clarify in maintained alias/review notes that publication status and Lean-count sentences describe September 8, while current source/statement records are already in main.
- Preserve actual interacting W6 and full source/clock/continuum obligations without a blanket claim that all fixed-spacing physical construction is absent.

**Located source-to-claim mapping.**

- `docs/research/spatial-continuum-passage-2026-09-08.md`, All paragraphs, including final publication-status sentence: Correct dated scientific synthesis. The final 'not committed, pushed or merged' is historical publication status superseded by the inspected main baseline.
- `docs/derivations/wilson-spatial-schur-excess.md`, Sections 2-5, SP1-SP19: Full graph, induced metric, cubic remainder reduction, magnetic/electric/Haar/vacuum/moving-source jets and harmonic compact-source effects are explicitly retained.
- `docs/derivations/wilson-spatial-schur-excess.md`, Section 6, SP20-SP24: Multiplying reciprocal-gap recursion by A_(j+1) and telescoping gives the exact bound; complete-frame composition and specified-observable telescoping have distinct premises.
- `docs/derivations/wilson-spatial-schur-excess.md`, Section 7, SP25: For hypothetical g_j^2=kappa/(j+j0), cubic errors have the stated finite integral-comparison budget; quadratic majorant alone cannot guarantee summability. No running coupling is derived.
- `docs/derivations/wilson-selected-inverse-wall.md`, W1-W6: Compact high-character quadratic spectrum versus finitely retained oscillator linear spectrum obstructs global upper relative comparison; selected-force W5 is conditional and actual interacting W6 remains open.
- `ledger/derivation_statements.yaml`, CITE:WILSON_SPATIAL and CITE:WILSON_SELECTED: All six Schur groups and four selected-inverse groups are already source pinned and scoped. Current abstract Schur/Neumann/variational Lean ingredients exceed the old report's two-lemma checkpoint without solving model identification.
- `docs/current_research.md`, Current route table and Supported Track A formalization: Confirms established fixed-spacing progress and newer scoped formal support; avoids reopening analytic results merely because their full model formalization remains unfinished.

Native ids: `CITE:SEPT_DOC_SPATIAL_CONTINUUM_PASSAGE_2026_09_08`, `CITE:WILSON_SPATIAL`, `CITE:WILSON_SELECTED`, `DERIV:WILSON_SPATIAL_SCHUR_EXCESS:SP1_SP6`, `DERIV:WILSON_SPATIAL_SCHUR_EXCESS:SP7_SP10`, `DERIV:WILSON_SPATIAL_SCHUR_EXCESS:SP11_SP16`, `DERIV:WILSON_SPATIAL_SCHUR_EXCESS:SP17_SP19`, `DERIV:WILSON_SPATIAL_SCHUR_EXCESS:SP20_SP24`, `DERIV:WILSON_SPATIAL_SCHUR_EXCESS:SP25`, `DERIV:WILSON_SELECTED_INVERSE_WALL:W1_W3_OBSTRUCTION`, `DERIV:WILSON_SELECTED_INVERSE_WALL:W4_W5`, `DERIV:WILSON_SELECTED_INVERSE_WALL:W6`, `RESULT:WILSON_FLAT_BACKGROUND_FAST_SOURCES`, `RESULT:WILSON_PHYSICAL_SOURCE_RANK_REPAIR`.

Archive SHA-256: `6f2595489eaabb401f025e288ec9bdbb6578111df85df88378fde50ec39328ca`; selected main SHA-256: `6f2595489eaabb401f025e288ec9bdbb6578111df85df88378fde50ec39328ca`.

## Minimal robust ingestion architecture

- `src/workhouse/claims.py`, load_document_aliases and collect citation aliases: Every resolved documents.yaml alias already produces a T3 CITE node; duplicate aliases may legitimately name one review document at different mathematical scopes.
- `src/workhouse/graph.py`, build document alias relationships: Curated cites links target CITE aliases; bears_on, supported_by, cannot_decide and superseded_by accept native graph ids. These existing relations suffice for research/validation routing without promoting a source.
- `src/workhouse/derivation_statements.py`, validate source path and source SHA-256: DERIV inventory deliberately requires top-level docs/derivations Markdown, native CITE identity, digest, section anchor, hypotheses, status and scoped formal links. Preserve this contract; nested source copies and validation JSON should not be forced into DERIV groups.
- `src/workhouse/recent_research.py`, validate, claim_records, edge_records: Recent-campaign registry is source-pinned and has scoped result/route links, but its SOURCE_BASE intentionally restricts it to its preserved September campaign bundle. General folder coverage should not silently broaden this historical source registry.
- `tests/test_documents.py`, test_legend_is_sound and test_explicit_document_citations_resolve_without_promoting_the_source: Existing checks validate existence, closed standing vocabulary, aliases and citation endpoints. They do not require complete representation of the three source folders or machine-validate hashes embedded only in notes.

- Reuse documents.yaml CITE nodes and native document relationships for every selected repository file; keep exact DERIV and RESULT records as the mathematical authority.
- Create a pinned folder-review manifest with one entry per archive path: archive digest/size, selected repository source digest/size, preservation disposition, aliases, source-specific review scope, precise claim ids and locators, and reviewed corrections or historical-status notes.
- Preserve differing archive bytes under the dated run bundle; keep newer valid main sources in their existing paths. Do not promote byte equality to independent scientific support.
- Add completeness and integrity checks: all input folder paths represented, digests/bytes match selected and preserved files, every alias identifies the selected path, every claim endpoint resolves, and review scope is nonempty. Include nested input manifests and README/source copies without claiming they are separate discoveries.
- Emit current document-to-result/DERIV links from the maintained manifest or documents aliases, then regenerate index, frontier and certified in their existing order. Use supported_by only for actual stated support, cites for documentary reference, bears_on for relevance and superseded_by for explicitly replaced historical guidance.

Do not broaden the top-level DERIV contract to validation JSON or count copied source texts as independent proof origins. A source hash identifies bytes; an explicit located claim review supplies semantic scope. T0/T1/T2/T3, mathematical status and evidence level remain independent.

## Verification and limitations

- Archive/main research SHA-256 comparison: **passed**. Two exact matches; one intentional newer U7 wording in main.
- Historical paragraph preservation: **passed**. All three preserved historical paragraph bodies equal git HEAD originals exactly after line-ending normalization.
- git diff --check: **passed**. Owned gap-ledger change checked immediately after edit.
- Focused pytest attempt: **interrupted**. Attempted focused Feshbach/ledger/result tests; interrupted at parent request before completion. Not a passing test report. Consolidated parent verification is authoritative for this integration.
- No Lean build performed by this subagent.
- No new mathematical theorem claimed.
- No generated catalogue edited or regenerated by this subagent.
- No independent fresh replay of all historical controls; parent records consolidated validation and exact publication state.
- All review conclusions are scoped to the three research documents and the dependencies inspected; the other two folders have separate reviewers.
