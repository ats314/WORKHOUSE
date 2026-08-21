# HODGE v10a.21r — ADJUDICATOR-ONLY RESUME
# ============================================================
# USE THIS IN THE SAME COLAB KERNEL THAT HAS ALREADY REACHED
# SECTION [8] OF v10a.20/v10a.21.
#
# If the current cell is still grinding through section [9],
# INTERRUPT IT first, then run this cell.
#
# This intentionally SKIPS the repeated global v10a.20 exact-D
# Haar sweep.  The exact D_A and m4 values below are frozen from
# the already completed 46/46 v10a.20 certificate.  They are
# used only as regression/adjudication references.
#
# The new work begins immediately at the ROOTED CLUSTER stage.
# Missing exact Haar values are lifted on demand inside the
# support-resolved cluster bilinears.
# ============================================================

from fractions import Fraction as _V21R_F
from collections import defaultdict, Counter
import itertools, heapq, math, time, os

_required = [
    "W1Ls","R1Ls","R12Ls","W2X","R2X","anchor_faces",
    "_x_exactify_labeled","_x_derive_R2","_x_compare_labeled",
    "_v10a13_haar_factor","_qcache","_x_haar_den_bound",
    "_V17_NEIGH","_single_emb","_pairs","_v17_connected",
    "_v17_translate_support","_v10a3_translate_state",
    "_v10a3_translate_sig","_v10a2_sig_canon","_v9_flux_key_state",
    "_joint_canon_states","_x_canon_block_pair","_x_phys_blocks",
    "_x_phys_index","_x_local_patterns_fast","verts","P","gates"
]
_missing=[x for x in _required if x not in globals()]
if _missing:
    raise RuntimeError(
        "This is a SAME-KERNEL resume cell. Missing prerequisites: "
        + ", ".join(_missing)
        + ". If you restarted Colab, run the full v10a.21 notebook instead."
    )

# Exact values already independently certified by the completed v10a.20 run.
D_EXACT = _V21R_F(-361008126292641364183, 7250590288602460800)
M4_EXACT = _V21R_F(-160506019419340168451, 14501180577204921600)

# Reuse any exact Haar values accumulated before interruption.  Starting empty
# is also valid: the adjudicator lifts only the topologies it actually needs.
if "HAAR_EXACT" not in globals():
    HAAR_EXACT = {}
if "LIFT_TOL" not in globals():
    LIFT_TOL = float(os.environ.get("V10A20_LIFT_TOL","1e-5"))

print("="*140)
print("HODGE v10a.21r — ADJUDICATOR-ONLY RESUME")
print("="*140)
print("repeated v10a.20 global Haar sweep : SKIPPED")
print("exact Haar values already cached   :", len(HAAR_EXACT))
print("new work starts                    : rooted support-resolved cluster ledgers")
print("D_A regression reference           :", D_EXACT)
print("m4 regression reference            :", M4_EXACT)
print()
# =============================================================================
# HODGE v10a.21 — EXACT ROOTED MARKED-CLUSTER INCIDENCE ADJUDICATOR
# =============================================================================
#
# Question being decided
# ----------------------
# The exact v10a.20 scalar
#
#   m4_rest = -160506019419340168451 / 14501180577204921600
#
# conflicts with the older record-backed SU(3) Gamma fourth-order scalar q3.
# The most plausible implementation-level concern is whether the v10a.7-v10a.20
# shortcut
#
#   connected marked histories - attached linked vacuum
#
# is actually identical to the full rooted marked-cluster incidence transform.
#
# v10a.21 does that transform explicitly in exact arithmetic.
#
# It DOES NOT merely subtract one global vacuum number.  It reconstructs exact
# support-resolved ledgers for
#
#   D(C), C(C), e2(C), N(C), J(C),
#
# forms the nonlinear fold -e2(C)N(C) at the SUPPORT level via union convolution,
# assigns the exact one-face and adjacent-pair vacuum weights to their concrete
# marked supports, constructs every downward-closed rooted cluster, and performs
#
#   omega(C) = delta(C) - sum_{S proper rooted connected subset C} omega(S)
#
# with literal concrete subsets.  No universal alternating-sign shortcut and no
# orbit multiplicity formula is used.
#
# Evidence boundary
# -----------------
# This adjudicates the linked-cluster transform of the COMPLETE support-resolved
# W1/W2 history corpus already certified by v10a.20.  If it agrees with v10a.20,
# then "missing recursive marked subcluster subtraction" is NOT the source of the
# q3 discrepancy within this corpus.  It does not by itself prove that an omitted
# microscopic history family is impossible; the existing locality/completeness
# gates remain the certificate for that separate issue.
# =============================================================================

