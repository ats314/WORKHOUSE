#!/usr/bin/env python3
"""Lift the curated judgements out of the fifth-edition guide into data.

The guide (a separate agent's edition, retained as a source) contains two
things this edition wants and cannot generate: a per-source statement of
*what is located where* and *what its scope is*, and a statement-to-evidence
crosswalk.  Those are judgement calls, not derivable from the ledgers.

Everything else about a source -- that its path exists, that its digest
still matches, that its graph identifiers resolve -- IS derivable, and is
re-derived at generation time rather than trusted from the guide.  So this
script extracts only the judgement, into

    paper/master/curation.yaml

which generate_sources.py then joins against the live repository.  The
split is the point: curated fields survive a ledger change, checkable
fields are re-checked on every build, and a divergence surfaces as a
generation warning rather than as a stale sentence.

Run once against the guide, then keep curation.yaml under review:

    python paper/master/extract_curation.py <guide.tex>
"""

from __future__ import annotations

import pathlib
import re
import sys

import yaml

HERE = pathlib.Path(__file__).resolve().parent
DEST = HERE / "curation.yaml"

# --------------------------------------------------------------------------
# Minimal LaTeX -> text.  The guide's curated fields are prose with a few
# markup commands; nothing here needs a real parser, but silently dropping
# a command would corrupt a scope note, so unknown commands are kept visible.
# --------------------------------------------------------------------------

UNWRAP = [
    (re.compile(r"\\sourcepath\{([^}]*)\}"), r"\1"),
    (re.compile(r"\\texttt\{([^}]*)\}"), r"\1"),
    (re.compile(r"\\emph\{([^}]*)\}"), r"\1"),
    (re.compile(r"\\textbf\{([^}]*)\}"), r"\1"),
    (re.compile(r"\\hyperref\[[^\]]*\]\{([^}]*)\}"), r"\1"),
    (re.compile(r"\\ref\{([^}]*)\}"), r"\1"),
    (re.compile(r"\\SU\b"), "SU"),
    (re.compile(r"\\textasciicircum\{\}"), "^"),
    (re.compile(r"\\textbackslash\{\}"), "\\\\"),
    (re.compile(r"\\par\b"), " "),
    (re.compile(r"\\newline\b"), " "),
    (re.compile(r"\\%"), "%"),
    (re.compile(r"\\_"), "_"),
    (re.compile(r"\\&"), "&"),
    (re.compile(r"\\\$"), "$"),
    (re.compile(r"\\#"), "#"),
]


def detex(s: str) -> str:
    out = s
    for _ in range(4):  # nested \texttt{\sourcepath{...}} occurs
        for pat, rep in UNWRAP:
            out = pat.sub(rep, out)
    out = re.sub(r"\s+", " ", out)
    return out.strip().rstrip(".").strip()


def field(block: str, label: str) -> str:
    """The text of \\textbf{label:} up to the next \\textbf or blank line."""
    m = re.search(
        r"\\textbf\{" + re.escape(label) + r":\}(.*?)(?=\\textbf\{|\n\s*\n|\Z)",
        block,
        re.S,
    )
    return detex(m.group(1)) if m else ""


def split_ids(s: str) -> list[str]:
    if not s or "No exact documentary path match" in s:
        return []
    return [p.strip() for p in re.split(r"[,;]\s*", s) if p.strip()]


# --------------------------------------------------------------------------


def parse_atlas(text: str) -> list[dict]:
    """Every source record: numbered atlas entries and literature entries."""
    records = []
    # Records are delimited by the \label{guide:source:KEY} that opens them.
    parts = re.split(r"\\phantomsection\s*\\label\{guide:source:([^}]+)\}", text)
    # parts = [preamble, key1, body1, key2, body2, ...]
    for i in range(1, len(parts) - 1, 2):
        key, body = parts[i], parts[i + 1]
        body = body.split("\\subsection")[0]
        # Title: the heading immediately before this label.
        before = parts[i - 1]
        mt = re.findall(r"\\subsection\*\{(?:S\d+:\s*)?(.*?)\}\s*$", before.strip())
        title = detex(mt[-1]) if mt else ""
        rec = {
            "key": key,
            "title": title,
            "local_file": field(body, "Local file"),
            "located_content": field(body, "Located content"),
            "use_and_scope": field(body, "Use and scope"),
            "sha256_prefix": field(body, "Source-byte SHA-256 prefix"),
            "graph_ids": split_ids(field(body, "Documentary graph identities")),
        }
        extra = field(body, "Index reading-copy locator")
        if extra:
            rec["reading_copy"] = extra
        pub = field(body, "Publication graph record")
        if pub:
            rec["publication_record"] = pub
        records.append(rec)
    return records


