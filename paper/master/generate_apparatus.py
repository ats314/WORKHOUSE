#!/usr/bin/env python3
"""Generate the master paper's apparatus from the ledgers.

Six artefacts, all derived and none hand-maintained:

  refs_generated.bib            every literature/index.yaml paper as BibTeX
  gen_literature.tex            the verified external-evidence map
  gen_obligations.tex           the route register: live, untried and DEAD routes
  gen_verification.tex          every analytic result by status and evidence
  gen_verification_register.tex the refutation register
  gen_macros.tex                every count the prose quotes, as a \newcommand

The macros live in their own file because the counts appear in the
abstract, which is typeset before any other body text.

The point of generating these is that the paper cannot drift from the
repository.  Re-run after any ledger change:

    python paper/master/generate_apparatus.py

Run from the repository root.
"""

from __future__ import annotations

import collections
import pathlib
import re
import sys

import yaml

ROOT = pathlib.Path(__file__).resolve().parents[2]
OUT = ROOT / "paper" / "master"

# --------------------------------------------------------------------------
# LaTeX escaping.  Ledger prose is written for terminals, not for TeX.
# --------------------------------------------------------------------------

# Ledger prose is written for a terminal and contains Unicode punctuation,
# comparison operators and the occasional Greek letter or accent.  The
# document uses an 8-bit font encoding, so these must be transliterated
# rather than passed through; an untransliterated character is silently
# dropped from the PDF, which is the worst of the available outcomes.
_UNICODE = {
    "—": "---",
    "–": "--",
    "−": "$-$",
    "‘": "`",
    "’": "'",
    "“": "``",
    "”": "''",
    "…": r"\ldots{}",
    " ": " ",
    "​": "",
    "≥": r"$\geq$",
    "≤": r"$\leq$",
    "≠": r"$\neq$",
    "≈": r"$\approx$",
    "×": r"$\times$",
    "±": r"$\pm$",
    "→": r"$\to$",
    "←": r"$\leftarrow$",
    "⇒": r"$\Rightarrow$",
    "∞": r"$\infty$",
    "∑": r"$\sum$",
    "√": r"$\sqrt{\ }$",
    "∈": r"$\in$",
    "⊆": r"$\subseteq$",
    "⊂": r"$\subset$",
    "·": r"$\cdot$",
    "°": r"$^\circ$",
    "§": r"\S{}",
    "α": r"$\alpha$",
    "β": r"$\beta$",
    "γ": r"$\gamma$",
    "δ": r"$\delta$",
    "ε": r"$\epsilon$",
    "η": r"$\eta$",
    "θ": r"$\theta$",
    "κ": r"$\kappa$",
    "λ": r"$\lambda$",
    "μ": r"$\mu$",
    "ν": r"$\nu$",
    "π": r"$\pi$",
    "ρ": r"$\rho$",
    "σ": r"$\sigma$",
    "τ": r"$\tau$",
    "φ": r"$\varphi$",
    "χ": r"$\chi$",
    "ψ": r"$\psi$",
    "ω": r"$\omega$",
    "Γ": r"$\Gamma$",
    "Δ": r"$\Delta$",
    "Λ": r"$\Lambda$",
    "Σ": r"$\Sigma$",
    "Ω": r"$\Omega$",
    "₀": r"$_0$",
    "₁": r"$_1$",
    "₂": r"$_2$",
    "₃": r"$_3$",
    "₄": r"$_4$",
    "ₙ": r"$_n$",
    "ō": r"\=o",
    "ū": r"\=u",
    "ā": r"\=a",
    "⁰": r"$^0$",
    "¹": r"$^1$",
    "²": r"$^2$",
    "³": r"$^3$",
    "⁴": r"$^4$",
    "é": r"\'e",
    "è": r"\`e",
    "ü": r"\"u",
    "ö": r"\"o",
    "ä": r"\"a",
    "ß": r"\ss{}",
    "ć": r"\'c",
}

_ESCAPES = {
    "\\": r"\textbackslash{}",
    "&": r"\&",
    "%": r"\%",
    "$": r"\$",
    "#": r"\#",
    "_": r"\_",
    "{": r"\{",
    "}": r"\}",
    "~": r"\textasciitilde{}",
    "^": r"\textasciicircum{}",
}


