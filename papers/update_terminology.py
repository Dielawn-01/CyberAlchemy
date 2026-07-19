import os
import re

FILES_TO_UPDATE = [
    "1a_Unreal_Algebra.tex",
    "1_Logical_Creativity.tex",
    "07_Metareal_ASI_Chromodynamics.tex",
    "8_Metareal_ASI_Chromodynamics.tex",
    "21_Quasicrystal_Physics.tex",
    "19_ASI_Chip.tex",
    "23_Prime_Functorial.tex",
    "ARC_Prize_2026_Plazmik_Omnibus.tex"
]

REPLACEMENTS = [
    (r"\bProtoreal Manifold\b", r"Unital Nonassociative C*-Algebra (Mesh)"),
    (r"\bprotoreal manifold\b", r"unital nonassociative C*-algebra (mesh)"),
    (r"\bPure Real Projection\b", r"GNS Vacuum State Functional ($\\omega$)"),
    (r"\bpure real projection\b", r"GNS vacuum state functional ($\\omega$)"),
    (r"\bDirichlet Basis\b", r"GNS Vacuum State Functional ($\\omega$)"),
    (r"\bDirichlet basis\b", r"GNS vacuum state functional ($\\omega$)"),
    (r"\bAQFT Truncation\b", r"GNS Null Space Quotient ($\\mathfrak{A}/N_\\omega$)"),
    (r"\bAQFT truncation\b", r"GNS null space quotient ($\\mathfrak{A}/N_\\omega$)"),
    (r"\bsuperepsilon_depth\b", r"GNS null space quotient ($\\mathfrak{A}/N_\\omega$)"),
    (r"\bUmbral Shift\b", r"GNS Involution ($u^*$)"),
    (r"\bumbral shift\b", r"GNS involution ($u^*$)"),
    (r"\bRaw Umbral Shift\b", r"GNS Adjoint Operator ($u^*$)"),
    (r"\braw umbral shift\b", r"GNS adjoint operator ($u^*$)"),
    (r"\bUmbral Calculus\b", r"GNS Adjoint Calculus"),
    (r"\bumbral calculus\b", r"GNS adjoint calculus"),
    (r"\bGolden Field Rotations\b", r"Unitary GNS Representations ($\\pi_\\omega$)"),
    (r"\bgolden field rotations\b", r"unitary GNS representations ($\\pi_\\omega$)"),
    (r"\bZero-Point Energy\b", r"Cyclic Vacuum Vector ($\\Omega_\\omega$)"),
    (r"\bZero-Point energy\b", r"Cyclic vacuum vector ($\\Omega_\\omega$)"),
    (r"\bZPE\b", r"$\\Omega_\\omega$")
]

def update_file(filename):
    if not os.path.exists(filename):
        print(f"Skipping {filename}, does not exist.")
        return
        
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
        
    new_content = content
    for pattern, replacement in REPLACEMENTS:
        # We need to escape backslashes in replacement string so re.sub doesn't interpret them
        replacement_escaped = replacement.replace('\\', '\\\\')
        new_content = re.sub(pattern, replacement_escaped, new_content)
        
    if new_content != content:
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated {filename}")
    else:
        print(f"No changes for {filename}")

if __name__ == "__main__":
    for f in FILES_TO_UPDATE:
        update_file(f)