print('\n'+'='*140)
print('HODGE v10a.21 — EXACT ROOTED MARKED-CLUSTER INCIDENCE ADJUDICATOR')
print('='*140)

V21_HEART=float(os.environ.get('V10A21_HEARTBEAT','15'))
V21_DENSE_REPS=int(os.environ.get('V10A21_DENSE_REPS','1'))
V21_GATE_START=len(gates)
ROOT=int(anchor_faces[2])

def _v21_prune_ledger(L):
    return {frozenset(S):_XQ(x) for S,x in L.items() if _XQ(x)}

def _v21_add_ledger(dst,src,scale=_XQ(1)):
    scale=_XQ(scale)
    for S,x in src.items():
        dst[frozenset(S)] += scale*_XQ(x)

def _v21_union_convolution(A,B):
    out=defaultdict(_XQ)
    for SA,a in A.items():
        for SB,b in B.items():
            out[frozenset(set(SA)|set(SB))] += _XQ(a)*_XQ(b)
    return _v21_prune_ledger(out)

def _v21_sum(L):
    return sum((_XQ(x) for x in L.values()),_XQ(0))

def _v21_size_table(L):
    n=Counter(); w=defaultdict(_XQ)
    for S,x in L.items():
        n[len(S)] += 1
        w[len(S)] += _XQ(x)
    return dict(sorted(n.items())),dict(sorted(w.items()))

def _v21_haar_exact(a,b):
    key=(a,b)
    q=HAAR_EXACT.get(key)
    if q is not None:
        return q
    qh=_x_haar_den_bound(a,b)
    hf=float(_v10a13_haar_factor.__wrapped__(a,b))
    y=hf*qh
    nh=int(round(y))
    resid=abs(y-nh)
    if resid>=LIFT_TOL:
        raise RuntimeError(
            f'v10a.21 Haar lift ambiguous: qH={qh}, h={hf:.17g}, '
            f'qH*h={y:.17g}, residual={resid:.3e}'
        )
    q=_XQ(nh,qh)
    HAAR_EXACT[key]=q
    return q

def _v21_exactify_and_derive_R(LD,label):
    X=_x_exactify_labeled(LD,label)
    return X,_x_derive_R2(X)

# One-step exact states.  Only W is independently rationalized; R is regenerated
# from the exact electric gap, as in the v10a.20 R2 certificate.
print('\n[11] EXACT ONE-STEP / FOLD HALF-HISTORIES')
W1X,R1X=_v21_exactify_and_derive_R(W1Ls[2],'v10a.21 scaled W1=sqrt(2) W1')
R1X_FLOAT=_x_exactify_labeled(R1Ls[2],'v10a.21 scaled R1=sqrt(2) R1 cold check')
badR1=_x_compare_labeled(R1X,R1X_FLOAT,'R1')
gate('v10a.21 exact R1 equals exact W1/(E0-H0)',
     len(badR1)==0,'exact equality' if not badR1 else badR1[0])

R12X=_x_derive_R2(R1X)
R12X_FLOAT=_x_exactify_labeled(R12Ls[2],'v10a.21 scaled R(R1)=sqrt(2) R^2 W1 cold check')
badR12=_x_compare_labeled(R12X,R12X_FLOAT,'R12')
gate('v10a.21 exact R(R1) equals second exact resolvent application',
     len(badR12)==0,'exact equality' if not badR12 else badR12[0])

