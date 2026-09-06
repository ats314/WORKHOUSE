"""Read-only independent replay of the six accepted original control payloads."""
from __future__ import annotations

import sys
sys.dont_write_bytecode = True

import argparse
import hashlib
import importlib.abc
import importlib.util
import json
from pathlib import Path


class NoScientificFallback(importlib.abc.MetaPathFinder):
    def find_spec(self, fullname, path=None, target=None):
        if fullname.split('.', 1)[0] in {'numpy', 'scipy'}:
            raise ImportError('Undeclared numerical dependency blocked: ' + fullname)
        return None


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    if sys.flags.optimize:
        raise RuntimeError('Exact replay requires assertions enabled')
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    if args.output.exists():
        raise FileExistsError('Choose a fresh output path')
    sys.meta_path.insert(0, NoScientificFallback())
    base = Path(__file__).resolve().parents[2]
    root = base.parents[3]
    cases = (
        ('center', 'next_quantum_score_center/check_central_score_identity_independent.py', 'next_quantum_score_center/central_score_identity_independent.json'),
        ('inverse', 'next_literal_inverse/check_literal_inverse_energy.py', 'next_literal_inverse/literal_inverse_energy_controls.json'),
        ('literal', 'next_literal/check_literal_vacuum_projection.py', 'next_literal/check_literal_vacuum_projection.json'),
        ('common', 'next_literal_common/check_common_gauss_literal_projection.py', 'next_literal_common/check_common_gauss_literal_projection.json'),
        ('score', 'next_literal/score_controls/check_ground_marginal_score.py', 'next_literal/score_controls/ground_marginal_score_controls_final.json'),
        ('gaussian', 'next_gaussian_full/check_entire_gaussian_literal_complement.py', 'next_gaussian_full/check_entire_gaussian_literal_complement.json'),
    )
    records = []
    for label, relative, report_name in cases:
        source, report_path = base/relative, base/report_name
        saved = json.loads(report_path.read_text(encoding='utf-8'))
        if 'sources' in saved:
            input_pins = {root/name: digest for name, digest in saved['sources'].items()}
            expected = saved['controls']
        elif isinstance(saved['source_sha256'], dict):
            input_pins = {source.parent/name: digest for name, digest in saved['source_sha256'].items()}
            expected = {key:value for key,value in saved.items() if key != 'source_sha256'}
        else:
            input_pins = {source:saved['source_sha256']}
            expected = {key:value for key,value in saved.items() if key != 'source_sha256'}
        before = {path:sha(path) for path in input_pins}
        assert before == input_pins, (label, 'declared source mismatch')
        spec = importlib.util.spec_from_file_location('original_control_' + label, source)
        assert spec and spec.loader
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        got = module.controls()
        assert got == expected, (label, 'complete payload differs')
        assert before == {path:sha(path) for path in input_pins}, (label, 'source changed')
        records.append({'family':label,'source':relative,'source_sha256':sha(source),
                        'report':report_name,'report_sha256':sha(report_path),
                        'declared_source_pins':len(input_pins),'complete_payload_matches':True})
    result = {'passed':True,'records':records,'numpy_scipy_blocked':True,
              'source_hashes_unchanged':True,'bytecode_disabled':True,
              'scope':'Exact original payload and declared-source replay. No canonical run, cold relocation or full analytic certification is claimed.'}
    args.output.parent.mkdir(parents=True, exist_ok=True)
    with args.output.open('x',encoding='utf-8',newline='\n') as stream:
        json.dump(result,stream,indent=2,sort_keys=True)
        stream.write('\n')
    print('PASS: six original exact payloads and all declared source pins')


if __name__ == '__main__':
    main()
