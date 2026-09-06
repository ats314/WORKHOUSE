"""Exact finite controls for the true-ground intrinsic-score criterion.

These certify the displayed matrix/torus/scalar models, not the uniform
Wilson score or complement hypotheses in the accompanying analytic note.
"""
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


def zero(expression, label):
    entries = list(expression) if isinstance(expression, sp.MatrixBase) else [expression]
    require(all(sp.simplify(entry) == 0 for entry in entries), label)


def positive_two(matrix):
    zero(matrix - matrix.T, 'symmetric matrix')
    require(matrix[0, 0] > 0 and matrix.det() > 0, 'positive leading minors')


def controls():
    if sys.flags.optimize:
        raise RuntimeError('Exact controls require assertions enabled')
    r = sp.Rational
    a = sp.Matrix([[2, 1], [1, 2]])
    score_values = [sp.Matrix([x, sp.sqrt(2)*y]) for x in (-1, 1) for y in (-1, 1)]
    fisher = sum((s*s.T for s in score_values), sp.zeros(2))/4
    zero(sum(score_values, sp.zeros(2, 1)), 'centered score')
    zero(fisher - sp.diag(1, 2), 'conditional Fisher matrix')
    require(a*fisher != fisher*a, 'noncommuting metric and Fisher')
    positive_two(a)
    beta = sp.Integer(6)
    slack = beta*a.inv() - fisher
    positive_two(slack)
    # This congruence is equivalent to A^(1/2) I A^(1/2)<=beta I.
    generalized_eigenvalues = sorted((a*fisher).eigenvals(), key=sp.default_sort_key)
    require(all(sp.simplify(beta-t) > 0 for t in generalized_eigenvalues), 'operator-norm Fisher cap')
    gvalues = [(sp.ones(2, 1).T*s)[0] for s in score_values]
    variance = sum(g*g for g in gvalues)/4
    correlation = sum((g*s for g, s in zip(gvalues, score_values, strict=True)), sp.zeros(2, 1))/4
    gradient = sp.Matrix([1, 2])
    coarse_form = (gradient.T*a*gradient)[0]/2
    cross = -(gradient.T*a*correlation)[0]/2
    eta, weight = r(1, 4), sp.Integer(12)
    zero(beta-2*eta*weight, 'Fisher factor two')
    require(cross**2 <= eta*coarse_form*weight*variance, 'dimension-free cross bound')
    # The right covariance inequality holds for every linear g and covector,
    # because I<=beta A^-1 and scalar Cauchy-Schwarz are exact PSD statements.

    x, y = sp.symbols('x y', real=True)
    def average(expression, variable):
        return sp.simplify(sp.integrate(sp.expand_trig(expression), (variable, -sp.pi, sp.pi))/(2*sp.pi))
    density = 1+sp.cos(y)/2
    b = (2+sp.cos(x))*sp.sin(y)
    connection_metric = sp.Matrix([[1, b], [b, 1+b*b]])
    zero(connection_metric.det()-1, 'nontrivial connection exact ellipticity determinant')
    score_numerator = sp.diff(density*b, y)
    score = score_numerator/density
    zero(average(density, y)-1, 'conditional density normalization')
    zero(average(score_numerator, y), 'intrinsic score centered')
    g = sp.cos(y)-r(1, 4)
    zero(average(density*g, y), 'conditional mean-zero g')
    expected_derivative = average(density*b*sp.diff(g, y), y)
    correlation_score = average(g*score_numerator, y)
    zero(expected_derivative+correlation_score, 'connection score identity')
    zero(correlation_score-(2+sp.cos(x))/2, 'exact nonzero score correlation')
    only_divergence = average(density*g*sp.diff(b, y), y)
    only_density_term = average(g*b*sp.diff(density, y), y)
    zero(only_divergence-r(7, 16)*(2+sp.cos(x)), 'divergence part')
    zero(only_density_term-r(1, 16)*(2+sp.cos(x)), 'density-connection part')
    require(sp.simplify(only_divergence-correlation_score) != 0, 'omitted density connection is rejected')
    require(sp.simplify(only_density_term-correlation_score) != 0, 'omitted fiber divergence is rejected')
    literal_f = sp.sin(x)
    cross_direct = average(average(density*sp.diff(literal_f, x)*b*sp.diff(g, y)/2, y), x)
    cross_score = -average(sp.diff(literal_f, x)*correlation_score/2, x)
    zero(cross_direct-cross_score, 'direct kinetic and intrinsic-score cross forms agree')
    zero(cross_direct+r(1, 8), 'nonzero actual torus cross form')
    require(cross_direct != 0, 'ignoring the connection gives a false zero')

    alpha, floor = sp.Integer(4), sp.Integer(9)
    form_matrix = sp.Matrix([[alpha, -3], [-3, floor]])
    positive_two(form_matrix)
    delta = (alpha+floor-sp.sqrt((alpha-floor)**2+4*eta*alpha*floor))/2
    zero(form_matrix.charpoly().as_expr().subs(form_matrix.charpoly().gen, delta), 'exact sharp energy eigenvalue')
    require(delta > 0, 'strict positive full gap')
    nullvector = sp.Matrix([3, alpha-delta])
    zero((form_matrix-delta*sp.eye(2))*nullvector, 'gap is attained')
    generalized = sp.Matrix([[1, -sp.sqrt(eta)], [-sp.sqrt(eta), 1]])
    mass = sp.diag(1/alpha, 1/floor)
    zero((generalized-delta*mass).det(), 'generalized form eigenvalue')
    wrong_delta = (alpha+floor-sp.sqrt((alpha-floor)**2+2*eta*alpha*floor))/2
    require(sp.simplify((form_matrix-wrong_delta*sp.eye(2)).det()) < 0,
            'incorrect Fisher factor yields false lower bound')
    schur = alpha-r(9, 1)/floor
    graph_mass = 1+r(9, 1)/floor**2
    normalized = schur/graph_mass
    require(floor*normalized/(floor+normalized) <= delta <= normalized, 'independent Schur sandwich')

    t, v = sp.symbols('t v', positive=True)
    c0, c1, c00, c11 = map(sp.Integer, (2, 3, 5, 4))
    majorant = r(5, 2)
    ratio = (c00+c11*t*v)/(c0*t+c1*t*t*v)
    margin = sp.factor(majorant/t-ratio)
    require(sp.simplify(margin) > 0, 'weighted ratio is bounded by inverse sqrt u')
    endpoint = sp.simplify((majorant/t-ratio).subs(v, 0))
    zero(endpoint, 'weighted constant branch exact endpoint')
    return {
        'passed': True,
        'noncommuting_fisher': {
            'A': str(a), 'I': str(fisher), 'operator_eigenvalues': list(map(str, generalized_eigenvalues)),
            'beta': str(beta), 'eta': str(eta), 'w': str(weight),
            'congruence_slack': str(slack), 'variance_g': str(variance),
            'coarse_form': str(coarse_form), 'cross_form': str(cross),
            'cross_squared': str(cross**2), 'upper_bound': str(eta*coarse_form*weight*variance),
        },
        'nonzero_connection_torus': {
            'conditional_density_relative_to_uniform_Haar': str(density), 'b': str(b),
            'score': str(sp.factor(score)), 'exact_cross_form': str(cross_direct),
            'score_correlation': str(correlation_score),
            'only_divergence': str(only_divergence), 'only_density_connection': str(only_density_term),
            'omitted_connection_negative_control': True,
            'omitted_divergence_negative_control': True,
            'omitted_density_connection_negative_control': True,
        },
        'sharp_gap_model': {
            'matrix': str(form_matrix), 'alpha': str(alpha), 'f0': str(floor), 'eta': str(eta),
            'delta': str(delta), 'exact_eigenvector': str(nullvector),
            'normalized_schur_energy': str(normalized), 'wrong_fisher_factor_rejected': True,
        },
        'weighted_ratio': {'ratio': str(ratio), 'inverse_sqrt_u_majorant': str(majorant/t), 'margin': str(margin)},
        'scope': 'Exact noncommuting finite Fisher model, compact torus connection identity, two-state sharp gap and scalar weighted-ratio controls. No uniform Wilson score, actual interacting-volume fast form or marginal-gap input is certified.',
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    if args.output.exists():
        raise FileExistsError('Choose a fresh output path')
    result = controls()
    source = Path(__file__).resolve()
    result['source_sha256'] = hashlib.sha256(source.read_bytes()).hexdigest()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    with args.output.open('x', encoding='utf-8', newline='\n') as stream:
        json.dump(result, stream, indent=2, sort_keys=True)
        stream.write('\n')
    print('PASS: four exact score/form control families')


if __name__ == '__main__':
    main()
