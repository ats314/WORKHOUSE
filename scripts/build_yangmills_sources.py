"""Integrate the curated Yang-Mills acquisition manifests into native literature.

The manifests and study YAML are authored inputs. This command resolves duplicate
DOIs, regenerates the marked literature section, and writes coverage and BibTeX.
It does not infer citations among secondary papers or promote verification tiers.
"""

from __future__ import annotations

import hashlib
import json
from collections import Counter
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
COLLECTION = ROOT / "literature/yangmills"
START = "  # BEGIN JAFFE-WITTEN SOURCE COLLECTION\n"
END = "  # END JAFFE-WITTEN SOURCE COLLECTION\n"
SEED_URL = "https://www.claymath.org/wp-content/uploads/2022/06/yangmills.pdf"
SEED_HASH = "3558403ca14c11e382f73a09e548222708540bfdf478cf96aa11c52d43e23e09"

# These assignments are authored relevance judgements, not citation inference.
METHOD_REFS = {
    2,
    3,
    4,
    5,
    6,
    7,
    9,
    13,
    18,
    19,
    20,
    22,
    24,
    28,
    29,
    33,
    35,
    36,
    39,
    43,
    44,
    45,
    46,
    48,
}
TARGETS = {
    2: ["G19"],
    3: ["G19"],
    4: ["G17", "G23"],
    5: ["G19"],
    6: ["G17", "G23"],
    7: ["G19", "G23"],
    8: ["G18"],
    9: ["G19"],
    11: ["G18", "G22"],
    13: ["G23"],
    18: ["G17", "G23"],
    19: ["G18", "G23"],
    20: ["G17"],
    21: ["G19"],
    22: ["G17", "G23"],
    24: ["G18", "G23"],
    25: ["G19"],
    26: ["G17"],
    28: ["G17", "G19"],
    29: ["G19"],
    33: ["G23"],
    35: ["G23"],
    36: ["G23"],
    39: ["G19"],
    43: ["G18", "G22"],
    44: ["G20", "G23"],
    45: ["G18", "G23"],
    46: ["G23"],
    48: ["G17", "G19"],
    50: ["G19"],
}


def url_for(work: dict) -> str:
    if work.get("source_url"):
        return work["source_url"]
    if work.get("doi"):
        return "https://doi.org/" + work["doi"]
    return next((u for u in work.get("urls", []) if u.startswith("https://")), "")


def bib_escape(value: str) -> str:
    return value.replace("\\", "\\textbackslash{}").replace("{", "\\{").replace("}", "\\}")


