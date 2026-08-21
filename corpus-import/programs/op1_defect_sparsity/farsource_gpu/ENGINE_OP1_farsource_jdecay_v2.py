#!/usr/bin/env python3
# ENGINE_OP1_farsource_jdecay_v2.py — GPU(CuPy)/CPU(NumPy) engine for the far-source interaction
# decay J(p,r) = log( <X_p X_r>/(<X_p><X_r>) ), the open Z.B content (handoff from F043).
# v2 vs v1: robust EFFECTIVE-MASS estimator m_eff(d)=log(C_c(d)/C_c(d+1)) (standard lattice
# mass-gap read; works even when the decay is fast, as it is deep in the ordered phase),
# plus jackknife errors and a plateau estimate. Reports the full C_c(d), G(d)=norm pair-corr,
# and m_eff(d) so the mass can be read off directly.
#
# PHYSICS / Z.B: the reduction's (TOS+J) needs J(p,r) <= C_J e^{-m_J d(p,r)}. J(p,r) is the
# log normalized pair-correlation of the defect/source-indicator field. So m_J = the MASS of
# the defect field. Z.B (far-source firewall) holds iff m_J stays bounded away from 0 UNIFORMLY
# along the AF trajectory. Along that trajectory beta INCREASES as a->0, the field gets more
# ordered, and m_J GROWS — so the binding case is the COARSE (small-beta) end. Scan beta
# downward toward the crossover; the question is whether m_J(beta) collapses there or stays > 0.
#   -> Recommended A100 production: --betas 2.2 2.4 2.6 2.8 3.0 3.5 4.0  --L 24 (or 32)
#      --nconfigs 200 --nthermal 400 --nsep 20.  (Small beta has the longest xi -> most
#       decay points; large beta is massive-but-fast, read via m_eff(1).)
#
# Self-test:  python3 ENGINE_OP1_farsource_jdecay_v2.py --selftest
# Gates: G-BK backend assoc; G-HB equilibrium plaquette (beta=3.5 ref 0.778); G-FFT FFT 2pt
#   == direct; G-DECORR config autocorr; G-MEFF at least one reliable effective mass.
import argparse, json, math, time
import numpy as _np