def tex(s: object) -> str:
    """Escape arbitrary ledger text for LaTeX text mode."""
    if s is None:
        return ""
    out = []
    for ch in str(s):
        if ch in _ESCAPES:
            out.append(_ESCAPES[ch])
        elif ch in _UNICODE:
            out.append(_UNICODE[ch])
        elif ord(ch) > 127:
            # Never drop a character silently: make the loss visible so the
            # transliteration table can be extended.
            out.append(f"[U+{ord(ch):04X}]")
        else:
            out.append(ch)
    txt = "".join(out)
    # Collapse the ledger's hard-wrapped prose into flowing text.
    txt = re.sub(r"\s*\n\s*", " ", txt)
    txt = re.sub(r"\s{2,}", " ", txt).strip()
    # Graph ids such as RESULT:TIER_COLLAPSE_ACTUAL_H4_SUPPORT run inline in
    # ledger prose and offer TeX no break point, overfilling the line.  Permit
    # a break after each separator without inserting a hyphen, which would
    # corrupt the identifier for anyone copying it back out.
    txt = txt.replace(r"\_", r"\_\allowbreak{}")
    txt = re.sub(r"(?<=[A-Za-z0-9]):(?=[A-Z])", r":\\allowbreak{}", txt)
    return txt


def first_sentences(s: object, n: int = 2, cap: int = 600) -> str:
    """The first n sentences of a ledger status field, escaped."""
    txt = tex(s)
    if not txt:
        return ""
    parts = re.split(r"(?<=[.;])\s+", txt)
    kept = " ".join(parts[:n])
    if len(kept) > cap:
        kept = kept[: cap - 1].rsplit(" ", 1)[0] + "\\,\\ldots"
    return kept


def load(name: str):
    with open(ROOT / name, encoding="utf-8") as fh:
        return yaml.safe_load(fh)


# --------------------------------------------------------------------------
# 1.  BibTeX
# --------------------------------------------------------------------------

# Paper titles and author names carry accents, Greek and sub/superscripts.
# BibTeX passes them through to an 8-bit font encoding, where an unmapped
# character is dropped silently, so they are transliterated at generation.
_BIB_UNICODE = dict(_UNICODE)
_BIB_UNICODE.update(
    {
        "ę": r"\k{e}",
        "ł": r"\l{}",
        "ϕ": r"$\phi$",
        "⁴": r"$^4$",
        "₂": r"$_2$",
        "₃": r"$_3$",
        "₁": r"$_1$",
        "ç": r"\c{c}",
        "ñ": r"\~n",
        "á": r"\'a",
        "í": r"\'i",
        "ó": r"\'o",
        "ú": r"\'u",
        "š": r"\v{s}",
        "č": r"\v{c}",
        "ž": r"\v{z}",
    }
)


def bib_escape(s: object) -> str:
    """BibTeX field escaping: protect specials, transliterate Unicode."""
    if s is None:
        return ""
    txt = str(s).replace("\\", "")
    for ch in ("&", "%", "_", "#", "$"):
        txt = txt.replace(ch, "\\" + ch)
    out = []
    for ch in txt:
        if ord(ch) < 128:
            out.append(ch)
        elif ch in _BIB_UNICODE:
            out.append(_BIB_UNICODE[ch])
        else:
            # Visible rather than silent: an unmapped character must show up
            # in the reference list so the table above can be extended.
            out.append(f"[U+{ord(ch):04X}]")
    return re.sub(r"\s+", " ", "".join(out)).strip()


