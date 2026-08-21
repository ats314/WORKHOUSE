#!/usr/bin/env python3
from __future__ import annotations
import itertools, sys, argparse, json, time, pickle, os
from collections import defaultdict
from fractions import Fraction as F
from pathlib import Path
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from ENGINE_FLUX_su3_moments_ext import link_terms, eval_term

DIRS=[(1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1)]
ORIENT=[(0,1),(0,2),(1,2)]

def edge_to_link(site,d):
    ax=d//2
    if d%2==0: lo=site; pw=1
    else: lo=tuple(site[k]+DIRS[d][k] for k in range(3)); pw=-1
    return (lo,ax),pw

def steps_to_word(start,dseq):
    word=[]; pos=start
    for d in dseq:
        lid,pw=edge_to_link(pos,d); word.append((lid,pw)); pos=tuple(pos[k]+DIRS[d][k] for k in range(3))
    return tuple(word),pos

def dagger(w): return tuple((g,-p) for g,p in reversed(w))
def plaquette_word(c,o,eps=1):
    mu,nu=ORIENT[o]; w,end=steps_to_word(c,[2*mu,2*nu,2*mu+1,2*nu+1]); assert end==c
    return w if eps==1 else dagger(w)

def _cyc_reduce(word):
    w=list(word); changed=True
    while changed and w:
      changed=False; L=len(w)
      for i in range(L):
        j=(i+1)%L
        if L>=2 and w[i][0]==w[j][0] and w[i][1]==-w[j][1]:
          w=w[:i]+w[j+1:] if j>i else w[1:-1]; changed=True; break
    return tuple(w)
def _min_rotation(w): return w if not w else min(tuple(w[i:]+w[:i]) for i in range(len(w)))
def expr_add(a,b,s=F(1)):
    o=dict(a)
    for m,c in b.items():
      o[m]=o.get(m,F(0))+s*c
      if not o[m]:del o[m]
    return o
def expr_scale(a,s): return {} if not s else {m:c*s for m,c in a.items() if c*s}
def expr_mul(a,b):
    o={}
    for m,c in a.items():
      for n,d in b.items():
        mn=tuple(sorted(m+n));o[mn]=o.get(mn,F(0))+c*d
    return {m:c for m,c in o.items() if c}

def canon_word(word):
    w=_cyc_reduce(tuple(word))
    if not w:return {():F(3)}
    L=len(w)
    for i in range(L):
      j=(i+1)%L
      if w[i]==w[j]:
        g,p=w[i]; alpha=w[j+1:]+w[:i] if j>i else w[1:-1]; out={}
        if p==1:
          terms=[(canon_word(alpha+((g,1),)),((g,1),),1),(canon_word(alpha),((g,-1),),-1),(canon_word(alpha+((g,-1),)),None,1)]
        else:
          terms=[(canon_word(alpha+((g,-1),)),((g,-1),),1),(canon_word(alpha),((g,1),),-1),(canon_word(alpha+((g,1),)),None,1)]
        for e,char,sgn in terms:
          for m,c in e.items():
            mm=m if char is None else tuple(sorted(m+(char,)));out[mm]=out.get(mm,F(0))+sgn*c
        return {m:c for m,c in out.items() if c}
    return {(_min_rotation(w),):F(1)}

def canon_expr(words,coeff=F(1)):
    out={():coeff}
    for w in words: out=expr_mul(out,canon_word(w))
    return out
def conj_expr(e):
    o={}
    for m,c in e.items():o=expr_add(o,canon_expr([tuple((g,-p) for g,p in reversed(w)) for w in m],c))
    return o

def charge_ok(m):
    q=defaultdict(int)
    for w in m:
      for g,p in w:q[g]+=p
    return all(v%3==0 for v in q.values())
_INT={}
def int_mono(m):
    if m in _INT:return _INT[m]
    if not charge_ok(m):_INT[m]=F(0);return F(0)
    nv=0; lf=defaultdict(lambda:([],[]))
    for w in m:
      ids=list(range(nv,nv+len(w)));nv+=len(w)
      for t,(g,p) in enumerate(w):
        a,b=ids[t],ids[(t+1)%len(w)];us,bs=lf[g]
        if p==1:us.append((a,b))
        else:bs.append((b,a))
    tls=[]
    for us,bs in lf.values():
      tl=link_terms(us,bs)
      if not tl:_INT[m]=F(0);return F(0)
      tls.append(tl)
    tls.sort(key=len);tot=F(0)
    for combo in itertools.product(*tls):
      cc=F(1);cons=()
      for c,k in combo:cc*=c;cons+=k
      if cc:tot+=eval_term(cc,cons,nv)
    _INT[m]=tot;return tot
