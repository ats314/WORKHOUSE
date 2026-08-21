#!/usr/bin/env python3
# ENGINE_OP1_za_overlap_f042.py — F042. Confirm the F041 heavy-tail MECHANISM: the records where
# the source-tilted amplification Amp(s)=nu^{B,s}(C_p)/nu(C_p) reaches (1+s)^2-(1+s)^3
# are exactly those where the target cap C_p overlaps SEVERAL incident caps.
#
# Per (e,p) record (vMF(m_e,kappa) MC, same geometry as F041):
#   pairwise conditional lift  L_r = nu(C_p|C_r)/nu(C_p)  for each of the 5 incident caps r
#   effective overlap count    k_eff = #{ r : L_r >= LTH }   (LTH=2: cap r at least doubles P(C_p))
#   full-conditioning lift     Lfull = nu(C_p|C_B)/nu(C_p)   (B = all 5 incident caps)
#   Amp(s) for s in {1,2,4} (product form, F041)
# Claim to test: (i) Amp(s) stratified by k_eff tracks (1+s)^{k_eff}; (ii) the heavy tail
# (top-1% Amp(4)) is concentrated on k_eff>=2; (iii) s->inf limit Amp(s)->Lfull.
#
# Gates: G-RT1 vMF sampler vs Bessel I2/I1; G-RT2 MC cap prob vs 1-D quadrature;
#   G-OV1 Amp(s=64) ~ Lfull within MC tol (s->inf interpretation); G-OV2 s=0 => Amp=1.
import json, math, os, sys, time, argparse
import numpy as np
from scipy.special import iv
HERE=os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0,HERE)
import ENGINE_PMBSF_su2hb_f041 as hb
import ENGINE_FLUX_lci_typicality_diagnostic as lci
S_LIST=[0.0,1.0,2.0,4.0,64.0]; LTH=2.0; MINHIT=40

def vmf_batch(mean_dir,kappa,n,rng):
    p=4
    if kappa<1e-10:
        v=rng.standard_normal((n,p)); return v/np.linalg.norm(v,axis=1,keepdims=True)
    b=(-2.0*kappa+math.sqrt(4.0*kappa*kappa+(p-1)**2))/(p-1)
    x0=(1.0-b)/(1.0+b); c=kappa*x0+(p-1)*math.log(1.0-x0*x0)
    w=np.empty(n); filled=0
    while filled<n:
        m_=2*(n-filled)+16
        z=rng.beta((p-1)/2.0,(p-1)/2.0,size=m_)
        wc=(1.0-(1.0+b)*z)/(1.0-(1.0-b)*z)
        logu=np.log(rng.uniform(size=m_))
        acc=kappa*wc+(p-1)*np.log(np.clip(1.0-x0*wc,1e-300,None))-c>=logu
        wa=wc[acc]; take=min(len(wa),n-filled); w[filled:filled+take]=wa[:take]; filled+=take
    V=rng.standard_normal((n,p)); V=V-(V@mean_dir)[:,None]*mean_dir[None,:]
    V=V/np.linalg.norm(V,axis=1,keepdims=True)
    return w[:,None]*mean_dir[None,:]+np.sqrt(np.maximum(0.0,1.0-w*w))[:,None]*V

def nu_cap_quad(kappa,c,a,Nw=4000):
    w=np.linspace(-1,1,Nw); fw=np.exp(kappa*(w-1.0))*np.sqrt(np.maximum(0,1-w*w))
    sp=math.sqrt(max(0.0,1-c*c)); denom=sp*np.sqrt(np.maximum(1e-300,1-w*w))
    py=np.clip(((a-c*w)/denom+1.0)/2.0,0.0,1.0)
    return float(np.trapezoid(fw*py,w)/np.trapezoid(fw,w))

def gate_rt1(rng):
    res={}
    for kap in (8.0,18.0,40.0):
        m=np.array([1.0,0,0,0]); u=vmf_batch(m,kap,200000,rng)
        emp=float((u@m).mean()); bess=float(iv(2,kap)/iv(1,kap))
        res[kap]=(emp,bess); assert abs(emp-bess)<0.01, f'G-RT1 {kap}'
    return res
