import os
import shutil

BASE_DIR = r"c:\Users\ats31\.gemini\antigravity\playground\scalar-cluster\CLEANUP TEST\MAXWELL"

# Destination Folders
DECAY = os.path.join(BASE_DIR, "Decay_Estimates")
HODGE = os.path.join(BASE_DIR, "Hodge_Structure")
MASSIVE = os.path.join(BASE_DIR, "Massive_Maxwell_Theory")
COVARIANCE = os.path.join(BASE_DIR, "Covariance_Methods")
RIGIDITY = os.path.join(BASE_DIR, "Rigidity_Bianchi")
LEGACY = os.path.join(BASE_DIR, "Legacy_Artifacts")

# Priority is top to bottom
RULES = [
    # Rigidity / Bianchi
    (["BIANCHI", "CALLADINE", "RIGIDITY"], RIGIDITY),
    
    # Decay / Estimates
    (["DAVIES", "COMBES", "THOMAS", "DECAY", "GREEN", "EXPONENTIAL", "BOUND"], DECAY),
    
    # Covariance / Helffer-Sjoestrand
    (["HELFFER", "SJOSTRAND", "COVARIANCE", "HS_"], COVARIANCE),
    
    # Hodge / Wilson Structure
    (["HODGE", "WILSON", "LAPLACIAN", "DISCRETE", "CURL", "STRUCT", "SELECTION_C"], HODGE),
    
    # Massive Maxwell Core
    (["MAXWELL", "MASSIVE", "MATRIX_HINGE", "PROCA", "VACUUM", "EXTRACT_01"], MASSIVE),
    
    # Legacy / Meta
    (["INDEX", "README", "OVERVIEW"], LEGACY)
]

def organize():
    files = [f for f in os.listdir(BASE_DIR) if os.path.isfile(os.path.join(BASE_DIR, f))]
    
    for f in files:
        upper = f.upper()
        src = os.path.join(BASE_DIR, f)
        
        # Determine destination
        target_dir = None
        for keywords, dest in RULES:
            if any(k in upper for k in keywords):
                target_dir = dest
                break
        
        # Fallback for remaining "Maxwell"-ish files if not caught above
        # If it has "MAXWELL" but wasn't caught by Decay/Rigidity, put it in Massive
        if not target_dir and "MAXWELL" in upper:
            target_dir = MASSIVE

        if target_dir:
            dest = os.path.join(target_dir, f)
            print(f"Moving {f} -> {os.path.basename(target_dir)}")
            try:
                shutil.move(src, dest)
            except Exception as e:
                print(f"Error moving {f}: {e}")
        else:
            print(f"Skipped {f} (No Match)")

if __name__ == "__main__":
    organize()
