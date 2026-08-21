import json, sympy as sp
from itertools import permutations, product
# ---- exec THEIR LR engine (cells 1,2 only: no file writes, no 1M loop) ----
nb=json.load(open('nb_d3.ipynb')); ns={}
for idx in (1,2):
    src=''.join(nb['cells'][idx]['source'])
    exec(compile(src,f'<cell{idx}>','exec'),ns)
their_prod=ns['su3_multi_product']; IRR=ns['IRREPS_DYNKIN']; conj=ns['conjugate_dynkin']; dec=ns['decode_triple']
print("their engine loaded; irreps:",IRR)

# ---- MY independent engine: gl3 Schur via bialternant/Vandermonde, peeling ----
x,y,z=sp.symbols('x y z'); V=(x-y)*(x-z)*(y-z); vars=[x,y,z]
def psign(p):
    s=1
    for i in range(3):
        for j in range(i+1,3):
            if p[i]>p[j]: s=-s
    return s
def bialt(mu):
    return sum(psign(p)*vars[0]**mu[p[0]]*vars[1]**mu[p[1]]*vars[2]**mu[p[2]] for p in permutations(range(3)))
_sc={}
def schur(part):
    part=tuple(part)
    if part not in _sc:
        mu=(part[0]+2,part[1]+1,part[2])
        _sc[part]=sp.Poly(sp.cancel(bialt(mu)/V),x,y,z)
    return _sc[part]
def decompose(poly):
    P=sp.Poly(sp.expand(poly),x,y,z); res={}
    while P.as_expr()!=0:
        lead=max(P.monoms()); c=int(P.coeff_monomial(lead))
        res[lead]=res.get(lead,0)+c
        P=sp.Poly(sp.expand(P.as_expr()-c*schur(lead).as_expr()),x,y,z)
    return res
def pq_to_part(pq): p,q=pq; return (p+q,q,0)
def part_to_pq(n): return (n[0]-n[1], n[1]-n[2])
def my_sl3_prod(pq1,pq2):
    prod=sp.expand(schur(pq_to_part(pq1)).as_expr()*schur(pq_to_part(pq2)).as_expr())
    d=decompose(prod); out={}
    for nu,m in d.items(): out[part_to_pq(nu)]=out.get(part_to_pq(nu),0)+m
    return out
def my_multi(pqs):
    cur={tuple(pqs[0]):1}
    for r in pqs[1:]:
        nxt={}
        for pq,m in cur.items():
            for pq2,m2 in my_sl3_prod(pq,r).items(): nxt[pq2]=nxt.get(pq2,0)+m*m2
        cur=nxt
    return cur

# ---- (1) compare ALL 100 pairwise products ----
bad=0; n=0
for i,j in product(range(10),repeat=2):
    theirs={tuple(k):v for k,v in their_prod((IRR[i],IRR[j])).items()}
    mine=my_sl3_prod(IRR[i],IRR[j])
    mine={k:v for k,v in mine.items() if v}
    if theirs!=mine: bad+=1; print("MISMATCH",IRR[i],IRR[j],"theirs",theirs,"mine",mine)
    n+=1
print(f"pairwise: {n-bad}/{n} sl3 products agree (two independent algorithms)")

# ---- (2) the 10 six-factor singlet anchors ----
anchors=[(0,0),(111,111),(123,456),(555,555),(678,876),(999,999),(5,500),(321,123),(808,80),(246,642)]
abad=0
for oc,ic in anchors:
    o=dec(oc); ii=dec(ic)
    factors=[IRR[t] for t in o]+[conj(IRR[t]) for t in ii]
    theirs=int(their_prod(factors).get((0,0),0))
    # mine: singlet mult in (Ra⊗Rb⊗Rc ⊗ conj...) = <Ra⊗Rb⊗Rc , Rd⊗Re⊗Rf>
    A=my_multi([IRR[t] for t in o]); B=my_multi([IRR[t] for t in ii])
    mine=sum(A.get(k,0)*B.get(k,0) for k in set(A)|set(B))
    ok=theirs==mine
    if not ok: abad+=1
    print(f"  anchor {oc}/{ic}: their singlet={theirs}  my singlet={mine}  match={ok}")
print(f"six-factor anchors: {len(anchors)-abad}/{len(anchors)} agree")
print("\nREP-THEORY FOUNDATION independently confirmed:" , bad==0 and abad==0)