def inner(a,b):
    return sum((c*int_mono(m) for m,c in expr_mul(conj_expr(a),b).items()),F(0))

def occs(m,g):return [(wi,t,p) for wi,w in enumerate(m) for t,(gg,p) in enumerate(w) if gg==g]
def ins_data(p):return ('after',0,1) if p==1 else ('before',1,-1)
def cut(L,t,w):return (t+1)%L if w=='after' else t%L
def opened(w,c):return w[c:]+w[:c]
def pair_fierz(m,ix,iy):
    wx,cx,sx=ix;wy,cy,sy=iy;words=list(m)
    if wx!=wy:
      A,B=words[wx],words[wy];rest=tuple(w for i,w in enumerate(words) if i not in (wx,wy));a=opened(A,cx);b=opened(B,cy)
      return expr_add(canon_expr(rest+(a+b,),F(1,2)),canon_expr(rest+(A,B),F(-1,6)))
    W=words[wx];rest=tuple(w for i,w in enumerate(words) if i!=wx);L=len(W);cx%=L;cy%=L
    c1,c2=(cx,cy) if (cx,sx)<=(cy,sy) else (cy,cx)
    if c1==c2:beta=();gamma=opened(W,c1)
    else:beta=tuple(W[i%L] for i in range(c1,c2 if c2>c1 else c2+L));gamma=tuple(W[i%L] for i in range(c2,c1+L))
    return expr_add(canon_expr(rest+(beta,gamma),F(1,2)),canon_expr(rest+(beta+gamma,),F(-1,6)))
_H0={}
def H0_mono(m):
    if m in _H0:return _H0[m]
    out={}
    for g in sorted({g for w in m for g,p in w}):
      oc=occs(m,g);block=expr_scale({m:F(1)},F(4,3)*len(oc))
      for i in range(len(oc)):
       for j in range(i+1,len(oc)):
        wi,ti,pi=oc[i];wj,tj,pj=oc[j];ai,si,ei=ins_data(pi);aj,sj,ej=ins_data(pj)
        block=expr_add(block,expr_scale(pair_fierz(m,(wi,cut(len(m[wi]),ti,ai),si),(wj,cut(len(m[wj]),tj,aj),sj)),F(2)*ei*ej))
      out=expr_add(out,expr_scale(block,F(1,2)))
    _H0[m]=out;return out

def solve(rows,rhs):
    A=[list(r)+[rhs[i]] for i,r in enumerate(rows)];m=len(A);n=len(rows[0]);piv=[];rr=0
    for col in range(n):
      p=next((i for i in range(rr,m) if A[i][col]),None)
      if p is None:continue
      A[rr],A[p]=A[p],A[rr];pv=A[rr][col];A[rr]=[x/pv for x in A[rr]]
      for i in range(m):
       if i!=rr and A[i][col]:
        f=A[i][col];A[i]=[A[i][j]-f*A[rr][j] for j in range(n+1)]
      piv.append(col);rr+=1
    if any(A[i][n] for i in range(rr,m)):return None,[]
    sol=[F(0)]*n
    for i,c in enumerate(piv):sol[c]=A[i][n]
    ker=[]
    for fc in [c for c in range(n) if c not in piv]:
      v=[F(0)]*n;v[fc]=1
      for i,c in enumerate(piv):v[c]=-A[i][fc]
      ker.append(v)
    return sol,ker

def candidate_edges(m):
    q=defaultdict(int)
    for w in m:
      for g,p in w:q[g]+=p
    out=set()
    for g,v in q.items():
      r=v%3
      if r==1:out.add((g,1))
      elif r==2:out.add((g,-1))
    return frozenset(out)
def endpoints(lid):
    lo,ax=lid;return lo,tuple(lo[k]+(1 if k==ax else 0) for k in range(3))
def is_simple(es):
    if not es:return False
    deg=defaultdict(int);nxt={};links=set()
    for g,p in es:
      if g in links:return False
      links.add(g);a,b=endpoints(g)
      if p==1:deg[a]+=1;deg[b]-=1;nxt[a]=b
      else:deg[a]-=1;deg[b]+=1;nxt[b]=a
    if any(deg.values()):return False
    st=next(iter(nxt));cur=st
    for k in range(len(es)):
      if cur not in nxt:return False
      cur=nxt[cur]
    return cur==st and len(nxt)==len(es)
