"""Stream the three oversized compressed data payloads without retaining copies."""
import collections,gzip,hashlib,json,re,struct,time
from pathlib import Path
p=Path(__file__).resolve().parent;root=Path('C:/WORKHOUSE')
s=json.loads((p/'supplement_summary.json').read_text(encoding='utf-8'))
paths=[r['path'] for r in s['coverage'] if r.get('error')=='gzip payload exceeds 128 MiB']
pat=re.compile(rb'\b(proof|proofs|prove[nds]?|theorem[s]?|lemma[s]?|derivation[s]?|proposition[s]?|corollar(?:y|ies)|qed)\b',re.I)
rows=[]
for name in paths:
 start=time.monotonic();n=0;digest=hashlib.sha256();counts=collections.Counter();samples=[];offset=0;tail=b''
 with gzip.open(root/name,'rb') as f:
  while True:
   b=f.read(1024*1024)
   if not b:break
   digest.update(b);n+=len(b);buf=tail+b;safe=len(buf)-128
   for m in pat.finditer(buf):
    if m.start()>=safe:continue
    counts[m.group().decode().lower()]+=1
    if len(samples)<12:samples.append({'byte_offset':offset+m.start(),'text':buf[max(0,m.start()-120):m.end()+200].decode('utf-8',errors='replace')})
   offset+=safe;tail=buf[safe:]
 for m in pat.finditer(tail):
  counts[m.group().decode().lower()]+=1
  if len(samples)<12:samples.append({'byte_offset':offset+m.start(),'text':tail[max(0,m.start()-120):m.end()+200].decode('utf-8',errors='replace')})
 rows.append({'path':name,'uncompressed_sha256':digest.hexdigest(),'uncompressed_bytes':n,'keyword_counts':dict(counts),'samples':samples,'elapsed_seconds':round(time.monotonic()-start,2),'status':'stream-searched'})
 print(name,n,dict(counts),flush=True)
(p/'oversize_stream_scan.json').write_text(json.dumps(rows,indent=2,ensure_ascii=False),encoding='utf-8')