def _v21_cluster_bilinear(leftX,rightX,label,skip_11=False,analytic_11=None):
    """Exact Gamma bilinear decomposed by MINIMAL concrete marked support.

    Both input half-states are sqrt(2)-scaled, therefore every bilinear carries
    the physical prefactor 1/2.

    Whole H0 block pairs are canonicalized exactly, but unlike v10a.20 their
    translation multiplicity is retained separately for every concrete union
    support.  Haar is then evaluated once per canonical topology and distributed
    back to those supports.
    """
    RB=_x_phys_index(rightX)
    Litems=[]
    for SL,st in leftX.items():
        for key,lv in _x_phys_blocks(st).items():
            Litems.append((SL,key,lv))
    Litems.sort(key=lambda z:len(z[2]))

    tasks={}
    matches=raw_upper=skipped=0
    t0=time.time(); last=t0
    for ii,(SL,(cs,Esg),lv) in enumerate(Litems):
        for dv in verts:
            tcs=_v10a2_sig_canon(_v10a3_translate_sig(cs,dv))
            candidates=RB.get((tcs,Esg),())
            if not candidates:
                continue
            tv={_v10a3_translate_state(z,dv):c for z,c in lv.items()}
            tSL=_v17_translate_support(SL,dv)
            for SR,rv in candidates:
                matches += 1
                raw_upper += len(tv)*len(rv)
                C=frozenset(set(tSL)|set(SR))
                if ROOT not in C:
                    raise RuntimeError(f'{label}: translated support lost marked root')
                if skip_11 and len(SL)==1 and len(SR)==1:
                    skipped += 1
                    continue
                key,A,B=_x_canon_block_pair(tv,rv)
                rec=tasks.get(key)
                if rec is None:
                    rec=[A,B,defaultdict(int)]
                    tasks[key]=rec
                rec[2][C] += 1
        now=time.time()
        if V10A7_PROGRESS and (now-last>=V21_HEART or ii+1==len(Litems)):
            print(f'      {label} scan {ii+1:,}/{len(Litems):,}; '
                  f'matches={matches:,}; block-types={len(tasks):,}; '
                  f'raw-pairs<={raw_upper:,}; elapsed={now-t0:.1f}s',flush=True)
            last=now

    # state-pair topology -> concrete support -> exact coefficient weight
    pairC={}
    pair_occ=0
    recs=list(tasks.values())
    t1=time.time(); last=t1
    for ti,(A,B,cmult) in enumerate(recs):
        ga=defaultdict(list); gb=defaultdict(list)
        for z,c in A: ga[_v9_flux_key_state(z)].append((z,c))
        for z,c in B: gb[_v9_flux_key_state(z)].append((z,c))
        for fk,la in ga.items():
            lb=gb.get(fk)
            if not lb: continue
            for aa,ca in la:
                for bb,cb in lb:
                    x,y=_joint_canon_states(aa,bb)
                    if (y.occ,y.part)<(x.occ,x.part):
                        x,y=y,x
                    pk=(x,y)
                    d=pairC.get(pk)
                    if d is None:
                        d=defaultdict(_XQ); pairC[pk]=d
                    base=_XQ(ca)*_XQ(cb)
                    for C,m in cmult.items():
                        d[C] += int(m)*base
                        pair_occ += int(m)
        now=time.time()
        if V10A7_PROGRESS and (now-last>=V21_HEART or ti+1==len(recs)):
            print(f'      {label} collapse {ti+1:,}/{len(recs):,}; '
                  f'occurrences={pair_occ:,}; topologies={len(pairC):,}; '
                  f'elapsed={now-t1:.1f}s',flush=True)
            last=now

    # Remove exact cancellations.
    pairC2={}
    for pk,d in pairC.items():
        z={C:w for C,w in d.items() if w}
        if z: pairC2[pk]=z
    pairC=pairC2

    # Cold endpoint-signature representatives against dense Haar.
    reps={}
    for a,b in pairC:
        sig=tuple(sorted(_x_local_patterns_fast(a,b)))
        reps.setdefault(sig,(a,b))
    maxdense=0.0
    if V21_DENSE_REPS:
        for sig,(a,b) in reps.items():
            q=_v21_haar_exact(a,b)
            hd=float(_qcache(a,b))
            maxdense=max(maxdense,abs(float(q)-hd))
    gate(f'{label} exact Haar lift agrees with dense endpoint representatives',
         maxdense<5e-12,
         f'signatures={len(reps)}, maxerr={maxdense:.3e}')

    ledger=defaultdict(_XQ)
    t2=time.time(); last=t2
    for pi,((a,b),d) in enumerate(pairC.items(),1):
        h=_v21_haar_exact(a,b)
        if h:
            for C,w in d.items():
                ledger[C] += _XQ(1,2)*w*h
        now=time.time()
        if V10A7_PROGRESS and (now-last>=V21_HEART or pi%5000==0 or pi==len(pairC)):
            print(f'      {label} distribute {pi:,}/{len(pairC):,}; '
                  f'supports={len(ledger):,}; elapsed={now-t2:.1f}s',flush=True)
            last=now

    if analytic_11 is not None:
        ledger[frozenset((ROOT,))] += _XQ(analytic_11)

    ledger=_v21_prune_ledger(ledger)
    bad=[S for S in ledger if ROOT not in S or not _v17_connected(S)]
    gate(f'{label} every nonzero minimal support is rooted and connected',
         len(bad)==0,f'bad={len(bad)}')
    n,w=_v21_size_table(ledger)
    print(f'      {label} MINIMAL-SUPPORT LEDGER sizes={n}')
    print(f'      {label} size sums={w}')
    print(f'      {label} TOTAL={_v21_sum(ledger)}')
    return ledger,dict(matches=matches,raw_upper=raw_upper,skipped=skipped,
                       block_types=len(tasks),pair_occ=pair_occ,
                       topology_count=len(pairC),support_count=len(ledger))