def edges_word(es):
    nxt={}
    for g,p in es:
      a,b=endpoints(g)
      if p==1:nxt[a]=(b,(g,p))
      else:nxt[b]=(a,(g,p))
    st=next(iter(nxt));cur=st;w=[]
    while True:
      cur2,lp=nxt[cur];w.append(lp);cur=cur2
      if cur==st:break
    return tuple(w)
def loop_expr(w):return canon_expr((w,))

def touching(links):
    out=set()
    for g in links:
      lo,ax=g
      for mu,nu in ORIENT:
        if ax not in (mu,nu):continue
        other=nu if ax==mu else mu
        for shift in (0,-1):
          c=list(lo);c[other]+=shift;c=tuple(c)
          for eps in (1,-1):out.add(plaquette_word(c,ORIENT.index((mu,nu)),eps))
    return out

def project_shell(expr,shell_len):
    out=defaultdict(F)
    for m,c in expr.items():
      es=candidate_edges(m)
      if len(es)!=shell_len or not is_simple(es):continue
      w=edges_word(es);f=loop_expr(w);amp=c*inner(f,{m:F(1)})
      if amp:out[es]+=amp
    return dict(out)

def q_out_shell(x,shell_len):
    out=dict(x);proj=project_shell(x,shell_len)
    for es,a in proj.items():out=expr_add(out,loop_expr(edges_word(es)),-a)
    return out

def resolvent_term(x,E0,shell_len):
    q=q_out_shell(x,shell_len)
    if not q:return {}
    basis=list(q);seen=set(basis);i=0
    while i<len(basis):
      for mm in H0_mono(basis[i]):
        if mm not in seen:seen.add(mm);basis.append(mm)
      i+=1
      if len(basis)>200:raise RuntimeError(f'closure {len(basis)}')
    n=len(basis)
    # Weak-form exact resolvent on the function quotient:
    # (E0 G - H)c = <basis|q>, with P-orthogonality constraints.
    G=[[inner({basis[i]:F(1)},{basis[j]:F(1)}) for j in range(n)] for i in range(n)]
    H=[]
    for i in range(n):
      row=[]
      bi={basis[i]:F(1)}
      for j in range(n):
        row.append(inner(bi,H0_mono(basis[j])))
      H.append(row)
    rows=[[E0*G[i][j]-H[i][j] for j in range(n)] for i in range(n)]
    rhs=[inner({basis[i]:F(1)},q) for i in range(n)]
    shellfs=[]
    # shell functions seen in q and closure; candidate charge determines the only possible simple loop
    for m in basis:
      es=candidate_edges(m)
      if len(es)==shell_len and is_simple(es):
        f=loop_expr(edges_word(es))
        if not any(f==g for g in shellfs):shellfs.append(f)
    for f in shellfs:
      rows.append([inner(f,{m:F(1)}) for m in basis]);rhs.append(F(0))
    sol,ker=solve(rows,rhs)
    if sol is None:
      raise RuntimeError(f'inconsistent weak resolvent closure={n} shellfs={len(shellfs)}')
    assert all(sum(rows[i][j]*sol[j] for j in range(n))-rhs[i]==0 for i in range(len(rows)))
    # Any remaining kernel must be a zero function. A nonzero norm means an unremoved E0 resonance.
    for kv in ker:
      e={basis[j]:c for j,c in enumerate(kv) if c}
      if inner(e,e)!=0:
        raise RuntimeError('nonzero resonant kernel outside shell projector')
    return {basis[j]:c for j,c in enumerate(sol) if c}

def apply_second_and_project(yexpr,shell_len):
    out=defaultdict(F)
    for m,c in yexpr.items():
      links={g for w in m for g,p in w}
      for pw in touching(links):
        z=canon_expr(m+(pw,),c)
        for es,a in project_shell(z,shell_len).items():out[es]+=a
    return dict(out)

def column(ket_word,shell_len,E0,verbose=False):
    ket=loop_expr(ket_word);links={g for g,p in ket_word};H1=defaultdict(F);H2=defaultdict(F)
    pws=touching(links)
    if verbose:print('first plaquettes',len(pws),flush=True)
    for n,pw in enumerate(sorted(pws)):
      if verbose: print(' starting term',n+1,pw,flush=True)
      x=canon_expr((ket_word,pw))
      for es,a in project_shell(x,shell_len).items():H1[es]-=a
      q=q_out_shell(x,shell_len)
      if not q:continue
      yy=resolvent_term(x,E0,shell_len)
      for es,a in apply_second_and_project(yy,shell_len).items():H2[es]+=a
      if verbose and (n+1)%4==0:print(' term',n+1,'R terms',len(yy),flush=True)
    return dict(H1),dict(H2)

