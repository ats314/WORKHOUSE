"""Read-only physical-root census, content search and graph coverage joins.

Only writes inside this campaign. No source code from the archive is executed.
"""
from __future__ import annotations
import collections, hashlib, io, json, os, re, subprocess, sys, time, zipfile
from pathlib import Path
from xml.etree import ElementTree as ET

ROOT = Path('C:/WORKHOUSE')
OUT = Path(__file__).resolve().parent
REPO = ROOT / 'REPO'
REMOTE = 'ffff7bb2e67b976ba50fe5cf7184966dd581535f'
CACHE = ROOT / 'worktrees/legacy/autonomous-20260905/outputs/corpus_coverage_20260907/extraction/texts'
TEXT_EXT = {'.md','.tex','.txt','.lean','.py','.ipynb','.json','.jsonl','.yaml','.yml','.rst','.wl','.wls','.m','.nb','.sage','.r','.html','.htm','.xml','.csv','.log'}
DOC_EXT = {'.pdf','.docx','.odt','.rtf'}
PAT = re.compile(r'\b(proof|proofs|prove[nds]?|theorem[s]?|lemma[s]?|derivation[s]?|proposition[s]?|corollar(?:y|ies)|qed)\b', re.I)
HEADER = re.compile(r'^\s*(?:#{1,6}\s.*|\\(?:sub)*section\{.*|(?:Theorem|Lemma|Proposition|Corollary)\b.*|(?:theorem|lemma)\s+\w+.*)', re.I)
RUNTIME = {'.git','.venv','venv','.lake','node_modules','__pycache__','.cache','.uv-cache','uv-cache','.pytest_cache','.ruff_cache','.mypy_cache','site-packages','.graph-state','.workhouse-local','.ipynb_checkpoints'}
GENERATED = re.compile(r'(?:^|/)(?:index/(?:claims|graph|symbols)\.jsonl|notes/[^/]+\.jsonl|navigation/(?:files\.jsonl|preserved/|reconciliation/)|outputs/corpus_coverage_20260907/|corpus-import/export/index/|docs/derivation_formalization\.md|FRONTIER\.md|CERTIFIED\.md)', re.I)
stats = collections.Counter()
errors, excluded, aliases = [], [], []
seen = {}
audit = {}
catalog = []
graph_names = collections.defaultdict(list)
graph_hashes = set()

def dump(name, obj):
    (OUT/name).write_text(json.dumps(obj,ensure_ascii=False,indent=2),encoding='utf-8')

def git_bytes(path):
    return subprocess.run(['git','show',f'{REMOTE}:{path}'],cwd=REPO,check=True,stdout=subprocess.PIPE).stdout

def baseline():
    dst=OUT/'baseline'; dst.mkdir(exist_ok=True)
    names=['index/claims.jsonl','index/graph.jsonl','index/symbols.jsonl','ledger/results.yaml','ledger/derivation_statements.yaml','ledger/notes.yaml','ledger/documents.yaml','ledger/theorems.yaml','ledger/gaps.yaml','ledger/recent_research.yaml']
    manifest={}
    for name in names:
        try:
            data=git_bytes(name)
            (dst/name.replace('/','__')).write_bytes(data)
            manifest[name]={'sha256':hashlib.sha256(data).hexdigest(),'size':len(data)}
            if name.startswith('ledger/'):
                graph_hashes.update(re.findall(r'\b[a-f0-9]{64}\b',data.decode('utf-8')))
        except Exception as e: errors.append({'path':name,'stage':'baseline','error':str(e)})
    for line in (dst/'index__claims.jsonl').read_text(encoding='utf-8').splitlines():
        row=json.loads(line); catalog.append(row)
        if row['kind'] not in ('note','archive'):
            for fld in ('where','cites','statement','detail'):
                for p in re.findall(r'[\w./\\ -]+\.(?:md|tex|lean|py|pdf|docx|ipynb)',str(row.get(fld,'')),re.I):
                    graph_names[Path(p.replace('\\','/')).name.casefold()].append(row['id'])
    for line in (REPO/'notes/WORKHOUSE_FULL_2026-09-07.jsonl').read_text(encoding='utf-8').splitlines():
        row=json.loads(line); audit[row['digest']]=row
    dump('baseline_manifest.json',{'remote_commit':REMOTE,'files':manifest,'catalog_kinds':dict(collections.Counter(r['kind'] for r in catalog))})