def make_bib(papers) -> str:
    lines = [
        "% Generated by paper/master/generate_apparatus.py from literature/index.yaml.",
        "% Do not edit.  Every entry's evidence relation lives in the ledger, not here:",
        "% a citation edge is bibliography and never endorsement.",
        "",
    ]
    for p in sorted(papers, key=lambda q: (q.get("year") or 0, q["id"])):
        authors = " and ".join(bib_escape(a) for a in (p.get("authors") or []))
        venue = str(p.get("venue") or "")
        arxiv = p.get("arxiv")
        doi = p.get("doi")
        # Classify: an arXiv-only record is a preprint, everything else an article.
        preprint = bool(arxiv) and (
            "arxiv" in venue.lower() or "preprint" in venue.lower() or not venue
        )
        kind = "misc" if preprint else "article"
        lines.append(f"@{kind}{{{p['id']},")
        lines.append(f"  title        = {{{bib_escape(p.get('title'))}}},")
        if authors:
            lines.append(f"  author       = {{{authors}}},")
        if p.get("year"):
            lines.append(f"  year         = {{{p['year']}}},")
        if venue:
            field = "note" if preprint else "journal"
            lines.append(f"  {field}{' ' * (12 - len(field))} = {{{bib_escape(venue)}}},")
        if doi:
            lines.append(f"  doi          = {{{bib_escape(doi)}}},")
        if arxiv:
            lines.append(f"  eprint       = {{{bib_escape(arxiv)}}},")
            lines.append("  archiveprefix = {arXiv},")
        cit = p.get("inspire_citations")
        if isinstance(cit, dict) and cit.get("count") is not None:
            lines.append(
                f"  keywords     = {{INSPIRE citations {cit['count']} "
                f"as of {bib_escape(cit.get('as_of'))}}},"
            )
        lines.append("}")
        lines.append("")
    return "\n".join(lines)


# --------------------------------------------------------------------------
# 2.  The verified external-evidence map
# --------------------------------------------------------------------------

RELATION_GLOSS = {
    "contradicts": "contradicts",
    "corroborates": "corroborates",
    "supplies-value": "supplies a value",
    "supplies-method": "supplies a method",
    "supplies-comparison": "supplies a comparison",
    "confusable": "confusable with",
}

# Relations ordered by how much they can hurt or help the program.
RELATION_ORDER = [
    "contradicts",
    "confusable",
    "corroborates",
    "supplies-value",
    "supplies-comparison",
    "supplies-method",
]


def make_literature(papers) -> str:
    rows = []
    for p in papers:
        for b in p.get("bears_on") or []:
            if b.get("status") != "verified":
                continue
            rows.append(
                {
                    "id": p["id"],
                    "year": p.get("year"),
                    "target": b.get("target"),
                    "relation": b.get("relation"),
                }
            )
    order = {r: i for i, r in enumerate(RELATION_ORDER)}
    rows.sort(key=lambda r: (order.get(r["relation"], 99), r["target"] or "", r["id"]))

    total_edges = sum(len(p.get("bears_on") or []) for p in papers)
    verified = len(rows)
    obtained = len({r["id"] for r in rows})

    out = [
        "% Generated by paper/master/generate_apparatus.py.  Do not edit.",
        "\\begin{longtable}{@{}l l l l l@{}}",
        "\\caption{Verified external-evidence edges. Each row is a published "
        "result that was obtained, read, and checked against a named claim of "
        "this program. Relation is the ledger's own classification; "
        "\\emph{contradicts} and \\emph{confusable} are listed first because "
        "they are the rows that cost the program something.}"
        "\\label{tab:literature}\\\\",
        "\\toprule",
        "Paper & Ref. & Year & Bears on & Relation \\\\",
        "\\midrule",
        "\\endfirsthead",
        "\\toprule Paper & Ref. & Year & Bears on & Relation \\\\ \\midrule \\endhead",
        "\\bottomrule",
        "\\endfoot",
    ]
    for r in rows:
        # The ledger id is also the BibTeX key, so citing it here both
        # populates the bibliography and gives the reader the actual paper.
        out.append(
            f"\\texttt{{\\small {tex(r['id'])}}} & \\cite{{{r['id']}}} & "
            f"{r['year'] or ''} & "
            f"\\texttt{{{tex(r['target'])}}} & "
            f"{tex(RELATION_GLOSS.get(r['relation'], r['relation']))} \\\\"
        )
    out.append("\\end{longtable}")
    out.append("")
    # Keep every indexed paper in the bibliography, not only the verified
    # rows the table cites: the not-yet-obtained list is itself a result,
    # and dropping it would overstate the coverage.
    out.append("\\nocite{*}")
    out.append("")
    out.append(
        f"\\newcommand{{\\LitPapers}}{{{len(papers)}}}"
        f"\\newcommand{{\\LitEdges}}{{{total_edges}}}"
        f"\\newcommand{{\\LitVerified}}{{{verified}}}"
        f"\\newcommand{{\\LitObtained}}{{{obtained}}}"
    )
    return "\n".join(out)


