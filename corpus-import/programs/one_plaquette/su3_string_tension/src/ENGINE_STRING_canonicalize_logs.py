#!/usr/bin/env python3
from __future__ import annotations
import re, sys
from pathlib import Path
root=Path(sys.argv[1])
sp=root/'support_scan_raw.log'
if sp.exists():
    s=sp.read_text()
    s=re.sub(r'("walltime_seconds"\s*:\s*)[0-9.eE+-]+', r'\1null', s)
    sp.write_text(s)
vp=root/'physical_verify.log'
if vp.exists():
    lines=[]
    for line in vp.read_text().splitlines():
        if line.startswith('CERTIFICATE '):
            line='CERTIFICATE results/CERT_STRING_su3_tension_physical_o6_certificate.json'
        lines.append(line)
    vp.write_text('\n'.join(lines)+'\n')
print('canonicalized logs')
