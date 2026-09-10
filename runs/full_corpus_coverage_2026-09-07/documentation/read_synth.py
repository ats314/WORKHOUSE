"""Number bounded source excerpts and retain their exact reading ranges."""
import json
import sys
from pathlib import Path

root = Path('C:/WORKHOUSE/SYNTH_COPY')
out = Path(__file__).parent
plan = json.loads(sys.argv[1])
logpath = out / 'SYNTH_READ_RANGES.jsonl'
with logpath.open('a', encoding='utf-8', newline='\n') as log:
    for number, ranges in plan.items():
        path, = root.glob(f'Synthesis_{number}_*.md')
        lines = path.read_text(encoding='utf-8').splitlines()
        for start, end in ranges:
            start = start if start > 0 else len(lines) + start + 1
            end = min(len(lines), end if end > 0 else len(lines) + end + 1)
            print(f'FILE: {path.name}; lines {start}-{end} of {len(lines)}')
            for index in range(start - 1, end):
                print(f'{index+1}: {lines[index]}')
            log.write(json.dumps({'file': path.name, 'line_start': start, 'line_end': end, 'total_lines': len(lines), 'kind': 'emitted_for_reading'}, ensure_ascii=False) + '\n')
