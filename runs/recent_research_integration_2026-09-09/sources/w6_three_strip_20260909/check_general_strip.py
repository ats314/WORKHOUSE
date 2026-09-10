import json
from pathlib import Path
import sympy as s

result=[]
for n in range(2,7):
    X=[s.Matrix(s.symbols(f'x{i}_0:3')) for i in range(n)]
    P=[s.Matrix(s.symbols(f'p{i}_0:3')) for i in range(n)]
    C=s.Matrix(n,n,lambda i,j:4 if i==j else -1 if abs(i-j)==1 else 0)
    H1=sum((X[i]+X[i+1]).dot(P[i].cross(P[i+1]))/2 for i in range(n-1))
    H1+=sum(X[j].dot(P[i].cross(P[j])) for i in range(n) for j in range(i+1,n))
    v=[-X[i].cross(sum(X[i+1:],s.zeros(3,1)))/2 for i in range(n)]
    comm=-sum(C[i,k]*s.diff(v[j][b],X[i][a])*P[k][a]*P[j][b] for i in range(n) for k in range(n) if C[i,k] for j in range(n) for a in range(3) for b in range(3))
    W=s.expand(H1+comm)
    G=sum((X[i].cross(P[i]) for i in range(n)),s.zeros(3,1))
    coeff=s.symbols(f'c0:{n}')
    rem=s.Poly(s.expand(W-sum(coeff[i]*P[i].dot(G) for i in range(n))),*[x for v in X+P for x in v])
    sol=s.solve(rem.coeffs(),coeff)
    print(n,sol,flush=True)
    result.append({'n':n,'gauss_solution':str(sol),'symbol_terms':len(s.Poly(W,*[x for v in X+P for x in v]).terms())})
Path(__file__).with_name('general_strip_checks.json').write_text(json.dumps(result,indent=2)+'\n')
