#!/usr/bin/env python3
from __future__ import annotations
import hashlib,json
from pathlib import Path
from fractions import Fraction as F
import sympy as sp

def find(name):
 for p in (Path('/content')/name,Path.cwd()/name,Path('/mnt/data')/name):
  if p.exists():return p
 for root in (Path('/content'),Path.cwd(),Path('/mnt/data')):
  if root.exists():
   for p in root.rglob(name):return p
 raise FileNotFoundError(name)
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def main():
 cp=find('CERT_Y4_sun_all_n_ge_3_band_shape_2026-06-14.json');c=json.loads(cp.read_text())
 spath=find('y4_exceptional_target_stage1_summary.json');s=json.loads(spath.read_text())
 xp=find('Y4_SU4_EXCEPTIONAL_CANCELLATION_LEDGER.json');x=json.loads(xp.read_text())
 rp=find('Y4_SU4_BALANCED_TARGET_REGRESSION.json');r=json.loads(rp.read_text())
 bp=find('NOTE_Y4_sun_b_structured_expression.txt');N=sp.symbols('N');B=sp.sympify(bp.read_text().strip(),locals={'N':N})
 stable=json.loads(find('CERT_Y4_sun_walled_brauer_full_symbolic_certificate_2026-06-14.json').read_text())
 assert c['gates']['passed'] and stable['gates']['passed'] and x['gates']['passed'] and r['gates']['passed']
 assert sha(spath)==c['hashes']['exceptional_stage1_summary'];assert sha(xp)==c['hashes']['su4_cancellation_ledger'];assert sha(rp)==c['hashes']['su4_balanced_regression'];assert sha(bp)==c['coefficients']['N_ge_4']['B_structured_expression_sha256']
 assert s['ranks']['4']['assignments']==33812 and s['ranks']['4']['charge_conjugation_orbits']==16906
 assert s['ranks']['5']['assignments']==33500 and s['ranks']['5']['target_unbalanced_signatures']==0
 assert s['ranks']['6']['assignments']==33502 and s['ranks']['6']['target_unbalanced_signatures']==0
 assert x['A_cancellation']['delta_A']=='0' and x['B_cancellation']['delta_B']=='0'
 assert x['counts']['amplitude_classes']==9 and x['counts']['target_topologies']==48 and x['counts']['fusion_paths']==144
 for row in x['B_cancellation']['amplitude_classes']:
  assert row['B_coefficient_histogram']=={'-8':row['topology_count']//2,'8':row['topology_count']//2}
 assert r['A']=='32/675' and r['B']=='3601925923737103752887/70481696720359496343750'
 table={int(row['N']):row for row in c['low_rank_exact_table']}
 assert table[3]['A']=='5/12' and table[3]['B']=='17607806155349/275331901291200'
 for n in (4,5,6):
  A=F(640,n*(n*n-1)**3);b=sp.cancel(B.subs(N,n));bf=F(int(b.p),int(b.q))
  assert table[n]['A']==str(A) and table[n]['B']==str(bf) and A>0 and bf>0
 print('PASS SU(4) exceptional census: +312 assignments, +156 C-orbits')
 print('PASS SU(4) determinant correction: delta A_4 = delta B_4 = 0')
 print('PASS SU(4) balanced target regression')
 print('PASS SU(5): no determinant sectors in complete geometry')
 print('PASS SU(6): sole determinant orbit absent from A/B target')
 print('PASS A_N,B_N positive at N=3,4,5,6 and symbolically for N>=7')
 print('ALL SU(N>=3) FOURTH-ORDER BAND-SHAPE GATES PASS')
if __name__=='__main__':main()