def main() -> None:
    references = []
    for name in ("sources_01_25.json", "sources_26_50.json"):
        references.extend(json.loads((COLLECTION / name).read_text(encoding="utf-8")))
    if sorted(r["number"] for r in references) != list(range(1, 51)):
        raise ValueError("Every seed reference 1-50 must occur exactly once")
    related = json.loads((COLLECTION / "sources_related.json").read_text(encoding="utf-8"))
    related.append(json.loads((COLLECTION / "source_babelon.json").read_text(encoding="utf-8")))
    index_path = ROOT / "literature/index.yaml"
    original = index_path.read_text(encoding="utf-8")
    if START in original:
        before, marked = original.split(START, 1)
        original = before + marked.split(END, 1)[1]
    base = yaml.safe_load(original)
    records = base.get("papers", []) + base.get("stubs", [])
    known = {p["id"] for p in records}
    by_doi = {p["doi"].lower(): p["id"] for p in records if p.get("doi")}
    papers = []
    mapping = []
    work_records = []
    for reference in references:
        number = reference["number"]
        if not reference.get("works"):
            raise ValueError(f"Empty reference [{number}]")
        for work in reference["works"]:
            work_records.append((number, work))
    work_records.extend((None, work) for work in related)
    for number, work in work_records:
        pid = by_doi.get(str(work.get("doi", "")).lower(), work["id"])
        source_url = url_for(work)
        if not source_url:
            raise ValueError(f"{pid}: no source link")
        mapping.append({"reference": number, "source_id": work["id"], "paper_id": pid})
        if pid in known:
            continue
        known.add(pid)
        if work.get("doi"):
            by_doi[work["doi"].lower()] = pid
        targets = work.get("targets", TARGETS.get(number, ["G19"]))
        scope = work.get("scope_note", "")
        local = work.get("local_path")
        digest = work.get("sha256")
        is_preview = "preview" in work.get("access_status", "").lower()
        if local and (ROOT / local).exists():
            actual = hashlib.sha256((ROOT / local).read_bytes()).hexdigest()
            if actual != digest:
                raise ValueError(f"{pid}: reading-copy hash mismatch")
        reviewed = work.get("fulltext_review", "")
        note = (
            f"Jaffe-Witten reference [{number}]. "
            if number is not None
            else "Related source acquired through the orbit-curvature research route. "
        )
        note += f"Acquisition: {work.get('access_status', 'metadata_only')}; "
        note += f"reading: {reviewed or 'see acquisition manifest and locators'}. "
        note += "The acquisition manifest preserves the exact source version and access limits."
        paper = {
            "id": pid,
            "title": work["title"],
            "authors": work["authors"],
            "year": work["year"],
            "venue": work["venue"],
            "doi": work.get("doi"),
            "arxiv": work.get("arxiv"),
            "source_url": source_url,
            "licence": "cc-by" if work.get("licence") == "cc-by" else "publisher-copyright",
            "fulltext": None,
            "note": note,
            "scope_firewall": scope,
            "bears_on": [
                {
                    "target": target,
                    "relation": "supplies-method"
                    if number in METHOD_REFS or number is None
                    else "supplies-comparison",
                    "status": "not-yet-obtained",
                    "detail": scope
                    + " Applicability is a curated research connection; consult the source locators"
                    " and stated model hypotheses.",
                }
                for target in targets
            ],
        }
        if digest and not is_preview:
            paper["source_sha256"] = digest
        if work.get("licence") == "cc-by" and local:
            paper["fulltext"] = str(Path(local).relative_to("literature")).replace("\\", "/")
        if work.get("licence") == "arxiv-nonexclusive":
            paper["licence"] = "arxiv-nonexclusive"
        if work.get("cites"):
            paper["cites"] = work["cites"]
            paper["note"] += " Citation provenance: " + work["citation_provenance"]
        papers.append(paper)
    cited = list(dict.fromkeys(m["paper_id"] for m in mapping if m["reference"] is not None))
    seed = {
        "id": "JW_2006",
        "title": "Quantum Yang-Mills Theory",
        "authors": ["Arthur Jaffe", "Edward Witten"],
        "year": 2006,
        "venue": "Clay Mathematics Institute, official 14-page problem statement",
        "doi": None,
        "arxiv": None,
        "source_url": SEED_URL,
        "licence": "publisher-copyright",
        "fulltext": None,
        "source_sha256": SEED_HASH,
        "note": (
            "The supplied 14-page PDF exactly matches the official hosted bytes. PDF creation"
            " metadata is dated 2006-08-04. Page locators refer to this PDF, not the differently"
            " paginated book edition. All 50 numbered references are represented, with bundled"
            " works split. Historical assessments are dated source statements; they do not"
            " adjudicate later research. See literature/yangmills/README.md and COVERAGE.md."
        ),
        "cites": cited,
        "bears_on": [
            {"target": t, "relation": "supplies-method", "status": "verified", "detail": d}
            for t, d in {
                "G17": (
                    "PDF pp. 7-8 and 12: quantitative convergent expansions and volume-uniform"
                    " estimates are central constructive tasks. Verification here is of the source"
                    " passage, not a new proof of the gap."
                ),
                "G18": (
                    "PDF pp. 5-6: identifies the physical vacuum representation, local"
                    " gauge-invariant fields, and the full-Hamiltonian definition of a mass gap."
                ),
                "G19": (
                    "PDF p. 6 section 4 and pp. 11-12: specifies the continuum existence problem,"
                    " ultraviolet behavior, gauge-invariant observable limits and volume control."
                ),
                "G20": (
                    "PDF p. 12 section 6.6 cites Singer [44] for a possible connection between"
                    " orbit-space curvature and a mass gap; it motivates a curvature research"
                    " route."
                ),
                "G22": (
                    "PDF p. 12 section 6.6 cites Feynman [11] and Simon [43] when discussing"
                    " quartic nonabelian potential and quantum behavior despite classical"
                    " flat directions."
                ),
                "G23": (
                    "PDF pp. 5, 11-12: Euclidean reconstruction, Wilson reflection positivity and"
                    " uniform estimates must connect geometric methods to a physical spectral"
                    " statement."
                ),
            }.items()
        ],
    }
    section = yaml.safe_dump([seed, *papers], sort_keys=False, allow_unicode=True, width=100)
    section = "".join(
        "  " + line if line.strip() else line for line in section.splitlines(keepends=True)
    )
    if "\nstubs:" not in original:
        raise ValueError("Expected native stubs section")
    index_path.write_text(
        original.replace("\nstubs:", "\n" + START + section + END + "\nstubs:", 1), encoding="utf-8"
    )
    (COLLECTION / "reference_map.json").write_text(
        json.dumps(mapping, indent=2) + "\n", encoding="utf-8"
    )
    counts = Counter(work.get("access_status", "metadata_only") for _, work in work_records)
    stored = [(n, w) for n, w in work_records if w.get("local_path") and w.get("sha256")]
    previews = [(n, w) for n, w in stored if "preview" in w.get("access_status", "").lower()]
    lines = [
        "# Yang-Mills source coverage",
        "",
        "Generated by `scripts/build_yangmills_sources.py` from the curated acquisition records.",
        "",
        f"- Seed bibliography: **50/50 numbered references**, **{len(cited)} distinct works**.",
        f"- Additional related works: **{len(related)}**.",
        f"- Recorded acquisitions of complete source PDFs: **{len(stored) - len(previews)}**,"
        f" plus the supplied/official seed PDF; **{len(previews)} publisher preview(s)**"
        " recorded separately.",
        f"- Source acquisition states: `{dict(sorted(counts.items()))}`.",
        "- Downloaded does not mean read in full. Each acquisition record states its reading"
        " and metadata coverage.",
        "- Native paper relationships remain source-scoped T3 records. Only the seed's"
        " passage-verified relationships are marked verified by this builder.",
        "- Fulltext without an explicit redistribution licence remains in the ignored local"
        " reading inbox. The source IDs, verified links, hashes, notes and graph remain"
        " versionable.",
        "",
        "The acquisition counts describe the recorded collection pass. A clean clone does not"
        " include ignored reading copies. Present copies are hash-checked during regeneration"
        " and by the source tests.",
        "",
        "## Every numbered citation",
        "",
        "| Ref. | Native paper ID | Work | Access |",
        "|---|---|---|---|",
    ]
    map_by_id = {m["source_id"]: m["paper_id"] for m in mapping}
    for number, work in work_records:
        title = work["title"].replace("|", "\\|")
        lines.append(
            f"| {number if number else 'Related'} | `{map_by_id[work['id']]}`"
            f" | [{title}]({url_for(work)}) | {work.get('access_status', 'metadata_only')} |"
        )
    lines += ["", "## Acquisition and reading limits", ""]
    for _number, work in work_records:
        limitation = work.get("access_limitation") or work.get("access_note")
        if limitation:
            lines.append(f"- **{work['id']}**: {limitation}")
        corrections = (
            work.get("citation_correction")
            or work.get("metadata_note")
            or work.get("citation_note")
        )
        if corrections:
            lines.append(f"- **{work['id']} metadata**: {corrections}")
    (COLLECTION / "COVERAGE.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    bib_records = [seed] + [dict(w, id=map_by_id[w["id"]]) for _, w in work_records]
    bib = []
    bib_ids = set()
    for work in bib_records:
        if work["id"] in bib_ids:
            continue
        bib_ids.add(work["id"])
        fields = {
            "title": work["title"],
            "author": " and ".join(work["authors"]),
            "year": str(work["year"]),
            "howpublished": work["venue"],
            "url": url_for(work),
        }
        if work.get("doi"):
            fields["doi"] = work["doi"]
        if work.get("arxiv"):
            fields["eprint"] = work["arxiv"]
            fields["archivePrefix"] = "arXiv"
        bib.append(
            "@misc{"
            + work["id"]
            + ",\n"
            + "\n".join(f"  {key} = {{{bib_escape(value)}}}," for key, value in fields.items())
            + "\n}"
        )
    (COLLECTION / "references.bib").write_text("\n\n".join(bib) + "\n", encoding="utf-8")
    print(
        f"Integrated 50 references / {len(cited)} distinct works, {len(related)} related works,"
        f" {len(stored)} acquired PDFs plus seed"
    )


if __name__ == "__main__":
    main()
