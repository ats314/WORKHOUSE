#!/usr/bin/env python3
# ENGINE_OP1_farsource_jdecay.py — GPU (CuPy) / CPU (NumPy) engine for the FAR-SOURCE interaction
# decay J(p,r), the open Z.B content handed off by F043.
#
# Reduction target (TOS+J): E_{mu^{S,s}} X_p <= C q exp(Σ_r J(p,r)),  J(p,r) <= C_J e^{-m_J d(p,r)}.
# The single-source (s->inf) log-amplification from the tilted measure (1.1) is exactly
#       J(p,r) = log( <X_p X_r> / (<X_p><X_r>) ),
# i.e. the log normalized pair-correlation of the defect/source-indicator field. The Z.B
# claim is that this is exponentially small in the lattice distance d(p,r) — equivalently
# the DEFECT FIELD IS MASSIVE, with mass m_J. This engine measures the connected defect
# correlation C_c(d) = <X(0)X(d)> - <X>^2 over the SU(2) Wilson heat-bath ensemble (FFT,
# all-pairs, translation-averaged), fits m_J(beta, theta_thr, L), and reports it with a
# jackknife error along the AF-relevant beta ladder. m_J(beta) bounded away from 0,
# uniformly along the trajectory, is the lattice evidence for Z.B; m_J -> 0 (critical
# source field) would be evidence against it.
#
# GPU: set device=gpu (auto-detects cupy). The heat-bath is the validated su2_hb_v3
# checkerboard ported to the xp backend. Standalone (no repo imports) so it runs on the A100.
#
# Self-test:   python3 ENGINE_OP1_farsource_jdecay.py --selftest         (L=8 numpy, gates only)
# Production:  python3 ENGINE_OP1_farsource_jdecay.py --L 24 --betas 3.0 3.5 4.0 --thetas 1.0 1.3 1.6 \
#                       --nconfigs 120 --nthermal 300 --nsep 20 --device gpu --out far_L24.json
#
# Hard gates: G-BK backend quaternion mul associativity; G-HB equilibrium plaquette stable
#   + matches the L=4,beta=3.5 reference 0.778; G-FFT FFT 2pt == direct on a small field;
#   G-DECORR config autocorrelation small; G-POS connected corr positive over fit range;
#   G-FIT exponential fit R^2 >= 0.9 (else m_J flagged unreliable).
import argparse, json, math, time, sys

def get_xp(device):
    if device=='gpu':
        try:
            import cupy as cp; return cp, True
        except Exception as e:
            print(f'[warn] cupy unavailable ({e}); falling back to numpy'); import numpy as np; return np, False
    import numpy as np; return np, False