print('\n[12] EXACT SUPPORT-RESOLVED FOUR-MOMENT LEDGERS')

D_MIN,DSTAT=_v21_cluster_bilinear(
    W2X,R2X,'v10a.21 D',skip_11=True,analytic_11=_XQ(-13,896)
)
E2_MIN,E2STAT=_v21_cluster_bilinear(W1X,R1X,'v10a.21 e2')
N_MIN,NSTAT=_v21_cluster_bilinear(R1X,R1X,'v10a.21 N')
J_MIN,JSTAT=_v21_cluster_bilinear(R1X,R12X,'v10a.21 J')
C_MIN,CSTAT=_v21_cluster_bilinear(R1X,R2X,'v10a.21 C')

gate('v10a.21 support-resolved D sums to exact v10a.20 D_A',
     _v21_sum(D_MIN)==D_EXACT,_v21_sum(D_MIN))
gate('v10a.21 support-resolved e2 sums to -5945/612',
     _v21_sum(E2_MIN)==_XQ(-5945,612),_v21_sum(E2_MIN))
gate('v10a.21 support-resolved N sums to 511051/124848',
     _v21_sum(N_MIN)==_XQ(511051,124848),_v21_sum(N_MIN))
gate('v10a.21 support-resolved J sums to -48945521/25468992',
     _v21_sum(J_MIN)==_XQ(-48945521,25468992),_v21_sum(J_MIN))
gate('v10a.21 support-resolved C cancels exactly at Gamma',
     _v21_sum(C_MIN)==0,_v21_sum(C_MIN))

# The nonlinear fold must be done BEFORE the cluster transform.  Its support
# ledger is the exact union convolution of the e2 and N minimal ledgers.
E2N_MIN=_v21_union_convolution(E2_MIN,N_MIN)

EA_MIN=defaultdict(_XQ)
_v21_add_ledger(EA_MIN,D_MIN,+1)
_v21_add_ledger(EA_MIN,C_MIN,-2)
_v21_add_ledger(EA_MIN,E2N_MIN,-1)
_v21_add_ledger(EA_MIN,J_MIN,+1)
EA_MIN=_v21_prune_ledger(EA_MIN)

EA_EXACT=D_EXACT - 2*_v21_sum(C_MIN) - _XQ(-5945,612)*_XQ(511051,124848) + _XQ(-48945521,25468992)
gate('v10a.21 nonlinear support fold sums to exact connected axial e4',
     _v21_sum(EA_MIN)==EA_EXACT,
     _v21_sum(EA_MIN))

print('\n  CONNECTED AXIAL MINIMAL-SUPPORT LEDGER')
na,wa=_v21_size_table(EA_MIN)
print('    nonzero clusters by size =',na)
print('    exact size sums          =',wa)
print('    exact total e4_A         =',_v21_sum(EA_MIN))

