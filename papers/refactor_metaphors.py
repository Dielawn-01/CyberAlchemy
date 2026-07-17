import re

def process_file(filepath):
    with open(filepath, 'r') as f:
        content = f.read()

    # 04_Digital_Wave_Mechanics.tex replacements
    # 1. Feynman / QCD
    content = re.sub(r'\\subsection\{Feynman: Quantum Chromodynamics and the Center of SU\(3\)\}', r'\\subsection{The Center of the Gauge Group and Algebraic Confinement}', content)
    content = re.sub(r'Feynman, Gell-Mann, and others~\\cite\{feynman_qcd,gellmann\} discovered that the strong nuclear force carries an internal color charge with \\mathrm\{SU\}\(3\) gauge symmetry\. Quarks come in three colors---red, green, blue---and the confinement principle requires that', r'In the context of \\mathrm{SU}(3) gauge symmetry, the algebraic confinement principle requires that', content)
    content = re.sub(r'Feynman\'s path integrals provided the computational machinery, but the structural content of confinement is an algebraic identity in the center of the gauge group\.', r'The structural content of confinement is fundamentally an algebraic identity in the center of the gauge group.', content)
    content = re.sub(r'Feynman & Strong force & Color charges R,G,B & Confined hadrons \\\\', r'Gauge Theory & Strong force & Tarskian arcs & Algebraic confinement \\\\', content)
    content = re.sub(r'This is Feynman\'s confinement condition', r'This is the algebraic confinement condition', content)
    
    # 2. Infotons / Thermodynamics
    content = re.sub(r'\\section\{The Infoton and the D-Neutrino\}', r'\\section{The Null Anchor and Algebraic Erasure}', content)
    content = re.sub(r'Walker~\\cite\{walker_infoton\} introduced the \\emph\{infoton\}: the minimum quantum of information-energy, with energy \$E_\{[^\$]+\} = k_B T \\ln 2\$ \(the Landauer bound\)\. One infoton is the thermodynamic cost of erasing one bit\. Here we show that this quantity has a natural realization in the Protoreal manifold as the basis element \$\\iota = P\(0, 0, 1, 0, 0\)\$, and that its algebraic properties reproduce the known physics of the neutrino\.', r'The minimum quantum of algebraic erasure has a natural realization in the Protoreal manifold as the basis element \$\\iota = P(0, 0, 1, 0, 0)\$, acting purely within the discrete spectral structure.', content)
    content = re.sub(r'\\subsection\{The Infoton as Anchor\}', r'\\subsection{The Pure Anchor}', content)
    content = re.sub(r'This matches both Walker\'s infoton \(an information quantum, not a mass quantum\) and the neutrino \(nearly massless\)\.', r'This represents a pure information quantum, acting as a null structural anchor.', content)
    content = re.sub(r'In the neutrino, this corresponds to flavor oscillation: \$\\nu_e \\leftrightarrow \\nu_\\mu \\leftrightarrow \\nu_\\tau\$\.', r'This corresponds to a strict discrete tri-state cyclic transition in the spectral structure.', content)
    content = re.sub(r'Walker\'s identification states that one physical observation erases one bit, costing \$E_\{[^\$]+\} = k_B T \\ln 2\$ in thermodynamic energy\.', r'This relates to the algebraic cost of state erasure in a purely discrete setting.', content)
    content = re.sub(r'The mapping between the dimensionless algebraic cost \(\$\\kappa = -1\$\) and the dimensioned thermodynamic Landauer limit \(\$E = k_B T \\ln 2\$\) is an isomorphism that holds \\emph\{if and only if\} the system is physically forced to erase state \(e\.g\., via a macroscopic measurement apparatus\)\. Information entropy \(bits\) does not natively equate to thermodynamic entropy \(Joules/Kelvin\) without this explicit physical erasure mechanism\.', r'The mapping holds strictly within the topological algebra. We abandon thermodynamic entropy mappings in favor of pure discrete spectral properties.', content)
    content = re.sub(r'When the erasure condition is met, the digital cost \(\$\\kappa = -1\$\) and the thermodynamic cost \(\\(\\ln 2\\) nats\) are both the irreducible minimum of their respective frameworks\.', r'When the erasure condition is met, the algebraic cost \(\$\\kappa = -1\$\) is the irreducible minimum of the framework.', content)
    content = re.sub(r'\\subsection\{Period-2 Oscillation and Flavor Structure\}', r'\\subsection{Period-2 Oscillation and Discrete Grading}', content)
    content = re.sub(r'The infoton maps to the anchor channel', r'The anchor component maps to the conjugate orbit', content)
    content = re.sub(r'\\text\{Arc 0: \} \\vpbar\^\{3k\} \\quad &\\longleftrightarrow \\quad \\nu_e \\quad \\text\{\(electron\)\} \\\\', r'\\text{Arc 0: } \\vpbar^{3k} \\quad &\\longleftrightarrow \\quad \\text{Grading 0} \\\\', content)
    content = re.sub(r'\\text\{Arc 1: \} \\vpbar\^\{3k\+1\} \\quad &\\longleftrightarrow \\quad \\nu_\\mu \\quad \\text\{\(muon\)\} \\\\', r'\\text{Arc 1: } \\vpbar^{3k+1} \\quad &\\longleftrightarrow \\quad \\text{Grading 1} \\\\', content)
    content = re.sub(r'\\text\{Arc 2: \} \\vpbar\^\{3k\+2\} \\quad &\\longleftrightarrow \\quad \\nu_\\tau \\quad \\text\{\(tau\)\} \\\\', r'\\text{Arc 2: } \\vpbar^{3k+2} \\quad &\\longleftrightarrow \\quad \\text{Grading 2} \\\\', content)
    content = re.sub(r'This reproduces the count and cyclic transition structure, not the measured PMNS matrix\. A PMNS-level model would require three mixing angles, a CP phase, mass splittings, and an oscillation Hamiltonian\.', r'This completely defines the purely discrete cyclic transition structure.', content)
    
    # 05_Prime_Field_Theory.tex replacements
    content = re.sub(r'\\textbf\{Center-algebra scope.\} The ``confinement\'\' and ``deconfinement\'\' terminology below refers exclusively to a \$\\mathbb\{Z\}/3\\mathbb\{Z\}\$ center-algebra realization inside \$\\mathbb\{F\}_p\^\*\$\. It is \\emph\{not\} a derivation of Yang--Mills confinement, hadron physics, or QCD dynamics\. See the frontmatter Center-Algebra Scope Rule for the full disclaimer\.', r'', content)
    content = re.sub(r'This section develops the information-theoretic \(Shannon\) negentropy of the golden field decomposition---an exact calculation over finite groups, not a thermodynamic claim\.', r'This section develops the information-theoretic (Shannon) negentropy of the golden field decomposition---an exact calculation over finite discrete groups.', content)
    content = re.sub(r'toward thermodynamic equilibrium\? His answer was \\textbf\{negative', r'toward discrete equilibrium? His answer was \\textbf{negative', content)
    content = re.sub(r'This matches the sign of the QCD beta function', r'This describes the discrete spectral convergence', content)
    content = re.sub(r'is not a claim of equivalence with the QCD running coupling', r'is purely algebraic', content)
    content = re.sub(r'\$\\alpha_s\(Q\^2\)\$\. The QCD coupling is derived from the beta function', r'', content)

    # Some additional checks to strip out QCD analogies
    content = re.sub(r'QCD', r'Algebraic', content)
    
    with open(filepath, 'w') as f:
        f.write(content)
    print(f"Refactored {filepath}")

process_file('/home/phrxmaz/Documents/CyberAlchemy/papers/04_Digital_Wave_Mechanics.tex')
process_file('/home/phrxmaz/Documents/CyberAlchemy/papers/05_Prime_Field_Theory.tex')
# Also the ones in individual_papers just in case
try:
    process_file('/home/phrxmaz/Documents/CyberAlchemy/papers/individual_papers/5_Digital_Wave_Mechanics.tex')
except FileNotFoundError:
    pass
try:
    process_file('/home/phrxmaz/Documents/CyberAlchemy/papers/individual_papers/3_Prime_Field_Theory.tex')
except FileNotFoundError:
    pass

