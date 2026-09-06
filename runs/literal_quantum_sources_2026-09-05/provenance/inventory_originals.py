"""Read-only planning inventory; does not assemble or seal a canonical run."""
from __future__ import annotations

import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
BASE = HERE.parents[1]
ROOT = HERE.parents[5]

INPUTS = {
    'next_quantum_score_center/TRUE_GROUND_CENTER_SCORE_OBSTRUCTION.md': 'proof',
    'next_quantum_score_center/check_central_score_identity_independent.py': 'original_control',
    'next_quantum_score_center/central_score_identity_independent.json': 'original_report',
    'next_quantum_score_center/INDEPENDENT_CENTRAL_SCORE_AUDIT.md': 'audit',
    'next_literal_inverse/LITERAL_INVERSE_ENERGY_FULL_FORM.md': 'proof_addendum',
    'next_literal_inverse/check_literal_inverse_energy.py': 'original_control',
    'next_literal_inverse/literal_inverse_energy_controls.json': 'original_report',
    'next_literal/LITERAL_VACUUM_COARSE_PROJECTION.md': 'proof',
    'next_literal/GROUND_MARGINAL_SCHUR_SCORE.md': 'proof',
    'next_literal_common/COMMON_GAUSS_LITERAL_FAST_FLOOR.md': 'proof',
    'next_gaussian_full/ENTIRE_GAUSSIAN_LITERAL_COMPLEMENT.md': 'proof',
    'next_literal/check_literal_vacuum_projection.py': 'original_control',
    'next_literal/check_literal_vacuum_projection.json': 'original_report',
    'next_literal_common/check_common_gauss_literal_projection.py': 'original_control',
    'next_literal_common/check_common_gauss_literal_projection.json': 'original_report',
    'next_literal/score_controls/check_ground_marginal_score.py': 'original_control',
    'next_literal/score_controls/ground_marginal_score_controls_final.json': 'original_report',
    'next_gaussian_full/check_entire_gaussian_literal_complement.py': 'original_control',
    'next_gaussian_full/check_entire_gaussian_literal_complement.json': 'original_report',
    'next_literal_common/ROOT_COMMON_GAUSS_AUDIT.md': 'audit',
    'next_literal/score_controls/INDEPENDENT_SCORE_AND_LITERAL_AUDIT.md': 'audit',
    'next_gaussian_full/INDEPENDENT_GAUSSIAN_FULL_AUDIT.md': 'audit',
}


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    records, missing, declared, failures = [], [], [], []
    for relative, kind in INPUTS.items():
        path = BASE / relative
        if not path.is_file():
            missing.append({'path': path.relative_to(ROOT).as_posix(), 'kind': kind})
            continue
        records.append({
            'path': path.relative_to(ROOT).as_posix(), 'kind': kind,
            'sha256': digest(path), 'bytes': path.stat().st_size,
            'proposed_original_tree_path': 'original_tree/' + path.relative_to(ROOT).as_posix(),
            'documentary_basename': path.name,
        })
        if kind != 'original_report':
            continue
        data = json.loads(path.read_text(encoding='utf-8'))
        if 'sources' in data:
            mappings = [(ROOT / name, sha) for name, sha in data['sources'].items()]
        elif isinstance(data.get('source_sha256'), dict):
            mappings = [(path.parent / name, sha) for name, sha in data['source_sha256'].items()]
        elif isinstance(data.get('source_sha256'), str):
            source_name = ('check_ground_marginal_score.py' if 'score_controls' in path.parts
                           else 'check_central_score_identity_independent.py' if 'next_quantum_score_center' in path.parts
                           else path.with_suffix('.py').name)
            mappings = [(path.with_name(source_name), data['source_sha256'])]
        else:
            mappings = []
            failures.append({'report': relative, 'reason': 'source-pin schema requires inspection'})
        for source, expected in mappings:
            actual = digest(source) if source.is_file() else None
            item = {
                'report': path.relative_to(ROOT).as_posix(),
                'source': source.relative_to(ROOT).as_posix(),
                'expected_sha256': expected, 'actual_sha256': actual, 'matches': expected == actual,
            }
            declared.append(item)
            if expected != actual:
                failures.append(item)
    metadata = []
    for name in ('results.yaml', 'documents.yaml'):
        path = HERE.parent / 'staged_docs' / name
        if path.is_file():
            metadata.append({'path': path.relative_to(ROOT).as_posix(), 'sha256': digest(path), 'status': 'staged, not canonical or frozen'})
    report = {
        'schema': 'workhouse-next-literal-run-plan/v1',
        'status': 'authorized assembly snapshot; final canonical proof/native freezes pending',
        'existing_input_count': len(records), 'inputs': records,
        'required_inputs_not_yet_written': missing,
        'original_declared_source_pins': declared,
        'source_pin_mismatches': failures,
        'staged_metadata': metadata,
        'excluded_draft_report': 'next_literal/score_controls/ground_marginal_score_controls.json',
        'canonical_run_created': False,
    }
    (HERE / 'CURRENT_ORIGINAL_INPUTS.json').write_text(json.dumps(report, indent=2, sort_keys=True)+'\n', encoding='utf-8')
    print(json.dumps({k:report[k] for k in ('status','existing_input_count','required_inputs_not_yet_written','source_pin_mismatches','canonical_run_created')}, indent=2))


if __name__ == '__main__':
    main()