# --------------------------------------------------------------------------
# 3.  The route register --- the roadmap proper
# --------------------------------------------------------------------------

TIER_NAME = {
    0: "Tier 0 (days)",
    1: "Tier 1 (weeks)",
    2: "Tier 2 (months)",
    3: "Tier 3 (unbounded)",
}


def make_obligations(gaps) -> str:
    counts = collections.Counter()
    for g in gaps:
        for s in g.get("plan") or []:
            counts[s.get("state")] += 1

    out = [
        "% Generated by paper/master/generate_apparatus.py.  Do not edit.",
        "% One subsection per gap that is not discharged, then the discharged",
        "% ones in brief.  Dead routes are reproduced in full: they are the",
        "% most expensive information in the ledger.",
        "",
    ]

    open_gaps = [g for g in gaps if g.get("state") != "discharged"]
    done_gaps = [g for g in gaps if g.get("state") == "discharged"]

    for g in sorted(open_gaps, key=lambda q: (q.get("tier", 9), q["id"])):
        gid = tex(g["id"])
        out.append(f"\\subsection*{{{gid} --- {tex(g.get('title'))}}}")
        out.append(f"\\addcontentsline{{toc}}{{subsection}}{{{gid} --- {tex(g.get('title'))}}}")
        bits = [TIER_NAME.get(g.get("tier"), "tier unrecorded"), tex(g.get("state"))]
        if g.get("load_bearing"):
            bits.append("\\textbf{load-bearing}")
        out.append("\\noindent\\emph{" + "; ".join(bits) + ".}\\par")
        if g.get("detail"):
            out.append("\\smallskip\\noindent " + first_sentences(g["detail"], 3) + "\\par")
        if g.get("status"):
            out.append(
                "\\smallskip\\noindent\\textbf{Ledger status.} "
                + first_sentences(g["status"], 4)
                + "\\par"
            )
        if g.get("depends_on"):
            dep = ", ".join(f"\\texttt{{{tex(d)}}}" for d in g["depends_on"])
            out.append(f"\\smallskip\\noindent\\textbf{{Depends on.}} {dep}\\par")
        if g.get("unblocks"):
            unb = ", ".join(f"\\texttt{{{tex(d)}}}" for d in g["unblocks"])
            out.append(f"\\smallskip\\noindent\\textbf{{Unblocks.}} {unb}\\par")

        plan = g.get("plan") or []
        if not plan:
            out.append("")
            continue

        for state, label in (
            ("live", "Live routes"),
            ("untried", "Untried routes"),
            ("dead", "Dead routes, and why they died"),
        ):
            steps = [s for s in plan if s.get("state") == state]
            if not steps:
                continue
            out.append(f"\\smallskip\\noindent\\textbf{{{label}.}}")
            out.append("\\begin{itemize}[leftmargin=1.4em]")
            for s in steps:
                body = first_sentences(s.get("status") or s.get("what"), 3)
                cd = s.get("cannot_decide") or []
                extra = ""
                if cd:
                    names = ", ".join(f"\\texttt{{{tex(c)}}}" for c in cd)
                    extra = f" \\emph{{Cannot decide:}} {names}."
                out.append(f"  \\item \\textbf{{{tex(s.get('step'))}.}} {body}{extra}")
            out.append("\\end{itemize}")
        # Completed routes are listed by name only: their content is in the body.
        finished = [s for s in plan if s.get("state") == "done"]
        if finished:
            names = "; ".join(tex(s.get("step")) for s in finished)
            out.append(
                f"\\smallskip\\noindent\\textbf{{Completed routes ({len(finished)}).}} "
                f"{names}.\\par"
            )
        out.append("")

    out.append("\\subsection*{Discharged gaps}")
    out.append("\\addcontentsline{toc}{subsection}{Discharged gaps}")
    out.append(
        "\\noindent Finished work stays recorded rather than re-queued. "
        "Each entry names what closed it.\\par\\smallskip"
    )
    out.append("\\begin{itemize}[leftmargin=1.4em]")
    for g in sorted(done_gaps, key=lambda q: q["id"]):
        out.append(
            f"  \\item \\texttt{{{tex(g['id'])}}} \\textbf{{{tex(g.get('title'))}.}} "
            + first_sentences(g.get("status"), 2)
        )
    out.append("\\end{itemize}")
    out.append("")
    out.append(
        f"\\newcommand{{\\RouteTotal}}{{{sum(counts.values())}}}"
        f"\\newcommand{{\\RouteDone}}{{{counts['done']}}}"
        f"\\newcommand{{\\RouteLive}}{{{counts['live']}}}"
        f"\\newcommand{{\\RouteUntried}}{{{counts['untried']}}}"
        f"\\newcommand{{\\RouteDead}}{{{counts['dead']}}}"
        f"\\newcommand{{\\GapOpen}}{{{len(open_gaps)}}}"
        f"\\newcommand{{\\GapDischarged}}{{{len(done_gaps)}}}"
    )
    return "\n".join(out)


