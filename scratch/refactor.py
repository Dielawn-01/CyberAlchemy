import os
import glob

def refactor_file(path):
    with open(path, 'r') as f:
        content = f.read()

    # Replacements
    content = content.replace('Adelic', 'S-Arithmetic')
    content = content.replace('adelic', 's_arithmetic')
    content = content.replace('AdelicStructure', 'SArithmeticStructure')
    content = content.replace('AdelicDescent', 'SArithmeticDescent')
    content = content.replace('InfinityModalTopos', 'InfinityModalCategory')
    content = content.replace('MetaRealTopos', 'MetaRealGrading')
    content = content.replace('Topos', 'Category')
    content = content.replace('topos', 'category')
    
    with open(path, 'w') as f:
        f.write(content)

lean_files = glob.glob('LaRueProtorealAlgebra/*.lean') + glob.glob('InfoPhysAxioms/*.lean') + glob.glob('*.lean')
for f in lean_files:
    refactor_file(f)
print(f"Refactored {len(lean_files)} lean files.")
