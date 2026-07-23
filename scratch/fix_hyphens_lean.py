import os
import glob

def refactor_file(path):
    with open(path, 'r') as f:
        content = f.read()

    # Fix all S-Arithmetic -> SArithmetic in lean files
    # because lean does not allow hyphens in identifiers
    content = content.replace('S-Arithmetic', 'SArithmetic')
    
    with open(path, 'w') as f:
        f.write(content)

lean_files = glob.glob('LaRueProtorealAlgebra/*.lean') + glob.glob('InfoPhysAxioms/*.lean') + glob.glob('*.lean')
for f in lean_files:
    refactor_file(f)
print("Fixed hyphens in lean files.")
