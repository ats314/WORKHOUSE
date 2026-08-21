#!/usr/bin/env python3
# ENGINE_PMBSF_su2hb_f041.py — byte-faithful re-deposit of ENGINE_PMBSF_su2_hb_v3.py at a FRESH path, because
# the sandbox mount served a truncated view of ENGINE_PMBSF_su2_hb_v3.py (cut at line 95), giving
# a SyntaxError on import (documented mount-staleness; host file is intact). Same
# code, validated by the same gates G-HB1/G-HB2. Importable: thermalize_vec, mean_plaq.
import math, os, sys, time
import numpy as np
_HERE=os.path.dirname(os.path.abspath(__file__))
PMBSF=os.path.normpath(os.path.join(_HERE,'..','..','..','programs','pmbsf'))
if not os.path.isdir(PMBSF):
    PMBSF=os.path.normpath(os.path.join(_HERE,'..','..','pmbsf'))
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
        Unu_xpmu=np.roll(Unu,-1,axis=mu); Umu_xpnu=np.roll(Umu,-1,axis=nu)
        fwd=qconj(qmul3(Unu_xpmu, qconj(Umu_xpnu), qconj(Unu)))
        Unu_xmnu=np.roll(Unu,+1,axis=nu); Umu_xmnu=np.roll(Umu,+1,axis=nu)
        Unu_xmnu_pmu=np.roll(Unu_xmnu,-1,axis=mu)
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
            for p in (0,1):
                H=staple_dir(U,mu); hn=np.linalg.norm(H,axis=-1)   # RECOMPUTE per parity
                mask=(par==p)&(hn>1e-12)
                if not mask.any(): continue
                md=H[mask]/hn[mask][:,None]; kp=beta*hn[mask]
                U[...,mu,:][mask]=_vmf(md,kp,rng)
        if log_every and ((s+1)%log_every==0 or s==nsweeps-1):
            print('[hbvec] L=%d sweep %d/%d  <half ReTr>=%.6f'%(L,s+1,nsweeps,mean_plaq(U)))
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