# ---------------------------------------------------------------------
# Exact vacuum linked ledger attached to the marked source.
# ---------------------------------------------------------------------
print('\n[13] EXACT ATTACHED-VACUUM MARKED-SUPPORT LEDGER')
V_MIN=defaultdict(_XQ)
V1=_XQ(-39,1280)
VPAIR=_XQ(-327,83776)

for f in _single_emb:
    C=frozenset((ROOT,int(f)))
    V_MIN[C] += V1
for S in _pairs:
    C=frozenset(set(map(int,S))|{ROOT})
    V_MIN[C] += VPAIR
V_MIN=_v21_prune_ledger(V_MIN)

gate('v10a.21 concrete vacuum marked-support ledger sums to exact attached subtraction',
     _v21_sum(V_MIN)==_XQ(-1474623,1675520),
     _v21_sum(V_MIN))
nv,wv=_v21_size_table(V_MIN)
print('    nonzero marked supports by size =',nv)
print('    exact size sums                 =',wv)

# Irreducible marked-history ledger before recursive incidence audit.
DELTA_MIN=defaultdict(_XQ)
_v21_add_ledger(DELTA_MIN,EA_MIN,+1)
_v21_add_ledger(DELTA_MIN,V_MIN,-1)
DELTA_MIN=_v21_prune_ledger(DELTA_MIN)

M4_FROM_MIN=_v21_sum(DELTA_MIN)
gate('v10a.21 minimal marked-history ledger sums to exact v10a.20 m4',
     M4_FROM_MIN==M4_EXACT,M4_FROM_MIN)

# ---------------------------------------------------------------------
# Build the literal downward-closed concrete rooted cluster poset.
# ---------------------------------------------------------------------
print('\n[14] LITERAL ROOTED CLUSTER POSET + RECURSIVE INCIDENCE TRANSFORM')

def _v21_rooted_connected_subsets_of(C):
    C=frozenset(map(int,C))
    if ROOT not in C:
        return ()
    rest=tuple(sorted(set(C)-{ROOT}))
    out=[]
    for mask in range(1<<len(rest)):
        S={ROOT}
        for i,f in enumerate(rest):
            if (mask>>i)&1:
                S.add(f)
        F=frozenset(S)
        if _v17_connected(F):
            out.append(F)
    return tuple(out)

CLUSTERS=set()
for C in DELTA_MIN:
    CLUSTERS.update(_v21_rooted_connected_subsets_of(C))
CLUSTERS=sorted(CLUSTERS,key=lambda S:(len(S),tuple(sorted(S))))

gate('v10a.21 rooted cluster poset is downward closed',
     all(S in set(CLUSTERS) for C in CLUSTERS for S in _v21_rooted_connected_subsets_of(C)),
     f'clusters={len(CLUSTERS)}')

# Raw finite-cluster coefficient reconstructed from all minimal histories that fit C.
# This is the exact order-four finite-cluster incidence function of the history corpus.
RAW={}
for C in CLUSTERS:
    x=_XQ(0)
    for S,w in DELTA_MIN.items():
        if S.issubset(C):
            x += w
    RAW[C]=x

# Literal recursive transform.  Every concrete proper rooted connected subset is
# subtracted once; repeated shape embeddings appear as distinct concrete subsets.
OMEGA={}
max_resid=_XQ(0)
for C in CLUSTERS:
    x=RAW[C]
    for S in _v21_rooted_connected_subsets_of(C):
        if S!=C:
            x -= OMEGA[S]
    OMEGA[C]=x
    resid=x-DELTA_MIN.get(C,_XQ(0))
    if resid:
        max_resid=resid
        break

gate('v10a.21 recursive incidence transform exactly recovers minimal-support weights',
     max_resid==0,
     'exact identity' if max_resid==0 else max_resid)

OMEGA_NZ={C:w for C,w in OMEGA.items() if w}
M4_MOBIUS=_v21_sum(OMEGA_NZ)
gate('v10a.21 full rooted recursive linked sum equals exact v10a.20 m4',
     M4_MOBIUS==M4_EXACT,M4_MOBIUS)