# --------------------------------------------------------------------------
# 4.  Verification index
# --------------------------------------------------------------------------


def make_verification(results, theorems, contradictions) -> tuple[str, str]:
    """Return (results table, refutation register) as two LaTeX bodies.

    They are separate files because they belong in different parts of the
    paper: the table is reference apparatus, the register is argument.
    """
    status = collections.Counter(r.get("status") for r in results)
    evidence = collections.Counter(r.get("evidence") for r in results)

    # Lean coverage, counted from the ledger rather than asserted.
    lean_total = len(theorems)
    lean_sorry = sum(1 for t in theorems if t.get("sorry"))

    # The register's own vocabulary: `falsified` is a claim killed by a
    # counterexample, `superseded` a claim replaced by a sharper statement,
    # `resolved` a collision dissolved without either side losing.  All three
    # belong in the paper; conflating them would be the overclaim.
    by_status = collections.defaultdict(list)
    for c in contradictions:
        by_status[c.get("status")].append(c)

    out = [
        "% Generated by paper/master/generate_apparatus.py.  Do not edit.",
        "\\begin{longtable}{@{}p{0.44\\linewidth} l l@{}}",
        "\\caption{Analytic results by recorded status and evidence level. "
        "\\emph{Status} is what the argument establishes; \\emph{evidence} is "
        "what artefact backs it. The two are deliberately independent: a "
        "result can be \\texttt{proven} in status and \\texttt{record-backed} "
        "in evidence, meaning the proof exists and the machine artefact does "
        "not.}\\label{tab:results}\\\\",
        "\\toprule",
        "Result & Status & Evidence \\\\",
        "\\midrule",
        "\\endfirsthead",
        "\\toprule Result & Status & Evidence \\\\ \\midrule \\endhead",
        "\\bottomrule",
        "\\endfoot",
    ]
    for r in sorted(results, key=lambda q: q["id"]):
        short = r["id"].replace("RESULT:", "")
        out.append(
            f"\\texttt{{\\scriptsize {tex(short)}}} & "
            f"{tex(r.get('status'))} & {tex(r.get('evidence'))} \\\\"
        )
    out.append("\\end{longtable}")
    out.append("")

    # Everything from here belongs in the register, not the table.
    table, out = out, ["% Generated by paper/master/generate_apparatus.py.  Do not edit."]

    def cid(c):
        # C10 must sort after C9, not between C1 and C2.
        m = re.match(r"([A-Za-z]+)(\d+)", c["id"])
        return (m.group(1), int(m.group(2))) if m else (c["id"], 0)

    STATUS_GLOSS = {
        "falsified": (
            "Falsified --- killed by a counterexample or an exact computation. "
            "These are the four claims this program asserted, or inherited, "
            "and then lost."
        ),
        "superseded": (
            "Superseded --- replaced by a sharper statement. The original is "
            "not wrong so much as no longer the best available."
        ),
        "resolved": (
            "Resolved --- the collision was dissolved. In most of these the "
            "two sides turned out to be differently anchored quantities "
            "rather than competing values."
        ),
    }
    for st in ("falsified", "superseded", "resolved"):
        entries = sorted(by_status.get(st, []), key=cid)
        if not entries:
            continue
        out.append(f"\\subsection*{{{st.title()} ({len(entries)})}}")
        out.append(f"\\addcontentsline{{toc}}{{subsection}}{{{st.title()}}}")
        out.append("\\noindent " + STATUS_GLOSS[st] + "\\par\\smallskip")
        out.append("\\begin{itemize}[leftmargin=1.4em]")
        for c in entries:
            title = tex(c.get("title") or "")
            res = first_sentences(c.get("resolution") or c.get("detail") or "", 3)
            out.append(f"  \\item \\texttt{{{tex(c['id'])}}} \\textbf{{{title}.}} {res}")
        out.append("\\end{itemize}")
        out.append("")

    counts = "".join(
        f"\\newcommand{{\\Res{k.title().replace('-', '')}}}{{{v}}}"
        for k, v in sorted(status.items())
        if k
    )
    out.append(
        f"\\newcommand{{\\ResTotal}}{{{len(results)}}}"
        f"\\newcommand{{\\LeanTotal}}{{{lean_total}}}"
        f"\\newcommand{{\\LeanSorry}}{{{lean_sorry}}}"
        f"\\newcommand{{\\ContradictionTotal}}{{{len(contradictions)}}}"
        f"\\newcommand{{\\ContraFalsified}}{{{len(by_status.get('falsified', []))}}}"
        f"\\newcommand{{\\ContraSuperseded}}{{{len(by_status.get('superseded', []))}}}"
        f"\\newcommand{{\\ContraResolved}}{{{len(by_status.get('resolved', []))}}}" + counts
    )
    out.append("")
    out.append("% status histogram: " + repr(dict(status)))
    out.append("% evidence histogram: " + repr(dict(evidence)))
    return "\n".join(table), "\n".join(out)