def parse_crosswalk(text: str) -> list[dict]:
    """The statement-to-evidence rows.

    A cell is a sequence of \\par-separated paragraphs, some opening with a
    \\textbf{Label:} and some not.  The unlabelled ones are the scope note,
    which is the judgement worth keeping, so the split has to be on \\par
    and not on \\textbf --- otherwise the note is swallowed by whichever
    labelled field happens to precede it.
    """
    m = re.search(r"\\label\{guide:graph:crosswalk\}(.*?)\\end\{longtable\}", text, re.S)
    if not m:
        return []
    rows = []
    for chunk in re.split(r"\\\\\[5pt\]", m.group(1)):
        if "\\textbf{Source:}" not in chunk:
            continue
        head, _, rest = chunk.partition("&")
        mnum = re.search(r"(\d+)\.\s*(?:Proposition|Theorem|Lemma|Corollary)", head)
        mlab = re.search(r"\\hyperref\[([^\]]+)\]", head)
        mname = re.search(r"\\newline\s*(.*?)\s*$", head.strip(), re.S)

        labelled: dict[str, str] = {}
        loose: list[str] = []
        for para in re.split(r"\\par\b", rest):
            para = para.strip()
            if not para:
                continue
            ml = re.match(r"\\textbf\{([^}]+):\}(.*)", para, re.S)
            if ml:
                labelled[ml.group(1)] = detex(ml.group(2))
            else:
                txt = detex(para)
                if txt:
                    loose.append(txt)

        # "Source:" is a list of source keys, then a full stop, then the
        # theorem labels inside those sources.  Keep them apart.
        raw = labelled.get("Source", "")
        keys_part, _, labels_part = raw.partition(". ")
        rows.append(
            {
                "number": int(mnum.group(1)) if mnum else None,
                "label": mlab.group(1) if mlab else "",
                "name": detex(mname.group(1)) if mname else "",
                "sources": split_ids(keys_part),
                "source_labels": split_ids(labels_part),
                "graph_entry": labelled.get("Graph entry", ""),
                "evidence_locator": labelled.get("Evidence locator", ""),
                "scope_note": " ".join(loose),
            }
        )
    return rows


def main() -> int:
    if len(sys.argv) < 2:
        raise SystemExit("usage: extract_curation.py <guide.tex>")
    src = pathlib.Path(sys.argv[1])
    text = src.read_text(encoding="utf-8", errors="replace")

    atlas = parse_atlas(text)
    cross = parse_crosswalk(text)

    doc = {
        "schema": "paper-curation/v1",
        "provenance": {
            "extracted_from": src.name,
            "note": (
                "Curated judgement lifted from a separate agent's fifth-edition "
                "guide, retained as a source. Only the judgement fields are "
                "carried: located_content, use_and_scope and scope_note. Paths, "
                "digests and graph identifiers are re-derived and re-checked "
                "against the repository at generation time, never trusted from "
                "here. Edit these fields as judgement improves; do not edit them "
                "to match a moved file."
            ),
        },
        "sources": atlas,
        "crosswalk": cross,
    }
    DEST.write_text(
        yaml.safe_dump(doc, sort_keys=False, allow_unicode=True, width=88),
        encoding="utf-8",
    )
    with_scope = sum(1 for a in atlas if a["use_and_scope"])
    with_ids = sum(1 for a in atlas if a["graph_ids"])
    print(
        f"wrote {DEST.name}: {len(atlas)} source records "
        f"({with_scope} with a scope note, {with_ids} with graph ids), "
        f"{len(cross)} crosswalk rows"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
