import os
import glob

def refactor_tex_files():
    injection_euler = (
        "\n\n% --- HEEGNER INJECTION ---\n"
        "Critically, the topological friction of the Euler-Penrose Engine vanishes precisely at the Heegner prime boundaries "
        "(e.g., 19, 163), forming a ``Hodge Parity Lock'' where the non-commutative shear ($\\kappa$) drops to zero, allowing "
        "frictionless prime identification.\n"
        "% -------------------------\n"
    )

    injection_bode = (
        "\n\n% --- BODE HEEGNER INJECTION ---\n"
        "This quantization bridges macroscopic gravitational dynamics directly to the Ramanujan discrete crossover "
        "($e^{\\pi\\sqrt{163}}$), where the Universal Bode Law phase locks into exact $\\langle 10 \\rangle$ invariant integer states modulo 229, "
        "proving that the Class Number 1 resonance operates at galactic scales.\n"
        "% -------------------------\n"
    )

    count = 0
    for filepath in glob.glob("*.tex"):
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()
        
        modified = False
        
        # Inject Euler-Penrose context (once per file)
        if "Euler-Penrose Engine" in content and "Hodge Parity Lock" not in content:
            content = content.replace("Euler-Penrose Engine", "Euler-Penrose Engine" + injection_euler, 1)
            modified = True
            
        # Inject Bode Law context (once per file)
        if "Universal Bode Law" in content and "Ramanujan discrete crossover" not in content:
            content = content.replace("Universal Bode Law", "Universal Bode Law" + injection_bode, 1)
            modified = True

        if modified:
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(content)
            print(f"Refactored {filepath}")
            count += 1
            
    print(f"Total files refactored: {count}")

if __name__ == "__main__":
    refactor_tex_files()
