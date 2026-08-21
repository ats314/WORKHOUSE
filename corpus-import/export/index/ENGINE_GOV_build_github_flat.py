#!/usr/bin/env python3
"""
Build GITHUB/ — a flat mirror of the corpus for upload to WORKHOUSE.

Every file is uploaded loose, with no directory structure, and a second agent
reorganizes them inside the repo. So the flat name and the manifest are the only
information that survives the trip. This emits:

  GITHUB/<flat files>          collision-safe names, origin encoded where needed
  GITHUB/_READ_ME_FIRST.md     briefing for the receiving agent
  GITHUB/_MANIFEST.tsv         flat_name, original_path, class, topic, size, md5, title
  GITHUB/_EXCLUDED.tsv         what was left out and why

  python ENGINE_GOV_build_github_flat.py            # dry run
  python ENGINE_GOV_build_github_flat.py --apply
  python ENGINE_GOV_build_github_flat.py --apply --include-npz --include-archive
"""
from __future__ import annotations

import argparse
import collections
import hashlib
import os
import re
import shutil
import stat
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
DEST = os.path.join(ROOT, "GITHUB")
SKIP = {"GITHUB", "__pycache__", ".git", ".ipynb_checkpoints"}
NAME = re.compile(r"^([A-Z]{2,7})_([A-Z0-9]{2,6})_(.+)$")


def md5(p):
    h = hashlib.md5()
    with open(p, "rb") as fh:
        for c in iter(lambda: fh.read(1 << 20), b""):
            h.update(c)
    return h.hexdigest()


def title_of(p, ext):
    if ext not in (".md", ".tex"):
        return ""
    try:
        head = open(p, encoding="utf-8", errors="replace").read(3000)
    except OSError:
        return ""
    m = re.search(r"^#\s+(.{4,110})$", head, re.M) or \
        re.search(r"\\title\{(.{4,110}?)\}", head, re.S)
    return re.sub(r"\s+", " ", m.group(1)).strip() if m else ""


def collect(inc_archive, inc_npz, max_bytes):
    skip = set(SKIP) | {"QUARANTINE"}
    if not inc_archive:
        skip.add("archive")
    kept, dropped = [], []
    for dp, dn, fn in os.walk(ROOT):
        dn[:] = [d for d in dn if d not in skip]
        for f in fn:
            p = os.path.join(dp, f)
            rel = os.path.relpath(p, ROOT).replace(os.sep, "/")
            try:
                size = os.path.getsize(p)
            except OSError:
                continue
            if f.endswith((".pyc", ".pyo")):
                dropped.append((rel, size, "build artifact"))
            elif f.endswith(".npz") and not inc_npz:
                dropped.append((rel, size, "matrix cache (--include-npz)"))
            elif size > max_bytes:
                dropped.append((rel, size, f"over {max_bytes//(1024*1024)} MB"))
            else:
                kept.append((rel, size))
    return kept, dropped


def flat_names(kept):
    """Unique basename wins; otherwise encode the origin directory into the name."""
    counts = collections.Counter(os.path.basename(r) for r, _ in kept)
    out, used = {}, set()
    for rel, _ in kept:
        base = os.path.basename(rel)
        if counts[base] == 1:
            name = base
        else:
            d = os.path.dirname(rel).replace("/", "__") or "root"
            stem, ext = os.path.splitext(base)
            name = f"{stem}__{d}{ext}"
        while name in used:
            stem, ext = os.path.splitext(name)
            name = f"{stem}_2{ext}"
        used.add(name)
        out[rel] = name
    return out


