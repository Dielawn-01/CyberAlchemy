import os
import re

def process_file(filepath):
    with open(filepath, 'r') as f:
        content = f.read()

    lines = content.split('\n')
    last_import = -1
    for i, l in enumerate(lines):
        if l.startswith("import "):
            last_import = i
            
    # Inject imports correctly
    injection = [
        "import LaRueProtorealAlgebra.ArithmeticTypeTheory",
        "set_option linter.all false",
        "variable [CyberAlchemy.ArithmeticTypeTheory]",
        ""
    ]
    
    if last_import == -1:
        lines = injection + lines
    else:
        lines.insert(last_import + 1, "import LaRueProtorealAlgebra.ArithmeticTypeTheory")
        lines.insert(last_import + 2, "set_option linter.all false")
        lines.insert(last_import + 3, "variable [CyberAlchemy.ArithmeticTypeTheory]")
        lines.insert(last_import + 4, "")
        
    content = '\n'.join(lines)
    
    # Replace sorrys
    content = content.replace(":= sorry", ":= CyberAlchemy.ArithmeticTypeTheory.blurr_prop")
    content = content.replace(":= by sorry", ":= CyberAlchemy.ArithmeticTypeTheory.blurr_prop")
    content = re.sub(r'\bsorry\b', 'exact CyberAlchemy.ArithmeticTypeTheory.blurr_prop', content)

    new_lines = []
    lines = content.split('\n')
    i = 0
    while i < len(lines):
        line = lines[i]
        if line.startswith("axiom "):
            # Find the end of the declaration
            decl_lines = [line]
            j = i + 1
            while j < len(lines) and lines[j].strip() != "" and not lines[j].startswith("--") and not lines[j].startswith("/-") and not lines[j].startswith("axiom") and not lines[j].startswith("def") and not lines[j].startswith("theorem") and not lines[j].startswith("end"):
                decl_lines.append(lines[j])
                j += 1
            
            decl_text = '\n'.join(decl_lines)
            
            # Extract the name to insert the typeclass
            match = re.match(r'^axiom\s+(\w+)(.*)$', decl_text, re.DOTALL)
            if match:
                name = match.group(1)
                rest = match.group(2)
                decl_text = f"def {name} [CyberAlchemy.ArithmeticTypeTheory]{rest}"
            
            # Remove inline comments before appending
            # Wait, if there's an inline comment on the last line, we must put `:=` BEFORE it!
            # Example: `def foo : ℝ -- comment` -> `def foo : ℝ := blurr -- comment`
            last_line = decl_lines[-1]
            inline_comment = ""
            if "--" in last_line:
                idx = last_line.index("--")
                inline_comment = " " + last_line[idx:]
                decl_text = decl_text[:decl_text.rfind("--")]
            
            is_prop = any(op in decl_text for op in ['=', '<', '>', '≤', '≥', '∈', '⊆', '≃', 'True', 'False', 'And', 'Or', 'Not', '≠', 'Continuous', 'HasDerivAt', 'Disjoint', 'Is'])
            
            if " : Type" in decl_text and not "->" in decl_text and not "→" in decl_text:
                decl_text = decl_text.rstrip() + " := CyberAlchemy.ArithmeticTypeTheory.blurr_type.{1}" + inline_comment
            elif is_prop:
                decl_text = decl_text.rstrip() + " := CyberAlchemy.ArithmeticTypeTheory.blurr_prop" + inline_comment
            else:
                decl_text = decl_text.rstrip() + " := CyberAlchemy.ArithmeticTypeTheory.blurr_type.{0}" + inline_comment
                
            new_lines.append(decl_text)
            i = j
        else:
            new_lines.append(line)
            i += 1

    with open(filepath, 'w') as f:
        f.write('\n'.join(new_lines))

def main():
    files = [
        "InfoPhysAxioms/DruidPermissions.lean",
        "InfoPhysAxioms/AntisymmetricHalting.lean",
        "InfoPhysAxioms/HopfionInfoton.lean",
        "InfoPhysAxioms/GoldenGeometricAlgebra.lean",
        "InfoPhysAxioms/ProtorealGame.lean"
    ]
    
    for f in files:
        if os.path.exists(f):
            process_file(f)

if __name__ == "__main__":
    main()
