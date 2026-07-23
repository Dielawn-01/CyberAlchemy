import os
import glob

def refactor_file(path):
    with open(path, 'r') as f:
        content = f.read()

    # Fix module imports
    content = content.replace('LaRueProtorealAlgebra.S-ArithmeticDescent', 'LaRueProtorealAlgebra.SArithmeticDescent')
    content = content.replace('LaRueProtorealAlgebra.S-ArithmeticStructure', 'LaRueProtorealAlgebra.SArithmeticStructure')
    
    with open(path, 'w') as f:
        f.write(content)

lean_files = glob.glob('LaRueProtorealAlgebra/*.lean') + glob.glob('InfoPhysAxioms/*.lean') + glob.glob('*.lean')
for f in lean_files:
    refactor_file(f)
print("Fixed hyphens.")