def calibrate():
    pa,_=steps_to_word((0,0,0),[0,2,1,3]);pb,_=steps_to_word((1,0,0),[0,2,1,3])
    H2cols=[]
    for w in (pa,dagger(pa)):
      h1,h2=column(w,4,F(8,3),True);H2cols.append(h2)
    targets=[frozenset(pb),frozenset(dagger(pb))]
    # rows pb,dagpb cols pa,dagpa
    vals=[[H2cols[j].get(targets[i],F(0)) for j in range(2)] for i in range(2)]
    print('block',vals)
    he=(vals[0][0]+vals[0][1]+vals[1][0]+vals[1][1])/2
    ho=(vals[0][0]-vals[0][1]-vals[1][0]+vals[1][1])/2
    print('he',he,'ho',ho)



# =============================================================================
# Production shell-six driver
# =============================================================================

def neg_dir(d):
    return d ^ 1


def canon_step_cycle(seq):
    seq = tuple(seq)
    return min(seq[i:] + seq[:i] for i in range(len(seq)))


def shapes6():
    """All oriented simple non-backtracking six-link loops, modulo translation
    and cyclic choice of starting vertex. Reversal is deliberately retained."""
    found = set()

    def dfs(seq, pos, visited):
        if len(seq) == 6:
            if pos == (0, 0, 0) and neg_dir(seq[-1]) != seq[0]:
                found.add(canon_step_cycle(tuple(seq)))
            return
        for d in range(6):
            if seq and neg_dir(seq[-1]) == d:
                continue
            nxt = tuple(pos[k] + DIRS[d][k] for k in range(3))
            if nxt == (0, 0, 0):
                if len(seq) + 1 != 6:
                    continue
            elif nxt in visited:
                continue
            dfs(seq + [d], nxt, visited | {nxt})

    dfs([], (0, 0, 0), {(0, 0, 0)})
    return sorted(found)


def word_to_edges(word):
    return frozenset(word)


def shift_lid(lid, delta):
    lo, axis = lid
    return (tuple(lo[k] + delta[k] for k in range(3)), axis)


def shift_word(word, delta):
    return tuple((shift_lid(lid, delta), pw) for lid, pw in word)


def shift_monomial(monomial, delta):
    return tuple(sorted(shift_word(word, delta) for word in monomial))


def shift_expr(expr, delta):
    return {shift_monomial(m, delta): c for m, c in expr.items()}


def shift_edges(edges, delta):
    return frozenset((shift_lid(lid, delta), pw) for lid, pw in edges)


def translation_anchor_expr(expr):
    lows = [
        lid[0]
        for monomial in expr
        for word in monomial
        for lid, _pw in word
    ]
    if not lows:
        return expr, (0, 0, 0)
    anchor = tuple(min(site[k] for site in lows) for k in range(3))
    delta = tuple(-x for x in anchor)
    return shift_expr(expr, delta), anchor


def canonical_edges_translation(edges):
    if not edges:
        return edges
    lows = [lid[0] for lid, _pw in edges]
    anchor = tuple(min(site[k] for site in lows) for k in range(3))
    delta = tuple(-x for x in anchor)
    return shift_edges(edges, delta)


def expr_cache_key(expr):
    return tuple(sorted(expr.items()))


_TERM_RESPONSE_CACHE = {}
_TERM_CACHE_PATH = None


def configure_term_cache(path):
    global _TERM_CACHE_PATH, _TERM_RESPONSE_CACHE
    _TERM_CACHE_PATH = path
    if path is not None and path.exists():
        with path.open("rb") as handle:
            payload = pickle.load(handle)
        if payload.get("version") != "2026-06-14-shell6-full-intermediate-v1":
            raise RuntimeError("term-cache version mismatch")
        _TERM_RESPONSE_CACHE = payload["responses"]
        print(
            f"LOADED persistent term cache: {len(_TERM_RESPONSE_CACHE)} topologies",
            flush=True,
        )


def persist_term_cache():
    if _TERM_CACHE_PATH is None:
        return
    _TERM_CACHE_PATH.parent.mkdir(parents=True, exist_ok=True)
    temporary = _TERM_CACHE_PATH.with_suffix(_TERM_CACHE_PATH.suffix + ".tmp")
    payload = {
        "version": "2026-06-14-shell6-full-intermediate-v1",
        "responses": _TERM_RESPONSE_CACHE,
    }
    with temporary.open("wb") as handle:
        pickle.dump(payload, handle, protocol=pickle.HIGHEST_PROTOCOL)
    os.replace(temporary, _TERM_CACHE_PATH)


