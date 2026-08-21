#!/usr/bin/env python3
"""
ENGINE_GOV_plan_rename.py — propose CLASS_TOPIC_descriptor names per NAMING_CONVENTION.md.

Dry run by default. --apply performs the renames, rewrites every inbound textual
reference, and records old->new with MD5 in records/RENAME_MANIFEST_*.tsv.

  python ENGINE_GOV_plan_rename.py                  # tier A, dry
  python ENGINE_GOV_plan_rename.py --tier AB        # + sanitize pass
  python ENGINE_GOV_plan_rename.py --tier AB --apply
"""
from __future__ import annotations

import argparse
import collections
import hashlib
import os
import re
import shutil
import sys
import unicodedata

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
SKIP_DIRS = {"GITHUB", "__pycache__", ".git", ".ipynb_checkpoints"}

# Structural names tools depend on. README.md especially: GitHub renders it
# automatically per directory, and renaming it silently breaks that everywhere.
STRUCTURAL = {"README.md", "readme.md", "_MANIFEST.tsv", "_EXCLUDED.tsv",
              "MAN_FLUX_manifest.md", "NOTE_MISC_requirements.txt", "Makefile", "LICENSE",
              "pyproject.toml", "setup.py", "__init__.py"}
ROOT_GOVERNANCE = {"CLAUDE.md", "INDEX.md", "STATE.md", "SOURCES.md",
                   "DECISIONS.md", "NAMING_CONVENTION.md"}

TEXTUAL = (".md", ".tex", ".py", ".ipynb", ".json", ".txt", ".yml", ".yaml",
           ".sh", ".csv", ".tsv")

TOPIC_RULES = [
    ("PMBSF",  r"pmbsf|lemma[_ ]?q|\blci\b|tosj"),
    ("RCAP",   r"rooted[_ ]?cap|projected[_ ]?capacity|peierls|source[_ ]?stab"),
    ("OP1",    r"\bop-?1\b|op_?12|defect[_ ]?spars|birman|schwinger|theta[_ ]?scan"),
    ("PENT",   r"pentagon"),
    ("SHELL6", r"shell[_ ]?4?6"),
    ("TROM",   r"tromino|domino"),
    ("HAAR",   r"haar|krylov|feshbach|resolvent|intertwiner"),
    ("MC",     r"monte[_ ]?carlo|spatial[_ ]?mc|ensemble|polarization"),
    ("STRING", r"string[_ ]?tension|sigma[_ ]?\d|torelon|\bkps\b"),
    ("Y6",     r"\by6\b|y_?6_|\bm6\b|sixth[_ ]?order"),
    ("Y5",     r"\by5\b|y_?5_|\bm5\b|fifth[_ ]?order"),
    ("Y4",     r"\by4\b|y_?4_"),
    ("O4",     r"\bo4\b|o_?4_|fourth[_ ]?order|marked[_ ]?cluster|v10a|"
               r"\bc4\b|\bq4\b|hodge[_ ]?pencil|189"),
    ("O3",     r"third[_ ]?order|\bo3\b"),
    ("O2",     r"second[_ ]?order|\bo2\b"),
    ("SU6",    r"su_?6|su\(6\)"),
    ("SU5",    r"su_?5|su\(5\)"),
    ("SU4",    r"su_?4|su\(4\)"),
    ("SU3",    r"su_?3|su\(3\)"),
    ("SU2",    r"su_?2|su\(2\)"),
    ("SUN",    r"su_?n|su\(n\)|all[_ ]?rank|n-?ality|walled[_ ]?brauer|large[_ ]?n"),
    ("FLUX",   r"flat[_ ]?band|flux|glueball|incidence|plaquette|band[_ ]?shape|"
               r"hodge|spectral[_ ]?geometry|mobility|syzygy|homolog"),
    ("GOV",    r"governance|charter|guardrail|protocol|session|reorg|decision|"
               r"naming|state\b|sources|provenance|quarantine|handoff|workhouse"),
]