def classify(locator):
    parts=locator.split('!/',1)[0].split('/')
    if parts[0]=='ARCHIVE': return '/'.join(parts[:3])
    if parts[0] in ('ALL THEORY','WORK_SINCE_LAST_SESSION','09_ARCHIVE','worktrees'): return '/'.join(parts[:2])
    return parts[0]

def decode(b):
    if b[:2] in (b'\xff\xfe',b'\xfe\xff'): return b.decode('utf-16',errors='replace')
    if b[:4] in (b'\xff\xfe\x00\x00',b'\x00\x00\xfe\xff'): return b.decode('utf-32',errors='replace')
    if b'\0' in b[:4096]: return None
    try: return b.decode('utf-8-sig')
    except UnicodeDecodeError: return b.decode('cp1252',errors='replace')

def extract(b, ext, digest):
    old=audit.get(digest)
    if ext in DOC_EXT and old:
        p=CACHE/(digest+'.txt')
        if p.exists():
            tb=p.read_bytes()
            if hashlib.sha256(tb).hexdigest()==old.get('extraction',{}).get('text_sha256'):
                stats['reused_exact_extractions']+=1
                return tb.decode('utf-8'), 'prior-hash-verified-extraction'
    if ext=='.docx':
        z=zipfile.ZipFile(io.BytesIO(b)); t=[]
        for name in ['word/document.xml','word/footnotes.xml','word/endnotes.xml']:
            if name not in z.namelist():continue
            root=ET.fromstring(z.read(name))
            for el in root.iter():
                if el.tag.endswith('}p'):
                    t.append(''.join(x.text or '' for x in el.iter() if x.tag.endswith('}t')))
        return '\n'.join(t),'docx-xml-paragraphs'
    if ext=='.pdf':
        from pypdf import PdfReader
        reader=PdfReader(io.BytesIO(b)); text=[]
        for i,page in enumerate(reader.pages): text.append(f'\n[PDF PAGE {i+1}]\n'+(page.extract_text() or ''))
        return '\n'.join(text),'pypdf-pages'
    if ext=='.odt':
        z=zipfile.ZipFile(io.BytesIO(b)); return '\n'.join(ET.fromstring(z.read('content.xml')).itertext()),'odt-xml'
    s=decode(b)
    if ext=='.ipynb' and s:
        obj=json.loads(s); cells=[]
        for i,cell in enumerate(obj.get('cells',[])):
            cells.append(f'[CELL {i+1} {cell.get("cell_type")}]\n'+''.join(cell.get('source',[])))
            for o in cell.get('outputs',[]):
                txt=o.get('text',o.get('data',{}).get('text/plain',[]))
                cells.append(''.join(txt) if isinstance(txt,list) else str(txt))
        return '\n'.join(cells),'notebook-cells-and-retained-output'
    return s,'decoded-text'

