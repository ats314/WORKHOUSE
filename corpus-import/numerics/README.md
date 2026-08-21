# numerics — engines + data that re-verify the computational claims

One subdirectory per engine family. Currently: `op12_theta/` — the OP-12 θ-scan with exact kernel constants (M1), pair certificates (M2), scaling tables (M4), and the red-Davies chain comparison (F020); `clay_verify/` — the Clay submission's CODE/VERIFY scripts, archived copies + first recorded run (F022; ungated demos — see its README before citing anything from them); `cw_extractor/` — recovered authoring notebook for PROOF_04's c_W constant (F023; **unrun/unverified** — gate-wrap before use). See each README.

House rules (CLAUDE.md rules 4, 7): every engine ships hard-failing gates (assert, never soft warnings); long jobs are deadline-chunked and resumable; documents cite the gate run that backs each claim; results notes live beside their engines, dated.