# Name patterns win over directory: a theorem inside papers/ is still a theorem.
CLASS_BY_NAME = [
    (r"^lemma[_ ]|_lemma_",                        "LEM"),
    (r"theorem|_thm_",                             "THM"),
    (r"erratum|errata",                            "AUDIT"),
    (r"audit|review|forensic|reconciliation|_report|verification_status",
                                                   "AUDIT"),
    (r"closure[_ ]?route|closure[_ ]?plan|milestone|roadmap|program_index|"
     r"_plan\b|preregistration",                   "PLAN"),
    (r"certificate|_cert\b",                       "CERT"),
    (r"manifest|md5sum|checksum",                  "MAN"),
    (r"changelog|conventions|chain_status|_index\b|_map\b|_guide\b|design",
                                                   "DOC"),
    (r"paper|manuscript",                          "PAPER"),
    (r"transcript|_run\b|_log\b|results?$",        "RUN"),
]

CLASS_BY_DIR = [
    ("theory/theorems/", "THM"), ("theory/notes/", "NOTE"),
    ("theory/conjectures/", "NOTE"), ("records/audits/", "AUDIT"),
    ("records/transcripts/", "RUN"), ("records/runs/", "RUN"),
    ("papers/", "PAPER"), ("literature/", "LIT"),
]

CLASS_BY_EXT = {
    ".py": "ENGINE", ".sh": "ENGINE", ".ipynb": "NB", ".log": "RUN",
    ".json": "CERT", ".csv": "DATA", ".tsv": "DATA", ".npz": "DATA",
    ".png": "DATA", ".jpg": "DATA", ".pdf": "PAPER", ".tex": "PAPER",
    ".docx": "PAPER", ".zip": "DATA", ".gz": "DATA", ".txt": "NOTE",
    ".md": "NOTE",
}

DATE_ISO = re.compile(r"(20\d{2})-(\d{2})-(\d{2})")
DATE_COMPACT = re.compile(r"(?<!\d)(20\d{2})(\d{2})(\d{2})(?!\d)")
VERSION = re.compile(r"[_\-. ]\b(v\d+(?:[_.]\d+)*[a-z]?\d*)\b", re.I)
COPY_SUFFIX = re.compile(r"\s*\(\s*(\d+)\s*\)")
HOSTILE = r"""#=(){}\[\],'"!$&;:@+~`^%"""
# A stem is uninformative if it is mostly hex/uuid or a bare "untitled"
UNINFORMATIVE = re.compile(r"(compass_artifact|untitled|copy[_ ]of|^[0-9a-f\-]{16,}$|"
                           r"wf-[0-9a-f\-]{8,})", re.I)
STOP = {"the", "of", "and", "for", "a", "an", "to", "in", "on", "with", "its",
        "complete", "final", "new", "copy", "text", "markdown", "document"}


def md5(p):
    h = hashlib.md5()
    with open(p, "rb") as fh:
        for c in iter(lambda: fh.read(1 << 20), b""):
            h.update(c)
    return h.hexdigest()


def ascii_fold(s):
    for a, b in (("–", "-"), ("—", "-"), ("‘", ""), ("’", ""), ("“", ""),
                 ("”", ""), ("×", "x"), ("→", "_to_")):
        s = s.replace(a, b)
    s = unicodedata.normalize("NFKD", s)
    return "".join(c for c in s if ord(c) < 128)


def sanitize(stem):
    s = ascii_fold(stem)
    s = COPY_SUFFIX.sub(lambda m: "_alt" + (m.group(1) if m.group(1) != "1" else ""), s)
    s = DATE_COMPACT.sub(r"\1-\2-\3", s)
    s = re.sub(f"[{HOSTILE}]", "_", s).replace(" ", "_")
    s = re.sub(r"_+", "_", s).strip("_-.")
    return s or "unnamed"


def h1_of(path):
    """First markdown H1 / LaTeX title, used when the filename is uninformative."""
    try:
        head = open(path, encoding="utf-8", errors="replace").read(4000)
    except OSError:
        return ""
    m = re.search(r"^#\s+(.{4,90})$", head, re.M)
    if not m:
        m = re.search(r"\\title\{(.{4,90}?)\}", head, re.S)
    return m.group(1).strip() if m else ""


