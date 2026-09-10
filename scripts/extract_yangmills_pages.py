"""Index every acquired source page without treating search hits as theorems.

Run with the PDF-enabled workspace Python. Complete extracted reading copies
stay in the ignored inbox beside the acquired PDFs. The versioned index records
hashes, page and line locators, topic hits and candidate labels only.
"""

from __future__ import annotations

import hashlib
import json
import re
from collections import Counter
from pathlib import Path

from pypdf import PdfReader

ROOT = Path(__file__).resolve().parents[1]
COLLECTION = ROOT / "literature/yangmills"
OUTPUT = COLLECTION / "extraction"
READING = ROOT / "literature/inbox/JW_2006/extracted"
TOPICS = {
    "ground_state": r"ground[ -]state|vacuum|Schr[oö]dinger",
    "spectral_gap": r"mass gap|spectral gap|discrete spectrum|compact resolvent",
    "curvature": r"curvature|Bakry|Ricci|orbit space",
    "reconstruction": r"reflection pos|Osterwalder|Wightman|reconstruct|semigroup",
    "uniform_limits": r"uniform|infinite volume|continuum limit|cutoff|cut-off",
    "constructive": r"cluster expansion|renormali|convergence|stability",
    "gauge_geometry": r"gauge|holonomy|connection|commutator",
}
LABEL = re.compile(r"\b(?:Theorem|Lemma|Proposition|Corollary|Definition)\s+[A-Z0-9][\w.\-]*")


def source_records() -> list[dict]:
    records = [
        {
            "id": "JW_2006",
            "title": "Quantum Yang-Mills Theory",
            "reference": None,
            "local_path": "literature/inbox/JW_2006/yangmills.pdf",
            "sha256": "3558403ca14c11e382f73a09e548222708540bfdf478cf96aa11c52d43e23e09",
            "access_status": "downloaded",
            "page_count": 14,
        }
    ]
    for name in ("sources_01_25.json", "sources_26_50.json"):
        for reference in json.loads((COLLECTION / name).read_text(encoding="utf-8")):
            records.extend(dict(work, reference=reference["number"]) for work in reference["works"])
    records.extend(json.loads((COLLECTION / "sources_related.json").read_text(encoding="utf-8")))
    records.append(json.loads((COLLECTION / "source_babelon.json").read_text(encoding="utf-8")))
    return records


def main() -> None:
    OUTPUT.mkdir(parents=True, exist_ok=True)
    READING.mkdir(parents=True, exist_ok=True)
    mapping = {
        r["source_id"]: r["paper_id"]
        for r in json.loads((COLLECTION / "reference_map.json").read_text(encoding="utf-8"))
    }
    pages, sources = [], []
    for work in source_records():
        source = {
            "source_id": work["id"],
            "paper_id": mapping.get(work["id"], work["id"]),
            "reference": work.get("reference"),
            "title": work["title"],
            "source_access": work.get("access_status"),
            "scope_note": work.get("scope_note", ""),
            "source_locators": work.get("evidence_locators", []),
            "review_status": (
                "mechanical page extraction; mathematical review is separately authored"
            ),
        }
        local = work.get("local_path")
        if not local or not (ROOT / local).exists():
            source.update(extraction_status="no local full text", pages=0)
            sources.append(source)
            continue
        digest = hashlib.sha256((ROOT / local).read_bytes()).hexdigest()
        if digest != work["sha256"]:
            raise ValueError(f"{work['id']}: source hash mismatch")
        reader = PdfReader(ROOT / local)
        text_path = READING / f"{work['id']}.txt"
        extracted, low_text = [], []
        for number, page in enumerate(reader.pages, 1):
            content = page.extract_text() or ""
            lines = content.splitlines()
            extracted.append(f"=== PDF PAGE {number} ===\n{content}\n")
            if len(content.strip()) < 80:
                low_text.append(number)
            hits = {}
            for topic, pattern in TOPICS.items():
                positions = [i for i, line in enumerate(lines, 1) if re.search(pattern, line, re.I)]
                if positions:
                    hits[topic] = positions
            pages.append(
                {
                    "paper_id": source["paper_id"],
                    "source_id": work["id"],
                    "pdf_page": number,
                    "source_sha256": digest,
                    "text_sha256": hashlib.sha256(content.encode("utf-8")).hexdigest(),
                    "reading_copy": text_path.relative_to(ROOT).as_posix(),
                    "text_characters": len(content),
                    "topic_line_hits": hits,
                    "candidate_labels": sorted(set(LABEL.findall(content))),
                    "status": "locator candidates only; hits may be citations or extraction errors",
                }
            )
        text_path.write_text("\n".join(extracted), encoding="utf-8")
        preview = "preview" in str(work.get("access_status", "")).lower()
        source.update(
            extraction_status="preview indexed" if preview else "all PDF pages indexed",
            pages=len(reader.pages),
            low_text_pages=low_text,
            source_sha256=digest,
            reading_copy=text_path.relative_to(ROOT).as_posix(),
            source_pdf=local,
        )
        sources.append(source)
    (OUTPUT / "pages.jsonl").write_text(
        "".join(json.dumps(p, ensure_ascii=False) + "\n" for p in pages), encoding="utf-8"
    )
    (OUTPUT / "sources.json").write_text(
        json.dumps(sources, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )
    counts = Counter(s["extraction_status"] for s in sources)
    summary = {
        "schema": "yangmills-extraction/v1",
        "sources": len(sources),
        "pages": len(pages),
        "access_counts": dict(counts),
        "candidate_label_pages": sum(bool(p["candidate_labels"]) for p in pages),
        "low_text_pages": sum(p["text_characters"] < 80 for p in pages),
        "scope": (
            "All acquired pages extracted and indexed. Candidate labels and topic matches "
            "are not reviewed theorem statements or certificates."
        ),
    }
    (OUTPUT / "summary.json").write_text(json.dumps(summary, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main()