nm,wm=_v21_size_table(OMEGA_NZ)
print('  rooted cluster count (including zero weights) =',len(CLUSTERS))
print('  nonzero irreducible marked clusters by size  =',nm)
print('  exact linked weight by cluster size          =',wm)
print('  exact recursive linked total                 =',M4_MOBIUS)

# Stronger spectator statement at the incidence-function level:
# adjoining a concrete disconnected face cannot change RAW because no minimal
# marked history has disconnected support.
_far21=next(int(f) for f in range(P)
            if f!=ROOT and f not in _V17_NEIGH[ROOT])
_base_candidates=[C for C in CLUSTERS if len(C)<=3 and _far21 not in C]
spec_bad=[]
for C in _base_candidates[:min(200,len(_base_candidates))]:
    Cf=frozenset(set(C)|{_far21})
    # raw support sum without imposing connectedness
    a=sum((w for S,w in DELTA_MIN.items() if S.issubset(C)),_XQ(0))
    b=sum((w for S,w in DELTA_MIN.items() if S.issubset(Cf)),_XQ(0))
    if a!=b:
        spec_bad.append((C,a,b))
        break
gate('v10a.21 disconnected-spectator invariance holds on exact marked incidence ledger',
     len(spec_bad)==0,'checked='+str(min(200,len(_base_candidates))))

# ---------------------------------------------------------------------
# Blind historical adjudication: load q3 ONLY AFTER the new recursive result.
# ---------------------------------------------------------------------
print('\n[15] BLIND HISTORICAL q3 ADJUDICATION')
Q3_OLD=_XQ(-20721577909065127111,7250590288602460800)
print('  exact v10a.21 recursive m4 =',M4_MOBIUS)
print('  older record-backed q3      =',Q3_OLD)
print('  exact difference            =',M4_MOBIUS-Q3_OLD)
print('  decimal new/old             =',float(M4_MOBIUS),float(Q3_OLD))

NEW_MATCH=(M4_MOBIUS==M4_EXACT)
OLD_MATCH=(M4_MOBIUS==Q3_OLD)

gate('v10a.21 adjudicator selects exactly one of {new exact m4, old q3}',
     int(NEW_MATCH)+int(OLD_MATCH)==1,
     f'new={NEW_MATCH}, old={OLD_MATCH}')

if NEW_MATCH and not OLD_MATCH:
    VERDICT='ROOTED INCIDENCE TRANSFORM SUPPORTS v10a.20; OLD q3 IS NOT RECOVERED'
elif OLD_MATCH and not NEW_MATCH:
    VERDICT='ROOTED INCIDENCE TRANSFORM RECOVERS OLD q3; v10a.20 SHORTCUT FAILED'
else:
    VERDICT='INCONCLUSIVE / THIRD VALUE'

print('\n  VERDICT:',VERDICT)

# ---------------------------------------------------------------------
# Final certificate summary.
# ---------------------------------------------------------------------
print('\n'+'='*140)
print('FINAL v10a.21 GATE SUMMARY')
print('='*140)
g21=gates[V21_GATE_START:]
for i,(n,ok,d) in enumerate(g21,1):
    print(f'{i:02d}. {"PASS" if ok else "FAIL"} — {n}'+(f' :: {d}' if d else ''))
print('-'*140)
print(f'PASSED {sum(ok for _,ok,_ in g21)}/{len(g21)} v10a.21 GATES')
if not all(ok for _,ok,_ in g21):
    raise AssertionError('v10a.21 rooted-cluster adjudication gate failure')

print('\nV10A.21 CONCLUSION')
print('------------------')
print('* All four Feshbach moments were reconstructed as exact concrete support ledgers.')
print('* The nonlinear -e2*N fold was performed by exact support-union convolution BEFORE linked subtraction.')
print('* Vacuum one-face and adjacent-pair weights were assigned to their literal marked supports.')
print('* The rooted cluster poset was made downward-closed and transformed by literal recursive subset incidence.')
print('* No universal alternating-sign Mobius shortcut was used.')
print('* The historical q3 number was loaded only after the recursive linked result was complete.')
print('* Evidence boundary: this closes the linked-transform question for the certified support-resolved history corpus;')
print('  it does not independently reconstruct a hypothetical history family absent from that corpus.')
print('* VERDICT:',VERDICT)
