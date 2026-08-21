#!/usr/bin/env python3
"""
Strict R2 recovery for SU(3) O(y^5)/O(y^6) historical coefficients.

This revision fixes the false-positive behavior of the first extractor:
  * title/author validation is mandatory;
  * one PDF hash cannot fill multiple source slots;
  * hep-lat/0005009 is explicitly recognized as the 2000 GFMC paper;
  * the KPS scan receives targeted full-page OCR for its definition and table pages.

No coefficient is accepted automatically.
"""
from __future__ import annotations

import hashlib, json, os, re, subprocess, sys
from pathlib import Path

try:
    import fitz
except Exception:
    subprocess.check_call([sys.executable, "-m", "pip", "install", "-q", "pymupdf"])
    import fitz

BASE = Path("/content") if Path("/content").exists() else Path("/mnt/data")
OUT = BASE / "SU3_Y5_Y6_HISTORICAL_RECOVERY_R2"
OUT.mkdir(parents=True, exist_ok=True)

SOURCES = {
    "KPS_1981_string": {
        "required": [["kogut"], ["pearson"], ["shigemitsu"]],
        "title_terms": ["string tension", "roughening", "su(3)"],
        "expected_pages_min": 6,
    },
    "HIP_1986_string": {
        "required": [["hamer"], ["irving"], ["preece"]],
        "title_terms": ["cluster expansion", "su(3)"],
        "expected_pages_min": 5,
    },
    "HAMER_1989_mass": {
        "required": [["hamer"]],
        "title_terms": ["strong coupling", "glueball masses", "su(3)"],
        "expected_pages_min": 4,
    },
}

def sha256(path):
    h=hashlib.sha256()
    with open(path,"rb") as f:
        for b in iter(lambda:f.read(1<<20),b""):
            h.update(b)
    return h.hexdigest()

def roots():
    out=[BASE,Path("/mnt/data")]
    if Path("/content/drive").exists():
        out.append(Path("/content/drive"))
    return out

def pdfs():
    seen={}
    for root in roots():
        if not root.exists(): continue
        for p in root.rglob("*.pdf"):
            try: seen[sha256(p)] = p
            except Exception: pass
    return list(seen.values())

def extract_text(path):
    doc=fitz.open(path)
    pages=[p.get_text("text") for p in doc]
    return pages

def normalized(text):
    return re.sub(r"\s+"," ",text.lower())

def validate(path, spec):
    pages=extract_text(path)
    head=normalized(" ".join(pages[:3]))
    if "green’s function monte carlo" in head or "green's function monte carlo" in head:
        return False, "identified as 2000 GFMC paper", pages
    for group in spec["required"]:
        if not any(term in head for term in group):
            return False, f"missing required author group {group}", pages
    hits=sum(term in head for term in spec["title_terms"])
    if hits < max(1, len(spec["title_terms"])-1):
        return False, f"title-term score too low ({hits})", pages
    if len(pages) < spec["expected_pages_min"]:
        return False, f"too few pages ({len(pages)})", pages
    return True, "validated", pages

def score(path, spec):
    name=path.name.lower()
    pages=extract_text(path)
    head=normalized(" ".join(pages[:3]))
    s=0
    for group in spec["required"]:
        if any(t in head for t in group): s += 10
    for t in spec["title_terms"]:
        if t in head: s += 6
    if "green's function monte carlo" in head or "green’s function monte carlo" in head:
        s -= 100
    return s

def upload():
    if not Path("/content").exists(): return
    try:
        from google.colab import files
    except Exception:
        return
    print("Upload missing historical PDFs. The KPS scan may be named LIT_Y5_8010101.pdf.")
    for n,d in files.upload().items():
        Path("/content",Path(n).name).write_bytes(d)

def ocr_page(page, scale=4.0):
    try:
        import pytesseract
        from PIL import Image
    except Exception:
        subprocess.check_call([sys.executable,"-m","pip","install","-q","pytesseract","pillow"])
        import pytesseract
        from PIL import Image
    if subprocess.call(["bash","-lc","command -v tesseract >/dev/null 2>&1"]) != 0:
        subprocess.check_call(["bash","-lc","apt-get update -qq && apt-get install -y -qq tesseract-ocr"])
    pix=page.get_pixmap(matrix=fitz.Matrix(scale,scale),alpha=False)
    img=Image.frombytes("RGB",[pix.width,pix.height],pix.samples)
    return pytesseract.image_to_string(img)

