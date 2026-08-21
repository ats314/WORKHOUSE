#!/usr/bin/env python3
# ENGINE_OP1_su2_hb_v2.py — vectorized SU(2) Wilson exact heat-bath, staple matched EXACTLY
# to diagnostic.plaquette_normal:
#   +nu n_p = qconj( U_nu(x+mu) * qconj(U_mu(x+nu)) * qconj(U_nu(x)) )
#   -nu n_p =        qconj(U_nu(x-nu)) * U_mu(x-nu) * U_nu(x-nu+mu)
# Gates: G-HB1 (staple == diagnostic), G-HB2 (L=4 equilibrium plaquette matches).
import math, sys, time
import numpy as np
PMBSF='/sessions/busy-admiring-dijkstra/mnt/THEORY/programs/pmbsf'
sys.path.insert(0, PMBSF)
import ENGINE_FLUX_lci_typicality_diagnostic as lci
D=4
qmul=lci.qmul; qconj=lci.qconj
def qmul3(a,b,c): return qmul(qmul(a,b),c)

def staple_dir(U, mu):
    Umu=U[...,mu,:]; H=np.zeros(Umu.shape)
    for nu in range(D):
        if nu==mu: continue
        Unu=U[...,nu,:]
        Unu_xpmu=np.roll(Unu,-1,axis=mu)          # U_nu(x+mu)
        Umu_xpnu=np.roll(Umu,-1,axis=nu)          # U_mu(x+nu)
        fwd=qconj(qmul3(Unu_xpmu, qconj(Umu_xpnu), qconj(Unu)))
        Unu_xmnu=np.roll(Unu,+1,axis=nu)          # U_nu(x-nu)
        Umu_xmnu=np.roll(Umu,+1,axis=nu)          # U_mu(x-nu)
        Unu_xmnu_pmu=np.roll(Unu_xmnu,-1,axis=mu) # U_nu(x-nu+mu)
        bwd=qmul3(qconj(Unu_xmnu), Umu_xmnu, Unu_xmnu_pmu)
        H+=fwd+bwd
    return H

def _vmf(meandir,kappa,rng):
    N=meandir.shape[0]; pm=3; out=np.zeros((N,4))
    small=kappa<1e-8
    if small.any():
        v=rng.standard_normal((int(small.sum()),4)); out[small]=v/np.linalg.norm(v,axis=1,keepdims=True)
    big=~small
    if big.any():
        kp=kappa[big]; M=meandir[big]; nb=kp.shape[0]
        b=(-2*kp+np.sqrt(4*kp*kp+pm*pm))/pm
        x0=(1-b)/(1+b); c=kp*x0+pm*np.log(1-x0*x0)
        w=np.empty(nb); done=np.zeros(nb,bool)
        while not done.all():
            idx=np.where(~done)[0]
            z=rng.beta(pm/2.0,pm/2.0,idx.shape[0])
            wc=(1-(1+b[idx])*z)/(1-(1-b[idx])*z)
            logu=np.log(rng.random(idx.shape[0]))
            acc=kp[idx]*wc+pm*np.log(np.clip(1-x0[idx]*wc,1e-300,None))-c[idx]>=logu
            ai=idx[acc]; w[ai]=wc[acc]; done[ai]=True
        g=rng.standard_normal((nb,4)); g=g-(np.sum(g*M,axis=1,keepdims=True))*M
        g/=np.linalg.norm(g,axis=1,keepdims=True)
        out[big]=w[:,None]*M+np.sqrt(np.clip(1-w*w,0,None))[:,None]*g
    return out

def thermalize_vec(L,beta,nsweeps,rng,log_every=10,U=None):
    if U is None: U=np.zeros((L,L,L,L,D,4)); U[...,0]=1.0
    par=np.indices((L,L,L,L)).sum(axis=0)%2
    for s in range(nsweeps):
        for mu in range(D):
            H=staple_dir(U,mu); hn=np.linalg.norm(H,axis=-1)
            for p in (0,1):
                mask=(par==p)&(hn>1e-12)
                if not mask.any(): continue
                md=H[mask]/hn[mask][:,None]; kp=beta*hn[mask]
                U[...,mu,:][mask]=_vmf(md,kp,rng)
        if log_every and ((s+1)%log_every==0 or s==nsweeps-1):
            print('[hbvec] L=%d sweep %d/%d  <½ReTr>=%.6f'%(L,s+1,nsweeps,mean_plaq(U)))
    return U

def mean_plaq(U):
    tot=0.0;cnt=0
    for mu in range(D):
        for nu in range(mu+1,D):
            Umu=U[...,mu,:]; Unu=U[...,nu,:]
            Unu_xpmu=np.roll(Unu,-1,axis=mu); Umu_xpnu=np.roll(Umu,-1,axis=nu)
            Up=qmul3(Umu,Unu_xpmu,qmul(qconj(Umu_xpnu),qconj(Unu)))
            tot+=Up[...,0].sum(); cnt+=Up[...,0].size
    return tot/cnt

if __name__=='__main__':
    rng=np.random.default_rng(7); L=4
    Uq=rng.standard_normal((L,L,L,L,D,4)); Uq/=np.linalg.norm(Uq,axis=-1,keepdims=True); U=Uq.copy()
    worst=0.0
    for _ in range(60):
        x=tuple(int(rng.integers(0,L)) for _ in range(4)); mu=int(rng.integers(0,4))
        Hvec=staple_dir(U,mu)[x]; nrm,_=lci.link_normals(U,x,mu,L); Hd=nrm.sum(axis=0)
        worst=max(worst,float(np.max(np.abs(Hvec-Hd))))
    assert worst<1e-10, f'G-HB1 FAIL {worst}'
    print('G-HB1 (vectorized staple == diagnostic): PASS worst %.2e'%worst)
    t0=time.time(); Uv=thermalize_vec(4,3.5,60,np.random.default_rng(11),log_every=60); tv=time.time()-t0
    mpv=mean_plaq(Uv); print('vec L=4 60sw: %.2fs <½ReTr>=%.5f'%(tv,mpv))
    Ud=lci.thermalize(4,3.5,60,np.random.default_rng(12),log_every=60)
    tot=0.0;cnt=0
    for xx in np.ndindex(4,4,4,4):
        for mu in range(4):
            for nu in range(mu+1,4):
                tot+=lci.plaquette_value_re_tr_half(Ud,xx,mu,nu,4);cnt+=1
    mpd=tot/cnt; print('diag L=4 60sw: <½ReTr>=%.5f'%mpd)
    assert abs(mpv-mpd)<0.02, f'G-HB2 FAIL {mpv} vs {mpd}'
    print('G-HB2 (equilibrium plaquette matches): PASS |diff|=%.4f'%abs(mpv-mpd))
    print('ALL_VALIDATION_PASS')
