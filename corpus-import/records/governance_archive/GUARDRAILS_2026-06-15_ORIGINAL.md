# GUARDRAILS — agent anti-patterns (learned the hard way)

Every one of these has actually gone wrong in this project. Don't repeat them.

1. **Don't re-impose the Clay / "Yang–Mills solver" frame.** The goal is strong, self-contained results — not a Millennium proof (`CHARTER`, DECISIONS #010). Never tell Alex "this isn't a Clay solution"; he knows, and it isn't trying to be.

2. **Understand structure before opening files.** Read `CHARTER` → `STATE` → the package READMEs first. Grasp the folder *packages*. Do **not** deep-dive individual files to form your mental model — deep reading is for a *scoped task*, not for orientation.

3. **Don't trust status headers.** "PROVEN/ESTABLISHED" banners sit over conditional content in every era. Route through `theory/DOC_GOV_chain_status_map.md`; label every claim by tier (see `AGENT_PROTOCOL`).

4. **Don't spawn new homes.** No new codenamed workspaces, no parallel status docs, no duplicate `ORGANIZED` trees. `C:\THEORY` is the only writable home; everything else is read-only archive. (This is how 200K files across 7 drives happened.)

5. **Don't grade your own proof.** Generation and verification are different jobs. A gate *you* wrote passing is not external validation.

6. **Reproducibility or it doesn't count.** Load-bearing results must rebuild from `C:\THEORY`. "Documented-but-not-reproducible" is flagged, never cited as established.

7. **Time-box meta-work.** Organizing, re-counting, and auditing are means, not the product. A pass that yields only logs — no movement toward a deliverable — failed.

8. **One scoped unit per session.** Don't "review everything." Pick one milestone, finish it, update `STATE`, stop.

9. **Alex owns framing & status.** Propose; don't silently redefine the project or promote a claim's status. Telos changes need his sign-off — that is precisely how this operating layer drifted before.

10. **Honesty over momentum.** Record negative and failed routes; don't bury them. A clean "this doesn't work" beats an optimistic blur.
