#!/usr/bin/env python3
import gzip,json,time
from fractions import Fraction as F
from pathlib import Path
from collections import Counter
S2=Path('/mnt/data/Y5_STAGE2_EXACT/y5_link_tensor_cards.json.gz')
S3=Path('/mnt/data/Y5_STAGE3G_EXACT/y5_exact_local_path_tensors.json.gz')
def read(p):
 with gzip.open(p,'rt') as f:return json.load(f)
def eps(a,b,c):
 if len({a,b,c})<3:return 0
 return -1 if ((a>b)+(a>c)+(b>c))%2 else 1
def rev_index(i,d):
 digs=[0]*d
 for k in range(d-1,-1,-1):digs[k]=i%3;i//=3
 o=0
 for x in digs:o=3*o+(2-x)
 return o
def basis_vec(card,b):
 sig=card['token_signature'];active=[i for i,x in enumerate(sig) if x];axis={e:i for i,e in enumerate(active)};d=len(active);v={}
 for flat in range(3**d):
  x=flat;colors=[0]*d
  for k in range(d-1,-1,-1):colors[k]=x%3;x//=3
  ec={e:colors[axis[e]] for e in active}
  if b['type']=='delta_pairing':
   val=1
   for a,c in b['event_position_pairs']:val*=int(ec[a]==ec[c])
  else:
   pos=b['epsilon_event_positions'];val=eps(ec[pos[0]],ec[pos[1]],ec[pos[2]])
   for a,c in b['delta_event_position_pairs']:val*=int(ec[a]==ec[c])
  if val:v[rev_index(flat,d)]=F(val)
 return v
def path_vec(p):return {int(i):F(int(n),int(d)) for i,n,d in p['vector']['entries']}
def main():
 t=time.time();cards={tuple(c['token_signature']):c for c in read(S2)['cards']};paths={tuple(r['signature']):r for r in read(S3)['path_tensors']};assert cards.keys()==paths.keys()
 hist=Counter();total=0
 for n,sig in enumerate(sorted(cards),1):
  c=cards[sig]; ps=[path_vec(p) for p in paths[sig]['paths']]; norms=[F(p['norm_squared']) for p in paths[sig]['paths']]
  for b in c['basis_in_event_order']:
   v=basis_vec(c,b);recon={}
   for p,norm in zip(ps,norms):
    if len(v)<len(p):dot=sum(x*p.get(i,0) for i,x in v.items())
    else:dot=sum(x*v.get(i,0) for i,x in p.items())
    coef=dot/norm
    if coef:
     for i,x in p.items():recon[i]=recon.get(i,F(0))+coef*x
   recon={i:x for i,x in recon.items() if x}
   assert recon==v,(sig,b['basis_index'])
   total+=1
  hist[c['basis_type']]+=1
  if n%100==0:print(n,'/',len(cards),flush=True)
 print('PASS',len(cards),'signatures',total,'basis vectors',dict(hist),'time',time.time()-t)
if __name__=='__main__':main()
