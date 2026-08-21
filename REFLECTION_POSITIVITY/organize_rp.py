"""
Organize REFLECTION_POSITIVITY files into subtopics.
"""
import os
import shutil
from pathlib import Path

BASE = Path(r"C:\Users\ats31\.gemini\antigravity\playground\scalar-cluster\CLEANUP TEST\REFLECTION_POSITIVITY")

# Define categories with keywords
CATEGORIES = {
    "01_OS_RECONSTRUCTION": ["OS_", "_OS_", "os_", "Appendix_L", "Core_3__OS", "D_OS", "SYNTH_CONJ", "J_one_step", 
                              "EXTRACT_05_CONJ", "SELECTED_05", "06_OS_mass"],
    "02_RP_FUNDAMENTALS": ["reflection_positivity", "Reflection_Positivity", "Appendix_K", "rulebook_entry", 
                           "02_Reflection", "08_reflection", "RP_", "_RP_"],
    "03_CONTINUUM_LIMITS": ["continuum", "Continuum", "permanence", "Permanence", "projective", "thermo", 
                            "Core_10", "PROOFS_Selected", "Mosco"],
    "04_GAP_BRIDGES": ["bridge", "Bridge", "diffusion", "Diffusion", "DOC_01", "DOC_02", "INEQ_CALC", 
                       "UNIFY_04", "Selection_F", "one_step", "One_Step", "Spectral_Gap"],
    "05_TRANSFER_MATRIX": ["transfer", "Transfer", "strong_coupling"],
    "06_PIPELINES_ROADMAPS": ["roadmap", "Roadmap", "pipeline", "Pipeline", "INDEX", "index", "README", 
                              "Project_", "PROJECT_", "Checklist", "OUTLINE", "00_"],
    "07_NUMERICAL_TESTS": ["stress_test", "simulation", "numerics", "admissibility"],
}

def categorize_file(filename):
    """Determine which category a file belongs to."""
    for category, keywords in CATEGORIES.items():
        for keyword in keywords:
            if keyword.lower() in filename.lower():
                return category
    return "08_MISC"

def main():
    # Get all .md and .txt files in base directory
    files = [f for f in os.listdir(BASE) if f.endswith(('.md', '.txt', '.tex')) and os.path.isfile(BASE / f)]
    
    print(f"Found {len(files)} files to organize")
    
    moved = {cat: 0 for cat in list(CATEGORIES.keys()) + ["08_MISC"]}
    
    for f in files:
        category = categorize_file(f)
        src = BASE / f
        dst = BASE / category / f
        
        try:
            shutil.move(str(src), str(dst))
            moved[category] += 1
        except Exception as e:
            print(f"Error moving {f}: {e}")
    
    print("\nFiles moved:")
    for cat, count in moved.items():
        print(f"  {cat}: {count}")

if __name__ == "__main__":
    main()
