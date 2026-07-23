with open("scripts/metareal_dec_simulator.py", "r") as f:
    content = f.read()

content = content.replace("Cayley-Dickson 4D Venting", "4D Krein Subspace Exhaust (Negative Norm)")
content = content.replace("shedding catastrophic zero-divisors directly into the $\\mathbb{R}^{16} \\ominus \\mathbb{R}^{12}$ topological sink", "shedding catastrophic zero-divisors into the 4 negative-norm subspaces (Ghost States) of the Krein space, handled by the J-symmetry operator")
content = content.replace("4D Sink Load", "Krein J-Symmetry Load")

with open("scripts/metareal_dec_simulator.py", "w") as f:
    f.write(content)

with open("scripts/metareal_dec_optimizer.py", "r") as f:
    content = f.read()

content = content.replace("Cayley-Dickson 4D Venting", "4D Krein Subspace Exhaust (Negative Norm)")
content = content.replace("shedding catastrophic zero-divisors directly into the $\\mathbb{R}^{16} \\ominus \\mathbb{R}^{12}$ topological sink", "shedding catastrophic zero-divisors into the 4 negative-norm subspaces (Ghost States) of the Krein space, handled by the J-symmetry operator")
content = content.replace("4D Sink Load", "Krein J-Symmetry Load")

with open("scripts/metareal_dec_optimizer.py", "w") as f:
    f.write(content)