def infer_topic(hay):
    for topic, pat in TOPIC_RULES:
        if re.search(pat, hay, re.I):
            return topic
    return ""


def infer_class(rel, stem, ext):
    low = stem.lower()
    for pat, cls in CLASS_BY_NAME:
        if re.search(pat, low):
            if cls == "CERT" and ext not in (".json", ".md"):
                continue
            if cls in ("THM", "LEM", "AUDIT", "PLAN", "MAN", "DOC") and \
                    ext in (".py", ".sh", ".ipynb"):
                continue
            return cls
    for prefix, cls in CLASS_BY_DIR:
        if rel.startswith(prefix):
            if ext in (".py", ".sh"):
                return "ENGINE"
            if ext == ".ipynb":
                return "NB"
            return cls
    return CLASS_BY_EXT.get(ext, "DATA")


def split_meta(stem):
    date = ""
    m = DATE_ISO.search(stem)
    if m:
        date = m.group(0)
        stem = stem.replace(date, " ")
    ver = ""
    vm = VERSION.search(stem)
    if vm:
        ver = vm.group(1).lower().replace(".", "_")
        stem = stem[: vm.start()] + " " + stem[vm.end():]
    return stem, ver, date


def descriptor(core, cls, topic, fallback_title=""):
    s = sanitize(core).lower()
    if UNINFORMATIVE.search(s) and fallback_title:
        s = sanitize(fallback_title).lower()
    drop = {cls.lower(), topic.lower()} | STOP
    toks = [t for t in re.split(r"[_\-]+", s) if t and t not in drop]
    seen, out = set(), []
    for t in toks:
        if t not in seen:
            seen.add(t)
            out.append(t)
    return "_".join(out[:7]) or "item"