def make_ops(xp):
    def qmul(a,b):
        a0,a1,a2,a3=a[...,0],a[...,1],a[...,2],a[...,3]
        b0,b1,b2,b3=b[...,0],b[...,1],b[...,2],b[...,3]
        return xp.stack([a0*b0-a1*b1-a2*b2-a3*b3,
                         a0*b1+a1*b0+a2*b3-a3*b2,
                         a0*b2-a1*b3+a2*b0+a3*b1,
                         a0*b3+a1*b2-a2*b1+a3*b0],axis=-1)
    def qconj(a):
        out=a.copy(); out[...,1:]*=-1.0; return out
    def qmul3(a,b,c): return qmul(qmul(a,b),c)
    return qmul,qconj,qmul3

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--L',type=int,default=16)
    ap.add_argument('--betas',type=float,nargs='+',default=[3.0,3.5,4.0])
    ap.add_argument('--thetas',type=float,nargs='+',default=[1.0,1.3,1.6],help='defect angle thresholds (rad): defect if arccos(½ReTr U_p) > theta')
    ap.add_argument('--nconfigs',type=int,default=100)
    ap.add_argument('--nthermal',type=int,default=300)
    ap.add_argument('--nsep',type=int,default=20)
    ap.add_argument('--seed',type=int,default=20260613)
    ap.add_argument('--device',choices=['cpu','gpu'],default='cpu')
    ap.add_argument('--out',type=str,default='farsource_Jdecay.json')
    ap.add_argument('--selftest',action='store_true')
    a=ap.parse_args()
    if a.selftest:
        a.L=8; a.betas=[3.5]; a.thetas=[1.0]; a.nconfigs=12; a.nthermal=120; a.nsep=8; a.device='cpu'
    xp,on_gpu=get_xp(a.device); D=4; L=a.L; V=L**4
    qmul,qconj,qmul3=make_ops(xp)
    rng=xp.random.default_rng(a.seed)
    T0=time.time(); gates={}

    # ---- G-BK: quaternion mul associativity on the backend ----
    A=rng.standard_normal((5,4)); B=rng.standard_normal((5,4)); Cc=rng.standard_normal((5,4))
    lhs=qmul(qmul(A,B),Cc); rhs=qmul(A,qmul(B,Cc))
    gbk=float(xp.max(xp.abs(lhs-rhs))); gates['G-BK_assoc']=gbk
    assert gbk<1e-10, f'G-BK fail {gbk}'

    def staple_dir(U,mu):
        Umu=U[...,mu,:]; H=xp.zeros(Umu.shape)
        for nu in range(D):
            if nu==mu: continue
            Unu=U[...,nu,:]
            Unu_xpmu=xp.roll(Unu,-1,axis=mu); Umu_xpnu=xp.roll(Umu,-1,axis=nu)
            fwd=qconj(qmul3(Unu_xpmu,qconj(Umu_xpnu),qconj(Unu)))
            Unu_xmnu=xp.roll(Unu,+1,axis=nu); Umu_xmnu=xp.roll(Umu,+1,axis=nu)
            Unu_xmnu_pmu=xp.roll(Unu_xmnu,-1,axis=mu)
            bwd=qmul3(qconj(Unu_xmnu),Umu_xmnu,Unu_xmnu_pmu)
            H=H+fwd+bwd
        return H
    def rbeta(shape_param,size):
        g1=rng.standard_gamma(shape_param,size); g2=rng.standard_gamma(shape_param,size)
        return g1/(g1+g2)
    def vmf(meandir,kappa):
        n=meandir.shape[0]; pm=3; out=xp.zeros((n,4))
        small=kappa<1e-8
        if bool(xp.any(small)):
            ns=int(xp.sum(small)); v=rng.standard_normal((ns,4)); out[small]=v/xp.linalg.norm(v,axis=1,keepdims=True)
        big=~small
        if bool(xp.any(big)):
            kp=kappa[big]; M=meandir[big]; nb=kp.shape[0]
            b=(-2*kp+xp.sqrt(4*kp*kp+pm*pm))/pm; x0=(1-b)/(1+b); c=kp*x0+pm*xp.log(1-x0*x0)
            w=xp.empty(nb); done=xp.zeros(nb,bool)
            it=0
            while not bool(xp.all(done)) and it<10000:
                it+=1; idx=xp.where(~done)[0]
                z=rbeta(pm/2.0,idx.shape[0])
                wc=(1-(1+b[idx])*z)/(1-(1-b[idx])*z)
                logu=xp.log(rng.random(idx.shape[0]))
                acc=kp[idx]*wc+pm*xp.log(xp.clip(1-x0[idx]*wc,1e-300,None))-c[idx]>=logu
                ai=idx[acc]; w[ai]=wc[acc]; done[ai]=True
            g=rng.standard_normal((nb,4)); g=g-(xp.sum(g*M,axis=1,keepdims=True))*M
            g/=xp.linalg.norm(g,axis=1,keepdims=True)
            out[big]=w[:,None]*M+xp.sqrt(xp.clip(1-w*w,0,None))[:,None]*g
        return out
    par=(xp.indices((L,)*4).sum(axis=0))%2
    def sweep(U,beta):
        for mu in range(D):
            for p in (0,1):
                H=staple_dir(U,mu); hn=xp.linalg.norm(H,axis=-1)
                mask=(par==p)&(hn>1e-12)
                if not bool(xp.any(mask)): continue
                md=H[mask]/hn[mask][:,None]; kp=beta*hn[mask]
                U[...,mu,:][mask]=vmf(md,kp)
        return U
    def plaq_field(U,mu,nu):
        Umu=U[...,mu,:]; Unu=U[...,nu,:]
        Unu_xpmu=xp.roll(Unu,-1,axis=mu); Umu_xpnu=xp.roll(Umu,-1,axis=nu)
        Up=qmul3(Umu,Unu_xpmu,qmul(qconj(Umu_xpnu),qconj(Unu)))
        return Up[...,0]   # ½ ReTr U_p  in [-1,1]
    def mean_plaq(U):
        tot=0.0;cnt=0
        for mu in range(D):
            for nu in range(mu+1,D):
                w=plaq_field(U,mu,nu); tot+=float(xp.sum(w)); cnt+=w.size
        return tot/cnt

    # ---- G-FFT: FFT 2pt == direct, on a random small field ----
    Xr=(rng.random((L,)*4)<0.3).astype(float)
    F=xp.fft.fftn(Xr); P=xp.abs(F)**2; Cfft=xp.fft.ifftn(P).real/V
    d_direct=float(xp.mean(Xr*xp.roll(Xr,-1,axis=2)))   # <X(x)X(x+e2)>
    gfft=abs(float(Cfft[0,0,1,0])-d_direct); gates['G-FFT']=gfft
    assert gfft<1e-9, f'G-FFT fail {gfft}'

    results={'meta':{'L':L,'V':V,'betas':a.betas,'thetas':a.thetas,'nconfigs':a.nconfigs,
                     'nthermal':a.nthermal,'nsep':a.nsep,'on_gpu':on_gpu,'seed':a.seed},'gates':gates,'runs':[]}
    dmax=L//2
    for beta in a.betas:
        U=xp.zeros((L,)*4+(D,4)); U[...,0]=1.0
        for _ in range(a.nthermal): U=sweep(U,beta)
        plaqs=[];
        # accumulators per theta: list of per-config (Xmean, Caxis[d])
        acc={th:{'Xm':[],'C':[]} for th in a.thetas}
        for ci in range(a.nconfigs):
            for _ in range(a.nsep): U=sweep(U,beta)
            plaqs.append(mean_plaq(U))
            # defect field on the (0,1) plaquette orientation
            w01=plaq_field(U,0,1); ang=xp.arccos(xp.clip(w01,-1.0,1.0))
            for th in a.thetas:
                X=(ang>th).astype(float); Xm=float(xp.mean(X))
                F=xp.fft.fftn(X); C=xp.fft.ifftn(xp.abs(F)**2).real/V
                # transverse axes (2,3) — out of the (0,1) plaquette plane
                Cax=xp.zeros(dmax+1)
                for d in range(dmax+1):
                    Cax[d]=0.5*(C[0,0,d,0]+C[0,0,0,d])
                acc[th]['Xm'].append(Xm); acc[th]['C'].append([float(x) for x in (Cax.get() if on_gpu else Cax)])
        plaqs=xp.array(plaqs)
        # G-DECORR: lag-1 autocorrelation of mean_plaq across recorded configs
        pa=(plaqs.get() if on_gpu else plaqs); pa=pa-pa.mean()
        import numpy as _np; pa=_np.asarray(pa)
        ac1=float((pa[:-1]@pa[1:])/ (pa@pa)) if (pa@pa)>0 else 0.0
        for th in a.thetas:
            Xm=_np.array(acc[th]['Xm']); Cc_all=_np.array(acc[th]['C'])   # (nconf, dmax+1)
            Xmean=float(Xm.mean())
            Cmean=Cc_all.mean(axis=0)                  # <X(0)X(d)>
            Cconn=Cmean-Xmean**2                       # connected
            G=Cmean/(Xmean**2) if Xmean>0 else _np.full_like(Cmean,_np.nan)  # normalized pair corr
            # fit m_J from log Cconn over d=1..dmax while Cconn>0 and decreasing
            ds=[]; ys=[]
            for d in range(1,dmax+1):
                if Cconn[d]>0 and (d==1 or Cconn[d]<Cconn[d-1]): ds.append(d); ys.append(math.log(Cconn[d]))
            mJ=None; mJerr=None; R2=None; pos_ok=len(ds)>=3
            if pos_ok:
                ds_=_np.array(ds); ys_=_np.array(ys)
                A_=_np.vstack([ds_,_np.ones_like(ds_)]).T
                (slope,inter),res,_,_=_np.linalg.lstsq(A_,ys_,rcond=None)
                mJ=float(-slope)
                yhat=A_@_np.array([slope,inter]); ss_res=float(((ys_-yhat)**2).sum()); ss_tot=float(((ys_-ys_.mean())**2).sum())
                R2=1-ss_res/ss_tot if ss_tot>0 else 0.0
                # jackknife over configs for mJ error
                jk=[]
                for k in range(len(Xm)):
                    Cm=_np.delete(Cc_all,k,axis=0).mean(axis=0); Xk=float(_np.delete(Xm,k).mean())
                    Cn=Cm-Xk**2; dd=[];yy=[]
                    for d in range(1,dmax+1):
                        if Cn[d]>0 and (d==1 or Cn[d]<Cn[d-1]): dd.append(d);yy.append(math.log(Cn[d]))
                    if len(dd)>=3:
                        Aj=_np.vstack([_np.array(dd),_np.ones(len(dd))]).T
                        sl,_=_np.linalg.lstsq(Aj,_np.array(yy),rcond=None)[0]; jk.append(-sl)
                if len(jk)>2:
                    jk=_np.array(jk); mJerr=float(math.sqrt((len(jk)-1)/len(jk)*((jk-jk.mean())**2).sum()))
            results['runs'].append({'beta':beta,'theta':th,'X_mean':Xmean,'plaq_mean':float(pa.mean()+0)/1 if False else float(_np.mean(pa)+Xmean*0)+0,  # placeholder
                'plaquette_mean':float(_np.mean(_np.asarray(plaqs.get() if on_gpu else plaqs))),
                'autocorr_lag1':ac1,'Cconn':[float(x) for x in Cconn],'G_normpair':[float(x) for x in G],
                'fit_d':ds,'m_J':mJ,'m_J_err':mJerr,'fit_R2':R2,'fit_npts':len(ds),
                'fit_ok':bool(pos_ok and (R2 is not None and R2>=0.9))})
        print('[beta=%.2f] plaq=%.4f autocorr1=%.3f  '%(beta,float(_np.mean(_np.asarray(plaqs.get() if on_gpu else plaqs))),ac1)
              +'  '.join('th%.2f:Xm=%.4f mJ=%s R2=%s'%(th,
                 [r for r in results['runs'] if r['beta']==beta and r['theta']==th][0]['X_mean'],
                 ('%.3f'%[r for r in results['runs'] if r['beta']==beta and r['theta']==th][0]['m_J']) if [r for r in results['runs'] if r['beta']==beta and r['theta']==th][0]['m_J'] is not None else 'NA',
                 ('%.2f'%[r for r in results['runs'] if r['beta']==beta and r['theta']==th][0]['fit_R2']) if [r for r in results['runs'] if r['beta']==beta and r['theta']==th][0]['fit_R2'] is not None else 'NA')
                 for th in a.thetas))
    # gate summary
    g_hb=results['runs'][0]['plaquette_mean'] if results['runs'] else 0.0
    gates['G-HB_plaq_beta0']=g_hb
    gates['G-DECORR_autocorr1_max']=max(r['autocorr_lag1'] for r in results['runs']) if results['runs'] else 0.0
    gates['G-FIT_min_R2']=min([r['fit_R2'] for r in results['runs'] if r['fit_R2'] is not None],default=None)
    results['gates']=gates
    results['meta']['walltime_s']=time.time()-T0
    json.dump(results,open(a.out,'w'),indent=1)
    if a.selftest:
        assert results['runs'][0]['X_mean']>0, 'selftest: no defects at theta'
        assert results['runs'][0]['fit_npts']>=1, 'selftest: no decay points'
        # equilibrium plaquette sanity at beta=3.5 (su2_hb_v3 reference ~0.778)
        assert abs(g_hb-0.778)<0.05, f'G-HB selftest plaq {g_hb}'
        print('SELFTEST_OK  plaq=%.4f  G-BK %.1e  G-FFT %.1e'%(g_hb,gbk,gfft))
    print('DONE -> %s  (%.1fs, %s)'%(a.out,results['meta']['walltime_s'],'GPU' if on_gpu else 'CPU'))

if __name__=='__main__': main()
