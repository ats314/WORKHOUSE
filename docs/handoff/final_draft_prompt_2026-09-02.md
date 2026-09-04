You are working in /home/user/WORKHOUSE (GitHub: ats314/WORKHOUSE). Read CLAUDE.md, AGENTS.md and FRONTIER.md first; they bind. Job: produce the final draft of the paper.

STARTING POINT
- paper/workhouse_publication_edition_rev5_2026-08-30.tex is the author's latest article (revision 5, pinned 2026-09-01). It is the text to finish.
- paper/master_paper_2026-08-30.tex is the merged artifact of record. Its fourth-order section is newer than rev. 5's: port from it the subsections "The kernel is six amplitudes" and "Both branches in one basis", and the sharp zone minimum min_{|k|>=r} q = 4 sin^2(r/2) with K = 10.85 / 15.06 (rev. 5 still prints the superseded 17.04 / 23.66).
- paper/README.md explains every file, the two verifiers (verify_publication_core.py, verify_radius2_report.py), make_coverage.py, and how a new edition enters (docs/decisions/0014-a-manuscript-enters-as-pinned-evidence.md).
- docs/referee/final_paper_review_2026-08-28.md and final_paper_2026-08-28.md are the referee reports; rev. 5 already addresses their three items.
- Everything else: ledger/ (contradictions, gaps, symbols, notes), runs/, docs/decisions/, notes/imported/, literature/, and the workhouse CLI (why, search, verify, branches, derive). Query the graph before reading files.

WHAT MUST CHANGE (all of it is in the fourth-order section, the evidence table, and the conclusion; nothing through third order moves)
- C2 now has THREE recorded sides, none promoted: historical -211835444920651/4405310420659200, cold v10a.26 -0.020213328886166577 (float), cluster-assembled -54822624038066723/853010622188524800. Present all three side by side. Never promote one, never average.
- ADRs 0019, 0020, 0021 (docs/decisions/) and runs g3_chain_amplitude_2026-09-02, g3_chain_amplitude_replication_2026-09-02, g3_shared_link_pair_2026-09-02 establish: u = X_QUANTUM exactly (cold dump wrong by 4.13); pi and nu reproduced exactly; rho matches neither kernel; C_shp = -5/96 - u - (rho + pi)/2; A = 5/48 is computed as the cube-completion channel (-5/48 opposite faces, 53/768 adjacent faces); U5 is refuted (eps-sector of rho + pi~ is -55/6936, not -25/512). Say the coefficient now rests on the corner cluster, which no agreed record can validate, and that is why C2 stays open.
- Replace "this edition does not adjudicate" and the conclusion's "decisive next object" with the above; the calculation asked for has been done from primitives.
- Keep the third-order "251/251 cold exact replay" separate from the fourth-order cold dump; the first stands, the second is wrong on u, pi, rho.
- Soften item 3 of the four geography measurements: the third side differs in the rotation orbit, so do not imply the low-weight sector cannot carry the dispute.
- Every new claim gets a \chk{...} whose label is an existing passing check name. Get names from: workhouse why C2, workhouse why U5, workhouse why G3, workhouse why G14, and CERTIFIED.md. Do not invent labels; the guard fails on any label that does not resolve.

RULES (from CLAUDE.md)
No document is authority, only a machine check. Exact stays exact (Fractions/sympy.Rational; floats carry _NUM). Never edit theory/. Never widen a tolerance. Never apply a 4**r rescaling. q_band^(4) and m_Gamma^(4) are differently anchored coordinates, not rival estimates. Runs and paper/ are byte-pinned by SHA256SUMS.

DONE MEANS
- New file paper/workhouse_publication_edition_rev6_<date>.tex (do not edit rev. 5 in place), README row added, SHA256SUMS regenerated over paper/, python3 paper/make_coverage.py run if the edition prints a coverage appendix.
- bash scripts/check.sh exits 0 (this runs the \chk guard and tests/test_paper.py). Then workhouse index -w, workhouse frontier --write, workhouse certified --write.
- Build if a TeX engine exists (tectonic or pdflatex; PR #62 has the bootstrap if not); otherwise say the build was not run.
- Branch from main, commit with the repository's trailer convention, push, open a DRAFT PR using .github's template if present, and do not merge it.
- Report: what changed, which \chk labels were added, what could not be verified.