# --------------------------------------------------------------------------


def main() -> int:
    OUT.mkdir(parents=True, exist_ok=True)

    lit = load("literature/index.yaml")["papers"]
    gaps = load("ledger/gaps.yaml")["gaps"]
    results = load("ledger/results.yaml")["results"]
    theorems = load("ledger/theorems.yaml").get("theorems") or []
    contradictions = load("ledger/contradictions.yaml").get("contradictions") or []

    ver_table, ver_register = make_verification(results, theorems, contradictions)
    artefacts = {
        "refs_generated.bib": make_bib(lit),
        "gen_literature.tex": make_literature(lit),
        "gen_obligations.tex": make_obligations(gaps),
        "gen_verification.tex": ver_table,
        "gen_verification_register.tex": ver_register,
    }
    # The counts appear in the abstract, so they must be defined before any
    # body text.  Lift every \newcommand out of the content files into one
    # macro file the drivers input first; the content files keep only content.
    macro_re = re.compile(r"\\newcommand\{\\[A-Za-z]+\}\{[^}]*\}")
    macros: list[str] = []
    for name in (
        "gen_literature.tex",
        "gen_obligations.tex",
        "gen_verification.tex",
        "gen_verification_register.tex",
    ):
        body = artefacts[name]
        macros.extend(macro_re.findall(body))
        artefacts[name] = "\n".join(
            ln for ln in body.splitlines() if not macro_re.match(ln.strip())
        )
    artefacts["gen_macros.tex"] = (
        "% Generated by paper/master/generate_apparatus.py.  Do not edit.\n"
        "% Every count the prose quotes is defined here, from the ledgers, so\n"
        "% the paper cannot state a number the repository has moved past.\n" + "\n".join(macros)
    )

    for name, body in artefacts.items():
        (OUT / name).write_text(body + "\n", encoding="utf-8")
        print(f"wrote {name}: {len(body.splitlines())} lines")

    print(
        f"\nsources: {len(lit)} papers, {len(gaps)} gaps, {len(results)} results, "
        f"{len(theorems)} theorems, {len(contradictions)} contradictions"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
