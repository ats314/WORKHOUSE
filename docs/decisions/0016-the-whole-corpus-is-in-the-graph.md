# 16. The whole corpus is in the graph, one node per pinned file

Date: 2026-09-01. Status: accepted. Reverses the scope limit in ADR 0009.

## Context

ALL THEORY was imported on 2026-08-20 as `corpus-import/`, 928 files pinned by
digest. ADR 0009 then reached the graph into it through `ledger/provenance.yaml`
— a handful of curated originating documents — and kept the rest out, on the
argument that a corpus file is not a claim. A value index beside the graph
(`workhouse.corpus_index`) recorded every exact rational per file for
`search --corpus`.

Measured on 2026-09-01: 12 of the 929 corpus files were graph nodes. The
maintainer's standing instruction, given more than once to more than one
session, is that the corpus loaded to the repository be reflected in the
graph. It was not, and `why` could not answer "which corpus files carry 5/48"
although the index beside it could.

## Decision

Every file `corpus-import/SHA256SUMS` pins is a catalogue node of kind
`corpus`, keyed on its manifest path, carrying its digest. One archive node
`ARCHIVE:ALL_THEORY_2026-08-20` has a `contains` edge to each. Each file has
a derived `carries` edge to every registered constant whose exact value its
bytes contain — matched through the same scan `search --corpus` uses, so the
graph and the search can never disagree about what a file holds — and a
curated `pinned_as` edge to the provenance document or document alias that
pins it, where one exists. `why <path>` resolves a corpus file by its path.

Every corpus node is T3. The join is by value, never by a name map, and
nothing here promotes a claim. ADR 0006 stands: corpus files do not auto-load
into a session; they are nodes, which is the opposite of loading.

## Consequences

The graph gains 928 nodes and roughly as many `contains` edges plus the value
joins. `why CONST:A_SHP_3` lists the corpus files that carry `5/48`; `derive`
reaches from a claim through its constants into the files that state them;
an intake of a new archive can be judged against the corpus by digest and by
value inside one graph. What it does not do: make any of those files
authority. That rule is unchanged.