def targeted_kps(path):
    doc=fitz.open(path)
    outputs=[]
    # Definitions are early; exact tables and figure captions tend to be late in the scan.
    candidates=sorted(set([0,1,2,3,4,5] + list(range(max(0,len(doc)-6),len(doc)))))
    for i in candidates:
        embedded=doc[i].get_text("text")
        ocr=ocr_page(doc[i],4.0)
        outputs.append({
            "page":i+1,
            "embedded_text":embedded,
            "ocr_text":ocr,
            "signals":{
                "table_I":bool(re.search(r"table\s+i\b",ocr,re.I)),
                "table_II":bool(re.search(r"table\s+ii\b",ocr,re.I)),
                "defines_x":bool(re.search(r"\bx\s*=",ocr,re.I)),
                "defines_T":bool(re.search(r"\bT\s*=",ocr)),
                "contains_x5_x6":("x5" in ocr.replace("^","").lower() or "x6" in ocr.replace("^","").lower()),
            }
        })
    return outputs

def main():
    allpdf=pdfs()
    chosen={}
    used=set()
    diagnostics={}
    for key,spec in SOURCES.items():
        ranked=sorted([(score(p,spec),p) for p in allpdf], key=lambda x:(-x[0],str(x[1])))
        accepted=None
        rejects=[]
        for sc,p in ranked:
            h=sha256(p)
            if h in used:
                rejects.append((str(p),sc,"hash already used by another slot"))
                continue
            ok,reason,pages=validate(p,spec)
            if ok:
                accepted=(p,pages)
                used.add(h)
                break
            rejects.append((str(p),sc,reason))
        diagnostics[key]={"rejects":rejects[:20]}
        if accepted:
            chosen[key]=accepted[0]
    missing=[k for k in SOURCES if k not in chosen]
    if missing:
        upload()
        # One retry after upload.
        allpdf=pdfs()
        chosen={}
        used=set()
        diagnostics={}
        for key,spec in SOURCES.items():
            ranked=sorted([(score(p,spec),p) for p in allpdf], key=lambda x:(-x[0],str(x[1])))
            rejects=[]
            for sc,p in ranked:
                h=sha256(p)
                if h in used:
                    rejects.append((str(p),sc,"hash already used by another slot"))
                    continue
                ok,reason,pages=validate(p,spec)
                if ok:
                    chosen[key]=p
                    used.add(h)
                    break
                rejects.append((str(p),sc,reason))
            diagnostics[key]={"rejects":rejects[:20]}
    missing=[k for k in SOURCES if k not in chosen]

    result={
        "status":"PARTIAL" if missing else "SOURCES_VALIDATED",
        "chosen":{k:{"path":str(p),"sha256":sha256(p),"pages":len(fitz.open(p))}
                  for k,p in chosen.items()},
        "missing":missing,
        "diagnostics":diagnostics,
        "accepted_coefficients":{},
    }

    if "KPS_1981_string" in chosen:
        result["KPS_targeted_pages"]=targeted_kps(chosen["KPS_1981_string"])

    j=OUT/"SU3_Y5_Y6_HISTORICAL_RECOVERY_R2.json"
    j.write_text(json.dumps(result,indent=2),encoding="utf-8")

    lines=[
        "# SU(3) historical coefficient recovery R2",
        "",
        f"**Status:** `{result['status']}`",
        "",
        "## Validated sources",
        "",
    ]
    for k,v in result["chosen"].items():
        lines += [f"- `{k}`: `{v['path']}` — SHA-256 `{v['sha256']}` — {v['pages']} pages"]
    lines += ["","## Missing sources",""]
    lines += [f"- `{k}`" for k in missing] or ["- none"]
    lines += ["","## Acceptance status","",
              "No fifth- or sixth-order coefficient has been accepted automatically.",
              "The KPS targeted OCR is stored in the JSON ledger for exact table reconstruction."]
    m=OUT/"SU3_Y5_Y6_HISTORICAL_RECOVERY_R2.md"
    m.write_text("\n".join(lines),encoding="utf-8")
    print("STATUS",result["status"])
    print("chosen",result["chosen"])
    print("missing",missing)
    print("JSON",j)
    print("MD",m)

if __name__=="__main__":
    main()
