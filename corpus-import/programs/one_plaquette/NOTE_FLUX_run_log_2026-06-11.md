# Run log — June 11, 2026 (deposit verification, E:\YANG store)

Environment: sandboxed Linux (Cowork session), Python 3 stdlib only (fractions/itertools/json). Both scripts run from this directory as deposited (byte-identical to delivered copies; MD5 7692946d… / ff5bc466…).

## ENGINE_FLUX_su3_moments_ext.py

```
ALL 27 GATES PASSED (moment engine certified)   [runtime 0.67 s]
```

## ENGINE_FLUX_su3_domino_d3.py

```
GATE PASS lines: 251 / 251   FAIL lines: 0   [runtime ~25 s]
Terminated after all gates with the documented environment caveat:
FileNotFoundError: '/home/claude/review/RUN_TROM_d3_results.json' (authoring-path
JSON write, master doc §6.13; notebook copy is canonical for the JSON).
```

Key constants printed to stdout (order-3 block), matching the certified whitelist:

```
  "order3": {
    "b3 = T3_odd(s=+1)": "1975/124848",
    "T3_even": "-6335/249696",
    "D3_odd": "-24541/62424",
    "D3_even": "-517313/6242400",
    "e_vac3_domino": "-9/16",
    "leak3_odd": "-12331/249696",
    "leak3_even": "-6335/249696",
    "d3 (C-odd flat band, all k)": "-109151/249696",
    "d3_top (C-odd dispersive top, mu=8)": "-61751/249696",
    "m3_even_k0 (A1++ at k=0)": "-54049/520200",
    "m3_even_bandmin (lambda=-4)": "471353/1560600"
  }
```

Full stdout reproducible via: python3 ENGINE_FLUX_su3_moments_ext.py && python3 ENGINE_FLUX_su3_domino_d3.py (run in this directory; the final JSON write requires /home/claude/review/ to exist or the documented one-line cwd fix at next touch — the deposited files are intentionally unmodified).
