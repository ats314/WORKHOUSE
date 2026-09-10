# The notes intake

This directory holds **generated inventories** of the maintainer's note
archives — one `<archive-id>.jsonl` per archive declared in
`ledger/notes.yaml`, one line per unique content digest. The manifests are
checked in so the review queue survives the archive being unmounted, and so
"how much is still unreviewed" is a number CI can compute rather than a
feeling.

The judgement lives in `ledger/notes.yaml` (verdicts, reasons, claim links);
the join is derived; the validation is mechanical — the same discipline as
every other register here.

The [September 7 full-root audit](../docs/corpus_coverage.md) adds a wider
content-addressed snapshot, including nested archive members and current
quarantine locators. It uses a pinned independent coverage contract, not the
older text-only `triage` scanner. Extraction metadata and prior-review references
are separate from new review verdicts. Its pending records must remain pending
until actual review; neither similar names nor a historical `ALREADY_REVIEWED`
folder supplies that review.

The queue reuses genuine recorded reviews across archives by exact content
hash. Status output separates reviews recorded in this archive from reused
reviews and names their source archive/verdict. A changed file with the same
name stays pending; `pinned_as` alone is not a semantic review. This prevents
an expanded inventory from requiring the same reviewed bytes to be read again.

```bash
uv run --no-sync workhouse notes                                # status: reviewed / pending, per archive
uv run --no-sync workhouse notes --queue                        # the next documents to review, highest signal first
uv run --no-sync workhouse notes --scan <root> --archive <id>   # write/rewrite the declared inventory
```

## The flow, end to end

1. **Declare** the archive in `ledger/notes.yaml` — id, what it is, where the
   bytes live. Declaring and inventorying are separate deliberate events.
2. **Inventory** with `--scan`. It reads the archive and writes the declared
   JSONL inventory. Preserve the old inventory bytes and digest before an
   intentional rescan; do not rescan a full-root coverage snapshot through the
   older text-only scanner. The underlying `workhouse triage` scanning is
   read-only with respect to source files, groups inventory records by digest
   without deleting duplicates, and ranks signals (files carrying
   registered coefficients surface first; `4**r`-erratum carriers are
   flagged so nobody rescales them).
3. **Review** from the queue. Each verdict is one entry in the register,
   keyed by digest, with a mandatory reason. The vocabulary is closed:
   `import`, `extract`, `duplicate`, `superseded`, `set-aside`.
4. **Incorporate** what earns it. An `import` is verbatim — the destination
   file must hash to the reviewed digest, and landing anything in `theory/`
   still goes through `make manifest` as its own reviewed event. An
   `extract` skips the copy: the note's content enters as registered claims
   or checks, and `bears_on` records which.

After an intentional inventory or review-register change, regenerate the
affected catalogue and views in the [documented order](../CONTRIBUTING.md#verification-by-change-type).
Inspect the diff and the affected `workhouse why` records before publishing.

## In the theory graph

Every inventoried document is a catalogue node (`NOTE:<archive>:<name>-<digest>`),
under an `ARCHIVE:<id>` node that `contains` it. Until 2026-08-28 none of them
were: 1,689 documents with no node, so every `bears_on` a review had recorded
was a sentence nobody could traverse, and "which notes touch C2?" had no answer
the graph could give. It does now.

```bash
uv run --no-sync workhouse why C2          # includes the notes that bear on it
uv run --no-sync workhouse search 'OFF AXIS LEDGER'
```

Archive membership produces `contains` links; review records provide
`bears_on`, `duplicate_of` and `superseded_by`. The `carries` links are
derived **by value**: `triage` records which coefficient signatures a
document's bytes contain, and a signature is the digit string of a registry
constant's own exact numerator and denominator, so a document links to a
constant only when it demonstrably carries that constant's digits — not
because a name map here decided what it was about. That is the same
value-first join the rest of the repository uses, and it means a pending,
never-reviewed document still connects to the constants it touches.

Two things this does **not** do. No node is above **T3**, whatever its verdict:
a verdict records a judgement about a document, never the truth of what the
document says, and `import` is the strongest of them precisely because it
promotes nothing. And no `carries` edge takes a side — a document carrying both
recorded `C_shp` values links to both.

`every declared note document is a graph node with an edge` fails if this
regresses, which is the point: the next archive declared and not regenerated
would otherwise go silently missing.

## What this layer refuses to be

- **A gate that loses things.** Every unique document in an inventoried
  archive is either reviewed (with a reason on record) or counted as
  pending. There is no third state and no silent drop.
- **A trash can.** `set-aside` records a judgement; it deletes nothing. The
  archive keeps the bytes, the register keeps the why, and a later review
  can overturn the verdict with a better reason.
- **A promoter.** No review verdict changes a claim's tier. Note records
  remain T3; the associated mathematical claims have their own status,
  evidence and machine-certification records. Follow the
  [derivation proof map](../docs/derivation_formalization.md) for precise
  formal coverage and [current research](../docs/current_research.md) for
  later results rather than treating the intake date as current status.
