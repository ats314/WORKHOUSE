"""Freeze bounded read coverage and exact counterexample controls, never sources."""
from __future__ import annotations

import hashlib
import json
from collections import defaultdict
from pathlib import Path

import sympy as s

OUT = Path(__file__).resolve().parent
ROOT = Path('C:/WORKHOUSE')


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def intervals(values: set[int]) -> list[list[int]]:
    result: list[list[int]] = []
    for value in sorted(values):
        if not result or value != result[-1][1] + 1:
            result.append([value, value])
        else:
            result[-1][1] = value
    return result


seen: dict[str, set[int]] = defaultdict(set)
for row in map(json.loads, (OUT / 'SYNTH_READ_RANGES.jsonl').read_text(encoding='utf-8').splitlines()):
    seen[row['file']].update(range(row['line_start'], row['line_end'] + 1))

coverage = []
for path in sorted((ROOT / 'SYNTH_COPY').glob('Synthesis_*.md')):
    count = len(path.read_text(encoding='utf-8').splitlines())
    read = seen[path.name]
    assert read <= set(range(1, count + 1))
    coverage.append({
        'source_path': str(path), 'sha256': digest(path), 'bytes': path.stat().st_size,
        'total_lines': count, 'read_lines': len(read),
        'read_ranges': intervals(read), 'unread_ranges': intervals(set(range(1, count + 1)) - read),
        'review_status': 'complete_text_read' if len(read) == count else 'selected_sections_read',
        'scope': 'Reading coverage only; mathematical findings are in SYNTH_COPY_REVIEW.md. No synthesis-wide acceptance.',
    })

originals = []
for relative in [
    '09_ARCHIVE/sorted_second_pass/BEST_02_local_to_global_PI_LSI_via_Lyapunov.md',
    '09_ARCHIVE/sorted_second_pass/EXCITING_02_HS_COVARIANCE_MASSIVE_MAXWELL.md',
    '05_LEAN/synthesis10_source/SourceTermPersistence.lean',
    '05_LEAN/synthesis10_source/QRacahDoob.lean',
]:
    path = ROOT / relative
    originals.append({'source_path': str(path), 'sha256': digest(path),
                      'read_ranges': [[1, len(path.read_text(encoding='utf-8').splitlines())]],
                      'scope': 'Full text read in supplemental original-source comparison; Lean not compiled in this audit.'})

payload = {
    'date': '2026-09-07',
    'scope': 'Bounded semantic source-family review, not complete review of 19 documents or their cited originals.',
    'synthesis_files': coverage, 'supplemental_originals': originals,
    'summary': {'files': len(coverage), 'distinct_sha256': len({r['sha256'] for r in coverage}),
                'bytes': sum(r['bytes'] for r in coverage),
                'lines': sum(r['total_lines'] for r in coverage),
                'read_lines': sum(r['read_lines'] for r in coverage),
                'complete_text_reads': sum(r['review_status'] == 'complete_text_read' for r in coverage),
                'selected_section_reads': sum(r['review_status'] != 'complete_text_read' for r in coverage)},
    'exact_registration_scope': 'Peer exact-byte join finds Synthesis_15 and Synthesis_19 in the RESEARCH inventory, both pending; other 17 have no exact graph/alias/inventory registration. Shared rewritten content is not excluded.',
    'reading_log_sha256': digest(OUT / 'SYNTH_READ_RANGES.jsonl'),
}
(OUT / 'SYNTH_REVIEW_COVERAGE.json').write_text(json.dumps(payload, ensure_ascii=False, indent=2) + '\n', encoding='utf-8', newline='\n')

# Counterexamples certify the displayed algebra and hypothesis failures only.
checks = []
N = s.Integer(16)
fine_gradient = 1 / N
claimed_rhs = fine_gradient / N
assert s.Integer(1) > claimed_rhs
checks.append({'name': 'pullback_is_not_reverse_conditional_gradient',
               'block_size': int(N), 'coarse_gradient_squared': '1',
               'fine_pullback_gradient_squared': str(fine_gradient),
               'claimed_reverse_rhs': str(claimed_rhs)})