def inspect_bytes(b, locator, ext, meta, depth=0):
    digest=hashlib.sha256(b).hexdigest(); stats['eligible_occurrences']+=1
    if digest in seen:
        seen[digest]['paths'].append(locator); return
    row={'sha256':digest,'size':len(b),'paths':[locator],'region':classify(locator),'ext':ext,**meta}
    seen[digest]=row
    if ext=='.zip':
        stats['distinct_zip_containers']+=1
        if depth>=5: row['scan']='archive-depth-limit'; return
        try:
            z=zipfile.ZipFile(io.BytesIO(b))
            for info in z.infolist():
                if info.is_dir():continue
                member=locator+'!/'+info.filename
                suffix=Path(info.filename).suffix.lower()
                stats['archive_members_listed']+=1
                if any(p.lower() in RUNTIME for p in Path(info.filename).parts):continue
                if suffix not in TEXT_EXT|DOC_EXT|{'.zip'}:continue
                if info.file_size>64*1024*1024:
                    errors.append({'path':member,'stage':'archive','error':'member exceeds 64 MiB extraction limit'});continue
                try:inspect_bytes(z.read(info),member,suffix,{'container':locator,'member':info.filename},depth+1)
                except Exception as e:errors.append({'path':member,'stage':'archive-member','error':str(e)})
            row['scan']='archive-enumerated'
        except Exception as e: row['scan']='error'; errors.append({'path':locator,'stage':'archive','error':str(e)})
        return
    try:
        text,method=extract(b,ext,digest)
        row['extraction_method']=method
        if text is None: row['scan']='binary-or-unsupported';return
        row['characters']=len(text)
        matches=list(PAT.finditer(text)); row['keyword_hits']=len(matches)
        row['keyword_counts']=dict(collections.Counter(m.group().lower() for m in matches))
        row['scan']='searched';stats['distinct_texts_searched']+=1
        if not matches:return
        lines=text.splitlines()
        row['headings']=[{'line':i+1,'text':s[:240]} for i,s in enumerate(lines) if HEADER.search(s)][:90]
        row['hits']=[{'line':i+1,'text':s[:450]} for i,s in enumerate(lines) if PAT.search(s)][:70]
        prior=audit.get(digest)
        row['prior_inventory']=bool(prior)
        row['prior_review_refs']=prior.get('provenance',{}).get('prior_review_refs',[]) if prior else []
        row['prior_registration']=prior.get('provenance',{}).get('existing_registration',[]) if prior else []
        row['pinned_as']=prior.get('pinned_as') if prior else None
        row['graph_hash_mentioned']=digest in graph_hashes
        row['graph_filename_ids']=list(dict.fromkeys(graph_names.get(Path(locator).name.casefold(),[])))[:20]
        score=min(40,len(matches)) + min(30,len(row['headings'])*2)
        if re.search(r'proof|theorem|deriv|appendix|lemma',Path(locator).name,re.I):score+=20
        if ext in ('.md','.tex','.docx','.pdf','.lean'):score+=10
        if not row['graph_filename_ids']:score+=15
        if row['prior_review_refs'] or row['pinned_as']:score-=25
        if re.search(r'(?:README|INDEX|MANIFEST|REVIEW|STATUS|AUDIT|PLAN|AGENTS|CLAUDE|GEMINI|PROGRESS)',Path(locator).name,re.I):score-=35
        if len(text)<500:score-=40
        if len(text)>500000:score-=10
        row['discovery_score']=score
        (OUT/'texts'/f'{digest}.txt').write_text(text,encoding='utf-8')
        stats['distinct_keyword_candidates']+=1
    except Exception as e:
        row['scan']='error';errors.append({'path':locator,'stage':'extract','error':str(e)})

