"""Content extraction coverage, deliberately separate from mathematical review."""

from __future__ import annotations

import argparse
import hashlib
import json
import logging
import re
import zipfile
from collections import Counter, defaultdict
from concurrent.futures import ThreadPoolExecutor
from html.parser import HTMLParser
from pathlib import Path
from xml.etree import ElementTree as ET

logging.getLogger("pypdf").setLevel(logging.ERROR)
TEXT = set(".md .txt .tex .py .lean .json .jsonl .csv .tsv .yaml .yml .toml .xml .bib .rst .sh .ps1 .c .cpp .h .html .htm .resolved .ini .cfg .log .out .err .patch".split())
ARCHIVES = set(".zip .gz .tar .7z .zst .skill".split())
GENERATED = set(".aux .toc .synctex .bbl .blg .fdb_latexmk .fls .pyc .olean".split())


def infrastructure(path):
    parts = path.split("/")
    if any(p in {"uv-cache", ".uv-cache", "site-packages"} or p.endswith("-uv-cache") for p in parts):
        return "Installed dependency or package cache; bytes remain in census"
    if "/outputs/cache/" in path:
        return "Generated computation/dependency cache; not originating research evidence"
    if any(p.startswith("pytest") or p.endswith("_pytest") or p.startswith(".pytest") for p in parts):
        return "Generated test temporary tree; original test/run files remain eligible"
    if "hodge-o4-intake-venv" in parts:
        return "Installed Python environment with a nonstandard directory name"
    if Path(path).suffix.lower() in GENERATED:
        return "Reproducible compiler auxiliary; parent source retained"
    if any(p.startswith(".env") or p in {"secrets.json", "settings.local.json"} for p in parts):
        return "Local configuration; excluded from text index and publication"
    return None


class HTMLText(HTMLParser):
    def __init__(self):
        super().__init__()
        self.pieces = []

    def handle_data(self, data):
        self.pieces.append(data)