rp = sum((s.Integer(x) - y) * (y - x) for x in [-1, 1] for y in [-1, 1]) / 4
assert rp == -2
checks.append({'name': 'reflection_equivariance_without_positive_half_locality',
               'fine_measure': 'independent symmetric signs; RP form is |E f|^2',
               'coarse_observable': 'y_plus=x_plus-x_minus, y_minus=-y_plus',
               'coarse_RP_form': str(rp)})

diffusion = s.diag(0, 1)
energy = s.diag(0, s.Rational(1, 100))
assert (diffusion - energy).is_positive_semidefinite
checks.append({'name': 'reverse_operator_order_cannot_lower_bound_physical_gap',
               'premise': 'L_conf >= H', 'diffusion_gap': '1', 'physical_gap': '1/100'})

C = s.Matrix([[s.Rational(3, 4), s.Rational(1, 4)], [s.Rational(1, 4), s.Rational(3, 4)]])
assert (s.eye(2) - C).is_positive_semidefinite
assert (C.inv() - s.eye(2)).is_positive_semidefinite
checks.append({'name': 'Loewner_order_not_entrywise_bilinear_order', 'covariance': str(C),
               'precision': str(C.inv()), 'actual_cross_covariance': '1/4', 'claimed_identity_comparison_cross': '0'})

t = s.symbols('t', real=True)
cf = s.exp(-t**2 / 2)
cos0 = cf.subs(t, 1)
cos2 = (-s.diff(cf, t, 2)).subs(t, 1)
cos4 = s.diff(cf, t, 4).subs(t, 1)
m2prime, m4prime = cos2 - cos0, cos4 - 3*cos0
k4prime = s.simplify(m4prime - 6*m2prime)
assert k4prime == s.exp(-s.Rational(1, 2))
checks.append({'name': 'zero_curvature_defect_does_not_imply_Gaussian',
               'potential': 'V_epsilon=x^2/2+epsilon(1-cos x), 0<epsilon<1',
               'uniform_Hessian_floor': '1-epsilon', 'uniform_third_derivative_bound': 'epsilon',
               'fourth_cumulant_derivative_at_zero': str(k4prime)})

rho = [s.Integer(2), s.Rational(3, 2), s.Rational(5, 6), s.Rational(1, 3)]
assert all(rho[j+1] >= rho[j] - 1/rho[j] for j in range(3))
n = s.symbols('n', integer=True, positive=True)
tail_difference = s.factor(1/(n+1) - (1/n - n))
assert tail_difference == (n**3 + n**2 - 1)/(n*(n+1))
checks.append({'name': 'single_Riccati_seed_not_an_infinite_scale_budget',
               'sequence': '2,3/2,5/6,1/3,1/4,1/5,...', 'M': '1',
               'tail_difference_positive_for_n_ge_3': str(tail_difference), 'limit': '0'})

entropy = s.log(2)/2
assert entropy.is_positive
checks.append({'name': 'indicator_entropy_is_not_conditional_entropy',
               'test': 'f=1, mu(K)=1/2', 'Ent_mu(f^2 1_K)': str(entropy), 'local_gradient_energy': '0'})

alpha, b, W = s.symbols('alpha b W', positive=True)
assert s.simplify(-(-alpha*W+b)/W - (alpha-b/W)) == 0
checks.append({'name': 'Lyapunov_division_keeps_unweighted_mass',
               'correct_identity': '-(-alpha W+b)/W=alpha-b/W',
               'repaired_PI_under_stated_hypotheses': 'C_P <= (1+b C_K)/alpha'})

out = {'scope': 'Eight exact algebraic controls for source-audit counterexamples and repairs. They do not test all source derivations, an actual Wilson trajectory, or any Lean build.',
       'checks': checks, 'passed': len(checks), 'checker_sha256': digest(Path(__file__))}
(OUT / 'SYNTH_SCOPE_CONTROLS.json').write_text(json.dumps(out, ensure_ascii=False, indent=2) + '\n', encoding='utf-8', newline='\n')
print(json.dumps({'coverage': payload['summary'], 'controls_passed': len(checks)}, indent=2))
