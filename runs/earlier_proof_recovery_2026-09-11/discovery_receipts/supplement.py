"""Close format gaps left explicitly recorded by the first physical scan."""
import collections,gzip,hashlib,io,json,re,subprocess,sys,tarfile,zipfile
from pathlib import Path
import scan as s
sys.stdout.reconfigure(encoding='utf-8')
OUT=s.OUT;ROOT=s.ROOT
old=[json.loads(x) for x in (OUT/'content_inventory.jsonl').read_text(encoding='utf-8').splitlines()]
s.seen={r['sha256']:r for r in old}
before=set(s.seen)
for line in (s.REPO/'notes/WORKHOUSE_FULL_2026-09-07.jsonl').read_text(encoding='utf-8').splitlines():
    r=json.loads(line);s.audit[r['digest']]=r
for f in (OUT/'baseline').glob('ledger__*'):
    s.graph_hashes.update(re.findall(r'\b[a-f0-9]{64}\b',f.read_text(encoding='utf-8')))
for r in old:
    if r.get('graph_filename_ids'):
        for p in r['paths']:s.graph_names[Path(p).name.casefold()]+=r['graph_filename_ids']
coverage=[]

def feed(b,loc,ext=None):
    ext=ext or Path(loc).suffix.lower()
    if ext in s.TEXT_EXT|s.DOC_EXT|{'.zip'}:
        s.inspect_bytes(b,loc,ext,{'supplement':True})

def archive(path,rel):
    digest=hashlib.sha256(path.read_bytes()).hexdigest()
    if digest in archives_seen:
        coverage.append({'path':rel,'sha256':digest,'state':'duplicate-container'});return
    archives_seen.add(digest);count=0
    try:
        if rel.endswith('.zip'):
            with zipfile.ZipFile(path) as z:
                for info in z.infolist():
                    if info.is_dir():continue
                    count+=1
                    if info.file_size>128*1024*1024:
                        coverage.append({'path':rel+'!/'+info.filename,'state':'member-over-128MiB'});continue
                    if Path(info.filename).suffix.lower() in s.TEXT_EXT|s.DOC_EXT|{'.zip'}:
                        feed(z.read(info),rel+'!/'+info.filename)
        elif rel.endswith(('.7z','.zst')):
            p=subprocess.run(['tar','-tf',str(path)],stdout=subprocess.PIPE,stderr=subprocess.PIPE,timeout=60,check=True)
            for member in p.stdout.decode('utf-8',errors='replace').splitlines():
                count+=1
                if Path(member).suffix.lower() not in s.TEXT_EXT|s.DOC_EXT|{'.zip'}:continue
                b=subprocess.run(['tar','-xOf',str(path),member],stdout=subprocess.PIPE,stderr=subprocess.PIPE,timeout=60,check=True).stdout
                feed(b,rel+'!/'+member)
        else:
            try:
                with tarfile.open(path,'r:*') as tf:
                    for member in tf:
                        if not member.isfile():continue
                        count+=1
                        if any(p.lower() in s.RUNTIME for p in Path(member.name).parts):continue
                        if member.size>128*1024*1024:
                            coverage.append({'path':rel+'!/'+member.name,'state':'member-over-128MiB'});continue
                        if Path(member.name).suffix.lower() in s.TEXT_EXT|s.DOC_EXT|{'.zip'}:
                            feed(tf.extractfile(member).read(),rel+'!/'+member.name)
            except tarfile.ReadError:
                if not rel.endswith('.gz'):raise
                with gzip.open(path,'rb') as f:
                    b=f.read(128*1024*1024+1)
                if len(b)>128*1024*1024:raise ValueError('gzip payload exceeds 128 MiB')
                feed(b,rel+'!/'+path.stem);count=1
        coverage.append({'path':rel,'sha256':digest,'state':'searched','members':count})
    except Exception as e:coverage.append({'path':rel,'sha256':digest,'state':'error','error':str(e)})

archives_seen=set()
files=(OUT/'rg-files.txt').read_text(encoding='utf-8').splitlines()
selected=[]
for rel in files:
    rel=rel.replace('\\','/');p=ROOT/rel
    if s.GENERATED.search(rel):continue
    if '.resolved' in p.name or p.suffix in ('.bak','.before_scope_correction') or p.name.startswith('SHA256SUMS'):
        selected.append(('text',p,rel))
    elif p.suffix in ('.gz','.tar','.zst','.7z') or (p.suffix=='.zip' and p.stat().st_size>128*1024*1024):
        selected.append(('archive',p,rel))
for i,(kind,p,rel) in enumerate(selected):
    if i%100==0:print('supplement',i,'/',len(selected),flush=True)
    try:
        if kind=='archive':archive(p,rel)
        else:feed(p.read_bytes(),rel,'.txt')
    except Exception as e:coverage.append({'path':rel,'state':'error','error':str(e)})

# A malformed historical notebook has nested text-output lists; flatten for retrieval.
p=ROOT/'07_PIPELINE_TOOLS/glacial_einstein/raw_experiments/SU2_4D_SELFCONTAINED.ipynb'
def flatten(x):
    if isinstance(x,str):return x
    if isinstance(x,list):return ''.join(flatten(y) for y in x)
    return json.dumps(x,ensure_ascii=False)
obj=json.loads(p.read_text(encoding='utf-8'))
txt='\n'.join(f'[CELL {i+1}]\n'+flatten(c.get('source',[]))+'\n'+flatten(c.get('outputs',[])) for i,c in enumerate(obj['cells']))
digest=hashlib.sha256(p.read_bytes()).hexdigest()
text_path=OUT/'texts'/f'{digest}.txt';text_path.write_text(txt,encoding='utf-8')
row=s.seen[digest];row.update(scan='searched',extraction_method='notebook-nested-output-flatten',keyword_hits=len(s.PAT.findall(txt)),characters=len(txt))
row.update(headings=[{'line':i+1,'text':x[:240]} for i,x in enumerate(txt.splitlines()) if s.HEADER.search(x)][:90],hits=[{'line':i+1,'text':x[:450]} for i,x in enumerate(txt.splitlines()) if s.PAT.search(x)][:70],prior_inventory=digest in s.audit,prior_review_refs=[],prior_registration=[],pinned_as=None,graph_hash_mentioned=digest in s.graph_hashes,graph_filename_ids=[],discovery_score=60)
coverage.append({'path':str(p.relative_to(ROOT)),'sha256':digest,'state':'notebook-recovered'})

allrows=list(s.seen.values());cand=[r for r in allrows if r.get('keyword_hits')];cand.sort(key=lambda r:-r['discovery_score'])
for name,rows in [('combined_content_inventory.jsonl',allrows),('combined_keyword_candidates.jsonl',cand)]:
    with (OUT/name).open('w',encoding='utf-8') as f:
        for row in rows:f.write(json.dumps(row,ensure_ascii=False)+'\n')
summary={'selected_extra_paths':len(selected),'new_distinct_contents':len(set(s.seen)-before),'combined_contents':len(allrows),'combined_searched_texts':sum(r.get('scan')=='searched' for r in allrows),'combined_keyword_candidates':len(cand),'additional_stats':dict(s.stats),'coverage':coverage,'errors':s.errors}
(OUT/'supplement_summary.json').write_text(json.dumps(summary,indent=2,ensure_ascii=False),encoding='utf-8')
print(json.dumps({k:v for k,v in summary.items() if k not in ('coverage','errors')},ensure_ascii=False),flush=True)
