"""Recover mislabeled text and index binary evidence without executing it."""
from __future__ import annotations

import argparse
import hashlib
import io
import json
import pickletools
import struct
import zipfile
from collections import Counter
from pathlib import Path
from xml.etree import ElementTree as ET


def protobuf_strings(data):
    pos, fields = 0, []

    def varint():
        nonlocal pos
        value, shift = 0, 0
        while pos < len(data) and shift < 70:
            byte = data[pos]
            pos += 1
            value |= (byte & 127) << shift
            if not byte & 128:
                return value
            shift += 7
        raise ValueError("incomplete protobuf varint")

    while pos < len(data):
        tag = varint()
        field, wire = tag >> 3, tag & 7
        if not field:
            raise ValueError("invalid protobuf field zero")
        if wire == 0:
            fields.append({"field": field, "integer": varint()})
        elif wire == 2:
            length = varint()
            if pos + length > len(data):
                raise ValueError("protobuf field leaves byte stream")
            payload = data[pos:pos + length]
            pos += length
            try:
                fields.append({"field": field, "text": payload.decode("utf-8")})
            except UnicodeDecodeError:
                fields.append({"field": field, "binary_bytes": length, "sha256": hashlib.sha256(payload).hexdigest()})
        elif wire in {1, 5}:
            size = 8 if wire == 1 else 4
            fields.append({"field": field, "fixed_hex": data[pos:pos + size].hex()})
            pos += size
        else:
            raise ValueError("unsupported protobuf wire type")
    if pos != len(data):
        raise ValueError("protobuf length mismatch")
    return fields


def flatten(value):
    if isinstance(value, str):
        return value
    if isinstance(value, list):
        return "".join(flatten(item) for item in value)
    return json.dumps(value, ensure_ascii=False)