def exact_term_response(x, shell_len, E0):
    """Return first- and second-order shell projections generated by one
    oriented plaquette insertion.

    Translation-equivalent terms share one exact resolvent solve. The returned
    edge sets are restored to the original absolute coordinates.
    """
    normalized, anchor = translation_anchor_expr(x)
    key = (expr_cache_key(normalized), shell_len, E0)

    if key not in _TERM_RESPONSE_CACHE:
        h1_local = {
            edges: -amp for edges, amp in project_shell(normalized, shell_len).items()
        }
        q = q_out_shell(normalized, shell_len)
        if q:
            resolved = resolvent_term(normalized, E0, shell_len)
            h2_local = apply_second_and_project(resolved, shell_len)
        else:
            h2_local = {}
        _TERM_RESPONSE_CACHE[key] = (h1_local, h2_local)
        persist_term_cache()

    h1_local, h2_local = _TERM_RESPONSE_CACHE[key]
    return (
        {shift_edges(edges, anchor): amp for edges, amp in h1_local.items()},
        {shift_edges(edges, anchor): amp for edges, amp in h2_local.items()},
    )


def exact_column(ket_word, shell_len, E0, verbose=False):
    """Connected H1 and H2 column for a fixed oriented loop.

    Disconnected vacuum bubbles are intentionally omitted. They contribute a
    common scalar shift and cannot affect shell-six channel ordering.
    """
    links = {lid for lid, _pw in ket_word}
    first_plaquettes = sorted(touching(links))
    H1 = defaultdict(F)
    H2 = defaultdict(F)

    if verbose:
        print(
            f"  first-hop oriented plaquettes: {len(first_plaquettes)}",
            flush=True,
        )

    for number, plaquette in enumerate(first_plaquettes, start=1):
        x = canon_expr((ket_word, plaquette))
        h1_term, h2_term = exact_term_response(x, shell_len, E0)
        for edges, amp in h1_term.items():
            H1[edges] += amp
        for edges, amp in h2_term.items():
            H2[edges] += amp
        if verbose and (number % 4 == 0 or number == len(first_plaquettes)):
            print(
                f"    term {number:3d}/{len(first_plaquettes)}; "
                f"cached topologies={len(_TERM_RESPONSE_CACHE)}",
                flush=True,
            )

    return dict(H1), dict(H2)


def shell4_codd_calibration(verbose=True):
    """Mandatory exact calibration against the certified domino result."""
    pa, end_a = steps_to_word((0, 0, 0), [0, 2, 1, 3])
    pb, end_b = steps_to_word((1, 0, 0), [0, 2, 1, 3])
    assert end_a == (0, 0, 0)
    assert end_b == (1, 0, 0)

    columns = []
    for ket in (pa, dagger(pa)):
        _h1, h2 = exact_column(ket, 4, F(8, 3), verbose=verbose)
        columns.append(h2)

    targets = [word_to_edges(pb), word_to_edges(dagger(pb))]
    block = [
        [columns[j].get(targets[i], F(0)) for j in range(2)]
        for i in range(2)
    ]

    even_hop = sum(block[i][j] for i in range(2) for j in range(2)) / 2
    odd_hop = (
        block[0][0] - block[0][1] - block[1][0] + block[1][1]
    ) / 2

    print("SHELL-4 CALIBRATION BLOCK")
    for row in block:
        print(" ", [str(x) for x in row])
    print("  C-even connected diagnostic:", even_hop)
    print("  C-odd connected hop:", odd_hop)

    if abs(odd_hop) != F(5, 612):
        raise RuntimeError(
            "shell-four C-odd calibration failed: "
            f"|{odd_hop}| != 5/612"
        )

    print("PASS shell-four C-odd exact hop magnitude = 5/612")
    return {
        "oriented_block": [[str(x) for x in row] for row in block],
        "c_even_connected_diagnostic": str(even_hop),
        "c_odd_hop": str(odd_hop),
        "c_odd_gate": True,
    }


def fraction_matrix_to_strings(matrix):
    return [[str(value) for value in row] for row in matrix]


def strings_to_fraction_matrix(matrix):
    return [[F(value) for value in row] for row in matrix]


def save_matrix_checkpoint(path, shapes, H1, H2, completed_columns, calibration):
    payload = {
        "meta": {
            "version": "2026-06-14-shell6-full-intermediate-v1",
            "scope": (
                "Connected shell-six H1/H2. Full trace-word Fierz resolvent; "
                "disconnected vacuum scalar omitted."
            ),
            "completed_columns": completed_columns,
            "matrix_dimension": len(shapes),
            "term_topology_cache_size": len(_TERM_RESPONSE_CACHE),
        },
        "shell_shapes": [list(shape) for shape in shapes],
        "H1": fraction_matrix_to_strings(H1),
        "H2_connected": fraction_matrix_to_strings(H2),
        "shell4_calibration": calibration,
    }
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")


