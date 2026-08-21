#!/usr/bin/env python3
# ENGINE_OP1_su2_hb_vec.py — VECTORIZED SU(2) Wilson exact heat-bath (quaternion), to reach
# L=8/16 for the Z.A min_A Delta_p measurement (the diagnostic's pure-Python
# heat-bath is too slow there).  Validated against ENGINE_FLUX_lci_typicality_diagnostic.py:
#   G-HB1: vectorized staple == diagnostic link_normals().sum() (machine precision)
#   G-HB2: L=4 equilibrium <½ReTr U_p> reproduces the diagnostic's value at beta=3.5
# Coloring: update links by (direction mu, site parity) — 8 sub-sweeps; for fixed
# (mu, parity) the staples never involve another link being updated (the (x±nu,mu)
# terms have opposite parity, the (·,nu) terms are different direction).
# Importable: provides thermalize_vec(L,beta,nsweeps,rng) -> U (L,L,L,L,4,4).
import math, sys
import numpy as np
PMBSF='/sessions/busy-admiring-dijkstra/mnt/THEORY/programs/pmbsf'
sys.path.insert(0, PMBSF)
import ENGINE_FLUX_lci_typicality_diagnostic as lci   # for qmul/qconj + validation

D=4
def qmul(a,b): return lci.qmul(a,b)
def qconj(a): return lci.qconj(a)

def staple_dir(U, mu):
    """H_mu(x) = sum over plaquettes through link (x,mu) of n_p, vectorized.
    Matches diagnostic.link_normals(...).sum(axis=0). U: (L,L,L,L,4,4)."""
    Umu = U[...,mu,:]
    H = np.zeros(Umu.shape)
    for nu in range(D):
        if nu==mu: continue
        Unu = U[...,nu,:]
        Unu_xpmu = np.roll(Unu, -1, axis=mu)         # U_nu(x+mu)
        Umu_xpnu = np.roll(Umu, -1, axis=nu)         # U_mu(x+nu)
        fwd = qmul(qmul(Unu_xpmu, qconj(Umu_xpnu)), qconj(Unu))   # +nu plaquette n_p
        Unu_xmnu = np.roll(Unu, +1, axis=nu)         # U_nu(x-nu)
        Umu_xmnu = np.roll(Umu, +1, axis=nu)         # U_mu(x-nu)
        Unu_xpmu_mnu = np.roll(Unu_xpmu, +1, axis=nu)# U_nu(x+mu-nu)
        bwd = qmul(qmul(qconj(Unu_xpmu_mnu), qconj(Umu_xmnu)), Unu_xmnu)  # -nu plaquette
        H += fwd + bwd
    return H

def _sample_vmf_batch(meandir, kappa, rng):
    """Batched vMF on S^3. meandir: (N,4) unit, kappa: (N,). Returns (N,4)."""
    N=meandir.shape[0]; p=4; pm=p-1
    out=np.zeros((N,4))
    small = kappa<1e-8
    if small.any():
        v=rng.standard_normal((small.sum(),4)); out[small]=v/np.linalg.norm(v,axis=1,keepdims=True)
    big = ~small
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
        # orthonormal complement of each meandir, sample S^2 in it
        g=rng.standard_normal((nb,4))
        g=g-(np.sum(g*M,axis=1,keepdims=True))*M       # project out meandir
        g/=np.linalg.norm(g,axis=1,keepdims=True)
        out[big]=w[:,None]*M+np.sqrt(np.clip(1-w*w,0,None))[:,None]*g
    return out

def thermalize_vec(L, beta, nsweeps, rng, log_every=10, U=None):
    if U is None:
        U=np.zeros((L,L,L,L,D,4)); U[...,0]=1.0
    # parity masks
    coords=np.indices((L,L,L,L)).sum(axis=0)%2     # (L,L,L,L) parity
    for s in range(nsweeps):
        for mu in range(D):
            H=staple_dir(U,mu)                      # (L,L,L,L,4)
            hn=np.linalg.norm(H,axis=-1)            # (L,L,L,L)
            for par in (0,1):
                mask=(coords==par)&(hn>1e-12)
                if not mask.any(): continue
                md=H[mask]/hn[mask][:,None]
                kp=beta*hn[mask]
                U[...,mu,:][mask]=_sample_vmf_batch(md,kp,rng)
        if log_every and ((s+1)%log_every==0 or s==nsweeps-1):
            mp=mean_plaq(U)
            print('[hbvec] L=%d sweep %d/%d  <½ReTr>=%.6f'%(L,s+1,nsweeps,mp))
    return U

def mean_plaq(U):
    """<½ Re Tr U_p> over all plaquettes (mu<nu)."""
    tot=0.0; cnt=0; L=U.shape[0]
    for mu in range(D):
        for nu in range(mu+1,D):
            Umu=U[...,mu,:]; Unu=U[...,nu,:]
            Unu_xpmu=np.roll(Unu,-1,axis=mu); Umu_xpnu=np.roll(Umu,-1,axis=nu)
            Up=qmul(qmul(Umu,Unu_xpmu),qmul(qconj(Umu_xpnu),qconj(Unu)))
            tot+=Up[...,0].sum(); cnt+=Up[...,0].size
    return tot/cnt

# ----------------- validation (run as __main__) -----------------
if __name__=='__main__':
    rng=np.random.default_rng(7)
    L=4
    U=np.zeros((L,L,L,L,D,4))
    Uq=rng.standard_normal((L,L,L,L,D,4)); Uq/=np.linalg.norm(Uq,axis=-1,keepdims=True)
    U[:]=Uq
    # G-HB1: vectorized staple vs diagnostic link_normals().sum()
    worst=0.0
    for _ in range(60):
        x=tuple(int(rng.integers(0,L)) for _ in range(4)); mu=int(rng.integers(0,4))
        Hvec=staple_dir(U,mu)[x]
        nrm,_=lci.link_normals(U,x,mu,L); Hdiag=nrm.sum(axis=0)
        worst=max(worst,float(np.max(np.abs(Hvec-Hdiag))))
    assert worst<1e-10, f'G-HB1 FAIL: vectorized staple != diagnostic by {worst}'
    print('G-HB1 (vectorized staple == diagnostic): PASS  worst %.2e'%worst)
    # G-HB2: equilibrium plaquette at beta=3.5 vs diagnostic's pure-Python heat-bath
    import time
    rng2=np.random.default_rng(11)
    t0=time.time(); Uv=thermalize_vec(4,3.5,60,rng2,log_every=60)
    mpv=mean_plaq(Uv); tv=time.time()-t0
    print('vectorized L=4 60 sweeps: %.2fs  <½ReTr>=%.5f'%(tv,mpv))
    rng3=np.random.default_rng(12)
    Ud=lci.thermalize(4,3.5,60,rng3,log_every=60)
    # diagnostic plaquette
    tot=0.0;cnt=0
    for xx in np.ndindex(4,4,4,4):
        for mu in range(4):
            for nu in range(mu+1,4):
                tot+=lci.plaquette_value_re_tr_half(Ud,xx,mu,nu,4);cnt+=1
    mpd=tot/cnt
    print('diagnostic L=4 60 sweeps: <½ReTr>=%.5f'%mpd)
    assert abs(mpv-mpd)<0.02, f'G-HB2 FAIL: plaquette {mpv} vs {mpd}'
    print('G-HB2 (equilibrium plaquette matches): PASS  |diff|=%.4f'%abs(mpv-mpd))
    print('ALL_VALIDATION_PASS')
