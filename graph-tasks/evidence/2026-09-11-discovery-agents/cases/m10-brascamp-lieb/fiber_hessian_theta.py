"""Scratch numeric check for case m10-brascamp-lieb (not repository evidence).
Constrained potential V on the fibre U2 U3 = Q, Q = exp(i theta n.sigma), n = e_3, at the S4
minimizer U0=U1=exp(i theta n.sigma/4), U2=U3=exp(i theta n.sigma/2). Fibre coordinates: left
deviations U_i -> exp(i x_i.sigma/2) U_i^*, i=0,1,2 (9 real dims), U3 = U2^{-1} Q.
V = 4[4 - tr U0/2 - tr U1/2 - tr(U2 U0^-1)/2 - tr(U3 U1^-1)/2]   (transport note S1).
Eigenvalues of the 9x9 Hessian of V at the minimizer on a theta grid (mpmath, finite differences).
"""
import json, mpmath as mp
mp.mp.dps=30
def mat(a,b,c,d): return mp.matrix([[a,b],[c,d]])
I2=mat(1,0,0,1)
sig=[mat(0,1,1,0),mat(0,-1j,1j,0),mat(1,0,0,-1)]
def su2(v):   # exp(i v.sigma/2)
    a=mp.sqrt(v[0]**2+v[1]**2+v[2]**2)
    if a==0: return I2
    ns=(v[0]*sig[0]+v[1]*sig[1]+v[2]*sig[2])/a
    return mp.cos(a/2)*I2+1j*mp.sin(a/2)*ns
def dag(M): return M.transpose_conj()
def htr(M): return mp.re(M[0,0]+M[1,1])/2
def V(U0,U1,U2,U3): return 4*(4-htr(U0)-htr(U1)-htr(U2*dag(U0))-htr(U3*dag(U1)))
def Vfib(x,theta):
    n=[mp.mpf(0),mp.mpf(0),mp.mpf(1)]
    Q=su2([2*theta*k for k in n]); U0s=su2([theta*k/2 for k in n]); U2s=su2([theta*k for k in n])
    U0=su2(x[0:3])*U0s; U1=su2(x[3:6])*U0s; U2=su2(x[6:9])*U2s; U3=dag(U2)*Q
    return V(U0,U1,U2,U3)
def hess(theta,h=mp.mpf('1e-5')):
    H=mp.matrix(9,9); z=[mp.mpf(0)]*9
    for i in range(9):
        for j in range(i,9):
            def f(si,sj):
                x=list(z); x[i]+=si*h; x[j]+=sj*h; return Vfib(x,theta)
            H[i,j]=(f(1,1)-f(1,-1)-f(-1,1)+f(-1,-1))/(4*h*h); H[j,i]=H[i,j]
    return H
out=[]
for th in ['0.05','0.5','1.0','1.5','2.0','2.5','2.8','3.0','3.1','3.13']+[str(mp.pi)]:
    theta=mp.mpf(th); z=[mp.mpf(0)]*9
    g=[]
    for i in range(9):
        x=list(z); x[i]+=mp.mpf('1e-8'); y=list(z); y[i]-=mp.mpf('1e-8'); g.append((Vfib(x,theta)-Vfib(y,theta))/mp.mpf('2e-8'))
    gn=mp.sqrt(sum(k*k for k in g))
    E,_=mp.eigsy(hess(theta)); ev=sorted([float(E[k]) for k in range(9)])
    rec={"theta":float(theta),"V_at_S4":float(Vfib(z,theta)),"v_star":float(16*(1-mp.cos(theta/4))),"grad_norm":float(gn),"eig":[round(e,6) for e in ev]}
    out.append(rec); print("theta=%.4f V=%.6f v*=%.6f |grad|=%.1e  eigs=%s"%(rec["theta"],rec["V_at_S4"],rec["v_star"],rec["grad_norm"],[round(e,4) for e in ev]))
for th in ['3.0','3.1','3.13','3.1405']:
    theta=mp.mpf(th); E,_=mp.eigsy(hess(theta)); ev=sorted([float(E[k]) for k in range(9)]); d=float(mp.pi-theta)
    print("pi-theta=%.4f  lambda_1=%.6f lambda_2=%.6f lambda_3=%.6f  lambda_1/(pi-theta)=%.4f lambda_1/(pi-theta)^2=%.4f"%(d,ev[0],ev[1],ev[2],ev[0]/d,ev[0]/d**2))
json.dump(out,open(__file__.replace('.py','.json'),'w'),indent=1)
