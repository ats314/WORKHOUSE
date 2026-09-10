"""Exact certificates for the actual coupled rectangular Gaussian floor.

No matrix-root numerical test is used as a proof. Rational identities are
checked independently of the all-size argument in grid_gaussian_floor.md.
"""
from fractions import Fraction as F
import json
from pathlib import Path


def zero(n, m=None):
    return [[F(0) for _ in range(n if m is None else m)] for _ in range(n)]


def outer_add(a, v, factor=F(1)):
    nz = [(i, x) for i, x in enumerate(v) if x]
    for i, x in nz:
        for j, y in nz:
            a[i][j] += factor*x*y


def check_rectangle(width, height):
    n = width*height
    idx = lambda x, y: y*width+x
    # A positive horizontal edge is oriented to the right; a positive
    # vertical edge upwards. Faces are counterclockwise.
    edges = ([('h', x, y) for y in range(height+1) for x in range(width)]
             + [('v', x, y) for y in range(height) for x in range(width+1)])
    edge_index = {e: k for k, e in enumerate(edges)}
    d = zero(n, len(edges))
    for y in range(height):
        for x in range(width):
            f = idx(x,y)
            for e, sign in [(('h',x,y), 1), (('v',x+1,y), 1),
                            (('h',x,y+1), -1), (('v',x,y), -1)]:
                d[f][edge_index[e]] = F(sign)
    c_incidence = zero(n)
    for k in range(len(edges)):
        outer_add(c_incidence, [d[i][k] for i in range(n)])
    c = zero(n)
    pairs = []
    deg = [0]*n
    for y in range(height):
        for x in range(width):
            i = idx(x,y)
            c[i][i] = F(4)
            for xx, yy in [(x+1,y),(x,y+1)]:
                if xx < width and yy < height:
                    j = idx(xx,yy)
                    c[i][j] = c[j][i] = F(-1)
                    pairs.append((i,j))
                    deg[i] += 1
                    deg[j] += 1
    checks = []
    def record(name, condition):
        assert condition, (width,height,name)
        checks.append(name)
    record('original_edge_incidence_equals_4I_minus_adjacency', c_incidence == c)
    pe, lower_cert = zero(n), zero(n)
    block_number = [-1]*n
    for by in range(0,height,2):
        for bx in range(0,width,2):
            inds = [idx(bx,by),idx(bx+1,by),idx(bx,by+1),idx(bx+1,by+1)]
            e, v = [F(0)]*n, [F(0)]*n
            for i, sign in zip(inds,[1,-1,-1,1]):
                e[i], v[i] = F(1,2), F(sign)
                block_number[i] = (by//2)*(width//2)+bx//2
            outer_add(pe,e)
            outer_add(lower_cert,v,F(1,2))
    qe = [[F(i==j)-pe[i][j] for j in range(n)] for i in range(n)]
    pe_squared = [[sum(pe[i][k]*pe[k][j] for k in range(n))
                   for j in range(n)] for i in range(n)]
    record('normalized_block_indicator_projection',pe_squared==pe)
    # Since C^(1/4) commutes with sqrt(C), invariance of C^(1/4)E
    # under sqrt(C) is equivalent to invariance of E under C.
    cpe = [[sum(c[i][k]*pe[k][j] for k in range(n))
            for j in range(n)] for i in range(n)]
    pec = [[sum(pe[i][k]*c[k][j] for k in range(n))
            for j in range(n)] for i in range(n)]
    reducing = cpe == pec
    record('actual_source_reduces_only_on_single_2x2_block',
           reducing == (width == 2 and height == 2))
    upper_cert = zero(n)
    for i,j in pairs:
        plus = [F(0)]*n
        plus[i] = plus[j] = F(1)
        outer_add(upper_cert,plus)
        if block_number[i] != block_number[j]:
            jump = [F(0)]*n
            jump[i],jump[j] = F(1),F(-1)
            outer_add(lower_cert,jump)
    for i in range(n):
        lower_cert[i][i] += 4-deg[i]
        upper_cert[i][i] += 4-deg[i]
    record('C_minus_2Q_is_explicit_positive_sum',
           [[c[i][j]-2*qe[i][j] for j in range(n)] for i in range(n)]==lower_cert)
    record('8I_minus_C_is_explicit_positive_sum',
           [[8*F(i==j)-c[i][j] for j in range(n)] for i in range(n)]==upper_cert)
    result = {'faces':[width,height], 'face_count':n,
              'original_edge_count':len(edges), 'source_reducing':reducing,
              'exact_checks':checks}
    return result,c,pe


def numerical_diagnostic(c,pe):
    try:
        import numpy as np
    except ImportError:
        return {'status':'NumPy unavailable; exact certificates unaffected'}
    c = np.array(c,dtype=float)
    pe = np.array(pe,dtype=float)
    vals,u = np.linalg.eigh(c)
    h = (u*np.sqrt(vals))@u.T
    cquarter = (u*vals**.25)@u.T
    eva,evu = np.linalg.eigh(pe)
    ebasis = evu[:,eva>.5]
    r = cquarter@ebasis
    pr = r@np.linalg.solve(r.T@r,r.T)
    qr = np.eye(len(c))-pr
    comparison_min = float(np.linalg.eigvalsh(h-qr/np.sqrt(2)).min())
    covariance_projection_error = float(np.linalg.norm(pr@pr-pr))
    nonreduction_norm = float(np.linalg.norm(h@pr-pr@h,ord=2))
    assert comparison_min > -1e-10
    assert covariance_projection_error < 1e-10
    return {'status':'diagnostic passed; not an exact proof',
            'minimum_full_gaussian_frequency':float(np.sqrt(vals.min())),
            'minimum_eigenvalue_of_proved_comparison':comparison_min,
            'covariance_projection_error':covariance_projection_error,
            'nonreducing_commutator_norm':nonreduction_norm}


def main():
    records=[]
    for wh in [(2,2),(2,4),(4,2),(4,4),(2,6),(6,2),(4,6),(6,4),(6,6),(8,8)]:
        rec,c,pe=check_rectangle(*wh)
        rec['numerical_diagnostic']=numerical_diagnostic(c,pe)
        records.append(rec)
    out={'theorem':'F0 >= 1/sqrt(2), all open even-sided face rectangles',
         'scope':'actual coupled Gaussian operator; all bosonic degrees and physical restriction',
         'exact_control_count':sum(len(r['exact_checks']) for r in records),
         'rectangles':records}
    path=Path(__file__).with_name('grid_gaussian_floor_checks.json')
    path.write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({'exact_control_count':out['exact_control_count'],
                      'record':str(path)},indent=2))


if __name__=='__main__':
    main()
