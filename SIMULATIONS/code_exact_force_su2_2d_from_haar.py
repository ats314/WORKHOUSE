import numpy as np

# SU(2) via unit quaternions
def normalize(q):
    return q / np.linalg.norm(q)

def qmul(q1, q2):
    a1,b1,c1,d1 = q1
    a2,b2,c2,d2 = q2
    return np.array([
        a1*a2 - b1*b2 - c1*c2 - d1*d2,
        a1*b2 + b1*a2 + c1*d2 - d1*c2,
        a1*c2 - b1*d2 + c1*a2 + d1*b2,
        a1*d2 + b1*c2 - c1*b2 + d1*a2
    ])

def qinv(q):
    return np.array([q[0],-q[1],-q[2],-q[3]])

def imag(q):
    return q[1:]

def cartan(theta):
    return np.array([np.cos(theta), 0.0, 0.0, np.sin(theta)])

def run(L=6, init='random', theta=1.2, eps0=0.6, lam=10.0, lr=0.03, iters=50, report_every=5):
    Nd = 2
    def mod(x): return x % L

    # initialize links
    links = {}
    for x in range(L):
        for y in range(L):
            for mu in range(Nd):
                if init == 'random':
                    q = np.random.normal(size=4)
                    links[(x,y,mu)] = normalize(q)
                elif init == 'checkerboard_cartan':
                    sign = 1 if (x+y+mu) % 2 == 0 else -1
                    links[(x,y,mu)] = cartan(sign*theta)
                else:
                    raise ValueError("init must be 'random' or 'checkerboard_cartan'")

    def plaquette(x,y):
        Ux  = links[(mod(x),   mod(y),   0)]
        Uy  = links[(mod(x+1), mod(y),   1)]
        Ux2 = qinv(links[(mod(x), mod(y+1), 0)])
        Uy2 = qinv(links[(mod(x), mod(y),   1)])
        return qmul(qmul(Ux, Uy), qmul(Ux2, Uy2))

    def disorder():
        s = 0.0
        for x in range(L):
            for y in range(L):
                s += (1.0 - plaquette(x,y)[0])
        return s / (L*L)

    def link_force(x,y,mu):
        F = np.zeros(3)
        if mu == 0:
            F += imag(plaquette(x,y))
            F -= imag(plaquette(x,y-1))
        if mu == 1:
            F += imag(plaquette(x-1,y))
            F -= imag(plaquette(x,y))
        return F

    def grad_norm():
        g = 0.0
        for x in range(L):
            for y in range(L):
                for mu in range(Nd):
                    F = link_force(x,y,mu)
                    g += np.dot(F,F)
        return g

    print(f"init={init} L={L}")
    print("Initial disorder:", disorder())
    print("Initial grad norm:", grad_norm())

    for it in range(iters):
        for x in range(L):
            for y in range(L):
                for mu in range(Nd):
                    q0 = links[(x,y,mu)]
                    F = link_force(x,y,mu)
                    dq = np.array([0.0, F[0], F[1], F[2]])
                    B = disorder()
                    if B < eps0:
                        dq *= (1.0 + lam*(eps0 - B))
                    links[(x,y,mu)] = normalize(q0 - lr*dq)

        if it % report_every == 0:
            print(f"Iter {it:2d} | disorder={disorder():.4f} | grad_norm={grad_norm():.6f}")

if __name__ == '__main__':
    run(L=6, init='random')
    run(L=6, init='checkerboard_cartan')