def load_matrix_checkpoint(path):
    payload = json.loads(path.read_text())
    shapes = [tuple(shape) for shape in payload["shell_shapes"]]
    H1 = strings_to_fraction_matrix(payload["H1"])
    H2 = strings_to_fraction_matrix(payload["H2_connected"])
    completed = int(payload["meta"]["completed_columns"])
    return payload, shapes, H1, H2, completed


def build_shell6_matrices(output, resume=True, max_columns=None, verbose=True):
    calibration = shell4_codd_calibration(verbose=verbose)
    shapes = shapes6()
    if len(shapes) != 44:
        raise RuntimeError(f"expected 44 shell-six oriented shapes, got {len(shapes)}")

    words = []
    edge_map = {}
    for index, shape in enumerate(shapes):
        word, end = steps_to_word((0, 0, 0), shape)
        if end != (0, 0, 0):
            raise RuntimeError("nonclosed shell shape")
        words.append(word)
        key = canonical_edges_translation(word_to_edges(word))
        if key in edge_map:
            raise RuntimeError("duplicate oriented shell shape")
        edge_map[key] = index

    dimension = len(shapes)
    H1 = [[F(0) for _ in range(dimension)] for _ in range(dimension)]
    H2 = [[F(0) for _ in range(dimension)] for _ in range(dimension)]
    start_column = 0

    if resume and output.exists():
        old, old_shapes, H1, H2, start_column = load_matrix_checkpoint(output)
        if old_shapes != shapes:
            raise RuntimeError("checkpoint shell basis does not match current basis")
        print(f"RESUME checkpoint after column {start_column}/{dimension}")

    stop_column = dimension
    if max_columns is not None:
        stop_column = min(dimension, start_column + max_columns)

    for column_index in range(start_column, stop_column):
        start = time.time()
        print(
            f"\nCOLUMN {column_index + 1}/{dimension}: {shapes[column_index]}",
            flush=True,
        )
        h1_column, h2_column = exact_column(
            words[column_index],
            shell_len=6,
            E0=F(4),
            verbose=verbose,
        )

        for edges, amplitude in h1_column.items():
            key = canonical_edges_translation(edges)
            if key in edge_map:
                H1[edge_map[key]][column_index] += amplitude

        for edges, amplitude in h2_column.items():
            key = canonical_edges_translation(edges)
            if key in edge_map:
                H2[edge_map[key]][column_index] += amplitude

        elapsed = time.time() - start
        print(
            f"  completed in {elapsed:.1f} s; "
            f"H1 nnz column={sum(x != 0 for x in [row[column_index] for row in H1])}; "
            f"H2 nnz column={sum(x != 0 for x in [row[column_index] for row in H2])}",
            flush=True,
        )
        save_matrix_checkpoint(
            output,
            shapes,
            H1,
            H2,
            column_index + 1,
            calibration,
        )

    if stop_column < dimension:
        print(
            f"PARTIAL checkpoint written: {stop_column}/{dimension} columns",
            flush=True,
        )
        return output

    # Exact matrix gates.
    if H1 != [list(row) for row in zip(*H1)]:
        raise RuntimeError("H1 is not exactly symmetric")
    if H2 != [list(row) for row in zip(*H2)]:
        raise RuntimeError("H2 is not exactly symmetric")

    nonzero_h1 = [
        value
        for row in H1
        for value in row
        if value != 0
    ]
    if len(nonzero_h1) != 96:
        raise RuntimeError(f"expected 96 H1 entries, got {len(nonzero_h1)}")
    if set(nonzero_h1) != {F(-1, 3)}:
        raise RuntimeError(f"unexpected H1 amplitudes: {sorted(set(nonzero_h1))}")

    print("PASS shell-six H1 exact symmetry")
    print("PASS shell-six H2 exact symmetry")
    print("PASS shell-six H1 has 96 entries, all -1/3")

    save_matrix_checkpoint(
        output,
        shapes,
        H1,
        H2,
        dimension,
        calibration,
    )
    return output


def signed_permutation_group():
    import numpy as np

    group = []
    for permutation in itertools.permutations(range(3)):
        for signs in itertools.product((1, -1), repeat=3):
            matrix = np.zeros((3, 3), dtype=int)
            for i in range(3):
                matrix[i, permutation[i]] = signs[i]
            group.append(matrix)
    return group


