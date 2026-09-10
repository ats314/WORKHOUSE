"""Source-level review inventory and independent integer arithmetic, not a Lean build."""
from pathlib import Path
import hashlib
import json
import math
import re

OUT = Path(__file__).resolve().parent
REPO = OUT.parents[2]


def strip_comments(source):
    result = []
    depth = 0
    i = 0
    while i < len(source):
        if source[i:i+2] == '/-':
            depth += 1
            result.extend('  ')
            i += 2
        elif depth and source[i:i+2] == '-/':
            depth -= 1
            result.extend('  ')
            i += 2
        elif not depth and source[i:i+2] == '--':
            while i < len(source) and source[i] != '\n':
                result.append(' ')
                i += 1
        else:
            result.append(source[i] if not depth or source[i] == '\n' else ' ')
            i += 1
    if depth:
        raise ValueError('Unterminated Lean block comment')
    return ''.join(result)


def main():
    objects = json.loads((OUT / 'archive_only_content.json').read_text(encoding='utf-8'))
    selected = [r for r in objects if r['occurrences'][0]['memberpath'].endswith('.lean')]
    live = (REPO / 'ledger/theorems.yaml').read_text(encoding='utf-8')
    records = []
    all_sources = {}
    for row in selected:
        source = (OUT / row['materialized_object']).read_text(encoding='utf-8')
        cleaned = strip_comments(source)
        all_sources[Path(row['occurrences'][0]['memberpath']).name] = source
        found = []
        for i, line in enumerate(cleaned.splitlines(), 1):
            declaration = re.match(r'\s*(?:private\s+)?(theorem|lemma|def|structure|inductive|axiom|opaque)\s+(\S+)', line)
            if declaration:
                found.append({'line': i, 'kind': declaration[1], 'name': declaration[2],
                              'live_theorem_ledger_contains_name': declaration[2] in live})
        records.append({**row, 'source_read_in_full': True,
                        'line_count': len(source.splitlines()), 'declarations': found,
                        'sorry_or_admit': [{'token': m[0], 'line': cleaned[:m.start()].count('\n')+1}
                                           for m in re.finditer(r'\b(?:sorry|admit)\b', cleaned)],
                        'declared_axioms': [r for r in found if r['kind'] == 'axiom'],
                        'native_decide': [{'line': cleaned[:m.start()].count('\n')+1}
                                          for m in re.finditer(r'\bnative_decide\b', cleaned)],
                        'imports': re.findall(r'^import (.+)$', cleaned, re.M)})
    witness = all_sources['Rank3Order4QBoundWitnesses.lean']
    lists = {name: [int(n) for n in re.search(r'def '+name+r' : List ℕ :=\s*\[(.*?)\]', witness, re.S)[1].split(',')]
             for name in ['w2Denoms', 'r2Denoms']}
    q_w2, q_r2, q_haar = 881280, 409824214482575692800, 87071293440000
    q_tight = 62895057857493885215590055852113920000000
    q_path = 4302674844130269372677454153332635148085549843213189120000000
    checks = {'w2_list_length': len(lists['w2Denoms']), 'r2_list_length': len(lists['r2Denoms']),
              'w2_lcm': math.lcm(*lists['w2Denoms']), 'r2_lcm': math.lcm(*lists['r2Denoms']),
              'all_w2_divide': all(q_w2 % d == 0 for d in lists['w2Denoms']),
              'all_r2_divide': all(q_r2 % d == 0 for d in lists['r2Denoms']),
              'q_tight_component_product': q_tight == 2*q_w2*q_r2*q_haar,
              'analytic_896_divides': q_tight % 896 == 0,
              'q_path_quotient': q_path // q_tight, 'q_path_divisible': q_path % q_tight == 0,
              'explicit_w2_quotient_matches': q_tight == q_w2*71367848876059691829600190464000000,
              'explicit_r2_quotient_matches': q_tight == q_r2*153468378965606400000}
    if checks['w2_lcm'] != q_w2 or checks['r2_lcm'] != q_r2 or not all(v for v in checks.values()):
        raise ValueError('Independent denominator arithmetic check failed')
    result = {'review': 'All five recovered Lean source files read in full; three mathematical modules and two import wrappers.',
              'verification_scope': 'Comment-aware source inventory and independent Python integer checks. No fresh Lean compilation or axiom audit inferred.',
              'files': records, 'independent_integer_checks': checks,
              'current_theorem_register_sha256': hashlib.sha256((REPO/'ledger/theorems.yaml').read_bytes()).hexdigest(),
              'missing_physics_premises': ['Complete enumeration of physical perturbative histories and primitive factors.',
                                         'Identity of the external hash-pinned coefficient ledger with the formal literal denominator lists.',
                                         'Numerators, linked-vacuum folds and spectral/continuum estimates.'],
              'scope_conclusion': 'Potential reusable exact denominator/CRT infrastructure. It supplies no unconditioned G19 scale estimate, Wilson H2 remainder, or continuum Yang-Mills mass-gap theorem.'}
    (OUT/'RECOVERED_LEAN_REVIEW.json').write_text(json.dumps(result, indent=2, ensure_ascii=False)+'\n', encoding='utf-8')
    print(json.dumps({'files': len(records), 'declared_axioms': sum(len(r['declared_axioms']) for r in records),
                      'sorry_or_admit': sum(len(r['sorry_or_admit']) for r in records),
                      'native_decide': sum(len(r['native_decide']) for r in records), 'integer_checks': checks}, indent=2))


if __name__ == '__main__':
    main()
