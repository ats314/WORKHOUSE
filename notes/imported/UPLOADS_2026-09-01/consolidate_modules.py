import os
import re

def consolidate_group(output_filename, input_filenames, base_dir):
    imports = set()
    file_contents = []

    print(f"Consolidating into {output_filename}...")

    for fname in input_filenames:
        path = os.path.join(base_dir, fname)
        with open(path, 'r') as f:
            lines = f.readlines()
        
        body_lines = []
        for line in lines:
            stripped = line.strip()
            if stripped.startswith('import '):
                imports.add(stripped)
            else:
                body_lines.append(line)
        
        # Trim leading/trailing whitespace from body but keep internal structure
        # Just join them back; we might want to ensure a newline at start/end
        content = "".join(body_lines).strip()
        file_contents.append((fname, content))

    sorted_imports = sorted(list(imports))

    with open(os.path.join(base_dir, output_filename), 'w') as out:
        # Header
        out.write(f"/-\n  Optimized_Lean/{output_filename}\n\n")
        out.write(f"  SUPER-CONSOLIDATED MODULE: {output_filename.replace('.lean', '').upper()}\n")
        out.write(f"  Sources: {', '.join(input_filenames)}\n")
        out.write("-/\n\n")

        # Imports
        for imp in sorted_imports:
            out.write(f"{imp}\n")
        out.write("\n")

        # Bodies
        for fname, content in file_contents:
            out.write(f"/-\n  ------------------------------------------------------------------------------\n")
            out.write(f"  SOURCE: {fname}\n")
            out.write(f"  ------------------------------------------------------------------------------\n")
            out.write("-/\n\n")
            out.write(content)
            out.write("\n\n")

    print(f"Finished {output_filename}")

base_dir = "/home/home/Documents/ANTIGRAVITY/antigravity/playground/scalar-cluster/yang_mills_lean/Optimized_Lean"

groups = [
    (
        "YM_Foundations.lean",
        [
            "Geometry_Combined.lean",
            "Geometric_Analysis_Combined.lean",
            "Lie_Group_Analysis_Combined.lean",
            "Simulation_Tools_Combined.lean"
        ]
    ),
    (
        "YM_GaugeTheory.lean",
        [
            "Gauge_Axioms_Combined.lean",
            "Dynamics_Combined.lean",
            "Quantum_Deformation_Combined.lean",
            "Gauge_Geometry_Advanced_Combined.lean"
        ]
    ),
    (
        "YM_Renormalization.lean",
        [
            "Lattice_Scaling_Combined.lean",
            "Typicality_Simulation_Combined.lean",
            "Renormalization_Advanced_Combined.lean",
            "Continuum_Combined.lean"
        ]
    ),
    (
        "YM_MassGapProof.lean",
        [
            "Physics_Combined.lean",
            "Topology_Anomaly_Combined.lean",
            "Spectral_Convexity_Combined.lean",
            "Master_Theorem_Combined.lean"
        ]
    )
]

for out_file, in_files in groups:
    consolidate_group(out_file, in_files, base_dir)