def transform_direction(matrix, direction):
    import numpy as np

    vector = np.asarray(DIRS[direction], dtype=int)
    transformed = tuple(int(x) for x in matrix.dot(vector))
    return DIRS.index(transformed)


def reverse_shape(shape):
    return canon_step_cycle(tuple(neg_dir(d) for d in reversed(shape)))


def transform_shape(shape, matrix):
    return canon_step_cycle(tuple(transform_direction(matrix, d) for d in shape))


OCTAHEDRAL_CHARACTERS = {
    "A1": {"E": 1, "C3": 1, "C2": 1, "C4": 1, "C2p": 1},
    "A2": {"E": 1, "C3": 1, "C2": 1, "C4": -1, "C2p": -1},
    "E": {"E": 2, "C3": -1, "C2": 2, "C4": 0, "C2p": 0},
    "T1": {"E": 3, "C3": 0, "C2": -1, "C4": 1, "C2p": -1},
    "T2": {"E": 3, "C3": 0, "C2": -1, "C4": -1, "C2p": 1},
}
IRREP_DIMENSIONS = {"A1": 1, "A2": 1, "E": 2, "T1": 3, "T2": 3}
J_LABEL = {"A1": 0, "A2": 3, "E": 2, "T1": 1, "T2": 2}


def proper_class(matrix):
    import numpy as np

    trace = int(round(np.trace(matrix)))
    if trace == 3:
        return "E"
    if trace == 1:
        return "C4"
    if trace == 0:
        return "C3"
    permutation = [
        int(np.nonzero(matrix[i])[0][0]) for i in range(3)
    ]
    return "C2" if permutation == [0, 1, 2] else "C2p"


def irrep_character(irrep, parity, matrix):
    import numpy as np

    determinant = int(round(np.linalg.det(matrix)))
    if determinant == 1:
        proper = matrix
        parity_sign = 1
    else:
        proper = -matrix
        parity_sign = 1 if parity == "+" else -1
    return OCTAHEDRAL_CHARACTERS[irrep][proper_class(proper)] * parity_sign


