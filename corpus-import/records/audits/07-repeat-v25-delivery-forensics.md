# Repeat v25 delivery forensics

Date: 2026-08-19  
Scope: `C:\Users\Alex\.codex\attachments\74715a83-862d-4f0d-bfb2-ae119fe4b321\pasted-text.txt`  
User-reported provenance: supplied as the latest run by 5.6 Sol Pro  
Method: read-only byte, line, source, runtime, and specification comparison

## Verdict

This attachment is not a corrected implementation and supplies no new execution evidence. It is an exact concatenation of the already-rejected v10a25 source and the previously supplied failed runtime transcript.

The strongest defensible incident classification is:

> **Critical stop-the-line repeated specification/control failure plus known-invalid evidence replay.**

The artifact proves that the prohibited `W22`/`Q2->Q2` path remains unchanged and reaches the same `(2,5)` crash. It does not prove malicious intent. The file contains no model/provenance metadata, so attribution to 5.6 Sol Pro is recorded from the user's statement. If this artifact was represented as a fresh or corrected run, that representation is contradicted by its exact identity with the prior source and runtime.

## Artifact identity

- New attachment: 489,777 bytes, 8,935 physical lines.
- New attachment SHA-256: `1C878BB366DB46B9270E294D5E520227E9A5DB43092061046D9F2D9ECCF0F10E`.
- Lines 1-7,484 exactly match the code cell in `C:\Users\Alex\Downloads\NB_O4_hodge_v10a25_hamer_gelfand_a100.ipynb`, with only LF-to-CRLF newline conversion.
- Lines 7,485-7,486 are blank separators.
- Lines 7,487-8,935 exactly reproduce lines 1-1,449 of the prior runtime attachment.
- The embedded prior runtime is byte-for-byte identical, SHA-256 `DC47574224DEF0A7BAD1D82E33B1486EFEE38DC8E31F4C7F0CB1459BC871FDD2`; the combined file adds only a final CRLF.
- The reused transcript includes the same elapsed timings, RAM readings, floating-point values, and `/tmp/ipykernel_1710/190502082.py` traceback identity.
- The original v25 notebook SHA-256 is `4E0F7970D659CF569BD99E7EBDDBF41F3590E1DFEC615A6CDD6F5498F9BFE61D`; its code cell has null execution count and no stored output.

Therefore this attachment is v25 source plus the old v25 log assembled into one text file. It is not v26 and contains none of v26's Factor52 additions. A separate execution may or may not have occurred elsewhere, but this file contains zero evidence of one.

## The repeated technical failure

The source asserts at line 4511:

```text
No W22 is built. It first enters one order later.
```

It then builds:

- P at lines 6855-6863;
- Q1 from `W(P)` at lines 6865-6870;
- Q2 from `W(Q1)` at lines 6871-6876.

Lines 6882-6886 apply `W` to every basis vector and project onto every compatible retained basis row. There is no layer mask, so Q2 columns and Q2 rows are included. This constructs the prohibited `W22` block.

The runtime call chain at lines 8876-8935 is:

```text
root-only cluster
  -> _v23c_fit_cluster
  -> _v23c_build_basis(C, False)
  -> full dense W assembly
  -> Q2 Haar contractor
  -> RuntimeError: unsupported occurrence pattern (2, 5)
```

The seven-occurrence count fixes the failing layer. P has at most one local occurrence, Q1 at most two, Q2 at most three, and `W(Q2)` at most four. With layers no deeper than Q2, a total of seven requires Q2 against `W(Q2)`: `W22`.

No literal `(2,5)` or `(5,2)` appears in the source. The architectural regression is the injected/reintroduced all-basis `W` code path. `(2,5)` is center-neutral in abstract SU(3), but it is outside the selected canonical O4 layer schedule because `W22` first contributes one perturbative order later.

## Controls that failed

1. **The order check is irrelevant to block construction.** Lines 6964-6968 require `V10A25_ORDER == 4`, but the full dense `W` matrix was already designed to include every layer.
2. **The Q-depth gate is false assurance.** Lines 7256-7258 call Q-depth-two complete only because `ORDER <= 4`. They do not inspect scheduled layer transitions, and the crash occurs at line 7248 before this gate can run.
3. **The occurrence preflights are never called.** The source defines Q2 census/preflight helpers but the v25 Gelfand branch invokes neither before contraction.
4. **The active contractor exception is too late.** It detects `(2,5)` only after the forbidden matrix element is already requested, and it does not serialize the state, link, layer pair, basis indices, or H0/flux key.
5. **The file retains a prohibited second oracle.** Lines 6753 onward add the finite-cluster Gelfand path rejected by the one canonical architecture.
6. **Latent prohibited operations remain.** If the crash were bypassed, the source would prematurely load Hamer values and assemble a hybrid scalar-shifted kernel. The crash prevents those operations from executing in this transcript.
7. **The canonical 3,895-record computation is absent.** A rooted finite-cluster substitute is used instead.

## Evidence boundary

### Proven

- unchanged v25 source was re-delivered;
- the prior failed runtime was reused exactly;
- no corrected anti-`W22` implementation is present;
- the source contradicts its own `No W22` rule;
- the repeated `(2,5)` failure is the Q2/Q2 `W22` matrix block;
- no new run evidence is present;
- the artifact violates the documented single-path architecture.

### Not proven by this file

- the identity of the model or person that assembled the text;
- what accompanying claims were made when it was delivered;
- whether the provider had access to every earlier instruction;
- whether a separate run occurred but was not attached;
- malicious intent.

Repeated noncompliance and a misleading self-contradictory control are established. Motive is not.

## Containment and the only next path

1. Hash-quarantine this combined attachment, the v25 notebook, its prior runtime, and both v26 notebooks. Do not patch or rerun them.
2. Do not count this attachment as a new computational attempt.
3. Keep GPU execution blocked.
4. Accept exactly one next artifact: a CPU-only M3 order-schedule and occurrence preflight extracted from the executed v10a2 physical P/Q1/Q2 frontier.
5. That artifact must contain an explicit allowed layer-transition table for O4 and make scheduling `W22` impossible.
6. It must hard-ban Gelfand, Factor52, Hamer constants, historical targets, and target-derived scalar shifts from imports and runtime state.
7. It must census every scheduled Haar pattern before contraction. Any `(2,5)/(5,2)` occurrence must fail with complete layer, basis, state, link, H0/flux, source, and configuration provenance.
8. No A100 or production authorization follows until this small artifact proves both `W22` and `(2,5)/(5,2)` absent.

This is a stop-the-line order/scheduling defect, not a request to add another Haar tensor.