BRIEF = """# READ ME FIRST — briefing for the agent organizing this repo

Every file here was uploaded **flat**. The directory structure it came from does
not exist in this repo yet. Your job is to rebuild it. Everything you need is in
the filenames and in `_MANIFEST.tsv`.

## 1. Filenames are structured metadata

Almost every file follows:

```
CLASS_TOPIC_descriptor[_vN][_YYYY-MM-DD].ext
```

`CLASS` and `TOPIC` are uppercase closed vocabularies; the descriptor is
lowercase. So you can classify the entire repo without opening a single file:

```bash
ls THM_*        # theorem statements
ls *_O4_*       # the fourth-order adjudication — the live research front
ls CERT_*       # machine-emitted certificates
ls ENGINE_*     # runnable scripts
```

| CLASS | | TOPIC | |
|---|---|---|---|
| `DOC` governance / navigation | `THM` theorem | `FLUX` one-plaquette flux band | `O2`–`O6` order-specific |
| `LEM` lemma | `NOTE` unpromoted derivation | `Y4` `Y5` `Y6` symbolic pipelines | `SUN` all-rank |
| `PLAN` campaign plan | `AUDIT` audit / review | `SU2`–`SU6` rank-specific | `OP1` Birman–Schwinger |
| `CERT` certificate | `ENGINE` script | `PMBSF` Lemma Q | `RCAP` rooted capacity |
| `NB` notebook | `RUN` log / transcript | `STRING` string tension | `SHELL6` shell-6 |
| `PAPER` manuscript | `DATA` data / figure | `PENT` pentagonal prism | `HAAR` Haar / Krylov |
| `LIT` external paper | `MAN` manifest | `MC` Monte Carlo | `TROM` tromino |
| `IDX` generated index | | `GOV` infrastructure | `MISC` cross-cutting |

Files named `README.md` are directory-level readmes whose origin directory is
encoded after a double underscore: `README__programs__one_plaquette.md`.

## 2. Rebuilding the original tree

`_MANIFEST.tsv` maps every flat name to its `original_path`, plus class, topic,
size, md5, and the document title where one exists. To restore the tree exactly,
create each `original_path` and move the flat file into it. The md5 column lets
you verify nothing changed in transit.

The original layout was:

```
corpus/      the four-document scientific authority — everything defers to it
theory/      open problems, conventions, citation-safety map, theorems, notes
programs/    active campaigns; hodge_o4_adjudication/ is the live front
numerics/    engines, notebooks, certificates, results, data
papers/      manuscripts (flat-band v1.1; spectral geometry v1.4)
literature/  third-party papers
records/     session log, audits, run logs, transcripts, manifests
export/      the hashed handoff contract + index tooling
```

## 3. Before you touch the mathematics

Read `CLAUDE.md` first — it is short and it is the operating document. Then
`README.md`, then `corpus/MASTER_THEORY_UNIFIED_2026-08-20_v3.md`.

Four things that will bite you otherwise:

1. **Truth status and evidence level are independent.** A claim can be
   analytically exact *and* rest on a disputed input. "Certified" never means
   "proved."
2. **`Y = 2*beta_lat/3 = 4u` in archived sources is a label erratum, not a
   rescaling rule.** Never multiply or divide those coefficients by `4^r`.
3. **One result is actively disputed** — the fourth-order planar coefficient
   `C^(4)`. Two independent computations agree on the axial coefficient and
   disagree off-axis, and **no scalar re-anchoring closes the gap**. Do not
   report them as reconciled. This is the whole point of the current work.
4. **A newer file does not outrank an exact counterexample**, and a file named
   `final` does not override a failed invariant.

## 4. The exact constants are the join keys

This corpus is identified by exact rationals, not concepts — 205 distinct
non-trivial constants across ~1,049 occurrences, some appearing in 39 separate
files. `DOC_FLUX_constants_index.md` lists every one with its symbol, defining
location, and how widely it is cited. No semantic search will retrieve
`20721577909065127111/7250590288602460800`; exact match will.

`ENGINE_GOV_constant_index.py --check` is a linter: it flags every pair of
constants standing in an exact 2x or 4x ratio, which is the shared signature of
the `Y=4u` erratum and the factor-2 metric trap. It currently passes with four
classified pairs. Keep it passing.

## 5. What is not here

`QUARANTINE/` was excluded — material already judged not to belong. Anything
else omitted is listed in `_EXCLUDED.tsv` with a reason.
"""


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--apply", action="store_true")
    ap.add_argument("--include-archive", action="store_true")
    ap.add_argument("--include-npz", action="store_true")
    ap.add_argument("--max-mb", type=int, default=45)
    a = ap.parse_args()

    kept, dropped = collect(a.include_archive, a.include_npz, a.max_mb * 1024 * 1024)
    names = flat_names(kept)
    total = sum(s for _, s in kept)
    encoded = sum(1 for r in names if names[r] != os.path.basename(r))

    ext = collections.Counter()
    extb = collections.Counter()
    for rel, size in kept:
        e = os.path.splitext(rel)[1].lower() or "(none)"
        ext[e] += 1
        extb[e] += size

    print(f"GITHUB/ flat mirror — {len(kept)} files, {total/1e6:.1f} MB")
    print(f"  {encoded} names carry an encoded origin path (collisions)")
    for e, n in ext.most_common(10):
        print(f"     {e:<8} {n:>5} files  {extb[e]/1e6:>8.1f} MB")
    if dropped:
        agg, aggb = collections.Counter(), collections.Counter()
        for rel, size, why in dropped:
            agg[why] += 1
            aggb[why] += size
        print(f"\n  excluded ({len(dropped)} files, {sum(x[1] for x in dropped)/1e6:.1f} MB):")
        for why, n in agg.most_common():
            print(f"     {n:>5} files  {aggb[why]/1e6:>8.1f} MB   {why}")
    if not a.apply:
        print("\n(dry run — rerun with --apply)")
        return 0

    def _force(func, path, _exc):
        os.chmod(path, stat.S_IWRITE)
        func(path)

    if os.path.isdir(DEST):
        shutil.rmtree(DEST, onexc=_force)
    os.makedirs(DEST)

    rows = []
    for rel, size in kept:
        src = os.path.join(ROOT, rel.replace("/", os.sep))
        flat = names[rel]
        dstp = os.path.join(DEST, flat)
        shutil.copy2(src, dstp)
        os.chmod(dstp, stat.S_IWRITE | stat.S_IREAD)
        stem, e = os.path.splitext(os.path.basename(rel))
        m = NAME.match(stem)
        rows.append((flat, rel, m.group(1) if m else "", m.group(2) if m else "",
                     size, md5(src), title_of(src, e.lower())))

    with open(os.path.join(DEST, "_MANIFEST.tsv"), "w",
              encoding="utf-8", newline="\n") as fh:
        fh.write("flat_name\toriginal_path\tclass\ttopic\tsize_bytes\tmd5\ttitle\n")
        for r in sorted(rows):
            fh.write("\t".join(str(x).replace("\t", " ") for x in r) + "\n")

    with open(os.path.join(DEST, "_READ_ME_FIRST.md"), "w",
              encoding="utf-8", newline="\n") as fh:
        fh.write(BRIEF)

    if dropped:
        with open(os.path.join(DEST, "_EXCLUDED.tsv"), "w",
                  encoding="utf-8", newline="\n") as fh:
            fh.write("original_path\tsize_bytes\treason\n")
            for rel, size, why in sorted(dropped):
                fh.write(f"{rel}\t{size}\t{why}\n")

    print(f"\nwrote {len(rows)} files to GITHUB/ ({total/1e6:.1f} MB)")
    print("  _READ_ME_FIRST.md  briefing for the receiving agent")
    print("  _MANIFEST.tsv      flat -> original path, class, topic, md5, title")
    return 0


if __name__ == "__main__":
    sys.exit(main())