def analyze_shell6_matrix(matrix_file, output_file):
    import numpy as np

    payload, shapes, H1, H2, completed = load_matrix_checkpoint(matrix_file)
    if completed != len(shapes):
        raise RuntimeError(
            f"matrix is partial: {completed}/{len(shapes)} columns"
        )

    dimension = len(shapes)
    index = {shape: i for i, shape in enumerate(shapes)}
    group = signed_permutation_group()

    representations = []
    for matrix in group:
        permutation = np.zeros((dimension, dimension), dtype=float)
        for j, shape in enumerate(shapes):
            transformed = transform_shape(shape, matrix)
            permutation[index[transformed], j] = 1.0
        representations.append(permutation)

    reversal = np.zeros((dimension, dimension), dtype=float)
    for j, shape in enumerate(shapes):
        reversal[index[reverse_shape(shape)], j] = 1.0

    h1 = np.asarray([[float(x) for x in row] for row in H1])
    h2 = np.asarray([[float(x) for x in row] for row in H2])

    tolerance = 2e-10
    if not np.allclose(h1, h1.T, atol=tolerance):
        raise RuntimeError("numeric H1 symmetry gate failed")
    if not np.allclose(h2, h2.T, atol=tolerance):
        raise RuntimeError("numeric H2 symmetry gate failed")
    if not all(
        np.allclose(h1 @ rho, rho @ h1, atol=tolerance)
        for rho in representations
    ):
        raise RuntimeError("H1 does not commute with O_h")
    if not all(
        np.allclose(h2 @ rho, rho @ h2, atol=tolerance)
        for rho in representations
    ):
        raise RuntimeError("H2 does not commute with O_h")
    if not np.allclose(h1 @ reversal, reversal @ h1, atol=tolerance):
        raise RuntimeError("H1 does not commute with C")
    if not np.allclose(h2 @ reversal, reversal @ h2, atol=tolerance):
        raise RuntimeError("H2 does not commute with C")

    odd = (np.eye(dimension) - reversal) / 2.0
    channel_rows = []

    for irrep in ("A1", "A2", "E", "T1", "T2"):
        for parity in ("+", "-"):
            projector = np.zeros((dimension, dimension), dtype=float)
            for matrix, rho in zip(group, representations):
                projector += irrep_character(irrep, parity, matrix) * rho
            projector *= IRREP_DIMENSIONS[irrep] / 48.0
            channel_projector = odd @ projector

            u, singular_values, _vh = np.linalg.svd(channel_projector)
            rank = int(np.sum(singular_values > 1e-8))
            if rank == 0:
                continue

            basis = u[:, :rank]
            block1 = basis.T @ h1 @ basis
            block2 = basis.T @ h2 @ basis
            first_eigenvalues = np.linalg.eigvalsh(block1)

            # For H1-degenerate exotic channels, H2 itself is the required
            # second-order splitting matrix.
            if np.max(np.abs(first_eigenvalues)) < 1e-9:
                second_eigenvalues = np.linalg.eigvalsh(block2)
            else:
                second_eigenvalues = []
                rounded = np.round(first_eigenvalues, 10)
                for first_value in sorted(set(rounded)):
                    eigenvalues, eigenvectors = np.linalg.eigh(block1)
                    selector = np.where(
                        np.isclose(eigenvalues, first_value, atol=1e-8)
                    )[0]
                    subspace = eigenvectors[:, selector]
                    corrected = subspace.T @ block2 @ subspace
                    second_eigenvalues.extend(
                        float(x) for x in np.linalg.eigvalsh(corrected)
                    )

            channel_rows.append(
                {
                    "channel": f"{J_LABEL[irrep]}{parity}-",
                    "irrep": f"{irrep}{parity}-",
                    "rank": rank,
                    "multiplicity": rank // IRREP_DIMENSIONS[irrep],
                    "first_order_eigenvalues": [
                        float(x) for x in first_eigenvalues
                    ],
                    "second_order_connected_eigenvalues": sorted(
                        float(x) for x in second_eigenvalues
                    ),
                }
            )

    analysis = {
        "meta": {
            "version": "2026-06-14-shell6-full-intermediate-analysis-v1",
            "common_disconnected_vacuum_shift_omitted": True,
            "interpretation": (
                "Channel differences and ordering are exact; add one common "
                "vacuum/self-energy scalar only for absolute masses."
            ),
        },
        "gates": {
            "H1_symmetric": True,
            "H2_symmetric": True,
            "H1_commutes_Oh": True,
            "H2_commutes_Oh": True,
            "H1_commutes_C": True,
            "H2_commutes_C": True,
        },
        "channels": channel_rows,
    }
    output_file.write_text(
        json.dumps(analysis, indent=2, sort_keys=True) + "\n"
    )

    print("PASS O_h x C symmetry gates")
    print("C-ODD SHELL-SIX CHANNELS")
    for row in channel_rows:
        print(
            f"  {row['channel']:>5}: "
            f"H1={row['first_order_eigenvalues']}  "
            f"H2_conn={row['second_order_connected_eigenvalues']}"
        )

    return output_file


def parse_arguments():
    parser = argparse.ArgumentParser(
        description=(
            "Exact connected O(u^2) shell-six C-odd SU(3) engine with full "
            "trace-word intermediate sectors."
        )
    )
    parser.add_argument(
        "--mode",
        choices=("calibrate", "compute", "analyze", "all"),
        default="all",
    )
    parser.add_argument(
        "--matrix",
        type=Path,
        default=Path("shell6_o2_full_intermediate_matrix.json"),
    )
    parser.add_argument(
        "--analysis",
        type=Path,
        default=Path("shell6_o2_full_intermediate_analysis.json"),
    )
    parser.add_argument(
        "--no-resume",
        action="store_true",
        help="discard any existing matrix checkpoint",
    )
    parser.add_argument(
        "--max-columns",
        type=int,
        default=None,
        help="compute only this many new columns, then checkpoint and exit",
    )
    parser.add_argument(
        "--term-cache",
        type=Path,
        default=Path("shell6_o2_full_intermediate_term_cache.pkl"),
        help=(
            "persistent exact topology cache; makes interrupted long runs "
            "resume at the individual first-hop topology level"
        ),
    )
    parser.add_argument(
        "--quiet",
        action="store_true",
    )
    return parser.parse_args()


def production_main():
    args = parse_arguments()
    configure_term_cache(args.term_cache.resolve())

    if args.mode == "calibrate":
        shell4_codd_calibration(verbose=not args.quiet)
        return

    if args.mode in ("compute", "all"):
        build_shell6_matrices(
            args.matrix.resolve(),
            resume=not args.no_resume,
            max_columns=args.max_columns,
            verbose=not args.quiet,
        )

    if args.mode in ("analyze", "all"):
        analyze_shell6_matrix(
            args.matrix.resolve(),
            args.analysis.resolve(),
        )


if __name__ == "__main__":
    production_main()
