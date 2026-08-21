import numpy as np

def build_2d_torus_complex(Lx:int, Ly:int):
    # vertices indexed by (x,y)
    V = [(x,y) for x in range(Lx) for y in range(Ly)]
    vid = {v:i for i,v in enumerate(V)}
    # edges: oriented +x and +y from each vertex
    edges=[]
    for x,y in V:
        edges.append(((x,y),'x'))  # x-edge from (x,y) -> (x+1,y)
        edges.append(((x,y),'y'))  # y-edge from (x,y) -> (x,y+1)
    eid={e:i for i,e in enumerate(edges)}
    def head(v,dir):
        x,y=v
        if dir=='x':
            return ((x+1)%Lx, y)
        if dir=='y':
            return (x,(y+1)%Ly)
        raise ValueError(dir)

    plaquettes=[(x,y) for x in range(Lx) for y in range(Ly)]
    pid={p:i for i,p in enumerate(plaquettes)}

    # d0: edges x vertices
    nE=len(edges); nV=len(V)
    d0=np.zeros((nE,nV),dtype=int)
    for (base,dir_),i in eid.items():
        tail=base
        headv=head(base,dir_)
        d0[i,vid[tail]]=-1
        d0[i,vid[headv]]=+1

    # d1: plaquettes x edges (oriented boundary)
    nP=len(plaquettes)
    d1=np.zeros((nP,nE),dtype=int)
    for p in plaquettes:
        x,y=p
        row=pid[p]
        # boundary: +x at (x,y), +y at (x+1,y), -x at (x,y+1), -y at (x,y)
        boundary = [
            (((x,y),'x'), +1),
            ((((x+1)%Lx,y),'y'), +1),
            (((x,(y+1)%Ly),'x'), -1),
            (((x,y),'y'), -1),
        ]
        for e,sgn in boundary:
            d1[row,eid[e]] += sgn

    return V,edges,plaquettes,d0,d1

def wilson_u1_action(theta:np.ndarray, beta:float, d1:np.ndarray):
    plaquette_angles = d1 @ theta
    return beta * np.sum(1 - np.cos(plaquette_angles))

def finite_difference_hessian(f, x0:np.ndarray, eps:float=1e-4):
    n=len(x0)
    H=np.zeros((n,n))
    f0=f(x0)
    for i in range(n):
        ei=np.zeros(n); ei[i]=1
        f_plus=f(x0+eps*ei)
        f_minus=f(x0-eps*ei)
        H[i,i]=(f_plus - 2*f0 + f_minus)/(eps**2)
        for j in range(i+1,n):
            ej=np.zeros(n); ej[j]=1
            f_pp=f(x0+eps*ei+eps*ej)
            f_pm=f(x0+eps*ei-eps*ej)
            f_mp=f(x0-eps*ei+eps*ej)
            f_mm=f(x0-eps*ei-eps*ej)
            val=(f_pp - f_pm - f_mp + f_mm)/(4*eps**2)
            H[i,j]=val
            H[j,i]=val
    return H

def check(L:int, beta:float=2.7, eps:float=1e-4):
    V,edges,plaquettes,d0,d1 = build_2d_torus_complex(L,L)
    nE=d1.shape[1]
    theta0=np.zeros(nE)
    f=lambda th: wilson_u1_action(th,beta,d1)

    H_fd = finite_difference_hessian(f, theta0, eps=eps)
    H_an = beta*(d1.T@d1)

    rel_err = np.linalg.norm(H_fd-H_an)/np.linalg.norm(H_an)

    evals = np.linalg.eigvalsh(H_an)
    tol=1e-9
    nullity = int(np.sum(evals<tol))
    min_pos = float(np.min(evals[evals>tol]))

    return rel_err, nullity, min_pos, nE, len(V), len(plaquettes)

if __name__ == "__main__":
    for L in [3,4,5]:
        rel_err, nullity, min_pos, nE, nV, nP = check(L, beta=2.7, eps=1e-4)
        print(f"L={L}x{L}: rel_err={rel_err:.3e}, nullity={nullity}, min_pos_eig={min_pos:.6f}, nE={nE}, nV={nV}, nP={nP}")