def array_header(stream):
    import ast
    if stream.read(6) != b"\x93NUMPY":
        raise ValueError("not an NPY array")
    version = tuple(stream.read(2))
    length_bytes = 2 if version == (1, 0) else 4
    length = int.from_bytes(stream.read(length_bytes), "little")
    if length > 2**20:
        raise ValueError("unusually large NPY header; not read automatically")
    value = ast.literal_eval(stream.read(length).decode("utf-8" if version == (3, 0) else "latin-1"))
    return {"version": list(version), "shape": list(value["shape"]), "dtype": value["descr"], "fortran_order": value["fortran_order"]}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", type=Path, required=True)
    ap.add_argument("--extraction", type=Path, required=True)
    args = ap.parse_args()
    rows = [json.loads(l) for l in (args.extraction / "content.jsonl").read_text(encoding="utf-8").splitlines()]
    corrected = []
    for original in rows:
        if original["extraction"] not in {"error", "unsupported"}:
            continue
        row = dict(original)
        path = next((args.root / p for p in row["paths"] if (args.root / p).is_file()), None)
        if path is None:
            continue
        ext = path.suffix.lower()
        data = path.read_bytes()
        if hashlib.sha256(data).hexdigest() != row["sha256"]:
            raise ValueError("recovery source changed")
        text = None
        try:
            if original["extraction"] == "error" and ext == ".md":
                if data.startswith(b"\x12"):
                    fields = protobuf_strings(data)
                    text = "\n".join(f"[PROTOBUF FIELD {f['field']}]\n{f.get('text', json.dumps(f))}" for f in fields)
                    row["method"] = "Complete protobuf wire fields; UTF-8 string payloads. Misnamed .md contained a text envelope. No execution."
                else:
                    text = data.decode("utf-8")
                    text = "".join(c if ord(c) >= 32 or c in "\r\n\t" else f"[U+{ord(c):04X}]" for c in text)
                    row["method"] = "UTF-8 text with embedded control bytes visibly escaped; original source remains corrupt at those positions"
            elif original["extraction"] == "error" and ext == ".ipynb":
                notebook = json.loads(data)
                text = "\n\n".join(f"[CELL {i}]\n{flatten(c.get('source', ''))}\n[STORED OUTPUT]\n{json.dumps(c.get('outputs', []), ensure_ascii=False)}" for i, c in enumerate(notebook.get("cells", [])))
                row["method"] = "Nested source-list recovery in malformed notebook; all source elements and stored outputs preserved, not executed"
            elif path.name.startswith("~$") and ext == ".docx":
                row.update(extraction="office-owner-lock-metadata", method="Office temporary owner lock; not an OOXML manuscript")
            elif ext in {".npz", ".npy"}:
                if ext == ".npy":
                    arrays = [{"name": path.name, **array_header(io.BytesIO(data))}]
                else:
                    with zipfile.ZipFile(io.BytesIO(data)) as z:
                        arrays = []
                        for info in z.infolist():
                            if info.filename.endswith(".npy"):
                                with z.open(info) as inp:
                                    arrays.append({"name": info.filename, **array_header(inp)})
                row.update(extraction="numeric-array-metadata-indexed", method="All NPY headers read; values not analyzed and pickle not loaded", arrays=arrays)
            elif ext in {".png", ".jpg", ".jpeg", ".webp"}:
                from PIL import Image
                with Image.open(io.BytesIO(data)) as img:
                    row.update(extraction="image-metadata-indexed", image_format=img.format, dimensions=list(img.size), method="Image header read; visual mathematical content still pending", needs_visual_review=True)
            elif ext in {".xlsx", ".ots"}:
                with zipfile.ZipFile(io.BytesIO(data)) as z:
                    members = [n for n in z.namelist() if n.endswith(".xml") and (n.startswith("xl/worksheets/") or n in {"xl/sharedStrings.xml", "content.xml"})]
                    text = "\n\n".join(f"[PART {n}]\n{z.read(n).decode('utf-8')}" for n in members)
                row["method"] = "Worksheet XML including cell references, formulas and shared strings; formula evaluation and layout not reviewed"
            elif ext in {".pb"}:
                fields = protobuf_strings(data)
                text = json.dumps(fields, indent=2, ensure_ascii=False)
                row["method"] = "Complete protobuf wire scan; decoded string fields only, binary fields remain explicitly recorded"
            elif data.startswith(b"\x80") and ext in {"", ".pkl"}:
                counts = Counter()
                atoms = []
                for opcode, arg, position in pickletools.genops(data):
                    counts[opcode.name] += 1
                    if isinstance(arg, str):
                        atoms.append({"position": position, "opcode": opcode.name, "value": arg})
                row.update(extraction="pickle-opcodes-indexed", method="pickletools disassembly only; no unpickling or execution; numerical meaning still pending", opcodes=dict(counts), string_atoms=atoms)
            elif ext in {".sty", ".cls", ".bst", ".def", ".lock", ".minted", ".tag"}:
                text = data.decode("utf-8")
                row["method"] = "UTF-8 auxiliary/source text"
            if text is not None:
                encoded = text.encode("utf-8")
                target = args.extraction / "texts" / (row["sha256"] + ".recovered.txt")
                target.write_bytes(encoded)
                row.update(extraction="text-extracted", text_file=target.relative_to(args.extraction).as_posix(), text_sha256=hashlib.sha256(encoded).hexdigest(), characters=len(text), lines=text.count("\n") + 1)
            if row["extraction"] != original["extraction"]:
                row.pop("error", None)
                row["recovered_from"] = original["extraction"]
                row["recovery_script_sha256"] = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
                corrected.append(row)
        except Exception as error:
            row["recovery_error"] = f"{type(error).__name__}: {error}"
            corrected.append(row)
    overrides = {r["sha256"]: r for r in corrected}
    final = [overrides.get(r["sha256"], r) for r in rows]
    for name, records in [("recovery.jsonl", corrected), ("content_final.jsonl", final)]:
        with (args.extraction / name).open("x", encoding="utf-8", newline="\n") as out:
            for r in records:
                out.write(json.dumps(r, sort_keys=True, ensure_ascii=False) + "\n")
    print(json.dumps({"rows": len(final), "recovered_or_further_indexed": len(corrected), "counts": dict(Counter(r["extraction"] for r in final)), "errors": [(r["representative"], r.get("recovery_error", r.get("error"))) for r in final if r["extraction"] == "error"]}), flush=True)


if __name__ == "__main__":
    main()
