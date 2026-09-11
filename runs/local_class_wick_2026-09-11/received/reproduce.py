"""Reproduce into a NEW directory; never overwrite an earlier run."""
import argparse
import shutil
import subprocess
import sys
from pathlib import Path
p=argparse.ArgumentParser()
p.add_argument("--out",type=Path,required=True)
args=p.parse_args()
src=Path(__file__).resolve().parent
out=args.out.resolve()
if out.exists(): raise FileExistsError(out)
out.mkdir(parents=True)
for name in ("wick_gap.py","independent_su3.py","verify_wick.py","verify_order5.py","requirements.txt"):
    shutil.copy2(src/name,out/name)
shutil.copytree(src/"sources",out/"sources")
commands=[
    ["wick_gap.py","--order","4","--out","coefficients_order4.json"],
    ["wick_gap.py","--order","5","--out","coefficients_order5.json"],
    ["independent_su3.py"],["verify_wick.py"],["verify_order5.py"],
]
for i,argv in enumerate(commands,1):
    command=[sys.executable,"-B","-u",*argv]
    print("RUN",*command,flush=True)
    with (out/f"{i:02d}-{Path(argv[0]).stem}.log").open("w",encoding="utf-8") as log:
        run=subprocess.run(command,cwd=out,stdout=log,stderr=subprocess.STDOUT,text=True)
    if run.returncode: raise SystemExit(f"FAILED {argv}; inspect {out}")
print("All reproductions passed:",out)

