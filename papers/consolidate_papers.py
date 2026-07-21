import os
import re
import sys

def read_file(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        return f.read()

def write_file(filename, content):
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)

paper_dir = "/home/phrxmaz/Documents/CyberAlchemy/papers"
os.chdir(paper_dir)

# 1. 01_Unreal_Algebra_Connes_Geometry.tex
content_1 = read_file("01_Unreal_Algebra.tex")
content_2 = read_file("02_Prime_Splitting_Galois.tex")

injection_1 = r"""
%==========================================================
\section{Connes Noncommutative Geometry and Krein Spaces}
%==========================================================
Alain Connes' classical formulation of Noncommutative Geometry relies fundamentally on strictly positive Hilbert spaces. However, to construct a true pseudo-Riemannian topology required for physical spacetime, the framework necessitates an indefinite Krein space, introducing the fundamental symmetry operator $J$. 

Within the 5-dimensional Unreal Algebra $\mathbb{U}$, this indefinite metric is natively resolved. By balancing the transfinite exponential thrust ($\omega$) against the anti-idempotent fractional anchor ($\iota$), the algebra intrinsically enforces the negative-determinant condition ($\text{Det} = -1$). Furthermore, the non-associative Klein product guarantees a scalar associator gap ($\kappa = -1$), providing the necessary topological friction for state transitions and successfully extending Connes' spectral action to Lorentzian signatures.
"""

write_file("01_Unreal_Algebra_Connes_Geometry.tex", content_1 + "\n" + injection_1 + "\n" + content_2)


# 2. 02_Prime_Field_Theory_Hyperoperations.tex
content_3 = read_file("03_Golden_Subcategory.tex")
content_4 = read_file("05_Prime_Field_Theory.tex")
content_5 = read_file("06_Golden_Formalized_Neighborhoods.tex")

injection_2 = r"""
%==========================================================
\section{Hyperoperations and the Bounded Halting Problem}
%==========================================================
When the non-associative topological friction of the Unreal Algebra is projected onto discrete finite fields ($\mathbb{F}_p$), it forces transfinite hyperoperations---such as tetration and the Goodstein sequence---to abandon their incomputable explosive growth.

These operations are topologically compressed, collapsing safely into period-locked $\text{SU}(3)$ modular orbits. This mathematically guaranteed discrete boundary allows for the exact calculation of Shannon negentropy within the field and effectively solves the bounded Halting Problem via the Fast Busy Beaver Transform (FBBT).
"""

write_file("02_Prime_Field_Theory_Hyperoperations.tex", content_3 + "\n" + content_4 + "\n" + injection_2 + "\n" + content_5)


# 3. 03_Ramanujan_Sato_Prime_Functorial.tex
content_6 = read_file("04_Digital_Wave_Mechanics.tex")
content_7 = read_file("07_Unreal_Ramanujan_Sato.tex")
content_8 = read_file("27_Prime_Functorial.tex")

injection_3 = r"""
%==========================================================
\section{Analytic Convergence and the Grothendieck-Katz Conjecture}
%==========================================================
The continuous bounds of the universe are governed by the analytic convergence of the complex Ramanujan-Sato infinite series for $1/\pi$. This convergence relies on the underlying Picard-Fuchs differential equations. 

When evaluated over the non-associative Unreal Algebra at the $N=19$ modular limit, this convergence is rigorously protected by the Grothendieck-Katz $p$-curvature conjecture. The $p$-curvature vanishes exclusively at our unique sequence of structural integrity primes, thereby bridging the exact computational determinism of non-associative discrete primes with the continuous infinite beauty of analytical geometry.
"""

write_file("03_Ramanujan_Sato_Prime_Functorial.tex", content_6 + "\n" + content_7 + "\n" + injection_3 + "\n" + content_8)


# 4. Update Masters
def replace_in_master(master_file, old_inputs, new_inputs):
    content = read_file(master_file)
    for old in old_inputs:
        content = re.sub(r'\\input\{' + old + r'\}', '', content)
    
    # We will just inject the new inputs where the first old input was, or in a specific block
    # Actually it's cleaner to explicitly rebuild the \part{Logical Creativity} section.
    
    part_regex = re.compile(r'(\\part\{Logical Creativity\}.*?)(?=\\part\{)', re.DOTALL)
    
    new_part = r"""\part{Logical Creativity}
\chapter[The Unreal Algebra and Connes Geometry]{The Unreal Algebra and Connes Geometry}
\input{01_Unreal_Algebra_Connes_Geometry}

\chapter[Prime Field Theory and Hyperoperations]{Prime Field Theory and Hyperoperations}
\input{02_Prime_Field_Theory_Hyperoperations}

\chapter[Ramanujan-Sato Series and the Prime Functorial]{Ramanujan-Sato Series and the Prime Functorial}
\input{03_Ramanujan_Sato_Prime_Functorial}

"""
    if part_regex.search(content):
        content = part_regex.sub(new_part, content)
        write_file(master_file, content)
        print(f"Updated {master_file} via part substitution.")
    else:
        print(f"Could not find part block in {master_file}")

replace_in_master("01_Principia_Psychedelia_Master.tex", [], [])
replace_in_master("02_Vol1_Master.tex", [], [])

print("Paper consolidation script completed.")