def main():
    start=time.time();(OUT/'texts').mkdir(exist_ok=True);baseline()
    print('Baseline captured; inventory scanning starts.',flush=True)
    # rg is the first-pass recursive finder. It does not follow junctions.
    cmd=['rg','--files','--hidden','--no-ignore']
    for name in sorted(RUNTIME):cmd+=['-g',f'!**/{name}/**']
    cmd+=['-g','!research/earlier_proof_discovery_20260911/**']
    p=subprocess.run(cmd,cwd=ROOT,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    (OUT/'rg-files.txt').write_bytes(p.stdout);(OUT/'rg-errors.txt').write_bytes(p.stderr)
    stats['rg_exit_code']=p.returncode
    files=p.stdout.decode('utf-8',errors='replace').splitlines()
    stats['physical_paths_listed']=len(files)
    print(f'Listed {len(files)} physical paths; reading eligible source content.',flush=True)
    with (OUT/'physical_inventory.jsonl').open('w',encoding='utf-8') as inv:
        for i,rel0 in enumerate(files):
            rel=rel0.replace('\\','/'); path=ROOT/rel
            if i%10000==0:print(f'paths {i}/{len(files)}; distinct texts {stats["distinct_texts_searched"]}; candidates {stats["distinct_keyword_candidates"]}',flush=True)
            try:
                st=path.stat();ext=path.suffix.lower()
                meta={'path':rel,'size':st.st_size,'mtime_ns':st.st_mtime_ns,'extension':ext}
                stats['extensions:'+ext]+=1
                if GENERATED.search(rel): meta['scan']='generated-retrieval-or-catalogue';stats['generated_paths_not_rescanned']+=1
                elif ext not in TEXT_EXT|DOC_EXT|{'.zip'}:meta['scan']='other-format';stats['other_format_paths']+=1
                elif st.st_size>128*1024*1024:meta['scan']='over-128MiB';errors.append({'path':rel,'stage':'read','error':'file exceeds 128 MiB content limit'})
                else:
                    inspect_bytes(path.read_bytes(),rel,ext,{'mtime_ns':st.st_mtime_ns})
                    meta['scan']='content-hashed'
                inv.write(json.dumps(meta,ensure_ascii=False)+'\n')
            except Exception as e:errors.append({'path':rel,'stage':'read','error':str(e)})
    rows=list(seen.values());candidates=[r for r in rows if r.get('keyword_hits')]
    candidates.sort(key=lambda r:(-r['discovery_score'],r['paths'][0]))
    with (OUT/'content_inventory.jsonl').open('w',encoding='utf-8') as f:
        for r in rows:f.write(json.dumps(r,ensure_ascii=False)+'\n')
    with (OUT/'keyword_candidates.jsonl').open('w',encoding='utf-8') as f:
        for r in candidates:f.write(json.dumps(r,ensure_ascii=False)+'\n')
    stats['distinct_contents']=len(rows);stats['elapsed_seconds']=round(time.time()-start,2)
    stats['candidate_inventory_only_or_uninventoried']=sum(not r['pinned_as'] and not r['prior_review_refs'] and not r['graph_filename_ids'] for r in candidates)
    dump('scan_summary.json',{'stats':dict(stats),'regions':dict(collections.Counter(r['region'] for r in candidates)),'errors':errors,'runtime_names_excluded':sorted(RUNTIME),'limits':{'file_MiB':128,'archive_member_MiB':64,'nested_zip_depth':5},'source_scope':'All physical paths visible to rg, including hidden and ignored paths, without following junctions; runtime and generated retrieval copies explicitly excluded.'})
    groups=collections.defaultdict(list)
    for r in candidates:
        if len(groups[r['region']])<12:groups[r['region']].append(r)
    text=['# Highest keyword candidates by source region','', 'Discovery ranking only. Every entry still needs source reading and substantive graph comparison.','']
    for region,rs in sorted(groups.items()):
        text+=['## '+region,'']
        for r in rs:
            text += [f'- {r["discovery_score"]}: `{r["paths"][0]}` | {r["keyword_hits"]} hits | hash `{r["sha256"][:12]}` | inventory {r["prior_inventory"]} | graph filename IDs {len(r["graph_filename_ids"])}', '  '+ ' / '.join(x['text'][:140] for x in r['headings'][:3])]
        text+=['']
    (OUT/'CANDIDATES_BY_REGION.md').write_text('\n'.join(text),encoding='utf-8')
    print(json.dumps({'done':True,'stats':dict(stats),'errors':len(errors)},ensure_ascii=False),flush=True)

if __name__=='__main__':main()
