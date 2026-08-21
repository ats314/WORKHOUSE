# records/runs/

Raw `.log` output from executions. Append-only; never edited.

A log is `Record-backed` evidence at best (corpus §1.2): it shows that something ran and what it printed. It does not establish that the computation was correct, that the inputs were what the document claims, or that the run is reproducible. Bind a log to source and input hashes before treating it as more than a trace.
