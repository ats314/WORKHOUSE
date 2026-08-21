"""
Organize TENSOR_NETWORK files into 8 subfolders
"""
import os
import shutil
from pathlib import Path

BASE = Path(r"C:\Users\ats31\.gemini\antigravity\playground\scalar-cluster\CLEANUP TEST\TENSOR_NETWORK")

# Create subfolders
folders = [
    "01_QRACAH_DOOB_GAP",
    "02_Q6J_SYMBOLS", 
    "03_THETA_DEFORMATION",
    "04_HOTRG_METHODS",
    "05_TRANSFER_OPERATOR",
    "06_LATTICE_QCD_SECTORS",
    "07_TOPOLOGICAL_SUSCEPTIBILITY",
    "08_MISC",
    "Model_Creation",
    "tools"
]

for folder in folders:
    (BASE / folder).mkdir(exist_ok=True)
    print(f"Created: {folder}")

# File categorization rules (keyword-based)
def categorize(filename):
    fn = filename.lower()
    
    # q-Racah / Doob / Gap
    if any(k in fn for k in ['qracah', 'doob', 'racah_doob', 'q_racah']):
        if '6j' not in fn:
            return "01_QRACAH_DOOB_GAP"
    
    # 6j symbols
    if any(k in fn for k in ['6j', 'q6j', 'logspace_qracah']):
        return "02_Q6J_SYMBOLS"
    
    # Theta deformation
    if any(k in fn for k in ['theta', 'deformation', 'quantumgroup']):
        return "03_THETA_DEFORMATION"
    
    # HOTRG methods
    if any(k in fn for k in ['hotrg', 'rank8', 'rank_8', 'vertex_tensor']):
        return "04_HOTRG_METHODS"
    
    # Transfer operator
    if any(k in fn for k in ['transfer_operator', 'casimir', 'transfer operator']):
        return "05_TRANSFER_OPERATOR"
    
    # Lattice QCD
    if fn.startswith('lattice_qcd') or 'yang-mills' in fn or 'su-3' in fn:
        return "06_LATTICE_QCD_SECTORS"
    
    # Topological susceptibility
    if any(k in fn for k in ['chi_top', 'susceptibility', 'chitop']):
        return "07_TOPOLOGICAL_SUSCEPTIBILITY"
    
    # Misc (READMEs, indexes, etc.)
    if any(k in fn for k in ['readme', 'index', '00_', 'runbook', 'selected', 'best_work']):
        return "08_MISC"
    
    # Default to misc
    return "08_MISC"

# Process files
moved = {f: 0 for f in folders}
skipped = []

for item in BASE.iterdir():
    if item.is_file():
        # Skip certain files
        if item.suffix in ['.zip', '.py']:
            skipped.append(item.name)
            continue
        
        category = categorize(item.name)
        dest = BASE / category / item.name
        
        try:
            shutil.move(str(item), str(dest))
            moved[category] = moved.get(category, 0) + 1
            print(f"  {item.name} -> {category}")
        except Exception as e:
            print(f"  ERROR: {item.name}: {e}")

print("\n=== Summary ===")
for folder, count in moved.items():
    if count > 0:
        print(f"{folder}: {count} files")

print(f"\nSkipped (kept at root): {skipped}")