def build():
    files = []
    for dp, dn, fn in os.walk(ROOT):
        dn[:] = [d for d in dn if d not in SKIP_DIRS]
        for f in fn:
            p = os.path.join(dp, f)
            files.append((os.path.relpath(p, ROOT).replace(os.sep, "/"), p))

    texts = {}
    for rel, p in files:
        if rel.endswith(TEXTUAL):
            try:
                texts[rel] = open(p, encoding="utf-8", errors="replace").read()
            except OSError:
                pass

    pymods = {os.path.splitext(os.path.basename(r))[0] for r, _ in files
              if r.endswith(".py")}
    IMPORT = re.compile(
        r"^\s*(?:from\s+([A-Za-z_]\w*)\s+import|import\s+([A-Za-z_]\w*))", re.M)
    imported = {a or b for t in texts.values() for a, b in IMPORT.findall(t)} & pymods

    tierA, tierB, exempt = [], [], []
    for rel, p in files:
        base = os.path.basename(rel)
        stem, ext = os.path.splitext(base)
        ext = ext.lower()

        why = None
        if base in STRUCTURAL:
            why = "structural name (README etc.) — tools depend on it"
        elif "/" not in rel and base in ROOT_GOVERNANCE:
            why = "root governance file"
        elif rel.startswith(("QUARANTINE/", "records/", "corpus/", "archive/")):
            why = "append-only history / hash-pinned authority"
        elif ext == ".py" and stem in imported:
            why = "imported as a python module"
        elif base.startswith(".~lock"):
            why = "editor lock file — delete, do not rename"
        if why:
            exempt.append((rel, why))
            continue

        core, ver, date = split_meta(stem)
        cls = infer_class(rel, stem, ext)
        title = h1_of(p) if ext in (".md", ".tex") else ""
        hay = rel + " " + stem + " " + title
        top = infer_topic(hay) or "MISC"
        desc = descriptor(core, cls, top, title)
        new = "_".join([cls, top, desc] + ([ver] if ver else []) +
                       ([date] if date else [])) + ext
        new = re.sub(r"_+", "_", new)
        if new == base:
            continue
        tier = "A" if (ext in (".md", ".tex") and rel.split("/")[0] in
                       ("theory", "papers", "literature", "programs", "export")) else "B"
        (tierA if tier == "A" else tierB).append((rel, new, tier))
    return tierA, tierB, exempt, texts, files


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--apply", action="store_true")
    ap.add_argument("--tier", default="A", choices=["A", "AB"])
    ap.add_argument("--samples", type=int, default=20)
    args = ap.parse_args()

    tierA, tierB, exempt, texts, files = build()
    chosen = tierA + (tierB if args.tier == "AB" else [])

    print("RENAME PLAN — per NAMING_CONVENTION.md")
    print(f"  Tier A (documents, full rename) : {len(tierA)}")
    print(f"  Tier B (sanitize / reclass)     : {len(tierB)}")
    print(f"  Tier C (exempt)                 : {len(exempt)}")
    for w, n in collections.Counter(w for _, w in exempt).most_common():
        print(f"        {n:>4}  {w}")
    print(f"\n  selected: {len(chosen)} (tier {args.tier})\n")

    print("  sample proposals:")
    for rel, new, _ in chosen[: args.samples]:
        print(f"    {rel}")
        print(f"      -> {new}")

    hits = 0
    for rel, new, _ in chosen:
        b = os.path.basename(rel)
        if len(b) >= 8:
            hits += sum(t.count(b) for o, t in texts.items() if o != rel)
    print(f"\n  inbound references to rewrite: {hits}")

    outp = os.path.join(ROOT, "records", "RENAME_PLAN_2026-08-20.tsv")
    with open(outp, "w", encoding="utf-8", newline="\n") as fh:
        fh.write("tier\told_path\tnew_name\n")
        for rel, new, tier in tierA + tierB:
            fh.write(f"{tier}\t{rel}\t{new}\n")
        for rel, why in exempt:
            fh.write(f"C\t{rel}\t(exempt: {why})\n")
    print("  full plan -> records/RENAME_PLAN_2026-08-20.tsv")

    if not args.apply:
        print("\n(dry run — nothing renamed)")
        return 0

    # ---------------------------------------------------------------- apply
    rows = []
    for rel, new, _ in chosen:
        src = os.path.join(ROOT, rel.replace("/", os.sep))
        dst = os.path.join(os.path.dirname(src), new)
        if os.path.exists(dst):
            stem, ext = os.path.splitext(new)
            n = 2
            while os.path.exists(os.path.join(os.path.dirname(src), f"{stem}_{n}{ext}")):
                n += 1
            dst = os.path.join(os.path.dirname(src), f"{stem}_{n}{ext}")
        h = md5(src)
        shutil.move(src, dst)
        rows.append((rel, os.path.relpath(dst, ROOT).replace(os.sep, "/"),
                     os.path.getsize(dst), h))

    # rewrite inbound references
    rename_map = {os.path.basename(o): os.path.basename(n) for o, n, _, _ in rows}
    edited = 0
    for dp, dn, fn in os.walk(ROOT):
        dn[:] = [d for d in dn if d not in SKIP_DIRS]
        for f in fn:
            if not f.endswith(TEXTUAL):
                continue
            p = os.path.join(dp, f)
            try:
                t = open(p, encoding="utf-8", errors="replace").read()
            except OSError:
                continue
            orig = t
            for old, new in rename_map.items():
                if len(old) >= 8 and old in t:
                    t = t.replace(old, new)
            if t != orig:
                open(p, "w", encoding="utf-8", newline="\n").write(t)
                edited += 1

    mp = os.path.join(ROOT, "records", "RENAME_MANIFEST_2026-08-20.tsv")
    with open(mp, "w", encoding="utf-8", newline="\n") as fh:
        fh.write("old_path\tnew_path\tsize_bytes\tmd5\n")
        for r in rows:
            fh.write("\t".join(str(x) for x in r) + "\n")
    print(f"\nrenamed {len(rows)} files; rewrote references in {edited} files")
    print(f"  manifest -> records/RENAME_MANIFEST_2026-08-20.tsv")
    return 0


if __name__ == "__main__":
    sys.exit(main())
