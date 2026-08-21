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

```bash
workhouse notes                                # status: reviewed / pending, per archive
workhouse notes --queue                        # the next documents to review, highest signal first
workhouse notes --scan <root> --archive <id>   # (re)inventory a mounted archive
```

## The flow, end to end

1. **Declare** the archive in `ledger/notes.yaml` — id, what it is, where the
   bytes live. Declaring and inventorying are separate deliberate events.
2. **Inventory** with `--scan`. The scanner is `workhouse triage` underneath:
   read-only, digest-deduplicating, and signal-ranking (files carrying
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

## What this layer refuses to be

- **A gate that loses things.** Every unique document in an inventoried
  archive is either reviewed (with a reason on record) or counted as
  pending. There is no third state and no silent drop.
- **A trash can.** `set-aside` records a judgement; it deletes nothing. The
  archive keeps the bytes, the register keeps the why, and a later review
  can overturn the verdict with a better reason.
- **A promoter.** No verdict changes any claim's tier. A note that bears on
  a claim is still T3 until an invariant or a Lean proof says otherwise —
  the same rule the published literature lives under.