def gate_rt2(rng):
    worst=0.0
    for _ in range(6):
        m=rng.standard_normal(4); m/=np.linalg.norm(m); n=rng.standard_normal(4); n/=np.linalg.norm(n)
        a=float(rng.uniform(-0.2,0.2)); c=float(m@n)
        u=vmf_batch(m,18.0,300000,rng); mc=float(((u@n)<=a).mean())
        qd=nu_cap_quad(18.0,c,a); se=math.sqrt(max(mc*(1-mc),1e-9)/300000)
        worst=max(worst,abs(mc-qd)); assert abs(mc-qd)<5*se+2e-3, 'G-RT2'
    return worst

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--L',type=int,required=True); ap.add_argument('--ncfg',type=int,default=8)
    ap.add_argument('--N',type=int,default=60000); ap.add_argument('--nlinks',type=int,default=30)
    ap.add_argument('--beta',type=float,default=3.5); ap.add_argument('--target',type=int,default=80)
    ap.add_argument('--deadline',type=float,default=40.0); ap.add_argument('--use-stored',action='store_true')
    a_=ap.parse_args(); T0=time.time(); L=a_.L; BETA=a_.beta
    t_param=1.0104245908659366; eta=0.005; aCAP=1.0-(t_param-eta)
    rng=np.random.default_rng(720000+L); g1=gate_rt1(rng); g2=gate_rt2(rng)
    CM=1 if L<6 else 2; blk=lci.Block(origin=tuple([0]*4),side=L,core_margin=CM)
    ov1=0.0  # G-OV1 worst |Amp(64)-Lfull|/Lfull
    rows=[]   # (keff, amp1, amp2, amp4, Lfull, maxLr)
    def measure(U,seed):
        nonlocal ov1
        rs=np.random.default_rng(seed); links=sorted(lci.core_links(blk,L)); rs.shuffle(links); links=links[:a_.nlinks]
        rmc=np.random.default_rng(seed^0x2545f491)
        for (x,mu) in links:
            normals,_=lci.link_normals(U,x,mu,L); He=normals.sum(axis=0); hn=float(np.linalg.norm(He))
            if hn<1e-12: continue
            m_e=He/hn; kap=BETA*hn
            u=vmf_batch(m_e,kap,a_.N,rmc); ind=(u@normals.T<=aCAP).astype(np.float64)
            for tix in range(6):
                others=[i for i in range(6) if i!=tix]; bp=ind[:,tix]
                hits=float(bp.sum()); nu_p=hits/a_.N
                if hits<MINHIT: continue
                lifts=[]
                for r in others:
                    nu_r=float(ind[:,r].mean()); nu_pr=float((bp*ind[:,r]).mean())
                    lifts.append((nu_pr/nu_r)/nu_p if (nu_r>0 and nu_p>0) else 0.0)
                lifts=np.array(lifts); keff=int(np.sum(lifts>=LTH)); maxLr=float(lifts.max())
                capB=np.prod(ind[:,others],axis=1); nu_B=float(capB.mean())
                Lfull=((bp*capB).mean()/nu_B)/nu_p if nu_B>0 else float('nan')
                amps={}
                for s in S_LIST:
                    Wt=np.prod(1.0+s*ind[:,others],axis=1); mw=float(Wt.mean())
                    amps[s]=(float((bp*Wt).mean())/mw)/nu_p if mw>0 else float('nan')
                if np.isfinite(Lfull) and Lfull>0 and np.isfinite(amps[64.0]):
                    ov1=max(ov1,abs(amps[64.0]-Lfull)/Lfull)
                rows.append((keff,amps[1.0],amps[2.0],amps[4.0],Lfull,maxLr))
            if (time.time()-T0)>a_.deadline-3.0: break
    if a_.use_stored:
        U=np.load(f'{HERE}/vsL_state_L{L}.npz')['U']; measure(U,123+L); nc=1; plaq=float(hb.mean_plaq(U))
    else:
        nc=0; plaq=0.0
        for ci in range(a_.ncfg):
            if (time.time()-T0)>a_.deadline-8.0: break
            U=np.zeros((L,L,L,L,4,4)); U[...,0]=1.0; rt=np.random.default_rng(20260613+1000*L+ci)
            for _ in range(a_.target): hb.thermalize_vec(L,BETA,1,rt,log_every=0,U=U)
            measure(U,5000+13*L+ci); nc+=1; plaq=float(hb.mean_plaq(U))
    assert rows, 'no records'
    assert ov1<0.06, f'G-OV1 fail {ov1}'   # Amp(64) ~ Lfull (s->inf interpretation), MC-loose
    R=np.array(rows); keff=R[:,0].astype(int); amp4=R[:,3]
    # stratify Amp(s) by k_eff
    strat={}
    for k in sorted(set(keff.tolist())):
        sel=keff==k
        strat[int(k)]={'n':int(sel.sum()),
            'amp1_med':float(np.median(R[sel,1])),'amp2_med':float(np.median(R[sel,2])),
            'amp4_med':float(np.median(R[sel,3])),'amp4_mean':float(np.mean(R[sel,3])),
            'Lfull_med':float(np.median(R[sel,4]))}
    # heavy tail: top 1% by Amp(4)
    thr=np.quantile(amp4,0.99); tail=amp4>=thr
    tail_keff=R[tail,0].astype(int)
    out={'tag':'F042','L':L,'beta':BETA,'a':aCAP,'core_margin':CM,'N_mc':a_.N,'ncfg':nc,
         'LTH':LTH,'MINHIT':MINHIT,'n_records':int(R.shape[0]),'mean_plaq':plaq,
         'G-RT1':{str(k):v for k,v in g1.items()},'G-RT2':float(g2),'G-OV1_Amp64_vs_Lfull':float(ov1),
         'gates':'G-RT1,G-RT2,G-OV1 PASS',
         'keff_hist':{int(k):int(np.sum(keff==k)) for k in sorted(set(keff.tolist()))},
         'amp4_q99_threshold':float(thr),
         'tail_keff_hist':{int(k):int(np.sum(tail_keff==k)) for k in sorted(set(tail_keff.tolist()))},
         'tail_frac_keff_ge2':float(np.mean(tail_keff>=2)),
         'bulk_frac_keff_le1':float(np.mean(R[~tail,0]<=1)),
         'strat_by_keff':strat}
    json.dump(out,open(f'{HERE}/overlap_L{L}.json','w'),indent=1)
    print('=== F042 cap-overlap mechanism  L=%d records=%d ncfg=%d N=%d ==='%(L,R.shape[0],nc,a_.N))
    print('  G-RT1 %s | G-RT2 %.1e | G-OV1 Amp(64)~Lfull worst %.3f  PASS'%(
        ' '.join('k%d:%.3f/%.3f'%(int(k),v[0],v[1]) for k,v in g1.items()),g2,ov1))
    print('  k_eff histogram (LTH=%.0f): %s'%(LTH,out['keff_hist']))
    print('  Amp(s) stratified by k_eff  [k: n  med Amp1 / Amp2 / Amp4   (1+s)^k ref: 2^k/3^k/5^k]')
    for k,d in strat.items():
        print('    k=%d n=%-4d  %6.2f / %6.2f / %7.2f    ref %d/%d/%d'%(
            k,d['n'],d['amp1_med'],d['amp2_med'],d['amp4_med'],2**k,3**k,5**k))
    print('  heavy tail (top 1%% Amp4, thr=%.1f): k_eff hist %s  => frac k_eff>=2 = %.2f'%(
        thr,out['tail_keff_hist'],out['tail_frac_keff_ge2']))
    print('  bulk (lower 99%%): frac k_eff<=1 = %.3f'%out['bulk_frac_keff_le1'])
    print('MEASURE_DONE')

if __name__=='__main__': main()
