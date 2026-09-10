# Task Record: YYYY-MM-DD-<topic>

## Identity
- **Task ID:** `YYYY-MM-DD-<topic>`
- **Date:** `YYYY-MM-DD`
- **Agent / Model:** `<agent-name>`
- **Checkout:** `C:\WORKHOUSE\REPO`
- **Branch / Revision:** `<branch> @ <commit-sha>`

## Target
- **Graph IDs:** `G19`, ...
- **Objective:** `<precise mathematical statement or question under investigation>`
- **Regime:** `finite lattice | infinite volume | continuum | physical observable`

## Start Snapshot
- **Snapshot Path:** `.graph-state/YYYY-MM-DD-<topic>/start.json`
- **Command:** `workhouse brief <TARGET> --json --out .graph-state/YYYY-MM-DD-<topic>/start.json`
- **Fingerprint:** `<sha256>`
- **Freshness:** `matched | stale | unknown`

## Established Inputs
- **Reviewed Sources:** `<paths and sections read>`
- **Dependencies:** `<registered result or lemma IDs>`

## Obligation
- **Investigated Statement:** `<narrow statement>`
- **Downstream Consequence:** `<what discharging this enables>`

## Ownership
- **Owned Files:** `<exact files modified or created>`
- **Shared Processes:** `<coordination with concurrent tasks>`

## Work and Checks
- **Commands Executed:** `<exact commands run>`
- **Outcomes:** `<results and tolerances>`
- **Evidence Paths:** `<retained test outputs or logs>`

## End Snapshot
- **Snapshot Path:** `.graph-state/YYYY-MM-DD-<topic>/end.json`
- **Command:** `workhouse brief <TARGET> --json --live --out .graph-state/YYYY-MM-DD-<topic>/end.json`
- **Fingerprint:** `<sha256>`

## Handoff
- **Established Result:** `<proven theorem or closed route>`
- **Failed Attempts / Obstructions:** `<retracted or falsified routes>`
- **Successor Obligation:** `<next task>`