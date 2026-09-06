"""Exact finite controls for the vacuum-preserving inverse-energy full form."""
from __future__ import annotations

import argparse
import hashlib
import json
import sys
from pathlib import Path

import sympy as sp


def require(condition, label):
    if not condition:
        raise AssertionError(label)


def psd_pivots(value):
    matrix = sp.Matrix(value)
    require(matrix == matrix.T, 'symmetric exact matrix')
    require(all(entry.is_Rational for entry in matrix), 'rational matrix')
    pivots = []
    for i in range(matrix.rows):
        pivot = matrix[i,i]
        require(pivot >= 0, 'nonnegative PSD pivot')
        pivots.append(str(pivot))
        if pivot == 0:
            require(all(matrix[i,j] == 0 for j in range(i+1,matrix.cols)), 'zero PSD pivot has no off-diagonal remainder')
            continue
        for row in range(i+1,matrix.rows):
            for col in range(row,matrix.cols):
                item = matrix[row,col]-matrix[row,i]*matrix[i,col]/pivot
                matrix[row,col] = matrix[col,row] = item
    return pivots


def controls():
    if sys.flags.optimize:
        raise RuntimeError('Exact controls require assertions enabled')
    r = sp.Rational
    h = sp.diag(0,4,7,11)
    vacuum = sp.eye(4)[:,0]
    v = sp.Matrix([0,r(3,5),r(4,5),0])
    p = vacuum*vacuum.T+v*v.T
    q = sp.eye(4)-p
    low = sp.diag(0,1,0,0)
    inverse = sp.diag(0,r(1,4),r(1,7),r(1,11))
    require(p*p == p and p.T == p and q*vacuum == sp.zeros(4,1), 'exact retained vacuum projection')
    require(h*inverse == inverse*h == sp.eye(4)-vacuum*vacuum.T, 'actual bounded pseudoinverse')
    leakage = r(16,25)
    require(low*q*low == leakage*low, 'complete low-space leakage')
    alpha, threshold = sp.Integer(4), sp.Integer(7)
    inverse_cap = 1/threshold+(1/alpha-1/threshold)*leakage
    full_floor = 1/inverse_cap
    compressed_floor = threshold-(threshold-alpha)*leakage
    require(full_floor == r(175,37) and compressed_floor == r(127,25), 'distinct exact constants')
    inverse_pivots = psd_pivots(inverse_cap*q-q*inverse*q)
    full_pivots = psd_pivots(h-full_floor*q)
    compression_pivots = psd_pivots(q*h*q-compressed_floor*q)
    nullvector = sp.Matrix([0,7,-3,0])
    require((h-full_floor*q)*nullvector == sp.zeros(4,1), 'sharp full form equality vector')
    bad_determinant = (h-compressed_floor*q).extract([1,2],[1,2]).det()
    require(bad_determinant == -r(1296,625), 'compressed floor cannot be promoted to full floor')
    bad_vacuum = r(3,5)*vacuum+r(4,5)*sp.eye(4)[:,3]
    bad_p = bad_vacuum*bad_vacuum.T+v*v.T
    bad_q = sp.eye(4)-bad_p
    vacuum_counter = (vacuum.T*(h-full_floor*bad_q)*vacuum)[0]
    require(vacuum_counter == -full_floor*r(16,25) < 0, 'exact vacuum retention is essential')
    aa, jump, x = sp.symbols('a jump x', positive=True)
    harmonic = aa*(aa+jump)/(aa+jump*x)
    arithmetic = aa+jump-jump*x
    require(sp.factor(arithmetic-harmonic-jump**2*x*(1-x)/(aa+jump*x)) == 0, 'general arithmetic-minus-harmonic identity')
    # At the actual first excited level E=4, the full-form frame bound is
    # weaker than, and consistent with, the exact low-space Gram weight.
    frame_bound = 1-alpha/full_floor
    exact_weight = 1-leakage
    require(frame_bound == r(27,175) and exact_weight == r(9,25) > frame_bound, 'full-window versus exact low-source frame')
    return {
        'passed':True,'hamiltonian':['0','4','7','11'],
        'retained_nonvacuum_vector':list(map(str,v)),
        'leakage_squared':str(leakage),'inverse_cap':str(inverse_cap),
        'full_form_floor':str(full_floor),'restricted_compression_floor':str(compressed_floor),
        'compressed_inverse_PSD_pivots':inverse_pivots,'full_form_PSD_pivots':full_pivots,
        'restricted_compression_PSD_pivots':compression_pivots,
        'full_form_saturation_vector':list(map(str,nullvector)),
        'wrong_full_floor_determinant':str(bad_determinant),
        'wrong_retained_vacuum_expectation':str(vacuum_counter),
        'arithmetic_minus_harmonic':'(t-a)^2*x*(1-x)/(a+(t-a)*x), 0<=x<=1',
        'energy_four_frame_lower':str(frame_bound),'exact_low_frame_weight':str(exact_weight),
        'scope':'Exact four-state full pseudoinverse/form and failure controls. No general operator, infinite-product or actual Wilson limit is machine-certified.',
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output',type=Path,required=True)
    args = parser.parse_args()
    if args.output.exists():
        raise FileExistsError('Choose a fresh output path')
    result = controls()
    source = Path(__file__).resolve()
    proof = source.with_name('LITERAL_INVERSE_ENERGY_FULL_FORM.md')
    result['source_sha256'] = {p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in (source,proof)}
    args.output.parent.mkdir(parents=True,exist_ok=True)
    with args.output.open('x',encoding='utf-8',newline='\n') as stream:
        json.dump(result,stream,indent=2,sort_keys=True)
        stream.write('\n')
    print('PASS: exact inverse-energy full form and both negative controls')


if __name__ == '__main__':
    main()