def get_xp(device):
    if device=='gpu':
        try:
            import cupy as cp; return cp, True
        except Exception as e:
            print(f'[warn] cupy unavailable ({e}); using numpy'); import numpy as np; return np, False
    import numpy as np; return np, False

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--L',type=int,default=16)
    ap.add_argument('--betas',type=float,nargs='+',default=[2.4,2.8,3.2,3.6,4.0])
    ap.add_argument('--thetas',type=float,nargs='+',default=[0.9,1.2,1.5])
    ap.add_argument('--nconfigs',type=int,default=120)
    ap.add_argument('--nthermal',type=int,default=400)
    ap.add_argument('--nsep',type=int,default=20)
    ap.add_argument('--seed',type=int,default=20260613)
    ap.add_argument('--device',choices=['cpu','gpu'],default='cpu')
    ap.add_argument('--out',type=str,default='CERT_OP1_farsource_jdecay_v2.json')
    ap.add_argument('--selftest',action='store_true')
    a=ap.parse_args()
    if a.selftest:
        a.L=10; a.betas=[2.4,3.5]; a.thetas=[0.9]; a.nconfigs=40; a.nthermal=120; a.nsep=5; a.device='cpu'
    xp,on_gpu=get_xp(a.device); D=4; L=a.L; V=L**4
    rng=xp.random.default_rng(a.seed); T0=time.time(); gates={}
    def to_np(x): return x.get() if on_gpu else _np.asarray(x)

    def qmul(A,B):
        a0,a1,a2,a3=A[...,0],A[...,1],A[...,2],A[...,3]; b0,b1,b2,b3=B[...,0],B[...,1],B[...,2],B[...,3]
        return xp.stack([a0*b0-a1*b1-a2*b2-a3*b3,a0*b1+a1*b0+a2*b3-a3*b2,
                         a0*b2-a1*b3+a2*b0+a3*b1,a0*b3+a1*b2-a2*b1+a3*b0],axis=-1)
    def qconj(A):
        o=A.copy(); o[...,1:]*=-1.0; return o
    def qmul3(A,B,C): return qmul(qmul(A,B),C)

    # G-BK
    A=rng.standard_normal((6,4)); B=rng.standard_normal((6,4)); C=rng.standard_normal((6,4))
    gbk=float(xp.max(xp.abs(qmul(qmul(A,B),C)-qmul(A,qmul(B,C))))); gates['G-BK']=gbk
    assert gbk<1e-10, f'G-BK {gbk}'

    def staple_dir(U,mu):
        Umu=U[...,mu,:]; H=xp.zeros(Umu.shape)
        for nu in range(D):
            if nu==mu: continue
            Unu=U[...,nu,:]
            Unu_xpmu=xp.roll(Unu,-1,axis=mu); Umu_xpnu=xp.roll(Umu,-1,axis=nu)
            fwd=qconj(qmul3(Unu_xpmu,qconj(Umu_xpnu),qconj(Unu)))
            Unu_xmnu=xp.roll(Unu,+1,axis=nu); Umu_xmnu=xp.roll(Umu,+1,axis=nu)
            bwd=qmul3(qconj(Unu_xmnu),Umu_xmnu,xp.roll(Unu_xmnu,-1,axis=mu))
            H=H+fwd+bwd
        return H
    def rbeta(sp,size):
        g1=rng.standard_gamma(sp,size); g2=rng.standard_gamma(sp,size); return g1/(g1+g2)
    def vmf(meandir,kappa):
        n=meandir.shape[0]; pm=3; out=xp.zeros((n,4)); small=kappa<1e-8
        if bool(xp.any(small)):
            v=rng.standard_normal((int(xp.sum(small)),4)); out[small]=v/xp.linalg.norm(v,axis=1,keepdims=True)
        big=~small
        if bool(xp.any(big)):
            kp=kappa[big]; M=meandir[big]; nb=kp.shape[0]
            b=(-2*kp+xp.sqrt(4*kp*kp+pm*pm))/pm; x0=(1-b)/(1+b); c=kp*x0+pm*xp.log(1-x0*x0)
            w=xp.empty(nb); done=xp.zeros(nb,bool); it=0
            while not bool(xp.all(done)) and it<20000:
                it+=1; idx=xp.where(~done)[0]; z=rbeta(pm/2.0,idx.shape[0])
                wc=(1-(1+b[idx])*z)/(1-(1-b[idx])*z); logu=xp.log(rng.random(idx.shape[0]))
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
                H=staple_dir(U,mu); hn=xp.linalg.norm(H,axis=-1); mask=(par==p)&(hn>1e-12)
                if not bool(xp.any(mask)): continue
                md=H[mask]/hn[mask][:,None]; U[...,mu,:][mask]=vmf(md,beta*hn[mask])
        return U
    def plaq_w(U,mu,nu):
        Umu=U[...,mu,:]; Unu=U[...,nu,:]
        return qmul3(Umu,xp.roll(Unu,-1,axis=mu),qmul(qconj(xp.roll(Umu,-1,axis=nu)),qconj(Unu)))[...,0]
    def mean_plaq(U):
        t=0.0;c=0
        for mu in range(D):
            for nu in range(mu+1,D):
                w=plaq_w(U,mu,nu); t+=float(xp.sum(w)); c+=w.size
        return t/c

    # G-FFT
    Xr=(rng.random((L,)*4)<0.3).astype(float)
    Cfft=xp.fft.ifftn(xp.abs(xp.fft.fftn(Xr))**2).real/V
    gfft=abs(float(Cfft[0,0,1,0])-float(xp.mean(Xr*xp.roll(Xr,-1,axis=2)))); gates['G-FFT']=gfft
    assert gfft<1e-9, f'G-FFT {gfft}'

    dmax=L//2; res={'meta':{'L':L,'V':V,'betas':a.betas,'thetas':a.thetas,'nconfigs':a.nconfigs,
        'nthermal':a.nthermal,'nsep':a.nsep,'on_gpu':on_gpu,'seed':a.seed,
        'observable':'J(d)=log<X0Xd>/<X>^2 ; m_eff(d)=log(Cconn(d)/Cconn(d+1)); m_J=defect-field mass'},
        'gates':gates,'runs':[]}
    any_meff=False
    for beta in a.betas:
        U=xp.zeros((L,)*4+(D,4)); U[...,0]=1.0
        for _ in range(a.nthermal): U=sweep(U,beta)
        plaqs=[]; acc={th:[] for th in a.thetas}; Xms={th:[] for th in a.thetas}
        for ci in range(a.nconfigs):
            for _ in range(a.nsep): U=sweep(U,beta)
            plaqs.append(mean_plaq(U))
            w01=plaq_w(U,0,1); ang=xp.arccos(xp.clip(w01,-1.0,1.0))
            for th in a.thetas:
                X=(ang>th).astype(float); Xms[th].append(float(xp.mean(X)))
                C=xp.fft.ifftn(xp.abs(xp.fft.fftn(X))**2).real/V
                Cax=[0.5*(float(C[0,0,d,0])+float(C[0,0,0,d])) for d in range(dmax+1)]
                acc[th].append(Cax)
        pa=to_np(xp.array(plaqs)); pac=pa-pa.mean(); ac1=float((pac[:-1]@pac[1:])/(pac@pac)) if (pac@pac)>0 else 0.0
        for th in a.thetas:
            Xm=_np.array(Xms[th]); Call=_np.array(acc[th]); Xmean=float(Xm.mean())
            Cmean=Call.mean(axis=0); Cconn=Cmean-Xmean**2; G=Cmean/(Xmean**2) if Xmean>0 else Cmean*_np.nan
            def meff_from(Cc):
                out=[]
                for d in range(0,dmax):
                    out.append(math.log(Cc[d]/Cc[d+1]) if (Cc[d]>0 and Cc[d+1]>0) else None)
                return out
            meff=meff_from(Cconn)
            # jackknife errors on m_eff(d)
            jkmeff={}
            for d in range(dmax):
                vals=[]
                for k in range(len(Xm)):
                    Cm=_np.delete(Call,k,axis=0).mean(axis=0)-_np.delete(Xm,k).mean()**2
                    if Cm[d]>0 and d+1<=dmax and Cm[d+1]>0: vals.append(math.log(Cm[d]/Cm[d+1]))
                if len(vals)>2:
                    vals=_np.array(vals); jkmeff[d]=float(math.sqrt((len(vals)-1)/len(vals)*((vals-vals.mean())**2).sum()))
            reliable=[d for d in range(dmax) if meff[d] is not None and Cconn[d]>1e-6]
            mJ=meff[reliable[0]] if reliable else None
            mJ_err=jkmeff.get(reliable[0]) if reliable else None
            if reliable: any_meff=True
            res['runs'].append({'beta':beta,'theta':th,'plaquette_mean':float(pa.mean()),'autocorr_lag1':ac1,
                'X_mean':Xmean,'Cconn':[float(x) for x in Cconn],'G_normpair':[float(x) for x in G],
                'm_eff':meff,'m_eff_err':{int(k):v for k,v in jkmeff.items()},
                'm_J':mJ,'m_J_err':mJ_err,'corr_len_xi':(1.0/mJ if (mJ and mJ>0) else None),
                'n_reliable_d':len(reliable)})
        print('[b=%.2f plaq=%.4f ac1=%.2f] '%(beta,pa.mean(),ac1)+' '.join(
            'th%.1f:Xm=%.3f mJ=%s'%(th,[r for r in res['runs'] if r['beta']==beta and r['theta']==th][0]['X_mean'],
            ('%.2f'%[r for r in res['runs'] if r['beta']==beta and r['theta']==th][0]['m_J']) if [r for r in res['runs'] if r['beta']==beta and r['theta']==th][0]['m_J'] is not None else 'NA')
            for th in a.thetas))
    gates['G-DECORR_ac1_max']=max(r['autocorr_lag1'] for r in res['runs'])
    gates['G-HB_plaq_first']=res['runs'][0]['plaquette_mean']
    res['gates']=gates; res['meta']['walltime_s']=time.time()-T0
    json.dump(res,open(a.out,'w'),indent=1)
    if a.selftest:
        assert any_meff, 'selftest: no reliable effective mass at any (beta,theta)'
        b35=[r for r in res['runs'] if abs(r['beta']-3.5)<1e-6]
        if b35: assert abs(b35[0]['plaquette_mean']-0.778)<0.05, f"G-HB {b35[0]['plaquette_mean']}"
        print('SELFTEST_OK G-BK %.1e G-FFT %.1e any_meff=%s'%(gbk,gfft,any_meff))
    print('DONE -> %s (%.1fs, %s)'%(a.out,res['meta']['walltime_s'],'GPU' if on_gpu else 'CPU'))

if __name__=='__main__': main()