def decode(data):
    if data.startswith((b"\xff\xfe", b"\xfe\xff")):
        return data.decode("utf-16"), "utf-16 BOM"
    if b"\0" in data[:4096]:
        raise ValueError("binary bytes, no text decoder selected")
    try:
        return data.decode("utf-8-sig"), "utf-8"
    except UnicodeDecodeError:
        return data.decode("cp1252"), "cp1252 fallback; inspect encoding before quotation"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", type=Path, required=True)
    ap.add_argument("--census", type=Path, required=True)
    ap.add_argument("--output", type=Path, required=True)
    args = ap.parse_args()
    args.output.mkdir(parents=True, exist_ok=True)
    textdir = args.output / "texts"
    textdir.mkdir(exist_ok=True)
    groups, classifications = defaultdict(list), []
    for line in args.census.read_text(encoding="utf-8").splitlines():
        row = json.loads(line)
        why = infrastructure(row["path"])
        classifications.append({"path": row["path"], "sha256": row["sha256"], "exclusion": why})
        if not why:
            groups[row["sha256"]].append(row)
    with (args.output / "classifications.jsonl").open("x", encoding="utf-8") as out:
        for row in classifications:
            out.write(json.dumps(row, sort_keys=True) + "\n")

    def extract(item):
        digest, rows = item
        first = min(rows, key=lambda x: ("/outputs/" in x["path"], len(x["path"]), x["path"]))
        path = args.root / first["path"]
        suffix = path.suffix.lower()
        rec = {"sha256": digest, "paths": sorted(r["path"] for r in rows), "size": first["size"], "representative": first["path"], "review": "pending", "extraction": "unsupported"}
        try:
            data = path.read_bytes()
            if hashlib.sha256(data).hexdigest() != digest:
                raise ValueError("Source changed after census")
            if suffix in ARCHIVES:
                rec["extraction"] = "archive-member-audit-separate"
                return rec
            text = None
            if suffix == ".pdf":
                from pypdf import PdfReader
                pdf = PdfReader(path)
                pages = [page.extract_text() or "" for page in pdf.pages]
                rec["pages"] = len(pages)
                rec["pages_with_under_40_text_characters"] = [i + 1 for i, p in enumerate(pages) if len(p.strip()) < 40]
                rec["method"] = "pypdf page text; equations/layout/images not visually verified; no OCR"
                text = "\n\n".join(f"[PAGE {i + 1}]\n{p}" for i, p in enumerate(pages))
                if rec["pages_with_under_40_text_characters"]:
                    rec["needs_visual_or_OCR_review"] = True
            elif suffix in {".docx", ".pptx"}:
                with zipfile.ZipFile(path) as package:
                    members = sorted(n for n in package.namelist() if n.endswith(".xml") and (n.startswith("word/") or n.startswith("ppt/slides/")))
                    text = "\n\n".join(f"[PART {n}]\n" + " ".join(ET.fromstring(package.read(n)).itertext()) for n in members)
                rec["method"] = "OOXML text from document, notes and XML parts; no visual equation verification"
            elif suffix == ".ipynb":
                notebook = json.loads(data)
                chunks = []
                for i, cell in enumerate(notebook.get("cells", [])):
                    source = cell.get("source", "")
                    chunks.append(f"[CELL {i}, {cell.get('cell_type')}]\n" + ("".join(source) if isinstance(source, list) else source))
                    for out in cell.get("outputs", []):
                        chunks.append("[STORED OUTPUT, not re-executed]\n" + json.dumps(out, ensure_ascii=False))
                text = "\n\n".join(chunks)
                rec["method"] = "All notebook cell sources and stored outputs; not execution"
                rec["cells"] = len(notebook.get("cells", []))
            elif suffix in TEXT or not suffix or suffix[1:].isdigit():
                text, enc = decode(data)
                rec["method"] = "Original text: " + enc
                if suffix in {".html", ".htm"}:
                    h = HTMLText()
                    h.feed(text)
                    text = "\n".join(h.pieces)
                    rec["method"] += "; HTML data text including scripts, original retained"
            if text is not None:
                target = textdir / (digest + ".txt")
                encoded = text.encode("utf-8")
                target.write_bytes(encoded)
                rec.update(extraction="text-extracted" if text.strip() else "empty-text", text_file=target.relative_to(args.output).as_posix(), text_sha256=hashlib.sha256(encoded).hexdigest(), characters=len(text), lines=text.count("\n") + 1)
                headings = [line.strip()[:250] for line in text.splitlines() if re.match(r"^\s*(#{1,4}\s|\\(?:sub)*section\{|(?:Theorem|Lemma|Proposition)\s)", line)]
                rec["headings"] = headings[:80]
        except Exception as error:
            rec.update(extraction="error", error=f"{type(error).__name__}: {error}")
        return rec

    records = []
    with ThreadPoolExecutor(max_workers=4) as pool:
        with (args.output / "content.jsonl").open("x", encoding="utf-8") as out:
            for i, row in enumerate(pool.map(extract, sorted(groups.items())), 1):
                records.append(row)
                out.write(json.dumps(row, ensure_ascii=False, sort_keys=True) + "\n")
                if i % 500 == 0:
                    out.flush()
                    print(json.dumps({"content_groups_processed": i}), flush=True)
    summary = {"path_count": len(classifications), "excluded_paths": sum(bool(r["exclusion"]) for r in classifications), "eligible_unique_contents": len(records), "extraction_counts": dict(Counter(r["extraction"] for r in records)), "extracted_characters": sum(r.get("characters", 0) for r in records), "scope": "Extraction only; every content review remains pending until an evidence-backed review is joined. PDFs and OOXML require visual verification for mathematical use.", "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
    (args.output / "summary.json").write_text(json.dumps(summary, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(summary), flush=True)


if __name__ == "__main__":
    main()
