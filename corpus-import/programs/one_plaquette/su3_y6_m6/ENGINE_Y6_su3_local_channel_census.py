#!/usr/bin/env python3
from __future__ import annotations
import argparse,collections,functools,gzip,hashlib,itertools,json
from pathlib import Path

ROOT=(0,0,0,0,1);E=((1,0,0),(0,1,0),(0,0,1))

def boundary(p):
    p=tuple(p);x=p[:3];a,b=p[3:];xa=tuple(x[i]+E[a][i] for i in range(3));xb=tuple(x[i]+E[b][i] for i in range(3))
    return (((*x,a),1),((*xa,b),1),((*xb,a),-1),((*x,b),-1))

def sign_tuple(idx,n=8):return tuple(1 if (idx>>(n-1-j))&1 else -1 for j in range(n))

def token_sigs(rec,sg):
    word=tuple(tuple(x) for x in rec['ordered_insertions']);out=tuple(rec['output']);fs=(ROOT,)+word+(out,);rows={}
    for c,p in enumerate(fs):
        ext=-1 if c==7 else 1
        for l,inc in boundary(p):rows.setdefault(l,[0]*8)[c]=ext*inc*sg[c]
    return rows.values()

def c2num(ir):p,q=ir;return p*p+q*q+p*q+3*p+3*q
@functools.lru_cache(None)
def fuse(ir,t):
    p,q=ir
    if t==1:
        out=[(p+1,q)]
        if p:out.append((p-1,q+1))
        if q:out.append((p,q-1))
    else:
        out=[(p,q+1)]
        if q:out.append((p+1,q-1))
        if p:out.append((p-1,q))
    return tuple(out)
@functools.lru_cache(None)
def paths(tok):
    states={(0,0):collections.Counter({():1})}
    for ei,t in enumerate(tok):
        nxt=collections.defaultdict(collections.Counter)
        for ir,hs in states.items():
            for ir2 in ((ir,) if t==0 else fuse(ir,t)):
                en=c2num(ir2)
                for h,m in hs.items():nxt[ir2][h+(en,) if ei in (1,2,3,4,5) else h]+=m
        states=nxt
    return tuple(sorted(states.get((0,0),{}).items()))

def main(inp:Path,out:Path):
    out.mkdir(parents=True,exist_ok=True)
    raw=inp.read_bytes();assert len(raw)%8==0
    sigs={tuple(int.from_bytes(bytes([b]),"little",signed=True) for b in raw[i:i+8]) for i in range(0,len(raw),8)}
    rows=[];families=collections.Counter();hc=collections.Counter();mc=collections.Counter();allh=set();rh=collections.Counter();maxh=0
    for i,tok in enumerate(sorted(sigs),1):
        r=sum(x==1 for x in tok);ss=sum(x==-1 for x in tok);families[(r,ss)]+=1;ps=paths(tok)
        if not ps:raise AssertionError(("no singlet path",tok))
        hc[len(ps)]+=1;mult=sum(m for _,m in ps);mc[mult]+=1;maxh=max(maxh,len(ps));hist=[]
        for h,m in ps:
            d=tuple(16-e for e in h);allh.add(d);rm=sum((e==16)<<j for j,e in enumerate(h));rh[rm]+=1;hist.append({"E6":list(h),"d6":list(d),"multiplicity":m,"resonant_mask":rm})
        rows.append({"signature_id":f"L8-{i:05d}","tokens":list(tok),"family":[r,ss],"degree":r+ss,"singlet_path_count":len(ps),"singlet_multiplicity":mult,"histories":hist})
    summary={"status":"PASS","version":"2026-06-14-su3-y6-local-v1","ordered_signatures":len(sigs),"families":{f"({a},{b})":v for (a,b),v in sorted(families.items())},"distinct_local_five_cut_energy_histories":len(allh),"max_histories_per_signature":maxh,"history_count_histogram":dict(sorted(hc.items())),"singlet_multiplicity_histogram":dict(sorted(mc.items())),"resonant_mask_histogram":dict(sorted(rh.items())),"energy_convention":"E6=6E; E0_6=16; cuts after insertions 1..5","passed":True}
    table=out/"su3_y6_local_channel_table.json.gz";payload=json.dumps({"summary":summary,"local_signatures":rows},separators=(",",":"),sort_keys=True).encode()
    with gzip.GzipFile(filename=str(table),mode="wb",compresslevel=9,mtime=0) as f:f.write(payload)
    (out/"su3_y6_local_channel_summary.json").write_text(json.dumps(summary,indent=2,sort_keys=True));(out/"SU3_Y6_LOCAL_CHANNEL_CERTIFICATE.md").write_text(f"# SU(3) O(u^6) local channel census\n\n**Status:** PASS\n\n- ordered final local signatures: **{len(sigs):,}**;\n- distinct local five-cut histories: **{len(allh):,}**;\n- maximum histories per signature: **{maxh:,}**.\n\nThe fifth cut can contain determinant channels. Exact Haar matrices and the sixth-order folded contraction remain next.\n");print(json.dumps(summary,indent=2));print("TABLE_SHA256",hashlib.sha256(table.read_bytes()).hexdigest())

if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--input',type=Path,required=True);ap.add_argument('--output',type=Path,required=True);a=ap.parse_args();main(a.input,a.output)
