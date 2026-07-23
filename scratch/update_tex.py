with open("papers/ARC_Prize_2026_Plazmik_Omnibus.tex", "r") as f:
    content = f.read()

# Update Abstract
old_abstract = "In Part I (Logical Creativity) and Part II (Prime Field Theory), we construct the discrete, non-associative Unital Nonassociative C*-Algebra (Mesh), proving that cognitive phase transitions mathematically mirror prime-field Galois structures and Golden Ratio equilibrium."
new_abstract = "In Part I (Arithmetic Type Theory \\& Logical Creativity) and Part II (Prime Field Theory), we construct the foundational logic of the universe as a pure \\emph{Arithmetic Topos}. We formally replace continuous associative geometry with \\textbf{Arithmetic Type Theory (ATT)}, demonstrating that the Euler-Grothendieck-Penrose (EGP) bridge operates as an \\emph{\\'etale descent} mechanism over discrete L-spaces. This proves that cognitive phase transitions mathematically mirror prime-field Galois structures and Golden Ratio equilibrium, with the Frobenius endomorphism explicitly generating the HoTT path identity."
content = content.replace(old_abstract, new_abstract)

# Update Part I Title
content = content.replace("\\part{The Core Architecture of Fluid Reasoning}", "\\part{Arithmetic Type Theory \\& The Core Architecture of Fluid Reasoning}")

# Update Part I Abstract
old_part_abstract = "In \\textbf{Part I (Logical Creativity)}, we construct the 5-dimensional Base and Non-Associative 5-Space Algebras ($\\Bseed, \\Afive$). By enforcing a strict scalar associator gap ($\\kap = -1$) and a negative-determinant condition ($\\mathrm{Det} = -1$), the characteristic polynomial locks to $X^2 - X - 1 = 0$, establishing the golden ratio as the native algebraic generator."
new_part_abstract = "In \\textbf{Part I (Arithmetic Type Theory \\& Logical Creativity)}, we establish that the physical universe and cognitive reasoning share a common substrate: a discrete Arithmetic Topos. By enforcing a strict scalar associator gap ($\\kappa = -1$) via the Euler-Grothendieck-Penrose (EGP) bridge, we construct local L-spaces that undergo \\'etale descent across the gauge triplet of primes $\\{139, 181, 229\\}$. The characteristic polynomial locks to $X^2 - X - 1 = 0$, establishing the golden ratio as the native algebraic generator."
content = content.replace(old_part_abstract, new_part_abstract)

with open("papers/ARC_Prize_2026_Plazmik_Omnibus.tex", "w") as f:
    f.write(content)
