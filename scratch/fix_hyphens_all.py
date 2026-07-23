import os
import glob

def refactor_file(path):
    with open(path, 'r') as f:
        content = f.read()

    # Fix namespace and structure names that got hyphens
    content = content.replace('S-ArithmeticStructure', 'SArithmeticStructure')
    content = content.replace('S-ArithmeticDescent', 'SArithmeticDescent')
    content = content.replace('LaRueProtorealAlgebra.S-Arithmetic', 'LaRueProtorealAlgebra.SArithmetic')
    
    with open(path, 'w') as f:
        f.write(content)

lean_files = glob.glob('LaRueProtorealAlgebra/*.lean') + glob.glob('InfoPhysAxioms/*.lean') + glob.glob('*.lean')
for f in lean_files:
    refactor_file(f)
print("Fixed hyphens again.")
